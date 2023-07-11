// constants
const LOAD_PLAYLISTS = "playlist/LOAD_PLAYLISTS";
const CREATE_PLAYLIST = "playlist/CREATE_PLAYLIST";
const DELETE_PLAYLIST = "playlist/DELETE_PLAYLIST";
const EDIT_PLAYLIST = "playlist/EDIT_PLAYLIST";

//actions
const actionLoadPlaylists = (body) => ({
  type: LOAD_PLAYLISTS,
  payload: body,
});

const actionCreatePlaylist = (body) => ({
  type: CREATE_PLAYLIST,
  payload: body,
});

//thunks
export const thunkGetPlaylists = () => async (dispatch) => {};

export const thunkCreatePlaylist = () => async (dispatch) => {};

const initialState = { playlists: {} };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    default:
      return state;
  }
}
