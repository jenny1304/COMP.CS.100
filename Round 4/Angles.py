"""
COMP.CS.100
huyen.pham@tuni.fi
"""
def calculate_angle( angle1,angle2=90):
    """print the 3rd angle
    If the triangle is a right triangle, only 1 value needs to be enetered"""
    return 180-angle1-angle2

def main():
    print(calculate_angle(30))

if __name__ == '__main__':
    main()