def main():
    in_coins()

def in_coins():
    due_amount = 50
    while due_amount > 0:
        n = int(input('Put your coin:$25 $10 $5  '))
        if n == 25 or n == 10 or n == 5:
            due_amount -= n
        print(f'Amount Due:{due_amount}')
    print(f"Change Owed:{-due_amount}")



if __name__ == "__main__":
    main()