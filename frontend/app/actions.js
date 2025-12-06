'use server';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function executeTask(taskInput) {
    try {
        const response = await fetch(`${API_URL}/api/execute`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ task: taskInput }),
            cache: 'no-store'
        });
        if (!response.ok) {
            throw new Error('Failed to execute task');
        }
        const data = await response.json();
        return { success: true, data };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

export async function getHistory() {
    try {
        const response = await fetch(`${API_URL}/api/history`, {
            cache: 'no-store'
        });
        if (!response.ok) {
            throw new Error('Failed to fetch history');
        }
        const data = await response.json();
        return { success: true, data: data.reverse() };
    } catch (error) {
        return { success: false, data: [] };
    }
}

export async function clearHistory() {
    try {
        const response = await fetch(`${API_URL}/api/history`, {
            method: 'DELETE',
            cache: 'no-store'
        });
        if (!response.ok) {
            throw new Error('Failed to clear history');
        }
        return { success: true };
    } catch (error) {
        return { success: false, error: error.message };
    }
}