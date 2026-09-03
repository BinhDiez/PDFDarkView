
# ============================================
# translations_lb.py - Lëtzebuergescht Wierderbuch
# Vollständig sortiert nach Kategorien
# ============================================

def load_luxembourgish_strings():
    """Lädt alle luxemburgischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF lueden",
        'btn_text_window': "OCR Text",
        'btn_first': "Éischt Säit",
        'btn_prev': "Säit zréck",
        'btn_next': "Nächst Säit",
        'btn_last': "Läscht Säit",
        'btn_print': "Drécken",
        'btn_darkmode_light': "Liichtmodus",
        'btn_darkmode_dark': "Däischtermodus",
        'btn_delete_pages': "Säiten läschen",
        'btn_extract_pages': "Säiten eraushuelen",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Ofbriechen",
        'btn_save': "Späicheren",
        'btn_close': "Zoumaachen",
        'btn_delete': "Läschen",
        'btn_delete_all': "All läschen",
        'btn_copy': "Kopéieren",
        'btn_export': "Exportéieren",
        'btn_show': "Passwuert weisen",
        'btn_hide': "Passwuert verstoppen",
        'btn_authenticate': "Authentifizéieren",
        'btn_settings': "Astellungen",
        'btn_protect': "Schützen",
        'btn_remove_password': "Passwuert ewechhuelen",
        'btn_manage': "Passwuertverwaltung",
        'btn_retry': "Nach eng Kéier probéieren",
        'btn_select_all': "All auswielen",
        'btn_clear_selection': "Auswiel ophiewen",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Säit {0} vun {1}",
        'page_count': "vun {0}",
        'goto_page': "Ginn op Säit",
        'page_simple': "Säit {0}",
        'full_view_page': "Vollusiicht Säit {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Sichbegrëff aginn + Enter",
        'search_results': "Resultater: {0} vun {1}",
        'search_nav_hint': "Enter: nächsten (Shift+Enter: viregen) Treffer",
        'search_no_results': "Keng Resultater",
        'search_error': "Sichfeeler",
        'search_active': "Sichfeld aktivéiert",
        'search_closed': "Sich ofgeschloss",
        'search_position': "Säit {0} {1}",
        'search_pos_top': "ganz uewen",
        'search_pos_upper': "uewen",
        'search_pos_middle': "Mëtt",
        'search_pos_lower': "ënnen",
        'search_pos_bottom': "ganz ënnen",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Texterkennung erfollegräich ofgeschloss!",
        'ocr_success_title': "OCR erfollegräich",
        'ocr_success_message': "Den Dokument ass elo duerchsichbar.",
        'ocr_failed': "OCR feelgeschloen",
        'ocr_in_progress': "OCR gëtt verschafft",
        'ocr_preparing': "PDF gëtt virbereet...",
        'ocr_analyzing': "PDF gëtt analyséiert...",
        'ocr_optimizing': "Bildoptiméierung leeft...",
        'ocr_recognizing': "Texterkennung am Gaang...",
        'ocr_embedding': "Text gëtt agebett...",
        'ocr_finalizing': "Finaliséierung vum PDF...",
        'ocr_not_available': "OCR net verfügbar",
        'ocr_install_message': "OCR-Tools goufen net fonnt.\n\nInstalléiert w.e.g.:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR néideg",
        'ocr_question': "D'PDF enthält keen duerchsichbaren Text.\nWëllt Dir OCR ausféieren, fir {0} z'erméiglechen?",
        'ocr_perform': "OCR ausféieren",
        'ocr_later': "Méi spéit",
        'ocr_starting': "Start garantéiert OCR...",
        'ocr_success_voice': "OCR erfollegräich. PDF ass elo duerchsichbar.",
        'ocr_partial_success': "OCR gouf ausgefouert, awer beim Ersetze gouf et Problemer.\n\nD'duerchsichbar Versioun gouf gespäichert ënner:\n{0}\n\nFeeler: {1}",
        'ocr_partial_title': "OCR deelweis erfollegräich",
        'ocr_partial_voice': "OCR ausgefouert, awer Ersetzen feelgeschloen.",
        'original_file': "Originaldatei:",
        'old_size': "Al Gréisst:    {0} Bytes",
        'new_size': "Nei Gréisst: {0} Bytes",
        'size_change': "Ännerung: {0}{1} Bytes",
        'backup_created_file': "Backup ugeluecht:\n{0}",
        'backup_not_created': "Backup net ugeluecht (Astellung ausgeschalt)",
        'page_header': "=== Säit {0} ===\n{1}\n",
        'scanned_page_header': "=== Säit {0} (gescannt) ===\n[Dës Säit enthält nëmme gescannten Text]\n[OCR w.e.g. manuell ausféieren]\n",
        'scanned_warning': "⚠️ GESCANNTE TEXT - OCR NÉIDEG",
        'guaranteed_title': "Duerchsichbar PDF ugeluecht",
        'guaranteed_message': "<b>Garantéiert duerchsichbar Versioun ugeluecht!</b>\n\nWell den automateschen OCR feelgeschloen ass, gouf eng alternativ duerchsichbar PDF ugeluecht:\n\n{0}\n\n<b>Dëse Fichier enthält:</b>\n• Extrahierten Text (falls do)\n• Hiweiser fir gescannte Säiten\n• Ass vollstänneg duerchsichbar",
        'guaranteed_voice': "Garantéiert duerchsichbar PDF ugeluecht.",
        'instruction_title': "OCR-ULEEDUNG",
        'instruction_file': "Originaldatei: {0}",
        'instruction_text': "Den automateschen OCR ass feelgeschloen.\nFéiert OCR manuell aus:\n\n1. MAT OCRmyPDF (Kommandozeil):\n   ocrmypdf --force-ocr \"[FICHIER]\" \"ausgab.pdf\"\n\n2. MAT ADOBE ACROBAT (macOS/Windows):\n   • PDF an Acrobat opmaachen\n   • Tools > PDF beaarbechten\n   • 'Texterkennung' auswielen\n\n3. MAT PREVIEW (macOS):\n   • PDF an Preview opmaachen\n   • Fichier > Exportéieren...\n   • Quartz-Filter: 'Reduce File Size'\n   • 'OCR ausféieren' aktivéieren\n\n4. ONLINE OCR SERVICER:\n   • smallpdf.com/lb/ocr-pdf\n   • ilovepdf.com/lb/ocr-pdf\n   • adobe.com/lb/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR-Uleedung ugeluecht",
        'instruction_created_message': "Eng detailléiert Uleedung gouf ugeluecht:\n\n{0}\n\nFollegt w.e.g. d'Schrëtt fir manuell OCR.",
        'instruction_created_voice': "OCR-Uleedung ugeluecht.",
        'ocr_impossible': "OCR net méiglech",
        'ocr_impossible_message': "OCR konnt net ausgefouert ginn.\n\nVerschafft '{0}' manuell mat OCR-Software.",
        'ocr_impossible_voice': "OCR net méiglech. Verschafft manuell.",
        'emergency_title': "Noutfall-OCR",
        'emergency_message': "Eng Noutfall-PDF gouf ugeluecht:\n\n{0}\n\nVerschafft dëse Fichier manuell mat OCR.",
        'emergency_voice': "Noutfall-PDF ugeluecht. Féiert OCR manuell aus.",
        'critical_error': "Kritesche Feeler",
        'critical_error_message': "OCR konnt net gestart ginn.\n\nStart de Programm nei a kontrolléiert d'OCR-Installatioun.",
        'critical_error_voice': "Kriteschen OCR-Feeler",
        'ocr_question_html': "<p>D'PDF enthält keen duerchsichbaren Text.<p>Wëllt Dir OCR ausféieren, fir <b>{0}</b> z'erméiglechen?</p>",
        'ocr_question_voice': "OCR néideg. D'PDF enthält keen duerchsichbaren Text. Wëllt Dir OCR ausféieren, fir {0} z'erméiglechen?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "kee PDF gelueden",
        'no_pdf_message': "Et ass kee PDF gelueden",
        'pdf_not_found': "PDF-Fichier net fonnt",
        'file_size': "Fichiergréisst",
        'bytes': "Bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup ugeluecht",
        'backup_disabled': "Backup ausgeschalt",
        'backup_activated': "Backup-Erstellung aktivéiert",
        'backup_deactivated': "Backup-Erstellung ausgeschalt",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ aktivéiert",
        'backup_off': "✘ ausgeschalt",
        'close_pdf': "Schléiss PDF: {0}",
        'pdf_not_found_format': "PDF-Fichier net fonnt: {0}",
        'error_pdf_load_format': "Feeler beim Luede vum PDF: {0}",
        'load_failed_format': "Luede feelgeschloen:\n{0}",
        'decrypted_suffix': "(entschlësselt)",
        'decryption_failed': "Entschlësselen feelgeschloen.",
        'decryption_error': "Feeler beim Entschlësselen",
        'decryption_success': "Erfollegräich entschlësselt",
        'decryption_success_message': "PDF gouf entschlësselt a gespäichert ënner:\n\n{0}",
        'decryption_success_voice': "PDF gouf entschlësselt a gespäichert.",
        'password_remove_error': "Feeler beim Ewechhuele vum Passwuert",
        'save_unencrypted': "Onverschlësselt PDF späicheren ënner",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Späicheren ënner...",
        'save_copy': "Kopie späicheren",
        'save_success': "PDF gespäichert ënner: {0}",
        'save_encrypted': "Geschützt PDF gespäichert ënner: {0}",
        'save_error': "PDF konnt net gespäichert ginn",
        'encryption_question': "Wëllt Dir d'PDF mat engem Passwuert schützen?",
        'encryption_yes': "Jo",
        'encryption_no': "Neen",
        'encryption_cancel': "Ofbriechen",
        'save_cancel': "Späicheren ofgebrach",
        'save_encrypted_voice': "Fichier verschlësselt a gespäichert.",
        'save_success_voice': "De PDF-Fichier gouf onverschlësselt gespäichert.",
        'save_error_format': "PDF konnt net gespäichert ginn:\n{0}",
        'export_pages_success': "Pages-Export erfollegräich",
        'export_pages_error': "Pages-Export feelgeschloen",
        'export_pages_error_format': "Pages-Export feelgeschloen: {0}",
        'export_word_success': "Word-Export erfollegräich",
        'export_word_error': "Word-Export feelgeschloen",
        'export_word_error_format': "Word-Export feelgeschloen: {0}",
        'export_text_success': "Text-Export erfollegräich",
        'export_text_error': "Text-Export feelgeschloen",
        'export_text_error_format': "Text-Export feelgeschloen: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Passwuert néideg",
        'password_enter': "Gitt w.e.g. d'Passwuert an",
        'password_confirm': "Passwuert bestätegen",
        'password_new': "Neit Passwuert",
        'password_current': "Aktuellt Passwuert",
        'password_save': "Passwuert späicheren (verschlësselt)",
        'password_saved': "✓ Passwuert fir dëse Fichier ass gespäichert",
        'password_wrong': "Falscht Passwuert",
        'password_mismatch': "Passwierder stëmmen net iwwereneen",
        'password_too_short': "Passwuert ze kuerz",
        'password_min_length': "D'Passwuert muss mindestens 4 Zeechen laang sinn",
        'password_strength': "Passwuertstäerkt",
        'password_strength_very_weak': "Ganz schwaach",
        'password_strength_weak': "Schwaach",
        'password_strength_medium': "Mëttel",
        'password_strength_strong': "Staark",
        'password_strength_very_strong': "Ganz staark",
        'password_char_count': "({0} Zeechen)",
        'password_match': "✓ Iwwereneestëmmung",
        'password_no_match': "✗ Passwierder stëmmen net iwwereneen",
        'password_show': "Weisen",
        'password_hide': "Verstoppen",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Passwuertverwaltung",
        'password_table_filename': "Fichiersnumm",
        'password_table_password': "Passwuert",
        'password_count': "{0} gespäichert Passwuert{1}",
        'password_count_singular': "",
        'password_count_plural': "er",
        'password_none': "Keng gespäichert Passwierder",
        'password_copied': "{0} Passwuert{1} kopéiert",
        'password_copied_singular': "",
        'password_copied_plural': "er",
        'password_delete_confirm': "Wëllt Dir wierklech d'Passwuert fir '{0}' läschen?",
        'password_delete_multiple': "Wëllt Dir wierklech déi {0} ausgewielte Passwierder läschen?",
        'password_delete_all_confirm': "Wëllt Dir wierklech all {0} gespäichert Passwierder läschen?",
        'password_deleted': "{0} Passwuert{1} gouf{2} geläscht",
        'password_deleted_singular': "",
        'password_deleted_plural': "er",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "n",
        'password_all_deleted': "All Passwierder goufe geläscht",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Passwuertgenerator",
        'generator_generated': "Generéiert Passwuert:",
        'generator_regenerate': "Nei generéieren",
        'generator_copy': "Kopéieren",
        'generator_use': "Benotzen",
        'generator_settings': "Astellungen",
        'generator_length': "Längt:",
        'generator_group_every': "Trennzeechen all",
        'generator_group_chars': "Zeechen.    Trenner:",
        'generator_uppercase': "Groussbuschtawen (A-Z)",
        'generator_lowercase': "Klengbuschtawen (a-z)",
        'generator_digits': "Zuelen (0-9)",
        'generator_symbols': "Sonderzeechen (!@#$%^&*)",
        'generator_exclude': "Ausgeschloss:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Master-Passwuert néideg",
        'master_password_setup': "Master-Passwuert ariichten",
        'master_password_change': "Master-Passwuert änneren",
        'master_password_enter': "Gitt w.e.g. Äert Master-Passwuert an",
        'master_password_choose': "Wielt e séchert Master-Passwuert (mindestens 8 Zeechen)",
        'master_password_new': "Gitt w.e.g. Äert neit Master-Passwuert an",
        'master_password_confirm': "Passwuert bestätegen",
        'master_password_authenticate': "Authentifizéieren",
        'master_password_success': "Master-Passwuert gouf erfollegräich ageriicht.",
        'master_password_changed': "Master-Passwuert gouf erfollegräich geännert.",
        'master_password_removed': "Master-Passwuert an all Passwierder goufe geläscht.",
        'master_password_remove': "Master-Passwuert ewechhuelen",
        'master_password_remove_confirm': "Sidd Dir SÉCHER, datt Dir ALL Passwierder läsche wëllt?\n\nDës Aktioun ass NET ZRÉCKZENUHUELEN!",
        'master_password_export_before': "Wëllt Dir virdrun eng Sécherheetskopie exportéieren?",
        'master_password_export_delete': "Exportéieren & läschen",
        'master_password_delete_now': "Direkt läschen",
        'master_password_for_signatures': "Fir Signature kënnen ze benotzen, musst Dir e Master-Passwuert ariichten.\n\nWëllt Dir elo e Master-Passwuert ariichten?",
        'master_password_for_private': "Fir privat Textbausteng kënnen ze benotzen, musst Dir e Master-Passwuert ariichten.\n\nWëllt Dir elo e Master-Passwuert ariichten?",
        'master_password_info': """
            <b>🔐 OUNI MASTER-PASSWUERT:</b><br>
            • Kee Weisen, Kopéieren an Export vu Passwierder méiglech<br>
            • Läsche vu Passwierder ass ëmmer méiglech (och ouni Master-Passwuert)<br><br>

            <b>🔐 MAT MASTER-PASSWUERT:</b><br>
            • All Funktiounen disponibel no Authentifizéierung<br>
            • Passwierder ginn mam Master-Passwuert verschlësselt<br>
            • Mindestlängt: 8 Zeechen<br>
            • Sécher SHA-256 Hash-Späicherung<br><br>

            <b>WICHTEG:</b><br>
            • Bei Verloscht vum Master-Passwuert: Passwierder net erëmzerstellen<br>
            • Beim Ewechhuele vum Master-Passwuert: ALL Passwierder ginn geläscht<br>
            • Export-Optioun virum Läschen disponibel<br>
            • Master-Passwuert jiddwerzäit änderbar
        """,
        'signature_auth_disabled': "Passwuertofro fir Signaturen ausschalten",
        'template_auth_disabled': "Passwuertofro fir privat Textbausteng ausschalten",
        'master_password_for_signatures_settings': "Fir Signature kënnen ze benotzen, musst Dir e Master-Passwuert ariichten.\n\nGitt dofir an Astellungen - Passwuertverwaltung",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF schützen",
        'protect_info': "De Fichier '{0}' gëtt mat engem Passwuert geschützt.",
        'protect_instruction': "Gitt w.e.g. 2-mol dat gewënschte Passwuert an, fir den Dokument ze schützen, oder benotzt de Passwuertgenerator riets nieft dem Inputfeld.",
        'protect_success': "PDF gouf erfollegräich geschützt a gespäichert ënner:\n{0}\n\nPasswuert: {1}\n\nWëllt Dir dat geschützt PDF elo opmaachen?",
        'protect_open': "Jo",
        'protect_skip': "Neen",
        'protect_error': "Feeler beim Schütze vum PDF",
        'protect_open_title': "geschützt PDF opmaachen",
        'protect_question': "Fäerdeg. Wëllt Dir dat geschützt PDF elo opmaachen? Jo oder Neen?",
        'password_cancel': "Passwuert-Dialog ofgebrach",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Säiten läschen",
        'pages_extract': "Säiten eraushuelen",
        'pages_insert': "Säiten afügen",
        'pages_move': "Säiten réckelen",
        'pages_delete_options': "Läschoptiounen",
        'pages_delete_empty': "All eidel Säiten läschen",
        'pages_delete_current': "Aktuell Säit läschen",
        'pages_delete_range': "Säiteberäich läschen",
        'pages_extract_options': "Eraushueloptiounen",
        'pages_extract_current': "Aktuell Säit eraushuelen",
        'pages_extract_range': "Säiteberäich eraushuelen",
        'pages_insert_position': "Afügepositioun",
        'pages_insert_before': "Afügen virun Säit:",
        'pages_insert_select': "PDF auswielen",
        'pages_insert_none': "Kee PDF ausgewielt",
        'pages_move_source': "Ze réckelend Säiten",
        'pages_move_from': "Vun Säit:",
        'pages_move_to': "Bis Säit:",
        'pages_move_target': "Zilpositioun",
        'pages_move_before': "Réckele virun Säit:",
        'pages_move_hint': "Hiweis: Säit 1 = Ufank, {0} = Enn",
        'pages_range_invalid': "D'Start säit muss méi kleng oder gläich wéi d'Enn säit sinn.",
        'pages_position_invalid': "D'Zilpositioun däerf net am Beräich leien, dee geréckelt gëtt.",
        'pages_no_pdf_selected': "Et ass kee PDF ausgewielt.",
        'pages_deleted': "Et goufen {0} Säite geläscht.",
        'pages_extracted': "Erausgeholl: {0}\nGespäichert ënner: {1}\nFichiergréisst: {2:.1f} KB",
        'pages_inserted': "{0} Säiten agefügt",
        'pages_moved': "Et goufen {0} Säite geréckelt.",
        'pages_deleted_none': "Et goufe keng Säite geläscht.",
        'pages_delete_progress': "Säite läschen...",
        'pages_deleted_with_backup': "Et goufen {0} Säite geläscht.\n\nBackup: {1}",
        'pages_deleted_voice': "Et gouf e Backup ugeluecht an {0} Säite geläscht.",
        'info': "Hiweis",
        'error_dialog_creation': "Dialog konnt net erstallt ginn",
        'extract_page_single': "Säit {0} eraushuelen",
        'extract_page_range': "Säiten {0}-{1} eraushuelen",
        'extract_success_voice': "Säiten erfollegräich erausgeholl",
        'extract_error_format': "Feeler beim Eraushuelen: {0}",
        'pages_inserted_voice': "Et goufen {0} Säiten agefügt.",
        'insert_error_format': "Feeler beim Afügen: {0}",
        'pages_move_progress': "Säite réckelen...",
        'pages_moved_with_backup': "Et goufen {0} Säite geréckelt.\n\nBackup: {1}",
        'move_success_title': "Erfollegräich geréckelt",
        'pages_moved_voice': "{0} Säiten erfollegräich geréckelt",
        'mark_removed': "Markéierung vun der Säit {0} ewechgeholl",
        'mark_empty': "Säit {0} als eidel markéiert",
        'mark_export_removed': "Export-Markéierung vun der Säit {0} ewechgeholl",
        'mark_export': "Säit {0} fir Export markéiert",
        'no_empty_pages': "Keng eidel Säite markéiert fir ze läschen",
        'delete_empty_confirm': "Wëllt Dir all {0} markéiert eidel Säite läschen?",
        'delete_empty_confirm_voice': "Elo all {0} markéiert eidel Säite läschen? Jo oder Neen.",
        'empty_pages_deleted': "{0} eidel Säite geläscht",
        'no_export_pages': "Keng Säite fir Export markéiert",
        'overwrite_title': "Bestehende Fichier iwwerschreiwen",
        'overwrite_question': "De Fichier\n\n{0}\n\ngëtt et schonn.\nWëllt Dir en iwwerschreiwen?",
        'overwrite_voice': "Bestehende Fichier iwwerschreiwen? Jo oder Neen.",
        'page_skipped': "Säit {0} gouf iwwersprongen",
        'export_complete': "Export ofgeschloss.",
        'export_complete_voice': "Den Export ass ofgeschloss.",
        'no_pages_exported': "Keng Säit exportéiert",
        'export_cancelled': "Export ofgebrach",
        'pages_exported': "{0} Säiten exportéiert op {1}",
        'export_page_title': "Säit exportéieren",
        'page_exported': "Säit {0} exportéiert op {1}",
        'export_error': "Feeler beim Export",
        'export_marked_title': "Markéiert Säiten exportéieren",
        'rotate_all_title': "all Säiten dréien",
        'rotate_all_question': "Wëllt Dir all Säiten ëm 90 Grad no riets dréien?",
        'rotate_all_voice': "Wëllt Dir all Säiten ëm 90 Grad no riets dréien? Jo oder Neen?",
        'all_pages_rotated': "All Säite gedréint",
        'page_rotated': "Säit {0} gedréint",
        'rotate_error': "Säit konnt net gedréint ginn",
        'delete_page_confirm': "Wëllt Dir d'Säit {0} läschen?",
        'delete_page_confirm_voice': "Wëllt Dir wierklech d'Säit {0} läschen? Jo oder Neen.",
        'page_deleted': "Säit {0} geläscht",
        'delete_error': "Säit konnt net geläscht ginn",
        'pages_deleted_voice': "{0} Säite geläscht",
        'pages_exported_split': "{0} Säite goufen erfollegräich exportéiert.",
        'pages_skipped': "{0} Säite goufen iwwersprongen.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Säiten eraushuelen (erweidert)",
        'pdf_splitter_title': "PDF Splitter & Extractor",
        'pdf_splitter_load': " PDF-Fichier auswielen",
        'pdf_splitter_info': "Wielt w.e.g. eng Optioun fir Ären PDF-Dokument",
        'pdf_splitter_basic': "Grondleeënd Operatiounen",
        'pdf_splitter_single': "An eenzel Säiten opdeelen",
        'pdf_splitter_range': "Säiten extrahéieren:",
        'pdf_splitter_range_placeholder': "z.B. 1-3,5,7-9",
        'pdf_splitter_clean': "Botzoperatiounen",
        'pdf_splitter_remove_empty': "All eidel Säiten ewechhuelen",
        'pdf_splitter_remove': "Säiteberäich läschen:",
        'pdf_splitter_remove_placeholder': "z.B. 2,4-6",
        'pdf_splitter_process': "PDF verschaffen",
        'pdf_splitter_loaded': "PDF gelueden. Wielt w.e.g. eng Optioun",
        'pdf_read_error': "PDF konnt net gelies ginn",
        'pages': "Säiten",
        'pages_created': "Säite goufen ugeluecht",
        'range_empty': "Gitt w.e.g. e Säiteberäich an",
        'range_invalid': "Ongültege Säiteberäich",
        'range_created': "Neit PDF mat den ausgewielte Säite gouf ugeluecht:\n{0}",
        'empty_removed': "{0} eidel Säiten ewechgeholl.\nAusgab: {1}",
        'remove_empty': "Gitt w.e.g. Säiten un déi ewechgeholl solle ginn",
        'remove_invalid': "Ongülteg Säiten zum Ewechhuelen",
        'remove_done': "Botzt PDF ugeluecht:\n{0}",
        'open_folder': "Dossier opmaachen",
        'show_in_finder': "Am Finder weisen",
        'pdf_splitter_no_pdf': "Luet w.e.g. fir d'éischt e PDF-Fichier.",
        'process_error': "Feeler beim Verschaffe vum PDF",
        'pages_created_voice': "{0} Säite goufen ugeluecht",
        'range_created_voice': "PDF mat den ausgewielte Säite gouf ugeluecht",
        'empty_removed_voice': "{0} eidel Säite goufen ewechgeholl",
        'remove_done_voice': "Botzt PDF gouf ugeluecht",
        'pdf_splitter_split_groups': "All zesummenhängend Grupp an eenzele Fichier",
        'range_created_single': "Neit PDF ugeluecht:\n{0}",
        'range_created_multiple': "{0} PDF-Fichieren ugeluecht.",
        'range_created_voice_single': "Ee PDF mat den ausgewielte Säite gouf ugeluecht",
        'range_created_voice_multiple': "{0} PDF-Fichiere goufen ugeluecht",
        'empty_removed_none_left': "Keng Säite méi iwwreg",
        'empty_removed_all_empty': "All Säite goufen als eidel erkannt a géifen ewechgeholl ginn. Et gouf kee Fichier ugeluecht.",
        'preview_single': "Virschau: {0}",
        'preview_enter_range': "Gitt w.e.g. e Säiteberäich an.",
        'preview_invalid_range': "Ongültege Säiteberäich.",
        'preview_file': "Virschau: {0}",
        'preview_files': "Virschau: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Start Dréckprozess",
        'print_sent': "Dréckoptrag geschéckt",
        'print_now': "Direkt drécken",
        'print_error': "Feeler beim Direkt-Drock",
        'print_limited': "Dréckfunktioun op dësem System ageschränkt",
        'print_error_format': "Feeler beim Direkt-Drock: {0}",
        'warning': "Hiweis",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Op Liichtmodus wiesselen",
        'mode_switch_to_dark': "Op Däischtermodus wiesselen",
        'mode_dark_activated': "Däischtermodus aktivéiert",
        'mode_light_activated': "Liichtmodus aktivéiert",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Vollusiicht",
        'zoom_two_pages': "Zwee Säiten niewentenee",
        'zoom_overview': "Iwwersiichtsmodus",
        'zoom_cannot_during_search': "Zoom während der Sich net méiglech",
        'zoom_exit_first': "Gitt w.e.g. fir d'éischt aus dem Zoom eraus",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop aktivéiert",
        'drag_disabled': "Drag & Drop ausgeschalt",
        'drag_page_grab': "Säit {0} gräifen",
        'drag_page_dropped': "Säit {0} op Positioun {1} agefügt",
        'drag_position_invalid': "Ongülteg Positioun",
        'drag_same_position': "Säit {0} bleift op Positioun {0}",
        'drag_error': "Feeler beim Réckelen",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Textagab mat erweiderte Formatéierungen a Textbaustengverwaltung",
        'text_templates': "Disponibel Textbausteng:",
        'text_name': "Numm",
        'text_preview': "Textvirschau",
        'text_enter': "Text:",
        'text_font_size': "Schrëftgréisst:",
        'text_formatting': "Formatéierung:",
        'text_bold': "Fett",
        'text_italic': "Kursiv",
        'text_underline': "Ënnerstrach",
        'text_alignment': "Ausriichtung:",
        'text_left': "Lénks",
        'text_center': "Zentréiert",
        'text_right': "Riets",
        'text_color': "Textfaarf:",
        'text_opacity': "Ofdeckung:",
        'text_word_wrap': "Zeilenëmbroch:",
        'text_auto': "Automatesch",
        'text_page_width_95': "Säitebreet (95 %)",
        'text_page_width_85': "Ganz breet (85 %)",
        'text_page_width_75': "Méi breet (75 %)",
        'text_page_width_60': "Breet (60 %)",
        'text_page_width_50': "Mëttel (50 %)",
        'text_page_width_30': "Schmuel (30 %)",
        'text_page_width_20': "Méi schmuel (20 %)",
        'text_page_width_10': "Ganz schmuel (10 %)",
        'text_no_wrap': "Keen Ëmbroch",
        'text_private': "Privat Textbausteng (erfuerdert Authentifizéierung)",
        'text_preview_label': "Virschau:",
        'text_preview_placeholder': "Hei gëtt eng Virschau vum Text gewisen...",
        'text_no_text': "(Keen Text)",
        'text_save_template': "💾 Als Bausteng späicheren",
        'text_delete_template': "🗑 Ausgewielten Textbausteng läschen",
        'text_show_private': "Privat weisen",
        'text_hide_private': "Privat verstoppen",
        'text_use': "✅ Text benotzen",
        'text_saved': "Textbausteng gespäichert als:\n{0}",
        'text_saved_voice': "Textbausteng gespäichert",
        'text_deleted': "Textbausteng geläscht",
        'text_no_text_to_save': "Keen Text fir ze späicheren.",
        'text_no_templates': "Keng Textbausteng fonnt",
        'text_private_master_required': "Privat Bausteng kënnen nëmme benotzt ginn, wann e Master-Passwuert ageriicht ass.\n\nWëllt Dir elo e Master-Passwuert ariichten?",
        'text_filename': "Fichiersnumm fir Textbausteng (ouni 'Text_' an '.txt'):",
        'text_filename_hint': "Beispill: 'Telefon Heembüro' gëtt gespäichert als 'Text_Telefon Heembüro.txt'",
        'text_save_hint': "Den Textbausteng gëtt automatesch mat Formatéierung gespäichert.",
        'text_guide_title': "Textagab - Uleedung",
        'text_delete_confirm': "Wëllt Dir wierklech den Textbausteng läschen?\n\nFichier: {0}\nText: {1}...",
        'text_make_public': "Als ëffentlech markéieren",
        'text_make_private': "Als privat markéieren",
        'text_privacy_changed': "Privatstatus geännert",
        'text_private_always': "Privat ëmmer siichtbar (Astellung)",
        'text_mode_required': "Gitt w.e.g. fir d'éischt an den Text-Modus",
        'text_continue_editing': "Weider beaarbechten - Cursor um Textenn",
        'text_no_input': "Keen Text aginn - Text verworf",
        'save_dialog_question': "Wéi wëllt Dir virufueren?",
        'text_save_question': "All Texter a Kräizer späicheren, upassen, weider beaarbechten oder verworf?",
        'copy_cross': "Kräiz kopéiert",
        'paste_cross': "Kräiz agefügt",
        'paste_text': "Text agefügt",
        'cross_discarded': "Kräiz verworf",
        'all_discarded': "Alles verworf",
        'text_discarded': "Text verworf",
        'no_texts_to_save': "Keng Texter fir ze späicheren",
        'no_valid_texts': "Keng gëlteg Texter fir ze späicheren",
        'text_word_singular': "Text",
        'text_word_plural': "Texter",
        'cross_word_singular': "Kräiz",
        'cross_word_plural': "Kräizer",
        'texts_saved_title': "Texter gespäichert",
        'texts_crosses_saved': "{0} {1} an {2} {3} goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'texts_crosses_saved_voice': "{0} {1} an {2} {3} gespäichert.",
        'texts_saved': "{0} {1} goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'texts_saved_voice': "{0} {1} gespäichert.",
        'crosses_saved': "{0} {1} goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'crosses_saved_voice': "{0} {1} gespäichert.",
        'elements_saved': "{0} Elementer goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'elements_saved_voice': "{0} Elementer gespäichert.",
        'text_window_load_error': "Textfënster konnt net gelueden ginn",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Textagab an Textbausteng – Ausféierlech Uleedung**

        **1. Text afügen a beaarbechten**
        - Klickt mat rietser Maustast op déi gewënschte Plaz am Dokument a wielt "Text afügen".
        - Et mécht sech en Dialog op, wou Dir Ären Text aginn a formatéiere kënnt:
        • Schrëftgréisst, Fett, Kursiv, Ënnersträichen
        • Textfaarf (fräi wielbar)
        • Transparenz (Ofdeckung) iwwer Schieberegler
        • Zeilenëmbroch (verschidde Breeten, z.B. Säitebreet, schmuel, keen Ëmbroch)
        - No Bestätegung erschéngt den Text op der Klickpositioun. Dir kënnt en mat der Maus oder de Pfeiltasten réckelen.
        - Duebelklick op den Text mécht de Beaarbechtungsmodus op; mat ESC verléisst Dir en erëm.

        **2. Textbausteng (Templates) verwalten**
        - Am Text-Dialog gesitt Dir lénks eng Lëscht vun alle gespäicherte Textbausteng.
        - **Späichere vun engem Bausteng:** Gitt Ären Text an, formatéiert en a klickt op "💾 Als Bausteng späicheren". Gitt e Fichiersnumm an (ouni Endung).
        - **Luede vun engem Bausteng:** Klickt an der Lëscht op de gewënschten Numm. Den Text an d'Formatéierung ginn iwwerholl a kënne bei Bedarf nach ugepasst ginn.
        - **Läschen:** Mat Rietsklick op e Bausteng kënnt Dir en läschen oder säi Privatstatus änneren.

        **3. Privat Textbausteng (Master-Passwuert)**
        - Wann Dir e Master-Passwuert ageriicht hutt (ënner Astellungen → Passwuertverwaltung), kënnt Dir Bausteng als "privat" markéieren.
        - Aktivéiert dofir d'Checkbox "Privat Textbausteng" am Dialog ier Dir späichert.
        - Privat Bausteng ginn an der Lëscht nëmme gewisen, wann Dir eemol pro Sëtzung Äert Master-Passwuert aginn hutt (Authentifizéierung iwwer d'Schlasssymbol oder beim éischten Zougrëff).
        - Esou kënnt Dir vertraulech Textbausteng viru friemem Zougrëff schützen.

        **4. Kräizer afügen**
        - Iwwer dat kontextuellt Menü kënnt Dir och e grafescht Kräiz (z.B. fir Kontrollkëschter) afügen.
        - D'Gréisst, Linnenstäerkt a Faarf vu Kräizer kënnt Dir global an den Astellungen upassen (Menü "Astellungen" → "Kräiz-Astellungen").
        - Mat Rietsklick op e bestoend Kräiz kënnt Dir et individuell veränneren.

        **5. Sammelaktiounen**
        - Wann Dir méi Texter oder Kräizer op enger Säit placéiert hutt, kënnt Dir iwwer dat kontextuellt Menü (Rietsklick am Textmodus) all Elementer zesumme späicheren oder verworf.
        - Beim Späichere ginn all Elementer an d'PDF agebett a bleiwe als Vektorgrafike bestoen.

        **6. Tastaturkuerzel am Textmodus**
        - Pfeiltasten: Element réckelen
        - Strg+Pfeiltasten: méi grouss Schrëtt
        - Enter: Späicherdialog opmaachen (all späicheren / upassen / verworf)
        - ESC: aktuellt Element verworf
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Textagab an Textbausteng – Ausféierlech Uleedung</strong></p>

        <p><strong>1. Text afügen a beaarbechten</strong></p>
        <ul>
        <li>Klickt mat rietser Maustast op déi gewënschte Plaz am Dokument a wielt "Text afügen".</li>
        <li>Et mécht sech en Dialog op, wou Dir Ären Text aginn a formatéiere kënnt:<br/>
        • Schrëftgréisst, Fett, Kursiv, Ënnersträichen<br/>
        • Textfaarf (fräi wielbar)<br/>
        • Transparenz (Ofdeckung) iwwer Schieberegler<br/>
        • Zeilenëmbroch (verschidde Breeten, z.B. Säitebreet, schmuel, keen Ëmbroch)</li>
        <li>No Bestätegung erschéngt den Text op der Klickpositioun. Dir kënnt en mat der Maus oder de Pfeiltasten réckelen.</li>
        <li>Duebelklick op den Text mécht de Beaarbechtungsmodus op; mat ESC verléisst Dir en erëm.</li>
        </ul>

        <p><strong>2. Textbausteng (Templates) verwalten</strong></p>
        <ul>
        <li>Am Text-Dialog gesitt Dir lénks eng Lëscht vun alle gespäicherte Textbausteng.</li>
        <li><strong>Späichere vun engem Bausteng:</strong> Gitt Ären Text an, formatéiert en a klickt op "💾 Als Bausteng späicheren". Gitt e Fichiersnumm an (ouni Endung).</li>
        <li><strong>Luede vun engem Bausteng:</strong> Klickt an der Lëscht op de gewënschten Numm. Den Text an d'Formatéierung ginn iwwerholl a kënne bei Bedarf nach ugepasst ginn.</li>
        <li><strong>Läschen:</strong> Mat Rietsklick op e Bausteng kënnt Dir en läschen oder säi Privatstatus änneren.</li>
        </ul>

        <p><strong>3. Privat Textbausteng (Master-Passwuert)</strong></p>
        <ul>
        <li>Wann Dir e Master-Passwuert ageriicht hutt (ënner Astellungen → Passwuertverwaltung), kënnt Dir Bausteng als "privat" markéieren.</li>
        <li>Aktivéiert dofir d'Checkbox "Privat Textbausteng" am Dialog ier Dir späichert.</li>
        <li>Privat Bausteng ginn an der Lëscht nëmme gewisen, wann Dir eemol pro Sëtzung Äert Master-Passwuert aginn hutt (Authentifizéierung iwwer d'Schlasssymbol oder beim éischten Zougrëff).</li>
        <li>Esou kënnt Dir vertraulech Textbausteng viru friemem Zougrëff schützen.</li>
        </ul>

        <p><strong>4. Kräizer afügen</strong></p>
        <ul>
        <li>Iwwert dat kontextuellt Menü kënnt Dir och e grafescht Kräiz (z.B. fir Kontrollkëschter) afügen.</li>
        <li>D'Gréisst, Linnenstäerkt a Faarf vu Kräizer kënnt Dir global an den Astellungen upassen (Menü "Astellungen" → "Kräiz-Astellungen").</li>
        <li>Mat Rietsklick op e bestoend Kräiz kënnt Dir et individuell veränneren.</li>
        </ul>

        <p><strong>5. Sammelaktiounen</strong></p>
        <ul>
        <li>Wann Dir méi Texter oder Kräizer op enger Säit placéiert hutt, kënnt Dir iwwer dat kontextuellt Menü (Rietsklick am Textmodus) all Elementer zesumme späicheren oder verworf.</li>
        <li>Beim Späichere ginn all Elementer an d'PDF agebett a bleiwe als Vektorgrafike bestoen.</li>
        </ul>

        <p><strong>6. Tastaturkuerzel am Textmodus</strong></p>
        <ul>
        <li>Pfeiltasten: Element réckelen</li>
        <li>Strg+Pfeiltasten: méi grouss Schrëtt</li>
        <li>Enter: Späicherdialog opmaachen (all späicheren / upassen / verworf)</li>
        <li>ESC: aktuellt Element verworf</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Kräiz-Astellungen",
        'cross_properties': "Kräiz-Eegeschaften",
        'cross_size': "Gréisst (px):",
        'cross_line_width': "Linnenstäerkt:",
        'cross_color': "Faarf:",
        'cross_choose_color': "Wielen",
        'cross_fine_tuning': "Feinjustéierung beim Späicheren (Pixel)",
        'cross_offset_x': "X-Offset:",
        'cross_offset_y': "Y-Offset:",
        'cross_offset_x_tooltip': "Negativ Wäerter réckelen d'Kräiz beim Späicheren no lénks, positiv no riets",
        'cross_offset_y_tooltip': "Negativ Wäerter réckelen d'Kräiz beim Späicheren no uewen, positiv no ënnen",
        'cross_preview': "Virschau",
        'cross_save': "Astellungen iwwerhuelen",
        'cross_customized': "Kräiz ugepasst",
        'cross_settings_applied': "Kräiz-Astellunge gespäichert.\nGréisst: {0}px, Linnenstäerkt: {1}px\n{2}",
        'cross_updated_count': "{0} bestoend Kräizer goufen aktualiséiert.",
        'cross_no_crosses': "Keng bestoend Kräizer fonnt.",
        'cross_settings_applied_all': "Kräizastellunge fir all {0} Kräizer iwwerholl",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Signatur-Astellungen",
        'signature_1': "Signatur 1",
        'signature_2': "Signatur 2",
        'signature_select': "Signatur auswielen",
        'signature_add': "➕ Nei Ënnerschrëft derbäisetzen...",
        'signature_size': "Gréisst fir Signatur {0} (%):",
        'signature_common': "Allgemeng Astellungen",
        'signature_timestamp': "Zäitstempel automatesch derbäisetzen",
        'signature_location': "Standardplaz:",
        'signature_timestamp_size': "Zäitstempel Schrëftgréisst:",
        'signature_no_files': "-- Keng Signature fonnt --",
        'signature_insert': "Ënnerschrëft afügen",
        'signature_insert_1': "Signatur 1 afügen",
        'signature_insert_2': "Signatur 2 afügen",
        'signature_customize': " Dës Signatur upassen",
        'signature_discard': " Dës Signatur verworf",
        'signature_save_all': " All Signature späicheren",
        'signature_discard_all': " All Signature verworf",
        'signature_guide_title': "Ënnerschrëften - Uleedung",
        'signature_guide': """
