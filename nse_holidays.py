# Coded by: Tahseen Jamal
# Github: github.com/tahseenjamal
# tahseen(dot)jamal(at)gmail.com
# ================================

from datetime import datetime, date
from selenium import webdriver
import os


def get_nse_holidays:

    url = 'https://www.nseindia.com/resources/exchange-communication-holidays'
    
    os.environ['MOZ_HEADLESS'] = '1'
    
    driver = webdriver.Firefox()
    
    driver.get(url)
    
    page_content = driver.page_source
    
    os.environ['MOZ_HEADLESS'] = '0'
    
    driver.close()
    
    df = pd.read_html(page_content, attrs={'id': 'holidayTable'})[0]
    holidays = df.Date.apply(lambda x : parse_date(x)).to_list()

    return holidays

def is_today_a_trading_holiday(holidays):

    # If today is in weekends or in the holiday dates then return true
    if date.today().weekday in [6,7] or date.today() in holidays:
        return True
    else:
        return False


holidays = get_nse_holidays()

print(is_today_a_trading_holiday(holidays))





