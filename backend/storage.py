import json
import os
from typing import List, Dict, Any

class Storage:
    def __init__(self, filename: str = "tasks_history.json"):
        self.filename = filename
        self.ensure_file_exists()
    
    def ensure_file_exists(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)
    
    def save_task(self, task_data: Dict[str, Any]) -> None:
        tasks = self.get_all_tasks()
        tasks.append(task_data)
        
        with open(self.filename, 'w') as f:
            json.dump(tasks, f, indent=2)
    
    def get_all_tasks(self) -> List[Dict[str, Any]]:
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def clear_history(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump([], f)