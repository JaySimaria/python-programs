# 16-1-23
# dictionary example
Employee = {"Name": "David", "Age": 30, "salary":55000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
print("Enter the details of the new employee....")
Employee["Name"] = input("Name: ")
Employee["Age"] = int(input("Age: "))
Employee["salary"] = int(input("Salary: "))
Employee["Company"] = input("Company:")
print("printing the new data")
print(Employee)
