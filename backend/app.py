
import os

from flask import Flask, jsonify, request
from src.storage import add_task, list_tasks

app = Flask(__name__)

TASKS_FILE = os.environ.get("TASKS_FILE", "tasks.json")


@app.get("/api/tasks")
def get_tasks():
    tasks = list_tasks(TASKS_FILE)
    return jsonify(tasks)


@app.post("/api/tasks")
def create_task():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected JSON object"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Title is required"}), 400

    task = add_task(title.strip(), TASKS_FILE)
    return jsonify(task), 201
