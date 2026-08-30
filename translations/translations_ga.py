
# ============================================
# translations_ga.py - Irisches Wörterbuch
# Vollständig sortiert nach Kategorien
# ============================================

def load_irish_strings():
    """Lädt alle irischen Strings (Gaeilge)"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View le BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Luchtaigh PDF",
        'btn_text_window': "Téacs OCR",
        'btn_first': "An Chéad Leathanach",
        'btn_prev': "Leathanach Roimhe",
        'btn_next': "Chéad Leathanach Eile",
        'btn_last': "Leathanach Deireanach",
        'btn_print': "Priontáil",
        'btn_darkmode_light': "Mód Geal",
        'btn_darkmode_dark': "Mód Dorcha",
        'btn_delete_pages': "Scrios Leathanaigh",
        'btn_extract_pages': "Bain Leathanaigh",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Cealaigh",
        'btn_save': "Sábháil",
        'btn_close': "Dún",
        'btn_delete': "Scrios",
        'btn_delete_all': "Scrios Uile",
        'btn_copy': "Cóipeáil",
        'btn_export': "Easpórtáil",
        'btn_show': "Taispeáin Pasfhocal",
        'btn_hide': "Folaigh Pasfhocal",
        'btn_authenticate': "Fíordheimhnigh",
        'btn_settings': "Socruithe",
        'btn_protect': "Cosain",
        'btn_remove_password': "Bain Pasfhocal",
        'btn_manage': "Bainistíocht Pasfhocal",
        'btn_retry': "Bain Triail Eile As",
        'btn_select_all': "Roghnaigh Uile",
        'btn_clear_selection': "Glan Roghnú",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Leathanach {0} as {1}",
        'page_count': "as {0}",
        'goto_page': "Téigh go Leathanach",
        'page_simple': "Leathanach {0}",
        'full_view_page': "Amharc Iomlán Leathanach {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Iontráil téarma cuardaigh + Iontráil",
        'search_results': "Torthaí: {0} as {1}",
        'search_nav_hint': "Iontráil: chéad toradh eile  (Shift+Iontráil: toradh roimhe)",
        'search_no_results': "Gan Torthaí",
        'search_error': "Earráid Cuardaigh",
        'search_active': "Réimse Cuardaigh gníomhachtaithe",
        'search_closed': "Cuardach críochnaithe",
        'search_position': "Leathanach {0} {1}",
        'search_pos_top': "barr amach",
        'search_pos_upper': "thuas",
        'search_pos_middle': "lár",
        'search_pos_lower': "thíos",
        'search_pos_bottom': "bun amach",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "D'éirigh le haithint téacs!",
        'ocr_success_title': "OCR Rathúil",
        'ocr_success_message': "Tá an doiciméad in-aimsithe anois.",
        'ocr_failed': "Theip ar OCR",
        'ocr_in_progress': "OCR ar siúl",
        'ocr_preparing': "Ag ullmhú PDF...",
        'ocr_analyzing': "Ag anailísiú PDF...",
        'ocr_optimizing': "Leasú íomhá ar siúl...",
        'ocr_recognizing': "Ag aithint téacs...",
        'ocr_embedding': "Ag leabú téacs...",
        'ocr_finalizing': "Ag críochnú PDF...",
        'ocr_not_available': "OCR ar fáil",
        'ocr_install_message': "Níor aimsíodh uirlisí OCR.\n\nSuiteáil iad le do thoil:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR ag teastáil",
        'ocr_question': "Níl téacs in-aimsithe sa PDF.\nAr mhaith leat OCR a dhéanamh chun {0} a chumasú?",
        'ocr_perform': "Déan OCR",
        'ocr_later': "Níos déanaí",
        'ocr_starting': "OCR ráthaithe á thionscnamh...",
        'ocr_success_voice': "OCR rathúil. Tá an PDF in-aimsithe anois.",
        'ocr_partial_success': "Rinneadh OCR, ach bhí fadhbanna ann le hathsholáthar.\n\nSábháladh an leagan in-aimsithe seo:\n{0}\n\nEarráid: {1}",
        'ocr_partial_title': "OCR páirteach",
        'ocr_partial_voice': "OCR déanta, ach theip ar athsholáthar.",
        'original_file': "Comhad bunaidh:",
        'old_size': "Seanmhéid:    {0} bytes",
        'new_size': "Méid nua: {0} bytes",
        'size_change': "Athrú: {0}{1} bytes",
        'backup_created_file': "Cúltaca cruthaithe:\n{0}",
        'backup_not_created': "Cúltaca gan chruthú (socrú díchumasaithe)",
        'page_header': "=== Leathanach {0} ===\n{1}\n",
        'scanned_page_header': "=== Leathanach {0} (scanta) ===\n[Níl ach téacs scanta ar an leathanach seo]\n[Déan OCR de láimh]\n",
        'scanned_warning': "⚠️ TÉACS SCANTA - OCR AG TEASTÁIL",
        'guaranteed_title': "PDF In-aimsithe Cruthaithe",
        'guaranteed_message': "<b>Cruthaíodh leagan ráthaithe in-aimsithe!</b>\n\nÓs rud é gur theip ar OCR uathoibríoch, cruthaíodh PDF in-aimsithe malartach:\n\n{0}\n\n<b>Tá an comhad seo ann:</b>\n• Téacs eastósctha (má bhí sé ann)\n• Nótaí do leathanaigh scanta\n• In-aimsithe go hiomlán",
        'guaranteed_voice': "PDF ráthaithe in-aimsithe cruthaithe.",
        'instruction_title': "TREORACHA OCR",
        'instruction_file': "Comhad bunaidh: {0}",
        'instruction_text': "Theip ar OCR uathoibríoch.\nDéan OCR de láimh:\n\n1. LE OCRmyPDF (orduithe):\n   ocrmypdf --force-ocr \"[COMHAD]\" \"aschur.pdf\"\n\n2. LE ADOBE ACROBAT (macOS/Windows):\n   • Oscail PDF in Acrobat\n   • Uirlisí > Cuir PDF in Eagar\n   • Roghnaigh 'Aithint Téacs'\n\n3. LE PREVIEW (macOS):\n   • Oscail PDF in Preview\n   • Comhad > Easportáil...\n   • Scagaire Quartz: 'Reduce File Size'\n   • Cumasaigh 'Déan OCR'\n\n4. SEIRBHÍSÍ OCR AR LÍNE:\n   • smallpdf.com/ga/ocr-pdf\n   • ilovepdf.com/ga/ocr-pdf\n   • adobe.com/ga/acrobat/online/pdf-to-word.html",
        'instruction_created': "Treoir OCR cruthaithe",
        'instruction_created_message': "Cruthaíodh treoir mhionsonraithe:\n\n{0}\n\nLean na céimeanna le haghaidh OCR láimhe.",
        'instruction_created_voice': "Treoir OCR cruthaithe.",
        'ocr_impossible': "OCR dodhéanta",
        'ocr_impossible_message': "Níorbh fhéidir OCR a dhéanamh.\n\nPróiseáil '{0}' de láimh le bogearraí OCR.",
        'ocr_impossible_voice': "OCR dodhéanta. Próiseáil de láimh.",
        'emergency_title': "OCR Éigeandála",
        'emergency_message': "Cruthaíodh PDF éigeandála:\n\n{0}\n\nPróiseáil an comhad seo de láimh le OCR.",
        'emergency_voice': "PDF éigeandála cruthaithe. Déan OCR de láimh.",
        'critical_error': "Earráid Chriticiúil",
        'critical_error_message': "Níorbh fhéidir OCR a thosú.\n\nAtosaigh an clár agus seiceáil suiteáil OCR.",
        'critical_error_voice': "Earráid OCR chriticiúil",
        'ocr_question_html': "<p>Níl téacs in-aimsithe sa PDF.<p>Ar mhaith leat OCR a dhéanamh chun <b>{0}</b> a chumasú?</p>",
        'ocr_question_voice': "OCR ag teastáil. Níl téacs in-aimsithe sa PDF. Ar mhaith leat OCR a dhéanamh chun {0} a chumasú?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "gan PDF luchtaithe",
        'no_pdf_message': "Níl aon PDF luchtaithe",
        'pdf_not_found': "Comhad PDF gan aimsiú",
        'file_size': "Méid Comhaid",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Cúltaca cruthaithe",
        'backup_disabled': "Cúltaca díchumasaithe",
        'backup_activated': "Cruthú cúltaca cumasaithe",
        'backup_deactivated': "Cruthú cúltaca díchumasaithe",
        'backup_status': "Cúltaca: {0}",
        'backup_on': "✔ cumasaithe",
        'backup_off': "✘ díchumasaithe",
        'close_pdf': "Ag dúnadh PDF: {0}",
        'pdf_not_found_format': "Comhad PDF gan aimsiú: {0}",
        'error_pdf_load_format': "Earráid agus PDF á luchtú: {0}",
        'load_failed_format': "Luchtú theip:\n{0}",
        'decrypted_suffix': "(díchriptithe)",
        'decryption_failed': "Theip ar dhíchriptiú.",
        'decryption_error': "Earráid agus díchriptiú ar siúl",
        'decryption_success': "Díchriptiú rathúil",
        'decryption_success_message': "Díchriptíodh PDF agus sábháladh é anseo:\n\n{0}",
        'decryption_success_voice': "Díchriptíodh PDF agus sábháladh é.",
        'password_remove_error': "Earráid agus pasfhocal á bhaint",
        'save_unencrypted': "Sábháil PDF gan chriptiú",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Sábháil Mar...",
        'save_copy': "Sábháil Cóip",
        'save_success': "PDF sábháilte anseo: {0}",
        'save_encrypted': "PDF cosanta sábháilte anseo: {0}",
        'save_error': "Níorbh fhéidir PDF a shábháil",
        'encryption_question': "Ar mhaith leat an PDF a chosaint le pasfhocal?",
        'encryption_yes': "Tá",
        'encryption_no': "Níl",
        'encryption_cancel': "Cealaigh",
        'save_cancel': "Sábháil ar ceal",
        'save_encrypted_voice': "Comhad criptithe agus sábháilte.",
        'save_success_voice': "Sábháladh an comhad PDF gan chriptiú.",
        'save_error_format': "Níorbh fhéidir PDF a shábháil:\n{0}",
        'export_pages_success': "Easpórtáil Pages rathúil",
        'export_pages_error': "Theip ar easpórtáil Pages",
        'export_pages_error_format': "Theip ar easpórtáil Pages: {0}",
        'export_word_success': "Easpórtáil Word rathúil",
        'export_word_error': "Theip ar easpórtáil Word",
        'export_word_error_format': "Theip ar easpórtáil Word: {0}",
        'export_text_success': "Easpórtáil Téacs rathúil",
        'export_text_error': "Theip ar easpórtáil Téacs",
        'export_text_error_format': "Theip ar easpórtáil Téacs: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Pasfhocal ag teastáil",
        'password_enter': "Cuir isteach an pasfhocal",
        'password_confirm': "Deimhnigh pasfhocal",
        'password_new': "Pasfhocal nua",
        'password_current': "Pasfhocal reatha",
        'password_save': "Sábháil pasfhocal (criptithe)",
        'password_saved': "✓ Pasfhocal don chomhad seo sábháilte",
        'password_wrong': "Pasfhocal mícheart",
        'password_mismatch': "Ní hionann na pasfhocail",
        'password_too_short': "Pasfhocal ró-ghearr",
        'password_min_length': "Caithfidh an pasfhocal a bheith 4 charachtar ar a laghad",
        'password_strength': "Láidreacht Pasfhocail",
        'password_strength_very_weak': "An-lag",
        'password_strength_weak': "Lag",
        'password_strength_medium': "Meánach",
        'password_strength_strong': "Láidir",
        'password_strength_very_strong': "An-láidir",
        'password_char_count': "({0} charachtar)",
        'password_match': "✓ Meaitseáil",
        'password_no_match': "✗ Ní hionann na pasfhocail",
        'password_show': "Taispeáin",
        'password_hide': "Folaigh",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Bainistíocht Pasfhocal",
        'password_table_filename': "Ainm Comhaid",
        'password_table_password': "Pasfhocal",
        'password_count': "{0} pasfhocal sábháilte",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Gan pasfhocail sábháilte",
        'password_copied': "{0} pasfhocal cóipeáilte",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "An bhfuil tú cinnte gur mhaith leat pasfhocal '{0}' a scriosadh?",
        'password_delete_multiple': "An bhfuil tú cinnte gur mhaith leat na {0} pasfhocal roghnaithe a scriosadh?",
        'password_delete_all_confirm': "An bhfuil tú cinnte gur mhaith leat gach ceann de na {0} pasfhocal sábháilte a scriosadh?",
        'password_deleted': "{0} pasfhocal scriosta",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Scriosadh gach pasfhocal",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Gineadóir Pasfhocal",
        'generator_generated': "Pasfhocal ginte:",
        'generator_regenerate': "Gin arís",
        'generator_copy': "Cóipeáil",
        'generator_use': "Úsáid",
        'generator_settings': "Socruithe",
        'generator_length': "Fad:",
        'generator_group_every': "Deighilteoir gach",
        'generator_group_chars': "charachtar.    Deighilteoir:",
        'generator_uppercase': "Ceannlitreacha (A-Z)",
        'generator_lowercase': "Litreacha beaga (a-z)",
        'generator_digits': "Uimhreacha (0-9)",
        'generator_symbols': "Siombailí (!@#$%^&*)",
        'generator_exclude': "Eisiata:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Príomhphasfhocal ag teastáil",
        'master_password_setup': "Socraigh Príomhphasfhocal",
        'master_password_change': "Athraigh Príomhphasfhocal",
        'master_password_enter': "Cuir isteach do Phríomhphasfhocal",
        'master_password_choose': "Roghnaigh Príomhphasfhocal láidir (8 gcarachtar ar a laghad)",
        'master_password_new': "Cuir isteach do Phríomhphasfhocal nua",
        'master_password_confirm': "Deimhnigh pasfhocal",
        'master_password_authenticate': "Fíordheimhnigh",
        'master_password_success': "Príomhphasfhocal socraithe go rathúil.",
        'master_password_changed': "Príomhphasfhocal athraithe go rathúil.",
        'master_password_removed': "Scriosadh Príomhphasfhocal agus gach pasfhocal.",
        'master_password_remove': "Bain Príomhphasfhocal",
        'master_password_remove_confirm': "An bhfuil tú CINNTE gur mhaith leat GACH pasfhocal a scriosadh?\n\nNÍ FÉIDIR an gníomh seo a chur ar ceal!",
        'master_password_export_before': "Ar mhaith leat cúltaca a easpórtáil roimh scriosadh?",
        'master_password_export_delete': "Easpórtáil & scrios",
        'master_password_delete_now': "Scrios anois",
        'master_password_for_signatures': "Chun síniú a úsáid, caithfidh tú Príomhphasfhocal a shocrú.\n\nAr mhaith leat Príomhphasfhocal a shocrú anois?",
        'master_password_for_private': "Chun blúirí téacs príobháideacha a úsáid, caithfidh tú Príomhphasfhocal a shocrú.\n\nAr mhaith leat Príomhphasfhocal a shocrú anois?",
        'master_password_info': """
            <b>🔐 GAN PRÍOMHPHASFHOCAL:</b><br>
            • Ní féidir pasfhocail a thaispeáint, a chóipeáil ná a easpórtáil<br>
            • Is féidir pasfhocail a scriosadh i gcónaí (fiú gan Príomhphasfhocal)<br><br>

            <b>🔐 LE PRÍOMHPHASFHOCAL:</b><br>
            • Gach feidhm ar fáil tar éis fíordheimhnithe<br>
            • Criptítear pasfhocail leis an bPríomhphasfhocal<br>
            • Íosfhad: 8 gcarachtar<br>
            • Stóráil shábháilte le haischur SHA-256<br><br>

            <b>TÁBHACHTACH:</b><br>
            • Má chailleann tú an Príomhphasfhocal, ní féidir pasfhocail a aisghabháil<br>
            • Nuair a bhaintear an Príomhphasfhocal, scriostar GACH pasfhocal<br>
            • Rogha easpórtála ar fáil roimh scriosadh<br>
            • Is féidir an Príomhphasfhocal a athrú am ar bith
        """,
        'signature_auth_disabled': "Díchumasaigh ceist pasfhocail do shínithe",
        'template_auth_disabled': "Díchumasaigh ceist pasfhocail do bhlúirí téacs príobháideacha",
        'master_password_for_signatures_settings': "Chun síniú a úsáid, caithfidh tú Príomhphasfhocal a shocrú.\n\nTéigh go Socruithe - Bainistíocht Pasfhocal",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Cosain PDF",
        'protect_info': "Cosnófar an comhad '{0}' le pasfhocal.",
        'protect_instruction': "Cuir isteach an pasfhocal atá uait faoi dhó chun an doiciméad a chosaint, nó úsáid an gineadóir pasfhocal ar dheis an réimse ionchuir.",
        'protect_success': "Cosnaíodh PDF go rathúil agus sábháladh é anseo:\n{0}\n\nPasfhocal: {1}\n\nAr mhaith leat an PDF cosanta a oscailt anois?",
        'protect_open': "Tá",
        'protect_skip': "Níl",
        'protect_error': "Earráid agus PDF á chosaint",
        'protect_open_title': "Oscail PDF cosanta",
        'protect_question': "Críochnaithe. Ar mhaith leat an PDF cosanta a oscailt anois? Tá nó Níl?",
        'password_cancel': "Dialóg pasfhocail ar ceal",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Scrios Leathanaigh",
        'pages_extract': "Bain Leathanaigh",
        'pages_insert': "Ionsáigh Leathanaigh",
        'pages_move': "Bog Leathanaigh",
        'pages_delete_options': "Roghanna Scriosta",
        'pages_delete_empty': "Scrios gach leathanach folamh",
        'pages_delete_current': "Scrios an leathanach reatha",
        'pages_delete_range': "Scrios raon leathanach",
        'pages_extract_options': "Roghanna Bainte",
        'pages_extract_current': "Bain an leathanach reatha",
        'pages_extract_range': "Bain raon leathanach",
        'pages_insert_position': "Ionsáigh ag",
        'pages_insert_before': "Ionsáigh roimh leathanach:",
        'pages_insert_select': "Roghnaigh PDF",
        'pages_insert_none': "Gan PDF roghnaithe",
        'pages_move_source': "Leathanaigh le bogadh",
        'pages_move_from': "Ó leathanach:",
        'pages_move_to': "Go leathanach:",
        'pages_move_target': "Suíomh sprice",
        'pages_move_before': "Bog roimh leathanach:",
        'pages_move_hint': "Nóta: leathanach 1 = tús, {0} = deireadh",
        'pages_range_invalid': "Caithfidh an chéad leathanach a bheith níos lú ná nó cothrom leis an leathanach deiridh.",
        'pages_position_invalid': "Ní féidir an sprioc a bheith laistigh den raon atá á bhogadh.",
        'pages_no_pdf_selected': "Níl aon PDF roghnaithe.",
        'pages_deleted': "Scriosadh {0} leathanach.",
        'pages_extracted': "Bainte: {0}\nSábháladh anseo: {1}\nMéid comhaid: {2:.1f} KB",
        'pages_inserted': "{0} leathanach curtha isteach",
        'pages_moved': "Bogadh {0} leathanach.",
        'pages_deleted_none': "Níor scriosadh aon leathanach.",
        'pages_delete_progress': "Leathanaigh á scriosadh...",
        'pages_deleted_with_backup': "Scriosadh {0} leathanach.\n\nCúltaca: {1}",
        'pages_deleted_voice': "Cruthaíodh cúltaca agus scriosadh {0} leathanach.",
        'info': "Nóta",
        'error_dialog_creation': "Níorbh fhéidir dialóg a chruthú",
        'extract_page_single': "Bain leathanach {0}",
        'extract_page_range': "Bain leathanaigh {0}-{1}",
        'extract_success_voice': "Leathanaigh bainte go rathúil",
        'extract_error_format': "Earráid agus leathanaigh á mbaint: {0}",
        'pages_inserted_voice': "Cuireadh {0} leathanach isteach.",
        'insert_error_format': "Earráid agus leathanaigh á n-ionsá: {0}",
        'pages_move_progress': "Leathanaigh á mbogadh...",
        'pages_moved_with_backup': "Bogadh {0} leathanach.\n\nCúltaca: {1}",
        'move_success_title': "Bogadh Rathúil",
        'pages_moved_voice': "Bogadh {0} leathanach go rathúil",
        'mark_removed': "Marcáil bainte de leathanach {0}",
        'mark_empty': "Leathanach {0} marcáilte mar fholamh",
        'mark_export_removed': "Marcáil easpórtála bainte de leathanach {0}",
        'mark_export': "Leathanach {0} marcáilte le haghaidh easpórtála",
        'no_empty_pages': "Gan aon leathanach folamh marcáilte le scriosadh",
        'delete_empty_confirm': "Ar mhaith leat gach ceann de na {0} leathanach folamh marcáilte a scriosadh?",
        'delete_empty_confirm_voice': "Anois scrios gach ceann de na {0} leathanach folamh marcáilte? Tá nó Níl.",
        'empty_pages_deleted': "{0} leathanach folamh scriosta",
        'no_export_pages': "Gan aon leathanach marcáilte le haghaidh easpórtála",
        'overwrite_title': "Forscríobh Comhad Reatha",
        'overwrite_question': "Tá an comhad\n\n{0}\n\nann cheana.\nAr mhaith leat é a fhorscríobh?",
        'overwrite_voice': "Forscríobh an comhad atá ann cheana? Tá nó Níl.",
        'page_skipped': "Scipeáladh leathanach {0}",
        'export_complete': "Easpórtáil críochnaithe.",
        'export_complete_voice': "Tá an easpórtáil críochnaithe.",
        'no_pages_exported': "Níor easpórtáladh aon leathanach",
        'export_cancelled': "Easpórtáil ar ceal",
        'pages_exported': "{0} leathanach easpórtáilte go {1}",
        'export_page_title': "Easpórtáil Leathanach",
        'page_exported': "Leathanach {0} easpórtáilte go {1}",
        'export_error': "Earráid le linn easpórtála",
        'export_marked_title': "Easpórtáil Leathanaigh Mharcáilte",
        'rotate_all_title': "rothlaigh gach leathanach",
        'rotate_all_question': "Ar mhaith leat gach leathanach a rothlú 90 céim ar dheis?",
        'rotate_all_voice': "Ar mhaith leat gach leathanach a rothlú 90 céim ar dheis? Tá nó Níl?",
        'all_pages_rotated': "Gach leathanach rothlaithe",
        'page_rotated': "Leathanach {0} rothlaithe",
        'rotate_error': "Níorbh fhéidir an leathanach a rothlú",
        'delete_page_confirm': "Ar mhaith leat leathanach {0} a scriosadh?",
        'delete_page_confirm_voice': "An bhfuil tú cinnte gur mhaith leat leathanach {0} a scriosadh? Tá nó Níl.",
        'page_deleted': "Leathanach {0} scriosta",
        'delete_error': "Níorbh fhéidir an leathanach a scriosadh",
        'pages_deleted_voice': "{0} leathanach scriosta",
        'pages_exported_split': "Easpórtáladh {0} leathanach go rathúil.",
        'pages_skipped': "Scipeáladh {0} leathanach.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Bain Leathanaigh (leathnaithe)",
        'pdf_splitter_title': "Deighilteoir & Bainteoir PDF",
        'pdf_splitter_load': " Roghnaigh comhad PDF",
        'pdf_splitter_info': "Roghnaigh rogha do dhoiciméid PDF",
        'pdf_splitter_basic': "Bunoibríochtaí",
        'pdf_splitter_single': "Deighilt ina leathanaigh aonair",
        'pdf_splitter_range': "Bain leathanaigh:",
        'pdf_splitter_range_placeholder': "m.sh. 1-3,5,7-9",
        'pdf_splitter_clean': "Oibríochtaí Glanta",
        'pdf_splitter_remove_empty': "Bain gach leathanach folamh",
        'pdf_splitter_remove': "Scrios raon leathanach:",
        'pdf_splitter_remove_placeholder': "m.sh. 2,4-6",
        'pdf_splitter_process': "Próiseáil PDF",
        'pdf_splitter_loaded': "PDF luchtaithe. Roghnaigh rogha",
        'pdf_read_error': "Níorbh fhéidir an PDF a léamh",
        'pages': "Leathanaigh",
        'pages_created': "Leathanaigh cruthaithe",
        'range_empty': "Iontráil raon leathanach",
        'range_invalid': "Raon leathanach neamhbhailí",
        'range_created': "Cruthaíodh PDF nua leis na leathanaigh roghnaithe:\n{0}",
        'empty_removed': "{0} leathanach folamh bainte.\nAschur: {1}",
        'remove_empty': "Iontráil leathanaigh le baint",
        'remove_invalid': "Leathanaigh le baint neamhbhailí",
        'remove_done': "Cruthaíodh PDF glanta:\n{0}",
        'open_folder': "Oscail Fillteán",
        'show_in_finder': "Taispeáin san Aimsitheoir",
        'pdf_splitter_no_pdf': "Luchtaigh comhad PDF ar dtús.",
        'process_error': "Earráid agus PDF á phróiseáil",
        'pages_created_voice': "Cruthaíodh {0} leathanach",
        'range_created_voice': "Cruthaíodh PDF leis na leathanaigh roghnaithe",
        'empty_removed_voice': "Baineadh {0} leathanach folamh",
        'remove_done_voice': "Cruthaíodh PDF glanta",
        'pdf_splitter_split_groups': "Gach grúpa leanúnach ina chomhad ar leith",
        'range_created_single': "Cruthaíodh PDF nua:\n{0}",
        'range_created_multiple': "Cruthaíodh {0} comhad PDF.",
        'range_created_voice_single': "Cruthaíodh aon PDF amháin leis na leathanaigh roghnaithe",
        'range_created_voice_multiple': "Cruthaíodh {0} comhad PDF",
        'empty_removed_none_left': "Gan aon leathanach fágtha",
        'empty_removed_all_empty': "Aithníodh gach leathanach mar fholamh agus bhainfí iad. Níor cruthaíodh aon chomhad.",
        'preview_single': "Réamhamharc: {0}",
        'preview_enter_range': "Iontráil raon leathanach.",
        'preview_invalid_range': "Raon leathanach neamhbhailí.",
        'preview_file': "Réamhamharc: {0}",
        'preview_files': "Réamhamharc: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Priontáil á thionscnamh",
        'print_sent': "Tasc priontála seolta",
        'print_now': "Priontáil anois",
        'print_error': "Earráid le priontáil láithreach",
        'print_limited': "Feidhm priontála teoranta ar an gcóras seo",
        'print_error_format': "Earráid le priontáil láithreach: {0}",
        'warning': "Rabhadh",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Athraigh go Mód Geal",
        'mode_switch_to_dark': "Athraigh go Mód Dorcha",
        'mode_dark_activated': "Mód Dorcha gníomhachtaithe",
        'mode_light_activated': "Mód Geal gníomhachtaithe",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Amharc Iomlán",
        'zoom_two_pages': "Dá leathanach taobh le taobh",
        'zoom_overview': "Mód Forbhreathnaithe",
        'zoom_cannot_during_search': "Ní féidir zúmáil le linn cuardaigh",
        'zoom_exit_first': "Fág an zúmáil ar dtús",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Tarraing is scaoil cumasaithe",
        'drag_disabled': "Tarraing is scaoil díchumasaithe",
        'drag_page_grab': "Leathanach {0} greim",
        'drag_page_dropped': "Leathanach {0} curtha isteach ag suíomh {1}",
        'drag_position_invalid': "Suíomh neamhbhailí",
        'drag_same_position': "Fanann leathanach {0} ag suíomh {0}",
        'drag_error': "Earráid agus leathanach á bhogadh",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Ionchur téacs le formáidiú fairsing agus bainistíocht blúirí téacs",
        'text_templates': "Blúirí téacs ar fáil:",
        'text_name': "Ainm",
        'text_preview': "Réamhamharc téacs",
        'text_enter': "Téacs:",
        'text_font_size': "Méid Cló:",
        'text_formatting': "Formáidiú:",
        'text_bold': "Trom",
        'text_italic': "Iodálach",
        'text_underline': "Folínithe",
        'text_alignment': "Ailíniú:",
        'text_left': "Ar Chlé",
        'text_center': "Lárnaithe",
        'text_right': "Ar Dheis",
        'text_color': "Dath Téacs:",
        'text_opacity': "Teimhneacht:",
        'text_word_wrap': "Timfhilleadh Focal:",
        'text_auto': "Uathoibríoch",
        'text_page_width_95': "Leithead leathanaigh (95 %)",
        'text_page_width_85': "An-leathan (85 %)",
        'text_page_width_75': "Níos leithne (75 %)",
        'text_page_width_60': "Leathan (60 %)",
        'text_page_width_50': "Meánach (50 %)",
        'text_page_width_30': "Cúng (30 %)",
        'text_page_width_20': "Níos cúinge (20 %)",
        'text_page_width_10': "An-chúng (10 %)",
        'text_no_wrap': "Gan timfhilleadh",
        'text_private': "Blúire téacs príobháideach (fíordheimhniú ag teastáil)",
        'text_preview_label': "Réamhamharc:",
        'text_preview_placeholder': "Taispeánfar réamhamharc an téacs anseo...",
        'text_no_text': "(Gan Téacs)",
        'text_save_template': "💾 Sábháil mar bhlúire",
        'text_delete_template': "🗑 Scrios an blúire téacs roghnaithe",
        'text_show_private': "Taispeáin príobháideacha",
        'text_hide_private': "Folaigh príobháideacha",
        'text_use': "✅ Úsáid téacs",
        'text_saved': "Blúire téacs sábháilte mar:\n{0}",
        'text_saved_voice': "Blúire téacs sábháilte",
        'text_deleted': "Blúire téacs scriosta",
        'text_no_text_to_save': "Gan aon téacs le sábháil.",
        'text_no_templates': "Gan aon bhlúire téacs aimsithe",
        'text_private_master_required': "Ní féidir blúirí príobháideacha a úsáid ach amháin má tá Príomhphasfhocal socraithe.\n\nAr mhaith leat Príomhphasfhocal a shocrú anois?",
        'text_filename': "Ainm comhaid don bhlúire téacs (gan 'Text_' ná '.txt'):",
        'text_filename_hint': "Sampla: 'Fón BaileOifig' sábhálfar mar 'Text_Fón BaileOifig.txt'",
        'text_save_hint': "Sábhálfar an blúire téacs go huathoibríoch leis an bhformáidiú.",
        'text_guide_title': "Ionchur Téacs - Treoir",
        'text_delete_confirm': "An bhfuil tú cinnte gur mhaith leat an blúire téacs a scriosadh?\n\nComhad: {0}\nTéacs: {1}...",
        'text_make_public': "Marcáil mar phoiblí",
        'text_make_private': "Marcáil mar phríobháideach",
        'text_privacy_changed': "Stádas príobháideachta athraithe",
        'text_private_always': "Príobháideach le feiceáil i gcónaí (socrú)",
        'text_mode_required': "Gníomhachtaigh mód téacs ar dtús",
        'text_continue_editing': "Lean ar aghaidh ag eagarthóireacht - cúrsóir ag deireadh an téacs",
        'text_no_input': "Gan aon téacs iontráilte - téacs caite",
        'save_dialog_question': "Conas is mian leat dul ar aghaidh?",
        'text_save_question': "Sábháil gach téacs agus cros, coigeartaigh, lean ar aghaidh ag eagarthóireacht nó caith?",
        'copy_cross': "Cros cóipeáilte",
        'paste_cross': "Cros greamaithe",
        'paste_text': "Téacs greamaithe",
        'cross_discarded': "Cros caite",
        'all_discarded': "Gach rud caite",
        'text_discarded': "Téacs caite",
        'no_texts_to_save': "Gan aon téacs le sábháil",
        'no_valid_texts': "Gan aon téacs bailí le sábháil",
        'text_word_singular': "téacs",
        'text_word_plural': "téacs",
        'cross_word_singular': "cros",
        'cross_word_plural': "cros",
        'texts_saved_title': "Téacsanna Sábháilte",
        'texts_crosses_saved': "Cuireadh {0} {1} agus {2} {3} isteach sa PDF.\n\nAthlódáladh an PDF...",
        'texts_crosses_saved_voice': "{0} {1} agus {2} {3} sábháilte.",
        'texts_saved': "Cuireadh {0} {1} isteach sa PDF.\n\nAthlódáladh an PDF...",
        'texts_saved_voice': "{0} {1} sábháilte.",
        'crosses_saved': "Cuireadh {0} {1} isteach sa PDF.\n\nAthlódáladh an PDF...",
        'crosses_saved_voice': "{0} {1} sábháilte.",
        'elements_saved': "Cuireadh {0} eilimint isteach sa PDF.\n\nAthlódáladh an PDF...",
        'elements_saved_voice': "{0} eilimint sábháilte.",
        'text_window_load_error': "Níorbh fhéidir fuinneog téacs a luchtú",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Ionchur Téacs agus Blúirí Téacs – Treoir Mhionsonraithe**

        **1. Téacs a chur isteach agus a chur in eagar**
        - Cliceáil deaschlice ag an áit atá uait sa doiciméad agus roghnaigh "Ionsáigh téacs".
        - Osclófar dialóg inar féidir leat do théacs a iontráil agus a fhormáidiú:
        • Méid cló, Trom, Iodálach, Folíne
        • Dath téacs (roghnach)
        • Trédhearcacht (teimhneacht) le sleamhnán
        • Timfhilleadh focal (leithead éagsúil, m.sh. leithead leathanaigh, cúng, gan timfhilleadh)
        - Tar éis deimhnithe, feicfear an téacs ag an áit a chliceáil tú. Is féidir é a bhogadh le luch nó le saigheadeochracha.
        - Cliceáil faoi dhó ar an téacs chun mód eagarthóireachta a oscailt; scoir le ESC.

        **2. Blúirí Téacs a bhainistiú**
        - Ar thaobh clé na dialóige tá liosta de na blúirí téacs go léir atá sábháilte.
        - **Blúire a shábháil:** Iontráil do théacs, formáidigh é agus cliceáil "💾 Sábháil mar bhlúire". Tabhair ainm comhaid (gan iarmhír).
        - **Blúire a luchtú:** Cliceáil ar an ainm atá uait sa liosta. Cóipeálfar an téacs agus an fhormáidiú agus is féidir iad a choigeartú más gá.
        - **Scriosadh:** Cliceáil deaschlice ar bhlúire agus is féidir é a scriosadh nó a stádas príobháideachta a athrú.

        **3. Blúirí Téacs Príobháideacha (Príomhphasfhocal)**
        - Má tá Príomhphasfhocal socraithe agat (faoi Socruithe → Bainistíocht Pasfhocal), is féidir leat blúirí a mharcáil mar "phríobháideach".
        - Cumasaigh an bosca "Blúire téacs príobháideach" sa dialóg sula sábhálann tú.
        - Ní thaispeánfar blúirí príobháideacha sa liosta ach amháin má tá tú fíordheimhnithe leis an bPríomhphasfhocal uair amháin in aghaidh an tseisiúin (fíordheimhniú trí dheilbhín an ghlasa nó ag an gcéad rochtain).
        - Ar an mbealach seo is féidir leat blúirí téacs íogaire a chosaint ó rochtain neamhúdaraithe.

        **4. Crosa a chur isteach**
        - Tríd an roghchlár comhthéacs is féidir leat cros ghrafach (m.sh. le haghaidh bosca seiceála) a chur isteach.
        - Is féidir méid, tiús líne agus dath na gcros a choigeartú go domhanda sna socruithe (roghchlár "Socruithe" → "Socruithe Cros").
        - Cliceáil deaschlice ar chros atá ann cheana chun é a chur in oiriúint go haonarach.

        **5. Comhghníomhartha**
        - Má tá il-téacsanna nó crosa curtha ar leathanach agat, is féidir leat iad go léir a shábháil nó a chaitheamh le chéile trí chliceáil deaschlice i mód téacs.
        - Nuair a shábhálann tú, leabaitear na heilimintí go léir sa PDF agus fanann siad mar ghrafaic veicteora.

        **6. Aicearraí méarchláir i mód téacs**
        - Saigheadeochracha: eilimint a bhogadh
        - Ctrl+Saigheadeochracha: céimeanna níos mó
        - Iontráil: dialóg sábhála a oscailt (sábháil uile / coigeartaigh / caith)
        - ESC: an eilimint reatha a chaitheamh
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Ionchur Téacs agus Blúirí Téacs – Treoir Mhionsonraithe</strong></p>

        <p><strong>1. Téacs a chur isteach agus a chur in eagar</strong></p>
        <ul>
        <li>Cliceáil deaschlice ag an áit atá uait sa doiciméad agus roghnaigh "Ionsáigh téacs".</li>
        <li>Osclófar dialóg inar féidir leat do théacs a iontráil agus a fhormáidiú:<br/>
        • Méid cló, Trom, Iodálach, Folíne<br/>
        • Dath téacs (roghnach)<br/>
        • Trédhearcacht (teimhneacht) le sleamhnán<br/>
        • Timfhilleadh focal (leithead éagsúil, m.sh. leithead leathanaigh, cúng, gan timfhilleadh)</li>
        <li>Tar éis deimhnithe, feicfear an téacs ag an áit a chliceáil tú. Is féidir é a bhogadh le luch nó le saigheadeochracha.</li>
        <li>Cliceáil faoi dhó ar an téacs chun mód eagarthóireachta a oscailt; scoir le ESC.</li>
        </ul>

        <p><strong>2. Blúirí Téacs a bhainistiú</strong></p>
        <ul>
        <li>Ar thaobh clé na dialóige tá liosta de na blúirí téacs go léir atá sábháilte.</li>
        <li><strong>Blúire a shábháil:</strong> Iontráil do théacs, formáidigh é agus cliceáil "💾 Sábháil mar bhlúire". Tabhair ainm comhaid (gan iarmhír).</li>
        <li><strong>Blúire a luchtú:</strong> Cliceáil ar an ainm atá uait sa liosta. Cóipeálfar an téacs agus an fhormáidiú agus is féidir iad a choigeartú más gá.</li>
        <li><strong>Scriosadh:</strong> Cliceáil deaschlice ar bhlúire agus is féidir é a scriosadh nó a stádas príobháideachta a athrú.</li>
        </ul>

        <p><strong>3. Blúirí Téacs Príobháideacha (Príomhphasfhocal)</strong></p>
        <ul>
        <li>Má tá Príomhphasfhocal socraithe agat (faoi Socruithe → Bainistíocht Pasfhocal), is féidir leat blúirí a mharcáil mar "phríobháideach".</li>
        <li>Cumasaigh an bosca "Blúire téacs príobháideach" sa dialóg sula sábhálann tú.</li>
        <li>Ní thaispeánfar blúirí príobháideacha sa liosta ach amháin má tá tú fíordheimhnithe leis an bPríomhphasfhocal uair amháin in aghaidh an tseisiúin (fíordheimhniú trí dheilbhín an ghlasa nó ag an gcéad rochtain).</li>
        <li>Ar an mbealach seo is féidir leat blúirí téacs íogaire a chosaint ó rochtain neamhúdaraithe.</li>
        </ul>

        <p><strong>4. Crosa a chur isteach</strong></p>
        <ul>
        <li>Tríd an roghchlár comhthéacs is féidir leat cros ghrafach (m.sh. le haghaidh bosca seiceála) a chur isteach.</li>
        <li>Is féidir méid, tiús líne agus dath na gcros a choigeartú go domhanda sna socruithe (roghchlár "Socruithe" → "Socruithe Cros").</li>
        <li>Cliceáil deaschlice ar chros atá ann cheana chun é a chur in oiriúint go haonarach.</li>
        </ul>

        <p><strong>5. Comhghníomhartha</strong></p>
        <ul>
        <li>Má tá il-téacsanna nó crosa curtha ar leathanach agat, is féidir leat iad go léir a shábháil nó a chaitheamh le chéile trí chliceáil deaschlice i mód téacs.</li>
        <li>Nuair a shábhálann tú, leabaitear na heilimintí go léir sa PDF agus fanann siad mar ghrafaic veicteora.</li>
        </ul>

        <p><strong>6. Aicearraí méarchláir i mód téacs</strong></p>
        <ul>
        <li>Saigheadeochracha: eilimint a bhogadh</li>
        <li>Ctrl+Saigheadeochracha: céimeanna níos mó</li>
        <li>Iontráil: dialóg sábhála a oscailt (sábháil uile / coigeartaigh / caith)</li>
        <li>ESC: an eilimint reatha a chaitheamh</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Socruithe Cros",
        'cross_properties': "Airíonna Croise",
        'cross_size': "Méid (px):",
        'cross_line_width': "Tiús Líne:",
        'cross_color': "Dath:",
        'cross_choose_color': "Roghnaigh",
        'cross_fine_tuning': "Mionchoigeartú agus é á shábháil (picteilín)",
        'cross_offset_x': "Fritháireamh X:",
        'cross_offset_y': "Fritháireamh Y:",
        'cross_offset_x_tooltip': "Luachanna diúltacha aistríonn an chros ar chlé agus í á sábháil, luachanna dearfacha ar dheis",
        'cross_offset_y_tooltip': "Luachanna diúltacha aistríonn an chros suas agus í á sábháil, luachanna dearfacha síos",
        'cross_preview': "Réamhamharc",
        'cross_save': "Glac le socruithe",
        'cross_customized': "Cros coigeartaithe",
        'cross_settings_applied': "Socruithe cros sábháilte.\nMéid: {0}px, tiús líne: {1}px\n{2}",
        'cross_updated_count': "Nuashonraíodh {0} cros atá ann cheana.",
        'cross_no_crosses': "Gan aon chros atá ann cheana aimsithe.",
        'cross_settings_applied_all': "Socruithe cros glactha do gach ceann de na {0} cros",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Socruithe Sínithe",
        'signature_1': "Síniú 1",
        'signature_2': "Síniú 2",
        'signature_select': "Roghnaigh síniú",
        'signature_add': "➕ Cuir síniú nua leis...",
        'signature_size': "Méid do shínithe {0} (%):",
        'signature_common': "Socruithe Ginearálta",
        'signature_timestamp': "Cuir stampa ama leis go huathoibríoch",
        'signature_location': "Áit réamhshocraithe:",
        'signature_timestamp_size': "Méid cló stampa ama:",
        'signature_no_files': "-- Gan aon síniú aimsithe --",
        'signature_insert': "Ionsáigh síniú",
        'signature_insert_1': "Ionsáigh síniú 1",
        'signature_insert_2': "Ionsáigh síniú 2",
        'signature_customize': " Cuir síniú in oiriúint",
        'signature_discard': " Caith an síniú seo",
        'signature_save_all': " Sábháil gach síniú",
        'signature_discard_all': " Caith gach síniú",
        'signature_guide_title': "Sínithe - Treoir",
        'signature_guide': """
