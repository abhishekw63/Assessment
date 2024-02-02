/**
* Template Name: Append
* Template URL: https://bootstrapmade.com/append-bootstrap-website-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
/**
 * Scroll up sticky header to headers with .scroll-up-sticky class
 */
let lastScrollTop = 0;
const selectHeader = document.querySelector('#header');
window.addEventListener('scroll', function() {
  if (!selectHeader.classList.contains('scroll-up-sticky')) return;

  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > lastScrollTop && scrollTop > selectHeader.offsetHeight) {
    selectHeader.style.setProperty('position', 'sticky', 'important');
    selectHeader.style.top = `-${header.offsetHeight + 50}px`;
  } else if (scrollTop > selectHeader.offsetHeight) {
    selectHeader.style.setProperty('position', 'sticky', 'important');
    selectHeader.style.top = "0";
  } else {
    selectHeader.style.removeProperty('top');
    selectHeader.style.removeProperty('position');
  }
  lastScrollTop = scrollTop;
});