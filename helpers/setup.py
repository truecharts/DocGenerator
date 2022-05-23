# Path where trains are stored
TRAINS_PATH = "./charts"

# Print Verbose Output
VERBOSE = True

# Exclude specific trains
EXCLUDE_TRAINS = [
    "dev",
]

# Exclude specific apps
EXCLUDE_APPS = [
    "traefik",
]

# The rest trains will be after those
TRAIN_ORDER_FOR_FILES = [
    "core",
    "stable"
]
