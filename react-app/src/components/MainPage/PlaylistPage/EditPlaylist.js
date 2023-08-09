import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../../context/Modal";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import {
  thunkDeletePlaylist,
  thunkEditPlaylist,
} from "../../../store/playlist";
import "./EditPlaylist.css";

export default function EditPlaylist({ playlist }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const { closeModal } = useModal();
  const [playlistImg, setPlaylistImg] = useState(null);
  const [displayUrl, setDisplayUrl] = useState(playlist.imageUrl);
  const [playlistName, setPlaylistName] = useState(playlist.name);
  const [playlistDescription, setPlaylistDescription] = useState(
    playlist.description
  );

  const handleEditSubmit = async (e) => {
      e.preventDefault();

      const formData = new FormData();
    formData.append("name", playlistName);
    formData.append("description", playlistDescription);

    if (playlistImg) {
        formData.append("image", playlistImg);
    }
    await dispatch(thunkEditPlaylist(playlist.id, formData));
    closeModal();
};

const handleNewImage = async (e) => {
    let image = e.target.files[0];
    setPlaylistImg(image);
    setDisplayUrl(URL.createObjectURL(image));
};

const handlePlaylistDelete = async (e) => {
    await dispatch(thunkDeletePlaylist(playlist.id));
    closeModal()
    history.push("/main");
};

return (
    <div className="edit-playlist__div">
      <h1 className="edit-playlist__title">Edit Playlist details</h1>
      <form
        className="edit-playlist__form"
        onSubmit={(e) => handleEditSubmit(e)}
        encType="multipart/form-data">
        <label className="edit-playlist__img-label">
          <img className="edit-playlist__image" src={displayUrl} alt="" />
          <input
            type="file"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => handleNewImage(e)}
          />
          <button
            className="edit-playlist__delete-button"
            onClick={handlePlaylistDelete}>
            DELETE Playlist
          </button>
        </label>

        <div className="edit-playlist__info">
          <div className="edit-playlist__section">
            <input
              required
              type="text"
              placeholder="Enter a name"
              value={playlistName}
              className="edit-playlist__name-input"
              onChange={(e) => setPlaylistName(e.target.value)}
              maxLength={100}
            />
            {playlistName.length >= 100 && (
              <span className="edit-playlist__error">
                maximum characters reached
              </span>
            )}
          </div>

          <div className="edit-playlist__section">
            <textarea
              required
              placeholder="enter a description"
              value={playlistDescription}
              className="edit-playlist__description-textarea"
              onChange={(e) => setPlaylistDescription(e.target.value)}
              maxLength={150}
            />
            {playlistDescription.length >= 150 && (
              <span className="edit-playlist__error">
                maximum characters reached
              </span>
            )}
          </div>

          <button className="edit-playlist__submit-button" type="submit">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}
