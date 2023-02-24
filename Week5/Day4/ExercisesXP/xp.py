f = open('word_list.txt')
secret_data = f.read()


def get_words_from_file():
    collection = []
    for word in secret_data:
        collection.append(word)
    print(collection)

get_words_from_file()