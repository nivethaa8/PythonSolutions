word_so_far = ['a', 'b', 'c']
my_word = word_so_far[:]
my_word = ''.join(my_word)

print(type(my_word))

print(my_word)
print(word_so_far)


word_so_far.append('d')
print(my_word)
print(word_so_far)

word_so_far.clear()

print(my_word)
print(word_so_far)