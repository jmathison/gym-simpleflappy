# gym-simpleflappy

A Gym environment for a Flappy bird clone with a simple observation space.

Get a reward for each pipe passed. Observations returned are:
```
[bird height, bird speed, distance to next pipe, height of next pipe, distance to second pipe, height of second pipe]
```

Installation
--
```
git clone https://github.com/jmathison/gym-simpleflappy.git
cd gym-simpleflappy
pip install -e .
```

Run an Example
--
Run this sample agent to see the environment in action:
```
python -m gym_simpleflappy.examples.flappy_random_agent
```
This agent picks a random action (flap or not flap) every 15 frames. Score is printed after each episode.
