def count_words():
    n_ish = int(input("Enter the number of words: "))
    counter_dict = {}
    words_list = []

    for i in range(n_ish):
        word = input("Enter a word: ")
        words_list.append(word)
        if word in counter_dict:
            counter_dict[word] += 1
        else:
            counter_dict[word] = 1

    print("Number of unique words:", len(counter_dict))
    print("Occurrences of each word:")
    print(' '.join([str(counter_dict[word]) for word in counter_dict]))
