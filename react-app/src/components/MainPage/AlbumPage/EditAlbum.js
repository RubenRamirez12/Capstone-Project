import { useState } from "react";
import { useDispatch } from "react-redux";
import { thunkDeleteAlbum, thunkEditAlbum } from "../../../store/album";
import { useModal } from "../../../context/Modal";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import "./EditAlbum.css";

export default function EditAlbum({ album }) {
  const dispatch = useDispatch();
  const [albumImg, setAlbumImg] = useState(null);
  const [displayUrl, setDisplayUrl] = useState(album.imageUrl);
  const history = useHistory()
  const [albumName, setAlbumName] = useState(album.name);
  const [albumDescription, setAlbumDescription] = useState(album.description);
  const { closeModal } = useModal();

  const handleEditSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("name", albumName);
    formData.append("description", albumDescription);

    if (albumImg) {
      formData.append("image", albumImg);
    }

    await dispatch(thunkEditAlbum(album.id, formData));
    closeModal();
  };

  const handleNewImage = async (e) => {
    let image = e.target.files[0];
    setAlbumImg(image);
    setDisplayUrl(URL.createObjectURL(image));
  };

  const handleAlbumDelete = async (e) => {
    await dispatch(thunkDeleteAlbum(album.id))
    history.push('/main')
  }

  return (
    <div className="edit-album__div">
      <h1 className="edit-album__title">Edit Album details</h1>
      <form
        className="edit-album__form"
        onSubmit={(e) => handleEditSubmit(e)}
        encType="multipart/form-data">
        <label className="edit-album__img-label">
          <img className="edit-album__image" src={displayUrl} alt="" />
          <input
            type="file"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => handleNewImage(e)}
          />
          <button
            className="edit-album__delete-button"
            onClick={handleAlbumDelete}>
            DELETE ALBUM
          </button>
        </label>

        <div className="edit-album__info">
          <div className="edit-album__section">
            <input
              required
              type="text"
              placeholder="Enter a name"
              value={albumName}
              className="edit-album__name-input"
              onChange={(e) => setAlbumName(e.target.value)}
              maxLength={100}
            />
            {albumName.length >= 100 && (
              <span className="edit-album__error">
                maximum characters reached
              </span>
            )}
          </div>

          <div className="edit-album__section">
            <textarea
              required
              placeholder="enter a description"
              value={albumDescription}
              className="edit-album__description-textarea"
              onChange={(e) => setAlbumDescription(e.target.value)}
              maxLength={150}
            />
            {albumDescription.length >= 150 && (
              <span className="edit-album__error">
                maximum characters reached
              </span>
            )}
          </div>

          <button className="edit-album__submit-button" type="submit">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}
