#write a program that accepts a string as input,capitalizes the first letter of each word in the string and then returns the result string

def capitalize_words (input_string):
    words = input_string.split()
    capitalized_words = [word.capitalize() for woed in words]
    result_string = ''.join(capitalized_words)
    return result_string

insta = "hi"
result1 = capitalize_words(insta)
print(result1)

feska = "ilove python programming"
result2 = capitalize_words(feska)
print(feska)



