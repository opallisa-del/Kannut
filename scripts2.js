/* =========================================
   PATRIMONIO 360 — scripts2.js
   Apple-style scroll storytelling engine
   =========================================*/

'use strict';

// ── Nav: dark / light mode on scroll ──────────
const nav = document.getElementById('nav');

function updateNav() {
    const hero = document.getElementById('hero');
    const heroBottom = hero ? hero.getBoundingClientRect().bottom : 0;
    if (heroBottom <= 52) {
        nav.classList.add('dark-mode');
    } else {
        nav.classList.remove('dark-mode');
    }
}
window.addEventListener('scroll', updateNav, { passive: true });
updateNav();


// ── Smooth-scroll anchors ──────────────────────
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            e.preventDefault();
            const top = target.getBoundingClientRect().top + window.scrollY - 52;
            window.scrollTo({ top, behavior: 'smooth' });
        }
    });
});


// ── Scroll Reveal ─────────────────────────────
const revealObserver = new IntersectionObserver(
    entries => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add('visible');
                revealObserver.unobserve(e.target);
            }
        });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);
document.querySelectorAll('.reveal, .reveal-scale').forEach(el => revealObserver.observe(el));


// ══════════════════════════════════════
//  STICKY STEP SCROLL ACTIVATION
//  Scroll-position based (works with sticky).
//  Also activates on hover.
// ══════════════════════════════════════
function initStickyScrollers() {
    const stepGroups = document.querySelectorAll('[data-sticky-steps]');

    stepGroups.forEach(group => {
        const items = Array.from(group.querySelectorAll('.step-item'));
        if (!items.length) return;

        // Always start with first step active
        items.forEach((item, i) => {
            if (i === 0) item.classList.add('active');
            else item.classList.remove('active');
        });

        // ── Hover to activate ───────────────────────
        items.forEach(item => {
            item.addEventListener('mouseenter', () => {
                items.forEach(i => i.classList.remove('active'));
                item.classList.add('active');
            });
            // On mouse leave the whole group, restore scroll-driven state
            item.addEventListener('mouseleave', (e) => {
                // Only revert if leaving to outside the group
                if (!group.contains(e.relatedTarget)) {
                    syncActiveStep(group, items);
                }
            });
        });

        // ── Scroll-driven activation ────────────────
        // We compute which step's "trigger zone" the viewport center falls in.
        function syncActiveStep(grp, its) {
            const viewCY = window.scrollY + window.innerHeight * 0.5;
            let best = 0;
            let bestDist = Infinity;
            its.forEach((item, idx) => {
                const r = item.getBoundingClientRect();
                const itemCY = window.scrollY + r.top + r.height / 2;
                const dist = Math.abs(viewCY - itemCY);
                if (dist < bestDist) { bestDist = dist; best = idx; }
            });
            its.forEach((item, idx) => {
                if (idx === best) item.classList.add('active');
                else item.classList.remove('active');
            });
        }

        window.addEventListener('scroll', () => {
            // Only run if group is in viewport proximity
            const gr = group.getBoundingClientRect();
            if (gr.top < window.innerHeight * 1.5 && gr.bottom > -window.innerHeight * 0.5) {
                syncActiveStep(group, items);
            }
        }, { passive: true });
    });
}
initStickyScrollers();


// ══════════════════════════════════════
//  SIMULATOR BARS — animate on scroll
// ══════════════════════════════════════
function initSimBars() {
    const simFills = document.querySelectorAll('.sim-fill[data-w]');
    if (!simFills.length) return;

    const obs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                simFills.forEach((bar, i) => {
                    const target = bar.dataset.w;
                    bar.style.width = '0%';
                    bar.style.transition = `width 1.3s cubic-bezier(0.4,0,0.2,1) ${0.05 + i * 0.14}s`;
                    requestAnimationFrame(() => {
                        requestAnimationFrame(() => { bar.style.width = target; });
                    });
                });
                obs.disconnect();
            }
        });
    }, { threshold: 0.4 });

    const container = simFills[0].closest('.sim-ui') || simFills[0];
    obs.observe(container);
}
initSimBars();


