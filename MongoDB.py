# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_22_2018  20:34
   File Name:      /GitHub/MongoDB
   Creat From:     PyCharm
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

__author__ = 'Loffew'

import logging
import pymongo

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")  # [filename]


# logging.disable(logging.CRITICAL)


def pp_dbg(*args):
    return logging.debug(*args)


c = pymongo.MongoClient(host="127.0.0.1", port=27017)
client = c["tt_test"]
db = client["study"]

# pp_dbg(list(db.find({"student": {"$gte": 60}})))
pp_dbg(db.find({}))
# db.insert({})
# db.save({})
# db.remove()
# db.delete_many()
# db.update()

# db.find().sort("money")
# db.update({"money":998},{"$set":{'people': 'ss', 'from': 'China', 'to': 'US', 'money': 10000}})