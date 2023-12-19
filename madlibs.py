#madlib is a program which can take user input and return string value with user name
Employee = "Hariyalni" #variable

#method we can use
print("Hi,"+Employee+ " "+ "welcome abord!")
print ("Hi, {} welcome abord!".format(Employee))
print(f"Hi, {Employee} welcome abord!")


Employee = input("Employee Name:")
noun1 = input("Team Name:")
noun2 = input("Job Role:")
madlib = f"Welcome aboard {Employee}, we are so exited to see here! \
We heard someone awesome was joining our team {noun1}, and that person is you!\
Congrats on the new role {noun2}!"

print(madlib)