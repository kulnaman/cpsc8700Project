import pygame as pg
pg.init()
music = pg.mixer.music.load('Assets/sound/bg.ogg')
def main():
    pg.music.play(loops=-1, start=0)
main()
