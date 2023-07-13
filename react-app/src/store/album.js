// constants
const LOAD_ALBUMS = "album/LOAD_ALBUM";
const LOAD_SINGLE_ALBUM = "album/LOAD_SINGLE_ALBUM";
const EDIT_ALBUM = "album/EDIT_ALBUM";
const CREATE_ALBUM_SONG = "album/CREATE_ALBUM_SONG"

//actions
const actionLoadAlbums = (body) => ({
  type: LOAD_ALBUMS,
  payload: body,
});

const actionLoadSingleAlbum = (body) => ({
  type: LOAD_SINGLE_ALBUM,
  payload: body,
});

const actionEditAlbum = (body) => ({
  type: EDIT_ALBUM,
  payload: body,
});

const actionCreateAlbumSong = (body) => ({
  type: CREATE_ALBUM_SONG,
  payload: body
})
//thunks
export const thunkGetAllAlbums = () => async (dispatch) => {
  const res = await fetch("/api/albums/getAll");

  if (res.ok) {
    const data = await res.json();
    const normalized = {};
    for (let album of data.albums) {
      normalized[album.id] = album;
    }
    return dispatch(actionLoadAlbums(normalized));
  } else {
    console.log("ERROR IN THUNK GET ALL ALBUMS");
  }
};

export const thunkGetSingleAlbum = (albumId) => async (dispatch) => {
  const res = await fetch(`/api/albums/getOne/${albumId}`);

  if (res.ok) {
    const data = await res.json();
    let album = data.album;
    return dispatch(actionLoadSingleAlbum(album));
  } else {
    console.log("ERROR IN THUNK GET SINGLE ALBUM");
  }
};

export const thunkEditAlbum = (albumId, formData) => async (dispatch) => {
  const res = await fetch(`/api/albums/edit/${albumId}`, {
    method: "PUT",
    body: formData,
  });

  if (res.ok) {
    const updated_album = await res.json();
	  dispatch(actionEditAlbum(updated_album))
  } else {
    console.log("ERROR IN thunk edit album");
  }

};

export const thunkCreateAlbumSong = (albumId, formData) => async (dispatch) => {
  const res = await fetch(`/api/albums/${albumId}/song`, {
    method: "POST",
    body: formData
  })

  if (res.ok) {
    const newSong = await res.json()
    console.log(newSong)
    return newSong
  } else {
    console.log("ERROR IN THUNK CREATE ALBUM SONG")
  }
}

const initialState = { albums: {}, singleAlbum: {} };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case LOAD_ALBUMS:
      return { ...state, albums: action.payload };

    case LOAD_SINGLE_ALBUM:
      return { ...state, singleAlbum: action.payload };

    case EDIT_ALBUM:
      return { ...state, singleAlbum: { ...action.payload } }

    default:
      return state;
  }
}
