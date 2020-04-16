from random import randint
print("Welcome to Tic-Tac-Toe!")
p1_name=input("Enter player1 name:")
p2_name=input("Enter player2 name:")
print("Choices available are: O and X")
choice_lst=['X','O']
location_list=[1,2,3,4,5,6,7,8,9]
str1='  -  ¦  -  ¦  -  \n'
str2='-----------------\n'
str3='  -  ¦  -  ¦  -  \n'
str4='-----------------\n'
str5='  -  ¦  -  ¦  -  '
#str_lst=[str1,str2,str3,str4,str5]
display_board_str=str1+str2+str3+str4+str5
print(display_board_str)
def display_board(loc,choice,display_board_str):
  display_board_str_split=display_board_str.split('\n')
  str1=display_board_str_split[0]
  str2=display_board_str_split[1]
  str3=display_board_str_split[2]
  str4=display_board_str_split[3]
  str5=display_board_str_split[4]
  str_lst=[str1,str2,str3,str4,str5]
  if loc in (1,2,3):
    row1_lst=str1.split('¦')
    if loc==1:
      row1_lst[0]=row1_lst[0].replace('-',choice)
    elif loc==2:
      row1_lst[1]=row1_lst[1].replace('-',choice)
    else:
      row1_lst[2]=row1_lst[2].replace('-',choice)
    str1='¦'.join([x for x in row1_lst])
    str1+='\n'
    str2+='\n'
    str3+='\n'
    str4+='\n'
    
    display_str=str1+str2+str3+str4+str5
    return display_str
  elif loc in (4,5,6):
    row2_lst=str3.split('¦')
    if loc==4:
      row2_lst[0]=row2_lst[0].replace('-',choice)
    elif loc==5:
      row2_lst[1]=row2_lst[1].replace('-',choice)
    else:
      row2_lst[2]=row2_lst[2].replace('-',choice)
    str3='¦'.join([x for x in row2_lst])
    str1+='\n'
    str2+='\n'
    str3+='\n'
    str4+='\n'
    display_str=str1+str2+str3+str4+str5
    return display_str
  else:
    row3_lst=str5.split('¦')
    if loc==7:
      row3_lst[0]=row3_lst[0].replace('-',choice)
    elif loc==8:
      row3_lst[1]=row3_lst[1].replace('-',choice)
    else:
      row3_lst[2]=row3_lst[2].replace('-',choice)
    str5='¦'.join([x or x in row3_lst])
    str1+='\n'
    str2+='\n'
    str3+='\n'
    str4+='\n'
    display_str=str1+str2+str3+str4+str5
    return display_str
first_chance=randint(1,2)
if first_chance==1:
  print("Player 1 will take first chance")
  p1_choice=input("Enter player1 choice:")
  if choice_lst[0]==p1_choice:p2_choice=choice_lst[1]
  else:p2_choice=choice_lst[0]
else:
  print("Player 2 will take first chance")
  p2_choice=input("Enter player2 choice:")
  if choice_lst[0]==p2_choice:p1_choice=choice_lst[1]
  else:p1_choice=choice_lst[0]
for chance_num in range(1,10):
  if chance_num%2!=0:
    if first_chance==1:
      board_loc=int(input("Player-1, Please choose any num from the avl list {1}:".format(first_chance,location_list)))
      display_board_str=display_board(board_loc,p1_choice,display_board_str)
      print(display_board_str)
    else:
      board_loc=int(input("Player-2, Please choose any num from the avl list {1}:".format(first_chance,location_list)))
      display_board_str=display_board(board_loc,p2_choice,display_board_str)
      print(display_board_str)
  else:
    if first_chance==1:
      board_loc=int(input("Player-2, Please choose any num from the avl list {1}:".format(first_chance,location_list)))
      display_board_str=display_board(board_loc,p2_choice,display_board_str)
      print(display_board_str)
    else:
      board_loc=int(input("Player-1, Please choose any num from the avl list {1}:".format(first_chance,location_list)))
      display_board_str=display_board(board_loc,p1_choice,display_board_str)
      print(display_board_str)
  location_list.remove(board_loc)
