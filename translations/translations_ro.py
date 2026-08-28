
# ============================================
# translations_ro.py - Dicționar românesc
# Vollständig sortiert nach Kategorien
# ============================================

def load_romanian_strings():
    """Lädt alle rumänischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Încarcă PDF",
        'btn_text_window': "Text OCR",
        'btn_first': "Prima pagină",
        'btn_prev': "Pagina anterioară",
        'btn_next': "Pagina următoare",
        'btn_last': "Ultima pagină",
        'btn_print': "Tipărește",
        'btn_darkmode_light': "Mod luminos",
        'btn_darkmode_dark': "Mod întunecat",
        'btn_delete_pages': "Șterge pagini",
        'btn_extract_pages': "Extrage pagini",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Anulează",
        'btn_save': "Salvează",
        'btn_close': "Închide",
        'btn_delete': "Șterge",
        'btn_delete_all': "Șterge tot",
        'btn_copy': "Copiază",
        'btn_export': "Exportă",
        'btn_show': "Arată parola",
        'btn_hide': "Ascunde parola",
        'btn_authenticate': "Autentifică",
        'btn_settings': "Setări",
        'btn_protect': "Protejează",
        'btn_remove_password': "Elimină parola",
        'btn_manage': "Gestionare parole",
        'btn_retry': "Încearcă din nou",
        'btn_select_all': "Selectează tot",
        'btn_clear_selection': "Anulează selecția",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Pagina {0} din {1}",
        'page_count': "din {0}",
        'goto_page': "Mergi la pagina",
        'page_simple': "Pagina {0}",
        'full_view_page': "Vizualizare completă pagina {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Introduceți termenul de căutare + Enter",
        'search_results': "Rezultate: {0} din {1}",
        'search_nav_hint': "Enter: următorul (Shift+Enter: anteriorul) rezultat",
        'search_no_results': "Niciun rezultat",
        'search_error': "Eroare de căutare",
        'search_active': "Câmp de căutare activat",
        'search_closed': "Căutare încheiată",
        'search_position': "Pagina {0} {1}",
        'search_pos_top': "chiar sus",
        'search_pos_upper': "sus",
        'search_pos_middle': "mijloc",
        'search_pos_lower': "jos",
        'search_pos_bottom': "chiar jos",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Recunoașterea textului s-a încheiat cu succes!",
        'ocr_success_title': "OCR reușit",
        'ocr_success_message': "Documentul este acum căutabil.",
        'ocr_failed': "OCR eșuat",
        'ocr_in_progress': "OCR în curs",
        'ocr_preparing': "Se pregătește PDF-ul...",
        'ocr_analyzing': "Se analizează PDF-ul...",
        'ocr_optimizing': "Optimizare imagine în curs...",
        'ocr_recognizing': "Recunoaștere text în curs...",
        'ocr_embedding': "Încorporare text...",
        'ocr_finalizing': "Finalizare PDF...",
        'ocr_not_available': "OCR indisponibil",
        'ocr_install_message': "Instrumentele OCR nu au fost găsite.\n\nVă rugăm să instalați:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR necesar",
        'ocr_question': "PDF-ul nu conține text căutabil.\nDoriți să efectuați OCR pentru a permite {0}?",
        'ocr_perform': "Efectuați OCR",
        'ocr_later': "Mai târziu",
        'ocr_starting': "Pornire OCR garantat...",
        'ocr_success_voice': "OCR reușit. PDF-ul este acum căutabil.",
        'ocr_partial_success': "OCR a fost efectuat, dar au apărut probleme la înlocuire.\n\nVersiunea căutabilă a fost salvată la:\n{0}\n\nEroare: {1}",
        'ocr_partial_title': "OCR parțial reușit",
        'ocr_partial_voice': "OCR efectuat, dar înlocuirea a eșuat.",
        'original_file': "Fișier original:",
        'old_size': "Dimensiune veche:    {0} octeți",
        'new_size': "Dimensiune nouă: {0} octeți",
        'size_change': "Modificare: {0}{1} octeți",
        'backup_created_file': "Backup creat:\n{0}",
        'backup_not_created': "Backup necreat (setare dezactivată)",
        'page_header': "=== Pagina {0} ===\n{1}\n",
        'scanned_page_header': "=== Pagina {0} (scanată) ===\n[Această pagină conține doar text scanat]\n[Efectuați OCR manual]\n",
        'scanned_warning': "⚠️ TEXT SCANAT - OCR NECESAR",
        'guaranteed_title': "PDF căutabil creat",
        'guaranteed_message': "<b>Versiune căutabilă garantată creată!</b>\n\nDeoarece OCR-ul automat a eșuat, a fost creat un PDF alternativ căutabil:\n\n{0}\n\n<b>Acest fișier conține:</b>\n• Text extras (dacă exista)\n• Indicații pentru paginile scanate\n• Este complet căutabil",
        'guaranteed_voice': "PDF căutabil garantat creat.",
        'instruction_title': "INSTRUCȚIUNI OCR",
        'instruction_file': "Fișier original: {0}",
        'instruction_text': "Recunoașterea automată a textului (OCR) a eșuat.\nEfectuați OCR manual:\n\n1. CU OCRmyPDF (linie de comandă):\n   ocrmypdf --force-ocr \"[FIȘIER]\" \"ieșire.pdf\"\n\n2. CU ADOBE ACROBAT (macOS/Windows):\n   • Deschideți PDF-ul în Acrobat\n   • Instrumente > Editare PDF\n   • Selectați 'Recunoaștere text'\n\n3. CU PREVIEW (macOS):\n   • Deschideți PDF-ul în Previzualizare\n   • Fișier > Exportă...\n   • Filtru Quartz: 'Reduceți dimensiunea fișierului'\n   • Activați 'Efectuați OCR'\n\n4. SERVICII OCR ONLINE:\n   • smallpdf.com/ro/ocr-pdf\n   • ilovepdf.com/ro/ocr-pdf\n   • adobe.com/ro/acrobat/online/pdf-to-word.html",
        'instruction_created': "Instrucțiuni OCR create",
        'instruction_created_message': "Au fost create instrucțiuni detaliate:\n\n{0}\n\nUrmați pașii pentru OCR manual.",
        'instruction_created_voice': "Instrucțiuni OCR create.",
        'ocr_impossible': "OCR imposibil",
        'ocr_impossible_message': "OCR nu a putut fi efectuat.\n\nProcesați '{0}' manual cu software OCR.",
        'ocr_impossible_voice': "OCR imposibil. Procesați manual.",
        'emergency_title': "OCR de urgență",
        'emergency_message': "A fost creat un PDF de urgență:\n\n{0}\n\nProcesați acest fișier manual cu OCR.",
        'emergency_voice': "PDF de urgență creat. Efectuați OCR manual.",
        'critical_error': "Eroare critică",
        'critical_error_message': "OCR nu a putut fi pornit.\n\nReporniți programul și verificați instalarea OCR.",
        'critical_error_voice': "Eroare critică OCR",
        'ocr_question_html': "<p>PDF-ul nu conține text căutabil.<p>Doriți să efectuați OCR pentru a permite <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR necesar. PDF-ul nu conține text căutabil. Doriți să efectuați OCR pentru a permite {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "niciun PDF încărcat",
        'no_pdf_message': "Nu este încărcat niciun PDF",
        'pdf_not_found': "Fișier PDF negăsit",
        'file_size': "Dimensiune fișier",
        'bytes': "octeți",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup creat",
        'backup_disabled': "Backup dezactivat",
        'backup_activated': "Creare backup activată",
        'backup_deactivated': "Creare backup dezactivată",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ activat",
        'backup_off': "✘ dezactivat",
        'close_pdf': "Închid PDF: {0}",
        'pdf_not_found_format': "Fișier PDF negăsit: {0}",
        'error_pdf_load_format': "Eroare la încărcarea PDF-ului: {0}",
        'load_failed_format': "Încărcare eșuată:\n{0}",
        'decrypted_suffix': "(decriptat)",
        'decryption_failed': "Decriptare eșuată.",
        'decryption_error': "Eroare la decriptare",
        'decryption_success': "Decriptare reușită",
        'decryption_success_message': "PDF-ul a fost decriptat și salvat la:\n\n{0}",
        'decryption_success_voice': "PDF-ul a fost decriptat și salvat.",
        'password_remove_error': "Eroare la eliminarea parolei",
        'save_unencrypted': "Salvează PDF necriptat ca",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Salvează ca...",
        'save_copy': "Salvează copie",
        'save_success': "PDF salvat la: {0}",
        'save_encrypted': "PDF protejat salvat la: {0}",
        'save_error': "PDF-ul nu a putut fi salvat",
        'encryption_question': "Doriți să protejați PDF-ul cu o parolă?",
        'encryption_yes': "Da",
        'encryption_no': "Nu",
        'encryption_cancel': "Anulează",
        'save_cancel': "Salvare anulată",
        'save_encrypted_voice': "Fișier criptat și salvat.",
        'save_success_voice': "Fișierul PDF a fost salvat necriptat.",
        'save_error_format': "PDF-ul nu a putut fi salvat:\n{0}",
        'export_pages_success': "Export Pages reușit",
        'export_pages_error': "Export Pages eșuat",
        'export_pages_error_format': "Export Pages eșuat: {0}",
        'export_word_success': "Export Word reușit",
        'export_word_error': "Export Word eșuat",
        'export_word_error_format': "Export Word eșuat: {0}",
        'export_text_success': "Export text reușit",
        'export_text_error': "Export text eșuat",
        'export_text_error_format': "Export text eșuat: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Parolă necesară",
        'password_enter': "Introduceți parola",
        'password_confirm': "Confirmați parola",
        'password_new': "Parolă nouă",
        'password_current': "Parola actuală",
        'password_save': "Salvează parola (criptată)",
        'password_saved': "✓ Parola pentru acest fișier este salvată",
        'password_wrong': "Parolă greșită",
        'password_mismatch': "Parolele nu coincid",
        'password_too_short': "Parolă prea scurtă",
        'password_min_length': "Parola trebuie să aibă cel puțin 4 caractere",
        'password_strength': "Puterea parolei",
        'password_strength_very_weak': "Foarte slabă",
        'password_strength_weak': "Slabă",
        'password_strength_medium': "Medie",
        'password_strength_strong': "Puternică",
        'password_strength_very_strong': "Foarte puternică",
        'password_char_count': "({0} caractere)",
        'password_match': "✓ Potrivire",
        'password_no_match': "✗ Parolele nu coincid",
        'password_show': "Arată",
        'password_hide': "Ascunde",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Gestionare parole",
        'password_table_filename': "Nume fișier",
        'password_table_password': "Parolă",
        'password_count': "{0} parolă{1} salvată",
        'password_count_singular': "",
        'password_count_plural': "e",
        'password_none': "Nicio parolă salvată",
        'password_copied': "{0} parolă{1} copiată",
        'password_copied_singular': "",
        'password_copied_plural': "e",
        'password_delete_confirm': "Sigur doriți să ștergeți parola pentru '{0}'?",
        'password_delete_multiple': "Sigur doriți să ștergeți cele {0} parole selectate?",
        'password_delete_all_confirm': "Sigur doriți să ștergeți toate cele {0} parole salvate?",
        'password_deleted': "{0} parolă{1} ștearsă",
        'password_deleted_singular': "",
        'password_deleted_plural': "e",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Toate parolele au fost șterse",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generator de parole",
        'generator_generated': "Parolă generată:",
        'generator_regenerate': "Regenerează",
        'generator_copy': "Copiază",
        'generator_use': "Folosește",
        'generator_settings': "Setări",
        'generator_length': "Lungime:",
        'generator_group_every': "Separator la fiecare",
        'generator_group_chars': "caractere.    Separator:",
        'generator_uppercase': "Litere mari (A-Z)",
        'generator_lowercase': "Litere mici (a-z)",
        'generator_digits': "Cifre (0-9)",
        'generator_symbols': "Caractere speciale (!@#$%^&*)",
        'generator_exclude': "Excluse:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Parolă master necesară",
        'master_password_setup': "Configurați parola master",
        'master_password_change': "Schimbați parola master",
        'master_password_enter': "Introduceți parola master",
        'master_password_choose': "Alegeți o parolă master puternică (cel puțin 8 caractere)",
        'master_password_new': "Introduceți noua parolă master",
        'master_password_confirm': "Confirmați parola",
        'master_password_authenticate': "Autentificați",
        'master_password_success': "Parola master a fost configurată cu succes.",
        'master_password_changed': "Parola master a fost schimbată cu succes.",
        'master_password_removed': "Parola master și toate parolele au fost șterse.",
        'master_password_remove': "Eliminați parola master",
        'master_password_remove_confirm': "Sunteți SIGUR că doriți să ștergeți TOATE parolele?\n\nAceastă acțiune este IREVERSIBILĂ!",
        'master_password_export_before': "Doriți să exportați o copie de rezervă înainte?",
        'master_password_export_delete': "Exportă și șterge",
        'master_password_delete_now': "Șterge acum",
        'master_password_for_signatures': "Pentru a putea folosi semnăturile, trebuie să configurați o parolă master.\n\nDoriți să configurați acum o parolă master?",
        'master_password_for_private': "Pentru a putea folosi fragmentele de text private, trebuie să configurați o parolă master.\n\nDoriți să configurați acum o parolă master?",
        'master_password_info': """
            <b>🔐 FĂRĂ PAROLĂ MASTER:</b><br>
            • Nu este posibilă afișarea, copierea și exportarea parolelor<br>
            • Ștergerea parolelor este întotdeauna posibilă (chiar și fără parolă master)<br><br>

            <b>🔐 CU PAROLĂ MASTER:</b><br>
            • Toate funcțiile disponibile după autentificare<br>
            • Parolele sunt criptate cu parola master<br>
            • Lungime minimă: 8 caractere<br>
            • Stocare securizată a hash-ului SHA-256<br><br>

            <b>IMPORTANT:</b><br>
            • La pierderea parolei master: parolele nu pot fi recuperate<br>
            • La eliminarea parolei master: TOATE parolele sunt șterse<br>
            • Opțiune de export disponibilă înainte de ștergere<br>
            • Parola master poate fi schimbată oricând
        """,
        'signature_auth_disabled': "Dezactivați cererea de parolă pentru semnături",
        'template_auth_disabled': "Dezactivați cererea de parolă pentru fragmentele de text private",
        'master_password_for_signatures_settings': "Pentru a putea folosi semnăturile, trebuie să configurați o parolă master.\n\nAccesați Setări - Gestionare parole",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Protejați PDF",
        'protect_info': "Fișierul '{0}' va fi protejat cu o parolă.",
        'protect_instruction': "Introduceți de două ori parola dorită pentru a proteja documentul, sau folosiți generatorul de parole din dreapta câmpului de intrare.",
        'protect_success': "PDF-ul a fost protejat cu succes și salvat la:\n{0}\n\nParola: {1}\n\nDoriți să deschideți acum PDF-ul protejat?",
        'protect_open': "Da",
        'protect_skip': "Nu",
        'protect_error': "Eroare la protejarea PDF-ului",
        'protect_open_title': "deschideți PDF-ul protejat",
        'protect_question': "Gata. Doriți să deschideți acum PDF-ul protejat? Da sau Nu?",
        'password_cancel': "Dialog parolă anulat",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Șterge pagini",
        'pages_extract': "Extrage pagini",
        'pages_insert': "Inserare pagini",
        'pages_move': "Mută pagini",
        'pages_delete_options': "Opțiuni de ștergere",
        'pages_delete_empty': "Șterge toate paginile goale",
        'pages_delete_current': "Șterge pagina curentă",
        'pages_delete_range': "Șterge interval de pagini",
        'pages_extract_options': "Opțiuni de extragere",
        'pages_extract_current': "Extrage pagina curentă",
        'pages_extract_range': "Extrage interval de pagini",
        'pages_insert_position': "Poziția de inserare",
        'pages_insert_before': "Inserare înainte de pagina:",
        'pages_insert_select': "Selectați PDF",
        'pages_insert_none': "Niciun PDF selectat",
        'pages_move_source': "Pagini de mutat",
        'pages_move_from': "De la pagina:",
        'pages_move_to': "Până la pagina:",
        'pages_move_target': "Poziția țintă",
        'pages_move_before': "Mută înainte de pagina:",
        'pages_move_hint': "Notă: pagina 1 = început, {0} = sfârșit",
        'pages_range_invalid': "Pagina de început trebuie să fie mai mică sau egală cu pagina de sfârșit.",
        'pages_position_invalid': "Poziția țintă nu poate fi în interiorul intervalului de mutat.",
        'pages_no_pdf_selected': "Nu este selectat niciun PDF.",
        'pages_deleted': "Au fost șterse {0} pagini.",
        'pages_extracted': "Extras: {0}\nSalvat la: {1}\nDimensiune fișier: {2:.1f} KB",
        'pages_inserted': "{0} pagini inserate",
        'pages_moved': "Au fost mutate {0} pagini.",
        'pages_deleted_none': "Nu a fost ștearsă nicio pagină.",
        'pages_delete_progress': "Ștergere pagini...",
        'pages_deleted_with_backup': "Au fost șterse {0} pagini.\n\nBackup: {1}",
        'pages_deleted_voice': "A fost creat un backup și au fost șterse {0} pagini.",
        'info': "Informație",
        'error_dialog_creation': "Dialogul nu a putut fi creat",
        'extract_page_single': "Extrage pagina {0}",
        'extract_page_range': "Extrage paginile {0}-{1}",
        'extract_success_voice': "Pagini extrase cu succes",
        'extract_error_format': "Eroare la extragere: {0}",
        'pages_inserted_voice': "Au fost inserate {0} pagini.",
        'insert_error_format': "Eroare la inserare: {0}",
        'pages_move_progress': "Mutare pagini...",
        'pages_moved_with_backup': "Au fost mutate {0} pagini.\n\nBackup: {1}",
        'move_success_title': "Mutare reușită",
        'pages_moved_voice': "{0} pagini mutate cu succes",
        'mark_removed': "Marcajul paginii {0} eliminat",
        'mark_empty': "Pagina {0} marcată ca goală",
        'mark_export_removed': "Marcajul de export al paginii {0} eliminat",
        'mark_export': "Pagina {0} marcată pentru export",
        'no_empty_pages': "Nicio pagină goală marcată pentru ștergere",
        'delete_empty_confirm': "Doriți să ștergeți toate cele {0} pagini goale marcate?",
        'delete_empty_confirm_voice': "Ștergeți acum toate cele {0} pagini goale marcate? Da sau Nu.",
        'empty_pages_deleted': "{0} pagini goale șterse",
        'no_export_pages': "Nicio pagină marcată pentru export",
        'overwrite_title': "Suprascrieți fișierul existent",
        'overwrite_question': "Fișierul\n\n{0}\n\nexistă deja.\nDoriți să-l suprascrieți?",
        'overwrite_voice': "Suprascrieți fișierul existent? Da sau Nu.",
        'page_skipped': "Pagina {0} a fost omisă",
        'export_complete': "Export finalizat.",
        'export_complete_voice': "Exportul este finalizat.",
        'no_pages_exported': "Nicio pagină exportată",
        'export_cancelled': "Export anulat",
        'pages_exported': "{0} pagini exportate în {1}",
        'export_page_title': "Exportă pagina",
        'page_exported': "Pagina {0} exportată în {1}",
        'export_error': "Eroare la export",
        'export_marked_title': "Exportă paginile marcate",
        'rotate_all_title': "rotește toate paginile",
        'rotate_all_question': "Doriți să rotiți toate paginile cu 90 de grade spre dreapta?",
        'rotate_all_voice': "Doriți să rotiți toate paginile cu 90 de grade spre dreapta? Da sau Nu?",
        'all_pages_rotated': "Toate paginile rotite",
        'page_rotated': "Pagina {0} rotită",
        'rotate_error': "Pagina nu a putut fi rotită",
        'delete_page_confirm': "Doriți să ștergeți pagina {0}?",
        'delete_page_confirm_voice': "Sigur doriți să ștergeți pagina {0}? Da sau Nu.",
        'page_deleted': "Pagina {0} ștearsă",
        'delete_error': "Pagina nu a putut fi ștearsă",
        'pages_deleted_voice': "{0} pagini șterse",
        'pages_exported_split': "{0} pagini au fost exportate cu succes.",
        'pages_skipped': "{0} pagini au fost omise.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extrage pagini (avansat)",
        'pdf_splitter_title': "Splitter și extractor PDF",
        'pdf_splitter_load': " Selectați fișierul PDF",
        'pdf_splitter_info': "Alegeți o opțiune pentru documentul dvs. PDF",
        'pdf_splitter_basic': "Operațiuni de bază",
        'pdf_splitter_single': "Împărțire în pagini individuale",
        'pdf_splitter_range': "Extrage pagini:",
        'pdf_splitter_range_placeholder': "de ex. 1-3,5,7-9",
        'pdf_splitter_clean': "Operațiuni de curățare",
        'pdf_splitter_remove_empty': "Eliminați toate paginile goale",
        'pdf_splitter_remove': "Ștergeți intervalul de pagini:",
        'pdf_splitter_remove_placeholder': "de ex. 2,4-6",
        'pdf_splitter_process': "Procesează PDF",
        'pdf_splitter_loaded': "PDF încărcat. Alegeți o opțiune",
        'pdf_read_error': "PDF-ul nu a putut fi citit",
        'pages': "Pagini",
        'pages_created': "Pagini create",
        'range_empty': "Introduceți un interval de pagini",
        'range_invalid': "Interval de pagini invalid",
        'range_created': "Un nou PDF cu paginile selectate a fost creat:\n{0}",
        'empty_removed': "{0} pagini goale eliminate.\nIeșire: {1}",
        'remove_empty': "Introduceți paginile de eliminat",
        'remove_invalid': "Pagini de eliminat invalide",
        'remove_done': "PDF curățat creat:\n{0}",
        'open_folder': "Deschide folderul",
        'show_in_finder': "Arată în Finder",
        'pdf_splitter_no_pdf': "Încărcați mai întâi un fișier PDF.",
        'process_error': "Eroare la procesarea PDF-ului",
        'pages_created_voice': "{0} pagini create",
        'range_created_voice': "PDF creat cu paginile selectate",
        'empty_removed_voice': "{0} pagini goale eliminate",
        'remove_done_voice': "PDF curățat creat",
        'pdf_splitter_split_groups': "Fiecare grup continuu în fișier separat",
        'range_created_single': "PDF nou creat:\n{0}",
        'range_created_multiple': "Au fost create {0} fișiere PDF.",
        'range_created_voice_single': "Un PDF cu paginile selectate a fost creat",
        'range_created_voice_multiple': "Au fost create {0} fișiere PDF",
        'empty_removed_none_left': "Nicio pagină rămasă",
        'empty_removed_all_empty': "Toate paginile au fost recunoscute ca goale și ar fi eliminate. Nu a fost creat niciun fișier.",
        'preview_single': "Previzualizare: {0}",
        'preview_enter_range': "Introduceți un interval de pagini.",
        'preview_invalid_range': "Interval de pagini invalid.",
        'preview_file': "Previzualizare: {0}",
        'preview_files': "Previzualizare: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Pornire imprimare",
        'print_sent': "Lucrare de imprimare trimisă",
        'print_now': "Imprimare imediată",
        'print_error': "Eroare la imprimarea imediată",
        'print_limited': "Funcția de imprimare limitată pe acest sistem",
        'print_error_format': "Eroare la imprimarea imediată: {0}",
        'warning': "Avertisment",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Comutați la modul luminos",
        'mode_switch_to_dark': "Comutați la modul întunecat",
        'mode_dark_activated': "Mod întunecat activat",
        'mode_light_activated': "Mod luminos activat",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Vizualizare completă",
        'zoom_two_pages': "Două pagini una lângă alta",
        'zoom_overview': "Mod de prezentare generală",
        'zoom_cannot_during_search': "Zoom-ul nu este posibil în timpul căutării",
        'zoom_exit_first': "Ieșiți mai întâi din zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop activat",
        'drag_disabled': "Drag & Drop dezactivat",
        'drag_page_grab': "Pagina {0} prinsă",
        'drag_page_dropped': "Pagina {0} inserată la poziția {1}",
        'drag_position_invalid': "Poziție invalidă",
        'drag_same_position': "Pagina {0} rămâne la poziția {0}",
        'drag_error': "Eroare la mutare",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Introducere text cu formatări avansate și gestionare fragmente",
        'text_templates': "Fragmente de text disponibile:",
        'text_name': "Nume",
        'text_preview': "Previzualizare text",
        'text_enter': "Text:",
        'text_font_size': "Dimensiune font:",
        'text_formatting': "Formatare:",
        'text_bold': "Îngroșat",
        'text_italic': "Cursiv",
        'text_underline': "Subliniat",
        'text_alignment': "Aliniere:",
        'text_left': "Stânga",
        'text_center': "Centrat",
        'text_right': "Dreapta",
        'text_color': "Culoare text:",
        'text_opacity': "Opacitate:",
        'text_word_wrap': "Împărțire pe linii:",
        'text_auto': "Automat",
        'text_page_width_95': "Lățime pagină (95%)",
        'text_page_width_85': "Foarte lat (85%)",
        'text_page_width_75': "Mai lat (75%)",
        'text_page_width_60': "Lat (60%)",
        'text_page_width_50': "Mediu (50%)",
        'text_page_width_30': "Îngust (30%)",
        'text_page_width_20': "Mai îngust (20%)",
        'text_page_width_10': "Foarte îngust (10%)",
        'text_no_wrap': "Fără împărțire",
        'text_private': "Fragment de text privat (necesită autentificare)",
        'text_preview_label': "Previzualizare:",
        'text_preview_placeholder': "Aici va fi afișată o previzualizare a textului...",
        'text_no_text': "(Niciun text)",
        'text_save_template': "💾 Salvează ca fragment",
        'text_delete_template': "🗑 Șterge fragmentul de text selectat",
        'text_show_private': "Arată private",
        'text_hide_private': "Ascunde private",
        'text_use': "✅ Folosește text",
        'text_saved': "Fragment de text salvat ca:\n{0}",
        'text_saved_voice': "Fragment de text salvat",
        'text_deleted': "Fragment de text șters",
        'text_no_text_to_save': "Niciun text de salvat.",
        'text_no_templates': "Niciun fragment de text găsit",
        'text_private_master_required': "Fragmentele private pot fi folosite numai dacă este configurată o parolă master.\n\nDoriți să configurați acum o parolă master?",
        'text_filename': "Nume fișier pentru fragmentul de text (fără 'Text_' și '.txt'):",
        'text_filename_hint': "Exemplu: 'Telefon HomeOffice' va fi salvat ca 'Text_Telefon HomeOffice.txt'",
        'text_save_hint': "Fragmentul de text va fi salvat automat cu formatarea.",
        'text_guide_title': "Introducere text – Instrucțiuni",
        'text_delete_confirm': "Sigur doriți să ștergeți fragmentul de text?\n\nFișier: {0}\nText: {1}...",
        'text_make_public': "Marchează ca public",
        'text_make_private': "Marchează ca privat",
        'text_privacy_changed': "Stare de confidențialitate modificată",
        'text_private_always': "Private mereu vizibile (setare)",
        'text_mode_required': "Activați mai întâi modul text",
        'text_continue_editing': "Continuă editarea – cursorul la sfârșitul textului",
        'text_no_input': "Niciun text introdus – text eliminat",
        'save_dialog_question': "Cum doriți să continuați?",
        'text_save_question': "Salvați toate textele și crucile, ajustați, continuați editarea sau eliminați?",
        'copy_cross': "Cruce copiată",
        'paste_cross': "Cruce inserată",
        'paste_text': "Text inserat",
        'cross_discarded': "Cruce eliminată",
        'all_discarded': "Tot eliminat",
        'text_discarded': "Text eliminat",
        'no_texts_to_save': "Niciun text de salvat",
        'no_valid_texts': "Niciun text valid de salvat",
        'text_word_singular': "text",
        'text_word_plural': "texte",
        'cross_word_singular': "cruce",
        'cross_word_plural': "cruci",
        'texts_saved_title': "Texte salvate",
        'texts_crosses_saved': "{0} {1} și {2} {3} au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'texts_crosses_saved_voice': "{0} {1} și {2} {3} salvate.",
        'texts_saved': "{0} {1} au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'texts_saved_voice': "{0} {1} salvate.",
        'crosses_saved': "{0} {1} au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'crosses_saved_voice': "{0} {1} salvate.",
        'elements_saved': "{0} elemente au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'elements_saved_voice': "{0} elemente salvate.",
        'text_window_load_error': "Fereastra de text nu a putut fi încărcată",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Introducere text și fragmente de text – Instrucțiuni detaliate**

        **1. Inserarea și editarea textului**
        - Faceți clic dreapta pe locul dorit în document și selectați „Inserare text”.
        - Se deschide un dialog în care puteți introduce și formata textul:
        • Dimensiune font, îngroșat, cursiv, subliniat
        • Culoare text (la alegere)
        • Transparență (opacitate) prin glisor
        • Împărțire pe linii (diferite lățimi, de ex. lățime pagină, îngust, fără împărțire)
        - După confirmare, textul apare la locul clicului. Îl puteți muta cu mouse-ul sau cu tastele săgeată.
        - Dublu clic pe text deschide modul de editare; ESC îl închide.

        **2. Gestionarea fragmentelor de text (șabloane)**
        - În dialogul text, în stânga, vedeți o listă cu toate fragmentele salvate.
        - **Salvarea unui fragment:** Introduceți textul, formatați-l și faceți clic pe „💾 Salvează ca fragment”. Introduceți un nume de fișier (fără extensie).
        - **Încărcarea unui fragment:** Faceți clic pe numele dorit din listă. Textul și formatarea sunt preluate și pot fi ajustate dacă este necesar.
        - **Ștergerea:** Faceți clic dreapta pe un fragment pentru a-l șterge sau pentru a-i modifica starea de confidențialitate.

        **3. Fragmente de text private (parolă master)**
        - Dacă ați configurat o parolă master (în Setări → Gestionare parole), puteți marca fragmentele ca „private”.
        - Activați caseta „Fragment de text privat” în dialog înainte de salvare.
        - Fragmentele private sunt afișate în listă numai după ce v-ați autentificat o dată pe sesiune cu parola master (autentificare prin pictograma lacăt sau la primul acces).
        - Astfel puteți proteja fragmentele confidențiale împotriva accesului neautorizat.

        **4. Inserarea crucilor**
        - Din meniul contextual puteți insera și o cruce grafică (de ex. pentru căsuțe de bifat).
        - Dimensiunea, grosimea liniei și culoarea crucilor pot fi ajustate global în setări (meniul „Setări” → „Setări cruci”).
        - Faceți clic dreapta pe o cruce existentă pentru a o modifica individual.

        **5. Acțiuni colective**
        - Dacă ați plasat mai multe texte sau cruci pe o pagină, le puteți salva sau elimina pe toate simultan din meniul contextual (clic dreapta în modul text).
        - La salvare, toate elementele sunt încorporate în PDF și rămân ca grafică vectorială.

        **6. Scurtături tastatură în modul text**
        - Taste săgeată: mutarea elementului
        - Ctrl+săgeată: pași mai mari
        - Enter: deschide dialogul de salvare (salvare totală / ajustare / eliminare)
        - ESC: elimină elementul curent
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Introducere text și fragmente de text – Instrucțiuni detaliate</strong></p>

        <p><strong>1. Inserarea și editarea textului</strong></p>
        <ul>
        <li>Faceți clic dreapta pe locul dorit în document și selectați „Inserare text”.</li>
        <li>Se deschide un dialog în care puteți introduce și formata textul:<br/>
        • Dimensiune font, îngroșat, cursiv, subliniat<br/>
        • Culoare text (la alegere)<br/>
        • Transparență (opacitate) prin glisor<br/>
        • Împărțire pe linii (diferite lățimi, de ex. lățime pagină, îngust, fără împărțire)</li>
        <li>După confirmare, textul apare la locul clicului. Îl puteți muta cu mouse-ul sau cu tastele săgeată.</li>
        <li>Dublu clic pe text deschide modul de editare; ESC îl închide.</li>
        </ul>

        <p><strong>2. Gestionarea fragmentelor de text (șabloane)</strong></p>
        <ul>
        <li>În dialogul text, în stânga, vedeți o listă cu toate fragmentele salvate.</li>
        <li><strong>Salvarea unui fragment:</strong> Introduceți textul, formatați-l și faceți clic pe „💾 Salvează ca fragment”. Introduceți un nume de fișier (fără extensie).</li>
        <li><strong>Încărcarea unui fragment:</strong> Faceți clic pe numele dorit din listă. Textul și formatarea sunt preluate și pot fi ajustate dacă este necesar.</li>
        <li><strong>Ștergerea:</strong> Faceți clic dreapta pe un fragment pentru a-l șterge sau pentru a-i modifica starea de confidențialitate.</li>
        </ul>

        <p><strong>3. Fragmente de text private (parolă master)</strong></p>
        <ul>
        <li>Dacă ați configurat o parolă master (în Setări → Gestionare parole), puteți marca fragmentele ca „private”.</li>
        <li>Activați caseta „Fragment de text privat” în dialog înainte de salvare.</li>
        <li>Fragmentele private sunt afișate în listă numai după ce v-ați autentificat o dată pe sesiune cu parola master (autentificare prin pictograma lacăt sau la primul acces).</li>
        <li>Astfel puteți proteja fragmentele confidențiale împotriva accesului neautorizat.</li>
        </ul>

        <p><strong>4. Inserarea crucilor</strong></p>
        <ul>
        <li>Din meniul contextual puteți insera și o cruce grafică (de ex. pentru căsuțe de bifat).</li>
        <li>Dimensiunea, grosimea liniei și culoarea crucilor pot fi ajustate global în setări (meniul „Setări” → „Setări cruci”).</li>
        <li>Faceți clic dreapta pe o cruce existentă pentru a o modifica individual.</li>
        </ul>

        <p><strong>5. Acțiuni colective</strong></p>
        <ul>
        <li>Dacă ați plasat mai multe texte sau cruci pe o pagină, le puteți salva sau elimina pe toate simultan din meniul contextual (clic dreapta în modul text).</li>
        <li>La salvare, toate elementele sunt încorporate în PDF și rămân ca grafică vectorială.</li>
        </ul>

        <p><strong>6. Scurtături tastatură în modul text</strong></p>
        <ul>
        <li>Taste săgeată: mutarea elementului</li>
        <li>Ctrl+săgeată: pași mai mari</li>
        <li>Enter: deschide dialogul de salvare (salvare totală / ajustare / eliminare)</li>
        <li>ESC: elimină elementul curent</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Setări cruci",
        'cross_properties': "Proprietăți cruce",
        'cross_size': "Dimensiune (px):",
        'cross_line_width': "Grosime linie:",
        'cross_color': "Culoare:",
        'cross_choose_color': "Alegeți",
        'cross_fine_tuning': "Reglaj fin la salvare (pixeli)",
        'cross_offset_x': "Decalaj X:",
        'cross_offset_y': "Decalaj Y:",
        'cross_offset_x_tooltip': "Valorile negative mută crucea la stânga la salvare, cele pozitive la dreapta",
        'cross_offset_y_tooltip': "Valorile negative mută crucea în sus la salvare, cele pozitive în jos",
        'cross_preview': "Previzualizare",
        'cross_save': "Aplică setările",
        'cross_customized': "Cruce ajustată",
        'cross_settings_applied': "Setări cruci salvate.\nDimensiune: {0}px, grosime linie: {1}px\n{2}",
        'cross_updated_count': "{0} cruci existente actualizate.",
        'cross_no_crosses': "Nicio cruce existentă găsită.",
        'cross_settings_applied_all': "Setări cruci aplicate pentru toate cele {0} cruci",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Setări semnături",
        'signature_1': "Semnătura 1",
        'signature_2': "Semnătura 2",
        'signature_select': "Selectați semnătura",
        'signature_add': "➕ Adăugați semnătură nouă...",
        'signature_size': "Dimensiune pentru semnătura {0} (%):",
        'signature_common': "Setări generale",
        'signature_timestamp': "Adăugați automat marcaj temporal",
        'signature_location': "Locație implicită:",
        'signature_timestamp_size': "Dimensiune font marcaj temporal:",
        'signature_no_files': "-- Nu s-au găsit semnături --",
        'signature_insert': "Inserați semnătura",
        'signature_insert_1': "Inserați semnătura 1",
        'signature_insert_2': "Inserați semnătura 2",
        'signature_customize': " Ajustați semnătura",
        'signature_discard': " Eliminați această semnătură",
        'signature_save_all': " Salvați toate semnăturile",
        'signature_discard_all': " Eliminați toate semnăturile",
        'signature_guide_title': "Semnături – Instrucțiuni",
        'signature_guide': """
