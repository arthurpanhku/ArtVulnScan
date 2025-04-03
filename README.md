# ArtVulnScan - Best Automated Vulnerability Scanner


A Python-powered tool harnessing Nmap for automated network vulnerability scanning, complete with detailed report generation.
This is an automated cybersecurity tool designed for everyone to use, consolidating only open-source and free software. Built with Python and powered by Nmap, it simplifies network vulnerability scanning by detecting services, identifying potential security risks, and generating detailed reports—all with an accessible, user-friendly interface.

## What It Does

This project delivers a straightforward, robust script to scan networks or hosts for vulnerabilities using Nmap. It detects services and versions, runs vulnerability checks via Nmap scripts, and saves results in timestamped text files. Built for security enthusiasts, network admins, and penetration testers, it simplifies automated security assessments.

## Key Features

- **Vulnerability Detection**: Leverages Nmap’s vulnerability scripts to pinpoint security risks.
- **Service Identification**: Spots open ports, services, and their versions.
- **Rich Reporting**: Produces in-depth, timestamped reports saved as text files.
- **Reliable Execution**: Features solid error handling for Nmap and scan operations.
- **Easy to Use**: Offers a clean command-line interface with clear prompts.

## Requirements

To get started, you’ll need:

- **Python 3.x**: The script runs on Python 3.
- **Nmap**: The core scanning engine (widely available on Linux).
- **python-nmap**: A Python library bridging Nmap functionality.

### Setup Steps

1. **Install Nmap**:
- Ubuntu/Debian:
```bash
sudo apt-get install nmap
```
- Red Hat/CentOS:
```bash
sudo yum install nmap
```

2. **Install python-nmap**:
```bash
pip install python-nmap
```

## Getting Started

1. Clone the repo:
```bash
git clone https://github.com/arthurpanhku/ArtVulnScan.git
cd automated-vulnerability-scanner
```

2. Verify prerequisites are installed (see above).

## How to Use

Launch the script with root privileges for optimal results:

```bash
sudo python3 vuln_scanner.py
```

- Enter a target (e.g., `192.168.1.1` or `scanme.nmap.org`) when prompted.
- Watch it scan and save a report as a `.txt` file in your current directory.

### Sample Run
```
$ sudo python3 vuln_scanner.py
Automated Vulnerability Scanner v1.0
===================================
Note: Requires root privileges for full functionality
Warning: Only scan networks you have permission to scan
===================================

Enter target IP or hostname (e.g., 192.168.1.1 or scanme.nmap.org): scanme.nmap.org

Starting vulnerability scan on scanme.nmap.org at 2025-04-03 12:00:00
Report saved to vuln_scan_scanme.nmap.org_1740926400.txt

Scan Summary:
[Detailed results appear here]
```

The output file (e.g., `vuln_scan_scanme.nmap.org_1740926400.txt`) lists ports, services, and vulnerabilities found.

## Customization

The default scan uses:
- `-sV`: Detects service versions.
- `--script=vuln`: Runs Nmap’s vulnerability scripts.

Tweak the `arguments` in the `scan_target` method of `vuln_scanner.py` for custom scans:
- All ports: `-p 1-65535`
- Full scan: `-A`
- Specific script: `--script=<script-name>`

## Project Layout

```
automated-vulnerability-scanner/
├── vuln_scanner.py  # Core script
├── README.md        # Documentation
└── .gitignore       # Excludes generated files (optional)
```

## Heads Up

- **Legal Note**: Only scan targets you’re authorized to test—unauthorized scanning might break laws.
- **Root Access**: Use `sudo` for full Nmap capabilities (e.g., SYN scans).
- **Script Updates**: Keep Nmap’s scripts current with `sudo nmap --script-updatedb`.
- **Purpose**: Designed for ethical, authorized security testing.

## Contributing

Love to have your input! Here’s how:
1. Fork this repo.
2. Branch out: `git checkout -b feature/your-cool-idea`
3. Commit changes: `git commit -m "Added something awesome"`
4. Push it: `git push origin feature/your-cool-idea`
5. Submit a Pull Request.

Stick to PEP 8 and add docs where needed.

## License

Licensed under the [MIT License](LICENSE)—check the `LICENSE` file for details.

## Credits

- Powered by [Nmap](https://nmap.org/) and [python-nmap](https://pypi.org/project/python-nmap/).
- Born from a passion for automated security tools.

## Questions?

Hit up GitHub Issues or email me at [u3638376@connect.hku.hk](mailto:u3638376@connect.hku.hk).

---

## Prerequisites

Install the additional dependency:

```bash
pip install schedule
```

## How to Run

```bash
sudo python3 vuln_scanner.py
```

- Input a target (e.g., `scanme.nmap.org`).
- Choose a frequency:
  - `1` for every day
  - `2` for every week
  - `3` for every month
- Enter a future date (e.g., `2025-04-10`).
- The script will wait until the specified date, then scan according to the schedule.

## Example Interaction

```
Automated Vulnerability Scanner v1.2
===================================
A free, open-source tool for everyone
Note: Requires root privileges (sudo) for best results
Warning: Only scan targets you have permission to test
===================================

Enter target IP or hostname (e.g., 192.168.1.1 or scanme.nmap.org): scanme.nmap.org

Choose scan frequency:
1. Every day
2. Every week
3. Every month
Enter choice (1-3): 2
Enter first scan date (YYYY-MM-DD): 2025-04-10
First scan scheduled for 2025-04-10 00:00:00. Waiting...
Scheduled weekly scans starting from 2025-04-10 00:00:00
```

## Notes

- **Time Precision**: Scans run at the time of day the script starts after the first date (e.g., if you run it at 14:30, scans occur at 14:30 on scheduled days). For exact times, modify the `.at()` parameter in the script.
- **Monthly Approximation**: True monthly scheduling requires more complex logic (e.g., using `dateutil`). This version uses 4 weeks for simplicity.
- **Background Running**: To run indefinitely, consider using a daemon or `nohup`. Example:
```bash
nohup sudo python3 vuln_scanner.py &
```

---
Scan smart, stay safe!
---
