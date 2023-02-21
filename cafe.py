# This program creates a list and dictionary for a Cafe containing menu and stock items
# then manipulates the data to output the total value of stock

menu = ['cake', 'bread', 'sugar', 'croissant', 'biscuit']     # List containing items
stock = {'cake': 1,
         'bread': 2,                                          # Dictionary with values of items
         'sugar': 3,
         'croissant': 4,
         'biscuit': 5
         }
price = {'cake': 5,
         'bread': 3,                                        # Dictionary containing prices of items
         'sugar': 2,
         'croissant': 4,
         'biscuit': 1
         }

stock_worth = {key: stock[key] * price[key] for key in stock}  # this loop iterates through stock and
print(stock_worth)                                             # multiplies by price

print(sum(stock_worth.values()))            # Finally the total is output using sum method for the values
