for i in range(100):
    if i < 99:
        print(f"{i:02d}", end=", ")
    if i == 99:
        print(f"{i:02d}", end=""+ "\n")
