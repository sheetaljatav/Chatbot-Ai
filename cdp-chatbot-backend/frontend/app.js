document.getElementById('sendBtn').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;

    // Display the user's message
    displayMessage(userInput, 'user-message');

    // Clear the input field
    document.getElementById('userInput').value = '';

    // Send the user's message to the Flask backend
    fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = data.answer || "Sorry, I couldn't understand your question.";
        displayMessage(botMessage, 'bot-message');
    })
    .catch(error => {
        displayMessage("Sorry, there was an error. Please try again later.", 'bot-message');
    });
});

function displayMessage(message, className) {
    const chatbox = document.getElementById('chatbox');
    const newMessage = document.createElement('div');
    newMessage.classList.add(className);
    newMessage.textContent = message;
    chatbox.appendChild(newMessage);

    // Scroll to the latest message
    chatbox.scrollTop = chatbox.scrollHeight;
}
