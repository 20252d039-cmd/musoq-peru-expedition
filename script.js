// Navbar Scroll Effect
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile Menu Toggle
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');
const mobileLinks = document.querySelectorAll('.mobile-link');

hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('active');
});

mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('active');
    });
});

// Scroll Reveal Animations (Intersection Observer)
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-up').forEach(element => {
    observer.observe(element);
});

// Hero Background Slideshow Transition Loop (Intelligent Duration & Video Control)
const heroSlides = document.querySelectorAll('.hero-slide');
if (heroSlides.length > 0) {
    let currentSlide = 0;
    let slideTimeout;

    function transitionSlide() {
        // Remove active class from current slide
        heroSlides[currentSlide].classList.remove('active');
        
        // Go to next slide
        currentSlide = (currentSlide + 1) % heroSlides.length;
        
        const nextSlideEl = heroSlides[currentSlide];
        nextSlideEl.classList.add('active');

        // Check if slide contains a video
        const video = nextSlideEl.querySelector('video');
        let duration = 5000; // Default image slide duration: 5 seconds
        
        if (video) {
            video.currentTime = 0;
            video.play().catch(err => console.log("Video play failed:", err));
            duration = 15000; // Video slide duration: 15 seconds (to appreciate it!)
        }

        // Schedule next transition
        slideTimeout = setTimeout(transitionSlide, duration);
    }

    // Initialize first slide video playback if applicable
    const firstSlide = heroSlides[0];
    const firstVideo = firstSlide.querySelector('video');
    let initialDuration = 5000;
    
    if (firstVideo) {
        firstVideo.play().catch(err => console.log("First video play failed:", err));
        initialDuration = 15000; // Start with 15s for the video
    }
    
    slideTimeout = setTimeout(transitionSlide, initialDuration);
}

// Cultural Music Toggle Player
function toggleMusic() {
    const culturalAudio = document.getElementById('culturalAudio');
    const musicControl = document.getElementById('musicControl');
    if (!culturalAudio || !musicControl) return;

    const statusText = musicControl.querySelector('.music-status');
    const icon = musicControl.querySelector('.music-icon');

    if (culturalAudio.paused) {
        culturalAudio.play().then(() => {
            musicControl.classList.add('playing');
            statusText.textContent = "MÚSICA: ACTIVADA";
            icon.textContent = "🔊";
        }).catch(err => {
            console.error("Audio playback error:", err);
        });
    } else {
        culturalAudio.pause();
        musicControl.classList.remove('playing');
        statusText.textContent = "MÚSICA: DESACTIVADA";
        icon.textContent = "🔇";
    }
}

// Autoplay sound and video on first user interaction anywhere
document.addEventListener('click', startAutoplayAudioAndVideo, { once: true });
document.addEventListener('touchstart', startAutoplayAudioAndVideo, { once: true });
document.addEventListener('scroll', startAutoplayAudioAndVideo, { once: true });

function startAutoplayAudioAndVideo() {
    const culturalAudio = document.getElementById('culturalAudio');
    const musicControl = document.getElementById('musicControl');
    
    // Play video if it was blocked or paused
    const activeVideo = document.querySelector('.hero-slide.active video');
    if (activeVideo && activeVideo.paused) {
        activeVideo.play().catch(err => console.log("Video interaction play failed:", err));
    }

    if (culturalAudio && culturalAudio.paused) {
        culturalAudio.play().then(() => {
            if (musicControl) {
                const statusText = musicControl.querySelector('.music-status');
                const icon = musicControl.querySelector('.music-icon');
                musicControl.classList.add('playing');
                statusText.textContent = "MÚSICA: ACTIVADA";
                icon.textContent = "🔊";
            }
        }).catch(err => {
            console.log("Audio autoplay blocked by browser policy:", err);
        });
    }
}

