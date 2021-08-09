import turtle
import time
import random

screen = turtle.Screen()
screen.title('Tetris by Magdalena Dhima')
screen.bgcolor('light pink')
screen.setup(width=500, height=900)
screen.tracer(0)

delay = 0.1

class Shape():
    def __init__(self):
        self.x = 5
        self.y = -2
        self.color = random.randint(1, 7)

        # Block Shape
        square = [[1,1],
                  [1,1]]

        horizontal_line = [[1,1,1,1]]

        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]

        left_l = [[1,0,0,0],
                  [1,1,1,1]]
                   
        right_l = [[0,0,0,1],
                   [1,1,1,1]]
                   
        left_s = [[1,1,0],
                  [0,1,1]]
                  
        right_s = [[0,1,1],
                   [1,1,0]]
                  
        t = [[0,1,0],
             [1,1,1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        # # Choose a random shape each time
        self.shape = random.choice(shapes)
        # self.shape = shapes[2]

        self.height = len(self.shape)
        self.width = len(self.shape[0])
        print(self.height, self.width)



    def move_left(self, grid):

        def find_width_at_Y(y):
                for x in range(shape.width):
                    if shape.shape[y][x] != 0:
                        return x

        # no need to worry about edge case
        # move right if not blocked
        # and if not off screen
        if self.x != 0:
            self.x -= 1

            for y in range(self.height):
                if self.y + y >= 0:
                    theWidth = find_width_at_Y(y)
                    for x in range(self.width):
                        if not (x != theWidth or grid[self.y + y][self.x + theWidth] == 0 or self.shape[y][x] == 0):
                            self.x += 1
                            return
    
            def moveShapeLeft():
                # draw the shape
                for y in range(self.height):
                    if self.y + y >= 0:
                        theWidth = find_width_at_Y(y)
                        for x in range(self.width):
                            if x != theWidth or grid[self.y + y][self.x + theWidth] == 0 or self.shape[y][x] == 0:
                                # checks the color in the dimensions of the shape
                                # print(str(shape.y + y) + "," + str(shape.x + x))
                                # print(grid)
                                # print(grid[self.y + y][self.x + x])
                                # print(x)
                                # print(self.shape[y][x])
                                if self.shape[y][x] != 0:
                                    grid[self.y + y][self.x + x] = self.color
                                else:
                                    if x > theWidth:
                                        grid[self.y + y][self.x + x] = 0
                                # erase part that is gone
                                if x == self.width -1 and shape.shape[y][x] != 0:
                                    grid[self.y + y][self.x + x + 1] = 0
                            else:
                                # print("AHH")
                                cantMove = True
                                crd = y
                                return cantMove, crd
                return False, 0

            cantMove, crd = moveShapeLeft()
            # print(cantMove)
            if cantMove:
                # print("JI")
                self.x += 1
                for y in range(self.height):
                    if self.y + y >= 0:
                        theWidth = find_width_at_Y(y)
                        for x in range(self.width):
                            if self.shape[y][x] != 0:
                                grid[self.y + y][self.x + x] = self.color
                            if x == theWidth and y < crd and self.shape[y][x] != 0 and grid[self.y + y][self.x + x -1] != 0 : 
                                grid[shape.y + y][shape.x + x -1] = 0

    def move_right(self, grid):

        def find_width_at_Y(y):
            for x in range(shape.width-1, -1, -1):
                if shape.shape[y][x] != 0:
                    return x

        # if edge case, don't right
        if self.x + self.width -1 != 11:
            self.x += 1

            for y in range(self.height):
                if self.y + y >= 0:
                    theWidth = find_width_at_Y(y)
                    for x in range(self.width):
                        if not (x != theWidth or grid[self.y + y][self.x + theWidth] == 0 or self.shape[y][x] == 0):
                            self.x -= 1
                            return

            # draw the shape
            def moveShapeRight():
                for y in range(self.height):
                    if self.y + y >= 0:
                        theWidth = find_width_at_Y(y)
                        for x in range(self.width):
                            # print(maxWidth)
                            # move right if not block
                            if x != theWidth or grid[self.y + y][self.x + theWidth] == 0 or self.shape[y][x] == 0:
                                # checks the color in the dimensions of the shape
                                # print(str(self.y + y) + "," + str(self.x + x))
                                # print(grid)
                                # print(grid[self.y + y][self.x + x])
                                # print(x)
                                # print(self.shape[y][x])
                                if self.shape[y][x] != 0:
                                    grid[self.y + y][self.x + x] = self.color
                                else:
                                    print("HETE")
                                    print(str(x) + " " + str(theWidth) )
                                    # print(grid)
                                    if x < theWidth:
                                        # print(grid)
                                        # print("then")
                                        grid[self.y + y][self.x + x] = 0
                                        # print(grid)
                                # erase part that is gone
                                if x == 0 and shape.shape[y][x] != 0: 
                                    grid[self.y + y][self.x + x -1] = 0
                            else:
                                cantMove = True
                                crd = y
                                return cantMove, x, y
                return False, 0, 0

            cantMove, x_stopped_at, y_stopped_at = moveShapeRight()
            if cantMove:
                print("ahh")
                self.x -= 1
                for y in range(self.height):
                    if self.y + y >= 0:
                        theWidth = find_width_at_Y(y)
                        for x in range(self.width):
                            if self.shape[y][x] != 0:
                                grid[self.y + y][self.x + x] = self.color

                            if x == theWidth and shape.shape[y][x] != 0 and grid[shape.y][shape.x + theWidth + 1] != 0:
                                if theWidth < shape.width -1:
                                    if y_stopped_at != y:
                                        grid[shape.y][shape.x + theWidth + 1] = 0

                                if y < y_stopped_at and x == x_stopped_at and grid[shape.y][shape.x + x + 1] != 0 and shape.shape[y][x] != 0:
                                    grid[shape.y][shape.x + x + 1] = 0

                        # if x == theWidth and y < crd and self.shape[y][x] != 0 and grid[self.y + y][self.x + x +1] != 0: 
                        #     grid[shape.y + y][shape.x + x +1] = 0

            # # if edge case was blocked, revert
            # if self.x == -1:
            #     self.x = 11

    def erase_shape(self, grid):
        for y in range(self.height):
            if shape.y + y >= 0:
                for x in range(self.width):
                    if(self.shape[y][x]==1):
                        grid[self.y + y][self.x + x] = 0

    def can_rotate(self, grid, shape):
        print(grid)
        for y in range(len(shape)):
            if self.y + y >= 0:
                for x in range(len(shape[0])):
                    print(shape)
                    print(str(self.y + y) + "," + str(self.x + x))
                    if shape[y][x] == 1 and grid[self.y + y][self.x + x] != 0:
                        return False
        return True

    def rotate(self, grid):
        # first erase the shape
        self.erase_shape(grid)
        rotated_shape = []
        for x in range(self.width):
            new_row = []
            for y in range(self.height-1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)

        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):  
            if self.can_rotate(grid, rotated_shape):
                self.shape = rotated_shape
                # Update the height and width
                self.height = len(self.shape)
                self.width = len(self.shape[0])
        # if self.can_rotate(grid, rotated_shape):
        #     self.shape = rotated_shape

        #     #   now update the height and width
        #     self.height = len(self.shape)
        #     self.width = len(self.shape[0])
        return



# create a list grid of zeros
grid = []
for _ in range(24):
    grid.append([0]*12)


# make visuals of squares with speed
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

def draw_grid(pen, grid):
    pen.clear()
    top = 240
    left= -110

    colors = ["orchid", "gold", "deep sky blue", "spring green", "dark slate blue", "orange", "deep pink", "red"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            colorNum = grid[y][x]
            color = colors[colorNum]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

def draw_score(pen, score):
    pen.color("blue")
    pen.hideturtle()
    pen.goto(-75, 350)
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))

    

