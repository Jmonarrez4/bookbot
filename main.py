def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
    word_count(contents)

def word_count(text):
    words = text.split()
    print(len(words))

main()
