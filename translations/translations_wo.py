
# ============================================
# translations_wo.py - Wolof Wörterbuch (Senegal)
# Vollständig sortiert nach Kategorien
# ============================================

def load_wolof_strings():
    """Lädt alle wolofischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View ci BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Yebi PDF",
        'btn_text_window': "Mbind OCR",
        'btn_first': "Xët jëkkaan",
        'btn_prev': "Xët bi ci kanam",
        'btn_next': "Xët bi ci topp",
        'btn_last': "Xët bu mujj",
        'btn_print': "Móol",
        'btn_darkmode_light': "Nopp bu leet",
        'btn_darkmode_dark': "Nopp bu ñuul",
        'btn_delete_pages': "Far xët yi",
        'btn_extract_pages': "Gëwal xët yi",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "Baax na",
        'btn_cancel': "Far",
        'btn_save': "Denci",
        'btn_close': "Tëj",
        'btn_delete': "Far",
        'btn_delete_all': "Far lépp",
        'btn_copy': "Sanc",
        'btn_export': "Yóbbu ci biti",
        'btn_show': "Wone baat biir",
        'btn_hide': "Nëbb baat biir",
        'btn_authenticate': "Seetal sa bopp",
        'btn_settings': "Jekkal",
        'btn_protect': "Aar",
        'btn_remove_password': "Far baat biir",
        'btn_manage': "Jëfandikoo baat biir",
        'btn_retry': "Esayatiy ci naw",
        'btn_select_all': "Tàllal lépp",
        'btn_clear_selection': "Far tàllal",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Xët {0} ci {1}",
        'page_count': "ci {0}",
        'goto_page': "Dem ci xët",
        'page_simple': "Xët {0}",
        'full_view_page': "Wonu mbubb xët {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Duggal baat laaj + Enter",
        'search_results': "Seet: {0} ci {1}",
        'search_nav_hint': "Enter: ci topp (Shift+Enter: ci kanam)",
        'search_no_results': "Amul luy seet",
        'search_error': "Njuumte ci seet",
        'search_active': "Fajwa seet tàmbali na",
        'search_closed': "Seet mujj na",
        'search_position': "Xët {0} {1}",
        'search_pos_top': "kaw",
        'search_pos_upper': "kaw",
        'search_pos_middle': "digg",
        'search_pos_lower': "suuf",
        'search_pos_bottom': "suuf",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Mbind gënotal dafa doxe baax na!",
        'ocr_success_title': "OCR doxe na",
        'ocr_success_message': "Denc bi man nañu ko seet.",
        'ocr_failed': "OCR doxe wut",
        'ocr_in_progress': "OCR taxaw na",
        'ocr_preparing': "PDF day jekk...",
        'ocr_analyzing': "PDF day xool ci...",
        'ocr_optimizing': "Nataal day baax yóbb...",
        'ocr_recognizing': "Mbind day gënotal...",
        'ocr_embedding': "Mbind day duggu...",
        'ocr_finalizing': "PDF day mujjal...",
        'ocr_not_available': "OCR amul",
        'ocr_install_message': "Jëfandikukaay yi OCR amuñu.\n\nJoxal ñoom:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR lañu koy soxla",
        'ocr_question': "PDF bi amul mbind gu man nga seet.\nDanga waxle a defar OCR ngir {0} man a dox?",
        'ocr_perform': "Defar OCR",
        'ocr_later': "Ci kanam",
        'ocr_starting': "OCR gu dalal day tàmbali...",
        'ocr_success_voice': "OCR doxe na. PDF bi man nañu ko seet.",
        'ocr_partial_success': "OCR defar na, waaye am njuumte ci tolofaane.\n\nBind bu seet man dale ci denci:\n{0}\n\nNjuumte: {1}",
        'ocr_partial_title': "OCR doxe na waaye dul lépp",
        'ocr_partial_voice': "OCR defar na, waaye tolofaane doxe wut.",
        'original_file': "Denc ju njëkk:",
        'old_size': "Mag jëkk:    {0} bytes",
        'new_size': "Mag bees: {0} bytes",
        'size_change': "Sol: {0}{1} bytes",
        'backup_created_file': "Santar defar na:\n{0}",
        'backup_not_created': "Santar: amul (jekkal tudd na)",
        'page_header': "=== Xët {0} ===\n{1}\n",
        'scanned_page_header': "=== Xët {0} (scan defar) ===\n[Xët bi am na mbind gu scan defar rekk]\n[Bëgg a defar OCR ci sa bopp]\n",
        'scanned_warning': "⚠️ MBIND GU SCAN DEFAR - OCR LAÑU KO SOXLA",
        'guaranteed_title': "PDF gu seet man defar na",
        'guaranteed_message': "<b>Bind bu seet man gu dalal defar na!</b>\n\nNdax OCR ci saa si doxe wut, PDF bees defar na bu man nga seet:\n\n{0}\n\n<b>Denc bi am na:</b>\n• Mbind gu gëwal (su am)\n• Ay xibaar ci xët yu scan defar\n• Man nga ko seet lépp",
        'guaranteed_voice': "PDF gu seet man gu dalal defar na.",
        'instruction_title': "Ndigal ci OCR",
        'instruction_file': "Denc ju njëkk: {0}",
        'instruction_text': "Mbind gënotal ci saa si (OCR) doxe wut.\nBëgg a defar OCR ci sa bopp:\n\n1. AK OCRmyPDF (ligne de commande):\n   ocrmypdf --force-ocr \"[DENCI]\" \"jéggi.pdf\"\n\n2. AK ADOBE ACROBAT (macOS/Windows):\n   • Yebi PDF ci Acrobat\n   • Jëfandikukaay yi > Soppi PDF\n   • Tànn 'Mbind gënotal'\n\n3. AK PREVIEW (macOS):\n   • Yebi PDF ci Preview\n   • Denc > Yóbbu ci biti...\n   • Quartz filtar: 'Waññi mag denc'\n   • Tànn 'Defar OCR'\n\n4. OCR CI INTERNET:\n   • smallpdf.com/wo/ocr-pdf\n   • ilovepdf.com/wo/ocr-pdf\n   • adobe.com/sn/acrobat/online/pdf-to-word.html",
        'instruction_created': "Ndigal ci OCR defar na",
        'instruction_created_message': "Ndigal gu yomb defar na:\n\n{0}\n\nToppal ay xët yi ngir OCR ci sa bopp.",
        'instruction_created_voice': "Ndigal ci OCR defar na.",
        'ocr_impossible': "OCR manu koy defar",
        'ocr_impossible_message': "OCR manuñu ko defar.\n\nBëgg a yóbb '{0}' ci sa bopp ak program OCR.",
        'ocr_impossible_voice': "OCR manuñu ko defar. Bëgg a yóbb ci sa bopp.",
        'emergency_title': "OCR gu dal",
        'emergency_message': "PDF bu dal defar na:\n\n{0}\n\nBëgg a yóbb denc bi ci sa bopp ak OCR.",
        'emergency_voice': "PDF bu dal defar na. Bëgg a defar OCR ci sa bopp.",
        'critical_error': "Njuumte bu mag",
        'critical_error_message': "OCR manuñu ko tàmbali.\n\nBëgg a tàmbali program bi ci naw ak xool ndax OCR tànn na.",
        'critical_error_voice': "Njuumte bu mag ci OCR",
        'ocr_question_html': "<p>PDF bi amul mbind gu man nga seet.<p>Danga waxle a defar OCR ngir <b>{0}</b> man a dox?</p>",
        'ocr_question_voice': "OCR lañu koy soxla. PDF bi amul mbind gu man nga seet. Danga waxle a defar OCR ngir {0} man a dox?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "Amul PDF bu yeb",
        'no_pdf_message': "Amul PDF bu yeb",
        'pdf_not_found': "Denci PDF amuñu ko gis",
        'file_size': "Mag denc",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Santar defar na",
        'backup_disabled': "Santar tudd na",
        'backup_activated': "Santar ci saa si tànn na",
        'backup_deactivated': "Santar ci saa si tudd na",
        'backup_status': "Santar: {0}",
        'backup_on': "✔ tànn",
        'backup_off': "✘ tudd",
        'close_pdf': "Tëj PDF: {0}",
        'pdf_not_found_format': "Denci PDF amuñu ko gis: {0}",
        'error_pdf_load_format': "Njuumte ci yeb PDF: {0}",
        'load_failed_format': "Yeb doxe wut:\n{0}",
        'decrypted_suffix': "(dëcc nu koo xam)",
        'decryption_failed': "Dëcc xam doxe wut.",
        'decryption_error': "Njuumte ci dëcc xam",
        'decryption_success': "Dëcc xam doxe na",
        'decryption_success_message': "PDF dëcc xam nañu ko, denci ko fii:\n\n{0}",
        'decryption_success_voice': "PDF dëcc xam nañu ko, denci ko.",
        'password_remove_error': "Njuumte ci far baat biir",
        'save_unencrypted': "Denci PDF gu amul lëdal ci nit",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Denci ni...",
        'save_copy': "Denci sanc",
        'save_success': "PDF denci na ci: {0}",
        'save_encrypted': "PDF gu aar denci na ci: {0}",
        'save_error': "PDF manuñu ko denci",
        'encryption_question': "Danga waxle a aar PDF bi ak baat biir?",
        'encryption_yes': "Waaw",
        'encryption_no': "Déet",
        'encryption_cancel': "Far",
        'save_cancel': "Denci far nañu ko",
        'save_encrypted_voice': "Denci lëdal nañu ko, denci ko.",
        'save_success_voice': "Denci PDF denci nañu ko, amul lëdal.",
        'save_error_format': "PDF manuñu ko denci:\n{0}",
        'export_pages_success': "Yóbbu ci Pages doxe na",
        'export_pages_error': "Yóbbu ci Pages doxe wut",
        'export_pages_error_format': "Yóbbu ci Pages doxe wut: {0}",
        'export_word_success': "Yóbbu ci Word doxe na",
        'export_word_error': "Yóbbu ci Word doxe wut",
        'export_word_error_format': "Yóbbu ci Word doxe wut: {0}",
        'export_text_success': "Yóbbu mbind doxe na",
        'export_text_error': "Yóbbu mbind doxe wut",
        'export_text_error_format': "Yóbbu mbind doxe wut: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Baat biir lañu koy soxla",
        'password_enter': "Jox baat biir bi",
        'password_confirm': "Tànn baat biir bi",
        'password_new': "Baat biir bu bees",
        'password_current': "Baat biir bi leegi",
        'password_save': "Denci baat biir (ci lëdal)",
        'password_saved': "✓ Baat biir ci denc bi denci nañu ko",
        'password_wrong': "Baat biir xaaj na",
        'password_mismatch': "Baat biir ño ko xaaj",
        'password_too_short': "Baat biir guddaawul",
        'password_min_length': "Baat biir war a am lu ci ëpp 4 mbind",
        'password_strength': "Doon baat biir",
        'password_strength_very_weak': "Doonul",
        'password_strength_weak': "Doonul rekk",
        'password_strength_medium': "Digg doon",
        'password_strength_strong': "Doon na",
        'password_strength_very_strong': "Doon na lool",
        'password_char_count': "({0} mbind)",
        'password_match': "✓ Moo ngi ko",
        'password_no_match': "✗ Baat biir ñoo ko xaaj",
        'password_show': "Wone",
        'password_hide': "Nëbb",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Jëfandikoo baat biir",
        'password_table_filename': "Tur denc",
        'password_table_password': "Baat biir",
        'password_count': "{0} baat biir denci nañu",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Amul baat biir bu denci",
        'password_copied': "{0} baat biir sanc nañu",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Danga sure ne danga waxle a far baat biir bi ci '{0}'?",
        'password_delete_multiple': "Danga sure ne danga waxle a far ñoom {0} baat biir yu tànn?",
        'password_delete_all_confirm': "Danga sure ne danga waxle a far ñépp {0} baat biir yu denci?",
        'password_deleted': "{0} baat biir far nañu",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Baat biir yépp far nañu",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Bawool baat biir",
        'generator_generated': "Baat biir bu bawool:",
        'generator_regenerate': "Bawool ci naw",
        'generator_copy': "Sanc",
        'generator_use': "Jëfandikoo",
        'generator_settings': "Jekkal",
        'generator_length': "Gudd:",
        'generator_group_every': "Cosaan ci",
        'generator_group_chars': "mbind. Cosaan:",
        'generator_uppercase': "Mbind yu mag (A-Z)",
        'generator_lowercase': "Mbind yu ndaw (a-z)",
        'generator_digits': "Xayma (0-9)",
        'generator_symbols': "Safaanu tukki (!@#$%^&*)",
        'generator_exclude': "Dugguwu ci:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Baat biir bu mag lañu koy soxla",
        'master_password_setup': "Jekkal baat biir bu mag",
        'master_password_change': "Soppi baat biir bu mag",
        'master_password_enter': "Jox sa baat biir bu mag",
        'master_password_choose': "Tànn baat biir bu mag gu doon (lu ci ëpp 8 mbind)",
        'master_password_new': "Jox sa baat biir bu mag bu bees",
        'master_password_confirm': "Tànn baat biir",
        'master_password_authenticate': "Seetal sa bopp",
        'master_password_success': "Baat biir bu mag jekkal nañu ko.",
        'master_password_changed': "Baat biir bu mag soppi nañu ko.",
        'master_password_removed': "Baat biir bu mag ak ñépp baat biir far nañu.",
        'master_password_remove': "Far baat biir bu mag",
        'master_password_remove_confirm': "Danga SURE ne danga waxle a far ñépp baat biir?\n\nLi ngay def manuñu ko def ci naw!",
        'master_password_export_before': "Danga waxle a yóbbu santar bi ci kanam?",
        'master_password_export_delete': "Yóbbu ak far",
        'master_password_delete_now': "Far leegi",
        'master_password_for_signatures': "Ngir jëfandikoo mbind bu bopp, war nga jekkal baat biir bu mag.\n\nDanga waxle a jekkal baat biir bu mag leegi?",
        'master_password_for_private': "Ngir jëfandikoo mbind bu suq, war nga jekkal baat biir bu mag.\n\nDanga waxle a jekkal baat biir bu mag leegi?",
        'master_password_info': """
            <b>🔐 SU AMUL BAAT BIIR BU MAG:</b><br>
            • Wone, sanc ak yóbbu baat biir manuñu koo def<br>
            • Far baat biir man nga koo def (su amul baat biir bu mag itam)<br><br>

            <b>🔐 SU AM BAAT BIIR BU MAG:</b><br>
            • Lépp dina dox su nga seetal sa bopp<br>
            • Baat biir ñoom lëdal nañu leen ak baat biir bu mag<br>
            • Gudd gi ci ëpp: 8 mbind<br>
            • Denci gu aar ak SHA-256 hash<br><br>

            <b>ËMBARE:</b><br>
            • Su nga fàddi baat biir bu mag: baat biir ñoom manuñu leen gis ci naw<br>
            • Su nga far baat biir bu mag: ñépp baat biir dinañu far<br>
            • Man nga yóbbu baat biir ci kanam ba far<br>
            • Baat biir bu mag man nga ko soppi bu baax
        """,
        'signature_auth_disabled': "Far laaj baat biir ci mbind yu bopp",
        'template_auth_disabled': "Far laaj baat biir ci mbind yu suq",
        'master_password_for_signatures_settings': "Ngir jëfandikoo mbind bu bopp, war nga jekkal baat biir bu mag.\n\nDem ci Jekkal - Jëfandikoo baat biir",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Aar PDF",
        'protect_info': "Denci '{0}' dinañu koo aar ak baat biir.",
        'protect_instruction': "Jox baat biir bu baax ñaari yoon ngir aar denc bi, walla jëfandikoo bawool baat biir bu nekk ci ndeyji duggal.",
        'protect_success': "PDF aar nañu ko baax na, denci ko fii:\n{0}\n\nBaat biir: {1}\n\nDanga waxle a yeb PDF bu aar bi leegi?",
        'protect_open': "Waaw",
        'protect_skip': "Déet",
        'protect_error': "Njuumte ci aar PDF",
        'protect_open_title': "Yeb PDF bu aar bi",
        'protect_question': "Mujj na. Danga waxle a yeb PDF bu aar bi leegi? Waaw walla Déet?",
        'password_cancel': "Këru baat biir far nañu ko",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Far xët yi",
        'pages_extract': "Gëwal xët yi",
        'pages_insert': "Duggal xët yi",
        'pages_move': "Indi xët yi",
        'pages_delete_options': "Tànn yu far",
        'pages_delete_empty': "Far xët yu mel ne dell",
        'pages_delete_current': "Far xët bi leegi",
        'pages_delete_range': "Far xët yu ci digg",
        'pages_extract_options': "Tànn yu gëwal",
        'pages_extract_current': "Gëwal xët bi leegi",
        'pages_extract_range': "Gëwal xët yu ci digg",
        'pages_insert_position': "Barab bu duggal",
        'pages_insert_before': "Duggal ci kanam xët:",
        'pages_insert_select': "Tànn PDF",
        'pages_insert_none': "Amul PDF bu tànn",
        'pages_move_source': "Xët yi nga bëgg a indi",
        'pages_move_from': "Ci xët:",
        'pages_move_to': "Ba xët:",
        'pages_move_target': "Barab bu dem",
        'pages_move_before': "Indi ci kanam xët:",
        'pages_move_hint': "Ëmbare: xët 1 = njëkk, {0} = mujj",
        'pages_range_invalid': "Xët njëkk war a ne lëf lu xam ci xët mujj.",
        'pages_position_invalid': "Barab bu dem war a ne dul ci xët yi nga indi.",
        'pages_no_pdf_selected': "Amul PDF bu tànn.",
        'pages_deleted': "{0} xët far nañu.",
        'pages_extracted': "Gëwal: {0}\nDenci fii: {1}\nMag denc: {2:.1f} KB",
        'pages_inserted': "{0} xët duggal nañu",
        'pages_moved': "{0} xët indi nañu.",
        'pages_deleted_none': "Amul xët bu far.",
        'pages_delete_progress': "Xët yi day far...",
        'pages_deleted_with_backup': "{0} xët far nañu.\n\nSantar: {1}",
        'pages_deleted_voice': "Santar defar nañu, {0} xët far nañu.",
        'info': "Xibaar",
        'error_dialog_creation': "Këru wax manuñu ko defar",
        'extract_page_single': "Gëwal xët {0}",
        'extract_page_range': "Gëwal xët {0}-{1}",
        'extract_success_voice': "Xët yi gëwal nañu leen baax na",
        'extract_error_format': "Njuumte ci gëwal: {0}",
        'pages_inserted_voice': "{0} xët duggal nañu.",
        'insert_error_format': "Njuumte ci duggal: {0}",
        'pages_move_progress': "Xët yi day indi...",
        'pages_moved_with_backup': "{0} xët indi nañu.\n\nSantar: {1}",
        'move_success_title': "Indi doxe na",
        'pages_moved_voice': "{0} xët indi nañu baax na",
        'mark_removed': "Dal ci xët {0} far nañu ko",
        'mark_empty': "Xët {0} dal nañu ko ni dell",
        'mark_export_removed': "Dal gu yóbbu ci xët {0} far nañu ko",
        'mark_export': "Xët {0} dal nañu ko ngir yóbbu",
        'no_empty_pages': "Amul xët yu dell yu dal ngir far",
        'delete_empty_confirm': "Danga waxle a far ñépp {0} xët yu dell yu dal?",
        'delete_empty_confirm_voice': "Far leegi ñépp {0} xët yu dell yu dal? Waaw walla Déet.",
        'empty_pages_deleted': "{0} xët yu dell far nañu",
        'no_export_pages': "Amul xët bu dal ngir yóbbu",
        'overwrite_title': "Bind ci kanam denc bu am",
        'overwrite_question': "Denci\n\n{0}\n\nam na ci kanam.\nDanga waxle a bind ci kanam?",
        'overwrite_voice': "Bind ci kanam denc bu am? Waaw walla Déet.",
        'page_skipped': "Xët {0} bañañu ko jëfandikoo",
        'export_complete': "Yóbbu mujj na.",
        'export_complete_voice': "Yóbbu mujj na.",
        'no_pages_exported': "Amul xët bu yóbbu",
        'export_cancelled': "Yóbbu far nañu ko",
        'pages_exported': "{0} xët yóbbu nañu ci {1}",
        'export_page_title': "Yóbbu xët",
        'page_exported': "Xët {0} yóbbu nañu ci {1}",
        'export_error': "Njuumte ci yóbbu",
        'export_marked_title': "Yóbbu xët yu dal",
        'rotate_all_title': "Wër ñépp xët yi",
        'rotate_all_question': "Danga waxle a wër ñépp xët yi 90 degré ci ndeyji?",
        'rotate_all_voice': "Danga waxle a wër ñépp xët yi 90 degré ci ndeyji? Waaw walla Déet?",
        'all_pages_rotated': "Ñépp xët yi wër nañu",
        'page_rotated': "Xët {0} wër nañu ko",
        'rotate_error': "Xët bi manuñu ko wër",
        'delete_page_confirm': "Danga waxle a far xët {0}?",
        'delete_page_confirm_voice': "Danga sure ne danga waxle a far xët {0}? Waaw walla Déet.",
        'page_deleted': "Xët {0} far nañu ko",
        'delete_error': "Xët bi manuñu ko far",
        'pages_deleted_voice': "{0} xët far nañu",
        'pages_exported_split': "{0} xët yóbbu nañu baax na.",
        'pages_skipped': "{0} xët bañañu leen jëfandikoo.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Gëwal xët (ci gën a mag)",
        'pdf_splitter_title': "Wëlal ak gëwal PDF",
        'pdf_splitter_load': " Tànn denc PDF",
        'pdf_splitter_info': "Tànn benn ci yoon yi ci sa denc PDF",
        'pdf_splitter_basic': "Jëf yu njëkk",
        'pdf_splitter_single': "Wëlal ci xët bu nekk",
        'pdf_splitter_range': "Gëwal xët:",
        'pdf_splitter_range_placeholder': "ni 1-3,5,7-9",
        'pdf_splitter_clean': "Jëf yu set",
        'pdf_splitter_remove_empty': "Far ñépp xët yu dell",
        'pdf_splitter_remove': "Far xët yu ci digg:",
        'pdf_splitter_remove_placeholder': "ni 2,4-6",
        'pdf_splitter_process': "Yóbb PDF",
        'pdf_splitter_loaded': "PDF yeb nañu ko. Tànn benn ci yoon",
        'pdf_read_error': "PDF manuñu ko jàng",
        'pages': "Xët",
        'pages_created': "Xët yi defar nañu",
        'range_empty': "Jox xët yu ci digg",
        'range_invalid': "Xët yu ci digg baaxul",
        'range_created': "PDF bees ak xët yu tànn defar na:\n{0}",
        'empty_removed': "{0} xët yu dell far nañu.\nJéggi: {1}",
        'remove_empty': "Jox xët yu nga bëgg a far",
        'remove_invalid': "Xët yu far baaxul",
        'remove_done': "PDF gu set defar na:\n{0}",
        'open_folder': "Yeb folder bi",
        'show_in_finder': "Wone ci Finder",
        'pdf_splitter_no_pdf': "Yeb PDF bu njëkk.",
        'process_error': "Njuumte ci yóbb PDF",
        'pages_created_voice': "{0} xët defar nañu",
        'range_created_voice': "PDF ak xët yu tànn defar na",
        'empty_removed_voice': "{0} xët yu dell far nañu",
        'remove_done_voice': "PDF gu set defar na",
        'pdf_splitter_split_groups': "Kurel bu nekk di wëlal ci denc bu nekk",
        'range_created_single': "PDF bees defar na:\n{0}",
        'range_created_multiple': "{0} denc PDF defar nañu.",
        'range_created_voice_single': "PDF benn ak xët yu tànn defar na",
        'range_created_voice_multiple': "{0} denc PDF defar nañu",
        'empty_removed_none_left': "Amul xët bu toog",
        'empty_removed_all_empty': "Ñépp xët yi dell lañu, dinañu leen far. Amul denc bu defar.",
        'preview_single': "Wone ci kanam: {0}",
        'preview_enter_range': "Jox xët yu ci digg.",
        'preview_invalid_range': "Xët yu ci digg baaxul.",
        'preview_file': "Wone ci kanam: {0}",
        'preview_files': "Wone ci kanam: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Tàmbali móol",
        'print_sent': "Kërkaandoo móol yóbbu nañu ko",
        'print_now': "Móol leegi",
        'print_error': "Njuumte ci móol leegi",
        'print_limited': "Móol ci sa jikkeem dina am ay wàng",
        'print_error_format': "Njuumte ci móol leegi: {0}",
        'warning': "Xeexal",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Soppi ci nopp bu leet",
        'mode_switch_to_dark': "Soppi ci nopp bu ñuul",
        'mode_dark_activated': "Nopp bu ñuul tànn na",
        'mode_light_activated': "Nopp bu leet tànn na",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Wonu mbubb",
        'zoom_two_pages': "Xët ñaari ci wet",
        'zoom_overview': "Nopp gu xool lépp",
        'zoom_cannot_during_search': "Xar a nga xool bu baax, ba ci seet dinañu ko def",
        'zoom_exit_first': "Jéggi ci zoom bu njëkk",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Ñëbb ak wàcce tànn na",
        'drag_disabled': "Ñëbb ak wàcce tudd na",
        'drag_page_grab': "Xët {0} ëmb nañu ko",
        'drag_page_dropped': "Xët {0} duggal nañu ko ci barab {1}",
        'drag_position_invalid': "Barab baaxul",
        'drag_same_position': "Xët {0} toog na ci barab {0}",
        'drag_error': "Njuumte ci indi",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Duggal mbind ak jekkal yu gën a mag ak jëfandikoo mbind yu denci",
        'text_templates': "Mbind yu denci yu am:",
        'text_name': "Tur",
        'text_preview': "Wone mbind ci kanam",
        'text_enter': "Mbind:",
        'text_font_size': "Mag mbind:",
        'text_formatting': "Jekkal mbind:",
        'text_bold': "Tar",
        'text_italic': "Ñaar",
        'text_underline': "Sër ci suuf",
        'text_alignment': "Wommat:",
        'text_left': "Camm",
        'text_center': "Diggu",
        'text_right': "Ndiank",
        'text_color': "Melow mbind:",
        'text_opacity': "Nettali:",
        'text_word_wrap': "Far lay:",
        'text_auto': "Ci saa si",
        'text_page_width_95': "Mag xët (95%)",
        'text_page_width_85': "Mag lool (85%)",
        'text_page_width_75': "Mag (75%)",
        'text_page_width_60': "Mag (60%)",
        'text_page_width_50': "Digg (50%)",
        'text_page_width_30': "Ndaw (30%)",
        'text_page_width_20': "Ndaw (20%)",
        'text_page_width_10': "Ndaw lool (10%)",
        'text_no_wrap': "Amul far",
        'text_private': "Mbind bu suq (laaj baat biir lañu koy soxla)",
        'text_preview_label': "Wone ci kanam:",
        'text_preview_placeholder': "Mbind bi dinañu koo wone ci kanam fii...",
        'text_no_text': "(Amul mbind)",
        'text_save_template': "💾 Denci ni mbind",
        'text_delete_template': "🗑 Far mbind bi nga tànn",
        'text_show_private': "Wone yu suq yi",
        'text_hide_private': "Nëbb yu suq yi",
        'text_use': "✅ Jëfandikoo mbind bi",
        'text_saved': "Mbind bi denci nañu ko ni:\n{0}",
        'text_saved_voice': "Mbind bi denci nañu ko",
        'text_deleted': "Mbind bi far nañu ko",
        'text_no_text_to_save': "Amul mbind ngir denci.",
        'text_no_templates': "Amul mbind bu denci",
        'text_private_master_required': "Mbind yu suq man nga leen jëfandikoo su nga jekkal baat biir bu mag.\n\nDanga waxle a jekkal baat biir bu mag leegi?",
        'text_filename': "Tur denc ngir mbind (ak 'Text_' ak '.txt'):",
        'text_filename_hint': "Ni: 'Telefonu kër' dina denci ni 'Text_Telefonu kër.txt'",
        'text_save_hint': "Mbind bi dina denci ak jekkalem ci saa si.",
        'text_guide_title': "Duggal mbind - Ndigal",
        'text_delete_confirm': "Danga sure ne danga waxle a far mbind bi?\n\nDenc: {0}\nMbind: {1}...",
        'text_make_public': "Dal ni li ëpp",
        'text_make_private': "Dal ni li suq",
        'text_privacy_changed': "Suq soppi na",
        'text_private_always': "Suq wone na bu baax (jekkal)",
        'text_mode_required': "Tànn nopp bu mbind bu njëkk",
        'text_continue_editing': "Jéggi ci soppi - Mbind bi mujj na",
        'text_no_input': "Amul mbind bu duggal - mbind bi wàcce nañu ko",
        'save_dialog_question': "Naka nga bëgg a jéggi?",
        'text_save_question': "Denci ñépp mbind yi ak làtt bi, jekkal leen, jéggi ci soppi walla wàcce leen?",
        'copy_cross': "Làtt bi sanc nañu ko",
        'paste_cross': "Làtt bi wàcce nañu ko",
        'paste_text': "Mbind bi wàcce nañu ko",
        'cross_discarded': "Làtt bi wàcce nañu ko",
        'all_discarded': "Lépp wàcce nañu",
        'text_discarded': "Mbind bi wàcce nañu ko",
        'no_texts_to_save': "Amul mbind ngir denci",
        'no_valid_texts': "Amul mbind gu baax ngir denci",
        'text_word_singular': "Mbind",
        'text_word_plural': "Mbind",
        'cross_word_singular': "Làtt",
        'cross_word_plural': "Làtt",
        'texts_saved_title': "Mbind denci nañu",
        'texts_crosses_saved': "{0} {1} ak {2} {3} duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'texts_crosses_saved_voice': "{0} {1} ak {2} {3} denci nañu.",
        'texts_saved': "{0} {1} duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'texts_saved_voice': "{0} {1} denci nañu.",
        'crosses_saved': "{0} {1} duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'crosses_saved_voice': "{0} {1} denci nañu.",
        'elements_saved': "{0} lëf duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'elements_saved_voice': "{0} lëf denci nañu.",
        'text_window_load_error': "Këru mbind manuñu ko yeb",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Duggal mbind ak mbind yu denci – Ndigal gu yomb**

        **1. Duggal mbind ak soppi ko**
        - Diggante denc bi, toggal ci ndeyji, tànn "Duggal mbind".
        - Kër bu bees dina woo la ngir duggal mbind bi ak jekkal ko:
        • Mag mbind, tar, ñaar, sër ci suuf
        • Melow mbind (man nga tànn)
        • Nettali (ak slider)
        • Far lay (mag yu bari, ni mag xët, ndaw, amul far)
        - Su nga tànn, mbind bi dina fekke ci barab bi nga toggal. Man nga ko indi ak mboq walla ak ndeyji.
        - Toggle ñaari yoon ci mbind bi ngir soppi ko; ESC ngir génn.

        **2. Jëfandikoo mbind yu denci (modèles)**
        - Ci këru mbind, ci camm, danga gis liir bu am mbind yu denci yépp.
        - **Denci mbind:** Duggal mbind bi, jekkal ko, toggal ci "💾 Denci ni mbind". Jox ko tur (ak .txt).
        - **Yeb mbind:** Toggal ci tur bi ci liir. Mbind bi ak jekkalem dinañu am, man nga ko jekkal.
        - **Far:** Toggal ci ndeyji ci mbind bi ngir far ko walla soppi suqam.

        **3. Mbind yu suq (Baat biir bu mag)**
        - Su nga jekkal baat biir bu mag (ci Jekkal → Jëfandikoo baat biir), man nga dal mbind ni "suq".
        - Tànn "Mbind bu suq" ci këru mbind ba denci ko.
        - Mbind yu suq dinañu wone ci liir su nga duggal baat biir bu mag benn yoon ci kàddu gu nekk (seetal sa bopp ak lock walla ci njëkk a jëfandikoo leen).
        - Ni nga man a aar mbind yu suq ci seen bopp.

        **4. Duggal làtt**
        - Ci njabootu toggal, man nga itam duggal làtt bu nataal (ni ngir case à cocher).
        - Mag làtt, yàqq wàll ak melom man nga leen jekkal ci Jekkal → Jekkal làtt.
        - Toggal ci ndeyji ci làtt bu am ngir soppi ko.

        **5. Jëf yu bari**
        - Su nga duggal mbind yu bari walla làtt ci xët bu nekk, man nga leen denci walla wàcce lépp ak ñoom ci njabootu toggal (toggal ci ndeyji ci nopp bu mbind).
        - Su nga leen denci, lépp dinañu duggu ci PDF, dinañu toog ni nataal yu vekter.

        **6. Ndeyji yu yomb ci nopp bu mbind**
        - Ndeyji: indi lëf
        - Ctrl+ndeyji: indi ci yàqq yu mag
        - Enter: yeb këru denci (denci lépp / jekkal / wàcce)
        - ESC: wàcce lëf bi leegi
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Duggal mbind ak mbind yu denci – Ndigal gu yomb</strong></p>

        <p><strong>1. Duggal mbind ak soppi ko</strong></p>
        <ul>
        <li>Diggante denc bi, toggal ci ndeyji, tànn "Duggal mbind".</li>
        <li>Kër bu bees dina woo la ngir duggal mbind bi ak jekkal ko:<br/>
        • Mag mbind, tar, ñaar, sër ci suuf<br/>
        • Melow mbind (man nga tànn)<br/>
        • Nettali (ak slider)<br/>
        • Far lay (mag yu bari, ni mag xët, ndaw, amul far)</li>
        <li>Su nga tànn, mbind bi dina fekke ci barab bi nga toggal. Man nga ko indi ak mboq walla ak ndeyji.</li>
        <li>Toggle ñaari yoon ci mbind bi ngir soppi ko; ESC ngir génn.</li>
        </ul>

        <p><strong>2. Jëfandikoo mbind yu denci (modèles)</strong></p>
        <ul>
        <li>Ci këru mbind, ci camm, danga gis liir bu am mbind yu denci yépp.</li>
        <li><strong>Denci mbind:</strong> Duggal mbind bi, jekkal ko, toggal ci "💾 Denci ni mbind". Jox ko tur (ak .txt).</li>
        <li><strong>Yeb mbind:</strong> Toggal ci tur bi ci liir. Mbind bi ak jekkalem dinañu am, man nga ko jekkal.</li>
        <li><strong>Far:</strong> Toggal ci ndeyji ci mbind bi ngir far ko walla soppi suqam.</li>
        </ul>

        <p><strong>3. Mbind yu suq (Baat biir bu mag)</strong></p>
        <ul>
        <li>Su nga jekkal baat biir bu mag (ci Jekkal → Jëfandikoo baat biir), man nga dal mbind ni "suq".</li>
        <li>Tànn "Mbind bu suq" ci këru mbind ba denci ko.</li>
        <li>Mbind yu suq dinañu wone ci liir su nga duggal baat biir bu mag benn yoon ci kàddu gu nekk (seetal sa bopp ak lock walla ci njëkk a jëfandikoo leen).</li>
        <li>Ni nga man a aar mbind yu suq ci seen bopp.</li>
        </ul>

        <p><strong>4. Duggal làtt</strong></p>
        <ul>
        <li>Ci njabootu toggal, man nga itam duggal làtt bu nataal (ni ngir case à cocher).</li>
        <li>Mag làtt, yàqq wàll ak melom man nga leen jekkal ci Jekkal → Jekkal làtt.</li>
        <li>Toggal ci ndeyji ci làtt bu am ngir soppi ko.</li>
        </ul>

        <p><strong>5. Jëf yu bari</strong></p>
        <ul>
        <li>Su nga duggal mbind yu bari walla làtt ci xët bu nekk, man nga leen denci walla wàcce lépp ak ñoom ci njabootu toggal (toggal ci ndeyji ci nopp bu mbind).</li>
        <li>Su nga leen denci, lépp dinañu duggu ci PDF, dinañu toog ni nataal yu vekter.</li>
        </ul>

        <p><strong>6. Ndeyji yu yomb ci nopp bu mbind</strong></p>
        <ul>
        <li>Ndeyji: indi lëf</li>
        <li>Ctrl+ndeyji: indi ci yàqq yu mag</li>
        <li>Enter: yeb këru denci (denci lépp / jekkal / wàcce)</li>
        <li>ESC: wàcce lëf bi leegi</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Jekkal làtt",
        'cross_properties': "Melom làtt",
        'cross_size': "Mag (px):",
        'cross_line_width': "Yàqq wàll:",
        'cross_color': "Melow:",
        'cross_choose_color': "Tànn",
        'cross_fine_tuning': "Jekkal bu yomb ci denci (pixel)",
        'cross_offset_x': "Indi X:",
        'cross_offset_y': "Indi Y:",
        'cross_offset_x_tooltip': "Nùmbal yu ñaaw dina indi làtt ci camm ci denci, yu baax ci ndeyji",
        'cross_offset_y_tooltip': "Nùmbal yu ñaaw dina indi làtt ci kaw ci denci, yu baax ci suuf",
        'cross_preview': "Wone ci kanam",
        'cross_save': "Jëfandikoo jekkal",
        'cross_customized': "Làtt jekkal nañu ko",
        'cross_settings_applied': "Jekkal làtt denci nañu.\nMag: {0}px, Yàqq wàll: {1}px\n{2}",
        'cross_updated_count': "{0} làtt yu am jekkal nañu leen.",
        'cross_no_crosses': "Amul làtt bu am.",
        'cross_settings_applied_all': "Jekkal làtt ci ñépp {0} làtt jëfandikoo nañu",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Jekkal mbind bu bopp",
        'signature_1': "Mbind bu bopp 1",
        'signature_2': "Mbind bu bopp 2",
        'signature_select': "Tànn mbind bu bopp",
        'signature_add': "➕ Yokk mbind bu bopp bu bees...",
        'signature_size': "Mag ngir mbind bu bopp {0} (%):",
        'signature_common': "Jekkal yu ëpp",
        'signature_timestamp': "Yokk waxtu ci saa si",
        'signature_location': "Barab bu njëkk:",
        'signature_timestamp_size': "Mag mbind ngir waxtu:",
        'signature_no_files': "-- Amul mbind bu bopp --",
        'signature_insert': "Duggal mbind bu bopp",
        'signature_insert_1': "Duggal mbind bu bopp 1",
        'signature_insert_2': "Duggal mbind bu bopp 2",
        'signature_customize': " Jekkal mbind bu bopp bii",
        'signature_discard': " Wàcce mbind bu bopp bii",
        'signature_save_all': " Denci ñépp mbind yu bopp",
        'signature_discard_all': " Wàcce ñépp mbind yu bopp",
        'signature_guide_title': "Mbind bu bopp - Ndigal",
        'signature_guide': """
