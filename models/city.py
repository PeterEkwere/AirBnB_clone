#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""defines City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class holds city's data"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
