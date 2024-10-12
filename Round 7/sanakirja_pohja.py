"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""

def main():

    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    spanish_english = {}

    print("Dictionary contents:")
    content = ", ".join(sorted(english_spanish))
    print(content)

    while True:
        for english in english_spanish:
            spanish_english.update({english_spanish[english]:english})

        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":

            key = input("Give the word to be added in English: ")
            payload = input("Give the word to be added in Spanish: ")
            english_spanish.update({key:payload})

            print("Dictionary contents:")
            content = ", ".join(sorted(english_spanish))
            print(content)

        elif command == "R":
            remove = input("Give the word to be removed: ")
            if remove in english_spanish:
                del english_spanish[remove]
            else:
                print("The word", remove, "could not be found from the dictionary.")

        elif command == "P":
            print("\nEnglish-Spanish")
            for i in sorted(english_spanish):
                print(f"{i} {english_spanish.get(i)}")
            print("\nSpanish-English")
            for i in sorted(spanish_english):
                print(f"{i} {spanish_english[i]}")
            print("")

        elif command == "T":
            sentence = input("Enter the text to be translated into Spanish: ")
            text = sentence.split(" ")

            for i in range(len(text)):
                if text[i] in english_spanish:
                    text[i]=english_spanish[text[i]]
            translated=" ".join(text)

            print("The text, translated by the dictionary:")
            print(translated)
        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

if __name__ == "__main__":
    main()
