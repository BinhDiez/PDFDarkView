
# ============================================
# translations_nl.py - Nederlands woordenboek
# Volledig gesorteerd op categorie
# Opmerkingen in het Duits voor consistentie
# ============================================

def load_dutch_strings():
    """Laadt alle Nederlandse strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View door BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF openen",
        'btn_text_window': "OCR tekst",
        'btn_first': "Eerste pagina",
        'btn_prev': "Vorige pagina",
        'btn_next': "Volgende pagina",
        'btn_last': "Laatste pagina",
        'btn_print': "Afdrukken",
        'btn_darkmode_light': "Lichte modus",
        'btn_darkmode_dark': "Donkere modus",
        'btn_delete_pages': "Pagina's verwijderen",
        'btn_extract_pages': "Pagina's uithalen",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Annuleren",
        'btn_save': "Opslaan",
        'btn_close': "Sluiten",
        'btn_delete': "Verwijderen",
        'btn_delete_all': "Alles verwijderen",
        'btn_copy': "Kopiëren",
        'btn_export': "Exporteren",
        'btn_show': "Toon wachtwoord",
        'btn_hide': "Verberg wachtwoord",
        'btn_authenticate': "Authenticeren",
        'btn_settings': "Instellingen",
        'btn_protect': "Beveiligen",
        'btn_remove_password': "Wachtwoord verwijderen",
        'btn_manage': "Wachtwoordbeheer",
        'btn_retry': "Opnieuw proberen",
        'btn_select_all': "Alles selecteren",
        'btn_clear_selection': "Selectie opheffen",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Pagina {0} van {1}",
        'page_count': "van {0}",
        'goto_page': "Ga naar pagina",
        'page_simple': "Pagina {0}",
        'full_view_page': "Volledig beeld pagina {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Zoekterm invoeren + Enter",
        'search_results': "Resultaten: {0} van {1}",
        'search_nav_hint': "Enter: volgende  (Shift+Enter: vorige) resultaat",
        'search_no_results': "Geen resultaten",
        'search_error': "Zoekfout",
        'search_active': "Zoekveld geactiveerd",
        'search_closed': "Zoeken beëindigd",
        'search_position': "Pagina {0} {1}",
        'search_pos_top': "helemaal bovenaan",
        'search_pos_upper': "bovenaan",
        'search_pos_middle': "midden",
        'search_pos_lower': "onderaan",
        'search_pos_bottom': "helemaal onderaan",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Tekstherkenning succesvol afgerond!",
        'ocr_success_title': "OCR gelukt",
        'ocr_success_message': "Het document is nu doorzoekbaar.",
        'ocr_failed': "OCR mislukt",
        'ocr_in_progress': "OCR bezig",
        'ocr_preparing': "PDF wordt voorbereid...",
        'ocr_analyzing': "PDF wordt geanalyseerd...",
        'ocr_optimizing': "Afbeeldingsoptimalisatie bezig...",
        'ocr_recognizing': "Tekstherkenning bezig...",
        'ocr_embedding': "Tekst wordt ingebed...",
        'ocr_finalizing': "PDF wordt afgerond...",
        'ocr_not_available': "OCR niet beschikbaar",
        'ocr_install_message': "OCR‑tools niet gevonden.\n\nInstalleer:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR vereist",
        'ocr_question': "De PDF bevat geen doorzoekbare tekst.\nOCR uitvoeren om {0} mogelijk te maken?",
        'ocr_perform': "OCR uitvoeren",
        'ocr_later': "Later",
        'ocr_starting': "Start gegarandeerde OCR...",
        'ocr_success_voice': "OCR gelukt. PDF is nu doorzoekbaar.",
        'ocr_partial_success': "OCR is uitgevoerd, maar er waren problemen bij het vervangen.\n\nDe doorzoekbare versie is opgeslagen onder:\n{0}\n\nFout: {1}",
        'ocr_partial_title': "OCR gedeeltelijk gelukt",
        'ocr_partial_voice': "OCR uitgevoerd, maar vervangen mislukt.",
        'original_file': "Origineel bestand:",
        'old_size': "Oude bestandsgrootte:    {0} bytes",
        'new_size': "Nieuwe bestandsgrootte: {0} bytes",
        'size_change': "Wijziging: {0}{1} bytes",
        'backup_created_file': "Backup gemaakt:\n{0}",
        'backup_not_created': "Backup: niet gemaakt (instelling uitgeschakeld)",
        'page_header': "=== Pagina {0} ===\n{1}\n",
        'scanned_page_header': "=== Pagina {0} (gescand) ===\n[Deze pagina bevat alleen gescande tekst]\n[Voer OCR handmatig uit]\n",
        'scanned_warning': "⚠️ GESCANDE TEKST - OCR VEREIST",
        'guaranteed_title': "Doorzoekbare PDF gemaakt",
        'guaranteed_message': "<b>Gegarandeerde doorzoekbare versie gemaakt!</b>\n\nOmdat de automatische OCR is mislukt, is een alternatieve doorzoekbare PDF gemaakt:\n\n{0}\n\n<b>Dit bestand bevat:</b>\n• Geëxtraheerde tekst (indien aanwezig)\n• Aanwijzingen voor gescande pagina's\n• Is volledig doorzoekbaar",
        'guaranteed_voice': "Gegarandeerde doorzoekbare PDF gemaakt.",
        'instruction_title': "INSTRUCTIE VOOR OCR",
        'instruction_file': "Origineel bestand: {0}",
        'instruction_text': "Automatische tekstherkenning (OCR) is mislukt.\nVoer OCR handmatig uit:\n\n1. MET OCRmyPDF (commandoregel):\n   ocrmypdf --force-ocr \"[BESTAND]\" \"uitvoer.pdf\"\n\n2. MET ADOBE ACROBAT (macOS/Windows):\n   • PDF openen in Acrobat\n   • Gereedschap > PDF bewerken\n   • 'Tekst herkennen' selecteren\n\n3. MET VOORVERTONING (macOS):\n   • PDF openen in Voorvertoning\n   • Archief > Exporteer...\n   • Quartz‑filter: 'Verklein bestandsgrootte'\n   • 'OCR uitvoeren' inschakelen\n\n4. ONLINE OCR‑DIENSTEN:\n   • smallpdf.com/nl/ocr-pdf\n   • ilovepdf.com/nl/ocr-pdf\n   • adobe.com/nl/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR‑instructie gemaakt",
        'instruction_created_message': "Een gedetailleerde instructie is gemaakt:\n\n{0}\n\nVolg de stappen voor handmatige OCR.",
        'instruction_created_voice': "OCR‑instructie gemaakt.",
        'ocr_impossible': "OCR niet mogelijk",
        'ocr_impossible_message': "OCR kon niet worden uitgevoerd.\n\nVerwerk '{0}' handmatig met OCR‑software.",
        'ocr_impossible_voice': "OCR niet mogelijk. Verwerk handmatig.",
        'emergency_title': "Nood‑OCR",
        'emergency_message': "Een nood‑PDF is gemaakt:\n\n{0}\n\nVerwerk dit bestand handmatig met OCR.",
        'emergency_voice': "Nood‑PDF gemaakt. Voer handmatig OCR uit.",
        'critical_error': "Kritieke fout",
        'critical_error_message': "OCR kon niet worden gestart.\n\nHerstart het programma en\ncontroleer de OCR‑installatie.",
        'critical_error_voice': "Kritieke OCR‑fout",
        'ocr_question_html': "<p>De PDF bevat geen doorzoekbare tekst.<p>OCR uitvoeren om <b>{0}</b> mogelijk te maken?</p>",
        'ocr_question_voice': "OCR vereist. De PDF bevat geen doorzoekbare tekst. OCR uitvoeren om {0} mogelijk te maken?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "geen PDF geladen",
        'no_pdf_message': "Er is geen PDF geladen",
        'pdf_not_found': "PDF‑bestand niet gevonden",
        'file_size': "Bestandsgrootte",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup gemaakt",
        'backup_disabled': "Backup uitgeschakeld",
        'backup_activated': "Backup aanmaken ingeschakeld",
        'backup_deactivated': "Backup aanmaken uitgeschakeld",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ ingeschakeld",
        'backup_off': "✘ uitgeschakeld",
        'close_pdf': "PDF sluiten: {0}",
        'pdf_not_found_format': "PDF‑bestand niet gevonden: {0}",
        'error_pdf_load_format': "Fout bij laden van PDF: {0}",
        'load_failed_format': "Laden mislukt:\n{0}",
        'decrypted_suffix': "(ontsleuteld)",
        'decryption_failed': "Ontsleutelen mislukt.",
        'decryption_error': "Fout bij ontsleutelen",
        'decryption_success': "Ontsleutelen gelukt",
        'decryption_success_message': "PDF is ontsleuteld en opgeslagen onder:\n\n{0}",
        'decryption_success_voice': "PDF is ontsleuteld en opgeslagen.",
        'password_remove_error': "Fout bij verwijderen wachtwoord",
        'save_unencrypted': "Onversleutelde PDF opslaan als",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Opslaan als...",
        'save_copy': "Kopie opslaan",
        'save_success': "PDF opgeslagen onder: {0}",
        'save_encrypted': "Beveiligde PDF opgeslagen onder: {0}",
        'save_error': "PDF kon niet worden opgeslagen",
        'encryption_question': "De PDF met een wachtwoord beveiligen?",
        'encryption_yes': "Ja",
        'encryption_no': "Nee",
        'encryption_cancel': "Annuleren",
        'save_cancel': "Opslaan geannuleerd",
        'save_encrypted_voice': "Bestand versleuteld en opgeslagen.",
        'save_success_voice': "Het PDF‑bestand is onversleuteld opgeslagen.",
        'save_error_format': "PDF kon niet worden opgeslagen:\n{0}",
        'export_pages_success': "Pages‑export gelukt",
        'export_pages_error': "Pages‑export mislukt",
        'export_pages_error_format': "Pages‑export mislukt: {0}",
        'export_word_success': "Word‑export gelukt",
        'export_word_error': "Word‑export mislukt",
        'export_word_error_format': "Word‑export mislukt: {0}",
        'export_text_success': "Tekstexport gelukt",
        'export_text_error': "Tekstexport mislukt",
        'export_text_error_format': "Tekstexport mislukt: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Wachtwoord vereist",
        'password_enter': "Voer het wachtwoord in",
        'password_confirm': "Bevestig wachtwoord",
        'password_new': "Nieuw wachtwoord",
        'password_current': "Huidig wachtwoord",
        'password_save': "Wachtwoord opslaan (versleuteld)",
        'password_saved': "✓ Wachtwoord voor dit bestand is opgeslagen",
        'password_wrong': "Onjuist wachtwoord",
        'password_mismatch': "Wachtwoorden komen niet overeen",
        'password_too_short': "Wachtwoord te kort",
        'password_min_length': "Het wachtwoord moet ten minste 4 tekens lang zijn",
        'password_strength': "Wachtwoordsterkte",
        'password_strength_very_weak': "Zeer zwak",
        'password_strength_weak': "Zwak",
        'password_strength_medium': "Gemiddeld",
        'password_strength_strong': "Sterk",
        'password_strength_very_strong': "Zeer sterk",
        'password_char_count': "({0} tekens)",
        'password_match': "✓ Komen overeen",
        'password_no_match': "✗ Wachtwoorden komen niet overeen",
        'password_show': "Tonen",
        'password_hide': "Verbergen",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Wachtwoordbeheer",
        'password_table_filename': "Bestandsnaam",
        'password_table_password': "Wachtwoord",
        'password_count': "{0} opgeslagen wachtwoord{1}",
        'password_count_singular': "",
        'password_count_plural': "en",
        'password_none': "Geen opgeslagen wachtwoorden",
        'password_copied': "{0} wachtwoord{1} gekopieerd",
        'password_copied_singular': "",
        'password_copied_plural': "en",
        'password_delete_confirm': "Wilt u het wachtwoord voor '{0}' echt verwijderen?",
        'password_delete_multiple': "Wilt u de {0} geselecteerde wachtwoorden echt verwijderen?",
        'password_delete_all_confirm': "Wilt u alle {0} opgeslagen wachtwoorden echt verwijderen?",
        'password_deleted': "{0} wachtwoord{1} verwijderd",
        'password_deleted_singular': "",
        'password_deleted_plural': "en",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Alle wachtwoorden zijn verwijderd",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Wachtwoordgenerator",
        'generator_generated': "Gegenereerd wachtwoord:",
        'generator_regenerate': "Opnieuw genereren",
        'generator_copy': "Kopiëren",
        'generator_use': "Gebruiken",
        'generator_settings': "Instellingen",
        'generator_length': "Lengte:",
        'generator_group_every': "Scheidingsteken elke",
        'generator_group_chars': "tekens.   Scheidingsteken:",
        'generator_uppercase': "Hoofdletters (A-Z)",
        'generator_lowercase': "Kleine letters (a-z)",
        'generator_digits': "Cijfers (0-9)",
        'generator_symbols': "Symbolen (!@#$%^&*)",
        'generator_exclude': "Uitgesloten:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Master‑wachtwoord vereist",
        'master_password_setup': "Master‑wachtwoord instellen",
        'master_password_change': "Master‑wachtwoord wijzigen",
        'master_password_enter': "Voer uw master‑wachtwoord in",
        'master_password_choose': "Kies een sterk master‑wachtwoord (minimaal 8 tekens)",
        'master_password_new': "Voer uw nieuwe master‑wachtwoord in",
        'master_password_confirm': "Bevestig wachtwoord",
        'master_password_authenticate': "Authenticeren",
        'master_password_success': "Master‑wachtwoord succesvol ingesteld.",
        'master_password_changed': "Master‑wachtwoord succesvol gewijzigd.",
        'master_password_removed': "Master‑wachtwoord en alle wachtwoorden verwijderd.",
        'master_password_remove': "Master‑wachtwoord verwijderen",
        'master_password_remove_confirm': "Weet u ZEKER dat u ALLE wachtwoorden wilt verwijderen?\n\nDeze actie is ONOMKEERBAAR!",
        'master_password_export_before': "Wilt u eerst een backupexport maken?",
        'master_password_export_delete': "Exporteren & verwijderen",
        'master_password_delete_now': "Nu verwijderen",
        'master_password_for_signatures': "Om handtekeningen te kunnen gebruiken, moet u een master‑wachtwoord instellen.\n\nWilt u nu een master‑wachtwoord instellen?",
        'master_password_for_private': "Om privétekstblokken te kunnen gebruiken, moet u een master‑wachtwoord instellen.\n\nWilt u nu een master‑wachtwoord instellen?",
        'master_password_info': """
            <b>🔐 ZONDER MASTER‑WACHTWOORD:</b><br>
            • Geen weergave, kopiëren of exporteren van wachtwoorden mogelijk<br>
            • Wachtwoorden verwijderen is altijd mogelijk (ook zonder master‑wachtwoord)<br><br>

            <b>🔐 MET MASTER‑WACHTWOORD:</b><br>
            • Alle functies beschikbaar na authenticatie<br>
            • Wachtwoorden worden versleuteld met het master‑wachtwoord<br>
            • Minimale lengte: 8 tekens<br>
            • Veilige SHA‑256 hash‑opslag<br><br>

            <b>BELANGRIJK:</b><br>
            • Bij verlies van master‑wachtwoord: wachtwoorden niet te herstellen<br>
            • Bij verwijderen van master‑wachtwoord: ALLE wachtwoorden worden gewist<br>
            • Exportoptie beschikbaar vóór verwijdering<br>
            • Master‑wachtwoord kan altijd worden gewijzigd
        """,
        'signature_auth_disabled': "Wachtwoordvraag voor handtekeningen uitschakelen",
        'template_auth_disabled': "Wachtwoordvraag voor privétekstblokken uitschakelen",
        'master_password_for_signatures_settings': "Om handtekeningen te kunnen gebruiken, moet u een master‑wachtwoord instellen.\n\nGa daarvoor naar Instellingen – Wachtwoordbeheer",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF beveiligen",
        'protect_info': "Het bestand '{0}' wordt met een wachtwoord beveiligd.",
        'protect_instruction': "Voer het gewenste wachtwoord twee keer in om het document te beveiligen, of gebruik de wachtwoordgenerator rechts van het invoerveld.",
        'protect_success': "PDF is succesvol beveiligd en opgeslagen onder:\n{0}\n\nWachtwoord: {1}\n\nWilt u de beveiligde PDF nu openen?",
        'protect_open': "Ja",
        'protect_skip': "Nee",
        'protect_error': "Fout bij beveiligen van PDF",
        'protect_open_title': "beveiligde PDF openen",
        'protect_question': "Gereed. Wilt u de beveiligde PDF nu openen? Ja of Nee?",
        'password_cancel': "Wachtwoorddialoog geannuleerd",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Pagina's verwijderen",
        'pages_extract': "Pagina's uithalen",
        'pages_insert': "Pagina's invoegen",
        'pages_move': "Pagina's verplaatsen",
        'pages_delete_options': "Verwijderopties",
        'pages_delete_empty': "Alle lege pagina's verwijderen",
        'pages_delete_current': "Huidige pagina verwijderen",
        'pages_delete_range': "Paginabereik verwijderen",
        'pages_extract_options': "Uithaalopties",
        'pages_extract_current': "Huidige pagina uithalen",
        'pages_extract_range': "Paginabereik uithalen",
        'pages_insert_position': "Invoegpositie",
        'pages_insert_before': "Invoegen vóór pagina:",
        'pages_insert_select': "PDF selecteren",
        'pages_insert_none': "Geen PDF geselecteerd",
        'pages_move_source': "Te verplaatsen pagina's",
        'pages_move_from': "Van pagina:",
        'pages_move_to': "Tot pagina:",
        'pages_move_target': "Doelpositie",
        'pages_move_before': "Verplaatsen vóór pagina:",
        'pages_move_hint': "Opmerking: pagina 1 = begin, {0} = einde",
        'pages_range_invalid': "De startpagina moet kleiner of gelijk zijn aan de eindpagina.",
        'pages_position_invalid': "De doelpositie mag niet binnen het te verplaatsen bereik liggen.",
        'pages_no_pdf_selected': "Er is geen PDF geselecteerd.",
        'pages_deleted': "Er zijn {0} pagina's verwijderd.",
        'pages_extracted': "Uitgehaald: {0}\nOpgeslagen onder: {1}\nBestandsgrootte: {2:.1f} KB",
        'pages_inserted': "{0} pagina's ingevoegd",
        'pages_moved': "Er zijn {0} pagina's verplaatst.",
        'pages_deleted_none': "Er zijn geen pagina's verwijderd.",
        'pages_delete_progress': "Pagina's verwijderen...",
        'pages_deleted_with_backup': "Er zijn {0} pagina's verwijderd.\n\nBackup: {1}",
        'pages_deleted_voice': "Er is een backup gemaakt en {0} pagina's verwijderd.",
        'info': "Informatie",
        'error_dialog_creation': "Dialoog kon niet worden gemaakt",
        'extract_page_single': "Pagina {0} uithalen",
        'extract_page_range': "Pagina's {0}-{1} uithalen",
        'extract_success_voice': "Pagina's succesvol uitgehaald",
        'extract_error_format': "Fout bij uithalen: {0}",
        'pages_inserted_voice': "{0} pagina's ingevoegd.",
        'insert_error_format': "Fout bij invoegen: {0}",
        'pages_move_progress': "Pagina's verplaatsen...",
        'pages_moved_with_backup': "Er zijn {0} pagina's verplaatst.\n\nBackup: {1}",
        'move_success_title': "Succesvol verplaatst",
        'pages_moved_voice': "{0} pagina's succesvol verplaatst",
        'mark_removed': "Markering van pagina {0} verwijderd",
        'mark_empty': "Pagina {0} als leeg gemarkeerd",
        'mark_export_removed': "Exportmarkering van pagina {0} verwijderd",
        'mark_export': "Pagina {0} gemarkeerd voor export",
        'no_empty_pages': "Geen lege pagina's gemarkeerd om te verwijderen",
        'delete_empty_confirm': "Wilt u alle {0} gemarkeerde lege pagina's verwijderen?",
        'delete_empty_confirm_voice': "Nu alle {0} gemarkeerde lege pagina's verwijderen? Ja of Nee.",
        'empty_pages_deleted': "{0} lege pagina's verwijderd",
        'no_export_pages': "Geen pagina's gemarkeerd voor export",
        'overwrite_title': "Bestaand bestand overschrijven",
        'overwrite_question': "Het bestand\n\n{0}\n\nbestaat al.\nWilt u het overschrijven?",
        'overwrite_voice': "Bestaand bestand overschrijven? Ja of Nee.",
        'page_skipped': "Pagina {0} is overgeslagen",
        'export_complete': "Export voltooid.",
        'export_complete_voice': "De export is voltooid.",
        'no_pages_exported': "Geen pagina geëxporteerd",
        'export_cancelled': "Export geannuleerd",
        'pages_exported': "{0} pagina's geëxporteerd naar {1}",
        'export_page_title': "Pagina exporteren",
        'page_exported': "Pagina {0} geëxporteerd naar {1}",
        'export_error': "Fout bij exporteren",
        'export_marked_title': "Gemarkeerde pagina's exporteren",
        'rotate_all_title': "alle pagina's draaien",
        'rotate_all_question': "Wilt u alle pagina's 90 graden naar rechts draaien?",
        'rotate_all_voice': "Wilt u alle pagina's 90 graden naar rechts draaien? Ja of Nee?",
        'all_pages_rotated': "Alle pagina's gedraaid",
        'page_rotated': "Pagina {0} gedraaid",
        'rotate_error': "Pagina kon niet worden gedraaid",
        'delete_page_confirm': "Wilt u pagina {0} verwijderen?",
        'delete_page_confirm_voice': "Wilt u pagina {0} echt verwijderen? Ja of Nee.",
        'page_deleted': "Pagina {0} verwijderd",
        'delete_error': "Pagina kon niet worden verwijderd",
        'pages_deleted_voice': "{0} pagina's verwijderd",
        'pages_exported_split': "{0} pagina's zijn succesvol geëxporteerd.",
        'pages_skipped': "{0} pagina's zijn overgeslagen.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Pagina's uithalen (geavanceerd)",
        'pdf_splitter_title': "PDF Splitter & Extractor",
        'pdf_splitter_load': " PDF‑bestand selecteren",
        'pdf_splitter_info': "Kies een optie voor uw PDF‑document",
        'pdf_splitter_basic': "Basisbewerkingen",
        'pdf_splitter_single': "In afzonderlijke pagina's splitsen",
        'pdf_splitter_range': "Pagina's extraheren:",
        'pdf_splitter_range_placeholder': "bv. 1-3,5,7-9",
        'pdf_splitter_clean': "Opschoonbewerkingen",
        'pdf_splitter_remove_empty': "Alle lege pagina's verwijderen",
        'pdf_splitter_remove': "Paginabereik verwijderen:",
        'pdf_splitter_remove_placeholder': "bv. 2,4-6",
        'pdf_splitter_process': "PDF verwerken",
        'pdf_splitter_loaded': "PDF geladen. Kies een optie",
        'pdf_read_error': "PDF kon niet worden gelezen",
        'pages': "Pagina's",
        'pages_created': "Pagina's zijn aangemaakt",
        'range_empty': "Voer een paginabereik in",
        'range_invalid': "Ongeldig paginabereik",
        'range_created': "Nieuwe PDF met de geselecteerde pagina's is aangemaakt:\n{0}",
        'empty_removed': "{0} lege pagina's verwijderd.\nUitvoer: {1}",
        'remove_empty': "Voer te verwijderen pagina's in",
        'remove_invalid': "Ongeldige pagina's om te verwijderen",
        'remove_done': "Opgeschoonde PDF aangemaakt:\n{0}",
        'open_folder': "Map openen",
        'show_in_finder': "Toon in Finder",
        'pdf_splitter_no_pdf': "Laad eerst een PDF‑bestand.",
        'process_error': "Fout bij verwerken van PDF",
        'pages_created_voice': "{0} pagina's zijn aangemaakt",
        'range_created_voice': "PDF met de geselecteerde pagina's is aangemaakt",
        'empty_removed_voice': "{0} lege pagina's zijn verwijderd",
        'remove_done_voice': "Opgeschoonde PDF is aangemaakt",
        'pdf_splitter_split_groups': "Elke aaneengesloten groep in apart bestand",
        'range_created_single': "Nieuwe PDF aangemaakt:\n{0}",
        'range_created_multiple': "{0} PDF‑bestanden zijn aangemaakt.",
        'range_created_voice_single': "Eén PDF met de geselecteerde pagina's is aangemaakt",
        'range_created_voice_multiple': "{0} PDF‑bestanden zijn aangemaakt",
        'empty_removed_none_left': "Geen pagina's over",
        'empty_removed_all_empty': "Alle pagina's zijn als leeg herkend en zouden worden verwijderd. Er is geen bestand aangemaakt.",
        'preview_single': "Voorvertoning: {0}",
        'preview_enter_range': "Voer een paginabereik in.",
        'preview_invalid_range': "Ongeldig paginabereik.",
        'preview_file': "Voorvertoning: {0}",
        'preview_files': "Voorvertoning: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Afdrukken starten",
        'print_sent': "Afdruktaak verzonden",
        'print_now': "Nu afdrukken",
        'print_error': "Fout bij direct afdrukken",
        'print_limited': "Afdrukfunctie beperkt op dit systeem",
        'print_error_format': "Fout bij direct afdrukken: {0}",
        'warning': "Opmerking",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Overschakelen naar lichte modus",
        'mode_switch_to_dark': "Overschakelen naar donkere modus",
        'mode_dark_activated': "Donkere modus geactiveerd",
        'mode_light_activated': "Lichte modus geactiveerd",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Volledig beeld",
        'zoom_two_pages': "Twee pagina's naast elkaar",
        'zoom_overview': "Overzichtsmodus",
        'zoom_cannot_during_search': "Zoomen tijdens zoeken niet mogelijk",
        'zoom_exit_first': "Verlaat eerst de zoommodus",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & drop ingeschakeld",
        'drag_disabled': "Drag & drop uitgeschakeld",
        'drag_page_grab': "Pagina {0} vastpakken",
        'drag_page_dropped': "Pagina {0} ingevoegd op positie {1}",
        'drag_position_invalid': "Ongeldige positie",
        'drag_same_position': "Pagina {0} blijft op positie {0}",
        'drag_error': "Fout bij verplaatsen",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Tekstinvoer met geavanceerde opmaak en tekstblokbeheer",
        'text_templates': "Beschikbare tekstblokken:",
        'text_name': "Naam",
        'text_preview': "Tekstvoorbeeld",
        'text_enter': "Tekst:",
        'text_font_size': "Lettergrootte:",
        'text_formatting': "Opmaak:",
        'text_bold': "Vet",
        'text_italic': "Cursief",
        'text_underline': "Onderstreept",
        'text_alignment': "Uitlijning:",
        'text_left': "Links",
        'text_center': "Gecentreerd",
        'text_right': "Rechts",
        'text_color': "Tekstkleur:",
        'text_opacity': "Dekking:",
        'text_word_wrap': "Woordterugloop:",
        'text_auto': "Automatisch",
        'text_page_width_95': "Pagina‑breedte (95%)",
        'text_page_width_85': "Zeer breed (85%)",
        'text_page_width_75': "Breder (75%)",
        'text_page_width_60': "Breed (60%)",
        'text_page_width_50': "Gemiddeld (50%)",
        'text_page_width_30': "Smal (30%)",
        'text_page_width_20': "Smaller (20%)",
        'text_page_width_10': "Zeer smal (10%)",
        'text_no_wrap': "Geen terugloop",
        'text_private': "Privétekstblok (vereist authenticatie)",
        'text_preview_label': "Voorbeeld:",
        'text_preview_placeholder': "Hier wordt een voorbeeld van de tekst getoond...",
        'text_no_text': "(Geen tekst)",
        'text_save_template': "💾 Als blok opslaan",
        'text_delete_template': "🗑 Geselecteerd tekstblok verwijderen",
        'text_show_private': "Privé tonen",
        'text_hide_private': "Privé verbergen",
        'text_use': "✅ Tekst gebruiken",
        'text_saved': "Tekstblok opgeslagen als:\n{0}",
        'text_saved_voice': "Tekstblok opgeslagen",
        'text_deleted': "Tekstblok verwijderd",
        'text_no_text_to_save': "Geen tekst om op te slaan.",
        'text_no_templates': "Geen tekstblokken gevonden",
        'text_private_master_required': "Privéblokken kunnen alleen worden gebruikt als een master‑wachtwoord is ingesteld.\n\nWilt u nu een master‑wachtwoord instellen?",
        'text_filename': "Bestandsnaam voor tekstblok (zonder 'Text_' en '.txt'):",
        'text_filename_hint': "Voorbeeld: 'Telefoon Thuis' wordt opgeslagen als 'Text_Telefoon Thuis.txt'",
        'text_save_hint': "Het tekstblok wordt automatisch met opmaak opgeslagen.",
        'text_guide_title': "Tekstinvoer - Handleiding",
        'text_delete_confirm': "Wilt u het tekstblok echt verwijderen?\n\nBestand: {0}\nTekst: {1}...",
        'text_make_public': "Als openbaar markeren",
        'text_make_private': "Als privé markeren",
        'text_privacy_changed': "Privacystatus gewijzigd",
        'text_private_always': "Privé altijd zichtbaar (instelling)",
        'text_mode_required': "Activeer eerst de tekstmodus",
        'text_continue_editing': "Verder bewerken – cursor aan het einde van de tekst",
        'text_no_input': "Geen tekst ingevoerd – tekst genegeerd",
        'save_dialog_question': "Hoe wilt u verdergaan?",
        'text_save_question': "Alle teksten en kruisen opslaan, aanpassen, verder bewerken of negeren?",
        'copy_cross': "Kruis gekopieerd",
        'paste_cross': "Kruis geplakt",
        'paste_text': "Tekst geplakt",
        'cross_discarded': "Kruis genegeerd",
        'all_discarded': "Alles genegeerd",
        'text_discarded': "Tekst genegeerd",
        'no_texts_to_save': "Geen teksten om op te slaan",
        'no_valid_texts': "Geen geldige teksten om op te slaan",
        'text_word_singular': "tekst",
        'text_word_plural': "teksten",
        'cross_word_singular': "kruis",
        'cross_word_plural': "kruisen",
        'texts_saved_title': "Teksten opgeslagen",
        'texts_crosses_saved': "{0} {1} en {2} {3} zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'texts_crosses_saved_voice': "{0} {1} en {2} {3} opgeslagen.",
        'texts_saved': "{0} {1} zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'texts_saved_voice': "{0} {1} opgeslagen.",
        'crosses_saved': "{0} {1} zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'crosses_saved_voice': "{0} {1} opgeslagen.",
        'elements_saved': "{0} elementen zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'elements_saved_voice': "{0} elementen opgeslagen.",
        'text_window_load_error': "Tekstvenster kon niet worden geladen",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Tekstinvoer en tekstblokken – Uitgebreide handleiding**

        **1. Tekst invoegen en bewerken**
        - Klik met de rechtermuisknop op de gewenste plek in het document en kies "Tekst invoegen".
        - Er opent een dialoog waarin u uw tekst kunt invoeren en opmaken:
        • Lettergrootte, Vet, Cursief, Onderstrepen
        • Tekstkleur (vrij te kiezen)
        • Transparantie (dekking) via schuifregelaar
        • Woordterugloop (verschillende breedtes, bv. paginabreedte, smal, geen terugloop)
        - Na bevestiging verschijnt de tekst op de klikpositie. U kunt hem met de muis of pijltjestoetsen verplaatsen.
        - Dubbelklik op de tekst opent de bewerkingsmodus; met ESC verlaat u hem weer.

        **2. Tekstblokken (sjablonen) beheren**
        - In de tekstdialoog ziet u links een lijst van alle opgeslagen tekstblokken.
        - **Blok opslaan:** Voer uw tekst in, formatteer hem en klik op "💾 Als blok opslaan". Voer een bestandsnaam in (zonder extensie).
        - **Blok laden:** Klik in de lijst op de gewenste naam. De tekst en opmaak worden overgenomen en kunnen zo nodig worden aangepast.
        - **Verwijderen:** Klik met rechts op een blok om het te verwijderen of de privéstatus te wijzigen.

        **3. Privétekstblokken (master‑wachtwoord)**
        - Als u een master‑wachtwoord hebt ingesteld (onder Instellingen → Wachtwoordbeheer), kunt u blokken als "privé" markeren.
        - Schakel daarvoor het selectievakje "Privétekstblok" in de dialoog in voordat u opslaat.
        - Privéblokken worden in de lijst alleen getoond als u eenmaal per sessie uw master‑wachtwoord hebt ingevoerd (authenticatie via het slotje of bij eerste toegang).
        - Zo beschermt u vertrouwelijke tekstblokken tegen ongeautoriseerde toegang.

        **4. Kruisen invoegen**
        - Via het contextmenu kunt u ook een grafisch kruis invoegen (bv. voor selectievakjes).
        - De grootte, lijndikte en kleur van kruisen kunt u globaal aanpassen in de instellingen (menu "Instellingen" → "Kruisinstellingen").
        - Klik met rechts op een bestaand kruis om het individueel te wijzigen.

        **5. Verzamelacties**
        - Als u meerdere teksten of kruisen op een pagina hebt geplaatst, kunt u via het contextmenu (rechtsklik in tekstmodus) alle elementen tegelijk opslaan of negeren.
        - Bij opslaan worden alle elementen in de PDF ingebed en blijven ze als vectorgrafieken behouden.

        **6. Sneltoetsen in tekstmodus**
        - Pijltjestoetsen: element verplaatsen
        - Ctrl+Pijltjes: grotere stappen
        - Enter: opslagdialoog openen (alles opslaan / aanpassen / negeren)
        - ESC: huidig element negeren
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Tekstinvoer en tekstblokken – Uitgebreide handleiding</strong></p>

        <p><strong>1. Tekst invoegen en bewerken</strong></p>
        <ul>
        <li>Klik met de rechtermuisknop op de gewenste plek in het document en kies "Tekst invoegen".</li>
        <li>Er opent een dialoog waarin u uw tekst kunt invoeren en opmaken:<br/>
        • Lettergrootte, Vet, Cursief, Onderstrepen<br/>
        • Tekstkleur (vrij te kiezen)<br/>
        • Transparantie (dekking) via schuifregelaar<br/>
        • Woordterugloop (verschillende breedtes, bv. paginabreedte, smal, geen terugloop)</li>
        <li>Na bevestiging verschijnt de tekst op de klikpositie. U kunt hem met de muis of pijltjestoetsen verplaatsen.</li>
        <li>Dubbelklik op de tekst opent de bewerkingsmodus; met ESC verlaat u hem weer.</li>
        </ul>

        <p><strong>2. Tekstblokken (sjablonen) beheren</strong></p>
        <ul>
        <li>In de tekstdialoog ziet u links een lijst van alle opgeslagen tekstblokken.</li>
        <li><strong>Blok opslaan:</strong> Voer uw tekst in, formatteer hem en klik op "💾 Als blok opslaan". Voer een bestandsnaam in (zonder extensie).</li>
        <li><strong>Blok laden:</strong> Klik in de lijst op de gewenste naam. De tekst en opmaak worden overgenomen en kunnen zo nodig worden aangepast.</li>
        <li><strong>Verwijderen:</strong> Klik met rechts op een blok om het te verwijderen of de privéstatus te wijzigen.</li>
        </ul>

        <p><strong>3. Privétekstblokken (master‑wachtwoord)</strong></p>
        <ul>
        <li>Als u een master‑wachtwoord hebt ingesteld (onder Instellingen → Wachtwoordbeheer), kunt u blokken als "privé" markeren.</li>
        <li>Schakel daarvoor het selectievakje "Privétekstblok" in de dialoog in voordat u opslaat.</li>
        <li>Privéblokken worden in de lijst alleen getoond als u eenmaal per sessie uw master‑wachtwoord hebt ingevoerd (authenticatie via het slotje of bij eerste toegang).</li>
        <li>Zo beschermt u vertrouwelijke tekstblokken tegen ongeautoriseerde toegang.</li>
        </ul>

        <p><strong>4. Kruisen invoegen</strong></p>
        <ul>
        <li>Via het contextmenu kunt u ook een grafisch kruis invoegen (bv. voor selectievakjes).</li>
        <li>De grootte, lijndikte en kleur van kruisen kunt u globaal aanpassen in de instellingen (menu "Instellingen" → "Kruisinstellingen").</li>
        <li>Klik met rechts op een bestaand kruis om het individueel te wijzigen.</li>
        </ul>

        <p><strong>5. Verzamelacties</strong></p>
        <ul>
        <li>Als u meerdere teksten of kruisen op een pagina hebt geplaatst, kunt u via het contextmenu (rechtsklik in tekstmodus) alle elementen tegelijk opslaan of negeren.</li>
        <li>Bij opslaan worden alle elementen in de PDF ingebed en blijven ze als vectorgrafieken behouden.</li>
        </ul>

        <p><strong>6. Sneltoetsen in tekstmodus</strong></p>
        <ul>
        <li>Pijltjestoetsen: element verplaatsen</li>
        <li>Ctrl+Pijltjes: grotere stappen</li>
        <li>Enter: opslagdialoog openen (alles opslaan / aanpassen / negeren)</li>
        <li>ESC: huidig element negeren</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Kruisinstellingen",
        'cross_properties': "Kruiseigenschappen",
        'cross_size': "Grootte (px):",
        'cross_line_width': "Lijndikte:",
        'cross_color': "Kleur:",
        'cross_choose_color': "Kiezen",
        'cross_fine_tuning': "Nauwkeurige afstelling bij opslaan (pixels)",
        'cross_offset_x': "X‑verschuiving:",
        'cross_offset_y': "Y‑verschuiving:",
        'cross_offset_x_tooltip': "Negatieve waarden verplaatsen het kruis naar links bij opslaan, positieve naar rechts",
        'cross_offset_y_tooltip': "Negatieve waarden verplaatsen het kruis naar boven bij opslaan, positieve naar beneden",
        'cross_preview': "Voorbeeld",
        'cross_save': "Instellingen toepassen",
        'cross_customized': "Kruis aangepast",
        'cross_settings_applied': "Kruisinstellingen opgeslagen.\nGrootte: {0}px, Lijndikte: {1}px\n{2}",
        'cross_updated_count': "{0} bestaande kruisen zijn bijgewerkt.",
        'cross_no_crosses': "Geen bestaande kruisen gevonden.",
        'cross_settings_applied_all': "Kruisinstellingen toegepast op alle {0} kruisen",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Handtekeninginstellingen",
        'signature_1': "Handtekening 1",
        'signature_2': "Handtekening 2",
        'signature_select': "Handtekening selecteren",
        'signature_add': "➕ Nieuwe handtekening toevoegen...",
        'signature_size': "Grootte voor handtekening {0} (%):",
        'signature_common': "Algemene instellingen",
        'signature_timestamp': "Automatisch tijdstempel toevoegen",
        'signature_location': "Standaardlocatie:",
        'signature_timestamp_size': "Lettergrootte tijdstempel:",
        'signature_no_files': "-- Geen handtekeningen gevonden --",
        'signature_insert': "Handtekening invoegen",
        'signature_insert_1': "Handtekening 1 invoegen",
        'signature_insert_2': "Handtekening 2 invoegen",
        'signature_customize': " Handtekening aanpassen",
        'signature_discard': " Deze handtekening negeren",
        'signature_save_all': " Alle handtekeningen opslaan",
        'signature_discard_all': " Alle handtekeningen negeren",
        'signature_guide_title': "Handtekeningen - Handleiding",
        'signature_guide': """
