def detector(word):
    ''' This  program detect if there is any duplicate letter'''
    
    list_word = list(word)
    new_word =[]
    for all_letters in list_word:
        if all_letters not in new_word:
            new_word.append(all_letters)
        else:
            return 'The word {} has duplicate letter'.format(word)
    return 'The word {} has no duplicate letter'.format(word)

print(detector(input('enter word or sentence: ')))
