#滑动的四个函数封装
from appium import webdriver
import time


def get_size(driver):
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return (x,y)

def swipe_up(driver):
    screen=get_size(driver)
    print(screen)
    driver.swipe(screen[0]*0.5,screen[1]*0.75,screen[0]*0.5,screen[1]*0.25,200)

def swipe_down(driver):
    screen = get_size(driver)
    # print(screen)
    driver.swipe(screen[0] * 0.5, screen[1] * 0.25, screen[0] * 0.5, screen[1] * 0.75, 200)

def swipe_left(driver):
    screen = get_size(driver)
    # print(screen)
    driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.25, screen[1] * 0.5, 200)


def swipe_right(driver):
    screen = get_size(driver)
    # print(screen)
    driver.swipe(screen[0] * 0.25, screen[1] * 0.5, screen[0] * 0.75, screen[1] * 0.5, 200)


# def swipe_left_time(driver,time):
#     screen = get_size(driver)
#     # print(screen)
#     for i in range (time):
#         driver.swipe(screen[0] * 0.75, screen[1] * 0.5, screen[0] * 0.25, screen[1] * 0.5, 200)
#         pass


if __name__ == '__main__':
    caps = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "chenwenbo",
        # "appPackage": "com.jhss.youguu",
        # "appActivity": "com.jhss.youguu.tip.TipScrollActivity"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    # swipe_left_time(driver,3)
    print(get_size(driver))



    pass

    # pass




