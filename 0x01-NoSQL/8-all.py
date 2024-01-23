#!/usr/bin/env python3
""" List all documents in Python """
import pymongo


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    return mongo_collection.find()
