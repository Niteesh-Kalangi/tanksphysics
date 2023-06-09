import pygame, sys, pygame_widgets, math
from pygame.locals import QUIT
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button

b = 0
g = 9.8
m = 10
w = 0
currentPlayer = 0
gameState = 1
castle = pygame.image.load('assets/castle.png')
castle = pygame.transform.scale(castle, (200, int(int(castle.get_rect().height) * (200/int(castle.get_rect().width)))))
cannonImg = pygame.image.load('assets/cannon.png')
cannonImg = pygame.transform.scale(cannonImg, (80, int(int(cannonImg.get_rect().height) * (80/int(cannonImg.get_rect().width)))))
cannonballImg = pygame.image.load('assets/cannonball.png')
cannonballImg = pygame.transform.scale(cannonballImg, (20, int(int(cannonballImg.get_rect().height) * (20/int(cannonballImg.get_rect().width)))))



class Cannon:
  def __init__(self, health, xPos, yPos):
    self.health = health
    self.xPos = xPos
    self.yPos = yPos

  #def fire(angle, velocity):
    #ball = CannonBall(xPos, yPos, )

    
cannon1 = Cannon(3, 100, 700)
cannon2 = Cannon(3, 900, 700)
#cannonball class
class CannonBall:
  xPos = 0
  yPos = 0
  xVel = 0
  yVel = 0
  iniXVel = 0
  iniYVel = 0
  lastUpdate = 0
  
  def __init__(self, xPos, yPos, xVel, yVel):
    self.xPos = xPos
    self.yPos = yPos
    self.xVel = xVel
    self.yVel = yVel
    #self.iniXVel = iniXVel
    #self.iniYVel = iniYVel

  def updateVelocity(self, time):
    self.yVel = self.yVel + ((-m*g - b*(self.yVel**2))/m)*(time)
    if self.xVel < 0:
      self.xVel = self.xVel + ((w+ b*(self.xVel**2))/m)*(time)
    else:
      self.xVel = self.xVel + ((w - b*(self.xVel**2))/m)*(time)

  def updatePosition(self, time):
    self.xPos = self.xPos + self.xVel * (time) * 30
    self.yPos = self.yPos - self.yVel * (time) * 30

  def colliding(self):
    global castle
    global cannon1
    global cannon2

    castlex = 500 - castle.get_rect().width/2 
    castley = 700 - castle.get_rect().height
    print(cannon2.xPos)
    print(cannon2.yPos)
    print(self.xPos)
    print(self.yPos)
    if self.xPos > 1000 or self.xPos < 0 or self.yPos < -200:
      return 1
    if self.yPos > 750:
      yPos = 700
      return 2
    if self.xPos > castlex and self.xPos < castlex + castle.get_rect().width and self.yPos > castley and self.yPos < castley + castle.get_rect().height:
      print(castle.get_rect().center)
      print("castle collision")
      if currentPlayer % 2 == 0:
        xPos = 400
      else:
        xPos = 600
      return 3
    if currentPlayer % 2 == 0:
      if self.xPos > cannon2.xPos - cannonImg.get_rect().width/2 and self.yPos > cannon2.yPos and self.xPos < cannon2.xPos + cannonImg.get_rect().width + cannonImg.get_rect().width/2 and self.yPos < cannon2.yPos + cannonImg.get_rect().height:
        cannon2.health = cannon2.health - 1
        print("cannon1")
        return 4
    else:
      if self.xPos < cannon1.xPos + cannonImg.get_rect().width/2 and self.yPos > cannon1.yPos and self.xPos > cannon1.xPos - cannonImg.get_rect().width/2 and self.yPos < cannon1.yPos + cannonImg.get_rect().height:
        cannon1.health = cannon1.health - 1
        print("cannon")
        return 4
    return 0

    

  #def hitCannon(cannon):
    


    
  
ball = CannonBall(0,0,10.0,10.0)


""" for i in range(400):

  ball.updateVelocity(0.005)
  ball.updatePosition(0.005)
  #print(ball.xVel)
  #print(ball.xPos)
  #print(ball.yVel)
  print(ball.yPos) """


pygame.init()
clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Hello World!')


def drawCannon(health, xPos, yPos):
    if xPos > 500:
      cannon_flipped = pygame.transform.flip(cannonImg, True, False)
      DISPLAYSURF.blit(cannon_flipped, (xPos - cannon_flipped.get_rect().width/2, yPos))
    else:
      DISPLAYSURF.blit(cannonImg, (xPos - cannonImg.get_rect().width/2, yPos))

def drawBall(xPos, yPos):
  DISPLAYSURF.blit(cannonballImg, (xPos, yPos))

