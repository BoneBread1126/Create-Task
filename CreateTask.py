import random
def failure(kills, rooms):
  print("You have died maidenless and alone.")
  print("You killed " + str(kills) + " enemies and had " + str(rooms) + " rooms left.")
  exit()
enemy = [0,0] 
player = [100, 0, 5, 10]
rooms = 5
action = 0
kills = 0
while (True):
  if rooms > 0:
    print("You've ran into an enemy")
    enemy[0] = random.randrange(20, 50)
    enemy[1] = random.randrange(10, 20)
  else:
    print("From the dark depths of the dungeon HE arose, Mr Cestaric approaches.")
    enemy = [120,25]
  while enemy[0] > 0 and player[0] > 0:
    print("enemy health: " + str(enemy[0]))
    action = input("What do you do?  1. Attack  2. Defend  3. Heal ")
    if action == "1":
      enemy[0] = enemy[0] - player[3]
    elif action == "2":
      player[1] = player[2] + 5
    elif action == "3":
      player[0] = player[0] + 50
    if player[0] > 100:
      player[0] = 100
    player[0] = player[0] - enemy[1]
    print("")
    print("The enemy attacks! Your health is " + str(player[0])) 
    print(" ")
    if player[0] <= 0:
      failure(kills, rooms)
    if enemy[0] <= 0:
      print("The enemy has been incapacitated!")
      kills = kills + 1
      print(" ")
      action = input("What do you upgrade?  1. Damage  2. Defense  3. Luck")
    if action == "1":
      player[3] = player[3] + player[2]
    elif action == "2":
      player[1] = player[1] + player[2]
    elif action == "3":
      player[2] = player[2] + player[2]
  rooms -= 1;
  if rooms < 0:
    break
print("You win!")