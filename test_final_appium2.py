# 檔案名稱：test_final_appium2.py

import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# =================================================================
# 元素定位符 (Locators)
# =================================================================
LOCATORS = {
    'pass_button': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/title_right_text'),
    'ad_close': (AppiumBy.XPATH, "//*[@resource-id='tw.com.icash.a.icashpay.debuging:id/label' and @text='關閉']"),
    'mine_tab': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/personal_text'),
    'login_register_button': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/text'),
    'login_account_field': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/et_acct'),
    'password_field': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/et_pwd'),
    'login_button': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/bt_login'),
    'setting_button': (AppiumBy.XPATH,
                       "//*[@resource-id='tw.com.icash.a.icashpay.debuging:id/item_name' and @text='設定']"),
    'setting_back_button': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow'),
    'homepage_tab': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/home_text'),
    'top_up_button': (AppiumBy.XPATH, "//*[@class = 'android.widget.TextView' and @text = '儲值']"),
    'top_up_back_button': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/title_right'),
    'transfer_button': (AppiumBy.XPATH, "//*[@class = 'android.widget.TextView' and @text = '轉帳']"),
    'transfer_back_button': (AppiumBy.XPATH,
                             "//*[@resource-id='tw.com.icash.a.icashpay.debuging:id/text' and @text='下次再說']"),
    'icash2_card': (AppiumBy.ID, 'tw.com.icash.a.icashpay.debuging:id/icash2_0_text'),
}


# =================================================================


@pytest.fixture(scope="module")
def appium_driver():
    """設定 Appium 2.x 連線"""

    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:udid": "emulator-5554",
        "appium:appPackage": "tw.com.icash.a.icashpay.debuging",
        "appium:appActivity": "tw.net.pic.m.wallet.activity.WelcomeActivity",
        "appium:appWaitActivity": "tw.com.icash.icashpay.framework.landing.LandingActivity",
        "appium:noReset": False,
        "appium:autoGrantPermissions": True,
    }

    # Appium 2.x 的連線路徑不需要 /wd/hub
    appium_server_url = 'http://localhost:4723'

    options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(appium_server_url, options=options)

    yield driver

    print("\n測試結束，關閉 Appium session...")
    driver.quit()


# --- 輔助函式 (保持不變) ---
def wait_and_click(wait, locator, message=""):
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()
    print(message)


def wait_and_send_keys(wait, locator, text, message=""):
    element = wait.until(EC.visibility_of_element_located(locator))
    element.send_keys(text)
    print(message)


def handle_optional_element_click(wait, locator, message_on_found="", message_on_not_found=""):
    try:
        element = WebDriverWait(wait._driver, 5).until(EC.element_to_be_clickable(locator))
        element.click()
        if message_on_found: print(message_on_found)
    except Exception:
        if message_on_not_found: print(message_on_not_found)


# -----------------------------

# 測試函式本身完全不用動
def test_icash_e2e_final(appium_driver):
    driver = appium_driver
    wait = WebDriverWait(driver, 20)

    handle_optional_element_click(wait, LOCATORS['pass_button'], "點擊 '略過' 按鈕", "未發現 '略過' 按鈕")
    handle_optional_element_click(wait, LOCATORS['ad_close'], "關閉廣告彈窗", "未發現廣告彈窗")
    time.sleep(2)

    wait_and_click(wait, LOCATORS['mine_tab'], "點擊 '我的' 分頁")
    wait_and_click(wait, LOCATORS['login_register_button'], "點擊 '登入/註冊'")
    wait_and_send_keys(wait, LOCATORS['login_account_field'], 'tester187', "輸入帳號")
    wait_and_send_keys(wait, LOCATORS['password_field'], 'Aa123456', "輸入密碼")
    wait_and_click(wait, LOCATORS['login_button'], "點擊 '登入' 按鈕")

    handle_optional_element_click(wait, LOCATORS['ad_close'], "關閉登入後的廣告", "未發現登入後的廣告")

    wait_and_click(wait, LOCATORS['mine_tab'], "再次點擊 '我的' 分頁")
    wait_and_click(wait, LOCATORS['setting_button'], "點擊 '設定'")
    wait_and_click(wait, LOCATORS['setting_back_button'], "從 '設定' 頁返回")
    wait_and_click(wait, LOCATORS['homepage_tab'], "點擊 '首頁' 分頁")
    wait_and_click(wait, LOCATORS['top_up_button'], "點擊 '儲值'")
    wait_and_click(wait, LOCATORS['top_up_back_button'], "從 '儲值' 頁返回")
    wait_and_click(wait, LOCATORS['transfer_button'], "點擊 '轉帳'")
    wait_and_click(wait, LOCATORS['transfer_back_button'], "從 '轉帳' 頁返回 (點擊下次再說)")
    time.sleep(2)

    wait_and_click(wait, LOCATORS['icash2_card'], "點擊 'icash2.0'")
    wait_and_click(wait, LOCATORS['homepage_tab'], "再次點擊 '首頁' 分頁")

    print("最終驗證：檢查是否成功停留在首頁...")
    homepage_unique_element = wait.until(EC.visibility_of_element_located(LOCATORS['top_up_button']))
    assert homepage_unique_element.is_displayed(), "測試失敗：沒有在最終畫面上找到首頁的'儲值'按鈕"
    print("測試成功：已驗證成功停留在首頁！")