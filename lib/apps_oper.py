from helpers import setup
from pathlib import Path


def get_trains():
    """
    Returns TRAINS that are not excluded
    """
    if Path(setup.TRAINS_PATH).exists():
        trains = [train for train in Path(
            setup.TRAINS_PATH).iterdir() if train.stem not in setup.EXCLUDE_TRAINS]

    return trains


def get_apps(train):
    """
    Returns APPS that are nto excluded
    """
    apps = [app for app in Path(train).iterdir()
            if app.stem not in setup.EXCLUDE_APPS]

    return apps
