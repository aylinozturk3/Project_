from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from base import LoginPage  #import base classes
from amazonvideo import AmazonVideoPage
from discordpage import DiscordPage
from skypepage import SkypePage
from warnerturnerpage import WarnerturnerPage
from youtubekidspage import YoutubeKidsPage

class ErrorHandling:# handle diff. types of exceptions
    @staticmethod # class ın bir örneği olmadan çağırabilmek için staticmethod kullanılmıştır
    def handle_exception(e):
        if isinstance(e, ValueError):
            print(f"ValueError occurred: {e}")
        elif isinstance(e, TimeoutException):
            print(f"TimeoutException occurred: {e}")
        elif isinstance(e, WebDriverException):
            print(f"WebDriverException occurred: {e}")
        else:
            print(f"Unexpected error occurred: {e}")

if __name__ == '__main__':
    driver = webdriver.Chrome()

    sites = { #dict
        'AmazonVideo': AmazonVideoPage,
        'Discord': DiscordPage,
        'Skype':SkypePage,
        'WarnerTurner': WarnerturnerPage,
        'YoutubeKids': YoutubeKidsPage
    }

    try:
        site_name = input("please enter the site name: ( AmazonVideo, Discord, Skype, WarnerTurner, YoutubeKids): ")
        site_class = sites.get(site_name)

        if not site_class:
            print(f"site '{site_name}' is not listed above")
            driver.quit()
            exit()

        page = site_class(driver)  # create object page
        email = input("please enter your email address: ")
        password = input("please enter your password: ")
        duration = int(input("please enter the duration in sec. :"))
        if site_name in ('Discord', 'Skype'):
            page.video_call(duration, email, password)
        else:
            page.play_first_video(duration, email, password)# calling the method to play first video

    except Exception as e:
        ErrorHandling.handle_exception(e)
    finally:
        driver.quit()

