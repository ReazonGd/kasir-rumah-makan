## ✅ Checklist Penilaian Tugas UAS OOP (Python – Aplikasi Restoran) - COMPLETED ITEMS

- [x] Menggunakan bahasa pemrograman Python
  - `main.py:1-2` (Python file dengan header)
- [x] Program dapat dijalankan tanpa error fatal
  - `main.py:13-28` (try/except/finally dengan KeyboardInterrupt handling)

### Konsep OOP
- [x] Menggunakan **kelas abstrak** (`MenuItem`)
  - `menu.py:2` (import ABC), `menu.py:10` (class MenuItem(ABC)), `menu.py:38-39` (@abstractmethod tampilMenu)
- [x] Mengimplementasikan **inheritance** dengan benar
  - `menu.py:42` (class Makanan(MenuItem)), `menu.py:94` (class Minuman(MenuItem)), `menu.py:145` (class Discout(MenuItem))
- [x] Mengimplementasikan **polymorphism** (`tampilMenu()` berbeda tiap kelas)
  - `menu.py:46-92` (Makanan.tampilMenu), `menu.py:97-143` (Minuman.tampilMenu), `menu.py:171-220` (Discout.tampilMenu)
- [x] Mengimplementasikan **encapsulation** (atribut private + getter/setter)
  - `menu.py:12-14` (private attributes: __name, __price, __jenis), `menu.py:18-25` (getters: get_name, get_price, get_jenis), `menu.py:30-32` (setter: update method)

### Struktur Kelas
- [x] Kelas `MenuItem` memiliki atribut nama, harga, kategori
  - `menu.py:11-14` (__init__ dengan name, price, jenis)
- [x] Kelas `Makanan` sebagai turunan `MenuItem`
  - `menu.py:42-44` (class definition dan __init__)
- [x] Kelas `Minuman` sebagai turunan `MenuItem`
  - `menu.py:94-96` (class definition dan __init__)
- [x] Kelas `Diskon` sebagai turunan `MenuItem`
  - `menu.py:145-149` (class definition dan __init__)
- [x] Kelas `Menu` untuk menyimpan daftar menu
  - `util/storage.py:4-10` (class Menu dengan add_menu method)
- [x] Kelas `Pesanan` untuk menyimpan pesanan pelanggan
  - `util/storage.py:59-64` (class Pesanan dengan add_to_keranjang method)

### Diskon
- [x] Diskon direpresentasikan sebagai **objek**
  - `menu.py:145-168` (class Discout dengan methods calculate, is_accepteble)
- [x] Diskon dapat dipilih oleh pelanggan
  - `pages/order_calculator.py:46-63` (select_discount method dengan ListOfChoice)
- [x] Diskon diterapkan pada perhitungan total
  - `pages/order_calculator.py:13-33` (calculate_total method dengan discount parameter)
- [x] Hanya satu diskon per pesanan
  - `pages/order_calculator.py:13` (calculate_total menerima single discount parameter)
- [x] Diskon ditampilkan di struk
  - `pages/order_calculator.py:98-101` (display discount in struk)

### Fitur Program
- [x] Menu utama interaktif
  - `main.py:31-45` (main_display dengan ListOfChoice)
- [x] Menambah item menu (makanan, minuman, diskon)
  - `pages/manage_menu.py:49-76` (add_menu untuk makanan/minuman), `pages/manage_menu.py:30-47` (add_discount)
- [x] Menampilkan daftar menu restoran
  - `pages/pesan.py:58-82` (menus_display method), `util/storage.py:36-44` (get_menu_list, get_makanan_list, get_minuman_list)
- [x] Menerima pesanan pelanggan
  - `pages/pesan.py:14-33` (kasir_option dengan menu selection)
- [x] Menyimpan pesanan ke dalam keranjang
  - `util/storage.py:64-66` (add_to_keranjang), `pages/pesan.py:81` (add_to_keranjang call)
- [x] Menghitung total biaya pesanan
  - `pages/order_calculator.py:13-33` (calculate_total dengan subtotal, tax, service_fee, discount)
- [x] Menampilkan struk/receipt pesanan
  - `pages/order_calculator.py:64-121` (display_struk method)
- [x] Opsi keluar dari program
  - `main.py:44-45` (return when ans is None), `main.py:22-28` (KeyboardInterrupt handling)

### Struktur Program
- [x] Menggunakan struktur keputusan (`if / elif / else`)
  - `main.py:40-45` (if/elif/else untuk menu selection), `pages/pesan.py:22-33` (if/elif untuk kasir options)
- [x] Menggunakan struktur pengulangan (`while / for`)
  - `main.py:32` (while True), `pages/pesan.py:15` (while True), `pages/order_calculator.py:36` (while True), `pages/order_calculator.py:88` (for loop)
- [x] Menggunakan list/array
  - `util/storage.py:6` (self.__menu: list[MenuItem]), `util/storage.py:61` (self.__keranjang__: list[tuple])
- [x] Mengolah data string dengan benar
  - `pages/pesan.py:41` (f-string formatting), `pages/pesan.py:59` (string formatting), `pages/order_calculator.py:90` (f-string)

### Exception Handling
- [x] Menangani input tidak valid
  - `util/user_input.py:85-94` (input_int dengan try/except), `util/user_input.py:96-105` (input_float dengan try/except)
- [x] Menangani menu yang tidak ditemukan
  - `util/storage.py:46-50` (get_menu_by_name returns None), `pages/pesan.py:74` (get_menu_detail)
- [x] Menangani pesanan kosong
  - `pages/pesan.py:36-39` (check if keranjang kosong), `pages/order_calculator.py:65-67` (check keranjang_size == 0)
- [x] Program tidak langsung crash saat error
  - `main.py:13-28` (try/except/finally), `pages/order_calculator.py:37-44` (try/except ValueError)

### Kelengkapan Pengumpulan
- [ ] Source code dikumpulkan dalam format PDF
- [ ] Video penjelasan tersedia
- [ ] Durasi video maksimal 15 menit
- [ ] Video menampilkan layar dan wajah
- [ ] Link video dapat diakses publik

---

## Summary

**Total Completed: 33/38 items (86.8%)**

**Completed Categories:**
- ✅ Dasar Program (2/2)
- ✅ Konsep OOP (4/4)
- ✅ Struktur Kelas (6/6)
- ✅ Diskon (5/5)
- ✅ Fitur Program (8/8)
- ✅ Struktur Program (4/4)
- ✅ Exception Handling (4/4)
- ⏳ Kelengkapan Pengumpulan (0/5)

**Remaining Tasks:**
- Source code PDF export
- Video penjelasan (dengan layar dan wajah, maksimal 15 menit, link publik)

