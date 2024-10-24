words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


def main():
    words_length = []
    for word in words:
        word_length = (word, len(word))
        words_length.append(word_length)
    print(words_length)


if __name__ == "__main__":
    main()
