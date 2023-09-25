import pufferlib.emulation
from pufferlib.environments import Squared as env_creator
from pufferlib.models import Default as Policy

def make_env(distance_to_target=3, num_targets=1):
    '''Puffer Squared environment'''
    env = env_creator(distance_to_target=distance_to_target, num_targets=num_targets)
    return pufferlib.emulation.GymPufferEnv(env=env)