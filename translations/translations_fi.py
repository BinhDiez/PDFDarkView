
# ============================================
# translations_fi.py - Finnisches Wörterbuch
# Vollständig sortiert nach Kategorien
# ============================================

def load_finnish_strings():
    """Lädt alle finnischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Lataa PDF",
        'btn_text_window': "OCR-teksti",
        'btn_first': "Ensimmäinen sivu",
        'btn_prev': "Edellinen sivu",
        'btn_next': "Seuraava sivu",
        'btn_last': "Viimeinen sivu",
        'btn_print': "Tulosta",
        'btn_darkmode_light': "Vaalea tila",
        'btn_darkmode_dark': "Tumma tila",
        'btn_delete_pages': "Poista sivuja",
        'btn_extract_pages': "Poimi sivuja",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Peruuta",
        'btn_save': "Tallenna",
        'btn_close': "Sulje",
        'btn_delete': "Poista",
        'btn_delete_all': "Poista kaikki",
        'btn_copy': "Kopioi",
        'btn_export': "Vie",
        'btn_show': "Näytä salasana",
        'btn_hide': "Piilota salasana",
        'btn_authenticate': "Todenna",
        'btn_settings': "Asetukset",
        'btn_protect': "Suojaa",
        'btn_remove_password': "Poista salasana",
        'btn_manage': "Salasanahallinta",
        'btn_retry': "Yritä uudelleen",
        'btn_select_all': "Valitse kaikki",
        'btn_clear_selection': "Poista valinta",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Sivu {0}/{1}",
        'page_count': "/{0}",
        'goto_page': "Siirry sivulle",
        'page_simple': "Sivu {0}",
        'full_view_page': "Koko näkymä sivu {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Kirjoita hakusana + Enter",
        'search_results': "Osumat: {0}/{1}",
        'search_nav_hint': "Enter: seuraava  (Shift+Enter: edellinen) osuma",
        'search_no_results': "Ei osumia",
        'search_error': "Hakuvirhe",
        'search_active': "Hakukenttä aktivoitu",
        'search_closed': "Haku päättyi",
        'search_position': "Sivu {0} {1}",
        'search_pos_top': "aivan ylhäällä",
        'search_pos_upper': "ylhäällä",
        'search_pos_middle': "keskellä",
        'search_pos_lower': "alhaalla",
        'search_pos_bottom': "aivan alhaalla",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Tekstintunnistus onnistui!",
        'ocr_success_title': "OCR onnistui",
        'ocr_success_message': "Dokumentti on nyt haettavissa.",
        'ocr_failed': "OCR epäonnistui",
        'ocr_in_progress': "OCR käynnissä",
        'ocr_preparing': "Valmistellaan PDF:ää...",
        'ocr_analyzing': "Analysoidaan PDF:ää...",
        'ocr_optimizing': "Kuvan optimointi käynnissä...",
        'ocr_recognizing': "Tekstintunnistus käynnissä...",
        'ocr_embedding': "Upotetaan tekstiä...",
        'ocr_finalizing': "Viimeistellään PDF:ää...",
        'ocr_not_available': "OCR ei ole käytettävissä",
        'ocr_install_message': "OCR-työkaluja ei löytynyt.\n\nAsenna seuraavat:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR vaaditaan",
        'ocr_question': "PDF ei sisällä haettavaa tekstiä.\nHaluatko suorittaa OCR:n, jotta {0} on mahdollista?",
        'ocr_perform': "Suorita OCR",
        'ocr_later': "Myöhemmin",
        'ocr_starting': "Käynnistetään taattu OCR...",
        'ocr_success_voice': "OCR onnistui. PDF on nyt haettavissa.",
        'ocr_partial_success': "OCR suoritettiin, mutta korvaamisessa oli ongelmia.\n\nHaettava versio tallennettiin kohteeseen:\n{0}\n\nVirhe: {1}",
        'ocr_partial_title': "OCR osittain onnistui",
        'ocr_partial_voice': "OCR suoritettiin, mutta korvaaminen epäonnistui.",
        'original_file': "Alkuperäinen tiedosto:",
        'old_size': "Vanha koko:    {0} tavua",
        'new_size': "Uusi koko: {0} tavua",
        'size_change': "Muutos: {0}{1} tavua",
        'backup_created_file': "Varmuuskopio luotu:\n{0}",
        'backup_not_created': "Varmuuskopiota ei luotu (asetus pois päältä)",
        'page_header': "=== Sivu {0} ===\n{1}\n",
        'scanned_page_header': "=== Sivu {0} (skannattu) ===\n[Tämä sivu sisältää vain skannattua tekstiä]\n[Suorita OCR manuaalisesti]\n",
        'scanned_warning': "⚠️ SKANNATTU TEKSTI - OCR VAADITAAN",
        'guaranteed_title': "Haettava PDF luotu",
        'guaranteed_message': "<b>Taattu haettava versio luotu!</b>\n\nKoska automaattinen OCR epäonnistui, luotiin vaihtoehtoinen haettava PDF:\n\n{0}\n\n<b>Tämä tiedosto sisältää:</b>\n• Poimittua tekstiä (jos saatavilla)\n• Ohjeita skannatuille sivuille\n• On täysin haettavissa",
        'guaranteed_voice': "Taattu haettava PDF luotu.",
        'instruction_title': "OCR-OHJE",
        'instruction_file': "Alkuperäinen tiedosto: {0}",
        'instruction_text': "Automaattinen tekstintunnistus (OCR) epäonnistui.\nSuorita OCR manuaalisesti:\n\n1. OCRmyPDF (komentorivi):\n   ocrmypdf --force-ocr \"[TIEDOSTO]\" \"tulos.pdf\"\n\n2. ADOBE ACROBAT (macOS/Windows):\n   • Avaa PDF Acrobatissa\n   • Työkalut > Muokkaa PDF:ää\n   • Valitse 'Tekstintunnistus'\n\n3. PREVIEW (macOS):\n   • Avaa PDF esikatselussa\n   • Tiedosto > Vie...\n   • Quartz-suodatin: 'Reduce File Size'\n   • Ota käyttöön 'Suorita OCR'\n\n4. VERKKOPALVELUT:\n   • smallpdf.com/fi/ocr-pdf\n   • ilovepdf.com/fi/ocr-pdf\n   • adobe.com/fi/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR-ohje luotu",
        'instruction_created_message': "Yksityiskohtainen ohje luotu:\n\n{0}\n\nNoudata ohjeita manuaalista OCR:ää varten.",
        'instruction_created_voice': "OCR-ohje luotu.",
        'ocr_impossible': "OCR ei ole mahdollista",
        'ocr_impossible_message': "OCR:ää ei voitu suorittaa.\n\nKäsittele '{0}' manuaalisesti OCR-ohjelmistolla.",
        'ocr_impossible_voice': "OCR ei mahdollista. Käsittele manuaalisesti.",
        'emergency_title': "Hätä-OCR",
        'emergency_message': "Hätä-PDF luotu:\n\n{0}\n\nKäsittele tämä tiedosto manuaalisesti OCR:llä.",
        'emergency_voice': "Hätä-PDF luotu. Suorita OCR manuaalisesti.",
        'critical_error': "Kriittinen virhe",
        'critical_error_message': "OCR:ää ei voitu käynnistää.\n\nKäynnistä ohjelma uudelleen ja tarkista OCR-asennus.",
        'critical_error_voice': "Kriittinen OCR-virhe",
        'ocr_question_html': "<p>PDF ei sisällä haettavaa tekstiä.<p>Haluatko suorittaa OCR:n, jotta <b>{0}</b> on mahdollista?</p>",
        'ocr_question_voice': "OCR vaaditaan. PDF ei sisällä haettavaa tekstiä. Haluatko suorittaa OCR:n, jotta {0} on mahdollista?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ei PDF:ää ladattu",
        'no_pdf_message': "PDF:ää ei ole ladattu",
        'pdf_not_found': "PDF-tiedostoa ei löydy",
        'file_size': "Tiedoston koko",
        'bytes': "tavua",
        'kb': "kt",
        'mb': "Mt",
        'backup_created': "Varmuuskopio luotu",
        'backup_disabled': "Varmuuskopiointi pois käytöstä",
        'backup_activated': "Varmuuskopiointi aktivoitu",
        'backup_deactivated': "Varmuuskopiointi poistettu käytöstä",
        'backup_status': "Varmuuskopio: {0}",
        'backup_on': "✔ käytössä",
        'backup_off': "✘ pois käytöstä",
        'close_pdf': "Suljetaan PDF: {0}",
        'pdf_not_found_format': "PDF-tiedostoa ei löydy: {0}",
        'error_pdf_load_format': "Virhe ladattaessa PDF:ää: {0}",
        'load_failed_format': "Lataus epäonnistui:\n{0}",
        'decrypted_suffix': "(salaus purettu)",
        'decryption_failed': "Salauksen purku epäonnistui.",
        'decryption_error': "Virhe salauksen purussa",
        'decryption_success': "Salauksen purku onnistui",
        'decryption_success_message': "PDF:n salaus purettu ja tallennettu kohteeseen:\n\n{0}",
        'decryption_success_voice': "PDF:n salaus purettu ja tallennettu.",
        'password_remove_error': "Virhe poistettaessa salasanaa",
        'save_unencrypted': "Tallenna salaamaton PDF",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Tallenna nimellä...",
        'save_copy': "Tallenna kopio",
        'save_success': "PDF tallennettu kohteeseen: {0}",
        'save_encrypted': "Suojattu PDF tallennettu kohteeseen: {0}",
        'save_error': "PDF:ää ei voitu tallentaa",
        'encryption_question': "Haluatko suojata PDF:n salasanalla?",
        'encryption_yes': "Kyllä",
        'encryption_no': "Ei",
        'encryption_cancel': "Peruuta",
        'save_cancel': "Tallennus peruttu",
        'save_encrypted_voice': "Tiedosto salattu ja tallennettu.",
        'save_success_voice': "PDF-tiedosto tallennettu salaamattomana.",
        'save_error_format': "PDF:ää ei voitu tallentaa:\n{0}",
        'export_pages_success': "Pages-vienti onnistui",
        'export_pages_error': "Pages-vienti epäonnistui",
        'export_pages_error_format': "Pages-vienti epäonnistui: {0}",
        'export_word_success': "Word-vienti onnistui",
        'export_word_error': "Word-vienti epäonnistui",
        'export_word_error_format': "Word-vienti epäonnistui: {0}",
        'export_text_success': "Tekstivienti onnistui",
        'export_text_error': "Tekstivienti epäonnistui",
        'export_text_error_format': "Tekstivienti epäonnistui: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Salasana vaaditaan",
        'password_enter': "Anna salasana",
        'password_confirm': "Vahvista salasana",
        'password_new': "Uusi salasana",
        'password_current': "Nykyinen salasana",
        'password_save': "Tallenna salasana (salattuna)",
        'password_saved': "✓ Salasana tälle tiedostolle on tallennettu",
        'password_wrong': "Väärä salasana",
        'password_mismatch': "Salasanat eivät täsmää",
        'password_too_short': "Salasana on liian lyhyt",
        'password_min_length': "Salasanan on oltava vähintään 4 merkkiä pitkä",
        'password_strength': "Salasanan vahvuus",
        'password_strength_very_weak': "Erittäin heikko",
        'password_strength_weak': "Heikko",
        'password_strength_medium': "Keskitaso",
        'password_strength_strong': "Vahva",
        'password_strength_very_strong': "Erittäin vahva",
        'password_char_count': "({0} merkkiä)",
        'password_match': "✓ Täsmää",
        'password_no_match': "✗ Salasanat eivät täsmää",
        'password_show': "Näytä",
        'password_hide': "Piilota",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Salasanahallinta",
        'password_table_filename': "Tiedostonimi",
        'password_table_password': "Salasana",
        'password_count': "{0} tallennettu salasana{1}",
        'password_count_singular': "",
        'password_count_plural': "a",
        'password_none': "Ei tallennettuja salasanoja",
        'password_copied': "{0} salasana{1} kopioitu",
        'password_copied_singular': "",
        'password_copied_plural': "a",
        'password_delete_confirm': "Haluatko varmasti poistaa salasanan tiedostolle '{0}'?",
        'password_delete_multiple': "Haluatko varmasti poistaa {0} valittua salasanaa?",
        'password_delete_all_confirm': "Haluatko varmasti poistaa kaikki {0} tallennettua salasanaa?",
        'password_deleted': "{0} salasana{1} poistett{2}",
        'password_deleted_singular': "",
        'password_deleted_plural': "a",
        'password_deleted_verb_singular': "u",
        'password_deleted_verb_plural': "iin",
        'password_all_deleted': "Kaikki salasanat poistettu",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Salasanageneraattori",
        'generator_generated': "Luotu salasana:",
        'generator_regenerate': "Luo uusi",
        'generator_copy': "Kopioi",
        'generator_use': "Käytä",
        'generator_settings': "Asetukset",
        'generator_length': "Pituus:",
        'generator_group_every': "Erotin joka",
        'generator_group_chars': "merkki.    Erotin:",
        'generator_uppercase': "isot kirjaimet (A-Z)",
        'generator_lowercase': "pienet kirjaimet (a-z)",
        'generator_digits': "numerot (0-9)",
        'generator_symbols': "erikoismerkit (!@#$%^&*)",
        'generator_exclude': "Poissuljetut:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Pääsalasana vaaditaan",
        'master_password_setup': "Aseta pääsalasana",
        'master_password_change': "Vaihda pääsalasana",
        'master_password_enter': "Anna pääsalasanasi",
        'master_password_choose': "Valitse vahva pääsalasana (vähintään 8 merkkiä)",
        'master_password_new': "Anna uusi pääsalasanasi",
        'master_password_confirm': "Vahvista salasana",
        'master_password_authenticate': "Todenna",
        'master_password_success': "Pääsalasana asetettu onnistuneesti.",
        'master_password_changed': "Pääsalasana vaihdettu onnistuneesti.",
        'master_password_removed': "Pääsalasana ja kaikki salasanat on poistettu.",
        'master_password_remove': "Poista pääsalasana",
        'master_password_remove_confirm': "Oletko VARMA, että haluat poistaa KAIKKI salasanat?\n\nTämä toiminto on PERUUTTAMATON!",
        'master_password_export_before': "Haluatko viedä varmuuskopion ennen poistoa?",
        'master_password_export_delete': "Vie ja poista",
        'master_password_delete_now': "Poista heti",
        'master_password_for_signatures': "Käyttääksesi allekirjoituksia sinun on asetettava pääsalasana.\n\nHaluatko asettaa pääsalasanan nyt?",
        'master_password_for_private': "Käyttääksesi yksityisiä tekstipaloja sinun on asetettava pääsalasana.\n\nHaluatko asettaa pääsalasanan nyt?",
        'master_password_info': """
            <b>🔐 ILMAN PÄÄSALASANAA:</b><br>
            • Salasanojen näyttäminen, kopiointi ja vienti ei ole mahdollista<br>
            • Salasanojen poistaminen on aina mahdollista (myös ilman pääsalasanaa)<br><br>

            <b>🔐 PÄÄSALASANAN KANSSA:</b><br>
            • Kaikki toiminnot käytettävissä todennuksen jälkeen<br>
            • Salasanat salataan pääsalasanalla<br>
            • Vähimmäispituus: 8 merkkiä<br>
            • Turvallinen SHA-256-tallennus<br><br>

            <b>TÄRKEÄÄ:</b><br>
            • Jos unohdat pääsalasanan, salasanoja ei voi palauttaa<br>
            • Kun poistat pääsalasanan, KAIKKI salasanat poistetaan<br>
            • Vientivaihtoehto saatavilla ennen poistoa<br>
            • Pääsalasanaa voi vaihtaa milloin tahansa
        """,
        'signature_auth_disabled': "Poista salasanakysely allekirjoituksilta",
        'template_auth_disabled': "Poista salasanakysely yksityisiltä tekstipaloilta",
        'master_password_for_signatures_settings': "Käyttääksesi allekirjoituksia sinun on asetettava pääsalasana.\n\nSiirry tätä varten Asetukset - Salasanahallinta",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Suojaa PDF",
        'protect_info': "Tiedosto '{0}' suojataan salasanalla.",
        'protect_instruction': "Anna haluamasi salasana kahdesti suojataksesi dokumentin, tai käytä salasanageneraattoria syöttökentän oikealla puolella.",
        'protect_success': "PDF suojattu onnistuneesti ja tallennettu kohteeseen:\n{0}\n\nSalasana: {1}\n\nHaluatko avata suojatun PDF:n nyt?",
        'protect_open': "Kyllä",
        'protect_skip': "Ei",
        'protect_error': "Virhe suojattaessa PDF:ää",
        'protect_open_title': "Avaa suojattu PDF",
        'protect_question': "Valmis. Haluatko avata suojatun PDF:n nyt? Kyllä vai Ei?",
        'password_cancel': "Salasanaikkuna peruttu",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Poista sivuja",
        'pages_extract': "Poimi sivuja",
        'pages_insert': "Lisää sivuja",
        'pages_move': "Siirrä sivuja",
        'pages_delete_options': "Poistovaihtoehdot",
        'pages_delete_empty': "Poista kaikki tyhjät sivut",
        'pages_delete_current': "Poista nykyinen sivu",
        'pages_delete_range': "Poista sivualue",
        'pages_extract_options': "Poimintavaihtoehdot",
        'pages_extract_current': "Poimi nykyinen sivu",
        'pages_extract_range': "Poimi sivualue",
        'pages_insert_position': "Lisäyspaikka",
        'pages_insert_before': "Lisää ennen sivua:",
        'pages_insert_select': "Valitse PDF",
        'pages_insert_none': "PDF:ää ei valittu",
        'pages_move_source': "Siirrettävät sivut",
        'pages_move_from': "Sivulta:",
        'pages_move_to': "Sivulle:",
        'pages_move_target': "Kohdepaikka",
        'pages_move_before': "Siirrä ennen sivua:",
        'pages_move_hint': "Huom: sivu 1 = alku, {0} = loppu",
        'pages_range_invalid': "Alkusivun on oltava pienempi tai yhtä suuri kuin loppusivu.",
        'pages_position_invalid': "Kohdepaikka ei voi olla siirrettävän alueen sisällä.",
        'pages_no_pdf_selected': "PDF:ää ei ole valittu.",
        'pages_deleted': "{0} sivua poistettiin.",
        'pages_extracted': "Poimittu: {0}\nTallennettu kohteeseen: {1}\nTiedoston koko: {2:.1f} kt",
        'pages_inserted': "{0} sivua lisätty",
        'pages_moved': "{0} sivua siirrettiin.",
        'pages_deleted_none': "Sivuja ei poistettu.",
        'pages_delete_progress': "Poistetaan sivuja...",
        'pages_deleted_with_backup': "{0} sivua poistettiin.\n\nVarmuuskopio: {1}",
        'pages_deleted_voice': "Varmuuskopio luotiin ja {0} sivua poistettiin.",
        'info': "Huomautus",
        'error_dialog_creation': "Ikkunaa ei voitu luoda",
        'extract_page_single': "Poimi sivu {0}",
        'extract_page_range': "Poimi sivut {0}-{1}",
        'extract_success_voice': "Sivut poimittu onnistuneesti",
        'extract_error_format': "Virhe poimittaessa: {0}",
        'pages_inserted_voice': "{0} sivua lisättiin.",
        'insert_error_format': "Virhe lisättäessä: {0}",
        'pages_move_progress': "Siirretään sivuja...",
        'pages_moved_with_backup': "{0} sivua siirrettiin.\n\nVarmuuskopio: {1}",
        'move_success_title': "Siirto onnistui",
        'pages_moved_voice': "{0} sivua siirretty onnistuneesti",
        'mark_removed': "Merkintä poistettu sivulta {0}",
        'mark_empty': "Sivu {0} merkitty tyhjäksi",
        'mark_export_removed': "Vientimerkintä poistettu sivulta {0}",
        'mark_export': "Sivu {0} merkitty vietäväksi",
        'no_empty_pages': "Ei tyhjiä sivuja poistettavaksi merkitty",
        'delete_empty_confirm': "Haluatko poistaa kaikki {0} merkittyä tyhjää sivua?",
        'delete_empty_confirm_voice': "Poistetaanko nyt kaikki {0} merkittyä tyhjää sivua? Kyllä vai Ei.",
        'empty_pages_deleted': "{0} tyhjää sivua poistettu",
        'no_export_pages': "Ei vietäväksi merkittyjä sivuja",
        'overwrite_title': "Korvaa olemassa oleva tiedosto",
        'overwrite_question': "Tiedosto\n\n{0}\n\non jo olemassa.\nHaluatko korvata sen?",
        'overwrite_voice': "Korvataanko olemassa oleva tiedosto? Kyllä vai Ei.",
        'page_skipped': "Sivu {0} ohitettiin",
        'export_complete': "Vienti valmis.",
        'export_complete_voice': "Vienti on valmis.",
        'no_pages_exported': "Yhtään sivua ei viety",
        'export_cancelled': "Vienti peruttu",
        'pages_exported': "{0} sivua viety kohteeseen {1}",
        'export_page_title': "Vie sivu",
        'page_exported': "Sivu {0} viety kohteeseen {1}",
        'export_error': "Virhe viennissä",
        'export_marked_title': "Vie merkityt sivut",
        'rotate_all_title': "Kierrä kaikkia sivuja",
        'rotate_all_question': "Haluatko kiertää kaikkia sivuja 90 astetta oikealle?",
        'rotate_all_voice': "Haluatko kiertää kaikkia sivuja 90 astetta oikealle? Kyllä vai Ei?",
        'all_pages_rotated': "Kaikki sivut kierretty",
        'page_rotated': "Sivu {0} kierretty",
        'rotate_error': "Sivua ei voitu kiertää",
        'delete_page_confirm': "Haluatko poistaa sivun {0}?",
        'delete_page_confirm_voice': "Haluatko varmasti poistaa sivun {0}? Kyllä vai Ei.",
        'page_deleted': "Sivu {0} poistettu",
        'delete_error': "Sivua ei voitu poistaa",
        'pages_deleted_voice': "{0} sivua poistettu",
        'pages_exported_split': "{0} sivua vietiin onnistuneesti.",
        'pages_skipped': "{0} sivua ohitettiin.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Poimi sivuja (laajennettu)",
        'pdf_splitter_title': "PDF Splitter & Poimija",
        'pdf_splitter_load': " Valitse PDF-tiedosto",
        'pdf_splitter_info': "Valitse vaihtoehto PDF-dokumentillesi",
        'pdf_splitter_basic': "Perustoiminnot",
        'pdf_splitter_single': "Jaa yksittäisiksi sivuiksi",
        'pdf_splitter_range': "Poimi sivut:",
        'pdf_splitter_range_placeholder': "esim. 1-3,5,7-9",
        'pdf_splitter_clean': "Puhdistustoiminnot",
        'pdf_splitter_remove_empty': "Poista kaikki tyhjät sivut",
        'pdf_splitter_remove': "Poista sivualue:",
        'pdf_splitter_remove_placeholder': "esim. 2,4-6",
        'pdf_splitter_process': "Käsittele PDF",
        'pdf_splitter_loaded': "PDF ladattu. Valitse vaihtoehto",
        'pdf_read_error': "PDF:ää ei voitu lukea",
        'pages': "Sivut",
        'pages_created': "Sivut luotu",
        'range_empty': "Anna sivualue",
        'range_invalid': "Virheellinen sivualue",
        'range_created': "Uusi PDF valituilla sivuilla luotu:\n{0}",
        'empty_removed': "{0} tyhjää sivua poistettu.\nTulos: {1}",
        'remove_empty': "Anna poistettavat sivut",
        'remove_invalid': "Virheelliset poistettavat sivut",
        'remove_done': "Puhdistettu PDF luotu:\n{0}",
        'open_folder': "Avaa kansio",
        'show_in_finder': "Näytä Finderissa",
        'pdf_splitter_no_pdf': "Lataa ensin PDF-tiedosto.",
        'process_error': "Virhe käsiteltäessä PDF:ää",
        'pages_created_voice': "{0} sivua luotu",
        'range_created_voice': "PDF valituilla sivuilla luotu",
        'empty_removed_voice': "{0} tyhjää sivua poistettu",
        'remove_done_voice': "Puhdistettu PDF luotu",
        'pdf_splitter_split_groups': "Jokainen yhtenäinen ryhmä erilliseen tiedostoon",
        'range_created_single': "Uusi PDF luotu:\n{0}",
        'range_created_multiple': "{0} PDF-tiedostoa luotu.",
        'range_created_voice_single': "Yksi PDF valituilla sivuilla luotu",
        'range_created_voice_multiple': "{0} PDF-tiedostoa luotu",
        'empty_removed_none_left': "Ei jäljellä olevia sivuja",
        'empty_removed_all_empty': "Kaikki sivut tunnistettiin tyhjiksi, joten tiedostoa ei luotu.",
        'preview_single': "Esikatselu: {0}",
        'preview_enter_range': "Anna sivualue.",
        'preview_invalid_range': "Virheellinen sivualue.",
        'preview_file': "Esikatselu: {0}",
        'preview_files': "Esikatselu: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Aloitetaan tulostus",
        'print_sent': "Tulostustyö lähetetty",
        'print_now': "Tulosta heti",
        'print_error': "Virhe heti-tulostuksessa",
        'print_limited': "Tulostustoiminto rajoitettu tässä järjestelmässä",
        'print_error_format': "Virhe heti-tulostuksessa: {0}",
        'warning': "Huomautus",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Vaihda vaaleaan tilaan",
        'mode_switch_to_dark': "Vaihda tummaan tilaan",
        'mode_dark_activated': "Tumma tila aktivoitu",
        'mode_light_activated': "Vaalea tila aktivoitu",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Koko sivu",
        'zoom_two_pages': "Kaksi sivua vierekkäin",
        'zoom_overview': "Yleiskuva",
        'zoom_cannot_during_search': "Zoomaus ei ole mahdollista haun aikana",
        'zoom_exit_first': "Poistu ensin zoomauksesta",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Vedä ja pudota käytössä",
        'drag_disabled': "Vedä ja pudota pois käytöstä",
        'drag_page_grab': "Sivu {0} otettu",
        'drag_page_dropped': "Sivu {0} lisätty paikkaan {1}",
        'drag_position_invalid': "Virheellinen paikka",
        'drag_same_position': "Sivu {0} pysyy paikassa {0}",
        'drag_error': "Virhe siirrettäessä",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Tekstinsyöttö laajennetuilla muotoiluilla ja tekstipalojen hallinnalla",
        'text_templates': "Käytettävissä olevat tekstipalat:",
        'text_name': "Nimi",
        'text_preview': "Tekstin esikatselu",
        'text_enter': "Teksti:",
        'text_font_size': "Kirjasinkoko:",
        'text_formatting': "Muotoilu:",
        'text_bold': "Lihavoitu",
        'text_italic': "Kursivoitu",
        'text_underline': "Alleviivattu",
        'text_alignment': "Tasaus:",
        'text_left': "Vasen",
        'text_center': "Keskitetty",
        'text_right': "Oikea",
        'text_color': "Tekstin väri:",
        'text_opacity': "Peittävyys:",
        'text_word_wrap': "Rivitys:",
        'text_auto': "Automaattinen",
        'text_page_width_95': "Sivun leveys (95 %)",
        'text_page_width_85': "Erittäin leveä (85 %)",
        'text_page_width_75': "Leveämpi (75 %)",
        'text_page_width_60': "Leveä (60 %)",
        'text_page_width_50': "Keskitaso (50 %)",
        'text_page_width_30': "Kapea (30 %)",
        'text_page_width_20': "Kapeampi (20 %)",
        'text_page_width_10': "Erittäin kapea (10 %)",
        'text_no_wrap': "Ei rivitystä",
        'text_private': "Yksityinen tekstipala (vaatii todennuksen)",
        'text_preview_label': "Esikatselu:",
        'text_preview_placeholder': "Tekstin esikatselu näkyy tässä...",
        'text_no_text': "(Ei tekstiä)",
        'text_save_template': "💾 Tallenna palaksi",
        'text_delete_template': "🗑 Poista valittu tekstipala",
        'text_show_private': "Näytä yksityiset",
        'text_hide_private': "Piilota yksityiset",
        'text_use': "✅ Käytä tekstiä",
        'text_saved': "Tekstipala tallennettu nimellä:\n{0}",
        'text_saved_voice': "Tekstipala tallennettu",
        'text_deleted': "Tekstipala poistettu",
        'text_no_text_to_save': "Ei tallennettavaa tekstiä.",
        'text_no_templates': "Tekstipaloja ei löytynyt",
        'text_private_master_required': "Yksityisiä paloja voidaan käyttää vain, jos pääsalasana on asetettu.\n\nHaluatko asettaa pääsalasanan nyt?",
        'text_filename': "Tiedostonimi tekstipalalle (ilman 'Text_' ja '.txt'):",
        'text_filename_hint': "Esimerkki: 'Puhelin Kotitoimisto' tallennetaan nimellä 'Text_Puhelin Kotitoimisto.txt'",
        'text_save_hint': "Tekstipala tallennetaan automaattisesti muotoilun kanssa.",
        'text_guide_title': "Tekstinsyöttö - Ohje",
        'text_delete_confirm': "Haluatko varmasti poistaa tekstipalan?\n\nTiedosto: {0}\nTeksti: {1}...",
        'text_make_public': "Merkitse julkiseksi",
        'text_make_private': "Merkitse yksityiseksi",
        'text_privacy_changed': "Yksityisyysasetus muutettu",
        'text_private_always': "Yksityiset aina näkyvissä (asetus)",
        'text_mode_required': "Aktivoi ensin tekstinsyöttötila",
        'text_continue_editing': "Jatka muokkausta - kursori tekstin lopussa",
        'text_no_input': "Tekstiä ei syötetty - teksti hylätty",
        'save_dialog_question': "Miten haluat jatkaa?",
        'text_save_question': "Tallennetaanko kaikki tekstit ja rastit, muokataanko, jatketaanko muokkausta vai hylätäänkö?",
        'copy_cross': "Rasti kopioitu",
        'paste_cross': "Rasti liitetty",
        'paste_text': "Teksti liitetty",
        'cross_discarded': "Rasti hylätty",
        'all_discarded': "Kaikki hylätty",
        'text_discarded': "Teksti hylätty",
        'no_texts_to_save': "Ei tallennettavia tekstejä",
        'no_valid_texts': "Ei kelvollisia tekstejä tallennettavaksi",
        'text_word_singular': "teksti",
        'text_word_plural': "tekstiä",
        'cross_word_singular': "rasti",
        'cross_word_plural': "rastia",
        'texts_saved_title': "Tekstit tallennettu",
        'texts_crosses_saved': "{0} {1} ja {2} {3} lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'texts_crosses_saved_voice': "{0} {1} ja {2} {3} tallennettu.",
        'texts_saved': "{0} {1} lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'texts_saved_voice': "{0} {1} tallennettu.",
        'crosses_saved': "{0} {1} lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'crosses_saved_voice': "{0} {1} tallennettu.",
        'elements_saved': "{0} elementtiä lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'elements_saved_voice': "{0} elementtiä tallennettu.",
        'text_window_load_error': "Teksti-ikkunaa ei voitu ladata",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Tekstinsyöttö ja tekstipalat – Yksityiskohtainen ohje**

        **1. Tekstin lisääminen ja muokkaaminen**
        - Napsauta hiiren kakkospainikkeella haluamaasi kohtaan asiakirjassa ja valitse "Lisää teksti".
        - Avautuu ikkuna, jossa voit kirjoittaa tekstin ja muotoilla sen:
        • Kirjasinkoko, lihavointi, kursivointi, alleviivaus
        • Tekstin väri (vapaasti valittavissa)
        • Läpinäkyvyys (peittävyys) liukusäätimellä
        • Rivitys (erilaisia leveyksiä, esim. sivun leveys, kapea, ei rivitystä)
        - Vahvistuksen jälkeen teksti ilmestyy napsautuskohtaan. Voit siirtää sitä hiirellä tai nuolinäppäimillä.
        - Kaksoisnapsautus tekstiä avaa muokkaustilan; ESC poistuu siitä.

        **2. Tekstipalojen hallinta**
        - Teksti-ikkunan vasemmassa reunassa näet luettelon kaikista tallennetuista tekstipaloista.
        - **Palon tallentaminen:** Kirjoita teksti, muotoile se ja napsauta "💾 Tallenna palaksi". Anna tiedostonimi (ilman päätettä).
        - **Palon lataaminen:** Napsauta haluamaasi nimeä luettelossa. Teksti ja muotoilu kopioituvat ja niitä voidaan tarvittaessa muokata.
        - **Poistaminen:** Napsauta palaa hiiren kakkospainikkeella ja voit poistaa sen tai muuttaa sen yksityisyysasetusta.

        **3. Yksityiset tekstipalat (pääsalasana)**
        - Jos olet asettanut pääsalasanan (Asetukset → Salasanahallinta), voit merkitä paloja "yksityisiksi".
        - Ota tällöin käyttöön valintaruutu "Yksityinen tekstipala" ennen tallennusta.
        - Yksityiset palat näkyvät luettelossa vain, jos olet kirjautunut sisään pääsalasanalla kerran istunnon aikana (todennus lukkokuvakkeella tai ensimmäisellä käyttökerralla).
        - Näin voit suojata luottamukselliset tekstipalat vieraalta käytöltä.

        **4. Rastien lisääminen**
        - Napsauta hiiren kakkospainikkeella ja voit lisätä myös graafisen rastin (esim. valintaruutua varten).
        - Rastien kokoa, viivan paksuutta ja väriä voi muuttaa yleisesti asetuksista (valikko "Asetukset" → "Rastien asetukset").
        - Napsauttamalla olemassa olevaa rastia hiiren kakkospainikkeella voit muokata sitä yksilöllisesti.

        **5. Yhteistoiminnot**
        - Jos olet sijoittanut useita tekstejä tai rasteja samalle sivulle, voit tallentaa tai hylätä ne kaikki yhdellä kertaa napsauttamalla hiiren kakkospainikkeella tekstinsyöttötilassa.
        - Tallennettaessa kaikki elementit upotetaan PDF:ään ja säilyvät vektorigrafiikkana.

        **6. Pikanäppäimet tekstinsyöttötilassa**
        - Nuolinäppäimet: elementin siirto
        - Ctrl + nuolinäppäimet: suuremmat siirtoaskeleet
        - Enter: tallennusvalinta (tallenna kaikki / muokkaa / hylkää)
        - ESC: nykyisen elementin hylkääminen
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Tekstinsyöttö ja tekstipalat – Yksityiskohtainen ohje</strong></p>

        <p><strong>1. Tekstin lisääminen ja muokkaaminen</strong></p>
        <ul>
        <li>Napsauta hiiren kakkospainikkeella haluamaasi kohtaan asiakirjassa ja valitse "Lisää teksti".</li>
        <li>Avautuu ikkuna, jossa voit kirjoittaa tekstin ja muotoilla sen:<br/>
        • Kirjasinkoko, lihavointi, kursivointi, alleviivaus<br/>
        • Tekstin väri (vapaasti valittavissa)<br/>
        • Läpinäkyvyys (peittävyys) liukusäätimellä<br/>
        • Rivitys (erilaisia leveyksiä, esim. sivun leveys, kapea, ei rivitystä)</li>
        <li>Vahvistuksen jälkeen teksti ilmestyy napsautuskohtaan. Voit siirtää sitä hiirellä tai nuolinäppäimillä.</li>
        <li>Kaksoisnapsautus tekstiä avaa muokkaustilan; ESC poistuu siitä.</li>
        </ul>

        <p><strong>2. Tekstipalojen hallinta</strong></p>
        <ul>
        <li>Teksti-ikkunan vasemmassa reunassa näet luettelon kaikista tallennetuista tekstipaloista.</li>
        <li><strong>Palon tallentaminen:</strong> Kirjoita teksti, muotoile se ja napsauta "💾 Tallenna palaksi". Anna tiedostonimi (ilman päätettä).</li>
        <li><strong>Palon lataaminen:</strong> Napsauta haluamaasi nimeä luettelossa. Teksti ja muotoilu kopioituvat ja niitä voidaan tarvittaessa muokata.</li>
        <li><strong>Poistaminen:</strong> Napsauta palaa hiiren kakkospainikkeella ja voit poistaa sen tai muuttaa sen yksityisyysasetusta.</li>
        </ul>

        <p><strong>3. Yksityiset tekstipalat (pääsalasana)</strong></p>
        <ul>
        <li>Jos olet asettanut pääsalasanan (Asetukset → Salasanahallinta), voit merkitä paloja "yksityisiksi".</li>
        <li>Ota tällöin käyttöön valintaruutu "Yksityinen tekstipala" ennen tallennusta.</li>
        <li>Yksityiset palat näkyvät luettelossa vain, jos olet kirjautunut sisään pääsalasanalla kerran istunnon aikana (todennus lukkokuvakkeella tai ensimmäisellä käyttökerralla).</li>
        <li>Näin voit suojata luottamukselliset tekstipalat vieraalta käytöltä.</li>
        </ul>

        <p><strong>4. Rastien lisääminen</strong></p>
        <ul>
        <li>Napsauta hiiren kakkospainikkeella ja voit lisätä myös graafisen rastin (esim. valintaruutua varten).</li>
        <li>Rastien kokoa, viivan paksuutta ja väriä voi muuttaa yleisesti asetuksista (valikko "Asetukset" → "Rastien asetukset").</li>
        <li>Napsauttamalla olemassa olevaa rastia hiiren kakkospainikkeella voit muokata sitä yksilöllisesti.</li>
        </ul>

        <p><strong>5. Yhteistoiminnot</strong></p>
        <ul>
        <li>Jos olet sijoittanut useita tekstejä tai rasteja samalle sivulle, voit tallentaa tai hylätä ne kaikki yhdellä kertaa napsauttamalla hiiren kakkospainikkeella tekstinsyöttötilassa.</li>
        <li>Tallennettaessa kaikki elementit upotetaan PDF:ään ja säilyvät vektorigrafiikkana.</li>
        </ul>

        <p><strong>6. Pikanäppäimet tekstinsyöttötilassa</strong></p>
        <ul>
        <li>Nuolinäppäimet: elementin siirto</li>
        <li>Ctrl + nuolinäppäimet: suuremmat siirtoaskeleet</li>
        <li>Enter: tallennusvalinta (tallenna kaikki / muokkaa / hylkää)</li>
        <li>ESC: nykyisen elementin hylkääminen</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Rastien asetukset",
        'cross_properties': "Rastin ominaisuudet",
        'cross_size': "Koko (px):",
        'cross_line_width': "Viivan paksuus:",
        'cross_color': "Väri:",
        'cross_choose_color': "Valitse",
        'cross_fine_tuning': "Hienosäätö tallennettaessa (pikseliä)",
        'cross_offset_x': "X-siirto:",
        'cross_offset_y': "Y-siirto:",
        'cross_offset_x_tooltip': "Negatiiviset arvot siirtävät rastia tallennettaessa vasemmalle, positiiviset oikealle",
        'cross_offset_y_tooltip': "Negatiiviset arvot siirtävät rastia tallennettaessa ylöspäin, positiiviset alaspäin",
        'cross_preview': "Esikatselu",
        'cross_save': "Ota asetukset käyttöön",
        'cross_customized': "Rastia muokattu",
        'cross_settings_applied': "Rastiasetukset tallennettu.\nKoko: {0}px, viivan paksuus: {1}px\n{2}",
        'cross_updated_count': "{0} olemassa olevaa rastia päivitettiin.",
        'cross_no_crosses': "Olemassa olevia rasteja ei löytynyt.",
        'cross_settings_applied_all': "Rastiasetukset otettu käyttöön kaikille {0} rastille",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Allekirjoitusasetukset",
        'signature_1': "Allekirjoitus 1",
        'signature_2': "Allekirjoitus 2",
        'signature_select': "Valitse allekirjoitus",
        'signature_add': "➕ Lisää uusi allekirjoitus...",
        'signature_size': "Allekirjoituksen {0} koko (%):",
        'signature_common': "Yleiset asetukset",
        'signature_timestamp': "Lisää aikaleima automaattisesti",
        'signature_location': "Oletuspaikka:",
        'signature_timestamp_size': "Aikaleiman kirjasinkoko:",
        'signature_no_files': "-- Allekirjoituksia ei löytynyt --",
        'signature_insert': "Lisää allekirjoitus",
        'signature_insert_1': "Lisää allekirjoitus 1",
        'signature_insert_2': "Lisää allekirjoitus 2",
        'signature_customize': " Mukauta allekirjoitusta",
        'signature_discard': " Hylkää tämä allekirjoitus",
        'signature_save_all': " Tallenna kaikki allekirjoitukset",
        'signature_discard_all': " Hylkää kaikki allekirjoitukset",
        'signature_guide_title': "Allekirjoitukset - Ohje",
        'signature_guide': """