# create the basic shape for the start of the game
shape = Shape()

# # put the shape in the grid
# for y in range(shape.height):
#     for x in range(shape.width):
#         if shape.shape[y][x] != 0:
#             grid[shape.y + y][shape.x + x] = shape.color
#         else:
#             grid[shape.y + y][shape.x + x] = 0

# # draw the initial grid
# draw_grid(pen, grid)

screen.listen()
screen.onkeypress(lambda: shape.move_left(grid), "a")
screen.onkeypress(lambda: shape.move_right(grid), "d")
screen.onkeypress(lambda: shape.rotate(grid), "space")


# set the score to zero
score = 0
draw_score(pen, score)

# main Gmae loop
while True:
    screen.update()
    # print(grid)

    cantMove = False

    # move the shape
    shape.y += 1

    def find_height_at_X(x):
        for y in range(shape.height-1, -1, -1):
            if shape.shape[y][x] != 0:
                return y

    # base floor checker
    if shape.y + shape.height -1 <= 23:
        def moveShape():
            for y in range(shape.height):
                if shape.y + y >= 0: 
                    for x in range(shape.width):
                        theHeight = find_height_at_X(x)
                        # Y_distance = shape.height - theHeight
                        if y != theHeight or grid[shape.y + theHeight][shape.x + x] == 0 or shape.shape[y][x] == 0:

                            # print(theHeight)
                            # print(grid)


                            if shape.shape[y][x] != 0:
                                grid[shape.y + y][shape.x + x] = shape.color
                            else:
                                if y < theHeight:
                                    grid[shape.y + y][shape.x + x] = 0

                            if y == 0 and shape.y + y - 1 >= 0 and shape.shape[y][x] != 0:
                                # print(grid)
                                # print("HI")
                                grid[shape.y + y - 1][shape.x + x] = 0
                                # print(grid)
                        else:
                            # print("ok " + str(y) + "," + str(x))
                            # print("so " + str(shape.y) + "," + str(shape.x))
                            # print(grid)
                            cantMove = True
                            # print(grid)
                            return cantMove, x, y

            return False, 0, 0
        # delay = 0.5
        cantMove, x_stopped_at, y_stopped_at = moveShape()
        if cantMove:
            time.sleep(1)
            # print("here")
            # print(grid)
            shape.y -= 1
            for y in range(shape.height):
                if shape.y + y >= 0:
                    for x in range(shape.width):
                        theHeight = find_height_at_X(x)
                        # makes sure it doesn't go off grid/to bottom

                        if shape.shape[y][x] != 0:
                            grid[shape.y + y][shape.x + x] = shape.color
                            # print(str(shape.y + y) + " " + str(shape.x + x))
                            # print("ok")
                            # print(str(shape.y + y) + " " + str(shape.x + x))
                        if y == theHeight and shape.shape[y][x] != 0 and grid[shape.y + theHeight +1][shape.x + x] != 0:
                            # print("Nice" + str(x) + " " + str(crd))
                            # print(str(shape.y + y + 1) + " " + str(shape.x + x))
                            if theHeight < shape.height -1:
                                if x_stopped_at != x:
                                    grid[shape.y + theHeight + 1][shape.x + x] = 0

                            if y == y_stopped_at and x < x_stopped_at and grid[shape.y + y +1][shape.x + x] != 0 and shape.shape[y][x] != 0:
                                grid[shape.y + y + 1][shape.x + x] = 0


                            # if y < theHeight and shape.shape[y][x] != 0 and grid[shape.y + y +1][shape.x + x] != 0:
                            #     grid[shape.y + y + 1][shape.x + x] = 0
                            # if y > theHeight and shape.shape[y][x] == 0 and grid[shape.y + y][shape.x + x] != 0:
                            #     print("oops")
                            #     print(str(shape.y + y) + " " + str(shape.x + x))
                            #     grid[shape.y + y ][shape.x + x] = 0

                # print(grid)

            if shape.y < 0:
                draw_score(pen, "Game is over!")
                break
                

            # print(grid)
            time.sleep(1)
            shape = Shape()
            # print("New Shape")
            # print(grid)

        # print(str(shape.y) + "," + str(shape.x))
        # print(grid)
    else:
        time.sleep(1)
        shape = Shape()
        # print("New Shape")

    # check if bottom row is full


    rows_to_clear = []
    for y in range(23, -1, -1):
        is_full = True
        for x in range(12):
            if grid[y][x] == 0:
                is_full = False
        if is_full:
            rows_to_clear.append(y)
        
    if len(rows_to_clear) != 0:
        score += 10 * len(rows_to_clear)
        for _ in range(len(rows_to_clear)):
            for new_y in range(rows_to_clear[len(rows_to_clear)-1]-1, -1, -1):
                for new_x in range(12):
                    grid[new_y+1][new_x] = grid[new_y][new_x]
                    # print(grid)

            rows_to_clear.pop()
    
    # draw the screen
    draw_grid(pen, grid)
    draw_score(pen, score)

    time.sleep(delay)
    
screen.mainloop()