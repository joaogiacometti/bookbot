# BookBot

BookBot is a command-line tool that analyzes text files (such as books) and provides useful statistics, including the total word count and the most common characters.

## Features

- Counts total words in a text file
- Lists the most common characters and their frequencies
- Simple command-line interface

## Usage

```bash
python main.py <file_path> [n]
```

- `<file_path>`: Path to the text file to analyze
- `[n]`: (Optional) Number of top characters to display (default: 10)

## Example

```bash
python main.py alice_in_wonderland.txt 5
```

## Requirements

- Python 3.x
