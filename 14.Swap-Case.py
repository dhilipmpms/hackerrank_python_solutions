def swap_case(s):
    
    swap=[]
    
    for item in s:
        if item.isalpha():
            if item.islower():
                swap.append(item.upper())
            else:
                swap.append(item.lower())
        else:
            swap.append(item)

    return ''.join(swap)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
