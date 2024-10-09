# This is a list of restaurant dictionaries
restaurants = [
    {"name": "Pasta Palace", "cuisine_type": "Italian"},
    {"name": "Burger Barn", "cuisine_type": "American"},
    {"name": "Taco Tower", "cuisine_type": "Mexican"},
    {"name": "Sushi Stop", "cuisine_type": "Japanese"},
    {"name": "Pizza Plaza", "cuisine_type": "Italian"}
]

# Print restaurant data
for restaurant in restaurants:
    print(f"Restaurant: {restaurant['name']}, Cuisine Type: {restaurant['cuisine_type']}")
