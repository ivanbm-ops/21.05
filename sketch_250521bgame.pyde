shar_x=100
shar_y=100
shar_dx=1
shar_dy=2
ladder_x=200
x=0
def setup():
    size(600,600)
def draw():
    global shar_x,shar_y,shar_dx,shar_dy,ladder_x,x
    background(200)
    textSize(20)
    fill(255,160,239)
    text(x,50,50)
    fill(255)
    rect(ladder_x,550,100,20)
    fill(66,250,224)
    ellipse(shar_x,shar_y,50,50)
    shar_x = shar_x + shar_dx   
    shar_y = shar_y + shar_dy   
    if shar_x > 580:      
        shar_dx = -shar_dx  
    if shar_x < 20:    
        shar_dx = -shar_dx
    if shar_y < 20:
          shar_dy = -shar_dy
    if shar_y > 580:
        textSize(20)
        fill(235,124,13)
        text("loss",300,300)
    if keyPressed and key == CODED: 
        if keyCode == LEFT:     
            ladder_x = ladder_x - 4   
        if keyCode == RIGHT:  
            ladder_x = ladder_x + 4
    if collideRectCircle(ladder_x, 550,100,20,shar_x,shar_y,50): 
        x=x+1 
        shar_dy = -random(4,6)      
        shar_dx = random(-5, 5)
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):
    radius = diameter / 2
    testX = cx
    testY = cy

    if cx < rx:
        testX = rx
    elif cx > rx + rw:
        testX = rx + rw

    if cy < ry:
        testY = ry
    elif cy > ry + rh:
        testY = ry + rh

    distX = cx - testX
    distY = cy - testY
    distance = sqrt((distX * distX) + (distY * distY))

    return distance <= radius   
