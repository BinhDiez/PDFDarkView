
# ============================================
# translations_tl.py - Tagalog Wörterbuch für PDFDarkView
# Vollständig sortiert nach Kategorien
# ============================================

def load_tagalog_strings():
    """Lädt alle Tagalog Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "I-load ang PDF",
        'btn_text_window': "OCR na Teksto",
        'btn_first': "Unang Pahina",
        'btn_prev': "Nakaraang Pahina",
        'btn_next': "Susunod na Pahina",
        'btn_last': "Huling Pahina",
        'btn_print': "I-print",
        'btn_darkmode_light': "Light Mode",
        'btn_darkmode_dark': "Dark Mode",
        'btn_delete_pages': "Burahin ang mga pahina",
        'btn_extract_pages': "Kunin ang mga pahina",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Kanselahin",
        'btn_save': "I-save",
        'btn_close': "Isara",
        'btn_delete': "Burahin",
        'btn_delete_all': "Burahin lahat",
        'btn_copy': "Kopyahin",
        'btn_export': "I-export",
        'btn_show': "Ipakita ang password",
        'btn_hide': "Itago ang password",
        'btn_authenticate': "Patunayan",
        'btn_settings': "Mga Setting",
        'btn_protect': "Protektahan",
        'btn_remove_password': "Alisin ang password",
        'btn_manage': "Pamahalaan ang password",
        'btn_retry': "Subukang muli",
        'btn_select_all': "Piliin lahat",
        'btn_clear_selection': "Alisin ang pagpili",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Pahina {0} ng {1}",
        'page_count': "ng {0}",
        'goto_page': "Pumunta sa pahina",
        'page_simple': "Pahina {0}",
        'full_view_page': "Buong tanawin pahina {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Ilagay ang terminong hahanapin + Enter",
        'search_results': "Mga resulta: {0} ng {1}",
        'search_nav_hint': "Enter: susunod (Shift+Enter: nakaraan) na resulta",
        'search_no_results': "Walang resulta",
        'search_error': "Error sa paghahanap",
        'search_active': "Aktibo ang field ng paghahanap",
        'search_closed': "Natapos ang paghahanap",
        'search_position': "Pahina {0} {1}",
        'search_pos_top': "pinakaitaas",
        'search_pos_upper': "itaas",
        'search_pos_middle': "gitna",
        'search_pos_lower': "ibaba",
        'search_pos_bottom': "pinakababa",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Matagumpay na natapos ang pagkilala sa teksto!",
        'ocr_success_title': "Matagumpay ang OCR",
        'ocr_success_message': "Naghahanap na ngayon ang dokumento.",
        'ocr_failed': "Nabigo ang OCR",
        'ocr_in_progress': "Isinasagawa ang OCR",
        'ocr_preparing': "Inihahanda ang PDF...",
        'ocr_analyzing': "Sinusuri ang PDF...",
        'ocr_optimizing': "Ino-optimize ang larawan...",
        'ocr_recognizing': "Isinasagawa ang pagkilala sa teksto...",
        'ocr_embedding': "Ine-embed ang teksto...",
        'ocr_finalizing': "Sinasapinal ang PDF...",
        'ocr_not_available': "Hindi available ang OCR",
        'ocr_install_message': "Hindi mahanap ang mga OCR tool.\n\nPakiusap i-install ang:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Kailangan ang OCR",
        'ocr_question': "Walang mahanap na teksto ang PDF.\nGusto mo bang mag-OCR upang paganahin ang {0}?",
        'ocr_perform': "Gawin ang OCR",
        'ocr_later': "Mamaya",
        'ocr_starting': "Sinisimulan ang garantisadong OCR...",
        'ocr_success_voice': "Matagumpay ang OCR. Naghahanap na ngayon ang PDF.",
        'ocr_partial_success': "Ginawa ang OCR, ngunit nagkaroon ng problema sa pagpapalit.\n\nAng bersyong nahahanap ay na-save sa:\n{0}\n\nError: {1}",
        'ocr_partial_title': "Bahagyang matagumpay ang OCR",
        'ocr_partial_voice': "Ginawa ang OCR, ngunit nabigo ang pagpapalit.",
        'original_file': "Orihinal na file:",
        'old_size': "Lumang laki ng file:    {0} bytes",
        'new_size': "Bagong laki ng file: {0} bytes",
        'size_change': "Pagbabago: {0}{1} bytes",
        'backup_created_file': "Nagawa ang backup:\n{0}",
        'backup_not_created': "Backup: Hindi nagawa (naka-disable ang setting)",
        'page_header': "=== Pahina {0} ===\n{1}\n",
        'scanned_page_header': "=== Pahina {0} (na-scan) ===\n[Ang pahinang ito ay naglalaman lamang ng na-scan na teksto]\n[Pakiusap manu-manong mag-OCR]\n",
        'scanned_warning': "⚠️ NA-SCAN NA TEKSTO - KAILANGAN ANG OCR",
        'guaranteed_title': "Nagawang mahanap na PDF",
        'guaranteed_message': "<b>Nagawang garantisadong mahanap na bersyon!</b>\n\nDahil nabigo ang awtomatikong OCR, isang\nalternatibong mahanap na PDF ang nagawa:\n\n{0}\n\n<b>Ang file na ito ay naglalaman ng:</b>\n• Nakuha na teksto (kung mayroon)\n• Mga paalala para sa na-scan na mga pahina\n• Ganap na mahanap",
        'guaranteed_voice': "Nagawang garantisadong mahanap na PDF.",
        'instruction_title': "PAALALA PARA SA OCR",
        'instruction_file': "Orihinal na file: {0}",
        'instruction_text': "Nabigo ang awtomatikong pagkilala sa teksto (OCR).\nPakiusap manu-manong mag-OCR:\n\n1. GAMIT ANG OCRmyPDF (command line):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. GAMIT ANG ADOBE ACROBAT (macOS/Windows):\n   • Buksan ang PDF sa Acrobat\n   • Tools > Edit PDF\n   • Piliin ang 'Text Recognition'\n\n3. GAMIT ANG PREVIEW (macOS):\n   • Buksan ang PDF sa Preview\n   • File > Export...\n   • Quartz Filter: 'Reduce File Size'\n   • I-activate ang 'Gumawa ng OCR'\n\n4. ONLINE OCR SERVICES:\n   • smallpdf.com/de/ocr-pdf\n   • ilovepdf.com/de/ocr-pdf\n   • adobe.com/de/acrobat/online/pdf-to-word.html",
        'instruction_created': "Nagawang paalala para sa OCR",
        'instruction_created_message': "Isang detalyadong paalala ang nagawa:\n\n{0}\n\nPakiusap sundin ang mga hakbang para sa manu-manong OCR.",
        'instruction_created_voice': "Nagawang paalala para sa OCR.",
        'ocr_impossible': "Hindi posible ang OCR",
        'ocr_impossible_message': "Hindi magawa ang OCR.\n\nPakiusap iproseso ang '{0}' nang manu-mano gamit ang OCR software.",
        'ocr_impossible_voice': "Hindi posible ang OCR. Pakiusap iproseso nang manu-mano.",
        'emergency_title': "Emergency OCR",
        'emergency_message': "Isang emergency PDF ang nagawa:\n\n{0}\n\nPakiusap iproseso ang file na ito nang manu-mano gamit ang OCR.",
        'emergency_voice': "Nagawang emergency PDF. Pakiusap manu-manong mag-OCR.",
        'critical_error': "Kritikal na Error",
        'critical_error_message': "Hindi masimulan ang OCR.\n\nPakiusap i-restart ang programa at\nsuriin ang pag-install ng OCR.",
        'critical_error_voice': "Kritikal na error sa OCR",
        'ocr_question_html': "<p>Walang mahanap na teksto ang PDF.<p>Gusto mo bang mag-OCR upang paganahin ang <b>{0}</b>?</p>",
        'ocr_question_voice': "Kailangan ang OCR. Walang mahanap na teksto ang PDF. Gusto mo bang mag-OCR upang paganahin ang {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "walang naka-load na PDF",
        'no_pdf_message': "Walang naka-load na PDF",
        'pdf_not_found': "Hindi mahanap ang PDF file",
        'file_size': "Laki ng file",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Nagawang backup",
        'backup_disabled': "Naka-disable ang backup",
        'backup_activated': "Naka-activate ang paggawa ng backup",
        'backup_deactivated': "Naka-deactivate ang paggawa ng backup",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ naka-activate",
        'backup_off': "✘ naka-deactivate",
        'close_pdf': "Sinasara ang PDF: {0}",
        'pdf_not_found_format': "Hindi mahanap ang PDF file: {0}",
        'error_pdf_load_format': "Error sa pag-load ng PDF: {0}",
        'load_failed_format': "Nabigo ang pag-load:\n{0}",
        'decrypted_suffix': "(na-decrypt)",
        'decryption_failed': "Nabigo ang pag-decrypt.",
        'decryption_error': "Error sa pag-decrypt",
        'decryption_success': "Matagumpay na na-decrypt",
        'decryption_success_message': "Na-decrypt ang PDF at na-save sa:\n\n{0}",
        'decryption_success_voice': "Na-decrypt at na-save ang PDF.",
        'password_remove_error': "Error sa pag-alis ng password",
        'save_unencrypted': "I-save ang hindi naka-encrypt na PDF",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "I-save bilang...",
        'save_copy': "I-save ang kopya",
        'save_success': "Na-save ang PDF sa: {0}",
        'save_encrypted': "Na-save ang protektadong PDF sa: {0}",
        'save_error': "Hindi ma-save ang PDF",
        'encryption_question': "Gusto mo bang protektahan ang PDF gamit ang password?",
        'encryption_yes': "Oo",
        'encryption_no': "Hindi",
        'encryption_cancel': "Kanselahin",
        'save_cancel': "Kinansela ang pag-save",
        'save_encrypted_voice': "Na-encrypt at na-save ang file.",
        'save_success_voice': "Na-save ang PDF file nang hindi naka-encrypt.",
        'save_error_format': "Hindi ma-save ang PDF:\n{0}",
        'export_pages_success': "Matagumpay ang Pages export",
        'export_pages_error': "Nabigo ang Pages export",
        'export_pages_error_format': "Nabigo ang Pages export: {0}",
        'export_word_success': "Matagumpay ang Word export",
        'export_word_error': "Nabigo ang Word export",
        'export_word_error_format': "Nabigo ang Word export: {0}",
        'export_text_success': "Matagumpay ang text export",
        'export_text_error': "Nabigo ang text export",
        'export_text_error_format': "Nabigo ang text export: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Kailangan ang password",
        'password_enter': "Pakiusap ilagay ang password",
        'password_confirm': "Kumpirmahin ang password",
        'password_new': "Bagong password",
        'password_current': "Kasalukuyang password",
        'password_save': "I-save ang password (naka-encrypt)",
        'password_saved': "✓ Na-save ang password para sa file na ito",
        'password_wrong': "Maling password",
        'password_mismatch': "Hindi magkatugma ang mga password",
        'password_too_short': "Masyadong maikli ang password",
        'password_min_length': "Ang password ay dapat na hindi bababa sa 4 na character ang haba",
        'password_strength': "Lakas ng password",
        'password_strength_very_weak': "Napakahina",
        'password_strength_weak': "Mahina",
        'password_strength_medium': "Katamtaman",
        'password_strength_strong': "Malakas",
        'password_strength_very_strong': "Napakalakas",
        'password_char_count': "({0} character)",
        'password_match': "✓ Tugma",
        'password_no_match': "✗ Hindi tugma ang mga password",
        'password_show': "Ipakita",
        'password_hide': "Itago",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Pamahalaan ang password",
        'password_table_filename': "Pangalan ng file",
        'password_table_password': "Password",
        'password_count': "{0} naka-save na password",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Walang naka-save na password",
        'password_copied': "Kinopya ang {0} password",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Gusto mo bang tanggalin ang password para sa '{0}'?",
        'password_delete_multiple': "Gusto mo bang tanggalin ang {0} napiling password?",
        'password_delete_all_confirm': "Gusto mo bang tanggalin ang lahat ng {0} naka-save na password?",
        'password_deleted': "Tinanggal ang {0} password",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Tinanggal ang lahat ng password",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Password Generator",
        'generator_generated': "Nabuo ang password:",
        'generator_regenerate': "Bumuo muli",
        'generator_copy': "Kopyahin",
        'generator_use': "Gamitin",
        'generator_settings': "Mga Setting",
        'generator_length': "Haba:",
        'generator_group_every': "Separator bawat",
        'generator_group_chars': "character.    Separator:",
        'generator_uppercase': "Malaking titik (A-Z)",
        'generator_lowercase': "Maliit na titik (a-z)",
        'generator_digits': "Mga numero (0-9)",
        'generator_symbols': "Mga espesyal na character (!@#$%^&*)",
        'generator_exclude': "Hindi isama:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Kailangan ang master password",
        'master_password_setup': "I-set up ang master password",
        'master_password_change': "Baguhin ang master password",
        'master_password_enter': "Pakiusap ilagay ang iyong master password",
        'master_password_choose': "Pumili ng malakas na master password (hindi bababa sa 8 character)",
        'master_password_new': "Pakiusap ilagay ang iyong bagong master password",
        'master_password_confirm': "Kumpirmahin ang password",
        'master_password_authenticate': "Patunayan",
        'master_password_success': "Matagumpay na nai-set up ang master password.",
        'master_password_changed': "Matagumpay na nabago ang master password.",
        'master_password_removed': "Tinanggal ang master password at lahat ng password.",
        'master_password_remove': "Alisin ang master password",
        'master_password_remove_confirm': "TIYAK ka bang gusto mong tanggalin ang LAHAT ng password?\n\nAng pagkilos na ito ay HINDI NA MABABALIK!",
        'master_password_export_before': "Gusto mo bang mag-export ng backup na kopya bago?",
        'master_password_export_delete': "I-export at tanggalin",
        'master_password_delete_now': "Tanggalin ngayon",
        'master_password_for_signatures': "Upang magamit ang mga lagda, kailangan mong mag-set up ng master password.\n\nGusto mo bang mag-set up ng master password ngayon?",
        'master_password_for_private': "Upang magamit ang mga pribadong text block, kailangan mong mag-set up ng master password.\n\nGusto mo bang mag-set up ng master password ngayon?",
        'master_password_info': """
            <b>🔐 WALANG MASTER PASSWORD:</b><br>
            • Hindi posible ang pagtingin, pagkopya at pag-export ng mga password<br>
            • Laging posible ang pagtanggal ng mga password (kahit walang master password)<br><br>

            <b>🔐 MAY MASTER PASSWORD:</b><br>
            • Available ang lahat ng function pagkatapos ng authentication<br>
            • Ang mga password ay naka-encrypt gamit ang master password<br>
            • Minimum na haba: 8 character<br>
            • Ligtas na SHA-256 hash storage<br><br>

            <b>MAHALAGA:</b><br>
            • Kung mawala ang master password: Hindi na mababawi ang mga password<br>
            • Kapag tinanggal ang master password: LAHAT ng password ay tatanggalin<br>
            • Available ang export option bago tanggalin<br>
            • Maaaring baguhin ang master password anumang oras
        """,
        'signature_auth_disabled': "I-disable ang pagtatanong ng password para sa mga lagda",
        'template_auth_disabled': "I-disable ang pagtatanong ng password para sa mga pribadong text block",
        'master_password_for_signatures_settings': "Upang magamit ang mga lagda, kailangan mong mag-set up ng master password.\n\nPumunta sa Mga Setting - Pamahalaan ang Password",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Protektahan ang PDF",
        'protect_info': "Ang file na '{0}' ay poprotektahan gamit ang password.",
        'protect_instruction': "Pakiusap ilagay ang gustong password nang dalawang beses upang protektahan ang dokumento, o gamitin ang password generator sa kanan ng input field.",
        'protect_success': "Matagumpay na naprotektahan at na-save ang PDF sa:\n{0}\n\nPassword: {1}\n\nGusto mo bang buksan ang protektadong PDF ngayon?",
        'protect_open': "Oo",
        'protect_skip': "Hindi",
        'protect_error': "Error sa pagprotekta ng PDF",
        'protect_open_title': "buksan ang protektadong PDF",
        'protect_question': "Tapos na. Gusto mo bang buksan ang protektadong PDF ngayon? Oo o Hindi?",
        'password_cancel': "Kinansela ang password dialog",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Burahin ang mga pahina",
        'pages_extract': "Kunin ang mga pahina",
        'pages_insert': "Ipasok ang mga pahina",
        'pages_move': "Ilipat ang mga pahina",
        'pages_delete_options': "Mga opsyon sa pagbura",
        'pages_delete_empty': "Burahin ang lahat ng walang laman na pahina",
        'pages_delete_current': "Burahin ang kasalukuyang pahina",
        'pages_delete_range': "Burahin ang hanay ng mga pahina",
        'pages_extract_options': "Mga opsyon sa pagkuha",
        'pages_extract_current': "Kunin ang kasalukuyang pahina",
        'pages_extract_range': "Kunin ang hanay ng mga pahina",
        'pages_insert_position': "Posisyon ng pagpasok",
        'pages_insert_before': "Ipasok bago ang pahina:",
        'pages_insert_select': "Pumili ng PDF",
        'pages_insert_none': "Walang napiling PDF",
        'pages_move_source': "Mga pahinang ililipat",
        'pages_move_from': "Mula sa pahina:",
        'pages_move_to': "Hanggang pahina:",
        'pages_move_target': "Target na posisyon",
        'pages_move_before': "Ilipat bago ang pahina:",
        'pages_move_hint': "Paalala: pahina 1 = simula, {0} = dulo",
        'pages_range_invalid': "Ang panimulang pahina ay dapat na mas maliit o katumbas ng panghuling pahina.",
        'pages_position_invalid': "Ang target na posisyon ay hindi maaaring nasa loob ng hanay na ililipat.",
        'pages_no_pdf_selected': "Walang napiling PDF.",
        'pages_deleted': "Tinanggal ang {0} pahina.",
        'pages_extracted': "Nakuha: {0}\nNa-save sa: {1}\nLaki ng file: {2:.1f} KB",
        'pages_inserted': "Naipasok ang {0} pahina",
        'pages_moved': "Naipasok ang {0} pahina.",
        'pages_deleted_none': "Walang pahinang tinanggal.",
        'pages_delete_progress': "Binubura ang mga pahina...",
        'pages_deleted_with_backup': "Tinanggal ang {0} pahina.\n\nBackup: {1}",
        'pages_deleted_voice': "Isang backup ang nagawa at tinanggal ang {0} pahina.",
        'info': "Paalala",
        'error_dialog_creation': "Hindi mabuo ang dialog",
        'extract_page_single': "Kunin ang pahina {0}",
        'extract_page_range': "Kunin ang mga pahina {0}-{1}",
        'extract_success_voice': "Matagumpay na nakuha ang mga pahina",
        'extract_error_format': "Error sa pagkuha: {0}",
        'pages_inserted_voice': "Naipasok ang {0} pahina.",
        'insert_error_format': "Error sa pagpasok: {0}",
        'pages_move_progress': "Inililipat ang mga pahina...",
        'pages_moved_with_backup': "Inilipat ang {0} pahina.\n\nBackup: {1}",
        'move_success_title': "Matagumpay na nailipat",
        'pages_moved_voice': "Matagumpay na nailipat ang {0} pahina",
        'mark_removed': "Tinanggal ang marka sa pahina {0}",
        'mark_empty': "Minarkahan ang pahina {0} bilang walang laman",
        'mark_export_removed': "Tinanggal ang marka ng export sa pahina {0}",
        'mark_export': "Minarkahan ang pahina {0} para i-export",
        'no_empty_pages': "Walang walang laman na pahinang minarkahan para burahin",
        'delete_empty_confirm': "Gusto mo bang burahin ang lahat ng {0} minarkahang walang laman na pahina?",
        'delete_empty_confirm_voice': "Burahin ngayon ang lahat ng {0} minarkahang walang laman na pahina? Oo o Hindi.",
        'empty_pages_deleted': "Tinanggal ang {0} walang laman na pahina",
        'no_export_pages': "Walang pahinang minarkahan para i-export",
        'overwrite_title': "I-overwrite ang umiiral na file",
        'overwrite_question': "Ang file\n\n{0}\n\nay umiiral na.\nGusto mo bang i-overwrite ito?",
        'overwrite_voice': "I-overwrite ang umiiral na file? Oo o Hindi.",
        'page_skipped': "Nilaktawan ang pahina {0}",
        'export_complete': "Tapos na ang export.",
        'export_complete_voice': "Tapos na ang export.",
        'no_pages_exported': "Walang pahinang na-export",
        'export_cancelled': "Kinansela ang export",
        'pages_exported': "Na-export ang {0} pahina sa {1}",
        'export_page_title': "I-export ang pahina",
        'page_exported': "Na-export ang pahina {0} sa {1}",
        'export_error': "Error sa pag-export",
        'export_marked_title': "I-export ang mga minarkahang pahina",
        'rotate_all_title': "paikutin ang lahat ng pahina",
        'rotate_all_question': "Gusto mo bang paikutin ang lahat ng pahina ng 90 degrees pakanan?",
        'rotate_all_voice': "Gusto mo bang paikutin ang lahat ng pahina ng 90 degrees pakanan? Oo o Hindi?",
        'all_pages_rotated': "Naikot ang lahat ng pahina",
        'page_rotated': "Naikot ang pahina {0}",
        'rotate_error': "Hindi maikot ang pahina",
        'delete_page_confirm': "Gusto mo bang burahin ang pahina {0}?",
        'delete_page_confirm_voice': "Gusto mo bang tanggalin ang pahina {0}? Oo o Hindi.",
        'page_deleted': "Tinanggal ang pahina {0}",
        'delete_error': "Hindi matanggal ang pahina",
        'pages_deleted_voice': "Tinanggal ang {0} pahina",
        'pages_exported_split': "Matagumpay na na-export ang {0} pahina.",
        'pages_skipped': "Nilaktawan ang {0} pahina.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Kunin ang mga pahina (advanced)",
        'pdf_splitter_title': "PDF Splitter at Extractor",
        'pdf_splitter_load': " Pumili ng PDF file",
        'pdf_splitter_info': "Pakiusap pumili ng opsyon para sa iyong PDF dokumento",
        'pdf_splitter_basic': "Mga pangunahing operasyon",
        'pdf_splitter_single': "Hatiin sa indibidwal na pahina",
        'pdf_splitter_range': "Kunin ang mga pahina:",
        'pdf_splitter_range_placeholder': "hal. 1-3,5,7-9",
        'pdf_splitter_clean': "Mga operasyon sa paglilinis",
        'pdf_splitter_remove_empty': "Alisin ang lahat ng walang laman na pahina",
        'pdf_splitter_remove': "Burahin ang hanay ng mga pahina:",
        'pdf_splitter_remove_placeholder': "hal. 2,4-6",
        'pdf_splitter_process': "Iproseso ang PDF",
        'pdf_splitter_loaded': "Na-load ang PDF. Pakiusap pumili ng opsyon",
        'pdf_read_error': "Hindi mabasa ang PDF",
        'pages': "Mga pahina",
        'pages_created': "Nagawang mga pahina",
        'range_empty': "Pakiusap maglagay ng hanay ng mga pahina",
        'range_invalid': "Hindi wastong hanay ng mga pahina",
        'range_created': "Nagawang bagong PDF kasama ang napiling mga pahina:\n{0}",
        'empty_removed': "Tinanggal ang {0} walang laman na pahina.\nOutput: {1}",
        'remove_empty': "Pakiusap maglagay ng mga pahinang aalisin",
        'remove_invalid': "Hindi wastong mga pahinang aalisin",
        'remove_done': "Nagawang nalinis na PDF:\n{0}",
        'open_folder': "Buksan ang folder",
        'show_in_finder': "Ipakita sa Finder",
        'pdf_splitter_no_pdf': "Pakiusap i-load muna ang PDF file.",
        'process_error': "Error sa pagproseso ng PDF",
        'pages_created_voice': "Nagawang {0} pahina",
        'range_created_voice': "Nagawang PDF kasama ang napiling mga pahina",
        'empty_removed_voice': "Tinanggal ang {0} walang laman na pahina",
        'remove_done_voice': "Nagawang nalinis na PDF",
        'pdf_splitter_split_groups': "Bawat magkakasunod na grupo sa hiwalay na file",
        'range_created_single': "Nagawang bagong PDF:\n{0}",
        'range_created_multiple': "Nagawang {0} PDF file.",
        'range_created_voice_single': "Nagawang isang PDF kasama ang napiling mga pahina",
        'range_created_voice_multiple': "Nagawang {0} PDF file",
        'empty_removed_none_left': "Walang natirang pahina",
        'empty_removed_all_empty': "Lahat ng pahina ay nakilala bilang walang laman at tatanggalin. Walang file na nagawa.",
        'preview_single': "Preview: {0}",
        'preview_enter_range': "Pakiusap maglagay ng hanay ng mga pahina.",
        'preview_invalid_range': "Hindi wastong hanay ng mga pahina.",
        'preview_file': "Preview: {0}",
        'preview_files': "Preview: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Sinisimulan ang proseso ng pag-print",
        'print_sent': "Naipadala ang print job",
        'print_now': "I-print ngayon",
        'print_error': "Error sa agarang pag-print",
        'print_limited': "Limitado ang print function sa system na ito",
        'print_error_format': "Error sa agarang pag-print: {0}",
        'warning': "Paalala",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Lumipat sa Light Mode",
        'mode_switch_to_dark': "Lumipat sa Dark Mode",
        'mode_dark_activated': "Na-activate ang Dark Mode",
        'mode_light_activated': "Na-activate ang Light Mode",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Buong tanawin",
        'zoom_two_pages': "Dalawang pahina magkatabi",
        'zoom_overview': "Overview mode",
        'zoom_cannot_during_search': "Hindi ma-zoom habang naghahanap",
        'zoom_exit_first': "Pakiusap lumabas muna sa zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Na-activate ang Drag & Drop",
        'drag_disabled': "Na-deactivate ang Drag & Drop",
        'drag_page_grab': "Kunin ang pahina {0}",
        'drag_page_dropped': "Naipasok ang pahina {0} sa posisyon {1}",
        'drag_position_invalid': "Hindi wastong posisyon",
        'drag_same_position': "Ang pahina {0} ay nananatili sa posisyon {0}",
        'drag_error': "Error sa paglipat",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Text input na may advanced na pag-format at pamamahala ng text block",
        'text_templates': "Available na text block:",
        'text_name': "Pangalan",
        'text_preview': "Preview ng text",
        'text_enter': "Text:",
        'text_font_size': "Laki ng font:",
        'text_formatting': "Pag-format:",
        'text_bold': "Makapal",
        'text_italic': "Nakasandal",
        'text_underline': "May guhit",
        'text_alignment': "Pag-align:",
        'text_left': "Kaliwa",
        'text_center': "Gitna",
        'text_right': "Kanana",
        'text_color': "Kulay ng text:",
        'text_opacity': "Opisidad:",
        'text_word_wrap': "Line break:",
        'text_auto': "Awtomatiko",
        'text_page_width_95': "Lapad ng pahina (95%)",
        'text_page_width_85': "Napakalawak (85%)",
        'text_page_width_75': "Malawak (75%)",
        'text_page_width_60': "Malawak (60%)",
        'text_page_width_50': "Katamtaman (50%)",
        'text_page_width_30': "Makipot (30%)",
        'text_page_width_20': "makipot (20%)",
        'text_page_width_10': "Napakamakipot (10%)",
        'text_no_wrap': "Walang break",
        'text_private': "Pribadong text block (kailangan ng authentication)",
        'text_preview_label': "Preview:",
        'text_preview_placeholder': "Dito ipapakita ang preview ng text...",
        'text_no_text': "(Walang text)",
        'text_save_template': "💾 I-save bilang block",
        'text_delete_template': "🗑 Burahin ang napiling text block",
        'text_show_private': "Ipakita ang pribado",
        'text_hide_private': "Itago ang pribado",
        'text_use': "✅ Gamitin ang text",
        'text_saved': "Na-save ang text block bilang:\n{0}",
        'text_saved_voice': "Na-save ang text block",
        'text_deleted': "Tinanggal ang text block",
        'text_no_text_to_save': "Walang text na ise-save.",
        'text_no_templates': "Walang nakitang text block",
        'text_private_master_required': "Magagamit lamang ang mga pribadong block kung naka-set up ang master password.\n\nGusto mo bang mag-set up ng master password ngayon?",
        'text_filename': "Pangalan ng file para sa text block (walang 'Text_' at '.txt'):",
        'text_filename_hint': "Halimbawa: 'Telefon HomeOffice' ay ise-save bilang 'Text_Telefon HomeOffice.txt'",
        'text_save_hint': "Awtomatikong ise-save ang text block kasama ang pag-format.",
        'text_guide_title': "Text Input - Gabay",
        'text_delete_confirm': "Gusto mo bang tanggalin ang text block?\n\nFile: {0}\nText: {1}...",
        'text_make_public': "Markahan bilang pampubliko",
        'text_make_private': "Markahan bilang pribado",
        'text_privacy_changed': "Binago ang katayuan ng privacy",
        'text_private_always': "Laging nakikita ang pribado (setting)",
        'text_mode_required': "Pakiusap i-activate muna ang text mode",
        'text_continue_editing': "Magpatuloy sa pag-edit - Cursor sa dulo ng text",
        'text_no_input': "Walang text na nailagay - itinapon ang text",
        'save_dialog_question': "Paano mo gustong magpatuloy?",
        'text_save_question': "I-save ang lahat ng text at krus, ayusin, magpatuloy sa pag-edit o itapon?",
        'copy_cross': "Kinopya ang krus",
        'paste_cross': "Idinikit ang krus",
        'paste_text': "Idinikit ang text",
        'cross_discarded': "Itinapon ang krus",
        'all_discarded': "Itinapon ang lahat",
        'text_discarded': "Itinapon ang text",
        'no_texts_to_save': "Walang text na ise-save",
        'no_valid_texts': "Walang wastong text na ise-save",
        'text_word_singular': "Text",
        'text_word_plural': "Mga text",
        'cross_word_singular': "Krus",
        'cross_word_plural': "Mga krus",
        'texts_saved_title': "Na-save ang mga text",
        'texts_crosses_saved': "{0} {1} at {2} {3} ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'texts_crosses_saved_voice': "{0} {1} at {2} {3} na-save.",
        'texts_saved': "{0} {1} ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'texts_saved_voice': "{0} {1} na-save.",
        'crosses_saved': "{0} {1} ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'crosses_saved_voice': "{0} {1} na-save.",
        'elements_saved': "{0} elemento ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'elements_saved_voice': "{0} elemento na-save.",
        'text_window_load_error': "Hindi ma-load ang text window",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Text Input at Text Block – Detalyadong Gabay**

        **1. Magpasok at mag-edit ng text**
        - Mag-right-click sa gustong lugar sa dokumento at piliin ang "Magpasok ng text".
        - Magbubukas ang isang dialog kung saan maaari mong i-type at i-format ang iyong text:
        • Laki ng font, bold, italic, underline
        • Kulay ng text (malayang mapipili)
        • Opisidad sa pamamagitan ng slider
        • Line break (iba't ibang lapad, hal. lapad ng pahina, makipot, walang break)
        - Pagkatapos ng kumpirmasyon, lilitaw ang text sa pinag-click na posisyon. Maaari mo itong ilipat gamit ang mouse o arrow keys.
        - Ang double-click sa text ay nagbubukas ng edit mode; lumabas gamit ang ESC.

        **2. Pamahalaan ang mga text block (Template)**
        - Sa text dialog makikita mo sa kaliwa ang listahan ng lahat ng na-save na text block.
        - **Pag-save ng block:** I-type ang iyong text, i-format ito at i-click ang "💾 I-save bilang block". Maglagay ng pangalan ng file (walang extension).
        - **Pag-load ng block:** I-click ang gustong pangalan sa listahan. Ang text at pag-format ay kukunin at maaaring ayusin kung kinakailangan.
        - **Pagbura:** Sa pamamagitan ng right-click sa isang block maaari mo itong burahin o baguhin ang pribadong katayuan nito.

        **3. Pribadong text block (Master Password)**
        - Kung nag-set up ka ng master password (sa ilalim ng Mga Setting → Pamahalaan ang Password), maaari mong markahan ang mga block bilang "pribado".
        - I-activate ang checkbox na "Pribadong text block" sa dialog bago mag-save.
        - Ang mga pribadong block ay ipapakita lamang sa listahan kung ilalagay mo ang iyong master password nang isang beses bawat session (authentication sa pamamagitan ng lock icon o sa unang pag-access).
        - Sa ganitong paraan mapoprotektahan mo ang mga kumpidensyal na text block laban sa hindi awtorisadong pag-access.

        **4. Magpasok ng krus**
- Sa pamamagitan ng context menu maaari ka ring magpasok ng graphical na krus (hal. para sa mga checkbox).
        - Ang laki, kapal ng linya at kulay ng mga krus ay maaari mong ayusin nang pandaigdigan sa mga setting (Menu "Mga Setting" → "Cross Settings").
        - Sa pamamagitan ng right-click sa isang umiiral na krus maaari mo itong baguhin nang paisa-isa.

        **5. Mga batch action**
        - Kung naglagay ka ng maraming text o krus sa isang pahina, maaari mong i-save o itapon ang lahat ng elemento nang magkasama sa pamamagitan ng context menu (right-click sa text mode).
        - Kapag nag-save, lahat ng elemento ay naka-embed sa PDF at nananatili bilang vector graphics.

        **6. Keyboard shortcuts sa text mode**
        - Arrow keys: Ilipat ang elemento
        - Ctrl+arrow keys: Mas malalaking hakbang
        - Enter: Buksan ang save dialog (i-save lahat / ayusin / itapon)
        - ESC: Itapon ang kasalukuyang elemento
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Text Input at Text Block – Detalyadong Gabay</strong></p>

        <p><strong>1. Magpasok at mag-edit ng text</strong></p>
        <ul>
        <li>Mag-right-click sa gustong lugar sa dokumento at piliin ang "Magpasok ng text".</li>
        <li>Magbubukas ang isang dialog kung saan maaari mong i-type at i-format ang iyong text:<br/>
        • Laki ng font, bold, italic, underline<br/>
        • Kulay ng text (malayang mapipili)<br/>
        • Opisidad sa pamamagitan ng slider<br/>
        • Line break (iba't ibang lapad, hal. lapad ng pahina, makipot, walang break)</li>
        <li>Pagkatapos ng kumpirmasyon, lilitaw ang text sa pinag-click na posisyon. Maaari mo itong ilipat gamit ang mouse o arrow keys.</li>
        <li>Ang double-click sa text ay nagbubukas ng edit mode; lumabas gamit ang ESC.</li>
        </ul>

        <p><strong>2. Pamahalaan ang mga text block (Template)</strong></p>
        <ul>
        <li>Sa text dialog makikita mo sa kaliwa ang listahan ng lahat ng na-save na text block.</li>
        <li><strong>Pag-save ng block:</strong> I-type ang iyong text, i-format ito at i-click ang "💾 I-save bilang block". Maglagay ng pangalan ng file (walang extension).</li>
        <li><strong>Pag-load ng block:</strong> I-click ang gustong pangalan sa listahan. Ang text at pag-format ay kukunin at maaaring ayusin kung kinakailangan.</li>
        <li><strong>Pagbura:</strong> Sa pamamagitan ng right-click sa isang block maaari mo itong burahin o baguhin ang pribadong katayuan nito.</li>
        </ul>

        <p><strong>3. Pribadong text block (Master Password)</strong></p>
        <ul>
        <li>Kung nag-set up ka ng master password (sa ilalim ng Mga Setting → Pamahalaan ang Password), maaari mong markahan ang mga block bilang "pribado".</li>
        <li>I-activate ang checkbox na "Pribadong text block" sa dialog bago mag-save.</li>
        <li>Ang mga pribadong block ay ipapakita lamang sa listahan kung ilalagay mo ang iyong master password nang isang beses bawat session (authentication sa pamamagitan ng lock icon o sa unang pag-access).</li>
        <li>Sa ganitong paraan mapoprotektahan mo ang mga kumpidensyal na text block laban sa hindi awtorisadong pag-access.</li>
        </ul>

        <p><strong>4. Magpasok ng krus</strong></p>
        <ul>
        <li>Sa pamamagitan ng context menu maaari ka ring magpasok ng graphical na krus (hal. para sa mga checkbox).</li>
        <li>Ang laki, kapal ng linya at kulay ng mga krus ay maaari mong ayusin nang pandaigdigan sa mga setting (Menu "Mga Setting" → "Cross Settings").</li>
        <li>Sa pamamagitan ng right-click sa isang umiiral na krus maaari mo itong baguhin nang paisa-isa.</li>
        </ul>

        <p><strong>5. Mga batch action</strong></p>
        <ul>
        <li>Kung naglagay ka ng maraming text o krus sa isang pahina, maaari mong i-save o itapon ang lahat ng elemento nang magkasama sa pamamagitan ng context menu (right-click sa text mode).</li>
        <li>Kapag nag-save, lahat ng elemento ay naka-embed sa PDF at nananatili bilang vector graphics.</li>
        </ul>

        <p><strong>6. Keyboard shortcuts sa text mode</strong></p>
        <ul>
        <li>Arrow keys: Ilipat ang elemento</li>
        <li>Ctrl+arrow keys: Mas malalaking hakbang</li>
        <li>Enter: Buksan ang save dialog (i-save lahat / ayusin / itapon)</li>
        <li>ESC: Itapon ang kasalukuyang elemento</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Cross Settings",
        'cross_properties': "Mga Katangian ng Krus",
        'cross_size': "Laki (px):",
        'cross_line_width': "Kapal ng linya:",
        'cross_color': "Kulay:",
        'cross_choose_color': "Pumili",
        'cross_fine_tuning': "Pinong pag-aayos kapag nagse-save (pixel)",
        'cross_offset_x': "X-Offset:",
        'cross_offset_y': "Y-Offset:",
        'cross_offset_x_tooltip': "Ang mga negatibong halaga ay naglilipat ng krus sa kaliwa kapag nagse-save, ang mga positibo sa kanan",
        'cross_offset_y_tooltip': "Ang mga negatibong halaga ay naglilipat ng krus pataas kapag nagse-save, ang mga positibo pababa",
        'cross_preview': "Preview",
        'cross_save': "Ilapat ang mga setting",
        'cross_customized': "Inayos ang krus",
        'cross_settings_applied': "Na-save ang cross settings.\nLaki: {0}px, Kapal ng linya: {1}px\n{2}",
        'cross_updated_count': "Na-update ang {0} umiiral na krus.",
        'cross_no_crosses': "Walang nakitang umiiral na krus.",
        'cross_settings_applied_all': "Inilapat ang cross settings sa lahat ng {0} krus",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Mga Setting ng Lagda",
        'signature_1': "Lagda 1",
        'signature_2': "Lagda 2",
        'signature_select': "Pumili ng lagda",
        'signature_add': "➕ Magdagdag ng bagong lagda...",
        'signature_size': "Laki para sa lagda {0} (%):",
        'signature_common': "Pangkalahatang Setting",
        'signature_timestamp': "Awtomatikong magdagdag ng timestamp",
        'signature_location': "Default na lokasyon:",
        'signature_timestamp_size': "Laki ng font ng timestamp:",
        'signature_no_files': "-- Walang nakitang lagda --",
        'signature_insert': "Magpasok ng lagda",
        'signature_insert_1': "Magpasok ng lagda 1",
        'signature_insert_2': "Magpasok ng lagda 2",
        'signature_customize': " Ayusin ang lagda",
        'signature_discard': " Itapon ang lagdang ito",
        'signature_save_all': " I-save ang lahat ng lagda",
        'signature_discard_all': " Itapon ang lahat ng lagda",
        'signature_guide_title': "Mga Lagda - Gabay",
        'signature_guide': """
