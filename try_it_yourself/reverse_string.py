def word_count(string):
    """Returns amount of words in a given string"""
    list_of_words = string.split(" ")
    return len(list_of_words)

my_string = "Hello world, how are you doing this fine day?"
amount_of_words = word_count(my_string)

print(amount_of_words)