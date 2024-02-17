n = input("Enter string:")
def rev(n):
    if len(n)==0:
        return n
    else:
        return n[-1]+rev(n[:-1])

print("Reversed string:",rev(n))
