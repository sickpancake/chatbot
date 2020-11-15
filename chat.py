import random
import turtle
import webbrowser

def initialize(t1):
    t1.reset()
    t1.clear()
    t1.penup()

def addition():
    addn1 = input("1st number")
    addn2 = input("2nd number")
    print(int(addn1) + int(addn2))

def subtraction():
    minusn1 = input("1st number")
    minusn2 = input("2nd number")
    print(int(minusn1) - int(minusn2))

def multiplication():
    timesn1 = input("1st number")
    timesn2 = input("2nd number")
    print(int(timesn1)*int(timesn2))

def division():
    dividen1 = input("1st number")
    dividen2 = input("2nd number")
    print(int(dividen1)/int(dividen2))

def opengoogle():
    webbrowser.open('http://google.co.kr', new=2)

def searchongoogle():
    webbrowser.open ('http://google.com/search?q=' + input('search?'))

def square(t1):
    initialize(t1)

    #faster
    t1.speed(8)

    #move(with out pen)
    t1.goto(-200,0)

    #make a square with "goto"
    t1.pendown()
    t1.goto(-200,-200)
    t1.goto(200,-200)
    t1.goto(200,200)
    t1.goto(-200,200)
    t1.goto(-200,0)
    t1.penup()
    t1.goto(0,0)

    #say "hi!"
    t1.write("hi!")

    #more "hi!"s
    for r1 in range(100):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        t1.goto(x, y)

        if y > 0:
            t1.write("hi!")
        else:
            t1.write("你好")


def circle(t1):
    initialize(t1)

    #slower
    t1.speed(0)

    #goto -200,0
    t1.goto(-200,0)

    #make circle
    t1.goto(-125,0)
    t1.pendown()
    t1.left(90)

    for r2 in range (1,362):
            t1.forward(3)
            t1.right(1)

    #say "let's learn python!"
    t1.penup()
    t1.goto(0,0)
    t1.pensize(10)
    t1.write("let's learn python!")
    t1.pensize(1)


def triangle(t1):
    initialize(t1)

    #goto
    t1.goto(-150,0)

    #make triangle
    t1.pendown()
    for r3 in range (3):
        t1.forward(300)
        t1.left(120)

def chat(t1):
    initialize(t1)

    math_cmd_dict = {
        "add": addition,
        "addition": addition,
        "minus": subtraction,
        "subtraction": subtraction,
        "times": multiplication,
        "multiplication": multiplication,
        "divide": division,
        "division": division,
    }

    browser_cmd_dict = {
        "o g": opengoogle,
        "open google": opengoogle,
        "search on google": searchongoogle,
        "sog": searchongoogle
    }

    t1_cmd_dict = {
        "sq": square,
        "square": square,
        "ci": circle,
        "circle": circle,
        "tr": triangle,
        "triangle": triangle,
        "cl": lambda t1: t1.clear(),
        "clear": lambda t1: t1.clear(),
        "00": lambda t1: t1.goto(0, 0),
        "pu": lambda t1: t1.penup(),
        "penup": lambda t1: t1.penup(),
        "pd": lambda t1: t1.pendown(),
        "pendown": lambda t1: t1.pendown(),
        
    }

    while True:
        cmd = input("what do you want to do?")
        
        if(cmd=="no" or cmd=="nothing"):
            print("ok")
            break

        if(cmd=="svg" or cmd=="suggest video game"):
            print("minecraft")    

        if(cmd=="fd" or cmd=="forward"):
            fd = input ("steps?")
            t1.forward(int(fd))

        if(cmd=="lt" or cmd=="left"):
            angle = input ("angle?")
            t1.left(int(angle))

        if(cmd=="rt" or cmd=="right"):
            angle = input ("angle")
            t1.right(int(angle))

        if(cmd=="bk" or cmd=="backward"):
            bk = input ("steps?")
            t1.backward(int(bk))

        if(cmd=="write" or cmd=="wr"):
            write = input ("what?")
            t1.write(write)

        if(cmd=="co" or cmd=="color"):
            color = input ("what color?")
            t1.color(color)

        if(cmd=="ps" or cmd=="pensize"):
            ps = input ("pick a size 1 to 10")
            t1.pensize(int(ps))

        if(cmd=="rn" or cmd=="random number"):
            rn = input (" first number?")
            rn2 = input (" 2nd number")
            r3 = random.randint(int(rn),int(rn2))
            print(r3)

        f = t1_cmd_dict.get(cmd, lambda *args: None)
        f(t1)

        m = math_cmd_dict.get(cmd, lambda *args: None)
        m()

        b = browser_cmd_dict.get(cmd, lambda *args: None)
        b()

if __name__ == "__main__":

    t1 = turtle.Turtle()
    chat(t1)
