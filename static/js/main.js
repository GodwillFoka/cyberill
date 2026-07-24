/* ============================================
   CYBERILL v2 — Animations & Interactions
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

    // ===== 1. Hero Slider =====
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dot');
    if (slides.length > 0) {
        let currentSlide = 0;
        const slideInterval = 5000;

        function showSlide(index) {
            slides.forEach(s => s.classList.remove('active'));
            dots.forEach(d => d.classList.remove('active'));
            slides[index].classList.add('active');
            dots[index].classList.add('active');
            currentSlide = index;
        }

        function nextSlide() {
            showSlide((currentSlide + 1) % slides.length);
        }

        dots.forEach((dot, i) => {
            dot.addEventListener('click', () => showSlide(i));
        });

        if (slides.length > 1) {
            setInterval(nextSlide, slideInterval);
        }
    }

    // ===== 2. Scroll Reveal (Fade-in) =====
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right, .stagger-children').forEach(el => {
        observer.observe(el);
    });

    // ===== 3. Count Up Animation =====
    const countObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseInt(el.dataset.target) || 0;
                const suffix = el.dataset.suffix || '';
                const duration = 2000;
                const start = performance.now();

                function updateCount(currentTime) {
                    const elapsed = currentTime - start;
                    const progress = Math.min(elapsed / duration, 1);
                    // Ease out cubic
                    const eased = 1 - Math.pow(1 - progress, 3);
                    const current = Math.floor(eased * target);
                    el.textContent = current + suffix;
                    if (progress < 1) {
                        requestAnimationFrame(updateCount);
                    } else {
                        el.textContent = target + suffix;
                    }
                }
                requestAnimationFrame(updateCount);
                countObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('.count-up').forEach(el => {
        countObserver.observe(el);
    });

    // ===== 4. Carousel Navigation =====
    document.querySelectorAll('.carousel-section').forEach(section => {
        const track = section.querySelector('.carousel-track');
        const prevBtn = section.querySelector('.carousel-btn.prev');
        const nextBtn = section.querySelector('.carousel-btn.next');
        if (!track || !prevBtn || !nextBtn) return;

        let position = 0;
        const card = track.querySelector('.carousel-card');
        if (!card) return;
        const cardWidth = card.offsetWidth + 30; // width + gap
        const maxPosition = track.scrollWidth - track.parentElement.offsetWidth;

        function updateCarousel() {
            track.style.transform = `translateX(-${position}px)`;
            prevBtn.style.opacity = position <= 0 ? '0.3' : '1';
            nextBtn.style.opacity = position >= maxPosition ? '0.3' : '1';
        }

        prevBtn.addEventListener('click', () => {
            position = Math.max(0, position - cardWidth);
            updateCarousel();
        });

        nextBtn.addEventListener('click', () => {
            position = Math.min(maxPosition, position + cardWidth);
            updateCarousel();
        });

        updateCarousel();

        // Touch support
        let startX, isDragging = false;
        track.addEventListener('mousedown', (e) => {
            startX = e.pageX;
            isDragging = true;
        });
        track.addEventListener('mouseup', (e) => {
            if (!isDragging) return;
            const diff = startX - e.pageX;
            if (diff > 50) nextBtn.click();
            else if (diff < -50) prevBtn.click();
            isDragging = false;
        });
        track.addEventListener('mouseleave', () => { isDragging = false; });
    });

    // ===== 5. Floating Particles (Hero) =====
    const particlesContainer = document.querySelector('.particles-container');
    if (particlesContainer) {
        const colors = ['#E6681B', '#20155C', '#FF8A3C'];
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            const size = 2 + Math.random() * 4;
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.background = colors[Math.floor(Math.random() * colors.length)];
            particle.style.animationDuration = (4 + Math.random() * 4) + 's';
            particle.style.animationDelay = (Math.random() * 4) + 's';
            particlesContainer.appendChild(particle);
        }
    }

    // ===== 6. Skill Bars Animation =====
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const fill = entry.target;
                const width = fill.dataset.width || '0';
                setTimeout(() => {
                    fill.style.width = width + '%';
                }, 200);
                skillObserver.unobserve(fill);
            }
        });
    }, { threshold: 0.3 });

    document.querySelectorAll('.skill-bar-fill').forEach(el => {
        skillObserver.observe(el);
    });

    // ===== 7. Active Nav Link =====
    const currentPath = window.location.pathname;
    document.querySelectorAll('.navbar .nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (href && href !== '#' && currentPath.startsWith(href) && href !== '/') {
            link.classList.add('active');
        } else if (href === '/' && currentPath === '/') {
            link.classList.add('active');
        }
    });

    // ===== 8. Smooth scroll for anchor links =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ===== 9. Dark/Light Mode Toggle =====
    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        // Load saved theme
        const savedTheme = localStorage.getItem('cyberill-theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeToggle.textContent = savedTheme === 'dark' ? '☀️' : '🌙';

        themeToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('cyberill-theme', next);
            themeToggle.textContent = next === 'dark' ? '☀️' : '🌙';
        });
    }

});

// ===== 10. Back to Top Button =====
const backToTop = document.getElementById('backToTop');
if (backToTop) {
    window.addEventListener('scroll', () => {
        backToTop.classList.toggle('show', window.scrollY > 400);
    });
    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// ===== 11. Cookie Consent Banner =====
function acceptCookies() {
    localStorage.setItem('cyberill-cookies', 'accepted');
    document.getElementById('cookieBanner').classList.remove('show');
}
if (document.getElementById('cookieBanner')) {
    if (!localStorage.getItem('cyberill-cookies')) {
        setTimeout(() => {
            document.getElementById('cookieBanner').classList.add('show');
        }, 1000);
    }
}

// ===== 12. Scroll Reveal Animations =====
const revealElements = document.querySelectorAll('.fade-in, .slide-up, .slide-left, .slide-right, .scale-in');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.15 });
revealElements.forEach(el => observer.observe(el));

// ===== 13. Stagger Children Animation =====
const staggerContainers = document.querySelectorAll('.stagger-children');
const staggerObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animated');
            staggerObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.15 });
staggerContainers.forEach(el => staggerObserver.observe(el));

// ===== 14. Skill Bars Animation =====
const skillBars = document.querySelectorAll('.skill-bar-fill');
const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animated');
            skillObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.3 });
skillBars.forEach(el => skillObserver.observe(el));

// ===== 15. Ripple Effect on Buttons =====
document.querySelectorAll('.ripple-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
        const rect = this.getBoundingClientRect();
        const ripple = document.createElement('span');
        ripple.className = 'ripple';
        ripple.style.left = (e.clientX - rect.left - 10) + 'px';
        ripple.style.top = (e.clientY - rect.top - 10) + 'px';
        ripple.style.width = ripple.style.height = '20px';
        this.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
    });
});

// ===== 16. Smooth Reveal on Load =====
document.querySelectorAll('.hero-badge, .hero-slide, .btn-accent').forEach((el, i) => {
    if (el.closest('.hero') || el.closest('.contact-section')) {
        el.style.opacity = '0';
        setTimeout(() => {
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            el.style.opacity = '1';
        }, 200 + i * 150);
    }
});

// ===== 17. Floating Animation on Hero Image =====
const heroImage = document.querySelector('.hero-image');
if (heroImage) heroImage.classList.add('float-anim');

// ===== 18. Animated Counters (re-initialize for dynamically loaded) =====
document.querySelectorAll('.count-up').forEach(counter => {
    const target = parseInt(counter.dataset.target) || 0;
    const suffix = counter.dataset.suffix || '';
    const updateCount = () => {
        const current = parseInt(counter.innerText) || 0;
        const increment = Math.ceil(target / 30);
        if (current < target) {
            counter.innerText = Math.min(current + increment, target) + suffix;
            requestAnimationFrame(updateCount);
        } else {
            counter.innerText = target + suffix;
        }
    };
    const counterObserver = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            counter.innerText = '0';
            updateCount();
            counterObserver.unobserve(counter);
        }
    }, { threshold: 0.5 });
    counterObserver.observe(counter);
});

// ===== 19. Lightbox =====
function openLightbox(imgSrc, caption) {
    const lb = document.getElementById('lightbox');
    const lbImg = document.getElementById('lightbox-img');
    const lbCap = document.getElementById('lightbox-caption');
    lbImg.src = imgSrc;
    lbCap.textContent = caption || '';
    lb.classList.add('active');
    document.body.style.overflow = 'hidden';
}
function closeLightbox(e) {
    if (e.target !== e.currentTarget && e.target.tagName !== 'BUTTON') return;
    document.getElementById('lightbox').classList.remove('active');
    document.body.style.overflow = '';
}
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        document.getElementById('lightbox').classList.remove('active');
        document.body.style.overflow = '';
    }
});
// Auto-bind all [data-lightbox] elements
document.querySelectorAll('[data-lightbox]').forEach(el => {
    el.style.cursor = 'pointer';
    el.addEventListener('click', () => {
        openLightbox(el.src || el.href, el.dataset.caption || '');
    });
});
