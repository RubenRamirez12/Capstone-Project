import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginPage from "./components/LoginPage";
import { authenticate } from "./store/session";
import { Redirect } from "react-router-dom/cjs/react-router-dom.min";
import MainPage from "./components/MainPage/MainPage";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {isLoaded && (
        <Switch>

          <Route exact path="/">
            <Redirect to="/main" />
          </Route>

          <Route path="/main">
            <MainPage />
          </Route>

          <Route path="/account/login">
            <LoginPage />
          </Route>

          <Route path="/account/signup">
            <SignupFormPage />
          </Route>

          <Route>
            <Redirect to="/main" />
          </Route>

        </Switch>
      )}
    </>
  );
}

export default App;