📝 Sínithe - Treoir Thapa

- Socraigh Príomhphasfhocal
- Cumraigh sínithe sa roghchlár Socruithe
  (méid, stampa ama ...)
- Ionsáigh le DECHCLICEÁIL ag an áit atá uait
  (Príomhphasfhocal ag teastáil uair amháin in aghaidh an tseisiúin)
- Bog an síniú le luch nó le saigheadeochracha
- Is féidir il-shínithe a chur isteach ceann i ndiaidh a chéile
- Is féidir gach síniú a chur in oiriúint go haonarach
- Caith síniú aonair
- Sábháil / caith gach síniú ag an am céanna
- Is féidir an roghchlár barra a úsáid freisin.
        """,
        'signature_placeholder': "Gan réamhamharc ar fáil",
        'signature_info': "Síniú {0}: {1}×{2} px ({3}% de {4}×{5})",
        'signature_info_placeholder': "Socruithe do shíniú {0}",
        'signature_inserted': "Síniú {0} curtha isteach ar leathanach {1}",
        'signature_deleted': "Síniú scriosta",
        'signature_copied': "Síniú cóipeáilte",
        'signature_pasted': "Síniú {0} greamaithe",
        'signature_saved': "Cuireadh {0} síniú isteach sa PDF.\n\nAthlódáladh an PDF...",
        'signature_saved_voice': "{0} síniú sábháilte",
        'mode_replace_signature_format': "Scoir den mhód agus ionsáigh síniú {0}",
        'mode_conflict_voice_signature': "Tá mód {0} gníomhach. Scoir agus ionsáigh síniú?",
        'signature_not_configured': "Síniú {0} gan chumrú",
        'signature_file_not_found': "Comhad sínithe gan aimsiú",
        'timestamp_format': "{0}, an {1}",
        'no_copied_signature': "Gan aon síniú cóipeáilte",
        'no_signatures_to_save': "Gan aon síniú le sábháil",
        'signature_save_question': "Sábháil gach síniú, coigeartaigh nó caith an ceann seo?",
        'signatures_saved_title': "Sínithe Sábháilte",
        'signatures_saved': "Cuireadh {0} síniú isteach sa PDF.\n\nAthlódáladh an PDF...",
        'signatures_saved_voice': "{0} síniú sábháilte.",
        'all_signatures_discarded': "Gach síniú caite",
        'signature_settings_saved': "Socruithe sínithe sábháilte",
        'signature_cancelled': "Síniú caite",
        'signature_active_title': "Síniú gníomhach",
        'signature_replace_question': "Tá síniú gníomhach cheana.\n\nAr mhaith leat an síniú reatha a athsholáthar?",
        'signature_replace': "Athsholáthar síniú",
        'signature_replace_voice': "Athsholáthar an síniú reatha nó cealaigh?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Socruithe Íomhánna",
        'image_common': "Socruithe Ginearálta Íomhánna",
        'image_keep_aspect': "Coinnigh cóimheas trasnáin agus íomhá á tarraingt",
        'image_default_size': "Méid réamhshocraithe (%):",
        'image_dark_invert': "Inbhéartaigh íomhánna i Mód Dorcha",
        'image_dark_invert_tooltip': "Cumasaithe: inbhéartaítear íomhánna le haghaidh infheictheachta níos fearr",
        'image_fine_tuning': "Mionchoigeartú (picteilín)",
        'image_offset_x': "Fritháireamh X:",
        'image_offset_y': "Fritháireamh Y:",
        'image_offset_x_tooltip': "Luachanna diúltacha aistríonn an íomhá ar chlé agus í á sábháil, dearfacha ar dheis",
        'image_offset_y_tooltip': "Luachanna diúltacha aistríonn an íomhá suas agus í á sábháil, dearfacha síos",
        'image_select': "Roghnaigh íomhá",
        'image_insert': "Ionsáigh íomhá",
        'image_customize': " Cuir íomhá in oiriúint",
        'image_aspect': " Coinnigh cóimheas trasnáin",
        'image_discard': " Caith an íomhá seo",
        'image_save_all': " Sábháil gach íomhá",
        'image_discard_all': " Caith gach íomhá",
        'image_filter': "Íomhánna",
        'image_guide_title': "Íomhánna a chur isteach - Treoir",
        'image_guide': """
📷 Íomhánna a chur isteach i PDF - Treoir Thapa:

1. Deaschliceáil ag an áit atá uait
2. "Ionsáigh íomhá" → roghnaigh íomhá
3. Suigh an íomhá: tarraing le luch
4. Coigeartaigh méid: tarraing ag na coirnéil/imeall
5. Coinnigh cóimheas trasnáin: [A] eochair
6. Tuilleadh coigeartuithe: deaschliceáil ar an íomhá

