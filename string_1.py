a="himansu"
b="sekhar"
print(a+" "+b)# it is valid 
c=25
d=25
print(c+d) #it is valid
# but if you print (a+cit is not valid because in python it can add int to int or any data type to its same data type so it will show error
# String indexing and string slicing in ;ython 
w="himansu to python"
print(w[3])  # Access the first character
print(w[-4])
##string slicing 
print(w[0:10]) ## according to index number it will print
print(w[0:10:2]) # it will print every second character
print(w[-1::-1]) #it reverse the string 
## string iteration
w1=w[-1::-1]
for i in w1:
    print(i) # it will print every character in new line
   ##t=len(w)
    ##print(t) # it will print the length of string ## index number =17
## string functions in python
## lower() function
##Upper() function
##title() function
##capitalize() function
##find() function
##index() function
##isalpha() function
##isdigit() function
##isalnum() function
##isupper() function
w2="HELLO WORLD"
print(w2.capitalize()) ## it will make first character capital and rest will be small letter
print(w2.lower()) ## it will make all character small letter
print(w2.upper())  ## it will make all character capital lett
print(w2.title()) ## it will make first character of every word capital letter
print(w2.find("HELLO")) ## it will return the index number of the first character of the word
print(w2.index("WORLD")) ## it will return the index number of the first character of the word
print(w2.isalpha()) ## it will return false because it contains space AND IT HAS DIGIT
print(w2.isdigit()) ## it will return false because it contains  SPACE HAS ALPHABET
print(w2.isalnum()) ## it will return false because it contains space AND IFIT HAS SPECIAL CHARACTER ALSO IT WILL RETURN FALSE
print(w2.isupper()) ## it will return true because all character are in upper case
## FUNCTIONS OF PYTHON 
## CHR() AND ORD() FUNCTION
print(chr(65))  ## it will return the character of the ASCII value 65
print(ord("A"))  ## it will return the ASCII value of the character "A"
## python string formatting method = by using format() function and curly braces {} you can insert the specified values inside the string placeholder section.
w3="hello {} welcome to {}"
print(w3.format("himansu","python")) ## it will replace the placeholder with the specified values in the order they are passed to the format() method.  
w4="hello {a:>10} welcome to {b}"## and in place of only a you can write a:10,or b:20 or a^(center) or b^(right) or a^(left) or b^(center) etc and this 10 0r any number you are using after colon that is character width . 
print(w4.format(a=30,b=40))