def fire(ball):
  
   global currentPlayer
   fire = True
   while fire:
      
      ball.updateVelocity(0.01)
      ball.updatePosition(0.01)
      pygame.time.wait(20)

      if ball.colliding() > 0:
        fire = False
        currentPlayer = currentPlayer + 1
      else:
        DISPLAYSURF.blit(cannonballImg, (ball.xPos, ball.yPos))
        repaint()
        pygame.display.update()

def repaint():
  color = (135, 206, 235)
  pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 0, 1000, 700))
  color = (0,200,0)
  pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 700, 1000, 300))
  drawCannon(cannon1.health, cannon1.xPos, cannon1.yPos)
  drawCannon(cannon2.health, cannon2.xPos, cannon2.yPos)
  drawBall(currentBall.xPos, currentBall.yPos)
  DISPLAYSURF.blit(castle, (DISPLAYSURF.get_width()/2 - castle.get_rect().width/2, 700 - castle.get_rect().height))



castle = pygame.image.load('assets/castle.png')
castle = pygame.transform.scale(castle, (200, int(int(castle.get_rect().height) * (200/int(castle.get_rect().width)))))
print(castle.get_rect().left)


rVelSlider = Slider(DISPLAYSURF, 50, 50, 200, 25, min=20, max = 60, step = 0.5)
rAngSlider = Slider(DISPLAYSURF, 50, 100, 200, 25, min = 1, max = 89, step = 1)
lVelSlider = Slider(DISPLAYSURF, 750, 50, 200, 25, min=20, max = 60, step = 0.5)
lAngSlider = Slider(DISPLAYSURF, 750, 100, 200, 25, min = 1, max = 89, step = 1)
c1Health = TextBox(DISPLAYSURF, cannon1.xPos + 25, cannon1.yPos + 40, 30, 25, fontSize = 20)
c2Health = TextBox(DISPLAYSURF, cannon2.xPos -50, cannon2.yPos + 40, 30, 25, fontSize = 20)
bSlider = Slider(DISPLAYSURF, 400, 300, 200, 25, min = 0, max = 1, step = 0.01)
gSlider = Slider(DISPLAYSURF, 400, 350, 200, 25, min = 5, max = 15, step = 0.5)
mSlider = Slider(DISPLAYSURF, 400, 400, 200, 25, min = 5, max = 20, step = 0.5)
wSlider = Slider(DISPLAYSURF, 400, 450, 200, 25, min = -20, max = 20, step = 0.01)
rVelOut = TextBox(DISPLAYSURF, 270, 50, 35, 25, fontSize = 20)
rAngOut = TextBox(DISPLAYSURF, 270, 100, 35, 25, fontSize = 20)
lVelOut = TextBox(DISPLAYSURF, 970, 50, 35, 25, fontSize = 20)
lAngOut = TextBox(DISPLAYSURF, 970, 100, 35, 25, fontSize = 20)
bOut = TextBox(DISPLAYSURF, 620, 300, 35, 25, fontSize = 20)
gOut = TextBox(DISPLAYSURF, 620, 350, 35, 25, fontSize = 20)
mOut = TextBox(DISPLAYSURF, 620, 400, 35, 25, fontSize = 20)
wOut = TextBox(DISPLAYSURF, 620, 450, 35, 25, fontSize = 20)
bLabel = TextBox(DISPLAYSURF, 300, 300, 50, 25, fontSize = 20)
gLabel = TextBox(DISPLAYSURF, 300, 350, 50, 25, fontSize = 20)
mLabel = TextBox(DISPLAYSURF, 300, 400, 50, 25, fontSize = 20)
wLabel = TextBox(DISPLAYSURF, 300, 450, 50, 25, fontSize = 20)
title = TextBox(DISPLAYSURF, 400, 200, 200, 75, fontSize = 65)
winner = TextBox(DISPLAYSURF, 400, 200, 200, 75, fontSize = 20)
title.setText("TANKS")
bLabel.setText("b")
gLabel.setText("g")
mLabel.setText("mass")
wLabel.setText("wind")
rVelOut.setText(rVelSlider.getValue())
rAngOut.setText(rAngSlider.getValue())
lVelOut.setText(lVelSlider.getValue())
lAngOut.setText(lAngSlider.getValue())
lVelSlider.hide()
lAngSlider.hide()
lVelOut.hide()
lAngOut.hide()
rVelSlider.hide()
rAngSlider.hide()
rVelOut.hide()
rAngOut.hide()
bLabel.hide()
gLabel.hide()
mLabel.hide()
wLabel.hide()
title.hide()
c1Health.hide()
c2Health.hide()
winner.hide()

