document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (e) {
        let valid = true;
        const requiredFields = form.querySelectorAll('input[required], select[required], textarea[required]');

        requiredFields.forEach(field => {
            if (!field.value) {
                field.style.borderColor = 'red';
                valid = false;
            } else {
                field.style.borderColor = '#ccc';
            }
        });

        if (!valid) {
            e.preventDefault();
            alert('Please fill out all required fields.');
        }
    });
});
