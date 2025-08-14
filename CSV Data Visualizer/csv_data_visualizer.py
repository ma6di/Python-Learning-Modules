import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style for better-looking plots
sns.set_style("whitegrid")  # Clean background with grid
sns.set_palette("husl")     # Beautiful color palette


def main():
	df = pd.read_csv('bitcoin_prices.csv')
	print("📊 Dataset loaded successfully!")
	print(f"📋 Columns available: {list(df.columns)}")
	print("\n🔍 First 5 rows:")
	print(df.head())
	
	# Create 3 charts in one window
	fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))  # 1 row, 3 columns
	
	# Chart 1: Line Plot - Bitcoin Price Over Time
	ax1.plot(df['Date'], df['Price_USD'], linewidth=2, color='orange')
	ax1.set_title('Bitcoin Price Over Time', fontsize=14, fontweight='bold')
	ax1.set_xlabel('Date')
	ax1.set_ylabel('Price (USD)')
	ax1.tick_params(axis='x', rotation=45)
	ax1.grid(True, alpha=0.3)
	
	# Chart 2: Bar Chart - Trading Volume (first 10 days)
	ax2.bar(df['Date'][:10], df['Volume_24h'][:10], color='skyblue', alpha=0.7)
	ax2.set_title('Trading Volume (First 10 Days)', fontsize=14, fontweight='bold')
	ax2.set_xlabel('Date')
	ax2.set_ylabel('Volume (24h)')
	ax2.tick_params(axis='x', rotation=45)
	
	# Chart 3: Scatter Plot - Price vs Volume Relationship
	ax3.scatter(df['Price_USD'], df['Volume_24h'], color='green', alpha=0.6)
	ax3.set_title('Price vs Volume Correlation', fontsize=14, fontweight='bold')
	ax3.set_xlabel('Price (USD)')
	ax3.set_ylabel('Volume (24h)')
	ax3.grid(True, alpha=0.3)
	
	# Adjust layout to prevent overlap
	plt.tight_layout()
	plt.show()
	
	print("\n📈 Charts displayed:")
	print("  1. Line Plot: Shows price trend over time")
	print("  2. Bar Chart: Shows trading volume for first 10 days") 
	print("  3. Scatter Plot: Shows relationship between price and volume")
	
	# Now let's create some SEABORN charts!
	print("\n🎨 Creating beautiful Seaborn visualizations...")
	
	# Create 2 more advanced charts using Seaborn
	fig2, (ax4, ax5) = plt.subplots(1, 2, figsize=(15, 6))
	
	# Chart 4: Seaborn Line Plot with confidence intervals
	sns.lineplot(data=df, x='Date', y='Price_USD', ax=ax4, linewidth=3)
	ax4.set_title('Bitcoin Price Trend (Seaborn Style)', fontsize=14, fontweight='bold')
	ax4.tick_params(axis='x', rotation=45)
	
	# Chart 5: Seaborn Scatter Plot with regression line
	sns.scatterplot(data=df, x='Price_USD', y='Volume_24h', ax=ax5, s=80, alpha=0.7)
	sns.regplot(data=df, x='Price_USD', y='Volume_24h', ax=ax5, scatter=False, color='red')
	ax5.set_title('Price vs Volume with Trend Line', fontsize=14, fontweight='bold')
	
	plt.tight_layout()
	plt.show()
	
	# Chart 6: Distribution Plot - Daily Price Changes
	plt.figure(figsize=(10, 6))
	sns.histplot(data=df, x='Daily_Change_Percent', bins=20, kde=True)
	plt.title('Distribution of Daily Price Changes', fontsize=16, fontweight='bold')
	plt.xlabel('Daily Change (%)')
	plt.ylabel('Frequency')
	plt.axvline(x=0, color='red', linestyle='--', alpha=0.7, label='No Change Line')
	plt.legend()
	plt.show()
	
	print("\n🎨 Seaborn charts displayed:")
	print("  4. Enhanced Line Plot: Cleaner seaborn styling")
	print("  5. Regression Plot: Scatter + trend line showing correlation") 
	print("  6. Distribution Plot: Histogram + density curve of price changes")


if __name__ == "__main__":
    main()