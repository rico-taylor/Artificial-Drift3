import random
import gym
import numpy as np
import pyglet
import GameEnv



from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers.legacy import Adam

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


env = GameEnv.RacingEnv()

states = 16
actions = 5

def random_action(numb):
    action_list = []
    for x in range(1,numb+1):
        action_list.append(random.choice([True,False]))
    
    return action_list

model = Sequential()
model.add(Flatten(input_shape=(1, states)))
model.add(Dense(24, activation="relu"))
model.add(Dense(24, activation="relu"))
model.add(Dense(actions, activation="linear"))

agent = DQNAgent(
    model=model,
    memory = SequentialMemory(limit=50000, window_length=1),
    policy=BoltzmannQPolicy(),
    nb_actions=actions,
    nb_steps_warmup=10,
    target_model_update=0.01
)

agent.compile(Adam(learning_rate=0.001), metrics=["mae"])
agent.fit(env, nb_steps=1, visualize=False, verbose=1)

results = agent.test(env, nb_episodes=10, visualize=True, verbose=1)
print(env)
print(np.mean(results.history["episode_reward"]))


episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score=0

    while not done:
        action = random_action(5)
        _, reward, done, __ = env.step(action)
        score += reward
        env.render()
        print("reward:", reward)

    print(f"Edpisode {episode}, Score: {score}")

env.close()
env.end()