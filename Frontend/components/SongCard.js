"use client";

export default function SongCard({ song }) {
  const openYoutube = () => window.open(song.youtube_url, "_blank");

  return (
    <div
      onClick={openYoutube}
      style={{
        background: "var(--surface)",
        border: "1px solid var(--border)",
        borderRadius: "1rem",
        padding: "1rem 1.25rem",
        display: "flex",
        alignItems: "center",
        gap: "1rem",
        boxShadow: "0 2px 8px rgba(124, 58, 237, 0.05)",
        transition: "box-shadow 0.2s, border-color 0.2s",
        cursor: "pointer",
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.borderColor = "rgba(124,58,237,0.3)";
        e.currentTarget.style.boxShadow = "0 4px 16px rgba(124,58,237,0.1)";
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.borderColor = "var(--border)";
        e.currentTarget.style.boxShadow = "0 2px 8px rgba(124,58,237,0.05)";
      }}
    >
      {/* Album Art */}
      {song.album_art ? (
        <img
          src={song.album_art}
          alt={song.name}
          style={{
            width: "52px",
            height: "52px",
            borderRadius: "0.6rem",
            objectFit: "cover",
            flexShrink: 0,
          }}
        />
      ) : (
        <div
          style={{
            width: "52px",
            height: "52px",
            borderRadius: "0.6rem",
            background: "var(--surface2)",
            flexShrink: 0,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "var(--muted)",
            fontSize: "1.2rem",
            fontWeight: 600,
          }}
        >
          ♪
        </div>
      )}

      {/* Info */}
      <div style={{ flex: 1, minWidth: 0 }}>
        <div
          style={{
            fontWeight: 600,
            fontSize: "0.95rem",
            color: "var(--text)",
            overflow: "hidden",
            textOverflow: "ellipsis",
            whiteSpace: "nowrap",
          }}
        >
          {song.name}
        </div>
        <div
          style={{
            fontSize: "0.8rem",
            color: "var(--muted)",
            marginTop: "0.2rem",
            overflow: "hidden",
            textOverflow: "ellipsis",
            whiteSpace: "nowrap",
          }}
        >
          {song.artist}
        </div>
      </div>

      {/* YouTube Button */}
      <button
        onClick={(e) => {
          e.stopPropagation();
          openYoutube();
        }}
        style={{
          flexShrink: 0,
          padding: "0.4rem 1rem",
          borderRadius: "999px",
          background: "rgba(192,38,211,0.08)",
          border: "1px solid rgba(192,38,211,0.25)",
          color: "var(--pink)",
          cursor: "pointer",
          fontSize: "0.75rem",
          fontWeight: 600,
          fontFamily: "Poppins, sans-serif",
          whiteSpace: "nowrap",
          transition: "all 0.2s",
        }}
        onMouseEnter={(e) => {
          e.currentTarget.style.background = "rgba(192,38,211,0.18)";
          e.currentTarget.style.borderColor = "var(--pink)";
        }}
        onMouseLeave={(e) => {
          e.currentTarget.style.background = "rgba(192,38,211,0.08)";
          e.currentTarget.style.borderColor = "rgba(192,38,211,0.25)";
        }}
      >
        Play on YouTube
      </button>
    </div>
  );
}