📝 Semnături – Instrucțiuni rapide

- Configurați o parolă master
- Configurați semnăturile în meniul Setări
  (dimensiune, marcaj temporal ...)
- Inserați cu CLIC DREAPTA la locația dorită
  (parola master necesară o dată pe sesiune)
- Mutați semnătura cu mouse-ul sau tastele săgeată
- Pot fi inserate mai multe semnături una după alta
- Fiecare semnătură poate fi ajustată individual
- Eliminați o singură semnătură
- Salvați / eliminați toate semnăturile simultan
- Alternativ, puteți folosi și bara de meniu.
        """,
        'signature_placeholder': "Nicio previzualizare disponibilă",
        'signature_info': "Semnătura {0}: {1}×{2} px ({3}% din {4}×{5})",
        'signature_info_placeholder': "Setări pentru semnătura {0}",
        'signature_inserted': "Semnătura {0} inserată pe pagina {1}",
        'signature_deleted': "Semnătură ștearsă",
        'signature_copied': "Semnătură copiată",
        'signature_pasted': "Semnătura {0} inserată",
        'signature_saved': "{0} semnături au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'signature_saved_voice': "{0} semnături salvate",
        'mode_replace_signature_format': "Ieșiți din mod și inserați semnătura {0}",
        'mode_conflict_voice_signature': "Modul {0} este activ. Ieșiți și inserați semnătura?",
        'signature_not_configured': "Semnătura {0} nu este configurată",
        'signature_file_not_found': "Fișierul semnăturii nu a fost găsit",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nicio semnătură copiată",
        'no_signatures_to_save': "Nicio semnătură de salvat",
        'signature_save_question': "Salvați toate semnăturile, ajustați sau eliminați aceasta?",
        'signatures_saved_title': "Semnături salvate",
        'signatures_saved': "{0} semnături au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'signatures_saved_voice': "{0} semnături salvate.",
        'all_signatures_discarded': "Toate semnăturile eliminate",
        'signature_settings_saved': "Setări semnături salvate",
        'signature_cancelled': "Semnătură eliminată",
        'signature_active_title': "Semnătură activă",
        'signature_replace_question': "Există deja o semnătură activă.\n\nDoriți să înlocuiți semnătura curentă?",
        'signature_replace': "Înlocuiți semnătura",
        'signature_replace_voice': "Înlocuiți semnătura curentă sau anulați?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Setări imagini",
        'image_common': "Setări generale imagini",
        'image_keep_aspect': "Păstrați raportul de aspect la tragere",
        'image_default_size': "Dimensiune implicită (%):",
        'image_dark_invert': "Inversați imaginile în modul întunecat",
        'image_dark_invert_tooltip': "Activat: imaginile sunt inversate pentru o vizibilitate mai bună",
        'image_fine_tuning': "Reglaj fin (pixeli)",
        'image_offset_x': "Decalaj X:",
        'image_offset_y': "Decalaj Y:",
        'image_offset_x_tooltip': "Valorile negative mută imaginea la stânga la salvare, pozitive la dreapta",
        'image_offset_y_tooltip': "Valorile negative mută imaginea în sus la salvare, pozitive în jos",
        'image_select': "Selectați imaginea",
        'image_insert': "Inserați imaginea",
        'image_customize': " Ajustați imaginea",
        'image_aspect': " Păstrați raportul de aspect",
        'image_discard': " Eliminați această imagine",
        'image_save_all': " Salvați toate imaginile",
        'image_discard_all': " Eliminați toate imaginile",
        'image_filter': "Imagini",
        'image_guide_title': "Inserarea imaginilor – Instrucțiuni",
        'image_guide': """
📷 Inserarea imaginilor în PDF – Instrucțiuni rapide:

1. Faceți clic dreapta la locația dorită
2. „Inserați imagine” → selectați imaginea
3. Poziționați imaginea: trageți cu mouse-ul
4. Ajustați dimensiunea: trageți de colțuri/margini
5. Păstrați raportul de aspect: tasta [A]
6. Alte ajustări: clic dreapta pe imagine

