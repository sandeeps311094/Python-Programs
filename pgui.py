#-- Trial tutorial of pyautogui module with basic examples --#

import time
import pyautogui as pygui
import pyperclip

#--
def display_screen_resolution():
    print ("\nScreen resolution: {}\n".format (pygui.size()))

#--
import pyautogui as pygui
def move_mouse_to():
    time.sleep (0.0)
    pygui.moveTo (1000, 1200, duration = 0.75)

#--
def relative_mouse_move():
    pygui.moveRel (1045, 0, duration = 0.75)

#--
def position():
    time.sleep (4)
    print ("\nCurrent cursor position: {}\n".format (pygui.position ()))

#--
def click():
    pygui.click (415, 50)

#--
import imp
from nltk import word_tokenize
def typrwrite():
    pygui.moveTo (655, 49, duration = 0.75)
    pygui.click (655, 49, duration = 0.75)
    time.sleep (0.25)
    function_name = "pyautogui"
    ls_func = word_tokenize (function_name)

    pygui.moveTo (403, 477, duration = 0.75)
    pygui.click (403, 477)

    pygui.typewrite ("Lord Shiva's trident")
    time.sleep (2.5)
    pygui.hotkey ('ctrl', 'a')
    nltk.word_tokenize ()

    pygui.click (811, 374)
    pygui.click (490, 554)

    '''
    decision_01 = int (input ("\n1. Google page\t2. Continue searching"))
    if (decision_01 == 1):
        pygui.click (148, 186)
    elif (decision_01 == 2):
        pygui.click (480, 191)
    else:
        print ("\nInvalid input !")
    '''

    str1 = str (pygui.prompt ('This displays some text... '))
    print ("\n\nSTR1 --> {}\n".format (str1))

    pygui.moveTo (604, 87)
    pygui.click (604, 87)
    pygui.hotkey ('ctrl', 'a')
    pygui.typewrite (['backspace'])
    pygui.typewrite ("www.google.com")
    pygui.hotkey ('enter')
    time.sleep (1.25)


    pygui.moveTo (491, 481)
    pygui.click (491, 481)
    pygui.typewrite (str1)
    pygui.click (915, 378)
    pygui.click (504, 547)

#--
def right_click():
    pygui.moveTo (949, 585)
    #pygui.click (button = 'right')
    pygui.scroll (-40)

#--
def main_automator():
    time.sleep (0.75)
    song_name = str (input ("Please enter the song name: "))
    song_name = 'title:' + '"' + song_name + '"' + ' type:audio'

    pygui.moveTo (30, 65, duration = 0.75)          #-- Cursor opening Firefox
    pygui.click (button = 'left')

    pygui.moveTo (340, 73, duration = 0.75)
    pygui.click ()
    time.sleep (1.25)

    pygui.moveTo (144, 199)             #-- Cursor at G-Drive icon to refresh
    pygui.click ()
    time.sleep (3.75)

    pygui.moveTo (485, 195, duration = 0.75)        #-- Cursor at G-Drive search bar
    pygui.click ()
    time.sleep (1.75)

    input_folder = "Music & Art"            #-- Input the folder name and click()
    pygui.typewrite (input_folder)
    time.sleep (2.25)
    pygui.moveTo (427, 242, duration = 0.75)
    pygui.click ()
    time.sleep (2.0)
    pygui.click ()

    input_subfolder_1 = "San"            #-- Input the sub-folder name and click()
    input_subfolder_2 = " Sree"
    pygui.moveTo (485, 195, duration = 0.75)
    pygui.click (button = 'left')
    time.sleep (4.5)
    pygui.typewrite (input_subfolder_1)
    time.sleep (2.5)
    pygui.typewrite (input_subfolder_2)
    time.sleep (2.25)
    pygui.moveTo (446, 282)
    pygui.click (button = 'left')

    pygui.moveTo(485, 195, duration=0.75)
    pygui.click(button='left')
    pygui.typewrite (song_name)
    time.sleep(2.75)

    pygui.hotkey ('enter')
    time.sleep (4.0)
    pygui.moveTo (423, 451, duration = 1.25)
    time.sleep (0.75)
    pygui.rightClick ()

    pygui.moveTo (458, 937, duration = 1.025)
    time.sleep (1.0)
    pygui.click ()
    time.sleep (7.5)
    pygui.moveTo (1180, 700, duration = 1.0)
    pygui.click ()

    time.sleep (5.5)
    pygui.moveTo (1765, 119, duration = 0.5)
    pygui.click ()
    pygui.moveTo (1230, 175)
    time.sleep (1.75)
    pygui.click ()

#--
def screenshot():
    time.sleep (1)
    main_automator()

#--
def tester():
    time.sleep (5)
    pygui.moveTo (404, 451, duration = 2.25)
    pygui.rightClick ()

#-------------------------
if __name__ == '__main__':
    #typrwrite ()
    #position ()
    screenshot()
    #tester()
