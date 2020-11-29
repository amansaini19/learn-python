print("Hello World!")

i = 5;
j = 3;
print("Sum : ", i+j)
print("Diff : " , i-j)
print("Product : " , i*j)
print("Modulo : " , i%j)
print("Floor Division : " , i//j)
print("Float Division : " , i/j)


# if-then
def weirdOrNot(n):
    if n%2 == 1  :
        print("Weird")
    elif n >=2 and n <=5 :
        print("Not Weird")
    elif n >=6 and n <=20 :
        print("Weird")
    elif n > 20 :
        print("Not Weird")

weirdOrNot(2)
weirdOrNot(3)
