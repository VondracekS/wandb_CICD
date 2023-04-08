import wandb

print(f"Current version of the wnadb package is {wandb.__version__}")
assert wandb.__version__ == wandb.__version__, print(f"Expencted 1.0.1 version, got {wandb.__version__}")
