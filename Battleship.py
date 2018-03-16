#################################################################
#   Rosen Georgiev W0405552 Prog1700/705                        #
#           FINAL Assignment                                    #
#         The 'BATTLESHIP' Game                                 #
#################################################################
# Design and develop a program that replicates the functionality
# of the provided sample application, a simple version of the game Battleship.
#
# Begin by designing your solution to this problem in pseudocode,
# which will be submitted along with the program.
# Your solution should demonstrate an understanding of how to apply file I/O,
# list and looping concepts, in a Battleship program that will work as follows:
#
# On application start, your code will read the contents of the provided ship grid text file into a
# two-dimensional list in your program. This ship map will be used as the “key”,
# indicating the locations of the five ships used in the game.
# Zeros (0) indicate empty water, while ones (1) indicate part of a ship exists at that location.
# The ship map will remain invisible to the user during gameplay.
# A second map (the targeting map) will be displayed to the user each turn,
# and will be used to show the targeting results of the current game turn by turn.
# The initial display of the targeting map will be blank except for the row and column indicators
# (Columns A, B, C, Rows 1, 2, 3, etc.).
#
# The user will be given 30 turns to attempt to sink all five ships.
# During each turn, the user will be prompted to enter a map coordinate
# (ex. A2, F5, B10) representing the location at which they wish to fire a missile.
# After each missile shot attempt, your program will evaluate whether the chosen coordinate
# is a hit or a miss and notify the user of the result.
# The targeting map will be updated to show the latest missile result and be shown to the user.
# A message indicating the current missile count will also be displayed,
# used to tell the player how many turns remain.
#
# Only valid targeting coordinates are allowed to be entered.
# If an invalid coordinate value is entered, the user will be prompted to re-enter
# a new coordinate until a valid coordinate is entered.
# The game has two ending conditions:
#
# •	If the user hits every individual location in the map that contains part of a ship before
#     running out of missiles, they win the game.
# •	If the user runs out of missiles before hitting every part of every ship, they lose the game.
#
# Your program should track the game’s progress and display either a “You win!”
# or “You lose!” message when either game ending condition is reached.
#
# Bonus Marks: Add functionality to the game such that the user is notified when
# a particular ship has been definitively sunk. You’ll likely need to modify the
# contents of the map so that it stores more than just ones and zeros in order to
# identif                                                                                                                                                                                                                                                                                                               y each ship individually.


# PSEUDO:
#
# Because this program is part of the Final project,
# there will be some personal touches
# there are a couple differences from the assignment-5
# The presentation will start with my Title page
# While the program will print a welcome message it
#
# Asking for user name at the beginning
# if the username is empty it will be replaced with the current user from OS
#
# Check the highest score from the csv file and display it as a part of a welcome message
#
# choose random map texture from the map folder for each game
# import the data from 'ShipMapX.txt
#       check the data and add the ship parts positions to list 'positions'
#       add the positions in list 'filling'
# close the txt
#
# print the map including h-line and v-lines
#       in v-line function look if there are hits in the list and display them on the map
#            o - for unsucefful
#            x - for succeful hit
#
# ask user for input the coordinates
#       check the remaining missles - if equal 0 - done - game over
#       check if input is valid; is the h-letter exist in list, is the v-number exist in list
#       check if the input match the target list: yes - add 1 to success number
#                                               add it to hits list
#                                               print HIT and sound
#       check the number of sucefull shots: if equal to the ship parts - done - win
#
# print the results
# Append the scores in .csv only if are > from the high score (to avoid overload)
# as extra ask if the user want to have an certificate and print it!
# The program can be terminated any time by typing Q or q at the prompt
# It will ask the player if he want to try one more time

# THERE IS an EXTRA help - type "??" - do not cheat!!!

import random
import csv
import datetime
import my
import os


h_header = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
v_header = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filling = []
positions = []
hits = []
high_ScorE = []
score_list = []

maps_dir_path = "maps"
answers = ['yes','y']

maxScor = [0]

# Ask for Username
def user_name():
    name = input("Please enter your name for the score record: ")
    if name == "":
        name = os.getenv('username')

    return name

def high_score_list():

    with open("scores.csv", "r") as scores_source:
        csv_list = csv.reader(scores_source)
        for row in csv_list:
            high_ScorE.append(row)
            if len(row) != 0:
                s = (row[0],row[3])
                score_list.append(s)


# choose random map
def random_map():

    list = os.listdir(maps_dir_path)
    ind = random.choice(list)
    return ind

def print_high_list():
    ls = sorted(score_list,key=lambda x:x[1],reverse=True)

    if len(ls) != 0:

        for s in range(0,len(ls)):
            print(s+1,score_list[s][0],score_list[s][1])

    else:
        print("Still have no High Score Records")

# return the message with the highest user score
def get_usr_score():
    high_score_list()
    hi_scor = max(maxScor)
    bigone = "{}, you are the first player".format(userName)
    scores = high_ScorE
    for row in scores:
        if len(row) != 0:
            scorx =  float(row[3])

            if scorx>=hi_scor:

                bigone = "As I know {0} is on the top with {3:.2f}% success,\nfrom {2} ships he sank {1}!!!\nTry to beat that record!\n".format(row[0],row[1],row[2],scorx)
                hi_scor = scorx
        else:
            bigone = bigone
            maxScor.append(hi_scor)
    return bigone

