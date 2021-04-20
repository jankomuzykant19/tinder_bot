from selenium import webdriver
import time

class tinder_bot():
    def __init__(self):
        self.driver = webdriver.Chrome('') #PATH TO THE CHROMEDRIVER
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def login(self, login, password):
        self.driver.get('https://tinder.com/')
        login_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_button.click()
        time.sleep(2)
        fb_button = self.driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_button.click()
        #pop up window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        #pop up window
        fb_cookies = self.driver.find_element_by_xpath('//*[@title="Akceptuj wszystkie"]')
        fb_cookies.click()
        fb_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_email.send_keys(login)
        fb_password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        fb_password.send_keys(password)
        time.sleep(2)
        fb_login_button = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        fb_login_button.click()

        self.driver.switch_to_window(base_window)
        time.sleep(2)
        time.sleep(5)

        pop_up_1 = self.driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div/div/div[3]/button[1]')
        pop_up_1.click()
        pop_up_2 = self.driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div/div/div[3]/button[1]')
        pop_up_2.click()
        pop_up_3 = self.driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[2]/div/div/div[1]/button')
        pop_up_3.click()

    def close_location_pop(self):
        location_button = self.driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[1]/button')
        #print(location_button)
        location_button.click()

    def like(self):
        like_button = self.driver.find_element_by_xpath('//*[@id="u-1554866805"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
        like_button.click()


    def auto_like(self):
        pairs = 0
        liked = 0
        fuse = True
        while fuse:
            time.sleep(0.5)
            try:
                self.like()
                print("Liked person")
                liked += 1
            except Exception:
                try:
                    self.close_match()
                    print("Closed match pop-up")
                    pairs += 1
                except Exception:
                    try:
                        self.close_super_pop()
                        print("Closed super match pop-up")
                    except Exception:
                        try:
                            self.close_app_pop()
                            print("Closed app pop-up")
                        except Exception:
                            self.no_likes_pop_up(liked, pairs)
                            fuse = False

    def close_match(self):
        close_match = self.driver.find_element_by_xpath('//*[@id="u-1224495604"]/div/div/div[1]/div/div[4]/button')
        close_match.click()

    def close_super_pop(self):
        super_pop = self.driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/button[2]')
        super_pop.click()

    def close_app_pop(self):
        app_pop = self.driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[2]/button[2]')
        app_pop.click()

    def no_likes_pop_up(self, liked, pairs):
        no_likes_pop = self.driver.find_element_by_xpath('//*[@id="u1011719415"]/div/div/div[3]/button[2]')
        no_likes_pop.click()
        print("No more likes left :/")
        print(f"While using you liked {liked-1} people and got {pairs} pairs")


