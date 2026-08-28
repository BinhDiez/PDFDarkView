
# ============================================
# translations_bs.py - Bosanski rječnik
# Vollständig sortiert nach Kategorien
# ============================================

def load_bosnian_strings():
    """Lädt alle bosnischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Otvori PDF",
        'btn_text_window': "OCR tekst",
        'btn_first': "Prva stranica",
        'btn_prev': "Prethodna stranica",
        'btn_next': "Sljedeća stranica",
        'btn_last': "Zadnja stranica",
        'btn_print': "Štampaj",
        'btn_darkmode_light': "Svijetli način",
        'btn_darkmode_dark': "Tamni način",
        'btn_delete_pages': "Izbriši stranice",
        'btn_extract_pages': "Izdvoj stranice",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Otkaži",
        'btn_save': "Sačuvaj",
        'btn_close': "Zatvori",
        'btn_delete': "Izbriši",
        'btn_delete_all': "Izbriši sve",
        'btn_copy': "Kopiraj",
        'btn_export': "Izvezi",
        'btn_show': "Prikaži lozinku",
        'btn_hide': "Sakrij lozinku",
        'btn_authenticate': "Autentifikuj",
        'btn_settings': "Postavke",
        'btn_protect': "Zaštiti",
        'btn_remove_password': "Ukloni lozinku",
        'btn_manage': "Upravljanje lozinkama",
        'btn_retry': "Pokušaj ponovo",
        'btn_select_all': "Odaberi sve",
        'btn_clear_selection': "Očisti odabir",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Stranica {0} od {1}",
        'page_count': "od {0}",
        'goto_page': "Idi na stranicu",
        'page_simple': "Stranica {0}",
        'full_view_page': "Puni prikaz stranice {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Unesite pojam za pretragu + Enter",
        'search_results': "Rezultata: {0} od {1}",
        'search_nav_hint': "Enter: sljedeći (Shift+Enter: prethodni) rezultat",
        'search_no_results': "Nema rezultata",
        'search_error': "Greška u pretrazi",
        'search_active': "Polje za pretragu aktivirano",
        'search_closed': "Pretraga završena",
        'search_position': "Stranica {0} {1}",
        'search_pos_top': "sasvim gore",
        'search_pos_upper': "gore",
        'search_pos_middle': "sredina",
        'search_pos_lower': "dolje",
        'search_pos_bottom': "sasvim dolje",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Prepoznavanje teksta uspješno završeno!",
        'ocr_success_title': "OCR uspješan",
        'ocr_success_message': "Dokument je sada moguće pretraživati.",
        'ocr_failed': "OCR nije uspio",
        'ocr_in_progress': "OCR u toku",
        'ocr_preparing': "Priprema PDF-a...",
        'ocr_analyzing': "Analiza PDF-a...",
        'ocr_optimizing': "Optimizacija slike...",
        'ocr_recognizing': "Prepoznavanje teksta...",
        'ocr_embedding': "Ugrađivanje teksta...",
        'ocr_finalizing': "Finalizacija PDF-a...",
        'ocr_not_available': "OCR nije dostupan",
        'ocr_install_message': "OCR alati nisu pronađeni.\n\nMolimo instalirajte:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR je potreban",
        'ocr_question': "PDF ne sadrži tekst koji se može pretraživati.\nŽelite li pokrenuti OCR kako biste omogućili {0}?",
        'ocr_perform': "Pokreni OCR",
        'ocr_later': "Kasnije",
        'ocr_starting': "Pokretanje garantovanog OCR-a...",
        'ocr_success_voice': "OCR uspješan. PDF je sada moguće pretraživati.",
        'ocr_partial_success': "OCR je izvršen, ali je došlo do problema prilikom zamjene.\n\nVerzija za pretragu sačuvana je na:\n{0}\n\nGreška: {1}",
        'ocr_partial_title': "OCR djelimično uspješan",
        'ocr_partial_voice': "OCR izvršen, ali zamjena nije uspjela.",
        'original_file': "Originalni fajl:",
        'old_size': "Stara veličina:    {0} bajtova",
        'new_size': "Nova veličina: {0} bajtova",
        'size_change': "Promjena: {0}{1} bajtova",
        'backup_created_file': "Rezervna kopija napravljena:\n{0}",
        'backup_not_created': "Rezervna kopija nije napravljena (postavka isključena)",
        'page_header': "=== Stranica {0} ===\n{1}\n",
        'scanned_page_header': "=== Stranica {0} (skenirana) ===\n[Ova stranica sadrži samo skenirani tekst]\n[Molimo izvršite OCR ručno]\n",
        'scanned_warning': "⚠️ SKENIRANI TEKST - OCR POTREBAN",
        'guaranteed_title': "Napravljen PDF za pretragu",
        'guaranteed_message': "<b>Garantovana verzija za pretragu napravljena!</b>\n\nPošto automatski OCR nije uspio, napravljen je alternativni PDF za pretragu:\n\n{0}\n\n<b>Ovaj fajl sadrži:</b>\n• Izdvojeni tekst (ako je postojao)\n• Upute za skenirane stranice\n• Potpuno je pretraživ",
        'guaranteed_voice': "Garantovani PDF za pretragu napravljen.",
        'instruction_title': "UPUTE ZA OCR",
        'instruction_file': "Originalni fajl: {0}",
        'instruction_text': "Automatsko prepoznavanje teksta (OCR) nije uspjelo.\nIzvršite OCR ručno:\n\n1. SA OCRmyPDF (komandna linija):\n   ocrmypdf --force-ocr \"[FAJL]\" \"izlaz.pdf\"\n\n2. SA ADOBE ACROBAT (macOS/Windows):\n   • Otvorite PDF u Acrobatu\n   • Alati > Uredi PDF\n   • Odaberite 'Prepoznavanje teksta'\n\n3. SA PREVIEW (macOS):\n   • Otvorite PDF u Pregledu\n   • Fajl > Izvezi...\n   • Quartz filter: 'Smanji veličinu fajla'\n   • Uključite 'Pokreni OCR'\n\n4. ONLINE OCR USLUGE:\n   • smallpdf.com/bs/ocr-pdf\n   • ilovepdf.com/bs/ocr-pdf\n   • adobe.com/bs/acrobat/online/pdf-to-word.html",
        'instruction_created': "Upute za OCR napravljene",
        'instruction_created_message': "Detaljne upute su napravljene:\n\n{0}\n\nSlijedite korake za ručni OCR.",
        'instruction_created_voice': "Upute za OCR napravljene.",
        'ocr_impossible': "OCR nije moguć",
        'ocr_impossible_message': "OCR nije mogao biti izvršen.\n\nObrađite '{0}' ručno pomoću OCR softvera.",
        'ocr_impossible_voice': "OCR nije moguć. Molimo obrađite ručno.",
        'emergency_title': "Hitni OCR",
        'emergency_message': "Hitni PDF je napravljen:\n\n{0}\n\nMolimo obrađite ovaj fajl ručno pomoću OCR-a.",
        'emergency_voice': "Hitni PDF napravljen. Molimo izvršite OCR ručno.",
        'critical_error': "Kritična greška",
        'critical_error_message': "OCR nije mogao biti pokrenut.\n\nPonovo pokrenite program i provjerite instalaciju OCR-a.",
        'critical_error_voice': "Kritična OCR greška",
        'ocr_question_html': "<p>PDF ne sadrži tekst koji se može pretraživati.<p>Želite li pokrenuti OCR kako biste omogućili <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR je potreban. PDF ne sadrži tekst koji se može pretraživati. Želite li pokrenuti OCR kako biste omogućili {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "nijedan PDF nije učitan",
        'no_pdf_message': "Nijedan PDF nije učitan",
        'pdf_not_found': "PDF fajl nije pronađen",
        'file_size': "Veličina fajla",
        'bytes': "bajtova",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Rezervna kopija napravljena",
        'backup_disabled': "Rezervno kopiranje isključeno",
        'backup_activated': "Pravljenje rezervnih kopija uključeno",
        'backup_deactivated': "Pravljenje rezervnih kopija isključeno",
        'backup_status': "Rezervna kopija: {0}",
        'backup_on': "✔ uključeno",
        'backup_off': "✘ isključeno",
        'close_pdf': "Zatvaranje PDF-a: {0}",
        'pdf_not_found_format': "PDF fajl nije pronađen: {0}",
        'error_pdf_load_format': "Greška pri učitavanju PDF-a: {0}",
        'load_failed_format': "Učitavanje nije uspjelo:\n{0}",
        'decrypted_suffix': "(dešifrovano)",
        'decryption_failed': "Dešifrovanje nije uspjelo.",
        'decryption_error': "Greška pri dešifrovanju",
        'decryption_success': "Uspješno dešifrovano",
        'decryption_success_message': "PDF je dešifrovan i sačuvan na:\n\n{0}",
        'decryption_success_voice': "PDF je dešifrovan i sačuvan.",
        'password_remove_error': "Greška pri uklanjanju lozinke",
        'save_unencrypted': "Sačuvaj nešifrovani PDF kao",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Sačuvaj kao...",
        'save_copy': "Sačuvaj kopiju",
        'save_success': "PDF sačuvan na: {0}",
        'save_encrypted': "Zaštićeni PDF sačuvan na: {0}",
        'save_error': "PDF nije mogao biti sačuvan",
        'encryption_question': "Želite li zaštititi PDF lozinkom?",
        'encryption_yes': "Da",
        'encryption_no': "Ne",
        'encryption_cancel': "Otkaži",
        'save_cancel': "Čuvanje otkazano",
        'save_encrypted_voice': "Fajl šifrovan i sačuvan.",
        'save_success_voice': "PDF fajl je sačuvan nešifrovan.",
        'save_error_format': "PDF nije mogao biti sačuvan:\n{0}",
        'export_pages_success': "Izvoz u Pages uspješan",
        'export_pages_error': "Izvoz u Pages nije uspio",
        'export_pages_error_format': "Izvoz u Pages nije uspio: {0}",
        'export_word_success': "Izvoz u Word uspješan",
        'export_word_error': "Izvoz u Word nije uspio",
        'export_word_error_format': "Izvoz u Word nije uspio: {0}",
        'export_text_success': "Izvoz teksta uspješan",
        'export_text_error': "Izvoz teksta nije uspio",
        'export_text_error_format': "Izvoz teksta nije uspio: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Lozinka je potrebna",
        'password_enter': "Molimo unesite lozinku",
        'password_confirm': "Potvrdite lozinku",
        'password_new': "Nova lozinka",
        'password_current': "Trenutna lozinka",
        'password_save': "Sačuvaj lozinku (šifrovanu)",
        'password_saved': "✓ Lozinka za ovaj fajl je sačuvana",
        'password_wrong': "Pogrešna lozinka",
        'password_mismatch': "Lozinke se ne podudaraju",
        'password_too_short': "Lozinka je prekratka",
        'password_min_length': "Lozinka mora imati najmanje 4 znaka",
        'password_strength': "Jačina lozinke",
        'password_strength_very_weak': "Vrlo slaba",
        'password_strength_weak': "Slaba",
        'password_strength_medium': "Srednja",
        'password_strength_strong': "Jaka",
        'password_strength_very_strong': "Vrlo jaka",
        'password_char_count': "({0} znakova)",
        'password_match': "✓ Podudaraju se",
        'password_no_match': "✗ Lozinke se ne podudaraju",
        'password_show': "Prikaži",
        'password_hide': "Sakrij",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Upravljanje lozinkama",
        'password_table_filename': "Naziv fajla",
        'password_table_password': "Lozinka",
        'password_count': "{0} sačuvanih lozinki",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Nema sačuvanih lozinki",
        'password_copied': "Kopirano {0} lozinki",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Jeste li sigurni da želite izbrisati lozinku za '{0}'?",
        'password_delete_multiple': "Jeste li sigurni da želite izbrisati {0} odabranih lozinki?",
        'password_delete_all_confirm': "Jeste li sigurni da želite izbrisati svih {0} sačuvanih lozinki?",
        'password_deleted': "Izbrisano {0} lozinki",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Sve lozinke su izbrisane",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generator lozinki",
        'generator_generated': "Generirana lozinka:",
        'generator_regenerate': "Generiraj ponovo",
        'generator_copy': "Kopiraj",
        'generator_use': "Koristi",
        'generator_settings': "Postavke",
        'generator_length': "Dužina:",
        'generator_group_every': "Razdjelnik svakih",
        'generator_group_chars': "znakova.    Razdjelnik:",
        'generator_uppercase': "Velika slova (A-Z)",
        'generator_lowercase': "Mala slova (a-z)",
        'generator_digits': "Brojevi (0-9)",
        'generator_symbols': "Simboli (!@#$%^&*)",
        'generator_exclude': "Isključeno:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Glavna lozinka je potrebna",
        'master_password_setup': "Postavi glavnu lozinku",
        'master_password_change': "Promijeni glavnu lozinku",
        'master_password_enter': "Molimo unesite svoju glavnu lozinku",
        'master_password_choose': "Odaberite jaku glavnu lozinku (najmanje 8 znakova)",
        'master_password_new': "Molimo unesite svoju novu glavnu lozinku",
        'master_password_confirm': "Potvrdite lozinku",
        'master_password_authenticate': "Autentifikuj",
        'master_password_success': "Glavna lozinka je uspješno postavljena.",
        'master_password_changed': "Glavna lozinka je uspješno promijenjena.",
        'master_password_removed': "Glavna lozinka i sve lozinke su izbrisane.",
        'master_password_remove': "Ukloni glavnu lozinku",
        'master_password_remove_confirm': "Jeste li SIGURNI da želite izbrisati SVE lozinke?\n\nOva radnja je NEPOVRATNA!",
        'master_password_export_before': "Želite li prvo izvesti rezervnu kopiju?",
        'master_password_export_delete': "Izvezi i izbriši",
        'master_password_delete_now': "Izbriši odmah",
        'master_password_for_signatures': "Da biste koristili potpise, morate postaviti glavnu lozinku.\n\nŽelite li postaviti glavnu lozinku sada?",
        'master_password_for_private': "Da biste koristili privatne tekstualne blokove, morate postaviti glavnu lozinku.\n\nŽelite li postaviti glavnu lozinku sada?",
        'master_password_info': """
            <b>🔐 BEZ GLAVNE LOZINKE:</b><br>
            • Nije moguće prikazivanje, kopiranje i izvoz lozinki<br>
            • Brisanje lozinki je uvijek moguće (čak i bez glavne lozinke)<br><br>

            <b>🔐 SA GLAVNOM LOZINKOM:</b><br>
            • Sve funkcije dostupne nakon autentifikacije<br>
            • Lozinke se šifriraju glavnom lozinkom<br>
            • Minimalna dužina: 8 znakova<br>
            • Sigurno čuvanje SHA-256 hash-a<br><br>

            <b>VAŽNO:</b><br>
            • Ako izgubite glavnu lozinku, lozinke se ne mogu povratiti<br>
            • Prilikom uklanjanja glavne lozinke, SVE lozinke se brišu<br>
            • Opcija izvoza dostupna prije brisanja<br>
            • Glavnu lozinku možete promijeniti u bilo kojem trenutku
        """,
        'signature_auth_disabled': "Isključi traženje lozinke za potpise",
        'template_auth_disabled': "Isključi traženje lozinke za privatne tekstualne blokove",
        'master_password_for_signatures_settings': "Da biste koristili potpise, morate postaviti glavnu lozinku.\n\nIdite na Postavke - Upravljanje lozinkama",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Zaštiti PDF",
        'protect_info': "Fajl '{0}' bit će zaštićen lozinkom.",
        'protect_instruction': "Molimo unesite željenu lozinku dvaput da biste zaštitili dokument ili koristite generator lozinki desno od polja za unos.",
        'protect_success': "PDF je uspješno zaštićen i sačuvan na:\n{0}\n\nLozinka: {1}\n\nŽelite li otvoriti zaštićeni PDF sada?",
        'protect_open': "Da",
        'protect_skip': "Ne",
        'protect_error': "Greška pri zaštiti PDF-a",
        'protect_open_title': "otvori zaštićeni PDF",
        'protect_question': "Gotovo. Želite li otvoriti zaštićeni PDF sada? Da ili Ne?",
        'password_cancel': "Dijalog za lozinku otkazan",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Izbriši stranice",
        'pages_extract': "Izdvoj stranice",
        'pages_insert': "Umetni stranice",
        'pages_move': "Premjesti stranice",
        'pages_delete_options': "Opcije brisanja",
        'pages_delete_empty': "Izbriši sve prazne stranice",
        'pages_delete_current': "Izbriši trenutnu stranicu",
        'pages_delete_range': "Izbriši raspon stranica",
        'pages_extract_options': "Opcije izdvajanja",
        'pages_extract_current': "Izdvoj trenutnu stranicu",
        'pages_extract_range': "Izdvoj raspon stranica",
        'pages_insert_position': "Pozicija umetanja",
        'pages_insert_before': "Umetni prije stranice:",
        'pages_insert_select': "Odaberi PDF",
        'pages_insert_none': "Nijedan PDF nije odabran",
        'pages_move_source': "Stranice za premještanje",
        'pages_move_from': "Od stranice:",
        'pages_move_to': "Do stranice:",
        'pages_move_target': "Ciljna pozicija",
        'pages_move_before': "Premjesti prije stranice:",
        'pages_move_hint': "Napomena: stranica 1 = početak, {0} = kraj",
        'pages_range_invalid': "Početna stranica mora biti manja ili jednaka krajnjoj stranici.",
        'pages_position_invalid': "Ciljna pozicija ne smije biti unutar raspona koji se premješta.",
        'pages_no_pdf_selected': "Nijedan PDF nije odabran.",
        'pages_deleted': "Izbrisano je {0} stranica.",
        'pages_extracted': "Izdvojeno: {0}\nSačuvano na: {1}\nVeličina fajla: {2:.1f} KB",
        'pages_inserted': "Umetnuto {0} stranica",
        'pages_moved': "Premješteno je {0} stranica.",
        'pages_deleted_none': "Nijedna stranica nije izbrisana.",
        'pages_delete_progress': "Brisanje stranica...",
        'pages_deleted_with_backup': "Izbrisano je {0} stranica.\n\nRezervna kopija: {1}",
        'pages_deleted_voice': "Napravljena je rezervna kopija i izbrisano {0} stranica.",
        'info': "Informacija",
        'error_dialog_creation': "Dijalog nije mogao biti napravljen",
        'extract_page_single': "Izdvoj stranicu {0}",
        'extract_page_range': "Izdvoj stranice {0}-{1}",
        'extract_success_voice': "Stranice uspješno izdvojene",
        'extract_error_format': "Greška pri izdvajanju: {0}",
        'pages_inserted_voice': "Umetnuto je {0} stranica.",
        'insert_error_format': "Greška pri umetanju: {0}",
        'pages_move_progress': "Premještanje stranica...",
        'pages_moved_with_backup': "Premješteno je {0} stranica.\n\nRezervna kopija: {1}",
        'move_success_title': "Uspješno premješteno",
        'pages_moved_voice': "{0} stranica uspješno premješteno",
        'mark_removed': "Oznaka stranice {0} uklonjena",
        'mark_empty': "Stranica {0} označena kao prazna",
        'mark_export_removed': "Oznaka za izvoz stranice {0} uklonjena",
        'mark_export': "Stranica {0} označena za izvoz",
        'no_empty_pages': "Nema praznih stranica označenih za brisanje",
        'delete_empty_confirm': "Želite li izbrisati svih {0} označenih praznih stranica?",
        'delete_empty_confirm_voice': "Izbrisati sada svih {0} označenih praznih stranica? Da ili Ne.",
        'empty_pages_deleted': "{0} praznih stranica izbrisano",
        'no_export_pages': "Nema stranica označenih za izvoz",
        'overwrite_title': "Prepiši postojeći fajl",
        'overwrite_question': "Fajl\n\n{0}\n\nveć postoji.\nŽelite li ga prepisati?",
        'overwrite_voice': "Prepisati postojeći fajl? Da ili Ne.",
        'page_skipped': "Stranica {0} je preskočena",
        'export_complete': "Izvoz završen.",
        'export_complete_voice': "Izvoz je završen.",
        'no_pages_exported': "Nijedna stranica nije izvezena",
        'export_cancelled': "Izvoz otkazan",
        'pages_exported': "{0} stranica izvezeno u {1}",
        'export_page_title': "Izvezi stranicu",
        'page_exported': "Stranica {0} izvezena u {1}",
        'export_error': "Greška pri izvozu",
        'export_marked_title': "Izvezi označene stranice",
        'rotate_all_title': "okreni sve stranice",
        'rotate_all_question': "Želite li okrenuti sve stranice za 90 stepeni udesno?",
        'rotate_all_voice': "Želite li okrenuti sve stranice za 90 stepeni udesno? Da ili Ne?",
        'all_pages_rotated': "Sve stranice okrenute",
        'page_rotated': "Stranica {0} okrenuta",
        'rotate_error': "Stranica nije mogla biti okrenuta",
        'delete_page_confirm': "Želite li izbrisati stranicu {0}?",
        'delete_page_confirm_voice': "Jeste li sigurni da želite izbrisati stranicu {0}? Da ili Ne.",
        'page_deleted': "Stranica {0} izbrisana",
        'delete_error': "Stranica nije mogla biti izbrisana",
        'pages_deleted_voice': "{0} stranica izbrisano",
        'pages_exported_split': "{0} stranica je uspješno izvezeno.",
        'pages_skipped': "{0} stranica je preskočeno.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Izdvoj stranice (napredno)",
        'pdf_splitter_title': "Razdjelnik i izdvajač PDF-a",
        'pdf_splitter_load': " Odaberi PDF fajl",
        'pdf_splitter_info': "Molimo odaberite opciju za svoj PDF dokument",
        'pdf_splitter_basic': "Osnovne operacije",
        'pdf_splitter_single': "Podijeli na pojedinačne stranice",
        'pdf_splitter_range': "Izdvoj stranice:",
        'pdf_splitter_range_placeholder': "npr. 1-3,5,7-9",
        'pdf_splitter_clean': "Operacije čišćenja",
        'pdf_splitter_remove_empty': "Ukloni sve prazne stranice",
        'pdf_splitter_remove': "Izbriši raspon stranica:",
        'pdf_splitter_remove_placeholder': "npr. 2,4-6",
        'pdf_splitter_process': "Obradi PDF",
        'pdf_splitter_loaded': "PDF učitan. Molimo odaberite opciju",
        'pdf_read_error': "PDF nije mogao biti pročitan",
        'pages': "Stranice",
        'pages_created': "Stranice su napravljene",
        'range_empty': "Molimo unesite raspon stranica",
        'range_invalid': "Nevažeći raspon stranica",
        'range_created': "Napravljen je novi PDF sa odabranim stranicama:\n{0}",
        'empty_removed': "Uklonjeno {0} praznih stranica.\nIzlaz: {1}",
        'remove_empty': "Molimo unesite stranice za uklanjanje",
        'remove_invalid': "Nevažeće stranice za uklanjanje",
        'remove_done': "Očišćeni PDF napravljen:\n{0}",
        'open_folder': "Otvori fasciklu",
        'show_in_finder': "Prikaži u Finderu",
        'pdf_splitter_no_pdf': "Molimo prvo učitajte PDF fajl.",
        'process_error': "Greška pri obradi PDF-a",
        'pages_created_voice': "{0} stranica napravljeno",
        'range_created_voice': "PDF sa odabranim stranicama napravljen",
        'empty_removed_voice': "{0} praznih stranica uklonjeno",
        'remove_done_voice': "Očišćeni PDF napravljen",
        'pdf_splitter_split_groups': "Svaku neprekidnu grupu u zaseban fajl",
        'range_created_single': "Napravljen novi PDF:\n{0}",
        'range_created_multiple': "Napravljeno {0} PDF fajlova.",
        'range_created_voice_single': "Napravljen jedan PDF sa odabranim stranicama",
        'range_created_voice_multiple': "Napravljeno {0} PDF fajlova",
        'empty_removed_none_left': "Nema preostalih stranica",
        'empty_removed_all_empty': "Sve stranice su prepoznate kao prazne i bile bi uklonjene. Nijedan fajl nije napravljen.",
        'preview_single': "Pregled: {0}",
        'preview_enter_range': "Molimo unesite raspon stranica.",
        'preview_invalid_range': "Nevažeći raspon stranica.",
        'preview_file': "Pregled: {0}",
        'preview_files': "Pregled: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Pokretanje štampanja",
        'print_sent': "Zadatak za štampanje poslan",
        'print_now': "Štampaj odmah",
        'print_error': "Greška pri trenutnom štampanju",
        'print_limited': "Funkcija štampanja ograničena na ovom sistemu",
        'print_error_format': "Greška pri trenutnom štampanju: {0}",
        'warning': "Upozorenje",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Prebaci na svijetli način",
        'mode_switch_to_dark': "Prebaci na tamni način",
        'mode_dark_activated': "Tamni način aktiviran",
        'mode_light_activated': "Svijetli način aktiviran",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Puni prikaz",
        'zoom_two_pages': "Dvije stranice jedna pored druge",
        'zoom_overview': "Režim pregleda",
        'zoom_cannot_during_search': "Zumiranje nije moguće tokom pretrage",
        'zoom_exit_first': "Molimo prvo izađite iz zumiranja",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Prevlačenje i ispuštanje uključeno",
        'drag_disabled': "Prevlačenje i ispuštanje isključeno",
        'drag_page_grab': "Stranica {0} uhvaćena",
        'drag_page_dropped': "Stranica {0} umetnuta na poziciju {1}",
        'drag_position_invalid': "Nevažeća pozicija",
        'drag_same_position': "Stranica {0} ostaje na poziciji {0}",
        'drag_error': "Greška pri premještanju",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Unos teksta s naprednim formatiranjem i upravljanjem tekstualnim blokovima",
        'text_templates': "Dostupni tekstualni blokovi:",
        'text_name': "Naziv",
        'text_preview': "Pregled teksta",
        'text_enter': "Tekst:",
        'text_font_size': "Veličina fonta:",
        'text_formatting': "Formatiranje:",
        'text_bold': "Podebljano",
        'text_italic': "Kurziv",
        'text_underline': "Podvučeno",
        'text_alignment': "Poravnanje:",
        'text_left': "Lijevo",
        'text_center': "Centrirano",
        'text_right': "Desno",
        'text_color': "Boja teksta:",
        'text_opacity': "Neprozirnost:",
        'text_word_wrap': "Prelamanje redova:",
        'text_auto': "Automatski",
        'text_page_width_95': "Širina stranice (95%)",
        'text_page_width_85': "Vrlo široko (85%)",
        'text_page_width_75': "Šire (75%)",
        'text_page_width_60': "Široko (60%)",
        'text_page_width_50': "Srednje (50%)",
        'text_page_width_30': "Usko (30%)",
        'text_page_width_20': "Uže (20%)",
        'text_page_width_10': "Vrlo usko (10%)",
        'text_no_wrap': "Bez prelamanja",
        'text_private': "Privatni tekstualni blok (zahtijeva autentifikaciju)",
        'text_preview_label': "Pregled:",
        'text_preview_placeholder': "Ovdje će se prikazati pregled teksta...",
        'text_no_text': "(Nema teksta)",
        'text_save_template': "💾 Sačuvaj kao blok",
        'text_delete_template': "🗑 Izbriši odabrani tekstualni blok",
        'text_show_private': "Prikaži privatne",
        'text_hide_private': "Sakrij privatne",
        'text_use': "✅ Koristi tekst",
        'text_saved': "Tekstualni blok sačuvan kao:\n{0}",
        'text_saved_voice': "Tekstualni blok sačuvan",
        'text_deleted': "Tekstualni blok izbrisan",
        'text_no_text_to_save': "Nema teksta za čuvanje.",
        'text_no_templates': "Nema pronađenih tekstualnih blokova",
        'text_private_master_required': "Privatni blokovi se mogu koristiti samo ako je postavljena glavna lozinka.\n\nŽelite li postaviti glavnu lozinku sada?",
        'text_filename': "Naziv fajla za tekstualni blok (bez 'Text_' i '.txt'):",
        'text_filename_hint': "Primjer: 'Telefon KućniUred' bit će sačuvan kao 'Text_Telefon KućniUred.txt'",
        'text_save_hint': "Tekstualni blok će biti automatski sačuvan s formatiranjem.",
        'text_guide_title': "Unos teksta – Vodič",
        'text_delete_confirm': "Jeste li sigurni da želite izbrisati tekstualni blok?\n\nFajl: {0}\nTekst: {1}...",
        'text_make_public': "Označi kao javno",
        'text_make_private': "Označi kao privatno",
        'text_privacy_changed': "Status privatnosti promijenjen",
        'text_private_always': "Privatni uvijek vidljivi (postavka)",
        'text_mode_required': "Molimo prvo uključite način rada za tekst",
        'text_continue_editing': "Nastavi uređivanje – kursor na kraju teksta",
        'text_no_input': "Nije unesen tekst – tekst odbačen",
        'save_dialog_question': "Kako želite nastaviti?",
        'text_save_question': "Sačuvati sve tekstove i križeve, prilagoditi, nastaviti uređivanje ili odbaciti?",
        'copy_cross': "Križ kopiran",
        'paste_cross': "Križ umetnut",
        'paste_text': "Tekst umetnut",
        'cross_discarded': "Križ odbačen",
        'all_discarded': "Sve odbačeno",
        'text_discarded': "Tekst odbačen",
        'no_texts_to_save': "Nema tekstova za čuvanje",
        'no_valid_texts': "Nema važećih tekstova za čuvanje",
        'text_word_singular': "tekst",
        'text_word_plural': "teksta",
        'cross_word_singular': "križ",
        'cross_word_plural': "križeva",
        'texts_saved_title': "Tekstovi sačuvani",
        'texts_crosses_saved': "{0} {1} i {2} {3} umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'texts_crosses_saved_voice': "{0} {1} i {2} {3} sačuvano.",
        'texts_saved': "{0} {1} umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'texts_saved_voice': "{0} {1} sačuvano.",
        'crosses_saved': "{0} {1} umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'crosses_saved_voice': "{0} {1} sačuvano.",
        'elements_saved': "{0} elemenata umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'elements_saved_voice': "{0} elemenata sačuvano.",
        'text_window_load_error': "Prozor za tekst nije mogao biti učitan",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Unos teksta i tekstualni blokovi – Detaljni vodič**

        **1. Umetanje i uređivanje teksta**
        - Kliknite desnim klikom na željeno mjesto u dokumentu i odaberite "Umetni tekst".
        - Otvorit će se dijalog u kojem možete unijeti i formatirati tekst:
        • Veličina fonta, podebljano, kurziv, podvučeno
        • Boja teksta (slobodan odabir)
        • Prozirnost (neprozirnost) pomoću klizača
        • Prelamanje redova (različite širine, npr. širina stranice, usko, bez prelamanja)
        - Nakon potvrde, tekst će se pojaviti na mjestu klika. Možete ga pomicati mišem ili strelicama.
        - Dvostruki klik na tekst otvara način uređivanja; ESC ga zatvara.

        **2. Upravljanje tekstualnim blokovima (šablonima)**
        - Na lijevoj strani dijaloga za tekst vidite listu svih sačuvanih tekstualnih blokova.
        - **Čuvanje bloka:** Unesite tekst, formatirajte ga i kliknite na "💾 Sačuvaj kao blok". Unesite naziv fajla (bez ekstenzije).
        - **Učitavanje bloka:** Kliknite na željeni naziv u listi. Tekst i formatiranje će se preuzeti i mogu se prilagoditi ako je potrebno.
        - **Brisanje:** Kliknite desnim klikom na blok da biste ga izbrisali ili promijenili status privatnosti.

        **3. Privatni tekstualni blokovi (glavna lozinka)**
        - Ako ste postavili glavnu lozinku (u Postavke → Upravljanje lozinkama), možete označiti blokove kao "privatne".
        - Označite polje "Privatni tekstualni blok" u dijalogu prije čuvanja.
        - Privatni blokovi se prikazuju u listi samo ako ste jednom po sesiji unijeli svoju glavnu lozinku (autentifikacija putem ikone lokota ili pri prvom pristupu).
        - Na taj način možete zaštititi povjerljive tekstualne blokove od neovlaštenog pristupa.

        **4. Umetanje križeva**
        - Iz kontekstualnog menija možete umetnuti i grafički križ (npr. za polja za potvrdu).
        - Veličinu, debljinu linije i boju križeva možete globalno prilagoditi u postavkama (meni "Postavke" → "Postavke križeva").
        - Kliknite desnim klikom na postojeći križ da biste ga pojedinačno promijenili.

        **5. Grupne radnje**
        - Ako ste na jednu stranicu postavili više tekstova ili križeva, možete ih sve zajedno sačuvati ili odbaciti iz kontekstualnog menija (desni klik u načinu rada za tekst).
        - Prilikom čuvanja, svi elementi se ugrađuju u PDF i ostaju kao vektorska grafika.

        **6. Prečice na tastaturi u načinu rada za tekst**
        - Strelice: pomicanje elementa
        - Ctrl+strelice: veći koraci
        - Enter: otvaranje dijaloga za čuvanje (sačuvaj sve / prilagodi / odbaci)
        - ESC: odbacivanje trenutnog elementa
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Unos teksta i tekstualni blokovi – Detaljni vodič</strong></p>

        <p><strong>1. Umetanje i uređivanje teksta</strong></p>
        <ul>
        <li>Kliknite desnim klikom na željeno mjesto u dokumentu i odaberite "Umetni tekst".</li>
        <li>Otvorit će se dijalog u kojem možete unijeti i formatirati tekst:<br/>
        • Veličina fonta, podebljano, kurziv, podvučeno<br/>
        • Boja teksta (slobodan odabir)<br/>
        • Prozirnost (neprozirnost) pomoću klizača<br/>
        • Prelamanje redova (različite širine, npr. širina stranice, usko, bez prelamanja)</li>
        <li>Nakon potvrde, tekst će se pojaviti na mjestu klika. Možete ga pomicati mišem ili strelicama.</li>
        <li>Dvostruki klik na tekst otvara način uređivanja; ESC ga zatvara.</li>
        </ul>

        <p><strong>2. Upravljanje tekstualnim blokovima (šablonima)</strong></p>
        <ul>
        <li>Na lijevoj strani dijaloga za tekst vidite listu svih sačuvanih tekstualnih blokova.</li>
        <li><strong>Čuvanje bloka:</strong> Unesite tekst, formatirajte ga i kliknite na "💾 Sačuvaj kao blok". Unesite naziv fajla (bez ekstenzije).</li>
        <li><strong>Učitavanje bloka:</strong> Kliknite na željeni naziv u listi. Tekst i formatiranje će se preuzeti i mogu se prilagoditi ako je potrebno.</li>
        <li><strong>Brisanje:</strong> Kliknite desnim klikom na blok da biste ga izbrisali ili promijenili status privatnosti.</li>
        </ul>

        <p><strong>3. Privatni tekstualni blokovi (glavna lozinka)</strong></p>
        <ul>
        <li>If you have set a master password (in Settings → Password Management), you can mark blocks as "private".</li>
        <li>Check the "Private text block" box in the dialog before saving.</li>
        <li>Private blocks are only displayed in the list if you have entered your master password once per session (authentication via the lock icon or on first access).</li>
        <li>This way you can protect confidential text blocks from unauthorized access.</li>
        </ul>

        <p><strong>4. Inserting crosses</strong></p>
        <ul>
        <li>From the context menu you can also insert a graphic cross (e.g. for checkboxes).</li>
        <li>The size, line width and color of crosses can be adjusted globally in the settings (menu "Settings" → "Cross settings").</li>
        <li>Right-click on an existing cross to change it individually.</li>
        </ul>

        <p><strong>5. Batch actions</strong></p>
        <ul>
        <li>If you have placed several texts or crosses on one page, you can save or discard them all at once from the context menu (right click in text mode).</li>
        <li>When saving, all elements are embedded in the PDF and remain as vector graphics.</li>
        </ul>

        <p><strong>6. Keyboard shortcuts in text mode</strong></p>
        <ul>
        <li>Arrow keys: move element</li>
        <li>Ctrl+arrow keys: larger steps</li>
        <li>Enter: open save dialog (save all / adjust / discard)</li>
        <li>ESC: discard current element</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Postavke križeva",
        'cross_properties': "Svojstva križa",
        'cross_size': "Veličina (px):",
        'cross_line_width': "Debljina linije:",
        'cross_color': "Boja:",
        'cross_choose_color': "Odaberi",
        'cross_fine_tuning': "Fino podešavanje pri čuvanju (pikseli)",
        'cross_offset_x': "Pomak X:",
        'cross_offset_y': "Pomak Y:",
        'cross_offset_x_tooltip': "Negativne vrijednosti pomiču križ ulijevo pri čuvanju, pozitivne udesno",
        'cross_offset_y_tooltip': "Negativne vrijednosti pomiču križ prema gore pri čuvanju, pozitivne prema dolje",
        'cross_preview': "Pregled",
        'cross_save': "Primijeni postavke",
        'cross_customized': "Križ prilagođen",
        'cross_settings_applied': "Postavke križeva sačuvane.\nVeličina: {0}px, debljina linije: {1}px\n{2}",
        'cross_updated_count': "Ažurirano {0} postojećih križeva.",
        'cross_no_crosses': "Nema pronađenih postojećih križeva.",
        'cross_settings_applied_all': "Postavke križeva primijenjene na svih {0} križeva",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Postavke potpisa",
        'signature_1': "Potpis 1",
        'signature_2': "Potpis 2",
        'signature_select': "Odaberi potpis",
        'signature_add': "➕ Dodaj novi potpis...",
        'signature_size': "Veličina za potpis {0} (%):",
        'signature_common': "Opće postavke",
        'signature_timestamp': "Automatski dodaj vremensku oznaku",
        'signature_location': "Zadano mjesto:",
        'signature_timestamp_size': "Veličina fonta vremenske oznake:",
        'signature_no_files': "-- Nema pronađenih potpisa --",
        'signature_insert': "Umetni potpis",
        'signature_insert_1': "Umetni potpis 1",
        'signature_insert_2': "Umetni potpis 2",
        'signature_customize': " Prilagodi potpis",
        'signature_discard': " Odbaci ovaj potpis",
        'signature_save_all': " Sačuvaj sve potpise",
        'signature_discard_all': " Odbaci sve potpise",
        'signature_guide_title': "Potpisi – Vodič",
        'signature_guide': """
