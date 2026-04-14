def main():
    get_twtter()

def get_twtter():
    sents = input('Input: ')
    for x in sents:
        if x in ['a', 'e', 'i', 'o', 'u']:
            sents = sents.replace(x, '')
    print(f'Output: {sents}')

if __name__ == "__main__":
    main()