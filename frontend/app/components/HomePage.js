'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import TaskForm from './TaskForm';
import ResultDisplay from './ResultDisplay';
import HistoryList from './HistoryList';
import { getHistory } from '../actions';
import '../styles/HomePage.css';

export default function HomePage({ initialHistory }) {
    const [currentResult, setCurrentResult] = useState(null);
    const [history, setHistory] = useState(initialHistory);
    const [showResult, setShowResult] = useState(false)
    const router = useRouter();

    const handleTaskExecuted = async (result) => {
        setCurrentResult(result);
        setShowResult(true)
        router.refresh();
        const historyResult = await getHistory();
        if (historyResult.success) {
            setHistory(historyResult.data);
        }
    };

    useEffect(() => {
        setHistory(initialHistory);
    }, [initialHistory]);

    return (
        <div className="app">
            <div className="header">
                <h1>BMO Agent Task System</h1>
                <p>Submit tasks and let the agent decide which tool to use</p>
            </div>
            <TaskForm onTaskExecuted={handleTaskExecuted} />
            {showResult && <ResultDisplay result={currentResult} closeResult={() => setShowResult(false)} />}
            <HistoryList initialHistory={history} />
        </div>
    );
}