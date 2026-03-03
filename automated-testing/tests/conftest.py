import pytest
from utils.driver_manager import get_driver
from pages.login_page import LoginPage
import json
import logging

@pytest.fixture(scope="session")
def config():
    with open("config.json") as file:
        return json.load(file)

@pytest.fixture(scope="session")
def logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )   
    return logging.getLogger()

@pytest.fixture()
def logged_in_driver(config, logger):
    driver = get_driver()

    driver.get(config["BASE_URL"])
    logger.info(f"logging in to \"{config['BASE_URL']}\"")
    login_page = LoginPage(driver)

    creds = config["CREDENTIALS"]
    login_page.login(creds["username"], creds["password"])

    yield driver
    driver.quit()

