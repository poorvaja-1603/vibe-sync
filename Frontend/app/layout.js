import "./globals.css";
import Navbar from "@/components/Navbar";

export const metadata = {
  title: "VibeSync — Music for Your Mood",
  description: "AI-powered mood detection meets music curation",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <Navbar />
        <main
          style={{
            maxWidth: "900px",
            margin: "0 auto",
            padding: "2rem 1.5rem",
          }}
        >
          {children}
        </main>
      </body>
    </html>
  );
}
