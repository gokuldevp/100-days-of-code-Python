from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import csv

DRIVER_PATH = "D:\Development\driver\Chrome\chromedriver.exe"
URL = "https://www.audible.in/"
contents = requests.get(URL)
driver = webdriver.Chrome(DRIVER_PATH)

driver.get(URL)

final_data = [["Sl.No","Category","Book Name","Author Name"]]

alts_list = driver.find_elements(By.TAG_NAME,"img")
books_name = [alt.get_attribute('alt') for alt in alts_list if alt.get_attribute('alt')[-9:] == "cover art"]

authors_name = driver.find_elements(By.CSS_SELECTOR,".bc-link.bc-color-link.bc-text-ellipses")


i = 1
for book_name in books_name:
    if i < 13:
        data = [i,"Best Seller",book_name[:-10],authors_name[i-1].text]
        final_data.append(data)
        i += 1
    else:
        break


with open("best_selling_books.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(final_data)
