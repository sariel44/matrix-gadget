import curses
import time
import random

strArray = []
blinkXPos = []
blinkYPos = []

maxBlink = 5
maxL = 0
maxC = 0
alphabet=u"АБВГДЕЖИІКЛМНОПРСФЦЧШЩЪЪІ[ХЬѢЮѮѰѲabcdefghijklmnopqrstuwxyzҀ[абвгдеёжзийклмнопрстуфхцчшщъыьэюяABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()[]-+<>,.?/:;{}"

def initWindow():
    window = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_GREEN)
    return window

def choice():
    if(random.randrange(0,10) > 2):
            return " "
    return random.choice(alphabet)

def stopWindow():
    curses.endwin()


def main():
    global maxL, maxC,maxBlink
    window = initWindow()
    maxL,maxC = window.getmaxyx()
    while True:
        line = u"".join([choice() for i in range(0, maxC - 1)])
        strArray.insert(0, line)

        window.noutrefresh()
        if len(strArray) > maxL:
                window.move(maxL - 1,0)
                window.clrtobot()
                strArray.pop()

         

        for i in range(0,len(strArray) - 1,1):
            window.addstr(i,0,strArray[i], curses.color_pair(1))
            if(random.randrange(0,10) > 3):
                jd = random.randrange(1, maxBlink)
                j = int(random.randrange(0,maxL - 1) * 1/jd + maxBlink)
                k = random.randrange(0,maxC - 1)
                blinkYPos.insert(0,j)
                blinkXPos.insert(0,k)

                # Update blinkers
                for j in range(0,len(blinkYPos) - 1):
                    for k in range(0,len(blinkXPos) - 1):
                        p = blinkYPos[j]
                        q = blinkXPos[k]
                        if p < len(strArray): 
                            blinkYPos[j] = blinkYPos[j] + 1
                            window.addstr(p,q,strArray[p][q],curses.color_pair(2))
                        window.addstr(1,1,"%s"%p,curses.color_pair(2))
                        window.addstr(2,1,"%s"%q,curses.color_pair(2))
                        window.addstr(3,1,"%s"%len(strArray),curses.color_pair(2))
                if(len(blinkYPos) > maxBlink):
                    blinkYPos.pop()
                    blinkXPos.pop()
            window.refresh()

        if random.randrange(0,10) > 8:
            curses.flash()
        time.sleep(0.2)


    stopWindow()


main()
