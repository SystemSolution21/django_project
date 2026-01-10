// blog/static/blog/script.js
// Add event listener to logout link
const logoutLink = document.getElementById("logout-link");
if (logoutLink) {
  logoutLink.addEventListener("click", function (e) {
    e.preventDefault();
    document.getElementById("logout-form").submit();
  });
}
