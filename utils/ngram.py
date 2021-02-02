def ngram(doc, n, word_to_int):
    l = []
    size_of_doc = len(doc)
    for m in range(2, n + 1):
        for i in range(size_of_doc - m):
            l.append([''.join([token.text_with_ws for token in doc[i : i + m]]), word_to_int[doc[i + m].text]])
    return l