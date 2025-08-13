#Countries of the world: try to guess the language spoken in one of the countries
#By:   Silvana Paredes
#Date: 06/08/2025


countries = {
  1: {"name": "Canada", "language": "English"},
  2: {"name": "Russia", "language": "Russian"},
  3: {"name": "China",  "language": "Chinese"},
  4: {"name": "USA",    "language": "English"},
  5: {"name": "Brazil", "language": "Portuguese"},
  6: {"name": "Spain",  "language": "Spanish"}
}


def get_country_number():
  while True:
      user = input("Enter a number from the list \n")
      if user.isdigit():
        number = int(user)
        if number > 0 and number <= 6:
          return number
        else:
          print('Enter a number between 1 and 6')
      else:
        print('Please enter a valid number')


def evaluate_winner(lang, numb):
  return lang.lower() == countries[numb]["language"].lower()
       
       
def game():
  while True:
    #Enter your option
    user_num = get_country_number()

    #Print the name of the country you entered
    print("You selected:", countries[user_num]["name"])

    #Ask the language
    language = input('Enter the language spoken in the country you entered:\n')

    #Evaluate the language
    answ_winner = evaluate_winner(language, user_num)
    if answ_winner:
      print('You won! 🎉 Ganaste')
    else:
      print('Wrong. You entered', language)
    print(f'The correct answer for {countries[user_num]["name"]} is {countries[user_num]["language"]}')
    
    while True:
      answer = input('Do you like to continue? (Y/N)').lower()
      if answer == 'n':
        print('Good bye!')
        return
      elif answer == 'y':
        break
      else:
        print('Please enter Y or N')


#Main
#Print the names of the countries listed in the dictionary
for country_id, country_data in countries.items():
  print(country_id, country_data["name"])
  
game()

  
  
