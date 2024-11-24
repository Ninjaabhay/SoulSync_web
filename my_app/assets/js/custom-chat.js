const chatWindow = document.getElementById("chat-window");
const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send-btn");

sendButton.addEventListener("click", () => {
  const message = messageInput.value.trim();
  if (message) {
    appendMessage("user", message);
    sendToChatbot(message);
    messageInput.value = "";
    sendButton.disabled = true; // Disable send button temporarily
  }
});

messageInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    sendButton.click();
  }
});

function appendMessage(sender, text) {
  const messageElement = document.createElement("div");
  messageElement.className = sender === "user" ? "user-message" : "bot-message";
  messageElement.textContent = text;
  chatWindow.appendChild(messageElement);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

// Update this function to send the message to the Hugging Face API
function sendToChatbot(message) {
  fetch("/get-chatbot-response/?message=" + encodeURIComponent(message))
    .then((response) => response.json())
    .then((data) => {
      console.log(data); // Log the response to the console
      const reply = data.reply || "Sorry, I couldn't understand that.";
      appendMessage("bot", reply);
    })
    .catch((error) => {
      appendMessage("bot", "Oops! Something went wrong.");
      console.error("Error:", error);
    })
    .finally(() => {
      sendButton.disabled = false;
    });
}
