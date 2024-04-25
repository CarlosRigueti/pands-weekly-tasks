# Collatz program
# Autor: Carlos Rigueti

while True:
    try:
        num = int(input("Input an integer value number (or digite 0 to exit): "))
        if num == 0:
            print(" Program closed.")
            break
        elif num < 0:
            print("Please, input an integir valid number.")
        else:
            print('"The successive calculation value for '"num,"' are:"')
            while num != 1:
                print(num, end=" ")
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
            print(1)  
    except ValueError:
        print("Please, insert an integer valid number.")


