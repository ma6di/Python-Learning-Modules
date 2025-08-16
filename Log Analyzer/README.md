# Log File Analyzer 📊

A  Python tool for analyzing Apache/Nginx web server logs with regex pattern matching, security threat detection, and statistical reporting.

## 🎯 Learning Objectives

### **Core Concepts:**
- **Regular Expressions**: Complex pattern matching with capturing groups
- **File Streaming**: Memory-efficient processing of large log files
- **Date/Time Parsing**: Converting string timestamps to datetime objects
- **Data Aggregation**: Statistical analysis and frequency counting
- **Command-Line Interfaces**: Professional argparse implementation
- **Security Analysis**: Detecting suspicious patterns and potential attacks

### **Advanced Python Features:**
- **Collections Module**: defaultdict for cleaner counting operations
- **String Processing**: Parsing structured text data
- **Error Handling**: Robust file processing with specific exception handling
- **Modular Design**: Function-based architecture for maintainable code

## 🚀 Features

### **📈 Statistical Analysis**
- **Request Volume**: Total requests and unique visitor counting
- **IP Analysis**: Top visitor identification and activity patterns
- **Status Code Distribution**: Response code analysis with percentages
- **HTTP Method Tracking**: GET, POST, PUT, DELETE frequency analysis
- **Popular Paths**: Most requested URLs and resources

### **🛡️ Security Monitoring**
- **Threat Detection**: Automatic identification of suspicious access patterns
- **Attack Pattern Recognition**: Common attack vectors (/admin, /.env, /wp-admin)
- **Brute Force Detection**: High-frequency access from single IPs
- **Vulnerability Scanning**: Detection of automated security probes

### **⏰ Time-Based Analytics**
- **Hourly Traffic Patterns**: Visual representation of request distribution
- **Peak Usage Analysis**: Identification of high-traffic periods
- **Timeline Visualization**: ASCII bar charts for quick insights

## 📋 Usage

### **Basic Analysis**
```bash
python3 log_analyzer.py sample_access.log
```

### **With Security Analysis**
```bash
python3 log_analyzer.py sample_access.log --security
```

### **Custom Options**
```bash
python3 log_analyzer.py logfile.log --top 10 --security
```

## 🔧 Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `logfile` | Path to log file (required) | - |
| `--top` | Number of top results to display | 5 |
| `--security` | Enable security threat analysis | False |

## 📊 Sample Output

```
=== LOG ANALYSIS REPORT ===
Total Requests: 20
Unique IPs: 4

TOP 5 IP ADDRESSES:
1. 192.168.1.100: 6 requests
2. 203.45.67.89: 3 requests
3. 10.0.0.15: 3 requests

STATUS CODE DISTRIBUTION:
200: 15 (75.0%)
401: 3 (15.0%)
404: 2 (10.0%)

HTTP METHOD DISTRIBUTION:
GET: 17 (85.0%)
POST: 3 (15.0%)

🛡️  SECURITY ANALYSIS:
⚠️  Suspicious access: /admin/login (2 times)
⚠️  Suspicious access: /.env (1 times)

⏰ TIME ANALYSIS:
08:00 - 20 requests ██████████
```

## 🧩 Code Structure

### **Core Functions:**
- `parse_log_line()`: Regex-based log entry parsing
- `update_statistics()`: Data aggregation and counting
- `generate_report()`: Statistical report generation
- `analyze_security_threats()`: Security pattern detection
- `analyze_time_patterns()`: Temporal analysis with visualization

### **Regex Pattern:**
```python
r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\] "(.*?)" (\d+) (\d+)'
```
**Captures**: IP, Timestamp, HTTP Request, Status Code, Response Size

## 📁 Sample Data

The project includes two sample log files:

### **sample_access.log**
- Normal website traffic patterns
- Various HTTP methods and status codes
- Mixed user agents and referrers

### **suspicious_access.log**
- Security attack simulations
- SQL injection attempts
- Directory traversal attacks
- Brute force login attempts

## 🎓 Learning Achievements

After completing this module, you will have mastered:

### **System Administration Skills**
- **Log Analysis**: Understanding web server operations and metrics
- **Security Monitoring**: Identifying potential threats and vulnerabilities
- **Performance Analysis**: Traffic pattern recognition and bottleneck identification

### **Advanced Programming Techniques**
- **Regular Expressions**: Complex pattern matching with capturing groups
- **Memory Management**: Efficient large file processing without memory overflow
- **Data Structures**: Advanced usage of dictionaries, defaultdict, and counters
- **Professional CLI**: Argument parsing, help documentation, and user experience

### **Real-World Applications**
- **DevOps Automation**: Automated log monitoring and alerting systems
- **Security Operations**: Threat detection and incident response
- **Web Analytics**: User behavior analysis and traffic optimization
- **System Monitoring**: Performance tracking and capacity planning

## 🔍 Technical Implementation

### **Regex Breakdown:**
- `(\d+\.\d+\.\d+\.\d+)`: IP address capture with word boundaries
- `.*?`: Non-greedy matching for intermediate log elements
- `\[(.*?)\]`: Timestamp extraction from square brackets
- `"(.*?)"`: HTTP request string capture from quotes
- `(\d+) (\d+)`: Status code and response size capture

### **Data Processing Pipeline:**
1. **File Streaming**: Line-by-line processing for memory efficiency
2. **Pattern Matching**: Regex validation and data extraction
3. **Data Aggregation**: Dictionary-based frequency counting
4. **Statistical Analysis**: Sorting, ranking, and percentage calculations
5. **Report Generation**: Formatted output with visual elements

### **Error Handling Strategy:**
- **Parse Errors**: Invalid log format detection and reporting
- **Data Errors**: Malformed timestamp or numeric field handling
- **File Errors**: Missing files, permission issues, and I/O exceptions

## 💡 Extensions & Improvements

### **Potential Enhancements:**
- **Database Integration**: Store analysis results in SQLite/PostgreSQL
- **Web Dashboard**: Flask/Django interface for visual analytics
- **Real-time Processing**: Live log monitoring with websockets
- **Machine Learning**: Anomaly detection using scikit-learn
- **Export Formats**: JSON, CSV, and Excel report generation

---

*Master log analysis, security monitoring, and data aggregation through hands-on server log processing* 🐍🔍
