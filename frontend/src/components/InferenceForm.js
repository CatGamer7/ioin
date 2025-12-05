import { useState } from 'react';
import axios from 'axios';

function InferenceForm({ chatId }) {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`${process.env.REACT_APP_API_BASE_URL}/api/v1/classify/`, {
        text,
        chat_id: chatId,
      });
      setResult(response.data);
    } catch (err) {
      alert('Error running inference.');
    }
  };

  return (
    <div className="mt-4">
      <h3>Run Inference</h3>
      <form onSubmit={handleSubmit}>
        <div className="input-group mb-3">
          <input
            type="text"
            className="form-control"
            placeholder="Enter text"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button type="submit" className="btn btn-primary">Run Inference</button>
        </div>
      </form>
      {result && (
        <div className="mt-3">
          <h5>Results:</h5>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default InferenceForm;
