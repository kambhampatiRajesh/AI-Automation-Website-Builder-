document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('.nav-link').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Optional: Form submission handling (for now, just logs to console)
    const contactForm = document.getElementById('contact-form');
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        console.log('Form Submitted:');
        console.log('Name:', name);
        console.log('Email:', email);
        console.log('Message:', message);

        // In a real application, you would send this data to a server
        alert('Message sent! Thank you.');
        contactForm.reset(); // Reset the form
    });
});