Leid: Is féidir na socruithe a choigeartú sa roghchlár comhthéacs.
        """,
        'image_inserted': "Íomhá {0} curtha isteach ar leathanach {1}",
        'image_deleted': "Íomhá caite",
        'image_copied': "Íomhá cóipeáilte",
        'image_pasted': "Íomhá greamaithe",
        'image_saved': "Cuireadh {0} íomhá isteach sa PDF.\n\nAthlódáladh an PDF...",
        'image_saved_voice': "{0} íomhá sábháilte",
        'image_aspect_on': "cumasaithe",
        'image_aspect_off': "díchumasaithe",
        'image_aspect_toggle': "Coinnigh cóimheas trasnáin {0}",
        'image_reset': "Íomhá athshocraithe go bunmhéid",
        'image_replaced': "Íomhá athsholáthraithe",
        'image_invalid': "Gan íomhá bhailí",
        'mode_replace_image': "Ionsáigh íomhá",
        'mode_conflict_voice_image': "Tá mód {0} gníomhach. Scoir agus ionsáigh íomhá?",
        'image_active_title': "Íomhá gníomhach",
        'image_replace_question': "Tá íomhá gníomhach cheana.\n\nAr mhaith leat an íomhá reatha a athsholáthar?",
        'image_replace': "Athsholáthar íomhá",
        'image_replace_voice': "Athsholáthar an íomhá reatha nó cealaigh?",
        'image_filter_all': "Íomhánna (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Gach comhad (*.*)",
        'no_copied_image': "Gan aon íomhá cóipeáilte",
        'image_discarded': "Íomhá caite",
        'image_save_question': "Sábháil gach íomhá, coigeartaigh nó caith an ceann seo?",
        'no_images_to_save': "Gan aon íomhá le sábháil",
        'no_valid_images': "Gan aon íomhá bhailí le sábháil",
        'images_saved_title': "Íomhánna Sábháilte",
        'images_saved': "Cuireadh {0} íomhá isteach sa PDF.\n\nAthlódáladh an PDF...",
        'images_saved_voice': "{0} íomhá sábháilte.",
        'all_images_discarded': "Gach íomhá caite",
        'image_settings_updated': "Socruithe íomhánna nuashonraithe",
        'image_replace_title': "Roghnaigh íomhá nua",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Socruithe Cruthanna",
        'form_basic': "Bunsocruithe",
        'form_default_type': "Cineál réamhshocraithe:",
        'form_rectangle': "Dronuilleog",
        'form_ellipse': "Éilips",
        'form_line': "Líne",
        'form_arrow': "Saighead",
        'form_line_width': "Tiús Líne:",
        'form_colors': "Dathanna",
        'form_line_color': "Dath Líne:",
        'form_fill_color': "Dath Líonta:",
        'form_choose_color': "Roghnaigh",
        'form_transparent': "Cúlra trédhearcach (líne amháin)",
        'form_filled': "líonta",
        'form_dark_mode': "Mód Dorcha",
        'form_dark_invert': "Inbhéartaigh dathanna i Mód Dorcha",
        'form_fine_tuning': "Mionchoigeartú (picteilín)",
        'form_offset_x': "Fritháireamh X:",
        'form_offset_y': "Fritháireamh Y:",
        'form_offset_x_tooltip': "Luachanna diúltacha aistríonn an cruth ar chlé agus é á shábháil, dearfacha ar dheis",
        'form_offset_y_tooltip': "Luachanna diúltacha aistríonn an cruth suas agus é á shábháil, dearfacha síos",
        'form_preview': "Réamhamharc",
        'form_insert': "Ionsáigh cruth",
        'form_rectangle_insert': "Dronuilleog",
        'form_ellipse_insert': "Éilips/ciorcal",
        'form_line_insert': "Líne (2 chliceáil)",
        'form_arrow_insert': "Saighead (2 chliceáil)",
        'form_customize': " Cuir cruth in oiriúint",
        'form_transparent_toggle': " Cúlra trédhearcach",
        'form_discard': " Caith an cruth seo",
        'form_save_all': " Sábháil gach cruth",
        'form_discard_all': " Caith gach cruth",
        'form_guide_title': "Cruthanna a chur isteach - Treoir",
        'form_guide': """
📐 Cruthanna a chur isteach i PDF - Treoir Thapa:

1. Roghnaigh cineál crutha (dronuilleog, éilips, líne, saighead)
2. Cliceáil ar an suíomh
   - Dronuilleog/éilips: cliceáil amháin chun cruth a chur
   - Líne/saighead: dhá chliceáil don phointe tosaigh agus don phointe deiridh
3. Suigh an cruth: tarraing le luch
4. Coigeartaigh méid: tarraing ag na coirnéil/imeall
5. Sábháil cruth: Iontráil
6. Caith cruth: ESC
7. Tuilleadh coigeartuithe: deaschliceáil ar an gcruth

