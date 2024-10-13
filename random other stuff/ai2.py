import os
import gym
from stable_baselines3 import PPO
#from stable_baselines3.common.vec_env import DummyVecEnv
#from stable_baselines3.common.evaluation import evaluate_policy

environment_name = 'CartPole-v1'
env = gym.make(environment_name)

episodes = 50
for episode in range(1, episodes+1): #makes 5 loops for the five environmnets
    state = env.reset() #resets the environment to the initial state
    done = False
    score = 0

    while not done:
        env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward
    print("Episdoe:{} Score: {}".format(episode, score))
env.close()