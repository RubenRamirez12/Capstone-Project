// constants
const LOAD_PLAYLISTS = "playlist/LOAD_PLAYLISTS";
const CREATE_PLAYLIST = "playlist/CREATE_PLAYLIST";
const CLEAR_PLAYLIST = "playlist/CLEAR_PLAYLIST"

//actions
const actionLoadPlaylists = (body) => ({
  type: LOAD_PLAYLISTS,
  payload: body,
});

const actionCreatePlaylist = (body) => ({
  type: CREATE_PLAYLIST,
  payload: body,
});

export const actionClearPlaylist = () => ({
  type: CLEAR_PLAYLIST
})

//thunks
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

const initialState = { playlists: {} };

export default function reducer(state = initialState, action) {
  switch (action.type) {

    case CLEAR_PLAYLIST:
      return { playlists: {} }

    case LOAD_PLAYLISTS:
      return {...state, playlists: action.payload}

    case CREATE_PLAYLIST:
      return { ...state, playlists: {...state.playlists, ...action.payload}}

    default:
      return state;
  }
}
