#heads or tails. 
import random 
choice = input("heads or tails?").lower()
#choice = choice1.lower()
result = random.randint(0,1)
print(f"your choice was {choice}")
if result == 0 :
    if choice == "heads":
        print ("You Win!! The result was heads")
    else:
         print ("You loose!! The result was heads")
else:
    if choice == "tails":  
        print ("You Win!! The result was tails")
    else:
        print ("You loose!! The result was tails")




