"use client";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import EmotionBadge from "@/components/EmotionBadge";
import SongCard from "@/components/SongCard";

export default function ResultsPage() {
  const [result, setResult] = useState(null);
  const router = useRouter();

  useEffect(() => {
    const stored = sessionStorage.getItem("emotion_result");
    if (!stored) {
      router.push("/detect");
      return;
    }
    setResult(JSON.parse(stored));
  }, []);

  const rescan = () => {
    sessionStorage.removeItem("emotion_result");
    router.push("/detect");
  };

  if (!result)
    return (
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          height: "60vh",
          color: "var(--muted)",
          fontFamily: "Poppins, sans-serif",
        }}
      >
        Loading...
      </div>
    );

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "3.5rem",
        paddingTop: "3rem",
        paddingBottom: "4rem",
      }}
    >
      {/* Emotion */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "0.5rem",
        }}
      >
        <span
          style={{
            color: "var(--muted)",
            fontSize: "0.75rem",
            letterSpacing: "0.12em",
            textTransform: "uppercase",
            fontWeight: 600,
          }}
        >
          Your mood right now
        </span>
        <EmotionBadge emotion={result.emotion} confidence={result.confidence} />
      </div>

      {/* Divider */}
      <div
        style={{
          width: "100%",
          maxWidth: "520px",
          height: "1px",
          background: "var(--border)",
        }}
      />

      {/* Songs */}
      <div
        style={{
          width: "100%",
          maxWidth: "520px",
          display: "flex",
          flexDirection: "column",
          gap: "1.5rem",
        }}
      >
        <div>
          <h2
            style={{
              fontFamily: "Playfair Display, serif",
              fontSize: "1.6rem",
              color: "var(--text)",
            }}
          >
            Songs for you
          </h2>
          <p
            style={{
              color: "var(--muted)",
              fontSize: "0.85rem",
              marginTop: "0.25rem",
            }}
          >
            Selected to match or lift your mood
          </p>
        </div>

        {result.songs.length === 0 ? (
          <p
            style={{
              color: "var(--muted)",
              textAlign: "center",
              padding: "2rem",
            }}
          >
            No songs found. Try scanning again.
          </p>
        ) : (
          <div
            style={{ display: "flex", flexDirection: "column", gap: "0.75rem" }}
          >
            {result.songs.map((song, i) => (
              <SongCard key={i} song={song} />
            ))}
          </div>
        )}
      </div>

      {/* Rescan */}
      <button
        onClick={rescan}
        style={{
          background: "var(--surface)",
          border: "1px solid var(--border)",
          color: "var(--muted)",
          padding: "0.75rem 2rem",
          borderRadius: "999px",
          cursor: "pointer",
          fontSize: "0.9rem",
          fontFamily: "Poppins, sans-serif",
          fontWeight: 500,
          transition: "all 0.2s",
          boxShadow: "0 2px 8px rgba(124,58,237,0.05)",
        }}
        onMouseEnter={(e) => {
          e.currentTarget.style.borderColor = "var(--purple)";
          e.currentTarget.style.color = "var(--purple)";
        }}
        onMouseLeave={(e) => {
          e.currentTarget.style.borderColor = "var(--border)";
          e.currentTarget.style.color = "var(--muted)";
        }}
      >
        Scan Again
      </button>
    </div>
  );
}
