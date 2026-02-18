import numpy as np
from stable_baselines import PPO
from stable_baselines.common.policies import MlpPolicy

class StrategyGenerator:
    def __init__(self):
        self.model = None
        
    def create_model(self, state_space, action_space):
        """
        Initializes the reinforcement learning model.
        Args:
            state_space (Space): State space for observations.
            action_space (Space): Action space for possible actions.
        """
        self.model = PPO(MlpPolicy, env, verbose=1)
        
    def train_model(self, environment, steps=1000):
        """
        Trains the reinforcement learning model.
        Args:
            environment: The trading environment to interact with.
            steps (int): Number of training steps.
        """
        self.model.learn(env, nb_steps=steps)
        
# Example usage:
env = CryptoTradingEnv()
generator = StrategyGenerator()
generator.create_model(env.observation_space, env.action_space)
generator.train_model(env, steps=1000)