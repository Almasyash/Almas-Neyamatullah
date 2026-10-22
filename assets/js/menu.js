/**
 * MAHMAS GROUP - High-Performance Responsive Navigation Drawer
 * Production-Quality, Zero-Dependency, Fully Accessible (a11y), Cache-Proof
 */
(function() {
    'use strict';

    // State tracking & debouncing
    var lastToggleTime = 0;
    var previousActiveElement = null;

    /**
     * Authoritative toggle function
     * @param {boolean} [forceOpen] - Explicitly set open (true) or closed (false)
     */
    window.toggleSiteMenu = function(forceOpen) {
        var now = Date.now();
        // Debounce rapid repeated triggers (e.g., synchronous double-dispatch within 150ms)
        if (now - lastToggleTime < 150) {
            return;
        }
        lastToggleTime = now;

        var menu = document.getElementById('site-menu');
        var overlay = document.getElementById('menuOverlay');
        var toggleBtn = document.getElementById('menuToggle');
        if (!menu || !overlay) return;

        var currentlyOpen = menu.classList.contains('open');
        var shouldOpen = (typeof forceOpen === 'boolean') ? forceOpen : !currentlyOpen;

        // If state is already matching, no-op
        if (currentlyOpen === shouldOpen) return;

        if (shouldOpen) {
            // Save currently focused element to return focus on close
            previousActiveElement = document.activeElement;

            menu.classList.add('open');
            overlay.classList.add('open');
            menu.setAttribute('aria-hidden', 'false');

            if (toggleBtn) {
                toggleBtn.classList.add('open');
                toggleBtn.setAttribute('aria-expanded', 'true');
            }
            document.body.classList.add('menu-open');

            // Move focus to close button or first link inside drawer
            requestAnimationFrame(function() {
                var closeBtn = document.getElementById('menuClose') || document.getElementById('menuCloseBtn');
                if (closeBtn) {
                    closeBtn.focus();
                } else {
                    var firstLink = menu.querySelector('a, button');
                    if (firstLink) firstLink.focus();
                }
            });
        } else {
            menu.classList.remove('open');
            overlay.classList.remove('open');
            menu.setAttribute('aria-hidden', 'true');

            if (toggleBtn) {
                toggleBtn.classList.remove('open');
                toggleBtn.setAttribute('aria-expanded', 'false');
            }
            document.body.classList.remove('menu-open');

            // Return focus to trigger button
            if (previousActiveElement && typeof previousActiveElement.focus === 'function') {
                try {
                    previousActiveElement.focus();
                } catch (e) {}
            } else if (toggleBtn) {
                try {
                    toggleBtn.focus();
                } catch (e) {}
            }
        }
    };

    // Attach document-level listeners only once
    if (window.__MAHMAS_DRAWER_BOUND__) return;
    window.__MAHMAS_DRAWER_BOUND__ = true;

    // Single delegated click handler
    document.addEventListener('click', function(e) {
        // Toggle button click
        var toggle = e.target.closest('#menuToggle, .menu-toggle');
        if (toggle) {
            e.preventDefault();
            e.stopPropagation();
            window.toggleSiteMenu();
            return;
        }

        // Close button click
        var closeBtn = e.target.closest('#menuClose, .menu-close-btn');
        if (closeBtn) {
            e.preventDefault();
            e.stopPropagation();
            window.toggleSiteMenu(false);
            return;
        }

        // Backdrop overlay click
        var overlay = e.target.closest('#menuOverlay, .menu-overlay');
        if (overlay) {
            e.preventDefault();
            e.stopPropagation();
            window.toggleSiteMenu(false);
            return;
        }

        // Navigation link click inside drawer
        var drawerLink = e.target.closest('#site-menu a');
        if (drawerLink) {
            // Close drawer cleanly on navigation
            window.toggleSiteMenu(false);
        }
    }, true); // Use capture phase so delegation handles it reliably

    // Keyboard accessibility: Escape to close and Tab focus trapping
    document.addEventListener('keydown', function(e) {
        var menu = document.getElementById('site-menu');
        if (!menu || !menu.classList.contains('open')) return;

        // Escape key closes menu
        if (e.key === 'Escape' || e.keyCode === 27) {
            e.preventDefault();
            window.toggleSiteMenu(false);
            return;
        }

        // Focus trap for Tab key
        if (e.key === 'Tab' || e.keyCode === 9) {
            var focusables = menu.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])');
            if (!focusables || focusables.length === 0) return;

            var firstFocusable = focusables[0];
            var lastFocusable = focusables[focusables.length - 1];

            if (e.shiftKey) {
                // Shift + Tab
                if (document.activeElement === firstFocusable) {
                    e.preventDefault();
                    lastFocusable.focus();
                }
            } else {
                // Tab
                if (document.activeElement === lastFocusable) {
                    e.preventDefault();
                    firstFocusable.focus();
                }
            }
        }
    });

})();
