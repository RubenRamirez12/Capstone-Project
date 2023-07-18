// constants
const PLAY_SONG = "song/PLAY_SONG";
const NEXT_SONG = 'song/NEXT_SONG';
const PLAY_ALBUM = 'songs/PLAY_ALBUM'

//actions
export const actionPlaySong = (song) => ({
  type: PLAY_SONG,
  payload: song,
});

export const actionNextSong = () => ({
    type: NEXT_SONG
})

export const actionPlayAlbum = (album) => ({
  type: PLAY_ALBUM,
  payload: album
})

//thunks

const initialState = { songs: [] };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case PLAY_SONG:
      return { songs: [action.payload] };

    case NEXT_SONG:
      let songs = state.songs;
      songs.shift();
      return { songs: [ ...songs ] };

    case PLAY_ALBUM:
      return { songs : [...action.payload]}

    default:
      return state;
  }
}
