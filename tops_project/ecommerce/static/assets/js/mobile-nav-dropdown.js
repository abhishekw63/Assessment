/**
* Template Name: Append
* Template URL: https://bootstrapmade.com/append-bootstrap-website-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
/**
 * Toggle mobile nav dropdowns
 */
document.querySelectorAll('.navmenu .has-dropdown i').forEach(navmenu => {
  navmenu.addEventListener('click', function(e) {
    if (document.querySelector('.mobile-nav-active')) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    }
  });
});