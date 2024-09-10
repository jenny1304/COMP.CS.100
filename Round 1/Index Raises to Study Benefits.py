"""
COMP.CS.100 The first Python program.
Creator: Huyen Pham
"""

stringBenefits = input("Enter the amount of the study benefits: ")
benefits = float(stringBenefits)
std = benefits* (1.17/100) + benefits
print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", std,  "euros")
benefits = std
std = benefits* (1.17/100) + benefits
print("and if there was another index raise, the study")
print("benefits would be as much as", std, "euros")
