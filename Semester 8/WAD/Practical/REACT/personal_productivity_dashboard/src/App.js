import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Timer from './components/Timer';
import AddTask from './components/AddTask';
import TaskList from './components/TaskList';
import Footer from './components/Footer';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([]);

  // Optional: load initial tasks
  useEffect(() => {
    const savedTasks = JSON.parse(localStorage.getItem('dashboard-tasks'));
    if (savedTasks && savedTasks.length > 0) {
      setTasks(savedTasks);
    } else {
      setTasks([
        { id: 1, text: 'Review WAD lecture notes' },
        { id: 2, text: 'Complete React SPA task' }
      ]);
    }
  }, []);

  // Save tasks when updated
  useEffect(() => {
    localStorage.setItem('dashboard-tasks', JSON.stringify(tasks));
  }, [tasks]);

  const addTask = (text) => {
    const newTask = {
      id: Date.now(),
      text
    };
    setTasks([...tasks, newTask]);
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  return (
    <div className="app-container">
      <div className="dashboard-content">
        <Header />
        
        <div className="main-grid">
          <div className="sidebar">
            <Timer />
          </div>
          
          <div className="main-panel glass-panel">
            <h2>My Tasks</h2>
            <AddTask onAdd={addTask} />
            <TaskList tasks={tasks} onDelete={deleteTask} />
          </div>
        </div>

      </div>
      <Footer />
    </div>
  );
}

export default App;
