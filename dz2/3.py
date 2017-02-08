my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

double = list(map(lambda key: my_dict[key]*2, my_dict))

print(double)

my_versions = ['1.22.8.47', '1.2.9', '1.5.3.45', '1.6.1', '1.8.2.4', '2.0']
my_versions.sort(key=lambda x: [int(y) for y in x.split('.')])
print(my_versions)