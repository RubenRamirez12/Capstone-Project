import { useDispatch, useSelector } from "react-redux";
import AlbumCard from "./AlbumCard";
import "./Browse.css";
import { useEffect } from "react";
import { thunkGetAllAlbums } from "../../../store/album";
import { Link } from 'react-router-dom'
import Navbar from "../Navbar/Navbar";

export default function Browse() {
  const dispatch = useDispatch();
  const albums = useSelector((state) => Object.values(state.album.albums));

  useEffect(() => {
    dispatch(thunkGetAllAlbums());
  }, [dispatch]);

  return (
    <div className="browse__div">

      <div className="browse__top">
        <Navbar />
      </div>

      <div className="browse__catalog">
        <h1>Explore Albums</h1>
        <ul className="browse__album-list">
          {albums.map((album) => {
            return (
              <li key={album.id}>
                <Link to={`/main/albums/${album.id}`} className="browse__list-link">
                  <AlbumCard album={album} />
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
    </div>
  );
}
