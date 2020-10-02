# Coded by: Tahseen Jamal
# Github: github.com/tahseenjamal
# tahseen(dot)jamal(at)gmail.com

from dateutil.parser import parse
from datetime import datetime, date
from selenium import webdriver
import bs4, os

def trading_day():

    holidays = []

    def parse_date(string):
        try:

            holiday = datetime.strptime(string, "%d-%b-%Y").date()

            return holiday

        except ValueError:

            return False

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    url = 'https://www1.nseindia.com/products/content/equities/equities/mrkt_timing_holidays.htm'

    os.environ['MOZ_HEADLESS'] = '1'

    driver = webdriver.Firefox()

    driver.get(url)

    page_content = driver.page_source

    os.environ['MOZ_HEADLESS'] = '0'

    driver.close()

    html = bs4.BeautifulSoup(page_content, 'lxml')
    tables = html.find("table", { "class" : "holiday_list" })
    rows = tables.findAll('td')

    string_array = []

    for row in rows:

        string_array.extend(row.text.splitlines())

    for string in string_array:

        valid = parse_date(string)

        if not valid:

            continue

        holidays.append(valid)

    print(holidays)

    if date.today().weekday in [6,7] or date.today() in holidays:

        return False

    return True

print(trading_day())




