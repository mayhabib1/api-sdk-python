# -*- coding: utf-8 -*-

"""
   QordobaLib.Models.Milestone
 
     by Qordoba BETA v2.0 on 02/25/2016
"""
from QordobaLib.APIHelper import APIHelper

class Milestone(object):

    """Implementation of the 'Milestone' model.

    TODO: type model description here.

    Attributes:
        milestone_id (int): TODO: type description here.
        name (string): TODO: type description here.
        order (int): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Milestone class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    milestone_id -- int -- Sets the attribute milestone_id
                    name -- string -- Sets the attribute name
                    order -- int -- Sets the attribute order
        
        """
        # Set all of the parameters to their default values
        self.milestone_id = None
        self.name = None
        self.order = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "milestone_id": "milestone_id",
            "name": "name",
            "order": "order",
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
            "milestone_id": "milestone_id",
            "name": "name",
            "order": "order",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)