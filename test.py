import tf_agents.environments.wrappers

for name in dir(tf_agents.environments.wrappers):
    obj = getattr(tf_agents.environments.wrappers, name)
    if hasattr(obj, "__base__") and issubclass(obj, tf_agents.environments.PyEnvironmentBaseWrapper):
        n = '\n'
        print(f"{name:27s} {obj.__doc__.split(n)[0]}")
