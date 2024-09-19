"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(weight,time,totalDoze):
    """calcualte the dose
    1. Check the time
    2. Check the max dose using weight
    3. Check the total dose taken before"""
    if time<6 or totalDoze>=4000:
        return 0
    elif time == 24:
        return weight*15
    else:
        if weight * 15 < 1000 and totalDoze <= 3*weight * 15:
            return weight*15
        elif weight * 15 > 1000 and totalDoze <= 3*((weight * 15 * 4)-4000):
            return ((weight * 15 * 4)-4000)
        elif totalDoze > 3*((weight * 15 * 4)-4000):
            return 4000 - totalDoze
def main():
    weight = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    total_doze_24 = int(input("The total dose for the last 24 hours (mg): "))
    ans = calculate_dose(weight,time,total_doze_24)
    print(f"The amount of Parasetamol to give to the patient: {ans}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
