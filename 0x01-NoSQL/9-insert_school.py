#!/usr/bin/env python3
"""Module for interacting with mongodb using python"""


def insert_school(mongo_collection, **kwargs):
    """Returns the id of the newly created documents"""
    id = mongo_collection.insert_one(kwargs).inserted_id
    return id
