from selenium import webdriver
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import os
import subprocess
import json
import requests
import urllib3
from urllib.parse import urlparse

class AFConnect:
    def __init__(self, url ,id, pw):
        self.url = url
        self.id = id
        self.pw = pw

    def webget(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.split_url=urlparse(self.url)
        self.ip=self.split_url.hostname

        self.req_session = requests.Session()
        self.url1 = "https://" + self.ip
        self.url2 = "https://" + self.ip + "/login.cgi"
        print(self.url1)
        try:
            self.test=self.req_session.get(self.url1, verify=False)
            if self.test.status_code == 200:
                self.data = {'username': self.id, 'password': self.pw}
                self.response2 = self.req_session.post(self.url2, data=self.data, verify=False)
                self.response_value = self.response2.text
                self.response_value = self.response_value.splitlines()
                print(self.response_value[0])
                if self.response_value[0] == "0":
                    print("Error!, please input right accout")
                elif self.response_value[0] == "15":
                    self.command = 'AFLoader.exe "-c" "' + self.ip + ':443" ' + '"VirtualConfig=' + \
                                   self.response2.cookies[
                                       'VirtualConfig'] + "; " + " SaveRequired=" + self.response2.cookies[
                                       'SaveRequired'] + "; " + "SessionID=" + self.response2.cookies[
                                       'SessionID'] + '" ' + '"' + self.response_value[0] + '"' + ' "kr" ""'
                    #os.system(self.command)
                    subprocess.Popen(self.command)
                else:
                    print("Error")
            else:
                print("Error")
        except Exception as e:
            print("Error")

class NGFWConnect:
    def __init__(self, url, id, pw):
        self.url = url
        self.id = id
        self.pw = pw

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=self.options)

    def teardown(self):
        self.driver.quit()

    def webget(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(2)
        self.driver.find_element(by='id', value='login_ft_id-inputEl').send_keys(self.id)
        self.driver.find_element(by='id', value='login_ft_password-inputEl').send_keys(self.pw + "\n")
        self.driverKill()

    def driverKill(self):
        os.kill(self.driver.service.process.pid, 9)
        return

class ZeniusConnect:
    def __init__(self, url, id, pw):
        self.url = url
        self.id = id
        self.pw = pw
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown(self):
        self.driver.quit()

    def webget(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(1)
        self.driver.find_element(by='name', value='z_username').send_keys(self.id)
        self.driver.find_element(by='name', value='z_password').send_keys(self.pw + "\n")
        self.driverKill()

    def driverKill(self):
        os.kill(self.driver.service.process.pid, 9)
        return

class JenniferConnect:
    def __init__(self, url, id, pw):
        self.url = url
        self.id = id
        self.pw = pw
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown(self):
        self.driver.quit()

    def webget(self):
        self.driver.get(self.url)
        self.driver.find_element(by='name', value='id').send_keys(self.id)
        self.driver.find_element(by='name', value='password').send_keys(self.pw + "\n")
        self.driverKill()

    def driverKill(self):
        os.kill(self.driver.service.process.pid, 9)
        return

class SherpaConnect:
    def __init__(self, url, id, pw):
        self.url = url
        self.id = id
        self.pw = pw
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def teardown(self):
        self.driver.quit()

    def webget(self):
        self.driver.get(self.url)
        self.driver.find_element(by='id', value='product').click()
        self.driver.find_element_by_css_selector('#selectP > ul > li:nth-child(2)').click()
        self.driver.find_element(by='id', value='userId').send_keys(self.id)
        self.driver.find_element(by='id', value='userPwd').send_keys(self.pw + '\n')
        self.driverKill()

    def driverKill(self):
        os.kill(self.driver.service.process.pid, 9)
        return

class fortiConnect:
    def __init__(self, url, id, pw):
        self.url = url
        self.id = id
        self.pw = pw

        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=self.options)

    def teardown(self):
        self.driver.quit()

    def webget(self):
        self.driver.get(self.url)
        self.driver.find_element(by='id', value='username').send_keys(self.id)
        self.driver.find_element(by='id', value='secretkey').send_keys(self.pw + "\n")
        self.driverKill()

    def driverKill(self):
        os.kill(self.driver.service.process.pid, 9)
        return
