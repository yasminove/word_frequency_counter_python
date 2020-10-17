def word_frequency(list):
    words = {}
    for word in list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


frequency_counter = word_frequency(['hey', 'hi', 'more', 'hey', 'hi'])

print(frequency_counter)
