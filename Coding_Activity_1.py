import requests


'''
OpenWeather API
1. Search for Weather Details of a City: Enter the name of a city and display its current weather details
using the OpenWeather API.
2. Add a City to Favourites: Allow users to add a city to their list of favourites, with a maximum of three
cities.
3. List Favourite Cities: Display the list of favourite cities along with their current weather details.
4. Update Favourite Cities: Enable users to remove a city from their favourites and add a new one,
ensuring the limit of three cities at a time
'''
api_key = "1a849286501d55967955eca71447e9d0"
cities = ['', '' ,'']
i = 0

def get_latLong():
    city = input("Enter a city name: ")
    country = input("Enter the ISO 3166 country code ie GB, US: ")
    coordinate_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&appid={api_key}"


    response = requests.get(coordinate_url)
    data = response.json()

    city_data = data[0]
    latitude = city_data['lat']
    longitude = city_data['lon']
    return latitude, longitude, city_data

def save_favourite_cities(i, city_data):
    question = input("Save City? (y/n) ")
    if question == "y":
        description = city_data['weather'][0]['description']
        name = city_data['name']
        cities[i] =  [name, description]
        return True
    return False


def get_cities(latitude, longitude):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        print(f"Weather: {description} ")

    else:
        print(f"Error: {response.status_code} ")

def get_favourite_cities():
    for city in cities:
        print(city)

def update_favourite_cities():
    global i
    for city in cities:
        print(city)
    list = input("which city to remove?")
    if list == "1":
        i = 1
    elif list == "2":
        i = 2
    elif list == "3":
        i = 3
    latitude, longitude, city_data = get_latLong()
    cities[i] = city_data

if __name__ == '__main__':
    while True:
        if i == 2:
            i = 0

        print("what would you like to do?\n "
              "1. Search for Weather Details of a City: Enter the name of a city and display its current weather details using the OpenWeather API.\n "
              "2. Add a City to Favourites: Allow users to add a city to their list of favourites, with a maximum of three cities.\n"
              "3. List Favourite Cities: Display the list of favourite cities along with their current weather details.\n"
              "4. Update Favourite Cities: Enable users to remove a city from their favourites and add a new one, ensuring the limit of three cities at a time\n")
        todo = input("Enter a number: ")
        if todo == "1":
            latitude, longitude, city_data = get_latLong()
            get_cities(latitude, longitude)
        elif todo == "2":
            latitude, longitude, city_data = get_latLong()
            save_favourite_cities(i, city_data)
        elif todo == "3":
            get_favourite_cities()
        elif todo == "4":
            update_favourite_cities()


