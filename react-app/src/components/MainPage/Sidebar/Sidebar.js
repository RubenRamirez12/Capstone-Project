import "./Sidebar.css";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import {
  thunkCreatePlaylist,
  thunkGetAllPlaylists,
} from "../../../store/playlist";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom/cjs/react-router-dom.min";
import OpenModalButton from "../../OpenModalButton";
import CreateAlbum from "./CreateAlbum";

export default function Sidebar() {
  const user = useSelector((state) => state.session.user);
  const playlists = useSelector((state) =>
    Object.values(state.playlist.playlists)
  );
  const history = useHistory();
  const dispatch = useDispatch();
  const [droppedDown, setDroppedDown] = useState(false);

  useEffect(() => {
    if (user) {
      dispatch(thunkGetAllPlaylists());
    }
  }, [dispatch, user]);

  const createPlaylist = async () => {
    if (user) {
      setDroppedDown(false);
      alert("Feature Coming Soon!")
      // const data = await dispatch(thunkCreatePlaylist());
      // let newId = Object.keys(data.payload)[0];
      // history.push(`/main/playlists/${newId}`);
    } else {
      return history.push("/account/login");
    }
  };

  return (
    <div className="sidebar__div">
      <div className="sidebar__nav">
        <button
          className="sidebar__nav-button"
          onClick={() => history.push("/main")}>
          <i className="fa-solid fa-house" />
          Home
        </button>
        <button
          className="sidebar__nav-button"
          onClick={() => alert("Feature Coming Soon!")}>
          <i className="fa-solid fa-magnifying-glass" />
          Search
        </button>
      </div>

      <div className="sidebar__library">
        <div className="sidebar__library-top">
          Your Library
          <button
            className="sidebar__nav-button"
            onClick={() => setDroppedDown(!droppedDown)}>
            <i className="fa-regular fa-plus" />
          </button>
        </div>
        {droppedDown && (
          <div className="sidebar__dropdown">
            <button className="side__dropdown-item" onClick={createPlaylist}>
              <i className="fa-solid fa-music" />
              Create a new playlist
            </button>
            <OpenModalButton
              modalComponent={<CreateAlbum setDroppedDown={setDroppedDown}/>}
              buttonClass={"side__dropdown-item"}
              buttonText={
                <>
                  <i className="fa-solid fa-compact-disc" />
                  Create a new album
                </>
              }
            />
          </div>
        )}

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
            {user &&
              playlists.map((playlist) => {
                return (
                  <li key={playlist.id} className="sidebar__playlist-entry" onClick={() => alert("Feature coming soon!")}>
                    <Link
                      // to={`/main/playlists/${playlist.id}`}
                      className="sidebar__playlist-link">
                      <img
                        className="sidebar__playlist-image"
                        src={playlist.imageUrl}
                        alt=""
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
