def ssort(a):
    #assert: a[0...n-1] is established
    i=0 #left pointer
    m=0 #mid pointer
    j=len(a)-1 #right pointer
    #INV: all the list is sorted till elements less than m 
    
    while m<=j:
        #assert: We increment m with 1 if a[m]=3
        if a[m]==3:
            m+=1
        elif a[m]==2:
            #If a[m]=2 swap the left pointer element with the mid element and increment both i and m by 1
            a[i],a[m]=a[m],a[i]
            i+=1
            m+=1
        else:
            #If a[m]=5 then decrement right pointer by 1 and swap the a[m] and a[j]
            a[m],a[j]=a[j],a[m]
            j-=1
    return a

N= 101

i = 0
a = []

while (i < N): 
    x=random.randint(2,3)
    y=random.randint(5,5)
    a.append(x)
    a.append(y)        
    i = i+1
# print(a)
print(ssort(a))
