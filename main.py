import turtle
import math
import random


def make_pyramids(x=math.sqrt(50),y=3,z=40,fill=False):
    '''
    x = distance per shape on tower
    y = number of towers and shape of polygons
    z = number of shapes per tower
    fill = boolean that chooses whether or not to fill in the shapes'''
    def make_pyramid(n, painter):
        painter.speed(0) #so its not too slow
        
        for i in range (z):
            #moving for next shape
            painter.left(45)
            painter.right(45)
            painter.forward(x)
            colors = [ #color list
        "#FF5733", "#33FF57", "#3357FF", "#FFFF33", "#FF33FF", "#33FFFF",
        "#FF6347", "#4682B4", "#00FF00", "#FF00FF", "#00FFFF", "#FF4500",
        "#32CD32", "#FFD700", "#FF1493", "#1E90FF", "#00BFFF", "#FF8C00",
        "#6A5ACD", "#8A2BE2", "#5F9EA0", "#D2691E", "#FF7F50", "#6495ED",
        "#DC143C", "#00CED1", "#8B4513", "#FF0000", "#C71585", "#7FFF00",
        "#DDA0DD", "#FF00FF", "#FFD700", "#ADFF2F", "#FF6347", "#40E0D0",
        "#FF1493", "#B22222", "#DAA520", "#8B008B", "#FF4500", "#2E8B57",
        "#D2691E", "#FFB6C1", "#A52A2A", "#DEB887", "#5F9EA0", "#7FFF00",
        "#D2691E", "#DC143C", "#FF8C00", "#C71585", "#8B4513", "#FF6347",
        "#BDB76B", "#B0C4DE", "#D8BFD8", "#FF4500", "#00FF7F", "#FF6347",
        "#ADFF2F", "#FFD700", "#FF1493", "#8B0000", "#A9A9A9", "#006400",
        "#8B008B", "#FFD700", "#7CFC00", "#FF00FF", "#00FA9A", "#8A2BE2",
        "#D2691E", "#F5DEB3", "#D3D3D3", "#FFB6C1", "#C0C0C0", "#FF8C00",
        "#B22222", "#8B4513", "#FF00FF", "#FFD700", "#7CFC00", "#FF6347",
        "#FF1493", "#C71585", "#8A2BE2", "#D2691E", "#B0E57A", "#00FA9A",
        "#A9A9A9", "#7FFF00", "#DAA520", "#8B4513", "#B0C4DE", "#00CED1",
        "#8B008B", "#FF4500", "#C71585", "#FF6347", "#FF4500", "#2E8B57",
        "#8A2BE2", "#B22222", "#D2691E", "#FFB6C1", "#8B4513", "#DAA520"
    ]
            #chooses random color for the turtle
            kolor = random.choice(colors)
            painter.color(kolor)
            #if the parameters ask to fill the shape...
            if fill:
                painter.begin_fill()
            #uses for loop to draw that shape
            for j in range(y):
                painter.forward((i+1)*10)
                painter.right(360/y)
            #if parameters ask to fill the shape...
            if fill:
                painter.end_fill()
        painter.color("black")
        painter.penup()
        #end of pyramid
        painter.goto(0,0)
        painter.pendown()

    #setup for multiple pyramids
    for i in range(y):
        painter = turtle.Turtle()
        make_pyramid(50, painter)
        painter.left(360/y)


make_pyramids(1,4,50, False) #example setup - result will be in separate file
wn = turtle.Screen()
wn.mainloop()
