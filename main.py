stock = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 190,
    "NVDA": 500,
    "META": 470
}
total_investment = 0
while True:

    user_stock = input("Enter a stock name or Done for end: ").upper()
    if user_stock in stock:
        price = stock[user_stock]
        quantity = int(input("Enter quantity: "))
        total_investment += quantity*price
        print(f"Total investment: {total_investment}")
    elif user_stock == "DONE":
        print("Done")
        print(f"Total investment: {total_investment}")
        break
    else:
        print("Stock not found!")