📝 Mbind bu bopp - Ndigal gu gàtt

- Jekkal baat biir bu mag
- Jekkal mbind bu bopp ci Jekkal
  (mag, waxtu ...)
- Duggal ak toggal ci ndeyji ci barab bu baax
  (baat biir bu mag lañu koy soxla benn yoon ci kàddu)
- Indi mbind bu bopp ak mboq walla ndeyji
- Man nga duggal mbind yu bopp yu bari
- Mbind bu bopp bu nekk man nga ko jekkal
- Wàcce mbind bu bopp bu nekk
- Denci / wàcce lépp ci yoon ju nekk
- Walla jëfandikoo barre menu.
        """,
        'signature_placeholder': "Amul wone ci kanam",
        'signature_info': "Mbind bu bopp {0}: {1}×{2} px ({3}% ci {4}×{5})",
        'signature_info_placeholder': "Jekkal ngir mbind bu bopp {0}",
        'signature_inserted': "Mbind bu bopp {0} ci xët {1} duggal nañu ko",
        'signature_deleted': "Mbind bu bopp far nañu ko",
        'signature_copied': "Mbind bu bopp sanc nañu ko",
        'signature_pasted': "Mbind bu bopp {0} wàcce nañu ko",
        'signature_saved': "{0} mbind yu bopp duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'signature_saved_voice': "{0} mbind yu bopp denci nañu",
        'mode_replace_signature_format': "Jéggi nopp bi, duggal mbind bu bopp {0}",
        'mode_conflict_voice_signature': "Nopp bu {0} tànn na. Jéggi ko, duggal mbind bu bopp?",
        'signature_not_configured': "Mbind bu bopp {0} jekkalul",
        'signature_file_not_found': "Denc mbind bu bopp amuñu ko gis",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Amul mbind bu bopp bu sanc",
        'no_signatures_to_save': "Amul mbind bu bopp ngir denci",
        'signature_save_question': "Denci ñépp mbind yu bopp, jekkal leen walla wàcce bii?",
        'signatures_saved_title': "Mbind yu bopp denci nañu",
        'signatures_saved': "{0} mbind yu bopp duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'signatures_saved_voice': "{0} mbind yu bopp denci nañu.",
        'all_signatures_discarded': "Ñépp mbind yu bopp wàcce nañu",
        'signature_settings_saved': "Jekkal mbind bu bopp denci nañu",
        'signature_cancelled': "Mbind bu bopp wàcce nañu ko",
        'signature_active_title': "Mbind bu bopp tànn na",
        'signature_replace_question': "Mbind bu bopp bu nekk tànn na.\n\nDanga waxle a tolofaane mbind bi leegi?",
        'signature_replace': "Tolofaane mbind bu bopp",
        'signature_replace_voice': "Tolofaane mbind bu bopp leegi walla far?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Jekkal nataal",
        'image_common': "Jekkal nataal yu ëpp",
        'image_keep_aspect': "Aar melo su nga koy ñëbb",
        'image_default_size': "Mag bu njëkk (%):",
        'image_dark_invert': "Séddataliku nataal ci nopp bu ñuul",
        'image_dark_invert_tooltip': "Tànn: nataal yi dinañu séddataliku ngir gis leen baax",
        'image_fine_tuning': "Jekkal bu yomb (pixel)",
        'image_offset_x': "Indi X:",
        'image_offset_y': "Indi Y:",
        'image_offset_x_tooltip': "Nùmbal yu ñaaw dina indi nataal ci camm ci denci, yu baax ci ndeyji",
        'image_offset_y_tooltip': "Nùmbal yu ñaaw dina indi nataal ci kaw ci denci, yu baax ci suuf",
        'image_select': "Tànn nataal",
        'image_insert': "Duggal nataal",
        'image_customize': " Jekkal nataal bii",
        'image_aspect': " Aar melo",
        'image_discard': " Wàcce nataal bii",
        'image_save_all': " Denci ñépp nataal yi",
        'image_discard_all': " Wàcce ñépp nataal yi",
        'image_filter': "Nataal",
        'image_guide_title': "Duggal nataal - Ndigal",
        'image_guide': """
