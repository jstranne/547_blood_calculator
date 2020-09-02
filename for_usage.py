foods = ["apples", "bananas", "cherries", "donuts", "eggplant"]

amounts = [11, 22, 33, 44, 55]


def num_fruit(fruit_name):
    for amount, food in zip(amounts, foods):
        if(food == fruit_name):
            return amount
    return 0


print("Number of bananas is", num_fruit("bananas"))
print("the number of cherries is", num_fruit("cherries"))
print("number of oranges is", num_fruit("oranges"))
