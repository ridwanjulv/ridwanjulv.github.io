// Mark active nav link based on current page
document.addEventListener('DOMContentLoaded', function () {
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(function (link) {
    if (link.href === window.location.href) {
      link.classList.add('active');
    }
  });
});
