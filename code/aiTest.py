import pyglet
import GameEnv
import random
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers.legacy import Adam

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

# Initialize the game environment
game = GameEnv.RacingEnv()

# Define the state space and number of actions
states = 16
actions = 15 

def chooseAction(int):
    if int == 1:
        action = [True, False, False, False, False]
    elif int == 2:
        action = [True, False, False, False, True]
    elif int == 3:
        action = [True, False, True, False, False]
    elif int == 4:
        action = [True, False, True, False, True]
    elif int == 5:
        action = [True, False, False, True, False]
    elif int == 6:
        action = [True, False, False, True, True]
    elif int == 7:
        action = [False, True, False, False, False]
    elif int == 8:
        action = [False, True, True, False, False]
    elif int == 9:
        action = [False, True, False, True, False]
    elif int == 10:
        action = [False, False, False, False, False]
    elif int == 11:
        action = [False, False, False, False, True]
    elif int == 12:
        action = [False, False, True, False, False]
    elif int == 13:
        action = [False, False, True, False, True]
    elif int == 14:
        action = [False, False, False, True, False]
    elif int == 15:
        action = [False, False, False, True, True]

# Build the model
model = Sequential()
model.add(Flatten(input_shape=(1, states)))
model.add(Dense(24, activation="relu"))
model.add(Dense(24, activation="relu"))
# Output layer with sigmoid activation for binary output (True/False)
model.add(Dense(actions, activation="sigmoid"))

# Create the agent
agent = DQNAgent(
    model=model,
    memory=SequentialMemory(limit=50000, window_length=1),
    policy=BoltzmannQPolicy(),
    nb_actions=actions,
    nb_steps_warmup=10,
    target_model_update=0.01
)

# Compile the agent
agent.compile(Adam(learning_rate=0.001), metrics=["mae"])

# Fit the agent
agent.fit(game, nb_steps=20000, visualize=False, verbose=1)

# Test the agent
results = agent.test(game, nb_episodes=10, visualize=False, verbose=1)

# Example output interpretation
for _ in range(10):
    action_probs = agent.forward(game.reset())
    action_bools = action_probs > 0.5  # Threshold at 0.5 to decide True/False
    print(action_bools)

print(np.mean(results.history["episode_reward"]))

#get random action from a list of five
def random_action(numb):
    action_list = []
    for x in range(1,numb+1):
        action_list.append(random.choice([True,False]))
    
    return action_list

games = 0
score = 0

game.MAX_EPISODE_LENGTH = 1000
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