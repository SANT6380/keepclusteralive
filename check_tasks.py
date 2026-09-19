from sandbox_env import make_sandbox_env

env = make_sandbox_env(seed=3, debug=True)

obs = env.reset()

for _ in range(20):
    obs, reward, done, info = env.step({})

    if len(obs["tasks"]) > 0:
        print(obs["tasks"][0])
        break