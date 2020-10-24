# {{ project_name }}

[![Test and Deploy][actions-badge]][commits-gh]
[![pipeline status][pipeline-badge]][commits-gl]
[![coverage report][coverage-badge]][commits-gl]

Repositori ini berisi sebuah templat untuk membuat proyek Django yang siap
di-*deploy* ke Heroku melalui GitHub Actions atau GitLab CI.

*To view this file in English, [click here][readme-en].*

## Daftar isi

- [Daftar isi](#daftar-isi)
- [Instruksi penggunaan](#instruksi-penggunaan)
- [Lanjutan](#lanjutan)
- [Tips pengembangan](#tips-pengembangan)
- [Sihir macam apa ini?](#sihir-macam-apa-ini)
- [Berkontribusi](#berkontribusi)
- [Lisensi](#lisensi)

## Instruksi penggunaan

1. Buat direktori untuk proyek yang akan kamu buat (contoh: `project_name`), lalu
   buka Command Prompt (cmd) atau Terminal di dalam direktori tersebut.

2. Buat Python *virtual environment* di dalamnya.

   ```shell
   python -m venv venv
   ```

   > Catatan: sesuaikan dengan *executable* `python` yang ada di komputer kamu,
   > karena terkadang (misal: di Ubuntu atau macOS) Python 3 hanya bisa
   > dipanggil dengan `python3`, bukan `python`.

3. Aktifkan *virtual environment* yang telah dibuat.\
   Di Windows:

   ```shell
   venv\Scripts\activate
   ```

   Di Linux/macOS:

   ```shell
   source venv/bin/activate
   ```

   Jika berhasil, akan muncul `(venv)` pada *prompt* cmd/terminal kamu.

4. Instal Django pada *virtual environment* tersebut.

   ```shell
   python -m pip install Django
   ```

5. Buat proyek Django baru dengan templat ini.

   ```shell
   django-admin startproject --template="https://codeload.github.com/laymonage/django-template-heroku/zip/template" --extension="py,yml,md" --name="Procfile" project_name .
   ```

   > Catatan: ubah `project_name` dengan nama proyek yang kamu inginkan.
   > Perhatikan bahwa terdapat tanda titik (`.`) di akhir perintah.
   > Apabila muncul *error* terkait pengunduhan templat dari GitHub, silakan
   > kunjungi pranala tersebut secara manual dan arahkan argumen `--template`
   > ke lokasi berkas `.zip` yang sudah kamu unduh ke komputer kamu.

6. Masuk ke [Heroku Dashboard][heroku-dashboard] dan buat aplikasi Heroku baru.
   Nama aplikasi ini **tidak harus sama** dengan nama proyek Django kamu. Lalu,
   buka bagian **Settings** dari aplikasi tersebut. Pada bagian **Config
   Vars**, klik tombol **Reveal Config Vars**. Tambahkan variabel bernama
   `HEROKU_APP_NAME` yang bernilai nama aplikasi Heroku kamu **tanpa
   `.herokuapp.com`**. Lalu, tambahkan juga variabel bernama `SECRET_KEY`
   dengan nilai berupa sebuah kunci yang dihasilkan oleh situs
   [Djecrety][djecrety].

7. Buat *project*/repositori baru di GitLab/GitHub (pilih salah satu).
   **Jangan** pilih opsi untuk menginisialisasi repositori dengan `README.md`,
   `LICENSE`, ataupun `.gitignore`. Biarkan kosong saja.

8. Jika menggunakan GitLab, buka menu **Settings > CI/CD** di *sidebar*
   sebelah kiri. Pada bagian **Variables**, tambahkan variabel bernama
   `HEROKU_API_KEY` yang bernilai API *key* akun Heroku kamu. Lalu, tambahkan
   juga variabel bernama `HEROKU_APP_NAME` yang bernilai nama aplikasi Heroku
   kamu **tanpa `.herokuapp.com`**.

   Jika menggunakan GitHub, lakukan hal yang sama melalui menu **Settings >
   Secrets**.

   > Catatan: API *key* akun Heroku kamu dapat dilihat melalui
   > [**Account settings**][account-settings].

9. **Jika menggunakan GitHub**, pindahkan berkas `tnd.yml` ke direktori
   `.github/workflows` dengan cara berikut.

   Di Windows:

   ```shell
   mkdir ".github\workflows"
   move tnd.yml ".github\workflows\"
   ```

   Di Linux/macOS:

   ```shell
   mkdir -p .github/workflows
   mv tnd.yml .github/workflows/
   ```

   Jika hanya menggunakan GitLab, kamu dapat menghapus berkas `tnd.yml`.
   Jika hanya menggunakan GitHub, kamu dapat menghapus berkas `.gitlab-ci.yml`.

10. Buat direktori proyek kamu menjadi sebuah repositori Git dan buatlah
    *commit* pertama.

    ```shell
    git init
    git add .
    git commit -m "Initial commit"
    ```

11. Tambahkan *remote* baru bernama `origin` yang mengarah ke repositori yang
    kamu buat di GitLab/GitHub, lalu push ke repositori tersebut.

    ```shell
    git remote add origin https://gitlab.com/usernamekamu/project-name.git
    git push -u origin master
    ```

12. Silakan cek **Pipelines** di GitLab atau Actions di GitHub. Jika
    langkah-langkah diikuti dengan benar, maka proyek Django kamu akan berhasil
    di-*deploy* ke Heroku.

    > Contoh: https://django-template-heroku.herokuapp.com

13. Selamat! Sekarang, kamu hanya perlu fokus mengembangkan proyek web kamu
    tanpa perlu pusing dengan masalah *deployment*. Untuk mengembangkan
    proyek web kamu, silakan instal terlebih dahulu *package-package* yang
    diperlukan dengan perintah berikut.

    ```shell
    python -m pip install -r requirements.txt
    ```

14. Lanjutkan dengan membuat basis data lokal dan mengumpulkan
    berkas *static* menjadi satu direktori dengan perintah-perintah berikut.

    ```shell
    python manage.py migrate
    python manage.py collectstatic
    ```
15. Jika sudah, kamu bisa menjalankan *web server* kamu secara lokal dengan
    perintah berikut.

    ```shell
    python manage.py runserver
    ```

16. Mulai dari sini, kamu cukup edit berkas-berkas proyek Django kamu
    sesuai kebutuhan. Lalu, jangan lupa gunakan perintah `git add`,
    `git commit`, dan `git push` untuk mengunggah perubahanmu ke GitLab/GitHub
    (yang kemudian akan di-*deploy* ke Heroku). Jangan lupa untuk membuat
    berkas-berkas *migrations* jika kamu mengubah berkas `models.py`.

    ```shell
    python manage.py makemigrations
    ```

    Berkas-berkas *migrations* yang dihasilkan **harus** dimasukkan ke dalam
    repositori <sup><sub>(kecuali kamu mengubah konfigurasi templat sehingga
    hal tersebut tidak diperlukan... tetapi mengapa?)</sub></sup>.

17. Untuk menjalankan *unit test*, kamu bisa gunakan perintah berikut.

    ```shell
    python manage.py test --exclude-tag=functional
    ```

## Lanjutan

Setelah berhasil membuat proyek Django baru dengan templat ini, ada
langkah-langkah lanjutan yang sangat direkomendasikan untuk dikerjakan demi
kemudahan pengembangan web kamu ke depannya.

1. Tambahkan Django *super user* baru ke aplikasi kamu yang ada di Heroku.

   Basis data yang digunakan di komputer lokal kamu **berbeda** dengan yang
   digunakan di Heroku. Secara *default*, kamu menggunakan basis data SQLite
   yang disimpan dalam berkas `db.sqlite3`, sedangkan Heroku menggunakan basis
   data PostgreSQL yang di-*host* di *cloud*.

   Untuk dapat mengakses situs administrasi Django milik proyek kalian yang ada
   di Heroku, buka Heroku Dashboard. Lalu, klik aplikasi kalian dan klik tombol
   **More > Run console** di pojok kanan atas. Ketik `bash` pada dialog
   *pop-up* yang muncul. Jika sudah, masukkan perintah
   `python manage.py createsuperuser` dan ikuti instruksinya.

   > Psst, di dalam `bash`, kamu bisa lihat-lihat proyek Django kamu seperti
   > dari cmd/terminal, lho! Artinya, kamu juga bisa memanggil perintah lain
   > seperti `python manage.py migrate` atau bahkan perintah-perintah Linux
   > *shell*.

2. Unduh `chromedriver` (atau *webdriver* lain yang kamu inginkan) untuk
   komputer kamu agar bisa menjalankan *functional test* secara lokal.
   **Ini akan sangat bermanfaat untuk salah satu *story*.**

   Di Windows:\
   Unduh [ChromeDriver][chromedriver] (`chromedriver_win32.zip`) untuk versi
   Chrome yang kamu gunakan. Lalu, ekstrak berkas `.zip` tersebut dan letakkan
   `chromedriver.exe` di direktori ini (setara dengan `manage.py`).

   Di Linux:\
   Beberapa distribusi Linux memiliki *package* khusus untuk ChromeDriver, atau
   sebagian juga sudah menyertakannya di dalam *package* `chromium` (misal:
   Arch Linux). Jika tidak ada *package* yang sesuai, kamu bisa unduh
   `chromedriver_linux64.zip` melalui pranala di atas, lalu `unzip` dan
   letakkan `chromedriver` ke salah satu direktori yang ada di `$PATH`.

   Di macOS:\
   Instal `chromedriver` dengan [Homebrew][homebrew]
   (`brew cask install chromedriver` di Terminal). Silakan instal Homebrew
   terlebih dahulu jika belum. Saya tidak punya perangkat dengan macOS, jadi
   silakan cari solusinya apabila ada kendala yang muncul ;)

   Untuk menjalankan *functional test* saja, gunakan perintah berikut:

   ```shell
   python manage.py test --tag=functional
   ```

   > Catatan: jika ingin menggunakan *webdriver* lain, silakan sesuaikan berkas
   > `tests.py` kamu serta lakukan instalasi untuk *webdriver* tersebut.
   > Jika ingin melihat proses *functional test* di komputer kamu, nonaktifkan
   > opsi `headless` pada `tests.py`. Namun, jangan lupa untuk mengaktifkannya
   > kembali karena opsi tersebut dibutuhkan oleh GitLab CI/GitHub Actions.
   > Pastikan kamu sudah menjalankan perintah `collectstatic` sebelum
   > menjalankan *functional test*.

   > Catatan khusus pengguna Windows: ketika kamu menjalankan
   > *functional test*, mungkin akan muncul *error* seperti
   > `ConnectionResetError: [WinError 10054] An existing connection was forcibly
   > closed by the remote host`. Selama tes tetap berjalan sampai selesai,
   > abaikan saja masalah tersebut. Ini memang [*bug*][ticket-21227] yang belum
   > diperbaiki untuk Django di Windows.

3. Atur konfigurasi *code coverage* di GitLab.

   *Code coverage* merupakan salah satu metrik yang berguna untuk mengukur
   sudah seberapa banyak kode kamu yang teruji. GitLab punya fitur untuk
   menangkap *code coverage* dari *output* sebuah *job* di **Pipelines**. Untuk
   mengaturnya, silakan buka **Settings > CI/CD > General pipelines**. Pada
   bagian **Test coverage parsing**, isikan ekspresi reguler berikut:
   `^TOTAL.*\s+(\d+\%)$` (kira-kira ini untuk apa ya?), lalu simpan.

   Nantinya, pada bagian **Coverage report** akan muncul *badge* yang
   menunjukkan *coverage* proyek kamu. *Badge* ini bisa kamu masukkan ke dalam
   `README.md` seperti yang ada pada berkas ini.

   Untuk menjalankan tes dengan pengukuran *coverage* pada komputer lokal kamu,
   gunakan perintah berikut.

   ```shell
   coverage run --include="./*" --omit="venv/*,manage.py,project_name/*" manage.py test
   ```

   > Catatan: Perintah ini akan menjalan *unit test* dan *functional test*
   > sekaligus, jadi pastikan kamu sudah menjalankan perintah `collectstatic`
   > sebelum menjalankan tes.

## Tips pengembangan

1. Mulai sekarang, **biasakan** untuk me-*reload* *browser* kamu dengan
   <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd> (beberapa *browser* juga bisa
   dengan <kbd>Shift</kbd>+<kbd>F5</kbd>), bukan hanya
   <kbd>Ctrl</kbd>+<kbd>R</kbd> atau <kbd>F5</kbd>. Jika tidak, ketika kamu
   mengembangkan web secara lokal, kamu mungkin akan sering menemukan kasus di
   mana berkas *static* yang muncul di *browser* tidak berubah setelah kamu
   memodifikasinya. Ini terjadi karena *browser* membuat *cache* dari berkas
   *static* kamu supaya dapat diakses lebih cepat. Dengan menekan tombol
   <kbd>Shift</kbd>, *browser* akan [mem-*bypass* berkas *static* yang sudah
   di-*cache*][bypass-cache].
2. Biasakan untuk menulis tes yang berkualitas untuk proyek web kamu, terutama
   untuk logika-logika seperti yang ada pada bagian *views*. Membuat tes akan
   memudahkan kamu untuk menemukan *bug* pada program kamu lebih awal. Selain
   itu, tes juga dapat mencegah kamu menciptakan *bug* baru ketika
   mengembangkan proyek web kamu.
3. *Code coverage* 100% tidak menjamin proyek kamu bebas *bug*. Namun, memiliki
   tes yang menguji proyek kamu secara keseluruhan tentu akan sangat
   bermanfaat. Mulailah menulis tes setiap kali kamu membuat fungsionalitas
   baru agar *code coverage* tetap terjaga.
4. Templat ini sengaja tidak menyertakan konfigurasi untuk *linting* seperti
   menggunakan [`flake8`][flake8] atau [`pylint`][pylint]. Hal ini untuk
   mencegah munculnya *warning* pada GitHub Actions atau GitLab CI jika kode
   kamu tidak sesuai aturan-aturan yang diterapkan *linter* tersebut. Jika kamu
   tidak ingin repot mengatur kode kamu supaya rapi, silakan coba
   [`black`][black] dan [`isort`][isort]. Akan sangat baik apabila kamu juga
   membuat konfigurasi untuk menjalankan *linter* tersebut di GitHub Actions
   atau GitLab CI untuk proyek yang kamu buat.

## Sihir macam apa ini?

Alat `django-admin` menyediakan opsi [`--template`][template] untuk perintah
`startproject` yang menerima alamat menuju berkas templat sebuah proyek Django.
Alamat tersebut dapat berupa lokasi berkas di komputer lokal atau URL untuk
mengunduh sebuah berkas arsip. GitLab/GitHub menyediakan opsi untuk mengunduh
repositori sebagai arsip `.zip`... sisanya silakan dipahami sendiri :)

Templat ini akan di-*render* dengan variabel-variabel yang bisa dikirimkan saat
menjalankan `startproject`. Cara kerjanya mirip dengan Django *templates* dan
*context variables* yang bisa dimasukkan ke dalamnya.

Mohon jadikan templat ini sebagai **sumber belajar sebanyak-banyaknya**.
Templat ini memang dapat memudahkan kamu untuk membuat proyek Django yang siap
di-*deploy* tanpa perlu melakukan banyak konfigurasi. Namun, akan sangat
bermanfaat bagi kamu apabila kamu memahami cara kerja konfigurasi yang ada di
templat ini.

## Berkontribusi

Apabila ingin berkontribusi ke templat ini, silakan buat *issue* atau kirim
*pull request* ke repositori untuk templat ini di [**GitHub**][repo-gh].
Repositori ini juga dicerminkan ke [GitLab][repo-gl] untuk keperluan
demonstrasi.

## Lisensi

Templat ini didistribusikan dengan lisensi [The Unlicense][license]. Proyek
yang dibuat dengan templat ini dipersilakan untuk didistribusikan dengan
ketentuan yang berbeda.

[actions-badge]: https://github.com/laymonage/django-template-heroku/workflows/Test%20and%20Deploy/badge.svg
[commits-gh]: https://github.com/laymonage/django-template-heroku/commits/master
[pipeline-badge]: https://gitlab.com/laymonage/django-template-heroku/badges/master/pipeline.svg
[coverage-badge]: https://gitlab.com/laymonage/django-template-heroku/badges/master/coverage.svg
[commits-gl]: https://gitlab.com/laymonage/django-template-heroku/-/commits/master
[readme-en]: README.en.md
[heroku-dashboard]: https://dashboard.heroku.com
[djecrety]: https://djecrety.ir
[account-settings]: https://dashboard.heroku.com/account
[chromedriver]: https://chromedriver.chromium.org/downloads
[homebrew]: https://brew.sh
[ticket-21227]: https://code.djangoproject.com/ticket/21227
[bypass-cache]: https://en.wikipedia.org/wiki/Wikipedia:Bypass_your_cache
[flake8]: https://pypi.org/project/flake8
[pylint]: https://pypi.org/project/pylint
[black]: https://pypi.org/project/black
[isort]: https://pypi.org/project/isort
[template]: https://docs.djangoproject.com/en/{{ docs_version }}/ref/django-admin/#cmdoption-startproject-template
[repo-gh]: https://github.com/laymonage/django-template-heroku
[repo-gl]: https://gitlab.com/laymonage/django-template-heroku
[license]: LICENSE
