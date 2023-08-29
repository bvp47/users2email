# Username Modifier Tool

## Overview

The Username Modifier Tool is a simple Python script designed to assist with bulk username modifications. It offers two main functionalities:

1. Add a domain to a list of usernames (e.g., converting `user1` to `user1@domain.com`).
2. Strip the domain from a list of email addresses (e.g., converting `user1@domain.com` to `user1`).

This tool reads usernames or email addresses from an input text file and writes the modified usernames or stripped email addresses to an output text file.

## Requirements

- Python 3.x

## Installation

Clone this repository or download the `modify_usernames.py` script.

## Usage

### Adding a Domain

To add a domain to a list of usernames, use the `-a` or `--add` option followed by the domain. You also need to specify the input and output filenames.

```python
python modify_usernames.py -a domain.com -i usernames.txt -o emails.txt
This will read usernames from usernames.txt, add @domain.com to each username, and save the modified usernames to emails.txt.
```
### Stripping a Domain
To strip the domain from a list of email addresses, use the -s or --strip option. You also need to specify the input and output filenames.

```python
python modify_usernames.py -s -i emails.txt -o usernames.txt
This will read email addresses from emails.txt, strip the domain part, and save the usernames to usernames.txt.
```

### Help
To view the available options and how to use them, run:
```python
python modify_usernames.py -h
```
### License
This project is open-source and available under the MIT License.
