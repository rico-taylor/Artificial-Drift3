import pyglet
import numpy as np
from ddqn_keras import DDQNAgent
import GameEnv

TOTAL_GAMETIME = 1000  # Max game time for one episode
N_EPISODES = 1000
REPLACE_TARGET = 50

game = GameEnv.RacingEnv()

ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=5, epsilon=1.00, epsilon_end=0.10, epsilon_dec=0.9995, replace_target=REPLACE_TARGET, batch_size=512, input_dims=16)

# if you want to load the existing model uncomment this line.
# careful an existing model might be overwritten
# ddqn_agent.load_model()

ddqn_scores = []
eps_history = []

def run_episode(e):
    #game.reset()  # Reset env

    done = False
    score = 0
    counter = 0

    # Initialize with a default action (all False)
    initial_action = [False, False, False, False, False]
    observation_, reward, done = game.step(initial_action)
    observation = np.array(observation_)

    gtime = 0  # Set game time back to 0
    renderFlag = False  # If you want to render every episode set to true

    if e % 10 == 0 and e > 0:  # Render every 10 episodes
        renderFlag = True

    while not done:
        action = ddqn_agent.choose_action(observation)
        observation_, reward, done = game.step(action)
        observation_ = np.array(observation_)

        # Countdown; if no reward is collected, the car will be done within 100 ticks
        if reward == 0:
            counter += 1
            if counter > 100:
                done = True
        else:
            counter = 0

        score += reward

        ddqn_agent.remember(observation, action, reward, observation_, int(done))
        observation = observation_
        ddqn_agent.learn()

        gtime += 1

        if gtime >= TOTAL_GAMETIME:
            done = True

        if renderFlag:
            game.render()

    eps_history.append(ddqn_agent.epsilon)
    ddqn_scores.append(score)
    avg_score = np.mean(ddqn_scores[max(0, e-100):(e+1)])

    if e % REPLACE_TARGET == 0 and e > REPLACE_TARGET:
        ddqn_agent.update_network_parameters()

    if e % 10 == 0 and e > 10:
        ddqn_agent.save_model()
        print("save model")

    print('episode: ', e, 'score: %.2f' % score,
          ' average score %.2f' % avg_score,
          ' epsilon: ', ddqn_agent.epsilon,
          ' memory size', ddqn_agent.memory.mem_cntr % ddqn_agent.memory.mem_size)

def run():
    for e in range(N_EPISODES):
        run_episode(e)

if __name__ == '__main__':
    pyglet.clock.schedule_interval(lambda dt: run(), 1/60)
    pyglet.app.run()