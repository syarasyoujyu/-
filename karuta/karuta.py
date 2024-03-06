import pygame,random,time
from pygame.locals import *
#the number of karuta
fuda_num=3

fuda_width,fuda_height=80,160
#for setting clear time
time_lag=0
WIDTH,HEIGHT=fuda_width*1.2*7,((fuda_num+4)//5+1)*fuda_height*1.2

class karuta:

    def __init__(self,screen,show,read,back):
        self.back=back
        self.start=time.time()
        self.count=0
        self.font=pygame.font.Font(None,30)
        self.untaken=[i for i in range(fuda_num)]
        self.show,self.read=show,read
        self.place=[[i%5*fuda_width*1.2,i//5*fuda_height*1.2] for i in self.untaken]
        self.need_take=random.sample(self.untaken,k=1)[0]
        self.select_show,self.select_read=[[self.show[i],i] for i in self.untaken],[[self.read[i],i] for i in self.untaken]
        self.screen=screen
        self.static()


    #make karuta field (base)
    def static(self):
        self.screen.blit(self.back,(0,0))
        self.select_show,self.select_read=[[self.show[i],i] for i in self.untaken],[[self.read[i],i] for i in self.untaken]

        #put karuta untaken
        for img in self.select_show:
            self.screen.blit(img[0],(self.place[img[1]][0],self.place[img[1]][1]))
        
        #put yomifuda
        text=self.font.render("Karuta to take",True,(130,130,130),(250,250,250))
        self.screen.blit(text,(5*fuda_width*1.2,0))
        for img in self.select_read:
            if img[1] == self.need_take:
                self.screen.blit(img[0],(5*fuda_width*1.2,fuda_height/3))
                break

        pygame.display.update()

    #check whether you take correct one or not(if True, upload yomofuda)
    def touch(self,x,y):
        if self.place[self.need_take][0]<=x<=self.place[self.need_take][0]+fuda_width and self.place[self.need_take][1]<=y<=self.place[self.need_take][1]+fuda_height:
                self.count+=1
                self.untaken.remove(self.need_take)
                if self.untaken:
                    self.need_take=random.sample(self.untaken,k=1)[0]
                self.static()
    

    #end of the game
    def end(self):
        global time_lag
        time_lag=round(time.time()-self.start,2)
        self.screen.fill((250,250,250))
        text=self.font.render(f'Congratulations! You spend {time_lag} seconds!',True,(130,130,130),(250,250,250))
        self.screen.blit(text,(180,280))
        pygame.display.update()

def main():

    #setup
    pygame.init()
    background=pygame.image.load('../KARUTA/畳.jpeg')
    background=pygame.transform.scale(background,(WIDTH,HEIGHT))
    fuda_top=["あ","い","う","え","お","か","き","く","け","こ","さ","し",
              "す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね",
              "の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","ん"]
    rand_fuda_mem=random.sample([i for i in range(len(fuda_top))],k=fuda_num)
    pygame.mouse.set_visible(True)
    fuda_show=[pygame.image.load(f'../KARUTA/fuda/show/{fuda_top[i]}.jpeg') for i in (rand_fuda_mem)]
    fuda_read=[pygame.image.load(f'../KARUTA/fuda/read/{fuda_top[i]}.jpeg') for i in (rand_fuda_mem)]
    for i in range(fuda_num):
        fuda_show[i]=pygame.transform.scale(fuda_show[i],(fuda_width,fuda_height))
        fuda_read[i]=pygame.transform.scale(fuda_read[i],(fuda_width,fuda_height))
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
    screen.blit(background,(0,0))
    pygame.display.set_caption("Karuta")
    pygame.mouse.set_pos((0,0))
    game=karuta(screen,fuda_show,fuda_read,background)
    clock=pygame.time.Clock()
    run=True

    #run the game
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run=False

            #Mouse click == take karuta
            if event.type == MOUSEBUTTONDOWN:
                    x,y=event.pos
                    game.touch(x,y)
                    #After finish game, the game close in 2 seconds
                    if game.untaken==[] and time_lag == 0:
                        run=False
                        game.end()
                        time.sleep(2)

        clock.tick(20)
    
    pygame.quit()

if __name__=="__main__":
    main()