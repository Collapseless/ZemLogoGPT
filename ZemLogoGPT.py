
#If the user use not right file to open,so need to reset a sleep.
def sleep(a=3):
    for _ in range(a*40000):
        print(end='\r')


from pic import p as pic
#from Words import * as ws

try:
    import pygame
except Exception:
    print("please install a pygame. \n\
    (pip install pygame)")
    sleep()
    #An unright code to exit. / 一个错误代码，报错以退出程序。
    s

else:
    pygame.init()

QUESTION = ''

while 1:
    QUESTION = input('Q: ')
    pic(QUESTION)
