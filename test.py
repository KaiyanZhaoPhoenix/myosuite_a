import os
import numpy as np
import skvideo.io
from stable_baselines3 import PPO
from myosuite.utils import gym
from tqdm import tqdm
import argparse

# Set up argument parser to allow selecting model from the command line
parser = argparse.ArgumentParser(description="Test trained model and generate video")
parser.add_argument('--model', type=str, required=True, help="Path to the trained model (e.g., saved_models/model_1000000.zip)")
args = parser.parse_args()

# Load the environment
env = gym.make('myoChallengeOslRunFixed-v0', reset_type='init')

# Load the trained model from command line argument
model_path = args.model
model = PPO.load(model_path)
print(f"Loaded model from: {model_path}")

# Render the trained policy and save as a video
frames = []
for _ in tqdm(range(5)):  # Run over different scenarios
    env.reset()
    done = False
    obs = env.reset()
    for _ in range(200):  # Increase the number of steps to generate more frames
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

# Create videos directory if it doesn't exist
os.makedirs('videos', exist_ok=True)

# Extract model name from the model path to use in video file name
model_name = os.path.splitext(os.path.basename(model_path))[0]
video_path = f'videos/test_policy_{model_name}.mp4'

# Save video to disk
skvideo.io.vwrite(video_path, np.asarray(frames), outputdict={"-pix_fmt": "yuv420p"})

print(f"Video has been saved to '{video_path}'")
