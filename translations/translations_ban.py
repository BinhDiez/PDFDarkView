
# ============================================
# translations_ban.py - Kamus Basa Bali
# Kapupulang antuk kategori (kaaturang sakadi asli)
# ============================================

def load_balinese_strings():
    """Ngamuat makejang kruna ring basa Bali"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF jemak",
        'btn_text_window': "Teks OCR",
        'btn_first': "Kaca ka-1",
        'btn_prev': "Kaca mabalik",
        'btn_next': "Kaca maju",
        'btn_last': "Kaca pungkasan",
        'btn_print': "Cetak",
        'btn_darkmode_light': "Mode Terang",
        'btn_darkmode_dark': "Mode Peteng",
        'btn_delete_pages': "Hapus kaca",
        'btn_extract_pages': "Alusin kaca",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Urung",
        'btn_save': "Simpen",
        'btn_close': "Tutup",
        'btn_delete': "Hapus",
        'btn_delete_all': "Hapus makejang",
        'btn_copy': "Salin",
        'btn_export': "Ekspor",
        'btn_show': "Témbongang kruna sandi",
        'btn_hide': "Pendem kruna sandi",
        'btn_authenticate': "Oténtikasi",
        'btn_settings': "Pangaturan",
        'btn_protect': "Amanang",
        'btn_remove_password': "Buang kruna sandi",
        'btn_manage': "Pangaturan kruna sandi",
        'btn_retry': "Coba malih",
        'btn_select_all': "Pilih makejang",
        'btn_clear_selection': "Usud pilihan",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Kaca {0} saking {1}",
        'page_count': "saking {0}",
        'goto_page': "Ka kaca",
        'page_simple': "Kaca {0}",
        'full_view_page': "Témbongang kaca {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Kruna sané rauhin + Enter",
        'search_results': "Kapanggih: {0} saking {1}",
        'search_nav_hint': "Enter: salanturnyan  (Shift+Enter: sadurungnyan) suratan",
        'search_no_results': "Tan wénten suratan",
        'search_error': "Pikobet nyarengin",
        'search_active': "Aktip nyarengin",
        'search_closed': "Nyarengin puput",
        'search_position': "Kaca {0} {1}",
        'search_pos_top': "paling duur",
        'search_pos_upper': "duur",
        'search_pos_middle': "tengah",
        'search_pos_lower': "beten",
        'search_pos_bottom': "paling beten",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Pangaksara OCR sampun prasida!",
        'ocr_success_title': "OCR prasida",
        'ocr_success_message': "Dokumén puniki sampun prasida kapanéhan.",
        'ocr_failed': "OCR gagal",
        'ocr_in_progress': "OCR dados kaanggen",
        'ocr_preparing': "PDF kakancanin...",
        'ocr_analyzing': "PDF ka-analisis...",
        'ocr_optimizing': "Ngoncengang gambar...",
        'ocr_recognizing': "Pangaksara kaanggen...",
        'ocr_embedding': "Teks kamargiang...",
        'ocr_finalizing': "Nyelesaiang PDF...",
        'ocr_not_available': "OCR tan kasedia",
        'ocr_install_message': "Piranti OCR nenten katemu.\n\nYening nyenengang panginstalan:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR kaperluang",
        'ocr_question': "PDF puniki nenten madaging teks sané prasida kapanéhan.\nKéngkén jagi nganggen OCR, mangda {0} prasida?",
        'ocr_perform': "Gelarang OCR",
        'ocr_later': "Nyen",
        'ocr_starting': "Ngawitin OCR sané kapastiayang...",
        'ocr_success_voice': "OCR prasida. PDF mangkin prasida kapanéhan.",
        'ocr_partial_success': "OCR sampun kagelarang, nanging wénten pikobet rikala ngantosang.\n\nVersi sané prasida kapanéhan sampun kasimpen ring:\n{0}\n\nPikobet: {1}",
        'ocr_partial_title': "OCR sawatara prasida",
        'ocr_partial_voice': "OCR sampun kagelarang, nanging ngantosang gagal.",
        'original_file': "Berkas asli:",
        'old_size': "Ukuran lami:    {0} bytes",
        'new_size': "Ukuran anyar: {0} bytes",
        'size_change': "Liwihan: {0}{1} bytes",
        'backup_created_file': "Backup kakardi:\n{0}",
        'backup_not_created': "Backup: Nenten kakardi (pangaturan kapatén)",
        'page_header': "=== Kaca {0} ===\n{1}\n",
        'scanned_page_header': "=== Kaca {0} (kaséken) ===\n[Kaca puniki madaging teks scan]\n[Mangda OCR gelarang antuk jujur]\n",
        'scanned_warning': "⚠️ TEKS SCAN - OCR KAPERLUANG",
        'guaranteed_title': "PDF sané prasida kapanéhan kakardi",
        'guaranteed_message': "<b>Versi PDF sané kapastiayang prasida kapanéhan sampun kakardi!</b>\n\nSantukan OCR otomatis gagal, sampun kakardi\nversi PDF sané prasida kapanéhan:\n\n{0}\n\n<b>Berkas puniki madaging:</b>\n• Teks sané kaambil (yénten wénten)\n• Paweweh antuk kaca sané kaséken\n• Sampun prasida kapanéhan",
        'guaranteed_voice': "PDF sané kapastiayang prasida kapanéhan sampun kakardi.",
        'instruction_title': "PANGANDIKA ANTUK OCR",
        'instruction_file': "Berkas asli: {0}",
        'instruction_text': "Pangaksara otomatis (OCR) gagal.\nGelarang OCR antuk jujur:\n\n1. ANGGEN OCRmyPDF (garis paréntah):\n   ocrmypdf --force-ocr \"[BERKAS]\" \"hasil.pdf\"\n\n2. ANGGEN ADOBE ACROBAT (macOS/Windows):\n   • Buka PDF ring Acrobat\n   • Piranti > Uah PDF\n   • Pilih 'Pangaksara Teks'\n\n3. ANGGEN PREVIEW (macOS):\n   • Buka PDF ring Preview\n   • Berkas > Ekspor...\n   • Quartz-Filter: 'Reduce File Size'\n   • Aktipang 'Gelarang OCR'\n\n4. LAYANAN OCR DARING:\n   • smallpdf.com/id/ocr-pdf\n   • ilovepdf.com/id/ocr-pdf\n   • adobe.com/id/acrobat/online/pdf-to-word.html",
        'instruction_created': "Pangandika OCR kakardi",
        'instruction_created_message': "Pangandika rincikan sampun kakardi:\n\n{0}\n\nTurutin undagan antuk OCR manual.",
        'instruction_created_voice': "Pangandika OCR sampun kakardi.",
        'ocr_impossible': "OCR tan prasida",
        'ocr_impossible_message': "OCR tan prasida kagelarang.\n\nNganggén pangolah manual antuk '{0}' anggén piranti OCR.",
        'ocr_impossible_voice': "OCR tan prasida. Mangda ngolah antuk manual.",
        'emergency_title': "OCR Darurat",
        'emergency_message': "PDF darurat sampun kakardi:\n\n{0}\n\nOlahan berkas puniki antuk manual nganggén OCR.",
        'emergency_voice': "PDF darurat sampun kakardi. Mangda ngelarang OCR manual.",
        'critical_error': "Pikobet Kritikal",
        'critical_error_message': "OCR tan prasida kawitin.\n\nMangda ngawitin malih programé tur\npariksa panginstalan OCR.",
        'critical_error_voice': "Pikobet Kritikal OCR",
        'ocr_question_html': "<p>PDF puniki nenten madaging teks sané prasida kapanéhan.<p>Kéngkén jagi nganggen OCR, mangda <b>{0}</b> prasida?</p>",
        'ocr_question_voice': "OCR kaperluang. PDF puniki nenten madaging teks sané prasida kapanéhan. Kéngkén jagi nganggen OCR, mangda {0} prasida?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "tan wénten PDF kajemak",
        'no_pdf_message': "Tan wénten PDF kajemak",
        'pdf_not_found': "PDF nenten katemu",
        'file_size': "Ukuran berkas",
        'bytes': "Bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup kakardi",
        'backup_disabled': "Backup kapatén",
        'backup_activated': "Backup kakardi",
        'backup_deactivated': "Backup kapatén",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ aktip",
        'backup_off': "✘ tan aktip",
        'close_pdf': "Nutup PDF: {0}",
        'pdf_not_found_format': "PDF nenten katemu: {0}",
        'error_pdf_load_format': "Pikobet rikala ngamuat PDF: {0}",
        'load_failed_format': "Ngamuat gagal:\n{0}",
        'decrypted_suffix': "(kabuka)",
        'decryption_failed': "Mabuka gagal.",
        'decryption_error': "Pikobet rikala mabuka",
        'decryption_success': "Prasida kabuka",
        'decryption_success_message': "PDF sampun kabuka tur kasimpen ring:\n\n{0}",
        'decryption_success_voice': "PDF sampun kabuka tur kasimpen.",
        'password_remove_error': "Pikobet rikala ngicalang kruna sandi",
        'save_unencrypted': "Simpen PDF tan kaciptayang ring",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Simpen dados...",
        'save_copy': "Simpen salinan",
        'save_success': "PDF kasimpen ring: {0}",
        'save_encrypted': "PDF sané kaamannang kasimpen ring: {0}",
        'save_error': "PDF tan prasida kasimpen",
        'encryption_question': "Kéngkén jagi ngamannang PDF nganggén kruna sandi?",
        'encryption_yes': "Inggih",
        'encryption_no': "Nenten",
        'encryption_cancel': "Urung",
        'save_cancel': "Nyimpen kaurungang",
        'save_encrypted_voice': "Berkas kaciptayang tur kasimpen.",
        'save_success_voice': "Berkas PDF sampun kasimpen tanpa ciptaan.",
        'save_error_format': "PDF tan prasida kasimpen:\n{0}",
        'export_pages_success': "Ekspor Pages prasida",
        'export_pages_error': "Ekspor Pages gagal",
        'export_pages_error_format': "Ekspor Pages gagal: {0}",
        'export_word_success': "Ekspor Word prasida",
        'export_word_error': "Ekspor Word gagal",
        'export_word_error_format': "Ekspor Word gagal: {0}",
        'export_text_success': "Ekspor Teks prasida",
        'export_text_error': "Ekspor Teks gagal",
        'export_text_error_format': "Ekspor Teks gagal: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Kruna sandi kaperluang",
        'password_enter': "Nunas, ngajiang kruna sandi",
        'password_confirm': "Konfirmasi kruna sandi",
        'password_new': "Kruna sandi anyar",
        'password_current': "Kruna sandi mangkin",
        'password_save': "Simpen kruna sandi (kaamannang)",
        'password_saved': "✓ Kruna sandi antuk berkas puniki sampun kasimpen",
        'password_wrong': "Kruna sandi iwang",
        'password_mismatch': "Kruna sandi nenten patuh",
        'password_too_short': "Kruna sandi terlalu cutet",
        'password_min_length': "Kruna sandi mangda 4 karakter",
        'password_strength': "Kekuatan kruna sandi",
        'password_strength_very_weak': "Lemah pisan",
        'password_strength_weak': "Lemah",
        'password_strength_medium': "Madya",
        'password_strength_strong': "Kuat",
        'password_strength_very_strong': "Kuat pisan",
        'password_char_count': "({0} karakter)",
        'password_match': "✓ Patuh",
        'password_no_match': "✗ Kruna sandi nenten patuh",
        'password_show': "Témbongang",
        'password_hide': "Pendem",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Pangaturan kruna sandi",
        'password_table_filename': "Aran berkas",
        'password_table_password': "Kruna sandi",
        'password_count': "{0} kruna sandi kasimpen",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Tan wénten kruna sandi kasimpen",
        'password_copied': "{0} kruna sandi ksalinn",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Nunas, yening jagi ngicalang kruna sandi antuk '{0}'?",
        'password_delete_multiple': "Nunas, yening jagi ngicalang {0} kruna sandi sané kapilih?",
        'password_delete_all_confirm': "Nunas, yening jagi ngicalang makejang {0} kruna sandi sané kasimpen?",
        'password_deleted': "{0} kruna sandi kicalang",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Makejang kruna sandi sampun kicalang",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Kardi kruna sandi",
        'generator_generated': "Kruna sandi sané kakardi:",
        'generator_regenerate': "Kardi malih",
        'generator_copy': "Salin",
        'generator_use': "Anggen",
        'generator_settings': "Pangaturan",
        'generator_length': "Lantang:",
        'generator_group_every': "Pamatiyas, metén",
        'generator_group_chars': "karakter.    Pamatiyas:",
        'generator_uppercase': "Huruf ageng (A-Z)",
        'generator_lowercase': "Huruf alit (a-z)",
        'generator_digits': "Angka (0-9)",
        'generator_symbols': "Tanda baca (!@#$%^&*)",
        'generator_exclude': "Tan kaanggen:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Kruna sandi utama kaperluang",
        'master_password_setup': "Ngadegang kruna sandi utama",
        'master_password_change': "Ngubah kruna sandi utama",
        'master_password_enter': "Nunas, ngajiang kruna sandi utama",
        'master_password_choose': "Pilih kruna sandi utama sané aman (min. 8 karakter)",
        'master_password_new': "Nunas, ngajiang kruna sandi utama anyar",
        'master_password_confirm': "Konfirmasi kruna sandi",
        'master_password_authenticate': "Oténtikasi",
        'master_password_success': "Kruna sandi utama sampun kadegang.",
        'master_password_changed': "Kruna sandi utama sampun kauah.",
        'master_password_removed': "Kruna sandi utama lan makejang kruna sandi sampun kicalang.",
        'master_password_remove': "Buang kruna sandi utama",
        'master_password_remove_confirm': "Nunas, yening PASTI jagi ngicalang MAKEJANG kruna sandi?\n\nPangicalan puniki SAWATARA NENTEN PRASIDA KABALIKANG!",
        'master_password_export_before': "Nunas, jagi nyalin cadangan sadurungnyan?",
        'master_password_export_delete': "Salin cadangan & sung",
        'master_password_delete_now': "Sung mangkin",
        'master_password_for_signatures': "Santukan jagi nganggén tanda tangan, patut ngadegang kruna sandi utama.\n\nKéngkén jagi ngadegang kruna sandi utama mangkin?",
        'master_password_for_private': "Santukan jagi nganggén teks pribadi, patut ngadegang kruna sandi utama.\n\nKéngkén jagi ngadegang kruna sandi utama mangkin?",
        'master_password_info': """
            <b>🔐 YEN TAN WÉNÉN KRUNA SANDI UTAMA:</b><br>
            • Tan prasida némbongang, nyalin, lan ngekspor kruna sandi<br>
            • Ngicalang kruna sandi salanturnyané prasida (taler tanpa kruna sandi utama)<br><br>

            <b>🔐 YEN MADAGING KRUNA SANDI UTAMA:</b><br>
            • Makejang fungsi kasedia sesampun oténtikasi<br>
            • Kruna sandi kaciptayang nganggén kruna sandi utama<br>
            • Lantang minimal: 8 karakter<br>
            • Panyimpenan aman SHA-256 Hash<br><br>

            <b>PENTING:</b><br>
            • Yening lali kruna sandi utama: kruna sandi nenten prasida kabalikang<br>
            • Rikala ngicalang kruna sandi utama: MAKEJANG kruna sandi pacang ical<br>
            • Opsi ekspor kasedia sadurung ngicalang<br>
            • Kruna sandi utama prasida kauah sambilanga
        """,
        'signature_auth_disabled': "Patakon kruna sandi antuk tanda tangan kapatén",
        'template_auth_disabled': "Patakon kruna sandi antuk teks pribadi kapatén",
        'master_password_for_signatures_settings': "Santukan jagi nganggén tanda tangan, patut ngadegang kruna sandi utama.\n\nNiki prasida kaatur ring Pangaturan - Tata Kruna Sandi",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Amanang PDF",
        'protect_info': "Berkas '{0}' pacang kaamannang nganggén kruna sandi.",
        'protect_instruction': "Nunas, ngajiang kaping kalih kruna sandi sané jagi kaanggen, utawi nganggén panggawé kruna sandi ring tengen.",
        'protect_success': "PDF sampun prasida kaamannang tur kasimpen ring:\n{0}\n\nKruna sandi: {1}\n\nKéngkén jagi ngajak PDF sané kaamannang mangkin?",
        'protect_open': "Inggih",
        'protect_skip': "Nenten",
        'protect_error': "Pikobet rikala ngamannang PDF",
        'protect_open_title': "buka PDF sané kaamannang",
        'protect_question': "Puput. Kéngkén jagi ngajak PDF sané kaamannang mangkin? Inggih utawi Nenten?",
        'password_cancel': "Pasauran kruna sandi kaurungang",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Hapus kaca",
        'pages_extract': "Alusin kaca",
        'pages_insert': "Sisipang kaca",
        'pages_move': "Genahang kaca",
        'pages_delete_options': "Pilihan ngapus",
        'pages_delete_empty': "Hapus kaca kosong",
        'pages_delete_current': "Hapus kaca mangkin",
        'pages_delete_range': "Hapus kaca akeh",
        'pages_extract_options': "Pilihan ngaluwang",
        'pages_extract_current': "Alusin kaca mangkin",
        'pages_extract_range': "Alusin kaca akeh",
        'pages_insert_position': "Genah sisipan",
        'pages_insert_before': "Sisipang sadurung kaca:",
        'pages_insert_select': "Pilih PDF",
        'pages_insert_none': "Tan wénten PDF kapilih",
        'pages_move_source': "Kaca sané jagi gingsirang",
        'pages_move_from': "Saking kaca:",
        'pages_move_to': "Ngantos kaca:",
        'pages_move_target': "Genah tujuwan",
        'pages_move_before': "Gingsirang sadurung kaca:",
        'pages_move_hint': "Pangeling: kaca 1 = pangawit, {0} = pungkasan",
        'pages_range_invalid': "Kaca pangawit patut alit utawi pateh sareng kaca pungkasan.",
        'pages_position_invalid': "Genah tujuwan nenten dados magenah ring wewidangan kaca sané jagi gingsirang.",
        'pages_no_pdf_selected': "Tan wénten PDF kapilih.",
        'pages_deleted': "Wénten {0} kaca kicalang.",
        'pages_extracted': "Kaaluwang: {0}\nKasimpen ring: {1}\nUkuran: {2:.1f} KB",
        'pages_inserted': "{0} kaca kasisipang",
        'pages_moved': "Wénten {0} kaca kagingsirang.",
        'pages_deleted_none': "Tan wénten kaca kicalang.",
        'pages_delete_progress': "Ngapus kaca...",
        'pages_deleted_with_backup': "Wénten {0} kaca kicalang.\n\nBackup: {1}",
        'pages_deleted_voice': "Sampun kakardi backup tur {0} kaca kicalang.",
        'info': "Pangeling",
        'error_dialog_creation': "Dialog tan prasida kakardi",
        'extract_page_single': "Alusin kaca {0}",
        'extract_page_range': "Alusin kaca {0}-{1}",
        'extract_success_voice': "Kaca prasida kaaluwang",
        'extract_error_format': "Pikobet rikala ngaluwang: {0}",
        'pages_inserted_voice': "Wénten {0} kaca kasisipang.",
        'insert_error_format': "Pikobet rikala nyisipang: {0}",
        'pages_move_progress': "Ngingsirang kaca...",
        'pages_moved_with_backup': "Wénten {0} kaca kagingsirang.\n\nBackup: {1}",
        'move_success_title': "Prasida kagingsirang",
        'pages_moved_voice': "{0} kaca prasida kagingsirang",
        'mark_removed': "Tanda ring kaca {0} kicalang",
        'mark_empty': "Kaca {0} katandain kosong",
        'mark_export_removed': "Tanda ekspor ring kaca {0} kicalang",
        'mark_export': "Kaca {0} katandain antuk ekspor",
        'no_empty_pages': "Tan wénten kaca kosong katandain",
        'delete_empty_confirm': "Kéngkén jagi ngapus makejang {0} kaca kosong sané katandain?",
        'delete_empty_confirm_voice': "Jagi ngapus mangkin makejang {0} kaca kosong sané katandain? Inggih utawi Nenten.",
        'empty_pages_deleted': "{0} kaca kosong kicalang",
        'no_export_pages': "Tan wénten kaca katandain antuk ekspor",
        'overwrite_title': "Gingsirang berkas sané sampun wénten",
        'overwrite_question': "Berkas\n\n{0}\n\nsampun wénten.\nKéngkén jagi ngingsirang?",
        'overwrite_voice': "Jagi ngingsirang berkas sané sampun wénten? Inggih utawi Nenten.",
        'page_skipped': "Kaca {0} kawonang",
        'export_complete': "Ekspor puput.",
        'export_complete_voice': "Ekspor sampun puput.",
        'no_pages_exported': "Tan wénten kaca kaekspor",
        'export_cancelled': "Ekspor kaurungang",
        'pages_exported': "{0} kaca kaekspor nuju {1}",
        'export_page_title': "Ekspor kaca",
        'page_exported': "Kaca {0} kaekspor nuju {1}",
        'export_error': "Pikobet rikala ngekspor",
        'export_marked_title': "Ekspor kaca katandain",
        'rotate_all_title': "Puter makejang kaca",
        'rotate_all_question': "Kéngkén jagi muter makejang kaca 90 derajat ka tengen?",
        'rotate_all_voice': "Jagi muter makejang kaca 90 derajat ka tengen? Inggih utawi Nenten?",
        'all_pages_rotated': "Makejang kaca kaputer",
        'page_rotated': "Kaca {0} kaputer",
        'rotate_error': "Kaca tan prasida kaputer",
        'delete_page_confirm': "Kéngkén jagi ngapus kaca {0}?",
        'delete_page_confirm_voice': "Nunas, yening jagi ngapus kaca {0}? Inggih utawi Nenten.",
        'page_deleted': "Kaca {0} kicalang",
        'delete_error': "Kaca tan prasida kicalang",
        'pages_deleted_voice': "{0} kaca kicalang",
        'pages_exported_split': "{0} kaca sampun prasida kaekspor.",
        'pages_skipped': "{0} kaca kawonang.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Alusin kaca (lengkap)",
        'pdf_splitter_title': "Pamisah & Panyalus PDF",
        'pdf_splitter_load': " Pilih berkas PDF",
        'pdf_splitter_info': "Pilih opsi antuk dokumén PDF",
        'pdf_splitter_basic': "Operasi dasar",
        'pdf_splitter_single': "Bagi dados kaca-kaca",
        'pdf_splitter_range': "Alusin kaca:",
        'pdf_splitter_range_placeholder': "c. 1-3,5,7-9",
        'pdf_splitter_clean': "Operasi ngeresikin",
        'pdf_splitter_remove_empty': "Buang makejang kaca kosong",
        'pdf_splitter_remove': "Hapus wewidangan kaca:",
        'pdf_splitter_remove_placeholder': "c. 2,4-6",
        'pdf_splitter_process': "Olahan PDF",
        'pdf_splitter_loaded': "PDF kajemak. Pilih opsi",
        'pdf_read_error': "PDF tan prasida kawaca",
        'pages': "kaca",
        'pages_created': "Kaca kakardi",
        'range_empty': "Nunas, ngajiang wewidangan kaca",
        'range_invalid': "Wewidangan kaca tan sah",
        'range_created': "PDF anyar antuk kaca kapilih sampun kakardi:\n{0}",
        'empty_removed': "{0} kaca kosong kicalang.\nHasil: {1}",
        'remove_empty': "Nunas, ngajiang kaca sané jagi kicalang",
        'remove_invalid': "Kaca sané jagi kicalang tan sah",
        'remove_done': "PDF sané karesikin sampun kakardi:\n{0}",
        'open_folder': "Buka folder",
        'show_in_finder': "Témbongang ring Finder",
        'pdf_splitter_no_pdf': "Nunas, jemak PDF dumun.",
        'process_error': "Pikobet rikala ngolah PDF",
        'pages_created_voice': "{0} kaca sampun kakardi",
        'range_created_voice': "PDF antuk kaca kapilih sampun kakardi",
        'empty_removed_voice': "{0} kaca kosong sampun kicalang",
        'remove_done_voice': "PDF sané karesikin sampun kakardi",
        'pdf_splitter_split_groups': "Tiap kelompok pateh ring berkas kapisah",
        'range_created_single': "PDF anyar kakardi:\n{0}",
        'range_created_multiple': "{0} berkas PDF sampun kakardi.",
        'range_created_voice_single': "PDF antuk kaca kapilih sampun kakardi",
        'range_created_voice_multiple': "{0} berkas PDF sampun kakardi",
        'empty_removed_none_left': "Tan wénten kaca nyisain",
        'empty_removed_all_empty': "Makejang kaca katetepang kosong tur pacang kicalang. Nenten wénten berkas kakardi.",
        'preview_single': "Pratinjau: {0}",
        'preview_enter_range': "Nunas, ngajiang wewidangan kaca.",
        'preview_invalid_range': "Wewidangan kaca tan sah.",
        'preview_file': "Pratinjau: {0}",
        'preview_files': "Pratinjau: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Ngawitin nyetak",
        'print_sent': "Parintah nyetak kakirim",
        'print_now': "Cetak langsung",
        'print_error': "Pikobet nyetak langsung",
        'print_limited': "Fungsi nyetak ring sistem puniki kawatesin",
        'print_error_format': "Pikobet nyetak langsung: {0}",
        'warning': "Pangeling",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Alih ka Mode Terang",
        'mode_switch_to_dark': "Alih ka Mode Peteng",
        'mode_dark_activated': "Mode Peteng aktip",
        'mode_light_activated': "Mode Terang aktip",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Témbongang kaca",
        'zoom_two_pages': "Kalih kaca sisian",
        'zoom_overview': "Mode Ringkesan",
        'zoom_cannot_during_search': "Zoom nenten prasida rikala nyarengin",
        'zoom_exit_first': "Nunas, puputang zoom dumun",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop aktip",
        'drag_disabled': "Drag & Drop tan aktip",
        'drag_page_grab': "Cekel kaca {0}",
        'drag_page_dropped': "Kaca {0} kasisipang ring genah {1}",
        'drag_position_invalid': "Genah tan sah",
        'drag_same_position': "Kaca {0} kantun ring genah {0}",
        'drag_error': "Pikobet rikala ngingsirang",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Ngajiang teks antuk format lengkap tur tata teks",
        'text_templates': "Teks sané kasedia:",
        'text_name': "Aran",
        'text_preview': "Pratinjau teks",
        'text_enter': "Teks:",
        'text_font_size': "Ukuran aksara:",
        'text_formatting': "Format:",
        'text_bold': "Tebal",
        'text_italic': "Miring",
        'text_underline': "Garisi beten",
        'text_alignment': "Genah:",
        'text_left': "Kiwa",
        'text_center': "Tengah",
        'text_right': "Tengen",
        'text_color': "Warna teks:",
        'text_opacity': "Bening:",
        'text_word_wrap': "Putus garis:",
        'text_auto': "Otomatis",
        'text_page_width_95': "Linggah kaca (95%)",
        'text_page_width_85': "Linggah pisan (85%)",
        'text_page_width_75': "Linggah (75%)",
        'text_page_width_60': "Linggah (60%)",
        'text_page_width_50': "Madya (50%)",
        'text_page_width_30': "Ciyut (30%)",
        'text_page_width_20': "ciyut (20%)",
        'text_page_width_10': "Ciyut pisan (10%)",
        'text_no_wrap': "Tan putus",
        'text_private': "Teks pribadi (perlu oténtikasi)",
        'text_preview_label': "Pratinjau:",
        'text_preview_placeholder': "Pratinjau teks pacang kaciré ring dini...",
        'text_no_text': "(Tan wénten teks)",
        'text_save_template': "💾 Simpen dados teks",
        'text_delete_template': "🗑 Hapus teks kapilih",
        'text_show_private': "Témbongang pribadi",
        'text_hide_private': "Pendem pribadi",
        'text_use': "✅ Anggen teks",
        'text_saved': "Teks kasimpen dados:\n{0}",
        'text_saved_voice': "Teks kasimpen",
        'text_deleted': "Teks kicalang",
        'text_no_text_to_save': "Tan wénten teks jagi kasimpen.",
        'text_no_templates': "Tan wénten teks katemu",
        'text_private_master_required': "Teks pribadi prasida kaanggen yénten sampun wénten kruna sandi utama.\n\nKéngkén jagi ngadegang kruna sandi utama mangkin?",
        'text_filename': "Aran berkas antuk teks (tanpa 'Teks_' miwah '.txt'):",
        'text_filename_hint': "Conto: 'Telepon Kantor' pacang kasimpen dados 'Teks_Telepon Kantor.txt'",
        'text_save_hint': "Teks pacang kasimpen otomatis antuk format.",
        'text_guide_title': "Ngajiang Teks - Pangandika",
        'text_delete_confirm': "Nunas, yening jagi ngicalang teks puniki?\n\nBerkas: {0}\nTeks: {1}...",
        'text_make_public': "Tandai publik",
        'text_make_private': "Tandai pribadi",
        'text_privacy_changed': "Status privasi kauah",
        'text_private_always': "Témbongang teks pribadi salanturnyané (pangaturan)",
        'text_mode_required': "Nunas, aktifang mode Teks dumun",
        'text_continue_editing': "Lantur ngubah - kursor ring pungkuran teks",
        'text_no_input': "Tan wénten teks kaajiang - teks kaurungang",
        'save_dialog_question': "Kéngkén jagi nglanturang?",
        'text_save_question': "Simpen makejang teks miwah tanda silang, uah, lantur ngubah utawi urung?",
        'copy_cross': "Tanda silang kasalin",
        'paste_cross': "Tanda silang kasisipang",
        'paste_text': "Teks kasisipang",
        'cross_discarded': "Tanda silang kaurungang",
        'all_discarded': "Makejang kaurungang",
        'text_discarded': "Teks kaurungang",
        'no_texts_to_save': "Tan wénten teks jagi kasimpen",
        'no_valid_texts': "Tan wénten teks sah jagi kasimpen",
        'text_word_singular': "Teks",
        'text_word_plural': "Teks",
        'cross_word_singular': "Tanda silang",
        'cross_word_plural': "Tanda silang",
        'texts_saved_title': "Teks kasimpen",
        'texts_crosses_saved': "{0} {1} miwah {2} {3} sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'texts_crosses_saved_voice': "{0} {1} miwah {2} {3} kasimpen.",
        'texts_saved': "{0} {1} sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'texts_saved_voice': "{0} {1} kasimpen.",
        'crosses_saved': "{0} {1} sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'crosses_saved_voice': "{0} {1} kasimpen.",
        'elements_saved': "{0} élemén sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'elements_saved_voice': "{0} élemén kasimpen.",
        'text_window_load_error': "Jendela teks tan prasida kamuat",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Ngajiang Teks miwah Tata Teks – Pangandika Lengkap**

        **1. Nganggen miwah ngubah teks**
        - Klik tengen ring genah sané jagi kasisipang ring dokumén tur pilih "Sisipang teks".
        - Pacang kabuka jendela, ditu rauhin teks miwah uah format:
        • Ukuran aksara, Tebal, Miring, Garisi beten
        • Warna teks (prasida milih)
        • Bening (nganggén pangatur)
        • Putus garis (linggah-lian, c. linggah kaca, ciyut, tan putus)
        - Sasampun konfirmasi, teks pacang medal ring genah klik. Prasida gingsirang nganggén tetikus utawi panah.
        - Klik ganda ring teks jagi ngubah; antuk ESC medal saking mode ubah.

        **2. Tata Teks ngatur**
        - Ring jendela Teks, tengen wénten lis makejang teks sané kasimpen.
        - **Nyimpen teks:** Rauhina teks, uah format, klik "💾 Simpen dados teks". Ajiang aran berkas (tanpa akhiran).
        - **Ngamuat teks:** Klik aran ring lis. Teks miwah format pacang kambil tur prasida kauah yéning perlu.
        - **Ngapus:** Klik tengen ring teks jagi ngapus utawi ngubah status privasi.

        **3. Teks Pribadi (Kruna Sandi Utama)**
        - Yéning sampun ngadegang kruna sandi utama (ring Pangaturan → Tata Kruna Sandi), prasida nandai teks dados "pribadi".
        - Aktifang kotak centang "Teks pribadi" ring jendela sadurung nyimpen.
        - Teks pribadi pacang kaciré ring lis yéning sampun ngajiang kruna sandi utama pateh sasih (oténtikasi).
        - Niki mangda teks rahasia tan prasida kaciré olih tiosan.

        **4. Nganggen tanda silang**
        - Nganggén menu tengen prasida taler nyisipang tanda silang (c. antuk kotak centang).
        - Ukuran, tebel garis, miwah warna tanda silang prasida kaatur ring pangaturan (Menu "Pangaturan" → "Pangaturan nyilang").
        - Antuk klik tengen ring tanda silang sané sampun wénten prasida ngubah.

        **5. Aksi sauntukan**
        - Yéning wénten makudang teks utawi tanda silang ring kaca, prasida antuk menu tengen (klik tengen ring mode Teks) nyimpen utawi ngurung makejang.
        - Rikala nyimpen, makejang élemén pacang kasisipang ring PDF tur tetep dados grafik vektor.

        **6. Teken engkak ring mode Teks**
        - Panah: ngingsirang élemén
        - Ctrl+Panah: langkahan ageng
        - Enter: buka dialog nyimpen (simpen makejang / uah / urung)
        - ESC: urung élemén mangkin
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Ngajiang Teks miwah Tata Teks – Pangandika Lengkap</strong></p>

        <p><strong>1. Nganggen miwah ngubah teks</strong></p>
        <ul>
        <li>Klik tengen ring genah sané jagi kasisipang ring dokumén tur pilih "Sisipang teks".</li>
        <li>Pacang kabuka jendela, ditu rauhin teks miwah uah format:<br/>
        • Ukuran aksara, Tebal, Miring, Garisi beten<br/>
        • Warna teks (prasida milih)<br/>
        • Bening (nganggén pangatur)<br/>
        • Putus garis (linggah-lian, c. linggah kaca, ciyut, tan putus)</li>
        <li>Sasampun konfirmasi, teks pacang medal ring genah klik. Prasida gingsirang nganggén tetikus utawi panah.</li>
        <li>Klik ganda ring teks jagi ngubah; antuk ESC medal saking mode ubah.</li>
        </ul>

        <p><strong>2. Tata Teks ngatur</strong></p>
        <ul>
        <li>Ring jendela Teks, tengen wénten lis makejang teks sané kasimpen.</li>
        <li><strong>Nyimpen teks:</strong> Rauhina teks, uah format, klik "💾 Simpen dados teks". Ajiang aran berkas (tanpa akhiran).</li>
        <li><strong>Ngamuat teks:</strong> Klik aran ring lis. Teks miwah format pacang kambil tur prasida kauah yéning perlu.</li>
        <li><strong>Ngapus:</strong> Klik tengen ring teks jagi ngapus utawi ngubah status privasi.</li>
        </ul>

        <p><strong>3. Teks Pribadi (Kruna Sandi Utama)</strong></p>
        <ul>
        <li>Yéning sampun ngadegang kruna sandi utama (ring Pangaturan → Tata Kruna Sandi), prasida nandai teks dados "pribadi".</li>
        <li>Aktifang kotak centang "Teks pribadi" ring jendela sadurung nyimpen.</li>
        <li>Teks pribadi pacang kaciré ring lis yéning sampun ngajiang kruna sandi utama pateh sasih (oténtikasi).</li>
        <li>Niki mangda teks rahasia tan prasida kaciré olih tiosan.</li>
        </ul>

        <p><strong>4. Nganggen tanda silang</strong></p>
        <ul>
        <li>Nganggén menu tengen prasida taler nyisipang tanda silang (c. antuk kotak centang).</li>
        <li>Ukuran, tebel garis, miwah warna tanda silang prasida kaatur ring pangaturan (Menu "Pangaturan" → "Pangaturan nyilang").</li>
        <li>Antuk klik tengen ring tanda silang sané sampun wénten prasida ngubah.</li>
        </ul>

        <p><strong>5. Aksi sauntukan</strong></p>
        <ul>
        <li>Yéning wénten makudang teks utawi tanda silang ring kaca, prasida antuk menu tengen (klik tengen ring mode Teks) nyimpen utawi ngurung makejang.</li>
        <li>Rikala nyimpen, makejang élemén pacang kasisipang ring PDF tur tetep dados grafik vektor.</li>
        </ul>

        <p><strong>6. Teken engkak ring mode Teks</strong></p>
        <ul>
        <li>Panah: ngingsirang élemén</li>
        <li>Ctrl+Panah: langkahan ageng</li>
        <li>Enter: buka dialog nyimpen (simpen makejang / uah / urung)</li>
        <li>ESC: urung élemén mangkin</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Pangaturan nyilang",
        'cross_properties': "Sipat tanda silang",
        'cross_size': "Ukuran (px):",
        'cross_line_width': "Tebal garis:",
        'cross_color': "Warna:",
        'cross_choose_color': "Pilih",
        'cross_fine_tuning': "Pangateran pas rikala nyimpen (piksel)",
        'cross_offset_x': "Geser X:",
        'cross_offset_y': "Geser Y:",
        'cross_offset_x_tooltip': "Nilai négatip ngingsirang tanda silang rikala nyimpen ka kiwa, positif ka tengen",
        'cross_offset_y_tooltip': "Nilai négatip ngingsirang tanda silang rikala nyimpen ka duur, positif ka beten",
        'cross_preview': "Pratinjau",
        'cross_save': "Anggen pangaturan",
        'cross_customized': "Tanda silang kauah",
        'cross_settings_applied': "Pangaturan tanda silang kasimpen.\nUkuran: {0}px, Tebal garis: {1}px\n{2}",
        'cross_updated_count': "{0} tanda silang sané sampun wénten kauah.",
        'cross_no_crosses': "Tan wénten tanda silang katemu.",
        'cross_settings_applied_all': "Pangaturan tanda silang antuk makejang {0} tanda silang sampun kaanggén",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Pangaturan tanda tangan",
        'signature_1': "Tanda tangan 1",
        'signature_2': "Tanda tangan 2",
        'signature_select': "Pilih tanda tangan",
        'signature_add': "➕ Sisipang tanda tangan anyar...",
        'signature_size': "Ukuran antuk tanda tangan {0} (%):",
        'signature_common': "Pangaturan umum",
        'signature_timestamp': "Tambahan cap waktu otomatis",
        'signature_location': "Genah standar:",
        'signature_timestamp_size': "Ukuran aksara cap waktu:",
        'signature_no_files': "-- Tan wénten tanda tangan katemu --",
        'signature_insert': "Sisipang tanda tangan",
        'signature_insert_1': "Sisipang tanda tangan 1",
        'signature_insert_2': "Sisipang tanda tangan 2",
        'signature_customize': " Uah tanda tangan",
        'signature_discard': " Urungang tanda tangan puniki",
        'signature_save_all': " Simpen makejang tanda tangan",
        'signature_discard_all': " Urungang makejang tanda tangan",
        'signature_guide_title': "Tanda Tangan - Pangandika",
        'signature_guide': """
