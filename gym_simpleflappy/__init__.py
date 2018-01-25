from gym.envs.registration import register

register(
    id='SimpleFlappy-v0',
    entry_point='gym_simpleflappy.envs:FlappyEnv',
)

register(
    id='SimpleFlappyDistance-v0',
    entry_point='gym_simpleflappy.envs:FlappyEnvDistance',
)
