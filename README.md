# Almas Neyamatullah · Cinematic Portfolio 🎬

A visually stunning, cinematic portfolio website showcasing the work of Almas Neyamatullah — a Full Stack Developer, UI/UX Designer, and AI Enthusiast. This portfolio blends Japanese aesthetics with modern web technologies to create an immersive experience.

## ✨ Features

### 🎨 Design & Experience
- **Cinematic Dark Theme** — Deep black with subtle gradients and glass-morphism effects
- **Custom Cursor** — Interactive cursor with hover effects for enhanced user experience
- **Rain Animation** — Atmospheric rain canvas effect in the background
- **Japanese Typography** — Beautiful blend of Noto Serif JP and Inter fonts
- **Smooth Animations** — Scroll reveals, hover effects, and smooth transitions

### 📱 Core Functionality
- **Responsive Design** — Fully responsive across all devices
- **Preloader Animation** — Elegant loading screen with spinning ring
- **Smart Navigation** — Auto-hiding header on scroll down
- **Project Showcase** — Interactive project cards with modal previews

### 🛠️ Projects Included
1. **⚡ Neon Pulse** — Real-time WebGL particle system with audio reactivity
2. **⏰ Clock & Stopwatch** — Digital clock with date display & stopwatch with millisecond precision
3. **🌊 Zen Flow** — Meditation app with dynamic ambient soundscapes
4. **✅ To-Do List** — Productive task manager with local storage & smart filters

### 📬 Contact & Social
- Integrated contact form with Web3Forms API
- Social links (GitHub, LinkedIn, Portfolio, Email)
- Resume download option

## 🚀 Technologies Used

### Frontend
- **HTML5** — Semantic markup
- **CSS3** — Custom properties, Flexbox, Grid, Animations
- **JavaScript** — Vanilla JS for interactivity, animations, and modals

### Fonts
- **Noto Serif JP** — Japanese typography
- **Inter** — Clean, modern sans-serif

### External Services
- **Web3Forms** — Contact form handling

## 📂 Project Structure

```
portfolio/
├── index.html                 # Main portfolio file
├── Neon Pulse.html            # Neon Pulse project
├── Digital Clock & StopWatch.html  # Clock & Stopwatch project
├── Zen Flow.html              # Zen Flow project
├── Todo List App.html         # To-Do List project
├── MD Elmas cv.pdf            # Resume PDF
└── README.md                  # This file
```

## 🔧 Setup & Usage

### Local Development
1. **Clone the repository**
   ```bash
   git clone https://github.com/Almasyash/Almas-Neyamatullah.git
   ```

2. **Navigate to project directory**
   ```bash
   cd Almas-Neyamatullah
   ```

3. **Open the website**
   - Simply open `index.html` in your browser
   - Or use a live server extension (VS Code: Live Server)

### Deployment
The portfolio is hosted on GitHub Pages:
- **Live URL**: [https://almasyash.github.io/Almas-Neyamatullah/](https://almasyash.github.io/Almas-Neyamatullah/)

To deploy your own version:
1. Fork this repository
2. Enable GitHub Pages in repository settings
3. Push changes to the `main` branch

## 🎯 Customization Guide

### Update Personal Information
- **Email**: Change `mailto:almasneyamt786@gmail.com` in contact links
- **GitHub**: Update `https://github.com/Almasyash`
- **LinkedIn**: Add your LinkedIn URL
- **Resume**: Replace `MD Elmas cv.pdf` with your resume

### Modify Projects
Each project card in `#projects` section can be:
- **Renamed**: Update `<h3>` text
- **Re-iconed**: Change the `<span class="icon">` emoji
- **Re-described**: Edit the `<p>` description
- **Re-tagged**: Modify tech tags in `<div class="tech-tags">`

### Update Contact Form
The form uses Web3Forms API. To use your own endpoint:
1. Create an account at [Web3Forms](https://web3forms.com/)
2. Get your access key
3. Update the `access_key` value in the form:
   ```html
   <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY">
   ```

### Change Colors
Customize the theme by updating CSS variables in `:root`:
```css
:root {
    --bg-primary: #0a0a0a;      /* Background */
    --accent: #cc2222;           /* Primary accent color */
    --text-primary: #f0ece4;     /* Main text color */
    --text-secondary: #b8b0a4;   /* Secondary text color */
}
```

## 📱 Responsive Breakpoints

- **Desktop**: > 900px — Full layout
- **Tablet**: 500px - 900px — Adjusted grid layouts
- **Mobile**: < 500px — Compact design, smaller text

## 🎨 Design Philosophy

This portfolio draws inspiration from:
- **Japanese Minimalism** — Clean, uncluttered design
- **Cinematic Aesthetics** — Dark themes, dramatic lighting
- **Glass-morphism** — Frosted glass effects for depth
- **Atmospheric Elements** — Rain animation for immersion

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Fonts**: Google Fonts (Noto Serif JP, Inter)
- **Form Handling**: Web3Forms
- **Inspiration**: Japanese aesthetics and modern web design trends

## 📞 Contact

**Almas Neyamatullah**  
- 📧 Email: almasneyamt786@gmail.com  
- 🐙 GitHub: [Almasyash](https://github.com/Almasyash)  
- 🌐 Portfolio: [almasyash.github.io/Almas-Neyamatullah](https://almasyash.github.io/Almas-Neyamatullah/)

---

*Built with ❤️ and caffeine.*