📝 Allekirjoitukset - Pikaohje

- Aseta pääsalasana
- Määritä allekirjoitukset valikossa Asetukset
  (koko, aikaleima ...)
- Lisää napsauttamalla HALUTTUA PAIKKAA hiiren kakkospainikkeella
  (pääsalasana vaaditaan kerran istunnossa)
- Siirrä allekirjoitusta hiirellä tai nuolinäppäimillä
- Useita allekirjoituksia voidaan lisätä peräkkäin
- Jokaista allekirjoitusta voi muokata yksilöllisesti
- Hylkää yksittäinen allekirjoitus
- Tallenna / hylkää kaikki allekirjoitukset kerralla
- Vaihtoehtoisesti voit käyttää myös valikkopalkkia.
        """,
        'signature_placeholder': "Esikatselu ei saatavilla",
        'signature_info': "Allekirjoitus {0}: {1}×{2} px ({3}% koosta {4}×{5})",
        'signature_info_placeholder': "Allekirjoituksen {0} asetukset",
        'signature_inserted': "Allekirjoitus {0} lisätty sivulle {1}",
        'signature_deleted': "Allekirjoitus poistettu",
        'signature_copied': "Allekirjoitus kopioitu",
        'signature_pasted': "Allekirjoitus {0} liitetty",
        'signature_saved': "{0} allekirjoitusta lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'signature_saved_voice': "{0} allekirjoitusta tallennettu",
        'mode_replace_signature_format': "Poistu tilasta ja lisää allekirjoitus {0}",
        'mode_conflict_voice_signature': "{0} -tila on aktiivinen. Poistutaanko ja lisätäänkö allekirjoitus?",
        'signature_not_configured': "Allekirjoitusta {0} ei ole määritetty",
        'signature_file_not_found': "Allekirjoitustiedostoa ei löydy",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Kopioitua allekirjoitusta ei ole",
        'no_signatures_to_save': "Ei tallennettavia allekirjoituksia",
        'signature_save_question': "Tallennetaanko kaikki allekirjoitukset, muokataanko vai hylätäänkö tämä?",
        'signatures_saved_title': "Allekirjoitukset tallennettu",
        'signatures_saved': "{0} allekirjoitusta lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'signatures_saved_voice': "{0} allekirjoitusta tallennettu.",
        'all_signatures_discarded': "Kaikki allekirjoitukset hylätty",
        'signature_settings_saved': "Allekirjoitusasetukset tallennettu",
        'signature_cancelled': "Allekirjoitus hylätty",
        'signature_active_title': "Allekirjoitus aktiivinen",
        'signature_replace_question': "Allekirjoitus on jo aktiivinen.\n\nHaluatko korvata nykyisen allekirjoituksen?",
        'signature_replace': "Korvaa allekirjoitus",
        'signature_replace_voice': "Korvataanko nykyinen allekirjoitus vai peruutetaanko?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Kuvien asetukset",
        'image_common': "Yleiset kuvien asetukset",
        'image_keep_aspect': "Säilytä kuvasuhde vedettäessä",
        'image_default_size': "Oletuskoko (%):",
        'image_dark_invert': "Käännä kuvien värit tummassa tilassa",
        'image_dark_invert_tooltip': "Käytössä: kuvien värit käännetään paremman näkyvyyden takaamiseksi",
        'image_fine_tuning': "Hienosäätö (pikseliä)",
        'image_offset_x': "X-siirto:",
        'image_offset_y': "Y-siirto:",
        'image_offset_x_tooltip': "Negatiiviset arvot siirtävät kuvaa tallennettaessa vasemmalle, positiiviset oikealle",
        'image_offset_y_tooltip': "Negatiiviset arvot siirtävät kuvaa tallennettaessa ylöspäin, positiiviset alaspäin",
        'image_select': "Valitse kuva",
        'image_insert': "Lisää kuva",
        'image_customize': " Mukauta kuvaa",
        'image_aspect': " Säilytä kuvasuhde",
        'image_discard': " Hylkää tämä kuva",
        'image_save_all': " Tallenna kaikki kuvat",
        'image_discard_all': " Hylkää kaikki kuvat",
        'image_filter': "Kuvat",
        'image_guide_title': "Kuvien lisääminen - Ohje",
        'image_guide': """
