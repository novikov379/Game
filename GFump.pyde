class player():
    def __init__(self):
        self.xpos = 135
        self.ypos = 475
        self.xvel = 0
        self.yvel = 0
        self.accel_g = 2
        self.colour = color(random(256), random(256), random(256))
        self.climb = 0
        self.score = 0
        
    def update(self, platforms):
        if (keyPressed and (keyCode == LEFT)):
            self.xpos -= 10
        elif (keyPressed and (keyCode == RIGHT)):
            self.xpos += 10
        
        self.yvel += self.accel_g
        
        for platform in platforms:
            if (((self.ypos >= platform.ypos-30) and (self.ypos <= platform.ypos+30) and (self.yvel >= 0)) and ((self.xpos >= platform.xpos-25) and (self.xpos <= platform.xpos+75+25))):
                self.ypos = platform.ypos-25
                self.yvel = -28
                
                if self.score/100 > 200:
                    if random(5) > 3:
                        platform.destroy()
                elif self.score/100 > 500:
                    platform.destroy()
        
        self.xpos += self.xvel
        self.ypos += self.yvel
        
        if self.xpos <= 0:
            self.xpos = (width+self.xpos)
        if self.xpos >= width:
            self.xpos = (self.xpos-width)
        
        if self.ypos < 300:
            self.climb = (300-self.ypos)
            self.ypos = 300
            for platform in platforms:
                platform.ypos += self.climb
                self.score += self.climb
            
        noStroke()
        #rect(self.xpos, self.ypos, 50, 50)
        translate(-30,-30)
        imageMode(CORNER)
        image(Mill, self.xpos, self.ypos, 50, 50)
        fill(0, 0, 0)
        textSize(30)
        text("Score: "+str(self.score/100), 50, 70)
        
        
class platform(object):
    def __init__(self, coords):
        self.xpos = coords[0]
        self.ypos = coords[1]
        self.colour = color(random(256), random(256), random(256))
        
    def display(self):
        strokeWeight(10)
        stroke(self.colour)
        line(self.xpos, self.ypos, self.xpos+75, self.ypos)
        
    def destroy(self):
        self.xpos = 600
        
        
def platform_manager(platforms):
    for p in platforms:
        if p.ypos > height:
            platforms.remove(p)
        else:
            pass
    while len(platforms) < 6:
        new_platform = platform([random(425), 700-(145*len(platforms))])
        platforms.append(new_platform)
        
        
def mousePressed():
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    loop()

def setup():
    size(500, 800)
    Mill=loadImage("1.png")
    BG=loadImage("forest1.jpg")
    KK=loadImage("TS.jpg")
    rectMode(CENTER)
    background(0, 255, 0)
    
    global platforms
    global Mill
    global BG
    global KK
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    
def draw():
    global Mill
    global BG
    global KK
    frameRate(30)
    imageMode(CORNER)
    image(BG, 0, 0, 500, 800)
    for platform in platforms:
        platform.display()
    p1.update(platforms)
    platform_manager(platforms)
    
    if p1.ypos > height+25:
        imageMode(CORNER)
        image(KK, 0, 0, 500, 800)
        fill(0, 255, 255)
        textAlign(CENTER, CENTER)
        textSize(80)
        text("GAME", width/2, 2*height/10)
        text("OVER", width/2, 3*height/10)
        textSize(40)
        text("Score: "+str(p1.score/100), width/2, 5*height/10)
        text("Retry: [CLICK]", width/2, 7*height/10)
        text("Exit: [ESC]", width/2, 8*height/10)
        textAlign(LEFT)
        noLoop()
