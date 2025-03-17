'''
Define a function to count the frequency of words in a given list of words.
Example:
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
Output: {'apple': 3, 'orange': 2, 'banana': 1}
'''

def count_word_frequency(words):
    count = {}.fromkeys(words,0)
    for items in words :
        count[items] += 1
    return count

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(count_word_frequency(words))

'''
def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
'''