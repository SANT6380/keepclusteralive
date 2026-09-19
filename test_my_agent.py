from sandbox_env import make_sandbox_env
from my_agent import MyAgent

env = make_sandbox_env(seed=3, debug=True)

agent = MyAgent(
    n_nodes=env.n_nodes,
    node_capacity=env.node_capacity
)

obs = env.reset()
agent.reset()

for t in range(env.episode_length):

    actions = agent.act(obs)

    obs, reward, done, info = env.step(actions)

    agent.update(obs, reward, done, info)

    if done:
        break

print(env.get_episode_log())