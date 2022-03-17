from functions import affirm,clear, pause
import random
from replit import db

def Pencounter():
  x = random.randint(1, 6)
  if x == 1:
    x = 'Bulbasaur'
  elif x == 2:
    x = 'Squirtle'
  elif x == 3:
    x = 'Charmander'
  elif x == 4:
    x = 'Ratatta'
  elif x == 5:
    x = 'Pidgey'
  elif x == 6:
    x = 'Sandile'
  Level = random.randint((db['EeveeLv']-1),(db['EeveeLv'] + 1))
  shiny = random.randint(1, 50)
  Health = Level * 2
  Attack = round(Level/2)
  if shiny == 50:
    x = 'Shiny-' + x
    Health = Health * 2
  if db['Perfume'] > 0:
    db['Perfume'] -= 1
    if shiny != 50:
      shiny = random.randint(1, 50)
      if shiny == 50:
        x = 'Shiny-' + x
        Health = Health * 2
      

  print(f'You encountered a Wild Level {Level} {x}! ')
  affirm()
  clear()
  while db['EeveeHP'] > 0 and Health > 0:
    choice = ''
    while choice.strip() != '1' and choice.strip() != '2' and choice.strip() != '3':
      print(f"""
  {db['PokemonName']} HP: {db['EeveeHP']}    
  {x} HP: {Health} 
  
  (1) Covet - Deal damage to opponent
  
  (2) Tail Whip - Decrease opponent's attack power
  
  (3) Growl - Gain attack power

  (4) Use Item - Use Potion To Heal, etc.
            
            """)
      choice = input('')
      clear()
      if choice.strip() == '4':
        print('Type whatever is in the Parenthesis to chose item')
        print('')
        if db['PokeBalls'] > 0:
          print(f"(PokeBalls) - {db['PokeBalls']}")
        if db['GreatBalls'] > 0:
          print(f"(GreatBalls) - {db['GreatBalls']}")
        if db['UltraBalls'] > 0:
          print(f"(UltraBalls) - {db['UltraBalls']}")
        if db['MasterBalls'] > 0:
          print(f"(MasterBalls) - {db['MasterBalls']}")
        if db['Potions'] > 0:
          print(f"(Potion) - {db['Potions']}")
        if db['SuperPotions'] > 0:
          print(f"(SuperPotions) - {db['SuperPotions']}")
        if db['HyperPotions'] > 0:
          print(f"(HyperPotions) - {db['HyperPotions']}")
        if db['MasterPotions'] > 0:
          print(f"(MaxPotions) - {db['MaxPotions']}")
        print('(Back) ')
        y = input('')
        y = (y.strip()).lower()
        if y == 'pokeballs':
          if db['PokeBalls'] > 0:
            db['PokeBalls'] -= 1
            print('You throw a pokeball! ')
            pause(2)
            chance = random.randint (1, 10)
            chance = chance - Health
            if shiny == 50:
              chance - 5
            if chance > -5:
              z = random.randint(1, 20)
              if z > 7:
                print(f"Gotcha! You caught the {x}! ")
                Level = str(Level)
                Entry = x + ',' + Level
                db['EeveeDmg'] = round(db['EeveeLv']/2)
                db['Pokemon'].append(Entry)
                affirm()
                clear()
                return ''
              else:
                print("Oh no! The Pokemon escaped!")
                affirm()
                clear()
            elif chance > -20 and chance < -5:
              z = random.randint(1, 20)
              if z > 18:
                print(f"Gotcha! You caught the {x}! ")
                Level = str(Level)
                Entry = x + ',' + Level
                db['EeveeDmg'] = round(db['EeveeLv']/2)
                db['Pokemon'].append(Entry)
                affirm()
                clear()
                return ''
              else:
                print("Oh no! The Pokemon escaped!")
                affirm()
                clear()
                
              
              
          else: 
            print('You have no Pokeballs. You lose a turn for wasting time trying to use something you do not own :D ')
            affirm()
            clear()

        elif y == 'potions' or y == 'potion':
          if db['Potions'] > 0:
            health = 2* db['EeveeLv']
            regain = health - db['EeveeHP']
            if regain > 10:
              regain = 10
            db['Potions'] -= 1
            print(f"You used a potion! Your Eevee regained {regain} HP! ")
            db['EeveeHP'] += regain
            affirm()
            clear()
      if choice == '1':
     
        print(f"{db['PokemonName']} attacked {x}!")
        pause(1)
        a = db['EeveeDmg'] + random.randint(1, 5)
        print(f"{x} took {a} damage! ")
        Health -= a
        print(f"{x} has {Health} HP left! ")
        affirm()
        clear()
      elif choice == '2':
  
        if Attack > ((1/2) * db['EeveeDmg']):
          print(f"{x}'s Attack power was lowered! ")
          Attack -= round((1/2) * db['EeveeDmg'])
        else:
          print(f"{x} has no attack power left to drain! ")
        affirm()
        clear()
      elif choice == '3':
   
        print(f"{db['PokemonName']}'s attack power increased!")
        affirm()
        clear()
      if Health > 0:
        g = random.randint(1, 2)
        if g == 1:
          
          print(f"{x} used pound! {db['PokemonName']} lost {Attack} HP! ")
          pause(1)
          db['EeveeHP'] -= Attack
          print(f"{db['PokemonName']} has {db['EeveeHP']} HP left. ") 
          affirm()
          clear()
        elif g == 2:
          print (f"{x} increased their attack power! ")
          Attack += random.randint(1, 2)
          affirm()
          clear()
  if db['EeveeHP'] > 0:
    print('You won! ')
    pause(1)
    db['Encounters'] += 1
    if db['EeveeLv'] != db['Encounters']:
      print('Your pokemon gained some experience! ')
      print(f"Defeat {(db['EeveeLv'] - db['Encounters'])} more pokemon to level up! ")
      db['EeveeDmg'] = round(db['EeveeLv']/2)
    else:
      print(f"{db['PokemonName']} leveled up! ")
      pause(2)
      db['EeveeLv'] += 1
      db['EeveeHP'] = db['EeveeLv'] * 2
      db['EeveeDmg'] = round(db['EeveeLv'] /2)
      db['Encounters'] = 0
      print(f"{db['PokemonName']} is now level {db['EeveeLv']}! ")
      affirm()
      clear()
    item = random.randint(1, 50)
    if item > 40:
      print(f"The {x} dropped a Pokeball! You add it to your inventory ")
      db['PokeBalls'] += 1
    elif item < 5:
      print(f"The {x} dropped a Potion! You add it to your inventory ")
      db['Potions'] += 1
    elif item == 15:
      print(f"The {x} disapears in a mist... The Sheening Perfume effect has been applied for 10 turns.... ")
      db['Perfume'] += 10
 
    mon = random.randint(20, 100)
    print(f"You gained {mon}$! ")
    db['Money'] += mon
    affirm()
    clear()
    return ''
  elif db['EeveeHP'] < 1:
    print(f"Your pokemon fainted! Heal your pokemon and try again! You lost {round(db['Money'] / 10)}$")
    x = round(db['Money'] / 10)
    db['Money'] -= x
    db['EeveeDmg'] = round(db['EeveeLv']/2)
    affirm()
    clear()
    return ''

def test():
  pass
  
    
    
    
      
        
    
    
  
  
