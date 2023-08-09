import { useEffect, useRef, useState } from "react";
import { useSelector } from "react-redux";
import OpenModalButton from "../../OpenModalButton";
import { useModal } from "../../../context/Modal";
import "./PlaylistSongCard.css";

export default function PlaylistSongCard(playSpecificSong, song, index) {
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
      className="album-song-card__div"
      onMouseEnter={(e) => setHovered(true)}
      onMouseLeave={(e) => {
        setHovered(false);
        setDropDownVisible(false);
      }}>
      <div className="album-song-card__number">
        {!hovered ? (
          index
        ) : (
          <button
            className="album-song-card__play-song-button"
            onClick={() => playSpecificSong(index - 1)}>
            <i className="fa-solid fa-play" />
          </button>
        )}{" "}
      </div>

      <div className="album-song-card__song-info">
        <div
          className={`album-song-card__name ${
            currentSong?.id === song.id ? "album-song-playing" : ""
          }`}>
          {song.name}
        </div>
        <div className="album-song-card__artist">{song.artistName}</div>
      </div>

      <div className="album-song-card__song-length">
        {user && (
          <button
            className="fa-solid fa-ellipsis album-song-card__options-button"
            onClick={() => setDropDownVisible(true)}
            style={{ visibility: hovered ? "visible" : "hidden" }}
          />
        )}
        {dropdDownVisible && user && (
          <ul className="album-song-card__dropdown-menu" ref={dropDownRef}>
            {/* delete song if user owns the playlist */}
            {user && user.id === song.artistId && (
              <li onClick={(e) => setDropDownVisible(false)}>
                {/* <OpenModalButton
                  modalComponent={<EditAlbumSong currentSong={song} />}
                  buttonText="Edit Song"
                  buttonClass={"album-song-card__play-song-button"}
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
//   <EditAlbumSong currentSong={song} />
// </div>
// )}
*/
