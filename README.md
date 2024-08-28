# Python と Selenium のセットアップ手順

このドキュメントでは、Python をインストールし、Selenium と WebDriver を設定して、スクリプトを実行するための手順を説明します。

## 目次

- [Python のインストール](#pythonのインストール)
- [Selenium のインストール](#seleniumのインストール)
- [WebDriver のダウンロード](#webdriverのダウンロード)
- [スクリプトの作成](#スクリプトの作成)
- [スクリプトの実行](#スクリプトの実行)

## Python のインストール

1. **Python の公式サイトから Python をダウンロードし、インストールします。**  
   [Python 公式サイト](https://www.python.org/downloads/)

   - インストールが完了したら、以下のコマンドでインストールが成功したか確認します。
     ```bash
     python --version
     pip --version
     ```
   - `where python` コマンドを使用して Python のパスを確認することもできます。

## Selenium のインストール

2. **Selenium のインストール**  
   `pip`を使用して Selenium をインストールします。コマンドプロンプトやターミナルで以下を実行します。
   ```bash
   pip install selenium
   ```

# WebDriver のダウンロードとセットアップ

## 3. WebDriver のダウンロード

使用するブラウザに対応する WebDriver をダウンロードします。以下のリンクから適切な WebDriver を取得してください：

- [Chrome WebDriver ダウンロード](https://googlechromelabs.github.io/chrome-for-testing/)

例えば、Google Chrome を使用する場合、ChromeDriver をダウンロードし、適切なディレクトリに配置します。

> **注意:** Chrome のバージョンは、Chrome ブラウザの「設定」→「ヘルプ」→「Google Chrome について」で確認できます。使用している Chrome バージョンに対応する ChromeDriver をダウンロードしてください。

## 4. ChromeDriver の PATH 設定

ダウンロードした ChromeDriver のパスをシステムの PATH に追加します。以下の手順で設定を行います：

1. ダウンロードした ChromeDriver の ZIP ファイルを解凍します。
2. 解凍した`chromedriver.exe`を、任意のディレクトリに移動します。例として、`C:\WebDriver\`に配置するとします。
3. 環境変数の設定を行います:
   - **Windows の場合**:
     1. スタートメニューを開き、「システム」を検索してクリックします。
     2. 左側のメニューから「システムの詳細設定」を選択します。
     3. 「環境変数」ボタンをクリックし、システム環境変数に ChromeDriver のパス（例：`C:\WebDriver\`）を追加します。

## 5. スクリプトの作成と実行

### スクリプトの作成

任意の Python スクリプトファイルを作成します。例えば、`xxx.py`というファイルを作成します。

### スクリプトの実行

作成したスクリプトを以下のコマンドで実行します：

```bash
python xxx.py
```
