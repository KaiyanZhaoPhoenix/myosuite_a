
## Installations
You will need Python 3.8 or later versions.

It is recommended to use [Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links) and to create a separate environment with:
``` bash
conda create --name MyoSuite python=3.8
conda activate MyoSuite
pip install -U myosuite
pip install stable_baseline3
```

It is possible to install MyoSuite from source:
``` bash
conda create --name MyoSuite python=3.8
conda activate MyoSuite
git clone https://github.com/KaiyanZhaoPhoenix/myosuite_a.git
pip install -e .
pip install stable_baseline3
```
for advanced installation, see [here](https://myosuite.readthedocs.io/en/latest/install.html#alternative-installing-from-source).

Test your installation using the following command (this will return also a list of all the current environments):
``` bash
python -m myosuite.tests.test_myo
```


You can also visualize the environments with random controls using the command below:
``` bash
python -m myosuite.utils.examine_env --env_name myoElbowPose1D6MRandom-v0
```
**NOTE:** On MacOS, we moved to mujoco native `launch_passive` which requires that the Python script be run under `mjpython`:
``` bash
mjpython -m myosuite.utils.examine_env --env_name myoElbowPose1D6MRandom-v0
```

It is possible to take advantage of the latest MyoSkeleton. Once added (follow the instructions prompted by `python -m myosuite_init`), run:
``` bash
python -m myosuite.utils.examine_sim -s myosuite/simhive/myo_model/myoskeleton/myoskeleton.xml
```

## Examples
It is possible to create and interface with MyoSuite environments just like any other OpenAI gym environments. For example, to use the `myoElbowPose1D6MRandom-v0` environment



```python
from myosuite.utils import gym
env = gym.make('myoElbowPose1D6MRandom-v0')
env.reset()
for _ in range(1000):
  env.mj_render()
  env.step(env.action_space.sample()) # take a random action
env.close()
```
