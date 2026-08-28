
# ============================================
# translations_sl.py - Slovenski slovar (Slowenisch)
# Vollständig sortiert nach Kategorien
# ============================================

def load_slovenian_strings():
    """Lädt alle slowenischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Odpri PDF",
        'btn_text_window': "Besedilo OCR",
        'btn_first': "Prva stran",
        'btn_prev': "Prejšnja stran",
        'btn_next': "Naslednja stran",
        'btn_last': "Zadnja stran",
        'btn_print': "Natisni",
        'btn_darkmode_light': "Svetli način",
        'btn_darkmode_dark': "Temni način",
        'btn_delete_pages': "Izbriši strani",
        'btn_extract_pages': "Izloči strani",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "V redu",
        'btn_cancel': "Prekliči",
        'btn_save': "Shrani",
        'btn_close': "Zapri",
        'btn_delete': "Izbriši",
        'btn_delete_all': "Izbriši vse",
        'btn_copy': "Kopiraj",
        'btn_export': "Izvozi",
        'btn_show': "Pokaži geslo",
        'btn_hide': "Skrij geslo",
        'btn_authenticate': "Avtenticiraj",
        'btn_settings': "Nastavitve",
        'btn_protect': "Zaščiti",
        'btn_remove_password': "Odstrani geslo",
        'btn_manage': "Upravljanje gesel",
        'btn_retry': "Poskusi znova",
        'btn_select_all': "Izberi vse",
        'btn_clear_selection': "Počisti izbiro",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Stran {0} od {1}",
        'page_count': "od {0}",
        'goto_page': "Pojdi na stran",
        'page_simple': "Stran {0}",
        'full_view_page': "Celoten pogled stran {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Vnesite iskalni izraz + Enter",
        'search_results': "Zadetki: {0} od {1}",
        'search_nav_hint': "Enter: naslednji (Shift+Enter: prejšnji) zadetek",
        'search_no_results': "Ni zadetkov",
        'search_error': "Napaka pri iskanju",
        'search_active': "Iskalno polje je aktivirano",
        'search_closed': "Iskanje končano",
        'search_position': "Stran {0} {1}",
        'search_pos_top': "čisto zgoraj",
        'search_pos_upper': "zgoraj",
        'search_pos_middle': "sredina",
        'search_pos_lower': "spodaj",
        'search_pos_bottom': "čisto spodaj",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Prepoznavanje besedila je uspešno zaključeno!",
        'ocr_success_title': "OCR uspešen",
        'ocr_success_message': "Dokument je zdaj mogoče iskati.",
        'ocr_failed': "OCR ni uspel",
        'ocr_in_progress': "OCR v teku",
        'ocr_preparing': "Pripravljam PDF...",
        'ocr_analyzing': "Analiziram PDF...",
        'ocr_optimizing': "Optimizacija slike...",
        'ocr_recognizing': "Prepoznavanje besedila...",
        'ocr_embedding': "Vdelava besedila...",
        'ocr_finalizing': "Zaključevanje PDF...",
        'ocr_not_available': "OCR ni na voljo",
        'ocr_install_message': "Orodja OCR niso bila najdena.\n\nNamestite jih:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Zahtevan je OCR",
        'ocr_question': "PDF ne vsebuje besedila, ki ga je mogoče iskati.\nAli želite izvesti OCR, da omogočite {0}?",
        'ocr_perform': "Izvedi OCR",
        'ocr_later': "Kasneje",
        'ocr_starting': "Zaganjam zajamčeni OCR...",
        'ocr_success_voice': "OCR uspešen. PDF je zdaj mogoče iskati.",
        'ocr_partial_success': "OCR je bil izveden, vendar je prišlo do težav pri zamenjavi.\n\nRazličica za iskanje je shranjena na:\n{0}\n\nNapaka: {1}",
        'ocr_partial_title': "OCR delno uspešen",
        'ocr_partial_voice': "OCR izveden, vendar zamenjava ni uspela.",
        'original_file': "Izvirna datoteka:",
        'old_size': "Stara velikost:    {0} bajtov",
        'new_size': "Nova velikost: {0} bajtov",
        'size_change': "Sprememba: {0}{1} bajtov",
        'backup_created_file': "Varnostna kopija ustvarjena:\n{0}",
        'backup_not_created': "Varnostna kopija ni ustvarjena (nastavitev izklopljena)",
        'page_header': "=== Stran {0} ===\n{1}\n",
        'scanned_page_header': "=== Stran {0} (skenirana) ===\n[Ta stran vsebuje samo skenirano besedilo]\n[Izvedite OCR ročno]\n",
        'scanned_warning': "⚠️ SKENIRANO BESEDILO - ZAHTEVAN OCR",
        'guaranteed_title': "Ustvarjen iskalni PDF",
        'guaranteed_message': "<b>Ustvarjena je zajamčena iskalna različica!</b>\n\nKer samodejni OCR ni uspel, je bila ustvarjena alternativna iskalna različica PDF:\n\n{0}\n\n<b>Ta datoteka vsebuje:</b>\n• Izvlečeno besedilo (če je obstajalo)\n• Navodila za skenirane strani\n• Popolnoma iskalno",
        'guaranteed_voice': "Ustvarjen zajamčeni iskalni PDF.",
        'instruction_title': "NAVODILA ZA OCR",
        'instruction_file': "Izvirna datoteka: {0}",
        'instruction_text': "Samodejno prepoznavanje besedila (OCR) ni uspelo.\nIzvedite OCR ročno:\n\n1. Z OCRmyPDF (ukazna vrstica):\n   ocrmypdf --force-ocr \"[DATOTEKA]\" \"izhod.pdf\"\n\n2. Z ADOBE ACROBAT (macOS/Windows):\n   • Odprite PDF v Acrobatu\n   • Orodja > Uredi PDF\n   • Izberite 'Prepoznavanje besedila'\n\n3. S PREVIEW (macOS):\n   • Odprite PDF v Predogledu\n   • Datoteka > Izvozi...\n   • Filter Quartz: 'Zmanjšaj velikost datoteke'\n   • Omogočite 'Izvedi OCR'\n\n4. SPLETNE STORITVE OCR:\n   • smallpdf.com/sl/ocr-pdf\n   • ilovepdf.com/sl/ocr-pdf\n   • adobe.com/sl/acrobat/online/pdf-to-word.html",
        'instruction_created': "Ustvarjena navodila za OCR",
        'instruction_created_message': "Ustvarjena so podrobna navodila:\n\n{0}\n\nSledite korakom za ročni OCR.",
        'instruction_created_voice': "Ustvarjena navodila za OCR.",
        'ocr_impossible': "OCR ni mogoč",
        'ocr_impossible_message': "OCR ni bilo mogoče izvesti.\n\nObdelajte '{0}' ročno s programsko opremo za OCR.",
        'ocr_impossible_voice': "OCR ni mogoč. Obdelajte ročno.",
        'emergency_title': "Nujni OCR",
        'emergency_message': "Ustvarjen je nujni PDF:\n\n{0}\n\nTo datoteko obdelajte ročno z OCR.",
        'emergency_voice': "Ustvarjen nujni PDF. Izvedite OCR ročno.",
        'critical_error': "Kritična napaka",
        'critical_error_message': "OCR ni bilo mogoče zagnati.\n\nZnova zaženite program in preverite namestitev OCR.",
        'critical_error_voice': "Kritična napaka OCR",
        'ocr_question_html': "<p>PDF ne vsebuje iskalnega besedila.<p>Ali želite izvesti OCR, da omogočite <b>{0}</b>?</p>",
        'ocr_question_voice': "Zahtevan je OCR. PDF ne vsebuje iskalnega besedila. Ali želite izvesti OCR, da omogočite {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ni naloženega PDF",
        'no_pdf_message': "Ni naloženega PDF",
        'pdf_not_found': "Datoteke PDF ni mogoče najti",
        'file_size': "Velikost datoteke",
        'bytes': "bajtov",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Varnostna kopija ustvarjena",
        'backup_disabled': "Varnostno kopiranje izklopljeno",
        'backup_activated': "Ustvarjanje varnostnih kopij vklopljeno",
        'backup_deactivated': "Ustvarjanje varnostnih kopij izklopljeno",
        'backup_status': "Varnostna kopija: {0}",
        'backup_on': "✔ vklopljeno",
        'backup_off': "✘ izklopljeno",
        'close_pdf': "Zapiram PDF: {0}",
        'pdf_not_found_format': "Datoteke PDF ni mogoče najti: {0}",
        'error_pdf_load_format': "Napaka pri nalaganju PDF: {0}",
        'load_failed_format': "Nalaganje ni uspelo:\n{0}",
        'decrypted_suffix': "(dešifrirano)",
        'decryption_failed': "Dešifriranje ni uspelo.",
        'decryption_error': "Napaka pri dešifriranju",
        'decryption_success': "Uspešno dešifrirano",
        'decryption_success_message': "PDF je bil dešifriran in shranjen na:\n\n{0}",
        'decryption_success_voice': "PDF je bil dešifriran in shranjen.",
        'password_remove_error': "Napaka pri odstranjevanju gesla",
        'save_unencrypted': "Shrani nešifriran PDF kot",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Shrani kot...",
        'save_copy': "Shrani kopijo",
        'save_success': "PDF shranjen na: {0}",
        'save_encrypted': "Zaščiten PDF shranjen na: {0}",
        'save_error': "PDF ni bilo mogoče shraniti",
        'encryption_question': "Ali želite zaščititi PDF z geslom?",
        'encryption_yes': "Da",
        'encryption_no': "Ne",
        'encryption_cancel': "Prekliči",
        'save_cancel': "Shranjevanje preklicano",
        'save_encrypted_voice': "Datoteka šifrirana in shranjena.",
        'save_success_voice': "Datoteka PDF je bila shranjena nešifrirana.",
        'save_error_format': "PDF ni bilo mogoče shraniti:\n{0}",
        'export_pages_success': "Izvoz v Pages uspešen",
        'export_pages_error': "Izvoz v Pages ni uspel",
        'export_pages_error_format': "Izvoz v Pages ni uspel: {0}",
        'export_word_success': "Izvoz v Word uspešen",
        'export_word_error': "Izvoz v Word ni uspel",
        'export_word_error_format': "Izvoz v Word ni uspel: {0}",
        'export_text_success': "Izvoz besedila uspešen",
        'export_text_error': "Izvoz besedila ni uspel",
        'export_text_error_format': "Izvoz besedila ni uspel: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Geslo je obvezno",
        'password_enter': "Vnesite geslo",
        'password_confirm': "Potrdite geslo",
        'password_new': "Novo geslo",
        'password_current': "Trenutno geslo",
        'password_save': "Shrani geslo (šifrirano)",
        'password_saved': "✓ Geslo za to datoteko je shranjeno",
        'password_wrong': "Napačno geslo",
        'password_mismatch': "Gesli se ne ujemata",
        'password_too_short': "Geslo je prekratko",
        'password_min_length': "Geslo mora vsebovati vsaj 4 znake",
        'password_strength': "Moč gesla",
        'password_strength_very_weak': "Zelo šibko",
        'password_strength_weak': "Šibko",
        'password_strength_medium': "Srednje",
        'password_strength_strong': "Močno",
        'password_strength_very_strong': "Zelo močno",
        'password_char_count': "({0} znakov)",
        'password_match': "✓ Ujemanje",
        'password_no_match': "✗ Gesli se ne ujemata",
        'password_show': "Pokaži",
        'password_hide': "Skrij",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Upravljanje gesel",
        'password_table_filename': "Ime datoteke",
        'password_table_password': "Geslo",
        'password_count': "{0} shranjenih gesel",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Ni shranjenih gesel",
        'password_copied': "{0} gesel kopiranih",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Ali res želite izbrisati geslo za '{0}'?",
        'password_delete_multiple': "Ali res želite izbrisati {0} izbranih gesel?",
        'password_delete_all_confirm': "Ali res želite izbrisati vseh {0} shranjenih gesel?",
        'password_deleted': "{0} gesel izbrisanih",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Vsa gesla so izbrisana",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generator gesel",
        'generator_generated': "Ustvarjeno geslo:",
        'generator_regenerate': "Ustvari znova",
        'generator_copy': "Kopiraj",
        'generator_use': "Uporabi",
        'generator_settings': "Nastavitve",
        'generator_length': "Dolžina:",
        'generator_group_every': "Ločilo vsakih",
        'generator_group_chars': "znakov.    Ločilo:",
        'generator_uppercase': "Velike črke (A-Z)",
        'generator_lowercase': "Male črke (a-z)",
        'generator_digits': "Številke (0-9)",
        'generator_symbols': "Posebni znaki (!@#$%^&*)",
        'generator_exclude': "Izključeno:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Zahtevano je glavno geslo",
        'master_password_setup': "Nastavi glavno geslo",
        'master_password_change': "Spremeni glavno geslo",
        'master_password_enter': "Vnesite svoje glavno geslo",
        'master_password_choose': "Izberite močno glavno geslo (vsaj 8 znakov)",
        'master_password_new': "Vnesite svoje novo glavno geslo",
        'master_password_confirm': "Potrdite geslo",
        'master_password_authenticate': "Avtenticiraj",
        'master_password_success': "Glavno geslo je bilo uspešno nastavljeno.",
        'master_password_changed': "Glavno geslo je bilo uspešno spremenjeno.",
        'master_password_removed': "Glavno geslo in vsa gesla so bila izbrisana.",
        'master_password_remove': "Odstrani glavno geslo",
        'master_password_remove_confirm': "Ali ste PREPRIČANI, da želite izbrisati VSA gesla?\n\nTo dejanje je NEPOVRATNO!",
        'master_password_export_before': "Ali želite pred tem izvoziti varnostno kopijo?",
        'master_password_export_delete': "Izvozi in izbriši",
        'master_password_delete_now': "Izbriši zdaj",
        'master_password_for_signatures': "Če želite uporabljati podpise, morate nastaviti glavno geslo.\n\nAli želite zdaj nastaviti glavno geslo?",
        'master_password_for_private': "Če želite uporabljati zasebne besedilne bloke, morate nastaviti glavno geslo.\n\nAli želite zdaj nastaviti glavno geslo?",
        'master_password_info': """
            <b>🔐 BREZ GLAVNEGA GESLA:</b><br>
            • Ni mogoče prikazovati, kopirati in izvažati gesel<br>
            • Brisanje gesel je vedno mogoče (tudi brez glavnega gesla)<br><br>

            <b>🔐 Z GLAVNIM GESLOM:</b><br>
            • Vse funkcije so na voljo po avtentikaciji<br>
            • Gesla so šifrirana z glavnim geslom<br>
            • Najmanjša dolžina: 8 znakov<br>
            • Varno shranjevanje zgoščene vrednosti SHA-256<br><br>

            <b>POMEMBNO:</b><br>
            • Če izgubite glavno geslo, gesel ni mogoče obnoviti<br>
            • Pri odstranitvi glavnega gesla se VSA gesla izbrišejo<br>
            • Pred brisanjem je na voljo možnost izvoza<br>
            • Glavno geslo lahko kadar koli spremenite
        """,
        'signature_auth_disabled': "Onemogoči zahtevo za geslo za podpise",
        'template_auth_disabled': "Onemogoči zahtevo za geslo za zasebne besedilne bloke",
        'master_password_for_signatures_settings': "Če želite uporabljati podpise, morate nastaviti glavno geslo.\n\nPojdite v Nastavitve - Upravljanje gesel",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Zaščiti PDF",
        'protect_info': "Datoteka '{0}' bo zaščitena z geslom.",
        'protect_instruction': "Dvakrat vnesite želeno geslo za zaščito dokumenta ali uporabite generator gesel desno od vnosnega polja.",
        'protect_success': "PDF je bil uspešno zaščiten in shranjen na:\n{0}\n\nGeslo: {1}\n\nAli želite zdaj odpreti zaščiteni PDF?",
        'protect_open': "Da",
        'protect_skip': "Ne",
        'protect_error': "Napaka pri zaščiti PDF",
        'protect_open_title': "odpri zaščiteni PDF",
        'protect_question': "Končano. Ali želite zdaj odpreti zaščiteni PDF? Da ali Ne?",
        'password_cancel': "Pogovorno okno za geslo je preklicano",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Izbriši strani",
        'pages_extract': "Izloči strani",
        'pages_insert': "Vstavi strani",
        'pages_move': "Premakni strani",
        'pages_delete_options': "Možnosti brisanja",
        'pages_delete_empty': "Izbriši vse prazne strani",
        'pages_delete_current': "Izbriši trenutno stran",
        'pages_delete_range': "Izbriši obseg strani",
        'pages_extract_options': "Možnosti izločanja",
        'pages_extract_current': "Izloči trenutno stran",
        'pages_extract_range': "Izloči obseg strani",
        'pages_insert_position': "Mesto vstavitve",
        'pages_insert_before': "Vstavi pred stran:",
        'pages_insert_select': "Izberi PDF",
        'pages_insert_none': "Ni izbranega PDF",
        'pages_move_source': "Strani za premik",
        'pages_move_from': "Od strani:",
        'pages_move_to': "Do strani:",
        'pages_move_target': "Ciljni položaj",
        'pages_move_before': "Premakni pred stran:",
        'pages_move_hint': "Opomba: stran 1 = začetek, {0} = konec",
        'pages_range_invalid': "Začetna stran mora biti manjša ali enaka končni strani.",
        'pages_position_invalid': "Ciljni položaj ne sme biti znotraj obsega, ki ga premikate.",
        'pages_no_pdf_selected': "Ni izbranega PDF.",
        'pages_deleted': "Izbrisanih je bilo {0} strani.",
        'pages_extracted': "Izločeno: {0}\nShranjeno na: {1}\nVelikost datoteke: {2:.1f} KB",
        'pages_inserted': "Vstavljenih {0} strani",
        'pages_moved': "Premaknjenih je bilo {0} strani.",
        'pages_deleted_none': "Nobena stran ni bila izbrisana.",
        'pages_delete_progress': "Brisanje strani...",
        'pages_deleted_with_backup': "Izbrisanih je bilo {0} strani.\n\nVarnostna kopija: {1}",
        'pages_deleted_voice': "Ustvarjena je bila varnostna kopija in izbrisanih {0} strani.",
        'info': "Informacija",
        'error_dialog_creation': "Pogovornega okna ni bilo mogoče ustvariti",
        'extract_page_single': "Izloči stran {0}",
        'extract_page_range': "Izloči strani {0}-{1}",
        'extract_success_voice': "Strani uspešno izločene",
        'extract_error_format': "Napaka pri izločanju: {0}",
        'pages_inserted_voice': "Vstavljenih {0} strani.",
        'insert_error_format': "Napaka pri vstavljanju: {0}",
        'pages_move_progress': "Premikanje strani...",
        'pages_moved_with_backup': "Premaknjenih {0} strani.\n\nVarnostna kopija: {1}",
        'move_success_title': "Uspešno premaknjeno",
        'pages_moved_voice': "{0} strani uspešno premaknjenih",
        'mark_removed': "Oznaka strani {0} odstranjena",
        'mark_empty': "Stran {0} označena kot prazna",
        'mark_export_removed': "Oznaka za izvoz strani {0} odstranjena",
        'mark_export': "Stran {0} označena za izvoz",
        'no_empty_pages': "Ni praznih strani, označenih za brisanje",
        'delete_empty_confirm': "Ali želite izbrisati vseh {0} označenih praznih strani?",
        'delete_empty_confirm_voice': "Ali naj zdaj izbrišem vseh {0} označenih praznih strani? Da ali Ne.",
        'empty_pages_deleted': "{0} praznih strani izbrisanih",
        'no_export_pages': "Ni strani, označenih za izvoz",
        'overwrite_title': "Prepiši obstoječo datoteko",
        'overwrite_question': "Datoteka\n\n{0}\n\nže obstaja.\nAli jo želite prepisati?",
        'overwrite_voice': "Prepišem obstoječo datoteko? Da ali Ne.",
        'page_skipped': "Stran {0} je bila preskočena",
        'export_complete': "Izvoz končan.",
        'export_complete_voice': "Izvoz je končan.",
        'no_pages_exported': "Nobena stran ni bila izvožena",
        'export_cancelled': "Izvoz preklican",
        'pages_exported': "{0} strani izvoženih v {1}",
        'export_page_title': "Izvozi stran",
        'page_exported': "Stran {0} izvožena v {1}",
        'export_error': "Napaka pri izvozu",
        'export_marked_title': "Izvozi označene strani",
        'rotate_all_title': "zasukaj vse strani",
        'rotate_all_question': "Ali želite zasukati vse strani za 90 stopinj v desno?",
        'rotate_all_voice': "Ali želite zasukati vse strani za 90 stopinj v desno? Da ali Ne?",
        'all_pages_rotated': "Vse strani zasukane",
        'page_rotated': "Stran {0} zasukana",
        'rotate_error': "Strani ni bilo mogoče zasukati",
        'delete_page_confirm': "Ali želite izbrisati stran {0}?",
        'delete_page_confirm_voice': "Ali res želite izbrisati stran {0}? Da ali Ne.",
        'page_deleted': "Stran {0} izbrisana",
        'delete_error': "Strani ni bilo mogoče izbrisati",
        'pages_deleted_voice': "{0} strani izbrisanih",
        'pages_exported_split': "{0} strani je bilo uspešno izvoženih.",
        'pages_skipped': "{0} strani je bilo preskočenih.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Izloči strani (napredno)",
        'pdf_splitter_title': "Razdelilnik in izločevalnik PDF",
        'pdf_splitter_load': " Izberi datoteko PDF",
        'pdf_splitter_info': "Izberite možnost za svoj dokument PDF",
        'pdf_splitter_basic': "Osnovne operacije",
        'pdf_splitter_single': "Razdeli na posamezne strani",
        'pdf_splitter_range': "Izloči strani:",
        'pdf_splitter_range_placeholder': "npr. 1-3,5,7-9",
        'pdf_splitter_clean': "Operacije čiščenja",
        'pdf_splitter_remove_empty': "Odstrani vse prazne strani",
        'pdf_splitter_remove': "Izbriši obseg strani:",
        'pdf_splitter_remove_placeholder': "npr. 2,4-6",
        'pdf_splitter_process': "Obdelaj PDF",
        'pdf_splitter_loaded': "PDF naložen. Izberite možnost",
        'pdf_read_error': "PDF ni bilo mogoče prebrati",
        'pages': "Strani",
        'pages_created': "Strani ustvarjene",
        'range_empty': "Vnesite obseg strani",
        'range_invalid': "Neveljaven obseg strani",
        'range_created': "Ustvarjen je bil nov PDF z izbranimi stranmi:\n{0}",
        'empty_removed': "{0} praznih strani odstranjenih.\nIzhod: {1}",
        'remove_empty': "Vnesite strani za odstranitev",
        'remove_invalid': "Neveljavne strani za odstranitev",
        'remove_done': "Ustvarjen očiščen PDF:\n{0}",
        'open_folder': "Odpri mapo",
        'show_in_finder': "Pokaži v Finderju",
        'pdf_splitter_no_pdf': "Najprej naložite datoteko PDF.",
        'process_error': "Napaka pri obdelavi PDF",
        'pages_created_voice': "{0} strani ustvarjenih",
        'range_created_voice': "Ustvarjen PDF z izbranimi stranmi",
        'empty_removed_voice': "{0} praznih strani odstranjenih",
        'remove_done_voice': "Ustvarjen očiščen PDF",
        'pdf_splitter_split_groups': "Vsako neprekinjeno skupino v ločeno datoteko",
        'range_created_single': "Ustvarjen nov PDF:\n{0}",
        'range_created_multiple': "Ustvarjenih {0} datotek PDF.",
        'range_created_voice_single': "Ustvarjen en PDF z izbranimi stranmi",
        'range_created_voice_multiple': "Ustvarjenih {0} datotek PDF",
        'empty_removed_none_left': "Ni preostalih strani",
        'empty_removed_all_empty': "Vse strani so bile prepoznane kot prazne in bi bile odstranjene. Nobena datoteka ni bila ustvarjena.",
        'preview_single': "Predogled: {0}",
        'preview_enter_range': "Vnesite obseg strani.",
        'preview_invalid_range': "Neveljaven obseg strani.",
        'preview_file': "Predogled: {0}",
        'preview_files': "Predogled: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Začetek tiskanja",
        'print_sent': "Tiskalno opravilo poslano",
        'print_now': "Natisni takoj",
        'print_error': "Napaka pri takojšnjem tiskanju",
        'print_limited': "Funkcija tiskanja je na tem sistemu omejena",
        'print_error_format': "Napaka pri takojšnjem tiskanju: {0}",
        'warning': "Opozorilo",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Preklopi na svetli način",
        'mode_switch_to_dark': "Preklopi na temni način",
        'mode_dark_activated': "Temni način aktiviran",
        'mode_light_activated': "Svetli način aktiviran",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Celoten pogled",
        'zoom_two_pages': "Dve strani druga poleg druge",
        'zoom_overview': "Način pregleda",
        'zoom_cannot_during_search': "Med iskanjem povečava ni mogoča",
        'zoom_exit_first': "Najprej zapustite povečavo",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Povleci in spusti omogočeno",
        'drag_disabled': "Povleci in spusti onemogočeno",
        'drag_page_grab': "Stran {0} prijeta",
        'drag_page_dropped': "Stran {0} vstavljena na položaj {1}",
        'drag_position_invalid': "Neveljaven položaj",
        'drag_same_position': "Stran {0} ostaja na položaju {0}",
        'drag_error': "Napaka pri premikanju",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Vnos besedila z naprednim oblikovanjem in upravljanjem besedilnih blokov",
        'text_templates': "Razpoložljivi besedilni bloki:",
        'text_name': "Ime",
        'text_preview': "Predogled besedila",
        'text_enter': "Besedilo:",
        'text_font_size': "Velikost pisave:",
        'text_formatting': "Oblikovanje:",
        'text_bold': "Krepko",
        'text_italic': "Ležeče",
        'text_underline': "Podčrtano",
        'text_alignment': "Poravnava:",
        'text_left': "Levo",
        'text_center': "Sredinsko",
        'text_right': "Desno",
        'text_color': "Barva besedila:",
        'text_opacity': "Prosojnost:",
        'text_word_wrap': "Prelom vrstic:",
        'text_auto': "Samodejno",
        'text_page_width_95': "Širina strani (95%)",
        'text_page_width_85': "Zelo široko (85%)",
        'text_page_width_75': "Širše (75%)",
        'text_page_width_60': "Široko (60%)",
        'text_page_width_50': "Srednje (50%)",
        'text_page_width_30': "Ozko (30%)",
        'text_page_width_20': "Ožje (20%)",
        'text_page_width_10': "Zelo ozko (10%)",
        'text_no_wrap': "Brez preloma",
        'text_private': "Zasebni besedilni blok (zahteva avtentikacijo)",
        'text_preview_label': "Predogled:",
        'text_preview_placeholder': "Tukaj bo prikazan predogled besedila...",
        'text_no_text': "(Ni besedila)",
        'text_save_template': "💾 Shrani kot blok",
        'text_delete_template': "🗑 Izbriši izbrani besedilni blok",
        'text_show_private': "Pokaži zasebne",
        'text_hide_private': "Skrij zasebne",
        'text_use': "✅ Uporabi besedilo",
        'text_saved': "Besedilni blok shranjen kot:\n{0}",
        'text_saved_voice': "Besedilni blok shranjen",
        'text_deleted': "Besedilni blok izbrisan",
        'text_no_text_to_save': "Ni besedila za shranjevanje.",
        'text_no_templates': "Ni najdenih besedilnih blokov",
        'text_private_master_required': "Zasebne bloke je mogoče uporabljati le, če je nastavljeno glavno geslo.\n\nAli želite zdaj nastaviti glavno geslo?",
        'text_filename': "Ime datoteke za besedilni blok (brez 'Text_' in '.txt'):",
        'text_filename_hint': "Primer: 'Telefon DomačaPisarna' bo shranjeno kot 'Text_Telefon DomačaPisarna.txt'",
        'text_save_hint': "Besedilni blok bo samodejno shranjen z oblikovanjem.",
        'text_guide_title': "Vnos besedila – Navodila",
        'text_delete_confirm': "Ali res želite izbrisati besedilni blok?\n\nDatoteka: {0}\nBesedilo: {1}...",
        'text_make_public': "Označi kot javno",
        'text_make_private': "Označi kot zasebno",
        'text_privacy_changed': "Status zasebnosti spremenjen",
        'text_private_always': "Zasebni vedno vidni (nastavitev)",
        'text_mode_required': "Najprej omogočite način besedila",
        'text_continue_editing': "Nadaljuj urejanje – kazalka na koncu besedila",
        'text_no_input': "Ni vnesenega besedila – besedilo zavrženo",
        'save_dialog_question': "Kako želite nadaljevati?",
        'text_save_question': "Shrani vsa besedila in križce, prilagodi, nadaljuj urejanje ali zavrzi?",
        'copy_cross': "Križec kopiran",
        'paste_cross': "Križec prilepljen",
        'paste_text': "Besedilo prilepljeno",
        'cross_discarded': "Križec zavržen",
        'all_discarded': "Vse zavrženo",
        'text_discarded': "Besedilo zavrženo",
        'no_texts_to_save': "Ni besedil za shranjevanje",
        'no_valid_texts': "Ni veljavnih besedil za shranjevanje",
        'text_word_singular': "besedilo",
        'text_word_plural': "besedila",
        'cross_word_singular': "križec",
        'cross_word_plural': "križci",
        'texts_saved_title': "Besedila shranjena",
        'texts_crosses_saved': "{0} {1} in {2} {3} je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'texts_crosses_saved_voice': "{0} {1} in {2} {3} shranjenih.",
        'texts_saved': "{0} {1} je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'texts_saved_voice': "{0} {1} shranjenih.",
        'crosses_saved': "{0} {1} je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'crosses_saved_voice': "{0} {1} shranjenih.",
        'elements_saved': "{0} elementov je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'elements_saved_voice': "{0} elementov shranjenih.",
        'text_window_load_error': "Okna za besedilo ni bilo mogoče naložiti",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Vnos besedila in besedilni bloki – Podrobna navodila**

        **1. Vstavljanje in urejanje besedila**
        - Z desno miškino tipko kliknite želeno mesto v dokumentu in izberite "Vstavi besedilo".
        - Odpre se pogovorno okno, v katerem lahko vnesete in oblikujete besedilo:
        • Velikost pisave, krepko, ležeče, podčrtano
        • Barva besedila (poljubna)
        • Prosojnost (neprosojnost) z drsnikom
        • Prelom vrstic (različne širine, npr. širina strani, ozko, brez preloma)
        - Po potrditvi se besedilo prikaže na mestu klika. Premikate ga lahko z miško ali puščičnimi tipkami.
        - Dvoklik na besedilo odpre način urejanja; ESC ga zapre.

        **2. Upravljanje besedilnih blokov (predlog)**
        - V pogovornem oknu za besedilo na levi strani vidite seznam vseh shranjenih besedilnih blokov.
        - **Shranjevanje bloka:** Vnesite besedilo, ga oblikujte in kliknite "💾 Shrani kot blok". Vnesite ime datoteke (brez končnice).
        - **Nalaganje bloka:** Kliknite želeno ime na seznamu. Besedilo in oblikovanje se prevzameta in ju lahko po potrebi prilagodite.
        - **Brisanje:** Z desno miškino tipko kliknite blok, da ga izbrišete ali spremenite njegov status zasebnosti.

        **3. Zasebni besedilni bloki (glavno geslo)**
        - Če ste nastavili glavno geslo (v Nastavitve → Upravljanje gesel), lahko bloke označite kot "zasebne".
        - Pred shranjevanjem potrdite polje "Zasebni besedilni blok" v pogovornem oknu.
        - Zasebni bloki so prikazani na seznamu le, če ste enkrat na sejo vnesli svoje glavno geslo (avtentikacija prek ikone ključavnice ali ob prvem dostopu).
        - Tako lahko zaupne besedilne bloke zaščitite pred nepooblaščenim dostopom.

        **4. Vstavljanje križcev**
        - V kontekstnem meniju lahko vstavite tudi grafični križec (npr. za potrditvena polja).
        - Velikost, debelino črte in barvo križcev lahko globalno prilagodite v nastavitvah (meni "Nastavitve" → "Nastavitve križcev").
        - Z desno miškino tipko kliknite obstoječi križec, da ga posamično spremenite.

        **5. Skupinska dejanja**
        - Če ste na eno stran postavili več besedil ali križcev, jih lahko vse hkrati shranite ali zavržete iz kontekstnega menija (desni klik v načinu besedila).
        - Pri shranjevanju se vsi elementi vdelajo v PDF in ostanejo kot vektorska grafika.

        **6. Tipkovne bližnjice v načinu besedila**
        - Puščične tipke: premikanje elementa
        - Ctrl+puščične tipke: večji koraki
        - Enter: odpre pogovorno okno za shranjevanje (shrani vse / prilagodi / zavrzi)
        - ESC: zavrže trenutni element
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Vnos besedila in besedilni bloki – Podrobna navodila</strong></p>

        <p><strong>1. Vstavljanje in urejanje besedila</strong></p>
        <ul>
        <li>Z desno miškino tipko kliknite želeno mesto v dokumentu in izberite "Vstavi besedilo".</li>
        <li>Odpre se pogovorno okno, v katerem lahko vnesete in oblikujete besedilo:<br/>
        • Velikost pisave, krepko, ležeče, podčrtano<br/>
        • Barva besedila (poljubna)<br/>
        • Prosojnost (neprosojnost) z drsnikom<br/>
        • Prelom vrstic (različne širine, npr. širina strani, ozko, brez preloma)</li>
        <li>Po potrditvi se besedilo prikaže na mestu klika. Premikate ga lahko z miško ali puščičnimi tipkami.</li>
        <li>Dvoklik na besedilo odpre način urejanja; ESC ga zapre.</li>
        </ul>

        <p><strong>2. Upravljanje besedilnih blokov (predlog)</strong></p>
        <ul>
        <li>V pogovornem oknu za besedilo na levi strani vidite seznam vseh shranjenih besedilnih blokov.</li>
        <li><strong>Shranjevanje bloka:</strong> Vnesite besedilo, ga oblikujte in kliknite "💾 Shrani kot blok". Vnesite ime datoteke (brez končnice).</li>
        <li><strong>Nalaganje bloka:</strong> Kliknite želeno ime na seznamu. Besedilo in oblikovanje se prevzameta in ju lahko po potrebi prilagodite.</li>
        <li><strong>Brisanje:</strong> Z desno miškino tipko kliknite blok, da ga izbrišete ali spremenite njegov status zasebnosti.</li>
        </ul>

        <p><strong>3. Zasebni besedilni bloki (glavno geslo)</strong></p>
        <ul>
        <li>Če ste nastavili glavno geslo (v Nastavitve → Upravljanje gesel), lahko bloke označite kot "zasebne".</li>
        <li>Pred shranjevanjem potrdite polje "Zasebni besedilni blok" v pogovornem oknu.</li>
        <li>Zasebni bloki so prikazani na seznamu le, če ste enkrat na sejo vnesli svoje glavno geslo (avtentikacija prek ikone ključavnice ali ob prvem dostopu).</li>
        <li>Tako lahko zaupne besedilne bloke zaščitite pred nepooblaščenim dostopom.</li>
        </ul>

        <p><strong>4. Vstavljanje križcev</strong></p>
        <ul>
        <li>V kontekstnem meniju lahko vstavite tudi grafični križec (npr. za potrditvena polja).</li>
        <li>Velikost, debelino črte in barvo križcev lahko globalno prilagodite v nastavitvah (meni "Nastavitve" → "Nastavitve križcev").</li>
        <li>Z desno miškino tipko kliknite obstoječi križec, da ga posamično spremenite.</li>
        </ul>

        <p><strong>5. Skupinska dejanja</strong></p>
        <ul>
        <li>Če ste na eno stran postavili več besedil ali križcev, jih lahko vse hkrati shranite ali zavržete iz kontekstnega menija (desni klik v načinu besedila).</li>
        <li>Pri shranjevanju se vsi elementi vdelajo v PDF in ostanejo kot vektorska grafika.</li>
        </ul>

        <p><strong>6. Tipkovne bližnjice v načinu besedila</strong></p>
        <ul>
        <li>Puščične tipke: premikanje elementa</li>
        <li>Ctrl+puščične tipke: večji koraki</li>
        <li>Enter: odpre pogovorno okno za shranjevanje (shrani vse / prilagodi / zavrzi)</li>
        <li>ESC: zavrže trenutni element</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Nastavitve križcev",
        'cross_properties': "Lastnosti križca",
        'cross_size': "Velikost (px):",
        'cross_line_width': "Debelina črte:",
        'cross_color': "Barva:",
        'cross_choose_color': "Izberi",
        'cross_fine_tuning': "Natančno uravnavanje pri shranjevanju (pikslov)",
        'cross_offset_x': "Odmik X:",
        'cross_offset_y': "Odmik Y:",
        'cross_offset_x_tooltip': "Negativne vrednosti premaknejo križec levo pri shranjevanju, pozitivne desno",
        'cross_offset_y_tooltip': "Negativne vrednosti premaknejo križec gor pri shranjevanju, pozitivne dol",
        'cross_preview': "Predogled",
        'cross_save': "Uveljavi nastavitve",
        'cross_customized': "Križec prilagojen",
        'cross_settings_applied': "Nastavitve križcev shranjene.\nVelikost: {0}px, debelina črte: {1}px\n{2}",
        'cross_updated_count': "{0} obstoječih križcev posodobljenih.",
        'cross_no_crosses': "Ni najdenih obstoječih križcev.",
        'cross_settings_applied_all': "Nastavitve križcev uporabljene za vseh {0} križcev",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Nastavitve podpisov",
        'signature_1': "Podpis 1",
        'signature_2': "Podpis 2",
        'signature_select': "Izberi podpis",
        'signature_add': "➕ Dodaj nov podpis...",
        'signature_size': "Velikost za podpis {0} (%):",
        'signature_common': "Splošne nastavitve",
        'signature_timestamp': "Samodejno dodaj časovni žig",
        'signature_location': "Privzeta lokacija:",
        'signature_timestamp_size': "Velikost pisave časovnega žiga:",
        'signature_no_files': "-- Ni najdenih podpisov --",
        'signature_insert': "Vstavi podpis",
        'signature_insert_1': "Vstavi podpis 1",
        'signature_insert_2': "Vstavi podpis 2",
        'signature_customize': " Prilagodi podpis",
        'signature_discard': " Zavrzi ta podpis",
        'signature_save_all': " Shrani vse podpise",
        'signature_discard_all': " Zavrzi vse podpise",
        'signature_guide_title': "Podpisi – Navodila",
        'signature_guide': """
