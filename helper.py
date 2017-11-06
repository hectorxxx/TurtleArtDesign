def polygon(bob, side, size, c):
    bob.color(c)
    angle = 360/side
    bob.begin_fill()
    for times in range(side):
        bob.forward(size)
        bob.right(angle)
    bob.end_fill()

def hexogon(bob, side, size, c):
    bob.color(c)
    angle = 360/side
    for times in range(side):
        bob.forward(size)
        bob.right(angle)
 
