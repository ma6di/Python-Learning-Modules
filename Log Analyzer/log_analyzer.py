import re
from datetime import datetime
from collections import defaultdict
import argparse


def analyze_time_patterns(timestamps):
    print("\n⏰ TIME ANALYSIS:")
    
    hour_counts = defaultdict(int)
    
    for timestamp_str in timestamps:
        try:
            # Parse: "15/Aug/2025:08:15:32 +0000"
            dt = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")
            hour_counts[dt.hour] += 1
        except:
            continue
    
    print("Requests by hour:")
    for hour in sorted(hour_counts.keys()):
        count = hour_counts[hour]
        bar = "█" * (count // 2)  # Simple bar chart
        print(f"{hour:02d}:00 - {count:3d} requests {bar}")

def analyze_security_threats(stats):
    print("\n🛡️  SECURITY ANALYSIS:")
    
    # Check for suspicious paths
    suspicious_paths = ['/admin', '/wp-admin', '/.env', '/phpmyadmin', '/config.php']
    threats_found = 0
    
    for path in stats['path_counts']:
        for suspicious in suspicious_paths:
            if suspicious in path:
                count = stats['path_counts'][path]
                print(f"⚠️  Suspicious access: {path} ({count} times)")
                threats_found += 1
    
    if threats_found == 0:
        print("✅ No obvious security threats detected")
    
    # Check for brute force (many 401s from same IP)
    print("\n🔒 POTENTIAL BRUTE FORCE ATTACKS:")
    for ip, count in stats['ip_counts'].items():
        if count > 10:  # More than 10 requests from one IP
            print(f"⚠️  High activity from {ip}: {count} requests")

def parse_log_line(line, pattern):
    """Parse a single log line and return extracted data"""
    match = re.match(pattern, line.strip())
    if match:
        return match.groups()
    return None

def update_statistics(stats, ip, timestamp, request, status, size):
    """Update statistics with parsed data"""
    stats['total_requests'] += 1
    stats['ip_counts'][ip] += 1
    stats['status_counts'][status] += 1
    stats['timestamps'].append(timestamp)
    
    request_parts = request.split()
    if len(request_parts) >= 2:
        method, path = request_parts[0], request_parts[1]
        stats['method_counts'][method] += 1
        stats['path_counts'][path] += 1

def generate_report(stats):
    """Generate and print analysis report"""
    print("\n=== LOG ANALYSIS REPORT ===")
    print(f"Total Requests: {stats['total_requests']}")
    print(f"Unique IPs: {len(stats['ip_counts'])}")

    print("\nTOP 5 IP ADDRESSES:")
    for i, (ip, count) in enumerate(sorted(stats['ip_counts'].items(), key=lambda x: x[1], reverse=True)[:5], 1):
        print(f"{i}. {ip}: {count} requests")

    print("\nSTATUS CODE DISTRIBUTION:")
    for status, count in sorted(stats['status_counts'].items()):
        percentage = (count / stats['total_requests']) * 100
        print(f"{status}: {count} ({percentage:.1f}%)")

    print("\nHTTP METHOD DISTRIBUTION:")
    for method, count in sorted(stats['method_counts'].items()):
        percentage = (count / stats['total_requests']) * 100
        print(f"{method}: {count} ({percentage:.1f}%)")

    print("\nTOP 5 REQUESTED PATHS:")
    for i, (path, count) in enumerate(sorted(stats['path_counts'].items(), key=lambda x: x[1], reverse=True)[:5], 1):
        print(f"{i}. {path}: {count} requests")

def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyze Apache/Nginx log files')
    parser.add_argument('logfile', help='Path to log file')
    parser.add_argument('--top', type=int, default=5, help='Number of top results to show')
    parser.add_argument('--security', action='store_true', help='Enable security analysis')
    return parser.parse_args()
    

def main():
    args = parse_arguments()
    filename = args.logfile
    pattern = r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\] "(.*?)" (\d+) (\d+)'

    stats = {
        'total_requests': 0,
        'ip_counts': defaultdict(int),
        'status_counts': defaultdict(int),
        'path_counts': defaultdict(int),
        'method_counts': defaultdict(int),
        'timestamps': []
    }
    
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            try:
                parsed_data = parse_log_line(line, pattern)
                if parsed_data:
                    ip, timestamp, request, status, size = parsed_data
                    update_statistics(stats, ip, timestamp, request, status, size)
                else:
                    print(f"Line {line_number}: Invalid log format")
            except ValueError as e:
                print(f"Line {line_number}: Data parsing error - {e}")
            except Exception as e:
                print(f"Line {line_number}: Unexpected error - {e}")

    # Generate reports
    generate_report(stats)
    
    if args.security:
        analyze_security_threats(stats)
    
    if stats['timestamps']:
        analyze_time_patterns(stats['timestamps'])



if __name__ == "__main__":
	main()