import { Link } from "react-router-dom";

const Profile = () => {
  return (
    <div className="profile-section">
      <h2>Student Profile</h2>
      <p><strong>Email:</strong> bscs22f41@namal.edu.pk</p>
      <p><strong>Semester:</strong> 8th</p>
      <p><strong>Major:</strong> Computer Science</p>
      <Link to="/dashboard" className="btn-secondary" style={{ marginTop: "1rem" }}>Back to Dashboard Info</Link>
    </div>
  );
};
export default Profile;
