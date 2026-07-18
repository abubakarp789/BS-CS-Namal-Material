import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Announcements from "./pages/Announcements";
import Contact from "./pages/Contact";
import NoPage from "./pages/NoPage";
import Profile from "./pages/Profile";

import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="dashboard" element={<Dashboard />}>
            <Route path="profile" element={<Profile />} />
          </Route>
          <Route path="announcements" element={<Announcements />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
