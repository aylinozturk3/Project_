from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from base import LoginPage, BasePage  # Import base class
import time
class AmazonVideoPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver, (By.ID, "ap_email"), # ensures that the correct order of initialization, handles complex inheritance,
                         (By.ID, "ap_password"),
                         (By.ID, 'signInSubmit'),
                         (By.ID, 'continue'))
        self.url = 'https://www.primevideo.com/offers/nonprimehomepage/ref=dvm_pds_amz_TR_lb_s_g_mkw_syv6tbjDU-dc_pcrid_620067107176?gclid=EAIaIQobChMIrJPj2ZGrhwMVkgcGAB1z3AnJEAAYASAAEgLYk_D_BwE&mrntrk=slid__pgrid_93213874476_pgeo_9199051_x__adext__ptid_kwd-297838409925'
        self.video_locator=(By.CLASS_NAME, 'tHfREs')
        self.play_button_locator=(By.XPATH, '//a[@role="button" and contains(@class, "_1jWggM") and contains(@class, "_3_H2aX") and contains(@class, "fbl-play-btn") and contains(@class, "fbl-btn")]')
        self.video_=(By.CLASS_NAME,'webPlayerSDKContainer')
    def play_first_video(self, duration, email, password):
         self.open_url(self.url)
         sign_in_element = self.find_element(By.XPATH, '//a[contains(@class, "DVPAWebWidgetsUI_Button__button") and @href="/gp/video/signup/ref=dvm_MLP_tr_Join_1_pm?offer=pm"]')
         if sign_in_element:
             sign_in_element.click()
         else:
             print("sign-in button isnot found")
             return False

         self.login(email, password)
         try:
             self.play_video(duration, self.video_locator, self.play_button_locator)
         finally:
             self.driver.quit()








