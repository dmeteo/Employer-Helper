let asideNavBar = document.querySelector('.aside-navbar');
let homeLink = document.querySelector('.home-link');
let navLinks = document.querySelectorAll('.nav-link');

asideNavBar.addEventListener('mouseover', function() {
    homeLink.querySelector('h2').hidden = false;
    navLinks.forEach(function(navLink) {
        navLink.querySelector('p').hidden = false;
    })
});

asideNavBar.addEventListener('mouseout', function() {
    homeLink.querySelector('h2').hidden = true;
    navLinks.forEach(function(navLink) {
        navLink.querySelector('p').hidden = true;
    })
});
