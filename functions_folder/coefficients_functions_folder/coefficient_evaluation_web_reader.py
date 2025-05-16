# using selenium to instance the browser to get all the values from the js scripts
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

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
    # links are located in the 3d tr section of page, full path in old version using beautiful soup and requests
    '''
     div1_list = body.find_all("div",class_="container-fluid main")
        for div1 in div1_list:
        main = div1.find("main")
        div2rrf = main.find("div",class_="row row-fluid")
        div3c12m4 = div2rrf.find("div", class_=["col-12", "mt-4"])

        div4rpfmc = div3c12m4.find("div",class_="row p-4 fond-main-core")
        div5c12cl10 = div4rpfmc.find("div",class_="col-12 col-lg-10")
        article1 = div5c12cl10.find("article")
        div6lgt = article1.find("div", id = "lastgames_tab")
        table1tlftsfflpb = div6lgt.find("table", class_="table_list footable toggle-square-filled footable-loaded phone breakpoint")
        tbody1 = table1tlftsfflpb.find("tbody")
        tr1 = tbody1.find("tr")
        td1 = tr1.find("td", class_="footable-visible footable-last-column")
        href = td1.find("a")
        matches.append(href)
    '''
  

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
        w_l = [0,0]
        for match_url in matches:
            driver.get(match_url)

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

                print("\n")

            except Exception as e:
                print(f"Error loading match page {i}: {type(e).__name__} - {e}")
                traceback.print_exc()

    finally:
        driver.quit()

   
   
   


