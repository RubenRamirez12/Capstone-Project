import { useDispatch, useSelector } from "react-redux";
import "./CreateAlbum.css";
import { useState } from "react";
import {
  Redirect,
  useHistory,
} from "react-router-dom/cjs/react-router-dom.min";
import { useModal } from "../../../context/Modal";
import { thunkCreateNewAlbum } from "../../../store/album";

export default function CreateAlbum() {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const [displayUrl, setDisplayUrl] = useState(undefined);
  const [albumName, setAlbumName] = useState("");
  const [albumDescription, setAlbumDescription] = useState("");
  const [albumImage, setAlbumImage] = useState();
  const { closeModal } = useModal();
  const history = useHistory();

  if (!user) {
    closeModal();
    return <Redirect to="/account/login" />;
  }

  const handleCreateSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();

    formData.append("name", albumName);
    formData.append("description", albumDescription);
    formData.append("image", albumImage);

    const res = await dispatch(thunkCreateNewAlbum(formData));
    closeModal();
    history.push(`/main/albums/${res.payload.id}`);
  };

  const handleNewImage = (e) => {
    let image = e.target.files[0];
    setAlbumImage(image);
    setDisplayUrl(URL.createObjectURL(image));
  };

  return (
    <div className="create-album__div">
      <h1 className="create-album__title">Create a Album</h1>
      <form
        className="create-album__form"
        onSubmit={(e) => handleCreateSubmit(e)}
        encType="multipart/form-data">
        <label className="create-album__img-label">
          <img className="create-album__image" src={displayUrl} alt="" />
          <input
            required
            type="file"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => handleNewImage(e)}
          />
        </label>

        <div className="create-album__info">
          <div className="create-album__section1">
            <input
              required
              type="text"
              placeholder="Enter a name"
              value={albumName}
              className="create-album__name-input"
              onChange={(e) => setAlbumName(e.target.value)}
              maxLength={100}
            />
            {albumName.length >= 100 && (
              <span className="create-album__error">
                maximum characters reached
              </span>
            )}
          </div>

          <div className="create-album__section2">
            <textarea
              required
              placeholder="enter a description"
              value={albumDescription}
              className="create-album__description-textarea"
              onChange={(e) => setAlbumDescription(e.target.value)}
              maxLength={150}
            />
            {albumDescription.length >= 150 && (
              <span className="create-album__error">
                maximum characters reached
              </span>
            )}
          </div>

          <button className="create-album__submit-button" type="submit">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}
