test_string = input('Please Input Your Sentence: ')

# printing original string
print("The original string is : " + test_string)

# using split()
# to count words in string
WordNumber = len(test_string.split())

# printing result
print("The number of words in string are : " + str(WordNumber))