import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import "./PlaylistPage.css";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import Navbar from "../Navbar/Navbar";
import { thunkGetSinglePlaylist, actionClearPlaylist } from "../../../store/playlist";
import { actionPlaySongs } from "../../../store/song";
import PlaylistSongCard from "./PlaylistSongCard";

export default function PlaylistPage() {
  const { playlistId } = useParams();
  const dispatch = useDispatch();
  const playlist = useSelector((state) => state.playlist.singlePlaylist);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(thunkGetSinglePlaylist(playlistId));
    return () => dispatch(actionClearPlaylist());
  }, [dispatch, playlistId]);

  const handlePlayPlaylist = () => {
    // dispatch(actionPlayPlaylist(playlist.songs));
    console.log("HELLO");
  };

  if (Object.values(playlist).length === 0) {
    return <div className="playlist-page__div" />;
  }

  const playSpecificSong = (index) => {
    const sorted_songs = playlist.songs.sort((a, b) => {
      const createdAtA = new Date(a.createdAt).getTime();
      const createdAtB = new Date(b.createdAt).getTime();
      return createdAtA - createdAtB;
    });
    let start = sorted_songs.slice(0, index);
    let end = sorted_songs.slice(index);

    let sortedPlaylist = end.concat(start);
    dispatch(actionPlaySongs(sortedPlaylist));
  };

  return (
    <div className="playlist-page__div">
      <div className="playlist-page__navbar">
        <Navbar />
      </div>

      <div className="playlist-page__title">
        <div className="playlist-page__playlist-image-div">
          <img
            className="playlist-page__playlist-image"
            src={playlist.imageUrl}
            alt=""
          />
        </div>

        <div className="playlist-page__playlist-info">
          <h1 className="playlist-page__playlist-name">{playlist.name}</h1>
          <p className="playlist-page__playlist-artist">
            <img
              src={playlist.ownerPic}
              className="playlist-page__playlist-info-image"
              alt=""
            />
            {playlist.ownerName} • {playlist.songs.length} songs{" "}
          </p>
        </div>
      </div>

      <div className="playlist-page__main-section">
        <div className="playlist-page__main-top">
          <div className="playlist-page__main-buttons">
            <button
              className="playlist-page__green-play-button"
              onClick={handlePlayPlaylist}>
              <i className="fa-solid fa-play" />
            </button>
            {/* {user && user.id === playlist.ownerId && (
              <OpenModalButton
                modalComponent={<EditPlaylist playlist={playlist} />}
                buttonText={<i className="fa-solid fa-ellipsis" />}
                buttonClass={"playlist-page__owner-options-button"}
              />
            )} */}
          </div>

          <div className="playlist-page__main-headers">
            <div className="playlist-page__header1">#</div>
            <div className="playlist-page__header2">Title</div>
            <div className="playlist-page__header3">
              {/* <i className="fa-solid fa-clock" /> */}
            </div>
          </div>
        </div>

        <ul className="playlist-page__song-list">
          {playlist.songs
            .sort((a, b) => {
              const createdAtA = new Date(a.createdAt).getTime();
              const createdAtB = new Date(b.createdAt).getTime();
              return createdAtA - createdAtB;
            })
            .map((song, index) => {
              return (
                <li key={index}>
                  {" "}
                  <PlaylistSongCard
                    playSpecificSong={playSpecificSong}
                    song={song}
                    index={index + 1}
                  />
                </li>
              );
            })}
        </ul>
      </div>
      {/* {user && user.id === playlist.artistId && (
        <div className="playlist-page__create-song-div">
          <OpenModalButton
            modalComponent={<CreateSong playlist={playlist} />}
            buttonText={"add a Song"}
            buttonClass={"playlist-page__create-song-button"}
          />
        </div>
      )} */}
    </div>
  );
}
