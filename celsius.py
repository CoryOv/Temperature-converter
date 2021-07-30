c = "celsius"
f = "fahrenheit"
#c/5 = f - 32/9
# def temp_conversion(scaleF=None, scaleC=None, temp=None):
#     if scaleF == "F":
#         return(temp - 32.0) * (5.0/9.0)
#     elif scaleC == "C":
#         return(temp * (9.0/5.0)) + 32.0
#     else:
#         print("Needs to be (F) or (C)!")
# scaleF = input("Select (F) or (C): ")
# temp = int(input("What is the temperature: "))
# m = temp_conversion(scaleF, scaleC, temp)
# print(temp, "degrees", scaleF, "is", m, "degrees", scaleC)


# C = 5/9 * (F – 32)
# F = (C * 9/5) + 32
# scale = input("select F or C")
# temp = int(input("What is the temp? "))

# if scale == "C":
#     C
#     print("Temp in F is .")
# else scale == "F":
#     F 
#     print("Temp in C is .")

temp = input("Input the temperature you would like to convert? (e.g., 45F, 102C etc.) : ") #float includes decimals
degree = float(temp[:-1]) #cuts last character off
i_convention = temp[-1] #only looks at last character

if i_convention.upper() == "C":
  result = float((9 * degree) / 5 + 32)
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = float((degree - 32) * 5 / 9)
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")