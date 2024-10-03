"""
COMP.CS.100
Huyen Pham; huyen.pham@tuni.fi; 153151026
6.1.Project: Level Changes in Seawater
The program will received inputs of seawater levels and display the minimum, maximum, median, mean, deviation
"""
import math

def store_inputs():
    """
    Purpose: Stores the values entered by the users into a list.

    :return: A list with all the seawater level values
    """
    input_list = []
    number_list = []

    check = True
    while True:
        input_value = (input(""))
        if input_value == "":
            #Stop adding values to the list if enter key is pressed on a new line
            break
        else:
            input_list.append(input_value)

    for i in range (0,len(input_list)):
        # Change the items type to float and store in number_list
        number_list.append(float(input_list[i]))

    #Check to see if at least two measurements has been entered
    if len(number_list) >= 2:
        return number_list
    else:
        print("Error: At least two measurements must be entered!")

def median(input_list):
    """
    Purpose: Sort the list entered from small to big and find the median

    :param input_list: List of seawater level values
    :return: minimum value, maximum value, median
    """
    input_list.sort()

    #Assign the total number of values of the list as i
    i = len(input_list)

    #Check if the total number of values are odd or even to find the median
    if i%2==0:
        middle_index = int((i)/2)
        median = (input_list[middle_index]+input_list[middle_index-1])/2
    else:
        middle_index = int((i-1)/2)
        median = input_list[middle_index]

    return min(input_list), max(input_list), median

def mean(input_list):
    """
    Purpose: Calculate the mean of the list

    :param input_list: List of seawater level values
    :return: mean
    """
    sum = 0
    #Calculate the sum of the values
    for i in range (0, len(input_list)):
        sum = sum + input_list[i]
    mean = sum/len(input_list)
    return mean

def calculations(input_list, mean):
    """
    Purpose: Calcualte the variance to get the standard deviation

    :param input_list: List of seawater level values
    :param mean: The mean calculated with function mean above
    :return: standard deviation
    """
    numerator = 0
    #Calcualte the numerator part of the variance: (value-mean)²
    for i in range (0,len(input_list)):
        numerator = numerator + (input_list[i]-mean)**2

    variance = numerator / (len(input_list)-1)
    deviation = math.sqrt(variance)
    return deviation

def display(min,max,median,mean,deviation):
    """
    Purpose: Print the results with correct formatting
    :param: All 5 values required
    """
    print(f"Minimum:   {min:.2f} cm")
    print(f"Maximum:   {max:.2f} cm")
    print(f"Median:    {median:.2f} cm")
    print(f"Mean:      {mean:.2f} cm")
    print(f"Deviation: {deviation:.2f} cm")

def main():
    print("Enter seawater levels in centimeters one per line.\nEnd by entering an empty line.")
    seawater_list = store_inputs()
    # Chech that the list has values, if not the program stops
    if seawater_list is not None:
        min, max, med = median(seawater_list)
        average = mean(seawater_list)
        deviation = calculations(seawater_list, average)
        display(min,max,med,average,deviation)


if __name__ == '__main__':
    main()