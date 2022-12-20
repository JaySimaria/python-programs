def merge_two_sorted_lists(a,b):
    sorting_list=[]
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorting_list.append(a[i])
            i+=1
        else:
            sorting_list.append(b[j])
            j+=1
    

    return sorting_list


if __name__ == '__main__':
    a = [2,4,6,7,8]
    b = [1,3,9,5,6]

    print(merge_two_sorted_lists(a,b))
