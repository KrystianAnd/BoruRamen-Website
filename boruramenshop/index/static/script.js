document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("pl").addEventListener("click", function () {
        changeLanguage("pl");
    });

    document.getElementById("en").addEventListener("click", function () {
        changeLanguage("en");
    });

    function changeLanguage(lang) {
        fetch(`/set-language/?lang=${lang}`, { method: "GET" })
            .then(() => location.reload()); 
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const burger = document.getElementById("burger");
    const nav = document.querySelector(".navi");
    const language = document.querySelector(".language");

    burger.addEventListener("click", function() {
        nav.classList.toggle("hidden"); 
        language.classList.toggle("hidden");
    });
});

