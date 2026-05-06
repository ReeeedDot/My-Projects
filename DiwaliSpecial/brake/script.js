const startBtn = document.getElementById('start-btn');
const stopBtn = document.getElementById('stop-btn');
const fireworks = document.querySelectorAll('.firework');
const crackers = document.querySelectorAll('.cracker');

let isAnimating = false;

startBtn.addEventListener('click', () => {
	if (!isAnimating) {
		isAnimating = true;
		fireworks.forEach(firework => firework.classList.add('active'));
		crackers.forEach(cracker => cracker.classList.add('active'));
	}
});

stopBtn.addEventListener('click', () => {
	if (isAnimating) {
		isAnimating = false;
		fireworks.forEach(firework => firework.classList.remove('active'));
		crackers.forEach(cracker => cracker.classList.remove('active'));
	}
});