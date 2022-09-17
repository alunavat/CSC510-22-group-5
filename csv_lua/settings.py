"""Settings module stores the settings for the application."""

import random


settings = {
    "eg": "nothing",
    "dump": False,
    "file": "../data/auto93.csv",
    "show_help": False,
    "nums": 512,
    "seperator": ",",
}


def update_seed(seed):
    """Update_seed method updates the seed for random selection."""
    settings["seed"] = seed
    random.seed(settings["seed"])


update_seed(10019)
