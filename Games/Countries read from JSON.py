#Countries read from a public JSON file
#With this list, the program asks the user to write the first letter and the
#program displays the matching countries.
#By:   Silvana Paredes
#Date: 07/08/2025

import requests

url = 'https://restcountries.com/v2/all?fields=name,capital'
response = requests.get(url)

if response.status_code == 200:
    countries = response.json()
    
    band = False

    while not band:

      initial = input('Enter the first letter of the countries you want to list:\n')[0]

      if len(initial) > 1:
          initial = initial[0]

      matched = [country for country in countries if country.get('name', '').lower().startswith(initial.lower())]

      if matched:
         for country in matched:
             print(country.get('name', 'No name'), "-", country.get('capital', 'No capital'))
      else:
         print(f"No countries found starting with '{initial}'")

      while True:
        answer = input('Do you like to continue? (Y/N)').lower()
        if answer == 'n':
            print('Good bye!')
            band = True
            break
        elif answer == 'y':
            break
        else:
            print('Please enter Y or N')
else:
    print(f'Error: {response.status_code}')
