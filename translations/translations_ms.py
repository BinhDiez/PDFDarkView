
# ============================================
# translations_ms.py - Wörterbuch Bahasa Malaysia
# Vollständig sortiert nach Kategorien
# ============================================

def load_malay_strings():
    """Lädt alle malaysischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View oleh BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Muat PDF",
        'btn_text_window': "Teks OCR",
        'btn_first': "Halaman Pertama",
        'btn_prev': "Halaman Sebelumnya",
        'btn_next': "Halaman Seterusnya",
        'btn_last': "Halaman Terakhir",
        'btn_print': "Cetak",
        'btn_darkmode_light': "Mod Terang",
        'btn_darkmode_dark': "Mod Gelap",
        'btn_delete_pages': "Padam Halaman",
        'btn_extract_pages': "Ekstrak Halaman",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Batal",
        'btn_save': "Simpan",
        'btn_close': "Tutup",
        'btn_delete': "Padam",
        'btn_delete_all': "Padam Semua",
        'btn_copy': "Salin",
        'btn_export': "Eksport",
        'btn_show': "Tunjuk Kata Laluan",
        'btn_hide': "Sembunyi Kata Laluan",
        'btn_authenticate': "Sahkan",
        'btn_settings': "Tetapan",
        'btn_protect': "Lindungi",
        'btn_remove_password': "Alih Keluar Kata Laluan",
        'btn_manage': "Pengurusan Kata Laluan",
        'btn_retry': "Cuba Semula",
        'btn_select_all': "Pilih Semua",
        'btn_clear_selection': "Nyahpilih",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Halaman {0} daripada {1}",
        'page_count': "daripada {0}",
        'goto_page': "Pergi ke halaman",
        'page_simple': "Halaman {0}",
        'full_view_page': "Paparan penuh halaman {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Masukkan istilah carian + Enter",
        'search_results': "Keputusan: {0} daripada {1}",
        'search_nav_hint': "Enter: seterusnya (Shift+Enter: sebelumnya)",
        'search_no_results': "Tiada keputusan",
        'search_error': "Ralat carian",
        'search_active': "Medan carian diaktifkan",
        'search_closed': "Carian ditamatkan",
        'search_position': "Halaman {0} {1}",
        'search_pos_top': "paling atas",
        'search_pos_upper': "atas",
        'search_pos_middle': "tengah",
        'search_pos_lower': "bawah",
        'search_pos_bottom': "paling bawah",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Pengecaman teks berjaya diselesaikan!",
        'ocr_success_title': "OCR berjaya",
        'ocr_success_message': "Dokumen kini boleh dicari.",
        'ocr_failed': "OCR gagal",
        'ocr_in_progress': "OCR sedang diproses",
        'ocr_preparing': "Menyediakan PDF...",
        'ocr_analyzing': "Menganalisis PDF...",
        'ocr_optimizing': "Pengoptimuman imej...",
        'ocr_recognizing': "Pengecaman teks...",
        'ocr_embedding': "Membenamkan teks...",
        'ocr_finalizing': "Menyiapkan PDF...",
        'ocr_not_available': "OCR tidak tersedia",
        'ocr_install_message': "Alat OCR tidak dijumpai.\n\nSila pasang:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR diperlukan",
        'ocr_question': "PDF ini tidak mengandungi teks yang boleh dicari.\nAdakah anda ingin melakukan OCR untuk membolehkan {0}?",
        'ocr_perform': "Lakukan OCR",
        'ocr_later': "Nanti",
        'ocr_starting': "Memulakan OCR terjamin...",
        'ocr_success_voice': "OCR berjaya. PDF kini boleh dicari.",
        'ocr_partial_success': "OCR telah dijalankan, tetapi terdapat masalah semasa menggantikan.\n\nVersi boleh dicari telah disimpan di:\n{0}\n\nRalat: {1}",
        'ocr_partial_title': "OCR sebahagian berjaya",
        'ocr_partial_voice': "OCR dijalankan, tetapi penggantian gagal.",
        'original_file': "Fail asal:",
        'old_size': "Saiz lama:    {0} bait",
        'new_size': "Saiz baharu: {0} bait",
        'size_change': "Perubahan: {0}{1} bait",
        'backup_created_file': "Sandaran dibuat:\n{0}",
        'backup_not_created': "Sandaran: Tidak dibuat (tetapan dinyahaktifkan)",
        'page_header': "=== Halaman {0} ===\n{1}\n",
        'scanned_page_header': "=== Halaman {0} (imbasan) ===\n[Halaman ini hanya mengandungi teks yang diimbas]\n[Sila lakukan OCR secara manual]\n",
        'scanned_warning': "⚠️ TEKS IMBASAN - OCR DIPERLUKAN",
        'guaranteed_title': "PDF boleh dicari dibuat",
        'guaranteed_message': "<b>Versi boleh dicari terjamin telah dibuat!</b>\n\nMemandangkan OCR automatik gagal, satu\nPDF alternatif boleh dicari telah dibuat:\n\n{0}\n\n<b>Fail ini mengandungi:</b>\n• Teks yang diekstrak (jika ada)\n• Nota untuk halaman imbasan\n• Boleh dicari sepenuhnya",
        'guaranteed_voice': "PDF boleh dicari terjamin telah dibuat.",
        'instruction_title': "PANDUAN UNTUK OCR",
        'instruction_file': "Fail asal: {0}",
        'instruction_text': "Pengecaman teks automatik (OCR) gagal.\nSila lakukan OCR secara manual:\n\n1. DENGAN OCRmyPDF (baris arahan):\n   ocrmypdf --force-ocr \"[NAMAFAIL]\" \"output.pdf\"\n\n2. DENGAN ADOBE ACROBAT (macOS/Windows):\n   • Buka PDF dalam Acrobat\n   • Alatan > Edit PDF\n   • Pilih 'Pengecaman Teks'\n\n3. DENGAN PREVIEW (macOS):\n   • Buka PDF dalam Preview\n   • Fail > Eksport...\n   • Penapis Quartz: 'Kurangkan Saiz Fail'\n   • Aktifkan 'Lakukan OCR'\n\n4. PERKHIDMATAN OCR DALAM TALIAN:\n   • smallpdf.com/ms/ocr-pdf\n   • ilovepdf.com/ms/ocr-pdf\n   • adobe.com/my_en/acrobat/online/pdf-to-word.html",
        'instruction_created': "Panduan OCR telah dibuat",
        'instruction_created_message': "Panduan terperinci telah dibuat:\n\n{0}\n\nSila ikuti langkah untuk OCR manual.",
        'instruction_created_voice': "Panduan OCR telah dibuat.",
        'ocr_impossible': "OCR tidak mungkin",
        'ocr_impossible_message': "OCR tidak dapat dijalankan.\n\nSila proses '{0}' secara manual dengan perisian OCR.",
        'ocr_impossible_voice': "OCR tidak mungkin. Sila proses secara manual.",
        'emergency_title': "OCR Kecemasan",
        'emergency_message': "PDF kecemasan telah dibuat:\n\n{0}\n\nSila proses fail ini secara manual dengan OCR.",
        'emergency_voice': "PDF kecemasan dibuat. Sila lakukan OCR secara manual.",
        'critical_error': "Ralat Kritikal",
        'critical_error_message': "OCR tidak dapat dimulakan.\n\nSila mulakan semula program dan\nperiksa pemasangan OCR.",
        'critical_error_voice': "Ralat Kritikal OCR",
        'ocr_question_html': "<p>PDF ini tidak mengandungi teks yang boleh dicari.<p>Adakah anda ingin melakukan OCR untuk membolehkan <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR diperlukan. PDF tidak mengandungi teks boleh dicari. Adakah anda ingin melakukan OCR untuk membolehkan {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "tiada PDF dimuat",
        'no_pdf_message': "Tiada PDF dimuat",
        'pdf_not_found': "Fail PDF tidak dijumpai",
        'file_size': "Saiz fail",
        'bytes': "bait",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Sandaran dibuat",
        'backup_disabled': "Sandaran dinyahaktifkan",
        'backup_activated': "Penciptaan sandaran diaktifkan",
        'backup_deactivated': "Penciptaan sandaran dinyahaktifkan",
        'backup_status': "Sandaran: {0}",
        'backup_on': "✔ diaktifkan",
        'backup_off': "✘ dinyahaktifkan",
        'close_pdf': "Menutup PDF: {0}",
        'pdf_not_found_format': "Fail PDF tidak dijumpai: {0}",
        'error_pdf_load_format': "Ralat semasa memuat PDF: {0}",
        'load_failed_format': "Muat gagal:\n{0}",
        'decrypted_suffix': "(dinyahsulit)",
        'decryption_failed': "Penyahsulitan gagal.",
        'decryption_error': "Ralat semasa menyahsulit",
        'decryption_success': "Berjaya dinyahsulit",
        'decryption_success_message': "PDF telah dinyahsulit dan disimpan di:\n\n{0}",
        'decryption_success_voice': "PDF telah dinyahsulit dan disimpan.",
        'password_remove_error': "Ralat semasa mengalih keluar kata laluan",
        'save_unencrypted': "Simpan PDF tanpa penyulitan sebagai",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Simpan sebagai...",
        'save_copy': "Simpan salinan",
        'save_success': "PDF disimpan di: {0}",
        'save_encrypted': "PDF dilindungi disimpan di: {0}",
        'save_error': "PDF tidak dapat disimpan",
        'encryption_question': "Adakah anda ingin melindungi PDF dengan kata laluan?",
        'encryption_yes': "Ya",
        'encryption_no': "Tidak",
        'encryption_cancel': "Batal",
        'save_cancel': "Simpan dibatalkan",
        'save_encrypted_voice': "Fail disulitkan dan disimpan.",
        'save_success_voice': "Fail PDF telah disimpan tanpa penyulitan.",
        'save_error_format': "PDF tidak dapat disimpan:\n{0}",
        'export_pages_success': "Eksport Pages berjaya",
        'export_pages_error': "Eksport Pages gagal",
        'export_pages_error_format': "Eksport Pages gagal: {0}",
        'export_word_success': "Eksport Word berjaya",
        'export_word_error': "Eksport Word gagal",
        'export_word_error_format': "Eksport Word gagal: {0}",
        'export_text_success': "Eksport teks berjaya",
        'export_text_error': "Eksport teks gagal",
        'export_text_error_format': "Eksport teks gagal: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Kata laluan diperlukan",
        'password_enter': "Sila masukkan kata laluan",
        'password_confirm': "Sahkan kata laluan",
        'password_new': "Kata laluan baharu",
        'password_current': "Kata laluan semasa",
        'password_save': "Simpan kata laluan (disulitkan)",
        'password_saved': "✓ Kata laluan untuk fail ini disimpan",
        'password_wrong': "Kata laluan salah",
        'password_mismatch': "Kata laluan tidak sepadan",
        'password_too_short': "Kata laluan terlalu pendek",
        'password_min_length': "Kata laluan mesti sekurang-kurangnya 4 aksara",
        'password_strength': "Kekuatan kata laluan",
        'password_strength_very_weak': "Sangat lemah",
        'password_strength_weak': "Lemah",
        'password_strength_medium': "Sederhana",
        'password_strength_strong': "Kuat",
        'password_strength_very_strong': "Sangat kuat",
        'password_char_count': "({0} aksara)",
        'password_match': "✓ Sepadan",
        'password_no_match': "✗ Kata laluan tidak sepadan",
        'password_show': "Tunjuk",
        'password_hide': "Sembunyi",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Pengurusan Kata Laluan",
        'password_table_filename': "Nama fail",
        'password_table_password': "Kata laluan",
        'password_count': "{0} kata laluan disimpan",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Tiada kata laluan disimpan",
        'password_copied': "{0} kata laluan disalin",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Adakah anda pasti mahu memadam kata laluan untuk '{0}'?",
        'password_delete_multiple': "Adakah anda pasti mahu memadam {0} kata laluan yang dipilih?",
        'password_delete_all_confirm': "Adakah anda pasti mahu memadam kesemua {0} kata laluan yang disimpan?",
        'password_deleted': "{0} kata laluan telah dipadamkan",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Semua kata laluan telah dipadamkan",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Penjana Kata Laluan",
        'generator_generated': "Kata laluan yang dijana:",
        'generator_regenerate': "Jana semula",
        'generator_copy': "Salin",
        'generator_use': "Guna",
        'generator_settings': "Tetapan",
        'generator_length': "Panjang:",
        'generator_group_every': "Pemisah setiap",
        'generator_group_chars': "aksara. Pemisah:",
        'generator_uppercase': "Huruf besar (A-Z)",
        'generator_lowercase': "Huruf kecil (a-z)",
        'generator_digits': "Nombor (0-9)",
        'generator_symbols': "Simbol khas (!@#$%^&*)",
        'generator_exclude': "Dikecualikan:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Kata Laluan Induk diperlukan",
        'master_password_setup': "Sediakan Kata Laluan Induk",
        'master_password_change': "Tukar Kata Laluan Induk",
        'master_password_enter': "Sila masukkan Kata Laluan Induk anda",
        'master_password_choose': "Pilih Kata Laluan Induk yang kukuh (sekurang-kurangnya 8 aksara)",
        'master_password_new': "Sila masukkan Kata Laluan Induk baharu anda",
        'master_password_confirm': "Sahkan kata laluan",
        'master_password_authenticate': "Sahkan",
        'master_password_success': "Kata Laluan Induk berjaya disediakan.",
        'master_password_changed': "Kata Laluan Induk berjaya ditukar.",
        'master_password_removed': "Kata Laluan Induk dan semua kata laluan telah dipadamkan.",
        'master_password_remove': "Alih keluar Kata Laluan Induk",
        'master_password_remove_confirm': "Adakah anda PASTI mahu memadam SEMUA kata laluan?\n\nTindakan ini TIDAK BOLEH DIUNDUR!",
        'master_password_export_before': "Adakah anda ingin mengeksport sandaran terlebih dahulu?",
        'master_password_export_delete': "Eksport & padam",
        'master_password_delete_now': "Padam sekarang",
        'master_password_for_signatures': "Untuk menggunakan tandatangan, anda perlu menyediakan Kata Laluan Induk.\n\nAdakah anda ingin menyediakan Kata Laluan Induk sekarang?",
        'master_password_for_private': "Untuk menggunakan blok teks peribadi, anda perlu menyediakan Kata Laluan Induk.\n\nAdakah anda ingin menyediakan Kata Laluan Induk sekarang?",
        'master_password_info': """
            <b>🔐 TANPA KATA LALUAN INDUK:</b><br>
            • Paparan, salinan dan eksport kata laluan tidak dibenarkan<br>
            • Pemadaman kata laluan sentiasa dibenarkan (walaupun tanpa Kata Laluan Induk)<br><br>

            <b>🔐 DENGAN KATA LALUAN INDUK:</b><br>
            • Semua fungsi tersedia selepas pengesahan<br>
            • Kata laluan disulitkan dengan Kata Laluan Induk<br>
            • Panjang minimum: 8 aksara<br>
            • Penyimpanan hash SHA-256 yang selamat<br><br>

            <b>PENTING:</b><br>
            • Jika Kata Laluan Induk hilang: kata laluan tidak boleh dipulihkan<br>
            • Apabila mengalih keluar Kata Laluan Induk: SEMUA kata laluan akan dipadamkan<br>
            • Pilihan eksport tersedia sebelum pemadaman<br>
            • Kata Laluan Induk boleh diubah pada bila-bila masa
        """,
        'signature_auth_disabled': "Nyahaktifkan pertanyaan kata laluan untuk tandatangan",
        'template_auth_disabled': "Nyahaktifkan pertanyaan kata laluan untuk blok teks peribadi",
        'master_password_for_signatures_settings': "Untuk menggunakan tandatangan, anda perlu menyediakan Kata Laluan Induk.\n\nSila pergi ke Tetapan - Pengurusan Kata Laluan",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Lindungi PDF",
        'protect_info': "Fail '{0}' akan dilindungi dengan kata laluan.",
        'protect_instruction': "Sila masukkan kata laluan yang dikehendaki dua kali untuk melindungi dokumen, atau gunakan penjana kata laluan di sebelah kanan medan input.",
        'protect_success': "PDF berjaya dilindungi dan disimpan di:\n{0}\n\nKata laluan: {1}\n\nAdakah anda ingin membuka PDF yang dilindungi sekarang?",
        'protect_open': "Ya",
        'protect_skip': "Tidak",
        'protect_error': "Ralat semasa melindungi PDF",
        'protect_open_title': "Buka PDF yang dilindungi",
        'protect_question': "Selesai. Adakah anda ingin membuka PDF yang dilindungi sekarang? Ya atau Tidak?",
        'password_cancel': "Dialog kata laluan dibatalkan",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Padam halaman",
        'pages_extract': "Ekstrak halaman",
        'pages_insert': "Sisip halaman",
        'pages_move': "Alih halaman",
        'pages_delete_options': "Pilihan pemadaman",
        'pages_delete_empty': "Padam semua halaman kosong",
        'pages_delete_current': "Padam halaman semasa",
        'pages_delete_range': "Padam julat halaman",
        'pages_extract_options': "Pilihan pengekstrakan",
        'pages_extract_current': "Ekstrak halaman semasa",
        'pages_extract_range': "Ekstrak julat halaman",
        'pages_insert_position': "Kedudukan sisipan",
        'pages_insert_before': "Sisip sebelum halaman:",
        'pages_insert_select': "Pilih PDF",
        'pages_insert_none': "Tiada PDF dipilih",
        'pages_move_source': "Halaman untuk dialihkan",
        'pages_move_from': "Dari halaman:",
        'pages_move_to': "Sehingga halaman:",
        'pages_move_target': "Kedudukan sasaran",
        'pages_move_before': "Alih sebelum halaman:",
        'pages_move_hint': "Petunjuk: halaman 1 = awal, {0} = akhir",
        'pages_range_invalid': "Halaman mula mestilah kurang daripada atau sama dengan halaman akhir.",
        'pages_position_invalid': "Kedudukan sasaran tidak boleh berada dalam julat yang dialihkan.",
        'pages_no_pdf_selected': "Tiada PDF dipilih.",
        'pages_deleted': "Sebanyak {0} halaman telah dipadamkan.",
        'pages_extracted': "Diekstrak: {0}\nDisimpan di: {1}\nSaiz fail: {2:.1f} KB",
        'pages_inserted': "{0} halaman disisipkan",
        'pages_moved': "Sebanyak {0} halaman telah dialihkan.",
        'pages_deleted_none': "Tiada halaman dipadamkan.",
        'pages_delete_progress': "Memadam halaman...",
        'pages_deleted_with_backup': "Sebanyak {0} halaman telah dipadamkan.\n\nSandaran: {1}",
        'pages_deleted_voice': "Sandaran telah dibuat dan {0} halaman dipadamkan.",
        'info': "Nota",
        'error_dialog_creation': "Dialog tidak dapat dibuat",
        'extract_page_single': "Ekstrak halaman {0}",
        'extract_page_range': "Ekstrak halaman {0}-{1}",
        'extract_success_voice': "Halaman berjaya diekstrak",
        'extract_error_format': "Ralat semasa mengekstrak: {0}",
        'pages_inserted_voice': "Sebanyak {0} halaman telah disisipkan.",
        'insert_error_format': "Ralat semasa menyisip: {0}",
        'pages_move_progress': "Mengalih halaman...",
        'pages_moved_with_backup': "Sebanyak {0} halaman telah dialihkan.\n\nSandaran: {1}",
        'move_success_title': "Berjaya dialihkan",
        'pages_moved_voice': "{0} halaman berjaya dialihkan",
        'mark_removed': "Tanda dari halaman {0} dialih keluar",
        'mark_empty': "Halaman {0} ditandakan sebagai kosong",
        'mark_export_removed': "Tanda eksport dari halaman {0} dialih keluar",
        'mark_export': "Halaman {0} ditandakan untuk eksport",
        'no_empty_pages': "Tiada halaman kosong ditandakan untuk dipadam",
        'delete_empty_confirm': "Adakah anda mahu memadam semua {0} halaman kosong yang ditandakan?",
        'delete_empty_confirm_voice': "Padam sekarang semua {0} halaman kosong yang ditandakan? Ya atau Tidak.",
        'empty_pages_deleted': "{0} halaman kosong dipadamkan",
        'no_export_pages': "Tiada halaman ditandakan untuk eksport",
        'overwrite_title': "Ganti fail sedia ada",
        'overwrite_question': "Fail\n\n{0}\n\nsudah wujud.\nAdakah anda mahu menggantikannya?",
        'overwrite_voice': "Ganti fail yang sedia ada? Ya atau Tidak.",
        'page_skipped': "Halaman {0} telah dilangkau",
        'export_complete': "Eksport selesai.",
        'export_complete_voice': "Eksport telah selesai.",
        'no_pages_exported': "Tiada halaman dieksport",
        'export_cancelled': "Eksport dibatalkan",
        'pages_exported': "{0} halaman dieksport ke {1}",
        'export_page_title': "Eksport halaman",
        'page_exported': "Halaman {0} dieksport ke {1}",
        'export_error': "Ralat semasa eksport",
        'export_marked_title': "Eksport halaman bertanda",
        'rotate_all_title': "putar semua halaman",
        'rotate_all_question': "Adakah anda mahu memutar semua halaman 90 darjah ke kanan?",
        'rotate_all_voice': "Adakah anda mahu memutar semua halaman 90 darjah ke kanan? Ya atau Tidak?",
        'all_pages_rotated': "Semua halaman diputar",
        'page_rotated': "Halaman {0} diputar",
        'rotate_error': "Halaman tidak dapat diputar",
        'delete_page_confirm': "Adakah anda mahu memadam halaman {0}?",
        'delete_page_confirm_voice': "Adakah anda pasti mahu memadam halaman {0}? Ya atau Tidak.",
        'page_deleted': "Halaman {0} dipadamkan",
        'delete_error': "Halaman tidak dapat dipadamkan",
        'pages_deleted_voice': "{0} halaman dipadamkan",
        'pages_exported_split': "{0} halaman telah berjaya dieksport.",
        'pages_skipped': "{0} halaman telah dilangkau.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Ekstrak halaman (lanjutan)",
        'pdf_splitter_title': "Pembahagi & Pengekstrak PDF",
        'pdf_splitter_load': " Pilih fail PDF",
        'pdf_splitter_info': "Sila pilih satu pilihan untuk dokumen PDF anda",
        'pdf_splitter_basic': "Operasi asas",
        'pdf_splitter_single': "Bahagikan kepada halaman individu",
        'pdf_splitter_range': "Ekstrak halaman:",
        'pdf_splitter_range_placeholder': "cth. 1-3,5,7-9",
        'pdf_splitter_clean': "Operasi pembersihan",
        'pdf_splitter_remove_empty': "Alih keluar semua halaman kosong",
        'pdf_splitter_remove': "Padam julat halaman:",
        'pdf_splitter_remove_placeholder': "cth. 2,4-6",
        'pdf_splitter_process': "Proses PDF",
        'pdf_splitter_loaded': "PDF dimuat. Sila pilih satu pilihan",
        'pdf_read_error': "PDF tidak dapat dibaca",
        'pages': "Halaman",
        'pages_created': "Halaman telah dibuat",
        'range_empty': "Sila masukkan julat halaman",
        'range_invalid': "Julat halaman tidak sah",
        'range_created': "PDF baharu dengan halaman yang dipilih telah dibuat:\n{0}",
        'empty_removed': "{0} halaman kosong dialih keluar.\nOutput: {1}",
        'remove_empty': "Sila masukkan halaman untuk dialih keluar",
        'remove_invalid': "Halaman untuk dialih keluar tidak sah",
        'remove_done': "PDF yang telah dibersihkan dibuat:\n{0}",
        'open_folder': "Buka folder",
        'show_in_finder': "Tunjukkan dalam Finder",
        'pdf_splitter_no_pdf': "Sila muatkan fail PDF terlebih dahulu.",
        'process_error': "Ralat semasa memproses PDF",
        'pages_created_voice': "{0} halaman telah dibuat",
        'range_created_voice': "PDF dengan halaman yang dipilih telah dibuat",
        'empty_removed_voice': "{0} halaman kosong telah dialih keluar",
        'remove_done_voice': "PDF yang telah dibersihkan telah dibuat",
        'pdf_splitter_split_groups': "Setiap kumpulan berterusan ke dalam fail berasingan",
        'range_created_single': "PDF baharu dibuat:\n{0}",
        'range_created_multiple': "{0} fail PDF telah dibuat.",
        'range_created_voice_single': "Satu PDF dengan halaman yang dipilih telah dibuat",
        'range_created_voice_multiple': "{0} fail PDF telah dibuat",
        'empty_removed_none_left': "Tiada halaman tinggal",
        'empty_removed_all_empty': "Semua halaman dikesan sebagai kosong dan akan dialih keluar. Tiada fail dibuat.",
        'preview_single': "Pratonton: {0}",
        'preview_enter_range': "Sila masukkan julat halaman.",
        'preview_invalid_range': "Julat halaman tidak sah.",
        'preview_file': "Pratonton: {0}",
        'preview_files': "Pratonton: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Memulakan pencetakan",
        'print_sent': "Tugasan cetak dihantar",
        'print_now': "Cetak sekarang",
        'print_error': "Ralat semasa mencetak segera",
        'print_limited': "Fungsi cetakan terhad pada sistem ini",
        'print_error_format': "Ralat semasa mencetak segera: {0}",
        'warning': "Amaran",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Tukar ke Mod Terang",
        'mode_switch_to_dark': "Tukar ke Mod Gelap",
        'mode_dark_activated': "Mod Gelap diaktifkan",
        'mode_light_activated': "Mod Terang diaktifkan",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Paparan penuh",
        'zoom_two_pages': "Dua halaman bersebelahan",
        'zoom_overview': "Mod gambaran keseluruhan",
        'zoom_cannot_during_search': "Zum tidak boleh dilakukan semasa carian",
        'zoom_exit_first': "Sila tamatkan zum terlebih dahulu",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop diaktifkan",
        'drag_disabled': "Drag & Drop dinyahaktifkan",
        'drag_page_grab': "Halaman {0} diambil",
        'drag_page_dropped': "Halaman {0} disisipkan pada kedudukan {1}",
        'drag_position_invalid': "Kedudukan tidak sah",
        'drag_same_position': "Halaman {0} kekal pada kedudukan {0}",
        'drag_error': "Ralat semasa mengalih",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Input teks dengan pemformatan lanjutan dan pengurusan blok teks",
        'text_templates': "Blok teks tersedia:",
        'text_name': "Nama",
        'text_preview': "Pratonton teks",
        'text_enter': "Teks:",
        'text_font_size': "Saiz fon:",
        'text_formatting': "Pemformatan:",
        'text_bold': "Tebal",
        'text_italic': "Condong",
        'text_underline': "Garis bawah",
        'text_alignment': "Penjajaran:",
        'text_left': "Kiri",
        'text_center': "Tengah",
        'text_right': "Kanan",
        'text_color': "Warna teks:",
        'text_opacity': "Kelegapan:",
        'text_word_wrap': "Pembalut teks:",
        'text_auto': "Automatik",
        'text_page_width_95': "Lebar halaman (95%)",
        'text_page_width_85': "Sangat lebar (85%)",
        'text_page_width_75': "Lebar (75%)",
        'text_page_width_60': "Lebar sederhana (60%)",
        'text_page_width_50': "Sederhana (50%)",
        'text_page_width_30': "Sempit (30%)",
        'text_page_width_20': "Lebih sempit (20%)",
        'text_page_width_10': "Sangat sempit (10%)",
        'text_no_wrap': "Tiada pembalut",
        'text_private': "Blok teks peribadi (memerlukan pengesahan)",
        'text_preview_label': "Pratonton:",
        'text_preview_placeholder': "Pratonton teks akan dipaparkan di sini...",
        'text_no_text': "(Tiada teks)",
        'text_save_template': "💾 Simpan sebagai blok",
        'text_delete_template': "🗑 Padam blok teks yang dipilih",
        'text_show_private': "Tunjuk peribadi",
        'text_hide_private': "Sembunyi peribadi",
        'text_use': "✅ Guna teks",
        'text_saved': "Blok teks disimpan sebagai:\n{0}",
        'text_saved_voice': "Blok teks disimpan",
        'text_deleted': "Blok teks dipadamkan",
        'text_no_text_to_save': "Tiada teks untuk disimpan.",
        'text_no_templates': "Tiada blok teks dijumpai",
        'text_private_master_required': "Blok peribadi hanya boleh digunakan jika Kata Laluan Induk disediakan.\n\nAdakah anda ingin menyediakan Kata Laluan Induk sekarang?",
        'text_filename': "Nama fail untuk blok teks (tanpa 'Text_' dan '.txt'):",
        'text_filename_hint': "Contoh: 'Telefon Pejabat' akan disimpan sebagai 'Text_Telefon Pejabat.txt'",
        'text_save_hint': "Blok teks akan disimpan secara automatik dengan pemformatan.",
        'text_guide_title': "Input Teks - Panduan",
        'text_delete_confirm': "Adakah anda pasti mahu memadam blok teks ini?\n\nFail: {0}\nTeks: {1}...",
        'text_make_public': "Tandakan sebagai awam",
        'text_make_private': "Tandakan sebagai peribadi",
        'text_privacy_changed': "Status privasi ditukar",
        'text_private_always': "Peribadi sentiasa kelihatan (tetapan)",
        'text_mode_required': "Sila aktifkan mod teks terlebih dahulu",
        'text_continue_editing': "Teruskan mengedit - Kursor di hujung teks",
        'text_no_input': "Tiada teks dimasukkan - teks dibuang",
        'save_dialog_question': "Bagaimana anda mahu meneruskan?",
        'text_save_question': "Simpan semua teks dan pangkah, laraskan, teruskan edit atau buang?",
        'copy_cross': "Pangkah disalin",
        'paste_cross': "Pangkah ditampal",
        'paste_text': "Teks ditampal",
        'cross_discarded': "Pangkah dibuang",
        'all_discarded': "Semua dibuang",
        'text_discarded': "Teks dibuang",
        'no_texts_to_save': "Tiada teks untuk disimpan",
        'no_valid_texts': "Tiada teks sah untuk disimpan",
        'text_word_singular': "Teks",
        'text_word_plural': "Teks",
        'cross_word_singular': "Pangkah",
        'cross_word_plural': "Pangkah",
        'texts_saved_title': "Teks disimpan",
        'texts_crosses_saved': "{0} {1} dan {2} {3} telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'texts_crosses_saved_voice': "{0} {1} dan {2} {3} disimpan.",
        'texts_saved': "{0} {1} telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'texts_saved_voice': "{0} {1} disimpan.",
        'crosses_saved': "{0} {1} telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'crosses_saved_voice': "{0} {1} disimpan.",
        'elements_saved': "{0} elemen telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'elements_saved_voice': "{0} elemen disimpan.",
        'text_window_load_error': "Tetingkap teks tidak dapat dimuatkan",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Input Teks dan Blok Teks – Panduan Terperinci**

        **1. Menyisip dan mengedit teks**
        - Klik kanan pada lokasi yang dikehendaki dalam dokumen dan pilih "Sisip teks".
        - Dialog akan dibuka di mana anda boleh memasukkan dan memformat teks anda:
        • Saiz fon, Tebal, Condong, Garis bawah
        • Warna teks (boleh dipilih bebas)
        • Transparensi (kelegapan) melalui gelangsar
        • Pembalut teks (pelbagai lebar, cth. lebar halaman, sempit, tiada pembalut)
        - Selepas pengesahan, teks akan muncul di lokasi klik. Anda boleh mengalihkannya dengan tetikus atau kekunci anak panah.
        - Klik dua kali pada teks membuka mod edit; ESC untuk keluar.

        **2. Mengurus blok teks (Templat)**
        - Dalam dialog teks, anda akan melihat senarai semua blok teks yang disimpan di sebelah kiri.
        - **Menyimpan blok:** Masukkan teks anda, formatkannya dan klik pada "💾 Simpan sebagai blok". Masukkan nama fail (tanpa sambungan).
        - **Memuat blok:** Klik pada nama yang dikehendaki dalam senarai. Teks dan pemformatan akan diambil dan boleh disesuaikan jika perlu.
        - **Memadam:** Dengan klik kanan pada blok, anda boleh memadamkannya atau menukar status privasinya.

        **3. Blok teks peribadi (Kata Laluan Induk)**
        - Jika anda telah menyediakan Kata Laluan Induk (di bawah Tetapan → Pengurusan Kata Laluan), anda boleh menandakan blok sebagai "peribadi".
        - Aktifkan kotak semak "Blok teks peribadi" dalam dialog sebelum menyimpan.
        - Blok peribadi hanya akan dipaparkan dalam senarai jika anda telah memasukkan Kata Laluan Induk sekali setiap sesi (pengesahan melalui simbol kunci atau pada akses pertama).
        - Dengan ini, anda boleh melindungi blok teks sulit daripada akses orang lain.

        **4. Menyisip pangkah**
        - Melalui menu konteks, anda juga boleh menyisipkan pangkah grafik (contohnya untuk kotak semak).
        - Saiz, ketebalan garis dan warna pangkah boleh dilaraskan secara global dalam tetapan (Menu "Tetapan" → "Tetapan Pangkah").
        - Dengan klik kanan pada pangkah yang sedia ada, anda boleh mengubahnya secara individu.

        **5. Tindakan berkumpulan**
        - Jika anda telah meletakkan beberapa teks atau pangkah pada satu halaman, anda boleh menyimpan atau membuang semua elemen bersama-sama melalui menu konteks (klik kanan dalam mod teks).
        - Apabila disimpan, semua elemen akan dibenamkan ke dalam PDF dan dikekalkan sebagai grafik vektor.

        **6. Pintasan papan kekunci dalam mod teks**
        - Kekunci anak panah: Alih elemen
        - Ctrl+Kekunci anak panah: Langkah lebih besar
        - Enter: Buka dialog simpan (simpan semua / laraskan / buang)
        - ESC: Buang elemen semasa
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Input Teks dan Blok Teks – Panduan Terperinci</strong></p>

        <p><strong>1. Menyisip dan mengedit teks</strong></p>
        <ul>
        <li>Klik kanan pada lokasi yang dikehendaki dalam dokumen dan pilih "Sisip teks".</li>
        <li>Dialog akan dibuka di mana anda boleh memasukkan dan memformat teks anda:<br/>
        • Saiz fon, Tebal, Condong, Garis bawah<br/>
        • Warna teks (boleh dipilih bebas)<br/>
        • Transparensi (kelegapan) melalui gelangsar<br/>
        • Pembalut teks (pelbagai lebar, cth. lebar halaman, sempit, tiada pembalut)</li>
        <li>Selepas pengesahan, teks akan muncul di lokasi klik. Anda boleh mengalihkannya dengan tetikus atau kekunci anak panah.</li>
        <li>Klik dua kali pada teks membuka mod edit; ESC untuk keluar.</li>
        </ul>

        <p><strong>2. Mengurus blok teks (Templat)</strong></p>
        <ul>
        <li>Dalam dialog teks, anda akan melihat senarai semua blok teks yang disimpan di sebelah kiri.</li>
        <li><strong>Menyimpan blok:</strong> Masukkan teks anda, formatkannya dan klik pada "💾 Simpan sebagai blok". Masukkan nama fail (tanpa sambungan).</li>
        <li><strong>Memuat blok:</strong> Klik pada nama yang dikehendaki dalam senarai. Teks dan pemformatan akan diambil dan boleh disesuaikan jika perlu.</li>
        <li><strong>Memadam:</strong> Dengan klik kanan pada blok, anda boleh memadamkannya atau menukar status privasinya.</li>
        </ul>

        <p><strong>3. Blok teks peribadi (Kata Laluan Induk)</strong></p>
        <ul>
        <li>Jika anda telah menyediakan Kata Laluan Induk (di bawah Tetapan → Pengurusan Kata Laluan), anda boleh menandakan blok sebagai "peribadi".</li>
        <li>Aktifkan kotak semak "Blok teks peribadi" dalam dialog sebelum menyimpan.</li>
        <li>Blok peribadi hanya akan dipaparkan dalam senarai jika anda telah memasukkan Kata Laluan Induk sekali setiap sesi (pengesahan melalui simbol kunci atau pada akses pertama).</li>
        <li>Dengan ini, anda boleh melindungi blok teks sulit daripada akses orang lain.</li>
        </ul>

        <p><strong>4. Menyisip pangkah</strong></p>
        <ul>
        <li>Melalui menu konteks, anda juga boleh menyisipkan pangkah grafik (contohnya untuk kotak semak).</li>
        <li>Saiz, ketebalan garis dan warna pangkah boleh dilaraskan secara global dalam tetapan (Menu "Tetapan" → "Tetapan Pangkah").</li>
        <li>Dengan klik kanan pada pangkah yang sedia ada, anda boleh mengubahnya secara individu.</li>
        </ul>

        <p><strong>5. Tindakan berkumpulan</strong></p>
        <ul>
        <li>Jika anda telah meletakkan beberapa teks atau pangkah pada satu halaman, anda boleh menyimpan atau membuang semua elemen bersama-sama melalui menu konteks (klik kanan dalam mod teks).</li>
        <li>Apabila disimpan, semua elemen akan dibenamkan ke dalam PDF dan dikekalkan sebagai grafik vektor.</li>
        </ul>

        <p><strong>6. Pintasan papan kekunci dalam mod teks</strong></p>
        <ul>
        <li>Kekunci anak panah: Alih elemen</li>
        <li>Ctrl+Kekunci anak panah: Langkah lebih besar</li>
        <li>Enter: Buka dialog simpan (simpan semua / laraskan / buang)</li>
        <li>ESC: Buang elemen semasa</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Tetapan Pangkah",
        'cross_properties': "Sifat Pangkah",
        'cross_size': "Saiz (px):",
        'cross_line_width': "Ketebalan garis:",
        'cross_color': "Warna:",
        'cross_choose_color': "Pilih",
        'cross_fine_tuning': "Pelarasan halus semasa menyimpan (piksel)",
        'cross_offset_x': "Ofset X:",
        'cross_offset_y': "Ofset Y:",
        'cross_offset_x_tooltip': "Nilai negatif mengalihkan pangkah ke kiri semasa menyimpan, positif ke kanan",
        'cross_offset_y_tooltip': "Nilai negatif mengalihkan pangkah ke atas semasa menyimpan, positif ke bawah",
        'cross_preview': "Pratonton",
        'cross_save': "Guna tetapan",
        'cross_customized': "Pangkah dilaraskan",
        'cross_settings_applied': "Tetapan pangkah disimpan.\nSaiz: {0}px, Ketebalan garis: {1}px\n{2}",
        'cross_updated_count': "{0} pangkah sedia ada telah dikemas kini.",
        'cross_no_crosses': "Tiada pangkah sedia ada dijumpai.",
        'cross_settings_applied_all': "Tetapan pangkah untuk semua {0} pangkah telah digunakan",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Tetapan Tandatangan",
        'signature_1': "Tandatangan 1",
        'signature_2': "Tandatangan 2",
        'signature_select': "Pilih tandatangan",
        'signature_add': "➕ Tambah tandatangan baharu...",
        'signature_size': "Saiz untuk tandatangan {0} (%):",
        'signature_common': "Tetapan am",
        'signature_timestamp': "Tambah cap masa secara automatik",
        'signature_location': "Lokasi standard:",
        'signature_timestamp_size': "Saiz fon cap masa:",
        'signature_no_files': "-- Tiada tandatangan dijumpai --",
        'signature_insert': "Sisip tandatangan",
        'signature_insert_1': "Sisip Tandatangan 1",
        'signature_insert_2': "Sisip Tandatangan 2",
        'signature_customize': " Laraskan tandatangan ini",
        'signature_discard': " Buang tandatangan ini",
        'signature_save_all': " Simpan semua tandatangan",
        'signature_discard_all': " Buang semua tandatangan",
        'signature_guide_title': "Tandatangan - Panduan",
        'signature_guide': """
