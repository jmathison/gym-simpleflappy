from gym.envs.registration import register

register(
    id='simpleflappy-v0',
    entry_point='gym_simpleflappy.envs:FlappyEnv',
)