import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json

with open("config.json") as file:
    config = json.load(file)

def get_browser():
    """
    Reads browser name from environment variable.
    Defaults to browser value defined in config file if environment variable is not set.
    """
    return os.getenv("BROWSER", config["BROWSER"]).lower()


def build_chrome():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox") # Bypass OS security model, useful for CI/CD or container environments

    return webdriver.Chrome(options=options)


def build_firefox():
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")

    return webdriver.Firefox(options=options)


def get_driver():
    browser = get_browser()

    if browser == "chrome":
        return build_chrome()

    if browser == "firefox":
        return build_firefox()

    raise ValueError(
        f"Unsupported browser '{browser}'. Use 'chrome' or 'firefox'."
    )
