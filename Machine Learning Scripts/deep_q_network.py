import numpy as np
import random

# Define Q-learning parameters
learning_rate = 0.1
discount_factor = 0.9
exploration_rate = 1.0
exploration_decay = 0.995
q_table = np.zeros([state_space, action_space])

# Training loop
for episode in range(num_episodes):
    state = get_initial_state()
    done = False
    while not done:
        if random.uniform(0, 1) < exploration_rate:
            action = choose_random_action(action_space)
        else:
            action = np.argmax(q_table[state])

        new_state, reward, done = take_action(state, action)
        q_table[state, action] = q_table[state, action] + learning_rate * (reward + discount_factor * np.max(q_table[new_state]) - q_table[state, action])
        state = new_state

    # Decay exploration rate over time
    exploration_rate *= exploration_decay
