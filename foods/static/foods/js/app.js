document.addEventListener('DOMContentLoaded', function () {
    const modalElement = document.getElementById('foodModal');
    if (modalElement && document.body.getAttribute('data-show-modal') === 'true') {
        const modal = new bootstrap.Modal(modalElement);
        modal.show();
    }
});
