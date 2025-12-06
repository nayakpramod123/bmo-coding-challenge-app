# bmo-coding-challenge-app
A full-stack application that uses an intelligent agent to process user tasks by automatically selecting and executing the appropriate tool.

## What This Application Does

The BMO Agent Task System is designed to intelligently handle various types of tasks by:

- **Analyzing user input** to determine the intent
- **Selecting the appropriate tool** from available options
- **Executing the task** and returning structured results
- **Tracking execution steps** for transparency
- **Maintaining history** of all processed tasks

### Available Tools

1. **Text Processor Tool**: Handles text operations
   - Convert text to uppercase or lowercase
   - Count words in text
   - Reverse text strings

2. **Calculator Tool**: Performs mathematical operations
   - Basic arithmetic (addition, subtraction, multiplication, division)
   - Supports complex expressions with parentheses
   - Handles operator symbols like +, -, *, /, ×, ÷

3. **Weather Mock Tool**: Provides weather information
   - Returns mock weather data for cities
   - Includes temperature and conditions

## Architecture

### Backend (Python FastAPI)
- **Agent Controller**: Analyzes tasks and routes to appropriate tools
- **Tool System**: Modular tools for different task types
- **Storage Layer**: JSON-based persistence for task history
- **REST API**: Endpoints for task execution and history management

### Frontend (Next.js 14 with SSR)
- **Server-Side Rendering**: Initial page load fetches data on the server
- **Server Actions**: API calls executed on the server, not the client
- **Client Components**: Interactive UI elements (forms, buttons, toggles)
- **Server Components**: Data fetching and initial rendering on the server
- **Hybrid Architecture**: Combines server and client rendering for optimal performance

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

## How to Run the Application

### Step 1: Setup Backend

1. Open a terminal and navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:

**For All Platforms:**
```bash
pip install -r requirements.txt
```

**If you get Rust compilation errors on Windows:**
```bash
# This installs the latest compatible versions with pre-built wheels
pip install fastapi uvicorn pydantic python-multipart
```

See `WINDOWS_INSTALL.txt` for detailed Windows troubleshooting.

3. Start the backend server:
```bash
uvicorn main:app --reload --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

The backend API is now running at `http://localhost:8000`

Leave this terminal running and open a new terminal for the frontend.

### Step 2: Setup Frontend

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies (first time only):
```bash
npm install
```

This will take a few minutes to download all dependencies

3. Start the Next.js development server:
```bash
npm run dev
```

**Expected Output:**
```
   ▲ Next.js 14.0.4
   - Local:        http://localhost:3000

 ✓ Ready in 2.5s
```

The frontend is now running at `http://localhost:3000`

### Step 3: Access the Application

Open your web browser and go to:
```
http://localhost:3000
```

You should see the Agent Task System interface!

## Quick Start Guide

Once the application is running:

1. **Enter a task** in the text input field
2. **Click "Execute"** button
3. **View the result** displayed with execution steps
4. **Check the history** section below to see all past tasks
5. **Click "Show Execution Steps"** on any history item to see detailed logs

## Testing the Application

### Example Tasks to Try

Copy and paste these into the application:

**Text Processing:**
- "Convert this to uppercase"
- "Make hello world lowercase"
- "Count words in the quick brown fox"
- "Reverse hello"
- "Make this text uppercase"

**Calculations:**
- "Calculate 25 + 37"
- "What is 100 - 45 * 2"
- "Solve 15 x 8"
- "(10 + 5) * 3"
- "What's 50 / 2"

**Weather:**
- "Weather in New York"
- "Temperature in London"
- "Climate in Tokyo"
- "What's the weather in Paris"

## API Endpoints

### POST /api/execute
Execute a task through the agent system.

**Request Body:**
```json
{
  "task": "Calculate 10 + 5"
}
```

**Response:**
```json
{
  "task": "Calculate 10 + 5",
  "result": "15",
  "tool_used": "Calculator Tool",
  "steps": [
    "Received input: 'Calculate 10 + 5'",
    "Analyzing task type...",
    "Selected tool: Calculator Tool",
    "Executing Calculator Tool...",
    "Tool execution completed",
    "Returning result to user"
  ],
  "timestamp": "2024-12-05T10:30:00.000000",
  "tool_details": {...}
}
```

