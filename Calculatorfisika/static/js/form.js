// static/js/form.js
document.addEventListener('DOMContentLoaded', function() {
    const jenisSelect = document.getElementById('jenis');
    const inputEpDiv = document.getElementById('input-ep');
    const inputEkDiv = document.getElementById('input-ek');
    const inputUsahaDiv = document.getElementById('input-usaha');

    // Fungsi untuk mengatur atribut 'required'
    function toggleRequired(divElement, enable) {
        const inputs = divElement.querySelectorAll('input'); // Pilih semua input
        inputs.forEach(input => {
            if (enable) {
                input.setAttribute('required', 'required');
            } else {
                input.removeAttribute('required');
            }
        });
    }

    window.tampilkanInput = function() {
        const selectedValue = jenisSelect.value;

        // Sembunyikan semua div dan nonaktifkan 'required' dari inputnya
        inputEpDiv.style.display = 'none';
        toggleRequired(inputEpDiv, false);

        inputEkDiv.style.display = 'none';
        toggleRequired(inputEkDiv, false);

        inputUsahaDiv.style.display = 'none';
        toggleRequired(inputUsahaDiv, false);

        // Tampilkan div yang relevan dan aktifkan 'required' pada inputnya
        if (selectedValue === 'ep') {
            inputEpDiv.style.display = 'block';
            toggleRequired(inputEpDiv, true);
        } else if (selectedValue === 'ek') {
            inputEkDiv.style.display = 'block';
            toggleRequired(inputEkDiv, true);
        } else if (selectedValue === 'usaha') {
            inputUsahaDiv.style.display = 'block';
            toggleRequired(inputUsahaDiv, true);
        }
    };

    // Panggil saat halaman dimuat untuk mengatur tampilan awal
    tampilkanInput();
});