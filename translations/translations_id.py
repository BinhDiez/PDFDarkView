
# ============================================
# translations_id.py - Kamus Bahasa Indonesia
# Vollständig sortiert nach Kategorien
# ============================================

def load_indonesian_strings():
    """Lädt alle indonesischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View oleh BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Buka PDF",
        'btn_text_window': "Teks OCR",
        'btn_first': "Halaman Pertama",
        'btn_prev': "Halaman Sebelumnya",
        'btn_next': "Halaman Berikutnya",
        'btn_last': "Halaman Terakhir",
        'btn_print': "Cetak",
        'btn_darkmode_light': "Mode Terang",
        'btn_darkmode_dark': "Mode Gelap",
        'btn_delete_pages': "Hapus Halaman",
        'btn_extract_pages': "Ekstrak Halaman",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Batal",
        'btn_save': "Simpan",
        'btn_close': "Tutup",
        'btn_delete': "Hapus",
        'btn_delete_all': "Hapus Semua",
        'btn_copy': "Salin",
        'btn_export': "Ekspor",
        'btn_show': "Tampilkan Kata Sandi",
        'btn_hide': "Sembunyikan Kata Sandi",
        'btn_authenticate': "Autentikasi",
        'btn_settings': "Pengaturan",
        'btn_protect': "Lindungi",
        'btn_remove_password': "Hapus Kata Sandi",
        'btn_manage': "Kelola Kata Sandi",
        'btn_retry': "Coba Lagi",
        'btn_select_all': "Pilih Semua",
        'btn_clear_selection': "Hapus Pilihan",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Halaman {0} dari {1}",
        'page_count': "dari {0}",
        'goto_page': "Pergi ke Halaman",
        'page_simple': "Halaman {0}",
        'full_view_page': "Tampilan Penuh Halaman {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Masukkan kata kunci + Enter",
        'search_results': "Hasil: {0} dari {1}",
        'search_nav_hint': "Enter: berikutnya (Shift+Enter: sebelumnya)",
        'search_no_results': "Tidak ada hasil",
        'search_error': "Kesalahan pencarian",
        'search_active': "Bidang pencarian diaktifkan",
        'search_closed': "Pencarian selesai",
        'search_position': "Halaman {0} {1}",
        'search_pos_top': "paling atas",
        'search_pos_upper': "atas",
        'search_pos_middle': "tengah",
        'search_pos_lower': "bawah",
        'search_pos_bottom': "paling bawah",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Pengenalan teks berhasil!",
        'ocr_success_title': "OCR Berhasil",
        'ocr_success_message': "Dokumen sekarang dapat dicari.",
        'ocr_failed': "OCR Gagal",
        'ocr_in_progress': "OCR Sedang Berlangsung",
        'ocr_preparing': "Mempersiapkan PDF...",
        'ocr_analyzing': "Menganalisis PDF...",
        'ocr_optimizing': "Optimasi gambar...",
        'ocr_recognizing': "Mengenali teks...",
        'ocr_embedding': "Menyisipkan teks...",
        'ocr_finalizing': "Menyelesaikan PDF...",
        'ocr_not_available': "OCR tidak tersedia",
        'ocr_install_message': "Alat OCR tidak ditemukan.\n\nSilakan instal:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR diperlukan",
        'ocr_question': "PDF tidak mengandung teks yang dapat dicari.\nApakah Anda ingin melakukan OCR untuk mengaktifkan {0}?",
        'ocr_perform': "Lakukan OCR",
        'ocr_later': "Nanti",
        'ocr_starting': "Memulai OCR terjamin...",
        'ocr_success_voice': "OCR berhasil. PDF sekarang dapat dicari.",
        'ocr_partial_success': "OCR telah dilakukan, tetapi ada masalah saat mengganti.\n\nVersi yang dapat dicari disimpan di:\n{0}\n\nKesalahan: {1}",
        'ocr_partial_title': "OCR Sebagian Berhasil",
        'ocr_partial_voice': "OCR dilakukan, tetapi penggantian gagal.",
        'original_file': "File asli:",
        'old_size': "Ukuran lama:    {0} byte",
        'new_size': "Ukuran baru: {0} byte",
        'size_change': "Perubahan: {0}{1} byte",
        'backup_created_file': "Cadangan dibuat:\n{0}",
        'backup_not_created': "Cadangan tidak dibuat (pengaturan dimatikan)",
        'page_header': "=== Halaman {0} ===\n{1}\n",
        'scanned_page_header': "=== Halaman {0} (pindaian) ===\n[Halaman ini hanya berisi teks pindaian]\n[Silakan lakukan OCR manual]\n",
        'scanned_warning': "⚠️ TEKS PINDAIAN - OCR DIPERLUKAN",
        'guaranteed_title': "PDF yang Dapat Dicari Dibuat",
        'guaranteed_message': "<b>Versi terjamin yang dapat dicari dibuat!</b>\n\nKarena OCR otomatis gagal, PDF alternatif yang dapat dicari telah dibuat:\n\n{0}\n\n<b>File ini berisi:</b>\n• Teks yang diekstrak (jika ada)\n• Petunjuk untuk halaman pindaian\n• Sepenuhnya dapat dicari",
        'guaranteed_voice': "PDF terjamin yang dapat dicari dibuat.",
        'instruction_title': "PETUNJUK OCR",
        'instruction_file': "File asli: {0}",
        'instruction_text': "Pengenalan teks otomatis (OCR) gagal.\nSilakan lakukan OCR manual:\n\n1. DENGAN OCRmyPDF (baris perintah):\n   ocrmypdf --force-ocr \"[FILE]\" \"keluaran.pdf\"\n\n2. DENGAN ADOBE ACROBAT (macOS/Windows):\n   • Buka PDF di Acrobat\n   • Alat > Edit PDF\n   • Pilih 'Pengenalan Teks'\n\n3. DENGAN PREVIEW (macOS):\n   • Buka PDF di Preview\n   • File > Ekspor...\n   • Filter Quartz: 'Kurangi Ukuran File'\n   • Aktifkan 'Lakukan OCR'\n\n4. LAYANAN OCR ONLINE:\n   • smallpdf.com/id/ocr-pdf\n   • ilovepdf.com/id/ocr-pdf\n   • adobe.com/id/acrobat/online/pdf-to-word.html",
        'instruction_created': "Petunjuk OCR dibuat",
        'instruction_created_message': "Petunjuk terperinci telah dibuat:\n\n{0}\n\nIkuti langkah-langkah untuk OCR manual.",
        'instruction_created_voice': "Petunjuk OCR dibuat.",
        'ocr_impossible': "OCR tidak memungkinkan",
        'ocr_impossible_message': "Tidak dapat melakukan OCR.\n\nProses '{0}' secara manual dengan perangkat lunak OCR.",
        'ocr_impossible_voice': "OCR tidak memungkinkan. Silakan proses manual.",
        'emergency_title': "OCR Darurat",
        'emergency_message': "PDF darurat telah dibuat:\n\n{0}\n\nSilakan proses file ini secara manual dengan OCR.",
        'emergency_voice': "PDF darurat dibuat. Silakan lakukan OCR manual.",
        'critical_error': "Kesalahan Kritis",
        'critical_error_message': "Tidak dapat memulai OCR.\n\nMulai ulang program dan periksa instalasi OCR.",
        'critical_error_voice': "Kesalahan Kritis OCR",
        'ocr_question_html': "<p>PDF tidak mengandung teks yang dapat dicari.<p>Apakah Anda ingin melakukan OCR untuk mengaktifkan <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR diperlukan. PDF tidak mengandung teks yang dapat dicari. Apakah Anda ingin melakukan OCR untuk mengaktifkan {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "tidak ada PDF dimuat",
        'no_pdf_message': "Tidak ada PDF yang dimuat",
        'pdf_not_found': "File PDF tidak ditemukan",
        'file_size': "Ukuran File",
        'bytes': "byte",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Cadangan dibuat",
        'backup_disabled': "Cadangan dimatikan",
        'backup_activated': "Pembuatan cadangan diaktifkan",
        'backup_deactivated': "Pembuatan cadangan dimatikan",
        'backup_status': "Cadangan: {0}",
        'backup_on': "✔ aktif",
        'backup_off': "✘ nonaktif",
        'close_pdf': "Menutup PDF: {0}",
        'pdf_not_found_format': "File PDF tidak ditemukan: {0}",
        'error_pdf_load_format': "Kesalahan saat memuat PDF: {0}",
        'load_failed_format': "Pemuatan gagal:\n{0}",
        'decrypted_suffix': "(didekripsi)",
        'decryption_failed': "Dekripsi gagal.",
        'decryption_error': "Kesalahan saat mendekripsi",
        'decryption_success': "Berhasil didekripsi",
        'decryption_success_message': "PDF telah didekripsi dan disimpan di:\n\n{0}",
        'decryption_success_voice': "PDF telah didekripsi dan disimpan.",
        'password_remove_error': "Kesalahan saat menghapus kata sandi",
        'save_unencrypted': "Simpan PDF tidak terenkripsi sebagai",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Simpan Sebagai...",
        'save_copy': "Simpan Salinan",
        'save_success': "PDF disimpan di: {0}",
        'save_encrypted': "PDF terlindung disimpan di: {0}",
        'save_error': "PDF tidak dapat disimpan",
        'encryption_question': "Apakah Anda ingin melindungi PDF dengan kata sandi?",
        'encryption_yes': "Ya",
        'encryption_no': "Tidak",
        'encryption_cancel': "Batal",
        'save_cancel': "Penyimpanan dibatalkan",
        'save_encrypted_voice': "File dienkripsi dan disimpan.",
        'save_success_voice': "File PDF disimpan tanpa enkripsi.",
        'save_error_format': "PDF tidak dapat disimpan:\n{0}",
        'export_pages_success': "Ekspor ke Pages berhasil",
        'export_pages_error': "Ekspor ke Pages gagal",
        'export_pages_error_format': "Ekspor ke Pages gagal: {0}",
        'export_word_success': "Ekspor ke Word berhasil",
        'export_word_error': "Ekspor ke Word gagal",
        'export_word_error_format': "Ekspor ke Word gagal: {0}",
        'export_text_success': "Ekspor teks berhasil",
        'export_text_error': "Ekspor teks gagal",
        'export_text_error_format': "Ekspor teks gagal: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Kata sandi diperlukan",
        'password_enter': "Silakan masukkan kata sandi",
        'password_confirm': "Konfirmasi kata sandi",
        'password_new': "Kata sandi baru",
        'password_current': "Kata sandi saat ini",
        'password_save': "Simpan kata sandi (dienkripsi)",
        'password_saved': "✓ Kata sandi untuk file ini disimpan",
        'password_wrong': "Kata sandi salah",
        'password_mismatch': "Kata sandi tidak cocok",
        'password_too_short': "Kata sandi terlalu pendek",
        'password_min_length': "Kata sandi harus minimal 4 karakter",
        'password_strength': "Kekuatan Kata Sandi",
        'password_strength_very_weak': "Sangat lemah",
        'password_strength_weak': "Lemah",
        'password_strength_medium': "Sedang",
        'password_strength_strong': "Kuat",
        'password_strength_very_strong': "Sangat kuat",
        'password_char_count': "({0} karakter)",
        'password_match': "✓ Cocok",
        'password_no_match': "✗ Kata sandi tidak cocok",
        'password_show': "Tampilkan",
        'password_hide': "Sembunyikan",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Kelola Kata Sandi",
        'password_table_filename': "Nama File",
        'password_table_password': "Kata Sandi",
        'password_count': "{0} kata sandi disimpan",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Tidak ada kata sandi disimpan",
        'password_copied': "{0} kata sandi disalin",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Apakah Anda yakin ingin menghapus kata sandi untuk '{0}'?",
        'password_delete_multiple': "Apakah Anda yakin ingin menghapus {0} kata sandi yang dipilih?",
        'password_delete_all_confirm': "Apakah Anda yakin ingin menghapus semua {0} kata sandi yang disimpan?",
        'password_deleted': "{0} kata sandi dihapus",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Semua kata sandi telah dihapus",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generator Kata Sandi",
        'generator_generated': "Kata sandi yang dihasilkan:",
        'generator_regenerate': "Hasilkan Ulang",
        'generator_copy': "Salin",
        'generator_use': "Gunakan",
        'generator_settings': "Pengaturan",
        'generator_length': "Panjang:",
        'generator_group_every': "Pemisah setiap",
        'generator_group_chars': "karakter.    Pemisah:",
        'generator_uppercase': "Huruf besar (A-Z)",
        'generator_lowercase': "Huruf kecil (a-z)",
        'generator_digits': "Angka (0-9)",
        'generator_symbols': "Simbol (!@#$%^&*)",
        'generator_exclude': "Dikecualikan:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Kata sandi utama diperlukan",
        'master_password_setup': "Atur Kata Sandi Utama",
        'master_password_change': "Ubah Kata Sandi Utama",
        'master_password_enter': "Silakan masukkan kata sandi utama Anda",
        'master_password_choose': "Pilih kata sandi utama yang kuat (minimal 8 karakter)",
        'master_password_new': "Silakan masukkan kata sandi utama baru Anda",
        'master_password_confirm': "Konfirmasi kata sandi",
        'master_password_authenticate': "Autentikasi",
        'master_password_success': "Kata sandi utama berhasil diatur.",
        'master_password_changed': "Kata sandi utama berhasil diubah.",
        'master_password_removed': "Kata sandi utama dan semua kata sandi telah dihapus.",
        'master_password_remove': "Hapus Kata Sandi Utama",
        'master_password_remove_confirm': "Apakah Anda YAKIN ingin menghapus SEMUA kata sandi?\n\nTindakan ini TIDAK DAPAT DIBATALKAN!",
        'master_password_export_before': "Apakah Anda ingin mengekspor cadangan sebelumnya?",
        'master_password_export_delete': "Ekspor & Hapus",
        'master_password_delete_now': "Hapus Sekarang",
        'master_password_for_signatures': "Untuk dapat menggunakan tanda tangan, Anda harus mengatur kata sandi utama.\n\nApakah Anda ingin mengatur kata sandi utama sekarang?",
        'master_password_for_private': "Untuk dapat menggunakan blok teks pribadi, Anda harus mengatur kata sandi utama.\n\nApakah Anda ingin mengatur kata sandi utama sekarang?",
        'master_password_info': """
            <b>🔐 TANPA KATA SANDI UTAMA:</b><br>
            • Tidak dapat menampilkan, menyalin, dan mengekspor kata sandi<br>
            • Penghapusan kata sandi selalu dimungkinkan (bahkan tanpa kata sandi utama)<br><br>

            <b>🔐 DENGAN KATA SANDI UTAMA:</b><br>
            • Semua fungsi tersedia setelah autentikasi<br>
            • Kata sandi dienkripsi dengan kata sandi utama<br>
            • Panjang minimal: 8 karakter<br>
            • Penyimpanan hash SHA-256 yang aman<br><br>

            <b>PENTING:</b><br>
            • Jika kehilangan kata sandi utama, kata sandi tidak dapat dipulihkan<br>
            • Saat menghapus kata sandi utama, SEMUA kata sandi akan dihapus<br>
            • Opsi ekspor tersedia sebelum penghapusan<br>
            • Kata sandi utama dapat diubah kapan saja
        """,
        'signature_auth_disabled': "Nonaktifkan permintaan kata sandi untuk tanda tangan",
        'template_auth_disabled': "Nonaktifkan permintaan kata sandi untuk blok teks pribadi",
        'master_password_for_signatures_settings': "Untuk dapat menggunakan tanda tangan, Anda harus mengatur kata sandi utama.\n\nPergi ke Pengaturan - Kelola Kata Sandi",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Lindungi PDF",
        'protect_info': "File '{0}' akan dilindungi dengan kata sandi.",
        'protect_instruction': "Silakan masukkan kata sandi yang diinginkan dua kali untuk melindungi dokumen, atau gunakan generator kata sandi di sebelah kanan bidang input.",
        'protect_success': "PDF berhasil dilindungi dan disimpan di:\n{0}\n\nKata sandi: {1}\n\nApakah Anda ingin membuka PDF yang dilindungi sekarang?",
        'protect_open': "Ya",
        'protect_skip': "Tidak",
        'protect_error': "Kesalahan saat melindungi PDF",
        'protect_open_title': "buka PDF yang dilindungi",
        'protect_question': "Selesai. Apakah Anda ingin membuka PDF yang dilindungi sekarang? Ya atau Tidak?",
        'password_cancel': "Dialog kata sandi dibatalkan",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Hapus Halaman",
        'pages_extract': "Ekstrak Halaman",
        'pages_insert': "Sisipkan Halaman",
        'pages_move': "Pindahkan Halaman",
        'pages_delete_options': "Opsi Hapus",
        'pages_delete_empty': "Hapus semua halaman kosong",
        'pages_delete_current': "Hapus halaman saat ini",
        'pages_delete_range': "Hapus rentang halaman",
        'pages_extract_options': "Opsi Ekstrak",
        'pages_extract_current': "Ekstrak halaman saat ini",
        'pages_extract_range': "Ekstrak rentang halaman",
        'pages_insert_position': "Posisi Sisip",
        'pages_insert_before': "Sisipkan sebelum halaman:",
        'pages_insert_select': "Pilih PDF",
        'pages_insert_none': "Tidak ada PDF dipilih",
        'pages_move_source': "Halaman yang akan dipindahkan",
        'pages_move_from': "Dari halaman:",
        'pages_move_to': "Sampai halaman:",
        'pages_move_target': "Posisi Tujuan",
        'pages_move_before': "Pindahkan sebelum halaman:",
        'pages_move_hint': "Catatan: halaman 1 = awal, {0} = akhir",
        'pages_range_invalid': "Halaman awal harus lebih kecil atau sama dengan halaman akhir.",
        'pages_position_invalid': "Posisi tujuan tidak boleh berada dalam rentang yang dipindahkan.",
        'pages_no_pdf_selected': "Tidak ada PDF yang dipilih.",
        'pages_deleted': "{0} halaman telah dihapus.",
        'pages_extracted': "Diekstrak: {0}\nDisimpan di: {1}\nUkuran file: {2:.1f} KB",
        'pages_inserted': "{0} halaman disisipkan",
        'pages_moved': "{0} halaman telah dipindahkan.",
        'pages_deleted_none': "Tidak ada halaman yang dihapus.",
        'pages_delete_progress': "Menghapus halaman...",
        'pages_deleted_with_backup': "{0} halaman telah dihapus.\n\nCadangan: {1}",
        'pages_deleted_voice': "Cadangan dibuat dan {0} halaman dihapus.",
        'info': "Informasi",
        'error_dialog_creation': "Dialog tidak dapat dibuat",
        'extract_page_single': "Ekstrak halaman {0}",
        'extract_page_range': "Ekstrak halaman {0}-{1}",
        'extract_success_voice': "Halaman berhasil diekstrak",
        'extract_error_format': "Kesalahan saat mengekstrak: {0}",
        'pages_inserted_voice': "{0} halaman disisipkan.",
        'insert_error_format': "Kesalahan saat menyisipkan: {0}",
        'pages_move_progress': "Memindahkan halaman...",
        'pages_moved_with_backup': "{0} halaman telah dipindahkan.\n\nCadangan: {1}",
        'move_success_title': "Berhasil Dipindahkan",
        'pages_moved_voice': "{0} halaman berhasil dipindahkan",
        'mark_removed': "Tanda halaman {0} dihapus",
        'mark_empty': "Halaman {0} ditandai kosong",
        'mark_export_removed': "Tanda ekspor halaman {0} dihapus",
        'mark_export': "Halaman {0} ditandai untuk ekspor",
        'no_empty_pages': "Tidak ada halaman kosong yang ditandai untuk dihapus",
        'delete_empty_confirm': "Apakah Anda ingin menghapus semua {0} halaman kosong yang ditandai?",
        'delete_empty_confirm_voice': "Hapus sekarang semua {0} halaman kosong yang ditandai? Ya atau Tidak.",
        'empty_pages_deleted': "{0} halaman kosong dihapus",
        'no_export_pages': "Tidak ada halaman yang ditandai untuk ekspor",
        'overwrite_title': "Timpa File yang Ada",
        'overwrite_question': "File\n\n{0}\n\nsudah ada.\nApakah Anda ingin menimpanya?",
        'overwrite_voice': "Timpa file yang ada? Ya atau Tidak.",
        'page_skipped': "Halaman {0} dilewati",
        'export_complete': "Ekspor selesai.",
        'export_complete_voice': "Ekspor selesai.",
        'no_pages_exported': "Tidak ada halaman yang diekspor",
        'export_cancelled': "Ekspor dibatalkan",
        'pages_exported': "{0} halaman diekspor ke {1}",
        'export_page_title': "Ekspor Halaman",
        'page_exported': "Halaman {0} diekspor ke {1}",
        'export_error': "Kesalahan saat ekspor",
        'export_marked_title': "Ekspor Halaman yang Ditandai",
        'rotate_all_title': "putar semua halaman",
        'rotate_all_question': "Apakah Anda ingin memutar semua halaman 90 derajat ke kanan?",
        'rotate_all_voice': "Apakah Anda ingin memutar semua halaman 90 derajat ke kanan? Ya atau Tidak?",
        'all_pages_rotated': "Semua halaman diputar",
        'page_rotated': "Halaman {0} diputar",
        'rotate_error': "Halaman tidak dapat diputar",
        'delete_page_confirm': "Apakah Anda ingin menghapus halaman {0}?",
        'delete_page_confirm_voice': "Apakah Anda yakin ingin menghapus halaman {0}? Ya atau Tidak.",
        'page_deleted': "Halaman {0} dihapus",
        'delete_error': "Halaman tidak dapat dihapus",
        'pages_deleted_voice': "{0} halaman dihapus",
        'pages_exported_split': "{0} halaman berhasil diekspor.",
        'pages_skipped': "{0} halaman dilewati.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Ekstrak Halaman (Lanjutan)",
        'pdf_splitter_title': "Pemisah & Ekstraktor PDF",
        'pdf_splitter_load': " Pilih File PDF",
        'pdf_splitter_info': "Silakan pilih opsi untuk dokumen PDF Anda",
        'pdf_splitter_basic': "Operasi Dasar",
        'pdf_splitter_single': "Bagi menjadi halaman individual",
        'pdf_splitter_range': "Ekstrak halaman:",
        'pdf_splitter_range_placeholder': "mis. 1-3,5,7-9",
        'pdf_splitter_clean': "Operasi Pembersihan",
        'pdf_splitter_remove_empty': "Hapus semua halaman kosong",
        'pdf_splitter_remove': "Hapus rentang halaman:",
        'pdf_splitter_remove_placeholder': "mis. 2,4-6",
        'pdf_splitter_process': "Proses PDF",
        'pdf_splitter_loaded': "PDF dimuat. Silakan pilih opsi",
        'pdf_read_error': "PDF tidak dapat dibaca",
        'pages': "Halaman",
        'pages_created': "Halaman dibuat",
        'range_empty': "Silakan masukkan rentang halaman",
        'range_invalid': "Rentang halaman tidak valid",
        'range_created': "PDF baru dengan halaman yang dipilih telah dibuat:\n{0}",
        'empty_removed': "{0} halaman kosong dihapus.\nKeluaran: {1}",
        'remove_empty': "Silakan masukkan halaman yang akan dihapus",
        'remove_invalid': "Halaman yang akan dihapus tidak valid",
        'remove_done': "PDF bersih dibuat:\n{0}",
        'open_folder': "Buka Folder",
        'show_in_finder': "Tampilkan di Finder",
        'pdf_splitter_no_pdf': "Silakan muat file PDF terlebih dahulu.",
        'process_error': "Kesalahan saat memproses PDF",
        'pages_created_voice': "{0} halaman dibuat",
        'range_created_voice': "PDF dengan halaman yang dipilih dibuat",
        'empty_removed_voice': "{0} halaman kosong dihapus",
        'remove_done_voice': "PDF bersih dibuat",
        'pdf_splitter_split_groups': "Setiap grup berurutan ke file terpisah",
        'range_created_single': "PDF baru dibuat:\n{0}",
        'range_created_multiple': "{0} file PDF dibuat.",
        'range_created_voice_single': "Satu PDF dengan halaman yang dipilih dibuat",
        'range_created_voice_multiple': "{0} file PDF dibuat",
        'empty_removed_none_left': "Tidak ada halaman tersisa",
        'empty_removed_all_empty': "Semua halaman dikenali sebagai kosong dan akan dihapus. Tidak ada file yang dibuat.",
        'preview_single': "Pratinjau: {0}",
        'preview_enter_range': "Silakan masukkan rentang halaman.",
        'preview_invalid_range': "Rentang halaman tidak valid.",
        'preview_file': "Pratinjau: {0}",
        'preview_files': "Pratinjau: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Memulai pencetakan",
        'print_sent': "Tugas cetak dikirim",
        'print_now': "Cetak Sekarang",
        'print_error': "Kesalahan saat mencetak langsung",
        'print_limited': "Fungsi cetak terbatas pada sistem ini",
        'print_error_format': "Kesalahan saat mencetak langsung: {0}",
        'warning': "Peringatan",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Beralih ke Mode Terang",
        'mode_switch_to_dark': "Beralih ke Mode Gelap",
        'mode_dark_activated': "Mode Gelap diaktifkan",
        'mode_light_activated': "Mode Terang diaktifkan",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Tampilan Penuh",
        'zoom_two_pages': "Dua Halaman Berdampingan",
        'zoom_overview': "Mode Ikhtisar",
        'zoom_cannot_during_search': "Pembesaran tidak dapat dilakukan selama pencarian",
        'zoom_exit_first': "Silakan keluar dari pembesaran terlebih dahulu",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Seret dan Lepas diaktifkan",
        'drag_disabled': "Seret dan Lepas dimatikan",
        'drag_page_grab': "Halaman {0} diambil",
        'drag_page_dropped': "Halaman {0} disisipkan di posisi {1}",
        'drag_position_invalid': "Posisi tidak valid",
        'drag_same_position': "Halaman {0} tetap di posisi {0}",
        'drag_error': "Kesalahan saat memindahkan",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Input Teks dengan Pemformatan Lanjutan dan Manajemen Blok Teks",
        'text_templates': "Blok Teks Tersedia:",
        'text_name': "Nama",
        'text_preview': "Pratinjau Teks",
        'text_enter': "Teks:",
        'text_font_size': "Ukuran Huruf:",
        'text_formatting': "Pemformatan:",
        'text_bold': "Tebal",
        'text_italic': "Miring",
        'text_underline': "Garis Bawah",
        'text_alignment': "Perataan:",
        'text_left': "Kiri",
        'text_center': "Tengah",
        'text_right': "Kanan",
        'text_color': "Warna Teks:",
        'text_opacity': "Opacity:",
        'text_word_wrap': "Pembungkusan Kata:",
        'text_auto': "Otomatis",
        'text_page_width_95': "Lebar Halaman (95%)",
        'text_page_width_85': "Sangat Lebar (85%)",
        'text_page_width_75': "Lebar (75%)",
        'text_page_width_60': "Lebar (60%)",
        'text_page_width_50': "Sedang (50%)",
        'text_page_width_30': "Sempit (30%)",
        'text_page_width_20': "Lebih Sempit (20%)",
        'text_page_width_10': "Sangat Sempit (10%)",
        'text_no_wrap': "Tanpa Pembungkusan",
        'text_private': "Blok Teks Pribadi (memerlukan autentikasi)",
        'text_preview_label': "Pratinjau:",
        'text_preview_placeholder': "Pratinjau teks akan ditampilkan di sini...",
        'text_no_text': "(Tidak Ada Teks)",
        'text_save_template': "💾 Simpan sebagai Blok",
        'text_delete_template': "🗑 Hapus Blok Teks yang Dipilih",
        'text_show_private': "Tampilkan Pribadi",
        'text_hide_private': "Sembunyikan Pribadi",
        'text_use': "✅ Gunakan Teks",
        'text_saved': "Blok teks disimpan sebagai:\n{0}",
        'text_saved_voice': "Blok teks disimpan",
        'text_deleted': "Blok teks dihapus",
        'text_no_text_to_save': "Tidak ada teks untuk disimpan.",
        'text_no_templates': "Tidak ada blok teks ditemukan",
        'text_private_master_required': "Blok pribadi hanya dapat digunakan jika kata sandi utama telah diatur.\n\nApakah Anda ingin mengatur kata sandi utama sekarang?",
        'text_filename': "Nama file untuk blok teks (tanpa 'Text_' dan '.txt'):",
        'text_filename_hint': "Contoh: 'Telepon KantorRumah' akan disimpan sebagai 'Text_Telepon KantorRumah.txt'",
        'text_save_hint': "Blok teks akan disimpan secara otomatis dengan pemformatan.",
        'text_guide_title': "Input Teks – Panduan",
        'text_delete_confirm': "Apakah Anda yakin ingin menghapus blok teks?\n\nFile: {0}\nTeks: {1}...",
        'text_make_public': "Tandai sebagai Publik",
        'text_make_private': "Tandai sebagai Pribadi",
        'text_privacy_changed': "Status privasi diubah",
        'text_private_always': "Pribadi selalu terlihat (pengaturan)",
        'text_mode_required': "Silakan aktifkan mode teks terlebih dahulu",
        'text_continue_editing': "Lanjutkan mengedit – kursor di akhir teks",
        'text_no_input': "Tidak ada teks yang dimasukkan – teks dibuang",
        'save_dialog_question': "Bagaimana Anda ingin melanjutkan?",
        'text_save_question': "Simpan semua teks dan tanda silang, sesuaikan, lanjutkan mengedit, atau buang?",
        'copy_cross': "Tanda silang disalin",
        'paste_cross': "Tanda silang ditempel",
        'paste_text': "Teks ditempel",
        'cross_discarded': "Tanda silang dibuang",
        'all_discarded': "Semua dibuang",
        'text_discarded': "Teks dibuang",
        'no_texts_to_save': "Tidak ada teks untuk disimpan",
        'no_valid_texts': "Tidak ada teks yang valid untuk disimpan",
        'text_word_singular': "teks",
        'text_word_plural': "teks",
        'cross_word_singular': "tanda silang",
        'cross_word_plural': "tanda silang",
        'texts_saved_title': "Teks Disimpan",
        'texts_crosses_saved': "{0} {1} dan {2} {3} telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'texts_crosses_saved_voice': "{0} {1} dan {2} {3} disimpan.",
        'texts_saved': "{0} {1} telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'texts_saved_voice': "{0} {1} disimpan.",
        'crosses_saved': "{0} {1} telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'crosses_saved_voice': "{0} {1} disimpan.",
        'elements_saved': "{0} elemen telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'elements_saved_voice': "{0} elemen disimpan.",
        'text_window_load_error': "Jendela teks tidak dapat dimuat",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Input Teks dan Blok Teks – Panduan Rinci**

        **1. Menyisipkan dan Mengedit Teks**
        - Klik kanan pada tempat yang diinginkan di dokumen dan pilih "Sisipkan Teks".
        - Sebuah dialog akan terbuka di mana Anda dapat memasukkan dan memformat teks:
        • Ukuran huruf, tebal, miring, garis bawah
        • Warna teks (dapat dipilih)
        • Transparansi (opasitas) dengan penggeser
        • Pembungkusan kata (berbagai lebar, mis. lebar halaman, sempit, tanpa pembungkusan)
        - Setelah dikonfirmasi, teks akan muncul di lokasi klik. Anda dapat memindahkannya dengan mouse atau tombol panah.
        - Klik dua kali pada teks untuk membuka mode edit; ESC untuk keluar.

        **2. Mengelola Blok Teks (Template)**
        - Di sisi kiri dialog teks, Anda melihat daftar semua blok teks yang disimpan.
        - **Menyimpan Blok:** Masukkan teks, format, dan klik "💾 Simpan sebagai Blok". Beri nama file (tanpa ekstensi).
        - **Memuat Blok:** Klik nama yang diinginkan di daftar. Teks dan format akan diambil dan dapat disesuaikan jika perlu.
        - **Menghapus:** Klik kanan pada blok untuk menghapusnya atau mengubah status privasinya.

        **3. Blok Teks Pribadi (Kata Sandi Utama)**
        - Jika Anda telah mengatur kata sandi utama (di Pengaturan → Kelola Kata Sandi), Anda dapat menandai blok sebagai "pribadi".
        - Centang kotak "Blok Teks Pribadi" di dialog sebelum menyimpan.
        - Blok pribadi hanya ditampilkan dalam daftar jika Anda telah memasukkan kata sandi utama sekali per sesi (autentikasi melalui ikon gembok atau saat akses pertama).
        - Dengan cara ini Anda dapat melindungi blok teks rahasia dari akses tidak sah.

        **4. Menyisipkan Tanda Silang**
        - Dari menu konteks, Anda juga dapat menyisipkan tanda silang grafis (mis. untuk kotak centang).
        - Ukuran, ketebalan garis, dan warna tanda silang dapat disesuaikan secara global di pengaturan (menu "Pengaturan" → "Pengaturan Tanda Silang").
        - Klik kanan pada tanda silang yang ada untuk mengubahnya secara individual.

        **5. Tindakan Massal**
        - Jika Anda telah menempatkan beberapa teks atau tanda silang pada satu halaman, Anda dapat menyimpan atau membuang semuanya sekaligus dari menu konteks (klik kanan dalam mode teks).
        - Saat menyimpan, semua elemen akan disematkan ke PDF dan tetap sebagai grafik vektor.

        **6. Pintasan Keyboard dalam Mode Teks**
        - Tombol panah: memindahkan elemen
        - Ctrl+tombol panah: langkah lebih besar
        - Enter: membuka dialog simpan (simpan semua / sesuaikan / buang)
        - ESC: membuang elemen saat ini
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Input Teks dan Blok Teks – Panduan Rinci</strong></p>

        <p><strong>1. Menyisipkan dan Mengedit Teks</strong></p>
        <ul>
        <li>Klik kanan pada tempat yang diinginkan di dokumen dan pilih "Sisipkan Teks".</li>
        <li>Sebuah dialog akan terbuka di mana Anda dapat memasukkan dan memformat teks:<br/>
        • Ukuran huruf, tebal, miring, garis bawah<br/>
        • Warna teks (dapat dipilih)<br/>
        • Transparansi (opasitas) dengan penggeser<br/>
        • Pembungkusan kata (berbagai lebar, mis. lebar halaman, sempit, tanpa pembungkusan)</li>
        <li>Setelah dikonfirmasi, teks akan muncul di lokasi klik. Anda dapat memindahkannya dengan mouse atau tombol panah.</li>
        <li>Klik dua kali pada teks untuk membuka mode edit; ESC untuk keluar.</li>
        </ul>

        <p><strong>2. Mengelola Blok Teks (Template)</strong></p>
        <ul>
        <li>Di sisi kiri dialog teks, Anda melihat daftar semua blok teks yang disimpan.</li>
        <li><strong>Menyimpan Blok:</strong> Masukkan teks, format, dan klik "💾 Simpan sebagai Blok". Beri nama file (tanpa ekstensi).</li>
        <li><strong>Memuat Blok:</strong> Klik nama yang diinginkan di daftar. Teks dan format akan diambil dan dapat disesuaikan jika perlu.</li>
        <li><strong>Menghapus:</strong> Klik kanan pada blok untuk menghapusnya atau mengubah status privasinya.</li>
        </ul>

        <p><strong>3. Blok Teks Pribadi (Kata Sandi Utama)</strong></p>
        <ul>
        <li>Jika Anda telah mengatur kata sandi utama (di Pengaturan → Kelola Kata Sandi), Anda dapat menandai blok sebagai "pribadi".</li>
        <li>Centang kotak "Blok Teks Pribadi" di dialog sebelum menyimpan.</li>
        <li>Blok pribadi hanya ditampilkan dalam daftar jika Anda telah memasukkan kata sandi utama sekali per sesi (autentikasi melalui ikon gembok atau saat akses pertama).</li>
        <li>Dengan cara ini Anda dapat melindungi blok teks rahasia dari akses tidak sah.</li>
        </ul>

        <p><strong>4. Menyisipkan Tanda Silang</strong></p>
        <ul>
        <li>Dari menu konteks, Anda juga dapat menyisipkan tanda silang grafis (mis. untuk kotak centang).</li>
        <li>Ukuran, ketebalan garis, dan warna tanda silang dapat disesuaikan secara global di pengaturan (menu "Pengaturan" → "Pengaturan Tanda Silang").</li>
        <li>Klik kanan pada tanda silang yang ada untuk mengubahnya secara individual.</li>
        </ul>

        <p><strong>5. Tindakan Massal</strong></p>
        <ul>
        <li>Jika Anda telah menempatkan beberapa teks atau tanda silang pada satu halaman, Anda dapat menyimpan atau membuang semuanya sekaligus dari menu konteks (klik kanan dalam mode teks).</li>
        <li>Saat menyimpan, semua elemen akan disematkan ke PDF dan tetap sebagai grafik vektor.</li>
        </ul>

        <p><strong>6. Pintasan Keyboard dalam Mode Teks</strong></p>
        <ul>
        <li>Tombol panah: memindahkan elemen</li>
        <li>Ctrl+tombol panah: langkah lebih besar</li>
        <li>Enter: membuka dialog simpan (simpan semua / sesuaikan / buang)</li>
        <li>ESC: membuang elemen saat ini</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Pengaturan Tanda Silang",
        'cross_properties': "Properti Tanda Silang",
        'cross_size': "Ukuran (px):",
        'cross_line_width': "Ketebalan Garis:",
        'cross_color': "Warna:",
        'cross_choose_color': "Pilih",
        'cross_fine_tuning': "Penyesuaian Halus saat Menyimpan (piksel)",
        'cross_offset_x': "Offset X:",
        'cross_offset_y': "Offset Y:",
        'cross_offset_x_tooltip': "Nilai negatif menggeser tanda silang ke kiri saat disimpan, positif ke kanan",
        'cross_offset_y_tooltip': "Nilai negatif menggeser tanda silang ke atas saat disimpan, positif ke bawah",
        'cross_preview': "Pratinjau",
        'cross_save': "Terapkan Pengaturan",
        'cross_customized': "Tanda Silang Disesuaikan",
        'cross_settings_applied': "Pengaturan tanda silang disimpan.\nUkuran: {0}px, ketebalan garis: {1}px\n{2}",
        'cross_updated_count': "{0} tanda silang yang ada diperbarui.",
        'cross_no_crosses': "Tidak ada tanda silang yang ditemukan.",
        'cross_settings_applied_all': "Pengaturan tanda silang diterapkan ke semua {0} tanda silang",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Pengaturan Tanda Tangan",
        'signature_1': "Tanda Tangan 1",
        'signature_2': "Tanda Tangan 2",
        'signature_select': "Pilih Tanda Tangan",
        'signature_add': "➕ Tambah Tanda Tangan Baru...",
        'signature_size': "Ukuran untuk Tanda Tangan {0} (%):",
        'signature_common': "Pengaturan Umum",
        'signature_timestamp': "Tambahkan stempel waktu secara otomatis",
        'signature_location': "Lokasi Default:",
        'signature_timestamp_size': "Ukuran Huruf Stempel Waktu:",
        'signature_no_files': "-- Tidak ada tanda tangan ditemukan --",
        'signature_insert': "Sisipkan Tanda Tangan",
        'signature_insert_1': "Sisipkan Tanda Tangan 1",
        'signature_insert_2': "Sisipkan Tanda Tangan 2",
        'signature_customize': " Sesuaikan Tanda Tangan",
        'signature_discard': " Buang Tanda Tangan Ini",
        'signature_save_all': " Simpan Semua Tanda Tangan",
        'signature_discard_all': " Buang Semua Tanda Tangan",
        'signature_guide_title': "Tanda Tangan – Panduan",
        'signature_guide': """
