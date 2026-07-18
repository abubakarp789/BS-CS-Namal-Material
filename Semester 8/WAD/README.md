# 🌐 Web Application Development (CS-450)

Welcome to the **Web Application Development (WAD)** course repository! This folder archives comprehensive lecture slides, practical lab exercises, document assignments, MongoDB database scripts & certificates, and full-stack web applications completed during Semester 8.

This course provides end-to-end practice in modern web engineering and the **MERN (MongoDB, Express.js, React, Node.js)** stack, covering frontend UI design, responsive layouts, asynchronous JavaScript (ES6+), RESTful APIs, and NoSQL database management.

---

## 📂 Directory Architecture & Submodules

This directory is organized into several key subdirectories and learning modules:

```text
WAD/
├── 📘 WAD Outline.pdf                   # Official course syllabus & grading breakdown
├── 📑 WAD_LECTURE 1 to 24.pdf           # 12 comprehensive lecture decks (HTML5 to React & Node)
├── 📂 Assignments and Tasks/            # 10 document-based practical assignments & task specifications
├── 📂 Mongodb/                          # MongoDB certification, CRUD scripts, & JSON datasets
└── 📂 Practical/                        # Raw HTML/JS tasks, Node scripts, & React Full-Stack applications
```

---

## 📑 Detailed Module Breakdown

### 1. 📘 Lecture Slides (Lectures 01 to 24)
*   **Lectures 1 to 4**: HTML5 Semantics, CSS3 styling, Flexbox grid systems, Responsive Web Design (RWD), and Bootstrap components.
*   **Lectures 5 to 10**: JavaScript Fundamentals (DOM manipulation, Event Listeners, Promises, Async/Await, ES6 Features).
*   **Lectures 11 to 14**: Server-side development with **Node.js** modules and **Express.js** routing & middleware.
*   **Lectures 15 to 18**: Frontend Component Engineering using **React** (State management, Props, Hooks: `useState`, `useEffect`).
*   **Lectures 19 to 24**: Database integration with **MongoDB** (Schemas, Mongoose ORM, Aggregation pipelines, CRUD REST APIs).

### 2. 📂 [Assignments and Tasks](./Assignments%20and%20Tasks/)
A collection of 10 hands-on tasks and assignment specifications:
*   [Assignment 1.docx](./Assignments%20and%20Tasks/Assignment%201.docx) — Advanced HTML5 & CSS3 layout design.
*   [Assignment 2.docx](./Assignments%20and%20Tasks/Assignment%202.docx) — JavaScript DOM manipulation & event handling.
*   [Assignment 3.docx](./Assignments%20and%20Tasks/Assignment%203.docx) — Asynchronous JavaScript and API integration.
*   [Assignment 4.docx](./Assignments%20and%20Tasks/Assignment%204.docx) — Full-stack API consumption and state persistence.
*   [Express Tasks.docx](./Assignments%20and%20Tasks/Express%20Tasks.docx) — Express routing, middleware implementation, and parameter extraction.
*   [Node Modules Tasks.docx](./Assignments%20and%20Tasks/Node%20Modules%20Tasks.docx) — File System (`fs`), `http`, and custom Node module creation.
*   [React with Bootstrap Tasks.docx](./Assignments%20and%20Tasks/React%20with%20Bootstrap%20Tasks.docx) — Building UI components with React & React-Bootstrap.
*   [Game.docx](./Assignments%20and%20Tasks/Game.docx) — Interactive JavaScript web game development task.

