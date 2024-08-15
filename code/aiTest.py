import pyglet
import GameEnv

game = GameEnv.RacingEnv()

games = 0
score = 0
def run_episode():
    global games
    global score

    done = False

    action = [True,False,True,False,False]

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