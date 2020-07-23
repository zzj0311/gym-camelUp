from gym.envs.registration import register

register(
    id='camelup-v0',
    entry_point='gym_camelup.envs:CamelUpEnv',
)