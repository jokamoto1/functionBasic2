def countDown(top):
    for x in range (top, -1, -1):
        print(x)
def printAndReturn(print1, return1):
    print(print1)
    return return1
def firstPlusLength(list):
    a = len(list) + list[0]
    print(a)
    return a
def valueGreaterThan(list1):
    list2 = []
    e = len(list1)
    if e < 2:
        return False
    else:
        a = list1[1]
        for b in range (0, len(list1)):
            c = list1[b] 
            if a < c:
                print(list1[b]) 
        return(list1[b])
def lengthValue(len1, value1):
    list1 = []
    for x in range (0,len1,1):
        list1.append(value1)
    print(list1)
#firstPlusLength([2,2,3,4,5,6,7])
#countDown(5)
#printAndReturn(1,2)
#valueGreaterThan([2,3,4])
lengthValue(10000000,1)