# API

### what are API's?
**Application Programming Interface** allows two servers to communicate with each others. The reason it is popular because 
APIs are used for various purposes, but their primary function is to enable seamless integration and interoperability between different software systems.

<img src="D:\Python project\Tech 241\python_and_api\APi.png"/>

### HTTP GET, POST, PUT, PATCH, DELETE
**Hypertext Transfer Protocol** allows to transport data between a client and a server

**Get** is used to get data from a server

**Post** is used to send data to the server and request for the server to create information based on the body of the HTTP request

**Put** is used to update or create a resource

**Patch** is used to update the information of the server and apply a partial modification

**delete** is used to delete a particular information on the server

### HTTP request structure

**_Verb_** - a set of request methods

**_URL_** - a Uniform Resource Locator

**_Version_** - defines the structure of the remain message

**_Header_** - allows additional data key/values pair to be passed between the client and the server

**_Body_** - the servers uses a body to create a message and send it back to the client

<img src="D:\Python project\Tech 241\python_and_api\http_request_structure.png.jpg"/> 

### HTTP Response Structure 
**_Respond code -_** a three digit number which indicating the result of the request

**_HTTP version_** - showing the HTTP version used for the response

**_Header_** - key/value pairs that provides information about the response

**_Body_** - contains the content that is sent to the client from the server

<img src="D:\Python project\Tech 241\python_and_api\http_response_structure.jpg"/>


### What is statelessness?
**Statelessness** is when API does not depend on the previous requests before able to process new requests.

#### What is caching?
**Caching** is a process of storing the response of an API request and respond it from the caching instead making a new request.
