
# ============================================
# translations_sq.py - Fjalor shqip (Albanisch)
# Vollständig sortiert nach Kategorien
# ============================================

def load_albanian_strings():
    """Lädt alle albanischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View nga BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Hap PDF",
        'btn_text_window': "Teksti OCR",
        'btn_first': "Faqja e parë",
        'btn_prev': "Faqja e mëparshme",
        'btn_next': "Faqja tjetër",
        'btn_last': "Faqja e fundit",
        'btn_print': "Printo",
        'btn_darkmode_light': "Modaliteti i ndritshëm",
        'btn_darkmode_dark': "Modaliteti i errët",
        'btn_delete_pages': "Fshi faqet",
        'btn_extract_pages': "Nxirr faqet",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Anulo",
        'btn_save': "Ruaj",
        'btn_close': "Mbylle",
        'btn_delete': "Fshi",
        'btn_delete_all': "Fshi të gjitha",
        'btn_copy': "Kopjo",
        'btn_export': "Eksporto",
        'btn_show': "Shfaq fjalëkalimin",
        'btn_hide': "Fsheh fjalëkalimin",
        'btn_authenticate': "Autentikohu",
        'btn_settings': "Cilësimet",
        'btn_protect': "Mbro",
        'btn_remove_password': "Hiq fjalëkalimin",
        'btn_manage': "Menaxhimi i fjalëkalimeve",
        'btn_retry': "Provo përsëri",
        'btn_select_all': "Zgjidh të gjitha",
        'btn_clear_selection': "Pastro përzgjedhjen",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Faqja {0} nga {1}",
        'page_count': "nga {0}",
        'goto_page': "Shko te faqja",
        'page_simple': "Faqja {0}",
        'full_view_page': "Pamje e plotë e faqes {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Fut termin e kërkimit + Enter",
        'search_results': "Rezultatet: {0} nga {1}",
        'search_nav_hint': "Enter: rezultati tjetër (Shift+Enter: rezultati i mëparshëm)",
        'search_no_results': "Nuk ka rezultate",
        'search_error': "Gabim në kërkim",
        'search_active': "Fusha e kërkimit u aktivizua",
        'search_closed': "Kërkimi përfundoi",
        'search_position': "Faqja {0} {1}",
        'search_pos_top': "krejt lart",
        'search_pos_upper': "lart",
        'search_pos_middle': "në mes",
        'search_pos_lower': "poshtë",
        'search_pos_bottom': "krejt poshtë",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Njohja e tekstit u krye me sukses!",
        'ocr_success_title': "OCR i suksesshëm",
        'ocr_success_message': "Dokumenti tani mund të kërkohet.",
        'ocr_failed': "OCR dështoi",
        'ocr_in_progress': "OCR në vazhdim",
        'ocr_preparing': "Duke përgatitur PDF...",
        'ocr_analyzing': "Duke analizuar PDF...",
        'ocr_optimizing': "Optimizimi i imazhit...",
        'ocr_recognizing': "Njohja e tekstit...",
        'ocr_embedding': "Vendosja e tekstit...",
        'ocr_finalizing': "Përfundimi i PDF...",
        'ocr_not_available': "OCR nuk është i disponueshëm",
        'ocr_install_message': "Mjetet OCR nuk u gjetën.\n\nJu lutemi instaloni:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Kërkohet OCR",
        'ocr_question': "PDF nuk përmban tekst të kërkueshëm.\nDëshironi të kryeni OCR për të mundësuar {0}?",
        'ocr_perform': "Kryej OCR",
        'ocr_later': "Më vonë",
        'ocr_starting': "Duke nisur OCR të garantuar...",
        'ocr_success_voice': "OCR i suksesshëm. PDF tani mund të kërkohet.",
        'ocr_partial_success': "OCR u krye, por pati probleme gjatë zëvendësimit.\n\nVersioni i kërkueshëm u ruajt në:\n{0}\n\nGabim: {1}",
        'ocr_partial_title': "OCR pjesërisht i suksesshëm",
        'ocr_partial_voice': "OCR u krye, por zëvendësimi dështoi.",
        'original_file': "Skedari origjinal:",
        'old_size': "Madhësia e vjetër:    {0} bajt",
        'new_size': "Madhësia e re: {0} bajt",
        'size_change': "Ndryshimi: {0}{1} bajt",
        'backup_created_file': "U krijua kopja rezervë:\n{0}",
        'backup_not_created': "Nuk u krijua kopje rezervë (cilësimi i çaktivizuar)",
        'page_header': "=== Faqja {0} ===\n{1}\n",
        'scanned_page_header': "=== Faqja {0} (e skanuar) ===\n[Kjo faqe përmban vetëm tekst të skanuar]\n[Ju lutemi kryeni OCR manualisht]\n",
        'scanned_warning': "⚠️ TEKST I SKANUAR - KËRKOHET OCR",
        'guaranteed_title': "U krijua PDF i kërkueshëm",
        'guaranteed_message': "<b>U krijua versioni i garantuar i kërkueshëm!</b>\n\nMeqenëse OCR automatik dështoi, u krijua një PDF alternativ i kërkueshëm:\n\n{0}\n\n<b>Ky skedar përmban:</b>\n• Tekst të nxjerrë (nëse ekzistonte)\n• Udhëzime për faqet e skanuara\n• Është plotësisht i kërkueshëm",
        'guaranteed_voice': "U krijua PDF i garantuar i kërkueshëm.",
        'instruction_title': "UDHËZIME PËR OCR",
        'instruction_file': "Skedari origjinal: {0}",
        'instruction_text': "Njohja automatike e tekstit (OCR) dështoi.\nKryeni OCR manualisht:\n\n1. ME OCRmyPDF (rreshti i komandave):\n   ocrmypdf --force-ocr \"[SKEDARI]\" \"output.pdf\"\n\n2. ME ADOBE ACROBAT (macOS/Windows):\n   • Hapni PDF në Acrobat\n   • Mjetet > Redakto PDF\n   • Zgjidhni 'Njohja e tekstit'\n\n3. ME PREVIEW (macOS):\n   • Hapni PDF në Preview\n   • Skedari > Eksporto...\n   • Filtri Quartz: 'Zvogëlo madhësinë e skedarit'\n   • Aktivizoni 'Kryej OCR'\n\n4. SHËRBIMET ONLINE OCR:\n   • smallpdf.com/sq/ocr-pdf\n   • ilovepdf.com/sq/ocr-pdf\n   • adobe.com/sq/acrobat/online/pdf-to-word.html",
        'instruction_created': "U krijuan udhëzimet për OCR",
        'instruction_created_message': "U krijuan udhëzime të detajuara:\n\n{0}\n\nNdiqni hapat për OCR manual.",
        'instruction_created_voice': "U krijuan udhëzimet për OCR.",
        'ocr_impossible': "OCR nuk është i mundur",
        'ocr_impossible_message': "Nuk mund të kryhej OCR.\n\nPërpunoni '{0}' manualisht me softuer OCR.",
        'ocr_impossible_voice': "OCR nuk është i mundur. Ju lutemi përpunoni manualisht.",
        'emergency_title': "OCR urgjent",
        'emergency_message': "U krijua PDF urgjent:\n\n{0}\n\nJu lutemi përpunoni këtë skedar manualisht me OCR.",
        'emergency_voice': "U krijua PDF urgjent. Ju lutemi kryeni OCR manualisht.",
        'critical_error': "Gabim kritik",
        'critical_error_message': "OCR nuk mund të nisej.\n\nRinisni programin dhe kontrolloni instalimin e OCR.",
        'critical_error_voice': "Gabim kritik OCR",
        'ocr_question_html': "<p>PDF nuk përmban tekst të kërkueshëm.<p>Dëshironi të kryeni OCR për të mundësuar <b>{0}</b>?</p>",
        'ocr_question_voice': "Kërkohet OCR. PDF nuk përmban tekst të kërkueshëm. Dëshironi të kryeni OCR për të mundësuar {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "asnjë PDF i ngarkuar",
        'no_pdf_message': "Nuk është ngarkuar asnjë PDF",
        'pdf_not_found': "Skedari PDF nuk u gjet",
        'file_size': "Madhësia e skedarit",
        'bytes': "bajt",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "U krijua kopja rezervë",
        'backup_disabled': "Kopjimi rezervë është çaktivizuar",
        'backup_activated': "Krijimi i kopjeve rezervë u aktivizua",
        'backup_deactivated': "Krijimi i kopjeve rezervë u çaktivizua",
        'backup_status': "Kopja rezervë: {0}",
        'backup_on': "✔ aktiv",
        'backup_off': "✘ joaktiv",
        'close_pdf': "Duke mbyllur PDF: {0}",
        'pdf_not_found_format': "Skedari PDF nuk u gjet: {0}",
        'error_pdf_load_format': "Gabim gjatë ngarkimit të PDF: {0}",
        'load_failed_format': "Ngarkimi dështoi:\n{0}",
        'decrypted_suffix': "(i deshifruar)",
        'decryption_failed': "Deshifrimi dështoi.",
        'decryption_error': "Gabim gjatë deshifrimit",
        'decryption_success': "Deshifrimi u krye me sukses",
        'decryption_success_message': "PDF u deshifrua dhe u ruajt në:\n\n{0}",
        'decryption_success_voice': "PDF u deshifrua dhe u ruajt.",
        'password_remove_error': "Gabim gjatë heqjes së fjalëkalimit",
        'save_unencrypted': "Ruaj PDF të pashifruar si",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Ruaj si...",
        'save_copy': "Ruaj kopje",
        'save_success': "PDF u ruajt në: {0}",
        'save_encrypted': "PDF i mbrojtur u ruajt në: {0}",
        'save_error': "PDF nuk mund të ruhej",
        'encryption_question': "Dëshironi të mbroni PDF me fjalëkalim?",
        'encryption_yes': "Po",
        'encryption_no': "Jo",
        'encryption_cancel': "Anulo",
        'save_cancel': "Ruajtja u anulua",
        'save_encrypted_voice': "Skedari u shifrua dhe u ruajt.",
        'save_success_voice': "Skedari PDF u ruajt i pashifruar.",
        'save_error_format': "PDF nuk mund të ruhej:\n{0}",
        'export_pages_success': "Eksportimi në Pages u krye me sukses",
        'export_pages_error': "Eksportimi në Pages dështoi",
        'export_pages_error_format': "Eksportimi në Pages dështoi: {0}",
        'export_word_success': "Eksportimi në Word u krye me sukses",
        'export_word_error': "Eksportimi në Word dështoi",
        'export_word_error_format': "Eksportimi në Word dështoi: {0}",
        'export_text_success': "Eksportimi i tekstit u krye me sukses",
        'export_text_error': "Eksportimi i tekstit dështoi",
        'export_text_error_format': "Eksportimi i tekstit dështoi: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Kërkohet fjalëkalimi",
        'password_enter': "Ju lutemi shkruani fjalëkalimin",
        'password_confirm': "Konfirmo fjalëkalimin",
        'password_new': "Fjalëkalim i ri",
        'password_current': "Fjalëkalimi aktual",
        'password_save': "Ruaj fjalëkalimin (të shifruar)",
        'password_saved': "✓ Fjalëkalimi për këtë skedar u ruajt",
        'password_wrong': "Fjalëkalim i gabuar",
        'password_mismatch': "Fjalëkalimet nuk përputhen",
        'password_too_short': "Fjalëkalimi është shumë i shkurtër",
        'password_min_length': "Fjalëkalimi duhet të ketë të paktën 4 karaktere",
        'password_strength': "Forca e fjalëkalimit",
        'password_strength_very_weak': "Shumë e dobët",
        'password_strength_weak': "E dobët",
        'password_strength_medium': "Mesatare",
        'password_strength_strong': "E fortë",
        'password_strength_very_strong': "Shumë e fortë",
        'password_char_count': "({0} karaktere)",
        'password_match': "✓ Përputhen",
        'password_no_match': "✗ Fjalëkalimet nuk përputhen",
        'password_show': "Shfaq",
        'password_hide': "Fsheh",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Menaxhimi i fjalëkalimeve",
        'password_table_filename': "Emri i skedarit",
        'password_table_password': "Fjalëkalimi",
        'password_count': "{0} fjalëkalime të ruajtura",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Nuk ka fjalëkalime të ruajtura",
        'password_copied': "U kopjuan {0} fjalëkalime",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Jeni i sigurt se doni të fshini fjalëkalimin për '{0}'?",
        'password_delete_multiple': "Jeni i sigurt se doni të fshini {0} fjalëkalime të zgjedhura?",
        'password_delete_all_confirm': "Jeni i sigurt se doni të fshini të gjitha {0} fjalëkalimet e ruajtura?",
        'password_deleted': "U fshinë {0} fjalëkalime",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Të gjitha fjalëkalimet u fshinë",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Gjeneruesi i fjalëkalimeve",
        'generator_generated': "Fjalëkalimi i gjeneruar:",
        'generator_regenerate': "Gjenero përsëri",
        'generator_copy': "Kopjo",
        'generator_use': "Përdor",
        'generator_settings': "Cilësimet",
        'generator_length': "Gjatësia:",
        'generator_group_every': "Ndarës çdo",
        'generator_group_chars': "karaktere.    Ndarësi:",
        'generator_uppercase': "Shkronja të mëdha (A-Z)",
        'generator_lowercase': "Shkronja të vogla (a-z)",
        'generator_digits': "Numra (0-9)",
        'generator_symbols': "Simbole (!@#$%^&*)",
        'generator_exclude': "Të përjashtuara:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Kërkohet fjalëkalimi master",
        'master_password_setup': "Cakto fjalëkalimin master",
        'master_password_change': "Ndrysho fjalëkalimin master",
        'master_password_enter': "Ju lutemi shkruani fjalëkalimin tuaj master",
        'master_password_choose': "Zgjidhni një fjalëkalim master të fortë (të paktën 8 karaktere)",
        'master_password_new': "Ju lutemi shkruani fjalëkalimin tuaj të ri master",
        'master_password_confirm': "Konfirmo fjalëkalimin",
        'master_password_authenticate': "Autentikohu",
        'master_password_success': "Fjalëkalimi master u caktua me sukses.",
        'master_password_changed': "Fjalëkalimi master u ndryshua me sukses.",
        'master_password_removed': "Fjalëkalimi master dhe të gjitha fjalëkalimet u fshinë.",
        'master_password_remove': "Hiq fjalëkalimin master",
        'master_password_remove_confirm': "Jeni i SIGURT se doni të fshini TË GJITHA fjalëkalimet?\n\nKy veprim është I PAKTHYESHËM!",
        'master_password_export_before': "Dëshironi të eksportoni një kopje rezervë më parë?",
        'master_password_export_delete': "Eksporto dhe fshi",
        'master_password_delete_now': "Fshi tani",
        'master_password_for_signatures': "Për të përdorur nënshkrimet, duhet të caktoni një fjalëkalim master.\n\nDëshironi të caktoni një fjalëkalim master tani?",
        'master_password_for_private': "Për të përdorur blloqet private të tekstit, duhet të caktoni një fjalëkalim master.\n\nDëshironi të caktoni një fjalëkalim master tani?",
        'master_password_info': """
            <b>🔐 PA FJALËKALIM MASTER:</b><br>
            • Nuk është e mundur të shfaqen, kopjohen dhe eksportohen fjalëkalimet<br>
            • Fshirja e fjalëkalimeve është gjithmonë e mundur (edhe pa fjalëkalim master)<br><br>

            <b>🔐 ME FJALËKALIM MASTER:</b><br>
            • Të gjitha funksionet janë të disponueshme pas autentikimit<br>
            • Fjalëkalimet shifrohen me fjalëkalimin master<br>
            • Gjatësia minimale: 8 karaktere<br>
            • Ruajtje e sigurt e hash-it SHA-256<br><br>

            <b>E RËNDËSISHME:</b><br>
            • Nëse humbni fjalëkalimin master, fjalëkalimet nuk mund të rikthehen<br>
            • Kur hiqni fjalëkalimin master, TË GJITHA fjalëkalimet fshihen<br>
            • Opsioni i eksportit është i disponueshëm para fshirjes<br>
            • Fjalëkalimi master mund të ndryshohet në çdo kohë
        """,
        'signature_auth_disabled': "Çaktivizo kërkesën për fjalëkalim për nënshkrimet",
        'template_auth_disabled': "Çaktivizo kërkesën për fjalëkalim për blloqet private të tekstit",
        'master_password_for_signatures_settings': "Për të përdorur nënshkrimet, duhet të caktoni një fjalëkalim master.\n\nShkoni te Cilësimet - Menaxhimi i fjalëkalimeve",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Mbro PDF",
        'protect_info': "Skedari '{0}' do të mbrohet me fjalëkalim.",
        'protect_instruction': "Ju lutemi shkruani fjalëkalimin e dëshiruar dy herë për të mbrojtur dokumentin, ose përdorni gjeneruesin e fjalëkalimeve në të djathtë të fushës së hyrjes.",
        'protect_success': "PDF u mbrojt me sukses dhe u ruajt në:\n{0}\n\nFjalëkalimi: {1}\n\nDëshironi të hapni PDF-në e mbrojtur tani?",
        'protect_open': "Po",
        'protect_skip': "Jo",
        'protect_error': "Gabim gjatë mbrojtjes së PDF",
        'protect_open_title': "hap PDF-në e mbrojtur",
        'protect_question': "U krye. Dëshironi të hapni PDF-në e mbrojtur tani? Po ose Jo?",
        'password_cancel': "Dialogu i fjalëkalimit u anulua",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Fshi faqet",
        'pages_extract': "Nxirr faqet",
        'pages_insert': "Fut faqet",
        'pages_move': "Zhvendos faqet",
        'pages_delete_options': "Opsionet e fshirjes",
        'pages_delete_empty': "Fshi të gjitha faqet e zbrazëta",
        'pages_delete_current': "Fshi faqen aktuale",
        'pages_delete_range': "Fshi intervalin e faqeve",
        'pages_extract_options': "Opsionet e nxjerrjes",
        'pages_extract_current': "Nxirr faqen aktuale",
        'pages_extract_range': "Nxirr intervalin e faqeve",
        'pages_insert_position': "Pozicioni i futjes",
        'pages_insert_before': "Fut para faqes:",
        'pages_insert_select': "Zgjidh PDF",
        'pages_insert_none': "Asnjë PDF i zgjedhur",
        'pages_move_source': "Faqet për t'u zhvendosur",
        'pages_move_from': "Nga faqja:",
        'pages_move_to': "Deri te faqja:",
        'pages_move_target': "Pozicioni i synuar",
        'pages_move_before': "Zhvendos para faqes:",
        'pages_move_hint': "Shënim: faqja 1 = fillimi, {0} = fundi",
        'pages_range_invalid': "Faqja fillestare duhet të jetë më e vogël ose e barabartë me faqen përfundimtare.",
        'pages_position_invalid': "Pozicioni i synuar nuk mund të jetë brenda intervalit që zhvendoset.",
        'pages_no_pdf_selected': "Asnjë PDF nuk është zgjedhur.",
        'pages_deleted': "U fshinë {0} faqe.",
        'pages_extracted': "U nxorën: {0}\nU ruajtën në: {1}\nMadhësia e skedarit: {2:.1f} KB",
        'pages_inserted': "U futën {0} faqe",
        'pages_moved': "U zhvendosën {0} faqe.",
        'pages_deleted_none': "Asnjë faqe nuk u fshi.",
        'pages_delete_progress': "Duke fshirë faqet...",
        'pages_deleted_with_backup': "U fshinë {0} faqe.\n\nKopja rezervë: {1}",
        'pages_deleted_voice': "U krijua një kopje rezervë dhe u fshinë {0} faqe.",
        'info': "Informacion",
        'error_dialog_creation': "Dialogu nuk mund të krijohej",
        'extract_page_single': "Nxirr faqen {0}",
        'extract_page_range': "Nxirr faqet {0}-{1}",
        'extract_success_voice': "Faqet u nxorën me sukses",
        'extract_error_format': "Gabim gjatë nxjerrjes: {0}",
        'pages_inserted_voice': "U futën {0} faqe.",
        'insert_error_format': "Gabim gjatë futjes: {0}",
        'pages_move_progress': "Duke zhvendosur faqet...",
        'pages_moved_with_backup': "U zhvendosën {0} faqe.\n\nKopja rezervë: {1}",
        'move_success_title': "U zhvendos me sukses",
        'pages_moved_voice': "{0} faqe u zhvendosën me sukses",
        'mark_removed': "Shenja e faqes {0} u hoq",
        'mark_empty': "Faqja {0} u shënua si e zbrazët",
        'mark_export_removed': "Shenja e eksportit të faqes {0} u hoq",
        'mark_export': "Faqja {0} u shënua për eksport",
        'no_empty_pages': "Nuk ka faqe të zbrazëta të shënuara për fshirje",
        'delete_empty_confirm': "Dëshironi të fshini të gjitha {0} faqet e zbrazëta të shënuara?",
        'delete_empty_confirm_voice': "Të fshihen tani të gjitha {0} faqet e zbrazëta të shënuara? Po ose Jo.",
        'empty_pages_deleted': "U fshinë {0} faqe të zbrazëta",
        'no_export_pages': "Nuk ka faqe të shënuara për eksport",
        'overwrite_title': "Mbishkruaj skedarin ekzistues",
        'overwrite_question': "Skedari\n\n{0}\n\nekziston tashmë.\nDëshironi ta mbishkruani?",
        'overwrite_voice': "Mbishkruaj skedarin ekzistues? Po ose Jo.",
        'page_skipped': "Faqja {0} u anashkalua",
        'export_complete': "Eksporti u përfundua.",
        'export_complete_voice': "Eksporti u përfundua.",
        'no_pages_exported': "Asnjë faqe nuk u eksportua",
        'export_cancelled': "Eksporti u anulua",
        'pages_exported': "{0} faqe u eksportuan në {1}",
        'export_page_title': "Eksporto faqen",
        'page_exported': "Faqja {0} u eksportua në {1}",
        'export_error': "Gabim gjatë eksportit",
        'export_marked_title': "Eksporto faqet e shënuara",
        'rotate_all_title': "rrotullo të gjitha faqet",
        'rotate_all_question': "Dëshironi të rrotulloni të gjitha faqet 90 gradë djathtas?",
        'rotate_all_voice': "Dëshironi të rrotulloni të gjitha faqet 90 gradë djathtas? Po ose Jo?",
        'all_pages_rotated': "Të gjitha faqet u rrotulluan",
        'page_rotated': "Faqja {0} u rrotullua",
        'rotate_error': "Faqja nuk mund të rrotullohej",
        'delete_page_confirm': "Dëshironi të fshini faqen {0}?",
        'delete_page_confirm_voice': "Jeni i sigurt se doni të fshini faqen {0}? Po ose Jo.",
        'page_deleted': "Faqja {0} u fshi",
        'delete_error': "Faqja nuk mund të fshihej",
        'pages_deleted_voice': "{0} faqe u fshinë",
        'pages_exported_split': "{0} faqe u eksportuan me sukses.",
        'pages_skipped': "{0} faqe u anashkaluan.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Nxirr faqet (të avancuara)",
        'pdf_splitter_title': "Ndarës dhe nxjerrës PDF",
        'pdf_splitter_load': " Zgjidh skedarin PDF",
        'pdf_splitter_info': "Ju lutemi zgjidhni një opsion për dokumentin tuaj PDF",
        'pdf_splitter_basic': "Operacionet themelore",
        'pdf_splitter_single': "Ndaj në faqe individuale",
        'pdf_splitter_range': "Nxirr faqet:",
        'pdf_splitter_range_placeholder': "p.sh. 1-3,5,7-9",
        'pdf_splitter_clean': "Operacionet e pastrimit",
        'pdf_splitter_remove_empty': "Hiq të gjitha faqet e zbrazëta",
        'pdf_splitter_remove': "Fshi intervalin e faqeve:",
        'pdf_splitter_remove_placeholder': "p.sh. 2,4-6",
        'pdf_splitter_process': "Përpunoni PDF",
        'pdf_splitter_loaded': "PDF u ngarkua. Ju lutemi zgjidhni një opsion",
        'pdf_read_error': "PDF nuk mund të lexohej",
        'pages': "Faqet",
        'pages_created': "Faqet u krijuan",
        'range_empty': "Ju lutemi shkruani një interval faqesh",
        'range_invalid': "Interval faqesh i pavlefshëm",
        'range_created': "U krijua një PDF i ri me faqet e zgjedhura:\n{0}",
        'empty_removed': "U hoqën {0} faqe të zbrazëta.\nDalja: {1}",
        'remove_empty': "Ju lutemi shkruani faqet për t'u hequr",
        'remove_invalid': "Faqe të pavlefshme për heqje",
        'remove_done': "U krijua PDF i pastruar:\n{0}",
        'open_folder': "Hap dosjen",
        'show_in_finder': "Shfaq në Finder",
        'pdf_splitter_no_pdf': "Ju lutemi ngarkoni së pari një skedar PDF.",
        'process_error': "Gabim gjatë përpunimit të PDF",
        'pages_created_voice': "U krijuan {0} faqe",
        'range_created_voice': "U krijua PDF me faqet e zgjedhura",
        'empty_removed_voice': "U hoqën {0} faqe të zbrazëta",
        'remove_done_voice': "U krijua PDF i pastruar",
        'pdf_splitter_split_groups': "Çdo grup i pandërprerë në skedar të veçantë",
        'range_created_single': "U krijua PDF i ri:\n{0}",
        'range_created_multiple': "U krijuan {0} skedarë PDF.",
        'range_created_voice_single': "U krijua një PDF me faqet e zgjedhura",
        'range_created_voice_multiple': "U krijuan {0} skedarë PDF",
        'empty_removed_none_left': "Nuk ka faqe të mbetura",
        'empty_removed_all_empty': "Të gjitha faqet u njohën si të zbrazëta dhe do të hiqeshin. Asnjë skedar nuk u krijua.",
        'preview_single': "Paraparje: {0}",
        'preview_enter_range': "Ju lutemi shkruani një interval faqesh.",
        'preview_invalid_range': "Interval faqesh i pavlefshëm.",
        'preview_file': "Paraparje: {0}",
        'preview_files': "Paraparje: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Duke filluar printimin",
        'print_sent': "Detyra e printimit u dërgua",
        'print_now': "Printo tani",
        'print_error': "Gabim gjatë printimit të menjëhershëm",
        'print_limited': "Funksioni i printimit është i kufizuar në këtë sistem",
        'print_error_format': "Gabim gjatë printimit të menjëhershëm: {0}",
        'warning': "Paralajmërim",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Kalo në modalitetin e ndritshëm",
        'mode_switch_to_dark': "Kalo në modalitetin e errët",
        'mode_dark_activated': "Modaliteti i errët u aktivizua",
        'mode_light_activated': "Modaliteti i ndritshëm u aktivizua",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Pamje e plotë",
        'zoom_two_pages': "Dy faqe krah njëra-tjetrës",
        'zoom_overview': "Modaliteti i përmbledhjes",
        'zoom_cannot_during_search': "Zmadhimi nuk është i mundur gjatë kërkimit",
        'zoom_exit_first': "Ju lutemi dilni së pari nga zmadhimi",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Zvarrit dhe lësho u aktivizua",
        'drag_disabled': "Zvarrit dhe lësho u çaktivizua",
        'drag_page_grab': "Faqja {0} u kap",
        'drag_page_dropped': "Faqja {0} u fut në pozicionin {1}",
        'drag_position_invalid': "Pozicion i pavlefshëm",
        'drag_same_position': "Faqja {0} mbetet në pozicionin {0}",
        'drag_error': "Gabim gjatë zhvendosjes",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        # (vjen nga pjesa e mëparshme, vazhdojmë me 19.2)

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Futja e tekstit dhe blloqet e tekstit – Udhëzues i detajuar**

        **1. Futja dhe redaktimi i tekstit**
        - Klikoni me të djathtën në vendin e dëshiruar në dokument dhe zgjidhni "Fut tekst".
        - Do të hapet një dialog ku mund të shkruani dhe formatoni tekstin:
        • Madhësia e shkronjave, të trasha, të pjerrëta, të nënvizuara
        • Ngjyra e tekstit (zgjedhje e lirë)
        • Transparenca (patejdukshmëria) me rrëshqitës
        • Thyerja e rreshtave (gjerësi të ndryshme, p.sh. gjerësia e faqes, e ngushtë, pa thyerje)
        - Pas konfirmimit, teksti do të shfaqet në vendin e klikimit. Mund ta lëvizni me miun ose me shigjeta.
        - Klikoni dy herë mbi tekst për të hapur modalitetin e redaktimit; ESC e mbyll atë.

        **2. Menaxhimi i blloqeve të tekstit (shablloneve)**
        - Në anën e majtë të dialogut të tekstit shihni një listë të të gjitha blloqeve të ruajtura të tekstit.
        - **Ruajtja e një blloku:** Shkruani tekstin, formatojeni dhe klikoni "💾 Ruaj si bllok". Shkruani një emër skedari (pa shtesë).
        - **Ngarkimi i një blloku:** Klikoni mbi emrin e dëshiruar në listë. Teksti dhe formatimi do të merren dhe mund të përshtaten nëse është e nevojshme.
        - **Fshirja:** Klikoni me të djathtën mbi një bllok për ta fshirë ose për të ndryshuar statusin e privatësisë.

        **3. Blloqet private të tekstit (fjalëkalimi master)**
        - Nëse keni caktuar një fjalëkalim master (në Cilësimet → Menaxhimi i fjalëkalimeve), mund t'i shënoni blloqet si "private".
        - Shënoni kutinë "Bllok privat i tekstit" në dialog para ruajtjes.
        - Blloqet private shfaqen në listë vetëm nëse keni futur fjalëkalimin tuaj master një herë për seancë (autentikimi përmes ikonës së dryrit ose në hyrjen e parë).
        - Në këtë mënyrë mund të mbroni blloqet konfidenciale të tekstit nga qasja e paautorizuar.

        **4. Futja e kryqeve**
        - Nga menyja e kontekstit mund të futni gjithashtu një kryq grafik (p.sh. për kutitë e kontrollit).
        - Madhësia, trashësia e vijës dhe ngjyra e kryqeve mund të rregullohen globalisht në cilësimet (menyja "Cilësimet" → "Cilësimet e kryqeve").
        - Klikoni me të djathtën mbi një kryq ekzistues për ta ndryshuar individualisht.

        **5. Veprimet në grup**
        - Nëse keni vendosur disa tekste ose kryqe në një faqe, mund t'i ruani ose t'i hidhni të gjitha menjëherë nga menyja e kontekstit (klikimi i djathtë në modalitetin e tekstit).
        - Gjatë ruajtjes, të gjithë elementët futen në PDF dhe mbeten si grafikë vektoriale.

        **6. Shkurtoret e tastierës në modalitetin e tekstit**
        - Shigjetat: lëvizja e elementit
        - Ctrl+shigjeta: hapa më të mëdhenj
        - Enter: hap dialogun e ruajtjes (ruaj të gjitha / përshtat / hidh)
        - ESC: hedh elementin aktual
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Futja e tekstit dhe blloqet e tekstit – Udhëzues i detajuar</strong></p>

        <p><strong>1. Futja dhe redaktimi i tekstit</strong></p>
        <ul>
        <li>Klikoni me të djathtën në vendin e dëshiruar në dokument dhe zgjidhni "Fut tekst".</li>
        <li>Do të hapet një dialog ku mund të shkruani dhe formatoni tekstin:<br/>
        • Madhësia e shkronjave, të trasha, të pjerrëta, të nënvizuara<br/>
        • Ngjyra e tekstit (zgjedhje e lirë)<br/>
        • Transparenca (patejdukshmëria) me rrëshqitës<br/>
        • Thyerja e rreshtave (gjerësi të ndryshme, p.sh. gjerësia e faqes, e ngushtë, pa thyerje)</li>
        <li>Pas konfirmimit, teksti do të shfaqet në vendin e klikimit. Mund ta lëvizni me miun ose me shigjeta.</li>
        <li>Klikoni dy herë mbi tekst për të hapur modalitetin e redaktimit; ESC e mbyll atë.</li>
        </ul>

        <p><strong>2. Menaxhimi i blloqeve të tekstit (shablloneve)</strong></p>
        <ul>
        <li>Në anën e majtë të dialogut të tekstit shihni një listë të të gjitha blloqeve të ruajtura të tekstit.</li>
        <li><strong>Ruajtja e një blloku:</strong> Shkruani tekstin, formatojeni dhe klikoni "💾 Ruaj si bllok". Shkruani një emër skedari (pa shtesë).</li>
        <li><strong>Ngarkimi i një blloku:</strong> Klikoni mbi emrin e dëshiruar në listë. Teksti dhe formatimi do të merren dhe mund të përshtaten nëse është e nevojshme.</li>
        <li><strong>Fshirja:</strong> Klikoni me të djathtën mbi një bllok për ta fshirë ose për të ndryshuar statusin e privatësisë.</li>
        </ul>

        <p><strong>3. Blloqet private të tekstit (fjalëkalimi master)</strong></p>
        <ul>
        <li>Nëse keni caktuar një fjalëkalim master (në Cilësimet → Menaxhimi i fjalëkalimeve), mund t'i shënoni blloqet si "private".</li>
        <li>Shënoni kutinë "Bllok privat i tekstit" në dialog para ruajtjes.</li>
        <li>Blloqet private shfaqen në listë vetëm nëse keni futur fjalëkalimin tuaj master një herë për seancë (autentikimi përmes ikonës së dryrit ose në hyrjen e parë).</li>
        <li>Në këtë mënyrë mund të mbroni blloqet konfidenciale të tekstit nga qasja e paautorizuar.</li>
        </ul>

        <p><strong>4. Futja e kryqeve</strong></p>
        <ul>
        <li>Nga menyja e kontekstit mund të futni gjithashtu një kryq grafik (p.sh. për kutitë e kontrollit).</li>
        <li>Madhësia, trashësia e vijës dhe ngjyra e kryqeve mund të rregullohen globalisht në cilësimet (menyja "Cilësimet" → "Cilësimet e kryqeve").</li>
        <li>Klikoni me të djathtën mbi një kryq ekzistues për ta ndryshuar individualisht.</li>
        </ul>

        <p><strong>5. Veprimet në grup</strong></p>
        <ul>
        <li>Nëse keni vendosur disa tekste ose kryqe në një faqe, mund t'i ruani ose t'i hidhni të gjitha menjëherë nga menyja e kontekstit (klikimi i djathtë në modalitetin e tekstit).</li>
        <li>Gjatë ruajtjes, të gjithë elementët futen në PDF dhe mbeten si grafikë vektoriale.</li>
        </ul>

        <p><strong>6. Shkurtoret e tastierës në modalitetin e tekstit</strong></p>
        <ul>
        <li>Shigjetat: lëvizja e elementit</li>
        <li>Ctrl+shigjeta: hapa më të mëdhenj</li>
        <li>Enter: hap dialogun e ruajtjes (ruaj të gjitha / përshtat / hidh)</li>
        <li>ESC: hedh elementin aktual</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Cilësimet e kryqeve",
        'cross_properties': "Vetitë e kryqit",
        'cross_size': "Madhësia (px):",
        'cross_line_width': "Trashësia e vijës:",
        'cross_color': "Ngjyra:",
        'cross_choose_color': "Zgjidh",
        'cross_fine_tuning': "Akordimi i imët gjatë ruajtjes (pikselë)",
        'cross_offset_x': "Zhvendosja X:",
        'cross_offset_y': "Zhvendosja Y:",
        'cross_offset_x_tooltip': "Vlerat negative e zhvendosin kryqin majtas gjatë ruajtjes, pozitive djathtas",
        'cross_offset_y_tooltip': "Vlerat negative e zhvendosin kryqin lart gjatë ruajtjes, pozitive poshtë",
        'cross_preview': "Paraparje",
        'cross_save': "Apliko cilësimet",
        'cross_customized': "Kryqi u përshtat",
        'cross_settings_applied': "Cilësimet e kryqeve u ruajtën.\nMadhësia: {0}px, trashësia e vijës: {1}px\n{2}",
        'cross_updated_count': "U përditësuan {0} kryqe ekzistues.",
        'cross_no_crosses': "Nuk u gjetën kryqe ekzistues.",
        'cross_settings_applied_all': "Cilësimet e kryqeve u aplikuan për të gjithë {0} kryqet",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Cilësimet e nënshkrimeve",
        'signature_1': "Nënshkrimi 1",
        'signature_2': "Nënshkrimi 2",
        'signature_select': "Zgjidh nënshkrimin",
        'signature_add': "➕ Shto nënshkrim të ri...",
        'signature_size': "Madhësia për nënshkrimin {0} (%):",
        'signature_common': "Cilësimet e përgjithshme",
        'signature_timestamp': "Shto vulën kohore automatikisht",
        'signature_location': "Vendndodhja e paracaktuar:",
        'signature_timestamp_size': "Madhësia e shkronjave të vulës kohore:",
        'signature_no_files': "-- Nuk u gjetën nënshkrime --",
        'signature_insert': "Fut nënshkrimin",
        'signature_insert_1': "Fut nënshkrimin 1",
        'signature_insert_2': "Fut nënshkrimin 2",
        'signature_customize': " Përshtat nënshkrimin",
        'signature_discard': " Hidh këtë nënshkrim",
        'signature_save_all': " Ruaj të gjitha nënshkrimet",
        'signature_discard_all': " Hidh të gjitha nënshkrimet",
        'signature_guide_title': "Nënshkrimet – Udhëzues",
        'signature_guide': """
