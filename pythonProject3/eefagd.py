products = [("Хлеб", 50), ("Молоко", 80), ("Сыр", 150), ("Яблоки", 70)]
sorted_products = sorted(products, key=lambda x: x[1], reverse=True)
print(sorted_products)