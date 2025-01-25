// Handles the input submission and interaction with the back-end
document.getElementById('submitInput').addEventListener('click', async () => {
    const userInput = document.getElementById('userInput').value;

    if (userInput) {
        try {
            console.log("kill raunak")
            const response = await fetch('/run-therapy', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_input: userInput })
            });
            
            const data = await response.json();
            console.log(data)
            document.getElementById('response').innerText = data.response;
            document.getElementById('responseSection').style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
        }
    } else {
        alert('Please enter your feelings!');
    }
});

document.getElementById('submitFeedback').addEventListener('click', async () => {
    const therapyFeedback = document.getElementById('therapyFeedback').value;

    if (therapyFeedback) {
        try {
            const response = await fetch('/submit-feedback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ therapy_feedback: therapyFeedback })
            });

            const result = await response.json();
            console.log(result)
            document.getElementById('finalResult').innerText = result.finalResult;

            const images = result.images;
            const imagesContainer = document.getElementById('images');
            imagesContainer.innerHTML = ''; // Clear any previous images

            images.forEach(image => {
                const img = document.createElement('img');
                img.src = image;
                img.alt = 'Calming Image';
                img.style.width = '200px';
                img.style.margin = '10px';
                imagesContainer.appendChild(img);
            });

            document.getElementById('resultSection').style.display = 'block';
        } catch (error) {
            console.error('Error:', error);
        }
    } else {
        alert('Please provide feedback on the therapy!');
    }
});

document.getElementById('playSound').addEventListener('click', () => {
    const audio = new Audio('../sounds/relaxing-piano-guitar.mp3'); // Update with your sound file path
    audio.play();
});
