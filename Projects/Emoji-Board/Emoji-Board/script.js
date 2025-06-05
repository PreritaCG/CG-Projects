document.querySelectorAll('.emoji').forEach(emoji => {
  emoji.addEventListener('click', function () {
    const mood = this.getAttribute('data-mood');
    const color = this.getAttribute('data-color');
    const gif = this.getAttribute('data-gif');
    document.body.style.backgroundColor = color;
    document.getElementById('mood-text').textContent = `Feeling ${mood}`;
    document.getElementById('mood-image').src = gif;
    document.getElementById('mood-image').style.display = 'block'; // Show the image
  });
});