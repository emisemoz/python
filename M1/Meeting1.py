# #this is comment
# """
# this is multiline comment
# """

# movie_title="Captain Marvel"
# release_year= 2019
# rating= 7.9
# is_general_audiences= False
# print("The Movie is " + movie_title)

# top_up_amount = 50 #great top up value
# count = 3 #how many times to top up
# discount = 2 #big discount
# #get total payment
# total_payment = top_up_amount * count
# print(total_payment)
# #total payment after discount
# total_discount = discount * 3
# payment_after_discount = total_payment - total_discount
# print("total payment : " + str(total_payment))
# print("total payment after discount : " +str(payment_after_discount))

# print("""Burger Pricelist : 
#     1. Beef Burgerr $15
#     2. Cheese Burger $20
#     3. Kids Burger $9 """)
# menu_price=input("Menu price :") #menu price value based on input
# amount=input("Amount :")
# bill= int(menu_price)* int(amount) #From string is changed into integer
# print("You need to pay $" +str(bill)) 

first_name=input("Your first name:")
last_name=input("Your last name :")
class_code=input("Your class code :")
print("Your information :")
print(first_name+last_name+class_code)