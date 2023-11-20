from flask import Flask, request, jsonify

app = Flask(__name__)

def import_tasks(filename="tasks.txt"):
    # Imports tasks from a text file
    imported_tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                task_data = line.strip().split(',')
                task_name, task_date, task_note, task_completed = task_data
                task_completed = task_completed.lower() == 'true'
                imported_tasks.append((task_name, task_date, task_note, task_completed))
    except FileNotFoundError:
        print(f"File {filename} not found. Returning an empty list.")
    return imported_tasks

def export_tasks(tasks, filename="tasks.txt"):
    # Exports tasks to a text file
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task[0]},{task[1]},{task[2]},{task[3]}\n")

@app.route("/import_tasks", methods=["GET"])
def get_import_tasks():
    # API endpoint for importing tasks
    tasks = import_tasks()
    return jsonify({"tasks": tasks})

@app.route("/export_tasks", methods=["POST"])
def post_export_tasks():
    # API endpoint for exporting tasks
    tasks = request.json.get("tasks")
    export_tasks(tasks)
    return jsonify({"message": "Tasks exported successfully"})

if __name__ == "__main__":
    app.run(port=5001)
