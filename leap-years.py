#get the year and answer if it's leap year or not

#ask user enter a year
year=int(input("which year do you want to check?"))

if year%4==0:
    if year%100!=0:
        print(f"{year} is a leap year")
    else:
        if year%400==0:
             print(f"{year} is a leap year")
        else:
             print(f"{year} is not a leap year")     
                
else:
     print(f"{year} is not a leap year")        

     