from typing import Dict, Any, List
from tools import TextProcessorTool, CalculatorTool, WeatherMockTool
from datetime import datetime
import re

class AgentController:
    def __init__(self):
        self.tools = {
            "TextProcessorTool": TextProcessorTool(),
            "CalculatorTool": CalculatorTool(),
            "WeatherMockTool": WeatherMockTool()
        }
        
    def analyze_task(self, task: str) -> str:
        task_lower = task.lower()
        
        calc_keywords = ["calculate", "compute", "solve", "+", "-", "*", "/", "÷", "x", 
                         "add", "subtract", "multiply", "divide", "sum", "difference"]
        weather_keywords = ["weather", "temperature", "forecast", "climate"]
        text_keywords = ["uppercase", "lowercase", "upper", "lower", "reverse", 
                        "word count", "count words", "convert"]
        
        if any(keyword in task_lower for keyword in weather_keywords):
            return "WeatherMockTool"
        elif any(keyword in task_lower for keyword in calc_keywords):
            return "CalculatorTool"
        elif any(keyword in task_lower for keyword in text_keywords):
            return "TextProcessorTool"
        else:
            has_numbers = any(char.isdigit() for char in task)
            has_operators = any(op in task for op in ['+', '-', '*', '/', '='])
            
            if has_numbers and has_operators:
                return "CalculatorTool"
            else:
                return "TextProcessorTool"
    
    def execute_task(self, task: str) -> Dict[str, Any]:
        steps = []
        timestamp = datetime.now().isoformat()
        
        steps.append(f"Received input: '{task}'")
        
        selected_tool = self.analyze_task(task)
        steps.append(f"Analyzing task type...")
        steps.append(f"Selected tool: {re.sub(r'(?<!^)(?=[A-Z])', ' ', selected_tool)}")
        
        tool = self.tools[selected_tool]
        steps.append(f"Executing {re.sub(r'(?<!^)(?=[A-Z])', ' ', selected_tool)}...")
        
        tool_result = tool.execute(task)
        result = tool_result.get("result", "")
        
        steps.append(f"Tool execution completed")
        steps.append(f"Returning result")
        
        return {
            "task": task,
            "result": result,
            "tool_used": re.sub(r'(?<!^)(?=[A-Z])', ' ', selected_tool),
            "steps": steps,
            "timestamp": timestamp,
            "tool_details": tool_result
        }