from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def login_twitter(username, password):

    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)

    password_field.send_keys(password)
    driver.implicitly_wait(1)

    password_field.send_keys(Keys.ENTER)

    textbox = driver.find_element_by_id('tweet-box-home-timeline')

    textbox.send_keys("""Im using Selenium!""")

    submit = driver.find_element_by_class_name("tweet-action")

    submit.click()


if __name__ == '__main__':
    username = "h1168636@nwytg.com"
    password = "asdasd123"
    login_twitter(username, password)