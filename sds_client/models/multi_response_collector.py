# coding: utf-8

"""
    SDS Client Service API

     This API can be used for: - get collectors configuration by query or by ID - get datasets by a search query or by ID - get files by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query - get data as json by path, search query over datasets, by ID, or by a subset/combination of results from a dataset query 

    The version of the OpenAPI document: 0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, conlist
from sds_client.models.collector import Collector

class MultiResponseCollector(BaseModel):
    """
    MultiResponseCollector
    """
    total: StrictInt = Field(...)
    search_after: Optional[StrictInt] = None
    collectors: conlist(Collector) = Field(...)
    __properties = ["total", "search_after", "collectors"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MultiResponseCollector:
        """Create an instance of MultiResponseCollector from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in collectors (list)
        _items = []
        if self.collectors:
            for _item in self.collectors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collectors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MultiResponseCollector:
        """Create an instance of MultiResponseCollector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MultiResponseCollector.parse_obj(obj)

        _obj = MultiResponseCollector.parse_obj({
            "total": obj.get("total"),
            "search_after": obj.get("search_after"),
            "collectors": [Collector.from_dict(_item) for _item in obj.get("collectors")] if obj.get("collectors") is not None else None
        })
        return _obj


