print("Tip calculator: ")
total_bill =  input("Whats is the total of the bill? $")
percent_tip = input("Whats percentage tip would you like to give? 10%, 12%, 13% ")
peoples =  input("How many people to slipt?" ) 


#just for fun I will do this (kkkkk )

total= round(((float(total_bill) * float("1." + percent_tip)) / float(peoples)),2)
print(f"Each person should pay: ${total}") 

#I mess around with string and types to make the percentage, was funy this. 



