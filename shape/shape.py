import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def circle(centerpoint=(0,0), radius=0.75):
    circle = plt.Circle(centerpoint, radius=radius, fc='y')
    plt.gca().add_patch(circle)

def rectangle(left_bottom_point=(10, 10), width=100, height=100):
    rectangle = plt.Rectangle(left_bottom_point, width, height, fc='r')
    plt.gca().add_patch(rectangle)
    
def line(point_x=(2, 8), point_y=(0, 6), line_width=2.5):
    line = plt.Line2D(point_x, point_y, lw=line_width)
    plt.gca().add_line(line)

def ellipse(xy=(157, 68), width=36, height=12, lw=2):
    ellipse = Ellipse(xy=xy, width=width, height=height, edgecolor='r', fc='None', lw=lw)
    plt.gca().add_patch(ellipse)


if __name__ == '__main__':
    plt.axes()
    #~ circle()
    #~ rectangle()
    #~ line()
    ellipse()
    plt.axis('scaled')
    plt.show()

