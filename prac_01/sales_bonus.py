"""
CP1404 2020 - Practical 1
Student Name: Amy Robinson
Program - Sales Bonus

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# sales = float(input("Enter sales: $"))
#
# if sales < 1000:
#     bonus = 0.10  # 10% as decimal
# else:
#     bonus = 0.15  # 15% as decimal
#
# sales_bonus = bonus * sales
# print("{:.0f}".format(sales_bonus))


sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = 0.10  # 10% as decimal
    else:
        bonus = 0.15  # 15% as decimal

    sales_bonus = bonus * sales
    print("{:.0f}".format(sales_bonus))
    sales = float(input("Enter sales: $"))
