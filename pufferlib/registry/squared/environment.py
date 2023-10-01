import pufferlib.emulation
import pufferlib.wrappers
from pufferlib.environments import Squared as env_creator


def make_env(distance_to_target=3, num_targets=1):
    '''Puffer Squared environment'''
    env = env_creator(distance_to_target=distance_to_target, num_targets=num_targets)
    env = pufferlib.wrappers.GymToGymnasium(env)
    return pufferlib.emulation.GymPufferEnv(env=env)
