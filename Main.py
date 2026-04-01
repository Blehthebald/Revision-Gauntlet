players = []
elo = []


def FiletoArray(filename, arr):


   with open(filename,'r') as file:
       for line in file:


           arr.append(line.strip())

def ArrayToFile(filename,arr):
   with open(filename,'w') as file:
       for i in range (len(arr)):
           file.write(arr[i])
           file.write("\n")


def Load():
   FiletoArray("Players.txt", players)


   FiletoArray("Elo.txt", elo)




def Save():
   ArrayToFile("Players.txt", players)
   ArrayToFile("Elo.txt", elo)


def AddPlayer():
   name = input("Please input name of player to be added: ")
   alreadyin = False
   i = 0
   while i < len(players) and not alreadyin:
       if name == players[i]:
           alreadyin = True
           print(players[i], "is already in the list, try using a different name")
       i = i + 1
   if not alreadyin:
       players.append(name)
       elo.append("800")
       Save()
       print("Player added successfully")
   main()


def RemovePlayer():
   i = 0
   name = input("Please input name of player to be removed: ")
   found = False
   while i < len(players) and not found:
       if name == players[i]:
           found = True
           players.remove(players[i])
           elo.remove(elo[i])
           Save()
       i = i +1




   if not found:
       print("Player not found in the list, recheck your spelling and try again")
   else:
       print("Player removed successfully")
   main()


def EditPlayer():
   name = input("Please input name of player to be edited: ")


   found = False
   fm = 0
   while fm < len(players) and not found:
       if name == players[fm]:


           found = True
           newelo = input("Please enter new elo value: ")
           elo[fm] = newelo
           Save()
           print("Player edited successfully")
       fm = fm + 1


   if not found:
       print("Player not found in the list, recheck your spelling and try again")
   main()
def Leaderboard():
   leaderboardelo , leaderboardplayer = zip(*sorted(zip(elo, players)))
   leaderboardelo = leaderboardelo[::-1]
   leaderboardplayer = leaderboardplayer[::-1]
   print("~~~~~~~~~~~~~~~~Leaderboard~~~~~~~~~~~~~~~~")
   for i in range (len(leaderboardplayer)):


       print(i+1, " " , leaderboardplayer[i], leaderboardelo[i])
   main()
def GetPlayerElo(name):
   found = False
   i = 0
   while not found and i < len(players):
       if name == players[i]:
           found = True
           return elo[i]
       i = i + 1
   if not found:
       print("Player not found in the list, recheck your spelling and try again")


def probwin(PlayerElo, OtherPlayerElo):
   return 1/(1+10**((OtherPlayerElo-PlayerElo)/400))


def EloChange(PlayerElo, Outcome, ProbOfWin):
   return PlayerElo + 32*(Outcome - ProbOfWin)
def battle():
   found1 = False
   found2= False
   while not found1:
       player1 = input("Please input name of the first player to battle: ")
       for j in range (len(players)):
           if player1 == players[j]:
               found1 = True
               player1rawscore = int(input("Please input the raw score of the first player: "))
               player1time = int(input("Please input the time of the first player: "))
               player1index = j
               break


   while not found2:
       player2 = input("Please input name of the second player to battle: ")
       for k in range (len(players)):
           if player2 == players[k] and k != player1index:
               found2 = True
               player2rawscore = int(input("Please input the raw score of the second player: "))
               player2time = int(input("Please input the time of the second player: "))
               player2index = k
               break
   timedifferentialpenalty = int(input("Please input the time differential penalty: "))


   if player1time < player2time:
       player1weighted = player1rawscore
       player2weighted = player2rawscore - ((player2time - player1time)//timedifferentialpenalty)
   else:
       player2weighted = player2rawscore
       player1weighted = player1rawscore - ((player1time - player2time) // timedifferentialpenalty)
   print(player1weighted, player2weighted)
   if player1weighted > player2weighted:
       print(player1, "wins!")
       player1outcome = 1
       player2outcome = 0
   elif player1weighted < player2weighted:
       print(player2, "wins!")
       player1outcome = 0
       player2outcome = 1
   else:
       print("Draw!")
       player1outcome = 0.5
       player2outcome = 0.5


   player1elo = int(GetPlayerElo(player1))
   player2elo = int(GetPlayerElo(player2))


   prob1win = probwin(player1elo,player2elo)
   prob2win = probwin(player2elo,player1elo)


   player1newelo = int(round(EloChange(player1elo,player1outcome,prob1win)))
   player2newelo = int(round(EloChange(player2elo, player2outcome, prob2win)))
   elo[player1index] = str(player1newelo)
   elo[player2index] = str(player2newelo)


   Save()
   main()


def main():


   valid = False
   while not valid:
       print("--------------------------------------------------------")
       choice = input("What would you like to do?:\n[1] Add a player \n[2] Remove a player \n[3] Edit a player \n[4] Display Leaderboard\n[5] Battle()\n[6] End Session\n: ")
       if choice == "1":
           valid = True
           AddPlayer()
       elif choice == "2":
           valid = True
           RemovePlayer()
       elif choice == "3":
           valid = True
           EditPlayer()
       elif choice == "4":
           valid = True
           Leaderboard()
       elif choice == "5":
           valid = True
           battle()
       elif choice == "6":
           valid = True
           Save()


       else:
           print("Please enter a valid option")
Load()
main()





