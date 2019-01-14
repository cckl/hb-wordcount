# put your code here.
# iterate over each line in the text, splitting it into lists of words
# iterate over those lists, counting the words
# add those words as keys to our empty dictionary and assign values (counts)

def count_words(filename):

    text_file = open(filename)

    words_dict = {}

    for line in text_file:
        line = line.rstrip()
        line = line.split(' ')
        for word in line:
            words_dict[word] = words_dict.get(word, 0) + 1

    #sorted(words_dict)
    #print(sorted(words_dict.values()))      
            
    for word, number in words_dict.items():
        print(f'{word} {number}')

    #print (words_dict)

count_words('test.txt')

