s = input("Enter String:")
with open("text.txt","a") as f:
    f.write(s)
print("Stirng added to the text.txt file.")