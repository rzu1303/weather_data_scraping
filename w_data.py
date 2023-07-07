from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import traceback
from selenium.webdriver import ActionChains

import pyautogui
import queue

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config


def read_weather(link, days):
    weather_q = queue.Queue(maxsize=days)
    website = link
    d = days

    # print(pyautogui.size())
    # Size(width=1366, height=768)
    # Website link
    # website = "https://www.visualcrossing.com/weather/weather-data-services/dhaka/metric/2023-05-28/2023-06-01"

    try:
        driver = webdriver.Chrome()
        driver.get(website)
        print("connected to the website")
    except Exception as e:
        print(f"Could not connect to the website {e} {traceback.format_exc()}")

    try:
        # Maximizing the window
        driver.maximize_window()
        # waiting for loading the page
        driver.implicitly_wait(5)
        # Handeling with welcome ....
        time.sleep(3)
        pyautogui.click(880, 545)
        time.sleep(3)
        # Handeling with cookie
        pyautogui.click(750, 525)
        driver.implicitly_wait(5)
        # temperature = []
        # humidity = []
        # precip = []
        # wind = []
        print(" handled cookies")
    except Exception as e:
        print(f"Could not handle cookies {e} {traceback.format_exc()}")   
       
    try:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        driver.implicitly_wait(5)
        time.sleep(3)
        items = driver.find_element(By.XPATH, ('//*[@id="queryApp"]/div/div[4]/div[5]/div[3]/table/tbody'))
        w_data = items.text
        # print(w_data)

        temp = w_data.split("\n")
        ### list
        # for i in range(len(temp)):
        #     mtemp = temp[i].split(" ")
        #     #append
        #     temperature.put(mtemp[3])
        #     humidity.put(mtemp[8])
        #     precip.put(mtemp[9])
        #     wind.put(mtemp[16])

        #### Queue
        # weather_q = queue.Queue(maxsize=days)
        with weather_q.mutex:
            weather_q.queue.clear()
        for i in range(days):
            if config.cancel:
                print("Download Cancelled")
                break
            mtemp = temp[i].split(" ")
            weather_q.put(
                {
                    'temperature': mtemp[3],
                    'humidity': mtemp[8],
                    'precip': mtemp[9],
                    'wind': mtemp[11]
                }
            )


        print("download data done")  
    except Exception as e:
        print(f"Unable to download data {e} {traceback.format_exc()}")
    # return(temperature, humidity, precip, wind)
    return weather_q
     
        

# def download_weather(self):   
#     if download == 1:

#         with open("Weather_data.csv", "a", encoding="utf-8") as fp:
#             for index in range(0, len(temperature), 1):
#                 fp.write(temperature[index]+","+" "+ humidity[index]+","+precip[index]+","
#                         +","+wind[index]+"\n")


if __name__=="__main__":
    read_weather()
    # download_weather()