### GET /api/history
Retrieve all executed tasks.

**Response:** Array of task execution objects

### DELETE /api/history
Clear all task history.

## Project Structure

```
bmo-agent-system/
├── backend/
│   ├── main.py              # FastAPI application entry point
│   ├── agent.py             # Agent controller with task analysis logic
│   ├── tools.py             # Tool implementations (Text, Calculator, Weather)
│   ├── storage.py           # JSON-based data persistence
│   ├── requirements.txt     # Python dependencies
│   └── tasks_history.json   # Storage file (created automatically)
│
└── frontend/
    ├── app/
    │   ├── components/          
    │   │   ├── HomePage.js      # Client Component - main page with state
    │   │   ├── TaskForm.js      # Client Component - form submission
    │   │   ├── ResultDisplay.js # Client Component - shows results
    │   │   └── HistoryList.js   # Client Component - displays history
    │   ├── styles/          
    │   │   ├── HomePage.css     # Styles for main component
    │   │   ├── TaskForm.css     # Styles for form submission component
    │   │   ├── ResultDisplay.css # Styles for results component
    │   │   └── HistoryList.css  # Styles for history component
    │   ├── actions.js           # Server Actions - API calls to backend
    │   ├── layout.js            # Root layout component
    │   ├── page.js              # Server Component - fetches initial data
    │   └── globals.css          # Global CSS File
    ├── public/  
    |   ├── assets/
    |   |   ├── images/          # Contains all the images related to the application     
    ├── .env.local               # Your environment file (create this, not in git)
    ├── next.config.js           # Next.js configuration
    └── package.json             # Node dependencies
```

## Design Decisions

### Agent Logic
The agent analyzes task text using keyword matching and pattern recognition to determine the appropriate tool. It considers:
- Explicit keywords (e.g., "calculate", "weather", "uppercase")
- Presence of numbers and operators for math operations
- Context clues in the task description

### Storage
JSON file-based storage was chosen for simplicity. The system maintains all task history including:
- Original task text
- Execution results
- Tool selection
- Step-by-step execution trace
- Timestamps

### Error Handling
- Invalid mathematical expressions return error messages
- Unknown cities get default weather data
- Clear error messages displayed in the UI

## Features

- **Automatic Tool Selection**: Agent intelligently chooses the right tool
- **Execution Transparency**: Complete step-by-step execution trace
- **Persistent History**: All tasks saved and retrievable
- **Clean Interface**: Simple, intuitive user experience with Tailwind CSS
- **Real-time Updates**: Immediate feedback on task execution
- **Expandable Architecture**: Easy to add new tools
- **Server-Side Rendering**: Fast initial page loads with pre-rendered content
- **Server Actions**: Secure API calls executed on the server
- **Optimized Performance**: Hybrid rendering for best user experience

## Environment Variables

The frontend uses environment variables to configure the backend API connection.

## Stopping the Application

To stop the servers:
- Press `Ctrl+C` in both terminal windows (backend and frontend)

## Complete Startup Commands Reference

**Backend (Terminal 1):**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend (Terminal 2):**
```bash
cd frontend
npm install
npm run dev
```

**Access:** Open browser to `http://localhost:3000`


**CORS errors:**
- Ensure the backend is running at `http://localhost:8000`
- Check that the NEXT_PUBLIC_API_URL in `frontend/.env.local` matches your backend URL
- Make sure you started the backend before the frontend

### Common Issues

**"Cannot connect to backend":**
1. Check if backend is running: Open `http://localhost:8000` in browser
2. You should see: `{"message":"API is running"}`
3. If not, restart the backend server

**"npm: command not found":**
- Install Node.js from https://nodejs.org/

**"python: command not found":**
- Install Python from https://www.python.org/downloads/

**Changes not reflecting:**
- Backend: Server auto-reloads with `--reload` flag
- Frontend: Next.js auto-reloads, refresh browser if needed