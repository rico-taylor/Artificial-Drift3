import pyglet
import GameEnv
import random

game = GameEnv.RacingEnv()

#get random action from a list of five
def random_action(numb):
    action_list = []
    for x in range(1,numb+1):
        action_list.append(random.choice([True,False]))
    
    return action_list

games = 0
score = 0

game.MAX_EPISODE_LENGTH = 1500
def run_episode():
    global games
    global score

    done = False

    action = random_action(5)

    observation_, reward, done = game.step(action)
    game.render()

    score += reward

    #print(observation_, reward, done)
    if done == True:
        games += 1
        print("game:",games,", reward:",score)
        score = 0
        game.reset()



def run():
    run_episode()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(lambda dt: run(), 1/60)
    pyglet.app.run()