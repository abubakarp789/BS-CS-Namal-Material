import React, { useState } from 'react';

const AddTask = ({ onAdd }) => {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    onAdd(text);
    setText('');
  };

  return (
    <form className="add-task-form glass-panel" onSubmit={handleSubmit}>
      <input 
        type="text" 
        placeholder="What needs to be done?" 
        value={text}
        onChange={(e) => setText(e.target.value)}
        className="task-input"
      />
      <button type="submit" className="btn-add">Add Task</button>
    </form>
  );
};

export default AddTask;
