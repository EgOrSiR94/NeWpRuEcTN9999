g = 300
h = 900
f = 350
x = 400
z = 450
c = 500
v = 550
b = 600
n = 650
m = 700
a = 750
s = 800
d = 850
def setup():
    size(1000,1000)
    background(224, 255, 255)
def draw():
    global x,z,c,v,b,n,m,a,s,d,f,g,h
    push()
    fill(70, 130, 180)
    background(224, 255, 255)
    if keyPressed:
        if key == ENTER:
            fill(70, 130, 180)
            x +=3
            z +=3
            c +=3
            v +=3
            b +=3
            n +=3
            m +=3
            a +=3
            s +=3
            d +=3
            f +=3
            g +=3
            h +=3

    else:
        fill(70, 130, 180)
    ellipse(450,x,80,80)
    ellipse(450,z,80,80)
    ellipse(450,c,80,80)
    ellipse(450,v,80,80)
    ellipse(450,b,80,80)
    ellipse(450,n,80,80)
    ellipse(450,m,80,80)
    ellipse(450,a,80,80)
    ellipse(450,s,80,80)
    ellipse(450,d,80,80)
    ellipse(450,f,80,80)
    ellipse(450,g,80,80)
    ellipse(450,h,80,80)
    pop()
    push()
    fill(128, 128, 128)
    rect(1,200,500,100)
    rect(400,250,80,80)
    pop()
    push()
    rect(600,100,300,500)
    pop()
    push()
    fill(0, 191, 255)
    rect(650,200,200,300)
    pop()    
    push()
    fill(128, 128, 128)
    rect(250,900,500,500)
    pop()
    push()
    noStroke()
    ellipse(700,250,50,50)
    ellipse(730,270,50,50)
    ellipse(690,400,50,50)
    ellipse(700,370,50,50)
    ellipse(800,350,50,50)
    ellipse(740,370,50,50)
    ellipse(730,400,50,50)
    ellipse(690,270,50,50)
    ellipse(800,300,50,50)
    ellipse(830,320,50,50)
    ellipse(790,320,50,50)
    pop()
    push()
    fill(238, 130, 238)
    rect(10,700,100,50)
    pop()
    push()
    fill(128,128,128)
    rect(5,740,120,50)
    pop()
    if n >= 950:
        n = 300
    if b >= 950:
        b = 300
    if v >= 950:
        v = 300
    if c >= 950:
        c = 300
    if x >= 950:
        x = 300
    if z >= 950:
        z = 300
    if z >= 950:
        z = 300
    if m >= 950:
        m = 300
    if a >= 950:
        a = 300
    if s >= 950:
        s = 300
    if d >= 950:
        d = 300
    if f >= 950:
        f = 300
    if g >= 950:
        g = 300
    if h >= 950:
        h = 300
