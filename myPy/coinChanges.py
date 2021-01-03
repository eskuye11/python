def change_coin():
    """ cashier change helper, this func tells you how many
        # quarter, dimes, nickle and pennies to give back """

    amount = int(input('Enter Your Change : '))
    out = input("Coin is Out (Optional) : ")  # if you are out of quarter, dime or nickles . . .
    out = 0 if out == '' else out  # if out is blank, default value is 0
    coins = {25: 'Quarter', 10: 'Dime', 5: 'Nickle', 1: 'Pennie'}
    outCoin = coins.pop(int(out), None)
    counts = [0] * len(coins)
    remainder = amount

    for index, coin in enumerate(coins):
        counts[index], remainder = divmod(remainder, coin)

    withC = f'without ({outCoin}s)'   # if out of Coin is blank or '0'
    print(f"{amount / 100} Cents", format(withC, '') if outCoin else '', 'will be : ')

    for count, name in zip(counts, coins.values()):
        if count != 0:
            name = name if count == 1 else name + 's'  # control (singular, plural)
            print(f"  {count}  {name}")


if __name__ == '__main__':
    while True:
        print()
        change_coin()