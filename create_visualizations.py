import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

# Create visualizations folder
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Load data
df = pd.read_csv('mental_health_tweets.csv')
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')

print("Creating Data Visualizations...")
print("="*60)

# 1. SENTIMENT DISTRIBUTION
print("1. Creating Sentiment Distribution chart...")
sentiment_counts = df['sentiment'].value_counts()
colors = {'positive': '#2ecc71', 'negative': '#e74c3c', 'neutral': '#95a5a6'}
sentiment_colors = [colors[sent] for sent in sentiment_counts.index]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.bar(sentiment_counts.index, sentiment_counts.values, color=sentiment_colors, edgecolor='black', linewidth=2)
ax1.set_title('Sentiment Distribution', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Sentiment', fontsize=13)
ax1.set_ylabel('Number of Tweets', fontsize=13)
for i, v in enumerate(sentiment_counts.values):
    ax1.text(i, v + 1, str(v), ha='center', fontweight='bold', fontsize=12)

ax2.pie(sentiment_counts.values, labels=sentiment_counts.index, autopct='%1.1f%%',
        colors=sentiment_colors, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
ax2.set_title('Sentiment Percentage', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('visualizations/1_sentiment_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. TIMELINE ANALYSIS
print("2. Creating Timeline Analysis chart...")
timeline_data = df.groupby('year_month').size()
plt.figure(figsize=(14, 6))
timeline_data.plot(kind='line', marker='o', linewidth=3, markersize=10, color='#3498db')
plt.title('Mental Health Tweet Volume Over Time (2020-2022)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=13)
plt.ylabel('Number of Tweets', fontsize=13)
plt.axhline(y=timeline_data.mean(), color='red', linestyle='--', linewidth=2, 
            label=f'Average: {timeline_data.mean():.1f}')
plt.grid(True, alpha=0.4)
plt.xticks(rotation=45)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig('visualizations/2_timeline_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. SENTIMENT TRENDS OVER TIME
print("3. Creating Sentiment Trends Over Time chart...")
sentiment_timeline = df.groupby(['year_month', 'sentiment']).size().unstack(fill_value=0)
plt.figure(figsize=(14, 6))
sentiment_timeline.plot(kind='area', stacked=True, 
                        color=['#2ecc71', '#e74c3c', '#95a5a6'], alpha=0.8)
plt.title('Sentiment Trends Over Time', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=13)
plt.ylabel('Number of Tweets', fontsize=13)
plt.legend(title='Sentiment', loc='upper left', fontsize=11)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/3_sentiment_timeline.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. CATEGORY DISTRIBUTION
print("4. Creating Category Distribution chart...")
category_counts = df['category'].value_counts()
plt.figure(figsize=(12, 8))
colors_cat = plt.cm.Set3(range(len(category_counts)))
plt.barh(category_counts.index, category_counts.values, color=colors_cat, edgecolor='black', linewidth=1.5)
plt.title('Mental Health Categories Distribution', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Number of Tweets', fontsize=13)
plt.ylabel('Category', fontsize=13)
plt.grid(axis='x', alpha=0.3)
for i, v in enumerate(category_counts.values):
    plt.text(v + 0.3, i, str(v), va='center', fontweight='bold', fontsize=11)
plt.tight_layout()
plt.savefig('visualizations/4_category_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. CATEGORY TRENDS OVER TIME
print("5. Creating Category Trends Over Time chart...")
category_timeline = df.groupby(['year_month', 'category']).size().unstack(fill_value=0)
plt.figure(figsize=(14, 8))
for category in category_timeline.columns:
    category_timeline[category].plot(kind='line', marker='o', linewidth=2.5, markersize=7, label=category)
plt.title('Mental Health Category Trends Over Time', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Month', fontsize=13)
plt.ylabel('Number of Tweets', fontsize=13)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/5_category_timeline.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. ENGAGEMENT ANALYSIS
print("6. Creating Engagement Analysis chart...")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

avg_likes = df.groupby('sentiment')['likes'].mean()
axes[0, 0].bar(avg_likes.index, avg_likes.values, color=['#2ecc71', '#e74c3c', '#95a5a6'], edgecolor='black', linewidth=1.5)
axes[0, 0].set_title('Average Likes by Sentiment', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Average Likes', fontsize=12)
axes[0, 0].grid(axis='y', alpha=0.3)

avg_retweets = df.groupby('sentiment')['retweets'].mean()
axes[0, 1].bar(avg_retweets.index, avg_retweets.values, color=['#2ecc71', '#e74c3c', '#95a5a6'], edgecolor='black', linewidth=1.5)
axes[0, 1].set_title('Average Retweets by Sentiment', fontsize=14, fontweight='bold')
axes[0, 1].set_ylabel('Average Retweets', fontsize=12)
axes[0, 1].grid(axis='y', alpha=0.3)

engagement_data = df.groupby('sentiment')[['likes', 'retweets']].mean()
x = range(len(engagement_data))
width = 0.35
axes[1, 0].bar([i - width/2 for i in x], engagement_data['likes'], width, label='Likes', color='#3498db', edgecolor='black')
axes[1, 0].bar([i + width/2 for i in x], engagement_data['retweets'], width, label='Retweets', color='#e67e22', edgecolor='black')
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(engagement_data.index)
axes[1, 0].set_title('Engagement Comparison', fontsize=14, fontweight='bold')
axes[1, 0].set_ylabel('Average Count', fontsize=12)
axes[1, 0].legend(fontsize=11)
axes[1, 0].grid(axis='y', alpha=0.3)

axes[1, 1].scatter(df['likes'], df['retweets'], 
                   c=df['sentiment'].map({'positive': '#2ecc71', 'negative': '#e74c3c', 'neutral': '#95a5a6'}), 
                   alpha=0.6, s=100, edgecolor='black', linewidth=1)
axes[1, 1].set_title('Likes vs Retweets', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Likes', fontsize=12)
axes[1, 1].set_ylabel('Retweets', fontsize=12)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('visualizations/6_engagement_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. GEOGRAPHIC DISTRIBUTION
print("7. Creating Geographic Distribution chart...")
location_counts = df['location'].value_counts()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

colors_loc = plt.cm.Set3(range(len(location_counts)))
ax1.pie(location_counts.values, labels=location_counts.index, autopct='%1.1f%%',
        colors=colors_loc, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
ax1.set_title('Geographic Distribution (Pie)', fontsize=14, fontweight='bold')

ax2.bar(location_counts.index, location_counts.values, color=colors_loc, edgecolor='black', linewidth=1.5)
ax2.set_title('Geographic Distribution (Bar)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Location', fontsize=12)
ax2.set_ylabel('Number of Tweets', fontsize=12)
ax2.grid(axis='y', alpha=0.3)
for i, v in enumerate(location_counts.values):
    ax2.text(i, v + 0.5, str(v), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/7_geographic_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. WORD CLOUDS
print("8. Creating Word Clouds...")
def clean_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|#', '', text)
    return text

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
sentiments = ['positive', 'negative', 'neutral']
colormaps = ['Greens', 'Reds', 'Greys']

for idx, (sentiment, colormap) in enumerate(zip(sentiments, colormaps)):
    text = ' '.join(df[df['sentiment'] == sentiment]['tweet_text'].values)
    text = clean_text(text)
    wordcloud = WordCloud(width=600, height=400, background_color='white',
                          colormap=colormap, max_words=60).generate(text)
    axes[idx].imshow(wordcloud, interpolation='bilinear')
    axes[idx].axis('off')
    axes[idx].set_title(f'{sentiment.capitalize()} Tweets Word Cloud', 
                       fontsize=14, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('visualizations/8_word_clouds.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. SENTIMENT BY CATEGORY HEATMAP
print("9. Creating Sentiment by Category Heatmap...")
sentiment_by_category = pd.crosstab(df['category'], df['sentiment'], normalize='index') * 100
plt.figure(figsize=(10, 8))
sns.heatmap(sentiment_by_category, annot=True, fmt='.1f', cmap='RdYlGn', 
            cbar_kws={'label': 'Percentage (%)'}, linewidths=2, linecolor='black')
plt.title('Sentiment Distribution by Category (%)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Sentiment', fontsize=13)
plt.ylabel('Category', fontsize=13)
plt.tight_layout()
plt.savefig('visualizations/9_sentiment_category_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 10. SUMMARY DASHBOARD
print("10. Creating Summary Dashboard...")
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Title
fig.suptitle('Mental Health Tweets Analysis - Summary Dashboard', 
             fontsize=20, fontweight='bold', y=0.98)

# Sentiment Distribution
ax1 = fig.add_subplot(gs[0, :2])
sentiment_counts.plot(kind='bar', ax=ax1, color=sentiment_colors, edgecolor='black', linewidth=1.5)
ax1.set_title('Sentiment Distribution', fontsize=13, fontweight='bold')
ax1.set_ylabel('Count')
ax1.grid(axis='y', alpha=0.3)

# Stats Box
ax2 = fig.add_subplot(gs[0, 2])
ax2.axis('off')
stats_text = f"""
KEY STATISTICS

Total Tweets: {len(df)}

Positive: {len(df[df['sentiment']=='positive'])}
Negative: {len(df[df['sentiment']=='negative'])}
Neutral: {len(df[df['sentiment']=='neutral'])}

Total Likes: {df['likes'].sum():,}
Total Retweets: {df['retweets'].sum():,}

Avg Likes: {df['likes'].mean():.1f}
Avg Retweets: {df['retweets'].mean():.1f}
"""
ax2.text(0.1, 0.5, stats_text, fontsize=11, verticalalignment='center',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Category Distribution
ax3 = fig.add_subplot(gs[1, :])
category_counts.head(8).plot(kind='barh', ax=ax3, color=plt.cm.Set3(range(8)), edgecolor='black')
ax3.set_title('Top Mental Health Categories', fontsize=13, fontweight='bold')
ax3.set_xlabel('Count')
ax3.grid(axis='x', alpha=0.3)

# Timeline
ax4 = fig.add_subplot(gs[2, :])
timeline_data.plot(kind='line', ax=ax4, marker='o', linewidth=2, markersize=6, color='#3498db')
ax4.set_title('Tweet Volume Timeline', fontsize=13, fontweight='bold')
ax4.set_xlabel('Month')
ax4.set_ylabel('Count')
ax4.grid(True, alpha=0.3)
plt.xticks(rotation=45)

plt.savefig('visualizations/10_summary_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "="*60)
print("✅ ALL VISUALIZATIONS CREATED SUCCESSFULLY!")
print("="*60)
print(f"\n📁 Location: visualizations/ folder")
print(f"📊 Total Files: 10 high-quality PNG images")
print("\nFiles created:")
for i in range(1, 11):
    files = [f for f in os.listdir('visualizations') if f.startswith(f'{i}_') and f.endswith('.png')]
    if files:
        print(f"  ✓ {files[0]}")
print("\n🎉 Ready to show to your teacher!")
