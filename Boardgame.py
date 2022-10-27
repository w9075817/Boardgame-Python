#Importing all the functions needed to run the game
import random
import boardgame_functions
import time

#These are defining the functions used in the game
def print_board():#This is used to print the board and format the leters correctly
    print('-' * 48, '\n')
    for x in range(0,len(treasures)):
        if x== 0 or x == 8 or x == 16 or x == 24 or x == 32:
            print('|', sep= ' ', end=' ', flush= True)
        print(treasures[x], ' | ', sep=' ', end=' ', flush =True)
        if ( (x%8) == 7):
            print('\n')
            print('-' * 48, '\n')

def clean_list(i):#This is used to take any unwanted values out of the collected gems list
        while '*' in treasure_collected[i]:
            treasure_collected[i].remove('*')
        while ' ' in treasure_collected[i]:
            treasure_collected[i].remove(' ')

def bonus_gem(bonus):#This is a function used to grant the player with a bonus gem if they dont make the last move
    global gem_scores
    a = random.randint(0,4)
    gem_scores[bonus][a] = gem_scores[bonus][a] + 1
    print('\nPlayer', bonus, 'got the bonus point!#')

def gem_score(num_gems):#This function is used to convert the amount of gems collected to points
    score = 0
    for x in range (1, num_gems + 1):
        score = score + x
    return score

def print_end_score():#This is used to print the final scores
    if total_1 > total_2:
        print(player_one, 'wins!')
    elif total_1 < total_2:
        print(player_two, 'wins!')
    elif total_1 == total_2:
        print("It's a draw!")
#These variables act as a counter for which move the game is on and which players turn it is
move = 0
tempmove = 0
player = 1
#This is a nested list to dictate the gems scored by each player
gem_scores = [[], []]
#These variables all help with drawing the board and labeling the different types of gems
gem_types = 'EDRS'
gem_types_w_beads = 'DERSB'
gem_names = ["Diamonds:", "Emeralds:", "Rubys:", "Saphires:", "Beads:"]
number_of_gems = len(gem_types)
treasures_string = ""
#This loop populates the treasures string with the correct number of each value
for i in range(0, number_of_gems):
    treasures_string = treasures_string + (gem_types[i] * 7)
treasures_string = treasures_string + ("B" * 11)
treasures = list(treasures_string)
#These are the moves available for the player
moves_available = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
#These are the nested lists for the treasures collected for each player
treasure_collected = [[], []]
#This randomises the gems and beads and inserts the counter at the beggining of the board
random.shuffle(treasures)
treasures.insert(0, '*')
#This imports the rules for the board game from a different module and prints them out
boardgame_functions.print_rules()
print('')
#This lebels each player with a different name to identify who's turn it is
player_one = ''
player_two = ''
while 3> len(player_one) or len(player_one)> 20:
    player_one = input('What is the name of Player 1? ')
    if 3> len(player_one) or len(player_one)> 20:
        print('Invalid Name')
while 3> len(player_two) or len(player_two)> 20:
    player_two = input('What is the name of Player 2? ')
    if 3> len(player_two) or len(player_two)>20:
        print('Invalid Name')
#This calls the function to print the board
print_board()
#This displays the cards to use and the moves available
print('Cards to use:', moves_available)
#This loop holds the bulk of the game and each players turn
next_move = ''

while tempmove < 39:#This dictates how long the loop will last which is 39 spaces
    if player == 1:#This is how a turn is decided
        print(player_one, 'its your turn')
        next_move = input('What move do you want to make? ')
        if next_move != '':
            next_move = int(next_move)#This converts the next move to an intger 
        if ValueError:
            pass
        if next_move in moves_available and next_move != '':#This checks if the move chosen is in the available move list
            tempmove = move + next_move
            if tempmove < 39:
                move = tempmove
            move = (int(move))
            for x in range(0,move):#This loop collects the treasures up to the move made
                treasure_collected[0].append(treasures[x])
                treasures[x] = ' '
            treasures[move] = '*'#This moves the counter
            moves_available.remove(next_move)
            print_board()
            player = 2
        else:
            print('Invalid move')#This denies the move made
        clean_list(0)
        print(player_one, 'has collected:', treasure_collected[0])
        print('Cards to use:', moves_available)
        bonus = 0
    elif player == 2:#This is how a turn is decided
        print(player_two, 'its your turn')
        next_move = input('What move do you want to make? ')
        if next_move != '':
           next_move = int(next_move)#This converts the next move to an intger   
        if ValueError:
            pass
        if next_move in moves_available and next_move != '':#This checks if the move chosen is in the available move list
            tempmove = move + next_move
            if tempmove < 39:
                move = tempmove
            move = (int(move))
            for x in range(0,move):#This loop collects the treasures up to the move made
                treasure_collected[1].append(treasures[x])
                treasures[x] = ' '
            treasures[move] = '*'#This moves the counter
            moves_available.remove(next_move)
            print_board()
            player = 1
        else:
            print('Invalid move')#This denies the move made
        clean_list(1)
        print(player_two, 'has collected:', treasure_collected[1])
        print('Cards to use:', moves_available)
        bonus = 1
    if tempmove > 39:#This ends the game when the players reach the end of the board
        move = 39

total_1 = 0
total_2 = 0
for x in range(0, len(gem_types_w_beads)):#This retrieves the total for each gem
    gem_scores[0].append(gem_score(treasure_collected[0].count(gem_types_w_beads[x])))
    gem_scores[1].append(gem_score(treasure_collected[1].count(gem_types_w_beads[x])))
bonus_gem(bonus)
for x in range(0, (len(gem_scores))):#This adds up the total for each gem and returns a total score 
    total_1 = total_1 + gem_scores[0][x]
    total_2 = total_2 + gem_scores[1][x]

print('Highscores:')#This prints out the scores for the players
print('\n', player_one)
for x in range(0, len(gem_names)):
    print(gem_names[x], gem_scores[0][x])
print('\n', player_two)
for x in range(0, len(gem_names)):
    print(gem_names[x], gem_scores[1][x])
print('\n', player_one)
print('Total points:', total_1)
print('\n', player_two)
print('Total points:', total_2)
print_end_score()
time.sleep(10)
