#!/usr/bin/python3
"""
The base model
Base class of all the classes in the project.
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes of an instance:
            random uuid, dates created/updated.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at':
                    setattr(
                        self,
                        k,
                        datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    )
                elif k == 'updated_at':
                    setattr(
                        self,
                        k,
                        datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    )
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return the string info about model."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update instance with updated time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns the __dict__ of the instance."""
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
