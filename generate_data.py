import pandas as pd
import json
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('mental_health_tweets.csv')
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')

# Create output directory
import os
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

print("Generating data files for web dashboard...")

# 1. Sentiment data
sentiment_counts = df['sentiment'].value_counts()
sentiment_data = {
    'labels': sentiment_counts.index.tolist(),
    'values': sentiment_counts.values.tolist(),
    'colors': ['#2ecc71', '#e74c3c', '#95a5a6']
}
with open('visualizations/sentiment_data.json', 'w') as f:
    json.dump(sentiment_data, f)
print("✓ Sentiment data")

# 2. Category data
category_counts = df['category'].value_counts()
category_data = {
    'labels': category_counts.index.tolist(),
    'values': category_counts.values.tolist()
}
with open('visualizations/category_data.json', 'w') as f:
    json.dump(category_data, f)
print("✓ Category data")

# 3. Timeline data
timeline_data = df.groupby('year_month').size()
timeline_json = {
    'dates': [str(date) for date in timeline_data.index],
    'counts': timeline_data.values.tolist()
}
with open('visualizations/timeline_data.json', 'w') as f:
    json.dump(timeline_json, f)
print("✓ Timeline data")

# 4. Sentiment timeline
sentiment_timeline = df.groupby(['year_month', 'sentiment']).size().unstack(fill_value=0)
sentiment_timeline_json = {
    'dates': [str(date) for date in sentiment_timeline.index],
    'positive': sentiment_timeline['positive'].tolist() if 'positive' in sentiment_timeline else [],
    'negative': sentiment_timeline['negative'].tolist() if 'negative' in sentiment_timeline else [],
    'neutral': sentiment_timeline['neutral'].tolist() if 'neutral' in sentiment_timeline else []
}
with open('visualizations/sentiment_timeline_data.json', 'w') as f:
    json.dump(sentiment_timeline_json, f)
print("✓ Sentiment timeline data")

# 5. Engagement data
avg_engagement = df.groupby('sentiment')[['likes', 'retweets']].mean()
engagement_data = {
    'sentiments': avg_engagement.index.tolist(),
    'likes': avg_engagement['likes'].tolist(),
    'retweets': avg_engagement['retweets'].tolist()
}
with open('visualizations/engagement_data.json', 'w') as f:
    json.dump(engagement_data, f)
print("✓ Engagement data")

# 6. Location data
location_counts = df['location'].value_counts()
location_data = {
    'labels': location_counts.index.tolist(),
    'values': location_counts.values.tolist()
}
with open('visualizations/location_data.json', 'w') as f:
    json.dump(location_data, f)
print("✓ Location data")

# 7. Category timeline
category_timeline = df.groupby(['year_month', 'category']).size().unstack(fill_value=0)
category_timeline_json = {
    'dates': [str(date) for date in category_timeline.index],
    'categories': {}
}
for col in category_timeline.columns:
    category_timeline_json['categories'][col] = category_timeline[col].tolist()
with open('visualizations/category_timeline_data.json', 'w') as f:
    json.dump(category_timeline_json, f)
print("✓ Category timeline data")

# 8. Summary statistics
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
print("✓ Summary statistics")

print("\n" + "="*60)
print("✅ All data files generated successfully!")
print("="*60)
print(f"\nTotal Tweets: {summary_stats['total_tweets']}")
print(f"Positive: {summary_stats['sentiment_percentages']['positive']}%")
print(f"Negative: {summary_stats['sentiment_percentages']['negative']}%")
print(f"Neutral: {summary_stats['sentiment_percentages']['neutral']}%")
print(f"\n🌐 Ready to open website!")