📝 Nënshkrimet – Udhëzues i shkurtër

- Caktoni një fjalëkalim master
- Konfiguroni nënshkrimet në menynë Cilësimet
  (madhësia, vula kohore ...)
- Futni me KLIKIM TË DJATHTË në vendin e dëshiruar
  (fjalëkalimi master kërkohet një herë për seancë)
- Lëvizni nënshkrimin me miun ose me shigjeta
- Mund të futen disa nënshkrime njëri pas tjetrit
- Çdo nënshkrim mund të përshtatet individualisht
- Hidhni një nënshkrim të vetëm
- Ruani / hidhni të gjitha nënshkrimet menjëherë
- Alternativisht, mund të përdorni edhe shiritin e menysë.
        """,
        'signature_placeholder': "Paraparje në dispozicion",
        'signature_info': "Nënshkrimi {0}: {1}×{2} px ({3}% e {4}×{5})",
        'signature_info_placeholder': "Cilësimet për nënshkrimin {0}",
        'signature_inserted': "Nënshkrimi {0} u fut në faqen {1}",
        'signature_deleted': "Nënshkrimi u fshi",
        'signature_copied': "Nënshkrimi u kopjua",
        'signature_pasted': "Nënshkrimi {0} u ngjit",
        'signature_saved': "{0} nënshkrime u futën në PDF.\n\nPDF u ringarkua...",
        'signature_saved_voice': "{0} nënshkrime u ruajtën",
        'mode_replace_signature_format': "Dil nga modaliteti dhe fut nënshkrimin {0}",
        'mode_conflict_voice_signature': "Modaliteti {0} është aktiv. Të dalësh dhe të fusësh nënshkrimin?",
        'signature_not_configured': "Nënshkrimi {0} nuk është konfiguruar",
        'signature_file_not_found': "Skedari i nënshkrimit nuk u gjet",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nuk ka nënshkrim të kopjuar",
        'no_signatures_to_save': "Nuk ka nënshkrime për t'u ruajtur",
        'signature_save_question': "Të ruhen të gjitha nënshkrimet, të përshtaten apo të hidhet ky?",
        'signatures_saved_title': "Nënshkrimet u ruajtën",
        'signatures_saved': "{0} nënshkrime u futën në PDF.\n\nPDF u ringarkua...",
        'signatures_saved_voice': "{0} nënshkrime u ruajtën.",
        'all_signatures_discarded': "Të gjitha nënshkrimet u hodhën",
        'signature_settings_saved': "Cilësimet e nënshkrimeve u ruajtën",
        'signature_cancelled': "Nënshkrimi u hodh",
        'signature_active_title': "Nënshkrimi aktiv",
        'signature_replace_question': "Tashmë ka një nënshkrim aktiv.\n\nDëshironi të zëvendësoni nënshkrimin aktual?",
        'signature_replace': "Zëvendëso nënshkrimin",
        'signature_replace_voice': "Të zëvendësohet nënshkrimi aktual apo të anulohet?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Cilësimet e imazheve",
        'image_common': "Cilësimet e përgjithshme të imazheve",
        'image_keep_aspect': "Mbaj raportin e aspektit gjatë zvarritjes",
        'image_default_size': "Madhësia e paracaktuar (%):",
        'image_dark_invert': "Përmbys imazhet në modalitetin e errët",
        'image_dark_invert_tooltip': "Aktiv: imazhet përmbysen për shikueshmëri më të mirë",
        'image_fine_tuning': "Akordimi i imët (pikselë)",
        'image_offset_x': "Zhvendosja X:",
        'image_offset_y': "Zhvendosja Y:",
        'image_offset_x_tooltip': "Vlerat negative e zhvendosin imazhin majtas gjatë ruajtjes, pozitive djathtas",
        'image_offset_y_tooltip': "Vlerat negative e zhvendosin imazhin lart gjatë ruajtjes, pozitive poshtë",
        'image_select': "Zgjidh imazhin",
        'image_insert': "Fut imazhin",
        'image_customize': " Përshtat imazhin",
        'image_aspect': " Mbaj raportin e aspektit",
        'image_discard': " Hidh këtë imazh",
        'image_save_all': " Ruaj të gjitha imazhet",
        'image_discard_all': " Hidh të gjitha imazhet",
        'image_filter': "Imazhet",
        'image_guide_title': "Futja e imazheve – Udhëzues",
        'image_guide': """
📷 Futja e imazheve në PDF – Udhëzues i shkurtër:

1. Klikoni me të djathtën në vendin e dëshiruar
2. "Fut imazh" → zgjidhni imazhin
3. Poziciononi imazhin: zvarriteni me miun
4. Rregulloni madhësinë: zvarriteni nga qoshet/skajet
5. Mbani raportin e aspektit: tast [A]
6. Përshtatje të mëtejshme: klikoni me të djathtën mbi imazh

Këshillë: Në menynë e kontekstit mund të rregulloni cilësimet.
        """,
        'image_inserted': "Imazhi u fut në faqen {1}",
        'image_deleted': "Imazhi u hodh",
        'image_copied': "Imazhi u kopjua",
        'image_pasted': "Imazhi u ngjit",
        'image_saved': "{0} imazhe u futën në PDF.\n\nPDF u ringarkua...",
        'image_saved_voice': "{0} imazhe u ruajtën",
        'image_aspect_on': "aktiv",
        'image_aspect_off': "joaktiv",
        'image_aspect_toggle': "Mbaj raportin e aspektit {0}",
        'image_reset': "Imazhi u kthye në madhësinë origjinale",
        'image_replaced': "Imazhi u zëvendësua",
        'image_invalid': "Imazh i pavlefshëm",
        'mode_replace_image': "Fut imazh",
        'mode_conflict_voice_image': "Modaliteti {0} është aktiv. Të dalësh dhe të fusësh imazhin?",
        'image_active_title': "Imazhi aktiv",
        'image_replace_question': "Tashmë ka një imazh aktiv.\n\nDëshironi të zëvendësoni imazhin aktual?",
        'image_replace': "Zëvendëso imazhin",
        'image_replace_voice': "Të zëvendësohet imazhi aktual apo të anulohet?",
        'image_filter_all': "Imazhet (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Të gjithë skedarët (*.*)",
        'no_copied_image': "Nuk ka imazh të kopjuar",
        'image_discarded': "Imazhi u hodh",
        'image_save_question': "Të ruhen të gjitha imazhet, të përshtaten apo të hidhet ky?",
        'no_images_to_save': "Nuk ka imazhe për t'u ruajtur",
        'no_valid_images': "Nuk ka imazhe të vlefshme për t'u ruajtur",
        'images_saved_title': "Imazhet u ruajtën",
        'images_saved': "{0} imazhe u futën në PDF.\n\nPDF u ringarkua...",
        'images_saved_voice': "{0} imazhe u ruajtën.",
        'all_images_discarded': "Të gjitha imazhet u hodhën",
        'image_settings_updated': "Cilësimet e imazheve u përditësuan",
        'image_replace_title': "Zgjidh imazh të ri",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Cilësimet e formave",
        'form_basic': "Cilësimet bazë",
        'form_default_type': "Lloji i paracaktuar i formës:",
        'form_rectangle': "Drejtkëndësh",
        'form_ellipse': "Elipsë",
        'form_line': "Vijë",
        'form_arrow': "Shigjetë",
        'form_line_width': "Trashësia e vijës:",
        'form_colors': "Ngjyrat",
        'form_line_color': "Ngjyra e vijës:",
        'form_fill_color': "Ngjyra e mbushjes:",
        'form_choose_color': "Zgjidh",
        'form_transparent': "Sfond transparent (vetëm vijë)",
        'form_filled': "e mbushur",
        'form_dark_mode': "Modaliteti i errët",
        'form_dark_invert': "Përmbys ngjyrat në modalitetin e errët",
        'form_fine_tuning': "Akordimi i imët (pikselë)",
        'form_offset_x': "Zhvendosja X:",
        'form_offset_y': "Zhvendosja Y:",
        'form_offset_x_tooltip': "Vlerat negative e zhvendosin formën majtas gjatë ruajtjes, pozitive djathtas",
        'form_offset_y_tooltip': "Vlerat negative e zhvendosin formën lart gjatë ruajtjes, pozitive poshtë",
        'form_preview': "Paraparje",
        'form_insert': "Fut formën",
        'form_rectangle_insert': "Drejtkëndësh",
        'form_ellipse_insert': "Elipsë/rreth",
        'form_line_insert': "Vijë (2 klikime)",
        'form_arrow_insert': "Shigjetë (2 klikime)",
        'form_customize': " Përshtat formën",
        'form_transparent_toggle': " Sfond transparent",
        'form_discard': " Hidh këtë formë",
        'form_save_all': " Ruaj të gjitha format",
        'form_discard_all': " Hidh të gjitha format",
        'form_guide_title': "Futja e formave – Udhëzues",
        'form_guide': """
