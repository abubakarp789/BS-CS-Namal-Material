import React from 'react';

const TaskItem = ({ task, onDelete }) => {
  return (
    <li className="task-item">
      <span className="task-text">{task.text}</span>
      <button className="btn-delete" onClick={() => onDelete(task.id)}>Delete</button>
    </li>
  );
};

export default TaskItem;
