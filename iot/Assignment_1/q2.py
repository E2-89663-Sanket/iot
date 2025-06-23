num = int(input("Enter a 4-digit number: "))


if num < 1000 or num > 9999:
    print("Please enter a valid 4-digit number.")
else:
    d1 = num // 1000
    d2 = (num // 100) % 10
    d3 = (num // 10) % 10
    d4 = num % 10

    print("a. Face values:", d1, d2, d3, d4)
    print(f"b. Place values: {num} = {d1*1000} + {d2*100} + {d3*10} + {d4}")
    reverse = int(str(num)[::-1])
    print("c. Reversed number:", reverse)
