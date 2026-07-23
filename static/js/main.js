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

});
