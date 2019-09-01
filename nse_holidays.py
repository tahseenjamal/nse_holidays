from dateutil.parser import parse
from datetime import datetime
import bs4, requests

def holidays():

    holidays = []

    def parse_date(string):
        try:

            holiday = datetime.strptime(string, "%d-%b-%Y").date()

            # Without str, it would give as date type
            return str(holiday)

        except ValueError:

            return False

    url = 'https://www.nseindia.com/products/content/equities/equities/mrkt_timing_holidays.htm'

    data = requests.get(url)
    html = bs4.BeautifulSoup(data.content, 'lxml')
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

    return holidays

# Returns string array of holidays. If you want as type date, remove the str() in the function
print(holidays())
