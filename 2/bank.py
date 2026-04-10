def main():
    words = input("How to say:").strip().lower()
    if words.startswith('hello'):
        print('$0')
    elif words.startswith('h'):
        print('$20')
    else:
        print('$100')


main()