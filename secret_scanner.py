"""
secret_scanner.py
CLI tool that scans files or directories for hardcoded secrets
(API keys, passwords, tokens, private keys, etc.) using regex patterns.

"""

import argparse
import logging
import os
import re
import sys
from dataclasses import dataclass
from typing import List

# Enable logging capabilities per assignment requirement.
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
logging.basicConfig(format=LOG_FORMAT, level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger("secret_scanner")


# Define regex patterns
# Reference: Author-regextokens, Source-https://github.com/dxa4481/truffleHogRegexes
# Assignment requirements: Use regex to detect common secret patterns.
#                          Must include at least 5 regex patters (API keys, passwords, tokens, and private keys)
SECRET_PATTERNS: List[tuple] = [
    (
        "Generic API Key",
        re.compile(r"[aA][pP][iI]_?[kK][eE][yY].*['\"][0-9a-zA-Z]{32,45}['\"]"),
    ),
    (
        "Generic Secret",
        re.compile(r"[sS][eE][cC][rR][eE][tT].*['\"][0-9a-zA-Z]{32,45}['\"]"),
    ),
    (
        "RSA Private Key",
        re.compile(r"-----BEGIN RSA PRIVATE KEY-----"),
    ),
    (
        "Google API Key",
        re.compile(r"AIza[0-9A-Za-z\-_]{35}"),
    ),
    (
        "Google OAuth Access Token",
        re.compile(r"ya29\.[0-9A-Za-z\-_]+"),
    ),
    (
        "GitHub Token",
        re.compile(r"[gG][iI][tT][hH][uU][bB].*['\"][0-9a-zA-Z]{35,40}['\"]"),
    ),
    (
        "Slack Token",
        re.compile(r"xox[pborsa]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32}"),
    ),
    (
        "Password in URL",
        re.compile(r"[a-zA-Z]{3,10}://[^/\s:@]{3,20}:[^/\s:@]{3,20}@.{1,100}[\"'\s]"),
    ),
]

# List of files to be scanned.
# Reference: Jackson. M. (2021, Mar 12). File types that most commonly contain sensitive information.
#            GitGardian. https://blog.gitguardian.com/top-10-file-extensions/
TEXT_EXTENSIONS = {
    ".bash",
    ".cfg",
    ".conf",
    ".css",
    ".cs",
    ".env",
    ".gradle",
    ".htm",
    ".html",
    ".ini",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".php",
    ".properties",
    ".py",
    ".sh",
    ".sql",
    ".tf",
    ".toml",
    ".ts",
    ".tsx",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}


# Define data class to be used for storing results of findings.
# Assignment requirement: Output a report of findings (filename, line number, matched string)
@dataclass
class Results:
    filepath: str
    line_number: int
    pattern_name: str
    matched_pattern: str


# Assignment requirement: Accept a directory path or file as input.
# Function to scan a line for matching patterns.
# Return a list of pattern name and matching text.
def scan_line(line: str) -> List[tuple]:
    matched_patterns = []

    for name, pattern in SECRET_PATTERNS:
        match = pattern.search(line)
        if match:
            matched_patterns.append(
                (name, match.group(0)[:30] + "...")
            )  # Add the first 30 characters of the matched string.

    return matched_patterns


# Function to scan a single file and return a list of Results.
def scan_file(filepath: str) -> List[Results]:
    logger.info("File scanned: %s", filepath)
    results: List[Results] = []

    _, ext = os.path.splitext(filepath)  # Read file extensions from a file path.

    # Exit the function early if the file extension is not in the list.
    if ext.lower() not in TEXT_EXTENSIONS and ext != "":
        return results

    # Read a file line by line to scan for secrets.
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            for line_num, line in enumerate(f, start=1):
                for name, matched_pattern in scan_line(line):
                    results.append(
                        Results(
                            filepath=filepath,
                            line_number=line_num,
                            pattern_name=name,
                            matched_pattern=matched_pattern.strip(),
                        )
                    )
    except PermissionError:
        logger.warning("Permission error: %s", filepath)
    except OSError:
        logger.error("OS error: %s", filepath)

    return results


# Function to scan a directory.
def scan_directory(dirpath: str) -> List[Results]:

    results: List[Results] = []
    logger.info("Directory scanned: %s", dirpath)

    for root, _, files in os.walk(dirpath):
        for filename in files:
            filepath = os.path.join(root, filename)
            results.extend(scan_file(filepath))
    return results


# Function to print a report of findings.
# Requirement: Output a report of findings (filename, line number, matched string)
def print_report(results: List[Results]) -> None:
    print("\nSecret Scanner Results:")
    print("     [File Path - Line Number - Pattern Name - Matched Text]")

    if not results:
        print("\n     -0 secrets found.")
    else:
        for r in results:
            print(
                f"\n     -{r.filepath} - Line {r.line_number} - {r.pattern_name} - {r.matched_pattern}"
            )
        print("\n     -%d secrets found." % len(results))


# Define CLI entry point
# Function to build the argument parser for CLI usage.
def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="secret_scanner",
        description=("This app scans files or directories for hardcoded secrets."),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples to enter:\n"
            "  python secret_scanner.py config.py for a file scan\n"
            "  python secret_scanner.py test_files for a directory scan\n"
        ),
    )

    parser.add_argument(
        "path",
        help="File path or directory path to scan.",
    )
    return parser

# Define the main function to handle CLI input.
def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()
    target = os.path.normpath(args.path)

    # Validate the path exists
    if not os.path.exists(target):
        logger.error("Invalid path: %s", target)
        exit(1)

    # Call scanner functions to build results.
    if os.path.isfile(target):
        results = scan_file(target)
    elif os.path.isdir(target):
        results = scan_directory(target)
    else:
        logger.error("Invalid path: %s", target)
        exit(1)

    # Print the report of findings.
    print_report(results)



if __name__ == "__main__":
    sys.exit(main())
