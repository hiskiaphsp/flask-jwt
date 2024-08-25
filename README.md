
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
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:@localhost/db_auth_jwt
   ```

   Ganti `your_secret_key` dengan kunci rahasia yang aman dan sesuaikan `SQLALCHEMY_DATABASE_URI` sesuai dengan konfigurasi database Anda (misalnya, gunakan `postgresql://user:password@localhost/db_name` untuk PostgreSQL).

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
   flask run
   ```

   Aplikasi akan tersedia di `http://127.0.0.1:5000/`.

## Penggunaan

Setelah server berjalan, Anda dapat menggunakan alat seperti Postman untuk berinteraksi dengan API:

- **Mendaftarkan pengguna baru**:
  - Endpoint: `POST /api/register`
  - Body (JSON):
    ```json
    {
      "name": "johndoe",
      "email": "johndoe@example.com",
      "password": "securepassword123"
    }
    ```

- **Login pengguna yang sudah ada**:
  - Endpoint: `POST /api/login`
  - Body (JSON):
    ```json
    {
      "email": "johndoe@example.com",
      "password": "securepassword123"
    }
    ```

- **Mengambil informasi pengguna (membutuhkan JWT)**:
  - Endpoint: `GET /api/user-info`
  - Header:
    ```
    Authorization: Bearer <your_jwt_token>
    ```
