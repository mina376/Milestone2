*The code in TaskManagementSystem.py has been changed a bit from the original code. Some code has been added, but some code has been removed because some features did not work on the Mac.


# **Request Data**
To make a request to the task management microservice, use the “/import_tasks” endpoint. It involves sending an HTTP GET request to the microservice's URL and port. The response will contain the tasks stored in the microservice in JSON format.

This is an example call using Python with the requests library:
```
import requests

def import_tasks_from_microservice():
    response = requests.get("http://localhost:5001/import_tasks")
    data = response.json()
    return data["tasks"]
```

# **Receive Data**
To receive data from the task management microservice, utilize the “/export_tasks” endpoint. It requires sending an HTTP POST request to the microservice's URL and port, including the tasks in the request body as a JSON object.

This is an example call using Python with the requests library:
```
def export_tasks_to_microservice(tasks):
    payload = {"tasks": tasks}
    response = requests.post("http://localhost:5001/export_tasks", json=payload)
    data = response.json()
    print(data["message"])
```

# **UML sequence diagram**
<img width="479" alt="スクリーンショット 2023-11-20 20 56 01" src="https://github.com/mina376/Milestone2/assets/114086158/e0dfd14c-f91d-4ef1-b3fe-a1251faaecf2">
