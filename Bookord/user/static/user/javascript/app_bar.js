//together with whats in html, this is how u pass context to javascrips
const header = JSON.parse(document.getElementById("header").textContent);

//see https://www.sitepoint.com/community/t/cannot-read-property-classlist-of-null-responsive-menu/349372/2 for why wrap things in this eventlistener
window.addEventListener("DOMContentLoaded", function () {
  if (!header.cloud) {
    document.getElementById("navbar").classList.add("navbar");
    document.getElementById("brand").classList.add("brand");
    document.getElementById("brand-container").classList.add("brand-container")
  } else {
    document.getElementById("brand").classList.add("brand-cloud");
    document.getElementById("navbar").classList.add("navbar-cloud");
    //scroll eventlistener for when the user scrolls more than 100 pixels
    window.addEventListener(
      "scroll",
      function () {
        if (
          document.body.scrollTop > 100 ||
          document.documentElement.scrollTop > 100
        ) {
          //this adding a class to elements is the best way to trigger animations from javascript
          document
            .getElementById("description")
            .classList.add("description-anim");
          document.getElementById("brand").classList.add("brand-anim");
          document.getElementById("navbar").classList.add("navbar-anim");
          document
            .getElementById("brand-container")
            .classList.add("brand-container-anim");
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
  }
});
