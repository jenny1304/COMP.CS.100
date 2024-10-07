"""
COMP.CS.100
Huyen Pham; huyen.pham@tuni.fi; 153151026
"""
def main():
    word = input("Enter a word: ")
    vowels = 0
    for i in range(0, len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[
            i] == "o" or word[i] == "u" or word[i] == "y":
            vowels += 1

    consonants = len(word) - vowels

    print(
        f"The word \"{word}\" contains {vowels} vowels and {consonants} consonants.")


if __name__ == '__main__':
    main()