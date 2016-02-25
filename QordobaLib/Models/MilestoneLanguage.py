# -*- coding: utf-8 -*-

"""
   QordobaLib.Models.MilestoneLanguage
 
     by Qordoba BETA v2.0 on 02/25/2016
"""
from QordobaLib.APIHelper import APIHelper
from QordobaLib.Models.Milestone import Milestone
from QordobaLib.Models.Language import Language

class MilestoneLanguage(object):

    """Implementation of the 'MilestoneLanguage' model.

    TODO: type model description here.

    Attributes:
        milestone (Milestone): TODO: type description here.
        languages (list of Language): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the MilestoneLanguage class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    milestone -- Milestone -- Sets the attribute milestone
                    languages -- list of Language -- Sets the attribute languages
        
        """
        # Set all of the parameters to their default values
        self.milestone = None
        self.languages = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "milestone": "milestone",
            "languages": "languages",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "milestone" in kwargs:
                self.milestone = Milestone(**kwargs["milestone"])

            # Other objects also need to be initialised properly
            if "languages" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.languages = list()
                for item in kwargs["languages"]:
                    self.languages.append(Language(**item))

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
            "milestone": "milestone",
            "languages": "languages",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)