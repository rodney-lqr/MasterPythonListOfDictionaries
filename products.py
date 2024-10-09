# List of product dictionaries
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 700},
    {"name": "Headphones", "price": 150},
    {"name": "Monitor", "price": 300},
    {"name": "Keyboard", "price": 50}
]

# Print product data
for product in products:
    print(f"Product: {product['name']}, Price: ${product['price']}")

print()
print()
print()

# Add another product
new_product = {"name": "Tablet", "price": 400}
products.append(new_product)
# Print updated product list
print("After adding a new product:")
for product in products:
    print(f"Product: {product['name']}, Price: ${product['price']}")

print()
print()
print()

# Change the price of 'Monitor' to 320
for product in products:
    if product['name'] == 'Monitor':
        product['price'] = 320
# Print updated product list
print("\nAfter changing the price of Monitor:")
for product in products:
    print(f"Product: {product['name']}, Price: ${product['price']}")

print()
print()
print()
# Add model to each product
for product in products:
    product['model'] = f"Model-{product['name']}"
# Print updated product list with models
print("\nAfter adding model to each product:")
for product in products:
    print(f"Product: {product['name']}, Price: ${product['price']}, Model: {product['model']}")

