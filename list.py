## list(it is always declared in the square brackets [] and it is mutable and it is placed in a comma separated values and it can contain any data type like string, int, float, boolean, list, tuple, set, dictionary etc)
l1=[1,2,3,4,5,6,7,8,9]
l2=["himansu","sekhar","python"]
l3=[1,4,"himansu",[2,4,8]]
print(l1, type(l1),l1[0::2])
print(l2, type(l2))
print(l3[3], type(l3[3]))
## list iteration
for i in l1:
    print(i) # it will print every element in new line
## list comprenhension 
l=[i for i in range(1,100)if i%2==0] # it will print the list of even numbers from 1 to 10
print(l)
## functions of list in python
##append() function
print(l1.append(10)) # it will add the element at the end of the list
print(l1)
##extend() function
print(l1.extend([11,12,13])) # it will add the elements at the end of the list
print(l1)
##insert() function
print (l1.insert(2,15)) # it will add the element at the specified index number
print(l1)
##remove () function
print(l1.remove(15)) # it will remove the specified element from the list   
print(l1)
##pop() function
print(l1.pop(2)) # it will remove the element at the specified index number
print(l1)
## del() function
del l1[2] # it will remove the element at the specified index number
print(l1)
##clear() function
print(l1.clear()) # it will remove all the elements from the list
print(l1)
## count() function
l1=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
print(l1.count(1)) # it will return the count of the specified element in the list  
## max() function
print(max(l1)) # it will return the maximum element from the list
print(l1)
## min() function
print(min(l1)) # it will return the minimum element from the list
print(l1)
## sort() function
print(l1.sort()) # it will sort the list in ascending order 
print(l1)
## reverse() function
print(l1.reverse()) # it will reverse the list
print(l1)
## index() function
print(l1.index(5)) # it will return the index number of the specified element in
print(l1)
## zip function 
l1=[1,2,3,4,5]
l2=["himansu","sekhar","python"] 
for i in zip(l1,l2): # it will return the tuple of the specified elements from the list.
    print(i)  ## if the length of the list is not same then it will return the tuple of the minimum length of the list.
    ## convert string to a list 
    s="himansu sekhar python"
    l=list(s)
    l1=s.split() # it will convert the string to a list of words
    print(l,l1)
    l=[]
    for a in range(1,6):
        n=input("enter the value:"+str(a)+":") # it will take the input from the user and store it in the list

        l.append(n) # it will add the element at the end of the list
    print(l)
    ## implement a stack and queue using a list data type 
    ## stack is a linear data structure that follows the LIFO(Last In First Out) principle. It means that the last element added to the stack will be the first one to be removed.
l=[]
while True:
    print("1. push")
    print("2. pop")
    print("3. display")
    print("4. exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        n=input("enter the value:")
        l.append(n)
    elif choice==2:
        if len(l)==0:
            print("stack is empty")
        else:
            print("popped element is:",l.pop())
    elif choice==3:
        print(l)
    elif choice==4:
        break
    else:
        print("invalid choice")

## queue is a linear data structure that follows the FIFO(First In First Out) principle. It means that the first element added to the queue will be the first one to be removed.
l=[]
while True: 
    print("1. enqueue")
    print("2. dequeue")
    print("3. display")
    print("4. exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        n=input("enter the value:")
        l.append(n)
    elif choice==2:
        if len(l)==0:
            print("queue is empty")
        else:
            print("dequeued element is:",l.pop(0))
    elif choice==3:
        print(l)
    elif choice==4:
        break
    else:
        print("invalid choice")



