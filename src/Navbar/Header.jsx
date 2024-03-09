import { Link } from "react-router-dom";

import "./Header.css";

const Header = () => {
  return (
    <>
      <nav className="nav-bar">
        <div className="left-container">
          <div className="home">
            <Link to="/" className="left-home">
              Home
            </Link>
          </div>
          <div className="about">
            <Link to="/about" className="right-about">
              About Us
            </Link>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Header;