Sfat: În meniul contextual puteți ajusta setările.
        """,
        'image_inserted': "Imagine inserată pe pagina {1}",
        'image_deleted': "Imagine eliminată",
        'image_copied': "Imagine copiată",
        'image_pasted': "Imagine inserată",
        'image_saved': "{0} imagini au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'image_saved_voice': "{0} imagini salvate",
        'image_aspect_on': "activat",
        'image_aspect_off': "dezactivat",
        'image_aspect_toggle': "Păstrați raportul de aspect {0}",
        'image_reset': "Imagine readusă la dimensiunea originală",
        'image_replaced': "Imagine înlocuită",
        'image_invalid': "Imagine invalidă",
        'mode_replace_image': "Inserați imagine",
        'mode_conflict_voice_image': "Modul {0} este activ. Ieșiți și inserați imaginea?",
        'image_active_title': "Imagine activă",
        'image_replace_question': "Există deja o imagine activă.\n\nDoriți să înlocuiți imaginea curentă?",
        'image_replace': "Înlocuiți imaginea",
        'image_replace_voice': "Înlocuiți imaginea curentă sau anulați?",
        'image_filter_all': "Imagini (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Toate fișierele (*.*)",
        'no_copied_image': "Nicio imagine copiată",
        'image_discarded': "Imagine eliminată",
        'image_save_question': "Salvați toate imaginile, ajustați sau eliminați aceasta?",
        'no_images_to_save': "Nicio imagine de salvat",
        'no_valid_images': "Nicio imagine validă de salvat",
        'images_saved_title': "Imagini salvate",
        'images_saved': "{0} imagini au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'images_saved_voice': "{0} imagini salvate.",
        'all_images_discarded': "Toate imaginile eliminate",
        'image_settings_updated': "Setări imagini actualizate",
        'image_replace_title': "Selectați o imagine nouă",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Setări forme",
        'form_basic': "Setări de bază",
        'form_default_type': "Tip formă implicit:",
        'form_rectangle': "Dreptunghi",
        'form_ellipse': "Elipsă",
        'form_line': "Linie",
        'form_arrow': "Săgeată",
        'form_line_width': "Grosime linie:",
        'form_colors': "Culori",
        'form_line_color': "Culoare linie:",
        'form_fill_color': "Culoare umplere:",
        'form_choose_color': "Alegeți",
        'form_transparent': "Fundal transparent (numai linie)",
        'form_filled': "umplut",
        'form_dark_mode': "Mod întunecat",
        'form_dark_invert': "Inversați culorile în modul întunecat",
        'form_fine_tuning': "Reglaj fin (pixeli)",
        'form_offset_x': "Decalaj X:",
        'form_offset_y': "Decalaj Y:",
        'form_offset_x_tooltip': "Valorile negative mută forma la stânga la salvare, pozitive la dreapta",
        'form_offset_y_tooltip': "Valorile negative mută forma în sus la salvare, pozitive în jos",
        'form_preview': "Previzualizare",
        'form_insert': "Inserați formă",
        'form_rectangle_insert': "Dreptunghi",
        'form_ellipse_insert': "Elipsă/cerc",
        'form_line_insert': "Linie (2 clicuri)",
        'form_arrow_insert': "Săgeată (2 clicuri)",
        'form_customize': " Ajustați forma",
        'form_transparent_toggle': " Fundal transparent",
        'form_discard': " Eliminați această formă",
        'form_save_all': " Salvați toate formele",
        'form_discard_all': " Eliminați toate formele",
        'form_guide_title': "Inserarea formelor – Instrucțiuni",
        'form_guide': """
📐 Inserarea formelor în PDF – Instrucțiuni rapide:

1. Selectați tipul de formă (dreptunghi, elipsă, linie, săgeată)
2. Faceți clic pe poziție
   - Dreptunghi/elipsă: un singur clic plasează forma
   - Linie/săgeată: două clicuri pentru punctul de început și sfârșit
3. Poziționați forma: trageți cu mouse-ul
4. Ajustați dimensiunea: trageți de colțuri/margini
5. Salvați forma: Enter
6. Eliminați forma: ESC
7. Alte ajustări: clic dreapta pe formă

