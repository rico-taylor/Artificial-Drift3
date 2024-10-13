import random
import GameEnv
import pyglet

env = GameEnv.RacingEnv()

#get random action from a list of five
def random_action(numb):
    action_list = []
    for x in range(1,numb+1):
        action_list.append(random.choice([True,False]))
    
    return action_list


def run():
    env.MAX_EPISODE_LENGTH = 300
    episodes = 10
    env.render()
    for episode in range(1, episodes+1):
        state = env.reset()
        done = False
        score = 0
        action = random_action(5)
        
        while not done:
            
            action = random_action(5)
            _, reward, done = env.step(action)
            score += reward
            #env.render()
        
        print(f"Episode {episode}, Score: {score}")

if __name__ == '__main__':
    pyglet.clock.schedule_interval(lambda dt: run(), 1/60)
    pyglet.app.run()
