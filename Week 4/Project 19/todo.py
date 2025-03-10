import json
import datetime
import argparse

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w")  as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": " ".join(description) if isinstance(description, list) else description,
        "status": "pending",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("✅ Task added Successfully!")

# View tasks
def view_tasks(status=None):
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    
    print("\n📝 Your Tasks:")
    print("---------------------------------")
    for task in tasks:
        if status and task["status"] != status:
            continue
        status_icon = "✔️" if task["status"] == "completed" else "⏳"
        print(f"[{task['id']}] {task['description']} {status_icon} (Created: {task['created_at']})")
    print("---------------------------------")

# Mark a task as completed
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            save_tasks(tasks)
            print(f"✅  Task {task_id} marked as completed!")
            return
    print("❌ Task not found.")

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        
        print("❌ Task not found.")
    else:
        save_tasks(updated_tasks)
        print(f"🗑️  Task {task_id} deleted.")

# Command-line argument parser
def main():
    parser = argparse.ArgumentParser(description="To-Do List CLI App")
    parser.add_argument("--add", metavar="task", type=str, nargs="+", help="Add a new task")
    parser.add_argument("--view", metavar="status", type=str, nargs="?", help="View tasks (all, pending, completed)", const="all")
    parser.add_argument("--complete", metavar="id", type=int, help="Mark a task as completed")
    parser.add_argument("--delete", metavar="id", type=int, help="Delete a task")
    
    args = parser.parse_args()
    
    if args.add:
        task_description = " ".join(args.add).strip()
        add_task(task_description)
    elif args.view:
        status = args.view if args.view in ["pending", "completed"] else None
        view_tasks(status)
    elif args.complete:
        complete_task(args.complete)
    elif args.delete:
        delete_task(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
