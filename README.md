
# Flask JWT Authentication API

Proyek ini adalah API berbasis Flask yang menyediakan fitur pendaftaran pengguna, login, dan pengambilan informasi pengguna menggunakan JSON Web Tokens (JWT) untuk autentikasi. Ini mencakup fitur dasar manajemen pengguna, menjadikannya fondasi yang kuat untuk membangun API yang aman.

## Fitur

- **Pendaftaran Pengguna**: Memungkinkan pengguna untuk mendaftar dengan alamat email yang unik.
- **Login Pengguna**: Pengguna yang terautentikasi akan menerima token JWT setelah berhasil login.
- **Informasi Pengguna**: Mengambil dan menampilkan informasi pengguna untuk pengguna yang telah terautentikasi.

## Keputusan Desain

Proyek ini dirancang dengan mempertimbangkan fleksibilitas dan keamanan sebagai prioritas utama. Berikut adalah beberapa keputusan desain yang dibuat:

1. **Penggunaan Flask sebagai Framework Web**: Flask dipilih karena kesederhanaannya dan kemampuannya untuk diperluas sesuai kebutuhan. Flask memungkinkan kami untuk memulai dengan cepat dan memberikan kontrol penuh atas arsitektur aplikasi.

2. **JWT (JSON Web Tokens) untuk Autentikasi**: JWT digunakan untuk mengelola sesi pengguna dengan cara yang aman dan terukur. JWT memungkinkan stateless authentication, di mana server tidak perlu menyimpan informasi sesi, sehingga lebih efisien untuk aplikasi skala besar.

3. **SQLAlchemy sebagai ORM**: Flask-SQLAlchemy dipilih untuk mengelola interaksi dengan database. Ini memberikan antarmuka yang bersih dan Pythonic untuk menulis query database, sekaligus mendukung migrasi database melalui Flask-Migrate.

4. **Struktur Proyek Monolitik**: Proyek ini diorganisasi dalam bentuk monolitik, Semua komponen seperti rute, model, dan layanan ditempatkan dalam beberapa file utama, dan tidak ada pembagian ke dalam modul yang lebih kecil atau terpisah. Pendekatan ini cocok untuk aplikasi kecil atau proyek dengan kompleksitas rendah, di mana memisahkan kode menjadi beberapa modul tidak diperlukan.

## Pilihan Pustaka

- **Flask**: Dipilih karena kesederhanaan, fleksibilitas, dan dokumentasi yang baik.
- **Flask-SQLAlchemy**: Memberikan abstraksi yang kuat untuk bekerja dengan database relasional.
- **Flask-JWT**: Dipilih untuk menangani autentikasi berbasis token dengan cara yang aman dan dapat disesuaikan.
- **Flask-Migrate**: Digunakan untuk mengelola migrasi skema database, memungkinkan perubahan skema dilakukan dengan aman.

## Tantangan

1. **Desain Otentikasi yang Aman**: Mengimplementasikan otentikasi yang aman dengan JWT, sambil memastikan bahwa token hanya disimpan dan dikirimkan dengan cara yang aman, menjadi fokus utama. Ini termasuk penanganan token yang benar di klien serta menjaga keamanan endpoint API.

2. **Pengelolaan Migrasi Database**: Menyusun skema database dan mengelola migrasi untuk memastikan bahwa perubahan skema tidak menyebabkan hilangnya data atau inkonsistensi adalah tantangan yang memerlukan perhatian khusus, terutama dengan alat seperti Flask-Migrate.

## Prasyarat

Untuk menjalankan proyek ini, Anda memerlukan:

- Python 3.7 atau lebih tinggi
- Database MySQL

## Instalasi

Ikuti langkah-langkah ini untuk mengatur proyek di mesin lokal Anda:

1. **Kloning Repository**

   Kloning repository proyek ke mesin lokal Anda menggunakan Git:

   ```bash
   git clone https://github.com/hiskiaphsp/flask-jwt.git
   cd flask-jwt-auth
   ```

2. **Instal Dependensi**

   Instal paket Python yang diperlukan menggunakan file `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurasi Variabel Lingkungan**

   Buat file `.env` di direktori root proyek untuk menyimpan variabel lingkungan yang spesifik:

   ```env
      DB_USERNAME=root
      DB_PASSWORD=
      DB_HOST=localhost
      DB_PORT=3306
      DB_NAME=database
      SECRET_KEY=your_secret_key
   ```

   Ganti `your_secret_key` dengan kunci rahasia yang aman dan sesuaikan `Konfigurasi Databse` sesuai dengan database Anda.

4. **Inisialisasi Database**

   Atur database dengan menjalankan perintah berikut:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Jalankan Aplikasi**

   Mulai server pengembangan Flask:

   ```bash
   flask run --port=8080
   ```

   Aplikasi akan tersedia di `http://127.0.0.1:8080/`.

## Penggunaan

Setelah server berjalan, Anda dapat menggunakan alat seperti Postman untuk berinteraksi dengan API:

- **API Mendaftarkan pengguna baru**:
  - Endpoint: `POST /api/register`
  - Body (JSON):
    ```json
    {
      "name": "test",
      "email": "test@gmail.com.com",
      "password": "password123"
    }
    ```

- **API Login pengguna yang sudah ada**:
  - Endpoint: `POST /api/login`
  - Body (JSON):
    ```json
    {
      "email": "test@gmail.com",
      "password": "password123"
    }
    ```

- **API Mengambil informasi pengguna (membutuhkan JWT)**:
  - Endpoint: `GET /api/user-info`
  - Header:
    ```
    Authorization: Bearer <your_jwt_token>
    ```
- **Halaman Login**:
   - Endpoint: `GET /login`

- **Halaman Register**:
   - Endpoint: `GET /register`

- **Halaman Home**:
   - Endpoint: `GET /`
