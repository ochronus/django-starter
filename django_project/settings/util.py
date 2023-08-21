import os
from pathlib import Path

import environ


def init_env(env):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    environ.Env.read_env(env.str("ENV_PATH", os.path.join(BASE_DIR, ".env")))
