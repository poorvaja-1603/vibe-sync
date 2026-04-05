"use client";
import Link from "next/link";

export default function Navbar() {
  return (
    <nav
      style={{
        borderBottom: "1px solid var(--border)",
        padding: "1.25rem 2rem",
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        backdropFilter: "blur(12px)",
        position: "sticky",
        top: 0,
        zIndex: 50,
        backgroundColor: "rgba(240, 237, 248, 0.85)",
      }}
    >
      <Link
        href="/"
        style={{
          fontFamily: "Playfair Display, serif",
          fontSize: "1.4rem",
          fontWeight: 700,
          background: "linear-gradient(135deg, var(--purple), var(--pink))",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent",
          textDecoration: "none",
        }}
      >
        VibeSync
      </Link>

      <div style={{ display: "flex", gap: "2rem" }}>
        {[
          ["Home", "/"],
          ["Try It", "/detect"],
        ].map(([label, href]) => (
          <Link
            key={href}
            href={href}
            style={{
              color: "var(--muted)",
              textDecoration: "none",
              fontSize: "0.9rem",
              fontWeight: 500,
              letterSpacing: "0.02em",
            }}
          >
            {label}
          </Link>
        ))}
      </div>
    </nav>
  );
}
