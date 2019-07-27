import math
import time

from graphics import *

def linePt(x1, y1, x2, y2):
    return Line(Point(x1, y1), Point(x2, y2))

def sin(a, b, c, d, x):
    return -(a*math.sin(((2*math.pi)/b)* (x - c)) + d)

def cos(a, b, c, d, x):
    return -(a*math.cos(((2*math.pi)/b)* (x - c)) + d)

def inputs():

    global graphType
    global a
    global b
    global c
    global d

    graphType = input("Enter the type of graph (cosine or sine): ").lower()
    if graphType != "cosine" and graphType != "sine" and graphType != "cos" and graphType != "sin":
        for i in range (0, 4):
            graphType = input("Your input was not \"cosine\" or \"sine\". Please input the type of graph (cosine or sine): ").lower()
            if graphType == "cosine" or graphType == "sine" or graphType == "cos" or graphType == "sin":
                break
            if i == 4:
                print("You did not input \"cosine\" or \"sine\". The graph has been defaulted to sine.")
                graphType = "sine"
                break

    a = input("Enter an amplitude: ")
    if a > "0" is False and a <= "9" is False:
        for i in range (0, 4):
            a = input("Your amplitude is less than zero, greater than nine, or is a string. Please enter another amplitude: ")
            print (a)
            if a > "0" and a <= "9":
                if float(a) > 0 is True:
                    break
            if i == 4:
                print("You did not input a valid amplitude. The amplitude has been defaulted to 1")
                a = 1
                break
    else:
        a = float(a)

    b = input("Enter a period length in pi radians: ")
    if b.isalpha() is True:
        for i in range (0, 5):
            b = input("Your period length is not a number. Please enter another period length: ")
            if b.isdigit() is True:
                break
            if i == 4:
                print("You did not input a valid period length. The period length has been defaulted to 2π")
                b = 2
                break
    if b[0] == "-":
        a = -1 * a
        b = b.replace("-", "")
    b = float(b)
    b = b*math.pi

    c = float(input("Enter a phase shift in pi radians: "))
    c = c*math.pi

    d = float(input("Enter a vertical shift in units: "))

def main():

    window = GraphWin("Baejoohyuned", 1920, 1000)
    line = linePt(960, 1000, 960, 0)
    line.setWidth(2)
    line.setOutline(color_rgb(0, 0, 0))
    line2 = linePt(0, 500, 1920, 500)
    line2.setWidth(2)
    line2.setOutline(color_rgb(0, 0, 0))
    line.draw(window)
    line2.draw(window)
    xCoord = math.degrees(-b)
    i = 960 - 3*math.degrees(b)
    i2 = 960 + 3*math.degrees(b)

    coefficient = 0

    for xCoordinate in range(960, 1920, 90):           #x axis hashmarks
        lineHash = linePt(xCoordinate, 520, xCoordinate, 480)
        lineHash.setWidth(2)
        lineHash.setOutline(color_rgb(0, 0, 0))
        lineHash.draw(window)

        if coefficient == 0:
            coefficient += 0.5
            continue
        else:
            shownText = Text(Point(xCoordinate, 550), (str(coefficient) + "π"))
            shownText.setSize(15)
            shownText.draw(window)
            coefficient += 0.5

    coefficient = 0

    for xCoordinate2 in range(960, 0, -90):           #x axis hashmarks
        lineHash2 = linePt(xCoordinate2, 520, xCoordinate2, 480)
        lineHash2.setWidth(2)
        lineHash2.setOutline(color_rgb(0, 0, 0))
        lineHash2.draw(window)
        if coefficient == 0:
            coefficient += 0.5
            continue
        else:
            shownText2 = Text(Point(xCoordinate2, 550), ("-" + str(coefficient) + "π"))
            shownText2.setSize(15)
            shownText2.draw(window)
            coefficient += 0.5

    yCoordCount = 0

    for yCoordinate in range(500, 1000, 101):           #y axis hashmarks
        lineHash3 = linePt(940, yCoordinate, 980, yCoordinate)
        lineHash3.setWidth(2)
        lineHash3.setOutline(color_rgb(0, 0, 0))
        lineHash3.draw(window)

        if yCoordCount == 0:
            yCoordCount += 1
            continue
        else:
            shownText3 = Text(Point(895, yCoordinate), "-" + str(yCoordCount) + " unit(s)")
            shownText3.setSize(15)
            shownText3.draw(window)
            yCoordCount += 1

    yCoordCount = 0

    for yCoordinate in range(500, 0, -100):           #y axis hashmarks
        lineHash4 = linePt(940, yCoordinate, 980, yCoordinate)
        lineHash4.setWidth(2)
        lineHash4.setOutline(color_rgb(0, 0, 0))
        lineHash4.draw(window)

        if yCoordCount == 0:
            yCoordCount += 1
            continue
        else:
            shownText4 = Text(Point(895, yCoordinate), str(yCoordCount) + " unit(s)")
            shownText4.setSize(15)
            shownText4.draw(window)
            yCoordCount += 1

    while True:
        angle = math.radians(xCoord)
        xCoord += 1
        if graphType == "sine":
            yCoord = sin(a, b, c, d, angle)
        else:
            yCoord = cos(a, b, c, d, angle)
        pt = Point(i, yCoord*100 + 500)
        pt.draw(window)
        time.sleep(0.001)
        if i > i2:
            break
        i += 1

    window.getMouse()
    window.close()

inputs()
main()


