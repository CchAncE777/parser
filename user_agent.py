from selenium import webdriver

# Инициализация драйвера браузера
def initial():
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome( options=options)
    return(driver)

def anonim(version):

    # Инициируем новый драйвер браузера
    driver = initial()

    prop_begin = "Object.defineProperty(navigator, 'userAgent', {value: 'Mozilla/"
    prop_end = ".0 (Windows NT 40.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'});"
    driver.execute_script(prop_begin + str(version) + prop_end)

    return driver

initial()
anonim(123)