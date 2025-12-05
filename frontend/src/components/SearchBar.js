import { useState } from 'react';
import axios from 'axios';

function SearchBar({ setPercentiles, setError, setChatId }) {
  const [inputChatId, setInputChatId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setPercentiles(null);
    setChatId(inputChatId);

    try {
      const response = await axios.get(`${process.env.REACT_APP_API_BASE_URL}/api/v1/stats/${inputChatId}/`);
      setPercentiles(response.data);
    } catch (err) {
      setError('No messages found for the given chat_id.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="input-group">
        <input
          type="text"
          className="form-control"
          placeholder="Enter chat_id"
          value={inputChatId}
          onChange={(e) => setInputChatId(e.target.value)}
        />
        <button type="submit" className="btn btn-primary">Search</button>
      </div>
    </form>
  );
}

export default SearchBar;
