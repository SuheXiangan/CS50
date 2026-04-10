def main():
    word = input("Please type you words:")
    print(convert(word))

def convert(a):
    a = a.replace(':)', '🙂')
    a = a.replace(':(', "🙁")
    return a

main()