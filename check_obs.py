from sandbox_env import make_sandbox_env

env = make_sandbox_env(seed=3, debug=True)

obs = env.reset()

print("NODES:")
print(obs["nodes"])

print("\nTASKS:")
print(obs["tasks"][:3])