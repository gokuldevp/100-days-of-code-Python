# 🚨 Don't change the code below 👇
row1 = ["☠️","☠️","☠️"]
row2 = ["☠️","☠️","☠️"]
row3 = ["☠️","☠️","☠️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("\nWhere do you want to put the treasure? \n\n")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
valid_positions = ["11","22","33","12","13","23","21","31","32"]
#if position == '11' or position == '22' or position == '33' or position == '12' or position == '13' or position == '23' or position == '21' or position == '31' or position == '32':
if position in valid_positions:
  position1 = int(position[0])
  position2 = int(position[1])
  map[position1-1][position2-1] = "🏆   "
else:
  print("\nYou didn't select a valid position\n")
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"\n{row1}\n{row2}\n{row3}")
