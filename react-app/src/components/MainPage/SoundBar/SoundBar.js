import { useEffect, useRef, useState } from "react";
import "./SoundBar.css";
import { useDispatch, useSelector } from "react-redux";
import { actionNextSong, actionPrevSong } from "../../../store/song";

export default function SoundBar() {
  const dispatch = useDispatch();
  const songs = useSelector((state) => state.song.songs);

  const [currentSong, setCurrentSong] = useState(null);
  const [playing, setPlaying] = useState(false);
  const [songProgress, setSongProgress] = useState(0);
  const [songDuration, setSongDuration] = useState(1);
  const [volume, setVolume] = useState(0.5);

  const audioRef = useRef();

  // console.log("THE CURRENT SONG!", currentSong)

  //sets up new song
  useEffect(() => {
    setCurrentSong(songs[0]);
  }, [songs]);

  //when new currentSong ^^
  useEffect(() => {
    if (currentSong) {
      audioRef.current.src = currentSong.songUrl;
      audioRef.current.load();
      setPlaying(true);
      audioRef.current.play();
    }
  }, [currentSong]);

  //if button is toggled
  useEffect(() => {
    if (audioRef.current) {
      if (playing) {
        audioRef.current.play();
      } else {
        audioRef.current.pause();
      }
    }
  }, [audioRef, playing]);

  const handleProgress = (e) => {
    const progress = parseInt(e.target.value);
    setSongProgress(progress);
    audioRef.current.currentTime = progress;

    if (progress === songDuration && songs.length <= 1) {
      setPlaying(false);
      setSongProgress(0);
      setSongDuration(0);
      audioRef.current.pause();
    }
  };

  const handleVolume = (e) => {
    const volumeVal = parseFloat(e.target.value);
    setVolume(volumeVal);
    audioRef.current.volume = volumeVal;
  };

  const handleNextButton = () => {
    dispatch(actionNextSong());
  };

  const handlePrevButton = () => {
    if (songProgress > 2) {
      audioRef.current.currentTime = 0
    } else {
      dispatch(actionPrevSong());
    }
  };

  return (
    <div className="sound-bar__div">
      <div className="sound-bar__song-info">
        {currentSong ? (
          <img className="sound-bar__img" src={currentSong?.albumImg} alt="" />
        ) : (
          <p className="sound-bar__img" alt="" />
        )}
        <div className="sound-bar__description">
          <div className="sound-bar__song-name">{currentSong?.name}</div>
          <div className="sound-bar__song-artist">
            {currentSong?.artistName}
          </div>
        </div>
      </div>

      <div className="sound-bar__song-menu">
        <div className="sound-bar__song-options">
          <button
            className="sound-bar__left-button"
            disabled={!currentSong}
            onClick={handlePrevButton}>
            <i className="fa-solid fa-backward-step"></i>
          </button>
          <button
            className="sound-bar__play-button"
            disabled={!currentSong}
            onClick={() => setPlaying(!playing)}>
            {playing ? (
              <i className="fa-solid fa-pause" />
            ) : (
              <i className="fa-solid fa-play" />
            )}
          </button>
          <button
            className="sound-bar__right-button"
            disabled={!currentSong}
            onClick={handleNextButton}>
            <i className="fa-solid fa-forward-step"></i>
          </button>
        </div>

        <input
          type="range"
          step="0.01"
          className="sound-bar__range"
          max={songDuration}
          value={songProgress}
          onChange={(e) => handleProgress(e)}
          disabled={!currentSong}
        />
      </div>

      <div className="sound-bar__audio-bar">
        {currentSong && (
          <audio
            ref={audioRef}
            src={currentSong.songUrl}
            onTimeUpdate={() => setSongProgress(audioRef.current.currentTime)}
            onLoadedMetadata={() => setSongDuration(audioRef.current.duration)}
            volume={volume}
            onEnded={handleNextButton}
          />
        )}
        <input
          type="range"
          step="0.01"
          className="sound-bar__volume"
          min={0}
          value={volume}
          max={1}
          onChange={(e) => handleVolume(e)}
          disabled={!currentSong}
        />
      </div>
    </div>
  );
}
