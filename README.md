# App name: Secret Scanner

A Python-based CLI tool that recursively scans files and directories for hardcoded secrets such as API keys, passwords, tokens, and private keys using regular expressions.

## Repository Link:
https://github.com/Tomomi-H011/M08Final.git

## Demo Video Link:



## How It Works

The scanner reads a file or directory and finds hardcoded secrets by matching against regular expressions list. And the end, it prints file path, line number, pattern name, and the first 30 characters of hardcoded secrets.

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





