weight = input("Please insert your weight: ") 
height = input ("please insert yout height: ")
total= int(weight) / (float(height) * float(height))


if round(total, 1) < 18.5:
    print(f"your BMI is {total}, you are underweight ")
elif round(total, 1) < 25:
    print(f"your BMI is {total}, you  have a normal weight ")
elif round(total, 1) < 30:
    print(f"your BMI is {total},  are slightly overweight " )
elif round(total, 1) < 35:
    print(f"your BMI is {total},  are obese " )
else:
   print(f"your BMI is {total},  you are Clinically obese " )


#The functino round can be use to get results like 2.67
#if you use double slash // you get a integer like 8//3 

#you can use the F-string to write differents types in a single string without convert them, like this. print(f"your scores is {score})