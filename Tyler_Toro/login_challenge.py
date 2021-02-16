# Feel free to update the values in the user dictionary
user = {
    "name": "Tyler Toro",
    "email": "t_toro@JTC.com",
    "password": "abcd1234"
}
print(user)
# Here is a while loop that runs as long as the email is incorrect
# When the correct email is entered, we exit the while loop and move to the next input for password
email = input("Email: ")

# Checks the value of email in line 10
while(email != user["email"]):
    # This code runs as long as the emails do not match
    print("This email does not exist in our system. Please try again.")
    # Ask to input email again and update value of email in line 10
    email = input("Email: ")

# Seeing 'Password: ' in command line means we have exited the while loop
password = input("Password: ")

# TODO: Write a while loop that checks whether the password is incorrect.
while(password != user["password"]):
    print("Something went wrong, please try entering your password again")
    password = input("Password: ")
# TODO: Print 'Logging In...'
print("Logging in...") 
# TODO: Print 'Welcome back, ' and the name in the user dictionary
print(f"Welcome back " + user["name"] )
