# Python Learning Journey 🐍

A comprehensive collection of Python projects built from scratch to master fundamental programming concepts, libraries, and real-world application development.

## 🎯 Learning Philosophy

**"Learn by Building"** - Each project introduces new Python concepts while creating practical, functional applications. Progress from basic syntax to advanced libraries through hands-on coding experience.

## 📚 Learning Modules

### 01. To-Do List CLI
**Core Python Fundamentals + File Handling**

**🧠 Learning Objectives:**
- **Object-Oriented Programming**: Classes, methods, `__init__`, `__str__`
- **Error Handling**: try/except blocks, KeyboardInterrupt, ValueError
- **File I/O**: JSON serialization/deserialization for data persistence
- **User Interface**: Menu-driven CLI with input validation
- **Data Structures**: Lists, dictionaries, enumerations
- **Date/Time**: datetime module, strftime/strptime formatting
- **String Methods**: .strip(), .lower(), .isdigit() validation

**✨ Key Features:**
- Full CRUD operations (Create, Read, Update, Delete)
- JSON persistence for data storage
- Color-coded terminal output
- Comprehensive input validation
- Real-time task editing with immediate updates

---

### 02. News Headlines Scraper
**Web Scraping + Command-Line Tools + Data Export**

**🧠 Learning Objectives:**
- **Web Scraping**: requests library for HTTP requests
- **HTML Parsing**: BeautifulSoup for DOM navigation and element selection
- **Command-Line Interface**: argparse for professional CLI design
- **Data Export**: CSV module for structured data output
- **Error Handling**: Network errors, HTTP status codes, missing elements
- **URL Processing**: urllib.parse for domain extraction

**✨ Key Features:**
- Multi-source news scraping (BBC, CNN, Reuters, etc.)
- Custom URL support for any website
- Professional CLI with argument validation
- CSV export with timestamps and metadata
- Smart headline detection using multiple selectors

---

### 03. CSV Data Visualizer
**Data Science + Statistical Analysis + Advanced Visualization**


**🧠 Learning Objectives:**
- **Data Analysis**: pandas DataFrames, data exploration, statistical summaries
- **Data Visualization**: matplotlib for basic plots, seaborn for advanced charts
- **Statistical Analysis**: Correlation analysis, distribution patterns, regression lines
- **Multi-Chart Displays**: Subplots, comparative analysis, professional styling
- **Data Science Workflow**: From raw CSV to publication-ready visualizations

**✨ Key Features:**
- Loads and analyzes Bitcoin price dataset (59 data points)
- Creates 6 different chart types simultaneously
- Professional seaborn styling with statistical overlays
- Correlation analysis with regression lines
- Distribution analysis with density curves
- Real-time data exploration and insights

---

### 04. [Log File Analyzer](./04-log-analyzer/)
**System Administration + Regex + Security Analysis**

**🧠 Learning Objectives:**
- **Regular Expressions**: Complex pattern matching with capturing groups
- **File Streaming**: Memory-efficient processing of large files
- **Date/Time Parsing**: Converting timestamps to datetime objects
- **Data Aggregation**: Statistical analysis and frequency counting
- **Security Analysis**: Detecting suspicious patterns and attacks
- **Command-Line Tools**: Professional argparse implementation

**✨ Key Features:**
- Parses Apache/Nginx log files with regex patterns
- Identifies top IPs, status codes, and request paths
- Security threat detection (brute force, suspicious paths)
- Time-based traffic analysis with visual charts
- Professional CLI with multiple analysis options
- Memory-efficient streaming for large log files

---

### 05. [Weather API Integration](./Weather%20Api/)
**API Integration + HTTP Requests + JSON Processing**

**🧠 Learning Objectives:**
- **HTTP Requests**: Making GET requests to external APIs using requests library
- **JSON Data Handling**: Parsing and extracting data from API responses
- **Error Handling**: Managing network errors, API failures, and invalid responses
- **Data Extraction**: Navigating complex nested JSON structures
- **User Input**: Interactive command-line interface with input validation
- **Service Integration**: Working with third-party weather services

**✨ Key Features:**
- Fetches real-time weather data from free APIs (no API key required)
- Smart location display with city, region, and country information
- Comprehensive weather data (temperature, humidity, wind speed)
- Robust error handling with user-friendly messages
- International support for cities worldwide
- Clean, readable output formatting

## 🛠️ Python Libraries Mastered

| Library | Purpose | Key Learning |
|---------|---------|--------------|
| **Built-in Modules** | | |
| `datetime` | Date/time handling | strftime, timedelta, date arithmetic |
| `json` | Data serialization | dumps, loads, file persistence |
| `csv` | Data export | writer, formatting, UTF-8 encoding |
| `argparse` | CLI interfaces | argument parsing, validation, help generation |
| `re` | Regular expressions | pattern matching, groups, text parsing |
| **External Packages** | | |
| `requests` | HTTP requests | GET requests, status codes, error handling |
| `beautifulsoup4` | HTML parsing | find_all, element selection, text extraction |
| `pandas` | Data analysis | DataFrames, CSV reading, data manipulation |
| `matplotlib` | Basic plotting | line plots, bar charts, scatter plots, subplots |
| `seaborn` | Statistical visualization | regression plots, distributions, professional styling |
| `numpy` | Mathematical operations | Array operations, statistical functions |
