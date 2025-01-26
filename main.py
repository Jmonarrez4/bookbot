def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
    
    # Call functions to get word and character data
    word_count_dict = word_count(contents)
    char_count_dict = count_characters(contents)
    total_words = sum(word_count_dict.values())
    
    # Print the report
    print_report(total_words, char_count_dict)

def word_count(text):
    words = text.split()
    word_count_dict = {}
    for word in words:
        word_lowered = word.lower()
        if word_lowered in word_count_dict:
            word_count_dict[word_lowered] += 1
        else:
            word_count_dict[word_lowered] = 1
    return word_count_dict

def count_characters(text):
    char_count_dict = {}
    text = text.lower()
    for char in text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def print_report(total_words, char_count_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    print()
    
    # Sort the characters by frequency in descending order
    sorted_chars = sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_chars:
        # Only print characters that are not whitespace, periods, or hashes
        if char not in [' ', '.', '#']:
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()
