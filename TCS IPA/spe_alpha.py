def str_num_list(s1):
    str_num = []

    alpha = ''.join([i for i in s1 if i.isalpha()])
    print(type(alpha))
    print(alpha)
    str_num.append(alpha) if len(alpha) != 0 else str_num
    
    num = ''.join([i for i in s1 if i.isdigit()])
    type(num)
    str_num.append(int(num)) if len(num) != 0 else str_num
    
    return str_num

inp_s = input()
ans = str_num_list(inp_s)
print(ans)
