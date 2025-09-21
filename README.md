link : https://mohammad-aly-soccercommerce.pbp.cs.ui.ac.id/

*JAWABAN TUGAS 3 DAN SETERUSNYA ADA DI BAWAH*

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



Tugas 3

1. Data delivery diperlukan dalam pengimplementasian sebuah platform karena memastikan data yang dikumpulkan, diproses, dan disajikan dapat sampai ke pengguna atau komponen sistem lain dengan tepat waktu, akurat, dan dalam format yang sesuai. Alasannya yaitu konsistensi data, realtime experience, integrasi antar komponen dan lain lain.

2. JSON umumnya dianggap lebih baik karena lebih mudah dibaca dan lebih cepat di proses. SON menggunakan struktur yang sederhana berbasis objek dan array, sehingga cocok untuk aplikasi web dan API yang membutuhkan transfer data cepat dan efisien. Sementara itu, XML memiliki sintaks yang lebih kompleks dengan banyak tag pembuka dan penutup, sehingga ukuran data menjadi lebih besar dan parsing lebih lambat. Popularitas JSON juga didorong oleh dukungannya yang erat dengan JavaScript (native di browser), membuat integrasi dengan aplikasi web lebih mudah.

3. Method is_valid() pada form Django berfungsi untuk memeriksa apakah data yang dikirimkan melalui form memenuhi semua aturan validasi yang telah ditentukan, baik validasi bawaan (seperti field yang wajib diisi, format email yang benar) maupun validasi kustom yang didefinisikan oleh developer. Method ini penting karena memastikan hanya data yang benar, lengkap, dan sesuai aturan yang akan diproses lebih lanjut atau disimpan ke database, sehingga mencegah error dan menjaga integritas data dalam aplikasi.

4. csrf_token pada Django digunakan untuk melindungi aplikasi dari CSRF (Cross-Site Request Forgery), yaitu serangan di mana pengguna tanpa sadar mengirimkan request berbahaya ke server saat mereka sudah login. Jika token tidak ada atau tidak cocok, Django akan menolak request tersebut. Jika kita tidak menambahkan csrf_token, Django akan menganggap request POST tidak aman dan akan mengembalikan error 403 Forbidden.

Serangan CSRF (Cross-Site Request Forgery) bisa dimanfaatkan penyerang dengan cara memaksa pengguna yang sedang login untuk mengirimkan request berbahaya tanpa sepengetahuan mereka. Contohnya, jika kamu sedang login di aplikasi bank, penyerang bisa membuat halaman berisi form tersembunyi yang otomatis melakukan POST request untuk mentransfer uang ke akun mereka. Karena browsermu secara otomatis mengirimkan cookie sesi saat request dilakukan, server akan menganggap itu adalah request sah dari kamu, padahal kamu tidak pernah benar-benar mengklik tombol transfer.

5. 

Client (Postman / Browser)
     |
     | 1. Mengirim HTTP Request (GET/POST/PUT/DELETE)
     v
URL Router / Dispatcher
(urls.py atau routes.js)
     |
     | 2. Mencocokkan URL dengan pola (endpoint API)
     v
View / Controller
(views.py atau controller.js)
     |
     | 3. Menjalankan logika bisnis sesuai request
     | 4. Memanggil Serializer/Validator untuk validasi data
     v
Serializer / Validator
(serializers.py / schema validation)
     |
     | 5. Mengecek apakah data valid
     |    - Jika valid → lanjut
     |    - Jika tidak → kembalikan error response (400)
     v
Model / Database
(models.py / ORM)
     |
     | 6. Mengambil / menyimpan data di database
     v
View / Controller
(views.py atau controller.js)
     |
     | 7. Menyiapkan Response (JSON)
     v
HTTP Response
(JSON Response)
     |
     | 8. Mengirim response kembali ke Client
     v
Client (Postman / Browser)
     |
     | 9. Menampilkan hasil response (status code + body)

6. tidak ada

link gambar POSTMAN :

https://drive.google.com/drive/folders/1k8qZLErAUMahK2kJrU42onvPL4esjMY5?usp=sharing 




Tugas 4 

