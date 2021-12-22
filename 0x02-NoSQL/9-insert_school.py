#!/usr/bin/env python3
""" Module for 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """insert_school- inserts new doc from kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