📝 Tanda Tangan - Pangandika cutet

- Adegang kruna sandi utama
- Tata tanda tangan ring menu Pangaturan
  (ukuran, cap waktu ...)
- Sisipang antuk KLIK TENGEN ring genah sané jagi kasisiang
  (kruna sandi utama perlu sakali per sasih)
- Gingsirang tanda tangan nganggén tetikus utawi panah
- Bisa nyisipang makudang tanda tangan
- Tiap tanda tangan prasida kauah
- Ngurungang tanda tangan sané kapilih
- Ngurungang utawi nyimpen makejang tanda tangan sakaligus
- Taler prasida nganggén bar menu.
        """,
        'signature_placeholder': "Tan wénten pratinjau",
        'signature_info': "Tanda tangan {0}: {1}×{2} px ({3}% saking {4}×{5})",
        'signature_info_placeholder': "Pangaturan antuk tanda tangan {0}",
        'signature_inserted': "Tanda tangan {0} kasisipang ring kaca {1}",
        'signature_deleted': "Tanda tangan kicalang",
        'signature_copied': "Tanda tangan kasalin",
        'signature_pasted': "Tanda tangan {0} kasisipang",
        'signature_saved': "{0} tanda tangan sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'signature_saved_voice': "{0} tanda tangan kasimpen",
        'mode_replace_signature_format': "Puputang mode miwah sisipang tanda tangan {0}",
        'mode_conflict_voice_signature': "Mode {0} aktip. Puputang miwah sisipang tanda tangan?",
        'signature_not_configured': "Tanda tangan {0} nenten katur",
        'signature_file_not_found': "Berkas tanda tangan nenten katemu",
        'timestamp_format': "{0}, tanggal {1}",
        'no_copied_signature': "Tan wénten tanda tangan kasalin",
        'no_signatures_to_save': "Tan wénten tanda tangan jagi kasimpen",
        'signature_save_question': "Simpen makejang tanda tangan, uah utawi urung puniki?",
        'signatures_saved_title': "Tanda tangan kasimpen",
        'signatures_saved': "{0} tanda tangan sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'signatures_saved_voice': "{0} tanda tangan kasimpen.",
        'all_signatures_discarded': "Makejang tanda tangan kaurungang",
        'signature_settings_saved': "Pangaturan tanda tangan kasimpen",
        'signature_cancelled': "Tanda tangan kaurungang",
        'signature_active_title': "Tanda tangan aktip",
        'signature_replace_question': "Sampun wénten tanda tangan aktip.\n\nKéngkén jagi ngingsirang tanda tangan mangkin?",
        'signature_replace': "Gingsirang tanda tangan",
        'signature_replace_voice': "Gingsirang tanda tangan mangkin utawi urung?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Pangaturan gambar",
        'image_common': "Pangaturan gambar umum",
        'image_keep_aspect': "Tetepang proporsi rikala ngingsirang",
        'image_default_size': "Ukuran standar (%):",
        'image_dark_invert': "Balikang gambar ring Mode Peteng",
        'image_dark_invert_tooltip': "Aktip: gambar pacang kawalikang mangda becik kacingak",
        'image_fine_tuning': "Pangateran pas (piksel)",
        'image_offset_x': "Geser X:",
        'image_offset_y': "Geser Y:",
        'image_offset_x_tooltip': "Nilai négatip ngingsirang gambar rikala nyimpen ka kiwa, positif ka tengen",
        'image_offset_y_tooltip': "Nilai négatip ngingsirang gambar rikala nyimpen ka duur, positif ka beten",
        'image_select': "Pilih gambar",
        'image_insert': "Sisipang gambar",
        'image_customize': " Uah gambar",
        'image_aspect': " Tetepang proporsi",
        'image_discard': " Urungang gambar puniki",
        'image_save_all': " Simpen makejang gambar",
        'image_discard_all': " Urungang makejang gambar",
        'image_filter': "Gambar",
        'image_guide_title': "Sisipang Gambar - Pangandika",
        'image_guide': """
