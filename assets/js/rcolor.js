let safeColors = ['00','33','66','99','cc','ff'];
let rand = function() {
    return Math.floor(Math.random()*6);
};
let randomColor = function() {
    let r = safeColors[rand()];
    let g = safeColors[rand()];
    let b = safeColors[rand()];
    document.getElementById("mess").style.backgroundColor = "#" + r + g + b;
};