// constants
const PLAY_SONGS = "song/PLAY_SONGS";
const NEXT_SONG = 'song/NEXT_SONG';
const PREV_SONG = 'song/PREV_SONG'
const PLAY_ALBUM = 'songs/PLAY_ALBUM'

//actions
export const actionPlaySongs = (songs) => ({
  type: PLAY_SONGS,
  payload: songs,
});

export const actionNextSong = () => ({
    type: NEXT_SONG
})

export const actionPrevSong = () => ({
  type: PREV_SONG
})

export const actionPlayAlbum = (album) => ({
  type: PLAY_ALBUM,
  payload: album
})

//thunks

const initialState = { songs: [] };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case PLAY_SONGS:
      return { songs: action.payload };

    case NEXT_SONG:
      let songs = state.songs;
      let firstSong = songs.shift()
      songs.push(firstSong)
      return { songs: [ ...songs ] };

    case PREV_SONG:
      let currentSongs = state.songs;
      let lastSong = currentSongs.pop()
      currentSongs.unshift(lastSong)
      return { songs: [ ...currentSongs ]}


    case PLAY_ALBUM:
      return { songs : [ ...action.payload ]}

    default:
      return state;
  }
}
