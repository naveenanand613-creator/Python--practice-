sales = {
    "Laptop": {"units": 5, "price": 50000},
    "Headphones": {"units": 20, "price": 1500},
    "Keyboard": {"units": 15, "price": 1000},
    "Mouse": {"units": 25, "price": 500}
}
total_revenue = 0
print("SALES DATA ANALYZER")
print("-------------------")
for product, data in sales.items():
    revenue = data["units"] * data["price"]
    total_revenue += revenue
    print(product)
    print("Units Sold:", data["units"])
    print("Revenue:", revenue)
best_seller = max(sales, key=lambda p: sales[p]["units"])
print("-------------------")
print("Total Revenue:", total_revenue)
print("Best-Selling Product:", best_seller)
print("Units Sold:", sales[best_seller]["units"])
