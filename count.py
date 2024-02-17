#To count occurences of a word in a txt file

f = open('text.txt','r')
data = f.read()
o = data.count(input("Enter a string: "))
print("String present:",o)