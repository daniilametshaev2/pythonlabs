def compress_string(s):
    compressed = []
    i = 0
    length = len(s)

    while i < length:
        char = s[i]
        count = 1
        i += 1
        while i < length and s[i] == char:
            count += 1
            i += 1
        if count > 1:
            compressed.append(char + str(count))
        else:
            compressed.append(char)

    return ''.join(compressed)

# Пример использования
decompressed_string= "YYYYYggkkkeeeAAAABVV"
compressed_string = compress_string(decompressed_string)
print(compressed_string)
