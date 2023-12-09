function updateText() {
    $.ajax({
        url: '/get_text',
        success: function(response) {
            $('#custom-output-textbox').val(response.text);
        }
    });
}

// Call the updateText function initially to load the initial text
updateText();

// Set an interval to update the text every few seconds
setInterval(updateText, 1000);

function openSettings() {
    window.location.href = 'settings';
}
