import os
import loguru


ENVIRONMENT = os.environ.get('ENVIRONMENT', False)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', '20937822'))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    OWNER_ID = os.environ.get('OWNER_ID', 6258709129)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 20937822 # api id here
    OWNER_ID = 1663603208
    API_HASH = "68d3b463d3c53536782545f790aa5147"
    BOT_TOKEN = "5497421359:AAHFjvr9I2ZjfwgV05oeaZQL1eMfgeiDt7k"
    DATABASE_URL = "postgres://tfzztwkgmoynsv:5b9438f345093083dcca74678c4f07067576e02ff1677668ab3ab157f71d886b@ec2-54-73-22-169.eu-west-1.compute.amazonaws.com:5432/djboigf6k6dvi"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "Film_Nest" # must join channel link here
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
