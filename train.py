# train_model.py

import os
from stable_baselines3 import PPO
from myosuite.utils import gym

# Create the environment
env = gym.make('myoChallengeOslRunFixed-v0', reset_type='init')

# Create PPO model
model = PPO("MlpPolicy", env, verbose=1)

# Set up training parameters
total_timesteps = 10_000_000  # Total training steps
save_interval = 1_000_000  # Save the model every 1 million steps
model_save_dir = 'saved_models'  # Directory to save models

# Create the directory to save models if it doesn't exist
os.makedirs(model_save_dir, exist_ok=True)

# Start training, saving the model at every interval
for step in range(1, total_timesteps // save_interval + 1):
    # Train the model for 'save_interval' steps
    model.learn(total_timesteps=save_interval)
    
    # Save the model
    model_path = os.path.join(model_save_dir, f'model_{step * save_interval}.zip')
    model.save(model_path)
    print(f"Model saved at: {model_path}")

# Final model save after all training steps
model.save(os.path.join(model_save_dir, 'final_model.zip'))
print("Training completed and final model saved.")
