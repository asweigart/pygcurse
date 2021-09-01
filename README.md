Pygcurse
========

http://inventwithpython.com/pygcurse

https://github.com/asweigart/pygcurse


Pygcurse (pronounced "pig curse") is a curses library emulator that runs on top of the Pygame framework. It provides an easy way to create text adventures, rougelikes, and console-style applications.

Unfortunately, the curses library that comes with the Python standard library does not work on Windows. The excellent Console module from effbot provides curses-like features, but it only runs on Windows and not Mac/Linux. By using Pygame, Pygcurse is able to run on all platforms.

Pygcurse provides several benefits over normal text-based stdio programs:

    1) Color text and background.
    2) The ability to move the cursor and print text anywhere in the console window.
    3) The ability to make console apps that make use of the mouse.
    4) The ability to have programs respond to individual key presses, instead of waiting for the user to type an entire string and press enter (as with input()/raw_input()).
    5) Since the console window that Pygcurse uses is just a Pygame surface object, additional drawing and transformations can be applied to it. Multiple consoles can also be used in the same program.

Pygcurse requires Pygame to be installed. Pygame can be downloaded from http://pygame.org

Pygcurse was developed by Al Sweigart (al@inventwithpython.com)

https://github.com/asweigart/pygcurse

The github repo contains several example programs.


Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
