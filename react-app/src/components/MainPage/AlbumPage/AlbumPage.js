import "./AlbumPage.css";
import Navbar from "../Navbar/Navbar";
import { useParams } from "react-router-dom/cjs/react-router-dom.min";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetSingleAlbum } from "../../../store/album";
import OpenModalButton from "../../OpenModalButton";
import EditAlbum from "./EditAlbum";
import CreateSong from "./CreateSong";
import AlbumSongCard from "./AlbumSongCard";

export default function AlbumPage() {
  const { albumId } = useParams();
  const dispatch = useDispatch();
  const album = useSelector((state) => state.album.singleAlbum);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(thunkGetSingleAlbum(albumId));
  }, [dispatch, albumId]);


  if (Object.values(album).length === 0) {
    return <></>;
  }

  return (
    <div className="album-page__div">
      <div className="album-page__navbar">
        <Navbar />
      </div>

      <div className="album-page__title">
        <div className="album-page__album-image-div">
          <img
            className="album-page__album-image"
            src={album.imageUrl}
            alt=""
          />
        </div>

        <div className="album-page__album-info">
          <h1 className="album-page__album-name">{album.name}</h1>
          <p className="album-page__album-artist">
            <img
              src={album.artistPic}
              className="album-page__album-info-image"
              alt=""
            />
            {album.artistName} • {album.songs.length} songs{" "}
          </p>
        </div>
      </div>

      <div className="album-page__main-section">
        <div className="album-page__main-top">
          <div className="album-page__main-buttons">
            <button className="album-page__green-play-button">
              <i className="fa-solid fa-play" />
            </button>
            {user && user.id === album.artistId && (
              <OpenModalButton
                modalComponent={<EditAlbum album={album} />}
                buttonText={<i className="fa-solid fa-ellipsis" />}
                buttonClass={"album-page__owner-options-button"}
              />
            )}
          </div>

          <div className="album-page__main-headers">
            <div className="album-page__header1">#</div>
            <div className="album-page__header2">Title</div>
            <div className="album-page__header3">
              {/* <i className="fa-solid fa-clock" /> */}
            </div>
          </div>
        </div>

        <ul className="album-page__song-list">
          {album.songs
            .sort((a, b) => {
              const createdAtA = new Date(a.createdAt).getTime();
              const createdAtB = new Date(b.createdAt).getTime();
              return createdAtA - createdAtB;
            })
            .map((song, index) => {
              return (
                <li key={index}>
                  {" "}
                  <AlbumSongCard song={song} index={index + 1} />
                </li>
              );
            })}
        </ul>
      </div>
      {user && user.id === album.artistId && (
        <OpenModalButton
          modalComponent={<CreateSong album={album} />}
          buttonText={"add a Song"}
          buttonClass={"album-page__create-song-button"}
        />
      )}
    </div>
  );
}
