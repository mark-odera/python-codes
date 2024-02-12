#write a program that takes an interger as input and returns with reversed digit ordering.
def reverse_numbers(num):
    if num < 0:
        return int(str(num)[::-1][-1] + str(num)[:-1])
        else:
            return int(str(num)[::-1])

print(reverse_numbers(456))
