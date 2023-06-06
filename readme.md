# WCSAC-IQN

Portions of the code in darksac.py are adapted from [Safety Starter Agents](https://github.com/openai/safety-starter-agents).

**Warning:** If you want to use the DARK-SAC algorithm in [Safety Gym](https://github.com/openai/safety-gym), make sure to install Safety Gym according to the instructions on the [Safety Gym repo](https://github.com/openai/safety-gym).

The various utilities here are copied over from [Spinning Up in Deep RL](https://github.com/openai/spinningup/tree/master/spinup/utils). 

The Spy Game is created within SpyGame.py.

## Installation & Operation

Two ways to install this package:

### Direct installation

To install this package:

```
cd /path/to/DARKSAC

pip install -e .
```

### Through [Safety Starter Agents]
So you can install [Safety Starter Agents](https://github.com/openai/safety-starter-agents), and add darksac.py of our package to `/path/to/safety-starter-agents/safe_rl/sac`.
Then you can follow the instructions on the [Safety Starter Agents](https://github.com/openai/safety-starter-agents) to use our algorithms as using their given baselines.

### Reproduce Experiments
**Example:** If you want to test DARK-SAC with risk level 0.5 in PointGoal, run:
```
cd /path/to/sac

python darksac.py --env 'Safexp-PointGoal1-v0' -s SEED --rl 0.5 --cost_lim d --logger_kwargs_str '{"output_dir": "./xxx"}'
```
where `SEED` is the random seed (we used 0, 10, and 20 in the paper experiments), `d` is the real-world safety threshold (25 in the paper), and `'{"output_dir": "./xxx"}'` indicates where to store the data. 