Sfat: În meniul contextual puteți ajusta setările.
        """,
        'form_inserted': "{0} inserat(ă) pe pagina {1}",
        'form_deleted': "Formă ștearsă",
        'form_copied': "Formă copiată",
        'form_pasted': "Formă inserată",
        'form_saved': "{0} forme au fost inserate în PDF.\n\nPDF-ul a fost reîncărcat...",
        'form_saved_voice': "{0} forme salvate",
        'form_reset': "Formă readusă la dimensiunea implicită",
        'form_transparent_on': "activat",
        'form_transparent_off': "dezactivat",
        'form_transparent_toggled': "Fundal transparent {0}",
        'form_line_cancel': "Desenare linie anulată",
        'form_second_click': "Acum faceți clic pe punctul final pentru {0}",
        'mode_replace_form': "Inserați formă",
        'mode_conflict_voice_form': "Modul {0} este activ. Ieșiți și inserați forma?",
        'form_settings_updated': "Setări forme actualizate",
        'form_unknown': "Formă",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Faceți clic pe poziția de start",
        'form_line_guide_2': "2. Faceți clic pe poziția de sfârșit",
        'form_line_guide_3': "Linia va fi desenată între cele două puncte.",
        'form_line_status_1': "Așteptare primul clic...",
        'form_line_status_2': "Primul punct setat: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Acum faceți clic pe punctul final...",
        'form_line_status_4': "Ambele puncte setate.\nFaceți clic pe 'Gata' pentru a salva.",
        'form_line_reset': "Resetați",
        'form_line_finish': "Gata",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Copiază (Cmd+C)",
        'paste': "Inserare (Cmd+V)",
        'copied': "Copiat: {0}",
        'no_element_to_copy': "Niciun element selectat pentru copiere",
        'no_copied_data': "Nicio dată copiată",
        'no_valid_position': "Nicio poziție validă pentru inserare",
        'copy_text': "Text copiat",
        'copy_image': "Imagine copiată",
        'copy_form': "Formă copiată",
        'copy_signature': "Semnătură copiată",
        'element_text': "Text",
        'element_image': "Imagine",
        'element_form': "Formă",
        'element_signature': "Semnătură",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Conflict de mod",
        'mode_conflict_message': "Modul '{0}' este deja activ.\n\nDoriți să ieșiți din el și să {1}?",
        'mode_replace': "Ieșiți din mod și {0}",
        'mode_cancel': "Anulează",
        'mode_replace_text': "inserați text",
        'mode_replace_cross': "inserați cruce",
        'mode_replace_signature': "inserați semnătură",
        'mode_replace_image': "inserați imagine",
        'mode_replace_form': "inserați formă",
        'mode_conflict_voice': "Modul {0} este activ. Ieșiți și inserați text?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Introducere text",
        'active_mode_signature': "Semnătură",
        'active_mode_image': "Imagine",
        'active_mode_form': "Formă",
        'active_mode_and': " și ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Inserare",
        'insert_another_text': "Inserare text",
        'insert_another_cross': "Inserare cruce",
        'insert_another_signature_1': "Semnătura 1",
        'insert_another_signature_2': "Semnătura 2",
        'insert_another_image': "Inserare imagine",
        'insert_another_form_rect': "Dreptunghi",
        'insert_another_form_ellipse': "Elipsă",
        'insert_another_form_line': "Linie (2 clicuri)",
        'insert_another_form_arrow': "Săgeată (2 clicuri)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Salvați {0}",
        'save_dialog_message': "{0} va fi salvat(ă) pe pagina {1}.\n\nCum doriți să continuați?",
        'save_all': "Salvați toate {0}",
        'save_single': "Salvați {0}",
        'save_customize': "Ajustați {0}",
        'save_discard': "Eliminați acest(ă) {0}",
        'save_continue': "Continuați editarea",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Mergi la pagina {0}",
        'context_rotate': " Rotește pagina {0}",
        'context_delete': " Șterge pagina {0}",
        'context_export': " Exportă pagina {0}",
        'context_mark_as': " Marcați pagina ca...",
        'context_mark_empty': " Pagină goală",
        'context_unmark_empty': " Nu mai este goală",
        'context_mark_export': " Marcați pentru export",
        'context_unmark_export': " Nu mai exportați",
        'context_batch_actions': " Acțiuni colective",
        'context_batch_delete_empty': " Ștergeți toate cele {0} pagini goale",
        'context_batch_export_single': " Exportați toate cele {0} pagini (un fișier)",
        'context_batch_export_split': " Exportați toate cele {0} pagini (separat)",
        'context_drag_start': " Porniți Drag & Drop",
        'context_drag_stop': " Opriți Drag & Drop",
        'context_insert': " Inserare",
        'context_insert_pages': " Inserați pagini",
        'context_zoom': "Zoom",
        'discard_mixed': "Eliminați toate {0} {1} și {2} {3}",
        'save_mixed': "Salvați {0} {1} și {2} {3}",
        'discard_texts': "Eliminați toate {0} texte",
        'discard_text_single': "Eliminați 1 text",
        'save_texts': "Salvați {0} texte",
        'save_text_single': "Salvați 1 text",
        'discard_crosses': "Eliminați toate {0} cruci",
        'discard_cross_single': "Eliminați 1 cruce",
        'save_crosses': "Salvați {0} cruci",
        'save_cross_single': "Salvați 1 cruce",
        'discard_signatures': "Eliminați toate {0} semnături",
        'save_signature_single': "Salvați 1 semnătură",
        'save_signatures': "Salvați {0} semnături",
        'discard_images': "Eliminați toate {0} imagini",
        'save_image_single': "Salvați 1 imagine",
        'save_images': "Salvați {0} imagini",
        'discard_forms': "Eliminați toate {0} forme",
        'save_form_single': "Salvați 1 formă",
        'save_forms': "Salvați {0} forme",
        'cross_discard': "Eliminați această cruce",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informații export / import",
        'export_what': "📋 Ce se exportă?",
        'export_general': "Setări generale",
        'export_general_items': "• Ieșire vocală (pornit/oprit, viteză)\n• Mod întunecat/luminos\n• Setări backup\n• Setări OCR",
        'export_image_form': "Setări imagini și forme",
        'export_image_form_items': "• Setări imagini (raport de aspect, dimensiune implicită)\n• Setări forme (grosime linie, culori)\n• Setări semnături (căi, dimensiuni, marcaj temporal)",
        'export_passwords': "Baza de date parole",
        'export_passwords_items': "• Toate parolele PDF salvate\n• Opțional criptate sau decriptate",
        'export_master': "Setări parolă master",
        'export_master_items': "• Hash parolă master\n• Setări pentru semnături/fragmente text",
        'export_signatures': "Semnături și fragmente text",
        'export_signatures_items': "• Toate fișierele imagine (semnături)\n• Toate fragmentele text cu formatare\n• Marcaje private/publice",
        'export_import_warning': "⚠️ Observații importante",
        'export_import_note': "• La import, TOATE setările curente sunt suprascrise\n• Este necesară repornirea aplicației\n• Semnăturile/fragmentele text existente sunt înlocuite",
        'export_master_note': "• Dacă este setată o parolă master, puteți alege:\n  - Decriptat (parole în text clar)\n  - Criptat (lizibil numai cu parola master)",
        'export_security': "• Fișierul ZIP exportat conține date confidențiale\n• Păstrați-l în siguranță (de ex. pe un stick USB criptat)\n• La pierderea fișierului, parolele sunt iremediabil pierdute",
        'export_format': "📁 Format export",
        'export_format_desc': "Setările sunt salvate într-un singur fișier ZIP:",
        'export_filename': "Setari_PDFDarkView_AAAALLZZ_HHMMSS.zip",
        'export_success': "Setările au fost exportate cu succes",
        'export_failed': "Export eșuat",
        'export_import_question': "Doriți să reporniți aplicația acum?",
        'export_password_question': "Este setată o parolă master.\n\nDoriți să exportați parolele decriptat?\n(altfel vor fi exportate criptat)",
        'export_decrypt': "Exportați decriptat",
        'export_encrypt': "Exportați criptat",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informații",
        'info_title': "Despre PDF Dark View",
        'info_version': "Versiune",
        'info_author': "Dezvoltat de Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Despre",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> este un vizualizator PDF accesibil, dezvoltat special pentru persoanele cu deficiențe de vedere.</p>

            <p><strong>Caracteristici principale:</strong></p>
            <ul>
                <li>Interfață cu contrast ridicat, personalizabilă</li>
                <li>Control complet prin tastatură</li>
                <li>Ieșire vocală integrată</li>
                <li>OCR pentru documente scanate</li>
                <li>Instrumente complete de editare</li>
            </ul>

            <p>Sunt acceptate peste 50 de limbi – astfel încât PDF-urile să fie accesibile pentru toată lumea.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funcționalități",
        'info_features_intro': "PDF Dark View vă oferă următoarele posibilități:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Vizualizare și navigare</strong> – Mod întunecat/deschis, răsfoire pagini, zoom, salt la pagină</li>
            <li><strong>OCR (recunoaștere text)</strong> – Faceți documentele scanate căutabile și copiabile</li>
            <li><strong>Editare</strong> – Inserați text, cruci, semnături, imagini și forme</li>
            <li><strong>Gestionare pagini</strong> – Ștergere, extragere, inserare, mutare prin tragere și plasare</li>
            <li><strong>Export</strong> – În Word, Pages sau ca text</li>
            <li><strong>Securitate</strong> – Protecție și gestionare prin parolă</li>
            <li><strong>Accesibilitate</strong> – Ieșire vocală, control prin tastatură, contrast ridicat</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Operare",
        'info_accessibility': "♿ Accesibilitate – control complet prin tastatură",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 General</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Deschide PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Caută</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Comută modul întunecat/deschis</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Imprimă</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Ieșire</div>

        <div class="shortcut-cat">📖 Navigare</div>
        <div class="shortcut-row"><kbd>Tastele săgeată</kbd> Răsfoiește pagină cu pagină</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Mergi la pagina</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Prima pagină</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Ultima pagină</div>

        <div class="shortcut-cat">✏️ Editare</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Inserare text</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Șterge pagini</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extrage pagini</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Inserare pagini</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Mută pagini</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rotește pagina</div>

        <div class="shortcut-cat">🖼️ Mutarea elementelor</div>
        <div class="shortcut-row"><kbd>Tastele săgeată</kbd> Mută text/Imagine/semnătură</div>
        <div class="shortcut-row"><kbd>Ctrl+Tastele săgeată</kbd> Pași mai mari</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Salvează</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Renunță</div>

        <div class="shortcut-cat">🗣️ Ieșire vocală</div>
        <div class="shortcut-row"><kbd>F2</kbd> Pornește/oprește ieșirea vocală</div>
        """,
        'info_contextmenu': "📌 Important: Toate funcțiile sunt accesibile și prin meniul contextual (butonul dreapta al mouse-ului)!",
        'info_accessibility_hint': "💡 Sfat: Ieșirea vocală (F2) facilitează orientarea și oferă feedback despre meniuri și ferestrele de dialog.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licență & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Informații conform § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germania<br>
        E-mail: binhdiez64@gmail.com<br>
        Responsabil pentru conținut: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Declinarea răspunderii</strong><br>
        Software-ul a fost dezvoltat cu cea mai mare atenție. Nu se oferă nicio garanție pentru corectitudinea, exhaustivitatea și funcționalitatea. Utilizarea se face pe propriul risc.<br><br>

        <strong>📄 Licența MIT (utilizare privată)</strong><br>
        Drepturi de autor (c) 2026 Toralf Schulz (BinhDiez)<br>
        Permis: utilizare gratuită, modificări private, copii personale.<br>
        Nepermis: vânzare, utilizare comercială, eliminarea notificărilor de drepturi de autor.<br><br>

        <strong>🔧 Componente terțe</strong><br>
        Acest software conține componente sub licențele GPL, AGPL, Apache 2.0, BSD și MIT.<br>
        La redistribuire, trebuie respectate termenii de licență corespunzători.<br><br>

        <strong>🌐 Open Source</strong><br>
        Codul sursă este disponibil și poate fi vizualizat, modificat și redistribuit în conformitate cu termenii de licență corespunzători.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Mulțumiri",
        'info_credits': "Mulțumiri comunității open-source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Procesare PDF</li>
            <li><strong>PyQt5</strong> – Interfață grafică</li>
            <li><strong>Tesseract OCR</strong> – Recunoaștere text</li>
            <li><strong>OCRmyPDF</strong> – Integrare OCR</li>
            <li><strong>python-docx</strong> – Export în Word</li>
            <li><strong>qtawesome</strong> – Pictograme</li>
            <li><strong>DeepSeek</strong> – Suport pentru traduceri (50+ limbi)</li>
            <li><strong>Tuturor utilizatorilor</strong> – Pentru feedback-ul valoros</li>
            <li><strong>Comunității open-source</strong> – Pentru bibliotecile excelente</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Limbi",
        'info_languages_header': "🌍 Suport lingvistic",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View acceptă în prezent <strong>62 de limbi</strong> – astfel încât software-ul poate fi utilizat accesibil în întreaga lume.</p>

            <p><strong>📖 Lista completă a limbilor (Stare: martie 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albaneză (Shqip)</li>
                    <li>🇩🇿 Arabă (العربية)</li>
                    <li>🇮🇩 Balineză (Basa Bali)</li>
                    <li>🇧🇩 Bengală (বাংলা)</li>
                    <li>🇲🇲 Birmană (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosniacă (Bosanski)</li>
                    <li>🇧🇬 Bulgară (Български)</li>
                    <li>🇨🇳 Chineză (中文)</li>
                    <li>🇩🇰 Daneză (Dansk)</li>
                    <li>🇩🇪 Germană (Deutsch)</li>
                    <li>🇬🇧 Engleză (English)</li>
                    <li>🇪🇪 Estonă (Eesti)</li>
                    <li>🇫🇮 Finlandeză (Suomi)</li>
                    <li>🇫🇷 Franceză (Français)</li>
                    <li>🇬🇷 Greacă (Ελληνικά)</li>
                    <li>🇮🇱 Ebraică (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croată (Hrvatski)</li>
                    <li>🇭🇺 Maghiară (Magyar)</li>
                    <li>🇮🇩 Indoneziană (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandeză (Gaeilge)</li>
                    <li>🇮🇸 Islandeză (Íslenska)</li>
                    <li>🇮🇹 Italiană (Italiano)</li>
                    <li>🇯🇵 Japoneză (日本語)</li>
                    <li>🇰🇭 Khmeră (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Coreeană (한국어)</li>
                    <li>🇱🇦 Laoțiană (ພາສາລາວ)</li>
                    <li>🇱🇻 Letonă (Latviešu)</li>
                    <li>🇱🇹 Lituaniană (Lietuvių)</li>
                    <li>🇱🇺 Luxemburgheză (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaeză (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolă (Монгол)</li>
                    <li>🇳🇵 Nepaleză (नेपाली)</li>
                    <li>🇳🇱 Olandeză (Nederlands)</li>
                    <li>🇳🇴 Norvegiană (Norsk)</li>
                    <li>🇦🇫 Paștună (پښتو)</li>
                    <li>🇮🇷 Persană (فارسی)</li>
                    <li>🇵🇱 Poloneză (Polski)</li>
                    <li>🇵🇹 Portugheză (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Română (Română)</li>
                    <li>🇷🇺 Rusă (Русский)</li>
                    <li>🇸🇪 Suedeză (Svenska)</li>
                    <li>🇷🇸 Sârbă (Српски)</li>
                    <li>🇸🇰 Slovacă (Slovenčina)</li>
                    <li>🇸🇮 Slovenă (Slovenščina)</li>
                    <li>🇪🇸 Spaniolă (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamilă (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thailandeză (ไทย)</li>
                    <li>🇨🇿 Cehă (Čeština)</li>
                    <li>🇹🇷 Turcă (Türkçe)</li>
                    <li>🇺🇦 Ucraineană (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnameză (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Idiș (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Adăugați propriile limbi:</strong><br>
                Doriți o limbă care nu este încă inclusă? Pur și simplu plasați propriul fișier de dicționar (<code>sprache_xx.py</code>) lângă aplicație – software-ul îl va recunoaște automat. Dacă sunteți interesat de o traducere specială, nu ezitați să mă contactați.
            </div>

            <p><strong>🙏 Mulțumiri speciale:</strong> DeepSeek pentru sprijinul în traducerea tuturor dicționarelor în 62 de limbi.</p>

            <p>📧 Contact pentru traduceri: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Eroare",
        'error_occurred': "A apărut o eroare",
        'error_pdf_load': "Eroare la încărcarea PDF-ului",
        'error_pdf_save': "Eroare la salvarea PDF-ului",
        'error_ocr': "Eroare la recunoașterea textului",
        'error_no_pdf': "Niciun PDF încărcat",
        'error_page_not_found': "Pagina nu a fost găsită",
        'error_invalid_range': "Interval de pagini invalid",
        'error_file_not_found': "Fișierul nu a fost găsit",
        'error_permission': "Nu aveți permisiunea necesară",
        'error_unknown': "Eroare necunoscută",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Succes",
        'success_operation': "Operațiune finalizată cu succes",
        'success_saved': "Salvat cu succes",
        'success_exported': "Exportat cu succes",
        'success_imported': "Importat cu succes",
        'success_deleted': "Șters cu succes",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Confirmare",
        'confirm_yes': "Da",
        'confirm_no': "Nu",
        'confirm_ok': "OK",
        'confirm_cancel': "Anulează",
        'confirm_delete': "Șterge",
        'confirm_overwrite': "Suprascrie",
        'confirm_continue': "Continuă",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Se încarcă PDF-ul...",
        'progress_saving': "Se salvează PDF-ul...",
        'progress_exporting': "Se exportă PDF-ul...",
        'progress_processing': "Procesare în curs...",
        'progress_wait': "Vă rugăm așteptați...",
        'progress_preparing': "Pregătire...",
        'progress_finalizing': "Finalizare...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Alb",
        'color_black': "Negru",
        'color_red': "Roșu",
        'color_green': "Verde",
        'color_blue': "Albastru",
        'color_yellow': "Galben",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Portocaliu",
        'color_gray': "Gri",
        'color_custom': "Alegere culoare",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fișier",
        'menu_edit': "&Editare",
        'menu_view': "&Vizualizare",
        'menu_tools': "&Instrumente",
        'menu_settings': "&Setări",
        'menu_help': "&Ajutor",
        'menu_language': "🌐 Limbă",
        'menu_guides': "&Instrucțiuni",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Deschideți",
        'file_save_as': "&Salvați ca...",
        'file_protect': "&Protejați documentul...",
        'file_export': "&Exportați",
        'file_export_pages': "Exportați în Pages",
        'file_export_word': "Exportați în DOCX",
        'file_export_text': "Exportați în TXT",
        'file_print_now': "&Tipăriți imediat",
        'file_print': "&Tipăriți",
        'file_close': "&Închideți",
        'file_quit': "&Ieșiți",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Căutați",
        'edit_ocr': " Efectuați OCR",
        'edit_rotate': "&Rotiți pagina",
        'edit_rotate_all': "&Rotiți toate paginile",
        'edit_delete_pages': "&Ștergeți pagini",
        'edit_extract_pages': "&Extrageți pagini",
        'edit_insert_pages': "&Inserați pagini",
        'edit_move_pages': "&Mutați pagini",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Inserați text și cruci",
        'text_insert': " Inserați text",
        'cross_insert': " Inserați cruce",
        'text_customize': " Ajustați textul",
        'cross_customize': " Ajustați această cruce",
        'cross_customize_all': " Ajustați toate crucile",
        'text_discard': " Eliminați acest text / această cruce",
        'text_discard_all': " Eliminați toate textele și crucile",
        'text_save_all': " Salvați toate textele și crucile",
        'text_guide': " Introducere text / fragmente text – instrucțiuni",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Inserați semnătură",
        'signature_settings_menu': " Setări...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Inserați imagine",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Inserați forme",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Afișați fereastra text",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Lățime pagină (implicit)",
        'view_zoom_two': "&Două pagini",
        'view_zoom_overview': "&Prezentare generală (mai multe pagini)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Accesibilitate",
        'settings_voice': "Ieșire vocală",
        'settings_voice_tooltip': "completează informațiile cititoarelor de ecran cu date suplimentare",
        'settings_signature': "&Setări semnături",
        'settings_password': "&Gestionare parole",
        'settings_backup': "Creați backup înainte de modificări",
        'settings_export_import': "&Exportați setări / importați setări",
        'settings_export': "&Exportați toate setările...",
        'settings_import': "&Importați toate setările...",
        'settings_export_info': "&Ce se exportă?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "pornit",
        'voice_off': "oprit",
        'voice_toggle': "Ieșire vocală {0}",
        'voice_speed': "Viteză {0} la sută",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Instrumentul nu a fost găsit:\n{0}\n\nBASE_DIR: {1}\nAsigurați-vă că instrumentele PDF sunt instalate în directorul {1}.",
        'tool_started': "{0} pornit",
        'tool_start_failed': "Nu a putut fi pornit",
        'process_error_failed_to_start': "Procesul nu a putut fi pornit. Există fișierul?",
        'process_error_crashed': "Procesul s-a prăbușit în timpul pornirii.",
        'process_error_timeout': "S-a atins limita de timp a procesului.",
        'process_error_write': "Eroare de scriere în proces.",
        'process_error_read': "Eroare de citire în proces.",
        'process_error_unknown': "Eroare de proces necunoscută",
        'process_command': "Comandă",
        'process_normal_exit': "terminat normal",
        'process_crashed': "s-a prăbușit",
        'process_nonzero_exit': "{0} s-a terminat cu codul de eroare {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Se anulează...",
        'move_cancelling': "Mutarea se anulează",
        'opening_pdf': "Se deschide PDF-ul...",
        'loading_document': "Se încarcă documentul...",
        'pdf_opened': "PDF deschis",
        'pages_found_moving': "{0} pagini găsite, {1} de mutat",
        'creating_backup': "Se creează backup...",
        'backup_description': "Se face backup fișier original...",
        'backup_saved_as': "Backup salvat ca: {0}",
        'error_format': "Eroare: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Căutare resetată",
        'page_header_simple': "=== Pagina {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Gestionare parole – Instrucțiuni",
        'password_guide_voice': "Instrucțiuni pentru gestionarea parolelor. Vă rugăm să citiți observațiile.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Gestionare parole – Instrucțiuni detaliate</strong></p>

        <p><strong>1. Protecția PDF-urilor cu parolă</strong></p>
        <ul>
        <li>La deschiderea unui PDF protejat cu parolă, apare un dialog în care puteți introduce parola.</li>
        <li>Puteți salva parola în mod criptat pentru a nu fi nevoie să o introduceți de fiecare dată (caseta „Salvați parola”).</li>
        <li>Cu butonul „Eliminați parola” puteți crea o copie decriptată a PDF-ului și șterge parola din baza de date.</li>
        </ul>

        <p><strong>2. Parola master</strong></p>
        <ul>
        <li>Parola master protejează accesul la toate parolele PDF salvate.</li>
        <li><strong>Configurare:</strong> Accesați „Setări → Gestionare parole → Setări parolă master” și faceți clic pe „Configurați parola master”. Alegeți o parolă puternică (cel puțin 8 caractere).</li>
        <li><strong>Schimbare:</strong> După autentificarea cu succes, puteți schimba parola master.</li>
        <li><strong>Eliminare:</strong> Dacă ștergeți parola master, TOATE parolele salvate sunt șterse ireversibil. Puteți exporta o copie de rezervă înainte.</li>
        <li>O dată pe sesiune, trebuie să vă autentificați cu parola master pentru a accesa funcțiile protejate (de ex. afișarea parolelor).</li>
        </ul>

        <p><strong>3. Gestionarea parolelor (listă)</strong></p>
        <ul>
        <li>În „Setări → Gestionare parole” se deschide un tabel cu toate PDF-urile salvate și parolele lor criptate.</li>
        <li><strong>Fără parolă master:</strong> Puteți doar șterge intrări – parolele rămân ascunse.</li>
        <li><strong>Cu parolă master (autentificat):</strong> Puteți afișa, copia, exporta și șterge parolele.</li>
        <li><strong>Export:</strong> Alegeți un format (JSON, CSV, TXT) și salvați lista. Dacă este setată o parolă master, puteți decide dacă parolele sunt exportate decriptat sau criptat.</li>
        <li><strong>Import:</strong> Un fișier ZIP exportat anterior (toate setările) poate fi reimportat prin „Setări → Exportați setări / importați setări”. Atenție: datele existente sunt suprascrise!</li>
        </ul>

        <p><strong>4. Generator de parole</strong></p>
        <ul>
        <li>În dialogul parolei (de ex. la protejarea unui PDF), în dreapta câmpului de intrare se află un buton cu zar 🎲.</li>
        <li>Faceți clic pe el pentru a deschide generatorul de parole. Puteți seta lungimea, seturile de caractere (litere mari, litere mici, cifre, caractere speciale) și un separator pentru o lizibilitate mai bună.</li>
        <li>Parola generată poate fi preluată direct și, dacă este necesar, copiată.</li>
        </ul>

        <p><strong>5. Observații importante de securitate</strong></p>
        <ul>
        <li>Parolele salvate sunt stocate criptat cu AES-256. Cheia este derivată din parola master (dacă este setată) sau dintr-o valoare fixă (fără parolă master).</li>
        <li>Fără parolă master, parolele sunt criptate, dar cheia este încorporată în program – un atacator cu acces la fișierele dvs. le-ar putea decripta. De aceea, recomandăm insistent utilizarea unei parole master.</li>
        <li>Baza de date a parolelor se află în fișierul `Data/passwords.json`. Faceți copii de rezervă regulate, mai ales înainte de a elimina parola master.</li>
        <li>La pierderea parolei master, toate parolele salvate sunt pierdute iremediabil.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Mod de inversare",
        'invert_mode_classic': "Clasic (inversează toate culorile)",
        'invert_mode_smart': "Inteligent (inversează doar luminozitatea)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Pragul de scară de gri",
        'gray_threshold_10': "10% (strict)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Implicit)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (moale)",
        'threshold_changed': "Pragul setat la {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Pragul de scară de gri – Explicație",
        'threshold_guide_text': "Pragul de scară de gri determină care pixeli în modul întunecat inteligent sunt considerați 'gri' și sunt inversați.\n\n"
                                "• O valoare scăzută (10%) inversează doar tonurile de gri aproape perfecte – elementele colorate rămân complet păstrate.\n"
                                "• O valoare ridicată (50%) inversează și pixelii ușor colorați – aceasta crește contrastul, dar poate denatura culorile.\n\n"
                                "Valoarea optimă depinde de document. Pentru documente pur text, 30–40% este adesea ideală, pentru grafică colorată mai degrabă 10–20%.\n\n"
                                "Puteți ajusta valoarea în orice moment prin meniul 'Setări' – PDF-ul va fi reîncărcat imediat.\n\n"
                                "Observație:\n* Fotografiile și imaginile pot fi afișate corect doar în modul deschis!\n* Setările de inversare sunt afișate numai când modul întunecat este activat.",
        'threshold_guide_voice': "Pragul de scară de gri determină cât de puternic intervine modul întunecat inteligent. O valoare scăzută protejează culorile, o valoare ridicată mărește contrastul.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Se deschide PDF-ul...",
        'progress_loading_document': "Se încarcă documentul...",
        'progress_pdf_opened': "PDF deschis",
        'progress_creating_backup': "Se creează copia de rezervă...",
        'progress_backup_description': "Se asigură fișierul original...",
        'progress_backup_created': "Copie de rezervă creată",
        'progress_backup_saved_as': "Salvat ca: {0}",
        'progress_analyzing_start': "Se începe analiza...",
        'progress_searching_empty': "Se caută pagini goale...",
        'progress_page_empty': "Pagina {0} este goală",
        'progress_page_keep': "Păstrează pagina {0}",
        'progress_analysis_complete': "Analiza finalizată",
        'progress_empty_found': "Găsite {0} pagini goale",
        'progress_current_page': "Pagina curentă",
        'progress_mark_delete': "Se marchează pentru ștergere",
        'progress_range_selected': "Interval pagini {0}-{1}",
        'progress_deleting_pages': "Se șterg {0} pagini",
        'progress_creating_new_pdf': "Se creează PDF nou...",
        'progress_transferring_pages': "Se transferă paginile",
        'progress_keeping_page': "Pagina {0} va fi păstrată ({1}/{2})",
        'progress_saving_pdf': "Se salvează PDF-ul...",
        'progress_optimizing': "Se optimizează dimensiunea fișierului...",
        'progress_finalizing': "Se finalizează...",
        'progress_new_size': "Dimensiune nouă: {0:.2f} MB",
        'progress_cancelling': "Se anulează...",
        'progress_cancel_message': "{0} se anulează",
        'progress_pages_found_moving': "Găsite {0} pagini, {1} pentru mutare",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Se analizează PDF-ul...",
        'ocr_status_optimizing': "Optimizarea imaginii în desfășurare...",
        'ocr_status_recognizing': "Recunoașterea textului în desfășurare...",
        'ocr_status_embedding': "Se încorporează textul...",
        'ocr_status_finalizing': "Se finalizează PDF-ul...",

        # PDF-Laden
        'progress_preparing': "Se pregătește...",
        'progress_loading': "Se încarcă PDF-ul...",

        # Seitenoperationen
        'progress_deleting_title': "Se șterg paginile...",
        'progress_moving_title': "Se mută paginile...",
        'pages_found': "Pagini găsite",
        'progress_creating_new_order': "Se creează o nouă ordine...",
        'progress_sorting_pages': "Se sortează paginile...",
        'progress_moving_to_begin': "Mută {0} pagini la început",
        'progress_transferring_count': "Transferă {0} pagini",
        'progress_transferring_before_target': "Transferă paginile înaintea țintei",
        'progress_moving_pages': "Mută {0} pagini",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_copie_rezerva_",
        'filename_protected_suffix': "_protejat_",
        'filename_copy_suffix': "_Copie",
        'filename_page_single': "_Pagina_",
        'filename_page_range': "_Pagini_",
        'filename_export_page': "_Pagina_{0:03}",
        'filename_export_range': "_Pagini_{0}-{1}",
        'filename_export_multiple': "_Pagini_{0}",
        'filename_with_text': "_cu_Text",
        'filename_with_signature': "_cu_Semnatura",
        'filename_with_image': "_cu_Imagine",
        'filename_with_forms': "_cu_Forme",
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
        'view_toggle_navbar': "Afișează bara de butoane",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Nu se pot șterge toate paginile",
		'pages_cannot_delete_last_page': 'Ultima pagină nu poate fi ștearsă!',
		'pages_cannot_delete_all_pages': 'Cel puțin o pagină trebuie să rămână în document!',
		'delete_pages_confirm': 'Sigur doriți să ștergeți {0} pagini?',
		'delete_pages_confirm_voice': 'Sigur doriți să ștergeți {0} pagini?',
		'pages_deleted': '{0} pagini au fost șterse cu succes.',
		'warning': 'Avertisment',
		'error': 'Eroare',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Niciun formular selectat",
        'form_customized': "Formular personalizat",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Selectează",
        'btn_use': "Folosește",
        'master_password_for_spasswords': "Pentru a stoca și utiliza parole, trebuie mai întâi să configurați o parolă principală.\n\nDoriți să configurați parola principală acum?",
        'open_saved_dialog_title': "Deschide fișierul salvat",
        'open_saved_question': "Doriți să deschideți fișierul salvat acum?",
        'password': "Parolă",
        'password_manager_master_required': "Managerul de parole este disponibil doar dacă a fost configurată o parolă principală.\n\nDoriți să configurați parola principală acum?",
        'password_master_required_for_select': "Pentru a vizualiza și selecta parolele salvate, trebuie mai întâi să vă autentificați cu parola dvs. principală.\n\nDoriți să vă autentificați acum?",
        'password_not_available': "Parola selectată nu este disponibilă sau nu a putut fi decriptată.",
        'password_options_title': "Opțiuni parolă",
        'password_save_choice_change': "Setează parolă nouă",
        'password_save_choice_keep': "Folosește parola existentă",
        'password_save_choice_none': "Salvează necriptat",
        'password_save_hint': "Configurați mai întâi o parolă principală pentru a stoca parolele în siguranță.",
        'password_save_master_required': "Salvează parola (posibil doar cu parola principală)",
        'password_save_question': "PDF-ul curent este protejat prin parolă. Doriți să folosiți parola existentă, să setați una nouă sau să salvați necriptat?",
        'password_select': "Selectează parola",
        'password_select_none': "Nicio parolă selectată.\n\nVă rugăm să selectați o parolă din listă.",
        'password_select_one': "Vă rugăm să selectați exact o parolă.\n\nAți marcat mai multe parole.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_copie_de_siguranta",
        'filename_insert_suffix': "_cu_inserare",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_pagini_sterse",
        'filename_pages_moved': "_pagini_mutate",
        'filename_rotated_all_suffix': "_toate_paginile_rotite",
        'filename_rotated_suffix': "_pagina_rotita",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configurarea numelor de fișiere la modificarea PDF-ului",
        'filename_keep_suffixes': "Păstrează extensiile anterioare (ex., _cu_text)",
        'filename_keep_suffixes_false': "Înlocuiește",
        'filename_keep_suffixes_true': "Păstrează",
        'filename_preview_label': "Previzualizarea numelui fișierului:",
        'filename_preview_overwrite_hint': "Previzualizare indisponibilă – originalul va fi suprascris.",
        'filename_separator': "Separator între cuvinte",
        'filename_separator_none': "Fără separator",
        'filename_separator_space': "Spațiu ( )",
        'filename_separator_underscore': "Linie de subliniere (_)",
        'filename_settings_saved': "Setările numelui fișierului au fost salvate",
        'filename_settings_title': "Formatarea numelui fișierului și copia de siguranță",
        'filename_timestamp_position': "Poziția marcajului temporal",
        'filename_timestamp_position_after': "După numele de bază",
        'filename_timestamp_position_before': "Chiar în față",
        'filename_timestamp_position_end': "La sfârșit",
        'filename_use_timestamp': "Folosește marcaj temporal",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Comportament la modificări:</b><ul><li>Ștergerea și inserarea paginilor</li><li>Inserarea textului, semnăturii, imaginii și formelor</li><li>OCR</li></ul></html>",
        'backup_section': "Copie de siguranță pentru operațiile cu pagini (Ștergere, Mutare)",
        'behavior_info': "Notă: La 'Suprascrie original', marcajele temporale și sufixele sunt ignorate – fișierul își păstrează numele.",
        'behavior_new_file': "Creează întotdeauna un fișier nou (cu marcaj temporal și sufix)",
        'behavior_overwrite': "Suprascrie original (fără fișier nou)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Toate paginile au fost rotite.\n\nOriginalul a rămas neschimbat.\nFișier nou: {0}",
        'all_pages_rotated_voice': "Toate paginile rotite, fișier nou creat.",
        'empty_pages_deleted_new_file': "{0} pagini goale au fost șterse.\n\nOriginalul a rămas neschimbat.\nFișier nou: {1}",
        'empty_pages_deleted_voice': "{0} pagini goale șterse, fișier nou creat.",
        'ocr_keep_original': "Păstrează originalul (deschide manual mai târziu)",
        'ocr_new_file_question': "Noul PDF căutabil a fost salvat la:\n{0}\n\nDoriți să îl deschideți acum?",
        'ocr_open_new': "Deschide fișierul OCR nou",
        'ocr_original_kept': "Fișierul original rămâne deschis. Fișierul OCR a fost salvat.",
        'page_deleted_new_file': "Pagina {0} a fost ștearsă.\n\nOriginalul a rămas neschimbat.\nFișier nou: {1}",
        'page_deleted_voice': "Pagina {0} ștearsă, fișier nou creat.",
        'page_rotated_new_file': "Pagina {0} a fost rotită.\n\nOriginalul a rămas neschimbat.\nFișier nou: {1}",
        'page_rotated_voice': "Pagina {0} rotită, fișier nou creat.",
        'pages_deleted_new_file': "{0} pagini au fost șterse.\n\nFișierul original a rămas neschimbat.\nFișier nou: {1}",
        'pages_deleted_new_file_voice': "{0} pagini șterse, fișier nou creat.",
        'pages_inserted_new_file': "{0} pagini au fost inserate.\n\nFișierul original a rămas neschimbat.\nFișier nou: {1}",
        'pages_inserted_new_file_ask': "{0} pagini au fost inserate.\n\nOriginalul a rămas neschimbat.\nFișier nou: {1}\n\nDoriți să îl deschideți acum?",
        'pages_inserted_voice_new': "{0} pagini inserate, fișier nou creat.",
        'pages_moved_new_file': "{0} pagini au fost mutate.\n\nFișierul original a rămas neschimbat.\nFișier nou: {1}",
        'pages_moved_new_file_voice': "{0} pagini mutate, fișier nou creat.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Nu mai afișa",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Setare copie de siguranță</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Copie de siguranță ACTIVATĂ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">La toate modificările care suprascriu originalul</strong> (text, semnătură, imagine, formă, OCR, rotire, inserare, ștergere/mutare pagini) se creează <strong>automat o copie de siguranță cu marcaj temporal</strong> înainte de aplicarea modificării.</p>
                <p style="margin: 5px 0 5px 20px;">• Copia de siguranță se află lângă fișierul original (ex., <code>Document_copie_de_siguranta_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Dacă ați activat suplimentar opțiunea <strong>„Suprascrie original“</strong>, se creează, de asemenea, o copie de siguranță.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Copie de siguranță DEZACTIVATĂ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Nu se creează nicio copie de siguranță</strong> – nici la suprascriere, nici la operațiile cu pagini.</p>
                <p style="margin: 5px 0 5px 20px;">• Fișierul original poate fi pierdut ireversibil la suprascriere.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Recomandat doar pentru utilizatorii experimentați!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Sfat:</strong> Setarea copiei de siguranță este independentă de opțiunea „Suprascrie original“. Puteți combina ambele.<br>
                Puteți ascunde acest mesaj permanent.
            </div>
        </div>
        """,
        'backup_info_title': "Comportamentul copiei de siguranță",
        'backup_info_voice': "Notificare despre comportamentul copiei de siguranță la operațiile cu pagini. Copie de siguranță activată suprascrie originalul, copie de siguranță dezactivată creează fișier nou.",
        'show_backup_info': "Informații despre setarea copiei de siguranță",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Nu mai afișa",
        'overwrite_enable_backup': "Activează copia de siguranță (recomandat)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Suprascrie original</p>
            <p>Dacă activați această opțiune, modificările (text, semnătură, imagine, formă, OCR, rotire, inserare) sunt <strong>salvate direct în original</strong> – <strong>nu se creează niciun fișier nou</strong>.</p>
            <p>• Numele fișierului rămâne neschimbat.<br>
            • Marcajele temporale și sufixele sunt ignorate.<br>
            • <strong>Fără copie de siguranță, originalul poate fi pierdut ireversibil.</strong></p>
            <p style="color: #FFD700;">Recomandare: Activați suplimentar opțiunea de copie de siguranță pentru a obține copii de siguranță automate.</p>
        </div>
        """,
        'overwrite_info_title': "Suprascrie original",
        'overwrite_info_voice': "Avertisment: Suprascrie original – niciun fișier nou. Copia de siguranță este recomandată.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} pagini au fost inserate.\n\nFișierul original a fost suprascris.\nS-a creat o copie de siguranță.",
        'pages_inserted_overwrite_no_backup': "{0} pagini au fost inserate.\n\nFișierul original a fost suprascris.\nNU s-a creat nicio copie de siguranță.",
        'texts_saved_overwrite_with_backup': "Modificările au fost salvate în original.\n\nS-a creat o copie de siguranță.",
        'texts_saved_overwrite_no_backup': "Modificările au fost salvate în original.\n\nNU s-a creat nicio copie de siguranță.",
        'texts_crosses_saved_new_file': "{0} {1} și {2} {3} au fost inserate.\n\nFișierul original a rămas neschimbat.\nS-a creat un fișier nou.\n\nSe încarcă noul PDF...",
        'texts_saved_new_file': "{0} {1} au fost inserate.\n\nFișierul original a rămas neschimbat.\nS-a creat un fișier nou.\n\nSe încarcă noul PDF...",
        'crosses_saved_new_file': "{0} {1} au fost inserate.\n\nFișierul original a rămas neschimbat.\nS-a creat un fișier nou.\n\nSe încarcă noul PDF...",
        'elements_saved_new_file': "{0} elemente au fost inserate.\n\nFișierul original a rămas neschimbat.\nS-a creat un fișier nou.\n\nSe încarcă noul PDF...",
        'signatures_saved_overwrite_with_backup': "Semnătura(ele) a(u) fost salvată(e) în original.\n\nS-a creat o copie de siguranță.",
        'signatures_saved_overwrite_no_backup': "Semnătura(ele) a(u) fost salvată(e) în original.\n\nNU s-a creat nicio copie de siguranță.",
        'images_saved_overwrite_with_backup': "Imaginea(imaginile) a(u) fost salvată(e) în original.\n\nS-a creat o copie de siguranță.",
        'images_saved_overwrite_no_backup': "Imaginea(imaginile) a(u) fost salvată(e) în original.\n\nNU s-a creat nicio copie de siguranță.",
        'forms_saved_overwrite_with_backup': "Forma(formele) a(u) fost salvată(e) în original.\n\nS-a creat o copie de siguranță.",
        'forms_saved_overwrite_no_backup': "Forma(formele) a(u) fost salvată(e) în original.\n\nNU s-a creat nicio copie de siguranță.",
        'signatures_saved_new_file': "{0} semnături au fost inserate.\n\nFișierul original a rămas neschimbat.\nS-a creat un fișier nou.\n\nSe încarcă noul PDF...",
        'images_saved_new_file': "{0} imagini au fost inserate.\n\nFișierul original a rămas neschimbat.\nS-a creat un fișier nou.\n\nSe încarcă noul PDF...",
        'forms_saved_new_file': "{0} forme au fost inserate.\n\nFișierul original a rămas neschimbat.\nS-a creat un fișier nou.\n\nSe încarcă noul PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Avertisment: Acest PDF conține pagini rotite. Poziționarea poate fi diferită.",
        'page_rotated_warning_title': "Pagină rotită detectată",
        'page_rotated_warning_message': "Pagina curentă {0} este rotită cu {1}°.\n\nInserarea de elemente pe pagini rotite nu este acceptată.\n\nDoriți să rotiți pagina acum în poziție verticală?",
        'page_rotated_warning_voice': "Avertisment: Pagina este rotită. Vă rugăm să o rotiți mai întâi.",
        'paste_on_rotated_page_simple_warning': "Inserarea pe pagina {0} nu este posibilă!\n\nAceastă pagină este rotită cu {1}°.\n\nVă rugăm să rotiți mai întâi pagina la 0° (Meniu: Editare → Aliniază pagina).\n\nAvertisment:\nElementul copiat anterior se va pierde dacă nu salvați înainte de a roti pagina.",
        'paste_on_rotated_page_voice': "Inserare anulată. Pagina este rotită. Vă rugăm să aliniați mai întâi pagina.",
        'page_rotated_cancel': "Anulează",
        'page_rotated_rotate_until_upright': "Rotește pagina în mod repetat (până când este verticală)",
        'page_rotated_now_upright': "Pagina este acum verticală. Acum puteți insera.",
        'page_rotated_still_not_upright': "Pagina nu a putut fi rotită în poziție verticală. Vă rugăm să corectați manual.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Ajutor: Corectați paginile rotite",
        'help_rotated_pages_voice': "Se deschide ajutorul pentru corectarea paginilor rotite.",
        'btn_help': "Ajutor",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problemă: Pagină rotită – Inserarea nu funcționează corect</p>

            <p>Dacă inserarea textelor, semnăturilor sau formelor pe o pagină rotită nu funcționează corect, puteți corecta pagina cu un editor PDF extern.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Soluție cu instrument extern (ex., Previzualizare macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Exportați pagina</strong><br>
                &nbsp;&nbsp;Faceți clic în meniu pe <strong>Fișier → Exportați ca pagini</strong> sau utilizați o altă metodă pentru a salva pagina dorită ca un singur PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Deschideți pagina într-un program extern</strong><br>
                &nbsp;&nbsp;Deschideți PDF-ul exportat într-un editor PDF (ex., <strong>Previzualizare macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rotiți pagina</strong><br>
                &nbsp;&nbsp;Rotiți pagina astfel încât să fie verticală (în Previzualizare: <strong>Unelte → Rotire</strong> sau <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Salvați</strong><br>
                &nbsp;&nbsp;Salvați pagina corectată (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Inserați din nou pagina în documentul original</strong><br>
                &nbsp;&nbsp;Reveniți la PDFDarkView și inserați pagina corectată în poziția dorită:<br>
                &nbsp;&nbsp;<strong>Editare → Inserați pagini</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativă: Rotiți pagina în original</p>
                <p style="margin: 5px 0 5px 20px;">• Utilizați funcția de rotire încorporată (<strong>Editare → Rotiți pagina</strong>) pentru a corecta pagina pas cu pas.<br>
                • După fiecare rotire, puteți verifica dacă inserarea funcționează acum.<br>
                • Aceasta este adesea soluția mai rapidă – încercați-o mai întâi!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Sfat:</strong> Dacă întâlniți frecvent pagini rotite, puteți ascunde permanent avertismentul în dialogul de inserare.<br>
                Poziționarea poate fi apoi diferită – utilizați această opțiune doar dacă cunoașteți consecințele.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Aliniază paginile",
        'menu_rotate_normalize_tooltip': "Rotește pagina sau resetează la 0°",
        'normalize_current_page': "Aduceți pagina curentă în poziție verticală (setați la 0°)",
        'normalize_all_pages': "Aduceți toate paginile în poziție verticală (setați la 0°)",
        'page_normalized': "Pagina {0} a fost setată în poziție verticală.",
        'all_pages_normalized': "Toate paginile au fost setate în poziție verticală.",
        'page_already_upright': "Pagina {0} este deja verticală.",
        'all_pages_already_upright': "Toate paginile sunt deja verticale.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF-ul nu conține text căutabil.</p><p>Doriți să efectuați OCR pentru a exporta în {0}?</p>",
        'export_ocr_voice': "PDF-ul nu conține text. Este necesar OCR pentru exportul în {0}.",
        'export_no_ocr_possible': "Exportul fără OCR nu este posibil. Vă rugăm să efectuați OCR prin meniu.",
        'ocr_failed_export_not_possible': "OCR a eșuat. Exportul nu poate fi efectuat.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF-ul se va deschide în Previzualizare. Vă rugăm să începeți procesul de imprimare acolo.",
        'print_preview_manual': "PDF-ul a fost deschis. Vă rugăm să executați comanda de imprimare manual (ex., Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Îmbină PDF-uri",
        'merge_pdfs': "Îmbină PDF-uri",
        'merge_progress_title': "Se îmbină PDF-urile...",
        'merge_pdfs_list': "PDF-uri în ordine (Trageți și plasați pentru sortare)",
        'merge_add_pdf': "Adaugă PDF",
        'merge_remove': "Elimină",
        'merge_move_up': "Sus",
        'merge_move_down': "Jos",
        'merge_pdfs_info': "💡 Sfat: Puteți schimba ordinea prin tragere și plasare",
        'merge_no_pdfs': "Niciun PDF selectat. Faceți clic pe 'Adaugă PDF'.",
        'merge_info': "{0} PDF-uri selectate (aproximativ {1} pagini)",
        'merge_open_file': "Deschide fișierul",
        'merge_merge': "Îmbină",
        'merge_error': "Eroare la îmbinare",
        'merge_min_two_pdfs_error': "Vă rugăm să selectați cel puțin două fișiere PDF pentru îmbinare.",
        'merge_select_pdfs': "Selectați PDF-urile pentru îmbinare",
        'merge_error_file': "Eroare la procesare",
        'merge_cancelled': "Îmbinarea a fost anulată",
        'merge_preparing': "Se pregătește...",
        'merge_processing': "Se procesează PDF {0} din {1}",
        'merge_saving': "Se salvează PDF-ul îmbinat...",
        'merge_complete': "Gata!",
        'merge_success_title': "Îmbinare reușită",
        'merge_success_voice': "{0} PDF-uri au fost îmbinate cu succes.",
        'merge_success_message': "{0} PDF-uri au fost îmbinate cu succes.\n\nNoul document are acum {1} pagini.\n\nFișier nou:\n{2}\n\nLocația de salvare:\n{3}\n{2}\n\nDoriți să deschideți acest PDF?",
        'replace_file_title': "Înlocuiți fișierul?",
        'replace_file_message': "Există deja un PDF deschis. Doriți să îl înlocuiți cu noul fișier?",
        'btn_yes': "Da",
        'btn_no': "Nu",
        'filename_merge_suffix': "imbinat",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Se deschide {0}...",
        'progress_merge_reading': "Se citește {0}...",
        'progress_merge_adding': "Se adaugă {0} pagini...",
        'progress_merge_optimizing': "Se optimizează PDF-ul...",
        'progress_merge_writing': "Se scrie PDF-ul...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "închiderea PDF-ului",
        'action_close_window': "închiderea ferestrei",
        'action_open_new_pdf': "deschiderea unui PDF nou",
        'action_quit_app': "ieșirea din aplicație",
        'changes_saved': "Modificările au fost salvate.",
        'file_close_title': "Închide fișierul PDF",
        'save_before_action': "Trebuie salvate modificările înainte de {0}? Da sau Nu?",
        'save_before_action_voice': "Trebuie salvate modificările înainte de {0}? Da sau Nu?",
        'save_before_close_question': "Trebuie salvate modificările înainte de închidere? Da sau Nu?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF căutabil creat:\n\n{0}\n\n<b>încercați din nou dacă este necesar",
        "ocr_rotate_title": "Aliniați paginile înainte de OCR",
        "ocr_rotate_question": "PDF-ul conține pagini rotite.\nDoriți să aliniați toate paginile la 0° înainte de OCR?\nAcest lucru îmbunătățește semnificativ recunoașterea textului.",
        "ocr_rotate_yes": "Da, aliniați",
        "ocr_rotate_no": "Nu, porniți OCR direct",
        "ocr_rotate_voice": "PDF-ul conține pagini rotite. Ar trebui să fie aliniate toate paginile înainte de OCR?",
        "ocr_not_performed_message": "Niciun text prezent. Vă rugăm să efectuați OCR (meniul \"Editare\" → \"Efectuați OCR\" sau tasta Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Setări OCR",
        "ocr_language_btn": "Selectați limba OCR",
        "ocr_language": "Limba(e) OCR",
        "ocr_language_current": "Limba curentă:",
        "ocr_param_info": "Informații despre parametru",

        "ocr_force_ocr_label": "Forțați OCR",
        "ocr_deskew_label": "Corectați înclinarea",
        "ocr_clean_label": "Curățați imaginea",
        "ocr_oversample_label": "Rezoluție (DPI)",
        "ocr_pagesegmode_label": "Segmentarea paginii",
        "ocr_oem_label": "Modul motor OCR",
        "ocr_optimize_label": "Compresie PDF",
        "ocr_jobs_label": "Procese paralele",
        "ocr_verbose_label": "Detaliu jurnal",

        "ocr_force_ocr_tooltip": "Forțați OCR pe fiecare pagină, chiar dacă textul există deja",
        "ocr_deskew_tooltip": "Aliniați automat scanările înclinate",
        "ocr_clean_tooltip": "Eliminați zgomotul și artefactele din imagine",
        "ocr_oversample_tooltip": "Măriți imaginea înainte de OCR la acest DPI",
        "ocr_pagesegmode_tooltip": "Determină modul în care pagina este împărțită în zone de text",
        "ocr_oem_tooltip": "Selectează motorul OCR al Tesseract",
        "ocr_optimize_tooltip": "Nivelul de compresie al PDF-ului de ieșire",
        "ocr_jobs_tooltip": "Numărul de procese OCR paralele",
        "ocr_verbose_tooltip": "Nivelul de detaliu al ieșirii jurnalului",
        "ocr_settings_explain_btn": "Explicație",

        "ocr_force_ocr_explain": "Forțează recunoașterea textului pe <b>fiecare</b> pagină, chiar dacă aceasta conține deja text.\n\nRecomandare: <b>Pornit</b> pentru PDF-uri scanate, <b>Oprit</b> pentru PDF-uri native cu text deja existent.",

        "ocr_deskew_explain": "Corectează scanările ușor înclinate (până la aproximativ 5°).\n\nRecomandare: <b>Pornit</b> pentru documente scanate, <b>Oprit</b> dacă paginile sunt deja perfect drepte.",

        "ocr_clean_explain": "Elimină zgomotul, punctele și artefactele mici din imagine.\n<b>IMPORTANT:</b> Pentru textele arabe, thailandeze sau vietnameze cu semne diacritice (puncte deasupra/sub litere) această opțiune ar trebui să fie <b>dezactivată</b>, altfel caractere importante pot fi pierdute.",

        "ocr_oversample_explain": "Mărește imaginea <b>înainte</b> de recunoașterea textului la DPI-ul specificat.<br><br>• <b>72-150 DPI:</b> Foarte rapid, dar rată scăzută de recunoaștere<br>• <b>200-300 DPI:</b> Interval optim (Implicit: 300)<br>• <b>400+ DPI:</b> Recunoaștere abia mai bună, dar fișiere semnificativ mai mari<br><br>Recomandare: 300 DPI pentru scrieri complexe (arabă, chineză, japoneză), 200 DPI pentru limbi occidentale.",

        "ocr_pagesegmode_explain": "Determină modul în care Tesseract împarte pagina în zone de text.\n\n• <b>3 - Automat (Implicit):</b> Bun pentru aspecte mixte\n• <b>4 - Coloană unică:</b> Pentru texte cu o singură coloană\n• <b>5 - Bloc vertical:</b> Pentru scrieri verticale (japoneză, chineză)\n• <b>6 - Bloc text uniform:</b> Optim pentru text continuu fără coloane\n• <b>11 - Imagine brută:</b> Pentru scanări proaste / scriere de mână\n\nRecomandare: <b>6</b> pentru documente text simple, <b>3</b> pentru aspecte complexe.",

        "ocr_oem_explain": "Selectează motorul OCR al Tesseract.\n\n• <b>0 - Legacy:</b> Motor vechi (rapid, dar mai puțin precis)\n• <b>1 - LSTM:</b> Motor neuronal (mai lent, dar mai precis)\n• <b>2 - Legacy + LSTM:</b> Combină ambele rezultate\n• <b>3 - Implicit (LSTM preferat):</b> Cea mai bună alegere pentru majoritatea cazurilor\n\nRecomandare: <b>3</b> pentru o precizie maximă de recunoaștere.",

        "ocr_optimize_explain": "Comprimă PDF-ul de ieșire.\n\n• <b>0:</b> Fără optimizare (procesare cea mai rapidă)\n• <b>1:</b> Optimizare ușoară (compromis bun)\n• <b>2:</b> Optimizare moderată\n• <b>3:</b> Optimizare puternică (cel mai mic fișier, dar mai lent)\n\nRecomandare: <b>1</b> pentru utilizarea zilnică.",

        "ocr_jobs_explain": "Numărul de procese paralele pentru OCR.\n\n• <b>1:</b> Lent, dar cel mai scăzut consum de memorie\n• <b>4-8:</b> Optim pentru procesoare multi-core moderne\n• <b>12+:</b> Procesare abia mai rapidă cu consum ridicat de memorie\n\nRecomandare: Numărul de nuclee CPU (de ex. <b>4</b> pe sisteme cu 4 nuclee).",

        "ocr_verbose_explain": "Nivelul de detaliu al ieșirii jurnalului în consolă.\n\n• <b>0:</b> Fără ieșire\n• <b>1:</b> Progres și mesaje de stare\n• <b>2:</b> Ieșire detaliată\n• <b>3:</b> Ieșire de depanare completă (foarte extinsă)\n\nRecomandare: <b>1</b> pentru funcționarea normală.",

        "ocr_reset_title": "Setările au fost resetate",
        "ocr_reset_message": "Toate setările OCR au fost resetate la valorile implicite.",
        "info_tooltip": "Mai multe informații despre acest parametru",
        "ocr_reset_defaults": "Resetați la valorile implicite",

        "ocr_psm_0": "Automat (motor Legacy)",
        "ocr_psm_1": "Detecție automată a coloanelor",
        "ocr_psm_3": "Automat (Implicit)",
        "ocr_psm_4": "Coloană unică",
        "ocr_psm_5": "Bloc vertical",
        "ocr_psm_6": "Bloc text uniform",
        "ocr_psm_7": "Linie text unică",
        "ocr_psm_8": "Cuvânt unic",
        "ocr_psm_11": "Imagine brută (fără analiză aspect)",

        "ocr_oem_0": "Motor Legacy (rapid)",
        "ocr_oem_1": "Motor LSTM (neuronal, precis)",
        "ocr_oem_2": "Legacy + LSTM combinate",
        "ocr_oem_3": "Implicit (LSTM preferat)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Limba(e) OCR...",
        "ocr_language_title": "Selectați limba(e) OCR",
        "ocr_language_instruction": "Selectați limba(e) pentru recunoașterea textului (OCR).\nAtenție: Mai multe limbi afectează performanța și precizia!\nObțineți cele mai bune rezultate dacă selectați o singură limbă.",
        "ocr_language_predefined": "Combinații predefinite",
        "ocr_language_custom": "Personalizat...",
        "ocr_language_selected": "Limbi OCR selectate",
        "ocr_language_changed": "Limba OCR a fost schimbată în {0}",
        "ocr_language_auto_detect": "Limbile disponibile sunt detectate automat.",
        "ocr_language_none_found": "Nu s-au găsit date de limbă Tesseract! Vă rugăm să instalați pachetele de limbă (de ex. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Selecție personalizată a limbii",
        "ocr_language_available": "Limbi disponibile (instalate):",
        "ocr_language_select_hint": "Selectați una sau mai multe limbi:",
        "ocr_language_confirm": "Aplicați",
        "ocr_language_reset": "Resetați la implicit (deu+eng+vie)",
        "ocr_language_priorities": "Limbi recomandate (preinstalate):",

        "select_all_languages": "Selectați tot",
        "clear_all_languages": "Goliți selecția",
        "install_language_packs": "Instalați pachetele de limbă lipsă...",
        "install_hint": "💡 Sfat: Nu toate limbile sunt instalate pe sistemul dumneavoastră. Prin acest buton veți primi ajutor pentru instalare.",
        "ocr_language_install_title": "Instalarea pachetelor de limbă Tesseract",

        "ocr_missing_languages": "Pachete de limbă OCR lipsă",
        "ocr_missing_languages_message": "Următoarele limbi selectate nu sunt instalate pe sistemul dumneavoastră:\n\n{0}\n\nVă rugăm să instalați pachetele de limbă lipsă (consultați ajutorul în 'Ajutor de instalare').\n\nDoriți să deschideți ajutorul de instalare acum?",
        "ocr_missing_languages_voice": "Pachete de limbă lipsă. Vă rugăm să instalați limbile lipsă.",
        "ocr_install_help_now": "Deschideți ajutorul",
        "ocr_continue_anyway": "Încercați oricum",
        "ocr_language_error_title": "Eroare de limbă OCR",
        "ocr_language_error_message": "Eroare în timpul recunoașterii textului: {0}\n\nVă rugăm să verificați setările limbii OCR (Setări → Limba OCR).",
        "ocr_install_help_button": "Ajutor de instalare",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalați pachetele de limbă Tesseract</p>

        <p>Pentru ca OCR să funcționeze într-o anumită limbă, datele de limbă corespunzătoare trebuie să fie instalate pe sistemul dumneavoastră. Urmați instrucțiunile pentru sistemul dumneavoastră de operare:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Deschideți <strong>Terminalul</strong> (Finder → Programe → Utilitare → Terminal).</li>
        <li>Instalați toate limbile disponibile cu:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Acest lucru poate dura câteva minute.)</li>
        <li>Sau doar limbi individuale (de ex. vietnameză):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Cu versiunile actuale de Homebrew, este posibil ca <code>*.traineddata</code> să fie nevoie să fie descărcat manual (vezi mai jos).</li>
        <li>După instalare: Închideți acest dialog și redeschideți selecția limbii OCR – noile limbi vor apărea automat.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Deschideți un terminal (Ctrl+Alt+T).</li>
        <li>Instalați limba dorită, de ex. pentru vietnameză:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Coduri de limbă importante: <code>deu</code> (germană), <code>eng</code> (engleză), <code>vie</code> (vietnameză), <code>spa</code> (spaniolă), <code>fra</code> (franceză), <code>ita</code> (italiană), <code>nld</code> (olandeză), <code>fin</code> (finlandeză), <code>swe</code> (suedeză), <code>nor</code> (norvegiană).</li>
        <li>Afișați toate pachetele disponibile:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Descărcați fișierele <code>*.traineddata</code> dorite de la:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (de ex. <code>vie.traineddata</code> pentru vietnameză).</li>
        <li>Copiați fișierele în folderul de limbi al Tesseract, de obicei:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Adaptați în funcție de instalarea individuală.)</li>
        <li>Reporniți aplicația (sau redeschideți selecția limbii OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativă pentru toate sistemele</p>
        <ul>
        <li>Instalați <strong>OCRmyPDF</strong> și <strong>Tesseract</strong> cu un manager de pachete la alegere. Majoritatea instalărilor conțin deja câteva limbi standard (engleză, germană, franceză).</li>
        <li>Limbile lipsă pot fi instalate oricând – selecția limbii OCR listează doar limbile care există efectiv.</li>
        </ul>

        <hr>
        <p><b>✅ După instalare:</b> Nu este necesară repornirea aplicației – limbile nou adăugate vor apărea imediat în listă.</p>
        <p><b>📖 Ajutor pentru codurile de limbă:</b> O listă completă este disponibilă în <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">documentația Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Fonturi Noto Sans",
        "info_noto_font_voice": "Ghid de instalare a fonturilor Noto Sans",
        "btn_info_noto_font_install": "Info font",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Cum să instalați fonturile gratuite Noto de la Google</h2>

        <p><strong>Fonturile Noto</strong> sunt o familie de fonturi open source de la Google. Scopul lor este de a nu vedea <em>"niciun tofu"</em> (adică fără casete goale □) și de a afișa corect fiecare caracter din standardul Unicode. Ele sunt completarea ideală pentru aplicațiile care trebuie să afișeze texte în multe limbi diferite.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalare pe macOS</h3>

        <p><strong>Metoda 1: Cu Homebrew (pentru utilizatori avansați)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metoda 2: Prin "Font Book" (Recomandat)</strong></p>

        <ol>
        <li>Descărcați pachetul oficial de fonturi:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extrageți fișierul ZIP</li>
        <li>Copiați fișierele în <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalare pe Windows (10 & 11)</h3>

        <p><strong>Metoda 1: Microsoft Store (Recomandat)</strong><br>
        Căutați "Google Noto Fonts" sau "Noto Sans" și faceți clic pe <strong>Instalare</strong>.</p>

        <p><strong>Metoda 2: Instalare manuală</strong></p>

        <ol>
        <li>Descărcare:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extrageți ZIP</li>
        <li>Selectați fișierele .ttf / .otf</li>
        <li>Clic dreapta → <strong>Instalare</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        sau<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nume\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalare pe Linux</h3>

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

        <p>Verificare:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Gestionați marcajele",
        "bookmark_add": "Adăugați marcaj",
        "bookmark_add_tooltip": "Salvați pagina curentă ca marcaj",
        "bookmark_remove": "Eliminați marcajul",
        "bookmark_remove_tooltip": "Ștergeți marcajul marcat",
        "bookmark_remove_all": "Eliminați toate",
        "bookmark_remove_all_tooltip": "Ștergeți toate marcajele acestui PDF",
        "bookmark_jump": "Săriți la marcaj",
        "bookmark_jump_tooltip": "Săriți la pagina selectată",
        "bookmark_name": "Nume",
        "bookmark_page": "Pagina",
        "bookmark_no_bookmarks": "Niciun marcaj prezent.\nFaceți clic pe 'Adăugați' pentru a salva pagina curentă ca marcaj.",
        "bookmark_added": "Marcaj pentru pagina {0} adăugat: {1}",
        "bookmark_removed": "Marcaj eliminat: {0}",
        "bookmark_all_removed": "Toate marcajele au fost eliminate.",
        "bookmark_name_default": "Pagina {0}",
        "bookmark_name_prompt": "Nume pentru marcaj:\n(textul lung va fi scurtat la 50 de caractere)",
        "bookmark_name_prompt_title": "Numele marcajului",
        "bookmark_confirm_remove_all": "Sunteți sigur că doriți să eliminați toate cele {0} marcaje?",
        "menu_bookmarks": "Marcaje",
        "bookmark_manage": "Gestionați marcajele",
        "bookmark_next": "Următorul marcaj",
        "bookmark_prev": "Marcajul anterior",
        "bookmark_page_display": "Pagina {0}",
        "bookmark_exists": "Există deja un marcaj pentru această pagină cu acest nume.",
        "bookmark_select_first": "Vă rugăm să selectați mai întâi un marcaj.",
        "bookmark_confirm_remove": "Sunteți sigur că doriți să eliminați marcajul 'Pagina {0}: {1}'?",
        "bookmark_jumped_to": "Sărit la marcajul '{0}' de pe pagina {1}.",
        "bookmark_jumped_to_voice": "Marcaj {0}, pagina {1}",
        "btn_close": "Închideți",

        "bookmark_list": "Marcajele dumneavoastră",
        "bookmark_rename": "Redenumiți marcajul",
        "bookmark_rename_tooltip": "Schimbați numele marcajului selectat",
        "bookmark_rename_title": "Redenumiți marcajul",
        "bookmark_rename_prompt": "Nume nou pentru marcajul de pe pagina {0}:\n(max. 50 de caractere)",
        "bookmark_renamed": "Marcajul '{0}' a fost redenumit în '{1}'.",
        "bookmark_item_tooltip": "Pagina {0}: {1}\nFaceți dublu clic pentru a sări",
        "bookmark_name_exists_question": "Există deja un marcaj cu numele '{0}' pe această pagină.\nRedenumiți oricum?",

        "context_bookmarks": "Marcaje",
        "context_bookmark_add_here": "Adăugați marcaj pentru această pagină",
        "context_bookmarks_existing": "Marcaje existente:",
        "context_bookmarks_jump": "Săriți la marcaj:",
        "context_bookmarks_none": "Niciun marcaj prezent",
        "context_bookmarks_clear_all": "Eliminați toate cele {0} marcaje",

        "bookmark_search_placeholder": "Căutați marcaje... (nume sau pagină)",
        "bookmark_search_results": "%d marcaje găsite pentru \"%s\"",
        "bookmark_no_search_results": "Niciun marcaj găsit pentru \"%s\"",
        "bookmark_no_search_results_label": "Niciun rezultat pentru \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Editați metadatele PDF",
        "metadata_title": "Titlu",
        "metadata_title_placeholder": "Titlul documentului",
        "metadata_title_tooltip": "Titlul documentului (afișat în bara de titlu)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Numele autorului",
        "metadata_author_tooltip": "Creatorul documentului",
        "metadata_subject": "Subiect",
        "metadata_subject_placeholder": "Subiectul documentului",
        "metadata_subject_tooltip": "O scurtă descriere a conținutului",
        "metadata_keywords": "Cuvinte cheie",
        "metadata_keywords_placeholder": "Cuvinte cheie separate prin virgule",
        "metadata_keywords_tooltip": "Cuvinte cheie pentru categorisirea documentului",
        "metadata_creator": "Creator",
        "metadata_creator_placeholder": "Aplicația care a creat PDF-ul",
        "metadata_creator_tooltip": "Software-ul cu care a fost creat documentul",
        "metadata_producer": "Producător",
        "metadata_producer_placeholder": "Aplicația care a convertit PDF-ul",
        "metadata_producer_tooltip": "Software-ul care a convertit PDF-ul",
        "metadata_creation_date": "Data creării",
        "metadata_creation_date_tooltip": "Data creării documentului",
        "metadata_mod_date": "Data modificării",
        "metadata_mod_date_tooltip": "Data ultimei modificări",
        "metadata_pdf_info": "📄 Informații PDF",
        "metadata_pages": "Numărul de pagini",
        "metadata_file_size": "Dimensiune fișier",
        "metadata_pdf_version": "Versiune PDF",
        "metadata_encrypted": "Criptat",
        "metadata_encrypted_yes": "Da (protejat cu parolă)",
        "metadata_encrypted_no": "Nu",
        "metadata_reload": "📂 Reîncărcați din PDF",
        "metadata_reset": "Renunțați la modificări",
        "metadata_reloaded": "Metadatele au fost reîncărcate din PDF.",
        "metadata_reset_done": "Toate câmpurile de metadate au fost resetate.",
        "metadata_no_file": "Niciun fișier PDF încărcat.",
        "metadata_save_error": "Eroare la salvarea metadatelor",
        "metadata_saved": "Metadatele au fost salvate cu succes.",
        "metadata_pdf_version_unknown": "PDF (necunoscut)",
        "metadata_saved_message": "Metadatele au fost salvate cu succes.",
        "metadata_saved_voice": "Metadate salvate.",

        "metadata_custom": "🔧 Metadate personalizate",
        "metadata_custom_placeholder": "{\n  \"câmpul_meu\": \"valoarea_mea\",\n  \"alt_câmp\": 123\n}",
        "metadata_custom_tooltip": "Format JSON pentru metadate personalizate (opțional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Șablonul \"{0}\" selectat - Faceți dublu clic pentru a insera",
        "text_use_template": "Utilizați bloc de text",
        "text_type": "Tip",
        "text_search_templates": "Căutați blocuri de text...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informații export / import",
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

        <h3>📦 Ce se exportă? (Prezentare generală)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Setări generale ale aplicației</span></li>
            <li class="detail">• Mod întunecat/deschis</li>
            <li class="detail">• Inversarea modului întunecat pentru imagini</li>
            <li class="detail">• Valoarea pragului de gri</li>
            <li class="detail">• Limba</li>
            <li class="detail">• Geometria ferestrei</li>
            <li class="detail">• Modul zoom</li>
            <li class="detail">• Navigare (Bara de navigare vizibilă)</li>
            <li class="detail">• Ieșire vocală (pornit/oprit)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Setări de backup</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Denumire fișiere (Marcaj temporal, Separator, Sufixe)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Setări pentru inserări de</span></li>
            <li class="detail">• Semnături</li>
            <li class="detail">• Text și blocuri de text</li>
            <li class="detail">• Semne, imagini și forme</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Setări OCR</span></li>
            <li class="detail">• Limba</li>
            <li class="detail">• Forțați OCR · Modul paginii</li>
            <li class="detail">• Preprocesarea imaginii: Corectare înclinare, Curățare, Supra-eșantionare</li>
            <li class="detail">• Numărul de sarcini paralele</li>
            <li class="detail">• Modul de inversare</li>
            <li class="detail">• Valoarea pragului de gri</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Marcaje</span></li>
            <li class="detail">• Toate marcajele per fișier PDF (Pagina, Nume, Ora creării)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Baza de date de parole</span></li>
            <li class="detail">• Parole PDF salvate (opțional criptate sau text simplu)</li>
            <li class="detail">• Hash-ul parolei master (dacă este setat)</li>
            <li class="detail">• Date de verificare</li>
        </ul>

        <h4>⚠️ Observații importante</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 La importare:</strong>
            <ul>
                <li><span class="warning">➜ TOATE setările curente vor fi suprascrise complet</span></li>
                <li>• Repornirea aplicației este obligatorie</li>
                <li>• Semnăturile, blocurile de text și marcajele existente vor fi înlocuite</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Parola master și modul de export:</strong>
            <ul>
                <li>• Când parola master este activă, puteți alege:</li>
                <li>  - <span style="color: #98FB98;"><strong>Decriptat</strong></span> (parolele sunt în text simplu în ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Criptat</strong></span> (lizibil doar cu parola master pe sistemul țintă)</li>
                <li>• Hash-ul parolei master este <strong>întotdeauna</strong> stocat criptat</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Notificare de securitate:</strong>
            <ul>
                <li>• Fișierul ZIP exportat conține date sensibile (<strong>parole, marcaje, semnături</strong>)</li>
                <li>• Păstrați-l într-un loc sigur (de ex. stick USB criptat, manager de parole)</li>
                <li>• Dacă fișierul se pierde, parolele PDF salvate sunt pierdute iremediabil</li>
            </ul>
        </div>

        <h4>📁 Format de export</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Setările sunt salvate într-un singur fișier ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Acest ZIP conține <code>settings.json</code> complet (din configurația dumneavoastră), precum și eventuale fișiere imagine de semnătură încorporate și parole criptate.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Semnături - Ghid",
        'signature_guide_html': """
        📝 <strong>Semnături - Ghid rapid</strong><br>
        <ul>
        <li>Setare parolă master</li>
        <li>Configurați semnăturile în meniul <em>Setări</em> (dimensiune, timestamp, …)</li>
        <li>Inserați cu <strong>CLIC DREAPTA</strong> în poziția dorită (parola master necesară o dată pe sesiune)</li>
        <li>Mutați semnătura cu mouse-ul sau tastele săgeată</li>
        <li>Inserați mai multe semnături una după alta</li>
        <li>Personalizați fiecare semnătură individual</li>
        <li>Respingeți o singură semnătură</li>
        <li>Salvați / respingeți toate semnăturile deodată</li>
        <li>Alternativ, puteți utiliza și bara de meniu.</li>
        </ul>
        """,
        'signature_guide_voice': "Ghid rapid pentru semnături. Setare parolă master. Configurați semnăturile în setări. Inserați cu clic dreapta.",

        'image_guide_title': "Inserare imagini - Ghid",
        'image_guide_html': """
        📷 <strong>Inserarea imaginilor în PDF - Ghid rapid</strong><br>
        <ol>
        <li>Clic dreapta pe poziția dorită</li>
        <li><em>„Inserare imagine“</em> → Selectați imaginea</li>
        <li>Poziționați imaginea: Trageți cu mouse-ul</li>
        <li>Reglați dimensiunea: Trageți de colțuri/margini</li>
        <li>Păstrați raportul de aspect: Tasta <strong>[A]</strong></li>
        <li>Reglaje suplimentare: Clic dreapta pe imagine</li>
        </ol>
        <p><strong>Sfat:</strong> În meniul contextual puteți regla setările.</p>
        """,
        'image_guide_voice': "Ghid rapid pentru imagini. Clic dreapta, inserare imagine, selectați. Poziționați cu mouse-ul, reglați dimensiunea la colțuri. Raport de aspect cu tasta A.",

        'form_guide_title': "Inserare forme - Ghid",
        'form_guide_html': """
        📐 <strong>Inserarea formelor în PDF - Ghid rapid</strong><br>
        <ol>
        <li>Selectați tipul de formă (dreptunghi, elipsă, linie, săgeată)</li>
        <li>Faceți clic pe poziție:
            <ul>
            <li>Pentru dreptunghi/elipsă: Un clic plasează forma</li>
            <li>Pentru linie/săgeată: Două clicuri pentru punctul de început și sfârșit</li>
            </ul>
        </li>
        <li>Poziționați forma: Trageți cu mouse-ul</li>
        <li>Reglați dimensiunea: Trageți de colțuri/margini</li>
        <li>Salvați forma: <strong>Enter</strong></li>
        <li>Respingeți forma: <strong>ESC</strong></li>
        <li>Reglaje suplimentare: Clic dreapta pe formă</li>
        </ol>
        <p><strong>Sfat:</strong> În meniul contextual puteți regla setările.</p>
        """,
        'form_guide_voice': "Ghid rapid pentru forme. Selectați tipul de formă. Pentru dreptunghi sau elipsă faceți clic o dată, pentru linie sau săgeată de două ori. Poziționați cu mouse-ul, reglați dimensiunea la colțuri. Salvați cu Enter, respingeți cu Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "anterior",
        "btn_next_result": "următor",
        "ocr_text_window": "Fereastră text OCR",
        "bookmark_existing": "Semne de carte existente",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Comparație OCR Mac - Windows",
        'ocr_method_mac_win_title': "Diferențe OCR între Mac și Windows",
        'ocr_method_mac_win_voice': "Mac este mai bun",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Diferențe între macOS și Windows</strong></p>

        <p><strong>macOS (recomandat)</strong></p>
        <p>Unealtă:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Rezultat:</p>
        <ul>
        <li>Un PDF căutabil cu text încorporat care păstrează în mare măsură aspectul original.</li>
        </ul>
        <p>Avantaje:</p>
        <ul>
        <li>Calitate excelentă a recunoașterii textului (chiar și pe pagini strâmbe).</li>
        <li>Păstrarea graficelor vectoriale și a fonturilor.</li>
        <li>Bară de progres GUI prin evaluarea subprocesului.</li>
        <li>Control deplin asupra tuturor parametrilor OCR (Deskew, Clean, Oversample, optimizare).</li>
        <li>Căutarea textului este disponibilă direct în fereastra principală (vizualizare PDF).</li>
        </ul>
        <p>Dezavantaje:</p>
        <ul>
        <li>Necesită unelte suplimentare de sistem (ocrmypdf, Ghostscript, unpaper, pngquant – incluse în pachetul aplicației).</li>
        <li>Gestionarea erorilor mai complexă (blocaje, timeout-uri).</li>
        </ul>

        <p><strong>Windows (alternativă stabilă)</strong></p>
        <p>Unealtă:</p>
        <ul>
        <li>pytesseract (conexiune directă la Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Rezultat:</p>
        <ul>
        <li>Un PDF căutabil care corespunde vizual unui PDF imagine, dar este căutabil prin textul transparent.</li>
        </ul>
        <p>Avantaje:</p>
        <ul>
        <li>Niciunul nu-mi vine în minte acum.</li>
        </ul>
        <p>Dezavantaje:</p>
        <ul>
        <li>PDF-ul este în esență o imagine cu text invizibil; aspectul poate devia ușor pentru documente complexe (coloane, tabele).</li>
        <li>Fără corecție automată a înclinării (--deskew) sau curățare a imaginii (--clean).</li>
        <li>Bara de progres GUI este actualizată doar aproximativ pe baza numărului de pagini procesate.</li>
        <li>Viteza OCR este ușor mai lentă (deoarece fiecare pagină este procesată individual).</li>
        <li>Căutarea textului este redirecționată către fereastra de text OCR.</li>
        </ul>

        <p><strong>Caracteristici comune</strong></p>
        <ul>
        <li>Ambele metode creează un PDF căutabil în același director cu fișierul sursă.</li>
        <li>Setările OCR (limbă, DPI, mod de segmentare a paginii, mod motor OCR) pot fi configurate prin OCRSettingsDialog și sunt valabile în ambele implementări.</li>
        </ul>

        <p><strong>Recomandare:</strong></p>
        <ul>
        <li>macOS: Binarul ocrmypdf oferă cele mai bune rezultate – Cumpărați un Mac și utilizați versiunea (PDFDarkView pentru Mac-uri cu cip Apple Silicon sau Intel). Rezultatele OCR sunt mai bune decât pe Windows!</li>
        <li>Windows: Utilizați soluția pytesseract. Este stabilă și oferă o calitate complet suficientă pentru majoritatea documentelor.</li>
        </ul>

        <p><strong>Notă importantă:</strong></p>
        <ul>
        <li>Ambele versiuni sunt complet integrate în interfața utilizator – utilizatorul nu observă nicio diferență.</li>
        <li>Programul decide automat ce motor OCR să utilizeze în funcție de sistemul de operare.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Creați semnătură (din scanare)",
        "signature_create_title": "Selectați semnătura scanată (PDF/imagine)",
        "image_pdf_filter": "Imagini și PDF",
        "signature_pdf_empty": "PDF-ul nu conține pagini.",
        "signature_created_success": "Semnătură creată cu succes: {0}",
        "signature_create_error": "Eroare la crearea semnăturii:\n{0}",
        "rembg_missing": "rembg nu este instalat.\nVă rugăm să instalați: pip install rembg\nEroare: {0}",
        "signature_name_title": "Nume fișier pentru semnătură",
        "signature_name_message": "Vă rugăm să introduceți un nume de fișier pentru noua semnătură (va fi salvată ca PNG cu fundal transparent):",
        "signature_name_label": "Nume fișier:",
        "signature_name_voice": "Introduceți numele fișierului pentru semnătură",
        "signature_processing": "Procesare în curs...",
        "signature_creation_title": "Se creează semnătura",
        "signature_overwrite_warning": "Fișierul '{0}' există deja. Suprascriere?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Pregătiți PDF-ul pentru semnătură",
        "signature_prepare_instruction":"Vă rugăm să selectați un PDF care conține pe o singură pagină o semnătură scanată.\n\nPentru o recunoaștere optimă, asigurați-vă că:\n• Semnătura este scrisă cu cerneală neagră (stilou cu bilă sau fineliner) pe hârtie albă.\n• Semnătura se află în treimea superioară a unei pagini A4 altfel goale.\n• PDF-ul a fost scanat cu cel puțin 300 dpi.\n• Semnătura este clară și nu prea subțire.\n• Nu există modele de fundal sau linii deranjante.",
        "signature_prepare_voice":"Vă rugăm să selectați un PDF cu o semnătură scanată. Atenție la calitate bună și contrast.",
        "sig_thickness_label":"Grosimea liniei:",
        "sig_thickness_normal":"Normal (subțire)",
        "sig_thickness_bold":"Îngroșat (recomandat)",
        "sig_thickness_very_bold":"Foarte îngroșat",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Adăugarea limbilor GUI și OCR - Ghid",
        'language_guide_title': "Adăugarea limbilor GUI și OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Descărcați fișierul de traducere dorit <code>translations_xy.py</code> de la<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        și plasați-l în următorul director:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Deschideți browserul web.</li>
        <li>Accesați: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Căutați pe marginea dreaptă a ecranului „Releases” și selectați-l pe cel marcat cu <strong>„latest”</strong>.</li>
        <li>Pe următoarea pagină de lansare, descărcați fișierul <code>Source Code.zip</code> de jos.</li>
        <li>Dezarhivați fișierul ZIP.</li>
        <li>În folderul dezarhivat, găsiți toate fișierele de limbă de care aveți nevoie și copiați-le în directorul:<br/>
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
        "menu_watermark":"Inserare filigran",
        "fullpage_text_watermark_title":"Text ca filigran",
        "fullpage_image_watermark_title":"Imagine ca filigran",
        "filename_with_watermark":"_cu_filigran",
        "watermark_text":"Text:",
        "watermark_text_placeholder":"Textul dvs. pentru filigran...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Dimensiune font:",
        "watermark_format":"Formatare:",
        "watermark_bold":"Îngroșat",
        "watermark_italic":"Cursiv",
        "watermark_color":"Culoare:",
        "watermark_choose_color":"Alegeți culoarea...",
        "watermark_opacity":"Opacitate / Transparență:",
        "watermark_direction":"Direcție de citire:",
        "watermark_direction_l_r":"Stânga → Dreapta",
        "watermark_direction_bl_tr":"Jos stânga → Sus dreapta",
        "watermark_direction_tl_br":"Sus stânga → Jos",
        "watermark_direction_b_t":"Jos → Sus",
        "watermark_direction_t_b":"Sus → Jos",
        "watermark_preview":"Previzualizare:",
        "watermark_preview_sample":"Text exemplu",
        "watermark_empty_text":"Vă rugăm să introduceți text.",
        "watermark_applied":"Filigranul a fost aplicat pe toate paginile.",
        "watermark_saved":"Filigran salvat.",
        "image_scale":"Dimensiune:",
        "image_preview":"Previzualizare imagine:",
        "no_image_selected":"Nicio imagine selectată",
        "browse":"Răsfoiți...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redactări",
        "redact_add_black": "Redactare (negru)",
        "redact_add_white": "Redactare (alb / ștergere)",
        "redact_added_black": "Redactare neagră adăugată",
        "redact_added_white": "Redactare albă adăugată",
        "redact_apply_all": "Aplicați toate redactările și salvați",
        "redact_discard_all": "Renunțați la toate redactările",
        "redact_discard": "Renunțați la această redactare",
        "no_redactions": "Nicio redactare",
        "redact_confirm_title": "Aplicați redactările permanent",
        "redact_confirm_message": "Atenție: Zonele marcate vor fi șterse permanent (negru sau alb).\nO copie de rezervă va fi creată (dacă este activată).\n\nContinuați?",
        "redact_apply": "Da, redactați acum",
        "redact_saved": "{0} redactare(ări) aplicată(e) și salvată(e) cu succes.",
        "redact_saved_voice": "{0} redactare(ări) aplicată(e)",
        "redact_error": "Eroare în timpul redactării",
        "filename_redacted":"_redactat",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Inserare numere de pagină',
        'page_numbers_format': 'Format număr:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabic)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (roman mic)',
        'page_numbers_format_roman_upper': 'I, II, III ... (roman mare)',
        'page_numbers_format_letter': 'A, B, C ... (litere)',
        'page_numbers_format_custom': 'Personalizat',
        'page_numbers_custom_pattern': 'Model:',
        'page_numbers_custom_placeholder': 'ex. "Pagina {nummer}" sau "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Utilizați {nummer} pentru numărul paginii curente și {total} pentru numărul total',
        'page_numbers_position': 'Poziție:',
        'page_numbers_pos_tl': 'Sus stânga',
        'page_numbers_pos_tc': 'Sus centru',
        'page_numbers_pos_tr': 'Sus dreapta',
        'page_numbers_pos_ml': 'Mijloc stânga',
        'page_numbers_pos_mc': 'Centrat',
        'page_numbers_pos_mr': 'Mijloc dreapta',
        'page_numbers_pos_bl': 'Jos stânga',
        'page_numbers_pos_bc': 'Jos centru',
        'page_numbers_pos_br': 'Jos dreapta',
        'page_numbers_margins': 'Margini:',
        'page_numbers_margin_x': 'Distanță orizontală:',
        'page_numbers_margin_y': 'Distanță verticală:',
        'page_numbers_range': 'Interval pagini:',
        'page_numbers_all_pages': 'Toate paginile',
        'page_numbers_custom_range': 'Interval personalizat',
        'page_numbers_from': 'De la:',
        'page_numbers_to': 'Până la:',
        'page_numbers_progress': 'Se inserează numerele de pagină...',
        'page_numbers_start': 'Se începe inserarea numerelor de pagină...',
        'page_numbers_cancel': 'Inserarea numerelor de pagină a fost anulată',
        'page_numbers_success': 'Numerele de pagină au fost adăugate cu succes.\n\nDoriți să deschideți noul PDF?\n\n{0}',
        'page_numbers_complete': 'Numerele de pagină au fost adăugate',
        'page_numbers_error_format': 'Eroare la inserarea numerelor de pagină: {0}',
        'page_numbers_content_type': 'Tip conținut:',
        'page_numbers_tab_simple': 'Număr simplu',
        'page_numbers_tab_range': 'Pagina X din Y',
        'page_numbers_tab_date': 'Dată',
        'page_numbers_tab_custom': 'Text liber',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Pagina {aktuell} din {gesamt}',
        'page_numbers_range_custom': 'Personalizat',
        'page_numbers_range_placeholder': 'ex. "Pagina {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format dată:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 ianuarie 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Personalizat',
        'page_numbers_date_placeholder': 'ex. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Poziție:',
        'page_numbers_date_before': 'Data înaintea numărului paginii',
        'page_numbers_date_after': 'Data după numărul paginii',
        'page_numbers_date_only': 'Doar data (fără număr de pagină)',
        'page_numbers_custom_text': 'Text personalizat:',
        'page_numbers_custom_placeholder_text': 'Utilizați {seite} pentru numărul paginii și {gesamt} pentru total\nex. "Confidențial - Pagina {seite}" sau "{seite} din {gesamt}"',
        "filename_with_page_number":"_cu_numar_pagina",
        "filename_with_page_declaration":"_cu_declaratie_pagina",
        "filename_with_pagenumber":"_cu_numar_pagina",
        "filename_with_date":"_cu_data",
        "filename_with_my_page_declaration":"_cu_declaratie_pagina_personalizata",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Modificări nesalvate",
        "unsaved_changes_message_darkmode": "Există inserări nesalvate.\nDoriți să le salvați înainte de comutare?",
        "save_and_switch": "Salvați și comutați",
        "discard_and_switch": "Comutați acum",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Exportați paginile ca imagini',
        'export_images_menu': 'Exportați ca imagini (PNG/JPEG)',
        'export_images_format': 'Format imagine:',
        'export_images_dpi': 'Rezoluție (DPI):',
        'export_images_quality': 'Calitate JPEG:',
        'export_images_range': 'Interval pagini:',
        'export_images_all_pages': 'Toate paginile',
        'export_images_custom_range': 'Interval personalizat',
        'export_images_from': 'De la:',
        'export_images_to': 'Până la:',
        'export_images_options': 'Opțiuni:',
        'export_images_single_files': 'Fiecare pagină ca fișier separat',
        'export_images_subfolder': 'Exportați în subdosar',
        'export_images_subfolder_info': 'În subdosarul "numePDF_imagini"',
        'export_images_same_folder': 'În același dosar ca PDF-ul',
        'export_images_apply_darkmode': 'Aplicați setările PDFDarkView (Mod întunecat)',
        'export_images_target_folder': 'Dosar destinație:',
        'export_images_browse': 'Răsfoiți...',
        'export_images_preview': 'Previzualizare:',
        'export_images_preview_info': 'Selectați setările pentru export',
        'export_images_preview_info_detail': '{0} pagini ca {1}\nRezoluție: {2} DPI\nNume fișier: {3}\n{4}',
        'export_images_select_folder': 'Selectați dosarul destinație',
        'export_images_start': 'Se începe exportul imaginilor...',
        'export_images_progress': 'Se exportă imaginile...',
        'export_images_saving': 'Se salvează pagina {0} din {1}...',
        'export_images_success': 'Export reușit!\n\n{0} imagini au fost salvate în:\n{1}',
        'export_images_complete': 'Exportul imaginilor s-a finalizat',
        'export_images_open_folder': '📁 Deschideți dosarul',
        'export_images_cancel': 'Exportul imaginilor a fost anulat',
        'export_images_error_format': 'Eroare la exportul imaginilor: {0}',
        'export_images_pdf2image_missing': 'Biblioteca "pdf2image" nu este instalată.\n\nVă rugăm să o instalați cu:\npip install pdf2image\n\nPentru Windows aveți nevoie și de Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Conversie PDF/A pentru arhivare pe termen lung',
        'pdfa_menu': 'Conversie PDF/A (adecvat pentru arhivare)',
        'pdfa_info': 'Convertește PDF-ul în format PDF/A.\n\nPDF/A este conceput special pentru arhivarea pe termen lung și asigură că documentul va fi afișat corect în viitor.',
        'pdfa_standard': 'Standard PDF/A:',
        'pdfa_standard_select': 'Versiune:',
        'pdfa_1': 'PDF/A-1 (simplu, compatibil pe scară largă)',
        'pdfa_2': 'PDF/A-2 (modern, compresie mai bună)',
        'pdfa_3': 'PDF/A-3 (cea mai recentă versiune, permite atașamente)',
        'pdfa_standards_explanation': '📖 Explicația standardelor:\n\n'
            '• PDF/A-1: De bază, compatibil cu sistemele mai vechi (aprox. 2005)\n'
            '• PDF/A-2: Mai modern, compresie mai bună, suport pentru transparență (aprox. 2011)\n'
            '• PDF/A-3: Cea mai recentă versiune, permite încorporarea de atașamente (aprox. 2013)\n\n'
            'Recomandare: PDF/A-2 este un compromis bun între compatibilitate și funcționalități moderne.',
        'pdfa_options': 'Opțiuni:',
        'pdfa_compress_enable': 'Comprimați PDF (fișier mai mic)',
        'pdfa_metadata_preserve': 'Păstrați metadatele (titlu, autor, etc.)',
        'pdfa_target_folder': 'Dosar destinație:',
        'pdfa_browse': 'Răsfoiți...',
        'pdfa_select_folder': 'Selectați dosarul destinație',
        'pdfa_ocr_info_unknown': '🔍 Nu s-a putut verifica conținutul textului.',
        'pdfa_ocr_info_not_needed': '✅ Text disponibil - OCR nu este necesar.\nPDF/A poate fi creat direct.',
        'pdfa_ocr_info_recommended': '⚠️ Nu s-a găsit suficient text.\n\nPentru PDF-uri căutabile, vă recomandăm să rulați mai întâi OCR.\nNotă: PDF/A funcționează și fără OCR - dar textul nu va fi căutabil.',
        'pdfa_ocr_info_error': '❌ Eroare la verificare: {0}',
        'pdfa_start': 'Se începe conversia PDF/A...',
        'pdfa_progress': 'Conversia PDF/A este în curs...',
        'pdfa_success': 'Conversia PDF/A a reușit!\n\nSalvat ca:\n{0}\n\nDoriți să deschideți noul PDF?',
        'pdfa_complete': 'Conversia PDF/A s-a finalizat',
        'pdfa_cancel': 'Conversia PDF/A a fost anulată',
        'pdfa_error_format': 'Eroare la conversia PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Biblioteca "ocrmypdf" nu este instalată.\n\nVă rugăm să o instalați cu:\npip install ocrmypdf',
        'btn_convert': 'Conversie',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimizați PDF (reduceți dimensiunea fișierului)',
        'optimize_menu': 'Optimizați PDF (dimensiune fișier)',
        'optimize_info': 'Reduce dimensiunea fișierului PDF prin diferite metode de optimizare.\n\nCu cât nivelul de compresie este mai ridicat, cu atât fișierul devine mai mic - cu posibilă pierdere de calitate în imagini.',
        'optimize_level': 'Nivel de compresie:',
        'optimize_level_low': 'Scăzut (rapid, economie mică)',
        'optimize_level_medium': 'Mediu (compromis bun)',
        'optimize_level_high': 'Ridicat (economie mare)',
        'optimize_level_maximum': 'Maxim (economie maximă, lent)',
        'optimize_level_explanation': 'Recomandare: "Mediu" este un compromis bun între viteză și dimensiunea fișierului.',
        'optimize_options': 'Opțiuni:',
        'optimize_compress_images': 'Comprimați imaginile (reduceți calitatea JPEG)',
        'optimize_clean_objects': 'Eliminați obiectele neutilizate',
        'optimize_preserve_metadata': 'Păstrați metadatele (titlu, autor, etc.)',
        'optimize_image_quality': 'Calitate imagine:',
        'optimize_range': 'Interval pagini:',
        'optimize_all_pages': 'Toate paginile',
        'optimize_custom_range': 'Interval personalizat',
        'optimize_from': 'De la:',
        'optimize_to': 'Până la:',
        'optimize_target_folder': 'Dosar destinație:',
        'optimize_browse': 'Răsfoiți...',
        'optimize_select_folder': 'Selectați dosarul destinație',
        'optimize_info_box': 'Informații',
        'optimize_info_text': 'Optimizarea poate dura câteva minute pentru PDF-uri mari.\n\nImaginile sunt salvate cu calitate redusă, ceea ce poate reduce semnificativ dimensiunea fișierului.',
        'optimize_start': 'Se începe optimizarea PDF...',
        'optimize_progress': 'Se optimizează PDF...',
        'optimize_cancel': 'Optimizarea PDF a fost anulată',
        'optimize_complete': 'Optimizarea PDF s-a finalizat',
        'optimize_error_format': 'Eroare la optimizarea PDF:\n\n{0}',
        'optimize_success_message': 'Optimizarea PDF a reușit!\n\nSalvat ca:\n{0}\n\nÎnainte: {1}\nDupă: {2}\nEconomie: {3:.1f}%\n\n{4}\n\nDoriți să deschideți PDF-ul optimizat?',
        'optimize_success_message_no_size': 'Optimizarea PDF a reușit!\n\nSalvat ca:\n{0}\n\nInformațiile despre dimensiune nu sunt disponibile.\n\nDoriți să deschideți PDF-ul optimizat?',
        'optimize_result_positive': 'Fișierul a fost redus cu {0:.1f}%.',
        'optimize_result_zero': 'Nicio modificare a dimensiunii fișierului.',
        'optimize_result_negative': 'Fișierul a crescut cu {0:.1f}%.\nOptimizarea a fost omisă, fișierul original a fost păstrat.',
        'btn_optimize': 'Începeți optimizarea',
        'filename_optimize_low_suffix': '_optimizat_scazut',
        'filename_optimize_medium_suffix': '_optimizat',
        'filename_optimize_high_suffix': '_optimizat_ridicat',
        'filename_optimize_maximum_suffix': '_optimizat_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Decupați PDF',
        'crop_menu': 'Decupați PDF (Crop)',
        'crop_range': 'Aplicați pe:',
        'crop_all_pages': 'Toate paginile',
        'crop_current_page': 'Doar pagina curentă',
        'crop_values': 'Valori de decupare (în puncte):',
        'crop_left': 'Stânga:',
        'crop_right': 'Dreapta:',
        'crop_top': 'Sus:',
        'crop_bottom': 'Jos:',
        'crop_presets': 'Predefinite:',
        'crop_preset_white': 'Detectați marginile albe',
        'crop_reset': 'Resetare',
        'crop_mouse_hint': '🖱️ Trageți un dreptunghi pentru a selecta aproximativ zona.\nApoi puteți ajusta valorile cu precizie în SpinBox-uri.\nAjustarea manuală cu mouse-ul nu este posibilă.',
        'crop_apply': 'Decupați',
        'crop_scope_all': 'Toate paginile',
        'crop_scope_current': 'Pagina curentă',
        'crop_new_size': 'Dimensiune nouă: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Niciun PDF încărcat',
        'crop_preview_error': 'Eroare la încărcarea previzualizării',
        'crop_start': 'Se începe decuparea...',
        'crop_progress': 'Se decupează PDF...',
        'crop_success': 'PDF decupat cu succes!\n\nSalvat ca:\n{0}\n\nDoriți să deschideți PDF-ul decupat?',
        'crop_complete': 'Decuparea s-a finalizat',
        'crop_cancel': 'Decuparea a fost anulată',
        'crop_error_format': 'Eroare la decupare:\n\n{0}',
        'filename_crop_suffix': '_decupat',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Aplatizați PDF (Flatten)',
        'flatten_menu': 'Aplatizați PDF (Flatten)',
        'flatten_info': 'Aplatizarea unui PDF "arde" toate elementele editabile în conținutul paginii.\n\nDupă aceea, câmpurile de formular, adnotările, textele, crucile, semnăturile, imaginile și formele nu mai sunt editabile individual.',
        'flatten_explanation_title': '📖 Pentru ce este bun acest lucru?',
        'flatten_explanation_text': 'Aplatizarea este necesară în următoarele situații:\n\n'
            '• 📄 Doriți să pregătiți documentul pentru imprimare\n'
            '• 🔒 Doriți să împiedicați pe cineva să modifice câmpurile de formular\n'
            '• 📎 Doriți să "încorporați" permanent adnotări și comentarii în document\n'
            '• 🖼️ Doriți să ancorați permanent texte, cruci, semnături, imagini și forme în document\n'
            '• 📦 Doriți să pregătiți fișierul pentru arhivare\n\n'
            'Aplatizarea face PDF-ul mai mic și previne mutarea sau ștergerea accidentală a elementelor.',
        'flatten_what_title': 'Ce este aplatizat?',
        'flatten_what_list': '• ✅ Câmpuri de formular (câmpuri text, casete de bifat, butoane)\n'
            '• ✅ Adnotări (comentarii, evidențieri, note)\n'
            '• ✅ Suprapuneri (texte, cruci, semnături, imagini, forme)',
        'flatten_options': 'Opțiuni:',
        'flatten_forms': 'Aplatizați câmpurile de formular',
        'flatten_annotations': 'Aplatizați adnotările',
        'flatten_overlays': 'Aplatizați suprapunerile (texte, cruci, semnături, imagini, forme)',
        'flatten_target_folder': 'Dosar destinație:',
        'flatten_browse': 'Răsfoiți...',
        'flatten_select_folder': 'Selectați dosarul destinație',
        'flatten_warning': '⚠️ Important: Aplatizarea este un proces ireversibil!\n\nDupă aplatizare, elementele editabile nu mai pot fi modificate sau șterse individual.\nCreați o copie de rezervă în prealabil dacă este necesar.',
        'flatten_apply': 'Aplatizați',
        'flatten_start': 'Se începe aplatizarea...',
        'flatten_progress': 'Se aplatizează PDF...',
        'flatten_success': 'PDF aplatizat cu succes!\n\nSalvat ca:\n{0}\n\nDoriți să deschideți PDF-ul aplatizat?',
        'flatten_complete': 'Aplatizarea s-a finalizat',
        'flatten_cancel': 'Aplatizarea a fost anulată',
        'flatten_error_format': 'Eroare la aplatizare:\n\n{0}',
        'filename_flatten_suffix': '_aplatizat',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Suprapunere PDF (Overlay)',
        'overlay_menu': 'Suprapunere PDF (Overlay)',
        'overlay_info': 'Plasează un PDF (suprapunere) peste un alt PDF.\n\nPDF-ul de suprapunere este plasat peste PDF-ul de bază. Acest lucru este util pentru filigrane, logo-uri, anteturi sau ștampile.',
        'overlay_explanation_title': '📖 Pentru ce este bun acest lucru?',
        'overlay_explanation_text': 'Suprapunerea este necesară în următoarele situații:\n\n'
            '• 🏢 Plasarea unui logo de companie ca filigran pe fiecare pagină\n'
            '• 📄 Plasarea unui antet pe un PDF gol\n'
            '• 🖊️ Plasarea unei suprapuneri de ștampilă pe un document\n'
            '• 🔖 Plasarea unui filigran pe toate paginile\n'
            '• 📑 Plasarea unei suprapuneri de formular pe un șablon',
        'overlay_type': 'Tip suprapunere:',
        'overlay_type_fullpage': 'Pagină întreagă (acoperitoare)',
        'overlay_type_transparent': 'Pagină întreagă (transparent - recomandat)',
        'overlay_type_stamp': 'Ștampilă (poziționabilă)',
        'overlay_type_info_fullpage': '📄 PDF-ul de suprapunere este plasat exact peste întreaga pagină.\nFundalul alb poate fi eliminat, astfel încât doar conținutul să rămână vizibil.',
        'overlay_type_info_transparent': '🔍 PDF-ul de suprapunere este plasat peste întreaga pagină cu fundal transparent.\nFundalul alb este eliminat automat - ideal pentru filigrane și logo-uri!',
        'overlay_type_info_stamp': '🖊️ PDF-ul de suprapunere este poziționat și scalat ca o ștampilă.\nPerfect pentru logo-uri, ștampile sau semnături în poziții specifice.',
        'overlay_remove_background': 'Eliminați fundalul alb:',
        'overlay_remove_background_enable': 'Eliminați fundalul alb din PDF-ul de suprapunere (face suprapunerea transparentă)',
        'overlay_remove_background_tooltip': 'Elimină zonele albe din PDF-ul de suprapunere, astfel încât textul de dedesubt să devină vizibil.',
        'overlay_threshold': 'Valoare prag:',
        'overlay_threshold_hint': '(1-254, mai mare = mai mult alb este eliminat)',
        'overlay_select_file': 'Selectați PDF-ul de suprapunere:',
        'overlay_file_placeholder': 'Vă rugăm să selectați un fișier PDF pentru suprapunere',
        'overlay_browse': 'Răsfoiți...',
        'overlay_select_overlay': 'Selectați PDF-ul de suprapunere',
        'overlay_range': 'Interval pagini:',
        'overlay_all_pages': 'Toate paginile',
        'overlay_custom_range': 'Interval personalizat',
        'overlay_from': 'De la:',
        'overlay_to': 'Până la:',
        'overlay_position': 'Poziție:',
        'overlay_position_center': 'Centru',
        'overlay_position_top_left': 'Sus stânga',
        'overlay_position_top_right': 'Sus dreapta',
        'overlay_position_bottom_left': 'Jos stânga',
        'overlay_position_bottom_right': 'Jos dreapta',
        'overlay_size': 'Dimensiune:',
        'overlay_size_original': 'Dimensiune originală',
        'overlay_size_fit_page': 'Potrivire la pagină',
        'overlay_size_custom': 'Personalizat (%)',
        'overlay_opacity': 'Transparență:',
        'overlay_target_folder': 'Dosar destinație:',
        'overlay_browse_folder': 'Răsfoiți...',
        'overlay_select_folder': 'Selectați dosarul destinație',
        'overlay_warning': '⚠️ Notă: PDF-ul de suprapunere este plasat peste PDF-ul de bază și "ars" în el.\n\nElementele PDF-ului de suprapunere nu mai pot fi editate individual după salvare.',
        'overlay_apply': 'Suprapuneți',
        'overlay_start': 'Se începe suprapunerea...',
        'overlay_progress': 'Se suprapune PDF...',
        'overlay_success': 'PDF suprapus cu succes!\n\nSalvat ca:\n{0}\n\nDoriți să deschideți PDF-ul suprapus?',
        'overlay_complete': 'Suprapunerea s-a finalizat',
        'overlay_cancel': 'Suprapunerea a fost anulată',
        'overlay_error_format': 'Eroare la suprapunere:\n\n{0}',
        'overlay_no_file': 'Niciun PDF de suprapunere selectat.\n\nVă rugăm să selectați un fișier PDF pentru suprapunere.',
        'filename_overlay_suffix': '_suprapus',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extrageți imagini din PDF',
        'extract_images_menu': 'Extrageți toate imaginile',
        'extract_images_info': 'Extrage toate imaginile din PDF și le salvează ca fișiere separate.\n\nImaginile sunt salvate în formatul lor original sau convertite într-un format selectat.',
        'extract_images_format': 'Format imagine:',
        'extract_images_quality': 'Calitate JPEG:',
        'extract_images_options': 'Opțiuni:',
        'extract_images_subfolder': 'Extrageți în subdosar ("numePDF_imagini")',
        'extract_images_unique': 'Doar imagini unice (evitați duplicatele)',
        'extract_images_range': 'Interval pagini:',
        'extract_images_all_pages': 'Toate paginile',
        'extract_images_custom_range': 'Interval personalizat',
        'extract_images_from': 'De la:',
        'extract_images_to': 'Până la:',
        'extract_images_target_folder': 'Dosar destinație:',
        'extract_images_browse': 'Răsfoiți...',
        'extract_images_select_folder': 'Selectați dosarul destinație',
        'extract_images_info_box': 'Informații',
        'extract_images_info_text': 'Extragerea poate dura câteva minute pentru PDF-uri mari.\n\nImaginile sunt salvate cu numele lor original (pagina_imagine).',
        'extract_images_extract': 'Extrageți',
        'extract_images_start': 'Se începe extragerea...',
        'extract_images_progress': 'Se extrag imaginile...',
        'extract_images_success': '✅ Imagini extrase cu succes!\n\n{0} imagini au fost salvate în:\n{1}',
        'extract_images_complete': 'Extragerea imaginilor s-a finalizat',
        'extract_images_cancel': 'Extragerea a fost anulată',
        'extract_images_error_format': 'Eroare la extragerea imaginilor:\n\n{0}',
        'extract_images_open_folder': '📁 Deschideți dosarul',
        'extract_images_no_images': 'Nu s-au găsit imagini în PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Mai multe pagini pe o pagină (N-Up)',
        'nup_menu': 'Mai multe pagini pe o pagină (N-Up)',
        'nup_info': 'Aranjează mai multe pagini PDF pe o singură pagină.\n\nIdeal pentru imprimări compacte, rezumate sau materiale de distribuit.',
        'nup_layout': 'Aspect:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Previzualizare:',
        'nup_preview_info': '{0} pagini → {1} pagini pe foaie → {2} foi\nAspect: {3}',
        'nup_order': 'Ordine:',
        'nup_order_horizontal': 'Orizontal (rând cu rând)',
        'nup_order_vertical': 'Vertical (coloană cu coloană)',
        'nup_order_horizontal_reverse': 'Orizontal invers',
        'nup_order_vertical_reverse': 'Vertical invers',
        'nup_range': 'Interval pagini:',
        'nup_all_pages': 'Toate paginile',
        'nup_custom_range': 'Interval personalizat',
        'nup_from': 'De la:',
        'nup_to': 'Până la:',
        'nup_options': 'Opțiuni:',
        'nup_margins': 'Margini:',
        'nup_margin_between': 'Spațiere între pagini:',
        'nup_page_numbers': 'Inserați numere de pagină',
        'nup_target_folder': 'Dosar destinație:',
        'nup_browse': 'Răsfoiți...',
        'nup_select_folder': 'Selectați dosarul destinație',
        'nup_create': 'Creați',
        'nup_start': 'Se începe N-Up...',
        'nup_progress': 'Se creează N-Up...',
        'nup_success': 'N-Up creat cu succes!\n\nSalvat ca:\n{0}\n\nDoriți să deschideți noul PDF?',
        'nup_complete': 'N-Up s-a finalizat',
        'nup_cancel': 'N-Up a fost anulat',
        'nup_error_format': 'Eroare la N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Modificați dimensiunea paginii',
        'pagesize_menu': 'Modificați dimensiunea paginii',
        'pagesize_info': 'Modifică dimensiunea paginii PDF-ului.\n\nConținutul este ajustat automat la noua dimensiune.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Selectați un format standard:',
        'pagesize_custom': 'Dimensiune personalizată:',
        'pagesize_width': 'Lățime:',
        'pagesize_height': 'Înălțime:',
        'pagesize_orientation': 'Orientare:',
        'pagesize_portrait': 'Portret',
        'pagesize_landscape': 'Peisaj',
        'pagesize_scale_options': 'Opțiuni de scalare:',
        'pagesize_fit': 'Potrivire (păstrați raportul de aspect)',
        'pagesize_stretch': 'Întindere (distorsionați)',
        'pagesize_center': 'Centrare (dimensiune originală)',
        'pagesize_range': 'Interval pagini:',
        'pagesize_all_pages': 'Toate paginile',
        'pagesize_custom_range': 'Interval personalizat',
        'pagesize_from': 'De la:',
        'pagesize_to': 'Până la:',
        'pagesize_target_folder': 'Dosar destinație:',
        'pagesize_browse': 'Răsfoiți...',
        'pagesize_select_folder': 'Selectați dosarul destinație',
        'pagesize_apply': 'Aplicați',
        'pagesize_start': 'Se începe modificarea dimensiunii paginii...',
        'pagesize_progress': 'Se modifică dimensiunea paginii...',
        'pagesize_success': 'Dimensiunea paginii a fost modificată cu succes!\n\nSalvat ca:\n{0}\n\nDoriți să deschideți noul PDF?',
        'pagesize_complete': 'Modificarea dimensiunii paginii s-a finalizat',
        'pagesize_cancel': 'Modificarea dimensiunii paginii a fost anulată',
        'pagesize_error_format': 'Eroare la modificarea dimensiunii paginii:\n\n{0}',
        'pagesize_preview_info': 'Dimensiune nouă: {0} x {1} pt',
        'filename_pagesize_suffix': '_dimensiune_noua',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informații PDF',
        'pdf_info_menu': 'Afișați informații PDF',
        'pdf_info_voice': 'Se afișează informațiile PDF',
        'pdf_info_error': 'Eroare la afișarea informațiilor PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Afișați comenzile rapide de la tastatură",
        "shortcuts_dialog_title": "Comenzi rapide de la tastatură",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FIȘIER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Deschideți PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Închideți PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Salvați ca...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Protejați documentul</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Imprimați</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Imprimați imediat (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Ieșiți din aplicație</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exportați ca Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exportați ca DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exportați ca TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exportați ca imagini (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extrageți imagini</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PROCESAREA DOCUMENTELOR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Pagini multiple)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Conversie PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Aplatizați PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Suprapuneți PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimizați PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDITARE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Căutați</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Adăugați marcaj</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Gestionați marcajele</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Următorul marcaj</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Marcajul anterior</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Rulați OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 GESTIONAREA PAGINILOR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rotiți pagina curentă</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rotiți toate paginile</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizați pagina curentă</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizați toate paginile</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Ștergeți pagini</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extrageți pagini</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Inserați pagini</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Mutați pagini</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Fuzionați PDF-uri</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Modificați dimensiunea paginii</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INSERARE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Inserați text</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Inserați cruce</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Inserați semnătura 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Inserați semnătura 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Inserați imagine</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Inserați dreptunghi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Inserați elipsă</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Inserați linie</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Inserați săgeată</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Inserați numere de pagină</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Filigran text</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Filigran imagine</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDACTĂRI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redactare (negru)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redactare (alb)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Aplicați toate redactările</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ AVANSAT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Decupați PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Editați metadatele</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VIZUALIZARE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Comutați modul Întunecat/Deschis</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Afișați fereastra de text</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Lățimea paginii (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Două pagini (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Prezentare generală (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ SETĂRI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Gestionarea parolelor</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Setări OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Setări semnătură</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formatare nume fișier</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Exportați setări</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importați setări</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMAȚII</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Afișați informații PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Activați/dezactivați ieșirea vocală</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Focalizați bara de meniu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Versiune nouă disponibilă",
        "update_available_message": "Există o versiune nouă <b>{0}</b>.\n\nVizitați pagina de lansare pentru a descărca actualizarea:\n{1}",
        "update_available_voice": "Versiunea nouă {0} este disponibilă. Descărcați actualizarea de pe pagina GitHub.",
        "update_open_release": "Deschideți pagina de lansare",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Descărcați toate traducerile",
        "ask_download_all_translations": """Pe lângă germană, engleză și vietnameză, sunt disponibile {total_languages} alte limbi GUI.\n\nTrebuie furnizate / actualizate?\n\nNotă:\nLimbile inutile pot fi șterse manual ulterior în directorul:\n{translations_path}
        \nDacă anulați, puteți descărca limbile GUI ulterior prin meniul 'Instrumente → Actualizați traducerile'.""",
        "menu_update_translations": "Actualizați traducerile",
        "translations_updated": "Traduceri actualizate",
        "translations_update_success": "{} traduceri au fost actualizate cu succes ({} noi, {} actualizate).",
        "translations_update_error": "Eroare la actualizarea traducerilor",
        "translations_update_no_changes": "Toate traducerile sunt deja actualizate.",
        "translations_update_offline": "Nicio conexiune la internet. Traducerile nu au putut fi actualizate.",
        "translations_update_in_progress": "Traducerile sunt actualizate în fundal...",
        "translations_downloading": "Se descarcă traducerile...",
        "translations_path_hint": "Director utilizator pentru traduceri",
        "translations_update_not_available_title": "Actualizarea nu este disponibilă",
        "translations_update_not_available_message": """Actualizarea traducerilor este disponibilă doar în versiunea instalată.\n\nÎn modul de dezvoltare, traducerile sunt deja actualizate.""",
        "translations_update_no_internet_title": "Nicio conexiune la internet",
        "translations_update_no_internet_message": """Nu s-a putut stabili o conexiune la internet.\n\nTraducerile nu pot fi descărcate de pe GitHub.\n\nSoluții posibile:
        • Verificați conexiunea la internet
        • Dezactivați temporar orice firewall
        • Încercați din nou mai târziu
        \nPuteți descărca și manual traducerile de pe GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Actualizarea este deja în desfășurare",
        "btn_retry": "Încercați din nou",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Bine ați venit la PDF Dark View",
        "welcome_title_not_supported": "Bine ați venit la PDF Dark View",
        "welcome_message": "Bine ați venit la PDF Dark View!\n\nLimba sistemului dvs. a fost detectată ca '{language}'.\nDoriți să utilizați această limbă pentru interfața utilizatorului?\n\nPuteți schimba limba oricând prin 'Setări → Limbă'.",
        "welcome_message_language_not_available": "Bine ați venit la PDF Dark View!\n\nLimba sistemului dvs. a fost detectată ca '{language}'.\nAceastă limbă nu este încă instalată.\n\nDoriți să descărcați acum traducerile pentru {language} de pe GitHub?\n\n(Limba va fi apoi utilizată automat pentru interfața utilizatorului.)",
        "welcome_message_language_not_supported": "Bine ați venit la PDF Dark View!\n\nLimba sistemului dvs. a fost detectată ca '{language}'.\nDin păcate, nu există încă traduceri pentru această limbă.\n\nInterfața utilizatorului va fi afișată în {fallback_language}.\n\nPuteți schimba limba oricând prin 'Setări → Limbă'.\nDacă doriți, puteți contribui și cu o traducere pentru limba dvs.:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Da, utilizați limba sistemului",
        "welcome_keep_english": "Nu, păstrați engleza",
        "welcome_download_language": "Da, descărcați {language}",

        # ============================================
        # 107. CĂI UTILIZATE RECENT
        # ============================================

        'menu_recent': 'Utilizate recent',
        'menu_recent_dirs': 'Directoare...',
        'menu_recent_files': 'Fișiere...',
        'recent_manage': 'Gestionare...',
        'recent_enable_tracking': 'Salvează căile recente (confidențialitate)',
        'recent_enable_info': 'Dezactivați această opțiune pentru a nu salva căi',
        'recent_tracking_disabled': 'Urmărirea căilor este dezactivată',
        'recent_enabled': 'activat',
        'recent_disabled': 'dezactivat',
        'recent_tracking_status': 'Urmărirea căilor {0}',
        'recent_dialog_title': 'Căi utilizate recent',
        'recent_tab_directories': 'Directoare',
        'recent_tab_files': 'Fișiere',
        'recent_dirs_instruction': 'Faceți dublu clic pentru a deschide dialogul fișierului în director',
        'recent_files_instruction': 'Faceți dublu clic pentru a deschide PDF-ul direct',
        'recent_no_directories': '(niciun director salvat)',
        'recent_no_files': '(niciun fișier salvat)',
        'recent_default_current': '⭐ Implicit: {0}',
        'recent_set_as_default': '⭐ Setați ca implicit',
        'recent_default_set_title': 'Director implicit setat',
        'recent_default_set_message': 'Directorul "{0}" a fost setat ca implicit pentru deschiderea PDF-urilor.',
        'recent_default_set_voice': 'Director implicit setat',
        'recent_directory_not_found': 'Director negăsit',
        'recent_file_not_found': 'Fișier negăsit',
        'recent_remove_selected': 'Elimină',
        'recent_remove_title': 'Elimină calea',
        'recent_remove_confirm': 'Sigur doriți să eliminați calea "{0}" din listă?',
        'recent_path_removed': 'Calea a fost eliminată',
        'recent_clear_all': 'Elimină toate',
        'recent_clear_title': 'Elimină toate căile',
        'recent_clear_confirm_type': 'Sigur doriți să ștergeți toate {0}?',
        'recent_cleared': 'Lista a fost curățată',
        'recent_path_not_found_title': 'Calea negăsită',
        'recent_path_not_found_message': 'Calea "{0}" nu mai există.',
        'recent_open_file': 'Deschide fișier',
        'btn_open_recent': 'Deschide',
        'recent_open_file_question': 'Doriți să deschideți "{0}" ca PDF?',
        'recent_not_pdf': 'Fișierul selectat nu este un PDF.',
        'recent_more_entries': 'Mai multe intrări...',
        'btn_remove': 'Elimină',
        'btn_clear': 'Curăță toate',
        'recent_context_open': 'Deschide',
        'recent_context_reveal': 'Arată în Finder',
        'recent_context_set_default': '⭐ Setați ca implicit',
        'recent_context_open_terminal': '💻 Deschide terminalul',
        'recent_context_file_info': 'Informații fișier',
        'recent_context_open_with_default': '📄 Deschide cu aplicația implicită',
        'recent_context_remove': 'Elimină din listă',
        'recent_context_clear_all': 'Elimină toate',
        'recent_file_info_title': 'Informații fișier',
        'recent_file_info_name': 'Nume',
        'recent_file_info_path': 'Cale',
        'recent_file_info_size': 'Dimensiune',
        'recent_file_info_modified': 'Modificat',
        'recent_file_info_pages': 'Pagini',
        'recent_error_reveal': 'Eroare la deschiderea în Finder',
        'recent_error_terminal': 'Eroare la deschiderea terminalului',
        'recent_error_info': 'Eroare la obținerea informațiilor fișierului',
        'open_user_data_folder': 'Arată directorul de date utilizator',

        # ============================================
        # 108. ȘTERGEREA PAGINILOR PARE/IMPARE
        # ============================================
        "pages_delete_even": "Șterge toate paginile pare",
        "pages_delete_odd":  "Șterge toate paginile impare",
        "progress_even_pages": "Se șterg paginile pare",
        "progress_odd_pages": "Se șterg paginile impare",
        "progress_mark_delete_even": "{} pagină/pagini pare marcate pentru ștergere",
        "progress_mark_delete_odd":  "{} pagină/pagini impare marcate pentru ștergere",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programul se închide",

    }
