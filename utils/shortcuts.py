import environ
import os
from pathlib import Path



def get_env(name):
    # Take environment variables from .env file
    BASE_DIR = Path(__file__).resolve().parent.parent
    env = environ.Env(
            # set casting, default value
            DEBUG=(bool, False)
        )
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    return env(name)