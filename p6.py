# grade marking 

marks=int(input("Enter your marks: "))
if marks<0 or marks>100:
    print("Invalid marks")
    exit()
    
if marks>=90:
    print("Your grade is A+ \a") # \a is used to make a sound congo
elif marks>=80:
    print("Your grade is A")
elif marks>=70:
    print("Your grade is B+")
elif marks>=60:
    print("Your grade is B")
else:
    print("Very poor, you need to work hard")