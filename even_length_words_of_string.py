# 21-7-22
# to print even length of a string
# Input string
n = 'One minute next minute up'
# splitting the words
j = n.split(" ")
for i in j:
        # checking the length of words
        if len(i)%2==0:
          print(i)

