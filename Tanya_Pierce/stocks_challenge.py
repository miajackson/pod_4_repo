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
# TODO: Write code to ask the client his savings and save it to another variable.
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.

name = input("Good morning, provide us your name by typing it the field below then pressing [enter] :")
savings = int(input("How much is in your savings account? Please enter the amount in the field below (excluding dollar sign '$' and commas ',') and press [enter] :"))
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft then press [enter] :")
print()

# checking user info, print function with input variables

if stock == "amzn":
    print(f"Thank you {name}, you currently have ${savings} in savings and are looking into purchasing stocks with Amazon")
elif stock == "aapl":
    print(f"Thank you {name}, you currently have ${savings} in savings and are looking into purchasing stocks with Apple")
elif stock == "fb":
    print(f"Thank you {name}, you currently have ${savings} in savings and are looking into purchasing stocks with Facebook")
elif stock == "goog":
    print(f"Thank you {name}, you currently have ${savings} in savings and are looking into purchasing stocks with Google")
elif stock == "msft":
    print(f"Thank you {name}, you currently have ${savings} in savings and are looking into purchasing stocks with Microsoft")

else:
    print("You didn't enter a valid stock option")