📐 Futja e formave në PDF – Udhëzues i shkurtër:

1. Zgjidhni llojin e formës (drejtkëndësh, elipsë, vijë, shigjetë)
2. Klikoni në vend
   - Drejtkëndësh/elipsë: një klikim vendos formën
   - Vijë/shigjetë: dy klikime për pikën e fillimit dhe të fundit
3. Poziciononi formën: zvarriteni me miun
4. Rregulloni madhësinë: zvarriteni nga qoshet/skajet
5. Ruaj formën: Enter
6. Hidh formën: ESC
7. Përshtatje të mëtejshme: klikoni me të djathtën mbi formë

Këshillë: Në menynë e kontekstit mund të rregulloni cilësimet.
        """,
        'form_inserted': "{0} u fut në faqen {1}",
        'form_deleted': "Forma u fshi",
        'form_copied': "Forma u kopjua",
        'form_pasted': "Forma u ngjit",
        'form_saved': "{0} forma u futën në PDF.\n\nPDF u ringarkua...",
        'form_saved_voice': "{0} forma u ruajtën",
        'form_reset': "Forma u kthye në madhësinë e paracaktuar",
        'form_transparent_on': "aktiv",
        'form_transparent_off': "joaktiv",
        'form_transparent_toggled': "Sfondi transparent {0}",
        'form_line_cancel': "Vizatimi i vijës u anulua",
        'form_second_click': "Tani klikoni pikën e fundit për {0}",
        'mode_replace_form': "Fut formë",
        'mode_conflict_voice_form': "Modaliteti {0} është aktiv. Të dalësh dhe të fusësh formën?",
        'form_settings_updated': "Cilësimet e formave u përditësuan",
        'form_unknown': "Formë",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klikoni pikën e fillimit",
        'form_line_guide_2': "2. Klikoni pikën e fundit",
        'form_line_guide_3': "Vija do të vizatohet midis dy pikave.",
        'form_line_status_1': "Në pritje të klikimit të parë...",
        'form_line_status_2': "Pika e parë u caktua: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Tani klikoni pikën e fundit...",
        'form_line_status_4': "Të dyja pikat u caktuan.\nKlikoni 'Përfundo' për të ruajtur.",
        'form_line_reset': "Rivendos",
        'form_line_finish': "Përfundo",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopjo (Cmd+C)",
        'paste': "Ngjit (Cmd+V)",
        'copied': "U kopjua: {0}",
        'no_element_to_copy': "Nuk u zgjodh asnjë element për kopjim",
        'no_copied_data': "Nuk ka të dhëna të kopjuara",
        'no_valid_position': "Nuk ka vend të vlefshëm për ngjitje",
        'copy_text': "Teksti u kopjua",
        'copy_image': "Imazhi u kopjua",
        'copy_form': "Forma u kopjua",
        'copy_signature': "Nënshkrimi u kopjua",
        'element_text': "Tekst",
        'element_image': "Imazh",
        'element_form': "Formë",
        'element_signature': "Nënshkrim",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflikt i modaliteteve",
        'mode_conflict_message': "Modaliteti '{0}' është tashmë aktiv.\n\nDëshironi të dilni prej tij dhe të {1}?",
        'mode_replace': "Dil nga modaliteti dhe {0}",
        'mode_cancel': "Anulo",
        'mode_replace_text': "fusësh tekst",
        'mode_replace_cross': "fusësh kryq",
        'mode_replace_signature': "fusësh nënshkrim",
        'mode_replace_image': "fusësh imazh",
        'mode_replace_form': "fusësh formë",
        'mode_conflict_voice': "Modaliteti {0} është aktiv. Të dalësh dhe të fusësh tekst?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Futja e tekstit",
        'active_mode_signature': "Nënshkrimi",
        'active_mode_image': "Imazhi",
        'active_mode_form': "Forma",
        'active_mode_and': " dhe ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Fut",
        'insert_another_text': "Fut tekst",
        'insert_another_cross': "Fut kryq",
        'insert_another_signature_1': "Nënshkrimi 1",
        'insert_another_signature_2': "Nënshkrimi 2",
        'insert_another_image': "Fut imazh",
        'insert_another_form_rect': "Drejtkëndësh",
        'insert_another_form_ellipse': "Elipsë",
        'insert_another_form_line': "Vijë (2 klikime)",
        'insert_another_form_arrow': "Shigjetë (2 klikime)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Ruaj {0}",
        'save_dialog_message': "{0} do të ruhet në faqen {1}.\n\nSi dëshironi të vazhdoni?",
        'save_all': "Ruaj të gjitha {0}",
        'save_single': "Ruaj {0}",
        'save_customize': "Përshtat {0}",
        'save_discard': "Hidh këtë {0}",
        'save_continue': "Vazhdo redaktimin",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Shko te faqja {0}",
        'context_rotate': " Rrotullo faqen {0}",
        'context_delete': " Fshi faqen {0}",
        'context_export': " Eksporto faqen {0}",
        'context_mark_as': " Shëno faqen si...",
        'context_mark_empty': " Faqe e zbrazët",
        'context_unmark_empty': " Jo më e zbrazët",
        'context_mark_export': " Shëno për eksport",
        'context_unmark_export': " Mos eksporto më",
        'context_batch_actions': " Veprime në grup",
        'context_batch_delete_empty': " Fshi të gjitha {0} faqet e zbrazëta",
        'context_batch_export_single': " Eksporto të gjitha {0} faqet (një skedar)",
        'context_batch_export_split': " Eksporto të gjitha {0} faqet (veçmas)",
        'context_drag_start': " Fillo zvarritjen",
        'context_drag_stop': " Ndale zvarritjen",
        'context_insert': " Fut",
        'context_insert_pages': " Fut faqe",
        'context_zoom': "Zmadhimi",
        'discard_mixed': "Hidh të gjitha {0} {1} dhe {2} {3}",
        'save_mixed': "Ruaj {0} {1} dhe {2} {3}",
        'discard_texts': "Hidh të gjitha {0} tekstet",
        'discard_text_single': "Hidh 1 tekst",
        'save_texts': "Ruaj {0} tekste",
        'save_text_single': "Ruaj 1 tekst",
        'discard_crosses': "Hidh të gjithë {0} kryqet",
        'discard_cross_single': "Hidh 1 kryq",
        'save_crosses': "Ruaj {0} kryqe",
        'save_cross_single': "Ruaj 1 kryq",
        'discard_signatures': "Hidh të gjitha {0} nënshkrimet",
        'save_signature_single': "Ruaj 1 nënshkrim",
        'save_signatures': "Ruaj {0} nënshkrime",
        'discard_images': "Hidh të gjitha {0} imazhet",
        'save_image_single': "Ruaj 1 imazh",
        'save_images': "Ruaj {0} imazhe",
        'discard_forms': "Hidh të gjitha {0} format",
        'save_form_single': "Ruaj 1 formë",
        'save_forms': "Ruaj {0} forma",
        'cross_discard': "Hidh këtë kryq",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informacion për eksport / import",
        'export_what': "📋 Çfarë eksportohet?",
        'export_general': "Cilësimet e përgjithshme",
        'export_general_items': "• Dalja zanore (aktive/joaktive, shpejtësia)\n• Modaliteti i errët/i ndritshëm\n• Cilësimet e kopjeve rezervë\n• Cilësimet e OCR",
        'export_image_form': "Cilësimet e imazheve dhe formave",
        'export_image_form_items': "• Cilësimet e imazheve (raporti i aspektit, madhësia e paracaktuar)\n• Cilësimet e formave (trashësia e vijës, ngjyrat)\n• Cilësimet e nënshkrimeve (shtigjet, madhësitë, vula kohore)",
        'export_passwords': "Baza e të dhënave të fjalëkalimeve",
        'export_passwords_items': "• Të gjitha fjalëkalimet e ruajtura PDF\n• Sipas zgjedhjes të shifruara ose të deshifruara",
        'export_master': "Cilësimet e fjalëkalimit master",
        'export_master_items': "• Hash-i i fjalëkalimit master\n• Cilësimet për nënshkrimet/blloqet e tekstit",
        'export_signatures': "Nënshkrimet dhe blloqet e tekstit",
        'export_signatures_items': "• Të gjithë skedarët e imazheve (nënshkrimet)\n• Të gjitha blloqet e tekstit me formatim\n• Shenjat private/publike",
        'export_import_warning': "⚠️ Shënime të rëndësishme",
        'export_import_note': "• Gjatë importit, TË GJITHA cilësimet aktuale do të mbishkruhen\n• Kërkohet rinisja e aplikacionit\n• Nënshkrimet/blloqet e tekstit ekzistues do të zëvendësohen",
        'export_master_note': "• Nëse fjalëkalimi master është caktuar, mund të zgjidhni:\n  - Të deshifruara (fjalëkalime në tekst të qartë)\n  - Të shifruara (të lexueshme vetëm me fjalëkalimin master)",
        'export_security': "• Skedari ZIP i eksportuar përmban të dhëna konfidenciale\n• Mbajeni në një vend të sigurt (p.sh. USB i shifruar)\n• Nëse humbni skedarin, fjalëkalimet humbasin përgjithmonë",
        'export_format': "📁 Formati i eksportit",
        'export_format_desc': "Cilësimet ruhen në një skedar të vetëm ZIP:",
        'export_filename': "Cilësimet_PDFDarkView_YYYYMMDD_HHMMSS.zip",
        'export_success': "Cilësimet u eksportuan me sukses",
        'export_failed': "Eksporti dështoi",
        'export_import_question': "Dëshironi ta rinisni aplikacionin tani?",
        'export_password_question': "Fjalëkalimi master është caktuar.\n\nDëshironi t'i eksportoni fjalëkalimet të deshifruara?\n(përndryshe ato do të eksportohen të shifruara)",
        'export_decrypt': "Eksporto të deshifruara",
        'export_encrypt': "Eksporto të shifruara",

      # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informacion",
        'info_title': "Rreth PDF Dark View",
        'info_version': "Versioni",
        'info_author': "Zhvilluar nga Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Rreth",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> është një shikues PDF i aksesueshëm, i zhvilluar posaçërisht për personat me dëmtim të shikimit.</p>

            <p><strong>Karakteristikat kryesore:</strong></p>
            <ul>
                <li>Ndërfaqe me kontrast të lartë, e personalizueshme</li>
                <li>Kontroll i plotë nga tastiera</li>
                <li>Dalje zanore e integruar</li>
                <li>OCR për dokumente të skanuara</li>
                <li>Mjete të gjera redaktimi</li>
            </ul>

            <p>Mbështeten më shumë se 50 gjuhë – në mënyrë që PDF-të të jenë të aksesueshme për të gjithë.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funksionet",
        'info_features_intro': "PDF Dark View ju ofron mundësitë e mëposhtme:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Shfaqja dhe navigimi</strong> – Mënyra e errët/e ndritshme, shfletimi i faqeve, zmadhimi, kërcimi te faqja</li>
            <li><strong>OCR (Njohja e tekstit)</strong> – Bëni dokumentet e skanuara të kërkueshme dhe të kopjueshme</li>
            <li><strong>Redaktimi</strong> – Futni tekst, kryqe, nënshkrime, imazhe dhe forma</li>
            <li><strong>Menaxhimi i faqeve</strong> – Fshirja, nxjerrja, futja, lëvizja me tërheq dhe lësho</li>
            <li><strong>Eksporti</strong> – Në Word, Pages ose si tekst</li>
            <li><strong>Siguria</strong> – Mbrojtja dhe menaxhimi me fjalëkalim</li>
            <li><strong>Aksesueshmëria</strong> – Dalje zanore, kontroll nga tastiera, kontrast i lartë</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Përdorimi",
        'info_accessibility': "♿ Aksesueshmëria – kontroll i plotë nga tastiera",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Të përgjithshme</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Hap PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Kërko</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Ndërro mënyrën e errët/të ndritshme</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Shtyp</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Dil</div>

        <div class="shortcut-cat">📖 Navigimi</div>
        <div class="shortcut-row"><kbd>Taste me shigjeta</kbd> Shfleto faqe për faqe</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Shko te faqja</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Faqja e parë</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Faqja e fundit</div>

        <div class="shortcut-cat">✏️ Redaktimi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Fut tekst</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Fshij faqe</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Nxjerr faqe</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Fut faqe</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Lëviz faqe</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rrotullo faqen</div>

        <div class="shortcut-cat">🖼️ Lëvizja e elementeve</div>
        <div class="shortcut-row"><kbd>Taste me shigjeta</kbd> Lëviz tekst/imazh/nënshkrim</div>
        <div class="shortcut-row"><kbd>Ctrl+Taste me shigjeta</kbd> Hapa më të mëdhenj</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Ruaj</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Anulo</div>

        <div class="shortcut-cat">🗣️ Dalje zanore</div>
        <div class="shortcut-row"><kbd>F2</kbd> Aktivizo/çaktivizo daljen zanore</div>
        """,
        'info_contextmenu': "📌 E rëndësishme: Të gjitha funksionet janë të arritshme edhe përmes menysë së kontekstit (butoni i djathtë i miut)!",
        'info_accessibility_hint': "💡 Këshillë: Dalja zanore (F2) lehtëson orientimin dhe jep reagime për menytë dhe dialogët.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licenca & Impresum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUM</strong><br>
        Informacione sipas § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Gjermani<br>
        E-mail: binhdiez64@gmail.com<br>
        Përgjegjës për përmbajtjen: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Heqja e përgjegjësisë</strong><br>
        Softueri është zhvilluar me kujdesin më të madh. Nuk jepet asnjë garanci për saktësinë, plotësinë dhe funksionalitetin. Përdorimi bëhet me përgjegjësinë tuaj.<br><br>

        <strong>📄 Licenca MIT (përdorim privat)</strong><br>
        E drejta e autorit (c) 2026 Toralf Schulz (BinhDiez)<br>
        E lejuar: përdorim falas, ndryshime private, kopje personale.<br>
        E palejuar: shitja, përdorimi tregtar, heqja e njoftimeve të së drejtës së autorit.<br><br>

        <strong>🔧 Komponentët e palëve të treta</strong><br>
        Ky softuer përmban komponentë nën licencat GPL, AGPL, Apache 2.0, BSD dhe MIT.<br>
        Gjatë rishpërndarjes, duhet të respektohen kushtet përkatëse të licencës.<br><br>

        <strong>🌐 Burim i hapur</strong><br>
        Kodi burimor është i disponueshëm dhe mund të shikohet, modifikohet dhe rishpërndahet sipas kushteve përkatëse të licencës.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Falënderime",
        'info_credits': "Falënderim për komunitetin me burim të hapur",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Përpunimi i PDF</li>
            <li><strong>PyQt5</strong> – Ndërfaqja grafike</li>
            <li><strong>Tesseract OCR</strong> – Njohja e tekstit</li>
            <li><strong>OCRmyPDF</strong> – Integrimi OCR</li>
            <li><strong>python-docx</strong> – Eksporti në Word</li>
            <li><strong>qtawesome</strong> – Ikonat</li>
            <li><strong>DeepSeek</strong> – Mbështetje për përkthime (50+ gjuhë)</li>
            <li><strong>Të gjithë përdoruesit</strong> – Për reagimet e vlefshme</li>
            <li><strong>Komunitetit me burim të hapur</strong> – Për bibliotekat e shkëlqyera</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Gjuhët",
        'info_languages_header': "🌍 Mbështetja e gjuhëve",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View aktualisht mbështet <strong>62 gjuhë</strong> – në mënyrë që softueri të mund të përdoret në mënyrë të aksesueshme në mbarë botën.</p>

            <p><strong>📖 Lista e plotë e gjuhëve (Statusi: Mars 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikanisht</li>
                    <li>🇦🇱 Shqip (Shqip)</li>
                    <li>🇩🇿 Arabisht (العربية)</li>
                    <li>🇮🇩 Balinezisht (Basa Bali)</li>
                    <li>🇧🇩 Bengalise (বাংলা)</li>
                    <li>🇲🇲 Birmanez (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Boshnjakisht (Bosanski)</li>
                    <li>🇧🇬 Bullgarisht (Български)</li>
                    <li>🇨🇳 Kinezisht (中文)</li>
                    <li>🇩🇰 Danisht (Dansk)</li>
                    <li>🇩🇪 Gjermanisht</li>
                    <li>🇬🇧 Anglisht (English)</li>
                    <li>🇪🇪 Estonisht (Eesti)</li>
                    <li>🇫🇮 Finlandisht (Suomi)</li>
                    <li>🇫🇷 Frëngjisht (Français)</li>
                    <li>🇬🇷 Greqisht (Ελληνικά)</li>
                    <li>🇮🇱 Hebraisht (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatisht (Hrvatski)</li>
                    <li>🇭🇺 Hungarisht (Magyar)</li>
                    <li>🇮🇩 Indonezisht (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandisht (Gaeilge)</li>
                    <li>🇮🇸 Islandisht (Íslenska)</li>
                    <li>🇮🇹 Italisht (Italiano)</li>
                    <li>🇯🇵 Japonisht (日本語)</li>
                    <li>🇰🇭 Kmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreanisht (한국어)</li>
                    <li>🇱🇦 Laosisht (ພາສາລາວ)</li>
                    <li>🇱🇻 Letonisht (Latviešu)</li>
                    <li>🇱🇹 Lituanisht (Lietuvių)</li>
                    <li>🇱🇺 Luksemburgisht (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajisht (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolisht (Монгол)</li>
                    <li>🇳🇵 Nepalise (नेपाली)</li>
                    <li>🇳🇱 Hollandisht (Nederlands)</li>
                    <li>🇳🇴 Norvegjisht (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persisht (فارسی)</li>
                    <li>🇵🇱 Polonisht (Polski)</li>
                    <li>🇵🇹 Portugalisht (Português)</li>
                    <li>🇮🇳 Punjabisht (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumanisht (Română)</li>
                    <li>🇷🇺 Rusisht (Русский)</li>
                    <li>🇸🇪 Suedisht (Svenska)</li>
                    <li>🇷🇸 Serbisht (Српски)</li>
                    <li>🇸🇰 Sllovakisht (Slovenčina)</li>
                    <li>🇸🇮 Sllovenisht (Slovenščina)</li>
                    <li>🇪🇸 Spanjisht (Español)</li>
                    <li>🇹🇿 Suahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamilisht (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Çekisht (Čeština)</li>
                    <li>🇹🇷 Turqisht (Türkçe)</li>
                    <li>🇺🇦 Ukrainisht (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamisht (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jidish (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Shto gjuhët e tua:</strong><br>
                Dëshironi një gjuhë që nuk është përfshirë ende? Thjesht vendosni skedarin tuaj të fjalorit (<code>sprache_xx.py</code>) pranë aplikacionit – softueri do ta njohë atë automatikisht. Nëse jeni të interesuar për një përkthim të veçantë, mos ngurroni të më kontaktoni.
            </div>

            <p><strong>🙏 Falënderim i veçantë:</strong> DeepSeek për mbështetjen në përkthimin e të gjitha fjalorëve në 62 gjuhë.</p>

            <p>📧 Kontakt për përkthime: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Gabim",
        'error_occurred': "Ndodhi një gabim",
        'error_pdf_load': "Gabim gjatë ngarkimit të PDF",
        'error_pdf_save': "Gabim gjatë ruajtjes së PDF",
        'error_ocr': "Gabim gjatë njohjes së tekstit",
        'error_no_pdf': "Asnjë PDF i ngarkuar",
        'error_page_not_found': "Faqja nuk u gjet",
        'error_invalid_range': "Interval faqesh i pavlefshëm",
        'error_file_not_found': "Skedari nuk u gjet",
        'error_permission': "Nuk ka leje",
        'error_unknown': "Gabim i panjohur",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Sukses",
        'success_operation': "Operacioni u krye me sukses",
        'success_saved': "U ruajt me sukses",
        'success_exported': "U eksportua me sukses",
        'success_imported': "U importua me sukses",
        'success_deleted': "U fshi me sukses",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Konfirmim",
        'confirm_yes': "Po",
        'confirm_no': "Jo",
        'confirm_ok': "OK",
        'confirm_cancel': "Anulo",
        'confirm_delete': "Fshi",
        'confirm_overwrite': "Mbishkruaj",
        'confirm_continue': "Vazhdo",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Duke ngarkuar PDF...",
        'progress_saving': "Duke ruajtur PDF...",
        'progress_exporting': "Duke eksportuar PDF...",
        'progress_processing': "Duke përpunuar...",
        'progress_wait': "Ju lutemi prisni...",
        'progress_preparing': "Duke përgatitur...",
        'progress_finalizing': "Duke përfunduar...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "E bardhë",
        'color_black': "E zezë",
        'color_red': "E kuqe",
        'color_green': "E gjelbër",
        'color_blue': "Blu",
        'color_yellow': "E verdhë",
        'color_magenta': "Magenta",
        'color_cyan': "Cian",
        'color_orange': "Portokalli",
        'color_gray': "Gri",
        'color_custom': "Zgjedhja e ngjyrës",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Skedari",
        'menu_edit': "&Redakto",
        'menu_view': "&Pamja",
        'menu_tools': "&Mjetet",
        'menu_settings': "&Cilësimet",
        'menu_help': "&Ndihmë",
        'menu_language': "🌐 Gjuha",
        'menu_guides': "&Udhëzuesit",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Hap",
        'file_save_as': "&Ruaj si...",
        'file_protect': "&Mbro dokumentin...",
        'file_export': "&Eksporto",
        'file_export_pages': "Eksporto në Pages",
        'file_export_word': "Eksporto në DOCX",
        'file_export_text': "Eksporto në TXT",
        'file_print_now': "&Printo tani",
        'file_print': "&Printo",
        'file_close': "&Mbylle",
        'file_quit': "&Dil",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Kërko",
        'edit_ocr': " Kryej OCR",
        'edit_rotate': "&Rrotullo faqen",
        'edit_rotate_all': "Rrotullo &të gjitha faqet",
        'edit_delete_pages': "&Fshi faqet",
        'edit_extract_pages': "&Nxirr faqet",
        'edit_insert_pages': "&Fut faqet",
        'edit_move_pages': "&Zhvendos faqet",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Fut tekst dhe kryqe",
        'text_insert': " Fut tekst",
        'cross_insert': " Fut kryq",
        'text_customize': " Përshtat tekstin",
        'cross_customize': " Përshtat këtë kryq",
        'cross_customize_all': " Përshtat të gjithë kryqet",
        'text_discard': " Hidh këtë tekst/kryq",
        'text_discard_all': " Hidh të gjitha tekstet dhe kryqet",
        'text_save_all': " Ruaj të gjitha tekstet dhe kryqet",
        'text_guide': " Futja e tekstit / blloqet e tekstit – udhëzues",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Fut nënshkrim",
        'signature_settings_menu': " Cilësimet...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Fut imazh",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Fut forma",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Shfaq dritaren e tekstit",
        'view_zoom': "&Zmadhimi",
        'view_zoom_page': "&Gjerësia e faqes (paracaktuar)",
        'view_zoom_two': "&Dy faqe",
        'view_zoom_overview': "&Përmbledhje (shumë faqe)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Qasja",
        'settings_voice': "Dalja zanore",
        'settings_voice_tooltip': "plotëson daljen zanore të lexuesve të ekranit me informacion shtesë",
        'settings_signature': "&Cilësimet e nënshkrimeve",
        'settings_password': "&Menaxhimi i fjalëkalimeve",
        'settings_backup': "Krijo kopje rezervë para ndryshimeve",
        'settings_export_import': "&Eksporto cilësimet / importo cilësimet",
        'settings_export': "&Eksporto të gjitha cilësimet...",
        'settings_import': "&Importo të gjitha cilësimet...",
        'settings_export_info': "&Çfarë eksportohet?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "aktiv",
        'voice_off': "joaktiv",
        'voice_toggle': "Dalja zanore {0}",
        'voice_speed': "Shpejtësia {0} përqind",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Mjeti nuk u gjet:\n{0}\n\nBASE_DIR: {1}\nSigurohuni që mjetet PDF janë instaluar në direktorinë {1}.",
        'tool_started': "{0} u nis",
        'tool_start_failed': "Nuk mund të nisej",
        'process_error_failed_to_start': "Procesi nuk mund të nisej. A ekziston skedari?",
        'process_error_crashed': "Procesi u rrëzua gjatë nisjes.",
        'process_error_timeout': "U arrit afati kohor i procesit.",
        'process_error_write': "Gabim shkrimi në proces.",
        'process_error_read': "Gabim leximi nga procesi.",
        'process_error_unknown': "Gabim i panjohur i procesit",
        'process_command': "Komanda",
        'process_normal_exit': "përfundoi normalisht",
        'process_crashed': "u rrëzua",
        'process_nonzero_exit': "{0} përfundoi me kodin e gabimit {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Duke anuluar...",
        'move_cancelling': "Zhvendosja po anulohet",
        'opening_pdf': "Duke hapur PDF...",
        'loading_document': "Duke ngarkuar dokumentin...",
        'pdf_opened': "PDF u hap",
        'pages_found_moving': "U gjetën {0} faqe, {1} për t'u zhvendosur",
        'creating_backup': "Duke krijuar kopje rezervë...",
        'backup_description': "Duke kopjuar skedarin origjinal...",
        'backup_saved_as': "Kopja rezervë u ruajt si: {0}",
        'error_format': "Gabim: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView nga BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Kërkimi u rivendos",
        'page_header_simple': "=== Faqja {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Menaxhimi i fjalëkalimeve – Udhëzues",
        'password_guide_voice': "Udhëzues për menaxhimin e fjalëkalimeve. Ju lutemi lexoni shënimet.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Menaxhimi i fjalëkalimeve – Udhëzues i detajuar</strong></p>

        <p><strong>1. Mbrojtja e PDF-ve me fjalëkalim</strong></p>
        <ul>
        <li>Kur hapni një PDF të mbrojtur me fjalëkalim, shfaqet një dialog ku mund të shkruani fjalëkalimin.</li>
        <li>Mund ta ruani fjalëkalimin të shifruar në mënyrë që të mos keni nevojë ta shkruani çdo herë (kutia e kontrollit "Ruaj fjalëkalimin").</li>
        <li>Me butonin "Hiq fjalëkalimin" mund të krijoni një kopje të deshifruar të PDF-së dhe të fshini fjalëkalimin nga baza e të dhënave.</li>
        </ul>

        <p><strong>2. Fjalëkalimi master</strong></p>
        <ul>
        <li>Fjalëkalimi master mbron qasjen në të gjitha fjalëkalimet e ruajtura PDF.</li>
        <li><strong>Caktimi:</strong> Shkoni te "Cilësimet → Menaxhimi i fjalëkalimeve → Cilësimet e fjalëkalimit master" dhe klikoni "Cakto fjalëkalimin master". Zgjidhni një fjalëkalim të fortë (të paktën 8 karaktere).</li>
        <li><strong>Ndryshimi:</strong> Pas autentikimit të suksesshëm, mund të ndryshoni fjalëkalimin master.</li>
        <li><strong>Heqja:</strong> Nëse hiqni fjalëkalimin master, TË GJITHA fjalëkalimet e ruajtura do të fshihen përgjithmonë. Para kësaj mund të eksportoni një kopje rezervë.</li>
        <li>Një herë për seancë, duhet të autentikoheni me fjalëkalimin master për të pasur qasje në funksionet e mbrojtura (p.sh. shfaqja e fjalëkalimeve).</li>
        </ul>

        <p><strong>3. Menaxhimi i fjalëkalimeve (lista)</strong></p>
        <ul>
        <li>Në "Cilësimet → Menaxhimi i fjalëkalimeve" hapet një tabelë e të gjitha PDF-ve të ruajtura me fjalëkalimet e tyre të shifruara.</li>
        <li><strong>Pa fjalëkalim master:</strong> Mund të fshini vetëm hyrjet – fjalëkalimet mbeten të fshehura.</li>
        <li><strong>Me fjalëkalim master (i autentikuar):</strong> Mund të shfaqni, kopjoni, eksportoni dhe fshini fjalëkalimet.</li>
        <li><strong>Eksporti:</strong> Zgjidhni një format (JSON, CSV, TXT) dhe ruani listën. Nëse fjalëkalimi master është caktuar, mund të zgjidhni nëse fjalëkalimet do të eksportohen të deshifruara apo të shifruara.</li>
        <li><strong>Importi:</strong> Një skedar ZIP i eksportuar më parë (të gjitha cilësimet) mund të importohet përsëri përmes "Cilësimet → Eksporto cilësimet / importo cilësimet". Kujdes: të dhënat ekzistuese do të mbishkruhen!</li>
        </ul>

        <p><strong>4. Gjeneruesi i fjalëkalimeve</strong></p>
        <ul>
        <li>Në dialogun e fjalëkalimit (p.sh. kur mbroni një PDF), në të djathtë të fushës së hyrjes gjendet një buton zari 🎲.</li>
        <li>Klikoni mbi të për të hapur gjeneruesin e fjalëkalimeve. Mund të caktoni gjatësinë, grupet e karaktereve (shkronja të mëdha, shkronja të vogla, numra, simbole) dhe ndarësin për lexueshmëri më të mirë.</li>
        <li>Fjalëkalimi i gjeneruar mund të përdoret drejtpërdrejt dhe, nëse nevojitet, të kopjohet.</li>
        </ul>

        <p><strong>5. Shënime të rëndësishme për sigurinë</strong></p>
        <ul>
        <li>Fjalëkalimet e ruajtura ruhen të shifruara me AES-256. Çelësi nxirret nga fjalëkalimi juaj master (nëse është caktuar) ose nga një vlerë fikse (pa fjalëkalim master).</li>
        <li>Pa fjalëkalim master, fjalëkalimet janë të shifruara, por çelësi është i integruar në program – një sulmues me qasje në skedarët tuaj mund t'i deshifrojë ato. Prandaj rekomandojmë fuqimisht përdorimin e një fjalëkalimi master.</li>
        <li>Baza e të dhënave të fjalëkalimeve ndodhet në skedarin `Data/passwords.json`. Bëni rregullisht kopje rezervë, veçanërisht para se të hiqni fjalëkalimin master.</li>
        <li>Nëse humbni fjalëkalimin master, të gjitha fjalëkalimet e ruajtura humbasin përgjithmonë.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Mënyra e përmbysjes",
        'invert_mode_classic': "Klasike (përmbys të gjitha ngjyrat)",
        'invert_mode_smart': "Inteligjente (përmbys vetëm shkëlqimin)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Pragu i shkallës gri",
        'gray_threshold_10': "10% (i rreptë)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Parazgjedhur)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (i butë)",
        'threshold_changed': "Pragu u vendos në {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Pragu i shkallës gri – Shpjegim",
        'threshold_guide_text': "Pragu i shkallës gri përcakton se cilët pixel në mënyrën inteligjente të errët konsiderohen 'gri' dhe përmbysen.\n\n"
                                "• Një vlerë e ulët (10%) përmbys vetëm nuancat gri pothuajse të përsosura – elementët me ngjyra mbeten plotësisht të ruajtura.\n"
                                "• Një vlerë e lartë (50%) përmbys gjithashtu pixelët pak të ngjyrosur – kjo rrit kontrastin, por mund të shtrembërojë ngjyrat.\n\n"
                                "Vlera optimale varet nga dokumenti. Për dokumente thjesht teksti, 30–40% shpesh është ideale, për grafika me ngjyra më mirë 10–20%.\n\n"
                                "Ju mund ta rregulloni vlerën në çdo kohë përmes menysë 'Cilësimet' – PDF do të ringarkohet menjëherë.\n\n"
                                "Shënim:\n* Fotot dhe imazhet mund të shfaqen saktë vetëm në mënyrën e ndritshme!\n* Cilësimet e përmbysjes shfaqen vetëm kur mënyra e errët është aktivizuar.",
        'threshold_guide_voice': "Pragu i shkallës gri përcakton se sa fuqishëm ndërhyn mënyra inteligjente e errët. Një vlerë e ulët kursen ngjyrat, një vlerë e lartë rrit kontrastin.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Po hapet PDF...",
        'progress_loading_document': "Po ngarkohet dokumenti...",
        'progress_pdf_opened': "PDF u hap",
        'progress_creating_backup': "Po krijohet rezervë...",
        'progress_backup_description': "Po sigurohet skedari origjinal...",
        'progress_backup_created': "Rezerva u krijua",
        'progress_backup_saved_as': "U ruajt si: {0}",
        'progress_analyzing_start': "Po fillon analiza...",
        'progress_searching_empty': "Po kërkohen faqet bosh...",
        'progress_page_empty': "Faqja {0} është bosh",
        'progress_page_keep': "Mbaj faqen {0}",
        'progress_analysis_complete': "Analiza përfundoi",
        'progress_empty_found': "U gjetën {0} faqe bosh",
        'progress_current_page': "Faqja aktuale",
        'progress_mark_delete': "Po shënohet për fshirje",
        'progress_range_selected': "Gama e faqeve {0}-{1}",
        'progress_deleting_pages': "Po fshihen {0} faqe",
        'progress_creating_new_pdf': "Po krijohet PDF e re...",
        'progress_transferring_pages': "Po transferohen faqet",
        'progress_keeping_page': "Faqja {0} do të mbahet ({1}/{2})",
        'progress_saving_pdf': "Po ruhet PDF...",
        'progress_optimizing': "Po optimizohet madhësia e skedarit...",
        'progress_finalizing': "Po finalizohet...",
        'progress_new_size': "Madhësia e re: {0:.2f} MB",
        'progress_cancelling': "Po anulohet...",
        'progress_cancel_message': "{0} po anulohet",
        'progress_pages_found_moving': "U gjetën {0} faqe, {1} për të lëvizur",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Po analizohet PDF...",
        'ocr_status_optimizing': "Optimizimi i imazhit në vazhdim...",
        'ocr_status_recognizing': "Njohja e tekstit në vazhdim...",
        'ocr_status_embedding': "Po futet teksti...",
        'ocr_status_finalizing': "Po finalizohet PDF...",

        # PDF-Laden
        'progress_preparing': "Po përgatitet...",
        'progress_loading': "Po ngarkohet PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Po fshihen faqet...",
        'progress_moving_title': "Po lëvizen faqet...",
        'pages_found': "Faqet e gjetura",
        'progress_creating_new_order': "Po krijohet rendi i ri...",
        'progress_sorting_pages': "Po renditen faqet...",
        'progress_moving_to_begin': "Lëviz {0} faqe në fillim",
        'progress_transferring_count': "Transfero {0} faqe",
        'progress_transferring_before_target': "Transfero faqet para objektivit",
        'progress_moving_pages': "Lëviz {0} faqe",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_rezerve_",
        'filename_protected_suffix': "_mbrojtur_",
        'filename_copy_suffix': "_Kopje",
        'filename_page_single': "_Faqja_",
        'filename_page_range': "_Faqet_",
        'filename_export_page': "_Faqja_{0:03}",
        'filename_export_range': "_Faqet_{0}-{1}",
        'filename_export_multiple': "_Faqet_{0}",
        'filename_with_text': "_me_Tekst",
        'filename_with_signature': "_me_Nenshkrim",
        'filename_with_image': "_me_Imazh",
        'filename_with_forms': "_me_Forma",
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
        'view_toggle_navbar': "Shfaq shiritin e butonave",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Nuk mund të fshihen të gjitha faqet",
		'pages_cannot_delete_last_page': 'Faqja e fundit nuk mund të fshihet!',
		'pages_cannot_delete_all_pages': 'Të paktën një faqe duhet të mbetet në dokument!',
		'delete_pages_confirm': 'Jeni i sigurt që dëshironi të fshini {0} faqe?',
		'delete_pages_confirm_voice': 'Jeni i sigurt që dëshironi të fshini {0} faqe?',
		'pages_deleted': '{0} faqe u fshinë me sukses.',
		'warning': 'Paralajmërim',
		'error': 'Gabim',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Asnjë formë e zgjedhur",
        'form_customized': "Forma e personalizuar",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Përzgjidh",
        'btn_use': "Përdor",
        'master_password_for_spasswords': "Për të ruajtur dhe përdorur fjalëkalimet, së pari duhet të vendosni një fjalëkalim master.\n\nDëshironi të vendosni fjalëkalimin master tani?",
        'open_saved_dialog_title': "Hap skedarin e ruajtur",
        'open_saved_question': "Dëshironi të hapni skedarin e ruajtur tani?",
        'password': "Fjalëkalim",
        'password_manager_master_required': "Menaxheri i fjalëkalimeve është i disponueshëm vetëm nëse është vendosur një fjalëkalim master.\n\nDëshironi të vendosni fjalëkalimin master tani?",
        'password_master_required_for_select': "Për të parë dhe përzgjedhur fjalëkalimet e ruajtura, së pari duhet të autentifikoheni me fjalëkalimin tuaj master.\n\nDëshironi të autentifikoheni tani?",
        'password_not_available': "Fjalëkalimi i përzgjedhur nuk është i disponueshëm ose nuk mund të deshifrohet.",
        'password_options_title': "Opsionet e fjalëkalimit",
        'password_save_choice_change': "Vendos fjalëkalim të ri",
        'password_save_choice_keep': "Përdor fjalëkalimin ekzistues",
        'password_save_choice_none': "Ruaj pa enkriptim",
        'password_save_hint': "Së pari vendosni një fjalëkalim master për të ruajtur fjalëkalimet në mënyrë të sigurt.",
        'password_save_master_required': "Ruaj fjalëkalimin (i mundshëm vetëm me fjalëkalim master)",
        'password_save_question': "PDF-ja aktuale është e mbrojtur me fjalëkalim. Dëshironi të përdorni fjalëkalimin ekzistues, të vendosni një të ri apo të ruani pa enkriptim?",
        'password_select': "Përzgjidh fjalëkalimin",
        'password_select_none': "Nuk është përzgjedhur asnjë fjalëkalim.\n\nJu lutemi përzgjidhni një fjalëkalim nga lista.",
        'password_select_one': "Ju lutemi përzgjidhni saktësisht një fjalëkalim.\n\nJu keni shënuar disa fjalëkalime.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_kopje_rezervë",
        'filename_insert_suffix': "_me_futje",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_faqet_u_fshinë",
        'filename_pages_moved': "_faqet_u_lëvizën",
        'filename_rotated_all_suffix': "_të_gjitha_faqet_u_rrotulluan",
        'filename_rotated_suffix': "_faqja_u_rrotullua",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurimi i emrave të skedarëve gjatë ndryshimit të PDF",
        'filename_keep_suffixes': "Mbaji prapashtesat e mëparshme (p.sh. _me_tekst)",
        'filename_keep_suffixes_false': "Zëvendëso",
        'filename_keep_suffixes_true': "Mbaj",
        'filename_preview_label': "Parapamje e emrit të skedarit:",
        'filename_preview_overwrite_hint': "Parapamja jo e disponueshme – origjinali do të mbishkruhet.",
        'filename_separator': "Ndarësi midis fjalëve",
        'filename_separator_none': "Pa ndarës",
        'filename_separator_space': "Hapësirë ( )",
        'filename_separator_underscore': "Nënvizë (_)",
        'filename_settings_saved': "Cilësimet e emrit të skedarit u ruajtën",
        'filename_settings_title': "Formësimi i emrit të skedarit dhe kopje rezervë",
        'filename_timestamp_position': "Pozicioni i vulës kohore",
        'filename_timestamp_position_after': "Pas emrit bazë",
        'filename_timestamp_position_before': "Shumë përpara",
        'filename_timestamp_position_end': "Në fund",
        'filename_use_timestamp': "Përdor vulë kohore",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Sjellja gjatë ndryshimeve:</b><ul><li>Fshirja dhe futja e faqeve</li><li>Futja e tekstit, nënshkrimit, figurës dhe formave</li><li>OCR</li></ul></html>",
        'backup_section': "Kopje rezervë për operacionet me faqe (Fshij, Lëviz)",
        'behavior_info': "Shënim: Tek 'Mbishkruaj origjinalin', vulat kohore dhe prapashtesat injorohen – skedari mban emrin e tij.",
        'behavior_new_file': "Gjithmonë krijo skedar të ri (me vulë kohore dhe prapashtesë)",
        'behavior_overwrite': "Mbishkruaj origjinalin (pa skedar të ri)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Të gjitha faqet u rrotulluan.\n\nOrigjinali mbeti i pandryshuar.\nSkedar i ri: {0}",
        'all_pages_rotated_voice': "Të gjitha faqet u rrotulluan, u krijua skedar i ri.",
        'empty_pages_deleted_new_file': "{0} faqe boshe u fshinë.\n\nOrigjinali mbeti i pandryshuar.\nSkedar i ri: {1}",
        'empty_pages_deleted_voice': "{0} faqe boshe u fshinë, u krijua skedar i ri.",
        'ocr_keep_original': "Mbaj origjinalin (hap manualisht më vonë)",
        'ocr_new_file_question': "PDF-ja e re e kërkueshme u ruajt në:\n{0}\n\nDëshironi ta hapni tani?",
        'ocr_open_new': "Hap skedarin e ri OCR",
        'ocr_original_kept': "Skedari origjinal mbetet i hapur. Skedari OCR u ruajt.",
        'page_deleted_new_file': "Faqja {0} u fshi.\n\nOrigjinali mbeti i pandryshuar.\nSkedar i ri: {1}",
        'page_deleted_voice': "Faqja {0} u fshi, u krijua skedar i ri.",
        'page_rotated_new_file': "Faqja {0} u rrotullua.\n\nOrigjinali mbeti i pandryshuar.\nSkedar i ri: {1}",
        'page_rotated_voice': "Faqja {0} u rrotullua, u krijua skedar i ri.",
        'pages_deleted_new_file': "U fshinë {0} faqe.\n\nSkedari origjinal mbeti i pandryshuar.\nSkedar i ri: {1}",
        'pages_deleted_new_file_voice': "{0} faqe u fshinë, u krijua skedar i ri.",
        'pages_inserted_new_file': "U futën {0} faqe.\n\nSkedari origjinal mbeti i pandryshuar.\nSkedar i ri: {1}",
        'pages_inserted_new_file_ask': "U futën {0} faqe.\n\nOrigjinali mbeti i pandryshuar.\nSkedar i ri: {1}\n\nDëshironi ta hapni tani?",
        'pages_inserted_voice_new': "{0} faqe u futën, u krijua skedar i ri.",
        'pages_moved_new_file': "U lëvizën {0} faqe.\n\nSkedari origjinal mbeti i pandryshuar.\nSkedar i ri: {1}",
        'pages_moved_new_file_voice': "{0} faqe u lëvizën, u krijua skedar i ri.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Mos e shfaq më",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Cilësimi i kopjes rezervë</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Kopje rezervë AKTIVE</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Për të gjitha ndryshimet që mbishkruajnë origjinalin</strong> (tekst, nënshkrim, figurë, formë, OCR, rrotullim, futje, fshirje/lëvizje faqesh) <strong>krijohet automatikisht një kopje rezervë me vulë kohore</strong> përpara se të zbatohet ndryshimi.</p>
                <p style="margin: 5px 0 5px 20px;">• Kopja rezervë ndodhet pranë skedarit origjinal (p.sh. <code>Dokumenti_kopje_rezervë_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Nëse keni aktivizuar gjithashtu opsionin <strong>„Mbishkruaj origjinalin“</strong>, krijohet gjithashtu një kopje rezervë.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Kopje rezervë JOAKTIVE</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Nuk krijohet asnjë kopje rezervë</strong> – as gjatë mbishkrimit, as gjatë operacioneve me faqe.</p>
                <p style="margin: 5px 0 5px 20px;">• Skedari origjinal mund të humbet në mënyrë të pakthyeshme gjatë mbishkrimit.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Rekomandohet vetëm për përdoruesit me përvojë!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Këshillë:</strong> Cilësimi i kopjes rezervë është i pavarur nga opsioni „Mbishkruaj origjinalin“. Ju mund t'i kombinoni të dyja.<br>
                Ju mund ta fshehni këtë mesazh përgjithmonë.
            </div>
        </div>
        """,
        'backup_info_title': "Sjellja e kopjes rezervë",
        'backup_info_voice': "Njoftim për sjelljen e kopjes rezervë gjatë operacioneve me faqe. Kopje rezervë aktive mbishkruan origjinalin, joaktive krijon skedar të ri.",
        'show_backup_info': "Informacion rreth cilësimit të kopjes rezervë",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Mos e shfaq më",
        'overwrite_enable_backup': "Aktivizo kopjen rezervë (rekomandohet)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Mbishkruaj origjinalin</p>
            <p>Nëse e aktivizoni këtë opsion, ndryshimet (tekst, nënshkrim, figurë, formë, OCR, rrotullim, futje) <strong>ruhen direkt në origjinal</strong> – <strong>nuk krijohet asnjë skedar i ri</strong>.</p>
            <p>• Emri i skedarit mbetet i pandryshuar.<br>
            • Vulat kohore dhe prapashtesat injorohen.<br>
            • <strong>Pa kopje rezervë, origjinali mund të humbet në mënyrë të pakthyeshme.</strong></p>
            <p style="color: #FFD700;">Rekomandim: Aktivizoni gjithashtu opsionin e kopjes rezervë për të marrë kopje të sigurisë automatike.</p>
        </div>
        """,
        'overwrite_info_title': "Mbishkruaj origjinalin",
        'overwrite_info_voice': "Paralajmërim: Mbishkruaj origjinalin – pa skedar të ri. Kopje rezervë rekomandohet.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "U futën {0} faqe.\n\nSkedari origjinal u mbishkrua.\nU krijua një kopje rezervë.",
        'pages_inserted_overwrite_no_backup': "U futën {0} faqe.\n\nSkedari origjinal u mbishkrua.\nNUK u krijua asnjë kopje rezervë.",
        'texts_saved_overwrite_with_backup': "Ndryshimet u ruajtën në origjinal.\n\nU krijua një kopje rezervë.",
        'texts_saved_overwrite_no_backup': "Ndryshimet u ruajtën në origjinal.\n\nNUK u krijua asnjë kopje rezervë.",
        'texts_crosses_saved_new_file': "{0} {1} dhe {2} {3} u futën.\n\nSkedari origjinal mbeti i pandryshuar.\nU krijua një skedar i ri.\n\nPo ngarkohet PDF-ja e re...",
        'texts_saved_new_file': "{0} {1} u futën.\n\nSkedari origjinal mbeti i pandryshuar.\nU krijua një skedar i ri.\n\nPo ngarkohet PDF-ja e re...",
        'crosses_saved_new_file': "{0} {1} u futën.\n\nSkedari origjinal mbeti i pandryshuar.\nU krijua një skedar i ri.\n\nPo ngarkohet PDF-ja e re...",
        'elements_saved_new_file': "{0} elemente u futën.\n\nSkedari origjinal mbeti i pandryshuar.\nU krijua një skedar i ri.\n\nPo ngarkohet PDF-ja e re...",
        'signatures_saved_overwrite_with_backup': "Nënshkrimi(et) u ruajt(ën) në origjinal.\n\nU krijua një kopje rezervë.",
        'signatures_saved_overwrite_no_backup': "Nënshkrimi(et) u ruajt(ën) në origjinal.\n\nNUK u krijua asnjë kopje rezervë.",
        'images_saved_overwrite_with_backup': "Figura(t) u ruajt(ën) në origjinal.\n\nU krijua një kopje rezervë.",
        'images_saved_overwrite_no_backup': "Figura(t) u ruajt(ën) në origjinal.\n\nNUK u krijua asnjë kopje rezervë.",
        'forms_saved_overwrite_with_backup': "Forma(t) u ruajt(ën) në origjinal.\n\nU krijua një kopje rezervë.",
        'forms_saved_overwrite_no_backup': "Forma(t) u ruajt(ën) në origjinal.\n\nNUK u krijua asnjë kopje rezervë.",
        'signatures_saved_new_file': "{0} nënshkrime u futën.\n\nSkedari origjinal mbeti i pandryshuar.\nU krijua një skedar i ri.\n\nPo ngarkohet PDF-ja e re...",
        'images_saved_new_file': "{0} figura u futën.\n\nSkedari origjinal mbeti i pandryshuar.\nU krijua një skedar i ri.\n\nPo ngarkohet PDF-ja e re...",
        'forms_saved_new_file': "{0} forma u futën.\n\nSkedari origjinal mbeti i pandryshuar.\nU krijua një skedar i ri.\n\nPo ngarkohet PDF-ja e re...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Paralajmërim: Kjo PDF përmban faqe të rrotulluara. Pozicionimi mund të jetë i ndryshëm.",
        'page_rotated_warning_title': "U zbulua një faqe e rrotulluar",
        'page_rotated_warning_message': "Faqja aktuale {0} është rrotulluar {1}°.\n\nFutja e elementeve në faqet e rrotulluara nuk mbështetet.\n\nDëshironi ta rrotulloni faqen në pozicion vertikal tani?",
        'page_rotated_warning_voice': "Paralajmërim: Faqja është rrotulluar. Ju lutemi rrotullojeni së pari.",
        'paste_on_rotated_page_simple_warning': "Futja në faqen {0} nuk është e mundur!\n\nKjo faqe është rrotulluar {1}°.\n\nJu lutemi rrotulloni së pari faqen në 0° (Menu: Redakto → Rreshto faqen).\n\nParalajmërim:\nElementi i kopjuar më parë do të humbasë nëse nuk ruani para se të rrotulloni faqen.",
        'paste_on_rotated_page_voice': "Futja u anulua. Faqja është rrotulluar. Ju lutemi rreshtoni së pari faqen.",
        'page_rotated_cancel': "Anulo",
        'page_rotated_rotate_until_upright': "Rrotullo faqen në mënyrë të përsëritur (derisa të jetë vertikale)",
        'page_rotated_now_upright': "Faqja tani është vertikale. Tani mund të futni.",
        'page_rotated_still_not_upright': "Faqja nuk mund të rrotullohej në pozicion vertikal. Ju lutemi korrigjoni manualisht.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Ndihmë: Korrigjo faqet e rrotulluara",
        'help_rotated_pages_voice': "Hapet ndihma për korrigjimin e faqeve të rrotulluara.",
        'btn_help': "Ndihmë",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Faqe e rrotulluar – Futja nuk funksionon siç duhet</p>

            <p>Nëse futja e teksteve, nënshkrimeve ose formave në një faqe të rrotulluar nuk funksionon siç duhet, mund ta korrigjoni faqen me një redaktues PDF të jashtëm.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Zgjidhje me mjet të jashtëm (p.sh. Parapamje macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksporto faqen</strong><br>
                &nbsp;&nbsp;Klikoni në menunë <strong>Skedar → Eksporto si faqe</strong> ose përdorni një metodë tjetër për të ruajtur faqen e dëshiruar si një PDF të vetme.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Hap faqen në një program të jashtëm</strong><br>
                &nbsp;&nbsp;Hapni PDF-në e eksportuar në një redaktues PDF (p.sh. <strong>Parapamje macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rrotullo faqen</strong><br>
                &nbsp;&nbsp;Rrotullojeni faqen në mënyrë që të jetë vertikale (në Parapamje: <strong>Mjetet → Rrotullo</strong> ose <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Ruaj</strong><br>
                &nbsp;&nbsp;Ruani faqen e korrigjuar (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Fute përsëri faqen në dokumentin origjinal</strong><br>
                &nbsp;&nbsp;Kthehuni te PDFDarkView dhe futni faqen e korrigjuar në pozicionin e dëshiruar:<br>
                &nbsp;&nbsp;<strong>Redakto → Fut faqe</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativë: Rrotullo faqen në origjinal</p>
                <p style="margin: 5px 0 5px 20px;">• Përdorni funksionin e integruar të rrotullimit (<strong>Redakto → Rrotullo faqen</strong>) për të korrigjuar faqen hap pas hapi.<br>
                • Pas çdo rrotullimi, mund të kontrolloni nëse futja tani funksionon.<br>
                • Kjo është shpesh zgjidhja më e shpejtë – provojeni së pari!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Këshillë:</strong> Nëse hasni shpesh faqe të rrotulluara, mund ta fshehni përgjithmonë paralajmërimin në dialogun e futjes.<br>
                Pozicionimi mund të jetë atëherë i ndryshëm – përdorni këtë opsion vetëm nëse i dini pasojat.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Rreshto faqet",
        'menu_rotate_normalize_tooltip': "Rrotullo faqen ose rivendos në 0°",
        'normalize_current_page': "Sill faqen aktuale në pozicion vertikal (vendose në 0°)",
        'normalize_all_pages': "Sill të gjitha faqet në pozicion vertikal (vendose në 0°)",
        'page_normalized': "Faqja {0} u vendos në pozicion vertikal.",
        'all_pages_normalized': "Të gjitha faqet u vendosën në pozicion vertikal.",
        'page_already_upright': "Faqja {0} është tashmë vertikale.",
        'all_pages_already_upright': "Të gjitha faqet janë tashmë vertikale.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF-ja nuk përmban tekst të kërkueshëm.</p><p>Dëshironi të kryeni OCR për të eksportuar në {0}?</p>",
        'export_ocr_voice': "PDF-ja nuk përmban tekst. OCR kërkohet për eksport në {0}.",
        'export_no_ocr_possible': "Eksportimi pa OCR nuk është i mundur. Ju lutemi kryeni OCR përmes menysë.",
        'ocr_failed_export_not_possible': "OCR dështoi. Eksportimi nuk mund të kryhet.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF-ja do të hapet në Parapamje. Ju lutemi filloni procesin e printimit atje.",
        'print_preview_manual': "PDF-ja u hap. Ju lutemi ekzekutoni komandën e printimit manualisht (p.sh. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Bashko PDF-të",
        'merge_pdfs': "Bashko PDF-të",
        'merge_progress_title': "Po bashkohen PDF-të...",
        'merge_pdfs_list': "PDF-të sipas radhës (Tërhiqe dhe lësho për renditje)",
        'merge_add_pdf': "Shto PDF",
        'merge_remove': "Hiq",
        'merge_move_up': "Lart",
        'merge_move_down': "Poshtë",
        'merge_pdfs_info': "💡 Këshillë: Ju mund të ndryshoni renditjen duke tërhequr dhe lëshuar",
        'merge_no_pdfs': "Nuk është zgjedhur asnjë PDF. Klikoni 'Shto PDF'.",
        'merge_info': "{0} PDF të zgjedhura (rreth {1} faqe)",
        'merge_open_file': "Hap skedarin",
        'merge_merge': "Bashko",
        'merge_error': "Gabim gjatë bashkimit",
        'merge_min_two_pdfs_error': "Ju lutemi zgjidhni të paktën dy skedarë PDF për t'u bashkuar.",
        'merge_select_pdfs': "Zgjidhni PDF-të për t'u bashkuar",
        'merge_error_file': "Gabim gjatë përpunimit",
        'merge_cancelled': "Bashkimi u anulua",
        'merge_preparing': "Po përgatitet...",
        'merge_processing': "Po përpunohet PDF {0} nga {1}",
        'merge_saving': "Po ruhet PDF-ja e bashkuar...",
        'merge_complete': "U krye!",
        'merge_success_title': "Bashkimi u krye me sukses",
        'merge_success_voice': "{0} PDF u bashkuan me sukses.",
        'merge_success_message': "{0} PDF u bashkuan me sukses.\n\nDokumenti i ri tani ka {1} faqe.\n\nSkedar i ri:\n{2}\n\nVendndodhja e ruajtjes:\n{3}\n{2}\n\nDëshironi të hapni këtë PDF?",
        'replace_file_title': "Të zëvendësohet skedari?",
        'replace_file_message': "Tashmë është hapur një PDF. Dëshironi ta zëvendësoni atë me skedarin e ri?",
        'btn_yes': "Po",
        'btn_no': "Jo",
        'filename_merge_suffix': "bashkuar",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Po hapet {0}...",
        'progress_merge_reading': "Po lexohet {0}...",
        'progress_merge_adding': "Po shtohen {0} faqe...",
        'progress_merge_optimizing': "Po optimizohet PDF...",
        'progress_merge_writing': "Po shkruhet PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "mbylljen e PDF-së",
        'action_close_window': "mbylljen e dritares",
        'action_open_new_pdf': "hapjen e një PDF të re",
        'action_quit_app': "daljen nga aplikacioni",
        'changes_saved': "Ndryshimet u ruajtën.",
        'file_close_title': "Mbyll skedarin PDF",
        'save_before_action': "A duhet të ruhen ndryshimet para {0}? Po ose Jo?",
        'save_before_action_voice': "A duhet të ruhen ndryshimet para {0}? Po ose Jo?",
        'save_before_close_question': "A duhet të ruhen ndryshimet para mbylljes? Po ose Jo?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>U krijua PDF i kërkueshëm:\n\n{0}\n\n<b>provo përsëri nëse është e nevojshme",
        "ocr_rotate_title": "Rreshto faqet para OCR",
        "ocr_rotate_question": "PDF përmban faqe të rrotulluara.\nDëshironi t'i rreshtoni të gjitha faqet në 0° para OCR?\nKjo përmirëson ndjeshëm njohjen e tekstit.",
        "ocr_rotate_yes": "Po, rreshtoji",
        "ocr_rotate_no": "Jo, fillo OCR drejtpërdrejt",
        "ocr_rotate_voice": "PDF përmban faqe të rrotulluara. A duhet të rreshtohen të gjitha faqet para OCR?",
        "ocr_not_performed_message": "Nuk ka tekst. Ju lutemi kryeni OCR (menyja \"Redakto\" → \"Kryej OCR\" ose taste Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Cilësimet e OCR",
        "ocr_language_btn": "Zgjidh gjuhën e OCR",
        "ocr_language": "Gjuha(t) e OCR",
        "ocr_language_current": "Gjuha aktuale:",
        "ocr_param_info": "Informacion rreth parametrit",

        "ocr_force_ocr_label": "Detyro OCR",
        "ocr_deskew_label": "Korrigjo animin",
        "ocr_clean_label": "Pastro imazhin",
        "ocr_oversample_label": "Rezolucioni (DPI)",
        "ocr_pagesegmode_label": "Ndarja e faqes",
        "ocr_oem_label": "Mënyra e motorit OCR",
        "ocr_optimize_label": "Kompresimi i PDF",
        "ocr_jobs_label": "Proceset paralele",
        "ocr_verbose_label": "Detajimi i regjistrit",

        "ocr_force_ocr_tooltip": "Detyro OCR në çdo faqe, edhe nëse teksti ekziston tashmë",
        "ocr_deskew_tooltip": "Rreshto automatikisht skanimet e anuara",
        "ocr_clean_tooltip": "Hiq zhurmën dhe artefaktet nga imazhi",
        "ocr_oversample_tooltip": "Zmadho imazhin para OCR në këtë DPI",
        "ocr_pagesegmode_tooltip": "Përcakton se si faqja ndahet në zona teksti",
        "ocr_oem_tooltip": "Zgjedh motorin OCR të Tesseract",
        "ocr_optimize_tooltip": "Niveli i kompresimit të PDF-së dalëse",
        "ocr_jobs_tooltip": "Numri i proceseve paralele të OCR",
        "ocr_verbose_tooltip": "Niveli i detajimit të daljes së regjistrit",
        "ocr_settings_explain_btn": "Shpjegim",

        "ocr_force_ocr_explain": "Detyron njohjen e tekstit në <b>çdo</b> faqe, edhe nëse ajo përmban tashmë tekst.\n\nRekomandim: <b>Aktiv</b> për PDF të skanuara, <b>Joaktiv</b> për PDF vendase me tekst ekzistues.",

        "ocr_deskew_explain": "Korrigjon skanimet pak të anuara (deri në rreth 5°).\n\nRekomandim: <b>Aktiv</b> për dokumente të skanuara, <b>Joaktiv</b> nëse faqet janë tashmë perfektisht të drejta.",

        "ocr_clean_explain": "Heq zhurmën, pikat dhe artefaktet e vogla nga imazhi.\n<b>E RËNDËSISHME:</b> Për tekstet arabe, tailandeze ose vietnameze me shenja diakritike (pika sipër/poshtë shkronjave) kjo mundësi duhet të <b>çaktivizohet</b>, përndryshe mund të humbasin karaktere të rëndësishme.",

        "ocr_oversample_explain": "Zmadhon imazhin <b>para</b> njohjes së tekstit në DPI-në e specifikuar.<br><br>• <b>72-150 DPI:</b> Shumë i shpejtë, por shkallë e ulët njohjeje<br>• <b>200-300 DPI:</b> Gama optimale (Parazgjedhur: 300)<br>• <b>400+ DPI:</b> Vështirë se njohje më e mirë, por skedarë dukshëm më të mëdhenj<br><br>Rekomandim: 300 DPI për shkrime komplekse (arabe, kineze, japoneze), 200 DPI për gjuhë perëndimore.",

        "ocr_pagesegmode_explain": "Përcakton se si Tesseract e ndan faqen në zona teksti.\n\n• <b>3 - Automatike (Parazgjedhur):</b> Mirë për paraqitje të përziera\n• <b>4 - Kolonë e vetme:</b> Për tekste me një kolonë\n• <b>5 - Bllok vertikal:</b> Për shkrime vertikale (japoneze, kineze)\n• <b>6 - Bllok teksti uniform:</b> Optimale për tekst të rrjedhshëm pa kolona\n• <b>11 - Imazh i papërpunuar:</b> Për skanime të këqija / shkrim dore\n\nRekomandim: <b>6</b> për dokumente të thjeshta teksti, <b>3</b> për paraqitje komplekse.",

        "ocr_oem_explain": "Zgjedh motorin OCR të Tesseract.\n\n• <b>0 - Legacy:</b> Motor i vjetër (i shpejtë, por më pak i saktë)\n• <b>1 - LSTM:</b> Motor neuronal (më i ngadalshëm, por më i saktë)\n• <b>2 - Legacy + LSTM:</b> Kumbinon të dy rezultatet\n• <b>3 - Parazgjedhur (LSTM preferohet):</b> Zgjedhja më e mirë për shumicën e rasteve\n\nRekomandim: <b>3</b> për saktësi maksimale të njohjes.",

        "ocr_optimize_explain": "Kompreson PDF-në dalëse.\n\n• <b>0:</b> Pa optimizim (përpunimi më i shpejtë)\n• <b>1:</b> Optimizim i lehtë (kompromis i mirë)\n• <b>2:</b> Optimizim i moderuar\n• <b>3:</b> Optimizim i fortë (skedari më i vogël, por më i ngadalshëm)\n\nRekomandim: <b>1</b> për përdorim të përditshëm.",

        "ocr_jobs_explain": "Numri i proceseve paralele për OCR.\n\n• <b>1:</b> I ngadalshëm, por konsumi më i ulët i memories\n• <b>4-8:</b> Optimale për procesorët modernë me shumë bërthama\n• <b>12+:</b> Vështirë se përpunim më i shpejtë me konsum të lartë memorie\n\nRekomandim: Numri i bërthamave të CPU-së (p.sh. <b>4</b> në sistemet me 4 bërthama).",

        "ocr_verbose_explain": "Niveli i detajimit të daljes së regjistrit në konsolë.\n\n• <b>0:</b> Pa dalje\n• <b>1:</b> Përparim dhe mesazhe statusi\n• <b>2:</b> Dalje e detajuar\n• <b>3:</b> Dalje e plotë e korrigjimit (shumë e gjerë)\n\nRekomandim: <b>1</b> për funksionim normal.",

        "ocr_reset_title": "Cilësimet u rivendosën",
        "ocr_reset_message": "Të gjitha cilësimet e OCR u rivendosën në vlerat e parazgjedhura.",
        "info_tooltip": "Më shumë informacion rreth këtij parametri",
        "ocr_reset_defaults": "Rivendos në parazgjedhje",

        "ocr_psm_0": "Automatike (motori Legacy)",
        "ocr_psm_1": "Zbulim automatik i kolonave",
        "ocr_psm_3": "Automatike (Parazgjedhur)",
        "ocr_psm_4": "Kolonë e vetme",
        "ocr_psm_5": "Bllok vertikal",
        "ocr_psm_6": "Bllok teksti uniform",
        "ocr_psm_7": "Rresht i vetëm teksti",
        "ocr_psm_8": "Fjalë e vetme",
        "ocr_psm_11": "Imazh i papërpunuar (pa analizë paraqitjeje)",

        "ocr_oem_0": "Motori Legacy (i shpejtë)",
        "ocr_oem_1": "Motori LSTM (neuronal, i saktë)",
        "ocr_oem_2": "Legacy + LSTM i kombinuar",
        "ocr_oem_3": "Parazgjedhur (LSTM preferohet)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Gjuha(t) e OCR...",
        "ocr_language_title": "Zgjidhni gjuhën(t) e OCR",
        "ocr_language_instruction": "Zgjidhni gjuhën(t) për njohjen e tekstit (OCR).\nKujdes: Gjuhët e shumta vijnë në kurriz të performancës dhe saktësisë!\nJu merrni rezultatet më të mira nëse zgjidhni vetëm një gjuhë.",
        "ocr_language_predefined": "Kombinime të paracaktuara",
        "ocr_language_custom": "E personalizuar...",
        "ocr_language_selected": "Gjuhët e zgjedhura të OCR",
        "ocr_language_changed": "Gjuha e OCR u ndryshua në {0}",
        "ocr_language_auto_detect": "Gjuhët e disponueshme zbulohen automatikisht.",
        "ocr_language_none_found": "Nuk u gjetën të dhëna të gjuhës Tesseract! Ju lutemi instaloni paketat e gjuhës (p.sh. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Përzgjedhje e personalizuar e gjuhës",
        "ocr_language_available": "Gjuhët e disponueshme (të instaluara):",
        "ocr_language_select_hint": "Zgjidhni një ose më shumë gjuhë:",
        "ocr_language_confirm": "Apliko",
        "ocr_language_reset": "Rivendos në parazgjedhje (deu+eng+vie)",
        "ocr_language_priorities": "Gjuhët e rekomanduara (të para-instaluara):",

        "select_all_languages": "Zgjidh të gjitha",
        "clear_all_languages": "Pastro përzgjedhjen",
        "install_language_packs": "Instalo paketat e gjuhës që mungojnë...",
        "install_hint": "💡 Këshillë: Jo të gjitha gjuhët janë të instaluara në sistemin tuaj. Përmes këtij butoni do të merrni ndihmë për instalimin.",
        "ocr_language_install_title": "Instalimi i paketave të gjuhës Tesseract",

        "ocr_missing_languages": "Paketat e gjuhës OCR që mungojnë",
        "ocr_missing_languages_message": "Gjuhët e mëposhtme të zgjedhura nuk janë të instaluara në sistemin tuaj:\n\n{0}\n\nJu lutemi instaloni paketat e gjuhës që mungojnë (shihni ndihmën nën 'Ndihmë instalimi').\n\nDëshironi të hapni ndihmën e instalimit tani?",
        "ocr_missing_languages_voice": "Paketat e gjuhës që mungojnë. Ju lutemi instaloni gjuhët që mungojnë.",
        "ocr_install_help_now": "Hap ndihmën",
        "ocr_continue_anyway": "Provo gjithsesi",
        "ocr_language_error_title": "Gabim i gjuhës OCR",
        "ocr_language_error_message": "Gabim gjatë njohjes së tekstit: {0}\n\nJu lutemi kontrolloni cilësimet e gjuhës OCR (Cilësimet → Gjuha OCR).",
        "ocr_install_help_button": "Ndihmë instalimi",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instaloni paketat e gjuhës Tesseract</p>

        <p>Që OCR të funksionojë në një gjuhë specifike, të dhënat përkatëse të gjuhës duhet të jenë të instaluara në sistemin tuaj. Ndiqni udhëzimet për sistemin tuaj operativ:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Hapni <strong>Terminalin</strong> (Finder → Programet → Mjetet → Terminal).</li>
        <li>Instaloni të gjitha gjuhët e disponueshme me:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Kjo mund të zgjasë disa minuta.)</li>
        <li>Ose vetëm gjuhë individuale (p.sh. vietnamisht):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Me versionet aktuale të Homebrew, mund të jetë e nevojshme të shkarkohet manualisht <code>*.traineddata</code> (shih më poshtë).</li>
        <li>Pas instalimit: Mbyllni këtë dialog dhe rihapni përzgjedhjen e gjuhës OCR – gjuhët e reja do të shfaqen automatikisht.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Hapni një terminal (Ctrl+Alt+T).</li>
        <li>Instaloni gjuhën e dëshiruar, p.sh. për vietnamisht:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Kodet e rëndësishme të gjuhëve: <code>deu</code> (gjermanisht), <code>eng</code> (anglisht), <code>vie</code> (vietnamisht), <code>spa</code> (spanjisht), <code>fra</code> (frëngjisht), <code>ita</code> (italisht), <code>nld</code> (holandisht), <code>fin</code> (finlandisht), <code>swe</code> (suedisht), <code>nor</code> (norvegjisht).</li>
        <li>Shfaq të gjitha paketat e disponueshme:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Shkarkoni skedarët e dëshiruar <code>*.traineddata</code> nga:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (p.sh. <code>vie.traineddata</code> për vietnamisht).</li>
        <li>Kopjoni skedarët në dosjen e gjuhëve të Tesseract, zakonisht:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Përshtateni sipas instalimit individual.)</li>
        <li>Rinisni aplikacionin (ose rihapni përzgjedhjen e gjuhës OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativë për të gjitha sistemet</p>
        <ul>
        <li>Instaloni <strong>OCRmyPDF</strong> dhe <strong>Tesseract</strong> me një menaxher paketash sipas zgjedhjes suaj. Shumica e instalimeve përmbajnë tashmë disa gjuhë standarde (anglisht, gjermanisht, frëngjisht).</li>
        <li>Gjuhët që mungojnë mund të instalohen në çdo kohë – përzgjedhja e gjuhës OCR liston vetëm gjuhët që ekzistojnë në të vërtetë.</li>
        </ul>

        <hr>
        <p><b>✅ Pas instalimit:</b> Nuk kërkohet rinisje e aplikacionit – gjuhët e sapo shtuara do të shfaqen menjëherë në listë.</p>
        <p><b>📖 Ndihmë për kodet e gjuhëve:</b> Një listë e plotë është e disponueshme në <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentacionin e Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Fontet Noto Sans",
        "info_noto_font_voice": "Udhëzues instalimi për fontet Noto Sans",
        "btn_info_noto_font_install": "Info fonti",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Si të instaloni fontet falas Noto nga Google</h2>

        <p><strong>Fontet Noto</strong> janë një familje fontesh me burim të hapur nga Google. Qëllimi i tyre është të mos shohin <em>"asnjë tofu"</em> (d.m.th. pa kuti boshe □) dhe të shfaqin saktë çdo karakter nga standardi Unicode. Ato janë shtesa ideale për aplikacionet që duhet të shfaqin tekste në shumë gjuhë të ndryshme.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalimi në macOS</h3>

        <p><strong>Metoda 1: Me Homebrew (për përdorues të avancuar)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metoda 2: Përmes "Font Book" (Rekomandohet)</strong></p>

        <ol>
        <li>Shkarkoni paketën zyrtare të fonteve:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Nxirreni skedarin ZIP</li>
        <li>Kopjoni skedarët në <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalimi në Windows (10 & 11)</h3>

        <p><strong>Metoda 1: Microsoft Store (Rekomandohet)</strong><br>
        Kërkoni për "Google Noto Fonts" ose "Noto Sans" dhe klikoni <strong>Instalo</strong>.</p>

        <p><strong>Metoda 2: Instalimi manual</strong></p>

        <ol>
        <li>Shkarkoni:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Nxirreni ZIP</li>
        <li>Zgjidhni skedarët .ttf / .otf</li>
        <li>Klikoni me të djathtën → <strong>Instalo</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        ose<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Emri\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalimi në Linux</h3>

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

        <p>Verifikimi:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Menaxho faqerojtësit",
        "bookmark_add": "Shto faqerojtës",
        "bookmark_add_tooltip": "Ruaj faqen aktuale si faqerojtës",
        "bookmark_remove": "Hiq faqerojtësin",
        "bookmark_remove_tooltip": "Fshij faqerojtësin e shënuar",
        "bookmark_remove_all": "Hiq të gjithë",
        "bookmark_remove_all_tooltip": "Fshij të gjithë faqerojtësit e këtij PDF",
        "bookmark_jump": "Kalo te faqerojtësi",
        "bookmark_jump_tooltip": "Kalo te faqja e zgjedhur",
        "bookmark_name": "Emri",
        "bookmark_page": "Faqja",
        "bookmark_no_bookmarks": "Nuk ka faqerojtës.\nKlikoni 'Shto' për të ruajtur faqen aktuale si faqerojtës.",
        "bookmark_added": "Faqerojtësi për faqen {0} u shtua: {1}",
        "bookmark_removed": "Faqerojtësi u hoq: {0}",
        "bookmark_all_removed": "Të gjithë faqerojtësit janë hequr.",
        "bookmark_name_default": "Faqja {0}",
        "bookmark_name_prompt": "Emri për faqerojtësin:\n(teksti i gjatë do të shkurtohet në 50 karaktere)",
        "bookmark_name_prompt_title": "Emri i faqerojtësit",
        "bookmark_confirm_remove_all": "Jeni i sigurt se dëshironi të hiqni të gjithë {0} faqerojtësit?",
        "menu_bookmarks": "Faqerojtës",
        "bookmark_manage": "Menaxho faqerojtësit",
        "bookmark_next": "Faqerojtësi tjetër",
        "bookmark_prev": "Faqerojtësi i mëparshëm",
        "bookmark_page_display": "Faqja {0}",
        "bookmark_exists": "Tashmë ekziston një faqerojtës për këtë faqe me këtë emër.",
        "bookmark_select_first": "Ju lutemi zgjidhni fillimisht një faqerojtës.",
        "bookmark_confirm_remove": "Jeni i sigurt se dëshironi të hiqni faqerojtësin 'Faqja {0}: {1}'?",
        "bookmark_jumped_to": "U kalua te faqerojtësi '{0}' në faqen {1}.",
        "bookmark_jumped_to_voice": "Faqerojtësi {0}, faqja {1}",
        "btn_close": "Mbyll",

        "bookmark_list": "Faqerojtësit tuaj",
        "bookmark_rename": "Riemërto faqerojtësin",
        "bookmark_rename_tooltip": "Ndrysho emrin e faqerojtësit të zgjedhur",
        "bookmark_rename_title": "Riemërto faqerojtësin",
        "bookmark_rename_prompt": "Emri i ri për faqerojtësin në faqen {0}:\n(maks. 50 karaktere)",
        "bookmark_renamed": "Faqerojtësi '{0}' u riemërua në '{1}'.",
        "bookmark_item_tooltip": "Faqja {0}: {1}\nKliko dy herë për të kaluar",
        "bookmark_name_exists_question": "Tashmë ekziston një faqerojtës me emrin '{0}' në këtë faqe.\nRiemërto gjithsesi?",

        "context_bookmarks": "Faqerojtës",
        "context_bookmark_add_here": "Shto faqerojtës për këtë faqe",
        "context_bookmarks_existing": "Faqerojtësit ekzistues:",
        "context_bookmarks_jump": "Kalo te faqerojtësi:",
        "context_bookmarks_none": "Nuk ka faqerojtës",
        "context_bookmarks_clear_all": "Hiq të gjithë {0} faqerojtësit",

        "bookmark_search_placeholder": "Kërko faqerojtës... (emri ose faqja)",
        "bookmark_search_results": "U gjetën %d faqerojtës për \"%s\"",
        "bookmark_no_search_results": "Nuk u gjetën faqerojtës për \"%s\"",
        "bookmark_no_search_results_label": "Nuk ka rezultate për \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Redakto metadata PDF",
        "metadata_title": "Titulli",
        "metadata_title_placeholder": "Titulli i dokumentit",
        "metadata_title_tooltip": "Titulli i dokumentit (shfaqet në shiritin e titullit)",
        "metadata_author": "Autori",
        "metadata_author_placeholder": "Emri i autorit",
        "metadata_author_tooltip": "Krijuesi i dokumentit",
        "metadata_subject": "Tema",
        "metadata_subject_placeholder": "Tema e dokumentit",
        "metadata_subject_tooltip": "Një përshkrim i shkurtër i përmbajtjes",
        "metadata_keywords": "Fjalët kyçe",
        "metadata_keywords_placeholder": "Fjalë kyçe të ndara me presje",
        "metadata_keywords_tooltip": "Fjalë kyçe për kategorizimin e dokumentit",
        "metadata_creator": "Krijuesi",
        "metadata_creator_placeholder": "Aplikacioni që krijoi PDF",
        "metadata_creator_tooltip": "Softueri me të cilin u krijua dokumenti",
        "metadata_producer": "Prodhuesi",
        "metadata_producer_placeholder": "Aplikacioni që konvertoi PDF",
        "metadata_producer_tooltip": "Softueri që konvertoi PDF",
        "metadata_creation_date": "Data e krijimit",
        "metadata_creation_date_tooltip": "Data e krijimit të dokumentit",
        "metadata_mod_date": "Data e modifikimit",
        "metadata_mod_date_tooltip": "Data e modifikimit të fundit",
        "metadata_pdf_info": "📄 Informacion PDF",
        "metadata_pages": "Numri i faqeve",
        "metadata_file_size": "Madhësia e skedarit",
        "metadata_pdf_version": "Versioni PDF",
        "metadata_encrypted": "I enkriptuar",
        "metadata_encrypted_yes": "Po (i mbrojtur me fjalëkalim)",
        "metadata_encrypted_no": "Jo",
        "metadata_reload": "📂 Ringarko nga PDF",
        "metadata_reset": "Hidhi poshtë ndryshimet",
        "metadata_reloaded": "Metadata u ringarkuan nga PDF.",
        "metadata_reset_done": "Të gjitha fushat e metadata u rivendosën.",
        "metadata_no_file": "Nuk është ngarkuar asnjë skedar PDF.",
        "metadata_save_error": "Gabim gjatë ruajtjes së metadata",
        "metadata_saved": "Metadata u ruajt me sukses.",
        "metadata_pdf_version_unknown": "PDF (i panjohur)",
        "metadata_saved_message": "Metadata u ruajt me sukses.",
        "metadata_saved_voice": "Metadata u ruajt.",

        "metadata_custom": "🔧 Metadata të personalizuara",
        "metadata_custom_placeholder": "{\n  \"fusha_ime\": \"vlera_ime\",\n  \"fusha_tjetër\": 123\n}",
        "metadata_custom_tooltip": "Formati JSON për metadata të personalizuara (opsionale)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "U zgjodh shablloni \"{0}\" - Kliko dy herë për të futur",
        "text_use_template": "Përdor bllok teksti",
        "text_type": "Lloji",
        "text_search_templates": "Kërko blloqe teksti...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informacion eksporti / importi",
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

        <h3>📦 Çfarë eksportohet? (Përmbledhje)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Cilësimet e përgjithshme të aplikacionit</span></li>
            <li class="detail">• Modaliteti i errët/i ndritshëm</li>
            <li class="detail">• Përmbysja e modalitetit të errët për imazhe</li>
            <li class="detail">• Vlera e pragut të grisë</li>
            <li class="detail">• Gjuha</li>
            <li class="detail">• Gjeometria e dritares</li>
            <li class="detail">• Modaliteti zmadhimit</li>
            <li class="detail">• Navigimi (Shiriti i navigimit i dukshëm)</li>
            <li class="detail">• Dalja e zërit (aktiv/joaktiv)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Cilësimet e rezervës</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Emërtimi i skedarëve (Vula kohore, Ndarësi, Prapashtesat)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Cilësimet për futjet e</span></li>
            <li class="detail">• Nënshkrimet</li>
            <li class="detail">• Teksti dhe blloqet e tekstit</li>
            <li class="detail">• Shenjat, imazhet dhe format</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Cilësimet e OCR</span></li>
            <li class="detail">• Gjuha</li>
            <li class="detail">• Detyro OCR · Modaliteti i faqes</li>
            <li class="detail">• Parapërpunimi i imazhit: Korrigjo animin, Pastro, Marrja e tepërt e mostrave</li>
            <li class="detail">• Numri i punëve paralele</li>
            <li class="detail">• Modaliteti i përmbysjes</li>
            <li class="detail">• Vlera e pragut të grisë</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Faqerojtësit</span></li>
            <li class="detail">• Të gjithë faqerojtësit për skedar PDF (Faqja, Emri, Koha e krijimit)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Baza e të dhënave të fjalëkalimeve</span></li>
            <li class="detail">• Fjalëkalimet e ruajtura të PDF (opsionalisht të enkriptuara ose tekst i thjeshtë)</li>
            <li class="detail">• Hash-i i fjalëkalimit master (nëse është vendosur)</li>
            <li class="detail">• Të dhënat e verifikimit</li>
        </ul>

        <h4>⚠️ Shënime të rëndësishme</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Gjatë importimit:</strong>
            <ul>
                <li><span class="warning">➜ TË GJITHA cilësimet aktuale do të mbishkruhen plotësisht</span></li>
                <li>• Rinisja e aplikacionit është e detyrueshme</li>
                <li>• Nënshkrimet, blloqet e tekstit dhe faqerojtësit ekzistues do të zëvendësohen</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Fjalëkalimi master dhe modaliteti i eksportit:</strong>
            <ul>
                <li>• Kur fjalëkalimi master është aktiv, ju mund të zgjidhni:</li>
                <li>  - <span style="color: #98FB98;"><strong>I dekriptuar</strong></span> (fjalëkalimet janë në tekst të thjeshtë në ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>I enkriptuar</strong></span> (i lexueshëm vetëm me fjalëkalimin master në sistemin e synuar)</li>
                <li>• Hash-i i fjalëkalimit master <strong>gjithmonë</strong> ruhet i enkriptuar</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Njoftim sigurie:</strong>
            <ul>
                <li>• Skedari ZIP i eksportuar përmban të dhëna të ndjeshme (<strong>fjalëkalime, faqerojtës, nënshkrime</strong>)</li>
                <li>• Ruajeni atë në një vend të sigurt (p.sh. USB i enkriptuar, menaxher fjalëkalimesh)</li>
                <li>• Nëse skedari humbet, fjalëkalimet e ruajtura të PDF humbasin në mënyrë të pakthyeshme</li>
            </ul>
        </div>

        <h4>📁 Formati i eksportit</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Cilësimet ruhen në një skedar të vetëm ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ky ZIP përmban <code>settings.json</code> të plotë (nga konfigurimi juaj) si dhe skedarët e mundshëm të imazheve të nënshkrimeve të ngulitura dhe fjalëkalimet e enkriptuara.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Nënshkrimet - Udhëzues",
        'signature_guide_html': """
        📝 <strong>Nënshkrimet - Udhëzues i shpejtë</strong><br>
        <ul>
        <li>Vendosni fjalëkalimin master</li>
        <li>Konfiguroni nënshkrimet në menunë <em>Cilësimet</em> (madhësia, vula kohore, …)</li>
        <li>Futni me <strong>KLIKIM TË DJATHTË</strong> në pozicionin e dëshiruar (fjalëkalimi master kërkohet një herë për seancë)</li>
        <li>Lëvizni nënshkrimin me miun ose tastet e shigjetave</li>
        <li>Futni disa nënshkrime njëri pas tjetrit</li>
        <li>Përshtatni çdo nënshkrim individualisht</li>
        <li>Hidhni poshtë një nënshkrim të vetëm</li>
        <li>Ruani / hidhni poshtë të gjithë nënshkrimet menjëherë</li>
        <li>Alternativisht, mund të përdoret edhe shiriti i menusë.</li>
        </ul>
        """,
        'signature_guide_voice': "Udhëzues i shpejtë për nënshkrimet. Vendosni fjalëkalimin master. Konfiguroni nënshkrimet në cilësime. Futni me klikim të djathtë.",

        'image_guide_title': "Futja e imazheve - Udhëzues",
        'image_guide_html': """
        📷 <strong>Futja e imazheve në PDF - Udhëzues i shpejtë</strong><br>
        <ol>
        <li>Klikimi i djathtë në pozicionin e dëshiruar</li>
        <li><em>„Fut imazh“</em> → Zgjidhni imazhin</li>
        <li>Poziciononi imazhin: Tërhiqeni me miun</li>
        <li>Rregulloni madhësinë: Tërhiqeni nga qoshet/skurte</li>
        <li>Ruani raportin e pamjes: Tasti <strong>[A]</strong></li>
        <li>Rregullime të mëtejshme: Klikimi i djathtë në imazh</li>
        </ol>
        <p><strong>Këshillë:</strong> Në menunë e kontekstit mund të rregulloni cilësimet.</p>
        """,
        'image_guide_voice': "Udhëzues i shpejtë për imazhet. Klikimi i djathtë, fut imazh, zgjidhni. Poziciononi me miun, rregulloni madhësinë në qoshe. Raporti i pamjes me tastin A.",

        'form_guide_title': "Futja e formave - Udhëzues",
        'form_guide_html': """
        📐 <strong>Futja e formave në PDF - Udhëzues i shpejtë</strong><br>
        <ol>
        <li>Zgjidhni llojin e formës (drejtkëndësh, elips, vijë, shigjetë)</li>
        <li>Klikoni në pozicion:
            <ul>
            <li>Për drejtkëndësh/elips: Një klikim vendos formën</li>
            <li>Për vijë/shigjetë: Dy klikime për pikën fillestare dhe përfundimtare</li>
            </ul>
        </li>
        <li>Poziciononi formën: Tërhiqeni me miun</li>
        <li>Rregulloni madhësinë: Tërhiqeni nga qoshet/skurte</li>
        <li>Ruani formën: <strong>Enter</strong></li>
        <li>Hidhni poshtë formën: <strong>ESC</strong></li>
        <li>Rregullime të mëtejshme: Klikimi i djathtë në formë</li>
        </ol>
        <p><strong>Këshillë:</strong> Në menunë e kontekstit mund të rregulloni cilësimet.</p>
        """,
        'form_guide_voice': "Udhëzues i shpejtë për format. Zgjidhni llojin e formës. Për drejtkëndësh ose elips klikoni një herë, për vijë ose shigjetë dy herë. Poziciononi me miun, rregulloni madhësinë në qoshe. Ruani me Enter, hidhni poshtë me Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "i mëparshmi",
        "btn_next_result": "tjetri",
        "ocr_text_window": "Dritarja e tekstit OCR",
        "bookmark_existing": "Faqerojtësit ekzistues",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Krahasimi OCR Mac - Windows",
        'ocr_method_mac_win_title': "Dallimet OCR midis Mac dhe Windows",
        'ocr_method_mac_win_voice': "Mac është më i mirë",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Dallimet midis macOS dhe Windows</strong></p>

        <p><strong>macOS (rekomandohet)</strong></p>
        <p>Mjeti:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Rezultati:</p>
        <ul>
        <li>Një PDF i kërkueshëm me tekst të integruar që ruan kryesisht paraqitjen origjinale.</li>
        </ul>
        <p>Përparësitë:</p>
        <ul>
        <li>Cilësi e shkëlqyer e njohjes së tekstit (edhe në faqe të shtrembëra).</li>
        <li>Ruajtja e grafikave vektoriale dhe fonteve.</li>
        <li>Shiriti i progresit GUI përmes vlerësimit të nënprocesit.</li>
        <li>Kontroll i plotë mbi të gjithë parametrat OCR (Deskew, Clean, Oversample, optimizimi).</li>
        <li>Kërkimi i tekstit është i disponueshëm direkt në dritaren kryesore (pamja PDF).</li>
        </ul>
        <p>Disavantazhet:</p>
        <ul>
        <li>Kërkon mjete shtesë të sistemit (ocrmypdf, Ghostscript, unpaper, pngquant – të përfshira në paketën e aplikacionit).</li>
        <li>Trajtimi më kompleks i gabimeve (bllokime, skadime kohe).</li>
        </ul>

        <p><strong>Windows (alternativë e qëndrueshme)</strong></p>
        <p>Mjeti:</p>
        <ul>
        <li>pytesseract (lidhje direkte me Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Rezultati:</p>
        <ul>
        <li>Një PDF i kërkueshëm që vizualisht korrespondon me një PDF imazhi, por është i kërkueshëm përmes tekstit transparent.</li>
        </ul>
        <p>Përparësitë:</p>
        <ul>
        <li>Asnjë nuk më vjen në mendje tani.</li>
        </ul>
        <p>Disavantazhet:</p>
        <ul>
        <li>PDF është në thelb një imazh me tekst të padukshëm; paraqitja mund të devijojë pak për dokumente komplekse (kolona, tabela).</li>
        <li>Asnjë korrigjim automatik i pjerrësisë (--deskew) ose pastrim i imazhit (--clean).</li>
        <li>Shiriti i progresit GUI përditësohet vetëm përafërsisht në bazë të numrit të faqeve të përpunuara.</li>
        <li>Shpejtësia e OCR është pak më e ngadaltë (sepse çdo faqe përpunohet veçmas).</li>
        <li>Kërkimi i tekstit ridrejtohet në dritaren e tekstit OCR.</li>
        </ul>

        <p><strong>Ngjashmëritë</strong></p>
        <ul>
        <li>Të dyja metodat krijojnë një PDF të kërkueshëm në të njëjtin drejtori me skedarin burimor.</li>
        <li>Cilësimet OCR (gjuha, DPI, mënyra e segmentimit të faqes, mënyra e motorit OCR) mund të konfigurohen përmes OCRSettingsDialog dhe vlejnë në të dyja zbatimet.</li>
        </ul>

        <p><strong>Rekomandimi:</strong></p>
        <ul>
        <li>macOS: Skedari binar ocrmypdf jep rezultatet më të mira – Bleni një Mac dhe përdorni versionin (PDFDarkView për Mac me çip Apple Silicon ose Intel). Rezultatet e OCR janë më të mira se në Windows!</li>
        <li>Windows: Përdorni zgjidhjen pytesseract. Është e qëndrueshme dhe siguron cilësi plotësisht të mjaftueshme për shumicën e dokumenteve.</li>
        </ul>

        <p><strong>Shënim i rëndësishëm:</strong></p>
        <ul>
        <li>Të dy versionet janë plotësisht të integruar në ndërfaqen e përdoruesit – përdoruesi nuk vëren asnjë ndryshim.</li>
        <li>Programi vendos automatikisht se cilin motor OCR të përdorë bazuar në sistemin operativ.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Krijo nënshkrim (nga skanimi)",
        "signature_create_title": "Zgjidhni nënshkrimin e skanuar (PDF/imazh)",
        "image_pdf_filter": "Imazhet dhe PDF",
        "signature_pdf_empty": "PDF nuk përmban faqe.",
        "signature_created_success": "Nënshkrimi u krijua me sukses: {0}",
        "signature_create_error": "Gabim gjatë krijimit të nënshkrimit:\n{0}",
        "rembg_missing": "rembg nuk është i instaluar.\nJu lutemi instaloni: pip install rembg\nGabim: {0}",
        "signature_name_title": "Emri i skedarit për nënshkrimin",
        "signature_name_message": "Ju lutemi vendosni një emër skedari për nënshkrimin e ri (do të ruhet si PNG me sfond transparent):",
        "signature_name_label": "Emri i skedarit:",
        "signature_name_voice": "Vendosni emrin e skedarit për nënshkrimin",
        "signature_processing": "Përpunimi në vazhdim...",
        "signature_creation_title": "Po krijohet nënshkrimi",
        "signature_overwrite_warning": "Skedari '{0}' tashmë ekziston. Të mbishkruhet?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Përgatitni PDF për nënshkrim",
        "signature_prepare_instruction":"Ju lutemi zgjidhni një PDF që përmban në një faqe të vetme një nënshkrim të skanuar.\n\nPër njohje optimale, sigurohuni që:\n• Nënshkrimi të jetë shkruar me bojë të zezë (stilolaps topi ose fineliner) në letër të bardhë.\n• Nënshkrimi të jetë në të tretën e sipërme të një faqeje A4 përndryshe të zbrazët.\n• PDF të jetë skanuar me të paktën 300 dpi.\n• Nënshkrimi të jetë i qartë dhe jo shumë i hollë.\n• Të mos ketë modele sfondi ose vija shqetësuese.",
        "signature_prepare_voice":"Ju lutemi zgjidhni një PDF me një nënshkrim të skanuar. Kushtojini vëmendje cilësisë së mirë dhe kontrastit.",
        "sig_thickness_label":"Trashësia e vijës:",
        "sig_thickness_normal":"Normale (e hollë)",
        "sig_thickness_bold":"E trashë (rekomandohet)",
        "sig_thickness_very_bold":"Shumë e trashë",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Shtimi i gjuhëve GUI dhe OCR - Udhëzues",
        'language_guide_title': "Shtimi i gjuhëve GUI dhe OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Shkarkoni skedarin e dëshiruar të përkthimit <code>translations_xy.py</code> nga<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        dhe vendoseni në drejtorinë e mëposhtme:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Hapni shfletuesin tuaj të internetit.</li>
        <li>Shkoni te: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Në skajin e djathtë të ekranit kërkoni "Releases" dhe zgjidhni atë të shënuar me <strong>"latest"</strong>.</li>
        <li>Në faqen tjetër të lëshimit, shkarkoni skedarin <code>Source Code.zip</code> në fund.</li>
        <li>Shpaketoni skedarin ZIP.</li>
        <li>Në dosjen e shpaketuar gjeni të gjithë skedarët e gjuhës që ju nevojiten dhe kopjoni ato në drejtori:<br/>
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
        "menu_watermark":"Fut shenjë uji",
        "fullpage_text_watermark_title":"Tekst si shenjë uji",
        "fullpage_image_watermark_title":"Imazh si shenjë uji",
        "filename_with_watermark":"_me_shenje_uji",
        "watermark_text":"Tekst:",
        "watermark_text_placeholder":"Teksti juaj i shenjës së ujit...",
        "watermark_font_family":"Fonti:",
        "watermark_font_size":"Madhësia e fontit:",
        "watermark_format":"Formatimi:",
        "watermark_bold":"Trashë",
        "watermark_italic":"Pjerrët",
        "watermark_color":"Ngjyra:",
        "watermark_choose_color":"Zgjidh ngjyrën...",
        "watermark_opacity":"Errësirë / Transparencë:",
        "watermark_direction":"Drejtimi i leximit:",
        "watermark_direction_l_r":"Majtas → Djathtas",
        "watermark_direction_bl_tr":"Poshtë majtas → Lart djathtas",
        "watermark_direction_tl_br":"Lart majtas → Poshtë",
        "watermark_direction_b_t":"Poshtë → Lart",
        "watermark_direction_t_b":"Lart → Poshtë",
        "watermark_preview":"Paraparje:",
        "watermark_preview_sample":"Tekst shembull",
        "watermark_empty_text":"Ju lutemi vendosni tekst.",
        "watermark_applied":"Shenja e ujit është aplikuar në të gjitha faqet.",
        "watermark_saved":"Shenja e ujit u ruajt.",
        "image_scale":"Madhësia:",
        "image_preview":"Paraparje e imazhit:",
        "no_image_selected":"Asnjë imazh i përzgjedhur",
        "browse":"Shfleto...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redaktimet",
        "redact_add_black": "Redaktim (i zi)",
        "redact_add_white": "Redaktim (i bardhë / fshij)",
        "redact_added_black": "U shtua redaktim i zi",
        "redact_added_white": "U shtua redaktim i bardhë",
        "redact_apply_all": "Apliko të gjitha redaktimet dhe ruaj",
        "redact_discard_all": "Hidhi poshtë të gjitha redaktimet",
        "redact_discard": "Hidhe poshtë këtë redaktim",
        "no_redactions": "Nuk ka redaktime",
        "redact_confirm_title": "Apliko redaktimet përgjithmonë",
        "redact_confirm_message": "Paralajmërim: Zonat e shënuara do të fshihen përgjithmonë (të zeza ose të bardha).\nDo të krijohet një kopje rezervë (nëse është aktivizuar).\n\nTë vazhdohet?",
        "redact_apply": "Po, redakto tani",
        "redact_saved": "{0} redaktim(e) u aplikua(n) dhe u ruajt(ën) me sukses.",
        "redact_saved_voice": "{0} redaktim(e) u aplikua(n)",
        "redact_error": "Gabim gjatë redaktimit",
        "filename_redacted":"_redaktuar",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Fut numrat e faqeve',
        'page_numbers_format': 'Formati i numrit:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabik)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romak i vogël)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romak i madh)',
        'page_numbers_format_letter': 'A, B, C ... (shkronja)',
        'page_numbers_format_custom': 'I personalizuar',
        'page_numbers_custom_pattern': 'Modeli:',
        'page_numbers_custom_placeholder': 'p.sh. "Faqja {nummer}" ose "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Përdorni {nummer} për numrin aktual të faqes dhe {total} për numrin total',
        'page_numbers_position': 'Pozicioni:',
        'page_numbers_pos_tl': 'Lart majtas',
        'page_numbers_pos_tc': 'Lart në qendër',
        'page_numbers_pos_tr': 'Lart djathtas',
        'page_numbers_pos_ml': 'Në mes majtas',
        'page_numbers_pos_mc': 'Në qendër',
        'page_numbers_pos_mr': 'Në mes djathtas',
        'page_numbers_pos_bl': 'Poshtë majtas',
        'page_numbers_pos_bc': 'Poshtë në qendër',
        'page_numbers_pos_br': 'Poshtë djathtas',
        'page_numbers_margins': 'Margjinat:',
        'page_numbers_margin_x': 'Distanca horizontale:',
        'page_numbers_margin_y': 'Distanca vertikale:',
        'page_numbers_range': 'Gama e faqeve:',
        'page_numbers_all_pages': 'Të gjitha faqet',
        'page_numbers_custom_range': 'Gamë e personalizuar',
        'page_numbers_from': 'Nga:',
        'page_numbers_to': 'Deri:',
        'page_numbers_progress': 'Po futen numrat e faqeve...',
        'page_numbers_start': 'Po fillohet futja e numrave të faqeve...',
        'page_numbers_cancel': 'Futja e numrave të faqeve u anulua',
        'page_numbers_success': 'Numrat e faqeve u shtuan me sukses.\n\nDëshironi të hapni PDF-në e re?\n\n{0}',
        'page_numbers_complete': 'Numrat e faqeve u shtuan',
        'page_numbers_error_format': 'Gabim gjatë futjes së numrave të faqeve: {0}',
        'page_numbers_content_type': 'Lloji i përmbajtjes:',
        'page_numbers_tab_simple': 'Numër i thjeshtë',
        'page_numbers_tab_range': 'Faqja X nga Y',
        'page_numbers_tab_date': 'Data',
        'page_numbers_tab_custom': 'Tekst i lirë',
        'page_numbers_range_format': 'Formati:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Faqja {aktuell} nga {gesamt}',
        'page_numbers_range_custom': 'I personalizuar',
        'page_numbers_range_placeholder': 'p.sh. "Faqja {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Formati i datës:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 janar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'I personalizuar',
        'page_numbers_date_placeholder': 'p.sh. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Pozicioni:',
        'page_numbers_date_before': 'Data para numrit të faqes',
        'page_numbers_date_after': 'Data pas numrit të faqes',
        'page_numbers_date_only': 'Vetëm data (pa numër faqe)',
        'page_numbers_custom_text': 'Tekst i personalizuar:',
        'page_numbers_custom_placeholder_text': 'Përdorni {seite} për numrin e faqes dhe {gesamt} për totalin\np.sh. "Konfidencial - Faqja {seite}" ose "{seite} nga {gesamt}"',
        "filename_with_page_number":"_me_numrin_e_faqes",
        "filename_with_page_declaration":"_me_deklaraten_e_faqes",
        "filename_with_pagenumber":"_me_numrin_e_faqes",
        "filename_with_date":"_me_daten",
        "filename_with_my_page_declaration":"_me_deklaraten_e_personalizuar",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Ndryshime të paruajtura",
        "unsaved_changes_message_darkmode": "Ka futje të paruajtura.\nDëshironi t'i ruani para se të kaloni?",
        "save_and_switch": "Ruaj dhe kalo",
        "discard_and_switch": "Kalo tani",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Eksporto faqet si imazhe',
        'export_images_menu': 'Eksporto si imazhe (PNG/JPEG)',
        'export_images_format': 'Formati i imazhit:',
        'export_images_dpi': 'Rezolucioni (DPI):',
        'export_images_quality': 'Cilësia JPEG:',
        'export_images_range': 'Gama e faqeve:',
        'export_images_all_pages': 'Të gjitha faqet',
        'export_images_custom_range': 'Gamë e personalizuar',
        'export_images_from': 'Nga:',
        'export_images_to': 'Deri:',
        'export_images_options': 'Opsionet:',
        'export_images_single_files': 'Çdo faqe si skedar i veçantë',
        'export_images_subfolder': 'Eksporto në nëndosje',
        'export_images_subfolder_info': 'Në nëndosjen "emriPDF_imazhe"',
        'export_images_same_folder': 'Në të njëjtën dosje me PDF-në',
        'export_images_apply_darkmode': 'Apliko cilësimet e PDFDarkView (Modaliteti i errët)',
        'export_images_target_folder': 'Dosja e destinacionit:',
        'export_images_browse': 'Shfleto...',
        'export_images_preview': 'Paraparje:',
        'export_images_preview_info': 'Zgjidhni cilësimet për eksport',
        'export_images_preview_info_detail': '{0} faqe si {1}\nRezolucioni: {2} DPI\nEmri i skedarit: {3}\n{4}',
        'export_images_select_folder': 'Zgjidhni dosjen e destinacionit',
        'export_images_start': 'Po fillohet eksporti i imazheve...',
        'export_images_progress': 'Po eksportohen imazhet...',
        'export_images_saving': 'Po ruhet faqja {0} nga {1}...',
        'export_images_success': 'Eksporti u krye me sukses!\n\n{0} imazhe u ruajtën në:\n{1}',
        'export_images_complete': 'Eksporti i imazheve u përfundua',
        'export_images_open_folder': '📁 Hap dosjen',
        'export_images_cancel': 'Eksporti i imazheve u anulua',
        'export_images_error_format': 'Gabim gjatë eksportimit të imazheve: {0}',
        'export_images_pdf2image_missing': 'Biblioteka "pdf2image" nuk është e instaluar.\n\nJu lutemi instalojeni me:\npip install pdf2image\n\nPër Windows ju duhet gjithashtu Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Konvertimi PDF/A për arkivim afatgjatë',
        'pdfa_menu': 'Konvertimi PDF/A (i përshtatshëm për arkiv)',
        'pdfa_info': 'Konverton PDF-në në format PDF/A.\n\nPDF/A është projektuar posaçërisht për arkivim afatgjatë dhe siguron që dokumenti të shfaqet saktë në të ardhmen.',
        'pdfa_standard': 'Standardi PDF/A:',
        'pdfa_standard_select': 'Versioni:',
        'pdfa_1': 'PDF/A-1 (i thjeshtë, i pajtueshëm gjerësisht)',
        'pdfa_2': 'PDF/A-2 (modern, kompresim më i mirë)',
        'pdfa_3': 'PDF/A-3 (versioni më i ri, lejon bashkëngjitjet)',
        'pdfa_standards_explanation': '📖 Shpjegimi i standardeve:\n\n'
            '• PDF/A-1: Bazë, i pajtueshëm me sistemet e vjetra (rreth 2005)\n'
            '• PDF/A-2: Më modern, kompresim më i mirë, mbështetje për transparencë (rreth 2011)\n'
            '• PDF/A-3: Versioni më i ri, lejon futjen e bashkëngjitjeve (rreth 2013)\n\n'
            'Rekomandim: PDF/A-2 është një kompromis i mirë midis pajtueshmërisë dhe funksioneve moderne.',
        'pdfa_options': 'Opsionet:',
        'pdfa_compress_enable': 'Kompreso PDF (skedar më i vogël)',
        'pdfa_metadata_preserve': 'Ruaj metadatat (titulli, autori, etj.)',
        'pdfa_target_folder': 'Dosja e destinacionit:',
        'pdfa_browse': 'Shfleto...',
        'pdfa_select_folder': 'Zgjidhni dosjen e destinacionit',
        'pdfa_ocr_info_unknown': '🔍 Nuk mund të kontrollohej përmbajtja e tekstit.',
        'pdfa_ocr_info_not_needed': '✅ Teksti i disponueshëm - OCR nuk kërkohet.\nPDF/A mund të krijohet direkt.',
        'pdfa_ocr_info_recommended': '⚠️ Nuk u gjet tekst i mjaftueshëm.\n\nPër PDF të kërkueshme, rekomandojmë të ekzekutoni fillimisht OCR.\nShënim: PDF/A funksionon edhe pa OCR - por teksti nuk do të jetë i kërkueshëm.',
        'pdfa_ocr_info_error': '❌ Gabim gjatë kontrollit: {0}',
        'pdfa_start': 'Po fillohet konvertimi PDF/A...',
        'pdfa_progress': 'Konvertimi PDF/A në vazhdim...',
        'pdfa_success': 'Konvertimi PDF/A u krye me sukses!\n\nU ruajt si:\n{0}\n\nDëshironi të hapni PDF-në e re?',
        'pdfa_complete': 'Konvertimi PDF/A u përfundua',
        'pdfa_cancel': 'Konvertimi PDF/A u anulua',
        'pdfa_error_format': 'Gabim gjatë konvertimit PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Biblioteka "ocrmypdf" nuk është e instaluar.\n\nJu lutemi instalojeni me:\npip install ocrmypdf',
        'btn_convert': 'Konverto',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimizo PDF (zvogëlo madhësinë e skedarit)',
        'optimize_menu': 'Optimizo PDF (madhësia e skedarit)',
        'optimize_info': 'Zvogëlon madhësinë e skedarit PDF përmes metodave të ndryshme të optimizimit.\n\nSa më i lartë niveli i kompresimit, aq më i vogël bëhet skedari - me humbje të mundshme të cilësisë në imazhe.',
        'optimize_level': 'Niveli i kompresimit:',
        'optimize_level_low': 'I ulët (i shpejtë, kursim i vogël)',
        'optimize_level_medium': 'I mesëm (kompromis i mirë)',
        'optimize_level_high': 'I lartë (kursim i madh)',
        'optimize_level_maximum': 'Maksimal (kursim maksimal, i ngadaltë)',
        'optimize_level_explanation': 'Rekomandim: "I mesëm" është një kompromis i mirë midis shpejtësisë dhe madhësisë së skedarit.',
        'optimize_options': 'Opsionet:',
        'optimize_compress_images': 'Kompreso imazhet (zvogëlo cilësinë JPEG)',
        'optimize_clean_objects': 'Hiq objektet e papërdorura',
        'optimize_preserve_metadata': 'Ruaj metadatat (titulli, autori, etj.)',
        'optimize_image_quality': 'Cilësia e imazhit:',
        'optimize_range': 'Gama e faqeve:',
        'optimize_all_pages': 'Të gjitha faqet',
        'optimize_custom_range': 'Gamë e personalizuar',
        'optimize_from': 'Nga:',
        'optimize_to': 'Deri:',
        'optimize_target_folder': 'Dosja e destinacionit:',
        'optimize_browse': 'Shfleto...',
        'optimize_select_folder': 'Zgjidhni dosjen e destinacionit',
        'optimize_info_box': 'Informacion',
        'optimize_info_text': 'Optimizimi mund të zgjasë disa minuta për PDF të mëdha.\n\nImazhet ruhen me cilësi të reduktuar, gjë që mund të zvogëlojë ndjeshëm madhësinë e skedarit.',
        'optimize_start': 'Po fillohet optimizimi i PDF...',
        'optimize_progress': 'Po optimizohet PDF...',
        'optimize_cancel': 'Optimizimi i PDF u anulua',
        'optimize_complete': 'Optimizimi i PDF u përfundua',
        'optimize_error_format': 'Gabim gjatë optimizimit të PDF:\n\n{0}',
        'optimize_success_message': 'Optimizimi i PDF u krye me sukses!\n\nU ruajt si:\n{0}\n\nPara: {1}\nPas: {2}\nKursimi: {3:.1f}%\n\n{4}\n\nDëshironi të hapni PDF-në e optimizuar?',
        'optimize_success_message_no_size': 'Optimizimi i PDF u krye me sukses!\n\nU ruajt si:\n{0}\n\nInformacioni i madhësisë nuk është i disponueshëm.\n\nDëshironi të hapni PDF-në e optimizuar?',
        'optimize_result_positive': 'Skedari u zvogëlua me {0:.1f}%.',
        'optimize_result_zero': 'Asnjë ndryshim në madhësinë e skedarit.',
        'optimize_result_negative': 'Skedari u rrit me {0:.1f}%.\nOptimizimi u anashkalua, skedari origjinal u ruajt.',
        'btn_optimize': 'Fillo optimizimin',
        'filename_optimize_low_suffix': '_optimizuar_i_ulet',
        'filename_optimize_medium_suffix': '_optimizuar',
        'filename_optimize_high_suffix': '_optimizuar_i_larte',
        'filename_optimize_maximum_suffix': '_optimizuar_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Prit PDF',
        'crop_menu': 'Prit PDF (Crop)',
        'crop_range': 'Apliko në:',
        'crop_all_pages': 'Të gjitha faqet',
        'crop_current_page': 'Vetëm faqja aktuale',
        'crop_values': 'Vlerat e prerjes (në pikë):',
        'crop_left': 'Majtas:',
        'crop_right': 'Djathtas:',
        'crop_top': 'Lart:',
        'crop_bottom': 'Poshtë:',
        'crop_presets': 'Paracaktime:',
        'crop_preset_white': 'Zbuloni margjinat e bardha',
        'crop_reset': 'Rivendos',
        'crop_mouse_hint': '🖱️ Tërhiqni një drejtkëndësh për të zgjedhur përafërsisht zonën.\nMë pas mund të rregulloni vlerat me saktësi në SpinBox.\nRregullimi manual me miun nuk është i mundur.',
        'crop_apply': 'Prit',
        'crop_scope_all': 'Të gjitha faqet',
        'crop_scope_current': 'Faqja aktuale',
        'crop_new_size': 'Madhësia e re: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Asnjë PDF e ngarkuar',
        'crop_preview_error': 'Gabim gjatë ngarkimit të paraparjes',
        'crop_start': 'Po fillohet prerja...',
        'crop_progress': 'Po pritet PDF...',
        'crop_success': 'PDF u pre me sukses!\n\nU ruajt si:\n{0}\n\nDëshironi të hapni PDF-në e prerë?',
        'crop_complete': 'Prerja u përfundua',
        'crop_cancel': 'Prerja u anulua',
        'crop_error_format': 'Gabim gjatë prerjes:\n\n{0}',
        'filename_crop_suffix': '_prerë',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Rrafsho PDF (Flatten)',
        'flatten_menu': 'Rrafsho PDF (Flatten)',
        'flatten_info': 'Rrafshimi i një PDF "djeg" të gjithë elementët e redaktueshëm në përmbajtjen e faqes.\n\nPas kësaj, fushat e formularit, shënimet, tekstet, kryqet, nënshkrimet, imazhet dhe format nuk janë më të redaktueshme individualisht.',
        'flatten_explanation_title': '📖 Për çfarë është i mirë ky?',
        'flatten_explanation_text': 'Rrafshimi është i nevojshëm në situatat e mëposhtme:\n\n'
            '• 📄 Dëshironi të përgatisni dokumentin për printim\n'
            '• 🔒 Dëshironi të parandaloni që dikush të ndryshojë fushat e formularit\n'
            '• 📎 Dëshironi të "fusni" përgjithmonë shënimet dhe komentet në dokument\n'
            '• 🖼️ Dëshironi të ankoni përgjithmonë tekstet, kryqet, nënshkrimet, imazhet dhe format në dokument\n'
            '• 📦 Dëshironi të përgatisni skedarin për arkivim\n\n'
            'Rrafshimi e bën PDF-në më të vogël dhe parandalon lëvizjen ose fshirjen aksidentale të elementeve.',
        'flatten_what_title': 'Çfarë rrafshohet?',
        'flatten_what_list': '• ✅ Fushat e formularit (fushat e tekstit, kutitë e kontrollit, butonat)\n'
            '• ✅ Shënimet (komentet, theksimet, shënimet)\n'
            '• ✅ Shtresat (tekstet, kryqet, nënshkrimet, imazhet, format)',
        'flatten_options': 'Opsionet:',
        'flatten_forms': 'Rrafsho fushat e formularit',
        'flatten_annotations': 'Rrafsho shënimet',
        'flatten_overlays': 'Rrafsho shtresat (tekstet, kryqet, nënshkrimet, imazhet, format)',
        'flatten_target_folder': 'Dosja e destinacionit:',
        'flatten_browse': 'Shfleto...',
        'flatten_select_folder': 'Zgjidhni dosjen e destinacionit',
        'flatten_warning': '⚠️ E rëndësishme: Rrafshimi është një proces i pakthyeshëm!\n\nPas rrafshimit, elementët e redaktueshëm nuk mund të ndryshohen ose fshihen më individualisht.\nKrijoni një kopje rezervë paraprakisht nëse është e nevojshme.',
        'flatten_apply': 'Rrafsho',
        'flatten_start': 'Po fillohet rrafshimi...',
        'flatten_progress': 'Po rrafshohet PDF...',
        'flatten_success': 'PDF u rrafshua me sukses!\n\nU ruajt si:\n{0}\n\nDëshironi të hapni PDF-në e rrafshuar?',
        'flatten_complete': 'Rrafshimi u përfundua',
        'flatten_cancel': 'Rrafshimi u anulua',
        'flatten_error_format': 'Gabim gjatë rrafshimit:\n\n{0}',
        'filename_flatten_suffix': '_rrafshuar',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Shtresa PDF (Overlay)',
        'overlay_menu': 'Shtresa PDF (Overlay)',
        'overlay_info': 'Vendos një PDF (shtresë) mbi një PDF tjetër.\n\nPDF shtresë vendoset mbi PDF bazë. Kjo është e dobishme për shenjat e ujit, logot, letrat me kokë ose vulat.',
        'overlay_explanation_title': '📖 Për çfarë është i mirë ky?',
        'overlay_explanation_text': 'Shtresa është e nevojshme në situatat e mëposhtme:\n\n'
            '• 🏢 Vendosja e logos së kompanisë si shenjë uji në çdo faqe\n'
            '• 📄 Vendosja e letrës me kokë në një PDF bosh\n'
            '• 🖊️ Vendosja e shtresës së vulës në një dokument\n'
            '• 🔖 Vendosja e shenjës së ujit në të gjitha faqet\n'
            '• 📑 Vendosja e shtresës së formularit në një shabllon',
        'overlay_type': 'Lloji i shtresës:',
        'overlay_type_fullpage': 'Faqe e plotë (mbuluese)',
        'overlay_type_transparent': 'Faqe e plotë (transparente - e rekomanduar)',
        'overlay_type_stamp': 'Vulë (e pozicionueshme)',
        'overlay_type_info_fullpage': '📄 PDF shtresë vendoset saktësisht mbi të gjithë faqen.\nSfondi i bardhë mund të hiqet në mënyrë që vetëm përmbajtja të mbetet e dukshme.',
        'overlay_type_info_transparent': '🔍 PDF shtresë vendoset mbi të gjithë faqen me sfond transparent.\nSfondi i bardhë hiqet automatikisht - ideale për shenjat e ujit dhe logot!',
        'overlay_type_info_stamp': '🖊️ PDF shtresë pozicionohet dhe shkallëzohet si vulë.\nE përkryer për logo, vula ose nënshkrime në pozicione specifike.',
        'overlay_remove_background': 'Hiq sfondin e bardhë:',
        'overlay_remove_background_enable': 'Hiq sfondin e bardhë nga PDF shtresë (e bën shtresën transparente)',
        'overlay_remove_background_tooltip': 'Heq zonat e bardha nga PDF shtresë në mënyrë që teksti poshtë të bëhet i dukshëm.',
        'overlay_threshold': 'Vlera e pragut:',
        'overlay_threshold_hint': '(1-254, më e lartë = më shumë e bardhë hiqet)',
        'overlay_select_file': 'Zgjidhni PDF shtresë:',
        'overlay_file_placeholder': 'Ju lutemi zgjidhni një skedar PDF për shtresën',
        'overlay_browse': 'Shfleto...',
        'overlay_select_overlay': 'Zgjidhni PDF shtresë',
        'overlay_range': 'Gama e faqeve:',
        'overlay_all_pages': 'Të gjitha faqet',
        'overlay_custom_range': 'Gamë e personalizuar',
        'overlay_from': 'Nga:',
        'overlay_to': 'Deri:',
        'overlay_position': 'Pozicioni:',
        'overlay_position_center': 'Qendër',
        'overlay_position_top_left': 'Lart majtas',
        'overlay_position_top_right': 'Lart djathtas',
        'overlay_position_bottom_left': 'Poshtë majtas',
        'overlay_position_bottom_right': 'Poshtë djathtas',
        'overlay_size': 'Madhësia:',
        'overlay_size_original': 'Madhësia origjinale',
        'overlay_size_fit_page': 'Përshtat në faqe',
        'overlay_size_custom': 'I personalizuar (%)',
        'overlay_opacity': 'Transparenca:',
        'overlay_target_folder': 'Dosja e destinacionit:',
        'overlay_browse_folder': 'Shfleto...',
        'overlay_select_folder': 'Zgjidhni dosjen e destinacionit',
        'overlay_warning': '⚠️ Shënim: PDF shtresë vendoset mbi PDF bazë dhe "digjet" në të.\n\nElementet e PDF shtresë nuk mund të redaktohen më individualisht pas ruajtjes.',
        'overlay_apply': 'Shtresë',
        'overlay_start': 'Po fillohet shtresa...',
        'overlay_progress': 'Po shtresohet PDF...',
        'overlay_success': 'PDF u shtresua me sukses!\n\nU ruajt si:\n{0}\n\nDëshironi të hapni PDF-në e shtresuar?',
        'overlay_complete': 'Shtresa u përfundua',
        'overlay_cancel': 'Shtresa u anulua',
        'overlay_error_format': 'Gabim gjatë shtresimit:\n\n{0}',
        'overlay_no_file': 'Asnjë PDF shtresë e përzgjedhur.\n\nJu lutemi zgjidhni një skedar PDF për shtresim.',
        'filename_overlay_suffix': '_shtresuar',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Nxjerr imazhet nga PDF',
        'extract_images_menu': 'Nxjerr të gjitha imazhet',
        'extract_images_info': 'Nxjerr të gjitha imazhet nga PDF dhe i ruan si skedarë të veçantë.\n\nImazhet ruhen në formatin e tyre origjinal ose konvertohen në një format të zgjedhur.',
        'extract_images_format': 'Formati i imazhit:',
        'extract_images_quality': 'Cilësia JPEG:',
        'extract_images_options': 'Opsionet:',
        'extract_images_subfolder': 'Nxjerr në nëndosje ("emriPDF_imazhe")',
        'extract_images_unique': 'Vetëm imazhe unike (shmang dublikatat)',
        'extract_images_range': 'Gama e faqeve:',
        'extract_images_all_pages': 'Të gjitha faqet',
        'extract_images_custom_range': 'Gamë e personalizuar',
        'extract_images_from': 'Nga:',
        'extract_images_to': 'Deri:',
        'extract_images_target_folder': 'Dosja e destinacionit:',
        'extract_images_browse': 'Shfleto...',
        'extract_images_select_folder': 'Zgjidhni dosjen e destinacionit',
        'extract_images_info_box': 'Informacion',
        'extract_images_info_text': 'Nxjerrja mund të zgjasë disa minuta për PDF të mëdha.\n\nImazhet ruhen me emrin e tyre origjinal (faqja_imazh).',
        'extract_images_extract': 'Nxjerr',
        'extract_images_start': 'Po fillohet nxjerrja...',
        'extract_images_progress': 'Po nxirren imazhet...',
        'extract_images_success': '✅ Imazhet u nxorrën me sukses!\n\n{0} imazhe u ruajtën në:\n{1}',
        'extract_images_complete': 'Nxjerrja e imazheve u përfundua',
        'extract_images_cancel': 'Nxjerrja u anulua',
        'extract_images_error_format': 'Gabim gjatë nxjerrjes së imazheve:\n\n{0}',
        'extract_images_open_folder': '📁 Hap dosjen',
        'extract_images_no_images': 'Nuk u gjetën imazhe në PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Faqe të shumta në një faqe (N-Up)',
        'nup_menu': 'Faqe të shumta në një faqe (N-Up)',
        'nup_info': 'Rregullon faqe të shumta PDF në një faqe.\n\nIdeale për printime kompakte, përmbledhje ose fletushka.',
        'nup_layout': 'Paraqitja:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Paraparje:',
        'nup_preview_info': '{0} faqe → {1} faqe për fletë → {2} fletë\nParaqitja: {3}',
        'nup_order': 'Renditja:',
        'nup_order_horizontal': 'Horizontale (rresht pas rreshti)',
        'nup_order_vertical': 'Vertikale (kolonë pas kolone)',
        'nup_order_horizontal_reverse': 'Horizontale e kundërt',
        'nup_order_vertical_reverse': 'Vertikale e kundërt',
        'nup_range': 'Gama e faqeve:',
        'nup_all_pages': 'Të gjitha faqet',
        'nup_custom_range': 'Gamë e personalizuar',
        'nup_from': 'Nga:',
        'nup_to': 'Deri:',
        'nup_options': 'Opsionet:',
        'nup_margins': 'Margjinat:',
        'nup_margin_between': 'Hapësira midis faqeve:',
        'nup_page_numbers': 'Fut numrat e faqeve',
        'nup_target_folder': 'Dosja e destinacionit:',
        'nup_browse': 'Shfleto...',
        'nup_select_folder': 'Zgjidhni dosjen e destinacionit',
        'nup_create': 'Krijo',
        'nup_start': 'Po fillohet N-Up...',
        'nup_progress': 'Po krijohet N-Up...',
        'nup_success': 'N-Up u krijua me sukses!\n\nU ruajt si:\n{0}\n\nDëshironi të hapni PDF-në e re?',
        'nup_complete': 'N-Up u përfundua',
        'nup_cancel': 'N-Up u anulua',
        'nup_error_format': 'Gabim gjatë N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Ndrysho madhësinë e faqes',
        'pagesize_menu': 'Ndrysho madhësinë e faqes',
        'pagesize_info': 'Ndryshon madhësinë e faqes së PDF.\n\nPërmbajtja përshtatet automatikisht me madhësinë e re.',
        'pagesize_format': 'Formati:',
        'pagesize_select': 'Zgjidhni një format standard:',
        'pagesize_custom': 'Madhësi e personalizuar:',
        'pagesize_width': 'Gjerësia:',
        'pagesize_height': 'Lartësia:',
        'pagesize_orientation': 'Orientimi:',
        'pagesize_portrait': 'Portret',
        'pagesize_landscape': 'Peizazh',
        'pagesize_scale_options': 'Opsionet e shkallëzimit:',
        'pagesize_fit': 'Përshtat (ruaj raportin e aspektit)',
        'pagesize_stretch': 'Shtri (shtrembëro)',
        'pagesize_center': 'Qendër (madhësia origjinale)',
        'pagesize_range': 'Gama e faqeve:',
        'pagesize_all_pages': 'Të gjitha faqet',
        'pagesize_custom_range': 'Gamë e personalizuar',
        'pagesize_from': 'Nga:',
        'pagesize_to': 'Deri:',
        'pagesize_target_folder': 'Dosja e destinacionit:',
        'pagesize_browse': 'Shfleto...',
        'pagesize_select_folder': 'Zgjidhni dosjen e destinacionit',
        'pagesize_apply': 'Apliko',
        'pagesize_start': 'Po fillohet ndryshimi i madhësisë së faqes...',
        'pagesize_progress': 'Po ndryshohet madhësia e faqes...',
        'pagesize_success': 'Madhësia e faqes u ndryshua me sukses!\n\nU ruajt si:\n{0}\n\nDëshironi të hapni PDF-në e re?',
        'pagesize_complete': 'Ndryshimi i madhësisë së faqes u përfundua',
        'pagesize_cancel': 'Ndryshimi i madhësisë së faqes u anulua',
        'pagesize_error_format': 'Gabim gjatë ndryshimit të madhësisë së faqes:\n\n{0}',
        'pagesize_preview_info': 'Madhësia e re: {0} x {1} pt',
        'filename_pagesize_suffix': '_madhësi_e_re',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informacioni i PDF',
        'pdf_info_menu': 'Shfaq informacionin e PDF',
        'pdf_info_voice': 'Po shfaqet informacioni i PDF',
        'pdf_info_error': 'Gabim gjatë shfaqjes së informacionit të PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Shfaq shkurtoret e tastierës",
        "shortcuts_dialog_title": "Shkurtoret e tastierës",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 SKEDARI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Hap PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Mbyll PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Ruaj si...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Mbro dokumentin</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Printo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Printo menjëherë (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Dil nga aplikacioni</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Eksporto si Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Eksporto si DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Eksporto si TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Eksporto si imazhe (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Nxjerr imazhet</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PËRPUNIMI I DOKUMENTEVE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Faqe të shumta)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Konvertimi PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Rrafsho PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Shtresë PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimizo PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDAKTIM</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Kërko</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Shto faqerojtës</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Menaxho faqerojtësit</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Faqerojtësi tjetër</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Faqerojtësi i mëparshëm</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Ekzekuto OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 MENAXHIMI I FAQEVE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rrotullo faqen aktuale</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rrotullo të gjitha faqet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizo faqen aktuale</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizo të gjitha faqet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Fshi faqet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Nxjerr faqet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Fut faqet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Zhvendos faqet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Bashko PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Ndrysho madhësinë e faqes</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 FUT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Fut tekst</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Fut kryq</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Fut nënshkrimin 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Fut nënshkrimin 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Fut imazh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Fut drejtkëndësh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Fut elips</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Fut vijë</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Fut shigjetë</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Fut numrat e faqeve</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Shenjë uji teksti</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Shenjë uji imazhi</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDAKTIMET</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redaktim (i zi)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redaktim (i bardhë)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Apliko të gjitha redaktimet</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ TË AVANCUARA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Prit PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Redakto metadatat</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ SHIKIM</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Ndërro modalitetin Errët/Shkëlqyeshëm</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Shfaq dritaren e tekstit</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Gjerësia e faqes (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dy faqe (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Përmbledhje (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ CILËSIMET</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Menaxhimi i fjalëkalimeve</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Cilësimet OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Cilësimet e nënshkrimit</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formatimi i emrit të skedarit</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Eksporto cilësimet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importo cilësimet</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMACION</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Shfaq informacionin e PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Ndërro daljen zanore</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokuso shiritin e menysë</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Version i ri në dispozicion",
        "update_available_message": "Ka një version të ri <b>{0}</b>.\n\nVizitoni faqen e lëshimit për të shkarkuar përditësimin:\n{1}",
        "update_available_voice": "Versioni i ri {0} është në dispozicion. Ju lutemi shkarkoni përditësimin nga faqja GitHub.",
        "update_open_release": "Hap faqen e lëshimit",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Shkarko të gjitha përkthimet",
        "ask_download_all_translations": """Përveç gjermanishtes, anglishtes dhe vietnamishtes, janë në dispozicion {total_languages} gjuhë të tjera GUI.\n\nA duhet të ofrohen / përditësohen?\n\nShënim:\nGjuhët e panevojshme mund t'i fshini më vonë manualisht në drejtori:\n{translations_path}
        \nNëse anuloni, mund t'i shkarkoni gjuhët GUI më vonë përmes menysë 'Mjetet → Përditëso përkthimet'.""",
        "menu_update_translations": "Përditëso përkthimet",
        "translations_updated": "Përkthimet u përditësuan",
        "translations_update_success": "{} përkthime u përditësuan me sukses ({} të reja, {} të përditësuara).",
        "translations_update_error": "Gabim gjatë përditësimit të përkthimeve",
        "translations_update_no_changes": "Të gjitha përkthimet janë tashmë të përditësuara.",
        "translations_update_offline": "Nuk ka lidhje interneti. Përkthimet nuk mund të përditësoheshin.",
        "translations_update_in_progress": "Përkthimet po përditësohen në sfond...",
        "translations_downloading": "Po shkarkohen përkthimet...",
        "translations_path_hint": "Drejtoria e përdoruesit për përkthime",
        "translations_update_not_available_title": "Përditësimi nuk është i disponueshëm",
        "translations_update_not_available_message": """Përditësimi i përkthimeve është i disponueshëm vetëm në versionin e instaluar.\n\nNë modalitetin e zhvillimit, përkthimet janë tashmë të përditësuara.""",
        "translations_update_no_internet_title": "Nuk ka lidhje interneti",
        "translations_update_no_internet_message": """Nuk mund të krijohet lidhje interneti.\n\nPërkthimet nuk mund të shkarkohen nga GitHub.\n\nZgjidhjet e mundshme:
        • Kontrolloni lidhjen tuaj të internetit
        • Çaktivizoni përkohësisht çdo mur zjarri
        • Provoni përsëri më vonë
        \nMund t'i shkarkoni gjithashtu përkthimet manualisht nga GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Përditësimi është tashmë në vazhdim",
        "btn_retry": "Provo përsëri",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Mirë se vini në PDF Dark View",
        "welcome_title_not_supported": "Mirë se vini në PDF Dark View",
        "welcome_message": "Mirë se vini në PDF Dark View!\n\nGjuha e sistemit tuaj u identifikua si '{language}'.\nDëshironi të përdorni këtë gjuhë për ndërfaqen e përdoruesit?\n\nMund ta ndryshoni gjuhën në çdo kohë përmes 'Cilësimet → Gjuha'.",
        "welcome_message_language_not_available": "Mirë se vini në PDF Dark View!\n\nGjuha e sistemit tuaj u identifikua si '{language}'.\nKjo gjuhë nuk është instaluar ende.\n\nDëshironi të shkarkoni përkthimet për {language} tani nga GitHub?\n\n(Gjuha do të përdoret më pas automatikisht për ndërfaqen e përdoruesit.)",
        "welcome_message_language_not_supported": "Mirë se vini në PDF Dark View!\n\nGjuha e sistemit tuaj u identifikua si '{language}'.\nFatkeqësisht, nuk ka ende përkthime për këtë gjuhë.\n\nNdërfaqja e përdoruesit do të shfaqet në {fallback_language}.\n\nMund ta ndryshoni gjuhën në çdo kohë përmes 'Cilësimet → Gjuha'.\nNëse dëshironi, mund të kontribuoni vetë me një përkthim për gjuhën tuaj:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Po, përdor gjuhën e sistemit",
        "welcome_keep_english": "Jo, mbaj anglishten",
        "welcome_download_language": "Po, shkarko {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programi po mbyllet",

    }