📝 Mga Lagda - Maikling Gabay

- Mag-set up ng master password
- I-configure ang mga lagda sa menu ng Mga Setting
  (laki, timestamp ...)
- Ipasok sa pamamagitan ng RIGHT-CLICK sa gustong posisyon
  (kailangan ang master password isang beses bawat session)
- Ilipat ang lagda gamit ang mouse o arrow keys
- Maaaring magpasok ng maraming lagda nang sunud-sunod
- Maaaring ayusin ang bawat lagda nang paisa-isa
- Itapon ang isang lagda
- I-save / itapon ang lahat ng lagda nang sabay-sabay
- Bilang kahalili, maaari ring gamitin ang menu bar.
        """,
        'signature_placeholder': "Walang available na preview",
        'signature_info': "Lagda {0}: {1}×{2} px ({3}% ng {4}×{5})",
        'signature_info_placeholder': "Mga setting para sa lagda {0}",
        'signature_inserted': "Naipasok ang lagda {0} sa pahina {1}",
        'signature_deleted': "Tinanggal ang lagda",
        'signature_copied': "Kinopya ang lagda",
        'signature_pasted': "Naipasok ang lagda {0}",
        'signature_saved': "{0} lagda ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'signature_saved_voice': "{0} lagda na-save",
        'mode_replace_signature_format': "Tapusin ang mode at ipasok ang lagda {0}",
        'mode_conflict_voice_signature': "Aktibo ang {0} mode. Tapusin at ipasok ang lagda?",
        'signature_not_configured': "Hindi naka-configure ang lagda {0}",
        'signature_file_not_found': "Hindi mahanap ang lagda file",
        'timestamp_format': "{0}, noong {1}",
        'no_copied_signature': "Walang nakopyang lagda",
        'no_signatures_to_save': "Walang lagda na ise-save",
        'signature_save_question': "I-save ang lahat ng lagda, ayusin o itapon ito?",
        'signatures_saved_title': "Na-save ang mga lagda",
        'signatures_saved': "{0} lagda ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'signatures_saved_voice': "{0} lagda na-save.",
        'all_signatures_discarded': "Itinapon ang lahat ng lagda",
        'signature_settings_saved': "Na-save ang signature settings",
        'signature_cancelled': "Itinapon ang lagda",
        'signature_active_title': "Aktibo ang lagda",
        'signature_replace_question': "Mayroon nang aktibong lagda.\n\nGusto mo bang palitan ang kasalukuyang lagda?",
        'signature_replace': "Palitan ang lagda",
        'signature_replace_voice': "Palitan ang kasalukuyang lagda o kanselahin?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Mga Setting ng Larawan",
        'image_common': "Pangkalahatang Setting ng Larawan",
        'image_keep_aspect': "Panatilihin ang aspect ratio kapag nagda-drag",
        'image_default_size': "Default na laki (%):",
        'image_dark_invert': "Baligtarin ang mga larawan sa Dark Mode",
        'image_dark_invert_tooltip': "Naka-activate: Ang mga larawan ay babaligtarin para sa mas mahusay na visibility",
        'image_fine_tuning': "Pinong pag-aayos (pixel)",
        'image_offset_x': "X-Offset:",
        'image_offset_y': "Y-Offset:",
        'image_offset_x_tooltip': "Ang mga negatibong halaga ay naglilipat ng larawan sa kaliwa kapag nagse-save, ang mga positibo sa kanan",
        'image_offset_y_tooltip': "Ang mga negatibong halaga ay naglilipat ng larawan pataas kapag nagse-save, ang mga positibo pababa",
        'image_select': "Pumili ng larawan",
        'image_insert': "Magpasok ng larawan",
        'image_customize': " Ayusin ang larawan",
        'image_aspect': " Panatilihin ang aspect ratio",
        'image_discard': " Itapon ang larawang ito",
        'image_save_all': " I-save ang lahat ng larawan",
        'image_discard_all': " Itapon ang lahat ng larawan",
        'image_filter': "Mga Larawan",
        'image_guide_title': "Magpasok ng larawan - Gabay",
        'image_guide': """
📷 Magpasok ng larawan sa PDF - Maikling Gabay:

1. Mag-right-click sa gustong posisyon
2. "Magpasok ng larawan" → Pumili ng larawan
3. Iposisyon ang larawan: I-drag gamit ang mouse
4. Ayusin ang laki: I-drag sa mga sulok/gilid
5. Panatilihin ang aspect ratio: [A] key
6. Karagdagang pagsasaayos: Right-click sa larawan

