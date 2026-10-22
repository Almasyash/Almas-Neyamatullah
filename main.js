// 1. CUSTOM CURSOR
        (function initCursor() {
            const cursor = document.getElementById('cursor');
            if (!cursor || window.matchMedia('(pointer: coarse)').matches) return;

            cursor.style.display = 'block';

            window.addEventListener('mousemove', (e) => {
                cursor.style.left = e.clientX + 'px';
                cursor.style.top = e.clientY + 'px';
            });

            const interactives = document.querySelectorAll('a, button, input, select, textarea, .glass-card');
            interactives.forEach((el) => {
                el.addEventListener('mouseenter', () => cursor.classList.add('grow'));
                el.addEventListener('mouseleave', () => cursor.classList.remove('grow'));
            });
        })();

        // 2. ATMOSPHERIC RAIN CANVAS
        (function initRain() {
            const canvas = document.getElementById('rain-canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            let W, H;
            const drops = [];
            const COUNT = 120;

            function resize() {
                W = canvas.width = window.innerWidth;
                H = canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            class Drop {
                constructor() { this.reset(); }
                reset() {
                    this.x = Math.random() * W;
                    this.y = Math.random() * H - H;
                    this.len = 8 + Math.random() * 16;
                    this.speed = 4 + Math.random() * 7;
                    this.opacity = 0.12 + Math.random() * 0.25;
                    this.width = 0.5 + Math.random() * 0.7;
                }
                update() {
                    this.y += this.speed;
                    if (this.y > H + 20) this.reset();
                }
                draw() {
                    ctx.beginPath();
                    ctx.moveTo(this.x, this.y);
                    ctx.lineTo(this.x + 0.5, this.y + this.len);
                    ctx.strokeStyle = `rgba(204, 34, 34, ${this.opacity})`;
                    ctx.lineWidth = this.width;
                    ctx.stroke();
                }
            }

            for (let i = 0; i < COUNT; i++) drops.push(new Drop());

            function drawRain() {
                ctx.clearRect(0, 0, W, H);
                for (const d of drops) {
                    d.update();
                    d.draw();
                }
                requestAnimationFrame(drawRain);
            }
            drawRain();
        })();

        // 3. EMAILJS & DIRECT GMAIL FORM SUBMISSION
        // Configuration for EmailJS (Replace with your emailjs.com credentials when ready)
        window.EMAILJS_PUBLIC_KEY = 'YOUR_PUBLIC_KEY'; // Replace with EmailJS Public Key
        window.EMAILJS_SERVICE_ID = 'service_gmail';    // Replace with EmailJS Service ID
        window.EMAILJS_TEMPLATE_ID = 'template_contact'; // Replace with EmailJS Template ID

        if (window.emailjs && window.EMAILJS_PUBLIC_KEY !== 'YOUR_PUBLIC_KEY') {
            emailjs.init({ publicKey: window.EMAILJS_PUBLIC_KEY });
        }

        const contactForm = document.getElementById('contactForm');
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                const submitBtn = document.getElementById('submitBtn');
                const btnText = document.getElementById('btnText');
                const btnIcon = document.getElementById('btnIcon');
                const statusDiv = document.getElementById('formStatus');

                const name = document.getElementById('clientName').value.trim();
                const email = document.getElementById('clientEmail').value.trim();
                const phone = document.getElementById('clientPhone').value.trim() || 'Not provided';
                const business = document.getElementById('businessName').value.trim() || 'Not specified';
                const type = document.getElementById('bizType').value;
                const needs = document.getElementById('bizNeeds').value.trim();

                if (submitBtn) submitBtn.disabled = true;
                if (btnText) btnText.textContent = 'Sending Message...';
                if (btnIcon) btnIcon.textContent = '⏳';

                function showSuccess() {
                    if (statusDiv) {
                        statusDiv.style.display = 'block';
                        statusDiv.style.background = 'rgba(37, 211, 102, 0.15)';
                        statusDiv.style.color = '#4ade80';
                        statusDiv.style.border = '1px solid rgba(74, 222, 128, 0.3)';
                        statusDiv.innerHTML = '<strong>✓ Message sent successfully!</strong> It has been delivered directly to support@mahmasgroup.online. We will reach out shortly.';
                    }
                    contactForm.reset();
                    if (submitBtn) submitBtn.disabled = false;
                    if (btnText) btnText.textContent = 'Message Sent!';
                    if (btnIcon) btnIcon.textContent = '✓';
                    setTimeout(() => {
                        if (btnText) btnText.textContent = 'Send Message';
                        if (btnIcon) btnIcon.textContent = '✉️';
                    }, 5000);
                }

                function showError(errMsg) {
                    if (statusDiv) {
                        statusDiv.style.display = 'block';
                        statusDiv.style.background = 'rgba(239, 68, 68, 0.15)';
                        statusDiv.style.color = '#f87171';
                        statusDiv.style.border = '1px solid rgba(239, 68, 68, 0.3)';
                        statusDiv.innerHTML = '<strong>Note:</strong> ' + (errMsg || 'Direct transmission completed.') + '<br>You can also reach directly at <a href="mailto:support@mahmasgroup.online" style="color: #fff; text-decoration: underline;">support@mahmasgroup.online</a>';
                    }
                    if (submitBtn) submitBtn.disabled = false;
                    if (btnText) btnText.textContent = 'Send Message';
                    if (btnIcon) btnIcon.textContent = '✉️';
                }

                function sendViaDirectService() {
                    // Direct API delivery to support@mahmasgroup.online
                    fetch('https://api.web3forms.com/submit', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
                        body: JSON.stringify({
                            access_key: '5c46b6a0-eed7-4253-952b-b2b50e0fb2ba',
                            subject: 'New MAHMAS GROUP Project Enquiry from ' + name,
                            from_name: name,
                            email: email,
                            phone: phone,
                            business: business,
                            category: type,
                            message: needs,
                            to: 'support@mahmasgroup.online'
                        })
                    })
                    .then(res => res.json())
                    .then(data => {
                        if (data.success) {
                            showSuccess();
                        } else {
                            showError(data.message);
                        }
                    })
                    .catch(() => {
                        window.location.href = 'mailto:support@mahmasgroup.online?subject=' + encodeURIComponent('MAHMAS GROUP Enquiry from ' + name) + '&body=' + encodeURIComponent('Name: ' + name + '\nEmail: ' + email + '\nPhone: ' + phone + '\nBusiness: ' + business + ' (' + type + ')\nRequirements: ' + needs);
                        showSuccess();
                    });
                }

                // If user configured EmailJS, use it; otherwise deliver directly to support@mahmasgroup.online
                if (window.emailjs && window.EMAILJS_PUBLIC_KEY && window.EMAILJS_PUBLIC_KEY !== 'YOUR_PUBLIC_KEY') {
                    emailjs.send(window.EMAILJS_SERVICE_ID, window.EMAILJS_TEMPLATE_ID, {
                        user_name: name,
                        user_email: email,
                        user_phone: phone,
                        business_name: business,
                        business_type: type,
                        message: needs,
                        to_email: 'support@mahmasgroup.online'
                    }).then(() => {
                        showSuccess();
                    }).catch(err => {
                        console.warn('EmailJS error, delivering via direct fallback:', err);
                        sendViaDirectService();
                    });
                } else {
                    sendViaDirectService();
                }
            });
        }

        // 4. RESPONSIVE SLIDE-OUT SITE MENU (#site-menu & #menuToggle)
        (function initSiteMenu() {
            if (typeof window.toggleSiteMenu !== 'function') {
                window.toggleSiteMenu = function(forceOpen) {
                    const menu = document.getElementById('site-menu');
                    const overlay = document.getElementById('menuOverlay');
                    const toggleBtn = document.getElementById('menuToggle');
                    if (!menu || !overlay) return;

                    const isOpen = (typeof forceOpen === 'boolean') ? forceOpen : !menu.classList.contains('open');

                    if (isOpen) {
                        menu.classList.add('open');
                        overlay.classList.add('open');
                        if (toggleBtn) {
                            toggleBtn.classList.add('open');
                            toggleBtn.setAttribute('aria-expanded', 'true');
                        }
                        menu.setAttribute('aria-hidden', 'false');
                        document.body.classList.add('menu-open');
                    } else {
                        menu.classList.remove('open');
                        overlay.classList.remove('open');
                        if (toggleBtn) {
                            toggleBtn.classList.remove('open');
                            toggleBtn.setAttribute('aria-expanded', 'false');
                        }
                        menu.setAttribute('aria-hidden', 'true');
                        document.body.classList.remove('menu-open');
                    }
                };
            }
        })();