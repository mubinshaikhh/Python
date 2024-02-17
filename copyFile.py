#To copy the contents of one file to another

f=open('text.txt','r')
data=f.read()
f=open('a.txt','w')
f.write(data)
print("File copied successfully.")