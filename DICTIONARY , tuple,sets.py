##Dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are mutable, meaning that they can be changed after they are created. They are defined using curly braces {} and the key-value pairs are separated by colons (:).
##The keys in a dictionary must be of an immutable data type, such as strings, numbers, or tuples. The values can be of any data type, including other dictionaries.
##Dictionaries are unordered, meaning that the order of the key-value pairs is not guaranteed.
d={"name":"himansu","age":21,"gender":"male"}
print(d,type(d),d['age']) # it will print the value of the specified key in the dictionary
##for i in d:  # it will print the keys of the dictionary
    ##print(i,d[i])

    ## functions in dictionary
    ###get() function
print(d.get("name")) # it will return the value of the specified key in the dictionary
    ## keys() function
print(d.keys()) # it will return a list of all the keys in the dictionary
    ## values() function
print(d.values()) # it will return a list of all the values in the dictionary
    ## items() function
print(d.items()) # it will return a list of all the key-value pairs in the dictionary  
    ##del() function
del d["age"] # it will remove the specified key-value pair from the dictionary
print(d)
    ##clear() function
d.clear() # it will remove all the key-value pairs from the dictionary
print(d)
    ##pop() function
d={"name":"himansu","age":21,"gender":"male"}
print(d.pop("name")) # it will remove and return the value of the specified key from the dictionary
print(d)
    ##dict () function
d1=dict(name="himansu",age=21,gender="male") # it will create a dictionary from the specified key-value pairs
print(d1)
    ##update() function
d1.update({"name":"sekhar"}) # it will update the value of the specified    key in the dictionary
print(d1)   
    ###copy() function
d2=d1.copy() # it will create a copy of the dictionary  
print(d2)
    ##nested dictionary- it is a dictionary that contains another dictionary as a value for one of its keys. It allows for more complex data structures and can be used to represent hierarchical relationships between data.
d3={"name":"himansu","age":21,"gender":"male","address":{"city":"delhi","state":"delhi","country":"india"}} # it will create a nested dictionary
print(d3)
##Tuple-it is a collection of ordered, immutable elements. Tuples are defined using parentheses () and can contain any data type, including other tuples. Tuples are often used to group related data together and can be used as keys in dictionaries or elements in sets.
t=(1,2,3,4,5)
t1=("python",)## if you will write a single element in a tuple then you have to put a comma after the element otherwise it will be considered as a string or int or any other data type.
print(t,type(t),type(t1),t[0]) # it will print the value of the specified index in the tuple
for i in t:  # it will print the elements of the tuple in iteration
    print(i)
## functions in tuple
    ##count() function
print(t.count(1)) # it will return the count of the specified element in the tuple
    ##index() function
print(t.index(1)) # it will return the index of the specified element in the tuple
##len() function
print(len(t)) # it will return the length of the tuple
##sum() function
print(sum(t)) # it will return the sum of the elements in the tuple and it will only work with the tuple of int or float data type
##min() function
print(min(t)) # it will return the minimum element in the tuple
##max() function
print(max(t)) # it will return the maximum element in the tuple 
## set-it is a collection of unordered,unindexed mutable elements. Sets are defined using curly braces {} or () and can contain any data type, including other sets. Sets are often used to remove duplicates from a list or to perform mathematical operations such as union, intersection, and difference.
s={1,2,3,4,5,6,7,8,9}
s1={1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9} # it will remove the duplicate elements from the set
print(s,type(s),s1) # it will print the set and its type and it will remove the duplicate elements from the set 
##functions in set
    ##add() function
s.add(10) # it will add the specified element to the set
###remove() function
s.remove(10) # it will remove the specified element from the set and if the element is not present in the set then it will give an error
print(s)
##discard() function
s.discard(10) # it will remove the specified element from the set and if the element is not present in the set then it will not give an error
print(s)
###pop() function
s.pop() # it will remove and return a random element from the set   
print(s)
##set () function
s2=set([1,2,3,4,5,6,7,8]) # it will create a set from the specified list
print(s2)
##union() function
s3=s.union(s2) # it will return a set that contains all the elements from both sets and it will remove the duplicate elements from the set
print(s3)
##clear() function
s3.clear() # it will remove all the elements from the set
print(s3)
##intersection() function
s4=s.intersection(s2) # it will return a set that contains only the elements that are present in both sets
print(s4)
##update() function
s.update(s2) # it will add the elements from the specified set to the set and it will remove the duplicate elements from the set
print(s)