📷 Sisipang Gambar ring PDF - Pangandika cutet:

1. Klik tengen ring genah sané jagi kasisiang
2. "Sisipang gambar" → Pilih gambar
3. Genahang gambar: gingsirang nganggén tetikus
4. Uah ukuran: gingsirang ring sisi/pakpakan
5. Tetepang proporsi: teken [A]
6. Uah lianan: Klik tengen ring gambar

Saran: Ring menu tengen prasida ngatur pangaturan.
        """,
        'image_inserted': "Gambar {0} kasisipang ring kaca {1}",
        'image_deleted': "Gambar kaurungang",
        'image_copied': "Gambar kasalin",
        'image_pasted': "Gambar kasisipang",
        'image_saved': "{0} gambar sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'image_saved_voice': "{0} gambar kasimpen",
        'image_aspect_on': "aktip",
        'image_aspect_off': "tan aktip",
        'image_aspect_toggle': "Tetepang proporsi {0}",
        'image_reset': "Gambar kawalikang ka ukuran asli",
        'image_replaced': "Gambar kagingsirang",
        'image_invalid': "Nenten gambar sané sah",
        'mode_replace_image': "Sisipang gambar",
        'mode_conflict_voice_image': "Mode {0} aktip. Puputang miwah sisipang gambar?",
        'image_active_title': "Gambar aktip",
        'image_replace_question': "Sampun wénten gambar aktip.\n\nKéngkén jagi ngingsirang gambar mangkin?",
        'image_replace': "Gingsirang gambar",
        'image_replace_voice': "Gingsirang gambar mangkin utawi urung?",
        'image_filter_all': "Gambar (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Makejang Berkas (*.*)",
        'no_copied_image': "Tan wénten gambar kasalin",
        'image_discarded': "Gambar kaurungang",
        'image_save_question': "Simpen makejang gambar, uah utawi urung puniki?",
        'no_images_to_save': "Tan wénten gambar jagi kasimpen",
        'no_valid_images': "Tan wénten gambar sah jagi kasimpen",
        'images_saved_title': "Gambar kasimpen",
        'images_saved': "{0} gambar sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'images_saved_voice': "{0} gambar kasimpen.",
        'all_images_discarded': "Makejang gambar kaurungang",
        'image_settings_updated': "Pangaturan gambar kauah",
        'image_replace_title': "Pilih gambar anyar",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Pangaturan wangun",
        'form_basic': "Pangaturan dasar",
        'form_default_type': "Tipe wangun standar:",
        'form_rectangle': "Pasagi",
        'form_ellipse': "Bunder",
        'form_line': "Garisi",
        'form_arrow': "Panah",
        'form_line_width': "Tebal garis:",
        'form_colors': "Warna",
        'form_line_color': "Warna garis:",
        'form_fill_color': "Warna isi:",
        'form_choose_color': "Pilih",
        'form_transparent': "Latar bening (wantah garis)",
        'form_filled': "kasi",
        'form_dark_mode': "Mode Peteng",
        'form_dark_invert': "Balikang warna ring Mode Peteng",
        'form_fine_tuning': "Pangateran pas (piksel)",
        'form_offset_x': "Geser X:",
        'form_offset_y': "Geser Y:",
        'form_offset_x_tooltip': "Nilai négatip ngingsirang wangun rikala nyimpen ka kiwa, positif ka tengen",
        'form_offset_y_tooltip': "Nilai négatip ngingsirang wangun rikala nyimpen ka duur, positif ka beten",
        'form_preview': "Pratinjau",
        'form_insert': "Sisipang wangun",
        'form_rectangle_insert': "Pasagi",
        'form_ellipse_insert': "Bunder",
        'form_line_insert': "Garisi (2 klik)",
        'form_arrow_insert': "Panah (2 klik)",
        'form_customize': " Uah wangun",
        'form_transparent_toggle': " Latar bening",
        'form_discard': " Urungang wangun puniki",
        'form_save_all': " Simpen makejang wangun",
        'form_discard_all': " Urungang makejang wangun",
        'form_guide_title': "Sisipang Wangun - Pangandika",
        'form_guide': """
📐 Sisipang Wangun ring PDF - Pangandika cutet:

1. Pilih tipe wangun (Pasagi, Bunder, Garisi, Panah)
2. Klik ring genah
   - Antuk Pasagi/Bunder: Sakali klik nempatang wangun
   - Antuk Garisi/Panah: Kalih klik antuk titik pangawit miwah pungkasan
3. Genahang wangun: gingsirang nganggén tetikus
4. Uah ukuran: gingsirang ring sisi/pakpakan
5. Simpen wangun: Enter
6. Urung wangun: ESC
7. Uah lianan: Klik tengen ring wangun

Saran: Ring menu tengen prasida ngatur pangaturan.
        """,
        'form_inserted': "{0} kasisipang ring kaca {1}",
        'form_deleted': "Wangun kicalang",
        'form_copied': "Wangun kasalin",
        'form_pasted': "Wangun kasisipang",
        'form_saved': "{0} wangun sampun kasisipang ring PDF.\n\nPDF kamuatin malih...",
        'form_saved_voice': "{0} wangun kasimpen",
        'form_reset': "Wangun kawalikang ka ukuran standar",
        'form_transparent_on': "aktip",
        'form_transparent_off': "tan aktip",
        'form_transparent_toggled': "Latar bening {0}",
        'form_line_cancel': "Nggambar garis kaurungang",
        'form_second_click': "Mangkin klik titik pungkasan antuk {0}",
        'mode_replace_form': "Sisipang wangun",
        'mode_conflict_voice_form': "Mode {0} aktip. Puputang miwah sisipang wangun?",
        'form_settings_updated': "Pangaturan wangun kauah",
        'form_unknown': "Wangun",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klik ring genah pangawit",
        'form_line_guide_2': "2. Klik ring genah pungkasan",
        'form_line_guide_3': "Garisi pacang kagambar riantara kalih titik punika.",
        'form_line_status_1': "Ngantos klik ka-1...",
        'form_line_status_2': "Titik ka-1 kaset: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Mangkin klik titik pungkasan...",
        'form_line_status_4': "Kalih titik sampun kaset.\nKlik 'Puput' jagi nyimpen.",
        'form_line_reset': "Balikang",
        'form_line_finish': "Puput",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Salin (Cmd+C)",
        'paste': "Tempel (Cmd+V)",
        'copied': "Kasalin: {0}",
        'no_element_to_copy': "Tan wénten élemén kapilih jagi kasalin",
        'no_copied_data': "Tan wénten data kasalin",
        'no_valid_position': "Tan wénten genah sah jagi nempel",
        'copy_text': "Teks kasalin",
        'copy_image': "Gambar kasalin",
        'copy_form': "Wangun kasalin",
        'copy_signature': "Tanda tangan kasalin",
        'element_text': "Teks",
        'element_image': "Gambar",
        'element_form': "Wangun",
        'element_signature': "Tanda tangan",
        'element_unknown': "Élemén",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflik mode",
        'mode_conflict_message': "Sampun wénten mode '{0}' aktip.\n\nKéngkén jagi puputang miwah {1}?",
        'mode_replace': "Puputang mode miwah {0}",
        'mode_cancel': "Urung",
        'mode_replace_text': "sisipang teks",
        'mode_replace_cross': "sisipang tanda silang",
        'mode_replace_signature': "sisipang tanda tangan",
        'mode_replace_image': "sisipang gambar",
        'mode_replace_form': "sisipang wangun",
        'mode_conflict_voice': "Mode {0} aktip. Puputang miwah sisipang teks?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Ngajiang teks",
        'active_mode_signature': "Tanda tangan",
        'active_mode_image': "Gambar",
        'active_mode_form': "Wangun",
        'active_mode_and': " miwah ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Sisipang",                    # Hauptmenü
        'insert_another_text': "Sisipang teks",          # Vereinfacht
        'insert_another_cross': "Sisipang tanda silang",        # Vereinfacht
        'insert_another_signature_1': "Tanda tangan 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Tanda tangan 2",      # Untermenü-Eintrag
        'insert_another_image': "Sisipang gambar",         # Vereinfacht
        'insert_another_form_rect': "Pasagi",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Bunder",        # Untermenü-Eintrag
        'insert_another_form_line': "Garisi (2 klik)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Panah (2 klik)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Simpen {0}",
        'save_dialog_message': "{0} pacang kasimpen ring kaca {1}.\n\nKéngkén jagi nglanturang?",
        'save_all': "Simpen makejang {0}",
        'save_single': "Simpen {0}",
        'save_customize': "Uah {0}",
        'save_discard': "Urungang {0} puniki",
        'save_continue': "Lantur ngubah",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Ka kaca {0}",
        'context_rotate': " Puter kaca {0}",
        'context_delete': " Hapus kaca {0}",
        'context_export': " Ekspor kaca {0}",
        'context_mark_as': " Tandain kaca dados...",
        'context_mark_empty': " Kaca kosong",
        'context_unmark_empty': " Nenten kosong",
        'context_mark_export': " Tandain antuk ekspor",
        'context_unmark_export': " Nenten ekspor",
        'context_batch_actions': " Aksi massal",
        'context_batch_delete_empty': " Hapus makejang {0} kaca kosong",
        'context_batch_export_single': " Makejang {0} kaca (asiki berkas)",
        'context_batch_export_split': " Makejang {0} kaca (kapisah)",
        'context_drag_start': " Kawitin Drag & Drop",
        'context_drag_stop': " Puputang Drag & Drop",
        'context_insert': " Sisipang",
        'context_insert_pages': " Sisipang kaca",
        'context_zoom': "Zoom",
        'discard_mixed': "Urungang makejang {0} {1} miwah {2} {3}",
        'save_mixed': "Simpen {0} {1} miwah {2} {3}",
        'discard_texts': "Urungang makejang {0} teks",
        'discard_text_single': "Urungang 1 teks",
        'save_texts': "Simpen {0} teks",
        'save_text_single': "Simpen 1 teks",
        'discard_crosses': "Urungang makejang {0} tanda silang",
        'discard_cross_single': "Urungang 1 tanda silang",
        'save_crosses': "Simpen {0} tanda silang",
        'save_cross_single': "Simpen 1 tanda silang",
        'discard_signatures': "Urungang makejang {0} tanda tangan",
        'save_signature_single': "Simpen 1 tanda tangan",
        'save_signatures': "Simpen {0} tanda tangan",
        'discard_images': "Urungang makejang {0} gambar",
        'save_image_single': "Simpen 1 gambar",
        'save_images': "Simpen {0} gambar",
        'discard_forms': "Urungang makejang {0} wangun",
        'save_form_single': "Simpen 1 wangun",
        'save_forms': "Simpen {0} wangun",
        'cross_discard': "Urungang tanda silang puniki",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Ekspor / Impor Info",
        'export_what': "📋 Apa sané kaekspor?",
        'export_general': "Pangaturan umum",
        'export_general_items': "• Suara (aktip/ten, kacepatan)\n• Mode Peteng/Terang\n• Pangaturan backup\n• Pangaturan OCR",
        'export_image_form': "Pangaturan gambar miwah wangun",
        'export_image_form_items': "• Pangaturan gambar (proporsi, ukuran standar)\n• Pangaturan wangun (tebel garis, warna)\n• Pangaturan tanda tangan (alamat, ukuran, cap waktu)",
        'export_passwords': "Database kruna sandi",
        'export_passwords_items': "• Makejang kruna sandi PDF sané kasimpen\n• Prasida kaciptayang utawi tan kaciptayang",
        'export_master': "Pangaturan kruna sandi utama",
        'export_master_items': "• Hash kruna sandi utama\n• Pangaturan antuk tanda tangan/teks",
        'export_signatures': "Tanda tangan miwah teks",
        'export_signatures_items': "• Makejang berkas gambar (tanda tangan)\n• Makejang teks antuk format\n• Tandai pribadi/publik",
        'export_import_warning': "⚠️ Pikobet penting",
        'export_import_note': "• Rikala impor, MAKEJANG pangaturan mangkin pacang kagingsirang\n• Perlu ngawitin malih aplikasi\n• Tanda tangan/teks sané sampun wénten pacang kagingsirang",
        'export_master_note': "• Yéning kruna sandi utama kaset, prasida milih:\n  - Tan kaciptayang (kruna sandi langsung kacingak)\n  - Kaciptayang (wantah prasida kabaca nganggén kruna sandi utama)",
        'export_security': "• Berkas ZIP sané kaekspor madaging data rahasia\n• Simpen ring genah aman (c. USB stick kaciptayang)\n• Yéning berkas ical: kruna sandi tan prasida kabalikang",
        'export_format': "📁 Format ekspor",
        'export_format_desc': "Pangaturan pacang kasimpen ring asiki berkas ZIP:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Pangaturan prasida kaekspor",
        'export_failed': "Ekspor gagal",
        'export_import_question': "Kéngkén jagi ngawitin malih aplikasi mangkin?",
        'export_password_question': "Kruna sandi utama kaset.\n\nKéngkén jagi ngekspor kruna sandi tan kaciptayang?\n(yen ten, pacang kaekspor antuk kaciptayang)",
        'export_decrypt': "Ekspor tan kaciptayang",
        'export_encrypt': "Ekspor antuk kaciptayang",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Indik PDF Dark View",
        'info_version': "Versi",
        'info_author': "Kakardi olih Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Indik",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> inggih punika paningal PDF sané prasida kaanggén olih sinamian, kawewehin antuk anak sané madué pikobet paningalan.</p>

            <p><strong>Ceciren utama:</strong></p>
            <ul>
                <li>Lontaran sané kontras, prasida kaatur</li>
                <li>Pangaturan antuk kenypian</li>
                <li>Kapasitas swara sané kagabung</li>
                <li>OCR antur dokumén sané kascan</li>
                <li>Piranti ngubah sané jangkep</li>
            </ul>

            <p>Luwih saking 50 basa kaicén – mangda PDF prasida kaanggén olih sami.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Fungsi",
        'info_features_intro': "PDF Dark View ngicénin ragané indik:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Paningalan & Navigasi</strong> – Mode Peteng/Terang, nyansan kaca, zoom, lantur ka kaca</li>
            <li><strong>OCR (Pangaksara Teks)</strong> – Dokumén sané kascan prasida kapanéhan tur kasalin</li>
            <li><strong>Ngubah</strong> – Sisipang teks, tanda silang, tanda tangan, gambar miwah wangun</li>
            <li><strong>Ngatur Kaca</strong> – Hapus, alusin, sisipang, gingsirang nganggén Drag & Drop</li>
            <li><strong>Ekspor</strong> – Nuju Word, Pages utawi dados teks</li>
            <li><strong>Kaamanan</strong> – Perlindungan kruna sandi miwah pangaturannyané</li>
            <li><strong>Kapasitas</strong> – Swara, pangaturan kenypian, kontras sané tegeh</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Pangaturan",
        'info_accessibility': "♿ Kapasitas – pangaturan kenypian sané jangkep",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Umum</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Buka PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Nyarengin</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Gingsirang Mode Peteng/Terang</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Cetak</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Puputang</div>

        <div class="shortcut-cat">📖 Navigasi</div>
        <div class="shortcut-row"><kbd>Panah</kbd> Kaca per kaca</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Ka kaca</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Kaca ka-1</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Kaca pungkasan</div>

        <div class="shortcut-cat">✏️ Ngubah</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Sisipang teks</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Hapus kaca</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Alusin kaca</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Sisipang kaca</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Gingsirang kaca</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Puter kaca</div>

        <div class="shortcut-cat">🖼️ Gingsirang Élemén</div>
        <div class="shortcut-row"><kbd>Panah</kbd> Gingsirang teks/gambar/tanda tangan</div>
        <div class="shortcut-row"><kbd>Ctrl+Panah</kbd> Langkahan ageng</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Simpen</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Urungang</div>

        <div class="shortcut-cat">🗣️ Swara</div>
        <div class="shortcut-row"><kbd>F2</kbd> Aktipang/paténang swara</div>
        """,
        'info_contextmenu': "📌 Penting: Makejang fungsi taler prasida kaaksés antuk menu tengen (klik tengen)!",
        'info_accessibility_hint': "💡 Saran: Swara (F2) ngawantu orientasi tur ngicénin umpan balik antuk menu miwah dialog.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lisensi & Impresum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUM</strong><br>
        Anggan manut § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Jerman<br>
        Email: binhdiez64@gmail.com<br>
        Tanggung jawab antuk isi: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Panyingakin</strong><br>
        Piranti lunak puniki kakardi antuk paindikan sané becik pisan. Tan wénten jaminan antuk katepatan, kelengkapan miwah fungsi. Panganggéné wantah tanggung jawab pribadi.<br><br>

        <strong>📄 Lisensi MIT (anggén pribadi)</strong><br>
        Hak cipta (c) 2026 Toralf Schulz (BinhDiez)<br>
