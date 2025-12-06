'use client';
import '../styles/ResultDisplay.css';

export default function ResultDisplay({ result, closeResult }) {
    if (!result) return null;

    const formatTimestamp = (timestamp) => {
        const date = new Date(timestamp);
        return date.toLocaleString();
    };

    return (
        <div className="resultDiv">
            <div className="resultHeaderDiv">
                <h2>Latest Result</h2>
                <img alt="" className="resultClose" src="/assets/images/close.svg" onClick={closeResult} />
            </div>
            <div className="resultContentDiv">
                <p><strong>Task:</strong> {result.task}</p>
                <p><strong>Result:</strong> {result.result}</p>
                <p><strong>Tool Used:</strong> {result.tool_used}</p>
                <p><strong>Timestamp:</strong> {formatTimestamp(result.timestamp)}</p>
                <div className="stepsDiv">
                    <h3>Execution Steps</h3>
                    <ol>
                        {result.steps.map((step, index) => (
                            <li key={index}>{step}</li>
                        ))}
                    </ol>
                </div>
            </div>
        </div>
    );
}