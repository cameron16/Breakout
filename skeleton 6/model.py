# model.py
# Cameron Boroumand cb596
"""Model module for Breakout

This module contains the model classes for the Breakout game. Instances of
Model storee the paddle, ball, and bricks.  The model has methods for resolving
collisions between the various game objects.  A lot of your of your work
on this assignment will be in this class.

This module also has an additional class for the ball.  You may wish to add
more classes (such as a Brick class) to add new features to the game.  What
you add is up to you."""
from constants import *
from game2d import *
import random # To randomly generate the ball velocity

class Model(object):
    """An instance is a single game of breakout.  The model keeps track of the
    state of the game.  It tracks the location of the ball, paddle, and bricks.
    It determines whether the player has won or lost the game.  
    
    To support the game, it has the following instance attributes:
    
        _bricks:  the bricks still remaining 
                  [list of GRectangle, can be empty]
        _paddle:  the paddle to play with 
                  [GRectangle, never None]
        _ball:    the ball 
                  [Ball, or None if waiting for a serve]
    
    As you can see, all of these attributes are hidden.  You may find that you
    want to access an attribute in call Breakout. It is okay if you do, but
    you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter and/or
    setter for any attribute that you need to access in Breakout.  Only add
    the getters and setters that you need.
                  
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER (TO CREATE PADDLES AND BRICKS)
    
    # ADD ANY ADDITIONAL METHODS (FULLY SPECIFIED) HERE

    def getBricks(self):
        """Returns: the list of GRectangle to draw the bricks for the game"""
        return self._bricks
        
    def getPaddle(self):
        """Returns: the paddle to play with in the game"""
        return self._paddle
    
    def getBall(self):
        """Returns: the ball to play with in the game"""
        return self._ball
    
    def getFakepaddle(self):
        return self._fakepaddle 
    
    def getSound(self):
        return self._sound
        
    
    
    def __init__(self):
        """Initializer: Sets up the game features including the bricks,
        paddle, and ball. The attribute _bricks is designed to store
        a list of bricks. The attribute _paddle stores the paddle object.
        The attribute _ball stores the ball."""
        
        self._bricks=self.create_brick()
        self._paddle=self.create_paddle()
        self._ball=Ball()
        self._sound=self.create_sound()
    
    
    def resetBall(self):
        """This method updates the position of the ball
        to the middle of the game screen"""
        self._ball.center_x=GAME_WIDTH/2
        self._ball.center_y=GAME_HEIGHT/2
    
    
    def resetpaddle(self):
        """This method updates the position of the paddle"""
        self._paddle.x=GAME_WIDTH/2-PADDLE_WIDTH/2
        self._paddle.y=PADDLE_OFFSET
    

    def create_brick(self):
        """Returns: a list of GRectangle. This function is used to create
        the bricks for the game. The colors of the bricks change between rows as you move
        down vertically in the following order: Red, Red, Orange, Orange, Yellow, Yellow,
        Green, Green, Cyan Cyan. If there are more than 10 rows, this sequence of color
        repeats itself"""
     
        k=[]
        xpos=-BRICK_SEP_H-BRICK_WIDTH+BRICK_SEP_H/2
        for x in range(BRICKS_IN_ROW):
            xpos=xpos+BRICK_SEP_H+BRICK_WIDTH
            ypos=GAME_HEIGHT-BRICK_Y_OFFSET+BRICK_SEP_V
            for y in range(BRICK_ROWS):
                ypos=ypos-BRICK_SEP_V-BRICK_HEIGHT
                if y > 9:
                    l=y/10
                    y=y-(10*(int(l)))
                if y==0 or y==1:
                    #brick=GImage(x=xpos,y=ypos,width=BRICK_WIDTH,height=8*BRICK_HEIGHT,source='MOTHER2.jpg')
                    brick=GRectangle(x=xpos,y=ypos,width=BRICK_WIDTH,height=BRICK_HEIGHT,fillcolor=colormodel.RED, linecolor=colormodel.RED)
                elif y==2 or y==3:
                    brick=GRectangle(x=xpos,y=ypos,width=BRICK_WIDTH,height=BRICK_HEIGHT,fillcolor=colormodel.ORANGE, linecolor=colormodel.ORANGE)
                elif y==4 or y==5:
                    brick=GRectangle(x=xpos,y=ypos,width=BRICK_WIDTH,height=BRICK_HEIGHT,fillcolor=colormodel.YELLOW, linecolor=colormodel.YELLOW)
                elif y==6 or y==7:
                    brick=GRectangle(x=xpos,y=ypos,width=BRICK_WIDTH,height=BRICK_HEIGHT,fillcolor=colormodel.GREEN, linecolor=colormodel.GREEN)
                elif y==8 or y==9:
                    #brick=GImage(x=xpos,y=ypos,width=BRICK_WIDTH,height=2*BRICK_HEIGHT,source='MOTHER2.jpg')
                    brick=GRectangle(x=xpos,y=ypos,width=BRICK_WIDTH,height=BRICK_HEIGHT,fillcolor=colormodel.CYAN, linecolor=colormodel.CYAN)
                k.append(brick)       
        return k
        

    def create_paddle(self):
        """Returns: the paddle object"""
        #return GImage(x=GAME_WIDTH/2-PADDLE_WIDTH/2,y=PADDLE_OFFSET,width=PADDLE_WIDTH, height=PADDLE_HEIGHT, source='FATHER.jpg')
        return GRectangle(x=GAME_WIDTH/2-PADDLE_WIDTH/2,y=PADDLE_OFFSET,width=PADDLE_WIDTH,height=PADDLE_HEIGHT,fillcolor=colormodel.RED)
    
    def create_sound(self):
        return Sound('saucer1.wav')
    
    
    #def create_fakepaddle(self):
     #   return GRectangle(x=GAME_WIDTH/2-PADDLE_WIDTH/2, y=PADDLE_OFFSET, width=GAME_WIDTH,height=GAME_HEIGHT)
 
    
    
    
    def move_ball(self):
        """Returns: Updated velocity of ball after a collision with a GObject.
        When the ball hits the top wall, it's velocity in the x-diretion remains unchanged
        but it's velocity in the y-direction is negated. When the ball hits a side wall,
        it's velocity in the y-direction remains unchanged but it's velocity in the
        x-diretion is negated. WHen the ball hits a brick, the velocity of the ball
        in the x-direction remains unchanged but it's velocity in the y-direction
        is negated. Also, the brick that the ball collided with is removed. When the ball
        collides with the paddle, the ball's velocity in the x-direction remains unchanged
        but it's velocity in the y-direction is negated"""
        
        self._ball.x=self._ball.x+self._ball._vx #velocity in x-direction
        self._ball.y=self._ball.y+self._ball._vy #velocity in y-direction
        if self._ball.x<=0:
            self._ball._vx=-self._ball._vx #velocity when hit left wall
        if self._ball.x>=GAME_WIDTH-BALL_DIAMETER:
            self._ball._vx=-self._ball._vx #velocity when hit right wall
        if self._ball.y>=GAME_HEIGHT-BALL_DIAMETER:
            self._ball._vy=-self._ball._vy #velocity when hit top wall
        if self._getCollidingObject()==self._paddle:
            if self._ball._vy<0:
                self._ball._vy=-self._ball._vy #velocity when hit paddle
        #if self._getCollidingObject()==self
        if self._getCollidingObject() in self._bricks:
            self._ball._vy=-self._ball._vy #velocity when hit brick
            self._bricks.remove(self._getCollidingObject()) #remove the brick
        #if self._ball.y<=0: ##These 2 lines of code are not necessary, but can be used
        ##to make possible different variations of the game (will keep for future use)
        #   self._ball._vy=-self._ball._vy #velocity when hit bottom wall
        

    def _getCollidingObject(self):
        """Returns: GObject that has collided with the ball
    
        This method checks the four corners of the ball, one at a 
        time. If one of these points collides with either the paddle 
        or a brick, it stops the checking immediately and returns the 
        object involved in the collision. It returns None if no 
        collision occurred."""
        
        if self._paddle.contains(self._ball.x,self._ball.y)==True:
            return self._paddle #paddle bottom left corner
        elif self._paddle.contains(self._ball.x+BALL_DIAMETER,self._ball.y)==True:
            return self._paddle #paddle bottom right corner
        for brick in range(len(self._bricks)):
            if self._bricks[brick].contains(self._ball.x, self._ball.y+BALL_DIAMETER)==True:
                return self._bricks[brick] #brick top left
            elif self._bricks[brick].contains(self._ball.x+BALL_DIAMETER, self._ball.y+BALL_DIAMETER)==True:
                return self._bricks #brick top right
            elif self._bricks[brick].contains(self._ball.x, self._ball.y)==True:
                return self._bricks #brick bottom left
            elif self._bricks[brick].contains(self._ball.x+BALL_DIAMETER, self._ball.y)==True:
                return self._bricks #brick bottom right
        return None
              
    
