
# arithmatic operators=add=+,substratct=-,divide=/,multiply=*,modulus=%,power or exponents=**,floor division=//
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a%b)
print(a//b)

#assignment operator is (=) and it can be used with arithmatic operators for increment and decrement like (+=)and (-=)
x=5
print(x)
x+=5 #x=x+5
print(x)
x-=5 #x=x-5
print(x)

#comparison operators are used for comparing two or more variables
##and these are equal(==),not equal(!=),grater than(>),smaller than(<),grater than or equal to (>=)and smaller than or equal to (<=)
x=5
y=2
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y) # if any one of the condition like if it is greater but not equal to then still it  will give output as true because two operators are used to compare 
print(x<=y) #same for this one also

#logical operators 
##and(it is used check and get output if all the statements are true )
##or(it is used check and get output if one of the statements is  true )
##not(it is used to reverse the output and return false if the result is true)
print(x>y and x<y)
print(x==y or x>y)
print(not(x>y))
#membership operator
##in(it checks and return true if a sequence with the specified value is present in the object)
##not in(it checks and return true if a sequence with the specified value is not present in the object)
string1="himansu"
print("h" in string1) #remeber PYTHON is a case sensitive language so  if you mistkely typed capital h(H) it will give the result as false
print("h" not in string1)# if h was not there so it must have printed true but h is there in hello so it printed false

#identity operator
##is(it checks and return true if both the variables are the same object) and it is the alternative of equal comparision operator
##is not(it checks and return true if both the variables are not the same object) and it is the alternative of not equal comparision operator
z=5
print(x is y,x==y)
print(x is z,x==z)
print(x is not y,x!=y)
print(x is not z,x!=z)
#Bitwise operator       TRUTH TABLE 
##&(and)           A    B   A&B  A|B  A^B
##|(or)            0    0    0    0    0  
##^(xor)           0    1    0    1    1  
##                 1    0    0    1    1
##                 1    1    1    1    0
print(bin(x)) #0b101 and ignore 0b and rest is thebinary of x and y
print(bin(y)) #0b010
# and there are 3 results of using these operators and the results are derived by the conditions given in the truth table by their binary values
print(x&y)    #0
print(x|y)    #7
print(x^y)    #7