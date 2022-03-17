from functions import affirm, clear, pause
from replit import db
from move import Pokemon
import thorns
import pokedex
import colorama
from colorama import *

def Game():
  
  while 1 == 1:
    if db['Level'] == 0:
      Place = 'Thorn Palace'
    input1 = ''
    while input1.strip() != '1' and input1.strip() != '2' and input1.strip() != '3' and input1.strip() != '4' and input1.strip() != '5' and input1.strip() != '6' and input1.strip() != '7':
      x = (f'''
Level {db['EeveeLv']} {db['PokemonName']}

{db['PokemonName']}'s HP: {db['EeveeHP']}

Money: {db['Money']}$

Options:

(1) Look for Pokemon 
(2) Explore {Place}
(3) Open Inventory  
(4) Tutorial   
(5) Heal {db['PokemonName']}
(6) PokeStore (Buy Items)
(7) View Pokemon
(8) Open Pokedex (See all Pokemon in the Game)
''')
      print(x)
      input1 = input().strip()
      clear()
      if input1 == '1':
        input1 = ''
        if db['EeveeHP'] > 0:
          Pokemon()
          clear()
        else:
          print(f"Heal up your {db['PokemonName']} before exploring! ")
          affirm()
          clear()
      elif input1 == '2':
        if db['EeveeHP'] > 0:
          thorns.ThornPalace()
        else:
          print(f"Heal up your {db['PokemonName']} before exploring! ")
          affirm()
          clear()
      elif input1 == '3':
        print(f"You have {db['PokeBalls']} Pokeballs, {db['GreatBalls']} Great Balls, {db['UltraBalls']} Ultra Balls, {db['MasterBalls']} Master Balls, {db['Potions']} Potions, {db['SuperPotions']} Super Potions, {db['HyperPotions']} Hyper Potions, and {db['MasterPotions']} Max Potions.  ")
        affirm()
        clear()
      elif input1 == '4':
        print('Look for Pokemon to fight them, and earn money, xp to level up your pokemon, and items! For each ultimate, you will have an area to explore which will involve riddles, rooms, and pokemon fights. At the end of each explore, you will reach an Ultimate Pokemon which you must fight. If you die, you will have to go through the whole explore process again. After you finish exploring an area and beat the ultimate, you will be able to explore a new area! Your data will be saved AFTER you finish exploring an area, so do not quit in between exploring an area or reload the project. Have fun!  ')
        affirm()
        clear()
      elif input1 == '5':
        if db['EeveeHP'] < (db['EeveeLv'] * 2):
          print(f"Your {db['PokemonName']} was healed to full health! ")
          db['EeveeHP'] = db['EeveeLv'] * 2
          affirm()
          clear()
        else:
          print(f"Your {db['PokemonName']} is already at full health!")
          affirm()
          clear()
      elif input1 == '6':
        print("Welcome to the Pokestore! ")
        print('')
        print("Here is our current stock: ")
        print('Potions - 50$ (Restores up to 10 HP!)')
        print('Pokeballs - 200$ (You get 10 per purchase) ')
        print('Sheening Perfume - 5000$ (Doubles chance of finding Shiny Pokemon for 50 encounters! [Stackable, and and effect applied on purchase])')
        
        print('')
        print(f"You have {db['Money']}$!")

        print("(1) Buy Potion (50$)")
        print("(2) Buy 10 Pokeballs (200$)")
        print("(3) Buy Sheening Perfume (5000$)")
        print("(4) Back")
        x = input('')
        x = x.strip()
        if x == '1':
          if db['Money'] > 50:
            print('You bought a Potion! It has been added to your inventory ')
            db['Money'] -= 50
            db['Potions'] += 1
            affirm()
            clear()
          else:
            print('Oh noes! Not enough money! ')
            affirm()
            clear()
        if x == '2':
          if db['Money'] > 200:
            print('You bought 10 Pokeballs! They have been added to your inventory ')
            db['Money'] -= 200
            db['PokeBalls'] += 10
            affirm()
            clear()
          else:
            print('Not enough money')
            affirm()
            clear()
        if x == '3':
          if db['Money'] > 5000:
            print("You bought a Sheening Perfume! The effect has been applied! ")
            db['Money'] -= 5000
            db['Perfume'] += 50
          else:
            print('Not enough money')
            affirm()
            clear()
        else:
          clear()
      elif  input1 == '7':
        print('Pokemon: ')
        print('')
        print(f"Level {db['EeveeLv']} {db['PokemonName']}")
        for i in db['Pokemon']:
          z = i.split(',')
          print(f"Level {z[1]} {z[0]}")
        print('')
        affirm()
        clear()
      elif input1 == '8':
        pokedex.pokeOPEN()
        
        
      
        
