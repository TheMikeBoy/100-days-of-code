#exercise to calculate how many days, weeks and months do you have if you going to live until 90 years old 
your_age = input ("how many years do you have? ")

until_age = 90 - int(your_age)
days_alive = until_age * 365 
months_alive = days_alive // 30 
weeks_alive = days_alive // 7
print( f"You have {days_alive} days, {weeks_alive} weeks and {months_alive} months ")