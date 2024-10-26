"""
COMP.CS.100 Programming 1
"""
def main():
    stored = {}
    name = input("Enter the name of the score file: ")

    try:
        score_file = open(name, mode="r")
    except OSError:
        print(f"There was an error in reading the file.")
        return

    for line in score_file:
        if " " not in line:
            print("There was an erroneous line in the file:")
            print(line, end="")
            return

        part = line.strip().split()

        person = part[0]

        try:
            score = int(part[1])
        except ValueError:
            print("There was an erroneous score in the file:")
            print(part[1], end = "")
            return

        if person in stored:
            stored[person]+=score
        else:
            stored[person]=score

    print("Contestant score:")
    for name in sorted(stored):
         print(f"{name} {stored[name]}")


if __name__ == '__main__':
    main()