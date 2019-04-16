first_name = 'david'
last_name = 'jones'
age = 18
city = 'dallas'
state = 'texas'
car = 'honda'
high_school_grad = True
college_grad = False
job_title = 'chef'
hourly_pay = 10

print("Your name is David Jones.")
print(first_name == 'david' and last_name == 'jones')

print("You are old enough to drink.")
print(age >= 21)

print("You live in Dallas, Kansas.")
print(city == 'dallas' and state == 'kansas')

print("You live in Dallas, Texas.")
print(city == 'dallas' and state == 'texas')

print("You have a car.")
print(car != 'none')

print("You are educated.")
print(high_school_grad == True or college_grad == True)

print("You have graduated from college.")
print(college_grad == True)

print("You don't work.")
print(job_title == 'none')

print("You are a chef.")
print(job_title == 'chef')

print("You make more than 10 dollars an hour.")
print(hourly_pay > 10)