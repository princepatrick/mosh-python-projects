from converter import lbs_to_kgs
from findLargestNumber import find_largest_number
from ecommerce.shipping import calc_shipping_costs
from railwayregistrationsystem import RailwayRegistrationUtil
from shoppingcomplex import ShoppingComplexUtil
from carrepairshop.CarRepairShopUtil import calculate_repair_costs
from theater.TheaterUtil import book_tickets
from pathlib import Path

# Retrieving from converter module to calculate pounds to kilograms conversion
print(lbs_to_kgs(170))

# Retrieving from findLargestNumber module to find the maximum number in the list
numbers = [10, 20, 30, 5, 35, 25]
print(find_largest_number(numbers))

# Retrieving the calculate-shipping costs method from the shipping module in the ecommerce package
print(calc_shipping_costs())

# Retrieving the find user and remove user methods from RailwayRegistrationUtil module in the railwayregistrationsystem package
RailwayRegistrationUtil.find_user("Prince Patrick Anand")
RailwayRegistrationUtil.remove_user("Prince Patrick Anand")

# Retrieving the find shop id and get the floor map methods from ShoppingComplexUtil module in the shoppingcomplex package
ShoppingComplexUtil.get_mall_map(2)
ShoppingComplexUtil.get_shop_details(2097)

# Retrieving the calculate-repair costs method from CarRepairShopUtil module in the carrepairshop package
calculate_repair_costs(31)

# Retrieving book tickets method from Theater Util module
book_tickets(4, "03:00", "Kuselan")

# importing Path module from in-built path package
path = Path("main.py")
print(f"does the file exist? {path.exists()}")



