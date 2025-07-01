import argparse
import sys

from stats import count_words, get_most_common_characters


def parse_args():
    parser = argparse.ArgumentParser(description="Analyze a text file.")
    parser.add_argument("file_path", help="Path to the text file")
    parser.add_argument("n", nargs="?", default=10, type=int,
                        help="Number of top characters to display (default: 10)")
    return parser.parse_args()


def get_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)


def main():
    args = parse_args()
    file_path = args.file_path
    n = args.n

    content = get_file_content(file_path)
    words = count_words(content)
    most_common_characters = get_most_common_characters(content, n)

    print("=== BOOK BOT ===\n")
    print(f"Analysis of the book: {file_path}")
    print(f"Word count: {words}")
    print("\nMost common characters:\n")
    print(f"{'Character':<10}{'Count':>10}")
    print("-" * 20)
    for item in most_common_characters:
        print(f"{item['char']:<10}{item['count']:>10}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
