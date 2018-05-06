#Comments are text that will not be executed in your code. Rather comments are for other programmers to read. 

# All of the exercises below are commented out. Write your Javascript code after each exercise.

#Variables and Data Types 
#Print each variable and test your code in the terminal using the Python interpreter

#example
greeting = 'Hello Prepster';
print(greeting); #this should print 'Hello Prepster'

#1 Variables with a String value
#Declare variables named first_name, last_name, birth_place, hobby, role_model, famous_quote, fav_president, fav_food, fav_color, fav_song

#Assign your own string values to each variable and print each variable.

first_name = 'Charlie'
print(first_name)
last_name = 'Brown'
print(last_name)
birth_place = 'Minnesota'
print(birth_place)
hobby = 'football'
print(hobby)
role_model = 'Snoopy'
print(role_model)
famous_quote = 'Good grief!'
print(famous_quote)
fav_president = 'Obama'
print(fav_president)
fav_food = 'carrot cake'
print(fav_food)
fav_color = 'yellow'
print(fav_color)
fav_song = "Don't Stop Believin"
print(fav_song)

#2 String Concatenation
#Declare a variable named full_name and concatenate first_name and last_name. Print the full_name variable.

full_name = first_name + " " + last_name
print(full_name)

#Declare a variable named intro that creates the following sentence:
#'Hello, my name is x and I was born in y.' Where x is full_name and y is birth_place. Print the intro variable.

intro = 'Hello, my name is '+ full_name + ' and I was born in ' + birth_place + '.'
print(intro)

#Declare a variable named about_me that creates the following sentence:
#'My hobby is x, my favorite song is y, and I like to eat z.' Where x is hobby, y is fav_song and z is fav_food. Print the about_me variable.

about_me = 'My hobby is ' + hobby + ', my favorite song is ' + fav_song + ', and I like to eat ' + fav_food + '.'
print(about_me)

#3 Spacing with tabs and newlines
#Declare a variable named my_hero that the following sentence using a tab:
#'My hero is x and his famous quote is y.' Where x is role_model and y is famous_quote. Print the my_hero variable.

my_hero = '\tMy hero is ' + role_model + ' and his famous quote is ' + famous_quote + '.'
print(my_hero)

#Declare a variable named my_favs that creates the following sentence and returns a new line after each numbered item. 
#'This is what I like: 1. hobby 2. fav_color 3. fav_song
#Print the my_favs variable.

my_favs = 'This is what I like: \n1. ' + hobby + '\n2. ' + fav_color + '\n3. ' + fav_song
print(my_favs)

#4 Variables with a Number value
#Declare variables named age, weight, shoe_size, fav_number, yen_rate, bitcoin_value, todays_temperature, hawaii_popuation, countries_traveled, number_of_siblings

#Assign your own number values to each variable and print each variable.

age = 68
print(age)
weight = 168
print(weight)
shoe_size = 11
print(shoe_size)
fav_number = 3
print(fav_number)
yen_rate = 110
print(yen_rate)
bitcoin_value = 10000
print(bitcoin_value)
todays_temperature = 78.1
print(todays_temperature)
hawaii_popuation = 1200000
print(hawaii_popuation)
countries_traveled = 25
print(countries_traveled)
number_of_siblings = 2
print(number_of_siblings)


