'use client';

import { useState, useEffect } from 'react';
import { clearHistory } from '../actions';
import { useRouter } from 'next/navigation';
import '../styles/HistoryList.css';

export default function HistoryList({ initialHistory }) {
    const [expandedSteps, setExpandedSteps] = useState({});
    const [isClient, setIsClient] = useState(false);
    const router = useRouter();

    useEffect(() => {
        setIsClient(true);
    }, []);

    const toggleSteps = (index) => {
        setExpandedSteps(prev => ({
            ...prev,
            [index]: !prev[index]
        }));
    };

    const handleClearHistory = async () => {
        if (!window.confirm('Are you sure you want to clear all history?')) {
            return;
        }
        const result = await clearHistory();
        if (result.success) {
            router.refresh();
        }
    };

    const formatTimestamp = (timestamp) => {
        if (!isClient) return '';
        const date = new Date(timestamp);
        return date.toLocaleString();
    };

    return (
        <div className="historyDiv">
            <div className="historyHeaderDiv">
                <h2>Task History</h2>
                {initialHistory.length > 0 && (
                    <button className="clearButton" onClick={handleClearHistory}>
                        Clear History
                    </button>
                )}
            </div>
            {initialHistory.length === 0 ? (
                <div className="noHistoryDiv">
                    <p>No tasks executed yet. Execute a task to see history of previous tasks.</p>
                </div>
            ) : (
                <div className="historyListDiv">
                    {initialHistory.map((item, index) => (
                        <div key={index} className="historyItemDiv">
                            <div className="historyHeader">
                                <div className="historyTask">{item.task}</div>
                                <div className="historyTime">
                                    {formatTimestamp(item.timestamp)}
                                </div>
                            </div>
                            <div className="historyTool">{item.tool_used}</div>
                            <div className="historyResult">
                                <strong>Result:</strong> {item.result}
                            </div>
                            <div className="historyStepsDiv">
                                <button
                                    className="historyToggle"
                                    onClick={() => toggleSteps(index)}
                                >
                                    <div className="historyToggleDiv">
                                        {expandedSteps[index] ? <img alt="" src="/assets/images/chevronDown.svg" /> : <img alt="" className="historyChevronRotated" src="/assets/images/chevronDown.svg" />}{" "}
                                        <div>{expandedSteps[index] ? 'Hide' : 'Show'} Execution Steps</div>
                                    </div>
                                </button>
                                {expandedSteps[index] && (
                                    <ol className="historyList">
                                        {item.steps.map((step, stepIndex) => (
                                            <li key={stepIndex}>{step}</li>
                                        ))}
                                    </ol>
                                )}
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}