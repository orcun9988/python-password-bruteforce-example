#!/usr/bin/env python3
"""
Educational password brute-force loop example
==============================================

EDUCATIONAL PURPOSES ONLY.

This script demonstrates the general structure of a password-guessing
loop against a wordlist. It exists as a reference for security
awareness training and CS coursework.

DO NOT use this code against any account or service you do not own
or have explicit written permission to test.

The attempt_login() function below is a placeholder and does NOT
make real network requests.

Author : Whis (legacy 2023 educational project)
"""

import sys


def attempt_login(username: str, password: str) -> bool:
    """
    Placeholder login attempt.

    Replace with your own controlled test harness (a CTF box, local
    DVWA, your own Flask server, etc.) for actual experimentation.

    Returns True on simulated success.
    """
    # Educational placeholder — does NOT make real network requests.
    return False


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: example.py <username> <wordlist.txt>")
        sys.exit(1)

    username = sys.argv[1]
    wordlist_path = sys.argv[2]

    with open(wordlist_path, "r", encoding="utf-8") as f:
        for line in f:
            password = line.strip()
            if not password:
                continue
            print(f"[*] Trying: {password}")
            if attempt_login(username, password):
                print(f"[+] Match: {password}")
                return

    print("[-] No match in wordlist.")


if __name__ == "__main__":
    main()
