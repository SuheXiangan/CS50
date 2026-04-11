def main():
    num1, sym, num2 = input('Expression:').split()
    if sym == "+":
        a = float(num1)+float(num2)
        print(f"{a:.1f}")
    elif sym == "-":
        a = float(num1)-float(num2)
        print(f"{a:.1f}")
    elif sym == "*":
        a = float(num1)*float(num2)
        print(f"{a:.1f}")
    else:
        a = float(num1)/float(num2)
        print(f"{a:.1f}")

main()