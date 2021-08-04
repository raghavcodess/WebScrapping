def download_image(count, topic):
    from selenium import webdriver
    import urllib
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    path = '/home/raghav/Downloads/Extensions/chrometool/chromedriver'
    jarvis = webdriver.Chrome(path)
    jarvis.get('https://www.google.com/imghp?hl=en')
    jarvis_search = jarvis.find_element_by_class_name('gLFyf')
    jarvis_search.send_keys(topic)
    jarvis_search.send_keys(Keys.RETURN)

    try:
        islmp = WebDriverWait(jarvis, 10).until(EC.presence_of_element_located((By.ID, 'islmp')))
        sub = islmp.find_elements_by_tag_name('img')
        for index,img in enumerate(sub):
            if count>=index:
                src = img.get_attribute('src')
                if src!=None:
                    src = str(src)
                    urllib.request.urlretrieve(src,''+str(index)+'.jpg')
        
        
    finally:
        jarvis.quit()
   
if __name__ == "__main__":
	download_image(5,"Logan Paul")