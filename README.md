
# Flask JWT Authentication API

Proyek ini adalah API berbasis Flask yang menyediakan fitur pendaftaran pengguna, login, dan pengambilan informasi pengguna menggunakan JSON Web Tokens (JWT) untuk autentikasi. Ini mencakup fitur dasar manajemen pengguna, menjadikannya fondasi yang kuat untuk membangun API yang aman.

## Fitur

- **Pendaftaran Pengguna**: Memungkinkan pengguna untuk mendaftar dengan alamat email yang unik.
- **Login Pengguna**: Pengguna yang terautentikasi akan menerima token JWT setelah berhasil login.
- **Informasi Pengguna**: Mengambil dan menampilkan informasi pengguna untuk pengguna yang telah terautentikasi.

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
