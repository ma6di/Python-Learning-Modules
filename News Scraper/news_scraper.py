import requests
from bs4 import BeautifulSoup
import argparse
import csv
from datetime import datetime


def get_news_url(source):
	"""Get the URL for predefined news sources."""
	urls = {
		'bbc': 'https://www.bbc.com/news',
		'cnn': 'https://www.cnn.com',
		'bbc-sport': 'https://www.bbc.com/sport',
		'reuters': 'https://www.reuters.com',
		'guardian': 'https://www.theguardian.com/uk'
	}
	return urls.get(source.lower())


def save_to_csv(headlines, filename, source_name):
	"""Save headlines to a CSV file."""
	try:
		with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
			writer = csv.writer(csvfile)
			
			# Write header
			writer.writerow(['Number', 'Headline', 'Source', 'Date_Scraped'])
			
			# Write headlines
			current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			for i, headline in enumerate(headlines, 1):
				writer.writerow([i, headline, source_name, current_time])
		
		print(f"💾 Successfully saved {len(headlines)} headlines to '{filename}'")
		return True
		
	except Exception as e:
		print(f"❌ Error saving to CSV: {e}")
		return False


def scrape_headlines(url, limit=10):
	"""Scrape headlines from a given URL."""
	print(f"🔍 Scraping headlines from: {url}")
	
	try:
		response = requests.get(url)
		print(f"✅ Got response: {response.status_code}")
		
		if response.status_code != 200:
			print(f"❌ Error: Website returned status {response.status_code}")
			return []
		
		html_content = response.text
		print(f"📄 HTML length: {len(html_content)} characters")

		soup = BeautifulSoup(html_content, 'html.parser')
		print("🍲 Created soup object")
		
		# Try different selectors to find headlines
		selectors_to_try = [
			('h2', {'class': 'headline'}),
			('h2', {}),  # All h2 tags
			('h3', {}),  # All h3 tags
			('h1', {}),  # All h1 tags
			('.headline', {}),  # Any element with class 'headline'
		]
		
		headlines = []
		for tag, attrs in selectors_to_try:
			if tag.startswith('.'):
				# CSS class selector
				found = soup.find_all(attrs={'class': tag[1:]})
			else:
				# HTML tag selector
				found = soup.find_all(tag, attrs)
			
			if found:
				print(f"🔍 Found {len(found)} headlines using selector: {tag}")
				headlines = found
				break
		
		if not headlines:
			print("❌ No headlines found with any selector")
			return []
		
		# Extract text and limit results
		headline_texts = []
		for headline in headlines[:limit]:
			text = headline.text.strip()
			if text and len(text) > 10:  # Filter out empty or very short text
				headline_texts.append(text)
		
		return headline_texts
		
	except requests.RequestException as e:
		print(f"❌ Network error: {e}")
		return []
	except Exception as e:
		print(f"❌ Error occurred: {e}")
		return []


def main():
	# Create argument parser
	parser = argparse.ArgumentParser(
		description='News Headlines Scraper',
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog="""
Examples:
  python3 news_scraper.py --source bbc --limit 5
  python3 news_scraper.py --url https://www.cnn.com --limit 10 --csv
  python3 news_scraper.py --source bbc-sport --output sports_news.csv
  python3 news_scraper.py --url https://news.ycombinator.com --limit 20 -o tech_news
		"""
	)
	
	# Add arguments
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--source', '-s', 
					  choices=['bbc', 'cnn', 'bbc-sport', 'reuters', 'guardian'],
					  help='Predefined news source')
	group.add_argument('--url', '-u',
					  help='Custom URL to scrape headlines from')
	
	parser.add_argument('--limit', '-l', 
					   type=int, 
					   default=10,
					   help='Number of headlines to fetch (default: 10)')
	
	parser.add_argument('--output', '-o',
					   help='Save headlines to CSV file (e.g., news.csv)')
	
	parser.add_argument('--csv', 
					   action='store_true',
					   help='Save to CSV with auto-generated filename')
	
	# Parse arguments
	args = parser.parse_args()
	
	# Determine URL to use
	if args.source:
		url = get_news_url(args.source)
		if not url:
			print(f"❌ Unknown source: {args.source}")
			return
		print(f"📰 Using predefined source: {args.source}")
		source_name = args.source
	else:
		url = args.url
		print(f"🌐 Using custom URL: {url}")
		# Extract domain name for source
		try:
			from urllib.parse import urlparse
			domain = urlparse(url).netloc
			source_name = domain.replace('www.', '')
		except:
			source_name = 'custom_url'
	
	# Scrape headlines
	headlines = scrape_headlines(url, args.limit)
	
	# Display results
	if headlines:
		print(f"\n📰 Found {len(headlines)} headlines:")
		print("=" * 60)
		for i, headline in enumerate(headlines, 1):
			print(f"{i:2d}. {headline}")
		print("=" * 60)
		
		# Save to CSV if requested
		if args.output or args.csv:
			if args.output:
				filename = args.output
				# Add .csv extension if not present
				if not filename.endswith('.csv'):
					filename += '.csv'
			else:
				# Auto-generate filename
				timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
				filename = f"headlines_{source_name}_{timestamp}.csv"
			
			success = save_to_csv(headlines, filename, source_name)
			if success:
				print(f"📄 You can open '{filename}' in Excel or any spreadsheet app!")
	else:
		print("❌ No headlines found!")


if __name__ == "__main__":
	main()