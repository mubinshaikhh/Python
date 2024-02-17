n = int(input("Enter number:"))
str_number = str(n)
def rev(n):
    if len(n)==0:
        return n
    else:
        return n[-1]+rev(n[:-1])
print("reversed number:",rev(str_number))
