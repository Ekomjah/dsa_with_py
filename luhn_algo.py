def verify_card_number(str):
    str = str.replace("-","").replace(" ","")
    arr = list(str)
    list_to_double = arr[-2::-2]
    odd_index = arr[-1::-2]
    total = 0
    total += sum([int(x) for x in odd_index])
    for val in list_to_double:
        tot = int(val) * 2
        if tot > 9:
            tot -=9
        total+=tot
    return 'VALID!' if (total % 10) == 0 else 'INVALID!'
    # sum = 0
    # for index,val in enumerate(arr):
    #     if index < len(arr) -1:
    #         sum += (int(val) * 2) % 9
    #     else:
    #         sum+=int(val)
    # print(sum)
    # return 

print(verify_card_number('453914889'))