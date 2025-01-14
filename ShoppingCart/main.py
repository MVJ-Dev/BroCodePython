#shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (press 'z' to quit): ")
    if food.lower() == 'z':
        break
    else:
        price = float(input(f"Enter the price: {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----------YOUR SHOPPING CART-------------")

for food in foods:
    print(food)
    
for price in prices:
    total += price

print(f"Your total is: $    {total}")
