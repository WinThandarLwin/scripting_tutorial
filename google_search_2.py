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

# Googleのホームページを開く
driver.get('https://www.google.com')

# 検索ボックスを見つけて検索キーワードを入力
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python programming')
search_box.send_keys(Keys.RETURN)

# 検索結果が表示されるまで待機
time.sleep(3)

# 2番目の検索結果のリンクをクリック
# 検索結果のタイトルが <h3> タグで囲まれているため
second_result = driver.find_elements(By.CSS_SELECTOR, 'h3')[1]
second_result.click()

# ブラウザを閉じずにそのまま残す

# 任意の時間待機
time.sleep(10)  # ここでブラウザが開いたまま10秒待機します