Tip: Sa context menu maaari mong ayusin ang mga setting.
        """,
        'image_inserted': "Naipasok ang larawan {0} sa pahina {1}",
        'image_deleted': "Itinapon ang larawan",
        'image_copied': "Kinopya ang larawan",
        'image_pasted': "Naipasok ang larawan",
        'image_saved': "{0} larawan ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'image_saved_voice': "{0} larawan na-save",
        'image_aspect_on': "naka-activate",
        'image_aspect_off': "naka-deactivate",
        'image_aspect_toggle': "Panatilihin ang aspect ratio {0}",
        'image_reset': "I-reset ang larawan sa orihinal na laki",
        'image_replaced': "Pinalitan ang larawan",
        'image_invalid': "Walang wastong larawan",
        'mode_replace_image': "Magpasok ng larawan",
        'mode_conflict_voice_image': "Aktibo ang {0} mode. Tapusin at ipasok ang larawan?",
        'image_active_title': "Aktibo ang larawan",
        'image_replace_question': "Mayroon nang aktibong larawan.\n\nGusto mo bang palitan ang kasalukuyang larawan?",
        'image_replace': "Palitan ang larawan",
        'image_replace_voice': "Palitan ang kasalukuyang larawan o kanselahin?",
        'image_filter_all': "Mga Larawan (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Lahat ng file (*.*)",
        'no_copied_image': "Walang nakopyang larawan",
        'image_discarded': "Itinapon ang larawan",
        'image_save_question': "I-save ang lahat ng larawan, ayusin o itapon ito?",
        'no_images_to_save': "Walang larawan na ise-save",
        'no_valid_images': "Walang wastong larawan na ise-save",
        'images_saved_title': "Na-save ang mga larawan",
        'images_saved': "{0} larawan ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'images_saved_voice': "{0} larawan na-save.",
        'all_images_discarded': "Itinapon ang lahat ng larawan",
        'image_settings_updated': "Na-update ang mga setting ng larawan",
        'image_replace_title': "Pumili ng bagong larawan",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Mga Setting ng Hugis",
        'form_basic': "Pangunahing Setting",
        'form_default_type': "Default na uri ng hugis:",
        'form_rectangle': "Parihaba",
        'form_ellipse': "Ellipse",
        'form_line': "Linya",
        'form_arrow': "Palaso",
        'form_line_width': "Kapal ng linya:",
        'form_colors': "Mga Kulay",
        'form_line_color': "Kulay ng linya:",
        'form_fill_color': "Kulay ng punan:",
        'form_choose_color': "Pumili",
        'form_transparent': "Transparent na background (linya lamang)",
        'form_filled': "napuno",
        'form_dark_mode': "Dark Mode",
        'form_dark_invert': "Baligtarin ang mga kulay sa Dark Mode",
        'form_fine_tuning': "Pinong pag-aayos (pixel)",
        'form_offset_x': "X-Offset:",
        'form_offset_y': "Y-Offset:",
        'form_offset_x_tooltip': "Ang mga negatibong halaga ay naglilipat ng hugis sa kaliwa kapag nagse-save, ang mga positibo sa kanan",
        'form_offset_y_tooltip': "Ang mga negatibong halaga ay naglilipat ng hugis pataas kapag nagse-save, ang mga positibo pababa",
        'form_preview': "Preview",
        'form_insert': "Magpasok ng hugis",
        'form_rectangle_insert': "Parihaba",
        'form_ellipse_insert': "Ellipse/Bilog",
        'form_line_insert': "Linya (2 click)",
        'form_arrow_insert': "Palaso (2 click)",
        'form_customize': " Ayusin ang hugis",
        'form_transparent_toggle': " Transparent na background",
        'form_discard': " Itapon ang hugis na ito",
        'form_save_all': " I-save ang lahat ng hugis",
        'form_discard_all': " Itapon ang lahat ng hugis",
        'form_guide_title': "Magpasok ng hugis - Gabay",
        'form_guide': """
📐 Magpasok ng hugis sa PDF - Maikling Gabay:

1. Piliin ang uri ng hugis (Parihaba, Ellipse, Linya, Palaso)
2. Mag-click sa posisyon
   - Para sa Parihaba/Ellipse: Isang click ang naglalagay ng hugis
   - Para sa Linya/Palaso: Dalawang click para sa simula at dulo
3. Iposisyon ang hugis: I-drag gamit ang mouse
4. Ayusin ang laki: I-drag sa mga sulok/gilid
5. I-save ang hugis: Enter
6. Itapon ang hugis: ESC
7. Karagdagang pagsasaayos: Right-click sa hugis

Tip: Sa context menu maaari mong ayusin ang mga setting.
        """,
        'form_inserted': "{0} naipasok sa pahina {1}",
        'form_deleted': "Tinanggal ang hugis",
        'form_copied': "Kinopya ang hugis",
        'form_pasted': "Naipasok ang hugis",
        'form_saved': "{0} hugis ay naipasok sa PDF.\n\nMuling nilo-load ang PDF...",
        'form_saved_voice': "{0} hugis na-save",
        'form_reset': "I-reset ang hugis sa default na laki",
        'form_transparent_on': "naka-activate",
        'form_transparent_off': "naka-deactivate",
        'form_transparent_toggled': "Transparent na background {0}",
        'form_line_cancel': "Kinansela ang pagguhit ng linya",
        'form_second_click': "Ngayon i-click ang endpoint para sa {0}",
        'mode_replace_form': "Magpasok ng hugis",
        'mode_conflict_voice_form': "Aktibo ang {0} mode. Tapusin at magpasok ng hugis?",
        'form_settings_updated': "Na-update ang mga setting ng hugis",
        'form_unknown': "Hugis",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Mag-click sa panimulang posisyon",
        'form_line_guide_2': "2. Mag-click sa dulo na posisyon",
        'form_line_guide_3': "Ang linya ay iguguhit sa pagitan ng dalawang punto.",
        'form_line_status_1': "Naghihintay ng unang click...",
        'form_line_status_2': "Naitakda ang unang punto: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Ngayon i-click ang endpoint...",
        'form_line_status_4': "Naitakda ang parehong punto.\nI-click ang 'Tapos' upang i-save.",
        'form_line_reset': "I-reset",
        'form_line_finish': "Tapos",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopyahin (Cmd+C)",
        'paste': "Idikit (Cmd+V)",
        'copied': "Kinopya: {0}",
        'no_element_to_copy': "Walang napiling elementong kokopyahin",
        'no_copied_data': "Walang nakopyang data",
        'no_valid_position': "Walang wastong posisyon para idikit",
        'copy_text': "Kinopya ang text",
        'copy_image': "Kinopya ang larawan",
        'copy_form': "Kinopya ang hugis",
        'copy_signature': "Kinopya ang lagda",
        'element_text': "Text",
        'element_image': "Larawan",
        'element_form': "Hugis",
        'element_signature': "Lagda",
        'element_unknown': "Elemento",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Salungatan sa mode",
        'mode_conflict_message': "Aktibo na ang '{0}' mode.\n\nGusto mo bang tapusin ito at {1}?",
        'mode_replace': "Tapusin ang mode at {0}",
        'mode_cancel': "Kanselahin",
        'mode_replace_text': "Magpasok ng text",
        'mode_replace_cross': "Magpasok ng krus",
        'mode_replace_signature': "Magpasok ng lagda",
        'mode_replace_image': "Magpasok ng larawan",
        'mode_replace_form': "Magpasok ng hugis",
        'mode_conflict_voice': "Aktibo ang {0} mode. Tapusin at magpasok ng text?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Text Input",
        'active_mode_signature': "Lagda",
        'active_mode_image': "Larawan",
        'active_mode_form': "Hugis",
        'active_mode_and': " at ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Magpasok",                    # Hauptmenü
        'insert_another_text': "Magpasok ng text",          # Vereinfacht
        'insert_another_cross': "Magpasok ng krus",        # Vereinfacht
        'insert_another_signature_1': "Lagda 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Lagda 2",      # Untermenü-Eintrag
        'insert_another_image': "Magpasok ng larawan",         # Vereinfacht
        'insert_another_form_rect': "Parihaba",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Linya (2 click)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Palaso (2 click)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "I-save ang {0}",
        'save_dialog_message': "Ang {0} ay ise-save sa pahina {1}.\n\nPaano mo gustong magpatuloy?",
        'save_all': "I-save ang lahat ng {0}",
        'save_single': "I-save ang {0}",
        'save_customize': "Ayusin ang {0}",
        'save_discard': "Itapon ang {0} na ito",
        'save_continue': "Magpatuloy sa pag-edit",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Pumunta sa pahina {0}",
        'context_rotate': " Iikot ang pahina {0}",
        'context_delete': " Burahin ang pahina {0}",
        'context_export': " I-export ang pahina {0}",
        'context_mark_as': " Markahan ang pahina bilang...",
        'context_mark_empty': " Walang laman na pahina",
        'context_unmark_empty': " Hindi na walang laman",
        'context_mark_export': " Markahan para i-export",
        'context_unmark_export': " Huwag nang i-export",
        'context_batch_actions': " Mga batch action",
        'context_batch_delete_empty': " Burahin ang lahat ng {0} walang laman na pahina",
        'context_batch_export_single': " Lahat ng {0} pahina (isang file)",
        'context_batch_export_split': " Lahat ng {0} pahina (hiwalay)",
        'context_drag_start': " Simulan ang Drag & Drop",
        'context_drag_stop': " Tapusin ang Drag & Drop",
        'context_insert': " Magpasok",
        'context_insert_pages': " Magpasok ng mga pahina",
        'context_zoom': "Zoom",
        'discard_mixed': "Itapon ang lahat ng {0} {1} at {2} {3}",
        'save_mixed': "I-save ang {0} {1} at {2} {3}",
        'discard_texts': "Itapon ang lahat ng {0} text",
        'discard_text_single': "Itapon ang 1 text",
        'save_texts': "I-save ang {0} text",
        'save_text_single': "I-save ang 1 text",
        'discard_crosses': "Itapon ang lahat ng {0} krus",
        'discard_cross_single': "Itapon ang 1 krus",
        'save_crosses': "I-save ang {0} krus",
        'save_cross_single': "I-save ang 1 krus",
        'discard_signatures': "Itapon ang lahat ng {0} lagda",
        'save_signature_single': "I-save ang 1 lagda",
        'save_signatures': "I-save ang {0} lagda",
        'discard_images': "Itapon ang lahat ng {0} larawan",
        'save_image_single': "I-save ang 1 larawan",
        'save_images': "I-save ang {0} larawan",
        'discard_forms': "Itapon ang lahat ng {0} hugis",
        'save_form_single': "I-save ang 1 hugis",
        'save_forms': "I-save ang {0} hugis",
        'cross_discard': "Itapon ang krus na ito",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Impormasyon sa Pag-export / Pag-import",
        'export_what': "📋 Ano ang nae-export?",
        'export_general': "Pangkalahatang Setting",
        'export_general_items': "• Speech output (on/off, bilis)\n• Dark/Light Mode\n• Backup settings\n• OCR settings",
        'export_image_form': "Mga Setting ng Larawan at Hugis",
        'export_image_form_items': "• Mga setting ng larawan (aspect ratio, default na laki)\n• Mga setting ng hugis (kapal ng linya, kulay)\n• Mga setting ng lagda (path, laki, timestamp)",
        'export_passwords': "Database ng Password",
        'export_passwords_items': "• Lahat ng naka-save na PDF password\n• Opsyonal na naka-encrypt o na-decrypt",
        'export_master': "Mga Setting ng Master Password",
        'export_master_items': "• Master password hash\n• Mga setting para sa mga lagda/text block",
        'export_signatures': "Mga Lagda at Text Block",
        'export_signatures_items': "• Lahat ng image file (mga lagda)\n• Lahat ng text block na may pag-format\n• Mga markang pribado/publiko",
        'export_import_warning': "⚠️ Mahahalagang Paalala",
        'export_import_note': "• Kapag nag-import, lahat ng kasalukuyang setting ay mai-overwrite\n• Kailangan i-restart ang application\n• Ang mga umiiral na lagda/text block ay papalitan",
        'export_master_note': "• Kapag naka-set ang master password maaari kang pumili:\n  - Na-decrypt (mga password sa plain text)\n  - Naka-encrypt (mababasa lamang gamit ang master password)",
        'export_security': "• Ang na-export na ZIP file ay naglalaman ng sensitibong data\n• Pakiusap itago nang ligtas (hal. naka-encrypt na USB stick)\n• Kung mawala ang file: Hindi na mababawi ang mga password",
        'export_format': "📁 Format ng Pag-export",
        'export_format_desc': "Ang mga setting ay ise-save sa isang ZIP file:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Matagumpay na na-export ang mga setting",
        'export_failed': "Nabigo ang pag-export",
        'export_import_question': "Gusto mo bang i-restart ang application ngayon?",
        'export_password_question': "Naka-set ang master password.\n\nGusto mo bang i-export ang mga password na na-decrypt?\n(kung hindi, sila ay ie-export na naka-encrypt)",
        'export_decrypt': "I-export na na-decrypt",
        'export_encrypt': "I-export na naka-encrypt",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Impormasyon",
        'info_title': "Tungkol sa PDF Dark View",
        'info_version': "Bersyon",
        'info_author': "Binuo ni Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Tungkol",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ay isang naa-access na PDF viewer na espesyal na binuo para sa mga taong may kapansanan sa paningin.</p>

            <p><strong>Mga pangunahing tampok:</strong></p>
            <ul>
                <li>Mayamang contrast, nako-customize na interface</li>
                <li>Buong keyboard control</li>
                <li>Integrated speech output</li>
                <li>OCR para sa mga na-scan na dokumento</li>
                <li>Malawak na mga tool sa pag-edit</li>
            </ul>

            <p>Mahigit sa 50 wika ang sinusuportahan – upang ang mga PDF ay maging naa-access para sa lahat.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Mga Tampok",
        'info_features_intro': "Ang PDF Dark View ay nagbibigay sa iyo ng mga sumusunod na posibilidad:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Display at Navigation</strong> – Dark/Light Mode, pag-browse ng pahina, zoom, pagtalon sa pahina</li>
            <li><strong>OCR (Text Recognition)</strong> – Gawing mahanap at makopya ang mga na-scan na dokumento</li>
            <li><strong>Pag-edit</strong> – Magpasok ng mga text, krus, lagda, larawan at hugis</li>
            <li><strong>Pamamahala ng Pahina</strong> – Burahin, kunin, ipasok, ilipat sa pamamagitan ng Drag & Drop</li>
            <li><strong>Pag-export</strong> – Bilang Word, Pages o text</li>
            <li><strong>Seguridad</strong> – Proteksyon ng password at pamamahala</li>
            <li><strong>Accessibility</strong> – Speech output, keyboard control, mataas na contrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Operasyon",
        'info_accessibility': "♿ Accessibility – buong keyboard control",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Pangkalahatan</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Buksan ang PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Maghanap</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> I-toggle ang Dark/Light Mode</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> I-print</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Lumabas</div>

        <div class="shortcut-cat">📖 Navigation</div>
        <div class="shortcut-row"><kbd>Arrow keys</kbd> Mag-browse ng pahina sa bawat pahina</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Pumunta sa pahina</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Unang pahina</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Huling pahina</div>

        <div class="shortcut-cat">✏️ Pag-edit</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Magpasok ng text</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Burahin ang mga pahina</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Kunin ang mga pahina</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Magpasok ng mga pahina</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Ilipat ang mga pahina</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Iikot ang pahina</div>

        <div class="shortcut-cat">🖼️ Ilipat ang mga elemento</div>
        <div class="shortcut-row"><kbd>Arrow keys</kbd> Ilipat ang text/larawan/lagda</div>
        <div class="shortcut-row"><kbd>Ctrl+arrow keys</kbd> Mas malalaking hakbang</div>
        <div class="shortcut-row"><kbd>Enter</kbd> I-save</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Itapon</div>

        <div class="shortcut-cat">🗣️ Speech output</div>
        <div class="shortcut-row"><kbd>F2</kbd> I-on/i-off ang speech output</div>
        """,
        'info_contextmenu': "📌 Mahalaga: Lahat ng function ay naa-access din sa pamamagitan ng context menu (right-click)!",
        'info_accessibility_hint': "💡 Tip: Ang speech output (F2) ay nagpapadali sa oryentasyon at nagbibigay ng feedback sa mga menu at dialog.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lisensya at Impressum",

        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Impormasyon ayon sa § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        Email: binhdiez64@gmail.com<br>
        Responsable para sa nilalaman: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Disclaimer</strong><br>
        Ang software ay binuo nang may lubos na pangangalaga. Walang pananagutan para sa katumpakan, pagkakumpleto at paggana. Ang paggamit ay sa sariling peligro.<br><br>

        <strong>📄 MIT License (pribadong paggamit)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
