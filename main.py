# Dictionary of available stocks and their prices
stock = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 190,
    "NVDA": 500,
    "META": 470
}

# Variable to store total investment value
total_investment = 0

# Function to calculate investment for a given stock
def current_investment(current_quantity, stock_price):
    return current_quantity * stock_price


while True:

    # Ask user to enter stock name or exit command
    user_stock = input("Enter a stock name or Done for end: ").upper()

    # If stock exists in dictionary
    if user_stock in stock:
        price = stock[user_stock]

        # ---------------------------------------
        # INPUT VALIDATION FOR QUANTITY
        # ---------------------------------------
        while True:
            try:
                # Try converting input into integer quantity
                quantity = int(input("Enter quantity: "))

                # Ensure quantity is positive
                if quantity <= 0:
                    print("Quantity must be greater than 0!")
                    continue

                # Valid input, exit loop
                break

            except ValueError:
                # Handles invalid input (text, float, symbols)
                print("Invalid input! Please enter a whole number (integer).")

        # Add investment to total
        total_investment += current_investment(quantity, price)

        # Show updated total
        print(f"Total investment: {total_investment}")

    # Exit condition
    elif user_stock == "DONE":
        print("Done")
        print(f"Total investment: {total_investment}")
        break

    # If stock is not found
    else:
        print("Stock not found!")

# Save result to a file
with open("total_investment.txt", mode="w") as f:
    f.write(f"Total investment: {total_investment}")
