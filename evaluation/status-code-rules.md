# Complete List of Status Code Usage Rules

`Has200IfGet`: Always implement a response with the status code '200 OK' in a 'GET' method.

`Has200Or201Or204IfPost`: Always implement a response with the status code '200 OK', '201 Created', or '204 No Content' in a 'POST' method.

`Has200Or201Or204IfPut`: Always implement a response with the status code '200 OK', '201 Created', or '204 No Content' in a 'PUT' method.

`Has200Or204IfDelete`: Always implement a response with the status code '200 OK' or '204 No Content' in a 'DELETE' method.

`Has200Or204IfPatch`: Always implement a response with the status code '200 OK' or '204 No Content' in a 'PATCH' method.

`Has204IfNoContent`: Always implement a response with the status code '204 No Content' if a response in the '2xx Successful' range does not have content.

`Has400IfParams`: Always implement a response with the status code '400 Bad Request' if the method contains parameters (in case of invalid syntax).

`Has400IfPayload`: Always implement a response with the status code '400 Bad Request' if the method contains a payload (in case of invalid syntax).

`Has404IfPath`: Always implement a response with the status code '404 Not Found' if the method contains path parameters.

`Has406IfAccept`: Always implement a response with the status code '406 Not Acceptable' in case the sever does not support the 'Accept' header specified in the request. Only applies to routes that respond with content.

`Has413IfContentLength`: Always implement a response with the status code '413 Content Too Large' in case the server does not support the 'Content-Length' header specified in the request.

`Has415IfContentType`: Always implement a response with the status code '415 Unsupported Media Type' in case the server does not support the 'Content-Type' header specified in the request.

`Has422IfParams`: Always implement a response with the status code '422 Unprocessable Content' if the method contains parameters (in case of invalid semantics).

`Has422IfPayload`: Always implement a response with the status code '422 Unprocessable Content' if the method contains a payload (in case of invalid semantics).

`No200IfError`: Never implement a response with the status code '200 OK' if the response content describes an error.

`No201IfDelete`: Never implement a response with the status code '201 Created' in a 'DELETE' method (as it can never create data).

`No201IfGet`: Never implement a response with the status code '201 Created' in a 'GET' method (as it can never create data).

`No201IfPatch`: Never implement a response with the status code '201 Created' in a 'PATCH' method (as it can never create data).

`No204IfContent`: Never implement a response with the status code '204 No Content' if its content is not empty. In the case of an OAS file, the response should not have a 'content' field.

`No401IfNoAuth`: Never implement a response with the status code '401 Unauthorized' if the specification does not contains an authentication mechanism.

`No403IfNo401`: Never implement a response with the status code '403 Forbidden' if the method does not implement a response with the status code '401 Unauthorized'.

`No413IfNoPayload`: Never implement a response with the status code '413 Content Too Large' if the method does not contain a payload.

`No415IfNoPayload`: Never implement a response with the status code '415 Unsupported Media Type' if the method does not contain a payload.

`NoNonStandardCodes`: Never implement responses with non-standard status codes.