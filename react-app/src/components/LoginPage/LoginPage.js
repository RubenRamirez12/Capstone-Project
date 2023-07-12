import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import "./LoginPage.css";
import { Link } from "react-router-dom/cjs/react-router-dom.min";
import whiteBlackLogo from "../../Images/LogoWhiteBlack.jpeg";

export default function LoginPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [credential, setCredential] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/main" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(credential, password));
    if (data) {
      setErrors(data);
    }
  };

  const handleDemoUser = (e) => {
    e.preventDefault()
    dispatch(login("Demo", "password"));
  }

  return (
    <div className="login-page__div">
      <div className="login-page__nav">
        <img className="login-page__logo" src={whiteBlackLogo} /> Groovify
      </div>
      <form onSubmit={handleSubmit} className="login-page__form">
        <h1 className="login-page__form-h1">Log in to Groovify</h1>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <label className="login-page__label">
          Email or username
          <input
            type="text"
            value={credential}
            onChange={(e) => setCredential(e.target.value)}
            required
            placeholder="Email or username"
            className="login-page__input"
          />
        </label>
        <label className="login-page__label">
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            placeholder="Password"
            className="login-page__input"
          />
        </label>
        <button type="submit" className="login-page__submit-button">
          Log In
        </button>
        <button className="login-page__demo-user" onClick={(e) => handleDemoUser(e)}>Log in as Demo User</button>
        <div className="login-page__sign-up">
          Don't have an account?
          <Link to="/account/signup" className="login-page__sign-up-link">
            {" "}
            Sign up for Groovify
          </Link>
        </div>
      </form>
    </div>
  );
}
