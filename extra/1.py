def count_chars(s):
    my_dict = {}
    for i in s:
        current_char = i
        if current_char in my_dict:
            my_dict[current_char] += 1
        else:
            my_dict[current_char] = 1
    print(my_dict)

count_chars('ababahalamaha')