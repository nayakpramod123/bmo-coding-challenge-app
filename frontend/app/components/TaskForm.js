'use client';

import { useState } from 'react';
import { executeTask } from '../actions';
import '../styles/TaskForm.css';

export default function TaskForm({ onTaskExecuted }) {
    const [task, setTask] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!task.trim()) return;
        setLoading(true);
        setError(null);
        const result = await executeTask(task);
        if (result.success) {
            setTask('');
            onTaskExecuted(result.data);
        } else {
            setError(result.error);
        }
        setLoading(false);
    };

    return (
        <div className="taskInputDiv">
            <h2>Execute a Task</h2>
            <form onSubmit={handleSubmit}>
                <div className="inputDiv">
                    <input
                        type="text"
                        value={task}
                        onChange={(e) => setTask(e.target.value)}
                        placeholder="Enter your task"
                        disabled={loading}
                    />
                    <button type="submit" disabled={loading || !task.trim()}>
                        {loading ? 'Processing...' : 'Execute'}
                    </button>
                </div>
            </form>

            {error && (
                <div className="errorDiv" style={{ marginTop: '15px' }}>
                    Error: {error}
                </div>
            )}

            <div className="exampleDiv">
                <p>Try these examples:</p>
                <ul>
                    <li>Convert this to uppercase</li>
                    <li>Make hello world lowercase</li>
                    <li>Calculate 25 + 37</li>
                    <li>What is 100 - 45 * 2</li>
                    <li>Weather in New York</li>
                    <li>Count words in this is a text</li>
                    <li>Reverse hello</li>
                    <li>Temperature in London</li>
                </ul>
            </div>
        </div>
    );
}