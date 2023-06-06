from gym.envs.registration import register
register(
    id='SPYENV-v0',
    entry_point='dark_sac.sac.SpyUnimodal:SpyUnimodal',
)

register(
    id='SPYENV-v1',
    entry_point='dark_sac.sac.SpyBimodal:SpyBimodal',
)