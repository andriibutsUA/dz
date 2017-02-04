def sort_versions(v):
    my_list = []
    for i in v.split('.'):
        my_list.append(int(i))
    return my_list

versions = ['1.22.8.47', '1.2.9', '1.5.3.45', '1.6.1', '1.8.2.4', '2.0']

versions.sort(key=sort_versions)
print(versions)