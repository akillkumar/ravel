#part a
import random
n=20
L = list(range(n))
random.shuffle(L)

#part b
array=[]
def sorter(L,n):
    evenArr = [] 
    oddArr = [] 
    for i in range(n): 
        if ((i % 2) == 0): 
            evenArr.append(L[i]) 
        else: 
            oddArr.append(L[i]) 

    # sort evenArr[] in ascending order 
    # sort oddArr[] in descending order 
    evenArr = sorted(evenArr) 
    oddArr = sorted(oddArr)

    L[::2] = evenArr
    L[1::2]= oddArr
       

#part c
def triadSort(L, n):
    count = 0
    triad = []
    newList = []
    for i in range(n):
        # when we have one full triad, sort and reset
        if (count == 3):
            newList.extend (sorted(triad))
            #print (newList)
            triad = []
            count = 0

        if (count < 3):
            triad.append(L[i])
            count += 1
    
    newList.extend ((sorted(triad)))
    print(newList)

    


sorter(L, 20) 
print(L)

triadSort (L, 20)