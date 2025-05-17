# using selenium to instance the browser to get all the values from the js scripts
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from classes_folder.team_classes_folder.team_service import Team

def scrape_match_links():
    # gets rid of window pop up
    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
   
    # initializes the browser instance
    driver = webdriver.Chrome(options=options)
    # navigates the browser to the home page
    driver.get("https://gol.gg/esports/home/")

    matches = []
   
  

    try:
        wait = WebDriverWait(driver, 30)
        
       

        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, " #lastgames_tab > table > tbody")))
        rows = driver.find_elements(By.CSS_SELECTOR, " #lastgames_tab > table > tbody > tr")
        
        i=0
        for row in rows:
            try:
                tds = row.find_elements(By.TAG_NAME, "td")
                # link is in 3d td
                if len(tds) < 3:
                    print(f"Row {i}: Not enough columns")
                    continue

                game_td = tds[2]
                a_tag = game_td.find_element(By.TAG_NAME, "a")
                href_raw = a_tag.get_attribute("href")

                if href_raw.startswith("../"):
                    href = "https://gol.gg" + href_raw[2:]
                else:
                    href = href_raw
                    
                #remove the game page part of the link
                href = href[:-10]
                matches.append(href)
                i+=1
            
    
            except Exception as e:
                print(f"Row {i} error: {e}")
                
                
        i=0
        while i < 10:
            matches[i] = matches[i]+"page-summary/"
            i+=1
        ws_ls= []
        for match_url in matches:
            driver.get(match_url)
            w_l=[]
            try:
                # Wait for the page to be fully loaded
                WebDriverWait(driver, 30).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )
                #wait for 
                wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "h1.text_victory, h1.text_defeat")))

                headers = driver.find_elements(By.CSS_SELECTOR, "h1.text_victory, h1.text_defeat")
                for header in headers:
                    text = driver.execute_script("return arguments[0].textContent", header)
                    print(text)
                    w_l.append(text)

                print("\n")

            except Exception as e:
                print(f"Error loading match page {i}: {type(e).__name__} - {e}")
                traceback.print_exc()
            ws_ls.append(w_l)
            
        print(ws_ls)
        
        
    finally:
        driver.quit()

   
   
   


