import random
from math import sqrt
from turtle import *

DEBUG = False
BRANCH_LENGTH = 60
SUN_RADIUS = 40
MAGIC = 12


class FloweringTree:
    def __init__(blossom):
        blossom.petal_count = 0
        blossom.petal_left_border = 0
        blossom.petal_right_border = 0
        blossom.turtle = Turtle()
        blossom.frame = Screen()
        if DEBUG:
            blossom.frame.tracer(0, 0)
        else:
            blossom.frame.tracer(3, 0)
        blossom.frame.bgcolor('tan')
        blossom.turtle.up()

    def tree(blossom, branch_len):
        if branch_len > 3:
            if 8 <= branch_len <= 12:
                if random.randint(0, 2) == 0:
                    blossom.turtle.color('snow')
                else:
                    blossom.turtle.color('lightcoral')
                blossom.turtle.pensize(branch_len / 3)
            elif branch_len < 8:
                blossom.petal_count += 1
                cur_x = blossom.turtle.pos()[0]
                if cur_x < 0:
                    blossom.petal_left_border = min(blossom.petal_left_border, cur_x)
                else:
                    blossom.petal_right_border = max(blossom.petal_right_border, cur_x)
                if random.randint(0, 1) == 0:
                    blossom.turtle.color('snow')
                else:
                    blossom.turtle.color('lightcoral')
                blossom.turtle.pensize(branch_len / 2)
            else:
                blossom.turtle.color('brown')
                blossom.turtle.pensize(branch_len / 10)

            # Draw the branch/leaf
            blossom.turtle.down()
            blossom.turtle.forward(branch_len)
            blossom.turtle.up()

            random_angle = 3 + 2 * MAGIC * random.random()
            random_length = MAGIC * random.random()

            blossom.turtle.right(random_angle)
            blossom.tree(branch_len - random_length)
            blossom.turtle.left(2 * random_angle)
            blossom.tree(branch_len - random_length)
            blossom.turtle.right(random_angle)

            # return to the root of this chile tree
            blossom.turtle.up()
            blossom.turtle.backward(branch_len)

    def petal_field(blossom, count, left_border=-100, right_border=100):
        middle = (right_border + left_border) / 2
        frame_width = (right_border - left_border) / 3
        depth = int(sqrt(frame_width))
        _start_pos = blossom.turtle.pos()
        start_pos = (middle, _start_pos[1] + depth / 2 - BRANCH_LENGTH / 10)
        blossom.turtle.goto(start_pos)

        for _ in range(count):
            random_width = frame_width - 2 * frame_width * random.random()
            random_depth = depth - 2 * depth * random.random()
            blossom.turtle.forward(random_depth)
            blossom.turtle.left(90)
            blossom.turtle.forward(random_width)
            blossom.turtle.down()
            if random.randint(0, 1) == 0:
                blossom.turtle.color("snow")
            else:
                blossom.turtle.color("crimson")
            rand_size = random.random()
            blossom.turtle.pensize(2.5 * rand_size)
            blossom.turtle.circle(rand_size)
            blossom.turtle.up()
            blossom.turtle.right(90)
            blossom.turtle.goto(start_pos)
        # Repaint the covered branch
        blossom.turtle.goto(_start_pos)
        blossom.turtle.color('sienna')
        blossom.turtle.pensize(BRANCH_LENGTH // 10)
        blossom.turtle.down()
        blossom.turtle.forward(BRANCH_LENGTH)
        blossom.turtle.up()

    def the_sun(blossom, radius=30):
        start_pos = blossom.turtle.pos()
        blossom.turtle.forward(500)
        blossom.turtle.left(90)
        blossom.turtle.forward(300)
        blossom.turtle.down()

        blossom.turtle.color('crimson')
        blossom.turtle.up()
        blossom.turtle.right(90)
        blossom.turtle.goto(start_pos)
    def signature(blossom):
        start_pos = blossom.turtle.pos()
        blossom.turtle.color('sienna')
        blossom.turtle.goto(start_pos)

    def draw(blossom):
        try:
            blossom.turtle.left(90)
            blossom.turtle.backward(250)
            blossom.the_sun(SUN_RADIUS)
            blossom.tree(BRANCH_LENGTH)
            blossom.petal_count = blossom.petal_count // (int(sqrt(2 * MAGIC)))
            blossom.petal_field(blossom.petal_count, blossom.petal_left_border, blossom.petal_right_border)
            blossom.turtle.backward(100)
            blossom.signature()
            blossom.turtle.color('tan')
            blossom.turtle.down()
            blossom.turtle.forward(20)
            blossom.frame.exitonclick()
        except KeyboardInterrupt:
            print('Interrupted!!')


if __name__ == '__main__':
    flowering_tree = FloweringTree()
    flowering_tree.draw()