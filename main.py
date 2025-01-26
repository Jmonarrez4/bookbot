def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
    word_count(contents)
    count_characters(contents)

def word_count(text):
    words = text.split()
    print(len(words))

def count_characters(text):
    characters = {}
    text = text.lower()
    for character in text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    print(characters)

main()