# App name: Secret Scanner

This app is a Python-based CLI tool that scans files and directories for hardcoded secrets such as API keys, passwords, tokens, and private keys using regular expressions.

## Repository Link:
https://github.com/Tomomi-H011/M08Final.git


## Demo Video Link:
https://drive.google.com/file/d/1KGXhOJpwcEDOWTG5stW3uE1U5k8Awcqk/view?usp=sharing


## Requirements

- Python 3.8 or higher


## How to run the app

```bash
# 1. Clone or download this repository
# 2. Open the file
cd M08Final
#. 3. To start scanning a file or directory:
python secret_scanner.py <path>

#Examples
# To scan a single file
python secret_scanner.py test_files/config.py

# To scan an entire directory
python secret_scanner.py ./test_files

# To display help
python secret_scanner.py -h
```

### Report Example
Secret Scanner Results:
     [File Path - Line Number - Pattern Name - Matched Text]

     -test_files\.env - Line 3 - Slack Token - xoxp-123456789012-123456789012...

     -test_files\app.js - Line 4 - Google OAuth Access Token - ya29.A0AfH6SMBxyz_some_long_ac...

     -test_files\app.js - Line 8 - Password in URL - https://user:hardcodedPassword...

     -test_files\config.py - Line 4 - Google API Key - AIzaSyD-9tSrke72PouQMnMX-a7eZS...

     -test_files\config.py - Line 7 - Generic API Key - api_key = "my_api_key='abcdefg...

     -test_files\private_key.txt - Line 1 - RSA Private Key - -----BEGIN RSA PRIVATE KEY----...

     -6 secrets found.

### Log Example
2026-05-07 17:19:05,565 [INFO] Directory scanned: test_files

2026-05-07 17:19:05,565 [INFO] File scanned: test_files\.env

2026-05-07 17:19:05,566 [INFO] File scanned: test_files\app.js

2026-05-07 17:19:05,566 [INFO] File scanned: test_files\config.py

2026-05-07 17:19:05,567 [INFO] File scanned: test_files\private_key.txt

### Help Example
python secret_scanner.py -h
usage: secret_scanner [-h] path

This app scans files or directories for hardcoded secrets.

positional arguments:
  path        File path or directory path to scan.

options:
  -h, --help  show this help message and exit

Examples to enter:
  python secret_scanner.py config.py for a file scan
  python secret_scanner.py test_files for a directory scan


### References used:
Johnson, T. (2024, Jun 2). Useful tips for logging in Python. Medium. https://medium.com/@tyrel.j.johnson/useful-tips-for-logging-in-python-c2c945358b5e
Python.(n.d.) Argparse Tutorial. https://docs.python.org/3/howto/argparse.html
Python. (n.d.) logging — Logging facility for Python. https://docs.python.org/3/library/logging.html

