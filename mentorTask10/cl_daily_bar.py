import datetime as dt

import attr
from mentorTask10.camel_to_snake_converter import change_case
from mentorTask10.cl_currency import ClCurrency


@attr.s
class ClDailyBar:
    date: dt.date = attr.ib(default=dt.datetime(2020, 7, 20))
    value: float = attr.ib(default=0.0)
    asset_name: str = attr.ib(default="Amazon")
    currency: ClCurrency = attr.ib(default=ClCurrency.USD)

    def __setattr__(self, __name: str, __value) -> None:
        __name = change_case(__name)
        if __name == "date":
            self.__dict__[__name] = __value
        elif __name == "value":
            self.__dict__[__name] = __value
        elif __name == "currency":
            if type(__value)==str:
                __value=ClCurrency[__value]
            self.__dict__[__name] = __value
        elif __name == "asset_name":
            
            self.__dict__[__name] = __value
