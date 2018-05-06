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

#5 Number as Strings Concatenation
#Declare a variable named self_intro that creates the following sentence:
#'Aloha, my name is x and I am y years old and my shoe size is z.' Where x is full_name, y is age and z is shoe_size. Print the self_intro variable.

self_intro = 'Aloha, my name is ' + full_name + ' and I am ' + str(age) + ' years old and my shoe size is ' + str(shoe_size) + '.'
print(self_intro)

#Declare a variable named market_update that creates the following sentence:
#"Today's bitcoin value is x and the yen exchange rate is y." Where x is bitcoin_value and y is yen_rate. Print the market_update variable.

market_update = "Today's bitcoin value is " + str(bitcoin_value) + " and the yen exchange rate is " + str(yen_rate) + "."
print(market_update)

#Declare a variable named about_hawaii that creates the following sentence:
#"Did you know that Hawaii's population is x and the average temperatue is y?" Where x is hawaii_population and y is todays_temperature. Print the about_hawaii variable.

about_hawaii = "Did you know that Hawaii's population is " + str(hawaii_popuation) + " and the average temperature is " + str(todays_temperature) + "?"
print(about_hawaii)

#6 Variables with a List value
#Declare a variable named fab_five and assign it a list containing five of your all time favorite snacks. Print the fab_five variable.

fab_five = ['Oreos', 'carrot cake', 'Pretz', 'peanut butter and chocolate cupcakes', 'pub mix']
print(fab_five)

#Declare a variable named plate_lunch and assign it a list containing five of your favorite lunch items. Print the plate_lunch variable.

plate_lunch = ['chicken katsu', 'kalbi', 'mac salad', 'meat jun','orange chicken']
print(plate_lunch)

#Declare a variable named ice_cream and assign it a list containing three of your favorite ice cream flavors. Print the ice_cream variable.

ice_cream = ['cookies and cream', 'brownie', 'chocolate and peanut butter']
print(ice_cream)

#Declare a variable named west_siiiiide and assign it a list containing states found on the west coast of the US. Print the west_siiiiide variable.

west_siiiiide = ['Washington', 'Oregon', 'California']
print(west_siiiiide)

#Declare a variable named mega_millions and assign it a list containing the Mega Millions Lottery results for May, 4, 2018
#https://www.lotteryusa.com/mega-millions/. Print the mega_millions variable

mega_millions = [4, 5, 10, 12, 18, 21]
print(mega_millions)

#Declare a variable named hamajang and assign it a list containing six different data types. Print the hamajang variable.

hamajang = ['pizza', 100, ['tacos', 'nachos'], {'name': 'Snoopy','breed': 'Beagle'}, ('DevLeague', 'Coding'), True]
print(hamajang)

#Declare a variable named dynamic_duos and assign it a list containing 3 lists, with each list containing items that pairs well with each other. Print the dynamic_duos variable.

dynamic_duos = [['gin', 'tonic'], ['peanut butter', 'celery'], ['bacon', 'cheeseburger']]
print(dynamic_duos)

#7 Accessing values in List
vics_list = ['Hendricks gin', 'Fever Tree tonic', 'Costco pub mix', 'cool ranch doritos', 'oreos', 'Safeway fried chicken', 'Morning Glass coffee']

#Print the entire list.
print(vics_list)
#Print the length of the list.
print(len(vics_list))
#Print only the first element in the list.
print(vics_list[0])
#Print only the last element in the list.
print(vics_list[6])
#Print 'Safeway fried chicken'
print(vics_list[5])
#Replace 'cool ranch doritos' with 'carrot cake' and print the list.
vics_list[3] = 'carrot cake'
print(vics_list)