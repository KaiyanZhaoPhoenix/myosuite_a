import mujoco
import numpy as np
import os
import skvideo.io
from base64 import b64encode
from stable_baselines3 import PPO
from tqdm import tqdm
import myosuite
from myosuite.utils import gym

# Create MyoChallenge environment and train the model
env = gym.make('myoChallengeOslRunFixed-v0', reset_type='init')
model = PPO("MlpPolicy", env, verbose=0)
model.learn(total_timesteps=10000000)

# Evaluate the trained policy
all_rewards = []
for _ in tqdm(range(5)):  # Randomize over different terrain types
    ep_rewards = []
    done = False
    obs = env.reset()
    while not done:
        obs = env.obsdict2obsvec(env.obs_dict, env.obs_keys)[1]
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, info, _ = env.step(action)
        ep_rewards.append(reward)
    all_rewards.append(np.sum(ep_rewards))
print(f"Average reward: {np.mean(all_rewards)} over 5 episodes")

# Render the trained policy and save as video
frames = []
for _ in tqdm(range(5)):  # Randomize over different terrain types
    env.reset()
    done = False
    obs = env.reset()
    for _ in range(200):
        obs = env.obsdict2obsvec(env.obs_dict, env.obs_keys)[1]
        action, _ = model.predict(obs, deterministic=True)
        geom_1_indices = np.where(env.sim.model.geom_group == 1)
        env.sim.model.geom_rgba[geom_1_indices, 3] = 0
        frame = env.sim.renderer.render_offscreen(
                          width=400,
                          height=400,
                          camera_id=1)
        frames.append(frame)
        obs, reward, done, info, _ = env.step(action)

env.close()

# Save video
os.makedirs('videos', exist_ok=True)
skvideo.io.vwrite('videos/test_policy.mp4', np.asarray(frames), outputdict={"-pix_fmt": "yuv420p"})