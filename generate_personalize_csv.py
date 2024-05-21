
from random import randint
from helpers.random_dates import random_timestamp
from helpers.csv_writer import write_dict_array_csv
import constants


# constants.py
event_types = constants.EVENT_TYPES
start_date = constants.START_DATE
end_date = constants.END_DATE
records = constants.RECORDS
distinct_users_ids = constants.DISTINCT_USERS_IDS
distinct_products_ids = constants.DISTINCT_PRODUCTS_IDS
csv_data_output_file = constants.CSV_DATA_OUTPUT_FILE

data = []
for i in range(records):
    record = {"USER_ID": 0, "ITEM_ID": 0, "TIMESTAMP": 0, "EVENT_TYPE": "", }
    event_type = randint(0, 4)
    user_id = randint(1, distinct_users_ids)
    item_id = randint(0, distinct_products_ids)
    r_timestamp = int(random_timestamp(start_date, end_date))

    record.update({"USER_ID": user_id})
    record.update({"ITEM_ID": item_id})
    record.update({"EVENT_TYPE": event_types[event_type]})
    record.update({"TIMESTAMP": r_timestamp})
 
    data.append(record)

write_dict_array_csv(
    csv_data_output_file, data, ["USER_ID", "ITEM_ID", "TIMESTAMP", "EVENT_TYPE"]
)
