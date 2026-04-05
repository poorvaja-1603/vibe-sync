const EMOTION_CONFIG = {
  happy: {
    label: "Happy",
    bg: "linear-gradient(135deg, #fef08a, #fde047)",
    color: "#713f12",
    border: "#fbbf24",
    desc: "Your energy is high — here is music to keep you going.",
  },
  sad: {
    label: "Sad",
    bg: "linear-gradient(135deg, #bfdbfe, #93c5fd)",
    color: "#1e3a5f",
    border: "#60a5fa",
    desc: "We hear you. Here is something to lift your spirits.",
  },
  angry: {
    label: "Angry",
    bg: "linear-gradient(135deg, #fecaca, #f87171)",
    color: "#7f1d1d",
    border: "#ef4444",
    desc: "Take a breath. Here is music to calm you down.",
  },
  fear: {
    label: "Fear",
    bg: "linear-gradient(135deg, #e9d5ff, #c084fc)",
    color: "#4c1d95",
    border: "#a855f7",
    desc: "You are safe. Here is something soothing.",
  },
  surprise: {
    label: "Surprised",
    bg: "linear-gradient(135deg, #fed7aa, #fb923c)",
    color: "#7c2d12",
    border: "#f97316",
    desc: "What a moment — here is something exciting.",
  },
  neutral: {
    label: "Neutral",
    bg: "linear-gradient(135deg, #e2e8f0, #cbd5e1)",
    color: "#334155",
    border: "#94a3b8",
    desc: "Feeling balanced — here is something chill.",
  },
};

export default function EmotionBadge({ emotion, confidence }) {
  const config = EMOTION_CONFIG[emotion] || EMOTION_CONFIG.neutral;

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "1.25rem",
      }}
    >
      {/* Big color card */}
      <div
        style={{
          width: "200px",
          height: "120px",
          borderRadius: "1.25rem",
          background: config.bg,
          border: `1px solid ${config.border}44`,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          boxShadow: `0 8px 32px ${config.border}33`,
        }}
      >
        <span
          style={{
            fontFamily: "Playfair Display, serif",
            fontSize: "1.8rem",
            fontWeight: 700,
            color: config.color,
          }}
        >
          {config.label}
        </span>
      </div>

      {/* Confidence */}
      {confidence && (
        <span
          style={{
            color: "var(--muted)",
            fontSize: "0.85rem",
            fontWeight: 500,
          }}
        >
          {confidence.toFixed(1)}% confident
        </span>
      )}

      {/* Description */}
      <p
        style={{
          color: "var(--muted)",
          fontSize: "0.9rem",
          textAlign: "center",
          maxWidth: "320px",
          lineHeight: 1.6,
        }}
      >
        {config.desc}
      </p>
    </div>
  );
}
