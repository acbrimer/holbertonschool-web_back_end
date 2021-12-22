#!/usr/bin/env python3
"""Module for 12-log_stats"""
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
collection = db["nginx"]
res = len(list(collection.find()))
print("{} logs".format(res))
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
pipeline = [
    {"$match": {"method": {"$in": methods}}},
    {"$group": {"_id": "$method", "count": {"$sum": 1}}}
]
agg = dict([(r['_id'], r['count'])
           for r in list(collection.aggregate(pipeline))])
print("Methods:")
res = ["  method {}: {}".format(
    m, agg[m] if m in agg.keys() else 0) for m in methods]
print("\n".join(res))
res = len(list(collection.find({"path": "/status"})))
print("{} status check".format(res))
