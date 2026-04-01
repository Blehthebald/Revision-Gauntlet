# LIST OF FUNCTIONS
## FiletoArray(filename, arr)
Reads a file and puts the contents of the file into an array
## ArrayToFile(filename,arr)
Reads the contents of an array and writes it to a file
## Load()
Load data in Players.txt to the player array and Elo.txt to the elo array
## Save()
Save data from the player and elo array into Players.txt and Elo.txt respectively
## AddPlayer()
Prompts for a player's username and adds them to the player array before saving it to players.txt, checks for username duplocates
## RemovePlayer()
Prompts for a player's username and removes them, checks if player is in the array
## EditPlayer()
Prompts for a player's username and checks if they are in the array before prompting for the new elo 
## Leaderboard()
Displays Player names and their elo in descending order of elo
## GetPlayerElo(name)
Gets the elo of a player whose name is set as the parameter
## probwin(PlayerElo, OtherPlayerElo)
Calculates the probability of a player winning based on the elo differential of them and their opponent
## EloChange(PlayerElo, Outcome, ProbOfWin)
Calculates the new elo of a player after a match based on their current elo, the outcome of the match and the probability that they were going to win that match
## battle()
Initiates a match between two players
## main()
The main interface for commands
