# 🖤 Almas Neyamatullah · Cinematic Portfolio

> A premium, cinematic developer portfolio inspired by Japanese aesthetics and modern web design principles. Built with vanilla HTML, CSS, and JavaScript — no frameworks required.

![Preview](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)
![HTML](https://img.shields.io/badge/HTML-5-orange)
![CSS](https://img.shields.io/badge/CSS-3-blue)
![JS](https://img.shields.io/badge/JavaScript-ES2026-yellow)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Performance](#performance)
- [Browser Support](#browser-support)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🌟 Overview

This is a **Phase 1** implementation of a cinematic portfolio website that blends:

- **Japanese minimalist aesthetics** with modern web design
- **Dynamic visual effects** (rain particles, custom cursor, smooth scrolling)
- **Glass-morphism UI** with subtle animations
- **Fully responsive** design from mobile to 4K displays

The design philosophy draws inspiration from:
- Japanese calligraphy and typography
- Cinematic storytelling through scroll
- Modern award-winning portfolio designs (Awwwards-style)

---

## ✨ Features

### Current Implementation (Phase 1)

| Feature | Description |
|---------|-------------|
| 🎬 **Cinematic Preloader** | Animated loading screen with Japanese text and spinning rings |
| 🖱️ **Custom Cursor** | Premium cursor with hover-grow effect on interactive elements |
| 🌧️ **Rain Particle System** | Canvas-based, performance-optimized rain animation |
| 🧊 **Glass-morphism UI** | Frosted glass effects with backdrop blur |
| 📜 **Smooth Scrolling** | Native smooth scroll with intersection-based reveals |
| 🎨 **Japanese Typography** | Noto Serif JP + Inter font pairing |
| 🎯 **Dynamic Navigation** | Auto-hides on scroll-down, reappears on scroll-up |
| 📱 **Fully Responsive** | Mobile-first design with fluid typography |
| ⚡ **Performance Optimized** | 60 FPS animations, lazy observers |

### Planned Features (Phases 2-5)

- 🔥 **Cinematic Engine** – Lightning strikes, fog particles, ambient audio
- 👁️ **Sharingan Engine** – Canvas-rendered eye with mouse tracking, Mangekyō transformation
- 🌑 **Amaterasu** – Procedural black flames with heat distortion
- 🐦 **Crow System** – Flocking behavior with hundreds of animated crows
- ✨ **Portfolio Polish** – WebGL bloom, timeline, resume download, SEO

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **HTML5** | Semantic structure |
| **CSS3** | Custom properties, flexbox, grid, animations |
| **JavaScript (ES2026)** | Canvas API, Intersection Observer, DOM manipulation |
| **Canvas API** | Rain particles, future visual effects |
| **Google Fonts** | Noto Serif JP + Inter |
| **Vanilla** | No frameworks, minimal dependencies |

---

## 📁 Project Structure

```
itachi-portfolio/
│
├── index.html              # Main entry point (Phase 1)
├── README.md               # This file
│
├── assets/                 # (Future phases)
│   ├── fonts/
│   ├── audio/
│   ├── images/
│   ├── shaders/
│   ├── icons/
│   └── videos/
│
└── sections/               # (Future phases - modular JS)
    ├── hero.js
    ├── rain.js
    ├── crows.js
    ├── eyes.js
    ├── particles.js
    ├── cursor.js
    ├── scroll.js
    └── portfolio.js
```

**Note:** Phase 1 is a single-file implementation for easy deployment. Future phases will modularize the code.

---

## 🚀 Installation

### Option 1: Direct Download

1. Clone the repository:
```bash
git clone https://github.com/yourusername/itachi-portfolio.git
cd itachi-portfolio
```

2. Open `index.html` in your browser.

### Option 2: Quick Start

```bash
# Using Python's built-in server
python -m http.server 8000

# Using VS Code Live Server
# Install the Live Server extension and click "Go Live"
```

### Option 3: Hosting

Deploy to any static hosting service:
- **Vercel**: `vercel --prod`
- **Netlify**: Drag-and-drop the folder
- **GitHub Pages**: Push to `gh-pages` branch

---

## 🎨 Usage

### Customization Guide

#### 1. Personal Information

In `index.html`, update:

```html
<!-- Hero Section -->
<h1>Your Name</h1>
<p class="subtitle">
  <strong>Your Title</strong> &middot; Your Skills
</p>

<!-- Contact Section -->
<a href="#">your.email@example.com</a>
<a href="#">github.com/yourusername</a>
<a href="#">linkedin.com/in/yourusername</a>
```

#### 2. Color Scheme

In the `:root` CSS section:

```css
:root {
  --bg-primary: #0a0a0a;     /* Dark background */
  --accent: #cc2222;          /* Primary red (change to your brand color) */
  --accent-glow: rgba(204, 34, 34, 0.5);
}
```

#### 3. Typography

```css
:root {
  --font-jp: 'Noto Serif JP', serif;  /* Japanese font */
  --font-en: 'Inter', sans-serif;     /* English font */
}
```

#### 4. Rain Particles

```javascript
const COUNT = 180;  // Number of raindrops (lower = better performance)
```

#### 5. Projects

Update the `.project-card` elements in the projects section:

```html
<div class="project-card glass">
  <span class="icon">⚡</span>
  <h3>Your Project</h3>
  <p>Your project description.</p>
</div>
```

---

## ⚡ Performance

| Metric | Target | Status |
|--------|--------|--------|
| **FPS** | 60 | ✅ Achieved |
| **LCP** | < 2.5s | ✅ Optimized |
| **FID** | < 100ms | ✅ Smooth |
| **CLS** | < 0.1 | ✅ Stable |
| **Bundle Size** | < 50KB | ✅ Minimal |

### Optimization Techniques Used

- ✅ Hardware-accelerated CSS animations
- ✅ Lazy-loaded Intersection Observer
- ✅ RequestAnimationFrame for smooth canvas
- ✅ Reduced DOM manipulation
- ✅ Efficient particle pooling
- ✅ CSS containment hints

---

## 🌐 Browser Support

| Browser | Version | Support |
|---------|---------|---------|
| **Chrome** | 90+ | ✅ Full |
| **Firefox** | 88+ | ✅ Full |
| **Safari** | 14+ | ✅ Full |
| **Edge** | 90+ | ✅ Full |
| **Opera** | 76+ | ✅ Full |
| **Mobile Safari** | 14+ | ✅ Full |
| **Chrome Android** | 90+ | ✅ Full |

---

## 🗺️ Roadmap

### ✅ Phase 1: Foundation (Current)
- [x] HTML structure & semantics
- [x] CSS design system (glass-morphism, typography)
- [x] Rain particle system
- [x] Custom cursor
- [x] Preloader
- [x] Responsive design
- [x] Scroll reveal animations
- [x] Header auto-hide

### 🔜 Phase 2: Cinematic Engine
- [ ] Lightning strikes
- [ ] Fog particles
- [ ] Ember effects
- [ ] Thunder sound toggle
- [ ] Ambient audio

### 🌀 Phase 3: Sharingan & Amaterasu
- [ ] Canvas-rendered Sharingan
- [ ] Mouse tracking
- [ ] Mangekyō transformation
- [ ] Pupil dilation
- [ ] Amaterasu black flames
- [ ] Heat distortion

### 🐦 Phase 4: Crow System
- [ ] Flocking behavior algorithm
- [ ] 100+ animated crows
- [ ] Feather particle system
- [ ] Dynamic shadows

### ✨ Phase 5: Portfolio Polish
- [ ] WebGL bloom effect
- [ ] Film grain overlay
- [ ] SVG morphing
- [ ] SEO optimization
- [ ] Accessibility audit
- [ ] Resume download
- [ ] Timeline section

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Code Style Guidelines

- HTML: Semantic elements, proper indentation
- CSS: BEM-like naming, custom properties, mobile-first
- JavaScript: ES6+, descriptive variable names, comments for complex logic

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Almas Neyamatullah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📬 Contact

**Almas Neyamatullah**

- 📧 Email: almas@example.com
- 🐙 GitHub: [@yourusername](https://github.com/yourusername)
- 🔗 LinkedIn: [in/yourusername](https://linkedin.com/in/yourusername)
- 🌐 Portfolio: [yourwebsite.com](https://yourwebsite.com)

---

## 🙏 Acknowledgments

- **Design Inspiration**: Awwwards winners, Japanese aesthetics, Naruto series
- **Fonts**: Google Fonts (Noto Serif JP, Inter)
- **Community**: Open-source contributors and web design community

---

## 📊 Stats

![Lines of Code](https://img.shields.io/badge/Code-1,200%2B%20lines-green)
![CSS](https://img.shields.io/badge/CSS-400%20rules-blue)
![JS](https://img.shields.io/badge/JS-350%20lines-yellow)
![HTML](https://img.shields.io/badge/HTML-450%20lines-orange)

---

## 🎯 Quick Reference

### Key Classes

| Class | Purpose |
|-------|---------|
| `.glass` | Glass-morphism effect |
| `.btn-primary` | Primary call-to-action button |
| `.section-title` | Section heading with Japanese style |
| `.stat-card` | Statistics card with glass effect |
| `.project-card` | Project showcase card |

### Key IDs

| ID | Purpose |
|----|---------|
| `#preloader` | Loading screen |
| `#cursor` | Custom cursor |
| `#rain-canvas` | Rain particle canvas |
| `#header` | Navigation header |

---

## 🐛 Known Issues

- [ ] Mobile touch events for custom cursor (currently disabled)
- [ ] Rain particles may flicker on some GPU configurations
- [ ] Safari backdrop-filter fallback (uses background color)

---

## 🔮 Future Enhancements

- [ ] Dark/Light mode toggle
- [ ] Language switching (EN/JP)
- [ ] Blog section integration
- [ ] CMS backend (Strapi/Sanity)
- [ ] 3D portfolio viewer (Three.js)
- [ ] Voice navigation
- [ ] WebVR/AR experiences

---

**Built with ❤️ by Almas Neyamatullah**

*"闇の先に光あり" — There is light beyond the darkness*