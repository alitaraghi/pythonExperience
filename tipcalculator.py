#Tip calculator

#welcome message
print("Welcome to the Tip calculator")

#ask user the whole bill price
bill=float(input("What was the total Bill?\n"))

#Ask the number of people they should pay
people=int(input("How many people to split the bill?\n"))

#Choose the rate of Tip
tip_percentage=0
while True:
    tip_percentage=int(input("What percentage tip would you like to give? 10,12,or 15?\n"))
    if tip_percentage==10 or tip_percentage==12 or tip_percentage==15:
        break
# Calculate Each person Share
share=round((bill+(bill*tip_percentage/100))/people , 2)
#show the answer
print(f"Each person should pay: {share:.2f}")
