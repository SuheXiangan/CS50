def main():
    ans = input('Please enter you answer:').lower()
    match ans:
        case '42' | 'forty-two' | 'forty two':
            print('Yes')
        case _:
            print('No')
    
main()