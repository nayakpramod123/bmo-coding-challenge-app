import HomePage from './components/HomePage';
import { getHistory } from './actions';

export default async function Page() {
    const historyResult = await getHistory();
    const initialHistory = historyResult.success ? historyResult.data : [];

    return <HomePage initialHistory={initialHistory} />;
}