📝 Tandatangan - Panduan ringkas

- Sediakan Kata Laluan Induk
- Konfigurasikan tandatangan dalam menu Tetapan
  (saiz, cap masa ...)
- Sisip dengan KLIK KANAN pada kedudukan yang dikehendaki
  (Kata Laluan Induk diperlukan sekali setiap sesi)
- Alihkan tandatangan dengan tetikus atau kekunci anak panah
- Pelbagai tandatangan boleh disisip berturut-turut
- Setiap tandatangan boleh dilaraskan secara individu
- Buang tandatangan individu
- Simpan / buang semua tandatangan sekaligus
- Sebagai alternatif, bar menu juga boleh digunakan.
        """,
        'signature_placeholder': "Tiada pratonton tersedia",
        'signature_info': "Tandatangan {0}: {1}×{2} px ({3}% daripada {4}×{5})",
        'signature_info_placeholder': "Tetapan untuk tandatangan {0}",
        'signature_inserted': "Tandatangan {0} pada halaman {1} disisipkan",
        'signature_deleted': "Tandatangan dipadamkan",
        'signature_copied': "Tandatangan disalin",
        'signature_pasted': "Tandatangan {0} ditampal",
        'signature_saved': "{0} tandatangan telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'signature_saved_voice': "{0} tandatangan disimpan",
        'mode_replace_signature_format': "Tamatkan mod dan sisip tandatangan {0}",
        'mode_conflict_voice_signature': "Mod {0} aktif. Tamatkan dan sisip tandatangan?",
        'signature_not_configured': "Tandatangan {0} tidak dikonfigurasi",
        'signature_file_not_found': "Fail tandatangan tidak dijumpai",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Tiada tandatangan yang disalin",
        'no_signatures_to_save': "Tiada tandatangan untuk disimpan",
        'signature_save_question': "Simpan semua tandatangan, laraskan atau buang yang ini?",
        'signatures_saved_title': "Tandatangan disimpan",
        'signatures_saved': "{0} tandatangan telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'signatures_saved_voice': "{0} tandatangan disimpan.",
        'all_signatures_discarded': "Semua tandatangan dibuang",
        'signature_settings_saved': "Tetapan tandatangan disimpan",
        'signature_cancelled': "Tandatangan dibuang",
        'signature_active_title': "Tandatangan aktif",
        'signature_replace_question': "Sudah ada tandatangan yang aktif.\n\nAdakah anda mahu menggantikan tandatangan semasa?",
        'signature_replace': "Ganti tandatangan",
        'signature_replace_voice': "Ganti tandatangan semasa atau batal?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Tetapan Imej",
        'image_common': "Tetapan imej am",
        'image_keep_aspect': "Kekalkan nisbah bidang semasa menarik",
        'image_default_size': "Saiz standard (%):",
        'image_dark_invert': "Songsangkan imej dalam Mod Gelap",
        'image_dark_invert_tooltip': "Diaktifkan: imej akan disongsangkan untuk keterlihatan yang lebih baik",
        'image_fine_tuning': "Pelarasan halus (piksel)",
        'image_offset_x': "Ofset X:",
        'image_offset_y': "Ofset Y:",
        'image_offset_x_tooltip': "Nilai negatif mengalihkan imej ke kiri semasa menyimpan, positif ke kanan",
        'image_offset_y_tooltip': "Nilai negatif mengalihkan imej ke atas semasa menyimpan, positif ke bawah",
        'image_select': "Pilih imej",
        'image_insert': "Sisip imej",
        'image_customize': " Laraskan imej ini",
        'image_aspect': " Kekalkan nisbah bidang",
        'image_discard': " Buang imej ini",
        'image_save_all': " Simpan semua imej",
        'image_discard_all': " Buang semua imej",
        'image_filter': "Imej",
        'image_guide_title': "Sisip imej - Panduan",
        'image_guide': """
