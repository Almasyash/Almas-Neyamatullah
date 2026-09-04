# Almas Neyamatullah · Cinematic Portfolio 🎬

A visually stunning, cinematic portfolio website showcasing the work of Almas Neyamatullah — a Full Stack Developer, UI/UX Designer, and AI Enthusiast.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/almas-neyamatullah/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/almasyash)
[![MIT License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Made with Love](https://img.shields.io/badge/Made%20with-Love-red?style=flat-square)](https://github.com/almasyash)


---

## 📋 Table of Contents

- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Showcase](#-project-showcase)
- [Project Structure](#-project-structure)
- [Setup & Usage](#-setup--usage)
- [LinkedIn Profile & Social Media Integration](#-linkedin-profile--social-media-integration)
- [Customization Guide](#-customization-guide)
- [Responsive Breakpoints](#-responsive-breakpoints)
- [Design Philosophy](#-design-philosophy)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

### 🎨 Design & Experience
- **Cinematic Dark Theme** — Deep black background (`#0a0a0a`) with subtle radial gradients and glass-morphism effects.
- **Custom Cursor** — Interactive magnetic cursor with hover animations for cards, links, and buttons.
- **Atmospheric Rain Animation** — Lightweight, high-performance HTML5 canvas rain effect.
- **Japanese Typography & Aesthetics** — Elegant blend of *Noto Serif JP* and *Inter* fonts with philosophical accents (静寂, 魂のコード).
- **Smooth Animations** — IntersectionObserver-powered scroll reveals, button glow effects, and transitions.
- **Preloader Animation** — Elegant minimal loading screen with rotating dual rings.

### 📱 Core Functionality
- **Responsive Design** — Pixel-perfect across mobile (<500px), tablet (500–900px), and desktop (>900px).
- **Smart Navigation** — Sticky header that smoothly slides away on scroll down and reveals on scroll up.
- **Interactive Project Modals** — Seamless modal overlays with full-screen iframe launchers, loading spinners, and keyboard (Escape) accessibility.
- **On-Demand Iframe Loading** — Project iframes load asynchronously only when opened, preventing unnecessary bandwidth usage and avoiding unwanted redirects.
- **Contact Form** — Production-ready form integrated with Web3Forms API.

---

## 🛠️ Project Showcase

| Project | Icon | Description | Technologies |
|---|:---:|---|---|
| **Rigid Fitness Club** | 🏋️ | Premium gym & fitness center website in Bettiah featuring memberships, trainers, batch schedules, and interactive BMI/calorie calculator | HTML, CSS, JavaScript, Responsive |
| **Dr. Mugdha Mohan** | 💎 | Skin Care Centre website for Bettiah's top dermatologist featuring patient testimonials, clinic timings, and appointment booking | Healthcare, SEO, Booking, HTML/CSS |
| **Clock & Stopwatch** | ⏰ | Real-time digital clock with live date display and stopwatch with millisecond precision | JavaScript, CSS, HTML |
| **To-Do List** | ✅ | Productive task manager with persistent local storage, CRUD operations, and category filters | LocalStorage, CRUD, Filters, JavaScript |

---

## 🚀 Technologies Used

### Frontend
- **HTML5** — Semantic, accessible markup
- **CSS3** — Custom properties, Flexbox, CSS Grid, backdrop-filter glassmorphism, animations
- **JavaScript (ES6+)** — Modular DOM manipulation, modal controls, canvas animation, responsive interactions

### Typography
- **Noto Serif JP** — Japanese serif styling for headers and accents
- **Inter** — Modern, clean sans-serif for UI elements and body text

### Integrations & Services
- **Web3Forms API** — Serverless contact form submission
- **GitHub Pages** — Automated continuous deployment
- **Playwright Automation** — Automated LinkedIn profile and portfolio synchronization

---

## 📂 Project Structure

```
Almas-Neyamatullah/
├── index.html                           # Main portfolio landing page
├── Rigid-Fitness-Club.html              # Rigid Fitness Club website project
├── Dr. Mugdha Mohan.html                # Dr. Mugdha Mohan Skin Care Centre project
├── Digital Clock & StopWatch.html       # Digital Clock & Stopwatch tool
├── Todo List App.html                   # To-Do List productivity application
├── dr-mugdha.jpg                        # Clinic image asset for Dr. Mugdha Mohan
├── MD Elmas cv.pdf                      # Resume / CV document
├── linkedin-data.json                   # Structured portfolio metadata for LinkedIn
├── automate_linkedin.py                 # Playwright automation script for LinkedIn profile
├── requirements.txt                     # Python dependencies for automation
├── README.md                            # Comprehensive project documentation
└── .github/                             # GitHub configuration & workflows
```

---

## 🌐 LinkedIn Profile & Social Media Integration

This portfolio is connected to LinkedIn for professional showcase and recruiter discovery:

- **LinkedIn Profile**: [https://linkedin.com/in/almas-neyamatullah](https://linkedin.com/in/almas-neyamatullah)
- **Profile Headline**: `Full Stack Developer | UI/UX Designer | AI Enthusiast | Cinematic Portfolio Creator`
- **Featured Section Link**: Points directly to [https://almasyash.github.io/Almas-Neyamatullah/](https://almasyash.github.io/Almas-Neyamatullah/)

### Profile Automation
To sync portfolio projects, headline, about section, and featured links directly to your LinkedIn profile:

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

2. **Preview profile data (Dry Run)**:
   ```bash
   python automate_linkedin.py --dry-run
   ```

3. **Run automated browser setup**:
   ```bash
   python automate_linkedin.py
   ```
   *The script opens a visible browser window, prompts you to sign in safely with your 2FA, and updates your headline, about summary, and featured portfolio links.*

---

## 🔧 Setup & Usage

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Almasyash/Almas-Neyamatullah.git
   ```

2. **Navigate to the project directory**
   ```bash
   cd Almas-Neyamatullah
   ```

3. **Run locally**
   - Open `index.html` directly in any modern browser, or
   - Use VS Code extension **Live Server** (`Go Live`) for hot reload.

### Deployment

The portfolio is deployed directly via **GitHub Pages**:
- **Live URL**: [https://almasyash.github.io/Almas-Neyamatullah/](https://almasyash.github.io/Almas-Neyamatullah/)

Any push to the `main` branch automatically triggers GitHub Pages to build and deploy the updated site.

---

## 🎯 Customization Guide

### Update Personal Details

| Item | File | Location |
|---|---|---|
| **Full Name / Title** | `index.html` | Hero section (`#hero`) |
| **About Bio & Skills** | `index.html` | About section (`#about`) |
| **Social Links & Email** | `index.html` | Contact section (`#contact`) |
| **LinkedIn URL** | `index.html` & `linkedin-data.json` | Contact list & JSON |
| **Resume PDF** | Root | Replace `MD Elmas cv.pdf` |

### Adding or Modifying a Project

1. Add a new `.html` project file into the repository root.
2. Add a project card inside `<div class="projects-grid">` in `index.html`:
   ```html
   <div class="project-card glass" id="myProjectTrigger">
       <span class="icon">🚀</span>
       <h3>My New Project</h3>
       <p>Description of what the project does.</p>
       <div class="tech-tags">
           <span>HTML</span>
           <span>CSS</span>
           <span>JavaScript</span>
       </div>
       <p class="launch-hint">▶ Click to launch</p>
   </div>
   ```
3. Add the corresponding modal overlay with an iframe:
   ```html
   <div class="modal-overlay" id="myProjectModal">
       <div class="modal-content">
           <button class="modal-close" id="myProjectModalClose">✕</button>
           <h2>🚀 My New Project</h2>
           <div class="project-iframe-container">
               <div class="iframe-loader" id="myProjectLoader"></div>
               <iframe id="myProjectIframe" src="" data-src="My-Project.html" allow="autoplay; fullscreen"></iframe>
           </div>
           <div style="margin-top: 15px; display: flex; gap: 15px;">
               <a href="My-Project.html" target="_blank" class="btn btn-primary">Open Full Screen</a>
               <button class="btn btn-outline" id="myProjectModalCloseBtn">Close</button>
           </div>
       </div>
   </div>
   ```
4. Hook up open/close event listeners in the `<script>` section.

---

## 📱 Responsive Breakpoints

| Device | Breakpoint | Layout Behavior |
|---|---|---|
| **Desktop** | `> 900px` | Multi-column grid, horizontal navigation bar, 70vh iframes |
| **Tablet** | `500px - 900px` | Single-column about/contact grids, compact 50vh iframes |
| **Mobile** | `< 500px` | Streamlined cards, 2-column stat counters, 40vh iframes |

---

## 🎨 Design Philosophy

- **Japanese Minimalism (侘寂)** — Intentional whitespace, purposeful typography, and clean contrast.
- **Cinematic Atmosphere** — Dark ambient canvas effects paired with crimson accent highlights (`#cc2222`).
- **Glassmorphism** — Layered frosted glass panels with `backdrop-filter: blur(12px)`.
- **Performance First** — Zero heavy external JavaScript frameworks; vanilla execution for instant load times.

---

## 📄 License

This project is licensed under the **MIT License** — see below for details:

```
MIT License

Copyright (c) 2026 Almas Neyamatullah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Contact

**Almas Neyamatullah**  
- 📧 Email: [almasneyamt786@gmail.com](mailto:almasneyamt786@gmail.com)  
- 💼 LinkedIn: [almas-neyamatullah](https://linkedin.com/in/almas-neyamatullah)  
- 🐙 GitHub: [@Almasyash](https://github.com/Almasyash)  
- 🌐 Portfolio: [almasyash.github.io/Almas-Neyamatullah](https://almasyash.github.io/Almas-Neyamatullah/)  
- 📄 Resume: [Download CV (PDF)](MD%20Elmas%20cv.pdf)

---

⭐ *Star this repository if you like the cinematic theme!*
