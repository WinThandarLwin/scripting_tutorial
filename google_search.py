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
print(driver.current_url)
#表示している HTML は page_source でアクセスすることができます
print(driver.page_source)


# 検索ボックスを見つけて検索キーワードを入力
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Python programming')
search_box.send_keys(Keys.RETURN)
print(driver.current_url)
# 検索結果が表示されるまで待機
time.sleep(3)

# 検索結果の最初のリンクをクリック
first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
first_result.click()
print(driver.current_url)

# ページが読み込まれるのを待機
time.sleep(10)

# ブラウザを閉じる
driver.quit()