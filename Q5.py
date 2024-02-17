def sumrec(list1):
    if len(list1)==0:
        return 0 
    else:
        return list1[0]+sumrec(list1[1:])
list1 = [1,2,3,4]
sumrec(list1)