📝 Ënnerschrëften - Kuerzuleedung

- Master-Passwuert ariichten
- Ënnerschrëften am Menü Astellunge konfiguréieren
  (Gréisst, Zäitstempel ...)
- Afügen mat RECHTSKLICK op der gewënschter Positioun
  (Master-Passwuert eemol pro Sëtzung néideg)
- Signatur mat der Maus oder Pfeiltaste réckelen
- Méi Signature kënnen noeneen agefügt ginn
- Jiddwer Signatur kann individuell ugepasst ginn
- Eenzel Signatur verworf
- All Signature gläichzäiteg späicheren / verworf
- Alternativ kann och d'Menüsläischt benotzt ginn.
        """,
        'signature_placeholder': "Keng Virschau disponibel",
        'signature_info': "Signatur {0}: {1}×{2} px ({3}% vun {4}×{5})",
        'signature_info_placeholder': "Astellunge fir Signatur {0}",
        'signature_inserted': "Signatur {0} op Säit {1} agefügt",
        'signature_deleted': "Signatur geläscht",
        'signature_copied': "Signatur kopéiert",
        'signature_pasted': "Signatur {0} agefügt",
        'signature_saved': "{0} Signature goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'signature_saved_voice': "{0} Signature gespäichert",
        'mode_replace_signature_format': "Modus verloossen a Signatur {0} afügen",
        'mode_conflict_voice_signature': "{0} Modus ass aktiv. Verloossen a Signatur afügen?",
        'signature_not_configured': "Signatur {0} net konfiguréiert",
        'signature_file_not_found': "Signatur-Fichier net fonnt",
        'timestamp_format': "{0}, den {1}",
        'no_copied_signature': "Keng kopéiert Signatur do",
        'no_signatures_to_save': "Keng Signature fir ze späicheren",
        'signature_save_question': "All Signature späicheren, upassen oder dës verworf?",
        'signatures_saved_title': "Signature gespäichert",
        'signatures_saved': "{0} Signature goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'signatures_saved_voice': "{0} Signature gespäichert.",
        'all_signatures_discarded': "All Signature verworf",
        'signature_settings_saved': "Signatur-Astellunge gespäichert",
        'signature_cancelled': "Signatur verworf",
        'signature_active_title': "Signatur aktiv",
        'signature_replace_question': "Et ass schonn eng Signatur aktiv.\n\nWëllt Dir déi aktuell Signatur ersetzen?",
        'signature_replace': "Ënnerschrëft ersetzen",
        'signature_replace_voice': "Aktuell Signatur ersetzen oder ofbriechen?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Bildastellungen",
        'image_common': "Allgemeng Bildastellungen",
        'image_keep_aspect': "Säiteverhältnis beim Zéien bäibehalen",
        'image_default_size': "Standardgréisst (%):",
        'image_dark_invert': "Biller am Däischtermodus invertéieren",
        'image_dark_invert_tooltip': "Aktivéiert: Biller ginn fir besser Siichtbarkeet invertéiert",
        'image_fine_tuning': "Feinjustéierung (Pixel)",
        'image_offset_x': "X-Offset:",
        'image_offset_y': "Y-Offset:",
        'image_offset_x_tooltip': "Negativ Wäerter réckelen d'Bild beim Späicheren no lénks, positiv no riets",
        'image_offset_y_tooltip': "Negativ Wäerter réckelen d'Bild beim Späicheren no uewen, positiv no ënnen",
        'image_select': "Bild auswielen",
        'image_insert': "Bild afügen",
        'image_customize': " Bild upassen",
        'image_aspect': " Säiteverhältnis bäibehalen",
        'image_discard': " Dëst Bild verworf",
        'image_save_all': " All Biller späicheren",
        'image_discard_all': " All Biller verworf",
        'image_filter': "Biller",
        'image_guide_title': "Biller afügen - Uleedung",
        'image_guide': """