### 3. 📂 [Mongodb — Database Management](./Mongodb/)
Includes official certification, query guides, and sample datasets:
*   📜 [MongoDB Foundations Certification.pdf](./Mongodb/Abubakar%20Panhwar_MongoDB%20Foundations%20Course%20For%20Beginners.pdf) — Certification earned for MongoDB Foundations.
*   [Introduction to MongoDB.pdf](./Mongodb/Introduction%20to%20MongoDB.pdf) & [Working With MongoDB.pdf](./Mongodb/Working%20With%20MongoDB.pdf) — Core lectures on document-oriented databases.
*   **CRUD & Query Scripts**: `crud.txt`, `query-selectors.txt`, `schema-validations.txt`, `find_operations.txt`, `collection.txt`, `cursor.txt`.
*   **JSON Datasets**: `employees.json`, `employee.json` for database seeding and query testing.

### 4. 📂 [Practical — Code Projects & Applications](./Practical/)
Hands-on code projects spanning plain HTML/JS to full React SPAs:
*   **Vanilla Web Labs**: `Task1.html`, `task2.html`, `callback.html`, `practice.html`, `18March26_Tasks/`.
*   **Node Services**: `Practical/NODE/script.js` — Basic Node server script.
*   **React Applications (`Practical/REACT/`)**:
    *   `personal_productivity_dashboard/` — Interactive task and time management app.
    *   `sudhaarai/` — Web frontend portal for SudhaarAI code assistant.
*   **🚀 [Student Portal](./Practical/Student%20Portal/)**: A production-grade Single Page Application (SPA) built using **Vite + React**, featuring component modularity, ESLint configuration, and dynamic student data routing.
*   **🔗 Official GitHub Code Repositories**:
    *   🌟 **[Rumi-House-Hub (Semester Project Repository)](https://github.com/abubakarp789/Rumi-House-Hub)** — Full-stack MERN portal for Namal student engagement, society enrollments, event proposals, seat RSVPs, and digital QR attendance gate passes.
    *   ✍️ **[WAD-Assignments Repository](https://github.com/abubakarp789/WAD-Assignments)** — Official repository housing full-stack assignments (`Assignment 1` to `4` for Rumi-House-Hub and Bootstrap Portfolio).
    *   🔧 **[WAD-Tasks Repository](https://github.com/abubakarp789/WAD-Tasks)** — Archive of practical web development tasks (`Student Portal`, `Quickbite`, `Personal Productivity Dashboard`, `StudentResultManagement`).

---

## 🛠️ Full-Stack Technology Architecture

```text
 ┌─────────────────────────────────────────────────────────────┐
 │                       FRONTEND (UI)                         │
 │   React (Vite)  •  Bootstrap 5  •  JavaScript (ES6+)  • HTML5 │
 └──────────────────────────────┬──────────────────────────────┘
                                │  REST HTTP Requests
                                ▼
 ┌─────────────────────────────────────────────────────────────┐
 │                      BACKEND (SERVER)                       │
 │        Node.js  •  Express.js REST APIs  •  Middleware      │
 └──────────────────────────────┬──────────────────────────────┘
                                │  Mongoose / Native Queries
                                ▼
 ┌─────────────────────────────────────────────────────────────┐
 │                     DATABASE (STORAGE)                      │
 │     MongoDB Document Stores  •  JSON Datasets  •  BSON      │
 └─────────────────────────────────────────────────────────────┘
```

---

## 🧠 Core Competencies Achieved

### 1. Client-Side Development
*   **Modern CSS & Responsive Design**: Building layouts with CSS Grid, Flexbox, and React-Bootstrap components.
*   **React Ecosystem**: Hook-driven state management (`useState`, `useEffect`), props passing, component modularity, and Vite fast-bundling.

### 2. Server-Side Development & APIs
*   **RESTful API Engineering**: Designing CRUD endpoints in Express.js with custom middleware for logging and authentication.
*   **Asynchronous Flow**: Leveraging Promises, `async/await`, and non-blocking I/O in Node.js.

### 3. Database Engineering
*   **NoSQL Modeling**: Designing document structures, embedded collections, and schema validation rules in MongoDB.
*   **Query Optimization**: Executing complex aggregation pipelines, projection filters, and index optimization.

---

*Explore any of the subdirectories above to inspect code files, database scripts, and full web applications!*
