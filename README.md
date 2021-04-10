<h1 align="center">API Documentation</h1>

<pre><b>Technologies Used</b>
•	Python 3.8
•	Django 3.1.7
•	Django Rest framework 3.12.2
•	Pythonanywhere (backend deployment)
•	Mysql (Database)
<b>Allowed HTTPs request:</b>
o	PUT       : To create resource
o	POST     : Update resource
o	GET       : Get a resource or list of resources
o	DELETE : To delete resource
<b>Deployment link</b>
abhijeetkr0202.pythonanywhere.com

<b>Restful API</b>
•	Create new user
POST       abhijeetkr0202.pythonanywhere.com

•	Get all users
GET        abhijeetkr0202.pythonanywhere.com

•	Get a particular user based on user_id
    GET       abhijeetkr0202.pythonanywhere.com/user_id/info

•	Modify user details based on user_id
PUT           abhijeetkr0202.pythonanywhere.com/user_id/info

•	Delete a user
DELETE     abhijeetkr0202.pythonanywhere.com/<id>/info

•	Export all user details to CSV
GET            abhijeetkr0202.pythonanywhere.com/export





<b>Description Of Usual Server Responses:</b>
•	200 OK - the request was successful (some API calls may return 201 instead).
•	201 Created - the request was successful and a resource was created.
•	204 No Content - the request was successful but there is no representation to return 
•	400 Bad Request - the request could not be understood or was missing required parameters.
•	403 Forbidden - access denied.
•	404 Not Found - resource was not found.
•	405 Method Not Allowed - requested method is not supported for resource.


<b>Model [Userdata] fields</b>
•	Id
•	Name
•	Age
•	Contact
•	Address

 </pre>
 





