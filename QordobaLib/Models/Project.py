# -*- coding: utf-8 -*-

"""
   QordobaLib.Models.Project
 
     by Qordoba BETA v2.0 on 02/25/2016
"""
from QordobaLib.APIHelper import APIHelper
from QordobaLib.Models.MilestoneLanguage import MilestoneLanguage
from QordobaLib.Models.StringFile import StringFile

class Project(object):

    """Implementation of the 'Project' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        source_language (int): TODO: type description here.
        content_type (int): TODO: type description here.
        organization_id (string): TODO: type description here.
        target_languages (list of int): TODO: type description here.
        milestones (list of MilestoneLanguage): TODO: type description here.
        string_files (list of StringFile): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Project class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    name -- string -- Sets the attribute name
                    source_language -- int -- Sets the attribute source_language
                    content_type -- int -- Sets the attribute content_type
                    organization_id -- string -- Sets the attribute organization_id
                    target_languages -- list of int -- Sets the attribute target_languages
                    milestones -- list of MilestoneLanguage -- Sets the attribute milestones
                    string_files -- list of StringFile -- Sets the attribute string_files
        
        """
        # Set all of the parameters to their default values
        self.name = None
        self.source_language = None
        self.content_type = None
        self.organization_id = None
        self.target_languages = None
        self.milestones = None
        self.string_files = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "name": "name",
            "source_language": "source_language",
            "content_type": "content_type",
            "organization_id": "organization_id",
            "target_languages": "target_languages",
            "milestones": "milestones",
            "string_files": "string_files",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "milestones" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.milestones = list()
                for item in kwargs["milestones"]:
                    self.milestones.append(MilestoneLanguage(**item))

            # Other objects also need to be initialised properly
            if "string_files" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.string_files = list()
                for item in kwargs["string_files"]:
                    self.string_files.append(StringFile(**item))

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
            "name": "name",
            "source_language": "source_language",
            "content_type": "content_type",
            "organization_id": "organization_id",
            "target_languages": "target_languages",
            "milestones": "milestones",
            "string_files": "string_files",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)