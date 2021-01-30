def ngram(doc, n, word_to_int):
    l = []
    size_of_doc = len(doc)
    for i in range(size_of_doc - n):
        l.append([''.join([token.text_with_ws for token in doc[i : i + n]]), word_to_int[doc[i + n].text]])
    return l