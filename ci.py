import wandb

print(f"Current version of the wnadb package is {wandb.__version__}")
assert wandb.__version__ == '1.0.0', print(f"Expencted 1.0.0 version, got {wandb.__version__}")
