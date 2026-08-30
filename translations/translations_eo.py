# ============================================
# translations_eo.py - Esperanta vortaro por PDFDarkView
# Vollständig sortiert nach Kategorien
# ============================================

def load_esperanto_strings():
    """Lädt alle Esperanto-Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Ŝargi PDF",
        'btn_text_window': "Teksto OCR",
        'btn_first': "Unua paĝo",
        'btn_prev': "Antaŭa paĝo",
        'btn_next': "Sekva paĝo",
        'btn_last': "Lasta paĝo",
        'btn_print': "Presi",
        'btn_darkmode_light': "Hela reĝimo",
        'btn_darkmode_dark': "Malhela reĝimo",
        'btn_delete_pages': "Forigi paĝojn",
        'btn_extract_pages': "Eltiri paĝojn",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Nuligi",
        'btn_save': "Konservi",
        'btn_close': "Fermi",
        'btn_delete': "Forigi",
        'btn_delete_all': "Forigi ĉiujn",
        'btn_copy': "Kopii",
        'btn_export': "Eksporti",
        'btn_show': "Montri pasvorton",
        'btn_hide': "Kaŝi pasvorton",
        'btn_authenticate': "Aŭtentigi",
        'btn_settings': "Agordoj",
        'btn_protect': "Protekti",
        'btn_remove_password': "Forigi pasvorton",
        'btn_manage': "Administri pasvortojn",
        'btn_retry': "Provi denove",
        'btn_select_all': "Elekti ĉiujn",
        'btn_clear_selection': "Nuligi elekton",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Paĝo {0} el {1}",
        'page_count': "el {0}",
        'goto_page': "Iri al paĝo",
        'page_simple': "Paĝo {0}",
        'full_view_page': "Plena vido de paĝo {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Enigu serĉvorton + Enter",
        'search_results': "Trovaĵoj: {0} el {1}",
        'search_nav_hint': "Enter: sekva (Shift+Enter: antaŭa) trovaĵo",
        'search_no_results': "Neniu trovaĵo",
        'search_error': "Serĉa eraro",
        'search_active': "Serĉkampo aktiva",
        'search_closed': "Serĉo finita",
        'search_position': "Paĝo {0} {1}",
        'search_pos_top': "tute supre",
        'search_pos_upper': "supre",
        'search_pos_middle': "meze",
        'search_pos_lower': "malsupre",
        'search_pos_bottom': "tute malsupre",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Teksta rekonado sukcese finita!",
        'ocr_success_title': "OCR sukcesis",
        'ocr_success_message': "La dokumento nun estas serĉebla.",
        'ocr_failed': "OCR malsukcesis",
        'ocr_in_progress': "OCR okazas",
        'ocr_preparing': "Preparas PDF...",
        'ocr_analyzing': "Analizas PDF...",
        'ocr_optimizing': "Optimumigas bildon...",
        'ocr_recognizing': "Rekonas tekston...",
        'ocr_embedding': "Enigas tekston...",
        'ocr_finalizing': "Finias PDF...",
        'ocr_not_available': "OCR ne disponebla",
        'ocr_install_message': "OCR-iloj ne troviĝis.\n\nBonvolu instali:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR nepras",
        'ocr_question': "La PDF ne enhavas serĉeblan tekston.\nĈu vi volas fari OCR por ebligi {0}?",
        'ocr_perform': "Fari OCR",
        'ocr_later': "Poste",
        'ocr_starting': "Komencas garantian OCR...",
        'ocr_success_voice': "OCR sukcesis. PDF nun estas serĉebla.",
        'ocr_partial_success': "OCR estis farita, sed problemoj okazis dum anstataŭigo.\n\nLa serĉebla versio estas konservita kiel:\n{0}\n\nEraro: {1}",
        'ocr_partial_title': "OCR parte sukcesis",
        'ocr_partial_voice': "OCR farita, sed anstataŭigo malsukcesis.",
        'original_file': "Origina dosiero:",
        'old_size': "Malnova grandeco:    {0} bajtoj",
        'new_size': "Nova grandeco: {0} bajtoj",
        'size_change': "Ŝanĝo: {0}{1} bajtoj",
        'backup_created_file': "Kreita sekurkopio:\n{0}",
        'backup_not_created': "Sekurkopio: ne kreita (agordo malŝaltita)",
        'page_header': "=== Paĝo {0} ===\n{1}\n",
        'scanned_page_header': "=== Paĝo {0} (skanita) ===\n[Ĉi tiu paĝo enhavas nur skanitan tekston]\n[Bonvolu fari OCR permane]\n",
        'scanned_warning': "⚠️ SKANITA TEKSTO - OCR NEPRAS",
        'guaranteed_title': "Kreita serĉebla PDF",
        'guaranteed_message': "<b>Kreita serĉebla versio!</b>\n\nĈar aŭtomata OCR malsukcesis, oni kreis\nalternativan serĉeblan PDF:\n\n{0}\n\n<b>Ĉi tiu dosiero enhavas:</b>\n• Eltiritan tekston (se ekzistas)\n• Konsilojn por skanitaj paĝoj\n• Estas plene serĉebla",
        'guaranteed_voice': "Kreita serĉebla PDF.",
        'instruction_title': "INSTRUKCIO POR OCR",
        'instruction_file': "Origina dosiero: {0}",
        'instruction_text': "Aŭtomata teksta rekonado (OCR) malsukcesis.\nBonvolu fari OCR permane:\n\n1. PER OCRmyPDF (komandlinio):\n   ocrmypdf --force-ocr \"[DOSIERO]\" \"elig.pdf\"\n\n2. PER ADOBE ACROBAT (macOS/Windows):\n   • Malfermu PDF en Acrobat\n   • Iloj > Redakti PDF\n   • Elektu 'Rekoni tekston'\n\n3. PER PREVIEW (macOS):\n   • Malfermu PDF en Antaŭvido\n   • Dosiero > Eksporti...\n   • Kvarca filtrilo: 'Reduce File Size'\n   • Aktivigu 'Fari OCR'\n\n4. RETAJ OCR-SERVOJ:\n   • smallpdf.com/de/ocr-pdf\n   • ilovepdf.com/de/ocr-pdf\n   • adobe.com/de/acrobat/online/pdf-to-word.html",
        'instruction_created': "Kreita OCR-instrukcio",
        'instruction_created_message': "Detala instrukcio estas kreita:\n\n{0}\n\nSekvu la paŝojn por permana OCR.",
        'instruction_created_voice': "Kreita OCR-instrukcio.",
        'ocr_impossible': "OCR ne ebla",
        'ocr_impossible_message': "Ne eblis fari OCR.\n\nBonvolu prilabori '{0}' permane per OCR-programaro.",
        'ocr_impossible_voice': "OCR ne ebla. Bonvolu prilabori permane.",
        'emergency_title': "Kriza OCR",
        'emergency_message': "Kriza PDF kreita:\n\n{0}\n\nBonvolu prilabori ĉi tiun dosieron permane per OCR.",
        'emergency_voice': "Kriza PDF kreita. Bonvolu fari OCR permane.",
        'critical_error': "Kritika eraro",
        'critical_error_message': "Ne eblis startigi OCR.\n\nBonvolu restartigi la programon kaj\nkontroli la instalon de OCR.",
        'critical_error_voice': "Kritika OCR-eraro",
        'ocr_question_html': "<p>La PDF ne enhavas serĉeblan tekston.<p>Ĉu vi volas fari OCR por ebligi <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR nepras. La PDF ne enhavas serĉeblan tekston. Ĉu vi volas fari OCR por ebligi {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "neniu PDF ŝargita",
        'no_pdf_message': "Neniu PDF estas ŝargita",
        'pdf_not_found': "PDF-dosiero ne trovita",
        'file_size': "Dosiera grandeco",
        'bytes': "bajtoj",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Sekurkopio kreita",
        'backup_disabled': "Sekurkopio malŝaltita",
        'backup_activated': "Kreado de sekurkopio aktivigita",
        'backup_deactivated': "Kreado de sekurkopio malaktivigita",
        'backup_status': "Sekurkopio: {0}",
        'backup_on': "✔ aktivigita",
        'backup_off': "✘ malaktivigita",
        'close_pdf': "Fermas PDF: {0}",
        'pdf_not_found_format': "PDF-dosiero ne trovita: {0}",
        'error_pdf_load_format': "Eraro dum ŝargado de PDF: {0}",
        'load_failed_format': "Ŝargado malsukcesis:\n{0}",
        'decrypted_suffix': "(malĉifrita)",
        'decryption_failed': "Malĉifrado malsukcesis.",
        'decryption_error': "Eraro de malĉifrado",
        'decryption_success': "Sukcese malĉifrita",
        'decryption_success_message': "PDF estis malĉifrita kaj konservita kiel:\n\n{0}",
        'decryption_success_voice': "PDF malĉifrita kaj konservita.",
        'password_remove_error': "Eraro dum forigo de pasvorto",
        'save_unencrypted': "Konservi neĉifritan PDF kiel",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Konservi kiel...",
        'save_copy': "Konservi kopion",
        'save_success': "PDF konservita kiel: {0}",
        'save_encrypted': "Protektita PDF konservita kiel: {0}",
        'save_error': "Ne eblis konservi PDF",
        'encryption_question': "Ĉu vi volas protekti la PDF per pasvorto?",
        'encryption_yes': "Jes",
        'encryption_no': "Ne",
        'encryption_cancel': "Nuligi",
        'save_cancel': "Konservado nuligita",
        'save_encrypted_voice': "Dosiero ĉifrita kaj konservita.",
        'save_success_voice': "La PDF-dosiero estis konservita neĉifrite.",
        'save_error_format': "Ne eblis konservi PDF:\n{0}",
        'export_pages_success': "Eksporto al Pages sukcesis",
        'export_pages_error': "Eksporto al Pages malsukcesis",
        'export_pages_error_format': "Eksporto al Pages malsukcesis: {0}",
        'export_word_success': "Eksporto al Word sukcesis",
        'export_word_error': "Eksporto al Word malsukcesis",
        'export_word_error_format': "Eksporto al Word malsukcesis: {0}",
        'export_text_success': "Eksporto al teksto sukcesis",
        'export_text_error': "Eksporto al teksto malsukcesis",
        'export_text_error_format': "Eksporto al teksto malsukcesis: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Pasvorto nepras",
        'password_enter': "Bonvolu enigi pasvorton",
        'password_confirm': "Konfirmi pasvorton",
        'password_new': "Nova pasvorto",
        'password_current': "Aktuala pasvorto",
        'password_save': "Konservi pasvorton (ĉifrite)",
        'password_saved': "✓ Pasvorto por ĉi tiu dosiero estas konservita",
        'password_wrong': "Malĝusta pasvorto",
        'password_mismatch': "Pasvortoj ne kongruas",
        'password_too_short': "Pasvorto tro mallonga",
        'password_min_length': "La pasvorto devas havi almenaŭ 4 signojn",
        'password_strength': "Forto de pasvorto",
        'password_strength_very_weak': "Tre malforta",
        'password_strength_weak': "Malforta",
        'password_strength_medium': "Meza",
        'password_strength_strong': "Forta",
        'password_strength_very_strong': "Tre forta",
        'password_char_count': "({0} signoj)",
        'password_match': "✓ Kongruo",
        'password_no_match': "✗ Pasvortoj ne kongruas",
        'password_show': "Montri",
        'password_hide': "Kaŝi",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Administrado de pasvortoj",
        'password_table_filename': "Dosiernomo",
        'password_table_password': "Pasvorto",
        'password_count': "{0} konservita pasvorto{1}",
        'password_count_singular': "",
        'password_count_plural': "j",
        'password_none': "Neniuj konservitaj pasvortoj",
        'password_copied': "Kopiita {0} pasvorto{1}",
        'password_copied_singular': "",
        'password_copied_plural': "j",
        'password_delete_confirm': "Ĉu vi certe volas forigi la pasvorton por '{0}'?",
        'password_delete_multiple': "Ĉu vi certe volas forigi la {0} elektitajn pasvortojn?",
        'password_delete_all_confirm': "Ĉu vi certe volas forigi ĉiujn {0} konservitajn pasvortojn?",
        'password_deleted': "Forigita {0} pasvorto{1}",
        'password_deleted_singular': "",
        'password_deleted_plural': "j",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "j",
        'password_all_deleted': "Ĉiuj pasvortoj estas forigitaj",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generatoro de pasvortoj",
        'generator_generated': "Generita pasvorto:",
        'generator_regenerate': "Regeneri",
        'generator_copy': "Kopii",
        'generator_use': "Uzi",
        'generator_settings': "Agordoj",
        'generator_length': "Longo:",
        'generator_group_every': "Apartigilo ĉiu",
        'generator_group_chars': "signoj.    Apartigilo:",
        'generator_uppercase': "Majuskloj (A-Z)",
        'generator_lowercase': "Minuskloj (a-z)",
        'generator_digits': "Ciferoj (0-9)",
        'generator_symbols': "Specialaj signoj (!@#$%^&*)",
        'generator_exclude': "Ekskluditaj:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Ĉefpasvorto nepras",
        'master_password_setup': "Agordi ĉefpasvorton",
        'master_password_change': "Ŝanĝi ĉefpasvorton",
        'master_password_enter': "Bonvolu enigi vian ĉefpasvorton",
        'master_password_choose': "Elektu fortan ĉefpasvorton (almenaŭ 8 signojn)",
        'master_password_new': "Bonvolu enigi vian novan ĉefpasvorton",
        'master_password_confirm': "Konfirmi pasvorton",
        'master_password_authenticate': "Aŭtentigi",
        'master_password_success': "Ĉefpasvorto estis sukcese agordita.",
        'master_password_changed': "Ĉefpasvorto estis sukcese ŝanĝita.",
        'master_password_removed': "Ĉefpasvorto kaj ĉiuj pasvortoj estas forigitaj.",
        'master_password_remove': "Forigi ĉefpasvorton",
        'master_password_remove_confirm': "Ĉu vi estas CERTA, ke vi volas forigi ĈIUJN pasvortojn?\n\nĈi tiu ago estas NEREVOKEBLA!",
        'master_password_export_before': "Ĉu vi volas antaŭe eksporti sekurkopion?",
        'master_password_export_delete': "Eksporti kaj forigi",
        'master_password_delete_now': "Forigi tuj",
        'master_password_for_signatures': "Por uzi subskribojn, vi devas agordi ĉefpasvorton.\n\nĈu vi volas agordi ĉefpasvorton nun?",
        'master_password_for_private': "Por uzi privatajn teksterojn, vi devas agordi ĉefpasvorton.\n\nĈu vi volas agordi ĉefpasvorton nun?",
        'master_password_info': """
            <b>🔐 SEN ĈEFPASVORTO:</b><br>
            • Ne eblas montri, kopii kaj eksporti pasvortojn<br>
            • Forigi pasvortojn ĉiam eblas (eĉ sen ĉefpasvorto)<br><br>

            <b>🔐 KUN ĈEFPASVORTO:</b><br>
            • Ĉiuj funkcioj disponeblaj post aŭtentigo<br>
            • Pasvortoj estas ĉifritaj per la ĉefpasvorto<br>
            • Minimuma longo: 8 signoj<br>
            • Sekura SHA-256 haŝa stokado<br><br>

            <b>GRAVA:</b><br>
            • Se vi perdas la ĉefpasvorton: pasvortoj ne estas restaŭreblaj<br>
            • Forigante la ĉefpasvorton: ĈIUJ pasvortoj estos forigitaj<br>
            • Eksporta opcio antaŭ forigo disponebla<br>
            • Ĉefpasvorto ĉiam ŝanĝebla
        """,
        'signature_auth_disabled': "Malŝalti pasvortpeton por subskriboj",
        'template_auth_disabled': "Malŝalti pasvortpeton por privataj teksteroj",
        'master_password_for_signatures_settings': "Por uzi subskribojn, vi devas agordi ĉefpasvorton.\n\nIru al Agordoj - Administrado de pasvortoj",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Protekti PDF",
        'protect_info': "La dosiero '{0}' estos protektita per pasvorto.",
        'protect_instruction': "Bonvolu enigi dufoje la deziratan pasvorton por protekti la dokumenton, aŭ uzu la generatoron de pasvortoj dekstre de la eniga kampo.",
        'protect_success': "PDF estis sukcese protektita kaj konservita kiel:\n{0}\n\nPasvorto: {1}\n\nĈu vi volas malfermi la protektitan PDF nun?",
        'protect_open': "Jes",
        'protect_skip': "Ne",
        'protect_error': "Eraro dum protektado de PDF",
        'protect_open_title': "malfermi protektitan PDF",
        'protect_question': "Farite. Ĉu vi volas malfermi la protektitan PDF nun? Jes aŭ Ne?",
        'password_cancel': "Pasvorta dialogo nuligita",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Forigi paĝojn",
        'pages_extract': "Eltiri paĝojn",
        'pages_insert': "Enmeti paĝojn",
        'pages_move': "Movi paĝojn",
        'pages_delete_options': "Forigaj opcioj",
        'pages_delete_empty': "Forigi ĉiujn malplenajn paĝojn",
        'pages_delete_current': "Forigi nunan paĝon",
        'pages_delete_range': "Forigi paĝaranĝon",
        'pages_cannot_delete_all': "Ne eblas forigi ĉiujn paĝojn",
        'pages_extract_options': "Eltiraj opcioj",
        'pages_extract_current': "Eltiri nunan paĝon",
        'pages_extract_range': "Eltiri paĝaranĝon",
        'pages_insert_position': "Enmeta pozicio",
        'pages_insert_before': "Enmeti antaŭ paĝo:",
        'pages_insert_select': "Elekti PDF",
        'pages_insert_none': "Neniu PDF elektita",
        'pages_move_source': "Paĝoj por movi",
        'pages_move_from': "De paĝo:",
        'pages_move_to': "Ĝis paĝo:",
        'pages_move_target': "Cela pozicio",
        'pages_move_before': "Movi antaŭ paĝon:",
        'pages_move_hint': "Noto: paĝo 1 = komenco, {0} = fino",
        'pages_range_invalid': "La komenca paĝo devas esti malpli aŭ egala al la fina paĝo.",
        'pages_position_invalid': "La cela pozicio ne povas esti ene de la movota intervalo.",
        'pages_no_pdf_selected': "Neniu PDF estas elektita.",
        'pages_deleted': "Forigitaj {0} paĝoj.",
        'pages_extracted': "Eltiritaj: {0}\nKonservita kiel: {1}\nGrandeco: {2:.1f} KB",
        'pages_inserted': "Enmetitaj {0} paĝoj",
        'pages_moved': "Moviĝis {0} paĝoj.",
        'pages_deleted_none': "Neniuj paĝoj forigitaj.",
        'pages_delete_progress': "Forigas paĝojn...",
        'pages_deleted_with_backup': "Forigitaj {0} paĝoj.\n\nSekurkopio: {1}",
        'pages_deleted_voice': "Sekurkopio kreita kaj {0} paĝoj forigitaj.",
        'info': "Noto",
        'error_dialog_creation': "Ne eblis krei dialogon",
        'extract_page_single': "Eltiri paĝon {0}",
        'extract_page_range': "Eltiri paĝojn {0}-{1}",
        'extract_success_voice': "Paĝoj sukcese eltiritaj",
        'extract_error_format': "Eraro dum eltiro: {0}",
        'pages_inserted_voice': "Enmetitaj {0} paĝoj.",
        'insert_error_format': "Eraro dum enmeto: {0}",
        'pages_move_progress': "Movas paĝojn...",
        'pages_moved_with_backup': "Moviĝis {0} paĝoj.\n\nSekurkopio: {1}",
        'move_success_title': "Sukcese movita",
        'pages_moved_voice': "Sukcese movis {0} paĝojn",
        'mark_removed': "Forigita marko de paĝo {0}",
        'mark_empty': "Paĝo {0} markita kiel malplena",
        'mark_export_removed': "Forigita eksportmarko de paĝo {0}",
        'mark_export': "Paĝo {0} markita por eksporto",
        'no_empty_pages': "Neniuj malplenaj paĝoj markitaj por forigo",
        'delete_empty_confirm': "Ĉu vi volas forigi ĉiujn {0} markitajn malplenajn paĝojn?",
        'delete_empty_confirm_voice': "Ĉu nun forigi ĉiujn {0} markitajn malplenajn paĝojn? Jes aŭ Ne.",
        'empty_pages_deleted': "Forigitaj {0} malplenaj paĝoj",
        'no_export_pages': "Neniuj paĝoj markitaj por eksporto",
        'overwrite_title': "Ĉu anstataŭigi ekzistantan dosieron?",
        'overwrite_question': "La dosiero\n\n{0}\n\nej ekzistas.\nĈu vi volas anstataŭigi ĝin?",
        'overwrite_voice': "Ĉu anstataŭigi ekzistantan dosieron? Jes aŭ Ne.",
        'page_skipped': "Paĝo {0} preterlasita",
        'export_complete': "Eksporto finita.",
        'export_complete_voice': "La eksporto estas finita.",
        'no_pages_exported': "Neniu paĝo eksportita",
        'export_cancelled': "Eksporto nuligita",
        'pages_exported': "Eksportitaj {0} paĝoj al {1}",
        'export_page_title': "Eksporti paĝon",
        'page_exported': "Eksportita paĝo {0} al {1}",
        'export_error': "Eraro de eksporto",
        'export_marked_title': "Eksporti markitajn paĝojn",
        'rotate_all_title': "turni ĉiujn paĝojn",
        'rotate_all_question': "Ĉu vi volas turni ĉiujn paĝojn je 90 gradoj dekstren?",
        'rotate_all_voice': "Ĉu vi volas turni ĉiujn paĝojn je 90 gradoj dekstren? Jes aŭ Ne?",
        'all_pages_rotated': "Turnitaj ĉiuj paĝoj",
        'page_rotated': "Turnita paĝo {0}",
        'rotate_error': "Ne eblis turni paĝon",
        'delete_page_confirm': "Ĉu vi volas forigi paĝon {0}?",
        'delete_page_confirm_voice': "Ĉu vi certe volas forigi paĝon {0}? Jes aŭ Ne.",
        'page_deleted': "Forigita paĝo {0}",
        'delete_error': "Ne eblis forigi paĝon",
        'pages_deleted_voice': "Forigitaj {0} paĝoj",
        'pages_exported_split': "Sukcese eksportitaj {0} paĝoj.",
        'pages_skipped': "Preterlasitaj {0} paĝoj.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Eltiri paĝojn (altnivela)",
        'pdf_splitter_title': "Dividilo kaj eltiro de PDF",
        'pdf_splitter_load': " Elekti PDF-dosieron",
        'pdf_splitter_info': "Bonvolu elekti opcion por via PDF-dokumento",
        'pdf_splitter_basic': "Bazaj operacioj",
        'pdf_splitter_single': "Dividi en unuopajn paĝojn",
        'pdf_splitter_range': "Eltiri paĝojn:",
        'pdf_splitter_range_placeholder': "ekz. 1-3,5,7-9",
        'pdf_splitter_clean': "Purigaj operacioj",
        'pdf_splitter_remove_empty': "Forigi ĉiujn malplenajn paĝojn",
        'pdf_splitter_remove': "Forigi paĝaranĝon:",
        'pdf_splitter_remove_placeholder': "ekz. 2,4-6",
        'pdf_splitter_process': "Prilabori PDF",
        'pdf_splitter_loaded': "PDF ŝargita. Bonvolu elekti opcion",
        'pdf_read_error': "Ne eblis legi PDF",
        'pages': "paĝoj",
        'pages_created': "Paĝoj estas kreitaj",
        'range_empty': "Bonvolu enigi paĝaranĝon",
        'range_invalid': "Malvalida paĝaranĝo",
        'range_created': "Kreita nova PDF kun la elektitaj paĝoj:\n{0}",
        'empty_removed': "Forigitaj {0} malplenaj paĝoj.\nEligo: {1}",
        'remove_empty': "Bonvolu enigi paĝojn por forigi",
        'remove_invalid': "Malvalidaj paĝoj por forigi",
        'remove_done': "Kreita purigita PDF:\n{0}",
        'open_folder': "Malfermi dosierujon",
        'show_in_finder': "Montri en Finder",
        'pdf_splitter_no_pdf': "Bonvolu unue ŝargi PDF-dosieron.",
        'process_error': "Eraro dum prilaborado de PDF",
        'pages_created_voice': "Kreitaj {0} paĝoj",
        'range_created_voice': "Kreita PDF kun la elektitaj paĝoj",
        'empty_removed_voice': "Forigitaj {0} malplenaj paĝoj",
        'remove_done_voice': "Kreita purigita PDF",
        'pdf_splitter_split_groups': "Ĉiu kohera grupo en apartan dosieron",
        'range_created_single': "Kreita nova PDF:\n{0}",
        'range_created_multiple': "Kreitaj {0} PDF-dosieroj.",
        'range_created_voice_single': "Kreita PDF kun la elektitaj paĝoj",
        'range_created_voice_multiple': "Kreitaj {0} PDF-dosieroj",
        'empty_removed_none_left': "Neniuj paĝoj restis",
        'empty_removed_all_empty': "Ĉiuj paĝoj estis rekonitaj kiel malplenaj kaj estus forigitaj. Neniu dosiero estis kreita.",
        'preview_single': "Antaŭvido: {0}",
        'preview_enter_range': "Bonvolu enigi paĝaranĝon.",
        'preview_invalid_range': "Malvalida paĝaranĝo.",
        'preview_file': "Antaŭvido: {0}",
        'preview_files': "Antaŭvido: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Komencas presadon",
        'print_sent': "Presordono sendita",
        'print_now': "Presi tuj",
        'print_error': "Eraro de tuja presado",
        'print_limited': "Presfunkcio limigita en ĉi tiu sistemo",
        'print_error_format': "Eraro de tuja presado: {0}",
        'warning': "Noto",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Ŝalti al hela reĝimo",
        'mode_switch_to_dark': "Ŝalti al malhela reĝimo",
        'mode_dark_activated': "Malhela reĝimo aktivigita",
        'mode_light_activated': "Hela reĝimo aktivigita",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Plena vido",
        'zoom_two_pages': "Du paĝoj apudaj",
        'zoom_overview': "Superrigarda reĝimo",
        'zoom_cannot_during_search': "Zoom dum serĉado ne eblas",
        'zoom_exit_first': "Bonvolu unue eliri zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Treni kaj faligi aktivigita",
        'drag_disabled': "Treni kaj faligi malaktivigita",
        'drag_page_grab': "Kapti paĝon {0}",
        'drag_page_dropped': "Paĝo {0} enmetita je pozicio {1}",
        'drag_position_invalid': "Malvalida pozicio",
        'drag_same_position': "Paĝo {0} restas je pozicio {0}",
        'drag_error': "Eraro dum movado",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Teksta enigo kun altnivela formatado kaj administrado de teksteroj",
        'text_templates': "Disponeblaj teksteroj:",
        'text_name': "Nomo",
        'text_preview': "Antaŭvido de teksto",
        'text_enter': "Teksto:",
        'text_font_size': "Tipara grando:",
        'text_formatting': "Formatado:",
        'text_bold': "Grasa",
        'text_italic': "Kursiva",
        'text_underline': "Substrekita",
        'text_alignment': "Ĝisrandigo:",
        'text_left': "Maldekstren",
        'text_center': "Centre",
        'text_right': "Dekstren",
        'text_color': "Koloro de teksto:",
        'text_opacity': "Opakeco:",
        'text_word_wrap': "Linia rompo:",
        'text_auto': "Aŭtomate",
        'text_page_width_95': "Paĝa larĝo (95%)",
        'text_page_width_85': "Tre larĝa (85%)",
        'text_page_width_75': "Larĝa (75%)",
        'text_page_width_60': "Larĝa (60%)",
        'text_page_width_50': "Meza (50%)",
        'text_page_width_30': "Mallarĝa (30%)",
        'text_page_width_20': "Pli mallarĝa (20%)",
        'text_page_width_10': "Tre mallarĝa (10%)",
        'text_no_wrap': "Sen rompo",
        'text_private': "Privata tekstero (postulas aŭtentigon)",
        'text_preview_label': "Antaŭvido:",
        'text_preview_placeholder': "Ĉi tie aperos antaŭvido de la teksto...",
        'text_no_text': "(Neniu teksto)",
        'text_save_template': "Konservi kiel eron",
        'text_delete_template': "Forigi elektitan teksteron",
        'text_show_private': "Montri privatajn",
        'text_hide_private': "Kaŝi privatajn",
        'text_use': "Uzi tekston",
        'text_saved': "Tekstero konservita kiel:\n{0}",
        'text_saved_voice': "Konservita tekstero",
        'text_deleted': "Forigita tekstero",
        'text_no_text_to_save': "Neniu teksto por konservi.",
        'text_no_templates': "Neniuj teksteroj trovitaj",
        'text_private_master_required': "Privataj eroj povas esti uzataj nur kiam ĉefpasvorto estas agordita.\n\nĈu vi volas agordi ĉefpasvorton nun?",
        'text_filename': "Dosiernomo por tekstero (sen 'Text_' kaj '.txt'):",
        'text_filename_hint': "Ekzemplo: 'Telefon HomeOffice' estos konservita kiel 'Text_Telefon HomeOffice.txt'",
        'text_save_hint': "La tekstero estos aŭtomate konservita kun formatado.",
        'text_guide_title': "Teksta enigo - instrukcio",
        'text_delete_confirm': "Ĉu vi certe volas forigi la tekstero?\n\nDosiero: {0}\nTeksto: {1}...",
        'text_make_public': "Marki kiel publika",
        'text_make_private': "Marki kiel privata",
        'text_privacy_changed': "Ŝanĝita privateca statuso",
        'text_private_always': "Privataj ĉiam videblaj (agordo)",
        'text_mode_required': "Bonvolu unue aktivigi tekst-reĝimon",
        'text_continue_editing': "Daŭrigi redaktadon - kursoro je la fino de teksto",
        'text_no_input': "Neniu teksto enigita - forĵetita",
        'save_dialog_question': "Kiel vi volas daŭrigi?",
        'text_save_question': "Ĉu konservi ĉiujn tekstojn kaj krucojn, ĝustigi, daŭrigi redaktadon aŭ forĵeti?",
        'copy_cross': "Kopii krucon",
        'paste_cross': "Enmeti krucon",
        'paste_text': "Enmeti tekston",
        'cross_discarded': "Forĵetita kruco",
        'all_discarded': "Ĉio forĵetita",
        'text_discarded': "Forĵetita teksto",
        'no_texts_to_save': "Neniuj tekstoj por konservi",
        'no_valid_texts': "Neniuj validaj tekstoj por konservi",
        'text_word_singular': "teksto",
        'text_word_plural': "tekstoj",
        'cross_word_singular': "kruco",
        'cross_word_plural': "krucoj",
        'texts_saved_title': "Konservitaj tekstoj",
        'texts_crosses_saved': "Konservitaj {0} {1} kaj {2} {3} en la PDF.\n\nPDF reŝargita...",
        'texts_crosses_saved_voice': "Konservitaj {0} {1} kaj {2} {3}.",
        'texts_saved': "Konservitaj {0} {1} en la PDF.\n\nPDF reŝargita...",
        'texts_saved_voice': "Konservitaj {0} {1}.",
        'crosses_saved': "Konservitaj {0} {1} en la PDF.\n\nPDF reŝargita...",
        'crosses_saved_voice': "Konservitaj {0} {1}.",
        'elements_saved': "Konservitaj {0} elementoj en la PDF.\n\nPDF reŝargita...",
        'elements_saved_voice': "Konservitaj {0} elementoj.",
        'text_window_load_error': "Ne eblis ŝargi tekstfenestron",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Teksta enigo kaj teksteroj – detala instrukcio**

        **1. Enmeti kaj redakti tekston**
        - Dekstre alklaku la deziratan lokon en la dokumento kaj elektu "Enmeti tekston".
        - Malfermiĝos dialogo, kie vi povas enigi kaj formati vian tekston:
        • Tipara grando, grasa, kursiva, substreko
        • Teksta koloro (libere elektebla)
        • Travidebleco (opakeco) per ŝovilo
        • Linia rompo (malsamaj larĝoj, ekz. paĝlarĝo, mallarĝa, sen rompo)
        - Post konfirmo la teksto aperos ĉe la alklaka loko. Vi povas movi ĝin per muso aŭ sagoklavoj.
        - Duobla alklako sur teksto malfermas redakton; per ESC vi eliras.

        **2. Administri teksterojn (ŝablonojn)**
        - En la teksta dialogo maldekstre estas listo de ĉiuj konservitaj teksteroj.
        - **Konservi eron:** Enigu vian tekston, formatu ĝin kaj alklaku "💾 Konservi kiel eron". Donu dosiernomon (sen finaĵo).
        - **Ŝargi eron:** Alklaku la deziratan nomon en la listo. La teksto kaj formatado estos transprenitaj kaj povas esti ĝustigitaj.
        - **Forigi:** Dekstre alklaku eron por forigi ĝin aŭ ŝanĝi ĝian privatecan statuson.

        **3. Privataj teksteroj (ĉefpasvorto)**
        - Se vi agordis ĉefpasvorton (sub Agordoj → Administrado de pasvortoj), vi povas marki erojn kiel "privataj".
        - Marku la markobuton "Privata tekstero" en la dialogo antaŭ konservado.
        - Privataj eroj estas montrataj en la listo nur post enigo de la ĉefpasvorto unufoje por seanco (aŭtentigo per la piktogramo aŭ unua aliro).
        - Tiel vi povas protekti konfidencajn teksterojn kontraŭ neaŭtorizita aliro.

        **4. Enmeti krucojn**
        - Per la kunteksta menuo vi ankaŭ povas enmeti grafan krucon (ekz. por markobutonoj).
        - Grandeco, linia dikeco kaj koloro de krucoj povas esti ĝustigitaj tutmonde en la agordoj (menu "Agordoj" → "Agordoj de krucoj").
        - Dekstre alklaku ekzistantan krucon por ĝustigi ĝin individue.

        **5. Kolektivaj agoj**
        - Se vi metis plurajn tekstojn aŭ krucojn sur paĝo, vi povas per la kunteksta menuo (dekstra klako en teksta reĝimo) konservi aŭ forĵeti ĉiujn elementojn kune.
        - Dum konservado ĉiuj elementoj estas enigitaj en la PDF kaj restas kiel vektoraj grafikaĵoj.

        **6. Klavaraj ŝparvojoj en teksta reĝimo**
        - Sagoklavoj: movi elementon
        - Ctrl+sagoklavoj: pli grandaj paŝoj
        - Enter: malfermi konservan dialogon (konservi ĉion / ĝustigi / forĵeti)
        - ESC: forĵeti nunan elementon
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Teksta enigo kaj teksteroj – detala instrukcio</strong></p>

        <p><strong>1. Enmeti kaj redakti tekston</strong></p>
        <ul>
        <li>Dekstre alklaku la deziratan lokon en la dokumento kaj elektu "Enmeti tekston".</li>
        <li>Malfermiĝos dialogo, kie vi povas enigi kaj formati vian tekston:<br/>
        • Tipara grando, grasa, kursiva, substreko<br/>
        • Teksta koloro (libere elektebla)<br/>
        • Travidebleco (opakeco) per ŝovilo<br/>
        • Linia rompo (malsamaj larĝoj, ekz. paĝlarĝo, mallarĝa, sen rompo)</li>
        <li>Post konfirmo la teksto aperos ĉe la alklaka loko. Vi povas movi ĝin per muso aŭ sagoklavoj.</li>
        <li>Duobla alklako sur teksto malfermas redakton; per ESC vi eliras.</li>
        </ul>

        <p><strong>2. Administri teksterojn (ŝablonojn)</strong></p>
        <ul>
        <li>En la teksta dialogo maldekstre estas listo de ĉiuj konservitaj teksteroj.</li>
        <li><strong>Konservi eron:</strong> Enigu vian tekston, formatu ĝin kaj alklaku "💾 Konservi kiel eron". Donu dosiernomon (sen finaĵo).</li>
        <li><strong>Ŝargi eron:</strong> Alklaku la deziratan nomon en la listo. La teksto kaj formatado estos transprenitaj kaj povas esti ĝustigitaj.</li>
        <li><strong>Forigi:</strong> Dekstre alklaku eron por forigi ĝin aŭ ŝanĝi ĝian privatecan statuson.</li>
        </ul>

        <p><strong>3. Privataj teksteroj (ĉefpasvorto)</strong></p>
        <ul>
        <li>Se vi agordis ĉefpasvorton (sub Agordoj → Administrado de pasvortoj), vi povas marki erojn kiel "privataj".</li>
        <li>Marku la markobuton "Privata tekstero" en la dialogo antaŭ konservado.</li>
        <li>Privataj eroj estas montrataj en la listo nur post enigo de la ĉefpasvorto unufoje por seanco (aŭtentigo per la piktogramo aŭ unua aliro).</li>
        <li>Tiel vi povas protekti konfidencajn teksterojn kontraŭ neaŭtorizita aliro.</li>
        </ul>

        <p><strong>4. Enmeti krucojn</strong></p>
        <ul>
        <li>Per la kunteksta menuo vi ankaŭ povas enmeti grafan krucon (ekz. por markobutonoj).</li>
        <li>Grandeco, linia dikeco kaj koloro de krucoj povas esti ĝustigitaj tutmonde en la agordoj (menu "Agordoj" → "Agordoj de krucoj").</li>
        <li>Dekstre alklaku ekzistantan krucon por ĝustigi ĝin individue.</li>
        </ul>

        <p><strong>5. Kolektivaj agoj</strong></p>
        <ul>
        <li>Se vi metis plurajn tekstojn aŭ krucojn sur paĝo, vi povas per la kunteksta menuo (dekstra klako en teksta reĝimo) konservi aŭ forĵeti ĉiujn elementojn kune.</li>
        <li>Dum konservado ĉiuj elementoj estas enigitaj en la PDF kaj restas kiel vektoraj grafikaĵoj.</li>
        </ul>

        <p><strong>6. Klavaraj ŝparvojoj en teksta reĝimo</strong></p>
        <ul>
        <li>Sagoklavoj: movi elementon</li>
        <li>Ctrl+sagoklavoj: pli grandaj paŝoj</li>
        <li>Enter: malfermi konservan dialogon (konservi ĉion / ĝustigi / forĵeti)</li>
        <li>ESC: forĵeti nunan elementon</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Agordoj de krucoj",
        'cross_properties': "Ecoj de kruco",
        'cross_size': "Grandeco (px):",
        'cross_line_width': "Dikeco de linio:",
        'cross_color': "Koloro:",
        'cross_choose_color': "Elekti",
        'cross_fine_tuning': "Precizigado dum konservado (pikseloj)",
        'cross_offset_x': "Ofseto X:",
        'cross_offset_y': "Ofseto Y:",
        'cross_offset_x_tooltip': "Negativaj valoroj movas la krucon maldekstren, pozitivaj dekstren",
        'cross_offset_y_tooltip': "Negativaj valoroj movas la krucon supren, pozitivaj malsupren",
        'cross_preview': "Antaŭvido",
        'cross_save': "Apliki agordojn",
        'cross_customized': "Kruco ĝustigita",
        'cross_settings_applied': "Konservitaj agordoj de krucoj.\nGrandeco: {0}px, dikeco: {1}px\n{2}",
        'cross_updated_count': "Ĝisdatigitaj {0} ekzistantaj krucoj.",
        'cross_no_crosses': "Neniuj ekzistantaj krucoj trovitaj.",
        'cross_settings_applied_all': "Aplikitaj agordoj de krucoj por ĉiuj {0} krucoj",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Agordoj de subskribo",
        'signature_1': "Subskribo 1",
        'signature_2': "Subskribo 2",
        'signature_select': "Elekti subskribon",
        'signature_add': "Aldoni novan subskribon...",
        'signature_size': "Grandeco por subskribo {0} (%):",
        'signature_common': "Ĝeneralaj agordoj",
        'signature_timestamp': "Aŭtomate aldoni tempostampon",
        'signature_location': "Defaŭlta loko:",
        'signature_timestamp_size': "Tipara grando de tempostampo:",
        'signature_no_files': "-- Neniuj subskriboj trovitaj --",
        'signature_insert': "Enmeti subskribon",
        'signature_insert_1': "Enmeti subskribon 1",
        'signature_insert_2': "Enmeti subskribon 2",
        'signature_customize': " Ĝustigi subskribon",
        'signature_discard': " Forĵeti ĉi tiun subskribon",
        'signature_save_all': " Konservi ĉiujn subskribojn",
        'signature_discard_all': " Forĵeti ĉiujn subskribojn",
        'signature_guide_title': "Subskriboj – instrukcio",
        'signature_guide': """
