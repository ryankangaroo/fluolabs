x = 0
y = 0
w  = 400
h = 400

def setup():
    size(600, 600, P3D)
    
def draw():
    global y
    background(0)
    noFill()
    
    stroke(255)
    
    
    translate(width/2, height/2)
    rotateX(PI/4)
    rect(-w/2, y, w, h)
    y = y- 1.0
 
