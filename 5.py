def srt(versions):

    def to_float(n):
        temp = ''
        if '.' in n:
            index_of_dot = (n.index('.'))
            temp += n[:index_of_dot+1]
            for k in range(index_of_dot, len(n)):
                if n[k] != '.':
                    temp += n[k]
            return float(temp)
        else:
            return float(n)
    versions.sort(key=to_float)
    return versions

print(srt(['22', '22.5', '5', '1.8.2.4', '1.5.3.45', '1.6.1', '1.2.8.47', '1.2.9', '2.0']))