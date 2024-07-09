from collections import Counter

prices = {'soap': 50, 'toothpast': 25, 'shampoo': 5}


def generate_bill(cart):
    total = 0
    for item,qty in cart.items():
        print(item , prices[item], 'X', qty, '=', prices[item]*qty)
        total += prices[item]*qty
    print('Total :', total)

cart = Counter(soap = 5 , toothpast = 2 , shampoo =10)
generate_bill(cart)