📷 Kuvien lisääminen PDF:ään - Pikaohje:

1. Napsauta hiiren kakkospainikkeella haluamaasi paikkaa
2. "Lisää kuva" → valitse kuva
3. Sijoita kuva: vedä hiirellä
4. Säädä kokoa: vedä kulmista/reunoista
5. Säilytä kuvasuhde: [A]-näppäin
6. Lisää muokkauksia: napsauta kuvaa hiiren kakkospainikkeella

Vinkki: Voit muokata asetuksia pikavalikosta.
        """,
        'image_inserted': "Kuva {0} lisätty sivulle {1}",
        'image_deleted': "Kuva hylätty",
        'image_copied': "Kuva kopioitu",
        'image_pasted': "Kuva liitetty",
        'image_saved': "{0} kuvaa lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'image_saved_voice': "{0} kuvaa tallennettu",
        'image_aspect_on': "käytössä",
        'image_aspect_off': "pois käytöstä",
        'image_aspect_toggle': "Säilytä kuvasuhde {0}",
        'image_reset': "Kuva palautettu alkuperäiseen kokoon",
        'image_replaced': "Kuva korvattu",
        'image_invalid': "Ei kelvollinen kuva",
        'mode_replace_image': "Lisää kuva",
        'mode_conflict_voice_image': "{0} -tila on aktiivinen. Poistutaanko ja lisätäänkö kuva?",
        'image_active_title': "Kuva aktiivinen",
        'image_replace_question': "Kuva on jo aktiivinen.\n\nHaluatko korvata nykyisen kuvan?",
        'image_replace': "Korvaa kuva",
        'image_replace_voice': "Korvataanko nykyinen kuva vai peruutetaanko?",
        'image_filter_all': "Kuvat (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Kaikki tiedostot (*.*)",
        'no_copied_image': "Kopioitua kuvaa ei ole",
        'image_discarded': "Kuva hylätty",
        'image_save_question': "Tallennetaanko kaikki kuvat, muokataanko vai hylätäänkö tämä?",
        'no_images_to_save': "Ei tallennettavia kuvia",
        'no_valid_images': "Ei kelvollisia kuvia tallennettavaksi",
        'images_saved_title': "Kuvat tallennettu",
        'images_saved': "{0} kuvaa lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'images_saved_voice': "{0} kuvaa tallennettu.",
        'all_images_discarded': "Kaikki kuvat hylätty",
        'image_settings_updated': "Kuvien asetukset päivitetty",
        'image_replace_title': "Valitse uusi kuva",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Muotojen asetukset",
        'form_basic': "Perusasetukset",
        'form_default_type': "Oletusmuoto:",
        'form_rectangle': "Suorakulmio",
        'form_ellipse': "Ellipsi",
        'form_line': "Viiva",
        'form_arrow': "Nuoli",
        'form_line_width': "Viivan paksuus:",
        'form_colors': "Värit",
        'form_line_color': "Viivan väri:",
        'form_fill_color': "Täyttöväri:",
        'form_choose_color': "Valitse",
        'form_transparent': "Läpinäkyvä tausta (vain viiva)",
        'form_filled': "täytetty",
        'form_dark_mode': "Tumma tila",
        'form_dark_invert': "Käännä värit tummassa tilassa",
        'form_fine_tuning': "Hienosäätö (pikseliä)",
        'form_offset_x': "X-siirto:",
        'form_offset_y': "Y-siirto:",
        'form_offset_x_tooltip': "Negatiiviset arvot siirtävät muotoa tallennettaessa vasemmalle, positiiviset oikealle",
        'form_offset_y_tooltip': "Negatiiviset arvot siirtävät muotoa tallennettaessa ylöspäin, positiiviset alaspäin",
        'form_preview': "Esikatselu",
        'form_insert': "Lisää muoto",
        'form_rectangle_insert': "Suorakulmio",
        'form_ellipse_insert': "Ellipsi/ympyrä",
        'form_line_insert': "Viiva (2 napsautusta)",
        'form_arrow_insert': "Nuoli (2 napsautusta)",
        'form_customize': " Mukauta muotoa",
        'form_transparent_toggle': " Läpinäkyvä tausta",
        'form_discard': " Hylkää tämä muoto",
        'form_save_all': " Tallenna kaikki muodot",
        'form_discard_all': " Hylkää kaikki muodot",
        'form_guide_title': "Muotojen lisääminen - Ohje",
        'form_guide': """
📐 Muotojen lisääminen PDF:ään - Pikaohje:

1. Valitse muototyyppi (suorakulmio, ellipsi, viiva, nuoli)
2. Napsauta haluttua paikkaa
   - Suorakulmio/ellipsi: yksi napsautus sijoittaa muodon
   - Viiva/nuoli: kaksi napsautusta alku- ja loppupisteelle
3. Sijoita muoto: vedä hiirellä
4. Säädä kokoa: vedä kulmista/reunoista
5. Tallenna muoto: Enter
6. Hylkää muoto: ESC
7. Lisää muokkauksia: napsauta muotoa hiiren kakkospainikkeella

