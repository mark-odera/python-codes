#write a program to generate the Fibonacci sequence up to 100

# Initialize variables
a, b = 0,1
#Generate the sequence up to 100
while a <= 100:
    print(a, end= '')
    a,b = b, a + b