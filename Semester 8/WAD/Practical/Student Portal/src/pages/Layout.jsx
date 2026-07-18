import { Outlet, NavLink } from "react-router-dom";

const Layout = () => {
  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="nav-brand">Namal Student Portal</div>
        <ul className="nav-links">
          <li>
            <NavLink to="/" className={({ isActive }) => isActive ? "active-link" : ""}>Home</NavLink>
          </li>
          <li>
            <NavLink to="/dashboard" className={({ isActive }) => isActive ? "active-link" : ""}>Dashboard</NavLink>
          </li>
          <li>
            <NavLink to="/announcements" className={({ isActive }) => isActive ? "active-link" : ""}>Announcements</NavLink>
          </li>
          <li>
            <NavLink to="/contact" className={({ isActive }) => isActive ? "active-link" : ""}>Contact</NavLink>
          </li>
        </ul>
      </nav>
      <main className="main-content">
        <Outlet />
      </main>
    </div>
  );
};
export default Layout;
