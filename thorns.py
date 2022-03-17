from functions import affirm, clear, pause
from replit import db
import random
def ThornPalace():
  clear()
  print(f"You walk up to Thorn Palace, your {db['PokemonName']} by your side. ")
  pause(1.5)
  print('There is a massive grand door in front of you, covered in vines and thorns. ')
  pause(1.5)
  print(f"Your {db['PokemonName']} sniffs at the door and doesn't seem to sense anything awry" )
  pause(1.5)
  print('To enter the palace, you must answer a riddle....')
  pause(1.5)
  affirm()
  clear()
  guess = ''
  while (guess.strip()).lower() != "plant" and  (guess.strip()).lower() != "plants" and (guess.strip()).lower() != "flower" and (guess.strip()).lower() != "flowers":
    print("You bury me when i'm alive, and dig me up when I die. What am I?  ")
    guess = input()
    clear()
  print('You are granted access into Thorn Palace. ')
  affirm()
  clear()
  print('The thorns unravel from the door and the gates swing open. ')
  pause(2)
  print('You are greeted by a group of Snivy. They say you must prove your Pokemon Knowledge before you can advance. ')
  affirm()
  answer = ''
  while (answer.strip()).lower() != 'leafeon':
    print('What is the grass type evolution of Eevee?')
    answer = input()
    clear()
  print(f"The Snivys are satisfied and make way for you and {db['PokemonName']}")
  pause(2)
  print('A Lv 15 Serperior pops out and challenges you! Its an ambush! ')
  affirm()
  clear()
  SerperiorHP = 30
  SerperiorAttack = 7
  z = ''
  while SerperiorHP > 0 and db['EeveeHP'] > 0:
    while z != '1' and z != '2' and z != '3':
      print(f"""
Eevee HP: {db['EeveeHP']}

Serperior HP: {SerperiorHP}

(1) Attack Serperior

(2) Defend

(3) Run Away
        
""")
      z = input('')
    if z == '1':
      clear()
      z = ''
      print(f"{db['PokemonName']} attacked the Serperior!")
      x = random.randint(1, 6)
      damage = db['EeveeDmg'] + x
      if x > 4:
        print('CRITICAL HIT!')
      print(f"The attack did {damage} points of damage to Opponent Serperior! ")
      SerperiorHP -= damage
      print(f"Opponent Serperior has {SerperiorHP} HP left ")
      affirm()
      clear()
    elif z == '2':
      clear()
      z = ''
      if SerperiorAttack > 1:
        print('Foe Serperior now does 2 less damage! ')
        SerperiorAttack -= 2
      else: print('Serperior has no attack power left to drain ')
      affirm()
      clear()
    elif z == '3':
      clear()
      z = ''
      print('You ran out of the palace, but surely you will be back later. ')
      affirm()
      clear()
      return ''
    c = random.randint(1, 4)
    if SerperiorAttack < 1:
      c = 2
    if c == 1 or c == 2 or c == 3:
      print(f"Foe Serperior attacks! Foe Serperior did {SerperiorAttack} damage! ")
      db['EeveeHP'] -= SerperiorAttack
      print(f"{db['PokemonName']} has {db['EeveeHP']} HP left ")
      affirm()
      clear()
    elif c == 4:
      print(f"Foe Serperior uses Growth! Serperior's attack power increased by 1 point!")
      SerperiorAttack += 1
      affirm()
      clear()
      
  if SerperiorHP < 1:
    print("You defeated Serperior! ")
    affirm()
    clear()
  elif db['EeveeHP'] < 1:
    print(f"Serperior defeated you! Heal up your {db['PokemonName']} and try again! ")
    affirm()
    clear()
    return ''
  print(f"All the pokemon surrounding you shrink away from you, scared after that display of {db['PokemonName']}'s power. '")
  pause(2)
  print("However, one timid Treeko crawls to you and heals your Eevee for you.")
  db['EeveeHP'] = db['EeveeLv'] * 2
  affirm()
  clear()
  print("More content coming soon! Check back later! ")
  affirm()
  clear()
    

  
def In_Progress():
  pass
  
  
    
  
  
  
        
  