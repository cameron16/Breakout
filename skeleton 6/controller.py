# controller.py
# Cameron Boroumand cb596
"""Primary module for Breakout application

This module contains the controller class for the Breakout application.
There should not be any need for additional classes in this module.
If you need more classes, 99% of the time they belong in the model 
module. If you are ensure about where a new class should go, post a
question on Piazza."""
from constants import *
from game2d import *
from model import *


class Breakout(Game):
    """Instance is a Breakout Application
    
    This class extends Game and implements the various methods necessary 
    for running the game.
    
        Method init starts up the game.
        
        Method update updates the model objects (e.g. move ball, remove bricks)
        
        Method draw displays all of the models on the screen
    
    Because of some of the weird ways that Kivy works, you do not need to make
    an initializer __init__ for this class.  Any initialization should be done
    in the init method instead.
    
    Most of the work handling the game is actually provided in the class Model.
    Model should have a method called moveBall() that moves the ball and processes
    all of the game physics. This class should simply call that method in update().
    
    The primary purpose of this class is managing the game state: when is the 
    game started, paused, completed, etc. It keeps track of that in an attribute
    called _state.
    
    Instance Attributes:
        view:   the game view, used in drawing 
                [Immutable instance of GView, it is inherited from Game]
        _state: the current state of the game
                [one of STATE_INACTIVE, STATE_COUNTDOWN, STATE_PAUSED, 
                 STATE_ACTIVE, or STATE_COMPLETE]
        _model: the game model, which stored the paddle, ball, and bricks
                [GModel, or None if there is no game currently active
                 It is only None if _state is STATE_INACTIVE]
    
    You may have more attributes if you wish (you might need an attribute to store
    any text messages you display on the screen). If you add new attributes, they
    need to be documented here.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        _message: the message shown at the beginnig of the game. If _state
                  is STATE_INACTIVE, the message appears on the screen.
                  Once the _state is not STATE_INACTIVE, the welcome message
                  is dismissed from the screen and is no longer visible
        _time: keeps track of time after intial click. When in state countdown,
                the hidden _time attribute keepps track of the time passed
                after the click
        _lose: when the ball hits the bottom wall of the screen, the player loses a life
                and the hidden _lose attribute is incremented by 1.
                the player is allowed to lose 3 lives before the game ends.
                when the _lose attribute is equal to 3, the game is over and
                the game state is change to STATE_COMPLETE
        _clock: when the user lets go of the mouse after the ball hits the bottom wall,
                the hidden attribute _clock is set to -1"""
    # DO NOT MAKE A NEW INITIALIZER!
    
    # METHODS
    def init(self):
        """Initialize the game state.
        
        This method is distinct from the built-in initializer __init__.
        This method is called once the game is running. You should use
        it to initialize any game specific attributes.
        
        This method should initialize any state attributes as necessary 
        to statisfy invariants. When done, set the _state to STATE_INACTIVE
        and create a message saying that the user should press to play a game."""
        
        self._state=STATE_INACTIVE
        self._message=GLabel(text='Welcome to Cornell\'s Breakout', font_size=34, linecolor=colormodel.RED, valign='bottom', y=300)
        self._message101=GLabel(text='Click to Play', font_size=34, linecolor=colormodel.BLUE, valign='bottom', y=200, x=135)
        self._message102=GLabel(text='Abandon hope all ye who enter here', font_size=28, linecolor=colormodel.RED, valign='bottom', y=400, x=10)

        if self._state!=STATE_INACTIVE:
            self._message=None
        self._model=None
        self._time=180
        self._lose=0
        self._clock=0
        self._restartmethod=0
        self._score=0

    def update(self,dt):
        """Animate a single frame in the game.
        
        It is the method that does most of the work. Of course, it should
        rely on helper methods in order to keep the method short and easy
        to read.  Some of the helper methods belong in this class, and
        others belong in class Model.
        
        The first thing this method should do is to check the state of the
        game. We recommend that you have a helper method for every single
        state: STATE_INACTIVE, STATE_COUNTDOWN, STATE_PAUSED, STATE_ACTIVE.
        The game does different things in each state.
        
        In STATE_INACTIVE, the method checks to see if the player clicks
        the mouse. If so, it starts the game and switches to STATE_COUNTDOWN.

        STATE_PAUSED is similar to STATE_INACTIVE. However, instead of 
        restarting the game, it simply switches to STATE_COUNTDOWN.
        
        In STATE_COUNTDOWN, the game counts down until the ball is served.
        The player is allowed to move the paddle, but there is no ball.
        This state should delay at least one second.
        
        In STATE_ACTIVE, the game plays normally.  The player can move the
        paddle and the ball moves on its own about the board.  Both of these
        should be handled by methods inside of class Model (not in the class).
        Model should have methods named movePaddle and moveBall.
        
        While in STATE_ACTIVE, if the ball goes off the screen and there
        are tries left, it switches to STATE_PAUSED.  If the ball is lost 
        with no tries left, or there are no bricks left on the screen, the
        game is over and it switches to STATE_INACTIVE.
        
        While in STATE_COMPLETE, this method does nothing.
        
        You are allowed to add more states if you wish. Should you do so,
        you should describe them here.
        
        Precondition: dt is the time since last update (a float).  This
        parameter can be safely ignored. It is only relevant for debugging
        if your game is running really slowly."""
    
        
        self.state_inactive()
        self.state_countdown()
        self.state_active()
        self.state_paused()
        self.state_complete()
        #if self.view.touch!=None and self._state==STATE_INACTIVE:
         #  self._state=STATE_COUNTDOWN
        #if self._state==STATE_COUNTDOWN: 
        #    self.counting_down(self)   
        #if self._state!=STATE_INACTIVE and self._model==None:
        #    self._model=Model()
        #if self._state==STATE_COUNTDOWN or self._state==STATE_ACTIVE:
         #   self.paddle_move(self)
        #if self._state==STATE_ACTIVE:
        #    self._model.move_ball()
        #    self._model._getCollidingObject()
        #if self._state==STATE_ACTIVE and self._model._ball.y<=0 and self._lose==0:
        #    self._state=STATE_PAUSED
        #    self._message2=GLabel(text='Click To Try Again', font_size=30, linecolor=colormodel.CYAN, valign='bottom', y=200, x=125)
        #    self._message44=GLabel(text='Nice Try. You Have 2 More Lives', font_size=30, linecolor=colormodel.GREEN, valign='bottom', y=300, x=27)
        #    self._messageNIET=GLabel(text='That which does not kill us makes us stronger', font_size=23, linecolor=colormodel.RED, valign='bottom', y=100, x=5)
        #    self._lose=self._lose+1    
        #if self._state==STATE_PAUSED:
        #    x=0
        #    self._model.resetBall()
        #    self._model.resetpaddle()
        #    self.counting_forpause(self, x)
        #    if self._clock==-1 and self.view.touch!=None:
        #        self._state=STATE_COUNTDOWN
        #        self._clock=0
        if self._state==STATE_ACTIVE and self._model._ball.y<=0 and self._lose==1:
            self._lose=self._lose+1
            self._message3=GLabel(text='Nice Try. You Have 1 More Life', font_size=30, linecolor=colormodel.GREEN, valign='bottom', y=300, x=32)
            self._message4=GLabel(text='Click To Try Again', font_size=30, linecolor=colormodel.CYAN, valign='bottom', y=200, x=125)
            self._state=STATE_PAUSED
        if self._state==STATE_ACTIVE and self._model._ball.y<=0 and self._lose==2:
            x=55
            self._lose=self._lose+1
            self._state=STATE_COMPLETE
            #self.counting_forpause(self, x)
            self._messageplayagain=GLabel(text='Click to play again', font_size=23, linecolor=colormodel.RED, valign='bottom', y=500, x=155)
            self._message5=GLabel(text='Woah, you really stink', font_size=30, linecolor=colormodel.GREEN, valign='bottom', y=200, x=90)
            self._message6=GLabel(text='YOU LOSE', font_size=30, linecolor=colormodel.CYAN, valign='bottom', y=250, x=175)
            self._message7=GLabel(text='GAME OVER', font_size=30, linecolor=colormodel.RED, valign='bottom', y=300, x=160)
        if self._state==STATE_ACTIVE and len(self._model._bricks)==0:
            x=33
            self._state=STATE_COMPLETE
            #self.counting_forpause(self,x)
            self._messageplayagain=GLabel(text='Click to play again', font_size=23, linecolor=colormodel.RED, valign='bottom', y=500, x=155)
            self._message8=GLabel(text='CONGRATULATIONS YOU WIN', font_size=30, linecolor=colormodel.RED, valign='bottom', y=425, x=44)
            self._message9=GLabel(text='Woah, you smell good', font_size=30, linecolor=colormodel.RED, valign='bottom', y=325, x=90)
            self._messageCAES=GLabel(text='I Came, I Saw, I Conquered', font_size=30, linecolor=colormodel.CYAN, valign='bottom', y=225, x=66)
            
       
    def state_inactive(self):
        if self.view.touch!=None and self._state==STATE_INACTIVE:
           self._state=STATE_COUNTDOWN 
        if self._state!=STATE_INACTIVE and self._model==None:
           self._model=Model()
    
    def state_countdown(self):
        if self._state==STATE_COUNTDOWN: 
            self.counting_down(self)
            self.paddle_move(self)
            bouncesound=Sound('saucer2.wav')
            if self._time<=180:
                bouncesound.play(loops=2)
            #if self._time==180 or self._time>=165:
            #    bouncesound.play()
            #if self._time<=125 or self._time>=115:
            #    bouncesound.play()
            #if self._time<=70 or self._time>=60:
            #    bouncesound.play()
            ##if self._time<=180 or self._time>120:
            #    bouncesound.play()
            #if self._time<=150 or self._time>=60:
            #    bouncesound.play()
            #if self._time<130:
            #    bouncesound.play()
            #self.countdown_timer3(self)
            #self.countdown_timer2(self)
            #self.countdown_timer1(self)
    
    def state_active(self):
        if self._state==STATE_ACTIVE:
            self.keep_score(self)
            self.paddle_move(self)
            self._model.move_ball()
            self._model._getCollidingObject()
            if self._model._ball.y<=0 and self._lose==0:
                self._state=STATE_PAUSED
                self._message2=GLabel(text='Click To Try Again', font_size=30, linecolor=colormodel.CYAN, valign='bottom', y=200, x=125)
                self._message44=GLabel(text='Nice Try. You Have 2 More Lives', font_size=30, linecolor=colormodel.GREEN, valign='bottom', y=300, x=27)
                self._messageNIET=GLabel(text='That which does not kill us makes us stronger', font_size=23, linecolor=colormodel.RED, valign='bottom', y=100, x=5)
                self._lose=self._lose+1    
        #if self._state==STATE_ACTIVE and self._model._ball.y<=0 and self._lose==1:
        #    self._lose=self._lose+1
        #    self._message3=GLabel(text='Nice Try. You Have 1 More Life', font_size=30, linecolor=colormodel.GREEN, valign='bottom', y=300, x=32)
        #    self._message4=GLabel(text='Click To Try Again', font_size=30, linecolor=colormodel.CYAN, valign='bottom', y=200, x=125)
        #    self._state=STATE_PAUSED
        #
        #
    def state_paused(self):
        if self._state==STATE_PAUSED:
            x=0
            self._model.resetBall()
            self._model.resetpaddle()
            self.counting_forpause(self, x)
            if self._clock==-1 and self.view.touch!=None:
                self._state=STATE_COUNTDOWN
                self._clock=0
    
    def state_complete(self):
        if self._state==STATE_COMPLETE:
            x=0
            self.counting_forpause(self, x)
            if self._clock==-1 and self.view.touch!=None:
                #self._state=STATE_INACTIVE
                #
                #if self._state!=STATE_INACTIVE:
                #    self._message=None
                self._model.resetBall()
                self._model.resetpaddle()
                self._model=Model()
                self._state=STATE_COUNTDOWN
                self._time=180
                self._lose=0
                self._clock=0
                
        #if self._state==STATE_COMPLETE and self.view.touch!=None:
        #    self._state=STATE_INACTIVE
        #    x=0
        #    self.counting_forpause(self, x)
        #    self._model=Model()
        #    self._message=GLabel(text='Welcome to Cornell\'s Breakout', font_size=34, linecolor=colormodel.RED, valign='bottom', y=300)
        #    self._message101=GLabel(text='Click to Play', font_size=34, linecolor=colormodel.BLUE, valign='bottom', y=200, x=135)
        #    self._message102=GLabel(text='Abandon hope all ye who enter here', font_size=28, linecolor=colormodel.RED, valign='bottom', y=400, x=10)

        
    def draw(self):
        """Draws the game objects to the view.
        
        Every single thing you want to draw in this game is a GObject. 
        To draw a GObject g, simply use the method g.draw(view).  It is 
        that easy!
        
        Many of the GObjects (such as the paddle, ball, and bricks) are
        attributes in Model. In order to draw them, you either need to
        add getters for these attributes or you need to add a draw method
        to class Model.  Which one you do is up to you."""
        
        if self._state==STATE_INACTIVE:
            self._message.draw(self.view)
            self._message101.draw(self.view)
            self._message102.draw(self.view)
        if self._state!=STATE_INACTIVE:
            for x in range((len(self._model._bricks))):
                self._model._bricks[x].draw(self.view)
        if self._model!=None and self._model._paddle!=None:
            self._model._paddle.draw(self.view)
        if self._state==STATE_COUNTDOWN or self._state==STATE_ACTIVE:
            self._model._ball.draw(self.view)
        if self._state==STATE_PAUSED and self._lose==1:
            self._message44.draw(self.view)
            self._message2.draw(self.view)
            self._messageNIET.draw(self.view)
        if self._state==STATE_PAUSED and self._lose==2:
            self._message3.draw(self.view)
            self._message4.draw(self.view)
        if self._state==STATE_COMPLETE and self._lose==3:
            self._message5.draw(self.view)
            self._message6.draw(self.view)
            self._message7.draw(self.view)
        if self._state==STATE_COMPLETE and self._lose!=3:
            self._message8.draw(self.view)
            self._message9.draw(self.view)
            self._messageCAES.draw(self.view)
        
        if self._state==STATE_COUNTDOWN and self._time<=180 and self._time>120:
            self._messagethree.draw(self.view)
            #bouncesound=Sound('bounce.wav')
        if self._state==STATE_COUNTDOWN and self._time<=120 and self._time>60: 
            self._messagetwo.draw(self.view)
        if self._state==STATE_COUNTDOWN and self._time<=60 and self._time>0:
            self._messageone.draw(self.view)
        
        if self._state==STATE_COMPLETE:
           self._messageplayagain.draw(self.view)
        
        
    
    def paddle_move(self, x):
        """This method updates the position of the paddle. By clicking on the paddle
        and dragging it, the user can move the paddle across the screen. The paddle
        cannot be dragged by clicking outside of the paddle. The user must click inside
        of the paddle to move it"""
        
        if self.view.touch!=None:
            if self._model._paddle.contains(self.view.touch.x,self.view.touch.y)==True:
                self._model._paddle.center_x=self.view.touch.x
        if self._model._paddle.center_x+(PADDLE_WIDTH/2)>=GAME_WIDTH:
            self._model._paddle.center_x=GAME_WIDTH-PADDLE_WIDTH/2
        if self._model._paddle.center_x-(PADDLE_WIDTH/2)<=0:
            self._model._paddle.center_x=PADDLE_WIDTH/2
                
            
    def counting_down(self, time):
        """This method counts down to 3 seconds for the ball to serve so the
        user has ample time to set him/herself up to play the game."""
        #if self.view.touch!=None and self._state==STATE_COUNTDOWN:
        self._time=self._time-1
        if self._time<=180:
            self._messagethree=GLabel(text='3', font_size=50, linecolor=colormodel.CYAN, valign='bottom', y=340, x=GAME_WIDTH/2-15)
            self._messagetwo=GLabel(text='2', font_size=50, linecolor=colormodel.CYAN, valign='bottom', y=250, x=GAME_WIDTH/2-15)
            self._messageone=GLabel(text='1', font_size=50, linecolor=colormodel.CYAN, valign='bottom', y=160, x=GAME_WIDTH/2-18)
        if self._time==0:
            self._state=STATE_ACTIVE
        if self._time==-1:
            self._time=180
    
    
    
    #def countdown_timer3(self, time):
    #    self._messagethree=GLabel(text='3', font_size=50, linecolor=colormodel.CYAN, valign='bottom', y=200, x=GAME_WIDTH/2)
    #    self._time=60
    #    self._time=self._time-1
    #    if self._time==0:
    #        self._message=None
    #
    #def countdown_timer2(self, time):
    #    self._messagetwo=GLabel(text='2', font_size=50, linecolor=colormodel.CYAN, valign='bottom', y=200, x=125)
    #    self._time=60
    #    self._time=self._time-1
    #    if self._time==0:
    #        self._message=None
    #
    #def countdown_timer1(self, time):
    #    self._messageone=GLabel(text='1', font_size=50, linecolor=colormodel.CYAN, valign='bottom', y=200, x=125)
    #    self._time=60
    #    self._time=self._time-1
    #    if self._time==0:
    #        self._message=None
    #
            
    
    
    
    def counting_forpause(self, time, clock):
        """This method makes sure that the game state does not go
        straight from STATE_PAUSE to STATE_COUNTDOWN when the user loses.
        When the ball initially hits the bottom wall, the user is likely to be
        pressing down on the mouse. This method gives the user
        a few seconds to let go of the mouse so the game does not go
        straight to STATE_COUNTDOWN unexpectedly. This way, the user
        can see the messages shown during STATE_PAUSE and prepare for a
        new round of breakdown!. """
        if self.view.touch!=None:
            self._time=self._time-1
        if self._time==-360:
            self._state=STATE_ACTIVE
        if self.view.touch==None:
            self._time=180
            self._clock=-1
        
        
    
    def keep_score(self, score):
              
        if self._model._getCollidingObject()==self._model._bricks:
            self._score=self._score+1
            print self._score
                
        #for some reason... only does the if statement sometimes???
    
   
        
    
        
    
            
        

        
        
    
    
            