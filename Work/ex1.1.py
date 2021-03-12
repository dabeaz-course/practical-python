# Lucky Larry bought 75 shares of Google stock at a price of $235.14 per share. Today, shares of Google are priced at $711.25. Using Python’s interactive mode as a calculator, figure out how much profit Larry would make if he sold all of his shares.

shares = 75
boughtPrice = 235.14
todayPrice = 711.25
profit = (todayPrice * shares) - (boughtPrice * shares)
if (profit > 0):
    print(f'If you sold today you would realize a gain of ${profit}')

if (profit == 0):
    print("Well, at least you didn't lose any money")

if (profit < 0):
    print(f'You lost ${abs(profit)} ')
