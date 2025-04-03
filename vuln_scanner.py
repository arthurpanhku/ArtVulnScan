#!/usr/bin/env python3

"""
Automated Vulnerability Scanner
A cybersecurity tool for everyone, using only open-source software (Nmap).
Performs automated network vulnerability scans on a user-defined schedule.
Version: 1.2
"""

import nmap
import sys
import time
import os
from datetime import datetime, timedelta
import schedule

class VulnerabilityScanner:
    def __init__(self):
        """Initialize Nmap PortScanner for vulnerability scanning."""
        try:
            self.nm = nmap.PortScanner()
        except nmap.PortScannerError:
            print("Error: Nmap not found. Please install it with 'sudo apt-get install nmap' or equivalent.")
            sys.exit(1)
        except Exception as e:
            print(f"Error initializing Nmap: {str(e)}")
            sys.exit(1)

    def scan_target(self, target, arguments='-sV --script=vuln'):
        """
        Scan the specified target for vulnerabilities.

        Args:
            target (str): IP address or hostname to scan
            arguments (str): Nmap arguments (default: service detection and vuln scripts)

        Returns:
            bool: True if scan succeeds, False otherwise
        """
        try:
            print(f"\nStarting scan on {target} at {datetime.now()}")
            self.nm.scan(hosts=target, arguments=arguments)
            
            if target not in self.nm.all_hosts():
                print(f"Target {target} did not respond. Check connectivity or permissions.")
                return False
            return True
            
        except Exception as e:
            print(f"Scan failed: {str(e)}")
            return False

    def generate_report(self, target):
        """
        Generate and save a detailed scan report.

        Args:
            target (str): Scanned target

        Returns:
            str: Report content
        """
        report = f"Vulnerability Scan Report - {target}\n"
        report += f"Generated: {datetime.now()}\n"
        report += "=" * 50 + "\n\n"
        
        for host in self.nm.all_hosts():
            report += f"Host: {host} ({self.nm[host].hostname()})\n"
            report += f"State: {self.nm[host].state()}\n\n"
            
            for proto in self.nm[host].all_protocols():
                report += f"Protocol: {proto}\n"
                ports = sorted(self.nm[host][proto].keys())
                
                for port in ports:
                    port_info = self.nm[host][proto][port]
                    report += f"Port: {port}\tState: {port_info['state']}\t"
                    report += f"Service: {port_info.get('name', 'unknown')} "
                    report += f"({port_info.get('product', '')} {port_info.get('version', '')})\n"
                    
                    if 'script' in port_info:
                        report += "Vulnerabilities:\n"
                        for script, output in port_info['script'].items():
                            report += f"- {script}:\n  {output}\n"
                    report += "\n"
            
            report += "-" * 50 + "\n"
        
        filename = f"vuln_scan_{target}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(report)
        
        print(f"\nReport saved to: {filename}")
        return report

def check_requirements():
    """Verify Nmap is installed on the system."""
    if not os.path.exists('/usr/bin/nmap') and not os.path.exists('/usr/local/bin/nmap'):
        print("Error: Nmap is not installed.")
        print("Install it with:")
        print("  - Ubuntu/Debian: sudo apt-get install nmap")
        print("  - Red Hat/CentOS: sudo yum install nmap")
        sys.exit(1)

def validate_date(date_str):
    """Validate and parse user-provided date string (YYYY-MM-DD)."""
    try:
        scan_date = datetime.strptime(date_str, "%Y-%m-%d")
        if scan_date < datetime.now():
            print("Error: First scan date must be in the future.")
            return None
        return scan_date
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD (e.g., 2025-04-10).")
        return None

def run_scan(target, scanner):
    """Execute the scan and generate report."""
    if scanner.scan_target(target):
        scanner.generate_report(target)
    else:
        print(f"Scan on {target} failed.")

def setup_schedule(target, scanner):
    """Set up scanning schedule based on user input."""
    print("\nChoose scan frequency:")
    print("1. Every day")
    print("2. Every week")
    print("3. Every month")
    frequency = input("Enter choice (1-3): ").strip()

    first_scan_date = input("Enter first scan date (YYYY-MM-DD): ").strip()
    scan_date = validate_date(first_scan_date)
    if not scan_date:
        sys.exit(1)

    # Calculate initial delay until first scan
    delay_seconds = (scan_date - datetime.now()).total_seconds()
    if delay_seconds > 0:
        print(f"First scan scheduled for {scan_date}. Waiting...")
        time.sleep(delay_seconds)

    # Set up recurring schedule
    if frequency == "1":
        schedule.every().day.at(scan_date.strftime("%H:%M")).do(run_scan, target, scanner)
        print("Scheduled daily scans starting from", scan_date)
    elif frequency == "2":
        schedule.every().week.at(scan_date.strftime("%H:%M")).do(run_scan, target, scanner)
        print("Scheduled weekly scans starting from", scan_date)
    elif frequency == "3":
        schedule.every(4).weeks.at(scan_date.strftime("%H:%M")).do(run_scan, target, scanner)  # Approx. monthly
        print("Scheduled monthly scans starting from", scan_date)
    else:
        print("Error: Invalid choice. Please select 1, 2, or 3.")
        sys.exit(1)

def main():
    """Run the vulnerability scanner with scheduling."""
    print("Automated Vulnerability Scanner v1.2")
    print("===================================")
    print("A free, open-source tool for everyone")
    print("Note: Requires root privileges (sudo) for best results")
    print("Warning: Only scan targets you have permission to test")
    print("===================================\n")
    
    check_requirements()
    
    target = input("Enter target IP or hostname (e.g., 192.168.1.1 or scanme.nmap.org): ").strip()
    if not target:
        print("Error: Please provide a valid target.")
        sys.exit(1)
    
    scanner = VulnerabilityScanner()
    setup_schedule(target, scanner)

    # Keep the script running to execute scheduled tasks
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\nScheduler stopped by user. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error in scheduler: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    main()
