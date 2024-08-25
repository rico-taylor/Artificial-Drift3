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

env.MAX_EPISODE_LENGTH = 2000
episodes = 10
for episode in range(1, episodes+1):
    try:
        state = env.reset()
    except:
        state = [0.0, 260, 540.7883010831061, 248.6026368207048, 122.23394041784448, 84.87471813575465, 68.58619476103772, 58.57323663106676, 80.89115626007674, 575.4958984540862, 89.799454388119, 63.25040349127835, 72.87139630657704, 89.1023960305774, 125.65244082804028, 240.87486636892078]
    done = False
    score = 0
    action = random_action(5)
    
    while not done:
        
        action = random_action(5)
        _, reward, done = env.step(action)
        score += reward
        env.render()
    
    print(f"Episode {episode}, Score: {score}")
