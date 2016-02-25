QordobaLib
=================
Qordoba’s Java SDK offers platform-specific features that make the Qordoba implementation much simpler. The SDKs are open-source, and can be forked at the links below. Once forked, you can integrate our API into your application.

Due to the UniRest package dependency this SDK only works under Python 2.7
It will not work using Python 3.x

How To Configure:
=================
The code might need to be configured with your API credentials. To do that,
provide the credentials and configuration values as constructor parameters for the controllers

How To Build: 
=============
The code uses Python libraries named UniRest and Jsonpickle. 

PIP is a popular tool for managing python packages[1].
To resolve these packages:
1) From terminal/cmd navigate to the root directory
2) Invoke 'pip install -r requirements.txt'

Note: You will need internet access to resolve these dependencies.

How To Use:
===========
The following shows how to make invoke the QordobaController controller.
It is also shown in [2].

    1. Create a "QordobaControllerTest.py" file in the root directory.
    2. Add the following import statement 
        'from QordobaLib.Controllers.QordobaController import *'
    3. Create a new instance using 'controller = QordobaController()'
    4. Invoke an endpoint with the appropriate parameters, for example
        'response = controller.create_projects(<required parameters if any>)'
    5. "response" will now be an object of type Void.

[1] PIP - https://pip.pypa.io

[2] from QordobaLib.Controllers.QordobaController import *

	controller = QordobaController()
    response = controller.create_projects()

    print response
