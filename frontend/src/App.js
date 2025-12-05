import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import SearchBar from './components/SearchBar';
import PercentilesTable from './components/PercentilesTable';
import InferenceForm from './components/InferenceForm';
import ErrorMessage from './components/ErrorMessage';

function App() {
  const [percentiles, setPercentiles] = useState(null);
  const [error, setError] = useState(null);
  const [chatId, setChatId] = useState('');

  return (
    <div className="container mt-5">
      <h1 className="mb-4">Telegram Message Analysis</h1>
      <SearchBar setPercentiles={setPercentiles} setError={setError} setChatId={setChatId} />
      {error && <ErrorMessage message={error} />}
      {percentiles && <PercentilesTable percentiles={percentiles} />}
      <InferenceForm chatId={chatId} />
    </div>
  );
}

export default App;
