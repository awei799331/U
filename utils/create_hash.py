def create_word_to_int(doc):
  word_to_int = {None: 0}
  for i, word in enumerate(set([j.text for j in doc])):
    word_to_int[word] = i+1
  return word_to_int

def create_int_to_word(word_to_int):
  int_to_word = {i: word for word, i in word_to_int.items()}
  return int_to_word