📷 Biller an PDF afügen - Kuerzuleedung:

1. Rietsklick op déi gewënschte Positioun
2. "Bild afügen" → Bild auswielen
3. Bild positionéieren: Zéien mat der Maus
4. Gréisst upassen: Zéien un den Ecken/Kante
5. Säiteverhältnis bäibehalen: [A] Taste
6. Weider Upassungen: Rietsklick op Bild

Tipp: Am Kontextmenü kënnt Dir d'Astellunge upassen.
        """,
        'image_inserted': "Bild {0} op Säit {1} agefügt",
        'image_deleted': "Bild verworf",
        'image_copied': "Bild kopéiert",
        'image_pasted': "Bild agefügt",
        'image_saved': "{0} Biller goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'image_saved_voice': "{0} Biller gespäichert",
        'image_aspect_on': "aktivéiert",
        'image_aspect_off': "ausgeschalt",
        'image_aspect_toggle': "Säiteverhältnis bäibehalen {0}",
        'image_reset': "Bild op Originalgréisst zréckgesat",
        'image_replaced': "Bild ersat",
        'image_invalid': "Kee gëltegt Bild",
        'mode_replace_image': "Bild afügen",
        'mode_conflict_voice_image': "{0} Modus ass aktiv. Verloossen a Bild afügen?",
        'image_active_title': "Bild aktiv",
        'image_replace_question': "Et ass schonn e Bild aktiv.\n\nWëllt Dir dat aktuellt Bild ersetzen?",
        'image_replace': "Bild ersetzen",
        'image_replace_voice': "Aktuellt Bild ersetzen oder ofbriechen?",
        'image_filter_all': "Biller (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;All Fichieren (*.*)",
        'no_copied_image': "Kee kopéiert Bild do",
        'image_discarded': "Bild verworf",
        'image_save_question': "All Biller späicheren, upassen oder dëst verworf?",
        'no_images_to_save': "Keng Biller fir ze späicheren",
        'no_valid_images': "Keng gëlteg Biller fir ze späicheren",
        'images_saved_title': "Biller gespäichert",
        'images_saved': "{0} Biller goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'images_saved_voice': "{0} Biller gespäichert.",
        'all_images_discarded': "All Biller verworf",
        'image_settings_updated': "Bildastellunge aktualiséiert",
        'image_replace_title': "Neit Bild auswielen",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Formen Astellungen",
        'form_basic': "Grondleeënd Astellungen",
        'form_default_type': "Standard-Formtyp:",
        'form_rectangle': "Rechteck",
        'form_ellipse': "Ellips",
        'form_line': "Linn",
        'form_arrow': "Feil",
        'form_line_width': "Linnenstäerkt:",
        'form_colors': "Faarwen",
        'form_line_color': "Linnenfaarf:",
        'form_fill_color': "Fëllfaarf:",
        'form_choose_color': "Wielen",
        'form_transparent': "Transparenten Hannergrond (nëmme Linn)",
        'form_filled': "gefëllt",
        'form_dark_mode': "Däischtermodus",
        'form_dark_invert': "Faarwen am Däischtermodus invertéieren",
        'form_fine_tuning': "Feinjustéierung (Pixel)",
        'form_offset_x': "X-Offset:",
        'form_offset_y': "Y-Offset:",
        'form_offset_x_tooltip': "Negativ Wäerter réckelen d'Form beim Späicheren no lénks, positiv no riets",
        'form_offset_y_tooltip': "Negativ Wäerter réckelen d'Form beim Späicheren no uewen, positiv no ënnen",
        'form_preview': "Virschau",
        'form_insert': "Form afügen",
        'form_rectangle_insert': "Rechteck",
        'form_ellipse_insert': "Ellips/Krees",
        'form_line_insert': "Linn (2 Klicks)",
        'form_arrow_insert': "Feil (2 Klicks)",
        'form_customize': " Form upassen",
        'form_transparent_toggle': " Transparenten Hannergrond",
        'form_discard': " Dës Form verworf",
        'form_save_all': " All Formen späicheren",
        'form_discard_all': " All Formen verworf",
        'form_guide_title': "Formen afügen - Uleedung",
        'form_guide': """
📐 Formen an PDF afügen - Kuerzuleedung:

1. Form-Typ auswielen (Rechteck, Ellips, Linn, Feil)
2. Op Positioun klicken
   - Bei Rechteck/Ellips: Ee Klick placéiert d'Form
   - Bei Linn/Feil: Zwee Klicks fir Start- an Ennpunkt
3. Form positionéieren: Zéien mat der Maus
4. Gréisst upassen: Zéien un den Ecken/Kante
5. Form späicheren: Enter
6. Form verworf: ESC
7. Weider Upassungen: Rietsklick op Form