📷 Menyisip imej ke dalam PDF - Panduan ringkas:

1. Klik kanan pada kedudukan yang dikehendaki
2. "Sisip imej" → Pilih imej
3. Letakkan imej: Seret dengan tetikus
4. Laraskan saiz: Seret pada sudut/tepi
5. Kekalkan nisbah bidang: Tekan kekunci [A]
6. Pelarasan lanjut: Klik kanan pada imej

Petua: Dalam menu konteks, anda boleh melaraskan tetapan.
        """,
        'image_inserted': "Imej {0} pada halaman {1} disisipkan",
        'image_deleted': "Imej dibuang",
        'image_copied': "Imej disalin",
        'image_pasted': "Imej ditampal",
        'image_saved': "{0} imej telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'image_saved_voice': "{0} imej disimpan",
        'image_aspect_on': "diaktifkan",
        'image_aspect_off': "dinyahaktifkan",
        'image_aspect_toggle': "Kekalkan nisbah bidang {0}",
        'image_reset': "Imej dikembalikan ke saiz asal",
        'image_replaced': "Imej diganti",
        'image_invalid': "Bukan imej yang sah",
        'mode_replace_image': "Sisip imej",
        'mode_conflict_voice_image': "Mod {0} aktif. Tamatkan dan sisip imej?",
        'image_active_title': "Imej aktif",
        'image_replace_question': "Sudah ada imej yang aktif.\n\nAdakah anda mahu menggantikan imej semasa?",
        'image_replace': "Ganti imej",
        'image_replace_voice': "Ganti imej semasa atau batal?",
        'image_filter_all': "Imej (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Semua fail (*.*)",
        'no_copied_image': "Tiada imej yang disalin",
        'image_discarded': "Imej dibuang",
        'image_save_question': "Simpan semua imej, laraskan atau buang yang ini?",
        'no_images_to_save': "Tiada imej untuk disimpan",
        'no_valid_images': "Tiada imej sah untuk disimpan",
        'images_saved_title': "Imej disimpan",
        'images_saved': "{0} imej telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'images_saved_voice': "{0} imej disimpan.",
        'all_images_discarded': "Semua imej dibuang",
        'image_settings_updated': "Tetapan imej dikemas kini",
        'image_replace_title': "Pilih imej baharu",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Tetapan Bentuk",
        'form_basic': "Tetapan asas",
        'form_default_type': "Jenis bentuk standard:",
        'form_rectangle': "Segi empat tepat",
        'form_ellipse': "Elips",
        'form_line': "Garis",
        'form_arrow': "Anak panah",
        'form_line_width': "Ketebalan garis:",
        'form_colors': "Warna",
        'form_line_color': "Warna garis:",
        'form_fill_color': "Warna isian:",
        'form_choose_color': "Pilih",
        'form_transparent': "Latar belakang telus (garis sahaja)",
        'form_filled': "diisi",
        'form_dark_mode': "Mod Gelap",
        'form_dark_invert': "Songsangkan warna dalam Mod Gelap",
        'form_fine_tuning': "Pelarasan halus (piksel)",
        'form_offset_x': "Ofset X:",
        'form_offset_y': "Ofset Y:",
        'form_offset_x_tooltip': "Nilai negatif mengalihkan bentuk ke kiri semasa menyimpan, positif ke kanan",
        'form_offset_y_tooltip': "Nilai negatif mengalihkan bentuk ke atas semasa menyimpan, positif ke bawah",
        'form_preview': "Pratonton",
        'form_insert': "Sisip bentuk",
        'form_rectangle_insert': "Segi empat tepat",
        'form_ellipse_insert': "Elips/Bulatan",
        'form_line_insert': "Garis (2 klik)",
        'form_arrow_insert': "Anak panah (2 klik)",
        'form_customize': " Laraskan bentuk ini",
        'form_transparent_toggle': " Latar belakang telus",
        'form_discard': " Buang bentuk ini",
        'form_save_all': " Simpan semua bentuk",
        'form_discard_all': " Buang semua bentuk",
        'form_guide_title': "Sisip bentuk - Panduan",
        'form_guide': """
📐 Menyisip bentuk ke dalam PDF - Panduan ringkas:

1. Pilih jenis bentuk (Segi empat tepat, Elips, Garis, Anak panah)
2. Klik pada kedudukan
   - Untuk segi empat tepat/elips: Satu klik meletakkan bentuk
   - Untuk garis/anak panah: Dua klik untuk titik mula dan akhir
3. Letakkan bentuk: Seret dengan tetikus
4. Laraskan saiz: Seret pada sudut/tepi
5. Simpan bentuk: Enter
6. Buang bentuk: ESC
7. Pelarasan lanjut: Klik kanan pada bentuk

