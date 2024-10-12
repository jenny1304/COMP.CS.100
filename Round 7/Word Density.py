"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name: Huyen Pham
Email: huyen.pham@tuni.fi
"""
def add(string, dictionary):
    """
    Add the words and the number of times it shows up to a dictionary

    :param string: The text entered by user by line
    :param dictionary: Storing the words as the key and the number of times it shows up as payload

    """
    words = string.lower().split(" ")

    for word in words:
        if word not in dictionary:
            dictionary.update({word:1})
        elif word in dictionary:
            dictionary[word]=dictionary[word]+1

def main():
    dict = {}
    Text = ""
    print("Enter rows of text for word counting. Empty row to quit.")
    while True:
        Text = input("")
        if Text=="":
            break
        else:
            add(Text,dict)

    for key in sorted(dict):
        print(f"{key} : {dict.get(key)} times")


if __name__ == '__main__':
    main()
