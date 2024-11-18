products = [("Бананы", 120), ("Мясо", 300), ("Яблоки", 80), ("Сыр", 200), ("Молоко", 50)]
expensive_products = list(filter(lambda x: x[1] > 100, products))
product_names = list(map(lambda x: x[0], expensive_products))
print(product_names)