Petua: Dalam menu konteks, anda boleh melaraskan tetapan.
        """,
        'form_inserted': "{0} pada halaman {1} disisipkan",
        'form_deleted': "Bentuk dipadamkan",
        'form_copied': "Bentuk disalin",
        'form_pasted': "Bentuk ditampal",
        'form_saved': "{0} bentuk telah dimasukkan ke dalam PDF.\n\nPDF telah dimuat semula...",
        'form_saved_voice': "{0} bentuk disimpan",
        'form_reset': "Bentuk dikembalikan ke saiz standard",
        'form_transparent_on': "diaktifkan",
        'form_transparent_off': "dinyahaktifkan",
        'form_transparent_toggled': "Latar belakang telus {0}",
        'form_line_cancel': "Lukisan garis dibatalkan",
        'form_second_click': "Sekarang klik titik akhir untuk {0}",
        'mode_replace_form': "Sisip bentuk",
        'mode_conflict_voice_form': "Mod {0} aktif. Tamatkan dan sisip bentuk?",
        'form_settings_updated': "Tetapan bentuk dikemas kini",
        'form_unknown': "Bentuk",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klik pada kedudukan mula",
        'form_line_guide_2': "2. Klik pada kedudukan akhir",
        'form_line_guide_3': "Garis akan dilukis di antara kedua-dua titik.",
        'form_line_status_1': "Menunggu klik pertama...",
        'form_line_status_2': "Titik pertama ditetapkan: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Sekarang klik titik akhir...",
        'form_line_status_4': "Kedua-dua titik ditetapkan.\nKlik 'Selesai' untuk menyimpan.",
        'form_line_reset': "Set semula",
        'form_line_finish': "Selesai",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Salin (Cmd+C)",
        'paste': "Tampal (Cmd+V)",
        'copied': "Disalin: {0}",
        'no_element_to_copy': "Tiada elemen dipilih untuk disalin",
        'no_copied_data': "Tiada data yang disalin",
        'no_valid_position': "Tiada kedudukan sah untuk ditampal",
        'copy_text': "Teks disalin",
        'copy_image': "Imej disalin",
        'copy_form': "Bentuk disalin",
        'copy_signature': "Tandatangan disalin",
        'element_text': "Teks",
        'element_image': "Imej",
        'element_form': "Bentuk",
        'element_signature': "Tandatangan",
        'element_unknown': "Elemen",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflik Mod",
        'mode_conflict_message': "Mod '{0}' sudah aktif.\n\nAdakah anda mahu menamatkannya dan {1}?",
        'mode_replace': "Tamatkan mod dan {0}",
        'mode_cancel': "Batal",
        'mode_replace_text': "sisip teks",
        'mode_replace_cross': "sisip pangkah",
        'mode_replace_signature': "sisip tandatangan",
        'mode_replace_image': "sisip imej",
        'mode_replace_form': "sisip bentuk",
        'mode_conflict_voice': "Mod {0} aktif. Tamatkan dan sisip teks?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Input teks",
        'active_mode_signature': "Tandatangan",
        'active_mode_image': "Imej",
        'active_mode_form': "Bentuk",
        'active_mode_and': " dan ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Sisip",                    # Hauptmenü
        'insert_another_text': "Sisip teks",          # Vereinfacht
        'insert_another_cross': "Sisip pangkah",        # Vereinfacht
        'insert_another_signature_1': "Tandatangan 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Tandatangan 2",      # Untermenü-Eintrag
        'insert_another_image': "Sisip imej",         # Vereinfacht
        'insert_another_form_rect': "Segi empat tepat",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Elips",        # Untermenü-Eintrag
        'insert_another_form_line': "Garis (2 klik)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Anak panah (2 klik)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Simpan {0}",
        'save_dialog_message': "{0} akan disimpan pada halaman {1}.\n\nBagaimana anda mahu meneruskan?",
        'save_all': "Simpan semua {0}",
        'save_single': "Simpan {0}",
        'save_customize': "Laraskan {0}",
        'save_discard': "Buang {0} ini",
        'save_continue': "Teruskan mengedit",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Pergi ke halaman {0}",
        'context_rotate': " Putar halaman {0}",
        'context_delete': " Padam halaman {0}",
        'context_export': " Eksport halaman {0}",
        'context_mark_as': " Tanda halaman sebagai...",
        'context_mark_empty': " Halaman kosong",
        'context_unmark_empty': " Bukan kosong lagi",
        'context_mark_export': " Tanda untuk eksport",
        'context_unmark_export': " Nyah tanda eksport",
        'context_batch_actions': " Tindakan berkumpulan",
        'context_batch_delete_empty': " Padam semua {0} halaman kosong",
        'context_batch_export_single': " Semua {0} halaman (satu fail)",
        'context_batch_export_split': " Semua {0} halaman (berasingan)",
        'context_drag_start': " Mula Drag & Drop",
        'context_drag_stop': " Tamat Drag & Drop",
        'context_insert': " Sisip",
        'context_insert_pages': " Sisip halaman",
        'context_zoom': "Zum",
        'discard_mixed': "Buang semua {0} {1} dan {2} {3}",
        'save_mixed': "Simpan {0} {1} dan {2} {3}",
        'discard_texts': "Buang semua {0} teks",
        'discard_text_single': "Buang 1 teks",
        'save_texts': "Simpan {0} teks",
        'save_text_single': "Simpan 1 teks",
        'discard_crosses': "Buang semua {0} pangkah",
        'discard_cross_single': "Buang 1 pangkah",
        'save_crosses': "Simpan {0} pangkah",
        'save_cross_single': "Simpan 1 pangkah",
        'discard_signatures': "Buang semua {0} tandatangan",
        'save_signature_single': "Simpan 1 tandatangan",
        'save_signatures': "Simpan {0} tandatangan",
        'discard_images': "Buang semua {0} imej",
        'save_image_single': "Simpan 1 imej",
        'save_images': "Simpan {0} imej",
        'discard_forms': "Buang semua {0} bentuk",
        'save_form_single': "Simpan 1 bentuk",
        'save_forms': "Simpan {0} bentuk",
        'cross_discard': "Buang pangkah ini",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Maklumat Eksport / Import",
        'export_what': "📋 Apa yang dieksport?",
        'export_general': "Tetapan am",
        'export_general_items': "• Output suara (hidup/mati, kelajuan)\n• Mod Gelap/Terang\n• Tetapan sandaran\n• Tetapan OCR",
        'export_image_form': "Tetapan imej dan bentuk",
        'export_image_form_items': "• Tetapan imej (nisbah bidang, saiz standard)\n• Tetapan bentuk (ketebalan garis, warna)\n• Tetapan tandatangan (laluan, saiz, cap masa)",
        'export_passwords': "Pangkalan data kata laluan",
        'export_passwords_items': "• Semua kata laluan PDF yang disimpan\n• Boleh dipilih disulitkan atau dinyahsulit",
        'export_master': "Tetapan Kata Laluan Induk",
        'export_master_items': "• Hash Kata Laluan Induk\n• Tetapan untuk tandatangan/blok teks",
        'export_signatures': "Tandatangan dan blok teks",
        'export_signatures_items': "• Semua fail imej (tandatangan)\n• Semua blok teks dengan pemformatan\n• Tanda peribadi/awam",
        'export_import_warning': "⚠️ Nota Penting",
        'export_import_note': "• Semasa import, SEMUA tetapan semasa akan ditimpa\n• Permulaan semula aplikasi diperlukan\n• Tandatangan/blok teks sedia ada akan diganti",
        'export_master_note': "• Jika Kata Laluan Induk ditetapkan, anda boleh memilih:\n  - Dinyahsulit (kata laluan dalam teks biasa)\n  - Disulitkan (hanya boleh dibaca dengan Kata Laluan Induk)",
        'export_security': "• Fail ZIP yang dieksport mengandungi data sensitif\n• Sila simpan dengan selamat (cth. pemacu USB yang disulitkan)\n• Jika fail hilang: kata laluan tidak boleh dipulihkan",
        'export_format': "📁 Format eksport",
        'export_format_desc': "Tetapan akan disimpan dalam satu fail ZIP:",
        'export_filename': "PDFDarkView_Tetapan_YYYYMMDD_HHMMSS.zip",
        'export_success': "Tetapan berjaya dieksport",
        'export_failed': "Eksport gagal",
        'export_import_question': "Adakah anda mahu memulakan semula aplikasi sekarang?",
        'export_password_question': "Kata Laluan Induk ditetapkan.\n\nAdakah anda mahu mengeksport kata laluan dalam bentuk dinyahsulit?\n(jika tidak, ia akan dieksport dalam bentuk disulitkan)",
        'export_decrypt': "Eksport dinyahsulit",
        'export_encrypt': "Eksport disulitkan",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Maklumat",
        'info_title': "Perihal PDF Dark View",
        'info_version': "Versi",
        'info_author': "Dibangunkan oleh Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Perihal",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ialah pembaca PDF yang boleh diakses, dibangunkan khas untuk individu kurang upaya penglihatan.</p>

            <p><strong>Ciri Utama:</strong></p>
            <ul>
                <li>Antara muka berkontras tinggi, boleh disesuaikan</li>
                <li>Kawalan papan kekunci sepenuhnya</li>
                <li>Output suara bersepadu</li>
                <li>OCR untuk dokumen yang diimbas</li>
                <li>Alat penyuntingan yang komprehensif</li>
            </ul>

            <p>Lebih daripada 50 bahasa disokong – menjadikan PDF boleh diakses oleh semua orang.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Fungsi",
        'info_features_intro': "PDF Dark View menawarkan kemungkinan berikut kepada anda:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Paparan & Navigasi</strong> – Mod Gelap/Terang, meneliti halaman, zum, lompat ke halaman</li>
            <li><strong>OCR (Pengecaman Teks)</strong> – Jadikan dokumen yang diimbas boleh dicari dan disalin</li>
            <li><strong>Penyuntingan</strong> – Masukkan teks, tanda silang, tandatangan, imej dan bentuk</li>
            <li><strong>Pengurusan Halaman</strong> – Padam, ekstrak, masukkan, alih melalui seret & lepas</li>
            <li><strong>Eksport</strong> – Ke Word, Pages atau sebagai teks</li>
            <li><strong>Keselamatan</strong> – Perlindungan dan pengurusan kata laluan</li>
            <li><strong>Kebolehaksesan</strong> – Output suara, kawalan papan kekunci, kontras tinggi</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Penggunaan",
        'info_accessibility': "♿ Kebolehaksesan – kawalan papan kekunci sepenuhnya",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Umum</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Buka PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Cari</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Togol Mod Gelap/Terang</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Cetak</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Keluar</div>

        <div class="shortcut-cat">📖 Navigasi</div>
        <div class="shortcut-row"><kbd>Kekunci anak panah</kbd> Meneliti halaman demi halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Pergi ke halaman</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Halaman pertama</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Halaman terakhir</div>

        <div class="shortcut-cat">✏️ Penyuntingan</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Masukkan teks</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Padam halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Ekstrak halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Masukkan halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Alih halaman</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Putar halaman</div>

        <div class="shortcut-cat">🖼️ Mengalih elemen</div>
        <div class="shortcut-row"><kbd>Kekunci anak panah</kbd> Alih teks/imej/tandatangan</div>
        <div class="shortcut-row"><kbd>Ctrl+Kekunci anak panah</kbd> Langkah yang lebih besar</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Simpan</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Batal</div>

        <div class="shortcut-cat">🗣️ Output suara</div>
        <div class="shortcut-row"><kbd>F2</kbd> Hidup/mati output suara</div>
        """,
        'info_contextmenu': "📌 Penting: Semua fungsi juga boleh diakses melalui menu konteks (butang tetikus kanan)!",
        'info_accessibility_hint': "💡 Petua: Output suara (F2) memudahkan orientasi dan memberikan maklum balas tentang menu dan dialog.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lesen & Impresum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUM</strong><br>
        Maklumat mengikut § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Jerman<br>
        E-mel: binhdiez64@gmail.com<br>
        Bertanggungjawab untuk kandungan: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Penafian</strong><br>
        Perisian ini dibangunkan dengan penuh ketelitian. Tiada jaminan diberikan untuk ketepatan, kesempurnaan dan kefungsian. Penggunaan adalah atas risiko sendiri.<br><br>

        <strong>📄 Lesen MIT (penggunaan persendirian)</strong><br>
        Hak cipta (c) 2026 Toralf Schulz (BinhDiez)<br>
        Dibenarkan: penggunaan percuma, perubahan persendirian, salinan peribadi.<br>
        Tidak dibenarkan: penjualan, penggunaan komersial, penyingkiran notis hak cipta.<br><br>

        <strong>🔧 Komponen pihak ketiga</strong><br>
        Perisian ini mengandungi komponen di bawah lesen GPL, AGPL, Apache 2.0, BSD dan MIT.<br>
        Apabila mengedarkan semula, syarat lesen masing-masing mesti dipatuhi.<br><br>

        <strong>🌐 Sumber Terbuka</strong><br>
        Kod sumber tersedia dan boleh dilihat, diubah suai dan diedarkan semula mengikut syarat lesen masing-masing.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Penghargaan",
        'info_credits': "Terima kasih kepada komuniti sumber terbuka",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Pemprosesan PDF</li>
            <li><strong>PyQt5</strong> – Antara muka grafik</li>
            <li><strong>Tesseract OCR</strong> – Pengecaman teks</li>
            <li><strong>OCRmyPDF</strong> – Integrasi OCR</li>
            <li><strong>python-docx</strong> – Eksport Word</li>
            <li><strong>qtawesome</strong> – Ikon</li>
            <li><strong>DeepSeek</strong> – Sokongan untuk terjemahan (50+ bahasa)</li>
            <li><strong>Semua pengguna</strong> – Untuk maklum balas berharga</li>
            <li><strong>Komuniti sumber terbuka</strong> – Untuk pustaka yang hebat</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Bahasa",
        'info_languages_header': "🌍 Sokongan Bahasa",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View kini menyokong <strong>62 bahasa</strong> – supaya perisian ini boleh digunakan secara boleh diakses di seluruh dunia.</p>

            <p><strong>📖 Senarai bahasa lengkap (Setakat Mac 2026):</strong></p>
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
                    <li>🇬🇧 Inggeris (English)</li>
                    <li>🇪🇪 Estonia (Eesti)</li>
                    <li>🇫🇮 Finland (Suomi)</li>
                    <li>🇫🇷 Perancis (Français)</li>
                    <li>🇬🇷 Greek (Ελληνικά)</li>
                    <li>🇮🇱 Ibrani (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croatia (Hrvatski)</li>
                    <li>🇭🇺 Hungary (Magyar)</li>
                    <li>🇮🇩 Indonesia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Ireland (Gaeilge)</li>
                    <li>🇮🇸 Iceland (Íslenska)</li>
                    <li>🇮🇹 Itali (Italiano)</li>
                    <li>🇯🇵 Jepun (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korea (한국어)</li>
                    <li>🇱🇦 Laos (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvia (Latviešu)</li>
                    <li>🇱🇹 Lithuania (Lietuvių)</li>
                    <li>🇱🇺 Luxembourg (Lëtzebuergesch)</li>
                    <li>🇲🇾 Melayu (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolia (Монгол)</li>
                    <li>🇳🇵 Nepal (नेपाली)</li>
                    <li>🇳🇱 Belanda (Nederlands)</li>
                    <li>🇳🇴 Norway (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Parsi (فارسی)</li>
                    <li>🇵🇱 Poland (Polski)</li>
                    <li>🇵🇹 Portugis (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Romania (Română)</li>
                    <li>🇷🇺 Rusia (Русский)</li>
                    <li>🇸🇪 Sweden (Svenska)</li>
                    <li>🇷🇸 Serbia (Српски)</li>
                    <li>🇸🇰 Slovakia (Slovenčina)</li>
                    <li>🇸🇮 Slovenia (Slovenščina)</li>
                    <li>🇪🇸 Sepanyol (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Czech (Čeština)</li>
                    <li>🇹🇷 Turki (Türkçe)</li>
                    <li>🇺🇦 Ukraine (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnam (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yiddish (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Tambah bahasa sendiri:</strong><br>
                Mahukan bahasa yang belum disertakan? Hanya letakkan fail kamus anda sendiri (<code>sprache_xx.py</code>) di sebelah aplikasi – perisian akan mengenalinya secara automatik. Jika anda berminat dengan terjemahan khusus, sila hubungi saya.
            </div>

            <p><strong>🙏 Penghargaan khusus:</strong> DeepSeek atas sokongan dalam menterjemahkan semua kamus ke dalam 62 bahasa.</p>

            <p>📧 Hubungi untuk terjemahan: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Ralat",
        'error_occurred': "Berlakunya ralat",
        'error_pdf_load': "Ralat semasa memuat PDF",
        'error_pdf_save': "Ralat semasa menyimpan PDF",
        'error_ocr': "Ralat semasa pengecaman teks",
        'error_no_pdf': "Tiada PDF dimuat",
        'error_page_not_found': "Halaman tidak dijumpai",
        'error_invalid_range': "Julat halaman tidak sah",
        'error_file_not_found': "Fail tidak dijumpai",
        'error_permission': "Tiada kebenaran",
        'error_unknown': "Ralat tidak diketahui",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Berjaya",
        'success_operation': "Operasi berjaya diselesaikan",
        'success_saved': "Berjaya disimpan",
        'success_exported': "Berjaya dieksport",
        'success_imported': "Berjaya diimport",
        'success_deleted': "Berjaya dipadamkan",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Pengesahan",
        'confirm_yes': "Ya",
        'confirm_no': "Tidak",
        'confirm_ok': "OK",
        'confirm_cancel': "Batal",
        'confirm_delete': "Padam",
        'confirm_overwrite': "Ganti",
        'confirm_continue': "Teruskan",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Memuat PDF...",
        'progress_saving': "Menyimpan PDF...",
        'progress_exporting': "Mengeksport PDF...",
        'progress_processing': "Pemprosesan sedang berjalan...",
        'progress_wait': "Sila tunggu...",
        'progress_preparing': "Persediaan...",
        'progress_finalizing': "Penyiapan...",

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
        'color_orange': "Oren",
        'color_gray': "Kelabu",
        'color_custom': "Pemilihan warna",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fail",
        'menu_edit': "&Edit",
        'menu_view': "&Paparan",
        'menu_tools': "&Alat",
        'menu_settings': "&Tetapan",
        'menu_help': "&Bantuan",
        'menu_language': "🌐 Bahasa",
        'menu_guides': "&Panduan",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Buka",
        'file_save_as': "&Simpan sebagai...",
        'file_protect': "&Lindungi dokumen...",
        'file_export': "&Eksport",
        'file_export_pages': "Eksport sebagai Pages",
        'file_export_word': "Eksport sebagai DOCX",
        'file_export_text': "Eksport sebagai TXT",
        'file_print_now': "&Cetak sekarang",
        'file_print': "&Cetak",
        'file_close': "&Tutup",
        'file_quit': "&Keluar",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Cari",
        'edit_ocr': " Lakukan OCR",
        'edit_rotate': "&Putar halaman",
        'edit_rotate_all': "&Putar semua halaman",
        'edit_delete_pages': "&Padam halaman",
        'edit_extract_pages': "&Ekstrak halaman",
        'edit_insert_pages': "&Sisip halaman",
        'edit_move_pages': "&Alih halaman",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Sisip teks dan pangkah",
        'text_insert': " Sisip teks",
        'cross_insert': " Sisip pangkah",
        'text_customize': " Laraskan teks ini",
        'cross_customize': " Laraskan pangkah ini",
        'cross_customize_all': " Laraskan semua pangkah",
        'text_discard': " Buang teks/pangkah ini",
        'text_discard_all': " Buang semua teks dan pangkah",
        'text_save_all': " Simpan semua teks dan pangkah",
        'text_guide': " Input teks / Blok teks - Panduan",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Sisip tandatangan",
        'signature_settings_menu': " Tetapan...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Sisip imej",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Sisip bentuk",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Tunjuk tetingkap teks",
        'view_zoom': "&Zum",
        'view_zoom_page': "&Lebar halaman (standard)",
        'view_zoom_two': "&Dua halaman",
        'view_zoom_overview': "&Gambaran keseluruhan (berbilang halaman)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Alat bantuan",
        'settings_voice': "Output suara",
        'settings_voice_tooltip': "menambah output suara pembaca skrin dengan maklumat tambahan",
        'settings_signature': "&Tetapan tandatangan",
        'settings_password': "&Pengurusan kata laluan",
        'settings_backup': "Buat sandaran sebelum perubahan",
        'settings_export_import': "&Eksport / import tetapan",
        'settings_export': "&Eksport semua tetapan...",
        'settings_import': "&Import semua tetapan...",
        'settings_export_info': "&Apa yang dieksport?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "hidup",
        'voice_off': "mati",
        'voice_toggle': "Output suara {0}",
        'voice_speed': "Kelajuan pada {0} peratus",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Alat tidak dijumpai:\n{0}\n\nBASE_DIR: {1}\nSila pastikan alat PDF dipasang dalam direktori {1}.",
        'tool_started': "{0} dimulakan",
        'tool_start_failed': "Tidak dapat dimulakan",
        'process_error_failed_to_start': "Proses tidak dapat dimulakan. Adakah fail wujud?",
        'process_error_crashed': "Proses ranap semasa permulaan.",
        'process_error_timeout': "Masa tamat proses dicapai.",
        'process_error_write': "Ralat tulis pada proses.",
        'process_error_read': "Ralat baca pada proses.",
        'process_error_unknown': "Ralat proses tidak diketahui",
        'process_command': "Arahan",
        'process_normal_exit': "tamat secara normal",
        'process_crashed': "ranap",
        'process_nonzero_exit': "{0} ditamatkan dengan kod ralat {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Membatalkan...",
        'move_cancelling': "Membatalkan pengalihan",
        'opening_pdf': "Membuka PDF...",
        'loading_document': "Memuat dokumen...",
        'pdf_opened': "PDF dibuka",
        'pages_found_moving': "{0} halaman dijumpai, {1} untuk dialihkan",
        'creating_backup': "Membuat sandaran...",
        'backup_description': "Menyandarkan fail asal...",
        'backup_saved_as': "Disandarkan sebagai: {0}",
        'error_format': "Ralat: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView oleh BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Carian diset semula",
        'page_header_simple': "=== Halaman {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Pengurusan Kata Laluan – Panduan",
        'password_guide_voice': "Panduan untuk pengurusan kata laluan. Sila baca nota.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Pengurusan Kata Laluan – Panduan Terperinci</strong></p>

        <p><strong>1. Perlindungan kata laluan untuk PDF</strong></p>
        <ul>
        <li>Apabila membuka PDF yang dilindungi kata laluan, dialog akan muncul di mana anda boleh memasukkan kata laluan.</li>
        <li>Anda boleh menyimpan kata laluan secara disulitkan supaya anda tidak perlu memasukkannya setiap kali (kotak semak "Simpan kata laluan").</li>
        <li>Dengan butang "Alih keluar kata laluan", anda boleh membuat salinan PDF yang dinyahsulit dan memadam kata laluan daripada pangkalan data.</li>
        </ul>

        <p><strong>2. Kata Laluan Induk</strong></p>
        <ul>
        <li>Kata Laluan Induk melindungi akses kepada semua kata laluan PDF yang disimpan.</li>
        <li><strong>Menyediakan:</strong> Pergi ke "Tetapan → Pengurusan Kata Laluan → Tetapan Kata Laluan Induk" dan klik pada "Sediakan Kata Laluan Induk". Pilih kata laluan yang kukuh (sekurang-kurangnya 8 aksara).</li>
        <li><strong>Menukar:</strong> Selepas pengesahan berjaya, anda boleh menukar Kata Laluan Induk.</li>
        <li><strong>Mengalih keluar:</strong> Jika anda memadam Kata Laluan Induk, SEMUA kata laluan yang disimpan akan dipadamkan secara kekal. Anda boleh mengeksport sandaran terlebih dahulu.</li>
        <li>Setiap sesi, anda perlu mengesahkan dengan Kata Laluan Induk sekali untuk mengakses fungsi yang dilindungi (cth. memaparkan kata laluan).</li>
        </ul>

        <p><strong>3. Pengurusan Kata Laluan (senarai)</strong></p>
        <ul>
        <li>Di bawah "Tetapan → Pengurusan Kata Laluan", anda membuka jadual semua PDF yang disimpan dengan kata laluan disulitkan mereka.</li>
        <li><strong>Tanpa Kata Laluan Induk:</strong> Anda hanya boleh memadam entri – kata laluan kekal tersembunyi.</li>
        <li><strong>Dengan Kata Laluan Induk (disahkan):</strong> Anda boleh melihat, menyalin, mengeksport dan memadam kata laluan.</li>
        <li><strong>Eksport:</strong> Pilih format (JSON, CSV, TXT) dan simpan senarai. Jika Kata Laluan Induk ditetapkan, anda boleh memutuskan sama ada kata laluan dieksport dalam teks biasa atau terus disulitkan.</li>
        <li><strong>Import:</strong> Fail ZIP yang dieksport sebelum ini dengan semua tetapan (termasuk kata laluan) boleh dibaca semula melalui "Tetapan → Eksport/import tetapan". Awas: Data sedia ada akan ditimpa!</li>
        </ul>

        <p><strong>4. Penjana Kata Laluan</strong></p>
        <ul>
        <li>Dalam dialog kata laluan (cth. semasa melindungi PDF), anda akan menemui butang dadu 🎲 di sebelah kanan medan input.</li>
        <li>Klik padanya untuk membuka penjana kata laluan. Anda boleh menetapkan panjang, set aksara (huruf besar, huruf kecil, nombor, simbol khas) dan pemisah untuk kebolehbacaan yang lebih baik.</li>
        <li>Kata laluan yang dijana boleh digunakan terus dan juga boleh disalin jika perlu.</li>
        </ul>

        <p><strong>5. Nota keselamatan penting</strong></p>
        <ul>
        <li>Kata laluan yang disimpan disimpan dengan penyulitan AES-256. Kunci diperoleh daripada Kata Laluan Induk anda (jika ditetapkan) atau daripada nilai tetap (tanpa Kata Laluan Induk).</li>
        <li>Tanpa Kata Laluan Induk, kata laluan disulitkan tetapi kunci disimpan dalam program – penyerang yang mempunyai akses kepada fail anda boleh menyahsulitnya. Oleh itu, kami amat mengesyorkan penggunaan Kata Laluan Induk.</li>
        <li>Pangkalan data kata laluan terletak dalam direktori `Daten/passwords.json`. Buat sandaran secara berkala, terutamanya sebelum mengalih keluar Kata Laluan Induk.</li>
        <li>Jika Kata Laluan Induk hilang, semua kata laluan yang disimpan akan hilang selama-lamanya.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Mod penyongsangan",
        'invert_mode_classic': "Klasik (songsangkan semua warna)",
        'invert_mode_smart': "Pintar (songsangkan hanya kecerahan)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Ambang skala kelabu",
        'gray_threshold_10': "10% (ketat)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Piawai)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (lembut)",
        'threshold_changed': "Ambang ditetapkan kepada {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Ambang skala kelabu – Penjelasan",
        'threshold_guide_text': "Ambang skala kelabu menentukan piksel mana dalam mod gelap pintar yang dianggap 'kelabu' dan disongsangkan.\n\n"
                                "• Nilai rendah (10%) hanya menyongsangkan ton kelabu yang hampir sempurna – elemen berwarna kekal terpelihara sepenuhnya.\n"
                                "• Nilai tinggi (50%) juga menyongsangkan piksel yang sedikit berwarna – ini meningkatkan kontras, tetapi boleh memesongkan warna.\n\n"
                                "Nilai optimum bergantung pada dokumen. Untuk dokumen teks tulen, 30–40% selalunya ideal, untuk grafik berwarna sebaiknya 10–20%.\n\n"
                                "Anda boleh menyesuaikan nilai pada bila-bila masa melalui menu 'Tetapan' – PDF akan dimuat semula dengan serta-merta.\n\n"
                                "Perhatian:\n* Foto dan imej hanya boleh dipaparkan dengan betul dalam Mod Terang!\n* Tetapan penyongsangan hanya dipaparkan apabila Mod Gelap diaktifkan.",
        'threshold_guide_voice': "Ambang skala kelabu menentukan seberapa kuat mod gelap pintar campur tangan. Nilai rendah mengekalkan warna, nilai tinggi meningkatkan kontras.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Membuka PDF...",
        'progress_loading_document': "Memuat dokumen...",
        'progress_pdf_opened': "PDF dibuka",
        'progress_creating_backup': "Membuat sandaran...",
        'progress_backup_description': "Melindungi fail asal...",
        'progress_backup_created': "Sandaran dibuat",
        'progress_backup_saved_as': "Disimpan sebagai: {0}",
        'progress_analyzing_start': "Memulakan analisis...",
        'progress_searching_empty': "Mencari halaman kosong...",
        'progress_page_empty': "Halaman {0} kosong",
        'progress_page_keep': "Kekalkan halaman {0}",
        'progress_analysis_complete': "Analisis selesai",
        'progress_empty_found': "Ditemui {0} halaman kosong",
        'progress_current_page': "Halaman semasa",
        'progress_mark_delete': "Ditanda untuk dipadam",
        'progress_range_selected': "Julat halaman {0}-{1}",
        'progress_deleting_pages': "Memadam {0} halaman",
        'progress_creating_new_pdf': "Membuat PDF baharu...",
        'progress_transferring_pages': "Memindahkan halaman",
        'progress_keeping_page': "Halaman {0} akan dikekalkan ({1}/{2})",
        'progress_saving_pdf': "Menyimpan PDF...",
        'progress_optimizing': "Mengoptimumkan saiz fail...",
        'progress_finalizing': "Memuktamadkan...",
        'progress_new_size': "Saiz baharu: {0:.2f} MB",
        'progress_cancelling': "Membatalkan...",
        'progress_cancel_message': "{0} sedang dibatalkan",
        'progress_pages_found_moving': "Ditemui {0} halaman, {1} untuk dialih",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Menganalisis PDF...",
        'ocr_status_optimizing': "Pengoptimuman imej sedang berjalan...",
        'ocr_status_recognizing': "Pengecaman teks sedang berjalan...",
        'ocr_status_embedding': "Membenamkan teks...",
        'ocr_status_finalizing': "Memuktamadkan PDF...",

        # PDF-Laden
        'progress_preparing': "Menyediakan...",
        'progress_loading': "Memuat PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Memadam halaman...",
        'progress_moving_title': "Mengalih halaman...",
        'pages_found': "Halaman ditemui",
        'progress_creating_new_order': "Membuat susunan baharu...",
        'progress_sorting_pages': "Menyusun halaman...",
        'progress_moving_to_begin': "Alih {0} halaman ke permulaan",
        'progress_transferring_count': "Pindahkan {0} halaman",
        'progress_transferring_before_target': "Pindahkan halaman sebelum sasaran",
        'progress_moving_pages': "Alih {0} halaman",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_sandaran_",
        'filename_protected_suffix': "_dilindungi_",
        'filename_copy_suffix': "_Salinan",
        'filename_page_single': "_Halaman_",
        'filename_page_range': "_Halaman_",
        'filename_export_page': "_Halaman_{0:03}",
        'filename_export_range': "_Halaman_{0}-{1}",
        'filename_export_multiple': "_Halaman_{0}",
        'filename_with_text': "_dengan_Teks",
        'filename_with_signature': "_dengan_Tandatangan",
        'filename_with_image': "_dengan_Imej",
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
        'view_toggle_navbar': "Tunjukkan bar butang",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Tidak boleh memadam semua halaman",
		'pages_cannot_delete_last_page': 'Halaman terakhir tidak boleh dipadam!',
		'pages_cannot_delete_all_pages': 'Sekurang-kurangnya satu halaman mesti kekal dalam dokumen!',
		'delete_pages_confirm': 'Adakah anda pasti mahu memadam {0} halaman?',
		'delete_pages_confirm_voice': 'Adakah anda pasti mahu memadam {0} halaman?',
		'pages_deleted': '{0} halaman berjaya dipadam.',
		'warning': 'Amaran',
		'error': 'Ralat',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Tiada borang dipilih",
        'form_customized': "Borang disesuaikan",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Pilih",
        'btn_use': "Guna",
        'master_password_for_spasswords': "Untuk menyimpan dan menggunakan kata laluan, anda perlu menyediakan kata laluan induk terlebih dahulu.\n\nAdakah anda ingin menyediakan kata laluan induk sekarang?",
        'open_saved_dialog_title': "Buka fail yang disimpan",
        'open_saved_question': "Adakah anda ingin membuka fail yang disimpan sekarang?",
        'password': "Kata laluan",
        'password_manager_master_required': "Pengurus kata laluan hanya tersedia jika kata laluan induk telah disediakan.\n\nAdakah anda ingin menyediakan kata laluan induk sekarang?",
        'password_master_required_for_select': "Untuk melihat dan memilih kata laluan yang disimpan, anda mesti mengesahkan dengan kata laluan induk anda terlebih dahulu.\n\nAdakah anda ingin mengesahkan sekarang?",
        'password_not_available': "Kata laluan yang dipilih tidak tersedia atau tidak dapat dinyahsulit.",
        'password_options_title': "Pilihan kata laluan",
        'password_save_choice_change': "Tetapkan kata laluan baharu",
        'password_save_choice_keep': "Gunakan kata laluan sedia ada",
        'password_save_choice_none': "Simpan tanpa penyulitan",
        'password_save_hint': "Sediakan kata laluan induk terlebih dahulu untuk menyimpan kata laluan dengan selamat.",
        'password_save_master_required': "Simpan kata laluan (hanya mungkin dengan kata laluan induk)",
        'password_save_question': "PDF semasa dilindungi kata laluan. Adakah anda ingin menggunakan kata laluan sedia ada, tetapkan yang baharu atau simpan tanpa penyulitan?",
        'password_select': "Pilih kata laluan",
        'password_select_none': "Tiada kata laluan dipilih.\n\nSila pilih kata laluan daripada senarai.",
        'password_select_one': "Sila pilih tepat satu kata laluan.\n\nAnda telah menandakan beberapa kata laluan.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_sandaran",
        'filename_insert_suffix': "_dengan_sisipan",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_halaman_dipadam",
        'filename_pages_moved': "_halaman_dialih",
        'filename_rotated_all_suffix': "_semua_halaman_diputar",
        'filename_rotated_suffix': "_halaman_diputar",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurasi nama fail apabila mengubah PDF",
        'filename_keep_suffixes': "Kekalkan sambungan sebelumnya (cth. _dengan_teks)",
        'filename_keep_suffixes_false': "Ganti",
        'filename_keep_suffixes_true': "Kekalkan",
        'filename_preview_label': "Pratonton nama fail:",
        'filename_preview_overwrite_hint': "Pratonton tidak tersedia – fail asal akan ditimpa.",
        'filename_separator': "Pemisah antara perkataan",
        'filename_separator_none': "Tiada pemisah",
        'filename_separator_space': "Ruang ( )",
        'filename_separator_underscore': "Garis bawah (_)",
        'filename_settings_saved': "Tetapan nama fail disimpan",
        'filename_settings_title': "Pemformatan nama fail dan sandaran",
        'filename_timestamp_position': "Kedudukan cap masa",
        'filename_timestamp_position_after': "Selepas nama asas",
        'filename_timestamp_position_before': "Paling depan",
        'filename_timestamp_position_end': "Di hujung",
        'filename_use_timestamp': "Guna cap masa",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Kelakuan semasa perubahan:</b><ul><li>Padam dan sisip halaman</li><li>Sisip teks, tandatangan, imej dan bentuk</li><li>OCR</li></ul></html>",
        'backup_section': "Sandaran untuk operasi halaman (Padam, Alih)",
        'behavior_info': "Nota: Pada 'Timpa asal', cap masa dan akhiran diabaikan – fail mengekalkan namanya.",
        'behavior_new_file': "Sentiasa cipta fail baharu (dengan cap masa dan akhiran)",
        'behavior_overwrite': "Timpa asal (tiada fail baharu)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Semua halaman telah diputar.\n\nAsal tidak berubah.\nFail baharu: {0}",
        'all_pages_rotated_voice': "Semua halaman diputar, fail baharu dicipta.",
        'empty_pages_deleted_new_file': "{0} halaman kosong telah dipadam.\n\nAsal tidak berubah.\nFail baharu: {1}",
        'empty_pages_deleted_voice': "{0} halaman kosong dipadam, fail baharu dicipta.",
        'ocr_keep_original': "Kekalkan asal (buka secara manual kemudian)",
        'ocr_new_file_question': "PDF baharu yang boleh dicari telah disimpan di:\n{0}\n\nAdakah anda ingin membukanya sekarang?",
        'ocr_open_new': "Buka fail OCR baharu",
        'ocr_original_kept': "Fail asal kekal terbuka. Fail OCR telah disimpan.",
        'page_deleted_new_file': "Halaman {0} telah dipadam.\n\nAsal tidak berubah.\nFail baharu: {1}",
        'page_deleted_voice': "Halaman {0} dipadam, fail baharu dicipta.",
        'page_rotated_new_file': "Halaman {0} telah diputar.\n\nAsal tidak berubah.\nFail baharu: {1}",
        'page_rotated_voice': "Halaman {0} diputar, fail baharu dicipta.",
        'pages_deleted_new_file': "{0} halaman telah dipadam.\n\nFail asal tidak berubah.\nFail baharu: {1}",
        'pages_deleted_new_file_voice': "{0} halaman dipadam, fail baharu dicipta.",
        'pages_inserted_new_file': "{0} halaman telah disisip.\n\nFail asal tidak berubah.\nFail baharu: {1}",
        'pages_inserted_new_file_ask': "{0} halaman telah disisip.\n\nAsal tidak berubah.\nFail baharu: {1}\n\nAdakah anda ingin membukanya sekarang?",
        'pages_inserted_voice_new': "{0} halaman disisip, fail baharu dicipta.",
        'pages_moved_new_file': "{0} halaman telah dialih.\n\nFail asal tidak berubah.\nFail baharu: {1}",
        'pages_moved_new_file_voice': "{0} halaman dialih, fail baharu dicipta.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Jangan tunjuk lagi",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Tetapan sandaran</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Sandaran HIDUP</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Pada semua perubahan yang menimpa asal</strong> (teks, tandatangan, imej, bentuk, OCR, putar, sisip, padam/ali halaman) <strong>sandaran dengan cap masa dicipta secara automatik</strong> sebelum perubahan digunakan.</p>
                <p style="margin: 5px 0 5px 20px;">• Sandaran terletak di sebelah fail asal (cth. <code>Dokumen_sandaran_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Jika anda juga telah mengaktifkan pilihan <strong>„Timpa asal“</strong>, sandaran juga dicipta.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Sandaran MATI</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Tiada sandaran dicipta</strong> – tidak semasa menimpa mahupun pada operasi halaman.</p>
                <p style="margin: 5px 0 5px 20px;">• Fail asal mungkin hilang secara tidak boleh dipulihkan apabila ditimpa.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Hanya disyorkan untuk pengguna berpengalaman!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Petua:</strong> Tetapan sandaran adalah bebas daripada pilihan „Timpa asal“. Anda boleh menggabungkan kedua-duanya.<br>
                Anda boleh menyembunyikan mesej ini secara kekal.
            </div>
        </div>
        """,
        'backup_info_title': "Kelakuan sandaran",
        'backup_info_voice': "Notis tentang kelakuan sandaran pada operasi halaman. Sandaran hidup menimpa asal, sandaran mati mencipta fail baharu.",
        'show_backup_info': "Maklumat tentang tetapan sandaran",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Jangan tunjuk lagi",
        'overwrite_enable_backup': "Aktifkan sandaran (disyorkan)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Timpa asal</p>
            <p>Jika anda mengaktifkan pilihan ini, perubahan (teks, tandatangan, imej, bentuk, OCR, putar, sisip) <strong>disimpan terus dalam asal</strong> – <strong>tiada fail baharu dicipta</strong>.</p>
            <p>• Nama fail tidak berubah.<br>
            • Cap masa dan akhiran diabaikan.<br>
            • <strong>Tanpa sandaran, asal mungkin hilang secara tidak boleh dipulihkan.</strong></p>
            <p style="color: #FFD700;">Cadangan: Aktifkan juga pilihan sandaran untuk mendapatkan salinan keselamatan automatik.</p>
        </div>
        """,
        'overwrite_info_title': "Timpa asal",
        'overwrite_info_voice': "Amaran: Timpa asal – tiada fail baharu. Sandaran disyorkan.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} halaman telah disisip.\n\nFail asal telah ditimpa.\nSandaran telah dicipta.",
        'pages_inserted_overwrite_no_backup': "{0} halaman telah disisip.\n\nFail asal telah ditimpa.\nTIADA sandaran dicipta.",
        'texts_saved_overwrite_with_backup': "Perubahan telah disimpan dalam asal.\n\nSandaran telah dicipta.",
        'texts_saved_overwrite_no_backup': "Perubahan telah disimpan dalam asal.\n\nTIADA sandaran dicipta.",
        'texts_crosses_saved_new_file': "{0} {1} dan {2} {3} telah disisip.\n\nFail asal tidak berubah.\nFail baharu telah dicipta.\n\nPDF baharu sedang dimuat...",
        'texts_saved_new_file': "{0} {1} telah disisip.\n\nFail asal tidak berubah.\nFail baharu telah dicipta.\n\nPDF baharu sedang dimuat...",
        'crosses_saved_new_file': "{0} {1} telah disisip.\n\nFail asal tidak berubah.\nFail baharu telah dicipta.\n\nPDF baharu sedang dimuat...",
        'elements_saved_new_file': "{0} elemen telah disisip.\n\nFail asal tidak berubah.\nFail baharu telah dicipta.\n\nPDF baharu sedang dimuat...",
        'signatures_saved_overwrite_with_backup': "Tandatangan telah disimpan dalam asal.\n\nSandaran telah dicipta.",
        'signatures_saved_overwrite_no_backup': "Tandatangan telah disimpan dalam asal.\n\nTIADA sandaran dicipta.",
        'images_saved_overwrite_with_backup': "Imej telah disimpan dalam asal.\n\nSandaran telah dicipta.",
        'images_saved_overwrite_no_backup': "Imej telah disimpan dalam asal.\n\nTIADA sandaran dicipta.",
        'forms_saved_overwrite_with_backup': "Bentuk telah disimpan dalam asal.\n\nSandaran telah dicipta.",
        'forms_saved_overwrite_no_backup': "Bentuk telah disimpan dalam asal.\n\nTIADA sandaran dicipta.",
        'signatures_saved_new_file': "{0} tandatangan telah disisip.\n\nFail asal tidak berubah.\nFail baharu telah dicipta.\n\nPDF baharu sedang dimuat...",
        'images_saved_new_file': "{0} imej telah disisip.\n\nFail asal tidak berubah.\nFail baharu telah dicipta.\n\nPDF baharu sedang dimuat...",
        'forms_saved_new_file': "{0} bentuk telah disisip.\n\nFail asal tidak berubah.\nFail baharu telah dicipta.\n\nPDF baharu sedang dimuat...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Amaran: PDF ini mengandungi halaman yang diputar. Kedudukan mungkin menyimpang.",
        'page_rotated_warning_title': "Halaman diputar dikesan",
        'page_rotated_warning_message': "Halaman semasa {0} diputar {1}°.\n\nMenyisipkan elemen pada halaman yang diputar tidak disokong.\n\nAdakah anda ingin memutar halaman ke kedudukan tegak sekarang?",
        'page_rotated_warning_voice': "Amaran: Halaman diputar. Sila putarkannya terlebih dahulu.",
        'paste_on_rotated_page_simple_warning': "Penyisipan pada halaman {0} tidak mungkin!\n\nHalaman ini diputar {1}°.\n\nSila putar halaman ke 0° terlebih dahulu (Menu: Edit → Selaraskan halaman).\n\nAmaran:\nElemen yang disalin sebelum ini akan hilang jika anda tidak menyimpan sebelum memutar halaman.",
        'paste_on_rotated_page_voice': "Penyisipan dibatalkan. Halaman diputar. Sila selaraskan halaman terlebih dahulu.",
        'page_rotated_cancel': "Batal",
        'page_rotated_rotate_until_upright': "Putar halaman berulang kali (sehingga tegak)",
        'page_rotated_now_upright': "Halaman kini tegak. Anda kini boleh menyisip.",
        'page_rotated_still_not_upright': "Halaman tidak dapat diputar ke kedudukan tegak. Sila betulkan secara manual.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Bantuan: Betulkan halaman yang diputar",
        'help_rotated_pages_voice': "Bantuan untuk membetulkan halaman yang diputar dibuka.",
        'btn_help': "Bantuan",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Masalah: Halaman diputar – Penyisipan tidak berfungsi dengan betul</p>

            <p>Jika penyisipan teks, tandatangan atau bentuk pada halaman yang diputar tidak berfungsi dengan betul, anda boleh membetulkan halaman dengan editor PDF luaran.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Penyelesaian dengan alat luaran (cth. Pratonton macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksport halaman</strong><br>
                &nbsp;&nbsp;Klik dalam menu pada <strong>Fail → Eksport sebagai Halaman</strong> atau gunakan kaedah lain untuk menyimpan halaman yang dikehendaki sebagai PDF tunggal.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Buka halaman dalam program luaran</strong><br>
                &nbsp;&nbsp;Buka PDF yang dieksport dalam editor PDF (cth. <strong>Pratonton macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Putar halaman</strong><br>
                &nbsp;&nbsp;Putar halaman supaya ia tegak (dalam Pratonton: <strong>Alat → Putar</strong> atau <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Simpan</strong><br>
                &nbsp;&nbsp;Simpan halaman yang telah dibetulkan (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Sisipkan semula halaman ke dalam dokumen asal</strong><br>
                &nbsp;&nbsp;Kembali ke PDFDarkView dan sisipkan halaman yang telah dibetulkan pada kedudukan yang dikehendaki:<br>
                &nbsp;&nbsp;<strong>Edit → Sisip halaman</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatif: Putar halaman dalam asal</p>
                <p style="margin: 5px 0 5px 20px;">• Gunakan fungsi putar terbina dalam (<strong>Edit → Putar halaman</strong>) untuk membetulkan halaman langkah demi langkah.<br>
                • Selepas setiap putaran, anda boleh memeriksa sama ada penyisipan kini berfungsi.<br>
                • Ini selalunya penyelesaian yang lebih cepat – cuba dahulu!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Petua:</strong> Jika anda sering menemui halaman yang diputar, anda boleh menyembunyikan amaran dalam dialog sisipan secara kekal.<br>
                Kedudukan kemudian mungkin menyimpang – gunakan pilihan ini hanya jika anda tahu akibatnya.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Selaraskan halaman",
        'menu_rotate_normalize_tooltip': "Putar halaman atau tetapkan semula ke 0°",
        'normalize_current_page': "Bawa halaman semasa ke kedudukan tegak (tetapkan ke 0°)",
        'normalize_all_pages': "Bawa semua halaman ke kedudukan tegak (tetapkan ke 0°)",
        'page_normalized': "Halaman {0} ditetapkan ke kedudukan tegak.",
        'all_pages_normalized': "Semua halaman ditetapkan ke kedudukan tegak.",
        'page_already_upright': "Halaman {0} sudah tegak.",
        'all_pages_already_upright': "Semua halaman sudah tegak.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF tidak mengandungi teks yang boleh dicari.</p><p>Adakah anda ingin melakukan OCR untuk mengeksport ke {0}?</p>",
        'export_ocr_voice': "PDF tidak mengandungi teks. OCR diperlukan untuk eksport ke {0}.",
        'export_no_ocr_possible': "Eksport tanpa OCR tidak mungkin. Sila lakukan OCR melalui menu.",
        'ocr_failed_export_not_possible': "OCR gagal. Eksport tidak dapat dilakukan.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF akan dibuka dalam Pratonton. Sila mulakan proses pencetakan di sana.",
        'print_preview_manual': "PDF telah dibuka. Sila laksanakan arahan cetak secara manual (cth. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Cantumkan PDF",
        'merge_pdfs': "Cantumkan PDF",
        'merge_progress_title': "Mencantumkan PDF...",
        'merge_pdfs_list': "PDF mengikut susunan (Seret dan lepas untuk menyusun)",
        'merge_add_pdf': "Tambah PDF",
        'merge_remove': "Buang",
        'merge_move_up': "Naik",
        'merge_move_down': "Turun",
        'merge_pdfs_info': "💡 Petua: Anda boleh menukar susunan dengan menyeret dan melepas",
        'merge_no_pdfs': "Tiada PDF dipilih. Klik pada 'Tambah PDF'.",
        'merge_info': "{0} PDF dipilih (kira-kira {1} halaman)",
        'merge_open_file': "Buka fail",
        'merge_merge': "Cantumkan",
        'merge_error': "Ralat semasa mencantumkan",
        'merge_min_two_pdfs_error': "Sila pilih sekurang-kurangnya dua fail PDF untuk dicantumkan.",
        'merge_select_pdfs': "Pilih PDF untuk dicantumkan",
        'merge_error_file': "Ralat semasa memproses",
        'merge_cancelled': "Pencantuman dibatalkan",
        'merge_preparing': "Bersedia...",
        'merge_processing': "Memproses PDF {0} daripada {1}",
        'merge_saving': "Menyimpan PDF yang dicantumkan...",
        'merge_complete': "Selesai!",
        'merge_success_title': "Pencantuman berjaya",
        'merge_success_voice': "{0} PDF berjaya dicantumkan.",
        'merge_success_message': "{0} PDF berjaya dicantumkan.\n\nDokumen baharu kini mempunyai {1} halaman.\n\nFail baharu:\n{2}\n\nLokasi simpanan:\n{3}\n{2}\n\nAdakah anda ingin membuka PDF ini?",
        'replace_file_title': "Gantikan fail?",
        'replace_file_message': "PDF sudah dibuka. Adakah anda ingin menggantikannya dengan fail baharu?",
        'btn_yes': "Ya",
        'btn_no': "Tidak",
        'filename_merge_suffix': "dicantumkan",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Membuka {0}...",
        'progress_merge_reading': "Membaca {0}...",
        'progress_merge_adding': "Menambah {0} halaman...",
        'progress_merge_optimizing': "Mengoptimumkan PDF...",
        'progress_merge_writing': "Menulis PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "menutup PDF",
        'action_close_window': "menutup tetingkap",
        'action_open_new_pdf': "membuka PDF baharu",
        'action_quit_app': "keluar dari aplikasi",
        'changes_saved': "Perubahan telah disimpan.",
        'file_close_title': "Tutup fail PDF",
        'save_before_action': "Perlukah perubahan disimpan sebelum {0}? Ya atau Tidak?",
        'save_before_action_voice': "Perlukah perubahan disimpan sebelum {0}? Ya atau Tidak?",
        'save_before_close_question': "Perlukah perubahan disimpan sebelum menutup? Ya atau Tidak?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF yang boleh dicari dicipta:\n\n{0}\n\n<b>cuba lagi jika perlu",
        "ocr_rotate_title": "Jajarkan halaman sebelum OCR",
        "ocr_rotate_question": "PDF mengandungi halaman yang diputar.\nAdakah anda ingin menjajarkan semua halaman ke 0° sebelum OCR?\nIni meningkatkan pengecaman teks dengan ketara.",
        "ocr_rotate_yes": "Ya, jajarkan",
        "ocr_rotate_no": "Tidak, mulakan OCR terus",
        "ocr_rotate_voice": "PDF mengandungi halaman yang diputar. Perlukah semua halaman dijajarkan sebelum OCR?",
        "ocr_not_performed_message": "Tiada teks. Sila lakukan OCR (menu \"Sunting\" → \"Lakukan OCR\" atau kekunci Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Tetapan OCR",
        "ocr_language_btn": "Pilih bahasa OCR",
        "ocr_language": "Bahasa OCR",
        "ocr_language_current": "Bahasa semasa:",
        "ocr_param_info": "Maklumat tentang parameter",

        "ocr_force_ocr_label": "Paksa OCR",
        "ocr_deskew_label": "Betulkan condong",
        "ocr_clean_label": "Bersihkan imej",
        "ocr_oversample_label": "Resolusi (DPI)",
        "ocr_pagesegmode_label": "Pembahagian halaman",
        "ocr_oem_label": "Mod enjin OCR",
        "ocr_optimize_label": "Mampatan PDF",
        "ocr_jobs_label": "Proses selari",
        "ocr_verbose_label": "Perincian log",

        "ocr_force_ocr_tooltip": "Paksa OCR pada setiap halaman, walaupun teks sudah wujud",
        "ocr_deskew_tooltip": "Jajarkan imbasan condong secara automatik",
        "ocr_clean_tooltip": "Buang bunyi dan artifak daripada imej",
        "ocr_oversample_tooltip": "Besarkan imej sebelum OCR ke DPI ini",
        "ocr_pagesegmode_tooltip": "Menentukan bagaimana halaman dibahagikan kepada kawasan teks",
        "ocr_oem_tooltip": "Memilih enjin OCR Tesseract",
        "ocr_optimize_tooltip": "Tahap mampatan PDF keluaran",
        "ocr_jobs_tooltip": "Bilangan proses OCR selari",
        "ocr_verbose_tooltip": "Tahap perincian keluaran log",
        "ocr_settings_explain_btn": "Penjelasan",

        "ocr_force_ocr_explain": "Memaksa pengecaman teks pada <b>setiap</b> halaman, walaupun ia sudah mengandungi teks.\n\nCadangan: <b>Hidup</b> untuk PDF yang diimbas, <b>Mati</b> untuk PDF asli dengan teks sedia ada.",

        "ocr_deskew_explain": "Membetulkan imbasan yang sedikit condong (sehingga kira-kira 5°).\n\nCadangan: <b>Hidup</b> untuk dokumen yang diimbas, <b>Mati</b> jika halaman sudah lurus dengan sempurna.",

        "ocr_clean_explain": "Membuang bunyi, titik dan artifak kecil daripada imej.\n<b>PENTING:</b> Untuk teks Arab, Thai atau Vietnam dengan tanda diakritik (titik di atas/bawah huruf) pilihan ini harus <b>dinyahaktifkan</b>, jika tidak aksara penting mungkin hilang.",

        "ocr_oversample_explain": "Membesarkan imej <b>sebelum</b> pengecaman teks ke DPI yang ditentukan.<br><br>• <b>72-150 DPI:</b> Sangat cepat, tetapi kadar pengecaman rendah<br>• <b>200-300 DPI:</b> Julat optimum (Default: 300)<br>• <b>400+ DPI:</b> Hampir tiada pengecaman lebih baik, tetapi fail jauh lebih besar<br><br>Cadangan: 300 DPI untuk skrip kompleks (Arab, Cina, Jepun), 200 DPI untuk bahasa Barat.",

        "ocr_pagesegmode_explain": "Menentukan bagaimana Tesseract membahagikan halaman kepada kawasan teks.\n\n• <b>3 - Automatik (Default):</b> Baik untuk susun atur bercampur\n• <b>4 - Lajur tunggal:</b> Untuk teks lajur tunggal\n• <b>5 - Blok menegak:</b> Untuk skrip menegak (Jepun, Cina)\n• <b>6 - Blok teks seragam:</b> Optimum untuk teks mengalir tanpa lajur\n• <b>11 - Imej mentah:</b> Untuk imbasan buruk / tulisan tangan\n\nCadangan: <b>6</b> untuk dokumen teks mudah, <b>3</b> untuk susun atur kompleks.",

        "ocr_oem_explain": "Memilih enjin OCR Tesseract.\n\n• <b>0 - Legacy:</b> Enjin lama (cepat, tetapi kurang tepat)\n• <b>1 - LSTM:</b> Enjin neural (lebih perlahan, tetapi lebih tepat)\n• <b>2 - Legacy + LSTM:</b> Menggabungkan kedua-dua keputusan\n• <b>3 - Default (LSTM diutamakan):</b> Pilihan terbaik untuk kebanyakan kes\n\nCadangan: <b>3</b> untuk ketepatan pengecaman maksimum.",

        "ocr_optimize_explain": "Memampatkan PDF keluaran.\n\n• <b>0:</b> Tiada pengoptimuman (pemprosesan terpantas)\n• <b>1:</b> Pengoptimuman ringan (kompromi yang baik)\n• <b>2:</b> Pengoptimuman sederhana\n• <b>3:</b> Pengoptimuman kuat (fail terkecil, tetapi lebih perlahan)\n\nCadangan: <b>1</b> untuk kegunaan harian.",

        "ocr_jobs_explain": "Bilangan proses selari untuk OCR.\n\n• <b>1:</b> Perlahan, tetapi penggunaan memori paling rendah\n• <b>4-8:</b> Optimum untuk pemproses berbilang teras moden\n• <b>12+:</b> Hampir tiada pemprosesan lebih cepat dengan penggunaan memori tinggi\n\nCadangan: Bilangan teras CPU (cth. <b>4</b> pada sistem 4 teras).",

        "ocr_verbose_explain": "Tahap perincian keluaran log dalam konsol.\n\n• <b>0:</b> Tiada keluaran\n• <b>1:</b> Kemajuan dan mesej status\n• <b>2:</b> Keluaran terperinci\n• <b>3:</b> Keluaran debug penuh (sangat luas)\n\nCadangan: <b>1</b> untuk operasi normal.",

        "ocr_reset_title": "Tetapan telah ditetapkan semula",
        "ocr_reset_message": "Semua tetapan OCR telah ditetapkan semula kepada nilai default.",
        "info_tooltip": "Maklumat lanjut tentang parameter ini",
        "ocr_reset_defaults": "Tetapkan semula kepada default",

        "ocr_psm_0": "Automatik (enjin Legacy)",
        "ocr_psm_1": "Pengesanan lajur automatik",
        "ocr_psm_3": "Automatik (Default)",
        "ocr_psm_4": "Lajur tunggal",
        "ocr_psm_5": "Blok menegak",
        "ocr_psm_6": "Blok teks seragam",
        "ocr_psm_7": "Baris teks tunggal",
        "ocr_psm_8": "Perkataan tunggal",
        "ocr_psm_11": "Imej mentah (tiada analisis susun atur)",

        "ocr_oem_0": "Enjin Legacy (cepat)",
        "ocr_oem_1": "Enjin LSTM (neural, tepat)",
        "ocr_oem_2": "Legacy + LSTM digabungkan",
        "ocr_oem_3": "Default (LSTM diutamakan)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Bahasa OCR...",
        "ocr_language_title": "Pilih bahasa OCR",
        "ocr_language_instruction": "Pilih bahasa untuk pengecaman teks (OCR).\nPerhatian: Berbilang bahasa menjejaskan prestasi dan ketepatan!\nAnda mendapat hasil terbaik jika hanya memilih satu bahasa.",
        "ocr_language_predefined": "Gabungan yang telah ditetapkan",
        "ocr_language_custom": "Tersuai...",
        "ocr_language_selected": "Bahasa OCR yang dipilih",
        "ocr_language_changed": "Bahasa OCR ditukar kepada {0}",
        "ocr_language_auto_detect": "Bahasa yang tersedia dikesan secara automatik.",
        "ocr_language_none_found": "Tiada data bahasa Tesseract ditemui! Sila pasang pakej bahasa (cth. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Pilihan bahasa tersuai",
        "ocr_language_available": "Bahasa yang tersedia (dipasang):",
        "ocr_language_select_hint": "Pilih satu atau lebih bahasa:",
        "ocr_language_confirm": "Guna",
        "ocr_language_reset": "Tetapkan semula kepada default (deu+eng+vie)",
        "ocr_language_priorities": "Bahasa yang disyorkan (dipasang terlebih dahulu):",

        "select_all_languages": "Pilih semua",
        "clear_all_languages": "Kosongkan pilihan",
        "install_language_packs": "Pasang pakej bahasa yang hilang...",
        "install_hint": "💡 Petua: Tidak semua bahasa dipasang pada sistem anda. Melalui butang ini anda akan mendapat bantuan pemasangan.",
        "ocr_language_install_title": "Pemasangan pakej bahasa Tesseract",

        "ocr_missing_languages": "Pakej bahasa OCR yang hilang",
        "ocr_missing_languages_message": "Bahasa-bahasa yang dipilih berikut tidak dipasang pada sistem anda:\n\n{0}\n\nSila pasang pakej bahasa yang hilang (lihat bantuan di bawah 'Bantuan Pemasangan').\n\nAdakah anda ingin membuka bantuan pemasangan sekarang?",
        "ocr_missing_languages_voice": "Pakej bahasa hilang. Sila pasang bahasa yang hilang.",
        "ocr_install_help_now": "Buka bantuan",
        "ocr_continue_anyway": "Tetap cuba",
        "ocr_language_error_title": "Ralat bahasa OCR",
        "ocr_language_error_message": "Ralat semasa pengecaman teks: {0}\n\nSila periksa tetapan bahasa OCR anda (Tetapan → Bahasa OCR).",
        "ocr_install_help_button": "Bantuan Pemasangan",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Pasang pakej bahasa Tesseract</p>

        <p>Untuk OCR berfungsi dalam bahasa tertentu, data bahasa yang sepadan mesti dipasang pada sistem anda. Ikut arahan untuk sistem pengendalian anda:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Buka <strong>Terminal</strong> (Finder → Program → Utiliti → Terminal).</li>
        <li>Pasang semua bahasa yang tersedia dengan:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Ini mungkin mengambil masa beberapa minit.)</li>
        <li>Atau hanya bahasa individu (cth. Vietnam):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Dengan versi Homebrew semasa, <code>*.traineddata</code> mungkin perlu dimuat turun secara manual (lihat di bawah).</li>
        <li>Selepas pemasangan: Tutup dialog ini dan buka semula pemilihan bahasa OCR – bahasa baharu akan muncul secara automatik.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Buka terminal (Ctrl+Alt+T).</li>
        <li>Pasang bahasa yang dikehendaki, cth. untuk Vietnam:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Kod bahasa penting: <code>deu</code> (Jerman), <code>eng</code> (Inggeris), <code>vie</code> (Vietnam), <code>spa</code> (Sepanyol), <code>fra</code> (Perancis), <code>ita</code> (Itali), <code>nld</code> (Belanda), <code>fin</code> (Finland), <code>swe</code> (Sweden), <code>nor</code> (Norway).</li>
        <li>Tunjukkan semua pakej yang tersedia:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Muat turun fail <code>*.traineddata</code> yang dikehendaki dari:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (cth. <code>vie.traineddata</code> untuk Vietnam).</li>
        <li>Salin fail ke folder bahasa Tesseract, biasanya:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Sesuaikan dengan pemasangan individu.)</li>
        <li>Mulakan semula aplikasi (atau buka semula pemilihan bahasa OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatif untuk semua sistem</p>
        <ul>
        <li>Pasang <strong>OCRmyPDF</strong> dan <strong>Tesseract</strong> dengan pengurus pakej pilihan anda. Kebanyakan pemasangan sudah mengandungi beberapa bahasa standard (Inggeris, Jerman, Perancis).</li>
        <li>Bahasa yang hilang boleh dipasang pada bila-bila masa – pemilihan bahasa OCR hanya menyenaraikan bahasa yang benar-benar wujud.</li>
        </ul>

        <hr>
        <p><b>✅ Selepas pemasangan:</b> Tidak perlu memulakan semula aplikasi – bahasa yang baru ditambahkan akan muncul dengan serta-merta dalam senarai.</p>
        <p><b>📖 Bantuan untuk kod bahasa:</b> Senarai lengkap boleh didapati dalam <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentasi Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Font Noto Sans",
        "info_noto_font_voice": "Panduan pemasangan font Noto Sans",
        "btn_info_noto_font_install": "Maklumat font",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Cara memasang font Noto percuma daripada Google</h2>

        <p><strong>Font Noto</strong> ialah keluarga font sumber terbuka daripada Google. Matlamat mereka adalah untuk tidak melihat <em>"tauhu"</em> (iaitu tiada kotak kosong □) dan memaparkan setiap aksara daripada standard Unicode dengan betul. Ia adalah tambahan yang ideal untuk aplikasi yang perlu memaparkan teks dalam pelbagai bahasa yang berbeza.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Pemasangan pada macOS</h3>

        <p><strong>Kaedah 1: Dengan Homebrew (untuk lanjutan)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Kaedah 2: Melalui "Font Book" (Disyorkan)</strong></p>

        <ol>
        <li>Muat turun pakej font rasmi:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ekstrak fail ZIP</li>
        <li>Salin fail ke <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Pemasangan pada Windows (10 & 11)</h3>

        <p><strong>Kaedah 1: Microsoft Store (Disyorkan)</strong><br>
        Cari "Google Noto Fonts" atau "Noto Sans" dan klik <strong>Pasang</strong>.</p>

        <p><strong>Kaedah 2: Pemasangan manual</strong></p>

        <ol>
        <li>Muat turun:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ekstrak ZIP</li>
        <li>Pilih fail .ttf / .otf</li>
        <li>Klik kanan → <strong>Pasang</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        atau<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nama\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Pemasangan pada Linux</h3>

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

        <p>Pengesahan:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Urus tanda buku",
        "bookmark_add": "Tambah tanda buku",
        "bookmark_add_tooltip": "Simpan halaman semasa sebagai tanda buku",
        "bookmark_remove": "Buang tanda buku",
        "bookmark_remove_tooltip": "Padam tanda buku yang ditanda",
        "bookmark_remove_all": "Buang semua",
        "bookmark_remove_all_tooltip": "Padam semua tanda buku PDF ini",
        "bookmark_jump": "Pergi ke tanda buku",
        "bookmark_jump_tooltip": "Pergi ke halaman yang dipilih",
        "bookmark_name": "Nama",
        "bookmark_page": "Halaman",
        "bookmark_no_bookmarks": "Tiada tanda buku.\nKlik 'Tambah' untuk menyimpan halaman semasa sebagai tanda buku.",
        "bookmark_added": "Tanda buku untuk halaman {0} ditambah: {1}",
        "bookmark_removed": "Tanda buku dibuang: {0}",
        "bookmark_all_removed": "Semua tanda buku telah dibuang.",
        "bookmark_name_default": "Halaman {0}",
        "bookmark_name_prompt": "Nama untuk tanda buku:\n(teks panjang akan dipendekkan kepada 50 aksara)",
        "bookmark_name_prompt_title": "Nama tanda buku",
        "bookmark_confirm_remove_all": "Adakah anda pasti ingin membuang semua {0} tanda buku?",
        "menu_bookmarks": "Tanda buku",
        "bookmark_manage": "Urus tanda buku",
        "bookmark_next": "Tanda buku seterusnya",
        "bookmark_prev": "Tanda buku sebelumnya",
        "bookmark_page_display": "Halaman {0}",
        "bookmark_exists": "Tanda buku untuk halaman ini dengan nama ini sudah wujud.",
        "bookmark_select_first": "Sila pilih tanda buku terlebih dahulu.",
        "bookmark_confirm_remove": "Adakah anda pasti ingin membuang tanda buku 'Halaman {0}: {1}'?",
        "bookmark_jumped_to": "Pergi ke tanda buku '{0}' pada halaman {1}.",
        "bookmark_jumped_to_voice": "Tanda buku {0}, halaman {1}",
        "btn_close": "Tutup",

        "bookmark_list": "Tanda buku anda",
        "bookmark_rename": "Ubah nama tanda buku",
        "bookmark_rename_tooltip": "Tukar nama tanda buku yang dipilih",
        "bookmark_rename_title": "Ubah nama tanda buku",
        "bookmark_rename_prompt": "Nama baharu untuk tanda buku pada halaman {0}:\n(maks. 50 aksara)",
        "bookmark_renamed": "Tanda buku '{0}' telah dinamakan semula kepada '{1}'.",
        "bookmark_item_tooltip": "Halaman {0}: {1}\nKlik dua kali untuk pergi",
        "bookmark_name_exists_question": "Tanda buku dengan nama '{0}' sudah wujud pada halaman ini.\nTetap ubah nama?",

        "context_bookmarks": "Tanda buku",
        "context_bookmark_add_here": "Tambah tanda buku untuk halaman ini",
        "context_bookmarks_existing": "Tanda buku sedia ada:",
        "context_bookmarks_jump": "Pergi ke tanda buku:",
        "context_bookmarks_none": "Tiada tanda buku",
        "context_bookmarks_clear_all": "Buang semua {0} tanda buku",

        "bookmark_search_placeholder": "Cari tanda buku... (nama atau halaman)",
        "bookmark_search_results": "%d tanda buku ditemui untuk \"%s\"",
        "bookmark_no_search_results": "Tiada tanda buku ditemui untuk \"%s\"",
        "bookmark_no_search_results_label": "Tiada hasil untuk \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Edit metadata PDF",
        "metadata_title": "Tajuk",
        "metadata_title_placeholder": "Tajuk dokumen",
        "metadata_title_tooltip": "Tajuk dokumen (ditunjukkan dalam bar tajuk)",
        "metadata_author": "Pengarang",
        "metadata_author_placeholder": "Nama pengarang",
        "metadata_author_tooltip": "Pencipta dokumen",
        "metadata_subject": "Subjek",
        "metadata_subject_placeholder": "Subjek dokumen",
        "metadata_subject_tooltip": "Penerangan ringkas kandungan",
        "metadata_keywords": "Kata kunci",
        "metadata_keywords_placeholder": "Kata kunci, dipisahkan dengan koma",
        "metadata_keywords_tooltip": "Kata kunci untuk mengkategorikan dokumen",
        "metadata_creator": "Pencipta",
        "metadata_creator_placeholder": "Aplikasi yang mencipta PDF",
        "metadata_creator_tooltip": "Perisian yang digunakan untuk mencipta dokumen",
        "metadata_producer": "Penerbit",
        "metadata_producer_placeholder": "Aplikasi yang menukar PDF",
        "metadata_producer_tooltip": "Perisian yang menukar PDF",
        "metadata_creation_date": "Tarikh penciptaan",
        "metadata_creation_date_tooltip": "Tarikh penciptaan dokumen",
        "metadata_mod_date": "Tarikh pengubahsuaian",
        "metadata_mod_date_tooltip": "Tarikh pengubahsuaian terakhir",
        "metadata_pdf_info": "📄 Maklumat PDF",
        "metadata_pages": "Bilangan halaman",
        "metadata_file_size": "Saiz fail",
        "metadata_pdf_version": "Versi PDF",
        "metadata_encrypted": "Disulitkan",
        "metadata_encrypted_yes": "Ya (dilindungi kata laluan)",
        "metadata_encrypted_no": "Tidak",
        "metadata_reload": "📂 Muat semula daripada PDF",
        "metadata_reset": "Buang perubahan",
        "metadata_reloaded": "Metadata telah dimuat semula daripada PDF.",
        "metadata_reset_done": "Semua medan metadata telah ditetapkan semula.",
        "metadata_no_file": "Tiada fail PDF dimuatkan.",
        "metadata_save_error": "Ralat semasa menyimpan metadata",
        "metadata_saved": "Metadata telah disimpan dengan jayanya.",
        "metadata_pdf_version_unknown": "PDF (tidak diketahui)",
        "metadata_saved_message": "Metadata telah disimpan dengan jayanya.",
        "metadata_saved_voice": "Metadata disimpan.",

        "metadata_custom": "🔧 Metadata tersuai",
        "metadata_custom_placeholder": "{\n  \"medan_saya\": \"nilai_saya\",\n  \"medan_lain\": 123\n}",
        "metadata_custom_tooltip": "Format JSON untuk metadata tersuai (pilihan)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Templat \"{0}\" dipilih - Klik dua kali untuk sisipkan",
        "text_use_template": "Guna blok teks",
        "text_type": "Jenis",
        "text_search_templates": "Cari blok teks...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Maklumat Eksport / Import",
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

        <h3>📦 Apakah yang dieksport? (Gambaran Keseluruhan)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Tetapan aplikasi am</span></li>
            <li class="detail">• Mod Gelap/Terang</li>
            <li class="detail">• Penyongsangan mod gelap untuk imej</li>
            <li class="detail">• Nilai ambang kelabu</li>
            <li class="detail">• Bahasa</li>
            <li class="detail">• Geometri tetingkap</li>
            <li class="detail">• Mod zum</li>
            <li class="detail">• Navigasi (Bar navigasi kelihatan)</li>
            <li class="detail">• Output pertuturan (hidup/mati)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Tetapan sandaran</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Penamaan fail (Cap masa, Pemisah, Akhiran)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Tetapan untuk sisipan</span></li>
            <li class="detail">• Tandatangan</li>
            <li class="detail">• Teks &amp; blok teks</li>
            <li class="detail">• Tanda, imej dan bentuk</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Tetapan OCR</span></li>
            <li class="detail">• Bahasa</li>
            <li class="detail">• Paksa OCR · Mod halaman</li>
            <li class="detail">• Pra-pemprosesan imej: Betulkan condong, Bersihkan, Persampelan berlebihan</li>
            <li class="detail">• Bilangan kerja selari</li>
            <li class="detail">• Mod penyongsangan</li>
            <li class="detail">• Nilai ambang kelabu</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Tanda buku</span></li>
            <li class="detail">• Semua tanda buku setiap fail PDF (Halaman, Nama, Masa penciptaan)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Pangkalan data kata laluan</span></li>
            <li class="detail">• Kata laluan PDF yang disimpan (pilihan disulitkan atau teks biasa)</li>
            <li class="detail">• Hash kata laluan master (jika ditetapkan)</li>
            <li class="detail">• Data pengesahan</li>
        </ul>

        <h4>⚠️ Nota penting</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Semasa mengimport:</strong>
            <ul>
                <li><span class="warning">➜ SEMUA tetapan semasa akan ditimpa sepenuhnya</span></li>
                <li>• Memulakan semula aplikasi adalah wajib</li>
                <li>• Tandatangan, blok teks dan tanda buku sedia ada akan diganti</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Kata laluan master dan mod eksport:</strong>
            <ul>
                <li>• Apabila kata laluan master aktif, anda boleh memilih:</li>
                <li>  - <span style="color: #98FB98;"><strong>Disahsulit</strong></span> (kata laluan dalam teks biasa dalam ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Disulitkan</strong></span> (hanya boleh dibaca dengan kata laluan master pada sistem sasaran)</li>
                <li>• Hash kata laluan master <strong>sentiasa</strong> disimpan disulitkan</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Notis keselamatan:</strong>
            <ul>
                <li>• Fail ZIP yang dieksport mengandungi data sensitif (<strong>kata laluan, tanda buku, tandatangan</strong>)</li>
                <li>• Sila simpan dengan selamat (cth. USB disulitkan, pengurus kata laluan)</li>
                <li>• Jika fail hilang, kata laluan PDF yang disimpan akan hilang selama-lamanya</li>
            </ul>
        </div>

        <h4>📁 Format eksport</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Tetapan disimpan dalam satu fail ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP ini mengandungi <code>settings.json</code> lengkap (dari konfigurasi anda) serta kemungkinan fail imej tandatangan terbenam dan kata laluan disulitkan.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Tandatangan - Panduan",
        'signature_guide_html': """
        📝 <strong>Tandatangan - Panduan Pantas</strong><br>
        <ul>
        <li>Set kata laluan induk</li>
        <li>Konfigurasikan tandatangan dalam menu <em>Tetapan</em> (saiz, cap masa, …)</li>
        <li>Sisipkan dengan <strong>KLIK KANAN</strong> pada kedudukan yang diingini (kata laluan induk diperlukan sekali setiap sesi)</li>
        <li>Gerakkan tandatangan dengan tetikus atau kekunci anak panah</li>
        <li>Sisipkan berbilang tandatangan berturut-turut</li>
        <li>Sesuaikan setiap tandatangan secara individu</li>
        <li>Buang tandatangan tunggal</li>
        <li>Simpan / buang semua tandatangan sekaligus</li>
        <li>Sebagai alternatif, bar menu juga boleh digunakan.</li>
        </ul>
        """,
        'signature_guide_voice': "Panduan pantas untuk tandatangan. Set kata laluan induk. Konfigurasikan tandatangan dalam tetapan. Sisipkan dengan klik kanan.",

        'image_guide_title': "Sisipkan gambar - Panduan",
        'image_guide_html': """
        📷 <strong>Sisipkan gambar ke PDF - Panduan Pantas</strong><br>
        <ol>
        <li>Klik kanan pada kedudukan yang diingini</li>
        <li><em>„Sisipkan gambar“</em> → Pilih gambar</li>
        <li>Letakkan gambar: Seret dengan tetikus</li>
        <li>Laraskan saiz: Seret pada sudut/tepi</li>
        <li>Kekalkan nisbah bidang: Kekunci <strong>[A]</strong></li>
        <li>Pelarasan selanjutnya: Klik kanan pada gambar</li>
        </ol>
        <p><strong>Petua:</strong> Dalam menu konteks, anda boleh melaraskan tetapan.</p>
        """,
        'image_guide_voice': "Panduan pantas untuk gambar. Klik kanan, sisipkan gambar, pilih. Letakkan dengan tetikus, laraskan saiz pada sudut. Nisbah bidang dengan kekunci A.",

        'form_guide_title': "Sisipkan bentuk - Panduan",
        'form_guide_html': """
        📐 <strong>Sisipkan bentuk ke PDF - Panduan Pantas</strong><br>
        <ol>
        <li>Pilih jenis bentuk (segi empat tepat, elips, garis, anak panah)</li>
        <li>Klik pada kedudukan:
            <ul>
            <li>Untuk segi empat tepat/elips: Satu klik meletakkan bentuk</li>
            <li>Untuk garis/anak panah: Dua klik untuk titik mula dan akhir</li>
            </ul>
        </li>
        <li>Letakkan bentuk: Seret dengan tetikus</li>
        <li>Laraskan saiz: Seret pada sudut/tepi</li>
        <li>Simpan bentuk: <strong>Enter</strong></li>
        <li>Buang bentuk: <strong>ESC</strong></li>
        <li>Pelarasan selanjutnya: Klik kanan pada bentuk</li>
        </ol>
        <p><strong>Petua:</strong> Dalam menu konteks, anda boleh melaraskan tetapan.</p>
        """,
        'form_guide_voice': "Panduan pantas untuk bentuk. Pilih jenis bentuk. Untuk segi empat tepat atau elips klik sekali, untuk garis atau anak panah klik dua kali. Letakkan dengan tetikus, laraskan saiz pada sudut. Simpan dengan Enter, buang dengan Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "sebelumnya",
        "btn_next_result": "seterusnya",
        "ocr_text_window": "Tetingkap teks OCR",
        "bookmark_existing": "Penanda buku sedia ada",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Perbandingan OCR Mac - Windows",
        'ocr_method_mac_win_title': "Perbezaan OCR antara Mac dan Windows",
        'ocr_method_mac_win_voice': "Mac lebih baik",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Perbezaan antara macOS dan Windows</strong></p>

        <p><strong>macOS (disyorkan)</strong></p>
        <p>Alat:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Hasil:</p>
        <ul>
        <li>PDF yang boleh dicari dengan teks terbenam yang sebahagian besarnya mengekalkan susun atur asal.</li>
        </ul>
        <p>Kelebihan:</p>
        <ul>
        <li>Kualiti pengecaman teks yang sangat baik (walaupun pada halaman yang bengkok).</li>
        <li>Pemeliharaan grafik vektor dan fon.</li>
        <li>Bar kemajuan GUI melalui penilaian subproses.</li>
        <li>Kawalan penuh ke atas semua parameter OCR (Deskew, Clean, Oversample, pengoptimuman).</li>
        <li>Carian teks tersedia terus dalam tetingkap utama (paparan PDF).</li>
        </ul>
        <p>Kekurangan:</p>
        <ul>
        <li>Memerlukan alat sistem tambahan (ocrmypdf, Ghostscript, unpaper, pngquant – disertakan dalam bundel Apl).</li>
        <li>Pengendalian ralat yang lebih kompleks (deadlock, timeouts).</li>
        </ul>

        <p><strong>Windows (alternatif stabil)</strong></p>
        <p>Alat:</p>
        <ul>
        <li>pytesseract (sambungan terus ke Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Hasil:</p>
        <ul>
        <li>PDF yang boleh dicari yang secara visual sepadan dengan PDF imej, tetapi boleh dicari melalui teks telus.</li>
        </ul>
        <p>Kelebihan:</p>
        <ul>
        <li>Tiada yang terlintas di fikiran sekarang.</li>
        </ul>
        <p>Kekurangan:</p>
        <ul>
        <li>PDF pada dasarnya adalah imej dengan teks tidak kelihatan; susun atur mungkin sedikit menyimpang untuk dokumen kompleks (lajur, jadual).</li>
        <li>Tiada pembetulan condong automatik (--deskew) atau pembersihan imej (--clean).</li>
        <li>Bar kemajuan GUI hanya dikemas kini secara kasar berdasarkan bilangan halaman yang diproses.</li>
        <li>Kelajuan OCR sedikit lebih perlahan (kerana setiap halaman diproses secara berasingan).</li>
        <li>Carian teks dihalakan semula ke tetingkap teks OCR.</li>
        </ul>

        <p><strong>Persamaan</strong></p>
        <ul>
        <li>Kedua-dua kaedah menghasilkan PDF yang boleh dicari dalam direktori yang sama dengan fail sumber.</li>
        <li>Tetapan OCR (bahasa, DPI, mod segmentasi halaman, mod enjin OCR) boleh dikonfigurasikan melalui OCRSettingsDialog dan berfungsi dalam kedua-dua pelaksanaan.</li>
        </ul>

        <p><strong>Cadangan:</strong></p>
        <ul>
        <li>macOS: Binari ocrmypdf memberikan hasil terbaik – Beli Mac dan gunakan versi (PDFDarkView untuk Mac dengan cip Apple Silicon atau Intel). Hasil OCR lebih baik daripada di Windows!</li>
        <li>Windows: Gunakan penyelesaian pytesseract. Ia stabil dan memberikan kualiti yang mencukupi untuk kebanyakan dokumen.</li>
        </ul>

        <p><strong>Nota penting:</strong></p>
        <ul>
        <li>Kedua-dua versi disepadukan sepenuhnya ke dalam antara muka pengguna – pengguna tidak melihat sebarang perbezaan.</li>
        <li>Program secara automatik memutuskan enjin OCR yang akan digunakan berdasarkan sistem pengendalian.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Buat tandatangan (dari imbasan)",
        "signature_create_title": "Pilih tandatangan yang diimbas (PDF/gambar)",
        "image_pdf_filter": "Gambar dan PDF",
        "signature_pdf_empty": "PDF tidak mengandungi halaman.",
        "signature_created_success": "Tandatangan berjaya dibuat: {0}",
        "signature_create_error": "Ralat semasa membuat tandatangan:\n{0}",
        "rembg_missing": "rembg tidak dipasang.\nSila pasang: pip install rembg\nRalat: {0}",
        "signature_name_title": "Nama fail untuk tandatangan",
        "signature_name_message": "Sila masukkan nama fail untuk tandatangan baharu (akan disimpan sebagai PNG dengan latar belakang telus):",
        "signature_name_label": "Nama fail:",
        "signature_name_voice": "Masukkan nama fail untuk tandatangan",
        "signature_processing": "Pemprosesan sedang berjalan...",
        "signature_creation_title": "Tandatangan sedang dibuat",
        "signature_overwrite_warning": "Fail '{0}' sudah wujud. Tulis ganti?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Sediakan PDF untuk tandatangan",
        "signature_prepare_instruction":"Sila pilih PDF yang mengandungi tandatangan yang diimbas pada satu halaman.\n\nPengecaman optimum dicapai jika:\n• Tandatangan ditulis dengan dakwat hitam (pen bola atau pen hujung halus) di atas kertas putih.\n• Tandatangan berada di bahagian atas pertiga halaman A4 yang kosong.\n• PDF diimbas dengan sekurang-kurangnya 300 dpi.\n• Tandatangan jelas dan tidak terlalu nipis.\n• Tiada corak latar belakang atau garis yang mengganggu.",
        "signature_prepare_voice":"Sila pilih PDF dengan tandatangan yang diimbas. Perhatikan kualiti dan kontras yang baik.",
        "sig_thickness_label":"Ketebalan garis:",
        "sig_thickness_normal":"Normal (nipis)",
        "sig_thickness_bold":"Tebal (disyorkan)",
        "sig_thickness_very_bold":"Sangat tebal",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Tambah bahasa GUI dan OCR - Panduan",
        'language_guide_title': "Tambah bahasa GUI dan OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Muat turun fail terjemahan yang diingini <code>translations_xy.py</code> dari<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        dan letakkannya dalam direktori berikut:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Buka pelayar web anda.</li>
        <li>Pergi ke: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Cari di tepi kanan skrin untuk "Releases" dan pilih yang bertanda <strong>"latest"</strong>.</li>
        <li>Pada halaman keluaran berikutnya, muat turun fail <code>Source Code.zip</code> di bahagian paling bawah.</li>
        <li>Nyahzip fail ZIP.</li>
        <li>Cari dalam folder yang dinyahzip semua fail bahasa yang anda perlukan, dan salinnya ke direktori:<br/>
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
        "menu_watermark":"Masukkan tanda air",
        "fullpage_text_watermark_title":"Teks sebagai tanda air",
        "fullpage_image_watermark_title":"Imej sebagai tanda air",
        "filename_with_watermark":"_dengan_tanda_air",
        "watermark_text":"Teks:",
        "watermark_text_placeholder":"Teks tanda air anda...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Saiz font:",
        "watermark_format":"Pemformatan:",
        "watermark_bold":"Tebal",
        "watermark_italic":"Condong",
        "watermark_color":"Warna:",
        "watermark_choose_color":"Pilih warna...",
        "watermark_opacity":"Kelegapan / Ketelusan:",
        "watermark_direction":"Arah bacaan:",
        "watermark_direction_l_r":"Kiri → Kanan",
        "watermark_direction_bl_tr":"Bawah kiri → Atas kanan",
        "watermark_direction_tl_br":"Atas kiri → Bawah",
        "watermark_direction_b_t":"Bawah → Atas",
        "watermark_direction_t_b":"Atas → Bawah",
        "watermark_preview":"Pratonton:",
        "watermark_preview_sample":"Teks contoh",
        "watermark_empty_text":"Sila masukkan teks.",
        "watermark_applied":"Tanda air telah digunakan pada semua halaman.",
        "watermark_saved":"Tanda air disimpan.",
        "image_scale":"Saiz:",
        "image_preview":"Pratonton imej:",
        "no_image_selected":"Tiada imej dipilih",
        "browse":"Layari...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Pemadaman",
        "redact_add_black": "Pemadaman (hitam)",
        "redact_add_white": "Pemadaman (putih / padam)",
        "redact_added_black": "Pemadaman hitam ditambah",
        "redact_added_white": "Pemadaman putih ditambah",
        "redact_apply_all": "Gunakan semua pemadaman dan simpan",
        "redact_discard_all": "Buang semua pemadaman",
        "redact_discard": "Buang pemadaman ini",
        "no_redactions": "Tiada pemadaman",
        "redact_confirm_title": "Gunakan pemadaman secara kekal",
        "redact_confirm_message": "Amaran: Kawasan yang ditanda akan dipadam secara kekal (hitam atau putih).\nSandaran akan dibuat (jika diaktifkan).\n\nTeruskan?",
        "redact_apply": "Ya, padam sekarang",
        "redact_saved": "{0} pemadaman berjaya digunakan dan disimpan.",
        "redact_saved_voice": "{0} pemadaman digunakan",
        "redact_error": "Ralat semasa pemadaman",
        "filename_redacted":"_dipadam",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Masukkan nombor halaman',
        'page_numbers_format': 'Format nombor:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arab)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Roman kecil)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Roman besar)',
        'page_numbers_format_letter': 'A, B, C ... (Huruf)',
        'page_numbers_format_custom': 'Tersuai',
        'page_numbers_custom_pattern': 'Corak:',
        'page_numbers_custom_placeholder': 'cth. "Halaman {nummer}" atau "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Gunakan {nummer} untuk nombor halaman semasa dan {total} untuk jumlah keseluruhan',
        'page_numbers_position': 'Kedudukan:',
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
        'page_numbers_margin_x': 'Jarak mendatar:',
        'page_numbers_margin_y': 'Jarak menegak:',
        'page_numbers_range': 'Julat halaman:',
        'page_numbers_all_pages': 'Semua halaman',
        'page_numbers_custom_range': 'Julat tersuai',
        'page_numbers_from': 'Dari:',
        'page_numbers_to': 'Ke:',
        'page_numbers_progress': 'Memasukkan nombor halaman...',
        'page_numbers_start': 'Memulakan pemasukan nombor halaman...',
        'page_numbers_cancel': 'Pemasukan nombor halaman dibatalkan',
        'page_numbers_success': 'Nombor halaman berjaya ditambah.\n\nAdakah anda mahu membuka PDF baru?\n\n{0}',
        'page_numbers_complete': 'Nombor halaman ditambah',
        'page_numbers_error_format': 'Ralat semasa memasukkan nombor halaman: {0}',
        'page_numbers_content_type': 'Jenis kandungan:',
        'page_numbers_tab_simple': 'Nombor mudah',
        'page_numbers_tab_range': 'Halaman X daripada Y',
        'page_numbers_tab_date': 'Tarikh',
        'page_numbers_tab_custom': 'Teks bebas',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Halaman {aktuell} daripada {gesamt}',
        'page_numbers_range_custom': 'Tersuai',
        'page_numbers_range_placeholder': 'cth. "Halaman {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format tarikh:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Januari 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Tersuai',
        'page_numbers_date_placeholder': 'cth. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Kedudukan:',
        'page_numbers_date_before': 'Tarikh sebelum nombor halaman',
        'page_numbers_date_after': 'Tarikh selepas nombor halaman',
        'page_numbers_date_only': 'Tarikh sahaja (tanpa nombor halaman)',
        'page_numbers_custom_text': 'Teks tersuai:',
        'page_numbers_custom_placeholder_text': 'Gunakan {seite} untuk nombor halaman dan {gesamt} untuk jumlah keseluruhan\ncth. "Rahsia - Halaman {seite}" atau "{seite} daripada {gesamt}"',
        "filename_with_page_number":"_dengan_nombor_halaman",
        "filename_with_page_declaration":"_dengan_pernyataan_halaman",
        "filename_with_pagenumber":"_dengan_nombor_halaman",
        "filename_with_date":"_dengan_tarikh",
        "filename_with_my_page_declaration":"_dengan_pernyataan_halaman_tersuai",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Perubahan tidak disimpan",
        "unsaved_changes_message_darkmode": "Terdapat sisipan yang tidak disimpan.\nAdakah anda mahu menyimpannya sebelum bertukar?",
        "save_and_switch": "Simpan dan tukar",
        "discard_and_switch": "Tukar sekarang",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Eksport halaman sebagai imej',
        'export_images_menu': 'Eksport sebagai imej (PNG/JPEG)',
        'export_images_format': 'Format imej:',
        'export_images_dpi': 'Resolusi (DPI):',
        'export_images_quality': 'Kualiti JPEG:',
        'export_images_range': 'Julat halaman:',
        'export_images_all_pages': 'Semua halaman',
        'export_images_custom_range': 'Julat tersuai',
        'export_images_from': 'Dari:',
        'export_images_to': 'Ke:',
        'export_images_options': 'Pilihan:',
        'export_images_single_files': 'Setiap halaman sebagai fail berasingan',
        'export_images_subfolder': 'Eksport ke subfolder',
        'export_images_subfolder_info': 'Ke subfolder "namaPDF_imej"',
        'export_images_same_folder': 'Dalam folder yang sama dengan PDF',
        'export_images_apply_darkmode': 'Gunakan tetapan PDFDarkView (Mod Gelap)',
        'export_images_target_folder': 'Folder sasaran:',
        'export_images_browse': 'Layari...',
        'export_images_preview': 'Pratonton:',
        'export_images_preview_info': 'Pilih tetapan untuk eksport',
        'export_images_preview_info_detail': '{0} halaman sebagai {1}\nResolusi: {2} DPI\nNama fail: {3}\n{4}',
        'export_images_select_folder': 'Pilih folder sasaran',
        'export_images_start': 'Memulakan eksport imej...',
        'export_images_progress': 'Mengeksport imej...',
        'export_images_saving': 'Menyimpan halaman {0} daripada {1}...',
        'export_images_success': 'Eksport berjaya!\n\n{0} imej disimpan di:\n{1}',
        'export_images_complete': 'Eksport imej selesai',
        'export_images_open_folder': '📁 Buka folder',
        'export_images_cancel': 'Eksport imej dibatalkan',
        'export_images_error_format': 'Ralat semasa mengeksport imej: {0}',
        'export_images_pdf2image_missing': 'Pustaka "pdf2image" tidak dipasang.\n\nSila pasang dengan:\npip install pdf2image\n\nUntuk Windows, anda juga memerlukan Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Penukaran PDF/A untuk pengarkiban jangka panjang',
        'pdfa_menu': 'Penukaran PDF/A (sedia arkib)',
        'pdfa_info': 'Menukar PDF ke format PDF/A.\n\nPDF/A direka khusus untuk pengarkiban jangka panjang dan memastikan dokumen dipaparkan dengan betul pada masa hadapan.',
        'pdfa_standard': 'Standard PDF/A:',
        'pdfa_standard_select': 'Versi:',
        'pdfa_1': 'PDF/A-1 (mudah, serasi luas)',
        'pdfa_2': 'PDF/A-2 (moden, mampatan lebih baik)',
        'pdfa_3': 'PDF/A-3 (versi terkini, membenarkan lampiran)',
        'pdfa_standards_explanation': '📖 Penjelasan standard:\n\n'
            '• PDF/A-1: Asas, serasi dengan sistem lama (sekitar 2005)\n'
            '• PDF/A-2: Lebih moden, mampatan lebih baik, sokongan ketelusan (sekitar 2011)\n'
            '• PDF/A-3: Versi terkini, membenarkan pembenaman lampiran fail (sekitar 2013)\n\n'
            'Cadangan: PDF/A-2 adalah kompromi yang baik antara keserasian dan ciri moden.',
        'pdfa_options': 'Pilihan:',
        'pdfa_compress_enable': 'Mampatkan PDF (fail lebih kecil)',
        'pdfa_metadata_preserve': 'Kekalkan metadata (tajuk, pengarang, dll.)',
        'pdfa_target_folder': 'Folder sasaran:',
        'pdfa_browse': 'Layari...',
        'pdfa_select_folder': 'Pilih folder sasaran',
        'pdfa_ocr_info_unknown': '🔍 Tidak dapat memeriksa kandungan teks.',
        'pdfa_ocr_info_not_needed': '✅ Teks tersedia - OCR tidak diperlukan.\nPDF/A boleh dibuat terus.',
        'pdfa_ocr_info_recommended': '⚠️ Teks yang mencukupi tidak ditemui.\n\nUntuk PDF yang boleh dicari, kami cadangkan menjalankan OCR terlebih dahulu.\nNota: PDF/A berfungsi tanpa OCR - tetapi teks tidak akan boleh dicari.',
        'pdfa_ocr_info_error': '❌ Ralat semasa memeriksa: {0}',
        'pdfa_start': 'Memulakan penukaran PDF/A...',
        'pdfa_progress': 'Penukaran PDF/A sedang berjalan...',
        'pdfa_success': 'Penukaran PDF/A berjaya!\n\nDisimpan sebagai:\n{0}\n\nAdakah anda mahu membuka PDF baru?',
        'pdfa_complete': 'Penukaran PDF/A selesai',
        'pdfa_cancel': 'Penukaran PDF/A dibatalkan',
        'pdfa_error_format': 'Ralat semasa penukaran PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Pustaka "ocrmypdf" tidak dipasang.\n\nSila pasang dengan:\npip install ocrmypdf',
        'btn_convert': 'Tukar',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimumkan PDF (kurangkan saiz fail)',
        'optimize_menu': 'Optimumkan PDF (saiz fail)',
        'optimize_info': 'Mengurangkan saiz fail PDF melalui pelbagai kaedah pengoptimuman.\n\nSemakin tinggi tahap mampatan, semakin kecil fail - dengan kemungkinan kehilangan kualiti dalam imej.',
        'optimize_level': 'Tahap mampatan:',
        'optimize_level_low': 'Rendah (cepat, penjimatan kecil)',
        'optimize_level_medium': 'Sederhana (kompromi baik)',
        'optimize_level_high': 'Tinggi (penjimatan besar)',
        'optimize_level_maximum': 'Maksimum (penjimatan maksimum, perlahan)',
        'optimize_level_explanation': 'Cadangan: "Sederhana" adalah kompromi baik antara kelajuan dan saiz fail.',
        'optimize_options': 'Pilihan:',
        'optimize_compress_images': 'Mampatkan imej (kurangkan kualiti JPEG)',
        'optimize_clean_objects': 'Alih keluar objek tidak digunakan',
        'optimize_preserve_metadata': 'Kekalkan metadata (tajuk, pengarang, dll.)',
        'optimize_image_quality': 'Kualiti imej:',
        'optimize_range': 'Julat halaman:',
        'optimize_all_pages': 'Semua halaman',
        'optimize_custom_range': 'Julat tersuai',
        'optimize_from': 'Dari:',
        'optimize_to': 'Ke:',
        'optimize_target_folder': 'Folder sasaran:',
        'optimize_browse': 'Layari...',
        'optimize_select_folder': 'Pilih folder sasaran',
        'optimize_info_box': 'Maklumat',
        'optimize_info_text': 'Pengoptimuman mungkin mengambil masa beberapa minit untuk PDF besar.\n\nImej disimpan dengan kualiti dikurangkan, yang boleh mengurangkan saiz fail dengan ketara.',
        'optimize_start': 'Memulakan pengoptimuman PDF...',
        'optimize_progress': 'Mengoptimumkan PDF...',
        'optimize_cancel': 'Pengoptimuman PDF dibatalkan',
        'optimize_complete': 'Pengoptimuman PDF selesai',
        'optimize_error_format': 'Ralat semasa pengoptimuman PDF:\n\n{0}',
        'optimize_success_message': 'Pengoptimuman PDF berjaya!\n\nDisimpan sebagai:\n{0}\n\nSebelum: {1}\nSelepas: {2}\nPenjimatan: {3:.1f}%\n\n{4}\n\nAdakah anda mahu membuka PDF yang dioptimumkan?',
        'optimize_success_message_no_size': 'Pengoptimuman PDF berjaya!\n\nDisimpan sebagai:\n{0}\n\nMaklumat saiz tidak tersedia.\n\nAdakah anda mahu membuka PDF yang dioptimumkan?',
        'optimize_result_positive': 'Fail dikurangkan sebanyak {0:.1f}%.',
        'optimize_result_zero': 'Tiada perubahan saiz fail.',
        'optimize_result_negative': 'Fail meningkat sebanyak {0:.1f}%.\nPengoptimuman dilangkau, fail asal dikekalkan.',
        'btn_optimize': 'Mulakan pengoptimuman',
        'filename_optimize_low_suffix': '_dioptimumkan_rendah',
        'filename_optimize_medium_suffix': '_dioptimumkan',
        'filename_optimize_high_suffix': '_dioptimumkan_tinggi',
        'filename_optimize_maximum_suffix': '_dioptimumkan_maks',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Potong PDF',
        'crop_menu': 'Potong PDF (Crop)',
        'crop_range': 'Gunakan pada:',
        'crop_all_pages': 'Semua halaman',
        'crop_current_page': 'Hanya halaman semasa',
        'crop_values': 'Nilai pemotongan (dalam mata):',
        'crop_left': 'Kiri:',
        'crop_right': 'Kanan:',
        'crop_top': 'Atas:',
        'crop_bottom': 'Bawah:',
        'crop_presets': 'Pratetap:',
        'crop_preset_white': 'Kesan margin putih',
        'crop_reset': 'Tetapkan semula',
        'crop_mouse_hint': '🖱️ Seret segi empat tepat untuk memilih kawasan secara kasar.\nKemudian anda boleh melaraskan nilai dengan tepat dalam SpinBox.\nPelarasan manual dengan tetikus tidak mungkin.',
        'crop_apply': 'Potong',
        'crop_scope_all': 'Semua halaman',
        'crop_scope_current': 'Halaman semasa',
        'crop_new_size': 'Saiz baru: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Tiada PDF dimuatkan',
        'crop_preview_error': 'Ralat semasa memuatkan pratonton',
        'crop_start': 'Memulakan pemotongan...',
        'crop_progress': 'Memotong PDF...',
        'crop_success': 'PDF berjaya dipotong!\n\nDisimpan sebagai:\n{0}\n\nAdakah anda mahu membuka PDF yang dipotong?',
        'crop_complete': 'Pemotongan selesai',
        'crop_cancel': 'Pemotongan dibatalkan',
        'crop_error_format': 'Ralat semasa memotong:\n\n{0}',
        'filename_crop_suffix': '_dipotong',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Ratakan PDF (Flatten)',
        'flatten_menu': 'Ratakan PDF (Flatten)',
        'flatten_info': 'Meratakan PDF "membakar" semua elemen yang boleh diedit ke dalam kandungan halaman.\n\nSelepas itu, medan borang, anotasi, teks, silang, tandatangan, imej dan bentuk tidak lagi boleh diedit secara individu.',
        'flatten_explanation_title': '📖 Untuk apa ini berguna?',
        'flatten_explanation_text': 'Perataan diperlukan dalam situasi berikut:\n\n'
            '• 📄 Anda mahu menyediakan dokumen untuk dicetak\n'
            '• 🔒 Anda mahu menghalang seseorang daripada mengubah medan borang\n'
            '• 📎 Anda mahu "menanamkan" anotasi dan komen secara kekal dalam dokumen\n'
            '• 🖼️ Anda mahu menambat teks, silang, tandatangan, imej dan bentuk secara kekal dalam dokumen\n'
            '• 📦 Anda mahu menyediakan fail untuk pengarkiban\n\n'
            'Perataan menjadikan PDF lebih kecil dan menghalang elemen daripada dialih atau dipadam secara tidak sengaja.',
        'flatten_what_title': 'Apa yang diratakan?',
        'flatten_what_list': '• ✅ Medan borang (medan teks, kotak semak, butang)\n'
            '• ✅ Anotasi (komen, sorotan, nota)\n'
            '• ✅ Lapisan atas (teks, silang, tandatangan, imej, bentuk)',
        'flatten_options': 'Pilihan:',
        'flatten_forms': 'Ratakan medan borang',
        'flatten_annotations': 'Ratakan anotasi',
        'flatten_overlays': 'Ratakan lapisan atas (teks, silang, tandatangan, imej, bentuk)',
        'flatten_target_folder': 'Folder sasaran:',
        'flatten_browse': 'Layari...',
        'flatten_select_folder': 'Pilih folder sasaran',
        'flatten_warning': '⚠️ Penting: Perataan adalah proses yang tidak boleh dibatalkan!\n\nSelepas perataan, elemen yang boleh diedit tidak boleh diubah atau dipadam secara individu.\nBuat sandaran terlebih dahulu jika perlu.',
        'flatten_apply': 'Ratakan',
        'flatten_start': 'Memulakan perataan...',
        'flatten_progress': 'Meratakan PDF...',
        'flatten_success': 'PDF berjaya diratakan!\n\nDisimpan sebagai:\n{0}\n\nAdakah anda mahu membuka PDF yang diratakan?',
        'flatten_complete': 'Perataan selesai',
        'flatten_cancel': 'Perataan dibatalkan',
        'flatten_error_format': 'Ralat semasa meratakan:\n\n{0}',
        'filename_flatten_suffix': '_diratakan',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Lapisan atas PDF (Overlay)',
        'overlay_menu': 'Lapisan atas PDF (Overlay)',
        'overlay_info': 'Meletakkan satu PDF (lapisan atas) di atas PDF yang lain.\n\nPDF lapisan atas diletakkan pada PDF asas. Ini berguna untuk tanda air, logo, kepala surat atau setem.',
        'overlay_explanation_title': '📖 Untuk apa ini berguna?',
        'overlay_explanation_text': 'Lapisan atas diperlukan dalam situasi berikut:\n\n'
            '• 🏢 Meletakkan logo syarikat sebagai tanda air pada setiap halaman\n'
            '• 📄 Meletakkan kepala surat pada PDF kosong\n'
            '• 🖊️ Meletakkan lapisan atas setem pada dokumen\n'
            '• 🔖 Meletakkan tanda air pada semua halaman\n'
            '• 📑 Meletakkan lapisan atas borang pada templat',
        'overlay_type': 'Jenis lapisan atas:',
        'overlay_type_fullpage': 'Halaman penuh (menutup)',
        'overlay_type_transparent': 'Halaman penuh (telus - disyorkan)',
        'overlay_type_stamp': 'Setem (boleh diposisikan)',
        'overlay_type_info_fullpage': '📄 PDF lapisan atas diletakkan tepat di atas keseluruhan halaman.\nLatar belakang putih boleh dialih keluar supaya hanya kandungan yang kelihatan.',
        'overlay_type_info_transparent': '🔍 PDF lapisan atas diletakkan di atas keseluruhan halaman dengan latar belakang telus.\nLatar belakang putih dialih keluar secara automatik - sesuai untuk tanda air dan logo!',
        'overlay_type_info_stamp': '🖊️ PDF lapisan atas diposisikan dan diskalakan sebagai setem.\nSempurna untuk logo, setem atau tandatangan pada kedudukan tertentu.',
        'overlay_remove_background': 'Alih keluar latar belakang putih:',
        'overlay_remove_background_enable': 'Alih keluar latar belakang putih daripada PDF lapisan atas (menjadikan lapisan atas telus)',
        'overlay_remove_background_tooltip': 'Mengalih keluar kawasan putih daripada PDF lapisan atas supaya teks di bawah kelihatan.',
        'overlay_threshold': 'Nilai ambang:',
        'overlay_threshold_hint': '(1-254, lebih tinggi = lebih banyak putih dialih keluar)',
        'overlay_select_file': 'Pilih PDF lapisan atas:',
        'overlay_file_placeholder': 'Sila pilih fail PDF untuk lapisan atas',
        'overlay_browse': 'Layari...',
        'overlay_select_overlay': 'Pilih PDF lapisan atas',
        'overlay_range': 'Julat halaman:',
        'overlay_all_pages': 'Semua halaman',
        'overlay_custom_range': 'Julat tersuai',
        'overlay_from': 'Dari:',
        'overlay_to': 'Ke:',
        'overlay_position': 'Kedudukan:',
        'overlay_position_center': 'Tengah',
        'overlay_position_top_left': 'Atas kiri',
        'overlay_position_top_right': 'Atas kanan',
        'overlay_position_bottom_left': 'Bawah kiri',
        'overlay_position_bottom_right': 'Bawah kanan',
        'overlay_size': 'Saiz:',
        'overlay_size_original': 'Saiz asal',
        'overlay_size_fit_page': 'Sesuaikan dengan halaman',
        'overlay_size_custom': 'Tersuai (%)',
        'overlay_opacity': 'Ketelusan:',
        'overlay_target_folder': 'Folder sasaran:',
        'overlay_browse_folder': 'Layari...',
        'overlay_select_folder': 'Pilih folder sasaran',
        'overlay_warning': '⚠️ Nota: PDF lapisan atas diletakkan pada PDF asas dan "dibakar" ke dalamnya.\n\nElemen PDF lapisan atas tidak boleh diedit secara individu selepas disimpan.',
        'overlay_apply': 'Lapisan atas',
        'overlay_start': 'Memulakan lapisan atas...',
        'overlay_progress': 'Melapisi PDF...',
        'overlay_success': 'PDF berjaya dilapisi!\n\nDisimpan sebagai:\n{0}\n\nAdakah anda mahu membuka PDF yang dilapisi?',
        'overlay_complete': 'Lapisan atas selesai',
        'overlay_cancel': 'Lapisan atas dibatalkan',
        'overlay_error_format': 'Ralat semasa melapisi:\n\n{0}',
        'overlay_no_file': 'Tiada PDF lapisan atas dipilih.\n\nSila pilih fail PDF untuk dilapisi.',
        'filename_overlay_suffix': '_dilapisi',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Ekstrak imej daripada PDF',
        'extract_images_menu': 'Ekstrak semua imej',
        'extract_images_info': 'Mengekstrak semua imej daripada PDF dan menyimpannya sebagai fail berasingan.\n\nImej disimpan dalam format asal atau ditukar kepada format yang dipilih.',
        'extract_images_format': 'Format imej:',
        'extract_images_quality': 'Kualiti JPEG:',
        'extract_images_options': 'Pilihan:',
        'extract_images_subfolder': 'Ekstrak ke subfolder ("namaPDF_imej")',
        'extract_images_unique': 'Hanya imej unik (elakkan pendua)',
        'extract_images_range': 'Julat halaman:',
        'extract_images_all_pages': 'Semua halaman',
        'extract_images_custom_range': 'Julat tersuai',
        'extract_images_from': 'Dari:',
        'extract_images_to': 'Ke:',
        'extract_images_target_folder': 'Folder sasaran:',
        'extract_images_browse': 'Layari...',
        'extract_images_select_folder': 'Pilih folder sasaran',
        'extract_images_info_box': 'Maklumat',
        'extract_images_info_text': 'Ekstraksi mungkin mengambil masa beberapa minit untuk PDF besar.\n\nImej disimpan dengan nama asal (halaman_imej).',
        'extract_images_extract': 'Ekstrak',
        'extract_images_start': 'Memulakan ekstraksi...',
        'extract_images_progress': 'Mengekstrak imej...',
        'extract_images_success': '✅ Imej berjaya diekstrak!\n\n{0} imej disimpan di:\n{1}',
        'extract_images_complete': 'Ekstraksi imej selesai',
        'extract_images_cancel': 'Ekstraksi dibatalkan',
        'extract_images_error_format': 'Ralat semasa mengekstrak imej:\n\n{0}',
        'extract_images_open_folder': '📁 Buka folder',
        'extract_images_no_images': 'Tiada imej ditemui dalam PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Pelbagai halaman pada satu halaman (N-Up)',
        'nup_menu': 'Pelbagai halaman pada satu halaman (N-Up)',
        'nup_info': 'Mengatur pelbagai halaman PDF pada satu halaman.\n\nSesuai untuk cetakan padat, gambaran keseluruhan atau bahan edaran.',
        'nup_layout': 'Tataletak:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Pratonton:',
        'nup_preview_info': '{0} halaman → {1} halaman setiap helaian → {2} helaian\nTataletak: {3}',
        'nup_order': 'Susunan:',
        'nup_order_horizontal': 'Mendatar (baris demi baris)',
        'nup_order_vertical': 'Menegak (lajur demi lajur)',
        'nup_order_horizontal_reverse': 'Mendatar songsang',
        'nup_order_vertical_reverse': 'Menegak songsang',
        'nup_range': 'Julat halaman:',
        'nup_all_pages': 'Semua halaman',
        'nup_custom_range': 'Julat tersuai',
        'nup_from': 'Dari:',
        'nup_to': 'Ke:',
        'nup_options': 'Pilihan:',
        'nup_margins': 'Margin:',
        'nup_margin_between': 'Jarak antara halaman:',
        'nup_page_numbers': 'Masukkan nombor halaman',
        'nup_target_folder': 'Folder sasaran:',
        'nup_browse': 'Layari...',
        'nup_select_folder': 'Pilih folder sasaran',
        'nup_create': 'Cipta',
        'nup_start': 'Memulakan N-Up...',
        'nup_progress': 'Mencipta N-Up...',
        'nup_success': 'N-Up berjaya dicipta!\n\nDisimpan sebagai:\n{0}\n\nAdakah anda mahu membuka PDF baru?',
        'nup_complete': 'N-Up selesai',
        'nup_cancel': 'N-Up dibatalkan',
        'nup_error_format': 'Ralat semasa N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Tukar saiz halaman',
        'pagesize_menu': 'Tukar saiz halaman',
        'pagesize_info': 'Menukar saiz halaman PDF.\n\nKandungan secara automatik disesuaikan dengan saiz baru.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Pilih format standard:',
        'pagesize_custom': 'Saiz tersuai:',
        'pagesize_width': 'Lebar:',
        'pagesize_height': 'Tinggi:',
        'pagesize_orientation': 'Orientasi:',
        'pagesize_portrait': 'Potret',
        'pagesize_landscape': 'Landskap',
        'pagesize_scale_options': 'Pilihan skala:',
        'pagesize_fit': 'Sesuaikan (kekalkan nisbah bidang)',
        'pagesize_stretch': 'Regangkan (herot)',
        'pagesize_center': 'Tengah (saiz asal)',
        'pagesize_range': 'Julat halaman:',
        'pagesize_all_pages': 'Semua halaman',
        'pagesize_custom_range': 'Julat tersuai',
        'pagesize_from': 'Dari:',
        'pagesize_to': 'Ke:',
        'pagesize_target_folder': 'Folder sasaran:',
        'pagesize_browse': 'Layari...',
        'pagesize_select_folder': 'Pilih folder sasaran',
        'pagesize_apply': 'Gunakan',
        'pagesize_start': 'Memulakan penukaran saiz halaman...',
        'pagesize_progress': 'Menukar saiz halaman...',
        'pagesize_success': 'Saiz halaman berjaya ditukar!\n\nDisimpan sebagai:\n{0}\n\nAdakah anda mahu membuka PDF baru?',
        'pagesize_complete': 'Penukaran saiz halaman selesai',
        'pagesize_cancel': 'Penukaran saiz halaman dibatalkan',
        'pagesize_error_format': 'Ralat semasa menukar saiz halaman:\n\n{0}',
        'pagesize_preview_info': 'Saiz baru: {0} x {1} pt',
        'filename_pagesize_suffix': '_saiz_baru',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Maklumat PDF',
        'pdf_info_menu': 'Tunjukkan maklumat PDF',
        'pdf_info_voice': 'Memaparkan maklumat PDF',
        'pdf_info_error': 'Ralat semasa memaparkan maklumat PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Tunjukkan pintasan papan kekunci",
        "shortcuts_dialog_title": "Pintasan Papan Kekunci",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FAIL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Buka PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Tutup PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Simpan sebagai...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Lindungi dokumen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Cetak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Cetak segera (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Tutup aplikasi</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Eksport sebagai Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Eksport sebagai DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Eksport sebagai TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Eksport sebagai imej (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Ekstrak imej</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PEMPROSESAN DOKUMEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Pelbagai halaman)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Penukaran PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Ratakan PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Lapisan atas PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimumkan PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDIT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Cari</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Tambah penanda buku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Urus penanda buku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Penanda buku seterusnya</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Penanda buku sebelumnya</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Jalankan OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 PENGURUSAN HALAMAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Putar halaman semasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Putar semua halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalisasi halaman semasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalisasi semua halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Padam halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ekstrak halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Masukkan halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Alih halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Cantumkan PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Tukar saiz halaman</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 MASUKKAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Masukkan teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Masukkan silang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Masukkan tandatangan 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Masukkan tandatangan 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Masukkan imej</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Masukkan segi empat tepat</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Masukkan elips</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Masukkan garis</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Masukkan anak panah</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Masukkan nombor halaman</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Tanda air teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Tanda air imej</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ PEMADAMAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Pemadaman (hitam)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Pemadaman (putih)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Gunakan semua pemadaman</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ LANJUTAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Potong PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Edit metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ PAPARAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Togol Mod Gelap/Terang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Tunjukkan tetingkap teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Lebar halaman (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dua halaman (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Gambaran keseluruhan (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ TETAPAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Pengurusan kata laluan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Tetapan OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Tetapan tandatangan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Pemformatan nama fail</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Eksport tetapan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Import tetapan</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ MAKLUMAT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Tunjukkan maklumat PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Togol output suara</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokus pada bar menu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Versi baharu tersedia",
        "update_available_message": "Terdapat versi baharu <b>{0}</b>.\n\nLawati halaman keluaran untuk memuat turun kemas kini:\n{1}",
        "update_available_voice": "Versi baharu {0} tersedia. Sila muat turun kemas kini dari halaman GitHub.",
        "update_open_release": "Buka halaman keluaran",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Muat turun semua terjemahan",
        "ask_download_all_translations": """Selain daripada bahasa Jerman, Inggeris dan Vietnam, terdapat {total_languages} bahasa GUI lain.\n\nPerlukah disediakan / dikemas kini?\n\nNota:\nBahasa yang tidak diperlukan boleh dipadam secara manual kemudian dalam direktori:\n{translations_path}
        \nJika anda membatalkan, anda boleh memuat turun bahasa GUI kemudian melalui menu 'Alatan → Kemas kini terjemahan'.""",
        "menu_update_translations": "Kemas kini terjemahan",
        "translations_updated": "Terjemahan dikemas kini",
        "translations_update_success": "{} terjemahan berjaya dikemas kini ({} baharu, {} dikemas kini).",
        "translations_update_error": "Ralat semasa mengemas kini terjemahan",
        "translations_update_no_changes": "Semua terjemahan sudah terkini.",
        "translations_update_offline": "Tiada sambungan internet. Terjemahan tidak dapat dikemas kini.",
        "translations_update_in_progress": "Terjemahan sedang dikemas kini di latar belakang...",
        "translations_downloading": "Memuat turun terjemahan...",
        "translations_path_hint": "Direktori pengguna untuk terjemahan",
        "translations_update_not_available_title": "Kemas kini tidak tersedia",
        "translations_update_not_available_message": """Mengemas kini terjemahan hanya tersedia dalam versi yang dipasang.\n\nDalam mod pembangunan, terjemahan sudah terkini.""",
        "translations_update_no_internet_title": "Tiada sambungan internet",
        "translations_update_no_internet_message": """Tidak dapat mewujudkan sambungan internet.\n\nTerjemahan tidak dapat dimuat turun dari GitHub.\n\nPenyelesaian yang mungkin:
        • Periksa sambungan internet anda
        • Nyahaktifkan sebarang tembok api buat sementara waktu
        • Cuba lagi kemudian
        \nAnda juga boleh memuat turun terjemahan secara manual dari GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Kemas kini sedang dijalankan",
        "btn_retry": "Cuba lagi",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Selamat datang ke PDF Dark View",
        "welcome_title_not_supported": "Selamat datang ke PDF Dark View",
        "welcome_message": "Selamat datang ke PDF Dark View!\n\nBahasa sistem anda dikesan sebagai '{language}'.\nAdakah anda ingin menggunakan bahasa ini untuk antara muka pengguna?\n\nAnda boleh menukar bahasa pada bila-bila masa melalui 'Tetapan → Bahasa'.",
        "welcome_message_language_not_available": "Selamat datang ke PDF Dark View!\n\nBahasa sistem anda dikesan sebagai '{language}'.\nBahasa ini belum dipasang.\n\nAdakah anda ingin memuat turun terjemahan untuk {language} sekarang dari GitHub?\n\n(Bahasa kemudian akan digunakan secara automatik untuk antara muka pengguna.)",
        "welcome_message_language_not_supported": "Selamat datang ke PDF Dark View!\n\nBahasa sistem anda dikesan sebagai '{language}'.\nMalangnya, belum ada terjemahan untuk bahasa ini.\n\nAntara muka pengguna akan dipaparkan dalam {fallback_language}.\n\nAnda boleh menukar bahasa pada bila-bila masa melalui 'Tetapan → Bahasa'.\nJika anda mahu, anda juga boleh menyumbang terjemahan untuk bahasa anda:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Ya, gunakan bahasa sistem",
        "welcome_keep_english": "Tidak, kekalkan bahasa Inggeris",
        "welcome_download_language": "Ya, muat turun {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program sedang ditutup",

    }
