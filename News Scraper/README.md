# News Headlines Scraper

A powerful command-line tool for scraping news headlines from various websites and exporting them to CSV format. Built with Python using web scraping, argument parsing, and data export techniques.

## ✨ Features

### Core Functionality
- 🌐 **Web Scraping**: Extract headlines from any news website using requests and BeautifulSoup
- 📰 **Multiple Sources**: Pre-configured popular news sources (BBC, CNN, Reuters, Guardian)
- 🔗 **Custom URLs**: Scrape headlines from any website URL
- 📊 **CSV Export**: Save headlines to CSV files for analysis in Excel or other tools
- 🎯 **Flexible Limits**: Control how many headlines to fetch (1-1000+)

### Command-Line Interface
- 🛠️ **Professional CLI**: Built with argparse for robust command-line interaction
- ⚡ **Quick Commands**: Short and long argument forms (-s vs --source)
- 📝 **Auto-generated Help**: Built-in help documentation with examples
- 🔒 **Input Validation**: Validates arguments and provides clear error messages

### Data Export
- 💾 **Multiple CSV Options**: Custom filenames or auto-generated timestamps
- 📋 **Structured Data**: Organized columns (Number, Headline, Source, Date)
- 🌍 **UTF-8 Support**: Handles international characters and emojis
- 📅 **Timestamps**: Records when each scraping session occurred

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Install Required Packages
```bash
pip3 install requests beautifulsoup4
```

## 📖 Usage

### Basic Commands

#### Get Help
```bash
python3 news_scraper.py --help
```

#### Scrape from Predefined Sources
```bash
# BBC News (10 headlines by default)
python3 news_scraper.py --source bbc

# CNN with custom limit
python3 news_scraper.py --source cnn --limit 5

# BBC Sport
python3 news_scraper.py --source bbc-sport --limit 15
```

#### Scrape from Custom URLs
```bash
# Any news website
python3 news_scraper.py --url https://www.reuters.com --limit 20

# Tech news
python3 news_scraper.py --url https://news.ycombinator.com
```

### CSV Export Options

#### Save with Custom Filename
```bash
# Custom filename (adds .csv automatically)
python3 news_scraper.py --source bbc --output today_news

# Specific filename
python3 news_scraper.py --source cnn --output headlines.csv --limit 10
```

#### Auto-generated Filenames
```bash
# Creates: headlines_bbc_20250813_143022.csv
python3 news_scraper.py --source bbc --csv

# Creates: headlines_cnn.com_20250813_144530.csv
python3 news_scraper.py --url https://www.cnn.com --csv --limit 15
```

### Short Form Arguments
```bash
# Quick commands with short flags
python3 news_scraper.py -s bbc -l 5 -o news.csv
python3 news_scraper.py -u https://www.guardian.com -l 10 --csv
```

## 🏗️ Command Reference

### Required Arguments (choose one)
- `--source, -s`: Choose from predefined sources
  - Options: `bbc`, `cnn`, `bbc-sport`, `reuters`, `guardian`
- `--url, -u`: Custom website URL to scrape

### Optional Arguments
- `--limit, -l`: Number of headlines to fetch (default: 10)
- `--output, -o`: Save to specific CSV filename
- `--csv`: Save with auto-generated filename
- `--help, -h`: Show help message and exit

## 📊 CSV Output Format

The exported CSV file contains:

| Column | Description | Example |
|--------|-------------|---------|
| Number | Sequential numbering | 1, 2, 3... |
| Headline | The news headline text | "Breaking News: Tech Update" |
| Source | Website or source name | bbc, cnn, reuters.com |
| Date_Scraped | When the data was collected | 2025-08-13 21:36:04 |

## 🌐 Supported Sources

### Pre-configured Sources
- **BBC**: `https://www.bbc.com/news`
- **CNN**: `https://www.cnn.com`
- **BBC Sport**: `https://www.bbc.com/sport`
- **Reuters**: `https://www.reuters.com`
- **Guardian**: `https://www.theguardian.com/uk`