📝 Potpisi – Kratki vodič

- Postavite glavnu lozinku
- Konfigurišite potpise u meniju Postavke
  (veličina, vremenska oznaka ...)
- Umetnite DESNIM KLIKOM na željenom mjestu
  (glavna lozinka potrebna jednom po sesiji)
- Pomjerite potpis mišem ili strelicama
- Može se umetnuti više potpisa jedan za drugim
- Svaki potpis se može pojedinačno prilagoditi
- Odbacite pojedinačni potpis
- Sačuvajte / odbacite sve potpise odjednom
- Alternativno, možete koristiti i traku menija.
        """,
        'signature_placeholder': "Pregled nije dostupan",
        'signature_info': "Potpis {0}: {1}×{2} px ({3}% od {4}×{5})",
        'signature_info_placeholder': "Postavke za potpis {0}",
        'signature_inserted': "Potpis {0} umetnut na stranicu {1}",
        'signature_deleted': "Potpis izbrisan",
        'signature_copied': "Potpis kopiran",
        'signature_pasted': "Potpis {0} umetnut",
        'signature_saved': "{0} potpisa umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'signature_saved_voice': "{0} potpisa sačuvano",
        'mode_replace_signature_format': "Izađi iz načina i umetni potpis {0}",
        'mode_conflict_voice_signature': "Način {0} je aktivan. Izaći i umetnuti potpis?",
        'signature_not_configured': "Potpis {0} nije konfigurisan",
        'signature_file_not_found': "Fajl potpisa nije pronađen",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nema kopiranog potpisa",
        'no_signatures_to_save': "Nema potpisa za čuvanje",
        'signature_save_question': "Sačuvati sve potpise, prilagoditi ili odbaciti ovaj?",
        'signatures_saved_title': "Potpisi sačuvani",
        'signatures_saved': "{0} potpisa umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'signatures_saved_voice': "{0} potpisa sačuvano.",
        'all_signatures_discarded': "Svi potpisi odbačeni",
        'signature_settings_saved': "Postavke potpisa sačuvane",
        'signature_cancelled': "Potpis odbačen",
        'signature_active_title': "Potpis aktivan",
        'signature_replace_question': "Potpis je već aktivan.\n\nŽelite li zamijeniti trenutni potpis?",
        'signature_replace': "Zamijeni potpis",
        'signature_replace_voice': "Zamijeniti trenutni potpis ili otkazati?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Postavke slika",
        'image_common': "Opće postavke slika",
        'image_keep_aspect': "Zadrži omjer stranica prilikom prevlačenja",
        'image_default_size': "Zadana veličina (%):",
        'image_dark_invert': "Invertiraj slike u tamnom načinu",
        'image_dark_invert_tooltip': "Uključeno: slike se invertiraju za bolju vidljivost",
        'image_fine_tuning': "Fino podešavanje (pikseli)",
        'image_offset_x': "Pomak X:",
        'image_offset_y': "Pomak Y:",
        'image_offset_x_tooltip': "Negativne vrijednosti pomiču sliku ulijevo pri čuvanju, pozitivne udesno",
        'image_offset_y_tooltip': "Negativne vrijednosti pomiču sliku prema gore pri čuvanju, pozitivne prema dolje",
        'image_select': "Odaberi sliku",
        'image_insert': "Umetni sliku",
        'image_customize': " Prilagodi sliku",
        'image_aspect': " Zadrži omjer stranica",
        'image_discard': " Odbaci ovu sliku",
        'image_save_all': " Sačuvaj sve slike",
        'image_discard_all': " Odbaci sve slike",
        'image_filter': "Slike",
        'image_guide_title': "Umetanje slika – Vodič",
        'image_guide': """
📷 Umetanje slika u PDF – Kratki vodič:

1. Kliknite desnim klikom na željeno mjesto
2. "Umetni sliku" → odaberite sliku
3. Pozicionirajte sliku: prevucite mišem
4. Prilagodite veličinu: prevucite za uglove/ivice
5. Zadržite omjer stranica: tipka [A]
6. Daljnja prilagođavanja: desni klik na sliku

