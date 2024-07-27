while True:
    try:
        n = int(input("Enter the number to print the table: "))
    except ValueError:
        print("Enter a number/integer value")
    else:
        for i in range(1,13):
            print(f"{n} X {i} = {n * i}")
    break