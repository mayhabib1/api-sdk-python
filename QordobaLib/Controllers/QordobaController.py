# -*- coding: utf-8 -*-

"""
   QordobaLib.Controllers.QordobaController

     by Qordoba BETA v2.0 on 02/25/2016
"""
import unirest

from QordobaLib.APIHelper import APIHelper
from QordobaLib.Configuration import Configuration
from QordobaLib.APIException import APIException


class QordobaController(object):


    """A Controller to access Endpoints in the QordobaLib API."""

    def __init__(self,
                 basic_auth_user_name,
                 basic_auth_password):
        """
        Constructor with authentication and configuration parameters
        """
        self.__basic_auth_user_name = basic_auth_user_name
        self.__basic_auth_password = basic_auth_password

    def create_projects(self,
                        body):
        """Does a POST request to /api/projects.

        Creates a new project

        Args:
            body (Project): Project creation payload

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "content-type": "application/json; charset=utf-8",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers,  params=APIHelper.json_serialize(body), auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_projects(self):
        """Does a GET request to /api/projects.

        Gets an organisation's projects

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_workflow(self):
        """Does a GET request to /api/workflows.

        Gets organisation workflows

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/workflows"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_workflow(self,
                     wf_id):
        """Does a GET request to /api/workflows/{wf_id}.

        Gets a workflow

        Args:
            wf_id (string): Your workflow ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/workflows/{wf_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "wf_id": wf_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_team(self,
                 filter_query,
                 limit,
                 offset):
        """Does a GET request to /api/team.

        Gets an organisation's team

        Args:
            filter_query (string): Your filter string
            limit (string): Your pagination limit
            offset (string): Your pagination offset

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/team"

        # Process optional query parameters
        query_parameters = {
            "filterQuery": filter_query,
            "limit": limit,
            "offset": offset
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_workflow(self,
                     language_id,
                     project_id):
        """Does a GET request to /api/projects/{project_id}/languages/{language_id}/workflow.

        Gets a project's workflow

        Args:
            language_id (string): Your language ID
            project_id (string): Your project ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/languages/{language_id}/workflow"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "language_id": language_id,
            "project_id": project_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_workflow(self,
                     mfrom,
                     limit,
                     project_id):
        """Does a GET request to /api/projects/{project_id}/feed.

        Gets an project's feed

        Args:
            mfrom (string): Feed source
            limit (string): Your pagination limit
            project_id (string): Your project ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/feed"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "project_id": project_id
        })

        # Process optional query parameters
        query_parameters = {
            "from": mfrom,
            "limit": limit
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_files(self,
                  language_id,
                  limit,
                  offset,
                  project_id,
                  search_string):
        """Does a GET request to /api/projects/{project_id}/languages/{language_id}/files.

        Gets project's files

        Args:
            language_id (string): Your language ID
            limit (string): Your pagination limit
            offset (string): Your pagination offset
            project_id (string): Your project ID
            search_string (string): Your search string

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/languages/{language_id}/files"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "language_id": language_id,
            "project_id": project_id
        })

        # Process optional query parameters
        query_parameters = {
            "limit": limit,
            "offset": offset,
            "search_string": search_string
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_files(self,
                     project_id):
        """Does a POST request to /api/projects/{project_id}/files.

        Uploads a project file

        Args:
            project_id (string): Your project ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/files"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "project_id": project_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_files(self,
                  file_id,
                  language_id,
                  project_id):
        """Does a GET request to /api/projects/{project_id}/languages/{language_id}/files/{file_id}.

        Downloads a project's file

        Args:
            file_id (string): Your file ID
            language_id (string): Your language ID
            project_id (string): Your project ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/languages/{language_id}/files/{file_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "file_id": file_id,
            "language_id": language_id,
            "project_id": project_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_segments(self,
                     file_id,
                     filter,
                     language_id,
                     limit,
                     offset,
                     project_id,
                     search_string):
        """Does a GET request to /api/projects/{project_id}/languages/{language_id}/files/{file_id}/segments.

        Gets a file's segments

        Args:
            file_id (string): Your file ID
            filter (string): Your filter string
            language_id (string): Your language ID
            limit (string): Your pagination limit
            offset (string): Your pagination offset
            project_id (string): Your project ID
            search_string (string): Your search string

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/languages/{language_id}/files/{file_id}/segments"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "file_id": file_id,
            "language_id": language_id,
            "project_id": project_id
        })

        # Process optional query parameters
        query_parameters = {
            "filter": filter,
            "limit": limit,
            "offset": offset,
            "search_string": search_string
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_segments(self,
                     file_id,
                     language_id,
                     project_id,
                     segment_id):
        """Does a GET request to /api/projects/{project_id}/languages/{language_id}/files/{file_id}/segments/{segment_id}.

        Gets a segment

        Args:
            file_id (string): Your file ID
            language_id (string): Your language ID
            project_id (string): Your project ID
            segment_id (string): Your segment ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/languages/{language_id}/files/{file_id}/segments/{segment_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "file_id": file_id,
            "language_id": language_id,
            "project_id": project_id,
            "segment_id": segment_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def update_segments(self,
                        file_id,
                        language_id,
                        project_id,
                        segment_id):
        """Does a PUT request to /api/projects/{project_id}/languages/{language_id}/files/{file_id}/segments/{segment_id}.

        Updates a segment

        Args:
            file_id (string): Your file ID
            language_id (string): Your language ID
            project_id (string): Your project ID
            segment_id (string): Your segment ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/languages/{language_id}/files/{file_id}/segments/{segment_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "file_id": file_id,
            "language_id": language_id,
            "project_id": project_id,
            "segment_id": segment_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.put(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def create_files(self,
                     body,
                     file_id,
                     project_id):
        """Does a POST request to /api/projects/{project_id}/files/{file_id}/segments.

        Adds segments to a file

        Args:
            body (Project): Project creation payload
            file_id (string): Your file ID
            project_id (string): Your project ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/files/{file_id}/segments"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "file_id": file_id,
            "project_id": project_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "content-type": "application/json; charset=utf-8",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers,  params=APIHelper.json_serialize(body), auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def create_files(self,
                     file_name,
                     project_id):
        """Does a POST request to /api/projects/{project_id}/files/{file_name}.

        Creates an empty file

        Args:
            file_name (string): Your file name
            project_id (string): Your project ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/projects/{project_id}/files/{file_name}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "file_name": file_name,
            "project_id": project_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_tm(self):
        """Does a GET request to /api/translation_memories.

        Gets an organisation's translation memory

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_tm(self):
        """Does a POST request to /api/translation_memories/upload.

        Posts an organisation's translation memory

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/upload"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_tm(self,
               tm_id):
        """Does a GET request to /api/translation_memories/{tm_id}/config.

        Gets a translation memory config

        Args:
            tm_id (string): Your translation memory ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/{tm_id}/config"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "tm_id": tm_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def update_tm(self,
                  tm_id):
        """Does a PUT request to /api/translation_memories/{tm_id}/config.

        Updates a translation memory config

        Args:
            tm_id (string): Your translation ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/{tm_id}/config"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "tm_id": tm_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.put(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_tm(self,
               tm_id):
        """Does a GET request to /api/translation_memories/{tm_id}.

        Gets a translation memory

        Args:
            tm_id (string): Your translation memory ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/{tm_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "tm_id": tm_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_tm(self,
               tm_id):
        """Does a GET request to /api/translation_memories/{tm_id}/segments.

        Gets a translation memory's segments

        Args:
            tm_id (string): Your translation memory ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/{tm_id}/segments"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "tm_id": tm_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_tm(self):
        """Does a POST request to /api/translation_memories/add_term.

        Posts a translation memory's term

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/add_term"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_tm(self,
               id,
               tm_id):
        """Does a GET request to /api/translation_memories/{tm_id}/segments/{id}.

        Gets a translation memory's segment

        Args:
            id (string): Your segment ID
            tm_id (string): Your translation memory ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/{tm_id}/segments/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "id": id,
            "tm_id": tm_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def update_tm(self,
                  id,
                  tm_id):
        """Does a PUT request to /api/translation_memories/{tm_id}/segments/{id}.

        Updates a translation memory's segment

        Args:
            id (string): Your segment ID
            tm_id (string): Your translation memory ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/{tm_id}/segments/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "id": id,
            "tm_id": tm_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.put(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def delete_tm(self,
                  id,
                  tm_id):
        """Does a DELETE request to /api/translation_memories/{tm_id}/segments/{id}.

        Deletes a translation memory's segment

        Args:
            id (string): Your segment ID
            tm_id (string): Your translation memory ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/translation_memories/{tm_id}/segments/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "id": id,
            "tm_id": tm_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.delete(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_glossaries(self):
        """Does a GET request to /api/glossaries.

        Gets organization's glossaries

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_glossaries(self):
        """Does a POST request to /api/glossaries/upload.

        Posts an organization glossary

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/upload"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_glossaries(self,
                       glossary_id):
        """Does a GET request to /api/glossaries/{glossary_id}/config.

        Gets a glossary's config

        Args:
            glossary_id (string): Your glossary ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/{glossary_id}/config"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "glossary_id": glossary_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def update_glossaries(self,
                          glossary_id):
        """Does a PUT request to /api/glossaries/{glossary_id}/config.

        Updates a glossary's config

        Args:
            glossary_id (string): Your glossary ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/{glossary_id}/config"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "glossary_id": glossary_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.put(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_glossaries(self,
                       glossary_id):
        """Does a GET request to /api/glossaries/{glossary_id}/download.

        Downloads a glossary

        Args:
            glossary_id (string): Your glossary ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/{glossary_id}/download"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "glossary_id": glossary_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_glossaries(self,
                       glossary_id):
        """Does a GET request to /api/glossaries/{glossary_id}.

        Gets a glossary

        Args:
            glossary_id (string): Your glossary ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/{glossary_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "glossary_id": glossary_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_glossaries(self,
                       language_id,
                       project_id):
        """Does a GET request to /api/project/{project_id}/languages/{language_id}/glossaries/terms.

        Gets project glossaries

        Args:
            language_id (string): Your language ID
            project_id (string): Your project ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/project/{project_id}/languages/{language_id}/glossaries/terms"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "language_id": language_id,
            "project_id": project_id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def create_glossaries(self):
        """Does a POST request to /api/glossaries/add_term.

        Posts glossary term

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/add_term"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.post(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_glossaries(self,
                       glossary_id,
                       id):
        """Does a GET request to /api/glossaries/{glossary_id}/terms/{id}.

        Gets glossary term

        Args:
            glossary_id (string): Your glossary ID
            id (string): Your glossary term ID

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/{glossary_id}/terms/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "glossary_id": glossary_id,
            "id": id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def update_glossaries(self,
                          glossary_id,
                          id):
        """Does a PUT request to /api/glossaries/{glossary_id}/terms/{id}.

        Updates glossary term

        Args:
            glossary_id (string): Your glossary ID
            id (string): Your glossary term ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/{glossary_id}/terms/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "glossary_id": glossary_id,
            "id": id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.put(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def delete_glossaries(self,
                          glossary_id,
                          id):
        """Does a DELETE request to /api/glossaries/{glossary_id}/terms/{id}.

        Deletes glossary term

        Args:
            glossary_id (string): Your glossary ID
            id (string): Your glossary term ID

        Returns:
            void: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/glossaries/{glossary_id}/terms/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "glossary_id": glossary_id,
            "id": id
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.delete(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    

    def get_languages(self):
        """Does a GET request to /api/languages.

        Gets languages

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/languages"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_languages(self):
        """Does a GET request to /api/countries.

        Gets countries

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/countries"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body

    def get_regextemplates(self):
        """Does a GET request to /api/regextemplates.

        Gets regex templates

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/api/regextemplates"

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {

            "user-agent": "Qordoba 2.0",
            "accept": "application/json",

        }

        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers, params={}, auth=(self.__basic_auth_user_name, self.__basic_auth_password))

        # Error handling using HTTP status codes
        if response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body) 
    
        return response.body