if 'Loaded' in db.keys():
  print('''You have saved progress, would you like to keep it or delete it? Type "Yes" to clear all progress, and if not, press [Enter]''')
  x = input()  
  if (x.strip()).lower() == 'yes':
    db.clear()
if not 'Roar' in db.keys():
  db['Roar'] = True
  db['Perfume'] = 0
  db['Pokemon2'] = []
  db['Pokemon3'] = []
  db['Pokemon4'] = []
  db['Pokemon5'] = []
if not 'New' in db.keys():
  db['New'] = True
  db['Pokemon'] = []
  
clear()
if not 'Loaded' in db.keys():
  db['Loaded'] = 0
  db['EeveeLv'] = 5
  db['EeveeHP'] = 10
  db['EeveeDmg'] = 2
  db['Money'] = 100
  db['Level'] = 0
  db['PokeBalls'] = 10
  db['GreatBalls'] = 0
  db['UltraBalls'] = 0
  db['MasterBalls'] = 0
  db['PokemonEvolution'] = 0
  db['Potions'] = 0
  db['SuperPotions'] = 0
  db['HyperPotions'] = 0
  db['MasterPotions'] = 0
  db['Encounters'] = 0
  db['Items'] = []
  db['PokemonName'] = 'Eevee'
  print('Welcome to my game, Pokemon Ultimates! There are 19 ultimate pokemon that have taken over the world, and it is your goal to stop them! You are given an Eevee to train and fight alongside to take down the ultimate! Good Luck! This game automatically saves your progress, so you can come back to it anytime! To see how to play the game, just use the tutorial option! ')
  print('')
  print(f"This program was created by Your mother, {Fore.BLUE} Jordan, {Style.BRIGHT + Fore.LIGHTYELLOW_EX} The, {Fore.RESET} and {Style.DIM + Fore.BLUE} Owner! ")
  print(Fore.RESET + Style.RESET_ALL + Back.RESET)
  print(f'Additional Mentions go to: {Fore.RED}H{Fore.LIGHTYELLOW_EX}e{Style.DIM + Fore.LIGHTGREEN_EX}nri{Style.BRIGHT + Fore.CYAN}n{Style.DIM + Fore.BLUE}er{Fore.RESET + Style.RESET_ALL}, and {Fore.LIGHTBLUE_EX} Whoever made python!{Fore.RESET}')
  affirm()
  clear()
  Game()
else:
  print(f"This program was created by SuryaRavi1, {Fore.BLUE}IMeanBusiness, {Style.BRIGHT + Fore.LIGHTYELLOW_EX}DotAccount,{Fore.RESET} and {Style.DIM + Fore.BLUE}ColinKirsch! ")
  print(Fore.RESET + Style.RESET_ALL + Back.RESET)
  print(f'Additional Mentions go to: {Fore.RED}C{Fore.LIGHTYELLOW_EX}o{Style.DIM + Fore.LIGHTGREEN_EX}lor{Style.BRIGHT + Fore.CYAN}ed{Style.DIM + Fore.BLUE}Hue{Fore.RESET + Style.RESET_ALL}, and {Fore.LIGHTBLUE_EX}HyperAlternative!{Fore.RESET}')
  affirm()
  db['Money'] = round(db['Money'])
  clear()
  Game()