def startGame():
  global m
  global b
  global g
  global w
  global gameState
  gameState = 2
  b = bSlider.getValue()
  g = gSlider.getValue()
  m = mSlider.getValue()
  w = wSlider.getValue()
  bSlider.hide()
  gSlider.hide()
  mSlider.hide()
  wSlider.hide()
  bOut.hide()
  gOut.hide()
  mOut.hide()
  wOut.hide()
  bLabel.hide()
  gLabel.hide()
  mLabel.hide()
  wLabel.hide()
  startButton.hide()
  title.hide()
  currentBall = CannonBall(cannon1.xPos + cannonImg.get_rect().width/2, cannon1.yPos, math.cos(math.radians(rAngSlider.getValue())) * rVelSlider.getValue(), math.sin(math.radians(rAngSlider.getValue())) * rVelSlider.getValue())

def restart():
  global gameState
  gameState = 1

def winScreen():
  pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 0, 1000, 800))
  lVelSlider.hide()
  lAngSlider.hide()
  lVelOut.hide()
  lAngOut.hide()
  rVelSlider.hide()
  rAngSlider.hide()
  rVelOut.hide()
  rAngOut.hide()
  bLabel.hide()
  gLabel.hide()
  mLabel.hide()
  wLabel.hide()
  title.hide()
  c1Health.hide()
  c2Health.hide()
  fireButton.hide()
  restartButton.show()
  winner.show()
  if cannon1.health <= 0:
    winner.setText("Player 2 Wins!")
  elif cannon2.health <= 0:
    winner.setText("Player 1 Wins!")

startButton = Button(DISPLAYSURF, 450, 500, 100, 50, text="START", onClick = lambda: startGame())
fireButton = Button(DISPLAYSURF, 450, 65, 100, 50, text="FIRE", onClick = lambda: fire(currentBall))
restartButton = Button(DISPLAYSURF, 450, 500, 100, 50, text="START", onClick = lambda: restart())
restartButton.hide()
fireButton.hide()


pygame.display.update()
while True:
    #print(cannon2.health)
    events = pygame.event.get()
    if gameState == 1:
        color = (255, 255, 255)
        pygame.draw.rect(DISPLAYSURF, color, pygame.Rect(0, 0, 1000, 800))
        fireButton.hide()
        lVelSlider.hide()
        lAngSlider.hide()
        lVelOut.hide()
        lAngOut.hide()
        rVelSlider.hide()
        rAngSlider.hide()
        rVelOut.hide()
        rAngOut.hide()
        bSlider.show()
        gSlider.show()
        mSlider.show()
        wSlider.show()
        bOut.show()
        gOut.show()
        mOut.show()
        wOut.show()
        bLabel.show()
        gLabel.show()
        mLabel.show()
        wLabel.show()
        title.show()
        bOut.setText(bSlider.getValue())
        gOut.setText(gSlider.getValue())
        mOut.setText(mSlider.getValue())
        wOut.setText(wSlider.getValue())
    elif gameState == 2:
      fireButton.show() 
      c1Health.show()
      c2Health.show() 
      if currentPlayer % 2 == 0:
        lVelSlider.hide()
        lAngSlider.hide()
        lVelOut.hide()
        lAngOut.hide()

        rVelSlider.show()
        rAngSlider.show()
        rVelOut.show()
        rAngOut.show()
        currentBall = CannonBall(cannon1.xPos + cannonImg.get_rect().width/2, cannon1.yPos, math.cos(math.radians(rAngSlider.getValue())) * rVelSlider.getValue(), math.sin(math.radians(rAngSlider.getValue())) * rVelSlider.getValue())
      else:
        rVelSlider.hide()
        rAngSlider.hide()
        rVelOut.hide()
        rAngOut.hide()

        lVelSlider.show()
        lAngSlider.show()
        lVelOut.show()
        lAngOut.show()
        currentBall = CannonBall(cannon2.xPos - cannonImg.get_rect().width/2, cannon2.yPos, -1 * math.cos(math.radians(lAngSlider.getValue())) * lVelSlider.getValue(), math.sin(math.radians(lAngSlider.getValue())) * lVelSlider.getValue())
        
      if cannon1.health <= 0 or cannon2.health <= 0:
        gameState = 3 
      repaint()
      pygame_widgets.update(events)
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
      rVelOut.setText(rVelSlider.getValue())
      rAngOut.setText(rAngSlider.getValue())
      lVelOut.setText(lVelSlider.getValue())
      lAngOut.setText(lAngSlider.getValue())
      c1Health.setText(cannon1.health)
      c2Health.setText(cannon2.health)
    elif gameState == 3:
      winScreen()
    pygame_widgets.update(events)
    pygame.display.update()

