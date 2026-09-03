
# ============================================
# translations_sw.py - Suaheli Wörterbuch für PDFDarkView
# Vollständig sortiert nach Kategorien
# ============================================

def load_swahili_strings():
    """Lädt alle Suaheli Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Pakia PDF",
        'btn_text_window': "Maandishi ya OCR",
        'btn_first': "Ukurasa wa Kwanza",
        'btn_prev': "Ukurasa uliopita",
        'btn_next': "Ukurasa ujao",
        'btn_last': "Ukurasa wa Mwisho",
        'btn_print': "Chapisha",
        'btn_darkmode_light': "Mwezi Mwanga",
        'btn_darkmode_dark': "Mwezi Giza",
        'btn_delete_pages': "Futa kurasa",
        'btn_extract_pages': "Toa kurasa",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "Sawa",
        'btn_cancel': "Ghairi",
        'btn_save': "Hifadhi",
        'btn_close': "Funga",
        'btn_delete': "Futa",
        'btn_delete_all': "Futa zote",
        'btn_copy': "Nakili",
        'btn_export': "Hamisha nje",
        'btn_show': "Onyesha nenosiri",
        'btn_hide': "Ficha nenosiri",
        'btn_authenticate': "Thibitisha",
        'btn_settings': "Mipangilio",
        'btn_protect': "Linda",
        'btn_remove_password': "Ondoa nenosiri",
        'btn_manage': "Usimamizi wa nenosiri",
        'btn_retry': "Jaribu tena",
        'btn_select_all': "Chagua zote",
        'btn_clear_selection': "Futa uteuzi",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Ukurasa {0} kati ya {1}",
        'page_count': "kati ya {0}",
        'goto_page': "Nenda kwenye ukurasa",
        'page_simple': "Ukurasa {0}",
        'full_view_page': "Mwonekano kamili ukurasa {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Weka neno la kutafuta + Enter",
        'search_results': "Matokeo: {0} kati ya {1}",
        'search_nav_hint': "Enter: matokeo yajayo (Shift+Enter: matokeo yaliyotangulia)",
        'search_no_results': "Hakuna matokeo",
        'search_error': "Hitilafu ya utafutaji",
        'search_active': "Sehemu ya utafutaji imeamilishwa",
        'search_closed': "Utafutaji umefungwa",
        'search_position': "Ukurasa {0} {1}",
        'search_pos_top': "juu kabisa",
        'search_pos_upper': "juu",
        'search_pos_middle': "katikati",
        'search_pos_lower': "chini",
        'search_pos_bottom': "chini kabisa",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Utambuzi wa maandishi umekamilika kwa mafanikio!",
        'ocr_success_title': "OCR imefanikiwa",
        'ocr_success_message': "Hati sasa inaweza kutafutwa.",
        'ocr_failed': "OCR imeshindwa",
        'ocr_in_progress': "OCR inaendelea",
        'ocr_preparing': "PDF inaandaliwa...",
        'ocr_analyzing': "PDF inachambuliwa...",
        'ocr_optimizing': "Uboreshaji wa picha unaendelea...",
        'ocr_recognizing': "Utambuzi wa maandishi unaendelea...",
        'ocr_embedding': "Maandishi yanapachikwa...",
        'ocr_finalizing': "PDF inakamilishwa...",
        'ocr_not_available': "OCR haipatikani",
        'ocr_install_message': "Zana za OCR hazikupatikana.\n\nTafadhali sakinisha:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR inahitajika",
        'ocr_question': "PDF haina maandishi yanayotafutika.\nJe, unataka kufanya OCR ili kuwezesha {0}?",
        'ocr_perform': "Fanya OCR",
        'ocr_later': "Baadaye",
        'ocr_starting': "Inaanzisha OCR iliyohakikishiwa...",
        'ocr_success_voice': "OCR imefanikiwa. PDF sasa inatafutika.",
        'ocr_partial_success': "OCR ilifanywa, lakini kulikuwa na matatizo wakati wa kubadilisha.\n\nToleo linalotafutika limehifadhiwa katika:\n{0}\n\nHitilafu: {1}",
        'ocr_partial_title': "OCR imefanikiwa kwa sehemu",
        'ocr_partial_voice': "OCR ilifanywa, lakini uingizwaji ulishindwa.",
        'original_file': "Faili asili:",
        'old_size': "Ukubwa wa faili la zamani:    {0} baiti",
        'new_size': "Ukubwa wa faili mpya: {0} baiti",
        'size_change': "Mabadiliko: {0}{1} baiti",
        'backup_created_file': "Nakala ya usalama imeundwa:\n{0}",
        'backup_not_created': "Nakala ya usalama: Haikuundwa (mpangilio umezimwa)",
        'page_header': "=== Ukurasa {0} ===\n{1}\n",
        'scanned_page_header': "=== Ukurasa {0} (uliochanganuliwa) ===\n[Ukurasa huu una maandishi yaliyochanganuliwa tu]\n[Tafadhali fanya OCR kwa mikono]\n",
        'scanned_warning': "⚠️ MAANDISHI YALIYOCHANGANULIWA - OCR INAHITAJIKA",
        'guaranteed_title': "PDF inayotafutika imeundwa",
        'guaranteed_message': "<b>Toleo la uhakika linalotafutika limeundwa!</b>\n\nKwa sababu OCR ya kiotomatiki imeshindwa, PDF\nmbadala inayotafutika imeundwa:\n\n{0}\n\n<b>Faili hili lina:</b>\n• Maandishi yaliyotolewa (ikiwa yapo)\n• Vidokezo kwa kurasa zilizochanganuliwa\n• Inatafutika kikamilifu",
        'guaranteed_voice': "PDF ya uhakika inayotafutika imeundwa.",
        'instruction_title': "MAELEKEZO YA OCR",
        'instruction_file': "Faili asili: {0}",
        'instruction_text': "Utambuzi wa maandishi kiotomatiki (OCR) umeshindwa.\nTafadhali fanya OCR kwa mikono:\n\n1. KWA OCRmyPDF (mstari wa amri):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. KWA ADOBE ACROBAT (macOS/Windows):\n   • Fungua PDF katika Acrobat\n   • Tools > Edit PDF\n   • Chagua 'Text Recognition'\n\n3. KWA PREVIEW (macOS):\n   • Fungua PDF katika Preview\n   • File > Export...\n   • Quartz Filter: 'Reduce File Size'\n   • Amilisha 'Fanya OCR'\n\n4. HUDUMA ZA OCR MTANDAONI:\n   • smallpdf.com/de/ocr-pdf\n   • ilovepdf.com/de/ocr-pdf\n   • adobe.com/de/acrobat/online/pdf-to-word.html",
        'instruction_created': "Maagizo ya OCR yameundwa",
        'instruction_created_message': "Maagizo ya kina yameundwa:\n\n{0}\n\nTafadhali fuata hatua kwa OCR ya mkono.",
        'instruction_created_voice': "Maagizo ya OCR yameundwa.",
        'ocr_impossible': "OCR haiwezekani",
        'ocr_impossible_message': "OCR haikuweza kufanywa.\n\nTafadhali shughulikia '{0}' kwa mikono kwa programu ya OCR.",
        'ocr_impossible_voice': "OCR haiwezekani. Tafadhali shughulikia kwa mikono.",
        'emergency_title': "OCR ya Dharura",
        'emergency_message': "PDF ya dharura imeundwa:\n\n{0}\n\nTafadhali shughulikia faili hili kwa mikono kwa OCR.",
        'emergency_voice': "PDF ya dharura imeundwa. Tafadhali fanya OCR kwa mkono.",
        'critical_error': "Hitilafu Kubwa",
        'critical_error_message': "OCR haikuweza kuanza.\n\nTafadhali anzisha programu tena na\nangalia usakinishaji wa OCR.",
        'critical_error_voice': "Hitilafu kubwa ya OCR",
        'ocr_question_html': "<p>PDF haina maandishi yanayotafutika.<p>Je, unataka kufanya OCR ili kuwezesha <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR inahitajika. PDF haina maandishi yanayotafutika. Je, unataka kufanya OCR ili kuwezesha {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "hakuna PDF iliyopakiwa",
        'no_pdf_message': "Hakuna PDF iliyopakiwa",
        'pdf_not_found': "Faili la PDF halikupatikana",
        'file_size': "Ukubwa wa faili",
        'bytes': "Baiti",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Nakala ya usalama imeundwa",
        'backup_disabled': "Nakala ya usalama imezimwa",
        'backup_activated': "Uundaji wa nakala ya usalama umeamilishwa",
        'backup_deactivated': "Uundaji wa nakala ya usalama umezimwa",
        'backup_status': "Nakala ya usalama: {0}",
        'backup_on': "✔ imeamilishwa",
        'backup_off': "✘ imezimwa",
        'close_pdf': "Inafunga PDF: {0}",
        'pdf_not_found_format': "Faili la PDF halikupatikana: {0}",
        'error_pdf_load_format': "Hitilafu wakati wa kupakia PDF: {0}",
        'load_failed_format': "Upakuaji umeshindwa:\n{0}",
        'decrypted_suffix': "(ilifunguliwa)",
        'decryption_failed': "Ufunguaji umeshindwa.",
        'decryption_error': "Hitilafu wakati wa kufungua",
        'decryption_success': "Imefunguliwa kwa mafanikio",
        'decryption_success_message': "PDF imefunguliwa na kuhifadhiwa katika:\n\n{0}",
        'decryption_success_voice': "PDF imefunguliwa na kuhifadhiwa.",
        'password_remove_error': "Hitilafu wakati wa kuondoa nenosiri",
        'save_unencrypted': "Hifadhi PDF isiyosimbwa",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Hifadhi kama...",
        'save_copy': "Hifadhi nakala",
        'save_success': "PDF imehifadhiwa katika: {0}",
        'save_encrypted': "PDF iliyolindwa imehifadhiwa katika: {0}",
        'save_error': "PDF haikuweza kuhifadhiwa",
        'encryption_question': "Je, unataka kulinda PDF kwa nenosiri?",
        'encryption_yes': "Ndiyo",
        'encryption_no': "Hapana",
        'encryption_cancel': "Ghairi",
        'save_cancel': "Uhifadhi umeghairiwa",
        'save_encrypted_voice': "Faili limesimbwa na kuhifadhiwa.",
        'save_success_voice': "Faili la PDF limehifadhiwa bila usimbaji.",
        'save_error_format': "PDF haikuweza kuhifadhiwa:\n{0}",
        'export_pages_success': "Uhamishaji wa Pages umefanikiwa",
        'export_pages_error': "Uhamishaji wa Pages umeshindwa",
        'export_pages_error_format': "Uhamishaji wa Pages umeshindwa: {0}",
        'export_word_success': "Uhamishaji wa Word umefanikiwa",
        'export_word_error': "Uhamishaji wa Word umeshindwa",
        'export_word_error_format': "Uhamishaji wa Word umeshindwa: {0}",
        'export_text_success': "Uhamishaji wa maandishi umefanikiwa",
        'export_text_error': "Uhamishaji wa maandishi umeshindwa",
        'export_text_error_format': "Uhamishaji wa maandishi umeshindwa: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Nenosiri linahitajika",
        'password_enter': "Tafadhali ingiza nenosiri",
        'password_confirm': "Thibitisha nenosiri",
        'password_new': "Nenosiri jipya",
        'password_current': "Nenosiri la sasa",
        'password_save': "Hifadhi nenosiri (kwa usimbaji)",
        'password_saved': "✓ Nenosiri la faili hili limehifadhiwa",
        'password_wrong': "Nenosiri lisilo sahihi",
        'password_mismatch': "Nyosiri hazilingani",
        'password_too_short': "Nenosiri fupi sana",
        'password_min_length': "Nenosiri lazima liwe na angalau herufi 4",
        'password_strength': "Nguvu ya nenosiri",
        'password_strength_very_weak': "Dhaifu sana",
        'password_strength_weak': "Dhaifu",
        'password_strength_medium': "Wastani",
        'password_strength_strong': "Imara",
        'password_strength_very_strong': "Imara sana",
        'password_char_count': "(herufi {0})",
        'password_match': "✓ Zinalingana",
        'password_no_match': "✗ Nyosiri hazilingani",
        'password_show': "Onyesha",
        'password_hide': "Ficha",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Usimamizi wa nenosiri",
        'password_table_filename': "Jina la faili",
        'password_table_password': "Nenosiri",
        'password_count': "{0} nenosiri lililohifadhiwa",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Hakuna nyosiri zilizohifadhiwa",
        'password_copied': "{0} nenosiri limekopiwa",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Je, unataka kufuta nenosiri la '{0}'?",
        'password_delete_multiple': "Je, unataka kufuta nyosiri {0} zilizochaguliwa?",
        'password_delete_all_confirm': "Je, unataka kufuta nyosiri zote {0} zilizohifadhiwa?",
        'password_deleted': "{0} nenosiri limefutwa",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Nyosiri zote zimefutwa",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Kizalisha nenosiri",
        'generator_generated': "Nenosiri lililozalishwa:",
        'generator_regenerate': "Zalisha upya",
        'generator_copy': "Nakili",
        'generator_use': "Tumia",
        'generator_settings': "Mipangilio",
        'generator_length': "Urefu:",
        'generator_group_every': "Kitenganishi kila",
        'generator_group_chars': "herufi.    Kitenganishi:",
        'generator_uppercase': "Herufi kubwa (A-Z)",
        'generator_lowercase': "Herufi ndogo (a-z)",
        'generator_digits': "Nambari (0-9)",
        'generator_symbols': "Alama maalum (!@#$%^&*)",
        'generator_exclude': "Ondoa:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Nenosiri kuu linahitajika",
        'master_password_setup': "Weka nenosiri kuu",
        'master_password_change': "Badilisha nenosiri kuu",
        'master_password_enter': "Tafadhali ingiza nenosiri lako kuu",
        'master_password_choose': "Chagua nenosiri kuu salama (angalau herufi 8)",
        'master_password_new': "Tafadhali ingiza nenosiri lako kuu jipya",
        'master_password_confirm': "Thibitisha nenosiri",
        'master_password_authenticate': "Thibitisha",
        'master_password_success': "Nenosiri kuu limewekwa kwa mafanikio.",
        'master_password_changed': "Nenosiri kuu limebadilishwa kwa mafanikio.",
        'master_password_removed': "Nenosiri kuu na nyosiri zote zimefutwa.",
        'master_password_remove': "Ondoa nenosiri kuu",
        'master_password_remove_confirm': "Je, una UHAKIKA unataka kufuta NYOSIRI ZOTE?\n\nKitendo hiki HAKIWEZI KUTENGULIWA!",
        'master_password_export_before': "Je, unataka kuhamisha nakala ya usalama kabla?",
        'master_password_export_delete': "Hamisha na ufute",
        'master_password_delete_now': "Futa sasa",
        'master_password_for_signatures': "Ili kutumia sahihi, lazima uweke nenosiri kuu.\n\nJe, unataka kuweka nenosiri kuu sasa?",
        'master_password_for_private': "Ili kutumia vipande vya maandishi vya faragha, lazima uweke nenosiri kuu.\n\nJe, unataka kuweka nenosiri kuu sasa?",
        'master_password_info': """
            <b>🔐 BILA NENOSIRI KUU:</b><br>
            • Hauwezi kuona, kunakili na kuhamisha nyosiri<br>
            • Kufuta nyosiri kunawezekana kila wakati (hata bila nenosiri kuu)<br><br>

            <b>🔐 KWA NENOSIRI KUU:</b><br>
            • Kazi zote zinapatikana baada ya uthibitishaji<br>
            • Nyosiri zinasimbwa kwa nenosiri kuu<br>
            • Urefu wa chini: herufi 8<br>
            • Hifadhi salama ya SHA-256 Hash<br><br>

            <b>MUHIMU:</b><br>
            • Ukipoteza nenosiri kuu: Nyosiri haziwezi kurejeshwa<br>
            • Unapoondoa nenosiri kuu: NYOSIRI ZOTE zitafutwa<br>
            • Chaguo la kuhamisha linapatikana kabla ya kufuta<br>
            • Nenosiri kuu linaweza kubadilishwa wakati wowote
        """,
        'signature_auth_disabled': "Zima kuuliza nenosiri kwa sahihi",
        'template_auth_disabled': "Zima kuuliza nenosiri kwa vipande vya maandishi vya faragha",
        'master_password_for_signatures_settings': "Ili kutumia sahihi, lazima uweke nenosiri kuu.\n\nNenda kwenye Mipangilio - Usimamizi wa Nenosiri",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Linda PDF",
        'protect_info': "Faili '{0}' litalindwa kwa nenosiri.",
        'protect_instruction': "Tafadhali ingiza nenosiri unalotaka mara mbili ili kulinda hati, au tumia kizalisha nenosiri upande wa kulia wa sehemu ya kuingiza.",
        'protect_success': "PDF imelindwa kwa mafanikio na kuhifadhiwa katika:\n{0}\n\nNenosiri: {1}\n\nJe, unataka kufungua PDF iliyolindwa sasa?",
        'protect_open': "Ndiyo",
        'protect_skip': "Hapana",
        'protect_error': "Hitilafu wakati wa kulinda PDF",
        'protect_open_title': "fungua PDF iliyolindwa",
        'protect_question': "Imekamilika. Je, unataka kufungua PDF iliyolindwa sasa? Ndiyo au Hapana?",
        'password_cancel': "Kidirisha cha nenosiri kimeghairiwa",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Futa kurasa",
        'pages_extract': "Toa kurasa",
        'pages_insert': "Ingiza kurasa",
        'pages_move': "Sogeza kurasa",
        'pages_delete_options': "Chaguzi za kufuta",
        'pages_delete_empty': "Futa kurasa zote tupu",
        'pages_delete_current': "Futa ukurasa wa sasa",
        'pages_delete_range': "Futa safu ya kurasa",
        'pages_extract_options': "Chaguzi za kutoa",
        'pages_extract_current': "Toa ukurasa wa sasa",
        'pages_extract_range': "Toa safu ya kurasa",
        'pages_insert_position': "Nafasi ya kuingiza",
        'pages_insert_before': "Ingiza kabla ya ukurasa:",
        'pages_insert_select': "Chagua PDF",
        'pages_insert_none': "Hakuna PDF iliyochaguliwa",
        'pages_move_source': "Kurasa za kuhamisha",
        'pages_move_from': "Kutoka ukurasa:",
        'pages_move_to': "Hadi ukurasa:",
        'pages_move_target': "Nafasi lengwa",
        'pages_move_before': "Hamisha kabla ya ukurasa:",
        'pages_move_hint': "Kidokezo: ukurasa 1 = mwanzo, {0} = mwisho",
        'pages_range_invalid': "Ukurasa wa mwanzo lazima uwe mdogo au sawa na ukurasa wa mwisho.",
        'pages_position_invalid': "Nafasi lengwa haiwezi kuwa ndani ya safu inayohamishwa.",
        'pages_no_pdf_selected': "Hakuna PDF iliyochaguliwa.",
        'pages_deleted': "Kurasa {0} zimefutwa.",
        'pages_extracted': "Zimetolewa: {0}\nZimehifadhiwa katika: {1}\nUkubwa wa faili: {2:.1f} KB",
        'pages_inserted': "Kurasa {0} zimeingizwa",
        'pages_moved': "Kurasa {0} zimehamishwa.",
        'pages_deleted_none': "Hakuna kurasa zilizofutwa.",
        'pages_delete_progress': "Kufuta kurasa...",
        'pages_deleted_with_backup': "Kurasa {0} zimefutwa.\n\nNakala ya usalama: {1}",
        'pages_deleted_voice': "Nakala ya usalama imeundwa na kurasa {0} zimefutwa.",
        'info': "Kidokezo",
        'error_dialog_creation': "Kidirisha hakiwezi kuundwa",
        'extract_page_single': "Toa ukurasa {0}",
        'extract_page_range': "Toa kurasa {0}-{1}",
        'extract_success_voice': "Kurasa zimetolewa kwa mafanikio",
        'extract_error_format': "Hitilafu wakati wa kutoa: {0}",
        'pages_inserted_voice': "Kurasa {0} zimeingizwa.",
        'insert_error_format': "Hitilafu wakati wa kuingiza: {0}",
        'pages_move_progress': "Kuhama kurasa...",
        'pages_moved_with_backup': "Kurasa {0} zimehamishwa.\n\nNakala ya usalama: {1}",
        'move_success_title': "Imehamishwa kwa mafanikio",
        'pages_moved_voice': "Kurasa {0} zimehamishwa kwa mafanikio",
        'mark_removed': "Alama imeondolewa kutoka ukurasa {0}",
        'mark_empty': "Ukurasa {0} umewekwa alama kuwa tupu",
        'mark_export_removed': "Alama ya kuhamisha imeondolewa kutoka ukurasa {0}",
        'mark_export': "Ukurasa {0} umewekwa alama kwa kuhamisha",
        'no_empty_pages': "Hakuna kurasa tupu zilizowekwa alama za kufuta",
        'delete_empty_confirm': "Je, unataka kufuta kurasa zote {0} tupu zilizowekwa alama?",
        'delete_empty_confirm_voice': "Je, nifute sasa kurasa zote {0} tupu zilizowekwa alama? Ndiyo au Hapana.",
        'empty_pages_deleted': "Kurasa {0} tupu zimefutwa",
        'no_export_pages': "Hakuna kurasa zilizowekwa alama za kuhamisha",
        'overwrite_title': "Andika juu ya faili lililopo",
        'overwrite_question': "Faili\n\n{0}\n\nlinashawahi kuwepo.\nJe, unataka kuandika juu yake?",
        'overwrite_voice': "Je, niandike juu ya faili lililopo? Ndiyo au Hapana.",
        'page_skipped': "Ukurasa {0} umeachwa",
        'export_complete': "Uhamishaji umekamilika.",
        'export_complete_voice': "Uhamishaji umekamilika.",
        'no_pages_exported': "Hakuna ukurasa uliohamishwa",
        'export_cancelled': "Uhamishaji umeghairiwa",
        'pages_exported': "Kurasa {0} zimehamishwa kwa {1}",
        'export_page_title': "Hamisha ukurasa",
        'page_exported': "Ukurasa {0} umehamishwa kwa {1}",
        'export_error': "Hitilafu wakati wa kuhamisha",
        'export_marked_title': "Hamisha kurasa zilizowekwa alama",
        'rotate_all_title': "zungusha kurasa zote",
        'rotate_all_question': "Je, unataka kuzungusha kurasa zote kwa digrii 90 kulia?",
        'rotate_all_voice': "Je, unataka kuzungusha kurasa zote kwa digrii 90 kulia? Ndiyo au Hapana?",
        'all_pages_rotated': "Kurasa zote zimezungushwa",
        'page_rotated': "Ukurasa {0} umezungushwa",
        'rotate_error': "Ukurasa haukuweza kuzungushwa",
        'delete_page_confirm': "Je, unataka kufuta ukurasa {0}?",
        'delete_page_confirm_voice': "Je, unataka kufuta ukurasa {0}? Ndiyo au Hapana.",
        'page_deleted': "Ukurasa {0} umefutwa",
        'delete_error': "Ukurasa haukuweza kufutwa",
        'pages_deleted_voice': "Kurasa {0} zimefutwa",
        'pages_exported_split': "Kurasa {0} zimehamishwa kwa mafanikio.",
        'pages_skipped': "Kurasa {0} zimeachwa.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Toa kurasa (hali ya juu)",
        'pdf_splitter_title': "Kigawanya na Kitoa PDF",
        'pdf_splitter_load': " Chagua faili la PDF",
        'pdf_splitter_info': "Tafadhali chagua chaguo kwa hati yako ya PDF",
        'pdf_splitter_basic': "Operesheni za msingi",
        'pdf_splitter_single': "Gawanya katika kurasa moja moja",
        'pdf_splitter_range': "Toa kurasa:",
        'pdf_splitter_range_placeholder': "mfano 1-3,5,7-9",
        'pdf_splitter_clean': "Operesheni za kusafisha",
        'pdf_splitter_remove_empty': "Ondoa kurasa zote tupu",
        'pdf_splitter_remove': "Futa safu ya kurasa:",
        'pdf_splitter_remove_placeholder': "mfano 2,4-6",
        'pdf_splitter_process': "Shughulikia PDF",
        'pdf_splitter_loaded': "PDF imepakiwa. Tafadhali chagua chaguo",
        'pdf_read_error': "PDF haikusomeka",
        'pages': "Kurasa",
        'pages_created': "Kurasa zimeundwa",
        'range_empty': "Tafadhali ingiza safu ya kurasa",
        'range_invalid': "Safu ya kurasa batili",
        'range_created': "PDF mpya iliyo na kurasa zilizochaguliwa imeundwa:\n{0}",
        'empty_removed': "Kurasa {0} tupu zimeondolewa.\nPato: {1}",
        'remove_empty': "Tafadhali ingiza kurasa za kuondoa",
        'remove_invalid': "Kurasa batili za kuondoa",
        'remove_done': "PDF iliyosafishwa imeundwa:\n{0}",
        'open_folder': "Fungua folda",
        'show_in_finder': "Onyesha kwenye Finder",
        'pdf_splitter_no_pdf': "Tafadhali pakia faili la PDF kwanza.",
        'process_error': "Hitilafu wakati wa kushughulikia PDF",
        'pages_created_voice': "Kurasa {0} zimeundwa",
        'range_created_voice': "PDF iliyo na kurasa zilizochaguliwa imeundwa",
        'empty_removed_voice': "Kurasa {0} tupu zimeondolewa",
        'remove_done_voice': "PDF iliyosafishwa imeundwa",
        'pdf_splitter_split_groups': "Kila kikundi kinachofuatana katika faili tofauti",
        'range_created_single': "PDF mpya imeundwa:\n{0}",
        'range_created_multiple': "Faili {0} za PDF zimeundwa.",
        'range_created_voice_single': "PDF moja iliyo na kurasa zilizochaguliwa imeundwa",
        'range_created_voice_multiple': "Faili {0} za PDF zimeundwa",
        'empty_removed_none_left': "Hakuna kurasa zilizosalia",
        'empty_removed_all_empty': "Kurasa zote zilitambuliwa kuwa tupu na zingeondolewa. Hakuna faili lililoundwa.",
        'preview_single': "Onesho la awali: {0}",
        'preview_enter_range': "Tafadhali ingiza safu ya kurasa.",
        'preview_invalid_range': "Safu ya kurasa batili.",
        'preview_file': "Onesho la awali: {0}",
        'preview_files': "Onesho la awali: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Inaanza mchakato wa uchapishaji",
        'print_sent': "Kazi ya uchapishaji imetumwa",
        'print_now': "Chapisha sasa",
        'print_error': "Hitilafu katika uchapishaji wa haraka",
        'print_limited': "Kazi ya uchapishaji kwenye mfumo huu ni mdogo",
        'print_error_format': "Hitilafu katika uchapishaji wa haraka: {0}",
        'warning': "Kidokezo",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Badilisha hadi Mwezi Mwanga",
        'mode_switch_to_dark': "Badilisha hadi Mwezi Giza",
        'mode_dark_activated': "Mwezi Giza umeamilishwa",
        'mode_light_activated': "Mwezi Mwanga umeamilishwa",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Mwonekano kamili",
        'zoom_two_pages': "Kurasa mbili kando",
        'zoom_overview': "Hali ya muhtasari",
        'zoom_cannot_during_search': "Kukuza haiwezekani wakati wa utafutaji",
        'zoom_exit_first': "Tafadhali toka kwenye kukuza kwanza",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Buruta na Acha imeamilishwa",
        'drag_disabled': "Buruta na Acha imezimwa",
        'drag_page_grab': "Shika ukurasa {0}",
        'drag_page_dropped': "Ukurasa {0} umeingizwa kwenye nafasi {1}",
        'drag_position_invalid': "Nafasi batili",
        'drag_same_position': "Ukurasa {0} unabaki kwenye nafasi {0}",
        'drag_error': "Hitilafu wakati wa kusogeza",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Ingiza maandishi kwa uumbizaji wa hali ya juu na usimamizi wa vipande vya maandishi",
        'text_templates': "Vipande vya maandishi vinavyopatikana:",
        'text_name': "Jina",
        'text_preview': "Onesho la awali la maandishi",
        'text_enter': "Maandishi:",
        'text_font_size': "Ukubwa wa fonti:",
        'text_formatting': "Uumbizaji:",
        'text_bold': "Nzito",
        'text_italic': "Mteremko",
        'text_underline': "Mstari chini",
        'text_alignment': "Mpangilio:",
        'text_left': "Kushoto",
        'text_center': "Katikati",
        'text_right': "Kulia",
        'text_color': "Rangi ya maandishi:",
        'text_opacity': "Uwazi:",
        'text_word_wrap': "Mvunjaji wa mstari:",
        'text_auto': "Kiotomatiki",
        'text_page_width_95': "Upana wa ukurasa (95%)",
        'text_page_width_85': "Pana sana (85%)",
        'text_page_width_75': "Pana (75%)",
        'text_page_width_60': "Pana (60%)",
        'text_page_width_50': "Wastani (50%)",
        'text_page_width_30': "Nyembamba (30%)",
        'text_page_width_20': "nyembamba (20%)",
        'text_page_width_10': "Nyembamba sana (10%)",
        'text_no_wrap': "Hakuna mvunjaji",
        'text_private': "Kipande cha maandishi cha faragha (kinahitaji uthibitishaji)",
        'text_preview_label': "Onesho la awali:",
        'text_preview_placeholder': "Onesho la awali la maandishi litaonyeshwa hapa...",
        'text_no_text': "(Hakuna maandishi)",
        'text_save_template': "💾 Hifadhi kama kipande",
        'text_delete_template': "🗑 Futa kipande cha maandishi kilichochaguliwa",
        'text_show_private': "Onyesha faragha",
        'text_hide_private': "Ficha faragha",
        'text_use': "✅ Tumia maandishi",
        'text_saved': "Kipande cha maandishi kimehifadhiwa kama:\n{0}",
        'text_saved_voice': "Kipande cha maandishi kimehifadhiwa",
        'text_deleted': "Kipande cha maandishi kimefutwa",
        'text_no_text_to_save': "Hakuna maandishi ya kuhifadhi.",
        'text_no_templates': "Hakuna vipande vya maandishi vilivyopatikana",
        'text_private_master_required': "Vipande vya faragha vinaweza kutumika tu ikiwa nenosiri kuu limewekwa.\n\nJe, unataka kuweka nenosiri kuu sasa?",
        'text_filename': "Jina la faili la kipande cha maandishi (bila 'Text_' na '.txt'):",
        'text_filename_hint': "Mfano: 'Telefon HomeOffice' itahifadhiwa kama 'Text_Telefon HomeOffice.txt'",
        'text_save_hint': "Kipande cha maandishi kitahifadhiwa kiotomatiki kwa uumbizaji.",
        'text_guide_title': "Ingiza maandishi - Mwongozo",
        'text_delete_confirm': "Je, unataka kufuta kipande cha maandishi?\n\nFaili: {0}\nMaandishi: {1}...",
        'text_make_public': "Weka alama kama ya umma",
        'text_make_private': "Weka alama kama ya faragha",
        'text_privacy_changed': "Hali ya faragha imebadilishwa",
        'text_private_always': "Faragha inaonekana kila wakati (mpangilio)",
        'text_mode_required': "Tafadhali amilisha hali ya maandishi kwanza",
        'text_continue_editing': "Endelea kuhariri - Kielekezi mwishoni mwa maandishi",
        'text_no_input': "Hakuna maandishi yaliyoingizwa - maandishi yametupiliwa mbali",
        'save_dialog_question': "Je, unaendeleaje?",
        'text_save_question': "Hifadhi maandishi na misalaba yote, rekebisha, endelea kuhariri au tupilia mbali?",
        'copy_cross': "Msalaba umenakiliwa",
        'paste_cross': "Msalaba umebandikwa",
        'paste_text': "Maandishi yamebandikwa",
        'cross_discarded': "Msalaba umetupiliwa mbali",
        'all_discarded': "Yote yametupiliwa mbali",
        'text_discarded': "Maandishi yametupiliwa mbali",
        'no_texts_to_save': "Hakuna maandishi ya kuhifadhi",
        'no_valid_texts': "Hakuna maandishi halali ya kuhifadhi",
        'text_word_singular': "Maandishi",
        'text_word_plural': "Maandishi",
        'cross_word_singular': "Msalaba",
        'cross_word_plural': "Misalaba",
        'texts_saved_title': "Maandishi yamehifadhiwa",
        'texts_crosses_saved': "{0} {1} na {2} {3} yameingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'texts_crosses_saved_voice': "{0} {1} na {2} {3} zimehifadhiwa.",
        'texts_saved': "{0} {1} yameingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'texts_saved_voice': "{0} {1} zimehifadhiwa.",
        'crosses_saved': "{0} {1} yameingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'crosses_saved_voice': "{0} {1} zimehifadhiwa.",
        'elements_saved': "Vipengee {0} vimeingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'elements_saved_voice': "Vipengee {0} vimehifadhiwa.",
        'text_window_load_error': "Dirisha la maandishi halikuweza kupakiwa",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Kuingiza Maandishi na Vipande vya Maandishi – Mwongozo wa Kina**

        **1. Kuingiza na kuhariri maandishi**
        - Bonyeza kitufe cha kulia mahali unapotaka kwenye hati na uchague "Ingiza maandishi".
        - Dirisha litafunguka ambapo unaweza kuingiza na kuumbiza maandishi yako:
        • Ukubwa wa fonti, nzito, mteremko, mstari chini
        • Rangi ya maandishi (inayochaguliwa kwa uhuru)
        • Uwazi kwa kitelezi
        • Mvunjaji wa mstari (upana tofauti, kama upana wa ukurasa, nyembamba, hakuna mvunjaji)
        - Baada ya kuthibitisha, maandishi yataonekana mahali ulipobofya. Unaweza kuyasogeza kwa panya au vitufe vya mishale.
        - Kubofya mara mbili kwenye maandishi kunafungua hali ya kuhariri; ESC inakuondoa.

        **2. Kusimamia vipande vya maandishi (Templeti)**
        - Katika dirisha la maandishi utaona orodha ya vipande vyote vya maandishi vilivyohifadhiwa upande wa kushoto.
        - **Kuhifadhi kipande:** Ingiza maandishi yako, uumbize na ubofye "💾 Hifadhi kama kipande". Ingiza jina la faili (bila kiendelezi).
        - **Kupakia kipande:** Bofya jina unalotaka kwenye orodha. Maandishi na uumbizaji utachukuliwa na unaweza kurekebishwa ikiwa inahitajika.
        - **Kufuta:** Kwa kubofya kitufe cha kulia kwenye kipande unaweza kukifuta au kubadilisha hali yake ya faragha.

        **3. Vipande vya maandishi vya faragha (Nenosiri Kuu)**
        - Ikiwa umeweka nenosiri kuu (chini ya Mipangilio → Usimamizi wa nenosiri), unaweza kuweka alama kwenye vipande kama "faragha".
        - Amilisha kisanduku cha uteuzi "Kipande cha maandishi cha faragha" kwenye dirisha kabla ya kuhifadhi.
        - Vipande vya faragha vitaonekana kwenye orodha tu ikiwa utaingiza nenosiri lako kuu mara moja kwa kila kipindi (uthibitishaji kupitia ikoni ya kufuli au wakati wa upatikanaji wa kwanza).
        - Kwa njia hii unaweza kulinda vipande vya maandishi ya siri dhidi ya ufikiaji usioidhinishwa.

        **4. Kuingiza msalaba**
        - Kupitia menyu ya muktadha unaweza pia kuingiza msalaba wa picha (kwa mfano kwa visanduku vya kuteua).
        - Ukubwa, unene wa mstari na rangi ya misalaba unaweza kurekebisha kimataifa kwenye mipangilio (Menyu "Mipangilio" → "Mipangilio ya Alama za Kuteua").
        - Kwa kubofya kitufe cha kulia kwenye msalaba uliopo unaweza kuubadilisha kibinafsi.

        **5. Vitendo vya pamoja**
        - Ikiwa umeweka maandishi au misalaba mingi kwenye ukurasa mmoja, unaweza kupitia menyu ya muktadha (bonyeza kulia katika hali ya maandishi) kuhifadhi au kutupilia mbali vipengee vyote pamoja.
        - Wakati wa kuhifadhi, vipengee vyote hupachikwa kwenye PDF na kubaki kama michoro ya vekta.

        **6. Njia za mkato za kibodi katika hali ya maandishi**
        - Vitufe vya mishale: Sogeza kipengee
        - Ctrl+vitufe vya mishale: Hatua kubwa zaidi
        - Enter: Fungua dirisha la kuhifadhi (hifadhi zote / rekebisha / tupilia mbali)
        - ESC: Tupilia mbali kipengee cha sasa
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Kuingiza Maandishi na Vipande vya Maandishi – Mwongozo wa Kina</strong></p>

        <p><strong>1. Kuingiza na kuhariri maandishi</strong></p>
        <ul>
        <li>Bonyeza kitufe cha kulia mahali unapotaka kwenye hati na uchague "Ingiza maandishi".</li>
        <li>Dirisha litafunguka ambapo unaweza kuingiza na kuumbiza maandishi yako:<br/>
        • Ukubwa wa fonti, nzito, mteremko, mstari chini<br/>
        • Rangi ya maandishi (inayochaguliwa kwa uhuru)<br/>
        • Uwazi kwa kitelezi<br/>
        • Mvunjaji wa mstari (upana tofauti, kama upana wa ukurasa, nyembamba, hakuna mvunjaji)</li>
        <li>Baada ya kuthibitisha, maandishi yataonekana mahali ulipobofya. Unaweza kuyasogeza kwa panya au vitufe vya mishale.</li>
        <li>Kubofya mara mbili kwenye maandishi kunafungua hali ya kuhariri; ESC inakuondoa.</li>
        </ul>

        <p><strong>2. Kusimamia vipande vya maandishi (Templeti)</strong></p>
        <ul>
        <li>Katika dirisha la maandishi utaona orodha ya vipande vyote vya maandishi vilivyohifadhiwa upande wa kushoto.</li>
        <li><strong>Kuhifadhi kipande:</strong> Ingiza maandishi yako, uumbize na ubofye "💾 Hifadhi kama kipande". Ingiza jina la faili (bila kiendelezi).</li>
        <li><strong>Kupakia kipande:</strong> Bofya jina unalotaka kwenye orodha. Maandishi na uumbizaji utachukuliwa na unaweza kurekebishwa ikiwa inahitajika.</li>
        <li><strong>Kufuta:</strong> Kwa kubofya kitufe cha kulia kwenye kipande unaweza kukifuta au kubadilisha hali yake ya faragha.</li>
        </ul>

        <p><strong>3. Vipande vya maandishi vya faragha (Nenosiri Kuu)</strong></p>
        <ul>
        <li>Ikiwa umeweka nenosiri kuu (chini ya Mipangilio → Usimamizi wa nenosiri), unaweza kuweka alama kwenye vipande kama "faragha".</li>
        <li>Amilisha kisanduku cha uteuzi "Kipande cha maandishi cha faragha" kwenye dirisha kabla ya kuhifadhi.</li>
        <li>Vipande vya faragha vitaonekana kwenye orodha tu ikiwa utaingiza nenosiri lako kuu mara moja kwa kila kipindi (uthibitishaji kupitia ikoni ya kufuli au wakati wa upatikanaji wa kwanza).</li>
        <li>Kwa njia hii unaweza kulinda vipande vya maandishi ya siri dhidi ya ufikiaji usioidhinishwa.</li>
        </ul>

        <p><strong>4. Kuingiza msalaba</strong></p>
        <ul>
        <li>Kupitia menyu ya muktadha unaweza pia kuingiza msalaba wa picha (kwa mfano kwa visanduku vya kuteua).</li>
        <li>Ukubwa, unene wa mstari na rangi ya misalaba unaweza kurekebisha kimataifa kwenye mipangilio (Menyu "Mipangilio" → "Mipangilio ya Alama za Kuteua").</li>
        <li>Kwa kubofya kitufe cha kulia kwenye msalaba uliopo unaweza kuubadilisha kibinafsi.</li>
        </ul>

        <p><strong>5. Vitendo vya pamoja</strong></p>
        <ul>
        <li>Ikiwa umeweka maandishi au misalaba mingi kwenye ukurasa mmoja, unaweza kupitia menyu ya muktadha (bonyeza kulia katika hali ya maandishi) kuhifadhi au kutupilia mbali vipengee vyote pamoja.</li>
        <li>Wakati wa kuhifadhi, vipengee vyote hupachikwa kwenye PDF na kubaki kama michoro ya vekta.</li>
        </ul>

        <p><strong>6. Njia za mkato za kibodi katika hali ya maandishi</strong></p>
        <ul>
        <li>Vitufe vya mishale: Sogeza kipengee</li>
        <li>Ctrl+vitufe vya mishale: Hatua kubwa zaidi</li>
        <li>Enter: Fungua dirisha la kuhifadhi (hifadhi zote / rekebisha / tupilia mbali)</li>
        <li>ESC: Tupilia mbali kipengee cha sasa</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Mipangilio ya Alama za Kuteua",
        'cross_properties': "Sifa za Msalaba",
        'cross_size': "Ukubwa (px):",
        'cross_line_width': "Unene wa mstari:",
        'cross_color': "Rangi:",
        'cross_choose_color': "Chagua",
        'cross_fine_tuning': "Urekebishaji mwembamba wakati wa kuhifadhi (pikseli)",
        'cross_offset_x': "Mkondo wa X:",
        'cross_offset_y': "Mkondo wa Y:",
        'cross_offset_x_tooltip': "Thamani hasi husogeza msalaba kushoto wakati wa kuhifadhi, chanya kulia",
        'cross_offset_y_tooltip': "Thamani hasi husogeza msalaba juu wakati wa kuhifadhi, chanya chini",
        'cross_preview': "Onesho la awali",
        'cross_save': "Tekeleza mipangilio",
        'cross_customized': "Msalaba umerekebishwa",
        'cross_settings_applied': "Mipangilio ya misalaba imehifadhiwa.\nUkubwa: {0}px, Unene wa mstari: {1}px\n{2}",
        'cross_updated_count': "Misalaba {0} iliyopo imesasishwa.",
        'cross_no_crosses': "Hakuna misalaba iliyopo iliyopatikana.",
        'cross_settings_applied_all': "Mipangilio ya misalaba imetekelezwa kwa misalaba yote {0}",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Mipangilio ya Sahihi",
        'signature_1': "Sahihi 1",
        'signature_2': "Sahihi 2",
        'signature_select': "Chagua sahihi",
        'signature_add': "➕ Ongeza sahihi mpya...",
        'signature_size': "Ukubwa wa sahihi {0} (%):",
        'signature_common': "Mipangilio ya jumla",
        'signature_timestamp': "Ongeza muhuri wa muda kiotomatiki",
        'signature_location': "Eneo la kawaida:",
        'signature_timestamp_size': "Ukubwa wa fonti ya muhuri wa muda:",
        'signature_no_files': "-- Hakuna sahihi zilizopatikana --",
        'signature_insert': "Ingiza sahihi",
        'signature_insert_1': "Ingiza sahihi 1",
        'signature_insert_2': "Ingiza sahihi 2",
        'signature_customize': " Rekebisha sahihi",
        'signature_discard': " Tupilia mbali sahihi hii",
        'signature_save_all': " Hifadhi sahihi zote",
        'signature_discard_all': " Tupilia mbali sahihi zote",
        'signature_guide_title': "Sahihi - Mwongozo",
        'signature_guide': """
