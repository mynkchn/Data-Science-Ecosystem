import matplotlib.pyplot as plt

class Circle(object) :
    def __init__(self,radius,color):
        self.radius=radius
        self.color=color
    def add_radius(self,r):
        self.radius=r+self.radius
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0,0),radius=self.radius,fc=self.color))
        plt.axis('scaled')
        plt.show()

RedCircle=Circle(10,'red')
print(dir(RedCircle))
RedCircle.draw_circle()
print(RedCircle.radius)
print(RedCircle.color)
