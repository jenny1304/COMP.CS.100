"""
COMP.CS.100 Programming 1
Huyen Pham; huyen.pham@tuni.fi; 153151026
9.9.Project: Course Registry
"""

def store_data(filename):
    """
    Read the data from the file and store it in a dictionary
    Return: A nested dictionary containing the data.
            The keys are department names and the payloads are
            dictionaries containing 'coursue_name' as key and 'credits' as payload.
    """
    #Initialize a new dictionary for data
    department_courses = {}
    try:
        data_file = open(filename, mode="r")

        for line in data_file:
            #Strip and split the line into 3 components
            component = line.strip().split(";")

            #Check whether the input file contains exactly three fields
            if len(component) != 3:
                print("Error in file!", end="")
                return

            #Name components for easier handling
            department_name, course_name, credits = component
            # Check if the department name already exist
            if department_name not in department_courses:
                #Creating new department if not found
                department_courses[department_name] = {}
            #Add the course and credits to the department payload as a dict
            department_courses[department_name][course_name] = credits

    #If there is an error, return none
    except IOError:
        print("Error opening file!", end="")
        return

    return department_courses


def print_all_data(department_courses):
    """
    Print in alphabetical order all the deparment names and the courses & credits they offer
    Parameter: The nested dictionary which contains department names, course names and credits
    """
    #Sort the department names in alphabetical order
    for department_name in sorted(department_courses.keys()):
        print(f"*{department_name}*")
        #Sort the courses in alphabetical order and print along with credits
        for course in sorted(department_courses[department_name].keys()):
            print(f"{course} : {department_courses[department_name][course]} cr")

def print_department_info(department_courses, department):
    """
    Print the names of the courses offered by a department in an alphabetical order
    Parameter:
        department_courses(dict): Contains department names, course names and credits
        department(str): The name of the department whose info should be printed
    """
    #Check if the specified department exist
    if department not in department_courses:
        print("Department not found!")
    else:
        print(f"*{department}*")
        # Sort the courses in alphabetical order and print along with credits
        for course in sorted(department_courses[department].keys()):
            print(f"{course} : {department_courses[department][course]} cr")


def calculate_total_credits(department_courses,department):
    """
    Print the total credits for a department
    Parameter:
        department_courses(dict): Contains department names, course names and credits
        department(str): The name of the department whose credits
         should be calculated
    """
    sum_credits = 0
    if department not in department_courses:
        print("Department not found!")
    else:
        #Accessing the course in the selected department
        for course in department_courses[department]:
            sum_credits += int(department_courses[department][course])
        print(f"Department {department} has to offer {sum_credits} cr.")

def add_course(department_courses, department, course, credits):
    """
    Add a new course for a given department
    Parameters:
        department_courses(dict): Contains department names, course names and credits
        department, course, credits (str): The name of the department and course and the credits
    """
    # If the department doesn't exist, a new department will be created
    if department not in department_courses:
        department_courses[department]={}
        print(f"Added department {department} with course {course}")
    else:
        print(f"Added course {course} to department {department}")

    # Add course and credits to department
    department_courses[department][course] = credits

def delete_department_or_course(department_courses, department, course):
    """
    Removes a department or course
    Parameters:
        department_courses(dict): Contains department names, course names and credits
        department, course (str): The name of the department and course
    """
    #Check the existent of the department
    if department not in department_courses:
        print(f"Department {department} not found!")
        return

    #If the course is not entered, only the department will be deleted
    if course == "":
        del department_courses[department]
        print(f"Department {department} removed.")
    else:
        #Check the existent of the entered course
        if course not in department_courses[department]:
            print(f"Course {course} from {department} not found!")
            return
        del department_courses[department][course]
        print(f"Department {department} course {course} removed.")

def main():
    file_name = input("Enter file name: ")
    department_courses = store_data(file_name)

    #If there is an error while reading the input file, the program ends immediately
    if department_courses == None:
        return

    while True:
        print("\n[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")
        #Split input to separate the department, course name, and course credits when needed
        user_input = input("Enter command: ").split()

        #In cases when the department is needed (add, calculate credit, print department info, delete)
        if len(user_input) >= 2:
            department = user_input[1].strip()

        print("")

        if user_input[0] == "p":
            print_all_data(department_courses)

        elif user_input[0] == "r":
            print_department_info(department_courses,department)

        elif user_input[0] == "c":
            calculate_total_credits(department_courses,department)

        elif user_input[0] == "a":
            #Check if the user has entered enough required info
            if len(user_input)>2:
                # Initialize a list that will contain the splitted words of the course name
                course_list = []
                #Add the words to the list
                for i in range(2, len(user_input)-1):
                    course_list.append(user_input[i])
                # Join the splitted words into one string
                course = " ".join(course_list)
                credits = user_input[-1].strip()
                add_course(department_courses,department,course,credits)
            else:
                print("Invalid command!")

        elif user_input[0] == "d":
            course_list = []
            for i in range(2, len(user_input)):
                course_list.append(user_input[i])
            course = " ".join(course_list)
            delete_department_or_course(department_courses,department,course)

        elif user_input[0] == "q":
            print("Ending program.", end="")
            return

        else:
            print("Invalid command!")

if __name__ == '__main__':
    main()
