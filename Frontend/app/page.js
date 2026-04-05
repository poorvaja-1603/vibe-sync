"use client";
import Link from "next/link";

const STEPS = [
  {
    num: "01",
    title: "Show Your Face",
    desc: "Allow camera access. Our model detects your face in real time using OpenCV.",
  },
  {
    num: "02",
    title: "AI Reads Your Mood",
    desc: "A CNN trained on FER2013 analyses your facial expression and classifies your emotion.",
  },
  {
    num: "03",
    title: "Music Plays",
    desc: "Songs are fetched from JioSaavn matching your mood. Click to play on YouTube.",
  },
];

const EMOTIONS = [
  { label: "Angry", color: "#f87171", bg: "rgba(248,113,113,0.1)" },
  { label: "Fear", color: "#c084fc", bg: "rgba(192,132,252,0.1)" },
  { label: "Happy", color: "#fbbf24", bg: "rgba(251,191,36,0.1)" },
  { label: "Neutral", color: "#94a3b8", bg: "rgba(148,163,184,0.1)" },
  { label: "Sad", color: "#60a5fa", bg: "rgba(96,165,250,0.1)" },
  { label: "Surprise", color: "#fb923c", bg: "rgba(251,146,60,0.1)" },
];

export default function Home() {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "6rem",
        paddingTop: "4rem",
      }}
    >
      {/* Hero */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "2rem",
          maxWidth: "600px",
        }}
      >
        <div
          style={{
            display: "inline-block",
            fontSize: "0.75rem",
            fontWeight: 600,
            letterSpacing: "0.15em",
            textTransform: "uppercase",
            color: "var(--purple)",
            border: "1px solid rgba(124, 58, 237, 0.25)",
            padding: "0.35rem 0.85rem",
            borderRadius: "999px",
            width: "fit-content",
            background: "rgba(124, 58, 237, 0.06)",
          }}
        >
          AI Powered Mood Detection
        </div>

        <h1
          style={{
            fontFamily: "Playfair Display, serif",
            fontSize: "clamp(2.8rem, 6vw, 4.5rem)",
            fontWeight: 700,
            lineHeight: 1.1,
            letterSpacing: "-0.02em",
            color: "var(--text)",
          }}
        >
          Music that feels
          <br />
          <span
            style={{
              background: "linear-gradient(135deg, var(--purple), var(--pink))",
              WebkitBackgroundClip: "text",
              WebkitTextFillColor: "transparent",
            }}
          >
            like you.
          </span>
        </h1>

        <p
          style={{
            color: "var(--muted)",
            fontSize: "1.1rem",
            lineHeight: 1.7,
            maxWidth: "480px",
          }}
        >
          We read your face, detect your emotion, and curate music to match or
          shift your mood. Powered by a CNN trained from scratch on FER2013.
        </p>

        <Link
          href="/detect"
          style={{
            display: "inline-block",
            background:
              "linear-gradient(135deg, var(--purple), var(--lavender))",
            color: "#ffffff",
            fontWeight: 600,
            padding: "0.9rem 2.2rem",
            borderRadius: "999px",
            textDecoration: "none",
            fontSize: "0.95rem",
            letterSpacing: "0.02em",
            width: "fit-content",
            fontFamily: "Poppins, sans-serif",
            boxShadow: "0 4px 20px rgba(124, 58, 237, 0.25)",
          }}
        >
          Detect My Mood
        </Link>
      </div>

      {/* How It Works */}
      <div style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
        <h2
          style={{
            fontFamily: "Playfair Display, serif",
            fontSize: "1.8rem",
            color: "var(--text)",
          }}
        >
          How it works
        </h2>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))",
            gap: "1.5rem",
          }}
        >
          {STEPS.map(({ num, title, desc }) => (
            <div
              key={num}
              style={{
                background: "var(--surface)",
                border: "1px solid var(--border)",
                borderRadius: "1.25rem",
                padding: "2rem",
                display: "flex",
                flexDirection: "column",
                gap: "1rem",
                boxShadow: "0 2px 12px rgba(124, 58, 237, 0.06)",
              }}
            >
              <span
                style={{
                  fontFamily: "Playfair Display, serif",
                  fontSize: "2.5rem",
                  fontWeight: 700,
                  background:
                    "linear-gradient(135deg, var(--purple), var(--pink))",
                  WebkitBackgroundClip: "text",
                  WebkitTextFillColor: "transparent",
                  lineHeight: 1,
                }}
              >
                {num}
              </span>
              <h3
                style={{
                  fontSize: "1rem",
                  fontWeight: 600,
                  color: "var(--text)",
                  fontFamily: "Poppins, sans-serif",
                }}
              >
                {title}
              </h3>
              <p
                style={{
                  color: "var(--muted)",
                  fontSize: "0.875rem",
                  lineHeight: 1.6,
                }}
              >
                {desc}
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Emotions */}
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "1.5rem",
          paddingBottom: "4rem",
        }}
      >
        <h2
          style={{
            fontFamily: "Playfair Display, serif",
            fontSize: "1.8rem",
            color: "var(--text)",
          }}
        >
          Emotions we detect
        </h2>
        <div style={{ display: "flex", gap: "0.75rem", flexWrap: "wrap" }}>
          {EMOTIONS.map(({ label, color, bg }) => (
            <span
              key={label}
              style={{
                background: "var(--surface)",
                border: "1px solid var(--border)",
                color: "var(--muted)",
                padding: "0.5rem 1.25rem",
                borderRadius: "999px",
                fontSize: "0.85rem",
                fontWeight: 500,
                cursor: "default",
                transition: "all 0.2s",
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.background = bg;
                e.currentTarget.style.borderColor = color;
                e.currentTarget.style.color = color;
                e.currentTarget.style.transform = "translateY(-2px)";
                e.currentTarget.style.boxShadow = `0 4px 12px ${color}33`;
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.background = "var(--surface)";
                e.currentTarget.style.borderColor = "var(--border)";
                e.currentTarget.style.color = "var(--muted)";
                e.currentTarget.style.transform = "translateY(0)";
                e.currentTarget.style.boxShadow = "none";
              }}
            >
              {label}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}
