function toggleMenu() {
    var sidebar = document.getElementById("mySidebar");
    if (sidebar.style.width == "0px" || sidebar.style.width === "") {
        sidebar.style.width = "250px";
    } else {
        sidebar.style.width = "0px";
    }
}

function goBack() {
    window.history.back();
}


