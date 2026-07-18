import { Link, Outlet, useLocation } from "react-router-dom";

const Dashboard = () => {
  const location = useLocation();
  
  return (
    <div className="page-content">
      <h1>Dashboard</h1>
      {location.pathname === "/dashboard" && (
        <div className="dashboard-info">
          <p><strong>Student Name:</strong> Abu Bakar</p>
          <p><strong>Courses:</strong> WAD, AI, DBMS</p>
          <Link to="profile" className="btn-secondary" style={{ marginTop: "1rem", display: "inline-block" }}>Go to Profile</Link>
        </div>
      )}
      <Outlet />
    </div>
  );
};
export default Dashboard;
