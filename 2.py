def rows(template, word, num):
    return template % (word, num)

print(rows('%s speaks %d languages', 'Petro', 5))