import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import { signUp } from "../../store/session";
import blackWhiteLogo from "../../Images/LogoBlackWhite.png";
import "./SignupPage.css";

export default function SignupPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState([]);

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password === confirmPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data);
      }
    } else {
      setErrors([
        "Confirm Password field must be the same as the Password field",
      ]);
    }
  };

  return (
    <div className="signup__div">
      <form onSubmit={handleSubmit} className="signup__form">
        <div className="signup__top">
          <img src={blackWhiteLogo} className="signup__logo" /> Groovify
        </div>
        <h1 className="signup__h1">Sign up for free to start listening.</h1>

        <ul>
          {errors.map((error, idx) => (
            <li className="signup-error" key={idx}>{error}</li>
          ))}
        </ul>
        <h3 className="signup__h3">Sign up with your email address</h3>
        <label className="signup__label">
          What's your email?
          <input
            type="email"
            className="signup__input"
            value={email}
            placeholder="Enter your email."
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <label className="signup__label">
          What should we call you?
          <input
            type="text"
            className="signup__input"
            value={username}
            placeholder="Enter a user name."
            onChange={(e) => setUsername(e.target.value)}
            required
            maxLength={40}
          />
          {username.length >= 40 && (
            <span className="signup-error">Max character limit reached</span>
          )}
        </label>
        <label className="signup__label">
          Create a password
          <input
            type="password"
            className="signup__input"
            placeholder="Create a password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            maxLength={60}
            required
          />
          {password.length >= 60 && (
            <span className="signup-error">Max character limit reached</span>
          )}
        </label>
        <label className="signup__label">
          Confirm your Password
          <input
            type="password"
            placeholder="Confirm your password"
            className="signup__input"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            maxLength={60}
            required
          />
          {confirmPassword.length >= 60 && (
            <span className="signup-error">Max character limit reached</span>
          )}
        </label>
        <button type="submit" className="signup__submit">
          Sign Up
        </button>
      </form>
    </div>
  );
}
