import { useState } from "react";
import "./AlbumSongCard.css";
import { useDispatch, useSelector } from "react-redux";
import OpenModalButton from "../../OpenModalButton";
import EditAlbumSong from "./EditAlbumSong";
import { actionPlaySong } from "../../../store/song";

export default function AlbumSongCard({ song, index }) {
  const [hovered, setHovered] = useState(false);
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch()

  const handlePlaySong = async () => {
    dispatch(actionPlaySong(song))
  }

  return (
    <div
      className="album-song-card__div"
      onMouseEnter={(e) => setHovered(true)}
      onMouseLeave={(e) => setHovered(false)}>
      <div className="album-song-card__number">
        {!hovered ? (
          index
        ) : (
          <button className="album-song-card__play-song-button" onClick={handlePlaySong}>
            <i className="fa-solid fa-play" />
          </button>
        )}{" "}
      </div>

      <div className="album-song-card__song-info">
        <div className="album-song-card__name">{song.name}</div>
        <div className="album-song-card__artist">{song.artistName}</div>
      </div>

      <div className="album-song-card__song-length">
        {hovered && user && user.id === song.artistId && (
          <OpenModalButton
            modalComponent={<EditAlbumSong currentSong={song} />}
            buttonText={<i className="fa-solid fa-ellipsis" />}
            buttonClass={"album-song-card__play-song-button"}
          />
        )}
      </div>
    </div>
  );
}
