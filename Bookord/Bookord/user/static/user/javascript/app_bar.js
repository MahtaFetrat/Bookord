//scroll eventlistener for when the user scrolls more than 100 pixels
window.addEventListener(
  "scroll",
  function () {
    if (
      document.body.scrollTop > 100 ||
      document.documentElement.scrollTop > 100
    ) {
      //this adding a class to elements is the best way to trigger animations from javascript
      document.getElementById("description").classList.add("description-anim");
      document.getElementById("brand").classList.add("brand-anim");
      document.getElementById("navbar").classList.add("navbar-anim");
    }
  },
  true
);

//to scroll back to top on page reload
window.addEventListener(
  "unload",
  function () {
    window.scrollTo(0, 0);
  },
  true
);