Savjet: U kontekstualnom meniju možete prilagoditi postavke.
        """,
        'image_inserted': "Slika umetnuta na stranicu {1}",
        'image_deleted': "Slika odbačena",
        'image_copied': "Slika kopirana",
        'image_pasted': "Slika umetnuta",
        'image_saved': "{0} slika umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'image_saved_voice': "{0} slika sačuvano",
        'image_aspect_on': "uključeno",
        'image_aspect_off': "isključeno",
        'image_aspect_toggle': "Zadrži omjer stranica {0}",
        'image_reset': "Slika vraćena na originalnu veličinu",
        'image_replaced': "Slika zamijenjena",
        'image_invalid': "Nevažeća slika",
        'mode_replace_image': "Umetni sliku",
        'mode_conflict_voice_image': "Način {0} je aktivan. Izaći i umetnuti sliku?",
        'image_active_title': "Slika aktivna",
        'image_replace_question': "Slika je već aktivna.\n\nŽelite li zamijeniti trenutnu sliku?",
        'image_replace': "Zamijeni sliku",
        'image_replace_voice': "Zamijeniti trenutnu sliku ili otkazati?",
        'image_filter_all': "Slike (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Svi fajlovi (*.*)",
        'no_copied_image': "Nema kopirane slike",
        'image_discarded': "Slika odbačena",
        'image_save_question': "Sačuvati sve slike, prilagoditi ili odbaciti ovu?",
        'no_images_to_save': "Nema slika za čuvanje",
        'no_valid_images': "Nema važećih slika za čuvanje",
        'images_saved_title': "Slike sačuvane",
        'images_saved': "{0} slika umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'images_saved_voice': "{0} slika sačuvano.",
        'all_images_discarded': "Sve slike odbačene",
        'image_settings_updated': "Postavke slika ažurirane",
        'image_replace_title': "Odaberi novu sliku",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Postavke oblika",
        'form_basic': "Osnovne postavke",
        'form_default_type': "Zadani tip oblika:",
        'form_rectangle': "Pravougaonik",
        'form_ellipse': "Elipsa",
        'form_line': "Linija",
        'form_arrow': "Strelica",
        'form_line_width': "Debljina linije:",
        'form_colors': "Boje",
        'form_line_color': "Boja linije:",
        'form_fill_color': "Boja ispune:",
        'form_choose_color': "Odaberi",
        'form_transparent': "Prozirna pozadina (samo linija)",
        'form_filled': "ispunjeno",
        'form_dark_mode': "Tamni način",
        'form_dark_invert': "Invertiraj boje u tamnom načinu",
        'form_fine_tuning': "Fino podešavanje (pikseli)",
        'form_offset_x': "Pomak X:",
        'form_offset_y': "Pomak Y:",
        'form_offset_x_tooltip': "Negativne vrijednosti pomiču oblik ulijevo pri čuvanju, pozitivne udesno",
        'form_offset_y_tooltip': "Negativne vrijednosti pomiču oblik prema gore pri čuvanju, pozitivne prema dolje",
        'form_preview': "Pregled",
        'form_insert': "Umetni oblik",
        'form_rectangle_insert': "Pravougaonik",
        'form_ellipse_insert': "Elipsa/krug",
        'form_line_insert': "Linija (2 klika)",
        'form_arrow_insert': "Strelica (2 klika)",
        'form_customize': " Prilagodi oblik",
        'form_transparent_toggle': " Prozirna pozadina",
        'form_discard': " Odbaci ovaj oblik",
        'form_save_all': " Sačuvaj sve oblike",
        'form_discard_all': " Odbaci sve oblike",
        'form_guide_title': "Umetanje oblika – Vodič",
        'form_guide': """
📐 Umetanje oblika u PDF – Kratki vodič:

1. Odaberite tip oblika (pravougaonik, elipsa, linija, strelica)
2. Kliknite na mjesto
   - Pravougaonik/elipsa: jedan klik postavlja oblik
   - Linija/strelica: dva klika za početnu i završnu tačku
3. Pozicionirajte oblik: prevucite mišem
4. Prilagodite veličinu: prevucite za uglove/ivice
5. Sačuvaj oblik: Enter
6. Odbaci oblik: ESC
7. Daljnja prilagođavanja: desni klik na oblik

