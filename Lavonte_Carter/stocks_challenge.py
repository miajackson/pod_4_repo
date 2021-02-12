print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
print()

name = str(input ("What is your name? "))
print(f"Welcome {name}!")
print()

# TODO: Write code to ask the client his savings and save it to another variable.
savings = int(input("What is the amount of your savings account? "))
print(f"You curently have ${savings} dollars to spend.")
user_savings = savings
print()

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.


stock = str(input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft. "))
print()

user_stock = stock

print(f"You chose {user_stock}.")

print()


print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

if user_stock == "amzn":
    print(f"{name} has ${savings} to buy {int(user_savings/amazon)} shares of Amazon at the current price of ${amazon}.")

elif user_stock == "aapl":
    print(f"{name} has ${savings} to buy {int(user_savings/apple)} shares of Apple at the current price of ${apple}.")

elif user_stock == "fb":
    print(f"{name} has ${savings} to buy {int(user_savings/fb)} shares of Facebook at the current price of ${fb}.")

elif user_stock == "goog":
    print(f"{name} has ${savings} to buy {int(user_savings/google)} shares of Google at the current price of ${google}.")

elif user_stock == "msft":
    print(f"{name} has ${savings} to buy {int(user_savings/msft)} shares of Microsoft at the current price of ${msft}.")

else:
    print(f"***Input invalid, please restart the program and select from the list of companies!***")
print()
print("Challenge 3.2.3: Output for the user the result")
# TODO: COnce you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

