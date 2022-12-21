import light_version_abuse_packet as abusePack
from light_version_abuse_packet.metamask import Metamask
from light_version_abuse_packet.adspower_driver import Driver
from light_version_abuse_packet.adspowered import AdsPower
from selenium.webdriver.common.by import By
import time 
import utils
import random


class Abuse():
    def __init__(self, antik_id, username):
        self.antik_id = antik_id
        self.driver = Driver().run_driver(self.antik_id)
        self.username = username
        self.dellayLoadPage = 18 # ожидание загрузки страницы



    def __clickSign(self):
        self.driver.execute_script('document.getElementsByClassName("button_button__+gfhG button_primary__VwQOG")[0].click()') 
        time.sleep(15) ## после подключения функций метамаск, изменить.


    def __clickKeysGen(self, id):
        btns  = self.driver.find_elements(By.CLASS_NAME, 'image_button_root__GPyPv')
        btns[id].click()
        time.sleep(1)



    def __connectWallet(self):
        btnConnectWallet  = self.driver.find_element(By.CLASS_NAME, 'wallet_interaction_toast_interactions__Z3xHH').find_element(By.TAG_NAME, 'button') # нажатие на Connect Wallet
        btnConnectWallet.click()

        time.sleep(2)
        btnMetaMask = self.driver.find_element(By.CLASS_NAME, "ju367v8r") # выбор MetaMask
        btnMetaMask.click()
    


    def loginAccount(self):
        self.driver.get('https://zk.money/balance')
        time.sleep(self.dellayLoadPage)
        self.__clickKeysGen(0)
        self.__connectWallet()
        # метод connect_wallet коннекта MetaMask
        self.__clickSign()
        time.sleep(5)## после подключения функций метамаск, изменить.
    


    def getBalance(self):
        self.driver.get('https://zk.money/balance')
        time.sleep(self.dellayLoadPage)
        balance = self.driver.find_element(By.CLASS_NAME, 'my_balance_amount__jqj1E').text

        return balance

    

    def deposit(self, depositValue):
        self.driver.get('https://zk.money/balance')
        time.sleep(self.dellayLoadPage)
        self.driver.execute_script('document.getElementsByClassName("button_text__xo9+v")[0].click()') 
        time.sleep(3)
        fieldAmountDeposit = self.driver.find_elements(By.CLASS_NAME, "field_field__T8s0-")[1] # вставить сумму депозита
        time.sleep(1)
        fieldAmountDeposit.send_keys(depositValue)
        time.sleep(1)
        self.driver.execute_script('document.getElementsByClassName("button_text__xo9+v")[0].click()')
        time.sleep(1)
        self.driver.execute_script('document.getElementsByClassName("sc-hHLeRK kZXBHC")[0].click()')
        time.sleep(1)
        self.driver.execute_script('document.getElementsByClassName("button_text__xo9+v")[0].click()')
        time.sleep(25)

        # метод confirm_transaction подписания MetaMask
        # метод confirm_transaction подписания MetaMask


        


    def registration(self):
        self.driver.get('https://zk.money/balance')
        time.sleep(self.dellayLoadPage)
        self.__clickKeysGen(0) #нажатие на Retrieve Aztec Address
        self.__connectWallet() 

        time.sleep(15) ## после подключения функций метамаск, изменить.
            # метод connect_wallet коннекта MetaMask
            # метод confirm_transaction подписания MetaMask
        
        self.__clickSign() # нажатие на sign
            # метод confirm_transaction подписания MetaMask
        self.__clickSign() # нажатие на sign
            # метод confirm_transaction подписания MetaMask
        self.__clickKeysGen(1) # нажатие на Retrive Spending Key
        self.__clickSign() # нажатие на sign
            # метод confirm_transaction подписания MetaMask
        self.__clickKeysGen(2) # нажатие на Copy To Clipboard
            # метод confirm_transaction подписания MetaMask
        utils.Utils().saveBooferText("file.txt") # сохранение из буффера обмена в файл
        time.sleep(2)

        self.driver.execute_script('document.getElementsByClassName("button_button__+gfhG button_primary__VwQOG")[0].click()') # нажатие на Next Step 
        time.sleep(2)

        fieldUserName = self.driver.find_element(By.CLASS_NAME, "field_field__T8s0-") # вставить юзернейм
        fieldUserName.send_keys(self.username) 

        self.driver.execute_script('document.getElementsByClassName("select_selectBox__lODUh select_border__edM58 fee_selector_inputInner__Ir8E1")[0].click()') # открыть список
        time.sleep(1)
 
        self.driver.execute_script('document.getElementsByClassName("dropdown_dropdownOption__GBX40 dropdown_feeOption__2mqfO")[0].click()') # выбор скорости
        time.sleep(1)

        self.driver.execute_script(f'document.getElementsByClassName("field_field__T8s0- field_fieldHasSelector__c1Y1O")[0].value = {random.uniform(0.001, 0.005)}') # вставить значение в ETH
       

        self.driver.execute_script('document.getElementsByClassName("button_text__xo9+v")[1].click()') # регистрация 
        self.__clickSign() # нажатие на sign
        time.sleep(300) # задержка на проверку аккаунта.
        # метод confirm_transaction подписания MetaMask
        self.__clickSign() # нажатие на sign
        # метод confirm_transaction подписания MetaMask

