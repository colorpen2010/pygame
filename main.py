import time

import pygame, random
pygame.init()

p1 = pygame.Surface([100, 100], )
pygame.draw.circle(p1, [255, 255, 255], [50, 50], 50, 1)
pygame.draw.rect(p1, [150, 150, 150], [10, 20, 30, 40])
pygame.image.save(p1, 'file1.png')

lgp1 = pygame.image.load('logo.jpg')
pygame.draw.circle(lgp1, [255, 255, 255], [114, 64], 50, 1)
pygame.image.save(lgp1, 'lgp.png')

ilt = pygame.image.load('i like trains.jpg')
ilt = pygame.transform.scale(ilt, [400, 300])
ilt = pygame.transform.flip(ilt, False, True)
# ilt.blit(ilt,[-50,0],[100,50,100,300])
pygame.image.save(ilt, 'ilt.png')

p2 = pygame.Surface([2000, 2000])
p2.fill([255, 255, 255])
p2.blit(p1, [500 / 2, 500 / 2])
p2.blit(lgp1, [50, 50])
p2.blit(ilt, [0, 500])
p2.blit(p2, [1000, 0])
pygame.image.save(p2, 'file2.png')



p3 = pygame.display.set_mode([1000, 1000], )

rec = random.randint(0, 100)
cer = random.randint(0, 100)
ecr = random.randint(0, 100)

car = 49
rac = 49

tank = 50
knat = 50

spas = 400
saps = 300

x = 2
y = 2
wid = 10
height = 15
while True:
    time.sleep(0.01)
    car += 1
    rac += 1

    tank += 1
    knat += 1

    spas -= 1
    saps -= 1

    x += 2
    y += 1
    wid += 0.5
    height += 0.5

    # rec+=1
    # cer+=1
    # ecr+=1
    # if rec==255:
    #     rec=random.randint(0,100)
    # if cer==255:
    #     cer=random.randint(0,100)
    # if ecr==255:
    #     ecr=random.randint(0,100)

    p3.fill([rec, cer, ecr])
    # ilt2=pygame.transform.scale(ilt,[spas,saps])
    # p3.blit(ilt2,[car,rac])

    pygame.draw.rect(p3, [234, 35, 12], [x, y, 100, height], 100)
    pygame.draw.circle(p3, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], [tank, knat], wid,10)
    pygame.draw.line(p3, [250, 30, 4],[tank,knat],[x,50],random.randint(1,50))


    pygame.display.flip()