- Kaicén: anggén gratis, ngubah antuk pribadi, nyalin antuk pribadi.<br>
- Nenten kaicén: adol, anggén komersial, ngicalang tandha hak cipta.<br><br>

        <strong>🔧 Komponén saking pihak katiga</strong><br>
        Piranti lunak puniki madaging komponén sané madué lisensi GPL, AGPL, Apache 2.0, BSD miwah MIT.<br>
        Yening kasebarkang, patuhin syarat lisensi sané becik.<br><br>

        <strong>🌐 Open Source</strong><br>
        Kode sumber prasida kacingak, kauah, miwah kasebarkang manut syarat lisensi sané becik.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Pangaksama",
        'info_credits': "Matur suksma antuk komunitas Open Source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Ngolah PDF</li>
            <li><strong>PyQt5</strong> – Antarmuka grafis</li>
            <li><strong>Tesseract OCR</strong> – Pangaksara teks</li>
            <li><strong>OCRmyPDF</strong> – Integrasi OCR</li>
            <li><strong>python-docx</strong> – Ekspor Word</li>
            <li><strong>qtawesome</strong> – Ikon</li>
            <li><strong>DeepSeek</strong> – Wantuan antuk terjemahan (50+ basa)</li>
            <li><strong>Sami sané nganggén</strong> – Antuk saran sané mabuat</li>
            <li><strong>Komunitas Open Source</strong> – Antuk pustaka sané becik</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Basa",
        'info_languages_header': "🌍 Panglola Basa",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View mangkin nyokong <strong>62 basa</strong> – mangda piranti lunak punika prasida kaanggén ring sajebag gumi.</p>

            <p><strong>📖 Lis Lengkap Basa (Per Maret 2026):</strong></p>
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
                    <li>🇩🇪 Jerman</li>
                    <li>🇬🇧 Inggris (English)</li>
                    <li>🇪🇪 Estonia (Eesti)</li>
                    <li>🇫🇮 Finlandia (Suomi)</li>
                    <li>🇫🇷 Perancis (Français)</li>
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
                    <li>🇲🇳 Mongol (Монгол)</li>
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
                    <li>🇹🇭 Thailand (ไทย)</li>
                    <li>🇨🇿 Ceko (Čeština)</li>
                    <li>🇹🇷 Turki (Türkçe)</li>
                    <li>🇺🇦 Ukraina (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnam (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yiddish (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Nambahkan Basa Diri:</strong><br>
                Yening wantah basa sane durung wenten? Pasang kemanten berkas kamus (<code>sprache_xx.py</code>) nampek aplikasi – piranti lunak pacang ngangken otomatis. Yening有兴趣 ring terjemahan khusus, sumangga kontak titiang.
            </div>

            <p><strong>🙏 Suksma Khusus:</strong> DeepSeek antuk panglola ring pangalihan basa antuk sami kamus ring 62 basa.</p>

            <p>📧 Kontak antuk terjemahan: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Pikobet",
        'error_occurred': "Wénten pikobet",
        'error_pdf_load': "Pikobet rikala ngamuat PDF",
        'error_pdf_save': "Pikobet rikala nyimpen PDF",
        'error_ocr': "Pikobet rikala pangaksara teks",
        'error_no_pdf': "Tan wénten PDF kajemak",
        'error_page_not_found': "Kaca nenten katemu",
        'error_invalid_range': "Wewidangan kaca tan sah",
        'error_file_not_found': "Berkas nenten katemu",
        'error_permission': "Tan wénten izin",
        'error_unknown': "Pikobet tan kauningin",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Prasida",
        'success_operation': "Aksi prasida puput",
        'success_saved': "Prasida kasimpen",
        'success_exported': "Prasida kaekspor",
        'success_imported': "Prasida ka-impor",
        'success_deleted': "Prasida kicalang",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Konfirmasi",
        'confirm_yes': "Inggih",
        'confirm_no': "Nenten",
        'confirm_ok': "OK",
        'confirm_cancel': "Urung",
        'confirm_delete': "Hapus",
        'confirm_overwrite': "Gingsirang",
        'confirm_continue': "Lanturang",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF kasiyang...",
        'progress_saving': "PDF kasimpen...",
        'progress_exporting': "PDF kaekspor...",
        'progress_processing': "Ngolah...",
        'progress_wait': "Nunas antos...",
        'progress_preparing': "Nyiapang...",
        'progress_finalizing': "Nyelesaiang...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Putih",
        'color_black': "Selem",
        'color_red': "Barak",
        'color_green': "Ijo",
        'color_blue': "Biru",
        'color_yellow': "Kuning",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Oranye",
        'color_gray': "Abu-abu",
        'color_custom': "Pilih warna",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Berkas",
        'menu_edit': "&Ubah",
        'menu_view': "&Témbongang",
        'menu_tools': "&Piranti",
        'menu_settings': "&Pangaturan",
        'menu_help': "&Wantuan",
        'menu_language': "🌐 Basa",
        'menu_guides': "&Panduan",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Buka",
        'file_save_as': "&Simpen dados...",
        'file_protect': "&Amanang dokumén...",
        'file_export': "&Ekspor",
        'file_export_pages': "Ekspor dados Pages",
        'file_export_word': "Ekspor dados DOCX",
        'file_export_text': "Ekspor dados TXT",
        'file_print_now': "&Cetak langsung",
        'file_print': "&Cetak",
        'file_close': "&Tutup",
        'file_quit': "&Puputang",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Nyarengin",
        'edit_ocr': " Gelarang OCR",
        'edit_rotate': "&Puter kaca",
        'edit_rotate_all': "&Puter makejang kaca",
        'edit_delete_pages': "&Hapus kaca",
        'edit_extract_pages': "&Alusin kaca",
        'edit_insert_pages': "&Sisipang kaca",
        'edit_move_pages': "&Gingsirang kaca",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Sisipang teks miwah tanda silang",
        'text_insert': " Sisipang teks",
        'cross_insert': " Sisipang tanda silang",
        'text_customize': " Uah teks",
        'cross_customize': " Uah tanda silang puniki",
        'cross_customize_all': " Uah makejang tanda silang",
        'text_discard': " Urungang teks / tanda silang puniki",
        'text_discard_all': " Urungang makejang teks miwah tanda silang",
        'text_save_all': " Simpen makejang teks miwah tanda silang",
        'text_guide': " Pangajiang teks / Tata teks - Panduan",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Sisipang tanda tangan",
        'signature_settings_menu': " Pangaturan...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Sisipang gambar",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Sisipang wangun",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Témbongang jendela teks",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Linggah kaca (standar)",
        'view_zoom_two': "&Kalih kaca",
        'view_zoom_overview': "&Ringkesan (makudang kaca)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Kapasitas",
        'settings_voice': "Swara",
        'settings_voice_tooltip': "nambahin informasi antuk swara saking screenreader",
        'settings_signature': "&Pangaturan tanda tangan",
        'settings_password': "&Pangaturan kruna sandi",
        'settings_backup': "Kardi backup sadurung ngubah",
        'settings_export_import': "&Ekspor / impor pangaturan",
        'settings_export': "&Ekspor makejang pangaturan...",
        'settings_import': "&Impor makejang pangaturan...",
        'settings_export_info': "&Apa sané kaekspor?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "aktip",
        'voice_off': "patén",
        'voice_toggle': "Swara {0}",
        'voice_speed': "Kacepatan ring {0} persen",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Piranti nenten katemu:\n{0}\n\nBASE_DIR: {1}\nPastiang yéning piranti PDF sampun kainsstal ring direktori {1}.",
        'tool_started': "{0} kawitin",
        'tool_start_failed': "Tan prasida kawitin",
        'process_error_failed_to_start': "Proses tan prasida kawitin. Napi berkas wénten?",
        'process_error_crashed': "Proses labuh rikala kawitin.",
        'process_error_timeout': "Wastu proses kadauan.",
        'process_error_write': "Pikobet nyurat ring proses.",
        'process_error_read': "Pikobet maca ring proses.",
        'process_error_unknown': "Pikobet proses tan kauningin",
        'process_command': "Paréntah",
        'process_normal_exit': "puput becik",
        'process_crashed': "labuh",
        'process_nonzero_exit': "{0} puput antuk kode pikobet {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Kaurungang...",
        'move_cancelling': "Ngingsirang kaurungang",
        'opening_pdf': "PDF kabuka...",
        'loading_document': "Ngamuat dokumén...",
        'pdf_opened': "PDF kabuka",
        'pages_found_moving': "{0} kaca katemu, {1} jagi gingsirang",
        'creating_backup': "Ngardi backup...",
        'backup_description': "Nyimpen berkas asli...",
        'backup_saved_as': "Kasimpen dados: {0}",
        'error_format': "Pikobet: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Nyarengin kausud",
        'page_header_simple': "=== Kaca {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Pangaturan kruna sandi – Panduan",
        'password_guide_voice': "Panduan indik pangaturan kruna sandi. Baca pangandikané.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Pangaturan kruna sandi – Panduan jangkep</strong></p>

        <p><strong>1. Perlindungan kruna sandi antuk PDF</strong></p>
        <ul>
        <li>Rikala ngajak PDF sané madaging kruna sandi, dialog pacang medal antuk ngajiang kruna sandi.</li>
        <li>Prasida nyimpen kruna sandi antuk kaciptayang, mangda tan perlu ngajiang nyabran warsa (centang „Simpen kruna sandi“).</li>
        <li>Antuk tombol „Buang kruna sandi“ prasida ngardi salinan PDF sané tan kaciptayang tur ngicalang kruna sandi saking database.</li>
        </ul>

        <p><strong>2. Kruna sandi utama</strong></p>
        <ul>
        <li>Kruna sandi utama ngamannang aksés ka makejang kruna sandi PDF sané kasimpen.</li>
        <li><strong>Ngadegang:</strong> Ka "Pangaturan → Tata kruna sandi → Pangaturan kruna sandi utama" tur klik "Ngadegang kruna sandi utama". Pilih kruna sandi sané aman (min. 8 karakter).</li>
        <li><strong>Ngubah:</strong> Sasampun oténtikasi prasida ngubah kruna sandi utama.</li>
        <li><strong>Ngicalang:</strong> Yéning ngicalang kruna sandi utama, MAKEJANG kruna sandi sané kasimpen pacang ical tahanan. Prasida ngardi ekspor cadangan sadurungnyan.</li>
        <li>Sasih apisan, patut oténtikasi antuk kruna sandi utama mangda prasida ngakses fungsi sané kaamannang (c. némbongang kruna sandi).</li>
        </ul>

        <p><strong>3. Tata kruna sandi (Lis)</strong></p>
        <ul>
        <li>Ring "Pangaturan → Tata kruna sandi" kabuka tabel makejang PDF sané kasimpen antuk kruna sandi sané kaciptayang.</li>
        <li><strong>Tanpa kruna sandi utama:</strong> Wantah prasida ngicalang entri – kruna sandi kantun maseb.</li>
        <li><strong>Antuk kruna sandi utama (sampun oténtikasi):</strong> Prasida némbongang, nyalin, ngekspor miwah ngicalang kruna sandi.</li>
        <li><strong>Ekspor:</strong> Pilih format (JSON, CSV, TXT) tur simpen lis. Yéning kruna sandi utama kaset, prasida milih ngekspor kruna sandi langsung kacingak utawi kantun kaciptayang.</li>
        <li><strong>Impor:</strong> Berkas ZIP sané kaekspor sadurungnyané (mawinan makejang pangaturan, rumasuk kruna sandi) prasida ka-impor malih nganggén "Pangaturan → Ekspor/impor pangaturan". Awas: data sané sampun wénten pacang kagingsirang!</li>
        </ul>

        <p><strong>4. Panggawé kruna sandi</strong></p>
        <ul>
        <li>Ring dialog kruna sandi (c. rikala ngamannang PDF) ring tengen kotak pangajian wénten tombol dadu 🎲.</li>
        <li>Klik jagi ngajak panggawé kruna sandi. Prasida ngatur lantang, karakter (ageng, alit, angka, tanda baca) miwah pamatiyas mangda becik kawacén.</li>
        <li>Kruna sandi sané kakardi prasida langsung kaanggén tur kasalin yéning perlu.</li>
        </ul>

        <p><strong>5. Pikobet kaamanan penting</strong></p>
        <ul>
        <li>Kruna sandi sané kasimpen kaciptayang nganggén AES-256. Konci kambil saking kruna sandi utama ragané (yéning kaset) utawi saking nilai tetep (yéning tanpa kruna sandi utama).</li>
        <li>Tanpa kruna sandi utama, kruna sandi kantun kaciptayang, nanging konci wénten ring program – anak sané madué aksés ka berkas ragané prasida mabuka. Dados, titiang nyaranang nganggén kruna sandi utama.</li>
        <li>Database kruna sandi magenah ring direktori `Daten/passwords.json`. Ngardi backup sacara berkala, utaminé sadurung ngicalang kruna sandi utama.</li>
        <li>Yéning lali kruna sandi utama, makejang kruna sandi sané kasimpen pacang ical tahanan.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # Neu ab 2026-03-19
        # ============================================

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Mode walik",
        'invert_mode_classic': "Klasik (walik makejang warna)",
        'invert_mode_smart': "Pintar (wantah katerangan)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Batas wates abu-abu",
        'gray_threshold_10': "10% (kaku)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (standar)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (lemah)",
        'threshold_changed': "Batas wates kaset ring {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Batas wates abu-abu – Palajahan",
        'threshold_guide_text': "Batas wates abu-abu nentuang piksel mana sané ring mode peteng pinar janten 'abu-abu' tur kawalik.\n\n"
                                "• Nilai rendah (10%) wantah ngawalik abu-abu sané sampurna – élemén mawarna kantun becik.\n"
                                "• Nilai tegeh (50%) ngawalik taler piksel sané mawarna sakedik – niki nambah kontras, nanging prasida ngubah warna.\n\n"
                                "Nilai sané becik gumantung ring dokumén. Antuk dokumén teks, 30–40% becik, antuk grafik mawarna 10–20%.\n\n"
                                "Prasida ngubah nilai sairik ring menu 'Pangaturan' – PDF pacang kamuat malih.\n\n"
                                "Catetan:\n* Foto miwah gambar wantah prasida kacingak becik ring mode terang!\n* Pangaturan walik wantah kacingak yéning mode peteng aktip.",
        'threshold_guide_voice': "Batas wates abu-abu nentuang seberapa kuat mode peteng pinar ngamargiang aksi. Nilai rendah ngajaga warna, nilai tegeh nambah kontras.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF kabuka...",
        'progress_loading_document': "Ngamuat dokumén...",
        'progress_pdf_opened': "PDF kabuka",
        'progress_creating_backup': "Ngardi backup...",
        'progress_backup_description': "Nyimpen berkas asli...",
        'progress_backup_created': "Backup kakardi",
        'progress_backup_saved_as': "Kasimpen dados: {0}",
        'progress_analyzing_start': "Ngawitin analisis...",
        'progress_searching_empty': "Nyarengin kaca kosong...",
        'progress_page_empty': "Kaca {0} kosong",
        'progress_page_keep': "Kaca {0} tetep",
        'progress_analysis_complete': "Analisis puput",
        'progress_empty_found': "{0} kaca kosong katemu",
        'progress_current_page': "Kaca mangkin",
        'progress_mark_delete': "Katandain jagi hapus",
        'progress_range_selected': "Wewidangan kaca {0}-{1}",
        'progress_deleting_pages': "Ngapus {0} kaca",
        'progress_creating_new_pdf': "Ngardi PDF anyar...",
        'progress_transferring_pages': "Ngelahin kaca",
        'progress_keeping_page': "Kaca {0} tetep ({1}/{2})",
        'progress_saving_pdf': "Nyimpen PDF...",
        'progress_optimizing': "Ngoptimalisasi ukuran...",
        'progress_finalizing': "Nyelesaiang...",
        'progress_new_size': "Ukuran anyar: {0:.2f} MB",
        'progress_cancelling': "Kaurungang...",
        'progress_cancel_message': "{0} kaurungang",
        'progress_pages_found_moving': "{0} kaca katemu, {1} jagi gingsirang",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF kaanalisis...",
        'ocr_status_optimizing': "Ngoncengang gambar...",
        'ocr_status_recognizing': "Pangaksara teks...",
        'ocr_status_embedding': "Teks kamargiang...",
        'ocr_status_finalizing': "Nyelesaiang PDF...",

        # PDF-Laden
        'progress_preparing': "Nyiapang...",
        'progress_loading': "PDF kasiyang...",

        # Seitenoperationen
        'progress_deleting_title': "Ngapus kaca...",
        'progress_moving_title': "Ngingsirang kaca...",
        'pages_found': "Kaca katemu",
        'progress_creating_new_order': "Ngardi urutan anyar...",
        'progress_sorting_pages': "Nata kaca...",
        'progress_moving_to_begin': "Ngingsirang {0} kaca ka pangawit",
        'progress_transferring_count': "Ngelahin {0} kaca",
        'progress_transferring_before_target': "Ngelahin kaca sadurung tujuwan",
        'progress_moving_pages': "Ngingsirang {0} kaca",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_kaamannang_",
        'filename_copy_suffix': "_salinan",
        'filename_page_single': "_kaca_",
        'filename_page_range': "_kaca_",
        'filename_export_page': "_Kaca_{0:03}",
        'filename_export_range': "_Kaca_{0}-{1}",
        'filename_export_multiple': "_Kaca_{0}",
        'filename_with_text': "_antuk_Teks",
        'filename_with_signature': "_antuk_TandaTangan",
        'filename_with_image': "_antuk_Gambar",
        'filename_with_forms': "_antuk_Wangun",
        # ---------------------------------------------------------
        'filename_timestamp_format': "%Y%m%d_%H%M%S",
        'filename_timestamp_micro': "%Y%m%d_%H%M%S_%f",

        # ============================================
        # 56. ANSICHT – BUTTONLEISTE EIN-/AUSBLENDEN
        # ============================================
        'view_toggle_navbar': "Témbongang bar tombol",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Tusing bisa ngapus makejang kaca",
		'pages_cannot_delete_last_page': 'Kaca pungkasan tusing bisa kaapus!',
		'pages_cannot_delete_all_pages': 'Akeh kaca ané musti ada abesik di dokumen!',
		'delete_pages_confirm': 'Yakin jema ngapus {0} kaca?',
		'delete_pages_confirm_voice': 'Yakin jema ngapus {0} kaca?',
		'pages_deleted': '{0} kaca sampun kaapus.',
		'warning': 'Penginget',
		'error': 'Pikobet',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nénten wentené",
        'form_customized': "Arancangan kaatur",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Pilih",
        'btn_use': "Anggen",
        'master_password_for_spasswords': "Miangkeb miwah nganggen kruna sandi, mangkin patut nyetel kruna sandi utama dumun.\n\nNapikang jagi nyetel kruna sandi utama mangkin?",
        'open_saved_dialog_title': "Buka berkas kaarsipang",
        'open_saved_question': "Napikang jagi mbuka berkas kaarsipang mangkin?",
        'password': "Kruna sandi",
        'password_manager_master_required': "Manajer kruna sandi wantah kasedia yening sampun nyetel kruna sandi utama.\n\nNapikang jagi nyetel kruna sandi utama mangkin?",
        'password_master_required_for_select': "Sane mangda prasida nyingak miwah milih kruna sandi kaarsipang, ragane patut mapamit sareng kruna sandi utama dumun.\n\nNapikang jagi mapamit mangkin?",
        'password_not_available': "Kruna sandi kapilih nenten kasedia utawi nenten prasida kadekskripsi.",
        'password_options_title': "Pilihan kruna sandi",
        'password_save_choice_change': "Setel kruna sandi anyar",
        'password_save_choice_keep': "Anggen kruna sandi sane wenten",
        'password_save_choice_none': "Arsipang tan pawatesan",
        'password_save_hint': "Setyel dumun kruna sandi utama mangda aman nyimpen kruna sandi.",
        'password_save_master_required': "Arsipang kruna sandi (wantah sareng kruna sandi utama)",
        'password_save_question': "PDF mangkin kaampehin kruna sandi. Napikang jagi nganggen kruna sandi sane wenten, nyetel kruna sandi anyar utawi nyimpen tan pawatesan?",
        'password_select': "Pilih kruna sandi",
        'password_select_none': "Tan wenten kruna sandi kapilih.\n\nRagané patut milih kruna sandi saking lis punika.",
        'password_select_one': "Ragané patut milih tepat asiki kruna sandi.\n\nRagané sampun namtosin makudang kruna sandi.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_cadangan",
        'filename_insert_suffix': "_sareng_pangeling",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_kaca_kaapus",
        'filename_pages_moved': "_kaca_kaalihang",
        'filename_rotated_all_suffix': "_kabeh_kaca_kaputer",
        'filename_rotated_suffix': "_kaca_kaputer",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurasi aran berkas ritatkala ngubah PDF",
        'filename_keep_suffixes': "Sisipin ekstensi sadurunge (contone _sareng_teks)",
        'filename_keep_suffixes_false': "Gentos",
        'filename_keep_suffixes_true': "Sisipin",
        'filename_preview_label': "Pratinjau aran berkas:",
        'filename_preview_overwrite_hint': "Pratinjau nenten kasedia – asli pacang katimpa.",
        'filename_separator': "Pamisah pantaraning kruna",
        'filename_separator_none': "Tan pamisah",
        'filename_separator_space': "Spasi ( )",
        'filename_separator_underscore': "Garis sor (_)",
        'filename_settings_saved': "Setelan aran berkas kaarsipang",
        'filename_settings_title': "Format aran berkas & cadangan",
        'filename_timestamp_position': "Genah cap waktu",
        'filename_timestamp_position_after': "Sesampuning aran dasar",
        'filename_timestamp_position_before': "Paling ajeng",
        'filename_timestamp_position_end': "Ring pungkuran",
        'filename_use_timestamp': "Anggen cap waktu",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Parilaksana ritatkala ngubah:</b><ul><li>Ngapus miwah nambakin kaca</li><li>Nambakin teks, tanda tangan, gambar miwah wangun</li><li>OCR</li></ul></html>",
        'backup_section': "Cadangan antuk operasi kaca (Ngapus, Alihang)",
        'behavior_info': "Pangeling: Ritatkala 'Timpa asli', cap waktu miwah sisipan kasiyaang – aran berkas tetep.",
        'behavior_new_file': "Sane ngeran anyar berkas (antuk cap waktu miwah sisipan)",
        'behavior_overwrite': "Timpa asli (tan wenten berkas anyar)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Kabeh kaca sampun kaputer.\n\nAsli tetep nenten kauwah.\nBerkas anyar: {0}",
        'all_pages_rotated_voice': "Kabeh kaca kaputer, berkas anyar karipta.",
        'empty_pages_deleted_new_file': "{0} kaca kosong sampun kaapus.\n\nAsli tetep nenten kauwah.\nBerkas anyar: {1}",
        'empty_pages_deleted_voice': "{0} kaca kosong kaapus, berkas anyar karipta.",
        'ocr_keep_original': "Sisipin asli (enggalang buka manual)",
        'ocr_new_file_question': "PDF anyar sane prasida karereh kaarsipang ring:\n{0}\n\nNapikang jagi nguncarang mangkin?",
        'ocr_open_new': "Buka berkas OCR anyar",
        'ocr_original_kept': "Berkas asli tetep buka. Berkas OCR sampun kaarsipang.",
        'page_deleted_new_file': "Kaca {0} sampun kaapus.\n\nAsli tetep nenten kauwah.\nBerkas anyar: {1}",
        'page_deleted_voice': "Kaca {0} kaapus, berkas anyar karipta.",
        'page_rotated_new_file': "Kaca {0} sampun kaputer.\n\nAsli tetep nenten kauwah.\nBerkas anyar: {1}",
        'page_rotated_voice': "Kaca {0} kaputer, berkas anyar karipta.",
        'pages_deleted_new_file': "Wenten {0} kaca kaapus.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar: {1}",
        'pages_deleted_new_file_voice': "{0} kaca kaapus, berkas anyar karipta.",
        'pages_inserted_new_file': "Wenten {0} kaca katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar: {1}",
        'pages_inserted_new_file_ask': "Wenten {0} kaca katambahang.\n\nAsli tetep nenten kauwah.\nBerkas anyar: {1}\n\nNapikang jagi nguncarang mangkin?",
        'pages_inserted_voice_new': "{0} kaca katambahang, berkas anyar karipta.",
        'pages_moved_new_file': "Wenten {0} kaca kaalihang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar: {1}",
        'pages_moved_new_file_voice': "{0} kaca kaalihang, berkas anyar karipta.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Sampunang tunjuk malih",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Setelan cadangan</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Cadangan NYALA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Ring samian owahan sane nimpa asli</strong> (teks, tanda tangan, gambar, wangun, OCR, puter, tambahang, apus/alihang kaca) jagi <strong>otomatis karipta cadangan antuk cap waktu</strong> sadurung owahan katerapang.</p>
                <p style="margin: 5px 0 5px 20px;">• Cadangan wenten ring sampingan berkas asli (contone <code>Dokument_cadangan_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Yening ragane taler ngaktipang pilihan <strong>„Timpa asli“</strong>, taler jagi karipta cadangan.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Cadangan MATI</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Nenten wenten cadangan</strong> karipta – nenten ritatkala nimpa miwah ritatkala operasi kaca.</p>
                <p style="margin: 5px 0 5px 20px;">• Berkas asli prasida ical tan prasida kaulihang rikala katimpa.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Wantah kaicayang antuk panganggih sane sampun pengalaman!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Timpal:</strong> Setelan cadangan nenten kakait sareng pilihan "Timpa asli". Ragané prasida nyarengin kekalih.<br>
                Ragané prasida nyumunin pesan puniki manut.
            </div>
        </div>
        """,
        'backup_info_title': "Parilaksana cadangan",
        'backup_info_voice': "Pangaweruh indik parilaksana cadangan ring operasi kaca. Cadangan nyala nimpa asli, cadangan mati nyiptayang berkas anyar.",
        'show_backup_info': "Info indik setelan cadangan",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Sampunang tunjuk malih",
        'overwrite_enable_backup': "Aktipang cadangan (kaicayang)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Timpa asli</p>
            <p>Yening ragane ngaktipang pilihan puniki, owahan (teks, tanda tangan, gambar, wangun, OCR, puter, tambahang) jagi <strong>karsipang langsung ring asli</strong> – <strong>nenten wenten berkas anyar</strong> karipta.</p>
            <p>• Aran berkas tetep nenten mauwah.<br>
            • Cap waktu miwah sisipan kasiyaang.<br>
            • <strong>Tanpa cadangan, asli prasida ical tan prasida kaulihang.</strong></p>
            <p style="color: #FFD700;">Pangiring: Aktipang taler pilihan cadangan mangda polih cadangan otomatis.</p>
        </div>
        """,
        'overwrite_info_title': "Timpa asli",
        'overwrite_info_voice': "Awas: Timpa asli – nenten wenten berkas anyar. Cadangan kaicayang.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Wenten {0} kaca katambahang.\n\nBerkas asli katimpa.\nCadangan sampun karipta.",
        'pages_inserted_overwrite_no_backup': "Wenten {0} kaca katambahang.\n\nBerkas asli katimpa.\nNenten wenten cadangan karipta.",
        'texts_saved_overwrite_with_backup': "Owahan sampun kaarsipang ring asli.\n\nCadangan sampun karipta.",
        'texts_saved_overwrite_no_backup': "Owahan sampun kaarsipang ring asli.\n\nNenten wenten cadangan karipta.",
        'texts_crosses_saved_new_file': "{0} {1} miwah {2} {3} sampun katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar sampun karipta.\n\nPDF anyar pinih kamuat...",
        'texts_saved_new_file': "{0} {1} sampun katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar sampun karipta.\n\nPDF anyar pinih kamuat...",
        'crosses_saved_new_file': "{0} {1} sampun katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar sampun karipta.\n\nPDF anyar pinih kamuat...",
        'elements_saved_new_file': "{0} unsur sampun katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar sampun karipta.\n\nPDF anyar pinih kamuat...",
        'signatures_saved_overwrite_with_backup': "Tanda tangan sampun kaarsipang ring asli.\n\nCadangan sampun karipta.",
        'signatures_saved_overwrite_no_backup': "Tanda tangan sampun kaarsipang ring asli.\n\nNenten wenten cadangan karipta.",
        'images_saved_overwrite_with_backup': "Gambar sampun kaarsipang ring asli.\n\nCadangan sampun karipta.",
        'images_saved_overwrite_no_backup': "Gambar sampun kaarsipang ring asli.\n\nNenten wenten cadangan karipta.",
        'forms_saved_overwrite_with_backup': "Wangun sampun kaarsipang ring asli.\n\nCadangan sampun karipta.",
        'forms_saved_overwrite_no_backup': "Wangun sampun kaarsipang ring asli.\n\nNenten wenten cadangan karipta.",
        'signatures_saved_new_file': "{0} tanda tangan sampun katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar sampun karipta.\n\nPDF anyar pinih kamuat...",
        'images_saved_new_file': "{0} gambar sampun katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar sampun karipta.\n\nPDF anyar pinih kamuat...",
        'forms_saved_new_file': "{0} wangun sampun katambahang.\n\nBerkas asli tetep nenten kauwah.\nBerkas anyar sampun karipta.\n\nPDF anyar pinih kamuat...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Awas: PDF puniki madaging kaca kaputer. Genahnyane prasida mabinayan.",
        'page_rotated_warning_title': "Kaca kaputer kacumpu",
        'page_rotated_warning_message': "Kaca mangkin {0} kaputer {1}°.\n\nNambakin unsur ring kaca kaputer nenten kadiukung.\n\nNapikang jagi muter kaca mangkin nuju genah tegak?",
        'page_rotated_warning_voice': "Awas: Kaca kaputer. Ragané patut muter dumun.",
        'paste_on_rotated_page_simple_warning': "Nambakin ring kaca {0} tan prasida!\n\nKaca puniki kaputer {1}°.\n\nRagané patut muter kaca dumun nuju 0° (Menu: Uah → Ajakin kaca tegak).\n\nAwas:\nUnsur sane sampun kasalin pacang ical yening ragané nenten nyimpen sadurung muter kaca.",
        'paste_on_rotated_page_voice': "Nambakin kapesan. Kaca kaputer. Ragané patut ajakin kaca tegak dumun.",
        'page_rotated_cancel': "Pesang",
        'page_rotated_rotate_until_upright': "Muter kaca makejang (ngantos tegak)",
        'page_rotated_now_upright': "Kaca mangkin tegak. Ragané prasida nambakin mangkin.",
        'page_rotated_still_not_upright': "Kaca nenten prasida kamuter nuju tegak. Ragané patut ngajakin manual.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Pitulung: Ngajakin kaca kaputer",
        'help_rotated_pages_voice': "Pitulung antuk ngajakin kaca kaputer jagi kabuka.",
        'btn_help': "Pitulung",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Pikobet: Kaca kaputer – Nambakin nenten becik</p>

            <p>Yening nambakin teks, tanda tangan, utawi wangun ring kaca kaputer nenten becik, ragané prasida ngajakin kaca antuk pangalih PDF eksternal.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solusi antuk piranti eksternal (contoné macOS Pratinjau)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Ekspor kaca</strong><br>
                &nbsp;&nbsp;Klik ring menu <strong>Berkas → Ekspor dados kaca</strong> utawi anggén metode tiosan antuk nyimpen kaca sane karesidayang dados PDF tunggal.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Buka kaca ring program eksternal</strong><br>
                &nbsp;&nbsp;Buka PDF sane kaekspor ring pangalih PDF (contoné <strong>macOS Pratinjau</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Puter kaca</strong><br>
                &nbsp;&nbsp;Puter kaca ngantos tegak (ring Pratinjau: <strong>Piranti → Puter</strong> utawi <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Simpen</strong><br>
                &nbsp;&nbsp;Simpen kaca sane sampun kawedar (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Tambahim malih kaca ring dokumen asli</strong><br>
                &nbsp;&nbsp;Walik mangkin ka PDFDarkView miwah tambahang kaca sane sampun kawedar ring genah sane karesidayang:<br>
                &nbsp;&nbsp;<strong>Uah → Tambahang kaca</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatif: Puter kaca ring asli</p>
                <p style="margin: 5px 0 5px 20px;">• Anggen fungsi puter sane sampun wenten (<strong>Uah → Puter kaca</strong>) antuk ngajakin kaca sacara bertahap.<br>
                • Sasampun nyetiap puteran, ragané prasida mriksa napi nambakin mangkin becik.<br>
                • Puniki sering solusi sane gelis – coba dumun!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Timpal:</strong> Yening ragané sering nemu kaca kaputer, ragané prasida nyumunin pangeling ring dialog nambakin manut.<br>
                Genahnyane prasida mabinayan – anggén pilihan puniki wantah yening ragané uning indik akibatnyane.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Ajakin kaca",
        'menu_rotate_normalize_tooltip': "Puter kaca utawi reset nuju 0°",
        'normalize_current_page': "Bakta kaca mangkin nuju genah tegak (setel nuju 0°)",
        'normalize_all_pages': "Bakta kabeh kaca nuju genah tegak (setel nuju 0°)",
        'page_normalized': "Kaca {0} sampun kasetel nuju genah tegak.",
        'all_pages_normalized': "Kabeh kaca sampun kasetel nuju genah tegak.",
        'page_already_upright': "Kaca {0} sampun tegak.",
        'all_pages_already_upright': "Kabeh kaca sampun tegak.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF nenten madaging teks sane prasida karereh.</p><p>Napikang jagi ngelaksanayang OCR antuk ngekspor nuju {0}?</p>",
        'export_ocr_voice': "PDF nenten madaging teks. OCR kaperluang antuk ekspor nuju {0}.",
        'export_no_ocr_possible': "Ekspor tanpa OCR nenten prasida. Ragané patut ngelaksanayang OCR liwat menu.",
        'ocr_failed_export_not_possible': "OCR gagal. Ekspor nenten prasida kalaksanayang.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF jagi kabuka ring Pratinjau. Ragané patut ngawitin proses nyetak irika.",
        'print_preview_manual': "PDF sampun kabuka. Ragané patut ngelaksanayang parentah nyetak sacara manual (contone Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Gabungang PDF",
        'merge_pdfs': "Gabungang PDF",
        'merge_progress_title': "PDF kagabungang...",
        'merge_pdfs_list': "PDF manut urutan (Sered miwah lepas mangda urutang)",
        'merge_add_pdf': "Tambahang PDF",
        'merge_remove': "Pesang",
        'merge_move_up': "Mengkab",
        'merge_move_down': "Mebeten",
        'merge_pdfs_info': "💡 Timpal: Ragané prasida ngubah urutan antuk sered miwah lepas",
        'merge_no_pdfs': "Tan wenten PDF kapilih. Klik ring 'Tambahang PDF'.",
        'merge_info': "{0} PDF kapilih (kintamangun {1} kaca)",
        'merge_open_file': "Buka berkas",
        'merge_merge': "Gabungang",
        'merge_error': "Pikobet ritatkala ngagabungang",
        'merge_min_two_pdfs_error': "Ragané patut milih saper kalih berkas PDF antuk kagabungang.",
        'merge_select_pdfs': "Pilih PDF antuk kagabungang",
        'merge_error_file': "Pikobet ritatkala ngolah",
        'merge_cancelled': "Ngagabungang kapesan",
        'merge_preparing': "Nyaga...",
        'merge_processing': "Ngolah PDF {0} saking {1}",
        'merge_saving': "Nyimpen PDF kagabungang...",
        'merge_complete': "Puput!",
        'merge_success_title': "Ngagabungang sukses",
        'merge_success_voice': "Wenten {0} PDF sukses kagabungang.",
        'merge_success_message': "Wenten {0} PDF sukses kagabungang.\n\nDokumen anyar mangkin madaging {1} kaca.\n\nBerkas anyar:\n{2}\n\nGenah nyimpen:\n{3}\n{2}\n\nNapikang jagi nguncarang PDF puniki?",
        'replace_file_title': "Gentos berkas?",
        'replace_file_message': "Wenten PDF sampun kabuka. Napikang jagi nggentos antuk berkas anyar?",
        'btn_yes': "Inggih",
        'btn_no': "Nenten",
        'filename_merge_suffix': "kagabungang",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Ngabuka {0}...",
        'progress_merge_reading': "Maca {0}...",
        'progress_merge_adding': "Nambahim {0} kaca...",
        'progress_merge_optimizing': "Ngoptimal PDF...",
        'progress_merge_writing': "Nulis PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "nutup PDF",
        'action_close_window': "nutup jendela",
        'action_open_new_pdf': "ngabuka PDF anyar",
        'action_quit_app': "mengelonin aplikasi",
        'changes_saved': "Owahan sampun kaarsipang.",
        'file_close_title': "Tutup berkas PDF",
        'save_before_action': "Napikang owahan patut kaarsipang sadurung {0}? Inggih utawi Nenten?",
        'save_before_action_voice': "Napikang owahan patut kaarsipang sadurung {0}? Inggih utawi Nenten?",
        'save_before_close_question': "Napikang owahan patut kaarsipang sadurung nutup? Inggih utawi Nenten?",

         # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF sané prasida karereh kawentuk:\n\n{0}\n\n<b>coba malih yening perlu",
        "ocr_rotate_title": "Uahin kaca sadurung OCR",
        "ocr_rotate_question": "PDF puniki madaging kaca sané kapepet.\nNapiké ragané jagi ngubah samian kaca ka 0° sadurung OCR?\nNiki ngicénin peningkatan pangakéhan teks sané signifikan.",
        "ocr_rotate_yes": "Inggih, uahin",
        "ocr_rotate_no": "Nenten, langsung ngawitin OCR",
        "ocr_rotate_voice": "PDF puniki madaging kaca sané kapepet. Apakah samian kaca patut kauahin sadurung OCR?",
        "ocr_not_performed_message": "Nénten wénten teks. Dasarang OCR (Menu \"Uah\" → \"Dasarang OCR\" utawi kenop Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Setélan OCR",
        "ocr_language_btn": "Pilih basa OCR",
        "ocr_language": "Basa OCR",
        "ocr_language_current": "Basa mangkin:",
        "ocr_param_info": "Inpormasi indik parameter",

        "ocr_force_ocr_label": "Paksa OCR",
        "ocr_deskew_label": "Koreksi miring",
        "ocr_clean_label": "Resikin gambar",
        "ocr_oversample_label": "Resolusi (DPI)",
        "ocr_pagesegmode_label": "Pawagian kaca",
        "ocr_oem_label": "Mode mesin OCR",
        "ocr_optimize_label": "Komprési PDF",
        "ocr_jobs_label": "Proses paralel",
        "ocr_verbose_label": "Detil log",

        "ocr_force_ocr_tooltip": "Paksa OCR ring soang-soang kaca, maski teks sampun wénten",
        "ocr_deskew_tooltip": "Uahin scan sané miring sacara otomatis",
        "ocr_clean_tooltip": "Ilangin bising miwah artefak saking gambar",
        "ocr_oversample_tooltip": "Besarin gambar sadurung OCR ka DPI puniki",
        "ocr_pagesegmode_tooltip": "Nemtuang cara kaca kawagi dados wewengkon teks",
        "ocr_oem_tooltip": "Milih mesin OCR saking Tesseract",
        "ocr_optimize_tooltip": "Tingkat komprési PDF keluaran",
        "ocr_jobs_tooltip": "Akéh proses OCR paralel",
        "ocr_verbose_tooltip": "Tingkat detil luaran log",
        "ocr_settings_explain_btn": "Panjelasan",

        "ocr_force_ocr_explain": "Maksa pangakéhan teks ring soang-soang kaca, maski sampun madaging teks.\n\nRekomendasi: <b>Huripang</b> antuk PDF sané kascan, <b>Pademang</b> antuk PDF asli sané sampun madaging teks.",

        "ocr_deskew_explain": "Ngicénin koreksi antuk scan sané rada miring (tekan 5°).\n\nRekomendasi: <b>Huripang</b> antuk dokumén sané kascan, <b>Pademang</b> yening kaca sampun lurus sampurna.",

        "ocr_clean_explain": "Ngicalang bising, titik-titik, miwah artefak alit saking gambar.\n<b>PENTING:</b> Antuk teks Arab, Thailand, utawi Vietnam sané madaging tanda diakritik (titik ring duur/kebawah aksara) opsén puniki patut <b>kapademang</b> santukan punika prasida ngicalang karakter sané penting.",

        "ocr_oversample_explain": "Besarin gambar <b>sadurung</b> pangakéhan teks ka DPI sané kacawisang.<br><br>• <b>72-150 DPI:</b> Cepet pisan, nanging tingkat pangakéhan éndép<br>• <b>200-300 DPI:</b> Wewengkon optimal (Standar: 300)<br>• <b>400+ DPI:</b> Pangakéhan sané kirang ja lédang, nanging berkas sané lantang pisan<br><br>Rekomendasi: 300 DPI antuk aksara kompleks (Arab, Cina, Jepang), 200 DPI antuk basa Kauh.",

        "ocr_pagesegmode_explain": "Nemtuang cara Tesseract ngewagi kaca dados wewengkon teks.\n\n• <b>3 - Otomatis (Standar):</b> Becik antuk tata letak campuhan\n• <b>4 - Kolom tunggal:</b> Antuk teks kolom tunggal\n• <b>5 - Blok vertikal:</b> Antuk aksara vertikal (Jepang, Cina)\n• <b>6 - Blok teks seragam:</b> Optimal antuk teks aliran tanpa kolom\n• <b>11 - Gambar kasar:</b> Antuk scan sané jelek / tulisan tangan\n\nRekomendasi: <b>6</b> antuk dokumén teks sederhana, <b>3</b> antuk tata letak kompleks.",

        "ocr_oem_explain": "Milih mesin OCR saking Tesseract.\n\n• <b>0 - Legacy:</b> Mesin lawas (cepet, nanging kirang akurat)\n• <b>1 - LSTM:</b> Mesin neural (lambat, nanging lédang akurat)\n• <b>2 - Legacy + LSTM:</b> Ngagabungang asil makakalih\n• <b>3 - Standar (LSTM kaanggen preferensi):</b> Pilihan pinih becik antuk makéhan kasus\n\nRekomendasi: <b>3</b> antuk akurasi pangakéhan maksimal.",

        "ocr_optimize_explain": "Ngakomprés PDF keluaran.\n\n• <b>0:</b> Tanpa optimalisasi (pangolahan pinih cepet)\n• <b>1:</b> Optimalisasi alit (kompromi sané becik)\n• <b>2:</b> Optimalisasi sedeng\n• <b>3:</b> Optimalisasi kuat (berkas pinih alit, nanging lambat)\n\nRekomendasi: <b>1</b> antuk anggén sapopoe.",

        "ocr_jobs_explain": "Akéh proses paralel antuk OCR.\n\n• <b>1:</b> Lambat, nanging panganggén memori pinih éndép\n• <b>4-8:</b> Optimal antuk prosesor multi-inti modern\n• <b>12+:</b> Pangolahan sané kirang ja cepet ring panganggén memori sané tegeh\n\nRekomendasi: Akéh inti CPU (minakadi <b>4</b> ring sistem 4-inti).",

        "ocr_verbose_explain": "Tingkat detil luaran log ring konsol.\n\n• <b>0:</b> Tanpa luaran\n• <b>1:</b> Kamajuan miwah parindikan status\n• <b>2:</b> Luaran detil\n• <b>3:</b> Luaran debug pangkep (luwih ageng pisan)\n\nRekomendasi: <b>1</b> antuk operasi normal.",

        "ocr_reset_title": "Setélan kawalikang",
        "ocr_reset_message": "Samian setélan OCR sampun kawalikang ka nilai standar.",
        "info_tooltip": "Inpormasi luwih akéh indik parameter puniki",
        "ocr_reset_defaults": "Walikang ka standar",

        "ocr_psm_0": "Otomatis (Mesin Legacy)",
        "ocr_psm_1": "Deteksi kolom otomatis",
        "ocr_psm_3": "Otomatis (Standar)",
        "ocr_psm_4": "Kolom tunggal",
        "ocr_psm_5": "Blok vertikal",
        "ocr_psm_6": "Blok teks seragam",
        "ocr_psm_7": "Baris teks tunggal",
        "ocr_psm_8": "Kruna tunggal",
        "ocr_psm_11": "Gambar kasar (tanpa analisis tata letak)",

        "ocr_oem_0": "Mesin Legacy (cepet)",
        "ocr_oem_1": "Mesin LSTM (neural, akurat)",
        "ocr_oem_2": "Legacy + LSTM kakombinasiang",
        "ocr_oem_3": "Standar (LSTM kaanggen preferensi)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Basa OCR...",
        "ocr_language_title": "Pilih basa OCR",
        "ocr_language_instruction": "Pilih basa antuk pangakéhan teks (OCR).\nPikobet: Makudang basa pacang ngawinang tuun kinerja miwah akurasi!\nRagané jagi molihang asil pinih becik yening milih wantah asiki basa.",
        "ocr_language_predefined": "Kombinasi sané sampun katetapang",
        "ocr_language_custom": "Tentuang padidi...",
        "ocr_language_selected": "Basa OCR kapilih",
        "ocr_language_changed": "Basa OCR kagingsirang ka {0}",
        "ocr_language_auto_detect": "Basa sané wénten karereh sacara otomatis.",
        "ocr_language_none_found": "Data basa Tesseract tan katemu! Dasarang pakét basa (minakadi 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Pilihan basa tentuang padidi",
        "ocr_language_available": "Basa sané wénten (kainstal):",
        "ocr_language_select_hint": "Pilih asiki utawi makudang basa:",
        "ocr_language_confirm": "Terapang",
        "ocr_language_reset": "Walikang ka standar (deu+eng+vie)",
        "ocr_language_priorities": "Basa sané karekomendasiang (sampun kainstal):",

        "select_all_languages": "Pilih samian",
        "clear_all_languages": "Bersihang pilihan",
        "install_language_packs": "Instal pakét basa sané kirang...",
        "install_hint": "💡 Tip: Nénten samian basa kainstal ring sistem ragané. Saking tombol puniki ragané jagi molihang pituduh antuk instalasi.",
        "ocr_language_install_title": "Instalasi Pakét Basa Tesseract",

        "ocr_missing_languages": "Pakét basa OCR sané kirang",
        "ocr_missing_languages_message": "Basa-basa kapilih puniki kirang miwah nenten kainstal ring sistem ragané:\n\n{0}\n\nDasarang pakét basa sané kirang (cingak pituduh ring 'Pituduh Instalasi').\n\nNapiké ragané jagi ngabuka Pituduh Instalasi mangkin?",
        "ocr_missing_languages_voice": "Pakét basa kirang. Dasarang basa-basa sané kirang.",
        "ocr_install_help_now": "Bukak pituduh",
        "ocr_continue_anyway": "Coba tusing dadi",  # Note: "nonetheless"
        "ocr_language_error_title": "Galat basa OCR",
        "ocr_language_error_message": "Galat ring pangakéhan teks: {0}\n\nPeriksa setélan basa OCR ragané (Setélan → Basa OCR).",
        "ocr_install_help_button": "Pituduh instalasi",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instal Pakét Basa Tesseract</p>

        <p>Supados OCR prasida mlaku ring basa tarténtu, data basa sané cocok patut kainstal ring sistem ragané. Tuturin pituduh antuk sistem operasi ragané:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Bukak <strong>Terminal</strong> (Finder → Aplikasi → Utilitas → Terminal).</li>
        <li>Instal samian basa sané wénten nganggén:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Punika prasida wantau makudang minit.)</li>
        <li>Utawi wantah basa perorangan (minakadi Vietnam):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Ring versi Homebrew mangkin, <code>*.traineddata</code> patut kauhanduh sacara manual (cingak ring sor).</li>
        <li>Sawusan instalasi: Tutup dialog puniki miwah bukak malih pilihan basa OCR – basa anyar pacang rauh otomatis.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Bukak terminal (Ctrl+Alt+T).</li>
        <li>Instal basa sané kayunin, minakadi antuk Vietnam:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Kode basa sané penting: <code>deu</code> (Jerman), <code>eng</code> (Inggris), <code>vie</code> (Vietnam), <code>spa</code> (Spanyol), <code>fra</code> (Prancis), <code>ita</code> (Italia), <code>nld</code> (Belanda), <code>fin</code> (Finlandia), <code>swe</code> (Swedia), <code>nor</code> (Norwegia).</li>
        <li>Tonton samian pakét sané wénten:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Unduh berkas <code>*.traineddata</code> sané kayunin saking:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (minakadi <code>vie.traineddata</code> antuk Vietnam).</li>
        <li>Salin berkas-berkas punika ka folder basa Tesseract, ketahnyané:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Sesuaikan yening instalasi ten standar.)</li>
        <li>Start malih aplikasi (utawi bukak malih pilihan basa OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatif antuk samian sistem</p>
        <ul>
        <li>Instal <strong>OCRmyPDF</strong> miwah <strong>Tesseract</strong> nganggén manajer pakét pilihan ragané. Makéhan instalasi sampun ngisi makudang basa standar (Inggris, Jerman, Prancis).</li>
        <li>Basa sané kirang prasida kainstal sairasa – pilihan basa OCR wantah nglaris basa sané sampun wénten.</li>
        </ul>

        <hr>
        <p><b>✅ Sawusan instalasi:</b> Nénten perlu start malih aplikasi – basa-basa anyar pacang rauh langsung ring lis.</p>
        <p><b>📖 Pituduh indik kode basa:</b> Lis pangkep wénten ring <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Dokumentasi Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Aksara Noto Sans",
        "info_noto_font_voice": "Pituduh instalasi aksara Noto Sans",
        "btn_info_noto_font_install": "Info Aksara",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Cara milu masang aksara Noto gratis saking Google</h2>

        <p><strong>Aksara Noto</strong> inggih punika kulawarga aksara sumber kabuka saking Google. Tujuannyané inggih punika mangda ten pasti ngaksi <em>"ten wénten tahu"</em> (artosnyané ten wénten kotak kosong □) miwah terangang soang-soang karakter saking standar Unicode antuk patut. Puniki inggih punika tambahan becik antuk aplikasi sané patut nayanggang teks ring makudang basa.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalasi ring macOS</h3>

        <p><strong>Cara 1: Nganggén Homebrew (antuk sané sampun lédang)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Cara 2: Nganggén "Font Book" (Rekomendasi)</strong></p>

        <ol>
        <li>Unduh pakét aksara resmi:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ekstrak berkas ZIP</li>
        <li>Salin berkas-berkas ka <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalasi ring Windows (10 & 11)</h3>

        <p><strong>Cara 1: Microsoft Store (Rekomendasi)</strong><br>
        Rereh "Google Noto Fonts" utawi "Noto Sans" tur klik <strong>Instal</strong>.</p>

        <p><strong>Cara 2: Instalasi manual</strong></p>

        <ol>
        <li>Unduh:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ekstrak ZIP</li>
        <li>Pilih berkas .ttf / .otf</li>
        <li>Klik kanan → <strong>Instal</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        utawi<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Name\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalasi ring Linux</h3>

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
        "bookmark_dialog_title": "Atur tandai",
        "bookmark_add": "Wewehin tandai",
        "bookmark_add_tooltip": "Simpen kaca mangkin dados tandai",
        "bookmark_remove": "Ilangin tandai",
        "bookmark_remove_tooltip": "Hapus tandai sané katandai",
        "bookmark_remove_all": "Ilangin samian",
        "bookmark_remove_all_tooltip": "Hapus samian tandai saking PDF puniki",
        "bookmark_jump": "Loncat ka tandai",
        "bookmark_jump_tooltip": "Loncat ka kaca kapilih",
        "bookmark_name": "Adan",
        "bookmark_page": "Kaca",
        "bookmark_no_bookmarks": "Nénten wénten tandai.\nKlik 'Wewehin' antuk nyimpen kaca mangkin dados tandai.",
        "bookmark_added": "Tandai antuk kaca {0} kawewehin: {1}",
        "bookmark_removed": "Tandai kailangin: {0}",
        "bookmark_all_removed": "Samian tandai sampun kailangin.",
        "bookmark_name_default": "Kaca {0}",
        "bookmark_name_prompt": "Adan antuk tandai:\n(teks lantang pacang kasiagang nganti 50 karakter)",
        "bookmark_name_prompt_title": "Adan tandai",
        "bookmark_confirm_remove_all": "Napiké ragané yakin jagi ngilangin samian tandai {0}?",
        "menu_bookmarks": "Tandai",
        "bookmark_manage": "Atur tandai",
        "bookmark_next": "Tandai salanturnyané",
        "bookmark_prev": "Tandai sadurungnyané",
        "bookmark_page_display": "Kaca {0}",
        "bookmark_exists": "Tandai antuk kaca puniki mawastanin punika sampun wénten.",
        "bookmark_select_first": "Pilih tandai dumun.",
        "bookmark_confirm_remove": "Napiké ragané yakin jagi ngilangin tandai 'Kaca {0}: {1}'?",
        "bookmark_jumped_to": "Loncat ka tandai '{0}' ring kaca {1}.",
        "bookmark_jumped_to_voice": "Tandai {0}, kaca {1}",
        "btn_close": "Tutup",

        "bookmark_list": "Tandai ragané",
        "bookmark_rename": "Ganti wasta tandai",
        "bookmark_rename_tooltip": "Ubah wasta tandai sané kapilih",
        "bookmark_rename_title": "Ganti wasta tandai",
        "bookmark_rename_prompt": "Wasta anyar antuk tandai ring kaca {0}:\n(maksimal 50 karakter)",
        "bookmark_renamed": "Tandai '{0}' kaganti wasta dados '{1}'.",
        "bookmark_item_tooltip": "Kaca {0}: {1}\nKlik kaping kalih antuk loncat",
        "bookmark_name_exists_question": "Wénten tandai mawasta '{0}' sampun wénten ring kaca puniki.\nGanti wasta tusing dadi?",

        "context_bookmarks": "Tandai",
        "context_bookmark_add_here": "Wewehin tandai antuk kaca puniki",
        "context_bookmarks_existing": "Tandai sané wénten:",
        "context_bookmarks_jump": "Loncat ka tandai:",
        "context_bookmarks_none": "Nénten wénten tandai",
        "context_bookmarks_clear_all": "Ilangin samian tandai {0}",

        "bookmark_search_placeholder": "Rereh tandai... (adan utawi kaca)",
        "bookmark_search_results": "%d tandai katemu antuk \"%s\"",
        "bookmark_no_search_results": "Tan wénten tandai katemu antuk \"%s\"",
        "bookmark_no_search_results_label": "Tan wénten asil antuk \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Uah metadata PDF",
        "metadata_title": "Murda",
        "metadata_title_placeholder": "Murda dokumén",
        "metadata_title_tooltip": "Murda dokumén (cetak ring bar murda)",
        "metadata_author": "Pangawi",
        "metadata_author_placeholder": "Adan pangawi",
        "metadata_author_tooltip": "Sang pangripta dokumén",
        "metadata_subject": "Jejer",
        "metadata_subject_placeholder": "Jejer dokumén",
        "metadata_subject_tooltip": "Pidarta cutet indik isi",
        "metadata_keywords": "Krunci",
        "metadata_keywords_placeholder": "Krunci, kapisah antuk koma",
        "metadata_keywords_tooltip": "Krunci antuk ngategoriang dokumén",
        "metadata_creator": "Pangripta",
        "metadata_creator_placeholder": "Aplikasi sané ngripta PDF",
        "metadata_creator_tooltip": "Perangkat lunak sané nganggén ngripta dokumén",
        "metadata_producer": "Produsen",
        "metadata_producer_placeholder": "Aplikasi sané ngonversi PDF",
        "metadata_producer_tooltip": "Perangkat lunak sané ngonversi PDF",
        "metadata_creation_date": "Tanggal karipta",
        "metadata_creation_date_tooltip": "Tanggal dokumén karipta",
        "metadata_mod_date": "Tanggal uahan",
        "metadata_mod_date_tooltip": "Tanggal uahan pinih untat",
        "metadata_pdf_info": "📄 Inpormasi PDF",
        "metadata_pages": "Akéh kaca",
        "metadata_file_size": "Ukuran berkas",
        "metadata_pdf_version": "Versi PDF",
        "metadata_encrypted": "Kaénkripsi",
        "metadata_encrypted_yes": "Inggih (kaprotéksi sareng kruna sandi)",
        "metadata_encrypted_no": "Nénten",
        "metadata_reload": "📂 Muat ulang saking PDF",
        "metadata_reset": "Buäng ubahan",
        "metadata_reloaded": "Metadata sampun kamuat ulang saking PDF.",
        "metadata_reset_done": "Samian kolom metadata sampun kawalikang.",
        "metadata_no_file": "Nénten wénten berkas PDF kamuat.",
        "metadata_save_error": "Galat nyimpen metadata",
        "metadata_saved": "Metadata sampun kasimpen antuk becik.",
        "metadata_pdf_version_unknown": "PDF (tan kauningin)",
        "metadata_saved_message": "Metadata sampun kasimpen antuk becik.",
        "metadata_saved_voice": "Metadata kasimpen.",

        "metadata_custom": "🔧 Metadata tentuang padidi",
        "metadata_custom_placeholder": "{\n  \"medan_titiang\": \"nilai_titiang\",\n  \"medan_liyanan\": 123\n}",
        "metadata_custom_tooltip": "Format JSON antuk metadata tentuang padidi (opsional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Templat \"{0}\" kapilih - Klik kaping kalih antuk nyisipang",
        "text_use_template": "Anggén blok teks",
        "text_type": "Tipe",
        "text_search_templates": "Rereh blok teks...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informasi Ékspor / Impor",
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

        <h3>📦 Apakah sané kaekspor? (Ringkesan)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Setélan aplikasi umum</span></li>
            <li class="detail">• Mode Peteng/Terang</li>
            <li class="detail">• Pabinayan gambar mode peteng</li>
            <li class="detail">• Nilai ambang abu</li>
            <li class="detail">• Basa</li>
            <li class="detail">• Géométri jendela</li>
            <li class="detail">• Mode Zum</li>
            <li class="detail">• Navigasi (Bar navigasi kacingak)</li>
            <li class="detail">• Luaran suara (nyala/padam)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Setélan cadangan</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Parinama berkas (Cap waktu, Pemisah, Akhiran)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Setélan antuk sisipan saking</span></li>
            <li class="detail">• Tanda tangan</li>
            <li class="detail">• Teks &amp; Blok teks</li>
            <li class="detail">• Cawang, gambar miwah wangun</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Setélan OCR</span></li>
            <li class="detail">• Basa</li>
            <li class="detail">• Paksa OCR · Mode kaca</li>
            <li class="detail">• Pamiarékan gambar sadurung: Lurusang, Resikin, Oversampling</li>
            <li class="detail">• Akéh proyék paralel</li>
            <li class="detail">• Mode pabinayan</li>
            <li class="detail">• Nilai ambang abu</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Tandai</span></li>
            <li class="detail">• Samian tandai per berkas PDF (Kaca, Adan, Waktu karipta)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Basis data kruna sandi</span></li>
            <li class="detail">• Kruna sandi PDF sané kasimpen (kaénkripsi utawi tèks biasa manut pilihan)</li>
            <li class="detail">• Hash kruna sandi induk (yening kasetel)</li>
            <li class="detail">• Data verifikasi</li>
        </ul>

        <h4>⚠️ Pikobet penting</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Ritatkala impor:</strong>
            <ul>
                <li><span class="warning">➜ Samian setélan sané wénten pacang kabales pangkep</span></li>
                <li>• Start malih aplikasi punika kawajibang</li>
                <li>• Tanda tangan, blok teks miwah tandai sané wénten pacang kagentos</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Kruna sandi induk &amp; Mode ékspor:</strong>
            <ul>
                <li>• Ritatkala kruna sandi induk aktif, ragané prasida milih:</li>
                <li>  - <span style="color: #98FB98;"><strong>Nyahang énkripsi</strong></span> (Kruna sandi wénten ring tèks biasa ring ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Kaénkripsi</strong></span> (Wantah prasida kawaca nganggén kruna sandi induk ring sistem tujuan)</li>
                <li>• Hash kruna sandi induk punika <strong>salawasnyá</strong> kasimpen ring énkripsi</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Pikobet kaamanan:</strong>
            <ul>
                <li>• Berkas ZIP sané kaekspor madaging data privasi (<strong>kruna sandi, tandai, tanda tangan</strong>)</li>
                <li>• Dasarang nyimpen antuk aman (minakadi USB énkripsi, manajer kruna sandi)</li>
                <li>• Yening berkas ical, kruna sandi PDF sané kasimpen pacang ical pisan tur nénten prasida kapulihang</li>
            </ul>
        </div>

        <h4>📁 Format ékspor</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Setélané kasimpen ring asiki berkas ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Berkas ZIP puniki madaging <code>settings.json</code> pangkep (saking konfigurasi ragané) taler kidung berkas gambar tanda tangan miwah kruna sandi kaénkripsi.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Tanda tangan - Panduan",
        'signature_guide_html': """
        📝 <strong>Tanda tangan - Panduan Singkat</strong><br>
        <ul>
        <li>Atur kruna sandi master</li>
        <li>Konfigurasi tanda tangan ring menu <em>Setélan</em> (ukuran, cap waktu, …)</li>
        <li>Selipang nganggen <strong>KLIK KIWA</strong> ring posisi sané kapingin (kruna sandi master apisan per sesi)</li>
        <li>Gingsirang tanda tangan nganggen mouse utawi ken jangka</li>
        <li>Selipang makudang tanda tangan sasih-sasih</li>
        <li>Sesuaikayang soang-soang tanda tangan</li>
        <li>Buang tanda tangan tunggal</li>
        <li>Simpen / buang sareng-sareng makasami tanda tangan</li>
        <li>Alternatif, bar menu taler prasida kaanggén.</li>
        </ul>
        """,
        'signature_guide_voice': "Panduan singkat tanda tangan. Atur kruna sandi master. Konfigurasi tanda tangan ring setélan. Selipang nganggen klik kiwa.",

        'image_guide_title': "Selipang gambar - Panduan",
        'image_guide_html': """
        📷 <strong>Selipang gambar ring PDF - Panduan Singkat</strong><br>
        <ol>
        <li>Klik kiwa ring posisi sané kapingin</li>
        <li><em>„Selipang gambar“</em> → Pilih gambar</li>
        <li>Tetuang posisi gambar: Seret nganggen mouse</li>
        <li>Ubah ukuran: Seret ring sisi/ujung</li>
        <li>Jaga rasio aspek: Teken <strong>[A]</strong></li>
        <li>Pangaturan lianan: Klik kiwa ring gambar</li>
        </ol>
        <p><strong>Saran:</strong> Ring menu konteks, Ida prasida nyesuaikayang setélan.</p>
        """,
        'image_guide_voice': "Panduan singkat gambar. Klik kiwa, selipang gambar, pilih. Tetuang posisi nganggen mouse, ubah ukuran ring sisi. Rasio aspek nganggen teken A.",

        'form_guide_title': "Selipang wangun - Panduan",
        'form_guide_html': """
        📐 <strong>Selipang wangun ring PDF - Panduan Singkat</strong><br>
        <ol>
        <li>Pilih tipe wangun (persegi panjang, elips, garis, panah)</li>
        <li>Klik ring posisi:
            <ul>
            <li>Antuk persegi panjang/elips: Akidik klik ngwangun wangun</li>
            <li>Antuk garis/panah: Kalih klik antuk titik awalan lan akhiran</li>
            </ul>
        </li>
        <li>Tetuang posisi wangun: Seret nganggen mouse</li>
        <li>Ubah ukuran: Seret ring sisi/ujung</li>
        <li>Simpen wangun: <strong>Enter</strong></li>
        <li>Buang wangun: <strong>ESC</strong></li>
        <li>Pangaturan lianan: Klik kiwa ring wangun</li>
        </ol>
        <p><strong>Saran:</strong> Ring menu konteks, Ida prasida nyesuaikayang setélan.</p>
        """,
        'form_guide_voice': "Panduan singkat wangun. Pilih tipe wangun. Antuk persegi panjang utawi elips klik apisan, antuk garis utawi panah klik kalih. Tetuang posisi nganggen mouse, ubah ukuran ring sisi. Simpen nganggen Enter, buang nganggen Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "sadurungnyane",
        "btn_next_result": "salanturnyane",
        "ocr_text_window": "Jendela teks OCR",
        "bookmark_existing": "Tétébékan sané wénten",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Perbandingan OCR Mac - Windows",
        'ocr_method_mac_win_title': "Bebédan OCR Mac lan Windows",
        'ocr_method_mac_win_voice': "Mac luwih becik",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Bebédan riantara macOS lan Windows</strong></p>

        <p><strong>macOS (karekomendasiang)</strong></p>
        <p>Piranti:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Asil:</p>
        <ul>
        <li>PDF sané prasida karepang antuk teks sané katanem, sané ngajaga tata letak asli.</li>
        </ul>
        <p>Kauntungan:</p>
        <ul>
        <li>Kualitas pangakenan teks sané becik pisan (malih ring kaca sané miring).</li>
        <li>Ngasthayang grafik vektor lan huruf.</li>
        <li>Palet kemajuan GUI liwat evaluasi subproses.</li>
        <li>Kontrol penuh ring makasami parameter OCR (Deskew, Clean, Oversample, optimasi).</li>
        <li>Pangalihan teks langsung wénten ring jendela utama (tampilan PDF).</li>
        </ul>
        <p>Kakurangan:</p>
        <ul>
        <li>Mabutuh piranti sistem tambahan (ocrmypdf, Ghostscript, unpaper, pngquant – kacumpu ring paket App).</li>
        <li>Penanganan kasalahan sané luwih kompleks (deadlocks, timeouts).</li>
        </ul>

        <p><strong>Windows (alternatif stabil)</strong></p>
        <p>Piranti:</p>
        <ul>
        <li>pytesseract (sambungan langsung ka Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Asil:</p>
        <ul>
        <li>PDF sané prasida karepang sané visualé pateh sareng PDF gambar, nanging prasida karepang liwat teks transparan.</li>
        </ul>
        <p>Kauntungan:</p>
        <ul>
        <li>Tan wénten sané ingetang.</li>
        </ul>
        <p>Kakurangan:</p>
        <ul>
        <li>PDF punika dawaning gambar antuk teks sané tan katingal; tata letak prasida lingsir alit ring dokumén kompleks (kolom, tabél).</li>
        <li>Tan wénten koreksi kemiringan otomatis (--deskew) utawi paberesihan gambar (--clean).</li>
        <li>Palet kemajuan GUI kakardi kasar wantah madasar antuk akéh kaca sané kaprosés.</li>
        <li>Kacepetan OCR alon alit (santukan soang-soang kaca kaprosés kapisah).</li>
        <li>Pangalihan teks kauahang ka jendela teks OCR.</li>
        </ul>

        <p><strong>Persamaan</strong></p>
        <ul>
        <li>Kalih proses ngasilang PDF sané prasida karepang ring direktori sané pateh sareng berkas sumber.</li>
        <li>Setélan OCR (basa, DPI, mode segmentasi kaca, mode mesin OCR) prasida kakonfigurasi liwat OCRSettingsDialog tur manjur ring kalih implementasi.</li>
        </ul>

        <p><strong>Rekomendasi:</strong></p>
        <ul>
        <li>macOS: Binary ocrmypdf ngasilang asil sané pinih becik – Bli Mac tur anggén vérsi punika (PDFDarkView antuk Mac sané madaging Apple Silicon utawi chip Intel). Asil OCR becik pisan nandingin Windows!</li>
        <li>Windows: Anggén solusi pytesseract. Punika stabil tur ngasilang kualitas sané cekap antuk akéh dokumén.</li>
        </ul>

        <p><strong>Pangeling-eling:</strong></p>
        <ul>
        <li>Kalih vérsi katémbokang sapunika ring antarmuka panganggén – panganggén tan merasayang bebadan.</li>
        <li>Pogram mutusang sacara otomatis mesin OCR sané jagi kaanggén madasar antuk sistem operasi.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Nyieun tanda tangan (saking pascan)",
        "signature_create_title": "Pilih tanda tangan sané kascan (PDF/Gambar)",
        "image_pdf_filter": "Gambar lan PDF",
        "signature_pdf_empty": "PDF nénten madaging kaca.",
        "signature_created_success": "Tanda tangan prasida kawangun: {0}",
        "signature_create_error": "Kasalahan rikala nyieun tanda tangan:\n{0}",
        "rembg_missing": "rembg durung kamasang.\nJagi masang: pip install rembg\nKasalahan: {0}",
        "signature_name_title": "Aran berkas antuk tanda tangan",
        "signature_name_message": "Ngiring ngisi aran berkas antuk tanda tangan anyar (jagi kasimpen dados PNG antuk latar transparan):",
        "signature_name_label": "Aran berkas:",
        "signature_name_voice": "Ngiring ngisi aran berkas antuk tanda tangan",
        "signature_processing": "Pamrosésan munggahang...",
        "signature_creation_title": "Tanda tangan jagi kawangun",
        "signature_overwrite_warning": "Berkas '{0}' sampun wénten. Gantos?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Nyiyapang PDF antuk tanda tangan",
        "signature_prepare_instruction":"Ngiring pilih PDF sané madaging tanda tangan sané kascan ring asiki kaca.\n\nPangakenan optimal kapolihang yening:\n• Tanda tangan kasurat nganggen tinta selem (bolpoin utawi fineliner) ring kertas putih.\n• Tanda tangan wénten ring telu duur saking kaca A4 sané lianan kosong.\n• PDF kascan minimal 300 dpi.\n• Tanda tangan jelas tur nénten teuing tipis.\n• Nénten wénten pola latar utawi garis sané ngawag.",
        "signature_prepare_voice":"Ngiring pilih PDF sané madaging tanda tangan kascan. Pikayunang kualitas lan kontras sané becik.",
        "sig_thickness_label":"Tebal garis:",
        "sig_thickness_normal":"Normal (tipis)",
        "sig_thickness_bold":"Tebal (karekomendasiang)",
        "sig_thickness_very_bold":"Tebal pisan",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Nambah basa GUI lan OCR - Panduan",
        'language_guide_title': "Nambah basa GUI lan OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Unduh berkas terjemahan sané kapingin <code>translations_xy.py</code> saking<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        tur pasang ring direktori puniki:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Buka panyungsi web panjenengan.</li>
        <li>Anggah ka: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Rereh ring sisin tengen layar antuk "Releases" tur pilih sané kacihnain <strong>"latest"</strong>.</li>
        <li>Ring kaca rilis salanturnyané, unduh berkas <code>Source Code.zip</code> ring betén pisan.</li>
        <li>Buka komprési berkas ZIP.</li>
        <li>Rereh ring folder sané sampun kabuka makasami berkas basa sané kabutuhang, tur salin ka direktori:<br/>
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
        "menu_watermark":"Sisipin tatu toya",
        "fullpage_text_watermark_title":"Teks pinaka tatu toya",
        "fullpage_image_watermark_title":"Gambar pinaka tatu toya",
        "filename_with_watermark":"_antuk_tatu_toya",
        "watermark_text":"Teks:",
        "watermark_text_placeholder":"Teks tatu toya ragane...",
        "watermark_font_family":"Aksara:",
        "watermark_font_size":"Ukuran aksara:",
        "watermark_format":"Pamorahan:",
        "watermark_bold":"Tebal",
        "watermark_italic":"Miring",
        "watermark_color":"Warna:",
        "watermark_choose_color":"Pilih warna...",
        "watermark_opacity":"Beton / Transparan:",
        "watermark_direction":"Arah maca:",
        "watermark_direction_l_r":"Kiwa → Tengen",
        "watermark_direction_bl_tr":"Sor kiwa → Duur tengen",
        "watermark_direction_tl_br":"Duur kiwa → Sor",
        "watermark_direction_b_t":"Sor → Duur",
        "watermark_direction_t_b":"Duur → Sor",
        "watermark_preview":"Pratayang:",
        "watermark_preview_sample":"Toh teks",
        "watermark_empty_text":"Mangda nganggen teks.",
        "watermark_applied":"Tatu toya sampun kakenang ring makasami kaca.",
        "watermark_saved":"Tatu toya sampun kasimpen.",
        "image_scale":"Ukuran:",
        "image_preview":"Pratayang gambar:",
        "no_image_selected":"Nénten wenten gambar kapilih",
        "browse":"Rereh...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Panghapus",
        "redact_add_black": "Panghapus (selem)",
        "redact_add_white": "Panghapus (putih / ngusap)",
        "redact_added_black": "Panghapus selem sampun katambah",
        "redact_added_white": "Panghapus putih sampun katambah",
        "redact_apply_all": "Terapang makasami panghapus tur simpen",
        "redact_discard_all": "Buang makasami panghapus",
        "redact_discard": "Buang panghapus puniki",
        "no_redactions": "Nénten wenten panghapus",
        "redact_confirm_title": "Terapang panghapus permanen",
        "redact_confirm_message": "Pengingat: Wawidangan sané katandain pacang kausap permanen (selem utawi putih).\nCadangan pacang kagawé (yening kaaktipang).\n\nLanturang?",
        "redact_apply": "Inggih, hapus mangkin",
        "redact_saved": "{0} panghapus sampun katerapang tur kasimpen.",
        "redact_saved_voice": "{0} panghapus katerapang",
        "redact_error": "Galat rikala ngapus",
        "filename_redacted":"_kahapus",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Sisipin nomer kaca',
        'page_numbers_format': 'Format nomer:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arab)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Romawi alit)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Romawi ageng)',
        'page_numbers_format_letter': 'A, B, C ... (Aksara)',
        'page_numbers_format_custom': 'Kustom',
        'page_numbers_custom_pattern': 'Pola:',
        'page_numbers_custom_placeholder': 'Cth. "Kaca {nummer}" utawi "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Anggen {nummer} antuk nomer kaca mangkin tur {total} antuk akéh total',
        'page_numbers_position': 'Genah:',
        'page_numbers_pos_tl': 'Duur kiwa',
        'page_numbers_pos_tc': 'Duur tengah',
        'page_numbers_pos_tr': 'Duur tengen',
        'page_numbers_pos_ml': 'Tengah kiwa',
        'page_numbers_pos_mc': 'Katerapang',
        'page_numbers_pos_mr': 'Tengah tengen',
        'page_numbers_pos_bl': 'Sor kiwa',
        'page_numbers_pos_bc': 'Sor tengah',
        'page_numbers_pos_br': 'Sor tengen',
        'page_numbers_margins': 'Bates:',
        'page_numbers_margin_x': 'Bates horizontal:',
        'page_numbers_margin_y': 'Bates vertikal:',
        'page_numbers_range': 'Rentang kaca:',
        'page_numbers_all_pages': 'Makasami kaca',
        'page_numbers_custom_range': 'Rentang kustom',
        'page_numbers_from': 'Saking:',
        'page_numbers_to': 'Ngantos:',
        'page_numbers_progress': 'Nyisipin nomer kaca...',
        'page_numbers_start': 'Ngawitin nyisipin nomer kaca...',
        'page_numbers_cancel': 'Panyisipan nomer kaca kawangdé',
        'page_numbers_success': 'Nomer kaca sampun katambahang.\n\nApaké ragané jagi ngungah PDF anyar?\n\n{0}',
        'page_numbers_complete': 'Nomer kaca sampun katambahang',
        'page_numbers_error_format': 'Galat rikala nyisipin nomer kaca: {0}',
        'page_numbers_content_type': 'Tipe konten:',
        'page_numbers_tab_simple': 'Nomer sederhana',
        'page_numbers_tab_range': 'Kaca X saking Y',
        'page_numbers_tab_date': 'Tanggal',
        'page_numbers_tab_custom': 'Teks bébas',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Kaca {aktuell} saking {gesamt}',
        'page_numbers_range_custom': 'Kustom',
        'page_numbers_range_placeholder': 'Cth. "Kaca {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format tanggal:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Januari 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Kustom',
        'page_numbers_date_placeholder': 'Cth. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Genah:',
        'page_numbers_date_before': 'Tanggal sadurung nomer kaca',
        'page_numbers_date_after': 'Tanggal sesampun nomer kaca',
        'page_numbers_date_only': 'Tanggal wungkul (tanpa nomer kaca)',
        'page_numbers_custom_text': 'Teks kustom:',
        'page_numbers_custom_placeholder_text': 'Anggen {seite} antuk nomer kaca tur {gesamt} antuk total\nCth. "Rahasia - Kaca {seite}" utawi "{seite} saking {gesamt}"',
        "filename_with_page_number":"_antuk_nomer_kaca",
        "filename_with_page_declaration":"_antuk_panyaru_ka",
        "filename_with_pagenumber":"_antuk_nomer_kaca",
        "filename_with_date":"_antuk_tanggal",
        "filename_with_my_page_declaration":"_antuk_panyaru_ka_kustom",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Paubahan tan kasimpen",
        "unsaved_changes_message_darkmode": "Wenten sisipan sané tan kasimpen.\nApaké ragané jagi nyimpen sadurung malih?",
        "save_and_switch": "Simpen tur malih",
        "discard_and_switch": "Malih mangkin",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Ékspor kaca pinaka gambar',
        'export_images_menu': 'Ékspor pinaka gambar (PNG/JPEG)',
        'export_images_format': 'Format gambar:',
        'export_images_dpi': 'Resolusi (DPI):',
        'export_images_quality': 'Kualitas JPEG:',
        'export_images_range': 'Rentang kaca:',
        'export_images_all_pages': 'Makasami kaca',
        'export_images_custom_range': 'Rentang kustom',
        'export_images_from': 'Saking:',
        'export_images_to': 'Ngantos:',
        'export_images_options': 'Pilihan:',
        'export_images_single_files': 'Tiap kaca pinaka berkas misah',
        'export_images_subfolder': 'Ékspor ka folder bawahan',
        'export_images_subfolder_info': 'Ka folder bawahan "aranPDF_gambar"',
        'export_images_same_folder': 'Ring folder sané pateh sareng PDF',
        'export_images_apply_darkmode': 'Terapang setelan PDFDarkView (Mode Peteng)',
        'export_images_target_folder': 'Folder tujuan:',
        'export_images_browse': 'Rereh...',
        'export_images_preview': 'Pratayang:',
        'export_images_preview_info': 'Pilih setelan antuk ékspor',
        'export_images_preview_info_detail': '{0} kaca pinaka {1}\nResolusi: {2} DPI\nAran berkas: {3}\n{4}',
        'export_images_select_folder': 'Pilih folder tujuan',
        'export_images_start': 'Ngawitin ékspor gambar...',
        'export_images_progress': 'Ngékspor gambar...',
        'export_images_saving': 'Nyimpen kaca {0} saking {1}...',
        'export_images_success': 'Ékspor becik!\n\n{0} gambar sampun kasimpen ring:\n{1}',
        'export_images_complete': 'Ékspor gambar puput',
        'export_images_open_folder': '📁 Buka folder',
        'export_images_cancel': 'Ékspor gambar kawangdé',
        'export_images_error_format': 'Galat rikala ngékspor gambar: {0}',
        'export_images_pdf2image_missing': 'Pustaka "pdf2image" tan kaintalang.\n\nMangda kaintalang antuk:\npip install pdf2image\n\nAntuk Windows ragané taler mabuat Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Konversi PDF/A antuk arsip jangka panjang',
        'pdfa_menu': 'Konversi PDF/A (siap arsip)',
        'pdfa_info': 'Ngubah PDF ka format PDF/A.\n\nPDF/A kakaryanang khusus antuk arsip jangka panjang tur njamin dokumen pacang kacingakang becik ring galah sané jagi rauh.',
        'pdfa_standard': 'Standar PDF/A:',
        'pdfa_standard_select': 'Versi:',
        'pdfa_1': 'PDF/A-1 (sederhana, kompatibel luas)',
        'pdfa_2': 'PDF/A-2 (modern, kompresi becik)',
        'pdfa_3': 'PDF/A-3 (versi anyar, ngawinang lampiran)',
        'pdfa_standards_explanation': '📖 Panjelasan standar:\n\n'
            '• PDF/A-1: Dasar, kompatibel sareng sistem kuna (kurang langkung 2005)\n'
            '• PDF/A-2: Langkung modern, kompresi becik, dukungan transparansi (kurang langkung 2011)\n'
            '• PDF/A-3: Versi anyar, ngawinang ngemban lampiran berkas (kurang langkung 2013)\n\n'
            'Rekomendasi: PDF/A-2 inggih punika kompromi becik riantara kompatibilitas tur fitur modern.',
        'pdfa_options': 'Pilihan:',
        'pdfa_compress_enable': 'Kompres PDF (berkas langkung alit)',
        'pdfa_metadata_preserve': 'Sisipin metadata (judul, pangawi, lan pasawahan)',
        'pdfa_target_folder': 'Folder tujuan:',
        'pdfa_browse': 'Rereh...',
        'pdfa_select_folder': 'Pilih folder tujuan',
        'pdfa_ocr_info_unknown': '🔍 Tan prasida mriksa konten teks.',
        'pdfa_ocr_info_not_needed': '✅ Teks wénten - OCR tan kawajibang.\nPDF/A prasida kagawé langsung.',
        'pdfa_ocr_info_recommended': '⚠️ Teks tan kapanggihang akéh.\n\nAntuk PDF sané prasida kapanjingan, mangda OCR kamargiang rumuhun.\nCatetan: PDF/A malarapan yening tanpa OCR - nanging teksé tan prasida kapanjingan.',
        'pdfa_ocr_info_error': '❌ Galat rikala mriksa: {0}',
        'pdfa_start': 'Ngawitin konversi PDF/A...',
        'pdfa_progress': 'Konversi PDF/A mamargi...',
        'pdfa_success': 'Konversi PDF/A becik!\n\nKasimpen pinaka:\n{0}\n\nApaké ragané jagi ngungah PDF anyar?',
        'pdfa_complete': 'Konversi PDF/A puput',
        'pdfa_cancel': 'Konversi PDF/A kawangdé',
        'pdfa_error_format': 'Galat rikala konversi PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Pustaka "ocrmypdf" tan kaintalang.\n\nMangda kaintalang antuk:\npip install ocrmypdf',
        'btn_convert': 'Konversi',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimasi PDF (ngurangin ukuran berkas)',
        'optimize_menu': 'Optimasi PDF (ukuran berkas)',
        'optimize_info': 'Ngurangin ukuran berkas PDF antuk makudang metode optimasi.\n\nSemanin tegeh tingkat kompresi, semanin alit berkasé - sareng kamungkinan kualitas gambar sané ical.',
        'optimize_level': 'Tingkat kompresi:',
        'optimize_level_low': 'Rendah (cepat, penghematan alit)',
        'optimize_level_medium': 'Sedeng (kompromi becik)',
        'optimize_level_high': 'Tinggi (penghematan ageng)',
        'optimize_level_maximum': 'Maksimum (penghematan maksimum, lambat)',
        'optimize_level_explanation': 'Rekomendasi: "Sedeng" inggih punika kompromi becik riantara kecepatan tur ukuran berkas.',
        'optimize_options': 'Pilihan:',
        'optimize_compress_images': 'Kompres gambar (ngurangin kualitas JPEG)',
        'optimize_clean_objects': 'Singkirang objek sané tan kagehang',
        'optimize_preserve_metadata': 'Sisipin metadata (judul, pangawi, lan pasawahan)',
        'optimize_image_quality': 'Kualitas gambar:',
        'optimize_range': 'Rentang kaca:',
        'optimize_all_pages': 'Makasami kaca',
        'optimize_custom_range': 'Rentang kustom',
        'optimize_from': 'Saking:',
        'optimize_to': 'Ngantos:',
        'optimize_target_folder': 'Folder tujuan:',
        'optimize_browse': 'Rereh...',
        'optimize_select_folder': 'Pilih folder tujuan',
        'optimize_info_box': 'Informasi',
        'optimize_info_text': 'Optimasi prasida ngambil makudang menit antuk PDF ageng.\n\nGambar kasimpen antuk kualitas sané kurangi, sané prasida ngurangin ukuran berkas sacara signifikan.',
        'optimize_start': 'Ngawitin optimasi PDF...',
        'optimize_progress': 'Ngoptimasi PDF...',
        'optimize_cancel': 'Optimasi PDF kawangdé',
        'optimize_complete': 'Optimasi PDF puput',
        'optimize_error_format': 'Galat rikala optimasi PDF:\n\n{0}',
        'optimize_success_message': 'Optimasi PDF becik!\n\nKasimpen pinaka:\n{0}\n\nSadurung: {1}\nSesampun: {2}\nPenghematan: {3:.1f}%\n\n{4}\n\nApaké ragané jagi ngungah PDF sané kaoptimasi?',
        'optimize_success_message_no_size': 'Optimasi PDF becik!\n\nKasimpen pinaka:\n{0}\n\nInformasi ukuran tan kasedia.\n\nApaké ragané jagi ngungah PDF sané kaoptimasi?',
        'optimize_result_positive': 'Berkas sampun kaurangin {0:.1f}%.',
        'optimize_result_zero': 'Tan wénten panguahan ukuran berkas.',
        'optimize_result_negative': 'Berkas sampun kateggang {0:.1f}%.\nOptimasi kawangdé, berkas asli kasisipang.',
        'btn_optimize': 'Ngawitin optimasi',
        'filename_optimize_low_suffix': '_optimasi_rendah',
        'filename_optimize_medium_suffix': '_optimasi',
        'filename_optimize_high_suffix': '_optimasi_tinggi',
        'filename_optimize_maximum_suffix': '_optimasi_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Motong PDF',
        'crop_menu': 'Motong PDF (Crop)',
        'crop_range': 'Terapang ka:',
        'crop_all_pages': 'Makasami kaca',
        'crop_current_page': 'Kaca mangkin wungkul',
        'crop_values': 'Nilai motong (ring titik):',
        'crop_left': 'Kiwa:',
        'crop_right': 'Tengen:',
        'crop_top': 'Duur:',
        'crop_bottom': 'Sor:',
        'crop_presets': 'Pratetap:',
        'crop_preset_white': 'Deteksi bates putih',
        'crop_reset': 'Reset',
        'crop_mouse_hint': '🖱️ Seret persegi panjang antuk milih wawidangan sacara kasar.\nSesampun punika ragané prasida nyaluyung nilai ring SpinBox.\nPanyaluyungan manual antuk mouse tan prasida.',
        'crop_apply': 'Motong',
        'crop_scope_all': 'Makasami kaca',
        'crop_scope_current': 'Kaca mangkin',
        'crop_new_size': 'Ukuran anyar: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Tan wénten PDF kaunggah',
        'crop_preview_error': 'Galat rikala ngunggah pratyang',
        'crop_start': 'Ngawitin motong...',
        'crop_progress': 'Ngmotong PDF...',
        'crop_success': 'PDF ka-motong becik!\n\nKasimpen pinaka:\n{0}\n\nApaké ragané jagi ngungah PDF sané ka-motong?',
        'crop_complete': 'Motong puput',
        'crop_cancel': 'Motong kawangdé',
        'crop_error_format': 'Galat rikala motong:\n\n{0}',
        'filename_crop_suffix': '_kamotong',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Ngelus PDF (Flatten)',
        'flatten_menu': 'Ngelus PDF (Flatten)',
        'flatten_info': 'Ngelus PDF "ngabakar" makasami elemen sané prasida kauwah ring konten kaca.\n\nSesampun punika, widang formulir, anotasi, teks, silang, tanda tangan, gambar tur wangun tan prasida kauwah malih.',
        'flatten_explanation_title': '📖 Antuk apa puniki?',
        'flatten_explanation_text': 'Ngelus mabuat ring situasi puniki:\n\n'
            '• 📄 Ragané jagi nyiapang dokumen antuk nyetak\n'
            '• 🔒 Ragané jagi ngawinang tan wenten sané ngubah widang formulir\n'
            '• 📎 Ragané jagi "nanceb" anotasi tur koméntar ring dokumen\n'
            '• 🖼️ Ragané jagi nanceb teks, silang, tanda tangan, gambar tur wangun ring dokumen\n'
            '• 📦 Ragané jagi nyiapang berkas antuk arsip\n\n'
            'Ngelus ngawinang PDF langkung alit tur nyegah elemen kagingsirang utawi kausap sacara tan sengaja.',
        'flatten_what_title': 'Apa sané kaelus?',
        'flatten_what_list': '• ✅ Widang formulir (widang teks, kotak centang, tombol)\n'
            '• ✅ Anotasi (koméntar, panyuratan, catetan)\n'
            '• ✅ Overlay (teks, silang, tanda tangan, gambar, wangun)',
        'flatten_options': 'Pilihan:',
        'flatten_forms': 'Elus widang formulir',
        'flatten_annotations': 'Elus anotasi',
        'flatten_overlays': 'Elus overlay (teks, silang, tanda tangan, gambar, wangun)',
        'flatten_target_folder': 'Folder tujuan:',
        'flatten_browse': 'Rereh...',
        'flatten_select_folder': 'Pilih folder tujuan',
        'flatten_warning': '⚠️ Penting: Ngelus inggih punika proses sané tan prasida kawali!\n\nSesampun ngelus, elemen sané prasida kauwah tan prasida kauwah utawi kausap malih.\nKaryanang cadangan sadurung yening mabuat.',
        'flatten_apply': 'Elus',
        'flatten_start': 'Ngawitin ngelus...',
        'flatten_progress': 'Ngelus PDF...',
        'flatten_success': 'PDF ka-elus becik!\n\nKasimpen pinaka:\n{0}\n\nApaké ragané jagi ngungah PDF sané ka-elus?',
        'flatten_complete': 'Ngelus puput',
        'flatten_cancel': 'Ngelus kawangdé',
        'flatten_error_format': 'Galat rikala ngelus:\n\n{0}',
        'filename_flatten_suffix': '_kaelus',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Numpang PDF (Overlay)',
        'overlay_menu': 'Numpang PDF (Overlay)',
        'overlay_info': 'Nempatang PDF (overlay) ring duur PDF lianan.\n\nPDF overlay katempataang ring PDF dasar. Puniki mabuat antuk tatu toya, logo, kop surat utawi cap.',
        'overlay_explanation_title': '📖 Antuk apa puniki?',
        'overlay_explanation_text': 'Numpang mabuat ring situasi puniki:\n\n'
            '• 🏢 Nempatang logo perusahaan pinaka tatu toya ring tiap kaca\n'
            '• 📄 Nempatang kop surat ring PDF kosong\n'
            '• 🖊️ Nempatang overlay cap ring dokumen\n'
            '• 🔖 Nempatang tatu toya ring makasami kaca\n'
            '• 📑 Nempatang overlay formulir ring citra',
        'overlay_type': 'Tipe overlay:',
        'overlay_type_fullpage': 'Kaca penuh (nutup)',
        'overlay_type_transparent': 'Kaca penuh (transparan - karekomendasiang)',
        'overlay_type_stamp': 'Cap (prasida ka-genahang)',
        'overlay_type_info_fullpage': '📄 PDF overlay katempataang tepat ring duur kaca penuh.\nLatar putih prasida kausap mangda wantah konten sané kacingak.',
        'overlay_type_info_transparent': '🔍 PDF overlay katempataang ring duur kaca penuh antuk latar transparan.\nLatar putih kausap otomatis - becik pisan antuk tatu toya tur logo!',
        'overlay_type_info_stamp': '🖊️ PDF overlay katempataang tur kaskala pinaka cap.\nBecik pisan antuk logo, cap utawi tanda tangan ring genah tarténtu.',
        'overlay_remove_background': 'Usap latar putih:',
        'overlay_remove_background_enable': 'Usap latar putih saking PDF overlay (ngawinang overlay transparan)',
        'overlay_remove_background_tooltip': 'Ngusap wawidangan putih saking PDF overlay mangda teks sané ring sor kacingak.',
        'overlay_threshold': 'Nilai ambang:',
        'overlay_threshold_hint': '(1-254, tegeh = ngusap putih langkung akéh)',
        'overlay_select_file': 'Pilih PDF overlay:',
        'overlay_file_placeholder': 'Mangda milih berkas PDF antuk overlay',
        'overlay_browse': 'Rereh...',
        'overlay_select_overlay': 'Pilih PDF overlay',
        'overlay_range': 'Rentang kaca:',
        'overlay_all_pages': 'Makasami kaca',
        'overlay_custom_range': 'Rentang kustom',
        'overlay_from': 'Saking:',
        'overlay_to': 'Ngantos:',
        'overlay_position': 'Genah:',
        'overlay_position_center': 'Tengah',
        'overlay_position_top_left': 'Duur kiwa',
        'overlay_position_top_right': 'Duur tengen',
        'overlay_position_bottom_left': 'Sor kiwa',
        'overlay_position_bottom_right': 'Sor tengen',
        'overlay_size': 'Ukuran:',
        'overlay_size_original': 'Ukuran asli',
        'overlay_size_fit_page': 'Pasang ring kaca',
        'overlay_size_custom': 'Kustom (%)',
        'overlay_opacity': 'Transparansi:',
        'overlay_target_folder': 'Folder tujuan:',
        'overlay_browse_folder': 'Rereh...',
        'overlay_select_folder': 'Pilih folder tujuan',
        'overlay_warning': '⚠️ Catetan: PDF overlay katempataang ring PDF dasar tur "kabakar" ring jerone.\n\nElemen PDF overlay tan prasida kauwah malih sesampun kasimpen.',
        'overlay_apply': 'Tumpang',
        'overlay_start': 'Ngawitin numpang...',
        'overlay_progress': 'Numpang PDF...',
        'overlay_success': 'PDF ka-tumpang becik!\n\nKasimpen pinaka:\n{0}\n\nApaké ragané jagi ngungah PDF sané ka-tumpang?',
        'overlay_complete': 'Numpang puput',
        'overlay_cancel': 'Numpang kawangdé',
        'overlay_error_format': 'Galat rikala numpang:\n\n{0}',
        'overlay_no_file': 'Tan wénten PDF overlay kapilih.\n\nMangda milih berkas PDF antuk katumpang.',
        'filename_overlay_suffix': '_katumpang',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Ekstrak gambar saking PDF',
        'extract_images_menu': 'Ekstrak makasami gambar',
        'extract_images_info': 'Ekstrak makasami gambar saking PDF tur simpen pinaka berkas misah.\n\nGambar kasimpen ring format asli utawi kaonversi ka format sané kapilih.',
        'extract_images_format': 'Format gambar:',
        'extract_images_quality': 'Kualitas JPEG:',
        'extract_images_options': 'Pilihan:',
        'extract_images_subfolder': 'Ekstrak ka folder bawahan ("aranPDF_gambar")',
        'extract_images_unique': 'Gambar unik wungkul (nyegah duplikat)',
        'extract_images_range': 'Rentang kaca:',
        'extract_images_all_pages': 'Makasami kaca',
        'extract_images_custom_range': 'Rentang kustom',
        'extract_images_from': 'Saking:',
        'extract_images_to': 'Ngantos:',
        'extract_images_target_folder': 'Folder tujuan:',
        'extract_images_browse': 'Rereh...',
        'extract_images_select_folder': 'Pilih folder tujuan',
        'extract_images_info_box': 'Informasi',
        'extract_images_info_text': 'Ekstraksi prasida ngambil makudang menit antuk PDF ageng.\n\nGambar kasimpen antuk aran asli (kaca_gambar).',
        'extract_images_extract': 'Ekstrak',
        'extract_images_start': 'Ngawitin ekstraksi...',
        'extract_images_progress': 'Ngekstrak gambar...',
        'extract_images_success': '✅ Gambar ka-ekstrak becik!\n\n{0} gambar sampun kasimpen ring:\n{1}',
        'extract_images_complete': 'Ekstraksi gambar puput',
        'extract_images_cancel': 'Ekstraksi kawangdé',
        'extract_images_error_format': 'Galat rikala ngekstrak gambar:\n\n{0}',
        'extract_images_open_folder': '📁 Buka folder',
        'extract_images_no_images': 'Tan wenten gambar kapanggih ring PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Makudang kaca ring satunggil kaca (N-Up)',
        'nup_menu': 'Makudang kaca ring satunggil kaca (N-Up)',
        'nup_info': 'Nata makudang kaca PDF ring satunggil kaca.\n\nBecik antuk cetakan kompak, tinjauan utawi handout.',
        'nup_layout': 'Tata letak:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Pratayang:',
        'nup_preview_info': '{0} kaca → {1} kaca per lembar → {2} lembar\nTata letak: {3}',
        'nup_order': 'Urutan:',
        'nup_order_horizontal': 'Horizontal (sabaris)',
        'nup_order_vertical': 'Vertikal (sakolom)',
        'nup_order_horizontal_reverse': 'Horizontal kabalik',
        'nup_order_vertical_reverse': 'Vertikal kabalik',
        'nup_range': 'Rentang kaca:',
        'nup_all_pages': 'Makasami kaca',
        'nup_custom_range': 'Rentang kustom',
        'nup_from': 'Saking:',
        'nup_to': 'Ngantos:',
        'nup_options': 'Pilihan:',
        'nup_margins': 'Bates:',
        'nup_margin_between': 'Jarak riantara kaca:',
        'nup_page_numbers': 'Sisipin nomer kaca',
        'nup_target_folder': 'Folder tujuan:',
        'nup_browse': 'Rereh...',
        'nup_select_folder': 'Pilih folder tujuan',
        'nup_create': 'Karyanang',
        'nup_start': 'Ngawitin N-Up...',
        'nup_progress': 'Ngawangun N-Up...',
        'nup_success': 'N-Up ka-wangun becik!\n\nKasimpen pinaka:\n{0}\n\nApaké ragané jagi ngungah PDF anyar?',
        'nup_complete': 'N-Up puput',
        'nup_cancel': 'N-Up kawangdé',
        'nup_error_format': 'Galat rikala N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Ubah ukuran kaca',
        'pagesize_menu': 'Ubah ukuran kaca',
        'pagesize_info': 'Ngubah ukuran kaca PDF.\n\nKonten otomatis kaluyungang ring ukuran anyar.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Pilih format standar:',
        'pagesize_custom': 'Ukuran kustom:',
        'pagesize_width': 'Linggah:',
        'pagesize_height': 'Duur:',
        'pagesize_orientation': 'Orientasi:',
        'pagesize_portrait': 'Potret',
        'pagesize_landscape': 'Lanskap',
        'pagesize_scale_options': 'Pilihan skala:',
        'pagesize_fit': 'Pasang (sisiin rasio aspek)',
        'pagesize_stretch': 'Regang (distorsi)',
        'pagesize_center': 'Tengah (ukuran asli)',
        'pagesize_range': 'Rentang kaca:',
        'pagesize_all_pages': 'Makasami kaca',
        'pagesize_custom_range': 'Rentang kustom',
        'pagesize_from': 'Saking:',
        'pagesize_to': 'Ngantos:',
        'pagesize_target_folder': 'Folder tujuan:',
        'pagesize_browse': 'Rereh...',
        'pagesize_select_folder': 'Pilih folder tujuan',
        'pagesize_apply': 'Terapang',
        'pagesize_start': 'Ngawitin ngubah ukuran kaca...',
        'pagesize_progress': 'Ngubah ukuran kaca...',
        'pagesize_success': 'Ukuran kaca ka-ubah becik!\n\nKasimpen pinaka:\n{0}\n\nApaké ragané jagi ngungah PDF anyar?',
        'pagesize_complete': 'Ngubah ukuran kaca puput',
        'pagesize_cancel': 'Ngubah ukuran kaca kawangdé',
        'pagesize_error_format': 'Galat rikala ngubah ukuran kaca:\n\n{0}',
        'pagesize_preview_info': 'Ukuran anyar: {0} x {1} pt',
        'filename_pagesize_suffix': '_ukuran_anyar',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informasi PDF',
        'pdf_info_menu': 'Tayang informasi PDF',
        'pdf_info_voice': 'Informasi PDF kacingakang',
        'pdf_info_error': 'Galat rikala nayang informasi PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Tayang péték keyboard",
        "shortcuts_dialog_title": "Péték Keyboard",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 BERKAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Buka PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Tutup PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Simpen pinaka...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Lindungin dokumen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Cetak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Cetak langsung (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Punyah aplikasi</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 ÉKSPOR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Ékspor pinaka Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Ékspor pinaka DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Ékspor pinaka TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Ékspor pinaka gambar (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Ekstrak gambar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PANGOLAHAN DOKUMEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Makudang kaca)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Konversi PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Elus PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Tumpang PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimasi PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ UBAH</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Rereh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Tambah tetenger</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Atur tetenger</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Tetenger salanturné</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Tetenger sadurungné</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Jalankan OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 PANGELOLAAN KACA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Puter kaca mangkin</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Puter makasami kaca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalisasi kaca mangkin</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalisasi makasami kaca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Hapus kaca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ekstrak kaca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Sisipin kaca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Gingsir kaca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Gabung PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Ubah ukuran kaca</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 SISIPIN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Sisipin teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Sisipin silang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Sisipin tanda tangan 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Sisipin tanda tangan 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Sisipin gambar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Sisipin persegi panjang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Sisipin elips</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Sisipin garis</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Sisipin panah</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Sisipin nomer kaca</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Tatu toya teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Tatu toya gambar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ PANGHAPUS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Panghapus (selem)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Panghapus (putih)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Terapang makasami panghapus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ MAJU</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Motong PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Ubah metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ TAYANG</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Alih Mode Peteng/Terang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Tayang jendela teks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Linggah kaca (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Kalih kaca (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Tinjauan (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ SETELAN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Pangelolaan sandi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Setelan OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Setelan tanda tangan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Format aran berkas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Ékspor setelan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Impor setelan</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMASI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Tayang informasi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Alih output suara</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokus bar menu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Versi anyar tersedia",
        "update_available_message": "Wenten versi anyar <b>{0}</b>.\n\nRauhang kaca rilis antuk ngunduh pembaruan:\n{1}",
        "update_available_voice": "Versi anyar {0} tersedia. Ngunduh pembaruan saking kaca GitHub.",
        "update_open_release": "Buka kaca rilis",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Unduh makasami terjemahan",
        "ask_download_all_translations": """Sajaba antuk basa Jerman, Inggris, miwah Vietnam, wenten malih {total_languages} basa GUI sané tersedia.\n\nNapi patut kasediaang / kapingarauin?\n\nPangeling:\nBasa sané nénten kaperluang prasida kausap salanturné ring direktori:\n{translations_path}
        sacara manual.\n\nYen ngicen, basa GUI prasida kaunduh salanturné ngalanturang menu 'Piranti → Pembaruan terjemahan'.""",
        "menu_update_translations": "Pembaruan terjemahan",
        "translations_updated": "Terjemahan kapingarauin",
        "translations_update_success": "{} terjemahan sampun kapingarauin ({} anyar, {} kapingarauin).",
        "translations_update_error": "Salah ring ngapingarauin terjemahan",
        "translations_update_no_changes": "Makasami terjemahan sampun anyar.",
        "translations_update_offline": "Nénten wénten sambungan internet. Terjemahan nénten prasida kapingarauin.",
        "translations_update_in_progress": "Terjemahan kapingarauin ring latar...",
        "translations_downloading": "Ngunduh terjemahan...",
        "translations_path_hint": "Direktori panganggé antuk terjemahan",
        "translations_update_not_available_title": "Pembaruan nénten tersedia",
        "translations_update_not_available_message": """Pembaruan terjemahan wantah tersedia ring versi sané kainsalang.\n\nRing mode pamekaran, terjemahan sampun anyar.""",
        "translations_update_no_internet_title": "Nénten wénten sambungan internet",
        "translations_update_no_internet_message": """Nénten prasida nyambung ka internet.\n\nTerjemahan nénten prasida kaunduh saking GitHub.\n\nSolusi sané prasida:
        • Pariksa sambungan internet
        • Paténang firewall sauntara
        • Coba malih salanturné
        \nTerjemahan taler prasida kaunduh sacara manual saking GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Pembaruan sampun kamargiang",
        "btn_retry": "Coba malih",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Rahajeng rauh ring PDF Dark View",
        "welcome_title_not_supported": "Rahajeng rauh ring PDF Dark View",
        "welcome_message": "Rahajeng rauh ring PDF Dark View!\n\nBasa sistem ragané kakenalang antuk '{language}'.\nNapi ragané jagi nganggén basa puniki antuk antarmuka panganggé?\n\nRagané prasida ngelih basa sawayahanyang ngalanturang 'Setélan → Basa'.",
        "welcome_message_language_not_available": "Rahajeng rauh ring PDF Dark View!\n\nBasa sistem ragané kakenalang antuk '{language}'.\nBasa puniki durung kainsalang.\n\nNapi ragané jagi ngunduh terjemahan antuk {language} mangkin saking GitHub?\n\n(Basa puniki lantas kaanggén antarmuka panganggé.)",
        "welcome_message_language_not_supported": "Rahajeng rauh ring PDF Dark View!\n\nBasa sistem ragané kakenalang antuk '{language}'.\nSayangnyané, durung wénten terjemahan antuk basa puniki.\n\nAntarmuka panganggé lantas kauningang ring {fallback_language}.\n\nRagané prasida ngelih basa sawayahanyang ngalanturang 'Setélan → Basa'.\nYen ragané kayun, prasida taler ngicén terjemahan antuk basa ragané:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Inggih, nganggén basa sistem",
        "welcome_keep_english": "Nénten, tetep Inggris",
        "welcome_download_language": "Inggih, unduh {language}",

        # ============================================
        # 107. JALAN ANYAR KAUNA
        # ============================================

        'menu_recent': 'Anyar kauna',
        'menu_recent_dirs': 'Direktori...',
        'menu_recent_files': 'Berkas...',
        'recent_manage': 'Atur...',
        'recent_enable_tracking': 'Simpan jalan anyar kauna (privasi)',
        'recent_enable_info': 'Patenang opsi puniki mangda tan nyimpen jalan',
        'recent_tracking_disabled': 'Pelacakan jalan kapatenang',
        'recent_enabled': 'kaaktipang',
        'recent_disabled': 'kapatenang',
        'recent_tracking_status': 'Pelacakan jalan {0}',
        'recent_dialog_title': 'Jalan anyar kauna',
        'recent_tab_directories': 'Direktori',
        'recent_tab_files': 'Berkas',
        'recent_dirs_instruction': 'Klik kaping kalih antuk ngawit dialog berkas ring direktori',
        'recent_files_instruction': 'Klik kaping kalih antuk ngawit PDF langsung',
        'recent_no_directories': '(tan direktori kaimb)',
        'recent_no_files': '(tan berkas kaimb)',
        'recent_default_current': '⭐ Baku: {0}',
        'recent_set_as_default': '⭐ Tetapang baku',
        'recent_default_set_title': 'Direktori baku sampun katemtokang',
        'recent_default_set_message': 'Direktori "{0}" sampun katemtokang baku antuk ngawit PDF.',
        'recent_default_set_voice': 'Direktori baku sampun katemtokang',
        'recent_directory_not_found': 'Direktori tan katemuang',
        'recent_file_not_found': 'Berkas tan katemuang',
        'recent_remove_selected': 'Usap',
        'recent_remove_title': 'Usap jalan',
        'recent_remove_confirm': 'Napi semeton yakin ngusap jalan "{0}" saking lis?',
        'recent_path_removed': 'Jalan sampun kausap',
        'recent_clear_all': 'Usap samian',
        'recent_clear_title': 'Usap samian jalan',
        'recent_clear_confirm_type': 'Napi semeton yakin ngusap samian {0}?',
        'recent_cleared': 'Lis sampun karesihang',
        'recent_path_not_found_title': 'Jalan tan katemuang',
        'recent_path_not_found_message': 'Jalan "{0}" nenten wenten malih.',
        'recent_open_file': 'Buka berkas',
        'btn_open_recent': 'Buka',
        'recent_open_file_question': 'Napi semeton jagi buka "{0}" pinaka PDF?',
        'recent_not_pdf': 'Berkas kapilih nenten PDF.',
        'recent_more_entries': 'Entri lianan...',
        'btn_remove': 'Usap',
        'btn_clear': 'Usap samian',
        'recent_context_open': 'Buka',
        'recent_context_reveal': 'Cingakin ring Finder',
        'recent_context_set_default': '⭐ Tetapang baku',
        'recent_context_open_terminal': '💻 Buka Terminal',
        'recent_context_file_info': 'Inpormasi berkas',
        'recent_context_open_with_default': '📄 Buka sareng aplikasi baku',
        'recent_context_remove': 'Usap saking lis',
        'recent_context_clear_all': 'Usap samian',
        'recent_file_info_title': 'Inpormasi berkas',
        'recent_file_info_name': 'Adan',
        'recent_file_info_path': 'Jalan',
        'recent_file_info_size': 'Ukuran',
        'recent_file_info_modified': 'Kaubah',
        'recent_file_info_pages': 'Kaca',
        'recent_error_reveal': 'Galat ngawitin ring Finder',
        'recent_error_terminal': 'Galat ngawitin Terminal',
        'recent_error_info': 'Galat ngalih inpormasi berkas',
        'open_user_data_folder': 'Cingakin direktori data semeton',

        # ============================================
        # 108. USAP KACA GENAP/GANJIL
        # ============================================
        "pages_delete_even": "Usap samian kaca genap",
        "pages_delete_odd":  "Usap samian kaca ganjil",
        "progress_even_pages": "Ngusap kaca genap",
        "progress_odd_pages": "Ngusap kaca ganjil",
        "progress_mark_delete_even": "{} kaca genap katandain antuk kausap",
        "progress_mark_delete_odd":  "{} kaca ganjil katandain antuk kausap",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program kapinggatang",

    }
