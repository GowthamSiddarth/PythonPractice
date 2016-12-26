'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
'''
from math import sqrt


def getRobotDistance():
    dx, dy = 0, 0
    while True:
        ip = input().strip()
        if not ip:
            break
        else:
            lst = ip.split()
            direction, dist = lst[0], int(lst[1])
            if direction == "UP":
                dy += dist
            elif direction == "DOWN":
                dy -= dist
            elif direction == "LEFT":
                dx -= dist
            elif direction == "RIGHT":
                dx += dist
    return round(sqrt(dx * dx + dy * dy))


res = getRobotDistance()
print(res)
