from enum import Enum

MAIN_LOGGER = 'main'

class Environment(Enum):
    DEV = 'dev'
    STAGING = 'staging'
    PROD = 'prod'
