import sys

from stats import count_words, get_character_count, get_most_common_characters


def get_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path> [n]")
        sys.exit(1)

    file_path = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 10

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
    main()