Leid: Is féidir na socruithe a choigeartú sa roghchlár comhthéacs.
        """,
        'form_inserted': "{0} curtha isteach ar leathanach {1}",
        'form_deleted': "Cruth scriosta",
        'form_copied': "Cruth cóipeáilte",
        'form_pasted': "Cruth greamaithe",
        'form_saved': "Cuireadh {0} cruth isteach sa PDF.\n\nAthlódáladh an PDF...",
        'form_saved_voice': "{0} cruth sábháilte",
        'form_reset': "Cruth athshocraithe go bunmhéid",
        'form_transparent_on': "cumasaithe",
        'form_transparent_off': "díchumasaithe",
        'form_transparent_toggled': "Cúlra trédhearcach {0}",
        'form_line_cancel': "Líníocht líne ar ceal",
        'form_second_click': "Cliceáil an pointe deiridh don {0} anois",
        'mode_replace_form': "Ionsáigh cruth",
        'mode_conflict_voice_form': "Tá mód {0} gníomhach. Scoir agus ionsáigh cruth?",
        'form_settings_updated': "Socruithe cruthanna nuashonraithe",
        'form_unknown': "Cruth",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Cliceáil an pointe tosaigh",
        'form_line_guide_2': "2. Cliceáil an pointe deiridh",
        'form_line_guide_3': "Tarringítear an líne idir an dá phointe.",
        'form_line_status_1': "Ag fanacht le chéad chliceáil...",
        'form_line_status_2': "An chéad phointe socraithe: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Cliceáil an pointe deiridh anois...",
        'form_line_status_4': "An dá phointe socraithe.\nCliceáil 'Críochnaigh' le sábháil.",
        'form_line_reset': "Athshocraigh",
        'form_line_finish': "Críochnaigh",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Cóipeáil (Cmd+C)",
        'paste': "Greamaigh (Cmd+V)",
        'copied': "Cóipeáilte: {0}",
        'no_element_to_copy': "Gan aon eilimint roghnaithe le cóipeáil",
        'no_copied_data': "Gan aon sonraí cóipeáilte",
        'no_valid_position': "Gan aon suíomh bailí le greamú",
        'copy_text': "Téacs cóipeáilte",
        'copy_image': "Íomhá cóipeáilte",
        'copy_form': "Cruth cóipeáilte",
        'copy_signature': "Síniú cóipeáilte",
        'element_text': "Téacs",
        'element_image': "Íomhá",
        'element_form': "Cruth",
        'element_signature': "Síniú",
        'element_unknown': "Eilimint",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Coimhlint Mód",
        'mode_conflict_message': "Tá mód '{0}' gníomhach cheana.\n\nAr mhaith leat scor de agus {1}?",
        'mode_replace': "Scoir den mhód agus {0}",
        'mode_cancel': "Cealaigh",
        'mode_replace_text': "téacs a chur isteach",
        'mode_replace_cross': "cros a chur isteach",
        'mode_replace_signature': "síniú a chur isteach",
        'mode_replace_image': "íomhá a chur isteach",
        'mode_replace_form': "cruth a chur isteach",
        'mode_conflict_voice': "Tá mód {0} gníomhach. Scoir agus cuir téacs isteach?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Ionchur Téacs",
        'active_mode_signature': "Síniú",
        'active_mode_image': "Íomhá",
        'active_mode_form': "Cruth",
        'active_mode_and': " agus ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Ionsáigh",                    # Hauptmenü
        'insert_another_text': "Ionsáigh téacs",          # Vereinfacht
        'insert_another_cross': "Ionsáigh cros",        # Vereinfacht
        'insert_another_signature_1': "Síniú 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Síniú 2",      # Untermenü-Eintrag
        'insert_another_image': "Ionsáigh íomhá",         # Vereinfacht
        'insert_another_form_rect': "Dronuilleog",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Éilips",        # Untermenü-Eintrag
        'insert_another_form_line': "Líne (2 chliceáil)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Saighead (2 chliceáil)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Sábháil {0}",
        'save_dialog_message': "Sábhálfar {0} ar leathanach {1}.\n\nConas is mian leat dul ar aghaidh?",
        'save_all': "Sábháil gach {0}",
        'save_single': "Sábháil {0}",
        'save_customize': "Cuir {0} in oiriúint",
        'save_discard': "Caith an {0} seo",
        'save_continue': "Lean ar aghaidh ag eagarthóireacht",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Téigh go leathanach {0}",
        'context_rotate': " Rothlaigh leathanach {0}",
        'context_delete': " Scrios leathanach {0}",
        'context_export': " Easportáil leathanach {0}",
        'context_mark_as': " Marcáil leathanach mar...",
        'context_mark_empty': " Leathanach folamh",
        'context_unmark_empty': " Gan a bheith folamh a thuilleadh",
        'context_mark_export': " Marcáil le haghaidh easpórtála",
        'context_unmark_export': " Ná easpórtáil a thuilleadh",
        'context_batch_actions': " Comhghníomhartha",
        'context_batch_delete_empty': " Scrios gach ceann de na {0} leathanach folamh",
        'context_batch_export_single': " Easportáil gach ceann de na {0} leathanach (aon chomhad amháin)",
        'context_batch_export_split': " Easportáil gach ceann de na {0} leathanach (scartha)",
        'context_drag_start': " Tosaigh tarraing is scaoil",
        'context_drag_stop': " Críochnaigh tarraing is scaoil",
        'context_insert': " Ionsáigh",
        'context_insert_pages': " Ionsáigh leathanaigh",
        'context_zoom': "Zúmáil",
        'discard_mixed': "Caith gach {0} {1} agus {2} {3}",
        'save_mixed': "Sábháil {0} {1} agus {2} {3}",
        'discard_texts': "Caith gach ceann de na {0} téacs",
        'discard_text_single': "Caith 1 téacs",
        'save_texts': "Sábháil {0} téacs",
        'save_text_single': "Sábháil 1 téacs",
        'discard_crosses': "Caith gach ceann de na {0} cros",
        'discard_cross_single': "Caith 1 cros",
        'save_crosses': "Sábháil {0} cros",
        'save_cross_single': "Sábháil 1 cros",
        'discard_signatures': "Caith gach ceann de na {0} síniú",
        'save_signature_single': "Sábháil 1 síniú",
        'save_signatures': "Sábháil {0} síniú",
        'discard_images': "Caith gach ceann de na {0} íomhá",
        'save_image_single': "Sábháil 1 íomhá",
        'save_images': "Sábháil {0} íomhá",
        'discard_forms': "Caith gach ceann de na {0} cruth",
        'save_form_single': "Sábháil 1 cruth",
        'save_forms': "Sábháil {0} cruth",
        'cross_discard': "Caith an chros seo",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Eolas Easpórtála / Iompórtála",
        'export_what': "📋 Cad a easpórtáiltear?",
        'export_general': "Socruithe Ginearálta",
        'export_general_items': "• Guth (ar/as, luas)\n• Mód Dorcha/Geal\n• Socruithe cúltaca\n• Socruithe OCR",
        'export_image_form': "Socruithe Íomhánna agus Cruthanna",
        'export_image_form_items': "• Socruithe íomhánna (cóimheas trasnáin, méid réamhshocraithe)\n• Socruithe cruthanna (tiús líne, dathanna)\n• Socruithe sínithe (cosáin, méideanna, stampa ama)",
        'export_passwords': "Bunachar Pasfhocal",
        'export_passwords_items': "• Gach pasfhocal PDF sábháilte\n• Criptithe nó díchriptithe de rogha",
        'export_master': "Socruithe Príomhphasfhocal",
        'export_master_items': "• Hais Phríomhphasfhocal\n• Socruithe do shínithe/bhlúirí téacs",
        'export_signatures': "Sínithe agus Blúirí Téacs",
        'export_signatures_items': "• Gach comhad íomhá (sínithe)\n• Gach blúire téacs le formáidiú\n• Marcálacha príobháideacha/poiblí",
        'export_import_warning': "⚠️ Nótaí Tábhachtacha",
        'export_import_note': "• Nuair a iompórtáiltear, FORSCRÍOBHFAR GACH socrú reatha\n• Caithfear an feidhmchlár a atosú\n• Cuirfear sínithe/bhlúirí téacs atá ann cheana in ionad",
        'export_master_note': "• Má tá Príomhphasfhocal socraithe, is féidir leat roghnú:\n  - Díchriptithe (pasfhocail soiléir)\n  - Criptithe (inléite le Príomhphasfhocal amháin)",
        'export_security': "• Tá sonraí íogaire sa chomhad ZIP easpórtáilte\n• Coinnigh go sábháilte é (m.sh. ar thiomántán USB criptithe)\n• Má chailleann tú an comhad, ní féidir pasfhocail a aisghabháil",
        'export_format': "📁 Formáid Easpórtála",
        'export_format_desc': "Sábhálfar na socruithe in aon chomhad ZIP amháin:",
        'export_filename': "Socruithe_PDFDarkView_YYYYMMDD_HHMMSS.zip",
        'export_success': "Easpórtáladh socruithe go rathúil",
        'export_failed': "Theip ar easpórtáil",
        'export_import_question': "Ar mhaith leat an feidhmchlár a atosú anois?",
        'export_password_question': "Tá Príomhphasfhocal socraithe.\n\nAr mhaith leat na pasfhocail a easpórtáil gan chriptiú?\n(seachas sin easpórtálfar criptithe iad)",
        'export_decrypt': "Easpórtáil gan chriptiú",
        'export_encrypt': "Easpórtáil criptithe",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Eolas",
        'info_title': "Maidir le PDF Dark View",
        'info_version': "Leagan",
        'info_author': "Forbraithe ag Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Maidir",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> is breathnóir PDF inrochtana é, a forbraíodh go speisialta do dhaoine a bhfuil lagú radhairc orthu.</p>

            <p><strong>Príomhghnéithe:</strong></p>
            <ul>
                <li>Comhéadan ardchodarsnachta, inoiriúnaithe</li>
                <li>Rialú iomlán méarchláir</li>
                <li>Aschur cainte comhtháite</li>
                <li>OCR le haghaidh doiciméid scanta</li>
                <li>Uirlisí cuimsitheacha eagarthóireachta</li>
            </ul>

            <p>Tacaítear le níos mó ná 50 teanga – ionas go mbeidh PDFanna inrochtana do chách.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Gnéithe",
        'info_features_intro': "Cuireann PDF Dark View na féidearthachtaí seo a leanas ar fáil duit:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Taispeáint & Nascleanúint</strong> – Mód Dorcha/Solasach, leathanach a bhrabhsáil, súmáil, léim go leathanach</li>
            <li><strong>OCR (Aithint Téacs)</strong> – Déan doiciméid scanta in-chuardaithe agus in-chóipeáilte</li>
            <li><strong>Eagarthóireacht</strong> – Cuir isteach téacs, crosa, sínithe, íomhánna agus cruthanna</li>
            <li><strong>Bainistíocht Leathanach</strong> – Scriosadh, baint, cur isteach, bogadh trí tharraing is scaoil</li>
            <li><strong>Onnmhairiú</strong> – Go Word, Pages nó mar théacs</li>
            <li><strong>Slándáil</strong> – Cosaint agus bainistíocht focal faire</li>
            <li><strong>Inrochtaineacht</strong> – Aschur cainte, rialú méarchláir, ardchodarsnacht</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Oibriú",
        'info_accessibility': "♿ Inrochtaineacht – rialú iomlán méarchláir",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Ginearálta</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Oscail PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Cuardaigh</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Aistrigh Mód Dorcha/Solasach</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Priontáil</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Scoir</div>

        <div class="shortcut-cat">📖 Nascleanúint</div>
        <div class="shortcut-row"><kbd>Eochracha saighead</kbd> Brabhsáil leathanach ar leathanach</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Téigh go leathanach</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> An chéad leathanach</div>
        <div class="shortcut-row"><kbd>Ende</kbd> An leathanach deireanach</div>

        <div class="shortcut-cat">✏️ Eagarthóireacht</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Cuir isteach téacs</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Scrios leathanaigh</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Bain leathanaigh</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Cuir isteach leathanaigh</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Bog leathanaigh</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rothlaigh leathanach</div>

        <div class="shortcut-cat">🖼️ Eilimintí a bhogadh</div>
        <div class="shortcut-row"><kbd>Eochracha saighead</kbd> Bog téacs/íomhá/síniú</div>
        <div class="shortcut-row"><kbd>Ctrl+Eochracha saighead</kbd> Céimeanna níos mó</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Sábháil</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Caith ar ceal</div>

        <div class="shortcut-cat">🗣️ Aschur cainte</div>
        <div class="shortcut-row"><kbd>F2</kbd> Cas aschur cainte air/as</div>
        """,
        'info_contextmenu': "📌 Tábhachtach: Tá na feidhmeanna go léir ar fáil freisin tríd an roghchlár comhthéacs (cnaipe deas luiche)!",
        'info_accessibility_hint': "💡 Leid: Éascaíonn an t-aschur cainte (F2) treoshuíomh agus tugann sé aiseolas ar roghchláir agus dialóga.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Ceadúnas & Colafón",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 COLAPHÓN</strong><br>
        Faisnéis de réir § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, an Ghearmáin<br>
        R-phost: binhdiez64@gmail.com<br>
        Freagrach as an ábhar: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Séanadh dliteanais</strong><br>
        Forbraíodh na bogearraí leis an gcúram is mó. Ní thugtar aon bharántas maidir le cruinneas, iomláine agus feidhmiúlacht. Úsáid ar do phriacal féin.<br><br>

        <strong>📄 Ceadúnas MIT (úsáid phríobháideach)</strong><br>
        Cóipcheart (c) 2026 Toralf Schulz (BinhDiez)<br>
        Ceadaithe: úsáid saor in aisce, athruithe príobháideacha, cóipeanna pearsanta.<br>
        Neamhcheadaithe: díol, úsáid tráchtála, fógraí cóipchirt a bhaint.<br><br>

        <strong>🔧 Comhpháirteanna tríú páirtí</strong><br>
        Tá comhpháirteanna sna bogearraí seo faoi cheadúnais GPL, AGPL, Apache 2.0, BSD agus MIT.<br>
        Agus iad á ndáileadh ar aghaidh, ní mór téarmaí an cheadúnais faoi seach a chomhlíonadh.<br><br>

        <strong>🌐 Foinse Oscailte</strong><br>
        Tá an cód foinseach ar fáil agus is féidir é a fheiceáil, a mhodhnú agus a athdháileadh de réir théarmaí an cheadúnais faoi seach.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Buíochas",
        'info_credits': "Buíochas le pobal na bhfoinsí oscailte",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Próiseáil PDF</li>
            <li><strong>PyQt5</strong> – Comhéadan grafach</li>
            <li><strong>Tesseract OCR</strong> – Aithint téacs</li>
            <li><strong>OCRmyPDF</strong> – Comhtháthú OCR</li>
            <li><strong>python-docx</strong> – Onnmhairiú Word</li>
            <li><strong>qtawesome</strong> – Deilbhíní</li>
            <li><strong>DeepSeek</strong> – Tacaíocht le haistriúcháin (50+ teanga)</li>
            <li><strong>Gach úsáideoir</strong> – As aiseolas luachmhar</li>
            <li><strong>Pobal na bhfoinsí oscailte</strong> – As leabharlanna iontacha</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Teangacha",
        'info_languages_header': "🌍 Tacaíocht Teanga",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>Tacaíonn PDF Dark View faoi láthair le <strong>62 teanga</strong> – ionas gur féidir an bogearraí a úsáid go hinrochtana ar fud an domhain.</p>

            <p><strong>📖 Liosta iomlán na dteangacha (Ó Mhárta 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afracáinis</li>
                    <li>🇦🇱 Albáinis (Shqip)</li>
                    <li>🇩🇿 Araibis (العربية)</li>
                    <li>🇮🇩 Balainnis (Basa Bali)</li>
                    <li>🇧🇩 Beangálais (বাংলা)</li>
                    <li>🇲🇲 Burmais (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Boisnis (Bosanski)</li>
                    <li>🇧🇬 Bulgáiris (Български)</li>
                    <li>🇨🇳 Sínis (中文)</li>
                    <li>🇩🇰 Danmhairgis (Dansk)</li>
                    <li>🇩🇪 Gearmáinis (Deutsch)</li>
                    <li>🇬🇧 Béarla (English)</li>
                    <li>🇪🇪 Eastóinis (Eesti)</li>
                    <li>🇫🇮 Fionlainnis (Suomi)</li>
                    <li>🇫🇷 Fraincis (Français)</li>
                    <li>🇬🇷 Gréigis (Ελληνικά)</li>
                    <li>🇮🇱 Eabhrais (עברית)</li>
                    <li>🇮🇳 Hiondúis (हिन्दी)</li>
                    <li>🇭🇷 Cróitis (Hrvatski)</li>
                    <li>🇭🇺 Ungáiris (Magyar)</li>
                    <li>🇮🇩 Indinéisis (Bahasa Indonesia)</li>
                    <li>🇮🇪 Gaeilge (Gaeilge)</li>
                    <li>🇮🇸 Íoslainnis (Íslenska)</li>
                    <li>🇮🇹 Iodáilis (Italiano)</li>
                    <li>🇯🇵 Seapáinis (日本語)</li>
                    <li>🇰🇭 Ciméiris (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Cóiréis (한국어)</li>
                    <li>🇱🇦 Laoisis (ພາສາລາວ)</li>
                    <li>🇱🇻 Laitvis (Latviešu)</li>
                    <li>🇱🇹 Liotuáinis (Lietuvių)</li>
                    <li>🇱🇺 Lucsambuirgis (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaeis (Bahasa Melayu)</li>
                    <li>🇮🇳 Maraitis (मराठी)</li>
                    <li>🇲🇳 Mongóilis (Монгол)</li>
                    <li>🇳🇵 Neipeailis (नेपाली)</li>
                    <li>🇳🇱 Ollainnis (Nederlands)</li>
                    <li>🇳🇴 Ioruais (Norsk)</li>
                    <li>🇦🇫 Paistis (پښتو)</li>
                    <li>🇮🇷 Peirsis (فارسی)</li>
                    <li>🇵🇱 Polainnis (Polski)</li>
                    <li>🇵🇹 Portaingéilis (Português)</li>
                    <li>🇮🇳 Puinseáibis (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rómáinis (Română)</li>
                    <li>🇷🇺 Rúisis (Русский)</li>
                    <li>🇸🇪 Sualainnis (Svenska)</li>
                    <li>🇷🇸 Seirbis (Српски)</li>
                    <li>🇸🇰 Slóvaicis (Slovenčina)</li>
                    <li>🇸🇮 Slóivéinis (Slovenščina)</li>
                    <li>🇪🇸 Spáinnis (Español)</li>
                    <li>🇹🇿 Svahaílis (Kiswahili)</li>
                    <li>🇵🇭 Tagálaigis (Filipino)</li>
                    <li>🇮🇳 Tamailis (தமிழ்)</li>
                    <li>🇮🇳 Teileagúis (తెలుగు)</li>
                    <li>🇹🇭 Téalainnis (ไทย)</li>
                    <li>🇨🇿 Seicis (Čeština)</li>
                    <li>🇹🇷 Tuircis (Türkçe)</li>
                    <li>🇺🇦 Úcráinis (Українська)</li>
                    <li>🇵🇰 Urdais (اردو)</li>
                    <li>🇻🇳 Vítneamais (Tiếng Việt)</li>
                    <li>🇸🇳 Volófais (Wolof)</li>
                    <li>🇺🇸 Giúdais (ייִדיש)</li>
                    <li>🇿🇦 Súlúis (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Cuir do theangacha féin leis:</strong><br>
                Ar mhaith leat teanga nach bhfuil san áireamh go fóill? Níl le déanamh ach do chomhad foclóra féin (<code>sprache_xx.py</code>) a chur in aice leis an bhfeidhmchlár – aithneoidh na bogearraí go huathoibríoch é. Má tá suim agat in aistriúchán ar leith, ná bíodh drogall ort teagmháil a dhéanamh liom.
            </div>

            <p><strong>🙏 Buíochas speisialta:</strong> Le DeepSeek as an tacaíocht chun na foclóirí go léir a aistriú go 62 teanga.</p>

            <p>📧 Teagmháil le haghaidh aistriúchán: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Earráid",
        'error_occurred': "Tharla earráid",
        'error_pdf_load': "Earráid agus PDF á luchtú",
        'error_pdf_save': "Earráid agus PDF á shábháil",
        'error_ocr': "Earráid le linn aithint téacs",
        'error_no_pdf': "Gan PDF luchtaithe",
        'error_page_not_found': "Leathanach gan aimsiú",
        'error_invalid_range': "Raon leathanach neamhbhailí",
        'error_file_not_found': "Comhad gan aimsiú",
        'error_permission': "Gan cead",
        'error_unknown': "Earráid anaithnid",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Rath",
        'success_operation': "Gníomh críochnaithe go rathúil",
        'success_saved': "Sábháilte go rathúil",
        'success_exported': "Easpórtáilte go rathúil",
        'success_imported': "Iompórtáilte go rathúil",
        'success_deleted': "Scriosta go rathúil",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Deimhniú",
        'confirm_yes': "Tá",
        'confirm_no': "Níl",
        'confirm_ok': "OK",
        'confirm_cancel': "Cealaigh",
        'confirm_delete': "Scrios",
        'confirm_overwrite': "Forscríobh",
        'confirm_continue': "Lean ar aghaidh",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF á luchtú...",
        'progress_saving': "PDF á shábháil...",
        'progress_exporting': "PDF á easpórtáil...",
        'progress_processing': "Próiseáil ar siúl...",
        'progress_wait': "Fan le do thoil...",
        'progress_preparing': "Ag ullmhú...",
        'progress_finalizing': "Ag críochnú...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Bán",
        'color_black': "Dubh",
        'color_red': "Dearg",
        'color_green': "Glas",
        'color_blue': "Gorm",
        'color_yellow': "Buí",
        'color_magenta': "Maigeanta",
        'color_cyan': "Cian",
        'color_orange': "Oráiste",
        'color_gray': "Liath",
        'color_custom': "Roghnú Datha",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Comhad",
        'menu_edit': "&Cuir in Eagar",
        'menu_view': "&Amharc",
        'menu_tools': "&Uirlisí",
        'menu_settings': "&Socruithe",
        'menu_help': "&Cabhair",
        'menu_language': "🌐 Teanga",
        'menu_guides': "&Treoracha",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Oscail",
        'file_save_as': "&Sábháil Mar...",
        'file_protect': "&Cosain doiciméad...",
        'file_export': "&Easpórtáil",
        'file_export_pages': "Easpórtáil mar Pages",
        'file_export_word': "Easpórtáil mar DOCX",
        'file_export_text': "Easpórtáil mar TXT",
        'file_print_now': "&Priontáil anois",
        'file_print': "&Priontáil",
        'file_close': "&Dún",
        'file_quit': "&Scoir",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Cuardaigh",
        'edit_ocr': " Déan OCR",
        'edit_rotate': "&Rothlaigh leathanach",
        'edit_rotate_all': "Rothlaigh &gach leathanach",
        'edit_delete_pages': "&Scrios leathanaigh",
        'edit_extract_pages': "&Bain leathanaigh",
        'edit_insert_pages': "&Ionsáigh leathanaigh",
        'edit_move_pages': "&Bog leathanaigh",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Ionsáigh téacs agus crosa",
        'text_insert': " Ionsáigh téacs",
        'cross_insert': " Ionsáigh cros",
        'text_customize': " Cuir téacs in oiriúint",
        'cross_customize': " Cuir an chros seo in oiriúint",
        'cross_customize_all': " Cuir gach cros in oiriúint",
        'text_discard': " Caith an téacs / an chros seo",
        'text_discard_all': " Caith gach téacs agus cros",
        'text_save_all': " Sábháil gach téacs agus cros",
        'text_guide': " Ionchur téacs / blúirí téacs - treoir",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Ionsáigh síniú",
        'signature_settings_menu': " Socruithe...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Ionsáigh íomhá",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Ionsáigh cruthanna",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Taispeáin fuinneog téacs",
        'view_zoom': "&Zúmáil",
        'view_zoom_page': "&Leithead leathanaigh (réamhshocrú)",
        'view_zoom_two': "&Dá leathanach",
        'view_zoom_overview': "&Forbhreathnú (il-leathanaigh)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Cúnamh",
        'settings_voice': "Guth",
        'settings_voice_tooltip': "comhlánaíonn guth léitheoirí scáileáin le heolas breise",
        'settings_signature': "&Socruithe Sínithe",
        'settings_password': "&Bainistíocht Pasfhocal",
        'settings_backup': "Cruthaigh cúltaca roimh athruithe",
        'settings_export_import': "&Easpórtáil socruithe / iompórtáil socruithe",
        'settings_export': "&Easpórtáil gach socrú...",
        'settings_import': "&Iompórtáil gach socrú...",
        'settings_export_info': "&Cad a easpórtáiltear?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "ar",
        'voice_off': "as",
        'voice_toggle': "Guth {0}",
        'voice_speed': "Luas {0} faoin gcéad",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Uirlis gan aimsiú:\n{0}\n\nBASE_DIR: {1}\nCinntigh go bhfuil uirlisí PDF suiteáilte in {1}.",
        'tool_started': "{0} tosaithe",
        'tool_start_failed': "Níorbh fhéidir é a thosú",
        'process_error_failed_to_start': "Níorbh fhéidir an próiseas a thosú. An bhfuil an comhad ann?",
        'process_error_crashed': "Thit an próiseas as a chéile le linn tosaithe.",
        'process_error_timeout': "Am próisis caite.",
        'process_error_write': "Earráid scríofa sa phróiseas.",
        'process_error_read': "Earráid léite sa phróiseas.",
        'process_error_unknown': "Earráid phróisis anaithnid",
        'process_command': "Ordú",
        'process_normal_exit': "críochnaithe de ghnáth",
        'process_crashed': "thit as a chéile",
        'process_nonzero_exit': "Chríochnaigh {0} le cód earráide {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Á chealú...",
        'move_cancelling': "Bogadh á chealú",
        'opening_pdf': "PDF á oscailt...",
        'loading_document': "Doiciméad á luchtú...",
        'pdf_opened': "PDF oscailte",
        'pages_found_moving': "{0} leathanach aimsithe, {1} le bogadh",
        'creating_backup': "Cúltaca á chruthú...",
        'backup_description': "Comhad bunaidh á chúltacú...",
        'backup_saved_as': "Cúltacaithe mar: {0}",
        'error_format': "Earráid: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView le BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Cuardach athshocraithe",
        'page_header_simple': "=== Leathanach {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Bainistíocht Pasfhocal – Treoir",
        'password_guide_voice': "Treoir ar bhainistíocht pasfhocal. Léigh na nótaí le do thoil.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Bainistíocht Pasfhocal – Treoir Mhionsonraithe</strong></p>

        <p><strong>1. Cosaint pasfhocail do PDFanna</strong></p>
        <ul>
        <li>Nuair a osclaíonn tú PDF atá cosanta le pasfhocal, feicfear dialóg inar féidir leat an pasfhocal a iontráil.</li>
        <li>Is féidir leat an pasfhocal a shábháil go criptithe, ionas nach mbeidh ort é a iontráil gach uair (bosca "Sábháil pasfhocal").</li>
        <li>Leis an gcnaipe "Bain pasfhocal" is féidir leat cóip dhíchriptithe den PDF a chruthú agus an pasfhocal a scriosadh ón mbunachar.</li>
        </ul>

        <p><strong>2. Príomhphasfhocal</strong></p>
        <ul>
        <li>Cosnaíonn an Príomhphasfhocal rochtain ar gach pasfhocal PDF atá sábháilte.</li>
        <li><strong>Socrú:</strong> Téigh go "Socruithe → Bainistíocht Pasfhocal → Socruithe Príomhphasfhocal" agus cliceáil "Socraigh Príomhphasfhocal". Roghnaigh pasfhocal láidir (8 gcarachtar ar a laghad).</li>
        <li><strong>Athrú:</strong> Tar éis fíordheimhnithe rathúil, is féidir leat an Príomhphasfhocal a athrú.</li>
        <li><strong>Baint:</strong> Má scriosann tú an Príomhphasfhocal, scriosfar GACH pasfhocal sábháilte go buan. Is féidir leat cúltaca a easpórtáil roimh ré.</li>
        <li>Uair amháin in aghaidh an tseisiúin, caithfidh tú fíordheimhniú leis an bPríomhphasfhocal chun rochtain a fháil ar fheidhmeanna cosanta (m.sh. pasfhocail a thaispeáint).</li>
        </ul>

        <p><strong>3. Bainistíocht Pasfhocal (liosta)</strong></p>
        <ul>
        <li>Faoi "Socruithe → Bainistíocht Pasfhocal" osclaíonn tú tábla de na PDFanna go léir a bhfuil pasfhocail sábháilte acu.</li>
        <li><strong>Gan Príomhphasfhocal:</strong> Ní féidir leat ach iontrálacha a scriosadh – fanann na pasfhocail i bhfolach.</li>
        <li><strong>Le Príomhphasfhocal (fíordheimhnithe):</strong> Is féidir leat pasfhocail a thaispeáint, a chóipeáil, a easpórtáil agus a scriosadh.</li>
        <li><strong>Easpórtáil:</strong> Roghnaigh formáid (JSON, CSV, TXT) agus sábháil an liosta. Má tá Príomhphasfhocal socraithe, is féidir leat a roghnú an ndéantar na pasfhocail a easpórtáil go soiléir nó criptithe.</li>
        <li><strong>Iompórtáil:</strong> Is féidir comhad ZIP a easpórtáladh roimhe seo (gach socrú san áireamh) a léamh ar ais trí "Socruithe → Easpórtáil socruithe / iompórtáil socruithe". Rabhadh: Forscríobhfar sonraí atá ann cheana!</li>
        </ul>

        <p><strong>4. Gineadóir Pasfhocal</strong></p>
        <ul>
        <li>Sa dialóg pasfhocail (m.sh. agus PDF á chosaint) gheobhaidh tú cnaipe dísle 🎲 ar dheis an réimse ionchuir.</li>
        <li>Cliceáil air chun an gineadóir pasfhocal a oscailt. Is féidir leat fad, tacair charachtar (ceannlitreacha, litreacha beaga, uimhreacha, siombailí) agus carachtar deighilte a shocrú le haghaidh inléiteachta níos fearr.</li>
        <li>Is féidir an pasfhocal ginte a ghlacadh go díreach agus a chóipeáil más gá.</li>
        </ul>

        <p><strong>5. Nótaí Tábhachtacha Slándála</strong></p>
        <ul>
        <li>Stóráiltear pasfhocail shábháilte le criptiú AES-256. Díorthaítear an eochair ó do Phríomhphasfhocal (má tá sé socraithe) nó ó luach seasta (gan Phríomhphasfhocal).</li>
        <li>Gan Phríomhphasfhocal, tá na pasfhocail criptithe, ach tá an eochair leabaithe sa chlár – d'fhéadfadh ionsaitheoir a bhfuil rochtain aige ar do chuid comhad iad a dhíchriptiú. Mar sin molaimid go láidir úsáid Príomhphasfhocail.</li>
        <li>Tá bunachar pasfhocal suite sa chomhad `Data/passwords.json`. Déan cúltaca go rialta, go háirithe roimh an bPríomhphasfhocal a bhaint.</li>
        <li>Má chailleann tú an Príomhphasfhocal, caillfear gach pasfhocal sábháilte go buan.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Mód inbhéartaithe",
        'invert_mode_classic': "Clasaiceach (inbhéartaigh gach dath)",
        'invert_mode_smart': "Cliste (inbhéartaigh gile amháin)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Tairseach scála liath",
        'gray_threshold_10': "10% (dian)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Réamhshocrú)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (bog)",
        'threshold_changed': "Tairseach socraithe go {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Tairseach scála liath – Míniú",
        'threshold_guide_text': "Cinneann an tairseach scála liath cé na picteilíní sa mhód dorcha cliste a mheastar a bheith 'liath' agus a inbhéartaítear.\n\n"
                                "• Déanann luach íseal (10%) inbhéartú ar scáthanna liatha beagnach foirfe amháin – coinnítear eilimintí daite go hiomlán.\n"
                                "• Déanann luach ard (50%) inbhéartú freisin ar phicteilíní beagáinín daite – méadaíonn sé seo an chodarsnacht, ach féadann sé dathanna a shaobhadh.\n\n"
                                "Braitheann an luach is fearr ar an doiciméad. I gcás doiciméid téacs amháin, is minic go bhfuil 30–40% iontach, i gcás grafaicí daite is fearr 10–20%.\n\n"
                                "Is féidir leat an luach a choigeartú tríd an roghchlár 'Socruithe' am ar bith – lódálfar an PDF arís láithreach.\n\n"
                                "Tabhair faoi deara:\n* Ní féidir grianghraif agus íomhánna a thaispeáint i gceart ach amháin sa mhód solasach!\n* Ní thaispeántar na socruithe inbhéartaithe ach amháin nuair a bhíonn an mód dorcha gníomhach.",
        'threshold_guide_voice': "Cinneann an tairseach scála liath cé chomh láidir agus a idirghabhálann an mód dorcha cliste. Coinníonn luach íseal dathanna, méadaíonn luach ard codarsnacht.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Ag oscailt PDF...",
        'progress_loading_document': "Ag lódáil doiciméid...",
        'progress_pdf_opened': "PDF oscailte",
        'progress_creating_backup': "Ag cruthú cúltaca...",
        'progress_backup_description': "Ag daingniú comhad bunaidh...",
        'progress_backup_created': "Cúltaca cruthaithe",
        'progress_backup_saved_as': "Sábháilte mar: {0}",
        'progress_analyzing_start': "Ag tosú anailíse...",
        'progress_searching_empty': "Ag cuardach leathanaigh fholamha...",
        'progress_page_empty': "Tá leathanach {0} folamh",
        'progress_page_keep': "Coinnigh leathanach {0}",
        'progress_analysis_complete': "Anailís críochnaithe",
        'progress_empty_found': "Fuarthas {0} leathanach folamh",
        'progress_current_page': "Leathanach reatha",
        'progress_mark_delete': "Á mharcáil le scriosadh",
        'progress_range_selected': "Raon leathanach {0}-{1}",
        'progress_deleting_pages': "Ag scriosadh {0} leathanach",
        'progress_creating_new_pdf': "Ag cruthú PDF nua...",
        'progress_transferring_pages': "Ag aistriú leathanach",
        'progress_keeping_page': "Coinneofar leathanach {0} ({1}/{2})",
        'progress_saving_pdf': "Ag sábháil PDF...",
        'progress_optimizing': "Ag optamú méid comhaid...",
        'progress_finalizing': "Ag críochnú...",
        'progress_new_size': "Méid nua: {0:.2f} MB",
        'progress_cancelling': "Ag cealú...",
        'progress_cancel_message': "Ag cealú {0}",
        'progress_pages_found_moving': "Fuarthas {0} leathanach, {1} le bogadh",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Ag anailísiú PDF...",
        'ocr_status_optimizing': "Optamú íomhá ar bun...",
        'ocr_status_recognizing': "Aithint téacs ar bun...",
        'ocr_status_embedding': "Ag leabú téacs...",
        'ocr_status_finalizing': "Ag críochnú PDF...",

        # PDF-Laden
        'progress_preparing': "Ag ullmhú...",
        'progress_loading': "Ag lódáil PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Ag scriosadh leathanach...",
        'progress_moving_title': "Ag bogadh leathanach...",
        'pages_found': "Leathanaigh aimsithe",
        'progress_creating_new_order': "Ag cruthú ord nua...",
        'progress_sorting_pages': "Ag sórtáil leathanach...",
        'progress_moving_to_begin': "Ag bogadh {0} leathanach go dtí an tús",
        'progress_transferring_count': "Ag aistriú {0} leathanach",
        'progress_transferring_before_target': "Ag aistriú leathanach roimh an sprioc",
        'progress_moving_pages': "Ag bogadh {0} leathanach",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_cúltaca_",
        'filename_protected_suffix': "_cosanta_",
        'filename_copy_suffix': "_Cóip",
        'filename_page_single': "_Leathanach_",
        'filename_page_range': "_Leathanaigh_",
        'filename_export_page': "_Leathanach_{0:03}",
        'filename_export_range': "_Leathanaigh_{0}-{1}",
        'filename_export_multiple': "_Leathanaigh_{0}",
        'filename_with_text': "_le_Téacs",
        'filename_with_signature': "_le_Síniú",
        'filename_with_image': "_le_hÍomhá",
        'filename_with_forms': "_le_Cruthanna",
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
        'view_toggle_navbar': "Taispeáin barra cnaipe",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Ní féidir gach leathanach a scriosadh",
		'pages_cannot_delete_last_page': 'Ní féidir an leathanach deireanach a scriosadh!',
		'pages_cannot_delete_all_pages': 'Caithfidh leathanach amháin ar a laghad fanacht sa cháipéis!',
		'delete_pages_confirm': 'An bhfuil tú cinnte gur mhaith leat {0} leathanach a scriosadh?',
		'delete_pages_confirm_voice': 'An bhfuil tú cinnte gur mhaith leat {0} leathanach a scriosadh?',
		'pages_deleted': 'Scriosadh {0} leathanach go rathúil.',
		'warning': 'Rabhadh',
		'error': 'Earráid',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Níor roghnaíodh foirm",
        'form_customized': "Foirm shaincheaptha",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Roghnaigh",
        'btn_use': "Úsáid",
        'master_password_for_spasswords': "Chun pasfhocail a stóráil agus a úsáid, ní mór duit másterphasfhocal a shocrú ar dtús.\n\nAr mhaith leat an másterphasfhocal a shocrú anois?",
        'open_saved_dialog_title': "Oscail comhad sábháilte",
        'open_saved_question': "Ar mhaith leat an comhad sábháilte a oscailt anois?",
        'password': "Pasfhocal",
        'password_manager_master_required': "Níl an bainisteoir pasfhocal ar fáil ach amháin má tá másterphasfhocal socraithe.\n\nAr mhaith leat an másterphasfhocal a shocrú anois?",
        'password_master_required_for_select': "Chun pasfhocail shábháilte a fheiceáil agus a roghnú, ní mór duit fíordheimhniú le do mhásterphasfhocal ar dtús.\n\nAr mhaith leat fíordheimhniú anois?",
        'password_not_available': "Níl an pasfhocal roghnaithe ar fáil nó níorbh fhéidir é a dhíchriptiú.",
        'password_options_title': "Roghanna pasfhocail",
        'password_save_choice_change': "Socraigh pasfhocal nua",
        'password_save_choice_keep': "Úsáid pasfhocal atá ann cheana",
        'password_save_choice_none': "Stóráil gan chriptiú",
        'password_save_hint': "Socraigh másterphasfhocal ar dtús chun pasfhocail a stóráil go sábháilte.",
        'password_save_master_required': "Stóráil pasfhocal (ní féidir ach le másterphasfhocal)",
        'password_save_question': "Tá an PDF reatha cosanta ag pasfhocal. Ar mhaith leat an pasfhocal atá ann cheana a úsáid, ceann nua a shocrú nó stóráil gan chriptiú?",
        'password_select': "Roghnaigh pasfhocal",
        'password_select_none': "Níor roghnaíodh aon phasfhocal.\n\nRoghnaigh pasfhocal as an liosta le do thoil.",
        'password_select_one': "Roghnaigh go díreach pasfhocal amháin le do thoil.\n\nTá roinnt pasfhocal marcáilte agat.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_cúltaca",
        'filename_insert_suffix': "_le_hionsá",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_leathanaigh_scriosta",
        'filename_pages_moved': "_leathanaigh_bhogtha",
        'filename_rotated_all_suffix': "_gach_leathanach_rothlaithe",
        'filename_rotated_suffix': "_leathanach_rothlaithe",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Cumraíocht ainmneacha comhad nuair a athraítear PDF",
        'filename_keep_suffixes': "Coinnigh iarfhocail roimhe seo (m.sh. _le_téacs)",
        'filename_keep_suffixes_false': "Cuir in ionad",
        'filename_keep_suffixes_true': "Coinnigh",
        'filename_preview_label': "Réamhamharc ar ainm an chomhaid:",
        'filename_preview_overwrite_hint': "Réamhamharc ar fáil – scríobhfar an bunleagan thar.",
        'filename_separator': "Deighilteoir idir focail",
        'filename_separator_none': "Gan deighilteoir",
        'filename_separator_space': "Spás ( )",
        'filename_separator_underscore': "Fothaiscne (_)",
        'filename_settings_saved': "Socruithe ainm comhaid sábháilte",
        'filename_settings_title': "Formáidiú ainm comhaid & cúltaca",
        'filename_timestamp_position': "Ionad an stampa ama",
        'filename_timestamp_position_after': "Tar éis an bhunainm",
        'filename_timestamp_position_before': "Go hiomlán chun tosaigh",
        'filename_timestamp_position_end': "Ag an deireadh",
        'filename_use_timestamp': "Úsáid stampa ama",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Iompar agus athruithe á ndéanamh:</b><ul><li>Scriosadh agus hionsá leathanach</li><li>Hionsá téacs, sínithe, íomhá agus cruthanna</li><li>OCR</li></ul></html>",
        'backup_section': "Cúltaca d'oibríochtaí leathanach (Scrios, Bog)",
        'behavior_info': "Nóta: Le 'Scríobh thar bhunleagan', déantar neamhaird ar stampaí ama agus iarfhocail – coinníonn an comhad a ainm.",
        'behavior_new_file': "Cruthaigh comhad nua i gcónaí (le stampa ama agus iarfhocal)",
        'behavior_overwrite': "Scríobh thar bhunleagan (gan comhad nua)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Rothlaíodh gach leathanach.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {0}",
        'all_pages_rotated_voice': "Gach leathanach rothlaithe, comhad nua cruthaithe.",
        'empty_pages_deleted_new_file': "Scriosadh {0} leathanach folamh.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {1}",
        'empty_pages_deleted_voice': "{0} leathanach folamh scriosta, comhad nua cruthaithe.",
        'ocr_keep_original': "Coinnigh an bunleagan (oscail de láimh níos déanaí)",
        'ocr_new_file_question': "Sábháladh an PDF nua inchuardaithe faoi:\n{0}\n\nAr mhaith leat é a oscailt anois?",
        'ocr_open_new': "Oscail comhad OCR nua",
        'ocr_original_kept': "Fanann an bunleagan oscailte. Sábháladh an comhad OCR.",
        'page_deleted_new_file': "Scriosadh leathanach {0}.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {1}",
        'page_deleted_voice': "Leathanach {0} scriosta, comhad nua cruthaithe.",
        'page_rotated_new_file': "Rothlaíodh leathanach {0}.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {1}",
        'page_rotated_voice': "Leathanach {0} rothlaithe, comhad nua cruthaithe.",
        'pages_deleted_new_file': "Scriosadh {0} leathanach.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {1}",
        'pages_deleted_new_file_voice': "{0} leathanach scriosta, comhad nua cruthaithe.",
        'pages_inserted_new_file': "Hionsáileadh {0} leathanach.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {1}",
        'pages_inserted_new_file_ask': "Hionsáileadh {0} leathanach.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {1}\n\nAr mhaith leat é a oscailt anois?",
        'pages_inserted_voice_new': "{0} leathanach hionsáilte, comhad nua cruthaithe.",
        'pages_moved_new_file': "Bogadh {0} leathanach.\n\nD'fhan an bunleagan gan athrú.\nComhad nua: {1}",
        'pages_moved_new_file_voice': "{0} leathanach bogtha, comhad nua cruthaithe.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ná taispeáin arís",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Socrú cúltaca</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Cúltaca AR</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Ag gach athrú a scríobhann thar an mbunleagan</strong> (téacs, síniú, íomhá, cruth, OCR, rothlú, hionsá, scriosadh/bogadh leathanach) cruthaítear <strong>go huathoibríoch cúltaca le stampa ama</strong> sula gcuirtear an t-athrú i bhfeidhm.</p>
                <p style="margin: 5px 0 5px 20px;">• Tá an cúltaca suite in aice leis an mbunleagan (m.sh. <code>Doiciméad_cúltaca_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Má ghníomhaigh tú an rogha <strong>„Scríobh thar bhunleagan“</strong> chomh maith, cruthaítear cúltaca freisin.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Cúltaca AS</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Ní chruthaítear aon chúltaca</strong> – ná agus tú ag scríobh thar, ná ag oibríochtaí leathanach.</p>
                <p style="margin: 5px 0 5px 20px;">• Is féidir an bunleagan a chailliúint go neamh-inchúlghairthe nuair a scríobhtar thar.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Molta d'úsáideoirí taithí amháin!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Leid:</strong> Tá socrú cúltaca neamhspleách ar an rogha „Scríobh thar bhunleagan“. Is féidir leat an dá rud a chomhcheangal.<br>
                Is féidir leat an teachtaireacht seo a cheilt go buan.
            </div>
        </div>
        """,
        'backup_info_title': "Iompar cúltaca",
        'backup_info_voice': "Fógra faoi iompar cúltaca ag oibríochtaí leathanach. Cúltaca ar scríobhann thar an mbunleagan, cúltaca as cruthaíonn comhad nua.",
        'show_backup_info': "Eolas faoi shocrú cúltaca",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ná taispeáin arís",
        'overwrite_enable_backup': "Gníomhaigh cúltaca (molta)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Scríobh thar bhunleagan</p>
            <p>Má ghníomhaíonn tú an rogha seo, sábhálfar athruithe (téacs, síniú, íomhá, cruth, OCR, rothlú, hionsá) <strong>go díreach sa bhunleagan</strong> – <strong>ní chruthaítear aon chomhad nua</strong>.</p>
            <p>• Fanann ainm an chomhaid gan athrú.<br>
            • Déantar neamhaird ar stampaí ama agus iarfhocail.<br>
            • <strong>Gan chúltaca, is féidir an bunleagan a chailliúint go neamh-inchúlghairthe.</strong></p>
            <p style="color: #FFD700;">Moltar: Gníomhaigh rogha cúltaca chomh maith chun cóipeanna slándála uathoibríocha a fháil.</p>
        </div>
        """,
        'overwrite_info_title': "Scríobh thar bhunleagan",
        'overwrite_info_voice': "Rabhadh: Scríobh thar bhunleagan – gan comhad nua. Cúltaca molta.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Hionsáileadh {0} leathanach.\n\nScríobhadh an bunleagan thar.\nCruthaíodh cúltaca.",
        'pages_inserted_overwrite_no_backup': "Hionsáileadh {0} leathanach.\n\nScríobhadh an bunleagan thar.\nNÍOR cruthaíodh cúltaca.",
        'texts_saved_overwrite_with_backup': "Sábháladh na hathruithe sa bhunleagan.\n\nCruthaíodh cúltaca.",
        'texts_saved_overwrite_no_backup': "Sábháladh na hathruithe sa bhunleagan.\n\nNÍOR cruthaíodh cúltaca.",
        'texts_crosses_saved_new_file': "Hionsáileadh {0} {1} agus {2} {3}.\n\nD'fhan an bunleagan gan athrú.\nCruthaíodh comhad nua.\n\nAn PDF nua á lódáil...",
        'texts_saved_new_file': "Hionsáileadh {0} {1}.\n\nD'fhan an bunleagan gan athrú.\nCruthaíodh comhad nua.\n\nAn PDF nua á lódáil...",
        'crosses_saved_new_file': "Hionsáileadh {0} {1}.\n\nD'fhan an bunleagan gan athrú.\nCruthaíodh comhad nua.\n\nAn PDF nua á lódáil...",
        'elements_saved_new_file': "Hionsáileadh {0} eilimint.\n\nD'fhan an bunleagan gan athrú.\nCruthaíodh comhad nua.\n\nAn PDF nua á lódáil...",
        'signatures_saved_overwrite_with_backup': "Sábháladh an síniú/sínithe sa bhunleagan.\n\nCruthaíodh cúltaca.",
        'signatures_saved_overwrite_no_backup': "Sábháladh an síniú/sínithe sa bhunleagan.\n\nNÍOR cruthaíodh cúltaca.",
        'images_saved_overwrite_with_backup': "Sábháladh an íomhá/íomhánna sa bhunleagan.\n\nCruthaíodh cúltaca.",
        'images_saved_overwrite_no_backup': "Sábháladh an íomhá/íomhánna sa bhunleagan.\n\nNÍOR cruthaíodh cúltaca.",
        'forms_saved_overwrite_with_backup': "Sábháladh an cruth/cruthanna sa bhunleagan.\n\nCruthaíodh cúltaca.",
        'forms_saved_overwrite_no_backup': "Sábháladh an cruth/cruthanna sa bhunleagan.\n\nNÍOR cruthaíodh cúltaca.",
        'signatures_saved_new_file': "Hionsáileadh {0} síniú.\n\nD'fhan an bunleagan gan athrú.\nCruthaíodh comhad nua.\n\nAn PDF nua á lódáil...",
        'images_saved_new_file': "Hionsáileadh {0} íomhá.\n\nD'fhan an bunleagan gan athrú.\nCruthaíodh comhad nua.\n\nAn PDF nua á lódáil...",
        'forms_saved_new_file': "Hionsáileadh {0} cruth.\n\nD'fhan an bunleagan gan athrú.\nCruthaíodh comhad nua.\n\nAn PDF nua á lódáil...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Rabhadh: Tá leathanaigh rothlaithe sa PDF seo. D'fhéadfadh an suíomh a bheith éagsúil.",
        'page_rotated_warning_title': "Leathanach rothlaithe braite",
        'page_rotated_warning_message': "Tá an leathanach reatha {0} rothlaithe faoi {1}°.\n\nNí thacaítear le heilimintí a hionsá ar leathanaigh rothlaithe.\n\nAr mhaith leat an leathanach a rothlú go dtí seasamh díreach anois?",
        'page_rotated_warning_voice': "Rabhadh: Tá an leathanach rothlaithe. Rothlaigh ar dtús é le do thoil.",
        'paste_on_rotated_page_simple_warning': "Ní féidir hionsá ar leathanach {0}!\n\nTá an leathanach seo rothlaithe faoi {1}°.\n\nRothlaigh an leathanach go 0° ar dtús le do thoil (Roghchlár: Cuir in Eagar → Ailínigh leathanach).\n\nRabhadh:\nCaillfear an eilimint a cóipeáladh roimhe seo mura sábhálann tú sula rothlaíonn tú an leathanach.",
        'paste_on_rotated_page_voice': "Hionsá cealaithe. Tá an leathanach rothlaithe. Ailínigh an leathanach ar dtús le do thoil.",
        'page_rotated_cancel': "Cealaigh",
        'page_rotated_rotate_until_upright': "Rothlaigh leathanach arís agus arís eile (go dtí go bhfuil sé díreach)",
        'page_rotated_now_upright': "Tá an leathanach díreach anois. Is féidir leat hionsá anois.",
        'page_rotated_still_not_upright': "Níorbh fhéidir an leathanach a rothlú go dtí seasamh díreach. Ceartaigh de láimh le do thoil.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Cabhair: Ceartaigh leathanaigh rothlaithe",
        'help_rotated_pages_voice': "Osclaítear cabhair chun leathanaigh rothlaithe a cheartú.",
        'btn_help': "Cabhair",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Fadhb: Leathanach rothlaithe – Ní oibríonn hionsá i gceart</p>

            <p>Mura n-oibríonn hionsá téacsanna, sínithe nó cruthanna ar leathanach rothlaithe i gceart, is féidir leat an leathanach a cheartú le heagarthóir PDF seachtrach.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Réiteach le huirlis sheachtrach (m.sh. macOS Réamhamharc)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Onnmhairigh leathanach</strong><br>
                &nbsp;&nbsp;Cliceáil sa roghchlár ar <strong>Comhad → Onnmhairigh mar leathanaigh</strong> nó bain úsáid as modh eile chun an leathanach atá uait a shábháil mar PDF amháin.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Oscail leathanach i gclár seachtrach</strong><br>
                &nbsp;&nbsp;Oscail an PDF onnmhairithe in eagarthóir PDF (m.sh. <strong>macOS Réamhamharc</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rothlaigh leathanach</strong><br>
                &nbsp;&nbsp;Rothlaigh an leathanach ionas go mbeidh sé díreach (i Réamhamharc: <strong>Uirlisí → Rothlaigh</strong> nó <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Sábháil</strong><br>
                &nbsp;&nbsp;Sábháil an leathanach ceartaithe (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Hionsá an leathanach ar ais sa doiciméad bunaidh</strong><br>
                &nbsp;&nbsp;Fill ar PDFDarkView agus hionsá an leathanach ceartaithe ag an suíomh atá uait:<br>
                &nbsp;&nbsp;<strong>Cuir in Eagar → Hionsá leathanaigh</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Rogha eile: Rothlaigh leathanach sa bhunleagan</p>
                <p style="margin: 5px 0 5px 20px;">• Úsáid an fheidhm rothlaithe ionsuite (<strong>Cuir in Eagar → Rothlaigh leathanach</strong>) chun an leathanach a cheartú céim ar chéim.<br>
                • Tar éis gach rothlaithe, is féidir leat seiceáil an n-oibríonn hionsá anois.<br>
                • Is minic gurb é seo an réiteach is tapúla – bain triail as ar dtús!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Leid:</strong> Má thagann tú ar leathanaigh rothlaithe go minic, is féidir leat an rabhadh sa dialóg hionsá a cheilt go buan.<br>
                D'fhéadfadh an suíomh a bheith éagsúil ansin – ná húsáid an rogha seo ach amháin má tá na hiarmhairtí ar eolas agat.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Ailínigh leathanaigh",
        'menu_rotate_normalize_tooltip': "Rothlaigh leathanach nó athshocraigh go 0°",
        'normalize_current_page': "Tabhair an leathanach reatha go dtí seasamh díreach (socraigh go 0°)",
        'normalize_all_pages': "Tabhair gach leathanach go dtí seasamh díreach (socraigh go 0°)",
        'page_normalized': "Cuireadh leathanach {0} go dtí seasamh díreach.",
        'all_pages_normalized': "Cuireadh gach leathanach go dtí seasamh díreach.",
        'page_already_upright': "Tá leathanach {0} díreach cheana féin.",
        'all_pages_already_upright': "Tá gach leathanach díreach cheana féin.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>Níl aon téacs inchuardaithe sa PDF.</p><p>Ar mhaith leat OCR a dhéanamh chun onnmhairiú go {0}?</p>",
        'export_ocr_voice': "Níl aon téacs sa PDF. Teastaíonn OCR chun onnmhairiú go {0}.",
        'export_no_ocr_possible': "Ní féidir onnmhairiú gan OCR. Déan OCR tríd an roghchlár le do thoil.",
        'ocr_failed_export_not_possible': "Theip ar OCR. Ní féidir onnmhairiú a dhéanamh.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "Osclófar an PDF i Réamhamharc. Tosaigh an próiseas priontála ansin le do thoil.",
        'print_preview_manual': "Osclaíodh an PDF. Rith an t-ordú priontála de láimh le do thoil (m.sh. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Cumaisc PDFanna",
        'merge_pdfs': "Cumaisc PDFanna",
        'merge_progress_title': "PDFanna á gcumasc...",
        'merge_pdfs_list': "PDFanna in ord (Tarraing agus scaoil le socrú)",
        'merge_add_pdf': "Cuir PDF leis",
        'merge_remove': "Bain",
        'merge_move_up': "Suas",
        'merge_move_down': "Síos",
        'merge_pdfs_info': "💡 Leid: Is féidir leat an t-ord a athrú trí tharraing agus scaoileadh",
        'merge_no_pdfs': "Níor roghnaíodh aon PDF. Cliceáil ar 'Cuir PDF leis'.",
        'merge_info': "{0} PDF roghnaithe (thart ar {1} leathanach)",
        'merge_open_file': "Oscail comhad",
        'merge_merge': "Cumaisc",
        'merge_error': "Earráid agus cumasc á dhéanamh",
        'merge_min_two_pdfs_error': "Roghnaigh dhá chomhad PDF ar a laghad le cumasc le do thoil.",
        'merge_select_pdfs': "Roghnaigh PDFanna le cumasc",
        'merge_error_file': "Earráid agus próiseáil á déanamh",
        'merge_cancelled': "Cuireadh an cumasc ar ceal",
        'merge_preparing': "Ag ullmhú...",
        'merge_processing': "Ag próiseáil PDF {0} as {1}",
        'merge_saving': "Ag sábháil an PDF chumaiscthe...",
        'merge_complete': "Déanta!",
        'merge_success_title': "D'éirigh le cumasc",
        'merge_success_voice': "Cumascadh {0} PDF go rathúil.",
        'merge_success_message': "Cumascadh {0} PDF go rathúil.\n\nTá {1} leathanach sa doiciméad nua anois.\n\nComhad nua:\n{2}\n\nSuíomh sábhála:\n{3}\n{2}\n\nAr mhaith leat an PDF seo a oscailt?",
        'replace_file_title': "An comhad a chur in ionad?",
        'replace_file_message': "Tá PDF oscailte cheana féin. Ar mhaith leat é a chur in ionad an chomhaid nua?",
        'btn_yes': "Tá",
        'btn_no': "Níl",
        'filename_merge_suffix': "cumaiscthe",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Ag oscailt {0}...",
        'progress_merge_reading': "Ag léamh {0}...",
        'progress_merge_adding': "Ag cur {0} leathanach leis...",
        'progress_merge_optimizing': "Ag optamú PDF...",
        'progress_merge_writing': "Ag scríobh PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "an PDF a dhúnadh",
        'action_close_window': "an fhuinneog a dhúnadh",
        'action_open_new_pdf': "PDF nua a oscailt",
        'action_quit_app': "an feidhmchlár a fhágáil",
        'changes_saved': "Sábháladh na hathruithe.",
        'file_close_title': "Dún comhad PDF",
        'save_before_action': "Ar cheart na hathruithe a shábháil roimh {0}? Tá nó Níl?",
        'save_before_action_voice': "Ar cheart na hathruithe a shábháil roimh {0}? Tá nó Níl?",
        'save_before_close_question': "Ar cheart na hathruithe a shábháil roimh dhúnadh? Tá nó Níl?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF inchuardaigh cruthaithe:\n\n{0}\n\n<b>Bain triail eile as más gá",
        "ocr_rotate_title": "Ailínigh leathanaigh roimh OCR",
        "ocr_rotate_question": "Tá leathanaigh rothlaithe sa PDF.\nAr mhaith leat gach leathanach a ailíniú go 0° roimh OCR?\nCuireann sé seo feabhas suntasach ar aithint téacs.",
        "ocr_rotate_yes": "Sea, ailínigh",
        "ocr_rotate_no": "Níl, tosaigh OCR díreach",
        "ocr_rotate_voice": "Tá leathanaigh rothlaithe sa PDF. Ar cheart gach leathanach a ailíniú roimh OCR?",
        "ocr_not_performed_message": "Níl aon téacs i láthair. Déan OCR le do thoil (roghchlár \"Eagar\" → \"Déan OCR\" nó eochair Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Socruithe OCR",
        "ocr_language_btn": "Roghnaigh teanga OCR",
        "ocr_language": "Teanga(ocha) OCR",
        "ocr_language_current": "Teanga reatha:",
        "ocr_param_info": "Eolas faoin bparaiméadar",

        "ocr_force_ocr_label": "Cuir OCR i bhfeidhm go héigeantach",
        "ocr_deskew_label": "Ceartaigh claonta",
        "ocr_clean_label": "Glan íomhá",
        "ocr_oversample_label": "Taifeach (DPI)",
        "ocr_pagesegmode_label": "Deighilt leathanaigh",
        "ocr_oem_label": "Mód inneall OCR",
        "ocr_optimize_label": "Comhbhrú PDF",
        "ocr_jobs_label": "Próisis chomhthreomhara",
        "ocr_verbose_label": "Mionsonraí loga",

        "ocr_force_ocr_tooltip": "Cuir OCR i bhfeidhm go héigeantach ar gach leathanach, fiú má tá téacs ann cheana",
        "ocr_deskew_tooltip": "Ailínigh scananna claonta go huathoibríoch",
        "ocr_clean_tooltip": "Bain torann agus earraí saorga as an íomhá",
        "ocr_oversample_tooltip": "Méadaigh íomhá roimh OCR go dtí an DPI seo",
        "ocr_pagesegmode_tooltip": "Cinneann sé conas a roinntear an leathanach ina réimsí téacs",
        "ocr_oem_tooltip": "Roghnaíonn sé inneall OCR Tesseract",
        "ocr_optimize_tooltip": "Leibhéal comhbhrú an aschuir PDF",
        "ocr_jobs_tooltip": "Líon na bpróiseas comhthreomhar OCR",
        "ocr_verbose_tooltip": "Leibhéal mionsonraí an aschuir loga",
        "ocr_settings_explain_btn": "Míniú",

        "ocr_force_ocr_explain": "Cuireann sé aithint téacs i bhfeidhm go héigeantach ar <b>gach</b> leathanach, fiú má tá téacs ann cheana.\n\nMoltar: <b>Ar</b> do PDFanna scanáilte, <b>As</b> do PDFanna dúchasacha a bhfuil téacs ann cheana.",

        "ocr_deskew_explain": "Ceartaíonn sé scananna atá beagán claonta (suas go dtí thart ar 5°).\n\nMoltar: <b>Ar</b> do dhoiciméid scanáilte, <b>As</b> má tá na leathanaigh foirfe díreach cheana.",

        "ocr_clean_explain": "Baintear torann, poncanna agus earraí saorga beaga as an íomhá.\n<TÁBHACHTACH:</b> I gcás téacsanna Araibise, Téalainnise nó Vietneaimise a bhfuil diacriticí orthu (poncanna os cionn/faoi bhun litreacha) ba chóir an rogha seo a <b>dhíghníomhachtú</b>, ar shlí eile d'fhéadfaí carachtair thábhachtacha a chailleadh.",

        "ocr_oversample_explain": "Méadaíonn sé an íomhá <b>roimh</b> aithint téacs go dtí an DPI sonraithe.<br><br>• <b>72-150 DPI:</b> An-tapa, ach ráta aitheantais íseal<br>• <b>200-300 DPI:</b> Raon optamach (Réamhshocrú: 300)<br>• <b>400+ DPI:</b> Ar éigean aitheantas níos fearr, ach comhaid i bhfad níos mó<br><br>Moltar: 300 DPI do scriptí casta (Araibis, Sínis, Seapáinis), 200 DPI do theangacha an Iarthair.",

        "ocr_pagesegmode_explain": "Cinneann sé conas a roinneann Tesseract an leathanach ina réimsí téacs.\n\n• <b>3 - Uathoibríoch (Réamhshocrú):</b> Maith do leaganacha amach measctha\n• <b>4 - Colún aonair:</b> Do théacsanna aoncholúin\n• <b>5 - Bloc ingearach:</b> Do scriptí ingearacha (Seapáinis, Sínis)\n• <b>6 - Bloc téacs aonfhoirmeach:</b> Optamach do théacs sreabhach gan cholúin\n• <b>11 - Íomhá amh:</b> Do scananna bochta / lámhscríbhneoireacht\n\nMoltar: <b>6</b> do dhoiciméid téacs shimplí, <b>3</b> do leaganacha amach casta.",

        "ocr_oem_explain": "Roghnaíonn sé inneall OCR Tesseract.\n\n• <b>0 - Legacy:</b> Seaniompar (tapa, ach chomh cruinn)\n• <b>1 - LSTM:</b> Inneall néarach (níos moille, ach níos cruinne)\n• <b>2 - Legacy + LSTM:</b> Comhcheanglaíonn sé an dá thoradh\n• <b>3 - Réamhshocrú (LSTM is fearr):</b> An rogha is fearr don chuid is mó de na cásanna\n\nMoltar: <b>3</b> don uas-chruinneas aitheantais.",

        "ocr_optimize_explain": "Comhbhrúitear an t-aschur PDF.\n\n• <b>0:</b> Gan optamú (an próiseáil is tapúla)\n• <b>1:</b> Optamú éadrom (comhréiteach maith)\n• <b>2:</b> Optamú measartha\n• <b>3:</b> Optamú láidir (an comhad is lú, ach níos moille)\n\nMoltar: <b>1</b> do ghnáthúsáid.",

        "ocr_jobs_explain": "Líon na bpróiseas comhthreomhar le haghaidh OCR.\n\n• <b>1:</b> Mall, ach an tomhaltas cuimhne is ísle\n• <b>4-8:</b> Optamach do phróiseálaithe ilchroí nua-aimseartha\n• <b>12+:</b> Ar éigean próiseáil níos tapúla le tomhaltas ard cuimhne\n\nMoltar: Líon croíleacáin LAP (m.sh. <b>4</b> ar chórais 4-chroí).",

        "ocr_verbose_explain": "Leibhéal mionsonraí aschuir loga sa chonsól.\n\n• <b>0:</b> Gan aschur\n• <b>1:</b> Dul chun cinn agus teachtaireachtaí stádais\n• <b>2:</b> Aschur mionsonraithe\n• <b>3:</b> Aschur dífhabhtaithe iomlán (an-mhór)\n\nMoltar: <b>1</b> do ghnáthoibriú.",

        "ocr_reset_title": "Socruithe athshocraithe",
        "ocr_reset_message": "Athshocraíodh gach socrú OCR go dtí na réamhshocruithe.",
        "info_tooltip": "Tuilleadh eolais faoin bparaiméadar seo",
        "ocr_reset_defaults": "Athshocraigh go réamhshocruithe",

        "ocr_psm_0": "Uathoibríoch (Inneall Legacy)",
        "ocr_psm_1": "Braiteadh uathoibríoch colún",
        "ocr_psm_3": "Uathoibríoch (Réamhshocrú)",
        "ocr_psm_4": "Colún aonair",
        "ocr_psm_5": "Bloc ingearach",
        "ocr_psm_6": "Bloc téacs aonfhoirmeach",
        "ocr_psm_7": "Líne téacs aonair",
        "ocr_psm_8": "Focal aonair",
        "ocr_psm_11": "Íomhá amh (gan anailís leagan amach)",

        "ocr_oem_0": "Inneall Legacy (tapa)",
        "ocr_oem_1": "Inneall LSTM (néarach, cruinn)",
        "ocr_oem_2": "Legacy + LSTM comhcheangailte",
        "ocr_oem_3": "Réamhshocrú (LSTM is fearr)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Teanga(ocha) OCR...",
        "ocr_language_title": "Roghnaigh teanga(ocha) OCR",
        "ocr_language_instruction": "Roghnaigh an teanga(ocha) le haghaidh aithint téacs (OCR).\nRabhadh: Téann ilteangacha ar chostas feidhmíochta agus cruinnis!\nFaigheann tú na torthaí is fearr má roghnaíonn tú teanga amháin.",
        "ocr_language_predefined": "Teaglaim réamhshainithe",
        "ocr_language_custom": "Saincheaptha...",
        "ocr_language_selected": "Teangacha OCR roghnaithe",
        "ocr_language_changed": "Athraíodh teanga OCR go {0}",
        "ocr_language_auto_detect": "Braitear teangacha atá ar fáil go huathoibríoch.",
        "ocr_language_none_found": "Níor aimsíodh aon sonraí teanga Tesseract! Suiteáil pacáistí teanga le do thoil (m.sh. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Roghnú teanga saincheaptha",
        "ocr_language_available": "Teangacha atá ar fáil (suiteáilte):",
        "ocr_language_select_hint": "Roghnaigh teanga amháin nó níos mó:",
        "ocr_language_confirm": "Cuir i bhfeidhm",
        "ocr_language_reset": "Athshocraigh go réamhshocrú (deu+eng+vie)",
        "ocr_language_priorities": "Teangacha molta (réamhshuiteáilte):",

        "select_all_languages": "Roghnaigh go léir",
        "clear_all_languages": "Glan roghnú",
        "install_language_packs": "Suiteáil pacáistí teanga atá in easnamh...",
        "install_hint": "💡 Leid: Níl gach teanga suiteáilte ar do chóras. Gheobhaidh tú cabhair le suiteáil tríd an gcnaipe seo.",
        "ocr_language_install_title": "Suiteáil pacáistí teanga Tesseract",

        "ocr_missing_languages": "Pacáistí teanga OCR atá in easnamh",
        "ocr_missing_languages_message": "Níl na teangacha roghnaithe seo a leanas suiteáilte ar do chóras:\n\n{0}\n\nSuiteáil na pacáistí teanga atá in easnamh le do thoil (féach cabhair faoi 'Cabhair suiteála').\n\nAr mhaith leat an chabhair suiteála a oscailt anois?",
        "ocr_missing_languages_voice": "Pacáistí teanga in easnamh. Suiteáil na teangacha atá in easnamh le do thoil.",
        "ocr_install_help_now": "Oscail cabhair",
        "ocr_continue_anyway": "Bain triail as mar sin féin",
        "ocr_language_error_title": "Earráid teanga OCR",
        "ocr_language_error_message": "Earráid le linn aithint téacs: {0}\n\nSeiceáil do shocruithe teanga OCR (Socruithe → Teanga OCR).",
        "ocr_install_help_button": "Cabhair suiteála",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Suiteáil pacáistí teanga Tesseract</p>

        <p>Chun go n-oibreoidh OCR i dteanga ar leith, ní mór na sonraí teanga comhfhreagracha a bheith suiteáilte ar do chóras. Lean na treoracha do do chóras oibriúcháin:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Oscail <strong>Teirminéal</strong> (Finder → Cláir → Fóntais → Teirminéal).</li>
        <li>Suiteáil gach teanga atá ar fáil le:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (D'fhéadfadh sé seo cúpla nóiméad a ghlacadh.)</li>
        <li>Nó ach teangacha aonair (m.sh. Vítneaimis):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Le leaganacha reatha Homebrew, b'fhéidir go mbeadh gá <code>*.traineddata</code> a íoslódáil de láimh (féach thíos).</li>
        <li>Tar éis suiteála: Dún an dialóg seo agus oscail roghnú teanga OCR arís – beidh na teangacha nua le feiceáil go huathoibríoch.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Oscail teirminéal (Ctrl+Alt+T).</li>
        <li>Suiteáil an teanga inmhianaithe, m.sh. do Vítneaimis:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Cóid teanga thábhachtacha: <code>deu</code> (Gearmáinis), <code>eng</code> (Béarla), <code>vie</code> (Vítneaimis), <code>spa</code> (Spáinnis), <code>fra</code> (Fraincis), <code>ita</code> (Iodáilis), <code>nld</code> (Ollainnis), <code>fin</code> (Fionlainnis), <code>swe</code> (Sualainnis), <code>nor</code> (Ioruais).</li>
        <li>Taispeáin gach pacáiste atá ar fáil:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (de láimh)</p>
        <ol>
        <li>Íoslódáil na comhaid <code>*.traineddata</code> inmhianaithe ó:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (m.sh. <code>vie.traineddata</code> do Vítneaimis).</li>
        <li>Cóipeáil na comhaid go fillteán teanga Tesseract, de ghnáth:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Coigeartaigh de réir suiteála aonair.)</li>
        <li>Atosaigh an feidhmchlár (nó athoscail roghnú teanga OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Rogha eile do gach córas</p>
        <ul>
        <li>Suiteáil <strong>OCRmyPDF</strong> agus <strong>Tesseract</strong> le bainisteoir pacáiste de do rogha féin. Tá roinnt teangacha caighdeánacha (Béarla, Gearmáinis, Fraincis) i bhformhór na suiteálacha cheana féin.</li>
        <li>Is féidir teangacha atá in easnamh a shuiteáil am ar bith – ní liostaíonn roghnú teanga OCR ach na teangacha atá ann i ndáiríre.</li>
        </ul>

        <hr>
        <p><b>✅ Tar éis suiteála:</b> Ní gá an feidhmchlár a atosú – beidh na teangacha nua-churtha le feiceáil láithreach ar an liosta.</p>
        <p><b>📖 Cabhair le cóid teanga:</b> Tá liosta iomlán ar fáil i <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">doiciméadú Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Clófhoireann Noto Sans",
        "info_noto_font_voice": "Treoir suiteála do chlófhoireann Noto Sans",
        "btn_info_noto_font_install": "Eolas cló",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Conas clófhoireann saor in aisce Noto ó Google a shuiteáil</h2>

        <p>Is clófhoireann foinse oscailte iad <strong>clónna Noto</strong> ó Google. Is é a gcuspóir gan <em>"aon tófú"</em> a fheiceáil (.ie. gan boscaí folmha □) agus gach carachtar ó chaighdeán Unicode a thaispeáint i gceart. Is iad an breisiú idéalach d'fheidhmchláir a chaithfidh téacsanna a thaispeáint i go leor teangacha difriúla.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Suiteáil ar macOS</h3>

        <p><strong>Modh 1: Le Homebrew (do dhaoine chun cinn)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Modh 2: Trí "Font Book" (Molta)</strong></p>

        <ol>
        <li>Íoslódáil an pacáiste cló oifigiúil:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Bain an comhad ZIP</li>
        <li>Cóipeáil comhaid chuig <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Suiteáil ar Windows (10 & 11)</h3>

        <p><strong>Modh 1: Microsoft Store (Molta)</strong><br>
        Cuardaigh "Google Noto Fonts" nó "Noto Sans" agus cliceáil <strong>Suiteáil</strong>.</p>

        <p><strong>Modh 2: Suiteáil de láimh</strong></p>

        <ol>
        <li>Íoslódáil:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Bain ZIP</li>
        <li>Roghnaigh comhaid .ttf / .otf</li>
        <li>Cliceáil ar dheis → <strong>Suiteáil</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        nó<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Ainm\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Suiteáil ar Linux</h3>

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

        <p>Fíorú:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Bainistigh leathanaigh chun doiciméid",
        "bookmark_add": "Cuir leabharmharc leis",
        "bookmark_add_tooltip": "Sábháil an leathanach reatha mar leabharmharc",
        "bookmark_remove": "Bain leabharmharc",
        "bookmark_remove_tooltip": "Scrios an leabharmharc marcáilte",
        "bookmark_remove_all": "Bain go léir",
        "bookmark_remove_all_tooltip": "Scrios gach leabharmharc den PDF seo",
        "bookmark_jump": "Téigh go leabharmharc",
        "bookmark_jump_tooltip": "Téigh go dtí an leathanach roghnaithe",
        "bookmark_name": "Ainm",
        "bookmark_page": "Leathanach",
        "bookmark_no_bookmarks": "Níl aon leabharmharc i láthair.\nCliceáil 'Cuir leis' chun an leathanach reatha a shábháil mar leabharmharc.",
        "bookmark_added": "Leabharmharc do leathanach {0} curtha leis: {1}",
        "bookmark_removed": "Leabharmharc bainte: {0}",
        "bookmark_all_removed": "Baineadh gach leabharmharc.",
        "bookmark_name_default": "Leathanach {0}",
        "bookmark_name_prompt": "Ainm don leabharmharc:\n(giorrófar téacs fada go 50 carachtar)",
        "bookmark_name_prompt_title": "Ainm an leabharmharc",
        "bookmark_confirm_remove_all": "An bhfuil tú cinnte gur mhaith leat gach {0} leabharmharc a bhaint?",
        "menu_bookmarks": "Leabharmharcanna",
        "bookmark_manage": "Bainistigh leabharmharcanna",
        "bookmark_next": "An chéad leabharmharc eile",
        "bookmark_prev": "Leabharmharc roimhe seo",
        "bookmark_page_display": "Leathanach {0}",
        "bookmark_exists": "Tá leabharmharc don leathanach seo leis an ainm seo ann cheana.",
        "bookmark_select_first": "Roghnaigh leabharmharc ar dtús.",
        "bookmark_confirm_remove": "An bhfuil tú cinnte gur mhaith leat an leabharmharc 'Leathanach {0}: {1}' a bhaint?",
        "bookmark_jumped_to": "Léim go leabharmharc '{0}' ar leathanach {1}.",
        "bookmark_jumped_to_voice": "Leabharmharc {0}, leathanach {1}",
        "btn_close": "Dún",

        "bookmark_list": "Do leabharmharcanna",
        "bookmark_rename": "Athainmhnigh leabharmharc",
        "bookmark_rename_tooltip": "Athraigh ainm an leabharmharc roghnaithe",
        "bookmark_rename_title": "Athainmhnigh leabharmharc",
        "bookmark_rename_prompt": "Ainm nua don leabharmharc ar leathanach {0}:\n(uasmhéid 50 carachtar)",
        "bookmark_renamed": "Athainmníodh leabharmharc '{0}' go '{1}'.",
        "bookmark_item_tooltip": "Leathanach {0}: {1}\nCliceáil faoi dhó chun léim",
        "bookmark_name_exists_question": "Tá leabharmharc leis an ainm '{0}' ar an leathanach seo cheana.\nAthainmnigh mar sin féin?",

        "context_bookmarks": "Leabharmharcanna",
        "context_bookmark_add_here": "Cuir leabharmharc leis an leathanach seo",
        "context_bookmarks_existing": "Leabharmharcanna atá ann cheana:",
        "context_bookmarks_jump": "Téigh go leabharmharc:",
        "context_bookmarks_none": "Níl aon leabharmharc i láthair",
        "context_bookmarks_clear_all": "Bain gach {0} leabharmharc",

        "bookmark_search_placeholder": "Cuardaigh leabharmharcanna... (ainm nó leathanach)",
        "bookmark_search_results": "Aimsíodh %d leabharmharc do \"%s\"",
        "bookmark_no_search_results": "Níor aimsíodh aon leabharmharc do \"%s\"",
        "bookmark_no_search_results_label": "Níl aon toradh do \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Cuir in eagar meiteashonraí PDF",
        "metadata_title": "Teideal",
        "metadata_title_placeholder": "Teideal an doiciméid",
        "metadata_title_tooltip": "Teideal an doiciméid (taispeántar é sa bharra teidil)",
        "metadata_author": "Údar",
        "metadata_author_placeholder": "Ainm an údair",
        "metadata_author_tooltip": "Cruthaitheoir an doiciméid",
        "metadata_subject": "Ábhar",
        "metadata_subject_placeholder": "Ábhar an doiciméid",
        "metadata_subject_tooltip": "Cur síos gairid ar an ábhar",
        "metadata_keywords": "Eochairfhocail",
        "metadata_keywords_placeholder": "Eochairfhocail, scartha le camóga",
        "metadata_keywords_tooltip": "Eochairfhocail chun an doiciméad a chatagóiriú",
        "metadata_creator": "Cruthaitheoir",
        "metadata_creator_placeholder": "Feidhmchlár a chruthaigh an PDF",
        "metadata_creator_tooltip": "Na bogearraí lenar cruthaíodh an doiciméad",
        "metadata_producer": "Léiritheoir",
        "metadata_producer_placeholder": "Feidhmchlár a thiontaigh an PDF",
        "metadata_producer_tooltip": "Na bogearraí a thiontaigh an PDF",
        "metadata_creation_date": "Dáta cruthaithe",
        "metadata_creation_date_tooltip": "Dáta cruthaithe an doiciméid",
        "metadata_mod_date": "Dáta modhnaithe",
        "metadata_mod_date_tooltip": "Dáta an mhodhnuithe dheireanaigh",
        "metadata_pdf_info": "📄 Eolas PDF",
        "metadata_pages": "Líon leathanach",
        "metadata_file_size": "Méid comhaid",
        "metadata_pdf_version": "Leagan PDF",
        "metadata_encrypted": "Criptithe",
        "metadata_encrypted_yes": "Tá (cosanta ag pasfhocal)",
        "metadata_encrypted_no": "Níl",
        "metadata_reload": "📂 Athlódáil ó PDF",
        "metadata_reset": "Diúltú d'athruithe",
        "metadata_reloaded": "Athlódáladh meiteashonraí ón PDF.",
        "metadata_reset_done": "Athshocraíodh gach réimse meiteashonraí.",
        "metadata_no_file": "Níor lódáladh aon chomhad PDF.",
        "metadata_save_error": "Earráid agus meiteashonraí á sábháil",
        "metadata_saved": "Sábháladh meiteashonraí go rathúil.",
        "metadata_pdf_version_unknown": "PDF (anaithnid)",
        "metadata_saved_message": "Sábháladh na meiteashonraí go rathúil.",
        "metadata_saved_voice": "Meiteashonraí sábháilte.",

        "metadata_custom": "🔧 Meiteashonraí saincheaptha",
        "metadata_custom_placeholder": "{\n  \"mo_réimse\": \"mo_luach\",\n  \"réimse_eile\": 123\n}",
        "metadata_custom_tooltip": "Formáid JSON do mheiteashonraí saincheaptha (roghnach)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Teimpléad \"{0}\" roghnaithe - Cliceáil faoi dhó chun a chur isteach",
        "text_use_template": "Úsáid bloc téacs",
        "text_type": "Cineál",
        "text_search_templates": "Cuardaigh blocanna téacs...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Eolas onnmhairithe / allmhairithe",
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

        <h3>📦 Cad a onnmhairítear? (Forbhreathnú)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Gnáthshocruithe feidhmchláir</span></li>
            <li class="detail">• Mód Dorcha/Solas</li>
            <li class="detail">• Aisiompú mód dorcha d'íomhánna</li>
            <li class="detail">• Luach tairsí liath</li>
            <li class="detail">• Teanga</li>
            <li class="detail">• Céiméadracht fuinneoige</li>
            <li class="detail">• Mód súmála</li>
            <li class="detail">• Nascleanúint (Barra nascleanúna infheicthe)</li>
            <li class="detail">• Aschur cainte (ar/as)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Socruithe cúltaca</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Ainmniú comhad (Stampa ama, Deighilteoir, Iarmhíreanna)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Socruithe do chuir isteach ar</span></li>
            <li class="detail">• Sínithe</li>
            <li class="detail">• Téacs &amp; blocanna téacs</li>
            <li class="detail">• Croiseanna, íomhánna agus cruthanna</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Socruithe OCR</span></li>
            <li class="detail">• Teanga</li>
            <li class="detail">• Cuir OCR i bhfeidhm go héigeantach · Mód leathanaigh</li>
            <li class="detail">• Réamhphróiseáil íomhá: Ceartaigh claonta, Glan, Fhorshampláil</li>
            <li class="detail">• Líon na bpostanna comhthreomhara</li>
            <li class="detail">• Mód aisiompaithe</li>
            <li class="detail">• Luach tairsí liath</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Leabharmharcanna</span></li>
            <li class="detail">• Gach leabharmharc in aghaidh comhad PDF (Leathanach, Ainm, Am cruthaithe)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bunachar sonraí pasfhocal</span></li>
            <li class="detail">• Pasfhocail PDF sábháilte (criptithe nó gnáth-théacs de rogha)</li>
            <li class="detail">• Hash pasfhocal máistir (má tá sé socraithe)</li>
            <li class="detail">• Sonraí fíorúcháin</li>
        </ul>

        <h4>⚠️ Nótaí tábhachtacha</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Agus tú ag allmhairiú:</strong>
            <ul>
                <li><span class="warning">➜ Scríobhfar thar GACH socrú reatha go hiomlán</span></li>
                <li>• Tá atosú an fheidhmchláir éigeantach</li>
                <li>• Cuirfear sínithe, blocanna téacs agus leabharmharcanna atá ann cheana in ionad</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Pasfhocal máistir agus mód onnmhairithe:</strong>
            <ul>
                <li>• Nuair a bhíonn pasfhocal máistir gníomhach, is féidir leat rogha a dhéanamh:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dhíchriptigh</strong></span> (tá pasfhocail i ngnáth-théacs sa ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Criptithe</strong></span> (ní féidir iad a léamh ach le pasfhocal máistir ar an gcóras sprice)</li>
                <li>• Stóráiltear hash an phasfhocail mháistir <strong>i gcónaí</strong> criptithe</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Fógra slándála:</strong>
            <ul>
                <li>• Tá sonraí íogaire sa chomhad ZIP onnmhairithe (<strong>pasfhocail, leabharmharcanna, sínithe</strong>)</li>
                <li>• Coinnigh go slán é (m.sh. USB criptithe, bainisteoir pasfhocal)</li>
                <li>• Má chailleann tú an comhad, cailltear pasfhocail PDF sábháilte go neamh-inchúlghairthe</li>
            </ul>
        </div>

        <h4>📁 Formáid onnmhairithe</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Sábháiltear na socruithe i gcomhad ZIP amháin:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Tá an <code>settings.json</code> iomlán (ó do chumraíocht) sa ZIP seo, chomh maith le comhaid íomhá sínithe leabaithe agus pasfhocail criptithe.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Sínithe - Treoir",
        'signature_guide_html': """
        📝 <strong>Sínithe - Treoir Thapa</strong><br>
        <ul>
        <li>Socraigh pasfhocal máistir</li>
        <li>Cumraigh sínithe sa roghchlár <em>Socruithe</em> (méid, stampa ama, …)</li>
        <li>Ionsáigh le <strong>CHLICEADH DHEIS</strong> ag an suíomh atá uait (pasfhocal máistir riachtanach uair amháin in aghaidh an tseisiúin)</li>
        <li>Bog an síniú leis an luch nó na heochracha saighde</li>
        <li>Ionsáigh il-sínithe i ndiaidh a chéile</li>
        <li>Saincheap gach síniú ina n-aonar</li>
        <li>Diúltaigh síniú aonair</li>
        <li>Sábháil / diúltaigh gach síniú ag an am céanna</li>
        <li>De rogha air sin, is féidir an barra roghchláir a úsáid freisin.</li>
        </ul>
        """,
        'signature_guide_voice': "Treoir thapa do shínithe. Socraigh pasfhocal máistir. Cumraigh sínithe i socruithe. Ionsáigh le cliceadh deis.",

        'image_guide_title': "Íomhánna a Ionsáil - Treoir",
        'image_guide_html': """
        📷 <strong>Íomhánna a Ionsáil i bPDF - Treoir Thapa</strong><br>
        <ol>
        <li>Cliceadh deis ag an suíomh atá uait</li>
        <li><em>„Íomhá a ionsáil“</em> → Roghnaigh íomhá</li>
        <li>Suiteáil an íomhá: Tarraing leis an luch</li>
        <li>Coigeartaigh méid: Tarraing ag na coirnéil/imeall</li>
        <li>Coinnigh cóimheas na gceamh: Eochair <strong>[A]</strong></li>
        <li>Tuilleadh coigeartuithe: Cliceadh deis ar an íomhá</li>
        </ol>
        <p><strong>Leid:</strong> Sa roghchlár comhthéacs, is féidir leat na socruithe a choigeartú.</p>
        """,
        'image_guide_voice': "Treoir thapa d'íomhánna. Cliceadh deis, íomhá a ionsáil, roghnaigh. Suiteáil le luch, coigeartaigh méid ag coirnéil. Cóimheas ceamh le heochair A.",

        'form_guide_title': "Cruthanna a Ionsáil - Treoir",
        'form_guide_html': """
        📐 <strong>Cruthanna a Ionsáil i bPDF - Treoir Thapa</strong><br>
        <ol>
        <li>Roghnaigh cineál crutha (dronuilleog, éilips, líne, saighead)</li>
        <li>Cliceáil ar shuíomh:
            <ul>
            <li>Do dhronuilleog/éilips: Cuireann cliceáil amháin an cruth</li>
            <li>Do líne/shaighead: Dhá chliceáil do phointe tosaigh agus deiridh</li>
            </ul>
        </li>
        <li>Suiteáil an cruth: Tarraing leis an luch</li>
        <li>Coigeartaigh méid: Tarraing ag na coirnéil/imeall</li>
        <li>Sábháil an cruth: <strong>Iontráil</strong></li>
        <li>Diúltaigh an cruth: <strong>Éalú</strong></li>
        <li>Tuilleadh coigeartuithe: Cliceadh deis ar an gcruth</li>
        </ol>
        <p><strong>Leid:</strong> Sa roghchlár comhthéacs, is féidir leat na socruithe a choigeartú.</p>
        """,
        'form_guide_voice': "Treoir thapa do chruthanna. Roghnaigh cineál crutha. Do dhronuilleog nó éilips cliceáil uair amháin, do líne nó saighead dhá uair. Suiteáil le luch, coigeartaigh méid ag coirnéil. Sábháil le Iontráil, diúltaigh le Éalú.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "roimhe seo",
        "btn_next_result": "seo chugainn",
        "ocr_text_window": "Fuinneog téacs OCR",
        "bookmark_existing": "Leabharmharcanna atá ann cheana",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Comparáid OCR Mac - Windows",
        'ocr_method_mac_win_title': "Difríochtaí OCR idir Mac agus Windows",
        'ocr_method_mac_win_voice': "Tá Mac níos fearr",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Difríochtaí idir macOS agus Windows</strong></p>

        <p><strong>macOS (molta)</strong></p>
        <p>Uirlis:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Toradh:</p>
        <ul>
        <li>PDF inchuardaigh le téacs leabaithe a choinníonn an leagan amach bunaidh den chuid is mó.</li>
        </ul>
        <p>Buntáistí:</p>
        <ul>
        <li>Cáilíocht fhíorthaitheach aitheantais téacs (fiú ar leathanaigh chlaonta).</li>
        <li>Caomhnú grafaicí veicteora agus clónna.</li>
        <li>Barra dul chun cinn GUI trí mheastóireacht fhophróisis.</li>
        <li>Smacht iomlán ar gach paraiméadar OCR (Deskew, Clean, Oversample, barrfheabhsú).</li>
        <li>Tá cuardach téacs ar fáil go díreach sa phríomhfhuinneog (amharc PDF).</li>
        </ul>
        <p>Míbhuntáistí:</p>
        <ul>
        <li>Éilíonn uirlisí córais bhreise (ocrmypdf, Ghostscript, unpaper, pngquant – san áireamh sa bhraisle aipe).</li>
        <li>Láimhseáil earráidí níos casta (marbhghlais, teorainneacha ama).</li>
        </ul>

        <p><strong>Windows (rogha eile chobhsaí)</strong></p>
        <p>Uirlis:</p>
        <ul>
        <li>pytesseract (nasc díreach le Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Toradh:</p>
        <ul>
        <li>PDF inchuardaigh a fhreagraíonn go hamhairc d'PDF íomhá, ach atá inchuardaigh tríd an téacs trédhearcach.</li>
        </ul>
        <p>Buntáistí:</p>
        <ul>
        <li>Ní thagann aon cheann i gcuimhne dom faoi láthair.</li>
        </ul>
        <p>Míbhuntáistí:</p>
        <ul>
        <li>Is é an PDF go bunúsach íomhá le téacs dofheicthe; d'fhéadfadh an leagan amach a bheith beagán difriúil i gcás doiciméad casta (colúin, táblaí).</li>
        <li>Níl aon cheartú uathoibríoch ar chlaonadh (--deskew) ná glanadh íomhá (--clean).</li>
        <li>Nuashonraítear barra dul chun cinn GUI go garbh amháin bunaithe ar líon na leathanach próiseáilte.</li>
        <li>Tá luas OCR beagán níos moille (toisc go bpróiseáiltear gach leathanach ar leithligh).</li>
        <li>Dírítear cuardach téacs ar fhuinneog téacs OCR.</li>
        </ul>

        <p><strong>Comhthréithe</strong></p>
        <ul>
        <li>Cruthaíonn an dá mhodh PDF inchuardaigh san eolaire chéanna leis an gcomhad foinse.</li>
        <li>Is féidir na socruithe OCR (teanga, DPI, mód deighilte leathanaigh, mód inneall OCR) a chumrú tríd an OCRSettingsDialog agus bíonn siad i bhfeidhm sa dá chur i bhfeidhm.</li>
        </ul>

        <p><strong>Moladh:</strong></p>
        <ul>
        <li>macOS: Tugann an dénártha ocrmypdf na torthaí is fearr – Ceannaigh Mac agus bain úsáid as an leagan (PDFDarkView do Macanna le sliseanna Apple Silicon nó Intel). Tá torthaí OCR níos fearr ná mar atá faoi Windows!</li>
        <li>Windows: Úsáid an réiteach pytesseract. Tá sé cobhsaí agus soláthraíonn sé cáilíocht leordhóthanach don chuid is mó de dhoiciméid.</li>
        </ul>

        <p><strong>Nóta tábhachtach:</strong></p>
        <ul>
        <li>Tá an dá leagan comhtháite go hiomlán sa chomhéadan úsáideora – ní thugann an t-úsáideoir aon difríocht faoi deara.</li>
        <li>Cinneann an clár go huathoibríoch cén t-inneall OCR a úsáidfear bunaithe ar an gcóras oibriúcháin.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Cruthaigh síniú (ó scanadh)",
        "signature_create_title": "Roghnaigh síniú scanta (PDF/Íomhá)",
        "image_pdf_filter": "Íomhánna agus PDF",
        "signature_pdf_empty": "Níl aon leathanach sa PDF.",
        "signature_created_success": "Síniú cruthaithe go rathúil: {0}",
        "signature_create_error": "Earráid agus síniú á chruthú:\n{0}",
        "rembg_missing": "Níl rembg suiteáilte.\nSuiteáil le do thoil: pip install rembg\nEarráid: {0}",
        "signature_name_title": "Ainm comhaid don síniú",
        "signature_name_message": "Cuir isteach ainm comhaid don síniú nua (sábhálfar é mar PNG le cúlra trédhearcach):",
        "signature_name_label": "Ainm comhaid:",
        "signature_name_voice": "Cuir isteach ainm comhaid don síniú",
        "signature_processing": "Próiseáil ar siúl...",
        "signature_creation_title": "Síniú á chruthú",
        "signature_overwrite_warning": "Tá an comhad '{0}' ann cheana. Forscríobh?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Ullmhaigh PDF don síniú",
        "signature_prepare_instruction":"Roghnaigh PDF ina bhfuil síniú scanta ar leathanach amháin, le do thoil.\n\nBaintear amach an aithint is fearr má:\n• Tá an síniú scríofa le dúch dubh (peann liathróid nó mínloineadóir) ar pháipéar bán.\n• Tá an síniú sa tríú cuid uachtarach de leathanach A4 atá folamh ar shlí eile.\n• Scanaíodh an PDF le 300 dpi ar a laghad.\n• Tá an síniú soiléir agus ní ró-tanaí.\n• Níl aon phatrúin chúlra nó línte cur isteach ann.",
        "signature_prepare_voice":"Roghnaigh PDF le síniú scanta, le do thoil. Tabhair aird ar chaighdeán maith agus codarsnacht.",
        "sig_thickness_label":"Tiús líne:",
        "sig_thickness_normal":"Gnáth (tanaí)",
        "sig_thickness_bold":"Tiubh (molta)",
        "sig_thickness_very_bold":"An-tiubh",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Teangacha GUI agus OCR a chur leis - Treoir",
        'language_guide_title': "Teangacha GUI agus OCR a chur leis",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Íoslódáil an comhad aistriúcháin atá uait <code>translations_xy.py</code> ó<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        agus cuir san eolaire seo a leanas é:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Oscail do bhrabhsálaí gréasáin.</li>
        <li>Téigh go: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Cuardaigh ar imeall deas an scáileáin "Releases" agus roghnaigh an ceann atá marcáilte <strong>"latest"</strong>.</li>
        <li>Ar an leathanach scaoilte seo chugainn, íoslódáil an comhad <code>Source Code.zip</code> ag bun an leathanaigh.</li>
        <li>Dízipáil an comhad ZIP.</li>
        <li>Sa fhillteán dízipáilte, aimsigh gach comhad teanga atá uait agus cóipeáil iad san eolaire:<br/>
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
        "menu_watermark":"Ionsáigh comhartha uisce",
        "fullpage_text_watermark_title":"Téacs mar chomhartha uisce",
        "fullpage_image_watermark_title":"Íomhá mar chomhartha uisce",
        "filename_with_watermark":"_le_comhartha_uisce",
        "watermark_text":"Téacs:",
        "watermark_text_placeholder":"Do théacs comhartha uisce...",
        "watermark_font_family":"Cló:",
        "watermark_font_size":"Méid cló:",
        "watermark_format":"Formáidiú:",
        "watermark_bold":"Trom",
        "watermark_italic":"Cló iodálach",
        "watermark_color":"Dath:",
        "watermark_choose_color":"Roghnaigh dath...",
        "watermark_opacity":"Teimhneacht / Trédhearcacht:",
        "watermark_direction":"Treo léitheoireachta:",
        "watermark_direction_l_r":"Clé → Deas",
        "watermark_direction_bl_tr":"Thíos clé → Thuas deas",
        "watermark_direction_tl_br":"Thuas clé → Thíos",
        "watermark_direction_b_t":"Thíos → Thuas",
        "watermark_direction_t_b":"Thuas → Thíos",
        "watermark_preview":"Réamhamharc:",
        "watermark_preview_sample":"Sampla téacs",
        "watermark_empty_text":"Cuir isteach téacs le do thoil.",
        "watermark_applied":"Cuireadh an comhartha uisce i bhfeidhm ar gach leathanach.",
        "watermark_saved":"Comhartha uisce sábháilte.",
        "image_scale":"Méid:",
        "image_preview":"Réamhamharc íomhá:",
        "no_image_selected":"Níor roghnaíodh aon íomhá",
        "browse":"Brabhsáil...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Cinsireachtaí",
        "redact_add_black": "Cinsireacht (dubh)",
        "redact_add_white": "Cinsireacht (bán / scrios)",
        "redact_added_black": "Cinsireacht dhubh curtha leis",
        "redact_added_white": "Cinsireacht bhán curtha leis",
        "redact_apply_all": "Cuir gach cinsireacht i bhfeidhm agus sábháil",
        "redact_discard_all": "Déan dearmad ar gach cinsireacht",
        "redact_discard": "Déan dearmad ar an gcinsireacht seo",
        "no_redactions": "Níl aon chinsireachtaí ann",
        "redact_confirm_title": "Cuir cinsireachtaí i bhfeidhm go buan",
        "redact_confirm_message": "Rabhadh: Scriosfar na limistéir mharcáilte go buan (dubh nó bán).\nCruthófar cúltaca (má tá sé cumasaithe).\n\nLean ar aghaidh?",
        "redact_apply": "Sea, cinsirigh anois",
        "redact_saved": "Cuireadh {0} cinsireacht(í) i bhfeidhm agus sábháladh iad.",
        "redact_saved_voice": "Cuireadh {0} cinsireacht(í) i bhfeidhm",
        "redact_error": "Earráid le linn cinsireachta",
        "filename_redacted":"_cinsithe",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Ionsáigh uimhreacha leathanaigh',
        'page_numbers_format': 'Formáid uimhreach:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arabach)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Rómhánach beag)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Rómhánach mór)',
        'page_numbers_format_letter': 'A, B, C ... (Litreacha)',
        'page_numbers_format_custom': 'Saincheaptha',
        'page_numbers_custom_pattern': 'Patrún:',
        'page_numbers_custom_placeholder': 'm.sh. "Leathanach {nummer}" nó "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Úsáid {nummer} don uimhir leathanaigh reatha agus {total} don iomlán',
        'page_numbers_position': 'Ionad:',
        'page_numbers_pos_tl': 'Thuas clé',
        'page_numbers_pos_tc': 'Thuas lár',
        'page_numbers_pos_tr': 'Thuas deas',
        'page_numbers_pos_ml': 'Lár clé',
        'page_numbers_pos_mc': 'Lárnaithe',
        'page_numbers_pos_mr': 'Lár deas',
        'page_numbers_pos_bl': 'Thíos clé',
        'page_numbers_pos_bc': 'Thíos lár',
        'page_numbers_pos_br': 'Thíos deas',
        'page_numbers_margins': 'Imill:',
        'page_numbers_margin_x': 'Fad cothrománach:',
        'page_numbers_margin_y': 'Fad ingearach:',
        'page_numbers_range': 'Raon leathanach:',
        'page_numbers_all_pages': 'Gach leathanach',
        'page_numbers_custom_range': 'Raon saincheaptha',
        'page_numbers_from': 'Ó:',
        'page_numbers_to': 'Go:',
        'page_numbers_progress': 'Ag ionsáil uimhreacha leathanaigh...',
        'page_numbers_start': 'Ag tosú ar ionsáil uimhreacha leathanaigh...',
        'page_numbers_cancel': 'Ionsáil uimhreacha leathanaigh curtha ar ceal',
        'page_numbers_success': 'Cuireadh na huimhreacha leathanaigh leis go rathúil.\n\nAr mhaith leat an PDF nua a oscailt?\n\n{0}',
        'page_numbers_complete': 'Cuireadh uimhreacha leathanaigh leis',
        'page_numbers_error_format': 'Earráid agus uimhreacha leathanaigh á n-ionsáil: {0}',
        'page_numbers_content_type': 'Cineál ábhair:',
        'page_numbers_tab_simple': 'Uimhir shimplí',
        'page_numbers_tab_range': 'Leathanach X de Y',
        'page_numbers_tab_date': 'Dáta',
        'page_numbers_tab_custom': 'Téacs saor',
        'page_numbers_range_format': 'Formáid:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Leathanach {aktuell} de {gesamt}',
        'page_numbers_range_custom': 'Saincheaptha',
        'page_numbers_range_placeholder': 'm.sh. "Leathanach {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Formáid dáta:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Eanáir 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Saincheaptha',
        'page_numbers_date_placeholder': 'm.sh. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Ionad:',
        'page_numbers_date_before': 'Dáta roimh uimhir leathanaigh',
        'page_numbers_date_after': 'Dáta tar éis uimhir leathanaigh',
        'page_numbers_date_only': 'Dáta amháin (gan uimhir leathanaigh)',
        'page_numbers_custom_text': 'Téacs saincheaptha:',
        'page_numbers_custom_placeholder_text': 'Úsáid {seite} don uimhir leathanaigh agus {gesamt} don iomlán\nm.sh. "Rúnda - Leathanach {seite}" nó "{seite} de {gesamt}"',
        "filename_with_page_number":"_le_uimhir_leathanaigh",
        "filename_with_page_declaration":"_le_raitheas_leathanaigh",
        "filename_with_pagenumber":"_le_uimhir_leathanaigh",
        "filename_with_date":"_le_dáta",
        "filename_with_my_page_declaration":"_le_raitheas_saincheaptha",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Athruithe gan sábháil",
        "unsaved_changes_message_darkmode": "Tá ionsáithe gan sábháil ann.\nAr mhaith leat iad a shábháil sula ndéanann tú athrú?",
        "save_and_switch": "Sábháil agus athraigh",
        "discard_and_switch": "Athraigh anois",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Easpórtáil leathanaigh mar íomhánna',
        'export_images_menu': 'Easpórtáil mar íomhánna (PNG/JPEG)',
        'export_images_format': 'Formáid íomhá:',
        'export_images_dpi': 'Taifeach (DPI):',
        'export_images_quality': 'Cáilíocht JPEG:',
        'export_images_range': 'Raon leathanach:',
        'export_images_all_pages': 'Gach leathanach',
        'export_images_custom_range': 'Raon saincheaptha',
        'export_images_from': 'Ó:',
        'export_images_to': 'Go:',
        'export_images_options': 'Roghanna:',
        'export_images_single_files': 'Gach leathanach mar chomhad ar leith',
        'export_images_subfolder': 'Easpórtáil go fochomhadlann',
        'export_images_subfolder_info': 'Go dtí an fochomhadlann "ainmPDF_íomhánna"',
        'export_images_same_folder': 'Sa chomhadlann chéanna leis an PDF',
        'export_images_apply_darkmode': 'Cuir socruithe PDFDarkView i bhfeidhm (Modh Dorcha)',
        'export_images_target_folder': 'Comhadlann sprioc:',
        'export_images_browse': 'Brabhsáil...',
        'export_images_preview': 'Réamhamharc:',
        'export_images_preview_info': 'Roghnaigh socruithe don easpórtáil',
        'export_images_preview_info_detail': '{0} leathanach mar {1}\nTaifeach: {2} DPI\nAinm comhaid: {3}\n{4}',
        'export_images_select_folder': 'Roghnaigh comhadlann sprioc',
        'export_images_start': 'Ag tosú ar easpórtáil íomhánna...',
        'export_images_progress': 'Ag easpórtáil íomhánna...',
        'export_images_saving': 'Ag sábháil leathanach {0} de {1}...',
        'export_images_success': 'D\'éirigh leis an easpórtáil!\n\nSábháladh {0} íomhá in:\n{1}',
        'export_images_complete': 'Easpórtáil íomhánna críochnaithe',
        'export_images_open_folder': '📁 Oscail comhadlann',
        'export_images_cancel': 'Easpórtáil íomhánna curtha ar ceal',
        'export_images_error_format': 'Earráid agus íomhánna á n-easpórtáil: {0}',
        'export_images_pdf2image_missing': 'Níl an leabharlann "pdf2image" suiteáilte.\n\nSuiteáil í le do thoil le:\npip install pdf2image\n\nMaidir le Windows, teastaíonn Poppler uait freisin:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Tiontú PDF/A do chártlannú fadtéarmach',
        'pdfa_menu': 'Tiontú PDF/A (oiriúnach do chártlann)',
        'pdfa_info': 'Tiontaíonn an PDF go formáid PDF/A.\n\nTá PDF/A deartha go speisialta do chártlannú fadtéarmach agus cinntíonn sé go dtaispeánfar an doiciméad i gceart sa todhchaí.',
        'pdfa_standard': 'Caighdeán PDF/A:',
        'pdfa_standard_select': 'Leagan:',
        'pdfa_1': 'PDF/A-1 (simplí, comhoiriúnach go forleathan)',
        'pdfa_2': 'PDF/A-2 (nua-aimseartha, comhbhrú níos fearr)',
        'pdfa_3': 'PDF/A-3 (an leagan is déanaí, ceadaíonn ceangaltáin)',
        'pdfa_standards_explanation': '📖 Míniú ar na caighdeáin:\n\n'
            '• PDF/A-1: Bunúsach, comhoiriúnach le córais níos sine (thart ar 2005)\n'
            '• PDF/A-2: Níos nua-aimseartha, comhbhrú níos fearr, tacaíocht do thrédhearcacht (thart ar 2011)\n'
            '• PDF/A-3: An leagan is déanaí, ceadaíonn leabú ceangaltán comhad (thart ar 2013)\n\n'
            'Moladh: Is comhbhabhtáil mhaith é PDF/A-2 idir comhoiriúnacht agus gnéithe nua-aimseartha.',
        'pdfa_options': 'Roghanna:',
        'pdfa_compress_enable': 'Comhbhrúigh PDF (comhad níos lú)',
        'pdfa_metadata_preserve': 'Coinnigh meiteashonraí (teideal, údar, srl.)',
        'pdfa_target_folder': 'Comhadlann sprioc:',
        'pdfa_browse': 'Brabhsáil...',
        'pdfa_select_folder': 'Roghnaigh comhadlann sprioc',
        'pdfa_ocr_info_unknown': '🔍 Níorbh fhéidir ábhar téacs a sheiceáil.',
        'pdfa_ocr_info_not_needed': '✅ Téacs ar fáil - níl OCR ag teastáil.\nIs féidir PDF/A a chruthú go díreach.',
        'pdfa_ocr_info_recommended': '⚠️ Níor aimsíodh téacs leordhóthanach.\n\nMaidir le PDFanna inchuardaithe, molaimid OCR a reáchtáil ar dtús.\nNóta: Oibríonn PDF/A gan OCR freisin - ach ní bheidh an téacs inchuardaithe.',
        'pdfa_ocr_info_error': '❌ Earráid le linn seiceála: {0}',
        'pdfa_start': 'Ag tosú ar thiontú PDF/A...',
        'pdfa_progress': 'Tiontú PDF/A ar siúl...',
        'pdfa_success': 'D\'éirigh leis an tiontú PDF/A!\n\nSábháladh mar:\n{0}\n\nAr mhaith leat an PDF nua a oscailt?',
        'pdfa_complete': 'Tiontú PDF/A críochnaithe',
        'pdfa_cancel': 'Tiontú PDF/A curtha ar ceal',
        'pdfa_error_format': 'Earráid le linn thiontú PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Níl an leabharlann "ocrmypdf" suiteáilte.\n\nSuiteáil í le do thoil le:\npip install ocrmypdf',
        'btn_convert': 'Tiontaigh',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optamaigh PDF (laghdaigh méid comhaid)',
        'optimize_menu': 'Optamaigh PDF (méid comhaid)',
        'optimize_info': 'Laghdaíonn méid an chomhaid PDF trí mhodhanna optamaithe éagsúla.\n\nDá airde an leibhéal comhbhrú, is ea is lú an comhad - le caillteanas cáilíochta féideartha in íomhánna.',
        'optimize_level': 'Leibhéal comhbhrú:',
        'optimize_level_low': 'Íseal (tapa, coigilteas beag)',
        'optimize_level_medium': 'Meánach (comhbhabhtáil mhaith)',
        'optimize_level_high': 'Ard (coigilteas mór)',
        'optimize_level_maximum': 'Uasmhéid (coigilteas uasta, mall)',
        'optimize_level_explanation': 'Moladh: Is comhbhabhtáil mhaith é "Meánach" idir luas agus méid comhaid.',
        'optimize_options': 'Roghanna:',
        'optimize_compress_images': 'Comhbhrúigh íomhánna (laghdaigh cáilíocht JPEG)',
        'optimize_clean_objects': 'Bain réada nár úsáideadh',
        'optimize_preserve_metadata': 'Coinnigh meiteashonraí (teideal, údar, srl.)',
        'optimize_image_quality': 'Cáilíocht íomhá:',
        'optimize_range': 'Raon leathanach:',
        'optimize_all_pages': 'Gach leathanach',
        'optimize_custom_range': 'Raon saincheaptha',
        'optimize_from': 'Ó:',
        'optimize_to': 'Go:',
        'optimize_target_folder': 'Comhadlann sprioc:',
        'optimize_browse': 'Brabhsáil...',
        'optimize_select_folder': 'Roghnaigh comhadlann sprioc',
        'optimize_info_box': 'Faisnéis',
        'optimize_info_text': 'Féadfaidh optamú roinnt nóiméad a ghlacadh do PDFanna móra.\n\nSábháiltear íomhánna le cáilíocht laghdaithe, rud a d\'fhéadfadh méid an chomhaid a laghdú go suntasach.',
        'optimize_start': 'Ag tosú ar optamú PDF...',
        'optimize_progress': 'Ag optamú PDF...',
        'optimize_cancel': 'Optamú PDF curtha ar ceal',
        'optimize_complete': 'Optamú PDF críochnaithe',
        'optimize_error_format': 'Earráid le linn optamú PDF:\n\n{0}',
        'optimize_success_message': 'D\'éirigh leis an optamú PDF!\n\nSábháladh mar:\n{0}\n\nRoimhe: {1}\nTar éis: {2}\nCoigilteas: {3:.1f}%\n\n{4}\n\nAr mhaith leat an PDF optamaithe a oscailt?',
        'optimize_success_message_no_size': 'D\'éirigh leis an optamú PDF!\n\nSábháladh mar:\n{0}\n\nNíl faisnéis faoin méid ar fáil.\n\nAr mhaith leat an PDF optamaithe a oscailt?',
        'optimize_result_positive': 'Laghdaíodh an comhad {0:.1f}%.',
        'optimize_result_zero': 'Níor athraigh méid an chomhaid.',
        'optimize_result_negative': 'Mhéadaigh an comhad {0:.1f}%.\nSkipeáladh an optamú, coinníodh an bun-chomhad.',
        'btn_optimize': 'Tosaigh optamú',
        'filename_optimize_low_suffix': '_optamaithe_íseal',
        'filename_optimize_medium_suffix': '_optamaithe',
        'filename_optimize_high_suffix': '_optamaithe_ard',
        'filename_optimize_maximum_suffix': '_optamaithe_uasta',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Bearr PDF',
        'crop_menu': 'Bearr PDF (Crop)',
        'crop_range': 'Cuir i bhfeidhm ar:',
        'crop_all_pages': 'Gach leathanach',
        'crop_current_page': 'An leathanach reatha amháin',
        'crop_values': 'Luachanna bearradh (i bpointí):',
        'crop_left': 'Clé:',
        'crop_right': 'Deas:',
        'crop_top': 'Thuas:',
        'crop_bottom': 'Thíos:',
        'crop_presets': 'Réamhshocruithe:',
        'crop_preset_white': 'Braith imill bhána',
        'crop_reset': 'Athshocraigh',
        'crop_mouse_hint': '🖱️ Tarraing dronuilleog chun an limistéar a roghnú go garbh.\nAnsin is féidir leat na luachanna a choigeartú go cruinn sna SpinBoxes.\nNíl coigeartú láimhe leis an luchóg indéanta.',
        'crop_apply': 'Bearr',
        'crop_scope_all': 'Gach leathanach',
        'crop_scope_current': 'Leathanach reatha',
        'crop_new_size': 'Méid nua: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Níl aon PDF luchtaithe',
        'crop_preview_error': 'Earráid agus réamhamharc á lódáil',
        'crop_start': 'Ag tosú ar bhearradh...',
        'crop_progress': 'Ag bearradh PDF...',
        'crop_success': 'Bearradh PDF go rathúil!\n\nSábháladh mar:\n{0}\n\nAr mhaith leat an PDF bearraithe a oscailt?',
        'crop_complete': 'Bearradh críochnaithe',
        'crop_cancel': 'Bearradh curtha ar ceal',
        'crop_error_format': 'Earráid le linn bearradh:\n\n{0}',
        'filename_crop_suffix': '_bearraithe',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Leathanaigh PDF (Flatten)',
        'flatten_menu': 'Leathanaigh PDF (Flatten)',
        'flatten_info': 'Leathanaigh PDF "dhónn" gach eilimint inathraithe isteach in ábhar an leathanaigh.\n\nIna dhiaidh sin, níl réimsí foirme, nótaí, téacsanna, crosa, sínithe, íomhánna agus cruthanna inathraithe ina n-aonar a thuilleadh.',
        'flatten_explanation_title': '📖 Cad chuige a bhfuil sé seo go maith?',
        'flatten_explanation_text': 'Tá gá le leathanaigh sna cásanna seo a leanas:\n\n'
            '• 📄 Ba mhaith leat an doiciméad a ullmhú le haghaidh priontála\n'
            '• 🔒 Ba mhaith leat cosc a chur ar dhuine réimsí foirme a athrú\n'
            '• 📎 Ba mhaith leat nótaí agus tuairimí a "leabú" go buan sa doiciméad\n'
            '• 🖼️ Ba mhaith leat téacsanna, crosa, sínithe, íomhánna agus cruthanna a ancaireacht go buan sa doiciméad\n'
            '• 📦 Ba mhaith leat an comhad a ullmhú le haghaidh cartlannaithe\n\n'
            'Déanann leathanaigh an PDF níos lú agus cuireann siad cosc ar eilimintí a bhogadh nó a scriosadh de thaisme.',
        'flatten_what_title': 'Cad a leathanaítear?',
        'flatten_what_list': '• ✅ Réimsí foirme (réimsí téacs, boscaí seiceála, cnaipí)\n'
            '• ✅ Nótaí (tuairimí, béim, nótaí)\n'
            '• ✅ Forleagan (téacsanna, crosa, sínithe, íomhánna, cruthanna)',
        'flatten_options': 'Roghanna:',
        'flatten_forms': 'Leathanaigh réimsí foirme',
        'flatten_annotations': 'Leathanaigh nótaí',
        'flatten_overlays': 'Leathanaigh forleagan (téacsanna, crosa, sínithe, íomhánna, cruthanna)',
        'flatten_target_folder': 'Comhadlann sprioc:',
        'flatten_browse': 'Brabhsáil...',
        'flatten_select_folder': 'Roghnaigh comhadlann sprioc',
        'flatten_warning': '⚠️ Tábhachtach: Is próiseas dochúlaithe é leathanaigh!\n\nTar éis leathanaigh, ní féidir eilimintí inathraithe a athrú nó a scriosadh ina n-aonar a thuilleadh.\nCruthaigh cúltaca roimh ré más gá.',
        'flatten_apply': 'Leathanaigh',
        'flatten_start': 'Ag tosú ar leathanaigh...',
        'flatten_progress': 'Ag leathanaigh PDF...',
        'flatten_success': 'Leathanaíodh PDF go rathúil!\n\nSábháladh mar:\n{0}\n\nAr mhaith leat an PDF leathanaithe a oscailt?',
        'flatten_complete': 'Leathanaigh críochnaithe',
        'flatten_cancel': 'Leathanaigh curtha ar ceal',
        'flatten_error_format': 'Earráid le linn leathanaigh:\n\n{0}',
        'filename_flatten_suffix': '_leathanaithe',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Forleagan PDF (Overlay)',
        'overlay_menu': 'Forleagan PDF (Overlay)',
        'overlay_info': 'Cuireann PDF amháin (forleagan) ar bharr PDF eile.\n\nCuirtear an PDF forleagain ar an mbun-PDF. Tá sé seo úsáideach le haghaidh comharthaí uisce, lógónna, ceannlitreacha nó stampaí.',
        'overlay_explanation_title': '📖 Cad chuige a bhfuil sé seo go maith?',
        'overlay_explanation_text': 'Tá gá le forleagan sna cásanna seo a leanas:\n\n'
            '• 🏢 Cuir lógó cuideachta mar chomhartha uisce ar gach leathanach\n'
            '• 📄 Cuir ceannlitir ar PDF bán\n'
            '• 🖊️ Cuir forleagan stampa ar dhoiciméad\n'
            '• 🔖 Cuir comhartha uisce ar gach leathanach\n'
            '• 📑 Cuir forleagan foirme ar theimpléad',
        'overlay_type': 'Cineál forleagain:',
        'overlay_type_fullpage': 'Leathanach iomlán (clúdaitheach)',
        'overlay_type_transparent': 'Leathanach iomlán (trédhearcach - molta)',
        'overlay_type_stamp': 'Stampa (ionadaithe)',
        'overlay_type_info_fullpage': '📄 Cuirtear an PDF forleagain go díreach ar an leathanach iomlán.\nIs féidir an cúlra bán a bhaint ionas go mbeidh an t-ábhar amháin le feiceáil.',
        'overlay_type_info_transparent': '🔍 Cuirtear an PDF forleagain ar an leathanach iomlán le cúlra trédhearcach.\nBaintear an cúlra bán go huathoibríoch - iontach do chomharthaí uisce agus lógónna!',
        'overlay_type_info_stamp': '🖊️ Cuirtear an PDF forleagain agus scálaítear é mar stampa.\nFoirfe do lógónna, stampaí nó sínithe ag suíomhanna ar leith.',
        'overlay_remove_background': 'Bain cúlra bán:',
        'overlay_remove_background_enable': 'Bain cúlra bán ón PDF forleagain (déanann an forleagan trédhearcach)',
        'overlay_remove_background_tooltip': 'Baineann réimsí bána ón PDF forleagain ionas go mbeidh an téacs thíos le feiceáil.',
        'overlay_threshold': 'Luach tairsí:',
        'overlay_threshold_hint': '(1-254, níos airde = baintear níos mó bán)',
        'overlay_select_file': 'Roghnaigh PDF forleagain:',
        'overlay_file_placeholder': 'Roghnaigh comhad PDF le haghaidh an fhorleagain le do thoil',
        'overlay_browse': 'Brabhsáil...',
        'overlay_select_overlay': 'Roghnaigh PDF forleagain',
        'overlay_range': 'Raon leathanach:',
        'overlay_all_pages': 'Gach leathanach',
        'overlay_custom_range': 'Raon saincheaptha',
        'overlay_from': 'Ó:',
        'overlay_to': 'Go:',
        'overlay_position': 'Ionad:',
        'overlay_position_center': 'Lár',
        'overlay_position_top_left': 'Thuas clé',
        'overlay_position_top_right': 'Thuas deas',
        'overlay_position_bottom_left': 'Thíos clé',
        'overlay_position_bottom_right': 'Thíos deas',
        'overlay_size': 'Méid:',
        'overlay_size_original': 'Méid bunaidh',
        'overlay_size_fit_page': 'Oiriúnú don leathanach',
        'overlay_size_custom': 'Saincheaptha (%)',
        'overlay_opacity': 'Trédhearcacht:',
        'overlay_target_folder': 'Comhadlann sprioc:',
        'overlay_browse_folder': 'Brabhsáil...',
        'overlay_select_folder': 'Roghnaigh comhadlann sprioc',
        'overlay_warning': '⚠️ Nóta: Cuirtear an PDF forleagain ar an mbun-PDF agus "dhónn" é isteach ann.\n\nNí féidir eilimintí an PDF forleagain a athrú ina n-aonar tar éis sábhála a thuilleadh.',
        'overlay_apply': 'Forleagan',
        'overlay_start': 'Ag tosú ar fhorleagan...',
        'overlay_progress': 'Ag forleagan PDF...',
        'overlay_success': 'Forleagadh PDF go rathúil!\n\nSábháladh mar:\n{0}\n\nAr mhaith leat an PDF forleagtha a oscailt?',
        'overlay_complete': 'Forleagan críochnaithe',
        'overlay_cancel': 'Forleagan curtha ar ceal',
        'overlay_error_format': 'Earráid le linn forleagan:\n\n{0}',
        'overlay_no_file': 'Níor roghnaíodh aon PDF forleagain.\n\nRoghnaigh comhad PDF le haghaidh forleagan le do thoil.',
        'filename_overlay_suffix': '_forleagtha',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Bain íomhánna as PDF',
        'extract_images_menu': 'Bain gach íomhá',
        'extract_images_info': 'Baineann gach íomhá as an PDF agus sábhálann sé iad mar chomhaid ar leith.\n\nSábháiltear na híomhánna ina bhformáid bhunaidh nó tiontaítear iad go formáid roghnaithe.',
        'extract_images_format': 'Formáid íomhá:',
        'extract_images_quality': 'Cáilíocht JPEG:',
        'extract_images_options': 'Roghanna:',
        'extract_images_subfolder': 'Bain go fochomhadlann ("ainmPDF_íomhánna")',
        'extract_images_unique': 'Íomhánna uathúla amháin (seachain dúblaigh)',
        'extract_images_range': 'Raon leathanach:',
        'extract_images_all_pages': 'Gach leathanach',
        'extract_images_custom_range': 'Raon saincheaptha',
        'extract_images_from': 'Ó:',
        'extract_images_to': 'Go:',
        'extract_images_target_folder': 'Comhadlann sprioc:',
        'extract_images_browse': 'Brabhsáil...',
        'extract_images_select_folder': 'Roghnaigh comhadlann sprioc',
        'extract_images_info_box': 'Faisnéis',
        'extract_images_info_text': 'Féadfaidh baint roinnt nóiméad a ghlacadh do PDFanna móra.\n\nSábháiltear íomhánna lena n-ainm bunaidh (leathanach_íomhá).',
        'extract_images_extract': 'Bain',
        'extract_images_start': 'Ag tosú ar bhaint...',
        'extract_images_progress': 'Ag baint íomhánna...',
        'extract_images_success': '✅ Baineadh íomhánna go rathúil!\n\nSábháladh {0} íomhá in:\n{1}',
        'extract_images_complete': 'Baint íomhánna críochnaithe',
        'extract_images_cancel': 'Baint curtha ar ceal',
        'extract_images_error_format': 'Earráid agus íomhánna á mbaint:\n\n{0}',
        'extract_images_open_folder': '📁 Oscail comhadlann',
        'extract_images_no_images': 'Níor aimsíodh aon íomhá sa PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Il-leathanaigh ar leathanach amháin (N-Up)',
        'nup_menu': 'Il-leathanaigh ar leathanach amháin (N-Up)',
        'nup_info': 'Eagraíonn il-leathanaigh PDF ar leathanach amháin.\n\nIontach le haghaidh priontaí dlútha, forbhreathnuithe nó bileoga.',
        'nup_layout': 'Leagan amach:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Réamhamharc:',
        'nup_preview_info': '{0} leathanach → {1} leathanach in aghaidh an bhileog → {2} bileog\nLeagan amach: {3}',
        'nup_order': 'Ord:',
        'nup_order_horizontal': 'Cothrománach (sraith ar shraith)',
        'nup_order_vertical': 'Ingearach (colún ar cholún)',
        'nup_order_horizontal_reverse': 'Cothrománach droim ar ais',
        'nup_order_vertical_reverse': 'Ingearach droim ar ais',
        'nup_range': 'Raon leathanach:',
        'nup_all_pages': 'Gach leathanach',
        'nup_custom_range': 'Raon saincheaptha',
        'nup_from': 'Ó:',
        'nup_to': 'Go:',
        'nup_options': 'Roghanna:',
        'nup_margins': 'Imill:',
        'nup_margin_between': 'Spásáil idir leathanaigh:',
        'nup_page_numbers': 'Ionsáigh uimhreacha leathanaigh',
        'nup_target_folder': 'Comhadlann sprioc:',
        'nup_browse': 'Brabhsáil...',
        'nup_select_folder': 'Roghnaigh comhadlann sprioc',
        'nup_create': 'Cruthaigh',
        'nup_start': 'Ag tosú ar N-Up...',
        'nup_progress': 'Ag cruthú N-Up...',
        'nup_success': 'Cruthaíodh N-Up go rathúil!\n\nSábháladh mar:\n{0}\n\nAr mhaith leat an PDF nua a oscailt?',
        'nup_complete': 'N-Up críochnaithe',
        'nup_cancel': 'N-Up curtha ar ceal',
        'nup_error_format': 'Earráid le linn N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Athraigh méid leathanaigh',
        'pagesize_menu': 'Athraigh méid leathanaigh',
        'pagesize_info': 'Athraíonn méid leathanaigh an PDF.\n\nOiriúnaítear an t-ábhar go huathoibríoch don mhéid nua.',
        'pagesize_format': 'Formáid:',
        'pagesize_select': 'Roghnaigh formáid chaighdeánach:',
        'pagesize_custom': 'Méid saincheaptha:',
        'pagesize_width': 'Leithead:',
        'pagesize_height': 'Airde:',
        'pagesize_orientation': 'Treoshuíomh:',
        'pagesize_portrait': 'Portráid',
        'pagesize_landscape': 'Tírdhreach',
        'pagesize_scale_options': 'Roghanna scála:',
        'pagesize_fit': 'Oiriúnú (coinnigh cóimheas gné)',
        'pagesize_stretch': 'Síneadh (saobhadh)',
        'pagesize_center': 'Lárnaigh (méid bunaidh)',
        'pagesize_range': 'Raon leathanach:',
        'pagesize_all_pages': 'Gach leathanach',
        'pagesize_custom_range': 'Raon saincheaptha',
        'pagesize_from': 'Ó:',
        'pagesize_to': 'Go:',
        'pagesize_target_folder': 'Comhadlann sprioc:',
        'pagesize_browse': 'Brabhsáil...',
        'pagesize_select_folder': 'Roghnaigh comhadlann sprioc',
        'pagesize_apply': 'Cuir i bhfeidhm',
        'pagesize_start': 'Ag tosú ar athrú méid leathanaigh...',
        'pagesize_progress': 'Ag athrú méid leathanaigh...',
        'pagesize_success': 'Athraíodh méid leathanaigh go rathúil!\n\nSábháladh mar:\n{0}\n\nAr mhaith leat an PDF nua a oscailt?',
        'pagesize_complete': 'Athrú méid leathanaigh críochnaithe',
        'pagesize_cancel': 'Athrú méid leathanaigh curtha ar ceal',
        'pagesize_error_format': 'Earráid agus méid leathanaigh á athrú:\n\n{0}',
        'pagesize_preview_info': 'Méid nua: {0} x {1} pt',
        'filename_pagesize_suffix': '_méid_nua',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Faisnéis PDF',
        'pdf_info_menu': 'Taispeáin faisnéis PDF',
        'pdf_info_voice': 'Ag taispeáint faisnéis PDF',
        'pdf_info_error': 'Earráid agus faisnéis PDF á taispeáint:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Taispeáin aicearraí méarchláir",
        "shortcuts_dialog_title": "Aicearraí Méarchláir",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 COMHAD</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Oscail PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Dún PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Sábháil mar...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Cosain doiciméad</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Priontáil</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Priontáil láithreach (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Scoir an feidhmchlár</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EASPÓRTÁIL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Easpórtáil mar Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Easpórtáil mar DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Easpórtáil mar TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Easpórtáil mar íomhánna (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Bain íomhánna</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PRÓISEÁIL DOICIMÉAD</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Il-leathanaigh)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Tiontú PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Leathanaigh PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Forleagan PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optamaigh PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ CUIR IN EAGAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Cuardaigh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Cuir leabharscéal leis</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Bainistigh leabharscéalta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>An chéad leabharscéal eile</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>An leabharscéal roimhe seo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Rith OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 BAINISTÍOCHT LEATHANACH</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rothlaigh an leathanach reatha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rothlaigh gach leathanach</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Gnásaigh an leathanach reatha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Gnásaigh gach leathanach</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Scrios leathanaigh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Bain leathanaigh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Ionsáigh leathanaigh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Bog leathanaigh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Cumaisc PDFanna</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Athraigh méid leathanaigh</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 IONSÁIGH</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Ionsáigh téacs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Ionsáigh cros</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Ionsáigh síniú 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Ionsáigh síniú 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Ionsáigh íomhá</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Ionsáigh dronuilleog</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ionsáigh éilips</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Ionsáigh líne</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Ionsáigh saighead</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Ionsáigh uimhreacha leathanaigh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Comhartha uisce téacs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Comhartha uisce íomhá</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ CINSIREACHTAÍ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Cinsireacht (dubh)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Cinsireacht (bán)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Cuir gach cinsireacht i bhfeidhm</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ CHUN CINN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Bearr PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Cuir meiteashonraí in eagar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ AMHARC</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Athraigh Modh Dorcha/Solas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Taispeáin fuinneog téacs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Leithead leathanaigh (Súmáil)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dhá leathanach (Súmáil)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Forbhreathnú (Súmáil)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ SOCRUITHE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Bainistíocht pasfhocal</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Socruithe OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Socruithe sínithe</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formáidiú ainmneacha comhad</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Easpórtáil socruithe</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Iompórtáil socruithe</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ FAISNÉIS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Taispeáin faisnéis PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Cas as/ar aschur gutha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Dírigh ar an mbarra roghchláir</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Leagan nua ar fáil",
        "update_available_message": "Tá leagan nua <b>{0}</b> ar fáil.\n\nTabhair cuairt ar an leathanach eisithe chun an nuashonrú a íoslódáil:\n{1}",
        "update_available_voice": "Leagan nua {0} ar fáil. Íoslódáil an nuashonrú ó leathanach GitHub.",
        "update_open_release": "Oscail leathanach eisithe",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Íoslódáil gach aistriúchán",
        "ask_download_all_translations": """Seachas Gearmáinis, Béarla agus Vítneaimis, tá {total_languages} teanga GUI eile ar fáil.\n\nAr cheart iad a sholáthar / a nuashonrú?\n\nNóta:\nIs féidir leat teangacha nach bhfuil gá leo a scriosadh de láimh níos déanaí sa chomhadlann:\n{translations_path}
        \nMá chealaíonn tú, is féidir leat na teangacha GUI a íoslódáil níos déanaí tríd an roghchlár 'Uirlisí → Nuashonraigh aistriúcháin'.""",
        "menu_update_translations": "Nuashonraigh aistriúcháin",
        "translations_updated": "Aistriúcháin nuashonraithe",
        "translations_update_success": "Nuashonraíodh {} aistriúchán go rathúil ({} nua, {} nuashonraithe).",
        "translations_update_error": "Earráid agus aistriúcháin á nuashonrú",
        "translations_update_no_changes": "Tá gach aistriúchán cothrom le dáta cheana féin.",
        "translations_update_offline": "Níl aon nasc idirlín ann. Níorbh fhéidir aistriúcháin a nuashonrú.",
        "translations_update_in_progress": "Tá aistriúcháin á nuashonrú sa chúlra...",
        "translations_downloading": "Ag íoslódáil aistriúchán...",
        "translations_path_hint": "Comhadlann úsáideora le haghaidh aistriúchán",
        "translations_update_not_available_title": "Níl nuashonrú ar fáil",
        "translations_update_not_available_message": """Níl nuashonrú aistriúchán ar fáil ach amháin sa leagan suiteáilte.\n\nSa mhodh forbartha, tá aistriúcháin cothrom le dáta cheana féin.""",
        "translations_update_no_internet_title": "Níl aon nasc idirlín ann",
        "translations_update_no_internet_message": """Níorbh fhéidir nasc idirlín a bhunú.\n\nNí féidir aistriúcháin a íoslódáil ó GitHub.\n\nRéitigh fhéideartha:
        • Seiceáil do nasc idirlín
        • Díchumasaigh aon bhalla dóiteáin go sealadach
        • Bain triail eile as níos déanaí
        \nIs féidir leat na haistriúcháin a íoslódáil de láimh ó GitHub freisin:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Tá nuashonrú ar siúl cheana féin",
        "btn_retry": "Bain triail eile as",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Fáilte go PDF Dark View",
        "welcome_title_not_supported": "Fáilte go PDF Dark View",
        "welcome_message": "Fáilte go PDF Dark View!\n\nAithníodh do theanga chórais mar '{language}'.\nAr mhaith leat an teanga seo a úsáid don chomhéadan úsáideora?\n\nIs féidir leat an teanga a athrú ag am ar bith trí 'Socruithe → Teanga'.",
        "welcome_message_language_not_available": "Fáilte go PDF Dark View!\n\nAithníodh do theanga chórais mar '{language}'.\nNíl an teanga seo suiteáilte go fóill.\n\nAr mhaith leat na haistriúcháin do {language} a íoslódáil anois ó GitHub?\n\n(Úsáidfear an teanga go huathoibríoch don chomhéadan úsáideora ansin.)",
        "welcome_message_language_not_supported": "Fáilte go PDF Dark View!\n\nAithníodh do theanga chórais mar '{language}'.\nAr an drochuair, níl aon aistriúcháin don teanga seo go fóill.\n\nTaispeánfar an comhéadan úsáideora i {fallback_language}.\n\nIs féidir leat an teanga a athrú ag am ar bith trí 'Socruithe → Teanga'.\nMás mian leat, is féidir leat aistriúchán a chur le do theanga féin:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Sea, bain úsáid as teanga an chórais",
        "welcome_keep_english": "Níl, coinnigh Béarla",
        "welcome_download_language": "Sea, íoslódáil {language}",

        # ============================================
        # 107. COSAIN LE DÉANAÍ
        # ============================================

        'menu_recent': 'Úsáidte le déanaí',
        'menu_recent_dirs': 'Comhlaí...',
        'menu_recent_files': 'Comhaid...',
        'recent_manage': 'Bainistigh...',
        'recent_enable_tracking': 'Sábháil cosáin le déanaí (príobháideachas)',
        'recent_enable_info': 'Díchumasaigh an rogha seo chun gan cosáin a shábháil',
        'recent_tracking_disabled': 'Rianú cosáin díchumasaithe',
        'recent_enabled': 'cumasaíodh',
        'recent_disabled': 'díchumasaíodh',
        'recent_tracking_status': 'Rianú cosáin {0}',
        'recent_dialog_title': 'Cosáin le déanaí',
        'recent_tab_directories': 'Comhlaí',
        'recent_tab_files': 'Comhaid',
        'recent_dirs_instruction': 'Cliceáil faoi dhó chun dialóg comhaid a oscailt sa chomhla',
        'recent_files_instruction': 'Cliceáil faoi dhó chun an PDF a oscailt go díreach',
        'recent_no_directories': '(níl aon chomhlaí sábháilte)',
        'recent_no_files': '(níl aon chomhaid sábháilte)',
        'recent_default_current': '⭐ Réamhshocrú: {0}',
        'recent_set_as_default': '⭐ Socraigh mar réamhshocrú',
        'recent_default_set_title': 'Comhla réamhshocraithe socraithe',
        'recent_default_set_message': 'Socraíodh an chomhla "{0}" mar réamhshocrú chun PDFanna a oscailt.',
        'recent_default_set_voice': 'Socraíodh comhla réamhshocraithe',
        'recent_directory_not_found': 'Comhla gan aimsiú',
        'recent_file_not_found': 'Comhad gan aimsiú',
        'recent_remove_selected': 'Bain',
        'recent_remove_title': 'Bain cosán',
        'recent_remove_confirm': 'An bhfuil tú cinnte gur mhaith leat an cosán "{0}" a bhaint as an liosta?',
        'recent_path_removed': 'Baineadh an cosán',
        'recent_clear_all': 'Bain uile',
        'recent_clear_title': 'Bain gach cosán',
        'recent_clear_confirm_type': 'An bhfuil tú cinnte gur mhaith leat gach {0} a scriosadh?',
        'recent_cleared': 'Glanadh an liosta',
        'recent_path_not_found_title': 'Cosán gan aimsiú',
        'recent_path_not_found_message': 'Níl an cosán "{0}" ann a thuilleadh.',
        'recent_open_file': 'Oscail comhad',
        'btn_open_recent': 'Oscail',
        'recent_open_file_question': 'Ar mhaith leat "{0}" a oscailt mar PDF?',
        'recent_not_pdf': 'Ní PDF é an comhad roghnaithe.',
        'recent_more_entries': 'Níos mó iontrálacha...',
        'btn_remove': 'Bain',
        'btn_clear': 'Glan uile',
        'recent_context_open': 'Oscail',
        'recent_context_reveal': 'Taispeáin sa Finder',
        'recent_context_set_default': '⭐ Socraigh mar réamhshocrú',
        'recent_context_open_terminal': '💻 Oscail Teirminéal',
        'recent_context_file_info': 'Eolas faoin gcomhad',
        'recent_context_open_with_default': '📄 Oscail le haip réamhshocraithe',
        'recent_context_remove': 'Bain as an liosta',
        'recent_context_clear_all': 'Bain uile',
        'recent_file_info_title': 'Eolas faoin gcomhad',
        'recent_file_info_name': 'Ainm',
        'recent_file_info_path': 'Cosán',
        'recent_file_info_size': 'Méid',
        'recent_file_info_modified': 'Athraithe',
        'recent_file_info_pages': 'Leathanaigh',
        'recent_error_reveal': 'Earráid ag oscailt sa Finder',
        'recent_error_terminal': 'Earráid ag oscailt an Teirminéil',
        'recent_error_info': 'Earráid ag fáil eolais faoin gcomhad',
        'open_user_data_folder': 'Taispeáin comhla sonraí an úsáideora',

        # ============================================
        # 108. LEATHANAIGH CHOTHROMA/CHORRA A SCRIOSADH
        # ============================================
        "pages_delete_even": "Scrios gach leathanach cothrom",
        "pages_delete_odd":  "Scrios gach leathanach corr",
        "progress_even_pages": "Ag scriosadh leathanach cothrom",
        "progress_odd_pages": "Ag scriosadh leathanach corr",
        "progress_mark_delete_even": "{} leathanach cothrom marcáilte le scriosadh",
        "progress_mark_delete_odd":  "{} leathanach corr marcáilte le scriosadh",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Tá an clár ag scor",

    }

