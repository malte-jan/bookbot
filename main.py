def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_file = file_contents.lower()

    # Count words
    words = lowered_file.split()
    word_count = len(words)

    # Initialize character count dictionary
    char_count = {}

    # Count each character
    for char in lowered_file:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Print the formatted output
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    # Sort characters by frequency and print each
    for char, count in sorted(char_count.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{char}' character was found {count} times")

main()