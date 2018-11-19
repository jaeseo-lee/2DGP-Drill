import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall

name = "MainState"

boy = None
grass = None
balls = []
big_balls = []


def collide(a, b): #충돌 검사함수
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False  #이런 경우에는 충돌이 없다!
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True  # 모두 통과하면 충돌이 있다!




def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)] # 리스트 컴프리헨션
    game_world.add_objects(balls, 1)  # 게임월드에 집어넣음 add_objects() 함수가 추가됨 리스트에 있는 객체를 모두 게임월드에 집어넣음





def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # 업테이트가 끝나고 나면
    for ball in balls:  #balls는 단순히 ball을 관리하는 리스트임
        if collide(boy, ball):  # 컬리젼 함수의 리턴 값이 트루이면
            balls.remove(ball)  # 일단 balls 리스트에서 충돌한 ball을 제거함.
            game_world.remove_object(ball)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