📝 Tanda Tangan – Panduan Singkat

- Atur kata sandi utama
- Konfigurasi tanda tangan di menu Pengaturan
  (ukuran, stempel waktu ...)
- Sisipkan dengan KLIK KANAN di lokasi yang diinginkan
  (kata sandi utama diperlukan sekali per sesi)
- Pindahkan tanda tangan dengan mouse atau tombol panah
- Beberapa tanda tangan dapat disisipkan satu per satu
- Setiap tanda tangan dapat disesuaikan secara individual
- Buang satu tanda tangan
- Simpan / buang semua tanda tangan sekaligus
- Alternatif, dapat juga menggunakan bilah menu.
        """,
        'signature_placeholder': "Pratinjau tidak tersedia",
        'signature_info': "Tanda Tangan {0}: {1}×{2} px ({3}% dari {4}×{5})",
        'signature_info_placeholder': "Pengaturan untuk Tanda Tangan {0}",
        'signature_inserted': "Tanda Tangan {0} disisipkan di halaman {1}",
        'signature_deleted': "Tanda Tangan dihapus",
        'signature_copied': "Tanda Tangan disalin",
        'signature_pasted': "Tanda Tangan {0} ditempel",
        'signature_saved': "{0} tanda tangan telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'signature_saved_voice': "{0} tanda tangan disimpan",
        'mode_replace_signature_format': "Keluar dari mode dan sisipkan Tanda Tangan {0}",
        'mode_conflict_voice_signature': "Mode {0} aktif. Keluar dan sisipkan tanda tangan?",
        'signature_not_configured': "Tanda Tangan {0} tidak dikonfigurasi",
        'signature_file_not_found': "File tanda tangan tidak ditemukan",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Tidak ada tanda tangan yang disalin",
        'no_signatures_to_save': "Tidak ada tanda tangan untuk disimpan",
        'signature_save_question': "Simpan semua tanda tangan, sesuaikan, atau buang yang ini?",
        'signatures_saved_title': "Tanda Tangan Disimpan",
        'signatures_saved': "{0} tanda tangan telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'signatures_saved_voice': "{0} tanda tangan disimpan.",
        'all_signatures_discarded': "Semua tanda tangan dibuang",
        'signature_settings_saved': "Pengaturan tanda tangan disimpan",
        'signature_cancelled': "Tanda Tangan dibuang",
        'signature_active_title': "Tanda Tangan Aktif",
        'signature_replace_question': "Sudah ada tanda tangan yang aktif.\n\nApakah Anda ingin mengganti tanda tangan saat ini?",
        'signature_replace': "Ganti Tanda Tangan",
        'signature_replace_voice': "Ganti tanda tangan saat ini atau batalkan?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Pengaturan Gambar",
        'image_common': "Pengaturan Umum Gambar",
        'image_keep_aspect': "Pertahankan rasio aspek saat menyeret",
        'image_default_size': "Ukuran Default (%):",
        'image_dark_invert': "Balikkan gambar dalam Mode Gelap",
        'image_dark_invert_tooltip': "Diaktifkan: gambar dibalik untuk visibilitas lebih baik",
        'image_fine_tuning': "Penyesuaian Halus (piksel)",
        'image_offset_x': "Offset X:",
        'image_offset_y': "Offset Y:",
        'image_offset_x_tooltip': "Nilai negatif menggeser gambar ke kiri saat disimpan, positif ke kanan",
        'image_offset_y_tooltip': "Nilai negatif menggeser gambar ke atas saat disimpan, positif ke bawah",
        'image_select': "Pilih Gambar",
        'image_insert': "Sisipkan Gambar",
        'image_customize': " Sesuaikan Gambar",
        'image_aspect': " Pertahankan Rasio Aspek",
        'image_discard': " Buang Gambar Ini",
        'image_save_all': " Simpan Semua Gambar",
        'image_discard_all': " Buang Semua Gambar",
        'image_filter': "Gambar",
        'image_guide_title': "Menyisipkan Gambar – Panduan",
        'image_guide': """
📷 Menyisipkan Gambar ke PDF – Panduan Singkat:

1. Klik kanan di lokasi yang diinginkan
2. "Sisipkan Gambar" → pilih gambar
3. Posisikan gambar: seret dengan mouse
4. Sesuaikan ukuran: seret di sudut/tepi
5. Pertahankan rasio aspek: tombol [A]
6. Penyesuaian lebih lanjut: klik kanan pada gambar

