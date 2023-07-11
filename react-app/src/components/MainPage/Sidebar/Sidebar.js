import "./Sidebar.css";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom"
import { thunkCreatePlaylist } from "../../../store/playlist";

export default function Sidebar() {
  const user = useSelector((state) => state.session.user);
  const playlists = useSelector((state) => Object.values(state.playlist.playlists));
  const history = useHistory()
  const dispatch = useDispatch()

  const handleNoPlaylists = async () => {
    if (user) {
        // dispatch(thunkCreatePlaylist())
    } else {
        return history.push('/account/login')
    }
  }

  return (
    <div className="sidebar__div">
      <div className="sidebar__nav">
        <div>Home</div>
        <div>Search</div>
      </div>

      <div className="sidebar__library">
        <div className="sidebar__library-top">
          Your Library
          <button>+</button>
        </div>

        <div className="sidebar__user-library">
          {playlists.length === 0 && (
            <div className="sidebar__no-playlists">
              <h3>Create your first playlist</h3>
              <p>It's easy, we'll help you</p>
              <button className="sidebar__no-playlists-button" onClick={handleNoPlaylists}>Create Playlist</button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
