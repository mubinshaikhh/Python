with open("text.txt","r") as f:
    file = f.read()
    print(file[::-1])