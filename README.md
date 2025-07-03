依照以下最終的、也是最標準的流程來執行測試：

啟動 Appium 2 Server

打開終端機 (Terminal)。

直接輸入 appium 指令後按下 Enter：

Bash

appium
您會看到日誌顯示 Welcome to Appium v2.x.x，並且伺服器會開始在 4723 埠上運行。

讓這個終端機視窗保持開啟，不要關閉。

使用最終版的 Python 腳本

請確認您 PyCharm 中的測試腳本，是我們倒數第二個版本，也就是專為 Appium 2 設計的那一版（capabilities 中有 appium: 前綴，且連線 URL 沒有 /wd/hub）。

我將它重新貼在下方，以確保萬無一失。

執行測試

打開另一個新的終端機視窗。

cd PyCharmMiscProject

pytest (如果您想產出報告，就用 pytest --html=report.html --self-contained-html)
