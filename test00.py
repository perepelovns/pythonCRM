from asyncio.windows_events import NULL
from email.message import EmailMessage
from logging import NullHandler
from msilib.schema import Error
from turtle import Screen
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

driver.get("https://msk03-sbl1-tst.licard.com/siebel/app/marketing/rus?SWECmd=Login&SWECM=S&SRN=")

def enter(): # вход в сибель
    login = driver.find_element_by_id('s_swepi_1')
    login.click()
    login.send_keys('SADMIN')

    password = driver.find_element_by_id('s_swepi_2')
    password.click()
    password.send_keys('SADMIN')

    enterButton = driver.find_element_by_id('s_swpi_22')
    enterButton.click()
    
    print('enter in CRM - passed')

def topUpplet(): # проверка шапки сибеля до раскрываемого блока
    # var:
    #     Домой -- home
    #     Календарь маркетинга -- marketingCalendar
    #     Маркетинговые планы -- marketingPlans
    #     Программы -- programs
    #     Кампании -- campaigns
    #     Сегменты -- segments
    #     Предложения -- offers
    #     Мероприятия -- events
    #     Статистика -- statistics
    #     Integration Error Screen -- IES
    #     Договоры -- treaties
    #         Администрирование - Карты, клиенты -- AMC
    #         Email -- email
    #         Клиенты ФЛ -- clietsInd 
    #         Поиск ФЛ -- searchInd
    #         Карты -- maps
    #         Администрирование - Отчеты BIP -- ABIP
    #         Поиск ЮЛ -- searchLeg
    #         Обращения -- hits
    #         Чеки -- checks
    #         Товары -- products
    #         Потенциальные сделки -- potentialDeals
    #         Почтовый ящик -- mailbox
    #         Администрирование - Справочная информация -- AHI
    
    home = driver.find_element(By.LINK_TEXT, 'Домой').click()
    print('Вкладка Домой работает')
    marketingCalendar = driver.find_element(By.LINK_TEXT, 'Календарь маркетинга').click()
    print('Вкладка Календарь маркетинга работает')
    marketingPlans = driver.find_element(By.LINK_TEXT, 'Маркетинговые планы').click()
    print('Вкладка Маркетинговые планы работает')
    programs = driver.find_element(By.LINK_TEXT, 'Программы').click()
    print('Вкладка Программы работает')
    campaigns = driver.find_element(By.LINK_TEXT, 'Кампании').click()
    print('Вкладка Кампании работает')
    segments = driver.find_element(By.LINK_TEXT, 'Сегменты').click()
    print('Вкладка Сегменты работает')
    offers = driver.find_element(By.LINK_TEXT, 'Предложения').click()
    print('Вкладка Предложения работает')
    events = driver.find_element(By.LINK_TEXT, 'Мероприятия').click()
    print('Вкладка Мероприятия работает')
    statistics = driver.find_element(By.LINK_TEXT, 'Статистика').click()
    print('Вкладка Статистика работает')
    IES = driver.find_element(By.LINK_TEXT, 'Integration Error Screen').click()
    print('Вкладка Integration Error Screen работает')
    treaties = driver.find_element(By.LINK_TEXT, 'Договоры').click()
    print('Вкладка Договоры работает')

driver.close()

if __name__ == "__main__":
    unittest.main()