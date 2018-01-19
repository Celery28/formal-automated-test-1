import random

from lib.models import Page
from lib.models.Teachers import Teachers

from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement


class SeriesCourse(Page):
    """
    系列课集合页模型
    """
