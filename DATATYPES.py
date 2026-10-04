# python divides data types into two categories 
##mutable                         immutable 
##list,dictionary,byte array      numeric(int,float,complex),string,tuple,set
x=5
y=5.5
z=2+7j
print(x," is a type of ",type(x))
print(y," is a type of ",type(y))
print(z," is a type of ",type(z))

# string-it is a collection of one or more characters put in a single or double quote or triple quote 
## multi line strings can be denoted using triple quotes,'''or"""
a="hello himansu"
s=''' hello 
      himansu 
'''
print(a,"is a type of ",type(a))
print(s)## remember any value you are putting in quotes and printing its type it will show as string because it is in quotes 

#list-it is an ordered sequence of items  and it is created by [].
## it is one of the most used data types in python and is very flexible.
l=[20,"hs",34]
l[2]=25# you can update the values of list like this and i have written 2 in square bracket because i want to change the value according to index number 
print(l,type(l))

#tuple- it is an ordered sequence of items same as list 
## it is defined with in parenthisis () where items are separated by commas 
t=(10,20,"hello")# and in tuple the values can not be changed or updated 
print(t,type(t))
t=(10)
print(t,type(t))#it will not show the type as tuple it will show the type as the value in that paranthesis
 #Dictionary- it is an unordered collection of key value pairs 
 ## in python dictionaries are defined with braces {} with each item being a pair in the form of key value 
d={"course name" :"python","course duration":"9 days "}
print(d["course name"])# you can change and update data type in dictionary 
print(d,type(d))

# set- it is an unordered collection of items 
## every set element is unique (no duplicate) and must be immutable (cannot be changed)and it is defined in {}
s={10,220,30,30,10}
print(s,type(s))