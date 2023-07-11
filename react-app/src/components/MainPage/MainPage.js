import Sidebar from "./Sidebar";
import "./MainPage.css";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";

export default function MainPage() {
  const dispatch = useDispatch();
  const handleLogout = () => {
    dispatch(logout());
    console.log("Logged Out!");
  };
  return (
    <div className="main-page__div">
      <Sidebar />
      <div>
        <button onClick={handleLogout}>LOGOUT</button>
      </div>
    </div>
  );
}