📷 Duggal nataal ci PDF - Ndigal gu gàtt:

1. Toggal ci ndeyji ci barab bu baax
2. "Duggal nataal" → Tànn nataal
3. Toogal nataal bi: ñëbb ko ak mboq
4. Jekkal magam: ñëbb ci ndombi/mbëlleef
5. Aar melo: toggal ci [A]
6. Jekkal ci naw: toggal ci ndeyji ci nataal

Kiiray: Ci njabootu toggal, man nga jekkal seen jekkal.
        """,
        'image_inserted': "Nataal {0} ci xët {1} duggal nañu ko",
        'image_deleted': "Nataal wàcce nañu ko",
        'image_copied': "Nataal sanc nañu ko",
        'image_pasted': "Nataal wàcce nañu ko",
        'image_saved': "{0} nataal duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'image_saved_voice': "{0} nataal denci nañu",
        'image_aspect_on': "tànn",
        'image_aspect_off': "tudd",
        'image_aspect_toggle': "Aar melo {0}",
        'image_reset': "Nataal indi nañu ko ci magam bu njëkk",
        'image_replaced': "Nataal tolofaane nañu ko",
        'image_invalid': "Nataal bu baaxul",
        'mode_replace_image': "Duggal nataal",
        'mode_conflict_voice_image': "Nopp bu {0} tànn na. Jéggi ko, duggal nataal?",
        'image_active_title': "Nataal tànn na",
        'image_replace_question': "Nataal bu nekk tànn na.\n\nDanga waxle a tolofaane nataal bi leegi?",
        'image_replace': "Tolofaane nataal",
        'image_replace_voice': "Tolofaane nataal bi leegi walla far?",
        'image_filter_all': "Nataal (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Ñépp denc yi (*.*)",
        'no_copied_image': "Amul nataal bu sanc",
        'image_discarded': "Nataal wàcce nañu ko",
        'image_save_question': "Denci ñépp nataal yi, jekkal leen walla wàcce bii?",
        'no_images_to_save': "Amul nataal ngir denci",
        'no_valid_images': "Amul nataal gu baax ngir denci",
        'images_saved_title': "Nataal denci nañu",
        'images_saved': "{0} nataal duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'images_saved_voice': "{0} nataal denci nañu.",
        'all_images_discarded': "Ñépp nataal yi wàcce nañu",
        'image_settings_updated': "Jekkal nataal yeesi nañu",
        'image_replace_title': "Tànn nataal bu bees",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Jekkal form",
        'form_basic': "Jekkal yu njëkk",
        'form_default_type': "Form bu njëkk:",
        'form_rectangle': "Mbaaxu ñaari",
        'form_ellipse': "Mbaaxu ndaaw",
        'form_line': "Làtt",
        'form_arrow': "Pippi",
        'form_line_width': "Yàqq wàll:",
        'form_colors': "Melow",
        'form_line_color': "Melow làtt:",
        'form_fill_color': "Melow ci biir:",
        'form_choose_color': "Tànn",
        'form_transparent': "Gannaaw gu nettali (làtt rekk)",
        'form_filled': "ci biir am",
        'form_dark_mode': "Nopp bu ñuul",
        'form_dark_invert': "Séddataliku melow yi ci nopp bu ñuul",
        'form_fine_tuning': "Jekkal bu yomb (pixel)",
        'form_offset_x': "Indi X:",
        'form_offset_y': "Indi Y:",
        'form_offset_x_tooltip': "Nùmbal yu ñaaw dina indi form ci camm ci denci, yu baax ci ndeyji",
        'form_offset_y_tooltip': "Nùmbal yu ñaaw dina indi form ci kaw ci denci, yu baax ci suuf",
        'form_preview': "Wone ci kanam",
        'form_insert': "Duggal form",
        'form_rectangle_insert': "Mbaaxu ñaari",
        'form_ellipse_insert': "Mbaaxu ndaaw / Mbaaxu",
        'form_line_insert': "Làtt (2 toggal)",
        'form_arrow_insert': "Pippi (2 toggal)",
        'form_customize': " Jekkal form bii",
        'form_transparent_toggle': " Gannaaw gu nettali",
        'form_discard': " Wàcce form bii",
        'form_save_all': " Denci ñépp form yi",
        'form_discard_all': " Wàcce ñépp form yi",
        'form_guide_title': "Duggal form - Ndigal",
        'form_guide': """
📐 Duggal form ci PDF - Ndigal gu gàtt:

1. Tànn form (Mbaaxu ñaari, Mbaaxu ndaaw, Làtt, Pippi)
2. Toggal ci barab
   - Mbaaxu ñaari/ndaaw: toggal benn rekk ngir toogal form
   - Làtt/pippi: toggal ñaar ngir njëkk ak mujj
3. Toogal form: ñëbb ko ak mboq
4. Jekkal magam: ñëbb ci ndombi/mbëlleef
5. Denci form: Enter
6. Wàcce form: ESC
7. Jekkal ci naw: toggal ci ndeyji ci form

