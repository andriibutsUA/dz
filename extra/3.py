def check_alphabet(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in letters:
        if i not in s:
            return False
    return True

print(check_alphabet('abcdefghijklmnopqrstuvwxy'))