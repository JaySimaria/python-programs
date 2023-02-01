# 1-2-23
# to print reverse string
while True:
    word = input('Enter a string and I will print it backwards(type q to quit): ')
    if word == 'q':
        break
    print(word[::-1])