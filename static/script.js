document.addEventListener('DOMContentLoaded', function() {
    const movieItems = document.querySelectorAll('.result-card');

    movieItems.forEach(item => {
        item.addEventListener('click', function() {
            const movieLink = item.getAttribute('data-link');

            // Fetch movie details using AJAX
            fetch(`/get-movie-info?link=${encodeURIComponent(movieLink)}`)
                .then(response => response.json())
                .then(data => {
                    console.log('Movie data:', data); // Debugging line

                    document.getElementById('popup-title').innerHTML = `<h2>${data.title}</h2>`;
                    document.getElementById('popup-image').innerHTML = `<img src="${data.image}" alt="${data.title}">`;
                    document.getElementById('popup-synopsis').textContent = data.synopsis;

                    let linksHtml = '';
                    data.linkList.forEach(season => {
                        linksHtml += `<h3>${season.title}</h3><ul>`;
                        season.directLinks.forEach(episode => {
                            linksHtml += `<li><a href="${episode.link}" target="_blank">${episode.title}</a></li>`;
                        });
                        linksHtml += '</ul>';
                    });
                    document.getElementById('popup-links').innerHTML = linksHtml;

                    // Show the pop-up
                    const popupModal = document.getElementById('popup-modal');
                    popupModal.classList.add('visible'); // Show modal
                    console.log('Popup shown'); // Debugging line
                })
                .catch(error => {
                    console.error('Error fetching movie info:', error);
                });
        });
    });

    document.getElementById('close-popup').addEventListener('click', function() {
        const popupModal = document.getElementById('popup-modal');
        popupModal.classList.remove('visible'); // Hide modal
    });
});