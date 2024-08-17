#!/usr/bin/env python3
"""Module the shows how to interact with mongodb using pymongo"""


def top_students(mongo_collection):
    """Returns all the students sorted by average score"""
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
