---
title: Python SDK for l10n
layout: api
---

# Python SDK

Qordoba’s Python SDK offers platform-specific features that make the Qordoba API implementation much simpler. The SDK allows you to integrate our API with your application without worrying about low-level API details. Our Python SDK is open-source and can be forked at the link below. Once forked and configured, you will be able to easily integrate our API into your application.

### Get the SDK:

Download the Python API SDK from [GitHub](https://github.com/Qordobacode/api-sdk-python).

To clone the repo: `git clone git@github.com:Qordobacode/api-sdk-python.git`.



###How to install via PIP: 

* From terminal/cmd navigate to the root directory
* Invoke `'pip install -r requirements.txt'`
* Create a "QordobaControllerTest.py" file in the root directory
* Add the following import statement:
        `'from QordobaLib.Controllers.QordobaController import *'`
* Create a new instance using `'controller = QordobaController()'`
* Invoke an endpoint with the appropriate parameters, for example:
        `'response = controller.create_projects(<required parameters if any>)'`
* `response` will now be an object of type Void.

The SDK uses the Python libraries [UniRest](http://unirest.io/python.html) and [Jsonpickle](https://jsonpickle.github.io/). 

### Bug reports
Have a bug? Please create an issue [here](https://github.com/Qordobacode/api-sdk-python/issues) on GitHub! 




### License
The MIT License (MIT)

