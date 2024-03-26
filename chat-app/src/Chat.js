import React, { useState } from 'react';
import axios from 'axios';

const Chat = () => {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    const response = await axios.post('http://your-api-url/messages', { message });
    setChat([...chat, response.data]);
    setMessage('');
  };

  return (
    <div>
      <ul>
        {chat.map((message, index) => (
          <li key={index}>{message}</li>
        ))}
      </ul>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default Chat;