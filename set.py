# 10-1-23
# set
# A Python program to
# demonstrate adding elements


# Creating a Set
people = {"Jay", "Jalpa", "Anjali"}

print("People:", end=" ")
print(people)

# This will add Suman
# in the set
people.add("Suman")

# Adding elements to the
# set using iterator
for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end=" ")
print(people)
