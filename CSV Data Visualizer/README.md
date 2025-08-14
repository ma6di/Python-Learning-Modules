# CSV Data Visualizer 📊

A powerful Python tool for analyzing and visualizing CSV data using pandas, matplotlib, and seaborn. Transform raw data into beautiful, insightful charts with professional styling and statistical analysis.

## ✨ Features

### Data Analysis
- 📊 **CSV Reading**: Load and explore any CSV file with pandas
- 🔍 **Data Exploration**: Automatic data summary, column info, and statistical overview
- 📈 **Multiple Chart Types**: Line plots, bar charts, scatter plots, and distributions
- 🎨 **Professional Styling**: Beautiful seaborn themes and color palettes

### Visualization Capabilities
- 📈 **Time Series Analysis**: Track trends over time with line plots
- 📊 **Comparative Analysis**: Bar charts for comparing quantities
- 🔗 **Correlation Analysis**: Scatter plots with regression lines to find relationships
- 📉 **Distribution Analysis**: Histograms with density curves for pattern recognition
- 🎯 **Multi-Chart Display**: View multiple perspectives of your data simultaneously

### Advanced Features
- 🎨 **Seaborn Integration**: Statistical visualizations with professional aesthetics
- 📊 **Regression Analysis**: Automatic trend lines and correlation detection
- 📈 **Statistical Overlays**: Confidence intervals, density curves, and trend indicators
- 🎯 **Customizable Display**: Adjustable figure sizes, colors, and styling options

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Install Required Packages
```bash
pip3 install pandas matplotlib seaborn numpy
```

## 📖 Usage

### Basic Usage
```bash
cd "CSV Data Visualizer"/
python3 csv_data_visualizer.py
```

### What You'll See
The script automatically:
1. **Loads the Bitcoin price dataset**
2. **Displays data summary** (columns, first 5 rows, statistics)
3. **Creates 6 different visualizations**:
   - Line plot of price trends
   - Bar chart of trading volumes
   - Scatter plot of price vs volume
   - Enhanced seaborn line plot
   - Regression analysis plot
   - Distribution histogram with density curve

## 📊 Sample Dataset

### Bitcoin Price Data (2024)
- **Period**: January 1 - February 29, 2024 (59 data points)
- **Columns**:
  - `Date`: Daily timestamps
  - `Price_USD`: Bitcoin price in US dollars
  - `Volume_24h`: 24-hour trading volume
  - `Market_Cap_Billion`: Market capitalization
  - `Daily_Change_Percent`: Daily price change percentage

### Data Characteristics
- **Price Range**: $42,150 - $96,150 USD
- **Volume Range**: $15.4B - $180.2B daily trading
- **Volatility**: -3.1% to +5.4% daily changes
- **Trend**: Generally upward with realistic market fluctuations

## 🎨 Chart Types Explained

### 1. **Line Plot (matplotlib)**
```python
plt.plot(df['Date'], df['Price_USD'])
```
- **Purpose**: Shows trends over time
- **Best for**: Time series data, tracking changes
- **Example**: Bitcoin price evolution

### 2. **Bar Chart (matplotlib)**
```python
plt.bar(df['Date'][:10], df['Volume_24h'][:10])
```
- **Purpose**: Compares discrete quantities
- **Best for**: Rankings, categorical comparisons
- **Example**: Trading volume by day

### 3. **Scatter Plot (matplotlib)**
```python
plt.scatter(df['Price_USD'], df['Volume_24h'])
```
- **Purpose**: Shows relationships between variables
- **Best for**: Correlation analysis
- **Example**: Price vs volume relationship

### 4. **Enhanced Line Plot (seaborn)**
```python
sns.lineplot(data=df, x='Date', y='Price_USD')
```
- **Purpose**: Professional styling with statistical features
- **Best for**: Publication-ready time series
- **Features**: Clean styling, confidence intervals

### 5. **Regression Plot (seaborn)**
```python
sns.scatterplot() + sns.regplot()
```
- **Purpose**: Correlation with trend line
- **Best for**: Relationship analysis with statistical significance
- **Features**: Automatic regression line, confidence bands

### 6. **Distribution Plot (seaborn)**
```python
sns.histplot(x='Daily_Change_Percent', kde=True)
```
- **Purpose**: Data distribution analysis
- **Best for**: Understanding data patterns and normality
- **Features**: Histogram bins + smooth density curve

## 🧠 Learning Achievements

This project demonstrates mastery of:

