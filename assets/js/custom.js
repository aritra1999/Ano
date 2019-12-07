openButton = document.getElementById("menuopen");
closeButton = document.getElementById("menuclose");
deskNav = document.getElementById("desknav");
mobileNav = document.getElementById("mobilenav");
let count = 1;

openButton.onclick = function () {
    deskNav.style.display="none";
    mobileNav.style.display="flex";
    count++;
};

closeButton.onclick = function () {
    mobileNav.style.display="none";
    count--;
};