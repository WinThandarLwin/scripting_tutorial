from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# ChromeDriverのパスを指定
driver_path = 'C:/WebDriver/chromedriver.exe'  # ダウンロードしたChromeDriverのパスを指定

# Serviceオブジェクトを作成
service = Service(executable_path=driver_path)

# Chromeブラウザを起動
driver = webdriver.Chrome(service=service)

# Wikipediaのホームページを開く
driver.get('https://www.wikipedia.org/')

# 検索ボックスを見つけて検索キーワードを入力
search_box = driver.find_element(By.NAME, 'search')
search_box.send_keys('Python (programming language)')
search_box.send_keys(Keys.RETURN)

# 検索結果が表示されるまで待機
time.sleep(3)

# 最初の検索結果のページのタイトルを取得
title = driver.find_element(By.ID, 'firstHeading').text
print('Page title is:', title)

# ページが読み込まれるのを待機
time.sleep(10)

# ブラウザを閉じる
driver.quit()
