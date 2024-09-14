// Fungsi untuk menyembunyikan marker
function hideMarker(marker) {
    marker.setOpacity(0); // Mengatur opasitas menjadi 0
  }
  
  // Fungsi untuk menampilkan kembali marker
  function showMarker(marker) {
    marker.setOpacity(1); // Mengatur opasitas menjadi 1
  }
  
  // Menggunakan fungsi hideMarker dan showMarker pada event klik marker
  marker1.on('click', function() {
    hideMarker(marker1);
    console.log('Marker 1 diklik!');
  });
  
  marker2.on('click', function() {
    hideMarker(marker2);
    console.log('Marker 2 diklik!');
  });
  