📝 Podpisi – Kratka navodila

- Nastavite glavno geslo
- Konfigurirajte podpise v meniju Nastavitve
  (velikost, časovni žig ...)
- Vstavite z DESNIM KLIKOM na želenem mestu
  (glavno geslo potrebno enkrat na sejo)
- Podpis premikajte z miško ali puščičnimi tipkami
- Več podpisov lahko vstavite zaporedoma
- Vsak podpis lahko prilagodite posamično
- Zavrzite posamezen podpis
- Shranite / zavrzite vse podpise hkrati
- Lahko uporabite tudi menijsko vrstico.
        """,
        'signature_placeholder': "Predogled ni na voljo",
        'signature_info': "Podpis {0}: {1}×{2} px ({3}% od {4}×{5})",
        'signature_info_placeholder': "Nastavitve za podpis {0}",
        'signature_inserted': "Podpis {0} vstavljen na stran {1}",
        'signature_deleted': "Podpis izbrisan",
        'signature_copied': "Podpis kopiran",
        'signature_pasted': "Podpis {0} prilepljen",
        'signature_saved': "{0} podpisov je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'signature_saved_voice': "{0} podpisov shranjenih",
        'mode_replace_signature_format': "Zapusti način in vstavi podpis {0}",
        'mode_conflict_voice_signature': "Način {0} je aktiven. Ali naj zapustim in vstavim podpis?",
        'signature_not_configured': "Podpis {0} ni konfiguriran",
        'signature_file_not_found': "Datoteke podpisa ni mogoče najti",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Ni kopiranega podpisa",
        'no_signatures_to_save': "Ni podpisov za shranjevanje",
        'signature_save_question': "Shrani vse podpise, prilagodi ali zavrzi tega?",
        'signatures_saved_title': "Podpisi shranjeni",
        'signatures_saved': "{0} podpisov je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'signatures_saved_voice': "{0} podpisov shranjenih.",
        'all_signatures_discarded': "Vsi podpisi zavrženi",
        'signature_settings_saved': "Nastavitve podpisov shranjene",
        'signature_cancelled': "Podpis zavržen",
        'signature_active_title': "Podpis aktiven",
        'signature_replace_question': "Podpis je že aktiven.\n\nAli želite zamenjati trenutni podpis?",
        'signature_replace': "Zamenjaj podpis",
        'signature_replace_voice': "Zamenjaj trenutni podpis ali prekliči?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Nastavitve slik",
        'image_common': "Splošne nastavitve slik",
        'image_keep_aspect': "Ohrani razmerje stranic pri vlečenju",
        'image_default_size': "Privzeta velikost (%):",
        'image_dark_invert': "Invertiraj slike v temnem načinu",
        'image_dark_invert_tooltip': "Omogočeno: slike se invertirajo za boljšo vidljivost",
        'image_fine_tuning': "Natančno uravnavanje (pikslov)",
        'image_offset_x': "Odmik X:",
        'image_offset_y': "Odmik Y:",
        'image_offset_x_tooltip': "Negativne vrednosti premaknejo sliko levo pri shranjevanju, pozitivne desno",
        'image_offset_y_tooltip': "Negativne vrednosti premaknejo sliko gor pri shranjevanju, pozitivne dol",
        'image_select': "Izberi sliko",
        'image_insert': "Vstavi sliko",
        'image_customize': " Prilagodi sliko",
        'image_aspect': " Ohrani razmerje stranic",
        'image_discard': " Zavrzi to sliko",
        'image_save_all': " Shrani vse slike",
        'image_discard_all': " Zavrzi vse slike",
        'image_filter': "Slike",
        'image_guide_title': "Vstavljanje slik – Navodila",
        'image_guide': """
📷 Vstavljanje slik v PDF – Kratka navodila:

1. Z desno miškino tipko kliknite želeno mesto
2. "Vstavi sliko" → izberite sliko
3. Postavite sliko: povlecite z miško
4. Prilagodite velikost: povlecite za vogale/robove
5. Ohrani razmerje stranic: tipka [A]
6. Dodatne prilagoditve: desni klik na sliko

