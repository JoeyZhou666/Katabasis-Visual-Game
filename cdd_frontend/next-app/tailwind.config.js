/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#e75a7c',
        secondary: '#f2b5d4',
        dark: '#2d2d34',
        light: '#fff9f9',
        accent: '#ffbe0b',
      },
      fontFamily: {
        'sans': ['Quicksand', 'Arial', 'sans-serif'],
        'indie': ['Comic Sans MS', 'Comic Sans', 'cursive'],
        'heading': ['Nunito', 'Arial', 'sans-serif'],
      },
    },
  },
  plugins: [],
} 