Tips: Di menu konteks Anda dapat menyesuaikan pengaturan.
        """,
        'image_inserted': "Gambar disisipkan di halaman {1}",
        'image_deleted': "Gambar dibuang",
        'image_copied': "Gambar disalin",
        'image_pasted': "Gambar ditempel",
        'image_saved': "{0} gambar telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'image_saved_voice': "{0} gambar disimpan",
        'image_aspect_on': "aktif",
        'image_aspect_off': "nonaktif",
        'image_aspect_toggle': "Pertahankan rasio aspek {0}",
        'image_reset': "Gambar dikembalikan ke ukuran asli",
        'image_replaced': "Gambar diganti",
        'image_invalid': "Gambar tidak valid",
        'mode_replace_image': "Sisipkan Gambar",
        'mode_conflict_voice_image': "Mode {0} aktif. Keluar dan sisipkan gambar?",
        'image_active_title': "Gambar Aktif",
        'image_replace_question': "Sudah ada gambar yang aktif.\n\nApakah Anda ingin mengganti gambar saat ini?",
        'image_replace': "Ganti Gambar",
        'image_replace_voice': "Ganti gambar saat ini atau batalkan?",
        'image_filter_all': "Gambar (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Semua File (*.*)",
        'no_copied_image': "Tidak ada gambar yang disalin",
        'image_discarded': "Gambar dibuang",
        'image_save_question': "Simpan semua gambar, sesuaikan, atau buang yang ini?",
        'no_images_to_save': "Tidak ada gambar untuk disimpan",
        'no_valid_images': "Tidak ada gambar yang valid untuk disimpan",
        'images_saved_title': "Gambar Disimpan",
        'images_saved': "{0} gambar telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'images_saved_voice': "{0} gambar disimpan.",
        'all_images_discarded': "Semua gambar dibuang",
        'image_settings_updated': "Pengaturan gambar diperbarui",
        'image_replace_title': "Pilih Gambar Baru",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Pengaturan Bentuk",
        'form_basic': "Pengaturan Dasar",
        'form_default_type': "Jenis Bentuk Default:",
        'form_rectangle': "Persegi Panjang",
        'form_ellipse': "Elips",
        'form_line': "Garis",
        'form_arrow': "Panah",
        'form_line_width': "Ketebalan Garis:",
        'form_colors': "Warna",
        'form_line_color': "Warna Garis:",
        'form_fill_color': "Warna Isian:",
        'form_choose_color': "Pilih",
        'form_transparent': "Latar Belakang Transparan (hanya garis)",
        'form_filled': "diisi",
        'form_dark_mode': "Mode Gelap",
        'form_dark_invert': "Balikkan warna dalam Mode Gelap",
        'form_fine_tuning': "Penyesuaian Halus (piksel)",
        'form_offset_x': "Offset X:",
        'form_offset_y': "Offset Y:",
        'form_offset_x_tooltip': "Nilai negatif menggeser bentuk ke kiri saat disimpan, positif ke kanan",
        'form_offset_y_tooltip': "Nilai negatif menggeser bentuk ke atas saat disimpan, positif ke bawah",
        'form_preview': "Pratinjau",
        'form_insert': "Sisipkan Bentuk",
        'form_rectangle_insert': "Persegi Panjang",
        'form_ellipse_insert': "Elips/Lingkaran",
        'form_line_insert': "Garis (2 klik)",
        'form_arrow_insert': "Panah (2 klik)",
        'form_customize': " Sesuaikan Bentuk",
        'form_transparent_toggle': " Latar Belakang Transparan",
        'form_discard': " Buang Bentuk Ini",
        'form_save_all': " Simpan Semua Bentuk",
        'form_discard_all': " Buang Semua Bentuk",
        'form_guide_title': "Menyisipkan Bentuk – Panduan",
        'form_guide': """
📐 Menyisipkan Bentuk ke PDF – Panduan Singkat:

1. Pilih jenis bentuk (persegi panjang, elips, garis, panah)
2. Klik di posisi
   - Persegi panjang/elips: satu klik menempatkan bentuk
   - Garis/panah: dua klik untuk titik awal dan akhir
3. Posisikan bentuk: seret dengan mouse
4. Sesuaikan ukuran: seret di sudut/tepi
5. Simpan bentuk: Enter
6. Buang bentuk: ESC
7. Penyesuaian lebih lanjut: klik kanan pada bentuk