Nasvet: V kontekstnem meniju lahko prilagodite nastavitve.
        """,
        'image_inserted': "Slika vstavljena na stran {1}",
        'image_deleted': "Slika zavržena",
        'image_copied': "Slika kopirana",
        'image_pasted': "Slika prilepljena",
        'image_saved': "{0} slik je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'image_saved_voice': "{0} slik shranjenih",
        'image_aspect_on': "vklopljeno",
        'image_aspect_off': "izklopljeno",
        'image_aspect_toggle': "Ohrani razmerje stranic {0}",
        'image_reset': "Slika povrnjena na prvotno velikost",
        'image_replaced': "Slika zamenjana",
        'image_invalid': "Neveljavna slika",
        'mode_replace_image': "Vstavi sliko",
        'mode_conflict_voice_image': "Način {0} je aktiven. Ali naj zapustim in vstavim sliko?",
        'image_active_title': "Slika aktivna",
        'image_replace_question': "Slika je že aktivna.\n\nAli želite zamenjati trenutno sliko?",
        'image_replace': "Zamenjaj sliko",
        'image_replace_voice': "Zamenjaj trenutno sliko ali prekliči?",
        'image_filter_all': "Slike (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Vse datoteke (*.*)",
        'no_copied_image': "Ni kopirane slike",
        'image_discarded': "Slika zavržena",
        'image_save_question': "Shrani vse slike, prilagodi ali zavrzi to?",
        'no_images_to_save': "Ni slik za shranjevanje",
        'no_valid_images': "Ni veljavnih slik za shranjevanje",
        'images_saved_title': "Slike shranjene",
        'images_saved': "{0} slik je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'images_saved_voice': "{0} slik shranjenih.",
        'all_images_discarded': "Vse slike zavržene",
        'image_settings_updated': "Nastavitve slik posodobljene",
        'image_replace_title': "Izberi novo sliko",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Nastavitve oblik",
        'form_basic': "Osnovne nastavitve",
        'form_default_type': "Privzeta vrsta oblike:",
        'form_rectangle': "Pravokotnik",
        'form_ellipse': "Elipsa",
        'form_line': "Črta",
        'form_arrow': "Puščica",
        'form_line_width': "Debelina črte:",
        'form_colors': "Barve",
        'form_line_color': "Barva črte:",
        'form_fill_color': "Barva polnila:",
        'form_choose_color': "Izberi",
        'form_transparent': "Prosojno ozadje (samo črta)",
        'form_filled': "polnjeno",
        'form_dark_mode': "Temni način",
        'form_dark_invert': "Invertiraj barve v temnem načinu",
        'form_fine_tuning': "Natančno uravnavanje (pikslov)",
        'form_offset_x': "Odmik X:",
        'form_offset_y': "Odmik Y:",
        'form_offset_x_tooltip': "Negativne vrednosti premaknejo obliko levo pri shranjevanju, pozitivne desno",
        'form_offset_y_tooltip': "Negativne vrednosti premaknejo obliko gor pri shranjevanju, pozitivne dol",
        'form_preview': "Predogled",
        'form_insert': "Vstavi obliko",
        'form_rectangle_insert': "Pravokotnik",
        'form_ellipse_insert': "Elipsa/krog",
        'form_line_insert': "Črta (2 klika)",
        'form_arrow_insert': "Puščica (2 klika)",
        'form_customize': " Prilagodi obliko",
        'form_transparent_toggle': " Prosojno ozadje",
        'form_discard': " Zavrzi to obliko",
        'form_save_all': " Shrani vse oblike",
        'form_discard_all': " Zavrzi vse oblike",
        'form_guide_title': "Vstavljanje oblik – Navodila",
        'form_guide': """
📐 Vstavljanje oblik v PDF – Kratka navodila:

1. Izberite vrsto oblike (pravokotnik, elipsa, črta, puščica)
2. Kliknite na mesto
   - Pravokotnik/elipsa: en klik postavi obliko
   - Črta/puščica: dva klika za začetno in končno točko
3. Postavite obliko: povlecite z miško
4. Prilagodite velikost: povlecite za vogale/robove
5. Shrani obliko: Enter
6. Zavrzi obliko: ESC
7. Dodatne prilagoditve: desni klik na obliko

