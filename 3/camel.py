def main():
    words = get_words()
    turn_words(words)

def get_words():
    a = input("Please enter the camel name:")
    return a
def turn_words(word):
    for a in word:
        if a.isupper():
            print(f"_{a.lower()}", end="")
        else:
            print(f"{a}", end = "")

if __name__ == '__main__':
    main()