const tg = window.Telegram?.WebApp;
if (tg) {
  tg.expand();
  tg.MainButton.hide();
}

const heartsContainer = document.getElementById("floatingHearts");
const floatingEmoji = ["💕", "💖", "💗", "💝", "❤️", "💜", "✨", "🌸"];

let currentStep = 1;

function randomBetween(min, max) {
  return Math.random() * (max - min) + min;
}

function createFloatingItem() {
  if (!heartsContainer) {
    return;
  }

  const el = document.createElement("span");
  el.className = "float-item";
  el.textContent = floatingEmoji[Math.floor(Math.random() * floatingEmoji.length)];
  el.style.left = `${randomBetween(2, 96)}%`;
  el.style.animationDuration = `${randomBetween(5, 10)}s`;
  el.style.fontSize = `${randomBetween(16, 34)}px`;

  heartsContainer.appendChild(el);
  setTimeout(() => el.remove(), 11000);
}

function showConfetti() {
  if (!heartsContainer) {
    return;
  }

  for (let i = 0; i < 30; i += 1) {
    setTimeout(() => {
      const confetti = document.createElement("span");
      confetti.className = "confetti";
      confetti.textContent = floatingEmoji[Math.floor(Math.random() * floatingEmoji.length)];
      confetti.style.left = `${randomBetween(0, 100)}%`;
      confetti.style.animationDuration = `${randomBetween(2.8, 4.8)}s`;
      confetti.style.fontSize = `${randomBetween(14, 28)}px`;
      heartsContainer.appendChild(confetti);

      setTimeout(() => confetti.remove(), 5200);
    }, i * 90);
  }
}

function goToStep(stepNumber) {
  const nextStep = document.getElementById(`step-${stepNumber}`);
  const current = document.getElementById(`step-${currentStep}`);

  if (!nextStep || !current || stepNumber === currentStep) {
    return;
  }

  current.classList.remove("active");
  nextStep.classList.add("active");
  currentStep = stepNumber;

  if (tg?.HapticFeedback) {
    tg.HapticFeedback.impactOccurred("light");
  }

  if (stepNumber === 3) {
    showConfetti();
  }
}

for (let i = 0; i < 12; i += 1) {
  setTimeout(createFloatingItem, i * 140);
}

setInterval(createFloatingItem, 500);

document.getElementById("openStep2")?.addEventListener("click", () => goToStep(2));
document.getElementById("openStep3")?.addEventListener("click", () => goToStep(3));
