import React from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Navbar.css";  // Ensure you create this CSS file

function Navbar() {
    const navigate = useNavigate();

    const handleLogout = () => {

        navigate('/logout');
    };

    return (
        <nav className="navbar">
            <div className="nav-logo" onClick={() => navigate('/')}>
                Almonds
            </div>
            <div className="nav-items">
                <button onClick={handleLogout} className="logout-button">
                    Logout
                </button>
            </div>
        </nav>
    );
}

export default Navbar;
