import "./AlbumCard.css";

export default function AlbumCard ({ album }) {
    return (
        <div className="album-card__div">
            <img src={album.imageUrl} className="album-card__image" alt=""/>

            <div className="album-card__description">
                <div className="album-card__album-name">{album.name}</div>
                <p className="album-card__album-description">{album.artistName}</p>
            </div>
        </div>
    )
}
