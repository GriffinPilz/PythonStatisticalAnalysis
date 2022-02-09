import sqlite3
from stats import DataClean
import random

conn = sqlite3.connect('dataset.db')

# cursor creation
c = conn.cursor()

# c.execute("""CREATE TABLE dataset (
#            data_id integer,
#            data_value real
#            )""")

# for i in range(10):
#    c.execute("INSERT INTO dataset (data_id, data_value) VALUES ({}, {})".format(i, random.randint(1, 10)))


def insert_data(insert_data, data):
    p_key = data[-1][0] + 1
    c.execute("INSERT INTO dataset (data_id, data_value) VALUES ({}, {})".format(p_key, insert_data))
    return c.fetchall()


def get_data(data=""):
    print("Get Data")
    if data:
        c.execute("SELECT * FROM dataset WHERE data_value={}".format(data))
    else:
        c.execute("SELECT * FROM dataset")
    return c.fetchall()


def update_data(identifier, data):
    c.execute("UPDATE dataset SET data_value={} WHERE data_id={}".format(data, identifier))
    return c.fetchall()


def delete_data(data=""):
    c.execute("DROP TABLE dataset")
    # c.execute("DELETE FROM dataset WHERE data_value={}".format(data))
    return c.fetchall()

# insert_data(17, get_data())


data_list = get_data()
new_list = []
for item in data_list:
    new_list.append(item[1])

data1 = DataClean(new_list)
# for i in range(10):
#    insert_data(i+1)

print(data1.calc_median(new_list))
print(data1.calc_mean())

conn.commit()

conn.close()