Vinkki: Voit muokata asetuksia pikavalikosta.
        """,
        'form_inserted': "{0} lisätty sivulle {1}",
        'form_deleted': "Muoto poistettu",
        'form_copied': "Muoto kopioitu",
        'form_pasted': "Muoto liitetty",
        'form_saved': "{0} muotoa lisättiin PDF:ään.\n\nPDF ladattiin uudelleen...",
        'form_saved_voice': "{0} muotoa tallennettu",
        'form_reset': "Muoto palautettu oletuskokoon",
        'form_transparent_on': "käytössä",
        'form_transparent_off': "pois käytöstä",
        'form_transparent_toggled': "Läpinäkyvä tausta {0}",
        'form_line_cancel': "Viivan piirto peruttu",
        'form_second_click': "Napsauta nyt loppupistettä muodolle {0}",
        'mode_replace_form': "Lisää muoto",
        'mode_conflict_voice_form': "{0} -tila on aktiivinen. Poistutaanko ja lisätäänkö muoto?",
        'form_settings_updated': "Muotojen asetukset päivitetty",
        'form_unknown': "Muoto",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Napsauta aloituspistettä",
        'form_line_guide_2': "2. Napsauta lopetuspistettä",
        'form_line_guide_3': "Viiva piirretään näiden pisteiden väliin.",
        'form_line_status_1': "Odotetaan ensimmäistä napsautusta...",
        'form_line_status_2': "Ensimmäinen piste asetettu: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Napsauta nyt loppupistettä...",
        'form_line_status_4': "Molemmat pisteet asetettu.\nNapsauta 'Valmis' tallentaaksesi.",
        'form_line_reset': "Nollaa",
        'form_line_finish': "Valmis",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopioi (Cmd+C)",
        'paste': "Liitä (Cmd+V)",
        'copied': "Kopioitu: {0}",
        'no_element_to_copy': "Ei valittua elementtiä kopioitavaksi",
        'no_copied_data': "Kopioituja tietoja ei ole",
        'no_valid_position': "Ei kelvollista paikkaa liittämistä varten",
        'copy_text': "Teksti kopioitu",
        'copy_image': "Kuva kopioitu",
        'copy_form': "Muoto kopioitu",
        'copy_signature': "Allekirjoitus kopioitu",
        'element_text': "Teksti",
        'element_image': "Kuva",
        'element_form': "Muoto",
        'element_signature': "Allekirjoitus",
        'element_unknown': "Elementti",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Tilaristiriita",
        'mode_conflict_message': "Tila '{0}' on jo aktiivinen.\n\nHaluatko poistua siitä ja {1}?",
        'mode_replace': "Poistu tilasta ja {0}",
        'mode_cancel': "Peruuta",
        'mode_replace_text': "lisätä teksti",
        'mode_replace_cross': "lisätä rasti",
        'mode_replace_signature': "lisätä allekirjoitus",
        'mode_replace_image': "lisätä kuva",
        'mode_replace_form': "lisätä muoto",
        'mode_conflict_voice': "{0} -tila on aktiivinen. Poistutaanko ja lisätäänkö teksti?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Tekstinsyöttö",
        'active_mode_signature': "Allekirjoitus",
        'active_mode_image': "Kuva",
        'active_mode_form': "Muoto",
        'active_mode_and': " ja ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Lisää",                    # Hauptmenü
        'insert_another_text': "Lisää teksti",          # Vereinfacht
        'insert_another_cross': "Lisää rasti",        # Vereinfacht
        'insert_another_signature_1': "Allekirjoitus 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Allekirjoitus 2",      # Untermenü-Eintrag
        'insert_another_image': "Lisää kuva",         # Vereinfacht
        'insert_another_form_rect': "Suorakulmio",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellipsi",        # Untermenü-Eintrag
        'insert_another_form_line': "Viiva (2 naps.)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Nuoli (2 naps.)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Tallenna {0}",
        'save_dialog_message': "{0} tallennetaan sivulle {1}.\n\nMiten haluat jatkaa?",
        'save_all': "Tallenna kaikki {0}",
        'save_single': "Tallenna {0}",
        'save_customize': "Mukauta {0}",
        'save_discard': "Hylkää tämä {0}",
        'save_continue': "Jatka muokkausta",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Siirry sivulle {0}",
        'context_rotate': " Kierrä sivu {0}",
        'context_delete': " Poista sivu {0}",
        'context_export': " Vie sivu {0}",
        'context_mark_as': " Merkitse sivu...",
        'context_mark_empty': " Tyhjä sivu",
        'context_unmark_empty': " Ei enää tyhjä",
        'context_mark_export': " Merkitse vietäväksi",
        'context_unmark_export': " Älä vie",
        'context_batch_actions': " Yhteistoiminnot",
        'context_batch_delete_empty': " Poista kaikki {0} tyhjää sivua",
        'context_batch_export_single': " Vie kaikki {0} sivua (yksi tiedosto)",
        'context_batch_export_split': " Vie kaikki {0} sivua (erilliset tiedostot)",
        'context_drag_start': " Aloita vedä ja pudota",
        'context_drag_stop': " Lopeta vedä ja pudota",
        'context_insert': " Lisää",
        'context_insert_pages': " Lisää sivuja",
        'context_zoom': "Zoom",
        'discard_mixed': "Hylkää kaikki {0} {1} ja {2} {3}",
        'save_mixed': "Tallenna {0} {1} ja {2} {3}",
        'discard_texts': "Hylkää kaikki {0} tekstiä",
        'discard_text_single': "Hylkää 1 teksti",
        'save_texts': "Tallenna {0} tekstiä",
        'save_text_single': "Tallenna 1 teksti",
        'discard_crosses': "Hylkää kaikki {0} rastia",
        'discard_cross_single': "Hylkää 1 rasti",
        'save_crosses': "Tallenna {0} rastia",
        'save_cross_single': "Tallenna 1 rasti",
        'discard_signatures': "Hylkää kaikki {0} allekirjoitusta",
        'save_signature_single': "Tallenna 1 allekirjoitus",
        'save_signatures': "Tallenna {0} allekirjoitusta",
        'discard_images': "Hylkää kaikki {0} kuvaa",
        'save_image_single': "Tallenna 1 kuva",
        'save_images': "Tallenna {0} kuvaa",
        'discard_forms': "Hylkää kaikki {0} muotoa",
        'save_form_single': "Tallenna 1 muoto",
        'save_forms': "Tallenna {0} muotoa",
        'cross_discard': "Hylkää tämä rasti",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Vienti- / tuontitiedot",
        'export_what': "📋 Mitä viedään?",
        'export_general': "Yleiset asetukset",
        'export_general_items': "• Puhe (päällä/pois, nopeus)\n• Tumma/vaalea tila\n• Varmuuskopiointiasetukset\n• OCR-asetukset",
        'export_image_form': "Kuva- ja muotoasetukset",
        'export_image_form_items': "• Kuvien asetukset (kuvasuhde, oletuskoko)\n• Muotojen asetukset (viivan paksuus, värit)\n• Allekirjoitusasetukset (polut, koot, aikaleima)",
        'export_passwords': "Salasanatietokanta",
        'export_passwords_items': "• Kaikki tallennetut PDF-salasanat\n• Valinnaisesti salattuna tai salaamattomana",
        'export_master': "Pääsalasana-asetukset",
        'export_master_items': "• Pääsalasanan tiiviste\n• Allekirjoitusten/tekstipalojen asetukset",
        'export_signatures': "Allekirjoitukset ja tekstipalat",
        'export_signatures_items': "• Kaikki kuvatiedostot (allekirjoitukset)\n• Kaikki tekstipalat muotoiluineen\n• Yksityiset/julkiset merkinnät",
        'export_import_warning': "⚠️ Tärkeitä huomautuksia",
        'export_import_note': "• Tuotaessa KAIKKI nykyiset asetukset korvataan\n• Sovellus on käynnistettävä uudelleen\n• Olemassa olevat allekirjoitukset/tekstipalat korvataan",
        'export_master_note': "• Jos pääsalasana on asetettu, voit valita:\n  - Salaamaton (salasanat selväkielisinä)\n  - Salattu (vain pääsalasanalla luettavissa)",
        'export_security': "• Viety ZIP-tiedosto sisältää luottamuksellisia tietoja\n• Säilytä se turvallisesti (esim. salatulla USB-muistitikulla)\n• Jos tiedosto katoaa, salasanoja ei voi palauttaa",
        'export_format': "📁 Vientimuoto",
        'export_format_desc': "Asetukset tallennetaan yhteen ZIP-tiedostoon:",
        'export_filename': "PDFDarkView_Asetukset_YYYYMMDD_HHMMSS.zip",
        'export_success': "Asetukset viety onnistuneesti",
        'export_failed': "Vienti epäonnistui",
        'export_import_question': "Haluatko käynnistää sovelluksen uudelleen nyt?",
        'export_password_question': "Pääsalasana on asetettu.\n\nHaluatko viedä salasanat salaamattomina?\n(muuten ne viedään salattuina)",
        'export_decrypt': "Vie salaamattomana",
        'export_encrypt': "Vie salattuna",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Tiedot",
        'info_title': "Tietoja PDF Dark Viewsta",
        'info_version': "Versio",
        'info_author': "Kehittäjä: Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Tietoja",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> on esteetön PDF-katselija, joka on kehitetty erityisesti näkövammaisille henkilöille.</p>

            <p><strong>Keskeiset ominaisuudet:</strong></p>
            <ul>
                <li>Korkeakontrastinen, muokattava käyttöliittymä</li>
                <li>Täysi näppäimistöohjaus</li>
                <li>Sisäänrakennettu puheentoisto</li>
                <li>OCR skannatuille asiakirjoille</li>
                <li>Laajat muokkaustyökalut</li>
            </ul>

            <p>Yli 50 kieltä tuetaan – jotta PDF-tiedostot ovat kaikkien saatavilla.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Ominaisuudet",
        'info_features_intro': "PDF Dark View tarjoaa sinulle seuraavat mahdollisuudet:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Näyttö ja navigointi</strong> – Tumma/vaalea tila, sivujen selaus, zoomaus, siirry sivulle</li>
            <li><strong>OCR (tekstintunnistus)</strong> – Tee skannatuista asiakirjoista haettavia ja kopioitavia</li>
            <li><strong>Muokkaus</strong> – Tekstin, rastien, allekirjoitusten, kuvien ja muotojen lisääminen</li>
            <li><strong>Sivujen hallinta</strong> – Poistaminen, erottaminen, lisääminen, siirtäminen vetämällä ja pudottamalla</li>
            <li><strong>Vienti</strong> – Wordiin, Pagesiin tai tekstinä</li>
            <li><strong>Tietoturva</strong> – Salasanasuojaus ja -hallinta</li>
            <li><strong>Esteettömyys</strong> – Puheentoisto, näppäimistöohjaus, korkea kontrasti</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Käyttö",
        'info_accessibility': "♿ Esteettömyys – täysi näppäimistöohjaus",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Yleiset</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Avaa PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Hae</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Vaihda tumma/vaalea tila</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Tulosta</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Lopeta</div>

        <div class="shortcut-cat">📖 Navigointi</div>
        <div class="shortcut-row"><kbd>Nuolinäppäimet</kbd> Selaa sivua sivulta</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Siirry sivulle</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Ensimmäinen sivu</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Viimeinen sivu</div>

        <div class="shortcut-cat">✏️ Muokkaus</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Lisää teksti</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Poista sivut</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Erota sivut</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Lisää sivut</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Siirrä sivut</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Kierrä sivua</div>

        <div class="shortcut-cat">🖼️ Elementtien siirtäminen</div>
        <div class="shortcut-row"><kbd>Nuolinäppäimet</kbd> Siirrä teksti/kuva/allekirjoitus</div>
        <div class="shortcut-row"><kbd>Ctrl+Nuolinäppäimet</kbd> Suuremmat askeleet</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Tallenna</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Hylkää</div>

        <div class="shortcut-cat">🗣️ Puheentoisto</div>
        <div class="shortcut-row"><kbd>F2</kbd> Kytke puheentoisto päälle/pois</div>
        """,
        'info_contextmenu': "📌 Tärkeää: Kaikki toiminnot ovat käytettävissä myös pikavalikosta (hiiren oikea painike)!",
        'info_accessibility_hint': "💡 Vinkki: Puheentoisto (F2) helpottaa suuntautumista ja antaa palautetta valikoista ja valintaikkunoista.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lisenssi & Imprint",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUMI</strong><br>
        Tiedot § 5 TMG:n mukaisesti:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Saksa<br>
        Sähköposti: binhdiez64@gmail.com<br>
        Vastuuhenkilö sisällöstä: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Vastuunrajoitus</strong><br>
        Ohjelmisto on kehitetty suurimmalla huolellisuudella. Sen oikeellisuudesta, täydellisyydestä ja toimivuudesta ei anneta takuuta. Käyttö tapahtuu omalla vastuulla.<br><br>

        <strong>📄 MIT-lisenssi (yksityiskäyttö)</strong><br>
        Tekijänoikeus (c) 2026 Toralf Schulz (BinhDiez)<br>
        Sallittu: ilmainen käyttö, yksityiset muutokset, henkilökohtaiset kopiot.<br>
        Ei sallittu: myynti, kaupallinen käyttö, tekijänoikeustietojen poistaminen.<br><br>

        <strong>🔧 Kolmannen osapuolen komponentit</strong><br>
        Tämä ohjelmisto sisältää komponentteja GPL-, AGPL-, Apache 2.0-, BSD- ja MIT-lisenssien alaisuudessa.<br>
        Jaettaessa edelleen on noudatettava kyseisiä lisenssiehtoja.<br><br>

        <strong>🌐 Avoin lähdekoodi</strong><br>
        Lähdekoodi on saatavilla, ja sitä voidaan tarkastella, muokata ja levittää edelleen kyseisten lisenssiehtojen mukaisesti.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Kiitokset",
        'info_credits': "Kiitokset avoimen lähdekoodin yhteisölle",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-käsittely</li>
            <li><strong>PyQt5</strong> – Graafinen käyttöliittymä</li>
            <li><strong>Tesseract OCR</strong> – Tekstintunnistus</li>
            <li><strong>OCRmyPDF</strong> – OCR-integraatio</li>
            <li><strong>python-docx</strong> – Word-vienti</li>
            <li><strong>qtawesome</strong> – Kuvakkeet</li>
            <li><strong>DeepSeek</strong> – Tuki käännöksille (50+ kieltä)</li>
            <li><strong>Kaikki käyttäjät</strong> – Arvokkaasta palautteesta</li>
            <li><strong>Avoimen lähdekoodin yhteisö</strong> – Upeista kirjastoista</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Kielet",
        'info_languages_header': "🌍 Kielituki",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View tukee tällä hetkellä <strong>62 kieltä</strong> – jotta ohjelmistoa voidaan käyttää esteettömästi maailmanlaajuisesti.</p>

            <p><strong>📖 Täydellinen kielilista (tilanne: maaliskuu 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albania (Shqip)</li>
                    <li>🇩🇿 Arabia (العربية)</li>
                    <li>🇮🇩 Bali (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Burma (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnia (Bosanski)</li>
                    <li>🇧🇬 Bulgaria (Български)</li>
                    <li>🇨🇳 Kiina (中文)</li>
                    <li>🇩🇰 Tanska (Dansk)</li>
                    <li>🇩🇪 Saksa (Deutsch)</li>
                    <li>🇬🇧 Englanti (English)</li>
                    <li>🇪🇪 Viro (Eesti)</li>
                    <li>🇫🇮 Suomi (Suomi)</li>
                    <li>🇫🇷 Ranska (Français)</li>
                    <li>🇬🇷 Kreikka (Ελληνικά)</li>
                    <li>🇮🇱 Heprea (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatia (Hrvatski)</li>
                    <li>🇭🇺 Unkari (Magyar)</li>
                    <li>🇮🇩 Indonesia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Iiri (Gaeilge)</li>
                    <li>🇮🇸 Islanti (Íslenska)</li>
                    <li>🇮🇹 Italia (Italiano)</li>
                    <li>🇯🇵 Japani (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korea (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvia (Latviešu)</li>
                    <li>🇱🇹 Liettua (Lietuvių)</li>
                    <li>🇱🇺 Luxemburg (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaiji (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolia (Монгол)</li>
                    <li>🇳🇵 Nepal (नेपाली)</li>
                    <li>🇳🇱 Hollanti (Nederlands)</li>
                    <li>🇳🇴 Norja (Norsk)</li>
                    <li>🇦🇫 Paštu (پښتو)</li>
                    <li>🇮🇷 Persia (فارسی)</li>
                    <li>🇵🇱 Puola (Polski)</li>
                    <li>🇵🇹 Portugali (Português)</li>
                    <li>🇮🇳 Punjab (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Romania (Română)</li>
                    <li>🇷🇺 Venäjä (Русский)</li>
                    <li>🇸🇪 Ruotsi (Svenska)</li>
                    <li>🇷🇸 Serbia (Српски)</li>
                    <li>🇸🇰 Slovakia (Slovenčina)</li>
                    <li>🇸🇮 Slovenia (Slovenščina)</li>
                    <li>🇪🇸 Espanja (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamili (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Tšekki (Čeština)</li>
                    <li>🇹🇷 Turkki (Türkçe)</li>
                    <li>🇺🇦 Ukraina (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnam (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddiš (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Lisää omia kieliä:</strong><br>
                Haluatko kielen, jota ei vielä ole? Aseta oma sanakirjatiedosto (<code>sprache_xx.py</code>) sovelluksen viereen – ohjelmisto tunnistaa sen automaattisesti. Jos olet kiinnostunut tietystä käännöksestä, ota rohkeasti yhteyttä.
            </div>

            <p><strong>🙏 Erityiskiitos:</strong> DeepSeekille kaikkien sanakirjojen kääntämisen tukemisesta 62 kielelle.</p>

            <p>📧 Yhteystiedot käännöksiä varten: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Virhe",
        'error_occurred': "Tapahtui virhe",
        'error_pdf_load': "Virhe ladattaessa PDF:ää",
        'error_pdf_save': "Virhe tallennettaessa PDF:ää",
        'error_ocr': "Virhe tekstintunnistuksessa",
        'error_no_pdf': "PDF:ää ei ole ladattu",
        'error_page_not_found': "Sivua ei löydy",
        'error_invalid_range': "Virheellinen sivualue",
        'error_file_not_found': "Tiedostoa ei löydy",
        'error_permission': "Ei oikeuksia",
        'error_unknown': "Tuntematon virhe",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Onnistui",
        'success_operation': "Toimenpide suoritettu onnistuneesti",
        'success_saved': "Tallennettu onnistuneesti",
        'success_exported': "Viety onnistuneesti",
        'success_imported': "Tuotu onnistuneesti",
        'success_deleted': "Poistettu onnistuneesti",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Vahvistus",
        'confirm_yes': "Kyllä",
        'confirm_no': "Ei",
        'confirm_ok': "OK",
        'confirm_cancel': "Peruuta",
        'confirm_delete': "Poista",
        'confirm_overwrite': "Korvaa",
        'confirm_continue': "Jatka",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Ladataan PDF:ää...",
        'progress_saving': "Tallennetaan PDF:ää...",
        'progress_exporting': "Viedään PDF:ää...",
        'progress_processing': "Käsitellään...",
        'progress_wait': "Odota...",
        'progress_preparing': "Valmistellaan...",
        'progress_finalizing': "Viimeistellään...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Valkoinen",
        'color_black': "Musta",
        'color_red': "Punainen",
        'color_green': "Vihreä",
        'color_blue': "Sininen",
        'color_yellow': "Keltainen",
        'color_magenta': "Magenta",
        'color_cyan': "Syaani",
        'color_orange': "Oranssi",
        'color_gray': "Harmaa",
        'color_custom': "Värivalinta",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Tiedosto",
        'menu_edit': "&Muokkaa",
        'menu_view': "&Näkymä",
        'menu_tools': "&Työkalut",
        'menu_settings': "&Asetukset",
        'menu_help': "&Ohje",
        'menu_language': "🌐 Kieli",
        'menu_guides': "&Ohjeet",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Avaa",
        'file_save_as': "&Tallenna nimellä...",
        'file_protect': "&Suojaa dokumentti...",
        'file_export': "&Vie",
        'file_export_pages': "Vie Pagesiin",
        'file_export_word': "Vie DOCX-muotoon",
        'file_export_text': "Vie TXT-muotoon",
        'file_print_now': "&Tulosta heti",
        'file_print': "&Tulosta",
        'file_close': "&Sulje",
        'file_quit': "&Lopeta",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Etsi",
        'edit_ocr': " Suorita OCR",
        'edit_rotate': "&Kierrä sivua",
        'edit_rotate_all': "Kierrä &kaikkia sivuja",
        'edit_delete_pages': "&Poista sivuja",
        'edit_extract_pages': "&Poimi sivuja",
        'edit_insert_pages': "&Lisää sivuja",
        'edit_move_pages': "&Siirrä sivuja",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Lisää tekstiä ja rasteja",
        'text_insert': " Lisää teksti",
        'cross_insert': " Lisää rasti",
        'text_customize': " Mukauta tekstiä",
        'cross_customize': " Mukauta tätä rastia",
        'cross_customize_all': " Mukauta kaikkia rasteja",
        'text_discard': " Hylkää tämä teksti/rasti",
        'text_discard_all': " Hylkää kaikki tekstit ja rastit",
        'text_save_all': " Tallenna kaikki tekstit ja rastit",
        'text_guide': " Tekstinsyöttö / tekstipalat - ohje",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Lisää allekirjoitus",
        'signature_settings_menu': " Asetukset...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Lisää kuva",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Lisää muotoja",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Näytä teksti-ikkuna",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Sivun leveys (oletus)",
        'view_zoom_two': "&Kaksi sivua",
        'view_zoom_overview': "&Yleiskuva (useita sivuja)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Käyttöapu",
        'settings_voice': "Puhe",
        'settings_voice_tooltip': "täydentää ruudunlukijan puhetta lisätiedoilla",
        'settings_signature': "&Allekirjoitusasetukset",
        'settings_password': "&Salasanahallinta",
        'settings_backup': "Luo varmuuskopio ennen muutoksia",
        'settings_export_import': "&Vie asetukset / tuo asetukset",
        'settings_export': "&Vie kaikki asetukset...",
        'settings_import': "&Tuo kaikki asetukset...",
        'settings_export_info': "&Mitä viedään?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "päällä",
        'voice_off': "pois",
        'voice_toggle': "Puhe {0}",
        'voice_speed': "Nopeus {0} prosenttia",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Työkalua ei löydy:\n{0}\n\nBASE_DIR: {1}\nVarmista, että PDF-työkalut on asennettu hakemistoon {1}.",
        'tool_started': "{0} käynnistetty",
        'tool_start_failed': "Käynnistys epäonnistui",
        'process_error_failed_to_start': "Prosessia ei voitu käynnistää. Onko tiedosto olemassa?",
        'process_error_crashed': "Prosessi kaatui käynnistyksen aikana.",
        'process_error_timeout': "Prosessin aikakatkaisu saavutettu.",
        'process_error_write': "Kirjoitusvirhe prosessissa.",
        'process_error_read': "Lukuvirhe prosessissa.",
        'process_error_unknown': "Tuntematon prosessivirhe",
        'process_command': "Komento",
        'process_normal_exit': "päättyi normaalisti",
        'process_crashed': "kaatui",
        'process_nonzero_exit': "{0} päättyi virhekoodilla {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Peruutetaan...",
        'move_cancelling': "Siirtoa peruutetaan",
        'opening_pdf': "Avataan PDF:ää...",
        'loading_document': "Ladataan dokumenttia...",
        'pdf_opened': "PDF avattu",
        'pages_found_moving': "{0} sivua löytyi, {1} siirrettävää",
        'creating_backup': "Luodaan varmuuskopiota...",
        'backup_description': "Varmuuskopioidaan alkuperäistä tiedostoa...",
        'backup_saved_as': "Varmuuskopioitu nimellä: {0}",
        'error_format': "Virhe: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Haku nollattu",
        'page_header_simple': "=== Sivu {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Salasanahallinta – Ohje",
        'password_guide_voice': "Ohje salasanahallintaan. Lue ohjeet huolellisesti.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Salasanahallinta – Yksityiskohtainen ohje</strong></p>

        <p><strong>1. PDF-tiedostojen salasanasuojaus</strong></p>
        <ul>
        <li>Kun avaat salasanalla suojatun PDF:n, näkyviin tulee ikkuna, johon voit syöttää salasanan.</li>
        <li>Voit tallentaa salasanan salattuna, jotta sinun ei tarvitse syöttää sitä joka kerta uudelleen (valintaruutu "Tallenna salasana").</li>
        <li>Painikkeella "Poista salasana" voit luoda salauksen puretun kopion PDF:stä ja poistaa salasanan tietokannasta.</li>
        </ul>

        <p><strong>2. Pääsalasana</strong></p>
        <ul>
        <li>Pääsalasana suojaa pääsyn kaikkiin tallennettuihin PDF-salasanoihin.</li>
        <li><strong>Asettaminen:</strong> Siirry kohtaan "Asetukset → Salasanahallinta → Pääsalasana-asetukset" ja napsauta "Aseta pääsalasana". Valitse vahva salasana (vähintään 8 merkkiä).</li>
        <li><strong>Vaihtaminen:</strong> Onnistuneen todennuksen jälkeen voit vaihtaa pääsalasanan.</li>
        <li><strong>Poistaminen:</strong> Jos poistat pääsalasanan, KAIKKI tallennetut salasanat poistetaan pysyvästi. Voit viedä varmuuskopion ennen poistoa.</li>
        <li>Kerran istunnossa sinun on todennettava itsesi pääsalasanalla päästäksesi suojattuihin toimintoihin (esim. salasanojen näyttäminen).</li>
        </ul>

        <p><strong>3. Salasanahallinta (luettelo)</strong></p>
        <ul>
        <li>Kohdassa "Asetukset → Salasanahallinta" avautuu taulukko kaikista tallennetuista PDF-tiedostoista ja niiden salatuista salasanoista.</li>
        <li><strong>Ilman pääsalasanaa:</strong> Voit vain poistaa merkintöjä – salasanat pysyvät piilossa.</li>
        <li><strong>Pääsalasanalla (todennettu):</strong> Voit näyttää, kopioida, viedä ja poistaa salasanoja.</li>
        <li><strong>Vienti:</strong> Valitse muoto (JSON, CSV, TXT) ja tallenna luettelo. Jos pääsalasana on asetettu, voit päättää, viedäänkö salasanat selväkielisinä vai salattuina.</li>
        <li><strong>Tuonti:</strong> Aiemmin viety ZIP-tiedosto (kaikki asetukset mukaan lukien salasanat) voidaan lukea takaisin kohdasta "Asetukset → Vie asetukset / tuo asetukset". Huom: Nykyiset tiedot korvataan!</li>
        </ul>

        <p><strong>4. Salasanageneraattori</strong></p>
        <ul>
        <li>Salasanavalintaikkunassa (esim. suojattaessa PDF:ää) on syöttökentän oikealla puolella noppapainike 🎲.</li>
        <li>Napsauta sitä avataksesi salasanageneraattorin. Voit säätää pituutta, merkistöä (isot kirjaimet, pienet kirjaimet, numerot, erikoismerkit) ja erotinmerkkejä luettavuuden parantamiseksi.</li>
        <li>Luotu salasana voidaan ottaa suoraan käyttöön ja tarvittaessa kopioida.</li>
        </ul>

        <p><strong>5. Tärkeitä turvallisuusohjeita</strong></p>
        <ul>
        <li>Tallennetut salasanat säilytetään AES-256 -salattuna. Avain johdetaan pääsalasanastasi (jos asetettu) tai kiinteästä arvosta (ilman pääsalasanaa).</li>
        <li>Ilman pääsalasanaa salasanat ovat kyllä salattuja, mutta avain on tallennettu ohjelmaan – hyökkääjä, jolla on pääsy tiedostoihisi, voisi purkaa ne. Siksi suosittelemme vahvasti pääsalasanan käyttöä.</li>
        <li>Salasanatietokanta sijaitsee hakemistossa `Data/passwords.json`. Tee säännöllisesti varmuuskopioita, erityisesti ennen pääsalasanan poistamista.</li>
        <li>Jos unohdat pääsalasanan, kaikki tallennetut salasanat ovat pysyvästi menetettyjä.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Käänteistila",
        'invert_mode_classic': "Klassinen (käännä kaikki värit)",
        'invert_mode_smart': "Älykäs (käännä vain kirkkaus)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Harmaasävyn kynnysarvo",
        'gray_threshold_10': "10% (tiukka)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Oletus)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (pehmeä)",
        'threshold_changed': "Kynnysarvoksi asetettu {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Harmaasävyn kynnysarvo – Selitys",
        'threshold_guide_text': "Harmaasävyn kynnysarvo määrittää, mitkä pikselit älykkäässä tummassa tilassa katsotaan 'harmaiiksi' ja käännetään.\n\n"
                                "• Alhainen arvo (10%) kääntää vain lähes täydelliset harmaasävyt – värilliset elementit säilyvät täysin.\n"
                                "• Korkea arvo (50%) kääntää myös hieman värisiä pikseleitä – tämä lisää kontrastia, mutta voi vääristää värejä.\n\n"
                                "Optimaalinen arvo riippuu asiakirjasta. Puhtaasti tekstiasiakirjoille 30–40% on usein ihanteellinen, värillisille grafiikoille mieluummin 10–20%.\n\n"
                                "Voit säätää arvoa milloin tahansa 'Asetukset'-valikon kautta – PDF ladataan uudelleen välittömästi.\n\n"
                                "Huomioi:\n* Valokuvat ja kuvat voidaan näyttää oikein vain vaaleassa tilassa!\n* Käänteisasetukset näytetään vain, kun tumma tila on aktivoitu.",
        'threshold_guide_voice': "Harmaasävyn kynnysarvo määrittää, kuinka voimakkaasti älykäs tumma tila puuttuu. Alhainen arvo säästää värejä, korkea arvo lisää kontrastia.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Avataan PDF-tiedostoa...",
        'progress_loading_document': "Ladataan asiakirjaa...",
        'progress_pdf_opened': "PDF avattu",
        'progress_creating_backup': "Luodaan varmuuskopiota...",
        'progress_backup_description': "Varmistetaan alkuperäinen tiedosto...",
        'progress_backup_created': "Varmuuskopio luotu",
        'progress_backup_saved_as': "Tallennettu nimellä: {0}",
        'progress_analyzing_start': "Aloitetaan analyysi...",
        'progress_searching_empty': "Etsitään tyhjiä sivuja...",
        'progress_page_empty': "Sivu {0} on tyhjä",
        'progress_page_keep': "Säilytä sivu {0}",
        'progress_analysis_complete': "Analyysi valmis",
        'progress_empty_found': "Löytyi {0} tyhjää sivua",
        'progress_current_page': "Nykyinen sivu",
        'progress_mark_delete': "Merkitään poistettavaksi",
        'progress_range_selected': "Sivualue {0}-{1}",
        'progress_deleting_pages': "Poistetaan {0} sivua",
        'progress_creating_new_pdf': "Luodaan uutta PDF-tiedostoa...",
        'progress_transferring_pages': "Siirretään sivuja",
        'progress_keeping_page': "Sivu {0} säilytetään ({1}/{2})",
        'progress_saving_pdf': "Tallennetaan PDF-tiedostoa...",
        'progress_optimizing': "Optimoidaan tiedostokokoa...",
        'progress_finalizing': "Viimeistellään...",
        'progress_new_size': "Uusi koko: {0:.2f} MB",
        'progress_cancelling': "Perutaan...",
        'progress_cancel_message': "{0} perutaan",
        'progress_pages_found_moving': "Löytyi {0} sivua, {1} siirrettäväksi",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analysoidaan PDF-tiedostoa...",
        'ocr_status_optimizing': "Kuvan optimointi käynnissä...",
        'ocr_status_recognizing': "Tekstintunnistus käynnissä...",
        'ocr_status_embedding': "Upotetaan tekstiä...",
        'ocr_status_finalizing': "Viimeistellään PDF-tiedostoa...",

        # PDF-Laden
        'progress_preparing': "Valmistellaan...",
        'progress_loading': "Ladataan PDF-tiedostoa...",

        # Seitenoperationen
        'progress_deleting_title': "Poistetaan sivuja...",
        'progress_moving_title': "Siirretään sivuja...",
        'pages_found': "Sivuja löytyi",
        'progress_creating_new_order': "Luodaan uutta järjestystä...",
        'progress_sorting_pages': "Lajitellaan sivuja...",
        'progress_moving_to_begin': "Siirretään {0} sivua alkuun",
        'progress_transferring_count': "Siirretään {0} sivua",
        'progress_transferring_before_target': "Siirretään sivut ennen kohdetta",
        'progress_moving_pages': "Siirretään {0} sivua",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_varmuuskopio_",
        'filename_protected_suffix': "_suojattu_",
        'filename_copy_suffix': "_Kopio",
        'filename_page_single': "_Sivu_",
        'filename_page_range': "_Sivut_",
        'filename_export_page': "_Sivu_{0:03}",
        'filename_export_range': "_Sivut_{0}-{1}",
        'filename_export_multiple': "_Sivut_{0}",
        'filename_with_text': "_tekstillä",
        'filename_with_signature': "_allekirjoituksella",
        'filename_with_image': "_kuvalla",
        'filename_with_forms': "_muodoilla",
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
        'view_toggle_navbar': "Näytä painikepalkki",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Kaikkia sivuja ei voi poistaa",
		'pages_cannot_delete_last_page': 'Viimeistä sivua ei voi poistaa!',
		'pages_cannot_delete_all_pages': 'Asiakirjassa on oltava vähintään yksi sivu!',
		'delete_pages_confirm': 'Haluatko varmasti poistaa {0} sivua?',
		'delete_pages_confirm_voice': 'Haluatko varmasti poistaa {0} sivua?',
		'pages_deleted': '{0} sivua poistettiin onnistuneesti.',
		'warning': 'Varoitus',
		'error': 'Virhe',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Lomaketta ei valittu",
        'form_customized': "Lomake muokattu",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Valitse",
        'btn_use': "Käytä",
        'master_password_for_spasswords': "Salasanojen tallentamiseksi ja käyttämiseksi on ensin määritettävä pääsalasana.\n\nHaluatko määrittää pääsalasanan nyt?",
        'open_saved_dialog_title': "Avaa tallennettu tiedosto",
        'open_saved_question': "Haluatko avata tallennetun tiedoston nyt?",
        'password': "Salasana",
        'password_manager_master_required': "Salasanahallinta on käytettävissä vain, jos pääsalasana on määritetty.\n\nHaluatko määrittää pääsalasanan nyt?",
        'password_master_required_for_select': "Nähdäksesi ja valitaksesi tallennetut salasanat, sinun on ensin todennettava pääsalasanallasi.\n\nHaluatko todentaa nyt?",
        'password_not_available': "Valittu salasana ei ole käytettävissä tai sitä ei voitu purkaa.",
        'password_options_title': "Salasanan asetukset",
        'password_save_choice_change': "Aseta uusi salasana",
        'password_save_choice_keep': "Käytä olemassa olevaa salasanaa",
        'password_save_choice_none': "Tallenna salaamattomana",
        'password_save_hint': "Määritä ensin pääsalasana tallentaaksesi salasanat turvallisesti.",
        'password_save_master_required': "Tallenna salasana (vain pääsalasanalla mahdollista)",
        'password_save_question': "Nykyinen PDF on suojattu salasanalla. Haluatko käyttää olemassa olevaa salasanaa, asettaa uuden vai tallentaa salaamattomana?",
        'password_select': "Valitse salasana",
        'password_select_none': "Salasanaa ei ole valittu.\n\nValitse salasana luettelosta.",
        'password_select_one': "Valitse tarkalleen yksi salasana.\n\nOlet merkinnyt useita salasanoja.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_varmuuskopio",
        'filename_insert_suffix': "_lisäyksellä",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_sivut_poistettu",
        'filename_pages_moved': "_sivut_siirretty",
        'filename_rotated_all_suffix': "_kaikki_sivut_käännetty",
        'filename_rotated_suffix': "_sivu_käännetty",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Tiedostonimien määritys PDF-muutoksissa",
        'filename_keep_suffixes': "Säilytä aiemmat jälkiliitteet (esim. _tekstillä)",
        'filename_keep_suffixes_false': "Korvaa",
        'filename_keep_suffixes_true': "Säilytä",
        'filename_preview_label': "Tiedostonimen esikatselu:",
        'filename_preview_overwrite_hint': "Esikatselu ei ole käytettävissä – alkuperäinen tiedosto ylikirjoitetaan.",
        'filename_separator': "Sanojen erotin",
        'filename_separator_none': "Ei erotinta",
        'filename_separator_space': "Välilyönti ( )",
        'filename_separator_underscore': "Alaviiva (_)",
        'filename_settings_saved': "Tiedostonimen asetukset tallennettu",
        'filename_settings_title': "Tiedostonimen muotoilu ja varmuuskopiointi",
        'filename_timestamp_position': "Aikaleiman sijainti",
        'filename_timestamp_position_after': "Perusnimen jälkeen",
        'filename_timestamp_position_before': "Aivan edessä",
        'filename_timestamp_position_end': "Lopussa",
        'filename_use_timestamp': "Käytä aikaleimaa",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Käyttäytyminen muutoksissa:</b><ul><li>Sivujen poistaminen ja lisääminen</li><li>Tekstin, allekirjoituksen, kuvan ja muotojen lisääminen</li><li>OCR</li></ul></html>",
        'backup_section': "Varmuuskopio sivuoperaatioille (Poista, Siirrä)",
        'behavior_info': "Huomautus: 'Ylikirjoita alkuperäinen' -tilassa aikaleimat ja jälkiliitteet ohitetaan – tiedosto säilyttää nimensä.",
        'behavior_new_file': "Luo aina uusi tiedosto (aikaleimalla ja jälkiliitteellä)",
        'behavior_overwrite': "Ylikirjoita alkuperäinen (ei uutta tiedostoa)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Kaikki sivut käännettiin.\n\nAlkuperäinen pysyi muuttumattomana.\nUusi tiedosto: {0}",
        'all_pages_rotated_voice': "Kaikki sivut käännettiin, uusi tiedosto luotu.",
        'empty_pages_deleted_new_file': "{0} tyhjää sivua poistettiin.\n\nAlkuperäinen pysyi muuttumattomana.\nUusi tiedosto: {1}",
        'empty_pages_deleted_voice': "{0} tyhjää sivua poistettiin, uusi tiedosto luotu.",
        'ocr_keep_original': "Säilytä alkuperäinen (avaa myöhemmin manuaalisesti)",
        'ocr_new_file_question': "Uusi haettava PDF tallennettiin osoitteeseen:\n{0}\n\nHaluatko avata sen nyt?",
        'ocr_open_new': "Avaa uusi OCR-tiedosto",
        'ocr_original_kept': "Alkuperäinen tiedosto pysyy auki. OCR-tiedosto on tallennettu.",
        'page_deleted_new_file': "Sivu {0} poistettiin.\n\nAlkuperäinen pysyi muuttumattomana.\nUusi tiedosto: {1}",
        'page_deleted_voice': "Sivu {0} poistettiin, uusi tiedosto luotu.",
        'page_rotated_new_file': "Sivu {0} käännettiin.\n\nAlkuperäinen pysyi muuttumattomana.\nUusi tiedosto: {1}",
        'page_rotated_voice': "Sivu {0} käännettiin, uusi tiedosto luotu.",
        'pages_deleted_new_file': "{0} sivua poistettiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto: {1}",
        'pages_deleted_new_file_voice': "{0} sivua poistettiin, uusi tiedosto luotu.",
        'pages_inserted_new_file': "{0} sivua lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto: {1}",
        'pages_inserted_new_file_ask': "{0} sivua lisättiin.\n\nAlkuperäinen pysyi muuttumattomana.\nUusi tiedosto: {1}\n\nHaluatko avata sen nyt?",
        'pages_inserted_voice_new': "{0} sivua lisättiin, uusi tiedosto luotu.",
        'pages_moved_new_file': "{0} sivua siirrettiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto: {1}",
        'pages_moved_new_file_voice': "{0} sivua siirrettiin, uusi tiedosto luotu.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Älä näytä enää",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Varmuuskopiointiasetus</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Varmuuskopiointi PÄÄLLÄ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Kaikissa muutoksissa, jotka ylikirjoittavat alkuperäisen</strong> (teksti, allekirjoitus, kuva, muoto, OCR, kääntäminen, lisäys, sivujen poisto/siirto) luodaan <strong>automaattisesti aikaleimalla varustettu varmuuskopio</strong> ennen muutoksen soveltamista.</p>
                <p style="margin: 5px 0 5px 20px;">• Varmuuskopio sijaitsee alkuperäisen tiedoston vieressä (esim. <code>Dokumentti_varmuuskopio_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Jos olet lisäksi aktivoinut asetuksen <strong>„Ylikirjoita alkuperäinen“</strong>, myös silloin luodaan varmuuskopio.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Varmuuskopiointi POIS PÄÄLTÄ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Varmuuskopiota ei luoda</strong> – ei ylikirjoitettaessa eikä sivuoperaatioiden yhteydessä.</p>
                <p style="margin: 5px 0 5px 20px;">• Alkuperäinen tiedosto voi ylikirjoitettaessa kadota peruuttamattomasti.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Suositellaan vain kokeneille käyttäjille!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Vinkki:</strong> Varmuuskopiointiasetus on riippumaton asetuksesta „Ylikirjoita alkuperäinen“. Voit yhdistää molemmat.<br>
                Voit piilottaa tämän viestin pysyvästi.
            </div>
        </div>
        """,
        'backup_info_title': "Varmuuskopioinnin toiminta",
        'backup_info_voice': "Ilmoitus varmuuskopioinnin toiminnasta sivuoperaatioiden yhteydessä. Varmuuskopiointi päällä ylikirjoittaa alkuperäisen, varmuuskopiointi pois päältä luo uuden tiedoston.",
        'show_backup_info': "Tietoa varmuuskopiointiasetuksesta",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Älä näytä enää",
        'overwrite_enable_backup': "Ota varmuuskopiointi käyttöön (suositeltavaa)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Ylikirjoita alkuperäinen</p>
            <p>Jos otat tämän asetuksen käyttöön, muutokset (teksti, allekirjoitus, kuva, muoto, OCR, kääntäminen, lisäys) tallennetaan <strong>suoraan alkuperäiseen</strong> – <strong>uutta tiedostoa ei luoda</strong>.</p>
            <p>• Tiedostonimi pysyy muuttumattomana.<br>
            • Aikaleimat ja jälkiliitteet ohitetaan.<br>
            • <strong>Ilman varmuuskopiota alkuperäinen voi kadota peruuttamattomasti.</strong></p>
            <p style="color: #FFD700;">Suositus: Ota lisäksi käyttöön varmuuskopiointi automaattisten varmuuskopioiden saamiseksi.</p>
        </div>
        """,
        'overwrite_info_title': "Ylikirjoita alkuperäinen",
        'overwrite_info_voice': "Varoitus: Ylikirjoita alkuperäinen – ei uutta tiedostoa. Varmuuskopiointi suositeltavaa.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} sivua lisättiin.\n\nAlkuperäinen tiedosto ylikirjoitettiin.\nVarmuuskopio luotiin.",
        'pages_inserted_overwrite_no_backup': "{0} sivua lisättiin.\n\nAlkuperäinen tiedosto ylikirjoitettiin.\nVarmuuskopiota EI luotu.",
        'texts_saved_overwrite_with_backup': "Muutokset tallennettiin alkuperäiseen.\n\nVarmuuskopio luotiin.",
        'texts_saved_overwrite_no_backup': "Muutokset tallennettiin alkuperäiseen.\n\nVarmuuskopiota EI luotu.",
        'texts_crosses_saved_new_file': "{0} {1} ja {2} {3} lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto luotiin.\n\nUutta PDF:ää ladataan...",
        'texts_saved_new_file': "{0} {1} lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto luotiin.\n\nUutta PDF:ää ladataan...",
        'crosses_saved_new_file': "{0} {1} lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto luotiin.\n\nUutta PDF:ää ladataan...",
        'elements_saved_new_file': "{0} elementtiä lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto luotiin.\n\nUutta PDF:ää ladataan...",
        'signatures_saved_overwrite_with_backup': "Allekirjoitus(t) tallennettiin alkuperäiseen.\n\nVarmuuskopio luotiin.",
        'signatures_saved_overwrite_no_backup': "Allekirjoitus(t) tallennettiin alkuperäiseen.\n\nVarmuuskopiota EI luotu.",
        'images_saved_overwrite_with_backup': "Kuva(t) tallennettiin alkuperäiseen.\n\nVarmuuskopio luotiin.",
        'images_saved_overwrite_no_backup': "Kuva(t) tallennettiin alkuperäiseen.\n\nVarmuuskopiota EI luotu.",
        'forms_saved_overwrite_with_backup': "Muoto(t) tallennettiin alkuperäiseen.\n\nVarmuuskopio luotiin.",
        'forms_saved_overwrite_no_backup': "Muoto(t) tallennettiin alkuperäiseen.\n\nVarmuuskopiota EI luotu.",
        'signatures_saved_new_file': "{0} allekirjoitusta lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto luotiin.\n\nUutta PDF:ää ladataan...",
        'images_saved_new_file': "{0} kuvaa lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto luotiin.\n\nUutta PDF:ää ladataan...",
        'forms_saved_new_file': "{0} muotoa lisättiin.\n\nAlkuperäinen tiedosto pysyi muuttumattomana.\nUusi tiedosto luotiin.\n\nUutta PDF:ää ladataan...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Varoitus: Tämä PDF sisältää käännettyjä sivuja. Sijoittelu voi poiketa.",
        'page_rotated_warning_title': "Käännetty sivu havaittu",
        'page_rotated_warning_message': "Nykyinen sivu {0} on käännetty {1}°.\n\nElementtien lisääminen käännetyille sivuille ei ole tuettua.\n\nHaluatko kääntää sivun nyt pystyasentoon?",
        'page_rotated_warning_voice': "Varoitus: Sivu on käännetty. Käännä se ensin.",
        'paste_on_rotated_page_simple_warning': "Lisääminen sivulle {0} ei ole mahdollista!\n\nTämä sivu on käännetty {1}°.\n\nKäännä sivu ensin 0°:een (Valikko: Muokkaa → Kohdista sivu).\n\nVaroitus:\nAiemmin kopioitu elementti menetetään, ellet tallenna ennen sivun kääntämistä.",
        'paste_on_rotated_page_voice': "Lisääminen peruutettu. Sivu on käännetty. Kohdista sivu ensin.",
        'page_rotated_cancel': "Peruuta",
        'page_rotated_rotate_until_upright': "Käännä sivua toistuvasti (kunnes pystyasennossa)",
        'page_rotated_now_upright': "Sivu on nyt pystyasennossa. Voit nyt lisätä.",
        'page_rotated_still_not_upright': "Sivua ei voitu kääntää pystyasentoon. Korjaa manuaalisesti.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Ohje: Käännettyjen sivujen korjaaminen",
        'help_rotated_pages_voice': "Ohje käännettyjen sivujen korjaamiseen avautuu.",
        'btn_help': "Ohje",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Ongelma: Käännetty sivu – Lisääminen ei toimi oikein</p>

            <p>Jos tekstien, allekirjoitusten tai muotojen lisääminen käännetylle sivulle ei toimi oikein, voit korjata sivun ulkoisella PDF-muokkaimella.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Ratkaisu ulkoisella työkalulla (esim. macOS Esikatselu)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Vie sivu</strong><br>
                &nbsp;&nbsp;Napsauta valikossa <strong>Tiedosto → Vie sivuina</strong> tai käytä muuta menetelmää tallentaaksesi halutun sivun yksittäisenä PDF:nä.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Avaa sivu ulkoisessa ohjelmassa</strong><br>
                &nbsp;&nbsp;Avaa viety PDF PDF-muokkaimessa (esim. <strong>macOS Esikatselu</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Käännä sivu</strong><br>
                &nbsp;&nbsp;Käännä sivu niin, että se on pystyasennossa (Esikatselussa: <strong>Työkalut → Käännä</strong> tai <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Tallenna</strong><br>
                &nbsp;&nbsp;Tallenna korjattu sivu (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Lisää sivu takaisin alkuperäiseen asiakirjaan</strong><br>
                &nbsp;&nbsp;Palaa PDFDarkViewiin ja lisää korjattu sivu haluttuun kohtaan:<br>
                &nbsp;&nbsp;<strong>Muokkaa → Lisää sivuja</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Vaihtoehto: Käännä sivu alkuperäisessä</p>
                <p style="margin: 5px 0 5px 20px;">• Käytä sisäänrakennettua kääntötoimintoa (<strong>Muokkaa → Käännä sivu</strong>) korjataksesi sivun vaiheittain.<br>
                • Jokaisen käännön jälkeen voit tarkistaa, toimiiko lisääminen nyt.<br>
                • Tämä on usein nopeampi ratkaisu – kokeile sitä ensin!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Vinkki:</strong> Jos kohtaat usein käännettyjä sivuja, voit piilottaa varoituksen lisäysvalintaikkunassa pysyvästi.<br>
                Sijoittelu voi silloin poiketa – käytä tätä asetusta vain, jos tunnet seuraukset.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Kohdista sivut",
        'menu_rotate_normalize_tooltip': "Käännä sivu tai palauta 0°:een",
        'normalize_current_page': "Tuo nykyinen sivu pystyasentoon (aseta 0°:een)",
        'normalize_all_pages': "Tuo kaikki sivut pystyasentoon (aseta 0°:een)",
        'page_normalized': "Sivu {0} asetettiin pystyasentoon.",
        'all_pages_normalized': "Kaikki sivut asetettiin pystyasentoon.",
        'page_already_upright': "Sivu {0} on jo pystyasennossa.",
        'all_pages_already_upright': "Kaikki sivut ovat jo pystyasennossa.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF ei sisällä haettavaa tekstiä.</p><p>Haluatko tehdä OCR:n viedäksesi {0}:ään?</p>",
        'export_ocr_voice': "PDF ei sisällä tekstiä. OCR vaaditaan vientiin {0}:ään.",
        'export_no_ocr_possible': "Vienti ilman OCR:ää ei ole mahdollista. Tee OCR valikon kautta.",
        'ocr_failed_export_not_possible': "OCR epäonnistui. Vientiä ei voida suorittaa.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF avautuu Esikatselussa. Käynnistä tulostusprosessi siellä.",
        'print_preview_manual': "PDF avattiin. Suorita tulostuskomento manuaalisesti (esim. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Yhdistä PDF-tiedostot",
        'merge_pdfs': "Yhdistä PDF-tiedostot",
        'merge_progress_title': "Yhdistetään PDF-tiedostoja...",
        'merge_pdfs_list': "PDF-tiedostot järjestyksessä (Järjestä raahaamalla)",
        'merge_add_pdf': "Lisää PDF",
        'merge_remove': "Poista",
        'merge_move_up': "Ylös",
        'merge_move_down': "Alas",
        'merge_pdfs_info': "💡 Vinkki: Voit muuttaa järjestystä raahaamalla",
        'merge_no_pdfs': "Yhtään PDF-tiedostoa ei ole valittu. Napsauta 'Lisää PDF'.",
        'merge_info': "{0} PDF-tiedostoa valittu (noin {1} sivua)",
        'merge_open_file': "Avaa tiedosto",
        'merge_merge': "Yhdistä",
        'merge_error': "Virhe yhdistettäessä",
        'merge_min_two_pdfs_error': "Valitse vähintään kaksi PDF-tiedostoa yhdistettäväksi.",
        'merge_select_pdfs': "Valitse PDF-tiedostot yhdistettäväksi",
        'merge_error_file': "Virhe käsiteltäessä",
        'merge_cancelled': "Yhdistäminen peruutettiin",
        'merge_preparing': "Valmistellaan...",
        'merge_processing': "Käsitellään PDF {0}/{1}",
        'merge_saving': "Tallennetaan yhdistettyä PDF:ää...",
        'merge_complete': "Valmis!",
        'merge_success_title': "Yhdistäminen onnistui",
        'merge_success_voice': "{0} PDF-tiedostoa yhdistettiin onnistuneesti.",
        'merge_success_message': "{0} PDF-tiedostoa yhdistettiin onnistuneesti.\n\nUusi asiakirja sisältää nyt {1} sivua.\n\nUusi tiedosto:\n{2}\n\nTallennussijainti:\n{3}\n{2}\n\nHaluatko avata tämän PDF:n?",
        'replace_file_title': "Korvataanko tiedosto?",
        'replace_file_message': "PDF on jo auki. Haluatko korvata sen uudella tiedostolla?",
        'btn_yes': "Kyllä",
        'btn_no': "Ei",
        'filename_merge_suffix': "yhdistetty",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Avataan {0}...",
        'progress_merge_reading': "Luetaan {0}...",
        'progress_merge_adding': "Lisätään {0} sivua...",
        'progress_merge_optimizing': "Optimoidaan PDF:ää...",
        'progress_merge_writing': "Kirjoitetaan PDF:ää...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF:n sulkemista",
        'action_close_window': "ikkunan sulkemista",
        'action_open_new_pdf': "uuden PDF:n avaamista",
        'action_quit_app': "sovelluksesta poistumista",
        'changes_saved': "Muutokset tallennettiin.",
        'file_close_title': "Sulje PDF-tiedosto",
        'save_before_action': "Pitääkö muutokset tallentaa ennen {0}? Kyllä vai Ei?",
        'save_before_action_voice': "Pitääkö muutokset tallentaa ennen {0}? Kyllä vai Ei?",
        'save_before_close_question': "Pitääkö muutokset tallentaa ennen sulkemista? Kyllä vai Ei?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Haettava PDF luotu:\n\n{0}\n\n<b>yritä uudelleen tarvittaessa",
        "ocr_rotate_title": "Tasoita sivut ennen OCR:ää",
        "ocr_rotate_question": "PDF sisältää käännettyjä sivuja.\nHaluatko tasoittaa kaikki sivut 0°:een ennen OCR:ää?\nTämä parantaa tekstintunnistusta merkittävästi.",
        "ocr_rotate_yes": "Kyllä, tasoita",
        "ocr_rotate_no": "Ei, käynnistä OCR suoraan",
        "ocr_rotate_voice": "PDF sisältää käännettyjä sivuja. Pitäisikö kaikki sivut tasoittaa ennen OCR:ää?",
        "ocr_not_performed_message": "Tekstiä ei ole. Suorita OCR (valikko \"Muokkaa\" → \"Suorita OCR\" tai näppäin Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-asetukset",
        "ocr_language_btn": "Valitse OCR-kieli",
        "ocr_language": "OCR-kieli(et)",
        "ocr_language_current": "Nykyinen kieli:",
        "ocr_param_info": "Tietoa parametrista",

        "ocr_force_ocr_label": "Pakota OCR",
        "ocr_deskew_label": "Korjaa vino",
        "ocr_clean_label": "Puhdista kuva",
        "ocr_oversample_label": "Resoluutio (DPI)",
        "ocr_pagesegmode_label": "Sivun segmentointi",
        "ocr_oem_label": "OCR-moottorin tila",
        "ocr_optimize_label": "PDF-pakkaus",
        "ocr_jobs_label": "Rinnakkaisprosessit",
        "ocr_verbose_label": "Lokin yksityiskohtaisuus",

        "ocr_force_ocr_tooltip": "Pakota OCR jokaiselle sivulle, vaikka tekstiä on jo olemassa",
        "ocr_deskew_tooltip": "Tasoita vinot skannaukset automaattisesti",
        "ocr_clean_tooltip": "Poista kohina ja artefaktit kuvasta",
        "ocr_oversample_tooltip": "Skaalaa kuva ennen OCR:ää tähän DPI-arvoon",
        "ocr_pagesegmode_tooltip": "Määrittää, miten sivu jaetaan tekstialueisiin",
        "ocr_oem_tooltip": "Valitsee Tesseractin OCR-moottorin",
        "ocr_optimize_tooltip": "Tulosteen PDF-pakkauksen taso",
        "ocr_jobs_tooltip": "Rinnakkaisten OCR-prosessien määrä",
        "ocr_verbose_tooltip": "Lokin tulosteen yksityiskohtaisuuden taso",
        "ocr_settings_explain_btn": "Selitys",

        "ocr_force_ocr_explain": "Pakottaa tekstintunnistuksen <b>jokaiselle</b> sivulle, vaikka se sisältää jo tekstiä.\n\nSuositus: <b>Päällä</b> skannatuille PDF-tiedostoille, <b>Pois</b> alkuperäisille PDF-tiedostoille, joissa on jo tekstiä.",

        "ocr_deskew_explain": "Korjaa hieman vinoja skannauksia (noin 5° asti).\n\nSuositus: <b>Päällä</b> skannatuille asiakirjoille, <b>Pois</b>, jos sivut ovat jo täysin suoria.",

        "ocr_clean_explain": "Poistaa kohinan, pisteet ja pienet artefaktit kuvasta.\n<b>TÄRKEÄÄ:</b> Arabialaisille, thai- tai vietnamilaisille teksteille, joissa on diakriittisiä merkkejä (pisteet kirjainten ylä-/alapuolella), tämä vaihtoehto tulisi <b>poistaa käytöstä</b>, muuten tärkeitä merkkejä saattaa kadota.",

        "ocr_oversample_explain": "Skaalaa kuvan <b>ennen</b> tekstintunnistusta määritettyyn DPI-arvoon.<br><br>• <b>72-150 DPI:</b> Erittäin nopea, mutta alhainen tunnistusaste<br>• <b>200-300 DPI:</b> Optimaalinen alue (Oletus: 300)<br>• <b>400+ DPI:</b> Tuskin parempi tunnistus, mutta huomattavasti suuremmat tiedostot<br><br>Suositus: 300 DPI monimutkaisille kirjoitusjärjestelmille (arabia, kiina, japani), 200 DPI länsimaisille kielille.",

        "ocr_pagesegmode_explain": "Määrittää, miten Tesseract jakaa sivun tekstialueisiin.\n\n• <b>3 - Automaattinen (oletus):</b> Hyvä sekalaisille asetteluille\n• <b>4 - Yksittäinen sarake:</b> Yksisarakeisille teksteille\n• <b>5 - Pystysuora lohko:</b> Pystysuorille kirjoitusjärjestelmille (japani, kiina)\n• <b>6 - Yhtenäinen tekstilohko:</b> Optimaalinen juoksevalle tekstille ilman sarakkeita\n• <b>11 - Raakakuva:</b> Huonoille skannauksille / käsialalle\n\nSuositus: <b>6</b> yksinkertaisille tekstiaineistoille, <b>3</b> monimutkaisille asetteluille.",

        "ocr_oem_explain": "Valitsee Tesseractin OCR-moottorin.\n\n• <b>0 - Legacy:</b> Vanha moottori (nopea, mutta vähemmän tarkka)\n• <b>1 - LSTM:</b> Neuroverkkomoottori (hitaampi, mutta tarkempi)\n• <b>2 - Legacy + LSTM:</b> Yhdistää molemmat tulokset\n• <b>3 - Oletus (LSTM suositeltava):</b> Paras valinta useimmissa tapauksissa\n\nSuositus: <b>3</b> maksimaaliseen tunnistustarkkuuteen.",

        "ocr_optimize_explain": "Pakkaa tulosteen PDF-tiedoston.\n\n• <b>0:</b> Ei optimointia (nopein käsittely)\n• <b>1:</b> Kevyt optimointi (hyvä kompromissi)\n• <b>2:</b> Kohtalainen optimointi\n• <b>3:</b> Voimakas optimointi (pienin tiedosto, mutta hitaampi)\n\nSuositus: <b>1</b> jokapäiväiseen käyttöön.",

        "ocr_jobs_explain": "Rinnakkaisten prosessien määrä OCR:lle.\n\n• <b>1:</b> Hidas, mutta alhaisin muistinkulutus\n• <b>4-8:</b> Optimaalinen moderneille moniydinprosessoreille\n• <b>12+:</b> Tuskin nopeampi käsittely korkealla muistinkulutuksella\n\nSuositus: CPU-ytimien määrä (esim. <b>4</b> 4-ydinjärjestelmissä).",

        "ocr_verbose_explain": "Lokin tulosteen yksityiskohtaisuuden taso konsolissa.\n\n• <b>0:</b> Ei tulostetta\n• <b>1:</b> Edistyminen ja tilaviestit\n• <b>2:</b> Yksityiskohtainen tuloste\n• <b>3:</b> Täysi virheenkorjaustuloste (erittäin laaja)\n\nSuositus: <b>1</b> normaalille toiminnalle.",

        "ocr_reset_title": "Asetukset nollattu",
        "ocr_reset_message": "Kaikki OCR-asetukset on nollattu oletusarvoihin.",
        "info_tooltip": "Lisätietoja tästä parametrista",
        "ocr_reset_defaults": "Palauta oletusarvoihin",

        "ocr_psm_0": "Automaattinen (Legacy-moottori)",
        "ocr_psm_1": "Automaattinen sarakkeiden tunnistus",
        "ocr_psm_3": "Automaattinen (oletus)",
        "ocr_psm_4": "Yksittäinen sarake",
        "ocr_psm_5": "Pystysuora lohko",
        "ocr_psm_6": "Yhtenäinen tekstilohko",
        "ocr_psm_7": "Yksittäinen tekstirivi",
        "ocr_psm_8": "Yksittäinen sana",
        "ocr_psm_11": "Raakakuva (ei asetteluanalyysiä)",

        "ocr_oem_0": "Legacy-moottori (nopea)",
        "ocr_oem_1": "LSTM-moottori (neuro, tarkka)",
        "ocr_oem_2": "Legacy + LSTM yhdistetty",
        "ocr_oem_3": "Oletus (LSTM suositeltava)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-kieli(et)...",
        "ocr_language_title": "Valitse OCR-kieli(et)",
        "ocr_language_instruction": "Valitse kieli(et) tekstintunnistusta (OCR) varten.\nHuomio: Useat kielet heikentävät suorituskykyä ja tarkkuutta!\nParhaat tulokset saat, kun valitset vain yhden kielen.",
        "ocr_language_predefined": "Esimääritellyt yhdistelmät",
        "ocr_language_custom": "Mukautettu...",
        "ocr_language_selected": "Valitut OCR-kielet",
        "ocr_language_changed": "OCR-kieli muutettu kohteeksi {0}",
        "ocr_language_auto_detect": "Saatavilla olevat kielet tunnistetaan automaattisesti.",
        "ocr_language_none_found": "Tesseract-kielitietoja ei löydy! Asenna kielipaketit (esim. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Mukautettu kielen valinta",
        "ocr_language_available": "Saatavilla olevat kielet (asennettu):",
        "ocr_language_select_hint": "Valitse yksi tai useampi kieli:",
        "ocr_language_confirm": "Käytä",
        "ocr_language_reset": "Palauta oletukseen (deu+eng+vie)",
        "ocr_language_priorities": "Suositellut kielet (esiasennettu):",

        "select_all_languages": "Valitse kaikki",
        "clear_all_languages": "Tyhjennä valinta",
        "install_language_packs": "Asenna puuttuvat kielipaketit...",
        "install_hint": "💡 Vinkki: Kaikki kielet eivät ole asennettuna järjestelmääsi. Tällä painikkeella saat apua asennukseen.",
        "ocr_language_install_title": "Tesseract-kielipakettien asennus",

        "ocr_missing_languages": "Puuttuvat OCR-kielipaketit",
        "ocr_missing_languages_message": "Seuraavat valitut kielet eivät ole asennettuna järjestelmääsi:\n\n{0}\n\nAsenna puuttuvat kielipaketit (katso ohje kohdasta 'Asennusohje').\n\nHaluatko avata asennusohjeen nyt?",
        "ocr_missing_languages_voice": "Puuttuvat kielipaketit. Asenna puuttuvat kielet.",
        "ocr_install_help_now": "Avaa ohje",
        "ocr_continue_anyway": "Yritä silti",
        "ocr_language_error_title": "OCR-kielivirhe",
        "ocr_language_error_message": "Virhe tekstintunnistuksessa: {0}\n\nTarkista OCR-kieliasetuksesi (Asetukset → OCR-kieli).",
        "ocr_install_help_button": "Asennusohje",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Asenna Tesseractin kielipaketit</p>

        <p>Jotta OCR toimisi tietyllä kielellä, vastaavien kielitietojen on oltava asennettuna järjestelmääsi. Noudata käyttöjärjestelmäsi ohjeita:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Avaa <strong>Terminaali</strong> (Finder → Ohjelmat → Apuohjelmat → Terminaali).</li>
        <li>Asenna kaikki saatavilla olevat kielet komennolla:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Tämä voi kestää muutaman minuutin.)</li>
        <li>Tai vain yksittäiset kielet (esim. vietnam):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Nykyisissä Homebrew-versioissa <code>*.traineddata</code> on ehkä ladattava manuaalisesti (katso alla).</li>
        <li>Asennuksen jälkeen: Sulje tämä valintaikkuna ja avaa OCR-kielen valinta uudelleen – uudet kielet näkyvät automaattisesti.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Avaa terminaali (Ctrl+Alt+T).</li>
        <li>Asenna haluamasi kieli, esim. vietnam:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Tärkeitä kielikoodeja: <code>deu</code> (saksa), <code>eng</code> (englanti), <code>vie</code> (vietnam), <code>spa</code> (espanja), <code>fra</code> (ranska), <code>ita</code> (italia), <code>nld</code> (hollanti), <code>fin</code> (suomi), <code>swe</code> (ruotsi), <code>nor</code> (norja).</li>
        <li>Näytä kaikki saatavilla olevat paketit:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuaalinen)</p>
        <ol>
        <li>Lataa haluamasi <code>*.traineddata</code>-tiedostot osoitteesta:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (esim. <code>vie.traineddata</code> vietnamille).</li>
        <li>Kopioi tiedostot Tesseractin kielikansioon, yleensä:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Säädä yksilöllisen asennuksen mukaan.)</li>
        <li>Käynnistä sovellus uudelleen (tai avaa OCR-kielen valinta uudelleen).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Vaihtoehto kaikille järjestelmille</p>
        <ul>
        <li>Asenna <strong>OCRmyPDF</strong> ja <strong>Tesseract</strong> haluamallasi paketinhallintaohjelmalla. Useimmat asennukset sisältävät jo joitakin peruskieliä (englanti, saksa, ranska).</li>
        <li>Puuttuvat kielet voidaan asentaa milloin tahansa – OCR-kielen valinta näyttää vain todella olemassa olevat kielet.</li>
        </ul>

        <hr>
        <p><b>✅ Asennuksen jälkeen:</b> Sovellusta ei tarvitse käynnistää uudelleen – äskettäin lisätyt kielet näkyvät heti luettelossa.</p>
        <p><b>📖 Apua kielikoodeihin:</b> Täydellinen luettelo on saatavilla <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseractin dokumentaatiossa</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans -kirjasimet",
        "info_noto_font_voice": "Noto Sans -kirjasinten asennusohje",
        "btn_info_noto_font_install": "Kirjasimen tiedot",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Näin asennat Googlen ilmaiset Noto-kirjasimet</h2>

        <p><strong>Noto-kirjasimet</strong> on Googlen avoimen lähdekoodin kirjasinperhe. Niiden tavoitteena on, ettei näe <em>"yhtään tofua"</em> (eli tyhjiä laatikoita □) ja että jokainen Unicode-standardin merkki näytetään oikein. Ne ovat ihanteellinen lisä sovelluksille, joiden on näytettävä tekstejä monilla eri kielillä.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Asennus macOS:ssä</h3>

        <p><strong>Menetelmä 1: Homebrew'lla (edistyneille)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Menetelmä 2: "Font Book" -sovelluksen kautta (suositeltava)</strong></p>

        <ol>
        <li>Lataa virallinen kirjasinpaketti:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pura ZIP-tiedosto</li>
        <li>Kopioi tiedostot kohteeseen <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Asennus Windowsissa (10 & 11)</h3>

        <p><strong>Menetelmä 1: Microsoft Store (suositeltava)</strong><br>
        Etsi "Google Noto Fonts" tai "Noto Sans" ja napsauta <strong>Asenna</strong>.</p>

        <p><strong>Menetelmä 2: Manuaalinen asennus</strong></p>

        <ol>
        <li>Lataus:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pura ZIP</li>
        <li>Valitse .ttf / .otf -tiedostot</li>
        <li>Oikea napsautus → <strong>Asenna</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        tai<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nimi\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Asennus Linuxissa</h3>

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

        <p>Tarkistus:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Kirjanmerkkien hallinta",
        "bookmark_add": "Lisää kirjanmerkki",
        "bookmark_add_tooltip": "Tallenna nykyinen sivu kirjanmerkiksi",
        "bookmark_remove": "Poista kirjanmerkki",
        "bookmark_remove_tooltip": "Poista merkitty kirjanmerkki",
        "bookmark_remove_all": "Poista kaikki",
        "bookmark_remove_all_tooltip": "Poista tämän PDF:n kaikki kirjanmerkit",
        "bookmark_jump": "Siirry kirjanmerkkiin",
        "bookmark_jump_tooltip": "Siirry valitulle sivulle",
        "bookmark_name": "Nimi",
        "bookmark_page": "Sivu",
        "bookmark_no_bookmarks": "Kirjanmerkkejä ei ole.\nTallenna nykyinen sivu kirjanmerkiksi napsauttamalla 'Lisää'.",
        "bookmark_added": "Kirjanmerkki sivulle {0} lisätty: {1}",
        "bookmark_removed": "Kirjanmerkki poistettu: {0}",
        "bookmark_all_removed": "Kaikki kirjanmerkit on poistettu.",
        "bookmark_name_default": "Sivu {0}",
        "bookmark_name_prompt": "Kirjanmerkin nimi:\n(pitkä teksti lyhennetään 50 merkkiin)",
        "bookmark_name_prompt_title": "Kirjanmerkin nimi",
        "bookmark_confirm_remove_all": "Oletko varma, että haluat poistaa kaikki {0} kirjanmerkkiä?",
        "menu_bookmarks": "Kirjanmerkit",
        "bookmark_manage": "Hallitse kirjanmerkkejä",
        "bookmark_next": "Seuraava kirjanmerkki",
        "bookmark_prev": "Edellinen kirjanmerkki",
        "bookmark_page_display": "Sivu {0}",
        "bookmark_exists": "Tälle sivulle on jo olemassa kirjanmerkki tällä nimellä.",
        "bookmark_select_first": "Valitse ensin kirjanmerkki.",
        "bookmark_confirm_remove": "Oletko varma, että haluat poistaa kirjanmerkin 'Sivu {0}: {1}'?",
        "bookmark_jumped_to": "Siirrytty kirjanmerkkiin '{0}' sivulla {1}.",
        "bookmark_jumped_to_voice": "Kirjanmerkki {0}, sivu {1}",
        "btn_close": "Sulje",

        "bookmark_list": "Kirjanmerkkisi",
        "bookmark_rename": "Nimeä kirjanmerkki uudelleen",
        "bookmark_rename_tooltip": "Muuta valitun kirjanmerkin nimeä",
        "bookmark_rename_title": "Nimeä kirjanmerkki uudelleen",
        "bookmark_rename_prompt": "Uusi nimi kirjanmerkille sivulla {0}:\n(maks. 50 merkkiä)",
        "bookmark_renamed": "Kirjanmerkki '{0}' on nimetty uudelleen muotoon '{1}'.",
        "bookmark_item_tooltip": "Sivu {0}: {1}\nSiirry kaksoisnapsauttamalla",
        "bookmark_name_exists_question": "Tällä sivulla on jo olemassa kirjanmerkki nimellä '{0}'.\nNimetäänkö silti uudelleen?",

        "context_bookmarks": "Kirjanmerkit",
        "context_bookmark_add_here": "Lisää kirjanmerkki tälle sivulle",
        "context_bookmarks_existing": "Olemassa olevat kirjanmerkit:",
        "context_bookmarks_jump": "Siirry kirjanmerkkiin:",
        "context_bookmarks_none": "Kirjanmerkkejä ei ole",
        "context_bookmarks_clear_all": "Poista kaikki {0} kirjanmerkkiä",

        "bookmark_search_placeholder": "Etsi kirjanmerkkejä... (nimi tai sivu)",
        "bookmark_search_results": "Löydettiin %d kirjanmerkkiä haulle \"%s\"",
        "bookmark_no_search_results": "Ei löytynyt kirjanmerkkejä haulle \"%s\"",
        "bookmark_no_search_results_label": "Ei tuloksia haulle \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Muokkaa PDF-metatietoja",
        "metadata_title": "Otsikko",
        "metadata_title_placeholder": "Asiakirjan otsikko",
        "metadata_title_tooltip": "Asiakirjan otsikko (näkyy otsikkopalkissa)",
        "metadata_author": "Tekijä",
        "metadata_author_placeholder": "Tekijän nimi",
        "metadata_author_tooltip": "Asiakirjan luoja",
        "metadata_subject": "Aihe",
        "metadata_subject_placeholder": "Asiakirjan aihe",
        "metadata_subject_tooltip": "Lyhyt kuvaus sisällöstä",
        "metadata_keywords": "Avainsanat",
        "metadata_keywords_placeholder": "Pilkuilla erotetut avainsanat",
        "metadata_keywords_tooltip": "Avainsanat asiakirjan luokitteluun",
        "metadata_creator": "Luoja",
        "metadata_creator_placeholder": "Sovellus, joka loi PDF:n",
        "metadata_creator_tooltip": "Ohjelmisto, jolla asiakirja luotiin",
        "metadata_producer": "Tuottaja",
        "metadata_producer_placeholder": "Sovellus, joka muunsi PDF:n",
        "metadata_producer_tooltip": "Ohjelmisto, joka muunsi PDF:n",
        "metadata_creation_date": "Luontipäivämäärä",
        "metadata_creation_date_tooltip": "Asiakirjan luontipäivämäärä",
        "metadata_mod_date": "Muokkauspäivämäärä",
        "metadata_mod_date_tooltip": "Viimeisen muokkauksen päivämäärä",
        "metadata_pdf_info": "📄 PDF-tiedot",
        "metadata_pages": "Sivumäärä",
        "metadata_file_size": "Tiedostokoko",
        "metadata_pdf_version": "PDF-versio",
        "metadata_encrypted": "Salattu",
        "metadata_encrypted_yes": "Kyllä (salasanalla suojattu)",
        "metadata_encrypted_no": "Ei",
        "metadata_reload": "📂 Lataa uudelleen PDF:stä",
        "metadata_reset": "Hylkää muutokset",
        "metadata_reloaded": "Metatiedot ladattiin uudelleen PDF:stä.",
        "metadata_reset_done": "Kaikki metatietokentät on nollattu.",
        "metadata_no_file": "PDF-tiedostoa ei ole ladattu.",
        "metadata_save_error": "Virhe metatietojen tallennuksessa",
        "metadata_saved": "Metatiedot tallennettiin onnistuneesti.",
        "metadata_pdf_version_unknown": "PDF (tuntematon)",
        "metadata_saved_message": "Metatiedot tallennettiin onnistuneesti.",
        "metadata_saved_voice": "Metatiedot tallennettu.",

        "metadata_custom": "🔧 Mukautetut metatiedot",
        "metadata_custom_placeholder": "{\n  \"minun_kenttäni\": \"minun arvoni\",\n  \"toinen_kenttä\": 123\n}",
        "metadata_custom_tooltip": "JSON-muoto mukautetuille metatiedoille (valinnainen)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Malli \"{0}\" valittu - Kaksoisnapsauta lisätäksesi",
        "text_use_template": "Käytä tekstilohkoa",
        "text_type": "Tyyppi",
        "text_search_templates": "Etsi tekstilohkoja...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Vienti / Tuonti -tiedot",
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

        <h3>📦 Mitä viedään? (Yleiskatsaus)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Yleiset sovellusasetukset</span></li>
            <li class="detail">• Tumma/Vaalea tila</li>
            <li class="detail">• Kuvien käänteinen tumma tila</li>
            <li class="detail">• Harmaan kynnysarvo</li>
            <li class="detail">• Kieli</li>
            <li class="detail">• Ikkunan geometria</li>
            <li class="detail">• Suurennustila</li>
            <li class="detail">• Navigointi (Navigointipalkki näkyvissä)</li>
            <li class="detail">• Puheentuotto (päällä/pois)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Varmuuskopioinnin asetukset</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Tiedostojen nimeäminen (Aikaleima, Erotin, Päätteet)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Asetukset lisäyksille</span></li>
            <li class="detail">• Allekirjoitukset</li>
            <li class="detail">• Teksti ja tekstilohkot</li>
            <li class="detail">• Rastit, kuvat ja muodot</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-asetukset</span></li>
            <li class="detail">• Kieli</li>
            <li class="detail">• Pakota OCR · Sivutila</li>
            <li class="detail">• Kuvan esikäsittely: Vinon korjaus, Puhdistus, Ylinäytteistys</li>
            <li class="detail">• Rinnakkaisten töiden määrä</li>
            <li class="detail">• Käänteistila</li>
            <li class="detail">• Harmaan kynnysarvo</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Kirjanmerkit</span></li>
            <li class="detail">• Kaikki kirjanmerkit PDF-tiedostoa kohti (Sivu, Nimi, Luontiaika)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Salasanatietokanta</span></li>
            <li class="detail">• Tallennetut PDF-salasanat (valinnaisesti salattuja tai pelkkää tekstiä)</li>
            <li class="detail">• Master-salasanan tiiviste (jos asetettu)</li>
            <li class="detail">• Varmennustiedot</li>
        </ul>

        <h4>⚠️ Tärkeitä huomautuksia</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Tuotaessa:</strong>
            <ul>
                <li><span class="warning">➜ KAIKKI nykyiset asetukset korvataan kokonaan</span></li>
                <li>• Sovellus on käynnistettävä uudelleen</li>
                <li>• Olemassa olevat allekirjoitukset, tekstilohkot ja kirjanmerkit korvataan</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Master-salasana ja vientitila:</strong>
            <ul>
                <li>• Kun master-salasana on aktiivinen, voit valita:</li>
                <li>  - <span style="color: #98FB98;"><strong>Pureskeltu</strong></span> (salasanat ovat pelkkää tekstiä ZIP-tiedostossa)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Salattu</strong></span> (vain master-salasanalla luettavissa kohdejärjestelmässä)</li>
                <li>• Master-salasanan tiiviste tallennetaan <strong>aina</strong> salattuna</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Turvallisuusohje:</strong>
            <ul>
                <li>• Viety ZIP-tiedosto sisältää arkaluonteisia tietoja (<strong>salasanat, kirjanmerkit, allekirjoitukset</strong>)</li>
                <li>• Säilytä sitä turvallisesti (esim. salattu USB-muistitikku, salasananhallinta)</li>
                <li>• Jos tiedosto katoaa, tallennetut PDF-salasanat ovat peruuttamattomasti kadonneet</li>
            </ul>
        </div>

        <h4>📁 Vientimuoto</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Asetukset tallennetaan yhteen ZIP-tiedostoon:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Tämä ZIP sisältää täydellisen <code>settings.json</code>-tiedoston (konfiguraatiostasi) sekä mahdollisesti upotetut allekirjoituskuvatiedostot ja salatut salasanat.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Allekirjoitukset - Opas",
        'signature_guide_html': """
        📝 <strong>Allekirjoitukset - Pikaopas</strong><br>
        <ul>
        <li>Aseta pääsalasana</li>
        <li>Määritä allekirjoitukset <em>Asetukset</em>-valikossa (koko, aikaleima, …)</li>
        <li>Lisää <strong>OIKEALLA KLLIKILLÄ</strong> haluamaasi kohtaan (pääsalasana tarvitaan kerran istuntoa kohti)</li>
        <li>Siirrä allekirjoitusta hiirellä tai nuolinäppäimillä</li>
        <li>Lisää useita allekirjoituksia peräkkäin</li>
        <li>Muokkaa jokaista allekirjoitusta yksilöllisesti</li>
        <li>Hylkää yksittäinen allekirjoitus</li>
        <li>Tallenna / hylkää kaikki allekirjoitukset kerralla</li>
        <li>Vaihtoehtoisesti voit käyttää myös valikkoriviä.</li>
        </ul>
        """,
        'signature_guide_voice': "Pikaopas allekirjoituksille. Aseta pääsalasana. Määritä allekirjoitukset asetuksissa. Lisää oikealla klikillä.",

        'image_guide_title': "Kuvien lisääminen - Opas",
        'image_guide_html': """
        📷 <strong>Kuvien lisääminen PDF-tiedostoon - Pikaopas</strong><br>
        <ol>
        <li>Oikea klikkaus haluamaasi kohtaan</li>
        <li><em>„Lisää kuva“</em> → Valitse kuva</li>
        <li>Sijoita kuva: Vedä hiirellä</li>
        <li>Muuta kokoa: Vedä kulmista/reunoista</li>
        <li>Säilytä kuvasuhde: <strong>[A]</strong>-näppäin</li>
        <li>Lisää muokkauksia: Oikea klikkaus kuvassa</li>
        </ol>
        <p><strong>Vinkki:</strong> Pikavalikosta voit muokata asetuksia.</p>
        """,
        'image_guide_voice': "Pikaopas kuville. Oikea klikkaus, lisää kuva, valitse. Sijoita hiirellä, muuta kokoa kulmista. Kuvasuhde A-näppäimellä.",

        'form_guide_title': "Muotojen lisääminen - Opas",
        'form_guide_html': """
        📐 <strong>Muotojen lisääminen PDF-tiedostoon - Pikaopas</strong><br>
        <ol>
        <li>Valitse muototyyppi (suorakulmio, ellipsi, viiva, nuoli)</li>
        <li>Klikkaa kohtaa:
            <ul>
            <li>Suorakulmio/ellipsi: Yksi klikkaus sijoittaa muodon</li>
            <li>Viiva/nuoli: Kaksi klikkausta aloitus- ja loppupisteelle</li>
            </ul>
        </li>
        <li>Sijoita muoto: Vedä hiirellä</li>
        <li>Muuta kokoa: Vedä kulmista/reunoista</li>
        <li>Tallenna muoto: <strong>Enter</strong></li>
        <li>Hylkää muoto: <strong>ESC</strong></li>
        <li>Lisää muokkauksia: Oikea klikkaus muodossa</li>
        </ol>
        <p><strong>Vinkki:</strong> Pikavalikosta voit muokata asetuksia.</p>
        """,
        'form_guide_voice': "Pikaopas muodoille. Valitse muototyyppi. Klikkaa kerran suorakulmiolle tai ellipsille, kahdesti viivalle tai nuolelle. Sijoita hiirellä, muuta kokoa kulmista. Tallenna Enterillä, hylkää Escapella.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "edellinen",
        "btn_next_result": "seuraava",
        "ocr_text_window": "OCR-teksti-ikkuna",
        "bookmark_existing": "Olemassa olevat kirjanmerkit",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR-vertailu Mac - Windows",
        'ocr_method_mac_win_title': "OCR-erot Macin ja Windowsin välillä",
        'ocr_method_mac_win_voice': "Mac on parempi",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Erot macOS:n ja Windowsin välillä</strong></p>

        <p><strong>macOS (suositeltu)</strong></p>
        <p>Työkalu:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Tulos:</p>
        <ul>
        <li>Haettava PDF, jossa on upotettu teksti ja joka säilyttää alkuperäisen asettelun suurelta osin.</li>
        </ul>
        <p>Edut:</p>
        <ul>
        <li>Erinomainen tekstintunnistuksen laatu (myös vinoilla sivuilla).</li>
        <li>Vektorigrafiikan ja fonttien säilyttäminen.</li>
        <li>GUI-edistymispalkki aliprosessin arvioinnin kautta.</li>
        <li>Täysi hallinta kaikista OCR-parametreista (Deskew, Clean, Oversample, optimointi).</li>
        <li>Tekstihaku on suoraan käytettävissä pääikkunassa (PDF-näkymä).</li>
        </ul>
        <p>Haitat:</p>
        <ul>
        <li>Vaatii ylimääräisiä järjestelmätyökaluja (ocrmypdf, Ghostscript, unpaper, pngquant – sisältyvät sovelluspakettiin).</li>
        <li>Monimutkaisempi virheiden käsittely (jumit, aikakatkaisut).</li>
        </ul>

        <p><strong>Windows (vakaa vaihtoehto)</strong></p>
        <p>Työkalu:</p>
        <ul>
        <li>pytesseract (suora yhteys Tesseractiin) + reportlab + PyPDF2</li>
        </ul>
        <p>Tulos:</p>
        <ul>
        <li>Haettava PDF, joka visuaalisesti vastaa kuvapohjaista PDF-tiedostoa, mutta on haettava läpinäkyvän tekstin kautta.</li>
        </ul>
        <p>Edut:</p>
        <ul>
        <li>Ei tule yhtään mieleen tällä hetkellä.</li>
        </ul>
        <p>Haitat:</p>
        <ul>
        <li>PDF on olennaisesti kuva, jossa on näkymätöntä tekstiä; asettelu voi poiketa hieman monimutkaisissa asiakirjoissa (sarakkeet, taulukot).</li>
        <li>Ei automaattista vinouden korjausta (--deskew) tai kuvansiivousta (--clean).</li>
        <li>GUI-edistymispalkki päivitetään vain karkeasti käsiteltyjen sivujen lukumäärän perusteella.</li>
        <li>OCR-nopeus on hieman hitaampi (koska jokainen sivu käsitellään erikseen).</li>
        <li>Tekstihaku ohjataan OCR-teksti-ikkunaan.</li>
        </ul>

        <p><strong>Yhteiset piirteet</strong></p>
        <ul>
        <li>Molemmat menetelmät luovat haettavan PDF-tiedoston samaan hakemistoon kuin lähdetiedosto.</li>
        <li>OCR-asetukset (kieli, DPI, sivun segmentointitila, OCR-moottorin tila) voidaan määrittää OCRSettingsDialogin kautta ja ne ovat voimassa molemmissa toteutuksissa.</li>
        </ul>

        <p><strong>Suositus:</strong></p>
        <ul>
        <li>macOS: ocrmypdf-binääri antaa parhaat tulokset – Osta Mac ja käytä versiota (PDFDarkView Macille, jossa on Apple Silicon tai Intel-siru). OCR-tulokset ovat parempia kuin Windowsissa!</li>
        <li>Windows: Käytä pytesseract-ratkaisua. Se on vakaa ja tarjoaa useimmille asiakirjoille täysin riittävän laadun.</li>
        </ul>

        <p><strong>Tärkeä huomautus:</strong></p>
        <ul>
        <li>Molemmat versiot on integroitu täysin käyttöliittymään – käyttäjä ei huomaa eroa.</li>
        <li>Ohjelma päättää automaattisesti, mitä OCR-moottoria käytetään käyttöjärjestelmän perusteella.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Luo allekirjoitus (skannauksesta)",
        "signature_create_title": "Valitse skannattu allekirjoitus (PDF/kuva)",
        "image_pdf_filter": "Kuvat ja PDF",
        "signature_pdf_empty": "PDF ei sisällä sivuja.",
        "signature_created_success": "Allekirjoitus luotu onnistuneesti: {0}",
        "signature_create_error": "Virhe allekirjoitusta luotaessa:\n{0}",
        "rembg_missing": "rembg ei ole asennettu.\nAsenna: pip install rembg\nVirhe: {0}",
        "signature_name_title": "Tiedostonimi allekirjoitukselle",
        "signature_name_message": "Anna tiedostonimi uudelle allekirjoitukselle (tallennetaan PNG-muodossa läpinäkyvällä taustalla):",
        "signature_name_label": "Tiedostonimi:",
        "signature_name_voice": "Anna tiedostonimi allekirjoitukselle",
        "signature_processing": "Käsittely käynnissä...",
        "signature_creation_title": "Luodaan allekirjoitusta",
        "signature_overwrite_warning": "Tiedosto '{0}' on jo olemassa. Korvataanko?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Valmistele PDF allekirjoitusta varten",
        "signature_prepare_instruction":"Valitse PDF, joka sisältää yhdellä sivulla skannatun allekirjoituksen.\n\nOptimaalinen tunnistus saavutetaan, jos:\n• Allekirjoitus on kirjoitettu mustalla musteella (kuulakärkikynä tai hienokärkinen tussi) valkoiselle paperille.\n• Allekirjoitus on muuten tyhjän A4-sivun yläkolmanneksessa.\n• PDF on skannattu vähintään 300 dpi:n tarkkuudella.\n• Allekirjoitus on selkeä eikä liian ohut.\n• Ei ole häiritseviä taustakuvioita tai viivoja.",
        "signature_prepare_voice":"Valitse PDF, jossa on skannattu allekirjoitus. Kiinnitä huomiota hyvään laatuun ja kontrastiin.",
        "sig_thickness_label":"Viivan paksuus:",
        "sig_thickness_normal":"Normaali (ohut)",
        "sig_thickness_bold":"Lihavoitu (suositeltu)",
        "sig_thickness_very_bold":"Erittäin lihavoitu",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI- ja OCR-kielten lisääminen - Opas",
        'language_guide_title': "GUI- ja OCR-kielten lisääminen",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Lataa haluamasi käännöstiedosto <code>translations_xy.py</code> osoitteesta<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        ja aseta se seuraavaan hakemistoon:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Avaa verkkoselaimesi.</li>
        <li>Mene osoitteeseen: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Etsi näytön oikeasta reunasta "Releases" ja valitse <strong>"latest"</strong>-merkitty.</li>
        <li>Lataa seuraavalta julkaisusivulta alareunasta tiedosto <code>Source Code.zip</code>.</li>
        <li>Pura ZIP-tiedosto.</li>
        <li>Etsi puretusta kansiosta kaikki tarvitsemasi kielitiedostot ja kopioi ne hakemistoon:<br/>
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
        "menu_watermark":"Lisää vesileima",
        "fullpage_text_watermark_title":"Teksti vesileimana",
        "fullpage_image_watermark_title":"Kuva vesileimana",
        "filename_with_watermark":"_vesileimalla",
        "watermark_text":"Teksti:",
        "watermark_text_placeholder":"Vesileimatekstisi...",
        "watermark_font_family":"Fontti:",
        "watermark_font_size":"Fonttikoko:",
        "watermark_format":"Muotoilu:",
        "watermark_bold":"Lihavoitu",
        "watermark_italic":"Kursivoitu",
        "watermark_color":"Väri:",
        "watermark_choose_color":"Valitse väri...",
        "watermark_opacity":"Peittävyys / Läpinäkyvyys:",
        "watermark_direction":"Lukusuunta:",
        "watermark_direction_l_r":"Vasen → Oikea",
        "watermark_direction_bl_tr":"Alhaalla vasen → Ylhäällä oikea",
        "watermark_direction_tl_br":"Ylhäällä vasen → Alhaalla",
        "watermark_direction_b_t":"Alhaalla → Ylhäällä",
        "watermark_direction_t_b":"Ylhäällä → Alhaalla",
        "watermark_preview":"Esikatselu:",
        "watermark_preview_sample":"Esimerkkiteksti",
        "watermark_empty_text":"Syötä teksti.",
        "watermark_applied":"Vesileima on lisätty kaikille sivuille.",
        "watermark_saved":"Vesileima tallennettu.",
        "image_scale":"Koko:",
        "image_preview":"Kuvan esikatselu:",
        "no_image_selected":"Kuvaa ei ole valittu",
        "browse":"Selaa...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Sensuroinnit",
        "redact_add_black": "Sensurointi (musta)",
        "redact_add_white": "Sensurointi (valkoinen / pyyhi)",
        "redact_added_black": "Musta sensurointi lisätty",
        "redact_added_white": "Valkoinen sensurointi lisätty",
        "redact_apply_all": "Käytä kaikki sensuroinnit ja tallenna",
        "redact_discard_all": "Hylkää kaikki sensuroinnit",
        "redact_discard": "Hylkää tämä sensurointi",
        "no_redactions": "Ei sensurointeja",
        "redact_confirm_title": "Käytä sensuroinnit pysyvästi",
        "redact_confirm_message": "Varoitus: Merkityt alueet poistetaan pysyvästi (musta tai valkoinen).\nVarmuuskopio luodaan (jos käytössä).\n\nJatketaanko?",
        "redact_apply": "Kyllä, sensuroi nyt",
        "redact_saved": "{0} sensurointia käytettiin ja tallennettiin onnistuneesti.",
        "redact_saved_voice": "{0} sensurointia käytetty",
        "redact_error": "Virhe sensuroinnissa",
        "filename_redacted":"_sensuroitu",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Lisää sivunumerot',
        'page_numbers_format': 'Numeromuoto:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabialainen)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (roomalainen pieni)',
        'page_numbers_format_roman_upper': 'I, II, III ... (roomalainen iso)',
        'page_numbers_format_letter': 'A, B, C ... (kirjaimet)',
        'page_numbers_format_custom': 'Mukautettu',
        'page_numbers_custom_pattern': 'Malli:',
        'page_numbers_custom_placeholder': 'esim. "Sivu {nummer}" tai "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Käytä {nummer} nykyiselle sivunumerolle ja {total} kokonaismäärälle',
        'page_numbers_position': 'Sijainti:',
        'page_numbers_pos_tl': 'Ylhäällä vasen',
        'page_numbers_pos_tc': 'Ylhäällä keskellä',
        'page_numbers_pos_tr': 'Ylhäällä oikea',
        'page_numbers_pos_ml': 'Keskellä vasen',
        'page_numbers_pos_mc': 'Keskitetty',
        'page_numbers_pos_mr': 'Keskellä oikea',
        'page_numbers_pos_bl': 'Alhaalla vasen',
        'page_numbers_pos_bc': 'Alhaalla keskellä',
        'page_numbers_pos_br': 'Alhaalla oikea',
        'page_numbers_margins': 'Marginaalit:',
        'page_numbers_margin_x': 'Vaakaetäisyys:',
        'page_numbers_margin_y': 'Pystyetäisyys:',
        'page_numbers_range': 'Sivualue:',
        'page_numbers_all_pages': 'Kaikki sivut',
        'page_numbers_custom_range': 'Mukautettu alue',
        'page_numbers_from': 'Alkaen:',
        'page_numbers_to': 'Päättyen:',
        'page_numbers_progress': 'Lisätään sivunumeroita...',
        'page_numbers_start': 'Käynnistetään sivunumeroiden lisäys...',
        'page_numbers_cancel': 'Sivunumeroiden lisäys peruutettu',
        'page_numbers_success': 'Sivunumerot lisättiin onnistuneesti.\n\nHaluatko avata uuden PDF:n?\n\n{0}',
        'page_numbers_complete': 'Sivunumerot lisätty',
        'page_numbers_error_format': 'Virhe sivunumeroiden lisäyksessä: {0}',
        'page_numbers_content_type': 'Sisältötyyppi:',
        'page_numbers_tab_simple': 'Yksinkertainen numero',
        'page_numbers_tab_range': 'Sivu X / Y',
        'page_numbers_tab_date': 'Päivämäärä',
        'page_numbers_tab_custom': 'Vapaa teksti',
        'page_numbers_range_format': 'Muoto:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Sivu {aktuell} / {gesamt}',
        'page_numbers_range_custom': 'Mukautettu',
        'page_numbers_range_placeholder': 'esim. "Sivu {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Päivämäärämuoto:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. tammikuuta 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Mukautettu',
        'page_numbers_date_placeholder': 'esim. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Sijainti:',
        'page_numbers_date_before': 'Päivämäärä ennen sivunumeroa',
        'page_numbers_date_after': 'Päivämäärä sivunumeron jälkeen',
        'page_numbers_date_only': 'Vain päivämäärä (ilman sivunumeroa)',
        'page_numbers_custom_text': 'Mukautettu teksti:',
        'page_numbers_custom_placeholder_text': 'Käytä {seite} sivunumerolle ja {gesamt} kokonaismäärälle\nesim. "Luottamuksellinen - Sivu {seite}" tai "{seite} / {gesamt}"',
        "filename_with_page_number":"_sivunumerolla",
        "filename_with_page_declaration":"_sivun_maarityksella",
        "filename_with_pagenumber":"_sivunumerolla",
        "filename_with_date":"_paivamaaralla",
        "filename_with_my_page_declaration":"_omalla_sivun_maarityksella",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Tallentamattomat muutokset",
        "unsaved_changes_message_darkmode": "Tallentamattomia lisäyksiä on.\nHaluatko tallentaa ne ennen vaihtoa?",
        "save_and_switch": "Tallenna ja vaihda",
        "discard_and_switch": "Vaihda nyt",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Vie sivut kuvina',
        'export_images_menu': 'Vie kuvina (PNG/JPEG)',
        'export_images_format': 'Kuvamuoto:',
        'export_images_dpi': 'Resoluutio (DPI):',
        'export_images_quality': 'JPEG-laatu:',
        'export_images_range': 'Sivualue:',
        'export_images_all_pages': 'Kaikki sivut',
        'export_images_custom_range': 'Mukautettu alue',
        'export_images_from': 'Alkaen:',
        'export_images_to': 'Päättyen:',
        'export_images_options': 'Asetukset:',
        'export_images_single_files': 'Jokainen sivu erillisenä tiedostona',
        'export_images_subfolder': 'Vie alikansioon',
        'export_images_subfolder_info': 'Alikansioon "PDFnimi_kuvat"',
        'export_images_same_folder': 'Samaan kansioon PDF:n kanssa',
        'export_images_apply_darkmode': 'Käytä PDFDarkView-asetuksia (Tumma tila)',
        'export_images_target_folder': 'Kohdekansio:',
        'export_images_browse': 'Selaa...',
        'export_images_preview': 'Esikatselu:',
        'export_images_preview_info': 'Valitse vientiasetukset',
        'export_images_preview_info_detail': '{0} sivua muodossa {1}\nResoluutio: {2} DPI\nTiedostonimi: {3}\n{4}',
        'export_images_select_folder': 'Valitse kohdekansio',
        'export_images_start': 'Käynnistetään kuvien vienti...',
        'export_images_progress': 'Viedään kuvia...',
        'export_images_saving': 'Tallennetaan sivua {0} / {1}...',
        'export_images_success': 'Vienti onnistui!\n\n{0} kuvaa tallennettiin osoitteeseen:\n{1}',
        'export_images_complete': 'Kuvien vienti valmis',
        'export_images_open_folder': '📁 Avaa kansio',
        'export_images_cancel': 'Kuvien vienti peruutettu',
        'export_images_error_format': 'Virhe kuvien viennissä: {0}',
        'export_images_pdf2image_missing': 'Kirjasto "pdf2image" ei ole asennettu.\n\nAsenna se komennolla:\npip install pdf2image\n\nWindowsille tarvitset myös Popplerin:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A-muunnos pitkäaikaiseen arkistointiin',
        'pdfa_menu': 'PDF/A-muunnos (arkistokelpoinen)',
        'pdfa_info': 'Muuntaa PDF:n PDF/A-muotoon.\n\nPDF/A on erityisesti suunniteltu pitkäaikaiseen arkistointiin ja varmistaa, että asiakirja näytetään oikein tulevaisuudessa.',
        'pdfa_standard': 'PDF/A-standardi:',
        'pdfa_standard_select': 'Versio:',
        'pdfa_1': 'PDF/A-1 (yksinkertainen, laajasti yhteensopiva)',
        'pdfa_2': 'PDF/A-2 (moderni, parempi pakkaus)',
        'pdfa_3': 'PDF/A-3 (uusin versio, sallii liitteet)',
        'pdfa_standards_explanation': '📖 Standardien selitys:\n\n'
            '• PDF/A-1: Perus, yhteensopiva vanhempien järjestelmien kanssa (n. 2005)\n'
            '• PDF/A-2: Modernimpi, parempi pakkaus, läpinäkyvyystuki (n. 2011)\n'
            '• PDF/A-3: Uusin versio, sallii tiedostoliitteiden upottamisen (n. 2013)\n\n'
            'Suositus: PDF/A-2 on hyvä kompromissi yhteensopivuuden ja modernien ominaisuuksien välillä.',
        'pdfa_options': 'Asetukset:',
        'pdfa_compress_enable': 'Pakkaus PDF (pienempi tiedosto)',
        'pdfa_metadata_preserve': 'Säilytä metadata (otsikko, tekijä jne.)',
        'pdfa_target_folder': 'Kohdekansio:',
        'pdfa_browse': 'Selaa...',
        'pdfa_select_folder': 'Valitse kohdekansio',
        'pdfa_ocr_info_unknown': '🔍 Tekstisisältöä ei voitu tarkistaa.',
        'pdfa_ocr_info_not_needed': '✅ Tekstiä on saatavilla - OCR ei ole tarpeen.\nPDF/A voidaan luoda suoraan.',
        'pdfa_ocr_info_recommended': '⚠️ Riittävää tekstiä ei löytynyt.\n\nHaettavia PDF-tiedostoja varten suosittelemme OCR:n suorittamista ensin.\nHuom: PDF/A toimii myös ilman OCR:ää - mutta teksti ei ole haettavissa.',
        'pdfa_ocr_info_error': '❌ Virhe tarkistuksessa: {0}',
        'pdfa_start': 'Käynnistetään PDF/A-muunnos...',
        'pdfa_progress': 'PDF/A-muunnos käynnissä...',
        'pdfa_success': 'PDF/A-muunnos onnistui!\n\nTallennettu nimellä:\n{0}\n\nHaluatko avata uuden PDF:n?',
        'pdfa_complete': 'PDF/A-muunnos valmis',
        'pdfa_cancel': 'PDF/A-muunnos peruutettu',
        'pdfa_error_format': 'Virhe PDF/A-muunnoksessa:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Kirjasto "ocrmypdf" ei ole asennettu.\n\nAsenna se komennolla:\npip install ocrmypdf',
        'btn_convert': 'Muunna',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimoi PDF (pienennä tiedostokokoa)',
        'optimize_menu': 'Optimoi PDF (tiedostokoko)',
        'optimize_info': 'Pienentää PDF-tiedoston kokoa eri optimointimenetelmillä.\n\nMitä korkeampi pakkaustaso, sitä pienempi tiedosto - mahdollisella kuvanlaadun heikkenemisellä.',
        'optimize_level': 'Pakkaustaso:',
        'optimize_level_low': 'Matala (nopea, pieni säästö)',
        'optimize_level_medium': 'Keskitaso (hyvä kompromissi)',
        'optimize_level_high': 'Korkea (suuri säästö)',
        'optimize_level_maximum': 'Maksimi (maksimi säästö, hidas)',
        'optimize_level_explanation': 'Suositus: "Keskitaso" on hyvä kompromissi nopeuden ja tiedostokoon välillä.',
        'optimize_options': 'Asetukset:',
        'optimize_compress_images': 'Pakkaa kuvat (vähennä JPEG-laatua)',
        'optimize_clean_objects': 'Poista käyttämättömät objektit',
        'optimize_preserve_metadata': 'Säilytä metadata (otsikko, tekijä jne.)',
        'optimize_image_quality': 'Kuvanlaatu:',
        'optimize_range': 'Sivualue:',
        'optimize_all_pages': 'Kaikki sivut',
        'optimize_custom_range': 'Mukautettu alue',
        'optimize_from': 'Alkaen:',
        'optimize_to': 'Päättyen:',
        'optimize_target_folder': 'Kohdekansio:',
        'optimize_browse': 'Selaa...',
        'optimize_select_folder': 'Valitse kohdekansio',
        'optimize_info_box': 'Tiedot',
        'optimize_info_text': 'Optimointi voi kestää useita minuutteja suurilla PDF-tiedostoilla.\n\nKuvat tallennetaan heikennetyllä laadulla, mikä voi vähentää tiedostokokoa merkittävästi.',
        'optimize_start': 'Käynnistetään PDF-optimointi...',
        'optimize_progress': 'Optimoidaan PDF:ää...',
        'optimize_cancel': 'PDF-optimointi peruutettu',
        'optimize_complete': 'PDF-optimointi valmis',
        'optimize_error_format': 'Virhe PDF-optimoinnissa:\n\n{0}',
        'optimize_success_message': 'PDF-optimointi onnistui!\n\nTallennettu nimellä:\n{0}\n\nEnnen: {1}\nJälkeen: {2}\nSäästö: {3:.1f}%\n\n{4}\n\nHaluatko avata optimoidun PDF:n?',
        'optimize_success_message_no_size': 'PDF-optimointi onnistui!\n\nTallennettu nimellä:\n{0}\n\nKokotietoja ei ole saatavilla.\n\nHaluatko avata optimoidun PDF:n?',
        'optimize_result_positive': 'Tiedostoa pienennettiin {0:.1f}%.',
        'optimize_result_zero': 'Tiedostokoko ei muuttunut.',
        'optimize_result_negative': 'Tiedosto kasvoi {0:.1f}%.\nOptimointi ohitettiin, alkuperäinen tiedosto säilytettiin.',
        'btn_optimize': 'Käynnistä optimointi',
        'filename_optimize_low_suffix': '_optimoitu_matala',
        'filename_optimize_medium_suffix': '_optimoitu',
        'filename_optimize_high_suffix': '_optimoitu_korkea',
        'filename_optimize_maximum_suffix': '_optimoitu_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Rajaa PDF',
        'crop_menu': 'Rajaa PDF (Crop)',
        'crop_range': 'Kohdista:',
        'crop_all_pages': 'Kaikki sivut',
        'crop_current_page': 'Vain nykyinen sivu',
        'crop_values': 'Rajausarvot (pisteissä):',
        'crop_left': 'Vasen:',
        'crop_right': 'Oikea:',
        'crop_top': 'Ylhäällä:',
        'crop_bottom': 'Alhaalla:',
        'crop_presets': 'Esiasetukset:',
        'crop_preset_white': 'Tunnista valkoiset marginaalit',
        'crop_reset': 'Nollaa',
        'crop_mouse_hint': '🖱️ Vedä suorakulmio valitaksesi alueen karkeasti.\nVoit sitten säätää arvoja tarkasti SpinBoxeissa.\nManuaalinen säätö hiirellä ei ole mahdollista.',
        'crop_apply': 'Rajaa',
        'crop_scope_all': 'Kaikki sivut',
        'crop_scope_current': 'Nykyinen sivu',
        'crop_new_size': 'Uusi koko: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'PDF:ää ei ole ladattu',
        'crop_preview_error': 'Virhe esikatselun latauksessa',
        'crop_start': 'Käynnistetään rajaaminen...',
        'crop_progress': 'Rajataan PDF:ää...',
        'crop_success': 'PDF rajattu onnistuneesti!\n\nTallennettu nimellä:\n{0}\n\nHaluatko avata rajatun PDF:n?',
        'crop_complete': 'Rajaaminen valmis',
        'crop_cancel': 'Rajaaminen peruutettu',
        'crop_error_format': 'Virhe rajaamisessa:\n\n{0}',
        'filename_crop_suffix': '_rajattu',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Tasoita PDF (Flatten)',
        'flatten_menu': 'Tasoita PDF (Flatten)',
        'flatten_info': 'PDF:n tasoittaminen "polttaa" kaikki muokattavat elementit sivun sisältöön.\n\nSen jälkeen lomakekentät, huomautukset, tekstit, ristit, allekirjoitukset, kuvat ja muodot eivät ole enää yksittäin muokattavissa.',
        'flatten_explanation_title': '📖 Mihin tämä on hyvä?',
        'flatten_explanation_text': 'Tasoittaminen on tarpeen seuraavissa tilanteissa:\n\n'
            '• 📄 Haluat valmistella asiakirjan tulostusta varten\n'
            '• 🔒 Haluat estää lomakekenttien muuttamisen\n'
            '• 📎 Haluat upottaa huomautukset ja kommentit "pysyvästi" asiakirjaan\n'
            '• 🖼️ Haluat ankkuroida lisätyt tekstit, ristit, allekirjoitukset, kuvat ja muodot pysyvästi asiakirjaan\n'
            '• 📦 Haluat valmistella tiedoston arkistointia varten\n\n'
            'Tasoittaminen tekee PDF:stä pienemmän ja estää elementtien vahingossa tapahtuvan siirtämisen tai poistamisen.',
        'flatten_what_title': 'Mitä tasoitetaan?',
        'flatten_what_list': '• ✅ Lomakekentät (tekstikentät, valintaruudut, painikkeet)\n'
            '• ✅ Huomautukset (kommentit, korostukset, muistiinpanot)\n'
            '• ✅ Päällekkäisyydet (tekstit, ristit, allekirjoitukset, kuvat, muodot)',
        'flatten_options': 'Asetukset:',
        'flatten_forms': 'Tasoita lomakekentät',
        'flatten_annotations': 'Tasoita huomautukset',
        'flatten_overlays': 'Tasoita päällekkäisyydet (tekstit, ristit, allekirjoitukset, kuvat, muodot)',
        'flatten_target_folder': 'Kohdekansio:',
        'flatten_browse': 'Selaa...',
        'flatten_select_folder': 'Valitse kohdekansio',
        'flatten_warning': '⚠️ Tärkeää: Tasoittaminen on peruuttamaton prosessi!\n\nTasoittamisen jälkeen muokattavia elementtejä ei voi enää yksittäin muuttaa tai poistaa.\nLuo tarvittaessa varmuuskopio etukäteen.',
        'flatten_apply': 'Tasoita',
        'flatten_start': 'Käynnistetään tasoittaminen...',
        'flatten_progress': 'Tasoitetaan PDF:ää...',
        'flatten_success': 'PDF tasoitettu onnistuneesti!\n\nTallennettu nimellä:\n{0}\n\nHaluatko avata tasoitetun PDF:n?',
        'flatten_complete': 'Tasoittaminen valmis',
        'flatten_cancel': 'Tasoittaminen peruutettu',
        'flatten_error_format': 'Virhe tasoittamisessa:\n\n{0}',
        'filename_flatten_suffix': '_tasoitettu',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF-päällekkäisyys (Overlay)',
        'overlay_menu': 'PDF-päällekkäisyys (Overlay)',
        'overlay_info': 'Asettaa yhden PDF:n (päällekkäisyyden) toisen PDF:n päälle.\n\nPäällekkäinen PDF asetetaan perus-PDF:n päälle. Tämä on hyödyllistä vesileimoille, logoille, kirjelomakkeille tai leimoille.',
        'overlay_explanation_title': '📖 Mihin tämä on hyvä?',
        'overlay_explanation_text': 'Päällekkäisyys on tarpeen seuraavissa tilanteissa:\n\n'
            '• 🏢 Aseta yrityksen logo vesileimana jokaiselle sivulle\n'
            '• 📄 Aseta kirjelomake tyhjälle PDF:lle\n'
            '• 🖊️ Aseta leimapäällekkäisyys asiakirjaan\n'
            '• 🔖 Aseta vesileima kaikille sivuille\n'
            '• 📑 Aseta lomakepäällekkäisyys mallille',
        'overlay_type': 'Päällekkäisyyden tyyppi:',
        'overlay_type_fullpage': 'Koko sivu (peittävä)',
        'overlay_type_transparent': 'Koko sivu (läpinäkyvä - suositeltu)',
        'overlay_type_stamp': 'Leima (paikoitettava)',
        'overlay_type_info_fullpage': '📄 Päällekkäinen PDF asetetaan tarkasti koko sivun päälle.\nValkoinen tausta voidaan poistaa, jotta vain sisältö näkyy.',
        'overlay_type_info_transparent': '🔍 Päällekkäinen PDF asetetaan koko sivun päälle läpinäkyvällä taustalla.\nValkoinen tausta poistetaan automaattisesti - ihanteellinen vesileimoille ja logoille!',
        'overlay_type_info_stamp': '🖊️ Päällekkäinen PDF asetetaan ja skaalataan leimana.\nTäydellinen logoille, leimoille tai allekirjoituksille tietyissä paikoissa.',
        'overlay_remove_background': 'Poista valkoinen tausta:',
        'overlay_remove_background_enable': 'Poista valkoinen tausta päällekkäisestä PDF:stä (tekee päällekkäisyydestä läpinäkyvän)',
        'overlay_remove_background_tooltip': 'Poistaa valkoiset alueet päällekkäisestä PDF:stä, jotta alla oleva teksti tulee näkyviin.',
        'overlay_threshold': 'Kynnysarvo:',
        'overlay_threshold_hint': '(1-254, korkeampi = enemmän valkoista poistetaan)',
        'overlay_select_file': 'Valitse päällekkäinen PDF:',
        'overlay_file_placeholder': 'Valitse PDF-tiedosto päällekkäisyyttä varten',
        'overlay_browse': 'Selaa...',
        'overlay_select_overlay': 'Valitse päällekkäinen PDF',
        'overlay_range': 'Sivualue:',
        'overlay_all_pages': 'Kaikki sivut',
        'overlay_custom_range': 'Mukautettu alue',
        'overlay_from': 'Alkaen:',
        'overlay_to': 'Päättyen:',
        'overlay_position': 'Sijainti:',
        'overlay_position_center': 'Keskellä',
        'overlay_position_top_left': 'Ylhäällä vasen',
        'overlay_position_top_right': 'Ylhäällä oikea',
        'overlay_position_bottom_left': 'Alhaalla vasen',
        'overlay_position_bottom_right': 'Alhaalla oikea',
        'overlay_size': 'Koko:',
        'overlay_size_original': 'Alkuperäinen koko',
        'overlay_size_fit_page': 'Sovita sivulle',
        'overlay_size_custom': 'Mukautettu (%)',
        'overlay_opacity': 'Läpinäkyvyys:',
        'overlay_target_folder': 'Kohdekansio:',
        'overlay_browse_folder': 'Selaa...',
        'overlay_select_folder': 'Valitse kohdekansio',
        'overlay_warning': '⚠️ Huom: Päällekkäinen PDF asetetaan perus-PDF:n päälle ja "poltetaan" siihen.\n\nPäällekkäisen PDF:n elementtejä ei voi enää muokata yksittäin tallennuksen jälkeen.',
        'overlay_apply': 'Päällekkäisyys',
        'overlay_start': 'Käynnistetään päällekkäisyys...',
        'overlay_progress': 'PDF-päällekkäisyys...',
        'overlay_success': 'PDF päällekkäisyys onnistui!\n\nTallennettu nimellä:\n{0}\n\nHaluatko avata päällekkäisen PDF:n?',
        'overlay_complete': 'Päällekkäisyys valmis',
        'overlay_cancel': 'Päällekkäisyys peruutettu',
        'overlay_error_format': 'Virhe päällekkäisyydessä:\n\n{0}',
        'overlay_no_file': 'Päällekkäistä PDF:ää ei ole valittu.\n\nValitse PDF-tiedosto päällekkäisyyttä varten.',
        'filename_overlay_suffix': '_paallekkainen',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Pura kuvat PDF:stä',
        'extract_images_menu': 'Pura kaikki kuvat',
        'extract_images_info': 'Puraa kaikki kuvat PDF:stä ja tallentaa ne erillisinä tiedostoina.\n\nKuvat tallennetaan alkuperäisessä muodossaan tai muunnetaan valittuun muotoon.',
        'extract_images_format': 'Kuvamuoto:',
        'extract_images_quality': 'JPEG-laatu:',
        'extract_images_options': 'Asetukset:',
        'extract_images_subfolder': 'Pura alikansioon ("PDFnimi_kuvat")',
        'extract_images_unique': 'Vain ainutlaatuiset kuvat (vältä kopioita)',
        'extract_images_range': 'Sivualue:',
        'extract_images_all_pages': 'Kaikki sivut',
        'extract_images_custom_range': 'Mukautettu alue',
        'extract_images_from': 'Alkaen:',
        'extract_images_to': 'Päättyen:',
        'extract_images_target_folder': 'Kohdekansio:',
        'extract_images_browse': 'Selaa...',
        'extract_images_select_folder': 'Valitse kohdekansio',
        'extract_images_info_box': 'Tiedot',
        'extract_images_info_text': 'Purku voi kestää useita minuutteja suurilla PDF-tiedostoilla.\n\nKuvat tallennetaan alkuperäisellä nimellään (sivu_kuva).',
        'extract_images_extract': 'Pura',
        'extract_images_start': 'Käynnistetään purku...',
        'extract_images_progress': 'Puretaan kuvia...',
        'extract_images_success': '✅ Kuvat purettiin onnistuneesti!\n\n{0} kuvaa tallennettiin osoitteeseen:\n{1}',
        'extract_images_complete': 'Kuvien purku valmis',
        'extract_images_cancel': 'Purku peruutettu',
        'extract_images_error_format': 'Virhe kuvien purussa:\n\n{0}',
        'extract_images_open_folder': '📁 Avaa kansio',
        'extract_images_no_images': 'PDF:stä ei löytynyt kuvia.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Useita sivuja yhdellä sivulla (N-Up)',
        'nup_menu': 'Useita sivuja yhdellä sivulla (N-Up)',
        'nup_info': 'Järjestää useita PDF-sivuja yhdelle sivulle.\n\nIhanteellinen kompakteille tulosteille, yleiskatsauksille tai monisteille.',
        'nup_layout': 'Asettelu:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Esikatselu:',
        'nup_preview_info': '{0} sivua → {1} sivua arkkia kohti → {2} arkkia\nAsettelu: {3}',
        'nup_order': 'Järjestys:',
        'nup_order_horizontal': 'Vaaka (rivi riviltä)',
        'nup_order_vertical': 'Pysty (sarake sarakkeelta)',
        'nup_order_horizontal_reverse': 'Vaaka käänteinen',
        'nup_order_vertical_reverse': 'Pysty käänteinen',
        'nup_range': 'Sivualue:',
        'nup_all_pages': 'Kaikki sivut',
        'nup_custom_range': 'Mukautettu alue',
        'nup_from': 'Alkaen:',
        'nup_to': 'Päättyen:',
        'nup_options': 'Asetukset:',
        'nup_margins': 'Marginaalit:',
        'nup_margin_between': 'Väli sivujen välillä:',
        'nup_page_numbers': 'Lisää sivunumerot',
        'nup_target_folder': 'Kohdekansio:',
        'nup_browse': 'Selaa...',
        'nup_select_folder': 'Valitse kohdekansio',
        'nup_create': 'Luo',
        'nup_start': 'Käynnistetään N-Up...',
        'nup_progress': 'Luodaan N-Up...',
        'nup_success': 'N-Up luotu onnistuneesti!\n\nTallennettu nimellä:\n{0}\n\nHaluatko avata uuden PDF:n?',
        'nup_complete': 'N-Up valmis',
        'nup_cancel': 'N-Up peruutettu',
        'nup_error_format': 'Virhe N-Up:ssa:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Muuta sivukokoa',
        'pagesize_menu': 'Muuta sivukokoa',
        'pagesize_info': 'Muuttaa PDF:n sivukokoa.\n\nSisältö mukautuu automaattisesti uuteen kokoon.',
        'pagesize_format': 'Muoto:',
        'pagesize_select': 'Valitse vakiomuoto:',
        'pagesize_custom': 'Mukautettu koko:',
        'pagesize_width': 'Leveys:',
        'pagesize_height': 'Korkeus:',
        'pagesize_orientation': 'Suunta:',
        'pagesize_portrait': 'Pysty',
        'pagesize_landscape': 'Vaaka',
        'pagesize_scale_options': 'Skaalausvaihtoehdot:',
        'pagesize_fit': 'Sovita (säilytä kuvasuhde)',
        'pagesize_stretch': 'Venytä (vääristä)',
        'pagesize_center': 'Keskitä (alkuperäinen koko)',
        'pagesize_range': 'Sivualue:',
        'pagesize_all_pages': 'Kaikki sivut',
        'pagesize_custom_range': 'Mukautettu alue',
        'pagesize_from': 'Alkaen:',
        'pagesize_to': 'Päättyen:',
        'pagesize_target_folder': 'Kohdekansio:',
        'pagesize_browse': 'Selaa...',
        'pagesize_select_folder': 'Valitse kohdekansio',
        'pagesize_apply': 'Käytä',
        'pagesize_start': 'Käynnistetään sivukoon muutos...',
        'pagesize_progress': 'Muutetaan sivukokoa...',
        'pagesize_success': 'Sivukoko muutettu onnistuneesti!\n\nTallennettu nimellä:\n{0}\n\nHaluatko avata uuden PDF:n?',
        'pagesize_complete': 'Sivukoon muutos valmis',
        'pagesize_cancel': 'Sivukoon muutos peruutettu',
        'pagesize_error_format': 'Virhe sivukoon muutoksessa:\n\n{0}',
        'pagesize_preview_info': 'Uusi koko: {0} x {1} pt',
        'filename_pagesize_suffix': '_uusi_koko',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-tiedot',
        'pdf_info_menu': 'Näytä PDF-tiedot',
        'pdf_info_voice': 'Näytetään PDF-tiedot',
        'pdf_info_error': 'Virhe PDF-tietojen näyttämisessä:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Näytä pikanäppäimet",
        "shortcuts_dialog_title": "Pikanäppäimet",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 TIEDOSTO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Avaa PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Sulje PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Tallenna nimellä...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Suojaa asiakirja</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Tulosta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Tulosta heti (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Sulje sovellus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 VIE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Vie Pages-muodossa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Vie DOCX-muodossa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Vie TXT-muodossa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Vie kuvina (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Pura kuvat</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ASIAKIRJAN KÄSITTELY</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Useita sivuja)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A-muunnos (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Tasoita PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF-päällekkäisyys</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimoi PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ MUOKKAA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Hae</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Lisää kirjanmerkki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Hallitse kirjanmerkkejä</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Seuraava kirjanmerkki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Edellinen kirjanmerkki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Suorita OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SIVUJEN HALLINTA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Kierrä nykyinen sivu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Kierrä kaikki sivut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalisoi nykyinen sivu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalisoi kaikki sivut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Poista sivut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Pura sivut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Lisää sivut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Siirrä sivut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Yhdistä PDF:t</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Muuta sivukokoa</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 LISÄÄ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Lisää teksti</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Lisää risti</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Lisää allekirjoitus 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Lisää allekirjoitus 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Lisää kuva</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Lisää suorakulmio</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Lisää ellipsi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Lisää viiva</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Lisää nuoli</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Lisää sivunumerot</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Tekstivesileima</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Kuvavesileima</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ SENSUROINNIT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Sensurointi (musta)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Sensurointi (valkoinen)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Käytä kaikki sensuroinnit</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ LISÄASETUKSET</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Rajaa PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Muokkaa metadataa</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ NÄKYMÄ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Vaihda Tumma/Vaalea tila</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Näytä teksti-ikkuna</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Sivun leveys (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Kaksi sivua (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Yleiskatsaus (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ASETUKSET</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Salasanahallinta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR-asetukset</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Allekirjoitusasetukset</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Tiedostonimien muotoilu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Vie asetukset</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Tuo asetukset</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ TIEDOT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Näytä PDF-tiedot</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Ota puheääni käyttöön/pois</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Kohdista valikkopalkki</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Uusi versio saatavilla",
        "update_available_message": "Uusi versio <b>{0}</b> on saatavilla.\n\nKäy julkaisusivulla ladataksesi päivityksen:\n{1}",
        "update_available_voice": "Uusi versio {0} saatavilla. Lataa päivitys GitHub-sivulta.",
        "update_open_release": "Avaa julkaisusivu",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Lataa kaikki käännökset",
        "ask_download_all_translations": """Saksan, englannin ja vietnamin lisäksi saatavilla on {total_languages} muuta käyttöliittymäkieltä.\n\nPitäisikö ne tarjota / päivittää?\n\nHuomautus:\nTarpeettomat kielet voit myöhemmin poistaa manuaalisesti hakemistosta:\n{translations_path}
        \nJos peruutat, voit ladata käyttöliittymäkielet myöhemmin valikosta 'Työkalut → Päivitä käännökset'.""",
        "menu_update_translations": "Päivitä käännökset",
        "translations_updated": "Käännökset päivitetty",
        "translations_update_success": "{} käännöstä päivitettiin onnistuneesti ({} uutta, {} päivitettyä).",
        "translations_update_error": "Virhe käännösten päivityksessä",
        "translations_update_no_changes": "Kaikki käännökset ovat jo ajan tasalla.",
        "translations_update_offline": "Ei internetyhteyttä. Käännöksiä ei voitu päivittää.",
        "translations_update_in_progress": "Käännöksiä päivitetään taustalla...",
        "translations_downloading": "Ladataan käännöksiä...",
        "translations_path_hint": "Käyttäjän hakemisto käännöksille",
        "translations_update_not_available_title": "Päivitys ei ole saatavilla",
        "translations_update_not_available_message": """Käännösten päivitys on saatavilla vain asennetussa versiossa.\n\nKehitystilassa käännökset ovat jo ajan tasalla.""",
        "translations_update_no_internet_title": "Ei internetyhteyttä",
        "translations_update_no_internet_message": """Internet-yhteyttä ei voitu muodostaa.\n\nKäännöksiä ei voida ladata GitHubista.\n\nMahdolliset ratkaisut:
        • Tarkista internetyhteytesi
        • Poista mahdollinen palomuuri tilapäisesti käytöstä
        • Yritä myöhemmin uudelleen
        \nVoit myös ladata käännökset manuaalisesti GitHubista:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Päivitys on jo käynnissä",
        "btn_retry": "Yritä uudelleen",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Tervetuloa PDF Dark View'hin",
        "welcome_title_not_supported": "Tervetuloa PDF Dark View'hin",
        "welcome_message": "Tervetuloa PDF Dark View'hin!\n\nJärjestelmäsi kieli tunnistettiin nimellä '{language}'.\nHaluatko käyttää tätä kieltä käyttöliittymässä?\n\nVoit vaihtaa kieltä milloin tahansa kohdasta 'Asetukset → Kieli'.",
        "welcome_message_language_not_available": "Tervetuloa PDF Dark View'hin!\n\nJärjestelmäsi kieli tunnistettiin nimellä '{language}'.\nTätä kieltä ei ole vielä asennettu.\n\nHaluatko ladata käännökset kielelle {language} nyt GitHubista?\n\n(Kieltä käytetään sitten automaattisesti käyttöliittymässä.)",
        "welcome_message_language_not_supported": "Tervetuloa PDF Dark View'hin!\n\nJärjestelmäsi kieli tunnistettiin nimellä '{language}'.\nValitettavasti tälle kielelle ei ole vielä käännöksiä.\n\nKäyttöliittymä näytetään kielellä {fallback_language}.\n\nVoit vaihtaa kieltä milloin tahansa kohdasta 'Asetukset → Kieli'.\nJos haluat, voit myös itse osallistua käännökseen omalle kielellesi:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Kyllä, käytä järjestelmän kieltä",
        "welcome_keep_english": "Ei, pidä englanti",
        "welcome_download_language": "Kyllä, lataa {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Ohjelma sulkeutuu",

    }
