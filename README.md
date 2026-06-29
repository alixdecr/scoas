# SCOAS: Status Code Analysis in OpenAPI Specifications

![Version](https://img.shields.io/badge/Version-1.1-green)
![Python](https://img.shields.io/badge/Python-v3.12-blue)
![OAS](https://img.shields.io/badge/OAS-v3.2.0-blue)
![Status Code Rules](https://img.shields.io/badge/Status%20Code%20Rules-30-purple)

SCOAS is a static analysis tool capable of detecting HTTP status code misuses in REST API specifications (OpenAPI Specification format). Below, you may find instructions for **Citation**, **Installation**, and a complete list of **Status Code Usage Rules** that are implemented in the tool.

## Citation

If you use this tool in your research or find it useful in your work, please cite our paper:

Decrop, A., Papadakis, M. and Perrouin, G. 2026. Analyzing Status Code Misuses in REST API Specifications. In Proceedings of the 26th International Conference on Web Engineering, ICWE 2026.

```bibtex
@inproceedings{decrop2026analyzing,
    title={Analyzing Status Code Misuses in REST API Specifications},
    author={Decrop, Alix and Papadakis, Mike and Perrouin, Gilles},
    booktitle={Proceedings of the 26th International Conference on Web Engineering, ICWE 2026},
    year={2026}
}
```

## Installation

To install and use the tool, you can follow the instructions below.

### 1. Clone the Repository

First, clone the repository of the tool and navigate to it with:

```bash
git clone https://github.com/alixdecr/scoas
cd <your-repository-folder>
```

### 2. Create a Virtual Environment

To use the tool, a Python virtual environment is recommended to avoid messing up your main Python interpreter. To do so, execute the following command in your repository folder:

```bash
python -m venv .venv
```

Which will create a Python virtual environment in the `.venv` folder. Depending on your Python installation and operation system, you might need to replace `python` with `py`, `python3`, or something else.

### 3. Activate the Virtual Environment

To activate the newly created virtual environment, execute the following command depending on your operating system:

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

##### CMD

```bash
.venv\Scripts\activate.bat
```

##### PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### 4. Install the Requirements

Before using the tool, you must upgrade pip and install the requirements using:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Execute the Tool

After installation, you can execute the tool with the following command:

```bash
python src/main.py
```

Steps 4 and 5 need to be done with the virtual environment activated (which should be the case if you followed step 3 correctly).

## Using the Tool

### 1. OAS File Folder

To execute SCOAS on OpenAPI Specifications, insert their files (must be in JSON `.json` format) in the `data/oas` folder. If for any reason you wish to use another OAS folder, modify the `OAS_PATH` variable located in `src/config.py`.

### 2. Execute the Tool

Execute the tool with the following command:

```bash
python src/main.py
```

### 3. Visualize Results

Once the execution is finished, you will be able to visualize the following:

- The execution logs, located in the `logs` folder.
- The execution raw data, located in the `outputs/<oas-name>/execution.json` file.
- The execution report, located in the `outputs/<oas-name>/report.html` file.


### 4. Fix the Status Code Misuses

After analyzing the execution report, feel free to modify your OpenAPI Specification based on the rule violations that were identified.

## Status Code Usage Rules

Below, you can find an exhaustive list of all implemented status code usage rules, their descriptions, and sources. Rules that were recently added are preceded by a **(new)** tag. There are currently **30** implemented status code usage rules.

| Rule Identifier | Description | Sources |
| --------------- | ----------- | ------- |
| has-200-if-get | Always implement a response with the status code `200 OK` in a `GET` method. | RFC 9110, Section 15.3.1 (200 OK), RFC 9110, Section 9.3.1 (GET) |
| has-200-or-201-or-204-if-post | Always implement a response with the status code `200 OK`, `201 Created`, or `204 No Content` in a `POST` method. | RFC 9110, Section 15.3.1 (200 OK), RFC 9110, Section 15.3.2 (201 Created), RFC 9110, Section 15.3.5 (204 No Content), RFC 9110, Section 9.3.3 (POST) |
| has-200-or-201-or-204-if-put | Always implement a response with the status code `200 OK`, `201 Created`, or `204 No Content` in a `PUT` method. | RFC 9110, Section 15.3.1 (200 OK), RFC 9110, Section 15.3.2 (201 Created), RFC 9110, Section 15.3.5 (204 No Content), RFC 9110, Section 9.3.4 (PUT) |
| has-200-or-204-if-delete | Always implement a response with the status code `200 OK` or `204 No Content` in a `DELETE` method. | RFC 9110, Section 15.3.1 (200 OK), RFC 9110, Section 15.3.5 (204 No Content), RFC 9110, Section 9.3.5 (DELETE) |
| has-200-or-204-if-patch | Always implement a response with the status code `200 OK` or `204 No Content` in a `PATCH` method. | RFC 9110, Section 15.3.1 (200 OK), RFC 9110, Section 15.3.5 (204 No Content), RFC 5789 (PATCH Method for HTTP) |
| has-204-if-no-content | Always implement a response with the status code `204 No Content` if a response in the `2xx Successful` range does not have content. | RFC 9110, Section 15.3.5 (204 No Content), RFC 9110, Section 15.3 (Successful 2xx) |
| has-400-if-params | Always implement a response with the status code `400 Bad Request` if the method contains parameters (in case of invalid syntax). | RFC 9110, Section 15.5.1 (400 Bad Request) |
| has-400-if-payload | Always implement a response with the status code `400 Bad Request` if the method contains a payload (in case of invalid syntax). | RFC 9110, Section 15.5.1 (400 Bad Request) |
| has-404-if-path | Always implement a response with the status code `404 Not Found` if the method contains path parameters. | RFC 9110, Section 15.5.5 (404 Not Found) |
| has-406-if-accept | Always implement a response with the status code `406 Not Acceptable` in case the sever does not support the `Accept` header specified in the request. Only applies to routes that respond with content. | RFC 9110, Section 15.5.7 (406 Not Acceptable), RFC 9110, Section 12.5.1 (Accept) |
| has-413-if-content-length | Always implement a response with the status code `413 Content Too Large` in case the server does not support the `Content-Length` header specified in the request. | RFC 9110, Section 15.5.14 (413 Content Too Large), RFC 9110, Section 8.6 (Content-Length) |
| has-415-if-content-type | Always implement a response with the status code `415 Unsupported Media Type` in case the server does not support the `Content-Type` header specified in the request. | RFC 9110, Section 15.5.16 (415 Unsupported Media Type), RFC 9110, Section 8.3 (Content-Type) |
| has-422-if-params | Always implement a response with the status code `422 Unprocessable Content` if the method contains parameters (in case of invalid semantics). | RFC 9110, Section 15.5.21 (422 Unprocessable Content) |
| has-422-if-payload | Always implement a response with the status code `422 Unprocessable Content` if the method contains a payload (in case of invalid semantics). | RFC 9110, Section 15.5.21 (422 Unprocessable Content) |
| no-200-if-error | Never implement a response with the status code `200 OK` if the response content describes an error. | RFC 9110, Section 15.3.1 (200 OK) |
| no-201-if-delete | Never implement a response with the status code `201 Created` in a `DELETE` method (as it can never create data). | RFC 9110, Section 15.3.2 (201 Created), RFC 9110, Section 9.3.5 (DELETE) |
| no-201-if-get | Never implement a response with the status code `201 Created` in a `GET` method (as it can never create data). | RFC 9110, Section 15.3.2 (201 Created), RFC 9110, Section 9.3.1 (GET) |
| no-201-if-patch | Never implement a response with the status code `201 Created` in a `PATCH` method (as it can never create data). | RFC 9110, Section 15.3.2 (201 Created), RFC 5789 (PATCH Method for HTTP) |
| no-204-if-content | Never implement a response with the status code `204 No Content` if its content is not empty. In the case of an OAS file, the response should not have a `content` field. | RFC 9110, Section 15.3.5 (204 No Content) |
| **(new)** no-205-if-content | Never implement a response with the status code `205 Reset Content` if its content is not empty. In the case of an OAS file, the response should not have a `content` field. | RFC 9110, Section 15.3.6 (205 Reset Content) |
| **(new)** no-304-if-no-get-or-head | Never implement a response with the status code `304 Not Modified` if the request method is not `GET` or `HEAD`. | RFC 9110, Section 15.4.5 (304 Not Modified), RFC 9110, Section 9.3.1 (GET), RFC 9110, Section 9.3.2 (HEAD) |
| no-401-if-no-auth | Never implement a response with the status code `401 Unauthorized` if the specification does not contains an authentication mechanism. | RFC 9110, Section 15.5.2 (401 Unauthorized) |
| **(new)** no-401-if-no-authenticate | Never implement a response with the status code `401 Unauthorized` if it does not return a `WWW-Authenticate` header. | RFC 9110, Section 15.5.2 (401 Unauthorized), RFC 9110, Section 11.6.1 (WWW-Authenticate) |
| no-403-if-no-401 | Never implement a response with the status code `403 Forbidden` if the method does not implement a response with the status code `401 Unauthorized`. | RFC 9110, Section 15.5.4 (403 Forbidden), RFC 9110, Section 15.5.2 (401 Unauthorized) |
| **(new)** no-405-if-no-allow | Never implement a response with the status code `405 Method Not Allowed` if it does not return an `Allow` header. | RFC 9110, Section 15.5.6 (405 Method Not Allowed), RFC 9110, Section 10.2.1 (Allow) |
| no-413-if-no-payload | Never implement a response with the status code `413 Content Too Large` if the method does not contain a payload. | RFC 9110, Section 15.5.14 (413 Content Too Large) |
| no-415-if-no-payload | Never implement a response with the status code `415 Unsupported Media Type` if the method does not contain a payload. | RFC 9110, Section 15.5.16 (415 Unsupported Media Type) |
| **(new)** no-426-if-no-upgrade | Never implement a response with the status code `426 Upgrade Required` if it does not return an `Upgrade` header. | RFC 9110, Section 15.5.22 (426 Upgrade Required), RFC 9110, Section 7.8 (Upgrade) |
| **(new)** no-501-if-implemented | Never implement a response with the status code `501 Not Implemented` if the request method is actually implemented. In the case of an OAS file, the code should not appear at all. | RFC 9110, Section 15.6.2 (501 Not Implemented) |
| no-non-standard-codes | Never implement responses with non-standard status codes. | RFC 9110, Section 15 (Status Codes), OpenAPI `default` response |