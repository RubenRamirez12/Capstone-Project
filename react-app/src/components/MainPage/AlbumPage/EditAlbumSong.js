import { useState } from "react";
import "./EditAlbumSong.css";
import { useDispatch } from "react-redux";
import { thunkDeleteAlbumSong, thunkEditAlbumSong } from "../../../store/album";
import { useModal } from "../../../context/Modal";

export default function EditAlbumSong({ currentSong }) {
  const dispatch = useDispatch();
  const [name, setName] = useState(currentSong.name);
  const [song, setSong] = useState(null);
  const { closeModal } = useModal();

  const handleEditSubmit = (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("name", name);

    if (song) {
      formData.append("song", song);
    }

    dispatch(thunkEditAlbumSong(currentSong.id, formData));
    closeModal();
  };

  const handleAlbumSongDelete = async (e) => {
    await dispatch(thunkDeleteAlbumSong(currentSong.id));
    closeModal();
  };

  return (
    <div className="edit-song__div">
      <h1>Edit Song</h1>
      <form
        className="edit-song__form"
        onSubmit={(e) => handleEditSubmit(e)}
        encType="multipart/form-data">
        <input
          required
          value={name}
          maxLength={200}
          placeholder="Choose a name for your song"
          onChange={(e) => setName(e.target.value)}
          className="edit-song__name-input"
        />
        <input
          type="file"
          accept=".mp3, .m4a, .wav, .flac, .ogg, .aac, .alac"
          onChange={(e) => setSong(e.target.files[0])}
          className="edit-song__song-input"
        />
        <div className="edit-song__buttons-div">
          <button className="edit-song__submit" type="submit">
            Submit
          </button>
        </div>
      </form>
      <button className="edit-song__delete" onClick={handleAlbumSongDelete}>
        Delete
      </button>
    </div>
  );
}
