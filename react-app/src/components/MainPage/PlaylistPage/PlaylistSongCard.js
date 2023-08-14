import { useEffect, useRef, useState } from "react";
import { useSelector } from "react-redux";
import OpenModalButton from "../../OpenModalButton";
import { useModal } from "../../../context/Modal";
import "./PlaylistSongCard.css";

export default function PlaylistSongCard({ playSpecificSong, song, index }) {
  const [hovered, setHovered] = useState(false);
  const [dropdDownVisible, setDropDownVisible] = useState(false);
  const user = useSelector((state) => state.session.user);
  const currentSong = useSelector((state) => state.song.songs[0]);
  const dropDownRef = useRef(null);
  const { closeModal } = useModal();

  const handleOutsideClick = (event) => {
    if (dropDownRef.current && !dropDownRef.current.contains(event.target)) {
      setDropDownVisible(false);
    }
  };

  useEffect(() => {
    document.addEventListener("mousedown", handleOutsideClick);
    return () => {
      document.removeEventListener("mousedown", handleOutsideClick);
    };
  }, []);

  return (
    <div
      className="playlist-song-card__div"
      onMouseEnter={(e) => setHovered(true)}
      onMouseLeave={(e) => {
        setHovered(false);
        setDropDownVisible(false);
      }}>
      <div className="playlist-song-card__number">
        {!hovered ? (
          index
        ) : (
          <button
            className="playlist-song-card__play-song-button"
            onClick={() => playSpecificSong(index - 1)}>
            <i className="fa-solid fa-play" />
          </button>
        )}{" "}
      </div>

      <div className="playlist-song-card__song-info">
        <img className="playlist-song-card__song-image" src={song.albumImg} />

        <div className="playlist-song-card__song-text">
          <div
            className={`playlist-song-card__name ${
              currentSong?.id === song.id ? "playlist-song-playing" : ""
            }`}>
            {song.name}
          </div>
          <div className="playlist-song-card__artist">{song.artistName}</div>
        </div>
      </div>

      <div className="playlist-song-card__song-length">
        {/* {user && (
          <button
            className="fa-solid fa-ellipsis playlist-song-card__options-button"
            onClick={() => setDropDownVisible(true)}
            style={{ visibility: hovered ? "visible" : "hidden" }}
          />
        )} */}
        {dropdDownVisible && user && (
          <ul className="playlist-song-card__dropdown-menu" ref={dropDownRef}>
            {user && user.id === song.artistId && (
              <li onClick={(e) => setDropDownVisible(false)}>
                {/* <OpenModalButton
                  modalComponent={<EditplaylistSong currentSong={song} />}
                  buttonText="Edit Song"
                  buttonClass={"playlist-song-card__play-song-button"}
                /> */}
              </li>
            )}
            <li />
          </ul>
        )}
      </div>
    </div>
  );
}

/*

  );
}

//             <button
// className="ellipsis-button"
// onClick={() => setDropDownVisible(true)}>
// <i className="fa-solid fa-ellipsis" />
// </button>
// {dropdDownVisible && (
// <div className="dropdown-menu" ref={dropDownRef}>
//   <button onClick={addToPlaylist}>Add to Playlist</button>
//   <EditplaylistSong currentSong={song} />
// </div>
// )}
*/