1. AuthenticationForm adalah form bawaan Django yang digunakan untuk menangani proses login pengguna. Form ini secara otomatis menyediakan field username dan password, serta melakukan validasi terhadap data yang dimasukkan dengan membandingkannya ke database user yang disediakan Django. Keunggulan utama dari AuthenticationForm adalah kemudahannya karena langsung terintegrasi dengan sistem autentikasi Django, aman secara default karena menggunakan hashing password, serta dapat dengan mudah diperluas jika ingin menambahkan field tambahan seperti "remember me". Namun, kelemahannya adalah kurang fleksibel jika ingin menerapkan metode login yang berbeda, misalnya login dengan email saja atau integrasi social login, dan tampilannya perlu disesuaikan secara manual agar sesuai dengan desain aplikasi. 

2. Autentikasi dan otorisasi adalah dua konsep berbeda dalam keamanan aplikasi web. Autentikasi adalah proses memverifikasi identitas pengguna, atau dengan kata lain memastikan bahwa pengguna benar-benar adalah orang yang dia klaim. Contohnya adalah saat pengguna login dengan username dan password. Otorisasi adalah proses menentukan hak akses pengguna setelah identitasnya diverifikasi, misalnya memastikan hanya admin yang bisa mengakses halaman /admin. Django mengimplementasikan autentikasi melalui fungsi authenticate() dan login() yang menyimpan informasi pengguna di session, sementara otorisasi diimplementasikan melalui sistem permission bawaan, dekorator seperti @login_required, @permission_required, serta atribut is_staff dan is_superuser yang dapat digunakan untuk membatasi akses ke fitur tertentu. 

3. Session dan cookies adalah dua mekanisme umum untuk menyimpan state di aplikasi web. Session menyimpan data di sisi server, sedangkan hanya session ID yang dikirimkan ke client melalui cookie. Keunggulan session adalah lebih aman karena data tidak terlihat oleh pengguna, serta bisa menyimpan data yang kompleks. Kekurangannya adalah membutuhkan storage di server, dan data bisa hilang jika server di-restart tanpa konfigurasi penyimpanan yang persisten. Sebaliknya, cookies menyimpan data langsung di browser pengguna sehingga ringan dan tidak membebani server. Namun, cookies memiliki keterbatasan ukuran (umumnya hanya 4KB), dan karena berada di sisi client, dapat dimodifikasi oleh pengguna sehingga berisiko jika tidak ditandatangani atau dienkripsi.


4. Penggunaan cookies tidak sepenuhnya aman secara default karena terdapat risiko seperti pencurian cookie melalui serangan XSS atau penyadapan data jika tidak menggunakan HTTPS. Selain itu, karena cookie disimpan di sisi pengguna, data di dalamnya bisa dimodifikasi. Django mengatasi hal ini dengan secara default menandatangani cookie session menggunakan SECRET_KEY sehingga perubahan tidak sah dapat terdeteksi. Django juga menyediakan pengaturan keamanan seperti SESSION_COOKIE_HTTPONLY untuk mencegah akses cookie melalui JavaScript, serta SESSION_COOKIE_SECURE untuk memastikan cookie hanya dikirim melalui koneksi HTTPS. Dengan pengaturan ini, risiko manipulasi dan pencurian cookie dapat diminimalisir.

5. Untuk mengimplementasikan registration, Django menyediakan UserCreationForm yang dapat digunakan untuk membuat akun baru melalui view sederhana yang memproses form dan menyimpannya ke database jika valid. Proses login dapat menggunakan AuthenticationForm yang memverifikasi username dan password, lalu menggunakan fungsi login() untuk menyimpan informasi pengguna di session sehingga pengguna tetap terautentikasi selama sesi berlangsung. Logout dilakukan dengan fungsi logout() yang menghapus session pengguna. Untuk cookies, Django menyediakan API sederhana melalui objek HttpResponse untuk membuat dan mengirim cookie ke browser, serta request.COOKIES untuk membaca nilai cookie. Dengan kombinasi ini, kita bisa membangun alur autentikasi lengkap dengan registration, login, logout, dan penyimpanan state tambahan melalui cookies.