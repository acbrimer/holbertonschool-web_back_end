#!/usr/bin/env python3
""" Module for 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """update_topics - updates mongo collection"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
