def vowels(l):
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
    new_l = []

    for item in l:
        if type(item) == str:
            new_l.append(item)

    def calc_vowels(item):
        num_of_vowels = 0
        for char in item:
            if char in vowels_list:
                num_of_vowels += 1
        return num_of_vowels

    new_l.sort(key=calc_vowels)

    return new_l


print(vowels([1, 'hello', 'world', 'foo', 'bar', 'aaaa']))