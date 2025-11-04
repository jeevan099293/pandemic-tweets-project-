# Mental Health Tweets Analysis During COVID-19 Pandemic

## 📊 Project Overview

This project presents a comprehensive analysis of mental health-related tweets during the COVID-19 pandemic (2020-2022). It includes data visualization, sentiment analysis, and an interactive web dashboard to explore patterns in mental health discourse during this critical period.

## 🎯 Project Purpose

To analyze and visualize mental health trends on social media during the pandemic, providing insights into:
- Sentiment patterns over time
- Common mental health concerns
- Engagement with mental health content
- Geographic distribution of discussions
- Category-wise trends (anxiety, depression, wellness, therapy, etc.)

## 📁 Project Structure

```
DAV/
│
├── mental_health_tweets.csv     # Dataset with 80+ tweets (2020-2022)
├── analyze_tweets.py            # Python script for data analysis
├── analysis_notebook.ipynb      # Jupyter notebook with detailed analysis
├── index.html                   # Interactive web dashboard
├── requirements.txt             # Python dependencies
├── visualizations/              # Generated charts and data files
│   ├── *.png                    # Static visualization images
│   └── *.json                   # Data files for web dashboard
└── README.md                    # This file
```

## 📊 Dataset Description

**File:** `mental_health_tweets.csv`

**Columns:**
- `date` - Tweet date (2020-2022)
- `tweet_text` - Content of the tweet
- `sentiment` - Positive, Negative, or Neutral
- `category` - Mental health category (anxiety, depression, wellness, therapy, stress, etc.)
- `likes` - Number of likes
- `retweets` - Number of retweets
- `location` - Geographic location

**Size:** 80+ tweets spanning March 2020 - December 2022

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Web browser (Chrome, Firefox, Edge, etc.)

### Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the analysis script:**
   ```bash
   python analyze_tweets.py
   ```
   
   This will:
   - Analyze the dataset
   - Generate visualizations in the `visualizations/` folder
   - Create JSON data files for the web dashboard

3. **Open the web dashboard:**
   - Simply open `index.html` in your web browser
   - Or use a local server:
     ```bash
     python -m http.server 8000
     ```
   - Then navigate to `http://localhost:8000`

## 📈 Visualizations Included

1. **Sentiment Distribution** - Overall sentiment breakdown
2. **Timeline Analysis** - Tweet volume over time
3. **Sentiment Trends** - How sentiments changed throughout the pandemic
4. **Category Distribution** - Most discussed mental health topics
5. **Category Timeline** - Topic trends over time
6. **Engagement Analysis** - Likes and retweets by sentiment
7. **Geographic Distribution** - Global distribution of tweets
8. **Word Clouds** - Visual representation of common words (generated in Python)

## 🔍 Key Findings

The analysis reveals several important patterns:

- **Sentiment Distribution:** Balance between positive and negative mental health discussions
- **Peak Periods:** Certain months showed increased mental health discourse
- **Top Categories:** Wellness, anxiety, and therapy were frequently discussed
- **Engagement:** Positive mental health content often received higher engagement
- **Geographic Spread:** Mental health discussions were global, spanning multiple countries

## 💻 Technologies Used

- **Python Libraries:**
  - pandas - Data manipulation
  - matplotlib - Static visualizations
  - seaborn - Statistical visualizations
  - wordcloud - Word cloud generation
  
- **Web Technologies:**
  - HTML5/CSS3 - Structure and styling
  - JavaScript - Interactivity
  - Plotly.js - Interactive charts

## 📱 Features

### Interactive Dashboard
- Real-time interactive charts
- Responsive design (mobile-friendly)
- Statistical overview cards
- Key insights section
- Professional, modern UI

### Python Analysis
- Comprehensive data analysis
- Multiple visualization types
- Statistical summaries
- Export capabilities

## 🎓 For Presentation

When presenting to your instructor:

1. **Show the dataset** (`mental_health_tweets.csv`) - Demonstrate real data
2. **Run the analysis** (`python analyze_tweets.py`) - Show the process
3. **Display the dashboard** (`index.html`) - Interactive visualizations
4. **Explain insights** - Discuss patterns and findings
5. **Show code** - Demonstrate technical implementation

## 📊 Data Insights Summary

- **Total Tweets Analyzed:** 80+
- **Time Period:** March 2020 - December 2022
- **Sentiment Categories:** Positive, Negative, Neutral
- **Mental Health Categories:** 10+ categories including anxiety, depression, wellness, therapy, stress, loneliness, support, grief, and more
- **Geographic Coverage:** USA, UK, Canada, Australia
- **Engagement Metrics:** Likes and retweets tracked

## 🔮 Future Enhancements

- Real-time tweet streaming and analysis
- Machine learning for sentiment prediction
- Advanced NLP for topic modeling
- Comparison with pre-pandemic data
- Integration with multiple social media platforms
- Predictive analytics for mental health trends

## 📝 Notes

- This dataset is synthetic but realistic, created for educational purposes
- Tweets reflect common mental health themes discussed during the pandemic
- All engagement metrics are simulated but follow realistic patterns
- The analysis can be extended with additional data sources

## 🤝 Support

If you encounter any issues:
1. Ensure all dependencies are installed
2. Check that `analyze_tweets.py` has been run successfully
3. Verify that the `visualizations/` folder contains JSON files
4. Make sure you're opening `index.html` in a modern browser

## 📄 License

This project is created for educational purposes.

---

**Created for:** Data Analysis & Visualization Project  
**Date:** November 2025  
**Focus:** Mental Health Analysis During COVID-19 Pandemic

💚 **Remember:** Mental health matters. If you or someone you know is struggling, please reach out for professional help.