📝 Handtekeningen - Snelgids

- Master‑wachtwoord instellen
- Handtekeningen configureren in het menu Instellingen
  (grootte, tijdstempel ...)
- Invoegen met RECHTSKLIK op de gewenste positie
  (eenmalig master‑wachtwoord per sessie vereist)
- Handtekening met muis of pijltjestoetsen verplaatsen
- Meerdere handtekeningen kunnen na elkaar worden ingevoegd
- Elke handtekening kan individueel worden aangepast
- Enkele handtekening negeren
- Alle handtekeningen in één keer opslaan / negeren
- Ook de menubalk kan worden gebruikt.
        """,
        'signature_placeholder': "Geen voorbeeld beschikbaar",
        'signature_info': "Handtekening {0}: {1}×{2} px ({3}% van {4}×{5})",
        'signature_info_placeholder': "Instellingen voor handtekening {0}",
        'signature_inserted': "Handtekening {0} ingevoegd op pagina {1}",
        'signature_deleted': "Handtekening verwijderd",
        'signature_copied': "Handtekening gekopieerd",
        'signature_pasted': "Handtekening {0} geplakt",
        'signature_saved': "{0} handtekeningen zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'signature_saved_voice': "{0} handtekeningen opgeslagen",
        'mode_replace_signature_format': "Modus beëindigen en handtekening {0} invoegen",
        'mode_conflict_voice_signature': "{0}‑modus is actief. Beëindigen en handtekening invoegen?",
        'signature_not_configured': "Handtekening {0} niet geconfigureerd",
        'signature_file_not_found': "Handtekeningbestand niet gevonden",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Geen gekopieerde handtekening beschikbaar",
        'no_signatures_to_save': "Geen handtekeningen om op te slaan",
        'signature_save_question': "Alle handtekeningen opslaan, aanpassen of deze negeren?",
        'signatures_saved_title': "Handtekeningen opgeslagen",
        'signatures_saved': "{0} handtekeningen zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'signatures_saved_voice': "{0} handtekeningen opgeslagen.",
        'all_signatures_discarded': "Alle handtekeningen genegeerd",
        'signature_settings_saved': "Handtekeninginstellingen opgeslagen",
        'signature_cancelled': "Handtekening genegeerd",
        'signature_active_title': "Handtekening actief",
        'signature_replace_question': "Er is al een handtekening actief.\n\nWilt u de huidige handtekening vervangen?",
        'signature_replace': "Handtekening vervangen",
        'signature_replace_voice': "Huidige handtekening vervangen of annuleren?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Afbeeldingsinstellingen",
        'image_common': "Algemene afbeeldingsinstellingen",
        'image_keep_aspect': "Beeldverhouding behouden bij slepen",
        'image_default_size': "Standaardgrootte (%):",
        'image_dark_invert': "Afbeeldingen omkeren in donkere modus",
        'image_dark_invert_tooltip': "Ingeschakeld: afbeeldingen worden omgekeerd voor betere zichtbaarheid",
        'image_fine_tuning': "Nauwkeurige afstelling (pixels)",
        'image_offset_x': "X‑verschuiving:",
        'image_offset_y': "Y‑verschuiving:",
        'image_offset_x_tooltip': "Negatieve waarden verplaatsen de afbeelding naar links bij opslaan, positieve naar rechts",
        'image_offset_y_tooltip': "Negatieve waarden verplaatsen de afbeelding naar boven bij opslaan, positieve naar beneden",
        'image_select': "Afbeelding selecteren",
        'image_insert': "Afbeelding invoegen",
        'image_customize': " Afbeelding aanpassen",
        'image_aspect': " Beeldverhouding behouden",
        'image_discard': " Deze afbeelding negeren",
        'image_save_all': " Alle afbeeldingen opslaan",
        'image_discard_all': " Alle afbeeldingen negeren",
        'image_filter': "Afbeeldingen",
        'image_guide_title': "Afbeelding invoegen - Handleiding",
        'image_guide': """
📷 Afbeeldingen in PDF invoegen - Snelgids:

1. Rechtsklik op de gewenste positie
2. "Afbeelding invoegen" → afbeelding selecteren
3. Afbeelding plaatsen: slepen met muis
4. Grootte aanpassen: slepen aan hoeken/randen
5. Beeldverhouding behouden: [A]‑toets
6. Verdere aanpassingen: rechtsklik op afbeelding

Tip: U kunt de instellingen in het contextmenu aanpassen.
        """,
        'image_inserted': "Afbeelding {0} ingevoegd op pagina {1}",
        'image_deleted': "Afbeelding genegeerd",
        'image_copied': "Afbeelding gekopieerd",
        'image_pasted': "Afbeelding geplakt",
        'image_saved': "{0} afbeeldingen zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'image_saved_voice': "{0} afbeeldingen opgeslagen",
        'image_aspect_on': "ingeschakeld",
        'image_aspect_off': "uitgeschakeld",
        'image_aspect_toggle': "Beeldverhouding behouden {0}",
        'image_reset': "Afbeelding teruggezet naar oorspronkelijke grootte",
        'image_replaced': "Afbeelding vervangen",
        'image_invalid': "Geen geldige afbeelding",
        'mode_replace_image': "Afbeelding invoegen",
        'mode_conflict_voice_image': "{0}‑modus is actief. Beëindigen en afbeelding invoegen?",
        'image_active_title': "Afbeelding actief",
        'image_replace_question': "Er is al een afbeelding actief.\n\nWilt u de huidige afbeelding vervangen?",
        'image_replace': "Afbeelding vervangen",
        'image_replace_voice': "Huidige afbeelding vervangen of annuleren?",
        'image_filter_all': "Afbeeldingen (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Alle bestanden (*.*)",
        'no_copied_image': "Geen gekopieerde afbeelding beschikbaar",
        'image_discarded': "Afbeelding genegeerd",
        'image_save_question': "Alle afbeeldingen opslaan, aanpassen of deze negeren?",
        'no_images_to_save': "Geen afbeeldingen om op te slaan",
        'no_valid_images': "Geen geldige afbeeldingen om op te slaan",
        'images_saved_title': "Afbeeldingen opgeslagen",
        'images_saved': "{0} afbeeldingen zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'images_saved_voice': "{0} afbeeldingen opgeslagen.",
        'all_images_discarded': "Alle afbeeldingen genegeerd",
        'image_settings_updated': "Afbeeldingsinstellingen bijgewerkt",
        'image_replace_title': "Nieuwe afbeelding selecteren",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Vorminstellingen",
        'form_basic': "Basisinstellingen",
        'form_default_type': "Standaard vormtype:",
        'form_rectangle': "Rechthoek",
        'form_ellipse': "Ellips",
        'form_line': "Lijn",
        'form_arrow': "Pijl",
        'form_line_width': "Lijndikte:",
        'form_colors': "Kleuren",
        'form_line_color': "Lijnkleur:",
        'form_fill_color': "Vulkleur:",
        'form_choose_color': "Kiezen",
        'form_transparent': "Transparante achtergrond (alleen lijn)",
        'form_filled': "gevuld",
        'form_dark_mode': "Donkere modus",
        'form_dark_invert': "Kleuren omkeren in donkere modus",
        'form_fine_tuning': "Nauwkeurige afstelling (pixels)",
        'form_offset_x': "X‑verschuiving:",
        'form_offset_y': "Y‑verschuiving:",
        'form_offset_x_tooltip': "Negatieve waarden verplaatsen de vorm naar links bij opslaan, positieve naar rechts",
        'form_offset_y_tooltip': "Negatieve waarden verplaatsen de vorm naar boven bij opslaan, positieve naar beneden",
        'form_preview': "Voorbeeld",
        'form_insert': "Vorm invoegen",
        'form_rectangle_insert': "Rechthoek",
        'form_ellipse_insert': "Ellips/Cirkel",
        'form_line_insert': "Lijn (2 klikken)",
        'form_arrow_insert': "Pijl (2 klikken)",
        'form_customize': " Vorm aanpassen",
        'form_transparent_toggle': " Transparante achtergrond",
        'form_discard': " Deze vorm negeren",
        'form_save_all': " Alle vormen opslaan",
        'form_discard_all': " Alle vormen negeren",
        'form_guide_title': "Vorm invoegen - Handleiding",
        'form_guide': """
📐 Vormen in PDF invoegen - Snelgids:

1. Kies vormtype (rechthoek, ellips, lijn, pijl)
2. Klik op de positie
   - Bij rechthoek/ellips: één klik plaatst de vorm
   - Bij lijn/pijl: twee klikken voor begin‑ en eindpunt
3. Vorm plaatsen: slepen met muis
4. Grootte aanpassen: slepen aan hoeken/randen
5. Vorm opslaan: Enter
6. Vorm negeren: ESC
7. Verdere aanpassingen: rechtsklik op vorm