Nasvet: V kontekstnem meniju lahko prilagodite nastavitve.
        """,
        'form_inserted': "{0} vstavljen/a na stran {1}",
        'form_deleted': "Oblika izbrisana",
        'form_copied': "Oblika kopirana",
        'form_pasted': "Oblika prilepljena",
        'form_saved': "{0} oblik je bilo vstavljenih v PDF.\n\nPDF je bil ponovno naložen...",
        'form_saved_voice': "{0} oblik shranjenih",
        'form_reset': "Oblika povrnjena na privzeto velikost",
        'form_transparent_on': "vklopljeno",
        'form_transparent_off': "izklopljeno",
        'form_transparent_toggled': "Prosojno ozadje {0}",
        'form_line_cancel': "Risanje črte preklicano",
        'form_second_click': "Zdaj kliknite končno točko za {0}",
        'mode_replace_form': "Vstavi obliko",
        'mode_conflict_voice_form': "Način {0} je aktiven. Ali naj zapustim in vstavim obliko?",
        'form_settings_updated': "Nastavitve oblik posodobljene",
        'form_unknown': "Oblika",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Kliknite začetno točko",
        'form_line_guide_2': "2. Kliknite končno točko",
        'form_line_guide_3': "Črta bo narisana med obema točkama.",
        'form_line_status_1': "Čakanje na prvi klik...",
        'form_line_status_2': "Prva točka nastavljena: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Zdaj kliknite končno točko...",
        'form_line_status_4': "Obe točki nastavljeni.\nKliknite 'Končano' za shranjevanje.",
        'form_line_reset': "Ponastavi",
        'form_line_finish': "Končano",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopiraj (Cmd+C)",
        'paste': "Prilepi (Cmd+V)",
        'copied': "Kopirano: {0}",
        'no_element_to_copy': "Ni izbranega elementa za kopiranje",
        'no_copied_data': "Ni kopiranih podatkov",
        'no_valid_position': "Ni veljavnega mesta za lepljenje",
        'copy_text': "Besedilo kopirano",
        'copy_image': "Slika kopirana",
        'copy_form': "Oblika kopirana",
        'copy_signature': "Podpis kopiran",
        'element_text': "Besedilo",
        'element_image': "Slika",
        'element_form': "Oblika",
        'element_signature': "Podpis",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflikt načinov",
        'mode_conflict_message': "Način '{0}' je že aktiven.\n\nAli želite zapustiti ta način in {1}?",
        'mode_replace': "Zapusti način in {0}",
        'mode_cancel': "Prekliči",
        'mode_replace_text': "vstavi besedilo",
        'mode_replace_cross': "vstavi križec",
        'mode_replace_signature': "vstavi podpis",
        'mode_replace_image': "vstavi sliko",
        'mode_replace_form': "vstavi obliko",
        'mode_conflict_voice': "Način {0} je aktiven. Ali naj zapustim in vstavim besedilo?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Vnos besedila",
        'active_mode_signature': "Podpis",
        'active_mode_image': "Slika",
        'active_mode_form': "Oblika",
        'active_mode_and': " in ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Vstavi",
        'insert_another_text': "Vstavi besedilo",
        'insert_another_cross': "Vstavi križec",
        'insert_another_signature_1': "Podpis 1",
        'insert_another_signature_2': "Podpis 2",
        'insert_another_image': "Vstavi sliko",
        'insert_another_form_rect': "Pravokotnik",
        'insert_another_form_ellipse': "Elipsa",
        'insert_another_form_line': "Črta (2 klika)",
        'insert_another_form_arrow': "Puščica (2 klika)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Shrani {0}",
        'save_dialog_message': "{0} bo shranjen/a na stran {1}.\n\nKako želite nadaljevati?",
        'save_all': "Shrani vse {0}",
        'save_single': "Shrani {0}",
        'save_customize': "Prilagodi {0}",
        'save_discard': "Zavrzi ta/tale {0}",
        'save_continue': "Nadaljuj urejanje",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Pojdi na stran {0}",
        'context_rotate': " Zasukaj stran {0}",
        'context_delete': " Izbriši stran {0}",
        'context_export': " Izvozi stran {0}",
        'context_mark_as': " Označi stran kot...",
        'context_mark_empty': " Prazna stran",
        'context_unmark_empty': " Ni več prazna",
        'context_mark_export': " Označi za izvoz",
        'context_unmark_export': " Ne izvozi več",
        'context_batch_actions': " Skupinska dejanja",
        'context_batch_delete_empty': " Izbriši vseh {0} praznih strani",
        'context_batch_export_single': " Izvozi vseh {0} strani (ena datoteka)",
        'context_batch_export_split': " Izvozi vseh {0} strani (ločeno)",
        'context_drag_start': " Začni povleci in spusti",
        'context_drag_stop': " Ustavi povleci in spusti",
        'context_insert': " Vstavi",
        'context_insert_pages': " Vstavi strani",
        'context_zoom': "Povečava",
        'discard_mixed': "Zavrzi vseh {0} {1} in {2} {3}",
        'save_mixed': "Shrani {0} {1} in {2} {3}",
        'discard_texts': "Zavrzi vseh {0} besedil",
        'discard_text_single': "Zavrzi 1 besedilo",
        'save_texts': "Shrani {0} besedil",
        'save_text_single': "Shrani 1 besedilo",
        'discard_crosses': "Zavrzi vseh {0} križcev",
        'discard_cross_single': "Zavrzi 1 križec",
        'save_crosses': "Shrani {0} križcev",
        'save_cross_single': "Shrani 1 križec",
        'discard_signatures': "Zavrzi vseh {0} podpisov",
        'save_signature_single': "Shrani 1 podpis",
        'save_signatures': "Shrani {0} podpisov",
        'discard_images': "Zavrzi vseh {0} slik",
        'save_image_single': "Shrani 1 sliko",
        'save_images': "Shrani {0} slik",
        'discard_forms': "Zavrzi vseh {0} oblik",
        'save_form_single': "Shrani 1 obliko",
        'save_forms': "Shrani {0} oblik",
        'cross_discard': "Zavrzi ta križec",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informacije o izvozu / uvozu",
        'export_what': "📋 Kaj se izvozi?",
        'export_general': "Splošne nastavitve",
        'export_general_items': "• Glasovni izhod (vklop/izklop, hitrost)\n• Temni/svetli način\n• Nastavitve varnostnega kopiranja\n• Nastavitve OCR",
        'export_image_form': "Nastavitve slik in oblik",
        'export_image_form_items': "• Nastavitve slik (razmerje stranic, privzeta velikost)\n• Nastavitve oblik (debelina črte, barve)\n• Nastavitve podpisov (poti, velikosti, časovni žig)",
        'export_passwords': "Podatkovna zbirka gesel",
        'export_passwords_items': "• Vsa shranjena gesla PDF\n• Izbirno šifrirana ali dešifrirana",
        'export_master': "Nastavitve glavnega gesla",
        'export_master_items': "• Zgoščena vrednost glavnega gesla\n• Nastavitve za podpise/besedilne bloke",
        'export_signatures': "Podpisi in besedilni bloki",
        'export_signatures_items': "• Vse slikovne datoteke (podpisi)\n• Vsi besedilni bloki z oblikovanjem\n• Oznake zasebno/javno",
        'export_import_warning': "⚠️ Pomembne opombe",
        'export_import_note': "• Pri uvozu se VSE trenutne nastavitve prepišejo\n• Zahtevan je ponovni zagon aplikacije\n• Obstoječi podpisi/besedilni bloki se zamenjajo",
        'export_master_note': "• Če je nastavljeno glavno geslo, lahko izberete:\n  - Dešifrirano (gesla v čisti obliki)\n  - Šifrirano (berljivo le z glavnim geslom)",
        'export_security': "• Izvožena datoteka ZIP vsebuje zaupne podatke\n• Hranite jo na varnem (npr. šifriranem USB-ključku)\n• Če datoteko izgubite, gesla ni mogoče obnoviti",
        'export_format': "📁 Format izvoza",
        'export_format_desc': "Nastavitve so shranjene v eni datoteki ZIP:",
        'export_filename': "Nastavitve_PDFDarkView_LLLLMMDD_HHMMSS.zip",
        'export_success': "Nastavitve so bile uspešno izvožene",
        'export_failed': "Izvoz ni uspel",
        'export_import_question': "Ali želite zdaj znova zagnati aplikacijo?",
        'export_password_question': "Nastavljeno je glavno geslo.\n\nAli želite izvoziti gesla dešifrirana?\n(sicer bodo izvožena šifrirana)",
        'export_decrypt': "Izvozi dešifrirano",
        'export_encrypt': "Izvozi šifrirano",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informacije",
        'info_title': "O PDF Dark View",
        'info_version': "Različica",
        'info_author': "Razvil Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "O programu",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> je dostopen PDF-pregledovalnik, razvit posebej za ljudi z okvaro vida.</p>

            <p><strong>Ključne značilnosti:</strong></p>
            <ul>
                <li>Kontrasten, prilagodljiv vmesnik</li>
                <li>Popoln nadzor s tipkovnico</li>
                <li>Vgrajen govorni izhod</li>
                <li>OCR za skenirane dokumente</li>
                <li>Obsežna orodja za urejanje</li>
            </ul>

            <p>Podprtih je več kot 50 jezikov – tako so PDF-ji dostopni vsem.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkcije",
        'info_features_intro': "PDF Dark View vam ponuja naslednje možnosti:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Prikaz in navigacija</strong> – Temni/Svetli način, listanje strani, zoom, skok na stran</li>
            <li><strong>OCR (prepoznavanje besedila)</strong> – Omogočite iskanje in kopiranje v skeniranih dokumentih</li>
            <li><strong>Urejanje</strong> – Vstavljanje besedila, križcev, podpisov, slik in oblik</li>
            <li><strong>Upravljanje strani</strong> – Brisanje, izločanje, vstavljanje, premikanje s povleci in spusti</li>
            <li><strong>Izvoz</strong> – V Word, Pages ali kot besedilo</li>
            <li><strong>Varnost</strong> – Zaščita in upravljanje z geslom</li>
            <li><strong>Dostopnost</strong> – Govorni izhod, nadzor s tipkovnico, visok kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Uporaba",
        'info_accessibility': "♿ Dostopnost – popoln nadzor s tipkovnico",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Splošno</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Odpri PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Išči</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Preklopi temni/svetli način</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Natisni</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Izhod</div>

        <div class="shortcut-cat">📖 Navigacija</div>
        <div class="shortcut-row"><kbd>Puščične tipke</kbd> Listaj stran za stranjo</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Pojdi na stran</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Prva stran</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Zadnja stran</div>

        <div class="shortcut-cat">✏️ Urejanje</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Vstavi besedilo</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Izbriši strani</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Izloči strani</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Vstavi strani</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Premakni strani</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Zavrti stran</div>

        <div class="shortcut-cat">🖼️ Premikanje elementov</div>
        <div class="shortcut-row"><kbd>Puščične tipke</kbd> Premakni besedilo/sliko/podpis</div>
        <div class="shortcut-row"><kbd>Ctrl+Puščične tipke</kbd> Večji koraki</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Shrani</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Zavrzi</div>

        <div class="shortcut-cat">🗣️ Govorni izhod</div>
        <div class="shortcut-row"><kbd>F2</kbd> Vklopi/izklopi govorni izhod</div>
        """,
        'info_contextmenu': "📌 Pomembno: Vse funkcije so dosegljive tudi prek kontekstnega menija (desni gumb miške)!",
        'info_accessibility_hint': "💡 Namig: Govorni izhod (F2) olajša orientacijo in daje povratne informacije o menijih in pogovornih oknih.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licenca & Impresum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUM</strong><br>
        Podatki v skladu z § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Nemčija<br>
        E-pošta: binhdiez64@gmail.com<br>
        Odgovoren za vsebino: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Izključitev odgovornosti</strong><br>
        Programska oprema je bila razvita z največjo skrbnostjo. Ne jamčimo za pravilnost, popolnost in funkcionalnost. Uporaba je na lastno odgovornost.<br><br>

        <strong>📄 Licenca MIT (zasebna uporaba)</strong><br>
        Avtorske pravice (c) 2026 Toralf Schulz (BinhDiez)<br>
        Dovoljeno: brezplačna uporaba, zasebne spremembe, osebne kopije.<br>
        Nedovoljeno: prodaja, komercialna uporaba, odstranitev obvestil o avtorskih pravicah.<br><br>

        <strong>🔧 Komponente tretjih oseb</strong><br>
        Ta programska oprema vsebuje komponente pod licencami GPL, AGPL, Apache 2.0, BSD in MIT.<br>
        Pri nadaljnjem razširjanju je treba upoštevati ustrezne pogoje licence.<br><br>

        <strong>🌐 Odprta koda</strong><br>
        Izvorna koda je na voljo in jo je mogoče pregledati, spreminjati in nadalje distribuirati v skladu z ustreznimi pogoji licence.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Zahvale",
        'info_credits': "Zahvala skupnosti odprte kode",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Obdelava PDF</li>
            <li><strong>PyQt5</strong> – Grafični vmesnik</li>
            <li><strong>Tesseract OCR</strong> – Prepoznavanje besedila</li>
            <li><strong>OCRmyPDF</strong> – Integracija OCR</li>
            <li><strong>python-docx</strong> – Izvoz v Word</li>
            <li><strong>qtawesome</strong> – Ikone</li>
            <li><strong>DeepSeek</strong> – Podpora pri prevodih (50+ jezikov)</li>
            <li><strong>Vsi uporabniki</strong> – Za dragocene povratne informacije</li>
            <li><strong>Skupnosti odprte kode</strong> – Za odlične knjižnice</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Jeziki",
        'info_languages_header': "🌍 Jezikovna podpora",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View trenutno podpira <strong>62 jezikov</strong> – tako da je programsko opremo mogoče uporabljati brez ovir po vsem svetu.</p>

            <p><strong>📖 Celoten seznam jezikov (Stanje: marec 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanščina (Shqip)</li>
                    <li>🇩🇿 Arabščina (العربية)</li>
                    <li>🇮🇩 Balijščina (Basa Bali)</li>
                    <li>🇧🇩 Bengalščina (বাংলা)</li>
                    <li>🇲🇲 Burmanščina (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosanščina (Bosanski)</li>
                    <li>🇧🇬 Bolgarščina (Български)</li>
                    <li>🇨🇳 Kitajščina (中文)</li>
                    <li>🇩🇰 Danščina (Dansk)</li>
                    <li>🇩🇪 Nemščina (Deutsch)</li>
                    <li>🇬🇧 Angleščina (English)</li>
                    <li>🇪🇪 Estonščina (Eesti)</li>
                    <li>🇫🇮 Finščina (Suomi)</li>
                    <li>🇫🇷 Francoščina (Français)</li>
                    <li>🇬🇷 Grščina (Ελληνικά)</li>
                    <li>🇮🇱 Hebrejščina (עברית)</li>
                    <li>🇮🇳 Hindijščina (हिन्दी)</li>
                    <li>🇭🇷 Hrvaščina (Hrvatski)</li>
                    <li>🇭🇺 Madžarščina (Magyar)</li>
                    <li>🇮🇩 Indonezijščina (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irščina (Gaeilge)</li>
                    <li>🇮🇸 Islandščina (Íslenska)</li>
                    <li>🇮🇹 Italijanščina (Italiano)</li>
                    <li>🇯🇵 Japonščina (日本語)</li>
                    <li>🇰🇭 Kmerščina (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korejščina (한국어)</li>
                    <li>🇱🇦 Laoščina (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvijščina (Latviešu)</li>
                    <li>🇱🇹 Litovščina (Lietuvių)</li>
                    <li>🇱🇺 Luksemburščina (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajščina (Bahasa Melayu)</li>
                    <li>🇮🇳 Maratščina (मराठी)</li>
                    <li>🇲🇳 Mongolščina (Монгол)</li>
                    <li>🇳🇵 Nepalščina (नेपाली)</li>
                    <li>🇳🇱 Nizozemščina (Nederlands)</li>
                    <li>🇳🇴 Norveščina (Norsk)</li>
                    <li>🇦🇫 Paštunščina (پښتو)</li>
                    <li>🇮🇷 Perzijščina (فارسی)</li>
                    <li>🇵🇱 Poljščina (Polski)</li>
                    <li>🇵🇹 Portugalščina (Português)</li>
                    <li>🇮🇳 Pandžabščina (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Romunščina (Română)</li>
                    <li>🇷🇺 Ruščina (Русский)</li>
                    <li>🇸🇪 Švedščina (Svenska)</li>
                    <li>🇷🇸 Srbščina (Српски)</li>
                    <li>🇸🇰 Slovaščina (Slovenčina)</li>
                    <li>🇸🇮 Slovenščina (Slovenščina)</li>
                    <li>🇪🇸 Španščina (Español)</li>
                    <li>🇹🇿 Svahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalogščina (Filipino)</li>
                    <li>🇮🇳 Tamilščina (தமிழ்)</li>
                    <li>🇮🇳 Telugujščina (తెలుగు)</li>
                    <li>🇹🇭 Tajščina (ไทย)</li>
                    <li>🇨🇿 Češčina (Čeština)</li>
                    <li>🇹🇷 Turščina (Türkçe)</li>
                    <li>🇺🇦 Ukrajinščina (Українська)</li>
                    <li>🇵🇰 Urdščina (اردو)</li>
                    <li>🇻🇳 Vietnamščina (Tiếng Việt)</li>
                    <li>🇸🇳 Volofščina (Wolof)</li>
                    <li>🇺🇸 Jidiš (ייִדיש)</li>
                    <li>🇿🇦 Zuluščina (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Dodajanje lastnih jezikov:</strong><br>
                Želite jezik, ki še ni vključen? Preprosto postavite svojo datoteko slovarja (<code>sprache_xx.py</code>) poleg aplikacije – programska oprema jo bo samodejno prepoznala. Če vas zanima poseben prevod, me kontaktirajte.
            </div>

            <p><strong>🙏 Posebna zahvala:</strong> DeepSeek-u za podporo pri prevodu vseh slovarjev v 62 jezikov.</p>

            <p>📧 Kontakt za prevode: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Napaka",
        'error_occurred': "Prišlo je do napake",
        'error_pdf_load': "Napaka pri nalaganju PDF",
        'error_pdf_save': "Napaka pri shranjevanju PDF",
        'error_ocr': "Napaka pri prepoznavanju besedila",
        'error_no_pdf': "Ni naloženega PDF",
        'error_page_not_found': "Strani ni mogoče najti",
        'error_invalid_range': "Neveljaven obseg strani",
        'error_file_not_found': "Datoteke ni mogoče najti",
        'error_permission': "Ni dovoljenja",
        'error_unknown': "Neznana napaka",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Uspeh",
        'success_operation': "Operacija uspešno zaključena",
        'success_saved': "Uspešno shranjeno",
        'success_exported': "Uspešno izvoženo",
        'success_imported': "Uspešno uvoženo",
        'success_deleted': "Uspešno izbrisano",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Potrditev",
        'confirm_yes': "Da",
        'confirm_no': "Ne",
        'confirm_ok': "V redu",
        'confirm_cancel': "Prekliči",
        'confirm_delete': "Izbriši",
        'confirm_overwrite': "Prepiši",
        'confirm_continue': "Nadaljuj",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Nalaganje PDF...",
        'progress_saving': "Shranjevanje PDF...",
        'progress_exporting': "Izvoz PDF...",
        'progress_processing': "Obdelava...",
        'progress_wait': "Prosimo, počakajte...",
        'progress_preparing': "Priprava...",
        'progress_finalizing': "Zaključevanje...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Bela",
        'color_black': "Črna",
        'color_red': "Rdeča",
        'color_green': "Zelena",
        'color_blue': "Modra",
        'color_yellow': "Rumena",
        'color_magenta': "Škrlatna",
        'color_cyan': "Cian",
        'color_orange': "Oranžna",
        'color_gray': "Siva",
        'color_custom': "Izbira barve",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Datoteka",
        'menu_edit': "&Uredi",
        'menu_view': "&Pogled",
        'menu_tools': "&Orodja",
        'menu_settings': "&Nastavitve",
        'menu_help': "&Pomoč",
        'menu_language': "🌐 Jezik",
        'menu_guides': "&Navodila",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Odpri",
        'file_save_as': "&Shrani kot...",
        'file_protect': "&Zaščiti dokument...",
        'file_export': "&Izvozi",
        'file_export_pages': "Izvozi v Pages",
        'file_export_word': "Izvozi v DOCX",
        'file_export_text': "Izvozi v TXT",
        'file_print_now': "&Natisni takoj",
        'file_print': "&Natisni",
        'file_close': "&Zapri",
        'file_quit': "&Izhod",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Išči",
        'edit_ocr': " Izvedi OCR",
        'edit_rotate': "&Zasukaj stran",
        'edit_rotate_all': "Zasukaj &vse strani",
        'edit_delete_pages': "&Izbriši strani",
        'edit_extract_pages': "&Izloči strani",
        'edit_insert_pages': "&Vstavi strani",
        'edit_move_pages': "&Premakni strani",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Vstavi besedilo in križce",
        'text_insert': " Vstavi besedilo",
        'cross_insert': " Vstavi križec",
        'text_customize': " Prilagodi besedilo",
        'cross_customize': " Prilagodi ta križec",
        'cross_customize_all': " Prilagodi vse križce",
        'text_discard': " Zavrzi to besedilo/križec",
        'text_discard_all': " Zavrzi vsa besedila in križce",
        'text_save_all': " Shrani vsa besedila in križce",
        'text_guide': " Vnos besedila / besedilni bloki – navodila",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Vstavi podpis",
        'signature_settings_menu': " Nastavitve...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Vstavi sliko",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Vstavi oblike",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Pokaži okno za besedilo",
        'view_zoom': "&Povečava",
        'view_zoom_page': "&Širina strani (privzeto)",
        'view_zoom_two': "&Dve strani",
        'view_zoom_overview': "&Pregled (več strani)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Dostopnost",
        'settings_voice': "Glasovni izhod",
        'settings_voice_tooltip': "dopolnjuje glasovni izhod bralnikov zaslona z dodatnimi informacijami",
        'settings_signature': "&Nastavitve podpisov",
        'settings_password': "&Upravljanje gesel",
        'settings_backup': "Ustvari varnostno kopijo pred spremembami",
        'settings_export_import': "&Izvozi nastavitve / uvozi nastavitve",
        'settings_export': "&Izvozi vse nastavitve...",
        'settings_import': "&Uvozi vse nastavitve...",
        'settings_export_info': "&Kaj se izvozi?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "vklopljeno",
        'voice_off': "izklopljeno",
        'voice_toggle': "Glasovni izhod {0}",
        'voice_speed': "Hitrost {0} odstotkov",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Orodja ni mogoče najti:\n{0}\n\nBASE_DIR: {1}\nPrepričajte se, da so orodja za PDF nameščena v imeniku {1}.",
        'tool_started': "{0} zagnano",
        'tool_start_failed': "Ni bilo mogoče zagnati",
        'process_error_failed_to_start': "Postopka ni bilo mogoče zagnati. Ali datoteka obstaja?",
        'process_error_crashed': "Postopek je med zagonom strmoglavil.",
        'process_error_timeout': "Dosežena je časovna omejitev postopka.",
        'process_error_write': "Napaka pri pisanju v postopek.",
        'process_error_read': "Napaka pri branju iz postopka.",
        'process_error_unknown': "Neznana napaka postopka",
        'process_command': "Ukaz",
        'process_normal_exit': "končano normalno",
        'process_crashed': "strmoglavilo",
        'process_nonzero_exit': "{0} se je končal s kodo napake {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Preklicujem...",
        'move_cancelling': "Preklicujem premikanje",
        'opening_pdf': "Odpiram PDF...",
        'loading_document': "Nalagam dokument...",
        'pdf_opened': "PDF odprt",
        'pages_found_moving': "Najdenih {0} strani, {1} za premik",
        'creating_backup': "Ustvarjam varnostno kopijo...",
        'backup_description': "Varnostno kopiranje izvirne datoteke...",
        'backup_saved_as': "Varnostna kopija shranjena kot: {0}",
        'error_format': "Napaka: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Iskanje ponastavljeno",
        'page_header_simple': "=== Stran {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Upravljanje gesel – Navodila",
        'password_guide_voice': "Navodila za upravljanje gesel. Preberite opombe.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Upravljanje gesel – Podrobna navodila</strong></p>

        <p><strong>1. Zaščita PDF z geslom</strong></p>
        <ul>
        <li>Ko odprete PDF, zaščiten z geslom, se prikaže pogovorno okno, v katerem lahko vnesete geslo.</li>
        <li>Geslo lahko shranite šifrirano, da ga vam ni treba vnašati vsakič (potrditveno polje „Shrani geslo“).</li>
        <li>Z gumbom „Odstrani geslo“ lahko ustvarite dešifrirano kopijo PDF in geslo odstranite iz podatkovne zbirke.</li>
        </ul>

        <p><strong>2. Glavno geslo</strong></p>
        <ul>
        <li>Glavno geslo ščiti dostop do vseh shranjenih gesel PDF.</li>
        <li><strong>Nastavitev:</strong> Pojdite na „Nastavitve → Upravljanje gesel → Nastavitve glavnega gesla“ in kliknite „Nastavi glavno geslo“. Izberite močno geslo (vsaj 8 znakov).</li>
        <li><strong>Spreminjanje:</strong> Po uspešni avtentikaciji lahko spremenite glavno geslo.</li>
        <li><strong>Odstranitev:</strong> Če odstranite glavno geslo, se VSA shranjena gesla nepreklicno izbrišejo. Pred tem lahko izvozite varnostno kopijo.</li>
        <li>Enkrat na sejo se morate avtenticirati z glavnim geslom, da pridobite dostop do zaščitenih funkcij (npr. prikazovanje gesel).</li>
        </ul>

        <p><strong>3. Upravljanje gesel (seznam)</strong></p>
        <ul>
        <li>V „Nastavitve → Upravljanje gesel“ se odpre tabela vseh shranjenih datotek PDF z njihovimi šifriranimi gesli.</li>
        <li><strong>Brez glavnega gesla:</strong> Lahko samo brišete vnose – gesla ostanejo skrita.</li>
        <li><strong>Z glavnim geslom (avtenticirano):</strong> Gesla lahko prikazujete, kopirate, izvažate in brišete.</li>
        <li><strong>Izvoz:</strong> Izberite obliko (JSON, CSV, TXT) in shranite seznam. Če je nastavljeno glavno geslo, se lahko odločite, ali se gesla izvozijo dešifrirana ali šifrirana.</li>
        <li><strong>Uvoz:</strong> Predhodno izvoženo datoteko ZIP (vse nastavitve) lahko ponovno uvozite prek „Nastavitve → Izvozi nastavitve / uvozi nastavitve“. Pozor: obstoječi podatki se prepišejo!</li>
        </ul>

        <p><strong>4. Generator gesel</strong></p>
        <ul>
        <li>V pogovornem oknu za geslo (npr. pri zaščiti PDF) je desno od vnosnega polja gumb s kocko 🎲.</li>
        <li>Kliknite ga, da odprete generator gesel. Nastavite lahko dolžino, nabor znakov (velike črke, male črke, številke, posebne znake) in ločilo za boljšo berljivost.</li>
        <li>Ustvarjeno geslo lahko neposredno uporabite in po potrebi kopirate.</li>
        </ul>

        <p><strong>5. Pomembne varnostne opombe</strong></p>
        <ul>
        <li>Shranjena gesla so šifrirana z AES-256. Ključ se izpelje iz vašega glavnega gesla (če je nastavljeno) ali iz fiksne vrednosti (brez glavnega gesla).</li>
        <li>Brez glavnega gesla so gesla sicer šifrirana, vendar je ključ vdelan v program – napadalec z dostopom do vaših datotek bi jih lahko dešifriral. Zato močno priporočamo uporabo glavnega gesla.</li>
        <li>Zbirka gesel se nahaja v datoteki `Data/passwords.json`. Redno ustvarjajte varnostne kopije, zlasti pred odstranitvijo glavnega gesla.</li>
        <li>Če izgubite glavno geslo, so vsa shranjena gesla nepreklicno izgubljena.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Način obračanja",
        'invert_mode_classic': "Klasičen (obrni vse barve)",
        'invert_mode_smart': "Pameten (obrni samo svetlost)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Prag sive lestvice",
        'gray_threshold_10': "10% (strog)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Privzeto)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (mehak)",
        'threshold_changed': "Prag nastavljen na {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Prag sive lestvice – Razlaga",
        'threshold_guide_text': "Prag sive lestvice določa, kateri piksli v pametnem temnem načinu veljajo za 'sive' in se obrnejo.\n\n"
                                "• Nizka vrednost (10%) obrne samo skoraj popolne odtenke sive – barvni elementi ostanejo popolnoma ohranjeni.\n"
                                "• Visoka vrednost (50%) obrne tudi rahlo obarvane piksle – to poveča kontrast, lahko pa popači barve.\n\n"
                                "Optimalna vrednost je odvisna od dokumenta. Za čiste besedilne dokumente je 30–40% pogosto idealno, za barvno grafiko raje 10–20%.\n\n"
                                "Vrednost lahko kadar koli prilagodite prek menija 'Nastavitve' – PDF se bo takoj znova naložil.\n\n"
                                "Opomba:\n* Fotografije in slike je mogoče pravilno prikazati samo v svetlem načinu!\n* Nastavitve obračanja so prikazane samo, ko je aktiviran temni način.",
        'threshold_guide_voice': "Prag sive lestvice določa, kako močno poseže pametni temni način. Nizka vrednost varčuje barve, visoka povečuje kontrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Odpiranje PDF...",
        'progress_loading_document': "Nalaganje dokumenta...",
        'progress_pdf_opened': "PDF odprt",
        'progress_creating_backup': "Ustvarjanje varnostne kopije...",
        'progress_backup_description': "Zavarovanje izvirne datoteke...",
        'progress_backup_created': "Varnostna kopija ustvarjena",
        'progress_backup_saved_as': "Shranjeno kot: {0}",
        'progress_analyzing_start': "Zagon analize...",
        'progress_searching_empty': "Iskanje praznih strani...",
        'progress_page_empty': "Stran {0} je prazna",
        'progress_page_keep': "Ohrani stran {0}",
        'progress_analysis_complete': "Analiza končana",
        'progress_empty_found': "Najdenih {0} praznih strani",
        'progress_current_page': "Trenutna stran",
        'progress_mark_delete': "Označeno za brisanje",
        'progress_range_selected': "Obseg strani {0}-{1}",
        'progress_deleting_pages': "Brisanje {0} strani",
        'progress_creating_new_pdf': "Ustvarjanje novega PDF...",
        'progress_transferring_pages': "Prenos strani",
        'progress_keeping_page': "Stran {0} bo ohranjena ({1}/{2})",
        'progress_saving_pdf': "Shranjevanje PDF...",
        'progress_optimizing': "Optimizacija velikosti datoteke...",
        'progress_finalizing': "Dokončevanje...",
        'progress_new_size': "Nova velikost: {0:.2f} MB",
        'progress_cancelling': "Preklic...",
        'progress_cancel_message': "{0} se prekliče",
        'progress_pages_found_moving': "Najdenih {0} strani, {1} za premik",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analiza PDF...",
        'ocr_status_optimizing': "Optimizacija slike poteka...",
        'ocr_status_recognizing': "Prepoznavanje besedila poteka...",
        'ocr_status_embedding': "Vgrajevanje besedila...",
        'ocr_status_finalizing': "Dokončevanje PDF...",

        # PDF-Laden
        'progress_preparing': "Priprava...",
        'progress_loading': "Nalaganje PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Brisanje strani...",
        'progress_moving_title': "Premikanje strani...",
        'pages_found': "Najdene strani",
        'progress_creating_new_order': "Ustvarjanje novega vrstnega reda...",
        'progress_sorting_pages': "Razvrščanje strani...",
        'progress_moving_to_begin': "Premakni {0} strani na začetek",
        'progress_transferring_count': "Prenesi {0} strani",
        'progress_transferring_before_target': "Prenesi strani pred cilj",
        'progress_moving_pages': "Premakni {0} strani",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_varnostna_kopija_",
        'filename_protected_suffix': "_zasciteno_",
        'filename_copy_suffix': "_Kopija",
        'filename_page_single': "_Stran_",
        'filename_page_range': "_Strani_",
        'filename_export_page': "_Stran_{0:03}",
        'filename_export_range': "_Strani_{0}-{1}",
        'filename_export_multiple': "_Strani_{0}",
        'filename_with_text': "_z_Besedilom",
        'filename_with_signature': "_s_Podpisom",
        'filename_with_image': "_s_Sliko",
        'filename_with_forms': "_z_Oblikami",
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
        'view_toggle_navbar': "Pokaži vrstico z gumbi",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Ni mogoče izbrisati vseh strani",
		'pages_cannot_delete_last_page': 'Zadnje strani ni mogoče izbrisati!',
		'pages_cannot_delete_all_pages': 'V dokumentu mora ostati vsaj ena stran!',
		'delete_pages_confirm': 'Ali ste prepričani, da želite izbrisati {0} strani?',
		'delete_pages_confirm_voice': 'Ali ste prepričani, da želite izbrisati {0} strani?',
		'pages_deleted': '{0} strani je bilo uspešno izbrisanih.',
		'warning': 'Opozorilo',
		'error': 'Napaka',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Obrazec ni izbran",
        'form_customized': "Obrazec prilagojen",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Izberi",
        'btn_use': "Uporabi",
        'master_password_for_spasswords': "Za shranjevanje in uporabo gesel morate najprej nastaviti glavno geslo.\n\nAli želite zdaj nastaviti glavno geslo?",
        'open_saved_dialog_title': "Odpri shranjeno datoteko",
        'open_saved_question': "Ali želite zdaj odpreti shranjeno datoteko?",
        'password': "Geslo",
        'password_manager_master_required': "Upravitelj gesel je na voljo le, če je nastavljeno glavno geslo.\n\nAli želite zdaj nastaviti glavno geslo?",
        'password_master_required_for_select': "Za prikaz in izbiro shranjenih gesel se morate najprej overiti s svojim glavnim geslom.\n\nAli se želite overiti zdaj?",
        'password_not_available': "Izbrano geslo ni na voljo ali ga ni bilo mogoče dešifrirati.",
        'password_options_title': "Možnosti gesla",
        'password_save_choice_change': "Nastavi novo geslo",
        'password_save_choice_keep': "Uporabi obstoječe geslo",
        'password_save_choice_none': "Shrani nešifrirano",
        'password_save_hint': "Najprej nastavite glavno geslo za varno shranjevanje gesel.",
        'password_save_master_required': "Shrani geslo (možno le z glavnim geslom)",
        'password_save_question': "Trenutni PDF je zaščiten z geslom. Ali želite uporabiti obstoječe geslo, nastaviti novo ali shraniti nešifrirano?",
        'password_select': "Izberi geslo",
        'password_select_none': "Ni izbranega gesla.\n\nIzberite geslo s seznama.",
        'password_select_one': "Izberite natančno eno geslo.\n\nOznačili ste več gesel.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_varnostna_kopija",
        'filename_insert_suffix': "_z_vstavljanjem",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_strani_izbrisane",
        'filename_pages_moved': "_strani_premaknjene",
        'filename_rotated_all_suffix': "_vse_strani_obrnjene",
        'filename_rotated_suffix': "_stran_obrnjena",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfiguracija imen datotek pri spremembah PDF",
        'filename_keep_suffixes': "Ohrani prejšnje končnice (npr. _z_besedilom)",
        'filename_keep_suffixes_false': "Zamenjaj",
        'filename_keep_suffixes_true': "Ohrani",
        'filename_preview_label': "Predogled imena datoteke:",
        'filename_preview_overwrite_hint': "Predogled ni na voljo – izvirnik bo prepisan.",
        'filename_separator': "Ločilo med besedami",
        'filename_separator_none': "Brez ločila",
        'filename_separator_space': "Presledek ( )",
        'filename_separator_underscore': "Podčrtaj (_)",
        'filename_settings_saved': "Nastavitve imena datoteke shranjene",
        'filename_settings_title': "Oblikovanje imena datoteke in varnostna kopija",
        'filename_timestamp_position': "Položaj časovnega žiga",
        'filename_timestamp_position_after': "Za osnovnim imenom",
        'filename_timestamp_position_before': "Čisto spredaj",
        'filename_timestamp_position_end': "Na koncu",
        'filename_use_timestamp': "Uporabi časovni žig",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Vedenje ob spremembah:</b><ul><li>Brisanje in vstavljanje strani</li><li>Vstavljanje besedila, podpisa, slike in oblik</li><li>OCR</li></ul></html>",
        'backup_section': "Varnostna kopija za operacije s stranmi (Brisanje, Premikanje)",
        'behavior_info': "Opomba: Pri 'Prepiši izvirnik' se časovni žigi in pripone ignorirajo – datoteka ohrani svoje ime.",
        'behavior_new_file': "Vedno ustvari novo datoteko (s časovnim žigom in pripono)",
        'behavior_overwrite': "Prepiši izvirnik (brez nove datoteke)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Vse strani so bile obrnjene.\n\nIzvirnik je ostal nespremenjen.\nNova datoteka: {0}",
        'all_pages_rotated_voice': "Vse strani obrnjene, ustvarjena nova datoteka.",
        'empty_pages_deleted_new_file': "{0} praznih strani je bilo izbrisanih.\n\nIzvirnik je ostal nespremenjen.\nNova datoteka: {1}",
        'empty_pages_deleted_voice': "{0} praznih strani izbrisanih, ustvarjena nova datoteka.",
        'ocr_keep_original': "Ohrani izvirnik (odpri ročno kasneje)",
        'ocr_new_file_question': "Nova iskalna PDF je shranjena pod:\n{0}\n\nAli jo želite odpreti zdaj?",
        'ocr_open_new': "Odpri novo OCR datoteko",
        'ocr_original_kept': "Izvirna datoteka ostane odprta. OCR datoteka je shranjena.",
        'page_deleted_new_file': "Stran {0} je bila izbrisana.\n\nIzvirnik je ostal nespremenjen.\nNova datoteka: {1}",
        'page_deleted_voice': "Stran {0} izbrisana, ustvarjena nova datoteka.",
        'page_rotated_new_file': "Stran {0} je bila obrnjena.\n\nIzvirnik je ostal nespremenjen.\nNova datoteka: {1}",
        'page_rotated_voice': "Stran {0} obrnjena, ustvarjena nova datoteka.",
        'pages_deleted_new_file': "Izbrisanih je bilo {0} strani.\n\nIzvirna datoteka je ostala nespremenjena.\nNova datoteka: {1}",
        'pages_deleted_new_file_voice': "{0} strani izbrisanih, ustvarjena nova datoteka.",
        'pages_inserted_new_file': "Vstavljenih je bilo {0} strani.\n\nIzvirna datoteka je ostala nespremenjena.\nNova datoteka: {1}",
        'pages_inserted_new_file_ask': "Vstavljenih je bilo {0} strani.\n\nIzvirnik je ostal nespremenjen.\nNova datoteka: {1}\n\nAli jo želite odpreti zdaj?",
        'pages_inserted_voice_new': "{0} strani vstavljenih, ustvarjena nova datoteka.",
        'pages_moved_new_file': "Premaknjenih je bilo {0} strani.\n\nIzvirna datoteka je ostala nespremenjena.\nNova datoteka: {1}",
        'pages_moved_new_file_voice': "{0} strani premaknjenih, ustvarjena nova datoteka.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ne prikaži več",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Nastavitev varnostne kopije</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Varnostna kopija VKLJUČENA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Pri vseh spremembah, ki prepišejo izvirnik</strong> (besedilo, podpis, slika, oblika, OCR, obračanje, vstavljanje, brisanje/premikanje strani) se <strong>samodejno ustvari varnostna kopija s časovnim žigom</strong> pred izvedbo spremembe.</p>
                <p style="margin: 5px 0 5px 20px;">• Varnostna kopija se nahaja poleg izvirne datoteke (npr. <code>Dokument_varnostna_kopija_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Če ste dodatno aktivirali možnost <strong>„Prepiši izvirnik“</strong>, se prav tako ustvari varnostna kopija.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Varnostna kopija IZKLJUČENA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Varnostna kopija se ne ustvari</strong> – niti pri prepisovanju niti pri operacijah s stranmi.</p>
                <p style="margin: 5px 0 5px 20px;">• Izvirna datoteka se lahko pri prepisovanju nepovratno izgubi.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Priporočljivo samo za izkušene uporabnike!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Namig:</strong> Nastavitev varnostne kopije je neodvisna od možnosti „Prepiši izvirnik“. Oboje lahko kombinirate.<br>
                To sporočilo lahko trajno skrijete.
            </div>
        </div>
        """,
        'backup_info_title': "Vedenje varnostne kopije",
        'backup_info_voice': "Obvestilo o vedenju varnostne kopije pri operacijah s stranmi. Varnostna kopija vključena prepiše izvirnik, izključena ustvari novo datoteko.",
        'show_backup_info': "Informacije o nastavitvi varnostne kopije",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ne prikaži več",
        'overwrite_enable_backup': "Omogoči varnostno kopijo (priporočljivo)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Prepiši izvirnik</p>
            <p>Če omogočite to možnost, se spremembe (besedilo, podpis, slika, oblika, OCR, obračanje, vstavljanje) <strong>shranijo neposredno v izvirnik</strong> – <strong>nova datoteka se ne ustvari</strong>.</p>
            <p>• Ime datoteke ostane nespremenjeno.<br>
            • Časovni žigi in pripone se ignorirajo.<br>
            • <strong>Brez varnostne kopije se lahko izvirnik nepovratno izgubi.</strong></p>
            <p style="color: #FFD700;">Priporočilo: Dodatno omogočite možnost varnostne kopije za samodejne varnostne kopije.</p>
        </div>
        """,
        'overwrite_info_title': "Prepiši izvirnik",
        'overwrite_info_voice': "Opozorilo: Prepiši izvirnik – brez nove datoteke. Varnostna kopija priporočljiva.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Vstavljenih je bilo {0} strani.\n\nIzvirna datoteka je bila prepisana.\nUstvarjena je bila varnostna kopija.",
        'pages_inserted_overwrite_no_backup': "Vstavljenih je bilo {0} strani.\n\nIzvirna datoteka je bila prepisana.\nNI bila ustvarjena varnostna kopija.",
        'texts_saved_overwrite_with_backup': "Spremembe so bile shranjene v izvirniku.\n\nUstvarjena je bila varnostna kopija.",
        'texts_saved_overwrite_no_backup': "Spremembe so bile shranjene v izvirniku.\n\nNI bila ustvarjena varnostna kopija.",
        'texts_crosses_saved_new_file': "{0} {1} in {2} {3} so bili vstavljeni.\n\nIzvirna datoteka je ostala nespremenjena.\nUstvarjena je bila nova datoteka.\n\nNalaganje novega PDF...",
        'texts_saved_new_file': "{0} {1} je bilo vstavljenih.\n\nIzvirna datoteka je ostala nespremenjena.\nUstvarjena je bila nova datoteka.\n\nNalaganje novega PDF...",
        'crosses_saved_new_file': "{0} {1} je bilo vstavljenih.\n\nIzvirna datoteka je ostala nespremenjena.\nUstvarjena je bila nova datoteka.\n\nNalaganje novega PDF...",
        'elements_saved_new_file': "{0} elementov je bilo vstavljenih.\n\nIzvirna datoteka je ostala nespremenjena.\nUstvarjena je bila nova datoteka.\n\nNalaganje novega PDF...",
        'signatures_saved_overwrite_with_backup': "Podpis(i) je bil(i) shranjen(i) v izvirniku.\n\nUstvarjena je bila varnostna kopija.",
        'signatures_saved_overwrite_no_backup': "Podpis(i) je bil(i) shranjen(i) v izvirniku.\n\nNI bila ustvarjena varnostna kopija.",
        'images_saved_overwrite_with_backup': "Slika(e) je bila(e) shranjena(e) v izvirniku.\n\nUstvarjena je bila varnostna kopija.",
        'images_saved_overwrite_no_backup': "Slika(e) je bila(e) shranjena(e) v izvirniku.\n\nNI bila ustvarjena varnostna kopija.",
        'forms_saved_overwrite_with_backup': "Oblika(e) je bila(e) shranjena(e) v izvirniku.\n\nUstvarjena je bila varnostna kopija.",
        'forms_saved_overwrite_no_backup': "Oblika(e) je bila(e) shranjena(e) v izvirniku.\n\nNI bila ustvarjena varnostna kopija.",
        'signatures_saved_new_file': "{0} podpisov je bilo vstavljenih.\n\nIzvirna datoteka je ostala nespremenjena.\nUstvarjena je bila nova datoteka.\n\nNalaganje novega PDF...",
        'images_saved_new_file': "{0} slik je bilo vstavljenih.\n\nIzvirna datoteka je ostala nespremenjena.\nUstvarjena je bila nova datoteka.\n\nNalaganje novega PDF...",
        'forms_saved_new_file': "{0} oblik je bilo vstavljenih.\n\nIzvirna datoteka je ostala nespremenjena.\nUstvarjena je bila nova datoteka.\n\nNalaganje novega PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Opozorilo: Ta PDF vsebuje obrnjene strani. Pozicioniranje je lahko drugačno.",
        'page_rotated_warning_title': "Zaznana obrnjena stran",
        'page_rotated_warning_message': "Trenutna stran {0} je obrnjena za {1}°.\n\nVstavljanje elementov na obrnjene strani ni podprto.\n\nAli želite zdaj obrniti stran v pokončni položaj?",
        'page_rotated_warning_voice': "Opozorilo: Stran je obrnjena. Najprej jo obrnite.",
        'paste_on_rotated_page_simple_warning': "Vstavljanje na stran {0} ni mogoče!\n\nTa stran je obrnjena za {1}°.\n\nNajprej obrnite stran na 0° (Meni: Uredi → Poravnaj stran).\n\nOpozorilo:\nPrej kopiran element se bo izgubil, če ne shranite pred obračanjem strani.",
        'paste_on_rotated_page_voice': "Vstavljanje preklicano. Stran je obrnjena. Najprej poravnajte stran.",
        'page_rotated_cancel': "Prekliči",
        'page_rotated_rotate_until_upright': "Večkratno obračanje strani (dokler ni pokončna)",
        'page_rotated_now_upright': "Stran je zdaj pokončna. Zdaj lahko vstavite.",
        'page_rotated_still_not_upright': "Strani ni bilo mogoče obrniti v pokončni položaj. Popravite ročno.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Pomoč: Popravi obrnjene strani",
        'help_rotated_pages_voice': "Odpre se pomoč za popravljanje obrnjenih strani.",
        'btn_help': "Pomoč",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Težava: Obrnjena stran – Vstavljanje ne deluje pravilno</p>

            <p>Če vstavljanje besedil, podpisov ali oblik na obrnjeni strani ne deluje pravilno, lahko stran popravite z zunanjim urejevalnikom PDF.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Rešitev z zunanjim orodjem (npr. macOS Predogled)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Izvozi stran</strong><br>
                &nbsp;&nbsp;Kliknite v meniju na <strong>Datoteka → Izvozi kot strani</strong> ali uporabite drugo metodo za shranjevanje želene strani kot posameznega PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Odpri stran v zunanjem programu</strong><br>
                &nbsp;&nbsp;Odprite izvoženi PDF v urejevalniku PDF (npr. <strong>macOS Predogled</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Obrni stran</strong><br>
                &nbsp;&nbsp;Obrnite stran tako, da je pokončna (v Predogledu: <strong>Orodja → Zavrti</strong> ali <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Shrani</strong><br>
                &nbsp;&nbsp;Shranite popravljeno stran (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Ponovno vstavi stran v izvirni dokument</strong><br>
                &nbsp;&nbsp;Vrnite se v PDFDarkView in vstavite popravljeno stran na želeno mesto:<br>
                &nbsp;&nbsp;<strong>Uredi → Vstavi strani</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativa: Obrni stran v izvirniku</p>
                <p style="margin: 5px 0 5px 20px;">• Uporabite vgrajeno funkcijo obračanja (<strong>Uredi → Zavrti stran</strong>) za postopno popravljanje strani.<br>
                • Po vsakem obračanju lahko preverite, ali vstavljanje zdaj deluje.<br>
                • To je pogosto hitrejša rešitev – najprej jo poskusite!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Namig:</strong> Če pogosto naletite na obrnjene strani, lahko opozorilo v pogovornem oknu za vstavljanje trajno skrijete.<br>
                Pozicioniranje je lahko nato drugačno – to možnost uporabite le, če poznate posledice.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Poravnaj strani",
        'menu_rotate_normalize_tooltip': "Zavrti stran ali ponastavi na 0°",
        'normalize_current_page': "Pripravi trenutno stran v pokončni položaj (nastavi na 0°)",
        'normalize_all_pages': "Pripravi vse strani v pokončni položaj (nastavi na 0°)",
        'page_normalized': "Stran {0} je bila nastavljena v pokončni položaj.",
        'all_pages_normalized': "Vse strani so bile nastavljene v pokončni položaj.",
        'page_already_upright': "Stran {0} je že pokončna.",
        'all_pages_already_upright': "Vse strani so že pokončne.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF ne vsebuje iskalnega besedila.</p><p>Ali želite izvesti OCR za izvoz v {0}?</p>",
        'export_ocr_voice': "PDF ne vsebuje besedila. Za izvoz v {0} je potreben OCR.",
        'export_no_ocr_possible': "Izvoz brez OCR ni mogoč. Izvedite OCR prek menija.",
        'ocr_failed_export_not_possible': "OCR ni uspel. Izvoza ni mogoče izvesti.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF se odpre v Predogledu. Tam zaženite postopek tiskanja.",
        'print_preview_manual': "PDF je odprt. Ukaz za tiskanje izvedite ročno (npr. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Združi PDF-je",
        'merge_pdfs': "Združi PDF-je",
        'merge_progress_title': "Združevanje PDF-jev...",
        'merge_pdfs_list': "PDF-ji po vrstnem redu (Povleci in spusti za razvrščanje)",
        'merge_add_pdf': "Dodaj PDF",
        'merge_remove': "Odstrani",
        'merge_move_up': "Gor",
        'merge_move_down': "Dol",
        'merge_pdfs_info': "💡 Namig: Vrstni red lahko spremenite s povleci in spusti",
        'merge_no_pdfs': "Noben PDF ni izbran. Kliknite 'Dodaj PDF'.",
        'merge_info': "Izbranih {0} PDF-jev (približno {1} strani)",
        'merge_open_file': "Odpri datoteko",
        'merge_merge': "Združi",
        'merge_error': "Napaka pri združevanju",
        'merge_min_two_pdfs_error': "Izberite vsaj dva PDF-ja za združevanje.",
        'merge_select_pdfs': "Izberite PDF-je za združevanje",
        'merge_error_file': "Napaka pri obdelavi",
        'merge_cancelled': "Združevanje je bilo preklicano",
        'merge_preparing': "Pripravljanje...",
        'merge_processing': "Obdelava PDF {0} od {1}",
        'merge_saving': "Shranjevanje združenega PDF...",
        'merge_complete': "Končano!",
        'merge_success_title': "Združevanje uspešno",
        'merge_success_voice': "{0} PDF-jev je bilo uspešno združenih.",
        'merge_success_message': "{0} PDF-jev je bilo uspešno združenih.\n\nNov dokument ima zdaj {1} strani.\n\nNova datoteka:\n{2}\n\nMesto shranjevanja:\n{3}\n{2}\n\nAli želite odpreti ta PDF?",
        'replace_file_title': "Zamenjati datoteko?",
        'replace_file_message': "PDF je že odprt. Ali ga želite zamenjati z novo datoteko?",
        'btn_yes': "Da",
        'btn_no': "Ne",
        'filename_merge_suffix': "združeno",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Odpiranje {0}...",
        'progress_merge_reading': "Branje {0}...",
        'progress_merge_adding': "Dodajanje {0} strani...",
        'progress_merge_optimizing': "Optimizacija PDF...",
        'progress_merge_writing': "Pisanje PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "zapiranje PDF",
        'action_close_window': "zapiranje okna",
        'action_open_new_pdf': "odpiranje novega PDF",
        'action_quit_app': "zapiranje aplikacije",
        'changes_saved': "Spremembe so shranjene.",
        'file_close_title': "Zapri PDF datoteko",
        'save_before_action': "Ali naj se spremembe shranijo pred {0}? Da ali Ne?",
        'save_before_action_voice': "Ali naj se spremembe shranijo pred {0}? Da ali Ne?",
        'save_before_close_question': "Ali naj se spremembe shranijo pred zapiranjem? Da ali Ne?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Ustvarjen iskalni PDF:\n\n{0}\n\n<b>po potrebi poskusite znova",
        "ocr_rotate_title": "Poravnaj strani pred OCR",
        "ocr_rotate_question": "PDF vsebuje zasukane strani.\nAli želite pred OCR poravnati vse strani na 0°?\nTo znatno izboljša prepoznavanje besedila.",
        "ocr_rotate_yes": "Da, poravnaj",
        "ocr_rotate_no": "Ne, zaženi OCR neposredno",
        "ocr_rotate_voice": "PDF vsebuje zasukane strani. Ali je treba pred OCR poravnati vse strani?",
        "ocr_not_performed_message": "Ni besedila. Izvedite OCR (meni \"Uredi\" → \"Izvedi OCR\" ali tipka Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Nastavitve OCR",
        "ocr_language_btn": "Izberite jezik OCR",
        "ocr_language": "Jezik(i) OCR",
        "ocr_language_current": "Trenutni jezik:",
        "ocr_param_info": "Informacije o parametru",

        "ocr_force_ocr_label": "Vsili OCR",
        "ocr_deskew_label": "Popravi poševnost",
        "ocr_clean_label": "Počisti sliko",
        "ocr_oversample_label": "Ločljivost (DPI)",
        "ocr_pagesegmode_label": "Razdelitev strani",
        "ocr_oem_label": "Način pogona OCR",
        "ocr_optimize_label": "Stiskanje PDF",
        "ocr_jobs_label": "Vzporedni procesi",
        "ocr_verbose_label": "Podrobnost dnevnika",

        "ocr_force_ocr_tooltip": "Vsili OCR na vsaki strani, tudi če besedilo že obstaja",
        "ocr_deskew_tooltip": "Samodejno poravnaj poševna skeniranja",
        "ocr_clean_tooltip": "Odstrani šum in artefakte s slike",
        "ocr_oversample_tooltip": "Povečaj sliko pred OCR na ta DPI",
        "ocr_pagesegmode_tooltip": "Določa, kako se stran razdeli na besedilna področja",
        "ocr_oem_tooltip": "Izbere Tesseractov pogon OCR",
        "ocr_optimize_tooltip": "Raven stiskanja izhodnega PDF",
        "ocr_jobs_tooltip": "Število vzporednih procesov OCR",
        "ocr_verbose_tooltip": "Raven podrobnosti izpisa dnevnika",
        "ocr_settings_explain_btn": "Pojasnilo",

        "ocr_force_ocr_explain": "Vsili prepoznavanje besedila na <b>vsaki</b> strani, tudi če že vsebuje besedilo.\n\nPriporočilo: <b>Vklopljeno</b> za skenirane PDF, <b>Izklopljeno</b> za izvorne PDF z že obstoječim besedilom.",

        "ocr_deskew_explain": "Popravi rahlo poševna skeniranja (do približno 5°).\n\nPriporočilo: <b>Vklopljeno</b> za skenirane dokumente, <b>Izklopljeno</b> če so strani že popolnoma ravne.",

        "ocr_clean_explain": "Odstrani šum, pike in majhne artefakte s slike.\n<b>POMEMBNO:</b> Za arabska, tajska ali vietnamska besedila z diakritičnimi znaki (pike nad/pod črkami) je treba to možnost <b>onemogočiti</b>, sicer se lahko izgubijo pomembni znaki.",

        "ocr_oversample_explain": "Poveča sliko <b>pred</b> prepoznavanjem besedila na določen DPI.<br><br>• <b>72-150 DPI:</b> Zelo hitro, vendar nizka stopnja prepoznavanja<br>• <b>200-300 DPI:</b> Optimalno območje (Standardno: 300)<br>• <b>400+ DPI:</b> Komaj boljše prepoznavanje, vendar bistveno večje datoteke<br><br>Priporočilo: 300 DPI za zapletene pisave (arabščina, kitajščina, japonščina), 200 DPI za zahodne jezike.",

        "ocr_pagesegmode_explain": "Določa, kako Tesseract razdeli stran na besedilna področja.\n\n• <b>3 - Samodejno (Standardno):</b> Dobro za mešane postavitve\n• <b>4 - Enojni stolpec:</b> Za besedila z enim stolpcem\n• <b>5 - Navpični blok:</b> Za navpične pisave (japonščina, kitajščina)\n• <b>6 - Enoten besedilni blok:</b> Optimalno za tekoče besedilo brez stolpcev\n• <b>11 - Surova slika:</b> Za slaba skeniranja / rokopise\n\nPriporočilo: <b>6</b> za preprosta besedilna dokumenta, <b>3</b> za zapletene postavitve.",

        "ocr_oem_explain": "Izbere Tesseractov pogon OCR.\n\n• <b>0 - Legacy:</b> Stari pogon (hiter, vendar manj natančen)\n• <b>1 - LSTM:</b> Nevronski pogon (počasnejši, vendar natančnejši)\n• <b>2 - Legacy + LSTM:</b> Združuje oba rezultata\n• <b>3 - Standardno (LSTM prednost):</b> Najboljša izbira za večino primerov\n\nPriporočilo: <b>3</b> za največjo natančnost prepoznavanja.",

        "ocr_optimize_explain": "Stisne izhodni PDF.\n\n• <b>0:</b> Brez optimizacije (najhitrejša obdelava)\n• <b>1:</b> Lahka optimizacija (dober kompromis)\n• <b>2:</b> Zmerna optimizacija\n• <b>3:</b> Močna optimizacija (najmanjša datoteka, vendar počasnejša)\n\nPriporočilo: <b>1</b> za vsakodnevno uporabo.",

        "ocr_jobs_explain": "Število vzporednih procesov za OCR.\n\n• <b>1:</b> Počasno, vendar najmanjša poraba pomnilnika\n• <b>4-8:</b> Optimalno za sodobne večjedrne procesorje\n• <b>12+:</b> Komaj hitrejša obdelaba z visoko porabo pomnilnika\n\nPriporočilo: Število jeder CPU (npr. <b>4</b> na 4-jedrnih sistemih).",

        "ocr_verbose_explain": "Raven podrobnosti izpisa dnevnika v konzoli.\n\n• <b>0:</b> Brez izpisa\n• <b>1:</b> Napredek in sporočila o stanju\n• <b>2:</b> Podroben izpis\n• <b>3:</b> Celoten izpis razhroščevanja (zelo obsežen)\n\nPriporočilo: <b>1</b> za normalno delovanje.",

        "ocr_reset_title": "Nastavitve so ponastavljene",
        "ocr_reset_message": "Vse nastavitve OCR so bile ponastavljene na standardne vrednosti.",
        "info_tooltip": "Več informacij o tem parametru",
        "ocr_reset_defaults": "Ponastavi na standardno",

        "ocr_psm_0": "Samodejno (pogon Legacy)",
        "ocr_psm_1": "Samodejno zaznavanje stolpcev",
        "ocr_psm_3": "Samodejno (Standardno)",
        "ocr_psm_4": "Enojni stolpec",
        "ocr_psm_5": "Navpični blok",
        "ocr_psm_6": "Enoten besedilni blok",
        "ocr_psm_7": "Enojna vrstica besedila",
        "ocr_psm_8": "Enojna beseda",
        "ocr_psm_11": "Surova slika (brez analize postavitve)",

        "ocr_oem_0": "Pogon Legacy (hiter)",
        "ocr_oem_1": "Pogon LSTM (nevronski, natančen)",
        "ocr_oem_2": "Legacy + LSTM kombinirano",
        "ocr_oem_3": "Standardno (LSTM prednost)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Jezik(i) OCR...",
        "ocr_language_title": "Izberite jezik(e) OCR",
        "ocr_language_instruction": "Izberite jezik(e) za prepoznavanje besedila (OCR).\nPozor: Več jezikov gre na račun zmogljivosti in natančnosti!\nNajboljše rezultate dosežete, če izberete samo en jezik.",
        "ocr_language_predefined": "Vnaprej določene kombinacije",
        "ocr_language_custom": "Po meri...",
        "ocr_language_selected": "Izbrani jeziki OCR",
        "ocr_language_changed": "Jezik OCR je spremenjen v {0}",
        "ocr_language_auto_detect": "Razpoložljivi jeziki se samodejno zaznajo.",
        "ocr_language_none_found": "Ni najdenih podatkov o jeziku Tesseract! Namestite jezikovne pakete (npr. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Izbira jezika po meri",
        "ocr_language_available": "Razpoložljivi jeziki (nameščeni):",
        "ocr_language_select_hint": "Izberite enega ali več jezikov:",
        "ocr_language_confirm": "Uporabi",
        "ocr_language_reset": "Ponastavi na standardno (deu+eng+vie)",
        "ocr_language_priorities": "Priporočeni jeziki (prednameščeni):",

        "select_all_languages": "Izberi vse",
        "clear_all_languages": "Počisti izbor",
        "install_language_packs": "Namesti manjkajoče jezikovne pakete...",
        "install_hint": "💡 Namig: Vsi jeziki niso nameščeni v vašem sistemu. S tem gumbom boste prejeli pomoč pri namestitvi.",
        "ocr_language_install_title": "Namestitev jezikovnih paketov Tesseract",

        "ocr_missing_languages": "Manjkajoči jezikovni paketi OCR",
        "ocr_missing_languages_message": "Naslednji izbrani jeziki niso nameščeni v vašem sistemu:\n\n{0}\n\nNamestite manjkajoče jezikovne pakete (glejte pomoč v 'Pomoč pri namestitvi').\n\nAli želite zdaj odpreti pomoč pri namestitvi?",
        "ocr_missing_languages_voice": "Manjkajoči jezikovni paketi. Namestite manjkajoče jezike.",
        "ocr_install_help_now": "Odpri pomoč",
        "ocr_continue_anyway": "Vseeno poskusi",
        "ocr_language_error_title": "Napaka jezika OCR",
        "ocr_language_error_message": "Napaka med prepoznavanjem besedila: {0}\n\nPreverite svoje nastavitve jezika OCR (Nastavitve → Jezik OCR).",
        "ocr_install_help_button": "Pomoč pri namestitvi",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Namestite jezikovne pakete Tesseract</p>

        <p>Da bo OCR deloval v določenem jeziku, morajo biti ustrezni jezikovni podatki nameščeni v vašem sistemu. Sledite navodilom za vaš operacijski sistem:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Odprite <strong>Terminal</strong> (Finder → Programi → Pripomočki → Terminal).</li>
        <li>Namestite vse razpoložljive jezike z:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (To lahko traja nekaj minut.)</li>
        <li>Ali samo posamezne jezike (npr. vietnamščino):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Pri trenutnih različicah Homebrew bo morda treba <code>*.traineddata</code> prenesti ročno (glejte spodaj).</li>
        <li>Po namestitvi: Zaprite to pogovorno okno in znova odprite izbor jezika OCR – novi jeziki se bodo prikazali samodejno.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Odprite terminal (Ctrl+Alt+T).</li>
        <li>Namestite želeni jezik, npr. za vietnamščino:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Pomembne jezikovne kode: <code>deu</code> (nemščina), <code>eng</code> (angleščina), <code>vie</code> (vietnamščina), <code>spa</code> (španščina), <code>fra</code> (francoščina), <code>ita</code> (italijanščina), <code>nld</code> (nizozemščina), <code>fin</code> (finščina), <code>swe</code> (švedščina), <code>nor</code> (norveščina).</li>
        <li>Prikaži vse razpoložljive pakete:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ročno)</p>
        <ol>
        <li>Prenesite želene datoteke <code>*.traineddata</code> s:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (npr. <code>vie.traineddata</code> za vietnamščino).</li>
        <li>Kopirajte datoteke v mapo jezikov Tesseract, običajno:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Prilagodite glede na individualno namestitev.)</li>
        <li>Ponovno zaženite aplikacijo (ali znova odprite izbor jezika OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativa za vse sisteme</p>
        <ul>
        <li>Namestite <strong>OCRmyPDF</strong> in <strong>Tesseract</strong> z upravljalnikom paketov po vaši izbiri. Večina namestitev že vsebuje nekaj standardnih jezikov (angleščino, nemščino, francoščino).</li>
        <li>Manjkajoče jezike lahko namestite kadar koli – izbor jezika OCR prikazuje samo dejansko obstoječe jezike.</li>
        </ul>

        <hr>
        <p><b>✅ Po namestitvi:</b> Ponovni zagon aplikacije ni potreben – novo dodani jeziki se bodo takoj prikazali na seznamu.</p>
        <p><b>📖 Pomoč za jezikovne kode:</b> Celoten seznam je na voljo v <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentaciji Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Pisave Noto Sans",
        "info_noto_font_voice": "Vodnik za namestitev pisav Noto Sans",
        "btn_info_noto_font_install": "Informacije o pisavi",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Kako namestiti brezplačne pisave Noto podjetja Google</h2>

        <p><strong>Pisave Noto</strong> so družina pisav odprte kode podjetja Google. Njihov cilj je, da ne vidite <em>"nobenega tofuja"</em> (tj. brez praznih škatel □) in da pravilno prikažejo vsak znak iz standarda Unicode. So idealen dodatek za aplikacije, ki morajo prikazovati besedila v številnih različnih jezikih.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Namestitev na macOS</h3>

        <p><strong>Metoda 1: Z Homebrew (za napredne)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metoda 2: Prek "Font Book" (Priporočeno)</strong></p>

        <ol>
        <li>Prenesite uradni paket pisav:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Razširite datoteko ZIP</li>
        <li>Kopirajte datoteke v <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Namestitev na Windows (10 in 11)</h3>

        <p><strong>Metoda 1: Microsoft Store (Priporočeno)</strong><br>
        Poiščite "Google Noto Fonts" ali "Noto Sans" in kliknite <strong>Namesti</strong>.</p>

        <p><strong>Metoda 2: Ročna namestitev</strong></p>

        <ol>
        <li>Prenos:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Razširite ZIP</li>
        <li>Izberite datoteke .ttf / .otf</li>
        <li>Desni klik → <strong>Namesti</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        ali<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Ime\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Namestitev na Linux</h3>

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

        <p>Preverjanje:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Upravljanje zaznamkov",
        "bookmark_add": "Dodaj zaznamek",
        "bookmark_add_tooltip": "Shrani trenutno stran kot zaznamek",
        "bookmark_remove": "Odstrani zaznamek",
        "bookmark_remove_tooltip": "Izbriši označeni zaznamek",
        "bookmark_remove_all": "Odstrani vse",
        "bookmark_remove_all_tooltip": "Izbriši vse zaznamke tega PDF",
        "bookmark_jump": "Skoči na zaznamek",
        "bookmark_jump_tooltip": "Skoči na izbrano stran",
        "bookmark_name": "Ime",
        "bookmark_page": "Stran",
        "bookmark_no_bookmarks": "Ni zaznamkov.\nKliknite 'Dodaj', da shranite trenutno stran kot zaznamek.",
        "bookmark_added": "Zaznamek za stran {0} dodan: {1}",
        "bookmark_removed": "Zaznamek odstranjen: {0}",
        "bookmark_all_removed": "Vsi zaznamki so bili odstranjeni.",
        "bookmark_name_default": "Stran {0}",
        "bookmark_name_prompt": "Ime zaznamka:\n(dolg tekst bo skrajšan na 50 znakov)",
        "bookmark_name_prompt_title": "Ime zaznamka",
        "bookmark_confirm_remove_all": "Ali ste prepričani, da želite odstraniti vseh {0} zaznamkov?",
        "menu_bookmarks": "Zaznamki",
        "bookmark_manage": "Upravljanje zaznamkov",
        "bookmark_next": "Naslednji zaznamek",
        "bookmark_prev": "Prejšnji zaznamek",
        "bookmark_page_display": "Stran {0}",
        "bookmark_exists": "Zaznamek za to stran s tem imenom že obstaja.",
        "bookmark_select_first": "Najprej izberite zaznamek.",
        "bookmark_confirm_remove": "Ali ste prepričani, da želite odstraniti zaznamek 'Stran {0}: {1}'?",
        "bookmark_jumped_to": "Skočeno na zaznamek '{0}' na strani {1}.",
        "bookmark_jumped_to_voice": "Zaznamek {0}, stran {1}",
        "btn_close": "Zapri",

        "bookmark_list": "Vaši zaznamki",
        "bookmark_rename": "Preimenuj zaznamek",
        "bookmark_rename_tooltip": "Spremeni ime izbranega zaznamka",
        "bookmark_rename_title": "Preimenuj zaznamek",
        "bookmark_rename_prompt": "Novo ime za zaznamek na strani {0}:\n(največ 50 znakov)",
        "bookmark_renamed": "Zaznamek '{0}' je bil preimenovan v '{1}'.",
        "bookmark_item_tooltip": "Stran {0}: {1}\nDvokliknite za skok",
        "bookmark_name_exists_question": "Zaznamek z imenom '{0}' že obstaja na tej strani.\nVseeno preimenujem?",

        "context_bookmarks": "Zaznamki",
        "context_bookmark_add_here": "Dodaj zaznamek za to stran",
        "context_bookmarks_existing": "Obstoječi zaznamki:",
        "context_bookmarks_jump": "Skoči na zaznamek:",
        "context_bookmarks_none": "Ni zaznamkov",
        "context_bookmarks_clear_all": "Odstrani vseh {0} zaznamkov",

        "bookmark_search_placeholder": "Išči zaznamke... (ime ali stran)",
        "bookmark_search_results": "Najdenih %d zaznamkov za \"%s\"",
        "bookmark_no_search_results": "Ni najdenih zaznamkov za \"%s\"",
        "bookmark_no_search_results_label": "Ni rezultatov za \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Uredi PDF metapodatke",
        "metadata_title": "Naslov",
        "metadata_title_placeholder": "Naslov dokumenta",
        "metadata_title_tooltip": "Naslov dokumenta (prikaže se v naslovni vrstici)",
        "metadata_author": "Avtor",
        "metadata_author_placeholder": "Ime avtorja",
        "metadata_author_tooltip": "Ustvarjalec dokumenta",
        "metadata_subject": "Zadeva",
        "metadata_subject_placeholder": "Zadeva dokumenta",
        "metadata_subject_tooltip": "Kratek opis vsebine",
        "metadata_keywords": "Ključne besede",
        "metadata_keywords_placeholder": "Ključne besede, ločene z vejicami",
        "metadata_keywords_tooltip": "Ključne besede za kategorizacijo dokumenta",
        "metadata_creator": "Ustvarjalec",
        "metadata_creator_placeholder": "Aplikacija, ki je ustvarila PDF",
        "metadata_creator_tooltip": "Programska oprema, s katero je bil dokument ustvarjen",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Aplikacija, ki je pretvorila PDF",
        "metadata_producer_tooltip": "Programska oprema, ki je pretvorila PDF",
        "metadata_creation_date": "Datum ustvarjanja",
        "metadata_creation_date_tooltip": "Datum ustvarjanja dokumenta",
        "metadata_mod_date": "Datum spremembe",
        "metadata_mod_date_tooltip": "Datum zadnje spremembe",
        "metadata_pdf_info": "📄 Informacije o PDF",
        "metadata_pages": "Število strani",
        "metadata_file_size": "Velikost datoteke",
        "metadata_pdf_version": "Različica PDF",
        "metadata_encrypted": "Šifrirano",
        "metadata_encrypted_yes": "Da (zaščiteno z geslom)",
        "metadata_encrypted_no": "Ne",
        "metadata_reload": "📂 Ponovno naloži iz PDF",
        "metadata_reset": "Zavrzi spremembe",
        "metadata_reloaded": "Metapodatki so bili ponovno naloženi iz PDF.",
        "metadata_reset_done": "Vsa polja metapodatkov so bila ponastavljena.",
        "metadata_no_file": "Nobena datoteka PDF ni naložena.",
        "metadata_save_error": "Napaka pri shranjevanju metapodatkov",
        "metadata_saved": "Metapodatki so bili uspešno shranjeni.",
        "metadata_pdf_version_unknown": "PDF (neznano)",
        "metadata_saved_message": "Metapodatki so bili uspešno shranjeni.",
        "metadata_saved_voice": "Metapodatki shranjeni.",

        "metadata_custom": "🔧 Metapodatki po meri",
        "metadata_custom_placeholder": "{\n  \"moje_polje\": \"moja_vrednost\",\n  \"drugo_polje\": 123\n}",
        "metadata_custom_tooltip": "Format JSON za metapodatke po meri (izbirno)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Predloga \"{0}\" izbrana - Dvokliknite za vstavljanje",
        "text_use_template": "Uporabi besedilni blok",
        "text_type": "Vrsta",
        "text_search_templates": "Išči besedilne bloke...",

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

        <h3>📦 Kaj se izvozi? (Pregled)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Splošne nastavitve aplikacije</span></li>
            <li class="detail">• Temni/Svetli način</li>
            <li class="detail">• Inverzija temnega načina za slike</li>
            <li class="detail">• Siva mejna vrednost</li>
            <li class="detail">• Jezik</li>
            <li class="detail">• Geometrija okna</li>
            <li class="detail">• Način približevanja</li>
            <li class="detail">• Navigacija (Navigacijska vrstica vidna)</li>
            <li class="detail">• Govorni izhod (vklopljeno/izklopljeno)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavitve varnostnega kopiranja</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Poimenovanje datotek (Časovni žig, Ločilo, Pripone)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavitve za vstavljanja</span></li>
            <li class="detail">• Podpisi</li>
            <li class="detail">• Besedilo in besedilni bloki</li>
            <li class="detail">• Kljukice, slike in oblike</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavitve OCR</span></li>
            <li class="detail">• Jezik</li>
            <li class="detail">• Vsili OCR · Način strani</li>
            <li class="detail">• Predobdelava slike: Popravi poševnost, Počisti, Prekomerno vzorčenje</li>
            <li class="detail">• Število vzporednih opravil</li>
            <li class="detail">• Način inverzije</li>
            <li class="detail">• Siva mejna vrednost</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Zaznamki</span></li>
            <li class="detail">• Vsi zaznamki na datoteko PDF (Stran, Ime, Čas ustvarjanja)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Baza podatkov gesel</span></li>
            <li class="detail">• Shranjena gesla PDF (izbirno šifrirana ali golo besedilo)</li>
            <li class="detail">• Zgoščena vrednost glavnega gesla (če je nastavljeno)</li>
            <li class="detail">• Podatki za preverjanje</li>
        </ul>

        <h4>⚠️ Pomembne opombe</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Pri uvozu:</strong>
            <ul>
                <li><span class="warning">➜ VSE trenutne nastavitve bodo v celoti prepisane</span></li>
                <li>• Ponovni zagon aplikacije je obvezen</li>
                <li>• Obstoječi podpisi, besedilni bloki in zaznamki bodo zamenjani</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Glavno geslo in način izvoza:</strong>
            <ul>
                <li>• Ko je glavno geslo aktivno, lahko izberete:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dešifrirano</strong></span> (gesla so v ZIP kot golo besedilo)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Šifrirano</strong></span> (berljivo samo z glavnim geslom na ciljnem sistemu)</li>
                <li>• Zgoščena vrednost glavnega gesla je <strong>vedno</strong> shranjena šifrirano</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Varnostno obvestilo:</strong>
            <ul>
                <li>• Izvožena datoteka ZIP vsebuje občutljive podatke (<strong>gesla, zaznamke, podpise</strong>)</li>
                <li>• Hranite jo na varnem mestu (npr. šifriran USB ključek, upravljalnik gesel)</li>
                <li>• Če datoteka izgine, so shranjena gesla PDF nepovratno izgubljena</li>
            </ul>
        </div>

        <h4>📁 Format izvoza</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Nastavitve se shranijo v eno samo datoteko ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ta ZIP vsebuje celotno <code>settings.json</code> (iz vaše konfiguracije) ter morebitne vgrajene slikovne datoteke podpisov in šifrirana gesla.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Podpisi - Vodnik",
        'signature_guide_html': """
        📝 <strong>Podpisi - Kratek vodnik</strong><br>
        <ul>
        <li>Nastavite glavno geslo</li>
        <li>Konfigurirajte podpise v meniju <em>Nastavitve</em> (velikost, časovni žig, …)</li>
        <li>Vstavite z <strong>DESNIM KLIKOM</strong> na želeni položaj (glavno geslo potrebno enkrat na sejo)</li>
        <li>Premaknite podpis z miško ali puščičnimi tipkami</li>
        <li>Vstavite več podpisov zaporedoma</li>
        <li>Prilagodite vsak podpis posebej</li>
        <li>Zavrzite posamezen podpis</li>
        <li>Shranite / zavrzite vse podpise naenkrat</li>
        <li>Namesto tega lahko uporabite tudi menijsko vrstico.</li>
        </ul>
        """,
        'signature_guide_voice': "Kratek vodnik za podpise. Nastavite glavno geslo. Konfigurirajte podpise v nastavitvah. Vstavite z desnim klikom.",

        'image_guide_title': "Vstavljanje slik - Vodnik",
        'image_guide_html': """
        📷 <strong>Vstavljanje slik v PDF - Kratek vodnik</strong><br>
        <ol>
        <li>Desni klik na želeni položaj</li>
        <li><em>„Vstavi sliko“</em> → Izberite sliko</li>
        <li>Pozicionirajte sliko: Povlecite z miško</li>
        <li>Prilagodite velikost: Povlecite za vogale/robove</li>
        <li>Ohranite razmerje stranic: Tipka <strong>[A]</strong></li>
        <li>Nadaljnje prilagoditve: Desni klik na sliki</li>
        </ol>
        <p><strong>Namig:</strong> V kontekstnem meniju lahko prilagodite nastavitve.</p>
        """,
        'image_guide_voice': "Kratek vodnik za slike. Desni klik, vstavi sliko, izberite. Pozicionirajte z miško, prilagodite velikost na vogalih. Razmerje stranic s tipko A.",

        'form_guide_title': "Vstavljanje oblik - Vodnik",
        'form_guide_html': """
        📐 <strong>Vstavljanje oblik v PDF - Kratek vodnik</strong><br>
        <ol>
        <li>Izberite vrsto oblike (pravokotnik, elipsa, črta, puščica)</li>
        <li>Kliknite na položaj:
            <ul>
            <li>Za pravokotnik/elipso: En klik postavi obliko</li>
            <li>Za črto/puščico: Dva klika za začetno in končno točko</li>
            </ul>
        </li>
        <li>Pozicionirajte obliko: Povlecite z miško</li>
        <li>Prilagodite velikost: Povlecite za vogale/robove</li>
        <li>Shranite obliko: <strong>Enter</strong></li>
        <li>Zavrzite obliko: <strong>ESC</strong></li>
        <li>Nadaljnje prilagoditve: Desni klik na obliki</li>
        </ol>
        <p><strong>Namig:</strong> V kontekstnem meniju lahko prilagodite nastavitve.</p>
        """,
        'form_guide_voice': "Kratek vodnik za oblike. Izberite vrsto oblike. Za pravokotnik ali elipso kliknite enkrat, za črto ali puščico dvakrat. Pozicionirajte z miško, prilagodite velikost na vogalih. Shranite z Enter, zavrzite z Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "prejšnji",
        "btn_next_result": "naslednji",
        "ocr_text_window": "OCR okno za besedilo",
        "bookmark_existing": "Obstoječi zaznamki",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Primerjava OCR Mac - Windows",
        'ocr_method_mac_win_title': "Razlike OCR med Mac in Windows",
        'ocr_method_mac_win_voice': "Mac je boljši",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Razlike med macOS in Windows</strong></p>

        <p><strong>macOS (priporočeno)</strong></p>
        <p>Orodje:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Rezultat:</p>
        <ul>
        <li>Iskalni PDF z vdelanim besedilom, ki v veliki meri ohrani prvotno postavitev.</li>
        </ul>
        <p>Prednosti:</p>
        <ul>
        <li>Odlična kakovost prepoznavanja besedila (tudi na ukrivljenih straneh).</li>
        <li>Ohranjanje vektorske grafike in pisav.</li>
        <li>Vrstica napredka GUI prek vrednotenja podprocesa.</li>
        <li>Popoln nadzor nad vsemi parametri OCR (Deskew, Clean, Oversample, optimizacija).</li>
        <li>Iskanje besedila je na voljo neposredno v glavnem oknu (pogled PDF).</li>
        </ul>
        <p>Slabosti:</p>
        <ul>
        <li>Zahteva dodatna sistemska orodja (ocrmypdf, Ghostscript, unpaper, pngquant – vključena v paket aplikacije).</li>
        <li>Bolj zapleteno obravnavanje napak (blokade, časovne omejitve).</li>
        </ul>

        <p><strong>Windows (stabilna alternativa)</strong></p>
        <p>Orodje:</p>
        <ul>
        <li>pytesseract (neposredna povezava s Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Rezultat:</p>
        <ul>
        <li>Iskalni PDF, ki vizualno ustreza slikovnemu PDF, vendar je iskalni prek prozornega besedila.</li>
        </ul>
        <p>Prednosti:</p>
        <ul>
        <li>Trenutno se nobena ne spomnim.</li>
        </ul>
        <p>Slabosti:</p>
        <ul>
        <li>PDF je v bistvu slika z nevidnim besedilom; postavitev se lahko pri zapletenih dokumentih (stolpci, tabele) nekoliko razlikuje.</li>
        <li>Brez samodejnega popravljanja poševnosti (--deskew) ali čiščenja slike (--clean).</li>
        <li>Vrstica napredka GUI se posodablja le grobo na podlagi števila obdelanih strani.</li>
        <li>Hitrost OCR je nekoliko počasnejša (ker se vsaka stran obdeluje posebej).</li>
        <li>Iskanje besedila se preusmeri v OCR okno za besedilo.</li>
        </ul>

        <p><strong>Skupne značilnosti</strong></p>
        <ul>
        <li>Obe metodi ustvarita iskalni PDF v istem imeniku kot izvorna datoteka.</li>
        <li>Nastavitve OCR (jezik, DPI, način segmentacije strani, način pogona OCR) je mogoče konfigurirati prek OCRSettingsDialog in veljajo v obeh izvedbah.</li>
        </ul>

        <p><strong>Priporočilo:</strong></p>
        <ul>
        <li>macOS: Dvojiška datoteka ocrmypdf daje najboljše rezultate – Kupite Mac in uporabite različico (PDFDarkView za Mac z Apple Silicon ali Intel čipom). Rezultati OCR so boljši kot v Windows!</li>
        <li>Windows: Uporabite rešitev pytesseract. Stabilna je in zagotavlja povsem zadostno kakovost za večino dokumentov.</li>
        </ul>

        <p><strong>Pomembno obvestilo:</strong></p>
        <ul>
        <li>Obe različici sta popolnoma integrirani v uporabniški vmesnik – uporabnik ne opazi nobene razlike.</li>
        <li>Program samodejno odloči, kateri pogon OCR uporabiti, glede na operacijski sistem.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Ustvari podpis (iz skeniranja)",
        "signature_create_title": "Izberite skenirani podpis (PDF/slika)",
        "image_pdf_filter": "Slike in PDF",
        "signature_pdf_empty": "PDF ne vsebuje strani.",
        "signature_created_success": "Podpis je bil uspešno ustvarjen: {0}",
        "signature_create_error": "Napaka pri ustvarjanju podpisa:\n{0}",
        "rembg_missing": "rembg ni nameščen.\nNamestite: pip install rembg\nNapaka: {0}",
        "signature_name_title": "Ime datoteke za podpis",
        "signature_name_message": "Vnesite ime datoteke za nov podpis (shranjen bo kot PNG s prozornim ozadjem):",
        "signature_name_label": "Ime datoteke:",
        "signature_name_voice": "Vnesite ime datoteke za podpis",
        "signature_processing": "Obdelava poteka...",
        "signature_creation_title": "Ustvarjanje podpisa",
        "signature_overwrite_warning": "Datoteka '{0}' že obstaja. Prepišem?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Pripravite PDF za podpis",
        "signature_prepare_instruction":"Izberite PDF, ki na eni sami strani vsebuje skenirani podpis.\n\nZa optimalno prepoznavanje zagotovite:\n• Podpis je napisan s črnim črnilom (kemični svinčnik ali fineliner) na belem papirju.\n• Podpis je v zgornji tretjini sicer prazne strani A4.\n• PDF je bil skeniran z najmanj 300 dpi.\n• Podpis je jasen in ne preveč tanek.\n• Ni motečih vzorcev ozadja ali črt.",
        "signature_prepare_voice":"Izberite PDF s skeniranim podpisom. Bodite pozorni na dobro kakovost in kontrast.",
        "sig_thickness_label":"Debelina črte:",
        "sig_thickness_normal":"Normalna (tanka)",
        "sig_thickness_bold":"Krepka (priporočeno)",
        "sig_thickness_very_bold":"Zelo krepka",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Dodajanje jezikov GUI in OCR - Vodnik",
        'language_guide_title': "Dodajanje jezikov GUI in OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Prenesite želeno prevajalsko datoteko <code>translations_xy.py</code> s<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        in jo postavite v naslednji imenik:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Odprite spletni brskalnik.</li>
        <li>Pojdite na: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Na desnem robu zaslona poiščite "Releases" in izberite tistega z oznako <strong>"latest"</strong>.</li>
        <li>Na naslednji strani izdaje prenesite datoteko <code>Source Code.zip</code> čisto na dnu.</li>
        <li>Razširite datoteko ZIP.</li>
        <li>V razširjeni mapi poiščite vse jezikovne datoteke, ki jih potrebujete, in jih kopirajte v imenik:<br/>
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
        "menu_watermark":"Vstavi vodni žig",
        "fullpage_text_watermark_title":"Besedilo kot vodni žig",
        "fullpage_image_watermark_title":"Slika kot vodni žig",
        "filename_with_watermark":"_z_vodnim_zigom",
        "watermark_text":"Besedilo:",
        "watermark_text_placeholder":"Vaše besedilo vodnega žiga...",
        "watermark_font_family":"Pisava:",
        "watermark_font_size":"Velikost pisave:",
        "watermark_format":"Oblikovanje:",
        "watermark_bold":"Krepko",
        "watermark_italic":"Poševno",
        "watermark_color":"Barva:",
        "watermark_choose_color":"Izberite barvo...",
        "watermark_opacity":"Motnost / Prosojnost:",
        "watermark_direction":"Smer branja:",
        "watermark_direction_l_r":"Levo → Desno",
        "watermark_direction_bl_tr":"Spodaj levo → Zgoraj desno",
        "watermark_direction_tl_br":"Zgoraj levo → Spodaj",
        "watermark_direction_b_t":"Spodaj → Zgoraj",
        "watermark_direction_t_b":"Zgoraj → Spodaj",
        "watermark_preview":"Predogled:",
        "watermark_preview_sample":"Primer besedila",
        "watermark_empty_text":"Prosimo, vnesite besedilo.",
        "watermark_applied":"Vodni žig je bil uporabljen na vseh straneh.",
        "watermark_saved":"Vodni žig je bil shranjen.",
        "image_scale":"Velikost:",
        "image_preview":"Predogled slike:",
        "no_image_selected":"Ni izbrane slike",
        "browse":"Prebrskaj...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Izbrisi",
        "redact_add_black": "Izbris (črna)",
        "redact_add_white": "Izbris (bela / brisanje)",
        "redact_added_black": "Dodan črn izbris",
        "redact_added_white": "Dodan bel izbris",
        "redact_apply_all": "Uporabi vse izbrise in shrani",
        "redact_discard_all": "Zavrzi vse izbrise",
        "redact_discard": "Zavrzi ta izbris",
        "no_redactions": "Ni izbrisov",
        "redact_confirm_title": "Trajno uporabi izbrise",
        "redact_confirm_message": "Opozorilo: Označena območja bodo trajno izbrisana (črna ali bela).\nVarnostna kopija bo ustvarjena (če je omogočena).\n\nNadaljuj?",
        "redact_apply": "Da, izbriši zdaj",
        "redact_saved": "{0} izbris(ov) uspešno uporabljen in shranjen.",
        "redact_saved_voice": "{0} izbris(ov) uporabljen",
        "redact_error": "Napaka med brisanjem",
        "filename_redacted":"_izbrisano",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Vstavi številke strani',
        'page_numbers_format': 'Oblika številke:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabsko)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (rimske male)',
        'page_numbers_format_roman_upper': 'I, II, III ... (rimske velike)',
        'page_numbers_format_letter': 'A, B, C ... (črke)',
        'page_numbers_format_custom': 'Po meri',
        'page_numbers_custom_pattern': 'Vzorec:',
        'page_numbers_custom_placeholder': 'npr. "Stran {nummer}" ali "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Uporabite {nummer} za trenutno številko strani in {total} za skupno število',
        'page_numbers_position': 'Položaj:',
        'page_numbers_pos_tl': 'Zgoraj levo',
        'page_numbers_pos_tc': 'Zgoraj sredina',
        'page_numbers_pos_tr': 'Zgoraj desno',
        'page_numbers_pos_ml': 'Sredina levo',
        'page_numbers_pos_mc': 'Centrirano',
        'page_numbers_pos_mr': 'Sredina desno',
        'page_numbers_pos_bl': 'Spodaj levo',
        'page_numbers_pos_bc': 'Spodaj sredina',
        'page_numbers_pos_br': 'Spodaj desno',
        'page_numbers_margins': 'Robovi:',
        'page_numbers_margin_x': 'Vodoravna razdalja:',
        'page_numbers_margin_y': 'Navpična razdalja:',
        'page_numbers_range': 'Obseg strani:',
        'page_numbers_all_pages': 'Vse strani',
        'page_numbers_custom_range': 'Obseg po meri',
        'page_numbers_from': 'Od:',
        'page_numbers_to': 'Do:',
        'page_numbers_progress': 'Vstavljanje številk strani...',
        'page_numbers_start': 'Zagon vstavljanja številk strani...',
        'page_numbers_cancel': 'Vstavljanje številk strani preklicano',
        'page_numbers_success': 'Številke strani so bile uspešno dodane.\n\nAli želite odpreti nov PDF?\n\n{0}',
        'page_numbers_complete': 'Številke strani so bile dodane',
        'page_numbers_error_format': 'Napaka pri vstavljanju številk strani: {0}',
        'page_numbers_content_type': 'Vrsta vsebine:',
        'page_numbers_tab_simple': 'Preprosta številka',
        'page_numbers_tab_range': 'Stran X od Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Prosto besedilo',
        'page_numbers_range_format': 'Oblika:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Stran {aktuell} od {gesamt}',
        'page_numbers_range_custom': 'Po meri',
        'page_numbers_range_placeholder': 'npr. "Stran {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Oblika datuma:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. januar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Po meri',
        'page_numbers_date_placeholder': 'npr. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Položaj:',
        'page_numbers_date_before': 'Datum pred številko strani',
        'page_numbers_date_after': 'Datum za številko strani',
        'page_numbers_date_only': 'Samo datum (brez številke strani)',
        'page_numbers_custom_text': 'Besedilo po meri:',
        'page_numbers_custom_placeholder_text': 'Uporabite {seite} za številko strani in {gesamt} za skupno število\nnpr. "Zaupno - Stran {seite}" ali "{seite} od {gesamt}"',
        "filename_with_page_number":"_s_stevilko_strani",
        "filename_with_page_declaration":"_z_oznako_strani",
        "filename_with_pagenumber":"_s_stevilko_strani",
        "filename_with_date":"_z_datumom",
        "filename_with_my_page_declaration":"_z_oznako_po_meri",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Neshranjene spremembe",
        "unsaved_changes_message_darkmode": "Obstajajo neshranjena vstavljanja.\nAli jih želite shraniti pred preklopom?",
        "save_and_switch": "Shrani in preklopi",
        "discard_and_switch": "Preklopi zdaj",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Izvozi strani kot slike',
        'export_images_menu': 'Izvozi kot slike (PNG/JPEG)',
        'export_images_format': 'Oblika slike:',
        'export_images_dpi': 'Ločljivost (DPI):',
        'export_images_quality': 'Kakovost JPEG:',
        'export_images_range': 'Obseg strani:',
        'export_images_all_pages': 'Vse strani',
        'export_images_custom_range': 'Obseg po meri',
        'export_images_from': 'Od:',
        'export_images_to': 'Do:',
        'export_images_options': 'Možnosti:',
        'export_images_single_files': 'Vsaka stran kot ločena datoteka',
        'export_images_subfolder': 'Izvozi v podmapo',
        'export_images_subfolder_info': 'V podmapo "imePDF_slike"',
        'export_images_same_folder': 'V isti mapi kot PDF',
        'export_images_apply_darkmode': 'Uporabi nastavitve PDFDarkView (Temni način)',
        'export_images_target_folder': 'Ciljna mapa:',
        'export_images_browse': 'Prebrskaj...',
        'export_images_preview': 'Predogled:',
        'export_images_preview_info': 'Izberite nastavitve za izvoz',
        'export_images_preview_info_detail': '{0} strani kot {1}\nLočljivost: {2} DPI\nIme datoteke: {3}\n{4}',
        'export_images_select_folder': 'Izberite ciljno mapo',
        'export_images_start': 'Zagon izvoza slik...',
        'export_images_progress': 'Izvažanje slik...',
        'export_images_saving': 'Shranjevanje strani {0} od {1}...',
        'export_images_success': 'Izvoz uspešen!\n\n{0} slik je bilo shranjenih v:\n{1}',
        'export_images_complete': 'Izvoz slik končan',
        'export_images_open_folder': '📁 Odpri mapo',
        'export_images_cancel': 'Izvoz slik preklican',
        'export_images_error_format': 'Napaka pri izvažanju slik: {0}',
        'export_images_pdf2image_missing': 'Knjižnica "pdf2image" ni nameščena.\n\nProsimo, namestite jo z:\npip install pdf2image\n\nZa Windows potrebujete tudi Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konverzija za dolgoročno arhiviranje',
        'pdfa_menu': 'PDF/A konverzija (primerno za arhiv)',
        'pdfa_info': 'Pretvori PDF v PDF/A format.\n\nPDF/A je posebej razvit za dolgoročno arhiviranje in zagotavlja, da bo dokument v prihodnosti pravilno prikazan.',
        'pdfa_standard': 'PDF/A standard:',
        'pdfa_standard_select': 'Različica:',
        'pdfa_1': 'PDF/A-1 (preprost, široko združljiv)',
        'pdfa_2': 'PDF/A-2 (sodoben, boljša kompresija)',
        'pdfa_3': 'PDF/A-3 (najnovejša različica, dovoljuje priloge)',
        'pdfa_standards_explanation': '📖 Razlaga standardov:\n\n'
            '• PDF/A-1: Osnovni, združljiv s starejšimi sistemi (pribl. 2005)\n'
            '• PDF/A-2: Sodobnejši, boljša kompresija, podpora za prosojnost (pribl. 2011)\n'
            '• PDF/A-3: Najnovejša različica, dovoljuje vgrajevanje prilog (pribl. 2013)\n\n'
            'Priporočilo: PDF/A-2 je dober kompromis med združljivostjo in sodobnimi funkcijami.',
        'pdfa_options': 'Možnosti:',
        'pdfa_compress_enable': 'Stisni PDF (manjša datoteka)',
        'pdfa_metadata_preserve': 'Ohrani metapodatke (naslov, avtor, itd.)',
        'pdfa_target_folder': 'Ciljna mapa:',
        'pdfa_browse': 'Prebrskaj...',
        'pdfa_select_folder': 'Izberite ciljno mapo',
        'pdfa_ocr_info_unknown': '🔍 Ni bilo mogoče preveriti vsebine besedila.',
        'pdfa_ocr_info_not_needed': '✅ Besedilo na voljo - OCR ni potreben.\nPDF/A je mogoče ustvariti neposredno.',
        'pdfa_ocr_info_recommended': '⚠️ Ni bilo najdeno zadostno besedilo.\n\nZa iskalne PDF priporočamo, da najprej zaženete OCR.\nOpomba: PDF/A deluje tudi brez OCR - vendar besedilo ne bo iskalno.',
        'pdfa_ocr_info_error': '❌ Napaka pri preverjanju: {0}',
        'pdfa_start': 'Zagon PDF/A konverzije...',
        'pdfa_progress': 'PDF/A konverzija v teku...',
        'pdfa_success': 'PDF/A konverzija uspešna!\n\nShranjeno kot:\n{0}\n\nAli želite odpreti nov PDF?',
        'pdfa_complete': 'PDF/A konverzija končana',
        'pdfa_cancel': 'PDF/A konverzija preklicana',
        'pdfa_error_format': 'Napaka pri PDF/A konverziji:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Knjižnica "ocrmypdf" ni nameščena.\n\nProsimo, namestite jo z:\npip install ocrmypdf',
        'btn_convert': 'Pretvori',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimiziraj PDF (zmanjšaj velikost datoteke)',
        'optimize_menu': 'Optimiziraj PDF (velikost datoteke)',
        'optimize_info': 'Zmanjša velikost PDF datoteke z različnimi metodami optimizacije.\n\nVišja kot je stopnja kompresije, manjša postane datoteka - z možno izgubo kakovosti slik.',
        'optimize_level': 'Stopnja kompresije:',
        'optimize_level_low': 'Nizka (hitro, majhen prihranek)',
        'optimize_level_medium': 'Srednja (dober kompromis)',
        'optimize_level_high': 'Visoka (velik prihranek)',
        'optimize_level_maximum': 'Največja (največji prihranek, počasi)',
        'optimize_level_explanation': 'Priporočilo: "Srednja" je dober kompromis med hitrostjo in velikostjo datoteke.',
        'optimize_options': 'Možnosti:',
        'optimize_compress_images': 'Stisni slike (zmanjšaj kakovost JPEG)',
        'optimize_clean_objects': 'Odstrani neuporabljene predmete',
        'optimize_preserve_metadata': 'Ohrani metapodatke (naslov, avtor, itd.)',
        'optimize_image_quality': 'Kakovost slike:',
        'optimize_range': 'Obseg strani:',
        'optimize_all_pages': 'Vse strani',
        'optimize_custom_range': 'Obseg po meri',
        'optimize_from': 'Od:',
        'optimize_to': 'Do:',
        'optimize_target_folder': 'Ciljna mapa:',
        'optimize_browse': 'Prebrskaj...',
        'optimize_select_folder': 'Izberite ciljno mapo',
        'optimize_info_box': 'Informacije',
        'optimize_info_text': 'Optimizacija lahko za velike PDF traja več minut.\n\nSlike se shranjujejo z zmanjšano kakovostjo, kar lahko znatno zmanjša velikost datoteke.',
        'optimize_start': 'Zagon PDF optimizacije...',
        'optimize_progress': 'Optimizacija PDF...',
        'optimize_cancel': 'PDF optimizacija preklicana',
        'optimize_complete': 'PDF optimizacija končana',
        'optimize_error_format': 'Napaka pri PDF optimizaciji:\n\n{0}',
        'optimize_success_message': 'PDF optimizacija uspešna!\n\nShranjeno kot:\n{0}\n\nPrej: {1}\nZdaj: {2}\nPrihranek: {3:.1f}%\n\n{4}\n\nAli želite odpreti optimizirani PDF?',
        'optimize_success_message_no_size': 'PDF optimizacija uspešna!\n\nShranjeno kot:\n{0}\n\nInformacija o velikosti ni na voljo.\n\nAli želite odpreti optimizirani PDF?',
        'optimize_result_positive': 'Datoteka je bila zmanjšana za {0:.1f}%.',
        'optimize_result_zero': 'Brez spremembe velikosti datoteke.',
        'optimize_result_negative': 'Datoteka se je povečala za {0:.1f}%.\nOptimizacija je bila preskočena, izvirna datoteka je bila ohranjena.',
        'btn_optimize': 'Začni optimizacijo',
        'filename_optimize_low_suffix': '_optimizirano_nizko',
        'filename_optimize_medium_suffix': '_optimizirano',
        'filename_optimize_high_suffix': '_optimizirano_visoko',
        'filename_optimize_maximum_suffix': '_optimizirano_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Obreži PDF',
        'crop_menu': 'Obreži PDF (Crop)',
        'crop_range': 'Uporabi na:',
        'crop_all_pages': 'Vse strani',
        'crop_current_page': 'Samo trenutna stran',
        'crop_values': 'Vrednosti obrezovanja (v točkah):',
        'crop_left': 'Levo:',
        'crop_right': 'Desno:',
        'crop_top': 'Zgoraj:',
        'crop_bottom': 'Spodaj:',
        'crop_presets': 'Prednastavitve:',
        'crop_preset_white': 'Zaznaj bele robove',
        'crop_reset': 'Ponastavi',
        'crop_mouse_hint': '🖱️ Povlecite pravokotnik za grobo izbiro območja.\nNato lahko natančno prilagodite vrednosti v SpinBoxih.\nRočno prilagajanje z miško ni mogoče.',
        'crop_apply': 'Obreži',
        'crop_scope_all': 'Vse strani',
        'crop_scope_current': 'Trenutna stran',
        'crop_new_size': 'Nova velikost: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Ni naloženega PDF',
        'crop_preview_error': 'Napaka pri nalaganju predogleda',
        'crop_start': 'Zagon obrezovanja...',
        'crop_progress': 'Obrezovanje PDF...',
        'crop_success': 'PDF uspešno obrezan!\n\nShranjeno kot:\n{0}\n\nAli želite odpreti obrezani PDF?',
        'crop_complete': 'Obrezovanje končano',
        'crop_cancel': 'Obrezovanje preklicano',
        'crop_error_format': 'Napaka pri obrezovanju:\n\n{0}',
        'filename_crop_suffix': '_obrezano',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Splošči PDF (Flatten)',
        'flatten_menu': 'Splošči PDF (Flatten)',
        'flatten_info': 'Sploščanje PDF "vžge" vse uredljive elemente v vsebino strani.\n\nPo tem polja obrazcev, opombe, besedila, križi, podpisi, slike in oblike niso več posamično uredljivi.',
        'flatten_explanation_title': '📖 Za kaj je to dobro?',
        'flatten_explanation_text': 'Sploščanje je potrebno v naslednjih situacijah:\n\n'
            '• 📄 Želite pripraviti dokument za tiskanje\n'
            '• 🔒 Želite preprečiti, da bi nekdo spreminjal polja obrazcev\n'
            '• 📎 Želite "trajno" vgraditi opombe in komentarje v dokument\n'
            '• 🖼️ Želite trajno vgraditi besedila, križe, podpise, slike in oblike v dokument\n'
            '• 📦 Želite pripraviti datoteko za arhiviranje\n\n'
            'Sploščanje naredi PDF manjši in preprečuje naključno premikanje ali brisanje elementov.',
        'flatten_what_title': 'Kaj se splošči?',
        'flatten_what_list': '• ✅ Polja obrazcev (besedilna polja, potrditvena polja, gumbi)\n'
            '• ✅ Opombe (komentarji, poudarki, opombe)\n'
            '• ✅ Prekrivanja (besedila, križi, podpisi, slike, oblike)',
        'flatten_options': 'Možnosti:',
        'flatten_forms': 'Splošči polja obrazcev',
        'flatten_annotations': 'Splošči opombe',
        'flatten_overlays': 'Splošči prekrivanja (besedila, križi, podpisi, slike, oblike)',
        'flatten_target_folder': 'Ciljna mapa:',
        'flatten_browse': 'Prebrskaj...',
        'flatten_select_folder': 'Izberite ciljno mapo',
        'flatten_warning': '⚠️ Pomembno: Sploščanje je nepovraten proces!\n\nPo sploščanju uredljivih elementov ni več mogoče posamično spreminjati ali brisati.\nPo potrebi predhodno ustvarite varnostno kopijo.',
        'flatten_apply': 'Splošči',
        'flatten_start': 'Zagon sploščanja...',
        'flatten_progress': 'Sploščanje PDF...',
        'flatten_success': 'PDF uspešno sploščen!\n\nShranjeno kot:\n{0}\n\nAli želite odpreti sploščeni PDF?',
        'flatten_complete': 'Sploščanje končano',
        'flatten_cancel': 'Sploščanje preklicano',
        'flatten_error_format': 'Napaka pri sploščanju:\n\n{0}',
        'filename_flatten_suffix': '_splosceeno',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Prekrivanje PDF (Overlay)',
        'overlay_menu': 'Prekrivanje PDF (Overlay)',
        'overlay_info': 'Postavi en PDF (prekrivanje) čez drug PDF.\n\nPrekrivni PDF se postavi na osnovni PDF. To je uporabno za vodne žige, logotipe, glave pisem ali žige.',
        'overlay_explanation_title': '📖 Za kaj je to dobro?',
        'overlay_explanation_text': 'Prekrivanje je potrebno v naslednjih situacijah:\n\n'
            '• 🏢 Postavitev logotipa podjetja kot vodnega žiga na vsako stran\n'
            '• 📄 Postavitev glave pisma na prazen PDF\n'
            '• 🖊️ Postavitev prekrivanja žiga na dokument\n'
            '• 🔖 Postavitev vodnega žiga na vse strani\n'
            '• 📑 Postavitev prekrivanja obrazca na predlogo',
        'overlay_type': 'Vrsta prekrivanja:',
        'overlay_type_fullpage': 'Celotna stran (prekriva)',
        'overlay_type_transparent': 'Celotna stran (prozorno - priporočeno)',
        'overlay_type_stamp': 'Žig (mogoče pozicionirati)',
        'overlay_type_info_fullpage': '📄 Prekrivni PDF se postavi natančno čez celotno stran.\nBelo ozadje je mogoče odstraniti, tako da ostane vidna samo vsebina.',
        'overlay_type_info_transparent': '🔍 Prekrivni PDF se postavi čez celotno stran s prozornim ozadjem.\nBelo ozadje se samodejno odstrani - idealno za vodne žige in logotipe!',
        'overlay_type_info_stamp': '🖊️ Prekrivni PDF se pozicionira in prilagodi kot žig.\nPopoln za logotipe, žige ali podpise na določenih položajih.',
        'overlay_remove_background': 'Odstrani belo ozadje:',
        'overlay_remove_background_enable': 'Odstrani belo ozadje iz prekrivnega PDF (naredi prekrivanje prozorno)',
        'overlay_remove_background_tooltip': 'Odstrani bele površine iz prekrivnega PDF, tako da postane spodnje besedilo vidno.',
        'overlay_threshold': 'Prag vrednosti:',
        'overlay_threshold_hint': '(1-254, višji = več belega se odstrani)',
        'overlay_select_file': 'Izberite prekrivni PDF:',
        'overlay_file_placeholder': 'Prosimo, izberite PDF datoteko za prekrivanje',
        'overlay_browse': 'Prebrskaj...',
        'overlay_select_overlay': 'Izberite prekrivni PDF',
        'overlay_range': 'Obseg strani:',
        'overlay_all_pages': 'Vse strani',
        'overlay_custom_range': 'Obseg po meri',
        'overlay_from': 'Od:',
        'overlay_to': 'Do:',
        'overlay_position': 'Položaj:',
        'overlay_position_center': 'Sredina',
        'overlay_position_top_left': 'Zgoraj levo',
        'overlay_position_top_right': 'Zgoraj desno',
        'overlay_position_bottom_left': 'Spodaj levo',
        'overlay_position_bottom_right': 'Spodaj desno',
        'overlay_size': 'Velikost:',
        'overlay_size_original': 'Izvirna velikost',
        'overlay_size_fit_page': 'Prilagodi strani',
        'overlay_size_custom': 'Po meri (%)',
        'overlay_opacity': 'Prosojnost:',
        'overlay_target_folder': 'Ciljna mapa:',
        'overlay_browse_folder': 'Prebrskaj...',
        'overlay_select_folder': 'Izberite ciljno mapo',
        'overlay_warning': '⚠️ Opomba: Prekrivni PDF se postavi na osnovni PDF in se "vžge" vanj.\n\nElementov prekrivnega PDF po shranjevanju ni več mogoče posamično urejati.',
        'overlay_apply': 'Prekrij',
        'overlay_start': 'Zagon prekrivanja...',
        'overlay_progress': 'Prekrivanje PDF...',
        'overlay_success': 'PDF uspešno prekrit!\n\nShranjeno kot:\n{0}\n\nAli želite odpreti prekriti PDF?',
        'overlay_complete': 'Prekrivanje končano',
        'overlay_cancel': 'Prekrivanje preklicano',
        'overlay_error_format': 'Napaka pri prekrivanju:\n\n{0}',
        'overlay_no_file': 'Ni izbranega prekrivnega PDF.\n\nProsimo, izberite PDF datoteko za prekrivanje.',
        'filename_overlay_suffix': '_prekrito',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Izlušči slike iz PDF',
        'extract_images_menu': 'Izlušči vse slike',
        'extract_images_info': 'Izlušči vse slike iz PDF in jih shrani kot ločene datoteke.\n\nSlike se shranijo v izvirni obliki ali pretvorijo v izbrano obliko.',
        'extract_images_format': 'Oblika slike:',
        'extract_images_quality': 'Kakovost JPEG:',
        'extract_images_options': 'Možnosti:',
        'extract_images_subfolder': 'Izlušči v podmapo ("imePDF_slike")',
        'extract_images_unique': 'Samo edinstvene slike (izogibanje dvojnikom)',
        'extract_images_range': 'Obseg strani:',
        'extract_images_all_pages': 'Vse strani',
        'extract_images_custom_range': 'Obseg po meri',
        'extract_images_from': 'Od:',
        'extract_images_to': 'Do:',
        'extract_images_target_folder': 'Ciljna mapa:',
        'extract_images_browse': 'Prebrskaj...',
        'extract_images_select_folder': 'Izberite ciljno mapo',
        'extract_images_info_box': 'Informacije',
        'extract_images_info_text': 'Izluščanje lahko za velike PDF traja več minut.\n\nSlike se shranjujejo s svojim izvirnim imenom (stran_slika).',
        'extract_images_extract': 'Izlušči',
        'extract_images_start': 'Zagon izluščanja...',
        'extract_images_progress': 'Izluščanje slik...',
        'extract_images_success': '✅ Slike uspešno izluščene!\n\n{0} slik je bilo shranjenih v:\n{1}',
        'extract_images_complete': 'Izluščanje slik končano',
        'extract_images_cancel': 'Izluščanje preklicano',
        'extract_images_error_format': 'Napaka pri izluščanju slik:\n\n{0}',
        'extract_images_open_folder': '📁 Odpri mapo',
        'extract_images_no_images': 'V PDF ni bilo najdenih slik.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Več strani na eni strani (N-Up)',
        'nup_menu': 'Več strani na eni strani (N-Up)',
        'nup_info': 'Razporedi več PDF strani na eno stran.\n\nIdealno za kompaktne izpise, preglede ali razdelilno gradivo.',
        'nup_layout': 'Postavitev:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Predogled:',
        'nup_preview_info': '{0} strani → {1} strani na list → {2} listov\nPostavitev: {3}',
        'nup_order': 'Vrstni red:',
        'nup_order_horizontal': 'Vodoravno (vrstica za vrstico)',
        'nup_order_vertical': 'Navpično (stolpec za stolpcem)',
        'nup_order_horizontal_reverse': 'Vodoravno obratno',
        'nup_order_vertical_reverse': 'Navpično obratno',
        'nup_range': 'Obseg strani:',
        'nup_all_pages': 'Vse strani',
        'nup_custom_range': 'Obseg po meri',
        'nup_from': 'Od:',
        'nup_to': 'Do:',
        'nup_options': 'Možnosti:',
        'nup_margins': 'Robovi:',
        'nup_margin_between': 'Razmik med stranmi:',
        'nup_page_numbers': 'Vstavi številke strani',
        'nup_target_folder': 'Ciljna mapa:',
        'nup_browse': 'Prebrskaj...',
        'nup_select_folder': 'Izberite ciljno mapo',
        'nup_create': 'Ustvari',
        'nup_start': 'Zagon N-Up...',
        'nup_progress': 'Ustvarjanje N-Up...',
        'nup_success': 'N-Up uspešno ustvarjen!\n\nShranjeno kot:\n{0}\n\nAli želite odpreti nov PDF?',
        'nup_complete': 'N-Up končan',
        'nup_cancel': 'N-Up preklican',
        'nup_error_format': 'Napaka pri N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Spremeni velikost strani',
        'pagesize_menu': 'Spremeni velikost strani',
        'pagesize_info': 'Spremeni velikost strani PDF.\n\nVsebina se samodejno prilagodi novi velikosti.',
        'pagesize_format': 'Oblika:',
        'pagesize_select': 'Izberite standardno obliko:',
        'pagesize_custom': 'Velikost po meri:',
        'pagesize_width': 'Širina:',
        'pagesize_height': 'Višina:',
        'pagesize_orientation': 'Orientacija:',
        'pagesize_portrait': 'Pokončno',
        'pagesize_landscape': 'Ležeče',
        'pagesize_scale_options': 'Možnosti skaliranja:',
        'pagesize_fit': 'Prilagodi (ohrani razmerje)',
        'pagesize_stretch': 'Raztegni (popači)',
        'pagesize_center': 'Centriraj (izvirna velikost)',
        'pagesize_range': 'Obseg strani:',
        'pagesize_all_pages': 'Vse strani',
        'pagesize_custom_range': 'Obseg po meri',
        'pagesize_from': 'Od:',
        'pagesize_to': 'Do:',
        'pagesize_target_folder': 'Ciljna mapa:',
        'pagesize_browse': 'Prebrskaj...',
        'pagesize_select_folder': 'Izberite ciljno mapo',
        'pagesize_apply': 'Uporabi',
        'pagesize_start': 'Zagon spreminjanja velikosti strani...',
        'pagesize_progress': 'Spreminjanje velikosti strani...',
        'pagesize_success': 'Velikost strani uspešno spremenjena!\n\nShranjeno kot:\n{0}\n\nAli želite odpreti nov PDF?',
        'pagesize_complete': 'Spreminjanje velikosti strani končano',
        'pagesize_cancel': 'Spreminjanje velikosti strani preklicano',
        'pagesize_error_format': 'Napaka pri spreminjanju velikosti strani:\n\n{0}',
        'pagesize_preview_info': 'Nova velikost: {0} x {1} pt',
        'filename_pagesize_suffix': '_nova_velikost',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF informacije',
        'pdf_info_menu': 'Prikaži PDF informacije',
        'pdf_info_voice': 'Prikazovanje PDF informacij',
        'pdf_info_error': 'Napaka pri prikazovanju PDF informacij:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Pokaži bližnjice na tipkovnici",
        "shortcuts_dialog_title": "Bližnjice na tipkovnici",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 DATOTEKA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Odpri PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Zapri PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Shrani kot...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Zaščiti dokument</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Natisni</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Natisni takoj (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Zapri aplikacijo</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 IZVOZ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Izvozi kot Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Izvozi kot DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Izvozi kot TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Izvozi kot slike (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Izlušči slike</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ OBDELAVA DOKUMENTOV</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Več strani)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konverzija (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Splošči PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Prekrij PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimiziraj PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ UREJANJE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Išči</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Dodaj zaznamek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Upravljaj zaznamke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Naslednji zaznamek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Prejšnji zaznamek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Zaženi OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 UPRAVLJANJE STRANI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Zavrti trenutno stran</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Zavrti vse strani</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normaliziraj trenutno stran</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normaliziraj vse strani</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Izbriši strani</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Izlušči strani</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Vstavi strani</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Premakni strani</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Združi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Spremeni velikost strani</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 VSTAVLJANJE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Vstavi besedilo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Vstavi križ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Vstavi podpis 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Vstavi podpis 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Vstavi sliko</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Vstavi pravokotnik</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Vstavi elipso</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Vstavi črto</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Vstavi puščico</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Vstavi številke strani</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Besedilni vodni žig</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Slikovni vodni žig</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ IZBRISI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Izbris (črna)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Izbris (bela)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Uporabi vse izbrise</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ NAPREDNO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Obreži PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Uredi metapodatke</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ POGLED</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Preklopi Temni/Svetli način</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Pokaži okno besedila</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Širina strani (Povečava)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dve strani (Povečava)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Pregled (Povečava)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ NASTAVITVE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Upravljanje gesel</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR nastavitve</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Nastavitve podpisa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Oblikovanje imena datoteke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Izvozi nastavitve</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Uvozi nastavitve</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMACIJE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Prikaži PDF informacije</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Vklopi/izklopi glasovni izhod</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokusiraj menijsko vrstico</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Na voljo je nova različica",
        "update_available_message": "Na voljo je nova različica <b>{0}</b>.\n\nObiščite stran za izdajo za prenos posodobitve:\n{1}",
        "update_available_voice": "Nova različica {0} je na voljo. Prenesite posodobitev s strani GitHub.",
        "update_open_release": "Odpri stran za izdajo",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Prenesi vse prevode",
        "ask_download_all_translations": """Poleg nemščine, angleščine in vietnamščine je na voljo še {total_languages} drugih GUI jezikov.\n\nAli naj bodo zagotovljeni / posodobljeni?\n\nOpomba:\nNepotrebne jezike lahko kasneje ročno izbrišete v imeniku:\n{translations_path}
        \nČe prekličete, lahko GUI jezike kasneje prenesete prek menija 'Orodja → Posodobi prevode'.""",
        "menu_update_translations": "Posodobi prevode",
        "translations_updated": "Prevodi posodobljeni",
        "translations_update_success": "{} prevodov je bilo uspešno posodobljenih ({} novih, {} posodobljenih).",
        "translations_update_error": "Napaka pri posodabljanju prevodov",
        "translations_update_no_changes": "Vsi prevodi so že posodobljeni.",
        "translations_update_offline": "Ni internetne povezave. Prevodi niso mogli biti posodobljeni.",
        "translations_update_in_progress": "Prevodi se posodabljajo v ozadju...",
        "translations_downloading": "Prenašanje prevodov...",
        "translations_path_hint": "Uporabniški imenik za prevode",
        "translations_update_not_available_title": "Posodobitev ni na voljo",
        "translations_update_not_available_message": """Posodabljanje prevodov je na voljo samo v nameščeni različici.\n\nV razvojnem načinu so prevodi že posodobljeni.""",
        "translations_update_no_internet_title": "Ni internetne povezave",
        "translations_update_no_internet_message": """Ni bilo mogoče vzpostaviti internetne povezave.\n\nPrevodov ni mogoče prenesti z GitHub-a.\n\nMožne rešitve:
        • Preverite svojo internetno povezavo
        • Začasno onemogočite morebitni požarni zid
        • Poskusite znova pozneje
        \nPrevode lahko prenesete tudi ročno z GitHub-a:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Posodobitev že poteka",
        "btn_retry": "Poskusi znova",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Dobrodošli v PDF Dark View",
        "welcome_title_not_supported": "Dobrodošli v PDF Dark View",
        "welcome_message": "Dobrodošli v PDF Dark View!\n\nVaš sistemski jezik je bil prepoznan kot '{language}'.\nAli želite uporabiti ta jezik za uporabniški vmesnik?\n\nJezik lahko kadar koli spremenite prek 'Nastavitve → Jezik'.",
        "welcome_message_language_not_available": "Dobrodošli v PDF Dark View!\n\nVaš sistemski jezik je bil prepoznan kot '{language}'.\nTa jezik še ni nameščen.\n\nAli želite zdaj prenesti prevode za {language} z GitHub-a?\n\n(Jezik bo nato samodejno uporabljen za uporabniški vmesnik.)",
        "welcome_message_language_not_supported": "Dobrodošli v PDF Dark View!\n\nVaš sistemski jezik je bil prepoznan kot '{language}'.\nNa žalost za ta jezik še ni prevodov.\n\nUporabniški vmesnik bo prikazan v {fallback_language}.\n\nJezik lahko kadar koli spremenite prek 'Nastavitve → Jezik'.\nČe želite, lahko tudi sami prispevate prevod za svoj jezik:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Da, uporabi sistemski jezik",
        "welcome_keep_english": "Ne, obdrži angleščino",
        "welcome_download_language": "Da, prenesi {language}",

        # ============================================
        # 107. ZADNJE UPORABLJENE POTI
        # ============================================

        'menu_recent': 'Zadnje uporabljeno',
        'menu_recent_dirs': 'Mape...',
        'menu_recent_files': 'Datoteke...',
        'recent_manage': 'Upravljanje...',
        'recent_enable_tracking': 'Shrani zadnje poti (zasebnost)',
        'recent_enable_info': 'Onemogočite to možnost, da ne shranjujete poti',
        'recent_tracking_disabled': 'Sledenje poti je onemogočeno',
        'recent_enabled': 'omogočeno',
        'recent_disabled': 'onemogočeno',
        'recent_tracking_status': 'Sledenje poti {0}',
        'recent_dialog_title': 'Zadnje uporabljene poti',
        'recent_tab_directories': 'Mape',
        'recent_tab_files': 'Datoteke',
        'recent_dirs_instruction': 'Dvokliknite za odpiranje pogovornega okna datoteke v mapi',
        'recent_files_instruction': 'Dvokliknite za neposredno odpiranje PDF',
        'recent_no_directories': '(ni shranjenih map)',
        'recent_no_files': '(ni shranjenih datotek)',
        'recent_default_current': '⭐ Privzeto: {0}',
        'recent_set_as_default': '⭐ Nastavi kot privzeto',
        'recent_default_set_title': 'Privzeta mapa je nastavljena',
        'recent_default_set_message': 'Mapa "{0}" je nastavljena kot privzeta za odpiranje PDF-jev.',
        'recent_default_set_voice': 'Privzeta mapa je nastavljena',
        'recent_directory_not_found': 'Mapa ni najdena',
        'recent_file_not_found': 'Datoteka ni najdena',
        'recent_remove_selected': 'Odstrani',
        'recent_remove_title': 'Odstrani pot',
        'recent_remove_confirm': 'Ali res želite odstraniti pot "{0}" s seznama?',
        'recent_path_removed': 'Pot je odstranjena',
        'recent_clear_all': 'Odstrani vse',
        'recent_clear_title': 'Odstrani vse poti',
        'recent_clear_confirm_type': 'Ali res želite izbrisati vse {0}?',
        'recent_cleared': 'Seznam je počisčen',
        'recent_path_not_found_title': 'Pot ni najdena',
        'recent_path_not_found_message': 'Pot "{0}" ne obstaja več.',
        'recent_open_file': 'Odpri datoteko',
        'btn_open_recent': 'Odpri',
        'recent_open_file_question': 'Ali želite odpreti "{0}" kot PDF?',
        'recent_not_pdf': 'Izbrana datoteka ni PDF.',
        'recent_more_entries': 'Več vnosov...',
        'btn_remove': 'Odstrani',
        'btn_clear': 'Počisti vse',
        'recent_context_open': 'Odpri',
        'recent_context_reveal': 'Pokaži v Finderju',
        'recent_context_set_default': '⭐ Nastavi kot privzeto',
        'recent_context_open_terminal': '💻 Odpri terminal',
        'recent_context_file_info': 'Informacije o datoteki',
        'recent_context_open_with_default': '📄 Odpri s privzeto aplikacijo',
        'recent_context_remove': 'Odstrani s seznama',
        'recent_context_clear_all': 'Odstrani vse',
        'recent_file_info_title': 'Informacije o datoteki',
        'recent_file_info_name': 'Ime',
        'recent_file_info_path': 'Pot',
        'recent_file_info_size': 'Velikost',
        'recent_file_info_modified': 'Spremenjeno',
        'recent_file_info_pages': 'Strani',
        'recent_error_reveal': 'Napaka pri odpiranju v Finderju',
        'recent_error_terminal': 'Napaka pri odpiranju terminala',
        'recent_error_info': 'Napaka pri pridobivanju informacij o datoteki',
        'open_user_data_folder': 'Pokaži mapo uporabniških podatkov',

        # ============================================
        # 108. BRISANJE SODIH/LIHIH STRANI
        # ============================================
        "pages_delete_even": "Izbriši vse sode strani",
        "pages_delete_odd":  "Izbriši vse lihe strani",
        "progress_even_pages": "Brisanje sodih strani",
        "progress_odd_pages": "Brisanje lihih strani",
        "progress_mark_delete_even": "{} soda(e) stran(i) označena(e) za brisanje",
        "progress_mark_delete_odd":  "{} liha(e) stran(i) označena(e) za brisanje",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program se zapira",

    }
