from setuptools import find_packages, setup
from Cython.Build import cythonize
from itertools import chain

GYMNASIUM_VERSION = '0.29.1'
GYM_VERSION = '0.23.0'
PETTINGZOO_VERSION = '1.24.1'

docs = [
    'sphinx==5.0.0',
    'sphinx-rtd-theme==0.5.1',
    'sphinxcontrib-youtube==1.0.1',
    'sphinx-rtd-theme==0.5.1',
    'sphinx-design==0.4.1',
    'furo==2023.3.27',
]


# These are the environments that PufferLib has made
# compatible with the latest version of Gym/Gymnasium/PettingZoo
# They are included in PufferTank as a default heavy install
# We force updated versions of Gym/Gymnasium/PettingZoo here to
# ensure that users do not have issues with conflicting versions
# when switching to incompatible environments
compatible_environments = {
    'atari': [
        'gymnasium[atari,accept-rom-license]',
        'stable_baselines3==2.1.0',
    ],
   'box2d': [
        'swig==4.1.1',
        'gymnasium[box2d]',
    ],
    'butterfly': [
        'pettingzoo[butterfly]',
    ],
    'crafter': [
        'crafter==1.8.0',
    ],
    'dm_lab': [
        'gym_deepmindlab==0.1.2',
        'dm_env==1.6',
    ],
    'griddly': [
        'imageio==2.23.0',
        'griddly==1.4.2',
    ],
    'microrts': [
        'ffmpeg==1.4',
        'gym_microrts==0.3.2',
    ],
    'minigrid': [
        'minigrid==2.3.1',
    ],
    'minihack': [
        'minihack==0.1.5',
    ],
    'nethack': [
        'nle==0.9.0',
    ],
    'nmmo': [
        'nmmo',
    ],
    'procgen': [
        'procgen==0.10.7',
    ],
}

for env, packages in compatible_environments.items():
    compatible_environments[env] = [
        f'gymnasium=={GYMNASIUM_VERSION}',
        f'gym=={GYM_VERSION}',
        f'pettingzoo=={PETTINGZOO_VERSION}',
        *packages,
    ]

# These environments require specific old versions of 
# Gym/Gymnasium/PettingZoo to work.
incompatible_environments = {
    'avalon': [
        'avalon-rl==1.0.0',
    ],
    'dm_control': [
        'dm_control==1.0.11',
        'gym_dmc==0.2.5',
        'gym==0.21.0',
    ],
    'magent': [
        'magent==0.2.4',
        'pettingzoo==1.19.0',
        # The Magent2 package is broken for now
        #'magent2==0.3.2',
    ],
    'minerl': [
        'gym==0.17.0',
        'minerl==0.4.4',
    ],
    #'smac': [
    #    'git+https://github.com/oxwhirl/smac.git',
    #],
    #'stable-retro': [
    #    'git+https://github.com/Farama-Foundation/stable-retro.git',
    #]
}

rllib = [
    'ray[all]==2.0.0',
    'setproctitle==1.1.10',
    'service-identity==21.1.0',
    'pydantic==1.9',
]

cleanrl = [
    'tensorboard==2.11.2',
    'torch',
    'wandb==0.13.7',
    'psutil==5.9.5',
]

setup(
    name="pufferlib",
    description="PufferAI Library"
    "PufferAI's library of RL tools and utilities",
    long_description_content_type="text/markdown",
    version=open('pufferlib/version.py').read().split()[-1].strip("'"),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'gym==0.23',
        'numpy==1.23.3',
        'opencv-python==3.4.17.63',
        'openskill==4.0.0',
        'pettingzoo==1.19.0',
        'cython==3.0.0',
    ],
    extras_require={
        'docs': docs,
        'rllib': rllib,
        'cleanrl': cleanrl,
        'compatible-environments': compatible_environments,
        **compatible_environments,
        **incompatible_environments,
    },
    ext_modules = cythonize("pufferlib/extensions.pyx"),
    python_requires=">=3.8",
    license="MIT",
    author="Joseph Suarez",
    author_email="jsuarez@mit.edu",
    url="https://github.com/PufferAI/PufferLib",
    keywords=["Puffer", "AI", "RL"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)

#stable_baselines3
#supersuit==3.3.5
#'git+https://github.com/oxwhirl/smac.git',

#curl -L -o smac.zip https://blzdistsc2-a.akamaihd.net/Linux/SC2.4.10.zip
#unzip -P iagreetotheeula smac.zip 
#curl -L -o maps.zip https://github.com/oxwhirl/smac/releases/download/v0.1-beta1/SMAC_Maps.zip
#unzip maps.zip && mv SMAC_Maps/ StarCraftII/Maps/
