import { useState } from "react";
import "./EditAlbum.css";

export default function EditAlbum({ album }) {
  const [albumImg, setAlbumImg] = useState(album.imageUrl);
  const [albumName, setAlbumName] = useState(album.name);
  const [albumDescription, setAlbumDescription] = useState(album.description);

  const handleAlbumImage = (e) => {
    const file = e.target.files[0];
    setAlbumImg(URL.createObjectURL(file));
  };

  const handleEditSubmit = () => {};

  return (
    <div className="edit-album__div">
      <h1 className="edit-album__title">Edit Album details</h1>
      <form className="edit-album__form" onSubmit={handleEditSubmit}>
        <label className="edit-album__img-label">
          <img className="edit-album__image" src={albumImg} />
          <input
            type="file"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => handleAlbumImage(e)}
          />
        </label>

        <div className="edit-album__info">
          <input
            required
            type="text"
            placeholder="Enter a name"
            value={albumName}
            className="edit-album__name-input"
            onChange={(e) => setAlbumName(e.target.value)}
            maxLength={100}
          />
          <textarea
            required
            placeholder="enter a description"
            value={albumDescription}
            className="edit-album__description-textarea"
            onChange={(e) => setAlbumDescription(e.target.value)}
            maxLength={150}
          />

          <button className="edit-album__submit-button" type="submit">Submit</button>
        </div>
      </form>
      <button className="edit-album__delete-button" onClick={() => alert("Feature Coming Soon")}>DELETE ALBUM</button>
    </div>
  );
}
