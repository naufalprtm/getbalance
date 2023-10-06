# getbalance
# *scan auto get balance EVM chain with python*

Kode yang disediakan berinteraksi dengan blockchain Binance Smart Chain (BSC) dan API CoinGecko untuk mengambil informasi tentang token tertentu dan menghitung nilainya dalam USD. Berikut cara menggunakan dan memahami kodenya:

Instal Paket yang Diperlukan:
Pastikan Anda telah menginstal paket Python yang diperlukan. Anda dapat menginstalnya menggunakan pip:

bash
Salin kode
pip instal pycoinecko web3 colorama
Siapkan Skrip:
Simpan kode yang diberikan ke dalam file Python, misalnya token_info.py.

Konfigurasi Token dan Dompet:
Ganti nilai placeholder dengan nilai sebenarnya untuk alamat token dan dompet Anda:

Ganti token_address dengan alamat kontrak token ERC20 yang ingin Anda analisis.
Ganti string kosong di wallet_addresses dengan alamat yang ingin Anda periksa.
Jalankan Skrip:
Jalankan skrip menggunakan Python:

bash
Salin kode
python token_info.py
Skrip akan menampilkan informasi token, harga BNB, saldo token untuk alamat yang ditentukan, nilainya dalam USD, dan hitungan mundur selama 3 detik.

Penjelasan Kode:

Kode ini menginisialisasi koneksi ke BSC menggunakan Web3 dan CoinGecko untuk mengambil harga token.
Ini mendefinisikan fungsi untuk mengambil saldo BNB, saldo token, dan harga token.
Ini menghitung nilai total dalam USD untuk setiap alamat dompet dengan mempertimbangkan nilai token dan saldo BNB.
Terakhir, ia mencetak informasi dalam format terstruktur menggunakan colorama untuk visibilitas yang lebih baik.
