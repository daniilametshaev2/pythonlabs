def decompress_string(s):
    decompressed = []
    i = 0
    length = len(s)

    while i < length:
        char = s[i]
        i += 1
        count = 0

        while i < length and s[i].isdigit():
            count = count * 10 + int(s[i]) 
            i += 1

        if count == 0:
            count = 1

        decompressed.append(char * count)

    return ''.join(decompressed)

compressed_string = "Y4g2ke3A3BV"
decompressed_string = decompress_string(compressed_string)
print(decompressed_string) 