Savjet: U kontekstualnom meniju možete prilagoditi postavke.
        """,
        'form_inserted': "{0} umetnut na stranicu {1}",
        'form_deleted': "Oblik izbrisan",
        'form_copied': "Oblik kopiran",
        'form_pasted': "Oblik umetnut",
        'form_saved': "{0} oblika umetnuto je u PDF.\n\nPDF je ponovo učitan...",
        'form_saved_voice': "{0} oblika sačuvano",
        'form_reset': "Oblik vraćen na zadanu veličinu",
        'form_transparent_on': "uključeno",
        'form_transparent_off': "isključeno",
        'form_transparent_toggled': "Prozirna pozadina {0}",
        'form_line_cancel': "Crtanje linije otkazano",
        'form_second_click': "Sada kliknite završnu tačku za {0}",
        'mode_replace_form': "Umetni oblik",
        'mode_conflict_voice_form': "Način {0} je aktivan. Izaći i umetnuti oblik?",
        'form_settings_updated': "Postavke oblika ažurirane",
        'form_unknown': "Oblik",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Kliknite na početnu tačku",
        'form_line_guide_2': "2. Kliknite na završnu tačku",
        'form_line_guide_3': "Linija će biti nacrtana između dvije tačke.",
        'form_line_status_1': "Čekanje na prvi klik...",
        'form_line_status_2': "Prva tačka postavljena: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Sada kliknite završnu tačku...",
        'form_line_status_4': "Obje tačke postavljene.\nKliknite 'Gotovo' za čuvanje.",
        'form_line_reset': "Resetuj",
        'form_line_finish': "Gotovo",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopiraj (Cmd+C)",
        'paste': "Zalijepi (Cmd+V)",
        'copied': "Kopirano: {0}",
        'no_element_to_copy': "Nijedan element nije odabran za kopiranje",
        'no_copied_data': "Nema kopiranih podataka",
        'no_valid_position': "Nema važeće pozicije za lijepljenje",
        'copy_text': "Tekst kopiran",
        'copy_image': "Slika kopirana",
        'copy_form': "Oblik kopiran",
        'copy_signature': "Potpis kopiran",
        'element_text': "Tekst",
        'element_image': "Slika",
        'element_form': "Oblik",
        'element_signature': "Potpis",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflikt načina",
        'mode_conflict_message': "Način '{0}' je već aktivan.\n\nŽelite li izaći iz njega i {1}?",
        'mode_replace': "Izađi iz načina i {0}",
        'mode_cancel': "Otkaži",
        'mode_replace_text': "umetnuti tekst",
        'mode_replace_cross': "umetnuti križ",
        'mode_replace_signature': "umetnuti potpis",
        'mode_replace_image': "umetnuti sliku",
        'mode_replace_form': "umetnuti oblik",
        'mode_conflict_voice': "Način {0} je aktivan. Izaći i umetnuti tekst?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Unos teksta",
        'active_mode_signature': "Potpis",
        'active_mode_image': "Slika",
        'active_mode_form': "Oblik",
        'active_mode_and': " i ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Umetni",
        'insert_another_text': "Umetni tekst",
        'insert_another_cross': "Umetni križ",
        'insert_another_signature_1': "Potpis 1",
        'insert_another_signature_2': "Potpis 2",
        'insert_another_image': "Umetni sliku",
        'insert_another_form_rect': "Pravougaonik",
        'insert_another_form_ellipse': "Elipsa",
        'insert_another_form_line': "Linija (2 klika)",
        'insert_another_form_arrow': "Strelica (2 klika)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Sačuvaj {0}",
        'save_dialog_message': "{0} će biti sačuvan na stranici {1}.\n\nKako želite nastaviti?",
        'save_all': "Sačuvaj sve {0}",
        'save_single': "Sačuvaj {0}",
        'save_customize': "Prilagodi {0}",
        'save_discard': "Odbaci ovaj {0}",
        'save_continue': "Nastavi uređivanje",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Idi na stranicu {0}",
        'context_rotate': " Okreni stranicu {0}",
        'context_delete': " Izbriši stranicu {0}",
        'context_export': " Izvezi stranicu {0}",
        'context_mark_as': " Označi stranicu kao...",
        'context_mark_empty': " Prazna stranica",
        'context_unmark_empty': " Nije više prazna",
        'context_mark_export': " Označi za izvoz",
        'context_unmark_export': " Ne izvozi više",
        'context_batch_actions': " Grupne radnje",
        'context_batch_delete_empty': " Izbriši svih {0} praznih stranica",
        'context_batch_export_single': " Izvezi svih {0} stranica (jedan fajl)",
        'context_batch_export_split': " Izvezi svih {0} stranica (odvojeno)",
        'context_drag_start': " Pokreni prevlačenje",
        'context_drag_stop': " Zaustavi prevlačenje",
        'context_insert': " Umetni",
        'context_insert_pages': " Umetni stranice",
        'context_zoom': "Zum",
        'discard_mixed': "Odbaci svih {0} {1} i {2} {3}",
        'save_mixed': "Sačuvaj {0} {1} i {2} {3}",
        'discard_texts': "Odbaci svih {0} tekstova",
        'discard_text_single': "Odbaci 1 tekst",
        'save_texts': "Sačuvaj {0} tekstova",
        'save_text_single': "Sačuvaj 1 tekst",
        'discard_crosses': "Odbaci svih {0} križeva",
        'discard_cross_single': "Odbaci 1 križ",
        'save_crosses': "Sačuvaj {0} križeva",
        'save_cross_single': "Sačuvaj 1 križ",
        'discard_signatures': "Odbaci svih {0} potpisa",
        'save_signature_single': "Sačuvaj 1 potpis",
        'save_signatures': "Sačuvaj {0} potpisa",
        'discard_images': "Odbaci svih {0} slika",
        'save_image_single': "Sačuvaj 1 sliku",
        'save_images': "Sačuvaj {0} slika",
        'discard_forms': "Odbaci svih {0} oblika",
        'save_form_single': "Sačuvaj 1 oblik",
        'save_forms': "Sačuvaj {0} oblika",
        'cross_discard': "Odbaci ovaj križ",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informacije o izvozu / uvozu",
        'export_what': "📋 Šta se izvozi?",
        'export_general': "Opće postavke",
        'export_general_items': "• Glasovni izlaz (uklj./isklj., brzina)\n• Tamni/svijetli način\n• Postavke rezervnog kopiranja\n• Postavke OCR-a",
        'export_image_form': "Postavke slika i oblika",
        'export_image_form_items': "• Postavke slika (omjer stranica, zadana veličina)\n• Postavke oblika (debljina linije, boje)\n• Postavke potpisa (putanje, veličine, vremenska oznaka)",
        'export_passwords': "Baza podataka lozinki",
        'export_passwords_items': "• Sve sačuvane PDF lozinke\n• Po izboru šifrovane ili dešifrovane",
        'export_master': "Postavke glavne lozinke",
        'export_master_items': "• Hash glavne lozinke\n• Postavke za potpise/tekstualne blokove",
        'export_signatures': "Potpisi i tekstualni blokovi",
        'export_signatures_items': "• Svi slikovni fajlovi (potpisi)\n• Svi tekstualni blokovi s formatiranjem\n• Oznake privatno/javno",
        'export_import_warning': "⚠️ Važne napomene",
        'export_import_note': "• Prilikom uvoza, SVE trenutne postavke će biti prepisane\n• Potrebno je ponovno pokretanje aplikacije\n• Postojeći potpisi/tekstualni blokovi će biti zamijenjeni",
        'export_master_note': "• Ako je glavna lozinka postavljena, možete odabrati:\n  - Dešifrovano (lozinke u čistom tekstu)\n  - Šifrovano (čitljivo samo s glavnom lozinkom)",
        'export_security': "• Izvezeni ZIP fajl sadrži povjerljive podatke\n• Čuvajte ga na sigurnom mjestu (npr. šifrovani USB stick)\n• Ako izgubite fajl, lozinke su nepovratno izgubljene",
        'export_format': "📁 Format izvoza",
        'export_format_desc': "Postavke se čuvaju u jednom ZIP fajlu:",
        'export_filename': "Postavke_PDFDarkView_GGGGMMDD_HHMMSS.zip",
        'export_success': "Postavke su uspješno izvezene",
        'export_failed': "Izvoz nije uspio",
        'export_import_question': "Želite li ponovo pokrenuti aplikaciju sada?",
        'export_password_question': "Glavna lozinka je postavljena.\n\nŽelite li izvesti lozinke dešifrovane?\n(inače će biti izvezene šifrovane)",
        'export_decrypt': "Izvezi dešifrovano",
        'export_encrypt': "Izvezi šifrovano",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informacije",
        'info_title': "O PDF Dark View-u",
        'info_version': "Verzija",
        'info_author': "Razvio Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "O programu",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> je pristupačan PDF preglednik, posebno razvijen za osobe s oštećenjem vida.</p>

            <p><strong>Ključne karakteristike:</strong></p>
            <ul>
                <li>Kontrastno, prilagodljivo sučelje</li>
                <li>Potpuna kontrola pomoću tastature</li>
                <li>Integrirana govorna podrška</li>
                <li>OCR za skenirane dokumente</li>
                <li>Opsežni alati za uređivanje</li>
            </ul>

            <p>Podržano je više od 50 jezika – tako da su PDF-ovi pristupačni svima.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkcije",
        'info_features_intro': "PDF Dark View vam nudi sljedeće mogućnosti:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Prikaz & Navigacija</strong> – Tamni/Svijetli način rada, listanje stranica, zumiranje, skok na stranicu</li>
            <li><strong>OCR (Prepoznavanje teksta)</strong> – Učinite skenirane dokumente pretraživim i kopirajivim</li>
            <li><strong>Uređivanje</strong> – Ubacivanje teksta, križeva, potpisa, slika i oblika</li>
            <li><strong>Upravljanje stranicama</strong> – Brisanje, izdvajanje, umetanje, premještanje putem 'povuci i ispusti'</li>
            <li><strong>Izvoz</strong> – U Word, Pages ili kao tekst</li>
            <li><strong>Sigurnost</strong> – Zaštita i upravljanje lozinkom</li>
            <li><strong>Pristupačnost</strong> – Govorna podrška, kontrola pomoću tastature, visok kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Upotreba",
        'info_accessibility': "♿ Pristupačnost – potpuna kontrola pomoću tastature",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Općenito</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Otvori PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Pretraga</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Prebaci između tamnog/svijetlog načina</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Štampaj</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Zatvori</div>

        <div class="shortcut-cat">📖 Navigacija</div>
        <div class="shortcut-row"><kbd>Strelica</kbd> Listanje stranicu po stranicu</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Idi na stranicu</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Prva stranica</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Posljednja stranica</div>

        <div class="shortcut-cat">✏️ Uređivanje</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Ubaci tekst</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Obriši stranice</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Izdvoji stranice</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Umetni stranice</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Premjesti stranice</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rotiraj stranicu</div>

        <div class="shortcut-cat">🖼️ Premještanje elemenata</div>
        <div class="shortcut-row"><kbd>Strelica</kbd> Premjesti tekst/sliku/potpis</div>
        <div class="shortcut-row"><kbd>Ctrl+Strelica</kbd> Veći koraci</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Spremi</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Odbaci</div>

        <div class="shortcut-cat">🗣️ Govorna podrška</div>
        <div class="shortcut-row"><kbd>F2</kbd> Uključi/isključi govornu podršku</div>
        """,
        'info_contextmenu': "📌 Važno: Sve funkcije su također dostupne putem kontekstnog izbornika (desni klik miša)!",
        'info_accessibility_hint': "💡 Savjet: Govorna podrška (F2) olakšava orijentaciju i daje povratne informacije o izbornicima i dijalozima.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licenca & Impresum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUM</strong><br>
        Podaci prema § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Njemačka<br>
        E-pošta: binhdiez64@gmail.com<br>
        Odgovoran za sadržaj: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Odricanje od odgovornosti</strong><br>
        Softver je razvijen s najvećom pažnjom. Ne preuzima se garancija za tačnost, potpunost i funkcionalnost. Upotreba je na vlastitu odgovornost.<br><br>

        <strong>📄 MIT licenca (privatna upotreba)</strong><br>
        Autorska prava (c) 2026 Toralf Schulz (BinhDiez)<br>
        Dozvoljeno: besplatna upotreba, privatne izmjene, lične kopije.<br>
        Nije dozvoljeno: prodaja, komercijalna upotreba, uklanjanje napomena o autorskim pravima.<br><br>

        <strong>🔧 Komponente trećih strana</strong><br>
        Ovaj softver sadrži komponente pod GPL, AGPL, Apache 2.0, BSD i MIT licencama.<br>
        Prilikom daljeg dijeljenja moraju se poštovati odgovarajući uvjeti licence.<br><br>

        <strong>🌐 Otvoreni kod</strong><br>
        Izvorni kod je dostupan i može se pregledati, mijenjati i dalje dijeliti u skladu s odgovarajućim uvjetima licence.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Zahvale",
        'info_credits': "Zahvala open-source zajednici",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Obrada PDF-a</li>
            <li><strong>PyQt5</strong> – Grafičko sučelje</li>
            <li><strong>Tesseract OCR</strong> – Prepoznavanje teksta</li>
            <li><strong>OCRmyPDF</strong> – OCR integracija</li>
            <li><strong>python-docx</strong> – Izvoz u Word</li>
            <li><strong>qtawesome</strong> – Ikone</li>
            <li><strong>DeepSeek</strong> – Podrška za prijevode (50+ jezika)</li>
            <li><strong>Svi korisnici</strong> – Za vrijedne povratne informacije</li>
            <li><strong>Open-source zajednici</strong> – Za sjajne biblioteke</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Jezici",
        'info_languages_header': "🌍 Jezička podrška",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View trenutno podržava <strong>62 jezika</strong> – kako bi softver mogao biti korišten bez barijera širom svijeta.</p>

            <p><strong>📖 Potpuna lista jezika (Stanje: Mart 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanski (Shqip)</li>
                    <li>🇩🇿 Arapski (العربية)</li>
                    <li>🇮🇩 Balijski (Basa Bali)</li>
                    <li>🇧🇩 Bengalski (বাংলা)</li>
                    <li>🇲🇲 Burmanski (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosanski (Bosanski)</li>
                    <li>🇧🇬 Bugarski (Български)</li>
                    <li>🇨🇳 Kineski (中文)</li>
                    <li>🇩🇰 Danski (Dansk)</li>
                    <li>🇩🇪 Njemački (Deutsch)</li>
                    <li>🇬🇧 Engleski (English)</li>
                    <li>🇪🇪 Estonski (Eesti)</li>
                    <li>🇫🇮 Finski (Suomi)</li>
                    <li>🇫🇷 Francuski (Français)</li>
                    <li>🇬🇷 Grčki (Ελληνικά)</li>
                    <li>🇮🇱 Hebrejski (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Hrvatski (Hrvatski)</li>
                    <li>🇭🇺 Mađarski (Magyar)</li>
                    <li>🇮🇩 Indonezijski (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irski (Gaeilge)</li>
                    <li>🇮🇸 Islandski (Íslenska)</li>
                    <li>🇮🇹 Italijanski (Italiano)</li>
                    <li>🇯🇵 Japanski (日本語)</li>
                    <li>🇰🇭 Kmerski (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korejski (한국어)</li>
                    <li>🇱🇦 Laoški (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvijski (Latviešu)</li>
                    <li>🇱🇹 Litvanski (Lietuvių)</li>
                    <li>🇱🇺 Luksemburški (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajski (Bahasa Melayu)</li>
                    <li>🇮🇳 Marati (मराठी)</li>
                    <li>🇲🇳 Mongolski (Монгол)</li>
                    <li>🇳🇵 Nepalski (नेपाली)</li>
                    <li>🇳🇱 Nizozemski (Nederlands)</li>
                    <li>🇳🇴 Norveški (Norsk)</li>
                    <li>🇦🇫 Paštunski (پښتو)</li>
                    <li>🇮🇷 Perzijski (فارسی)</li>
                    <li>🇵🇱 Poljski (Polski)</li>
                    <li>🇵🇹 Portugalski (Português)</li>
                    <li>🇮🇳 Pandžapski (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumunski (Română)</li>
                    <li>🇷🇺 Ruski (Русский)</li>
                    <li>🇸🇪 Švedski (Svenska)</li>
                    <li>🇷🇸 Srpski (Српски)</li>
                    <li>🇸🇰 Slovački (Slovenčina)</li>
                    <li>🇸🇮 Slovenski (Slovenščina)</li>
                    <li>🇪🇸 Španski (Español)</li>
                    <li>🇹🇿 Svahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamilski (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Tajlandski (ไทย)</li>
                    <li>🇨🇿 Češki (Čeština)</li>
                    <li>🇹🇷 Turski (Türkçe)</li>
                    <li>🇺🇦 Ukrajinski (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vijetnamski (Tiếng Việt)</li>
                    <li>🇸🇳 Volof (Wolof)</li>
                    <li>🇺🇸 Jidiš (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Dodajte vlastite jezike:</strong><br>
                Želite li jezik koji još nije uključen? Jednostavno postavite vlastitu datoteku rječnika (<code>sprache_xx.py</code>) pored aplikacije – softver će je automatski prepoznati. Ako ste zainteresirani za poseban prijevod, slobodno me kontaktirajte.
            </div>

            <p><strong>🙏 Posebna zahvala:</strong> DeepSeek-u za podršku pri prijevodu svih rječnika na 62 jezika.</p>

            <p>📧 Kontakt za prijevode: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Greška",
        'error_occurred': "Došlo je do greške",
        'error_pdf_load': "Greška pri učitavanju PDF-a",
        'error_pdf_save': "Greška pri čuvanju PDF-a",
        'error_ocr': "Greška pri prepoznavanju teksta",
        'error_no_pdf': "Nijedan PDF nije učitan",
        'error_page_not_found': "Stranica nije pronađena",
        'error_invalid_range': "Nevažeći raspon stranica",
        'error_file_not_found': "Fajl nije pronađen",
        'error_permission': "Nema dozvole",
        'error_unknown': "Nepoznata greška",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Uspjeh",
        'success_operation': "Operacija uspješno završena",
        'success_saved': "Uspješno sačuvano",
        'success_exported': "Uspješno izvezeno",
        'success_imported': "Uspješno uvezeno",
        'success_deleted': "Uspješno izbrisano",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Potvrda",
        'confirm_yes': "Da",
        'confirm_no': "Ne",
        'confirm_ok': "OK",
        'confirm_cancel': "Otkaži",
        'confirm_delete': "Izbriši",
        'confirm_overwrite': "Prepiši",
        'confirm_continue': "Nastavi",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Učitavanje PDF-a...",
        'progress_saving': "Čuvanje PDF-a...",
        'progress_exporting': "Izvoz PDF-a...",
        'progress_processing': "Obrada...",
        'progress_wait': "Molimo pričekajte...",
        'progress_preparing': "Priprema...",
        'progress_finalizing': "Finalizacija...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Bijela",
        'color_black': "Crna",
        'color_red': "Crvena",
        'color_green': "Zelena",
        'color_blue': "Plava",
        'color_yellow': "Žuta",
        'color_magenta': "Magenta",
        'color_cyan': "Cijan",
        'color_orange': "Narandžasta",
        'color_gray': "Siva",
        'color_custom': "Odabir boje",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fajl",
        'menu_edit': "&Uredi",
        'menu_view': "&Pogled",
        'menu_tools': "&Alati",
        'menu_settings': "&Postavke",
        'menu_help': "&Pomoć",
        'menu_language': "🌐 Jezik",
        'menu_guides': "&Vodiči",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Otvori",
        'file_save_as': "&Sačuvaj kao...",
        'file_protect': "&Zaštiti dokument...",
        'file_export': "&Izvezi",
        'file_export_pages': "Izvezi u Pages",
        'file_export_word': "Izvezi u DOCX",
        'file_export_text': "Izvezi u TXT",
        'file_print_now': "&Štampaj odmah",
        'file_print': "&Štampaj",
        'file_close': "&Zatvori",
        'file_quit': "&Izlaz",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Pretraži",
        'edit_ocr': " Pokreni OCR",
        'edit_rotate': "&Okreni stranicu",
        'edit_rotate_all': "Okreni &sve stranice",
        'edit_delete_pages': "&Izbriši stranice",
        'edit_extract_pages': "&Izdvoj stranice",
        'edit_insert_pages': "&Umetni stranice",
        'edit_move_pages': "&Premjesti stranice",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Umetni tekst i križeve",
        'text_insert': " Umetni tekst",
        'cross_insert': " Umetni križ",
        'text_customize': " Prilagodi tekst",
        'cross_customize': " Prilagodi ovaj križ",
        'cross_customize_all': " Prilagodi sve križeve",
        'text_discard': " Odbaci ovaj tekst/križ",
        'text_discard_all': " Odbaci sve tekstove i križeve",
        'text_save_all': " Sačuvaj sve tekstove i križeve",
        'text_guide': " Unos teksta / tekstualni blokovi – vodič",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Umetni potpis",
        'signature_settings_menu': " Postavke...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Umetni sliku",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Umetni oblike",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Prikaži prozor za tekst",
        'view_zoom': "&Zum",
        'view_zoom_page': "&Širina stranice (zadano)",
        'view_zoom_two': "&Dvije stranice",
        'view_zoom_overview': "&Pregled (više stranica)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Pristupačnost",
        'settings_voice': "Glasovni izlaz",
        'settings_voice_tooltip': "dopunjuje glasovni izlaz čitača ekrana dodatnim informacijama",
        'settings_signature': "&Postavke potpisa",
        'settings_password': "&Upravljanje lozinkama",
        'settings_backup': "Napravi rezervnu kopiju prije promjena",
        'settings_export_import': "&Izvezi postavke / uvezi postavke",
        'settings_export': "&Izvezi sve postavke...",
        'settings_import': "&Uvezi sve postavke...",
        'settings_export_info': "&Šta se izvozi?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "uklj",
        'voice_off': "isklj",
        'voice_toggle': "Glasovni izlaz {0}",
        'voice_speed': "Brzina {0} posto",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Alat nije pronađen:\n{0}\n\nBASE_DIR: {1}\nProvjerite da su PDF alati instalirani u direktorij {1}.",
        'tool_started': "{0} pokrenut",
        'tool_start_failed': "Nije mogao biti pokrenut",
        'process_error_failed_to_start': "Proces nije mogao biti pokrenut. Da li fajl postoji?",
        'process_error_crashed': "Proces se srušio tokom pokretanja.",
        'process_error_timeout': "Dostignuto je vremensko ograničenje procesa.",
        'process_error_write': "Greška pri pisanju u proces.",
        'process_error_read': "Greška pri čitanju iz procesa.",
        'process_error_unknown': "Nepoznata greška procesa",
        'process_command': "Komanda",
        'process_normal_exit': "normalno završen",
        'process_crashed': "srušio se",
        'process_nonzero_exit': "{0} je završen sa kodom greške {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Otkazivanje...",
        'move_cancelling': "Premještanje se otkazuje",
        'opening_pdf': "Otvaranje PDF-a...",
        'loading_document': "Učitavanje dokumenta...",
        'pdf_opened': "PDF otvoren",
        'pages_found_moving': "Pronađeno {0} stranica, {1} za premještanje",
        'creating_backup': "Pravljenje rezervne kopije...",
        'backup_description': "Rezervno kopiranje originalnog fajla...",
        'backup_saved_as': "Rezervna kopija sačuvana kao: {0}",
        'error_format': "Greška: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Pretraga resetovana",
        'page_header_simple': "=== Stranica {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Upravljanje lozinkama – Vodič",
        'password_guide_voice': "Vodič za upravljanje lozinkama. Molimo pročitajte napomene.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Upravljanje lozinkama – Detaljni vodič</strong></p>

        <p><strong>1. Zaštita PDF-a lozinkom</strong></p>
        <ul>
        <li>Prilikom otvaranja PDF-a zaštićenog lozinkom, pojavljuje se dijalog u koji možete unijeti lozinku.</li>
        <li>Lozinku možete sačuvati šifrovanu kako je ne biste morali unositi svaki put (polje za potvrdu "Sačuvaj lozinku").</li>
        <li>Pomoću dugmeta "Ukloni lozinku" možete napraviti dešifrovanu kopiju PDF-a i izbrisati lozinku iz baze podataka.</li>
        </ul>

        <p><strong>2. Glavna lozinka</strong></p>
        <ul>
        <li>Glavna lozinka štiti pristup svim sačuvanim PDF lozinkama.</li>
        <li><strong>Postavljanje:</strong> Idite na "Postavke → Upravljanje lozinkama → Postavke glavne lozinke" i kliknite na "Postavi glavnu lozinku". Odaberite jaku lozinku (najmanje 8 znakova).</li>
        <li><strong>Promjena:</strong> Nakon uspješne autentifikacije, možete promijeniti glavnu lozinku.</li>
        <li><strong>Uklanjanje:</strong> Ako uklonite glavnu lozinku, SVE sačuvane lozinke će biti nepovratno izbrisane. Prije toga možete izvesti rezervnu kopiju.</li>
        <li>Jednom po sesiji, morate se autentificirati glavnom lozinkom da biste pristupili zaštićenim funkcijama (npr. prikazivanje lozinki).</li>
        </ul>

        <p><strong>3. Upravljanje lozinkama (lista)</strong></p>
        <ul>
        <li>U "Postavke → Upravljanje lozinkama" otvara se tabela svih sačuvanih PDF-ova s njihovim šifrovanim lozinkama.</li>
        <li><strong>Bez glavne lozinke:</strong> Možete samo brisati unose – lozinke ostaju skrivene.</li>
        <li><strong>S glavnom lozinkom (autentificirano):</strong> Možete prikazivati, kopirati, izvoziti i brisati lozinke.</li>
        <li><strong>Izvoz:</strong> Odaberite format (JSON, CSV, TXT) i sačuvajte listu. Ako je glavna lozinka postavljena, možete odabrati hoće li se lozinke izvesti dešifrovane ili šifrovane.</li>
        <li><strong>Uvoz:</strong> Ranije izvezeni ZIP fajl (sve postavke) može se ponovo uvesti putem "Postavke → Izvezi postavke / uvezi postavke". Upozorenje: postojeći podaci će biti prepisani!</li>
        </ul>

        <p><strong>4. Generator lozinki</strong></p>
        <ul>
        <li>U dijalogu za lozinku (npr. prilikom zaštite PDF-a), desno od polja za unos nalazi se dugme s kockicom 🎲.</li>
        <li>Kliknite na njega da biste otvorili generator lozinki. Možete podesiti dužinu, skupove znakova (velika slova, mala slova, brojevi, simboli) i razdjelnik za bolju čitljivost.</li>
        <li>Generirana lozinka može se direktno koristiti i po potrebi kopirati.</li>
        </ul>

        <p><strong>5. Važne sigurnosne napomene</strong></p>
        <ul>
        <li>Sačuvane lozinke se čuvaju šifrovane pomoću AES-256. Ključ se izvodi iz vaše glavne lozinke (ako je postavljena) ili iz fiksne vrijednosti (bez glavne lozinke).</li>
        <li>Bez glavne lozinke, lozinke su šifrovane, ali je ključ ugrađen u program – napadač s pristupom vašim fajlovima mogao bi ih dešifrovati. Stoga snažno preporučujemo korištenje glavne lozinke.</li>
        <li>Baza podataka lozinki nalazi se u fajlu `Data/passwords.json`. Redovno pravite rezervne kopije, posebno prije uklanjanja glavne lozinke.</li>
        <li>Ako izgubite glavnu lozinku, sve sačuvane lozinke su nepovratno izgubljene.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Način invertiranja",
        'invert_mode_classic': "Klasičan (invertira sve boje)",
        'invert_mode_smart': "Inteligentan (invertira samo svjetlinu)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Prag sive skale",
        'gray_threshold_10': "10% (strogo)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standardno)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (meko)",
        'threshold_changed': "Prag postavljen na {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Prag sive skale – Objašnjenje",
        'threshold_guide_text': "Prag sive skale određuje koji se pikseli u inteligentnom tamnom načinu smatraju 'sivim' i invertiraju.\n\n"
                                "• Niska vrijednost (10%) invertira samo gotovo savršene nijanse sive – obojeni elementi ostaju potpuno očuvani.\n"
                                "• Visoka vrijednost (50%) invertira i lagano obojene piksele – to povećava kontrast, ali može izobličiti boje.\n\n"
                                "Optimalna vrijednost ovisi o dokumentu. Za čiste tekstualne dokumente 30–40% je često idealno, za obojene grafike radije 10–20%.\n\n"
                                "Vrijednost možete prilagoditi u bilo koje vrijeme putem izbornika 'Postavke' – PDF će se odmah ponovno učitati.\n\n"
                                "Napomena:\n* Fotografije i slike mogu se ispravno prikazati samo u svijetlom načinu rada!\n* Postavke invertiranja prikazuju se samo kada je tamni način rada aktiviran.",
        'threshold_guide_voice': "Prag sive skale određuje koliko snažno inteligentni tamni način intervenira. Niska vrijednost štedi boje, visoka povećava kontrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Otvaranje PDF-a...",
        'progress_loading_document': "Učitavanje dokumenta...",
        'progress_pdf_opened': "PDF otvoren",
        'progress_creating_backup': "Kreiranje sigurnosne kopije...",
        'progress_backup_description': "Sigurnosno kopiranje originalne datoteke...",
        'progress_backup_created': "Sigurnosna kopija kreirana",
        'progress_backup_saved_as': "Spremljeno kao: {0}",
        'progress_analyzing_start': "Pokretanje analize...",
        'progress_searching_empty': "Traženje praznih stranica...",
        'progress_page_empty': "Stranica {0} je prazna",
        'progress_page_keep': "Zadrži stranicu {0}",
        'progress_analysis_complete': "Analiza završena",
        'progress_empty_found': "Pronađeno {0} praznih stranica",
        'progress_current_page': "Trenutna stranica",
        'progress_mark_delete': "Označava se za brisanje",
        'progress_range_selected': "Opseg stranica {0}-{1}",
        'progress_deleting_pages': "Brisanje {0} stranica",
        'progress_creating_new_pdf': "Kreiranje novog PDF-a...",
        'progress_transferring_pages': "Prijenos stranica",
        'progress_keeping_page': "Stranica {0} će biti zadržana ({1}/{2})",
        'progress_saving_pdf': "Spremanje PDF-a...",
        'progress_optimizing': "Optimizacija veličine datoteke...",
        'progress_finalizing': "Finalizacija...",
        'progress_new_size': "Nova veličina: {0:.2f} MB",
        'progress_cancelling': "Otkazivanje...",
        'progress_cancel_message': "{0} se otkazuje",
        'progress_pages_found_moving': "Pronađeno {0} stranica, {1} za premještanje",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analiza PDF-a...",
        'ocr_status_optimizing': "Optimizacija slike u toku...",
        'ocr_status_recognizing': "Prepoznavanje teksta u toku...",
        'ocr_status_embedding': "Ugrađivanje teksta...",
        'ocr_status_finalizing': "Finalizacija PDF-a...",

        # PDF-Laden
        'progress_preparing': "Priprema...",
        'progress_loading': "Učitavanje PDF-a...",

        # Seitenoperationen
        'progress_deleting_title': "Brisanje stranica...",
        'progress_moving_title': "Premještanje stranica...",
        'pages_found': "Pronađene stranice",
        'progress_creating_new_order': "Kreiranje novog redoslijeda...",
        'progress_sorting_pages': "Sortiranje stranica...",
        'progress_moving_to_begin': "Premještanje {0} stranica na početak",
        'progress_transferring_count': "Prijenos {0} stranica",
        'progress_transferring_before_target': "Prijenos stranica prije cilja",
        'progress_moving_pages': "Premještanje {0} stranica",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_sigurnosna_kopija_",
        'filename_protected_suffix': "_zasticeno_",
        'filename_copy_suffix': "_Kopija",
        'filename_page_single': "_Stranica_",
        'filename_page_range': "_Stranice_",
        'filename_export_page': "_Stranica_{0:03}",
        'filename_export_range': "_Stranice_{0}-{1}",
        'filename_export_multiple': "_Stranice_{0}",
        'filename_with_text': "_sa_Tekstom",
        'filename_with_signature': "_sa_Potpisom",
        'filename_with_image': "_sa_Slikom",
        'filename_with_forms': "_sa_Oblcima",
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
        'view_toggle_navbar': "Prikaži traku s dugmadima",


		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Ne mogu se izbrisati sve stranice",
		'pages_cannot_delete_last_page': 'Posljednja stranica se ne može izbrisati!',
		'pages_cannot_delete_all_pages': 'Najmanje jedna stranica mora ostati u dokumentu!',
		'delete_pages_confirm': 'Jeste li sigurni da želite izbrisati {0} stranica?',
		'delete_pages_confirm_voice': 'Jeste li sigurni da želite izbrisati {0} stranica?',
		'pages_deleted': '{0} stranica je uspješno izbrisano.',
		'warning': 'Upozorenje',
		'error': 'Greška',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nije odabran obrazac",
        'form_customized': "Obrazac prilagođen",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Odaberi",
        'btn_use': "Koristi",
        'master_password_for_spasswords': "Za spremanje i korištenje lozinki, prvo morate postaviti glavnu lozinku.\n\nŽelite li sada postaviti glavnu lozinku?",
        'open_saved_dialog_title': "Otvori spremljenu datoteku",
        'open_saved_question': "Želite li sada otvoriti spremljenu datoteku?",
        'password': "Lozinka",
        'password_manager_master_required': "Upravitelj lozinki dostupan je samo ako je postavljena glavna lozinka.\n\nŽelite li sada postaviti glavnu lozinku?",
        'password_master_required_for_select': "Da biste prikazali i odabrali spremljene lozinke, prvo se morate autentificirati svojom glavnom lozinkom.\n\nŽelite li se sada autentificirati?",
        'password_not_available': "Odabrana lozinka nije dostupna ili se ne može dešifrirati.",
        'password_options_title': "Opcije lozinke",
        'password_save_choice_change': "Postavi novu lozinku",
        'password_save_choice_keep': "Koristi postojeću lozinku",
        'password_save_choice_none': "Spremi nešifrirano",
        'password_save_hint': "Prvo postavite glavnu lozinku za sigurno spremanje lozinki.",
        'password_save_master_required': "Spremi lozinku (moguće samo s glavnom lozinkom)",
        'password_save_question': "Trenutni PDF je zaštićen lozinkom. Želite li koristiti postojeću lozinku, postaviti novu ili spremiti nešifrirano?",
        'password_select': "Odaberi lozinku",
        'password_select_none': "Nije odabrana nijedna lozinka.\n\nMolimo odaberite lozinku s popisa.",
        'password_select_one': "Molimo odaberite točno jednu lozinku.\n\nOznačili ste više lozinki.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_sigurnosna_kopija",
        'filename_insert_suffix': "_sa_umetanjem",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_stranice_izbrisane",
        'filename_pages_moved': "_stranice_pomjerene",
        'filename_rotated_all_suffix': "_sve_stranice_rotirane",
        'filename_rotated_suffix': "_stranica_rotirana",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfiguracija imena datoteka pri promjenama PDF-a",
        'filename_keep_suffixes': "Zadrži prethodne ekstenzije (npr. _s_tekstom)",
        'filename_keep_suffixes_false': "Zamijeni",
        'filename_keep_suffixes_true': "Zadrži",
        'filename_preview_label': "Pregled imena datoteke:",
        'filename_preview_overwrite_hint': "Pregled nije dostupan – original će biti prepisan.",
        'filename_separator': "Razdjelnik između riječi",
        'filename_separator_none': "Bez razdjelnika",
        'filename_separator_space': "Razmak ( )",
        'filename_separator_underscore': "Donja crta (_)",
        'filename_settings_saved': "Postavke imena datoteke spremljene",
        'filename_settings_title': "Formatiranje imena datoteke i sigurnosna kopija",
        'filename_timestamp_position': "Pozicija vremenske oznake",
        'filename_timestamp_position_after': "Nakon osnovnog imena",
        'filename_timestamp_position_before': "Skroz naprijed",
        'filename_timestamp_position_end': "Na kraju",
        'filename_use_timestamp': "Koristi vremensku oznaku",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Ponašanje pri promjenama:</b><ul><li>Brisanje i umetanje stranica</li><li>Umetanje teksta, potpisa, slike i oblika</li><li>OCR</li></ul></html>",
        'backup_section': "Sigurnosna kopija za operacije sa stranicama (Brisanje, Pomicanje)",
        'behavior_info': "Napomena: Kod 'Prepiši original' vremenske oznake i sufiksi se ignoriraju – datoteka zadržava svoje ime.",
        'behavior_new_file': "Uvijek kreiraj novu datoteku (s vremenskom oznakom i sufiksom)",
        'behavior_overwrite': "Prepiši original (nema nove datoteke)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Sve stranice su rotirane.\n\nOriginal je ostao nepromijenjen.\nova datoteka: {0}",
        'all_pages_rotated_voice': "Sve stranice rotirane, kreirana nova datoteka.",
        'empty_pages_deleted_new_file': "{0} praznih stranica je izbrisano.\n\nOriginal je ostao nepromijenjen.\nova datoteka: {1}",
        'empty_pages_deleted_voice': "{0} praznih stranica izbrisano, kreirana nova datoteka.",
        'ocr_keep_original': "Zadrži original (kasnije ručno otvori)",
        'ocr_new_file_question': "Nova PDF datoteka koja se može pretraživati spremljena je na:\n{0}\n\nŽelite li je sada otvoriti?",
        'ocr_open_new': "Otvori novu OCR datoteku",
        'ocr_original_kept': "Originalna datoteka ostaje otvorena. OCR datoteka je spremljena.",
        'page_deleted_new_file': "Stranica {0} je izbrisana.\n\nOriginal je ostao nepromijenjen.\nova datoteka: {1}",
        'page_deleted_voice': "Stranica {0} izbrisana, kreirana nova datoteka.",
        'page_rotated_new_file': "Stranica {0} je rotirana.\n\nOriginal je ostao nepromijenjen.\nova datoteka: {1}",
        'page_rotated_voice': "Stranica {0} rotirana, kreirana nova datoteka.",
        'pages_deleted_new_file': "Izbrisano je {0} stranica.\n\nOriginalna datoteka je ostala nepromijenjena.\nova datoteka: {1}",
        'pages_deleted_new_file_voice': "{0} stranica izbrisano, kreirana nova datoteka.",
        'pages_inserted_new_file': "Umetnuto je {0} stranica.\n\nOriginalna datoteka je ostala nepromijenjena.\nova datoteka: {1}",
        'pages_inserted_new_file_ask': "Umetnuto je {0} stranica.\n\nOriginal je ostao nepromijenjen.\nova datoteka: {1}\n\nŽelite li je sada otvoriti?",
        'pages_inserted_voice_new': "{0} stranica umetnuto, kreirana nova datoteka.",
        'pages_moved_new_file': "Pomjereno je {0} stranica.\n\nOriginalna datoteka je ostala nepromijenjena.\nova datoteka: {1}",
        'pages_moved_new_file_voice': "{0} stranica pomjereno, kreirana nova datoteka.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ne prikazuj više",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Postavka sigurnosne kopije</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Sigurnosna kopija UKLJUČENA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Kod svih promjena koje prepisuju original</strong> (tekst, potpis, slika, oblik, OCR, rotiranje, umetanje, brisanje/pomicanje stranica) <strong>automatski se kreira sigurnosna kopija s vremenskom oznakom</strong> prije nego što se promjena primijeni.</p>
                <p style="margin: 5px 0 5px 20px;">• Sigurnosna kopija nalazi se pored originalne datoteke (npr. <code>Dokument_sigurnosna_kopija_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Ako ste dodatno aktivirali opciju <strong>„Prepiši original“</strong>, također se kreira sigurnosna kopija.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Sigurnosna kopija ISKLJUČENA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Ne kreira se sigurnosna kopija</strong> – niti kod prepisivanja niti kod operacija sa stranicama.</p>
                <p style="margin: 5px 0 5px 20px;">• Originalna datoteka može se nepovratno izgubiti prilikom prepisivanja.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Preporučuje se samo za iskusne korisnike!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Savjet:</strong> Postavka sigurnosne kopije neovisna je o opciji „Prepiši original“. Možete kombinirati oboje.<br>
                Ovu poruku možete trajno sakriti.
            </div>
        </div>
        """,
        'backup_info_title': "Ponašanje sigurnosne kopije",
        'backup_info_voice': "Obavijest o ponašanju sigurnosne kopije kod operacija sa stranicama. Sigurnosna kopija uključena prepisuje original, sigurnosna kopija isključena kreira novu datoteku.",
        'show_backup_info': "Informacije o postavci sigurnosne kopije",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ne prikazuj više",
        'overwrite_enable_backup': "Aktiviraj sigurnosnu kopiju (preporučeno)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Prepiši original</p>
            <p>Ako aktivirate ovu opciju, promjene (tekst, potpis, slika, oblik, OCR, rotiranje, umetanje) se <strong>spremaju direktno u original</strong> – <strong>ne kreira se nova datoteka</strong>.</p>
            <p>• Ime datoteke ostaje nepromijenjeno.<br>
            • Vremenske oznake i sufiksi se ignoriraju.<br>
            • <strong>Bez sigurnosne kopije original se može nepovratno izgubiti.</strong></p>
            <p style="color: #FFD700;">Preporuka: Dodatno aktivirajte opciju sigurnosne kopije za automatske sigurnosne kopije.</p>
        </div>
        """,
        'overwrite_info_title': "Prepiši original",
        'overwrite_info_voice': "Upozorenje: Prepiši original – nema nove datoteke. Preporučuje se sigurnosna kopija.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Umetnuto je {0} stranica.\n\nOriginalna datoteka je prepisana.\nKreirana je sigurnosna kopija.",
        'pages_inserted_overwrite_no_backup': "Umetnuto je {0} stranica.\n\nOriginalna datoteka je prepisana.\nNije kreirana sigurnosna kopija.",
        'texts_saved_overwrite_with_backup': "Promjene su spremljene u originalu.\n\nKreirana je sigurnosna kopija.",
        'texts_saved_overwrite_no_backup': "Promjene su spremljene u originalu.\n\nNije kreirana sigurnosna kopija.",
        'texts_crosses_saved_new_file': "{0} {1} i {2} {3} su umetnuti.\n\nOriginalna datoteka je ostala nepromijenjena.\nKreirana je nova datoteka.\n\nNovi PDF se učitava...",
        'texts_saved_new_file': "{0} {1} je umetnuto.\n\nOriginalna datoteka je ostala nepromijenjena.\nKreirana je nova datoteka.\n\nNovi PDF se učitava...",
        'crosses_saved_new_file': "{0} {1} je umetnuto.\n\nOriginalna datoteka je ostala nepromijenjena.\nKreirana je nova datoteka.\n\nNovi PDF se učitava...",
        'elements_saved_new_file': "{0} elemenata je umetnuto.\n\nOriginalna datoteka je ostala nepromijenjena.\nKreirana je nova datoteka.\n\nNovi PDF se učitava...",
        'signatures_saved_overwrite_with_backup': "Potpis(i) su spremljeni u originalu.\n\nKreirana je sigurnosna kopija.",
        'signatures_saved_overwrite_no_backup': "Potpis(i) su spremljeni u originalu.\n\nNije kreirana sigurnosna kopija.",
        'images_saved_overwrite_with_backup': "Slika(e) su spremljene u originalu.\n\nKreirana je sigurnosna kopija.",
        'images_saved_overwrite_no_backup': "Slika(e) su spremljene u originalu.\n\nNije kreirana sigurnosna kopija.",
        'forms_saved_overwrite_with_backup': "Oblik(ci) su spremljeni u originalu.\n\nKreirana je sigurnosna kopija.",
        'forms_saved_overwrite_no_backup': "Oblik(ci) su spremljeni u originalu.\n\nNije kreirana sigurnosna kopija.",
        'signatures_saved_new_file': "{0} potpisa je umetnuto.\n\nOriginalna datoteka je ostala nepromijenjena.\nKreirana je nova datoteka.\n\nNovi PDF se učitava...",
        'images_saved_new_file': "{0} slika je umetnuto.\n\nOriginalna datoteka je ostala nepromijenjena.\nKreirana je nova datoteka.\n\nNovi PDF se učitava...",
        'forms_saved_new_file': "{0} oblika je umetnuto.\n\nOriginalna datoteka je ostala nepromijenjena.\nKreirana je nova datoteka.\n\nNovi PDF se učitava...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Upozorenje: Ovaj PDF sadrži rotirane stranice. Pozicioniranje može odstupati.",
        'page_rotated_warning_title': "Otkrivena rotirana stranica",
        'page_rotated_warning_message': "Trenutna stranica {0} je rotirana za {1}°.\n\nUmetanje elemenata na rotirane stranice nije podržano.\n\nŽelite li sada rotirati stranicu u uspravni položaj?",
        'page_rotated_warning_voice': "Upozorenje: Stranica je rotirana. Molimo prvo je rotirajte.",
        'paste_on_rotated_page_simple_warning': "Umetanje na stranicu {0} nije moguće!\n\nOva stranica je rotirana za {1}°.\n\nMolimo prvo rotirajte stranicu na 0° (Izbornik: Uredi → Poravnaj stranicu).\n\nUpozorenje:\nPrethodno kopirani element će se izgubiti ako ne spremite prije rotiranja stranice.",
        'paste_on_rotated_page_voice': "Umetanje prekinuto. Stranica je rotirana. Molimo prvo poravnajte stranicu.",
        'page_rotated_cancel': "Odustani",
        'page_rotated_rotate_until_upright': "Rotiraj stranicu više puta (dok ne bude uspravna)",
        'page_rotated_now_upright': "Stranica je sada uspravna. Sada možete umetati.",
        'page_rotated_still_not_upright': "Stranica nije mogla biti rotirana u uspravni položaj. Molimo ručno ispravite.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Pomoć: Ispravljanje rotiranih stranica",
        'help_rotated_pages_voice': "Pomoć za ispravljanje rotiranih stranica se otvara.",
        'btn_help': "Pomoć",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Rotirana stranica – Umetanje ne radi ispravno</p>

            <p>Ako umetanje tekstova, potpisa ili oblika na rotiranoj stranici ne radi ispravno, možete ispraviti stranicu vanjskim PDF uređivačem.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Rješenje s vanjskim alatom (npr. macOS Pregled)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Izvezi stranicu</strong><br>
                &nbsp;&nbsp;Kliknite u izborniku na <strong>Datoteka → Izvezi kao stranice</strong> ili koristite drugu metodu za spremanje željene stranice kao pojedinačni PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Otvori stranicu u vanjskom programu</strong><br>
                &nbsp;&nbsp;Otvorite izvezeni PDF u PDF uređivaču (npr. <strong>macOS Pregled</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rotiraj stranicu</strong><br>
                &nbsp;&nbsp;Rotirajte stranicu tako da bude uspravna (u Pregledu: <strong>Alati → Rotiraj</strong> ili <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Spremi</strong><br>
                &nbsp;&nbsp;Spremite ispravljenu stranicu (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Ponovno umetni stranicu u originalni dokument</strong><br>
                &nbsp;&nbsp;Vratite se u PDFDarkView i umetnite ispravljenu stranicu na željenu poziciju:<br>
                &nbsp;&nbsp;<strong>Uredi → Umetni stranice</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativa: Rotiraj stranicu u originalu</p>
                <p style="margin: 5px 0 5px 20px;">• Koristite ugrađenu funkciju rotiranja (<strong>Uredi → Rotiraj stranicu</strong>) za postupno ispravljanje stranice.<br>
                • Nakon svakog rotiranja možete provjeriti radi li umetanje sada.<br>
                • Ovo je često brže rješenje – prvo ga isprobajte!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Savjet:</strong> Ako često nailazite na rotirane stranice, možete trajno sakriti upozorenje u dijalogu za umetanje.<br>
                Pozicioniranje tada može odstupati – koristite ovu opciju samo ako znate posljedice.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Poravnaj stranice",
        'menu_rotate_normalize_tooltip': "Rotiraj stranicu ili resetiraj na 0°",
        'normalize_current_page': "Dovedi trenutnu stranicu u uspravni položaj (postavi na 0°)",
        'normalize_all_pages': "Dovedi sve stranice u uspravni položaj (postavi na 0°)",
        'page_normalized': "Stranica {0} je dovedena u uspravni položaj.",
        'all_pages_normalized': "Sve stranice su dovedene u uspravni položaj.",
        'page_already_upright': "Stranica {0} je već uspravna.",
        'all_pages_already_upright': "Sve stranice su već uspravne.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF ne sadrži tekst koji se može pretraživati.</p><p>Želite li izvršiti OCR za izvoz u {0}?</p>",
        'export_ocr_voice': "PDF ne sadrži tekst. OCR je potreban za izvoz u {0}.",
        'export_no_ocr_possible': "Izvoz bez OCR-a nije moguć. Molimo izvršite OCR putem izbornika.",
        'ocr_failed_export_not_possible': "OCR nije uspio. Izvoz se ne može izvršiti.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF će se otvoriti u Pregledu. Molimo pokrenite postupak ispisa tamo.",
        'print_preview_manual': "PDF je otvoren. Molimo izvršite naredbu za ispis ručno (npr. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Spoji PDF-ove",
        'merge_pdfs': "Spoji PDF-ove",
        'merge_progress_title': "Spajanje PDF-ova...",
        'merge_pdfs_list': "PDF-ovi po redu (Povucite i ispustite za sortiranje)",
        'merge_add_pdf': "Dodaj PDF",
        'merge_remove': "Ukloni",
        'merge_move_up': "Gore",
        'merge_move_down': "Dolje",
        'merge_pdfs_info': "💡 Savjet: Redoslijed možete mijenjati povlačenjem i ispuštanjem",
        'merge_no_pdfs': "Nije odabran nijedan PDF. Kliknite na 'Dodaj PDF'.",
        'merge_info': "{0} PDF-ova odabrano (otprilike {1} stranica)",
        'merge_open_file': "Otvori datoteku",
        'merge_merge': "Spoji",
        'merge_error': "Greška prilikom spajanja",
        'merge_min_two_pdfs_error': "Molimo odaberite najmanje dvije PDF datoteke za spajanje.",
        'merge_select_pdfs': "Odaberite PDF-ove za spajanje",
        'merge_error_file': "Greška pri obradi",
        'merge_cancelled': "Spajanje je prekinuto",
        'merge_preparing': "Priprema...",
        'merge_processing': "Obrada PDF {0} od {1}",
        'merge_saving': "Spremanje spojenog PDF-a...",
        'merge_complete': "Gotovo!",
        'merge_success_title': "Spajanje uspješno",
        'merge_success_voice': "{0} PDF-ova je uspješno spojeno.",
        'merge_success_message': "{0} PDF-ova je uspješno spojeno.\n\nNovi dokument sada ima {1} stranica.\n\nNova datoteka:\n{2}\n\nMjesto spremanja:\n{3}\n{2}\n\nŽelite li otvoriti ovaj PDF?",
        'replace_file_title': "Zamijeniti datoteku?",
        'replace_file_message': "PDF je već otvoren. Želite li ga zamijeniti novom datotekom?",
        'btn_yes': "Da",
        'btn_no': "Ne",
        'filename_merge_suffix': "spojeno",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Otvaram {0}...",
        'progress_merge_reading': "Čitam {0}...",
        'progress_merge_adding': "Dodajem {0} stranica...",
        'progress_merge_optimizing': "Optimiram PDF...",
        'progress_merge_writing': "Pišem PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "zatvaranja PDF-a",
        'action_close_window': "zatvaranja prozora",
        'action_open_new_pdf': "otvaranja novog PDF-a",
        'action_quit_app': "zatvaranja aplikacije",
        'changes_saved': "Promjene su spremljene.",
        'file_close_title': "Zatvori PDF datoteku",
        'save_before_action': "Treba li spremiti promjene prije {0}? Da ili Ne?",
        'save_before_action_voice': "Treba li spremiti promjene prije {0}? Da ili Ne?",
        'save_before_close_question': "Treba li spremiti promjene prije zatvaranja? Da ili Ne?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Kreiran PDF za pretraživanje:\n\n{0}\n\n<b>pokušajte ponovo ako je potrebno",
        "ocr_rotate_title": "Poravnanje stranica prije OCR",
        "ocr_rotate_question": "PDF sadrži rotirane stranice.\nŽelite li poravnati sve stranice na 0° prije OCR?\nOvo značajno poboljšava prepoznavanje teksta.",
        "ocr_rotate_yes": "Da, poravnaj",
        "ocr_rotate_no": "Ne, pokreni OCR direktno",
        "ocr_rotate_voice": "PDF sadrži rotirane stranice. Trebaju li se sve stranice poravnati prije OCR?",
        "ocr_not_performed_message": "Nema teksta. Molimo izvršite OCR (meni \"Uredi\" → \"Izvrši OCR\" ili tipka Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR postavke",
        "ocr_language_btn": "Odaberi OCR jezik",
        "ocr_language": "OCR jezik(ci)",
        "ocr_language_current": "Trenutni jezik:",
        "ocr_param_info": "Informacije o parametru",

        "ocr_force_ocr_label": "Forsiraj OCR",
        "ocr_deskew_label": "Ispravi nagib",
        "ocr_clean_label": "Očisti sliku",
        "ocr_oversample_label": "Rezolucija (DPI)",
        "ocr_pagesegmode_label": "Podjela stranice",
        "ocr_oem_label": "OCR režim motora",
        "ocr_optimize_label": "PDF kompresija",
        "ocr_jobs_label": "Paralelni procesi",
        "ocr_verbose_label": "Detaljnost loga",

        "ocr_force_ocr_tooltip": "Forsiraj OCR na svakoj stranici, čak i ako tekst već postoji",
        "ocr_deskew_tooltip": "Automatski poravnaj nagnute skenove",
        "ocr_clean_tooltip": "Ukloni šum i artefakte sa slike",
        "ocr_oversample_tooltip": "Uvećaj sliku prije OCR na ovaj DPI",
        "ocr_pagesegmode_tooltip": "Određuje kako se stranica dijeli na tekstualne oblasti",
        "ocr_oem_tooltip": "Odabire OCR motor Tesseracta",
        "ocr_optimize_tooltip": "Nivo kompresije izlaznog PDF",
        "ocr_jobs_tooltip": "Broj paralelnih OCR procesa",
        "ocr_verbose_tooltip": "Nivo detaljnosti izlaza loga",
        "ocr_settings_explain_btn": "Objašnjenje",

        "ocr_force_ocr_explain": "Forsira prepoznavanje teksta na <b>svakoj</b> stranici, čak i ako već sadrži tekst.\n\nPreporuka: <b>Uključeno</b> za skenirane PDF-ove, <b>Isključeno</b> za izvorne PDF-ove s već postojećim tekstom.",

        "ocr_deskew_explain": "Ispravlja blago nagnute skenove (do oko 5°).\n\nPreporuka: <b>Uključeno</b> za skenirane dokumente, <b>Isključeno</b> ako su stranice već savršeno ravne.",

        "ocr_clean_explain": "Uklanja šum, tačke i male artefakte sa slike.\n<b>VAŽNO:</b> Za arapske, tajlandske ili vijetnamske tekstove s dijakritičkim znacima (tačke iznad/ispod slova) ova opcija treba biti <b>isključena</b>, jer se inače mogu izgubiti važni znakovi.",

        "ocr_oversample_explain": "Uvećava sliku <b>prije</b> prepoznavanja teksta na navedeni DPI.<br><br>• <b>72-150 DPI:</b> Vrlo brzo, ali niska stopa prepoznavanja<br>• <b>200-300 DPI:</b> Optimalni raspon (Standard: 300)<br>• <b>400+ DPI:</b> Nešto bolje prepoznavanje, ali znatno veće datoteke<br><br>Preporuka: 300 DPI za složena pisma (arapsko, kinesko, japansko), 200 DPI za zapadne jezike.",

        "ocr_pagesegmode_explain": "Određuje kako Tesseract dijeli stranicu na tekstualne oblasti.\n\n• <b>3 - Automatski (Standard):</b> Dobro za miješane rasporede\n• <b>4 - Pojedinačna kolona:</b> Za tekstove s jednom kolonom\n• <b>5 - Vertikalni blok:</b> Za vertikalna pisma (japansko, kinesko)\n• <b>6 - Jedinstveni tekstualni blok:</b> Optimalno za tekući tekst bez kolona\n• <b>11 - Sirova slika:</b> Za loše skenove / rukopise\n\nPreporuka: <b>6</b> za jednostavne tekstualne dokumente, <b>3</b> za složene rasporede.",

        "ocr_oem_explain": "Odabire OCR motor Tesseracta.\n\n• <b>0 - Legacy:</b> Stari motor (brz, ali manje tačan)\n• <b>1 - LSTM:</b> Neuralni motor (sporiji, ali tačniji)\n• <b>2 - Legacy + LSTM:</b> Kombinira oba rezultata\n• <b>3 - Standard (LSTM preferiran):</b> Najbolji izbor za većinu slučajeva\n\nPreporuka: <b>3</b> za maksimalnu tačnost prepoznavanja.",

        "ocr_optimize_explain": "Komprimira izlazni PDF.\n\n• <b>0:</b> Bez optimizacije (najbrža obrada)\n• <b>1:</b> Lagana optimizacija (dobar kompromis)\n• <b>2:</b> Umjerena optimizacija\n• <b>3:</b> Jaka optimizacija (najmanja datoteka, ali sporija)\n\nPreporuka: <b>1</b> za svakodnevnu upotrebu.",

        "ocr_jobs_explain": "Broj paralelnih procesa za OCR.\n\n• <b>1:</b> Sporo, ali najniža potrošnja memorije\n• <b>4-8:</b> Optimalno za moderne višejezgrene procesore\n• <b>12+:</b> Nešto brža obrada uz visoku potrošnju memorije\n\nPreporuka: Broj CPU jezgri (npr. <b>4</b> na 4-jezgrenim sistemima).",

        "ocr_verbose_explain": "Nivo detaljnosti izlaza loga u konzoli.\n\n• <b>0:</b> Bez izlaza\n• <b>1:</b> Napredak i statusne poruke\n• <b>2:</b> Detaljni izlaz\n• <b>3:</b> Potpuni debug izlaz (veoma opširan)\n\nPreporuka: <b>1</b> za normalan rad.",

        "ocr_reset_title": "Postavke su resetirane",
        "ocr_reset_message": "Sve OCR postavke su resetirane na standardne vrijednosti.",
        "info_tooltip": "Više informacija o ovom parametru",
        "ocr_reset_defaults": "Resetiraj na standardno",

        "ocr_psm_0": "Automatski (Legacy motor)",
        "ocr_psm_1": "Automatsko otkrivanje kolona",
        "ocr_psm_3": "Automatski (Standard)",
        "ocr_psm_4": "Pojedinačna kolona",
        "ocr_psm_5": "Vertikalni blok",
        "ocr_psm_6": "Jedinstveni tekstualni blok",
        "ocr_psm_7": "Pojedinačna linija teksta",
        "ocr_psm_8": "Pojedinačna riječ",
        "ocr_psm_11": "Sirova slika (bez analize rasporeda)",

        "ocr_oem_0": "Legacy motor (brz)",
        "ocr_oem_1": "LSTM motor (neuralan, tačan)",
        "ocr_oem_2": "Legacy + LSTM kombinovano",
        "ocr_oem_3": "Standard (LSTM preferiran)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR jezik(ci)...",
        "ocr_language_title": "Odaberi OCR jezik(e)",
        "ocr_language_instruction": "Odaberite jezik(e) za prepoznavanje teksta (OCR).\nPažnja: Više jezika ide na štetu performansi i tačnosti!\nNajbolje rezultate postižete ako odaberete samo jedan jezik.",
        "ocr_language_predefined": "Pretpostavljene kombinacije",
        "ocr_language_custom": "Prilagođeno...",
        "ocr_language_selected": "Odabrani OCR jezici",
        "ocr_language_changed": "OCR jezik promijenjen na {0}",
        "ocr_language_auto_detect": "Dostupni jezici se automatski otkrivaju.",
        "ocr_language_none_found": "Nisu pronađeni Tesseract jezički podaci! Molimo instalirajte jezičke pakete (npr. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Prilagođeni odabir jezika",
        "ocr_language_available": "Dostupni jezici (instalirani):",
        "ocr_language_select_hint": "Odaberite jedan ili više jezika:",
        "ocr_language_confirm": "Primijeni",
        "ocr_language_reset": "Resetiraj na standardno (deu+eng+vie)",
        "ocr_language_priorities": "Preporučeni jezici (prethodno instalirani):",

        "select_all_languages": "Odaberi sve",
        "clear_all_languages": "Poništi odabir",
        "install_language_packs": "Instaliraj nedostajuće jezičke pakete...",
        "install_hint": "💡 Savjet: Nisu svi jezici instalirani na vašem sistemu. Preko ovog dugmeta dobit ćete pomoć za instalaciju.",
        "ocr_language_install_title": "Instalacija Tesseract jezičkih paketa",

        "ocr_missing_languages": "Nedostajući OCR jezički paketi",
        "ocr_missing_languages_message": "Sljedeći odabrani jezici nisu instalirani na vašem sistemu:\n\n{0}\n\nMolimo instalirajte nedostajuće jezičke pakete (pogledajte pomoć u 'Pomoć za instalaciju').\n\nŽelite li otvoriti pomoć za instalaciju sada?",
        "ocr_missing_languages_voice": "Nedostajući jezički paketi. Molimo instalirajte nedostajuće jezike.",
        "ocr_install_help_now": "Otvori pomoć",
        "ocr_continue_anyway": "Svejedno pokušaj",
        "ocr_language_error_title": "OCR jezička greška",
        "ocr_language_error_message": "Greška pri prepoznavanju teksta: {0}\n\nMolimo provjerite vaše OCR jezičke postavke (Postavke → OCR jezik).",
        "ocr_install_help_button": "Pomoć za instalaciju",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalacija Tesseract jezičkih paketa</p>

        <p>Da bi OCR radio na određenom jeziku, odgovarajući jezički podaci moraju biti instalirani na vašem sistemu. Slijedite upute za vaš operativni sistem:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Otvorite <strong>Terminal</strong> (Finder → Programi → Uslužni programi → Terminal).</li>
        <li>Instalirajte sve dostupne jezike sa:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
>(Ovo može potrajati nekoliko minuta.)</li>
        <li>Ili samo pojedinačne jezike (npr. vijetnamski):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
Kod trenutnih Homebrew verzija, <code>*.traineddata</code> možda treba ručno preuzeti (pogledajte dolje).</li>
        <li>Nakon instalacije: Zatvorite ovaj dijalog i ponovo otvorite odabir OCR jezika – novi jezici će se automatski pojaviti.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Otvorite terminal (Ctrl+Alt+T).</li>
        <li>Instalirajte željeni jezik, npr. za vijetnamski:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
Važni jezički kodovi: <code>deu</code> (njemački), <code>eng</code> (engleski), <code>vie</code> (vijetnamski), <code>spa</code> (španski), <code>fra</code> (francuski), <code>ita</code> (italijanski), <code>nld</code> (holandski), <code>fin</code> (finski), <code>swe</code>(švedski), <code>nor</code> (norveški).</li>
        <li>Prikaži sve dostupne pakete:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ručno)</p>
        <ol>
        <li>Preuzmite željene <code>*.traineddata</code> datoteke sa:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
(npr. <code>vie.traineddata</code> za vijetnamski).</li>
        <li>Kopirajte datoteke u Tesseract jezičku mapu, obično:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
(Prilagodite prema individualnoj instalaciji.)</li>
        <li>Ponovo pokrenite aplikaciju (ili ponovo otvorite odabir OCR jezika).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativa za sve sisteme</p>
        <ul>
        <li>Instalirajte <strong>OCRmyPDF</strong> i <strong>Tesseract</strong> sa menadžerom paketa po vašem izboru. Većina instalacija već sadrži neke standardne jezike (engleski, njemački, francuski).</li>
        <li>Nedostajući jezici se mogu instalirati u bilo koje vrijeme – odabir OCR jezika prikazuje samo stvarno postojeće.</li>
        </ul>

        <hr>
        <p><b>✅ Nakon instalacije:</b> Nije potrebno ponovno pokretanje aplikacije – novododani jezici će se odmah pojaviti na listi.</p>
        <p><b>📖 Pomoć za jezičke kodove:</b> Potpuna lista dostupna je u <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract dokumentaciji</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans fontovi",
        "info_noto_font_voice": "Vodič za instalaciju Noto Sans fontova",
        "btn_info_noto_font_install": "Info o fontu",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Kako instalirati besplatne Noto fontove kompanije Google</h2>

        <p><strong>Noto fontovi</strong> su open-source porodica fontova kompanije Google. Njihov cilj je da se <em>"ne vidi tofu"</em> (tj. bez praznih kutija □) i da se svaki znak iz Unicode standarda ispravno prikaže. Oni su idealan dodatak za aplikacije koje moraju prikazivati tekstove na mnogo različitih jezika.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalacija na macOS</h3>

        <p><strong>Metoda 1: Sa Homebrew (za napredne)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metoda 2: Preko "Font Book" (Preporučeno)</strong></p>

        <ol>
        <li>Preuzmite službeni paket fontova:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Raspakirajte ZIP datoteku</li>
        <li>Kopirajte datoteke u <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalacija na Windows (10 & 11)</h3>

        <p><strong>Metoda 1: Microsoft Store (Preporučeno)</strong><br>
Tražite "Google Noto Fonts" ili "Noto Sans" i kliknite na <strong>Instaliraj</strong>.</p>

        <p><strong>Metoda 2: Ručna instalacija</strong></p>

        <ol>
        <li>Preuzimanje:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Raspakirajte ZIP</li>
        <li>Odaberite .ttf / .otf datoteke</li>
        <li>Desni klik → <strong>Instaliraj</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        ili<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Ime\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalacija na Linux</h3>

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

        <p>Provjera:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Upravljanje bookmarkovima",
        "bookmark_add": "Dodaj bookmark",
        "bookmark_add_tooltip": "Spremi trenutnu stranicu kao bookmark",
        "bookmark_remove": "Ukloni bookmark",
        "bookmark_remove_tooltip": "Izbriši označeni bookmark",
        "bookmark_remove_all": "Ukloni sve",
        "bookmark_remove_all_tooltip": "Izbriši sve bookmarkove ovog PDF",
        "bookmark_jump": "Skoči na bookmark",
        "bookmark_jump_tooltip": "Skoči na odabranu stranicu",
        "bookmark_name": "Ime",
        "bookmark_page": "Stranica",
        "bookmark_no_bookmarks": "Nema bookmarkova.\nKliknite na 'Dodaj' da spasite trenutnu stranicu kao bookmark.",
        "bookmark_added": "Dodan bookmark za stranicu {0}: {1}",
        "bookmark_removed": "Bookmark uklonjen: {0}",
        "bookmark_all_removed": "Svi bookmarkovi su uklonjeni.",
        "bookmark_name_default": "Stranica {0}",
        "bookmark_name_prompt": "Ime za bookmark:\n(dugi tekst će biti skraćen na 50 znakova)",
        "bookmark_name_prompt_title": "Ime bookmarka",
        "bookmark_confirm_remove_all": "Jeste li sigurni da želite ukloniti svih {0} bookmarkova?",
        "menu_bookmarks": "Bookmarkovi",
        "bookmark_manage": "Upravljanje bookmarkovima",
        "bookmark_next": "Sljedeći bookmark",
        "bookmark_prev": "Prethodni bookmark",
        "bookmark_page_display": "Stranica {0}",
        "bookmark_exists": "Bookmark za ovu stranicu s ovim imenom već postoji.",
        "bookmark_select_first": "Molimo prvo odaberite bookmark.",
        "bookmark_confirm_remove": "Jeste li sigurni da želite ukloniti bookmark 'Stranica {0}: {1}'?",
        "bookmark_jumped_to": "Skočeno na bookmark '{0}' na stranici {1}.",
        "bookmark_jumped_to_voice": "Bookmark {0}, stranica {1}",
        "btn_close": "Zatvori",

        "bookmark_list": "Vaši bookmarkovi",
        "bookmark_rename": "Preimenuj bookmark",
        "bookmark_rename_tooltip": "Promijeni ime odabranog bookmarka",
        "bookmark_rename_title": "Preimenuj bookmark",
        "bookmark_rename_prompt": "Novo ime za bookmark na stranici {0}:\n(maks. 50 znakova)",
        "bookmark_renamed": "Bookmark '{0}' je preimenovan u '{1}'.",
        "bookmark_item_tooltip": "Stranica {0}: {1}\nDvostruki klik za skok",
        "bookmark_name_exists_question": "Bookmark s imenom '{0}' već postoji na ovoj stranici.\nSvejedno preimenovati?",

        "context_bookmarks": "Bookmarkovi",
        "context_bookmark_add_here": "Dodaj bookmark za ovu stranicu",
        "context_bookmarks_existing": "Postojeći bookmarkovi:",
        "context_bookmarks_jump": "Skoči na bookmark:",
        "context_bookmarks_none": "Nema bookmarkova",
        "context_bookmarks_clear_all": "Ukloni svih {0} bookmarkova",

        "bookmark_search_placeholder": "Pretraži bookmarkove... (ime ili stranica)",
        "bookmark_search_results": "%d bookmarkova pronađeno za \"%s\"",
        "bookmark_no_search_results": "Nema bookmarkova pronađenih za \"%s\"",
        "bookmark_no_search_results_label": "Nema rezultata za \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Uredi PDF metapodatke",
        "metadata_title": "Naslov",
        "metadata_title_placeholder": "Naslov dokumenta",
        "metadata_title_tooltip": "Naslov dokumenta (prikazuje se u naslovnoj traci)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Ime autora",
        "metadata_author_tooltip": "Kreator dokumenta",
        "metadata_subject": "Predmet",
        "metadata_subject_placeholder": "Predmet dokumenta",
        "metadata_subject_tooltip": "Kratak opis sadržaja",
        "metadata_keywords": "Ključne riječi",
        "metadata_keywords_placeholder": "Ključne riječi, odvojene zarezima",
        "metadata_keywords_tooltip": "Ključne riječi za kategorizaciju dokumenta",
        "metadata_creator": "Kreator",
        "metadata_creator_placeholder": "Aplikacija koja je kreirala PDF",
        "metadata_creator_tooltip": "Softver s kojim je dokument kreiran",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Aplikacija koja je konvertirala PDF",
        "metadata_producer_tooltip": "Softver koji je konvertirao PDF",
        "metadata_creation_date": "Datum kreiranja",
        "metadata_creation_date_tooltip": "Datum kreiranja dokumenta",
        "metadata_mod_date": "Datum izmjene",
        "metadata_mod_date_tooltip": "Datum posljednje izmjene",
        "metadata_pdf_info": "📄 PDF informacije",
        "metadata_pages": "Broj stranica",
        "metadata_file_size": "Veličina datoteke",
        "metadata_pdf_version": "PDF verzija",
        "metadata_encrypted": "Šifrirano",
        "metadata_encrypted_yes": "Da (zaštićeno lozinkom)",
        "metadata_encrypted_no": "Ne",
        "metadata_reload": "📂 Ponovo učitaj iz PDF",
        "metadata_reset": "Odbaci promjene",
        "metadata_reloaded": "Metapodaci su ponovo učitani iz PDF.",
        "metadata_reset_done": "Sva polja metapodataka su resetirana.",
        "metadata_no_file": "Nema učitane PDF datoteke.",
        "metadata_save_error": "Greška pri čuvanju metapodataka",
        "metadata_saved": "Metapodaci su uspješno sačuvani.",
        "metadata_pdf_version_unknown": "PDF (nepoznato)",
        "metadata_saved_message": "Metapodaci su uspješno sačuvani.",
        "metadata_saved_voice": "Metapodaci sačuvani.",

        "metadata_custom": "🔧 Prilagođeni metapodaci",
        "metadata_custom_placeholder": "{\n  \"moje_polje\": \"moja vrijednost\",\n  \"drugo_polje\": 123\n}",
        "metadata_custom_tooltip": "JSON format za prilagođene metapodatke (opciono)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Predložak \"{0}\" odabran - Dvostruki klik za umetanje",
        "text_use_template": "Koristi tekstualni blok",
        "text_type": "Tip",
        "text_search_templates": "Pretraži tekstualne blokove...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informacije o izvozu / uvozu",
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

        <h3>📦 Šta se izvozi? (Pregled)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Opće postavke aplikacije</span></li>
            <li class="detail">• Tamni/Svijetli način rada</li>
            <li class="detail">• Invertiranje tamnog načina za slike</li>
            <li class="detail">• Siva granična vrijednost</li>
            <li class="detail">• Jezik</li>
            <li class="detail">• Geometrija prozora</li>
            <li class="detail">• Zum način rada</li>
            <li class="detail">• Navigacija (Navigaciona traka vidljiva)</li>
            <li class="detail">• Glasovni izlaz (uključeno/isključeno)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Postavke sigurnosne kopije</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Imenovanje datoteka (Vremenska oznaka, Razdjelnik, Sufiksi)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Postavke za umetanje</span></li>
            <li class="detail">• Potpisi</li>
            <li class="detail">• Tekst i tekstualni blokovi</li>
            <li class="detail">• Kvačice, slike i oblici</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR postavke</span></li>
            <li class="detail">• Jezik</li>
            <li class="detail">• Forsiraj OCR · Način rada stranice</li>
            <li class="detail">• Prethodna obrada slike: Ispravi nagib, Očisti, Preuzorkovanje</li>
            <li class="detail">• Broj paralelnih poslova</li>
            <li class="detail">• Način invertiranja</li>
            <li class="detail">• Siva granična vrijednost</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bookmarkovi</span></li>
            <li class="detail">• Svi bookmarkovi po PDF datoteci (Stranica, Ime, Vrijeme kreiranja)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Baza podataka lozinki</span></li>
            <li class="detail">• Sačuvane PDF lozinke (opciono šifrirane ili običan tekst)</li>
            <li class="detail">• Hash glavne lozinke (ako je postavljena)</li>
            <li class="detail">• Verifikacijski podaci</li>
        </ul>

        <h4>⚠️ Važne napomene</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Prilikom uvoza:</strong>
            <ul>
                <li><span class="warning">➜ SVE trenutne postavke će biti u potpunosti prepisane</span></li>
                <li>• Ponovno pokretanje aplikacije je obavezno</li>
                <li>• Postojeći potpisi, tekstualni blokovi i bookmarkovi će biti zamijenjeni</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Glavna lozinka i način izvoza:</strong>
            <ul>
                <li>• Kada je glavna lozinka aktivna, možete odabrati:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dešifrirano</strong></span> (lozinke su u običnom tekstu u ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Šifrirano</strong></span> (samo se mogu čitati s glavnom lozinkom na ciljnom sistemu)</li>
                <li>• Hash glavne lozinke se <strong>uvijek</strong> pohranjuje šifrirano</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Sigurnosna napomena:</strong>
            <ul>
                <li>• Izvezena ZIP datoteka sadrži osjetljive podatke (<strong>lozinke, bookmarkove, potpise</strong>)</li>
                <li>• Molimo čuvajte je na sigurnom (npr. šifrirani USB stick, menadžer lozinki)</li>
                <li>• Ako se datoteka izgubi, sačuvane PDF lozinke su nepovratno izgubljene</li>
            </ul>
        </div>

        <h4>📁 Format izvoza</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Postavke se pohranjuju u jednu ZIP datoteku:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ovaj ZIP sadrži potpuni <code>settings.json</code> (iz vaše konfiguracije) kao i eventualno ugrađene slikovne datoteke potpisa i šifrirane lozinke.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Potpisi - Vodič",
        'signature_guide_html': """
        📝 <strong>Potpisi - Kratki vodič</strong><br>
        <ul>
        <li>Postavite glavnu lozinku</li>
        <li>Konfigurišite potpise u meniju <em>Postavke</em> (veličina, vremenska oznaka, …)</li>
        <li>Ubacite sa <strong>DESNIM KLIKOM</strong> na željenu poziciju (glavna lozinka potrebna jednom po sesiji)</li>
        <li>Pomjerite potpis mišem ili strelicama</li>
        <li>Ubacite više potpisa jedan za drugim</li>
        <li>Prilagodite svaki potpis pojedinačno</li>
        <li>Odbacite pojedinačni potpis</li>
        <li>Spremite / odbacite sve potpise odjednom</li>
        <li>Alternativno, može se koristiti i meni traka.</li>
        </ul>
        """,
        'signature_guide_voice': "Kratki vodič za potpise. Postavite glavnu lozinku. Konfigurišite potpise u postavkama. Ubacite desnim klikom.",

        'image_guide_title': "Ubacivanje slika - Vodič",
        'image_guide_html': """
        📷 <strong>Ubacivanje slika u PDF - Kratki vodič</strong><br>
        <ol>
        <li>Desni klik na željenu poziciju</li>
        <li><em>„Ubaci sliku“</em> → Odaberite sliku</li>
        <li>Pozicionirajte sliku: Povucite mišem</li>
        <li>Podesite veličinu: Povucite za uglove/ivice</li>
        <li>Zadržite omjer stranica: Taster <strong>[A]</strong></li>
        <li>Daljnja podešavanja: Desni klik na sliku</li>
        </ol>
        <p><strong>Savjet:</strong> U kontekstnom meniju možete podesiti postavke.</p>
        """,
        'image_guide_voice': "Kratki vodič za slike. Desni klik, ubaci sliku, odaberite. Pozicionirajte mišem, podesite veličinu na uglovima. Omjer stranica tasterom A.",

        'form_guide_title': "Ubacivanje oblika - Vodič",
        'form_guide_html': """
        📐 <strong>Ubacivanje oblika u PDF - Kratki vodič</strong><br>
        <ol>
        <li>Odaberite tip oblika (pravougaonik, elipsa, linija, strelica)</li>
        <li>Kliknite na poziciju:
            <ul>
            <li>Za pravougaonik/elipsu: Jedan klik postavlja oblik</li>
            <li>Za liniju/strelicu: Dva klika za početnu i krajnju tačku</li>
            </ul>
        </li>
        <li>Pozicionirajte oblik: Povucite mišem</li>
        <li>Podesite veličinu: Povucite za uglove/ivice</li>
        <li>Spremite oblik: <strong>Enter</strong></li>
        <li>Odbacite oblik: <strong>ESC</strong></li>
        <li>Daljnja podešavanja: Desni klik na oblik</li>
        </ol>
        <p><strong>Savjet:</strong> U kontekstnom meniju možete podesiti postavke.</p>
        """,
        'form_guide_voice': "Kratki vodič za oblike. Odaberite tip oblika. Za pravougaonik ili elipsu kliknite jednom, za liniju ili strelicu dva puta. Pozicionirajte mišem, podesite veličinu na uglovima. Spremite sa Enter, odbacite sa Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "prethodni",
        "btn_next_result": "sljedeći",
        "ocr_text_window": "OCR prozor za tekst",
        "bookmark_existing": "Postojeće oznake",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR poređenje Mac - Windows",
        'ocr_method_mac_win_title': "OCR razlike između Mac i Windows",
        'ocr_method_mac_win_voice': "Mac je bolji",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Razlike između macOS i Windows</strong></p>

        <p><strong>macOS (preporučeno)</strong></p>
        <p>Alat:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Rezultat:</p>
        <ul>
        <li>PDF koji se može pretraživati sa ugrađenim tekstom koji u velikoj mjeri zadržava originalni raspored.</li>
        </ul>
        <p>Prednosti:</p>
        <ul>
        <li>Odličan kvalitet prepoznavanja teksta (čak i na nagnutim stranicama).</li>
        <li>Zadržavanje vektorske grafike i fontova.</li>
        <li>GUI traka napretka preko evaluacije podprocesa.</li>
        <li>Potpuna kontrola nad svim OCR parametrima (Deskew, Clean, Oversample, optimizacija).</li>
        <li>Pretraga teksta je direktno dostupna u glavnom prozoru (PDF prikaz).</li>
        </ul>
        <p>Nedostaci:</p>
        <ul>
        <li>Zahtijeva dodatne sistemske alate (ocrmypdf, Ghostscript, unpaper, pngquant – uključeni u App Bundle).</li>
        <li>Složenije rukovanje greškama (deadlockovi, timeouti).</li>
        </ul>

        <p><strong>Windows (stabilna alternativa)</strong></p>
        <p>Alat:</p>
        <ul>
        <li>pytesseract (direktna veza sa Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Rezultat:</p>
        <ul>
        <li>PDF koji se može pretraživati, koji vizuelno odgovara slici PDF-a, ali se može pretraživati kroz prozirni tekst.</li>
        </ul>
        <p>Prednosti:</p>
        <ul>
        <li>Trenutno mi nijedna ne pada na pamet.</li>
        </ul>
        <p>Nedostaci:</p>
        <ul>
        <li>PDF je u suštini slika sa nevidljivim tekstom; raspored može malo odstupati kod složenih dokumenata (kolone, tabele).</li>
        <li>Nema automatske korekcije nagiba (--deskew) ili čišćenja slike (--clean).</li>
        <li>GUI traka napretka se ažurira samo grubo na osnovu broja obrađenih stranica.</li>
        <li>OCR brzina je nešto sporija (jer se svaka stranica obrađuje zasebno).</li>
        <li>Pretraga teksta se preusmjerava na OCR prozor za tekst.</li>
        </ul>

        <p><strong>Zajedničke karakteristike</strong></p>
        <ul>
        <li>Obje metode stvaraju PDF koji se može pretraživati u istom direktoriju kao i izvorna datoteka.</li>
        <li>OCR postavke (jezik, DPI, način segmentacije stranice, način rada OCR motora) mogu se konfigurirati putem OCRSettingsDialog-a i djeluju u obje implementacije.</li>
        </ul>

        <p><strong>Preporuka:</strong></p>
        <ul>
        <li>macOS: ocrmypdf binarna datoteka daje najbolje rezultate – Kupite Mac i koristite verziju (PDFDarkView za Mac sa Apple Silicon ili Intel čipom). OCR rezultati su bolji nego na Windows-u!</li>
        <li>Windows: Koristite pytesseract rješenje. Stabilno je i pruža sasvim dovoljan kvalitet za većinu dokumenata.</li>
        </ul>

        <p><strong>Važna napomena:</strong></p>
        <ul>
        <li>Obje verzije su u potpunosti integrirane u korisničko sučelje – korisnik ne primjećuje razliku.</li>
        <li>Program automatski odlučuje koji OCR motor će se koristiti na osnovu operativnog sistema.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Kreiraj potpis (iz skeniranja)",
        "signature_create_title": "Odaberite skenirani potpis (PDF/Slika)",
        "image_pdf_filter": "Slike i PDF",
        "signature_pdf_empty": "PDF ne sadrži stranice.",
        "signature_created_success": "Potpis uspješno kreiran: {0}",
        "signature_create_error": "Greška pri kreiranju potpisa:\n{0}",
        "rembg_missing": "rembg nije instaliran.\nMolimo instalirajte: pip install rembg\nGreška: {0}",
        "signature_name_title": "Ime datoteke za potpis",
        "signature_name_message": "Molimo unesite ime datoteke za novi potpis (bit će sačuvan kao PNG sa prozirnom pozadinom):",
        "signature_name_label": "Ime datoteke:",
        "signature_name_voice": "Unesite ime datoteke za potpis",
        "signature_processing": "Obrada u toku...",
        "signature_creation_title": "Potpis se kreira",
        "signature_overwrite_warning": "Datoteka '{0}' već postoji. Prebrisati?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Pripremite PDF za potpis",
        "signature_prepare_instruction":"Molimo odaberite PDF koji na jednoj stranici sadrži skenirani potpis.\n\nOptimalno prepoznavanje postiže se ako:\n• Potpis je napisan crnom tintom (hemijska olovka ili fineliner) na bijelom papiru.\n• Potpis se nalazi u gornjoj trećini inače prazne A4 stranice.\n• PDF je skeniran sa najmanje 300 dpi.\n• Potpis je jasan i nije previše tanak.\n• Nema ometajućih uzoraka pozadine ili linija.",
        "signature_prepare_voice":"Molimo odaberite PDF sa skeniranim potpisom. Obratite pažnju na dobar kvalitet i kontrast.",
        "sig_thickness_label":"Debljina linije:",
        "sig_thickness_normal":"Normalna (tanka)",
        "sig_thickness_bold":"Podebljana (preporučeno)",
        "sig_thickness_very_bold":"Veoma podebljana",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Dodavanje GUI i OCR jezika - Vodič",
        'language_guide_title': "Dodavanje GUI i OCR jezika",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Preuzmite željenu datoteku prijevoda <code>translations_xy.py</code> sa<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        i stavite je u sljedeći direktorij:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Otvorite vaš web pretraživač.</li>
        <li>Idite na: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Potražite na desnoj ivici ekrana "Releases" i odaberite onu označenu sa <strong>"latest"</strong>.</li>
        <li>Na sljedećoj stranici izdanja, preuzmite datoteku <code>Source Code.zip</code> pri dnu.</li>
        <li>Raspakirajte ZIP datoteku.</li>
        <li>Potražite u raspakiranom folderu sve jezičke datoteke koje su vam potrebne i kopirajte ih u direktorij:<br/>
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
        "menu_watermark":"Umetni vodeni žig",
        "fullpage_text_watermark_title":"Tekst kao vodeni žig",
        "fullpage_image_watermark_title":"Slika kao vodeni žig",
        "filename_with_watermark":"_sa_vodenim_zigom",
        "watermark_text":"Tekst:",
        "watermark_text_placeholder":"Vaš tekst za vodeni žig...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Veličina fonta:",
        "watermark_format":"Formatiranje:",
        "watermark_bold":"Podebljano",
        "watermark_italic":"Kurziv",
        "watermark_color":"Boja:",
        "watermark_choose_color":"Odaberite boju...",
        "watermark_opacity":"Neprozirnost / Prozirnost:",
        "watermark_direction":"Smjer čitanja:",
        "watermark_direction_l_r":"Lijevo → Desno",
        "watermark_direction_bl_tr":"Dolje lijevo → Gore desno",
        "watermark_direction_tl_br":"Gore lijevo → Dolje",
        "watermark_direction_b_t":"Dolje → Gore",
        "watermark_direction_t_b":"Gore → Dolje",
        "watermark_preview":"Pregled:",
        "watermark_preview_sample":"Primjer teksta",
        "watermark_empty_text":"Molimo unesite tekst.",
        "watermark_applied":"Vodeni žig je primijenjen na sve stranice.",
        "watermark_saved":"Vodeni žig je sačuvan.",
        "image_scale":"Veličina:",
        "image_preview":"Pregled slike:",
        "no_image_selected":"Nije odabrana slika",
        "browse":"Pretraži...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Crnjenje",
        "redact_add_black": "Crnjenje (crno)",
        "redact_add_white": "Crnjenje (bijelo / brisanje)",
        "redact_added_black": "Dodano crno crnjenje",
        "redact_added_white": "Dodano bijelo crnjenje",
        "redact_apply_all": "Primijeni sva crnjenja i sačuvaj",
        "redact_discard_all": "Odbaci sva crnjenja",
        "redact_discard": "Odbaci ovo crnjenje",
        "no_redactions": "Nema crnjenja",
        "redact_confirm_title": "Trajno primijeni crnjenja",
        "redact_confirm_message": "Upozorenje: Označena područja će biti trajno izbrisana (crno ili bijelo).\nSigurnosna kopija će biti kreirana (ako je omogućena).\n\nNastaviti?",
        "redact_apply": "Da, crni sada",
        "redact_saved": "{0} crnjenje(a) uspješno primijenjeno i sačuvano.",
        "redact_saved_voice": "{0} crnjenje(a) primijenjeno",
        "redact_error": "Greška prilikom crnjenja",
        "filename_redacted":"_ocrnjeno",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Umetni brojeve stranica',
        'page_numbers_format': 'Format broja:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arapski)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (rimski mali)',
        'page_numbers_format_roman_upper': 'I, II, III ... (rimski veliki)',
        'page_numbers_format_letter': 'A, B, C ... (slova)',
        'page_numbers_format_custom': 'Prilagođeno',
        'page_numbers_custom_pattern': 'Uzorak:',
        'page_numbers_custom_placeholder': 'npr. "Stranica {nummer}" ili "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Koristite {nummer} za trenutni broj stranice i {total} za ukupan broj',
        'page_numbers_position': 'Pozicija:',
        'page_numbers_pos_tl': 'Gore lijevo',
        'page_numbers_pos_tc': 'Gore sredina',
        'page_numbers_pos_tr': 'Gore desno',
        'page_numbers_pos_ml': 'Sredina lijevo',
        'page_numbers_pos_mc': 'Centrirano',
        'page_numbers_pos_mr': 'Sredina desno',
        'page_numbers_pos_bl': 'Dolje lijevo',
        'page_numbers_pos_bc': 'Dolje sredina',
        'page_numbers_pos_br': 'Dolje desno',
        'page_numbers_margins': 'Margine:',
        'page_numbers_margin_x': 'Horizontalna udaljenost:',
        'page_numbers_margin_y': 'Vertikalna udaljenost:',
        'page_numbers_range': 'Raspon stranica:',
        'page_numbers_all_pages': 'Sve stranice',
        'page_numbers_custom_range': 'Prilagođeni raspon',
        'page_numbers_from': 'Od:',
        'page_numbers_to': 'Do:',
        'page_numbers_progress': 'Umetanje brojeva stranica...',
        'page_numbers_start': 'Pokretanje umetanja brojeva stranica...',
        'page_numbers_cancel': 'Umetanje brojeva stranica otkazano',
        'page_numbers_success': 'Brojevi stranica su uspješno dodani.\n\nŽelite li otvoriti novi PDF?\n\n{0}',
        'page_numbers_complete': 'Brojevi stranica su dodani',
        'page_numbers_error_format': 'Greška pri umetanju brojeva stranica: {0}',
        'page_numbers_content_type': 'Vrsta sadržaja:',
        'page_numbers_tab_simple': 'Jednostavan broj',
        'page_numbers_tab_range': 'Stranica X od Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Slobodan tekst',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Stranica {aktuell} od {gesamt}',
        'page_numbers_range_custom': 'Prilagođeno',
        'page_numbers_range_placeholder': 'npr. "Stranica {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Format datuma:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. januar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Prilagođeno',
        'page_numbers_date_placeholder': 'npr. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Pozicija:',
        'page_numbers_date_before': 'Datum prije broja stranice',
        'page_numbers_date_after': 'Datum nakon broja stranice',
        'page_numbers_date_only': 'Samo datum (bez broja stranice)',
        'page_numbers_custom_text': 'Prilagođeni tekst:',
        'page_numbers_custom_placeholder_text': 'Koristite {seite} za broj stranice i {gesamt} za ukupan broj\nnpr. "Povjerljivo - Stranica {seite}" ili "{seite} od {gesamt}"',
        "filename_with_page_number":"_sa_brojem_stranice",
        "filename_with_page_declaration":"_sa_oznakom_stranice",
        "filename_with_pagenumber":"_sa_brojem_stranice",
        "filename_with_date":"_sa_datumom",
        "filename_with_my_page_declaration":"_sa_prilagodjenom_oznakom",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Nesačuvane promjene",
        "unsaved_changes_message_darkmode": "Postoje nesačuvana umetanja.\nŽelite li ih sačuvati prije prebacivanja?",
        "save_and_switch": "Sačuvaj i prebaci",
        "discard_and_switch": "Prebaci sada",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Izvoz stranica kao slike',
        'export_images_menu': 'Izvoz kao slike (PNG/JPEG)',
        'export_images_format': 'Format slike:',
        'export_images_dpi': 'Rezolucija (DPI):',
        'export_images_quality': 'Kvalitet JPEG-a:',
        'export_images_range': 'Raspon stranica:',
        'export_images_all_pages': 'Sve stranice',
        'export_images_custom_range': 'Prilagođeni raspon',
        'export_images_from': 'Od:',
        'export_images_to': 'Do:',
        'export_images_options': 'Opcije:',
        'export_images_single_files': 'Svaka stranica kao zasebna datoteka',
        'export_images_subfolder': 'Izvoz u podmapu',
        'export_images_subfolder_info': 'U podmapu "imePDF_slike"',
        'export_images_same_folder': 'U istoj mapi kao PDF',
        'export_images_apply_darkmode': 'Primijeni PDFDarkView postavke (Tamni način)',
        'export_images_target_folder': 'Ciljna mapa:',
        'export_images_browse': 'Pretraži...',
        'export_images_preview': 'Pregled:',
        'export_images_preview_info': 'Odaberite postavke za izvoz',
        'export_images_preview_info_detail': '{0} stranica kao {1}\nRezolucija: {2} DPI\nNaziv datoteke: {3}\n{4}',
        'export_images_select_folder': 'Odaberite ciljnu mapu',
        'export_images_start': 'Pokretanje izvoza slika...',
        'export_images_progress': 'Izvoz slika...',
        'export_images_saving': 'Čuvanje stranice {0} od {1}...',
        'export_images_success': 'Izvoz uspješan!\n\n{0} slika je sačuvano u:\n{1}',
        'export_images_complete': 'Izvoz slika završen',
        'export_images_open_folder': '📁 Otvori mapu',
        'export_images_cancel': 'Izvoz slika otkazan',
        'export_images_error_format': 'Greška pri izvozu slika: {0}',
        'export_images_pdf2image_missing': 'Biblioteka "pdf2image" nije instalirana.\n\nMolimo instalirajte je sa:\npip install pdf2image\n\nZa Windows vam je također potreban Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konverzija za dugoročno arhiviranje',
        'pdfa_menu': 'PDF/A konverzija (pogodno za arhiv)',
        'pdfa_info': 'Konvertuje PDF u PDF/A format.\n\nPDF/A je posebno razvijen za dugoročno arhiviranje i osigurava da će dokument biti ispravno prikazan u budućnosti.',
        'pdfa_standard': 'PDF/A standard:',
        'pdfa_standard_select': 'Verzija:',
        'pdfa_1': 'PDF/A-1 (jednostavan, široko kompatibilan)',
        'pdfa_2': 'PDF/A-2 (moderan, bolja kompresija)',
        'pdfa_3': 'PDF/A-3 (najnovija verzija, dozvoljava priloge)',
        'pdfa_standards_explanation': '📖 Objašnjenje standarda:\n\n'
            '• PDF/A-1: Osnovni, kompatibilan sa starijim sistemima (oko 2005)\n'
            '• PDF/A-2: Moderniji, bolja kompresija, podrška za prozirnost (oko 2011)\n'
            '• PDF/A-3: Najnovija verzija, dozvoljava ugrađivanje priloga (oko 2013)\n\n'
            'Preporuka: PDF/A-2 je dobar kompromis između kompatibilnosti i modernih funkcija.',
        'pdfa_options': 'Opcije:',
        'pdfa_compress_enable': 'Kompresuj PDF (manja datoteka)',
        'pdfa_metadata_preserve': 'Zadrži metapodatke (naslov, autor, itd.)',
        'pdfa_target_folder': 'Ciljna mapa:',
        'pdfa_browse': 'Pretraži...',
        'pdfa_select_folder': 'Odaberite ciljnu mapu',
        'pdfa_ocr_info_unknown': '🔍 Nije moguće provjeriti sadržaj teksta.',
        'pdfa_ocr_info_not_needed': '✅ Tekst dostupan - OCR nije potreban.\nPDF/A se može direktno kreirati.',
        'pdfa_ocr_info_recommended': '⚠️ Nije pronađen dovoljan tekst.\n\nZa pretražive PDF-ove preporučujemo da prvo pokrenete OCR.\nNapomena: PDF/A radi i bez OCR-a - ali tekst tada nije pretraživ.',
        'pdfa_ocr_info_error': '❌ Greška pri provjeri: {0}',
        'pdfa_start': 'Pokretanje PDF/A konverzije...',
        'pdfa_progress': 'PDF/A konverzija u toku...',
        'pdfa_success': 'PDF/A konverzija uspješna!\n\nSačuvano kao:\n{0}\n\nŽelite li otvoriti novi PDF?',
        'pdfa_complete': 'PDF/A konverzija završena',
        'pdfa_cancel': 'PDF/A konverzija otkazana',
        'pdfa_error_format': 'Greška pri PDF/A konverziji:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Biblioteka "ocrmypdf" nije instalirana.\n\nMolimo instalirajte je sa:\npip install ocrmypdf',
        'btn_convert': 'Konvertuj',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimiziraj PDF (smanji veličinu datoteke)',
        'optimize_menu': 'Optimiziraj PDF (veličina datoteke)',
        'optimize_info': 'Smanjuje veličinu PDF datoteke kroz različite metode optimizacije.\n\nŠto je viši nivo kompresije, to je datoteka manja - uz mogući gubitak kvaliteta slika.',
        'optimize_level': 'Nivo kompresije:',
        'optimize_level_low': 'Nizak (brzo, mala ušteda)',
        'optimize_level_medium': 'Srednji (dobar kompromis)',
        'optimize_level_high': 'Visok (velika ušteda)',
        'optimize_level_maximum': 'Maksimalan (maksimalna ušteda, sporo)',
        'optimize_level_explanation': 'Preporuka: "Srednji" je dobar kompromis između brzine i veličine datoteke.',
        'optimize_options': 'Opcije:',
        'optimize_compress_images': 'Kompresuj slike (smanji JPEG kvalitet)',
        'optimize_clean_objects': 'Ukloni neiskorištene objekte',
        'optimize_preserve_metadata': 'Zadrži metapodatke (naslov, autor, itd.)',
        'optimize_image_quality': 'Kvalitet slike:',
        'optimize_range': 'Raspon stranica:',
        'optimize_all_pages': 'Sve stranice',
        'optimize_custom_range': 'Prilagođeni raspon',
        'optimize_from': 'Od:',
        'optimize_to': 'Do:',
        'optimize_target_folder': 'Ciljna mapa:',
        'optimize_browse': 'Pretraži...',
        'optimize_select_folder': 'Odaberite ciljnu mapu',
        'optimize_info_box': 'Informacije',
        'optimize_info_text': 'Optimizacija može potrajati nekoliko minuta za velike PDF-ove.\n\nSlike se čuvaju sa smanjenim kvalitetom, što može značajno smanjiti veličinu datoteke.',
        'optimize_start': 'Pokretanje PDF optimizacije...',
        'optimize_progress': 'Optimizacija PDF-a...',
        'optimize_cancel': 'PDF optimizacija otkazana',
        'optimize_complete': 'PDF optimizacija završena',
        'optimize_error_format': 'Greška pri PDF optimizaciji:\n\n{0}',
        'optimize_success_message': 'PDF optimizacija uspješna!\n\nSačuvano kao:\n{0}\n\nPrije: {1}\nPoslije: {2}\nUšteda: {3:.1f}%\n\n{4}\n\nŽelite li otvoriti optimizirani PDF?',
        'optimize_success_message_no_size': 'PDF optimizacija uspješna!\n\nSačuvano kao:\n{0}\n\nInformacija o veličini nije dostupna.\n\nŽelite li otvoriti optimizirani PDF?',
        'optimize_result_positive': 'Datoteka je smanjena za {0:.1f}%.',
        'optimize_result_zero': 'Nema promjene u veličini datoteke.',
        'optimize_result_negative': 'Datoteka je povećana za {0:.1f}%.\nOptimizacija je preskočena, originalna datoteka je zadržana.',
        'btn_optimize': 'Pokreni optimizaciju',
        'filename_optimize_low_suffix': '_optimizirano_nisko',
        'filename_optimize_medium_suffix': '_optimizirano',
        'filename_optimize_high_suffix': '_optimizirano_visoko',
        'filename_optimize_maximum_suffix': '_optimizirano_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Obrezivanje PDF-a',
        'crop_menu': 'Obrezivanje PDF-a (Crop)',
        'crop_range': 'Primijeni na:',
        'crop_all_pages': 'Sve stranice',
        'crop_current_page': 'Samo trenutna stranica',
        'crop_values': 'Vrijednosti obrezivanja (u tačkama):',
        'crop_left': 'Lijevo:',
        'crop_right': 'Desno:',
        'crop_top': 'Gore:',
        'crop_bottom': 'Dolje:',
        'crop_presets': 'Unaprijed postavljeno:',
        'crop_preset_white': 'Otkrivanje bijelih margina',
        'crop_reset': 'Resetuj',
        'crop_mouse_hint': '🖱️ Prevucite pravougaonik za grubi odabir područja.\nZatim možete precizno podesiti vrijednosti u SpinBox-ovima.\nRučno podešavanje mišem nije moguće.',
        'crop_apply': 'Obreži',
        'crop_scope_all': 'Sve stranice',
        'crop_scope_current': 'Trenutna stranica',
        'crop_new_size': 'Nova veličina: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Nije učitano PDF-a',
        'crop_preview_error': 'Greška pri učitavanju pregleda',
        'crop_start': 'Pokretanje obrezivanja...',
        'crop_progress': 'Obrezivanje PDF-a...',
        'crop_success': 'PDF uspješno obrezan!\n\nSačuvano kao:\n{0}\n\nŽelite li otvoriti obrezani PDF?',
        'crop_complete': 'Obrezivanje završeno',
        'crop_cancel': 'Obrezivanje otkazano',
        'crop_error_format': 'Greška pri obrezivanju:\n\n{0}',
        'filename_crop_suffix': '_obrezano',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Izravnavanje PDF-a (Flatten)',
        'flatten_menu': 'Izravnavanje PDF-a (Flatten)',
        'flatten_info': 'Izravnavanje PDF-a "upisuje" sve elemente za uređivanje u sadržaj stranice.\n\nNakon toga, polja formulara, anotacije, tekstovi, križevi, potpisi, slike i oblici više nisu pojedinačno uredivi.',
        'flatten_explanation_title': '📖 Za šta je ovo dobro?',
        'flatten_explanation_text': 'Izravnavanje je potrebno u sljedećim situacijama:\n\n'
            '• 📄 Želite pripremiti dokument za štampanje\n'
            '• 🔒 Želite spriječiti da neko mijenja polja formulara\n'
            '• 📎 Želite "trajno" ugraditi anotacije i komentare u dokument\n'
            '• 🖼️ Želite trajno ugraditi tekstove, križeve, potpise, slike i oblike u dokument\n'
            '• 📦 Želite pripremiti datoteku za arhiviranje\n\n'
            'Izravnavanje čini PDF manjim i sprječava slučajno pomicanje ili brisanje elemenata.',
        'flatten_what_title': 'Šta se izravnava?',
        'flatten_what_list': '• ✅ Polja formulara (tekstualna polja, polja za potvrdu, dugmad)\n'
            '• ✅ Anotacije (komentari, isticanja, bilješke)\n'
            '• ✅ Prekrivanja (tekstovi, križevi, potpisi, slike, oblici)',
        'flatten_options': 'Opcije:',
        'flatten_forms': 'Izravnaj polja formulara',
        'flatten_annotations': 'Izravnaj anotacije',
        'flatten_overlays': 'Izravnaj prekrivanja (tekstovi, križevi, potpisi, slike, oblici)',
        'flatten_target_folder': 'Ciljna mapa:',
        'flatten_browse': 'Pretraži...',
        'flatten_select_folder': 'Odaberite ciljnu mapu',
        'flatten_warning': '⚠️ Važno: Izravnavanje je nepovratan proces!\n\nNakon izravnavanja, elementi za uređivanje se više ne mogu pojedinačno mijenjati ili brisati.\nPo potrebi prethodno napravite sigurnosnu kopiju.',
        'flatten_apply': 'Izravnaj',
        'flatten_start': 'Pokretanje izravnavanja...',
        'flatten_progress': 'Izravnavanje PDF-a...',
        'flatten_success': 'PDF uspješno izravnan!\n\nSačuvano kao:\n{0}\n\nŽelite li otvoriti izravnani PDF?',
        'flatten_complete': 'Izravnavanje završeno',
        'flatten_cancel': 'Izravnavanje otkazano',
        'flatten_error_format': 'Greška pri izravnavanju:\n\n{0}',
        'filename_flatten_suffix': '_izravnano',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Prekrivanje PDF-a (Overlay)',
        'overlay_menu': 'Prekrivanje PDF-a (Overlay)',
        'overlay_info': 'Postavlja jedan PDF (prekrivanje) preko drugog PDF-a.\n\nPDF za prekrivanje se postavlja na osnovni PDF. Ovo je korisno za vodene žigove, logotipe, memorandume ili pečate.',
        'overlay_explanation_title': '📖 Za šta je ovo dobro?',
        'overlay_explanation_text': 'Prekrivanje je potrebno u sljedećim situacijama:\n\n'
            '• 🏢 Postavljanje logotipa kompanije kao vodeni žig na svaku stranicu\n'
            '• 📄 Postavljanje memoranduma na prazan PDF\n'
            '• 🖊️ Postavljanje prekrivanja pečata na dokument\n'
            '• 🔖 Postavljanje vodenog žiga na sve stranice\n'
            '• 📑 Postavljanje prekrivanja formulara na šablon',
        'overlay_type': 'Vrsta prekrivanja:',
        'overlay_type_fullpage': 'Cijela stranica (prekriva)',
        'overlay_type_transparent': 'Cijela stranica (prozirno - preporučeno)',
        'overlay_type_stamp': 'Pečat (može se pozicionirati)',
        'overlay_type_info_fullpage': '📄 PDF za prekrivanje se postavlja tačno preko cijele stranice.\nBijela pozadina se može ukloniti tako da samo sadržaj ostane vidljiv.',
        'overlay_type_info_transparent': '🔍 PDF za prekrivanje se postavlja preko cijele stranice s prozirnom pozadinom.\nBijela pozadina se automatski uklanja - idealno za vodene žigove i logotipe!',
        'overlay_type_info_stamp': '🖊️ PDF za prekrivanje se pozicionira i skalira kao pečat.\nSavršeno za logotipe, pečate ili potpise na određenim pozicijama.',
        'overlay_remove_background': 'Ukloni bijelu pozadinu:',
        'overlay_remove_background_enable': 'Ukloni bijelu pozadinu s PDF-a za prekrivanje (čini prekrivanje prozirnim)',
        'overlay_remove_background_tooltip': 'Uklanja bijela područja s PDF-a za prekrivanje kako bi donji tekst postao vidljiv.',
        'overlay_threshold': 'Prag vrijednosti:',
        'overlay_threshold_hint': '(1-254, više = više bijelog se uklanja)',
        'overlay_select_file': 'Odaberite PDF za prekrivanje:',
        'overlay_file_placeholder': 'Molimo odaberite PDF datoteku za prekrivanje',
        'overlay_browse': 'Pretraži...',
        'overlay_select_overlay': 'Odaberite PDF za prekrivanje',
        'overlay_range': 'Raspon stranica:',
        'overlay_all_pages': 'Sve stranice',
        'overlay_custom_range': 'Prilagođeni raspon',
        'overlay_from': 'Od:',
        'overlay_to': 'Do:',
        'overlay_position': 'Pozicija:',
        'overlay_position_center': 'Centar',
        'overlay_position_top_left': 'Gore lijevo',
        'overlay_position_top_right': 'Gore desno',
        'overlay_position_bottom_left': 'Dolje lijevo',
        'overlay_position_bottom_right': 'Dolje desno',
        'overlay_size': 'Veličina:',
        'overlay_size_original': 'Originalna veličina',
        'overlay_size_fit_page': 'Prilagodi stranici',
        'overlay_size_custom': 'Prilagođeno (%)',
        'overlay_opacity': 'Prozirnost:',
        'overlay_target_folder': 'Ciljna mapa:',
        'overlay_browse_folder': 'Pretraži...',
        'overlay_select_folder': 'Odaberite ciljnu mapu',
        'overlay_warning': '⚠️ Napomena: PDF za prekrivanje se postavlja na osnovni PDF i "upisuje" u njega.\n\nElementi PDF-a za prekrivanje se nakon čuvanja više ne mogu pojedinačno uređivati.',
        'overlay_apply': 'Prekrij',
        'overlay_start': 'Pokretanje prekrivanja...',
        'overlay_progress': 'Prekrivanje PDF-a...',
        'overlay_success': 'PDF uspješno prekriven!\n\nSačuvano kao:\n{0}\n\nŽelite li otvoriti prekriveni PDF?',
        'overlay_complete': 'Prekrivanje završeno',
        'overlay_cancel': 'Prekrivanje otkazano',
        'overlay_error_format': 'Greška pri prekrivanju:\n\n{0}',
        'overlay_no_file': 'Nije odabran PDF za prekrivanje.\n\nMolimo odaberite PDF datoteku za prekrivanje.',
        'filename_overlay_suffix': '_prekriveno',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Izdvajanje slika iz PDF-a',
        'extract_images_menu': 'Izdvoji sve slike',
        'extract_images_info': 'Izdvaja sve slike iz PDF-a i čuva ih kao zasebne datoteke.\n\nSlike se čuvaju u originalnom formatu ili konvertuju u odabrani format.',
        'extract_images_format': 'Format slike:',
        'extract_images_quality': 'Kvalitet JPEG-a:',
        'extract_images_options': 'Opcije:',
        'extract_images_subfolder': 'Izdvoji u podmapu ("imePDF_slike")',
        'extract_images_unique': 'Samo jedinstvene slike (izbjegavanje duplikata)',
        'extract_images_range': 'Raspon stranica:',
        'extract_images_all_pages': 'Sve stranice',
        'extract_images_custom_range': 'Prilagođeni raspon',
        'extract_images_from': 'Od:',
        'extract_images_to': 'Do:',
        'extract_images_target_folder': 'Ciljna mapa:',
        'extract_images_browse': 'Pretraži...',
        'extract_images_select_folder': 'Odaberite ciljnu mapu',
        'extract_images_info_box': 'Informacije',
        'extract_images_info_text': 'Izdvajanje može potrajati nekoliko minuta za velike PDF-ove.\n\nSlike se čuvaju s originalnim nazivom (stranica_slika).',
        'extract_images_extract': 'Izdvoji',
        'extract_images_start': 'Pokretanje izdvajanja...',
        'extract_images_progress': 'Izdvajanje slika...',
        'extract_images_success': '✅ Slike uspješno izdvojene!\n\n{0} slika je sačuvano u:\n{1}',
        'extract_images_complete': 'Izdvajanje slika završeno',
        'extract_images_cancel': 'Izdvajanje otkazano',
        'extract_images_error_format': 'Greška pri izdvajanju slika:\n\n{0}',
        'extract_images_open_folder': '📁 Otvori mapu',
        'extract_images_no_images': 'Nema pronađenih slika u PDF-u.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Više stranica na jednoj stranici (N-Up)',
        'nup_menu': 'Više stranica na jednoj stranici (N-Up)',
        'nup_info': 'Raspoređuje više PDF stranica na jednu stranicu.\n\nIdealno za kompaktne ispise, preglede ili materijale za dijeljenje.',
        'nup_layout': 'Raspored:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Pregled:',
        'nup_preview_info': '{0} stranica → {1} stranica po listu → {2} listova\nRaspored: {3}',
        'nup_order': 'Redoslijed:',
        'nup_order_horizontal': 'Horizontalno (red po red)',
        'nup_order_vertical': 'Vertikalno (kolona po kolona)',
        'nup_order_horizontal_reverse': 'Horizontalno obrnuto',
        'nup_order_vertical_reverse': 'Vertikalno obrnuto',
        'nup_range': 'Raspon stranica:',
        'nup_all_pages': 'Sve stranice',
        'nup_custom_range': 'Prilagođeni raspon',
        'nup_from': 'Od:',
        'nup_to': 'Do:',
        'nup_options': 'Opcije:',
        'nup_margins': 'Margine:',
        'nup_margin_between': 'Razmak između stranica:',
        'nup_page_numbers': 'Umetni brojeve stranica',
        'nup_target_folder': 'Ciljna mapa:',
        'nup_browse': 'Pretraži...',
        'nup_select_folder': 'Odaberite ciljnu mapu',
        'nup_create': 'Kreiraj',
        'nup_start': 'Pokretanje N-Up...',
        'nup_progress': 'Kreiranje N-Up...',
        'nup_success': 'N-Up uspješno kreiran!\n\nSačuvano kao:\n{0}\n\nŽelite li otvoriti novi PDF?',
        'nup_complete': 'N-Up završen',
        'nup_cancel': 'N-Up otkazan',
        'nup_error_format': 'Greška pri N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Promijeni veličinu stranice',
        'pagesize_menu': 'Promijeni veličinu stranice',
        'pagesize_info': 'Mijenja veličinu stranice PDF-a.\n\nSadržaj se automatski prilagođava novoj veličini.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Odaberite standardni format:',
        'pagesize_custom': 'Prilagođena veličina:',
        'pagesize_width': 'Širina:',
        'pagesize_height': 'Visina:',
        'pagesize_orientation': 'Orijentacija:',
        'pagesize_portrait': 'Portret',
        'pagesize_landscape': 'Pejzaž',
        'pagesize_scale_options': 'Opcije skaliranja:',
        'pagesize_fit': 'Prilagodi (zadrži omjer)',
        'pagesize_stretch': 'Rastegni (izobliči)',
        'pagesize_center': 'Centriraj (originalna veličina)',
        'pagesize_range': 'Raspon stranica:',
        'pagesize_all_pages': 'Sve stranice',
        'pagesize_custom_range': 'Prilagođeni raspon',
        'pagesize_from': 'Od:',
        'pagesize_to': 'Do:',
        'pagesize_target_folder': 'Ciljna mapa:',
        'pagesize_browse': 'Pretraži...',
        'pagesize_select_folder': 'Odaberite ciljnu mapu',
        'pagesize_apply': 'Primijeni',
        'pagesize_start': 'Pokretanje promjene veličine stranice...',
        'pagesize_progress': 'Promjena veličine stranice...',
        'pagesize_success': 'Veličina stranice uspješno promijenjena!\n\nSačuvano kao:\n{0}\n\nŽelite li otvoriti novi PDF?',
        'pagesize_complete': 'Promjena veličine stranice završena',
        'pagesize_cancel': 'Promjena veličine stranice otkazana',
        'pagesize_error_format': 'Greška pri promjeni veličine stranice:\n\n{0}',
        'pagesize_preview_info': 'Nova veličina: {0} x {1} pt',
        'filename_pagesize_suffix': '_nova_velicina',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF informacije',
        'pdf_info_menu': 'Prikaži PDF informacije',
        'pdf_info_voice': 'Prikazivanje PDF informacija',
        'pdf_info_error': 'Greška pri prikazivanju PDF informacija:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Prikaži prečice na tastaturi",
        "shortcuts_dialog_title": "Prečice na tastaturi",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 DATOTEKA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Otvori PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Zatvori PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Sačuvaj kao...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Zaštiti dokument</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Štampaj</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Štampaj odmah (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Izađi iz aplikacije</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 IZVOZ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Izvezi kao Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Izvezi kao DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Izvezi kao TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Izvezi kao slike (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Izdvoji slike</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ OBRADA DOKUMENATA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Više stranica)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konverzija (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Izravnaj PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Prekrij PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimiziraj PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ UREĐIVANJE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Pretraži</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Dodaj oznaku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Upravljaj oznakama</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Sljedeća oznaka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Prethodna oznaka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Pokreni OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 UPRAVLJANJE STRANICAMA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rotiraj trenutnu stranicu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rotiraj sve stranice</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normaliziraj trenutnu stranicu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normaliziraj sve stranice</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Obriši stranice</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Izdvoji stranice</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Umetni stranice</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Pomjeri stranice</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Spoji PDF-ove</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Promijeni veličinu stranice</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 UMETANJE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Umetni tekst</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Umetni križ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Umetni potpis 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Umetni potpis 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Umetni sliku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Umetni pravougaonik</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Umetni elipsu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Umetni liniju</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Umetni strelicu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Umetni brojeve stranica</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Vodeni žig (tekst)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Vodeni žig (slika)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ CRNJENJA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Crnjenje (crno)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Crnjenje (bijelo)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Primijeni sva crnjenja</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ NAPREDNO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Obreži PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Uredi metapodatke</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ PRIKAZ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Prebaci Tamni/Svijetli način</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Prikaži prozor teksta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Širina stranice (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dvije stranice (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Pregled (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ POSTAVKE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Upravljanje lozinkama</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR postavke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Postavke potpisa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formatiranje naziva datoteka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Izvezi postavke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Uvezi postavke</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMACIJE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Prikaži PDF informacije</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Uključi/isključi glasovni izlaz</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokusiraj meni traku</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nova verzija dostupna",
        "update_available_message": "Dostupna je nova verzija <b>{0}</b>.\n\nPosjetite stranicu za izdanje da preuzmete ažuriranje:\n{1}",
        "update_available_voice": "Nova verzija {0} je dostupna. Preuzmite ažuriranje sa GitHub stranice.",
        "update_open_release": "Otvori stranicu za izdanje",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Preuzmi sve prijevode",
        "ask_download_all_translations": """Pored njemačkog, engleskog i vijetnamskog, dostupno je još {total_languages} GUI jezika.\n\nDa li ih treba omogućiti / ažurirati?\n\nNapomena:\nNepotrebne jezike kasnije možete ručno obrisati u direktoriju:\n{translations_path}
        \nAko odustanete, GUI jezike kasnije možete preuzeti putem menija 'Alati → Ažuriraj prijevode'.""",
        "menu_update_translations": "Ažuriraj prijevode",
        "translations_updated": "Prijevodi ažurirani",
        "translations_update_success": "{} prijevoda je uspješno ažurirano ({} novih, {} ažuriranih).",
        "translations_update_error": "Greška pri ažuriranju prijevoda",
        "translations_update_no_changes": "Svi prijevodi su već ažurni.",
        "translations_update_offline": "Nema internetske veze. Prijevodi se nisu mogli ažurirati.",
        "translations_update_in_progress": "Prijevodi se ažuriraju u pozadini...",
        "translations_downloading": "Preuzimanje prijevoda...",
        "translations_path_hint": "Korisnički direktorij za prijevode",
        "translations_update_not_available_title": "Ažuriranje nije dostupno",
        "translations_update_not_available_message": """Ažuriranje prijevoda dostupno je samo u instaliranoj verziji.\n\nU razvojnom načinu rada prijevodi su već ažurni.""",
        "translations_update_no_internet_title": "Nema internetske veze",
        "translations_update_no_internet_message": """Nije moguće uspostaviti internetsku vezu.\n\nPrijevodi se ne mogu preuzeti sa GitHub-a.\n\nMoguća rješenja:
        • Provjerite internetsku vezu
        • Privremeno onemogućite eventualni vatrozid
        • Pokušajte ponovo kasnije
        \nPrijevode možete preuzeti i ručno sa GitHub-a:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Ažuriranje je već u toku",
        "btn_retry": "Pokušaj ponovo",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Dobrodošli u PDF Dark View",
        "welcome_title_not_supported": "Dobrodošli u PDF Dark View",
        "welcome_message": "Dobrodošli u PDF Dark View!\n\nVaš sistemski jezik je prepoznat kao '{language}'.\nŽelite li koristiti ovaj jezik za korisnički interfejs?\n\nJezik možete promijeniti u bilo koje vrijeme putem 'Postavke → Jezik'.",
        "welcome_message_language_not_available": "Dobrodošli u PDF Dark View!\n\nVaš sistemski jezik je prepoznat kao '{language}'.\nOvaj jezik još nije instaliran.\n\nŽelite li sada preuzeti prijevode za {language} sa GitHub-a?\n\n(Jezik će se zatim automatski koristiti za korisnički interfejs.)",
        "welcome_message_language_not_supported": "Dobrodošli u PDF Dark View!\n\nVaš sistemski jezik je prepoznat kao '{language}'.\nNažalost, još nema prijevoda za ovaj jezik.\n\nKorisnički interfejs će biti prikazan na {fallback_language}.\n\nJezik možete promijeniti u bilo koje vrijeme putem 'Postavke → Jezik'.\nAko želite, možete i sami doprinijeti prijevod za svoj jezik:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Da, koristi sistemski jezik",
        "welcome_keep_english": "Ne, zadrži engleski",
        "welcome_download_language": "Da, preuzmi {language}",

        # ============================================
        # 107. NEDAVNO KORIŠTENE PUTANJE
        # ============================================

        'menu_recent': 'Nedavno korišteno',
        'menu_recent_dirs': 'Direktoriji...',
        'menu_recent_files': 'Datoteke...',
        'recent_manage': 'Upravljaj...',
        'recent_enable_tracking': 'Sačuvaj nedavno korištene putanje (privatnost)',
        'recent_enable_info': 'Isključite ovu opciju da ne biste sačuvali putanje',
        'recent_tracking_disabled': 'Praćenje putanja je onemogućeno',
        'recent_enabled': 'omogućeno',
        'recent_disabled': 'onemogućeno',
        'recent_tracking_status': 'Praćenje putanja {0}',
        'recent_dialog_title': 'Nedavno korištene putanje',
        'recent_tab_directories': 'Direktoriji',
        'recent_tab_files': 'Datoteke',
        'recent_dirs_instruction': 'Dvokliknite da otvorite dijalog za datoteke u direktoriju',
        'recent_files_instruction': 'Dvokliknite da direktno otvorite PDF',
        'recent_no_directories': '(nema sačuvanih direktorija)',
        'recent_no_files': '(nema sačuvanih datoteka)',
        'recent_default_current': '⭐ Zadano: {0}',
        'recent_set_as_default': '⭐ Postavi kao zadano',
        'recent_default_set_title': 'Zadani direktorij je postavljen',
        'recent_default_set_message': 'Direktorij "{0}" je postavljen kao zadani za otvaranje PDF-ova.',
        'recent_default_set_voice': 'Zadani direktorij je postavljen',
        'recent_directory_not_found': 'Direktorij nije pronađen',
        'recent_file_not_found': 'Datoteka nije pronađena',
        'recent_remove_selected': 'Ukloni',
        'recent_remove_title': 'Ukloni putanju',
        'recent_remove_confirm': 'Da li zaista želite ukloniti putanju "{0}" sa liste?',
        'recent_path_removed': 'Putanja je uklonjena',
        'recent_clear_all': 'Ukloni sve',
        'recent_clear_title': 'Ukloni sve putanje',
        'recent_clear_confirm_type': 'Da li zaista želite izbrisati sve {0}?',
        'recent_cleared': 'Lista je očišćena',
        'recent_path_not_found_title': 'Putanja nije pronađena',
        'recent_path_not_found_message': 'Putanja "{0}" više ne postoji.',
        'recent_open_file': 'Otvorite datoteku',
        'btn_open_recent': 'Otvori',
        'recent_open_file_question': 'Želite li otvoriti "{0}" kao PDF?',
        'recent_not_pdf': 'Odabrana datoteka nije PDF.',
        'recent_more_entries': 'Više unosa...',
        'btn_remove': 'Ukloni',
        'btn_clear': 'Obriši sve',
        'recent_context_open': 'Otvori',
        'recent_context_reveal': 'Prikaži u Finderu',
        'recent_context_set_default': '⭐ Postavi kao zadano',
        'recent_context_open_terminal': '💻 Otvori Terminal',
        'recent_context_file_info': 'Info o datoteci',
        'recent_context_open_with_default': '📄 Otvori sa zadanim programom',
        'recent_context_remove': 'Ukloni sa liste',
        'recent_context_clear_all': 'Ukloni sve',
        'recent_file_info_title': 'Informacije o datoteci',
        'recent_file_info_name': 'Ime',
        'recent_file_info_path': 'Putanja',
        'recent_file_info_size': 'Veličina',
        'recent_file_info_modified': 'Izmijenjeno',
        'recent_file_info_pages': 'Stranice',
        'recent_error_reveal': 'Greška pri otvaranju u Finderu',
        'recent_error_terminal': 'Greška pri otvaranju Terminala',
        'recent_error_info': 'Greška pri dohvaćanju informacija o datoteci',
        'open_user_data_folder': 'Prikaži korisnički direktorij podataka',

        # ============================================
        # 108. BRISANJE PARNIH/NEPARNIH STRANICA
        # ============================================
        "pages_delete_even": "Izbriši sve parne stranice",
        "pages_delete_odd":  "Izbriši sve neparne stranice",
        "progress_even_pages": "Brišu se parne stranice",
        "progress_odd_pages": "Brišu se neparne stranice",
        "progress_mark_delete_even": "{} parna(e) stranica(e) označene za brisanje",
        "progress_mark_delete_odd":  "{} neparna(e) stranica(e) označene za brisanje",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program se zatvara",

    }
