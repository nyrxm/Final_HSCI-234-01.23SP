import js
p5 = js.window

p5.imageMode(p5.CENTER)
Enemy_S_img = p5.loadImage('Enemy_S.png');
Enemy_M_img = p5.loadImage('Enemy_M.png');
Enemy_L_img = p5.loadImage('Enemy_L.png');
Player_img = p5.loadImage('Player.png');
BG_img = p5.loadImage('Space_BG.png');
Start_Menu_img = p5.loadImage('Start_Menu.png');
font = p5.loadFont('ethnocentric rg.otf');

class Object:
    def __init__(self, x = 150, y = 250):
        self.x = x  
        self.y = y

class Enemy(Object):
    def __init__(self, x = 270, y = 140):
        self.img = Enemy_S_img
        self.x = x  
        self.y = y
        self.timer = p5.millis()
        self.speed = 2
        self.width = self.img.width
        self.height = self.img.height

    def update(self):
        self.x -= self.speed
        if(self.x < 0):
            self.y = p5.random(15, 270)
            self.x = p5.random(280, 500)
        if(self.speed < 11):
            if(p5.millis() > self.timer + 7000):
                self.speed += 1
                self.timer = p5.millis()

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop()

class Enemy_S_1(Enemy):
    pass
class Enemy_S_2(Enemy):
    pass
class Enemy_S_3(Enemy):
    pass
class Enemy_M_1(Enemy):
    def __init__(self, x = 1150, y = 70):
        self.img = Enemy_M_img
        self.x = x  
        self.y = y
        self.timer = p5.millis()
        self.speed = 1
        self.width = self.img.width
        self.height = self.img.height
        
    def update(self):
        self.x -= self.speed
        if(self.x < 0):
            self.y = p5.random(15, 270)
            self.x = p5.random(280, 630)
        if(self.speed < 5):
            if(p5.millis() > self.timer + 10000):
                self.speed += 1
                self.timer = p5.millis()

    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop()

class Enemy_M_2(Enemy_M_1):
    pass

class Enemy_L_1(Enemy):
    def __init__(self, x = 2550, y = 70):
        self.img = Enemy_L_img
        self.x = x  
        self.y = y
        self.timer = p5.millis()
        self.speed = 1
        self.width = self.img.width
        self.height = self.img.height
        
    def update(self):
        self.x -= self.speed
        if(self.x < 0):
            self.y = p5.random(15, 270)
            self.x = p5.random(600, 1600)
        if(self.speed < 3):
            if(p5.millis() > self.timer + 25000):
                self.speed += 1
                self.timer = p5.millis()
    
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop() 

class Player(Object): 
    def __init__(self):
        self.img = p5.loadImage('Player.png')
        self.x = 20
        self.y = 150
        self.width = self.img.width
        self.height = self.img.height
    
    def draw(self):
        p5.push()
        p5.translate(self.x, self.y)
        p5.image(self.img, 0, 0)
        p5.pop()
    

player = Player()
enemy_s_1 = Enemy_S_1()
enemy_s_2 = Enemy_S_2()
enemy_s_3 = Enemy_S_3()
enemy_m_1 = Enemy_M_1()
enemy_m_2 = Enemy_M_2()
enemy_l_1 = Enemy_L_1()
program_state = 'START'
score = 0
timer_ms = 0

def setup():
    p5.createCanvas(300, 300) 
    print('finished setup') 
    
def draw():
    p5.background(255)
    msec = p5.millis()
    global timer_ms
    global program_state
    global score
    if(program_state == 'START'):
        p5.image(BG_img, 150, 150)
        p5.image(Start_Menu_img, 150, 210)
        p5.textFont(font)
        p5.fill(255)
        p5.textSize(12)
        p5.text('click to start game', 50, 50)
    elif(program_state == 'PLAY'):
        p5.image(BG_img, 150, 150)
        p5.text('score: ' + str(score), 25, 25)
        enemy_s_1.update()
        enemy_s_1.draw()
        enemy_s_2.update()
        enemy_s_2.draw()
        enemy_s_3.update()
        enemy_s_3.draw()
        enemy_m_1.update()
        enemy_m_1.draw()
        enemy_m_2.update()
        enemy_m_2.draw()
        enemy_l_1.update()
        enemy_l_1.draw()
        if(p5.keyIsPressed == True):
            if(p5.keyCode == p5.RIGHT_ARROW):
                if(player.x < p5.width - player.width/2):
                    player.x += 3
            elif(p5.keyCode == p5.LEFT_ARROW):
                if(player.x > player.width/2):
                    player.x -= 3
            elif(p5.keyCode == p5.UP_ARROW):
                if(player.y > player.height/2):
                    player.y -= 3
            elif(p5.keyCode == p5.DOWN_ARROW):
                if(player.y < p5.height - player.height/2):
                    player.y += 3
        player.draw()
        d_1 = p5.dist(player.x, player.y, enemy_s_1.x, enemy_s_1.y)
        d_2 = p5.dist(player.x, player.y, enemy_s_2.x, enemy_s_2.y)
        d_3 = p5.dist(player.x, player.y, enemy_s_3.x, enemy_s_3.y)
        d_4 = p5.dist(player.x, player.y, enemy_m_1.x, enemy_m_1.y)
        d_5 = p5.dist(player.x, player.y, enemy_m_2.x, enemy_m_2.y)
        d_6 = p5.dist(player.x, player.y, enemy_l_1.x, enemy_l_1.y)
        if(d_1 < 18) or (d_2 < 18) or (d_3 < 18) or (d_4 < 32) or (d_5 < 32) or (d_6 < 45):
            program_state = 'LOOSE'
            score = 0
        if(score < 100):
            if(p5.millis() > timer_ms + 2000):
                score += 1
                timer_ms = p5.millis()
        if(score == 100):
            program_state = 'WIN'
            score = 0
    elif(program_state == 'WIN'):
        p5.image(BG_img, 150, 150)
        p5.textSize(24)
        p5.text('You Win!!', 50, 150)
        p5.textSize(8)
        p5.text('click to restart game', 80, 260)
    elif(program_state == 'LOOSE'):
        p5.image(BG_img, 150, 150)
        p5.textSize(24)
        p5.text('You Loose...', 45, 150)
        p5.textSize(8)
        p5.text('click to restart game', 80, 260)
    if(program_state == 'WIN') or (program_state == 'LOOSE'):
        player.x = 20
        player.y = 150
        enemy_s_1.x = 270
        enemy_s_1.y = 140
        enemy_s_1.speed = 2
        enemy_s_2.x = 270
        enemy_s_2.y = 140
        enemy_s_2.speed = 2
        enemy_s_3.x = 270
        enemy_s_3.y = 140
        enemy_s_3.speed = 2
        enemy_m_1.x = 1150
        enemy_m_1.y = 70
        enemy_m_1.speed = 1
        enemy_m_2.x = 1150
        enemy_m_2.y = 70
        enemy_m_2.speed = 1
        enemy_l_1.x = 2550
        enemy_l_1.y = 70
        enemy_l_1.speed = 1



def keyPressed(event):
    pass 

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    global program_state
    if(program_state == 'START'):
        program_state = 'PLAY'
    elif(program_state == 'WIN') or (program_state == 'LOOSE'):
        program_state = 'PLAY'
