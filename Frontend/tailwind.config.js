/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/**/*.{js,jsx}", "./components/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#0f0d14",
        surface: "#1a1625",
        surface2: "#221d30",
        border: "#2e2840",
        purple: "#c084fc",
        pink: "#f0abfc",
        lavender: "#a78bfa",
        muted: "#9d95b5",
      },
      fontFamily: {
        sans: ["Poppins", "sans-serif"],
        display: ["Poppins", "serif"],
      },
    },
  },
  plugins: [],
};
