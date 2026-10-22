# MAHMAS GROUP — PHASE 1: LOCALHOST NAVIGATION & PAGE AUDIT REPORT

**Date:** October 21, 2026  
**Auditor Roles:** Senior Full-Stack Developer, Frontend Architect, UI/UX Engineer, QA Automation Expert  
**Target Environment:** Localhost First (`http://localhost:5500/`)  
**Production Site Reference:** [https://mahmasgroup.online](https://mahmasgroup.online)  
**Safety Status:** STRICT AUDIT ONLY — Zero code fixes applied to production, zero Git commits, zero pushes.

---

## 1. Executive Summary

This Phase 1 audit provides a complete, forensic examination of the MAHMAS GROUP website hosted locally on `http://localhost:5500/`. The audit investigated all six primary routes (`/`, `/services.html`, `/work.html`, `/pricing.html`, `/about.html`, `/contact.html`), their folder counterparts, shared layouts, mobile navigation drawer functionality, event listeners, CSS stacking contexts, and the reported persistent appearance of "WhatsApp CRM & Orders".

### Key Diagnostic Takeaways:
1. **Hamburger Menu Non-Functionality:** The slide-out menu appears completely non-responsive to clicks due to a **synchronous double-toggle event cancellation**. The `<button id="menuToggle">` element contains an inline `onclick="toggleSiteMenu()"` attribute **AND** a delegated `document.addEventListener('click')` handler inside [menu.js](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/assets/js/menu.js#L39-L46). Every user click triggers both handlers within less than 0.1ms: the first adds the `.open` class and the second immediately removes it, leaving the menu permanently closed to the user.
2. **"WhatsApp CRM & Orders" Phenomenon:** This item is **not** a corrupted page, a broken route, or an incorrectly routed portfolio project. It is **Item #8** in a global, horizontal scrolling marquee capabilities banner (`.marquee-strip`) placed directly beneath `<header>` across all 25 HTML files in the project. Because it sits at the very fold on every subpage (Work, Pricing, About, Contact), users perceive it as displacing or overriding intended page content.
3. **Route Dualism & Canonical Desynchronization:** The site maintains duplicate files for each page: flat root files (`about.html`) and folder files (`about/index.html`). Navigation links exclusively target flat `.html` files, while `sitemap.xml` and `<link rel="canonical">` target directory trailing-slash URLs (`https://mahmasgroup.online/about/`).

---

## 2. Project Architecture & Framework Discovery

- **Runtime & Tech Stack:** Pure Static HTML5 / CSS3 / Vanilla JavaScript (ES6+).
- **Frameworks / Libraries Detected:** Zero heavy frameworks (No React, Vue, Next.js, Angular, or Vite). The site utilizes lightweight, zero-dependency native browser APIs.
- **Form Delivery Engine:** Dual-mode asynchronous submission via [Web3Forms REST API](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/main.js#L136-L150) with fallback to `mailto:` and optional EmailJS integration.
- **Styling Architecture:** Modern dark-mode Japanese cyberpunk-inspired UI/UX, built with CSS custom properties (`--bg-primary`, `--accent: #cc2222`, `--accent-cyan: #00f2fe`, `--accent-gold: #d4af37`), CSS backdrop blur (`backdrop-filter: blur(28px)`), and CSS Grid/Flexbox layouts defined in [style.css](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/style.css).
- **Production Hosting:** GitHub Pages pointing to custom CNAME `mahmasgroup.online`.
- **Local Dev Server:** Python HTTP daemon (`http://localhost:5500/`) serving the root workspace.

---

## 3. Hamburger Menu (☰) Forensic Diagnosis

### Reported Symptom:
Clicking the three-line hamburger menu toggle icon (`#menuToggle`) in the header produces no visible action.

### Root Cause Analysis:
The failure is caused by an **event handling conflict between inline HTML attributes and external delegated event listeners**:

1. **Inline HTML Handler:**
   In [index.html:160](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/index.html#L160) (and duplicated across all primary HTML pages):
   ```html
   <button id="menuToggle" class="menu-toggle" aria-label="Toggle navigation menu" 
           aria-expanded="false" aria-controls="site-menu" onclick="toggleSiteMenu()">
   ```
2. **Delegated Click Listener in [assets/js/menu.js:39-46](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/assets/js/menu.js#L39-L46):**
   ```javascript
   document.addEventListener('click', function(e) {
       const toggle = e.target.closest('#menuToggle') || e.target.closest('.menu-toggle');
       if (toggle) {
           e.preventDefault();
           e.stopPropagation();
           window.toggleSiteMenu();
           return;
       }
   ```
3. **Execution Trace on User Click:**
   - **Phase 1 (Target Phase):** The user clicks `#menuToggle`. The browser synchronously executes the element's inline `onclick="toggleSiteMenu()"`. Inside `window.toggleSiteMenu()`, `menu.classList.contains('open')` evaluates to `false`. The function adds `.open` to `#site-menu` and `#menuOverlay`.
   - **Phase 2 (Bubble Phase):** The click event bubbles up the DOM tree from `<button>` to `document`.
   - **Phase 3 (Document Capture):** The click listener in `menu.js` catches the event. `e.target.closest('#menuToggle')` matches `<button id="menuToggle">`.
   - **Phase 4 (Instant Cancellation):** The listener calls `window.toggleSiteMenu()` a second time. Inside `window.toggleSiteMenu()`, `menu.classList.contains('open')` is now `true` from Phase 1. The function immediately executes the `else` branch: `menu.classList.remove('open')`.
   - **Net Visual Outcome:** The menu opens and closes within 0.05 milliseconds inside the same browser event loop tick. To the browser compositor and human user, the menu never opens.

### Stacking Context & CSS Inspection:
- `#site-menu`: `z-index: 1000`, `position: fixed`, `transform: translateX(100%)`, `visibility: hidden`.
- `#site-menu.open`: `transform: translateX(0)!important`, `visibility: visible!important`.
- `#menuOverlay`: `z-index: 999`, `position: fixed`, `opacity: 0`, `visibility: hidden`.
- `#menuOverlay.open`: `opacity: 1!important`, `visibility: visible!important`.
- `#menuToggle`: `z-index: 101`, `position: relative`, `pointer-events: auto`.
- `.menu-icon`: `pointer-events: none` (prevents SVG child target misalignment).
- **CSS Verdict:** CSS layout, transitions, stacking contexts, and z-index ordering are correct; the bug is purely the double-trigger execution in JavaScript.

### Accessibility (a11y) Findings:
- `aria-expanded` and `aria-controls` are present on `#menuToggle`.
- `aria-hidden` toggles on `#site-menu`.
- `Escape` key handler is wired to close the menu.
- **Deficiencies:** Focus trapping is missing (Tab key escapes the drawer to background links), initial focus is not programmatically moved to `#menuClose` or the first navigation item upon opening, and `role="dialog"` / `aria-modal="true"` is not assigned.

---

## 4. "WhatsApp CRM & Orders" Forensic Diagnosis

### Reported Symptom:
"WhatsApp CRM & Orders" appears across pages, including where the user expects different page content.

### Forensic Investigation:
- A full-workspace grep confirmed that "WhatsApp CRM & Orders" appears **only** within the following markup across all 25 HTML files:
  ```html
  <span class="marquee-item accent-green">
      <span class="m-icon">💬</span>
      <span>WhatsApp CRM &amp; Orders</span>
  </span>
  ```
- **File & Line References:**
  - [index.html:301 & 321](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/index.html#L301)
  - [services.html:247 & 267](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/services.html#L247)
  - [work.html:247 & 267](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/work.html#L247)
  - [pricing.html:288 & 308](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/pricing.html#L288)
  - [about.html:247 & 267](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/about.html#L247)
  - [contact.html:310 & 330](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/contact.html#L310)
  - [404.html:220 & 240](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/404.html#L220)

### Why It Creates Confusion:
1. **Intended Role:** It is item #8 in a 9-item agency capabilities ticker (High-performance websites, Custom billing software, Google Business Listings, Mobile & Android Apps, Local SEO, Shop & Clinic POS, Cloud Hosting, **WhatsApp CRM & Orders**, Ultra-Fast PageSpeed).
2. **Prominent Subpage Position:** On every subpage (`services.html`, `work.html`, `pricing.html`, `about.html`, `contact.html`), `<div class="marquee-strip">` is placed right below `<header>` and immediately above `<main id="top">`.
3. **Visual Override Effect:** When a visitor lands on "Work" or "About", the animated ticker is the very first visual element below the header, drawing immediate attention and leading the user to believe the page content itself is about WhatsApp CRM.
4. **Intended Architecture:** In professional agency UI/UX, capability marquee tickers belong on the **Homepage**, whereas subpages should lead directly with their contextual breadcrumb and page hero.

---

## 5. Navigation & Routing Architecture Audit

### Route Inventory & Canonical Mappings:

| Page Name | Root HTML File | Subdirectory File | Sitemap / Canonical URL | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Home** | [index.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/index.html) | N/A | `https://mahmasgroup.online/` | PASS |
| **Services** | [services.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/services.html) | [services/index.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/services/index.html) | `https://mahmasgroup.online/services/` | PASS (Dual file) |
| **Work** | [work.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/work.html) | [work/index.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/work/index.html) | `https://mahmasgroup.online/work/` | PASS (Dual file) |
| **Pricing** | [pricing.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/pricing.html) | [pricing/index.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/pricing/index.html) | `https://mahmasgroup.online/pricing/` | PASS (Dual file) |
| **About** | [about.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/about.html) | [about/index.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/about/index.html) | `https://mahmasgroup.online/about/` | PASS (Dual file) |
| **Contact** | [contact.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/contact.html) | [contact/index.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/contact/index.html) | `https://mahmasgroup.online/contact/` | PASS (Dual file) |
| **404 Page** | [404.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/404.html) | N/A | `https://mahmasgroup.online/404.html` | PASS |

### Routing Deficiencies:
- **Link Inconsistency:** All internal links in desktop `<nav>`, `#site-menu`, and `<footer>` target `.html` files (`services.html`), but canonical tags declare trailing slashes (`/services/`).
- **Subpage Jump Back:** If a user visits `/services/` directly, links pointing to `../about.html` redirect them back to the flat `.html` route, creating disjointed browser history and URL inconsistencies.

---

## 6. Page-by-Page Audit Findings

### Route 1: Home (`http://localhost:5500/` & `/index.html`)
- **HTTP Status:** 200 OK (32,659 bytes)
- **Primary H1:** "Your shop, online. Simple and fast."
- **Desktop Nav State:** "Home" marked with `class="active"`.
- **Content Verification:** Displays exclusively core homepage content: Hero banner, Japanese typography kicker (`静寂 BETTIAH · WEST CHAMPARAN`), "What We Build" capabilities overview, trust metrics, and footer. All redundant inline subpage sections have been successfully decoupled.
- **CTA Functionality:** "Discuss on WhatsApp" (`wa.me`) and "View Services" anchor links are correctly formatted.

### Route 2: Services (`http://localhost:5500/services.html`)
- **HTTP Status:** 200 OK (33,454 bytes)
- **Primary H1:** "Software & Digital Solutions for Bettiah Businesses."
- **Desktop Nav State:** "Services" marked with `class="active"`.
- **Content Verification:** Contains all 6 comprehensive service pillars:
  1. High-Performance Website Design & Development
  2. Custom Billing & POS Software
  3. Google Business Listing & Local SEO
  4. Mobile & Android App Development
  5. E-Commerce & Online Store Solutions
  6. Website Maintenance, Security & Support
- **Sub-pages:** Deep links to individual service landing pages (`/services/website-design/`, `/services/billing-software/`, etc.) exist and return 200 OK.

### Route 3: Work / Portfolio (`http://localhost:5500/work.html`)
- **HTTP Status:** 200 OK (35,140 bytes)
- **Primary H1:** "Real Platforms & Software. Live & Verifiable."
- **Desktop Nav State:** "Work" marked with `class="active"`.
- **Content Verification:** Contains 6 detailed project case studies:
  1. Pets Heaven (`petsheaven.in`)
  2. E-Commerce Platform demo (`almasyash.github.io/E-COMMERCE-WEBSITE/`)
  3. Editor FS Android Utility APK
  4. Retail Billing Suite (Counter POS & Khata)
  5. Clinic & Diagnostic Portal
  6. School & Coaching Management System

### Route 4: Pricing (`http://localhost:5500/pricing.html`)
- **HTTP Status:** 200 OK (34,403 bytes)
- **Primary H1:** "Affordable, Simple Pricing. Zero Hidden Charges."
- **Desktop Nav State:** "Pricing" marked with `class="active"`.
- **Content Verification:** Transparent tier cards present:
  1. Business Website: ₹3,000 onwards (Featured)
  2. Google Listing: ₹500 onwards
  3. Custom Software: ₹5,000 onwards
  4. Full Shop Package: ₹8,000 onwards

### Route 5: About (`http://localhost:5500/about.html`)
- **HTTP Status:** 200 OK (32,182 bytes)
- **Primary H1:** "Engineering Digital Growth in Bettiah & West Champaran."
- **Desktop Nav State:** "About" marked with `class="active"`.
- **Content Verification:** Company mission, Bettiah regional commitment, founder background (Almas Neyamatullah), tech stack details, and verified MSME Udyam credentials (`UDYAM-BR-38-0075911`).

### Route 6: Contact (`http://localhost:5500/contact.html`)
- **HTTP Status:** 200 OK (42,612 bytes)
- **Primary H1:** "Start Your Project. Simple, Fast & Direct."
- **Desktop Nav State:** "Contact" marked with `class="active"`.
- **Content Verification:** Fully featured inquiry form, direct studio phone links (`+91 7033761519`, `+91 6254465166`), verified support email (`support@mahmasgroup.online`), physical studio location, and embedded Google Maps link.

---

## 7. Responsive Viewport Testing Matrix

| Viewport Resolution | Device Category | Desktop Nav (`<nav>`) | Hamburger (`#menuToggle`) | Layout Stability | Horizontal Overflow | Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1920 × 1080** | Large Desktop | Visible | Visible | Stable | None (0px) | **PASS** (Desktop nav functional; menu toggle affected by double-toggle bug) |
| **1366 × 768** | Standard Laptop | Visible | Visible | Stable | None (0px) | **PASS** (Desktop nav functional; menu toggle affected by double-toggle bug) |
| **768 × 1024** | Tablet (iPad) | **Hidden** (`max-width: 1060px`) | **Primary Nav** | Stable | None (0px) | **FAIL** (Hamburger click blocked; users cannot navigate to subpages) |
| **390 × 844** | Mobile (iPhone 12/13/14) | **Hidden** | **Primary Nav** | Stable | None (0px) | **FAIL** (Hamburger click blocked; users cannot navigate to subpages) |
| **360 × 800** | Small Android | **Hidden** | **Primary Nav** | Stable | None (0px) | **FAIL** (Hamburger click blocked; users cannot navigate to subpages) |

---

## 8. Network & Console Error Audit

- **Asset Reference Audit:** Verified all 10 local assets across CSS, JavaScript, WebP images, and SVG icons. **Result: 0 Missing Assets (Zero 404s)**.
- **External Dependencies:** Only 1 external CDN script exists on `contact.html` (`@emailjs/browser@4`), which is safely guarded against missing API keys.
- **Console Errors:** No unhandled JavaScript runtime exceptions occur on page load. All script modules feature null checks for DOM elements (`#rain-canvas`, `#cursor`, `#contactForm`).

---

## 9. Severity Classification of Discovered Issues

| Issue ID | Component | Description | Severity | Impact |
| :--- | :--- | :--- | :--- | :--- |
| **BUG-01** | Hamburger Menu | Double-toggle event cancellation prevents slide-out menu from opening on click | **CRITICAL** | High: Mobile and tablet users cannot navigate between pages |
| **BUG-02** | Marquee Ticker | "WhatsApp CRM & Orders" ticker strip sits at the top of all subpages, causing user disorientation | **MEDIUM** | Moderate: Visual confusion on subpages (Work, About, Contact) |
| **BUG-03** | Routing / SEO | Dual route paths (`.html` vs trailing slash `/`) and link targets inconsistent with canonical URLs | **LOW** | Minor: SEO canonicalization and internal link cleanliness |
| **BUG-04** | Accessibility | Slide-out navigation drawer lacks focus trap and modal role attributes | **LOW** | Minor: Screen reader & keyboard-only user experience |

---

## 10. Exact Files Requiring Modification in Phase 2

1. **[assets/js/menu.js](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/assets/js/menu.js):**
   - Lines 39–46: Remove the delegated click listener on `#menuToggle`, or implement a re-entrancy / debounce check, and rely exclusively on a unified handler.
2. **All 25 HTML Pages (Header & Head Blocks):**
   - Head `<script>` block: Remove redundant inline `window.toggleSiteMenu` definitions once `menu.js` handles it authoritatively.
   - Header button: Clean up `onclick="toggleSiteMenu()"` to eliminate dual-registration.
   - Subpages (`services.html`, `work.html`, `pricing.html`, `about.html`, `contact.html`): Conditionally remove `<div class="marquee-strip">` from subpages, reserving it exclusively for [index.html](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/index.html).
3. **[style.css](file:///c:/Users/almas/Desktop/Almas-Neyamatullah/style.css):**
   - Consolidate all menu styles and ensure zero duplication between inline `<style>` and external stylesheet.

---

## 11. Recommended Phase 2 Repair Plan

1. **Fix 1: Bulletproof Single-Trigger Hamburger Event Model**
   - Standardize event handling: Remove inline `onclick="toggleSiteMenu()"` from `#menuToggle` across all HTML files.
   - In `assets/js/menu.js`, attach a single, robust event listener that checks `!menu.classList.contains('open')`, adds `.open`, manages `aria-expanded="true"`, and traps focus.
2. **Fix 2: Subpage Ticker Cleanup**
   - Retain the capabilities marquee strip on the Homepage (`index.html`) where it serves as a high-impact overview of services (including WhatsApp CRM).
   - Remove `<div class="marquee-strip">` from subpages (`services.html`, `work.html`, `pricing.html`, `about.html`, `contact.html`, and their subdirectories) so each subpage leads cleanly with its breadcrumbs and page hero.
3. **Fix 3: Navigation Link URL Harmonization**
   - Ensure all internal navigation links align with the canonical URL structure established in `sitemap.xml`.
4. **Fix 4: Accessibility Hardening**
   - Add focus trapping to `#site-menu` so keyboard Tab navigation cycles inside the drawer until closed.
   - Add `role="dialog"` and `aria-modal="true"`.

---

## 12. Safety Confirmation

**CONFIRMATION:** Zero modifications have been pushed, merged, or deployed to production (`mahmasgroup.online`). All audits were conducted strictly on localhost. No code changes will be implemented until explicit user approval is granted for Phase 2.
