
const connection = document.getElementById("connection");
const statusText = document.getElementById("status");
const micButton = document.getElementById("micButton");
const userCommand = document.getElementById("userCommand");
const jarvisResponse = document.getElementById("jarvisResponse");

// Check backend connection
async function checkConnection() {
    try {
        const response = await fetch("/status");
        const data = await response.json();

        if (!response.ok) throw new Error("Server error");

        connection.textContent = "● SYSTEM ONLINE";
        connection.style.color = "#00ff99";
        statusText.textContent = data.status;

    } catch (error) {
        connection.textContent = "● SYSTEM OFFLINE";
        connection.style.color = "#ff5b5b";
        statusText.textContent = "Connection Lost";
    }
}

checkConnection();
setInterval(checkConnection, 5000);


// Activate real Python microphone
micButton.addEventListener("click", async function () {
    micButton.disabled = true;
    micButton.textContent = "🔵 LISTENING...";
    statusText.textContent = "Listening... Speak now!";
    userCommand.textContent = "Waiting for your voice...";
    jarvisResponse.textContent = "JARVIS is listening...";

    try {
        const response = await fetch("/command", {
            method: "POST"
        });

        const data = await response.json();

        userCommand.textContent = data.command || "No command detected";
        jarvisResponse.textContent = data.response;

        statusText.textContent = data.success
            ? "Command Executed"
            : "Ready for another command";

    } catch (error) {
        jarvisResponse.textContent = "Voice connection failed.";
        statusText.textContent = "System Error";
    }

    micButton.disabled = false;
    micButton.textContent = "🎙 TALK TO JARVIS";
});
