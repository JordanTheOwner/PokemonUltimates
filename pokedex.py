
from replit import clear
from colorama import *
from getkey import getkey, keys
pokeDex = False
pokemon = {
"Ratatta":{'Name':Fore.RESET + "Ratatta [Normal Type]", "Desc":"Will chew on anything with its fangs. If you see one, you can be certain that 40 more live in the area."},
"Bulbasaur": {"Name":Style.BRIGHT + Fore.GREEN + "Bulbasaur [Grass & Poison type]","Desc":"There is a plant seed on its back right from the day this Pokémon is born. The seed slowly grows larger."},
"Squirtle":{"Name":Style.RESET_ALL + Fore.BLUE + "Squirtle [Water type]","Desc":"When it retracts its long neck into its shell, it shoots out water with strong force."},
"Charmander":{"Name":Style.BRIGHT + Fore.RED + "Charmander [Fire type]","Desc":"It has a liking for hot things. When it rains, steam is said to appear from the tip of its tail."},
"Pidgey": {"Name":Style.RESET_ALL + Fore.RESET + "Pidgey [Normal & Flying type]","Desc":"Very submissive. If attacked, it will often kick sand to protect itself instead of fight back."},
"Sandile":{"Name":Style.BRIGHT + Fore.LIGHTBLACK_EX + "Sandile [Ground & Dark type]","Desc":"The desert gets cold at night, so when the sun sets, this Pokémon burrows far into the sand and sleeps until sunrise."},
"Eevee":{"Name":Style.RESET_ALL + Fore.RESET + "Eevee [Normal type]","Desc":"It has the ability to change the composition of its body to fit its needs in its surrounding environment."} 
}
order = {
	1:"Bulbasaur",
	2:"Charmander",
	3:"Squirtle",
	4:"Pidgey",
  5:"Eevee",
  6:"Sandile"
}
def select(key):
	clear()
	print(f"{pokemon[key]['Name']}{Fore.RESET + Style.RESET_ALL + Back.RESET}\n{pokemon[key]['Desc']}")
	print("press 'e' to go back")
	print("arrow keys, A and D, or Z and X to move in the pokedex")
def pokeOPEN():
	start = 1
	pokeDex = True
	while pokeDex == True:
		select(order[start])
		key = getkey()
		if key == keys.LEFT or key == keys.A or key ==  keys.Z:
			if start > 1:
		 		start -= 1
		elif key == keys.RIGHT or key == keys.D or key == keys.X:
			if start < len(pokemon)-1:
				start += 1
		elif key == keys.E:
			pokeDex == False
			clear()
			print(Fore.RESET + Style.RESET_ALL + Back.RESET)
			return ''