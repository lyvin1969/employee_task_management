document.addEventListener('DOMContentLoaded', function () {
    // Select sidebar elements and toggle buttons
    const sidebar = document.querySelector('.sidebar') || document.querySelector('#sidebar');
    const toggleButtons = document.querySelectorAll('.sidebar-toggle, #sidebarToggle, [data-bs-toggle="sidebar"]');
    
    // Also grab the navbar hamburger button if present
    const navMenuBtn = document.querySelector('nav .btn, .navbar-toggler, .hamburger');

    function toggleSidebar() {
        if (sidebar) {
            sidebar.classList.toggle('show');
            sidebar.classList.toggle('active');
        }
    }

    // Add click listeners to toggle buttons
    toggleButtons.forEach(button => {
        button.addEventListener('click', toggleSidebar);
    });

    if (navMenuBtn && toggleButtons.length === 0) {
        navMenuBtn.addEventListener('click', toggleSidebar);
    }

    // Close sidebar when clicking outside of it on mobile screens
    document.addEventListener('click', function (event) {
        if (window.innerWidth < 992 && sidebar) {
            const isClickInsideSidebar = sidebar.contains(event.target);
            const isClickOnToggle = Array.from(toggleButtons).some(btn => btn.contains(event.target)) || 
                                    (navMenuBtn && navMenuBtn.contains(event.target));

            if (!isClickInsideSidebar && !isClickOnToggle && (sidebar.classList.contains('show') || sidebar.classList.contains('active'))) {
                sidebar.classList.remove('show');
                sidebar.classList.remove('active');
            }
        }
    });
});