📝 Sahihi - Mwongozo mfupi

- Weka nenosiri kuu
- Sanidi sahihi kwenye menyu ya Mipangilio
  (ukubwa, muhuri wa muda ...)
- Ingiza kwa BONYEZA KULIA mahali unapotaka
  (nenosiri kuu linahitajika mara moja kwa kila kipindi)
- Sogeza sahihi kwa panya au vitufe vya mishale
- Sahihi nyingi zinaweza kuingizwa moja baada ya nyingine
- Kila sahihi inaweza kurekebishwa kibinafsi
- Tupilia mbali sahihi moja
- Hifadhi / tupilia mbali sahihi zote kwa wakati mmoja
- Vinginevyo, unaweza pia kutumia upau wa menyu.
        """,
        'signature_placeholder': "Hakuna onesho la awali linalopatikana",
        'signature_info': "Sahihi {0}: {1}×{2} px ({3}% ya {4}×{5})",
        'signature_info_placeholder': "Mipangilio ya sahihi {0}",
        'signature_inserted': "Sahihi {0} imeingizwa kwenye ukurasa {1}",
        'signature_deleted': "Sahihi imefutwa",
        'signature_copied': "Sahihi imenakiliwa",
        'signature_pasted': "Sahihi {0} imeingizwa",
        'signature_saved': "Sahihi {0} zimeingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'signature_saved_voice': "Sahihi {0} zimehifadhiwa",
        'mode_replace_signature_format': "Maliza hali na ingiza sahihi {0}",
        'mode_conflict_voice_signature': "Hali ya {0} imeamilishwa. Maliza na ingiza sahihi?",
        'signature_not_configured': "Sahihi {0} haijasanidiwa",
        'signature_file_not_found': "Faili la sahihi halikupatikana",
        'timestamp_format': "{0}, tarehe {1}",
        'no_copied_signature': "Hakuna sahihi iliyonakiliwa",
        'no_signatures_to_save': "Hakuna sahihi za kuhifadhi",
        'signature_save_question': "Hifadhi sahihi zote, rekebisha au tupilia mbali hii?",
        'signatures_saved_title': "Sahihi zimehifadhiwa",
        'signatures_saved': "Sahihi {0} zimeingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'signatures_saved_voice': "Sahihi {0} zimehifadhiwa.",
        'all_signatures_discarded': "Sahihi zote zimetupiliwa mbali",
        'signature_settings_saved': "Mipangilio ya sahihi imehifadhiwa",
        'signature_cancelled': "Sahihi imetupiliwa mbali",
        'signature_active_title': "Sahihi imeamilishwa",
        'signature_replace_question': "Tayari kuna sahihi imeamilishwa.\n\nJe, unataka kubadilisha sahihi ya sasa?",
        'signature_replace': "Badilisha sahihi",
        'signature_replace_voice': "Badilisha sahihi ya sasa au ghairi?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Mipangilio ya Picha",
        'image_common': "Mipangilio ya jumla ya picha",
        'image_keep_aspect': "Dumisha uwiano wa vipimo unapoburuta",
        'image_default_size': "Ukubwa wa kawaida (%):",
        'image_dark_invert': "Geuza picha katika Mwezi Giza",
        'image_dark_invert_tooltip': "Imeamilishwa: Picha zitageuzwa kwa mwonekano bora",
        'image_fine_tuning': "Urekebishaji mwembamba (pikseli)",
        'image_offset_x': "Mkondo wa X:",
        'image_offset_y': "Mkondo wa Y:",
        'image_offset_x_tooltip': "Thamani hasi husogeza picha kushoto wakati wa kuhifadhi, chanya kulia",
        'image_offset_y_tooltip': "Thamani hasi husogeza picha juu wakati wa kuhifadhi, chanya chini",
        'image_select': "Chagua picha",
        'image_insert': "Ingiza picha",
        'image_customize': " Rekebisha picha",
        'image_aspect': " Dumisha uwiano wa vipimo",
        'image_discard': " Tupilia mbali picha hii",
        'image_save_all': " Hifadhi picha zote",
        'image_discard_all': " Tupilia mbali picha zote",
        'image_filter': "Picha",
        'image_guide_title': "Ingiza picha - Mwongozo",
        'image_guide': """
📷 Ingiza picha kwenye PDF - Mwongozo mfupi:

