#######################################################################################
#   Rosen Georgiev W0405552 PROG1700-705
#    Started at   10/12/2017
#   That should be my ToolBox
#
#######################################################################################

    # Thank's Jeff for the clean_scr! have to fix it but now works

    # Clears the terminal window in an operating specific way

    # get the first character of the operating system we are using

import sys
import os
import time

# Nice duck from Jeff

def duckling_wait(seconds):

    #import sys
    #import time

    duck = """ASCII Duck says, "Wait":
            _
       ____{ o>
    ~~~\_<_._)~~~~
          <_"""
    sys.stdout.write(duck)
    frames = ["      \\ ", "      <_", "     _/ "]
    sleep_time = 0.3
    frame = 0
    total_frames = len(frames)
    while seconds > 0:
        sys.stdout.write("\r    " + frames[frame] + "      ")
        frame = frame + 1
        frame = frame % total_frames
        time.sleep(sleep_time)
        seconds = seconds - sleep_time
    sys.stdout.write("\n")


#small script for WAIT by different OS

def wait_prompt():
    if sys.platform.lower().startswith('w'):
        # windows version
        os.system("pause")
    elif sys.platform.startswith('l'):
        # linux version
        os.system('read -s -n 1 -p "Press any key to continue..."')
    else:
        print("PRES ENTER TO CONTINUE...")


# small screen cleaning solution

def clear_screen():
    if sys.platform.lower().startswith('w'):
        # windows version
        os.system("cls")
    elif sys.platform.startswith('l'):
        # linux version
        os.system("clear")
    else:
        print("\n" ** 1000)


#Easy way to get the CURENT file name

def file_name():
    #import os

    filename = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    return filename


# That's only MINE Title Page!

def title():
    #should change to get the name not from my.py
    filename = file_name()
    # vertical symbol
    str0 = "[0]"
    # horizontal symbol POCEH is my name on cyrillic
    str1 = "POCEH"
    # screen width
    str2 = int(80)
    # screen high - 2 lines
    str3 = int(24) - 2
    autor = "Rosen Georgiev"
    stNum = "W0405552@nscc.ca"
    authority = "SysAdmin & Security"
    underline = "NSCC IT Campus"
    # text
    str4 = ["oooO*FINAL*Oooo", filename, autor, stNum, authority, underline]
    # my first try to do that!
    header = str1 * int(str2 / len(str1))
    line2 = str0.ljust(int(str2 / 2)) + str0.rjust(int(str2 / 2))
    repeat = int((str3 / 2) - len(str4) / 2)

    clear_screen()

    print(header)
    # maybe in the future will be better
    for i in range(repeat):
        print(line2)

    for i in range(len(str4)):
        duma = str4[i]
        text = duma.center(str2 - int(len(str0) * 2))
        line = str0 + text + str0
        print(line)

    for i in range(repeat):
        print(line2)

    print(header)

    #wait_prompt()



def GetDigitCount():
    # First wiil get some input from the user
    # and will check it is it numeric
    # then check for negative numbers and convert to positive by multiplying to -1
    while True:
        try:
            num = float(input("Enter a number: "))
        except ValueError:
            dig1 = "Invalid Entry!"
        else:
            num = int(num)
            if num < 0:
                num = num * -1
            # start check for the digits
            if num > 0:
                dig1 = 1
            if num > 10:
               dig1 = 2
            if num > 100:
                dig1 = 3
            if num > 1000:
                dig1 = 4
            if num > 10000:
                dig1 = 5
            if num > 100000:
                dig1 = 6
            if num > 1000000:
                dig1 = 7
            if num > 10000000:
                dig1 = 8
            if num > 100000000:
                dig1 = 9
            if num > 1000000000:
                dig1 = 10
            if num > 10000000000:
                dig1 = 11
            if num > 100000000000:
                dig1 = 12
            if num > 1000000000000:
                dig1 = 9
            #else:
                #dig1="...etc."
            # and same ... till the end
        print("Digit Count Result: {}".format(dig1))
        break


# check the value of input is it a number:

def check_inpit_num (text, error):
    while True:
        try:
            number = float(input(text))
            #some = 1000 / number
        except ValueError:
            print(error)
        # except ZeroDivisionError:
        #     print(error)
        else:
            return number

# error = "Incorect Value!"
# text = "Enter a number: "
#
# print("{} is a number".format(check_inpit_num(text,error)))