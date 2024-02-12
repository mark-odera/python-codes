#Write  a program that takes an integer as input and returns true if the input is a power of two.
 def is_power_of_two(n):
    #check if the number is positive and has only one set bit
    return n>0 and (n&(n-1))== 0

    #Test the function
    print(is_power_of_two(16))
     #output:true
    print(is_power_of_two(12))
     # output: False
