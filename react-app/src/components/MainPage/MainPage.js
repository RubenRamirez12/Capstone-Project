import Sidebar from "./Sidebar";
import "./MainPage.css";
import {
  Redirect,
  Route,
  Switch,
} from "react-router-dom/cjs/react-router-dom.min";
import Browse from "./Browse";
import PlaylistPage from "./PlaylistPage/PlaylistPage";
import AlbumPage from "./AlbumPage/AlbumPage";
import SoundBar from "./SoundBar";

export default function MainPage() {
  return (
    <div className="main-page__div">
      <div className="main-page__top">
        <Sidebar />
        <Switch>
          <Route exact path="/main">
            <Browse />
          </Route>

          <Route path="/main/playlists/:playlistId">
            <PlaylistPage />
          </Route>

          <Route path="/main/albums/:albumId">
            <AlbumPage />
          </Route>

          <Route>
            <Redirect to="/main" />
          </Route>
        </Switch>
      </div>
      <div className="main-page__bottom">
        <SoundBar />
      </div>
    </div>
  );
}
