from selenium import webdriver

DRIVER = webdriver.Chrome('./chromedriver')

_base_url = "https://app.interviewme.pl/template/concept"

_deafult_implicit_wait = 10