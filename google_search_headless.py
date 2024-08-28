from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import logging

# ChromeDriverのパスを指定
driver_path = 'C:/WebDriver/chromedriver.exe'  # ダウンロードしたChromeDriverのパスを指定

# ChromeOptionsオブジェクトを作成し、ヘッドレスモードを有効にする
chrome_options = Options()
#--headless オプションでヘッドレスモードを有効にします。
chrome_options.add_argument('--headless')
#--disable-gpu オプションでGPUの使用を無効にします（特にLinux環境での安定性向上のため）。
chrome_options.add_argument('--disable-gpu')
#--window-size=1920x1080 オプションでウィンドウサイズを指定します。
# ヘッドレスモードではデフォルトでウィンドウサイズが小さいため、適切なサイズを設定します。
chrome_options.add_argument('--window-size=1920x1080')

# Serviceオブジェクトを作成
service = Service(executable_path=driver_path)

# Chromeブラウザをヘッドレスモードで起動
driver = webdriver.Chrome(service=service, options=chrome_options)

#ブラウザのコンソールに表示される警告メッセージを無視したいのでtryを追加
try:
    # Googleのホームページを開く
    driver.get('https://www.google.com')
    print(driver.current_url)

    # 検索ボックスを見つけて検索キーワードを入力
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Python programming')
    search_box.send_keys(Keys.RETURN)

    # 検索結果が表示されるまで待機
    time.sleep(3)

    # 2番目の検索結果のリンクをクリック
    second_result = driver.find_elements(By.CSS_SELECTOR, 'div.g h3 a')[1]
    second_result.click()

    # ブラウザを閉じずにそのまま残す
    # 任意の時間待機
    time.sleep(10)  # ここでブラウザが開いたまま10秒待機します
    print("Program Finsh!!")
finally:
    # ブラウザを閉じる（必要に応じてコメントアウト）
    driver.quit()
