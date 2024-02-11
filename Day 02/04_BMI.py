Height = float(input("Enter your height in m: "))
Weight=float(input("Enter your weight in kg: "))
BMI_Cal=Weight/Height**2
BMI=int(BMI_Cal)#Type Conversion  from Float to Integer
print(BMI)