class Ball(GEllipse):
    """Instance is a game ball.
    
    We extends GEllipse because a ball in order to add attributes for a 
    velocity. This subclass adds these two attributes.
    
    INSTANCE ATTRIBUTES:
        _vx: Velocity in x direction [int or float]
        _vy: Velocity in y direction [int or float]
    
    The class Model will need to access the attributes. You will
    need getters and setters for these attributes.
    
    In addition to the getters and setter, you should add two
    methods to this class: an initializer to set the starting velocity 
    and a method to "move" the ball. The move method should adjust the 
    ball position according to the velocity.
    
    NOTE: The ball does not have to be a GEllipse. It could be an instance
    of GImage (why?). This change is allowed, but you must modify the class
    header up above.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """
    
    def getBall(self):
        """Returns the ball object"""
        return self
    
    
    def __init__(self):
        """Initializer: initializes the width and height of the ball to BALL_DIAMETER.
        The intializer creates the ball object and places it in the middle of the
        gaming screen. The ball's velocity in the y-direction is set to -5.0 and
        it is givine a random velocity in the x-direction"""
        
        width=BALL_DIAMETER
        height=BALL_DIAMETER
        ball=GEllipse.__init__(self, x=GAME_WIDTH/2-BALL_DIAMETER/2, y=GAME_HEIGHT/2-BALL_DIAMETER/2,width=BALL_DIAMETER ,height=BALL_DIAMETER,fillcolor=colormodel.RED)
        self._vy=-5.0
        self._vx = random.uniform(1.0,5.0) 
        self._vx = self._vx * random.choice([-1, 1])
    
   
    
    
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER TO SET VELOCITY
    
    # METHOD TO MOVE BALL BY PROPER VELOCITY
    
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


# ADD ANY ADDITIONAL CLASSES HERE