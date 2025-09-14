#Write a program to check whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as input from the user.
m1=int(input("Enter your marks in math: "))
m2=int(input("Enter your marks in science: "))
m3=int(input("Enter your marks in english: "))

total=m1+m2+m3
p=(total/300)*100 #percentage
print("PASS MARKS=33")
if m1<33 or m2<33 or m3<33:
    print("You are fail due to less marks in either one subjects")
elif p<40:
    print("You are fail due to less percentage")
else:
    print("Congratulations! You are pass")
    
print("Your percentage is: ",p)   
print("You scored", m1,"in math,", m2,"in science and", m3,"in english")    