total_sum = 0
exit_tag = 0


def add_func(my_str):
    global exit_tag, total_sum
    local_sum = 0
    my_str = " ".join(my_str.split())
    for c in my_str.split(' '):
        if c.isdigit():
            local_sum += float(c)
        elif c.lower() == 'q':
            exit_tag = 1
        else:
            print('Error')
    return local_sum


while exit_tag == 0:
    input_value = input('Введите числа с пробелами:')
    local_sum = add_func(input_value)
    total_sum += local_sum
    print(total_sum) if exit_tag == 1 else print(f'{local_sum}({total_sum})')
