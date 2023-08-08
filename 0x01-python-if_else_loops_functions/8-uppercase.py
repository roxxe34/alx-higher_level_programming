def uppercase(string):
    for i in string:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
            print(f"{i}", end ="")
    print("")
