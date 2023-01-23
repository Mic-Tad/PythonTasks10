import datetime as dt
import random
from typing import List
from mentorTask10.cl_currency import ClCurrency
from mentorTask10.cl_daily_bar import ClDailyBar

START_YEAR = 2000
END_YEAR = START_YEAR + 20
START_MONTH = 1
END_MONTH = 12
START_DAY = 1
END_DAY = 30
START_DATE = dt.datetime(START_YEAR, START_MONTH, START_DAY)
END_DATE = dt.datetime(END_YEAR, END_MONTH, END_DAY)
ASSETS = {1: "Dell", 2: "Amazon", 3: "Apple", 4: "Tesla", 5: "Microsoft", 6: "Zoom"}


def generate_list_of_entities(n: int, st_y: int = START_YEAR, e_y: int = END_YEAR, st_m: int = START_MONTH,
                              e_m: int = END_MONTH, st_d: int = START_DAY,
                              e_d: int = END_DAY) -> List[ClDailyBar]:
    li = []

    for j in range(st_y, e_y + 1):
        for k in range(st_m, e_m + 1):
            for l in range(st_d, e_d + 1):
                if k != 2 or l < 29:
                    i = random.randint(1, n)
                    e = ClDailyBar()
                    e.__setattr__("Date", dt.datetime(j, k, l))
                    e.__setattr__("Value", i + 100 * (k * i + l) % 1000 + j * l + k + l * k + 1.0)
                    e.__setattr__("AssetName", ASSETS[(n + l) % 6 + 1])
                    e.__setattr__("Currency", ClCurrency((i + k) % (len(ClCurrency)) + 1))
                    li.append(e)
    return li


def generate_list_of_n_entities(n: int, st_y: int = START_YEAR, e_y: int = END_YEAR, st_m: int = START_MONTH,
                                e_m: int = END_MONTH, st_d: int = START_DAY,
                                e_d: int = END_DAY) -> List[ClDailyBar]:
    li = []
    x=0
    for j in range(st_y, e_y + 1):
        for k in range(st_m, e_m + 1):
            for l in range(st_d, e_d + 1):
                if k != 2 or l < 29:
                    i = random.randint(1, n)
                    e = ClDailyBar()
                    e.__setattr__("Date", dt.datetime(j, k, l))
                    e.__setattr__("Value", i + 100 * (k * i + l) % 1000 + j * l + k + l * k + 1.0)
                    e.__setattr__("AssetName", ASSETS[x % 6 + 1])
                    e.__setattr__("Currency", ClCurrency((i + k) % (len(ClCurrency)) + 1))
                    x+=1
                    li.append(e)
    return li[:n]


if __name__ == "__main__":
    print(generate_list_of_entities(4))