1. Bonyeza kulia mahali unapotaka
2. "Ingiza picha" → Chagua picha
3. Weka picha: Buruta kwa panya
4. Rekebisha ukubwa: Buruta kwenye pembe/kando
5. Dumisha uwiano wa vipimo: Kitufe [A]
6. Marekebisho zaidi: Bonyeza kulia kwenye picha

Kidokezo: Kwenye menyu ya muktadha unaweza kurekebisha mipangilio.
        """,
        'image_inserted': "Picha {0} imeingizwa kwenye ukurasa {1}",
        'image_deleted': "Picha imetupiliwa mbali",
        'image_copied': "Picha imenakiliwa",
        'image_pasted': "Picha imeingizwa",
        'image_saved': "Picha {0} zimeingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'image_saved_voice': "Picha {0} zimehifadhiwa",
        'image_aspect_on': "imeamilishwa",
        'image_aspect_off': "imezimwa",
        'image_aspect_toggle': "Dumisha uwiano wa vipimo {0}",
        'image_reset': "Picha imerejeshwa kwa ukubwa asili",
        'image_replaced': "Picha imebadilishwa",
        'image_invalid': "Hakuna picha halali",
        'mode_replace_image': "Ingiza picha",
        'mode_conflict_voice_image': "Hali ya {0} imeamilishwa. Maliza na ingiza picha?",
        'image_active_title': "Picha imeamilishwa",
        'image_replace_question': "Tayari kuna picha imeamilishwa.\n\nJe, unataka kubadilisha picha ya sasa?",
        'image_replace': "Badilisha picha",
        'image_replace_voice': "Badilisha picha ya sasa au ghairi?",
        'image_filter_all': "Picha (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Faili zote (*.*)",
        'no_copied_image': "Hakuna picha iliyonakiliwa",
        'image_discarded': "Picha imetupiliwa mbali",
        'image_save_question': "Hifadhi picha zote, rekebisha au tupilia mbali hii?",
        'no_images_to_save': "Hakuna picha za kuhifadhi",
        'no_valid_images': "Hakuna picha halali za kuhifadhi",
        'images_saved_title': "Picha zimehifadhiwa",
        'images_saved': "Picha {0} zimeingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'images_saved_voice': "Picha {0} zimehifadhiwa.",
        'all_images_discarded': "Picha zote zimetupiliwa mbali",
        'image_settings_updated': "Mipangilio ya picha imesasishwa",
        'image_replace_title': "Chagua picha mpya",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Mipangilio ya Maumbo",
        'form_basic': "Mipangilio ya msingi",
        'form_default_type': "Aina chaguo-msingi ya umbo:",
        'form_rectangle': "Mstatili",
        'form_ellipse': "Duwara",
        'form_line': "Mstari",
        'form_arrow': "Mshale",
        'form_line_width': "Unene wa mstari:",
        'form_colors': "Rangi",
        'form_line_color': "Rangi ya mstari:",
        'form_fill_color': "Rangi ya kujaza:",
        'form_choose_color': "Chagua",
        'form_transparent': "Asili ya uwazi (mstari tu)",
        'form_filled': "imejazwa",
        'form_dark_mode': "Mwezi Giza",
        'form_dark_invert': "Geuza rangi katika Mwezi Giza",
        'form_fine_tuning': "Urekebishaji mwembamba (pikseli)",
        'form_offset_x': "Mkondo wa X:",
        'form_offset_y': "Mkondo wa Y:",
        'form_offset_x_tooltip': "Thamani hasi husogeza umbo kushoto wakati wa kuhifadhi, chanya kulia",
        'form_offset_y_tooltip': "Thamani hasi husogeza umbo juu wakati wa kuhifadhi, chanya chini",
        'form_preview': "Onesho la awali",
        'form_insert': "Ingiza umbo",
        'form_rectangle_insert': "Mstatili",
        'form_ellipse_insert': "Duwara/Mduara",
        'form_line_insert': "Mstari (mibofyo 2)",
        'form_arrow_insert': "Mshale (mibofyo 2)",
        'form_customize': " Rekebisha umbo",
        'form_transparent_toggle': " Asili ya uwazi",
        'form_discard': " Tupilia mbali umbo hili",
        'form_save_all': " Hifadhi maumbo yote",
        'form_discard_all': " Tupilia mbali maumbo yote",
        'form_guide_title': "Ingiza maumbo - Mwongozo",
        'form_guide': """
📐 Ingiza maumbo kwenye PDF - Mwongozo mfupi:

1. Chagua aina ya umbo (Mstatili, Duwara, Mstari, Mshale)
2. Bofya kwenye nafasi
   - Kwa Mstatili/Duwara: Bofya moja linaweka umbo
   - Kwa Mstari/Mshale: Mibofyo miwili kwa alama ya mwanzo na mwisho
3. Weka umbo: Buruta kwa panya
4. Rekebisha ukubwa: Buruta kwenye pembe/kando
5. Hifadhi umbo: Enter
6. Tupilia mbali umbo: ESC
7. Marekebisho zaidi: Bonyeza kulia kwenye umbo

Kidokezo: Kwenye menyu ya muktadha unaweza kurekebisha mipangilio.
        """,
        'form_inserted': "{0} imeingizwa kwenye ukurasa {1}",
        'form_deleted': "Umbo limefutwa",
        'form_copied': "Umbo limenakiliwa",
        'form_pasted': "Umbo limeingizwa",
        'form_saved': "Maumbo {0} yameingizwa kwenye PDF.\n\nPDF inapakiwa upya...",
        'form_saved_voice': "Maumbo {0} yamehifadhiwa",
        'form_reset': "Umbo limerejeshwa kwa ukubwa wa kawaida",
        'form_transparent_on': "imeamilishwa",
        'form_transparent_off': "imezimwa",
        'form_transparent_toggled': "Asili ya uwazi {0}",
        'form_line_cancel': "Kuchora mstari kumeghairiwa",
        'form_second_click': "Sasa bofya alama ya mwisho ya {0}",
        'mode_replace_form': "Ingiza umbo",
        'mode_conflict_voice_form': "Hali ya {0} imeamilishwa. Maliza na ingiza umbo?",
        'form_settings_updated': "Mipangilio ya maumbo imesasishwa",
        'form_unknown': "Umbo",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Bofya kwenye nafasi ya kuanzia",
        'form_line_guide_2': "2. Bofya kwenye nafasi ya mwisho",
        'form_line_guide_3': "Mstari utachorwa kati ya alama zote mbili.",
        'form_line_status_1': "Inasubiri bofyo la kwanza...",
        'form_line_status_2': "Alama ya kwanza imewekwa: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Sasa bofya alama ya mwisho...",
        'form_line_status_4': "Alama zote mbili zimewekwa.\nBofya 'Maliza' ili kuhifadhi.",
        'form_line_reset': "Weka upya",
        'form_line_finish': "Maliza",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Nakili (Cmd+C)",
        'paste': "Bandika (Cmd+V)",
        'copied': "Imenakiliwa: {0}",
        'no_element_to_copy': "Hakuna kipengee kilichochaguliwa cha kunakili",
        'no_copied_data': "Hakuna data iliyonakiliwa",
        'no_valid_position': "Hakuna nafasi halali ya kubandika",
        'copy_text': "Maandishi yamenakiliwa",
        'copy_image': "Picha imenakiliwa",
        'copy_form': "Umbo limenakiliwa",
        'copy_signature': "Sahihi imenakiliwa",
        'element_text': "Maandishi",
        'element_image': "Picha",
        'element_form': "Umbo",
        'element_signature': "Sahihi",
        'element_unknown': "Kipengee",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Mgogoro wa hali",
        'mode_conflict_message': "Hali '{0}' tayari imeamilishwa.\n\nJe, unataka kuimaliza na {1}?",
        'mode_replace': "Maliza hali na {0}",
        'mode_cancel': "Ghairi",
        'mode_replace_text': "Ingiza maandishi",
        'mode_replace_cross': "Ingiza msalaba",
        'mode_replace_signature': "Ingiza sahihi",
        'mode_replace_image': "Ingiza picha",
        'mode_replace_form': "Ingiza umbo",
        'mode_conflict_voice': "Hali ya {0} imeamilishwa. Maliza na ingiza maandishi?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Kuingiza maandishi",
        'active_mode_signature': "Sahihi",
        'active_mode_image': "Picha",
        'active_mode_form': "Umbo",
        'active_mode_and': " na ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Ingiza",                    # Hauptmenü
        'insert_another_text': "Ingiza maandishi",          # Vereinfacht
        'insert_another_cross': "Ingiza msalaba",        # Vereinfacht
        'insert_another_signature_1': "Sahihi 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Sahihi 2",      # Untermenü-Eintrag
        'insert_another_image': "Ingiza picha",         # Vereinfacht
        'insert_another_form_rect': "Mstatili",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Duwara",        # Untermenü-Eintrag
        'insert_another_form_line': "Mstari (mibofyo 2)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Mshale (mibofyo 2)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Hifadhi {0}",
        'save_dialog_message': "{0} itahifadhiwa kwenye ukurasa {1}.\n\nJe, unaendeleaje?",
        'save_all': "Hifadhi {0} zote",
        'save_single': "Hifadhi {0}",
        'save_customize': "Rekebisha {0}",
        'save_discard': "Tupilia mbali {0} hii",
        'save_continue': "Endelea kuhariri",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Nenda kwenye ukurasa {0}",
        'context_rotate': " Zungusha ukurasa {0}",
        'context_delete': " Futa ukurasa {0}",
        'context_export': " Hamisha ukurasa {0}",
        'context_mark_as': " Weka alama kwenye ukurasa kama...",
        'context_mark_empty': " Ukurasa tupu",
        'context_unmark_empty': " Sio tupu tena",
        'context_mark_export': " Weka alama kwa kuhamisha",
        'context_unmark_export': " Usihamishe tena",
        'context_batch_actions': " Vitendo vya pamoja",
        'context_batch_delete_empty': " Futa kurasa zote {0} tupu",
        'context_batch_export_single': " Kurasa zote {0} (faili moja)",
        'context_batch_export_split': " Kurasa zote {0} (tofauti)",
        'context_drag_start': " Anza Buruta na Acha",
        'context_drag_stop': " Maliza Buruta na Acha",
        'context_insert': " Ingiza",
        'context_insert_pages': " Ingiza kurasa",
        'context_zoom': "Kukuza",
        'discard_mixed': "Tupilia mbali {0} {1} na {2} {3} zote",
        'save_mixed': "Hifadhi {0} {1} na {2} {3}",
        'discard_texts': "Tupilia mbali maandishi {0} yote",
        'discard_text_single': "Tupilia mbali maandishi 1",
        'save_texts': "Hifadhi maandishi {0}",
        'save_text_single': "Hifadhi maandishi 1",
        'discard_crosses': "Tupilia mbali misalaba {0} yote",
        'discard_cross_single': "Tupilia mbali msalaba 1",
        'save_crosses': "Hifadhi misalaba {0}",
        'save_cross_single': "Hifadhi msalaba 1",
        'discard_signatures': "Tupilia mbali sahihi {0} zote",
        'save_signature_single': "Hifadhi sahihi 1",
        'save_signatures': "Hifadhi sahihi {0}",
        'discard_images': "Tupilia mbali picha {0} zote",
        'save_image_single': "Hifadhi picha 1",
        'save_images': "Hifadhi picha {0}",
        'discard_forms': "Tupilia mbali maumbo {0} yote",
        'save_form_single': "Hifadhi umbo 1",
        'save_forms': "Hifadhi maumbo {0}",
        'cross_discard': "Tupilia mbali msalaba huu",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Habari za Kuhamisha / Kuagiza",
        'export_what': "📋 Nini kinahamishwa?",
        'export_general': "Mipangilio ya jumla",
        'export_general_items': "• Toleo la sauti (kuwasha/kuzima, kasi)\n• Mwezi Giza/Mwanga\n• Mipangilio ya nakala ya usalama\n• Mipangilio ya OCR",
        'export_image_form': "Mipangilio ya picha na maumbo",
        'export_image_form_items': "• Mipangilio ya picha (uwiano wa vipimo, ukubwa wa kawaida)\n• Mipangilio ya maumbo (unene wa mstari, rangi)\n• Mipangilio ya sahihi (njia, ukubwa, muhuri wa muda)",
        'export_passwords': "Hifadhidata ya nyosiri",
        'export_passwords_items': "• Nyosiri zote za PDF zilizohifadhiwa\n• Chaguo la kusimbwa au kufunguliwa",
        'export_master': "Mipangilio ya nenosiri kuu",
        'export_master_items': "• Hashi ya nenosiri kuu\n• Mipangilio ya sahihi/vipande vya maandishi",
        'export_signatures': "Sahihi na vipande vya maandishi",
        'export_signatures_items': "• Faili zote za picha (sahihi)\n• Vipande vyote vya maandishi kwa uumbizaji\n• Alama za faragha/umma",
        'export_import_warning': "⚠️ Vidokezo muhimu",
        'export_import_note': "• Wakati wa kuagiza, mipangilio YOTE ya sasa itaandikwa juu\n• Kuanzisha programu tena inahitajika\n• Sahihi/vipande vya maandishi vilivyopo vitabadilishwa",
        'export_master_note': "• Ikiwa nenosiri kuu limewekwa unaweza kuchagua:\n  - Imefunguliwa (nyosiri katika maandishi wazi)\n  - Imesimbwa (inaweza kusomwa tu kwa nenosiri kuu)",
        'export_security': "• Faili la ZIP lililohamishwa lina data nyeti\n• Tafadhali weka salama (km. kwenye USB iliyosimbwa)\n• Ukipoteza faili: Nyosiri hazitarejeshwa kamwe",
        'export_format': "📁 Umbizo la kuhamisha",
        'export_format_desc': "Mipangilio itahifadhiwa katika faili moja la ZIP:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Mipangilio imehamishwa kwa mafanikio",
        'export_failed': "Uhamishaji umeshindwa",
        'export_import_question': "Je, unataka kuanzisha programu tena sasa?",
        'export_password_question': "Nenosiri kuu limewekwa.\n\nJe, unataka kuhamisha nyosiri zikiwa zimefunguliwa?\n(vinginevyo zitahamishwa zikiwa zimesimbwa)",
        'export_decrypt': "Hamisha zikiwa zimefunguliwa",
        'export_encrypt': "Hamisha zikiwa zimesimbwa",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Habari",
        'info_title': "Kuhusu PDF Dark View",
        'info_version': "Toleo",
        'info_author': "Imetengenezwa na Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Kuhusu",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ni kivinjari cha PDF kinachoweza kufikiwa ambacho kimeundwa mahususi kwa watu wenye matatizo ya kuona.</p>

            <p><strong>Vipengele vikuu:</strong></p>
            <ul>
                <li>Kiolesura chenye utofautishaji wa juu, kinachoweza kubadilishwa</li>
                <li>Udhibiti kamili wa kibodi</li>
                <li>Toleo la sauti lililojumuishwa</li>
                <li>OCR kwa hati zilizochanganuliwa</li>
                <li>Zana za kina za uhariri</li>
            </ul>

            <p>Zaidi ya lugha 50 zinasaidiwa – ili PDF ziweze kufikiwa na wote.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Vipengele",
        'info_features_intro': "PDF Dark View inakupa fursa zifuatazo:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Onyesho na Urambazaji</strong> – Mwezi Giza/Mwanga, kuvinjari kurasa, kukuza, kuruka kwenye ukurasa</li>
            <li><strong>OCR (Utambuzi wa Maandishi)</strong> – Fanya hati zilizochanganuliwa ziweze kutafutwa na kunakiliwa</li>
            <li><strong>Uhariri</strong> – Ingiza maandishi, misalaba, sahihi, picha na maumbo</li>
            <li><strong>Usimamizi wa kurasa</strong> – Futa, toa, ingiza, sogeza kwa Buruta na Acha</li>
            <li><strong>Kuhamisha</strong> – Kama Word, Pages au maandishi</li>
            <li><strong>Usalama</strong> – Ulinzi wa nenosiri na usimamizi</li>
            <li><strong>Ufikivu</strong> – Toleo la sauti, udhibiti wa kibodi, utofautishaji wa juu</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Uendeshaji",
        'info_accessibility': "♿ Ufikivu – udhibiti kamili wa kibodi",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Jumla</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Fungua PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Tafuta</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Badilisha Mwezi Giza/Mwanga</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Chapisha</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Ondoka</div>

        <div class="shortcut-cat">📖 Urambazaji</div>
        <div class="shortcut-row"><kbd>Vitufe vya mishale</kbd> Vinjari ukurasa kwa ukurasa</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Nenda kwenye ukurasa</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Ukurasa wa kwanza</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Ukurasa wa mwisho</div>

        <div class="shortcut-cat">✏️ Uhariri</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Ingiza maandishi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Futa kurasa</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Toa kurasa</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Ingiza kurasa</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Sogeza kurasa</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Zungusha ukurasa</div>

        <div class="shortcut-cat">🖼️ Sogeza vipengee</div>
        <div class="shortcut-row"><kbd>Vitufe vya mishale</kbd> Sogeza maandishi/picha/sahihi</div>
        <div class="shortcut-row"><kbd>Ctrl+vitufe vya mishale</kbd> Hatua kubwa zaidi</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Hifadhi</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Tupilia mbali</div>

        <div class="shortcut-cat">🗣️ Toleo la sauti</div>
        <div class="shortcut-row"><kbd>F2</kbd> Washa/zima toleo la sauti</div>
        """,
        'info_contextmenu': "📌 Muhimu: Kazi zote zinapatikana pia kupitia menyu ya muktadha (bonyeza kulia)!",
        'info_accessibility_hint': "💡 Kidokezo: Toleo la sauti (F2) hurahisisha mwelekeo na hutoa maoni kwa menyu na vidirisha.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Leseni na Taarifa za Kisheria",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 TAARIFA ZA KISHERIA</strong><br>
        Taarifa kulingana na § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        Barua pepe: binhdiez64@gmail.com<br>
        Anayewajibika kwa maudhui: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Kanusho la dhima</strong><br>
        Programu imetengenezwa kwa uangalifu mkubwa. Hakuna dhamana ya usahihi, ukamilifu na utendakazi inayotolewa. Matumizi ni kwa hatari yako mwenyewe.<br><br>

        <strong>📄 Leseni ya MIT (matumizi ya kibinafsi)</strong><br>
        Hakimiliki (c) 2026 Toralf Schulz (BinhDiez)<br>
        Inaruhusiwa: matumizi bila malipo, mabadiliko ya kibinafsi, nakala za kibinafsi.<br>
