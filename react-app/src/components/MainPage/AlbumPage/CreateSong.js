import { useState } from "react";
import "./CreateSong.css";
import { useDispatch } from "react-redux";
import { thunkCreateAlbumSong } from "../../../store/album";
import { useModal } from "../../../context/Modal";

export default function CreateSong({ album }) {
  const [name, setName] = useState("");
  const [song, setSong] = useState(null);
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  console.log(album)
  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("album_id", album.id);
    formData.append("name", name);
    formData.append("song", song);


    dispatch(thunkCreateAlbumSong(album.id, formData));
    closeModal();
  };
  return (
    <div className="create-song__div">
      <h1 className="create-song__title">Add a song to</h1>
      <div className="create-song__main">
        <div className="create-song__album-info">
          <h2 className="create-song__album-name">{album.name}</h2>
          <img src={album.imageUrl} className="create-song__album-img" alt=""/>
        </div>

        <form
          className="create-song__form"
          encType="multipart/form-data"
          onSubmit={(e) => handleSubmit(e)}>
          <h1>Song Details</h1>
          <input
            required
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Choose a name for your song"
            maxLength={200}
            className="create-song__name-input"
          />
          {name.length >= 200 && (
            <span className="create-song__error">
              maximum characters reached
            </span>
          )}

          <input
            required
            type="file"
            accept=".mp3, .m4a, .wav, .flac, .ogg, .aac, .alac"
            onChange={(e) => setSong(e.target.files[0])}
            className="create-song__song-input"
          />

          <button type="submit" className="create-song__submit-button">
            Create song
          </button>
        </form>
      </div>
    </div>
  );
}