# save The highest scores in .csv
def add_user_score(success, pos, high_ScorE=high_ScorE):

    scor = max(maxScor)
    with open("scores.csv", "w") as SCORES:
        suc_score = success/pos*100
        want = input("Do you want to save your scores? (Yes or No): ")
        if want.lower() in answers:

            if len(high_ScorE) >= 10:
                high_ScorE.pop(-1)
            result = [userName,success,pos,suc_score,str(datetime.datetime.date(datetime.datetime.now()))]
            if len(result) != 0:
                high_ScorE.append(result)
            csvwriter = csv.writer(SCORES)
            for row in high_ScorE:
                csvwriter.writerow(row)


# read certificate.html / write award.html
def write_cert(success, pos, name):
    name = name.replace(",", " ")
    pname = name.lower()
    pname = pname.replace(" ","_")
    suc_score = success / pos * 100
    path = os.path.normcase('certificates/')

    try:
        cert_y = input("Do you want an Certificate of completion? 'Yes/No': ")
        cert_y = cert_y.lower()
    except:
        cert_y = 'n'
    if cert_y in answers:
        with open(r'{}certificate.html'.format(path), 'r') as cert:
            with open(r'{}award_{}.html'.format(path, pname), 'w') as award:
                cert = cert.read()
                award.write(cert.format(name, success, pos, suc_score, str(datetime.datetime.date(datetime.datetime.now()))))
        my.duckling_wait(4)
        award.close()
        os.startfile(r'{}award_{}.html'.format(path, pname))


# print the lines, check the hits, assign the symbol
def v_line():

    for i in (v_header):
        text = ""
        v = i
        i -= 1

        for h in range(len(h_header) - 1):

            match = h_header[h+1]+str(v)

            if len(hits) > 0:
                good = (set(hits) & set(positions))
                notgood = (set(hits) - set(good))

                if match in notgood:
                    text += (" 0")
                elif match in good:
                    text += (" X")
                else:
                    text += ("  ")
            else:
                text += ("  ")

        print("{0:<2}{1:>2}".format(i+1, text))



# HEADER of the map
def header():

    head_text = " "
    for b in range(len(h_header)):
        head_text += (h_header[b] + " ")
    print(head_text)

# print the map
def file_map():

    header()
    v_line()

# import the lines from the file and write the positions in list
def get_line_file():
    with open('{0}/{1}'.format(maps_dir_path, random_map()), 'r') as file:
        n = 0
        for line in file:
            some = []
            line = line.split(',')
            for a in range(len(line)):
                pixel = line[a][0]
                some.append(pixel)
                if pixel == "1":
                    positions.append(str(h_header[a + 1]) + str(v_header[n]))

            filling.append(some)
            n += 1

# Ask for more
def one_more_game():
    will_ = input("Would you like to try one more time? (Yes or No): ")
    if will_.lower()in answers:
        return True
    else:
        print("Thank you for playing BATTLESHIP!")
        return False


# The game :)
def the_game(name):

    get_line_file()
    missles = 30
    success = 0
    pos = len(positions)


    print(
        "Hi {},\nLet's play Battleship!\nYou Have {} missles to sink all {} ships.\nYou can quit by typing 'q'\n".format(
            userName, missles, pos))
    print(get_usr_score())
    print_high_list()
    print()

    while success < pos:

        if missles > 0:

            file_map()

            try:
                tri = input("\nChoose Your Target (Ex. A7): ")
                my.clear_screen()
                if tri == "??":  # Just for test purpose! DO NOT CHEAT!!!
                    hint = random.choice(positions)
                    print("With compliments from the author: {}!".format(hint))
                elif tri == "Q" or tri == "q":
                    break

                t = tri[0].upper()
                h_header.index(t)

                a = len(tri)
                if a < 2:
                    raise ValueError
                if a == 2:
                    n = int(tri[1])
                    v_header.index(n)
                    tri = t + tri[1]
                elif a == 3:
                    n = int(tri[1] + tri[2])
                    v_header.index(n)
                    tri = t + tri[1] + tri[2]

            except:
                print("Incorect input!\nSample: B10")
                print("You have {} missles remaining\n".format(missles))
                # OUTPUT
            else:

                hits.append(tri)
                missles -= 1
                success = len(set(hits) & set(positions))

                if tri in positions:

                    print("HIT!!!!!", '\a')  # try to beep...very interesting it beeps only by hiting some ship parts???

                    if success < pos:
                        print("You have {} missles remaining\n".format(missles))
                    else:
                        add_user_score(success,pos)

                        print(
                            "YOU SANK MY ENTIRE FLEET!\a\a\a\nYou had {0} of {1} hits, which sank all the ships!\nYou won, congratulations!".format(
                                (success), pos))

                        write_cert(success, pos, name)

                else:

                    print("Miss")
                    print("You have {} missles remaining".format(missles))
        else:
            add_user_score(success, pos)

            print("GAME OVER.\n{} you had {} of {} hits, but didn't sink all ships!\nBetter luck next time.".format(name,
                (success), pos))

            write_cert(success, pos, name)
            break

##################################OUTPUT#######################################



my.title()
my.wait_prompt()
userName = user_name()

will_ = True

while will_ is True:
    my.clear_screen()
    the_game(userName)
    will_ = one_more_game()
    #RESET THE LISTS
    hits = []
    filling = []
    positions = []
