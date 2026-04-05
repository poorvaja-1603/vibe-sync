"use client";
import { useRef, useEffect, useState } from "react";
import { useRouter } from "next/navigation";

export default function DetectPage() {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [cameraReady, setCameraReady] = useState(false);
  const router = useRouter();

  useEffect(() => {
    startCamera();
    return () => stopCamera();
  }, []);

  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        setCameraReady(true);
      }
    } catch {
      setError("Camera access denied. Please allow camera access and refresh.");
    }
  };

  const stopCamera = () => {
    if (videoRef.current?.srcObject)
      videoRef.current.srcObject.getTracks().forEach((t) => t.stop());
  };

  const captureAndDetect = async () => {
    if (!videoRef.current || !canvasRef.current) return;
    setLoading(true);
    setError(null);

    const canvas = canvasRef.current;
    const video = videoRef.current;
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext("2d").drawImage(video, 0, 0);

    canvas.toBlob(async (blob) => {
      try {
        const formData = new FormData();
        formData.append("file", blob, "frame.jpg");

        const API_URL =
          process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";
        const response = await fetch(`${API_URL}/predict`, {
          method: "POST",
          body: formData,
        });

        if (!response.ok) {
          const err = await response.json();
          throw new Error(err.detail || "Detection failed");
        }

        const data = await response.json();
        stopCamera();
        sessionStorage.setItem("emotion_result", JSON.stringify(data));
        router.push("/results");
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    }, "image/jpeg");
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: "2.5rem",
        paddingTop: "3rem",
      }}
    >
      <div style={{ textAlign: "center" }}>
        <h1
          style={{
            fontFamily: "Playfair Display, serif",
            fontSize: "2.5rem",
            fontWeight: 700,
            color: "var(--text)",
          }}
        >
          Detect Your Mood
        </h1>
        <p
          style={{
            color: "var(--muted)",
            fontSize: "1rem",
            marginTop: "0.5rem",
          }}
        >
          Look at the camera and click the button when ready
        </p>
      </div>

      {/* Video */}
      <div
        style={{
          position: "relative",
          width: "100%",
          maxWidth: "520px",
          aspectRatio: "4/3",
          borderRadius: "1.5rem",
          overflow: "hidden",
          background: "var(--surface2)",
          border: "1px solid var(--border)",
          boxShadow: "0 4px 24px rgba(124, 58, 237, 0.08)",
        }}
      >
        <video
          ref={videoRef}
          autoPlay
          playsInline
          muted
          style={{ width: "100%", height: "100%", objectFit: "cover" }}
        />
        {!cameraReady && (
          <div
            style={{
              position: "absolute",
              inset: 0,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "var(--muted)",
              fontSize: "0.9rem",
            }}
          >
            Starting camera...
          </div>
        )}

        {/* Corner accents */}
        {[
          { top: "12px", left: "12px", borderWidth: "2px 0 0 2px" },
          { top: "12px", right: "12px", borderWidth: "2px 2px 0 0" },
          { bottom: "12px", left: "12px", borderWidth: "0 0 2px 2px" },
          { bottom: "12px", right: "12px", borderWidth: "0 2px 2px 0" },
        ].map((style, i) => (
          <div
            key={i}
            style={{
              position: "absolute",
              width: "20px",
              height: "20px",
              borderColor: "var(--purple)",
              borderStyle: "solid",
              ...style,
            }}
          />
        ))}
      </div>

      <canvas ref={canvasRef} style={{ display: "none" }} />

      {error && (
        <div
          style={{
            background: "rgba(239, 68, 68, 0.08)",
            border: "1px solid rgba(239, 68, 68, 0.25)",
            color: "#dc2626",
            padding: "0.75rem 1.25rem",
            borderRadius: "0.75rem",
            fontSize: "0.875rem",
            maxWidth: "520px",
            width: "100%",
          }}
        >
          {error}
        </div>
      )}

      <button
        onClick={captureAndDetect}
        disabled={!cameraReady || loading}
        style={{
          background:
            cameraReady && !loading
              ? "linear-gradient(135deg, var(--purple), var(--lavender))"
              : "var(--surface2)",
          color: cameraReady && !loading ? "#ffffff" : "var(--muted)",
          border: "none",
          fontWeight: 600,
          padding: "1rem 3rem",
          borderRadius: "999px",
          fontSize: "1rem",
          cursor: cameraReady && !loading ? "pointer" : "not-allowed",
          transition: "all 0.2s",
          fontFamily: "Poppins, sans-serif",
          letterSpacing: "0.02em",
          boxShadow:
            cameraReady && !loading
              ? "0 4px 20px rgba(124, 58, 237, 0.3)"
              : "none",
        }}
      >
        {loading ? "Analysing..." : "Detect My Mood"}
      </button>
    </div>
  );
}
