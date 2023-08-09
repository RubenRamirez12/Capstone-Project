// constants
const LOAD_PLAYLISTS = "playlist/LOAD_PLAYLISTS";
const CREATE_PLAYLIST = "playlist/CREATE_PLAYLIST";
const CLEAR_PLAYLIST = "playlist/CLEAR_PLAYLIST"
const LOAD_SINGLE_PLAYLIST = "playlist/LOAD_SINGLE_PLAYLIST"
const ADD_SONG_TO_PLAYLIST = "playlist/ADD_SONG_TO_PLAYLIST"

//actions
const actionLoadPlaylists = (body) => ({
  type: LOAD_PLAYLISTS,
  payload: body,
});

const actionAddSongToPlaylist = (body) => ({
  type: ADD_SONG_TO_PLAYLIST,
  payload: body
})

const actionCreatePlaylist = (body) => ({
  type: CREATE_PLAYLIST,
  payload: body,
});

export const actionClearPlaylist = () => ({
  type: CLEAR_PLAYLIST
})

const actionLoadSinglePlaylist = (body) => ({
  type: LOAD_SINGLE_PLAYLIST,
  payload: body
})

//thunks
export const thunkAddSongToPlaylist = (playlistId, songId) => async (dispatch) => {
  const res = await fetch(`/api/playlists/addSong/${playlistId}/${songId}`)
  if (res.ok) {
    const data = await res.json()
    return dispatch(actionAddSongToPlaylist(data))
  } else {
    console.log("ERROR IN thunkAddSongToPlaylist")
  }
}

export const thunkGetAllPlaylists = () => async (dispatch) => {
  const res = await fetch('/api/playlists/getAll')

  if (res.ok) {
    const data = await res.json()
    const normalized = {}
    for (let playlist of data.playlists) {
      normalized[playlist.id] = playlist
    }
    return dispatch(actionLoadPlaylists(normalized))
  }else {
    console.log("ERROR IN THUNK GET ALL PLAYLISTS")
  }
};

export const thunkCreatePlaylist = () => async (dispatch) => {
  const res = await fetch('/api/playlists/create')

  if (res.ok) {
    const data = await res.json()
    return dispatch(actionCreatePlaylist({[data.id]: {...data}}))
  } else {
    console.log("ERROR IN thunkCreatePlaylist")
  }
};

export const thunkGetSinglePlaylist = (playlistId) => async (dispatch) => {
  const res = await fetch(`/api/playlists/${playlistId}`)

  if (res.ok) {
    const playlist = await res.json()
    return dispatch(actionLoadSinglePlaylist(playlist))
  } else {
    console.log("ERROR IN thunkGetSinglePlaylist")
  }
}

const initialState = { playlists: {}, singlePlaylist: {} };

export default function reducer(state = initialState, action) {
  switch (action.type) {

    case CLEAR_PLAYLIST:
      return { ...state, singlePlaylist: {} }

    case LOAD_PLAYLISTS:
      return {...state, playlists: action.payload}

    case CREATE_PLAYLIST:
      return { ...state, playlists: {...state.playlists, ...action.payload}}

    case LOAD_SINGLE_PLAYLIST:
      return {...state, singlePlaylist: action.payload}
    default:
      return state;
  }
}
