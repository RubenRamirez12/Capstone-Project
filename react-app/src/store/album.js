// constants
const LOAD_ALBUMS = "album/LOAD_ALBUM";

//actions
const actionLoadAlbums = (body) => ({
  type: LOAD_ALBUMS,
  payload: body,
});

//thunks
export const thunkGetAllAlbums = () => async (dispatch) => {
  const res = await fetch('/api/albums/getAll')

  if (res.ok) {
    const data = await res.json()
    const normalized = {}
    for (let album of data.albums) {
      normalized[album.id] = album
    }
    return dispatch(actionLoadAlbums(normalized))
  }else {
    console.log("ERROR IN THUNK GET ALL ALBUMS")
  }
};

const initialState = { albums: {} };

export default function reducer(state = initialState, action) {
  switch (action.type) {

    case LOAD_ALBUMS:
      return {...state, albums: action.payload}

    default:
      return state;
  }
}