📝 Subskriboj – mallonga instrukcio

- Agordi ĉefpasvorton
- Konfiguri subskribojn en menuo Agordoj
  (grandeco, tempostampo ...)
- Enmeti per DEKSTRA ALKLAKO ĉe la dezirata pozicio
  (ĉefpasvorto necesas unufoje por seanco)
- Movi subskribon per muso aŭ sagoklavoj
- Pluraj subskriboj povas esti enmetitaj sinsekve
- Ĉiu subskribo povas esti individue ĝustigita
- Forĵeti unuopajn subskribojn
- Konservi / forĵeti ĉiujn subskribojn samtempe
- Alternative oni povas uzi la menuon.
        """,
        'signature_placeholder': "Neniu antaŭvido disponebla",
        'signature_info': "Subskribo {0}: {1}×{2} px ({3}% el {4}×{5})",
        'signature_info_placeholder': "Agordoj por subskribo {0}",
        'signature_inserted': "Enmetita subskribo {0} sur paĝo {1}",
        'signature_deleted': "Forigita subskribo",
        'signature_copied': "Kopiita subskribo",
        'signature_pasted': "Enmetita subskribo {0}",
        'signature_saved': "Konservitaj {0} subskriboj en la PDF.\n\nPDF reŝargita...",
        'signature_saved_voice': "Konservitaj {0} subskriboj",
        'mode_replace_signature_format': "Eliri reĝimon kaj enmeti subskribon {0}",
        'mode_conflict_voice_signature': "Reĝimo {0} estas aktiva. Ĉu eliri kaj enmeti subskribon?",
        'signature_not_configured': "Subskribo {0} ne konfigurita",
        'signature_file_not_found': "Dosiero de subskribo ne trovita",
        'timestamp_format': "{0}, la {1}",
        'no_copied_signature': "Neniu kopiita subskribo ekzistas",
        'no_signatures_to_save': "Neniuj subskriboj por konservi",
        'signature_save_question': "Ĉu konservi ĉiujn subskribojn, ĝustigi aŭ forĵeti ĉi tiun?",
        'signatures_saved_title': "Konservitaj subskriboj",
        'signatures_saved': "Konservitaj {0} subskriboj en la PDF.\n\nPDF reŝargita...",
        'signatures_saved_voice': "Konservitaj {0} subskriboj.",
        'all_signatures_discarded': "Ĉiuj subskriboj forĵetitaj",
        'signature_settings_saved': "Konservitaj agordoj de subskriboj",
        'signature_cancelled': "Forĵetita subskribo",
        'signature_active_title': "Subskribo aktiva",
        'signature_replace_question': "Subskribo jam estas aktiva.\n\nĈu vi volas anstataŭigi la nunan subskribon?",
        'signature_replace': "Anstataŭigi subskribon",
        'signature_replace_voice': "Ĉu anstataŭigi nunan subskribon aŭ nuligi?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Agordoj de bildoj",
        'image_common': "Ĝeneralaj agordoj de bildoj",
        'image_keep_aspect': "Konservi bildproporcion dum trenado",
        'image_default_size': "Defaŭlta grandeco (%):",
        'image_dark_invert': "Inversigi bildojn en malhela reĝimo",
        'image_dark_invert_tooltip': "Aktivigita: bildoj estas inversigitaj por pli bona videbleco",
        'image_fine_tuning': "Precizigado (pikseloj)",
        'image_offset_x': "Ofseto X:",
        'image_offset_y': "Ofseto Y:",
        'image_offset_x_tooltip': "Negativaj valoroj movas la bildon maldekstren, pozitivaj dekstren",
        'image_offset_y_tooltip': "Negativaj valoroj movas la bildon supren, pozitivaj malsupren",
        'image_select': "Elekti bildon",
        'image_insert': "Enmeti bildon",
        'image_customize': " Ĝustigi bildon",
        'image_aspect': " Konservi proporciojn",
        'image_discard': " Forĵeti ĉi tiun bildon",
        'image_save_all': " Konservi ĉiujn bildojn",
        'image_discard_all': " Forĵeti ĉiujn bildojn",
        'image_filter': "Bildoj",
        'image_guide_title': "Enmeti bildojn – instrukcio",
        'image_guide': """
📷 Enmeti bildojn en PDF – mallonga instrukcio:

1. Dekstre alklaku la deziratan lokon
2. "Enmeti bildon" → elekti bildon
3. Poziciigi: treni per muso
4. Alĝustigi grandecon: treni ĉe la anguloj/randoj
5. Konservi proporciojn: klavo [A]
6. Pliaj ĝustigoj: dekstra klako sur bildo

