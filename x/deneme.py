from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


html_file_path = "C:/Users/Dell/Desktop/x/index.html"


driver.get(html_file_path)


adres_listesi = [
    "New York, Times Square",
    "New York, Central Park",
    "New York, Empire State Building",
    "New York, Statue of Liberty",
    "New York, Metropolitan Sanat Müzesi",
    "New York, Rockefeller Center",
    "New York, One World Trade Center",
    "New York, Brooklyn Köprüsü",
    "New York, Central Park Hayvanat Bahçesi",
    "New York, Broadway",
    "New York, High Line Park",
    "New York, Museum of Modern Art (MoMA)",
    "New York, Grand Central Terminal",
    "New York, 9/11 Memorial ve Müzesi",
    "New York, Top of the Rock",
    "Tokyo, Tokyo Kulesi",
    "Tokyo, Senso-ji Tapınağı",
    "Tokyo, Meiji Tapınağı",
    "Tokyo, Shibuya Kavşağı",
    "Tokyo, Shinjuku Gyoen Ulusal Bahçesi",
    "Tokyo, Tokyo Disneyland",
    "Tokyo, Tokyo DisneySea",
    "Tokyo, Ueno Park",
    "Tokyo, Tokyo Ulusal Müzesi",
    "Tokyo, Tokyo Skytree",
    "Tokyo, Odaiba",
    "Tokyo, Tokyo Metropolitan Government Building",
    "Tokyo, Akihabara",
    "Tokyo, Roppongi Hills ve Mori Sanat Müzesi"
]



for adres in adres_listesi:
   
    adres_input = driver.find_element(By.ID, "address")

    
    adres_input.clear()
    adres_input.send_keys(adres)

    
    search_button = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_button.click()

   
    time.sleep(2)  

   
    results = driver.find_elements(By.CSS_SELECTOR, ".results")
    if results:
        for result in results:
            print(result.text)
    else:
        print("Not found")


driver.quit()
