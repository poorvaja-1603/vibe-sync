"use client";
import { useState } from "react";

export default function SongCard({ song }) {
  const [playing, setPlaying] = useState(false);
  const [audio, setAudio] = useState(null);
  const [finished, setFinished] = useState(false);

  const handlePlay = () => {
    if (!song.preview_url) return;

    if (playing && audio) {
      audio.pause();
      setPlaying(false);
      setAudio(null);
      return;
    }

    const a = new Audio(song.preview_url);
    a.play();
    a.onended = () => {
      setPlaying(false);
      setFinished(true);
    };
    setAudio(a);
    setPlaying(true);
    setFinished(false);
  };

  return (
    <div
      style={{
        background: "var(--surface)",
        border: "1px solid var(--border)",
        borderRadius: "1rem",
        padding: "1rem 1.25rem",
        display: "flex",
        flexDirection: "column",
        gap: "0.75rem",
        boxShadow: "0 2px 8px rgba(124,58,237,0.05)",
        transition: "border-color 0.2s",
      }}
      onMouseEnter={(e) =>
        (e.currentTarget.style.borderColor = "rgba(124,58,237,0.3)")
      }
      onMouseLeave={(e) =>
        (e.currentTarget.style.borderColor = "var(--border)")
      }
    >
      {/* Top row */}
      <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
        {/* Album art */}
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
              fontWeight: 600,
            }}
          >
            ♪
          </div>
        )}

        {/* Song info */}
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

        {/* Play 30s preview */}
        <button
          onClick={handlePlay}
          style={{
            width: "38px",
            height: "38px",
            borderRadius: "50%",
            flexShrink: 0,
            background: playing
              ? "linear-gradient(135deg, var(--purple), var(--lavender))"
              : "rgba(124,58,237,0.1)",
            border: "1px solid rgba(124,58,237,0.3)",
            color: playing ? "#fff" : "var(--purple)",
            cursor: "pointer",
            fontSize: "0.8rem",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            transition: "all 0.2s",
          }}
          title="Play 30s preview"
        >
          {playing ? "■" : "▶"}
        </button>
      </div>

      {/* After preview ends — show full song options */}
      {finished && (
        <div
          style={{
            display: "flex",
            gap: "0.5rem",
            alignItems: "center",
            background: "var(--surface2)",
            borderRadius: "0.6rem",
            padding: "0.5rem 0.75rem",
          }}
        >
          <span style={{ color: "var(--muted)", fontSize: "0.75rem", flex: 1 }}>
            Listen to full song:
          </span>
          <button
            onClick={() => window.open(song.deezer_url, "_blank")}
            style={{
              padding: "0.35rem 0.85rem",
              borderRadius: "999px",
              background: "rgba(124,58,237,0.15)",
              border: "1px solid rgba(124,58,237,0.3)",
              color: "var(--purple)",
              cursor: "pointer",
              fontSize: "0.72rem",
              fontWeight: 600,
              fontFamily: "Poppins, sans-serif",
            }}
          >
            Deezer
          </button>
          <button
            onClick={() => window.open(song.youtube_url, "_blank")}
            style={{
              padding: "0.35rem 0.85rem",
              borderRadius: "999px",
              background: "rgba(192,38,211,0.08)",
              border: "1px solid rgba(192,38,211,0.25)",
              color: "var(--pink)",
              cursor: "pointer",
              fontSize: "0.72rem",
              fontWeight: 600,
              fontFamily: "Poppins, sans-serif",
            }}
          >
            YouTube
          </button>
        </div>
      )}

      {/* Before preview ends — just YouTube */}
      {!finished && (
        <button
          onClick={() => window.open(song.youtube_url, "_blank")}
          style={{
            padding: "0.35rem 1rem",
            borderRadius: "999px",
            alignSelf: "flex-start",
            background: "rgba(192,38,211,0.08)",
            border: "1px solid rgba(192,38,211,0.25)",
            color: "var(--pink)",
            cursor: "pointer",
            fontSize: "0.75rem",
            fontWeight: 600,
            fontFamily: "Poppins, sans-serif",
          }}
        >
          Play on YouTube
        </button>
      )}
    </div>
  );
}
