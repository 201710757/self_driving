# Driving environment

import numpy as np
import gym
from gym.utils import seeding
from gym import spaces

ACTION_SPACE = 9 # Left, Right, Straight, Backwards combination + stop => (8way + 1stop)
OBS_SPACE = 180*1 # every 2 degrees out of 360 * (No obastacles : -1, else : distance)
FLAG = True # Can see road = True

class Drive(gym.Env):
    def __init__(self):
        super(Drive, self).__init__()
        self.action_space = spaces.Discrete(ACTION_SPACE)
        self.observation_space = spaces.Discrete(OBS_SPACE)

    def step(self, action):
        
        observation = np.zeros(shape=(OBS_SPACE,), dtype=int)
        reward = 0
        done = True

        return observation, reward, done, {}

    def reset(self):
        observation = np.zeros(shape=(OBS_SPACE,), dtype=int)

        return observation

    def render(self):
        pass
