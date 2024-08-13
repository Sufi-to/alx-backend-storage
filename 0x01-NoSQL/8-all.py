#!/usr/bin/env python3
"""Module that interacts with a mongo database."""


def list_all(mongo_collection):
    """Returns the list of all the documents in the collection"""
    return [i for i in mongo_collection.find()]
        