stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}
total_investment = 0
n = int(input("Enter number of stocks: "))
for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] *quantity
        total_investment +=investment
    else:
        print(f"{stock_name} not found in portfolio.")
print("\nTotal Investment Value = $",total_investment)
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total_investment}")
print("Result saved in portfolio.txt")
