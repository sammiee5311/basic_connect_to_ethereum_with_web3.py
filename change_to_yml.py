import yaml


abi = None  # paste abi

with open('abi.yml', 'w') as f:
    yaml.dump(abi, f)