Konsilo: En la kunteksta menuo vi povas ĝustigi agordojn.
        """,
        'image_inserted': "Enmetita bildo {0} sur paĝo {1}",
        'image_deleted': "Forĵetita bildo",
        'image_copied': "Kopiita bildo",
        'image_pasted': "Enmetita bildo",
        'image_saved': "Konservitaj {0} bildoj en la PDF.\n\nPDF reŝargita...",
        'image_saved_voice': "Konservitaj {0} bildoj",
        'image_aspect_on': "aktivigita",
        'image_aspect_off': "malaktivigita",
        'image_aspect_toggle': "Konservi proporciojn {0}",
        'image_reset': "Reagordita bildo al originala grandeco",
        'image_replaced': "Anstataŭigita bildo",
        'image_invalid': "Nevalida bildo",
        'mode_replace_image': "Enmeti bildon",
        'mode_conflict_voice_image': "Reĝimo {0} estas aktiva. Ĉu eliri kaj enmeti bildon?",
        'image_active_title': "Bildo aktiva",
        'image_replace_question': "Bildo jam estas aktiva.\n\nĈu vi volas anstataŭigi la nunan bildon?",
        'image_replace': "Anstataŭigi bildon",
        'image_replace_voice': "Ĉu anstataŭigi nunan bildon aŭ nuligi?",
        'image_filter_all': "Bildoj (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Ĉiuj dosieroj (*.*)",
        'no_copied_image': "Neniu kopiita bildo ekzistas",
        'image_discarded': "Forĵetita bildo",
        'image_save_question': "Ĉu konservi ĉiujn bildojn, ĝustigi aŭ forĵeti ĉi tiun?",
        'no_images_to_save': "Neniuj bildoj por konservi",
        'no_valid_images': "Neniuj validaj bildoj por konservi",
        'images_saved_title': "Konservitaj bildoj",
        'images_saved': "Konservitaj {0} bildoj en la PDF.\n\nPDF reŝargita...",
        'images_saved_voice': "Konservitaj {0} bildoj.",
        'all_images_discarded': "Ĉiuj bildoj forĵetitaj",
        'image_settings_updated': "Ĝisdatigitaj agordoj de bildoj",
        'image_replace_title': "Elekti novan bildon",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Agordoj de formoj",
        'form_basic': "Bazaj agordoj",
        'form_default_type': "Defaŭlta tipo de formo:",
        'form_rectangle': "Rektangulo",
        'form_ellipse': "Elipso",
        'form_line': "Linio",
        'form_arrow': "Sago",
        'form_line_width': "Dikeco de linio:",
        'form_colors': "Koloroj",
        'form_line_color': "Koloro de linio:",
        'form_fill_color': "Koloro de plenigo:",
        'form_choose_color': "Elekti",
        'form_transparent': "Travidebla fono (nur linio)",
        'form_filled': "plenigita",
        'form_dark_mode': "Malhela reĝimo",
        'form_dark_invert': "Inversigi kolorojn en malhela reĝimo",
        'form_fine_tuning': "Precizigado (pikseloj)",
        'form_offset_x': "Ofseto X:",
        'form_offset_y': "Ofseto Y:",
        'form_offset_x_tooltip': "Negativaj valoroj movas la formon maldekstren, pozitivaj dekstren",
        'form_offset_y_tooltip': "Negativaj valoroj movas la formon supren, pozitivaj malsupren",
        'form_preview': "Antaŭvido",
        'form_insert': "Enmeti formon",
        'form_rectangle_insert': "Rektangulo",
        'form_ellipse_insert': "Cirklo / Elipso",
        'form_line_insert': "Linio (2 klakoj)",
        'form_arrow_insert': "Sago (2 klakoj)",
        'form_customize': " Ĝustigi formon",
        'form_transparent_toggle': " Travidebla fono",
        'form_discard': " Forĵeti ĉi tiun formon",
        'form_save_all': " Konservi ĉiujn formojn",
        'form_discard_all': " Forĵeti ĉiujn formojn",
        'form_guide_title': "Enmeti formojn – instrukcio",
        'form_guide': """
📐 Enmeti formojn en PDF – mallonga instrukcio:

1. Elektu tipon de formo (rektangulo, cirklo/elipso, linio, sago)
2. Klaku je celpozicio
   - Por rektangulo/elipso: unu klako metas la formon
   - Por linio/sago: du klakoj por komenca kaj fina punktoj
3. Poziciigi formon: treni per muso
4. Alĝustigi grandecon: treni ĉe la anguloj/randoj
5. Konservi formon: Enter
6. Forĵeti formon: ESC
7. Pliaj ĝustigoj: dekstra klako sur formo