>        Pinapayagan: libreng paggamit, pribadong pagbabago, personal na mga kopya.<br>
        Hindi pinapayagan: pagbebenta, komersyal na paggamit, pagtanggal ng mga paalala sa copyright.<br><br>

        <strong>🔧 Mga bahagi ng third-party</strong><br>
        Ang software na ito ay naglalaman ng mga bahagi sa ilalim ng GPL, AGPL, Apache 2.0, BSD at MIT license.<br>
        Sa pamamahagi, dapat sundin ang mga kaukulang kondisyon ng lisensya.<br><br>

        <strong>🌐 Open Source</strong><br>
        Ang source code ay available at maaaring tingnan, baguhin at ipamahagi ayon sa mga kaukulang kondisyon ng lisensya.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Pasasalamat",
        'info_credits': "Salamat sa open-source community",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Pagproseso ng PDF</li>
            <li><strong>PyQt5</strong> – Graphical interface</li>
            <li><strong>Tesseract OCR</strong> – Text recognition</li>
            <li><strong>OCRmyPDF</strong> – OCR integration</li>
            <li><strong>python-docx</strong> – Word export</li>
            <li><strong>qtawesome</strong> – Mga icon</li>
            <li><strong>DeepSeek</strong> – Suporta sa mga pagsasalin (50+ wika)</li>
            <li><strong>Lahat ng gumagamit</strong> – Para sa mahalagang feedback</li>
            <li><strong>Open-source community</strong> – Para sa magagandang library</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Mga Wika",
        'info_languages_header': "🌍 Suporta sa Wika",
        'info_languages_html': """
        <div style="line-height:1.6;">
            <p>Sinusuportahan ng PDF Dark View ang <strong>62 wika</strong> – upang ang software ay maging naa-access sa buong mundo.</p>

            <p><strong>📖 Buong listahan ng wika (mula Marso 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanian (Shqip)</li>
                    <li>🇩🇿 Arabic (العربية)</li>
                    <li>🇮🇩 Balinese (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Burmese (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnian (Bosanski)</li>
                    <li>🇧🇬 Bulgarian (Български)</li>
                    <li>🇨🇳 Chinese (中文)</li>
                    <li>🇩🇰 Danish (Dansk)</li>
                    <li>🇩🇪 German (Deutsch)</li>
                    <li>🇬🇧 English (English)</li>
                    <li>🇪🇪 Estonian (Eesti)</li>
                    <li>🇫🇮 Finnish (Suomi)</li>
                    <li>🇫🇷 French (Français)</li>
                    <li>🇬🇷 Greek (Ελληνικά)</li>
                    <li>🇮🇱 Hebrew (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croatian (Hrvatski)</li>
                    <li>🇭🇺 Hungarian (Magyar)</li>
                    <li>🇮🇩 Indonesian (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irish (Gaeilge)</li>
                    <li>🇮🇸 Icelandic (Íslenska)</li>
                    <li>🇮🇹 Italian (Italiano)</li>
                    <li>🇯🇵 Japanese (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korean (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvian (Latviešu)</li>
                    <li>🇱🇹 Lithuanian (Lietuvių)</li>
                    <li>🇱🇺 Luxembourgish (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malay (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolian (Монгол)</li>
                    <li>🇳🇵 Nepali (नेपाली)</li>
                    <li>🇳🇱 Dutch (Nederlands)</li>
                    <li>🇳🇴 Norwegian (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persian (فارسی)</li>
                    <li>🇵🇱 Polish (Polski)</li>
                    <li>🇵🇹 Portuguese (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Romanian (Română)</li>
                    <li>🇷🇺 Russian (Русский)</li>
                    <li>🇸🇪 Swedish (Svenska)</li>
                    <li>🇷🇸 Serbian (Српски)</li>
                    <li>🇸🇰 Slovak (Slovenčina)</li>
                    <li>🇸🇮 Slovenian (Slovenščina)</li>
                    <li>🇪🇸 Spanish (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Czech (Čeština)</li>
                    <li>🇹🇷 Turkish (Türkçe)</li>
                    <li>🇺🇦 Ukrainian (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamese (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yiddish (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Magdagdag ng sariling wika:</strong><br>
                Gusto mo ng wikang hindi pa kasama? Ilagay lamang ang iyong sariling diksyunaryo file (<code>sprache_xx.py</code>) sa tabi ng application – awtomatikong makikilala ito ng software. Kung interesado sa isang espesyal na pagsasalin, makipag-ugnayan sa akin.
            </div>

            <p><strong>🙏 Espesyal na pasasalamat:</strong> DeepSeek para sa suporta sa pagsasalin ng lahat ng diksyunaryo sa 62 wika.</p>

            <p>📧 Kontak para sa mga pagsasalin: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Error",
        'error_occurred': "May naganap na error",
        'error_pdf_load': "Error sa pag-load ng PDF",
        'error_pdf_save': "Error sa pag-save ng PDF",
        'error_ocr': "Error sa text recognition",
        'error_no_pdf': "Walang naka-load na PDF",
        'error_page_not_found': "Hindi mahanap ang pahina",
        'error_invalid_range': "Hindi wastong hanay ng pahina",
        'error_file_not_found': "Hindi mahanap ang file",
        'error_permission': "Walang pahintulot",
        'error_unknown': "Hindi kilalang error",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Matagumpay",
        'success_operation': "Matagumpay na natapos ang operasyon",
        'success_saved': "Matagumpay na na-save",
        'success_exported': "Matagumpay na na-export",
        'success_imported': "Matagumpay na na-import",
        'success_deleted': "Matagumpay na nabura",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Kumpirmasyon",
        'confirm_yes': "Oo",
        'confirm_no': "Hindi",
        'confirm_ok': "OK",
        'confirm_cancel': "Kanselahin",
        'confirm_delete': "Burahin",
        'confirm_overwrite': "I-overwrite",
        'confirm_continue': "Magpatuloy",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Nilo-load ang PDF...",
        'progress_saving': "Sine-save ang PDF...",
        'progress_exporting': "Ini-export ang PDF...",
        'progress_processing': "Nagproseso...",
        'progress_wait': "Pakiusap maghintay...",
        'progress_preparing': "Naghahanda...",
        'progress_finalizing': "Sinasapinal...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Puti",
        'color_black': "Itim",
        'color_red': "Pula",
        'color_green': "Berde",
        'color_blue': "Asul",
        'color_yellow': "Dilaw",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Kahel",
        'color_gray': "Gray",
        'color_custom': "Pumili ng kulay",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&File",
        'menu_edit': "&I-edit",
        'menu_view': "&Tingnan",
        'menu_tools': "&Mga Tool",
        'menu_settings': "&Mga Setting",
        'menu_help': "&Tulong",
        'menu_language': "🌐 Wika",
        'menu_guides': "&Mga Gabay",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Buksan",
        'file_save_as': "&I-save bilang...",
        'file_protect': "&Protektahan ang dokumento...",
        'file_export': "&I-export",
        'file_export_pages': "I-export bilang Pages",
        'file_export_word': "I-export bilang DOCX",
        'file_export_text': "I-export bilang TXT",
        'file_print_now': "&I-print ngayon",
        'file_print': "&I-print",
        'file_close': "&Isara",
        'file_quit': "&Lumabas",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Maghanap",
        'edit_ocr': " Gumawa ng OCR",
        'edit_rotate': "&Iikot ang pahina",
        'edit_rotate_all': "&Iikot ang lahat ng pahina",
        'edit_delete_pages': "&Burahin ang mga pahina",
        'edit_extract_pages': "&Kunin ang mga pahina",
        'edit_insert_pages': "&Magpasok ng mga pahina",
        'edit_move_pages': "&Ilipat ang mga pahina",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Magpasok ng text at krus",
        'text_insert': " Magpasok ng text",
        'cross_insert': " Magpasok ng krus",
        'text_customize': " Ayusin ang text",
        'cross_customize': " Ayusin ang krus na ito",
        'cross_customize_all': " Ayusin ang lahat ng krus",
        'text_discard': " Itapon ang text/krus na ito",
        'text_discard_all': " Itapon ang lahat ng text at krus",
        'text_save_all': " I-save ang lahat ng text at krus",
        'text_guide': " Text Input / Text Block - Gabay",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Magpasok ng lagda",
        'signature_settings_menu': " Mga Setting...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Magpasok ng larawan",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Magpasok ng mga hugis",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Ipakita ang text window",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Lapad ng pahina (Default)",
        'view_zoom_two': "&Dalawang pahina",
        'view_zoom_overview': "&Overview (maraming pahina)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Accessibility aid",
        'settings_voice': "Speech output",
        'settings_voice_tooltip': "pinupunan ang speech output ng screen reader ng karagdagang impormasyon",
        'settings_signature': "&Mga Setting ng Lagda",
        'settings_password': "&Pamahalaan ang Password",
        'settings_backup': "Gumawa ng backup bago ang mga pagbabago",
        'settings_export_import': "&I-export / i-import ang mga setting",
        'settings_export': "&I-export ang lahat ng setting...",
        'settings_import': "&I-import ang lahat ng setting...",
        'settings_export_info': "&Ano ang nae-export?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "on",
        'voice_off': "off",
        'voice_toggle': "Speech output {0}",
        'voice_speed': "Bilis sa {0} porsyento",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Hindi mahanap ang tool:\n{0}\n\nBASE_DIR: {1}\nSiguraduhin na ang mga PDF tool ay naka-install sa direktoryo {1}.",
        'tool_started': "Nagsimula ang {0}",
        'tool_start_failed': "Hindi masimulan",
        'process_error_failed_to_start': "Hindi masimulan ang proseso. Umiiral ba ang file?",
        'process_error_crashed': "Nag-crash ang proseso habang nagsisimula.",
        'process_error_timeout': "Naabot ang timeout ng proseso.",
        'process_error_write': "Error sa pagsulat sa proseso.",
        'process_error_read': "Error sa pagbasa sa proseso.",
        'process_error_unknown': "Hindi kilalang error sa proseso",
        'process_command': "Command",
        'process_normal_exit': "normal na natapos",
        'process_crashed': "nag-crash",
        'process_nonzero_exit': "{0} ay natapos na may error code {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Kinakansela...",
        'move_cancelling': "Kinakansela ang paglipat",
        'opening_pdf': "Binubuksan ang PDF...",
        'loading_document': "Niloload ang dokumento...",
        'pdf_opened': "Bukas ang PDF",
        'pages_found_moving': "{0} pahina ang natagpuan, {1} para ilipat",
        'creating_backup': "Gumagawa ng backup...",
        'backup_description': "Sini-secure ang orihinal na file...",
        'backup_saved_as': "Na-secure bilang: {0}",
        'error_format': "Error: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "I-reset ang paghahanap",
        'page_header_simple': "=== Pahina {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Pamahalaan ang Password – Gabay",
        'password_guide_voice': "Gabay sa pamamahala ng password. Pakiusap basahin ang mga paalala.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Pamahalaan ang Password – Detalyadong Gabay</strong></p>

        <p><strong>1. Proteksyon ng password para sa PDF</strong></p>
        <ul>
        <li>Kapag nagbukas ng PDF na protektado ng password, lilitaw ang isang dialog kung saan maaari mong ilagay ang password.</li>
        <li>Maaari mong i-save ang password na naka-encrypt, upang hindi mo na ito kailangang ilagay muli sa bawat pagkakataon (checkbox "I-save ang password").</li>
        <li>Gamit ang button na "Alisin ang password" maaari kang lumikha ng isang na-decrypt na kopya ng PDF at tanggalin ang password mula sa database.</li>
        </ul>

        <p><strong>2. Master Password</strong></p>
        <ul>
        <li>Pinoprotektahan ng master password ang access sa lahat ng naka-save na PDF password.</li>
        <li><strong>Pag-set up:</strong> Pumunta sa "Mga Setting → Pamahalaan ang Password → Master PW Settings" at i-click ang "Mag-set up ng master password". Pumili ng malakas na master password (hindi bababa sa 8 character).</li>
        <li><strong>Pagbabago:</strong> Pagkatapos ng matagumpay na authentication maaari mong baguhin ang master password.</li>
        <li><strong>Pag-alis:</strong> Kung tatanggalin mo ang master password, LAHAT ng naka-save na password ay permanenteng tatanggalin. Maaari kang mag-export ng backup bago.</li>
        <li>Isang beses bawat session kailangan mong mag-authenticate gamit ang master password upang ma-access ang mga protektadong function (hal. pagtingin ng mga password).</li>
        </ul>

        <p><strong>3. Pamamahala ng password (Listahan)</strong></p>
        <ul>
        <li>Sa ilalim ng "Mga Setting → Pamahalaan ang Password" bubuksan mo ang isang table ng lahat ng naka-save na PDF kasama ang kanilang naka-encrypt na password.</li>
        <li><strong>Walang master password:</strong> Maaari ka lamang magtanggal ng mga entry – ang mga password ay nananatiling nakatago.</li>
        <li><strong>May master password (naka-authenticate):</strong> Maaari mong tingnan, kopyahin, i-export at tanggalin ang mga password.</li>
        <li><strong>Pag-export:</strong> Pumili ng format (JSON, CSV, TXT) at i-save ang listahan. Kung naka-set ang master password, maaari kang magpasya kung ang mga password ay ie-export sa plain text o mananatiling naka-encrypt.</li>
        <li><strong>Pag-import:</strong> Ang isang dating na-export na ZIP file (kasama ang mga setting) ay maaaring basahin muli sa pamamagitan ng "Mga Setting → I-export / i-import ang mga setting". Babala: Ang umiiral na data ay mai-overwrite!</li>
        </ul>

        <p><strong>4. Password Generator</strong></p>
        <ul>
        <li>Sa password dialog (hal. kapag pinoprotektahan ang PDF) makikita mo ang isang dice button 🎲 sa kanan ng input field.</li>
        <li>I-click ito upang buksan ang password generator. Maaari mong itakda ang haba, character set (malaking titik, maliit na titik, numero, espesyal na character) at separator para sa mas mahusay na pagbabasa.</li>
        <li>Ang nabuong password ay maaaring kunin nang direkta at kopyahin kung kinakailangan.</li>
        </ul>

        <p><strong>5. Mahahalagang paalala sa seguridad</strong></p>
        <ul>
        <li>Ang mga naka-save na password ay naka-imbak sa AES-256 encrypted form. Ang key ay nagmula sa iyong master password (kung naka-set) o mula sa isang fixed value (walang master password).</li>
        <li>Kung walang master password, ang mga password ay naka-encrypt ngunit ang key ay naka-imbak sa programa – ang isang attacker na may access sa iyong mga file ay maaaring mag-decrypt sa kanila. Samakatuwid mahigpit naming inirerekomenda ang paggamit ng master password.</li>
        <li>Ang password database ay matatagpuan sa direktoryo `Daten/passwords.json`. Gumawa ng regular na backup, lalo na bago tanggalin ang master password.</li>
        <li>Kung mawala ang master password, lahat ng naka-save na password ay permanenteng mawawala.</li>
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
        'invert_mode_label': "Inversion Mode",
        'invert_mode_classic': "Classic (baligtarin ang lahat ng kulay)",
        'invert_mode_smart': "Smart (baligtarin lamang ang liwanag)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Grayscale Threshold",
        'gray_threshold_10': "10% (mahigpit)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (default)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (malambot)",
        'threshold_changed': "Naitakda ang threshold sa {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Grayscale Threshold – Paliwanag",
        'threshold_guide_text': "Ang grayscale threshold ay tumutukoy kung aling mga pixel sa smart dark mode ang itinuturing na 'gray' at ibabaligtad.\n\n"
                                "• Ang mababang halaga (10%) ay binabaligtad lamang ang halos perpektong gray tones – nananatiling ganap na napanatili ang mga may kulay na elemento.\n"
                                "• Ang mataas na halaga (50%) ay binabaligtad kahit ang bahagyang may kulay na pixel – pinapataas nito ang contrast, ngunit maaaring baluktutin ang mga kulay.\n\n"
                                "Ang pinakamainam na halaga ay depende sa dokumento. Para sa purong text na dokumento, ang 30–40% ay madalas na perpekto, para sa may kulay na graphics ay 10–20%.\n\n"
                                "Maaari mong ayusin ang halaga anumang oras sa pamamagitan ng menu na 'Mga Setting' – ang PDF ay agad na muling ilo-load.\n\n"
                                "Tandaan:\n* Ang mga larawan ay maaari lamang maipakita nang tama sa Light Mode!\n* Ang inversion settings ay ipinapakita lamang kapag naka-activate ang Dark Mode.",
        'threshold_guide_voice': "Ang grayscale threshold ay tumutukoy kung gaano kalakas ang pag-impluwensya ng smart dark mode. Pinapanatili ng mababang halaga ang mga kulay, pinapataas ng mataas na halaga ang contrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Binubuksan ang PDF...",
        'progress_loading_document': "Niloload ang dokumento...",
        'progress_pdf_opened': "Bukas ang PDF",
        'progress_creating_backup': "Gumagawa ng backup...",
        'progress_backup_description': "Sini-secure ang orihinal na file...",
        'progress_backup_created': "Nagawang backup",
        'progress_backup_saved_as': "Na-secure bilang: {0}",
        'progress_analyzing_start': "Sinisimulan ang pagsusuri...",
        'progress_searching_empty': "Naghahanap ng mga walang laman na pahina...",
        'progress_page_empty': "Walang laman ang pahina {0}",
        'progress_page_keep': "Pahina {0} ay itatago",
        'progress_analysis_complete': "Tapos ang pagsusuri",
        'progress_empty_found': "{0} walang laman na pahina ang natagpuan",
        'progress_current_page': "Kasalukuyang pahina",
        'progress_mark_delete': "Minamarkahan para burahin",
        'progress_range_selected': "Hanay ng pahina {0}-{1}",
        'progress_deleting_pages': "Binubura ang {0} pahina",
        'progress_creating_new_pdf': "Gumagawa ng bagong PDF...",
        'progress_transferring_pages': "Inililipat ang mga pahina",
        'progress_keeping_page': "Pahina {0} ay itatago ({1}/{2})",
        'progress_saving_pdf': "Sine-save ang PDF...",
        'progress_optimizing': "Ino-optimize ang laki ng file...",
        'progress_finalizing': "Sinasapinal...",
        'progress_new_size': "Bagong laki: {0:.2f} MB",
        'progress_cancelling': "Kinakansela...",
        'progress_cancel_message': "Kinakansela ang {0}",
        'progress_pages_found_moving': "{0} pahina ang natagpuan, {1} para ilipat",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Sinusuri ang PDF...",
        'ocr_status_optimizing': "Ino-optimize ang larawan...",
        'ocr_status_recognizing': "Isinasagawa ang pagkilala sa teksto...",
        'ocr_status_embedding': "Ine-embed ang teksto...",
        'ocr_status_finalizing': "Sinasapinal ang PDF...",

        # PDF-Laden
        'progress_preparing': "Naghahanda...",
        'progress_loading': "Nilo-load ang PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Binubura ang mga pahina...",
        'progress_moving_title': "Inililipat ang mga pahina...",
        'pages_found': "Mga pahinang natagpuan",
        'progress_creating_new_order': "Gumagawa ng bagong pagkakasunud-sunod...",
        'progress_sorting_pages': "Inaayos ang mga pahina...",
        'progress_moving_to_begin': "Inililipat ang {0} pahina sa simula",
        'progress_transferring_count': "Inililipat ang {0} pahina",
        'progress_transferring_before_target': "Inililipat ang mga pahina bago ang target",
        'progress_moving_pages': "Inililipat ang {0} pahina",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_protektado_",
        'filename_copy_suffix': "_kopya",
        'filename_page_single': "_pahina_",
        'filename_page_range': "_mga_pahina_",
        'filename_export_page': "_pahina_{0:03}",
        'filename_export_range': "_mga_pahina_{0}-{1}",
        'filename_export_multiple': "_mga_pahina_{0}",
        'filename_with_text': "_may_text",
        'filename_with_signature': "_may_lagda",
        'filename_with_image': "_may_larawan",
        'filename_with_forms': "_may_mga_hugis",
        # ---------------------------------------------------------
        # Zentrale Verwaltung des Formats der Zeitstempel
        # ---------------------------------------------------------
        'filename_timestamp_format': "%Y%m%d_%H%M%S",
        'filename_timestamp_micro': "%Y%m%d_%H%M%S_%f",

        # ============================================
        # 56. ANSICHT – BUTTONLEISTE EIN-/AUSBLENDEN
        # ============================================
        'view_toggle_navbar': "Ipakita ang button bar",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Hindi matanggal ang lahat ng pahina",
		'pages_cannot_delete_last_page': 'Hindi matanggal ang huling pahina!',
		'pages_cannot_delete_all_pages': 'Dapat may natitirang kahit isang pahina sa dokumento!',
		'delete_pages_confirm': 'Sigurado ka bang gusto mong tanggalin ang {0} na pahina?',
		'delete_pages_confirm_voice': 'Sigurado ka bang gusto mong tanggalin ang {0} na pahina?',
		'pages_deleted': 'Matagumpay na natanggal ang {0} na pahina.',
		'warning': 'Babala',
		'error': 'Error',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Walang napiling form",
        'form_customized': "Inayos ang form",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Piliin",
        'btn_use': "Gamitin",
        'master_password_for_spasswords': "Upang mag-imbak at gumamit ng mga password, kailangan munang mag-set up ng master password.\n\nNais mo bang i-set up ang master password ngayon?",
        'open_saved_dialog_title': "Buksan ang naka-save na file",
        'open_saved_question': "Nais mo bang buksan ang naka-save na file ngayon?",
        'password': "Password",
        'password_manager_master_required': "Ang password manager ay magagamit lamang kung ang isang master password ay na-set up.\n\nNais mo bang i-set up ang master password ngayon?",
        'password_master_required_for_select': "Upang matingnan at mapili ang mga naka-save na password, kailangan mo munang mag-authenticate gamit ang iyong master password.\n\nNais mo bang mag-authenticate ngayon?",
        'password_not_available': "Ang napiling password ay hindi magagamit o hindi ma-decrypt.",
        'password_options_title': "Mga opsyon sa password",
        'password_save_choice_change': "Magtakda ng bagong password",
        'password_save_choice_keep': "Gamitin ang umiiral na password",
        'password_save_choice_none': "I-save nang walang encryption",
        'password_save_hint': "Mag-set up muna ng master password upang ligtas na mag-imbak ng mga password.",
        'password_save_master_required': "I-save ang password (posible lamang sa master password)",
        'password_save_question': "Ang kasalukuyang PDF ay protektado ng password. Nais mo bang gamitin ang umiiral na password, magtakda ng bago, o i-save nang walang encryption?",
        'password_select': "Pumili ng password",
        'password_select_none': "Walang napiling password.\n\nMangyaring pumili ng password mula sa listahan.",
        'password_select_one': "Mangyaring pumili ng eksaktong isang password.\n\nNag-marka ka ng maraming password.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_backup",
        'filename_insert_suffix': "_may_pagpasok",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_mga_pahina_nabura",
        'filename_pages_moved': "_mga_pahina_nailipat",
        'filename_rotated_all_suffix': "_lahat_ng_pahina_naikot",
        'filename_rotated_suffix': "_pahina_naikot",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configuration ng mga pangalan ng file kapag binabago ang PDF",
        'filename_keep_suffixes': "Panatilihin ang mga nakaraang extension (hal. _may_texto)",
        'filename_keep_suffixes_false': "Palitan",
        'filename_keep_suffixes_true': "Panatilihin",
        'filename_preview_label': "Preview ng pangalan ng file:",
        'filename_preview_overwrite_hint': "Walang preview – ang orihinal ay mapapatungan.",
        'filename_separator': "Separator sa pagitan ng mga salita",
        'filename_separator_none': "Walang separator",
        'filename_separator_space': "Espasyo ( )",
        'filename_separator_underscore': "Underscore (_)",
        'filename_settings_saved': "Na-save ang mga setting ng pangalan ng file",
        'filename_settings_title': "Pag-format ng pangalan ng file at backup",
        'filename_timestamp_position': "Posisyon ng timestamp",
        'filename_timestamp_position_after': "Pagkatapos ng base name",
        'filename_timestamp_position_before': "Sa unahan",
        'filename_timestamp_position_end': "Sa dulo",
        'filename_use_timestamp': "Gumamit ng timestamp",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Pag-uugali kapag nagbabago:</b><ul><li>Pagbubura at pagpasok ng mga pahina</li><li>Pagpasok ng teksto, lagda, larawan at mga hugis</li><li>OCR</li></ul></html>",
        'backup_section': "Backup para sa mga operasyon sa pahina (Burahin, Ilipat)",
        'behavior_info': "Tandaan: Sa 'Patungan ang orihinal', hindi pinapansin ang mga timestamp at suffix – pinapanatili ng file ang pangalan nito.",
        'behavior_new_file': "Palaging lumikha ng bagong file (na may timestamp at suffix)",
        'behavior_overwrite': "Patungan ang orihinal (walang bagong file)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Lahat ng pahina ay naikot.\n\nAng orihinal ay nanatiling hindi nagbago.\nBagong file: {0}",
        'all_pages_rotated_voice': "Lahat ng pahina naikot, ginawa ang bagong file.",
        'empty_pages_deleted_new_file': "{0} blangkong pahina ay nabura.\n\nAng orihinal ay nanatiling hindi nagbago.\nBagong file: {1}",
        'empty_pages_deleted_voice': "{0} blangkong pahina nabura, ginawa ang bagong file.",
        'ocr_keep_original': "Panatilihin ang orihinal (buksan nang manu-mano mamaya)",
        'ocr_new_file_question': "Ang bagong nako-customize na PDF ay na-save sa:\n{0}\n\nNais mo bang buksan ito ngayon?",
        'ocr_open_new': "Buksan ang bagong OCR file",
        'ocr_original_kept': "Ang orihinal na file ay nananatiling bukas. Ang OCR file ay na-save.",
        'page_deleted_new_file': "Ang pahina {0} ay nabura.\n\nAng orihinal ay nanatiling hindi nagbago.\nBagong file: {1}",
        'page_deleted_voice': "Pahina {0} nabura, ginawa ang bagong file.",
        'page_rotated_new_file': "Ang pahina {0} ay naikot.\n\nAng orihinal ay nanatiling hindi nagbago.\nBagong file: {1}",
        'page_rotated_voice': "Pahina {0} naikot, ginawa ang bagong file.",
        'pages_deleted_new_file': "{0} mga pahina ay nabura.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nBagong file: {1}",
        'pages_deleted_new_file_voice': "{0} mga pahina nabura, ginawa ang bagong file.",
        'pages_inserted_new_file': "{0} mga pahina ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nBagong file: {1}",
        'pages_inserted_new_file_ask': "{0} mga pahina ay naipasok.\n\nAng orihinal ay nanatiling hindi nagbago.\nBagong file: {1}\n\nNais mo bang buksan ito ngayon?",
        'pages_inserted_voice_new': "{0} mga pahina naipasok, ginawa ang bagong file.",
        'pages_moved_new_file': "{0} mga pahina ay nailipat.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nBagong file: {1}",
        'pages_moved_new_file_voice': "{0} mga pahina nailipat, ginawa ang bagong file.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Huwag nang ipakita muli",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Setting ng backup</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Backup ON</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Sa lahat ng pagbabagong pumapatong sa orihinal</strong> (teksto, lagda, larawan, hugis, OCR, pag-ikot, pagpasok, pagbura/paglipat ng mga pahina) <strong>awtomatikong nalilikha ang isang backup na may timestamp</strong> bago ilapat ang pagbabago.</p>
                <p style="margin: 5px 0 5px 20px;">• Ang backup ay nasa tabi ng orihinal na file (hal. <code>Dokumento_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Kung pinagana mo rin ang opsyon na <strong>„Patungan ang orihinal“</strong>, nalilikha rin ang isang backup.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Backup OFF</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Walang backup na nalilikha</strong> – ni kapag pumapatong, ni sa mga operasyon sa pahina.</p>
                <p style="margin: 5px 0 5px 20px;">• Ang orihinal na file ay maaaring mawala nang hindi na mababawi kapag napatanungan.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Inirerekomenda lamang para sa mga may karanasang gumagamit!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Ang setting ng backup ay malaya mula sa opsyon na „Patungan ang orihinal“. Maaari mong pagsamahin ang dalawa.<br>
                Maaari mong permanenteng itago ang mensaheng ito.
            </div>
        </div>
        """,
        'backup_info_title': "Pag-uugali ng backup",
        'backup_info_voice': "Abiso tungkol sa pag-uugali ng backup sa mga operasyon sa pahina. Backup ON pumapatong sa orihinal, backup OFF lumilikha ng bagong file.",
        'show_backup_info': "Impormasyon tungkol sa setting ng backup",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Huwag nang ipakita muli",
        'overwrite_enable_backup': "Paganahin ang backup (inirerekomenda)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Patungan ang orihinal</p>
            <p>Kung pinagana mo ang opsyong ito, ang mga pagbabago (teksto, lagda, larawan, hugis, OCR, pag-ikot, pagpasok) ay <strong>nai-save nang direkta sa orihinal</strong> – <strong>walang bagong file na nalilikha</strong>.</p>
            <p>• Ang pangalan ng file ay nananatiling hindi nagbabago.<br>
            • Hindi pinapansin ang mga timestamp at suffix.<br>
            • <strong>Kung walang backup, ang orihinal ay maaaring mawala nang hindi na mababawi.</strong></p>
            <p style="color: #FFD700;">Rekomendasyon: Paganahin din ang backup na opsyon upang makakuha ng awtomatikong mga kopya ng seguridad.</p>
        </div>
        """,
        'overwrite_info_title': "Patungan ang orihinal",
        'overwrite_info_voice': "Babala: Patungan ang orihinal – walang bagong file. Inirerekomenda ang backup.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} mga pahina ay naipasok.\n\nAng orihinal na file ay napatanungan.\nIsang backup ang nalikha.",
        'pages_inserted_overwrite_no_backup': "{0} mga pahina ay naipasok.\n\nAng orihinal na file ay napatanungan.\nWALANG backup na nalikha.",
        'texts_saved_overwrite_with_backup': "Ang mga pagbabago ay na-save sa orihinal.\n\nIsang backup ang nalikha.",
        'texts_saved_overwrite_no_backup': "Ang mga pagbabago ay na-save sa orihinal.\n\nWALANG backup na nalikha.",
        'texts_crosses_saved_new_file': "{0} {1} at {2} {3} ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nIsang bagong file ang nalikha.\n\nNaglo-load ang bagong PDF...",
        'texts_saved_new_file': "{0} {1} ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nIsang bagong file ang nalikha.\n\nNaglo-load ang bagong PDF...",
        'crosses_saved_new_file': "{0} {1} ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nIsang bagong file ang nalikha.\n\nNaglo-load ang bagong PDF...",
        'elements_saved_new_file': "{0} elemento ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nIsang bagong file ang nalikha.\n\nNaglo-load ang bagong PDF...",
        'signatures_saved_overwrite_with_backup': "Ang (mga) lagda ay na-save sa orihinal.\n\nIsang backup ang nalikha.",
        'signatures_saved_overwrite_no_backup': "Ang (mga) lagda ay na-save sa orihinal.\n\nWALANG backup na nalikha.",
        'images_saved_overwrite_with_backup': "Ang (mga) larawan ay na-save sa orihinal.\n\nIsang backup ang nalikha.",
        'images_saved_overwrite_no_backup': "Ang (mga) larawan ay na-save sa orihinal.\n\nWALANG backup na nalikha.",
        'forms_saved_overwrite_with_backup': "Ang (mga) hugis ay na-save sa orihinal.\n\nIsang backup ang nalikha.",
        'forms_saved_overwrite_no_backup': "Ang (mga) hugis ay na-save sa orihinal.\n\nWALANG backup na nalikha.",
        'signatures_saved_new_file': "{0} (mga) lagda ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nIsang bagong file ang nalikha.\n\nNaglo-load ang bagong PDF...",
        'images_saved_new_file': "{0} (mga) larawan ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nIsang bagong file ang nalikha.\n\nNaglo-load ang bagong PDF...",
        'forms_saved_new_file': "{0} (mga) hugis ay naipasok.\n\nAng orihinal na file ay nanatiling hindi nagbago.\nIsang bagong file ang nalikha.\n\nNaglo-load ang bagong PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Babala: Ang PDF na ito ay naglalaman ng mga pahinang naikot. Maaaring mag-iba ang pagpoposisyon.",
        'page_rotated_warning_title': "May nakitang naikot na pahina",
        'page_rotated_warning_message': "Ang kasalukuyang pahina {0} ay naikot ng {1}°.\n\nHindi sinusuportahan ang pagpasok ng mga elemento sa mga naikot na pahina.\n\nNais mo bang ikot ang pahina sa patayong posisyon ngayon?",
        'page_rotated_warning_voice': "Babala: Ang pahina ay naikot. Pakiirot muna ito.",
        'paste_on_rotated_page_simple_warning': "Hindi posible ang pagpasok sa pahina {0}!\n\nAng pahinang ito ay naikot ng {1}°.\n\nPakiirot muna ang pahina sa 0° (Menu: I-edit → I-align ang pahina).\n\nBabala:\nAng dating kinopyang elemento ay mawawala kung hindi ka magse-save bago ikot ang pahina.",
        'paste_on_rotated_page_voice': "Kinansela ang pagpasok. Naikot ang pahina. Pakii-align muna ang pahina.",
        'page_rotated_cancel': "Kanselahin",
        'page_rotated_rotate_until_upright': "Ikot ang pahina nang paulit-ulit (hanggang maging patayo)",
        'page_rotated_now_upright': "Ang pahina ay patayo na ngayon. Maaari ka nang magpasok.",
        'page_rotated_still_not_upright': "Hindi maikot ang pahina sa patayong posisyon. Pakiiwasto nang manu-mano.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Tulong: Iwasto ang mga naikot na pahina",
        'help_rotated_pages_voice': "Binubuksan ang tulong para sa pagwawasto ng mga naikot na pahina.",
        'btn_help': "Tulong",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problema: Naikot na pahina – Hindi gumagana nang tama ang pagpasok</p>

            <p>Kung ang pagpasok ng mga teksto, lagda o hugis sa isang naikot na pahina ay hindi gumagana nang tama, maaari mong iwasto ang pahina gamit ang isang panlabas na editor ng PDF.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solusyon gamit ang panlabas na kasangkapan (hal. Preview ng macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>I-export ang pahina</strong><br>
                &nbsp;&nbsp;Mag-click sa menu sa <strong>File → I-export bilang mga pahina</strong> o gumamit ng ibang pamamaraan upang i-save ang nais na pahina bilang isang PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Buksan ang pahina sa panlabas na programa</strong><br>
                &nbsp;&nbsp;Buksan ang na-export na PDF sa isang editor ng PDF (hal. <strong>Preview ng macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Ikot ang pahina</strong><br>
                &nbsp;&nbsp;Ikot ang pahina upang ito ay maging patayo (sa Preview: <strong>Mga Kasangkapan → I-rotate</strong> o <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>I-save</strong><br>
                &nbsp;&nbsp;I-save ang naitamang pahina (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Ipasok muli ang pahina sa orihinal na dokumento</strong><br>
                &nbsp;&nbsp;Bumalik sa PDFDarkView at ipasok ang naitamang pahina sa nais na posisyon:<br>
                &nbsp;&nbsp;<strong>I-edit → Ipasok ang mga pahina</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatibo: Ikot ang pahina sa orihinal</p>
                <p style="margin: 5px 0 5px 20px;">• Gamitin ang built-in na function ng pag-ikot (<strong>I-edit → I-rotate ang pahina</strong>) upang iwasto ang pahina nang hakbang-hakbang.<br>
                • Pagkatapos ng bawat pag-ikot, maaari mong suriin kung gumagana na ang pagpasok.<br>
                • Ito ay madalas na mas mabilis na solusyon – subukan muna ito!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Kung madalas kang makatagpo ng mga naikot na pahina, maaari mong permanenteng itago ang babala sa dialog ng pagpasok.<br>
                Maaaring mag-iba ang pagpoposisyon – gamitin lamang ang opsyong ito kung alam mo ang mga kahihinatnan.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "I-align ang mga pahina",
        'menu_rotate_normalize_tooltip': "Ikot ang pahina o i-reset sa 0°",
        'normalize_current_page': "Dalhin ang kasalukuyang pahina sa patayong posisyon (itakda sa 0°)",
        'normalize_all_pages': "Dalhin ang lahat ng pahina sa patayong posisyon (itakda sa 0°)",
        'page_normalized': "Ang pahina {0} ay itinakda sa patayong posisyon.",
        'all_pages_normalized': "Lahat ng pahina ay itinakda sa patayong posisyon.",
        'page_already_upright': "Ang pahina {0} ay patayo na.",
        'all_pages_already_upright': "Lahat ng pahina ay patayo na.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>Ang PDF ay walang nako-customize na teksto.</p><p>Nais mo bang magsagawa ng OCR upang i-export sa {0}?</p>",
        'export_ocr_voice': "Ang PDF ay walang teksto. Kinakailangan ang OCR para sa pag-export sa {0}.",
        'export_no_ocr_possible': "Hindi posible ang pag-export nang walang OCR. Pakisagawa ang OCR sa pamamagitan ng menu.",
        'ocr_failed_export_not_possible': "Nabigo ang OCR. Hindi maisagawa ang pag-export.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "Ang PDF ay bubuksan sa Preview. Pakisimulan ang proseso ng pag-print doon.",
        'print_preview_manual': "Ang PDF ay nabuksan. Pakisagawa ang utos ng pag-print nang manu-mano (hal. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Pagsamahin ang mga PDF",
        'merge_pdfs': "Pagsamahin ang mga PDF",
        'merge_progress_title': "Pinagsasama ang mga PDF...",
        'merge_pdfs_list': "Mga PDF sa pagkakasunud-sunod (I-drag at i-drop upang pagbukud-bukurin)",
        'merge_add_pdf': "Magdagdag ng PDF",
        'merge_remove': "Alisin",
        'merge_move_up': "Pataas",
        'merge_move_down': "Pababa",
        'merge_pdfs_info': "💡 Tip: Maaari mong baguhin ang pagkakasunud-sunod sa pamamagitan ng pag-drag at pag-drop",
        'merge_no_pdfs': "Walang napiling PDF. Mag-click sa 'Magdagdag ng PDF'.",
        'merge_info': "{0} mga PDF ang napili (humigit-kumulang {1} mga pahina)",
        'merge_open_file': "Buksan ang file",
        'merge_merge': "Pagsamahin",
        'merge_error': "Error habang pinagsasama",
        'merge_min_two_pdfs_error': "Mangyaring pumili ng hindi bababa sa dalawang PDF file upang pagsamahin.",
        'merge_select_pdfs': "Pumili ng mga PDF na pagsasamahin",
        'merge_error_file': "Error habang pinoproseso",
        'merge_cancelled': "Kinansela ang pagsasama",
        'merge_preparing': "Naghahanda...",
        'merge_processing': "Pinoproseso ang PDF {0} ng {1}",
        'merge_saving': "Sine-save ang pinagsamang PDF...",
        'merge_complete': "Tapos na!",
        'merge_success_title': "Matagumpay ang pagsasama",
        'merge_success_voice': "{0} mga PDF ay matagumpay na naisama.",
        'merge_success_message': "{0} mga PDF ay matagumpay na naisama.\n\nAng bagong dokumento ay mayroon na ngayong {1} mga pahina.\n\nBagong file:\n{2}\n\nLokasyon ng pag-save:\n{3}\n{2}\n\nNais mo bang buksan ang PDF na ito?",
        'replace_file_title': "Palitan ang file?",
        'replace_file_message': "Mayroon nang bukas na PDF. Nais mo bang palitan ito ng bagong file?",
        'btn_yes': "Oo",
        'btn_no': "Hindi",
        'filename_merge_suffix': "pinagsama",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Binubuksan ang {0}...",
        'progress_merge_reading': "Binabasa ang {0}...",
        'progress_merge_adding': "Nagdaragdag ng {0} mga pahina...",
        'progress_merge_optimizing': "Ino-optimize ang PDF...",
        'progress_merge_writing': "Sinusulat ang PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "pagsasara ng PDF",
        'action_close_window': "pagsasara ng window",
        'action_open_new_pdf': "pagbubukas ng bagong PDF",
        'action_quit_app': "paglabas sa application",
        'changes_saved': "Na-save ang mga pagbabago.",
        'file_close_title': "Isara ang PDF file",
        'save_before_action': "Dapat bang i-save ang mga pagbabago bago {0}? Oo o Hindi?",
        'save_before_action_voice': "Dapat bang i-save ang mga pagbabago bago {0}? Oo o Hindi?",
        'save_before_close_question': "Dapat bang i-save ang mga pagbabago bago isara? Oo o Hindi?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Nagawang mahanap na PDF:\n\n{0}\n\n<b>subukan muli kung kinakailangan",
        "ocr_rotate_title": "Ihanay ang mga pahina bago ang OCR",
        "ocr_rotate_question": "Ang PDF ay naglalaman ng mga pinaikot na pahina.\nNais mo bang ihanay ang lahat ng pahina sa 0° bago ang OCR?\nIto ay makabuluhang nagpapabuti sa pagkilala ng teksto.",
        "ocr_rotate_yes": "Oo, ihanay",
        "ocr_rotate_no": "Hindi, simulan ang OCR nang direkta",
        "ocr_rotate_voice": "Ang PDF ay naglalaman ng mga pinaikot na pahina. Dapat bang ihanay ang lahat ng pahina bago ang OCR?",
        "ocr_not_performed_message": "Walang teksto. Mangyaring magsagawa ng OCR (menu \"I-edit\" → \"Magsagawa ng OCR\" o key Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Mga Setting ng OCR",
        "ocr_language_btn": "Pumili ng wika ng OCR",
        "ocr_language": "(Mga) Wika ng OCR",
        "ocr_language_current": "Kasalukuyang wika:",
        "ocr_param_info": "Impormasyon tungkol sa parameter",

        "ocr_force_ocr_label": "Puwersahin ang OCR",
        "ocr_deskew_label": "Iwasto ang pagkakiling",
        "ocr_clean_label": "Linisin ang larawan",
        "ocr_oversample_label": "Resolusyon (DPI)",
        "ocr_pagesegmode_label": "Paghati ng pahina",
        "ocr_oem_label": "Mode ng makina ng OCR",
        "ocr_optimize_label": "Pag-compress ng PDF",
        "ocr_jobs_label": "Magkakatulad na proseso",
        "ocr_verbose_label": "Detalye ng log",

        "ocr_force_ocr_tooltip": "Puwersahin ang OCR sa bawat pahina, kahit na may teksto na",
        "ocr_deskew_tooltip": "Awtomatikong ihanay ang mga nakiling na scan",
        "ocr_clean_tooltip": "Alisin ang ingay at mga artepakto mula sa larawan",
        "ocr_oversample_tooltip": "Palakihin ang larawan bago ang OCR sa DPI na ito",
        "ocr_pagesegmode_tooltip": "Tinutukoy kung paano hinahati ang pahina sa mga lugar ng teksto",
        "ocr_oem_tooltip": "Pinipili ang makina ng OCR ng Tesseract",
        "ocr_optimize_tooltip": "Antas ng pag-compress ng output na PDF",
        "ocr_jobs_tooltip": "Bilang ng magkakatulad na proseso ng OCR",
        "ocr_verbose_tooltip": "Antas ng detalye ng output ng log",
        "ocr_settings_explain_btn": "Paliwanag",

        "ocr_force_ocr_explain": "Puwersahin ang pagkilala ng teksto sa <b>bawat</b> pahina, kahit na naglalaman na ito ng teksto.\n\nRekomendasyon: <b>Naka-on</b> para sa na-scan na PDF, <b>Naka-off</b> para sa katutubong PDF na may umiiral nang teksto.",

        "ocr_deskew_explain": "Iwawasto ang bahagyang nakiling na mga scan (hanggang sa humigit-kumulang 5°).\n\nRekomendasyon: <b>Naka-on</b> para sa mga na-scan na dokumento, <b>Naka-off</b> kung ang mga pahina ay perpektong tuwid na.",

        "ocr_clean_explain": "Tinatanggal ang ingay, mga tuldok at maliliit na artepakto mula sa larawan.\n<b>MAHALAGA:</b> Para sa Arabic, Thai o Vietnamese na mga teksto na may mga diacritic na marka (mga tuldok sa itaas/ibaba ng mga titik) ang opsyon na ito ay dapat <b>i-deactivate</b>, kung hindi, maaaring mawala ang mahahalagang karakter.",

        "ocr_oversample_explain": "Pinalalaki ang larawan <b>bago</b> ang pagkilala ng teksto sa tinukoy na DPI.<br><br>• <b>72-150 DPI:</b> Napakabilis, ngunit mababang rate ng pagkilala<br>• <b>200-300 DPI:</b> Pinakamainam na hanay (Default: 300)<br>• <b>400+ DPI:</b> Bahagya lamang na mas mahusay na pagkilala, ngunit mas malalaking file<br><br>Rekomendasyon: 300 DPI para sa kumplikadong mga script (Arabic, Chinese, Japanese), 200 DPI para sa mga Kanluraning wika.",

        "ocr_pagesegmode_explain": "Tinutukoy kung paano hinahati ng Tesseract ang pahina sa mga lugar ng teksto.\n\n• <b>3 - Awtomatiko (Default):</b> Mabuti para sa halo-halong mga layout\n• <b>4 - Iisang column:</b> Para sa mga tekstong may isang column\n• <b>5 - Patayong bloke:</b> Para sa patayong mga script (Japanese, Chinese)\n• <b>6 - Magkakatulad na bloke ng teksto:</b> Pinakamainam para sa dumadaloy na teksto nang walang mga column\n• <b>11 - Hilaw na larawan:</b> Para sa mahinang pag-scan / sulat-kamay\n\nRekomendasyon: <b>6</b> para sa simpleng mga dokumento ng teksto, <b>3</b> para sa kumplikadong mga layout.",

        "ocr_oem_explain": "Pinipili ang makina ng OCR ng Tesseract.\n\n• <b>0 - Legacy:</b> Lumang makina (mabilis, ngunit hindi gaanong tumpak)\n• <b>1 - LSTM:</b> Neural na makina (mas mabagal, ngunit mas tumpak)\n• <b>2 - Legacy + LSTM:</b> Pinagsasama ang parehong mga resulta\n• <b>3 - Default (Mas gusto ang LSTM):</b> Pinakamahusay na pagpipilian para sa karamihan ng mga kaso\n\nRekomendasyon: <b>3</b> para sa pinakamataas na katumpakan ng pagkilala.",

        "ocr_optimize_explain": "Pinipiga ang output na PDF.\n\n• <b>0:</b> Walang pag-optimize (pinakamabilis na pagproseso)\n• <b>1:</b> Magaan na pag-optimize (magandang kompromiso)\n• <b>2:</b> Katamtamang pag-optimize\n• <b>3:</b> Malakas na pag-optimize (pinakamaliit na file, ngunit mas mabagal)\n\nRekomendasyon: <b>1</b> para sa pang-araw-araw na paggamit.",

        "ocr_jobs_explain": "Bilang ng magkakatulad na proseso para sa OCR.\n\n• <b>1:</b> Mabagal, ngunit pinakamababang konsumo ng memorya\n• <b>4-8:</b> Pinakamainam para sa modernong multi-core na processor\n• <b>12+:</b> Bahagya lamang na mas mabilis na pagproseso na may mataas na paggamit ng memorya\n\nRekomendasyon: Bilang ng mga CPU core (hal. <b>4</b> sa 4-core na mga sistema).",

        "ocr_verbose_explain": "Antas ng detalye ng output ng log sa console.\n\n• <b>0:</b> Walang output\n• <b>1:</b> Pag-unlad at mga mensahe ng katayuan\n• <b>2:</b> Detalyadong output\n• <b>3:</b> Buong debug output (napakalawak)\n\nRekomendasyon: <b>1</b> para sa normal na operasyon.",

        "ocr_reset_title": "Na-reset ang mga setting",
        "ocr_reset_message": "Lahat ng mga setting ng OCR ay na-reset sa mga default na halaga.",
        "info_tooltip": "Karagdagang impormasyon tungkol sa parameter na ito",
        "ocr_reset_defaults": "I-reset sa default",

        "ocr_psm_0": "Awtomatiko (Legacy na makina)",
        "ocr_psm_1": "Awtomatikong pagtuklas ng column",
        "ocr_psm_3": "Awtomatiko (Default)",
        "ocr_psm_4": "Iisang column",
        "ocr_psm_5": "Patayong bloke",
        "ocr_psm_6": "Magkakatulad na bloke ng teksto",
        "ocr_psm_7": "Iisang linya ng teksto",
        "ocr_psm_8": "Iisang salita",
        "ocr_psm_11": "Hilaw na larawan (walang pagsusuri ng layout)",

        "ocr_oem_0": "Legacy na makina (mabilis)",
        "ocr_oem_1": "LSTM na makina (neural, tumpak)",
        "ocr_oem_2": "Legacy + LSTM na pinagsama",
        "ocr_oem_3": "Default (Mas gusto ang LSTM)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "(Mga) Wika ng OCR...",
        "ocr_language_title": "Pumili ng (mga) wika ng OCR",
        "ocr_language_instruction": "Piliin ang (mga) wika para sa pagkilala ng teksto (OCR).\nBabala: Ang maraming wika ay makakaapekto sa pagganap at katumpakan!\nMakukuha mo ang pinakamahusay na mga resulta kung pipili ka lamang ng isang wika.",
        "ocr_language_predefined": "Mga paunang tinukoy na kumbinasyon",
        "ocr_language_custom": "Pasadya...",
        "ocr_language_selected": "Napiling mga wika ng OCR",
        "ocr_language_changed": "Ang wika ng OCR ay binago sa {0}",
        "ocr_language_auto_detect": "Ang mga magagamit na wika ay awtomatikong natutukoy.",
        "ocr_language_none_found": "Walang nakitang data ng wika ng Tesseract! Mangyaring i-install ang mga pakete ng wika (hal. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Pasadyaang pagpili ng wika",
        "ocr_language_available": "Mga magagamit na wika (naka-install):",
        "ocr_language_select_hint": "Pumili ng isa o higit pang mga wika:",
        "ocr_language_confirm": "Ilapat",
        "ocr_language_reset": "I-reset sa default (deu+eng+vie)",
        "ocr_language_priorities": "Inirerekomendang mga wika (paunang naka-install):",

        "select_all_languages": "Piliin lahat",
        "clear_all_languages": "I-clear ang pagpili",
        "install_language_packs": "I-install ang mga nawawalang pakete ng wika...",
        "install_hint": "💡 Tip: Hindi lahat ng wika ay naka-install sa iyong sistema. Sa pamamagitan ng button na ito makakakuha ka ng tulong sa pag-install.",
        "ocr_language_install_title": "Pag-install ng mga pakete ng wika ng Tesseract",

        "ocr_missing_languages": "Mga nawawalang pakete ng wika ng OCR",
        "ocr_missing_languages_message": "Ang mga sumusunod na napiling wika ay hindi naka-install sa iyong sistema:\n\n{0}\n\nMangyaring i-install ang mga nawawalang pakete ng wika (tingnan ang tulong sa ilalim ng 'Tulong sa pag-install').\n\nNais mo bang buksan ang tulong sa pag-install ngayon?",
        "ocr_missing_languages_voice": "Mga nawawalang pakete ng wika. Mangyaring i-install ang mga nawawalang wika.",
        "ocr_install_help_now": "Buksan ang tulong",
        "ocr_continue_anyway": "Subukan pa rin",
        "ocr_language_error_title": "Error sa wika ng OCR",
        "ocr_language_error_message": "Error sa panahon ng pagkilala ng teksto: {0}\n\nMangyaring suriin ang iyong mga setting ng wika ng OCR (Mga Setting → Wika ng OCR).",
        "ocr_install_help_button": "Tulong sa pag-install",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 I-install ang mga pakete ng wika ng Tesseract</p>

        <p>Para gumana ang OCR sa isang partikular na wika, ang kaukulang data ng wika ay dapat na naka-install sa iyong sistema. Sundin ang mga tagubilin para sa iyong operating system:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Buksan ang <strong>Terminal</strong> (Finder → Mga Programa → Mga Utility → Terminal).</li>
        <li>I-install ang lahat ng magagamit na wika sa:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Maaaring tumagal ito ng ilang minuto.)</li>
        <li>O indibidwal na mga wika lamang (hal. Vietnamese):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
>Sa kasalukuyang mga bersyon ng Homebrew, maaaring kailanganing manu-manong i-download ang <code>*.traineddata</code> (tingnan sa ibaba).</li>
        <li>Pagkatapos ng pag-install: Isara ang dialog na ito at buksan muli ang pagpili ng wika ng OCR – awtomatikong lilitaw ang mga bagong wika.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Buksan ang isang terminal (Ctrl+Alt+T).</li>
        <li>I-install ang nais na wika, hal. para sa Vietnamese:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Mahahalagang code ng wika: <code>deu</code> (Aleman), <code>eng</code> (Ingles), <code>vie</code> (Vietnamese), <code>spa</code> (Espanyol), <code>fra</code> (Pranses), <code>ita</code> (Italyano), <code>nld</code> (Olandes), <code>fin</code> (Finnish), <code>swe</code> (Suweko), <code>nor</code> (Norwegian).</li>
        <li>Ipakita ang lahat ng magagamit na pakete:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manwal)</p>
        <ol>
        <li>I-download ang nais na mga file na <code>*.traineddata</code> mula sa:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (hal. <code>vie.traineddata</code> para sa Vietnamese).</li>
        <li>Kopyahin ang mga file sa folder ng wika ng Tesseract, karaniwan:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Ayusin ayon sa indibidwal na pag-install.)</li>
        <li>I-restart ang application (o buksan muli ang pagpili ng wika ng OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatibo para sa lahat ng sistema</p>
        <ul>
        <li>I-install ang <strong>OCRmyPDF</strong> at <strong>Tesseract</strong> gamit ang isang tagapamahala ng pakete na iyong pinili. Karamihan sa mga pag-install ay naglalaman na ng ilang karaniwang wika (Ingles, Aleman, Pranses).</li>
        <li>Ang mga nawawalang wika ay maaaring i-install anumang oras – ang pagpili ng wika ng OCR ay naglilista lamang ng mga wikang aktwal na umiiral.</li>
        </ul>

        <hr>
        <p><b>✅ Pagkatapos ng pag-install:</b> Hindi kinakailangan ang pag-restart ng application – ang mga bagong idinagdag na wika ay lalabas kaagad sa listahan.</p>
        <p><b>📖 Tulong sa mga code ng wika:</b> Ang isang kumpletong listahan ay makukuha sa <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentasyon ng Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Mga font ng Noto Sans",
        "info_noto_font_voice": "Gabay sa pag-install ng font na Noto Sans",
        "btn_info_noto_font_install": "Impormasyon ng font",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Paano i-install ang mga libreng Noto font mula sa Google</h2>

        <p>Ang <strong>mga font ng Noto</strong> ay isang open-source na pamilya ng font mula sa Google. Ang kanilang layunin ay hindi makakita ng <em>"walang tofu"</em> (ibig sabihin, walang mga walang laman na kahon □) at maipakita nang tama ang bawat karakter mula sa pamantayan ng Unicode. Sila ang mainam na karagdagan para sa mga application na kailangang magpakita ng mga teksto sa maraming iba't ibang wika.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Pag-install sa macOS</h3>

        <p><strong>Paraan 1: Gamit ang Homebrew (para sa mga advanced na gumagamit)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Paraan 2: Sa pamamagitan ng "Font Book" (Inirerekomenda)</strong></p>

        <ol>
        <li>I-download ang opisyal na pakete ng font:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>I-extract ang ZIP file</li>
        <li>Kopyahin ang mga file sa <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Pag-install sa Windows (10 at 11)</h3>

        <p><strong>Paraan 1: Microsoft Store (Inirerekomenda)</strong><br>
        Hanapin ang "Google Noto Fonts" o "Noto Sans" at i-click ang <strong>I-install</strong>.</p>

        <p><strong>Paraan 2: Manu-manong pag-install</strong></p>

        <ol>
        <li>I-download:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>I-extract ang ZIP</li>
        <li>Piliin ang mga .ttf / .otf file</li>
        <li>I-right-click → <strong>I-install</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        o<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Pangalan\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Pag-install sa Linux</h3>

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

        <p>Pag-verify:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Pamahalaan ang mga bookmark",
        "bookmark_add": "Magdagdag ng bookmark",
        "bookmark_add_tooltip": "I-save ang kasalukuyang pahina bilang bookmark",
        "bookmark_remove": "Alisin ang bookmark",
        "bookmark_remove_tooltip": "Burahin ang may markang bookmark",
        "bookmark_remove_all": "Alisin lahat",
        "bookmark_remove_all_tooltip": "Burahin ang lahat ng bookmark ng PDF na ito",
        "bookmark_jump": "Pumunta sa bookmark",
        "bookmark_jump_tooltip": "Pumunta sa napiling pahina",
        "bookmark_name": "Pangalan",
        "bookmark_page": "Pahina",
        "bookmark_no_bookmarks": "Walang mga bookmark.\nI-click ang 'Magdagdag' upang i-save ang kasalukuyang pahina bilang bookmark.",
        "bookmark_added": "Idinagdag ang bookmark para sa pahina {0}: {1}",
        "bookmark_removed": "Tinanggal ang bookmark: {0}",
        "bookmark_all_removed": "Lahat ng mga bookmark ay tinanggal.",
        "bookmark_name_default": "Pahina {0}",
        "bookmark_name_prompt": "Pangalan para sa bookmark:\n(mahabang teksto ay paikliin sa 50 karakter)",
        "bookmark_name_prompt_title": "Pangalan ng bookmark",
        "bookmark_confirm_remove_all": "Sigurado ka bang gusto mong alisin ang lahat ng {0} mga bookmark?",
        "menu_bookmarks": "Mga bookmark",
        "bookmark_manage": "Pamahalaan ang mga bookmark",
        "bookmark_next": "Susunod na bookmark",
        "bookmark_prev": "Nakaraang bookmark",
        "bookmark_page_display": "Pahina {0}",
        "bookmark_exists": "Mayroon nang bookmark para sa pahinang ito na may ganitong pangalan.",
        "bookmark_select_first": "Mangyaring pumuna ng bookmark.",
        "bookmark_confirm_remove": "Sigurado ka bang gusto mong alisin ang bookmark na 'Pahina {0}: {1}'?",
        "bookmark_jumped_to": "Tumalon sa bookmark '{0}' sa pahina {1}.",
        "bookmark_jumped_to_voice": "Bookmark {0}, pahina {1}",
        "btn_close": "Isara",

        "bookmark_list": "Iyong mga bookmark",
        "bookmark_rename": "Palitan ang pangalan ng bookmark",
        "bookmark_rename_tooltip": "Baguhin ang pangalan ng napiling bookmark",
        "bookmark_rename_title": "Palitan ang pangalan ng bookmark",
        "bookmark_rename_prompt": "Bagong pangalan para sa bookmark sa pahina {0}:\n(max. 50 karakter)",
        "bookmark_renamed": "Ang bookmark '{0}' ay pinalitan ng pangalan sa '{1}'.",
        "bookmark_item_tooltip": "Pahina {0}: {1}\nMag-double click upang tumalon",
        "bookmark_name_exists_question": "Mayroon nang bookmark na may pangalang '{0}' sa pahinang ito.\nPalitan pa rin ang pangalan?",

        "context_bookmarks": "Mga bookmark",
        "context_bookmark_add_here": "Magdagdag ng bookmark para sa pahinang ito",
        "context_bookmarks_existing": "Umiiral na mga bookmark:",
        "context_bookmarks_jump": "Pumunta sa bookmark:",
        "context_bookmarks_none": "Walang mga bookmark",
        "context_bookmarks_clear_all": "Alisin ang lahat ng {0} mga bookmark",

        "bookmark_search_placeholder": "Maghanap ng mga bookmark... (pangalan o pahina)",
        "bookmark_search_results": "%d mga bookmark ang natagpuan para sa \"%s\"",
        "bookmark_no_search_results": "Walang mga bookmark na natagpuan para sa \"%s\"",
        "bookmark_no_search_results_label": "Walang mga resulta para sa \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "I-edit ang PDF metadata",
        "metadata_title": "Pamagat",
        "metadata_title_placeholder": "Pamagat ng dokumento",
        "metadata_title_tooltip": "Ang pamagat ng dokumento (ipinapakita sa title bar)",
        "metadata_author": "May-akda",
        "metadata_author_placeholder": "Pangalan ng may-akda",
        "metadata_author_tooltip": "Ang lumikha ng dokumento",
        "metadata_subject": "Paksa",
        "metadata_subject_placeholder": "Paksa ng dokumento",
        "metadata_subject_tooltip": "Isang maikling paglalarawan ng nilalaman",
        "metadata_keywords": "Mga keyword",
        "metadata_keywords_placeholder": "Mga keyword na pinaghihiwalay ng kuwit",
        "metadata_keywords_tooltip": "Mga keyword para sa pagkakategorya ng dokumento",
        "metadata_creator": "Lumikha",
        "metadata_creator_placeholder": "Application na lumikha ng PDF",
        "metadata_creator_tooltip": "Ang software kung saan nilikha ang dokumento",
        "metadata_producer": "Producer",
        "metadata_producer_placeholder": "Application na nag-convert ng PDF",
        "metadata_producer_tooltip": "Ang software na nag-convert ng PDF",
        "metadata_creation_date": "Petsa ng paglikha",
        "metadata_creation_date_tooltip": "Ang petsa ng paglikha ng dokumento",
        "metadata_mod_date": "Petsa ng pagbabago",
        "metadata_mod_date_tooltip": "Ang petsa ng huling pagbabago",
        "metadata_pdf_info": "📄 Impormasyon ng PDF",
        "metadata_pages": "Bilang ng mga pahina",
        "metadata_file_size": "Laki ng file",
        "metadata_pdf_version": "Bersyon ng PDF",
        "metadata_encrypted": "Naka-encrypt",
        "metadata_encrypted_yes": "Oo (protektado ng password)",
        "metadata_encrypted_no": "Hindi",
        "metadata_reload": "📂 I-reload mula sa PDF",
        "metadata_reset": "Itapon ang mga pagbabago",
        "metadata_reloaded": "Ang metadata ay na-reload mula sa PDF.",
        "metadata_reset_done": "Lahat ng mga field ng metadata ay na-reset.",
        "metadata_no_file": "Walang na-load na PDF file.",
        "metadata_save_error": "Error sa pag-save ng metadata",
        "metadata_saved": "Matagumpay na na-save ang metadata.",
        "metadata_pdf_version_unknown": "PDF (hindi alam)",
        "metadata_saved_message": "Matagumpay na na-save ang metadata.",
        "metadata_saved_voice": "Na-save ang metadata.",

        "metadata_custom": "🔧 Pasadwang metadata",
        "metadata_custom_placeholder": "{\n  \"aking_field\": \"aking_halaga\",\n  \"ibang_field\": 123\n}",
        "metadata_custom_tooltip": "JSON format para sa pasadyang metadata (opsyonal)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Napili ang template na \"{0}\" - Mag-double click upang ipasok",
        "text_use_template": "Gamitin ang text block",
        "text_type": "Uri",
        "text_search_templates": "Maghanap ng mga text block...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Impormasyon sa Export / Import",
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

        <h3>📦 Ano ang na-e-export? (Pangkalahatang-ideya)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Pangkalahatang mga setting ng application</span></li>
            <li class="detail">• Madilim/Maliwanag na mode</li>
            <li class="detail">• Pagbabaligtad ng madilim na mode para sa mga larawan</li>
            <li class="detail">• Halaga ng gray threshold</li>
            <li class="detail">• Wika</li>
            <li class="detail">• Geometry ng window</li>
            <li class="detail">• Zoom mode</li>
            <li class="detail">• Navigation (Nakikitang navigation bar)</li>
            <li class="detail">• Output ng pagsasalita (naka-on/naka-off)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Mga setting ng backup</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Pagpapangalan ng file (Timestamp, Separator, Suffixes)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Mga setting para sa mga pagpasok ng</span></li>
            <li class="detail">• Mga lagda</li>
            <li class="detail">• Teksto at mga text block</li>
            <li class="detail">• Mga tsek, larawan at hugis</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Mga setting ng OCR</span></li>
            <li class="detail">• Wika</li>
            <li class="detail">• Puwersahin ang OCR · Mode ng pahina</li>
            <li class="detail">• Preprocessing ng larawan: Iwasto ang pagkakiling, Linisin, Oversampling</li>
            <li class="detail">• Bilang ng magkakatulad na trabaho</li>
            <li class="detail">• Mode ng pagbabaligtad</li>
            <li class="detail">• Halaga ng gray threshold</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Mga bookmark</span></li>
            <li class="detail">• Lahat ng mga bookmark bawat PDF file (Pahina, Pangalan, Oras ng paglikha)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Database ng password</span></li>
            <li class="detail">• Naka-save na mga password ng PDF (opsyonal na naka-encrypt o plain text)</li>
            <li class="detail">• Hash ng master password (kung nakatakda)</li>
            <li class="detail">• Data ng pag-verify</li>
        </ul>

        <h4>⚠️ Mahahalagang paalala</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Kapag nag-i-import:</strong>
            <ul>
                <li><span class="warning">➜ LAHAT ng kasalukuyang mga setting ay ganap na mapapatungan</span></li>
                <li>• Kailangan ang pag-restart ng application</li>
                <li>• Ang mga umiiral na lagda, text block at bookmark ay papalitan</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Master password at mode ng pag-export:</strong>
            <ul>
                <li>• Kapag aktibo ang master password, maaari kang pumili:</li>
                <li>  - <span style="color: #98FB98;"><strong>Na-decrypt</strong></span> (ang mga password ay nasa plain text sa ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Naka-encrypt</strong></span> (mababasa lamang gamit ang master password sa target na sistema)</li>
                <li>• Ang hash ng master password ay <strong>palaging</strong> naka-imbak na naka-encrypt</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Paalala sa seguridad:</strong>
            <ul>
                <li>• Ang na-export na ZIP file ay naglalaman ng sensitibong data (<strong>mga password, bookmark, lagda</strong>)</li>
                <li>• Mangyaring itago ito nang ligtas (hal. naka-encrypt na USB stick, password manager)</li>
                <li>• Kung mawala ang file, ang mga naka-save na password ng PDF ay hindi na mababawi</li>
            </ul>
        </div>

        <h4>📁 Format ng pag-export</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Ang mga setting ay naka-save sa isang ZIP file:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ang ZIP na ito ay naglalaman ng kumpletong <code>settings.json</code> (mula sa iyong configuration) pati na rin ang posibleng naka-embed na mga file ng larawan ng lagda at naka-encrypt na mga password.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Mga Lagda - Gabay",
        'signature_guide_html': """
        📝 <strong>Mga Lagda - Mabilis na Gabay</strong><br>
        <ul>
        <li>Itakda ang master password</li>
        <li>I-configure ang mga lagda sa menu na <em>Mga Setting</em> (laki, timestamp, …)</li>
        <li>Ipasok gamit ang <strong>RIGHT CLICK</strong> sa nais na posisyon (kinakailangan ang master password isang beses bawat session)</li>
        <li>Ilipat ang lagda gamit ang mouse o mga arrow key</li>
        <li>Ipasok ang maraming lagda nang sunud-sunod</li>
        <li>I-customize ang bawat lagda nang paisa-isa</li>
        <li>Itapon ang isang lagda</li>
        <li>I-save / itapon ang lahat ng lagda nang sabay-sabay</li>
        <li>Bilang kahalili, maaari ring gamitin ang menu bar.</li>
        </ul>
        """,
        'signature_guide_voice': "Mabilis na gabay para sa mga lagda. Itakda ang master password. I-configure ang mga lagda sa mga setting. Ipasok gamit ang right click.",

        'image_guide_title': "Pagsingit ng mga Larawan - Gabay",
        'image_guide_html': """
        📷 <strong>Pagsingit ng mga Larawan sa PDF - Mabilis na Gabay</strong><br>
        <ol>
        <li>Mag-right click sa nais na posisyon</li>
        <li><em>„Ipasok ang larawan“</em> → Pumili ng larawan</li>
        <li>Iposisyon ang larawan: I-drag gamit ang mouse</li>
        <li>Ayusin ang laki: I-drag sa mga sulok/gilid</li>
        <li>Panatilihin ang aspect ratio: Pindutang <strong>[A]</strong></li>
        <li>Karagdagang pagsasaayos: Mag-right click sa larawan</li>
        </ol>
        <p><strong>Tip:</strong> Sa context menu maaari mong ayusin ang mga setting.</p>
        """,
        'image_guide_voice': "Mabilis na gabay para sa mga larawan. Mag-right click, ipasok ang larawan, pumili. Iposisyon gamit ang mouse, ayusin ang laki sa mga sulok. Aspect ratio gamit ang A key.",

        'form_guide_title': "Pagsingit ng mga Hugis - Gabay",
        'form_guide_html': """
        📐 <strong>Pagsingit ng mga Hugis sa PDF - Mabilis na Gabay</strong><br>
        <ol>
        <li>Pumili ng uri ng hugis (parihaba, ellipse, linya, arrow)</li>
        <li>Mag-click sa posisyon:
            <ul>
            <li>Para sa parihaba/ellipse: Isang click ang naglalagay ng hugis</li>
            <li>Para sa linya/arrow: Dalawang click para sa simula at dulo na punto</li>
            </ul>
        </li>
        <li>Iposisyon ang hugis: I-drag gamit ang mouse</li>
        <li>Ayusin ang laki: I-drag sa mga sulok/gilid</li>
        <li>I-save ang hugis: <strong>Enter</strong></li>
        <li>Itapon ang hugis: <strong>ESC</strong></li>
        <li>Karagdagang pagsasaayos: Mag-right click sa hugis</li>
        </ol>
        <p><strong>Tip:</strong> Sa context menu maaari mong ayusin ang mga setting.</p>
        """,
        'form_guide_voice': "Mabilis na gabay para sa mga hugis. Pumili ng uri ng hugis. Para sa parihaba o ellipse mag-click nang isang beses, para sa linya o arrow dalawang beses. Iposisyon gamit ang mouse, ayusin ang laki sa mga sulok. I-save gamit ang Enter, itapon gamit ang Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "nakaraan",
        "btn_next_result": "susunod",
        "ocr_text_window": "OCR text window",
        "bookmark_existing": "Umiiral na mga bookmark",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Paghahambing ng OCR Mac - Windows",
        'ocr_method_mac_win_title': "Mga pagkakaiba ng OCR sa pagitan ng Mac at Windows",
        'ocr_method_mac_win_voice': "Mas mahusay ang Mac",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Mga pagkakaiba sa pagitan ng macOS at Windows</strong></p>

        <p><strong>macOS (inirerekomenda)</strong></p>
        <p>Kasangkapan:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resulta:</p>
        <ul>
        <li>Isang mase-search na PDF na may naka-embed na teksto na higit na pinapanatili ang orihinal na layout.</li>
        </ul>
        <p>Mga Bentahe:</p>
        <ul>
        <li>Napakahusay na kalidad ng pagkilala ng teksto (kahit sa mga baku-bakong pahina).</li>
        <li>Pagpapanatili ng vector graphics at mga font.</li>
        <li>GUI progress bar sa pamamagitan ng pagsusuri ng subprocess.</li>
        <li>Ganap na kontrol sa lahat ng parameter ng OCR (Deskew, Clean, Oversample, pag-optimize).</li>
        <li>Ang paghahanap ng teksto ay direktang magagamit sa pangunahing window (pagtingin sa PDF).</li>
        </ul>
        <p>Mga Disbentaha:</p>
        <ul>
        <li>Nangangailangan ng karagdagang mga tool ng system (ocrmypdf, Ghostscript, unpaper, pngquant – kasama sa App Bundle).</li>
        <li>Mas kumplikadong paghawak ng error (deadlocks, timeouts).</li>
        </ul>

        <p><strong>Windows (matatag na alternatibo)</strong></p>
        <p>Kasangkapan:</p>
        <ul>
        <li>pytesseract (direktang koneksyon sa Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resulta:</p>
        <ul>
        <li>Isang mase-search na PDF na biswal na tumutugma sa isang imaheng PDF, ngunit mase-search sa pamamagitan ng transparent na teksto.</li>
        </ul>
        <p>Mga Bentahe:</p>
        <ul>
        <li>Wala akong maisip sa ngayon.</li>
        </ul>
        <p>Mga Disbentaha:</p>
        <ul>
        <li>Ang PDF ay mahalagang isang imahe na may hindi nakikitang teksto; maaaring bahagyang lumihis ang layout para sa mga kumplikadong dokumento (mga column, talahanayan).</li>
        <li>Walang awtomatikong pagwawasto ng pagkiling (--deskew) o paglilinis ng imahe (--clean).</li>
        <li>Ang GUI progress bar ay ina-update lamang nang halos batay sa bilang ng mga naprosesong pahina.</li>
        <li>Medyo mabagal ang bilis ng OCR (dahil ang bawat pahina ay pinoproseso nang hiwalay).</li>
        <li>Ang paghahanap ng teksto ay nire-redirect sa OCR text window.</li>
        </ul>

        <p><strong>Mga Karaniwang Tampok</strong></p>
        <ul>
        <li>Ang parehong pamamaraan ay lumilikha ng isang mase-search na PDF sa parehong direktoryo ng source file.</li>
        <li>Ang mga setting ng OCR (wika, DPI, mode ng pagse-segment ng pahina, mode ng OCR engine) ay maaaring i-configure sa pamamagitan ng OCRSettingsDialog at may bisa sa parehong mga pagpapatupad.</li>
        </ul>

        <p><strong>Rekomendasyon:</strong></p>
        <ul>
        <li>macOS: Ang ocrmypdf binary ay nagbibigay ng pinakamahusay na mga resulta – Bumili ng Mac at gamitin ang bersyon (PDFDarkView para sa Mac na may Apple Silicon o Intel chip). Ang mga resulta ng OCR ay mas mahusay kaysa sa ilalim ng Windows!</li>
        <li>Windows: Gamitin ang pytesseract solution. Ito ay matatag at nagbibigay ng ganap na sapat na kalidad para sa karamihan ng mga dokumento.</li>
        </ul>

        <p><strong>Mahalagang Paalala:</strong></p>
        <ul>
        <li>Ang parehong mga bersyon ay ganap na isinama sa user interface – hindi napapansin ng user ang anumang pagkakaiba.</li>
        <li>Awtomatikong nagpapasya ang programa kung aling OCR engine ang gagamitin batay sa operating system.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Lumikha ng lagda (mula sa scan)",
        "signature_create_title": "Pumili ng na-scan na lagda (PDF/larawan)",
        "image_pdf_filter": "Mga larawan at PDF",
        "signature_pdf_empty": "Ang PDF ay walang laman na mga pahina.",
        "signature_created_success": "Matagumpay na nagawa ang lagda: {0}",
        "signature_create_error": "Error habang lumilikha ng lagda:\n{0}",
        "rembg_missing": "Hindi naka-install ang rembg.\nMangyaring i-install: pip install rembg\nError: {0}",
        "signature_name_title": "Pangalan ng file para sa lagda",
        "signature_name_message": "Mangyaring magpasok ng pangalan ng file para sa bagong lagda (i-save bilang PNG na may transparent na background):",
        "signature_name_label": "Pangalan ng file:",
        "signature_name_voice": "Magpasok ng pangalan ng file para sa lagda",
        "signature_processing": "Nagpoproseso...",
        "signature_creation_title": "Lumilikha ng lagda",
        "signature_overwrite_warning": "Umiiral na ang file na '{0}'. I-overwrite?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Ihanda ang PDF para sa lagda",
        "signature_prepare_instruction":"Mangyaring pumili ng PDF na naglalaman sa isang pahina ng isang na-scan na lagda.\n\nPara sa pinakamainam na pagkilala, tiyakin na:\n• Ang lagda ay nakasulat na may itim na tinta (ballpen o fineliner) sa puting papel.\n• Ang lagda ay nasa itaas na ikatlong bahagi ng kung hindi man ay blangkong pahina ng A4.\n• Ang PDF ay na-scan na may hindi bababa sa 300 dpi.\n• Ang lagda ay malinaw at hindi masyadong manipis.\n• Walang nakakagambalang pattern ng background o mga linya.",
        "signature_prepare_voice":"Mangyaring pumili ng PDF na may na-scan na lagda. Bigyang-pansin ang magandang kalidad at contrast.",
        "sig_thickness_label":"Kapal ng linya:",
        "sig_thickness_normal":"Normal (manipis)",
        "sig_thickness_bold":"Makapal (inirerekomenda)",
        "sig_thickness_very_bold":"Napakakapal",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Magdagdag ng mga wikang GUI at OCR - Gabay",
        'language_guide_title': "Magdagdag ng mga wikang GUI at OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>I-download ang gustong file ng pagsasalin <code>translations_xy.py</code> mula sa<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        at ilagay ito sa sumusunod na direktoryo:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Buksan ang iyong web browser.</li>
        <li>Pumunta sa: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Hanapin sa kanang gilid ng screen ang "Releases" at piliin ang may markang <strong>"latest"</strong>.</li>
        <li>Sa susunod na pahina ng paglabas, i-download ang file na <code>Source Code.zip</code> sa pinakailalim.</li>
        <li>I-unzip ang ZIP file.</li>
        <li>Sa na-unzip na folder, hanapin ang lahat ng kinakailangang file ng wika, at kopyahin ang mga ito sa direktoryo:<br/>
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
        "menu_watermark":"Ipasok ang watermark",
        "fullpage_text_watermark_title":"Teksto bilang watermark",
        "fullpage_image_watermark_title":"Larawan bilang watermark",
        "filename_with_watermark":"_may_watermark",
        "watermark_text":"Teksto:",
        "watermark_text_placeholder":"Iyong watermark na teksto...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Laki ng font:",
        "watermark_format":"Pag-format:",
        "watermark_bold":"Makapal",
        "watermark_italic":"Nakapailalim",
        "watermark_color":"Kulay:",
        "watermark_choose_color":"Pumili ng kulay...",
        "watermark_opacity":"Opacity / Transparency:",
        "watermark_direction":"Direksyon ng pagbasa:",
        "watermark_direction_l_r":"Kaliwa → Kanan",
        "watermark_direction_bl_tr":"Ibaba kaliwa → Itaas kanan",
        "watermark_direction_tl_br":"Itaas kaliwa → Ibaba",
        "watermark_direction_b_t":"Ibaba → Itaas",
        "watermark_direction_t_b":"Itaas → Ibaba",
        "watermark_preview":"Preview:",
        "watermark_preview_sample":"Halimbawang teksto",
        "watermark_empty_text":"Mangyaring maglagay ng teksto.",
        "watermark_applied":"Ang watermark ay inilapat sa lahat ng pahina.",
        "watermark_saved":"Na-save ang watermark.",
        "image_scale":"Laki:",
        "image_preview":"Preview ng larawan:",
        "no_image_selected":"Walang napiling larawan",
        "browse":"Mag-browse...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Mga redaction",
        "redact_add_black": "Redaction (itim)",
        "redact_add_white": "Redaction (puti / burahin)",
        "redact_added_black": "Naidagdag ang itim na redaction",
        "redact_added_white": "Naidagdag ang puting redaction",
        "redact_apply_all": "Ilapat ang lahat ng redaction at i-save",
        "redact_discard_all": "Itapon ang lahat ng redaction",
        "redact_discard": "Itapon ang redaction na ito",
        "no_redactions": "Walang redaction",
        "redact_confirm_title": "Ilapat ang redaction nang permanente",
        "redact_confirm_message": "Babala: Ang mga markadong lugar ay permanenteng tatanggalin (itim o puti).\nGagawa ng backup (kung naka-enable).\n\nMagpatuloy?",
        "redact_apply": "Oo, redact ngayon",
        "redact_saved": "{0} redaction ang matagumpay na nailapat at na-save.",
        "redact_saved_voice": "{0} redaction ang nailapat",
        "redact_error": "Error habang nagre-redact",
        "filename_redacted":"_na-redact",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Ipasok ang mga numero ng pahina',
        'page_numbers_format': 'Format ng numero:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arabic)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Roman maliit)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Roman malaki)',
        'page_numbers_format_letter': 'A, B, C ... (Mga titik)',
        'page_numbers_format_custom': 'Na-customize',
        'page_numbers_custom_pattern': 'Pattern:',
        'page_numbers_custom_placeholder': 'hal. "Pahina {nummer}" o "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Gamitin ang {nummer} para sa kasalukuyang numero ng pahina at {total} para sa kabuuan',
        'page_numbers_position': 'Posisyon:',
        'page_numbers_pos_tl': 'Itaas kaliwa',
        'page_numbers_pos_tc': 'Itaas gitna',
        'page_numbers_pos_tr': 'Itaas kanan',
        'page_numbers_pos_ml': 'Gitna kaliwa',
        'page_numbers_pos_mc': 'Naka-center',
        'page_numbers_pos_mr': 'Gitna kanan',
        'page_numbers_pos_bl': 'Ibaba kaliwa',
        'page_numbers_pos_bc': 'Ibaba gitna',
        'page_numbers_pos_br': 'Ibaba kanan',
        'page_numbers_margins': 'Margin:',
        'page_numbers_margin_x': 'Horizontal na distansya:',
        'page_numbers_margin_y': 'Vertical na distansya:',
        'page_numbers_range': 'Saklaw ng pahina:',
        'page_numbers_all_pages': 'Lahat ng pahina',
        'page_numbers_custom_range': 'Na-customize na saklaw',
        'page_numbers_from': 'Mula:',
        'page_numbers_to': 'Hanggang:',
        'page_numbers_progress': 'Nagpapasok ng mga numero ng pahina...',
        'page_numbers_start': 'Sinisimulan ang pagpasok ng numero ng pahina...',
        'page_numbers_cancel': 'Na-cancel ang pagpasok ng numero ng pahina',
        'page_numbers_success': 'Matagumpay na naidagdag ang mga numero ng pahina.\n\nGusto mo bang buksan ang bagong PDF?\n\n{0}',
        'page_numbers_complete': 'Naidagdag ang mga numero ng pahina',
        'page_numbers_error_format': 'Error habang nagpapasok ng mga numero ng pahina: {0}',
        'page_numbers_content_type': 'Uri ng nilalaman:',
        'page_numbers_tab_simple': 'Simpleng numero',
        'page_numbers_tab_range': 'Pahina X ng Y',
        'page_numbers_tab_date': 'Petsa',
        'page_numbers_tab_custom': 'Malayang teksto',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Pahina {aktuell} ng {gesamt}',
        'page_numbers_range_custom': 'Na-customize',
        'page_numbers_range_placeholder': 'hal. "Pahina {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format ng petsa:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': 'Enero 1, 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Na-customize',
        'page_numbers_date_placeholder': 'hal. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Posisyon:',
        'page_numbers_date_before': 'Petsa bago ang numero ng pahina',
        'page_numbers_date_after': 'Petsa pagkatapos ng numero ng pahina',
        'page_numbers_date_only': 'Petsa lamang (walang numero ng pahina)',
        'page_numbers_custom_text': 'Na-customize na teksto:',
        'page_numbers_custom_placeholder_text': 'Gamitin ang {seite} para sa numero ng pahina at {gesamt} para sa kabuuan\nhal. "Kumpidensyal - Pahina {seite}" o "{seite} ng {gesamt}"',
        "filename_with_page_number":"_may_numero_ng_pahina",
        "filename_with_page_declaration":"_may_deklarasyon_ng_pahina",
        "filename_with_pagenumber":"_may_numero_ng_pahina",
        "filename_with_date":"_may_petsa",
        "filename_with_my_page_declaration":"_may_custom_na_deklarasyon_ng_pahina",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Mga hindi na-save na pagbabago",
        "unsaved_changes_message_darkmode": "May mga hindi na-save na pagpasok.\nGusto mo bang i-save ang mga ito bago lumipat?",
        "save_and_switch": "I-save at lumipat",
        "discard_and_switch": "Lumipat ngayon",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'I-export ang mga pahina bilang mga larawan',
        'export_images_menu': 'I-export bilang mga larawan (PNG/JPEG)',
        'export_images_format': 'Format ng larawan:',
        'export_images_dpi': 'Resolusyon (DPI):',
        'export_images_quality': 'Kalidad ng JPEG:',
        'export_images_range': 'Saklaw ng pahina:',
        'export_images_all_pages': 'Lahat ng pahina',
        'export_images_custom_range': 'Na-customize na saklaw',
        'export_images_from': 'Mula:',
        'export_images_to': 'Hanggang:',
        'export_images_options': 'Mga opsyon:',
        'export_images_single_files': 'Bawat pahina bilang hiwalay na file',
        'export_images_subfolder': 'I-export sa subfolder',
        'export_images_subfolder_info': 'Sa subfolder na "pangalanPDF_mga_larawan"',
        'export_images_same_folder': 'Sa parehong folder ng PDF',
        'export_images_apply_darkmode': 'Ilapat ang mga setting ng PDFDarkView (Dark Mode)',
        'export_images_target_folder': 'Target na folder:',
        'export_images_browse': 'Mag-browse...',
        'export_images_preview': 'Preview:',
        'export_images_preview_info': 'Pumili ng mga setting para sa pag-export',
        'export_images_preview_info_detail': '{0} pahina bilang {1}\nResolusyon: {2} DPI\nPangalan ng file: {3}\n{4}',
        'export_images_select_folder': 'Pumili ng target na folder',
        'export_images_start': 'Sinisimulan ang pag-export ng larawan...',
        'export_images_progress': 'Nag-e-export ng mga larawan...',
        'export_images_saving': 'Sine-save ang pahina {0} ng {1}...',
        'export_images_success': 'Matagumpay ang pag-export!\n\n{0} mga larawan ang na-save sa:\n{1}',
        'export_images_complete': 'Nakumpleto ang pag-export ng larawan',
        'export_images_open_folder': '📁 Buksan ang folder',
        'export_images_cancel': 'Na-cancel ang pag-export ng larawan',
        'export_images_error_format': 'Error habang nag-e-export ng mga larawan: {0}',
        'export_images_pdf2image_missing': 'Ang library na "pdf2image" ay hindi naka-install.\n\nPak i-install ito gamit ang:\npip install pdf2image\n\nPara sa Windows kailangan mo rin ng Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A conversion para sa pangmatagalang pag-archive',
        'pdfa_menu': 'PDF/A conversion (angkop para sa archive)',
        'pdfa_info': 'Kino-convert ang PDF sa PDF/A format.\n\nAng PDF/A ay espesyal na idinisenyo para sa pangmatagalang pag-archive at tinitiyak na ang dokumento ay ipapakita nang tama sa hinaharap.',
        'pdfa_standard': 'PDF/A standard:',
        'pdfa_standard_select': 'Bersyon:',
        'pdfa_1': 'PDF/A-1 (simple, malawak na compatible)',
        'pdfa_2': 'PDF/A-2 (moderno, mas mahusay na compression)',
        'pdfa_3': 'PDF/A-3 (pinakabagong bersyon, pinapayagan ang mga attachment)',
        'pdfa_standards_explanation': '📖 Paliwanag ng mga standard:\n\n'
            '• PDF/A-1: Basic, compatible sa mas lumang sistema (mga 2005)\n'
            '• PDF/A-2: Mas moderno, mas mahusay na compression, suporta sa transparency (mga 2011)\n'
            '• PDF/A-3: Pinakabagong bersyon, pinapayagan ang pag-embed ng mga file attachment (mga 2013)\n\n'
            'Rekomendasyon: Ang PDF/A-2 ay isang magandang kompromiso sa pagitan ng compatibility at modernong mga feature.',
        'pdfa_options': 'Mga opsyon:',
        'pdfa_compress_enable': 'I-compress ang PDF (mas maliit na file)',
        'pdfa_metadata_preserve': 'Panatilihin ang metadata (pamagat, may-akda, atbp.)',
        'pdfa_target_folder': 'Target na folder:',
        'pdfa_browse': 'Mag-browse...',
        'pdfa_select_folder': 'Pumili ng target na folder',
        'pdfa_ocr_info_unknown': '🔍 Hindi masuri ang nilalaman ng teksto.',
        'pdfa_ocr_info_not_needed': '✅ Available ang teksto - hindi kailangan ang OCR.\nMaaaring direktang gawin ang PDF/A.',
        'pdfa_ocr_info_recommended': '⚠️ Walang sapat na teksto na natagpuan.\n\nPara sa mga searchable na PDF, inirerekomenda naming patakbuhin muna ang OCR.\nTandaan: Gumagana ang PDF/A kahit walang OCR - ngunit ang teksto ay hindi magiging searchable.',
        'pdfa_ocr_info_error': '❌ Error habang sinusuri: {0}',
        'pdfa_start': 'Sinisimulan ang PDF/A conversion...',
        'pdfa_progress': 'Nagaganap ang PDF/A conversion...',
        'pdfa_success': 'Matagumpay ang PDF/A conversion!\n\nNa-save bilang:\n{0}\n\nGusto mo bang buksan ang bagong PDF?',
        'pdfa_complete': 'Nakumpleto ang PDF/A conversion',
        'pdfa_cancel': 'Na-cancel ang PDF/A conversion',
        'pdfa_error_format': 'Error habang nagko-convert ng PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Ang library na "ocrmypdf" ay hindi naka-install.\n\nPak i-install ito gamit ang:\npip install ocrmypdf',
        'btn_convert': 'I-convert',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'I-optimize ang PDF (bawasan ang laki ng file)',
        'optimize_menu': 'I-optimize ang PDF (laki ng file)',
        'optimize_info': 'Binabawasan ang laki ng PDF file sa pamamagitan ng iba\'t ibang paraan ng pag-optimize.\n\nKung mas mataas ang antas ng compression, mas maliit ang file - na may posibleng pagkawala ng kalidad sa mga larawan.',
        'optimize_level': 'Antas ng compression:',
        'optimize_level_low': 'Mababa (mabilis, maliit na ipon)',
        'optimize_level_medium': 'Katamtaman (magandang kompromiso)',
        'optimize_level_high': 'Mataas (malaking ipon)',
        'optimize_level_maximum': 'Maximum (maximum na ipon, mabagal)',
        'optimize_level_explanation': 'Rekomendasyon: Ang "Katamtaman" ay isang magandang kompromiso sa pagitan ng bilis at laki ng file.',
        'optimize_options': 'Mga opsyon:',
        'optimize_compress_images': 'I-compress ang mga larawan (bawasan ang kalidad ng JPEG)',
        'optimize_clean_objects': 'Alisin ang mga hindi nagamit na bagay',
        'optimize_preserve_metadata': 'Panatilihin ang metadata (pamagat, may-akda, atbp.)',
        'optimize_image_quality': 'Kalidad ng larawan:',
        'optimize_range': 'Saklaw ng pahina:',
        'optimize_all_pages': 'Lahat ng pahina',
        'optimize_custom_range': 'Na-customize na saklaw',
        'optimize_from': 'Mula:',
        'optimize_to': 'Hanggang:',
        'optimize_target_folder': 'Target na folder:',
        'optimize_browse': 'Mag-browse...',
        'optimize_select_folder': 'Pumili ng target na folder',
        'optimize_info_box': 'Impormasyon',
        'optimize_info_text': 'Maaaring tumagal ng ilang minuto ang pag-optimize para sa malalaking PDF.\n\nAng mga larawan ay sine-save na may mas mababang kalidad, na maaaring makabuluhang bawasan ang laki ng file.',
        'optimize_start': 'Sinisimulan ang PDF optimization...',
        'optimize_progress': 'Ino-optimize ang PDF...',
        'optimize_cancel': 'Na-cancel ang PDF optimization',
        'optimize_complete': 'Nakumpleto ang PDF optimization',
        'optimize_error_format': 'Error habang nag-o-optimize ng PDF:\n\n{0}',
        'optimize_success_message': 'Matagumpay ang PDF optimization!\n\nNa-save bilang:\n{0}\n\nDati: {1}\nNgayon: {2}\nIpon: {3:.1f}%\n\n{4}\n\nGusto mo bang buksan ang na-optimize na PDF?',
        'optimize_success_message_no_size': 'Matagumpay ang PDF optimization!\n\nNa-save bilang:\n{0}\n\nHindi available ang impormasyon sa laki.\n\nGusto mo bang buksan ang na-optimize na PDF?',
        'optimize_result_positive': 'Ang file ay nabawasan ng {0:.1f}%.',
        'optimize_result_zero': 'Walang pagbabago sa laki ng file.',
        'optimize_result_negative': 'Ang file ay tumaas ng {0:.1f}%.\nLinalaktawan ang pag-optimize, ang orihinal na file ay pinanatili.',
        'btn_optimize': 'Simulan ang pag-optimize',
        'filename_optimize_low_suffix': '_na-optimize_mababa',
        'filename_optimize_medium_suffix': '_na-optimize',
        'filename_optimize_high_suffix': '_na-optimize_mataas',
        'filename_optimize_maximum_suffix': '_na-optimize_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'I-crop ang PDF',
        'crop_menu': 'I-crop ang PDF (Crop)',
        'crop_range': 'Ilapat sa:',
        'crop_all_pages': 'Lahat ng pahina',
        'crop_current_page': 'Kasalukuyang pahina lamang',
        'crop_values': 'Mga halaga ng crop (sa mga puntos):',
        'crop_left': 'Kaliwa:',
        'crop_right': 'Kanan:',
        'crop_top': 'Itaas:',
        'crop_bottom': 'Ibaba:',
        'crop_presets': 'Mga preset:',
        'crop_preset_white': 'Tuklasin ang puting margin',
        'crop_reset': 'I-reset',
        'crop_mouse_hint': '🖱️ I-drag ang isang parihaba upang halos pumili ng lugar.\nPagkatapos ay maaari mong ayusin ang mga halaga nang tumpak sa SpinBoxes.\nHindi posible ang manu-manong pagsasaayos gamit ang mouse.',
        'crop_apply': 'I-crop',
        'crop_scope_all': 'Lahat ng pahina',
        'crop_scope_current': 'Kasalukuyang pahina',
        'crop_new_size': 'Bagong laki: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Walang PDF na na-load',
        'crop_preview_error': 'Error habang naglo-load ng preview',
        'crop_start': 'Sinisimulan ang pag-crop...',
        'crop_progress': 'Nag-crop ng PDF...',
        'crop_success': 'Matagumpay na na-crop ang PDF!\n\nNa-save bilang:\n{0}\n\nGusto mo bang buksan ang na-crop na PDF?',
        'crop_complete': 'Nakumpleto ang pag-crop',
        'crop_cancel': 'Na-cancel ang pag-crop',
        'crop_error_format': 'Error habang nag-crop:\n\n{0}',
        'filename_crop_suffix': '_na-crop',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Patagin ang PDF (Flatten)',
        'flatten_menu': 'Patagin ang PDF (Flatten)',
        'flatten_info': 'Ang pagpapatag ng PDF ay "nagsusunog" ng lahat ng nabe-edit na elemento sa nilalaman ng pahina.\n\nPagkatapos nito, ang mga field ng form, anotasyon, teksto, krus, lagda, larawan at hugis ay hindi na nabe-edit nang paisa-isa.',
        'flatten_explanation_title': '📖 Para saan ito maganda?',
        'flatten_explanation_text': 'Ang pagpapatag ay kinakailangan sa mga sumusunod na sitwasyon:\n\n'
            '• 📄 Gusto mong ihanda ang dokumento para sa pag-print\n'
            '• 🔒 Gusto mong pigilan ang isang tao na baguhin ang mga field ng form\n'
            '• 📎 Gusto mong "i-embed" ang mga anotasyon at komento sa dokumento\n'
            '• 🖼️ Gusto mong i-angkla ang mga teksto, krus, lagda, larawan at hugis sa dokumento\n'
            '• 📦 Gusto mong ihanda ang file para sa pag-archive\n\n'
            'Ang pagpapatag ay nagpapaliit ng PDF at pinipigilan ang mga elemento na hindi sinasadyang ilipat o tanggalin.',
        'flatten_what_title': 'Ano ang pinapatag?',
        'flatten_what_list': '• ✅ Mga field ng form (mga text field, checkbox, button)\n'
            '• ✅ Mga anotasyon (komento, highlight, tala)\n'
            '• ✅ Mga overlay (teksto, krus, lagda, larawan, hugis)',
        'flatten_options': 'Mga opsyon:',
        'flatten_forms': 'Patagin ang mga field ng form',
        'flatten_annotations': 'Patagin ang mga anotasyon',
        'flatten_overlays': 'Patagin ang mga overlay (teksto, krus, lagda, larawan, hugis)',
        'flatten_target_folder': 'Target na folder:',
        'flatten_browse': 'Mag-browse...',
        'flatten_select_folder': 'Pumili ng target na folder',
        'flatten_warning': '⚠️ Mahalaga: Ang pagpapatag ay isang hindi maibabalik na proseso!\n\nPagkatapos ng pagpapatag, ang mga nabe-edit na elemento ay hindi na maaaring baguhin o tanggalin nang paisa-isa.\nGumawa ng backup nang maaga kung kinakailangan.',
        'flatten_apply': 'Patagin',
        'flatten_start': 'Sinisimulan ang pagpapatag...',
        'flatten_progress': 'Pinapatag ang PDF...',
        'flatten_success': 'Matagumpay na napatag ang PDF!\n\nNa-save bilang:\n{0}\n\nGusto mo bang buksan ang napapatag na PDF?',
        'flatten_complete': 'Nakumpleto ang pagpapatag',
        'flatten_cancel': 'Na-cancel ang pagpapatag',
        'flatten_error_format': 'Error habang nagpapatag:\n\n{0}',
        'filename_flatten_suffix': '_napapatag',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF overlay (Overlay)',
        'overlay_menu': 'PDF overlay (Overlay)',
        'overlay_info': 'Naglalagay ng isang PDF (overlay) sa ibabaw ng isa pang PDF.\n\nAng overlay na PDF ay inilalagay sa base PDF. Ito ay kapaki-pakinabang para sa mga watermark, logo, letterhead o stamp.',
        'overlay_explanation_title': '📖 Para saan ito maganda?',
        'overlay_explanation_text': 'Ang overlay ay kinakailangan sa mga sumusunod na sitwasyon:\n\n'
            '• 🏢 Maglagay ng logo ng kumpanya bilang watermark sa bawat pahina\n'
            '• 📄 Maglagay ng letterhead sa isang blangkong PDF\n'
            '• 🖊️ Maglagay ng stamp overlay sa isang dokumento\n'
            '• 🔖 Maglagay ng watermark sa lahat ng pahina\n'
            '• 📑 Maglagay ng form overlay sa isang template',
        'overlay_type': 'Uri ng overlay:',
        'overlay_type_fullpage': 'Buong pahina (sumasaklaw)',
        'overlay_type_transparent': 'Buong pahina (transparent - inirerekomenda)',
        'overlay_type_stamp': 'Stamp (napaposisyon)',
        'overlay_type_info_fullpage': '📄 Ang overlay na PDF ay inilalagay nang eksakto sa buong pahina.\nAng puting background ay maaaring alisin upang ang nilalaman lamang ang manatiling nakikita.',
        'overlay_type_info_transparent': '🔍 Ang overlay na PDF ay inilalagay sa buong pahina na may transparent na background.\nAng puting background ay awtomatikong inaalis - perpekto para sa mga watermark at logo!',
        'overlay_type_info_stamp': '🖊️ Ang overlay na PDF ay ipinoposisyon at ini-scale bilang isang stamp.\nPerpekto para sa mga logo, stamp o lagda sa mga partikular na posisyon.',
        'overlay_remove_background': 'Alisin ang puting background:',
        'overlay_remove_background_enable': 'Alisin ang puting background mula sa overlay na PDF (ginagawang transparent ang overlay)',
        'overlay_remove_background_tooltip': 'Nag-aalis ng mga puting lugar mula sa overlay na PDF upang makita ang nakapailalim na teksto.',
        'overlay_threshold': 'Halaga ng threshold:',
        'overlay_threshold_hint': '(1-254, mas mataas = mas maraming puti ang tinatanggal)',
        'overlay_select_file': 'Pumili ng overlay na PDF:',
        'overlay_file_placeholder': 'Mangyaring pumili ng PDF file para sa overlay',
        'overlay_browse': 'Mag-browse...',
        'overlay_select_overlay': 'Pumili ng overlay na PDF',
        'overlay_range': 'Saklaw ng pahina:',
        'overlay_all_pages': 'Lahat ng pahina',
        'overlay_custom_range': 'Na-customize na saklaw',
        'overlay_from': 'Mula:',
        'overlay_to': 'Hanggang:',
        'overlay_position': 'Posisyon:',
        'overlay_position_center': 'Gitna',
        'overlay_position_top_left': 'Itaas kaliwa',
        'overlay_position_top_right': 'Itaas kanan',
        'overlay_position_bottom_left': 'Ibaba kaliwa',
        'overlay_position_bottom_right': 'Ibaba kanan',
        'overlay_size': 'Laki:',
        'overlay_size_original': 'Orihinal na laki',
        'overlay_size_fit_page': 'Pagkasyahin sa pahina',
        'overlay_size_custom': 'Na-customize (%)',
        'overlay_opacity': 'Transparency:',
        'overlay_target_folder': 'Target na folder:',
        'overlay_browse_folder': 'Mag-browse...',
        'overlay_select_folder': 'Pumili ng target na folder',
        'overlay_warning': '⚠️ Tandaan: Ang overlay na PDF ay inilalagay sa base PDF at "sinusunog" dito.\n\nAng mga elemento ng overlay na PDF ay hindi na maaaring i-edit nang paisa-isa pagkatapos i-save.',
        'overlay_apply': 'Mag-overlay',
        'overlay_start': 'Sinisimulan ang overlay...',
        'overlay_progress': 'Nag-o-overlay ng PDF...',
        'overlay_success': 'Matagumpay na na-overlay ang PDF!\n\nNa-save bilang:\n{0}\n\nGusto mo bang buksan ang na-overlay na PDF?',
        'overlay_complete': 'Nakumpleto ang overlay',
        'overlay_cancel': 'Na-cancel ang overlay',
        'overlay_error_format': 'Error habang nag-o-overlay:\n\n{0}',
        'overlay_no_file': 'Walang napiling overlay na PDF.\n\nMangyaring pumili ng PDF file para i-overlay.',
        'filename_overlay_suffix': '_na-overlay',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'I-extract ang mga larawan mula sa PDF',
        'extract_images_menu': 'I-extract ang lahat ng larawan',
        'extract_images_info': 'Nag-e-extract ng lahat ng larawan mula sa PDF at sine-save ang mga ito bilang magkakahiwalay na file.\n\nAng mga larawan ay sine-save sa kanilang orihinal na format o kina-convert sa isang napiling format.',
        'extract_images_format': 'Format ng larawan:',
        'extract_images_quality': 'Kalidad ng JPEG:',
        'extract_images_options': 'Mga opsyon:',
        'extract_images_subfolder': 'I-extract sa subfolder ("pangalanPDF_mga_larawan")',
        'extract_images_unique': 'Mga natatanging larawan lamang (iwasan ang mga duplicate)',
        'extract_images_range': 'Saklaw ng pahina:',
        'extract_images_all_pages': 'Lahat ng pahina',
        'extract_images_custom_range': 'Na-customize na saklaw',
        'extract_images_from': 'Mula:',
        'extract_images_to': 'Hanggang:',
        'extract_images_target_folder': 'Target na folder:',
        'extract_images_browse': 'Mag-browse...',
        'extract_images_select_folder': 'Pumili ng target na folder',
        'extract_images_info_box': 'Impormasyon',
        'extract_images_info_text': 'Maaaring tumagal ng ilang minuto ang pag-extract para sa malalaking PDF.\n\nAng mga larawan ay sine-save gamit ang kanilang orihinal na pangalan (pahina_larawan).',
        'extract_images_extract': 'I-extract',
        'extract_images_start': 'Sinisimulan ang pag-extract...',
        'extract_images_progress': 'Nag-e-extract ng mga larawan...',
        'extract_images_success': '✅ Matagumpay na na-extract ang mga larawan!\n\n{0} mga larawan ang na-save sa:\n{1}',
        'extract_images_complete': 'Nakumpleto ang pag-extract ng larawan',
        'extract_images_cancel': 'Na-cancel ang pag-extract',
        'extract_images_error_format': 'Error habang nag-e-extract ng mga larawan:\n\n{0}',
        'extract_images_open_folder': '📁 Buksan ang folder',
        'extract_images_no_images': 'Walang nakitang larawan sa PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Maramihang pahina sa isang pahina (N-Up)',
        'nup_menu': 'Maramihang pahina sa isang pahina (N-Up)',
        'nup_info': 'Inaayos ang maraming PDF pahina sa isang pahina.\n\nPerpekto para sa mga compact print, overview o handout.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Preview:',
        'nup_preview_info': '{0} pahina → {1} pahina bawat sheet → {2} sheet\nLayout: {3}',
        'nup_order': 'Pagkakasunud-sunod:',
        'nup_order_horizontal': 'Pahalang (hilera bawat hilera)',
        'nup_order_vertical': 'Patayo (kolum bawat kolum)',
        'nup_order_horizontal_reverse': 'Pahalang na baligtad',
        'nup_order_vertical_reverse': 'Patayo na baligtad',
        'nup_range': 'Saklaw ng pahina:',
        'nup_all_pages': 'Lahat ng pahina',
        'nup_custom_range': 'Na-customize na saklaw',
        'nup_from': 'Mula:',
        'nup_to': 'Hanggang:',
        'nup_options': 'Mga opsyon:',
        'nup_margins': 'Margin:',
        'nup_margin_between': 'Espasyo sa pagitan ng mga pahina:',
        'nup_page_numbers': 'Ipasok ang mga numero ng pahina',
        'nup_target_folder': 'Target na folder:',
        'nup_browse': 'Mag-browse...',
        'nup_select_folder': 'Pumili ng target na folder',
        'nup_create': 'Lumikha',
        'nup_start': 'Sinisimulan ang N-Up...',
        'nup_progress': 'Gumagawa ng N-Up...',
        'nup_success': 'Matagumpay na ginawa ang N-Up!\n\nNa-save bilang:\n{0}\n\nGusto mo bang buksan ang bagong PDF?',
        'nup_complete': 'Nakumpleto ang N-Up',
        'nup_cancel': 'Na-cancel ang N-Up',
        'nup_error_format': 'Error habang ginagawa ang N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Baguhin ang laki ng pahina',
        'pagesize_menu': 'Baguhin ang laki ng pahina',
        'pagesize_info': 'Binabago ang laki ng pahina ng PDF.\n\nAng nilalaman ay awtomatikong inaayos sa bagong laki.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Pumili ng standard na format:',
        'pagesize_custom': 'Na-customize na laki:',
        'pagesize_width': 'Lapad:',
        'pagesize_height': 'Taas:',
        'pagesize_orientation': 'Orientasyon:',
        'pagesize_portrait': 'Patayo',
        'pagesize_landscape': 'Pahalang',
        'pagesize_scale_options': 'Mga opsyon sa pag-scale:',
        'pagesize_fit': 'Pagkasyahin (panatilihin ang aspect ratio)',
        'pagesize_stretch': 'I-stretch (i-distort)',
        'pagesize_center': 'I-center (orihinal na laki)',
        'pagesize_range': 'Saklaw ng pahina:',
        'pagesize_all_pages': 'Lahat ng pahina',
        'pagesize_custom_range': 'Na-customize na saklaw',
        'pagesize_from': 'Mula:',
        'pagesize_to': 'Hanggang:',
        'pagesize_target_folder': 'Target na folder:',
        'pagesize_browse': 'Mag-browse...',
        'pagesize_select_folder': 'Pumili ng target na folder',
        'pagesize_apply': 'Ilapat',
        'pagesize_start': 'Sinisimulan ang pagbabago ng laki ng pahina...',
        'pagesize_progress': 'Binabago ang laki ng pahina...',
        'pagesize_success': 'Matagumpay na nabago ang laki ng pahina!\n\nNa-save bilang:\n{0}\n\nGusto mo bang buksan ang bagong PDF?',
        'pagesize_complete': 'Nakumpleto ang pagbabago ng laki ng pahina',
        'pagesize_cancel': 'Na-cancel ang pagbabago ng laki ng pahina',
        'pagesize_error_format': 'Error habang binabago ang laki ng pahina:\n\n{0}',
        'pagesize_preview_info': 'Bagong laki: {0} x {1} pt',
        'filename_pagesize_suffix': '_bagong_laki',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Impormasyon sa PDF',
        'pdf_info_menu': 'Ipakita ang impormasyon sa PDF',
        'pdf_info_voice': 'Ipinapakita ang impormasyon sa PDF',
        'pdf_info_error': 'Error habang ipinapakita ang impormasyon sa PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Ipakita ang mga keyboard shortcut",
        "shortcuts_dialog_title": "Mga Keyboard Shortcut",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FILE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Buksan ang PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Isara ang PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>I-save bilang...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Protektahan ang dokumento</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Mag-print</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Mag-print agad (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Lumabas sa application</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>I-export bilang Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>I-export bilang DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>I-export bilang TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>I-export bilang mga larawan (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>I-extract ang mga larawan</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PAGPROSESO NG DOKUMENTO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Maramihang pahina)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A conversion (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Patagin ang PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF overlay</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>I-optimize ang PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDIT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Maghanap</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Magdagdag ng bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Pamahalaan ang mga bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Susunod na bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Nakaraang bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Patakbuhin ang OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 PAMAMAHALA NG PAHINA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>I-rotate ang kasalukuyang pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>I-rotate ang lahat ng pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>I-normalize ang kasalukuyang pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>I-normalize ang lahat ng pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Burahin ang mga pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>I-extract ang mga pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Ipasok ang mga pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Ilipat ang mga pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Pagsamahin ang mga PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Baguhin ang laki ng pahina</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 IPASOK</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Ipasok ang teksto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Ipasok ang krus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Ipasok ang lagda 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Ipasok ang lagda 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Ipasok ang larawan</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Ipasok ang parihaba</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ipasok ang ellipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Ipasok ang linya</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Ipasok ang arrow</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Ipasok ang mga numero ng pahina</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Watermark ng teksto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Watermark ng larawan</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ MGA REDACTION</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redaction (itim)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redaction (puti)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Ilapat ang lahat ng redaction</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ADVANCED</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>I-crop ang PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>I-edit ang metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VIEW</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>I-toggle ang Dark/Light Mode</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Ipakita ang text window</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Lapad ng pahina (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dalawang pahina (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Pangkalahatang-tanaw (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ MGA SETTING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Pamamahala ng password</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Mga setting ng OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Mga setting ng lagda</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Pag-format ng pangalan ng file</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>I-export ang mga setting</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>I-import ang mga setting</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ IMPORMASYON</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Ipakita ang impormasyon sa PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>I-toggle ang voice output</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Pagtuunan ang menu bar</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "May bagong bersyon",
        "update_available_message": "May bagong bersyon <b>{0}</b>.\n\nBisitahin ang pahina ng release upang i-download ang update:\n{1}",
        "update_available_voice": "May bagong bersyon {0}. Pakii-download ang update mula sa pahina ng GitHub.",
        "update_open_release": "Buksan ang pahina ng release",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "I-download ang lahat ng pagsasalin",
        "ask_download_all_translations": """Bukod sa German, English at Vietnamese, mayroong {total_languages} pang GUI na wika.\n\nDapat bang ibigay / i-update ang mga ito?\n\nTandaan:\nAng mga hindi kinakailangang wika ay maaari mong manu-manong tanggalin sa direktoryo:\n{translations_path}
        \nKung kakanselahin mo, maaari mong i-download ang mga GUI na wika sa ibang pagkakataon sa pamamagitan ng menu 'Mga Tool → I-update ang mga pagsasalin'.""",
        "menu_update_translations": "I-update ang mga pagsasalin",
        "translations_updated": "Na-update ang mga pagsasalin",
        "translations_update_success": "{} mga pagsasalin ang matagumpay na na-update ({} bago, {} na-update).",
        "translations_update_error": "Error sa pag-update ng mga pagsasalin",
        "translations_update_no_changes": "Lahat ng pagsasalin ay napapanahon na.",
        "translations_update_offline": "Walang koneksyon sa internet. Hindi ma-update ang mga pagsasalin.",
        "translations_update_in_progress": "Ang mga pagsasalin ay ina-update sa background...",
        "translations_downloading": "Nagda-download ng mga pagsasalin...",
        "translations_path_hint": "Direktoryo ng gumagamit para sa mga pagsasalin",
        "translations_update_not_available_title": "Hindi available ang update",
        "translations_update_not_available_message": """Ang pag-update ng mga pagsasalin ay available lamang sa naka-install na bersyon.\n\nSa development mode, ang mga pagsasalin ay napapanahon na.""",
        "translations_update_no_internet_title": "Walang koneksyon sa internet",
        "translations_update_no_internet_message": """Hindi makapagtatag ng koneksyon sa internet.\n\nHindi ma-download ang mga pagsasalin mula sa GitHub.\n\nMga posibleng solusyon:
        • Suriin ang iyong koneksyon sa internet
        • Huwag paganahin ang anumang firewall pansamantala
        • Subukan muli sa ibang pagkakataon
        \nMaaari mo ring manu-manong i-download ang mga pagsasalin mula sa GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Ang update ay kasalukuyang isinasagawa",
        "btn_retry": "Subukan muli",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Maligayang pagdating sa PDF Dark View",
        "welcome_title_not_supported": "Maligayang pagdating sa PDF Dark View",
        "welcome_message": "Maligayang pagdating sa PDF Dark View!\n\nAng iyong wika ng sistema ay nakilala bilang '{language}'.\nGusto mo bang gamitin ang wikang ito para sa interface ng gumagamit?\n\nMaaari mong baguhin ang wika anumang oras sa pamamagitan ng 'Mga Setting → Wika'.",
        "welcome_message_language_not_available": "Maligayang pagdating sa PDF Dark View!\n\nAng iyong wika ng sistema ay nakilala bilang '{language}'.\nAng wikang ito ay hindi pa naka-install.\n\nGusto mo bang i-download ang mga pagsasalin para sa {language} ngayon mula sa GitHub?\n\n(Ang wika ay awtomatikong gagamitin para sa interface ng gumagamit.)",
        "welcome_message_language_not_supported": "Maligayang pagdating sa PDF Dark View!\n\nAng iyong wika ng sistema ay nakilala bilang '{language}'.\nSa kasamaang-palad, wala pang mga pagsasalin para sa wikang ito.\n\nAng interface ng gumagamit ay ipapakita sa {fallback_language}.\n\nMaaari mong baguhin ang wika anumang oras sa pamamagitan ng 'Mga Setting → Wika'.\nKung gusto mo, maaari ka ring mag-ambag ng pagsasalin para sa iyong wika:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Oo, gamitin ang wika ng sistema",
        "welcome_keep_english": "Hindi, panatilihin ang Ingles",
        "welcome_download_language": "Oo, i-download ang {language}",

        # ============================================
        # 107. MGA BAGONG GINAMIT NA LANDAS
        # ============================================

        'menu_recent': 'Kamakailang ginamit',
        'menu_recent_dirs': 'Mga Direktoryo...',
        'menu_recent_files': 'Mga File...',
        'recent_manage': 'Pamahalaan...',
        'recent_enable_tracking': 'I-save ang mga bagong landas (privacy)',
        'recent_enable_info': 'I-disable ang opsyong ito upang hindi mag-save ng mga landas',
        'recent_tracking_disabled': 'Ang pagsubaybay sa landas ay hindi pinagana',
        'recent_enabled': 'pinagana',
        'recent_disabled': 'hindi pinagana',
        'recent_tracking_status': 'Pagsubaybay sa landas {0}',
        'recent_dialog_title': 'Mga bagong landas',
        'recent_tab_directories': 'Mga Direktoryo',
        'recent_tab_files': 'Mga File',
        'recent_dirs_instruction': 'Mag-double click upang buksan ang dialog ng file sa direktoryo',
        'recent_files_instruction': 'Mag-double click upang direktang buksan ang PDF',
        'recent_no_directories': '(walang naka-save na direktoryo)',
        'recent_no_files': '(walang naka-save na file)',
        'recent_default_current': '⭐ Default: {0}',
        'recent_set_as_default': '⭐ Itakda bilang default',
        'recent_default_set_title': 'Naitakda ang default na direktoryo',
        'recent_default_set_message': 'Ang direktoryo "{0}" ay naitakda bilang default para sa pagbubukas ng PDF.',
        'recent_default_set_voice': 'Naitakda ang default na direktoryo',
        'recent_directory_not_found': 'Hindi natagpuan ang direktoryo',
        'recent_file_not_found': 'Hindi natagpuan ang file',
        'recent_remove_selected': 'Alisin',
        'recent_remove_title': 'Alisin ang landas',
        'recent_remove_confirm': 'Sigurado ka bang gusto mong alisin ang landas "{0}" mula sa listahan?',
        'recent_path_removed': 'Inalis ang landas',
        'recent_clear_all': 'Alisin lahat',
        'recent_clear_title': 'Alisin ang lahat ng landas',
        'recent_clear_confirm_type': 'Sigurado ka bang gusto mong tanggalin ang lahat ng {0}?',
        'recent_cleared': 'Nalinis ang listahan',
        'recent_path_not_found_title': 'Hindi natagpuan ang landas',
        'recent_path_not_found_message': 'Ang landas "{0}" ay wala na.',
        'recent_open_file': 'Buksan ang file',
        'btn_open_recent': 'Buksan',
        'recent_open_file_question': 'Gusto mo bang buksan ang "{0}" bilang PDF?',
        'recent_not_pdf': 'Ang napiling file ay hindi PDF.',
        'recent_more_entries': 'Higit pang mga entry...',
        'btn_remove': 'Alisin',
        'btn_clear': 'Linisan lahat',
        'recent_context_open': 'Buksan',
        'recent_context_reveal': 'Ipakita sa Finder',
        'recent_context_set_default': '⭐ Itakda bilang default',
        'recent_context_open_terminal': '💻 Buksan ang Terminal',
        'recent_context_file_info': 'Impormasyon ng file',
        'recent_context_open_with_default': '📄 Buksan gamit ang default na app',
        'recent_context_remove': 'Alisin mula sa listahan',
        'recent_context_clear_all': 'Alisin lahat',
        'recent_file_info_title': 'Impormasyon ng file',
        'recent_file_info_name': 'Pangalan',
        'recent_file_info_path': 'Landas',
        'recent_file_info_size': 'Laki',
        'recent_file_info_modified': 'Binago',
        'recent_file_info_pages': 'Mga Pahina',
        'recent_error_reveal': 'Error sa pagbukas sa Finder',
        'recent_error_terminal': 'Error sa pagbukas ng Terminal',
        'recent_error_info': 'Error sa pagkuha ng impormasyon ng file',
        'open_user_data_folder': 'Ipakita ang direktoryo ng data ng user',

        # ============================================
        # 108. BURAHIN ANG MGA PANTAY/HINDI PANTAY NA PAHINA
        # ============================================
        "pages_delete_even": "Burahin ang lahat ng pantay na pahina",
        "pages_delete_odd":  "Burahin ang lahat ng hindi pantay na pahina",
        "progress_even_pages": "Binubura ang mga pantay na pahina",
        "progress_odd_pages": "Binubura ang mga hindi pantay na pahina",
        "progress_mark_delete_even": "{} pantay na pahina ang minarkahan para burahin",
        "progress_mark_delete_odd":  "{} hindi pantay na pahina ang minarkahan para burahin",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Nagsasara ang programa",

    }
