weight = input("Please insert your weight: ") 
height = input ("please insert yout height: ")
total= int(weight) / (float(height) * float(height))
print ( str(weight )+ "÷" + str(height)+ "^2 = ", int(total))


#The functino round can be use to get results like 2.67
#if you use double slash // you get a integer like 8//3 

#you can use the F-string to write differents types in a single string without convert them, like this. print(f"your scores is {score})