################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#local scope:

def drink_strength_portion():
    portion_strength = 2 #here portion strength is a local so it can only be accessed in side the function
    print(portion_strength)

drink_strength_portion()
#print(portion_strength) - portion_strength is not avalible since it is local scope

#Global scope:

player_health = 10
def game():
    def drink_health_potion():
        portion_health = 5
        print(portion_health)

    drink_health_potion()
game()    
print(player_health)

# There is no block scope in python

game_level = 3
def create_enemy():
    global game_level  #modifying global scope is not recomented
    game_level = 4
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)   
create_enemy() 

#changeing globalscope value without global scope:
player_level = 3
enemies = ["Snake"]
def create_enemies():
    print(f"The current enemies is {enemies}")
    return player_level + 1 and enemies.append("Bear")
create_enemies()
print(f"The current enemies is {enemies}")  

# Global Constands:


def pi():
    global PI 
    PI =  3.14
    return PI
def google():
    global URL
    URL = "https//www.google.com"
    return URL    

print(pi())
print(google())
