#!/usr/bin/env python3
"""11-schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """schools_by_topic - lists schools by topic"""
    return mongo_collection.find({"topics": {"$in": [topic]}})
