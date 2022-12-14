# 14-12-2022
# bubble sort example
def bubblesort(elements):
    size = len(elements)

    for i in range(size - 1):
        # compare both elements
        if elements[i] > elements[i + 1]:
            temp = elements[i]
            elements[i] = elements[i + 1]
            elements[i] = temp


if __name__ == '__main__':
    elements = [
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'}, ]
    bubblesort(elements, key='transaction_amount')
    print(bubblesort)