Konsilo: En la kunteksta menuo vi povas ĝustigi agordojn.
        """,
        'form_inserted': "Enmetita {0} sur paĝo {1}",
        'form_deleted': "Forigita formo",
        'form_copied': "Kopiita formo",
        'form_pasted': "Enmetita formo",
        'form_saved': "Konservitaj {0} formoj en la PDF.\n\nPDF reŝargita...",
        'form_saved_voice': "Konservitaj {0} formoj",
        'form_reset': "Reagordita formo al defaŭlta grandeco",
        'form_transparent_on': "aktivigita",
        'form_transparent_off': "malaktivigita",
        'form_transparent_toggled': "Travidebla fono {0}",
        'form_line_cancel': "Desegnado de linio nuligita",
        'form_second_click': "Nun klaku finpunkton por {0}",
        'mode_replace_form': "Enmeti formon",
        'mode_conflict_voice_form': "Reĝimo {0} estas aktiva. Ĉu eliri kaj enmeti formon?",
        'form_settings_updated': "Ĝisdatigitaj agordoj de formoj",
        'form_unknown': "Formo",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klaku la komencan pozicion",
        'form_line_guide_2': "2. Klaku la finan pozicion",
        'form_line_guide_3': "La linio estos desegnita inter la du punktoj.",
        'form_line_status_1': "Atendas unuan klakon...",
        'form_line_status_2': "Unua punkto fiksita: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Nun klaku finpunkton...",
        'form_line_status_4': "Ambaŭ punktoj fiksitaj.\nKlaku 'Pret' por konservi.",
        'form_line_reset': "Reagordi",
        'form_line_finish': "Pret",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopii (Cmd+C)",
        'paste': "Enmeti (Cmd+V)",
        'copied': "Kopiita: {0}",
        'no_element_to_copy': "Neniu elemento elektita por kopii",
        'no_copied_data': "Neniuj kopiitaj datumoj ekzistas",
        'no_valid_position': "Neniu valida pozicio por enmeti",
        'copy_text': "Kopiita teksto",
        'copy_image': "Kopiita bildo",
        'copy_form': "Kopiita formo",
        'copy_signature': "Kopiita subskribo",
        'element_text': "Teksto",
        'element_image': "Bildo",
        'element_form': "Formo",
        'element_signature': "Subskribo",
        'element_unknown': "Elemento",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflikto de reĝimoj",
        'mode_conflict_message': "Reĝimo '{0}' jam estas aktiva.\n\nĈu vi volas eliri kaj {1}?",
        'mode_replace': "Eliri reĝimon kaj {0}",
        'mode_cancel': "Nuligi",
        'mode_replace_text': "enmeti tekston",
        'mode_replace_cross': "enmeti krucon",
        'mode_replace_signature': "enmeti subskribon",
        'mode_replace_image': "enmeti bildon",
        'mode_replace_form': "enmeti formon",
        'mode_conflict_voice': "Reĝimo {0} estas aktiva. Ĉu eliri kaj enmeti tekston?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Teksta enigo",
        'active_mode_signature': "Subskribo",
        'active_mode_image': "Bildo",
        'active_mode_form': "Formo",
        'active_mode_and': " kaj ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Enmeti",
        'insert_another_text': "Enmeti tekston",
        'insert_another_cross': "Enmeti krucon",
        'insert_another_signature_1': "Subskribo 1",
        'insert_another_signature_2': "Subskribo 2",
        'insert_another_image': "Enmeti bildon",
        'insert_another_form_rect': "Rektangulo",
        'insert_another_form_ellipse': "Cirklo / Elipso",
        'insert_another_form_line': "Linio (2 klakoj)",
        'insert_another_form_arrow': "Sago (2 klakoj)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Konservi {0}",
        'save_dialog_message': "{0} estos konservita sur paĝo {1}.\n\nKiel vi volas daŭrigi?",
        'save_all': "Konservi ĉiujn {0}",
        'save_single': "Konservi {0}",
        'save_customize': "Ĝustigi {0}",
        'save_discard': "Forĵeti ĉi tiun {0}",
        'save_continue': "Daŭrigi redaktadon",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Iri al paĝo {0}",
        'context_rotate': " Turni paĝon {0}",
        'context_delete': " Forigi paĝon {0}",
        'context_export': " Eksporti paĝon {0}",
        'context_mark_as': " Marki paĝon kiel...",
        'context_mark_empty': " Malplena paĝo",
        'context_unmark_empty': " Ne plu malplena",
        'context_mark_export': " Marki por eksporto",
        'context_unmark_export': " Ne plu eksporti",
        'context_batch_actions': " Kolektivaj agoj",
        'context_batch_delete_empty': " Forigi ĉiujn {0} malplenajn paĝojn",
        'context_batch_export_single': " Eksporti ĉiujn {0} paĝojn (unu dosiero)",
        'context_batch_export_split': " Eksporti ĉiujn {0} paĝojn (apartaj)",
        'context_drag_start': " Komenci trenadon",
        'context_drag_stop': " Ĉesi trenadon",
        'context_insert': " Enmeti",
        'context_insert_pages': " Enmeti paĝojn",
        'context_zoom': "Zoom",
        'discard_mixed': "Forĵeti ĉiujn {0} {1} kaj {2} {3}",
        'save_mixed': "Konservi {0} {1} kaj {2} {3}",
        'discard_texts': "Forĵeti ĉiujn {0} tekstojn",
        'discard_text_single': "Forĵeti 1 tekston",
        'save_texts': "Konservi {0} tekstojn",
        'save_text_single': "Konservi 1 tekston",
        'discard_crosses': "Forĵeti ĉiujn {0} krucojn",
        'discard_cross_single': "Forĵeti 1 krucon",
        'save_crosses': "Konservi {0} krucojn",
        'save_cross_single': "Konservi 1 krucon",
        'discard_signatures': "Forĵeti ĉiujn {0} subskribojn",
        'save_signature_single': "Konservi 1 subskribon",
        'save_signatures': "Konservi {0} subskribojn",
        'discard_images': "Forĵeti ĉiujn {0} bildojn",
        'save_image_single': "Konservi 1 bildon",
        'save_images': "Konservi {0} bildojn",
        'discard_forms': "Forĵeti ĉiujn {0} formojn",
        'save_form_single': "Konservi 1 formon",
        'save_forms': "Konservi {0} formojn",
        'cross_discard': "Forĵeti ĉi tiun krucon",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informoj pri eksporto / importo",
        'export_what': "📋 Kio estas eksportata?",
        'export_general': "Ĝeneralaj agordoj",
        'export_general_items': "• Parolado (aktivigi/malaktivigi, rapido)\n• Malhela/hela reĝimo\n• Agordoj de sekurkopio\n• Agordoj de OCR",
        'export_image_form': "Agordoj de bildoj kaj formoj",
        'export_image_form_items': "• Agordoj de bildoj (proporcioj, defaŭlta grandeco)\n• Agordoj de formoj (dikeco, koloroj)\n• Agordoj de subskriboj (vojoj, grandecoj, tempostampoj)",
        'export_passwords': "Bazdatenaro de pasvortoj",
        'export_passwords_items': "• Ĉiuj konservitaj pasvortoj de PDF\n• Laŭelekte ĉifritaj aŭ malĉifritaj",
        'export_master': "Agordoj de ĉefpasvorto",
        'export_master_items': "• Haŝo de ĉefpasvorto\n• Agordoj por subskriboj/teksteroj",
        'export_signatures': "Subskriboj kaj teksteroj",
        'export_signatures_items': "• Ĉiuj bildaj dosieroj (subskriboj)\n• Ĉiuj teksteroj kun formatado\n• Markoj privataj/publikaj",
        'export_import_warning': "⚠️ Gravaj notoj",
        'export_import_note': "• Dum importo ĈIUJ nunaj agordoj estos anstataŭigitaj\n• Necesas restartigi la aplikaĵon\n• Ekzistantaj subskriboj/teksteroj estos anstataŭigitaj",
        'export_master_note': "• Kiam ĉefpasvorto estas agordita, vi povas elekti:\n  - Malĉifrite (pasvortoj en klara teksto)\n  - Ĉifrite (legeblaj nur per ĉefpasvorto)",
        'export_security': "• La eksportita ZIP-dosiero enhavas konfidencajn datumojn\n• Konservu ĝin sekure (ekz. ĉifrita USB-memorilo)\n• Se la dosiero perdiĝas: pasvortoj estas nereakireblaj",
        'export_format': "📁 Formo de eksporto",
        'export_format_desc': "La agordoj estas konservitaj en ununura ZIP-dosiero:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Agordoj sukcese eksportitaj",
        'export_failed': "Eksporto malsukcesis",
        'export_import_question': "Ĉu vi volas nun restartigi la aplikaĵon?",
        'export_password_question': "Ĉefpasvorto estas agordita.\n\nĈu vi volas eksporti la pasvortojn malĉifrite?\n(alie ili estos eksportitaj ĉifrite)",
        'export_decrypt': "Eksporti malĉifrite",
        'export_encrypt': "Eksporti ĉifrite",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informoj",
        'info_title': "Pri PDF Dark View",
        'info_version': "Versio",
        'info_author': "Evoluigita de Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Pri",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> estas alirebla PDF-legilo, speciale evoluigita por homoj kun vidhandikapo.</p>

            <p><strong>Ĉefaj trajtoj:</strong></p>
            <ul>
                <li>Kontrasta, agordebla interfaco</li>
                <li>Plena klavara regado</li>
                <li>Enkonstruita parolsintezilo</li>
                <li>OCR por skanitaj dokumentoj</li>
                <li>Ampleksaj redaktiloj</li>
            </ul>

            <p>Nuntempe subtenataj estas pli ol 60 lingvoj – por ke PDF-oj estu alireblaj por ĉiuj.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkcioj",
        'info_features_intro': "PDF Dark View ofertas al vi la sekvajn eblojn:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Vidigo kaj navigado</strong> – malhela/hela reĝimo, foliumado, zomo, salto al paĝo, legosignoj</li>
            <li><strong>OCR (teksta rekonado)</strong> – igi skanitajn dokumentojn serĉeblaj kaj kopieblaj</li>
            <li><strong>Redaktado</strong> – enmeti tekstojn, krucojn, subskribojn, bildojn kaj formojn</li>
            <li><strong>Administrado de paĝoj</strong> – forigi, turni, eltiri, enmeti, movi per trenado</li>
            <li><strong>Kunfandi PDF-ojn</strong></li>
            <li><strong>Eksporto</strong> – al Word, Pages aŭ kiel teksto</li>
            <li><strong>Sekureco</strong> – protekto per pasvorto kaj administrado de pasvortoj</li>
            <li><strong>Metadatenoj</strong> – redakti</li>
            <li><strong>Dosiernomoj</strong> – centra agordo por sekurkopio kaj dosiernomoj ĉe ŝanĝoj</li>
            <li><strong>Alirebleco</strong> – parolsintezilo, klavara regado, alta kontrasto</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Uzado",
        'info_accessibility': "♿ Alirebleco – plena klavara regado",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Ĝeneralaj</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Malfermi PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Serĉi</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Ŝalti malhelan/helan reĝimon</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Presi</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Eliri</div>

        <div class="shortcut-cat">📖 Navigado</div>
        <div class="shortcut-row"><kbd>Sagoklavoj</kbd> Foliumi paĝon post paĝo</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Iri al paĝo</div>
        <div class="shortcut-row"><kbd>Hejmo</kbd> Unua paĝo</div>
        <div class="shortcut-row"><kbd>Fino</kbd> Lasta paĝo</div>

        <div class="shortcut-cat">✏️ Redaktado</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Enmeti tekston</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Forigi paĝojn</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Eltiri paĝojn</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Enmeti paĝojn</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Movi paĝojn</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Turni paĝon</div>

        <div class="shortcut-cat">🖼️ Movi elementojn</div>
        <div class="shortcut-row"><kbd>Sagoklavoj</kbd> Movi tekston/bildon/subskribon</div>
        <div class="shortcut-row"><kbd>Ctrl+Sagoklavoj</kbd> Pli grandaj paŝoj</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Konservi</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Forĵeti</div>

        <div class="shortcut-cat">🗣️ Parolsintezilo</div>
        <div class="shortcut-row"><kbd>F2</kbd> Ŝalti/malŝalti paroladon</div>
        """,
        'info_contextmenu': "📌 Grava: Ĉiuj funkcioj ankaŭ haveblas per la kunteksta menuo (dekstra musbutono)!",
        'info_accessibility_hint': "💡 Konsilo: La parolsintezilo (F2) faciligas orientiĝon kaj donas retrokuplon pri menuoj kaj dialogoj.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licenco kaj Impresumo",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUMO</strong><br>
        Informoj laŭ § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germanio<br>
        Retpoŝto: binhdiez64@gmail.com<br>
        Interreto: https://github.com/BinhDiez64/PDFDarkView<br>
        Respondeca por enhavo: Toralf Schulz (BinhDiez)<br><br>

        <strong>Malgarantio</strong><br>
        La programaro estis evoluigita kun plej granda zorgo. Ne estas garantiite pri ĝusteco, pleneco kaj funkcieco.<br>
        Uzo okazas propra respondeco.<br><br>

        <strong>📄 MIT-permesilo (privata uzo)</strong><br>
        Aŭtorrajto (c) 2026 Toralf Schulz (BinhDiez)<br>
        Permesite: senpaga uzo, privataj modifoj, personaj kopioj.<br>
        Malpermesite: vendo, komerca uzo, forigo de aŭtorrajtaj indikoj.<br><br>

        <strong>🔧 Komponantoj de triaj</strong><br>
        Ĉi tiu programaro enhavas komponantojn sub GPL, AGPL, Apache 2.0, BSD kaj MIT-permesiloj.<br>
        Je redistribuo oni devas observi la respektivajn permesilajn kondiĉojn.<br><br>

        <strong>🌐 Malferma kodo</strong><br>
        La fontkodo estas havebla kaj povas esti vidata, modifata kaj redistribuata laŭ la respektivaj permesilaj kondiĉoj.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # Englische Version (bleibt in allen Sprachversionen gleich, wird unter dem landessprachlichen Text angezeigt)
        'info_license_html_en': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRINT</strong><br>
        Information according to § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        Email: binhdiez64@gmail.com<br>
        Responsible for content: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Disclaimer</strong><br>
        This software was developed with the greatest care. No warranty is given for correctness, completeness or functionality. Use is at your own risk.<br><br>

        <strong>📄 MIT License (private use)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Permitted: free use, private modifications, personal copies.<br>
        Not permitted: sale, commercial use, removal of copyright notices.<br><br>

        <strong>🔧 Third-Party Components</strong><br>
        This software contains components under GPL, AGPL, Apache 2.0, BSD and MIT licenses.<br>
        When redistributing, the respective license terms must be complied with.<br><br>

        <strong>🌐 Open Source</strong><br>
        The source code is available and can be viewed, modified and redistributed according to the respective license terms.<br><br>

        <em>📖 This license information is also available in your local language – simply change the application language.</em><br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Dankoj",
        'info_credits': "Dankon al la komunumo de malferma kodo",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – prilaborado de PDF</li>
            <li><strong>PyQt5</strong> – grafika interfaco</li>
            <li><strong>Tesseract OCR</strong> – rekono de teksto</li>
            <li><strong>OCRmyPDF</strong> – integriĝo de OCR</li>
            <li><strong>python-docx</strong> – eksporto al Word</li>
            <li><strong>qtawesome</strong> – ikonoj</li>
            <li><strong>DeepSeek</strong> – helpo pri tradukoj (pli ol 60 lingvoj)</li>
            <li><strong>Ĉiuj uzantoj</strong> – por valoraj rimarkoj</li>
            <li><strong>La komunumo de malferma kodo</strong> – por bonegaj bibliotekoj</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Lingvoj",
        'info_languages_header': "🌍 Lingva subteno",
        'info_languages_html': """
        <div style="line-height:1.6;">
            <p>PDF Dark View nuntempe subtenas <strong>62 lingvojn</strong> – por ke la programaro estu uzebla tutmonde en alirebla maniero.</p>

            <p><strong>📖 Plena lingvolisto (stato: marto 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albana (Shqip)</li>
                    <li>🇩🇿 Araba (العربية)</li>
                    <li>🇮🇩 Balia (Basa Bali)</li>
                    <li>🇧🇩 Bengala (বাংলা)</li>
                    <li>🇲🇲 Birmanca (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosna (Bosanski)</li>
                    <li>🇧🇬 Bulgara (Български)</li>
                    <li>🇨🇳 Ĉina (中文)</li>
                    <li>🇩🇰 Dana (Dansk)</li>
                    <li>🇩🇪 Germana (Deutsch)</li>
                    <li>🇬🇧 Angla (English)</li>
                    <li>🇪🇪 Estona (Eesti)</li>
                    <li>🇫🇮 Finlanda (Suomi)</li>
                    <li>🇫🇷 Franca (Français)</li>
                    <li>🇬🇷 Greka (Ελληνικά)</li>
                    <li>🇮🇱 Hebrea (עברית)</li>
                    <li>🇮🇳 Hinda (हिन्दी)</li>
                    <li>🇭🇷 Kroata (Hrvatski)</li>
                    <li>🇭🇺 Hungara (Magyar)</li>
                    <li>🇮🇩 Indonezia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlanda (Gaeilge)</li>
                    <li>🇮🇸 Islanda (Íslenska)</li>
                    <li>🇮🇹 Itala (Italiano)</li>
                    <li>🇯🇵 Japana (日本語)</li>
                    <li>🇰🇭 Kmera (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korea (한국어)</li>
                    <li>🇱🇦 Laosa (ພາສາລາວ)</li>
                    <li>🇱🇻 Latva (Latviešu)</li>
                    <li>🇱🇹 Litova (Lietuvių)</li>
                    <li>🇱🇺 Luksemburga (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaja (Bahasa Melayu)</li>
                    <li>🇮🇳 Maratha (मराठी)</li>
                    <li>🇲🇳 Mongola (Монгол)</li>
                    <li>🇳🇵 Nepala (नेपाली)</li>
                    <li>🇳🇱 Nederlanda (Nederlands)</li>
                    <li>🇳🇴 Norvega (Norsk)</li>
                    <li>🇦🇫 Paŝtua (پښتو)</li>
                    <li>🇮🇷 Persa (فارسی)</li>
                    <li>🇵🇱 Pola (Polski)</li>
                    <li>🇵🇹 Portugala (Português)</li>
                    <li>🇮🇳 Panĝaba (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumana (Română)</li>
                    <li>🇷🇺 Rusa (Русский)</li>
                    <li>🇸🇪 Sveda (Svenska)</li>
                    <li>🇷🇸 Serba (Српски)</li>
                    <li>🇸🇰 Slovaka (Slovenčina)</li>
                    <li>🇸🇮 Slovena (Slovenščina)</li>
                    <li>🇪🇸 Hispana (Español)</li>
                    <li>🇹🇿 Svahila (Kiswahili)</li>
                    <li>🇵🇭 Tagala (Filipino)</li>
                    <li>🇮🇳 Tamila (தமிழ்)</li>
                    <li>🇮🇳 Telugua (తెలుగు)</li>
                    <li>🇹🇭 Taja (ไทย)</li>
                    <li>🇨🇿 Ĉeĥa (Čeština)</li>
                    <li>🇹🇷 Turka (Türkçe)</li>
                    <li>🇺🇦 Ukraina (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vjetnama (Tiếng Việt)</li>
                    <li>🇸🇳 Volofa (Wolof)</li>
                    <li>🇺🇸 Jida (ייִדיש)</li>
                    <li>🇿🇦 Zulua (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Aldoni proprajn lingvojn:</strong><br>
                Ĉu vi deziras lingvon, kiu ankoraŭ ne estas inkluzivita? Simple metu vian propran vortaran dosieron (<code>lingvo_xx.py</code>) apud la aplikaĵon – la programaro rekonos ĝin aŭtomate. Se vi interesiĝas pri specifa traduko, bonvolu kontakti min.
            </div>

            <p><strong>🙏 Speciala danko:</strong> DeepSeek por helpo pri tradukado de ĉiuj vortaroj en 62 lingvojn.</p>

            <p>📧 Kontakto por tradukoj: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Eraro",
        'error_occurred': "Eraro okazis",
        'error_pdf_load': "Eraro dum ŝargado de PDF",
        'error_pdf_save': "Eraro dum konservado de PDF",
        'error_ocr': "Eraro de rekono de teksto",
        'error_no_pdf': "Neniu PDF ŝargita",
        'error_page_not_found': "Paĝo ne trovita",
        'error_invalid_range': "Malvalida paĝaranĝo",
        'error_file_not_found': "Dosiero ne trovita",
        'error_permission': "Neniu permeso",
        'error_unknown': "Nekonata eraro",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Sukceso",
        'success_operation': "Operacio sukcese finita",
        'success_saved': "Sukcese konservita",
        'success_exported': "Sukcese eksportita",
        'success_imported': "Sukcese importita",
        'success_deleted': "Sukcese forigita",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Konfirmo",
        'confirm_yes': "Jes",
        'confirm_no': "Ne",
        'confirm_ok': "OK",
        'confirm_cancel': "Nuligi",
        'confirm_delete': "Forigi",
        'confirm_overwrite': "Anstataŭigi",
        'confirm_continue': "Daŭrigi",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Ŝargado de PDF...",
        'progress_saving': "Konservado de PDF...",
        'progress_exporting': "Eksportado de PDF...",
        'progress_processing': "Prilaborado okazas...",
        'progress_wait': "Bonvolu atendi...",
        'progress_preparing': "Preparado...",
        'progress_finalizing': "Finiĝado...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Blanka",
        'color_black': "Nigra",
        'color_red': "Ruĝa",
        'color_green': "Verda",
        'color_blue': "Blua",
        'color_yellow': "Flava",
        'color_magenta': "Magenta",
        'color_cyan': "Ciana",
        'color_orange': "Oranĝa",
        'color_gray': "Griza",
        'color_custom': "Elekti koloron",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Dosiero",
        'menu_edit': "&Redakti",
        'menu_view': "&Vidi",
        'menu_tools': "&Iloj",
        'menu_settings': "&Agordoj",
        'menu_help': "&Helpo",
        'menu_language': "🌐 Lingvo",
        'menu_guides': "&Instrukcioj",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Malfermi",
        'file_save_as': "&Konservi kiel...",
        'file_protect': "&Protekti dokumenton...",
        'file_export': "&Eksporti",
        'file_export_pages': "Eksporti kiel Pages",
        'file_export_word': "Eksporti kiel DOCX",
        'file_export_text': "Eksporti kiel TXT",
        'file_print_now': "&Presi tuj",
        'file_print': "&Presi",
        'file_close': "&Fermi",
        'file_quit': "&Eliri",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Serĉi",
        'edit_ocr': " Fari OCR",
        'edit_rotate': "&Turni paĝon",
        'edit_rotate_all': "Turni &ĉiujn paĝojn",
        'edit_delete_pages': "&Forigi paĝojn",
        'edit_extract_pages': "&Eltiri paĝojn",
        'edit_insert_pages': "&Enmeti paĝojn",
        'edit_move_pages': "&Movi paĝojn",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Enmeti tekstojn kaj krucojn",
        'text_insert': " Enmeti tekston",
        'cross_insert': " Enmeti krucon",
        'text_customize': " Ĝustigi tekston",
        'cross_customize': " Ĝustigi ĉi tiun krucon",
        'cross_customize_all': " Ĝustigi ĉiujn krucojn",
        'text_discard': " Forĵeti ĉi tiun tekston/krucon",
        'text_discard_all': " Forĵeti ĉiujn tekstojn kaj krucojn",
        'text_save_all': " Konservi ĉiujn tekstojn kaj krucojn",
        'text_guide': " Teksta enigo / teksteroj - instrukcio",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Enmeti subskribon",
        'signature_settings_menu': " Agordoj...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Enmeti bildon",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Enmeti formojn",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "Montri &tekstfenestron",
        'view_zoom': "&Zomo",
        'view_zoom_page': "&Paĝlarĝo (defaŭlta)",
        'view_zoom_two': "&Du paĝoj",
        'view_zoom_overview': "&Superrigardo (pluraj paĝoj)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Alirebleco",
        'settings_voice': "Parolsintezilo",
        'settings_voice_tooltip': "kompletigas la paroladon de ekranlegiloj per pliaj informoj",
        'settings_signature': "&Agordoj de subskribo",
        'settings_password': "&Administrado de pasvortoj",
        'settings_backup': "Krei sekurkopion antaŭ ŝanĝoj",
        'settings_export_import': "&Eksporti / importi agordojn",
        'settings_export': "&Eksporti ĉiujn agordojn...",
        'settings_import': "&Importi ĉiujn agordojn...",
        'settings_export_info': "&Kio estas eksportata?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "aktivigita",
        'voice_off': "malaktivigita",
        'voice_toggle': "Parolsintezilo {0}",
        'voice_speed': "Rapido je {0} procentoj",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Ilo ne trovita:\n{0}\n\nBASE_DIR: {1}\nCertigu, ke la PDF-iloj estas instalitaj en la dosierujo {1}.",
        'tool_started': "Komencita {0}",
        'tool_start_failed': "Ne eblis startigi",
        'process_error_failed_to_start': "Ne eblis startigi la procezon. Ĉu la dosiero ekzistas?",
        'process_error_crashed': "Procezo paneis dum startigo.",
        'process_error_timeout': "Tempolimo de procezo atingita.",
        'process_error_write': "Skriberaro en procezo.",
        'process_error_read': "Legaderaro en procezo.",
        'process_error_unknown': "Nekonata proceza eraro",
        'process_command': "Komando",
        'process_normal_exit': "normale finita",
        'process_crashed': "paneis",
        'process_nonzero_exit': "{0} finiĝis kun erarkodo {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Nuligado...",
        'move_cancelling': "Nuligado de movado",
        'opening_pdf': "Malfermado de PDF...",
        'loading_document': "Ŝargado de dokumento...",
        'pdf_opened': "PDF malfermita",
        'pages_found_moving': "{0} paĝoj trovitaj, {1} por movi",
        'creating_backup': "Kreado de sekurkopio...",
        'backup_description': "Sekurigas originalan dosieron...",
        'backup_saved_as': "Konservita kiel: {0}",
        'error_format': "Eraro: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Serĉo restartigita",
        'page_header_simple': "=== Paĝo {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Administrado de pasvortoj – instrukcio",
        'password_guide_voice': "Instrukcio pri administrado de pasvortoj. Bonvolu legi la notojn.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Administrado de pasvortoj – detala instrukcio</strong></p>

        <p><strong>1. Protekto de PDF per pasvorto</strong></p>
        <ul>
        <li>Malfermante PDF protektitan per pasvorto aperos dialogo, kie vi povas enigi la pasvorton.</li>
        <li>Vi povas konservi la pasvorton ĉifrite, por ne devi enigi ĝin ĉiufoje (markobutono „Konservi pasvorton“).</li>
        <li>Per la butono „Forigi pasvorton“ vi povas krei malĉifritan kopion de la PDF kaj forigi la pasvorton el la datumbazo.</li>
        </ul>

        <p><strong>2. Ĉefpasvorto</strong></p>
        <ul>
        <li>La ĉefpasvorto protektas aliron al ĉiuj konservitaj pasvortoj de PDF.</li>
        <li><strong>Agordi:</strong> Iru al „Agordoj → Administrado de pasvortoj → Agordoj de ĉefpasvorto“ kaj alklaku „Agordi ĉefpasvorton“. Elektu fortan pasvorton (almenaŭ 8 signojn).</li>
        <li><strong>Ŝanĝi:</strong> Post sukcesa aŭtentigo vi povas ŝanĝi la ĉefpasvorton.</li>
        <li><strong>Forigi:</strong> Se vi forigas la ĉefpasvorton, ĈIUJ konservitaj pasvortoj estos nerevokeble forigitaj. Vi povas antaŭe eksporti sekurkopion.</li>
        <li>Unufoje por seanco vi devas aŭtentigi vin per la ĉefpasvorto por aliri protektitajn funkciojn (ekz. montri pasvortojn).</li>
        </ul>

        <p><strong>3. Administrado de pasvortoj (listo)</strong></p>
        <ul>
        <li>Sub „Agordoj → Administrado de pasvortoj“ malfermiĝas tabelo de ĉiuj konservitaj PDF-oj kun iliaj ĉifritaj pasvortoj.</li>
        <li><strong>Sen ĉefpasvorto:</strong> Vi povas nur forigi erojn – la pasvortoj restas kaŝitaj.</li>
        <li><strong>Kun ĉefpasvorto (aŭtentigita):</strong> Vi povas montri, kopii, eksporti kaj forigi pasvortojn.</li>
        <li><strong>Eksporto:</strong> Elektu formaton (JSON, CSV, TXT) kaj konservu la liston. Se ĉefpasvorto estas agordita, vi povas decidi ĉu eksporti la pasvortojn en klara teksto aŭ plu ĉifrite.</li>
        <li><strong>Importo:</strong> Antaŭe eksportitan ZIP-dosieron kun ĉiuj agordoj (inkluzive pasvortojn) oni povas importi per „Agordoj → Eksporti/importi agordojn“. Atentu: Ekzistantaj datumoj estos anstataŭigitaj!</li>
        </ul>

        <p><strong>4. Generatoro de pasvortoj</strong></p>
        <ul>
        <li>En la pasvorta dialogo (ekz. dum protektado de PDF) dekstre de la eniga kampo troviĝas ĵetkuba butono 🎲.</li>
        <li>Alklaku ĝin por malfermi la generatoron de pasvortoj. Vi povas agordi longon, signarojn (majuskloj, minuskloj, ciferoj, specialaj signoj) kaj apartigilojn por pli bona legebleco.</li>
        <li>La generitan pasvorton vi povas rekte preni kaj kopii se necese.</li>
        </ul>

        <p><strong>5. Gravaj sekurecaj konsiloj</strong></p>
        <ul>
        <li>Konservitaj pasvortoj estas stokitaj ĉifrite per AES-256. La ŝlosilo estas derivita el via ĉefpasvorto (se agordita) aŭ el fiksa valoro (sen ĉefpasvorto).</li>
        <li>Sen ĉefpasvorto la pasvortoj estas ja ĉifritaj, sed la ŝlosilo estas en la programo – atakanto kun aliro al viaj dosieroj povus malĉifri ilin. Tial ni forte rekomendas uzi ĉefpasvorton.</li>
        <li>La datumbazo de pasvortoj troviĝas en la dosierujo `Daten/passwords.json`. Faru regulajn sekurkopiojn, precipe antaŭ forigo de la ĉefpasvorto.</li>
        <li>Se vi perdas la ĉefpasvorton, ĉiuj konservitaj pasvortoj estas nereakireblaj.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # Neu ab 2026-03-19
        # (32 Info und alles ab 53 in den anderen Wörterbüchern ersetzen)
        # ============================================

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Reĝimo de inversigo",
        'invert_mode_classic': "Klasika (inversigi ĉiujn kolorojn)",
        'invert_mode_smart': "Inteligenta (inversigi nur helecon)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Sojlo de grizaj nuancoj",
        'gray_threshold_10': "10% (strikta)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (defaŭlta)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (milda)",
        'threshold_changed': "Sojlo fiksita je {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Sojlo de grizaj nuancoj – klarigo",
        'threshold_guide_text': "La sojlo de grizaj nuancoj determinas, kiuj pikseloj en la inteligenta malhela reĝimo estas konsiderataj 'grizaj' kaj inversigataj.\n\n"
                                "• Malalta valoro (10%) inversigas nur preskaŭ perfektajn grizajn nuancojn – koloraj elementoj restas tute konservitaj.\n"
                                "• Alta valoro (50%) inversigas ankaŭ iomete kolorajn pikselojn – tio pliigas kontraston, sed povas misformi kolorojn.\n\n"
                                "La optimuma valoro dependas de la dokumento. Por puraj tekstaj dokumentoj 30–40% ofte estas idealaj, por koloraj grafikaĵoj prefere 10–20%.\n\n"
                                "Vi povas ŝanĝi la valoron iam ajn per la menuo 'Agordoj' – la PDF tiam estos tuj reŝargita.\n\n"
                                "Noto:\n* Fotoj kaj bildoj povas esti ĝuste montrataj nur en hela reĝimo!\n* La agordoj de inversigo estas montrataj nur kiam la malhela reĝimo estas aktivigita.",
        'threshold_guide_voice': "La sojlo de grizaj nuancoj determinas, kiel forte la inteligenta malhela reĝimo intervenas. Malalta valoro protektas kolorojn, alta pliigas kontraston.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Malfermado de PDF...",
        'progress_loading_document': "Ŝargado de dokumento...",
        'progress_pdf_opened': "PDF malfermita",
        'progress_creating_backup': "Kreado de sekurkopio...",
        'progress_backup_description': "Sekurigas originalan dosieron...",
        'progress_backup_created': "Sekurkopio kreita",
        'progress_backup_saved_as': "Konservita kiel: {0}",
        'progress_analyzing_start': "Komenco de analizo...",
        'progress_searching_empty': "Serĉo de malplenaj paĝoj...",
        'progress_page_empty': "Paĝo {0} estas malplena",
        'progress_page_keep': "Paĝo {0} restas",
        'progress_analysis_complete': "Analizo finita",
        'progress_empty_found': "Trovitaj {0} malplenaj paĝoj",
        'progress_current_page': "Nuna paĝo",
        'progress_mark_delete': "Markita por forigo",
        'progress_range_selected': "Elektita intervalo {0}-{1}",
        'progress_deleting_pages': "Forigado de {0} paĝoj",
        'progress_creating_new_pdf': "Kreado de nova PDF...",
        'progress_transferring_pages': "Transpreno de paĝoj",
        'progress_keeping_page': "Paĝo {0} estas konservata ({1}/{2})",
        'progress_saving_pdf': "Konservado de PDF...",
        'progress_optimizing': "Optimumigo de grandeco...",
        'progress_finalizing': "Finiĝo...",
        'progress_new_size': "Nova grandeco: {0:.2f} MB",
        'progress_cancelling': "Nuligado...",
        'progress_cancel_message': "Nuligado de {0}",
        'progress_pages_found_moving': "Trovitaj {0} paĝoj, {1} por movi",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analizo de PDF...",
        'ocr_status_optimizing': "Optimumigo de bildo...",
        'ocr_status_recognizing': "Rekonado de teksto...",
        'ocr_status_embedding': "Enigo de teksto...",
        'ocr_status_finalizing': "Finiĝo de PDF...",

        # PDF-Laden
        'progress_preparing': "Preparado...",
        'progress_loading': "Ŝargado de PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Forigado de paĝoj...",
        'progress_moving_title': "Movado de paĝoj...",
        'pages_found': "Paĝoj trovitaj",
        'progress_creating_new_order': "Kreado de nova ordo...",
        'progress_sorting_pages': "Ordigo de paĝoj...",
        'progress_moving_to_begin': "Movado de {0} paĝoj al la komenco",
        'progress_transferring_count': "Transpreno de {0} paĝoj",
        'progress_transferring_before_target': "Transpreno de paĝoj antaŭ la celo",
        'progress_moving_pages': "Movado de {0} paĝoj",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_sekurkopio_",
        'filename_protected_suffix': "_protektita_",
        'filename_copy_suffix': "_kopiaĵo",
        'filename_page_single': "_paĝo_",
        'filename_page_range': "_paĝoj_",
        'filename_export_page': "_paĝo_{0:03}",
        'filename_export_range': "_paĝoj_{0}-{1}",
        'filename_export_multiple': "_paĝoj_{0}",
        'filename_with_text': "_kun_teksto",
        'filename_with_signature': "_kun_subskribo",
        'filename_with_image': "_kun_bildo",
        'filename_with_forms': "_kun_formoj",
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
        'view_toggle_navbar': "Montri butonbreton",

        # ============================================
        # 57. SEITEN LÖSCHEN
        # ============================================
        'pages_cannot_delete_all': "Ne eblas forigi ĉiujn paĝojn",
        'pages_cannot_delete_last_page': 'Ne eblas forigi la lastan paĝon!',
        'pages_cannot_delete_all_pages': 'Almenaŭ unu paĝo devas resti en la dokumento!',
        'delete_pages_confirm': 'Ĉu vi certe volas forigi {0} paĝojn?',
        'delete_pages_confirm_voice': 'Ĉu vi certe volas forigi {0} paĝojn?',
        'pages_deleted': 'Sukcese forigitaj {0} paĝoj.',
        'warning': 'Averto',
        'error': 'Eraro',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Neniu formo elektita",
        'form_customized': "Formo ĝustigita",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Elekti",
        'btn_use': "Uzi",
        'master_password_for_spasswords': "Por konservi kaj uzi pasvortojn, oni unue devas agordi ĉefpasvorton.\n\nĈu vi volas agordi ĉefpasvorton nun?",
        'open_saved_dialog_title': "Malfermi konservitan dosieron",
        'open_saved_question': "Ĉu vi volas malfermi la konservitan dosieron nun?",
        'password': "Pasvorto",
        'password_manager_master_required': "La administranto de pasvortoj disponeblas nur post agordo de ĉefpasvorto.\n\nĈu vi volas agordi ĉefpasvorton nun?",
        'password_master_required_for_select': "Por montri kaj elekti konservitajn pasvortojn, vi devas unue aŭtentigi vin per via ĉefpasvorto.\n\nĈu vi volas aŭtentigi nun?",
        'password_not_available': "La elektita pasvorto ne disponeblas aŭ ne povas esti malĉifrita.",
        'password_options_title': "Opcioj de pasvorto",
        'password_save_choice_change': "Agordi novan pasvorton",
        'password_save_choice_keep': "Uzi ekzistantan pasvorton",
        'password_save_choice_none': "Konservi neĉifrite",
        'password_save_hint': "Unue agordu ĉefpasvorton por sekure konservi pasvortojn.",
        'password_save_master_required': "Konservi pasvorton (nur ebla kun ĉefpasvorto)",
        'password_save_question': "La nuna PDF estas protektita per pasvorto. Ĉu vi volas uzi ekzistantan pasvorton, agordi novan aŭ konservi neĉifrite?",
        'password_select': "Elekti pasvorton",
        'password_select_none': "Neniu pasvorto elektita.\n\nBonvolu elekti pasvorton el la listo.",
        'password_select_one': "Bonvolu elekti ĝuste unu pasvorton.\n\nVi markis plurajn pasvortojn.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_sekurkopio",  # Hinweis: Dieser Eintrag existiert bereits in 55, wird hier aber für andere Kontexte genutzt. Ist kein Duplikat im Sinne des Dictionary-Keys, da der Schlüssel gleich ist. Aber Achtung: Der Wert wird überschrieben. Ich belasse es zur Sicherheit so, wie es war. In der Praxis sollte man den Schlüssel nicht doppelt verwenden.
        'filename_insert_suffix': "_kun_enmeto",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_forigitaj_paĝoj",
        'filename_pages_moved': "_movenitaj_paĝoj",
        'filename_rotated_all_suffix': "_ĉiuj_paĝoj_turnitaj",
        'filename_rotated_suffix': "_paĝo_turnita",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Agordoj de dosiernomoj por ŝanĝoj en PDF",
        'filename_keep_suffixes': "Konservi antaŭajn sufiksojn (ekz. _kun_teksto)",
        'filename_keep_suffixes_false': "Anstataŭigi",
        'filename_keep_suffixes_true': "Konservi",
        'filename_preview_label': "Antaŭvido de dosiernomo:",
        'filename_preview_overwrite_hint': "Antaŭvido ne disponebla – la originalo estos anstataŭigita.",
        'filename_separator': "Apartigilo inter vortoj",
        'filename_separator_none': "Neniu apartigilo",
        'filename_separator_space': "Spaco ( )",
        'filename_separator_underscore': "Substreko (_)",
        'filename_settings_saved': "Agordoj de dosiernomoj konservitaj",
        'filename_settings_title': "Formatado de dosiernomoj kaj sekurkopio",
        'filename_timestamp_position': "Pozicio de tempostampo",
        'filename_timestamp_position_after': "Post la baza nomo",
        'filename_timestamp_position_before': "Tute antaŭe",
        'filename_timestamp_position_end': "Je la fino",
        'filename_use_timestamp': "Uzi tempostampon",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Konduto ĉe ŝanĝoj:</b><ul><li>Forigi kaj enmeti paĝojn</li><li>Enmeti tekston, subskribon, bildon kaj formojn</li><li>OCR</li></ul></html>",
        'backup_section': "Sekurkopio por operacioj sur paĝoj (forigi, movi)",
        'behavior_info': "Noto: Ĉe 'Anstataŭigi originalon' tempostampoj kaj sufiksoj estas ignorataj – la dosiero konservas sian nomon.",
        'behavior_new_file': "Ĉiam krei novan dosieron (kun tempostampo kaj sufikso)",
        'behavior_overwrite': "Anstataŭigi originalon (neniu nova dosiero)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Ĉiuj paĝoj turnitaj.\n\nOriginalo restis senŝanĝa.\nNova dosiero: {0}",
        'all_pages_rotated_voice': "Ĉiuj paĝoj turnitaj, nova dosiero kreita.",
        'empty_pages_deleted_new_file': "Forigitaj {0} malplenaj paĝoj.\n\nOriginalo restis senŝanĝa.\nNova dosiero: {1}",
        'empty_pages_deleted_voice': "Forigitaj {0} malplenaj paĝoj, nova dosiero kreita.",
        'ocr_keep_original': "Konservi originalon (malfermi permane poste)",
        'ocr_new_file_question': "La nova serĉebla PDF estas konservita kiel:\n{0}\n\nĈu vi volas malfermi ĝin nun?",
        'ocr_open_new': "Malfermi novan OCR-dosieron",
        'ocr_original_kept': "La originala dosiero restas malfermita. La OCR-dosiero estas konservita.",
        'page_deleted_new_file': "Forigita paĝo {0}.\n\nOriginalo restis senŝanĝa.\nNova dosiero: {1}",
        'page_deleted_voice': "Forigita paĝo {0}, nova dosiero kreita.",
        'page_rotated_new_file': "Turnita paĝo {0}.\n\nOriginalo restis senŝanĝa.\nNova dosiero: {1}",
        'page_rotated_voice': "Turnita paĝo {0}, nova dosiero kreita.",
        'pages_deleted_new_file': "Forigitaj {0} paĝoj.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero: {1}",
        'pages_deleted_new_file_voice': "Forigitaj {0} paĝoj, nova dosiero kreita.",
        'pages_inserted_new_file': "Enmetitaj {0} paĝoj.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero: {1}",
        'pages_inserted_new_file_ask': "Enmetitaj {0} paĝoj.\n\nOriginalo restis senŝanĝa.\nNova dosiero: {1}\n\nĈu vi volas malfermi ĝin nun?",
        'pages_inserted_voice_new': "Enmetitaj {0} paĝoj, nova dosiero kreita.",
        'pages_moved_new_file': "Movenitaj {0} paĝoj.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero: {1}",
        'pages_moved_new_file_voice': "Movenitaj {0} paĝoj, nova dosiero kreita.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ne plu montri",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Agordo de sekurkopio</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Sekurkopio EN</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Ĉe ĉiuj ŝanĝoj, kiuj anstataŭigas la originalon</strong> (teksto, subskribo, bildo, formo, OCR, turni, enmeti, forigi/movi paĝojn) aŭtomate kreiĝas <strong>sekurkopio kun tempostampo</strong> antaŭ ol la ŝanĝo estas aplikata.</p>
                <p style="margin: 5px 0 5px 20px;">• La sekurkopio troviĝas apud la originala dosiero (ekz. <code>Dokumento_sekurkopio_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Se vi ankaŭ aktivigis la opcion <strong>„Anstataŭigi originalon“</strong>, ankaŭ tiam kreiĝas sekurkopio.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Sekurkopio el</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Neniu sekurkopio</strong> kreiĝas – nek ĉe anstataŭigo nek ĉe operacioj sur paĝoj.</p>
                <p style="margin: 5px 0 5px 20px;">• La originala dosiero povas esti nerevokeble perdita dum anstataŭigo.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Rekomendata nur por spertaj uzantoj!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Konsilo:</strong> La agordo de sekurkopio estas sendependa de la opcio „Anstataŭigi originalon“. Vi povas kombini ambaŭ.<br>
                Vi povas kaŝi ĉi tiun mesaĝon konstante.
            </div>
        </div>
        """,
        'backup_info_title': "Konduto de sekurkopio",
        'backup_info_voice': "Informo pri konduto de sekurkopio ĉe operacioj sur paĝoj. Sekurkopio en anstataŭas originalon, sekurkopio el kreas novan dosieron.",
        'show_backup_info': "Informo pri agordo de sekurkopio",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ne plu montri",
        'overwrite_enable_backup': "Aktivigi sekurkopion (rekomendate)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Anstataŭigi originalon</p>
            <p>Se vi aktivigas ĉi tiun opcion, ŝanĝoj (teksto, subskribo, bildo, formo, OCR, turni, enmeti) estos <strong>konservitaj rekte en la originalo</strong> – <strong>neniu nova dosiero kreiĝas</strong>.</p>
            <p>• La dosiernomo restas senŝanĝa.<br>
            • Tempostampoj kaj sufiksoj estas ignorataj.<br>
            • <strong>Sen sekurkopio la originalo povas esti nerevokeble perdita.</strong></p>
            <p style="color: #FFD700;">Rekomendo: Aktivigu ankaŭ la sekurkopian opcion por aŭtomataj sekurkopioj.</p>
        </div>
        """,
        'overwrite_info_title': "Anstataŭigi originalon",
        'overwrite_info_voice': "Atentu: Anstataŭigi originalon – sen nova dosiero. Sekurkopio rekomendata.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Enmetitaj {0} paĝoj.\n\nLa originala dosiero estis anstataŭigita.\nSekurkopio kreita.",
        'pages_inserted_overwrite_no_backup': "Enmetitaj {0} paĝoj.\n\nLa originala dosiero estis anstataŭigita.\nNENIU sekurkopio kreita.",
        'texts_saved_overwrite_with_backup': "La ŝanĝoj estis konservitaj en la originalo.\n\nSekurkopio kreita.",
        'texts_saved_overwrite_no_backup': "La ŝanĝoj estis konservitaj en la originalo.\n\nNENIU sekurkopio kreita.",
        'texts_crosses_saved_new_file': "Konservitaj {0} {1} kaj {2} {3}.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero kreita.\n\nLa nova PDF estas ŝargata...",
        'texts_saved_new_file': "Konservitaj {0} {1}.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero kreita.\n\nLa nova PDF estas ŝargata...",
        'crosses_saved_new_file': "Konservitaj {0} {1}.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero kreita.\n\nLa nova PDF estas ŝargata...",
        'elements_saved_new_file': "Konservitaj {0} elementoj.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero kreita.\n\nLa nova PDF estas ŝargata...",
        'signatures_saved_overwrite_with_backup': "La subskribo(j) estis konservita(j) en la originalo.\n\nSekurkopio kreita.",
        'signatures_saved_overwrite_no_backup': "La subskribo(j) estis konservita(j) en la originalo.\n\nNENIU sekurkopio kreita.",
        'images_saved_overwrite_with_backup': "La bildo(j) estis konservita(j) en la originalo.\n\nSekurkopio kreita.",
        'images_saved_overwrite_no_backup': "La bildo(j) estis konservita(j) en la originalo.\n\nNENIU sekurkopio kreita.",
        'forms_saved_overwrite_with_backup': "La formo(j) estis konservita(j) en la originalo.\n\nSekurkopio kreita.",
        'forms_saved_overwrite_no_backup': "La formo(j) estis konservita(j) en la originalo.\n\nNENIU sekurkopio kreita.",
        'signatures_saved_new_file': "Konservitaj {0} subskriboj.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero kreita.\n\nLa nova PDF estas ŝargata...",
        'images_saved_new_file': "Konservitaj {0} bildoj.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero kreita.\n\nLa nova PDF estas ŝargata...",
        'forms_saved_new_file': "Konservitaj {0} formoj.\n\nLa originala dosiero restis senŝanĝa.\nNova dosiero kreita.\n\nLa nova PDF estas ŝargata...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Atentu: Ĉi tiu PDF enhavas turnitajn paĝojn. Poziciigado povus esti malpreciza.",
        'page_rotated_warning_title': "Turnita paĝo detektita",
        'page_rotated_warning_message': "La nuna paĝo {0} estas turnita je {1}°.\n\nEnmeto de elementoj sur turnitaj paĝoj ne estas subtenata.\n\nĈu vi volas turni la paĝon nun en vertikalan pozicion?",
        'page_rotated_warning_voice': "Atentu: La paĝo estas turnita. Bonvolu unue turni ĝin.",
        'paste_on_rotated_page_simple_warning': "Enmeto sur paĝo {0} ne eblas!\n\nĈi tiu paĝo estas turnita je {1}°.\n\nBonvolu unue turni la paĝon al 0° (menu: Redakti → Wyrównaj stronę).\n\nAtentu:\nLa antaŭe kopiita elemento perdiĝos, se vi ne konservos ĝin antaŭ turni la paĝon.",
        'paste_on_rotated_page_voice': "Enmeto nuligita. Paĝo turnita. Bonvolu unue Wyrównaj.",
        'page_rotated_cancel': "Nuligi",
        'page_rotated_rotate_until_upright': "Turni paĝon plurfoje (ĝis vertikala)",
        'page_rotated_now_upright': "La paĝo nun estas vertikala. Vi nun povas enmeti.",
        'page_rotated_still_not_upright': "Ne eblis turni la paĝon al vertikala pozicio. Bonvolu korekti permane.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Helpo: Korekti turnitajn paĝojn",
        'help_rotated_pages_voice': "Malfermas helpon pri korektado de turnitaj paĝoj.",
        'btn_help': "Helpo",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problemo: Turnita paĝo – enmeto ne funkcias ĝuste</p>

            <p>Se enmeto de tekstoj, subskriboj aŭ formoj sur turnita paĝo ne funkcias ĝuste, vi povas korekti la paĝon per ekstera PDF-redaktilo.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solvo per ekstera ilo (ekz. Antaŭvido macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksporti paĝon</strong><br>
                &nbsp;&nbsp;En la menuo elektu <strong>Dosiero → Eksporti kiel Pages</strong> aŭ uzu alian metodon por konservi la deziratan paĝon kiel apartan PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Malfermi paĝon en ekstera programo</strong><br>
                &nbsp;&nbsp;Malfermu la eksportitan PDF en PDF-redaktilo (ekz. <strong>Antaŭvido macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Turni paĝon</strong><br>
                &nbsp;&nbsp;Turnu la paĝon tiel, ke ĝi staru vertikale (en Antaŭvido: <strong>Iloj → Turni</strong> aŭ <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Konservi</strong><br>
                &nbsp;&nbsp;Konservu la korektitan paĝon (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Reenmeti la paĝon en la originalan dokumenton</strong><br>
                &nbsp;&nbsp;Revenu al PDFDarkView kaj enmetu la korektitan paĝon ĉe la dezirata pozicio:<br>
                &nbsp;&nbsp;<strong>Redakti → Enmeti paĝojn</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativo: Turni paĝon en la originalo</p>
                <p style="margin: 5px 0 5px 20px;">• Uzu la enkonstruitan turnan funkcion (<strong>Redakti → Turni paĝon</strong>) por iom post iom korekti la paĝon.<br>
                • Post ĉiu turno vi povas kontroli ĉu enmeto nun funkcias.<br>
                • Ĉi tio ofte estas pli rapida solvo – provu ĝin unue!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Konsilo:</strong> Se vi ofte renkontas turnitajn paĝojn, vi povas konstante kaŝi la averton en la enmeta dialogo.<br>
                La poziciigado tiam povus esti malpreciza – uzu ĉi tiun opcion nur se vi konas la sekvojn.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Rektigi paĝojn",
        'menu_rotate_normalize_tooltip': "Turni paĝon aŭ resetigi al 0°",
        'normalize_current_page': "Rektigi nunan paĝon (agordi al 0°)",
        'normalize_all_pages': "Rektigi ĉiujn paĝojn (agordi al 0°)",
        'page_normalized': "Paĝo {0} estis rektigita.",
        'all_pages_normalized': "Ĉiuj paĝoj estis rektigitaj.",
        'page_already_upright': "Paĝo {0} jam estas vertikala.",
        'all_pages_already_upright': "Ĉiuj paĝoj jam estas vertikalaj.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>La PDF ne enhavas serĉeblan tekston.</p><p>Ĉu vi volas fari OCR por eksporti al {0}?</p>",
        'export_ocr_voice': "La PDF ne enhavas tekston. OCR necesas por eksporto al {0}.",
        'export_no_ocr_possible': "Eksporto sen OCR ne eblas. Bonvolu fari OCR per la menuo.",
        'ocr_failed_export_not_possible': "OCR malsukcesis. Eksporto ne eblas.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF malfermiĝas en antaŭvido. Bonvolu tie komenci presadon.",
        'print_preview_manual': "PDF malfermita. Bonvolu ekzekuti la preskomandon permane (ekz. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Kunfandi PDF-ojn",
        'merge_pdfs': "Kunfandi PDF-ojn",
        'merge_progress_title': "Kunfandado de PDF-oj...",
        'merge_pdfs_list': "PDF-oj en ordo (treni por ordigi)",
        'merge_add_pdf': "Aldoni PDF",
        'merge_remove': "Forigi",
        'merge_move_up': "Supren",
        'merge_move_down': "Malsupren",
        'merge_pdfs_info': "💡 Konsilo: Vi povas ŝanĝi la ordon per trenado",
        'merge_no_pdfs': "Neniuj PDF-oj elektitaj. Alklaku 'Aldoni PDF'.",
        'merge_info': "Elektitaj {0} PDF-oj (ĉ. {1} paĝoj)",
        'merge_open_file': "Malfermi dosieron",
        'merge_merge': "Kunfandi",
        'merge_error': "Eraro de kunfandado",
        'merge_min_two_pdfs_error': "Bonvolu elekti almenaŭ du PDF-dosierojn por kunfandi.",
        'merge_select_pdfs': "Elekti PDF-ojn por kunfandi",
        'merge_error_file': "Eraro de prilaborado",
        'merge_cancelled': "Kunfandado nuligita",
        'merge_preparing': "Preparado...",
        'merge_processing': "Prilaborado de PDF {0} el {1}",
        'merge_saving': "Konservado de kunfandita PDF...",
        'merge_complete': "Pret!",
        'merge_success_title': "Kunfandado sukcesis",
        'merge_success_voice': "Sukcese kunfanditaj {0} PDF-oj.",
        'merge_success_message': "Sukcese kunfanditaj {0} PDF-oj.\n\nLa nova dokumento nun havas {1} paĝojn.\n\nNova dosiero:\n{2}\n\nLoko:\n{3}\n{2}\n\nĈu vi volas malfermi ĉi tiun PDF?",
        'replace_file_title': "Ĉu anstataŭigi dosieron?",
        'replace_file_message': "PDF jam estas malfermita. Ĉu vi volas anstataŭigi ĝin per la nova dosiero?",
        'btn_yes': "Jes",
        'btn_no': "Ne",
        'filename_merge_suffix': "kunfandita",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Malfermo de {0}...",
        'progress_merge_reading': "Legado de {0}...",
        'progress_merge_adding': "Aldonado de {0} paĝoj...",
        'progress_merge_optimizing': "Optimumigo de PDF...",
        'progress_merge_writing': "Skribado de PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "fermo de la PDF",
        'action_close_window': "fermo de la fenestro",
        'action_open_new_pdf': "malfermo de nova PDF",
        'action_quit_app': "eliro el la aplikaĵo",
        'changes_saved': "La ŝanĝoj estis konservitaj.",
        'file_close_title': "Fermi PDF-dosieron",
        'save_before_action': "Ĉu konservi la ŝanĝojn antaŭ {0}? Jes aŭ Ne?",
        'save_before_action_voice': "Ĉu konservi la ŝanĝojn antaŭ {0}? Jes aŭ Ne?",
        'save_before_close_question': "Ĉu konservi la ŝanĝojn antaŭ fermo? Jes aŭ Ne?",

        # ============================================
        # Neue Einträge (noch nicht übersetzt)
        # ============================================

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Kreita serĉebla PDF:\n\n{0}\n\n<b>eventuale reprovi",
        "ocr_rotate_title": "Rektigi paĝojn antaŭ OCR",
        "ocr_rotate_question": "La PDF enhavas turnitajn paĝojn.\nĈu vi volas rektigi ĉiujn paĝojn al 0° antaŭ OCR?\nĈi tio signife plibonigas la tekst-rekonon.",
        "ocr_rotate_yes": "Jes, rektigi",
        "ocr_rotate_no": "Ne, komenci OCR tuj",
        "ocr_rotate_voice": "La PDF enhavas turnitajn paĝojn. Ĉu rektigi ĉiujn paĝojn antaŭ OCR?",
        "ocr_not_performed_message": "Neniu teksto. Bonvolu fari OCR (menu \"Redakti\" → \"Fari OCR\" aŭ klavo Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Agordoj de OCR",
        "ocr_language_btn": "Elekti OCR-lingvon",
        "ocr_language": "OCR-lingvo(j)",
        "ocr_language_current": "Nuna lingvo:",
        "ocr_param_info": "Informo pri parametro",

        # Parameter-Labels
        "ocr_force_ocr_label": "Devigi OCR",
        "ocr_deskew_label": "Korekti klinon",
        "ocr_clean_label": "Purigi bildon",
        "ocr_oversample_label": "Distancaĵo (DPI)",
        "ocr_pagesegmode_label": "Paĝa segmentado",
        "ocr_oem_label": "Reĝimo de OCR-motoro",
        "ocr_optimize_label": "Kompreso de PDF",
        "ocr_jobs_label": "Paralelaj procezoj",
        "ocr_verbose_label": "Detalo de protokolo",
        # Tooltips für die Controls
        "ocr_force_ocr_tooltip": "Devigi OCR sur ĉiu paĝo, eĉ se teksto ekzistas",
        "ocr_deskew_tooltip": "Aŭtomate korekti klinitajn skanaĵojn",
        "ocr_clean_tooltip": "Forigi bruon kaj artefaktojn el la bildo",
        "ocr_oversample_tooltip": "Plialtigi la bildon al ĉi tiuj DPI antaŭ OCR",
        "ocr_pagesegmode_tooltip": "Difinas kiel la paĝo estas dividata en tekstajn areojn",
        "ocr_oem_tooltip": "Elektas la OCR-motoro de Tesseract",
        "ocr_optimize_tooltip": "Kompresa nivelo de la eliga PDF",
        "ocr_jobs_tooltip": "Nombro de paralelaj OCR-procezoj",
        "ocr_verbose_tooltip": "Detala nivelo de protokolaj eligaĵoj",
        "ocr_settings_explain_btn": "Klarigo",

        # Parameter-Erklärungen (Tooltips + Info-Dialoge)
        "ocr_force_ocr_explain": "Devigas tekst-rekonon sur <b>ĉiu</b> paĝo, eĉ se ĝi jam enhavas tekston.\n\nRekomendo: <b>Ŝalti</b> por skanitaj PDF-oj, <b>Malŝalti</b> por denaskaj PDF-oj kun jam ekzistanta teksto.",

        "ocr_deskew_explain": "Korektas iomete klinitajn skanaĵojn (ĝis ĉ. 5°).\n\nRekomendo: <b>Ŝalti</b> por skanitaj dokumentoj, <b>Malŝalti</b> se la paĝoj jam estas perfekte rektaj.",

        "ocr_clean_explain": "Forigas bruon, punktojn kaj malgrandajn artefaktojn el la bildo.\n<b>GRAVA:</b> Por arabaj, tajaj aŭ vjetnamaj tekstoj kun diakritaj signoj (punktoj super/sub literoj) ĉi tiu opcio devus esti <b>malŝaltita</b>, ĉar alie gravaj signoj povus perdiĝi.",

        "ocr_oversample_explain": "Skalas la bildon <b>antaŭ</b> la rekono al la indikita DPI.<br><br>• <b>72-150 DPI:</b> Tre rapida, sed malalta rekona indico<br>• <b>200-300 DPI:</b> Optimuma intervalo (defaŭlte: 300)<br>• <b>400+ DPI:</b> Preskaŭ ne pli bona rekono, sed signife pli grandaj dosieroj<br><br>Rekomendo: 300 DPI por kompleksaj skriboj (araba, ĉina, japana), 200 DPI por okcidentaj lingvoj.",
        "ocr_pagesegmode_explain": "Difinas kiel Tesseract dividas la paĝon en tekstajn areojn.\n\n• <b>3 - Aŭtomate (defaŭlte):</b> Bona por miksitaj aranĝoj\n• <b>4 - Ununura kolumno:</b> Por unukolumnaj tekstoj\n• <b>5 - Vertikala bloko:</b> Por vertikalaj skriboj (japana, ĉina)\n• <b>6 - Unueca tekstbloko:</b> Optimuma por fluanta teksto sen kolumnoj\n• <b>11 - Kruda bildo:</b> Por malbonaj skanaĵoj / manskribo\n\nRekomendo: <b>6</b> por simplaj tekstaj dokumentoj, <b>3</b> por kompleksaj aranĝoj.",

        "ocr_oem_explain": "Elektas la OCR-motoro de Tesseract.\n\n• <b>0 - Legacy:</b> Malnova motoro (rapida, sed malpli preciza)\n• <b>1 - LSTM:</b> Neŭrala motoro (pli malrapida, sed pli preciza)\n• <b>2 - Legacy + LSTM:</b> Kombinas ambaŭ rezultojn\n• <b>3 - Standard (preferas LSTM):</b> Plej bona elekto por la plej multaj kazoj\n\nRekomendo: <b>3</b> por maksimuma rekona precizeco.",

        "ocr_optimize_explain": "Komprimas la eligan PDF.\n\n• <b>0:</b> Neniu optimumigo (plej rapida prilaborado)\n• <b>1:</b> Malpeza optimumigo (bona kompromiso)\n• <b>2:</b> Modera optimumigo\n• <b>3:</b> Forta optimumigo (plej malgranda dosiero, sed pli malrapida)\n\nRekomendo: <b>1</b> por ĉiutaga uzo.",

        "ocr_jobs_explain": "Nombro de paralelaj procezoj por OCR.\n\n• <b>1:</b> Malrapida, sed plej malalta memorkonsumo\n• <b>4-8:</b> Optimuma por modernaj plurprocesoroj\n• <b>12+:</b> Preskaŭ neniu plirapidigo, sed alta memorkonsumo\n\nRekomendo: Nombro de CPU-kerroj (ekz. <b>4</b> por 4-kerra sistemo).",

        "ocr_verbose_explain": "Detala nivelo de protokolaj eligaĵoj en la konzolo.\n\n• <b>0:</b> Neniu eligo\n• <b>1:</b> Progreso kaj statmesaĝoj\n• <b>2:</b> Detalaj eligaĵoj\n• <b>3:</b> Plena sencimiga eligo (tre ampleksa)\n\nRekomendo: <b>1</b> por normala operacio.",

        "ocr_reset_title": "Agordoj resetigitaj",
        "ocr_reset_message": "Ĉiuj agordoj de OCR estis resetigitaj al defaŭltaj valoroj.",
        "info_tooltip": "Pliaj informoj pri ĉi tiu parametro",
        "ocr_reset_defaults": "Resetigi al defaŭltaj",
        # ==================== OCR PSM-Modi (Seitenaufteilung) ====================
        "ocr_psm_0": "Aŭtomate (Legacy-motoro)",
        "ocr_psm_1": "Aŭtomata detekto de kolumnoj",
        "ocr_psm_3": "Aŭtomate (defaŭlte)",
        "ocr_psm_4": "Ununura kolumno",
        "ocr_psm_5": "Vertikala bloko",
        "ocr_psm_6": "Unueca tekstbloko",
        "ocr_psm_7": "Ununura tekstlinio",
        "ocr_psm_8": "Ununura vorto",
        "ocr_psm_11": "Kruda bildo (sen aranĝo-analizo)",
        # ==================== OCR OEM-Modi (Engine-Modus) ====================
        "ocr_oem_0": "Legacy-motoro (rapida)",
        "ocr_oem_1": "LSTM-motoro (neŭrala, preciza)",
        "ocr_oem_2": "Legacy + LSTM kombinitaj",
        "ocr_oem_3": "Standard (preferas LSTM)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-lingvo(j)...",
        "ocr_language_title": "Elekti OCR-lingvon(jn)",
        "ocr_language_instruction": "Elektu la lingvon(jn) por tekst-rekono (OCR).\nAtentu: Pluraj lingvoj malrapidigas kaj malprecizigas!\nPlej bonajn rezultojn vi ricevas, se vi elektas nur unu lingvon.",
        "ocr_language_predefined": "Antaŭdifinitaj kombinoj",
        "ocr_language_custom": "Propra...",
        "ocr_language_selected": "Elektitaj OCR-lingvoj",
        "ocr_language_changed": "OCR-lingvo ŝanĝita al {0}",
        "ocr_language_auto_detect": "Disponeblaj lingvoj estas aŭtomate detektitaj.",
        "ocr_language_none_found": "Neniuj Tesseract-lingvaj datumoj trovitaj! Bonvolu instali lingvajn pakaĵojn (ekz. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Propra elekto de lingvoj",
        "ocr_language_available": "Disponeblaj lingvoj (instalitaj):",
        "ocr_language_select_hint": "Elektu unu aŭ plurajn lingvojn:",
        "ocr_language_confirm": "Apliki",
        "ocr_language_reset": "Resetigi al defaŭlta (deu+eng+vie)",
        "ocr_language_priorities": "Rekomendataj lingvoj (antaŭinstalitaj):",
        # Für den MultiLanguageDialog
        "select_all_languages": "Elekti ĉiujn",
        "clear_all_languages": "Nuligi elekton",
        "install_language_packs": "Instali mankantajn lingvajn pakaĵojn...",
        "install_hint": "💡 Konsilo: Ne ĉiuj lingvoj estas instalitaj en via sistemo. Ĉi tiu butono helpos vin instali ilin.",
        "ocr_language_install_title": "Instalado de Tesseract-lingvaj pakaĵoj",
        # OCR-Sprachfehler und Hilfetexte
        "ocr_missing_languages": "Mankantaj OCR-lingvaj pakaĵoj",
        "ocr_missing_languages_message": "La sekvaj elektitaj lingvoj ne estas instalitaj en via sistemo:\n\n{0}\n\nBonvolu instali la mankantajn lingvajn pakaĵojn (vidu helpon sub 'Instala helpo').\n\nĈu vi volas malfermi la instalan helpon nun?",
        "ocr_missing_languages_voice": "Mankantaj lingvaj pakaĵoj. Bonvolu instali la mankantajn lingvojn.",
        "ocr_install_help_now": "Malfermi helpon",
        "ocr_continue_anyway": "Provu ĉiuokaze",
        "ocr_language_error_title": "Eraro de OCR-lingvo",
        "ocr_language_error_message": "Eraro dum tekst-rekono: {0}\n\nBonvolu kontroli viajn OCR-lingvajn agordojn (Agordoj → OCR-lingvo).",
        "ocr_install_help_button": "Instala helpo",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalado de Tesseract-lingvaj pakaĵoj</p>

        <p>Por ke OCR funkciu en certa lingvo, la respondaj lingvaj datumoj devas esti instalitaj en via sistemo. Sekvu la instrukciojn por via operaciumo:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Malfermu la <strong>Terminal</strong> (Finder → Programoj → Utilaĵoj → Terminal).</li>
        <li>Instalu ĉiujn haveblajn lingvojn per:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Tio povas daŭri kelkajn minutojn.)</li>
        <li>Aŭ nur unuopajn lingvojn (ekz. vjetnaman):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Ĉe modernaj Homebrew-versioj eble necesas permane elŝuti la <code>*.traineddata</code> (vidu sube).</li>
        <li>Post instalo: Fermu ĉi tiun dialogon kaj remalfermu la elekton de OCR-lingvo – la novaj lingvoj aperos aŭtomate.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Malfermu terminalon (Ctrl+Alt+T).</li>
        <li>Instalu la deziratan lingvon, ekz. por vjetnama:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Gravaj lingvokodoj: <code>deu</code> (germana), <code>eng</code> (angla), <code>vie</code> (vjetnama), <code>spa</code> (hispana), <code>fra</code> (franca), <code>ita</code> (itala), <code>nld</code> (nederlanda), <code>fin</code> (finna), <code>swe</code> (sveda), <code>nor</code> (norvega).</li>
        <li>Montri ĉiujn haveblajn pakaĵojn:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (permane)</p>
        <ol>
        <li>Elŝutu la deziratajn <code>*.traineddata</code>-dosierojn de:<br>
        <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ekz. <code>vie.traineddata</code> por vjetnama).</li>
        <li>Kopiu la dosierojn en la Tesseract-lingvan dosierujon, kutime:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Ĉe propra instalo adaptu laŭe.)</li>
        <li>Restartigu la aplikaĵon (aŭ remalfermu la elekton de OCR-lingvo).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativo por ĉiuj sistemoj</p>
        <ul>
        <li>Instalu <strong>OCRmyPDF</strong> kaj <strong>Tesseract</strong> per via pakaĵadministrilo. Plej multaj instalaĵoj jam enhavas kelkajn normajn lingvojn (angla, germana, franca).</li>
        <li>Mankantajn lingvojn vi povas ĉiam postinstali – la OCR-lingva elekto listigas nur la efektive haveblajn.</li>
        </ul>

        <hr>
        <p><b>✅ Post instalo:</b> Neniu restarto de la aplikaĵo necesas – la nove aldonitaj lingvoj tuj aperos en la listo.</p>
        <p><b>📖 Helpo pri lingvokodoj:</b> Plenan liston troviĝas en la <a style="color:#E0E0E0;" href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentado de Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Tiparoj Noto Sans",
        "info_noto_font_voice": "Instrukcio por instali Noto Sans-tiparojn",
        "btn_info_noto_font_install": "Informo pri tiparo",
        # Anleitung

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Kiel instali la senpagajn Noto-tiparojn de Google</h2>

        <p>La <strong>Noto-tiparoj</strong> estas libera tiparfamilio de Google. Ilia celo estas <em>"neniu tofuo"</em> (do neniu malplena kvadrato □) kaj ĝuste montri ĉiun signon el la Unikoda normo. Ili estas la ideala komplemento por aplikaĵoj, kiuj devas montri tekstojn en multaj malsamaj lingvoj.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalado en macOS</h3>

        <p><strong>Metodo 1: Per Homebrew (por spertuloj)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metodo 2: Per la "Tipara aldono" (rekomendata)</strong></p>

        <ol>
        <li>Elŝutu la oficialan tiparan pakaĵon:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Malpakumu la ZIP-dosieron</li>
        <li>Kopiu la dosierojn al <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > Uzantoj > Via Uzantonomo > Biblioteko > Tiparoj</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalado en Windows (10 kaj 11)</h3>

        <p><strong>Metodo 1: Microsoft Store (rekomendata)</strong><br>
        Serĉu "Google Noto Fonts" aŭ "Noto Sans" kaj alklaku <strong>Instali</strong>.</p>

        <p><strong>Metodo 2: Permana instalado</strong></p>

        <ol>
        <li>Elŝutu:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Malpakumu ZIP</li>
        <li>Elektu la .ttf / .otf-dosierojn</li>
        <li>Dekstra klako → <strong>Instali</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        aŭ<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\ViaUzantonomo\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalado en Linux</h3>

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

        <p>Kontrolo:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Administri legosignojn",
        "bookmark_add": "Aldoni legosignon",
        "bookmark_add_tooltip": "Konservi nunan paĝon kiel legosignon",
        "bookmark_remove": "Forigi legosignon",
        "bookmark_remove_tooltip": "Forigi la markitan legosignon",
        "bookmark_remove_all": "Forigi ĉiujn",
        "bookmark_remove_all_tooltip": "Forigi ĉiujn legosignojn de ĉi tiu PDF",
        "bookmark_jump": "Salti al legosigno",
        "bookmark_jump_tooltip": "Salti al la elektita paĝo",
        "bookmark_name": "Nomo",
        "bookmark_page": "Paĝo",
        "bookmark_no_bookmarks": "Neniuj legosignoj.\nAlklaku 'Aldoni' por konservi la nunan paĝon kiel legosignon.",
        "bookmark_added": "Legosigno por paĝo {0} aldonita: {1}",
        "bookmark_removed": "Legosigno forigita: {0}",
        "bookmark_all_removed": "Ĉiuj legosignoj forigitaj.",
        "bookmark_name_default": "Paĝo {0}",
        "bookmark_name_prompt": "Nomo por la legosigno:\n(pli longa teksto estos mallongigita al 50 signoj)",
        "bookmark_name_prompt_title": "Nomo de legosigno",
        "bookmark_confirm_remove_all": "Ĉu vi certe volas forigi ĉiujn {0} legosignojn?",
        "menu_bookmarks": "Legosignoj",
        "bookmark_manage": "Administri legosignojn",
        "bookmark_next": "Sekva legosigno",
        "bookmark_prev": "Antaŭa legosigno",
        "bookmark_page_display": "Paĝo {0}",
        "bookmark_exists": "Legosigno por ĉi tiu paĝo kun ĉi tiu nomo jam ekzistas.",
        "bookmark_select_first": "Bonvolu unue elekti legosignon.",
        "bookmark_confirm_remove": "Ĉu vi certe volas forigi la legosignon 'Paĝo {0}: {1}'?",
        "bookmark_jumped_to": "Saltis al legosigno '{0}' sur paĝo {1}.",
        "bookmark_jumped_to_voice": "Legosigno {0}, paĝo {1}",
        "btn_close": "Fermi",
        # LESEZEICHEN KONTEXTMENÜ im Dialog
        "bookmark_list": "Viaj legosignoj",
        "bookmark_rename": "Renomi legosignon",
        "bookmark_rename_tooltip": "Ŝanĝi la nomon de la elektita legosigno",
        "bookmark_rename_title": "Renomi legosignon",
        "bookmark_rename_prompt": "Nova nomo por legosigno sur paĝo {0}:\n(maks. 50 signoj)",
        "bookmark_renamed": "Legosigno '{0}' estis renomita al '{1}'.",
        "bookmark_item_tooltip": "Paĝo {0}: {1}\nDuobla klako por salti",
        "bookmark_name_exists_question": "Legosigno kun la nomo '{0}' jam ekzistas sur ĉi tiu paĝo.\nĈu tamen renomi?",
        # LESEZEICHEN KONTEXTMENÜ im Hauptfenster
        "context_bookmarks": "Legosignoj",
        "context_bookmark_add_here": "Aldoni legosignon por ĉi tiu paĝo",
        "context_bookmarks_existing": "Ekzistantaj legosignoj:",
        "context_bookmarks_jump": "Salti al legosigno:",
        "context_bookmarks_none": "Neniuj legosignoj",
        "context_bookmarks_clear_all": "Forigi ĉiujn {0} legosignojn",
        # LESEZEICHEN SUCHLEISTE
        "bookmark_search_placeholder": "Serĉi legosignojn... (nomo aŭ paĝo)",
        "bookmark_search_results": "Trovitaj %d legosignoj por \"%s\"",
        "bookmark_no_search_results": "Neniuj legosignoj trovitaj por \"%s\"",
        "bookmark_no_search_results_label": "Neniuj rezultoj por \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Redakti metadatenojn de PDF",
        "metadata_title": "Titolo",
        "metadata_title_placeholder": "Titolo de dokumento",
        "metadata_title_tooltip": "La titolo de la dokumento (montrata en la titolbreto)",
        "metadata_author": "Aŭtoro",
        "metadata_author_placeholder": "Nomo de aŭtoro",
        "metadata_author_tooltip": "La kreinto de la dokumento",
        "metadata_subject": "Temo",
        "metadata_subject_placeholder": "Temo de la dokumento",
        "metadata_subject_tooltip": "Mallonga priskribo de la enhavo",
        "metadata_keywords": "Ŝlosilvortoj",
        "metadata_keywords_placeholder": "Ŝlosilvortoj, apartigitaj per komoj",
        "metadata_keywords_tooltip": "Etikedoj por kategorii la dokumenton",
        "metadata_creator": "Kreilo",
        "metadata_creator_placeholder": "Aplikaĵo, kiu kreis la PDF",
        "metadata_creator_tooltip": "La programaro, per kiu la dokumento estis kreita",
        "metadata_producer": "Produktilo",
        "metadata_producer_placeholder": "Aplikaĵo, kiu konvertis la PDF",
        "metadata_producer_tooltip": "La programaro, kiu konvertis la PDF",
        "metadata_creation_date": "Krea dato",
        "metadata_creation_date_tooltip": "La dato de kreado de la dokumento",
        "metadata_mod_date": "Dato de modifo",
        "metadata_mod_date_tooltip": "La dato de la lasta modifo",
        "metadata_pdf_info": "📄 Informoj pri PDF",
        "metadata_pages": "Nombro de paĝoj",
        "metadata_file_size": "Dosiera grandeco",
        "metadata_pdf_version": "Versio de PDF",
        "metadata_encrypted": "Ĉifrita",
        "metadata_encrypted_yes": "Jes (protektita per pasvorto)",
        "metadata_encrypted_no": "Ne",
        "metadata_reload": "📂 Reŝargi el PDF",
        "metadata_reset": "Forĵeti ŝanĝojn",
        "metadata_reloaded": "Metadatenoj reŝargitaj el la PDF.",
        "metadata_reset_done": "Ĉiuj metadatenaj kampoj resetigitaj.",
        "metadata_no_file": "Neniu PDF-dosiero ŝargita.",
        "metadata_save_error": "Eraro dum konservado de metadatenoj",
        "metadata_saved": "Metadatenoj sukcese konservitaj.",
        "metadata_pdf_version_unknown": "PDF (nekonata)",
        "metadata_saved_message": "La metadatenoj estis sukcese konservitaj.",
        "metadata_saved_voice": "Metadatenoj konservitaj.",

        "metadata_custom": "🔧 Propraj metadatenoj",
        "metadata_custom_placeholder": "{\n  \"mia_kampo\": \"mia valoro\",\n  \"alia_kampo\": 123\n}",
        "metadata_custom_tooltip": "JSON-formo por propraj metadatenoj (laŭvola)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Ŝablono \"{0}\" elektita - duobla klako por enmeti",
        "text_use_template": "Uzi teksteron",
        "text_type": "Tipo",
        "text_search_templates": "Serĉi teksterojn...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informoj pri eksporto / importo",
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

        <h3>📦 Kio estas eksportata? (Superrigardo)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Ĝeneralaj agordoj de aplikaĵo</span></li>
            <li class="detail">• Malhela/hela reĝimo</li>
            <li class="detail">• Inversigo de bildoj en malhela reĝimo</li>
            <li class="detail">• Sojlo de grizaj nuancoj</li>
            <li class="detail">• Lingvo</li>
            <li class="detail">• Fenestra geometrio</li>
            <li class="detail">• Reĝimo de zomo</li>
            <li class="detail">• Navigado (butonbreto videbla)</li>
            <li class="detail">• Parolsintezilo (ŝaltita/malŝaltita)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Agordoj de sekurkopio</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nomenklaturo de dosieroj (tempostampo, apartigilo, sufiksoj)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Agordoj por enmetoj</span></li>
            <li class="detail">• Subskriboj</li>
            <li class="detail">• Teksto kaj teksteroj</li>
            <li class="detail">• Krucoj, bildoj kaj formoj</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Agordoj de OCR</span></li>
            <li class="detail">• Lingvo</li>
            <li class="detail">• Devigi OCR · paĝa reĝimo</li>
            <li class="detail">• Antaŭprilaborado de bildo: Deskew, Clean, Oversampling</li>
            <li class="detail">• Nombro de paralelaj taskoj</li>
            <li class="detail">• Reĝimo de inversigo</li>
            <li class="detail">• Sojlo de grizaj nuancoj</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Legosignoj</span></li>
            <li class="detail">• Ĉiuj legosignoj por ĉiu PDF-dosiero (paĝo, nomo, krea tempo)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Datumbazo de pasvortoj</span></li>
            <li class="detail">• Konservitaj pasvortoj de PDF (laŭelekte ĉifritaj aŭ klaraj)</li>
            <li class="detail">• Haŝo de ĉefpasvorto (se agordita)</li>
            <li class="detail">• Verifikaj datumoj</li>
        </ul>

        <h4>⚠️ Gravaj notoj</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Ĉe importo:</strong>
            <ul>
                <li><span class="warning">➜ ĈIUJ nunaj agordoj estos tute anstataŭigitaj</span></li>
                <li>• Necesas restartigi la aplikaĵon</li>
                <li>• Ekzistantaj subskriboj, teksteroj kaj legosignoj estos anstataŭigitaj</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Ĉefpasvorto kaj eksporta reĝimo:</strong>
            <ul>
                <li>• Kiam ĉefpasvorto estas aktiva, vi povas elekti:</li>
                <li>  - <span style="color: #98FB98;"><strong>Malĉifrite</strong></span> (pasvortoj en klara teksto en la ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Ĉifrite</strong></span> (legeblaj nur per ĉefpasvorto en la cela sistemo)</li>
                <li>• La haŝo de la ĉefpasvorto estas <strong>ĉiam</strong> konservita ĉifrite</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Sekurecaj konsiloj:</strong>
            <ul>
                <li>• La eksportita ZIP-dosiero enhavas konfidencajn datumojn (<strong>pasvortoj, legosignoj, subskriboj</strong>)</li>
                <li>• Konservu ĝin sekure (ekz. ĉifrita USB-memorilo, pasvortadministrilo)</li>
                <li>• Se la dosiero perdiĝas, konservitaj PDF-pasvortoj estas nereakireblaj</li>
            </ul>
        </div>

        <h4>📁 Formo de eksporto</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            La agordoj estas konservitaj en ununura ZIP-dosiero:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ĉi tiu ZIP enhavas la kompletan <code>settings.json</code> (el via agordo) kaj eventuale enigitajn subskribajn bildajn dosierojn kaj ĉifritajn pasvortojn.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Subskriboj – instrukcio",
        'signature_guide_html': """
        📝 <strong>Subskriboj – mallonga instrukcio</strong><br>
        <ul>
        <li>Agordi ĉefpasvorton</li>
        <li>Konfiguri subskribojn en menuo <em>Agordoj</em> (grandeco, tempostampo, …)</li>
        <li>Enmeti per <strong>DEKSTRA ALKLAKO</strong> ĉe la dezirata pozicio (ĉefpasvorto necesas unufoje por seanco)</li>
        <li>Movi subskribon per muso aŭ sagoklavoj</li>
        <li>Pluraj subskriboj povas esti enmetitaj sinsekve</li>
        <li>Ĉiu subskribo povas esti individue ĝustigita</li>
        <li>Forĵeti unuopajn subskribojn</li>
        <li>Konservi / forĵeti ĉiujn subskribojn samtempe</li>
        <li>Alternative oni povas uzi la menuon.</li>
        </ul>
        """,
        'signature_guide_voice': "Mallonga instrukcio pri subskriboj. Agordu ĉefpasvorton. Konfiguru subskribojn en agordoj. Enmetu per dekstra alklako.",

        'image_guide_title': "Enmeti bildojn – instrukcio",
        'image_guide_html': """
        📷 <strong>Enmeti bildojn en PDF – mallonga instrukcio</strong><br>
        <ol>
        <li>Dekstra alklako ĉe la dezirata pozicio</li>
        <li>„Enmeti bildon“ → elekti bildon</li>
        <li>Poziciigi: treni per muso</li>
        <li>Alĝustigi grandecon: treni ĉe la anguloj/randoj</li>
        <li>Konservi proporciojn: klavo <strong>[A]</strong></li>
        <li>Pliaj ĝustigoj: dekstra klako sur bildo</li>
        </ol>
        <p><strong>Konsilo:</strong> En la kunteksta menuo vi povas ĝustigi agordojn.</p>
        """,
        'image_guide_voice': "Mallonga instrukcio pri bildoj. Dekstra alklako, enmeti bildon, elekti. Poziciigi per muso, alĝustigi grandecon per anguloj. Konservi proporciojn per klavo A.",

        'form_guide_title': "Enmeti formojn – instrukcio",
        'form_guide_html': """
        📐 <strong>Enmeti formojn en PDF – mallonga instrukcio</strong><br>
        <ol>
        <li>Elektu tipon de formo (rektangulo, elipso, linio, sago)</li>
        <li>Klaku je celpozicio:
            <ul>
            <li>Por rektangulo/elipso: unu klako metas la formon</li>
            <li>Por linio/sago: du klakoj por komenca kaj fina punktoj</li>
            </ul>
        </li>
        <li>Poziciigi formon: treni per muso</li>
        <li>Alĝustigi grandecon: treni ĉe la anguloj/randoj</li>
        <li>Konservi formon: <strong>Enter</strong></li>
        <li>Forĵeti formon: <strong>ESC</strong></li>
        <li>Pliaj ĝustigoj: dekstra klako sur formo</li>
        </ol>
        <p><strong>Konsilo:</strong> En la kunteksta menuo vi povas ĝustigi agordojn.</p>
        """,
        'form_guide_voice': "Mallonga instrukcio pri formoj. Elektu tipon. Por rektangulo aŭ elipso klaku unufoje, por linio aŭ sago dufoje. Poziciigu per muso, alĝustigu per anguloj. Konservu per Enter, forĵetu per Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "antaŭa",
        "btn_next_result": "sekva",
        "ocr_text_window": "Fenestro de OCR-teksto",
        "bookmark_existing": "Ekzistantaj legosignoj",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Komparo OCR Mac - Windows",
        'ocr_method_mac_win_title': "Diferencoj de OCR inter Mac kaj Windows",
        'ocr_method_mac_win_voice': "Mac estas pli bona",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – diferencoj inter macOS kaj Windows</strong></p>

        <p><strong>macOS (rekomendata)</strong></p>
        <p>Ilo:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Rezulto:</p>
        <ul>
        <li>Serĉebla PDF kun enigita teksto, kiu plejparte konservas la originalan aranĝon.</li>
        </ul>
        <p>Avantaĝoj:</p>
        <ul>
        <li>Elstara kvalito de tekst-rekono (ankaŭ por kurbaj paĝoj).</li>
        <li>Konservo de vektoraj grafikaĵoj kaj tiparoj.</li>
        <li>GUI-progresbreto per subprocess-evaluo.</li>
        <li>Plena kontrolo pri ĉiuj OCR-parametroj (Deskew, Clean, Oversample, optimumigo).</li>
        <li>La tekstserĉo rekte havebla en la ĉefa fenestro (PDF-vido).</li>
        </ul>
        <p>Malavantaĝoj:</p>
        <ul>
        <li>Bezonas pliajn sistemajn ilojn (ocrmypdf, Ghostscript, unpaper, pngquant – enhavitaj en la aplikaĵo).</li>
        <li>Pli kompleksa erarprilaborado (blokadoj, tempolimoj).</li>
        </ul>

        <p><strong>Windows (stabila alternativo)</strong></p>
        <p>Ilo:</p>
        <ul>
        <li>pytesseract (rekta ligo al Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Rezulto:</p>
        <ul>
        <li>Serĉebla PDF, kiu vide aspektas kiel bilda PDF, sed estas serĉebla per travidebla teksto.</li>
        </ul>
        <p>Avantaĝoj:</p>
        <ul>
        <li>Neniuj venas al miaj kalkuloj.</li>
        </ul>
        <p>Malavantaĝoj:</p>
        <ul>
        <li>La PDF estas esence bildo kun nevidebla teksto; la aranĝo povas iomete diferenci ĉe kompleksaj dokumentoj (kolumnoj, tabeloj).</li>
        <li>Neniu aŭtomata korekto de kliniteco (--deskew) aŭ bildpurigo (--clean).</li>
        <li>La GUI-progresbreto estas ĝisdatigita nur malglate laŭ la nombro de prilaboritaj paĝoj.</li>
        <li>La rapido de OCR estas iomete pli malrapida (ĉar ĉiu paĝo estas prilaborita aparte).</li>
        <li>La serĉo de teksto estas direktita al la fenestro de OCR-teksto.</li>
        </ul>

        <p><strong>Komunaĵoj</strong></p>
        <ul>
        <li>Ambaŭ metodoj kreas serĉeblan PDF en la sama dosierujo kiel la fonta dosiero.</li>
        <li>La OCR-agordoj (lingvo, DPI, paĝo-segmentada reĝimo, OCR-motoro-reĝimo) povas esti agorditaj per OCRSettingsDialog kaj efikas en ambaŭ implementoj.</li>
        </ul>

        <p><strong>Rekomendo:</strong></p>
        <ul>
        <li>macOS: La binara ocrmypdf liveras la plej bonajn rezultojn – aĉetu Mac-on kaj uzu la version (PDFDarkView por Mac-oj kun Apple Silicon aŭ Intel-ĉipo). La OCR-rezultoj estas pli bonaj ol sub Windows!</li>
        <li>Windows: Uzu la pytesseract-solvon. Ĝi estas stabila kaj liveras por la plej multaj dokumentoj sufiĉe bonan kvaliton.</li>
        </ul>

        <p><strong>Gravaj notoj:</strong></p>
        <ul>
        <li>Ambaŭ versioj estas plene integritaj en la uzantinterfacon – la uzanto ne rimarkas diferencon.</li>
        <li>La decido, kiu OCR-motoro estos uzata, estas farita aŭtomate de la programo surbaze de la operaciumo.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Krei subskribon (el skano)",
        "signature_create_title": "Elekti skanitan subskribon (PDF/bildo)",
        "image_pdf_filter": "Bildoj kaj PDF",
        "signature_pdf_empty": "La PDF ne enhavas paĝojn.",
        "signature_created_success": "Subskribo sukcese kreita: {0}",
        "signature_create_error": "Eraro dum kreado de subskribo:\n{0}",
        "rembg_missing": "rembg ne estas instalita.\nBonvolu instali: pip install rembg\nEraro: {0}",
        "signature_name_title": "Dosiernomo por la subskribo",
        "signature_name_message": "Bonvolu doni dosiernomon por la nova subskribo (estos konservita kiel PNG kun travidebla fono):",
        "signature_name_label": "Dosiernomo:",
        "signature_name_voice": "Enigu dosiernomon por la subskribo",
        "signature_processing": "Prilaborado...",
        "signature_creation_title": "Kreado de subskribo",
        "signature_overwrite_warning": "La dosiero '{0}' jam ekzistas. Ĉu anstataŭigi?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Preparado de PDF por subskribo",
        "signature_prepare_instruction":"Bonvolu elekti PDF, kiu sur ununura paĝo enhavas skanitan subskribon.\n\nOptimuman rekonon vi atingas, se:\n• La subskribo estas skribita per nigra inko (globkrajono aŭ fajnlinio) sur blanka papero.\n• La subskribo troviĝas en la supra triono de la alie malplena A4-paĝo.\n• La PDF estis skanita kun almenaŭ 300 dpi.\n• La subskribo estas klara kaj ne tro maldika.\n• Ne estas ĝenaj fonaj ŝablonoj aŭ linioj.",
        "signature_prepare_voice":"Bonvolu elekti PDF kun skanita subskribo. Atentu bonan kvaliton kaj kontraston.",
        "sig_thickness_label":"Dikeco de linio:",
        "sig_thickness_normal":"Normala (maldika)",
        "sig_thickness_bold":"Dika (rekomendata)",
        "sig_thickness_very_bold":"Tre dika",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Aldoni GUI- kaj OCR-lingvojn – instrukcio",
        'language_guide_title': "Aldoni GUI- kaj OCR-lingvojn",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Elŝutu la deziratan tradukan dosieron <code>translations_xy.py</code> de<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        kaj metu ĝin en la sekvan dosierujon:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Malfermu vian retumilon.</li>
        <li>Iru al: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Serĉu dekstre de la ekrano "Releases" kaj elektu la markitan <strong>"latest"</strong>.</li>
        <li>Sur la sekva eldonpaĝo elŝutu malsupre la dosieron <code>Source Code.zip</code>.</li>
        <li>Malpakumu la ZIP-dosieron.</li>
        <li>En la malpakumita dosierujo trovu ĉiujn bezonatajn lingvajn dosierojn kaj kopiu ilin en la dosierujon:<br/>
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
        "menu_watermark":"Enmeti akvomarkon",
        "fullpage_text_watermark_title":"Akvomarko (teksto)",
        "fullpage_image_watermark_title":"Akvomarko (bildo)",
        "filename_with_watermark":"_kun_akvomarko",

        # ===== DIALOG TEXTE =====
        "watermark_text":"Teksto:",
        "watermark_text_placeholder":"Via akvomarka teksto...",
        "watermark_font_family":"Tiparo:",
        "watermark_font_size":"Tipara grando:",
        "watermark_format":"Formatado:",
        "watermark_bold":"Grasa",
        "watermark_italic":"Kursiva",
        "watermark_color":"Koloro:",
        "watermark_choose_color":"Elekti koloron...",
        "watermark_opacity":"Travidebleco / opakeco:",
        "watermark_direction":"Legdirekto:",
        "watermark_direction_l_r":"Maldekstro → Dekstro",
        "watermark_direction_bl_tr":"Malsupra maldekstro → Supra dekstro",
        "watermark_direction_tl_br":"Supra maldekstro → Malsupra dekstro",
        "watermark_direction_b_t":"Malsupre → Supre",
        "watermark_direction_t_b":"Supre → Malsupre",
        "watermark_preview":"Antaŭvido:",
        "watermark_preview_sample":"Ekzempla teksto",
        "watermark_empty_text":"Bonvolu enigi tekston.",
        "watermark_applied":"Akvomarko estis aplikita al ĉiuj paĝoj.",
        "watermark_saved":"Akvomarko konservita.",

        # ===== DIALOG BILD =====
        "image_scale":"Grandeco:",
        "image_preview":"Antaŭvido de bildo:",
        "no_image_selected":"Neniu bildo elektita",
        "browse":"Foliumi...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI (REDAKTION)
        # ============================================
        "menu_redact": "Forigoj",
        "redact_add_black": "Forigo (nigra)",
        "redact_add_white": "Forigo (blanka / forviŝi)",
        "redact_added_black": "Aldono de nigra forigo",
        "redact_added_white": "Aldono de blanka forigo",
        "redact_apply_all": "Apliki kaj konservi ĉiujn forigojn",
        "redact_discard_all": "Forĵeti ĉiujn forigojn",
        "redact_discard": "Forĵeti ĉi tiun forigon",
        "no_redactions": "Neniuj forigoj ekzistas",
        "redact_confirm_title": "Tutdaŭre apliki forigojn",
        "redact_confirm_message": "Atentu: La markitaj areoj estos nerevokeble forigitaj (nigre aŭ blanke).\nSekurkopio estos kreita (se aktivigita).\n\nDaŭrigi?",
        "redact_apply": "Jes, forigi nun",
        "redact_saved": "{0} forigo(j) sukcese aplikitaj kaj konservitaj.",
        "redact_saved_voice": "Aplikitaj {0} forigo(j)",
        "redact_error": "Eraro dum forigo",
        "filename_redacted":"_kun_forigoj",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        # Dialog-Titel und Beschriftungen
        'page_numbers_title': 'Enmeti paĝnumerojn',
        'page_numbers_format': 'Formo de numeroj:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabaj)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romaj minuskloj)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romaj majuskloj)',
        'page_numbers_format_letter': 'A, B, C ... (literoj)',
        'page_numbers_format_custom': 'Propra',
        'page_numbers_custom_pattern': 'Ŝablono:',
        'page_numbers_custom_placeholder': 'ekz. "Paĝo {nummer}" aŭ "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Uzu {nummer} por la nuna paĝnumero kaj {total} por la tuta kvanto',
        'page_numbers_position': 'Pozicio:',
        'page_numbers_pos_tl': 'Supra maldekstro',
        'page_numbers_pos_tc': 'Supra centro',
        'page_numbers_pos_tr': 'Supra dekstro',
        'page_numbers_pos_ml': 'Meza maldekstro',
        'page_numbers_pos_mc': 'Centro',
        'page_numbers_pos_mr': 'Meza dekstro',
        'page_numbers_pos_bl': 'Malsupra maldekstro',
        'page_numbers_pos_bc': 'Malsupra centro',
        'page_numbers_pos_br': 'Malsupra dekstro',
        'page_numbers_margins': 'Marĝenoj:',
        'page_numbers_margin_x': 'Horizontala marĝeno:',
        'page_numbers_margin_y': 'Vertikala marĝeno:',
        'page_numbers_range': 'Paĝa intervalo:',
        'page_numbers_all_pages': 'Ĉiuj paĝoj',
        'page_numbers_custom_range': 'Propra intervalo',
        'page_numbers_from': 'De:',
        'page_numbers_to': 'Ĝis:',
        'page_numbers_progress': 'Enmeto de paĝnumeroj...',
        'page_numbers_start': 'Komenco de enmeto de paĝnumeroj...',
        'page_numbers_cancel': 'Enmeto de paĝnumeroj nuligita',
        'page_numbers_success': 'Paĝnumeroj sukcese aldonitaj.\n\nĈu vi volas malfermi la novan PDF?\n\n{0}',
        'page_numbers_complete': 'Paĝnumeroj aldonitaj',
        'page_numbers_error_format': 'Eraro dum enmeto de paĝnumeroj: {0}',
        # Zusätzliche Übersetzungen für den erweiterten Dialog
        'page_numbers_content_type': 'Tipo de enhavo:',
        'page_numbers_tab_simple': 'Simpla numero',
        'page_numbers_tab_range': 'Paĝo X el Y',
        'page_numbers_tab_date': 'Dato',
        'page_numbers_tab_custom': 'Libera teksto',
        'page_numbers_range_format': 'Formo:',
        'page_numbers_range_short': '{aktuala}/{tuta}',
        'page_numbers_range_long': 'Paĝo {aktuala} el {tuta}',
        'page_numbers_range_custom': 'Propra',
        'page_numbers_range_placeholder': 'ekz. "Paĝo {aktuala} / {tuta}"',
        'page_numbers_date_format': 'Formo de dato:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1-a de januaro 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Propra',
        'page_numbers_date_placeholder': 'ekz. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Pozicio:',
        'page_numbers_date_before': 'Dato antaŭ paĝnumero',
        'page_numbers_date_after': 'Dato post paĝnumero',
        'page_numbers_date_only': 'Nur dato (sen paĝnumero)',
        'page_numbers_custom_text': 'Propra teksto:',
        'page_numbers_custom_placeholder_text': 'Uzu {paĝo} por la paĝnumero kaj {tuta} por la tuta kvanto\nekz. "Konfidenca - paĝo {paĝo}" aŭ "{paĝo} el {tuta}"',
        "filename_with_page_number":"_kun_paĝnumero",
        "filename_with_page_declaration":"_kun_paĝindiko",
        "filename_with_pagenumber":"_kun_paĝnumero",
        "filename_with_date":"_kun_dato",
        "filename_with_my_page_declaration":"_kun_propra_paĝindiko",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Ne konservitaj ŝanĝoj",
        "unsaved_changes_message_darkmode": "Estas ne konservitaj enmetoj.\nĈu vi volas konservi ilin antaŭ ŝalti?",
        "save_and_switch": "Konservi kaj ŝalti",
        "discard_and_switch": "Ŝalti nun",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        # Export Images Dialog
        'export_images_title': 'Eksporti paĝojn kiel bildojn',
        'export_images_menu': 'Eksporti kiel bildoj (PNG/JPEG)',
        'export_images_format': 'Formo de bildo:',
        'export_images_dpi': 'Distancaĵo (DPI):',
        'export_images_quality': 'Kvalito de JPEG:',
        'export_images_range': 'Paĝa intervalo:',
        'export_images_all_pages': 'Ĉiuj paĝoj',
        'export_images_custom_range': 'Propra intervalo',
        'export_images_from': 'De:',
        'export_images_to': 'Ĝis:',
        'export_images_options': 'Opcioj:',
        'export_images_single_files': 'Ĉiu paĝo kiel aparta dosiero',
        'export_images_subfolder': 'Eksporti en subdosierujon',
        'export_images_subfolder_info': 'En subdosierujon "NomoPDF_bildoj"',
        'export_images_same_folder': 'En la sama dosierujo kiel la PDF',
        'export_images_apply_darkmode': 'Apliki agordojn de PDFDarkView (malhela reĝimo)',
        'export_images_target_folder': 'Cela dosierujo:',
        'export_images_browse': 'Foliumi...',
        'export_images_preview': 'Antaŭvido:',
        'export_images_preview_info': 'Elektu agordojn por la eksporto',
        'export_images_preview_info_detail': '{0} paĝoj kiel {1}\nDistancaĵo: {2} DPI\nDosiernomo: {3}\n{4}',
        'export_images_select_folder': 'Elekti celan dosierujon',
        'export_images_start': 'Komenco de bild-eksporto...',
        'export_images_progress': 'Eksportado de bildoj...',
        'export_images_saving': 'Konservado de paĝo {0} el {1}...',
        'export_images_success': 'Eksporto sukcesis!\n\n{0} bildoj konservitaj en:\n{1}',
        'export_images_complete': 'Bild-eksporto finita',
        'export_images_open_folder': '📁 Malfermi dosierujon',
        'export_images_cancel': 'Bild-eksporto nuligita',
        'export_images_error_format': 'Eraro dum eksporto de bildoj: {0}',
        'export_images_pdf2image_missing': 'La biblioteko "pdf2image" ne estas instalita.\n\nBonvolu instali ĝin per:\npip install pdf2image\n\nPor Windows vi ankaŭ bezonas Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        # PDF/A Dialog
        'pdfa_title': 'Konvertado al PDF/A por longdaŭra arkivado',
        'pdfa_menu': 'Konvertado al PDF/A (arkiv-taŭga)',
        'pdfa_info': 'Konvertas la PDF al PDF/A-formo.\n\nPDF/A estas speciale evoluigita por longdaŭra arkivado kaj certigas, ke la dokumento estos ĝuste montrata ankaŭ en la estonteco.',
        'pdfa_standard': 'Normo PDF/A:',
        'pdfa_standard_select': 'Versio:',
        'pdfa_1': 'PDF/A-1 (simpla, larĝe kongrua)',
        'pdfa_2': 'PDF/A-2 (moderna, pli bona kompreso)',
        'pdfa_3': 'PDF/A-3 (plej nova versio, permesas aldonaĵojn)',
        'pdfa_standards_explanation': '📖 Klarigo de normoj:\n\n'
            '• PDF/A-1: Baza, kongrua kun malnovaj sistemoj (ĉ. 2005)\n'
            '• PDF/A-2: Pli moderna, pli bona kompreso, subteno de travidebleco (ĉ. 2011)\n'
            '• PDF/A-3: Plej nova versio, permesas enmeti dosierojn (ĉ. 2013)\n\n'
            'Rekomendo: PDF/A-2 estas bona kompromiso inter kongrueco kaj modernaj funkcioj.',
        'pdfa_options': 'Opcioj:',
        'pdfa_compress_enable': 'Kompresi PDF (pli malgranda dosiero)',
        'pdfa_metadata_preserve': 'Konservi metadatenojn (titolo, aŭtoro, ktp.)',
        'pdfa_target_folder': 'Cela dosierujo:',
        'pdfa_browse': 'Foliumi...',
        'pdfa_select_folder': 'Elekti celan dosierujon',
        'pdfa_ocr_info_unknown': '🔍 Ne eblis kontroli la enhavon de teksto.',
        'pdfa_ocr_info_not_needed': '✅ Teksto ekzistas - OCR ne estas necesa.\nPDF/A povas esti kreita rekte.',
        'pdfa_ocr_info_recommended': '⚠️ Ne sufiĉa teksto trovita.\n\nPor serĉeblaj PDF-oj ni rekomendas antaŭe fari OCR.\nNoto: PDF/A funkcias ankaŭ sen OCR - la teksto tiam ne estos serĉebla.',
        'pdfa_ocr_info_error': '❌ Eraro dum kontrolo: {0}',
        'pdfa_start': 'Komenco de konvertado al PDF/A...',
        'pdfa_progress': 'Konvertado al PDF/A okazas...',
        'pdfa_success': 'Konvertado al PDF/A sukcesis!\n\nKonservita kiel:\n{0}\n\nĈu vi volas malfermi la novan PDF?',
        'pdfa_complete': 'Konvertado al PDF/A finita',
        'pdfa_cancel': 'Konvertado al PDF/A nuligita',
        'pdfa_error_format': 'Eraro dum konvertado al PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'La biblioteko "ocrmypdf" ne estas instalita.\n\nBonvolu instali ĝin per:\npip install ocrmypdf',
        'btn_convert': 'Konverti',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        ### ------------------------------------
        ### 95. OPTIMIEREN (KOMPIMIEREN)
        ### ------------------------------------
        # ===== PDF OPTIMIEREN =====
        'optimize_title': 'Optimumigi PDF (malpligrandigi dosiergrandon)',
        'optimize_menu': 'Optimumigi PDF (grandeco)',
        'optimize_info': 'Malpligrandigas la dosiergrandon de la PDF per diversaj optimumigaj metodoj.\n\nJu pli alta la kompresa nivelo, des pli malgranda la dosiero – kun ebla kvalita perdo ĉe bildoj.',
        'optimize_level': 'Kompresa nivelo:',
        'optimize_level_low': 'Malalta (rapida, malgranda ŝparo)',
        'optimize_level_medium': 'Meza (bona kompromiso)',
        'optimize_level_high': 'Alta (granda ŝparo)',
        'optimize_level_maximum': 'Maksimuma (maksimuma ŝparo, malrapida)',
        'optimize_level_explanation': 'Rekomendo: "Meza" estas bona kompromiso inter rapido kaj dosiergrandeco.',
        'optimize_options': 'Opcioj:',
        'optimize_compress_images': 'Kompresi bildojn (malpligrandigi JPEG-kvaliton)',
        'optimize_clean_objects': 'Forigi neuzatajn objektojn',
        'optimize_preserve_metadata': 'Konservi metadatenojn (titolo, aŭtoro, ktp.)',
        'optimize_image_quality': 'Kvalito de bildoj:',
        'optimize_range': 'Paĝa intervalo:',
        'optimize_all_pages': 'Ĉiuj paĝoj',
        'optimize_custom_range': 'Propra intervalo',
        'optimize_from': 'De:',
        'optimize_to': 'Ĝis:',
        'optimize_target_folder': 'Cela dosierujo:',
        'optimize_browse': 'Foliumi...',
        'optimize_select_folder': 'Elekti celan dosierujon',
        'optimize_info_box': 'Informoj',
        'optimize_info_text': 'La optimumigo de grandaj PDF-oj povas daŭri plurajn minutojn.\n\nBildoj estas konservitaj kun malpligrandigita kvalito, kio povas signife malpligrandigi la dosiergrandon.',
        'optimize_start': 'Komenco de optimumigo de PDF...',
        'optimize_progress': 'Optimumigo de PDF okazas...',
        'optimize_cancel': 'Optimumigo de PDF nuligita',
        'optimize_complete': 'Optimumigo de PDF finita',
        'optimize_error_format': 'Eraro dum optimumigo de PDF:\n\n{0}',
        # Erfolgsmeldungen (mit Platzhaltern)
        'optimize_success_message': 'Optimumigo de PDF sukcesis!\n\nKonservita kiel:\n{0}\n\nAntaŭe:  {1}\nPoste:   {2}\nŜparo: {3:.1f}%\n\n{4}\n\nĈu vi volas malfermi la optimumigitan PDF?',
        'optimize_success_message_no_size': 'Optimumigo de PDF sukcesis!\n\nKonservita kiel:\n{0}\n\nInformo pri grandeco ne disponebla.\n\nĈu vi volas malfermi la optimumigitan PDF?',
        # Ergebnis-Texte
        'optimize_result_positive': 'La dosiero estis malpligrandigita je {0:.1f}%.',
        'optimize_result_zero': 'Neniu ŝanĝo de dosiergrandeco.',
        'optimize_result_negative': 'La dosiero estas pli granda je {0:.1f}%.\nLa optimumigo estis preterlasita, la originala dosiero estis konservita.',
        'btn_optimize': 'Komenci optimumigon',
        # Dateinamen-Suffixe
        'filename_optimize_low_suffix': '_optimumigita_malalta',
        'filename_optimize_medium_suffix': '_optimumigita',
        'filename_optimize_high_suffix': '_optimumigita_alta',
        'filename_optimize_maximum_suffix': '_optimumigita_max',

        ### ------------------------------------
        ### 96. ZUSCHNEIDEN CROPPING
        ### ------------------------------------
        # ===== PDF ZUSCHNEIDEN =====
        # Crop Dialog
        'crop_title': 'Tondi PDF',
        'crop_menu': 'Tondi PDF',
        'crop_range': 'Apliki al:',
        'crop_all_pages': 'Ĉiuj paĝoj',
        'crop_current_page': 'Nur nuna paĝo',
        'crop_values': 'Tondaj valoroj (en punktoj):',
        'crop_left': 'Maldekstro:',
        'crop_right': 'Dekstro:',
        'crop_top': 'Supro:',
        'crop_bottom': 'Malsupro:',
        'crop_presets': 'Antaŭdifinitaj:',
        'crop_preset_white': 'Detekti blankajn marĝenojn',
        'crop_reset': 'Resetigi',
        'crop_mouse_hint': '🖱️ Trenu rektangulon por malglate elekti la areon.\nPoste vi povas precizigi la valorojn en la spinujoj.\nPermana ĝustigo per muso ne eblas.',
        'crop_apply': 'Tondi',
        'crop_scope_all': 'Ĉiuj paĝoj',
        'crop_scope_current': 'Nuna paĝo',
        'crop_new_size': 'Nova grandeco: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Neniu PDF ŝargita',
        'crop_preview_error': 'Eraro dum ŝargado de antaŭvido',
        'crop_start': 'Komenco de tondado...',
        'crop_progress': 'Tondado de PDF okazas...',
        'crop_success': 'PDF sukcese tondita!\n\nKonservita kiel:\n{0}\n\nĈu vi volas malfermi la tonditan PDF?',
        'crop_complete': 'Tondado finita',
        'crop_cancel': 'Tondado nuligita',
        'crop_error_format': 'Eraro dum tondado:\n\n{0}',
        'filename_crop_suffix': '_tondita',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        # ===== PDF GLÄTTEN =====
        'flatten_title': 'Glatigi PDF (Flatten)',
        'flatten_menu': 'Glatigi PDF (Flatten)',
        'flatten_info': 'Glatigado de PDF "enbruligas" ĉiujn redakteblajn elementojn en la paĝan enhavon.\n\nPoste formularoj, notoj, tekstoj, krucoj, subskriboj, bildoj kaj formoj ne plu estas redakteblaj individue.',
        'flatten_explanation_title': '📖 Por kio tio utilas?',
        'flatten_explanation_text': 'Glatigado estas bezonata en la sekvaj situacioj:\n\n'
            '• 📄 Preparo de dokumento por presado\n'
            '• 🔒 Malhelpi ŝanĝojn de formularaj kampoj\n'
            '• 📎 Tute enigi notojn kaj komentojn en la dokumenton\n'
            '• 🖼️ Tute enigi enmetitajn tekstojn, krucojn, subskribojn, bildojn kaj formojn\n'
            '• 📦 Preparo de dosiero por arkivado\n\n'
            'Glatigado malpligrandigas la PDF kaj malhelpas hazardan movadon aŭ forigon de elementoj.',
        'flatten_what_title': 'Kio estas glatigata?',
        'flatten_what_list': '• ✅ Formularaj kampoj (tekstaj kampoj, markobutonoj, butonoj)\n'
            '• ✅ Notoj (komentoj, emfazoj, notoj)\n'
            '• ✅ Supermetaĵoj (tekstoj, krucoj, subskriboj, bildoj, formoj)',
        'flatten_options': 'Opcioj:',
        'flatten_forms': 'Glatigi formularajn kampojn',
        'flatten_annotations': 'Glatigi notojn',
        'flatten_overlays': 'Glatigi supermetaĵojn (tekstoj, krucoj, subskriboj, bildoj, formoj)',
        'flatten_target_folder': 'Cela dosierujo:',
        'flatten_browse': 'Foliumi...',
        'flatten_select_folder': 'Elekti celan dosierujon',
        'flatten_warning': '⚠️ Grava: Glatigado estas nerevokeble!\n\nPost glatigado redakteblaj elementoj ne plu povas esti ŝanĝitaj aŭ forigitaj individue.\n\nSe necese, kreu antaŭe sekurkopion.',
        'flatten_apply': 'Glatigi',
        'flatten_start': 'Komenco de glatigado...',
        'flatten_progress': 'Glatigado de PDF okazas...',
        'flatten_success': 'PDF sukcese glatigita!\n\nKonservita kiel:\n{0}\n\nĈu vi volas malfermi la glatigitan PDF?',
        'flatten_complete': 'Glatigado finita',
        'flatten_cancel': 'Glatigado nuligita',
        'flatten_error_format': 'Eraro dum glatigado:\n\n{0}',
        'filename_flatten_suffix': '_glatigita',

        ### ------------------------------------
        ### 98. PDF ÜBEREINANDERLEGEN OVERLAY
        ### ------------------------------------
        'overlay_title': 'Supermeti PDF (Overlay)',
        'overlay_menu': 'Supermeti PDF (Overlay)',
        'overlay_info': 'Supermetas unu PDF (supermetaĵon) super alian PDF.\n\nLa supermetaĵa PDF estas metita sur la baza PDF. Utilas por akvomarkoj, emblemoj, leterkapoj aŭ stampoj.',
        'overlay_explanation_title': '📖 Por kio tio utilas?',
        'overlay_explanation_text': 'Supermetado estas bezonata en la sekvaj situacioj:\n\n'
            '• 🏢 Meti firmaan emblemon kiel akvomarkon sur ĉiu paĝo\n'
            '• 📄 Meti leterkapon sur malplenan PDF\n'
            '• 🖊️ Meti stampan supermetaĵon sur dokumenton\n'
            '• 🔖 Meti akvomarkon sur ĉiujn paĝojn\n'
            '• 📑 Meti formularan supermetaĵon sur ŝablonon',
        'overlay_type': 'Tipo de supermetaĵo:',
        'overlay_type_fullpage': 'Tuta paĝo (kovra)',
        'overlay_type_transparent': 'Tuta paĝo (travidebla - rekomendata)',
        'overlay_type_stamp': 'Stampo (poziciigebla)',
        'overlay_type_info_fullpage': '📄 La supermetaĵa PDF estas metita ekzakte super la tutan paĝon.\nLa blanka fono povas esti forigita, tiel ke nur la enhavo restas videbla.',
        'overlay_type_info_transparent': '🔍 La supermetaĵa PDF estas metita super la tutan paĝon kun travidebla fono.\nLa blanka fono estas aŭtomate forigita – ideala por akvomarkoj kaj emblemoj!',
        'overlay_type_info_stamp': '🖊️ La supermetaĵa PDF estas poziciigita kaj skalita kiel stampo.\nPerfekta por emblemoj, stampoj aŭ subskriboj je certaj pozicioj.',
        'overlay_remove_background': 'Forigi blankan fonon:',
        'overlay_remove_background_enable': 'Forigi blankan fonon el la supermetaĵa PDF (faras ĝin travidebla)',
        'overlay_remove_background_tooltip': 'Forigas blankajn areojn el la supermetaĵa PDF, por ke la suba teksto fariĝu videbla.',
        'overlay_threshold': 'Sojlo:',
        'overlay_threshold_hint': '(1-254, pli alta = pli da blanko estas forigata)',
        'overlay_select_file': 'Elekti supermetaĵan PDF:',
        'overlay_file_placeholder': 'Bonvolu elekti PDF-dosieron por la supermetaĵo',
        'overlay_browse': 'Foliumi...',
        'overlay_select_overlay': 'Elekti supermetaĵan PDF',
        'overlay_range': 'Paĝa intervalo:',
        'overlay_all_pages': 'Ĉiuj paĝoj',
        'overlay_custom_range': 'Propra intervalo',
        'overlay_from': 'De:',
        'overlay_to': 'Ĝis:',
        'overlay_position': 'Pozicio:',
        'overlay_position_center': 'Centro',
        'overlay_position_top_left': 'Supra maldekstro',
        'overlay_position_top_right': 'Supra dekstro',
        'overlay_position_bottom_left': 'Malsupra maldekstro',
        'overlay_position_bottom_right': 'Malsupra dekstro',
        'overlay_size': 'Grandeco:',
        'overlay_size_original': 'Originala grandeco',
        'overlay_size_fit_page': 'Alĝustigi al paĝo',
        'overlay_size_custom': 'Propra (%)',
        'overlay_opacity': 'Travidebleco:',
        'overlay_target_folder': 'Cela dosierujo:',
        'overlay_browse_folder': 'Foliumi...',
        'overlay_select_folder': 'Elekti celan dosierujon',
        'overlay_warning': '⚠️ Noto: La supermetaĵa PDF estas "enbruligita" en la baza PDF.\n\nLa elementoj de la supermetaĵo ne plu povas esti redaktitaj individue post konservado.',
        'overlay_apply': 'Supermeti',
        'overlay_start': 'Komenco de supermetado...',
        'overlay_progress': 'Supermetado de PDF okazas...',
        'overlay_success': 'Supermetado de PDF sukcesis!\n\nKonservita kiel:\n{0}\n\nĈu vi volas malfermi la supermetitan PDF?',
        'overlay_complete': 'Supermetado finita',
        'overlay_cancel': 'Supermetado nuligita',
        'overlay_error_format': 'Eraro dum supermetado:\n\n{0}',
        'overlay_no_file': 'Neniu supermetaĵa PDF elektita.\n\nBonvolu elekti PDF-dosieron por supermeti.',
        'filename_overlay_suffix': '_supermetita',

        ###==============================================
        ### 99. ALLE BILDER EXPTRAHIEREN
        ###==============================================
        'extract_images_title': 'Eltiri bildojn el PDF',
        'extract_images_menu': 'Eltiri ĉiujn bildojn',
        'extract_images_info': 'Eltiras ĉiujn bildojn el la PDF kaj konservas ilin kiel apartajn dosierojn.\n\nLa bildoj estas konservitaj en sia originala formato aŭ konvertitaj al elektita formato.',
        'extract_images_format': 'Formo de bildo:',
        'extract_images_quality': 'Kvalito de JPEG:',
        'extract_images_options': 'Opcioj:',
        'extract_images_subfolder': 'Eltiri en subdosierujon ("NomoPDF_bildoj")',
        'extract_images_unique': 'Nur unikaj bildoj (eviti duoblaĵojn)',
        'extract_images_range': 'Paĝa intervalo:',
        'extract_images_all_pages': 'Ĉiuj paĝoj',
        'extract_images_custom_range': 'Propra intervalo',
        'extract_images_from': 'De:',
        'extract_images_to': 'Ĝis:',
        'extract_images_target_folder': 'Cela dosierujo:',
        'extract_images_browse': 'Foliumi...',
        'extract_images_select_folder': 'Elekti celan dosierujon',
        'extract_images_info_box': 'Informoj',
        'extract_images_info_text': 'La eltiro povas daŭri plurajn minutojn por grandaj PDF-oj.\n\nBildoj estas konservitaj kun nomoj (paĝo_bildo).',
        'extract_images_extract': 'Eltiri',
        'extract_images_start': 'Komenco de eltiro...',
        'extract_images_progress': 'Eltiro de bildoj okazas...',
        'extract_images_success': '✅ Bildoj sukcese eltiritaj!\n\n{0} bildoj konservitaj en:\n{1}',
        'extract_images_complete': 'Eltiro de bildoj finita',
        'extract_images_cancel': 'Eltiro nuligita',
        'extract_images_error_format': 'Eraro dum eltiro de bildoj:\n\n{0}',
        'extract_images_open_folder': '📁 Malfermi dosierujon',
        'extract_images_no_images': 'Neniuj bildoj trovitaj en la PDF.',

        ### ------------------------
        ### 100.MEHRERE SEITEN AUF EINE SEITE
        ### ------------------------
        'nup_title': 'Pluraj paĝoj sur unu paĝo (N-Up)',
        'nup_menu': 'Pluraj paĝoj sur unu paĝo (N-Up)',
        'nup_info': 'Arangas plurajn PDF-paĝojn sur unu paĝo.\n\nIdeala por kompaktaj presaĵoj, superrigardoj aŭ manlibroj.',
        'nup_layout': 'Arangxo:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Antaŭvido:',
        'nup_preview_info': '{0} paĝoj → {1} paĝoj po folio → {2} folioj\nArangxo: {3}',
        'nup_order': 'Ordo:',
        'nup_order_horizontal': 'Horizontale (vicoj)',
        'nup_order_vertical': 'Vertikale (kolumnoj)',
        'nup_order_horizontal_reverse': 'Horizontale return',
        'nup_order_vertical_reverse': 'Vertikale return',
        'nup_range': 'Paĝa intervalo:',
        'nup_all_pages': 'Ĉiuj paĝoj',
        'nup_custom_range': 'Propra intervalo',
        'nup_from': 'De:',
        'nup_to': 'Ĝis:',
        'nup_options': 'Opcioj:',
        'nup_margins': 'Marĝenoj:',
        'nup_margin_between': 'Spaco inter paĝoj:',
        'nup_page_numbers': 'Enmeti paĝnumerojn',
        'nup_target_folder': 'Cela dosierujo:',
        'nup_browse': 'Foliumi...',
        'nup_select_folder': 'Elekti celan dosierujon',
        'nup_create': 'Krei',
        'nup_start': 'Komenco de N-Up...',
        'nup_progress': 'Kreado de N-Up...',
        'nup_success': 'N-Up sukcese kreita!\n\nKonservita kiel:\n{0}\n\nĈu vi volas malfermi la novan PDF?',
        'nup_complete': 'N-Up finita',
        'nup_cancel': 'N-Up nuligita',
        'nup_error_format': 'Eraro dum N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        ###==============================================
        ### 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        ###==============================================
        'pagesize_title': 'Ŝanĝi paĝgrandecon',
        'pagesize_menu': 'Ŝanĝi paĝgrandecon',
        'pagesize_info': 'Ŝanĝas la paĝgrandecon de la PDF.\n\nLa enhavo estas aŭtomate alĝustigita al la nova grandeco.',
        'pagesize_format': 'Formato:',
        'pagesize_select': 'Elektu norman formaton:',
        'pagesize_custom': 'Propra grandeco:',
        'pagesize_width': 'Larĝo:',
        'pagesize_height': 'Alto:',
        'pagesize_orientation': 'Orientiĝo:',
        'pagesize_portrait': 'Portreta',
        'pagesize_landscape': 'Pejzaĝa',
        'pagesize_scale_options': 'Opcioj de skalo:',
        'pagesize_fit': 'Alĝustigi (konservi proporciojn)',
        'pagesize_stretch': 'Streĉi (distordi)',
        'pagesize_center': 'Centri (originala grandeco)',
        'pagesize_range': 'Paĝa intervalo:',
        'pagesize_all_pages': 'Ĉiuj paĝoj',
        'pagesize_custom_range': 'Propra intervalo',
        'pagesize_from': 'De:',
        'pagesize_to': 'Ĝis:',
        'pagesize_target_folder': 'Cela dosierujo:',
        'pagesize_browse': 'Foliumi...',
        'pagesize_select_folder': 'Elekti celan dosierujon',
        'pagesize_apply': 'Apliki',
        'pagesize_start': 'Komenco de ŝanĝo de paĝgrandeco...',
        'pagesize_progress': 'Ŝanĝo de paĝgrandeco okazas...',
        'pagesize_success': 'Paĝgrandeco sukcese ŝanĝita!\n\nKonservita kiel:\n{0}\n\nĈu vi volas malfermi la novan PDF?',
        'pagesize_complete': 'Ŝanĝo de paĝgrandeco finita',
        'pagesize_cancel': 'Ŝanĝo de paĝgrandeco nuligita',
        'pagesize_error_format': 'Eraro dum ŝanĝo de paĝgrandeco:\n\n{0}',
        'pagesize_preview_info': 'Nova grandeco: {0} x {1} pt',
        'filename_pagesize_suffix': '_nova_grandeco',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informoj pri PDF',
        'pdf_info_menu': 'Montri informojn pri PDF',
        'pdf_info_voice': 'Montri informojn pri PDF',
        'pdf_info_error': 'Eraro dum montrado de informoj pri PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Montri klavajn ŝparvojojn",
        "shortcuts_dialog_title": "Klavaj ŝparvojoj",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 DOSIERO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Malfermi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Fermi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Konservi kiel...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Protekti dokumenton</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Presi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Presi tuj (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Eliri el aplikaĵo</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORTO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Eksporti kiel Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Eksporti kiel DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Eksporti kiel TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Eksporti kiel bildoj (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Eltiri bildojn</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PRILABORADO DE DOKUMENTOJ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (pluraj paĝoj)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Konverti al PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Glatigi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Supermeti PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimumigi PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDAKTI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Serĉi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Aldoni legosignon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Administri legosignojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Sekva legosigno</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Antaŭa legosigno</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Fari OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 ADMINISTRADO DE PAĜOJ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Turni nunan paĝon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Turni ĉiujn paĝojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Rektigi nunan paĝon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Rektigi ĉiujn paĝojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Forigi paĝojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Eltiri paĝojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Enmeti paĝojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Movi paĝojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Kunfandi PDF-ojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Ŝanĝi paĝgrandecon</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 ENMETI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Enmeti tekston</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Enmeti krucon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Enmeti subskribon 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Enmeti subskribon 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Enmeti bildon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Enmeti rektangulon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Enmeti elipson</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Enmeti linion</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Enmeti sagon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Enmeti paĝnumerojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Akvomarko (teksto)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Akvomarko (bildo)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ FORIGOJ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Forigo (nigra)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Forigo (blanka)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Apliki ĉiujn forigojn</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ALTNIVELAJ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Tondi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Redakti metadatenojn</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VIDO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Ŝalti malhelan/helan reĝimon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Montri tekstfenestron</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Paĝlarĝo (zomo)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Du paĝoj (zomo)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Superrigardo (zomo)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ AGORDOJ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Administrado de pasvortoj</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Agordoj de OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Agordoj de subskribo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formatado de dosiernomoj</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Eksporti agordojn</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importi agordojn</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMOJ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Montri informojn pri PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Ŝalti/malŝalti paroladon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokusigi menubreton</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nova versio disponebla",
        "update_available_message": "Nova versio <b>{0}</b> estas disponebla.\n\nVizitu la eldonpaĝon por elŝuti la ĝisdatigon:\n{1}",
        "update_available_voice": "Nova versio {0} disponebla. Bonvolu elŝuti la ĝisdatigon de la GitHub-paĝo.",
        "update_open_release": "Malfermi eldonpaĝon",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Elŝuti ĉiujn tradukojn",
        "ask_download_all_translations": """Krom la germana, angla kaj vjetnama estas ankoraŭ {total_languages} aliaj GUI-lingvoj disponeblaj.\n\nĈu elŝuti / ĝisdatigi ilin?\n\nNoto:\nNecesajn lingvojn vi povas poste forigi permane el la dosierujo:\n{translations_path}\n\nSe vi nuligas, vi povos poste elŝuti la GUI-lingvojn per la menuo 'Iloj → Ĝisdatigi tradukojn'.""",
        "menu_update_translations": "Ĝisdatigi tradukojn",
        "translations_updated": "Tradukoj ĝisdatigitaj",
        "translations_update_success": "Sukcese ĝisdatigitaj {} tradukoj ({} novaj, {} ĝisdatigitaj).",
        "translations_update_error": "Eraro dum ĝisdatigo de tradukoj",
        "translations_update_no_changes": "Ĉiuj tradukoj jam estas aktualaj.",
        "translations_update_offline": "Neniu interreta konekto. Ne eblis ĝisdatigi tradukojn.",
        "translations_update_in_progress": "Ĝisdatigo de tradukoj en fono...",
        "translations_downloading": "Elŝutado de tradukoj...",
        "translations_path_hint": "Uzanta dosierujo por tradukoj",
        "translations_update_not_available_title": "Ĝisdatigo ne disponebla",
        "translations_update_not_available_message": """Ĝisdatigo de tradukoj disponeblas nur en la instalita versio.\n\nEn evolua reĝimo la tradukoj jam estas aktualaj.""",
        "translations_update_no_internet_title": "Neniu interreta konekto",
        "translations_update_no_internet_message": """Ne eblis establi interretan konekton.\n\nLa tradukoj ne povas esti elŝutitaj de GitHub.\n\nEblaj solvoj:
        • Kontrolu vian interretan konekton
        • Provizore malŝalti eventualan fajroŝirmilon
        • Reprovi poste
        \nVi ankaŭ povas permane elŝuti la tradukojn de GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Ĝisdatigo jam okazas",
        "btn_retry": "Reprovi",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Bonvenon al PDF Dark View",
        "welcome_title_not_supported": "Bonvenon al PDF Dark View",
        "welcome_message": "Bonvenon al PDF Dark View!\n\nVia sistema lingvo estis detektita kiel '{language}'.\nĈu vi volas uzi ĉi tiun lingvon por la uzantinterfaco?\n\nVi povas ŝanĝi la lingvon iam ajn per 'Agordoj → Lingvo'.",
        "welcome_message_language_not_available": "Bonvenon al PDF Dark View!\n\nVia sistema lingvo estis detektita kiel '{language}'.\nĈi tiu lingvo ankoraŭ ne estas instalita.\n\nĈu vi volas elŝuti la tradukojn por {language} nun de GitHub?\n\n(La lingvo estos aŭtomate uzata por la interfaco.)",
        "welcome_message_language_not_supported": "Bonvenon al PDF Dark View!\n\nVia sistema lingvo estis detektita kiel '{language}'.\nBedaŭrinde, por ĉi tiu lingvo ankoraŭ ne ekzistas tradukoj.\n\nLa uzantinterfaco estos montrata en {fallback_language}.\n\nVi povas ŝanĝi la lingvon iam ajn per 'Agordoj → Lingvo'.\nSe vi volas, vi mem povas kontribui tradukon por via lingvo:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Jes, uzi sisteman lingvon",
        "welcome_keep_english": "Ne, konservi la anglan",
        "welcome_download_language": "Jes, elŝuti {language}",

        # ============================================
        # 107. ZULETZT VERWENDETE PFADE
        # ============================================

        'menu_recent': 'Laste uzitaj',
        'menu_recent_dirs': 'Dosierujoj...',
        'menu_recent_files': 'Dosieroj...',
        'recent_manage': 'Administri...',
        # Recent Paths - Einstellungen
        'recent_enable_tracking': 'Konservi laste uzitajn vojojn (datumprotekto)',
        'recent_enable_info': 'Malŝalti ĉi tiun opcion por ne konservi vojojn',
        'recent_tracking_disabled': 'Sekvado de vojoj malŝaltita',
        'recent_enabled': 'ŝaltita',
        'recent_disabled': 'malŝaltita',
        'recent_tracking_status': 'Sekvado de vojoj {0}',
        # Recent Paths - Dialog
        'recent_dialog_title': 'Laste uzitaj vojoj',
        'recent_tab_directories': 'Dosierujoj',
        'recent_tab_files': 'Dosieroj',
        'recent_dirs_instruction': 'Duobla klako por malfermi dosieran dialogon en la dosierujo',
        'recent_files_instruction': 'Duobla klako por rekte malfermi la PDF',
        'recent_no_directories': '(neniuj dosierujoj konservitaj)',
        'recent_no_files': '(neniuj dosieroj konservitaj)',
        'recent_default_current': '⭐ Defaŭlta: {0}',
        'recent_set_as_default': '⭐ Agordi kiel defaŭltan',
        'recent_default_set_title': 'Agordita defaŭlta dosierujo',
        'recent_default_set_message': 'La dosierujo "{0}" estis agordita kiel defaŭlta por malfermi PDF-ojn.',
        'recent_default_set_voice': 'Agordita defaŭlta dosierujo',
        'recent_directory_not_found': 'Dosierujo ne trovita',
        'recent_file_not_found': 'Dosiero ne trovita',
        'recent_remove_selected': 'Forigi',
        'recent_remove_title': 'Forigi vojon',
        'recent_remove_confirm': 'Ĉu vi certe volas forigi la vojon "{0}" el la listo?',
        'recent_path_removed': 'Vojo forigita',
        'recent_clear_all': 'Forigi ĉiujn',
        'recent_clear_title': 'Forigi ĉiujn vojojn',
        'recent_clear_confirm_type': 'Ĉu vi certe volas forigi ĉiujn {0}?',
        'recent_cleared': 'Listo forigita',
        'recent_path_not_found_title': 'Vojo ne trovita',
        'recent_path_not_found_message': 'La vojo "{0}" jam ne ekzistas.',
        'recent_open_file': 'Malfermi dosieron',
        'btn_open_recent': 'Malfermi',
        'recent_open_file_question': 'Ĉu vi volas malfermi "{0}" kiel PDF?',
        'recent_not_pdf': 'La elektita dosiero ne estas PDF.',
        'recent_more_entries': 'Pliaj eroj...',
        'btn_remove': 'Forigi',
        'btn_clear': 'Forigi ĉiujn',
        # Recent Paths - Context Menu
        'recent_context_open': 'Malfermi',
        'recent_context_reveal': 'Montri en Finder',
        'recent_context_set_default': '⭐ Agordi kiel defaŭltan',
        'recent_context_open_terminal': '💻 Malfermi terminalon',
        'recent_context_file_info': 'Informoj pri dosiero',
        'recent_context_open_with_default': '📄 Malfermi per defaŭlta aplikaĵo',
        'recent_context_remove': 'Forigi el listo',
        'recent_context_clear_all': 'Forigi ĉiujn',

        # Recent Paths - File Info
        'recent_file_info_title': 'Informoj pri dosiero',
        'recent_file_info_name': 'Nomo',
        'recent_file_info_path': 'Vojo',
        'recent_file_info_size': 'Grandeco',
        'recent_file_info_modified': 'Modifita',
        'recent_file_info_pages': 'Paĝoj',

        # Recent Paths - Errors
        'recent_error_reveal': 'Eraro dum malfermo en Finder',
        'recent_error_terminal': 'Eraro dum malfermo de terminalo',
        'recent_error_info': 'Eraro dum ricevo de informoj pri dosiero',
        'open_user_data_folder': 'Montri dosierujon de uzantaj datumoj',

        # ============================================
        # 108. GERADE UNGERADE SEITEN LÖSCHEN
        # ============================================
        "pages_delete_even": "Forigi ĉiujn parajn paĝojn",
        "pages_delete_odd":  "Forigi ĉiujn neparajn paĝojn",
        "progress_even_pages": "Forigado de paraj paĝoj",
        "progress_odd_pages": "Forigado de neparaj paĝoj",
        "progress_mark_delete_even": "{} paraj paĝoj markitaj por forigo",
        "progress_mark_delete_odd":  "{} neparaj paĝoj markitaj por forigo",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Eliro el la programo",

    }
