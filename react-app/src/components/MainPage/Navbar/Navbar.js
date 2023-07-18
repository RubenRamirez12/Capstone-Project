import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { logout } from "../../../store/session";
import { actionClearPlaylist } from "../../../store/playlist";
import "./Navbar.css";

export default function Navbar() {
  const user = useSelector((state) => state.session.user);
  const [dropped, setDropped] = useState(false);
  const history = useHistory();
  const dispatch = useDispatch();

  const handleProfileClick = async () => {
    await setDropped(!dropped);
    console.log(dropped);
  };

  const handleNavSignup = () => {
    history.push("/account/signup");
  };

  const handleNavLogin = () => {
    history.push("/account/login");
  };

  const handleNavLogout = async () => {
    await dispatch(actionClearPlaylist());
    await dispatch(logout());
  };

  if (user) {
    return (
      <div className="nav-bar__logged-in-div">
        <button
          onClick={handleProfileClick}
          className="nav-bar__profile-button">
          <img className="nav-bar__profile-image" src={user.profilePic} />
        </button>
        {dropped && (
          <ul className="nav-bar__dropdown-menu">
            <li>{user.username}</li>
            <li>
              <button className="nav-bar__logout" onClick={handleNavLogout}>
                Logout
              </button>
            </li>
          </ul>
        )}
      </div>
    );
  } else {
    return (
      <div className="nav-bar__no-user-buttons">
        <button className="nav-bar__signup" onClick={handleNavSignup}>
          Sign up
        </button>
        <button className="nav-bar__login" onClick={handleNavLogin}>
          Log in
        </button>
      </div>
    );
  }
}
