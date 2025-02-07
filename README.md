# PassGenX
PassGenX - Smart Wordlist Generator

# Overview

PassGenX is a powerful and efficient password wordlist generator designed for penetration testers and security researchers. It intelligently appends common prefixes and suffixes to usernames to create a custom wordlist, making it highly effective for password attacks.

# Features

* Generates password lists based on usernames and common password patterns.
* Includes 500+ common suffixes and prefixes used in real-world passwords.
* Allows users to specify input username files and output wordlist files.
* Simple and lightweight with an easy-to-use command-line interface.

# Installation

Ensure you have Python 3 installed on your system.

1. Clone the Repository.

```
git clone https://github.com/Rao-Pranava/PassGenX.git
cd PassGenX
```
3. Run the Help optoin of the Tool.
```
python3 passgenx.py --help
```

# Usage

```
python3 passgenx.py -i usernames.txt -o CustomPassword.txt
```

## Command-Line Options

| Option       | Description |
|-------------|------------|
| `-i`, `--input`  | Path to the input file containing usernames (one per line). |
| `-o`, `--output` | Path to save the generated password wordlist. Default: `CustomPassword.txt`. |
| `-h`, `--help`   | Show help message and usage information. |

## Input File Format

The username file should contain one username per line, for example:

```
JohnDoe
Alice123
HackerPro
```

### Example Output

If the input file contains JohnDoe, PassGenX will generate variations like:

```
JohnDoe123
JohnDoe@2024
AdminJohnDoe
SuperJohnDoe
JohnDoe!
...
```

# License

PassGenX is released under the MIT License.

# Disclaimer

This tool is intended for educational and ethical testing purposes only. Do not use it for unauthorized access or malicious activities.

# Contributions

Feel free to contribute by submitting issues, feature requests, or pull requests.

# Author

[Pranava Rao] - Cybersecurity Enthusiast

## Contact

GitHub: Rao-Pranava
* X (Twitter): @Pranava__Rao
* YouTube: [@Pranava__Rao](https://www.youtube.com/@pranava__rao)
* Instagram: [@Pranava__Rao](https://www.instagram.com/pranava__rao/)