Tipp: Am Kontextmenü kënnt Dir d'Astellunge upassen.
        """,
        'form_inserted': "{0} op Säit {1} agefügt",
        'form_deleted': "Form geläscht",
        'form_copied': "Form kopéiert",
        'form_pasted': "Form agefügt",
        'form_saved': "{0} Formen goufen an d'PDF agefügt.\n\nPDF gouf nei gelueden...",
        'form_saved_voice': "{0} Forme gespäichert",
        'form_reset': "Form op Standardgréisst zréckgesat",
        'form_transparent_on': "aktivéiert",
        'form_transparent_off': "ausgeschalt",
        'form_transparent_toggled': "Transparenten Hannergrond {0}",
        'form_line_cancel': "Linn-Zeechnen ofgebrach",
        'form_second_click': "Elo Ennpunkt fir {0} klicken",
        'mode_replace_form': "Form afügen",
        'mode_conflict_voice_form': "{0} Modus ass aktiv. Verloossen a Form afügen?",
        'form_settings_updated': "Formen-Astellunge aktualiséiert",
        'form_unknown': "Form",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klickt op d'Startpositioun",
        'form_line_guide_2': "2. Klickt op d'Ennpositioun",
        'form_line_guide_3': "D'Linn gëtt tëscht béide Punkte gezeechent.",
        'form_line_status_1': "Waart op éischte Klick...",
        'form_line_status_2': "Éischte Punkt gesat: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Elo Ennpunkt klicken...",
        'form_line_status_4': "Béid Punkte gesat.\nKlickt op 'Fäerdeg' fir ze späicheren.",
        'form_line_reset': "Zrécksetzen",
        'form_line_finish': "Fäerdeg",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopéieren (Cmd+C)",
        'paste': "Afügen (Cmd+V)",
        'copied': "Kopéiert: {0}",
        'no_element_to_copy': "Keen Element zum Kopéieren ausgewielt",
        'no_copied_data': "Keng kopéiert Date do",
        'no_valid_position': "Keng gëlteg Positioun fir anzesetzen",
        'copy_text': "Text kopéiert",
        'copy_image': "Bild kopéiert",
        'copy_form': "Form kopéiert",
        'copy_signature': "Signatur kopéiert",
        'element_text': "Text",
        'element_image': "Bild",
        'element_form': "Form",
        'element_signature': "Signatur",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Modus-Konflikt",
        'mode_conflict_message': "Et ass schonn de Modus '{0}' aktiv.\n\nWëllt Dir dëse verloossen an {1}?",
        'mode_replace': "Modus verloossen an {0}",
        'mode_cancel': "Ofbriechen",
        'mode_replace_text': "Text afügen",
        'mode_replace_cross': "Kräiz afügen",
        'mode_replace_signature': "Signatur afügen",
        'mode_replace_image': "Bild afügen",
        'mode_replace_form': "Form afügen",
        'mode_conflict_voice': "{0} Modus ass aktiv. Verloossen a Text afügen?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Textagab",
        'active_mode_signature': "Signatur",
        'active_mode_image': "Bild",
        'active_mode_form': "Form",
        'active_mode_and': " an ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Afügen",                    # Hauptmenü
        'insert_another_text': "Text afügen",          # Vereinfacht
        'insert_another_cross': "Kräiz afügen",        # Vereinfacht
        'insert_another_signature_1': "Signatur 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Signatur 2",      # Untermenü-Eintrag
        'insert_another_image': "Bild afügen",         # Vereinfacht
        'insert_another_form_rect': "Rechteck",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellips",        # Untermenü-Eintrag
        'insert_another_form_line': "Linn (2 Klicks)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Feil (2 Klicks)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} späicheren",
        'save_dialog_message': "{0} gëtt op Säit {1} gespäichert.\n\nWéi wëllt Dir virufueren?",
        'save_all': "All {0} späicheren",
        'save_single': "{0} späicheren",
        'save_customize': "{0} upassen",
        'save_discard': "Dës {0} verworf",
        'save_continue': "Weider beaarbechten",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Op Säit {0} sprangen",
        'context_rotate': " Säit {0} dréien",
        'context_delete': " Säit {0} läschen",
        'context_export': " Säit {0} exportéieren",
        'context_mark_as': " Säit markéieren als...",
        'context_mark_empty': " Eidel Säit",
        'context_unmark_empty': " Net méi eidel",
        'context_mark_export': " Fir Export markéieren",
        'context_unmark_export': " Net méi exportéieren",
        'context_batch_actions': " Sammelaktiounen",
        'context_batch_delete_empty': " All {0} eidel Säite läschen",
        'context_batch_export_single': " All {0} Säiten (ee Fichier)",
        'context_batch_export_split': " All {0} Säiten (getrennt)",
        'context_drag_start': " Drag & Drop starten",
        'context_drag_stop': " Drag & Drop ophalen",
        'context_insert': " Afügen",
        'context_insert_pages': " Säiten afügen",
        'context_zoom': "Zoom",
        'discard_mixed': "All {0} {1} an {2} {3} verworf",
        'save_mixed': "{0} {1} an {2} {3} späicheren",
        'discard_texts': "All {0} Texter verworf",
        'discard_text_single': "1 Text verworf",
        'save_texts': "{0} Texter späicheren",
        'save_text_single': "1 Text späicheren",
        'discard_crosses': "All {0} Kräizer verworf",
        'discard_cross_single': "1 Kräiz verworf",
        'save_crosses': "{0} Kräizer späicheren",
        'save_cross_single': "1 Kräiz späicheren",
        'discard_signatures': "All {0} Signature verworf",
        'save_signature_single': "1 Signatur späicheren",
        'save_signatures': "{0} Signature späicheren",
        'discard_images': "All {0} Biller verworf",
        'save_image_single': "1 Bild späicheren",
        'save_images': "{0} Biller späicheren",
        'discard_forms': "All {0} Formen verworf",
        'save_form_single': "1 Form späicheren",
        'save_forms': "{0} Forme späicheren",
        'cross_discard': "Dëst Kräiz verworf",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Export / Import Informatioun",
        'export_what': "📋 Wat gëtt exportéiert?",
        'export_general': "Allgemeng Astellungen",
        'export_general_items': "• Sproochausgab (un/aus, Vitesse)\n• Däischter/Liicht Modus\n• Backup-Astellungen\n• OCR-Astellungen",
        'export_image_form': "Bild- a Formen-Astellungen",
        'export_image_form_items': "• Bildastellungen (Säiteverhältnis, Standardgréisst)\n• Formen-Astellungen (Linnenstäerkt, Faarwen)\n• Signatur-Astellungen (Weeg, Gréissten, Zäitstempel)",
        'export_passwords': "Passwuert-Datebank",
        'export_passwords_items': "• All gespäichert PDF-Passwierder\n• Wahlweis verschlësselt oder entschlësselt",
        'export_master': "Master-Passwuert-Astellungen",
        'export_master_items': "• Master-Passwuert-Hash\n• Astellunge fir Signaturen/Textbausteng",
        'export_signatures': "Signaturen an Textbausteng",
        'export_signatures_items': "• All Bild-Fichieren (Ënnerschrëften)\n• All Textbausteng mat Formatéierungen\n• Privat/ëffentlech Markéierungen",
        'export_import_warning': "⚠️ Wichteg Hiweiser",
        'export_import_note': "• Beim Import ginn ALL aktuell Astellungen iwwerschriwwen\n• En Neistart vun der Applikatioun ass néideg\n• Bestoend Signaturen/Textbausteng ginn ersat",
        'export_master_note': "• Bei gesatem Master-Passwuert kënnt Dir wielen:\n  - Entschlësselt (Passwierder am Klartext)\n  - Verschlësselt (nëmme mam Master-PW liesbar)",
        'export_security': "• Déi exportéiert ZIP-Datei enthält vertraulech Donnéeën\n• Bewahrt se sécher op (z.B. verschlësselte USB-Stick)\n• Bei Verloscht vun der Datei: Passwierder fir ëmmer verluer",
        'export_format': "📁 Exportformat",
        'export_format_desc': "D'Astellunge ginn an enger eenzeger ZIP-Datei gespäichert:",
        'export_filename': "PDFDarkView_Astellungen_YYYYMMDD_HHMMSS.zip",
        'export_success': "Astellunge goufen erfollegräich exportéiert",
        'export_failed': "Export feelgeschloen",
        'export_import_question': "Wëllt Dir d'Applikatioun elo nei starten?",
        'export_password_question': "Et ass e Master-Passwuert gesat.\n\nWëllt Dir d'Passwierder entschlësselt exportéieren?\n(soss ginn se verschlësselt exportéiert)",
        'export_decrypt': "Entschlësselt exportéieren",
        'export_encrypt': "Verschlësselt exportéieren",

       # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Iwwer PDF Dark View",
        'info_version': "Versioun",
        'info_author': "Entwéckelt vum Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Iwwer",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ass en barrièrefräie PDF-Viewer, dee speziell fir Leit mat Sehbehënnerung entwéckelt gouf.</p>

            <p><strong>Käreigenschaften:</strong></p>
            <ul>
                <li>Kontrasträich, upassbar Uewerfläch</li>
                <li>Komplett Tastatursteierung</li>
                <li>Integréiert Sproochausgab</li>
                <li>OCR fir gescannt Dokumenter</li>
                <li>Ëmfangräich Bearbeitungswerkzeugen</li>
            </ul>

            <p>Méi wéi 50 Sprooche ginn ënnerstëtzt – fir datt PDFe fir jiddereen zougänglech sinn.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funktiounen",
        'info_features_intro': "PDF Dark View bitt Iech folgend Méiglechkeeten:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Unzeig & Navigatioun</strong> – Däischter/Liicht Modus, Säite bliederen, Zoom, Sprong op Säit</li>
            <li><strong>OCR (Texterkennung)</strong> – Gescannt Dokumenter duerchsicht- a kopéierbar maachen</li>
            <li><strong>Bearbeitung</strong> – Texter, Kräizer, Signaturen, Biller a Formen afügen</li>
            <li><strong>Säiteverwaltung</strong> – Läschen, extrahéieren, afügen, verréckelen per Drag & Drop</li>
            <li><strong>Export</strong> – An Word, Pages oder als Text</li>
            <li><strong>Sécherheet</strong> – Passwuertschutz a -verwaltung</li>
            <li><strong>Barrièrefräiheet</strong> – Sproochausgab, Tastatursteierung, héije Kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Bedienung",
        'info_accessibility': "♿ Barrièrefräiheet – komplett Tastatursteierung",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Allgemeng</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF opmaachen</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Sichen</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Däischter/Liicht Modus ëmschalten</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Drécken</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Ophieren</div>

        <div class="shortcut-cat">📖 Navigatioun</div>
        <div class="shortcut-row"><kbd>Pfeiltasten</kbd> Säit fir Säit bliederen</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Ginn op Säit</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Éischt Säit</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Lescht Säit</div>

        <div class="shortcut-cat">✏️ Bearbeitung</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Text afügen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Säite läschen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Säiten enthuelen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Säiten afügen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Säiten verréckelen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Säit dréinen</div>

        <div class="shortcut-cat">🖼️ Elementer verréckelen</div>
        <div class="shortcut-row"><kbd>Pfeiltasten</kbd> Text/Bild/Signatur verréckelen</div>
        <div class="shortcut-row"><kbd>Ctrl+Pfeiltasten</kbd> Gréisser Schrëtt</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Späicheren</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Verwerfen</div>

        <div class="shortcut-cat">🗣️ Sproochausgab</div>
        <div class="shortcut-row"><kbd>F2</kbd> Sproochausgab un/aus</div>
        """,
        'info_contextmenu': "📌 Wichteg: All Funktiounen sinn och iwwert d'Kontextmenü (riets Maustast) erreechbar!",
        'info_accessibility_hint': "💡 Tipp: D'Sproochausgab (F2) erliichtert d'Orientéierung a gëtt Feedback zu Menüen an Dialogen.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lizenz & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Angaben no § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Däitschland<br>
        E-Mail: binhdiez64@gmail.com<br>
        Verantwortlech fir den Inhalt: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Haftungsausschluss</strong><br>
        D'Software gouf mat gréisster Suergfalt entwéckelt. Eng Gewier fir d'Richtegkeet, Vollstännegkeet a Funktionalitéit gëtt net iwwerholl. D'Notzung geschitt op eegen Verantwortung.<br><br>

        <strong>📄 MIT-Lizenz (privaten Notzung)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Erlaabt: gratis Notzung, privat Ännerungen, perséinlech Kopien.<br>
        Net erlaabt: Verkaf, kommerziell Notzung, Entfernung vun Urheberrechtshinweisen.<br><br>

        <strong>🔧 Drëttubidder-Komponenten</strong><br>
        Dës Software enthält Komponenten ënner GPL, AGPL, Apache 2.0, BSD a MIT-Lizenzen.<br>
        Bei Weidergab musse déi respektiv Lizenzbedingunge agehale ginn.<br><br>

        <strong>🌐 Open Source</strong><br>
        De Quellcode ass disponibel a kann no de respektive Lizenzbedingungen aginn, geännert a weiderverbreet ginn.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Merci",
        'info_credits': "Merci un d'Open-Source-Communautéit",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-Verarbeitung</li>
            <li><strong>PyQt5</strong> – Grafesch Uewerfläch</li>
            <li><strong>Tesseract OCR</strong> – Texterkennung</li>
            <li><strong>OCRmyPDF</strong> – OCR-Integratioun</li>
            <li><strong>python-docx</strong> – Word-Export</li>
            <li><strong>qtawesome</strong> – Icons</li>
            <li><strong>DeepSeek</strong> – Ënnerstëtzung bei Iwwersetzungen (50+ Sproochen)</li>
            <li><strong>All Benotzer</strong> – Fir wäertvoll Feedback</li>
            <li><strong>Der Open-Source-Communautéit</strong> – Fir fantastesch Bibliothéiken</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Sproochen",
        'info_languages_header': "🌍 Sproochënnerstëtzung",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View ënnerstëtzt momentan <strong>62 Sproochen</strong> – fir datt d'Software weltwäit barrièrefräi ka benotzt ginn.</p>

            <p><strong>📖 Vollstänneg Sproochelëscht (Stand: Mäerz 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanesch (Shqip)</li>
                    <li>🇩🇿 Arabesch (العربية)</li>
                    <li>🇮🇩 Balinesesch (Basa Bali)</li>
                    <li>🇧🇩 Bengalesch (বাংলা)</li>
                    <li>🇲🇲 Birmanesch (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnesch (Bosanski)</li>
                    <li>🇧🇬 Bulgaresch (Български)</li>
                    <li>🇨🇳 Chinesesch (中文)</li>
                    <li>🇩🇰 Dänesch (Dansk)</li>
                    <li>🇩🇪 Däitsch (Deutsch)</li>
                    <li>🇬🇧 Englesch (English)</li>
                    <li>🇪🇪 Estnesch (Eesti)</li>
                    <li>🇫🇮 Finnesch (Suomi)</li>
                    <li>🇫🇷 Franséisch (Français)</li>
                    <li>🇬🇷 Griichesch (Ελληνικά)</li>
                    <li>🇮🇱 Hebräesch (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatesch (Hrvatski)</li>
                    <li>🇭🇺 Ungaresch (Magyar)</li>
                    <li>🇮🇩 Indoneesesch (Bahasa Indonesia)</li>
                    <li>🇮🇪 Iresch (Gaeilge)</li>
                    <li>🇮🇸 Islännesch (Íslenska)</li>
                    <li>🇮🇹 Italieenesch (Italiano)</li>
                    <li>🇯🇵 Japanesch (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreanesch (한국어)</li>
                    <li>🇱🇦 Laotesch (ພາສາລາວ)</li>
                    <li>🇱🇻 Lettesch (Latviešu)</li>
                    <li>🇱🇹 Litauesch (Lietuvių)</li>
                    <li>🇱🇺 Lëtzebuergesch (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaiesch (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolesch (Монгол)</li>
                    <li>🇳🇵 Nepalesesch (नेपाली)</li>
                    <li>🇳🇱 Hollännesch (Nederlands)</li>
                    <li>🇳🇴 Norwegesch (Norsk)</li>
                    <li>🇦🇫 Paschtu (پښتو)</li>
                    <li>🇮🇷 Persesch (فارسی)</li>
                    <li>🇵🇱 Polnesch (Polski)</li>
                    <li>🇵🇹 Portugisesch (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumänesch (Română)</li>
                    <li>🇷🇺 Russesch (Русский)</li>
                    <li>🇸🇪 Schweedesch (Svenska)</li>
                    <li>🇷🇸 Serbesch (Српски)</li>
                    <li>🇸🇰 Slowakesch (Slovenčina)</li>
                    <li>🇸🇮 Sloweenesch (Slovenščina)</li>
                    <li>🇪🇸 Spuenesch (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thailännesch (ไทย)</li>
                    <li>🇨🇿 Tschechesch (Čeština)</li>
                    <li>🇹🇷 Tierkesch (Türkçe)</li>
                    <li>🇺🇦 Ukrainesch (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamesesch (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddesch (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Eege Sproochen dobäisetzen:</strong><br>
                Wëllt Dir eng Sprooch, déi nach net dobäi ass? Setzt einfach Är eege Wierderbuch-Datei (<code>sprache_xx.py</code>) nieft der Applikatioun – d'Software erkennt se automatesch. Wann Dir un enger spezieller Iwwersetzung interesséiert sidd, kontaktéiert mech gerne.
            </div>

            <p><strong>🙏 Besonneschen Dank:</strong> DeepSeek fir d'Ënnerstëtzung bei der Iwwersetzung vun all Wierderbicher an 62 Sproochen.</p>

            <p>📧 Kontakt fir Iwwersetzungen: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Feeler",
        'error_occurred': "Et ass e Feeler opgetrueden",
        'error_pdf_load': "Feeler beim Luede vum PDF",
        'error_pdf_save': "Feeler beim Späichere vum PDF",
        'error_ocr': "Feeler bei der Texterkennung",
        'error_no_pdf': "Kee PDF gelueden",
        'error_page_not_found': "Säit net fonnt",
        'error_invalid_range': "Ongültege Säiteberäich",
        'error_file_not_found': "Fichier net fonnt",
        'error_permission': "Keng Berechtegung",
        'error_unknown': "Onbekannte Feeler",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Erfolleg",
        'success_operation': "Virgang erfollegräich ofgeschloss",
        'success_saved': "Erfollegräich gespäichert",
        'success_exported': "Erfollegräich exportéiert",
        'success_imported': "Erfollegräich importéiert",
        'success_deleted': "Erfollegräich geläscht",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Bestätegung",
        'confirm_yes': "Jo",
        'confirm_no': "Neen",
        'confirm_ok': "OK",
        'confirm_cancel': "Ofbriechen",
        'confirm_delete': "Läschen",
        'confirm_overwrite': "Iwwerschreiwen",
        'confirm_continue': "Virfueren",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF gëtt gelueden...",
        'progress_saving': "PDF gëtt gespäichert...",
        'progress_exporting': "PDF gëtt exportéiert...",
        'progress_processing': "Verschaffung leeft...",
        'progress_wait': "Waart w.e.g...",
        'progress_preparing': "Virbereedung...",
        'progress_finalizing': "Finaliséierung...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Wäiss",
        'color_black': "Schwaarz",
        'color_red': "Rout",
        'color_green': "Gréng",
        'color_blue': "Blo",
        'color_yellow': "Giel",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Orange",
        'color_gray': "Gro",
        'color_custom': "Faarwauswiel",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fichier",
        'menu_edit': "&Beaarbechten",
        'menu_view': "&Usiicht",
        'menu_tools': "&Extras",
        'menu_settings': "&Astellungen",
        'menu_help': "&Hëllef",
        'menu_language': "🌐 Sprooch",
        'menu_guides': "&Uleedungen",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Opmaachen",
        'file_save_as': "&Späicheren ënner...",
        'file_protect': "Dokument &schützen...",
        'file_export': "&Exportéieren",
        'file_export_pages': "Als Pages exportéieren",
        'file_export_word': "Als DOCX exportéieren",
        'file_export_text': "Als TXT exportéieren",
        'file_print_now': "&Direkt drécken",
        'file_print': "&Drécken",
        'file_close': "&Zoumaachen",
        'file_quit': "&Verloossen",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Sichen",
        'edit_ocr': " OCR ausféieren",
        'edit_rotate': "Säit &dréien",
        'edit_rotate_all': "&All Säiten dréien",
        'edit_delete_pages': "Säiten &läschen",
        'edit_extract_pages': "Säiten &eraushuelen",
        'edit_insert_pages': "Säiten &afügen",
        'edit_move_pages': "Säiten &réckelen",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Text a Kräizer afügen",
        'text_insert': " Text afügen",
        'cross_insert': " Kräiz afügen",
        'text_customize': " Text upassen",
        'cross_customize': " Dëst Kräiz upassen",
        'cross_customize_all': " All Kräizer upassen",
        'text_discard': " Dësen Text / Kräiz verworf",
        'text_discard_all': " All Texter a Kräizer verworf",
        'text_save_all': " All Texter a Kräizer späicheren",
        'text_guide': " Textagab / Textbausteng - Uleedung",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Ënnerschrëft afügen",
        'signature_settings_menu': " Astellungen...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Bild afügen",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Formen afügen",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Textfënster weisen",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Säitebreet (Standard)",
        'view_zoom_two': "&Zwee Säiten",
        'view_zoom_overview': "&Iwwersiicht (méi Säiten)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Bedienungshëllefen",
        'settings_voice': "Sproochausgab",
        'settings_voice_tooltip': "ergänzt d'Sproochausgab vu Screenreader mat zousätzlechen Informatiounen",
        'settings_signature': "&Signatur-Astellungen",
        'settings_password': "&Passwuertverwaltung",
        'settings_backup': "Backup virun Ännerungen uginn",
        'settings_export_import': "&Astellungen exportéieren / importéieren",
        'settings_export': "&All Astellungen exportéieren...",
        'settings_import': "&All Astellungen importéieren...",
        'settings_export_info': "&Wat gëtt exportéiert?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "un",
        'voice_off': "aus",
        'voice_toggle': "Sproochausgab {0}",
        'voice_speed': "Vitesse op {0} Prozent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Tool net fonnt:\n{0}\n\nBASE_DIR: {1}\nStellt sécher, datt d'PDF-Tools am Dossier {1} installéiert sinn.",
        'tool_started': "{0} gestart",
        'tool_start_failed': "Konnt net gestart ginn",
        'process_error_failed_to_start': "Prozess konnt net gestart ginn. Ass de Fichier do?",
        'process_error_crashed': "Prozess ofgestierzt während dem Start.",
        'process_error_timeout': "Prozess-Timeout erreecht.",
        'process_error_write': "Schreiffeeler beim Prozess.",
        'process_error_read': "Liesenfeeler beim Prozess.",
        'process_error_unknown': "Onbekannte Prozess-Feeler",
        'process_command': "Kommando",
        'process_normal_exit': "normal ofgeschloss",
        'process_crashed': "ofgestierzt",
        'process_nonzero_exit': "{0} gouf mat Feelercode {1} ofgeschloss",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Gëtt ofgebrach...",
        'move_cancelling': "Réckele gëtt ofgebrach",
        'opening_pdf': "PDF gëtt opgemaach...",
        'loading_document': "Lued Dokument...",
        'pdf_opened': "PDF opgemaach",
        'pages_found_moving': "{0} Säite fonnt, {1} fir ze réckelen",
        'creating_backup': "Erstelle Backup...",
        'backup_description': "Originaldatei sécheren...",
        'backup_saved_as': "Gespäichert als: {0}",
        'error_format': "Feeler: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Sich zréckgesat",
        'page_header_simple': "=== Säit {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Passwuertverwaltung – Uleedung",
        'password_guide_voice': "Uleedung zur Passwuertverwaltung. Liest w.e.g. d'Hiweiser.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Passwuertverwaltung – Ausféierlech Uleedung</strong></p>

        <p><strong>1. Passwuertschutz fir PDFen</strong></p>
        <ul>
        <li>Beim Opmaache vun engem passwuertgeschützte PDF erschéngt en Dialog, wou Dir d'Passwuert aginn kënnt.</li>
        <li>Dir kënnt d'Passwuert verschlësselt späicheren, fir datt Dir et net all Kéier nei aginn musst (Checkbox „Passwuert späicheren“).</li>
        <li>Mat dem Knäppchen „Passwuert ewechhuelen“ kënnt Dir eng entschlësselt Kopie vum PDF erstellen an d'Passwuert aus der Datebank läschen.</li>
        </ul>

        <p><strong>2. Master-Passwuert</strong></p>
        <ul>
        <li>D'Master-Passwuert schützt den Zougrëff op all gespäichert PDF-Passwierder.</li>
        <li><strong>Ariichten:</strong> Gitt op „Astellungen → Passwuertverwaltung → Master-PW Astellungen“ a klickt op „Master-Passwuert ariichten“. Wielt e séchert Passwuert (mindestens 8 Zeechen).</li>
        <li><strong>Änneren:</strong> No erfollegräicher Authentifizéierung kënnt Dir d'Master-Passwuert änneren.</li>
        <li><strong>Ewechhuelen:</strong> Wann Dir d'Master-Passwuert läscht, ginn ALL gespäichert Passwierder onwiderrëfflech geläscht. Dir kënnt virdrun eng Sécherung exportéieren.</li>
        <li>Eemol pro Sëtzung musst Dir Iech mam Master-Passwuert authentifizéieren, fir op geschützt Funktiounen (z.B. Weise vu Passwierder) zougräifen ze kënnen.</li>
        </ul>

        <p><strong>3. Passwuertverwaltung (Lëscht)</strong></p>
        <ul>
        <li>Ënner „Astellungen → Passwuertverwaltung“ mécht sech eng Tabell vun alle gespäicherte PDFen mat hiren verschlësselte Passwierder op.</li>
        <li><strong>Ouni Master-Passwuert:</strong> Dir kënnt nëmmen Andr</li></ul></body></html>"""
        ,  # Komma nicht vergessen!

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Invertéierungsmodus",
        'invert_mode_classic': "Klassesch (all Faarwen invertéieren)",
        'invert_mode_smart': "Intelligent (nëmmen d'Helligkeet invertéieren)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Graustufen-Schwellwert",
        'gray_threshold_10': "10% (streng)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (mëll)",
        'threshold_changed': "Schwellwert op {0}% gesat",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Graustufen-Schwellwert – Erklärung",
        'threshold_guide_text': "De Graustufen-Schwellwert bestëmmt, wéi eng Pixel am intelligente Dark Mode als 'gro' gëllen an invertéiert ginn.\n\n"
                                "• E niddrege Wäert (10%) invertéiert nëmme bal perfekt Grohéin – faarweg Elementer bleiwe komplett erhalen.\n"
                                "• E héije Wäert (50%) invertéiert och liicht faarweg Pixel – dat erhéicht de Kontrast, kann awer Faarwe verfälschen.\n\n"
                                "Den optimale Wäert hänkt vum Dokument of. Fir reng Textdokumenter ass 30–40% dacks ideal, fir faarweg Grafike léiwer 10–20%.\n\n"
                                "Dir kënnt de Wäert all Moment iwwert d'Menü 'Astellungen' upassen – d'PDF gëtt dann direkt nei gelueden.\n\n"
                                "Beuecht:\n* Fotoen a Biller kënnen nëmmen am Light Mode korrekt ugewise ginn!\n* D'Invertéierungsastellunge ginn nëmmen ugewis, wann den Dark Mode aktivéiert ass.",
        'threshold_guide_voice': "De Graustufen-Schwellwert bestëmmt, wéi staark den intelligente Dark Mode ageet. En niddrege Wäert schount Faarwen, en héijen erhéicht de Kontrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF gëtt opgemaach...",
        'progress_loading_document': "Lued Dokument...",
        'progress_pdf_opened': "PDF opgemaach",
        'progress_creating_backup': "Erstelle Backup...",
        'progress_backup_description': "Sécher Originaldatei...",
        'progress_backup_created': "Backup erstallt",
        'progress_backup_saved_as': "Gespäichert als: {0}",
        'progress_analyzing_start': "Start Analyse...",
        'progress_searching_empty': "Sich eidel Säiten...",
        'progress_page_empty': "Säit {0} ass eidel",
        'progress_page_keep': "Säit {0} behalen",
        'progress_analysis_complete': "Analyse ofgeschloss",
        'progress_empty_found': "{0} eidel Säite fonnt",
        'progress_current_page': "Aktuell Säit",
        'progress_mark_delete': "Gëtt geläscht markéiert",
        'progress_range_selected': "Säitenberäich {0}-{1}",
        'progress_deleting_pages': "Läschen {0} Säiten",
        'progress_creating_new_pdf': "Erstellt nei PDF...",
        'progress_transferring_pages': "Iwwerdroen Säiten",
        'progress_keeping_page': "Säit {0} gëtt behalen ({1}/{2})",
        'progress_saving_pdf': "Späichert PDF...",
        'progress_optimizing': "Optiméiert Dateigréisst...",
        'progress_finalizing': "Finaliséiert...",
        'progress_new_size': "Nei Gréisst: {0:.2f} MB",
        'progress_cancelling': "Gëtt ofgebrach...",
        'progress_cancel_message': "{0} gëtt ofgebrach",
        'progress_pages_found_moving': "{0} Säite fonnt, {1} fir ze verréckelen",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF gëtt analyséiert...",
        'ocr_status_optimizing': "Bildoptiméierung leeft...",
        'ocr_status_recognizing': "Texterkennung an Aarbecht...",
        'ocr_status_embedding': "Text gëtt agebaut...",
        'ocr_status_finalizing': "Finaliséierung vum PDF...",

        # PDF-Laden
        'progress_preparing': "Virbereedung...",
        'progress_loading': "PDF gëtt gelueden...",

        # Seitenoperationen
        'progress_deleting_title': "Säite läschen...",
        'progress_moving_title': "Säite verréckelen...",
        'pages_found': "Säite fonnt",
        'progress_creating_new_order': "Erstellt nei Reiefolleg...",
        'progress_sorting_pages': "Sortéiert Säiten...",
        'progress_moving_to_begin': "Verréckelt {0} Säiten un den Ufank",
        'progress_transferring_count': "Iwwerdroen {0} Säiten",
        'progress_transferring_before_target': "Iwwerdroen Säiten virum Zil",
        'progress_moving_pages': "Verréckelt {0} Säiten",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_geschützt_",
        'filename_copy_suffix': "_Kopie",
        'filename_page_single': "_Säit_",
        'filename_page_range': "_Säiten_",
        'filename_export_page': "_Säit_{0:03}",
        'filename_export_range': "_Säiten_{0}-{1}",
        'filename_export_multiple': "_Säiten_{0}",
        'filename_with_text': "_mat_Text",
        'filename_with_signature': "_mat_Ënnerschrëft",
        'filename_with_image': "_mat_Bild",
        'filename_with_forms': "_mat_Formen",
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
        'view_toggle_navbar': "Butteläischt uweisen",
		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Et kënnen net all Säiten geläscht ginn",
		'pages_cannot_delete_last_page': 'Déi lescht Säit kann net geläscht ginn!',
		'pages_cannot_delete_all_pages': 'Et muss mindestens eng Säit am Dokument bleiwen!',
		'delete_pages_confirm': 'Sidd Dir sécher datt Dir {0} Säite läsche wëllt?',
		'delete_pages_confirm_voice': 'Sidd Dir sécher datt Dir {0} Säite läsche wëllt?',
		'pages_deleted': '{0} Säite goufen erfollegräich geläscht.',
		'warning': 'Warnung',
		'error': 'Feeler',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Keng Form ausgewielt",
        'form_customized': "Form ugepasst",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Auswielen",
        'btn_use': "Benotzen",
        'master_password_for_spasswords': "Fir Passwierder ze späicheren an ze benotzen, muss fir d'éischt e Master-Passwuert ageriicht ginn.\n\nWëllt Dir elo d'Master-Passwuert ariichten?",
        'open_saved_dialog_title': "Gespäichert Fichier opmaachen",
        'open_saved_question': "Wëllt Dir de gespäicherte Fichier elo opmaachen?",
        'password': "Passwuert",
        'password_manager_master_required': "De Passwuert-Manager ass nëmme verfügbar wann e Master-Passwuert ageriicht gouf.\n\nWëllt Dir elo d'Master-Passwuert ariichten?",
        'password_master_required_for_select': "Fir gespäichert Passwierder unzeweisen an auszewielen, musst Dir Iech fir d'éischt mat Ärem Master-Passwuert authentifizéieren.\n\nWëllt Dir Iech elo authentifizéieren?",
        'password_not_available': "Dat ausgewielte Passwuert ass net verfügbar oder konnt net entschlësselt ginn.",
        'password_options_title': "Passwuert-Optiounen",
        'password_save_choice_change': "Neit Passwuert festleeën",
        'password_save_choice_keep': "Besteet Passwuert benotzen",
        'password_save_choice_none': "Onverschlësselt späicheren",
        'password_save_hint': "Richt fir d'éischt e Master-Passwuert an fir Passwierder sécher ze späicheren.",
        'password_save_master_required': "Passwuert späicheren (nëmme mat Master-Passwuert méiglech)",
        'password_save_question': "Den aktuelle PDF ass mat engem Passwuert geschützt. Wëllt Dir dat bestoend Passwuert benotzen, en neit festleeën oder onverschlësselt späicheren?",
        'password_select': "Passwuert auswielen",
        'password_select_none': "Kee Passwuert ausgewielt.\n\nWielt w.e.g. e Passwuert aus der Lëscht aus.",
        'password_select_one': "Wielt w.e.g. genee eent Passwuert aus.\n\nDir hutt méi Passwierder markéiert.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_backup",
        'filename_insert_suffix': "_mat_asetzung",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_säiten_geläscht",
        'filename_pages_moved': "_säiten_verréckelt",
        'filename_rotated_all_suffix': "_all_säiten_gedréint",
        'filename_rotated_suffix': "_säit_gedréint",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfiguratioun vun den Nimm vu Fichieren bei Ännerunge vum PDF",
        'filename_keep_suffixes': "Vireg Extensiounen (z.B. _mat_Text) bäibehalen",
        'filename_keep_suffixes_false': "Ersetzen",
        'filename_keep_suffixes_true': "Bäibehalen",
        'filename_preview_label': "Virschau vum Fichiersnumm:",
        'filename_preview_overwrite_hint': "Virschau net verfügbar – den Original gëtt iwwerschriwwen.",
        'filename_separator': "Trennszeechen tëscht de Wierder",
        'filename_separator_none': "Keen Trennszeechen",
        'filename_separator_space': "Raum ( )",
        'filename_separator_underscore': "Ënnersträich (_)",
        'filename_settings_saved': "Astellungen zum Fichiersnumm gespäichert",
        'filename_settings_title': "Fichiersnumm-Formatéierung a Backup",
        'filename_timestamp_position': "Positioun vum Zäitstempel",
        'filename_timestamp_position_after': "Noum Basisnumm",
        'filename_timestamp_position_before': "Ganz vir",
        'filename_timestamp_position_end': "Um Enn",
        'filename_use_timestamp': "Zäitstempel benotzen",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Verhale bei Ännerungen:</b><ul><li>Läschen an Asetze vu Säiten</li><li>Asetze vun Text, Ënnerschrëft, Bild a Formen</li><li>OCR</li></ul></html>",
        'backup_section': "Backup fir Säiten-Operatiounen (Läschen, Verréckelen)",
        'behavior_info': "Hinweis: Bei 'Original iwwerschreiwen' ginn Zäitstempel a Suffixen ignoréiert – de Fichier behält säin Numm.",
        'behavior_new_file': "Ëmmer neie Fichier erstellen (mat Zäitstempel a Suffix)",
        'behavior_overwrite': "Original iwwerschreiwen (kee neie Fichier)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "All Säite goufen gedréint.\n\nDen Original ass onverännert bliwwen.\nNeie Fichier: {0}",
        'all_pages_rotated_voice': "All Säite gedréint, neie Fichier erstallt.",
        'empty_pages_deleted_new_file': "{0} eidel Säite goufe geläscht.\n\nDen Original ass onverännert bliwwen.\nNeie Fichier: {1}",
        'empty_pages_deleted_voice': "{0} eidel Säite geläscht, neie Fichier erstallt.",
        'ocr_keep_original': "Original bäibehalen (spéider manuell opmaachen)",
        'ocr_new_file_question': "Den neien duerchsichtbare PDF gouf gespäichert ënner:\n{0}\n\nWëllt Dir en elo opmaachen?",
        'ocr_open_new': "Neien OCR-Fichier opmaachen",
        'ocr_original_kept': "Den Originalfichier bleift op. Den OCR-Fichier gouf gespäichert.",
        'page_deleted_new_file': "Säit {0} gouf geläscht.\n\nDen Original ass onverännert bliwwen.\nNeie Fichier: {1}",
        'page_deleted_voice': "Säit {0} geläscht, neie Fichier erstallt.",
        'page_rotated_new_file': "Säit {0} gouf gedréint.\n\nDen Original ass onverännert bliwwen.\nNeie Fichier: {1}",
        'page_rotated_voice': "Säit {0} gedréint, neie Fichier erstallt.",
        'pages_deleted_new_file': "Et goufen {0} Säite geläscht.\n\nDen Originalfichier ass onverännert bliwwen.\nNeie Fichier: {1}",
        'pages_deleted_new_file_voice': "{0} Säite geläscht, neie Fichier erstallt.",
        'pages_inserted_new_file': "Et goufen {0} Säiten agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nNeie Fichier: {1}",
        'pages_inserted_new_file_ask': "Et goufen {0} Säiten agesat.\n\nDen Original ass onverännert bliwwen.\nNeie Fichier: {1}\n\nWëllt Dir en elo opmaachen?",
        'pages_inserted_voice_new': "{0} Säiten agesat, neie Fichier erstallt.",
        'pages_moved_new_file': "Et goufen {0} Säite verréckelt.\n\nDen Originalfichier ass onverännert bliwwen.\nNeie Fichier: {1}",
        'pages_moved_new_file_voice': "{0} Säite verréckelt, neie Fichier erstallt.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Net méi weisen",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Backup-Astellung</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Backup UN</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Bei all Ännerungen, déi den Original iwwerschreiwen</strong> (Text, Ënnerschrëft, Bild, Form, OCR, dréinen, asetzen, Säiten läschen/verréckelen) gëtt <strong>automatesch e Backup mat Zäitstempel</strong> erstallt, ier d'Ännerung ugewannt gëtt.</p>
                <p style="margin: 5px 0 5px 20px;">• De Backup läit niewent dem Originalfichier (z.B. <code>Dokument_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Wann Dir zousätzlech d'Optioun <strong>„Original iwwerschreiwen“</strong> aktivéiert hutt, gëtt och e Backup erstallt.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Backup AUS</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Et gëtt kee Backup erstallt</strong> – weder beim Iwwerschreiwen nach bei Säiten-Operatiounen.</p>
                <p style="margin: 5px 0 5px 20px;">• Den Originalfichier kann beim Iwwerschreiwen onwiderrufflech verluer goen.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Nëmme fir erfuerene Benotzer recommandéiert!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tipp:</strong> D'Backup-Astellung ass onofhängeg vun der Optioun „Original iwwerschreiwen“. Dir kënnt béid kombinéieren.<br>
                Dir kënnt dës Meldung dauerhaft verstoppen.
            </div>
        </div>
        """,
        'backup_info_title': "Backup-Verhalen",
        'backup_info_voice': "Hiweis zum Backup-Verhalen bei Säiten-Operatiounen. Backup un iwwerschreift Original, Backup aus erstellt neie Fichier.",
        'show_backup_info': "Info zur Backup-Astellung",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Net méi weisen",
        'overwrite_enable_backup': "Backup aktivéieren (recommandéiert)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Original iwwerschreiwen</p>
            <p>Wann Dir dës Optioun aktivéiert, ginn Ännerungen (Text, Ënnerschrëft, Bild, Form, OCR, dréinen, asetzen) <strong>direkt am Original gespäichert</strong> – et gëtt <strong>kee neie Fichier</strong> erstallt.</p>
            <p>• Den Numm vum Fichier bleift onverännert.<br>
            • Zäitstempel a Suffixe ginn ignoréiert.<br>
            • <strong>Ouni Backup kann den Original onwiderrufflech verluer goen.</strong></p>
            <p style="color: #FFD700;">Recommandatioun: Aktivéiert zousätzlech d'Backup-Optioun fir automatesch Sécherheetskopien ze kréien.</p>
        </div>
        """,
        'overwrite_info_title': "Original iwwerschreiwen",
        'overwrite_info_voice': "Opgepasst: Original iwwerschreiwen – keen neie Fichier. Backup recommandéiert.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Et goufen {0} Säiten agesat.\n\nDen Originalfichier gouf iwwerschriwwen.\nEt gouf e Backup erstallt.",
        'pages_inserted_overwrite_no_backup': "Et goufen {0} Säiten agesat.\n\nDen Originalfichier gouf iwwerschriwwen.\nEt gouf KEEN Backup erstallt.",
        'texts_saved_overwrite_with_backup': "D'Ännerunge goufen am Original gespäichert.\n\nEt gouf e Backup erstallt.",
        'texts_saved_overwrite_no_backup': "D'Ännerunge goufen am Original gespäichert.\n\nEt gouf KEEN Backup erstallt.",
        'texts_crosses_saved_new_file': "{0} {1} an {2} {3} goufen agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nEt gouf en neie Fichier erstallt.\n\nDen neie PDF gëtt gelueden...",
        'texts_saved_new_file': "{0} {1} goufen agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nEt gouf en neie Fichier erstallt.\n\nDen neie PDF gëtt gelueden...",
        'crosses_saved_new_file': "{0} {1} goufen agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nEt gouf en neie Fichier erstallt.\n\nDen neie PDF gëtt gelueden...",
        'elements_saved_new_file': "{0} Elementer goufen agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nEt gouf en neie Fichier erstallt.\n\nDen neie PDF gëtt gelueden...",
        'signatures_saved_overwrite_with_backup': "D'Ënnerschrëft(en) gouf(en) am Original gespäichert.\n\nEt gouf e Backup erstallt.",
        'signatures_saved_overwrite_no_backup': "D'Ënnerschrëft(en) gouf(en) am Original gespäichert.\n\nEt gouf KEEN Backup erstallt.",
        'images_saved_overwrite_with_backup': "D'Bild(er) gouf(en) am Original gespäichert.\n\nEt gouf e Backup erstallt.",
        'images_saved_overwrite_no_backup': "D'Bild(er) gouf(en) am Original gespäichert.\n\nEt gouf KEEN Backup erstallt.",
        'forms_saved_overwrite_with_backup': "D'Form(en) gouf(en) am Original gespäichert.\n\nEt gouf e Backup erstallt.",
        'forms_saved_overwrite_no_backup': "D'Form(en) gouf(en) am Original gespäichert.\n\nEt gouf KEEN Backup erstallt.",
        'signatures_saved_new_file': "{0} Ënnerschrëfte goufen agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nEt gouf en neie Fichier erstallt.\n\nDen neie PDF gëtt gelueden...",
        'images_saved_new_file': "{0} Biller goufen agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nEt gouf en neie Fichier erstallt.\n\nDen neie PDF gëtt gelueden...",
        'forms_saved_new_file': "{0} Formen goufen agesat.\n\nDen Originalfichier ass onverännert bliwwen.\nEt gouf en neie Fichier erstallt.\n\nDen neie PDF gëtt gelueden...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Opgepasst: Dëse PDF enthält gedréint Säiten. D'Positionéierung kéint ofwäichen.",
        'page_rotated_warning_title': "Gedréint Säit erkannt",
        'page_rotated_warning_message': "Déi aktuell Säit {0} ass ëm {1}° gedréint.\n\nD'Asetze vun Elementer op gedréint Säite gëtt net ënnerstëtzt.\n\nWëllt Dir d'Säit elo an déi oprecht Positioun dréinen?",
        'page_rotated_warning_voice': "Opgepasst: D'Säit ass gedréint. Dréint se w.e.g. fir d'éischt.",
        'paste_on_rotated_page_simple_warning': "Asetzen op Säit {0} net méiglech!\n\nDës Säit ass ëm {1}° gedréint.\n\nDréint w.e.g. fir d'éischt d'Säit op 0° (Menü: Änneren → Säit ausriichten).\n\nOpgepasst:\nDat viregt kopéiert Element geet verluer, wann Dir net späichert ier Dir d'Säit dréint.",
        'paste_on_rotated_page_voice': "Asetzen ofgebrach. D'Säit ass gedréint. Riicht d'Säit w.e.g. fir d'éischt aus.",
        'page_rotated_cancel': "Ofbriechen",
        'page_rotated_rotate_until_upright': "Säit widderholl dréinen (bis oprecht)",
        'page_rotated_now_upright': "D'Säit ass elo oprecht. Dir kënnt elo asetzen.",
        'page_rotated_still_not_upright': "D'Säit konnt net an déi oprecht Positioun gedréint ginn. Korrigéiert w.e.g. manuell.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hëllef: Gedréint Säite korrigéieren",
        'help_rotated_pages_voice': "Hëllef fir d'Korrigéiere vu gedréinte Säite gëtt opgemaach.",
        'btn_help': "Hëllef",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Gedréint Säit – Asetze funktionéiert net richteg</p>

            <p>Wann d'Asetze vun Texter, Ënnerschrëften oder Formen op enger gedréinter Säit net richteg funktionéiert, kënnt Dir d'Säit mat engem externe PDF-Editor korrigéieren.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Léisung mat engem externe Tool (z.B. macOS Virschau)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Säit exportéieren</strong><br>
                &nbsp;&nbsp;Klickt am Menü op <strong>Fichier → Als Säiten exportéieren</strong> oder benotzt eng aner Method fir déi gewënschte Säit als eenzelen PDF ze späicheren.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Säit am externe Programm opmaachen</strong><br>
                &nbsp;&nbsp;Maacht den exportéierte PDF an engem PDF-Editor op (z.B. <strong>macOS Virschau</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Säit dréinen</strong><br>
                &nbsp;&nbsp;Dréint d'Säit sou datt se oprecht steet (an der Virschau: <strong>Geschir → Dréinen</strong> oder <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Späicheren</strong><br>
                &nbsp;&nbsp;Späichert déi korrigéiert Säit (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Säit erëm an den Originaldokument asetzen</strong><br>
                &nbsp;&nbsp;Gitt zréck op PDFDarkView a setzt déi korrigéiert Säit op déi gewënscht Positioun an:<br>
                &nbsp;&nbsp;<strong>Änneren → Säiten asetzen</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativ: Säit am Original dréinen</p>
                <p style="margin: 5px 0 5px 20px;">• Benotzt déi agebaute Dréinfunktioun (<strong>Änneren → Säit dréinen</strong>) fir d'Säit schrëttweis ze korrigéieren.<br>
                • No all Dréiung kënnt Dir prüfen, ob d'Asetze elo funktionéiert.<br>
                • Dëst ass dacks déi méi séier Léisung – probéiert et fir d'éischt!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tipp:</strong> Wann Dir dacks op gedréint Säite stéisst, kënnt Dir d'Warnung am Asetz-Dialog dauerhaft verstoppen.<br>
                D'Positionéierung kann dann awer ofwäichen – benotzt dës Optioun nëmme wann Dir d'Auswierkunge kennt.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Säiten ausriichten",
        'menu_rotate_normalize_tooltip': "Säit dréinen oder op 0° zrécksetzen",
        'normalize_current_page': "Aktuell Säit an déi oprecht Positioun bréngen (op 0° setzen)",
        'normalize_all_pages': "All Säiten an déi oprecht Positioun bréngen (op 0° setzen)",
        'page_normalized': "Säit {0} gouf an déi oprecht Positioun gesat.",
        'all_pages_normalized': "All Säite goufen an déi oprecht Positioun gesat.",
        'page_already_upright': "Säit {0} ass scho oprecht.",
        'all_pages_already_upright': "All Säite si scho oprecht.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>De PDF enthält keen duerchsichtbaren Text.</p><p>Wëllt Dir OCR duerchféieren, fir op {0} z'exportéieren?</p>",
        'export_ocr_voice': "De PDF enthält keen Text. OCR noutwendeg fir den Export op {0}.",
        'export_no_ocr_possible': "Export ouni OCR net méiglech. Féiert w.e.g. OCR iwwert de Menü aus.",
        'ocr_failed_export_not_possible': "OCR feelgeschloen. Export kann net duerchgefouert ginn.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "De PDF gëtt an der Virschau opgemaach. Start w.e.g. den Dréckprozess do.",
        'print_preview_manual': "De PDF gouf opgemaach. Féiert w.e.g. den Dréckbefehl manuell aus (z.B. Strg+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDFs zesummeféieren",
        'merge_pdfs': "PDFs zesummeféieren",
        'merge_progress_title': "PDFs ginn zesummegeluecht...",
        'merge_pdfs_list': "PDFs an der Reiefolleg (Drag & Drop fir ze sortéieren)",
        'merge_add_pdf': "PDF derbäisetzen",
        'merge_remove': "Ewechhuelen",
        'merge_move_up': "No uewen",
        'merge_move_down': "No ënnen",
        'merge_pdfs_info': "💡 Tipp: Dir kënnt d'Reiefolleg per Drag & Drop änneren",
        'merge_no_pdfs': "Keng PDFs ausgewielt. Klickt op 'PDF derbäisetzen'.",
        'merge_info': "{0} PDFs ausgewielt (ongeféier {1} Säiten)",
        'merge_open_file': "Fichier opmaachen",
        'merge_merge': "Zesummeféieren",
        'merge_error': "Feeler beim Zesummeféieren",
        'merge_min_two_pdfs_error': "Wielt w.e.g. mindestens zwee PDF-Fichieren aus fir zesummenzeféieren.",
        'merge_select_pdfs': "PDFs auswielen fir zesummenzeféieren",
        'merge_error_file': "Feeler bei der Veraarbechtung",
        'merge_cancelled': "Zesummeféieren gouf ofgebrach",
        'merge_preparing': "Virbereedung...",
        'merge_processing': "Verafft PDF {0} vu(n) {1}",
        'merge_saving': "Späichert zesummegeféierten PDF...",
        'merge_complete': "Fäerdeg!",
        'merge_success_title': "Zesummeféieren erfollegräich",
        'merge_success_voice': "{0} PDFs goufen erfollegräich zesummegeféiert.",
        'merge_success_message': "{0} PDFs goufen erfollegräich zesummegeféiert.\n\nDat neit Dokument huet elo {1} Säiten.\n\nNeie Fichier:\n{2}\n\nSpäicherplaz:\n{3}\n{2}\n\nWëllt Dir dëse PDF opmaachen?",
        'replace_file_title': "Fichier ersetzen?",
        'replace_file_message': "Et ass schonn e PDF op. Wëllt Dir en duerch den neie Fichier ersetzen?",
        'btn_yes': "Jo",
        'btn_no': "Neen",
        'filename_merge_suffix': "zesummegeféiert",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Maacht {0} op...",
        'progress_merge_reading': "Liest {0}...",
        'progress_merge_adding': "Setzt {0} Säiten derbäi...",
        'progress_merge_optimizing': "Optiméiert PDF...",
        'progress_merge_writing': "Schreift PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "dem Zoumaache vum PDF",
        'action_close_window': "dem Zoumaache vum Fënster",
        'action_open_new_pdf': "dem Opmaache vun engem neie PDF",
        'action_quit_app': "dem Verloosse vun der Applikatioun",
        'changes_saved': "D'Ännerunge goufe gespäichert.",
        'file_close_title': "PDF Fichier zoumaachen",
        'save_before_action': "Sollen d'Ännerunge virum {0} gespäichert ginn? Jo oder Neen?",
        'save_before_action_voice': "Sollen d'Ännerunge virum {0} gespäichert ginn? Jo oder Neen?",
        'save_before_close_question': "Sollen d'Ännerunge virum Zoumaache gespäichert ginn? Jo oder Neen?",

         # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Duersichtbar PDF erstallt:\n\n{0}\n\n<b>probéiert wann néideg nach eng Kéier",
        "ocr_rotate_title": "Säiten ausriichten virun OCR",
        "ocr_rotate_question": "D'PDF enthält gedréint Säiten.\nWëllt Dir all Säiten virun OCR op 0° ausriichten?\nDëst verbessert d'Texterkennung wesentlech.",
        "ocr_rotate_yes": "Jo, ausriichten",
        "ocr_rotate_no": "Nee, OCR direkt starten",
        "ocr_rotate_voice": "D'PDF enthält gedréint Säiten. Sollen all Säiten virun OCR ausgeriicht ginn?",
        "ocr_not_performed_message": "Keen Text do. W.e.g. OCR ausféieren (Menü \"Beaarbechten\" → \"OCR ausféieren\" oder Taste Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-Astellungen",
        "ocr_language_btn": "OCR-Sprooch auswielen",
        "ocr_language": "OCR-Sprooch(en)",
        "ocr_language_current": "Aktuell Sprooch:",
        "ocr_param_info": "Informatioun iwwer de Parameter",

        "ocr_force_ocr_label": "OCR erzwingen",
        "ocr_deskew_label": "Schréi korrigéieren",
        "ocr_clean_label": "Bild botzen",
        "ocr_oversample_label": "Resolutioun (DPI)",
        "ocr_pagesegmode_label": "Säitenandeelung",
        "ocr_oem_label": "OCR-Engine-Modus",
        "ocr_optimize_label": "PDF-Kompressioun",
        "ocr_jobs_label": "Parallel Prozesser",
        "ocr_verbose_label": "Log-Detailgrad",

        "ocr_force_ocr_tooltip": "OCR op all Säit erzwingen, och wann Text scho do ass",
        "ocr_deskew_tooltip": "Schréi Scannen automatesch ausriichten",
        "ocr_clean_tooltip": "Kaméidi an Artefakte aus dem Bild ewechhuelen",
        "ocr_oversample_tooltip": "Bild virun OCR op dësen DPI eropskaléieren",
        "ocr_pagesegmode_tooltip": "Bestëmmt wéi d'Säit an Textberäicher opgedeelt gëtt",
        "ocr_oem_tooltip": "Wiellt d'OCR-Engine vum Tesseract aus",
        "ocr_optimize_tooltip": "Kompressiounsstufe vun der Ausgab-PDF",
        "ocr_jobs_tooltip": "Zuel vun de parallelen OCR-Prozesser",
        "ocr_verbose_tooltip": "Detailgrad vun de Log-Ausgaben",
        "ocr_settings_explain_btn": "Erklärung",

        "ocr_force_ocr_explain": "Erzwingt d'Texterkennung op <b>all</b> Säit, och wann dës scho Text enthält.\n\nEmpfehlung: <b>Un</b> fir gescannte PDFen, <b>Aus</b> fir natierlech PDFe mat scho bestehendem Text.",

        "ocr_deskew_explain": "Korrigéiert liicht schréi Scannen (bis ca. 5°).\n\nEmpfehlung: <b>Un</b> fir gescannt Dokumenter, <b>Aus</b> wann d'Säite scho perfekt riicht sinn.",

        "ocr_clean_explain": "Entfernt Kaméidi, Punkten a kleng Artefakte aus dem Bild.\n<b>WICHTEG:</b> Fir arabesch, thailännesch oder vietnameesesch Texter mat Diakritiken (Punkten iwwer/ënner Buschtawen) soll dës Optioun <b>deaktivéiert</b> ginn, well soss wichteg Zeechen verläiere kënnen.",

        "ocr_oversample_explain": "Skaléiert d'Bild <b>virun</b> der Texterkennung op den uginn DPI erop.<br><br>• <b>72-150 DPI:</b> Ganz séier, awer niddreg Erkennungsquote<br>• <b>200-300 DPI:</b> Optimalen Beräich (Standard: 300)<br>• <b>400+ DPI:</b> Kaum besser Erkennung, awer däitlech méi grouss Dateien<br><br>Empfehlung: 300 DPI fir komplex Schrëften (Arabesch, Chinesesch, Japanesch), 200 DPI fir westlech Sproochen.",

        "ocr_pagesegmode_explain": "Bestëmmt wéi Tesseract d'Säit an Textberäicher opdeelt.\n\n• <b>3 - Automatesch (Standard):</b> Gutt fir gemëschte Layouten\n• <b>4 - Eenzel Kolonn:</b> Fir eenzelkolonne Texter\n• <b>5 - Vertikale Block:</b> Fir vertikal Schrëften (Japanesch, Chinesesch)\n• <b>6 - Eenheetlechen Textblock:</b> Optimal fir Fléisstext ouni Kolonnen\n• <b>11 - Raa Bild:</b> Fir schlecht Scannen / Handschrëften\n\nEmpfehlung: <b>6</b> fir einfach Textdokumenter, <b>3</b> fir komplex Layouten.",

        "ocr_oem_explain": "Wiellt d'OCR-Engine vum Tesseract aus.\n\n• <b>0 - Legacy:</b> Al Engine (séier, awer manner genee)\n• <b>1 - LSTM:</b> Neural Engine (lues, awer méi genee)\n• <b>2 - Legacy + LSTM:</b> Kombinéiert béid Resultater\n• <b>3 - Standard (LSTM léiwer):</b> Bescht Wiel fir déi meescht Fäll\n\nEmpfehlung: <b>3</b> fir maximal Erkennungsgenauegkeet.",

        "ocr_optimize_explain": "Kompriméiert d'Ausgab-PDF.\n\n• <b>0:</b> Keng Optiméierung (séierst Veraarbechtung)\n• <b>1:</b> Liicht Optiméierung (gudde Kompromëss)\n• <b>2:</b> Moderéiert Optiméierung\n• <b>3:</b> Staark Optiméierung (klengst Datei, awer méi lues)\n\nEmpfehlung: <b>1</b> fir deegleche Gebrauch.",

        "ocr_jobs_explain": "Zuel vun de parallele Prozesser fir OCR.\n\n• <b>1:</b> Lues, awer niddregste Späicherverbrauch\n• <b>4-8:</b> Optimal fir modern Multiprozessoren\n• <b>12+:</b> Kaum méi séier Veraarbechtung bei héichem Späicherverbrauch\n\nEmpfehlung: Zuel vun de CPU-Kären (z.B. <b>4</b> bei 4-Kär Systemer).",

        "ocr_verbose_explain": "Detailgrad vun de Log-Ausgaben an der Konsole.\n\n• <b>0:</b> Keng Ausgaben\n• <b>1:</b> Fortschrëtt a Statusmeldungen\n• <b>2:</b> Detailléiert Ausgaben\n• <b>3:</b> Vollstänneg Debug-Ausgaben (ganz ëmfangräich)\n\nEmpfehlung: <b>1</b> fir normalen Operatioun.",

        "ocr_reset_title": "Astellungen zréckgesat",
        "ocr_reset_message": "All OCR-Astellunge goufen op d'Standardwäerter zréckgesat.",
        "info_tooltip": "Méi Informatiounen iwwert dëse Parameter",
        "ocr_reset_defaults": "Op Standard zrécksetzen",

        "ocr_psm_0": "Automatesch (Legacy-Engine)",
        "ocr_psm_1": "Automatesch Kolonneerkennung",
        "ocr_psm_3": "Automatesch (Standard)",
        "ocr_psm_4": "Eenzel Kolonn",
        "ocr_psm_5": "Vertikale Block",
        "ocr_psm_6": "Eenheetlechen Textblock",
        "ocr_psm_7": "Eenzel Textlinn",
        "ocr_psm_8": "Eenzel Wuert",
        "ocr_psm_11": "Raa Bild (keng Layoutanalyse)",

        "ocr_oem_0": "Legacy-Engine (séier)",
        "ocr_oem_1": "LSTM-Engine (neural, genee)",
        "ocr_oem_2": "Legacy + LSTM kombinéiert",
        "ocr_oem_3": "Standard (LSTM léiwer)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-Sprooch(en)...",
        "ocr_language_title": "OCR-Sprooch(en) auswielen",
        "ocr_language_instruction": "Wielt d'Sprooch(en) fir d'Texterkennung (OCR).\nOpgepasst: Méi Sprooche gi mam Leeschtungsverloscht a Genauegkeetsverloscht!\nDéi bescht Resultater kritt Dir, wann Dir nëmmen eng Sprooch auswielt.",
        "ocr_language_predefined": "Virdefinéiert Kombinatiounen",
        "ocr_language_custom": "Benotzerdefinéiert...",
        "ocr_language_selected": "Ausgewielten OCR-Sproochen",
        "ocr_language_changed": "OCR-Sprooch geännert op {0}",
        "ocr_language_auto_detect": "Disponibel Sprooche ginn automatesch erkannt.",
        "ocr_language_none_found": "Keng Tesseract-Sproochdate fonnt! W.e.g. installéiert Sproochpaketer (z.B. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Benotzerdefinéiert Sproochauswiel",
        "ocr_language_available": "Disponibel Sproochen (installéiert):",
        "ocr_language_select_hint": "Wielt eng oder méi Sproochen aus:",
        "ocr_language_confirm": "Iwwerhuelen",
        "ocr_language_reset": "Op Standard zrécksetzen (deu+eng+vie)",
        "ocr_language_priorities": "Empfoll Sproochen (virinstalléiert):",

        "select_all_languages": "All auswielen",
        "clear_all_languages": "Auswiel läschen",
        "install_language_packs": "Feelend Sproochpaketer installéieren...",
        "install_hint": "💡 Tipp: Net all Sprooche sinn op Ärem System installéiert. Iwwert dëse Knäppche kritt Dir Hëllef fir d'Installatioun.",
        "ocr_language_install_title": "Installatioun vun Tesseract-Sproochpaketer",

        "ocr_missing_languages": "Feelend OCR-Sproochpaketer",
        "ocr_missing_languages_message": "Déi folgend ausgewielte Sprooche sinn net op Ärem System installéiert:\n\n{0}\n\nW.e.g. installéiert déi feelend Sproochpaketer (kuckt Hëllef ënner 'Installatiounshëllef').\n\nWëllt Dir d'Installatiounshëllef elo opmaachen?",
        "ocr_missing_languages_voice": "Feelend Sproochpaketer. W.e.g. installéiert déi feelend Sproochen.",
        "ocr_install_help_now": "Hëllef opmaachen",
        "ocr_continue_anyway": "Trotzdem probéieren",
        "ocr_language_error_title": "OCR-Sproochfeeler",
        "ocr_language_error_message": "Feeler bei der Texterkennung: {0}\n\nW.e.g. iwwerpréift Är OCR-Sproochastellungen (Astellungen → OCR-Sprooch).",
        "ocr_install_help_button": "Installatiounshëllef",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract-Sproochpakter installéieren</p>

        <p>Fir datt OCR an enger bestëmmter Sprooch funktionéiert, mussen déi entspriechend Sproochdate op Ärem System installéiert sinn. Follegt d'Uweisunge fir Äre Betribssystem:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Maacht den <strong>Terminal</strong> op (Finder → Programmer → Hëllefsprogrammer → Terminal).</li>
        <li>Installéiert all verfügbar Sprooche mat:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Dat kann e puer Minutten daueren.)</li>
        <li>Oder nëmmen eenzel Sproochen (z.B. Vietnameesesch):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Bei aktuellen Homebrew-Versiounen muss <code>*.traineddata</code> vläicht manuell erofgeluede ginn (kuckt hei ënnen).</li>
        <li>No der Installatioun: Maacht dësen Dialog zou an maacht d'OCR-Sproochauswiel nees op – déi nei Sprooche kommen automatesch.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Maacht en Terminal op (Ctrl+Alt+T).</li>
        <li>Installéiert déi gewënschte Sprooch, z.B. fir Vietnameesesch:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Wichteg Sproochcoden: <code>deu</code> (Däitsch), <code>eng</code> (Englesch), <code>vie</code> (Vietnameesesch), <code>spa</code> (Spuenesch), <code>fra</code> (Franséisch), <code>ita</code> (Italienesch), <code>nld</code> (Hollännesch), <code>fin</code> (Finnesch), <code>swe</code> (Schweedesch), <code>nor</code> (Norwegesch).</li>
        <li>Weist all verfügbar Paketer:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuell)</p>
        <ol>
        <li>Luet déi gewënschte <code>*.traineddata</code>-Dateien erof vu:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (z.B. <code>vie.traineddata</code> fir Vietnameesesch).</li>
        <li>Kopéiert d'Dateien an den Tesseract-Sproochdossier, meeschtens:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Passt se un no individueller Installatioun.)</li>
        <li>Start d'Applikatioun nei (oder maacht d'OCR-Sproochauswiel nees op).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativ fir all Systemer</p>
        <ul>
        <li>Installéiert <strong>OCRmyPDF</strong> a <strong>Tesseract</strong> mat engem Paketmanager vun Ärer Wiel. Déi meescht Installatiounen enthalte scho puer Standardsproochen (Englesch, Däitsch, Franséisch).</li>
        <li>Fehlend Sprooche kënnen zu all Moment nogeholl ginn – d'OCR-Sproochauswiel weist nëmmen déi tatsächlech existent Sproochen.</li>
        </ul>

        <hr>
        <p><b>✅ No der Installatioun:</b> Keng Applikatiounsneistart néideg – déi nei dobäigesaten Sprooche ginn direkt an der Lëscht ugewisen.</p>
        <p><b>📖 Hëllef zu Sproochcoden:</b> Eng vollstänneg Lëscht fannt Dir an der <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract-Dokumentatioun</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans Schrëften",
        "info_noto_font_voice": "Noto Sans Schrëften Installatiounsuguid",
        "btn_info_noto_font_install": "Schrëft Info",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Wéi installéiert een déi gratis Noto Schrëfte vu Google</h2>

        <p>D'<strong>Noto Schrëften</strong> sinn eng Open-Source Schrëftfamill vu Google. Hiert Zil ass et, <em>"keen Tofu"</em> (d.h. keng eidel Këschten □) ze gesinn a wierklech all Zeechen aus dem Unicode-Standard korrekt duerzestellen. Si sinn déi ideal Ergänzung fir Applikatiounen, déi Texter a ville verschiddene Sprooche mussen duerstellen.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installatioun ënner macOS</h3>

        <p><strong>Methode 1: Mat Homebrew (fir Fortgeschratt)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Methode 2: Iwwer d'"Font Book" (Empfoll)</strong></p>

        <ol>
        <li>Luet den offiziellen Schrëftpaket erof:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/NotoSans</a></li>
        <li>Entpaakt d'ZIP-Datei</li>
        <li>Kopéiert d'Dateien an <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installatioun ënner Windows (10 & 11)</h3>

        <p><strong>Methode 1: Microsoft Store (Empfoll)</strong><br>
        Sich no "Google Noto Fonts" oder "Noto Sans" a klick op <strong>Installéieren</strong>.</p>

        <p><strong>Methode 2: Manuell Installatioun</strong></p>

        <ol>
        <li>Eroflueden:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP entpaaken</li>
        <li>.ttf / .otf Dateien auswielen</li>
        <li>Rietsklick → <strong>Installéieren</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        oder<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Numm\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installatioun ënner Linux</h3>

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

        <p>Iwwerpréiwung:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Lieszeechen verwalten",
        "bookmark_add": "Lieszeechen derbäisetzen",
        "bookmark_add_tooltip": "Aktuell Säit als Lieszeechen späicheren",
        "bookmark_remove": "Lieszeechen ewechhuelen",
        "bookmark_remove_tooltip": "Dat markéiert Lieszeechen läschen",
        "bookmark_remove_all": "All ewechhuelen",
        "bookmark_remove_all_tooltip": "All Lieszeechen vun dësem PDF läschen",
        "bookmark_jump": "Zum Lieszeechen sprangen",
        "bookmark_jump_tooltip": "Op déi ausgewielte Säit sprangen",
        "bookmark_name": "Numm",
        "bookmark_page": "Säit",
        "bookmark_no_bookmarks": "Keng Lieszeechen do.\nKlickt op 'Derbäisetzen' fir déi aktuell Säit als Lieszeechen ze späicheren.",
        "bookmark_added": "Lieszeechen fir Säit {0} derbäigesat: {1}",
        "bookmark_removed": "Lieszeechen ewechgeholl: {0}",
        "bookmark_all_removed": "All Lieszeechen goufen ewechgeholl.",
        "bookmark_name_default": "Säit {0}",
        "bookmark_name_prompt": "Numm fir d'Lieszeechen:\n(laangen Text gëtt op 50 Zeechen verkierzt)",
        "bookmark_name_prompt_title": "Lieszeechen-Numm",
        "bookmark_confirm_remove_all": "Sidd Dir sécher datt Dir all {0} Lieszeechen ewechhuele wëllt?",
        "menu_bookmarks": "Lieszeechen",
        "bookmark_manage": "Lieszeechen verwalten",
        "bookmark_next": "Nächst Lieszeechen",
        "bookmark_prev": "Viregt Lieszeechen",
        "bookmark_page_display": "Säit {0}",
        "bookmark_exists": "E Lieszeechen fir dës Säit mat dësem Numm existéiert schonn.",
        "bookmark_select_first": "Wielt w.e.g. fir d'éischt e Lieszeechen aus.",
        "bookmark_confirm_remove": "Sidd Dir sécher datt Dir d'Lieszeechen 'Säit {0}: {1}' ewechhuele wëllt?",
        "bookmark_jumped_to": "Op Lieszeechen '{0}' op Säit {1} gesprongen.",
        "bookmark_jumped_to_voice": "Lieszeechen {0}, Säit {1}",
        "btn_close": "Zoumaachen",

        "bookmark_list": "Är Lieszeechen",
        "bookmark_rename": "Lieszeechen ëmbenennen",
        "bookmark_rename_tooltip": "Den Numm vum ausgewielten Lieszeechen änneren",
        "bookmark_rename_title": "Lieszeechen ëmbenennen",
        "bookmark_rename_prompt": "Neien Numm fir d'Lieszeechen op Säit {0}:\n(max. 50 Zeechen)",
        "bookmark_renamed": "Lieszeechen '{0}' gouf op '{1}' ëmbenannt.",
        "bookmark_item_tooltip": "Säit {0}: {1}\nDuebelklick fir ze sprangen",
        "bookmark_name_exists_question": "E Lieszeechen mam Numm '{0}' existéiert schonn op dëser Säit.\nTrotzdem ëmbenennen?",

        "context_bookmarks": "Lieszeechen",
        "context_bookmark_add_here": "Lieszeechen fir dës Säit derbäisetzen",
        "context_bookmarks_existing": "Existéierend Lieszeechen:",
        "context_bookmarks_jump": "Op Lieszeechen sprangen:",
        "context_bookmarks_none": "Keng Lieszeechen do",
        "context_bookmarks_clear_all": "All {0} Lieszeechen ewechhuelen",

        "bookmark_search_placeholder": "Lieszeechen sichen... (Numm oder Säit)",
        "bookmark_search_results": "%d Lieszeechen fir \"%s\" fonnt",
        "bookmark_no_search_results": "Keng Lieszeechen fir \"%s\" fonnt",
        "bookmark_no_search_results_label": "Keng Resultater fir \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF-Metadaten beaarbechten",
        "metadata_title": "Titel",
        "metadata_title_placeholder": "Dokumententitel",
        "metadata_title_tooltip": "Den Titel vum Dokument (gëtt an der Titellëscht ugewisen)",
        "metadata_author": "Auteur",
        "metadata_author_placeholder": "Numm vum Auteur",
        "metadata_author_tooltip": "Den Ersteller vum Dokument",
        "metadata_subject": "Betreff",
        "metadata_subject_placeholder": "Betreff vum Dokument",
        "metadata_subject_tooltip": "Eng kuerz Beschreiwung vum Inhalt",
        "metadata_keywords": "Stéchwierder",
        "metadata_keywords_placeholder": "Stéchwierder, duerch Komma getrennt",
        "metadata_keywords_tooltip": "Schlagwierder fir d'Kategoriséierung vum Dokument",
        "metadata_creator": "Ersteller",
        "metadata_creator_placeholder": "Applikatioun déi d'PDF erstallt huet",
        "metadata_creator_tooltip": "D'Software mat där d'Dokument erstallt gouf",
        "metadata_producer": "Produzent",
        "metadata_producer_placeholder": "Applikatioun déi d'PDF konvertéiert huet",
        "metadata_producer_tooltip": "D'Software déi d'PDF konvertéiert huet",
        "metadata_creation_date": "Erstellungsdatum",
        "metadata_creation_date_tooltip": "D'Datum vun der Dokumenterstellung",
        "metadata_mod_date": "Ännerungsdatum",
        "metadata_mod_date_tooltip": "D'Datum vun der leschter Ännerung",
        "metadata_pdf_info": "📄 PDF-Informationen",
        "metadata_pages": "Säitenzuel",
        "metadata_file_size": "Dateigréisst",
        "metadata_pdf_version": "PDF-Versioun",
        "metadata_encrypted": "Verschlësselt",
        "metadata_encrypted_yes": "Jo (passwuertgeschützt)",
        "metadata_encrypted_no": "Nee",
        "metadata_reload": "📂 Aus PDF nei lueden",
        "metadata_reset": "Ännerungen verwëerfen",
        "metadata_reloaded": "Metadaten goufen aus dem PDF nei gelueden.",
        "metadata_reset_done": "All Metadatefelder goufen zréckgesat.",
        "metadata_no_file": "Keng PDF-Datei gelueden.",
        "metadata_save_error": "Feeler beim Späicheren vun de Metadaten",
        "metadata_saved": "Metadaten goufen erfollegräich gespäichert.",
        "metadata_pdf_version_unknown": "PDF (onbekannt)",
        "metadata_saved_message": "D'Metadaten goufen erfollegräich gespäichert.",
        "metadata_saved_voice": "Metadaten gespäichert.",

        "metadata_custom": "🔧 Benotzerdefinéiert Metadaten",
        "metadata_custom_placeholder": "{\n  \"mäi_Feld\": \"mäi Wäert\",\n  \"anert_Feld\": 123\n}",
        "metadata_custom_tooltip": "JSON-Format fir benotzerdefinéiert Metadaten (optional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Virlag \"{0}\" ausgewielt - Duebelklick zum Afügen",
        "text_use_template": "Textbaustein benotzen",
        "text_type": "Typ",
        "text_search_templates": "Textbaustein sichen...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Export / Import Informatiounen",
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

        <h3>📦 Wat gëtt exportéiert? (Iwwersiicht)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Allgemeng Applikatiounsastellungen</span></li>
            <li class="detail">• Däischter/Helleg Modi</li>
            <li class="detail">• Däischter-Modus Invertéierung fir Biller</li>
            <li class="detail">• Gro Schwellwäert</li>
            <li class="detail">• Sprooch</li>
            <li class="detail">• Fënstergeometrie</li>
            <li class="detail">• Zoom-Modus</li>
            <li class="detail">• Navigatioun (Navbar siichtbar)</li>
            <li class="detail">• Sproochausgab (un/aus)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Backup-Astellungen</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Dateibenennung (Zäitstempel, Trennzeechen, Suffixen)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Astellunge fir Afügungen</span></li>
            <li class="detail">• Ënnerschrëften</li>
            <li class="detail">• Text &amp; Textbaustenger</li>
            <li class="detail">• Kräizer, Biller a Formen</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-Astellungen</span></li>
            <li class="detail">• Sprooch</li>
            <li class="detail">• OCR erzwingen · Säitemodus</li>
            <li class="detail">• Bildvirveraarbechtung: Schréi korrigéieren, Botzen, Oversampling</li>
            <li class="detail">• Zuel vun de parallelen Aufgaben</li>
            <li class="detail">• Invertéierungsmodus</li>
            <li class="detail">• Gro Schwellwäert</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Lieszeechen</span></li>
            <li class="detail">• All Lieszeechen pro PDF-Datei (Säit, Numm, Erstellzäit)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Passwuert-Datebank</span></li>
            <li class="detail">• Gespäichert PDF-Passwierder (op Wonsch verschlësselt oder Klartext)</li>
            <li class="detail">• Master-Passwuert-Hash (wann gesat)</li>
            <li class="detail">• Verifikatiounsdaten</li>
        </ul>

        <h4>⚠️ Wichteg Hiweiser</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Beim Import:</strong>
            <ul>
                <li><span class="warning">➜ ALL aktuell Astellunge ginn komplett iwwerschriwwen</span></li>
                <li>• E Neistart vun der Applikatioun ass obligatoresch</li>
                <li>• Bestoend Ënnerschrëften, Textbaustenger a Lieszeechen ginn ersat</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Master-Passwuert &amp; Exportmodus:</strong>
            <ul>
                <li>• Bei aktivem Master-Passwuert kënnt Dir wielen:</li>
                <li>  - <span style="color: #98FB98;"><strong>Entschlësselt</strong></span> (Passwierder leien am Klartext an der ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Verschlësselt</strong></span> (nëmme mam Master-Passwuert am Zilsystem liesbar)</li>
                <li>• De Master-Passwuert-Hash selwer gëtt <strong>ëmmer</strong> verschlësselt ofgeluecht</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Sécherheetshinweis:</strong>
            <ul>
                <li>• Déi exportéiert ZIP-Datei enthält vertraulech Daten (<strong>Passwierder, Lieszeechen, Ënnerschrëften</strong>)</li>
                <li>• W.e.g. sécher opbewahren (z.B. verschlësselten USB-Stick, Passwuert-Manager)</li>
                <li>• Bei Verloscht vun der Datei si gespäichert PDF-Passwierder onwiderrufflech verluer</li>
            </ul>
        </div>

        <h4>📁 Exportformat</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            D'Astellungen ginn an enger eenzeger ZIP-Datei gespäichert:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Dës ZIP enthält déi vollstänneg <code>settings.json</code> (aus Ärer Konfiguratioun) souwéi gëff. agebett Ënnerschrëft-Bilddateien a verschlësselt Passwierder.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Ënnerschriften - Guide",
        'signature_guide_html': """
        📝 <strong>Ënnerschriften - Kuerzguide</strong><br>
        <ul>
        <li>Master Passwuert astellen</li>
        <li>Ënnerschriften am Menü <em>Astellungen</em> konfiguréieren (Gréisst, Zäitstempel, …)</li>
        <li>Asetze mat <strong>RIETSKLICK</strong> op der gewënschter Positioun (Master Passwuert eemol pro Sëtzung néideg)</li>
        <li>Ënnerschrëft mat der Maus oder Pfeiltaste réckelen</li>
        <li>Méier Ënnerschriften noenee asetzen</li>
        <li>All Ënnerschrëft individuell upassen</li>
        <li>Eenzel Ënnerschrëft verwëerfen</li>
        <li>All Ënnerschriften op eemol späicheren / verwëerfen</li>
        <li>Alternativ kann och d'Menüleescht benotzt ginn.</li>
        </ul>
        """,
        'signature_guide_voice': "Kuerzguide fir Ënnerschriften. Master Passwuert astellen. Ënnerschriften an den Astellunge konfiguréieren. Asetze mat Rietsklick.",

        'image_guide_title': "Biller asetzen - Guide",
        'image_guide_html': """
        📷 <strong>Biller a PDF asetzen - Kuerzguide</strong><br>
        <ol>
        <li>Rietsklick op déi gewënscht Positioun</li>
        <li><em>„Bild asetzen“</em> → Bild auswielen</li>
        <li>Bild positionéieren: Zéie mat der Maus</li>
        <li>Gréisst upassen: Zéie un den Ecker/Kanten</li>
        <li>Säiteverhältnis bäibehalen: Taste <strong>[A]</strong></li>
        <li>Weider Upassungen: Rietsklick op d'Bild</li>
        </ol>
        <p><strong>Tipp:</strong> Am Kontextmenü kënnt Dir d'Astellungen upassen.</p>
        """,
        'image_guide_voice': "Kuerzguide fir Biller. Rietsklick, Bild asetzen, auswielen. Positionéiere mat Maus, Gréisst upassen un Ecker. Säiteverhältnis mat Taste A.",

        'form_guide_title': "Formen asetzen - Guide",
        'form_guide_html': """
        📐 <strong>Formen a PDF asetzen - Kuerzguide</strong><br>
        <ol>
        <li>Form-Typ auswielen (Rechteck, Ellips, Linn, Feil)</li>
        <li>Op Positioun klicken:
            <ul>
            <li>Bei Rechteck/Ellips: Ee Klick setzt d'Form</li>
            <li>Bei Linn/Feil: Zwee Klick fir Start- an Endpunkt</li>
            </ul>
        </li>
        <li>Form positionéieren: Zéie mat der Maus</li>
        <li>Gréisst upassen: Zéie un den Ecker/Kanten</li>
        <li>Form späicheren: <strong>Enter</strong></li>
        <li>Form verwëerfen: <strong>ESC</strong></li>
        <li>Weider Upassungen: Rietsklick op d'Form</li>
        </ol>
        <p><strong>Tipp:</strong> Am Kontextmenü kënnt Dir d'Astellungen upassen.</p>
        """,
        'form_guide_voice': "Kuerzguide fir Formen. Form-Typ auswielen. Bei Rechteck oder Ellips eemol klicken, bei Linn oder Feil zweemol klicken. Positionéiere mat Maus, Gréisst upassen un Ecker. Späicheren mat Enter, verwëerfen mat Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "vireg",
        "btn_next_result": "nächst",
        "ocr_text_window": "OCR Textfenster",
        "bookmark_existing": "Virdrun Lieszeechen",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR Verglach Mac - Windows",
        'ocr_method_mac_win_title': "OCR Ënnerscheeder tëscht Mac a Windows",
        'ocr_method_mac_win_voice': "Mac ass besser",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Ënnerscheeder tëscht macOS a Windows</strong></p>

        <p><strong>macOS (empfohlen)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resultat:</p>
        <ul>
        <li>Eng durchsichtbar PDF mat agebettem Text, déi gréisstendeels dat original Layout behält.</li>
        </ul>
        <p>Virdeeler:</p>
        <ul>
        <li>Ausgezeechent Qualitéit vun der Texterkennung (och bei kromme Säiten).</li>
        <li>Behale vu Vektorgrafiken a Schrëftaarten.</li>
        <li>GUI-Fortschrëttsbalken iwwer Subprocess-Auswäertung.</li>
        <li>Voll Kontroll iwwer all OCR-Parameter (Deskew, Clean, Oversample, Optimiséierung).</li>
        <li>D'Textsich ass direkt am Haaptfenster (PDF Vue) verfügbar.</li>
        </ul>
        <p>Nodeeler:</p>
        <ul>
        <li>Braucht zousätzlech System-Tools (ocrmypdf, Ghostscript, unpaper, pngquant – am App Bundle enthalen).</li>
        <li>Komplexer Feelermellung (Deadlocks, Timeouts).</li>
        </ul>

        <p><strong>Windows (stabil Alternativ)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>pytesseract (direkt Verbindung un Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resultat:</p>
        <ul>
        <li>Eng durchsichtbar PDF, déi visuell enger Bild-PDF entsprécht, awer duerch den transparenten Text durchsichtbar ass.</li>
        </ul>
        <p>Virdeeler:</p>
        <ul>
        <li>Do fale mir grad keng an.</li>
        </ul>
        <p>Nodeeler:</p>
        <ul>
        <li>D'PDF ass am Wiesen e Bild mat onsichtbarem Text; d'Layout ka bei komplexen Dokumenter (Spalten, Tabellen) liicht ofwäichen.</li>
        <li>Keng automatesch Schréilagkorrektur (--deskew) oder Bildbereenegung (--clean).</li>
        <li>Den GUI-Fortschrëttsbalke gëtt nëmme grob iwwer d'Zuel vu veraarbechte Säiten aktualiséiert.</li>
        <li>D'OCR-Geschwindegkeet ass e bësse méi lues (well all Säit eenzel veraarbecht gëtt).</li>
        <li>D'Textsich gëtt op d'OCR Textfenster ëmgeleet.</li>
        </ul>

        <p><strong>Gemeinsamkeeten</strong></p>
        <ul>
        <li>Béid Prozedure produzéieren eng durchsichtbar PDF am selwechte Verzeechnes wéi d'Quelldatei.</li>
        <li>D'OCR-Astellungen (Sprooch, DPI, Säiten-Segmentéierungsmodus, OCR-Engine-Modus) kënnen iwwer den OCRSettingsDialog konfiguréiert ginn a wierken a béiden Implementatiounen.</li>
        </ul>

        <p><strong>Empfehlung:</strong></p>
        <ul>
        <li>macOS: D'ocrmypdf-Binary liwwert déi bescht Resultater – Kaaft Iech e Mac a benotzt d'Versioun (PDFDarkView fir Mac's mat Apple Silicon oder Intel Chip). D'OCR Resultater si besser wéi ënner Windows!</li>
        <li>Windows: Benotzt d'pytesseract-Léisung. Se ass stabil a liwwert fir déi meescht Dokumenter eng ganz ausreechend Qualitéit.</li>
        </ul>

        <p><strong>Wichteg Hiweis:</strong></p>
        <ul>
        <li>Béid Versioune si komplett an d'Benotzeroberfläche integréiert – de Benotzer mierkt keen Ënnerscheed.</li>
        <li>D'Entscheedung, wéi eng OCR-Engine benotzt gëtt, trëfft d'Programm automatesch baséierend op dem Betribssystem.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Ënnerschrëft erstellen (aus Scan)",
        "signature_create_title": "Gescannt Ënnerschrëft auswielen (PDF/Bild)",
        "image_pdf_filter": "Biller a PDF",
        "signature_pdf_empty": "D'PDF enthält keng Säiten.",
        "signature_created_success": "Ënnerschrëft erfollegräich erstallt: {0}",
        "signature_create_error": "Feeler beim Erstelle vun der Ënnerschrëft:\n{0}",
        "rembg_missing": "rembg ass net installéiert.\nW.e.g. installéieren: pip install rembg\nFeeler: {0}",
        "signature_name_title": "Dateinumm fir d'Ënnerschrëft",
        "signature_name_message": "Gitt w.e.g. e Dateinumm fir déi nei Ënnerschrëft an (gëtt als PNG mat transparentem Hannergrond gespäichert):",
        "signature_name_label": "Dateinumm:",
        "signature_name_voice": "Dateinumm fir d'Ënnerschrëft aginn",
        "signature_processing": "Veraarbechtung leeft...",
        "signature_creation_title": "Ënnerschrëft gëtt erstallt",
        "signature_overwrite_warning": "D'Datei '{0}' existéiert schonn. Iwwerschreiwen?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"PDF fir Ënnerschrëft virbereeden",
        "signature_prepare_instruction":"Wielt w.e.g. e PDF aus, dat op enger eenzeger Säit eng gescannt Ënnerschrëft enthält.\n\nOptimal Erkennung erreecht Dir wann:\n• D'Ënnerschrëft mat schwaarzer Tënt (Kugelschreiwer oder Fineliner) op wäissem Pabeier geschriwwen ass.\n• D'Ënnerschrëft sech am ieweschten Drëttel vun der soss eiderer A4 Säit befënnt.\n• D'PDF mat mindestens 300 dpi gescannt gouf.\n• D'Ënnerschrëft kloer an net ze dënn ass.\n• Keng stéierend Hannergrondmuster oder Linnen do sinn.",
        "signature_prepare_voice":"Wielt w.e.g. e PDF mat enger gescannter Ënnerschrëft aus. Aacht op gutt Qualitéit a Kontrast.",
        "sig_thickness_label":"Linnestäerkt:",
        "sig_thickness_normal":"Normal (dënn)",
        "sig_thickness_bold":"Kräfteg (empfohlen)",
        "sig_thickness_very_bold":"Ganz kräfteg",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI an OCR Sproochen derbäisetzen - Guide",
        'language_guide_title': "GUI an OCR Sproochen derbäisetzen",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Luet déi gewënscht Iwwersetzungsdatei <code>translations_xy.py</code> erof vu<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        a lee se an dëst Verzeechnes:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Maacht Äre Webbrowser op.</li>
        <li>Gitt op: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Sicht um rietsen Ecranrand no "Releases" a wielt dat mat <strong>"latest"</strong> markéiert.</li>
        <li>Op der folgender Release-Säit lued ganz ënnen d'Datei <code>Source Code.zip</code> erof.</li>
        <li>Entpackt d'ZIP-Datei.</li>
        <li>Sicht am entpackten Dossier all Sproochdateien, déi Dir braucht, a kopéiert se an d'Verzeechnes:<br/>
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
        "menu_watermark":"Waasserzeechen afügen",
        "fullpage_text_watermark_title":"Text als Waasserzeechen",
        "fullpage_image_watermark_title":"Bild als Waasserzeechen",
        "filename_with_watermark":"_mat_Waasserzeechen",
        "watermark_text":"Text:",
        "watermark_text_placeholder":"Äre Waasserzeechen-Text...",
        "watermark_font_family":"Schrëftart:",
        "watermark_font_size":"Schrëftgréisst:",
        "watermark_format":"Formatéierung:",
        "watermark_bold":"Fett",
        "watermark_italic":"Kursiv",
        "watermark_color":"Faarf:",
        "watermark_choose_color":"Faarf wielen...",
        "watermark_opacity":"Duerchsiichtegkeet / Transparenz:",
        "watermark_direction":"Liesrichtung:",
        "watermark_direction_l_r":"Links → Riets",
        "watermark_direction_bl_tr":"Ënne lénks → Uewe riets",
        "watermark_direction_tl_br":"Uewe lénks → Ënnen",
        "watermark_direction_b_t":"Ënnen → Uewen",
        "watermark_direction_t_b":"Uewen → Ënnen",
        "watermark_preview":"Virschau:",
        "watermark_preview_sample":"Beispilltext",
        "watermark_empty_text":"W.e.g. gitt en Text an.",
        "watermark_applied":"Waasserzeechen gouf op all Säiten ugewannt.",
        "watermark_saved":"Waasserzeechen gespäichert.",
        "image_scale":"Gréisst:",
        "image_preview":"Bildvirschau:",
        "no_image_selected":"Kee Bild ausgewielt",
        "browse":"Duerchsichen...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Réchirungen",
        "redact_add_black": "Réchirung (schwaarz)",
        "redact_add_white": "Réchirung (wäiss / läschen)",
        "redact_added_black": "Schwaarz Réchirung derbäigesat",
        "redact_added_white": "Wäiss Réchirung derbäigesat",
        "redact_apply_all": "All Réchirungen uwenden a späicheren",
        "redact_discard_all": "All Réchirungen verwërf",
        "redact_discard": "Dës Réchirung verwërf",
        "no_redactions": "Keng Réchirungen",
        "redact_confirm_title": "Réchirungen permanent uwenden",
        "redact_confirm_message": "Opgepasst: Déi markéiert Beräicher gi permanent geläscht (schwaarz oder wäiss).\nEng Sécherheetskopie gëtt ugeluecht (wa aktivéiert).\n\nWeider maachen?",
        "redact_apply": "Jo, elo réchiréieren",
        "redact_saved": "{0} Réchirung(en) erfollegräich ugewannt a gespäichert.",
        "redact_saved_voice": "{0} Réchirung(en) ugewannt",
        "redact_error":"Feeler beim Réchiréieren",
        "filename_redacted":"_réchiréiert",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Säitenzuelen afügen',
        'page_numbers_format': 'Zueleformat:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabesch)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (réimesch kleng)',
        'page_numbers_format_roman_upper': 'I, II, III ... (réimesch grouss)',
        'page_numbers_format_letter': 'A, B, C ... (Buschtawen)',
        'page_numbers_format_custom': 'Personaliséiert',
        'page_numbers_custom_pattern': 'Muster:',
        'page_numbers_custom_placeholder': 'z.B. "Säit {nummer}" oder "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Benotzt {nummer} fir déi aktuell Säitenzuel a {total} fir d\'Gesamtzuel',
        'page_numbers_position': 'Positioun:',
        'page_numbers_pos_tl': 'Uewe lénks',
        'page_numbers_pos_tc': 'Uewe mëtt',
        'page_numbers_pos_tr': 'Uewe riets',
        'page_numbers_pos_ml': 'Mëtt lénks',
        'page_numbers_pos_mc': 'Zentréiert',
        'page_numbers_pos_mr': 'Mëtt riets',
        'page_numbers_pos_bl': 'Ënne lénks',
        'page_numbers_pos_bc': 'Ënne mëtt',
        'page_numbers_pos_br': 'Ënne riets',
        'page_numbers_margins': 'Ränner:',
        'page_numbers_margin_x': 'Horizontalen Ofstand:',
        'page_numbers_margin_y': 'Vertikalen Ofstand:',
        'page_numbers_range': 'Säiteberäich:',
        'page_numbers_all_pages': 'All Säiten',
        'page_numbers_custom_range': 'Personaliséierte Beräich',
        'page_numbers_from': 'Vun:',
        'page_numbers_to': 'Bis:',
        'page_numbers_progress': 'Säitenzuelen afügen...',
        'page_numbers_start': 'Säitenzuelen afügen starten...',
        'page_numbers_cancel': 'Säitenzuelen afügen ofgebrach',
        'page_numbers_success': 'Säitenzuelen goufen erfollegräich derbäigesat.\n\nWëllt Dir déi nei PDF opmaachen?\n\n{0}',
        'page_numbers_complete': 'Säitenzuelen derbäigesat',
        'page_numbers_error_format': 'Feeler beim Afüge vun de Säitenzuelen: {0}',
        'page_numbers_content_type': 'Inhaltstyp:',
        'page_numbers_tab_simple': 'Einfach Zuel',
        'page_numbers_tab_range': 'Säit X vu Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Frëien Text',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Säit {aktuell} vu {gesamt}',
        'page_numbers_range_custom': 'Personaliséiert',
        'page_numbers_range_placeholder': 'z.B. "Säit {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Datumsformat:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. Januar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Personaliséiert',
        'page_numbers_date_placeholder': 'z.B. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Positioun:',
        'page_numbers_date_before': 'Datum virun der Säitenzuel',
        'page_numbers_date_after': 'Datum no der Säitenzuel',
        'page_numbers_date_only': 'Nëmmen Datum (ouni Säitenzuel)',
        'page_numbers_custom_text': 'Personaliséierten Text:',
        'page_numbers_custom_placeholder_text': 'Benotzt {seite} fir d\'Säitenzuel an {gesamt} fir d\'Gesamtzuel\nz.B. "Vertraulech - Säit {seite}" oder "{seite} vu {gesamt}"',
        "filename_with_page_number":"_mat_Säitenzuel",
        "filename_with_page_declaration":"_mat_Säitenugab",
        "filename_with_pagenumber":"_mat_Säitenzuel",
        "filename_with_date":"_mat_Datum",
        "filename_with_my_page_declaration":"_mat_eegener_Säitenugab",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Net gespäichert Ännerungen",
        "unsaved_changes_message_darkmode": "Et gi net gespäichert Afügungen.\nWëllt Dir déi virum Wiessel späicheren?",
        "save_and_switch": "Späicheren a wiesselen",
        "discard_and_switch": "Elo wiesselen",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Säiten als Biller exportéieren',
        'export_images_menu': 'Als Biller exportéieren (PNG/JPEG)',
        'export_images_format': 'Bildformat:',
        'export_images_dpi': 'Resolutioun (DPI):',
        'export_images_quality': 'JPEG-Qualitéit:',
        'export_images_range': 'Säiteberäich:',
        'export_images_all_pages': 'All Säiten',
        'export_images_custom_range': 'Personaliséierte Beräich',
        'export_images_from': 'Vun:',
        'export_images_to': 'Bis:',
        'export_images_options': 'Optiounen:',
        'export_images_single_files': 'All Säit als eenzel Datei',
        'export_images_subfolder': 'An Ënneruerdnung exportéieren',
        'export_images_subfolder_info': 'An Ënneruerdnung "PDFNumm_Biller"',
        'export_images_same_folder': 'An der selwechter Uerdnung wéi d\'PDF',
        'export_images_apply_darkmode': 'PDFDarkView-Astellungen uwenden (Däischter Modus)',
        'export_images_target_folder': 'Ziluerdnung:',
        'export_images_browse': 'Duerchsichen...',
        'export_images_preview': 'Virschau:',
        'export_images_preview_info': 'Wielt d\'Astellunge fir den Export',
        'export_images_preview_info_detail': '{0} Säiten als {1}\nResolutioun: {2} DPI\nDateinumm: {3}\n{4}',
        'export_images_select_folder': 'Ziluerdnung auswielen',
        'export_images_start': 'Billexport starten...',
        'export_images_progress': 'Biller exportéieren...',
        'export_images_saving': 'Späicheren Säit {0} vu {1}...',
        'export_images_success': 'Export erfollegräich!\n\n{0} Biller goufen gespäichert an:\n{1}',
        'export_images_complete': 'Billexport ofgeschloss',
        'export_images_open_folder': '📁 Uerdnung opmaachen',
        'export_images_cancel': 'Billexport ofgebrach',
        'export_images_error_format': 'Feeler beim Exportéiere vun de Biller: {0}',
        'export_images_pdf2image_missing': 'D\'Bibliothéik "pdf2image" ass net installéiert.\n\nW.e.g. installéiert se mat:\npip install pdf2image\n\nFir Windows braucht Dir och Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A-Konvertéierung fir laangfristeg Archivéierung',
        'pdfa_menu': 'PDF/A-Konvertéierung (archivtauglech)',
        'pdfa_info': 'Konvertéiert d\'PDF an e PDF/A-Format.\n\nPDF/A ass speziell fir laangfristeg Archivéierung entwéckelt a garantéiert datt d\'Dokument och an Zukunft korrekt ugewise gëtt.',
        'pdfa_standard': 'PDF/A-Standard:',
        'pdfa_standard_select': 'Versioun:',
        'pdfa_1': 'PDF/A-1 (einfach, breet kompatibel)',
        'pdfa_2': 'PDF/A-2 (modern, besser Kompressioun)',
        'pdfa_3': 'PDF/A-3 (neiste Versioun, erlaabt Usätz)',
        'pdfa_standards_explanation': '📖 Erklärung vun de Standarden:\n\n'
            '• PDF/A-1: Basis, kompatibel mat méi ale Systemer (ongeféier 2005)\n'
            '• PDF/A-2: Moderner, besser Kompressioun, Transparenz-Ënnerstëtzung (ongeféier 2011)\n'
            '• PDF/A-3: Neiste Versioun, erlaabt d\'Afüge vu Datei Usätz (ongeféier 2013)\n\n'
            'Empfehlung: PDF/A-2 ass e gudde Kompromëss tëscht Kompatibilitéit a moderne Funktiounen.',
        'pdfa_options': 'Optiounen:',
        'pdfa_compress_enable': 'PDF kompriméieren (méi kleng Datei)',
        'pdfa_metadata_preserve': 'Metadate behalen (Titel, Auteur, asw.)',
        'pdfa_target_folder': 'Ziluerdnung:',
        'pdfa_browse': 'Duerchsichen...',
        'pdfa_select_folder': 'Ziluerdnung auswielen',
        'pdfa_ocr_info_unknown': '🔍 Konnt Textinhalt net iwwerpréiwen.',
        'pdfa_ocr_info_not_needed': '✅ Text present - OCR ass net néideg.\nPDF/A kann direkt erstallt ginn.',
        'pdfa_ocr_info_recommended': '⚠️ Kee genuch Text fonnt.\n\nFir duerchsichtbar PDFe empfeele mir virdrun OCR duerchzeféieren.\nHinweis: PDF/A funktionéiert och ouni OCR - awer den Text ass dann net duerchsichtbar.',
        'pdfa_ocr_info_error': '❌ Feeler beim Iwwerpréiwen: {0}',
        'pdfa_start': 'PDF/A-Konvertéierung starten...',
        'pdfa_progress': 'PDF/A-Konvertéierung leeft...',
        'pdfa_success': 'PDF/A-Konvertéierung erfollegräich!\n\nGespäichert als:\n{0}\n\nWëllt Dir déi nei PDF opmaachen?',
        'pdfa_complete': 'PDF/A-Konvertéierung ofgeschloss',
        'pdfa_cancel': 'PDF/A-Konvertéierung ofgebrach',
        'pdfa_error_format': 'Feeler bei der PDF/A-Konvertéierung:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'D\'Bibliothéik "ocrmypdf" ass net installéiert.\n\nW.e.g. installéiert se mat:\npip install ocrmypdf',
        'btn_convert': 'Konvertéieren',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF optimiséieren (Dateigréisst reduzéieren)',
        'optimize_menu': 'PDF optimiséieren (Dateigréisst)',
        'optimize_info': 'Reduzéiert d\'Dateigréisst vun der PDF duerch verschidden Optimiséierungsmethoden.\n\nWat méi héich d\'Kompressiounsstuf, wat méi kleng d\'Datei gëtt - bei méiglechem Qualitéitsverloscht bei Biller.',
        'optimize_level': 'Kompressiounsstuf:',
        'optimize_level_low': 'Niddreg (schnell, kleng Erspuernes)',
        'optimize_level_medium': 'Mëttel (gudde Kompromëss)',
        'optimize_level_high': 'Héich (stark Erspuernes)',
        'optimize_level_maximum': 'Maximum (maximal Erspuernes, lues)',
        'optimize_level_explanation': 'Empfehlung: "Mëttel" ass e gudde Kompromëss tëscht Geschwindegkeet an Dateigréisst.',
        'optimize_options': 'Optiounen:',
        'optimize_compress_images': 'Biller kompriméieren (JPEG-Qualitéit reduzéieren)',
        'optimize_clean_objects': 'Net benotzt Objeten ewechhuelen',
        'optimize_preserve_metadata': 'Metadate behalen (Titel, Auteur, asw.)',
        'optimize_image_quality': 'Bildqualitéit:',
        'optimize_range': 'Säiteberäich:',
        'optimize_all_pages': 'All Säiten',
        'optimize_custom_range': 'Personaliséierte Beräich',
        'optimize_from': 'Vun:',
        'optimize_to': 'Bis:',
        'optimize_target_folder': 'Ziluerdnung:',
        'optimize_browse': 'Duerchsichen...',
        'optimize_select_folder': 'Ziluerdnung auswielen',
        'optimize_info_box': 'Informatioun',
        'optimize_info_text': 'D\'Optimiséierung kann bei grousse PDFe puer Minutten daueren.\n\nBiller gi mat reduzéierter Qualitéit gespäichert, wat d\'Dateigréisst bedeitend reduzéiere kann.',
        'optimize_start': 'PDF-Optimiséierung starten...',
        'optimize_progress': 'PDF gëtt optimiséiert...',
        'optimize_cancel': 'PDF-Optimiséierung ofgebrach',
        'optimize_complete': 'PDF-Optimiséierung ofgeschloss',
        'optimize_error_format': 'Feeler bei der PDF-Optimiséierung:\n\n{0}',
        'optimize_success_message': 'PDF-Optimiséierung erfollegräich!\n\nGespäichert als:\n{0}\n\nVirdrun: {1}\nDuerno: {2}\nErspuernes: {3:.1f}%\n\n{4}\n\nWëllt Dir déi optimiséiert PDF opmaachen?',
        'optimize_success_message_no_size': 'PDF-Optimiséierung erfollegräich!\n\nGespäichert als:\n{0}\n\nGréisstinformatioun net verfügbar.\n\nWëllt Dir déi optimiséiert PDF opmaachen?',
        'optimize_result_positive': 'D\'Datei gouf ëm {0:.1f}% méi kleng gemaach.',
        'optimize_result_zero': 'Keng Verännerung vun der Dateigréisst.',
        'optimize_result_negative': 'D\'Datei ass ëm {0:.1f}% méi grouss ginn.\nD\'Optimiséierung gouf iwwersprongen, d\'Originaldatei gouf behalen.',
        'btn_optimize': 'Optimiséierung starten',
        'filename_optimize_low_suffix': '_optimiséiert_niddreg',
        'filename_optimize_medium_suffix': '_optimiséiert',
        'filename_optimize_high_suffix': '_optimiséiert_héich',
        'filename_optimize_maximum_suffix': '_optimiséiert_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF zoueschneiden',
        'crop_menu': 'PDF zoueschneiden (Crop)',
        'crop_range': 'Uwenden op:',
        'crop_all_pages': 'All Säiten',
        'crop_current_page': 'Nëmmen aktuell Säit',
        'crop_values': 'Crop-Wäerter (a Punkten):',
        'crop_left': 'Lénks:',
        'crop_right': 'Riets:',
        'crop_top': 'Uewen:',
        'crop_bottom': 'Ënnen:',
        'crop_presets': 'Virastellungen:',
        'crop_preset_white': 'Wäiss Ränner erkennen',
        'crop_reset': 'Zrécksetzen',
        'crop_mouse_hint': '🖱️ Zitt e Rechteck fir de Beräich ongeféier auszewielen.\nDuerno kënnt Dir d\'Wäerter an de SpinBoxe genee ajustéieren.\nEng manuell Ajustéierung mat der Maus ass net méiglech.',
        'crop_apply': 'Zouschneiden',
        'crop_scope_all': 'All Säiten',
        'crop_scope_current': 'Aktuell Säit',
        'crop_new_size': 'Nei Gréisst: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Keng PDF gelueden',
        'crop_preview_error': 'Feeler beim Luede vun der Virschau',
        'crop_start': 'Zouschneiden starten...',
        'crop_progress': 'PDF gëtt zougeschnidden...',
        'crop_success': 'PDF erfollegräich zougeschnidden!\n\nGespäichert als:\n{0}\n\nWëllt Dir déi zougeschnidden PDF opmaachen?',
        'crop_complete': 'Zouschneiden ofgeschloss',
        'crop_cancel': 'Zouschneiden ofgebrach',
        'crop_error_format': 'Feeler beim Zouschneiden:\n\n{0}',
        'filename_crop_suffix': '_zougeschnidden',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF glätten (Flatten)',
        'flatten_menu': 'PDF glätten (Flatten)',
        'flatten_info': 'D\'Glätte vun enger PDF "brennt" all editéierbar Elementer an de Säiteninhalt.\n\nDuerno si Formulairen, Annotatiounen, Texter, Kräizer, Signaturer, Biller a Formen net méi eenzel editéierbar.',
        'flatten_explanation_title': '📖 Woufir ass dat gutt?',
        'flatten_explanation_text': 'D\'Glätte gëtt an dëse Situatioune gebraucht:\n\n'
            '• 📄 Dir wëllt d\'Dokument fir den Drock virbereeden\n'
            '• 🔒 Dir wëllt verhënneren datt een Formulairen ännert\n'
            '• 📎 Dir wëllt Annotatiounen a Kommentarer "fest" am Dokument afügen\n'
            '• 🖼️ Dir wëllt agefügte Texter, Kräizer, Signaturer, Biller a Formen dauerhaft am Dokument verankeren\n'
            '• 📦 Dir wëllt d\'Datei fir d\'Archivéierung virbereeden\n\n'
            'D\'Glätte mécht d\'PDF méi kleng a verhënnert datt Elementer zoufälleg geréckelt oder geläscht ginn.',
        'flatten_what_title': 'Wat gëtt geglätt?',
        'flatten_what_list': '• ✅ Formulairen (Textfelder, Checkboxen, Knäppercher)\n'
            '• ✅ Annotatiounen (Kommentarer, Markéierungen, Notizen)\n'
            '• ✅ Overlays (Texter, Kräizer, Signaturer, Biller, Formen)',
        'flatten_options': 'Optiounen:',
        'flatten_forms': 'Formulairen glätten',
        'flatten_annotations': 'Annotatiounen glätten',
        'flatten_overlays': 'Overlays glätten (Texter, Kräizer, Signaturer, Biller, Formen)',
        'flatten_target_folder': 'Ziluerdnung:',
        'flatten_browse': 'Duerchsichen...',
        'flatten_select_folder': 'Ziluerdnung auswielen',
        'flatten_warning': '⚠️ Wichteg: D\'Glätte ass en irreversible Prozess!\n\nNom Glätte kënnen editéierbar Elementer net méi eenzel geännert oder geläscht ginn.\nMaacht wann néideg virdrun eng Sécherheetskopie.',
        'flatten_apply': 'Glätten',
        'flatten_start': 'Glätte starten...',
        'flatten_progress': 'PDF gëtt geglätt...',
        'flatten_success': 'PDF erfollegräich geglätt!\n\nGespäichert als:\n{0}\n\nWëllt Dir déi geglätte PDF opmaachen?',
        'flatten_complete': 'Glätte ofgeschloss',
        'flatten_cancel': 'Glätte ofgebrach',
        'flatten_error_format': 'Feeler beim Glätte:\n\n{0}',
        'filename_flatten_suffix': '_geglätt',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF iwwereneenleeën (Overlay)',
        'overlay_menu': 'PDF iwwereneenleeën (Overlay)',
        'overlay_info': 'Leeët eng PDF (Overlay) iwwer eng aner PDF.\n\nD\'Overlay-PDF gëtt op d\'Basis-PDF geluecht. Dat ass nëtzlech fir Waasserzeechen, Logoen, Bréifkäpp oder Stempel.',
        'overlay_explanation_title': '📖 Woufir ass dat gutt?',
        'overlay_explanation_text': 'D\'Iwwereneenleeë gëtt an dëse Situatioune gebraucht:\n\n'
            '• 🏢 E Firme-Logo als Waasserzeechen op all Säit leeën\n'
            '• 📄 E Bréifkapp op eng eidel PDF leeën\n'
            '• 🖊️ E Stempel-Overlay op en Dokument leeën\n'
            '• 🔖 E Waasserzeechen op all Säite leeën\n'
            '• 📑 E Formulaire-Overlay op eng Virlag leeën',
        'overlay_type': 'Overlay-Typ:',
        'overlay_type_fullpage': 'Ganz Säit (deckend)',
        'overlay_type_transparent': 'Ganz Säit (transparent - empfohlen)',
        'overlay_type_stamp': 'Stempel (positionéierbar)',
        'overlay_type_info_fullpage': '📄 D\'Overlay-PDF gëtt exakt iwwer déi ganz Säit geluecht.\nDe wäissen Hannergrond kann ewechgeholl ginn, sou datt nëmmen den Inhalt siichtbar bleift.',
        'overlay_type_info_transparent': '🔍 D\'Overlay-PDF gëtt mat transparentem Hannergrond iwwer déi ganz Säit geluecht.\nDe wäissen Hannergrond gëtt automatesch ewechgeholl - ideal fir Waasserzeechen a Logoen!',
        'overlay_type_info_stamp': '🖊️ D\'Overlay-PDF gëtt als Stempel positionéiert a skaléiert.\nPerfekt fir Logoen, Stempel oder Signaturer op bestëmmte Positiounen.',
        'overlay_remove_background': 'Wäissen Hannergrond ewechhuelen:',
        'overlay_remove_background_enable': 'Wäissen Hannergrond vun der Overlay-PDF ewechhuelen (mécht d\'Overlay transparent)',
        'overlay_remove_background_tooltip': 'Hëlt wäiss Beräicher aus der Overlay-PDF ewech, sou datt den ënnerleeënde Text siichtbar gëtt.',
        'overlay_threshold': 'Schwellewäert:',
        'overlay_threshold_hint': '(1-254, méi héich = méi Wäiss gëtt ewechgeholl)',
        'overlay_select_file': 'Overlay-PDF auswielen:',
        'overlay_file_placeholder': 'W.e.g. wielt eng PDF-Datei fir d\'Overlay',
        'overlay_browse': 'Duerchsichen...',
        'overlay_select_overlay': 'Overlay-PDF auswielen',
        'overlay_range': 'Säiteberäich:',
        'overlay_all_pages': 'All Säiten',
        'overlay_custom_range': 'Personaliséierte Beräich',
        'overlay_from': 'Vun:',
        'overlay_to': 'Bis:',
        'overlay_position': 'Positioun:',
        'overlay_position_center': 'Mëtt',
        'overlay_position_top_left': 'Uewe lénks',
        'overlay_position_top_right': 'Uewe riets',
        'overlay_position_bottom_left': 'Ënne lénks',
        'overlay_position_bottom_right': 'Ënne riets',
        'overlay_size': 'Gréisst:',
        'overlay_size_original': 'Originalgréisst',
        'overlay_size_fit_page': 'Un Säit upassen',
        'overlay_size_custom': 'Personaliséiert (%)',
        'overlay_opacity': 'Transparenz:',
        'overlay_target_folder': 'Ziluerdnung:',
        'overlay_browse_folder': 'Duerchsichen...',
        'overlay_select_folder': 'Ziluerdnung auswielen',
        'overlay_warning': '⚠️ Hinweis: D\'Overlay-PDF gëtt op d\'Basis-PDF geluecht an dobäi "agebrannt".\n\nD\'Elementer vun der Overlay-PDF kënnen nom Späicheren net méi eenzel beaarbecht ginn.',
        'overlay_apply': 'Iwwereneenleeën',
        'overlay_start': 'Iwwereneenleeë starten...',
        'overlay_progress': 'PDF gëtt iwwereneegeluecht...',
        'overlay_success': 'PDF erfollegräich iwwereneegeluecht!\n\nGespäichert als:\n{0}\n\nWëllt Dir déi iwwereneegeluecht PDF opmaachen?',
        'overlay_complete': 'Iwwereneenleeë ofgeschloss',
        'overlay_cancel': 'Iwwereneenleeë ofgebrach',
        'overlay_error_format': 'Feeler beim Iwwereneenleeë:\n\n{0}',
        'overlay_no_file': 'Et gouf keng Overlay-PDF ausgewielt.\n\nW.e.g. wielt eng PDF-Datei fir iwwereneenzeleeën.',
        'filename_overlay_suffix': '_iwwereneegeluecht',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Biller aus PDF extrahéieren',
        'extract_images_menu': 'All Biller extrahéieren',
        'extract_images_info': 'Extraheiert all Biller aus der PDF a späichert se als eenzel Dateien.\n\nD\'Biller ginn an hirem Originalformat oder an engem ausgewielte Format konvertéiert.',
        'extract_images_format': 'Bildformat:',
        'extract_images_quality': 'JPEG-Qualitéit:',
        'extract_images_options': 'Optiounen:',
        'extract_images_subfolder': 'An Ënneruerdnung extrahéieren ("PDFNumm_Biller")',
        'extract_images_unique': 'Nëmmen eenzegaarteg Biller (Dublécke vermeiden)',
        'extract_images_range': 'Säiteberäich:',
        'extract_images_all_pages': 'All Säiten',
        'extract_images_custom_range': 'Personaliséierte Beräich',
        'extract_images_from': 'Vun:',
        'extract_images_to': 'Bis:',
        'extract_images_target_folder': 'Ziluerdnung:',
        'extract_images_browse': 'Duerchsichen...',
        'extract_images_select_folder': 'Ziluerdnung auswielen',
        'extract_images_info_box': 'Informatioun',
        'extract_images_info_text': 'D\'Extraktioun kann bei grousse PDFe puer Minutten daueren.\n\nBiller gi mat hirem originelle Numm (Säit_Bild) gespäichert.',
        'extract_images_extract': 'Extraheieren',
        'extract_images_start': 'Extraktioun starten...',
        'extract_images_progress': 'Biller ginn extrahéiert...',
        'extract_images_success': '✅ Biller erfollegräich extrahéiert!\n\n{0} Biller goufen gespäichert an:\n{1}',
        'extract_images_complete': 'Bild-Extraktioun ofgeschloss',
        'extract_images_cancel': 'Extraktioun ofgebrach',
        'extract_images_error_format': 'Feeler beim Extraheiere vun de Biller:\n\n{0}',
        'extract_images_open_folder': '📁 Uerdnung opmaachen',
        'extract_images_no_images': 'Keng Biller an der PDF fonnt.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Méi Säiten op enger Säit (N-Up)',
        'nup_menu': 'Méi Säiten op enger Säit (N-Up)',
        'nup_info': 'Uerdnet verschidde PDF-Säiten op enger Säit.\n\nIdeal fir kompakt Dréck, Iwwersichten oder Handouts.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Virschau:',
        'nup_preview_info': '{0} Säiten → {1} Säite pro Blat → {2} Blieder\nLayout: {3}',
        'nup_order': 'Reiefolleg:',
        'nup_order_horizontal': 'Horizontal (Reieweis)',
        'nup_order_vertical': 'Vertikal (Kolonneweis)',
        'nup_order_horizontal_reverse': 'Horizontal réckwäerts',
        'nup_order_vertical_reverse': 'Vertikal réckwäerts',
        'nup_range': 'Säiteberäich:',
        'nup_all_pages': 'All Säiten',
        'nup_custom_range': 'Personaliséierte Beräich',
        'nup_from': 'Vun:',
        'nup_to': 'Bis:',
        'nup_options': 'Optiounen:',
        'nup_margins': 'Ränner:',
        'nup_margin_between': 'Ofstand tëscht de Säiten:',
        'nup_page_numbers': 'Säitenzuelen afügen',
        'nup_target_folder': 'Ziluerdnung:',
        'nup_browse': 'Duerchsichen...',
        'nup_select_folder': 'Ziluerdnung auswielen',
        'nup_create': 'Erstellen',
        'nup_start': 'N-Up starten...',
        'nup_progress': 'N-Up gëtt erstallt...',
        'nup_success': 'N-Up erfollegräich erstallt!\n\nGespäichert als:\n{0}\n\nWëllt Dir déi nei PDF opmaachen?',
        'nup_complete': 'N-Up ofgeschloss',
        'nup_cancel': 'N-Up ofgebrach',
        'nup_error_format': 'Feeler bei N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Säitegréisst änneren',
        'pagesize_menu': 'Säitegréisst änneren',
        'pagesize_info': 'Ännert d\'Säitegréisst vun der PDF.\n\nDen Inhalt gëtt automatesch un déi nei Gréisst ugepasst.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Wielt e Standardformat:',
        'pagesize_custom': 'Personaliséiert Gréisst:',
        'pagesize_width': 'Breet:',
        'pagesize_height': 'Héicht:',
        'pagesize_orientation': 'Ausrichtung:',
        'pagesize_portrait': 'Héichformat',
        'pagesize_landscape': 'Querformat',
        'pagesize_scale_options': 'Skaléierungsoptioune:',
        'pagesize_fit': 'Upassen (Säiteverhältnis behalen)',
        'pagesize_stretch': 'Strecken (Verzerren)',
        'pagesize_center': 'Zentréieren (Originalgréisst)',
        'pagesize_range': 'Säiteberäich:',
        'pagesize_all_pages': 'All Säiten',
        'pagesize_custom_range': 'Personaliséierte Beräich',
        'pagesize_from': 'Vun:',
        'pagesize_to': 'Bis:',
        'pagesize_target_folder': 'Ziluerdnung:',
        'pagesize_browse': 'Duerchsichen...',
        'pagesize_select_folder': 'Ziluerdnung auswielen',
        'pagesize_apply': 'Uwenden',
        'pagesize_start': 'Säitegréisst änneren starten...',
        'pagesize_progress': 'Säitegréisst gëtt geännert...',
        'pagesize_success': 'Säitegréisst erfollegräich geännert!\n\nGespäichert als:\n{0}\n\nWëllt Dir déi nei PDF opmaachen?',
        'pagesize_complete': 'Säitegréisst ännere ofgeschloss',
        'pagesize_cancel': 'Säitegréisst ännere ofgebrach',
        'pagesize_error_format': 'Feeler beim Säitegréisst ännere:\n\n{0}',
        'pagesize_preview_info': 'Nei Gréisst: {0} x {1} pt',
        'filename_pagesize_suffix': '_neiGréisst',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-Informatiounen',
        'pdf_info_menu': 'PDF-Info weisen',
        'pdf_info_voice': 'PDF-Informatioune gi gewisen',
        'pdf_info_error': 'Feeler beim Weise vun der PDF-Info:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Tastaturkuerzel weisen",
        "shortcuts_dialog_title": "Tastaturkuerzel",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 DATEI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF opmaachen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF zoumaachen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Späicheren als...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Dokument schützen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Drécken</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Sofort drécken (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Applikatioun zoumaachen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Als Pages exportéieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Als DOCX exportéieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Als TXT exportéieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Als Biller exportéieren (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Biller extrahéieren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTERVERARBEEDUNG</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Méi Säiten)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A-Konvertéierung (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF glätten</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF iwwereneenleeën</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF optimiséieren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ BEARBEETEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Sichen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Lieszeechen derbäisetzen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Lieszeechen verwalten</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Nächst Lieszeechen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Viregt Lieszeechen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR duerchféieren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SÄITEVERWALTUNG</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Aktuell Säit dréinen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>All Säiten dréinen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Aktuell Säit normaliséieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>All Säiten normaliséieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Säiten läschen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Säiten enthuelen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Säiten afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Säite réckelen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDFe zesummefügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Säitegréisst änneren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 AFÜGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Text afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Kräiz afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Signatur 1 afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Signatur 2 afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Bild afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rechteck afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ellips afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Linn afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Pfeil afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Säitenzuelen afügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Text-Waasserzeechen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Bild-Waasserzeechen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ RÉCHIRUNGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Réchirung (schwaarz)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Réchirung (wäiss)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>All Réchirungen uwenden</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ FORTGESCHRIDDEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF zouschneiden</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Metadaten beaarbechten</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ USICHT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Däischter/Liicht Modus wiesselen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Textfënster weisen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Säitebreet (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Zwee Säiten (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Iwwersiicht (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ASTELLUNGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Passwuertverwaltung</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR-Astellungen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Signatur-Astellungen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Dateinumm-Formatéierung</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Astellunge exportéieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Astellunge importéieren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF-Info weisen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Sproochausgab un/aus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Menübar fokusséieren</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nei Versioun disponibel",
        "update_available_message": "Et gëtt eng nei Versioun <b>{0}</b>.\n\nBesicht d'Release-Säit fir den Update erofzelueden:\n{1}",
        "update_available_voice": "Nei Versioun {0} disponibel. Lued den Update vun der GitHub-Säit erof.",
        "update_open_release": "Release Säit opmaachen",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "All Iwwersetzungen eroflueden",
        "ask_download_all_translations": """Nieft Däitsch, Englesch a Vietnamesesch ginn et nach {total_languages} aner GUI-Sproochen.\n\nSolle se zur Verfügung gestallt / aktualiséiert ginn?\n\nHinweis:\nNet néideg Sprooche kënnt Dir méi spéit am Verzeechnes:\n{translations_path}
        manuell läschen.\n\nWann Dir ofbriechen, kënnt Dir d'GUI-Sprooche méi spéit iwwer de Menü 'Extras → Iwwersetzungen aktualiséieren' eroflueden.""",
        "menu_update_translations": "Iwwersetzungen aktualiséieren",
        "translations_updated": "Iwwersetzungen aktualiséiert",
        "translations_update_success": "{} Iwwersetzunge goufe succesvoll aktualiséiert ({} nei, {} aktualiséiert).",
        "translations_update_error": "Feeler beim Aktualiséiere vun den Iwwersetzungen",
        "translations_update_no_changes": "All Iwwersetzunge si scho aktuell.",
        "translations_update_offline": "Keng Internetverbindung. Iwwersetzunge konnten net aktualiséiert ginn.",
        "translations_update_in_progress": "Iwwersetzunge ginn am Hannergrond aktualiséiert...",
        "translations_downloading": "Lued Iwwersetzungen erof...",
        "translations_path_hint": "Benotzerverzeechnes fir Iwwersetzungen",
        "translations_update_not_available_title": "Update net disponibel",
        "translations_update_not_available_message": """D'Aktualiséierung vun den Iwwersetzungen ass nëmmen an der installéierter Versioun verfügbar.\n\nAm Entwécklungsmodus sinn d'Iwwersetzunge scho aktuell.""",
        "translations_update_no_internet_title": "Keng Internetverbindung",
        "translations_update_no_internet_message": """Et konnt keng Internetverbindung hiergestallt ginn.\n\nD'Iwwersetzunge kënnen net vu GitHub erofgeluede ginn.\n\nMéiglech Léisungen:
        • Préift Är Internetverbindung
        • Deaktivéiert eng eventuell Firewall kuerzfristeg
        • Probéiert et méi spéit nach eng Kéier
        \nDir kënnt d'Iwwersetzungen och manuell vu GitHub eroflueden:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Update leeft scho",
        "btn_retry": "Nach eng Kéier probéieren",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Wëllkomm bei PDF Dark View",
        "welcome_title_not_supported": "Wëllkomm bei PDF Dark View",
        "welcome_message": "Wëllkomm bei PDF Dark View!\n\nÄr Systemsprooch gouf als '{language}' erkannt.\nWëllt Dir dës Sprooch fir d'Benotzeroberfläche benotzen?\n\nDir kënnt d'Sprooch zu all Moment iwwer 'Astellungen → Sprooch' änneren.",
        "welcome_message_language_not_available": "Wëllkomm bei PDF Dark View!\n\nÄr Systemsprooch gouf als '{language}' erkannt.\nDës Sprooch ass nach net installéiert.\n\nWëllt Dir d'Iwwersetzunge fir {language} elo vu GitHub eroflueden?\n\n(D'Sprooch gëtt dann automatesch fir d'Benotzeroberfläche benotzt.)",
        "welcome_message_language_not_supported": "Wëllkomm bei PDF Dark View!\n\nÄr Systemsprooch gouf als '{language}' erkannt.\nLeider gëtt et fir dës Sprooch nach keng Iwwersetzungen.\n\nD'Benotzeroberfläche gëtt dofir op {fallback_language} ugewisen.\n\nDir kënnt d'Sprooch zu all Moment iwwer 'Astellungen → Sprooch' änneren.\nWann Dir wëllt, kënnt Dir och selwer eng Iwwersetzung fir Är Sprooch bäidroen:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Jo, Systemsprooch benotzen",
        "welcome_keep_english": "Nee, Englesch behalen",
        "welcome_download_language": "Jo, {language} eroflueden",

        # ============================================
        # 107. LESCHT BENOTZT PÄIF
        # ============================================

        'menu_recent': 'Lescht benotzt',
        'menu_recent_dirs': 'Dossieren...',
        'menu_recent_files': 'Fichieren...',
        'recent_manage': 'Verwalten...',
        'recent_enable_tracking': 'Lescht benotzt Päif späicheren (Dateschutz)',
        'recent_enable_info': 'Schalt dës Optioun aus, fir keng Päif ze späicheren',
        'recent_tracking_disabled': 'Päifverfolgung ausgeschalt',
        'recent_enabled': 'aktivéiert',
        'recent_disabled': 'deaktivéiert',
        'recent_tracking_status': 'Päifverfolgung {0}',
        'recent_dialog_title': 'Lescht benotzt Päif',
        'recent_tab_directories': 'Dossieren',
        'recent_tab_files': 'Fichieren',
        'recent_dirs_instruction': 'Duebelklick fir den Fichierdialog am Dossier ze oppen',
        'recent_files_instruction': 'Duebelklick fir de PDF direkt ze oppen',
        'recent_no_directories': '(keng Dossiere gespäichert)',
        'recent_no_files': '(keng Fichiere gespäichert)',
        'recent_default_current': '⭐ Standard: {0}',
        'recent_set_as_default': '⭐ Als Standard setzen',
        'recent_default_set_title': 'Standarddossier gesat',
        'recent_default_set_message': 'Den Dossier "{0}" gouf als Standard fir d\'Öffne vu PDFe gesat.',
        'recent_default_set_voice': 'Standarddossier gouf gesat',
        'recent_directory_not_found': 'Dossier net fonnt',
        'recent_file_not_found': 'Fichier net fonnt',
        'recent_remove_selected': 'Ewechhuelen',
        'recent_remove_title': 'Päif ewechhuelen',
        'recent_remove_confirm': 'Wëllt Dir de Päif "{0}" wierklech aus der Lëscht ewechhuelen?',
        'recent_path_removed': 'Päif gouf ewechgeholl',
        'recent_clear_all': 'All ewechhuelen',
        'recent_clear_title': 'All Päif ewechhuelen',
        'recent_clear_confirm_type': 'Wëllt Dir wierklech all {0} läschen?',
        'recent_cleared': 'Lëscht gouf geläscht',
        'recent_path_not_found_title': 'Päif net fonnt',
        'recent_path_not_found_message': 'De Päif "{0}" gëtt et net méi.',
        'recent_open_file': 'Fichier opmaachen',
        'btn_open_recent': 'Opmaachen',
        'recent_open_file_question': 'Wëllt Dir "{0}" als PDF opmaachen?',
        'recent_not_pdf': 'Den ausgewielte Fichier ass kee PDF.',
        'recent_more_entries': 'Méi Anträg...',
        'btn_remove': 'Ewechhuelen',
        'btn_clear': 'All läschen',
        'recent_context_open': 'Opmaachen',
        'recent_context_reveal': 'Am Finder weisen',
        'recent_context_set_default': '⭐ Als Standard setzen',
        'recent_context_open_terminal': '💻 Terminal opmaachen',
        'recent_context_file_info': 'Fichierinfo',
        'recent_context_open_with_default': '📄 Mat Standard-App opmaachen',
        'recent_context_remove': 'Aus der Lëscht huelen',
        'recent_context_clear_all': 'All ewechhuelen',
        'recent_file_info_title': 'Fichierinformatiounen',
        'recent_file_info_name': 'Numm',
        'recent_file_info_path': 'Päif',
        'recent_file_info_size': 'Gréisst',
        'recent_file_info_modified': 'Geännert',
        'recent_file_info_pages': 'Säiten',
        'recent_error_reveal': 'Feeler beim Opmaachen am Finder',
        'recent_error_terminal': 'Feeler beim Opmaache vum Terminal',
        'recent_error_info': 'Feeler beim Ofruffe vun de Fichierinformatiounen',
        'open_user_data_folder': 'Benotzerdaten-Dossier weisen',

        # ============================================
        # 108. GERAD/ONGERAD SÄITEN LÄSCHEN
        # ============================================
        "pages_delete_even": "All gerad Säiten läschen",
        "pages_delete_odd":  "All ongerad Säiten läschen",
        "progress_even_pages": "Gerad Säite gi geläscht",
        "progress_odd_pages": "Ongerad Säite gi geläscht",
        "progress_mark_delete_even": "{} gerad Säit(en) fir d\'Läschen markéiert",
        "progress_mark_delete_odd":  "{} ongerad Säit(en) fir d\'Läschen markéiert",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programm gëtt zougemaach",

    }
