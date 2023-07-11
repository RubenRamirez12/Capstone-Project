import "./Sidebar.css";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import {
  thunkCreatePlaylist,
  thunkGetAllPlaylists,
} from "../../../store/playlist";
import { useEffect } from "react";
import { Link } from "react-router-dom/cjs/react-router-dom.min";

export default function Sidebar() {
  const user = useSelector((state) => state.session.user);
  const playlists = useSelector((state) =>
    Object.values(state.playlist.playlists)
  );
  const history = useHistory();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(thunkGetAllPlaylists());
  }, [dispatch, user]);

  const createPlaylist = async () => {
    if (user) {
      dispatch(thunkCreatePlaylist());
    } else {
      return history.push("/account/login");
    }
  };

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
              <button
                className="sidebar__no-playlists-button"
                onClick={createPlaylist}>
                Create Playlist
              </button>
            </div>
          )}

          <ul className="sidebar__playlist-list">
            {playlists.map((playlist) => {
              return (
                <li key={playlist.id} className="sidebar__playlist-entry">
                  <Link
                    to={`/main/playlists/${playlist.id}`}
                    className="sidebar__playlist-link">
                    <img
                      className="sidebar__playlist-image"
                      src={playlist.imageUrl}
                    />
                    <div className="sidebar__playlist-info">
                      <p className="sidebar__playlist-info__name">
                        {playlist.name}
                      </p>
                      <p className="sidebar__playlist-info__user">
                        {user.username}
                      </p>
                    </div>
                  </Link>
                </li>
              );
            })}
          </ul>
        </div>
      </div>
    </div>
  );
}
