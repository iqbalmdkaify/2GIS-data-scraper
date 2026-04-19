import logging
from typing import TypeAlias

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

NoSuchElement: TypeAlias = NoSuchElementException

XPATHS = {
    "result_count": "(//span[@class='_1xhlznaa'])[1]",
    "scroll_container_primary": "(//div[@class='_15gu4wr'])[3]",
    "scroll_container_fallback": "(//div[@class='_15gu4wr'])[2]",
    "next_page_btn": "//div[@class='_5ocwns']//div[2]",
}


def get_default_chrome_options() -> Options:
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")

    return options


def get_default_chrome_service() -> Service:
    service = webdriver.ChromeService()

    return service


# Module-level defaults used as fallback when create_session is called without arguments
default_options: Options = get_default_chrome_options()
default_service: Service = get_default_chrome_service()


def create_session(
    options: Options = get_default_chrome_options(),
    service: Service = get_default_chrome_service(),
) -> WebDriver:
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()

    logging.debug("CHROME SESSION STARTED")

    return driver


def quit_session(driver: WebDriver) -> None:
    driver.quit()
    logging.debug("CHROME SESSION TERMINATED")


def navigate(url: str, driver: WebDriver) -> None:
    driver.get(url)


def find(driver: WebDriver, xpath: str) -> WebElement:
    return driver.find_element(By.XPATH, xpath)


def scroll_into_view(driver: WebDriver, el: WebElement | None) -> None:
    driver.execute_script("arguments[0].scrollIntoView(false);", el)


def wait(time: float, driver: WebDriver) -> None:
    driver.implicitly_wait(time)


def click_element(element: WebElement) -> None:
    element.click()
