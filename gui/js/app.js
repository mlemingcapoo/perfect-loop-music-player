// this file is for the first loading screen, or initialization

async function callPython() {
    console.log("callPython");
}

async function allReady() {
    console.log("All ready!!!");
    // this is example of how to call backend
    // const response = await window.pywebview.api.call_backend(text);
}

$(document).ready(async () => {
    // prevent default form submission
    $('form').submit(function (event) {
        event.preventDefault();
    });

});
