// Get the navbar
const navbar = document.querySelector('nav');

// Get the offset position of the navbar
const sticky = navbar.offsetTop;

// Function to add 'sticky' class on scroll
function stickyNavbar() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add('sticky');
    } else {
        navbar.classList.remove('sticky');
    }
}

// Listen for the scroll event and call the 'stickyNavbar' function
window.onscroll = function() {
    stickyNavbar();
};