Kiiray: Ci njabootu toggal, man nga jekkal seen jekkal.
        """,
        'form_inserted': "{0} ci xët {1} duggal nañu ko",
        'form_deleted': "Form far nañu ko",
        'form_copied': "Form sanc nañu ko",
        'form_pasted': "Form wàcce nañu ko",
        'form_saved': "{0} form duggal nañu ci PDF.\n\nPDF yeb nañu ko ci naw...",
        'form_saved_voice': "{0} form denci nañu",
        'form_reset': "Form indi nañu ko ci magam bu njëkk",
        'form_transparent_on': "tànn",
        'form_transparent_off': "tudd",
        'form_transparent_toggled': "Gannaaw gu nettali {0}",
        'form_line_cancel': "Làtt gànnal far nañu ko",
        'form_second_click': "Leegi toggal ci mujj ngir {0}",
        'mode_replace_form': "Duggal form",
        'mode_conflict_voice_form': "Nopp bu {0} tànn na. Jéggi ko, duggal form?",
        'form_settings_updated': "Jekkal form yeesi nañu",
        'form_unknown': "Form",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Toggal ci njëkk",
        'form_line_guide_2': "2. Toggal ci mujj",
        'form_line_guide_3': "Làtt bi dina gànal ci diggante ñaari barab yi.",
        'form_line_status_1': "Nga xaar toggal bu njëkk...",
        'form_line_status_2': "Njëkk tànn na: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Leegi toggal ci mujj...",
        'form_line_status_4': "Ñaari barab yi tànn nañu.\nToggal ci 'Mujj' ngir denci.",
        'form_line_reset': "Bind ci naw",
        'form_line_finish': "Mujj",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Sanc (Cmd+C)",
        'paste': "Wàcce (Cmd+V)",
        'copied': "Sanc nañu: {0}",
        'no_element_to_copy': "Amul lëf bu tànn ngir sanc",
        'no_copied_data': "Amul xibaar bu sanc",
        'no_valid_position': "Amul barab bu baax ngir wàcce",
        'copy_text': "Mbind sanc nañu ko",
        'copy_image': "Nataal sanc nañu ko",
        'copy_form': "Form sanc nañu ko",
        'copy_signature': "Mbind bu bopp sanc nañu ko",
        'element_text': "Mbind",
        'element_image': "Nataal",
        'element_form': "Form",
        'element_signature': "Mbind bu bopp",
        'element_unknown': "Lëf",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Xaaj nopp",
        'mode_conflict_message': "Nopp bu '{0}' tànn na.\n\nDanga waxle a jéggi ko ak {1}?",
        'mode_replace': "Jéggi nopp bi ak {0}",
        'mode_cancel': "Far",
        'mode_replace_text': "duggal mbind",
        'mode_replace_cross': "duggal làtt",
        'mode_replace_signature': "duggal mbind bu bopp",
        'mode_replace_image': "duggal nataal",
        'mode_replace_form': "duggal form",
        'mode_conflict_voice': "Nopp bu {0} tànn na. Jéggi ko, duggal mbind?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Duggal mbind",
        'active_mode_signature': "Mbind bu bopp",
        'active_mode_image': "Nataal",
        'active_mode_form': "Form",
        'active_mode_and': " ak ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Duggal",
        'insert_another_text': "Duggal mbind",
        'insert_another_cross': "Duggal làtt",
        'insert_another_signature_1': "Mbind bu bopp 1",
        'insert_another_signature_2': "Mbind bu bopp 2",
        'insert_another_image': "Duggal nataal",
        'insert_another_form_rect': "Mbaaxu ñaari",
        'insert_another_form_ellipse': "Mbaaxu ndaaw",
        'insert_another_form_line': "Làtt (2 toggal)",
        'insert_another_form_arrow': "Pippi (2 toggal)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Denci {0}",
        'save_dialog_message': "{0} dina denci ci xët {1}.\n\nNaka nga bëgg a jéggi?",
        'save_all': "Denci ñépp {0}",
        'save_single': "Denci {0}",
        'save_customize': "Jekkal {0}",
        'save_discard': "Wàcce bii {0}",
        'save_continue': "Jéggi ci soppi",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Dem ci xët {0}",
        'context_rotate': " Wër xët {0}",
        'context_delete': " Far xët {0}",
        'context_export': " Yóbbu xët {0}",
        'context_mark_as': " Dal xët ni...",
        'context_mark_empty': " Xët bu dell",
        'context_unmark_empty': " Dellul fi",
        'context_mark_export': " Dal ngir yóbbu",
        'context_unmark_export': " Far dal gu yóbbu",
        'context_batch_actions': " Jëf yu bari",
        'context_batch_delete_empty': " Far ñépp {0} xët yu dell",
        'context_batch_export_single': " Yóbbu ñépp {0} xët (denc bu nekk)",
        'context_batch_export_split': " Yóbbu ñépp {0} xët (ci wàlli)",
        'context_drag_start': " Tàmbali ñëbb ak wàcce",
        'context_drag_stop': " Tuddal ñëbb ak wàcce",
        'context_insert': " Duggal",
        'context_insert_pages': " Duggal xët",
        'context_zoom': "Xool bu baax",
        'discard_mixed': "Wàcce ñépp {0} {1} ak {2} {3}",
        'save_mixed': "Denci {0} {1} ak {2} {3}",
        'discard_texts': "Wàcce ñépp {0} mbind",
        'discard_text_single': "Wàcce 1 mbind",
        'save_texts': "Denci {0} mbind",
        'save_text_single': "Denci 1 mbind",
        'discard_crosses': "Wàcce ñépp {0} làtt",
        'discard_cross_single': "Wàcce 1 làtt",
        'save_crosses': "Denci {0} làtt",
        'save_cross_single': "Denci 1 làtt",
        'discard_signatures': "Wàcce ñépp {0} mbind yu bopp",
        'save_signature_single': "Denci 1 mbind bu bopp",
        'save_signatures': "Denci {0} mbind yu bopp",
        'discard_images': "Wàcce ñépp {0} nataal",
        'save_image_single': "Denci 1 nataal",
        'save_images': "Denci {0} nataal",
        'discard_forms': "Wàcce ñépp {0} form",
        'save_form_single': "Denci 1 form",
        'save_forms': "Denci {0} form",
        'cross_discard': "Wàcce làtt bii",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Xibaar ci yóbbu / duggal",
        'export_what': "📋 Lan lañu yóbbu?",
        'export_general': "Jekkal yu ëpp",
        'export_general_items': "• Génne baat (tànn/tudd, gaaw)\n• Nopp bu ñuul/leet\n• Jekkal santar\n• Jekkal OCR",
        'export_image_form': "Jekkal nataal ak form",
        'export_image_form_items': "• Jekkal nataal (melo, mag bu njëkk)\n• Jekkal form (yàqq wàll, melow)\n• Jekkal mbind bu bopp (yoon, mag, waxtu)",
        'export_passwords': "Denci baat biir",
        'export_passwords_items': "• Ñépp baat biir PDF yu denci\n• Mën nga tànn lëdal walla amul lëdal",
        'export_master': "Jekkal baat biir bu mag",
        'export_master_items': "• Hash baat biir bu mag\n• Jekkal ngir mbind bu bopp/mbind",
        'export_signatures': "Mbind yu bopp ak mbind",
        'export_signatures_items': "• Ñépp denc nataal (mbind yu bopp)\n• Ñépp mbind ak jekkaleem\n• Dal yu suq/yu ëpp",
        'export_import_warning': "⚠️ Ëmbare yu am solo",
        'export_import_note': "• Ci duggal, ñépp jekkal yi leegi dinañu bind ci kanam\n• War nga tàmbali program bi ci naw\n• Mbind yu bopp/mbind yu am dinañu tolofaane",
        'export_master_note': "• Su am baat biir bu mag, man nga tànn:\n  - Amul lëdal (baat biir ci seen bopp)\n  - Lëdal (ak baat biir bu mag rekk man nga jàng leen)",
        'export_security': "• Denc ZIP bu yóbbu am na xibaar yu suq\n• Aar ko baax (ni USB gu lëdal)\n• Su denc bi àgg, baat biir yi manuñu leen gis ci naw",
        'export_format': "📁 Melo yu yóbbu",
        'export_format_desc': "Jekkal yi dinañu denci ci benn denc ZIP:",
        'export_filename': "PDFDarkView_Jekkal_YYYYMMDD_HHMMSS.zip",
        'export_success': "Jekkal yóbbu nañu ko baax na",
        'export_failed': "Yóbbu doxe wut",
        'export_import_question': "Danga waxle a tàmbali program bi ci naw leegi?",
        'export_password_question': "Baat biir bu mag tànn na.\n\nDanga waxle a yóbbu baat biir yi ak amul lëdal?\n(walla dinañu yóbbu leen ak lëdal)",
        'export_decrypt': "Yóbbu ak amul lëdal",
        'export_encrypt': "Yóbbu ak lëdal",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Xibaar",
        'info_title': "Ci PDF Dark View",
        'info_version': "Versiõ",
        'info_author': "Soxlawu Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Ci",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> mooy nattuukaay PDF bu yomb, soxlawu waa-ndaw yu gisul.</p>

            <p><strong>Mbetteel yu koore:</strong></p>
            <ul>
                <li>Kontaraas bu gën, li mu tàjjoo manees na ko wër</li>
                <li>Fajukaay bu tollu ci keyboard</li>
                <li>Kanamukaay buñ bind</li>
                <li>OCR ngir xibaar yiñ seet</li>
                <li>Làppinayu xel yu bari</li>
            </ul>

            <p>Ba taxawal 50 làkk – ngir PDF yi yomb nu bari.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Mbetteel",
        'info_features_intro': "PDF Dark View di ko def:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Wonee ak tënk</strong> – Lënd/Leeral, xool xët, zoom, tambali ci xët</li>
            <li><strong>OCR (Tëggal mbind)</strong> – Xibaar yiñ seet xam nga leen jële</li>
            <li><strong>Soppi</strong> – Dox mbind, x, tar, lim, melosuuf</li>
            <li><strong>Xët yi jariñ</strong> – Far, jóge, wuti, wërsé ak fekk dikk</li>
            <li><strong>Wutt</strong> – Ci Word, Pages mbaa mbind</li>
            <li><strong>Sigg</strong> – Karaas-paas</li>
            <li><strong>Yombu wonee</strong> – Kanam, fajukaay keyboard, kontaraas bu gën</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Jariñ",
        'info_accessibility': "♿ Yombu wonee – fajukaay keyboard bu tollu",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Aju</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Ubbi PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Ceet</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Wutal Lënd/Leeral</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Mbind</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Dikk</div>

        <div class="shortcut-cat">📖 Tënk</div>
        <div class="shortcut-row"><kbd>Tastu tënk</kbd> Xool xët ci xët</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Tambali ci xët</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Xët bu njëk</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Xët bu gën</div>

        <div class="shortcut-cat">✏️ Soppi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Wuti mbind</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Far xët yi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Jóge xët yi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Wuti xët yi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Wërsé xët yi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Wërsé xët</div>

        <div class="shortcut-cat">🖼️ Wërsé ay mbetteel</div>
        <div class="shortcut-row"><kbd>Tastu tënk</kbd> Wërsé mbind/lim/tar</div>
        <div class="shortcut-row"><kbd>Ctrl+Tastu tënk</kbd> Wërsé bu mag</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Jàpp</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Bokk</div>

        <div class="shortcut-cat">🗣️ Kanamukaay</div>
        <div class="shortcut-row"><kbd>F2</kbd> Tollal kanamukaay</div>
        """,
        'info_contextmenu': "📌 Lu koore: Mbetteel yi nekk nañu ci menu bu baat (tastu natt gi wàllu njëk)!",
        'info_accessibility_hint': "💡 Xelal: Kanamukaay (F2) dafay wone yoon ba yomb, dafay yon ci menu yi ak boole yi.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licence & Xibaar",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 XIBAAR</strong><br>
        Xibaar § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Almaañ<br>
        Meel: binhdiez64@gmail.com<br>
        Dafa ko yore: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Kàddu</strong><br>
        Soflawe bi ñu soxlawu ci xel bu bari. Dara kàddu amul ci lu baax, lu war ci li. Jariñ bi nga def fenn.<br><br>

        <strong>📄 Licence MIT (jariñ bu nit)</strong><br>
        Droit d'auteur (c) 2026 Toralf Schulz (BinhDiez)<br>
        Muy am: jariñ bu fees, soppi bu nit, càppi bu nit.<br>
        Dara: jaay, jariñ bu jàkkarlan, far droit d'auteur.<br><br>

        <strong>🔧 Ay wàll yu ñu jox</strong><br>
        Soflawe bi am na ay wàll ci GPL, AGPL, Apache 2.0, BSD ak MIT.<br>
        Su ñu ko wutal, war nga liggéey ci mbetteel yi.<br><br>

        <strong>🌐 Open Source</strong><br>
        Kodu bi am na, man nga ko gis, soppi, wutal ci mbetteel yi.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Jërëjëf",
        'info_credits': "Jërëjëf ci wàllu Open Source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Jariñ PDF</li>
            <li><strong>PyQt5</strong> – Melosuuf</li>
            <li><strong>Tesseract OCR</strong> – Tëggal mbind</li>
            <li><strong>OCRmyPDF</strong> – Lu wéy OCR</li>
            <li><strong>python-docx</strong> – Wutt ci Word</li>
            <li><strong>qtawesome</strong> – Ay taq</li>
            <li><strong>DeepSeek</strong> – Yon ci wut (50+ làkk)</li>
            <li><strong>Kuy jariñ</strong> – Ci yonte yu baax</li>
            <li><strong>Wàllu Open Source</strong> – Ci biir yu baax</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Yeneen làkk",
        'info_languages_header': "🌍 Jàmm ci làkk",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View ci tundu jégg na <strong>62 làkk</strong> – ngir njëkkikaay bi xamné luy jëfandikoo ci àdduna bi.</p>

            <p><strong>📖 Limu làkk yi yépp (Ci weeru Mars 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanés (Shqip)</li>
                    <li>🇩🇿 Araab (العربية)</li>
                    <li>🇮🇩 Balines (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Birman (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnien (Bosanski)</li>
                    <li>🇧🇬 Bulgaar (Български)</li>
                    <li>🇨🇳 Sin (中文)</li>
                    <li>🇩🇰 Danois (Dansk)</li>
                    <li>🇩🇪 Alman (Deutsch)</li>
                    <li>🇬🇧 Àngale (English)</li>
                    <li>🇪🇪 Estonien (Eesti)</li>
                    <li>🇫🇮 Finnois (Suomi)</li>
                    <li>🇫🇷 Faraasé (Français)</li>
                    <li>🇬🇷 Grik (Ελληνικά)</li>
                    <li>🇮🇱 Ebra (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Krooat (Hrvatski)</li>
                    <li>🇭🇺 Ongrois (Magyar)</li>
                    <li>🇮🇩 Endonesien (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlànd (Gaeilge)</li>
                    <li>🇮🇸 Islànd (Íslenska)</li>
                    <li>🇮🇹 Italien (Italiano)</li>
                    <li>🇯🇵 Japon (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreen (한국어)</li>
                    <li>🇱🇦 Laaw (ພາສາລາວ)</li>
                    <li>🇱🇻 Leton (Latviešu)</li>
                    <li>🇱🇹 Lituanien (Lietuvių)</li>
                    <li>🇱🇺 Luksembuur (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malai (Bahasa Melayu)</li>
                    <li>🇮🇳 Marati (मराठी)</li>
                    <li>🇲🇳 Mongol (Монгол)</li>
                    <li>🇳🇵 Nepaal (नेपाली)</li>
                    <li>🇳🇱 Neylànd (Nederlands)</li>
                    <li>🇳🇴 Norwéj (Norsk)</li>
                    <li>🇦🇫 Pachto (پښتو)</li>
                    <li>🇮🇷 Pers (فارسی)</li>
                    <li>🇵🇱 Polon (Polski)</li>
                    <li>🇵🇹 Purtugal (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumaan (Română)</li>
                    <li>🇷🇺 Rus (Русский)</li>
                    <li>🇸🇪 Swed (Svenska)</li>
                    <li>🇷🇸 Serb (Српски)</li>
                    <li>🇸🇰 Slovak (Slovenčina)</li>
                    <li>🇸🇮 Sloven (Slovenščina)</li>
                    <li>🇪🇸 Español (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamoul (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Tay (ไทย)</li>
                    <li>🇨🇿 Tchèque (Čeština)</li>
                    <li>🇹🇷 Turku (Türkçe)</li>
                    <li>🇺🇦 Ukren (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnam (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yidish (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Rëy yeneen làkk:</strong><br>
                Bég naa làkk buñ ko waxee ba noppi? Muy rëy sa wàllu kàddu (<code>sprache_xx.py</code>) ci njëkkaay bi – njëkkikaay bi xam na koo. Su bégge naa wax wu ni mel, waxtaan ma.
            </div>

            <p><strong>🙏 Jërëjef ga wu tënk:</strong> DeepSeek ci jàmm ci wàllu wixal wàllu kàddu yi ci làkk 62.</p>

            <p>📧 Jant bi ngir wixal: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Njuumte",
        'error_occurred': "Am na njuumte",
        'error_pdf_load': "Njuumte ci yeb PDF",
        'error_pdf_save': "Njuumte ci denci PDF",
        'error_ocr': "Njuumte ci gënotal mbind",
        'error_no_pdf': "Amul PDF bu yeb",
        'error_page_not_found': "Xët bi amuñu ko gis",
        'error_invalid_range': "Xët yu ci digg baaxul",
        'error_file_not_found': "Denc bi amuñu ko gis",
        'error_permission': "Amul sañ-sañ",
        'error_unknown': "Njuumte bu xamul",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Doxe na",
        'success_operation': "Jëf bi doxe na baax na",
        'success_saved': "Denci nañu ko baax na",
        'success_exported': "Yóbbu nañu ko baax na",
        'success_imported': "Duggal nañu ko baax na",
        'success_deleted': "Far nañu ko baax na",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Tànn",
        'confirm_yes': "Waaw",
        'confirm_no': "Déet",
        'confirm_ok': "Baax na",
        'confirm_cancel': "Far",
        'confirm_delete': "Far",
        'confirm_overwrite': "Bind ci kanam",
        'confirm_continue': "Jéggi",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF day yeb...",
        'progress_saving': "PDF day denci...",
        'progress_exporting': "PDF day yóbbu...",
        'progress_processing': "Day yóbb...",
        'progress_wait': "Nga xaar...",
        'progress_preparing': "Day jekk...",
        'progress_finalizing': "Day mujjal...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Weex",
        'color_black': "Ñuul",
        'color_red': "Xonq",
        'color_green': "Wert",
        'color_blue': "Baxa",
        'color_yellow': "Mboq",
        'color_magenta': "Xonk baxa",
        'color_cyan': "Baxa weex",
        'color_orange': "Soxna siis",
        'color_gray': "Ganaaw",
        'color_custom': "Tànn melow",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Denc",
        'menu_edit': "&Soppi",
        'menu_view': "&Wonu",
        'menu_tools': "&Jëfandikukaay",
        'menu_settings': "&Jekkal",
        'menu_help': "&Ndimbal",
        'menu_language': "🌐 Làkku",
        'menu_guides': "&Ndigal",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Yeb",
        'file_save_as': "&Denci ni...",
        'file_protect': "&Aar denc bi...",
        'file_export': "&Yóbbu",
        'file_export_pages': "Yóbbu ci Pages",
        'file_export_word': "Yóbbu ci DOCX",
        'file_export_text': "Yóbbu ci TXT",
        'file_print_now': "&Móol leegi",
        'file_print': "&Móol",
        'file_close': "&Tëj",
        'file_quit': "&Génn",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Seet",
        'edit_ocr': " Defar OCR",
        'edit_rotate': "&Wër xët",
        'edit_rotate_all': "&Wër ñépp xët yi",
        'edit_delete_pages': "&Far xët",
        'edit_extract_pages': "&Gëwal xët",
        'edit_insert_pages': "&Duggal xët",
        'edit_move_pages': "&Indi xët",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Duggal mbind ak làtt",
        'text_insert': " Duggal mbind",
        'cross_insert': " Duggal làtt",
        'text_customize': " Jekkal mbind bii",
        'cross_customize': " Jekkal làtt bii",
        'cross_customize_all': " Jekkal ñépp làtt yi",
        'text_discard': " Wàcce mbind/làtt bii",
        'text_discard_all': " Wàcce ñépp mbind ak làtt yi",
        'text_save_all': " Denci ñépp mbind ak làtt yi",
        'text_guide': " Duggal mbind / mbind - Ndigal",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Duggal mbind bu bopp",
        'signature_settings_menu': " Jekkal...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Duggal nataal",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Duggal form",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Wone këru mbind",
        'view_zoom': "&Xool bu baax",
        'view_zoom_page': "&Mag xët (njëkk)",
        'view_zoom_two': "&Xët ñaari",
        'view_zoom_overview': "&Wonu lépp (xët yu bari)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Jëfandikukaay yu wér",
        'settings_voice': "Baati génne",
        'settings_voice_tooltip': "Dina yokk xibaar ci baati génne yu wâkkil mbind mi",
        'settings_signature': "&Jekkal mbind bu bopp",
        'settings_password': "&Jëfandikoo baat biir",
        'settings_backup': "Defar santar ba soppi",
        'settings_export_import': "&Yóbbu / duggal jekkal",
        'settings_export': "&Yóbbu ñépp jekkal yi...",
        'settings_import': "&Duggal ñépp jekkal yi...",
        'settings_export_info': "&Lan lañu yóbbu?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "tànn",
        'voice_off': "tudd",
        'voice_toggle': "Baati génne {0}",
        'voice_speed': "Gaaw gi {0} përsañ",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Jëfandikukaay bi amuñu ko gis:\n{0}\n\nBASE_DIR: {1}\nXoolal ndax jëfandikukaay PDF yi tànn nañu ci {1}.",
        'tool_started': "{0} tàmbali na",
        'tool_start_failed': "Manuñu ko tàmbali",
        'process_error_failed_to_start': "Jëf mi manuñu ko tàmbali. Denc bi am na?",
        'process_error_crashed': "Jëf bi mettu na ci tàmbali.",
        'process_error_timeout': "Jëf bi yagg na.",
        'process_error_write': "Njuumte ci bind ci jëf bi.",
        'process_error_read': "Njuumte ci jàng ci jëf bi.",
        'process_error_unknown': "Njuumte bu xamul ci jëf bi",
        'process_command': "Ndigal",
        'process_normal_exit': "mujj na baax na",
        'process_crashed': "mettu na",
        'process_nonzero_exit': "{0} mujj na ak code njuumte {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Day far...",
        'move_cancelling': "Indi day far",
        'opening_pdf': "PDF day yeb...",
        'loading_document': "Denc bi day yeb...",
        'pdf_opened': "PDF yeb nañu ko",
        'pages_found_moving': "{0} xët gis nañu, {1} ngir indi",
        'creating_backup': "Santar day defar...",
        'backup_description': "Denc bu njëkk day santar...",
        'backup_saved_as': "Santar nañu ko ni: {0}",
        'error_format': "Njuumte: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView ci BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Seet bind nañu ko ci naw",
        'page_header_simple': "=== Xët {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Jëfandikoo baat biir – Ndigal",
        'password_guide_voice': "Ndigal ngir jëfandikoo baat biir. Jàngal ëmbare yi.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Jëfandikoo baat biir – Ndigal gu yomb</strong></p>

        <p><strong>1. Aar PDF ak baat biir</strong></p>
        <ul>
        <li>Su nga yeb PDF bu aar ak baat biir, këru wax dina woo la ngir duggal baat biir bi.</li>
        <li>Mën nga denci baat biir bi ak lëdal, ba dul ko duggal seen yoon (case "Denci baat biir").</li>
        <li>Ak buton "Far baat biir", mën nga defar benn sanc PDF bu dëcc xam, far baat biir bi ci denci.</li>
        </ul>

        <p><strong>2. Baat biir bu mag</strong></p>
        <ul>
        <li>Baat biir bu mag dina aar seen duggal ci ñépp baat biir PDF yu denci.</li>
        <li><strong>Jekkal:</strong> Dem ci "Jekkal → Jëfandikoo baat biir → Jekkal baat biir bu mag", toggal ci "Jekkal baat biir bu mag". Tànn baat biir bu doon (8 mbind lu ci ëpp).</li>
        <li><strong>Soppi:</strong> Su nga seetal sa bopp baax na, mën nga soppi baat biir bu mag.</li>
        <li><strong>Far:</strong> Su nga far baat biir bu mag, ñépp baat biir yu denci dinañu far. Mën nga yóbbu santar ba kanam.</li>
        <li>Benn yoon ci kàddu gu nekk, war nga seetal sa bopp ak baat biir bu mag ngir duggal ci jëf yu aar (ni wone baat biir).</li>
        </ul>

        <p><strong>3. Jëfandikoo baat biir (liir)</strong></p>
        <ul>
        <li>Ci "Jekkal → Jëfandikoo baat biir", danga gis taabal bu am ñépp PDF yu denci ak seen baat biir yu lëdal.</li>
        <li><strong>Su amul baat biir bu mag:</strong> Mën nga far rekk – baat biir yi nëbb nañu.</li>
        <li><strong>Su am baat biir bu mag (seetal na sa bopp):</strong> Mën nga gis, sanc, yóbbu, far baat biir yi.</li>
        <li><strong>Yóbbu:</strong> Tànn melo (JSON, CSV, TXT), denci liir bi. Su am baat biir bu mag, mën nga tànn ndax baat biir yi dinañu yóbbu seen bopp walla ak lëdal.</li>
        <li><strong>Duggal:</strong> Denc ZIP bu yóbbu (ak ñépp jekkal, baat biir ci biir) mën nga ko duggal ci "Jekkal → Yóbbu / duggal jekkal". Ëmbare: Xibaar yi leegi dinañu bind ci kanam!</li>
        </ul>

        <p><strong>4. Bawool baat biir</strong></p>
        <ul>
        <li>Ci këru baat biir (ni ci aar PDF), danga gis buton wi mel ni xance 🎲 ci ndeyji fajwa duggal.</li>
        <li>Toggal ci, bawool baat biir bi dina woo la. Mën nga jekkal gudd, mbind (mag, ndaw, xayma, safaanu tukki), ak cosaan ngir jàng ko baax.</li>
        <li>Baat biir bu bawool mën nga koo jëfandikoo leegi, sanc ko su la soxla.</li>
        </ul>

        <p><strong>5. Ëmbare yu am solo ci aaru</strong></p>
        <ul>
        <li>Baat biir yu denci ñoo leen denci ak AES-256 lëdal. Caabi bi dina gëm ci sa baat biir bu mag (su am) walla ci ay nùmbal (su amul).</li>
        <li>Su amul baat biir bu mag, baat biir yi lëdal nañu leen waaye caabi bi nekk na ci program bi – nit ku mën a duggal ci sa denc yi mën a dëcc leen. Loolu taxañu laaj a jëfandikoo baat biir bu mag.</li>
        <li>Denci baat biir bi nekk na ci yoon wi `Daten/passwords.json`. Defar santar lool, lu ci ëpp ba far baat biir bu mag.</li>
        <li>Su nga fàddi baat biir bu mag, ñépp baat biir yu denci dinañu àgg.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Wutal",
        'invert_mode_classic': "Cosaan (wutal melo yi)",
        'invert_mode_smart': "Xel (wutal leeral)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Wert bi ci xër",
        'gray_threshold_10': "10% (tollu)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Jagleem)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (yomb)",
        'threshold_changed': "Wert bi tollu ci {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Wert bi ci xër – Xibaar",
        'threshold_guide_text': "Wert bi ci xër mooy wax ay pixel yu tollu ci lënd bu xel ngir 'xër' ak wutal.\n\n"
                                "• Wert bu ndaw (10%) wutal ay xër bu baax – melo yi dafa wéy.\n"
                                "• Wert bu gën (50%) wutal pixel yu melo – bi dafa def kontaraas bu gën, waaye man na def melo bi doy.\n\n"
                                "Wert bi fi am na ci xibaar. Ci xibaar bu mbind, 30–40% dafa baax, ci melosuuf bu melo 10–20%.\n\n"
                                "Man nga ko soppi ci 'Settings' – PDF dañu ko wutal.\n\n"
                                "Xibaar:\n* Lim ak melosuuf man nañu wonee ci leeral!\n* Wutal yi nekk nañu ci lënd.",
        'threshold_guide_voice': "Wert bi ci xër mooy wax lënd bu xel ci doy. Wert bu ndaw dafay wéy melo, bu gën dafay def kontaraas.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Ubb PDF...",
        'progress_loading_document': "Wuti xibaar...",
        'progress_pdf_opened': "PDF ubbi",
        'progress_creating_backup': "Def backup...",
        'progress_backup_description': "Wéy xibaar...",
        'progress_backup_created': "Backup def",
        'progress_backup_saved_as': "Jàpp: {0}",
        'progress_analyzing_start': "Xëcc...",
        'progress_searching_empty': "Ceet xët yu bari...",
        'progress_page_empty': "Xët {0} bari",
        'progress_page_keep': "Wéy xët {0}",
        'progress_analysis_complete': "Xëcc dem",
        'progress_empty_found': "{0} xët yu bari gis",
        'progress_current_page': "Xët bi",
        'progress_mark_delete': "Wuti far",
        'progress_range_selected': "Xët yi {0}-{1}",
        'progress_deleting_pages': "Far {0} xët",
        'progress_creating_new_pdf': "Def PDF bu bees...",
        'progress_transferring_pages': "Wuti xët",
        'progress_keeping_page': "Xët {0} dafa wéy ({1}/{2})",
        'progress_saving_pdf': "Jàpp PDF...",
        'progress_optimizing': "Def mag...",
        'progress_finalizing': "Dem...",
        'progress_new_size': "Mag bees: {0:.2f} MB",
        'progress_cancelling': "Bokk...",
        'progress_cancel_message': "{0} bokk",
        'progress_pages_found_moving': "{0} xët gis, {1} wërsé",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Xëcc PDF...",
        'ocr_status_optimizing': "Def melosuuf...",
        'ocr_status_recognizing': "Tëggal mbind...",
        'ocr_status_embedding': "Wuti mbind...",
        'ocr_status_finalizing': "Dem PDF...",

        # PDF-Laden
        'progress_preparing': "Wuti...",
        'progress_loading': "Wuti PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Far xët...",
        'progress_moving_title': "Wërsé xët...",
        'pages_found': "Xët gis",
        'progress_creating_new_order': "Def wërsé bu bees...",
        'progress_sorting_pages': "Wuti xët...",
        'progress_moving_to_begin': "Wërsé {0} xët ci njëk",
        'progress_transferring_count': "Wuti {0} xët",
        'progress_transferring_before_target': "Wuti xët ci njëk",
        'progress_moving_pages': "Wërsé {0} xët",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_wéy_",
        'filename_copy_suffix': "_Càppi",
        'filename_page_single': "_Xët_",
        'filename_page_range': "_Xët_",
        'filename_export_page': "_Xët_{0:03}",
        'filename_export_range': "_Xët_{0}-{1}",
        'filename_export_multiple': "_Xët_{0}",
        'filename_with_text': "_ak_mbind",
        'filename_with_signature': "_ak_tar",
        'filename_with_image': "_ak_lim",
        'filename_with_forms': "_ak_melosuuf",
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
        'view_toggle_navbar': "Wone tastu yi",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Xaaj yi yépp lépp du ñu leen far",
		'pages_cannot_delete_last_page': 'Xaaj bu mujj gi du far!',
		'pages_cannot_delete_all_pages': 'Suuf ci benn xaaj moo war a dikk ci dokument bi!',
		'delete_pages_confirm': 'Danga bëgg a far {0} xaaj?',
		'delete_pages_confirm_voice': 'Danga bëgg a far {0} xaaj?',
		'pages_deleted': '{0} xaaj yi far nañu.',
		'warning': 'Kele',
		'error': 'Njuumte',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Darañu tontu",
        'form_customized': "Foom bi ñu ko solusiku",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Tànnal",
        'btn_use': "Jëfandikoo",
        'master_password_for_spasswords': "Ngir ay password-ca jàpp a jëfandikoo, ba noppi nag, sañ-sañ bu mag ay diggante.\n\nYaa ngi bëgg a diggante sañ-sañ bu mag ba leegi?",
        'open_saved_dialog_title': "Ubbi teyubal bi",
        'open_saved_question': "Yaa ngi bëgg a ubbi teyubal bi leegi?",
        'password': "Sañ-sañ",
        'password_manager_master_required': "Jàppaleekat password yi am na solo lool ci lii di sañ-sañ bu mag.\n\nYaa ngi bëgg a diggante sañ-sañ bu mag ba leegi?",
        'password_master_required_for_select': "Ngir gis te tànnal ay password-ca, ba noppi nag, sañ-sañ bu mag la war a bind.\n\nYaa ngi bëgg a bind ba leegi?",
        'password_not_available': "Password bi tànnal amul na ba tax ñu ko def.",
        'password_options_title': "Tànkatu password",
        'password_save_choice_change': "Wutal password bu bees",
        'password_save_choice_keep': "Jëfandikoo password bi nekk",
        'password_save_choice_none': "Jàpp a jàppale",
        'password_save_hint': "Diggante sañ-sañ bu mag ba noppi nga jàpp a jàppale.",
        'password_save_master_required': "Jàpp password (mog a am benn sañ-sañ bu mag)",
        'password_save_question': "PDF bii da fa password. Yaa ngi bëgg a jëfandikoo password bi nekk, waxtaan wala jàpp a jàppale?",
        'password_select': "Tànnal password",
        'password_select_none': "Password teyul.\n\nBa noppi, tànnal password ci biir tééré bi.",
        'password_select_one': "Ba noppi, tànnal benn password la benn.\n\nYa tànnal password yu bari.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_wër",
        'filename_insert_suffix': "_ak_tàllal",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_xëtër_yu_far",
        'filename_pages_moved': "_xëtër_yu_démb",
        'filename_rotated_all_suffix': "_xëtër_yépp_ñu_nëbb",
        'filename_rotated_suffix': "_xëtër_gu_nëbb",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Sañ-sañ téyubal yi ci biir PDF",
        'filename_keep_suffixes': "Farlu ci wàll",
        'filename_keep_suffixes_false': "Dég",
        'filename_keep_suffixes_true': "Farlu",
        'filename_preview_label': "Xoolal téyubal bi:",
        'filename_preview_overwrite_hint': "Xoolal amul – dafa farlu.",
        'filename_separator': "Benn",
        'filename_separator_none': "Bennul",
        'filename_separator_space': "Benn (_)",
        'filename_separator_underscore': "Benn (_)",
        'filename_settings_saved': "Teyubal bi farlu na",
        'filename_settings_title': "Teyubal bi",
        'filename_timestamp_position': "Teyubal bi",
        'filename_timestamp_position_after': "Ci wàll",
        'filename_timestamp_position_before': "Ci wàll",
        'filename_timestamp_position_end': "Ci wàll",
        'filename_use_timestamp': "Jëfandikoo",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Bii:</b><ul><li>Far xëtër</li><li>Tàllal</li><li>OCR</li></ul></html>",
        'backup_section': "Wër",
        'behavior_info': "Bii",
        'behavior_new_file': "Wutal téyubal bu bees",
        'behavior_overwrite': "Farlu",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Xëtër yépp nungi nëbb.\n\nBu yees na.\nTeyubal bu bees: {0}",
        'all_pages_rotated_voice': "Xëtër yépp nungi nëbb, teyubal bu bees.",
        'empty_pages_deleted_new_file': "{0} xëtër yépp nungi far.\n\nBu yees na.\nTeyubal bu bees: {1}",
        'empty_pages_deleted_voice': "{0} xëtër yépp nungi far, teyubal bu bees.",
        'ocr_keep_original': "Farlu",
        'ocr_new_file_question': "PDF bu bees bu tàllal na: {0}\n\nBëgg a ubbi leegi?",
        'ocr_open_new': "Ubbi OCR bu bees",
        'ocr_original_kept': "Teyubal bi yees na. OCR bi jàpp na.",
        'page_deleted_new_file': "Xëtër {0} nungi far.\n\nBu yees na.\nTeyubal bu bees: {1}",
        'page_deleted_voice': "Xëtër {0} far, teyubal bu bees.",
        'page_rotated_new_file': "Xëtër {0} nungi nëbb.\n\nBu yees na.\nTeyubal bu bees: {1}",
        'page_rotated_voice': "Xëtër {0} nëbb, teyubal bu bees.",
        'pages_deleted_new_file': "Xëtër {0} nungi far.\n\nBu yees na.\nTeyubal bu bees: {1}",
        'pages_deleted_new_file_voice': "{0} xëtër far, teyubal bu bees.",
        'pages_inserted_new_file': "Xëtër {0} nungi tàllal.\n\nBu yees na.\nTeyubal bu bees: {1}",
        'pages_inserted_new_file_ask': "Xëtër {0} nungi tàllal.\n\nBu yees na.\nTeyubal bu bees: {1}\n\nBëgg a ubbi leegi?",
        'pages_inserted_voice_new': "{0} xëtër tàllal, teyubal bu bees.",
        'pages_moved_new_file': "Xëtër {0} nungi démbb.\n\nBu yees na.\nTeyubal bu bees: {1}",
        'pages_moved_new_file_voice': "{0} xëtër démbb, teyubal bu bees.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ba noppi doon ko won",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Wër</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Wër</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Bii</strong> (text, signature, image, shape, OCR, rotate, insert, delete/move pages) <strong>automatic</strong> before applying the change.</p>
                <p style="margin: 5px 0 5px 20px;">• Wër bi <code>Dokument_wër_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• If you have additionally activated the option <strong>„Overwrite original“</strong>, a backup is also created.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Wër</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>No backup is created</strong> – neither when overwriting nor during page operations.</p>
                <p style="margin: 5px 0 5px 20px;">• The original file can be irretrievably lost when overwriting.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Recommended only for experienced users!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> The backup setting is independent of the "Overwrite original" option. You can combine both.<br>
                You can permanently hide this message.
            </div>
        </div>
        """,
        'backup_info_title': "Wër",
        'backup_info_voice': "Wër",
        'show_backup_info': "Wër",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ba noppi doon ko won",
        'overwrite_enable_backup': "Wër",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Farlu</p>
            <p>If you enable this option, changes (text, signature, image, shape, OCR, rotate, insert) are <strong>saved directly in the original</strong> – <strong>no new file is created</strong>.</p>
            <p>• The filename remains unchanged.<br>
            • Timestamps and suffixes are ignored.<br>
            • <strong>Without backup, the original can be irretrievably lost.</strong></p>
            <p style="color: #FFD700;">Recommendation: Additionally enable the backup option to get automatic backups.</p>
        </div>
        """,
        'overwrite_info_title': "Farlu",
        'overwrite_info_voice': "Warning: Overwrite original – no new file. Backup recommended.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} pages were inserted.\n\nThe original file was overwritten.\nA backup was created.",
        'pages_inserted_overwrite_no_backup': "{0} pages were inserted.\n\nThe original file was overwritten.\nNo backup was created.",
        'texts_saved_overwrite_with_backup': "The changes were saved in the original.\n\nA backup was created.",
        'texts_saved_overwrite_no_backup': "The changes were saved in the original.\n\nNo backup was created.",
        'texts_crosses_saved_new_file': "{0} {1} and {2} {3} were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'texts_saved_new_file': "{0} {1} were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'crosses_saved_new_file': "{0} {1} were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'elements_saved_new_file': "{0} elements were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'signatures_saved_overwrite_with_backup': "The signature(s) were saved in the original.\n\nA backup was created.",
        'signatures_saved_overwrite_no_backup': "The signature(s) were saved in the original.\n\nNo backup was created.",
        'images_saved_overwrite_with_backup': "The image(s) were saved in the original.\n\nA backup was created.",
        'images_saved_overwrite_no_backup': "The image(s) were saved in the original.\n\nNo backup was created.",
        'forms_saved_overwrite_with_backup': "The shape(s) were saved in the original.\n\nA backup was created.",
        'forms_saved_overwrite_no_backup': "The shape(s) were saved in the original.\n\nNo backup was created.",
        'signatures_saved_new_file': "{0} signatures were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'images_saved_new_file': "{0} images were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'forms_saved_new_file': "{0} shapes were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Warning: This PDF contains rotated pages. Positioning may deviate.",
        'page_rotated_warning_title': "Rotated page detected",
        'page_rotated_warning_message': "The current page {0} is rotated by {1}°.\n\nInserting elements on rotated pages is not supported.\n\nDo you want to rotate the page to upright position now?",
        'page_rotated_warning_voice': "Warning: The page is rotated. Please rotate it first.",
        'paste_on_rotated_page_simple_warning': "Inserting on page {0} not possible!\n\nThis page is rotated by {1}°.\n\nPlease first rotate the page to 0° (Menu: Edit → Align page).\n\nWarning:\nThe previously copied element will be lost if you do not save before rotating the page.",
        'paste_on_rotated_page_voice': "Insertion cancelled. Page is rotated. Please align the page first.",
        'page_rotated_cancel': "Cancel",
        'page_rotated_rotate_until_upright': "Rotate page repeatedly (until upright)",
        'page_rotated_now_upright': "The page is now upright. You can now insert.",
        'page_rotated_still_not_upright': "The page could not be rotated to upright position. Please correct manually.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Help: Correct rotated pages",
        'help_rotated_pages_voice': "Help for correcting rotated pages is opening.",
        'btn_help': "Help",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Rotated page – Insertion does not work correctly</p>

            <p>If inserting texts, signatures or shapes on a rotated page does not work properly, you can correct the page with an external PDF editor.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solution with external tool (e.g., macOS Preview)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Export page</strong><br>
                &nbsp;&nbsp;Click in the menu on <strong>File → Export as Pages</strong> or use another method to save the desired page as a single PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Open page in external program</strong><br>
                &nbsp;&nbsp;Open the exported PDF in a PDF editor (e.g., <strong>macOS Preview</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rotate page</strong><br>
                &nbsp;&nbsp;Rotate the page so that it is upright (in Preview: <strong>Tools → Rotate</strong> or <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Save</strong><br>
                &nbsp;&nbsp;Save the corrected page (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Reinsert the page into the original document</strong><br>
                &nbsp;&nbsp;Return to PDFDarkView and insert the corrected page at the desired position:<br>
                &nbsp;&nbsp;<strong>Edit → Insert pages</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternative: Rotate page in the original</p>
                <p style="margin: 5px 0 5px 20px;">• Use the built-in rotate function (<strong>Edit → Rotate page</strong>) to correct the page step by step.<br>
                • After each rotation, you can check if insertion now works.<br>
                • This is often the faster solution – try it first!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> If you frequently encounter rotated pages, you can permanently hide the warning in the insert dialog.<br>
                Positioning may then deviate – only use this option if you know the consequences.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Align pages",
        'menu_rotate_normalize_tooltip': "Rotate page or reset to 0°",
        'normalize_current_page': "Bring current page to upright position (set to 0°)",
        'normalize_all_pages': "Bring all pages to upright position (set to 0°)",
        'page_normalized': "Page {0} was set to upright position.",
        'all_pages_normalized': "All pages were set to upright position.",
        'page_already_upright': "Page {0} is already upright.",
        'all_pages_already_upright': "All pages are already upright.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>The PDF does not contain any searchable text.</p><p>Do you want to perform OCR to export to {0}?</p>",
        'export_ocr_voice': "The PDF does not contain any text. OCR required for export to {0}.",
        'export_no_ocr_possible': "Export without OCR not possible. Please perform OCR via the menu.",
        'ocr_failed_export_not_possible': "OCR failed. Export cannot be performed.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF will open in Preview. Please start the printing process there.",
        'print_preview_manual': "PDF has been opened. Please execute the print command manually (e.g., Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Merge PDFs",
        'merge_pdfs': "Merge PDFs",
        'merge_progress_title': "Merging PDFs...",
        'merge_pdfs_list': "PDFs in order (Drag & drop to sort)",
        'merge_add_pdf': "Add PDF",
        'merge_remove': "Remove",
        'merge_move_up': "Move up",
        'merge_move_down': "Move down",
        'merge_pdfs_info': "💡 Tip: You can change the order by drag & drop",
        'merge_no_pdfs': "No PDFs selected. Click on 'Add PDF'.",
        'merge_info': "{0} PDFs selected (approx. {1} pages)",
        'merge_open_file': "Open file",
        'merge_merge': "Merge",
        'merge_error': "Error while merging",
        'merge_min_two_pdfs_error': "Please select at least two PDF files to merge.",
        'merge_select_pdfs': "Select PDFs to merge",
        'merge_error_file': "Error while processing",
        'merge_cancelled': "Merging was cancelled",
        'merge_preparing': "Preparing...",
        'merge_processing': "Processing PDF {0} of {1}",
        'merge_saving': "Saving merged PDF...",
        'merge_complete': "Done!",
        'merge_success_title': "Merge successful",
        'merge_success_voice': "{0} PDFs were successfully merged.",
        'merge_success_message': "{0} PDFs were successfully merged.\n\nThe new document now has {1} pages.\n\nNew file:\n{2}\n\nSave location:\n{3}\n{2}\n\nDo you want to open this PDF?",
        'replace_file_title': "Replace file?",
        'replace_file_message': "A PDF is already open. Do you want to replace it with the new file?",
        'btn_yes': "Yes",
        'btn_no': "No",
        'filename_merge_suffix': "merged",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Opening {0}...",
        'progress_merge_reading': "Reading {0}...",
        'progress_merge_adding': "Adding {0} pages...",
        'progress_merge_optimizing': "Optimizing PDF...",
        'progress_merge_writing': "Writing PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "closing the PDF",
        'action_close_window': "closing the window",
        'action_open_new_pdf': "opening a new PDF",
        'action_quit_app': "quitting the application",
        'changes_saved': "The changes have been saved.",
        'file_close_title': "Close PDF file",
        'save_before_action': "Should the changes be saved before {0}? Yes or No?",
        'save_before_action_voice': "Should the changes be saved before {0}? Yes or No?",
        'save_before_close_question': "Should the changes be saved before closing? Yes or No?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF bu nu koy gis ànd na sos:\n\n{0}\n\n<b>lay wutal bu ñaaree seeni soxla",
        "ocr_rotate_title": "Téereelu xëtu mbir yi bees ngiy wax (OCR)",
        "ocr_rotate_question": "PDF bi am na xëtu mbir yi ñu ko tàmbali.\nYaa nga bëgg a wërloo téereelu mbir yi yépp ci 0° ba bees ngiy wax (OCR)?\nBiiy jóge ab yoon a koy tess ba noppi ci gisgisaal wax.",
        "ocr_rotate_yes": "Waaw, wërloo",
        "ocr_rotate_no": "Déedét, tàmbali OCR ba noppi",
        "ocr_rotate_voice": "PDF bi am na xëtu mbir yi ñu ko tàmbali. Xëtu mbir yi yépp ñoo war a wërloo ba bees ngiy wax (OCR)?",
        "ocr_not_performed_message": "Waxu amul. Baal ma, def OCR (menu \"Sopale\" → \"Def OCR\" walla Ctrl+R keys).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Teesal yi ngir OCR",
        "ocr_language_btn": "Tànkum benn làkk ngir OCR",
        "ocr_language": "Làkk ci diggante (yokku)",
        "ocr_language_current": "Làkk biy jëfandikoo kii:",
        "ocr_param_info": "Xibaar ci biimbali",

        "ocr_force_ocr_label": "Wattali OCR",
        "ocr_deskew_label": "Tànn li màgnal",
        "ocr_clean_label": "Sell liggéey bi",
        "ocr_oversample_label": "Sàn-sàn (DPI)",
        "ocr_pagesegmode_label": "Tontu xëtu mbir",
        "ocr_oem_label": "Mood bu jumtukaay bi (OCR engine mode)",
        "ocr_optimize_label": "Noppalin PDF",
        "ocr_jobs_label": "Proses yi man a def li ñu koy laaj",
        "ocr_verbose_label": "Bari-bari ci jële bi",

        "ocr_force_ocr_tooltip": "Wattali OCR ci téereelu mbir yi yépp, ba tax wax di ko yépp",
        "ocr_deskew_tooltip": "Wërloo xëtu mbir yi màgnal te boole",
        "ocr_clean_tooltip": "Fay xam-xam ëtt",
        "ocr_oversample_tooltip": "Yokk xëtu mbir bi ba bees ngiy wax (OCR) kooku DPI",
        "ocr_pagesegmode_tooltip": "Mën na ko xëtu mbir bi",
        "ocr_oem_tooltip": "Tànkum jumtukaay bi(OCR) Tesseract",
        "ocr_optimize_tooltip": "Noppalin PDF bi",
        "ocr_jobs_tooltip": "Xibaar bi ëpp",
        "ocr_verbose_tooltip": "Xibaar bi ëpp",
        "ocr_settings_explain_btn": "Cosaan",

        "ocr_force_ocr_explain": "Tànkum <b>téereebu mbir bu bees ngiy wax</b> di ko jëfandikoo — <b>Wattali</b> ba tax li ko xëtu mbir bi man a def",
        "ocr_deskew_explain": "Tànkum xëtu mbir bi — <b>Fi..</b>",
        "ocr_clean_explain": "Fay xam-xam ëtt",
        "ocr_oversample_explain": "Yokk xëtu mbir bi ba bees ngiy wax (OCR) kooku DPI",
        "ocr_pagesegmode_explain": "Mën na ko xëtu mbir bi",
        "ocr_oem_explain": "Tànkum jumtukaay bi(OCR) Tesseract",
        "ocr_optimize_explain": "Noppalin PDF bi",
        "ocr_jobs_explain": "Xibaar bi ëpp",
        "ocr_verbose_explain": "Xibaar bi ëpp",
        "ocr_reset_title": "Teesal yi ñu ko wóor",
        "ocr_reset_message": "Teesal yi ñu ko wóor",
        "info_tooltip": "Xibaar bi ëpp ci xibaar bi",
        "ocr_reset_defaults": "Wóor teesal yi",

        "ocr_psm_0": "Biram (Legacy engine)",
        "ocr_psm_1": "Biram",
        "ocr_psm_3": "Biram (Default)",
        "ocr_psm_4": "Biram",
        "ocr_psm_5": "Biram",
        "ocr_psm_6": "Biram",
        "ocr_psm_7": "Biram",
        "ocr_psm_8": "Biram",
        "ocr_psm_11": "Biram",

        "ocr_oem_0": "Biram",
        "ocr_oem_1": "Biram",
        "ocr_oem_2": "Biram",
        "ocr_oem_3": "Biram",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Làkk yi ngir OCR...",
        "ocr_language_title": "Tànkum làkk yi ngir OCR",
        "ocr_language_instruction": "Tànkum làkk yi ngir gisgisaal wax (OCR).\nGën: làkk yu bari dañuy yokk jébbanu ak ndimbal!\ngis ay màkku yo bu baax su tànke làkk bu bañ.",
        "ocr_language_predefined": "Noppal yu ñu koy tànkum",
        "ocr_language_custom": "Bu bees...",
        "ocr_language_selected": "Làkk yi tànkum ngir OCR",
        "ocr_language_changed": "Làkk bi OCR tintal na {0}",
        "ocr_language_auto_detect": "Làkk yi am nañu gis.",
        "ocr_language_none_found": "Xibaar làkk Tesseract amul! Baal ma, tàllal paket làkk bi (ni 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Tànkum làkk bu bees",
        "ocr_language_available": "Làkk yi am (tàllal nañu):",
        "ocr_language_select_hint": "Tànkum làkk bu bañ walla yu bari:",
        "ocr_language_confirm": "Yokk",
        "ocr_language_reset": "Wóor teesal yi (deu+eng+vie)",
        "ocr_language_priorities": "Làkk yi ñu koy gise (tàllal nañu):",

        "select_all_languages": "Tànkum lépp",
        "clear_all_languages": "Far tànkum bi",
        "install_language_packs": "Tàllal paket làkk yi ba mél...",
        "install_hint": "💡 Xibaar: làkk yi yépp tàllalul ci nosukaay bi. Ci buton bi nga gis ndimbal.",
        "ocr_language_install_title": "Tàllal paket làkk yi Tesseract",

        "ocr_missing_languages": "Paket làkk yi OCR ba mél",
        "ocr_missing_languages_message": "Làkk yi tànkum yi tàllalul ci nosukaay bi:\n\n{0}\n\nBaal ma, tàllal paket làkk yi ba mél (xool ndimbal ci 'ndimbal bu tàllal').\n\nYaa nga bëgg a ubbi ndimbal bu tàllal?",
        "ocr_missing_languages_voice": "Paket làkk yi ba mél. Baal ma, tàllal làkk yi ba mél.",
        "ocr_install_help_now": "Ubbi ndimbal",
        "ocr_continue_anyway": "Ci wàll",
        "ocr_language_error_title": "Njamala làkk bi OCR",
        "ocr_language_error_message": "Njamala ci gisgisaal wax: {0}\n\nBaal ma, xool teesal yi làkk bi (Teesal → Làkk bi OCR).",
        "ocr_install_help_button": "Ndimbal bu tàllal",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tàllal paket yi ngir làkk Tesseract</p>

        <p>Ngir OCR man a liggéey ci làkk bu xam-xam, li ko xam-xam war naa tàllal ci nosukaay bi. Noppi mbir wi ngir nosukaay bi:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Ubbi <strong>Terminal</strong> (Finder → Program yi → Utilité yi → Terminal).</li>
        <li>Tàllal làkk yi yépp ci:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Li man naa faye waxtu.)</li>
        <li>Walla làkk bu bañ (ni vietnam):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Ci Homebrew bi, <code>*.traineddata</code> man naa soppi ci liggéey wi (fii bu ne.</li>
        <li>Buy tàllal: Ubbi bii boole te ubbi làkk bu ngiy wax – làkk bu bees ngiy wax.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Ubbi terminal (Ctrl+Alt+T).</li>
        <li>Tàllal làkk bu la bëgg, ni vietnam:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Kood yi ngir làkk: <code>deu</code> (Almaa), <code>eng</code> (Àngale), <code>vie</code> (Vietnam), <code>spa</code> (Español), <code>fra</code> (Farañse), <code>ita</code> (Itali), <code>nld</code> (Holand), <code>fin</code> (Finland), <code>swe</code> (Suweed), <code>nor</code> (Norweej).</li>
        <li>Wone paket yi yépp:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ci liggéey)</p>
        <ol>
        <li>Sax file yi <code>*.traineddata</code> ci:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ni <code>vie.traineddata</code> ngir Vietnam).</li>
        <li>Wër file yi ci Tesseract làkk folder, ba noppi:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Noppi ngir nosukaay bi.)</li>
        <li>Waxtu wutal app bi (walla ubbi làkk bu ngiy wax).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Ci nosukaay yi yépp</p>
        <ul>
        <li>Tàllal <strong>OCRmyPDF</strong> ak <strong>Tesseract</strong> ci package manager. Làkk yi bari (Àngale, Almaa, Farañse).</li>
        <li>Làkk yi ŋun sabe man nañu tàllal – làkk bu ngiy wax moo tànkum làkk yi yépp.</li>
        </ul>

        <hr>
        <p><b>✅ Buy tàllal:</b> Dëgër wutal app – làkk bu bees ngiy wax day wone.</p>
        <p><b>📖 Ndimbal ci kood làkk:</b> Làkk yi yépp ci <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract documentation</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Pol yi Noto Sans",
        "info_noto_font_voice": "Ndimbal ngir tàllal pol yi Noto Sans",
        "btn_info_noto_font_install": "Xibaar pol bi",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Noppi tàllal pol yi Noto bu bañ bu Google</h2>

        <p><strong>Pol yi Noto</strong> pol yi open-source ci Google. Li ëpp: <em>"Toftu"</em> (ba tax, gaaw gaaw □) te tax wax te yépp ci Unicode standard. Li ëpp ci app yi wax te yépp làkk yi bari.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Noppi ci macOS</h3>

        <p><strong>Mbooloom 1: Ci Homebrew (ci xajaay)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Mbooloom 2: Ci "Font Book" (Noppi)</strong></p>

        <ol>
        <li>Sax pol bi:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ubbi file ZIP</li>
        <li>Wër file yi ci <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Noppi ci Windows (10 ak 11)</h3>

        <p><strong>Mbooloom 1: Microsoft Store (Noppi)</strong><br>
        Wax "Google Noto Fonts" walla "Noto Sans" te klick ci <strong>Tàllal</strong>.</p>

        <p><strong>Mbooloom 2: Tàllal ci liggéey</strong></p>

        <ol>
        <li>Sax:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Ubbi ZIP</li>
        <li>Tànkum file yi .ttf / .otf</li>
        <li>Klick bu wecc → <strong>Tàllal</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        walla<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Tur\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Noppi ci Linux</h3>

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

        <p>Xool:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Tànn lëj yi (bookmarks)",
        "bookmark_add": "Yokk lëj gi",
        "bookmark_add_tooltip": "Bépp xëtu mbir bi ngir lëj gi",
        "bookmark_remove": "Far lëj gi",
        "bookmark_remove_tooltip": "Tontu lëj gi",
        "bookmark_remove_all": "Far lépp",
        "bookmark_remove_all_tooltip": "Tontu lëj yi yépp ci PDF bi",
        "bookmark_jump": "Dem ci lëj gi",
        "bookmark_jump_tooltip": "Dem ci xëtu mbir bi",
        "bookmark_name": "Tur",
        "bookmark_page": "Xëtu mbir",
        "bookmark_no_bookmarks": "Lëj yi amul.\nKlick ci 'Yokk' ngir bépp xëtu mbir bi ngir lëj gi",
        "bookmark_added": "Lëj gi ngir xëtu mbir {0} yokk: {1}",
        "bookmark_removed": "Lëj gi far: {0}",
        "bookmark_all_removed": "Lëj yi yépp far.",
        "bookmark_name_default": "Xëtu mbir {0}",
        "bookmark_name_prompt": "Tur ngir lëj gi:\n(wax bu guddu day xaw 50 char)",
        "bookmark_name_prompt_title": "Tur lëj gi",
        "bookmark_confirm_remove_all": "Bëgg nga far lëj yi yépp {0}?",
        "menu_bookmarks": "Lëj yi",
        "bookmark_manage": "Tànn lëj yi",
        "bookmark_next": "Lëj bi ci topp",
        "bookmark_prev": "Lëj bi ci kanam",
        "bookmark_page_display": "Xëtu mbir {0}",
        "bookmark_exists": "Lëj gi am na kanam.",
        "bookmark_select_first": "Tànkum lëj gi bu jëkk.",
        "bookmark_confirm_remove": "Bëgg nga far lëj gi 'Xëtu mbir {0}: {1}'?",
        "bookmark_jumped_to": "Dem ci lëj gi '{0}' ci xëtu mbir {1}.",
        "bookmark_jumped_to_voice": "Lëj gi {0}, xëtu mbir {1}",
        "btn_close": "Ubbi",

        "bookmark_list": "Lëj yi ngir la",
        "bookmark_rename": "Turu lëj gi",
        "bookmark_rename_tooltip": "Turu lëj gi",
        "bookmark_rename_title": "Turu lëj gi",
        "bookmark_rename_prompt": "Tur bu bees ngir lëj gi ci xëtu mbir {0}:\n(50 char max)",
        "bookmark_renamed": "Lëj gi '{0}' am na tur bu bees '{1}'.",
        "bookmark_item_tooltip": "Xëtu mbir {0}: {1}\nKlick bu bàny ak yépp ngir dem",
        "bookmark_name_exists_question": "Lëj gi '{0}' am na kanam ci xëtu mbir bi.\nTuru ko lépp?",

        "context_bookmarks": "Lëj yi",
        "context_bookmark_add_here": "Yokk lëj gi ngir xëtu mbir bi",
        "context_bookmarks_existing": "Lëj yi ci kanam:",
        "context_bookmarks_jump": "Dem ci lëj gi:",
        "context_bookmarks_none": "Lëj yi amul",
        "context_bookmarks_clear_all": "Far lëj yi yépp {0}",

        "bookmark_search_placeholder": "Ceet lëj yi... (tur walla xëtu mbir)",
        "bookmark_search_results": "%d lëj yi gise ci \"%s\"",
        "bookmark_no_search_results": "Lëj yi giseul ci \"%s\"",
        "bookmark_no_search_results_label": "Lépp lëj gi giseul ci \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Sopale metadata PDF",
        "metadata_title": "Bëjjeem",
        "metadata_title_placeholder": "Bëjjeem document bi",
        "metadata_title_tooltip": "Bëjjeem document bi (ci barre bi)",
        "metadata_author": "Mbindum",
        "metadata_author_placeholder": "Tur mbindum bi",
        "metadata_author_tooltip": "Ci anga bind",
        "metadata_subject": "Mbiri",
        "metadata_subject_placeholder": "Mbiri document bi",
        "metadata_subject_tooltip": "Xibaar gi ci gàncarg",
        "metadata_keywords": "Kee yu toll",
        "metadata_keywords_placeholder": "Kee yu toll, tontu ci virgule",
        "metadata_keywords_tooltip": "Kee yu toll ngir document bi",
        "metadata_creator": "Sosukaay",
        "metadata_creator_placeholder": "App bi PDF bi sos",
        "metadata_creator_tooltip": "Software bi document bi sos",
        "metadata_producer": "Jëmukaay",
        "metadata_producer_placeholder": "App bi PDF bi wàll",
        "metadata_producer_tooltip": "Software bi PDF bi wàll",
        "metadata_creation_date": "Bés bu sos",
        "metadata_creation_date_tooltip": "Bés bu document bi sos",
        "metadata_mod_date": "Bés bu sopale",
        "metadata_mod_date_tooltip": "Bés bu sopale bi tis",
        "metadata_pdf_info": "📄 Xibaar PDF",
        "metadata_pages": "Xëtu mbir yi",
        "metadata_file_size": "Xëtu file bi",
        "metadata_pdf_version": "Version PDF",
        "metadata_encrypted": "Encrypt",
        "metadata_encrypted_yes": "Waaw (bañ)",
        "metadata_encrypted_no": "Déedét",
        "metadata_reload": "📂 Sàn sàn ci PDF",
        "metadata_reset": "Bàyyi sopale yi",
        "metadata_reloaded": "Metadata sàn sàn ci PDF.",
        "metadata_reset_done": "Metadata lépp wóor.",
        "metadata_no_file": "File PDF amul.",
        "metadata_save_error": "Njamala ci sag metadata",
        "metadata_saved": "Metadata sag noppi.",
        "metadata_pdf_version_unknown": "PDF (xamul)",
        "metadata_saved_message": "Metadata sag noppi.",
        "metadata_saved_voice": "Metadata sag.",

        "metadata_custom": "🔧 Metadata bu bees",
        "metadata_custom_placeholder": "{\n  \"safara_sama\": \"gëna_sama\",\n  \"safara_génn\": 123\n}",
        "metadata_custom_tooltip": "JSON format ngir metadata bu bees (bañ walla)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Template \"{0}\" tànkum - Klick bu bàny ak yépp ngir saw",
        "text_use_template": "Jëfandikoo bloc wax",
        "text_type": "Mbooloom",
        "text_search_templates": "Ceet bloc wax yi...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Xibaar Export / Import",
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

        <h3>📦 Li ëpp ci export? (Cosaan)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Teesal yi bu bañ ci app</span></li>
            <li class="detail">• Modu Dëkk/Bàyyi</li>
            <li class="detail">• Modu Dëkk ci li ëpp</li>
            <li class="detail">• Valeur gray ci tànn</li>
            <li class="detail">• Làkk</li>
            <li class="detail">• Fënêtre</li>
            <li class="detail">• Modu zoom</li>
            <li class="detail">• Navigation (Barre navigation)</li>
            <li class="detail">• Wax (on/off)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Teesal backup</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Tur file (Timestamp, Separator, Suffixes)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Teesal ngir saw</span></li>
            <li class="detail">• Signature</li>
            <li class="detail">• Wax ak bloc wax</li>
            <li class="detail">• Croix, image ak forme</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Teesal OCR</span></li>
            <li class="detail">• Làkk</li>
            <li class="detail">• Wattali OCR · Modu xëtu mbir</li>
            <li class="detail">• Préprocess image: Tànn li màgnal, Sell, Oversampling</li>
            <li class="detail">• Xibaar job yi</li>
            <li class="detail">• Modu inversion</li>
            <li class="detail">• Valeur gray ci tànn</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Lëj yi</span></li>
            <li class="detail">• Lëj yi yépp ci file PDF (Xëtu mbir, Tur, Waxtu bu sos)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Database password</span></li>
            <li class="detail">• Password PDF yi sag (encrypt walla text clair)</li>
            <li class="detail">• Hash password master (samaët)</li>
            <li class="detail">• Données vérification</li>
        </ul>

        <h4>⚠️ Xibaar ci ëpp</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Ci import:</strong>
            <ul>
                <li><span class="warning">➜ Li ëpp ci teesal yi yépp</span></li>
                <li>• Waxtu wutal app bi</li>
                <li>• Signature, bloc wax ak lëj yi ci kanam</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Password master ak mode export:</strong>
            <ul>
                <li>• Ci password master bi:</li>
                <li>  - <span style="color: #98FB98;"><strong>Décrypt</strong></span> (password yi ci text clair ci ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Encrypt</strong></span> (lu tax password master ci système cible)</li>
                <li>• Hash password master <strong>wax te</strong> encrypt</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Jaax:</strong>
            <ul>
                <li>• ZIP bi am na données (<strong>password, lëj yi, signature</strong>)</li>
                <li>• Bépp ko (ex: USB encrypt, password manager)</li>
                <li>• File bi jàppul, password PDF yi jàpp</li>
            </ul>
        </div>

        <h4>📁 Format export</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Teesal yi sag ci file ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP bi am na <code>settings.json</code> (cig configuration) ak file image signature ak password encrypt.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Sigantura - Jangal",
        'signature_guide_html': """
        📝 <strong>Sigantura - Jangal bu xew-xew</strong><br>
        <ul>
        <li>Def wuuru jaayuka bi</li>
        <li>Konfiguré sigantura ci menu <em>Tanoraayu</em> (nag, mbindum waxtu, …)</li>
        <li>Solal ci <strong>Klikk bu Dima</strong> ci wotug laaj (wuuru jaayuka bi laaj na buur bu nekk benn baatukaay)</li>
        <li>Féete sigantura bi mbooloom mbaa bijjaani rééy</li>
        <li>Solal sigantura yu bari ya wàll-wàll</li>
        <li>Bees yi xeetu sigantura bi mbooloo mbaa boobu</li>
        <li>Baal benn sigantura bi</li>
        <li>Dig / baal sigantura yépp waxtu bu benn</li>
        <li>Benn ci chu, mën nañu faral doonj bi.</li>
        </ul>
        """,
        'signature_guide_voice': "Jangal bu xew-xew ngir sigantura. Def wuuru jaayuka bi. Konfiguré sigantura ci tanoraayu. Solal ci klikk bu dima.",

        'image_guide_title': "Solal take - Jangal",
        'image_guide_html': """
        📷 <strong>Solal take ci PDF - Jangal bu xew-xew</strong><br>
        <ol>
        <li>Klikk bu dima ci wotug laaj</li>
        <li><em>„Solal take“</em> → Tak fame</li>
        <li>Dindi tak bi: Ruxal mbooloom</li>
        <li>Dimbal nagam: Ruxal ci punaawi/kallist</li>
        <li>Noorbenu mbind mi: <strong>[A]</strong> bijjaan</li>
        <li>Yu mángoo dimbal: Klikk bu dima ci tak bi</li>
        </ol>
        <p><strong>Benn cee:</strong> Ci menu konteks mën nga dimbal tanoraayu.</p>
        """,
        'image_guide_voice': "Jangal bu xew-xew ngir take. Klikk bu dima, solal take, fame. Dindi mbooloom, dimbal nagam ci punaawi. Noorbenu mbind mi ci bijjaan A.",

        'form_guide_title': "Solal mbind - Jangal",
        'form_guide_html': """
        📐 <strong>Solal mbind ci PDF - Jangal bu xew-xew</strong><br>
        <ol>
        <li>Fame bukki mbind (kare, cerkaar, toll, nemm)</li>
        <li>Klikk ci wotug:
            <ul>
            <li>Ngir kare/cerkaar: Klikk bu benn solal mbind</li>
            <li>Ngir toll/nemm: Klikk ñaar bu ab turam bu tollook ndigal ak lodd</li>
            </ul>
        </li>
        <li>Dindi mbind bi: Ruxal mbooloom</li>
        <li>Dimbal nagam: Ruxal ci punaawi/kallist</li>
        <li>Dig mbind bi: <strong>Enter</strong></li>
        <li>Baal mbind bi: <strong>ESC</strong></li>
        <li>Yu mángoo dimbal: Klikk bu dima ci mbind bi</li>
        </ol>
        <p><strong>Benn cee:</strong> Ci menu konteks mën nga dimbal tanoraayu.</p>
        """,
        'form_guide_voice': "Jangal bu xew-xew ngir mbind. Fame bukki mbind. Ngir kare mbaa cerkaar klikk benn waxtu, ngir toll mbaa nemm klikk ñaar waxtu. Dindi mbooloom, dimbal nagam ci punaawi. Dig ci Enter, baal ci Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "bu jëm kanam",
        "btn_next_result": "bu jëm",
        "ocr_text_window": "Lëndo matukaay OCR",
        "bookmark_existing": "Bookmark yu am",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Wuttali OCR Mac - Windows",
        'ocr_method_mac_win_title': "Noppu yu bokk ci OCR bu Mac ak Windows",
        'ocr_method_mac_win_voice': "Mac mëna a koy baax",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Noppu yu bokk ci macOS ak Windows</strong></p>

        <p><strong>macOS (recmmandé)</strong></p>
        <p>Doj:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Ñaari ci:</p>
        <ul>
        <li>PDF bu mën a féeteek matukaay ak matukaay ci xiimbuul bu mag bi yoreeli layuwaay.</li>
        </ul>
        <p>Mbay:</p>
        <ul>
        <li>Noppu bu aju ci matukaay bii bëgg a gise (ba ci xët yi ju diglu).</li>
        <li>Noorbenu grafik vektör ak fonte yu am.</li>
        <li>Bar progress GUI ci yoonu wuttali subprocess.</li>
        <li>Konfiguré wuñi ci paramètre yu bokk ci OCR (Deskew, Clean, Oversample, optimisasyo).</li>
        <li>Féete matukaay mën nga ko def ci liggéeykat bi (mbooloo PDF).</li>
        </ul>
        <p>Bës:</p>
        <ul>
        <li>Nogoo doj yu bari yu sistèm (ocrmypdf, Ghostscript, unpaper, pngquant – ci pakk App).</li>
        <li>Yor wu ndaw ci mbind (deadlocks, timeouts).</li>
        </ul>

        <p><strong>Windows (benn ci chu bu am)</strong></p>
        <p>Doj:</p>
        <ul>
        <li>pytesseract (lu gën a feeñal ci Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Ñaari ci:</p>
        <ul>
        <li>PDF bu mën a féeteek matukaay bu gën a feeñal PDF bu tak, waaye mën a féete ci matukaay bu ub.</li>
        </ul>
        <p>Mbay:</p>
        <ul>
        <li>Duma gis bu am.</li>
        </ul>
        <p>Bës:</p>
        <ul>
        <li>PDF bii benn taak ak matukaay bu gën a feeñ; layuwaay mën a wës ànd ak dokumaa yu bari (kolon, tablo).</li>
        <li>Du ci def wu bind (--deskew) mbaa xarala wu tak (--clean).</li>
        <li>Bar progress GUI yonu ba fii ci xët yi yu def.</li>
        <li>Loo OCR gën a baax lool (ci xët bi nu def).</li>
        <li>Féete matukaay bi yépp a dem ci OCR.</li>
        </ul>

        <p><strong>Noppu yu bokk</strong></p>
        <ul>
        <li>Ñi bokk ci def PDF bu mën a féete ci buum yi.</li>
        <li>Tanoraayu OCR (làkk, DPI, xët, mode OCR) ci OCRSettingsDialog.</li>
        </ul>

        <p><strong>Recmmandasyo:</strong></p>
        <ul>
        <li>macOS: ocrmypdf binary dafa baax – Sàcc Mac ak jëfandiko (PDFDarkView ci Mac mi ngi ci Apple Silicon mbaa Intel). OCR di baax lool ci Windows!</li>
        <li>Windows: Jëfandiko pytesseract. Dafa amal wu baax.</li>
        </ul>

        <p><strong>Nataal:</strong></p>
        <ul>
        <li>Ñi bokk ci def lu am.</li>
        <li>Programe dafa amal wu baax ci xaru yoon.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Def sigantura (ci scan)",
        "signature_create_title": "Fame sigantura yu scan (PDF/tak)",
        "image_pdf_filter": "Take yi ak PDF",
        "signature_pdf_empty": "PDF bi dafa am xët.",
        "signature_created_success": "Sigantura def ci baax: {0}",
        "signature_create_error": "Nga xare ci def sigantura:\n{0}",
        "rembg_missing": "rembg du ci def.\nDef ko: pip install rembg\nNga xare: {0}",
        "signature_name_title": "Tur wu file ngir sigantura",
        "signature_name_message": "Def tur wu file ngir sigantura bii (ci PNG ak wu ub):",
        "signature_name_label": "Tur file:",
        "signature_name_voice": "Def tur file ngir sigantura",
        "signature_processing": "Mën a def...",
        "signature_creation_title": "Sigantura mën a def",
        "signature_overwrite_warning": "File '{0}' am na. Overwrite?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Def PDF ngir sigantura",
        "signature_prepare_instruction":"Fame PDF bu am sigantura yu scan ci xët bu benn.\n\nNgir gise baax, néew:\n• Sigantura bi def na wu xara (stilo mbaa fineliner) ci wu baax.\n• Sigantura bi ci wu baax.\n• PDF bi def na ci 300 dpi.\n• Sigantura bi da wu baax.\n• Du am wu waxtu.",
        "signature_prepare_voice":"Fame PDF ak sigantura yu scan. Gis ci baax.",
        "sig_thickness_label":"Nog wu ligne:",
        "sig_thickness_normal":"Wu naw (wu ndaw)",
        "sig_thickness_bold":"Wu naw (recmmandé)",
        "sig_thickness_very_bold":"Wu naw lool",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Def làkk yu GUI ak OCR - Jangal",
        'language_guide_title': "Def làkk yu GUI ak OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Fame file <code>translations_xy.py</code> ci<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        ak def ci directory:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Fame browser.</li>
        <li>Def ci: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Gis "Releases" ak def <strong>"latest"</strong>.</li>
        <li>Def file <code>Source Code.zip</code>.</li>
        <li>Unzip ZIP file.</li>
        <li>Gis file làkk ak def ci directory:<br/>
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
        "menu_watermark":"Tereelu màll bi",
        "fullpage_text_watermark_title":"Tayal bu màll",
        "fullpage_image_watermark_title":"Nataal bu màll",
        "filename_with_watermark":"_ak_màll",
        "watermark_text":"Tayal:",
        "watermark_text_placeholder":"Saw tayal bu màll...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Dayo bu font:",
        "watermark_format":"Format:",
        "watermark_bold":"Daj",
        "watermark_italic":"Tof",
        "watermark_color":"Melo:",
        "watermark_choose_color":"Taneel melo...",
        "watermark_opacity":"Guddi / Xarala:",
        "watermark_direction":"Bànkug jàng:",
        "watermark_direction_l_r":"Ngañ ñu → Njub",
        "watermark_direction_bl_tr":"Suuf ngañ ñu → Kawe njub",
        "watermark_direction_tl_br":"Kawe ngañ ñu → Suuf",
        "watermark_direction_b_t":"Suuf → Kawe",
        "watermark_direction_t_b":"Kawe → Suuf",
        "watermark_preview":"Nanu:",
        "watermark_preview_sample":"Tayal jiite",
        "watermark_empty_text":"Taneel dugal tayal.",
        "watermark_applied":"Màll bi def na ci xetu yépp.",
        "watermark_saved":"Màll bi nangu na.",
        "image_scale":"Dayo:",
        "image_preview":"Nanu nataal:",
        "no_image_selected":"Nataal kenn nanguwu ko",
        "browse":"Xool...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Rey",
        "redact_add_black": "Rey (xawt)",
        "redact_add_white": "Rey (weex / far)",
        "redact_added_black": "Rey bu xawt dugal na",
        "redact_added_white": "Rey bu weex dugal na",
        "redact_apply_all": "Jëfandikoo rey yépp te nangu",
        "redact_discard_all": "Takk rey yépp",
        "redact_discard": "Takk rey ji",
        "no_redactions": "Rey kenn nanguwu ko",
        "redact_confirm_title": "Jëfandikoo rey yépp ci wàll",
        "redact_confirm_message": "Kaxaw: Fekku yi dugg wontey far (xawt walla weex).\nNangu jiitee dinañ ko def (su nu ko taneel).\n\nTudd?",
        "redact_apply": "Waaw, rey leegi",
        "redact_saved": "{0} rey jëfandikoo te nangu.",
        "redact_saved_voice": "{0} rey jëfandikoo",
        "redact_error": "Njuumte ci rey",
        "filename_redacted":"_rey",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Tereelu limbe xetu',
        'page_numbers_format': 'Format bu limbe:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Araab)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Rom tus)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Rom njur)',
        'page_numbers_format_letter': 'A, B, C ... (Tayal)',
        'page_numbers_format_custom': 'Taneel',
        'page_numbers_custom_pattern': 'Nataal:',
        'page_numbers_custom_placeholder': 'tamit "Xetu {nummer}" walla "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Jëfandikoo {nummer} ngir limbe bi neexe te {total} ngir limbe yépp',
        'page_numbers_position': 'Barab:',
        'page_numbers_pos_tl': 'Kawe ngañ ñu',
        'page_numbers_pos_tc': 'Kawe guddi',
        'page_numbers_pos_tr': 'Kawe njub',
        'page_numbers_pos_ml': 'Guddi ngañ ñu',
        'page_numbers_pos_mc': 'Ci guddi',
        'page_numbers_pos_mr': 'Guddi njub',
        'page_numbers_pos_bl': 'Suuf ngañ ñu',
        'page_numbers_pos_bc': 'Suuf guddi',
        'page_numbers_pos_br': 'Suuf njub',
        'page_numbers_margins': 'Njaareef:',
        'page_numbers_margin_x': 'Diggu wi:',
        'page_numbers_margin_y': 'Diggu tay:',
        'page_numbers_range': 'Xetug xetu:',
        'page_numbers_all_pages': 'Xetu yépp',
        'page_numbers_custom_range': 'Xetug taneel',
        'page_numbers_from': 'Jaw:',
        'page_numbers_to': 'Ba:',
        'page_numbers_progress': 'Tereelu limbe xetu...',
        'page_numbers_start': 'Tereelu limbe xetu jëm...',
        'page_numbers_cancel': 'Tereelu limbe xetu tàcc na',
        'page_numbers_success': 'Limbe xetu dugal na.\n\nDégg na nga xuloo PDF bu bees?\n\n{0}',
        'page_numbers_complete': 'Limbe xetu dugal na',
        'page_numbers_error_format': 'Njuumte ci tereelu limbe xetu: {0}',
        'page_numbers_content_type': 'Mbeexal:',
        'page_numbers_tab_simple': 'Limbe wuñ',
        'page_numbers_tab_range': 'Xetu X ci Y',
        'page_numbers_tab_date': 'Taariix',
        'page_numbers_tab_custom': 'Tayal bu am',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Xetu {aktuell} ci {gesamt}',
        'page_numbers_range_custom': 'Taneel',
        'page_numbers_range_placeholder': 'tamit "Xetu {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format bu taariix:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Samwie 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Taneel',
        'page_numbers_date_placeholder': 'tamit %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Barab:',
        'page_numbers_date_before': 'Taariix bu Jaraale limbe xetu',
        'page_numbers_date_after': 'Taariix bu Jêgale limbe xetu',
        'page_numbers_date_only': 'Taariix (ba limbe xetu)',
        'page_numbers_custom_text': 'Tayal bu taneel:',
        'page_numbers_custom_placeholder_text': 'Jëfandikoo {seite} ngir limbe xetu te {gesamt} ngir yépp\ntamit "Sëcret - Xetu {seite}" walla "{seite} ci {gesamt}"',
        "filename_with_page_number":"_ak_limbe_xetu",
        "filename_with_page_declaration":"_ak_xalaat_xetu",
        "filename_with_pagenumber":"_ak_limbe_xetu",
        "filename_with_date":"_ak_taariix",
        "filename_with_my_page_declaration":"_ak_xalaat_xetu_bu_taneel",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Tànk bu nanguwu ko",
        "unsaved_changes_message_darkmode": "Tereel yu nanguwu ko.\nDégg na nga nangu leen ba fàtte?",
        "save_and_switch": "Nangu te fàtte",
        "discard_and_switch": "Fàtte leegi",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Xetu yépp wàcc nataal',
        'export_images_menu': 'Wàcc nataal (PNG/JPEG)',
        'export_images_format': 'Format bu nataal:',
        'export_images_dpi': 'Xool (DPI):',
        'export_images_quality': 'MBooj bu JPEG:',
        'export_images_range': 'Xetug xetu:',
        'export_images_all_pages': 'Xetu yépp',
        'export_images_custom_range': 'Xetug taneel',
        'export_images_from': 'Jaw:',
        'export_images_to': 'Ba:',
        'export_images_options': 'Taneel:',
        'export_images_single_files': 'Xetu bu nekk tegi',
        'export_images_subfolder': 'Wàcc ci subfolder',
        'export_images_subfolder_info': 'Ci subfolder "turuPDF_nataal"',
        'export_images_same_folder': 'Ci folder bu nekk ak PDF',
        'export_images_apply_darkmode': 'Jëfandikoo PDFDarkView (Modu Dàgg)',
        'export_images_target_folder': 'Folder bu xuloo:',
        'export_images_browse': 'Xool...',
        'export_images_preview': 'Nanu:',
        'export_images_preview_info': 'Taneel wàcc',
        'export_images_preview_info_detail': '{0} xetu ci {1}\nXool: {2} DPI\nTuru fayil: {3}\n{4}',
        'export_images_select_folder': 'Taneel folder bu xuloo',
        'export_images_start': 'Wàcc nataal jëm...',
        'export_images_progress': 'Wàcc nataal...',
        'export_images_saving': 'Nangu xetu {0} ci {1}...',
        'export_images_success': 'Wàcc na!\n\n{0} nataal nangu na ci:\n{1}',
        'export_images_complete': 'Wàcc nataal na',
        'export_images_open_folder': '📁 Xuloo folder',
        'export_images_cancel': 'Wàcc nataal tàcc na',
        'export_images_error_format': 'Njuumte ci wàcc nataal: {0}',
        'export_images_pdf2image_missing': 'Librari "pdf2image" nga nanguwu ko.\n\nTaneel nga nangu ko ak:\npip install pdf2image\n\nNgir Windows, Poppler soxla:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A wàllu ngir njub di',
        'pdfa_menu': 'PDF/A wàllu (njub di)',
        'pdfa_info': 'Wàllu PDF ci PDF/A.\n\nPDF/A wax ñu ko ngir njub di, te dina taxawu ci jamono.',
        'pdfa_standard': 'PDF/A wàllu:',
        'pdfa_standard_select': 'Melokaan:',
        'pdfa_1': 'PDF/A-1 (wun, jëfandikoo)',
        'pdfa_2': 'PDF/A-2 (jamono, njareef)',
        'pdfa_3': 'PDF/A-3 (melokaan bu bees, fayil yépp)',
        'pdfa_standards_explanation': '📖 Xalaat wàllu:\n\n'
            '• PDF/A-1: Gànc, jëfandikoo (2005)\n'
            '• PDF/A-2: Jamono, njareef, xarala (2011)\n'
            '• PDF/A-3: Melokaan bu bees, fayil yépp (2013)\n\n'
            'Wax: PDF/A-2 mooy mbir bu baax ci jëfandikoo ak jamono.',
        'pdfa_options': 'Taneel:',
        'pdfa_compress_enable': 'Compres PDF (fayil bu ndaw)',
        'pdfa_metadata_preserve': 'Nangu metadata (turu, boroom, ak yeneen)',
        'pdfa_target_folder': 'Folder bu xuloo:',
        'pdfa_browse': 'Xool...',
        'pdfa_select_folder': 'Taneel folder bu xuloo',
        'pdfa_ocr_info_unknown': '🔍 Tayal xoolu ko.',
        'pdfa_ocr_info_not_needed': '✅ Tayal neexna - OCR soxlawu.\nPDF/A dinañ def.',
        'pdfa_ocr_info_recommended': '⚠️ Tayal baax xoolu ko.\n\nNgir PDF yu xool, OCR soxla.\nXalaat: PDF/A ak OCR dépp na - waaye tayal xoolu.',
        'pdfa_ocr_info_error': '❌ Njuumte ci xool: {0}',
        'pdfa_start': 'PDF/A wàllu jëm...',
        'pdfa_progress': 'PDF/A wàllu...',
        'pdfa_success': 'PDF/A wàllu na!\n\nNangu:\n{0}\n\nDégg na nga xuloo PDF bu bees?',
        'pdfa_complete': 'PDF/A wàllu na',
        'pdfa_cancel': 'PDF/A wàllu tàcc na',
        'pdfa_error_format': 'Njuumte ci PDF/A wàllu:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Librari "ocrmypdf" nga nanguwu ko.\n\nTaneel nga nangu ko ak:\npip install ocrmypdf',
        'btn_convert': 'Wàllu',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF ci baax (dayo fayil tàkk)',
        'optimize_menu': 'PDF ci baax (dayo fayil)',
        'optimize_info': 'Tàkk dayo fayil PDF ak yeneen.\n\nCompres di njëkk, dayo di ndaw - waaye nataal mbooj.',
        'optimize_level': 'Compres:',
        'optimize_level_low': 'Ndaw (xew, ndaw)',
        'optimize_level_medium': 'Guddi (mbir bu baax)',
        'optimize_level_high': 'Njëkk (njëkk)',
        'optimize_level_maximum': 'Njëkk (njëkk, daw)',
        'optimize_level_explanation': 'Wax: "Guddi" mooy mbir bu baax ci xew ak dayo.',
        'optimize_options': 'Taneel:',
        'optimize_compress_images': 'Compres nataal (tàkk JPEG mbooj)',
        'optimize_clean_objects': 'Far ci yeneen',
        'optimize_preserve_metadata': 'Nangu metadata (turu, boroom, ak yeneen)',
        'optimize_image_quality': 'Mbooj nataal:',
        'optimize_range': 'Xetug xetu:',
        'optimize_all_pages': 'Xetu yépp',
        'optimize_custom_range': 'Xetug taneel',
        'optimize_from': 'Jaw:',
        'optimize_to': 'Ba:',
        'optimize_target_folder': 'Folder bu xuloo:',
        'optimize_browse': 'Xool...',
        'optimize_select_folder': 'Taneel folder bu xuloo',
        'optimize_info_box': 'Xalaat',
        'optimize_info_text': 'Optimisation dina jàpp jamono PDF yu mag.\n\nNataal nangu ci mbooj bu ndaw, nga tàkk dayo.',
        'optimize_start': 'PDF optimisation jëm...',
        'optimize_progress': 'PDF optimisation...',
        'optimize_cancel': 'PDF optimisation tàcc na',
        'optimize_complete': 'PDF optimisation na',
        'optimize_error_format': 'Njuumte ci PDF optimisation:\n\n{0}',
        'optimize_success_message': 'PDF optimisation na!\n\nNangu:\n{0}\n\nJaraale: {1}\nJëgale: {2}\nTàkk: {3:.1f}%\n\n{4}\n\nDégg na nga xuloo PDF bu bees?',
        'optimize_success_message_no_size': 'PDF optimisation na!\n\nNangu:\n{0}\n\nDayo xoolu.\n\nDégg na nga xuloo PDF bu bees?',
        'optimize_result_positive': 'Fayil tàkk {0:.1f}%.',
        'optimize_result_zero': 'Dayo fayil nangu.',
        'optimize_result_negative': 'Fayil dayo {0:.1f}%.\nOptimisation tàcc na, fayil jaraale nangu.',
        'btn_optimize': 'Optimisation jëm',
        'filename_optimize_low_suffix': '_optimisation_ndaw',
        'filename_optimize_medium_suffix': '_optimisation',
        'filename_optimize_high_suffix': '_optimisation_njëkk',
        'filename_optimize_maximum_suffix': '_optimisation_njëkk',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF sàcc',
        'crop_menu': 'PDF sàcc (Crop)',
        'crop_range': 'Jëfandikoo:',
        'crop_all_pages': 'Xetu yépp',
        'crop_current_page': 'Xetu bi neexe',
        'crop_values': 'Sàcc (ci point):',
        'crop_left': 'Ngañ ñu:',
        'crop_right': 'Njub:',
        'crop_top': 'Kawe:',
        'crop_bottom': 'Suuf:',
        'crop_presets': 'Taneel:',
        'crop_preset_white': 'Xool weex',
        'crop_reset': 'Tàkk',
        'crop_mouse_hint': '🖱️ Sàcc nga xool.\nJëfandikoo SpinBox taneel.\nXoolu man.',
        'crop_apply': 'Sàcc',
        'crop_scope_all': 'Xetu yépp',
        'crop_scope_current': 'Xetu bi neexe',
        'crop_new_size': 'Dayo bees: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'PDF kenn nanguwu ko',
        'crop_preview_error': 'Njuumte ci nanu',
        'crop_start': 'Sàcc jëm...',
        'crop_progress': 'PDF sàcc...',
        'crop_success': 'PDF sàcc na!\n\nNangu:\n{0}\n\nDégg na nga xuloo PDF bu bees?',
        'crop_complete': 'Sàcc na',
        'crop_cancel': 'Sàcc tàcc na',
        'crop_error_format': 'Njuumte ci sàcc:\n\n{0}',
        'filename_crop_suffix': '_sàcc',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF wàll (Flatten)',
        'flatten_menu': 'PDF wàll (Flatten)',
        'flatten_info': 'PDF wàll "far" yépp ci xetu.\n\nJëgale, jëfandikoo',
        'flatten_explanation_title': '📖 Lu?',
        'flatten_explanation_text': 'PDF wàll soxla:\n\n'
            '• 📄 Print\n'
            '• 🔒 Jëfandikoo\n'
            '• 📎 Xalaat\n'
            '• 🖼️ Tayal, nataal, ak yeneen\n'
            '• 📦 Archive\n\n'
            'PDF wàll dayo tàkk te jëfandikoo.',
        'flatten_what_title': 'Lu wàll?',
        'flatten_what_list': '• ✅ Form (tayal, check, button)\n'
            '• ✅ Xalaat (comment, highlight, note)\n'
            '• ✅ Overlay (tayal, nataal, ak yeneen)',
        'flatten_options': 'Taneel:',
        'flatten_forms': 'Form wàll',
        'flatten_annotations': 'Xalaat wàll',
        'flatten_overlays': 'Overlay wàll (tayal, nataal, ak yeneen)',
        'flatten_target_folder': 'Folder bu xuloo:',
        'flatten_browse': 'Xool...',
        'flatten_select_folder': 'Taneel folder bu xuloo',
        'flatten_warning': '⚠️ Wàll man!\n\nJëgale, jëfandikoo.\nNangu nga.',
        'flatten_apply': 'Wàll',
        'flatten_start': 'Wàll jëm...',
        'flatten_progress': 'PDF wàll...',
        'flatten_success': 'PDF wàll na!\n\nNangu:\n{0}\n\nDégg na nga xuloo PDF bu bees?',
        'flatten_complete': 'Wàll na',
        'flatten_cancel': 'Wàll tàcc na',
        'flatten_error_format': 'Njuumte ci wàll:\n\n{0}',
        'filename_flatten_suffix': '_wàll',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF overlay (Overlay)',
        'overlay_menu': 'PDF overlay (Overlay)',
        'overlay_info': 'Dugal PDF (overlay) ci PDF.\n\nOverlay PDF dugg ci base PDF. Ngir màll, logo, walla stamp.',
        'overlay_explanation_title': '📖 Lu?',
        'overlay_explanation_text': 'Overlay soxla:\n\n'
            '• 🏢 Logo ci xetu yépp\n'
            '• 📄 Letterhead ci PDF\n'
            '• 🖊️ Stamp overlay\n'
            '• 🔖 Màll ci xetu yépp\n'
            '• 📑 Form overlay',
        'overlay_type': 'Overlay:',
        'overlay_type_fullpage': 'Xetu (cover)',
        'overlay_type_transparent': 'Xetu (xarala - wax)',
        'overlay_type_stamp': 'Stamp (taneel)',
        'overlay_type_info_fullpage': '📄 Overlay PDF dugg.\nWeex far.',
        'overlay_type_info_transparent': '🔍 Overlay PDF dugg ak xarala.\nWeex far - màll ak logo!',
        'overlay_type_info_stamp': '🖊️ Overlay PDF dugg stamp.\nLogo, stamp, walla signature ci barab.',
        'overlay_remove_background': 'Far weex:',
        'overlay_remove_background_enable': 'Far weex ci overlay PDF (xarala)',
        'overlay_remove_background_tooltip': 'Far weex ci overlay PDF ngir tayal xool.',
        'overlay_threshold': 'Xool:',
        'overlay_threshold_hint': '(1-254, njëkk = weex far)',
        'overlay_select_file': 'Taneel overlay PDF:',
        'overlay_file_placeholder': 'Taneel PDF file ngir overlay',
        'overlay_browse': 'Xool...',
        'overlay_select_overlay': 'Taneel overlay PDF',
        'overlay_range': 'Xetug xetu:',
        'overlay_all_pages': 'Xetu yépp',
        'overlay_custom_range': 'Xetug taneel',
        'overlay_from': 'Jaw:',
        'overlay_to': 'Ba:',
        'overlay_position': 'Barab:',
        'overlay_position_center': 'Guddi',
        'overlay_position_top_left': 'Kawe ngañ ñu',
        'overlay_position_top_right': 'Kawe njub',
        'overlay_position_bottom_left': 'Suuf ngañ ñu',
        'overlay_position_bottom_right': 'Suuf njub',
        'overlay_size': 'Dayo:',
        'overlay_size_original': 'Dayo jaraale',
        'overlay_size_fit_page': 'Xetu',
        'overlay_size_custom': 'Taneel (%)',
        'overlay_opacity': 'Xarala:',
        'overlay_target_folder': 'Folder bu xuloo:',
        'overlay_browse_folder': 'Xool...',
        'overlay_select_folder': 'Taneel folder bu xuloo',
        'overlay_warning': '⚠️ Overlay PDF dugg base PDF te "far" ci.\n\nJëgale, jëfandikoo.',
        'overlay_apply': 'Overlay',
        'overlay_start': 'Overlay jëm...',
        'overlay_progress': 'PDF overlay...',
        'overlay_success': 'PDF overlay na!\n\nNangu:\n{0}\n\nDégg na nga xuloo PDF bu bees?',
        'overlay_complete': 'Overlay na',
        'overlay_cancel': 'Overlay tàcc na',
        'overlay_error_format': 'Njuumte ci overlay:\n\n{0}',
        'overlay_no_file': 'Overlay PDF kenn nanguwu ko.\n\nTaneel PDF file ngir overlay.',
        'filename_overlay_suffix': '_overlay',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Nataal ci PDF',
        'extract_images_menu': 'Nataal yépp',
        'extract_images_info': 'Nataal yépp ci PDF te nangu.\n\nNataal nangu ci format jaraale walla format bees.',
        'extract_images_format': 'Format nataal:',
        'extract_images_quality': 'Mbooj JPEG:',
        'extract_images_options': 'Taneel:',
        'extract_images_subfolder': 'Nataal ci subfolder ("turuPDF_nataal")',
        'extract_images_unique': 'Nataal (duplicate)',
        'extract_images_range': 'Xetug xetu:',
        'extract_images_all_pages': 'Xetu yépp',
        'extract_images_custom_range': 'Xetug taneel',
        'extract_images_from': 'Jaw:',
        'extract_images_to': 'Ba:',
        'extract_images_target_folder': 'Folder bu xuloo:',
        'extract_images_browse': 'Xool...',
        'extract_images_select_folder': 'Taneel folder bu xuloo',
        'extract_images_info_box': 'Xalaat',
        'extract_images_info_text': 'Nataal dina jàpp jamono PDF yu mag.\n\nNataal nangu ak tur (xetu_nataal).',
        'extract_images_extract': 'Nataal',
        'extract_images_start': 'Nataal jëm...',
        'extract_images_progress': 'Nataal...',
        'extract_images_success': '✅ Nataal na!\n\n{0} nataal nangu ci:\n{1}',
        'extract_images_complete': 'Nataal na',
        'extract_images_cancel': 'Nataal tàcc na',
        'extract_images_error_format': 'Njuumte ci nataal:\n\n{0}',
        'extract_images_open_folder': '📁 Xuloo folder',
        'extract_images_no_images': 'Nataal kenn ci PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Xetu yu bari ci xetu (N-Up)',
        'nup_menu': 'Xetu yu bari ci xetu (N-Up)',
        'nup_info': 'Xetu yu bari ci xetu.\n\nNgir print, xool, walla handout.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Nanu:',
        'nup_preview_info': '{0} xetu → {1} xetu ci sheet → {2} sheet\nLayout: {3}',
        'nup_order': 'Tudd:',
        'nup_order_horizontal': 'Horizontal (réw)',
        'nup_order_vertical': 'Vertical (kolon)',
        'nup_order_horizontal_reverse': 'Horizontal réw',
        'nup_order_vertical_reverse': 'Vertical réw',
        'nup_range': 'Xetug xetu:',
        'nup_all_pages': 'Xetu yépp',
        'nup_custom_range': 'Xetug taneel',
        'nup_from': 'Jaw:',
        'nup_to': 'Ba:',
        'nup_options': 'Taneel:',
        'nup_margins': 'Njaareef:',
        'nup_margin_between': 'Diggu xetu:',
        'nup_page_numbers': 'Tereelu limbe xetu',
        'nup_target_folder': 'Folder bu xuloo:',
        'nup_browse': 'Xool...',
        'nup_select_folder': 'Taneel folder bu xuloo',
        'nup_create': 'Def',
        'nup_start': 'N-Up jëm...',
        'nup_progress': 'N-Up def...',
        'nup_success': 'N-Up def na!\n\nNangu:\n{0}\n\nDégg na nga xuloo PDF bu bees?',
        'nup_complete': 'N-Up na',
        'nup_cancel': 'N-Up tàcc na',
        'nup_error_format': 'Njuumte ci N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Tàkk dayo xetu',
        'pagesize_menu': 'Tàkk dayo xetu',
        'pagesize_info': 'Tàkk dayo xetu PDF.\n\nTayal dina wàll.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Taneel format:',
        'pagesize_custom': 'Dayo taneel:',
        'pagesize_width': 'Rëy:',
        'pagesize_height': 'Kawe:',
        'pagesize_orientation': 'Orientation:',
        'pagesize_portrait': 'Portrait',
        'pagesize_landscape': 'Landscape',
        'pagesize_scale_options': 'Scale:',
        'pagesize_fit': 'Wàll (ratio)',
        'pagesize_stretch': 'Sàcc (distort)',
        'pagesize_center': 'Guddi (dayo jaraale)',
        'pagesize_range': 'Xetug xetu:',
        'pagesize_all_pages': 'Xetu yépp',
        'pagesize_custom_range': 'Xetug taneel',
        'pagesize_from': 'Jaw:',
        'pagesize_to': 'Ba:',
        'pagesize_target_folder': 'Folder bu xuloo:',
        'pagesize_browse': 'Xool...',
        'pagesize_select_folder': 'Taneel folder bu xuloo',
        'pagesize_apply': 'Jëfandikoo',
        'pagesize_start': 'Tàkk dayo xetu jëm...',
        'pagesize_progress': 'Tàkk dayo xetu...',
        'pagesize_success': 'Dayo xetu tàkk na!\n\nNangu:\n{0}\n\nDégg na nga xuloo PDF bu bees?',
        'pagesize_complete': 'Tàkk dayo xetu na',
        'pagesize_cancel': 'Tàkk dayo xetu tàcc na',
        'pagesize_error_format': 'Njuumte ci tàkk dayo xetu:\n\n{0}',
        'pagesize_preview_info': 'Dayo bees: {0} x {1} pt',
        'filename_pagesize_suffix': '_dayo_bee',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Xalaat PDF',
        'pdf_info_menu': 'Xool PDF',
        'pdf_info_voice': 'PDF xalaat...',
        'pdf_info_error': 'Njuumte ci xool PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Xool shortcut",
        "shortcuts_dialog_title": "Shortcut",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FAYIL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Xuloo PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Tàpp PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Nangu...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Jàmm document</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Print</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Print (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Far</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 WÀCC</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Wàcc Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Wàcc DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Wàcc TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Wàcc nataal (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Nataal</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOCUMENT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF wàll</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF overlay</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF optimisation</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ JËFANDIKOO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Xool</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 XETU</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Xetu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Xetu yépp</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Xetu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Xetu yépp</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Far xetu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Xetu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Tereelu xetu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Xetu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Dayo xetu</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 TEREEL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Tayal</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>X</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Signature 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Signature 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Nataal</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rectangle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ellipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Ligne</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Flèche</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Limbe xetu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Màll tayal</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Màll nataal</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REY</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Rey (xawt)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Rey (weex)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rey yépp</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ADVANCÉ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF sàcc</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ XOOL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Dàgg/Xarala</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Tayal</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Xetu (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Xetu (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Xool (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ TANEEL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Password</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Signature</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Fayil</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Wàcc</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Tereel</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ XALAAT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF xalaat</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Wax</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Menu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Versiom bu bees am na",
        "update_available_message": "Am na versiom bu bees <b>{0}</b>.\n\nJéexal xët waxtu bi ngay jël leen:\n{1}",
        "update_available_voice": "Versiom bu bees {0} am na. Jël leen ci xët wi GitHub.",
        "update_open_release": "Ubbi xët waxtu bi",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Jël wàlluñu yi",
        "ask_download_all_translations": """Nekk nañu {total_languages} làkk GUI, te tànk ci làkk wu Jermaa, wu Angale ak wu Wiyetnaam.\n\nDafañu bëgg a jox / ko wut?\n\nTànk:\nLàkk yi duñu bëgg, nga leen defar ci doomiir bi:\n{translations_path}
        \nSu nga bokk, nga leen jël ci lu ñuul bi 'Mbëttel → Wut wàlluñu yi'.""",
        "menu_update_translations": "Wut wàlluñu yi",
        "translations_updated": "Wàlluñu yi wutt nañu",
        "translations_update_success": "{} wàlluñu wutt nañu ({} bees, {} wutt).",
        "translations_update_error": "Njamal ci wut wàlluñu yi",
        "translations_update_no_changes": "Wàlluñu yi nekk nañu ci jamono bi.",
        "translations_update_offline": "Amul liñkaay gu Internet. Wàlluñu yi duñu wut.",
        "translations_update_in_progress": "Wàlluñu yi wutt nañu ci sàx i...",
        "translations_downloading": "Jël wàlluñu yi...",
        "translations_path_hint": "Doomiir bu jëfandikukat bu wàlluñu",
        "translations_update_not_available_title": "Wut wi nekkul",
        "translations_update_not_available_message": """Wut wàlluñu yi nekk na ci versiom bu indi.\n\nCi moode bu sos, wàlluñu yi nekk nañu ci jamono bi.""",
        "translations_update_no_internet_title": "Amul liñkaay gu Internet",
        "translations_update_no_internet_message": """Dëppu gu Internet du am.\n\nDuñu jël wàlluñu yi ci GitHub.\n\nTànn xam-xam yi:
        • Tànn liñkaay gu Internet
        • Nagal firewall bi
        • Gisal benn waxtu
        \nNga jël wàlluñu yi ci GitHub ci sa bopp:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Wut wi am na",
        "btn_retry": "Gisal",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Samañ ci PDF Dark View",
        "welcome_title_not_supported": "Samañ ci PDF Dark View",
        "welcome_message": "Samañ ci PDF Dark View!\n\nLàkk bi nga jëfandikoo '{language}'.\nDanga bëgg a jëfandikoo làkk bi ci interface?\n\nDanga wut làkk bi ci 'Jàllal → Làkk'.",
        "welcome_message_language_not_available": "Samañ ci PDF Dark View!\n\nLàkk bi nga jëfandikoo '{language}'.\nLàkk bi indul.\n\nDanga bëgg a jël wàlluñu yi ci {language} ci GitHub?\n\n(Làkk bi dina jëfandikoo ci interface.)",
        "welcome_message_language_not_supported": "Samañ ci PDF Dark View!\n\nLàkk bi nga jëfandikoo '{language}'.\nRaxas, amul wàlluñu ci làkk bi.\n\nInterface bi dina bon ci {fallback_language}.\n\nDanga wut làkk bi ci 'Jàllal → Làkk'.\nSu nga bëgg, nga jox wàlluñu ci làkk bo:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Waaw, jëfandikoo làkk bi",
        "welcome_keep_english": "Déed, tànk ci làkk wu Angale",
        "welcome_download_language": "Waaw, jël {language}",

        # ============================================
        # 107. TUDDU YI JÉFANDIKKOON BU NEK
        # ============================================

        'menu_recent': 'Jéfandikkoon bu nek',
        'menu_recent_dirs': 'Répertoires...',
        'menu_recent_files': 'Fichiers...',
        'recent_manage': 'Yokkale...',
        'recent_enable_tracking': 'Bokk tuddu yi jéfandikkoon bu nek (sirum)',
        'recent_enable_info': 'Nuddal feññeel bi ngir dei tuddu',
        'recent_tracking_disabled': 'Sikkale tuddu di nuddal',
        'recent_enabled': 'nuddaloon',
        'recent_disabled': 'nuddalekoon',
        'recent_tracking_status': 'Sikkale tuddu {0}',
        'recent_dialog_title': 'Tuddu yi jéfandikkoon bu nek',
        'recent_tab_directories': 'Répertoires',
        'recent_tab_files': 'Fichiers',
        'recent_dirs_instruction': 'Tàppul ñaari baat ngir ubbi dialogue bi ci répertoire bi',
        'recent_files_instruction': 'Tàppul ñaari baat ngir ubbi PDF bi ba noppi',
        'recent_no_directories': '(amul répertoire bu bokk)',
        'recent_no_files': '(amul fichier bu bokk)',
        'recent_default_current': '⭐ Ci boo xam: {0}',
        'recent_set_as_default': '⭐ Wax ci boo xam',
        'recent_default_set_title': 'Répertoire ci boo xam làkkoon',
        'recent_default_set_message': 'Répertoire bi "{0}" làkkoon ci boo xam ngir ubbi PDF yi.',
        'recent_default_set_voice': 'Répertoire ci boo xam làkkoon',
        'recent_directory_not_found': 'Répertoire bañu ko man',
        'recent_file_not_found': 'Fichier bañu ko man',
        'recent_remove_selected': 'Fal',
        'recent_remove_title': 'Fal tuddu bi',
        'recent_remove_confirm': 'Deesu bëgg fal tuddu bi "{0}" ci limbu bi?',
        'recent_path_removed': 'Tuddu bi falu na',
        'recent_clear_all': 'Fal lépp',
        'recent_clear_title': 'Fal tuddu yi lépp',
        'recent_clear_confirm_type': 'Deesu bëgg far {0} lépp?',
        'recent_cleared': 'Limbu bi waccu na',
        'recent_path_not_found_title': 'Tuddu bañu ko man',
        'recent_path_not_found_message': 'Tuddu bi "{0}" nekkul wone.',
        'recent_open_file': 'Ubbi fichier',
        'btn_open_recent': 'Ubbi',
        'recent_open_file_question': 'Deesu bëgg ubbi "{0}" niki PDF?',
        'recent_not_pdf': 'Fichier mi ñu tàppale du PDF.',
        'recent_more_entries': 'Entrées yu bare...',
        'btn_remove': 'Fal',
        'btn_clear': 'Waccu lépp',
        'recent_context_open': 'Ubbi',
        'recent_context_reveal': 'Wone ci Finder',
        'recent_context_set_default': '⭐ Wax ci boo xam',
        'recent_context_open_terminal': '💻 Ubbi terminal bi',
        'recent_context_file_info': 'Xibaar fichier mi',
        'recent_context_open_with_default': '📄 Ubbi ak application ci boo xam',
        'recent_context_remove': 'Fal ci limbu bi',
        'recent_context_clear_all': 'Fal lépp',
        'recent_file_info_title': 'Xibaar fichier mi',
        'recent_file_info_name': 'Turu',
        'recent_file_info_path': 'Tuddu',
        'recent_file_info_size': 'Dayo',
        'recent_file_info_modified': 'Soppi',
        'recent_file_info_pages': 'Xët',
        'recent_error_reveal': 'Njuumte ci ubbi ci Finder',
        'recent_error_terminal': 'Njuumte ci ubbi terminal bi',
        'recent_error_info': 'Njuumte ci jël xibaar fichier mi',
        'open_user_data_folder': 'Wone répertoire bii xarala',

        # ============================================
        # 108. FAL XËT YI TUSSI/SUNA
        # ============================================
        "pages_delete_even": "Fal xët yi tussi lépp",
        "pages_delete_odd":  "Fal xët yi suna lépp",
        "progress_even_pages": "Fal xët yi tussi",
        "progress_odd_pages": "Fal xët yi suna",
        "progress_mark_delete_even": "{} xët bu tussi faral",
        "progress_mark_delete_odd":  "{} xët bu suna faral",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Prograam bi dafa dëpp",

    }
