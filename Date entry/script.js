document.getElementById('login-btn').addEventListener('click', function() {
    document.getElementById('login-menu').style.opacity = 10;
    document.getElementById('login-menu').style.pointerEvents = 'all';
});

document.getElementsByClassName('login-close')[0].addEventListener('click', function() {
    document.getElementById('login-menu').style.opacity = 1;
    document.getElementById('login-menu').style.pointerEvents = 'none';
});