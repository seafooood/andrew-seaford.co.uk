import { useState } from 'react';

export default function Home() {
  const [text, setText] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async () => {
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const data = await res.json();
      setResponse(data.message || data.error);
    } catch (error) {
      setResponse('An error occurred.');
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Send a Message</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter your message here"
        rows="4"
        cols="50"
      />
      <br />
      <button onClick={handleSubmit}>Send</button>
      {response && <p>Response: {response}</p>}
    </div>
  );
}
