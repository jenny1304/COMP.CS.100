"""
COMP.CS.100 Programming 1
"""

def read_file(file_name):
    """
    create a dict in dict from the csv file
    """
    try:
        data_file = open(file_name, mode="r")

        info = {}

        row = data_file.readline().strip()

        parts= row.split(";")

        for line in data_file:
            line = line.split(";")

            info[line[0]]={parts[1]:line[1], parts[2]:line[2], parts[3]:line[3] }

            if len(line)>=5:
                info[line[0]][parts[4]]=line[4].strip()

    except OSError:
        print(FILE_ERROR_MESSAGE)

        # Return the data or the error code.
    return info

i