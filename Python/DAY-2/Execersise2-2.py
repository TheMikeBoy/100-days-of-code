#If the year was division by 4 == 0 
#if the year was division by 100 !=0 
#unless this year was division by 400 
year = int(input("Give me a Year:" ))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0: 
            print(f"The Year {year} is a Leap Year ")
        else:
             print("this is not a leap year ")
    else:
         print("this is  a leap year ")
else:  
    print("this is not a leap year ")