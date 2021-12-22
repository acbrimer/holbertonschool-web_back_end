#!/usr/bin/env python3
""" Module for 8-all """


def list_all(mongo_collection):
    """list_all - lists all docs in mongo_collection"""
    return [doc for doc in mongo_collection.find()]
