import pygame
# [235,96,123]
p1 = pygame.display.set_mode([1000, 1000], )
x_x=100
y_y=60
pygame.key.set_repeat(100,100)

def dis():
    p1.fill([20, 35, 23])

def rec(x,y):
    x2=50
    y2=10
    pygame.draw.line(p1,[230,145,53],[x,y],[x+x2,y],5)
    pygame.draw.line(p1,[230,145,53],[x+x2,y],[x+x2,1000],5)
    if x<1000:
        rec(x+x2,y+y2)

def calodes(r,s,col,loc,olc):
    pygame.draw.circle(p1,[col,loc,olc],[500,500],r,s)
    if r>10:
        calodes(r-10,s-1,col-10,loc-10,olc-10)
    pygame.draw.circle(p1,[0,0,0],[500,500],25)

def romb(x,y,xx,yy):
    #правая верхняя
    pygame.draw.line(p1,[255,255,255],[x,y-yy+20],[x+xx,y],5)
    #правая нижняя
    pygame.draw.line(p1,[255,255,255],[x,y+yy],[x+xx,y],5)
    #левая верхняя
    pygame.draw.line(p1,[255,255,255],[x,y-yy],[x-xx,y],5)
    #левая нижняя
    pygame.draw.line(p1,[255,255,255],[x,y+yy],[x-xx,y],5)

    pygame.draw.circle(p1,[255,255,255],[x,y],3)

    if xx>20 and yy>20:
        romb(x, y, xx-20, yy-20)



def eventure():
    global y_y,x_x
    events=pygame.event.get()
    for ev in events:
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_LEFT:
            x_x-=10
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_RIGHT:
            x_x+=10
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_DOWN:
            y_y-=10
        if ev.type == pygame.KEYDOWN and ev.key == pygame.K_UP:
            y_y+=10
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            dis()
            # romb(ev.pos[0],ev.pos[1],x_x,y_y)

while True:
    # rec(0,100)
    # calodes(200,100,255,255,255)
    dis()
    romb(500, 500, x_x, y_y)
    eventure()




    pygame.display.flip()