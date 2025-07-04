依照以下的流程來執行測試：

啟動 Appium 2 Server

打開終端機 (Terminal)

直接輸入 appium 指令後按下 Enter：

Bash appium

您會看到日誌顯示 Welcome to Appium v2.x.x，並且伺服器會開始在 4723 埠上運行

讓這個終端機視窗保持開啟，不要關閉。

使用 test_final_appium2.py 的 Python 腳本

在腳本的項目裡面的終端機視窗打上：

pytest 執行測試 (如果您想產出報告，就用 pytest --html=report.html --self-contained-html)
