link : https://mohammad-aly-soccercommerce.pbp.cs.ui.ac.id/

1. Struktur proyek pada gambar adalah contoh penerapan pola MVT (Model–View–Template) di Django. Untuk membuatnya, pertama kita perlu membuat proyek Django baru dengan perintah django-admin startproject nama_proyek, yang akan menghasilkan folder utama (seperti soccer_commerce pada gambar) berisi file penting seperti settings.py, urls.py, dan manage.py. Setelah itu, kita buat aplikasi baru di dalam proyek dengan python manage.py startapp main. Folder aplikasi main akan berisi file bawaan seperti models.py, views.py, urls.py, dan tests.py.

Pada bagian Model, kita mendefinisikan struktur data dalam models.py, misalnya kelas Product yang mewakili entitas produk dengan atribut seperti name, price, quantity, dan sebagainya. Model ini akan otomatis terhubung dengan database setelah kita melakukan migrasi dengan python manage.py makemigrations dan python manage.py migrate.

Bagian View diimplementasikan dalam views.py, di mana kita membuat fungsi seperti show_main(request) untuk memproses data dari model (jika diperlukan) dan mengirimkannya ke template. View ini kemudian dihubungkan dengan URL pada main/urls.py, misalnya dengan path('', show_main, name='show_main').

Bagian Template berada di folder templates di dalam aplikasi, di mana kita membuat file HTML seperti main.html. File ini berisi struktur tampilan halaman yang akan dirender. View akan memanggil render(request, "main.html", context) untuk menampilkan data ke pengguna.

Terakhir, kita perlu mendaftarkan aplikasi main ke INSTALLED_APPS di settings.py dan meng-include main.urls pada soccer_commerce/urls.py, agar URL dari aplikasi bisa diakses. Dengan langkah-langkah ini, kita berhasil membuat pola MVT yang memisahkan logika data (Model), logika bisnis (View), dan tampilan (Template) dengan rapi, seperti struktur pada gambar. 

2. 

Client (Browser)
     |
     | 1. Mengirim HTTP Request (GET/POST)
     v
Django URL Dispatcher
(urls.py)
     |
     | 2. Mencocokkan URL dengan pola (path/route)
     v
View Function / Class
(views.py)
     |
     | 3. Menjalankan logika bisnis
     | 4. Jika perlu, mengambil/menyimpan data dari/ke Database
     v
Model
(models.py)
     |
     | 5. Mengambil/menyimpan data dari/ke database
     v
View Function / Class
(views.py)
     |
     | 6. Mengolah data dan menyiapkan context
     v
Template
(HTML)
     |
     | 7. Merender halaman HTML menggunakan data dari view
     v
HTTP Response
     |
     | 8. Mengirim halaman yang sudah dirender ke client
     v
Client (Browser)


3. settings.py adalah file konfigurasi utama pada proyek Django yang berfungsi mengatur seluruh perilaku aplikasi. Di dalamnya terdapat pengaturan penting seperti koneksi database, daftar aplikasi yang digunakan (INSTALLED_APPS), middleware, pengaturan keamanan (misalnya SECRET_KEY, ALLOWED_HOSTS), konfigurasi template, static files, bahasa, zona waktu, hingga opsi debugging. File ini memungkinkan pengembang menyesuaikan lingkungan proyek (development, staging, production) tanpa mengubah kode inti aplikasi. Dengan kata lain, settings.py menjadi pusat kendali yang memastikan aplikasi Django berjalan sesuai kebutuhan dan lingkungan tempat aplikasi dijalankan.

4. Migrasi database di Django adalah proses sinkronisasi antara struktur model di models.py dengan struktur tabel di database. Ketika developer membuat atau mengubah model, Django menggunakan perintah python manage.py makemigrations untuk membuat file migrasi yang berisi instruksi perubahan skema (misalnya membuat tabel baru, menambah kolom, atau mengubah tipe data). Setelah itu, perintah python manage.py migrate dijalankan untuk menerapkan file migrasi tersebut ke database sehingga struktur tabel sesuai dengan definisi model terbaru. Proses ini memungkinkan perubahan skema database dilakukan secara terkontrol, bertahap, dan dapat dilacak melalui file migrasi, sehingga memudahkan pengelolaan versi database di berbagai lingkungan pengembangan maupun produksi.

5. Django sering dijadikan permulaan pembelajaran pengembangan perangkat lunak karena sifatnya yang terstruktur, lengkap, dan “batteries-included”, sehingga memudahkan pemula memahami konsep fundamental pengembangan aplikasi web tanpa harus membangun semuanya dari nol. Framework ini menyediakan komponen penting seperti autentikasi, ORM (Object Relational Mapping), routing, templating, hingga panel admin bawaan, yang memungkinkan mahasiswa atau pemula fokus pada logika bisnis alih-alih konfigurasi teknis yang rumit. Selain itu, Django menerapkan pola arsitektur MVT (Model-View-Template) yang membantu memahami pemisahan tanggung jawab dalam pengembangan perangkat lunak. Dokumentasinya juga sangat lengkap dan komunitasnya besar, sehingga pembelajaran menjadi lebih mudah. Hal ini membuat Django cocok sebagai “pintu masuk” sebelum beralih ke framework lain atau pendekatan yang lebih kompleks. 

6. Tidak.