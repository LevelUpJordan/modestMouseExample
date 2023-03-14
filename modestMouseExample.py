from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 

#%%

def loadChrome():
    options = Options()
    options.page_load_strategy = 'none'
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver



#%%
driver = loadChrome()

#%%

#Go to artists page

driver.get("https://genius.com/artists/Modest-mouse")
#%%

#Find all albums

driver.find_element(By.XPATH, "//div[contains(@class, 'full_width_button')][text()[contains(.,'all albums')]]").click()

albumElements = driver.find_elements(By.XPATH, "//div[contains(@class, 'profile_list_item')]//div[contains(@class, 'mini_card-info')]/parent::a")

albumLinks = []
for album in albumElements:
    albumLinks.append(album.get_attribute('href'))
    
#%%

#Create full song list

fullSongList = []
for album in albumLinks:
    driver.get(album)
    time.sleep(10)
    songs = []
    songElements = driver.find_elements(By.XPATH, '//album-tracklist-row//a[@href]')
    for song in songElements:
        songs.append(song.get_attribute("href"))
    
    fullSongList.append([album, songs])

#%%
with open(r'\\Mac\Home\Documents\modestMouse.txt', 'w', encoding='utf-8') as f:
    f.write('Modest Mouse Lyrics')
    
for albumList in fullSongList:
    with open(r'\\Mac\Home\Documents\modestMouse.txt', 'a', encoding='utf-8') as f:
        f.write('\n\n\n Album: '+albumList[0])
    
    songs = albumList[1]
    for song in songs:
        with open(r'\\Mac\Home\Documents\modestMouse.txt', 'a', encoding='utf-8') as f:
            f.write('\n\n Song: '+song)
        driver.get(song)
        time.sleep(5)
        try:
            with open(r'\\Mac\Home\Documents\modestMouse.txt', 'a', encoding='utf-8') as f:
                f.write('\n')
                f.write(driver.find_element(By.XPATH, "//div[contains(@class, 'Lyrics__Container')]").text)
        except:
            with open(r'\\Mac\Home\Documents\modestMouse.txt', 'a', encoding='utf-8') as f:
                f.write('\n')
                f.write('NO LYRICS')
            

            
        
