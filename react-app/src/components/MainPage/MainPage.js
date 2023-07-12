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

export default function MainPage() {
  return (
    <div className="main-page__div">
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
  );
}
