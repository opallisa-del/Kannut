/* ================================================
   PATRIMONIO 360 — Marketing Site Scripts
   Scroll reveal, counters, nav blur, parallax
   ================================================ */

'use strict';

// ── Nav scroll effect ──────────────────────────
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 24) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}, { passive: true });

// ── Mobile Menu Toggle ──────────────────────────
const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
const navLinks = document.querySelector('.nav-links');

// Keep --nav-height CSS var in sync so the mobile menu always
// opens right below the navbar, even after scroll or resize.
function updateNavHeight() {
    const h = navbar ? navbar.getBoundingClientRect().height : 64;
    document.documentElement.style.setProperty('--nav-height', h + 'px');
}
updateNavHeight();
window.addEventListener('resize', updateNavHeight, { passive: true });

if (mobileNavToggle) {
    mobileNavToggle.addEventListener('click', () => {
        updateNavHeight(); // recalculate at moment of opening
        document.body.classList.toggle('nav-open');
        const isOpen = document.body.classList.contains('nav-open');
        mobileNavToggle.setAttribute('aria-expanded', isOpen);
    });
}

// Close menu when clicking a link
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
    });
});


// ── Smooth scroll for anchor links ────────────
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            const navH = navbar.getBoundingClientRect().height;
            const top = target.getBoundingClientRect().top + window.scrollY - navH - 16;
            window.scrollTo({ top, behavior: 'smooth' });
        }
    });
});


// ── Intersection Observer — Scroll Reveal ─────
const revealObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                revealObserver.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));


// ── Animated Number Counters ──────────────────
function animateCounter(el, from, to, duration, suffix) {
    const startTime = performance.now();
    const isFloat = !Number.isInteger(to);

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Ease out cubic
        const ease = 1 - Math.pow(1 - progress, 3);
        const current = from + (to - from) * ease;
        el.textContent = (isFloat ? current.toFixed(1) : Math.round(current)) + suffix;

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    requestAnimationFrame(update);
}

// Observe stat numbers
const counterObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseFloat(el.dataset.target);
                const suffix = el.dataset.suffix || '';
                if (!isNaN(target)) {
                    animateCounter(el, 0, target, 1800, suffix);
                }
                counterObserver.unobserve(el);
            }
        });
    },
    { threshold: 0.5 }
);

document.querySelectorAll('[data-target]').forEach(el => counterObserver.observe(el));


// ── Parallax on Hero Glows ─────────────────────
const heroGlows = document.querySelectorAll('#hero .bg-glow');

function updateParallax() {
    const scrollY = window.scrollY;
    heroGlows.forEach((glow, i) => {
        const speed = i % 2 === 0 ? 0.25 : -0.15;
        glow.style.transform = `translateY(${scrollY * speed}px)`;
    });
}

window.addEventListener('scroll', updateParallax, { passive: true });


// ── Feature card subtle tilt on mouse move ─────
document.querySelectorAll('.glass-card.feature-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        const dx = (e.clientX - cx) / (rect.width / 2);
        const dy = (e.clientY - cy) / (rect.height / 2);
        const rotX = dy * -4;
        const rotY = dx * 4;
        card.style.transform = `perspective(800px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateY(-3px)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
        card.style.transition = 'transform 0.5s cubic-bezier(0.4,0,0.2,1)';
        setTimeout(() => { card.style.transition = ''; }, 500);
    });
});


// ── Mockup 3D tilt on scroll ───────────────────
const mockupFrame = document.querySelector('.mockup-frame');
if (mockupFrame) {
    window.addEventListener('scroll', () => {
        const rect = mockupFrame.closest('.dashboard-mockup').getBoundingClientRect();
        const centerY = rect.top + rect.height / 2;
        const viewportCenter = window.innerHeight / 2;
        const offset = (centerY - viewportCenter) / viewportCenter;
        const clampedOffset = Math.max(-1, Math.min(1, offset));
        const angle = clampedOffset * 6 + 4; // between -2 and 10 deg
        mockupFrame.style.transform = `rotateX(${angle}deg)`;
    }, { passive: true });
}


// ── Typing animation on AI chat ────────────────
const aiInputText = document.querySelector('.ai-input-text');
if (aiInputText) {
    const phrases = [
        '¿Cómo mejoro mi yield actual?',
        '¿Cuándo llegaré a la independencia financiera?',
        '¿Qué acciones tienen mejor dividendo?',
        'Analiza mi exposición a riesgo...',
        '¿Debería rebalancear mi cartera?',
    ];
    let phraseIdx = 0;
    let charIdx = 0;
    let isDeleting = false;
    let pause = false;

    function typeEffect() {
        const current = phrases[phraseIdx];
        if (pause) { pause = false; setTimeout(typeEffect, 1200); return; }

        if (!isDeleting) {
            aiInputText.textContent = current.slice(0, charIdx + 1);
            charIdx++;
            if (charIdx === current.length) { isDeleting = true; pause = true; }
        } else {
            aiInputText.textContent = current.slice(0, charIdx - 1);
            charIdx--;
            if (charIdx === 0) {
                isDeleting = false;
                phraseIdx = (phraseIdx + 1) % phrases.length;
                pause = true;
            }
        }

        const delay = isDeleting ? 40 : (pause ? 0 : 70);
        setTimeout(typeEffect, delay);
    }

    // Start after a short delay for page load
    setTimeout(typeEffect, 2000);
}


// ── Dashboard mockup fake ticker ──────────────
const movers = document.querySelectorAll('.m-mover-pct');
if (movers.length) {
    const values = [
        { up: ['+2.4%', '+1.8%', '+1.2%'], down: ['-0.6%'] },
        { up: ['+3.1%', '+0.9%', '+2.2%'], down: ['-1.2%'] },
        { up: ['+1.7%', '+2.6%', '+0.4%'], down: ['-0.3%'] },
    ];
    let tick = 0;

    setInterval(() => {
        tick = (tick + 1) % values.length;
        const set = values[tick];
        const allMovers = document.querySelectorAll('.m-mover-pct');
        allMovers.forEach((el, i) => {
            if (el.classList.contains('up')) {
                el.textContent = set.up[i] || set.up[0];
            } else {
                el.textContent = set.down[0];
            }
        });
        // Animate
        allMovers.forEach(el => {
            el.style.transition = 'opacity 0.3s';
            el.style.opacity = '0';
            setTimeout(() => { el.style.opacity = '1'; }, 300);
        });
    }, 4000);
}


// ── Retirement ring animate on reveal ─────────
const retFill = document.querySelector('.ret-goal-fill');
if (retFill) {
    const ringObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    retFill.style.transition = 'width 1.5s cubic-bezier(0.4,0,0.2,1) 0.3s';
                    retFill.style.width = '68%';
                    ringObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.5 }
    );
    retFill.style.width = '0%';
    ringObserver.observe(retFill);
}


// ── Simulator bars animate on reveal ─────────
const simBars = document.querySelectorAll('.sim-bar-fill');
if (simBars.length) {
    const targets = ['31%', '42%', '55%', '72%', '100%'];
    const barObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    simBars.forEach((bar, i) => {
                        bar.style.width = '0%';
                        bar.style.transition = `width 1.2s cubic-bezier(0.4,0,0.2,1) ${0.1 + i * 0.12}s`;
                        setTimeout(() => { bar.style.width = targets[i]; }, 50);
                    });
                    barObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.4 }
    );
    if (simBars[0]) barObserver.observe(simBars[0].closest('.sim-panel') || simBars[0]);
}
