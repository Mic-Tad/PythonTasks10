import datetime as dt

import pymongo
from mentorTask10.camel_to_snake_converter import change_case
from mentorTask10.cl_currency import ClCurrency
from mentorTask10.cl_daily_bar import ClDailyBar
from mentorTask10.list_generator import END_DATE, START_DATE, generate_list_of_entities

client = pymongo.MongoClient("localhost:27017")
db = client.cl_daily_bars
coll = db.First


def import_entity(entity, coll=coll):
    coll.insert_one(
        {"Date": entity.date, "Value": entity.value, "AssetName": entity.asset_name, "Currency": entity.currency.name}
    )


def import_entities(list_of_entities, coll=coll):
    for entity in list_of_entities:
        import_entity(entity, coll)


def clear_db(coll=coll):
    coll.delete_many({})


def create_index(field, unique=False, coll=coll):
    coll.create_index(field, unique=unique)


def lazy_update(entity, new_data, coll=coll):
    flag = False
    for k, v in new_data.items():
        k = change_case(k)
        if entity.__dict__[k] != v:
            flag = True
            break
    if flag:
        filter = {
            "Date": entity.date,
            "Value": entity.value,
            "AssetName": entity.asset_name,
            "Currency": entity.currency.name,
        }
        new_values = {"$set": new_data}
        coll.update_one(filter, new_values)


def get_data_slice(asset_name, from_date=START_DATE, to_date=END_DATE, coll=coll):
    li = []
    for i in coll.find({"AssetName": asset_name, "Date": {"$gte": from_date, "$lte": to_date}}):
        e = ClDailyBar()
        for k, v in i.items():
            e.__setattr__(k, v)
        li.append(e)
    return li


if __name__ == "__main__":
    e = ClDailyBar(dt.datetime(2000, 1, 1), 2305.0, "Dell", ClCurrency.F_E_CHF)
    # l=generate_list_of_entities(5)
    clear_db()
    import_entity(e)
    # print(get_data_slice("Dell", from_date=dt.datetime(2010, 1, 1)))
    print("ok")
