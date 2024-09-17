"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""
def print_verse(animal,noise):
    """Print the verse, animal and noise are string parameters"""
    print(f"Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {noise} {noise} here")
    print(f"And a {noise} {noise} there")
    print(f"Here a {noise}, there a {noise}")
    print(f"Everywhere a {noise} {noise}")
    print("Old MacDonald had a farm\nE-I-E-I-O")

def main():
    print_verse("cow", "moo")
    print("")
    print_verse("pig", "oink")
    print("")
    print_verse("duck", "quack")
    print("")
    print_verse("horse", "neigh")
    print("")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
