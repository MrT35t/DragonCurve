#Program demonstrating L-Systems (Sierpinski's Triangle)
#B5 Programming 2
#1/9/24
#Mr. Test's version of a program provided by UVU CS1400
#See also wikipedia entry on L-Systems

import turtle
import random

def rule(char):
    """Accepts a character as a parameter and returns a string
    based on the application of a rule to that character"""
    if (char == "F"):
        return "FRG"
    elif (char == "G"):
        return "FLG"
    else:
        return char
    
def process(string):
    """Applies rule function to each character in a given string
    and returns a new string based on that rule application"""
    new_str = ""
    for c in string:
        new_str += rule(c)
    return new_str
    
    
def generate(itr, begin):
    """Processes begin parameter string through a given number
    of generations (itr) and returns the newly expanded string"""
    for x in range(itr):
        begin = process(begin)
    return begin

def draw_system(trt, instr, angle, dist):
    """Interprets a given instruction string by having the given
    turtle move forward the given distance or turn the given
    angle for each character in the string"""
    jitter_scale = 1
    for cmd in instr:
        jitter = random.randint(-2, 2) * jitter_scale
        if (cmd == "F" or cmd == "G"):
            trt.forward(dist + jitter)
        elif (cmd == "L"):
            trt.left(angle + jitter)
        elif (cmd == "R"):
            trt.right(angle + jitter)
            
def main():
    """Entry point for program--manages turtle and screen, generates
    instructions, and calls draw_system"""
    ANGLE = 90
    SIZE = 4
    GENS = 17
    instr = generate(GENS, "F")
    #print(instr)
    #turtle stuff
    root = turtle.Screen()
    berph = turtle.Turtle()
    root.screensize(2800, 2800, "sienna")
    root.setup(width = 718, height = 718)
    root.tracer(0)
    berph.color("dark goldenrod")
    berph.penup()
    berph.goto(359, -359)
    berph.setheading(180)
    berph.speed(0)
    berph.hideturtle()
    berph.pendown()
    draw_system(berph, instr, ANGLE, SIZE)
    root.update()
    root.exitonclick()
    
    
if __name__ == "__main__":
    main()
    
    
    