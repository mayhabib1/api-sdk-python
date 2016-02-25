# -*- coding: utf-8 -*-

"""
   QordobaLib.Models.StringFile
 
     by Qordoba BETA v2.0 on 02/25/2016
"""
from QordobaLib.APIHelper import APIHelper

class StringFile(object):

    """Implementation of the 'StringFile' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        file_name (string): TODO: type description here.
        file_type (string): TODO: type description here.
        source_columns (list of int): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the StringFile class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    id -- string -- Sets the attribute id
                    file_name -- string -- Sets the attribute file_name
                    file_type -- string -- Sets the attribute file_type
                    source_columns -- list of int -- Sets the attribute source_columns
        
        """
        # Set all of the parameters to their default values
        self.id = None
        self.file_name = None
        self.file_type = None
        self.source_columns = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "id": "id",
            "file_name": "file_name",
            "file_type": "file_type",
            "source_columns": "source_columns",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the  dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "id": "id",
            "file_name": "file_name",
            "file_type": "file_type",
            "source_columns": "source_columns",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)