
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
It is possible to create and interface with MyoSuite environments just like any other OpenAI gym environments. For example, to use the `myoElbowPose1D6MRandom-v0` environment, it is possible simply to run: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zFuNLsrmx42vT4oV8RbnEWtkSJ1xajEo)



```python
from myosuite.utils import gym
env = gym.make('myoElbowPose1D6MRandom-v0')
env.reset()
for _ in range(1000):
  env.mj_render()
  env.step(env.action_space.sample()) # take a random action
env.close()
```

You can find our [tutorials](https://github.com/myohub/myosuite/tree/main/docs/source/tutorials#tutorials) on the general features and the **ICRA2023 Colab Tutorial** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1KGqZgSYgKXF-vaYC33GR9llDsIW9Rp-q) **ICRA2024 Colab Tutorial** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1JwxE7o6Z3bqCT4ewELacJ-Z1SV8xFhKK#scrollTo=QDppGIzHB9Zu)
on how to load MyoSuite models/tasks, train them, and visualize their outcome. Also, you can find [baselines](https://github.com/myohub/myosuite/tree/main/myosuite/agents) to test some pre-trained policies.



## License

MyoSuite is licensed under the [Apache License](LICENSE).

## Citation

If you find this repository useful in your research, please consider giving a star ⭐ and cite our [arXiv paper](https://arxiv.org/abs/2205.13600)  by using the following BibTeX entrys.

```BibTeX
@Misc{MyoSuite2022,
  author =       {Vittorio, Caggiano AND Huawei, Wang AND Guillaume, Durandau AND Massimo, Sartori AND Vikash, Kumar},
  title =        {MyoSuite -- A contact-rich simulation suite for musculoskeletal motor control},
  publisher = {arXiv},
  year = {2022},
  howpublished = {\url{https://github.com/myohub/myosuite}},
  year =         {2022}
  doi = {10.48550/ARXIV.2205.13600},
  url = {https://arxiv.org/abs/2205.13600},
}
```
