#write a program that counts the number of vowels in a sentence.
def vowel_count(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for char in sentence:
        if char in vowels:
            count += 1
    
    return count

code = "Hello World"
print(count_vowels(code))