// ══════════════════════════════════════
//  FEATURE CARD TILT (mosaic cards)
// ══════════════════════════════════════
document.querySelectorAll('.mosaic-card').forEach(card => {
    card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        const cx = r.left + r.width / 2;
        const cy = r.top + r.height / 2;
        const rx = ((e.clientY - cy) / (r.height / 2)) * -3.5;
        const ry = ((e.clientX - cx) / (r.width / 2)) * 3.5;
        card.style.transform = `perspective(700px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-4px)`;
    });
    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
    });
});


// ══════════════════════════════════════
//  AI TYPING EFFECT
// ══════════════════════════════════════
const aiPlaceholder = document.getElementById('ai-placeholder');
if (aiPlaceholder) {
    const phrases = [
        '¿Cuándo me puedo jubilar?',
        '¿Cómo mejoro mi yield?',
        '¿Debería rebalancear ya?',
        '¿Qué ETF compro este mes?',
        '¿Cómo afecta mi LTIP a la proyección?',
    ];
    let pi = 0, ci = 0, del = false, pause = false;

    function tick() {
        if (pause) { pause = false; setTimeout(tick, 1200); return; }
        const phrase = phrases[pi];
        if (!del) {
            aiPlaceholder.textContent = phrase.slice(0, ci + 1) + '|';
            ci++;
            if (ci === phrase.length) { del = true; pause = true; }
        } else {
            aiPlaceholder.textContent = phrase.slice(0, ci - 1) + (ci > 0 ? '|' : '');
            ci--;
            if (ci === 0) { del = false; pi = (pi + 1) % phrases.length; pause = true; }
        }
        setTimeout(tick, del ? 45 : 75);
    }
    setTimeout(tick, 3000);
}


// ══════════════════════════════════════
//  HERO PARALLAX
// ══════════════════════════════════════
const heroGlows = document.querySelectorAll('#hero .hero-glow');
function onScroll() {
    const sy = window.scrollY;
    heroGlows.forEach((g, i) => {
        const dir = i % 2 === 0 ? 0.2 : -0.1;
        g.style.transform = `translateY(${sy * dir}px) ${i === 1 ? '' : 'translateX(-50%)'}`;
    });
}
window.addEventListener('scroll', onScroll, { passive: true });


// ══════════════════════════════════════
//  NUMBER COUNTERS (stats if added later)
// ══════════════════════════════════════
function animateCount(el, end, dur, suffix) {
    const start = performance.now();
    const isFloat = !Number.isInteger(end);
    const step = t => {
        const p = Math.min((t - start) / dur, 1);
        const e = 1 - Math.pow(1 - p, 3);
        el.textContent = (isFloat ? (end * e).toFixed(1) : Math.round(end * e)) + suffix;
        if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
}

const counterObs = new IntersectionObserver(entries => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            const el = e.target;
            const v = parseFloat(el.dataset.count);
            const s = el.dataset.suffix || '';
            if (!isNaN(v)) animateCount(el, v, 1600, s);
            counterObs.unobserve(el);
        }
    });
}, { threshold: 0.6 });
document.querySelectorAll('[data-count]').forEach(el => counterObs.observe(el));


// ══════════════════════════════════════
//  DASHBOARD TICKER
// ══════════════════════════════════════
const tickerDataSets = [
    ['+2.4%', '+1.8%', '+1.2%', '-0.6%'],
    ['+3.1%', '+0.7%', '+1.6%', '-1.2%'],
    ['+1.3%', '+2.2%', '+0.9%', '-0.3%'],
];
let tickIdx = 0;

function rotateTicker() {
    tickIdx = (tickIdx + 1) % tickerDataSets.length;
    const set = tickerDataSets[tickIdx];
    const rows = document.querySelectorAll('.dm-pct');
    rows.forEach((el, i) => {
        const val = set[i] || set[0];
        el.style.opacity = '0';
        setTimeout(() => {
            el.textContent = val;
            el.className = 'dm-pct ' + (val.startsWith('+') ? 'up' : 'dn');
            el.style.opacity = '1';
            el.style.transition = 'opacity 0.4s';
        }, 300);
    });
}
setInterval(rotateTicker, 4500);
