print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print("Challenge 2.2:")
print("Print the variables that track the number of 3 pt shots made by each of the three players")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_attempts = 93
fred_vanvleet_3pts_attempts = 110
james_harden_3pts_attempts = 109
print()

print("Challenge 2.4: Build on your print statement")
print(f"In the 2020 NBA playoffs, Jamal Murray attempts {jamal_murray_3pts_attempts} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet attempts {fred_vanvleet_3pts_attempts} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden attempts {james_harden_3pts_attempts} 3 point shots")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
percentage_jamal = jamal_murray_3pts_made/jamal_murray_3pts_attempts  
percentage_fred = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts
percentage_james= james_harden_3pts_made/james_harden_3pts_attempts
print(f"{percentage_jamal} -Jamal points made and attempts percentage")
print(f"{percentage_fred} -Fred points made and attempts percentage")
print(f"{percentage_james} -James points made and attempts percentage")

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
big_paragraph = 'The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\nThe Lakers ended the season atop the Western Conference with a record of 49-14.\nThey were narrowly behind the Bucks for the best record in the league.\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.'

print("The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis.\nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis.\nThose three have made good developments with the Pelicans, especially Brandon Ingram.\nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season.\nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA.\nThe Lakers ended the season atop the Western Conference with a record of 49-14.\nThey were narrowly behind the Bucks for the best record in the league.\nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year.\nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season.") 

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, orint out the paragraph with only 1 sentence per line, and all in upper case
print (big_paragraph.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
Lakers_are_the_best = True
print(type(Lakers_are_the_best))
# TODO: print out the variable in an f-string to convey your opinion on the lakers
print(f"{Lakers_are_the_best} -The Lakers are the best basketball team in the NBA I guess, I don't watch sports too much")

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
x = int(Lakers_are_the_best) 
print(x)
# TODO: Convert your `lakers_are best` variable to a float, and print it out
y = float(Lakers_are_the_best) 
print(y)

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.

# percentage_jamal = jamal_murray_3pts_made/jamal_murray_3pts_attempts  
# percentage_fred = fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts
# percentage_james= james_harden_3pts_made/james_harden_3pts_attempts

a = str(jamal_murray_3pts_made/jamal_murray_3pts_attempts)
print(a)
b = str(fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts)
print(b)
c = str(james_harden_3pts_made/james_harden_3pts_attempts)
print(c)
a = 1
print(type(a))

# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
d = int(jamal_murray_3pts_made/jamal_murray_3pts_attempts)
print(d)
e = int(fred_vanvleet_3pts_made/fred_vanvleet_3pts_attempts)
print(e)
f = int(james_harden_3pts_made/james_harden_3pts_attempts)
print(f)
d = 2
print(type(d))