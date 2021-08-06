//scroll eventlistener for when the user scrolls more than 100 pixels
window.addEventListener(
  "scroll",
  function () {
    if (
      document.body.scrollTop > 100 ||
      document.documentElement.scrollTop > 100
    ) {
      document.getElementById("zero").classList.add("zero-anim");
    }
  },
  true
);
