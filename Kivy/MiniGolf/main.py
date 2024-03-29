'''
Version 1.0 
    Version Date 10/1/2021
        Initial build of the mini golf game
        
'''
from io import DEFAULT_BUFFER_SIZE
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.lang import Builder
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

#loading the kivy file
Builder.load_file('golf.kv')

#Creating the putter
class Putter(Widget):

    def putt (self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 *vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

#Creating the Golf ball class
class GolfBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


#Creating a class for the first hole.
#class Hole1(Widget):
   # pass

#Creating the Mini Golf Course. 
class GolfCourse(Widget):
    ball = ObjectProperty(None)
    player = ObjectProperty(None)

    #putting
    def putt_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))
    
    
    #golf ball movement
    def update(self, dt):
        self.ball.move()

        self.player.putt(self.ball)

        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player.center_y = touch.y



#Creating the Mini Golf App
class MiniGolf(App):
    def build(self):
        golf_course = GolfCourse()
        Clock.schedule_interval(golf_course.update, 1.0/60.0)
        golf_course.putt_ball()
        #hole_1 = Hole1()
        #golf_course.add_widget(hole_1)

        return golf_course

#Running the app
if __name__ == '__main__':
    MiniGolf().run()