### Custom Sources
Any website can be scraped using the `--url` parameter. The scraper intelligently tries multiple HTML selectors to find headlines.

## 🧠 Learning Achievements

This project demonstrates mastery of:

### Python Libraries
- **requests**: HTTP requests and web communication
- **BeautifulSoup**: HTML parsing and element selection
- **argparse**: Professional command-line interface design
- **csv**: Data export and file formatting
- **datetime**: Timestamp generation and formatting

### Web Scraping Concepts
- **HTTP Status Codes**: Understanding 200, 404, 500 responses
- **HTML Selectors**: Finding elements by tag, class, and attributes
- **Error Handling**: Network timeouts, missing elements, malformed HTML
- **Data Cleaning**: Filtering empty text and formatting output

### Software Development
- **CLI Design**: User-friendly command-line interfaces
- **Error Management**: Graceful failure handling with helpful messages
- **Code Organization**: Functions, documentation, and modularity
- **Data Validation**: Input checking and argument validation

## 🔧 Technical Implementation

### Smart Headline Detection
The scraper tries multiple strategies to find headlines:
1. `<h2>` tags with class "headline"
2. All `<h2>` tags
3. All `<h3>` tags
4. All `<h1>` tags
5. Any element with class "headline"

### Error Handling
- Network connection issues
- Invalid URLs
- HTTP error responses
- Missing HTML elements
- File writing permissions

### Data Processing
- Text cleaning and whitespace removal
- Minimum length filtering (excludes very short text)
- UTF-8 encoding for international support
- Automatic timestamp generation

## 📝 Example Output

### Terminal Output
```
🔍 Scraping headlines from: https://www.cnn.com
✅ Got response: 200
📄 HTML length: 157823 characters
🍲 Created soup object
🔍 Found 45 headlines using selector: h2

📰 Found 5 headlines:
============================================================
 1. Trump vows 'severe consequences' if Putin doesn't agree to end war
 2. Major climate summit reaches historic agreement
 3. Tech giants announce AI safety partnership
 4. Global markets surge on economic optimism
 5. Scientists discover breakthrough in renewable energy
============================================================
💾 Successfully saved 5 headlines to 'today_headlines.csv'
📄 You can open 'today_headlines.csv' in Excel or any spreadsheet app!
```

### CSV File Content
```csv
Number,Headline,Source,Date_Scraped
1,"Trump vows 'severe consequences' if Putin doesn't agree to end war",cnn,2025-08-13 21:36:04
2,"Major climate summit reaches historic agreement",cnn,2025-08-13 21:36:04
3,"Tech giants announce AI safety partnership",cnn,2025-08-13 21:36:04
```

## 🚨 Important Notes

### Ethical Web Scraping
- Respect website terms of service
- Don't overwhelm servers with too many requests
- Check robots.txt files when appropriate
- Use scraped data responsibly

### Limitations
- Some websites may block automated requests
- Dynamic content (JavaScript-loaded) might not be captured
- HTML structure changes can affect scraping success
- Rate limiting may apply to frequent requests

## 🎯 Future Enhancements Ideas

- Add more news sources
- Implement article content extraction
- Add date filtering options
- Create JSON export format
- Add search/filter functionality
- Implement concurrent scraping for multiple sources

## 📄 Project Structure

```
News Scraper/
├── news_scraper.py      # Main scraper application
├── README.md           # This documentation
├── today_headlines.csv # Example output file
└── requirements.txt    # Dependencies (optional)
```

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new news sources
- Improve headline detection
- Enhance CSV formatting
- Add new export formats

## 📜 License

This project is open source and available under the MIT License.

---

## 🎉 Project Complete!

Congratulations! You've built a professional news scraping tool that combines web scraping, command-line interfaces, and data export. This project showcases practical Python skills for real-world automation tasks.