Tips: Di menu konteks Anda dapat menyesuaikan pengaturan.
        """,
        'form_inserted': "{0} disisipkan di halaman {1}",
        'form_deleted': "Bentuk dihapus",
        'form_copied': "Bentuk disalin",
        'form_pasted': "Bentuk ditempel",
        'form_saved': "{0} bentuk telah disisipkan ke PDF.\n\nPDF dimuat ulang...",
        'form_saved_voice': "{0} bentuk disimpan",
        'form_reset': "Bentuk dikembalikan ke ukuran default",
        'form_transparent_on': "aktif",
        'form_transparent_off': "nonaktif",
        'form_transparent_toggled': "Latar Belakang Transparan {0}",
        'form_line_cancel': "Pembuatan garis dibatalkan",
        'form_second_click': "Sekarang klik titik akhir untuk {0}",
        'mode_replace_form': "Sisipkan Bentuk",
        'mode_conflict_voice_form': "Mode {0} aktif. Keluar dan sisipkan bentuk?",
        'form_settings_updated': "Pengaturan bentuk diperbarui",
        'form_unknown': "Bentuk",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klik pada posisi awal",
        'form_line_guide_2': "2. Klik pada posisi akhir",
        'form_line_guide_3': "Garis akan digambar di antara kedua titik.",
        'form_line_status_1': "Menunggu klik pertama...",
        'form_line_status_2': "Titik pertama ditetapkan: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Sekarang klik titik akhir...",
        'form_line_status_4': "Kedua titik telah ditetapkan.\nKlik 'Selesai' untuk menyimpan.",
        'form_line_reset': "Reset",
        'form_line_finish': "Selesai",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Salin (Cmd+C)",
        'paste': "Tempel (Cmd+V)",
        'copied': "Disalin: {0}",
        'no_element_to_copy': "Tidak ada elemen yang dipilih untuk disalin",
        'no_copied_data': "Tidak ada data yang disalin",
        'no_valid_position': "Tidak ada posisi yang valid untuk menempel",
        'copy_text': "Teks disalin",
        'copy_image': "Gambar disalin",
        'copy_form': "Bentuk disalin",
        'copy_signature': "Tanda Tangan disalin",
        'element_text': "Teks",
        'element_image': "Gambar",
        'element_form': "Bentuk",
        'element_signature': "Tanda Tangan",
        'element_unknown': "Elemen",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflik Mode",
        'mode_conflict_message': "Mode '{0}' sudah aktif.\n\nApakah Anda ingin keluar dari mode itu dan {1}?",
        'mode_replace': "Keluar dari mode dan {0}",
        'mode_cancel': "Batal",
        'mode_replace_text': "sisipkan teks",
        'mode_replace_cross': "sisipkan tanda silang",
        'mode_replace_signature': "sisipkan tanda tangan",
        'mode_replace_image': "sisipkan gambar",
        'mode_replace_form': "sisipkan bentuk",
        'mode_conflict_voice': "Mode {0} aktif. Keluar dan sisipkan teks?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Input Teks",
        'active_mode_signature': "Tanda Tangan",
        'active_mode_image': "Gambar",
        'active_mode_form': "Bentuk",
        'active_mode_and': " dan ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Sisipkan",
        'insert_another_text': "Sisipkan Teks",
        'insert_another_cross': "Sisipkan Tanda Silang",
        'insert_another_signature_1': "Tanda Tangan 1",
        'insert_another_signature_2': "Tanda Tangan 2",
        'insert_another_image': "Sisipkan Gambar",
        'insert_another_form_rect': "Persegi Panjang",
        'insert_another_form_ellipse': "Elips",
        'insert_another_form_line': "Garis (2 klik)",
        'insert_another_form_arrow': "Panah (2 klik)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Simpan {0}",
        'save_dialog_message': "{0} akan disimpan di halaman {1}.\n\nBagaimana Anda ingin melanjutkan?",
        'save_all': "Simpan Semua {0}",
        'save_single': "Simpan {0}",
        'save_customize': "Sesuaikan {0}",
        'save_discard': "Buang {0} ini",
        'save_continue': "Lanjutkan Mengedit",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Pergi ke Halaman {0}",
        'context_rotate': " Putar Halaman {0}",
        'context_delete': " Hapus Halaman {0}",
        'context_export': " Ekspor Halaman {0}",
        'context_mark_as': " Tandai Halaman Sebagai...",
        'context_mark_empty': " Halaman Kosong",
        'context_unmark_empty': " Tidak Lagi Kosong",
        'context_mark_export': " Tandai untuk Ekspor",
        'context_unmark_export': " Jangan Ekspor Lagi",
        'context_batch_actions': " Tindakan Massal",
        'context_batch_delete_empty': " Hapus Semua {0} Halaman Kosong",
        'context_batch_export_single': " Ekspor Semua {0} Halaman (satu file)",
        'context_batch_export_split': " Ekspor Semua {0} Halaman (terpisah)",
        'context_drag_start': " Mulai Seret dan Lepas",
        'context_drag_stop': " Hentikan Seret dan Lepas",
        'context_insert': " Sisipkan",
        'context_insert_pages': " Sisipkan Halaman",
        'context_zoom': "Pembesaran",
        'discard_mixed': "Buang semua {0} {1} dan {2} {3}",
        'save_mixed': "Simpan {0} {1} dan {2} {3}",
        'discard_texts': "Buang semua {0} teks",
        'discard_text_single': "Buang 1 teks",
        'save_texts': "Simpan {0} teks",
        'save_text_single': "Simpan 1 teks",
        'discard_crosses': "Buang semua {0} tanda silang",
        'discard_cross_single': "Buang 1 tanda silang",
        'save_crosses': "Simpan {0} tanda silang",
        'save_cross_single': "Simpan 1 tanda silang",
        'discard_signatures': "Buang semua {0} tanda tangan",
        'save_signature_single': "Simpan 1 tanda tangan",
        'save_signatures': "Simpan {0} tanda tangan",
        'discard_images': "Buang semua {0} gambar",
        'save_image_single': "Simpan 1 gambar",
        'save_images': "Simpan {0} gambar",
        'discard_forms': "Buang semua {0} bentuk",
        'save_form_single': "Simpan 1 bentuk",
        'save_forms': "Simpan {0} bentuk",
        'cross_discard': "Buang tanda silang ini",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informasi Ekspor / Impor",
        'export_what': "📋 Apa yang diekspor?",
        'export_general': "Pengaturan Umum",
        'export_general_items': "• Keluaran suara (aktif/nonaktif, kecepatan)\n• Mode Gelap/Terang\n• Pengaturan cadangan\n• Pengaturan OCR",
        'export_image_form': "Pengaturan Gambar dan Bentuk",
        'export_image_form_items': "• Pengaturan gambar (rasio aspek, ukuran default)\n• Pengaturan bentuk (ketebalan garis, warna)\n• Pengaturan tanda tangan (jalur, ukuran, stempel waktu)",
        'export_passwords': "Basis Data Kata Sandi",
        'export_passwords_items': "• Semua kata sandi PDF yang disimpan\n• Dapat dipilih dienkripsi atau didekripsi",
        'export_master': "Pengaturan Kata Sandi Utama",
        'export_master_items': "• Hash kata sandi utama\n• Pengaturan untuk tanda tangan/blok teks",
        'export_signatures': "Tanda Tangan dan Blok Teks",
        'export_signatures_items': "• Semua file gambar (tanda tangan)\n• Semua blok teks dengan pemformatan\n• Penandaan pribadi/publik",
        'export_import_warning': "⚠️ Catatan Penting",
        'export_import_note': "• Saat mengimpor, SEMUA pengaturan saat ini akan ditimpa\n• Aplikasi perlu dimulai ulang\n• Tanda tangan/blok teks yang ada akan diganti",
        'export_master_note': "• Jika kata sandi utama diatur, Anda dapat memilih:\n  - Didekripsi (kata sandi dalam teks biasa)\n  - Dienkripsi (hanya dapat dibaca dengan kata sandi utama)",
        'export_security': "• File ZIP yang diekspor berisi data rahasia\n• Simpan dengan aman (mis. di USB terenkripsi)\n• Jika file hilang, kata sandi tidak dapat dipulihkan",
        'export_format': "📁 Format Ekspor",
        'export_format_desc': "Pengaturan disimpan dalam satu file ZIP:",
        'export_filename': "Pengaturan_PDFDarkView_YYYYMMDD_HHMMSS.zip",
        'export_success': "Pengaturan berhasil diekspor",
        'export_failed': "Ekspor gagal",
        'export_import_question': "Apakah Anda ingin memulai ulang aplikasi sekarang?",
        'export_password_question': "Kata sandi utama diatur.\n\nApakah Anda ingin mengekspor kata sandi dalam bentuk didekripsi?\n(jika tidak, mereka akan diekspor dalam bentuk terenkripsi)",
        'export_decrypt': "Ekspor Didekripsi",
        'export_encrypt': "Ekspor Dienkripsi",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Tentang PDF Dark View",
        'info_version': "Versi",
        'info_author': "Dikembangkan oleh Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Tentang",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> adalah penampil PDF yang mudah diakses, dikembangkan khusus untuk penyandang tunanetra.</p>

            <p><strong>Fitur Utama:</strong></p>
            <ul>
                <li>Antarmuka kontras tinggi, dapat disesuaikan</li>
                <li>Kontrol keyboard penuh</li>
                <li>Output suara terintegrasi</li>
                <li>OCR untuk dokumen hasil pindaian</li>
                <li>Alat pengeditan yang lengkap</li>
            </ul>

            <p>Lebih dari 50 bahasa didukung – sehingga PDF dapat diakses oleh semua orang.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Fitur",
        'info_features_intro': "PDF Dark View menawarkan kemungkinan berikut kepada Anda:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Tampilan & Navigasi</strong> – Mode Gelap/Terang, membalik halaman, zoom, lompat ke halaman</li>
            <li><strong>OCR (Pengenalan Teks)</strong> – Buat dokumen hasil pindaian dapat dicari dan disalin</li>
            <li><strong>Pengeditan</strong> – Sisipkan teks, tanda silang, tanda tangan, gambar, dan bentuk</li>
            <li><strong>Manajemen Halaman</strong> – Hapus, ekstrak, sisipkan, pindahkan dengan tarik & lepas</li>
            <li><strong>Ekspor</strong> – Ke Word, Pages, atau sebagai teks</li>
            <li><strong>Keamanan</strong> – Perlindungan dan manajemen kata sandi</li>
            <li><strong>Aksesibilitas</strong> – Output suara, kontrol keyboard, kontras tinggi</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Pengoperasian",
        'info_accessibility': "♿ Aksesibilitas – kontrol keyboard penuh",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Umum</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Buka PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Cari</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Alihkan Mode Gelap/Terang</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Cetak</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Keluar</div>

        <div class="shortcut-cat">📖 Navigasi</div>
        <div class="shortcut-row"><kbd>Tombol panah</kbd> Membalik halaman demi halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Pergi ke halaman</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Halaman pertama</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Halaman terakhir</div>

        <div class="shortcut-cat">✏️ Pengeditan</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Sisipkan teks</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Hapus halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Ekstrak halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Sisipkan halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Pindahkan halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Putar halaman</div>

        <div class="shortcut-cat">🖼️ Memindahkan elemen</div>
        <div class="shortcut-row"><kbd>Tombol panah</kbd> Pindahkan teks/gambar/tanda tangan</div>
        <div class="shortcut-row"><kbd>Ctrl+Tombol panah</kbd> Langkah yang lebih besar</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Simpan</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Batalkan</div>

        <div class="shortcut-cat">🗣️ Output suara</div>
        <div class="shortcut-row"><kbd>F2</kbd> Nyalakan/matikan output suara</div>
        """,
        'info_contextmenu': "📌 Penting: Semua fungsi juga dapat diakses melalui menu konteks (tombol kanan mouse)!",
        'info_accessibility_hint': "💡 Tip: Output suara (F2) memudahkan orientasi dan memberikan umpan balik tentang menu dan dialog.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lisensi & Impresum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Informasi sesuai dengan § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Jerman<br>
        Email: binhdiez64@gmail.com<br>
        Bertanggung jawab atas konten: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Penafian</strong><br>
        Perangkat lunak ini dikembangkan dengan sangat hati-hati. Tidak ada jaminan atas keakuratan, kelengkapan, dan fungsionalitas. Penggunaan dilakukan atas risiko sendiri.<br><br>

        <strong>📄 Lisensi MIT (penggunaan pribadi)</strong><br>
        Hak cipta (c) 2026 Toralf Schulz (BinhDiez)<br>
        Diizinkan: penggunaan gratis, perubahan pribadi, salinan pribadi.<br>
        Tidak diizinkan: penjualan, penggunaan komersial, penghapusan pemberitahuan hak cipta.<br><br>

        <strong>🔧 Komponen pihak ketiga</strong><br>
        Perangkat lunak ini berisi komponen di bawah lisensi GPL, AGPL, Apache 2.0, BSD, dan MIT.<br>
        Saat mendistribusikan ulang, ketentuan lisensi masing-masing harus dipatuhi.<br><br>

        <strong>🌐 Sumber Terbuka</strong><br>
        Kode sumber tersedia dan dapat dilihat, diubah, dan didistribusikan ulang sesuai dengan ketentuan lisensi masing-masing.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Penghargaan",
        'info_credits': "Terima kasih kepada komunitas sumber terbuka",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Pemrosesan PDF</li>
            <li><strong>PyQt5</strong> – Antarmuka grafis</li>
            <li><strong>Tesseract OCR</strong> – Pengenalan teks</li>
            <li><strong>OCRmyPDF</strong> – Integrasi OCR</li>
            <li><strong>python-docx</strong> – Ekspor ke Word</li>
            <li><strong>qtawesome</strong> – Ikon</li>
            <li><strong>DeepSeek</strong> – Dukungan untuk terjemahan (50+ bahasa)</li>
            <li><strong>Semua pengguna</strong> – Untuk umpan balik yang berharga</li>
            <li><strong>Komunitas sumber terbuka</strong> – Untuk pustaka yang luar biasa</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Bahasa",
        'info_languages_header': "🌍 Dukungan Bahasa",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View saat ini mendukung <strong>62 bahasa</strong> – sehingga perangkat lunak ini dapat digunakan secara aksesibel di seluruh dunia.</p>

            <p><strong>📖 Daftar bahasa lengkap (Per Maret 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albania (Shqip)</li>
                    <li>🇩🇿 Arab (العربية)</li>
                    <li>🇮🇩 Bali (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Burma (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnia (Bosanski)</li>
                    <li>🇧🇬 Bulgaria (Български)</li>
                    <li>🇨🇳 Cina (中文)</li>
                    <li>🇩🇰 Denmark (Dansk)</li>
                    <li>🇩🇪 Jerman (Deutsch)</li>
                    <li>🇬🇧 Inggris (English)</li>
                    <li>🇪🇪 Estonia (Eesti)</li>
                    <li>🇫🇮 Finlandia (Suomi)</li>
                    <li>🇫🇷 Prancis (Français)</li>
                    <li>🇬🇷 Yunani (Ελληνικά)</li>
                    <li>🇮🇱 Ibrani (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroasia (Hrvatski)</li>
                    <li>🇭🇺 Hungaria (Magyar)</li>
                    <li>🇮🇩 Indonesia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandia (Gaeilge)</li>
                    <li>🇮🇸 Islandia (Íslenska)</li>
                    <li>🇮🇹 Italia (Italiano)</li>
                    <li>🇯🇵 Jepang (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korea (한국어)</li>
                    <li>🇱🇦 Laos (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvia (Latviešu)</li>
                    <li>🇱🇹 Lituania (Lietuvių)</li>
                    <li>🇱🇺 Luksemburg (Lëtzebuergesch)</li>
                    <li>🇲🇾 Melayu (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolia (Монгол)</li>
                    <li>🇳🇵 Nepal (नेपाली)</li>
                    <li>🇳🇱 Belanda (Nederlands)</li>
                    <li>🇳🇴 Norwegia (Norsk)</li>
                    <li>🇦🇫 Pashtun (پښتو)</li>
                    <li>🇮🇷 Persia (فارسی)</li>
                    <li>🇵🇱 Polandia (Polski)</li>
                    <li>🇵🇹 Portugis (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumania (Română)</li>
                    <li>🇷🇺 Rusia (Русский)</li>
                    <li>🇸🇪 Swedia (Svenska)</li>
                    <li>🇷🇸 Serbia (Српски)</li>
                    <li>🇸🇰 Slowakia (Slovenčina)</li>
                    <li>🇸🇮 Slovenia (Slovenščina)</li>
                    <li>🇪🇸 Spanyol (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Ceko (Čeština)</li>
                    <li>🇹🇷 Turki (Türkçe)</li>
                    <li>🇺🇦 Ukraina (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnam (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yiddi (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Tambahkan bahasa sendiri:</strong><br>
                Menginginkan bahasa yang belum tersedia? Cukup letakkan file kamus Anda sendiri (<code>sprache_xx.py</code>) di samping aplikasi – perangkat lunak akan mengenalinya secara otomatis. Jika tertarik dengan terjemahan khusus, jangan ragu untuk menghubungi saya.
            </div>

            <p><strong>🙏 Ucapan terima kasih khusus:</strong> DeepSeek atas dukungannya dalam menerjemahkan semua kamus ke dalam 62 bahasa.</p>

            <p>📧 Kontak untuk terjemahan: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Kesalahan",
        'error_occurred': "Terjadi kesalahan",
        'error_pdf_load': "Kesalahan saat memuat PDF",
        'error_pdf_save': "Kesalahan saat menyimpan PDF",
        'error_ocr': "Kesalahan saat pengenalan teks",
        'error_no_pdf': "Tidak ada PDF dimuat",
        'error_page_not_found': "Halaman tidak ditemukan",
        'error_invalid_range': "Rentang halaman tidak valid",
        'error_file_not_found': "File tidak ditemukan",
        'error_permission': "Tidak ada izin",
        'error_unknown': "Kesalahan tidak dikenal",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Berhasil",
        'success_operation': "Operasi berhasil diselesaikan",
        'success_saved': "Berhasil disimpan",
        'success_exported': "Berhasil diekspor",
        'success_imported': "Berhasil diimpor",
        'success_deleted': "Berhasil dihapus",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Konfirmasi",
        'confirm_yes': "Ya",
        'confirm_no': "Tidak",
        'confirm_ok': "OK",
        'confirm_cancel': "Batal",
        'confirm_delete': "Hapus",
        'confirm_overwrite': "Timpa",
        'confirm_continue': "Lanjutkan",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Memuat PDF...",
        'progress_saving': "Menyimpan PDF...",
        'progress_exporting': "Mengekspor PDF...",
        'progress_processing': "Memproses...",
        'progress_wait': "Harap tunggu...",
        'progress_preparing': "Mempersiapkan...",
        'progress_finalizing': "Menyelesaikan...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Putih",
        'color_black': "Hitam",
        'color_red': "Merah",
        'color_green': "Hijau",
        'color_blue': "Biru",
        'color_yellow': "Kuning",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Oranye",
        'color_gray': "Abu-abu",
        'color_custom': "Pilih Warna",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&File",
        'menu_edit': "&Edit",
        'menu_view': "&Tampilan",
        'menu_tools': "&Alat",
        'menu_settings': "&Pengaturan",
        'menu_help': "&Bantuan",
        'menu_language': "🌐 Bahasa",
        'menu_guides': "&Panduan",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Buka",
        'file_save_as': "&Simpan Sebagai...",
        'file_protect': "&Lindungi Dokumen...",
        'file_export': "&Ekspor",
        'file_export_pages': "Ekspor ke Pages",
        'file_export_word': "Ekspor ke DOCX",
        'file_export_text': "Ekspor ke TXT",
        'file_print_now': "&Cetak Sekarang",
        'file_print': "&Cetak",
        'file_close': "&Tutup",
        'file_quit': "&Keluar",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Cari",
        'edit_ocr': " Lakukan OCR",
        'edit_rotate': "&Putar Halaman",
        'edit_rotate_all': "Putar &Semua Halaman",
        'edit_delete_pages': "&Hapus Halaman",
        'edit_extract_pages': "&Ekstrak Halaman",
        'edit_insert_pages': "&Sisipkan Halaman",
        'edit_move_pages': "&Pindahkan Halaman",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Sisipkan Teks dan Tanda Silang",
        'text_insert': " Sisipkan Teks",
        'cross_insert': " Sisipkan Tanda Silang",
        'text_customize': " Sesuaikan Teks",
        'cross_customize': " Sesuaikan Tanda Silang Ini",
        'cross_customize_all': " Sesuaikan Semua Tanda Silang",
        'text_discard': " Buang Teks/Tanda Silang Ini",
        'text_discard_all': " Buang Semua Teks dan Tanda Silang",
        'text_save_all': " Simpan Semua Teks dan Tanda Silang",
        'text_guide': " Input Teks / Blok Teks – Panduan",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Sisipkan Tanda Tangan",
        'signature_settings_menu': " Pengaturan...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Sisipkan Gambar",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Sisipkan Bentuk",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Tampilkan Jendela Teks",
        'view_zoom': "&Pembesaran",
        'view_zoom_page': "&Lebar Halaman (default)",
        'view_zoom_two': "&Dua Halaman",
        'view_zoom_overview': "&Ikhtisar (beberapa halaman)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Aksesibilitas",
        'settings_voice': "Keluaran Suara",
        'settings_voice_tooltip': "melengkapi keluaran suara pembaca layar dengan informasi tambahan",
        'settings_signature': "&Pengaturan Tanda Tangan",
        'settings_password': "&Kelola Kata Sandi",
        'settings_backup': "Buat cadangan sebelum perubahan",
        'settings_export_import': "&Ekspor Pengaturan / Impor Pengaturan",
        'settings_export': "&Ekspor Semua Pengaturan...",
        'settings_import': "&Impor Semua Pengaturan...",
        'settings_export_info': "&Apa yang diekspor?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "aktif",
        'voice_off': "nonaktif",
        'voice_toggle': "Keluaran Suara {0}",
        'voice_speed': "Kecepatan {0} persen",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Alat tidak ditemukan:\n{0}\n\nBASE_DIR: {1}\nPastikan alat PDF diinstal di direktori {1}.",
        'tool_started': "{0} dimulai",
        'tool_start_failed': "Tidak dapat memulai",
        'process_error_failed_to_start': "Proses tidak dapat dimulai. Apakah file tersebut ada?",
        'process_error_crashed': "Proses macet saat memulai.",
        'process_error_timeout': "Batas waktu proses tercapai.",
        'process_error_write': "Kesalahan menulis ke proses.",
        'process_error_read': "Kesalahan membaca dari proses.",
        'process_error_unknown': "Kesalahan proses tidak dikenal",
        'process_command': "Perintah",
        'process_normal_exit': "selesai normal",
        'process_crashed': "macet",
        'process_nonzero_exit': "{0} selesai dengan kode kesalahan {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Membatalkan...",
        'move_cancelling': "Pemindahan dibatalkan",
        'opening_pdf': "Membuka PDF...",
        'loading_document': "Memuat dokumen...",
        'pdf_opened': "PDF dibuka",
        'pages_found_moving': "{0} halaman ditemukan, {1} untuk dipindahkan",
        'creating_backup': "Membuat cadangan...",
        'backup_description': "Mencadangkan file asli...",
        'backup_saved_as': "Cadangan disimpan sebagai: {0}",
        'error_format': "Kesalahan: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView oleh BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Pencarian direset",
        'page_header_simple': "=== Halaman {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Kelola Kata Sandi – Panduan",
        'password_guide_voice': "Panduan manajemen kata sandi. Silakan baca catatan.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Kelola Kata Sandi – Panduan Rinci</strong></p>

        <p><strong>1. Perlindungan Kata Sandi untuk PDF</strong></p>
        <ul>
        <li>Saat membuka PDF yang dilindungi kata sandi, muncul dialog di mana Anda dapat memasukkan kata sandi.</li>
        <li>Anda dapat menyimpan kata sandi dalam bentuk terenkripsi sehingga tidak perlu memasukkannya setiap kali (kotak centang "Simpan Kata Sandi").</li>
        <li>Dengan tombol "Hapus Kata Sandi" Anda dapat membuat salinan PDF yang didekripsi dan menghapus kata sandi dari basis data.</li>
        </ul>

        <p><strong>2. Kata Sandi Utama</strong></p>
        <ul>
        <li>Kata sandi utama melindungi akses ke semua kata sandi PDF yang disimpan.</li>
        <li><strong>Mengatur:</strong> Pergi ke "Pengaturan → Kelola Kata Sandi → Pengaturan Kata Sandi Utama" dan klik "Atur Kata Sandi Utama". Pilih kata sandi yang kuat (minimal 8 karakter).</li>
        <li><strong>Mengubah:</strong> Setelah autentikasi berhasil, Anda dapat mengubah kata sandi utama.</li>
        <li><strong>Menghapus:</strong> Jika Anda menghapus kata sandi utama, SEMUA kata sandi yang disimpan akan dihapus secara permanen. Anda dapat mengekspor cadangan sebelumnya.</li>
        <li>Sekali per sesi, Anda harus mengautentikasi dengan kata sandi utama untuk mengakses fungsi yang dilindungi (mis. menampilkan kata sandi).</li>
        </ul>

        <p><strong>3. Manajemen Kata Sandi (Daftar)</strong></p>
        <ul>
        <li>Di "Pengaturan → Kelola Kata Sandi" terbuka tabel semua PDF yang disimpan dengan kata sandi terenkripsi.</li>
        <li><strong>Tanpa Kata Sandi Utama:</strong> Anda hanya dapat menghapus entri – kata sandi tetap tersembunyi.</li>
        <li><strong>Dengan Kata Sandi Utama (terautentikasi):</strong> Anda dapat menampilkan, menyalin, mengekspor, dan menghapus kata sandi.</li>
        <li><strong>Ekspor:</strong> Pilih format (JSON, CSV, TXT) dan simpan daftar. Jika kata sandi utama diatur, Anda dapat memilih apakah kata sandi diekspor dalam bentuk didekripsi atau terenkripsi.</li>
        <li><strong>Impor:</strong> File ZIP yang diekspor sebelumnya (semua pengaturan) dapat diimpor kembali melalui "Pengaturan → Ekspor Pengaturan / Impor Pengaturan". Perhatian: Data yang ada akan ditimpa!</li>
        </ul>

        <p><strong>4. Generator Kata Sandi</strong></p>
        <ul>
        <li>Di dialog kata sandi (mis. saat melindungi PDF), di sebelah kanan bidang input terdapat tombol dadu 🎲.</li>
        <li>Klik untuk membuka generator kata sandi. Anda dapat mengatur panjang, kumpulan karakter (huruf besar, huruf kecil, angka, simbol) dan pemisah untuk keterbacaan yang lebih baik.</li>
        <li>Kata sandi yang dihasilkan dapat langsung digunakan dan jika perlu disalin.</li>
        </ul>

        <p><strong>5. Catatan Keamanan Penting</strong></p>
        <ul>
        <li>Kata sandi yang disimpan disimpan terenkripsi dengan AES-256. Kunci diturunkan dari kata sandi utama Anda (jika diatur) atau dari nilai tetap (tanpa kata sandi utama).</li>
        <li>Tanpa kata sandi utama, kata sandi tetap terenkripsi tetapi kunci tertanam dalam program – penyerang dengan akses ke file Anda dapat mendekripsinya. Oleh karena itu, kami sangat menyarankan penggunaan kata sandi utama.</li>
        <li>Basis data kata sandi terletak di file `Data/passwords.json`. Lakukan cadangan secara teratur, terutama sebelum menghapus kata sandi utama.</li>
        <li>Jika kata sandi utama hilang, semua kata sandi yang disimpan akan hilang secara permanen.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Mode inversi",
        'invert_mode_classic': "Klasik (inversi semua warna)",
        'invert_mode_smart': "Cerdas (inversi hanya kecerahan)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Ambang batas skala abu-abu",
        'gray_threshold_10': "10% (ketat)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standar)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (lunak)",
        'threshold_changed': "Ambang batas diatur ke {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Ambang batas skala abu-abu – Penjelasan",
        'threshold_guide_text': "Ambang batas skala abu-abu menentukan piksel mana dalam mode gelap cerdas yang dianggap 'abu-abu' dan diinversi.\n\n"
                                "• Nilai rendah (10%) hanya menginversi nuansa abu-abu yang hampir sempurna – elemen berwarna tetap terjaga sepenuhnya.\n"
                                "• Nilai tinggi (50%) juga menginversi piksel yang sedikit berwarna – ini meningkatkan kontras, tetapi dapat mendistorsi warna.\n\n"
                                "Nilai optimal tergantung pada dokumen. Untuk dokumen teks murni, 30–40% seringkali ideal, untuk grafik berwarna sebaiknya 10–20%.\n\n"
                                "Anda dapat menyesuaikan nilai kapan saja melalui menu 'Pengaturan' – PDF akan dimuat ulang segera.\n\n"
                                "Catatan:\n* Foto dan gambar hanya dapat ditampilkan dengan benar dalam Mode Terang!\n* Pengaturan inversi hanya ditampilkan ketika Mode Gelap diaktifkan.",
        'threshold_guide_voice': "Ambang batas skala abu-abu menentukan seberapa kuat mode gelap cerdas berintervensi. Nilai rendah melindungi warna, nilai tinggi meningkatkan kontras.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Membuka PDF...",
        'progress_loading_document': "Memuat dokumen...",
        'progress_pdf_opened': "PDF dibuka",
        'progress_creating_backup': "Membuat cadangan...",
        'progress_backup_description': "Mengamankan file asli...",
        'progress_backup_created': "Cadangan dibuat",
        'progress_backup_saved_as': "Disimpan sebagai: {0}",
        'progress_analyzing_start': "Memulai analisis...",
        'progress_searching_empty': "Mencari halaman kosong...",
        'progress_page_empty': "Halaman {0} kosong",
        'progress_page_keep': "Pertahankan halaman {0}",
        'progress_analysis_complete': "Analisis selesai",
        'progress_empty_found': "Ditemukan {0} halaman kosong",
        'progress_current_page': "Halaman saat ini",
        'progress_mark_delete': "Ditandai untuk dihapus",
        'progress_range_selected': "Rentang halaman {0}-{1}",
        'progress_deleting_pages': "Menghapus {0} halaman",
        'progress_creating_new_pdf': "Membuat PDF baru...",
        'progress_transferring_pages': "Memindahkan halaman",
        'progress_keeping_page': "Halaman {0} akan dipertahankan ({1}/{2})",
        'progress_saving_pdf': "Menyimpan PDF...",
        'progress_optimizing': "Mengoptimalkan ukuran file...",
        'progress_finalizing': "Menyelesaikan...",
        'progress_new_size': "Ukuran baru: {0:.2f} MB",
        'progress_cancelling': "Membatalkan...",
        'progress_cancel_message': "{0} sedang dibatalkan",
        'progress_pages_found_moving': "Ditemukan {0} halaman, {1} untuk dipindahkan",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Menganalisis PDF...",
        'ocr_status_optimizing': "Optimalisasi gambar sedang berlangsung...",
        'ocr_status_recognizing': "Pengenalan teks sedang berlangsung...",
        'ocr_status_embedding': "Menyematkan teks...",
        'ocr_status_finalizing': "Menyelesaikan PDF...",

        # PDF-Laden
        'progress_preparing': "Mempersiapkan...",
        'progress_loading': "Memuat PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Menghapus halaman...",
        'progress_moving_title': "Memindahkan halaman...",
        'pages_found': "Halaman ditemukan",
        'progress_creating_new_order': "Membuat urutan baru...",
        'progress_sorting_pages': "Mengurutkan halaman...",
        'progress_moving_to_begin': "Memindahkan {0} halaman ke awal",
        'progress_transferring_count': "Memindahkan {0} halaman",
        'progress_transferring_before_target': "Memindahkan halaman sebelum target",
        'progress_moving_pages': "Memindahkan {0} halaman",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_cadangan_",
        'filename_protected_suffix': "_dilindungi_",
        'filename_copy_suffix': "_Salinan",
        'filename_page_single': "_Halaman_",
        'filename_page_range': "_Halaman_",
        'filename_export_page': "_Halaman_{0:03}",
        'filename_export_range': "_Halaman_{0}-{1}",
        'filename_export_multiple': "_Halaman_{0}",
        'filename_with_text': "_dengan_Teks",
        'filename_with_signature': "_dengan_TandaTangan",
        'filename_with_image': "_dengan_Gambar",
        'filename_with_forms': "_dengan_Bentuk",
        # ---------------------------------------------------------
        # Zentrale Verwaltung des Formats der Zeitstempel
        # z.B. bei Änderung von %Y%m%d_%H%M%S auf %Y-%m-%d_%H.%M.%S
        # könnte hier vom User angepasst werden
        # ---------------------------------------------------------
        'filename_timestamp_format': "%Y%m%d_%H%M%S",
        'filename_timestamp_micro': "%Y%m%d_%H%M%S_%f",

        # ============================================
        # 56. ANSICHT – BUTTONLEISTE EIN-/AUSBLENDEN
        # ============================================
        'view_toggle_navbar': "Tampilkan bilah tombol",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Tidak dapat menghapus semua halaman",
		'pages_cannot_delete_last_page': 'Halaman terakhir tidak dapat dihapus!',
		'pages_cannot_delete_all_pages': 'Setidaknya harus ada satu halaman yang tersisa dalam dokumen!',
		'delete_pages_confirm': 'Apakah Anda yakin ingin menghapus {0} halaman?',
		'delete_pages_confirm_voice': 'Apakah Anda yakin ingin menghapus {0} halaman?',
		'pages_deleted': '{0} halaman berhasil dihapus.',
		'warning': 'Peringatan',
		'error': 'Kesalahan',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Tidak ada formulir dipilih",
        'form_customized': "Formulir disesuaikan",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Pilih",
        'btn_use': "Gunakan",
        'master_password_for_spasswords': "Untuk menyimpan dan menggunakan kata sandi, pertama-tama harus menyiapkan kata sandi utama.\n\nApakah Anda ingin menyiapkan kata sandi utama sekarang?",
        'open_saved_dialog_title': "Buka file yang disimpan",
        'open_saved_question': "Apakah Anda ingin membuka file yang disimpan sekarang?",
        'password': "Kata sandi",
        'password_manager_master_required': "Pengelola kata sandi hanya tersedia jika kata sandi utama telah disiapkan.\n\nApakah Anda ingin menyiapkan kata sandi utama sekarang?",
        'password_master_required_for_select': "Untuk menampilkan dan memilih kata sandi yang disimpan, Anda harus mengautentikasi dengan kata sandi utama terlebih dahulu.\n\nApakah Anda ingin mengautentikasi sekarang?",
        'password_not_available': "Kata sandi yang dipilih tidak tersedia atau tidak dapat didekripsi.",
        'password_options_title': "Opsi kata sandi",
        'password_save_choice_change': "Tetapkan kata sandi baru",
        'password_save_choice_keep': "Gunakan kata sandi yang ada",
        'password_save_choice_none': "Simpan tanpa enkripsi",
        'password_save_hint': "Siapkan kata sandi utama terlebih dahulu untuk menyimpan kata sandi dengan aman.",
        'password_save_master_required': "Simpan kata sandi (hanya mungkin dengan kata sandi utama)",
        'password_save_question': "PDF saat ini dilindungi kata sandi. Apakah Anda ingin menggunakan kata sandi yang ada, menetapkan yang baru, atau menyimpan tanpa enkripsi?",
        'password_select': "Pilih kata sandi",
        'password_select_none': "Tidak ada kata sandi yang dipilih.\n\nSilakan pilih kata sandi dari daftar.",
        'password_select_one': "Silakan pilih tepat satu kata sandi.\n\nAnda telah menandai beberapa kata sandi.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_cadangan",
        'filename_insert_suffix': "_dengan_penyisipan",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_halaman_dihapus",
        'filename_pages_moved': "_halaman_dipindahkan",
        'filename_rotated_all_suffix': "_semua_halaman_diputar",
        'filename_rotated_suffix': "_halaman_diputar",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurasi nama file saat mengubah PDF",
        'filename_keep_suffixes': "Pertahankan ekstensi sebelumnya (mis. _dengan_teks)",
        'filename_keep_suffixes_false': "Ganti",
        'filename_keep_suffixes_true': "Pertahankan",
        'filename_preview_label': "Pratinjau nama file:",
        'filename_preview_overwrite_hint': "Pratinjau tidak tersedia – file asli akan ditimpa.",
        'filename_separator': "Pemisah antar kata",
        'filename_separator_none': "Tanpa pemisah",
        'filename_separator_space': "Spasi ( )",
        'filename_separator_underscore': "Garis bawah (_)",
        'filename_settings_saved': "Pengaturan nama file disimpan",
        'filename_settings_title': "Pemformatan nama file & cadangan",
        'filename_timestamp_position': "Posisi stempel waktu",
        'filename_timestamp_position_after': "Setelah nama dasar",
        'filename_timestamp_position_before': "Paling depan",
        'filename_timestamp_position_end': "Di akhir",
        'filename_use_timestamp': "Gunakan stempel waktu",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Perilaku saat perubahan:</b><ul><li>Menghapus dan menyisipkan halaman</li><li>Menyisipkan teks, tanda tangan, gambar, dan bentuk</li><li>OCR</li></ul></html>",
        'backup_section': "Cadangan untuk operasi halaman (Hapus, Pindahkan)",
        'behavior_info': "Catatan: Pada 'Timpa asli', stempel waktu dan sufiks diabaikan – file mempertahankan namanya.",
        'behavior_new_file': "Selalu buat file baru (dengan stempel waktu dan sufiks)",
        'behavior_overwrite': "Timpa asli (tanpa file baru)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Semua halaman diputar.\n\nAsli tetap tidak berubah.\nFile baru: {0}",
        'all_pages_rotated_voice': "Semua halaman diputar, file baru dibuat.",
        'empty_pages_deleted_new_file': "{0} halaman kosong dihapus.\n\nAsli tetap tidak berubah.\nFile baru: {1}",
        'empty_pages_deleted_voice': "{0} halaman kosong dihapus, file baru dibuat.",
        'ocr_keep_original': "Pertahankan asli (buka secara manual nanti)",
        'ocr_new_file_question': "PDF baru yang dapat dicari disimpan di:\n{0}\n\nApakah Anda ingin membukanya sekarang?",
        'ocr_open_new': "Buka file OCR baru",
        'ocr_original_kept': "File asli tetap terbuka. File OCR telah disimpan.",
        'page_deleted_new_file': "Halaman {0} dihapus.\n\nAsli tetap tidak berubah.\nFile baru: {1}",
        'page_deleted_voice': "Halaman {0} dihapus, file baru dibuat.",
        'page_rotated_new_file': "Halaman {0} diputar.\n\nAsli tetap tidak berubah.\nFile baru: {1}",
        'page_rotated_voice': "Halaman {0} diputar, file baru dibuat.",
        'pages_deleted_new_file': "{0} halaman dihapus.\n\nFile asli tetap tidak berubah.\nFile baru: {1}",
        'pages_deleted_new_file_voice': "{0} halaman dihapus, file baru dibuat.",
        'pages_inserted_new_file': "{0} halaman disisipkan.\n\nFile asli tetap tidak berubah.\nFile baru: {1}",
        'pages_inserted_new_file_ask': "{0} halaman disisipkan.\n\nAsli tetap tidak berubah.\nFile baru: {1}\n\nApakah Anda ingin membukanya sekarang?",
        'pages_inserted_voice_new': "{0} halaman disisipkan, file baru dibuat.",
        'pages_moved_new_file': "{0} halaman dipindahkan.\n\nFile asli tetap tidak berubah.\nFile baru: {1}",
        'pages_moved_new_file_voice': "{0} halaman dipindahkan, file baru dibuat.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Jangan tampilkan lagi",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Pengaturan cadangan</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Cadangan AKTIF</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Pada semua perubahan yang menimpa asli</strong> (teks, tanda tangan, gambar, bentuk, OCR, putar, sisip, hapus/pindah halaman) <strong>secara otomatis dibuat cadangan dengan stempel waktu</strong> sebelum perubahan diterapkan.</p>
                <p style="margin: 5px 0 5px 20px;">• Cadangan terletak di samping file asli (mis. <code>Dokumen_cadangan_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Jika Anda juga mengaktifkan opsi <strong>„Timpa asli“</strong>, cadangan juga dibuat.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Cadangan NONAKTIF</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Tidak ada cadangan yang dibuat</strong> – baik saat menimpa maupun pada operasi halaman.</p>
                <p style="margin: 5px 0 5px 20px;">• File asli dapat hilang secara tidak dapat dipulihkan saat ditimpa.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Hanya direkomendasikan untuk pengguna berpengalaman!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tips:</strong> Pengaturan cadangan tidak tergantung pada opsi „Timpa asli“. Anda dapat menggabungkan keduanya.<br>
                Anda dapat menyembunyikan pesan ini secara permanen.
            </div>
        </div>
        """,
        'backup_info_title': "Perilaku cadangan",
        'backup_info_voice': "Pemberitahuan tentang perilaku cadangan pada operasi halaman. Cadangan aktif menimpa asli, cadangan nonaktif membuat file baru.",
        'show_backup_info': "Info tentang pengaturan cadangan",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Jangan tampilkan lagi",
        'overwrite_enable_backup': "Aktifkan cadangan (direkomendasikan)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Timpa asli</p>
            <p>Jika Anda mengaktifkan opsi ini, perubahan (teks, tanda tangan, gambar, bentuk, OCR, putar, sisip) <strong>disimpan langsung di asli</strong> – <strong>tidak ada file baru yang dibuat</strong>.</p>
            <p>• Nama file tetap tidak berubah.<br>
            • Stempel waktu dan sufiks diabaikan.<br>
            • <strong>Tanpa cadangan, asli dapat hilang secara tidak dapat dipulihkan.</strong></p>
            <p style="color: #FFD700;">Rekomendasi: Aktifkan juga opsi cadangan untuk mendapatkan cadangan otomatis.</p>
        </div>
        """,
        'overwrite_info_title': "Timpa asli",
        'overwrite_info_voice': "Peringatan: Timpa asli – tanpa file baru. Cadangan direkomendasikan.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} halaman disisipkan.\n\nFile asli ditimpa.\nSebuah cadangan dibuat.",
        'pages_inserted_overwrite_no_backup': "{0} halaman disisipkan.\n\nFile asli ditimpa.\nTIDAK ada cadangan yang dibuat.",
        'texts_saved_overwrite_with_backup': "Perubahan disimpan di asli.\n\nSebuah cadangan dibuat.",
        'texts_saved_overwrite_no_backup': "Perubahan disimpan di asli.\n\nTIDAK ada cadangan yang dibuat.",
        'texts_crosses_saved_new_file': "{0} {1} dan {2} {3} disisipkan.\n\nFile asli tetap tidak berubah.\nSebuah file baru dibuat.\n\nPDF baru sedang dimuat...",
        'texts_saved_new_file': "{0} {1} disisipkan.\n\nFile asli tetap tidak berubah.\nSebuah file baru dibuat.\n\nPDF baru sedang dimuat...",
        'crosses_saved_new_file': "{0} {1} disisipkan.\n\nFile asli tetap tidak berubah.\nSebuah file baru dibuat.\n\nPDF baru sedang dimuat...",
        'elements_saved_new_file': "{0} elemen disisipkan.\n\nFile asli tetap tidak berubah.\nSebuah file baru dibuat.\n\nPDF baru sedang dimuat...",
        'signatures_saved_overwrite_with_backup': "Tanda tangan disimpan di asli.\n\nSebuah cadangan dibuat.",
        'signatures_saved_overwrite_no_backup': "Tanda tangan disimpan di asli.\n\nTIDAK ada cadangan yang dibuat.",
        'images_saved_overwrite_with_backup': "Gambar disimpan di asli.\n\nSebuah cadangan dibuat.",
        'images_saved_overwrite_no_backup': "Gambar disimpan di asli.\n\nTIDAK ada cadangan yang dibuat.",
        'forms_saved_overwrite_with_backup': "Bentuk disimpan di asli.\n\nSebuah cadangan dibuat.",
        'forms_saved_overwrite_no_backup': "Bentuk disimpan di asli.\n\nTIDAK ada cadangan yang dibuat.",
        'signatures_saved_new_file': "{0} tanda tangan disisipkan.\n\nFile asli tetap tidak berubah.\nSebuah file baru dibuat.\n\nPDF baru sedang dimuat...",
        'images_saved_new_file': "{0} gambar disisipkan.\n\nFile asli tetap tidak berubah.\nSebuah file baru dibuat.\n\nPDF baru sedang dimuat...",
        'forms_saved_new_file': "{0} bentuk disisipkan.\n\nFile asli tetap tidak berubah.\nSebuah file baru dibuat.\n\nPDF baru sedang dimuat...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Peringatan: PDF ini berisi halaman yang diputar. Posisi mungkin menyimpang.",
        'page_rotated_warning_title': "Halaman terdeteksi diputar",
        'page_rotated_warning_message': "Halaman saat ini {0} diputar {1}°.\n\nMenyisipkan elemen pada halaman yang diputar tidak didukung.\n\nApakah Anda ingin memutar halaman ke posisi tegak sekarang?",
        'page_rotated_warning_voice': "Peringatan: Halaman diputar. Harap putar terlebih dahulu.",
        'paste_on_rotated_page_simple_warning': "Penyisipan pada halaman {0} tidak mungkin!\n\nHalaman ini diputar {1}°.\n\nHarap putar halaman ke 0° terlebih dahulu (Menu: Edit → Sejajarkan halaman).\n\nPeringatan:\nElemen yang sebelumnya disalin akan hilang jika Anda tidak menyimpan sebelum memutar halaman.",
        'paste_on_rotated_page_voice': "Penyisipan dibatalkan. Halaman diputar. Harap sejajarkan halaman terlebih dahulu.",
        'page_rotated_cancel': "Batal",
        'page_rotated_rotate_until_upright': "Putar halaman berulang kali (sampai tegak)",
        'page_rotated_now_upright': "Halaman sekarang tegak. Anda sekarang dapat menyisipkan.",
        'page_rotated_still_not_upright': "Halaman tidak dapat diputar ke posisi tegak. Harap perbaiki secara manual.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Bantuan: Perbaiki halaman yang diputar",
        'help_rotated_pages_voice': "Bantuan untuk memperbaiki halaman yang diputar sedang dibuka.",
        'btn_help': "Bantuan",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Masalah: Halaman diputar – Penyisipan tidak berfungsi dengan benar</p>

            <p>Jika penyisipan teks, tanda tangan, atau bentuk pada halaman yang diputar tidak berfungsi dengan benar, Anda dapat memperbaiki halaman dengan editor PDF eksternal.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solusi dengan alat eksternal (mis. Pratinjau macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Ekspor halaman</strong><br>
                &nbsp;&nbsp;Klik di menu pada <strong>File → Ekspor sebagai Halaman</strong> atau gunakan metode lain untuk menyimpan halaman yang diinginkan sebagai PDF tunggal.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Buka halaman di program eksternal</strong><br>
                &nbsp;&nbsp;Buka PDF yang diekspor di editor PDF (mis. <strong>Pratinjau macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Putar halaman</strong><br>
                &nbsp;&nbsp;Putar halaman sehingga tegak (di Pratinjau: <strong>Alat → Putar</strong> atau <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Simpan</strong><br>
                &nbsp;&nbsp;Simpan halaman yang telah diperbaiki (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Sisipkan kembali halaman ke dokumen asli</strong><br>
                &nbsp;&nbsp;Kembali ke PDFDarkView dan sisipkan halaman yang telah diperbaiki di posisi yang diinginkan:<br>
                &nbsp;&nbsp;<strong>Edit → Sisipkan halaman</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatif: Putar halaman di asli</p>
                <p style="margin: 5px 0 5px 20px;">• Gunakan fungsi putar bawaan (<strong>Edit → Putar halaman</strong>) untuk memperbaiki halaman langkah demi langkah.<br>
                • Setelah setiap putaran, Anda dapat memeriksa apakah penyisipan sekarang berfungsi.<br>
                • Ini sering kali merupakan solusi yang lebih cepat – coba dulu!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tips:</strong> Jika Anda sering menemukan halaman yang diputar, Anda dapat menyembunyikan peringatan di dialog penyisipan secara permanen.<br>
                Posisi mungkin kemudian menyimpang – gunakan opsi ini hanya jika Anda mengetahui konsekuensinya.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Sejajarkan halaman",
        'menu_rotate_normalize_tooltip': "Putar halaman atau setel ulang ke 0°",
        'normalize_current_page': "Bawa halaman saat ini ke posisi tegak (setel ke 0°)",
        'normalize_all_pages': "Bawa semua halaman ke posisi tegak (setel ke 0°)",
        'page_normalized': "Halaman {0} disetel ke posisi tegak.",
        'all_pages_normalized': "Semua halaman disetel ke posisi tegak.",
        'page_already_upright': "Halaman {0} sudah tegak.",
        'all_pages_already_upright': "Semua halaman sudah tegak.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF tidak mengandung teks yang dapat dicari.</p><p>Apakah Anda ingin melakukan OCR untuk mengekspor ke {0}?</p>",
        'export_ocr_voice': "PDF tidak mengandung teks. OCR diperlukan untuk ekspor ke {0}.",
        'export_no_ocr_possible': "Ekspor tanpa OCR tidak dimungkinkan. Harap lakukan OCR melalui menu.",
        'ocr_failed_export_not_possible': "OCR gagal. Ekspor tidak dapat dilakukan.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF akan dibuka di Pratinjau. Harap mulai proses pencetakan di sana.",
        'print_preview_manual': "PDF telah dibuka. Harap jalankan perintah cetak secara manual (mis. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Gabungkan PDF",
        'merge_pdfs': "Gabungkan PDF",
        'merge_progress_title': "Menggabungkan PDF...",
        'merge_pdfs_list': "PDF dalam urutan (Seret dan lepas untuk mengurutkan)",
        'merge_add_pdf': "Tambah PDF",
        'merge_remove': "Hapus",
        'merge_move_up': "Naik",
        'merge_move_down': "Turun",
        'merge_pdfs_info': "💡 Tips: Anda dapat mengubah urutan dengan menyeret dan melepas",
        'merge_no_pdfs': "Tidak ada PDF yang dipilih. Klik 'Tambah PDF'.",
        'merge_info': "{0} PDF dipilih (sekitar {1} halaman)",
        'merge_open_file': "Buka file",
        'merge_merge': "Gabungkan",
        'merge_error': "Kesalahan saat menggabungkan",
        'merge_min_two_pdfs_error': "Harap pilih setidaknya dua file PDF untuk digabungkan.",
        'merge_select_pdfs': "Pilih PDF untuk digabungkan",
        'merge_error_file': "Kesalahan saat memproses",
        'merge_cancelled': "Penggabungan dibatalkan",
        'merge_preparing': "Mempersiapkan...",
        'merge_processing': "Memproses PDF {0} dari {1}",
        'merge_saving': "Menyimpan PDF yang digabungkan...",
        'merge_complete': "Selesai!",
        'merge_success_title': "Penggabungan berhasil",
        'merge_success_voice': "{0} PDF berhasil digabungkan.",
        'merge_success_message': "{0} PDF berhasil digabungkan.\n\nDokumen baru sekarang memiliki {1} halaman.\n\nFile baru:\n{2}\n\nLokasi penyimpanan:\n{3}\n{2}\n\nApakah Anda ingin membuka PDF ini?",
        'replace_file_title': "Ganti file?",
        'replace_file_message': "Sudah ada PDF yang terbuka. Apakah Anda ingin menggantinya dengan file baru?",
        'btn_yes': "Ya",
        'btn_no': "Tidak",
        'filename_merge_suffix': "digabungkan",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Membuka {0}...",
        'progress_merge_reading': "Membaca {0}...",
        'progress_merge_adding': "Menambahkan {0} halaman...",
        'progress_merge_optimizing': "Mengoptimalkan PDF...",
        'progress_merge_writing': "Menulis PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "menutup PDF",
        'action_close_window': "menutup jendela",
        'action_open_new_pdf': "membuka PDF baru",
        'action_quit_app': "keluar dari aplikasi",
        'changes_saved': "Perubahan telah disimpan.",
        'file_close_title': "Tutup file PDF",
        'save_before_action': "Haruskah perubahan disimpan sebelum {0}? Ya atau Tidak?",
        'save_before_action_voice': "Haruskah perubahan disimpan sebelum {0}? Ya atau Tidak?",
        'save_before_close_question': "Haruskah perubahan disimpan sebelum menutup? Ya atau Tidak?",

         # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF yang dapat dicari dibuat:\n\n{0}\n\n<b>coba lagi jika perlu",
        "ocr_rotate_title": "Sejajarkan halaman sebelum OCR",
        "ocr_rotate_question": "PDF berisi halaman yang diputar.\nApakah Anda ingin menyelaraskan semua halaman ke 0° sebelum OCR?\nIni sangat meningkatkan pengenalan teks.",
        "ocr_rotate_yes": "Ya, sejajarkan",
        "ocr_rotate_no": "Tidak, mulai OCR langsung",
        "ocr_rotate_voice": "PDF berisi halaman yang diputar. Haruskah semua halaman diselaraskan sebelum OCR?",
        "ocr_not_performed_message": "Tidak ada teks. Harap lakukan OCR (menu \"Edit\" → \"Lakukan OCR\" atau tombol Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Pengaturan OCR",
        "ocr_language_btn": "Pilih bahasa OCR",
        "ocr_language": "Bahasa OCR",
        "ocr_language_current": "Bahasa saat ini:",
        "ocr_param_info": "Informasi tentang parameter",

        "ocr_force_ocr_label": "Paksa OCR",
        "ocr_deskew_label": "Koreksi kemiringan",
        "ocr_clean_label": "Bersihkan gambar",
        "ocr_oversample_label": "Resolusi (DPI)",
        "ocr_pagesegmode_label": "Segmentasi halaman",
        "ocr_oem_label": "Mode mesin OCR",
        "ocr_optimize_label": "Kompresi PDF",
        "ocr_jobs_label": "Proses paralel",
        "ocr_verbose_label": "Detail log",

        "ocr_force_ocr_tooltip": "Paksa OCR pada setiap halaman, meskipun teks sudah ada",
        "ocr_deskew_tooltip": "Sejajarkan scan miring secara otomatis",
        "ocr_clean_tooltip": "Hapus noise dan artefak dari gambar",
        "ocr_oversample_tooltip": "Perbesar gambar sebelum OCR ke DPI ini",
        "ocr_pagesegmode_tooltip": "Menentukan bagaimana halaman dibagi menjadi area teks",
        "ocr_oem_tooltip": "Memilih mesin OCR dari Tesseract",
        "ocr_optimize_tooltip": "Tingkat kompresi PDF keluaran",
        "ocr_jobs_tooltip": "Jumlah proses OCR paralel",
        "ocr_verbose_tooltip": "Tingkat detail keluaran log",
        "ocr_settings_explain_btn": "Penjelasan",

        "ocr_force_ocr_explain": "Memaksa pengenalan teks pada <b>setiap</b> halaman, meskipun sudah berisi teks.\n\nRekomendasi: <b>Hidup</b> untuk PDF hasil scan, <b>Mati</b> untuk PDF asli dengan teks yang sudah ada.",

        "ocr_deskew_explain": "Mengoreksi scan yang sedikit miring (hingga sekitar 5°).\n\nRekomendasi: <b>Hidup</b> untuk dokumen scan, <b>Mati</b> jika halaman sudah benar-benar lurus.",

        "ocr_clean_explain": "Menghilangkan noise, titik, dan artefak kecil dari gambar.\n<b>PENTING:</b> Untuk teks Arab, Thailand, atau Vietnam dengan tanda diakritik (titik di atas/bawah huruf) opsi ini harus <b>dinonaktifkan</b>, jika tidak karakter penting dapat hilang.",

        "ocr_oversample_explain": "Memperbesar gambar <b>sebelum</b> pengenalan teks ke DPI yang ditentukan.<br><br>• <b>72-150 DPI:</b> Sangat cepat, tetapi tingkat pengenalan rendah<br>• <b>200-300 DPI:</b> Rentang optimal (Standar: 300)<br>• <b>400+ DPI:</b> Hampir tidak ada pengenalan yang lebih baik, tetapi file jauh lebih besar<br><br>Rekomendasi: 300 DPI untuk aksara kompleks (Arab, Cina, Jepang), 200 DPI untuk bahasa Barat.",

        "ocr_pagesegmode_explain": "Menentukan bagaimana Tesseract membagi halaman menjadi area teks.\n\n• <b>3 - Otomatis (Standar):</b> Baik untuk tata letak campuran\n• <b>4 - Kolom tunggal:</b> Untuk teks satu kolom\n• <b>5 - Blok vertikal:</b> Untuk aksara vertikal (Jepang, Cina)\n• <b>6 - Blok teks seragam:</b> Optimal untuk teks mengalir tanpa kolom\n• <b>11 - Gambar mentah:</b> Untuk scan buruk / tulisan tangan\n\nRekomendasi: <b>6</b> untuk dokumen teks sederhana, <b>3</b> untuk tata letak kompleks.",

        "ocr_oem_explain": "Memilih mesin OCR dari Tesseract.\n\n• <b>0 - Legacy:</b> Mesin lama (cepat, tetapi kurang akurat)\n• <b>1 - LSTM:</b> Mesin neural (lebih lambat, tetapi lebih akurat)\n• <b>2 - Legacy + LSTM:</b> Menggabungkan kedua hasil\n• <b>3 - Standar (LSTM lebih disukai):</b> Pilihan terbaik untuk sebagian besar kasus\n\nRekomendasi: <b>3</b> untuk akurasi pengenalan maksimal.",

        "ocr_optimize_explain": "Mengompresi PDF keluaran.\n\n• <b>0:</b> Tanpa optimasi (pemrosesan tercepat)\n• <b>1:</b> Optimasi ringan (kompromi yang baik)\n• <b>2:</b> Optimasi sedang\n• <b>3:</b> Optimasi kuat (file terkecil, tetapi lebih lambat)\n\nRekomendasi: <b>1</b> untuk penggunaan sehari-hari.",

        "ocr_jobs_explain": "Jumlah proses paralel untuk OCR.\n\n• <b>1:</b> Lambat, tetapi konsumsi memori terendah\n• <b>4-8:</b> Optimal untuk prosesor multi-inti modern\n• <b>12+:</b> Hampir tidak ada pemrosesan lebih cepat dengan penggunaan memori tinggi\n\nRekomendasi: Jumlah inti CPU (misalnya <b>4</b> pada sistem 4 inti).",

        "ocr_verbose_explain": "Tingkat detail keluaran log di konsol.\n\n• <b>0:</b> Tidak ada keluaran\n• <b>1:</b> Kemajuan dan pesan status\n• <b>2:</b> Keluaran terperinci\n• <b>3:</b> Keluaran debug lengkap (sangat ekstensif)\n\nRekomendasi: <b>1</b> untuk operasi normal.",

        "ocr_reset_title": "Pengaturan direset",
        "ocr_reset_message": "Semua pengaturan OCR telah direset ke nilai standar.",
        "info_tooltip": "Informasi lebih lanjut tentang parameter ini",
        "ocr_reset_defaults": "Reset ke standar",

        "ocr_psm_0": "Otomatis (mesin Legacy)",
        "ocr_psm_1": "Deteksi kolom otomatis",
        "ocr_psm_3": "Otomatis (Standar)",
        "ocr_psm_4": "Kolom tunggal",
        "ocr_psm_5": "Blok vertikal",
        "ocr_psm_6": "Blok teks seragam",
        "ocr_psm_7": "Garis teks tunggal",
        "ocr_psm_8": "Kata tunggal",
        "ocr_psm_11": "Gambar mentah (tanpa analisis tata letak)",

        "ocr_oem_0": "Mesin Legacy (cepat)",
        "ocr_oem_1": "Mesin LSTM (neural, akurat)",
        "ocr_oem_2": "Legacy + LSTM dikombinasikan",
        "ocr_oem_3": "Standar (LSTM lebih disukai)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Bahasa OCR...",
        "ocr_language_title": "Pilih bahasa OCR",
        "ocr_language_instruction": "Pilih bahasa untuk pengenalan teks (OCR).\nPerhatian: Banyak bahasa akan mengorbankan kinerja dan akurasi!\nAnda mendapatkan hasil terbaik jika hanya memilih satu bahasa.",
        "ocr_language_predefined": "Kombinasi yang ditentukan",
        "ocr_language_custom": "Kustom...",
        "ocr_language_selected": "Bahasa OCR yang dipilih",
        "ocr_language_changed": "Bahasa OCR diubah menjadi {0}",
        "ocr_language_auto_detect": "Bahasa yang tersedia dideteksi secara otomatis.",
        "ocr_language_none_found": "Tidak ada data bahasa Tesseract yang ditemukan! Harap instal paket bahasa (misalnya 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Pilihan bahasa kustom",
        "ocr_language_available": "Bahasa yang tersedia (terinstal):",
        "ocr_language_select_hint": "Pilih satu atau lebih bahasa:",
        "ocr_language_confirm": "Terapkan",
        "ocr_language_reset": "Reset ke standar (deu+eng+vie)",
        "ocr_language_priorities": "Bahasa yang direkomendasikan (pra-instal):",

        "select_all_languages": "Pilih semua",
        "clear_all_languages": "Hapus pilihan",
        "install_language_packs": "Instal paket bahasa yang hilang...",
        "install_hint": "💡 Tip: Tidak semua bahasa terinstal di sistem Anda. Melalui tombol ini Anda akan mendapatkan bantuan instalasi.",
        "ocr_language_install_title": "Instalasi paket bahasa Tesseract",

        "ocr_missing_languages": "Paket bahasa OCR yang hilang",
        "ocr_missing_languages_message": "Bahasa-bahasa yang dipilih berikut tidak terinstal di sistem Anda:\n\n{0}\n\nHarap instal paket bahasa yang hilang (lihat bantuan di 'Bantuan Instalasi').\n\nApakah Anda ingin membuka bantuan instalasi sekarang?",
        "ocr_missing_languages_voice": "Paket bahasa hilang. Harap instal bahasa yang hilang.",
        "ocr_install_help_now": "Buka bantuan",
        "ocr_continue_anyway": "Tetap coba",
        "ocr_language_error_title": "Kesalahan bahasa OCR",
        "ocr_language_error_message": "Kesalahan selama pengenalan teks: {0}\n\nHarap periksa pengaturan bahasa OCR Anda (Pengaturan → Bahasa OCR).",
        "ocr_install_help_button": "Bantuan Instalasi",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instal paket bahasa Tesseract</p>

        <p>Agar OCR dapat bekerja dalam bahasa tertentu, data bahasa yang sesuai harus diinstal di sistem Anda. Ikuti petunjuk untuk sistem operasi Anda:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Buka <strong>Terminal</strong> (Finder → Program → Utilitas → Terminal).</li>
        <li>Instal semua bahasa yang tersedia dengan:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Ini mungkin memerlukan waktu beberapa menit.)</li>
        <li>Atau hanya bahasa individual (misalnya Vietnam):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Dengan versi Homebrew saat ini, <code>*.traineddata</code> mungkin perlu diunduh secara manual (lihat di bawah).</li>
        <li>Setelah instalasi: Tutup dialog ini dan buka kembali pemilihan bahasa OCR – bahasa baru akan muncul secara otomatis.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Buka terminal (Ctrl+Alt+T).</li>
        <li>Instal bahasa yang diinginkan, misalnya untuk Vietnam:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Kode bahasa penting: <code>deu</code> (Jerman), <code>eng</code> (Inggris), <code>vie</code> (Vietnam), <code>spa</code> (Spanyol), <code>fra</code> (Prancis), <code>ita</code> (Italia), <code>nld</code> (Belanda), <code>fin</code> (Finlandia), <code>swe</code> (Swedia), <code>nor</code> (Norwegia).</li>
        <li>Tampilkan semua paket yang tersedia:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Unduh file <code>*.traineddata</code> yang diinginkan dari:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (misalnya <code>vie.traineddata</code> untuk Vietnam).</li>
        <li>Salin file ke folder bahasa Tesseract, biasanya:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Sesuaikan dengan instalasi individual.)</li>
        <li>Mulai ulang aplikasi (atau buka kembali pemilihan bahasa OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatif untuk semua sistem</p>
        <ul>
        <li>Instal <strong>OCRmyPDF</strong> dan <strong>Tesseract</strong> dengan manajer paket pilihan Anda. Sebagian besar instalasi sudah berisi beberapa bahasa standar (Inggris, Jerman, Prancis).</li>
        <li>Bahasa yang hilang dapat diinstal kapan saja – pemilihan bahasa OCR hanya mencantumkan bahasa yang benar-benar ada.</li>
        </ul>

        <hr>
        <p><b>✅ Setelah instalasi:</b> Tidak perlu memulai ulang aplikasi – bahasa yang baru ditambahkan akan segera muncul dalam daftar.</p>
        <p><b>📖 Bantuan untuk kode bahasa:</b> Daftar lengkap tersedia di <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentasi Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Font Noto Sans",
        "info_noto_font_voice": "Panduan instalasi font Noto Sans",
        "btn_info_noto_font_install": "Info font",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Cara menginstal font Noto gratis dari Google</h2>

        <p><strong>Font Noto</strong> adalah keluarga font sumber terbuka dari Google. Tujuan mereka adalah untuk tidak melihat <em>"tofu"</em> (yaitu tanpa kotak kosong □) dan menampilkan setiap karakter dari standar Unicode dengan benar. Font ini adalah pelengkap ideal untuk aplikasi yang harus menampilkan teks dalam berbagai bahasa.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalasi di macOS</h3>

        <p><strong>Metode 1: Dengan Homebrew (untuk tingkat lanjut)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metode 2: Melalui "Font Book" (Direkomendasikan)</strong></p>

        <ol>
        <li>Unduh paket font resmi:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ekstrak file ZIP</li>
        <li>Salin file ke <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalasi di Windows (10 & 11)</h3>

        <p><strong>Metode 1: Microsoft Store (Direkomendasikan)</strong><br>
        Cari "Google Noto Fonts" atau "Noto Sans" dan klik <strong>Instal</strong>.</p>

        <p><strong>Metode 2: Instalasi manual</strong></p>

        <ol>
        <li>Unduh:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ekstrak ZIP</li>
        <li>Pilih file .ttf / .otf</li>
        <li>Klik kanan → <strong>Instal</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        atau<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nama\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalasi di Linux</h3>

        <ul style='list-style: none; padding-left: 0;'>

        <li><strong>Ubuntu / Debian:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo apt update && sudo apt install fonts-noto-core fonts-noto-cjk fonts-noto-extra</pre>
        </li>

        <li><strong>Fedora:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo dnf install google-noto-sans-cjk-ttc</pre>
        </li>

        <li><strong>Arch:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo pacman -S noto-fonts noto-fonts-cjk</pre>
        </li>

        <li><strong>openSUSE:</strong>
        <pre style='background: #1e293b; padding: 0.6rem; border-radius: 0.5rem; white-space: pre-wrap; overflow-wrap: anywhere;'>sudo zypper install google-noto-fonts</pre>
        </li>

        </ul>

        <p>Verifikasi:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Kelola markah",
        "bookmark_add": "Tambah markah",
        "bookmark_add_tooltip": "Simpan halaman saat ini sebagai markah",
        "bookmark_remove": "Hapus markah",
        "bookmark_remove_tooltip": "Hapus markah yang ditandai",
        "bookmark_remove_all": "Hapus semua",
        "bookmark_remove_all_tooltip": "Hapus semua markah PDF ini",
        "bookmark_jump": "Lompat ke markah",
        "bookmark_jump_tooltip": "Lompat ke halaman yang dipilih",
        "bookmark_name": "Nama",
        "bookmark_page": "Halaman",
        "bookmark_no_bookmarks": "Tidak ada markah.\nKlik 'Tambah' untuk menyimpan halaman saat ini sebagai markah.",
        "bookmark_added": "Markah untuk halaman {0} ditambahkan: {1}",
        "bookmark_removed": "Markah dihapus: {0}",
        "bookmark_all_removed": "Semua markah telah dihapus.",
        "bookmark_name_default": "Halaman {0}",
        "bookmark_name_prompt": "Nama untuk markah:\n(teks panjang akan dipersingkat menjadi 50 karakter)",
        "bookmark_name_prompt_title": "Nama markah",
        "bookmark_confirm_remove_all": "Apakah Anda yakin ingin menghapus semua {0} markah?",
        "menu_bookmarks": "Markah",
        "bookmark_manage": "Kelola markah",
        "bookmark_next": "Markah berikutnya",
        "bookmark_prev": "Markah sebelumnya",
        "bookmark_page_display": "Halaman {0}",
        "bookmark_exists": "Markah untuk halaman ini dengan nama ini sudah ada.",
        "bookmark_select_first": "Silakan pilih markah terlebih dahulu.",
        "bookmark_confirm_remove": "Apakah Anda yakin ingin menghapus markah 'Halaman {0}: {1}'?",
        "bookmark_jumped_to": "Lompat ke markah '{0}' di halaman {1}.",
        "bookmark_jumped_to_voice": "Markah {0}, halaman {1}",
        "btn_close": "Tutup",

        "bookmark_list": "Markah Anda",
        "bookmark_rename": "Ganti nama markah",
        "bookmark_rename_tooltip": "Ubah nama markah yang dipilih",
        "bookmark_rename_title": "Ganti nama markah",
        "bookmark_rename_prompt": "Nama baru untuk markah di halaman {0}:\n(maks. 50 karakter)",
        "bookmark_renamed": "Markah '{0}' telah diganti namanya menjadi '{1}'.",
        "bookmark_item_tooltip": "Halaman {0}: {1}\nKlik dua kali untuk melompat",
        "bookmark_name_exists_question": "Markah dengan nama '{0}' sudah ada di halaman ini.\nTetap ganti nama?",

        "context_bookmarks": "Markah",
        "context_bookmark_add_here": "Tambah markah untuk halaman ini",
        "context_bookmarks_existing": "Markah yang ada:",
        "context_bookmarks_jump": "Lompat ke markah:",
        "context_bookmarks_none": "Tidak ada markah",
        "context_bookmarks_clear_all": "Hapus semua {0} markah",

        "bookmark_search_placeholder": "Cari markah... (nama atau halaman)",
        "bookmark_search_results": "Ditemukan %d markah untuk \"%s\"",
        "bookmark_no_search_results": "Tidak ada markah ditemukan untuk \"%s\"",
        "bookmark_no_search_results_label": "Tidak ada hasil untuk \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Edit metadata PDF",
        "metadata_title": "Judul",
        "metadata_title_placeholder": "Judul dokumen",
        "metadata_title_tooltip": "Judul dokumen (ditampilkan di bilah judul)",
        "metadata_author": "Penulis",
        "metadata_author_placeholder": "Nama penulis",
        "metadata_author_tooltip": "Pembuat dokumen",
        "metadata_subject": "Subjek",
        "metadata_subject_placeholder": "Subjek dokumen",
        "metadata_subject_tooltip": "Deskripsi singkat tentang konten",
        "metadata_keywords": "Kata kunci",
        "metadata_keywords_placeholder": "Kata kunci, dipisahkan dengan koma",
        "metadata_keywords_tooltip": "Kata kunci untuk mengkategorikan dokumen",
        "metadata_creator": "Pembuat",
        "metadata_creator_placeholder": "Aplikasi yang membuat PDF",
        "metadata_creator_tooltip": "Perangkat lunak yang digunakan untuk membuat dokumen",
        "metadata_producer": "Produser",
        "metadata_producer_placeholder": "Aplikasi yang mengonversi PDF",
        "metadata_producer_tooltip": "Perangkat lunak yang mengonversi PDF",
        "metadata_creation_date": "Tanggal pembuatan",
        "metadata_creation_date_tooltip": "Tanggal pembuatan dokumen",
        "metadata_mod_date": "Tanggal modifikasi",
        "metadata_mod_date_tooltip": "Tanggal modifikasi terakhir",
        "metadata_pdf_info": "📄 Informasi PDF",
        "metadata_pages": "Jumlah halaman",
        "metadata_file_size": "Ukuran file",
        "metadata_pdf_version": "Versi PDF",
        "metadata_encrypted": "Dienkripsi",
        "metadata_encrypted_yes": "Ya (dilindungi kata sandi)",
        "metadata_encrypted_no": "Tidak",
        "metadata_reload": "📂 Muat ulang dari PDF",
        "metadata_reset": "Batalkan perubahan",
        "metadata_reloaded": "Metadata telah dimuat ulang dari PDF.",
        "metadata_reset_done": "Semua bidang metadata telah direset.",
        "metadata_no_file": "Tidak ada file PDF yang dimuat.",
        "metadata_save_error": "Kesalahan saat menyimpan metadata",
        "metadata_saved": "Metadata berhasil disimpan.",
        "metadata_pdf_version_unknown": "PDF (tidak diketahui)",
        "metadata_saved_message": "Metadata berhasil disimpan.",
        "metadata_saved_voice": "Metadata disimpan.",

        "metadata_custom": "🔧 Metadata kustom",
        "metadata_custom_placeholder": "{\n  \"bidang_saya\": \"nilai_saya\",\n  \"bidang_lain\": 123\n}",
        "metadata_custom_tooltip": "Format JSON untuk metadata kustom (opsional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Template \"{0}\" dipilih - Klik dua kali untuk menyisipkan",
        "text_use_template": "Gunakan blok teks",
        "text_type": "Tipe",
        "text_search_templates": "Cari blok teks...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informasi Ekspor / Impor",
        "qsettings_export_import_info_html": """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
        body {
            margin: 0;
            padding: 16px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #2d2d2d;
            color: #f0f0f0;
            line-height: 1.5;
        }
        h3 {
            color: #FFD700;
            font-size: 20px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 15px;
            border-bottom: 2px solid #FFD700;
            padding-bottom: 8px;
        }
        h4 {
            color: #87CEEB;
            font-size: 18px;
            font-weight: bold;
            margin-top: 25px;
            margin-bottom: 10px;
        }
        ul {
            margin-top: 5px;
            margin-bottom: 15px;
            list-style-type: none;
            padding-left: 5px;
        }
        li {
            margin-bottom: 8px;
            font-size: 15px;
            line-height: 1.6;
        }
        .category {
            color: #98FB98;
            font-weight: bold;
            font-size: 16px;
            margin-right: 15px;
        }
        .detail {
            color: #FFFFFF;
            margin-left: 30px;
        }
        .checkmark {
            color: #4CAF50;
            font-weight: bold;
            margin-right: 8px;
        }
        .warning {
            color: #FF6B6B;
            font-weight: bold;
        }
        .box {
            background-color: #3a3a3a;
            border-left: 4px solid #FFD700;
            padding: 12px 16px;
            margin: 15px 0;
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.2);
        }
        .box strong {
            display: block;
            margin-bottom: 8px;
        }
        .box ul {
            margin: 5px 0 0 0;
            padding-left: 20px;
        }
        .box li {
            margin-bottom: 4px;
        }
        code {
            background-color: #444;
            padding: 4px 8px;
            border-radius: 5px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', monospace;
            font-size: 13px;
            display: inline-block;
            margin-top: 6px;
        }
        hr {
            border: none;
            border-top: 1px solid #555;
            margin: 20px 0;
        }
        </style>
        </head>
        <body>

        <h3>📦 Apa yang diekspor? (Ikhtisar)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Pengaturan aplikasi umum</span></li>
            <li class="detail">• Mode Gelap/Terang</li>
            <li class="detail">• Pembalikan mode gelap untuk gambar</li>
            <li class="detail">• Nilai ambang abu-abu</li>
            <li class="detail">• Bahasa</li>
            <li class="detail">• Geometri jendela</li>
            <li class="detail">• Mode zoom</li>
            <li class="detail">• Navigasi (Bilah navigasi terlihat)</li>
            <li class="detail">• Keluaran suara (nyala/mati)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Pengaturan cadangan</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Penamaan file (Stempel waktu, Pemisah, Akhiran)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Pengaturan untuk penyisipan</span></li>
            <li class="detail">• Tanda tangan</li>
            <li class="detail">• Teks &amp; blok teks</li>
            <li class="detail">• Tanda silang, gambar, dan bentuk</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Pengaturan OCR</span></li>
            <li class="detail">• Bahasa</li>
            <li class="detail">• Paksa OCR · Mode halaman</li>
            <li class="detail">• Pra-pemrosesan gambar: Koreksi kemiringan, Bersihkan, Oversampling</li>
            <li class="detail">• Jumlah pekerjaan paralel</li>
            <li class="detail">• Mode pembalikan</li>
            <li class="detail">• Nilai ambang abu-abu</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Markah</span></li>
            <li class="detail">• Semua markah per file PDF (Halaman, Nama, Waktu pembuatan)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Basis data kata sandi</span></li>
            <li class="detail">• Kata sandi PDF yang disimpan (opsional dienkripsi atau teks biasa)</li>
            <li class="detail">• Hash kata sandi master (jika disetel)</li>
            <li class="detail">• Data verifikasi</li>
        </ul>

        <h4>⚠️ Catatan penting</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Saat mengimpor:</strong>
            <ul>
                <li><span class="warning">➜ SEMUA pengaturan saat ini akan ditimpa sepenuhnya</span></li>
                <li>• Memulai ulang aplikasi adalah wajib</li>
                <li>• Tanda tangan, blok teks, dan markah yang ada akan diganti</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Kata sandi master dan mode ekspor:</strong>
            <ul>
                <li>• Ketika kata sandi master aktif, Anda dapat memilih:</li>
                <li>  - <span style="color: #98FB98;"><strong>Didekripsi</strong></span> (kata sandi dalam teks biasa di ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Dienkripsi</strong></span> (hanya dapat dibaca dengan kata sandi master di sistem target)</li>
                <li>• Hash kata sandi master <strong>selalu</strong> disimpan terenkripsi</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Pemberitahuan keamanan:</strong>
            <ul>
                <li>• File ZIP yang diekspor berisi data sensitif (<strong>kata sandi, markah, tanda tangan</strong>)</li>
                <li>• Harap simpan dengan aman (misalnya USB terenkripsi, pengelola kata sandi)</li>
                <li>• Jika file hilang, kata sandi PDF yang disimpan akan hilang selamanya</li>
            </ul>
        </div>

        <h4>📁 Format ekspor</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Pengaturan disimpan dalam satu file ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP ini berisi <code>settings.json</code> lengkap (dari konfigurasi Anda) serta kemungkinan file gambar tanda tangan yang disematkan dan kata sandi terenkripsi.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Tanda Tangan - Panduan",
        'signature_guide_html': """
        📝 <strong>Tanda Tangan - Panduan Singkat</strong><br>
        <ul>
        <li>Atur kata sandi master</li>
        <li>Konfigurasikan tanda tangan di menu <em>Pengaturan</em> (ukuran, stempel waktu, …)</li>
        <li>Sisipkan dengan <strong>KLIK KANAN</strong> di posisi yang diinginkan (kata sandi master diperlukan sekali per sesi)</li>
        <li>Pindahkan tanda tangan dengan mouse atau tombol panah</li>
        <li>Sisipkan beberapa tanda tangan secara berurutan</li>
        <li>Sesuaikan setiap tanda tangan secara individual</li>
        <li>Batalkan tanda tangan tunggal</li>
        <li>Simpan / batalkan semua tanda tangan sekaligus</li>
        <li>Atau, bilah menu juga dapat digunakan.</li>
        </ul>
        """,
        'signature_guide_voice': "Panduan singkat untuk tanda tangan. Atur kata sandi master. Konfigurasikan tanda tangan di pengaturan. Sisipkan dengan klik kanan.",

        'image_guide_title': "Menyisipkan Gambar - Panduan",
        'image_guide_html': """
        📷 <strong>Menyisipkan Gambar ke PDF - Panduan Singkat</strong><br>
        <ol>
        <li>Klik kanan di posisi yang diinginkan</li>
        <li><em>„Sisipkan gambar“</em> → Pilih gambar</li>
        <li>Posisikan gambar: Seret dengan mouse</li>
        <li>Sesuaikan ukuran: Seret di sudut/tepi</li>
        <li>Pertahankan rasio aspek: Tombol <strong>[A]</strong></li>
        <li>Penyesuaian lebih lanjut: Klik kanan pada gambar</li>
        </ol>
        <p><strong>Tips:</strong> Di menu konteks, Anda dapat menyesuaikan pengaturan.</p>
        """,
        'image_guide_voice': "Panduan singkat untuk gambar. Klik kanan, sisipkan gambar, pilih. Posisikan dengan mouse, sesuaikan ukuran di sudut. Rasio aspek dengan tombol A.",

        'form_guide_title': "Menyisipkan Bentuk - Panduan",
        'form_guide_html': """
        📐 <strong>Menyisipkan Bentuk ke PDF - Panduan Singkat</strong><br>
        <ol>
        <li>Pilih jenis bentuk (persegi panjang, elips, garis, panah)</li>
        <li>Klik pada posisi:
            <ul>
            <li>Untuk persegi panjang/elips: Satu klik menempatkan bentuk</li>
            <li>Untuk garis/panah: Dua klik untuk titik awal dan akhir</li>
            </ul>
        </li>
        <li>Posisikan bentuk: Seret dengan mouse</li>
        <li>Sesuaikan ukuran: Seret di sudut/tepi</li>
        <li>Simpan bentuk: <strong>Enter</strong></li>
        <li>Batalkan bentuk: <strong>ESC</strong></li>
        <li>Penyesuaian lebih lanjut: Klik kanan pada bentuk</li>
        </ol>
        <p><strong>Tips:</strong> Di menu konteks, Anda dapat menyesuaikan pengaturan.</p>
        """,
        'form_guide_voice': "Panduan singkat untuk bentuk. Pilih jenis bentuk. Untuk persegi panjang atau elips klik sekali, untuk garis atau panah klik dua kali. Posisikan dengan mouse, sesuaikan ukuran di sudut. Simpan dengan Enter, batalkan dengan Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "sebelumnya",
        "btn_next_result": "berikutnya",
        "ocr_text_window": "Jendela teks OCR",
        "bookmark_existing": "Markah yang ada",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Perbandingan OCR Mac - Windows",
        'ocr_method_mac_win_title': "Perbedaan OCR antara Mac dan Windows",
        'ocr_method_mac_win_voice': "Mac lebih baik",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Perbedaan antara macOS dan Windows</strong></p>

        <p><strong>macOS (direkomendasikan)</strong></p>
        <p>Alat:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Hasil:</p>
        <ul>
        <li>PDF yang dapat dicari dengan teks tersemat yang sebagian besar mempertahankan tata letak asli.</li>
        </ul>
        <p>Kelebihan:</p>
        <ul>
        <li>Kualitas pengenalan teks yang sangat baik (bahkan pada halaman miring).</li>
        <li>Mempertahankan grafik vektor dan font.</li>
        <li>Bilah kemajuan GUI melalui evaluasi subproses.</li>
        <li>Kontrol penuh atas semua parameter OCR (Deskew, Clean, Oversample, optimalisasi).</li>
        <li>Pencarian teks tersedia langsung di jendela utama (tampilan PDF).</li>
        </ul>
        <p>Kekurangan:</p>
        <ul>
        <li>Membutuhkan alat sistem tambahan (ocrmypdf, Ghostscript, unpaper, pngquant – termasuk dalam bundel Aplikasi).</li>
        <li>Penanganan kesalahan yang lebih kompleks (deadlock, timeouts).</li>
        </ul>

        <p><strong>Windows (alternatif stabil)</strong></p>
        <p>Alat:</p>
        <ul>
        <li>pytesseract (koneksi langsung ke Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Hasil:</p>
        <ul>
        <li>PDF yang dapat dicari yang secara visual sesuai dengan PDF gambar, tetapi dapat dicari melalui teks transparan.</li>
        </ul>
        <p>Kelebihan:</p>
        <ul>
        <li>Tidak ada yang terpikirkan saat ini.</li>
        </ul>
        <p>Kekurangan:</p>
        <ul>
        <li>PDF pada dasarnya adalah gambar dengan teks tidak terlihat; tata letak dapat sedikit menyimpang untuk dokumen kompleks (kolom, tabel).</li>
        <li>Tidak ada koreksi kemiringan otomatis (--deskew) atau pembersihan gambar (--clean).</li>
        <li>Bilah kemajuan GUI hanya diperbarui secara kasar berdasarkan jumlah halaman yang diproses.</li>
        <li>Kecepatan OCR sedikit lebih lambat (karena setiap halaman diproses secara terpisah).</li>
        <li>Pencarian teks dialihkan ke jendela teks OCR.</li>
        </ul>

        <p><strong>Kesamaan</strong></p>
        <ul>
        <li>Kedua metode menghasilkan PDF yang dapat dicari di direktori yang sama dengan file sumber.</li>
        <li>Pengaturan OCR (bahasa, DPI, mode segmentasi halaman, mode mesin OCR) dapat dikonfigurasi melalui OCRSettingsDialog dan berlaku di kedua implementasi.</li>
        </ul>

        <p><strong>Rekomendasi:</strong></p>
        <ul>
        <li>macOS: Biner ocrmypdf memberikan hasil terbaik – Belilah Mac dan gunakan versi ini (PDFDarkView untuk Mac dengan chip Apple Silicon atau Intel). Hasil OCR lebih baik daripada di Windows!</li>
        <li>Windows: Gunakan solusi pytesseract. Solusi ini stabil dan memberikan kualitas yang sepenuhnya memadai untuk sebagian besar dokumen.</li>
        </ul>

        <p><strong>Catatan penting:</strong></p>
        <ul>
        <li>Kedua versi terintegrasi sepenuhnya ke dalam antarmuka pengguna – pengguna tidak melihat perbedaan.</li>
        <li>Program secara otomatis memutuskan mesin OCR mana yang akan digunakan berdasarkan sistem operasi.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Buat tanda tangan (dari pindaian)",
        "signature_create_title": "Pilih tanda tangan yang dipindai (PDF/Gambar)",
        "image_pdf_filter": "Gambar dan PDF",
        "signature_pdf_empty": "PDF tidak berisi halaman.",
        "signature_created_success": "Tanda tangan berhasil dibuat: {0}",
        "signature_create_error": "Kesalahan saat membuat tanda tangan:\n{0}",
        "rembg_missing": "rembg tidak terinstal.\nSilakan instal: pip install rembg\nKesalahan: {0}",
        "signature_name_title": "Nama file untuk tanda tangan",
        "signature_name_message": "Silakan masukkan nama file untuk tanda tangan baru (akan disimpan sebagai PNG dengan latar belakang transparan):",
        "signature_name_label": "Nama file:",
        "signature_name_voice": "Masukkan nama file untuk tanda tangan",
        "signature_processing": "Pemrosesan berjalan...",
        "signature_creation_title": "Membuat tanda tangan",
        "signature_overwrite_warning": "File '{0}' sudah ada. Timpa?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Siapkan PDF untuk tanda tangan",
        "signature_prepare_instruction":"Silakan pilih PDF yang berisi tanda tangan yang dipindai pada satu halaman.\n\nPengenalan optimal dicapai jika:\n• Tanda tangan ditulis dengan tinta hitam (bolpoin atau spidol halus) di atas kertas putih.\n• Tanda tangan berada di sepertiga atas halaman A4 yang kosong.\n• PDF dipindai dengan setidaknya 300 dpi.\n• Tanda tangan jelas dan tidak terlalu tipis.\n• Tidak ada pola latar belakang atau garis yang mengganggu.",
        "signature_prepare_voice":"Silakan pilih PDF dengan tanda tangan yang dipindai. Perhatikan kualitas dan kontras yang baik.",
        "sig_thickness_label":"Ketebalan garis:",
        "sig_thickness_normal":"Normal (tipis)",
        "sig_thickness_bold":"Tebal (direkomendasikan)",
        "sig_thickness_very_bold":"Sangat tebal",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Menambahkan bahasa GUI dan OCR - Panduan",
        'language_guide_title': "Menambahkan bahasa GUI dan OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Unduh file terjemahan yang diinginkan <code>translations_xy.py</code> dari<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        dan letakkan di direktori berikut:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Buka peramban web Anda.</li>
        <li>Buka: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Cari di tepi kanan layar "Releases" dan pilih yang bertanda <strong>"latest"</strong>.</li>
        <li>Di halaman rilis berikutnya, unduh file <code>Source Code.zip</code> di bagian paling bawah.</li>
        <li>Ekstrak file ZIP.</li>
        <li>Cari di folder yang diekstrak semua file bahasa yang Anda butuhkan, dan salin ke direktori:<br/>
            <ul>
            <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/tessdata/</code></li>
            <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\tessdata</code></li>
            <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/tessdata</code></li>
            </ul>
        </li>
        </ol>
        </body>
        </html>
        """,

        # ============================================
        # 89. WASSERZEICHEN EINFÜGEN
        # ============================================
        "menu_watermark":"Sisipkan tanda air",
        "fullpage_text_watermark_title":"Teks sebagai tanda air",
        "fullpage_image_watermark_title":"Gambar sebagai tanda air",
        "filename_with_watermark":"_dengan_tanda_air",
        "watermark_text":"Teks:",
        "watermark_text_placeholder":"Teks tanda air Anda...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Ukuran font:",
        "watermark_format":"Pemformatan:",
        "watermark_bold":"Tebal",
        "watermark_italic":"Miring",
        "watermark_color":"Warna:",
        "watermark_choose_color":"Pilih warna...",
        "watermark_opacity":"Opasitas / Transparansi:",
        "watermark_direction":"Arah baca:",
        "watermark_direction_l_r":"Kiri → Kanan",
        "watermark_direction_bl_tr":"Bawah kiri → Atas kanan",
        "watermark_direction_tl_br":"Atas kiri → Bawah",
        "watermark_direction_b_t":"Bawah → Atas",
        "watermark_direction_t_b":"Atas → Bawah",
        "watermark_preview":"Pratinjau:",
        "watermark_preview_sample":"Teks contoh",
        "watermark_empty_text":"Silakan masukkan teks.",
        "watermark_applied":"Tanda air telah diterapkan ke semua halaman.",
        "watermark_saved":"Tanda air disimpan.",
        "image_scale":"Ukuran:",
        "image_preview":"Pratinjau gambar:",
        "no_image_selected":"Tidak ada gambar yang dipilih",
        "browse":"Jelajahi...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redaksi",
        "redact_add_black": "Redaksi (hitam)",
        "redact_add_white": "Redaksi (putih / hapus)",
        "redact_added_black": "Redaksi hitam ditambahkan",
        "redact_added_white": "Redaksi putih ditambahkan",
        "redact_apply_all": "Terapkan semua redaksi dan simpan",
        "redact_discard_all": "Batalkan semua redaksi",
        "redact_discard": "Batalkan redaksi ini",
        "no_redactions": "Tidak ada redaksi",
        "redact_confirm_title": "Terapkan redaksi secara permanen",
        "redact_confirm_message": "Peringatan: Area yang ditandai akan dihapus secara permanen (hitam atau putih).\nCadangan akan dibuat (jika diaktifkan).\n\nLanjutkan?",
        "redact_apply": "Ya, redaksi sekarang",
        "redact_saved": "{0} redaksi berhasil diterapkan dan disimpan.",
        "redact_saved_voice": "{0} redaksi diterapkan",
        "redact_error": "Kesalahan saat redaksi",
        "filename_redacted":"_direduksi",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Sisipkan nomor halaman',
        'page_numbers_format': 'Format angka:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arab)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Romawi kecil)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Romawi besar)',
        'page_numbers_format_letter': 'A, B, C ... (Huruf)',
        'page_numbers_format_custom': 'Kustom',
        'page_numbers_custom_pattern': 'Pola:',
        'page_numbers_custom_placeholder': 'mis. "Halaman {nummer}" atau "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Gunakan {nummer} untuk nomor halaman saat ini dan {total} untuk jumlah total',
        'page_numbers_position': 'Posisi:',
        'page_numbers_pos_tl': 'Atas kiri',
        'page_numbers_pos_tc': 'Atas tengah',
        'page_numbers_pos_tr': 'Atas kanan',
        'page_numbers_pos_ml': 'Tengah kiri',
        'page_numbers_pos_mc': 'Tengah',
        'page_numbers_pos_mr': 'Tengah kanan',
        'page_numbers_pos_bl': 'Bawah kiri',
        'page_numbers_pos_bc': 'Bawah tengah',
        'page_numbers_pos_br': 'Bawah kanan',
        'page_numbers_margins': 'Margin:',
        'page_numbers_margin_x': 'Jarak horizontal:',
        'page_numbers_margin_y': 'Jarak vertikal:',
        'page_numbers_range': 'Rentang halaman:',
        'page_numbers_all_pages': 'Semua halaman',
        'page_numbers_custom_range': 'Rentang kustom',
        'page_numbers_from': 'Dari:',
        'page_numbers_to': 'Sampai:',
        'page_numbers_progress': 'Menyisipkan nomor halaman...',
        'page_numbers_start': 'Memulai penyisipan nomor halaman...',
        'page_numbers_cancel': 'Penyisipan nomor halaman dibatalkan',
        'page_numbers_success': 'Nomor halaman berhasil ditambahkan.\n\nApakah Anda ingin membuka PDF baru?\n\n{0}',
        'page_numbers_complete': 'Nomor halaman ditambahkan',
        'page_numbers_error_format': 'Kesalahan saat menyisipkan nomor halaman: {0}',
        'page_numbers_content_type': 'Jenis konten:',
        'page_numbers_tab_simple': 'Angka sederhana',
        'page_numbers_tab_range': 'Halaman X dari Y',
        'page_numbers_tab_date': 'Tanggal',
        'page_numbers_tab_custom': 'Teks bebas',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Halaman {aktuell} dari {gesamt}',
        'page_numbers_range_custom': 'Kustom',
        'page_numbers_range_placeholder': 'mis. "Halaman {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format tanggal:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Januari 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Kustom',
        'page_numbers_date_placeholder': 'mis. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Posisi:',
        'page_numbers_date_before': 'Tanggal sebelum nomor halaman',
        'page_numbers_date_after': 'Tanggal setelah nomor halaman',
        'page_numbers_date_only': 'Hanya tanggal (tanpa nomor halaman)',
        'page_numbers_custom_text': 'Teks kustom:',
        'page_numbers_custom_placeholder_text': 'Gunakan {seite} untuk nomor halaman dan {gesamt} untuk total\nmis. "Rahasia - Halaman {seite}" atau "{seite} dari {gesamt}"',
        "filename_with_page_number":"_dengan_nomor_halaman",
        "filename_with_page_declaration":"_dengan_pernyataan_halaman",
        "filename_with_pagenumber":"_dengan_nomor_halaman",
        "filename_with_date":"_dengan_tanggal",
        "filename_with_my_page_declaration":"_dengan_pernyataan_halaman_kustom",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Perubahan belum disimpan",
        "unsaved_changes_message_darkmode": "Ada sisipan yang belum disimpan.\nApakah Anda ingin menyimpannya sebelum beralih?",
        "save_and_switch": "Simpan dan alihkan",
        "discard_and_switch": "Alihkan sekarang",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Ekspor halaman sebagai gambar',
        'export_images_menu': 'Ekspor sebagai gambar (PNG/JPEG)',
        'export_images_format': 'Format gambar:',
        'export_images_dpi': 'Resolusi (DPI):',
        'export_images_quality': 'Kualitas JPEG:',
        'export_images_range': 'Rentang halaman:',
        'export_images_all_pages': 'Semua halaman',
        'export_images_custom_range': 'Rentang kustom',
        'export_images_from': 'Dari:',
        'export_images_to': 'Sampai:',
        'export_images_options': 'Opsi:',
        'export_images_single_files': 'Setiap halaman sebagai file terpisah',
        'export_images_subfolder': 'Ekspor ke subfolder',
        'export_images_subfolder_info': 'Ke subfolder "namaPDF_gambar"',
        'export_images_same_folder': 'Di folder yang sama dengan PDF',
        'export_images_apply_darkmode': 'Terapkan pengaturan PDFDarkView (Mode Gelap)',
        'export_images_target_folder': 'Folder tujuan:',
        'export_images_browse': 'Jelajahi...',
        'export_images_preview': 'Pratinjau:',
        'export_images_preview_info': 'Pilih pengaturan untuk ekspor',
        'export_images_preview_info_detail': '{0} halaman sebagai {1}\nResolusi: {2} DPI\nNama file: {3}\n{4}',
        'export_images_select_folder': 'Pilih folder tujuan',
        'export_images_start': 'Memulai ekspor gambar...',
        'export_images_progress': 'Mengekspor gambar...',
        'export_images_saving': 'Menyimpan halaman {0} dari {1}...',
        'export_images_success': 'Ekspor berhasil!\n\n{0} gambar disimpan di:\n{1}',
        'export_images_complete': 'Ekspor gambar selesai',
        'export_images_open_folder': '📁 Buka folder',
        'export_images_cancel': 'Ekspor gambar dibatalkan',
        'export_images_error_format': 'Kesalahan saat mengekspor gambar: {0}',
        'export_images_pdf2image_missing': 'Pustaka "pdf2image" tidak terinstal.\n\nSilakan instal dengan:\npip install pdf2image\n\nUntuk Windows Anda juga memerlukan Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Konversi PDF/A untuk pengarsipan jangka panjang',
        'pdfa_menu': 'Konversi PDF/A (siap arsip)',
        'pdfa_info': 'Mengonversi PDF ke format PDF/A.\n\nPDF/A dirancang khusus untuk pengarsipan jangka panjang dan memastikan dokumen akan ditampilkan dengan benar di masa depan.',
        'pdfa_standard': 'Standar PDF/A:',
        'pdfa_standard_select': 'Versi:',
        'pdfa_1': 'PDF/A-1 (sederhana, kompatibel luas)',
        'pdfa_2': 'PDF/A-2 (modern, kompresi lebih baik)',
        'pdfa_3': 'PDF/A-3 (versi terbaru, mengizinkan lampiran)',
        'pdfa_standards_explanation': '📖 Penjelasan standar:\n\n'
            '• PDF/A-1: Dasar, kompatibel dengan sistem lama (sekitar 2005)\n'
            '• PDF/A-2: Lebih modern, kompresi lebih baik, dukungan transparansi (sekitar 2011)\n'
            '• PDF/A-3: Versi terbaru, mengizinkan penyematan lampiran file (sekitar 2013)\n\n'
            'Rekomendasi: PDF/A-2 adalah kompromi yang baik antara kompatibilitas dan fitur modern.',
        'pdfa_options': 'Opsi:',
        'pdfa_compress_enable': 'Kompres PDF (file lebih kecil)',
        'pdfa_metadata_preserve': 'Pertahankan metadata (judul, penulis, dll.)',
        'pdfa_target_folder': 'Folder tujuan:',
        'pdfa_browse': 'Jelajahi...',
        'pdfa_select_folder': 'Pilih folder tujuan',
        'pdfa_ocr_info_unknown': '🔍 Tidak dapat memeriksa konten teks.',
        'pdfa_ocr_info_not_needed': '✅ Teks tersedia - OCR tidak diperlukan.\nPDF/A dapat dibuat langsung.',
        'pdfa_ocr_info_recommended': '⚠️ Teks yang cukup tidak ditemukan.\n\nUntuk PDF yang dapat dicari, kami sarankan menjalankan OCR terlebih dahulu.\nCatatan: PDF/A berfungsi tanpa OCR - tetapi teks tidak akan dapat dicari.',
        'pdfa_ocr_info_error': '❌ Kesalahan saat memeriksa: {0}',
        'pdfa_start': 'Memulai konversi PDF/A...',
        'pdfa_progress': 'Konversi PDF/A sedang berlangsung...',
        'pdfa_success': 'Konversi PDF/A berhasil!\n\nDisimpan sebagai:\n{0}\n\nApakah Anda ingin membuka PDF baru?',
        'pdfa_complete': 'Konversi PDF/A selesai',
        'pdfa_cancel': 'Konversi PDF/A dibatalkan',
        'pdfa_error_format': 'Kesalahan saat konversi PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Pustaka "ocrmypdf" tidak terinstal.\n\nSilakan instal dengan:\npip install ocrmypdf',
        'btn_convert': 'Konversi',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimalkan PDF (kurangi ukuran file)',
        'optimize_menu': 'Optimalkan PDF (ukuran file)',
        'optimize_info': 'Mengurangi ukuran file PDF melalui berbagai metode optimasi.\n\nSemakin tinggi tingkat kompresi, semakin kecil file - dengan kemungkinan penurunan kualitas gambar.',
        'optimize_level': 'Tingkat kompresi:',
        'optimize_level_low': 'Rendah (cepat, penghematan kecil)',
        'optimize_level_medium': 'Sedang (kompromi baik)',
        'optimize_level_high': 'Tinggi (penghematan besar)',
        'optimize_level_maximum': 'Maksimum (penghematan maksimum, lambat)',
        'optimize_level_explanation': 'Rekomendasi: "Sedang" adalah kompromi baik antara kecepatan dan ukuran file.',
        'optimize_options': 'Opsi:',
        'optimize_compress_images': 'Kompres gambar (kurangi kualitas JPEG)',
        'optimize_clean_objects': 'Hapus objek yang tidak digunakan',
        'optimize_preserve_metadata': 'Pertahankan metadata (judul, penulis, dll.)',
        'optimize_image_quality': 'Kualitas gambar:',
        'optimize_range': 'Rentang halaman:',
        'optimize_all_pages': 'Semua halaman',
        'optimize_custom_range': 'Rentang kustom',
        'optimize_from': 'Dari:',
        'optimize_to': 'Sampai:',
        'optimize_target_folder': 'Folder tujuan:',
        'optimize_browse': 'Jelajahi...',
        'optimize_select_folder': 'Pilih folder tujuan',
        'optimize_info_box': 'Informasi',
        'optimize_info_text': 'Optimasi dapat memakan waktu beberapa menit untuk PDF besar.\n\nGambar disimpan dengan kualitas yang dikurangi, yang dapat mengurangi ukuran file secara signifikan.',
        'optimize_start': 'Memulai optimasi PDF...',
        'optimize_progress': 'Mengoptimalkan PDF...',
        'optimize_cancel': 'Optimasi PDF dibatalkan',
        'optimize_complete': 'Optimasi PDF selesai',
        'optimize_error_format': 'Kesalahan saat optimasi PDF:\n\n{0}',
        'optimize_success_message': 'Optimasi PDF berhasil!\n\nDisimpan sebagai:\n{0}\n\nSebelum: {1}\nSesudah: {2}\nPenghematan: {3:.1f}%\n\n{4}\n\nApakah Anda ingin membuka PDF yang dioptimalkan?',
        'optimize_success_message_no_size': 'Optimasi PDF berhasil!\n\nDisimpan sebagai:\n{0}\n\nInformasi ukuran tidak tersedia.\n\nApakah Anda ingin membuka PDF yang dioptimalkan?',
        'optimize_result_positive': 'File dikurangi {0:.1f}%.',
        'optimize_result_zero': 'Tidak ada perubahan ukuran file.',
        'optimize_result_negative': 'File bertambah {0:.1f}%.\nOptimasi dilewati, file asli dipertahankan.',
        'btn_optimize': 'Mulai optimasi',
        'filename_optimize_low_suffix': '_dioptimalkan_rendah',
        'filename_optimize_medium_suffix': '_dioptimalkan',
        'filename_optimize_high_suffix': '_dioptimalkan_tinggi',
        'filename_optimize_maximum_suffix': '_dioptimalkan_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Potong PDF',
        'crop_menu': 'Potong PDF (Crop)',
        'crop_range': 'Terapkan ke:',
        'crop_all_pages': 'Semua halaman',
        'crop_current_page': 'Hanya halaman saat ini',
        'crop_values': 'Nilai potong (dalam poin):',
        'crop_left': 'Kiri:',
        'crop_right': 'Kanan:',
        'crop_top': 'Atas:',
        'crop_bottom': 'Bawah:',
        'crop_presets': 'Prasetel:',
        'crop_preset_white': 'Deteksi margin putih',
        'crop_reset': 'Atur ulang',
        'crop_mouse_hint': '🖱️ Seret persegi panjang untuk memilih area secara kasar.\nKemudian Anda dapat menyesuaikan nilai dengan tepat di SpinBox.\nPenyesuaian manual dengan mouse tidak dimungkinkan.',
        'crop_apply': 'Potong',
        'crop_scope_all': 'Semua halaman',
        'crop_scope_current': 'Halaman saat ini',
        'crop_new_size': 'Ukuran baru: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Tidak ada PDF yang dimuat',
        'crop_preview_error': 'Kesalahan saat memuat pratinjau',
        'crop_start': 'Memulai pemotongan...',
        'crop_progress': 'Memotong PDF...',
        'crop_success': 'PDF berhasil dipotong!\n\nDisimpan sebagai:\n{0}\n\nApakah Anda ingin membuka PDF yang dipotong?',
        'crop_complete': 'Pemotongan selesai',
        'crop_cancel': 'Pemotongan dibatalkan',
        'crop_error_format': 'Kesalahan saat memotong:\n\n{0}',
        'filename_crop_suffix': '_dipotong',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Ratakan PDF (Flatten)',
        'flatten_menu': 'Ratakan PDF (Flatten)',
        'flatten_info': 'Meratakan PDF "membakar" semua elemen yang dapat diedit ke dalam konten halaman.\n\nSetelah itu, bidang formulir, anotasi, teks, silang, tanda tangan, gambar, dan bentuk tidak lagi dapat diedit secara individual.',
        'flatten_explanation_title': '📖 Untuk apa ini berguna?',
        'flatten_explanation_text': 'Perataan diperlukan dalam situasi berikut:\n\n'
            '• 📄 Anda ingin menyiapkan dokumen untuk dicetak\n'
            '• 🔒 Anda ingin mencegah seseorang mengubah bidang formulir\n'
            '• 📎 Anda ingin "menanamkan" anotasi dan komentar secara permanen ke dalam dokumen\n'
            '• 🖼️ Anda ingin menjangkar teks, silang, tanda tangan, gambar, dan bentuk secara permanen dalam dokumen\n'
            '• 📦 Anda ingin menyiapkan file untuk pengarsipan\n\n'
            'Perataan membuat PDF lebih kecil dan mencegah elemen dipindahkan atau dihapus secara tidak sengaja.',
        'flatten_what_title': 'Apa yang diratakan?',
        'flatten_what_list': '• ✅ Bidang formulir (bidang teks, kotak centang, tombol)\n'
            '• ✅ Anotasi (komentar, sorotan, catatan)\n'
            '• ✅ Hamparan (teks, silang, tanda tangan, gambar, bentuk)',
        'flatten_options': 'Opsi:',
        'flatten_forms': 'Ratakan bidang formulir',
        'flatten_annotations': 'Ratakan anotasi',
        'flatten_overlays': 'Ratakan hamparan (teks, silang, tanda tangan, gambar, bentuk)',
        'flatten_target_folder': 'Folder tujuan:',
        'flatten_browse': 'Jelajahi...',
        'flatten_select_folder': 'Pilih folder tujuan',
        'flatten_warning': '⚠️ Penting: Perataan adalah proses yang tidak dapat dibatalkan!\n\nSetelah perataan, elemen yang dapat diedit tidak dapat lagi diubah atau dihapus secara individual.\nBuat cadangan terlebih dahulu jika perlu.',
        'flatten_apply': 'Ratakan',
        'flatten_start': 'Memulai perataan...',
        'flatten_progress': 'Meratakan PDF...',
        'flatten_success': 'PDF berhasil diratakan!\n\nDisimpan sebagai:\n{0}\n\nApakah Anda ingin membuka PDF yang diratakan?',
        'flatten_complete': 'Perataan selesai',
        'flatten_cancel': 'Perataan dibatalkan',
        'flatten_error_format': 'Kesalahan saat meratakan:\n\n{0}',
        'filename_flatten_suffix': '_diratakan',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Hamparan PDF (Overlay)',
        'overlay_menu': 'Hamparan PDF (Overlay)',
        'overlay_info': 'Menempatkan satu PDF (hamparan) di atas PDF lain.\n\nPDF hamparan ditempatkan di atas PDF dasar. Ini berguna untuk tanda air, logo, kop surat, atau stempel.',
        'overlay_explanation_title': '📖 Untuk apa ini berguna?',
        'overlay_explanation_text': 'Hamparan diperlukan dalam situasi berikut:\n\n'
            '• 🏢 Menempatkan logo perusahaan sebagai tanda air di setiap halaman\n'
            '• 📄 Menempatkan kop surat pada PDF kosong\n'
            '• 🖊️ Menempatkan hamparan stempel pada dokumen\n'
            '• 🔖 Menempatkan tanda air pada semua halaman\n'
            '• 📑 Menempatkan hamparan formulir pada templat',
        'overlay_type': 'Jenis hamparan:',
        'overlay_type_fullpage': 'Halaman penuh (menutupi)',
        'overlay_type_transparent': 'Halaman penuh (transparan - direkomendasikan)',
        'overlay_type_stamp': 'Stempel (dapat diposisikan)',
        'overlay_type_info_fullpage': '📄 PDF hamparan ditempatkan tepat di atas seluruh halaman.\nLatar belakang putih dapat dihapus sehingga hanya konten yang terlihat.',
        'overlay_type_info_transparent': '🔍 PDF hamparan ditempatkan di atas seluruh halaman dengan latar belakang transparan.\nLatar belakang putih secara otomatis dihapus - ideal untuk tanda air dan logo!',
        'overlay_type_info_stamp': '🖊️ PDF hamparan diposisikan dan diskalakan sebagai stempel.\nSempurna untuk logo, stempel, atau tanda tangan pada posisi tertentu.',
        'overlay_remove_background': 'Hapus latar belakang putih:',
        'overlay_remove_background_enable': 'Hapus latar belakang putih dari PDF hamparan (membuat hamparan transparan)',
        'overlay_remove_background_tooltip': 'Menghapus area putih dari PDF hamparan sehingga teks di bawahnya terlihat.',
        'overlay_threshold': 'Nilai ambang:',
        'overlay_threshold_hint': '(1-254, lebih tinggi = lebih banyak putih dihapus)',
        'overlay_select_file': 'Pilih PDF hamparan:',
        'overlay_file_placeholder': 'Silakan pilih file PDF untuk hamparan',
        'overlay_browse': 'Jelajahi...',
        'overlay_select_overlay': 'Pilih PDF hamparan',
        'overlay_range': 'Rentang halaman:',
        'overlay_all_pages': 'Semua halaman',
        'overlay_custom_range': 'Rentang kustom',
        'overlay_from': 'Dari:',
        'overlay_to': 'Sampai:',
        'overlay_position': 'Posisi:',
        'overlay_position_center': 'Tengah',
        'overlay_position_top_left': 'Atas kiri',
        'overlay_position_top_right': 'Atas kanan',
        'overlay_position_bottom_left': 'Bawah kiri',
        'overlay_position_bottom_right': 'Bawah kanan',
        'overlay_size': 'Ukuran:',
        'overlay_size_original': 'Ukuran asli',
        'overlay_size_fit_page': 'Sesuaikan dengan halaman',
        'overlay_size_custom': 'Kustom (%)',
        'overlay_opacity': 'Transparansi:',
        'overlay_target_folder': 'Folder tujuan:',
        'overlay_browse_folder': 'Jelajahi...',
        'overlay_select_folder': 'Pilih folder tujuan',
        'overlay_warning': '⚠️ Catatan: PDF hamparan ditempatkan di atas PDF dasar dan "dibakar" ke dalamnya.\n\nElemen PDF hamparan tidak dapat diedit secara individual setelah disimpan.',
        'overlay_apply': 'Hamparan',
        'overlay_start': 'Memulai hamparan...',
        'overlay_progress': 'Menghampar PDF...',
        'overlay_success': 'PDF berhasil dihamparkan!\n\nDisimpan sebagai:\n{0}\n\nApakah Anda ingin membuka PDF yang dihamparkan?',
        'overlay_complete': 'Hamparan selesai',
        'overlay_cancel': 'Hamparan dibatalkan',
        'overlay_error_format': 'Kesalahan saat menghampar:\n\n{0}',
        'overlay_no_file': 'Tidak ada PDF hamparan yang dipilih.\n\nSilakan pilih file PDF untuk dihamparkan.',
        'filename_overlay_suffix': '_dihamparkan',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Ekstrak gambar dari PDF',
        'extract_images_menu': 'Ekstrak semua gambar',
        'extract_images_info': 'Mengekstrak semua gambar dari PDF dan menyimpannya sebagai file terpisah.\n\nGambar disimpan dalam format aslinya atau dikonversi ke format yang dipilih.',
        'extract_images_format': 'Format gambar:',
        'extract_images_quality': 'Kualitas JPEG:',
        'extract_images_options': 'Opsi:',
        'extract_images_subfolder': 'Ekstrak ke subfolder ("namaPDF_gambar")',
        'extract_images_unique': 'Hanya gambar unik (hindari duplikat)',
        'extract_images_range': 'Rentang halaman:',
        'extract_images_all_pages': 'Semua halaman',
        'extract_images_custom_range': 'Rentang kustom',
        'extract_images_from': 'Dari:',
        'extract_images_to': 'Sampai:',
        'extract_images_target_folder': 'Folder tujuan:',
        'extract_images_browse': 'Jelajahi...',
        'extract_images_select_folder': 'Pilih folder tujuan',
        'extract_images_info_box': 'Informasi',
        'extract_images_info_text': 'Ekstraksi dapat memakan waktu beberapa menit untuk PDF besar.\n\nGambar disimpan dengan nama aslinya (halaman_gambar).',
        'extract_images_extract': 'Ekstrak',
        'extract_images_start': 'Memulai ekstraksi...',
        'extract_images_progress': 'Mengekstrak gambar...',
        'extract_images_success': '✅ Gambar berhasil diekstrak!\n\n{0} gambar disimpan di:\n{1}',
        'extract_images_complete': 'Ekstraksi gambar selesai',
        'extract_images_cancel': 'Ekstraksi dibatalkan',
        'extract_images_error_format': 'Kesalahan saat mengekstrak gambar:\n\n{0}',
        'extract_images_open_folder': '📁 Buka folder',
        'extract_images_no_images': 'Tidak ada gambar yang ditemukan di PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Beberapa halaman dalam satu halaman (N-Up)',
        'nup_menu': 'Beberapa halaman dalam satu halaman (N-Up)',
        'nup_info': 'Mengatur beberapa halaman PDF dalam satu halaman.\n\nIdeal untuk cetakan kompak, ikhtisar, atau handout.',
        'nup_layout': 'Tata letak:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Pratinjau:',
        'nup_preview_info': '{0} halaman → {1} halaman per lembar → {2} lembar\nTata letak: {3}',
        'nup_order': 'Urutan:',
        'nup_order_horizontal': 'Horizontal (baris demi baris)',
        'nup_order_vertical': 'Vertikal (kolom demi kolom)',
        'nup_order_horizontal_reverse': 'Horizontal terbalik',
        'nup_order_vertical_reverse': 'Vertikal terbalik',
        'nup_range': 'Rentang halaman:',
        'nup_all_pages': 'Semua halaman',
        'nup_custom_range': 'Rentang kustom',
        'nup_from': 'Dari:',
        'nup_to': 'Sampai:',
        'nup_options': 'Opsi:',
        'nup_margins': 'Margin:',
        'nup_margin_between': 'Jarak antar halaman:',
        'nup_page_numbers': 'Sisipkan nomor halaman',
        'nup_target_folder': 'Folder tujuan:',
        'nup_browse': 'Jelajahi...',
        'nup_select_folder': 'Pilih folder tujuan',
        'nup_create': 'Buat',
        'nup_start': 'Memulai N-Up...',
        'nup_progress': 'Membuat N-Up...',
        'nup_success': 'N-Up berhasil dibuat!\n\nDisimpan sebagai:\n{0}\n\nApakah Anda ingin membuka PDF baru?',
        'nup_complete': 'N-Up selesai',
        'nup_cancel': 'N-Up dibatalkan',
        'nup_error_format': 'Kesalahan saat N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Ubah ukuran halaman',
        'pagesize_menu': 'Ubah ukuran halaman',
        'pagesize_info': 'Mengubah ukuran halaman PDF.\n\nKonten secara otomatis disesuaikan dengan ukuran baru.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Pilih format standar:',
        'pagesize_custom': 'Ukuran kustom:',
        'pagesize_width': 'Lebar:',
        'pagesize_height': 'Tinggi:',
        'pagesize_orientation': 'Orientasi:',
        'pagesize_portrait': 'Potret',
        'pagesize_landscape': 'Lanskap',
        'pagesize_scale_options': 'Opsi penskalaan:',
        'pagesize_fit': 'Sesuaikan (pertahankan rasio aspek)',
        'pagesize_stretch': 'Regangkan (distorsi)',
        'pagesize_center': 'Tengah (ukuran asli)',
        'pagesize_range': 'Rentang halaman:',
        'pagesize_all_pages': 'Semua halaman',
        'pagesize_custom_range': 'Rentang kustom',
        'pagesize_from': 'Dari:',
        'pagesize_to': 'Sampai:',
        'pagesize_target_folder': 'Folder tujuan:',
        'pagesize_browse': 'Jelajahi...',
        'pagesize_select_folder': 'Pilih folder tujuan',
        'pagesize_apply': 'Terapkan',
        'pagesize_start': 'Memulai perubahan ukuran halaman...',
        'pagesize_progress': 'Mengubah ukuran halaman...',
        'pagesize_success': 'Ukuran halaman berhasil diubah!\n\nDisimpan sebagai:\n{0}\n\nApakah Anda ingin membuka PDF baru?',
        'pagesize_complete': 'Perubahan ukuran halaman selesai',
        'pagesize_cancel': 'Perubahan ukuran halaman dibatalkan',
        'pagesize_error_format': 'Kesalahan saat mengubah ukuran halaman:\n\n{0}',
        'pagesize_preview_info': 'Ukuran baru: {0} x {1} pt',
        'filename_pagesize_suffix': '_ukuran_baru',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informasi PDF',
        'pdf_info_menu': 'Tampilkan informasi PDF',
        'pdf_info_voice': 'Menampilkan informasi PDF',
        'pdf_info_error': 'Kesalahan saat menampilkan informasi PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Tampilkan pintasan keyboard",
        "shortcuts_dialog_title": "Pintasan Keyboard",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FILE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Buka PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Tutup PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Simpan sebagai...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Lindungi dokumen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Cetak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Cetak segera (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Keluar dari aplikasi</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPOR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Ekspor sebagai Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Ekspor sebagai DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Ekspor sebagai TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Ekspor sebagai gambar (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Ekstrak gambar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PEMROSESAN DOKUMEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Beberapa halaman)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Konversi PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Ratakan PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Hamparan PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimalkan PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDIT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Cari</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Tambah markah</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Kelola markah</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Markah berikutnya</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Markah sebelumnya</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Jalankan OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 MANAJEMEN HALAMAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Putar halaman saat ini</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Putar semua halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalisasi halaman saat ini</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalisasi semua halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Hapus halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ekstrak halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Sisipkan halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Pindahkan halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Gabungkan PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Ubah ukuran halaman</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 SISIPKAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Sisipkan teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Sisipkan silang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Sisipkan tanda tangan 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Sisipkan tanda tangan 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Sisipkan gambar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Sisipkan persegi panjang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Sisipkan elips</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Sisipkan garis</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Sisipkan panah</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Sisipkan nomor halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Tanda air teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Tanda air gambar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDAKSI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redaksi (hitam)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redaksi (putih)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Terapkan semua redaksi</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ LANJUTAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Potong PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Edit metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ TAMPILAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Alihkan Mode Gelap/Terang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Tampilkan jendela teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Lebar halaman (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dua halaman (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Ikhtisar (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PENGATURAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Manajemen kata sandi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Pengaturan OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Pengaturan tanda tangan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Pemformatan nama file</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Ekspor pengaturan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Impor pengaturan</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMASI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Tampilkan informasi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Aktifkan/nonaktifkan output suara</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokus pada bilah menu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Versi baru tersedia",
        "update_available_message": "Ada versi baru <b>{0}</b>.\n\nKunjungi halaman rilis untuk mengunduh pembaruan:\n{1}",
        "update_available_voice": "Versi baru {0} tersedia. Silakan unduh pembaruan dari halaman GitHub.",
        "update_open_release": "Buka halaman rilis",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Unduh semua terjemahan",
        "ask_download_all_translations": """Selain bahasa Jerman, Inggris, dan Vietnam, tersedia {total_languages} bahasa GUI lainnya.\n\nApakah perlu disediakan / diperbarui?\n\nCatatan:\nBahasa yang tidak diperlukan dapat Anda hapus secara manual nanti di direktori:\n{translations_path}
        \nJika Anda membatalkan, Anda dapat mengunduh bahasa GUI nanti melalui menu 'Alat → Perbarui terjemahan'.""",
        "menu_update_translations": "Perbarui terjemahan",
        "translations_updated": "Terjemahan diperbarui",
        "translations_update_success": "{} terjemahan berhasil diperbarui ({} baru, {} diperbarui).",
        "translations_update_error": "Kesalahan saat memperbarui terjemahan",
        "translations_update_no_changes": "Semua terjemahan sudah mutakhir.",
        "translations_update_offline": "Tidak ada koneksi internet. Terjemahan tidak dapat diperbarui.",
        "translations_update_in_progress": "Terjemahan sedang diperbarui di latar belakang...",
        "translations_downloading": "Mengunduh terjemahan...",
        "translations_path_hint": "Direktori pengguna untuk terjemahan",
        "translations_update_not_available_title": "Pembaruan tidak tersedia",
        "translations_update_not_available_message": """Memperbarui terjemahan hanya tersedia dalam versi terinstal.\n\nDalam mode pengembangan, terjemahan sudah mutakhir.""",
        "translations_update_no_internet_title": "Tidak ada koneksi internet",
        "translations_update_no_internet_message": """Tidak dapat membuat koneksi internet.\n\nTerjemahan tidak dapat diunduh dari GitHub.\n\nSolusi yang mungkin:
        • Periksa koneksi internet Anda
        • Nonaktifkan sementara firewall yang mungkin aktif
        • Coba lagi nanti
        \nAnda juga dapat mengunduh terjemahan secara manual dari GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Pembaruan sedang berlangsung",
        "btn_retry": "Coba lagi",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Selamat datang di PDF Dark View",
        "welcome_title_not_supported": "Selamat datang di PDF Dark View",
        "welcome_message": "Selamat datang di PDF Dark View!\n\nBahasa sistem Anda terdeteksi sebagai '{language}'.\nApakah Anda ingin menggunakan bahasa ini untuk antarmuka pengguna?\n\nAnda dapat mengubah bahasa kapan saja melalui 'Pengaturan → Bahasa'.",
        "welcome_message_language_not_available": "Selamat datang di PDF Dark View!\n\nBahasa sistem Anda terdeteksi sebagai '{language}'.\nBahasa ini belum terinstal.\n\nApakah Anda ingin mengunduh terjemahan untuk {language} sekarang dari GitHub?\n\n(Bahasa tersebut kemudian akan digunakan secara otomatis untuk antarmuka pengguna.)",
        "welcome_message_language_not_supported": "Selamat datang di PDF Dark View!\n\nBahasa sistem Anda terdeteksi sebagai '{language}'.\nSayangnya, belum ada terjemahan untuk bahasa ini.\n\nAntarmuka pengguna akan ditampilkan dalam {fallback_language}.\n\nAnda dapat mengubah bahasa kapan saja melalui 'Pengaturan → Bahasa'.\nJika Anda mau, Anda juga dapat menyumbangkan terjemahan untuk bahasa Anda:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Ya, gunakan bahasa sistem",
        "welcome_keep_english": "Tidak, pertahankan bahasa Inggris",
        "welcome_download_language": "Ya, unduh {language}",


        # ============================================
        # 107. JALUR YANG BARU DIGUNAKAN
        # ============================================

        'menu_recent': 'Baru digunakan',
        'menu_recent_dirs': 'Direktori...',
        'menu_recent_files': 'Berkas...',
        'recent_manage': 'Kelola...',
        'recent_enable_tracking': 'Simpan jalur terbaru (privasi)',
        'recent_enable_info': 'Nonaktifkan opsi ini untuk tidak menyimpan jalur',
        'recent_tracking_disabled': 'Pelacakan jalur dinonaktifkan',
        'recent_enabled': 'diaktifkan',
        'recent_disabled': 'dinonaktifkan',
        'recent_tracking_status': 'Pelacakan jalur {0}',
        'recent_dialog_title': 'Jalur terbaru',
        'recent_tab_directories': 'Direktori',
        'recent_tab_files': 'Berkas',
        'recent_dirs_instruction': 'Klik dua kali untuk membuka dialog berkas di direktori',
        'recent_files_instruction': 'Klik dua kali untuk membuka PDF secara langsung',
        'recent_no_directories': '(tidak ada direktori yang disimpan)',
        'recent_no_files': '(tidak ada berkas yang disimpan)',
        'recent_default_current': '⭐ Bawaan: {0}',
        'recent_set_as_default': '⭐ Tetapkan sebagai bawaan',
        'recent_default_set_title': 'Direktori bawaan telah ditetapkan',
        'recent_default_set_message': 'Direktori "{0}" telah ditetapkan sebagai bawaan untuk membuka PDF.',
        'recent_default_set_voice': 'Direktori bawaan telah ditetapkan',
        'recent_directory_not_found': 'Direktori tidak ditemukan',
        'recent_file_not_found': 'Berkas tidak ditemukan',
        'recent_remove_selected': 'Hapus',
        'recent_remove_title': 'Hapus jalur',
        'recent_remove_confirm': 'Apakah Anda yakin ingin menghapus jalur "{0}" dari daftar?',
        'recent_path_removed': 'Jalur telah dihapus',
        'recent_clear_all': 'Hapus semua',
        'recent_clear_title': 'Hapus semua jalur',
        'recent_clear_confirm_type': 'Apakah Anda yakin ingin menghapus semua {0}?',
        'recent_cleared': 'Daftar telah dibersihkan',
        'recent_path_not_found_title': 'Jalur tidak ditemukan',
        'recent_path_not_found_message': 'Jalur "{0}" sudah tidak ada lagi.',
        'recent_open_file': 'Buka berkas',
        'btn_open_recent': 'Buka',
        'recent_open_file_question': 'Apakah Anda ingin membuka "{0}" sebagai PDF?',
        'recent_not_pdf': 'Berkas yang dipilih bukan PDF.',
        'recent_more_entries': 'Entri lainnya...',
        'btn_remove': 'Hapus',
        'btn_clear': 'Bersihkan semua',
        'recent_context_open': 'Buka',
        'recent_context_reveal': 'Tampilkan di Finder',
        'recent_context_set_default': '⭐ Tetapkan sebagai bawaan',
        'recent_context_open_terminal': '💻 Buka Terminal',
        'recent_context_file_info': 'Info berkas',
        'recent_context_open_with_default': '📄 Buka dengan aplikasi bawaan',
        'recent_context_remove': 'Hapus dari daftar',
        'recent_context_clear_all': 'Hapus semua',
        'recent_file_info_title': 'Informasi berkas',
        'recent_file_info_name': 'Nama',
        'recent_file_info_path': 'Jalur',
        'recent_file_info_size': 'Ukuran',
        'recent_file_info_modified': 'Diubah',
        'recent_file_info_pages': 'Halaman',
        'recent_error_reveal': 'Kesalahan saat membuka di Finder',
        'recent_error_terminal': 'Kesalahan saat membuka Terminal',
        'recent_error_info': 'Kesalahan saat mengambil info berkas',
        'open_user_data_folder': 'Tampilkan direktori data pengguna',

        # ============================================
        # 108. HAPUS HALAMAN GENAP/GANJIL
        # ============================================
        "pages_delete_even": "Hapus semua halaman genap",
        "pages_delete_odd":  "Hapus semua halaman ganjil",
        "progress_even_pages": "Menghapus halaman genap",
        "progress_odd_pages": "Menghapus halaman ganjil",
        "progress_mark_delete_even": "{} halaman genap ditandai untuk dihapus",
        "progress_mark_delete_odd":  "{} halaman ganjil ditandai untuk dihapus",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program sedang ditutup",

    }
