#!/usr/bin/node

const socket = new WebSocket("ws://localhost:8000/ws");

const statusEl = document.getElementById("status");
const messagesEl = document.getElementById("messages");
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");

function addMessage(text, type) {
    const li = document.createElement("li");
    li.className = `message ${type}`;

    const time = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    li.textContent = `[${time}] ${text}`;

    messagesEl.appendChild(li);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

socket.onopen = () => {
    statusEl.textContent = "Connected";
    statusEl.className = "status connected";
    addMessage("Connected to server", "system");
};

socket.onmessage = (event) => {
    addMessage(`Server: ${event.data}`, "received");
};

socket.onclose = () => {
    statusEl.textContent = "Disconnected";
    statusEl.className = "status disconnected";
    addMessage("Connection closed", "system");
};

socket.onerror = () => {
    statusEl.textContent = "Connection error";
    statusEl.className = "status disconnected";
};

chatForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const message = messageInput.value;
    if (message.trim() === "") {
        return;
    }

    if (socket.readyState === WebSocket.OPEN) {
        socket.send(message);
        addMessage(`You: ${message}`, "sent");
        messageInput.value = "";
        messageInput.focus();
    }
});