### Data Science Libraries
- **pandas**: DataFrame operations, CSV reading, data exploration
- **matplotlib**: Basic plotting, subplots, customization
- **seaborn**: Statistical visualizations, professional styling
- **numpy**: Mathematical operations (automatically included)

### Data Analysis Concepts
- **Exploratory Data Analysis**: Understanding dataset structure and patterns
- **Time Series Analysis**: Tracking changes over time periods
- **Correlation Analysis**: Finding relationships between variables
- **Distribution Analysis**: Understanding data spread and patterns
- **Statistical Visualization**: Professional chart creation with insights

### Python Programming Skills
- **Data Manipulation**: Slicing, filtering, and transforming datasets
- **Visualization Workflow**: From raw data to publication-ready charts
- **Library Integration**: Combining multiple libraries effectively
- **Code Organization**: Clean, readable data analysis scripts

## 🔧 Technical Implementation

### Data Loading and Exploration
```python
df = pd.read_csv('bitcoin_prices.csv')
print(df.head())        # First 5 rows
print(df.info())        # Data types and structure
print(df.describe())    # Statistical summary
```

### Multiple Subplot Creation
```python
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
# Each chart gets its own axis for independent customization
```

### Seaborn Styling
```python
sns.set_style("whitegrid")  # Clean background
sns.set_palette("husl")     # Professional color scheme
```

### Statistical Analysis
```python
sns.regplot(data=df, x='Price_USD', y='Volume_24h')  # Automatic regression
sns.histplot(data=df, x='Daily_Change_Percent', kde=True)  # Distribution + density
```

## 📈 Data Insights You Can Discover

### Trend Analysis
- **Price Evolution**: How Bitcoin price changed over 2 months
- **Volume Patterns**: Which days had highest trading activity
- **Volatility Analysis**: Distribution of daily price changes

### Correlation Analysis
- **Price-Volume Relationship**: Do higher prices correlate with more trading?
- **Market Behavior**: How does trading volume respond to price changes?
- **Statistical Significance**: Is the correlation meaningful?

### Pattern Recognition
- **Seasonal Effects**: Any patterns in specific days/weeks?
- **Outlier Detection**: Unusual price movements or volume spikes
- **Distribution Shape**: Are price changes normally distributed?

## 🎯 Example Output

### Terminal Display
```
📊 Dataset loaded successfully!
📋 Columns available: ['Date', 'Price_USD', 'Volume_24h', 'Market_Cap_Billion', 'Daily_Change_Percent']

🔍 First 5 rows:
        Date   Price_USD  Volume_24h  Market_Cap_Billion  Daily_Change_Percent
0  2024-01-01   42150.50  15420000000               825.2                   2.3
1  2024-01-02   43280.75  18750000000               848.1                   2.7
...

📈 Charts displayed:
  1. Line Plot: Shows price trend over time
  2. Bar Chart: Shows trading volume for first 10 days
  3. Scatter Plot: Shows relationship between price and volume

🎨 Seaborn charts displayed:
  4. Enhanced Line Plot: Cleaner seaborn styling
  5. Regression Plot: Scatter + trend line showing correlation
  6. Distribution Plot: Histogram + density curve of price changes
```

## 🚀 Extending the Project

### Add New Datasets
Replace `bitcoin_prices.csv` with your own data:
- **Stock prices** (Apple, Tesla, etc.)
- **Weather data** (temperature, precipitation)
- **Sales data** (monthly revenue, products)
- **Personal data** (fitness tracking, expenses)

### Add New Chart Types
```python
# Heatmap for correlations
sns.heatmap(df.corr(), annot=True)

# Box plots for distributions
sns.boxplot(data=df, y='Price_USD')

# Pair plots for multiple relationships
sns.pairplot(df)
```

### Add Interactive Features
- Command-line arguments for file selection
- Chart type selection options
- Save charts to files (PNG, PDF)
- Multiple dataset comparison

## 📊 Real-World Applications

- **Financial Analysis**: Stock market trends, crypto analysis
- **Business Intelligence**: Sales performance, customer analytics
- **Scientific Research**: Experimental data visualization
- **Personal Analytics**: Health tracking, expense analysis
- **Market Research**: Survey data analysis and presentation

## 📜 License

This project is open source and available under the MIT License.

---

## 🎉 Project Complete!

You've successfully built a comprehensive data visualization tool that transforms raw CSV data into professional, insightful charts. This project bridges the gap between basic programming and advanced data science capabilities!
