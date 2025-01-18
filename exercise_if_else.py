
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

age = int (input("Enter your age: "))

if age >=18:
    print("You are old enough to drive")
else:
    years_to_wait= 18- age
    print(f"You need {years_to_wait} to learn to drive")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age= int(input("My Age: "))
your_age = int(input("Enter your age: "))

if your_age>my_age:
    age_diff= your_age - my_age
    if age_diff ==1:
        print("You are 1 year older than me. ")
    else: 
        print(f" You are {age_diff} older then me.")
elif your_age<my_age:
    age_diff=my_age-your_age
    if age_diff==1:
        print("I am 1 year older than you")
    else:
        print(f"I am { age_diff} years older than you")
else:
    print("We are same age. So we are bondhu")