Tip: U kunt de instellingen in het contextmenu aanpassen.
        """,
        'form_inserted': "{0} ingevoegd op pagina {1}",
        'form_deleted': "Vorm verwijderd",
        'form_copied': "Vorm gekopieerd",
        'form_pasted': "Vorm geplakt",
        'form_saved': "{0} vormen zijn in de PDF ingevoegd.\n\nPDF is herladen...",
        'form_saved_voice': "{0} vormen opgeslagen",
        'form_reset': "Vorm teruggezet naar standaardgrootte",
        'form_transparent_on': "ingeschakeld",
        'form_transparent_off': "uitgeschakeld",
        'form_transparent_toggled': "Transparante achtergrond {0}",
        'form_line_cancel': "Lijn tekenen geannuleerd",
        'form_second_click': "Klik nu op het eindpunt voor {0}",
        'mode_replace_form': "Vorm invoegen",
        'mode_conflict_voice_form': "{0}‑modus is actief. Beëindigen en een vorm invoegen?",
        'form_settings_updated': "Vorminstellingen bijgewerkt",
        'form_unknown': "Vorm",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klik op de startpositie",
        'form_line_guide_2': "2. Klik op de eindpositie",
        'form_line_guide_3': "De lijn wordt tussen beide punten getekend.",
        'form_line_status_1': "Wacht op eerste klik...",
        'form_line_status_2': "Eerste punt ingesteld: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Klik nu op het eindpunt...",
        'form_line_status_4': "Beide punten ingesteld.\nKlik op 'Gereed' om op te slaan.",
        'form_line_reset': "Opnieuw",
        'form_line_finish': "Gereed",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopiëren (Cmd+C)",
        'paste': "Plakken (Cmd+V)",
        'copied': "Gekopieerd: {0}",
        'no_element_to_copy': "Geen element geselecteerd om te kopiëren",
        'no_copied_data': "Geen gekopieerde gegevens beschikbaar",
        'no_valid_position': "Geen geldige positie om te plakken",
        'copy_text': "Tekst gekopieerd",
        'copy_image': "Afbeelding gekopieerd",
        'copy_form': "Vorm gekopieerd",
        'copy_signature': "Handtekening gekopieerd",
        'element_text': "tekst",
        'element_image': "afbeelding",
        'element_form': "vorm",
        'element_signature': "handtekening",
        'element_unknown': "element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Modusconflict",
        'mode_conflict_message': "De modus '{0}' is al actief.\n\nWilt u deze beëindigen en {1}?",
        'mode_replace': "Modus beëindigen en {0}",
        'mode_cancel': "Annuleren",
        'mode_replace_text': "tekst invoegen",
        'mode_replace_cross': "kruis invoegen",
        'mode_replace_signature': "handtekening invoegen",
        'mode_replace_image': "afbeelding invoegen",
        'mode_replace_form': "vorm invoegen",
        'mode_conflict_voice': "{0}‑modus is actief. Beëindigen en tekst invoegen?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Tekstinvoer",
        'active_mode_signature': "Handtekening",
        'active_mode_image': "Afbeelding",
        'active_mode_form': "Vorm",
        'active_mode_and': " en ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Invoegen",                    # Hauptmenü
        'insert_another_text': "Tekst invoegen",          # Vereinfacht
        'insert_another_cross': "Kruis invoegen",        # Vereinfacht
        'insert_another_signature_1': "Handtekening 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Handtekening 2",      # Untermenü-Eintrag
        'insert_another_image': "Afbeelding invoegen",         # Vereinfacht
        'insert_another_form_rect': "Rechthoek",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellips",        # Untermenü-Eintrag
        'insert_another_form_line': "Lijn (2 klikken)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Pijl (2 klikken)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} opslaan",
        'save_dialog_message': "{0} wordt op pagina {1} opgeslagen.\n\nHoe wilt u verdergaan?",
        'save_all': "Alle {0} opslaan",
        'save_single': "{0} opslaan",
        'save_customize': "{0} aanpassen",
        'save_discard': "Deze {0} negeren",
        'save_continue': "Verder bewerken",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Naar pagina {0} gaan",
        'context_rotate': " Pagina {0} draaien",
        'context_delete': " Pagina {0} verwijderen",
        'context_export': " Pagina {0} exporteren",
        'context_mark_as': " Pagina markeren als...",
        'context_mark_empty': " Lege pagina",
        'context_unmark_empty': " Niet langer leeg",
        'context_mark_export': " Voor export markeren",
        'context_unmark_export': " Niet meer exporteren",
        'context_batch_actions': " Verzamelacties",
        'context_batch_delete_empty': " Alle {0} lege pagina's verwijderen",
        'context_batch_export_single': " Alle {0} pagina's (één bestand)",
        'context_batch_export_split': " Alle {0} pagina's (afzonderlijk)",
        'context_drag_start': " Drag & drop starten",
        'context_drag_stop': " Drag & drop beëindigen",
        'context_insert': " Invoegen",
        'context_insert_pages': " Pagina's invoegen",
        'context_zoom': "Zoom",
        'discard_mixed': "Alle {0} {1} en {2} {3} negeren",
        'save_mixed': "{0} {1} en {2} {3} opslaan",
        'discard_texts': "Alle {0} teksten negeren",
        'discard_text_single': "1 tekst negeren",
        'save_texts': "{0} teksten opslaan",
        'save_text_single': "1 tekst opslaan",
        'discard_crosses': "Alle {0} kruisen negeren",
        'discard_cross_single': "1 kruis negeren",
        'save_crosses': "{0} kruisen opslaan",
        'save_cross_single': "1 kruis opslaan",
        'discard_signatures': "Alle {0} handtekeningen negeren",
        'save_signature_single': "1 handtekening opslaan",
        'save_signatures': "{0} handtekeningen opslaan",
        'discard_images': "Alle {0} afbeeldingen negeren",
        'save_image_single': "1 afbeelding opslaan",
        'save_images': "{0} afbeeldingen opslaan",
        'discard_forms': "Alle {0} vormen negeren",
        'save_form_single': "1 vorm opslaan",
        'save_forms': "{0} vormen opslaan",
        'cross_discard': "Dit kruis negeren",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Export‑ / importinformatie",
        'export_what': "📋 Wat wordt geëxporteerd?",
        'export_general': "Algemene instellingen",
        'export_general_items': "• Spraakuitvoer (aan/uit, snelheid)\n• Donkere/lichte modus\n• Back‑upinstellingen\n• OCR‑instellingen",
        'export_image_form': "Afbeeldings‑ en vorminstellingen",
        'export_image_form_items': "• Afbeeldingsinstellingen (beeldverhouding, standaardgrootte)\n• Vorminstellingen (lijndikte, kleuren)\n• Handtekeninginstellingen (paden, groottes, tijdstempel)",
        'export_passwords': "Wachtwoordendatabase",
        'export_passwords_items': "• Alle opgeslagen PDF‑wachtwoorden\n• Naar keuze versleuteld of ontsleuteld",
        'export_master': "Master‑wachtwoordinstellingen",
        'export_master_items': "• Master‑wachtwoord‑hash\n• Instellingen voor handtekeningen/tekstblokken",
        'export_signatures': "Handtekeningen en tekstblokken",
        'export_signatures_items': "• Alle afbeeldingsbestanden (handtekeningen)\n• Alle tekstblokken met opmaak\n• Privé/openbare markeringen",
        'export_import_warning': "⚠️ Belangrijke opmerkingen",
        'export_import_note': "• Bij importeren worden ALLE huidige instellingen overschreven\n• Een herstart van de applicatie is vereist\n• Bestaande handtekeningen/tekstblokken worden vervangen",
        'export_master_note': "• Als een master‑wachtwoord is ingesteld, kunt u kiezen:\n  - Ontsleuteld (wachtwoorden in platte tekst)\n  - Versleuteld (alleen leesbaar met master‑wachtwoord)",
        'export_security': "• Het geëxporteerde ZIP‑bestand bevat vertrouwelijke gegevens\n• Bewaar het veilig (bijv. versleutelde USB‑stick)\n• Bij verlies van het bestand zijn wachtwoorden onherroepelijk verloren",
        'export_format': "📁 Exportformaat",
        'export_format_desc': "De instellingen worden opgeslagen in één ZIP‑bestand:",
        'export_filename': "PDFDarkView_Instellingen_JJJJMMDD_UUmmss.zip",
        'export_success': "Instellingen succesvol geëxporteerd",
        'export_failed': "Exporteren mislukt",
        'export_import_question': "Wilt u de applicatie nu herstarten?",
        'export_password_question': "Er is een master‑wachtwoord ingesteld.\n\nWilt u de wachtwoorden ontsleuteld exporteren?\n(anders worden ze versleuteld geëxporteerd)",
        'export_decrypt': "Ontsleuteld exporteren",
        'export_encrypt': "Versleuteld exporteren",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Over PDF Dark View",
        'info_version': "Versie",
        'info_author': "Ontwikkeld door Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Over",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> is een toegankelijke PDF-viewer, speciaal ontwikkeld voor mensen met een visuele beperking.</p>

            <p><strong>Kernmerken:</strong></p>
            <ul>
                <li>Contrastrijk, aanpasbare interface</li>
                <li>Volledige toetsenbordbediening</li>
                <li>Geïntegreerde voorleesfunctie</li>
                <li>OCR voor gescande documenten</li>
                <li>Uitgebreide bewerkingstools</li>
            </ul>

            <p>Meer dan 50 talen worden ondersteund – zodat PDF's voor iedereen toegankelijk zijn.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Functies",
        'info_features_intro': "PDF Dark View biedt u de volgende mogelijkheden:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Weergave & Navigatie</strong> – Donker/Licht-modus, pagina's bladeren, zoom, spring naar pagina</li>
            <li><strong>OCR (tekstherkenning)</strong> – Maak gescande documenten doorzoekbaar en kopieerbaar</li>
            <li><strong>Bewerking</strong> – Tekst, kruizen, handtekeningen, afbeeldingen en vormen invoegen</li>
            <li><strong>Paginabeheer</strong> – Verwijderen, extraheren, invoegen, verplaatsen via slepen & neerzetten</li>
            <li><strong>Export</strong> – Naar Word, Pages of als tekst</li>
            <li><strong>Beveiliging</strong> – Wachtwoordbeveiliging en -beheer</li>
            <li><strong>Toegankelijkheid</strong> – Voorleesfunctie, toetsenbordbediening, hoog contrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Bediening",
        'info_accessibility': "♿ Toegankelijkheid – volledige toetsenbordbediening",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Algemeen</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF openen</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Zoeken</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Donker/Licht-modus schakelen</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Afdrukken</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Afsluiten</div>

        <div class="shortcut-cat">📖 Navigatie</div>
        <div class="shortcut-row"><kbd>Pijltjestoetsen</kbd> Pagina voor pagina bladeren</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Ga naar pagina</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Eerste pagina</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Laatste pagina</div>

        <div class="shortcut-cat">✏️ Bewerking</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Tekst invoegen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Pagina's verwijderen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Pagina's extraheren</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Pagina's invoegen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Pagina's verplaatsen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Pagina draaien</div>

        <div class="shortcut-cat">🖼️ Elementen verplaatsen</div>
        <div class="shortcut-row"><kbd>Pijltjestoetsen</kbd> Tekst/afbeelding/handtekening verplaatsen</div>
        <div class="shortcut-row"><kbd>Ctrl+Pijltjestoetsen</kbd> Grotere stappen</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Opslaan</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Annuleren</div>

        <div class="shortcut-cat">🗣️ Voorleesfunctie</div>
        <div class="shortcut-row"><kbd>F2</kbd> Voorleesfunctie aan/uit</div>
        """,
        'info_contextmenu': "📌 Belangrijk: Alle functies zijn ook via het contextmenu (rechtermuisknop) bereikbaar!",
        'info_accessibility_hint': "💡 Tip: De voorleesfunctie (F2) vergemakkelijkt de oriëntatie en geeft feedback over menu's en dialoogvensters.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licentie & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Informatie volgens § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Duitsland<br>
        E-mail: binhdiez64@gmail.com<br>
        Verantwoordelijk voor de inhoud: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Aansprakelijkheidsuitsluiting</strong><br>
        De software is met de grootste zorg ontwikkeld. Er wordt geen garantie gegeven voor de juistheid, volledigheid en functionaliteit. Het gebruik is op eigen risico.<br><br>

        <strong>📄 MIT-licentie (privégebruik)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Toegestaan: gratis gebruik, privéwijzigingen, persoonlijke kopieën.<br>
        Niet toegestaan: verkoop, commercieel gebruik, verwijdering van copyrightmeldingen.<br><br>

        <strong>🔧 Componenten van derden</strong><br>
        Deze software bevat componenten onder GPL, AGPL, Apache 2.0, BSD en MIT-licenties.<br>
        Bij verdere verspreiding moeten de respectievelijke licentievoorwaarden worden nageleefd.<br><br>

        <strong>🌐 Open Source</strong><br>
        De broncode is beschikbaar en kan worden bekeken, gewijzigd en verder verspreid volgens de respectievelijke licentievoorwaarden.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Dankwoord",
        'info_credits': "Dank aan de open-sourcegemeenschap",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-verwerking</li>
            <li><strong>PyQt5</strong> – Grafische interface</li>
            <li><strong>Tesseract OCR</strong> – Tekstherkenning</li>
            <li><strong>OCRmyPDF</strong> – OCR-integratie</li>
            <li><strong>python-docx</strong> – Word-export</li>
            <li><strong>qtawesome</strong> – Iconen</li>
            <li><strong>DeepSeek</strong> – Ondersteuning bij vertalingen (50+ talen)</li>
            <li><strong>Alle gebruikers</strong> – Voor waardevolle feedback</li>
            <li><strong>De open-sourcegemeenschap</strong> – Voor geweldige bibliotheken</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Talen",
        'info_languages_header': "🌍 Taalondersteuning",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View ondersteunt momenteel <strong>62 talen</strong> – zodat de software wereldwijd toegankelijk kan worden gebruikt.</p>

            <p><strong>📖 Volledige taallijst (Stand: maart 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanees (Shqip)</li>
                    <li>🇩🇿 Arabisch (العربية)</li>
                    <li>🇮🇩 Balinees (Basa Bali)</li>
                    <li>🇧🇩 Bengaals (বাংলা)</li>
                    <li>🇲🇲 Birmees (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnisch (Bosanski)</li>
                    <li>🇧🇬 Bulgaars (Български)</li>
                    <li>🇨🇳 Chinees (中文)</li>
                    <li>🇩🇰 Deens (Dansk)</li>
                    <li>🇩🇪 Duits (Deutsch)</li>
                    <li>🇬🇧 Engels (English)</li>
                    <li>🇪🇪 Estisch (Eesti)</li>
                    <li>🇫🇮 Fins (Suomi)</li>
                    <li>🇫🇷 Frans (Français)</li>
                    <li>🇬🇷 Grieks (Ελληνικά)</li>
                    <li>🇮🇱 Hebreeuws (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatisch (Hrvatski)</li>
                    <li>🇭🇺 Hongaars (Magyar)</li>
                    <li>🇮🇩 Indonesisch (Bahasa Indonesia)</li>
                    <li>🇮🇪 Iers (Gaeilge)</li>
                    <li>🇮🇸 IJslands (Íslenska)</li>
                    <li>🇮🇹 Italiaans (Italiano)</li>
                    <li>🇯🇵 Japans (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreaans (한국어)</li>
                    <li>🇱🇦 Laotiaans (ພາສາລາວ)</li>
                    <li>🇱🇻 Lets (Latviešu)</li>
                    <li>🇱🇹 Litouws (Lietuvių)</li>
                    <li>🇱🇺 Luxemburgs (Lëtzebuergesch)</li>
                    <li>🇲🇾 Maleis (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongools (Монгол)</li>
                    <li>🇳🇵 Nepalees (नेपाली)</li>
                    <li>🇳🇱 Nederlands (Nederlands)</li>
                    <li>🇳🇴 Noors (Norsk)</li>
                    <li>🇦🇫 Pasjtoe (پښتو)</li>
                    <li>🇮🇷 Perzisch (فارسی)</li>
                    <li>🇵🇱 Pools (Polski)</li>
                    <li>🇵🇹 Portugees (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Roemeens (Română)</li>
                    <li>🇷🇺 Russisch (Русский)</li>
                    <li>🇸🇪 Zweeds (Svenska)</li>
                    <li>🇷🇸 Servisch (Српски)</li>
                    <li>🇸🇰 Slowaaks (Slovenčina)</li>
                    <li>🇸🇮 Sloveens (Slovenščina)</li>
                    <li>🇪🇸 Spaans (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Tsjechisch (Čeština)</li>
                    <li>🇹🇷 Turks (Türkçe)</li>
                    <li>🇺🇦 Oekraïens (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamees (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddisch (ייִדיש)</li>
                    <li>🇿🇦 Zoeloe (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Eigen talen toevoegen:</strong><br>
                Wil je een taal die nog niet is opgenomen? Plaats gewoon je eigen woordenboekbestand (<code>sprache_xx.py</code>) naast de applicatie – de software herkent het automatisch. Als je geïnteresseerd bent in een specifieke vertaling, neem dan gerust contact met mij op.
            </div>

            <p><strong>🙏 Bijzondere dank:</strong> DeepSeek voor de ondersteuning bij het vertalen van alle woordenboeken in 62 talen.</p>

            <p>📧 Contact voor vertalingen: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Fout",
        'error_occurred': "Er is een fout opgetreden",
        'error_pdf_load': "Fout bij laden van PDF",
        'error_pdf_save': "Fout bij opslaan van PDF",
        'error_ocr': "Fout bij tekstherkenning",
        'error_no_pdf': "Geen PDF geladen",
        'error_page_not_found': "Pagina niet gevonden",
        'error_invalid_range': "Ongeldig paginabereik",
        'error_file_not_found': "Bestand niet gevonden",
        'error_permission': "Geen toestemming",
        'error_unknown': "Onbekende fout",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Succes",
        'success_operation': "Bewerking succesvol afgerond",
        'success_saved': "Succesvol opgeslagen",
        'success_exported': "Succesvol geëxporteerd",
        'success_imported': "Succesvol geïmporteerd",
        'success_deleted': "Succesvol verwijderd",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Bevestiging",
        'confirm_yes': "Ja",
        'confirm_no': "Nee",
        'confirm_ok': "OK",
        'confirm_cancel': "Annuleren",
        'confirm_delete': "Verwijderen",
        'confirm_overwrite': "Overschrijven",
        'confirm_continue': "Doorgaan",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF laden...",
        'progress_saving': "PDF opslaan...",
        'progress_exporting': "PDF exporteren...",
        'progress_processing': "Bezig met verwerken...",
        'progress_wait': "Even geduld...",
        'progress_preparing': "Voorbereiden...",
        'progress_finalizing': "Afronden...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Wit",
        'color_black': "Zwart",
        'color_red': "Rood",
        'color_green': "Groen",
        'color_blue': "Blauw",
        'color_yellow': "Geel",
        'color_magenta': "Magenta",
        'color_cyan': "Cyaan",
        'color_orange': "Oranje",
        'color_gray': "Grijs",
        'color_custom': "Kleurkiezer",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Bestand",
        'menu_edit': "&Bewerken",
        'menu_view': "&Beeld",
        'menu_tools': "&Extra",
        'menu_settings': "&Instellingen",
        'menu_help': "&Help",
        'menu_language': "🌐 Taal",
        'menu_guides': "&Handleidingen",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Openen",
        'file_save_as': "&Opslaan als...",
        'file_protect': "Document &beveiligen...",
        'file_export': "&Exporteren",
        'file_export_pages': "Exporteren als Pages",
        'file_export_word': "Exporteren als DOCX",
        'file_export_text': "Exporteren als TXT",
        'file_print_now': "&Nu afdrukken",
        'file_print': "&Afdrukken",
        'file_close': "&Sluiten",
        'file_quit': "&Afsluiten",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Zoeken",
        'edit_ocr': " OCR uitvoeren",
        'edit_rotate': "Pagina &draaien",
        'edit_rotate_all': "&Alle pagina's draaien",
        'edit_delete_pages': "Pagina's &verwijderen",
        'edit_extract_pages': "Pagina's &uithalen",
        'edit_insert_pages': "Pagina's &invoegen",
        'edit_move_pages': "Pagina's &verplaatsen",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Tekst en kruisen invoegen",
        'text_insert': " Tekst invoegen",
        'cross_insert': " Kruis invoegen",
        'text_customize': " Tekst aanpassen",
        'cross_customize': " Dit kruis aanpassen",
        'cross_customize_all': " Alle kruisen aanpassen",
        'text_discard': " Deze tekst/dit kruis negeren",
        'text_discard_all': " Alle teksten en kruisen negeren",
        'text_save_all': " Alle teksten en kruisen opslaan",
        'text_guide': " Tekstinvoer / tekstblokken - Handleiding",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Handtekening invoegen",
        'signature_settings_menu': " Instellingen...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Afbeelding invoegen",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Vormen invoegen",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Tekstvenster tonen",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Paginabreedte (standaard)",
        'view_zoom_two': "&Twee pagina's",
        'view_zoom_overview': "&Overzicht (meerdere pagina's)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Toegankelijkheid",
        'settings_voice': "Spraakuitvoer",
        'settings_voice_tooltip': "vult de spraakuitvoer van schermlezers aan met extra informatie",
        'settings_signature': "&Handtekeninginstellingen",
        'settings_password': "&Wachtwoordbeheer",
        'settings_backup': "Backup maken vóór wijzigingen",
        'settings_export_import': "&Instellingen exporteren / importeren",
        'settings_export': "&Alle instellingen exporteren...",
        'settings_import': "&Alle instellingen importeren...",
        'settings_export_info': "&Wat wordt geëxporteerd?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "aan",
        'voice_off': "uit",
        'voice_toggle': "Spraakuitvoer {0}",
        'voice_speed': "Snelheid op {0} procent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Hulpprogramma niet gevonden:\n{0}\n\nBASE_DIR: {1}\nZorg ervoor dat de PDF‑hulpprogramma's in de map {1} zijn geïnstalleerd.",
        'tool_started': "{0} gestart",
        'tool_start_failed': "Kon niet starten",
        'process_error_failed_to_start': "Proces kon niet worden gestart. Bestaat het bestand?",
        'process_error_crashed': "Proces gecrasht tijdens opstarten.",
        'process_error_timeout': "Time‑out van proces bereikt.",
        'process_error_write': "Schrijffout naar proces.",
        'process_error_read': "Leesfout van proces.",
        'process_error_unknown': "Onbekende procesfout",
        'process_command': "Opdracht",
        'process_normal_exit': "normaal beëindigd",
        'process_crashed': "gecrasht",
        'process_nonzero_exit': "{0} beëindigd met foutcode {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Annuleren...",
        'move_cancelling': "Verplaatsen wordt geannuleerd",
        'opening_pdf': "PDF wordt geopend...",
        'loading_document': "Document laden...",
        'pdf_opened': "PDF geopend",
        'pages_found_moving': "{0} pagina's gevonden, {1} te verplaatsen",
        'creating_backup': "Backup maken...",
        'backup_description': "Origineel bestand veiligstellen...",
        'backup_saved_as': "Opgeslagen als: {0}",
        'error_format': "Fout: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Zoekopdracht gereset",
        'page_header_simple': "=== Pagina {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Wachtwoordbeheer – Handleiding",
        'password_guide_voice': "Handleiding voor wachtwoordbeheer. Lees de opmerkingen.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Wachtwoordbeheer – Uitgebreide handleiding</strong></p>

        <p><strong>1. Wachtwoordbeveiliging voor PDF's</strong></p>
        <ul>
        <li>Bij het openen van een met een wachtwoord beveiligde PDF verschijnt een dialoog waarin u het wachtwoord kunt invoeren.</li>
        <li>U kunt het wachtwoord versleuteld opslaan, zodat u het niet elke keer opnieuw hoeft in te voeren (selectievakje "Wachtwoord opslaan").</li>
        <li>Met de knop "Wachtwoord verwijderen" kunt u een ontsleutelde kopie van de PDF maken en het wachtwoord uit de database verwijderen.</li>
        </ul>

        <p><strong>2. Master‑wachtwoord</strong></p>
        <ul>
        <li>Het master‑wachtwoord beveiligt de toegang tot alle opgeslagen PDF‑wachtwoorden.</li>
        <li><strong>Instellen:</strong> Ga naar "Instellingen → Wachtwoordbeheer → Master‑wachtwoordinstellingen" en klik op "Master‑wachtwoord instellen". Kies een sterk master‑wachtwoord (minimaal 8 tekens).</li>
        <li><strong>Wijzigen:</strong> Na succesvolle authenticatie kunt u het master‑wachtwoord wijzigen.</li>
        <li><strong>Verwijderen:</strong> Als u het master‑wachtwoord verwijdert, worden ALLE opgeslagen wachtwoorden onherroepelijk gewist. U kunt vooraf een backup exporteren.</li>
        <li>Eenmaal per sessie moet u zich met het master‑wachtwoord authenticeren om toegang te krijgen tot beveiligde functies (bijv. wachtwoorden bekijken).</li>
        </ul>

        <p><strong>3. Wachtwoordbeheer (lijst)</strong></p>
        <ul>
        <li>Onder "Instellingen → Wachtwoordbeheer" opent u een tabel met alle opgeslagen PDF's en hun versleutelde wachtwoorden.</li>
        <li><strong>Zonder master‑wachtwoord:</strong> U kunt alleen vermeldingen verwijderen – de wachtwoorden blijven verborgen.</li>
        <li><strong>Met master‑wachtwoord (geauthenticeerd):</strong> U kunt wachtwoorden bekijken, kopiëren, exporteren en verwijderen.</li>
        <li><strong>Exporteren:</strong> Kies een formaat (JSON, CSV, TXT) en sla de lijst op. Als een master‑wachtwoord is ingesteld, kunt u kiezen of de wachtwoorden in platte tekst of nog steeds versleuteld worden geëxporteerd.</li>
        <li><strong>Importeren:</strong> Een eerder geëxporteerd ZIP‑bestand met alle instellingen (inclusief wachtwoorden) kan opnieuw worden ingelezen via "Instellingen → Instellingen exporteren/importeren". Let op: bestaande gegevens worden overschreven!</li>
        </ul>

        <p><strong>4. Wachtwoordgenerator</strong></p>
        <ul>
        <li>In de wachtwoorddialoog (bijv. bij het beveiligen van een PDF) vindt u rechts van het invoerveld een dobbelsteenknoop 🎲.</li>
        <li>Klik erop om de wachtwoordgenerator te openen. U kunt lengte, tekensets (hoofdletters, kleine letters, cijfers, symbolen) en een scheidingsteken voor betere leesbaarheid instellen.</li>
        <li>Het gegenereerde wachtwoord kan direct worden overgenomen en indien nodig worden gekopieerd.</li>
        </ul>

        <p><strong>5. Belangrijke veiligheidsopmerkingen</strong></p>
        <ul>
        <li>Opgeslagen wachtwoorden worden versleuteld met AES‑256 opgeslagen. De sleutel wordt afgeleid van uw master‑wachtwoord (indien ingesteld) of van een vaste waarde (zonder master‑wachtwoord).</li>
        <li>Zonder master‑wachtwoord zijn de wachtwoorden weliswaar versleuteld, maar de sleutel is in het programma ingebed – een aanvaller met toegang tot uw bestanden zou ze kunnen ontsleutelen. Daarom raden we ten zeerste het gebruik van een master‑wachtwoord aan.</li>
        <li>De wachtwoordendatabase bevindt zich in de map `Data/wachtwoorden.json`. Maak regelmatig backups, vooral voordat u het master‑wachtwoord verwijdert.</li>
        <li>Bij verlies van het master‑wachtwoord zijn alle opgeslagen wachtwoorden onherroepelijk verloren.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Inversiemodus",
        'invert_mode_classic': "Klassiek (alle kleuren inverteren)",
        'invert_mode_smart': "Slim (alleen helderheid inverteren)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Grijswaardedrempel",
        'gray_threshold_10': "10% (streng)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standaard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (zacht)",
        'threshold_changed': "Drempel ingesteld op {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Grijswaardedrempel – Uitleg",
        'threshold_guide_text': "De grijswaardedrempel bepaalt welke pixels in de slimme donkere modus als 'grijs' worden beschouwd en worden geïnverteerd.\n\n"
                                "• Een lage waarde (10%) inverteert alleen bijna perfecte grijstinten – gekleurde elementen blijven volledig behouden.\n"
                                "• Een hoge waarde (50%) inverteert ook licht gekleurde pixels – dit verhoogt het contrast, maar kan kleuren vervormen.\n\n"
                                "De optimale waarde hangt af van het document. Voor pure tekstdocumenten is 30–40% vaak ideaal, voor gekleurde afbeeldingen eerder 10–20%.\n\n"
                                "U kunt de waarde op elk moment aanpassen via het menu 'Instellingen' – de PDF wordt dan onmiddellijk herladen.\n\n"
                                "Let op:\n* Foto's en afbeeldingen kunnen alleen correct worden weergegeven in de lichte modus!\n* De inversie-instellingen worden alleen weergegeven wanneer de donkere modus is geactiveerd.",
        'threshold_guide_voice': "De grijswaardedrempel bepaalt hoe sterk de slimme donkere modus ingrijpt. Een lage waarde spaart kleuren, een hoge waarde verhoogt het contrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF wordt geopend...",
        'progress_loading_document': "Document laden...",
        'progress_pdf_opened': "PDF geopend",
        'progress_creating_backup': "Back-up maken...",
        'progress_backup_description': "Origineel bestand beveiligen...",
        'progress_backup_created': "Back-up gemaakt",
        'progress_backup_saved_as': "Opgeslagen als: {0}",
        'progress_analyzing_start': "Analyse starten...",
        'progress_searching_empty': "Lege pagina's zoeken...",
        'progress_page_empty': "Pagina {0} is leeg",
        'progress_page_keep': "Pagina {0} behouden",
        'progress_analysis_complete': "Analyse voltooid",
        'progress_empty_found': "{0} lege pagina's gevonden",
        'progress_current_page': "Huidige pagina",
        'progress_mark_delete': "Wordt gemarkeerd voor verwijdering",
        'progress_range_selected': "Paginabereik {0}-{1}",
        'progress_deleting_pages': "{0} pagina's verwijderen",
        'progress_creating_new_pdf': "Nieuwe PDF maken...",
        'progress_transferring_pages': "Pagina's overzetten",
        'progress_keeping_page': "Pagina {0} wordt behouden ({1}/{2})",
        'progress_saving_pdf': "PDF opslaan...",
        'progress_optimizing': "Bestandsgrootte optimaliseren...",
        'progress_finalizing': "Finaliseren...",
        'progress_new_size': "Nieuwe grootte: {0:.2f} MB",
        'progress_cancelling': "Annuleren...",
        'progress_cancel_message': "{0} wordt geannuleerd",
        'progress_pages_found_moving': "{0} pagina's gevonden, {1} om te verplaatsen",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF wordt geanalyseerd...",
        'ocr_status_optimizing': "Afbeeldingsoptimalisatie bezig...",
        'ocr_status_recognizing': "Tekstherkenning bezig...",
        'ocr_status_embedding': "Tekst wordt ingebed...",
        'ocr_status_finalizing': "PDF wordt gefinaliseerd...",

        # PDF-Laden
        'progress_preparing': "Voorbereiden...",
        'progress_loading': "PDF wordt geladen...",

        # Seitenoperationen
        'progress_deleting_title': "Pagina's verwijderen...",
        'progress_moving_title': "Pagina's verplaatsen...",
        'pages_found': "Pagina's gevonden",
        'progress_creating_new_order': "Nieuwe volgorde maken...",
        'progress_sorting_pages': "Pagina's sorteren...",
        'progress_moving_to_begin': "{0} pagina's naar het begin verplaatsen",
        'progress_transferring_count': "{0} pagina's overzetten",
        'progress_transferring_before_target': "Pagina's voor het doel overzetten",
        'progress_moving_pages': "{0} pagina's verplaatsen",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_back-up_",
        'filename_protected_suffix': "_beschermd_",
        'filename_copy_suffix': "_Kopie",
        'filename_page_single': "_Pagina_",
        'filename_page_range': "_Paginas_",
        'filename_export_page': "_Pagina_{0:03}",
        'filename_export_range': "_Paginas_{0}-{1}",
        'filename_export_multiple': "_Paginas_{0}",
        'filename_with_text': "_met_Tekst",
        'filename_with_signature': "_met_Handtekening",
        'filename_with_image': "_met_Afbeelding",
        'filename_with_forms': "_met_Vormen",
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
        'view_toggle_navbar': "Knopbalk weergeven",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Niet alle pagina's kunnen worden verwijderd",
		'pages_cannot_delete_last_page': 'De laatste pagina kan niet worden verwijderd!',
		'pages_cannot_delete_all_pages': 'Er moet minimaal één pagina in het document blijven!',
		'delete_pages_confirm': 'Weet u zeker dat u {0} pagina\'s wilt verwijderen?',
		'delete_pages_confirm_voice': 'Weet u zeker dat u {0} pagina\'s wilt verwijderen?',
		'pages_deleted': '{0} pagina\'s zijn succesvol verwijderd.',
		'warning': 'Waarschuwing',
		'error': 'Fout',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Geen formulier geselecteerd",
        'form_customized': "Formulier aangepast",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Selecteren",
        'btn_use': "Gebruiken",
        'master_password_for_spasswords': "Om wachtwoorden op te slaan en te gebruiken, moet u eerst een hoofdwachtwoord instellen.\n\nWilt u nu het hoofdwachtwoord instellen?",
        'open_saved_dialog_title': "Opgeslagen bestand openen",
        'open_saved_question': "Wilt u het opgeslagen bestand nu openen?",
        'password': "Wachtwoord",
        'password_manager_master_required': "De wachtwoordbeheerder is alleen beschikbaar als er een hoofdwachtwoord is ingesteld.\n\nWilt u nu het hoofdwachtwoord instellen?",
        'password_master_required_for_select': "Om opgeslagen wachtwoorden weer te geven en te selecteren, moet u zich eerst authenticeren met uw hoofdwachtwoord.\n\nWilt u zich nu authenticeren?",
        'password_not_available': "Het geselecteerde wachtwoord is niet beschikbaar of kon niet worden ontsleuteld.",
        'password_options_title': "Wachtwoordopties",
        'password_save_choice_change': "Nieuw wachtwoord instellen",
        'password_save_choice_keep': "Bestaand wachtwoord gebruiken",
        'password_save_choice_none': "Ong Versleuteld opslaan",
        'password_save_hint': "Stel eerst een hoofdwachtwoord in om wachtwoorden veilig op te slaan.",
        'password_save_master_required': "Wachtwoord opslaan (alleen mogelijk met hoofdwachtwoord)",
        'password_save_question': "De huidige PDF is beveiligd met een wachtwoord. Wilt u het bestaande wachtwoord gebruiken, een nieuw instellen of onversleuteld opslaan?",
        'password_select': "Selecteer wachtwoord",
        'password_select_none': "Geen wachtwoord geselecteerd.\n\nSelecteer een wachtwoord uit de lijst.",
        'password_select_one': "Selecteer exact één wachtwoord.\n\nU heeft meerdere wachtwoorden gemarkeerd.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_back-up",
        'filename_insert_suffix': "_met_invoeging",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_pagina's_verwijderd",
        'filename_pages_moved': "_pagina's_verplaatst",
        'filename_rotated_all_suffix': "_alle_pagina's_gedraaid",
        'filename_rotated_suffix': "_pagina_gedraaid",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configuratie van bestandsnamen bij wijzigingen aan PDF",
        'filename_keep_suffixes': "Vorige extensies behouden (bv. _met_tekst)",
        'filename_keep_suffixes_false': "Vervangen",
        'filename_keep_suffixes_true': "Behouden",
        'filename_preview_label': "Voorbeeld van bestandsnaam:",
        'filename_preview_overwrite_hint': "Voorbeeld niet beschikbaar – het origineel wordt overschreven.",
        'filename_separator': "Scheidingsteken tussen woorden",
        'filename_separator_none': "Geen scheidingsteken",
        'filename_separator_space': "Spatie ( )",
        'filename_separator_underscore': "Onderscore (_)",
        'filename_settings_saved': "Bestandsnaam instellingen opgeslagen",
        'filename_settings_title': "Bestandsnaamopmaak en back-up",
        'filename_timestamp_position': "Positie van de tijdstempel",
        'filename_timestamp_position_after': "Na de basisnaam",
        'filename_timestamp_position_before': "Helemaal vooraan",
        'filename_timestamp_position_end': "Aan het einde",
        'filename_use_timestamp': "Tijdstempel gebruiken",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Gedrag bij wijzigingen:</b><ul><li>Pagina's verwijderen en invoegen</li><li>Tekst, handtekening, afbeelding en vormen invoegen</li><li>OCR</li></ul></html>",
        'backup_section': "Back-up voor paginabewerkingen (Verwijderen, Verplaatsen)",
        'behavior_info': "Opmerking: Bij 'Origineel overschrijven' worden tijdstempels en achtervoegsels genegeerd – het bestand behoudt zijn naam.",
        'behavior_new_file': "Altijd nieuw bestand aanmaken (met tijdstempel en achtervoegsel)",
        'behavior_overwrite': "Origineel overschrijven (geen nieuw bestand)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Alle pagina's zijn gedraaid.\n\nHet origineel bleef ongewijzigd.\nNieuw bestand: {0}",
        'all_pages_rotated_voice': "Alle pagina's gedraaid, nieuw bestand aangemaakt.",
        'empty_pages_deleted_new_file': "{0} lege pagina's zijn verwijderd.\n\nHet origineel bleef ongewijzigd.\nNieuw bestand: {1}",
        'empty_pages_deleted_voice': "{0} lege pagina's verwijderd, nieuw bestand aangemaakt.",
        'ocr_keep_original': "Origineel behouden (later handmatig openen)",
        'ocr_new_file_question': "De nieuwe doorzoekbare PDF is opgeslagen onder:\n{0}\n\nWilt u deze nu openen?",
        'ocr_open_new': "Nieuw OCR-bestand openen",
        'ocr_original_kept': "Het originele bestand blijft open. Het OCR-bestand is opgeslagen.",
        'page_deleted_new_file': "Pagina {0} is verwijderd.\n\nHet origineel bleef ongewijzigd.\nNieuw bestand: {1}",
        'page_deleted_voice': "Pagina {0} verwijderd, nieuw bestand aangemaakt.",
        'page_rotated_new_file': "Pagina {0} is gedraaid.\n\nHet origineel bleef ongewijzigd.\nNieuw bestand: {1}",
        'page_rotated_voice': "Pagina {0} gedraaid, nieuw bestand aangemaakt.",
        'pages_deleted_new_file': "Er zijn {0} pagina's verwijderd.\n\nHet originele bestand bleef ongewijzigd.\nNieuw bestand: {1}",
        'pages_deleted_new_file_voice': "{0} pagina's verwijderd, nieuw bestand aangemaakt.",
        'pages_inserted_new_file': "Er zijn {0} pagina's ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nNieuw bestand: {1}",
        'pages_inserted_new_file_ask': "Er zijn {0} pagina's ingevoegd.\n\nHet origineel bleef ongewijzigd.\nNieuw bestand: {1}\n\nWilt u deze nu openen?",
        'pages_inserted_voice_new': "{0} pagina's ingevoegd, nieuw bestand aangemaakt.",
        'pages_moved_new_file': "Er zijn {0} pagina's verplaatst.\n\nHet originele bestand bleef ongewijzigd.\nNieuw bestand: {1}",
        'pages_moved_new_file_voice': "{0} pagina's verplaatst, nieuw bestand aangemaakt.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Niet meer tonen",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Back-upinstelling</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Back-up AAN</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Bij alle wijzigingen die het origineel overschrijven</strong> (tekst, handtekening, afbeelding, vorm, OCR, draaien, invoegen, pagina's verwijderen/verplaatsen) wordt <strong>automatisch een back-up met tijdstempel</strong> aangemaakt voordat de wijziging wordt toegepast.</p>
                <p style="margin: 5px 0 5px 20px;">• De back-up bevindt zich naast het originele bestand (bv. <code>Document_back-up_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Als u daarnaast de optie <strong>„Origineel overschrijven“</strong> hebt geactiveerd, wordt ook een back-up gemaakt.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Back-up UIT</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Er wordt geen back-up gemaakt</strong> – noch bij overschrijven, noch bij paginabewerkingen.</p>
                <p style="margin: 5px 0 5px 20px;">• Het originele bestand kan onherroepelijk verloren gaan bij overschrijven.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Alleen aanbevolen voor ervaren gebruikers!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> De back-upinstelling is onafhankelijk van de optie „Origineel overschrijven“. U kunt beide combineren.<br>
                U kunt dit bericht permanent verbergen.
            </div>
        </div>
        """,
        'backup_info_title': "Back-upgedrag",
        'backup_info_voice': "Melding over het back-upgedrag bij paginabewerkingen. Back-up aan overschrijft origineel, back-up uit maakt nieuw bestand.",
        'show_backup_info': "Info over back-upinstelling",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Niet meer tonen",
        'overwrite_enable_backup': "Back-up inschakelen (aanbevolen)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Origineel overschrijven</p>
            <p>Als u deze optie inschakelt, worden wijzigingen (tekst, handtekening, afbeelding, vorm, OCR, draaien, invoegen) <strong>direct in het origineel opgeslagen</strong> – <strong>er wordt geen nieuw bestand aangemaakt</strong>.</p>
            <p>• De bestandsnaam blijft ongewijzigd.<br>
            • Tijdstempels en achtervoegsels worden genegeerd.<br>
            • <strong>Zonder back-up kan het origineel onherroepelijk verloren gaan.</strong></p>
            <p style="color: #FFD700;">Aanbeveling: Schakel daarnaast de back-upoptie in om automatische veiligheidskopieën te krijgen.</p>
        </div>
        """,
        'overwrite_info_title': "Origineel overschrijven",
        'overwrite_info_voice': "Waarschuwing: Origineel overschrijven – geen nieuw bestand. Back-up aanbevolen.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Er zijn {0} pagina's ingevoegd.\n\nHet originele bestand werd overschreven.\nEr is een back-up gemaakt.",
        'pages_inserted_overwrite_no_backup': "Er zijn {0} pagina's ingevoegd.\n\nHet originele bestand werd overschreven.\nEr is GEEN back-up gemaakt.",
        'texts_saved_overwrite_with_backup': "De wijzigingen zijn opgeslagen in het origineel.\n\nEr is een back-up gemaakt.",
        'texts_saved_overwrite_no_backup': "De wijzigingen zijn opgeslagen in het origineel.\n\nEr is GEEN back-up gemaakt.",
        'texts_crosses_saved_new_file': "{0} {1} en {2} {3} zijn ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nEr is een nieuw bestand aangemaakt.\n\nDe nieuwe PDF wordt geladen...",
        'texts_saved_new_file': "{0} {1} zijn ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nEr is een nieuw bestand aangemaakt.\n\nDe nieuwe PDF wordt geladen...",
        'crosses_saved_new_file': "{0} {1} zijn ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nEr is een nieuw bestand aangemaakt.\n\nDe nieuwe PDF wordt geladen...",
        'elements_saved_new_file': "{0} elementen zijn ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nEr is een nieuw bestand aangemaakt.\n\nDe nieuwe PDF wordt geladen...",
        'signatures_saved_overwrite_with_backup': "De handtekening(en) is/zijn opgeslagen in het origineel.\n\nEr is een back-up gemaakt.",
        'signatures_saved_overwrite_no_backup': "De handtekening(en) is/zijn opgeslagen in het origineel.\n\nEr is GEEN back-up gemaakt.",
        'images_saved_overwrite_with_backup': "De afbeelding(en) is/zijn opgeslagen in het origineel.\n\nEr is een back-up gemaakt.",
        'images_saved_overwrite_no_backup': "De afbeelding(en) is/zijn opgeslagen in het origineel.\n\nEr is GEEN back-up gemaakt.",
        'forms_saved_overwrite_with_backup': "De vorm(en) is/zijn opgeslagen in het origineel.\n\nEr is een back-up gemaakt.",
        'forms_saved_overwrite_no_backup': "De vorm(en) is/zijn opgeslagen in het origineel.\n\nEr is GEEN back-up gemaakt.",
        'signatures_saved_new_file': "{0} handtekening(en) zijn ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nEr is een nieuw bestand aangemaakt.\n\nDe nieuwe PDF wordt geladen...",
        'images_saved_new_file': "{0} afbeelding(en) zijn ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nEr is een nieuw bestand aangemaakt.\n\nDe nieuwe PDF wordt geladen...",
        'forms_saved_new_file': "{0} vorm(en) zijn ingevoegd.\n\nHet originele bestand bleef ongewijzigd.\nEr is een nieuw bestand aangemaakt.\n\nDe nieuwe PDF wordt geladen...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Waarschuwing: Deze PDF bevat gedraaide pagina's. De positionering kan afwijken.",
        'page_rotated_warning_title': "Gedraaide pagina gedetecteerd",
        'page_rotated_warning_message': "De huidige pagina {0} is {1}° gedraaid.\n\nHet invoegen van elementen op gedraaide pagina's wordt niet ondersteund.\n\nWilt u de pagina nu naar de rechtopstaande positie draaien?",
        'page_rotated_warning_voice': "Waarschuwing: De pagina is gedraaid. Draai deze eerst.",
        'paste_on_rotated_page_simple_warning': "Invoegen op pagina {0} niet mogelijk!\n\nDeze pagina is {1}° gedraaid.\n\nDraai de pagina eerst naar 0° (Menu: Bewerken → Pagina uitlijnen).\n\nWaarschuwing:\nHet eerder gekopieerde element gaat verloren als u niet opslaat voordat u de pagina draait.",
        'paste_on_rotated_page_voice': "Invoegen geannuleerd. Pagina is gedraaid. Lijn de pagina eerst uit.",
        'page_rotated_cancel': "Annuleren",
        'page_rotated_rotate_until_upright': "Pagina herhaaldelijk draaien (tot rechtop)",
        'page_rotated_now_upright': "De pagina staat nu rechtop. U kunt nu invoegen.",
        'page_rotated_still_not_upright': "De pagina kon niet naar de rechtopstaande positie worden gedraaid. Corrigeer handmatig.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hulp: Gedraaide pagina's corrigeren",
        'help_rotated_pages_voice': "Hulp voor het corrigeren van gedraaide pagina's wordt geopend.",
        'btn_help': "Hulp",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Probleem: Gedraaide pagina – Invoegen werkt niet correct</p>

            <p>Als het invoegen van teksten, handtekeningen of vormen op een gedraaide pagina niet correct werkt, kunt u de pagina corrigeren met een externe PDF-editor.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Oplossing met extern hulpmiddel (bv. macOS Voorvertoning)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Pagina exporteren</strong><br>
                &nbsp;&nbsp;Klik in het menu op <strong>Bestand → Exporteren als pagina's</strong> of gebruik een andere methode om de gewenste pagina als afzonderlijke PDF op te slaan.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Pagina openen in extern programma</strong><br>
                &nbsp;&nbsp;Open de geëxporteerde PDF in een PDF-editor (bv. <strong>macOS Voorvertoning</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Pagina draaien</strong><br>
                &nbsp;&nbsp;Draai de pagina zodat deze rechtop staat (in Voorvertoning: <strong>Gereedschap → Draai</strong> of <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Opslaan</strong><br>
                &nbsp;&nbsp;Sla de gecorrigeerde pagina op (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Pagina opnieuw invoegen in het originele document</strong><br>
                &nbsp;&nbsp;Ga terug naar PDFDarkView en voeg de gecorrigeerde pagina op de gewenste positie in:<br>
                &nbsp;&nbsp;<strong>Bewerken → Pagina's invoegen</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatief: Pagina in het origineel draaien</p>
                <p style="margin: 5px 0 5px 20px;">• Gebruik de ingebouwde draaifunctie (<strong>Bewerken → Pagina draaien</strong>) om de pagina stap voor stap te corrigeren.<br>
                • Na elke draai kunt u controleren of het invoegen nu werkt.<br>
                • Dit is vaak de snellere oplossing – probeer dit eerst!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Als u vaak tegen gedraaide pagina's aanloopt, kunt u de waarschuwing in het invoegdialoogvenster permanent verbergen.<br>
                De positionering kan dan afwijken – gebruik deze optie alleen als u de gevolgen kent.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Pagina's uitlijnen",
        'menu_rotate_normalize_tooltip': "Pagina draaien of resetten naar 0°",
        'normalize_current_page': "Huidige pagina in rechtopstaande positie brengen (instellen op 0°)",
        'normalize_all_pages': "Alle pagina's in rechtopstaande positie brengen (instellen op 0°)",
        'page_normalized': "Pagina {0} is in rechtopstaande positie gebracht.",
        'all_pages_normalized': "Alle pagina's zijn in rechtopstaande positie gebracht.",
        'page_already_upright': "Pagina {0} staat al rechtop.",
        'all_pages_already_upright': "Alle pagina's staan al rechtop.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>De PDF bevat geen doorzoekbare tekst.</p><p>Wilt u OCR uitvoeren om naar {0} te exporteren?</p>",
        'export_ocr_voice': "De PDF bevat geen tekst. OCR vereist voor export naar {0}.",
        'export_no_ocr_possible': "Exporteren zonder OCR niet mogelijk. Voer OCR uit via het menu.",
        'ocr_failed_export_not_possible': "OCR mislukt. Exporteren kan niet worden uitgevoerd.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF wordt geopend in Voorvertoning. Start daar het afdrukproces.",
        'print_preview_manual': "PDF is geopend. Voer de afdrukopdracht handmatig uit (bv. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDF's samenvoegen",
        'merge_pdfs': "PDF's samenvoegen",
        'merge_progress_title': "PDF's worden samengevoegd...",
        'merge_pdfs_list': "PDF's in volgorde (Sleep en sorteer)",
        'merge_add_pdf': "PDF toevoegen",
        'merge_remove': "Verwijderen",
        'merge_move_up': "Omhoog",
        'merge_move_down': "Omlaag",
        'merge_pdfs_info': "💡 Tip: U kunt de volgorde wijzigen door te slepen",
        'merge_no_pdfs': "Geen PDF's geselecteerd. Klik op 'PDF toevoegen'.",
        'merge_info': "{0} PDF's geselecteerd (ongeveer {1} pagina's)",
        'merge_open_file': "Bestand openen",
        'merge_merge': "Samenvoegen",
        'merge_error': "Fout bij samenvoegen",
        'merge_min_two_pdfs_error': "Selecteer ten minste twee PDF-bestanden om samen te voegen.",
        'merge_select_pdfs': "Selecteer PDF's om samen te voegen",
        'merge_error_file': "Fout bij verwerking",
        'merge_cancelled': "Samenvoegen is geannuleerd",
        'merge_preparing': "Voorbereiden...",
        'merge_processing': "Verwerken PDF {0} van {1}",
        'merge_saving': "Samengevoegde PDF opslaan...",
        'merge_complete': "Klaar!",
        'merge_success_title': "Samenvoegen geslaagd",
        'merge_success_voice': "{0} PDF's zijn succesvol samengevoegd.",
        'merge_success_message': "{0} PDF's zijn succesvol samengevoegd.\n\nHet nieuwe document heeft nu {1} pagina's.\n\nNieuw bestand:\n{2}\n\nOpslaglocatie:\n{3}\n{2}\n\nWilt u deze PDF openen?",
        'replace_file_title': "Bestand vervangen?",
        'replace_file_message': "Er is al een PDF geopend. Wilt u deze vervangen door het nieuwe bestand?",
        'btn_yes': "Ja",
        'btn_no': "Nee",
        'filename_merge_suffix': "samengevoegd",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Openen {0}...",
        'progress_merge_reading': "Lezen {0}...",
        'progress_merge_adding': "{0} pagina's toevoegen...",
        'progress_merge_optimizing': "PDF optimaliseren...",
        'progress_merge_writing': "PDF schrijven...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "het sluiten van de PDF",
        'action_close_window': "het sluiten van het venster",
        'action_open_new_pdf': "het openen van een nieuwe PDF",
        'action_quit_app': "het afsluiten van de applicatie",
        'changes_saved': "De wijzigingen zijn opgeslagen.",
        'file_close_title': "PDF-bestand sluiten",
        'save_before_action': "Moeten de wijzigingen worden opgeslagen vóór {0}? Ja of Nee?",
        'save_before_action_voice': "Moeten de wijzigingen worden opgeslagen vóór {0}? Ja of Nee?",
        'save_before_close_question': "Moeten de wijzigingen worden opgeslagen vóór het sluiten? Ja of Nee?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Doorzoekbare PDF aangemaakt:\n\n{0}\n\n<b>probeer opnieuw indien nodig",
        "ocr_rotate_title": "Pagina's uitlijnen voor OCR",
        "ocr_rotate_question": "De PDF bevat gedraaide pagina's.\nWilt u alle pagina's voor OCR uitlijnen op 0°?\nDit verbetert de tekstherkenning aanzienlijk.",
        "ocr_rotate_yes": "Ja, uitlijnen",
        "ocr_rotate_no": "Nee, OCR direct starten",
        "ocr_rotate_voice": "De PDF bevat gedraaide pagina's. Moeten alle pagina's voor OCR worden uitgelijnd?",
        "ocr_not_performed_message": "Geen tekst aanwezig. Voer OCR uit (menu \"Bewerken\" → \"OCR uitvoeren\" of toets Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-instellingen",
        "ocr_language_btn": "OCR-taal selecteren",
        "ocr_language": "OCR-taal(pen)",
        "ocr_language_current": "Huidige taal:",
        "ocr_param_info": "Informatie over parameter",

        "ocr_force_ocr_label": "OCR afdwingen",
        "ocr_deskew_label": "Scheefstand corrigeren",
        "ocr_clean_label": "Afbeelding reinigen",
        "ocr_oversample_label": "Resolutie (DPI)",
        "ocr_pagesegmode_label": "Pagina-indeling",
        "ocr_oem_label": "OCR-engine-modus",
        "ocr_optimize_label": "PDF-compressie",
        "ocr_jobs_label": "Parallelle processen",
        "ocr_verbose_label": "Logdetail",

        "ocr_force_ocr_tooltip": "OCR op elke pagina afdwingen, zelfs als er al tekst is",
        "ocr_deskew_tooltip": "Scheve scans automatisch uitlijnen",
        "ocr_clean_tooltip": "Ruis en artefacten uit de afbeelding verwijderen",
        "ocr_oversample_tooltip": "Afbeelding voor OCR opschalen naar deze DPI",
        "ocr_pagesegmode_tooltip": "Bepaalt hoe de pagina wordt verdeeld in tekstgebieden",
        "ocr_oem_tooltip": "Selecteert de OCR-engine van Tesseract",
        "ocr_optimize_tooltip": "Compressieniveau van de uitvoer-PDF",
        "ocr_jobs_tooltip": "Aantal parallelle OCR-processen",
        "ocr_verbose_tooltip": "Detailniveau van de loguitvoer",
        "ocr_settings_explain_btn": "Uitleg",

        "ocr_force_ocr_explain": "Dwingt tekstherkenning af op <b>elke</b> pagina, zelfs als deze al tekst bevat.\n\nAanbeveling: <b>Aan</b> voor gescande PDF's, <b>Uit</b> voor native PDF's met reeds bestaande tekst.",

        "ocr_deskew_explain": "Corrigeert licht scheve scans (tot ongeveer 5°).\n\nAanbeveling: <b>Aan</b> voor gescande documenten, <b>Uit</b> als pagina's al perfect recht zijn.",

        "ocr_clean_explain": "Verwijdert ruis, puntjes en kleine artefacten uit de afbeelding.\n<b>BELANGRIJK:</b> Voor Arabische, Thaise of Vietnamese teksten met diakritische tekens (punten boven/onder letters) moet deze optie <b>uitgeschakeld</b> worden, anders kunnen belangrijke karakters verloren gaan.",

        "ocr_oversample_explain": "Schaalt de afbeelding <b>voor</b> tekstherkenning op naar de opgegeven DPI.<br><br>• <b>72-150 DPI:</b> Zeer snel, maar lage herkenningsgraad<br>• <b>200-300 DPI:</b> Optimaal bereik (Standaard: 300)<br>• <b>400+ DPI:</b> Nauwelijks betere herkenning, maar aanzienlijk grotere bestanden<br><br>Aanbeveling: 300 DPI voor complexe schriften (Arabisch, Chinees, Japans), 200 DPI voor westerse talen.",

        "ocr_pagesegmode_explain": "Bepaalt hoe Tesseract de pagina verdeelt in tekstgebieden.\n\n• <b>3 - Automatisch (Standaard):</b> Goed voor gemengde lay-outs\n• <b>4 - Enkele kolom:</b> Voor teksten met één kolom\n• <b>5 - Verticaal blok:</b> Voor verticale schriften (Japans, Chinees)\n• <b>6 - Uniform tekstblok:</b> Optimaal voor doorlopende tekst zonder kolommen\n• <b>11 - Ruw beeld:</b> Voor slechte scans / handschrift\n\nAanbeveling: <b>6</b> voor eenvoudige tekstdocumenten, <b>3</b> voor complexe lay-outs.",

        "ocr_oem_explain": "Selecteert de OCR-engine van Tesseract.\n\n• <b>0 - Legacy:</b> Oude engine (snel, maar minder nauwkeurig)\n• <b>1 - LSTM:</b> Neurale engine (langzamer, maar nauwkeuriger)\n• <b>2 - Legacy + LSTM:</b> Combineert beide resultaten\n• <b>3 - Standaard (LSTM heeft voorkeur):</b> Beste keuze voor de meeste gevallen\n\nAanbeveling: <b>3</b> voor maximale herkenningsnauwkeurigheid.",

        "ocr_optimize_explain": "Compresseert de uitvoer-PDF.\n\n• <b>0:</b> Geen optimalisatie (snelste verwerking)\n• <b>1:</b> Lichte optimalisatie (goed compromis)\n• <b>2:</b> Matige optimalisatie\n• <b>3:</b> Sterke optimalisatie (kleinste bestand, maar langzamer)\n\nAanbeveling: <b>1</b> voor dagelijks gebruik.",

        "ocr_jobs_explain": "Aantal parallelle processen voor OCR.\n\n• <b>1:</b> Langzaam, maar laagste geheugenverbruik\n• <b>4-8:</b> Optimaal voor moderne multi-core processors\n• <b>12+:</b> Nauwelijks snellere verwerking bij hoog geheugenverbruik\n\nAanbeveling: Aantal CPU-kernen (bv. <b>4</b> op 4-kern systemen).",

        "ocr_verbose_explain": "Detailniveau van de loguitvoer in de console.\n\n• <b>0:</b> Geen uitvoer\n• <b>1:</b> Voortgang en statusberichten\n• <b>2:</b> Gedetailleerde uitvoer\n• <b>3:</b> Volledige debug-uitvoer (zeer uitgebreid)\n\nAanbeveling: <b>1</b> voor normaal gebruik.",

        "ocr_reset_title": "Instellingen gereset",
        "ocr_reset_message": "Alle OCR-instellingen zijn teruggezet naar de standaardwaarden.",
        "info_tooltip": "Meer informatie over deze parameter",
        "ocr_reset_defaults": "Terugzetten naar standaard",

        "ocr_psm_0": "Automatisch (Legacy-engine)",
        "ocr_psm_1": "Automatische kolom detectie",
        "ocr_psm_3": "Automatisch (Standaard)",
        "ocr_psm_4": "Enkele kolom",
        "ocr_psm_5": "Verticaal blok",
        "ocr_psm_6": "Uniform tekstblok",
        "ocr_psm_7": "Enkele tekstregel",
        "ocr_psm_8": "Enkel woord",
        "ocr_psm_11": "Ruw beeld (geen lay-outanalyse)",

        "ocr_oem_0": "Legacy-engine (snel)",
        "ocr_oem_1": "LSTM-engine (neuraal, nauwkeurig)",
        "ocr_oem_2": "Legacy + LSTM gecombineerd",
        "ocr_oem_3": "Standaard (LSTM heeft voorkeur)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-taal(pen)...",
        "ocr_language_title": "OCR-taal(pen) selecteren",
        "ocr_language_instruction": "Selecteer de taal(pen) voor tekstherkenning (OCR).\nLet op: Meerdere talen gaan ten koste van prestaties en nauwkeurigheid!\nU behaalt de beste resultaten als u slechts één taal selecteert.",
        "ocr_language_predefined": "Voorgedefinieerde combinaties",
        "ocr_language_custom": "Aangepast...",
        "ocr_language_selected": "Geselecteerde OCR-talen",
        "ocr_language_changed": "OCR-taal gewijzigd naar {0}",
        "ocr_language_auto_detect": "Beschikbare talen worden automatisch gedetecteerd.",
        "ocr_language_none_found": "Geen Tesseract-taalgegevens gevonden! Installeer taalpakketten (bv. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Aangepaste taalselectie",
        "ocr_language_available": "Beschikbare talen (geïnstalleerd):",
        "ocr_language_select_hint": "Selecteer één of meer talen:",
        "ocr_language_confirm": "Toepassen",
        "ocr_language_reset": "Terugzetten naar standaard (deu+eng+vie)",
        "ocr_language_priorities": "Aanbevolen talen (vooraf geïnstalleerd):",

        "select_all_languages": "Alles selecteren",
        "clear_all_languages": "Selectie wissen",
        "install_language_packs": "Ontbrekende taalpakketten installeren...",
        "install_hint": "💡 Tip: Niet alle talen zijn op uw systeem geïnstalleerd. Via deze knop krijgt u hulp bij installatie.",
        "ocr_language_install_title": "Installatie van Tesseract-taalpakketten",

        "ocr_missing_languages": "Ontbrekende OCR-taalpakketten",
        "ocr_missing_languages_message": "De volgende geselecteerde talen zijn niet geïnstalleerd op uw systeem:\n\n{0}\n\nInstalleer de ontbrekende taalpakketten (zie hulp onder 'Installatiehulp').\n\nWilt u de installatiehulp nu openen?",
        "ocr_missing_languages_voice": "Ontbrekende taalpakketten. Installeer de ontbrekende talen.",
        "ocr_install_help_now": "Hulp openen",
        "ocr_continue_anyway": "Toch proberen",
        "ocr_language_error_title": "OCR-taal fout",
        "ocr_language_error_message": "Fout tijdens tekstherkenning: {0}\n\nControleer uw OCR-taalinstellingen (Instellingen → OCR-taal).",
        "ocr_install_help_button": "Installatiehulp",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract-taalpakketten installeren</p>

        <p>Om OCR in een specifieke taal te laten werken, moeten de bijbehorende taalgegevens op uw systeem zijn geïnstalleerd. Volg de instructies voor uw besturingssysteem:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Open de <strong>Terminal</strong> (Finder → Programma's → Hulpprogramma's → Terminal).</li>
        <li>Installeer alle beschikbare talen met:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Dit kan enkele minuten duren.)</li>
        <li>Of alleen individuele talen (bv. Vietnamees):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Bij huidige Homebrew-versies moet <code>*.traineddata</code> mogelijk handmatig worden gedownload (zie hieronder).</li>
        <li>Na installatie: Sluit dit dialoogvenster en open de OCR-taalselectie opnieuw – de nieuwe talen verschijnen automatisch.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Open een terminal (Ctrl+Alt+T).</li>
        <li>Installeer de gewenste taal, bv. voor Vietnamees:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Belangrijke taal codes: <code>deu</code> (Duits), <code>eng</code> (Engels), <code>vie</code> (Vietnamees), <code>spa</code> (Spaans), <code>fra</code> (Frans), <code>ita</code> (Italiaans), <code>nld</code> (Nederlands), <code>fin</code> (Fins), <code>swe</code> (Zweeds), <code>nor</code> (Noors).</li>
        <li>Toon alle beschikbare pakketten:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (handmatig)</p>
        <ol>
        <li>Download de gewenste <code>*.traineddata</code>-bestanden van:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (bv. <code>vie.traineddata</code> voor Vietnamees).</li>
        <li>Kopieer de bestanden naar de Tesseract-taalmap, meestal:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Pas aan bij individuele installatie.)</li>
        <li>Herstart de applicatie (of open de OCR-taalselectie opnieuw).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatief voor alle systemen</p>
        <ul>
        <li>Installeer <strong>OCRmyPDF</strong> en <strong>Tesseract</strong> met een pakketbeheerder naar keuze. De meeste installaties bevatten al enkele standaard talen (Engels, Duits, Frans).</li>
        <li>Ontbrekende talen kunnen op elk gewenst moment worden geïnstalleerd – de OCR-taalselectie toont alleen de daadwerkelijk bestaande talen.</li>
        </ul>

        <hr>
        <p><b>✅ Na installatie:</b> Herstart van de applicatie is niet nodig – de nieuw toegevoegde talen verschijnen onmiddellijk in de lijst.</p>
        <p><b>📖 Hulp bij taal codes:</b> Een volledige lijst is beschikbaar in de <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract-documentatie</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans-lettertypen",
        "info_noto_font_voice": "Handleiding voor installatie van Noto Sans-lettertypen",
        "btn_info_noto_font_install": "Lettertype-info",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ De gratis Noto-lettertypen van Google installeren</h2>

        <p>De <strong>Noto-lettertypen</strong> zijn een open-source lettertypefamilie van Google. Hun doel is om <em>"geen tofu"</em> (d.w.z. geen lege vakjes □) te zien en elk teken uit de Unicode-standaard correct weer te geven. Ze zijn de ideale aanvulling voor toepassingen die teksten in vele verschillende talen moeten weergeven.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installatie op macOS</h3>

        <p><strong>Methode 1: Met Homebrew (voor gevorderden)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Methode 2: Via "Font Book" (Aanbevolen)</strong></p>

        <ol>
        <li>Download het officiële lettertypepakket:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pak het ZIP-bestand uit</li>
        <li>Kopieer bestanden naar <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installatie op Windows (10 & 11)</h3>

        <p><strong>Methode 1: Microsoft Store (Aanbevolen)</strong><br>
        Zoek naar "Google Noto Fonts" of "Noto Sans" en klik op <strong>Installeren</strong>.</p>

        <p><strong>Methode 2: Handmatige installatie</strong></p>

        <ol>
        <li>Download:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pak ZIP uit</li>
        <li>Selecteer .ttf / .otf bestanden</li>
        <li>Rechtsklik → <strong>Installeren</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        of<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Naam\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installatie op Linux</h3>

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

        <p>Verificatie:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Bladwijzers beheren",
        "bookmark_add": "Bladwijzer toevoegen",
        "bookmark_add_tooltip": "Huidige pagina opslaan als bladwijzer",
        "bookmark_remove": "Bladwijzer verwijderen",
        "bookmark_remove_tooltip": "De gemarkeerde bladwijzer verwijderen",
        "bookmark_remove_all": "Alles verwijderen",
        "bookmark_remove_all_tooltip": "Alle bladwijzers van deze PDF verwijderen",
        "bookmark_jump": "Naar bladwijzer gaan",
        "bookmark_jump_tooltip": "Naar geselecteerde pagina gaan",
        "bookmark_name": "Naam",
        "bookmark_page": "Pagina",
        "bookmark_no_bookmarks": "Geen bladwijzers aanwezig.\nKlik op 'Toevoegen' om de huidige pagina als bladwijzer op te slaan.",
        "bookmark_added": "Bladwijzer voor pagina {0} toegevoegd: {1}",
        "bookmark_removed": "Bladwijzer verwijderd: {0}",
        "bookmark_all_removed": "Alle bladwijzers zijn verwijderd.",
        "bookmark_name_default": "Pagina {0}",
        "bookmark_name_prompt": "Naam voor de bladwijzer:\n(lange tekst wordt ingekort tot 50 tekens)",
        "bookmark_name_prompt_title": "Bladwijzernaam",
        "bookmark_confirm_remove_all": "Weet u zeker dat u alle {0} bladwijzers wilt verwijderen?",
        "menu_bookmarks": "Bladwijzers",
        "bookmark_manage": "Bladwijzers beheren",
        "bookmark_next": "Volgende bladwijzer",
        "bookmark_prev": "Vorige bladwijzer",
        "bookmark_page_display": "Pagina {0}",
        "bookmark_exists": "Er bestaat al een bladwijzer voor deze pagina met deze naam.",
        "bookmark_select_first": "Selecteer eerst een bladwijzer.",
        "bookmark_confirm_remove": "Weet u zeker dat u de bladwijzer 'Pagina {0}: {1}' wilt verwijderen?",
        "bookmark_jumped_to": "Naar bladwijzer '{0}' op pagina {1} gegaan.",
        "bookmark_jumped_to_voice": "Bladwijzer {0}, pagina {1}",
        "btn_close": "Sluiten",

        "bookmark_list": "Uw bladwijzers",
        "bookmark_rename": "Bladwijzer hernoemen",
        "bookmark_rename_tooltip": "De naam van de geselecteerde bladwijzer wijzigen",
        "bookmark_rename_title": "Bladwijzer hernoemen",
        "bookmark_rename_prompt": "Nieuwe naam voor bladwijzer op pagina {0}:\n(max. 50 tekens)",
        "bookmark_renamed": "Bladwijzer '{0}' is hernoemd naar '{1}'.",
        "bookmark_item_tooltip": "Pagina {0}: {1}\nDubbelklik om te gaan",
        "bookmark_name_exists_question": "Er bestaat al een bladwijzer met de naam '{0}' op deze pagina.\nToch hernoemen?",

        "context_bookmarks": "Bladwijzers",
        "context_bookmark_add_here": "Bladwijzer voor deze pagina toevoegen",
        "context_bookmarks_existing": "Bestaande bladwijzers:",
        "context_bookmarks_jump": "Naar bladwijzer gaan:",
        "context_bookmarks_none": "Geen bladwijzers aanwezig",
        "context_bookmarks_clear_all": "Alle {0} bladwijzers verwijderen",

        "bookmark_search_placeholder": "Bladwijzers zoeken... (naam of pagina)",
        "bookmark_search_results": "%d bladwijzers gevonden voor \"%s\"",
        "bookmark_no_search_results": "Geen bladwijzers gevonden voor \"%s\"",
        "bookmark_no_search_results_label": "Geen resultaten voor \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF-metadata bewerken",
        "metadata_title": "Titel",
        "metadata_title_placeholder": "Documenttitel",
        "metadata_title_tooltip": "De titel van het document (wordt weergegeven in de titelbalk)",
        "metadata_author": "Auteur",
        "metadata_author_placeholder": "Naam van de auteur",
        "metadata_author_tooltip": "De maker van het document",
        "metadata_subject": "Onderwerp",
        "metadata_subject_placeholder": "Onderwerp van het document",
        "metadata_subject_tooltip": "Een korte beschrijving van de inhoud",
        "metadata_keywords": "Trefwoorden",
        "metadata_keywords_placeholder": "Trefwoorden, gescheiden door komma's",
        "metadata_keywords_tooltip": "Trefwoorden voor het categoriseren van het document",
        "metadata_creator": "Maker",
        "metadata_creator_placeholder": "Applicatie die de PDF heeft gemaakt",
        "metadata_creator_tooltip": "De software waarmee het document is gemaakt",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Applicatie die de PDF heeft geconverteerd",
        "metadata_producer_tooltip": "De software die de PDF heeft geconverteerd",
        "metadata_creation_date": "Aanmaakdatum",
        "metadata_creation_date_tooltip": "De datum van het aanmaken van het document",
        "metadata_mod_date": "Wijzigingsdatum",
        "metadata_mod_date_tooltip": "De datum van de laatste wijziging",
        "metadata_pdf_info": "📄 PDF-informatie",
        "metadata_pages": "Aantal pagina's",
        "metadata_file_size": "Bestandsgrootte",
        "metadata_pdf_version": "PDF-versie",
        "metadata_encrypted": "Versleuteld",
        "metadata_encrypted_yes": "Ja (wachtwoordbeveiligd)",
        "metadata_encrypted_no": "Nee",
        "metadata_reload": "📂 Herladen vanuit PDF",
        "metadata_reset": "Wijzigingen verwerpen",
        "metadata_reloaded": "Metadata zijn herladen vanuit de PDF.",
        "metadata_reset_done": "Alle metadatavelden zijn gereset.",
        "metadata_no_file": "Geen PDF-bestand geladen.",
        "metadata_save_error": "Fout bij opslaan van metadata",
        "metadata_saved": "Metadata zijn succesvol opgeslagen.",
        "metadata_pdf_version_unknown": "PDF (onbekend)",
        "metadata_saved_message": "De metadata zijn succesvol opgeslagen.",
        "metadata_saved_voice": "Metadata opgeslagen.",

        "metadata_custom": "🔧 Aangepaste metadata",
        "metadata_custom_placeholder": "{\n  \"mijn_veld\": \"mijn_waarde\",\n  \"ander_veld\": 123\n}",
        "metadata_custom_tooltip": "JSON-formaat voor aangepaste metadata (optioneel)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Sjabloon \"{0}\" geselecteerd - Dubbelklik om in te voegen",
        "text_use_template": "Tekstblok gebruiken",
        "text_type": "Type",
        "text_search_templates": "Tekstblokken zoeken...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Export / Import informatie",
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

        <h3>📦 Wat wordt er geëxporteerd? (Overzicht)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Algemene applicatie-instellingen</span></li>
            <li class="detail">• Donker/Licht-modus</li>
            <li class="detail">• Donkermodus inversie voor afbeeldingen</li>
            <li class="detail">• Grijze drempelwaarde</li>
            <li class="detail">• Taal</li>
            <li class="detail">• Venstergeometrie</li>
            <li class="detail">• Zoom-modus</li>
            <li class="detail">• Navigatie (Navbalk zichtbaar)</li>
            <li class="detail">• Spraakuitvoer (aan/uit)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Back-up instellingen</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bestandsnaamgeving (Tijdstempel, Scheidingsteken, Achtervoegsels)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Instellingen voor invoegingen van</span></li>
            <li class="detail">• Handtekeningen</li>
            <li class="detail">• Tekst &amp; tekstblokken</li>
            <li class="detail">• Kruisjes, afbeeldingen en vormen</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-instellingen</span></li>
            <li class="detail">• Taal</li>
            <li class="detail">• OCR afdwingen · Paginamodus</li>
            <li class="detail">• Beeldvoorbewerking: Scheefstand corrigeren, Reinigen, Overbemonstering</li>
            <li class="detail">• Aantal parallelle taken</li>
            <li class="detail">• Inversiemodus</li>
            <li class="detail">• Grijze drempelwaarde</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bladwijzers</span></li>
            <li class="detail">• Alle bladwijzers per PDF-bestand (Pagina, Naam, Aanmaaktijd)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Wachtwoorddatabase</span></li>
            <li class="detail">• Opgeslagen PDF-wachtwoorden (optioneel versleuteld of platte tekst)</li>
            <li class="detail">• Masterwachtwoord hash (indien ingesteld)</li>
            <li class="detail">• Verificatiegegevens</li>
        </ul>

        <h4>⚠️ Belangrijke opmerkingen</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Bij importeren:</strong>
            <ul>
                <li><span class="warning">➜ ALLE huidige instellingen worden volledig overschreven</span></li>
                <li>• Een herstart van de applicatie is verplicht</li>
                <li>• Bestaande handtekeningen, tekstblokken en bladwijzers worden vervangen</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Masterwachtwoord &amp; exportmodus:</strong>
            <ul>
                <li>• Bij actief masterwachtwoord kunt u kiezen:</li>
                <li>  - <span style="color: #98FB98;"><strong>Ontsleuteld</strong></span> (wachtwoorden staan in platte tekst in de ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Versleuteld</strong></span> (alleen leesbaar met masterwachtwoord op het doelsysteem)</li>
                <li>• De masterwachtwoord hash zelf wordt <strong>altijd</strong> versleuteld opgeslagen</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Beveiligingsmededeling:</strong>
            <ul>
                <li>• Het geëxporteerde ZIP-bestand bevat gevoelige gegevens (<strong>wachtwoorden, bladwijzers, handtekeningen</strong>)</li>
                <li>• Bewaar het op een veilige plaats (bv. versleutelde USB-stick, wachtwoordmanager)</li>
                <li>• Bij verlies van het bestand zijn opgeslagen PDF-wachtwoorden onherstelbaar verloren</li>
            </ul>
        </div>

        <h4>📁 Exportformaat</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            De instellingen worden opgeslagen in een enkel ZIP-bestand:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Deze ZIP bevat de volledige <code>settings.json</code> (uit uw configuratie) en eventueel ingesloten handtekeningafbeeldingsbestanden en versleutelde wachtwoorden.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Handtekeningen - Handleiding",
        'signature_guide_html': """
        📝 <strong>Handtekeningen - Beknopte handleiding</strong><br>
        <ul>
        <li>Master wachtwoord instellen</li>
        <li>Handtekeningen configureren in het menu <em>Instellingen</em> (grootte, tijdstempel, …)</li>
        <li>Invoegen met <strong>RECHTSKLIK</strong> op de gewenste positie (master wachtwoord eenmalig per sessie vereist)</li>
        <li>Handtekening verplaatsen met muis of pijltjestoetsen</li>
        <li>Meerdere handtekeningen achter elkaar invoegen</li>
        <li>Elke handtekening individueel aanpassen</li>
        <li>Enkele handtekening verwerpen</li>
        <li>Alle handtekeningen tegelijk opslaan / verwerpen</li>
        <li>Alternatief kan ook de menubalk worden gebruikt.</li>
        </ul>
        """,
        'signature_guide_voice': "Beknopte handleiding voor handtekeningen. Master wachtwoord instellen. Handtekeningen configureren in instellingen. Invoegen met rechtsklik.",

        'image_guide_title': "Afbeeldingen invoegen - Handleiding",
        'image_guide_html': """
        📷 <strong>Afbeeldingen invoegen in PDF - Beknopte handleiding</strong><br>
        <ol>
        <li>Rechtsklik op de gewenste positie</li>
        <li><em>„Afbeelding invoegen“</em> → Afbeelding selecteren</li>
        <li>Afbeelding positioneren: Slepen met muis</li>
        <li>Grootte aanpassen: Slepen aan de hoeken/randen</li>
        <li>Beeldverhouding behouden: Toets <strong>[A]</strong></li>
        <li>Verdere aanpassingen: Rechtsklik op de afbeelding</li>
        </ol>
        <p><strong>Tip:</strong> In het contextmenu kunt u de instellingen aanpassen.</p>
        """,
        'image_guide_voice': "Beknopte handleiding voor afbeeldingen. Rechtsklik, afbeelding invoegen, selecteren. Positioneren met muis, grootte aanpassen aan hoeken. Beeldverhouding met toets A.",

        'form_guide_title': "Vormen invoegen - Handleiding",
        'form_guide_html': """
        📐 <strong>Vormen invoegen in PDF - Beknopte handleiding</strong><br>
        <ol>
        <li>Vormtype selecteren (rechthoek, ellips, lijn, pijl)</li>
        <li>Klik op positie:
            <ul>
            <li>Bij rechthoek/ellips: Eén klik plaatst de vorm</li>
            <li>Bij lijn/pijl: Twee kliks voor begin- en eindpunt</li>
            </ul>
        </li>
        <li>Vorm positioneren: Slepen met muis</li>
        <li>Grootte aanpassen: Slepen aan de hoeken/randen</li>
        <li>Vorm opslaan: <strong>Enter</strong></li>
        <li>Vorm verwerpen: <strong>ESC</strong></li>
        <li>Verdere aanpassingen: Rechtsklik op de vorm</li>
        </ol>
        <p><strong>Tip:</strong> In het contextmenu kunt u de instellingen aanpassen.</p>
        """,
        'form_guide_voice': "Beknopte handleiding voor vormen. Vormtype selecteren. Bij rechthoek of ellips één keer klikken, bij lijn of pijl twee keer. Positioneren met muis, grootte aanpassen aan hoeken. Opslaan met Enter, verwerpen met Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "vorige",
        "btn_next_result": "volgende",
        "ocr_text_window": "OCR-tekstvenster",
        "bookmark_existing": "Bestaande bladwijzers",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR-vergelijking Mac - Windows",
        'ocr_method_mac_win_title': "OCR-verschillen tussen Mac en Windows",
        'ocr_method_mac_win_voice': "Mac is beter",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Verschillen tussen macOS en Windows</strong></p>

        <p><strong>macOS (aanbevolen)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resultaat:</p>
        <ul>
        <li>Een doorzoekbare PDF met ingebedde tekst die de oorspronkelijke lay-out grotendeels behoudt.</li>
        </ul>
        <p>Voordelen:</p>
        <ul>
        <li>Uitstekende kwaliteit van tekstherkenning (ook bij scheve pagina's).</li>
        <li>Behoud van vectorgraphics en lettertypen.</li>
        <li>GUI-voortgangsbalk via subproces-evaluatie.</li>
        <li>Volledige controle over alle OCR-parameters (Deskew, Clean, Oversample, optimalisatie).</li>
        <li>De tekstzoekopdracht is direct beschikbaar in het hoofdvenster (PDF-weergave).</li>
        </ul>
        <p>Nadelen:</p>
        <ul>
        <li>Vereist extra systeemtools (ocrmypdf, Ghostscript, unpaper, pngquant – inbegrepen in de App Bundle).</li>
        <li>Complexere foutafhandeling (deadlocks, time-outs).</li>
        </ul>

        <p><strong>Windows (stabiel alternatief)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>pytesseract (directe verbinding met Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resultaat:</p>
        <ul>
        <li>Een doorzoekbare PDF die visueel overeenkomt met een afbeeldings-PDF, maar doorzoekbaar is via de transparante tekst.</li>
        </ul>
        <p>Voordelen:</p>
        <ul>
        <li>Die schieten me nu even niet te binnen.</li>
        </ul>
        <p>Nadelen:</p>
        <ul>
        <li>De PDF is in wezen een afbeelding met onzichtbare tekst; de lay-out kan bij complexe documenten (kolommen, tabellen) enigszins afwijken.</li>
        <li>Geen automatische correctie van scheefstand (--deskew) of beeldreiniging (--clean).</li>
        <li>De GUI-voortgangsbalk wordt alleen grof bijgewerkt op basis van het aantal verwerkte pagina's.</li>
        <li>De OCR-snelheid is iets langzamer (omdat elke pagina afzonderlijk wordt verwerkt).</li>
        <li>De tekstzoekopdracht wordt omgeleid naar het OCR-tekstvenster.</li>
        </ul>

        <p><strong>Gemeenschappelijke kenmerken</strong></p>
        <ul>
        <li>Beide methoden genereren een doorzoekbare PDF in dezelfde map als het bronbestand.</li>
        <li>De OCR-instellingen (taal, DPI, paginasegmentatiemodus, OCR-motor-modus) kunnen via de OCRSettingsDialog worden geconfigureerd en zijn van toepassing in beide implementaties.</li>
        </ul>

        <p><strong>Aanbeveling:</strong></p>
        <ul>
        <li>macOS: De ocrmypdf-binary levert de beste resultaten – Koop een Mac en gebruik de versie (PDFDarkView voor Mac's met Apple Silicon of Intel-chip). De OCR-resultaten zijn beter dan onder Windows!</li>
        <li>Windows: Gebruik de pytesseract-oplossing. Deze is stabiel en levert voor de meeste documenten een volledig voldoende kwaliteit.</li>
        </ul>

        <p><strong>Belangrijke opmerking:</strong></p>
        <ul>
        <li>Beide versies zijn volledig geïntegreerd in de gebruikersinterface – de gebruiker merkt geen verschil.</li>
        <li>Het programma beslist automatisch welke OCR-motor wordt gebruikt op basis van het besturingssysteem.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Handtekening maken (van scan)",
        "signature_create_title": "Gescande handtekening selecteren (PDF/afbeelding)",
        "image_pdf_filter": "Afbeeldingen en PDF",
        "signature_pdf_empty": "De PDF bevat geen pagina's.",
        "signature_created_success": "Handtekening succesvol gemaakt: {0}",
        "signature_create_error": "Fout bij het maken van de handtekening:\n{0}",
        "rembg_missing": "rembg is niet geïnstalleerd.\nInstalleer: pip install rembg\nFout: {0}",
        "signature_name_title": "Bestandsnaam voor de handtekening",
        "signature_name_message": "Voer een bestandsnaam in voor de nieuwe handtekening (wordt opgeslagen als PNG met transparante achtergrond):",
        "signature_name_label": "Bestandsnaam:",
        "signature_name_voice": "Voer bestandsnaam in voor handtekening",
        "signature_processing": "Verwerking bezig...",
        "signature_creation_title": "Handtekening wordt gemaakt",
        "signature_overwrite_warning": "Het bestand '{0}' bestaat al. Overschrijven?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"PDF voorbereiden voor handtekening",
        "signature_prepare_instruction":"Selecteer een PDF die op een enkele pagina een gescande handtekening bevat.\n\nOptimale herkenning wordt bereikt als:\n• De handtekening met zwarte inkt (balpen of fineliner) op wit papier is geschreven.\n• De handtekening zich in het bovenste derde deel van een verder lege A4-pagina bevindt.\n• De PDF met minimaal 300 dpi is gescand.\n• De handtekening duidelijk en niet te dun is.\n• Geen storende achtergrondpatronen of lijnen aanwezig zijn.",
        "signature_prepare_voice":"Selecteer een PDF met een gescande handtekening. Let op goede kwaliteit en contrast.",
        "sig_thickness_label":"Lijndikte:",
        "sig_thickness_normal":"Normaal (dun)",
        "sig_thickness_bold":"Dik (aanbevolen)",
        "sig_thickness_very_bold":"Zeer dik",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI- en OCR-talen toevoegen - Handleiding",
        'language_guide_title': "GUI- en OCR-talen toevoegen",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Download het gewenste vertaalbestand <code>translations_xy.py</code> van<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        en plaats het in de volgende map:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Open uw webbrowser.</li>
        <li>Ga naar: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Zoek aan de rechterrand van het scherm naar "Releases" en selecteer degene gemarkeerd met <strong>"latest"</strong>.</li>
        <li>Download op de volgende releasepagina helemaal onderaan het bestand <code>Source Code.zip</code>.</li>
        <li>Pak het ZIP-bestand uit.</li>
        <li>Zoek in de uitgepakte map alle taalbestanden die u nodig hebt en kopieer ze naar de map:<br/>
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
        "menu_watermark":"Watermerk invoegen",
        "fullpage_text_watermark_title":"Tekst als watermerk",
        "fullpage_image_watermark_title":"Afbeelding als watermerk",
        "filename_with_watermark":"_met_watermerk",
        "watermark_text":"Tekst:",
        "watermark_text_placeholder":"Uw watermerktekst...",
        "watermark_font_family":"Lettertype:",
        "watermark_font_size":"Lettergrootte:",
        "watermark_format":"Opmaak:",
        "watermark_bold":"Vet",
        "watermark_italic":"Cursief",
        "watermark_color":"Kleur:",
        "watermark_choose_color":"Kies kleur...",
        "watermark_opacity":"Dekkracht / Transparantie:",
        "watermark_direction":"Leesrichting:",
        "watermark_direction_l_r":"Links → Rechts",
        "watermark_direction_bl_tr":"Linksonder → Rechtsboven",
        "watermark_direction_tl_br":"Linksboven → Onder",
        "watermark_direction_b_t":"Onder → Boven",
        "watermark_direction_t_b":"Boven → Onder",
        "watermark_preview":"Voorbeeld:",
        "watermark_preview_sample":"Voorbeeldtekst",
        "watermark_empty_text":"Voer een tekst in.",
        "watermark_applied":"Watermerk is op alle pagina's toegepast.",
        "watermark_saved":"Watermerk opgeslagen.",
        "image_scale":"Grootte:",
        "image_preview":"Afbeeldingsvoorbeeld:",
        "no_image_selected":"Geen afbeelding geselecteerd",
        "browse":"Bladeren...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redacties",
        "redact_add_black": "Redactie (zwart)",
        "redact_add_white": "Redactie (wit / wissen)",
        "redact_added_black": "Zwarte redactie toegevoegd",
        "redact_added_white": "Witte redactie toegevoegd",
        "redact_apply_all": "Alle redacties toepassen en opslaan",
        "redact_discard_all": "Alle redacties annuleren",
        "redact_discard": "Deze redactie annuleren",
        "no_redactions": "Geen redacties",
        "redact_confirm_title": "Redacties permanent toepassen",
        "redact_confirm_message": "Waarschuwing: Gemarkeerde gebieden worden permanent verwijderd (zwart of wit).\nEr wordt een back-up gemaakt (indien ingeschakeld).\n\nDoorgaan?",
        "redact_apply": "Ja, nu redigeren",
        "redact_saved": "{0} redactie(s) succesvol toegepast en opgeslagen.",
        "redact_saved_voice": "{0} redactie(s) toegepast",
        "redact_error": "Fout tijdens redactie",
        "filename_redacted":"_geredigeerd",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Paginanummers invoegen',
        'page_numbers_format': 'Nummernotatie:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arabisch)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Romeins klein)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Romeins groot)',
        'page_numbers_format_letter': 'A, B, C ... (Letters)',
        'page_numbers_format_custom': 'Aangepast',
        'page_numbers_custom_pattern': 'Patroon:',
        'page_numbers_custom_placeholder': 'bijv. "Pagina {nummer}" of "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Gebruik {nummer} voor het huidige paginanummer en {total} voor het totaal',
        'page_numbers_position': 'Positie:',
        'page_numbers_pos_tl': 'Linksboven',
        'page_numbers_pos_tc': 'Midden boven',
        'page_numbers_pos_tr': 'Rechtsboven',
        'page_numbers_pos_ml': 'Links midden',
        'page_numbers_pos_mc': 'Gecentreerd',
        'page_numbers_pos_mr': 'Rechts midden',
        'page_numbers_pos_bl': 'Linksonder',
        'page_numbers_pos_bc': 'Midden onder',
        'page_numbers_pos_br': 'Rechtsonder',
        'page_numbers_margins': 'Marges:',
        'page_numbers_margin_x': 'Horizontale afstand:',
        'page_numbers_margin_y': 'Verticale afstand:',
        'page_numbers_range': 'Paginabereik:',
        'page_numbers_all_pages': 'Alle pagina\'s',
        'page_numbers_custom_range': 'Aangepast bereik',
        'page_numbers_from': 'Van:',
        'page_numbers_to': 'Tot:',
        'page_numbers_progress': 'Paginanummers invoegen...',
        'page_numbers_start': 'Paginanummers invoegen starten...',
        'page_numbers_cancel': 'Paginanummers invoegen geannuleerd',
        'page_numbers_success': 'Paginanummers zijn succesvol toegevoegd.\n\nWilt u de nieuwe PDF openen?\n\n{0}',
        'page_numbers_complete': 'Paginanummers toegevoegd',
        'page_numbers_error_format': 'Fout bij het invoegen van paginanummers: {0}',
        'page_numbers_content_type': 'Inhoudstype:',
        'page_numbers_tab_simple': 'Eenvoudig nummer',
        'page_numbers_tab_range': 'Pagina X van Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Vrije tekst',
        'page_numbers_range_format': 'Formaat:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Pagina {aktuell} van {gesamt}',
        'page_numbers_range_custom': 'Aangepast',
        'page_numbers_range_placeholder': 'bijv. "Pagina {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Datumnotatie:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 januari 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Aangepast',
        'page_numbers_date_placeholder': 'bijv. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Positie:',
        'page_numbers_date_before': 'Datum vóór paginanummer',
        'page_numbers_date_after': 'Datum na paginanummer',
        'page_numbers_date_only': 'Alleen datum (zonder paginanummer)',
        'page_numbers_custom_text': 'Aangepaste tekst:',
        'page_numbers_custom_placeholder_text': 'Gebruik {seite} voor paginanummer en {gesamt} voor totaal\nbijv. "Vertrouwelijk - Pagina {seite}" of "{seite} van {gesamt}"',
        "filename_with_page_number":"_met_paginanummer",
        "filename_with_page_declaration":"_met_pagina_aanduiding",
        "filename_with_pagenumber":"_met_paginanummer",
        "filename_with_date":"_met_datum",
        "filename_with_my_page_declaration":"_met_eigen_pagina_aanduiding",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Niet-opgeslagen wijzigingen",
        "unsaved_changes_message_darkmode": "Er zijn niet-opgeslagen invoegingen.\nWilt u deze opslaan voordat u overschakelt?",
        "save_and_switch": "Opslaan en overschakelen",
        "discard_and_switch": "Nu overschakelen",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Pagina\'s als afbeeldingen exporteren',
        'export_images_menu': 'Exporteren als afbeeldingen (PNG/JPEG)',
        'export_images_format': 'Afbeeldingsformaat:',
        'export_images_dpi': 'Resolutie (DPI):',
        'export_images_quality': 'JPEG-kwaliteit:',
        'export_images_range': 'Paginabereik:',
        'export_images_all_pages': 'Alle pagina\'s',
        'export_images_custom_range': 'Aangepast bereik',
        'export_images_from': 'Van:',
        'export_images_to': 'Tot:',
        'export_images_options': 'Opties:',
        'export_images_single_files': 'Elke pagina als apart bestand',
        'export_images_subfolder': 'Exporteren naar submap',
        'export_images_subfolder_info': 'Naar submap "PDFnaam_afbeeldingen"',
        'export_images_same_folder': 'In dezelfde map als de PDF',
        'export_images_apply_darkmode': 'PDFDarkView-instellingen toepassen (Donkere modus)',
        'export_images_target_folder': 'Doelmap:',
        'export_images_browse': 'Bladeren...',
        'export_images_preview': 'Voorbeeld:',
        'export_images_preview_info': 'Selecteer instellingen voor export',
        'export_images_preview_info_detail': '{0} pagina\'s als {1}\nResolutie: {2} DPI\nBestandsnaam: {3}\n{4}',
        'export_images_select_folder': 'Selecteer doelmap',
        'export_images_start': 'Afbeeldingsexport starten...',
        'export_images_progress': 'Afbeeldingen exporteren...',
        'export_images_saving': 'Pagina {0} van {1} opslaan...',
        'export_images_success': 'Export succesvol!\n\n{0} afbeeldingen zijn opgeslagen in:\n{1}',
        'export_images_complete': 'Afbeeldingsexport voltooid',
        'export_images_open_folder': '📁 Map openen',
        'export_images_cancel': 'Afbeeldingsexport geannuleerd',
        'export_images_error_format': 'Fout bij exporteren van afbeeldingen: {0}',
        'export_images_pdf2image_missing': 'De bibliotheek "pdf2image" is niet geïnstalleerd.\n\nInstalleer deze met:\npip install pdf2image\n\nVoor Windows heeft u ook Poppler nodig:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A-conversie voor langdurige archivering',
        'pdfa_menu': 'PDF/A-conversie (archiveringsgeschikt)',
        'pdfa_info': 'Converteert de PDF naar PDF/A-formaat.\n\nPDF/A is speciaal ontwikkeld voor langdurige archivering en zorgt ervoor dat het document in de toekomst correct wordt weergegeven.',
        'pdfa_standard': 'PDF/A-standaard:',
        'pdfa_standard_select': 'Versie:',
        'pdfa_1': 'PDF/A-1 (eenvoudig, breed compatibel)',
        'pdfa_2': 'PDF/A-2 (modern, betere compressie)',
        'pdfa_3': 'PDF/A-3 (nieuwste versie, staat bijlagen toe)',
        'pdfa_standards_explanation': '📖 Uitleg over standaarden:\n\n'
            '• PDF/A-1: Basis, compatibel met oudere systemen (ca. 2005)\n'
            '• PDF/A-2: Moderner, betere compressie, transparantie-ondersteuning (ca. 2011)\n'
            '• PDF/A-3: Nieuwste versie, staat inbedding van bijlagen toe (ca. 2013)\n\n'
            'Aanbeveling: PDF/A-2 is een goed compromis tussen compatibiliteit en moderne functies.',
        'pdfa_options': 'Opties:',
        'pdfa_compress_enable': 'PDF comprimeren (kleiner bestand)',
        'pdfa_metadata_preserve': 'Metadata behouden (titel, auteur, etc.)',
        'pdfa_target_folder': 'Doelmap:',
        'pdfa_browse': 'Bladeren...',
        'pdfa_select_folder': 'Selecteer doelmap',
        'pdfa_ocr_info_unknown': '🔍 Kon tekstinhoud niet controleren.',
        'pdfa_ocr_info_not_needed': '✅ Tekst beschikbaar - OCR is niet nodig.\nPDF/A kan direct worden gemaakt.',
        'pdfa_ocr_info_recommended': '⚠️ Geen voldoende tekst gevonden.\n\nVoor doorzoekbare PDF\'s raden we aan eerst OCR uit te voeren.\nOpmerking: PDF/A werkt ook zonder OCR - maar de tekst is dan niet doorzoekbaar.',
        'pdfa_ocr_info_error': '❌ Fout bij controleren: {0}',
        'pdfa_start': 'PDF/A-conversie starten...',
        'pdfa_progress': 'PDF/A-conversie bezig...',
        'pdfa_success': 'PDF/A-conversie succesvol!\n\nOpgeslagen als:\n{0}\n\nWilt u de nieuwe PDF openen?',
        'pdfa_complete': 'PDF/A-conversie voltooid',
        'pdfa_cancel': 'PDF/A-conversie geannuleerd',
        'pdfa_error_format': 'Fout tijdens PDF/A-conversie:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'De bibliotheek "ocrmypdf" is niet geïnstalleerd.\n\nInstalleer deze met:\npip install ocrmypdf',
        'btn_convert': 'Converteren',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF optimaliseren (bestandsgrootte verkleinen)',
        'optimize_menu': 'PDF optimaliseren (bestandsgrootte)',
        'optimize_info': 'Verkleint de bestandsgrootte van de PDF via verschillende optimalisatiemethoden.\n\nHoe hoger het compressieniveau, hoe kleiner het bestand wordt - met mogelijk kwaliteitsverlies bij afbeeldingen.',
        'optimize_level': 'Compressieniveau:',
        'optimize_level_low': 'Laag (snel, kleine besparing)',
        'optimize_level_medium': 'Gemiddeld (goed compromis)',
        'optimize_level_high': 'Hoog (grote besparing)',
        'optimize_level_maximum': 'Maximum (maximale besparing, langzaam)',
        'optimize_level_explanation': 'Aanbeveling: "Gemiddeld" is een goed compromis tussen snelheid en bestandsgrootte.',
        'optimize_options': 'Opties:',
        'optimize_compress_images': 'Afbeeldingen comprimeren (JPEG-kwaliteit verlagen)',
        'optimize_clean_objects': 'Ongebruikte objecten verwijderen',
        'optimize_preserve_metadata': 'Metadata behouden (titel, auteur, etc.)',
        'optimize_image_quality': 'Afbeeldingskwaliteit:',
        'optimize_range': 'Paginabereik:',
        'optimize_all_pages': 'Alle pagina\'s',
        'optimize_custom_range': 'Aangepast bereik',
        'optimize_from': 'Van:',
        'optimize_to': 'Tot:',
        'optimize_target_folder': 'Doelmap:',
        'optimize_browse': 'Bladeren...',
        'optimize_select_folder': 'Selecteer doelmap',
        'optimize_info_box': 'Informatie',
        'optimize_info_text': 'Optimalisatie kan bij grote PDF\'s enkele minuten duren.\n\nAfbeeldingen worden met verlaagde kwaliteit opgeslagen, wat de bestandsgrootte aanzienlijk kan verkleinen.',
        'optimize_start': 'PDF-optimalisatie starten...',
        'optimize_progress': 'PDF wordt geoptimaliseerd...',
        'optimize_cancel': 'PDF-optimalisatie geannuleerd',
        'optimize_complete': 'PDF-optimalisatie voltooid',
        'optimize_error_format': 'Fout tijdens PDF-optimalisatie:\n\n{0}',
        'optimize_success_message': 'PDF-optimalisatie succesvol!\n\nOpgeslagen als:\n{0}\n\nVoorheen: {1}\nNu: {2}\nBesparing: {3:.1f}%\n\n{4}\n\nWilt u de geoptimaliseerde PDF openen?',
        'optimize_success_message_no_size': 'PDF-optimalisatie succesvol!\n\nOpgeslagen als:\n{0}\n\nGrootte-informatie niet beschikbaar.\n\nWilt u de geoptimaliseerde PDF openen?',
        'optimize_result_positive': 'Het bestand is met {0:.1f}% verkleind.',
        'optimize_result_zero': 'Geen verandering in bestandsgrootte.',
        'optimize_result_negative': 'Het bestand is met {0:.1f}% groter geworden.\nOptimalisatie overgeslagen, het originele bestand is behouden.',
        'btn_optimize': 'Optimalisatie starten',
        'filename_optimize_low_suffix': '_geoptimaliseerd_laag',
        'filename_optimize_medium_suffix': '_geoptimaliseerd',
        'filename_optimize_high_suffix': '_geoptimaliseerd_hoog',
        'filename_optimize_maximum_suffix': '_geoptimaliseerd_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF bijsnijden',
        'crop_menu': 'PDF bijsnijden (Crop)',
        'crop_range': 'Toepassen op:',
        'crop_all_pages': 'Alle pagina\'s',
        'crop_current_page': 'Alleen huidige pagina',
        'crop_values': 'Bijsnijdwaarden (in punten):',
        'crop_left': 'Links:',
        'crop_right': 'Rechts:',
        'crop_top': 'Boven:',
        'crop_bottom': 'Onder:',
        'crop_presets': 'Voorinstellingen:',
        'crop_preset_white': 'Witte marges detecteren',
        'crop_reset': 'Resetten',
        'crop_mouse_hint': '🖱️ Sleep een rechthoek om het gebied grof te selecteren.\nDaarna kunt u de waarden nauwkeurig aanpassen in de SpinBoxen.\nHandmatig aanpassen met de muis is niet mogelijk.',
        'crop_apply': 'Bijsnijden',
        'crop_scope_all': 'Alle pagina\'s',
        'crop_scope_current': 'Huidige pagina',
        'crop_new_size': 'Nieuwe grootte: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Geen PDF geladen',
        'crop_preview_error': 'Fout bij laden van voorbeeld',
        'crop_start': 'Bijsnijden starten...',
        'crop_progress': 'PDF wordt bijgesneden...',
        'crop_success': 'PDF succesvol bijgesneden!\n\nOpgeslagen als:\n{0}\n\nWilt u de bijgesneden PDF openen?',
        'crop_complete': 'Bijsnijden voltooid',
        'crop_cancel': 'Bijsnijden geannuleerd',
        'crop_error_format': 'Fout tijdens bijsnijden:\n\n{0}',
        'filename_crop_suffix': '_bijgesneden',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF afvlakken (Flatten)',
        'flatten_menu': 'PDF afvlakken (Flatten)',
        'flatten_info': 'Het afvlakken van een PDF "brandt" alle bewerkbare elementen in de pagina-inhoud.\n\nDaarna zijn formuliervelden, annotaties, teksten, kruisen, handtekeningen, afbeeldingen en vormen niet meer afzonderlijk bewerkbaar.',
        'flatten_explanation_title': '📖 Waar is dit goed voor?',
        'flatten_explanation_text': 'Afvlakken is nodig in de volgende situaties:\n\n'
            '• 📄 U wilt het document voorbereiden voor afdrukken\n'
            '• 🔒 U wilt voorkomen dat iemand formuliervelden wijzigt\n'
            '• 📎 U wilt annotaties en opmerkingen "vast" in het document insluiten\n'
            '• 🖼️ U wilt ingevoegde teksten, kruisen, handtekeningen, afbeeldingen en vormen permanent in het document verankeren\n'
            '• 📦 U wilt het bestand voorbereiden voor archivering\n\n'
            'Afvlakken maakt de PDF kleiner en voorkomt dat elementen per ongeluk worden verplaatst of verwijderd.',
        'flatten_what_title': 'Wat wordt afgevlakt?',
        'flatten_what_list': '• ✅ Formuliervelden (tekstvelden, selectievakjes, knoppen)\n'
            '• ✅ Annotaties (opmerkingen, markeringen, notities)\n'
            '• ✅ Overlays (teksten, kruisen, handtekeningen, afbeeldingen, vormen)',
        'flatten_options': 'Opties:',
        'flatten_forms': 'Formuliervelden afvlakken',
        'flatten_annotations': 'Annotaties afvlakken',
        'flatten_overlays': 'Overlays afvlakken (teksten, kruisen, handtekeningen, afbeeldingen, vormen)',
        'flatten_target_folder': 'Doelmap:',
        'flatten_browse': 'Bladeren...',
        'flatten_select_folder': 'Selecteer doelmap',
        'flatten_warning': '⚠️ Belangrijk: Afvlakken is een onomkeerbaar proces!\n\nNa het afvlakken kunnen bewerkbare elementen niet meer afzonderlijk worden gewijzigd of verwijderd.\nMaak indien nodig vooraf een back-up.',
        'flatten_apply': 'Afvlakken',
        'flatten_start': 'Afvlakken starten...',
        'flatten_progress': 'PDF wordt afgevlakt...',
        'flatten_success': 'PDF succesvol afgevlakt!\n\nOpgeslagen als:\n{0}\n\nWilt u de afgevlakte PDF openen?',
        'flatten_complete': 'Afvlakken voltooid',
        'flatten_cancel': 'Afvlakken geannuleerd',
        'flatten_error_format': 'Fout tijdens afvlakken:\n\n{0}',
        'filename_flatten_suffix': '_afgevlakt',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF-overlay (Overlay)',
        'overlay_menu': 'PDF-overlay (Overlay)',
        'overlay_info': 'Plaatst een PDF (overlay) over een andere PDF.\n\nDe overlay-PDF wordt op de basis-PDF geplaatst. Dit is nuttig voor watermerken, logo\'s, briefhoofden of stempels.',
        'overlay_explanation_title': '📖 Waar is dit goed voor?',
        'overlay_explanation_text': 'Overlay is nodig in de volgende situaties:\n\n'
            '• 🏢 Een bedrijfslogo als watermerk op elke pagina plaatsen\n'
            '• 📄 Een briefhoofd op een lege PDF plaatsen\n'
            '• 🖊️ Een stempel-overlay op een document plaatsen\n'
            '• 🔖 Een watermerk op alle pagina\'s plaatsen\n'
            '• 📑 Een formulier-overlay op een sjabloon plaatsen',
        'overlay_type': 'Overlay-type:',
        'overlay_type_fullpage': 'Volledige pagina (bedekkend)',
        'overlay_type_transparent': 'Volledige pagina (transparant - aanbevolen)',
        'overlay_type_stamp': 'Stempel (positioneerbaar)',
        'overlay_type_info_fullpage': '📄 De overlay-PDF wordt exact over de hele pagina geplaatst.\nDe witte achtergrond kan worden verwijderd, zodat alleen de inhoud zichtbaar blijft.',
        'overlay_type_info_transparent': '🔍 De overlay-PDF wordt met transparante achtergrond over de hele pagina geplaatst.\nDe witte achtergrond wordt automatisch verwijderd - ideaal voor watermerken en logo\'s!',
        'overlay_type_info_stamp': '🖊️ De overlay-PDF wordt als stempel gepositioneerd en geschaald.\nPerfect voor logo\'s, stempels of handtekeningen op specifieke posities.',
        'overlay_remove_background': 'Witte achtergrond verwijderen:',
        'overlay_remove_background_enable': 'Witte achtergrond van de overlay-PDF verwijderen (maakt de overlay transparant)',
        'overlay_remove_background_tooltip': 'Verwijdert witte gebieden uit de overlay-PDF zodat de onderliggende tekst zichtbaar wordt.',
        'overlay_threshold': 'Drempelwaarde:',
        'overlay_threshold_hint': '(1-254, hoger = meer wit wordt verwijderd)',
        'overlay_select_file': 'Overlay-PDF selecteren:',
        'overlay_file_placeholder': 'Selecteer een PDF-bestand voor de overlay',
        'overlay_browse': 'Bladeren...',
        'overlay_select_overlay': 'Selecteer overlay-PDF',
        'overlay_range': 'Paginabereik:',
        'overlay_all_pages': 'Alle pagina\'s',
        'overlay_custom_range': 'Aangepast bereik',
        'overlay_from': 'Van:',
        'overlay_to': 'Tot:',
        'overlay_position': 'Positie:',
        'overlay_position_center': 'Midden',
        'overlay_position_top_left': 'Linksboven',
        'overlay_position_top_right': 'Rechtsboven',
        'overlay_position_bottom_left': 'Linksonder',
        'overlay_position_bottom_right': 'Rechtsonder',
        'overlay_size': 'Grootte:',
        'overlay_size_original': 'Originele grootte',
        'overlay_size_fit_page': 'Aanpassen aan pagina',
        'overlay_size_custom': 'Aangepast (%)',
        'overlay_opacity': 'Transparantie:',
        'overlay_target_folder': 'Doelmap:',
        'overlay_browse_folder': 'Bladeren...',
        'overlay_select_folder': 'Selecteer doelmap',
        'overlay_warning': '⚠️ Opmerking: De overlay-PDF wordt op de basis-PDF geplaatst en daarin "ingebrand".\n\nDe elementen van de overlay-PDF kunnen na opslaan niet meer afzonderlijk worden bewerkt.',
        'overlay_apply': 'Overlay',
        'overlay_start': 'Overlay starten...',
        'overlay_progress': 'PDF wordt overlayed...',
        'overlay_success': 'PDF succesvol overlayed!\n\nOpgeslagen als:\n{0}\n\nWilt u de overlayed PDF openen?',
        'overlay_complete': 'Overlay voltooid',
        'overlay_cancel': 'Overlay geannuleerd',
        'overlay_error_format': 'Fout tijdens overlay:\n\n{0}',
        'overlay_no_file': 'Geen overlay-PDF geselecteerd.\n\nSelecteer een PDF-bestand om te overlayen.',
        'filename_overlay_suffix': '_overlayed',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Afbeeldingen uit PDF extraheren',
        'extract_images_menu': 'Alle afbeeldingen extraheren',
        'extract_images_info': 'Extraheert alle afbeeldingen uit de PDF en slaat ze op als aparte bestanden.\n\nDe afbeeldingen worden in hun oorspronkelijke formaat opgeslagen of geconverteerd naar een geselecteerd formaat.',
        'extract_images_format': 'Afbeeldingsformaat:',
        'extract_images_quality': 'JPEG-kwaliteit:',
        'extract_images_options': 'Opties:',
        'extract_images_subfolder': 'Extraheren naar submap ("PDFnaam_afbeeldingen")',
        'extract_images_unique': 'Alleen unieke afbeeldingen (duplicaten vermijden)',
        'extract_images_range': 'Paginabereik:',
        'extract_images_all_pages': 'Alle pagina\'s',
        'extract_images_custom_range': 'Aangepast bereik',
        'extract_images_from': 'Van:',
        'extract_images_to': 'Tot:',
        'extract_images_target_folder': 'Doelmap:',
        'extract_images_browse': 'Bladeren...',
        'extract_images_select_folder': 'Selecteer doelmap',
        'extract_images_info_box': 'Informatie',
        'extract_images_info_text': 'Extractie kan bij grote PDF\'s enkele minuten duren.\n\nAfbeeldingen worden met hun oorspronkelijke naam opgeslagen (pagina_afbeelding).',
        'extract_images_extract': 'Extraheren',
        'extract_images_start': 'Extractie starten...',
        'extract_images_progress': 'Afbeeldingen extraheren...',
        'extract_images_success': '✅ Afbeeldingen succesvol geëxtraheerd!\n\n{0} afbeeldingen zijn opgeslagen in:\n{1}',
        'extract_images_complete': 'Afbeeldingsextractie voltooid',
        'extract_images_cancel': 'Extractie geannuleerd',
        'extract_images_error_format': 'Fout bij extraheren van afbeeldingen:\n\n{0}',
        'extract_images_open_folder': '📁 Map openen',
        'extract_images_no_images': 'Geen afbeeldingen gevonden in de PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Meerdere pagina\'s op één pagina (N-Up)',
        'nup_menu': 'Meerdere pagina\'s op één pagina (N-Up)',
        'nup_info': 'Rangschikt meerdere PDF-pagina\'s op één pagina.\n\nIdeaal voor compacte afdrukken, overzichten of hand-outs.',
        'nup_layout': 'Indeling:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Voorbeeld:',
        'nup_preview_info': '{0} pagina\'s → {1} pagina\'s per vel → {2} vellen\nIndeling: {3}',
        'nup_order': 'Volgorde:',
        'nup_order_horizontal': 'Horizontaal (rij voor rij)',
        'nup_order_vertical': 'Verticaal (kolom voor kolom)',
        'nup_order_horizontal_reverse': 'Horizontaal achterstevoren',
        'nup_order_vertical_reverse': 'Verticaal achterstevoren',
        'nup_range': 'Paginabereik:',
        'nup_all_pages': 'Alle pagina\'s',
        'nup_custom_range': 'Aangepast bereik',
        'nup_from': 'Van:',
        'nup_to': 'Tot:',
        'nup_options': 'Opties:',
        'nup_margins': 'Marges:',
        'nup_margin_between': 'Afstand tussen pagina\'s:',
        'nup_page_numbers': 'Paginanummers invoegen',
        'nup_target_folder': 'Doelmap:',
        'nup_browse': 'Bladeren...',
        'nup_select_folder': 'Selecteer doelmap',
        'nup_create': 'Maken',
        'nup_start': 'N-Up starten...',
        'nup_progress': 'N-Up wordt gemaakt...',
        'nup_success': 'N-Up succesvol gemaakt!\n\nOpgeslagen als:\n{0}\n\nWilt u de nieuwe PDF openen?',
        'nup_complete': 'N-Up voltooid',
        'nup_cancel': 'N-Up geannuleerd',
        'nup_error_format': 'Fout tijdens N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Paginaformaat wijzigen',
        'pagesize_menu': 'Paginaformaat wijzigen',
        'pagesize_info': 'Wijzigt het paginaformaat van de PDF.\n\nDe inhoud wordt automatisch aangepast aan het nieuwe formaat.',
        'pagesize_format': 'Formaat:',
        'pagesize_select': 'Selecteer een standaardformaat:',
        'pagesize_custom': 'Aangepast formaat:',
        'pagesize_width': 'Breedte:',
        'pagesize_height': 'Hoogte:',
        'pagesize_orientation': 'Oriëntatie:',
        'pagesize_portrait': 'Staand',
        'pagesize_landscape': 'Liggend',
        'pagesize_scale_options': 'Schaalopties:',
        'pagesize_fit': 'Aanpassen (beeldverhouding behouden)',
        'pagesize_stretch': 'Uitrekken (vervormen)',
        'pagesize_center': 'Centreren (originele grootte)',
        'pagesize_range': 'Paginabereik:',
        'pagesize_all_pages': 'Alle pagina\'s',
        'pagesize_custom_range': 'Aangepast bereik',
        'pagesize_from': 'Van:',
        'pagesize_to': 'Tot:',
        'pagesize_target_folder': 'Doelmap:',
        'pagesize_browse': 'Bladeren...',
        'pagesize_select_folder': 'Selecteer doelmap',
        'pagesize_apply': 'Toepassen',
        'pagesize_start': 'Paginaformaat wijzigen starten...',
        'pagesize_progress': 'Paginaformaat wordt gewijzigd...',
        'pagesize_success': 'Paginaformaat succesvol gewijzigd!\n\nOpgeslagen als:\n{0}\n\nWilt u de nieuwe PDF openen?',
        'pagesize_complete': 'Paginaformaat wijzigen voltooid',
        'pagesize_cancel': 'Paginaformaat wijzigen geannuleerd',
        'pagesize_error_format': 'Fout tijdens wijzigen van paginaformaat:\n\n{0}',
        'pagesize_preview_info': 'Nieuw formaat: {0} x {1} pt',
        'filename_pagesize_suffix': '_nieuw_formaat',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-informatie',
        'pdf_info_menu': 'PDF-info weergeven',
        'pdf_info_voice': 'PDF-informatie wordt weergegeven',
        'pdf_info_error': 'Fout bij weergeven van PDF-info:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Sneltoetsen weergeven",
        "shortcuts_dialog_title": "Sneltoetsen",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 BESTAND</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF openen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF sluiten</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Opslaan als...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Document beveiligen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Afdrukken</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Direct afdrukken (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Applicatie afsluiten</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORTEREN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exporteren als Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exporteren als DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exporteren als TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exporteren als afbeeldingen (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Afbeeldingen extraheren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOCUMENTVERWERKING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Meerdere pagina's)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A-conversie (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF afvlakken</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF-overlay</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF optimaliseren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ BEWERKEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Zoeken</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Bladwijzer toevoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Bladwijzers beheren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Volgende bladwijzer</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Vorige bladwijzer</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR uitvoeren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 PAGINABEHEER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Huidige pagina roteren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Alle pagina's roteren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Huidige pagina normaliseren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Alle pagina's normaliseren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Pagina's verwijderen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Pagina's extraheren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Pagina's invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Pagina's verplaatsen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDF's samenvoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Paginaformaat wijzigen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INVOEGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Tekst invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Kruis invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Handtekening 1 invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Handtekening 2 invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Afbeelding invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rechthoek invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ellips invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Lijn invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Pijl invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Paginanummers invoegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Tekst-watermerk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Afbeelding-watermerk</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDACTIES</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redactie (zwart)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redactie (wit)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Alle redacties toepassen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ GEAVANCEERD</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF bijsnijden</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Metadata bewerken</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ WEERGAVE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Donkere/Lichte modus wisselen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Tekstvenster weergeven</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Paginabreedte (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Twee pagina's (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Overzicht (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ INSTELLINGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Wachtwoordbeheer</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR-instellingen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Handtekeninginstellingen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Bestandsnaamopmaak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Instellingen exporteren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Instellingen importeren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF-info weergeven</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Spraakuitvoer in/uitschakelen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Menubalk focussen</td></tr>"
        "</table>",


        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nieuwe versie beschikbaar",
        "update_available_message": "Er is een nieuwe versie <b>{0}</b> beschikbaar.\n\nBezoek de release-pagina om de update te downloaden:\n{1}",
        "update_available_voice": "Nieuwe versie {0} beschikbaar. Download de update van de GitHub-pagina.",
        "update_open_release": "Release-pagina openen",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Alle vertalingen downloaden",
        "ask_download_all_translations": """Naast Duits, Engels en Vietnamees zijn er nog {total_languages} andere GUI-talen beschikbaar.\n\nMoeten deze worden voorzien / bijgewerkt?\n\nOpmerking:\nOnnodige talen kunt u later handmatig verwijderen in de map:\n{translations_path}
        \nAls u annuleert, kunt u de GUI-talen later downloaden via het menu 'Extra → Vertalingen bijwerken'.""",
        "menu_update_translations": "Vertalingen bijwerken",
        "translations_updated": "Vertalingen bijgewerkt",
        "translations_update_success": "{} vertalingen zijn succesvol bijgewerkt ({} nieuw, {} bijgewerkt).",
        "translations_update_error": "Fout bij het bijwerken van vertalingen",
        "translations_update_no_changes": "Alle vertalingen zijn al up-to-date.",
        "translations_update_offline": "Geen internetverbinding. Vertalingen konden niet worden bijgewerkt.",
        "translations_update_in_progress": "Vertalingen worden op de achtergrond bijgewerkt...",
        "translations_downloading": "Vertalingen downloaden...",
        "translations_path_hint": "Gebruikersmap voor vertalingen",
        "translations_update_not_available_title": "Update niet beschikbaar",
        "translations_update_not_available_message": """Het bijwerken van vertalingen is alleen beschikbaar in de geïnstalleerde versie.\n\nIn ontwikkelmodus zijn de vertalingen al up-to-date.""",
        "translations_update_no_internet_title": "Geen internetverbinding",
        "translations_update_no_internet_message": """Er kon geen internetverbinding tot stand worden gebracht.\n\nDe vertalingen kunnen niet van GitHub worden gedownload.\n\nMogelijke oplossingen:
        • Controleer uw internetverbinding
        • Schakel eventuele firewall tijdelijk uit
        • Probeer het later opnieuw
        \nU kunt de vertalingen ook handmatig van GitHub downloaden:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Update is al bezig",
        "btn_retry": "Opnieuw proberen",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Welkom bij PDF Dark View",
        "welcome_title_not_supported": "Welkom bij PDF Dark View",
        "welcome_message": "Welkom bij PDF Dark View!\n\nUw systeemtaal werd herkend als '{language}'.\nWilt u deze taal gebruiken voor de gebruikersinterface?\n\nU kunt de taal op elk moment wijzigen via 'Instellingen → Taal'.",
        "welcome_message_language_not_available": "Welkom bij PDF Dark View!\n\nUw systeemtaal werd herkend als '{language}'.\nDeze taal is nog niet geïnstalleerd.\n\nWilt u nu de vertalingen voor {language} downloaden van GitHub?\n\n(De taal wordt dan automatisch gebruikt voor de gebruikersinterface.)",
        "welcome_message_language_not_supported": "Welkom bij PDF Dark View!\n\nUw systeemtaal werd herkend als '{language}'.\nHelaas zijn er nog geen vertalingen voor deze taal.\n\nDe gebruikersinterface wordt weergegeven in {fallback_language}.\n\nU kunt de taal op elk moment wijzigen via 'Instellingen → Taal'.\nAls u wilt, kunt u ook zelf een vertaling voor uw taal bijdragen:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Ja, systeemtaal gebruiken",
        "welcome_keep_english": "Nee, Engels behouden",
        "welcome_download_language": "Ja, {language} downloaden",

        # ============================================
        # 107. RECENT GEBRUIKTE PADEN
        # ============================================

        'menu_recent': 'Recent gebruikt',
        'menu_recent_dirs': 'Mappen...',
        'menu_recent_files': 'Bestanden...',
        'recent_manage': 'Beheren...',
        'recent_enable_tracking': 'Recent gebruikte paden opslaan (privacy)',
        'recent_enable_info': 'Schakel deze optie uit om geen paden op te slaan',
        'recent_tracking_disabled': 'Padvolging is uitgeschakeld',
        'recent_enabled': 'ingeschakeld',
        'recent_disabled': 'uitgeschakeld',
        'recent_tracking_status': 'Padvolging {0}',
        'recent_dialog_title': 'Recent gebruikte paden',
        'recent_tab_directories': 'Mappen',
        'recent_tab_files': 'Bestanden',
        'recent_dirs_instruction': 'Dubbelklik om het bestandsdialoogvenster in de map te openen',
        'recent_files_instruction': 'Dubbelklik om de PDF direct te openen',
        'recent_no_directories': '(geen opgeslagen mappen)',
        'recent_no_files': '(geen opgeslagen bestanden)',
        'recent_default_current': '⭐ Standaard: {0}',
        'recent_set_as_default': '⭐ Als standaard instellen',
        'recent_default_set_title': 'Standaardmap ingesteld',
        'recent_default_set_message': 'De map "{0}" is ingesteld als standaard voor het openen van PDF\'s.',
        'recent_default_set_voice': 'Standaardmap is ingesteld',
        'recent_directory_not_found': 'Map niet gevonden',
        'recent_file_not_found': 'Bestand niet gevonden',
        'recent_remove_selected': 'Verwijderen',
        'recent_remove_title': 'Pad verwijderen',
        'recent_remove_confirm': 'Weet u zeker dat u het pad "{0}" uit de lijst wilt verwijderen?',
        'recent_path_removed': 'Pad is verwijderd',
        'recent_clear_all': 'Alles verwijderen',
        'recent_clear_title': 'Alle paden verwijderen',
        'recent_clear_confirm_type': 'Weet u zeker dat u alle {0} wilt verwijderen?',
        'recent_cleared': 'Lijst is gewist',
        'recent_path_not_found_title': 'Pad niet gevonden',
        'recent_path_not_found_message': 'Het pad "{0}" bestaat niet meer.',
        'recent_open_file': 'Bestand openen',
        'btn_open_recent': 'Openen',
        'recent_open_file_question': 'Wilt u "{0}" als PDF openen?',
        'recent_not_pdf': 'Het geselecteerde bestand is geen PDF.',
        'recent_more_entries': 'Meer items...',
        'btn_remove': 'Verwijderen',
        'btn_clear': 'Alles wissen',
        'recent_context_open': 'Openen',
        'recent_context_reveal': 'Toon in Finder',
        'recent_context_set_default': '⭐ Als standaard instellen',
        'recent_context_open_terminal': '💻 Terminal openen',
        'recent_context_file_info': 'Bestandsinfo',
        'recent_context_open_with_default': '📄 Openen met standaardapp',
        'recent_context_remove': 'Uit lijst verwijderen',
        'recent_context_clear_all': 'Alles verwijderen',
        'recent_file_info_title': 'Bestandsinformatie',
        'recent_file_info_name': 'Naam',
        'recent_file_info_path': 'Pad',
        'recent_file_info_size': 'Grootte',
        'recent_file_info_modified': 'Gewijzigd',
        'recent_file_info_pages': 'Pagina\'s',
        'recent_error_reveal': 'Fout bij openen in Finder',
        'recent_error_terminal': 'Fout bij openen van Terminal',
        'recent_error_info': 'Fout bij ophalen van bestandsinfo',
        'open_user_data_folder': 'Toon gebruikersgegevensmap',

        # ============================================
        # 108. EVEN/ONEVEN PAGINA'S VERWIJDEREN
        # ============================================
        "pages_delete_even": "Alle even pagina's verwijderen",
        "pages_delete_odd":  "Alle oneven pagina's verwijderen",
        "progress_even_pages": "Even pagina's worden verwijderd",
        "progress_odd_pages": "Oneven pagina's worden verwijderd",
        "progress_mark_delete_even": "{} even pagina('s) gemarkeerd voor verwijdering",
        "progress_mark_delete_odd":  "{} oneven pagina('s) gemarkeerd voor verwijdering",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programma wordt afgesloten",

    }
