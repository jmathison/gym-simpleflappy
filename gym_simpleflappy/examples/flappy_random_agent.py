import gym
import gym_simpleflappy

env = gym.make("SimpleFlappy-v0")
env.reset()

max_eps = 1000
episode = 0

steps = 0

while episode < max_eps:
    obs = env.reset()
    steps = 0
    score = 0
    while True:

        if steps % 15 == 0:
            action = env.action_space.sample()
        else:
            action = 0

        obs, reward, done, _ = env.step(action)
        env.render()
        score += reward
        steps += 1
        if done:
            break

    print(score)
    episode += 1

env.close()