>        Hairuhusiwi: uuzaji, matumizi ya kibiashara, kuondoa taarifa za hakimiliki.<br><br>

        <strong>🔧 Vipengee vya watoa huduma wengine</strong><br>
        Programu hii ina vipengee chini ya leseni za GPL, AGPL, Apache 2.0, BSD na MIT.<br>
        Wakati wa kusambaza tena, masharti ya leseni husika lazima yazingatiwe.<br><br>

        <strong>🌐 Chanzo Huria</strong><br>
        Msimbo wa chanzo unapatikana na unaweza kutazamwa, kubadilishwa na kusambazwa tena kulingana na masharti ya leseni husika.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Shukrani",
        'info_credits': "Shukrani kwa jumuiya ya Chanzo Huria",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Uchakataji wa PDF</li>
            <li><strong>PyQt5</strong> – Kiolesura cha picha</li>
            <li><strong>Tesseract OCR</strong> – Utambuzi wa maandishi</li>
            <li><strong>OCRmyPDF</strong> – Ujumuishaji wa OCR</li>
            <li><strong>python-docx</strong> – Uhamishaji wa Word</li>
            <li><strong>qtawesome</strong> – Picha ndogo</li>
            <li><strong>DeepSeek</strong> – Usaidizi katika tafsiri (lugha 50+)</li>
            <li><strong>Watumiaji wote</strong> – Kwa maoni muhimu</li>
            <li><strong>Jumuiya ya Chanzo Huria</strong> – Kwa maktaba bora</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Lugha",
        'info_languages_header': "🌍 Usaidizi wa Lugha",
        'info_languages_html': """
        <div style="line-height:1.6;">
            <p>PDF Dark View kwa sasa inasaidia <strong>lugha 62</strong> – ili programu iweze kufikiwa duniani kote.</p>

            <p><strong>📖 Orodha kamili ya lugha (Kufikia Machi 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Kiafrikana</li>
                    <li>🇦🇱 Kialbania (Shqip)</li>
                    <li>🇩🇿 Kiarabu (العربية)</li>
                    <li>🇮🇩 Kibali (Basa Bali)</li>
                    <li>🇧🇩 Kibengali (বাংলা)</li>
                    <li>🇲🇲 Kiburma (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Kibosnia (Bosanski)</li>
                    <li>🇧🇬 Kibulgaria (Български)</li>
                    <li>🇨🇳 Kichina (中文)</li>
                    <li>🇩🇰 Kideni (Dansk)</li>
                    <li>🇩🇪 Kijerumani (Deutsch)</li>
                    <li>🇬🇧 Kiingereza (English)</li>
                    <li>🇪🇪 Kiestonia (Eesti)</li>
                    <li>🇫🇮 Kifini (Suomi)</li>
                    <li>🇫🇷 Kifaransa (Français)</li>
                    <li>🇬🇷 Kigiriki (Ελληνικά)</li>
                    <li>🇮🇱 Kiebrania (עברית)</li>
                    <li>🇮🇳 Kihindi (हिन्दी)</li>
                    <li>🇭🇷 Kikroeshia (Hrvatski)</li>
                    <li>🇭🇺 Kihungaria (Magyar)</li>
                    <li>🇮🇩 Kiindonesia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Kiayalandi (Gaeilge)</li>
                    <li>🇮🇸 Kiaisilandi (Íslenska)</li>
                    <li>🇮🇹 Kiitaliano (Italiano)</li>
                    <li>🇯🇵 Kijapani (日本語)</li>
                    <li>🇰🇭 Kikhmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Kikorea (한국어)</li>
                    <li>🇱🇦 Kilaothia (ພາສາລາວ)</li>
                    <li>🇱🇻 Kilatvia (Latviešu)</li>
                    <li>🇱🇹 Kilithuania (Lietuvių)</li>
                    <li>🇱🇺 Kilasembagi (Lëtzebuergesch)</li>
                    <li>🇲🇾 Kimalesia (Bahasa Melayu)</li>
                    <li>🇮🇳 Kimarathi (मराठी)</li>
                    <li>🇲🇳 Kimongolia (Монгол)</li>
                    <li>🇳🇵 Kinepali (नेपाली)</li>
                    <li>🇳🇱 Kiholanzi (Nederlands)</li>
                    <li>🇳🇴 Kinorwe (Norsk)</li>
                    <li>🇦🇫 Kipashto (پښتو)</li>
                    <li>🇮🇷 Kiajemi (فارسی)</li>
                    <li>🇵🇱 Kipolandi (Polski)</li>
                    <li>🇵🇹 Kireno (Português)</li>
                    <li>🇮🇳 Kipunjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Kiromania (Română)</li>
                    <li>🇷🇺 Kirusi (Русский)</li>
                    <li>🇸🇪 Kiswidi (Svenska)</li>
                    <li>🇷🇸 Kiserbia (Српски)</li>
                    <li>🇸🇰 Kislovakia (Slovenčina)</li>
                    <li>🇸🇮 Kislovenia (Slovenščina)</li>
                    <li>🇪🇸 Kihispania (Español)</li>
                    <li>🇹🇿 Kiswahili (Kiswahili)</li>
                    <li>🇵🇭 Kitagalog (Filipino)</li>
                    <li>🇮🇳 Kitamil (தமிழ்)</li>
                    <li>🇮🇳 Kitelugu (తెలుగు)</li>
                    <li>🇹🇭 Kithai (ไทย)</li>
                    <li>🇨🇿 Kicheki (Čeština)</li>
                    <li>🇹🇷 Kituruki (Türkçe)</li>
                    <li>🇺🇦 Kiukreni (Українська)</li>
                    <li>🇵🇰 Kiurdu (اردو)</li>
                    <li>🇻🇳 Kivietinamu (Tiếng Việt)</li>
                    <li>🇸🇳 Kiwolof (Wolof)</li>
                    <li>🇺🇸 Kiyidi (ייִדיש)</li>
                    <li>🇿🇦 Kizulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Ongeza lugha yako mwenyewe:</strong><br>
                Unataka lugha ambayo bado haijajumuishwa? Weka tu faili yako mwenyewe ya kamusi (<code>sprache_xx.py</code>) karibu na programu – programu itaitambua kiotomatiki. Ikiwa una nia ya tafsiri maalum, tafadhali wasiliana nami.
            </div>

            <p><strong>🙏 Shukrani maalum:</strong> DeepSeek kwa usaidizi katika kutafsiri kamusi zote katika lugha 62.</p>

            <p>📧 Mawasiliano kwa tafsiri: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Hitilafu",
        'error_occurred': "Hitilafu imetokea",
        'error_pdf_load': "Hitilafu wakati wa kupakia PDF",
        'error_pdf_save': "Hitilafu wakati wa kuhifadhi PDF",
        'error_ocr': "Hitilafu katika utambuzi wa maandishi",
        'error_no_pdf': "Hakuna PDF iliyopakiwa",
        'error_page_not_found': "Ukurasa haukupatikana",
        'error_invalid_range': "Safu batili ya kurasa",
        'error_file_not_found': "Faili halikupatikana",
        'error_permission': "Hakuna ruhusa",
        'error_unknown': "Hitilafu isiyojulikana",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Mafanikio",
        'success_operation': "Operesheni imekamilika kwa mafanikio",
        'success_saved': "Imehifadhiwa kwa mafanikio",
        'success_exported': "Imehamishwa kwa mafanikio",
        'success_imported': "Imeagizwa kwa mafanikio",
        'success_deleted': "Imefutwa kwa mafanikio",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Uthibitisho",
        'confirm_yes': "Ndiyo",
        'confirm_no': "Hapana",
        'confirm_ok': "Sawa",
        'confirm_cancel': "Ghairi",
        'confirm_delete': "Futa",
        'confirm_overwrite': "Andika juu",
        'confirm_continue': "Endelea",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF inapakiwa...",
        'progress_saving': "PDF inahifadhiwa...",
        'progress_exporting': "PDF inahamishwa...",
        'progress_processing': "Usindikaji unaendelea...",
        'progress_wait': "Tafadhali subiri...",
        'progress_preparing': "Maandalizi...",
        'progress_finalizing': "Inakamilishwa...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Nyeupe",
        'color_black': "Nyeusi",
        'color_red': "Nyekundu",
        'color_green': "Kijani",
        'color_blue': "Bluu",
        'color_yellow': "Njano",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Machungwa",
        'color_gray': "Kijivu",
        'color_custom': "Chagua rangi",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Faili",
        'menu_edit': "&Hariri",
        'menu_view': "&Tazama",
        'menu_tools': "&Zana",
        'menu_settings': "&Mipangilio",
        'menu_help': "&Usaidizi",
        'menu_language': "🌐 Lugha",
        'menu_guides': "&Mwongozo",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Fungua",
        'file_save_as': "&Hifadhi kama...",
        'file_protect': "&Linda hati...",
        'file_export': "&Hamisha",
        'file_export_pages': "Hamisha kama Pages",
        'file_export_word': "Hamisha kama DOCX",
        'file_export_text': "Hamisha kama TXT",
        'file_print_now': "&Chapisha sasa",
        'file_print': "&Chapisha",
        'file_close': "&Funga",
        'file_quit': "&Ondoka",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Tafuta",
        'edit_ocr': " Fanya OCR",
        'edit_rotate': "&Zungusha ukurasa",
        'edit_rotate_all': "&Zungusha kurasa zote",
        'edit_delete_pages': "&Futa kurasa",
        'edit_extract_pages': "&Toa kurasa",
        'edit_insert_pages': "&Ingiza kurasa",
        'edit_move_pages': "&Sogeza kurasa",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Ingiza maandishi na misalaba",
        'text_insert': " Ingiza maandishi",
        'cross_insert': " Ingiza msalaba",
        'text_customize': " Rekebisha maandishi",
        'cross_customize': " Rekebisha msalaba huu",
        'cross_customize_all': " Rekebisha misalaba yote",
        'text_discard': " Tupilia mbali maandishi/msalaba huu",
        'text_discard_all': " Tupilia mbali maandishi na misalaba yote",
        'text_save_all': " Hifadhi maandishi na misalaba yote",
        'text_guide': " Kuingiza maandishi / Vipande vya maandishi - Mwongozo",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Ingiza sahihi",
        'signature_settings_menu': " Mipangilio...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Ingiza picha",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Ingiza maumbo",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Onyesha dirisha la maandishi",
        'view_zoom': "&Kukuza",
        'view_zoom_page': "&Upana wa ukurasa (Kawaida)",
        'view_zoom_two': "&Kurasa mbili",
        'view_zoom_overview': "&Muhtasari (kurasa nyingi)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Usaidizi wa ufikivu",
        'settings_voice': "Toleo la sauti",
        'settings_voice_tooltip': "huongeza maelezo ya ziada kwa toleo la sauti la visoma skrini",
        'settings_signature': "&Mipangilio ya sahihi",
        'settings_password': "&Usimamizi wa nenosiri",
        'settings_backup': "Unda nakala ya usalama kabla ya mabadiliko",
        'settings_export_import': "&Hamisha / Agiza mipangilio",
        'settings_export': "&Hamisha mipangilio yote...",
        'settings_import': "&Agiza mipangilio yote...",
        'settings_export_info': "&Nini kinahamishwa?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "imewashwa",
        'voice_off': "imezimwa",
        'voice_toggle': "Toleo la sauti {0}",
        'voice_speed': "Kasi kwa asilimia {0}",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Zana haikupatikana:\n{0}\n\nBASE_DIR: {1}\nHakikisha kuwa zana za PDF zimesakinishwa kwenye saraka {1}.",
        'tool_started': "{0} imeanzishwa",
        'tool_start_failed': "Haikuweza kuanzishwa",
        'process_error_failed_to_start': "Mchakato haukuweza kuanzishwa. Je, faili lipo?",
        'process_error_crashed': "Mchakato ulianguka wakati wa kuanza.",
        'process_error_timeout': "Muda wa mchakato umeisha.",
        'process_error_write': "Hitilafu ya kuandika katika mchakato.",
        'process_error_read': "Hitilafu ya kusoma katika mchakato.",
        'process_error_unknown': "Hitilafu isiyojulikana ya mchakato",
        'process_command': "Amri",
        'process_normal_exit': "imeisha kwa kawaida",
        'process_crashed': "imeanguka",
        'process_nonzero_exit': "{0} imeisha kwa msimbo wa hitilafu {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Inaghairiwa...",
        'move_cancelling': "Uhamishaji unaghairiwa",
        'opening_pdf': "PDF inafunguliwa...",
        'loading_document': "Inapakia hati...",
        'pdf_opened': "PDF imefunguliwa",
        'pages_found_moving': "Kurasa {0} zimepatikana, {1} za kuhamisha",
        'creating_backup': "Inaunda nakala ya usalama...",
        'backup_description': "Inahifadhi faili asili...",
        'backup_saved_as': "Imehifadhiwa kama: {0}",
        'error_format': "Hitilafu: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Utafutaji umeondolewa",
        'page_header_simple': "=== Ukurasa {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Usimamizi wa nenosiri – Mwongozo",
        'password_guide_voice': "Mwongozo wa usimamizi wa nenosiri. Tafadhali soma maelekezo.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Usimamizi wa nenosiri – Mwongozo wa Kina</strong></p>

        <p><strong>1. Ulinzi wa nenosiri kwa PDF</strong></p>
        <ul>
        <li>Unapofungua PDF iliyolindwa kwa nenosiri, kidirisha kitaonekana ambapo unaweza kuingiza nenosiri.</li>
        <li>Unaweza kuhifadhi nenosiri kwa usimbaji, ili usilazimike kuliingiza kila wakati (kisanduku cha uteuzi "Hifadhi nenosiri").</li>
        <li>Kwa kitufe "Ondoa nenosiri" unaweza kuunda nakala iliyofunguliwa ya PDF na kufuta nenosiri kutoka kwenye hifadhidata.</li>
        </ul>

        <p><strong>2. Nenosiri Kuu</strong></p>
        <ul>
        <li>Nenosiri kuu linalinda ufikiaji wa nyosiri zote za PDF zilizohifadhiwa.</li>
        <li><strong>Kuweka:</strong> Nenda kwenye "Mipangilio → Usimamizi wa nenosiri → Mipangilio ya Nenosiri Kuu" na ubofye "Weka nenosiri kuu". Chagua nenosiri kuu salama (angalau herufi 8).</li>
        <li><strong>Kubadilisha:</strong> Baada ya uthibitishaji uliofanikiwa unaweza kubadilisha nenosiri kuu.</li>
        <li><strong>Kuondoa:</strong> Ukifuta nenosiri kuu, NYOSIRI ZOTE zilizohifadhiwa zitafutwa kwa kudumu. Unaweza kuhamisha nakala ya usalama kabla.</li>
        <li>Mara moja kwa kila kipindi, lazima ujitambulishe kwa nenosiri kuu ili kupata kazi zilizolindwa (kwa mfano kuona nyosiri).</li>
        </ul>

        <p><strong>3. Usimamizi wa nenosiri (Orodha)</strong></p>
        <ul>
        <li>Chini ya "Mipangilio → Usimamizi wa nenosiri" unafungua jedwali la PDF zote zilizohifadhiwa pamoja na nyosiri zao zilizosimbwa.</li>
        <li><strong>Bila nenosiri kuu:</strong> Unaweza tu kufuta maingizo – nyosiri zinabaki zimefichwa.</li>
        <li><strong>Kwa nenosiri kuu (umejidhinisha):</strong> Unaweza kuona, kunakili, kuhamisha na kufuta nyosiri.</li>
        <li><strong>Kuhamisha:</strong> Chagua umbizo (JSON, CSV, TXT) na uhifadhi orodha. Ikiwa nenosiri kuu limewekwa, unaweza kuamua kama nyosiri zitahamishwa kwa maandishi wazi au zikiwa zimesimbwa.</li>
        <li><strong>Kuagiza:</strong> Faili la ZIP lililohamishwa hapo awali (pamoja na mipangilio) linaweza kusomwa tena kupitia "Mipangilio → Hamisha / Agiza mipangilio". Tahadhari: Data iliyopo itaandikwa juu!</li>
        </ul>

        <p><strong>4. Kizalisha nenosiri</strong></p>
        <ul>
        <li>Katika kidirisha cha nenosiri (kwa mfano wakati wa kulinda PDF) utapata kitufe cha kete 🎲 upande wa kulia wa sehemu ya kuingiza.</li>
        <li>Bofya ili kufungua kizalisha nenosiri. Unaweza kuweka urefu, seti za herufi (herufi kubwa, herufi ndogo, nambari, alama maalum) na kitenganishi kwa usomaji bora.</li>
        <li>Nenosiri lililozalishwa linaweza kuchukuliwa moja kwa moja na pia kunakiliwa ikiwa inahitajika.</li>
        </ul>

        <p><strong>5. Vidokezo muhimu vya usalama</strong></p>
        <ul>
        <li>Nyosiri zilizohifadhiwa zimehifadhiwa kwa usimbaji wa AES-256. Ufunguo unatokana na nenosiri lako kuu (ikiwa limewekwa) au kutoka kwa thamani isiyobadilika (bila nenosiri kuu).</li>
        <li>Bila nenosiri kuu, nyosiri zimesimbwa lakini ufunguo umehifadhiwa kwenye programu – mshambuliaji aliye na ufikiaji wa faili zako anaweza kuzifungua. Kwa hivyo tunapendekeza sana kutumia nenosiri kuu.</li>
        <li>Hifadhidata ya nenosiri iko kwenye saraka `Daten/passwords.json`. Fanya nakala za usalama mara kwa mara, haswa kabla ya kuondoa nenosiri kuu.</li>
        <li>Ukipoteza nenosiri kuu, nyosiri zote zilizohifadhiwa hazitarejeshwa kamwe.</li>
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
        'invert_mode_label': "Hali ya kugeuza",
        'invert_mode_classic': "Kawaida (geuza rangi zote)",
        'invert_mode_smart': "Akili (geuza mwangaza tu)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Kizingiti cha kijivu",
        'gray_threshold_10': "10% (kali)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (kawaida)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (laini)",
        'threshold_changed': "Kizingiti kimewekwa kwa {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Kizingiti cha kijivu – Maelezo",
        'threshold_guide_text': "Kizingiti cha kijivu huamua ni pikseli gani katika hali ya akili ya Mwezi Giza zinachukuliwa kama 'kijivu' na kugeuzwa.\n\n"
                                "• Thamani ya chini (10%) hugeuza tu rangi za kijivu karibu kamili – vipengee vya rangi vinabaki vilivyohifadhiwa kabisa.\n"
                                "• Thamani ya juu (50%) hugeuza hata pikseli zenye rangi kidogo – hii huongeza utofautishaji, lakini inaweza kupotosha rangi.\n\n"
                                "Thamani bora inategemea hati. Kwa hati za maandishi tu, 30–40% mara nyingi ni bora, kwa michoro ya rangi 10–20%.\n\n"
                                "Unaweza kurekebisha thamani wakati wowote kupitia menyu ya 'Mipangilio' – PDF itapakiwa upya mara moja.\n\n"
                                "Kumbuka:\n* Picha na picha zinaweza kuonyeshwa kwa usahihi tu katika Mwezi Mwanga!\n* Mipangilio ya kugeuza inaonyeshwa tu wakati Mwezi Giza umeamilishwa.",
        'threshold_guide_voice': "Kizingiti cha kijivu huamua ni kwa kiasi gani hali ya akili ya Mwezi Giza inaingilia. Thamani ya chini huhifadhi rangi, thamani ya juu huongeza utofautishaji.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF inafunguliwa...",
        'progress_loading_document': "Inapakia hati...",
        'progress_pdf_opened': "PDF imefunguliwa",
        'progress_creating_backup': "Inaunda nakala ya usalama...",
        'progress_backup_description': "Inahifadhi faili asili...",
        'progress_backup_created': "Nakala ya usalama imeundwa",
        'progress_backup_saved_as': "Imehifadhiwa kama: {0}",
        'progress_analyzing_start': "Inaanza uchambuzi...",
        'progress_searching_empty': "Inatafuta kurasa tupu...",
        'progress_page_empty': "Ukurasa {0} ni tupu",
        'progress_page_keep': "Ukurasa {0} utahifadhiwa",
        'progress_analysis_complete': "Uchambuzi umekamilika",
        'progress_empty_found': "Kurasa {0} tupu zimepatikana",
        'progress_current_page': "Ukurasa wa sasa",
        'progress_mark_delete': "Inawekwa alama ya kufuta",
        'progress_range_selected': "Safu ya kurasa {0}-{1}",
        'progress_deleting_pages': "Inafuta kurasa {0}",
        'progress_creating_new_pdf': "Inaunda PDF mpya...",
        'progress_transferring_pages': "Inahamisha kurasa",
        'progress_keeping_page': "Ukurasa {0} utahifadhiwa ({1}/{2})",
        'progress_saving_pdf': "Inahifadhi PDF...",
        'progress_optimizing': "Inaboresha ukubwa wa faili...",
        'progress_finalizing': "Inakamilisha...",
        'progress_new_size': "Ukubwa mpya: {0:.2f} MB",
        'progress_cancelling': "Inaghairiwa...",
        'progress_cancel_message': "{0} inaghairiwa",
        'progress_pages_found_moving': "Kurasa {0} zimepatikana, {1} za kuhamisha",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF inachambuliwa...",
        'ocr_status_optimizing': "Uboreshaji wa picha unaendelea...",
        'ocr_status_recognizing': "Utambuzi wa maandishi unaendelea...",
        'ocr_status_embedding': "Maandishi yanapachikwa...",
        'ocr_status_finalizing': "PDF inakamilishwa...",

        # PDF-Laden
        'progress_preparing': "Maandalizi...",
        'progress_loading': "PDF inapakiwa...",

        # Seitenoperationen
        'progress_deleting_title': "Inafuta kurasa...",
        'progress_moving_title': "Inasogeza kurasa...",
        'pages_found': "Kurasa zimepatikana",
        'progress_creating_new_order': "Inaunda mpangilio mpya...",
        'progress_sorting_pages': "Inapanga kurasa...",
        'progress_moving_to_begin': "Inasogeza kurasa {0} mwanzoni",
        'progress_transferring_count': "Inahamisha kurasa {0}",
        'progress_transferring_before_target': "Inahamisha kurasa kabla ya lengwa",
        'progress_moving_pages': "Inasogeza kurasa {0}",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_nakala_usalama_",
        'filename_protected_suffix': "_iliyolindwa_",
        'filename_copy_suffix': "_nakala",
        'filename_page_single': "_ukurasa_",
        'filename_page_range': "_kurasa_",
        'filename_export_page': "_ukurasa_{0:03}",
        'filename_export_range': "_kurasa_{0}-{1}",
        'filename_export_multiple': "_kurasa_{0}",
        'filename_with_text': "_kwa_maandishi",
        'filename_with_signature': "_kwa_sahihi",
        'filename_with_image': "_kwa_picha",
        'filename_with_forms': "_kwa_maumbo",
        # ---------------------------------------------------------
        # Zentrale Verwaltung des Formats der Zeitstempel
        # ---------------------------------------------------------
        'filename_timestamp_format': "%Y%m%d_%H%M%S",
        'filename_timestamp_micro': "%Y%m%d_%H%M%S_%f",

        # ============================================
        # 56. ANSICHT – BUTTONLEISTE EIN-/AUSBLENDEN
        # ============================================
        'view_toggle_navbar': "Onyesha upau wa vitufe",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Haiwezekani kufuta kurasa zote",
		'pages_cannot_delete_last_page': 'Ukurasa wa mwisho hauwezi kufutwa!',
		'pages_cannot_delete_all_pages': 'Lazima angalau ukurasa mmoja ubaki kwenye hati!',
		'delete_pages_confirm': 'Una uhakika unataka kufuta kurasa {0}?',
		'delete_pages_confirm_voice': 'Una uhakika unataka kufuta kurasa {0}?',
		'pages_deleted': 'Kurasa {0} zimefutwa kikamilifu.',
		'warning': 'Onyo',
		'error': 'Hitilafu',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Hakuna fomu iliyochaguliwa",
        'form_customized': "Fomu imebinafsishwa",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Chagua",
        'btn_use': "Tumia",
        'master_password_for_spasswords': "Ili kuhifadhi na kutumia nywila, lazima kwanza uweke nywila kuu.\n\nJe, unataka kuweka nywila kuu sasa?",
        'open_saved_dialog_title': "Fungua faili iliyohifadhiwa",
        'open_saved_question': "Je, unataka kufungua faili iliyohifadhiwa sasa?",
        'password': "Nywila",
        'password_manager_master_required': "Kidhibiti cha nywila kinapatikana tu ikiwa nywila kuu imewekwa.\n\nJe, unataka kuweka nywila kuu sasa?",
        'password_master_required_for_select': "Ili kuona na kuchagua nywila zilizohifadhiwa, lazima kwanza uthibitishe kwa nywila yako kuu.\n\nJe, unataka kuthibitisha sasa?",
        'password_not_available': "Nywila iliyochaguliwa haipatikani au haikuweza kusimbuliwa.",
        'password_options_title': "Chaguo za nywila",
        'password_save_choice_change': "Weka nywila mpya",
        'password_save_choice_keep': "Tumia nywila iliyopo",
        'password_save_choice_none': "Hifadhi bila usimbaji fiche",
        'password_save_hint': "Kwanza weka nywila kuu ili kuhifadhi nywila kwa usalama.",
        'password_save_master_required': "Hifadhi nywila (inawezekana tu kwa nywila kuu)",
        'password_save_question': "PDF ya sasa imelindwa kwa nywila. Je, unataka kutumia nywila iliyopo, kuweka mpya au kuhifadhi bila usimbaji fiche?",
        'password_select': "Chagua nywila",
        'password_select_none': "Hakuna nywila iliyochaguliwa.\n\nTafadhali chagua nywila kutoka kwenye orodha.",
        'password_select_one': "Tafadhali chagua nywila moja tu.\n\nUmeweka alama kwenye nywila nyingi.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_chelezo",
        'filename_insert_suffix': "_kwa_uingizaji",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_kurasa_zimefutwa",
        'filename_pages_moved': "_kurasa_zimehamishwa",
        'filename_rotated_all_suffix': "_kurasa_zote_zimezungushwa",
        'filename_rotated_suffix': "_ukurasa_umezungushwa",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Usanidi wa majina ya faili wakati wa kubadilisha PDF",
        'filename_keep_suffixes': "Hifadhi viambishi vilivyotangulia (mfano: _kwa_maandishi)",
        'filename_keep_suffixes_false': "Badilisha",
        'filename_keep_suffixes_true': "Hifadhi",
        'filename_preview_label': "Muundo wa awali wa jina la faili:",
        'filename_preview_overwrite_hint': "Muundo wa awali haupatikani – asili itaandikwa juu.",
        'filename_separator': "Kitenganishi kati ya maneno",
        'filename_separator_none': "Hakuna kitenganishi",
        'filename_separator_space': "Nafasi ( )",
        'filename_separator_underscore': "Kistari (_)",
        'filename_settings_saved': "Mipangilio ya jina la faili imehifadhiwa",
        'filename_settings_title': "Uumbizaji wa jina la faili na chelezo",
        'filename_timestamp_position': "Nafasi ya muhuri wa muda",
        'filename_timestamp_position_after': "Baada ya jina la msingi",
        'filename_timestamp_position_before': "Mbele kabisa",
        'filename_timestamp_position_end': "Mwishoni",
        'filename_use_timestamp': "Tumia muhuri wa muda",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Tabia wakati wa mabadiliko:</b><ul><li>Kufuta na kuingiza kurasa</li><li>Kuingiza maandishi, sahihi, picha na maumbo</li><li>OCR</li></ul></html>",
        'backup_section': "Chelezo kwa shughuli za kurasa (Futa, Hamisha)",
        'behavior_info': "Kumbuka: Kwenye 'Andika juu ya asili', mihuri ya muda na viambishi hupuuzwa – faili huhifadhi jina lake.",
        'behavior_new_file': "Daima tengeneza faili mpya (kwa muhuri wa muda na kiambishi)",
        'behavior_overwrite': "Andika juu ya asili (hakuna faili mpya)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Kurasa zote zimezungushwa.\n\nAsili imebaki bila kubadilika.\nFaili mpya: {0}",
        'all_pages_rotated_voice': "Kurasa zote zimezungushwa, faili mpya imeundwa.",
        'empty_pages_deleted_new_file': "{0} kurasa tupu zimefutwa.\n\nAsili imebaki bila kubadilika.\nFaili mpya: {1}",
        'empty_pages_deleted_voice': "{0} kurasa tupu zimefutwa, faili mpya imeundwa.",
        'ocr_keep_original': "Hifadhi asili (fungua mwenyewe baadaye)",
        'ocr_new_file_question': "PDF mpya inayotafutwa imehifadhiwa kwenye:\n{0}\n\nJe, unataka kuifungua sasa?",
        'ocr_open_new': "Fungua faili mpya ya OCR",
        'ocr_original_kept': "Faili asili inabaki wazi. Faili ya OCR imehifadhiwa.",
        'page_deleted_new_file': "Ukurasa {0} umefutwa.\n\nAsili imebaki bila kubadilika.\nFaili mpya: {1}",
        'page_deleted_voice': "Ukurasa {0} umefutwa, faili mpya imeundwa.",
        'page_rotated_new_file': "Ukurasa {0} umezungushwa.\n\nAsili imebaki bila kubadilika.\nFaili mpya: {1}",
        'page_rotated_voice': "Ukurasa {0} umezungushwa, faili mpya imeundwa.",
        'pages_deleted_new_file': "Kurasa {0} zimefutwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya: {1}",
        'pages_deleted_new_file_voice': "Kurasa {0} zimefutwa, faili mpya imeundwa.",
        'pages_inserted_new_file': "Kurasa {0} zimeingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya: {1}",
        'pages_inserted_new_file_ask': "Kurasa {0} zimeingizwa.\n\nAsili imebaki bila kubadilika.\nFaili mpya: {1}\n\nJe, unataka kuifungua sasa?",
        'pages_inserted_voice_new': "Kurasa {0} zimeingizwa, faili mpya imeundwa.",
        'pages_moved_new_file': "Kurasa {0} zimehamishwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya: {1}",
        'pages_moved_new_file_voice': "Kurasa {0} zimehamishwa, faili mpya imeundwa.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Usionyeshe tena",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Mpangilio wa chelezo</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Chelezo IMEWASHA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Kwenye mabadiliko yote yanayoandika juu ya asili</strong> (maandishi, sahihi, picha, umbo, OCR, kuzungusha, kuingiza, kufuta/kuhamaisha kurasa) <strong>chelezo kwa muhuri wa muda huundwa kiotomatiki</strong> kabla ya mabadiliko kutumika.</p>
                <p style="margin: 5px 0 5px 20px;">• Chelezo iko kando ya faili asili (mfano: <code>Hati_chelezo_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Ikiwa umeanzisha chaguo la <strong>„Andika juu ya asili“</strong> kwa kuongeza, chelezo pia huundwa.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Chelezo IMEZIMWA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Hakuna chelezo kinachoundwa</strong> – wala wakati wa kuandika juu, wala wakati wa shughuli za kurasa.</p>
                <p style="margin: 5px 0 5px 20px;">• Faili asili inaweza kupotea kwa kudumu wakati wa kuandikwa juu.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Inapendekezwa kwa watumiaji wenye uzoefu tu!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Kidokezo:</strong> Mpangilio wa chelezo haujitegemei na chaguo la „Andika juu ya asili“. Unaweza kuchanganya vyote viwili.<br>
                Unaweza kuficha ujumbe huu kwa kudumu.
            </div>
        </div>
        """,
        'backup_info_title': "Tabia ya chelezo",
        'backup_info_voice': "Notisi kuhusu tabia ya chelezo kwenye shughuli za kurasa. Chelezo imewasha inaandika juu ya asili, chelezo imezimwa inaunda faili mpya.",
        'show_backup_info': "Maelezo kuhusu mpangilio wa chelezo",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Usionyeshe tena",
        'overwrite_enable_backup': "Washa chelezo (inapendekezwa)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Andika juu ya asili</p>
            <p>Ikiwa utawezesha chaguo hili, mabadiliko (maandishi, sahihi, picha, umbo, OCR, kuzungusha, kuingiza) <strong>yanahifadhiwa moja kwa moja kwenye asili</strong> – <strong>hakuna faili mpya inayoundwa</strong>.</p>
            <p>• Jina la faili linabaki bila kubadilika.<br>
            • Muhuri wa muda na viambishi hupuuzwa.<br>
            • <strong>Bila chelezo, asili inaweza kupotea kwa kudumu.</strong></p>
            <p style="color: #FFD700;">Pendekezo: Wezesha pia chaguo la chelezo ili kupata nakala za usalama za kiotomatiki.</p>
        </div>
        """,
        'overwrite_info_title': "Andika juu ya asili",
        'overwrite_info_voice': "Tahadhari: Andika juu ya asili – hakuna faili mpya. Chelezo inapendekezwa.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Kurasa {0} zimeingizwa.\n\nFaili asili imeandikwa juu.\nChelezo imeundwa.",
        'pages_inserted_overwrite_no_backup': "Kurasa {0} zimeingizwa.\n\nFaili asili imeandikwa juu.\nHakuna chelezo kilichoundwa.",
        'texts_saved_overwrite_with_backup': "Mabadiliko yamehifadhiwa kwenye asili.\n\nChelezo imeundwa.",
        'texts_saved_overwrite_no_backup': "Mabadiliko yamehifadhiwa kwenye asili.\n\nHakuna chelezo kilichoundwa.",
        'texts_crosses_saved_new_file': "{0} {1} na {2} {3} zimeingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya imeundwa.\n\nPDF mpya inapakia...",
        'texts_saved_new_file': "{0} {1} zimeingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya imeundwa.\n\nPDF mpya inapakia...",
        'crosses_saved_new_file': "{0} {1} zimeingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya imeundwa.\n\nPDF mpya inapakia...",
        'elements_saved_new_file': "{0} vipengele vimeingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya imeundwa.\n\nPDF mpya inapakia...",
        'signatures_saved_overwrite_with_backup': "Sahihi zimehifadhiwa kwenye asili.\n\nChelezo imeundwa.",
        'signatures_saved_overwrite_no_backup': "Sahihi zimehifadhiwa kwenye asili.\n\nHakuna chelezo kilichoundwa.",
        'images_saved_overwrite_with_backup': "Picha zimehifadhiwa kwenye asili.\n\nChelezo imeundwa.",
        'images_saved_overwrite_no_backup': "Picha zimehifadhiwa kwenye asili.\n\nHakuna chelezo kilichoundwa.",
        'forms_saved_overwrite_with_backup': "Maumbo yamehifadhiwa kwenye asili.\n\nChelezo imeundwa.",
        'forms_saved_overwrite_no_backup': "Maumbo yamehifadhiwa kwenye asili.\n\nHakuna chelezo kilichoundwa.",
        'signatures_saved_new_file': "Sahihi {0} zimeingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya imeundwa.\n\nPDF mpya inapakia...",
        'images_saved_new_file': "Picha {0} zimeingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya imeundwa.\n\nPDF mpya inapakia...",
        'forms_saved_new_file': "Maumbo {0} yameingizwa.\n\nFaili asili imebaki bila kubadilika.\nFaili mpya imeundwa.\n\nPDF mpya inapakia...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Tahadhari: PDF hii ina kurasa zilizozungushwa. Nafasi inaweza kuwa tofauti.",
        'page_rotated_warning_title': "Ukurasa uliozungushwa umegunduliwa",
        'page_rotated_warning_message': "Ukurasa wa sasa {0} umezungushwa {1}°.\n\nKuingiza vipengele kwenye kurasa zilizozungushwa hakutumiki.\n\nJe, unataka kuzungusha ukurasa kwenye mkao wima sasa?",
        'page_rotated_warning_voice': "Tahadhari: Ukurasa umezungushwa. Tafadhali uzungushe kwanza.",
        'paste_on_rotated_page_simple_warning': "Kuingiza kwenye ukurasa {0} hakunawezekani!\n\nUkurasa huu umezungushwa {1}°.\n\nTafadhali kwanza zungusha ukurasa hadi 0° (Menyu: Hariri → Pangilia ukurasa).\n\nTahadhari:\nKipengele kilichonakiliwa hapo awali kitapotea ikiwa hutahifadhi kabla ya kuzungusha ukurasa.",
        'paste_on_rotated_page_voice': "Kuingiza kumefutwa. Ukurasa umezungushwa. Tafadhali pangilia ukurasa kwanza.",
        'page_rotated_cancel': "Ghairi",
        'page_rotated_rotate_until_upright': "Zungusha ukurasa mara kwa mara (mpaka uwe wima)",
        'page_rotated_now_upright': "Ukurasa sasa uko wima. Sasa unaweza kuingiza.",
        'page_rotated_still_not_upright': "Ukurasa haukuweza kuzungushwa kwenye mkao wima. Tafadhali sahihisha kwa mkono.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Usaidizi: Sahihisha kurasa zilizozungushwa",
        'help_rotated_pages_voice': "Usaidizi wa kusahihisha kurasa zilizozungushwa unafunguliwa.",
        'btn_help': "Usaidizi",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Tatizo: Ukurasa umezungushwa – Kuingiza haifanyi kazi vizuri</p>

            <p>Ikiwa kuingiza maandishi, sahihi au maumbo kwenye ukurasa uliozungushwa hakufanyi kazi vizuri, unaweza kusahihisha ukurasa kwa kihariri cha PDF cha nje.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Suluhisho kwa zana ya nje (mfano: macOS Onyesha)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Safirisha ukurasa</strong><br>
                &nbsp;&nbsp;Bonyeza kwenye menyu <strong>Faili → Safirisha kama kurasa</strong> au tumia njia nyingine kuhifadhi ukurasa unaotaka kama PDF moja.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Fungua ukurasa kwenye programu ya nje</strong><br>
                &nbsp;&nbsp;Fungua PDF iliyosafirishwa kwenye kihariri cha PDF (mfano: <strong>macOS Onyesha</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Zungusha ukurasa</strong><br>
                &nbsp;&nbsp;Zungusha ukurasa ili uwe wima (kwenye Onyesha: <strong>Zana → Zungusha</strong> au <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Hifadhi</strong><br>
                &nbsp;&nbsp;Hifadhi ukurasa uliosahihishwa (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Ingiza tena ukurasa kwenye hati asili</strong><br>
                &nbsp;&nbsp;Rudi kwenye PDFDarkView na uingize ukurasa uliosahihishwa kwenye nafasi unayotaka:<br>
                &nbsp;&nbsp;<strong>Hariri → Ingiza kurasa</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Njia mbadala: Zungusha ukurasa kwenye asili</p>
                <p style="margin: 5px 0 5px 20px;">• Tumia kitendaji cha kuzungusha kilichojengewa ndani (<strong>Hariri → Zungusha ukurasa</strong>) ili kusahihisha ukurasa hatua kwa hatua.<br>
                • Baada ya kila kuzungusha, unaweza kuangalia ikiwa kuingiza kunafanya kazi sasa.<br>
                • Hii mara nyingi ni suluhisho la haraka – jaribu kwanza!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Kidokezo:</strong> Ikiwa mara nyingi unakutana na kurasa zilizozungushwa, unaweza kuficha onyo kwenye kidirisha cha kuingiza kwa kudumu.<br>
                Nafasi inaweza kuwa tofauti – tumia chaguo hili tu ikiwa unajua matokeo.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Pangilia kurasa",
        'menu_rotate_normalize_tooltip': "Zungusha ukurasa au weka upya kwa 0°",
        'normalize_current_page': "Leta ukurasa wa sasa kwenye mkao wima (weka kwa 0°)",
        'normalize_all_pages': "Leta kurasa zote kwenye mkao wima (weka kwa 0°)",
        'page_normalized': "Ukurasa {0} umewekwa kwenye mkao wima.",
        'all_pages_normalized': "Kurasa zote zimewekwa kwenye mkao wima.",
        'page_already_upright': "Ukurasa {0} tayari uko wima.",
        'all_pages_already_upright': "Kurasa zote tayari ziko wima.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF haina maandishi yanayotafutwa.</p><p>Je, unataka kufanya OCR ili kusafirisha kwa {0}?</p>",
        'export_ocr_voice': "PDF haina maandishi. OCR inahitajika kwa usafirishaji kwa {0}.",
        'export_no_ocr_possible': "Usafirishaji bila OCR hauwezekani. Tafadhali fanya OCR kupitia menyu.",
        'ocr_failed_export_not_possible': "OCR imeshindwa. Usafirishaji hauwezi kufanywa.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF itafunguliwa kwenye Onyesha. Tafadhali anza mchakato wa uchapishaji huko.",
        'print_preview_manual': "PDF imefunguliwa. Tafadhali tekeleza amri ya uchapishaji kwa mkono (mfano: Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Unganisha PDF",
        'merge_pdfs': "Unganisha PDF",
        'merge_progress_title': "Inaunganisha PDF...",
        'merge_pdfs_list': "PDF kwa mpangilio (Buruta na uachwe ili kupanga)",
        'merge_add_pdf': "Ongeza PDF",
        'merge_remove': "Ondoa",
        'merge_move_up': "Juu",
        'merge_move_down': "Chini",
        'merge_pdfs_info': "💡 Kidokezo: Unaweza kubadilisha mpangilio kwa kuburuta na kuacha",
        'merge_no_pdfs': "Hakuna PDF iliyochaguliwa. Bonyeza 'Ongeza PDF'.",
        'merge_info': "{0} PDF zimechaguliwa (takriban kurasa {1})",
        'merge_open_file': "Fungua faili",
        'merge_merge': "Unganisha",
        'merge_error': "Hitilafu wakati wa kuunganisha",
        'merge_min_two_pdfs_error': "Tafadhali chagua angalau faili mbili za PDF za kuunganisha.",
        'merge_select_pdfs': "Chagua PDF za kuunganisha",
        'merge_error_file': "Hitilafu wakati wa kuchakata",
        'merge_cancelled': "Kuunganisha kulighairiwa",
        'merge_preparing': "Inaandaa...",
        'merge_processing': "Inachakata PDF {0} kati ya {1}",
        'merge_saving': "Inahifadhi PDF iliyounganishwa...",
        'merge_complete': "Imekamilika!",
        'merge_success_title': "Kuunganisha kumefanikiwa",
        'merge_success_voice': "PDF {0} zimeunganishwa kwa mafanikio.",
        'merge_success_message': "PDF {0} zimeunganishwa kwa mafanikio.\n\nHati mpya sasa ina kurasa {1}.\n\nFaili mpya:\n{2}\n\nMahali pa kuhifadhi:\n{3}\n{2}\n\nJe, unataka kufungua PDF hii?",
        'replace_file_title': "Badilisha faili?",
        'replace_file_message': "PDF tayari imefunguliwa. Je, unataka kuibadilisha na faili mpya?",
        'btn_yes': "Ndiyo",
        'btn_no': "Hapana",
        'filename_merge_suffix': "iliyounganishwa",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Inafungua {0}...",
        'progress_merge_reading': "Inasoma {0}...",
        'progress_merge_adding': "Inaongeza kurasa {0}...",
        'progress_merge_optimizing': "Inaboresha PDF...",
        'progress_merge_writing': "Inaandika PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "kufunga PDF",
        'action_close_window': "kufunga dirisha",
        'action_open_new_pdf': "kufungua PDF mpya",
        'action_quit_app': "kuondoka kwenye programu",
        'changes_saved': "Mabadiliko yamehifadhiwa.",
        'file_close_title': "Funga faili ya PDF",
        'save_before_action': "Je, mabadiliko yahifadhiwe kabla ya {0}? Ndiyo au Hapana?",
        'save_before_action_voice': "Je, mabadiliko yahifadhiwe kabla ya {0}? Ndiyo au Hapana?",
        'save_before_close_question': "Je, mabadiliko yahifadhiwe kabla ya kufunga? Ndiyo au Hapana?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF inayotafutwa imeundwa:\n\n{0}\n\n<b>jaribu tena ikiwa ni lazima",
        "ocr_rotate_title": "Panga kurasa kabla ya OCR",
        "ocr_rotate_question": "PDF ina kurasa zilizozungushwa.\nJe, unataka kupanga kurasa zote hadi 0° kabla ya OCR?\nHii inaboresha utambuzi wa maandishi kwa kiasi kikubwa.",
        "ocr_rotate_yes": "Ndiyo, panga",
        "ocr_rotate_no": "Hapana, anza OCR moja kwa moja",
        "ocr_rotate_voice": "PDF ina kurasa zilizozungushwa. Je, kurasa zote zipangwe kabla ya OCR?",
        "ocr_not_performed_message": "Hakuna maandishi. Tafadhali fanya OCR (menyu \"Hariri\" → \"Fanya OCR\" au kitufe Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Mipangilio ya OCR",
        "ocr_language_btn": "Chagua lugha ya OCR",
        "ocr_language": "Lugha ya OCR",
        "ocr_language_current": "Lugha ya sasa:",
        "ocr_param_info": "Habari kuhusu kigezo",

        "ocr_force_ocr_label": "Lazimisha OCR",
        "ocr_deskew_label": "Sahihisha mwinuko",
        "ocr_clean_label": "Safisha picha",
        "ocr_oversample_label": "Uwazi (DPI)",
        "ocr_pagesegmode_label": "Mgawanyiko wa ukurasa",
        "ocr_oem_label": "Hali ya injini ya OCR",
        "ocr_optimize_label": "Mbano wa PDF",
        "ocr_jobs_label": "Michakato sambamba",
        "ocr_verbose_label": "Ufungamano wa kumbukumbu",

        "ocr_force_ocr_tooltip": "Lazimisha OCR kwenye kila ukurasa, hata kama maandishi yapo tayari",
        "ocr_deskew_tooltip": "Panga skeni zilizoinama kiotomatiki",
        "ocr_clean_tooltip": "Ondoa kelele na visakale kutoka kwenye picha",
        "ocr_oversample_tooltip": "Panua picha kabla ya OCR hadi DPI hii",
        "ocr_pagesegmode_tooltip": "Huamua jinsi ukurasa unavyogawanywa katika maeneo ya maandishi",
        "ocr_oem_tooltip": "Huchagua injini ya OCR ya Tesseract",
        "ocr_optimize_tooltip": "Kiwango cha mbano wa PDF ya pato",
        "ocr_jobs_tooltip": "Idadi ya michakato sambamba ya OCR",
        "ocr_verbose_tooltip": "Kiwango cha ufungamano wa pato la kumbukumbu",
        "ocr_settings_explain_btn": "Maelezo",

        "ocr_force_ocr_explain": "Hulazimisha utambuzi wa maandishi kwenye <b>kila</b> ukurasa, hata kama tayari una maandishi.\n\nPendekezo: <b>Washa</b> kwa PDF zilizoskenwa, <b>Zima</b> kwa PDF asili zilizo na maandishi tayari.",

        "ocr_deskew_explain": "Husahihisha skeni zilizoinama kidogo (hadi takriban 5°).\n\nPendekezo: <b>Washa</b> kwa hati zilizoskenwa, <b>Zima</b> ikiwa kurasa tayari ziko sawa kabisa.",

        "ocr_clean_explain": "Huondoa kelele, vitone na visakale vidogo kutoka kwenye picha.\n<b>MUHIMU:</b> Kwa maandishi ya Kiarabu, Kithai au Kivietnamu yenye alama za diakritiki (vitone juu/chini ya herufi) chaguo hili linapaswa <b>kuzimwa</b>, vinginevyo herufi muhimu zinaweza kupotea.",

        "ocr_oversample_explain": "Huipanua picha <b>kabla</b> ya utambuzi wa maandishi hadi DPI iliyobainishwa.<br><br>• <b>72-150 DPI:</b> Ni haraka sana, lakini kiwango cha chini cha utambuzi<br>• <b>200-300 DPI:</b> Masafa bora (Chaguo-msingi: 300)<br>• <b>400+ DPI:</b> Utambuzi bora kidogo tu, lakini faili kubwa zaidi<br><br>Pendekezo: 300 DPI kwa maandishi changamano (Kiarabu, Kichina, Kijapani), 200 DPI kwa lugha za Magharibi.",

        "ocr_pagesegmode_explain": "Huamua jinsi Tesseract inavyogawanya ukurasa katika maeneo ya maandishi.\n\n• <b>3 - Kiotomatiki (Chaguo-msingi):</b> Nzuri kwa mipangilio mchanganyiko\n• <b>4 - Safu moja:</b> Kwa maandishi ya safu moja\n• <b>5 - Kizuizi wima:</b> Kwa maandishi wima (Kijapani, Kichina)\n• <b>6 - Kizuizi cha maandishi chenye umbo moja:</b> Bora kwa maandishi ya mtiririko bila safu\n• <b>11 - Picha ghafi:</b> Kwa skeni mbaya / maandishi ya mkono\n\nPendekezo: <b>6</b> kwa hati rahisi za maandishi, <b>3</b> kwa mipangilio changamano.",

        "ocr_oem_explain": "Huchagua injini ya OCR ya Tesseract.\n\n• <b>0 - Legacy:</b> Injini ya zamani (haraka, lakini si sahihi kiasi)\n• <b>1 - LSTM:</b> Injini ya neva (polepole, lakini sahihi zaidi)\n• <b>2 - Legacy + LSTM:</b> Huunganisha matokeo yote mawili\n• <b>3 - Chaguo-msingi (LSTM inapendekezwa):</b> Chaguo bora kwa hali nyingi\n\nPendekezo: <b>3</b> kwa usahihi wa juu wa utambuzi.",

        "ocr_optimize_explain": "Hubana PDF ya pato.\n\n• <b>0:</b> Hakuna uboreshaji (usindikaji wa haraka zaidi)\n• <b>1:</b> Uboreshaji mwepesi (maelewano mzuri)\n• <b>2:</b> Uboreshaji wa wastani\n• <b>3:</b> Uboreshaji mkali (faili ndogo zaidi, lakini polepole)\n\nPendekezo: <b>1</b> kwa matumizi ya kila siku.",

        "ocr_jobs_explain": "Idadi ya michakato sambamba kwa OCR.\n\n• <b>1:</b> Polepole, lakini matumizi ya chini ya kumbukumbu\n• <b>4-8:</b> Bora kwa wasindikaji wa kisasa wa nyuzi nyingi\n• <b>12+:</b> Usindikaji wa haraka kidogo tu kwa matumizi makubwa ya kumbukumbu\n\nPendekezo: Idadi ya nyuzi za CPU (mfano <b>4</b> kwenye mifumo ya nyuzi 4).",

        "ocr_verbose_explain": "Kiwango cha ufungamano wa pato la kumbukumbu kwenye koni.\n\n• <b>0:</b> Hakuna pato\n• <b>1:</b> Maendeleo na ujumbe wa hali\n• <b>2:</b> Pato la kina\n• <b>3:</b> Pato kamili la utatuzi (pana sana)\n\nPendekezo: <b>1</b> kwa uendeshaji wa kawaida.",

        "ocr_reset_title": "Mipangilio imewekwa upya",
        "ocr_reset_message": "Mipangilio yote ya OCR imewekwa upya kwa viwango vya msingi.",
        "info_tooltip": "Taarifa zaidi kuhusu kigezo hiki",
        "ocr_reset_defaults": "Weka upya kwa msingi",

        "ocr_psm_0": "Kiotomatiki (injini ya Legacy)",
        "ocr_psm_1": "Utambuzi otomatiki wa safu",
        "ocr_psm_3": "Kiotomatiki (Chaguo-msingi)",
        "ocr_psm_4": "Safu moja",
        "ocr_psm_5": "Kizuizi wima",
        "ocr_psm_6": "Kizuizi cha maandishi chenye umbo moja",
        "ocr_psm_7": "Mstari mmoja wa maandishi",
        "ocr_psm_8": "Neno moja",
        "ocr_psm_11": "Picha ghafi (hakuna uchambuzi wa mpangilio)",

        "ocr_oem_0": "Injini ya Legacy (haraka)",
        "ocr_oem_1": "Injini ya LSTM (neva, sahihi)",
        "ocr_oem_2": "Legacy + LSTM kwa pamoja",
        "ocr_oem_3": "Chaguo-msingi (LSTM inapendekezwa)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Lugha ya OCR...",
        "ocr_language_title": "Chagua lugha ya OCR",
        "ocr_language_instruction": "Chagua lugha kwa ajili ya utambuzi wa maandishi (OCR).\nTahadhari: Lugha nyingi huchukua utendaji na usahihi!\nUnapata matokeo bora ikiwa utachagua lugha moja tu.",
        "ocr_language_predefined": "Michanganyiko iliyobainishwa awali",
        "ocr_language_custom": "Maalum...",
        "ocr_language_selected": "Lugha za OCR zilizochaguliwa",
        "ocr_language_changed": "Lugha ya OCR imebadilishwa kuwa {0}",
        "ocr_language_auto_detect": "Lugha zinazopatikana hutambuliwa kiotomatiki.",
        "ocr_language_none_found": "Hakuna data ya lugha ya Tesseract iliyopatikana! Tafadhali sakinisha vifurushi vya lugha (mfano 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Uchaguzi wa lugha maalum",
        "ocr_language_available": "Lugha zinazopatikana (zilizosakinishwa):",
        "ocr_language_select_hint": "Chagua lugha moja au zaidi:",
        "ocr_language_confirm": "Weka",
        "ocr_language_reset": "Weka upya kwa msingi (deu+eng+vie)",
        "ocr_language_priorities": "Lugha zilizopendekezwa (zilizosakinishwa awali):",

        "select_all_languages": "Chagua zote",
        "clear_all_languages": "Futa uteuzi",
        "install_language_packs": "Sakinisha vifurushi vya lugha vilivyokosekana...",
        "install_hint": "💡 Kidokezo: Sio lugha zote zilizosakinishwa kwenye mfumo wako. Kupitia kitufe hiki utapata usaidizi wa usakinishaji.",
        "ocr_language_install_title": "Usakinishaji wa vifurushi vya lugha vya Tesseract",

        "ocr_missing_languages": "Vifurushi vya lugha vya OCR vilivyokosekana",
        "ocr_missing_languages_message": "Lugha zifuatazo zilizochaguliwa hazijasakinishwa kwenye mfumo wako:\n\n{0}\n\nTafadhali sakinisha vifurushi vya lugha vilivyokosekana (angalia usaidizi chini ya 'Usaidizi wa usakinishaji').\n\nJe, unataka kufungua usaidizi wa usakinishaji sasa?",
        "ocr_missing_languages_voice": "Vifurushi vya lugha vilivyokosekana. Tafadhali sakinisha lugha zilizokosekana.",
        "ocr_install_help_now": "Fungua usaidizi",
        "ocr_continue_anyway": "Jaribu hata hivyo",
        "ocr_language_error_title": "Hitilafu ya lugha ya OCR",
        "ocr_language_error_message": "Hitilafu wakati wa utambuzi wa maandishi: {0}\n\nTafadhali angalia mipangilio yako ya lugha ya OCR (Mipangilio → Lugha ya OCR).",
        "ocr_install_help_button": "Usaidizi wa usakinishaji",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Sakinisha vifurushi vya lugha vya Tesseract</p>

        <p>Ili OCR ifanye kazi katika lugha maalum, data ya lugha inayolingana lazima isakinishwe kwenye mfumo wako. Fuata maagizo kwa mfumo wako wa uendeshaji:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Fungua <strong>Terminal</strong> (Finder → Programu → Zana → Terminal).</li>
        <li>Sakinisha lugha zote zinazopatikana kwa:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Hii inaweza kuchukua dakika chache.)</li>
        <li>Au lugha za kibinafsi tu (mfano Kivietnamu):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Kwa matoleo ya sasa ya Homebrew, <code>*.traineddata</code> inaweza kuhitaji kupakuliwa kwa mkono (tazama hapa chini).</li>
        <li>Baada ya usakinishaji: Funga kisanduku hiki cha mazungumzo na ufungue tena uteuzi wa lugha ya OCR – lugha mpya zitaonekana kiotomatiki.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Fungua terminal (Ctrl+Alt+T).</li>
        <li>Sakinisha lugha unayotaka, mfano kwa Kivietnamu:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
>Misimbo muhimu ya lugha: <code>deu</code> (Kijerumani), <code>eng</code> (Kiingereza), <code>vie</code> (Kivietnamu), <code>spa</code> (Kihispania), <code>fra</code> (Kifaransa), <code>ita</code> (Kiitaliano), <code>nld</code> (Kiholanzi), <code>fin</code> (Kifinlandi), <code>swe</code> (Kiswidi), <code>nor</code> (Kinorwe).</li>
        <li>Onyesha vifurushi vyote vinavyopatikana:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (kwa mkono)</p>
        <ol>
        <li>Pakua faili za <code>*.traineddata</code> unazotaka kutoka:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (mfano <code>vie.traineddata</code> kwa Kivietnamu).</li>
        <li>Nakili faili kwenye folda ya lugha ya Tesseract, kwa kawaida:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Rekebisha kulingana na usakinishaji wa mtu binafsi.)</li>
        <li>Anzisha upya programu (au fungua tena uteuzi wa lugha ya OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Njia mbadala kwa mifumo yote</p>
        <ul>
        <li>Sakinisha <strong>OCRmyPDF</strong> na <strong>Tesseract</strong> kwa kidhibiti cha vifurushi cha chaguo lako. Usakinishaji mwingi tayari una lugha kadhaa za kawaida (Kiingereza, Kijerumani, Kifaransa).</li>
        <li>Lugha zilizokosekana zinaweza kusakinishwa wakati wowote – uteuzi wa lugha ya OCR huorodhesha lugha zilizopo tu.</li>
        </ul>

        <hr>
        <p><b>✅ Baada ya usakinishaji:</b> Hakuna haja ya kuanzisha upya programu – lugha mpya zilizoongezwa zitaonekana mara moja kwenye orodha.</p>
        <p><b>📖 Usaidizi wa misimbo ya lugha:</b> Orodha kamili inapatikana kwenye <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">nyaraka za Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Fonti za Noto Sans",
        "info_noto_font_voice": "Mwongozo wa usakinishaji wa fonti za Noto Sans",
        "btn_info_noto_font_install": "Taarifa za fonti",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Jinsi ya kusakinisha fonti za Noto za bure kutoka Google</h2>

        <p><strong>Fonti za Noto</strong> ni familia ya fonti za chanzo huria kutoka Google. Lengo lao ni kutoona <em>"tofu"</em> (yaani hakuna masanduku tupu □) na kuonyesha kila herufi kutoka kwa kiwango cha Unicode kwa usahihi. Ni nyongeza bora kwa programu zinazohitaji kuonyesha maandishi katika lugha nyingi tofauti.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Usakinishaji kwenye macOS</h3>

        <p><strong>Njia ya 1: Kwa Homebrew (kwa watumiaji wa hali ya juu)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Njia ya 2: Kupitia "Font Book" (Inapendekezwa)</strong></p>

        <ol>
        <li>Pakua kifurushi rasmi cha fonti:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Toa faili ya ZIP</li>
        <li>Nakili faili kwenye <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Usakinishaji kwenye Windows (10 & 11)</h3>

        <p><strong>Njia ya 1: Microsoft Store (Inapendekezwa)</strong><br>
        Tafuta "Google Noto Fonts" au "Noto Sans" na ubofye <strong>Sakinisha</strong>.</p>

        <p><strong>Njia ya 2: Usakinishaji kwa mkono</strong></p>

        <ol>
        <li>Pakua:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Toa ZIP</li>
        <li>Chagua faili za .ttf / .otf</li>
        <li>Bofya kwa kitufe cha kulia → <strong>Sakinisha</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        au<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Jina\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Usakinishaji kwenye Linux</h3>

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

        <p>Uthibitisho:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Dhibiti vialamsho",
        "bookmark_add": "Ongeza kialamsho",
        "bookmark_add_tooltip": "Hifadhi ukurasa wa sasa kama kialamsho",
        "bookmark_remove": "Ondoa kialamsho",
        "bookmark_remove_tooltip": "Futa kialamsho kilichowekwa alama",
        "bookmark_remove_all": "Ondoa zote",
        "bookmark_remove_all_tooltip": "Futa vialamsho vyote vya PDF hii",
        "bookmark_jump": "Ruka hadi kialamsho",
        "bookmark_jump_tooltip": "Ruka hadi ukurasa uliochaguliwa",
        "bookmark_name": "Jina",
        "bookmark_page": "Ukurasa",
        "bookmark_no_bookmarks": "Hakuna vialamsho.\nBofya 'Ongeza' ili kuhifadhi ukurasa wa sasa kama kialamsho.",
        "bookmark_added": "Kialamsho kwa ukurasa {0} kimeongezwa: {1}",
        "bookmark_removed": "Kialamsho kimeondolewa: {0}",
        "bookmark_all_removed": "Vialamsho vyote vimeondolewa.",
        "bookmark_name_default": "Ukurasa {0}",
        "bookmark_name_prompt": "Jina la kialamsho:\n(maandishi marefu yatafupishwa hadi herufi 50)",
        "bookmark_name_prompt_title": "Jina la kialamsho",
        "bookmark_confirm_remove_all": "Je, una uhakika unataka kuondoa vialamsho vyote {0}?",
        "menu_bookmarks": "Vialamsho",
        "bookmark_manage": "Dhibiti vialamsho",
        "bookmark_next": "Kialamsho kinachofuata",
        "bookmark_prev": "Kialamsho kilichopita",
        "bookmark_page_display": "Ukurasa {0}",
        "bookmark_exists": "Kialamsho cha ukurasa huu kwa jina hili tayari lipo.",
        "bookmark_select_first": "Tafadhali chagua kialamsho kwanza.",
        "bookmark_confirm_remove": "Je, una uhakika unataka kuondoa kialamsho 'Ukurasa {0}: {1}'?",
        "bookmark_jumped_to": "Imeruka hadi kialamsho '{0}' kwenye ukurasa {1}.",
        "bookmark_jumped_to_voice": "Kialamsho {0}, ukurasa {1}",
        "btn_close": "Funga",

        "bookmark_list": "Vialamsho vyako",
        "bookmark_rename": "Badilisha jina la kialamsho",
        "bookmark_rename_tooltip": "Badilisha jina la kialamsho kilichochaguliwa",
        "bookmark_rename_title": "Badilisha jina la kialamsho",
        "bookmark_rename_prompt": "Jina jipya la kialamsho kwenye ukurasa {0}:\n(herufi 50 kiwango cha juu)",
        "bookmark_renamed": "Kialamsho '{0}' kimebadilishwa jina kuwa '{1}'.",
        "bookmark_item_tooltip": "Ukurasa {0}: {1}\nBofya mara mbili ili kuruka",
        "bookmark_name_exists_question": "Kialamsho kwa jina '{0}' tayari lipo kwenye ukurasa huu.\nBado ubadilishe jina?",

        "context_bookmarks": "Vialamsho",
        "context_bookmark_add_here": "Ongeza kialamsho kwa ukurasa huu",
        "context_bookmarks_existing": "Vialamsho vilivyopo:",
        "context_bookmarks_jump": "Ruka hadi kialamsho:",
        "context_bookmarks_none": "Hakuna vialamsho",
        "context_bookmarks_clear_all": "Ondoa vialamsho vyote {0}",

        "bookmark_search_placeholder": "Tafuta vialamsho... (jina au ukurasa)",
        "bookmark_search_results": "%d vialamsho vimepatikana kwa \"%s\"",
        "bookmark_no_search_results": "Hakuna vialamsho vilivyopatikana kwa \"%s\"",
        "bookmark_no_search_results_label": "Hakuna matokeo kwa \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Hariri metadata za PDF",
        "metadata_title": "Kichwa",
        "metadata_title_placeholder": "Kichwa cha hati",
        "metadata_title_tooltip": "Kichwa cha hati (kinaonyeshwa kwenye upau wa kichwa)",
        "metadata_author": "Mwandishi",
        "metadata_author_placeholder": "Jina la mwandishi",
        "metadata_author_tooltip": "Muundaji wa hati",
        "metadata_subject": "Mada",
        "metadata_subject_placeholder": "Mada ya hati",
        "metadata_subject_tooltip": "Maelezo mafupi ya maudhui",
        "metadata_keywords": "Maneno muhimu",
        "metadata_keywords_placeholder": "Maneno muhimu, yaliyotengwa na koma",
        "metadata_keywords_tooltip": "Maneno muhimu kwa ajili ya kuainisha hati",
        "metadata_creator": "Muundaji",
        "metadata_creator_placeholder": "Programu iliyoumba PDF",
        "metadata_creator_tooltip": "Programu ambayo hati iliundwa nayo",
        "metadata_producer": "Mtayarishaji",
        "metadata_producer_placeholder": "Programu iliyobadilisha PDF",
        "metadata_producer_tooltip": "Programu iliyobadilisha PDF",
        "metadata_creation_date": "Tarehe ya uumbaji",
        "metadata_creation_date_tooltip": "Tarehe ya uumbaji wa hati",
        "metadata_mod_date": "Tarehe ya marekebisho",
        "metadata_mod_date_tooltip": "Tarehe ya marekebisho ya mwisho",
        "metadata_pdf_info": "📄 Taarifa za PDF",
        "metadata_pages": "Idadi ya kurasa",
        "metadata_file_size": "Ukubwa wa faili",
        "metadata_pdf_version": "Toleo la PDF",
        "metadata_encrypted": "Imechomewa",
        "metadata_encrypted_yes": "Ndiyo (inalindwa na nenosiri)",
        "metadata_encrypted_no": "Hapana",
        "metadata_reload": "📂 Pakia upya kutoka PDF",
        "metadata_reset": "Tupa mabadiliko",
        "metadata_reloaded": "Metadata zimepakuliwa upya kutoka kwenye PDF.",
        "metadata_reset_done": "Sehemu zote za metadata zimewekwa upya.",
        "metadata_no_file": "Hakuna faili ya PDF iliyopakiwa.",
        "metadata_save_error": "Hitilafu wakati wa kuhifadhi metadata",
        "metadata_saved": "Metadata zimehifadhiwa kwa mafanikio.",
        "metadata_pdf_version_unknown": "PDF (isiyojulikana)",
        "metadata_saved_message": "Metadata zimehifadhiwa kwa mafanikio.",
        "metadata_saved_voice": "Metadata zimehifadhiwa.",

        "metadata_custom": "🔧 Metadata maalum",
        "metadata_custom_placeholder": "{\n  \"uwanja_wangu\": \"thamani_yangu\",\n  \"uwanja_mwingine\": 123\n}",
        "metadata_custom_tooltip": "Umbo la JSON kwa metadata maalum (si lazima)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Kiolezo \"{0}\" kimechaguliwa - Bofya mara mbili ili kuingiza",
        "text_use_template": "Tumia kizuizi cha maandishi",
        "text_type": "Aina",
        "text_search_templates": "Tafuta vizuizi vya maandishi...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Taarifa za Utoaji / Uingizaji",
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

        <h3>📦 Nini kinachotolewa? (Muhtasari)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Mipangilio ya jumla ya programu</span></li>
            <li class="detail">• Hali ya Giza/Nuru</li>
            <li class="detail">• Ugeuzaji wa hali ya giza kwa picha</li>
            <li class="detail">• Thamani ya kizingiti cha kijivu</li>
            <li class="detail">• Lugha</li>
            <li class="detail">• Jiometri ya dirisha</li>
            <li class="detail">• Hali ya kukunja</li>
            <li class="detail">• Urambazaji (Upau wa urambazaji unaonekana)</li>
            <li class="detail">• Pato la sauti (imewashwa/imezimwa)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Mipangilio ya chelezo</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Upevaji wa faili (Muhuri wa muda, Kitenganishi, Viambishi tamati)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Mipangilio ya uwekaji wa</span></li>
            <li class="detail">• Sahihi</li>
            <li class="detail">• Maandishi na vizuizi vya maandishi</li>
            <li class="detail">• Alama za vema, picha na maumbo</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Mipangilio ya OCR</span></li>
            <li class="detail">• Lugha</li>
            <li class="detail">• Lazimisha OCR · Hali ya ukurasa</li>
            <li class="detail">• Uchakataji wa awali wa picha: Sahihisha mwinuko, Safisha, Uwekaji sampuli zaidi</li>
            <li class="detail">• Idadi ya kazi sambamba</li>
            <li class="detail">• Hali ya ugeuzaji</li>
            <li class="detail">• Thamani ya kizingiti cha kijivu</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Vialamsho</span></li>
            <li class="detail">• Vialamsho vyote kwa faili ya PDF (Ukurasa, Jina, Muda wa uumbaji)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Hifadhidata ya nywila</span></li>
            <li class="detail">• Nywila za PDF zilizohifadhiwa (zilizochomewa au maandishi wazi kwa hiari)</li>
            <li class="detail">• Hashi ya nywila kuu (ikiwa imewekwa)</li>
            <li class="detail">• Data ya uthibitishaji</li>
        </ul>

        <h4>⚠️ Maelezo muhimu</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Wakati wa kuingiza:</strong>
            <ul>
                <li><span class="warning">➜ Mipangilio YOTE ya sasa itabatilishwa kabisa</span></li>
                <li>• Kuwasha upya programu ni lazima</li>
                <li>• Sahihi, vizuizi vya maandishi na vialamsho vilivyopo vitabadilishwa</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Nenosiri kuu na hali ya utoaji:</strong>
            <ul>
                <li>• Nenosiri kuu linapokuwa hai, unaweza kuchagua:</li>
                <li>  - <span style="color: #98FB98;"><strong>Iliyofumbuliwa</strong></span> (nywila ziko katika maandishi wazi kwenye ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Iliyochomewa</strong></span> (inasomeka tu kwa nenosiri kuu kwenye mfumo lengwa)</li>
                <li>• Hashi ya nenosiri kuu <strong>daima</strong> huhifadhiwa kwa njia iliyochomewa</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Taarifa ya usalama:</strong>
            <ul>
                <li>• Faili ya ZIP iliyotolewa ina data nyeti (<strong>nywila, vialamsho, sahihi</strong>)</li>
                <li>• Tafadhali ihifadhi mahali salama (mfano: kidude cha USB kilichochomewa, kidhibiti nywila)</li>
                <li>• Ikiwa faili itapotea, nywila za PDF zilizohifadhiwa zitapotea kwa kudumu</li>
            </ul>
        </div>

        <h4>📁 Fomati ya utoaji</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Mipangilio huhifadhiwa kwenye faili moja ya ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP hii ina <code>settings.json</code> kamili (kutoka kwa usanidi wako) pamoja na faili za picha za sahihi zilizopachikwa na nywila zilizochomewa.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Sahihi - Mwongozo",
        'signature_guide_html': """
        📝 <strong>Sahihi - Mwongozo wa haraka</strong><br>
        <ul>
        <li>Weka nenosiri kuu</li>
        <li>Sanidi sahihi kwenye menyu ya <em>Mipangilio</em> (ukubwa, muhuri wa wakati, …)</li>
        <li>Ingiza kwa <strong>BONYEZA KULIA</strong> kwenye nafasi inayotakiwa (nenosiri kuu linahitajika mara moja kwa kikao)</li>
        <li>Hamisha sahihi kwa kipanya au vitufe vya mishale</li>
        <li>Ingiza sahihi nyingi mfululizo</li>
        <li>Binafsisha kila sahihi kivyake</li>
        <li>Tupa sahihi moja</li>
        <li>Hifadhi / tupa sahihi zote mara moja</li>
        <li>Vinginevyo, upau wa menyu unaweza pia kutumika.</li>
        </ul>
        """,
        'signature_guide_voice': "Mwongozo wa haraka wa sahihi. Weka nenosiri kuu. Sanidi sahihi kwenye mipangilio. Ingiza kwa kubonyeza kulia.",

        'image_guide_title': "Kuingiza picha - Mwongozo",
        'image_guide_html': """
        📷 <strong>Kuingiza picha kwenye PDF - Mwongozo wa haraka</strong><br>
        <ol>
        <li>Bonyeza kulia kwenye nafasi inayotakiwa</li>
        <li><em>„Ingiza picha“</em> → Chagua picha</li>
        <li>Weka picha: Buruta kwa kipanya</li>
        <li>Rekebisha ukubwa: Buruta kwenye pembe/kingo</li>
        <li>Dumisha uwiano wa vipimo: Kitufe <strong>[A]</strong></li>
        <li>Marekebisho zaidi: Bonyeza kulia kwenye picha</li>
        </ol>
        <p><strong>Kidokezo:</strong> Kwenye menyu ya muktadha unaweza kurekebisha mipangilio.</p>
        """,
        'image_guide_voice': "Mwongozo wa haraka wa picha. Bonyeza kulia, ingiza picha, chagua. Weka kwa kipanya, rekebisha ukubwa kwenye pembe. Uwiano wa vipimo kwa kitufe A.",

        'form_guide_title': "Kuingiza maumbo - Mwongozo",
        'form_guide_html': """
        📐 <strong>Kuingiza maumbo kwenye PDF - Mwongozo wa haraka</strong><br>
        <ol>
        <li>Chagua aina ya umbo (mstatili, duaradufu, mstari, mshale)</li>
        <li>Bonyeza kwenye nafasi:
            <ul>
            <li>Kwa mstatili/duaradufu: Bonyeza moja linaweka umbo</li>
            <li>Kwa mstari/mshale: Bonyeza mbili kwa sehemu ya kuanzia na mwisho</li>
            </ul>
        </li>
        <li>Weka umbo: Buruta kwa kipanya</li>
        <li>Rekebisha ukubwa: Buruta kwenye pembe/kingo</li>
        <li>Hifadhi umbo: <strong>Enter</strong></li>
        <li>Tupa umbo: <strong>ESC</strong></li>
        <li>Marekebisho zaidi: Bonyeza kulia kwenye umbo</li>
        </ol>
        <p><strong>Kidokezo:</strong> Kwenye menyu ya muktadha unaweza kurekebisha mipangilio.</p>
        """,
        'form_guide_voice': "Mwongozo wa haraka wa maumbo. Chagua aina ya umbo. Kwa mstatili au duaradufu bonyeza mara moja, kwa mstari au mshale mara mbili. Weka kwa kipanya, rekebisha ukubwa kwenye pembe. Hifadhi kwa Enter, tupa kwa Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "uliopita",
        "btn_next_result": "ujao",
        "ocr_text_window": "Dirisha la maandishi ya OCR",
        "bookmark_existing": "Alamati zilizopo",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Ulinganisho wa OCR Mac - Windows",
        'ocr_method_mac_win_title': "Tofauti za OCR kati ya Mac na Windows",
        'ocr_method_mac_win_voice': "Mac ni bora",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Tofauti kati ya macOS na Windows</strong></p>

        <p><strong>macOS (inapendekezwa)</strong></p>
        <p>Kifaa:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Matokeo:</p>
        <ul>
        <li>PDF inayotafutwa yenye maandishi yaliyopachikwa ambayo kwa kiasi kikubwa huhifadhi mpangilio asili.</li>
        </ul>
        <p>Faida:</p>
        <ul>
        <li>Ubora bora wa utambuzi wa maandishi (hata kwenye kurasa zilizoinama).</li>
        <li>Uhifadhi wa picha za vekta na fonti.</li>
        <li>Upau wa maendeleo wa GUI kupitia tathmini ya mchakato mdogo.</li>
        <li>Udhibiti kamili juu ya vigezo vyote vya OCR (Deskew, Clean, Oversample, uboreshaji).</li>
        <li>Utafutaji wa maandishi unapatikana moja kwa moja kwenye dirisha kuu (mwonekano wa PDF).</li>
        </ul>
        <p>Hasara:</p>
        <ul>
        <li>Inahitaji zana za mfumo za ziada (ocrmypdf, Ghostscript, unpaper, pngquant – zilizojumuishwa kwenye kifurushi cha programu).</li>
        <li>Ushughulikiaji wa makosa changamano zaidi (deadlocks, muda uliopita).</li>
        </ul>

        <p><strong>Windows (mfumo mbadala thabiti)</strong></p>
        <p>Kifaa:</p>
        <ul>
        <li>pytesseract (muunganisho wa moja kwa moja kwa Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Matokeo:</p>
        <ul>
        <li>PDF inayotafutwa ambayo kwa kuibua inalingana na PDF ya picha, lakini inatafutwa kupitia maandishi ya uwazi.</li>
        </ul>
        <p>Faida:</p>
        <ul>
        <li>Hakuna inayonijia akilini sasa.</li>
        </ul>
        <p>Hasara:</p>
        <ul>
        <li>PDF kimsingi ni picha yenye maandishi yasiyoonekana; mpangilio unaweza kupotoka kidogo kwa hati changamano (safu, majedwali).</li>
        <li>Hakuna urekebishaji wa kuegemea kiotomatiki (--deskew) au usafishaji wa picha (--clean).</li>
        <li>Upau wa maendeleo wa GUI unasasishwa tu kwa makadirio kulingana na idadi ya kurasa zilizochakatwa.</li>
        <li>Kasi ya OCR ni ndogo kidogo (kwa sababu kila ukurasa huchakatwa tofauti).</li>
        <li>Utafutaji wa maandishi huelekezwa upya kwenye dirisha la maandishi ya OCR.</li>
        </ul>

        <p><strong>Sifa za kawaida</strong></p>
        <ul>
        <li>Mbinu zote mbili hutengeneza PDF inayotafutwa kwenye saraka sawa na faili chanzo.</li>
        <li>Mipangilio ya OCR (lugha, DPI, hali ya ugawaji wa ukurasa, hali ya injini ya OCR) inaweza kusanidiwa kupitia OCRSettingsDialog na inatumika katika utekelezaji wote wawili.</li>
        </ul>

        <p><strong>Mapendekezo:</strong></p>
        <ul>
        <li>macOS: Binary ya ocrmypdf inatoa matokeo bora – Nunua Mac na utumie toleo (PDFDarkView kwa Mac zilizo na Apple Silicon au chip ya Intel). Matokeo ya OCR ni bora kuliko Windows!</li>
        <li>Windows: Tumia suluhisho la pytesseract. Ni thabiti na inatoa ubora wa kutosha kabisa kwa hati nyingi.</li>
        </ul>

        <p><strong>Kumbuka muhimu:</strong></p>
        <ul>
        <li>Toleo zote mbili zimeunganishwa kikamilifu katika kiolesura cha mtumiaji – mtumiaji haoni tofauti yoyote.</li>
        <li>Programu huamua kiotomatiki ni injini gani ya OCR kutumia kulingana na mfumo wa uendeshaji.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Unda sahihi (kutoka kwa skana)",
        "signature_create_title": "Chagua sahihi iliyoskana (PDF/picha)",
        "image_pdf_filter": "Picha na PDF",
        "signature_pdf_empty": "PDF haina kurasa.",
        "signature_created_success": "Sahihi imeundwa kwa mafanikio: {0}",
        "signature_create_error": "Hitilafu wakati wa kuunda sahihi:\n{0}",
        "rembg_missing": "rembg haijasakinishwa.\nTafadhali sakinisha: pip install rembg\nHitilafu: {0}",
        "signature_name_title": "Jina la faili kwa sahihi",
        "signature_name_message": "Tafadhali ingiza jina la faili kwa sahihi mpya (itahifadhiwa kama PNG yenye mandharinyuma ya uwazi):",
        "signature_name_label": "Jina la faili:",
        "signature_name_voice": "Ingiza jina la faili kwa sahihi",
        "signature_processing": "Usindikaji unaendelea...",
        "signature_creation_title": "Inaunda sahihi",
        "signature_overwrite_warning": "Faili '{0}' tayari lipo. Kuandika juu?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Andaa PDF kwa ajili ya sahihi",
        "signature_prepare_instruction":"Tafadhali chagua PDF ambayo kwenye ukurasa mmoja ina sahihi iliyoskana.\n\nKwa utambuzi bora, hakikisha kwamba:\n• Sahihi imeandikwa kwa wino mweusi (kalamu ya mpira au kalamu nyembamba) kwenye karatasi nyeupe.\n• Sahihi iko katika theluthi ya juu ya ukurasa wa A4 ulio wazi.\n• PDF imeskana kwa angalau 300 dpi.\n• Sahihi ni wazi na sio nyembamba sana.\n• Hakuna mifumo ya mandharinyuma au mistari inayosumbua.",
        "signature_prepare_voice":"Tafadhali chagua PDF yenye sahihi iliyoskana. Zingatia ubora mzuri na utofautishaji.",
        "sig_thickness_label":"Unene wa mstari:",
        "sig_thickness_normal":"Kawaida (nyembamba)",
        "sig_thickness_bold":"Nzito (inapendekezwa)",
        "sig_thickness_very_bold":"Nzito sana",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Kuongeza lugha za GUI na OCR - Mwongozo",
        'language_guide_title': "Kuongeza lugha za GUI na OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Pakua faili ya tafsiri unayotaka <code>translations_xy.py</code> kutoka<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        na kuiweka kwenye saraka ifuatayo:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Fungua kivinjari chako cha wavuti.</li>
        <li>Nenda kwa: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Kwenye ukingo wa kulia wa skrini tafuta "Releases" na uchague iliyowekwa alama <strong>"latest"</strong>.</li>
        <li>Kwenye ukurasa unaofuata wa toleo, pakua faili <code>Source Code.zip</code> chini kabisa.</li>
        <li>Fungua faili la ZIP.</li>
        <li>Kwenye folda iliyofunguliwa, tafuta faili zote za lugha unazohitaji, na uzikopie kwenye saraka:<br/>
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
        "menu_watermark":"Ingiza alama ya maji",
        "fullpage_text_watermark_title":"Maandishi kama alama ya maji",
        "fullpage_image_watermark_title":"Picha kama alama ya maji",
        "filename_with_watermark":"_pamoja_na_alama_ya_maji",
        "watermark_text":"Maandishi:",
        "watermark_text_placeholder":"Maandishi yako ya alama ya maji...",
        "watermark_font_family":"Fonti:",
        "watermark_font_size":"Ukubwa wa fonti:",
        "watermark_format":"Uumbizaji:",
        "watermark_bold":"Nzito",
        "watermark_italic":"Mteremko",
        "watermark_color":"Rangi:",
        "watermark_choose_color":"Chagua rangi...",
        "watermark_opacity":"Uzito / Uwazi:",
        "watermark_direction":"Mwelekeo wa kusoma:",
        "watermark_direction_l_r":"Kushoto → Kulia",
        "watermark_direction_bl_tr":"Chini kushoto → Juu kulia",
        "watermark_direction_tl_br":"Juu kushoto → Chini",
        "watermark_direction_b_t":"Chini → Juu",
        "watermark_direction_t_b":"Juu → Chini",
        "watermark_preview":"Picha ya awali:",
        "watermark_preview_sample":"Maandishi ya mfano",
        "watermark_empty_text":"Tafadhali ingiza maandishi.",
        "watermark_applied":"Alama ya maji imetumika kwenye kurasa zote.",
        "watermark_saved":"Alama ya maji imehifadhiwa.",
        "image_scale":"Ukubwa:",
        "image_preview":"Picha ya awali ya picha:",
        "no_image_selected":"Hakuna picha iliyochaguliwa",
        "browse":"Vinjari...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Ufutaji",
        "redact_add_black": "Ufutaji (nyeusi)",
        "redact_add_white": "Ufutaji (nyeupe / futa)",
        "redact_added_black": "Ufutaji mweusi umeongezwa",
        "redact_added_white": "Ufutaji mweupe umeongezwa",
        "redact_apply_all": "Tumia ufutaji wote na uhifadhi",
        "redact_discard_all": "Tupa ufutaji wote",
        "redact_discard": "Tupa ufutaji huu",
        "no_redactions": "Hakuna ufutaji",
        "redact_confirm_title": "Tumia ufutaji kabisa",
        "redact_confirm_message": "Onyo: Maeneo yaliyowekwa alama yatafutwa kabisa (nyeusi au nyeupe).\nNakala ya chelezo itaundwa (ikiwa imewashwa).\n\nEndelea?",
        "redact_apply": "Ndiyo, futa sasa",
        "redact_saved": "{0} ufutaji umetumika na kuhifadhiwa.",
        "redact_saved_voice": "{0} ufutaji umetumika",
        "redact_error": "Hitilafu wakati wa kufuta",
        "filename_redacted":"_imefutwa",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Ingiza nambari za kurasa',
        'page_numbers_format': 'Muundo wa nambari:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Kiarabu)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Kirumi ndogo)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Kirumi kubwa)',
        'page_numbers_format_letter': 'A, B, C ... (Herufi)',
        'page_numbers_format_custom': 'Iliyobinafsishwa',
        'page_numbers_custom_pattern': 'Mfano:',
        'page_numbers_custom_placeholder': 'mfano "Ukurasa {nummer}" au "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Tumia {nummer} kwa nambari ya ukurasa wa sasa na {total} kwa jumla',
        'page_numbers_position': 'Mahali:',
        'page_numbers_pos_tl': 'Juu kushoto',
        'page_numbers_pos_tc': 'Juu katikati',
        'page_numbers_pos_tr': 'Juu kulia',
        'page_numbers_pos_ml': 'Katikati kushoto',
        'page_numbers_pos_mc': 'Katikati',
        'page_numbers_pos_mr': 'Katikati kulia',
        'page_numbers_pos_bl': 'Chini kushoto',
        'page_numbers_pos_bc': 'Chini katikati',
        'page_numbers_pos_br': 'Chini kulia',
        'page_numbers_margins': 'Pembeni:',
        'page_numbers_margin_x': 'Umbali wa mlalo:',
        'page_numbers_margin_y': 'Umbali wa wima:',
        'page_numbers_range': 'Mfululizo wa kurasa:',
        'page_numbers_all_pages': 'Kurasa zote',
        'page_numbers_custom_range': 'Mfululizo uliobinafsishwa',
        'page_numbers_from': 'Kuanzia:',
        'page_numbers_to': 'Hadi:',
        'page_numbers_progress': 'Kuingiza nambari za kurasa...',
        'page_numbers_start': 'Kuanza kuingiza nambari za kurasa...',
        'page_numbers_cancel': 'Kuingiza nambari za kurasa kumeghairiwa',
        'page_numbers_success': 'Nambari za kurasa zimeongezwa.\n\nJe, unataka kufungua PDF mpya?\n\n{0}',
        'page_numbers_complete': 'Nambari za kurasa zimeongezwa',
        'page_numbers_error_format': 'Hitilafu wakati wa kuingiza nambari za kurasa: {0}',
        'page_numbers_content_type': 'Aina ya maudhui:',
        'page_numbers_tab_simple': 'Nambari rahisi',
        'page_numbers_tab_range': 'Ukurasa X kati ya Y',
        'page_numbers_tab_date': 'Tarehe',
        'page_numbers_tab_custom': 'Maandishi huru',
        'page_numbers_range_format': 'Muundo:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Ukurasa {aktuell} kati ya {gesamt}',
        'page_numbers_range_custom': 'Iliyobinafsishwa',
        'page_numbers_range_placeholder': 'mfano "Ukurasa {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Muundo wa tarehe:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Januari 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Iliyobinafsishwa',
        'page_numbers_date_placeholder': 'mfano %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Mahali:',
        'page_numbers_date_before': 'Tarehe kabla ya nambari ya ukurasa',
        'page_numbers_date_after': 'Tarehe baada ya nambari ya ukurasa',
        'page_numbers_date_only': 'Tarehe tu (bila nambari ya ukurasa)',
        'page_numbers_custom_text': 'Maandishi yaliyobinafsishwa:',
        'page_numbers_custom_placeholder_text': 'Tumia {seite} kwa nambari ya ukurasa na {gesamt} kwa jumla\nmfano "Siri - Ukurasa {seite}" au "{seite} kati ya {gesamt}"',
        "filename_with_page_number":"_pamoja_na_nambari_ya_ukurasa",
        "filename_with_page_declaration":"_pamoja_na_tamko_la_ukurasa",
        "filename_with_pagenumber":"_pamoja_na_nambari_ya_ukurasa",
        "filename_with_date":"_pamoja_na_tarehe",
        "filename_with_my_page_declaration":"_pamoja_na_tamko_la_ukurasa_iliyobinafsishwa",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Mabadiliko ambayo hayajahifadhiwa",
        "unsaved_changes_message_darkmode": "Kuna uingizaji ambao haujahifadhiwa.\nJe, unataka kuhifadhi kabla ya kubadili?",
        "save_and_switch": "Hifadhi na badili",
        "discard_and_switch": "Badili sasa",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Hamisha kurasa kama picha',
        'export_images_menu': 'Hamisha kama picha (PNG/JPEG)',
        'export_images_format': 'Muundo wa picha:',
        'export_images_dpi': 'Ubora (DPI):',
        'export_images_quality': 'Ubora wa JPEG:',
        'export_images_range': 'Mfululizo wa kurasa:',
        'export_images_all_pages': 'Kurasa zote',
        'export_images_custom_range': 'Mfululizo uliobinafsishwa',
        'export_images_from': 'Kuanzia:',
        'export_images_to': 'Hadi:',
        'export_images_options': 'Chaguzi:',
        'export_images_single_files': 'Kila ukurasa kama faili tofauti',
        'export_images_subfolder': 'Hamisha kwenye folda ndogo',
        'export_images_subfolder_info': 'Kwenye folda ndogo "jinaPDF_picha"',
        'export_images_same_folder': 'Kwenye folda sawa na PDF',
        'export_images_apply_darkmode': 'Tumia mipangilio ya PDFDarkView (Hali ya giza)',
        'export_images_target_folder': 'Folda lengwa:',
        'export_images_browse': 'Vinjari...',
        'export_images_preview': 'Picha ya awali:',
        'export_images_preview_info': 'Chagua mipangilio kwa uhamishaji',
        'export_images_preview_info_detail': '{0} kurasa kama {1}\nUbora: {2} DPI\nJina la faili: {3}\n{4}',
        'export_images_select_folder': 'Chagua folda lengwa',
        'export_images_start': 'Kuanza uhamishaji wa picha...',
        'export_images_progress': 'Kuhifadhi picha...',
        'export_images_saving': 'Kuhifadhi ukurasa {0} kati ya {1}...',
        'export_images_success': 'Uhamishaji umefanikiwa!\n\nPicha {0} zimehifadhiwa katika:\n{1}',
        'export_images_complete': 'Uhamishaji wa picha umekamilika',
        'export_images_open_folder': '📁 Fungua folda',
        'export_images_cancel': 'Uhamishaji wa picha umeghairiwa',
        'export_images_error_format': 'Hitilafu wakati wa kuhamisha picha: {0}',
        'export_images_pdf2image_missing': 'Maktaba "pdf2image" haijasakinishwa.\n\nTafadhali isakinishe kwa:\npip install pdf2image\n\nKwa Windows unahitaji pia Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Ubadilishaji PDF/A kwa uhifadhi wa muda mrefu',
        'pdfa_menu': 'Ubadilishaji PDF/A (inafaa kwa uhifadhi)',
        'pdfa_info': 'Inabadilisha PDF hadi muundo wa PDF/A.\n\nPDF/A imeundwa mahsusi kwa uhifadhi wa muda mrefu na inahakikisha kwamba hati itaonyeshwa kwa usahihi katika siku zijazo.',
        'pdfa_standard': 'Kiwango cha PDF/A:',
        'pdfa_standard_select': 'Toleo:',
        'pdfa_1': 'PDF/A-1 (rahisi, inaendana kwa upana)',
        'pdfa_2': 'PDF/A-2 (ya kisasa, mbano bora)',
        'pdfa_3': 'PDF/A-3 (toleo la hivi karibuni, inaruhusu viambatisho)',
        'pdfa_standards_explanation': '📖 Maelezo ya viwango:\n\n'
            '• PDF/A-1: Msingi, inaendana na mifumo ya zamani (takriban 2005)\n'
            '• PDF/A-2: Ya kisasa zaidi, mbano bora, usaidizi wa uwazi (takriban 2011)\n'
            '• PDF/A-3: Toleo la hivi karibuni, inaruhusu kupachika viambatisho vya faili (takriban 2013)\n\n'
            'Mapendekezo: PDF/A-2 ni maelewano mazuri kati ya uendanaji na vipengele vya kisasa.',
        'pdfa_options': 'Chaguzi:',
        'pdfa_compress_enable': 'Bana PDF (faili ndogo)',
        'pdfa_metadata_preserve': 'Hifadhi metadata (kichwa, mwandishi, nk.)',
        'pdfa_target_folder': 'Folda lengwa:',
        'pdfa_browse': 'Vinjari...',
        'pdfa_select_folder': 'Chagua folda lengwa',
        'pdfa_ocr_info_unknown': '🔍 Haikuweza kuangalia maudhui ya maandishi.',
        'pdfa_ocr_info_not_needed': '✅ Maandishi yapatikana - OCR haihitajiki.\nPDF/A inaweza kuundwa moja kwa moja.',
        'pdfa_ocr_info_recommended': '⚠️ Hakuna maandishi ya kutosha yaliyopatikana.\n\nKwa PDF zinazoweza kutafutwa, tunapendekeza kuendesha OCR kwanza.\nKumbuka: PDF/A inafanya kazi bila OCR - lakini maandishi hayatatambulika.',
        'pdfa_ocr_info_error': '❌ Hitilafu wakati wa kuangalia: {0}',
        'pdfa_start': 'Kuanza ubadilishaji wa PDF/A...',
        'pdfa_progress': 'Ubadilishaji wa PDF/A unaendelea...',
        'pdfa_success': 'Ubadilishaji wa PDF/A umefanikiwa!\n\nImehifadhiwa kama:\n{0}\n\nJe, unataka kufungua PDF mpya?',
        'pdfa_complete': 'Ubadilishaji wa PDF/A umekamilika',
        'pdfa_cancel': 'Ubadilishaji wa PDF/A umeghairiwa',
        'pdfa_error_format': 'Hitilafu wakati wa ubadilishaji wa PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Maktaba "ocrmypdf" haijasakinishwa.\n\nTafadhali isakinishe kwa:\npip install ocrmypdf',
        'btn_convert': 'Badilisha',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Boresha PDF (punguza saizi ya faili)',
        'optimize_menu': 'Boresha PDF (saizi ya faili)',
        'optimize_info': 'Inapunguza saizi ya faili ya PDF kupitia mbinu mbalimbali za uboreshaji.\n\nKiwango cha juu cha mbano, faili inakuwa ndogo - pamoja na upotezaji unaowezekana wa ubora wa picha.',
        'optimize_level': 'Kiwango cha mbano:',
        'optimize_level_low': 'Chini (haraka, akiba ndogo)',
        'optimize_level_medium': 'Kati (maelewano mazuri)',
        'optimize_level_high': 'Juu (akiba kubwa)',
        'optimize_level_maximum': 'Upeo (akiba ya juu, polepole)',
        'optimize_level_explanation': 'Mapendekezo: "Kati" ni maelewano mazuri kati ya kasi na saizi ya faili.',
        'optimize_options': 'Chaguzi:',
        'optimize_compress_images': 'Bana picha (punguza ubora wa JPEG)',
        'optimize_clean_objects': 'Ondoa vitu visivyotumika',
        'optimize_preserve_metadata': 'Hifadhi metadata (kichwa, mwandishi, nk.)',
        'optimize_image_quality': 'Ubora wa picha:',
        'optimize_range': 'Mfululizo wa kurasa:',
        'optimize_all_pages': 'Kurasa zote',
        'optimize_custom_range': 'Mfululizo uliobinafsishwa',
        'optimize_from': 'Kuanzia:',
        'optimize_to': 'Hadi:',
        'optimize_target_folder': 'Folda lengwa:',
        'optimize_browse': 'Vinjari...',
        'optimize_select_folder': 'Chagua folda lengwa',
        'optimize_info_box': 'Habari',
        'optimize_info_text': 'Uboreshaji unaweza kuchukua dakika kadhaa kwa PDF kubwa.\n\nPicha zinahifadhiwa kwa ubora uliopunguzwa, ambayo inaweza kupunguza saizi ya faili kwa kiasi kikubwa.',
        'optimize_start': 'Kuanza uboreshaji wa PDF...',
        'optimize_progress': 'Kuboresha PDF...',
        'optimize_cancel': 'Uboreshaji wa PDF umeghairiwa',
        'optimize_complete': 'Uboreshaji wa PDF umekamilika',
        'optimize_error_format': 'Hitilafu wakati wa uboreshaji wa PDF:\n\n{0}',
        'optimize_success_message': 'Uboreshaji wa PDF umefanikiwa!\n\nImehifadhiwa kama:\n{0}\n\nKabla: {1}\nBaada: {2}\nAkiba: {3:.1f}%\n\n{4}\n\nJe, unataka kufungua PDF iliyoboreshwa?',
        'optimize_success_message_no_size': 'Uboreshaji wa PDF umefanikiwa!\n\nImehifadhiwa kama:\n{0}\n\nHabari ya saizi haipatikani.\n\nJe, unataka kufungua PDF iliyoboreshwa?',
        'optimize_result_positive': 'Faili imepunguzwa kwa {0:.1f}%.',
        'optimize_result_zero': 'Hakuna mabadiliko katika saizi ya faili.',
        'optimize_result_negative': 'Faili imeongezeka kwa {0:.1f}%.\nUboreshaji umeachwa, faili asili imehifadhiwa.',
        'btn_optimize': 'Anza uboreshaji',
        'filename_optimize_low_suffix': '_iliyoboreshwa_chini',
        'filename_optimize_medium_suffix': '_iliyoboreshwa',
        'filename_optimize_high_suffix': '_iliyoboreshwa_juu',
        'filename_optimize_maximum_suffix': '_iliyoboreshwa_upeo',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Kata PDF',
        'crop_menu': 'Kata PDF (Crop)',
        'crop_range': 'Tumia kwa:',
        'crop_all_pages': 'Kurasa zote',
        'crop_current_page': 'Ukurasa wa sasa tu',
        'crop_values': 'Thamani za kukata (katika pointi):',
        'crop_left': 'Kushoto:',
        'crop_right': 'Kulia:',
        'crop_top': 'Juu:',
        'crop_bottom': 'Chini:',
        'crop_presets': 'Mpangilio wa awali:',
        'crop_preset_white': 'Gundua pembeni nyeupe',
        'crop_reset': 'Weka upya',
        'crop_mouse_hint': '🖱️ Buruta mstatili ili kuchagua eneo kwa makadirio.\nKisha unaweza kurekebisha thamani kwa usahihi katika SpinBox.\nMarekebisho ya mwongozo na panya haiwczekani.',
        'crop_apply': 'Kata',
        'crop_scope_all': 'Kurasa zote',
        'crop_scope_current': 'Ukurasa wa sasa',
        'crop_new_size': 'Ukubwa mpya: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Hakuna PDF iliyopakiwa',
        'crop_preview_error': 'Hitilafu wakati wa kupakia picha ya awali',
        'crop_start': 'Kuanza kukata...',
        'crop_progress': 'Kukata PDF...',
        'crop_success': 'PDF imekatwa!\n\nImehifadhiwa kama:\n{0}\n\nJe, unataka kufungua PDF iliyokatwa?',
        'crop_complete': 'Kukata kumekamilika',
        'crop_cancel': 'Kukata kumeghairiwa',
        'crop_error_format': 'Hitilafu wakati wa kukata:\n\n{0}',
        'filename_crop_suffix': '_iliyokatwa',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Sawazisha PDF (Flatten)',
        'flatten_menu': 'Sawazisha PDF (Flatten)',
        'flatten_info': 'Kusawazisha PDF "kuchoma" vipengele vyote vinavyoweza kuhaririwa kwenye maudhui ya ukurasa.\n\nBaada ya hayo, sehemu za fomu, maelezo, maandishi, misalaba, saini, picha na maumbo hayawezi kuhaririwa kibinafsi tena.',
        'flatten_explanation_title': '📖 Hii ni nzuri kwa nini?',
        'flatten_explanation_text': 'Kusawazisha kunahitajika katika hali zifuatazo:\n\n'
            '• 📄 Unataka kuandaa hati kwa uchapishaji\n'
            '• 🔒 Unataka kuzuia mtu kubadilisha sehemu za fomu\n'
            '• 📎 Unataka "kupachika" maelezo na maoni katika hati\n'
            '• 🖼️ Unataka kuweka maandishi, misalaba, saini, picha na maumbo katika hati\n'
            '• 📦 Unataka kuandaa faili kwa uhifadhi\n\n'
            'Kusawazisha kunafanya PDF kuwa ndogo na kuzuia vipengele kuhamishwa au kufutwa kwa bahati mbaya.',
        'flatten_what_title': 'Nini kinasawazishwa?',
        'flatten_what_list': '• ✅ Sehemu za fomu (sehemu za maandishi, visanduku vya uteuzi, vitufe)\n'
            '• ✅ Maelezo (maoni, mwangaza, maelezo)\n'
            '• ✅ Tabaka za juu (maandishi, misalaba, saini, picha, maumbo)',
        'flatten_options': 'Chaguzi:',
        'flatten_forms': 'Sawazisha sehemu za fomu',
        'flatten_annotations': 'Sawazisha maelezo',
        'flatten_overlays': 'Sawazisha tabaka za juu (maandishi, misalaba, saini, picha, maumbo)',
        'flatten_target_folder': 'Folda lengwa:',
        'flatten_browse': 'Vinjari...',
        'flatten_select_folder': 'Chagua folda lengwa',
        'flatten_warning': '⚠️ Muhimu: Kusawazisha ni mchakato usioweza kutenduliwa!\n\nBaada ya kusawazisha, vipengele vinavyoweza kuhaririwa haviwezi kubadilishwa au kufutwa kibinafsi.\nUnda nakala ya chelezo mapema ikiwa ni lazima.',
        'flatten_apply': 'Sawazisha',
        'flatten_start': 'Kuanza kusawazisha...',
        'flatten_progress': 'Kusawazisha PDF...',
        'flatten_success': 'PDF imesawazishwa!\n\nImehifadhiwa kama:\n{0}\n\nJe, unataka kufungua PDF iliyosawazishwa?',
        'flatten_complete': 'Kusawazisha kumekamilika',
        'flatten_cancel': 'Kusawazisha kumeghairiwa',
        'flatten_error_format': 'Hitilafu wakati wa kusawazisha:\n\n{0}',
        'filename_flatten_suffix': '_imesawazishwa',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Tabaka la juu la PDF (Overlay)',
        'overlay_menu': 'Tabaka la juu la PDF (Overlay)',
        'overlay_info': 'Inaweka PDF moja (tabaka la juu) juu ya PDF nyingine.\n\nPDF ya tabaka la juu inawekwa kwenye PDF ya msingi. Hii ni muhimu kwa alama za maji, nembo, vichwa vya barua au mihuri.',
        'overlay_explanation_title': '📖 Hii ni nzuri kwa nini?',
        'overlay_explanation_text': 'Tabaka la juu linahitajika katika hali zifuatazo:\n\n'
            '• 🏢 Kuweka nembo ya kampuni kama alama ya maji kwenye kila ukurasa\n'
            '• 📄 Kuweka kichwa cha barua kwenye PDF tupu\n'
            '• 🖊️ Kuweka tabaka la juu la muhuri kwenye hati\n'
            '• 🔖 Kuweka alama ya maji kwenye kurasa zote\n'
            '• 📑 Kuweka tabaka la juu la fomu kwenye kiolezo',
        'overlay_type': 'Aina ya tabaka la juu:',
        'overlay_type_fullpage': 'Ukurasa mzima (unaofunika)',
        'overlay_type_transparent': 'Ukurasa mzima (uwazi - inapendekezwa)',
        'overlay_type_stamp': 'Muhuri (unaoweza kuwekwa mahali)',
        'overlay_type_info_fullpage': '📄 PDF ya tabaka la juu inawekwa haswa juu ya ukurasa mzima.\nMandharinyuma meupe yanaweza kuondolewa ili maudhui tu yabaki kuonekana.',
        'overlay_type_info_transparent': '🔍 PDF ya tabaka la juu inawekwa juu ya ukurasa mzima kwa mandharinyuma ya uwazi.\nMandharinyuma meupe huondolewa kiatomati - bora kwa alama za maji na nembo!',
        'overlay_type_info_stamp': '🖊️ PDF ya tabaka la juu inawekwa mahali na kupimwa kama muhuri.\nBora kwa nembo, mihuri au saini katika sehemu mahususi.',
        'overlay_remove_background': 'Ondoa mandharinyuma meupe:',
        'overlay_remove_background_enable': 'Ondoa mandharinyuma meupe kutoka kwa PDF ya tabaka la juu (inafanya tabaka la juu kuwa wazi)',
        'overlay_remove_background_tooltip': 'Inaondoa maeneo meupe kutoka kwa PDF ya tabaka la juu ili maandishi yaliyo chini yaonekane.',
        'overlay_threshold': 'Thamani ya kizingiti:',
        'overlay_threshold_hint': '(1-254, juu = zaidi nyeupe huondolewa)',
        'overlay_select_file': 'Chagua PDF ya tabaka la juu:',
        'overlay_file_placeholder': 'Tafadhali chagua faili ya PDF kwa tabaka la juu',
        'overlay_browse': 'Vinjari...',
        'overlay_select_overlay': 'Chagua PDF ya tabaka la juu',
        'overlay_range': 'Mfululizo wa kurasa:',
        'overlay_all_pages': 'Kurasa zote',
        'overlay_custom_range': 'Mfululizo uliobinafsishwa',
        'overlay_from': 'Kuanzia:',
        'overlay_to': 'Hadi:',
        'overlay_position': 'Mahali:',
        'overlay_position_center': 'Katikati',
        'overlay_position_top_left': 'Juu kushoto',
        'overlay_position_top_right': 'Juu kulia',
        'overlay_position_bottom_left': 'Chini kushoto',
        'overlay_position_bottom_right': 'Chini kulia',
        'overlay_size': 'Ukubwa:',
        'overlay_size_original': 'Ukubwa wa asili',
        'overlay_size_fit_page': 'Lingana na ukurasa',
        'overlay_size_custom': 'Iliyobinafsishwa (%)',
        'overlay_opacity': 'Uwazi:',
        'overlay_target_folder': 'Folda lengwa:',
        'overlay_browse_folder': 'Vinjari...',
        'overlay_select_folder': 'Chagua folda lengwa',
        'overlay_warning': '⚠️ Kumbuka: PDF ya tabaka la juu inawekwa kwenye PDF ya msingi na "kuchomwa" ndani yake.\n\nVipengele vya PDF ya tabaka la juu haziwezi kuhaririwa kibinafsi baada ya kuhifadhi.',
        'overlay_apply': 'Weka tabaka la juu',
        'overlay_start': 'Kuanza kuweka tabaka la juu...',
        'overlay_progress': 'Kuweka tabaka la juu kwenye PDF...',
        'overlay_success': 'PDF imewekewa tabaka la juu!\n\nImehifadhiwa kama:\n{0}\n\nJe, unataka kufungua PDF iliyowekewa tabaka la juu?',
        'overlay_complete': 'Kuweka tabaka la juu kumekamilika',
        'overlay_cancel': 'Kuweka tabaka la juu kumeghairiwa',
        'overlay_error_format': 'Hitilafu wakati wa kuweka tabaka la juu:\n\n{0}',
        'overlay_no_file': 'Hakuna PDF ya tabaka la juu iliyochaguliwa.\n\nTafadhali chagua faili ya PDF kuweka tabaka la juu.',
        'filename_overlay_suffix': '_imewekewa_tabaka_la_juu',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Toa picha kutoka kwa PDF',
        'extract_images_menu': 'Toa picha zote',
        'extract_images_info': 'Inatoa picha zote kutoka kwa PDF na kuzihifadhi kama faili tofauti.\n\nPicha zinahifadhiwa katika muundo wao asili au kubadilishwa hadi muundo uliochaguliwa.',
        'extract_images_format': 'Muundo wa picha:',
        'extract_images_quality': 'Ubora wa JPEG:',
        'extract_images_options': 'Chaguzi:',
        'extract_images_subfolder': 'Toa kwenye folda ndogo ("jinaPDF_picha")',
        'extract_images_unique': 'Picha za kipekee tu (epuka nakala)',
        'extract_images_range': 'Mfululizo wa kurasa:',
        'extract_images_all_pages': 'Kurasa zote',
        'extract_images_custom_range': 'Mfululizo uliobinafsishwa',
        'extract_images_from': 'Kuanzia:',
        'extract_images_to': 'Hadi:',
        'extract_images_target_folder': 'Folda lengwa:',
        'extract_images_browse': 'Vinjari...',
        'extract_images_select_folder': 'Chagua folda lengwa',
        'extract_images_info_box': 'Habari',
        'extract_images_info_text': 'Utoaji unaweza kuchukua dakika kadhaa kwa PDF kubwa.\n\nPicha zinahifadhiwa kwa jina lake asili (ukurasa_picha).',
        'extract_images_extract': 'Toa',
        'extract_images_start': 'Kuanza utoaji...',
        'extract_images_progress': 'Kutoa picha...',
        'extract_images_success': '✅ Picha zimetolewa!\n\nPicha {0} zimehifadhiwa katika:\n{1}',
        'extract_images_complete': 'Utoaji wa picha umekamilika',
        'extract_images_cancel': 'Utoaji umeghairiwa',
        'extract_images_error_format': 'Hitilafu wakati wa kutoa picha:\n\n{0}',
        'extract_images_open_folder': '📁 Fungua folda',
        'extract_images_no_images': 'Hakuna picha zilizopatikana kwenye PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Kurasa nyingi kwenye ukurasa mmoja (N-Up)',
        'nup_menu': 'Kurasa nyingi kwenye ukurasa mmoja (N-Up)',
        'nup_info': 'Inapanga kurasa nyingi za PDF kwenye ukurasa mmoja.\n\nBora kwa uchapishaji wa kompakt, muhtasari au vipeperushi.',
        'nup_layout': 'Mpangilio:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Picha ya awali:',
        'nup_preview_info': '{0} kurasa → {1} kurasa kwa karatasi → {2} karatasi\nMpangilio: {3}',
        'nup_order': 'Mpangilio:',
        'nup_order_horizontal': 'Mlalo (safu kwa safu)',
        'nup_order_vertical': 'Wima (safu wima kwa safu wima)',
        'nup_order_horizontal_reverse': 'Mlalo kinyume',
        'nup_order_vertical_reverse': 'Wima kinyume',
        'nup_range': 'Mfululizo wa kurasa:',
        'nup_all_pages': 'Kurasa zote',
        'nup_custom_range': 'Mfululizo uliobinafsishwa',
        'nup_from': 'Kuanzia:',
        'nup_to': 'Hadi:',
        'nup_options': 'Chaguzi:',
        'nup_margins': 'Pembeni:',
        'nup_margin_between': 'Nafasi kati ya kurasa:',
        'nup_page_numbers': 'Ingiza nambari za kurasa',
        'nup_target_folder': 'Folda lengwa:',
        'nup_browse': 'Vinjari...',
        'nup_select_folder': 'Chagua folda lengwa',
        'nup_create': 'Unda',
        'nup_start': 'Kuanza N-Up...',
        'nup_progress': 'Kuunda N-Up...',
        'nup_success': 'N-Up imeundwa!\n\nImehifadhiwa kama:\n{0}\n\nJe, unataka kufungua PDF mpya?',
        'nup_complete': 'N-Up imekamilika',
        'nup_cancel': 'N-Up imeghairiwa',
        'nup_error_format': 'Hitilafu wakati wa N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Badilisha ukubwa wa ukurasa',
        'pagesize_menu': 'Badilisha ukubwa wa ukurasa',
        'pagesize_info': 'Inabadilisha ukubwa wa ukurasa wa PDF.\n\nMaudhui hulinganishwa kiotomati na ukubwa mpya.',
        'pagesize_format': 'Muundo:',
        'pagesize_select': 'Chagua muundo wa kawaida:',
        'pagesize_custom': 'Ukubwa uliobinafsishwa:',
        'pagesize_width': 'Upana:',
        'pagesize_height': 'Urefu:',
        'pagesize_orientation': 'Mwelekeo:',
        'pagesize_portrait': 'Wima',
        'pagesize_landscape': 'Mlalo',
        'pagesize_scale_options': 'Chaguzi za upimaji:',
        'pagesize_fit': 'Lingana (hifadhi uwiano)',
        'pagesize_stretch': 'Panua (potosha)',
        'pagesize_center': 'Katikati (ukubwa asili)',
        'pagesize_range': 'Mfululizo wa kurasa:',
        'pagesize_all_pages': 'Kurasa zote',
        'pagesize_custom_range': 'Mfululizo uliobinafsishwa',
        'pagesize_from': 'Kuanzia:',
        'pagesize_to': 'Hadi:',
        'pagesize_target_folder': 'Folda lengwa:',
        'pagesize_browse': 'Vinjari...',
        'pagesize_select_folder': 'Chagua folda lengwa',
        'pagesize_apply': 'Tumia',
        'pagesize_start': 'Kuanza kubadilisha ukubwa wa ukurasa...',
        'pagesize_progress': 'Kubadilisha ukubwa wa ukurasa...',
        'pagesize_success': 'Ukubwa wa ukurasa umebadilishwa!\n\nImehifadhiwa kama:\n{0}\n\nJe, unataka kufungua PDF mpya?',
        'pagesize_complete': 'Kubadilisha ukubwa wa ukurasa kumekamilika',
        'pagesize_cancel': 'Kubadilisha ukubwa wa ukurasa kumeghairiwa',
        'pagesize_error_format': 'Hitilafu wakati wa kubadilisha ukubwa wa ukurasa:\n\n{0}',
        'pagesize_preview_info': 'Ukubwa mpya: {0} x {1} pt',
        'filename_pagesize_suffix': '_ukubwa_mpya',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Maelezo ya PDF',
        'pdf_info_menu': 'Onyesha maelezo ya PDF',
        'pdf_info_voice': 'Kuonyesha maelezo ya PDF',
        'pdf_info_error': 'Hitilafu wakati wa kuonyesha maelezo ya PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Onyesha njia za mkato za kibodi",
        "shortcuts_dialog_title": "Njia za mkato za kibodi",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FAILI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Fungua PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Funga PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Hifadhi kama...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Linda hati</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Chapisha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Chapisha mara moja (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Toka kwenye programu</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 HAMISHA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Hamisha kama Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Hamisha kama DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Hamisha kama TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Hamisha kama picha (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Toa picha</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ UCHAKATAJI WA HATI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Kurasa nyingi)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Ubadilishaji PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Sawazisha PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Tabaka la juu la PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Boresha PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ HARIRI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Tafuta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Ongeza alamisho</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Simamia alamisho</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Alamisho inayofuata</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Alamisho iliyotangulia</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Endesha OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 USIMAMIZI WA KURASA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Zungusha ukurasa wa sasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Zungusha kurasa zote</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Sawazisha ukurasa wa sasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Sawazisha kurasa zote</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Futa kurasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Toa kurasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Ingiza kurasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Hamisha kurasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Unganisha PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Badilisha ukubwa wa ukurasa</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INGIZA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Ingiza maandishi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Ingiza msalaba</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Ingiza saini 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Ingiza saini 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Ingiza picha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Ingiza mstatili</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ingiza duaradufu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Ingiza mstari</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Ingiza mshale</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Ingiza nambari za kurasa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Alama ya maji ya maandishi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Alama ya maji ya picha</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ UFUTAJI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Ufutaji (nyeusi)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Ufutaji (nyeupe)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Tumia ufutaji wote</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ Hali ya juu</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Kata PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Hariri metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ TAZAMA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Badilisha hali ya Giza/Nuru</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Onyesha dirisha la maandishi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Upana wa ukurasa (Kukuza)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Kurasa mbili (Kukuza)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Muhtasari (Kukuza)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ MIPANGILIO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Usimamizi wa nywila</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Mipangilio ya OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Mipangilio ya saini</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Uumbizaji wa jina la faili</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Hamisha mipangilio</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Ingiza mipangilio</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ MAELEZO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Onyesha maelezo ya PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Washa/zima matokeo ya sauti</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Lenga kwenye upau wa menyu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Toleo jipya linapatikana",
        "update_available_message": "Kuna toleo jipya <b>{0}</b>.\n\nTembelea ukurasa wa toleo ili kupakua sasisho:\n{1}",
        "update_available_voice": "Toleo jipya {0} linapatikana. Tafadhali pakua sasisho kutoka ukurasa wa GitHub.",
        "update_open_release": "Fungua ukurasa wa toleo",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Pakua tafsiri zote",
        "ask_download_all_translations": """Mbali na Kijerumani, Kiingereza na Kivietinamu, kuna lugha nyingine {total_languages} za GUI zinazopatikana.\n\nJe, zinapaswa kutolewa / kusasishwa?\n\nKumbuka:\nLugha zisizohitajika unaweza kuzifuta baadaye mwenyewe kwenye saraka:\n{translations_path}
        \nUkighairi, unaweza kupakua lugha za GUI baadaye kupitia menyu 'Zana → Sasisha tafsiri'.""",
        "menu_update_translations": "Sasisha tafsiri",
        "translations_updated": "Tafsiri zimesasishwa",
        "translations_update_success": "Tafsiri {} zimesasishwa kwa mafanikio ({} mpya, {} zimesasishwa).",
        "translations_update_error": "Hitilafu wakati wa kusasisha tafsiri",
        "translations_update_no_changes": "Tafsiri zote tayari zimesasishwa.",
        "translations_update_offline": "Hakuna muunganisho wa mtandao. Tafsiri hazikuweza kusasishwa.",
        "translations_update_in_progress": "Tafsiri zinasasishwa nyuma...",
        "translations_downloading": "Inapakua tafsiri...",
        "translations_path_hint": "Saraka ya mtumiaji kwa tafsiri",
        "translations_update_not_available_title": "Sasisho halipatikani",
        "translations_update_not_available_message": """Kusasisha tafsiri kunapatikana tu katika toleo lililosanikwa.\n\nKatika hali ya maendeleo, tafsiri tayari zimesasishwa.""",
        "translations_update_no_internet_title": "Hakuna muunganisho wa mtandao",
        "translations_update_no_internet_message": """Haikuwezekana kuanzisha muunganisho wa mtandao.\n\nTafsiri haziwezi kupakuliwa kutoka GitHub.\n\nSuluhisho zinazowezekana:
        • Angalia muunganisho wako wa mtandao
        • Zima firewall yoyote kwa muda
        • Jaribu tena baadaye
        \nUnaweza pia kupakua tafsiri mwenyewe kutoka GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Sasisho tayari linaendelea",
        "btn_retry": "Jaribu tena",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Karibu kwenye PDF Dark View",
        "welcome_title_not_supported": "Karibu kwenye PDF Dark View",
        "welcome_message": "Karibu kwenye PDF Dark View!\n\nLugha yako ya mfumo ilitambuliwa kama '{language}'.\nJe, ungependa kutumia lugha hii kwa kiolesura cha mtumiaji?\n\nUnaweza kubadilisha lugha wakati wowote kupitia 'Mipangilio → Lugha'.",
        "welcome_message_language_not_available": "Karibu kwenye PDF Dark View!\n\nLugha yako ya mfumo ilitambuliwa kama '{language}'.\nLugha hii bado haijasanikwa.\n\nJe, ungependa kupakua tafsiri za {language} sasa kutoka GitHub?\n\n(Lugha itatumika moja kwa moja kwa kiolesura cha mtumiaji.)",
        "welcome_message_language_not_supported": "Karibu kwenye PDF Dark View!\n\nLugha yako ya mfumo ilitambuliwa kama '{language}'.\nKwa bahati mbaya, hakuna tafsiri za lugha hii bado.\n\nKiolesura cha mtumiaji kitaonyeshwa kwa {fallback_language}.\n\nUnaweza kubadilisha lugha wakati wowote kupitia 'Mipangilio → Lugha'.\nIkiwa unataka, unaweza pia kuchangia tafsiri kwa lugha yako:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Ndio, tumia lugha ya mfumo",
        "welcome_keep_english": "Hapana, weka Kiingereza",
        "welcome_download_language": "Ndio, pakua {language}",

        # ============================================
        # 107. NJIA ZILIZOTUMIWA HIVI KARIBU
        # ============================================

        'menu_recent': 'Zilizotumiwa hivi karibu',
        'menu_recent_dirs': 'Daftari...',
        'menu_recent_files': 'Faili...',
        'recent_manage': 'Simamia...',
        'recent_enable_tracking': 'Hifadhi njia za hivi karibu (faragha)',
        'recent_enable_info': 'Zima chaguo hili ili usihifadhi njia',
        'recent_tracking_disabled': 'Ufuatiliaji wa njia umezimwa',
        'recent_enabled': 'imewashwa',
        'recent_disabled': 'imezimwa',
        'recent_tracking_status': 'Ufuatiliaji wa njia {0}',
        'recent_dialog_title': 'Njia zilizotumiwa hivi karibu',
        'recent_tab_directories': 'Daftari',
        'recent_tab_files': 'Faili',
        'recent_dirs_instruction': 'Bonyeza mara mbili kufungua kidirisha cha faili katika daftari',
        'recent_files_instruction': 'Bonyeza mara mbili kufungua PDF moja kwa moja',
        'recent_no_directories': '(hakuna daftari lililohifadhiwa)',
        'recent_no_files': '(hakuna faili lililohifadhiwa)',
        'recent_default_current': '⭐ Chaguo-msingi: {0}',
        'recent_set_as_default': '⭐ Weka kama chaguo-msingi',
        'recent_default_set_title': 'Daftari chaguo-msingi limewekwa',
        'recent_default_set_message': 'Daftari "{0}" limewekwa kama chaguo-msingi kwa kufungua PDF.',
        'recent_default_set_voice': 'Daftari chaguo-msingi limewekwa',
        'recent_directory_not_found': 'Daftari halipatikani',
        'recent_file_not_found': 'Faili halipatikani',
        'recent_remove_selected': 'Ondoa',
        'recent_remove_title': 'Ondoa njia',
        'recent_remove_confirm': 'Je, una hakika unataka kuondoa njia "{0}" kutoka kwenye orodha?',
        'recent_path_removed': 'Njia imeondolewa',
        'recent_clear_all': 'Ondoa zote',
        'recent_clear_title': 'Ondoa njia zote',
        'recent_clear_confirm_type': 'Je, una hakika unataka kufuta {0} zote?',
        'recent_cleared': 'Orodha imesafishwa',
        'recent_path_not_found_title': 'Njia haipatikani',
        'recent_path_not_found_message': 'Njia "{0}" haipo tena.',
        'recent_open_file': 'Fungua faili',
        'btn_open_recent': 'Fungua',
        'recent_open_file_question': 'Je, unataka kufungua "{0}" kama PDF?',
        'recent_not_pdf': 'Faili lililochaguliwa si PDF.',
        'recent_more_entries': 'Maingizo zaidi...',
        'btn_remove': 'Ondoa',
        'btn_clear': 'Safisha zote',
        'recent_context_open': 'Fungua',
        'recent_context_reveal': 'Onyesha kwenye Finder',
        'recent_context_set_default': '⭐ Weka kama chaguo-msingi',
        'recent_context_open_terminal': '💻 Fungua Terminal',
        'recent_context_file_info': 'Maelezo ya faili',
        'recent_context_open_with_default': '📄 Fungua kwa programu chaguo-msingi',
        'recent_context_remove': 'Ondoa kutoka kwenye orodha',
        'recent_context_clear_all': 'Ondoa zote',
        'recent_file_info_title': 'Maelezo ya faili',
        'recent_file_info_name': 'Jina',
        'recent_file_info_path': 'Njia',
        'recent_file_info_size': 'Ukubwa',
        'recent_file_info_modified': 'Ilibadilishwa',
        'recent_file_info_pages': 'Kurasa',
        'recent_error_reveal': 'Hitilafu wakati wa kufungua kwenye Finder',
        'recent_error_terminal': 'Hitilafu wakati wa kufungua Terminal',
        'recent_error_info': 'Hitilafu wakati wa kupata maelezo ya faili',
        'open_user_data_folder': 'Onyesha daftari la data za mtumiaji',

        # ============================================
        # 108. FUTA KURASA ZA SAWA/ISIYO SAWA
        # ============================================
        "pages_delete_even": "Futa kurasa zote za sawa",
        "pages_delete_odd":  "Futa kurasa zote za isiyo sawa",
        "progress_even_pages": "Inafuta kurasa za sawa",
        "progress_odd_pages": "Inafuta kurasa za isiyo sawa",
        "progress_mark_delete_even": "Kurasa {} za sawa zimewekwa alama kwa kufutwa",
        "progress_mark_delete_odd":  "Kurasa {} za isiyo sawa zimewekwa alama kwa kufutwa",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programu inafungwa",

    }
