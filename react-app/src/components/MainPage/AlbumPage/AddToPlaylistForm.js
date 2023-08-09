import { useDispatch, useSelector } from "react-redux";
import "./AddToPlaylistForm.css";
import { thunkAddSongToPlaylist } from "../../../store/playlist";

//make a div with a add to playlist header and then a list of playlists
export default function AddToPlaylistForm({ song, closeModal }) {
  const dispatch = useDispatch();

  const playlists = useSelector((state) =>
    Object.values(state.playlist.playlists)
  );

  const noPlaylist = () => {
    closeModal();
  };

  const handleAddSong = (playlistId) => {
    dispatch(thunkAddSongToPlaylist(playlistId, song.id));
    closeModal();
  };

  return (
    <div className="add-to-playlist-form__div">
      <h1 className="add-to-playlist-form__header">Add to playlist</h1>
      {playlists.length > 0 && (
        <ul className="add-to-playlist-form__list">
          {playlists.map((playlist) => {
            return (
              <li
                key={playlist.id}
                className="add-to-playlist-form__list-entree"
                onClick={() => handleAddSong(playlist.id)}>
                <img
                  src={playlist.imageUrl}
                  alt=""
                  className="add-to-playlist-form__image"
                />
                <h1 className="add-to-playlist-form__name">{playlist.name}</h1>
              </li>
            );
          })}
        </ul>
      )}
      {playlists.length === 0 && (
        <button
          className="add-to-playlist-form__no-playlists"
          onClick={noPlaylist}>
          {" "}
          you have no playlists! create one to add songs{" "}
        </button>
      )}
    </div>
  );
}
