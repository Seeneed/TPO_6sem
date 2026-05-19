import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
@pytest.mark.parametrize("item", ["Dress", "T-shirt", "Jeans"])
def test_search_product(driver, item):
    home_page = HomePage(driver)
    home_page.search_product(item)
    
    home_page.make_screenshot(f"search_{item}")
    
    products = driver.find_elements(*HomePage.PRODUCT_NAME)
    assert len(products) > 0, f"Товар {item} не найден!"

@pytest.mark.regression
def test_cookie_check(driver):
    home_page = HomePage(driver)
    driver.get("https://automationexercise.com/")
    
    cookies = home_page.get_cookies()
    print(f"\nКоличество кук на сайте: {len(cookies)}")
    assert len(cookies) > 0

@pytest.mark.skip(reason="Функционал в разработке")
def test_future_feature(driver):
    pass

@pytest.mark.xfail(reason="Известный баг с версткой")
def test_broken_feature(driver):
    assert 1 == 2