#if statement 
## if statement is used with the condition so if the condition is not showed the true then program will not give the output
a=int(input("enter the number : "))
if a%2==0:
    print(a,"is a even number")
#if-else statement 
#previously if the condition applied with f is not true then it will not give the output but here in if-else statement else is used for if then condition is not true and still you want to print something for the error or for different answer so in this case else is used 
#else :
    print(a,"is a odd number")

#if elif statement 
##these are used to check the condition afterif like if the condition is not true by if then it will checked by elif and if the condition is still not true bu elif it will go to else and then the final output will be given by this 
elif a>=2:
    print("you are very close to the first even number")

# make a calculator using if elif and else satement which will perform all the mathematic calculation
num1=int(input("enter the value of number 1 : "))
num2=int(input("enter the value of number 2 : "))
opr=input("enter the value of opreation you want to perform :")
if opr=="+":
     print("the adiition of two numbers given are :",num1+num2)
elif opr=="-":
    print("the substraction of the given two numbers are :",num1-num2)
elif opr=="/":
    print("the division of the two numbers are :",num1/num2)
elif opr=="*":
    print("the multiplication of the two numbers are :",num1*num2)
else:
    print("invalid operation")

