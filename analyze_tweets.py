import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import json
from collections import Counter
import re
from datetime import datetime

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load the dataset
df = pd.read_csv('mental_health_tweets.csv')
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')

# Create output directory for visualizations
import os
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

print("Dataset loaded successfully!")
print(f"Total tweets: {len(df)}")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
print("\n" + "="*50 + "\n")

# 1. Sentiment Distribution
print("Generating Sentiment Distribution...")
sentiment_counts = df['sentiment'].value_counts()
plt.figure(figsize=(10, 6))
colors = {'positive': '#2ecc71', 'negative': '#e74c3c', 'neutral': '#95a5a6'}
sentiment_colors = [colors[sent] for sent in sentiment_counts.index]
plt.bar(sentiment_counts.index, sentiment_counts.values, color=sentiment_colors, edgecolor='black', linewidth=1.5)
plt.title('Distribution of Tweet Sentiments', fontsize=16, fontweight='bold')
plt.xlabel('Sentiment', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.grid(axis='y', alpha=0.3)
for i, v in enumerate(sentiment_counts.values):
    plt.text(i, v + 1, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/sentiment_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Save data for web visualization
sentiment_data = {
    'labels': sentiment_counts.index.tolist(),
    'values': sentiment_counts.values.tolist(),
    'colors': sentiment_colors
}
with open('visualizations/sentiment_data.json', 'w') as f:
    json.dump(sentiment_data, f)

# 2. Category Distribution
print("Generating Category Distribution...")
category_counts = df['category'].value_counts()
plt.figure(figsize=(12, 6))
colors_cat = plt.cm.Set3(range(len(category_counts)))
plt.barh(category_counts.index, category_counts.values, color=colors_cat, edgecolor='black')
plt.title('Mental Health Categories in Tweets', fontsize=16, fontweight='bold')
plt.xlabel('Number of Tweets', fontsize=12)
plt.ylabel('Category', fontsize=12)
plt.grid(axis='x', alpha=0.3)
for i, v in enumerate(category_counts.values):
    plt.text(v + 0.5, i, str(v), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/category_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Save data for web
category_data = {
    'labels': category_counts.index.tolist(),
    'values': category_counts.values.tolist()
}
with open('visualizations/category_data.json', 'w') as f:
    json.dump(category_data, f)

# 3. Timeline Analysis - Tweets over time
print("Generating Timeline Analysis...")
timeline_data = df.groupby('year_month').size()
plt.figure(figsize=(14, 6))
timeline_data.plot(kind='line', marker='o', linewidth=2, markersize=8, color='#3498db')
plt.title('Mental Health Tweet Volume Over Time (2020-2022)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/timeline_tweets.png', dpi=300, bbox_inches='tight')
plt.close()

# Save timeline data
timeline_json = {
    'dates': [str(date) for date in timeline_data.index],
    'counts': timeline_data.values.tolist()
}
with open('visualizations/timeline_data.json', 'w') as f:
    json.dump(timeline_json, f)

# 4. Sentiment Timeline
print("Generating Sentiment Timeline...")
sentiment_timeline = df.groupby(['year_month', 'sentiment']).size().unstack(fill_value=0)
plt.figure(figsize=(14, 6))
sentiment_timeline.plot(kind='area', stacked=True, 
                        color=['#2ecc71', '#e74c3c', '#95a5a6'],
                        alpha=0.7)
plt.title('Sentiment Trends Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.legend(title='Sentiment', loc='upper left')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/sentiment_timeline.png', dpi=300, bbox_inches='tight')
plt.close()

# Save sentiment timeline data
sentiment_timeline_json = {
    'dates': [str(date) for date in sentiment_timeline.index],
    'positive': sentiment_timeline['positive'].tolist() if 'positive' in sentiment_timeline else [],
    'negative': sentiment_timeline['negative'].tolist() if 'negative' in sentiment_timeline else [],
    'neutral': sentiment_timeline['neutral'].tolist() if 'neutral' in sentiment_timeline else []
}
with open('visualizations/sentiment_timeline_data.json', 'w') as f:
    json.dump(sentiment_timeline_json, f)

# 5. Engagement Analysis
print("Generating Engagement Analysis...")
avg_engagement = df.groupby('sentiment')[['likes', 'retweets']].mean()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Likes
avg_engagement['likes'].plot(kind='bar', ax=ax1, color=['#2ecc71', '#e74c3c', '#95a5a6'], edgecolor='black')
ax1.set_title('Average Likes by Sentiment', fontsize=14, fontweight='bold')
ax1.set_xlabel('Sentiment', fontsize=12)
ax1.set_ylabel('Average Likes', fontsize=12)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0)
ax1.grid(axis='y', alpha=0.3)

# Retweets
avg_engagement['retweets'].plot(kind='bar', ax=ax2, color=['#2ecc71', '#e74c3c', '#95a5a6'], edgecolor='black')
ax2.set_title('Average Retweets by Sentiment', fontsize=14, fontweight='bold')
ax2.set_xlabel('Sentiment', fontsize=12)
ax2.set_ylabel('Average Retweets', fontsize=12)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=0)
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('visualizations/engagement_analysis.png', dpi=300, bbox_inches='tight')
plt.close()

# Save engagement data
engagement_data = {
    'sentiments': avg_engagement.index.tolist(),
    'likes': avg_engagement['likes'].tolist(),
    'retweets': avg_engagement['retweets'].tolist()
}
with open('visualizations/engagement_data.json', 'w') as f:
    json.dump(engagement_data, f)

# 6. Word Cloud for each sentiment
print("Generating Word Clouds...")
for sentiment in ['positive', 'negative', 'neutral']:
    text = ' '.join(df[df['sentiment'] == sentiment]['tweet_text'].values)
    # Remove URLs, mentions, hashtags for cleaner wordcloud
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|#', '', text)
    
    if sentiment == 'positive':
        colormap = 'Greens'
    elif sentiment == 'negative':
        colormap = 'Reds'
    else:
        colormap = 'Greys'
    
    wordcloud = WordCloud(width=800, height=400, 
                          background_color='white',
                          colormap=colormap,
                          max_words=100).generate(text)
    
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud - {sentiment.capitalize()} Tweets', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig(f'visualizations/wordcloud_{sentiment}.png', dpi=300, bbox_inches='tight')
    plt.close()

# 7. Location Distribution
print("Generating Location Distribution...")
location_counts = df['location'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(location_counts.values, labels=location_counts.index, autopct='%1.1f%%',
        startangle=90, colors=plt.cm.Set3(range(len(location_counts))))
plt.title('Tweet Distribution by Location', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('visualizations/location_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Save location data
location_data = {
    'labels': location_counts.index.tolist(),
    'values': location_counts.values.tolist()
}
with open('visualizations/location_data.json', 'w') as f:
    json.dump(location_data, f)

# 8. Monthly Category Trends
print("Generating Monthly Category Trends...")
category_timeline = df.groupby(['year_month', 'category']).size().unstack(fill_value=0)
plt.figure(figsize=(14, 8))
category_timeline.plot(kind='line', marker='o', linewidth=2, markersize=6)
plt.title('Mental Health Category Trends Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Number of Tweets', fontsize=12)
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('visualizations/category_timeline.png', dpi=300, bbox_inches='tight')
plt.close()

# Save category timeline data
category_timeline_json = {
    'dates': [str(date) for date in category_timeline.index],
    'categories': {}
}
for col in category_timeline.columns:
    category_timeline_json['categories'][col] = category_timeline[col].tolist()
with open('visualizations/category_timeline_data.json', 'w') as f:
    json.dump(category_timeline_json, f)

# 9. Generate Summary Statistics
print("\nGenerating Summary Statistics...")
summary_stats = {
    'total_tweets': len(df),
    'date_range': {
        'start': df['date'].min().strftime('%Y-%m-%d'),
        'end': df['date'].max().strftime('%Y-%m-%d')
    },
    'sentiment_distribution': {
        'positive': int(df[df['sentiment'] == 'positive'].shape[0]),
        'negative': int(df[df['sentiment'] == 'negative'].shape[0]),
        'neutral': int(df[df['sentiment'] == 'neutral'].shape[0])
    },
    'sentiment_percentages': {
        'positive': round(df[df['sentiment'] == 'positive'].shape[0] / len(df) * 100, 1),
        'negative': round(df[df['sentiment'] == 'negative'].shape[0] / len(df) * 100, 1),
        'neutral': round(df[df['sentiment'] == 'neutral'].shape[0] / len(df) * 100, 1)
    },
    'top_categories': df['category'].value_counts().head(5).to_dict(),
    'total_engagement': {
        'likes': int(df['likes'].sum()),
        'retweets': int(df['retweets'].sum())
    },
    'avg_engagement': {
        'likes': round(df['likes'].mean(), 2),
        'retweets': round(df['retweets'].mean(), 2)
    },
    'locations': df['location'].value_counts().to_dict()
}

with open('visualizations/summary_stats.json', 'w') as f:
    json.dump(summary_stats, f, indent=2)

print("\n" + "="*50)
print("Analysis Complete!")
print("="*50)
print(f"\nAll visualizations saved in 'visualizations/' folder")
print(f"JSON data files created for web dashboard")
print("\nSummary Statistics:")
print(f"- Total Tweets: {summary_stats['total_tweets']}")
print(f"- Positive: {summary_stats['sentiment_percentages']['positive']}%")
print(f"- Negative: {summary_stats['sentiment_percentages']['negative']}%")
print(f"- Neutral: {summary_stats['sentiment_percentages']['neutral']}%")
print(f"- Total Likes: {summary_stats['total_engagement']['likes']:,}")
print(f"- Total Retweets: {summary_stats['total_engagement']['retweets']:,}")
