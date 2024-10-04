import os

from typing import Optional

def pick_env_variable(env_var_name: str, default: Optional[str] = None) -> str:
    """Pick an environment variable or return a default value."""
    return os.environ.get(env_var_name, default)

def load_env_file_in_memory(env_file_path: str) -> None:
    """Load an environment file in memory."""
    with open(env_file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            os.environ[key] = value