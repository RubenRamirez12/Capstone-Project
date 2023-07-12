import Sidebar from "./Sidebar";
import "./MainPage.css";
import { Redirect, Route, Switch } from "react-router-dom/cjs/react-router-dom.min";
import Browse from './Browse'

export default function MainPage() {

  return (
    <div className="main-page__div">
      <Sidebar />
      <Switch>

        <Route exact path="/main">
          <Browse />
        </Route>

        <Route path="/main/playlists/:id"></Route>

        <Route path="/main/albums/:id"></Route>

        <Route>
          <Redirect to="/main"/>
        </Route>

      </Switch>
    </div>
  );
}
