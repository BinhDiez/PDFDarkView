
# ============================================
# translations_no.py - Norsk ordbok (bokmål)
# Fullstendig sortert etter kategorier
# Kommentarer på tysk for konsistens
# ============================================

def load_norwegian_strings():
    """Laster alle norske strenger"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View av BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Åpne PDF",
        'btn_text_window': "OCR‑tekst",
        'btn_first': "Første side",
        'btn_prev': "Forrige side",
        'btn_next': "Neste side",
        'btn_last': "Siste side",
        'btn_print': "Skriv ut",
        'btn_darkmode_light': "Lys modus",
        'btn_darkmode_dark': "Mørk modus",
        'btn_delete_pages': "Slett sider",
        'btn_extract_pages': "Trekk ut sider",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Avbryt",
        'btn_save': "Lagre",
        'btn_close': "Lukk",
        'btn_delete': "Slett",
        'btn_delete_all': "Slett alle",
        'btn_copy': "Kopier",
        'btn_export': "Eksporter",
        'btn_show': "Vis passord",
        'btn_hide': "Skjul passord",
        'btn_authenticate': "Autentiser",
        'btn_settings': "Innstillinger",
        'btn_protect': "Beskytt",
        'btn_remove_password': "Fjern passord",
        'btn_manage': "Passordbehandling",
        'btn_retry': "Prøv på nytt",
        'btn_select_all': "Velg alle",
        'btn_clear_selection': "Fjern valg",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Side {0} av {1}",
        'page_count': "av {0}",
        'goto_page': "Gå til side",
        'page_simple': "Side {0}",
        'full_view_page': "Full visning side {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Skriv søkeord + Enter",
        'search_results': "Resultater: {0} av {1}",
        'search_nav_hint': "Enter: neste  (Shift+Enter: forrige) treff",
        'search_no_results': "Ingen treff",
        'search_error': "Søkefeil",
        'search_active': "Søkefelt aktivert",
        'search_closed': "Søk avsluttet",
        'search_position': "Side {0} {1}",
        'search_pos_top': "helt øverst",
        'search_pos_upper': "øverst",
        'search_pos_middle': "midten",
        'search_pos_lower': "nederst",
        'search_pos_bottom': "helt nederst",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Tekstgjenkjenning fullført!",
        'ocr_success_title': "OCR vellykket",
        'ocr_success_message': "Dokumentet er nå søkbart.",
        'ocr_failed': "OCR mislyktes",
        'ocr_in_progress': "OCR pågår",
        'ocr_preparing': "Forbereder PDF...",
        'ocr_analyzing': "Analyserer PDF...",
        'ocr_optimizing': "Bildeoptimalisering pågår...",
        'ocr_recognizing': "Tekstgjenkjenning pågår...",
        'ocr_embedding': "Bygger inn tekst...",
        'ocr_finalizing': "Fullfører PDF...",
        'ocr_not_available': "OCR ikke tilgjengelig",
        'ocr_install_message': "OCR‑verktøy ble ikke funnet.\n\nInstaller:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR påkrevd",
        'ocr_question': "PDF‑en inneholder ingen søkbar tekst.\nVil du kjøre OCR for å muliggjøre {0}?",
        'ocr_perform': "Kjør OCR",
        'ocr_later': "Senere",
        'ocr_starting': "Starter garantert OCR...",
        'ocr_success_voice': "OCR vellykket. PDF er nå søkbar.",
        'ocr_partial_success': "OCR ble utført, men det oppsto problemer under erstatning.\n\nDen søkbare versjonen ble lagret som:\n{0}\n\nFeil: {1}",
        'ocr_partial_title': "OCR delvis vellykket",
        'ocr_partial_voice': "OCR utført, men erstatning mislyktes.",
        'original_file': "Originalfil:",
        'old_size': "Gammel filstørrelse:    {0} byte",
        'new_size': "Ny filstørrelse: {0} byte",
        'size_change': "Endring: {0}{1} byte",
        'backup_created_file': "Sikkerhetskopi opprettet:\n{0}",
        'backup_not_created': "Sikkerhetskopi: ikke opprettet (innstilling deaktivert)",
        'page_header': "=== Side {0} ===\n{1}\n",
        'scanned_page_header': "=== Side {0} (skannet) ===\n[Denne siden inneholder kun skannet tekst]\n[Utfør OCR manuelt]\n",
        'scanned_warning': "⚠️ SKANNET TEKST – OCR PÅKREVD",
        'guaranteed_title': "Søkbar PDF opprettet",
        'guaranteed_message': "<b>Garantert søkbar versjon opprettet!</b>\n\nSiden automatisk OCR mislyktes, ble en alternativ søkbar PDF opprettet:\n\n{0}\n\n<b>Denne filen inneholder:</b>\n• Utvunnet tekst (hvis tilgjengelig)\n• Henvisninger til skannede sider\n• Er fullt søkbar",
        'guaranteed_voice': "Garantert søkbar PDF opprettet.",
        'instruction_title': "VEILEDNING FOR OCR",
        'instruction_file': "Originalfil: {0}",
        'instruction_text': "Automatisk tekstgjenkjenning (OCR) mislyktes.\nUtfør OCR manuelt:\n\n1. MED OCRmyPDF (kommandolinje):\n   ocrmypdf --force-ocr \"[FIL]\" \"utdata.pdf\"\n\n2. MED ADOBE ACROBAT (macOS/Windows):\n   • Åpne PDF i Acrobat\n   • Verktøy > Rediger PDF\n   • Velg 'Gjenkjenn tekst'\n\n3. MED FORHÅNDSVISNING (macOS):\n   • Åpne PDF i Forhåndsvisning\n   • Arkiv > Eksporter...\n   • Quartz‑filter: 'Reduser filstørrelse'\n   • Aktiver 'Utfør OCR'\n\n4. ONLINE OCR‑TJENESTER:\n   • smallpdf.com/no/ocr-pdf\n   • ilovepdf.com/no/ocr-pdf\n   • adobe.com/no/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR‑veiledning opprettet",
        'instruction_created_message': "En detaljert veiledning ble opprettet:\n\n{0}\n\nFølg trinnene for manuell OCR.",
        'instruction_created_voice': "OCR‑veiledning opprettet.",
        'ocr_impossible': "OCR ikke mulig",
        'ocr_impossible_message': "OCR kunne ikke utføres.\n\nBearbeid '{0}' manuelt med OCR‑programvare.",
        'ocr_impossible_voice': "OCR ikke mulig. Utfør manuell behandling.",
        'emergency_title': "Nød‑OCR",
        'emergency_message': "En nød‑PDF ble opprettet:\n\n{0}\n\nBearbeid denne filen manuelt med OCR.",
        'emergency_voice': "Nød‑PDF opprettet. Utfør OCR manuelt.",
        'critical_error': "Kritisk feil",
        'critical_error_message': "OCR kunne ikke startes.\n\nStart programmet på nytt og\nkontroller OCR‑installasjonen.",
        'critical_error_voice': "Kritisk OCR‑feil",
        'ocr_question_html': "<p>PDF‑en inneholder ingen søkbar tekst.<p>Vil du kjøre OCR for å muliggjøre <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR påkrevd. PDF‑en inneholder ingen søkbar tekst. Vil du kjøre OCR for å muliggjøre {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ingen PDF lastet",
        'no_pdf_message': "Ingen PDF er lastet",
        'pdf_not_found': "PDF‑fil ikke funnet",
        'file_size': "Filstørrelse",
        'bytes': "byte",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Sikkerhetskopi opprettet",
        'backup_disabled': "Sikkerhetskopi deaktivert",
        'backup_activated': "Sikkerhetskopiering aktivert",
        'backup_deactivated': "Sikkerhetskopiering deaktivert",
        'backup_status': "Sikkerhetskopi: {0}",
        'backup_on': "✔ aktivert",
        'backup_off': "✘ deaktivert",
        'close_pdf': "Lukker PDF: {0}",
        'pdf_not_found_format': "PDF‑fil ikke funnet: {0}",
        'error_pdf_load_format': "Feil ved lasting av PDF: {0}",
        'load_failed_format': "Lasting mislyktes:\n{0}",
        'decrypted_suffix': "(dekryptert)",
        'decryption_failed': "Dekryptering mislyktes.",
        'decryption_error': "Feil under dekryptering",
        'decryption_success': "Dekryptering vellykket",
        'decryption_success_message': "PDF ble dekryptert og lagret som:\n\n{0}",
        'decryption_success_voice': "PDF ble dekryptert og lagret.",
        'password_remove_error': "Feil ved fjerning av passord",
        'save_unencrypted': "Lagre ukryptert PDF som",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Lagre som...",
        'save_copy': "Lagre kopi",
        'save_success': "PDF lagret som: {0}",
        'save_encrypted': "Beskyttet PDF lagret som: {0}",
        'save_error': "PDF kunne ikke lagres",
        'encryption_question': "Vil du beskytte PDF‑en med et passord?",
        'encryption_yes': "Ja",
        'encryption_no': "Nei",
        'encryption_cancel': "Avbryt",
        'save_cancel': "Lagring avbrutt",
        'save_encrypted_voice': "Filkryptert og lagret.",
        'save_success_voice': "PDF‑filen ble lagret ukryptert.",
        'save_error_format': "PDF kunne ikke lagres:\n{0}",
        'export_pages_success': "Pages‑eksport vellykket",
        'export_pages_error': "Pages‑eksport mislyktes",
        'export_pages_error_format': "Pages‑eksport mislyktes: {0}",
        'export_word_success': "Word‑eksport vellykket",
        'export_word_error': "Word‑eksport mislyktes",
        'export_word_error_format': "Word‑eksport mislyktes: {0}",
        'export_text_success': "Teksteksport vellykket",
        'export_text_error': "Teksteksport mislyktes",
        'export_text_error_format': "Teksteksport mislyktes: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Passord påkrevd",
        'password_enter': "Skriv inn passord",
        'password_confirm': "Bekreft passord",
        'password_new': "Nytt passord",
        'password_current': "Nåværende passord",
        'password_save': "Lagre passord (kryptert)",
        'password_saved': "✓ Passord for denne filen er lagret",
        'password_wrong': "Feil passord",
        'password_mismatch': "Passordene stemmer ikke overens",
        'password_too_short': "Passordet er for kort",
        'password_min_length': "Passordet må være minst 4 tegn langt",
        'password_strength': "Passordstyrke",
        'password_strength_very_weak': "Veldig svakt",
        'password_strength_weak': "Svakt",
        'password_strength_medium': "Middels",
        'password_strength_strong': "Sterkt",
        'password_strength_very_strong': "Veldig sterkt",
        'password_char_count': "({0} tegn)",
        'password_match': "✓ Stemmer",
        'password_no_match': "✗ Passordene stemmer ikke overens",
        'password_show': "Vis",
        'password_hide': "Skjul",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Passordbehandling",
        'password_table_filename': "Filnavn",
        'password_table_password': "Passord",
        'password_count': "{0} lagret passord",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Ingen lagrede passord",
        'password_copied': "{0} passord kopiert",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Vil du virkelig slette passordet for '{0}'?",
        'password_delete_multiple': "Vil du virkelig slette de {0} valgte passordene?",
        'password_delete_all_confirm': "Vil du virkelig slette alle {0} lagrede passord?",
        'password_deleted': "{0} passord slettet",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Alle passord er slettet",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Passordgenerator",
        'generator_generated': "Generert passord:",
        'generator_regenerate': "Generer på nytt",
        'generator_copy': "Kopier",
        'generator_use': "Bruk",
        'generator_settings': "Innstillinger",
        'generator_length': "Lengde:",
        'generator_group_every': "Skilletegn hver",
        'generator_group_chars': "tegn.   Skilletegn:",
        'generator_uppercase': "Store bokstaver (A‑Z)",
        'generator_lowercase': "Små bokstaver (a‑z)",
        'generator_digits': "Siffer (0‑9)",
        'generator_symbols': "Symboler (!@#$%^&*)",
        'generator_exclude': "Utelukket:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Masterpassord påkrevd",
        'master_password_setup': "Opprett masterpassord",
        'master_password_change': "Endre masterpassord",
        'master_password_enter': "Skriv inn ditt masterpassord",
        'master_password_choose': "Velg et sterkt masterpassord (minst 8 tegn)",
        'master_password_new': "Skriv inn ditt nye masterpassord",
        'master_password_confirm': "Bekreft passord",
        'master_password_authenticate': "Autentiser",
        'master_password_success': "Masterpassord opprettet.",
        'master_password_changed': "Masterpassord endret.",
        'master_password_removed': "Masterpassord og alle passord slettet.",
        'master_password_remove': "Fjern masterpassord",
        'master_password_remove_confirm': "Er du SIKKER på at du vil slette ALLE passord?\n\nDenne handlingen er UOPPRETTELIG!",
        'master_password_export_before': "Vil du eksportere en sikkerhetskopi først?",
        'master_password_export_delete': "Eksporter og slett",
        'master_password_delete_now': "Slett nå",
        'master_password_for_signatures': "For å bruke signaturer må du opprette et masterpassord.\n\nVil du opprette et masterpassord nå?",
        'master_password_for_private': "For å bruke private tekstblokker må du opprette et masterpassord.\n\nVil du opprette et masterpassord nå?",
        'master_password_info': """
            <b>🔐 UTEN MASTERPASSORD:</b><br>
            • Ingen visning, kopiering eller eksport av passord mulig<br>
            • Sletting av passord er alltid mulig (også uten masterpassord)<br><br>

            <b>🔐 MED MASTERPASSORD:</b><br>
            • Alle funksjoner tilgjengelige etter autentisering<br>
            • Passord krypteres med masterpassordet<br>
            • Minimumslengde: 8 tegn<br>
            • Sikker SHA‑256 hash‑lagring<br><br>

            <b>VIKTIG:</b><br>
            • Hvis masterpassordet mistes, kan passordene ikke gjenopprettes<br>
            • Når masterpassordet fjernes, slettes ALLE passord<br>
            • Eksportmulighet før sletting<br>
            • Masterpassordet kan alltid endres
        """,
        'signature_auth_disabled': "Deaktiver passordforespørsel for signaturer",
        'template_auth_disabled': "Deaktiver passordforespørsel for private tekstblokker",
        'master_password_for_signatures_settings': "For å bruke signaturer må du opprette et masterpassord.\n\nGå til Innstillinger – Passordbehandling",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Beskytt PDF",
        'protect_info': "Filen '{0}' vil bli beskyttet med et passord.",
        'protect_instruction': "Skriv inn ønsket passord to ganger for å beskytte dokumentet, eller bruk passordgeneratoren til høyre for inntastingsfeltet.",
        'protect_success': "PDF ble beskyttet og lagret som:\n{0}\n\nPassord: {1}\n\nVil du åpne den beskyttede PDF‑en nå?",
        'protect_open': "Ja",
        'protect_skip': "Nei",
        'protect_error': "Feil ved beskyttelse av PDF",
        'protect_open_title': "åpne beskyttet PDF",
        'protect_question': "Ferdig. Vil du åpne den beskyttede PDF‑en nå? Ja eller Nei?",
        'password_cancel': "Passorddialog avbrutt",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Slett sider",
        'pages_extract': "Trekk ut sider",
        'pages_insert': "Sett inn sider",
        'pages_move': "Flytt sider",
        'pages_delete_options': "Slettealternativer",
        'pages_delete_empty': "Slett alle tomme sider",
        'pages_delete_current': "Slett gjeldende side",
        'pages_delete_range': "Slett sideintervall",
        'pages_extract_options': "Uttrekkingsalternativer",
        'pages_extract_current': "Trekk ut gjeldende side",
        'pages_extract_range': "Trekk ut sideintervall",
        'pages_insert_position': "Innsettingsposisjon",
        'pages_insert_before': "Sett inn før side:",
        'pages_insert_select': "Velg PDF",
        'pages_insert_none': "Ingen PDF valgt",
        'pages_move_source': "Sider som skal flyttes",
        'pages_move_from': "Fra side:",
        'pages_move_to': "Til side:",
        'pages_move_target': "Målposisjon",
        'pages_move_before': "Flytt før side:",
        'pages_move_hint': "Merk: side 1 = begynnelse, {0} = slutt",
        'pages_range_invalid': "Startside må være mindre enn eller lik sluttside.",
        'pages_position_invalid': "Målposisjonen må ikke være innenfor intervallet som skal flyttes.",
        'pages_no_pdf_selected': "Ingen PDF er valgt.",
        'pages_deleted': "{0} sider ble slettet.",
        'pages_extracted': "Utvunnet: {0}\nLagret som: {1}\nFilstørrelse: {2:.1f} KB",
        'pages_inserted': "{0} sider satt inn",
        'pages_moved': "{0} sider ble flyttet.",
        'pages_deleted_none': "Ingen sider ble slettet.",
        'pages_delete_progress': "Sletter sider...",
        'pages_deleted_with_backup': "{0} sider ble slettet.\n\nSikkerhetskopi: {1}",
        'pages_deleted_voice': "En sikkerhetskopi ble opprettet, og {0} sider ble slettet.",
        'info': "Info",
        'error_dialog_creation': "Dialog kunne ikke opprettes",
        'extract_page_single': "Trekk ut side {0}",
        'extract_page_range': "Trekk ut sidene {0}‑{1}",
        'extract_success_voice': "Sider utvunnet",
        'extract_error_format': "Feil ved uttrekking: {0}",
        'pages_inserted_voice': "{0} sider satt inn.",
        'insert_error_format': "Feil ved innsetting: {0}",
        'pages_move_progress': "Flytter sider...",
        'pages_moved_with_backup': "{0} sider ble flyttet.\n\nSikkerhetskopi: {1}",
        'move_success_title': "Flytting vellykket",
        'pages_moved_voice': "{0} sider flyttet",
        'mark_removed': "Markering fjernet fra side {0}",
        'mark_empty': "Side {0} markert som tom",
        'mark_export_removed': "Eksportmarkering fjernet fra side {0}",
        'mark_export': "Side {0} markert for eksport",
        'no_empty_pages': "Ingen tomme sider markert for sletting",
        'delete_empty_confirm': "Vil du slette alle {0} markerte tomme sider?",
        'delete_empty_confirm_voice': "Slett alle {0} markerte tomme sider nå? Ja eller Nei.",
        'empty_pages_deleted': "{0} tomme sider slettet",
        'no_export_pages': "Ingen sider markert for eksport",
        'overwrite_title': "Overskriv eksisterende fil",
        'overwrite_question': "Filen\n\n{0}\n\nfinnes allerede.\nVil du overskrive den?",
        'overwrite_voice': "Overskriv eksisterende fil? Ja eller Nei.",
        'page_skipped': "Side {0} ble hoppet over",
        'export_complete': "Eksport fullført.",
        'export_complete_voice': "Eksporten er fullført.",
        'no_pages_exported': "Ingen side eksportert",
        'export_cancelled': "Eksport avbrutt",
        'pages_exported': "{0} sider eksportert til {1}",
        'export_page_title': "Eksporter side",
        'page_exported': "Side {0} eksportert til {1}",
        'export_error': "Feil ved eksport",
        'export_marked_title': "Eksporter markerte sider",
        'rotate_all_title': "roter alle sider",
        'rotate_all_question': "Vil du rotere alle sider 90 grader til høyre?",
        'rotate_all_voice': "Vil du rotere alle sider 90 grader til høyre? Ja eller Nei?",
        'all_pages_rotated': "Alle sider rotert",
        'page_rotated': "Side {0} rotert",
        'rotate_error': "Siden kunne ikke roteres",
        'delete_page_confirm': "Vil du slette side {0}?",
        'delete_page_confirm_voice': "Vil du virkelig slette side {0}? Ja eller Nei.",
        'page_deleted': "Side {0} slettet",
        'delete_error': "Siden kunne ikke slettes",
        'pages_deleted_voice': "{0} sider slettet",
        'pages_exported_split': "{0} sider ble eksportert.",
        'pages_skipped': "{0} sider ble hoppet over.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Trekk ut sider (avansert)",
        'pdf_splitter_title': "PDF‑deler og ‑uttrekker",
        'pdf_splitter_load': " Velg PDF‑fil",
        'pdf_splitter_info': "Velg et alternativ for PDF‑dokumentet ditt",
        'pdf_splitter_basic': "Grunnleggende operasjoner",
        'pdf_splitter_single': "Del opp i enkeltsider",
        'pdf_splitter_range': "Trekk ut sider:",
        'pdf_splitter_range_placeholder': "f.eks. 1‑3,5,7‑9",
        'pdf_splitter_clean': "Rengjøringsoperasjoner",
        'pdf_splitter_remove_empty': "Fjern alle tomme sider",
        'pdf_splitter_remove': "Slett sideintervall:",
        'pdf_splitter_remove_placeholder': "f.eks. 2,4‑6",
        'pdf_splitter_process': "Behandle PDF",
        'pdf_splitter_loaded': "PDF lastet. Velg et alternativ",
        'pdf_read_error': "PDF kunne ikke leses",
        'pages': "Sider",
        'pages_created': "Sider opprettet",
        'range_empty': "Skriv inn et sideintervall",
        'range_invalid': "Ugyldig sideintervall",
        'range_created': "Ny PDF med valgte sider opprettet:\n{0}",
        'empty_removed': "{0} tomme sider fjernet.\nUtdata: {1}",
        'remove_empty': "Skriv inn sider som skal fjernes",
        'remove_invalid': "Ugyldige sider å fjerne",
        'remove_done': "Ren PDF opprettet:\n{0}",
        'open_folder': "Åpne mappe",
        'show_in_finder': "Vis i Finder",
        'pdf_splitter_no_pdf': "Last først inn en PDF‑fil.",
        'process_error': "Feil ved behandling av PDF",
        'pages_created_voice': "{0} sider opprettet",
        'range_created_voice': "PDF med valgte sider opprettet",
        'empty_removed_voice': "{0} tomme sider fjernet",
        'remove_done_voice': "Ren PDF opprettet",
        'pdf_splitter_split_groups': "Hver sammenhengende gruppe i separat fil",
        'range_created_single': "Ny PDF opprettet:\n{0}",
        'range_created_multiple': "{0} PDF‑filer opprettet.",
        'range_created_voice_single': "Én PDF med valgte sider opprettet",
        'range_created_voice_multiple': "{0} PDF‑filer opprettet",
        'empty_removed_none_left': "Ingen sider igjen",
        'empty_removed_all_empty': "Alle sider ble gjenkjent som tomme og ville bli fjernet. Ingen fil opprettet.",
        'preview_single': "Forhåndsvisning: {0}",
        'preview_enter_range': "Skriv inn et sideintervall.",
        'preview_invalid_range': "Ugyldig sideintervall.",
        'preview_file': "Forhåndsvisning: {0}",
        'preview_files': "Forhåndsvisning: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Starter utskrift",
        'print_sent': "Utskriftsoppdrag sendt",
        'print_now': "Skriv ut nå",
        'print_error': "Feil ved direkte utskrift",
        'print_limited': "Utskriftsfunksjonen er begrenset på dette systemet",
        'print_error_format': "Feil ved direkte utskrift: {0}",
        'warning': "Merknad",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Bytt til lys modus",
        'mode_switch_to_dark': "Bytt til mørk modus",
        'mode_dark_activated': "Mørk modus aktivert",
        'mode_light_activated': "Lys modus aktivert",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Full visning",
        'zoom_two_pages': "To sider side ved side",
        'zoom_overview': "Oversiktsmodus",
        'zoom_cannot_during_search': "Zoom ikke mulig under søk",
        'zoom_exit_first': "Forlat zoom først",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Dra og slipp aktivert",
        'drag_disabled': "Dra og slipp deaktivert",
        'drag_page_grab': "Griper side {0}",
        'drag_page_dropped': "Side {0} satt inn på posisjon {1}",
        'drag_position_invalid': "Ugyldig posisjon",
        'drag_same_position': "Side {0} forblir på posisjon {0}",
        'drag_error': "Feil ved flytting",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Tekstinntasting med avansert formatering og tekstblokkbehandling",
        'text_templates': "Tilgjengelige tekstblokker:",
        'text_name': "Navn",
        'text_preview': "Teksteksempel",
        'text_enter': "Tekst:",
        'text_font_size': "Skriftstørrelse:",
        'text_formatting': "Formatering:",
        'text_bold': "Fet",
        'text_italic': "Kursiv",
        'text_underline': "Understreket",
        'text_alignment': "Justering:",
        'text_left': "Venstre",
        'text_center': "Sentrert",
        'text_right': "Høyre",
        'text_color': "Tekstfarge:",
        'text_opacity': "Gjennomsiktighet:",
        'text_word_wrap': "Orddeling:",
        'text_auto': "Automatisk",
        'text_page_width_95': "Sidebredde (95%)",
        'text_page_width_85': "Veldig bred (85%)",
        'text_page_width_75': "Bredere (75%)",
        'text_page_width_60': "Bred (60%)",
        'text_page_width_50': "Middels (50%)",
        'text_page_width_30': "Smal (30%)",
        'text_page_width_20': "Smallere (20%)",
        'text_page_width_10': "Veldig smal (10%)",
        'text_no_wrap': "Ingen ombryting",
        'text_private': "Privat tekstblokk (krever autentisering)",
        'text_preview_label': "Forhåndsvisning:",
        'text_preview_placeholder': "Her vises et eksempel på teksten...",
        'text_no_text': "(Ingen tekst)",
        'text_save_template': "💾 Lagre som blokk",
        'text_delete_template': "🗑 Slett valgt tekstblokk",
        'text_show_private': "Vis private",
        'text_hide_private': "Skjul private",
        'text_use': "✅ Bruk tekst",
        'text_saved': "Tekstblokk lagret som:\n{0}",
        'text_saved_voice': "Tekstblokk lagret",
        'text_deleted': "Tekstblokk slettet",
        'text_no_text_to_save': "Ingen tekst å lagre.",
        'text_no_templates': "Ingen tekstblokker funnet",
        'text_private_master_required': "Private blokker kan bare brukes hvis et masterpassord er opprettet.\n\nVil du opprette et masterpassord nå?",
        'text_filename': "Filnavn for tekstblokk (uten 'Text_' og '.txt'):",
        'text_filename_hint': "Eksempel: 'Telefon Hjem' lagres som 'Text_Telefon Hjem.txt'",
        'text_save_hint': "Tekstblokken lagres automatisk med formatering.",
        'text_guide_title': "Tekstinntasting - Veiledning",
        'text_delete_confirm': "Vil du virkelig slette tekstblokken?\n\nFil: {0}\nTekst: {1}...",
        'text_make_public': "Marker som offentlig",
        'text_make_private': "Marker som privat",
        'text_privacy_changed': "Personvernstatus endret",
        'text_private_always': "Private alltid synlige (innstilling)",
        'text_mode_required': "Aktiver først tekstmodus",
        'text_continue_editing': "Fortsett redigering – markør på slutten av teksten",
        'text_no_input': "Ingen tekst angitt – tekst forkastet",
        'save_dialog_question': "Hvordan vil du fortsette?",
        'text_save_question': "Lagre alle tekster og kryss, juster, fortsett redigering eller forkast?",
        'copy_cross': "Kryss kopiert",
        'paste_cross': "Kryss limt inn",
        'paste_text': "Tekst limt inn",
        'cross_discarded': "Kryss forkastet",
        'all_discarded': "Alt forkastet",
        'text_discarded': "Tekst forkastet",
        'no_texts_to_save': "Ingen tekster å lagre",
        'no_valid_texts': "Ingen gyldige tekster å lagre",
        'text_word_singular': "tekst",
        'text_word_plural': "tekster",
        'cross_word_singular': "kryss",
        'cross_word_plural': "kryss",
        'texts_saved_title': "Tekster lagret",
        'texts_crosses_saved': "{0} {1} og {2} {3} ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'texts_crosses_saved_voice': "{0} {1} og {2} {3} lagret.",
        'texts_saved': "{0} {1} ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'texts_saved_voice': "{0} {1} lagret.",
        'crosses_saved': "{0} {1} ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'crosses_saved_voice': "{0} {1} lagret.",
        'elements_saved': "{0} elementer ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'elements_saved_voice': "{0} elementer lagret.",
        'text_window_load_error': "Tekstvindu kunne ikke lastes",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Tekstinntasting og tekstblokker – Detaljert veiledning**

        **1. Sett inn og rediger tekst**
        - Høyreklikk på ønsket sted i dokumentet og velg "Sett inn tekst".
        - En dialog åpnes der du kan skrive inn og formatere teksten:
        • Skriftstørrelse, Fet, Kursiv, Understreket
        • Tekstfarge (fritt valg)
        • Gjennomsiktighet via glidebryter
        • Orddeling (forskjellige bredder, f.eks. sidebredde, smal, ingen ombryting)
        - Etter bekreftelse vises teksten på klikkstedet. Du kan flytte den med musen eller piltastene.
        - Dobbeltklikk på teksten åpner redigeringsmodus; ESC forlater den.

        **2. Administrer tekstblokker (maler)**
        - I tekstdialogen ser du til venstre en liste over alle lagrede tekstblokker.
        - **Lagre en blokk:** Skriv inn teksten, formater den og klikk på "💾 Lagre som blokk". Skriv inn et filnavn (uten endelse).
        - **Last inn en blokk:** Klikk på ønsket navn i listen. Teksten og formateringen overtas og kan justeres ved behov.
        - **Slett:** Høyreklikk på en blokk for å slette den eller endre personvernstatus.

        **3. Private tekstblokker (masterpassord)**
        - Hvis du har opprettet et masterpassord (under Innstillinger → Passordbehandling), kan du markere blokker som "private".
        - Aktiver avmerkingsboksen "Privat tekstblokk" i dialogen før du lagrer.
        - Private blokker vises bare i listen når du én gang per økt har skrevet inn masterpassordet ditt (autentisering via hengelåssymbolet eller ved første tilgang).
        - På den måten beskytter du konfidensielle tekstblokker mot uautorisert tilgang.

        **4. Sett inn kryss**
        - Via hurtigmenyen kan du også sette inn et grafisk kryss (f.eks. for avkrysningsbokser).
        - Størrelsen, strektykkelsen og fargen på kryss kan justeres globalt i innstillingene (meny "Innstillinger" → "Kryssinnstillinger").
        - Høyreklikk på et eksisterende kryss for å endre det individuelt.

        **5. Samlehandlinger**
        - Hvis du har plassert flere tekster eller kryss på én side, kan du lagre eller forkaste alle elementene samtidig via hurtigmenyen (høyreklikk i tekstmodus).
        - Ved lagring bygges alle elementene inn i PDF‑en og forblir som vektorgrafikk.

        **6. Tastaturgenveier i tekstmodus**
        - Piltaster: flytt element
        - Ctrl+Piltaster: større trinn
        - Enter: åpne lagre‑dialog (lagre alt / juster / forkast)
        - ESC: forkast gjeldende element
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Tekstinntasting og tekstblokker – Detaljert veiledning</strong></p>

        <p><strong>1. Sett inn og rediger tekst</strong></p>
        <ul>
        <li>Høyreklikk på ønsket sted i dokumentet og velg "Sett inn tekst".</li>
        <li>En dialog åpnes der du kan skrive inn og formatere teksten:<br/>
        • Skriftstørrelse, Fet, Kursiv, Understreket<br/>
        • Tekstfarge (fritt valg)<br/>
        • Gjennomsiktighet via glidebryter<br/>
        • Orddeling (forskjellige bredder, f.eks. sidebredde, smal, ingen ombryting)</li>
        <li>Etter bekreftelse vises teksten på klikkstedet. Du kan flytte den med musen eller piltastene.</li>
        <li>Dobbeltklikk på teksten åpner redigeringsmodus; ESC forlater den.</li>
        </ul>

        <p><strong>2. Administrer tekstblokker (maler)</strong></p>
        <ul>
        <li>I tekstdialogen ser du til venstre en liste over alle lagrede tekstblokker.</li>
        <li><strong>Lagre en blokk:</strong> Skriv inn teksten, formater den og klikk på "💾 Lagre som blokk". Skriv inn et filnavn (uten endelse).</li>
        <li><strong>Last inn en blokk:</strong> Klikk på ønsket navn i listen. Teksten og formateringen overtas og kan justeres ved behov.</li>
        <li><strong>Slett:</strong> Høyreklikk på en blokk for å slette den eller endre personvernstatus.</li>
        </ul>

        <p><strong>3. Private tekstblokker (masterpassord)</strong></p>
        <ul>
        <li>Hvis du har opprettet et masterpassord (under Innstillinger → Passordbehandling), kan du markere blokker som "private".</li>
        <li>Aktiver avmerkingsboksen "Privat tekstblokk" i dialogen før du lagrer.</li>
        <li>Private blokker vises bare i listen når du én gang per økt har skrevet inn masterpassordet ditt (autentisering via hengelåssymbolet eller ved første tilgang).</li>
        <li>På den måten beskytter du konfidensielle tekstblokker mot uautorisert tilgang.</li>
        </ul>

        <p><strong>4. Sett inn kryss</strong></p>
        <ul>
        <li>Via hurtigmenyen kan du også sette inn et grafisk kryss (f.eks. for avkrysningsbokser).</li>
        <li>Størrelsen, strektykkelsen og fargen på kryss kan justeres globalt i innstillingene (meny "Innstillinger" → "Kryssinnstillinger").</li>
        <li>Høyreklikk på et eksisterende kryss for å endre det individuelt.</li>
        </ul>

        <p><strong>5. Samlehandlinger</strong></p>
        <ul>
        <li>Hvis du har plassert flere tekster eller kryss på én side, kan du lagre eller forkaste alle elementene samtidig via hurtigmenyen (høyreklikk i tekstmodus).</li>
        <li>Ved lagring bygges alle elementene inn i PDF‑en og forblir som vektorgrafikk.</li>
        </ul>

        <p><strong>6. Tastaturgenveier i tekstmodus</strong></p>
        <ul>
        <li>Piltaster: flytt element</li>
        <li>Ctrl+Piltaster: større trinn</li>
        <li>Enter: åpne lagre‑dialog (lagre alt / juster / forkast)</li>
        <li>ESC: forkast gjeldende element</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Kryssinnstillinger",
        'cross_properties': "Krysegenskaper",
        'cross_size': "Størrelse (px):",
        'cross_line_width': "Strektykkelse:",
        'cross_color': "Farge:",
        'cross_choose_color': "Velg",
        'cross_fine_tuning': "Finjustering ved lagring (piksler)",
        'cross_offset_x': "X‑forskyvning:",
        'cross_offset_y': "Y‑forskyvning:",
        'cross_offset_x_tooltip': "Negative verdier flytter krysset til venstre ved lagring, positive til høyre",
        'cross_offset_y_tooltip': "Negative verdier flytter krysset oppover ved lagring, positive nedover",
        'cross_preview': "Forhåndsvisning",
        'cross_save': "Bruk innstillinger",
        'cross_customized': "Kryss tilpasset",
        'cross_settings_applied': "Kryssinnstillinger lagret.\nStørrelse: {0}px, Strektykkelse: {1}px\n{2}",
        'cross_updated_count': "{0} eksisterende kryss ble oppdatert.",
        'cross_no_crosses': "Ingen eksisterende kryss funnet.",
        'cross_settings_applied_all': "Kryssinnstillinger brukt på alle {0} kryss",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Signaturinnstillinger",
        'signature_1': "Signatur 1",
        'signature_2': "Signatur 2",
        'signature_select': "Velg signatur",
        'signature_add': "➕ Legg til ny signatur...",
        'signature_size': "Størrelse for signatur {0} (%):",
        'signature_common': "Generelle innstillinger",
        'signature_timestamp': "Legg til tidsstempel automatisk",
        'signature_location': "Standardsted:",
        'signature_timestamp_size': "Skriftstørrelse for tidsstempel:",
        'signature_no_files': "-- Ingen signaturer funnet --",
        'signature_insert': "Sett inn signatur",
        'signature_insert_1': "Sett inn signatur 1",
        'signature_insert_2': "Sett inn signatur 2",
        'signature_customize': " Tilpass signatur",
        'signature_discard': " Forkast denne signaturen",
        'signature_save_all': " Lagre alle signaturer",
        'signature_discard_all': " Forkast alle signaturer",
        'signature_guide_title': "Signaturer - Veiledning",
        'signature_guide': """
📝 Signaturer - Hurtigveiledning

- Opprett masterpassord
- Konfigurer signaturer i menyen Innstillinger
  (størrelse, tidsstempel ...)
- Sett inn med HØYREKLIKK på ønsket sted
  (masterpassord kreves én gang per økt)
- Flytt signaturen med musen eller piltastene
- Flere signaturer kan settes inn etter hverandre
- Hver signatur kan tilpasses individuelt
- Forkast en enkelt signatur
- Lagre / forkast alle signaturer på én gang
- Alternativt kan menylinjen brukes.
        """,
        'signature_placeholder': "Ingen forhåndsvisning tilgjengelig",
        'signature_info': "Signatur {0}: {1}×{2} px ({3}% av {4}×{5})",
        'signature_info_placeholder': "Innstillinger for signatur {0}",
        'signature_inserted': "Signatur {0} satt inn på side {1}",
        'signature_deleted': "Signatur slettet",
        'signature_copied': "Signatur kopiert",
        'signature_pasted': "Signatur {0} limt inn",
        'signature_saved': "{0} signaturer ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'signature_saved_voice': "{0} signaturer lagret",
        'mode_replace_signature_format': "Avslutt modus og sett inn signatur {0}",
        'mode_conflict_voice_signature': "{0}‑modus er aktiv. Avslutt og sett inn signatur?",
        'signature_not_configured': "Signatur {0} ikke konfigurert",
        'signature_file_not_found': "Signaturfil ikke funnet",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Ingen kopiert signatur tilgjengelig",
        'no_signatures_to_save': "Ingen signaturer å lagre",
        'signature_save_question': "Lagre alle signaturer, juster eller forkast denne?",
        'signatures_saved_title': "Signaturer lagret",
        'signatures_saved': "{0} signaturer ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'signatures_saved_voice': "{0} signaturer lagret.",
        'all_signatures_discarded': "Alle signaturer forkastet",
        'signature_settings_saved': "Signaturinnstillinger lagret",
        'signature_cancelled': "Signatur forkastet",
        'signature_active_title': "Signatur aktiv",
        'signature_replace_question': "En signatur er allerede aktiv.\n\nVil du erstatte den gjeldende signaturen?",
        'signature_replace': "Erstatt signatur",
        'signature_replace_voice': "Erstatt gjeldende signatur eller avbryt?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Bildeinnstillinger",
        'image_common': "Generelle bildeinnstillinger",
        'image_keep_aspect': "Bevar sideforhold ved dragging",
        'image_default_size': "Standardstørrelse (%):",
        'image_dark_invert': "Inverter bilder i mørk modus",
        'image_dark_invert_tooltip': "Aktivert: bilder inverteres for bedre synlighet",
        'image_fine_tuning': "Finjustering (piksler)",
        'image_offset_x': "X‑forskyvning:",
        'image_offset_y': "Y‑forskyvning:",
        'image_offset_x_tooltip': "Negative verdier flytter bildet til venstre ved lagring, positive til høyre",
        'image_offset_y_tooltip': "Negative verdier flytter bildet oppover ved lagring, positive nedover",
        'image_select': "Velg bilde",
        'image_insert': "Sett inn bilde",
        'image_customize': " Tilpass bilde",
        'image_aspect': " Bevar sideforhold",
        'image_discard': " Forkast dette bildet",
        'image_save_all': " Lagre alle bilder",
        'image_discard_all': " Forkast alle bilder",
        'image_filter': "Bilder",
        'image_guide_title': "Sett inn bilde - Veiledning",
        'image_guide': """
📷 Sett inn bilde i PDF - Hurtigveiledning:

1. Høyreklikk på ønsket sted
2. "Sett inn bilde" → velg bilde
3. Plasser bildet: dra med musen
4. Juster størrelsen: dra i hjørner/kanter
5. Bevar sideforhold: [A]‑tast
6. Ytterligere justeringer: høyreklikk på bildet

Tips: Du kan justere innstillingene i hurtigmenyen.
        """,
        'image_inserted': "Bilde {0} satt inn på side {1}",
        'image_deleted': "Bilde forkastet",
        'image_copied': "Bilde kopiert",
        'image_pasted': "Bilde limt inn",
        'image_saved': "{0} bilder ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'image_saved_voice': "{0} bilder lagret",
        'image_aspect_on': "aktivert",
        'image_aspect_off': "deaktivert",
        'image_aspect_toggle': "Bevar sideforhold {0}",
        'image_reset': "Bilde tilbakestilt til original størrelse",
        'image_replaced': "Bilde erstattet",
        'image_invalid': "Ikke et gyldig bilde",
        'mode_replace_image': "Sett inn bilde",
        'mode_conflict_voice_image': "{0}‑modus er aktiv. Avslutt og sett inn bilde?",
        'image_active_title': "Bilde aktivt",
        'image_replace_question': "Et bilde er allerede aktivt.\n\nVil du erstatte det gjeldende bildet?",
        'image_replace': "Erstatt bilde",
        'image_replace_voice': "Erstatt gjeldende bilde eller avbryt?",
        'image_filter_all': "Bilder (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Alle filer (*.*)",
        'no_copied_image': "Ingen kopiert bilde tilgjengelig",
        'image_discarded': "Bilde forkastet",
        'image_save_question': "Lagre alle bilder, juster eller forkast dette?",
        'no_images_to_save': "Ingen bilder å lagre",
        'no_valid_images': "Ingen gyldige bilder å lagre",
        'images_saved_title': "Bilder lagret",
        'images_saved': "{0} bilder ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'images_saved_voice': "{0} bilder lagret.",
        'all_images_discarded': "Alle bilder forkastet",
        'image_settings_updated': "Bildeinnstillinger oppdatert",
        'image_replace_title': "Velg nytt bilde",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Forminnstillinger",
        'form_basic': "Grunninnstillinger",
        'form_default_type': "Standardformtype:",
        'form_rectangle': "Rektangel",
        'form_ellipse': "Ellipse",
        'form_line': "Linje",
        'form_arrow': "Pil",
        'form_line_width': "Strektykkelse:",
        'form_colors': "Farger",
        'form_line_color': "Linjefarge:",
        'form_fill_color': "Fyllfarge:",
        'form_choose_color': "Velg",
        'form_transparent': "Gjennomsiktig bakgrunn (kun linje)",
        'form_filled': "fylt",
        'form_dark_mode': "Mørk modus",
        'form_dark_invert': "Inverter farger i mørk modus",
        'form_fine_tuning': "Finjustering (piksler)",
        'form_offset_x': "X‑forskyvning:",
        'form_offset_y': "Y‑forskyvning:",
        'form_offset_x_tooltip': "Negative verdier flytter formen til venstre ved lagring, positive til høyre",
        'form_offset_y_tooltip': "Negative verdier flytter formen oppover ved lagring, positive nedover",
        'form_preview': "Forhåndsvisning",
        'form_insert': "Sett inn form",
        'form_rectangle_insert': "Rektangel",
        'form_ellipse_insert': "Ellipse/Sirkel",
        'form_line_insert': "Linje (2 klikk)",
        'form_arrow_insert': "Pil (2 klikk)",
        'form_customize': " Tilpass form",
        'form_transparent_toggle': " Gjennomsiktig bakgrunn",
        'form_discard': " Forkast denne formen",
        'form_save_all': " Lagre alle former",
        'form_discard_all': " Forkast alle former",
        'form_guide_title': "Sett inn form - Veiledning",
        'form_guide': """
📐 Sett inn form i PDF - Hurtigveiledning:

1. Velg formtype (rektangel, ellipse, linje, pil)
2. Klikk på posisjonen
   - For rektangel/ellipse: ett klikk plasserer formen
   - For linje/pil: to klikk for start‑ og sluttpunkt
3. Plasser formen: dra med musen
4. Juster størrelsen: dra i hjørner/kanter
5. Lagre formen: Enter
6. Forkast formen: ESC
7. Ytterligere justeringer: høyreklikk på formen

Tips: Du kan justere innstillingene i hurtigmenyen.
        """,
        'form_inserted': "{0} satt inn på side {1}",
        'form_deleted': "Form slettet",
        'form_copied': "Form kopiert",
        'form_pasted': "Form limt inn",
        'form_saved': "{0} former ble satt inn i PDF‑en.\n\nPDF lastet på nytt...",
        'form_saved_voice': "{0} former lagret",
        'form_reset': "Form tilbakestilt til standardstørrelse",
        'form_transparent_on': "aktivert",
        'form_transparent_off': "deaktivert",
        'form_transparent_toggled': "Gjennomsiktig bakgrunn {0}",
        'form_line_cancel': "Linjetegning avbrutt",
        'form_second_click': "Klikk nå på sluttpunktet for {0}",
        'mode_replace_form': "Sett inn form",
        'mode_conflict_voice_form': "{0}‑modus er aktiv. Avslutt og sett inn en form?",
        'form_settings_updated': "Forminnstillinger oppdatert",
        'form_unknown': "Form",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klikk på startposisjonen",
        'form_line_guide_2': "2. Klikk på sluttposisjonen",
        'form_line_guide_3': "Linjen vil bli tegnet mellom de to punktene.",
        'form_line_status_1': "Venter på første klikk...",
        'form_line_status_2': "Første punkt angitt: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Klikk nå på sluttpunktet...",
        'form_line_status_4': "Begge punkter angitt.\nKlikk på 'Fullfør' for å lagre.",
        'form_line_reset': "Tilbakestill",
        'form_line_finish': "Fullfør",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopier (Cmd+C)",
        'paste': "Lim inn (Cmd+V)",
        'copied': "Kopiert: {0}",
        'no_element_to_copy': "Ingen element valgt å kopiere",
        'no_copied_data': "Ingen kopierte data tilgjengelig",
        'no_valid_position': "Ingen gyldig posisjon å lime inn på",
        'copy_text': "Tekst kopiert",
        'copy_image': "Bilde kopiert",
        'copy_form': "Form kopiert",
        'copy_signature': "Signatur kopiert",
        'element_text': "tekst",
        'element_image': "bilde",
        'element_form': "form",
        'element_signature': "signatur",
        'element_unknown': "element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Moduskonflikt",
        'mode_conflict_message': "Modusen '{0}' er allerede aktiv.\n\nVil du avslutte den og {1}?",
        'mode_replace': "Avslutt modus og {0}",
        'mode_cancel': "Avbryt",
        'mode_replace_text': "sett inn tekst",
        'mode_replace_cross': "sett inn kryss",
        'mode_replace_signature': "sett inn signatur",
        'mode_replace_image': "sett inn bilde",
        'mode_replace_form': "sett inn form",
        'mode_conflict_voice': "{0}‑modus er aktiv. Avslutt og sett inn tekst?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Tekstinntasting",
        'active_mode_signature': "Signatur",
        'active_mode_image': "Bilde",
        'active_mode_form': "Form",
        'active_mode_and': " og ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Sett inn",                    # Hauptmenü
        'insert_another_text': "Sett inn tekst",          # Vereinfacht
        'insert_another_cross': "Sett inn kryss",        # Vereinfacht
        'insert_another_signature_1': "Signatur 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Signatur 2",      # Untermenü-Eintrag
        'insert_another_image': "Sett inn bilde",         # Vereinfacht
        'insert_another_form_rect': "Rektangel",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Linje (2 klikk)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Pil (2 klikk)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Lagre {0}",
        'save_dialog_message': "{0} vil bli lagret på side {1}.\n\nHvordan vil du fortsette?",
        'save_all': "Lagre alle {0}",
        'save_single': "Lagre {0}",
        'save_customize': "Juster {0}",
        'save_discard': "Forkast denne {0}",
        'save_continue': "Fortsett redigering",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Gå til side {0}",
        'context_rotate': " Roter side {0}",
        'context_delete': " Slett side {0}",
        'context_export': " Eksporter side {0}",
        'context_mark_as': " Merk side som...",
        'context_mark_empty': " Tom side",
        'context_unmark_empty': " Ikke lenger tom",
        'context_mark_export': " Merk for eksport",
        'context_unmark_export': " Ikke eksporter",
        'context_batch_actions': " Samlehandlinger",
        'context_batch_delete_empty': " Slett alle {0} tomme sider",
        'context_batch_export_single': " Alle {0} sider (én fil)",
        'context_batch_export_split': " Alle {0} sider (separate)",
        'context_drag_start': " Start dra og slipp",
        'context_drag_stop': " Stopp dra og slipp",
        'context_insert': " Sett inn",
        'context_insert_pages': " Sett inn sider",
        'context_zoom': "Zoom",
        'discard_mixed': "Forkast {0} {1} og {2} {3}",
        'save_mixed': "Lagre {0} {1} og {2} {3}",
        'discard_texts': "Forkast {0} tekster",
        'discard_text_single': "Forkast 1 tekst",
        'save_texts': "Lagre {0} tekster",
        'save_text_single': "Lagre 1 tekst",
        'discard_crosses': "Forkast {0} kryss",
        'discard_cross_single': "Forkast 1 kryss",
        'save_crosses': "Lagre {0} kryss",
        'save_cross_single': "Lagre 1 kryss",
        'discard_signatures': "Forkast {0} signaturer",
        'save_signature_single': "Lagre 1 signatur",
        'save_signatures': "Lagre {0} signaturer",
        'discard_images': "Forkast {0} bilder",
        'save_image_single': "Lagre 1 bilde",
        'save_images': "Lagre {0} bilder",
        'discard_forms': "Forkast {0} former",
        'save_form_single': "Lagre 1 form",
        'save_forms': "Lagre {0} former",
        'cross_discard': "Forkast dette krysset",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Eksport‑ / importinformasjon",
        'export_what': "📋 Hva eksporteres?",
        'export_general': "Generelle innstillinger",
        'export_general_items': "• Taleutdata (på/av, hastighet)\n• Mørk/lys modus\n• Sikkerhetskopieringsinnstillinger\n• OCR‑innstillinger",
        'export_image_form': "Bilde‑ og forminnstillinger",
        'export_image_form_items': "• Bildeinnstillinger (sideforhold, standardstørrelse)\n• Forminnstillinger (strektykkelse, farger)\n• Signaturinnstillinger (stier, størrelser, tidsstempel)",
        'export_passwords': "Passorddatabase",
        'export_passwords_items': "• Alle lagrede PDF‑passord\n• Valgfritt kryptert eller dekryptert",
        'export_master': "Masterpassordinnstillinger",
        'export_master_items': "• Masterpassord‑hash\n• Innstillinger for signaturer/tekstblokker",
        'export_signatures': "Signaturer og tekstblokker",
        'export_signatures_items': "• Alle bildefiler (signaturer)\n• Alle tekstblokker med formatering\n• Private/offentlige markeringer",
        'export_import_warning': "⚠️ Viktige merknader",
        'export_import_note': "• Ved import overskrives ALLE nåværende innstillinger\n• En omstart av applikasjonen er nødvendig\n• Eksisterende signaturer/tekstblokker erstattes",
        'export_master_note': "• Hvis et masterpassord er angitt, kan du velge:\n  - Dekryptert (passord i klartekst)\n  - Kryptert (kun lesbart med masterpassord)",
        'export_security': "• Den eksporterte ZIP‑filen inneholder konfidensielle data\n• Oppbevar den sikkert (f.eks. kryptert USB‑minne)\n• Hvis filen mistes, er passordene uopprettelig tapt",
        'export_format': "📁 Eksportformat",
        'export_format_desc': "Innstillingene lagres i én enkelt ZIP‑fil:",
        'export_filename': "PDFDarkView_Innstillinger_ÅÅÅÅMMDD_TTMMSS.zip",
        'export_success': "Innstillinger eksportert",
        'export_failed': "Eksport mislyktes",
        'export_import_question': "Vil du starte applikasjonen på nytt nå?",
        'export_password_question': "Et masterpassord er angitt.\n\nVil du eksportere passordene dekryptert?\n(ellers eksporteres de kryptert)",
        'export_decrypt': "Eksporter dekryptert",
        'export_encrypt': "Eksporter kryptert",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Om PDF Dark View",
        'info_version': "Versjon",
        'info_author': "Utviklet av Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Om",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> er en tilgjengelig PDF-viser som er spesielt utviklet for personer med synshemming.</p>

            <p><strong>Kjernefunksjoner:</strong></p>
            <ul>
                <li>Kontrastrik, tilpassbar grensesnitt</li>
                <li>Full tastaturkontroll</li>
                <li>Integrert taleutgang</li>
                <li>OCR for skannede dokumenter</li>
                <li>Omfattende redigeringsverktøy</li>
            </ul>

            <p>Mer enn 50 språk støttes – slik at PDF-er er tilgjengelige for alle.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funksjoner",
        'info_features_intro': "PDF Dark View tilbyr deg følgende muligheter:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Visning og navigasjon</strong> – Mørk/lys modus, bla gjennom sider, zoom, hopp til side</li>
            <li><strong>OCR (tekstgjenkjenning)</strong> – Gjør skannede dokumenter søkbare og kopierbare</li>
            <li><strong>Redigering</strong> – Sett inn tekst, kryss, signaturer, bilder og former</li>
            <li><strong>Sidebehandling</strong> – Slett, ekstraher, sett inn, flytt via dra og slipp</li>
            <li><strong>Eksport</strong> – Til Word, Pages eller som tekst</li>
            <li><strong>Sikkerhet</strong> – Passordbeskyttelse og -administrasjon</li>
            <li><strong>Tilgjengelighet</strong> – Taleutgang, tastaturkontroll, høy kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Betjening",
        'info_accessibility': "♿ Tilgjengelighet – full tastaturkontroll",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Generelt</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Åpne PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Søk</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Bytt mørk/lys modus</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Skriv ut</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Avslutt</div>

        <div class="shortcut-cat">📖 Navigasjon</div>
        <div class="shortcut-row"><kbd>Piltastene</kbd> Bla side for side</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Gå til side</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Første side</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Siste side</div>

        <div class="shortcut-cat">✏️ Redigering</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Sett inn tekst</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Slett sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Ekstraher sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Sett inn sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Flytt sider</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Roter side</div>

        <div class="shortcut-cat">🖼️ Flytt elementer</div>
        <div class="shortcut-row"><kbd>Piltastene</kbd> Flytt tekst/bilde/signatur</div>
        <div class="shortcut-row"><kbd>Ctrl+Piltastene</kbd> Større trinn</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Lagre</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Forkast</div>

        <div class="shortcut-cat">🗣️ Taleutgang</div>
        <div class="shortcut-row"><kbd>F2</kbd> Slå taleutgang på/av</div>
        """,
        'info_contextmenu': "📌 Viktig: Alle funksjoner er også tilgjengelige via hurtigmenyen (høyre museknapp)!",
        'info_accessibility_hint': "💡 Tips: Taleutgang (F2) letter orienteringen og gir tilbakemelding om menyer og dialoger.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lisens & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Informasjon i henhold til § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Tyskland<br>
        E-post: binhdiez64@gmail.com<br>
        Ansvarlig for innholdet: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Ansvarsfraskrivelse</strong><br>
        Programvaren er utviklet med største forsiktighet. Det gis ingen garanti for riktighet, fullstendighet og funksjonalitet. Bruk skjer på egen risiko.<br><br>

        <strong>📄 MIT-lisens (privat bruk)</strong><br>
        Opphavsrett (c) 2026 Toralf Schulz (BinhDiez)<br>
        Tillatt: gratis bruk, private endringer, personlige kopier.<br>
        Ikke tillatt: salg, kommersiell bruk, fjerning av opphavsrettsmerknader.<br><br>

        <strong>🔧 Tredjepartskomponenter</strong><br>
        Denne programvaren inneholder komponenter under GPL, AGPL, Apache 2.0, BSD og MIT-lisenser.<br>
        Ved videre distribusjon må de respektive lisensvilkårene overholdes.<br><br>

        <strong>🌐 Åpen kildekode</strong><br>
        Kildekoden er tilgjengelig og kan sees, endres og distribueres videre i samsvar med de respektive lisensvilkårene.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Takk til",
        'info_credits': "Takk til open-source-miljøet",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-behandling</li>
            <li><strong>PyQt5</strong> – Grafisk grensesnitt</li>
            <li><strong>Tesseract OCR</strong> – Tekstgjenkjenning</li>
            <li><strong>OCRmyPDF</strong> – OCR-integrasjon</li>
            <li><strong>python-docx</strong> – Word-eksport</li>
            <li><strong>qtawesome</strong> – Ikoner</li>
            <li><strong>DeepSeek</strong> – Støtte for oversettelser (50+ språk)</li>
            <li><strong>Alle brukere</strong> – For verdifull tilbakemelding</li>
            <li><strong>Open-source-miljøet</strong> – For gode biblioteker</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Språk",
        'info_languages_header': "🌍 Språkstøtte",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View støtter for øyeblikket <strong>62 språk</strong> – slik at programvaren kan brukes tilgjengelig over hele verden.</p>

            <p><strong>📖 Fullstendig språkliste (Status: mars 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albansk (Shqip)</li>
                    <li>🇩🇿 Arabisk (العربية)</li>
                    <li>🇮🇩 Balinesisk (Basa Bali)</li>
                    <li>🇧🇩 Bengalsk (বাংলা)</li>
                    <li>🇲🇲 Burmesisk (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnisk (Bosanski)</li>
                    <li>🇧🇬 Bulgarsk (Български)</li>
                    <li>🇨🇳 Kinesisk (中文)</li>
                    <li>🇩🇰 Dansk (Dansk)</li>
                    <li>🇩🇪 Tysk (Deutsch)</li>
                    <li>🇬🇧 Engelsk (English)</li>
                    <li>🇪🇪 Estisk (Eesti)</li>
                    <li>🇫🇮 Finsk (Suomi)</li>
                    <li>🇫🇷 Fransk (Français)</li>
                    <li>🇬🇷 Gresk (Ελληνικά)</li>
                    <li>🇮🇱 Hebraisk (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatisk (Hrvatski)</li>
                    <li>🇭🇺 Ungarsk (Magyar)</li>
                    <li>🇮🇩 Indonesisk (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irsk (Gaeilge)</li>
                    <li>🇮🇸 Islandsk (Íslenska)</li>
                    <li>🇮🇹 Italiensk (Italiano)</li>
                    <li>🇯🇵 Japansk (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreansk (한국어)</li>
                    <li>🇱🇦 Laotisk (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvisk (Latviešu)</li>
                    <li>🇱🇹 Litauisk (Lietuvių)</li>
                    <li>🇱🇺 Luxembourgsk (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaysisk (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolsk (Монгол)</li>
                    <li>🇳🇵 Nepalsk (नेपाली)</li>
                    <li>🇳🇱 Nederlandsk (Nederlands)</li>
                    <li>🇳🇴 Norsk (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persisk (فارسی)</li>
                    <li>🇵🇱 Polsk (Polski)</li>
                    <li>🇵🇹 Portugisisk (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumensk (Română)</li>
                    <li>🇷🇺 Russisk (Русский)</li>
                    <li>🇸🇪 Svensk (Svenska)</li>
                    <li>🇷🇸 Serbisk (Српски)</li>
                    <li>🇸🇰 Slovakisk (Slovenčina)</li>
                    <li>🇸🇮 Slovensk (Slovenščina)</li>
                    <li>🇪🇸 Spansk (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Tsjekkisk (Čeština)</li>
                    <li>🇹🇷 Tyrkisk (Türkçe)</li>
                    <li>🇺🇦 Ukrainsk (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamesisk (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddisch (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Legg til egne språk:</strong><br>
                Ønsker du et språk som ikke er inkludert ennå? Bare plasser din egen ordbokfil (<code>sprache_xx.py</code>) ved siden av applikasjonen – programvaren vil gjenkjenne den automatisk. Hvis du er interessert i en spesifikk oversettelse, kontakt meg gjerne.
            </div>

            <p><strong>🙏 Spesiell takk:</strong> DeepSeek for støtten med å oversette alle ordbøker til 62 språk.</p>

            <p>📧 Kontakt for oversettelser: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Feil",
        'error_occurred': "En feil oppstod",
        'error_pdf_load': "Feil ved lasting av PDF",
        'error_pdf_save': "Feil ved lagring av PDF",
        'error_ocr': "Feil under tekstgjenkjenning",
        'error_no_pdf': "Ingen PDF lastet",
        'error_page_not_found': "Side ikke funnet",
        'error_invalid_range': "Ugyldig sideintervall",
        'error_file_not_found': "Fil ikke funnet",
        'error_permission': "Ingen tillatelse",
        'error_unknown': "Ukjent feil",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Vellykket",
        'success_operation': "Handlingen lyktes",
        'success_saved': "Lagret",
        'success_exported': "Eksportert",
        'success_imported': "Importert",
        'success_deleted': "Slettet",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Bekreftelse",
        'confirm_yes': "Ja",
        'confirm_no': "Nei",
        'confirm_ok': "OK",
        'confirm_cancel': "Avbryt",
        'confirm_delete': "Slett",
        'confirm_overwrite': "Overskriv",
        'confirm_continue': "Fortsett",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Laster PDF...",
        'progress_saving': "Lagrer PDF...",
        'progress_exporting': "Eksporterer PDF...",
        'progress_processing': "Behandler...",
        'progress_wait': "Vennligst vent...",
        'progress_preparing': "Forbereder...",
        'progress_finalizing': "Fullfører...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Hvit",
        'color_black': "Svart",
        'color_red': "Rød",
        'color_green': "Grønn",
        'color_blue': "Blå",
        'color_yellow': "Gul",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Oransje",
        'color_gray': "Grå",
        'color_custom': "Fargevelger",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fil",
        'menu_edit': "&Rediger",
        'menu_view': "&Vis",
        'menu_tools': "&Verktøy",
        'menu_settings': "&Innstillinger",
        'menu_help': "&Hjelp",
        'menu_language': "🌐 Språk",
        'menu_guides': "&Veiledninger",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Åpne",
        'file_save_as': "&Lagre som...",
        'file_protect': "&Beskytt dokument...",
        'file_export': "&Eksporter",
        'file_export_pages': "Eksporter som Pages",
        'file_export_word': "Eksporter som DOCX",
        'file_export_text': "Eksporter som TXT",
        'file_print_now': "&Skriv ut nå",
        'file_print': "&Skriv ut",
        'file_close': "&Lukk",
        'file_quit': "&Avslutt",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Søk",
        'edit_ocr': " Kjør OCR",
        'edit_rotate': "&Roter side",
        'edit_rotate_all': "&Roter alle sider",
        'edit_delete_pages': "&Slett sider",
        'edit_extract_pages': "&Trekk ut sider",
        'edit_insert_pages': "&Sett inn sider",
        'edit_move_pages': "&Flytt sider",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Sett inn tekst og kryss",
        'text_insert': " Sett inn tekst",
        'cross_insert': " Sett inn kryss",
        'text_customize': " Tilpass tekst",
        'cross_customize': " Tilpass dette krysset",
        'cross_customize_all': " Tilpass alle kryss",
        'text_discard': " Forkast denne teksten/dette krysset",
        'text_discard_all': " Forkast alle tekster og kryss",
        'text_save_all': " Lagre alle tekster og kryss",
        'text_guide': " Tekstinntasting / tekstblokker - Veiledning",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Sett inn signatur",
        'signature_settings_menu': " Innstillinger...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Sett inn bilde",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Sett inn former",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Vis tekstvindu",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Sidebredde (standard)",
        'view_zoom_two': "&To sider",
        'view_zoom_overview': "&Oversikt (flere sider)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Tilgjengelighet",
        'settings_voice': "Taleutdata",
        'settings_voice_tooltip': "supplerer skjermleseres taleutdata med ekstra informasjon",
        'settings_signature': "&Signaturinnstillinger",
        'settings_password': "&Passordbehandling",
        'settings_backup': "Opprett sikkerhetskopi før endringer",
        'settings_export_import': "&Eksporter / importer innstillinger",
        'settings_export': "&Eksporter alle innstillinger...",
        'settings_import': "&Importer alle innstillinger...",
        'settings_export_info': "&Hva eksporteres?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "på",
        'voice_off': "av",
        'voice_toggle': "Taleutdata {0}",
        'voice_speed': "Hastighet {0} prosent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Verktøy ikke funnet:\n{0}\n\nBASE_DIR: {1}\nSørg for at PDF‑verktøyene er installert i katalogen {1}.",
        'tool_started': "{0} startet",
        'tool_start_failed': "Kunne ikke starte",
        'process_error_failed_to_start': "Prosessen kunne ikke startes. Finnes filen?",
        'process_error_crashed': "Prosessen krasjet under oppstart.",
        'process_error_timeout': "Prosess‑tidsavbrudd nådd.",
        'process_error_write': "Skrivefeil til prosessen.",
        'process_error_read': "Lesefeil fra prosessen.",
        'process_error_unknown': "Ukjent prosessfeil",
        'process_command': "Kommando",
        'process_normal_exit': "avsluttet normalt",
        'process_crashed': "krasjet",
        'process_nonzero_exit': "{0} avsluttet med feilkode {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Avbryter...",
        'move_cancelling': "Flytting avbrytes",
        'opening_pdf': "Åpner PDF...",
        'loading_document': "Laster dokument...",
        'pdf_opened': "PDF åpnet",
        'pages_found_moving': "{0} sider funnet, {1} skal flyttes",
        'creating_backup': "Oppretter sikkerhetskopi...",
        'backup_description': "Sikkerhetskopierer originalfil...",
        'backup_saved_as': "Sikkerhetskopiert som: {0}",
        'error_format': "Feil: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Søk tilbakestilt",
        'page_header_simple': "=== Side {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Passordbehandling – Veiledning",
        'password_guide_voice': "Veiledning for passordbehandling. Les merknadene.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Passordbehandling – Detaljert veiledning</strong></p>

        <p><strong>1. Passordbeskyttelse for PDF‑filer</strong></p>
        <ul>
        <li>Når du åpner en passordbeskyttet PDF, vises en dialog der du kan skrive inn passordet.</li>
        <li>Du kan lagre passordet kryptert, slik at du ikke trenger å skrive det inn hver gang (avmerkingsboks "Lagre passord").</li>
        <li>Med knappen "Fjern passord" kan du opprette en dekryptert kopi av PDF‑en og slette passordet fra databasen.</li>
        </ul>

        <p><strong>2. Masterpassord</strong></p>
        <ul>
        <li>Masterpassordet beskytter tilgangen til alle lagrede PDF‑passord.</li>
        <li><strong>Opprett:</strong> Gå til "Innstillinger → Passordbehandling → Masterpassordinnstillinger" og klikk på "Opprett masterpassord". Velg et sterkt masterpassord (minst 8 tegn).</li>
        <li><strong>Endre:</strong> Etter vellykket autentisering kan du endre masterpassordet.</li>
        <li><strong>Fjern:</strong> Hvis du fjerner masterpassordet, slettes ALLE lagrede passord uopprettelig. Du kan eksportere en sikkerhetskopi først.</li>
        <li>Én gang per økt må du autentisere deg med masterpassordet for å få tilgang til beskyttede funksjoner (f.eks. vise passord).</li>
        </ul>

        <p><strong>3. Passordbehandling (liste)</strong></p>
        <ul>
        <li>Under "Innstillinger → Passordbehandling" åpnes en tabell over alle lagrede PDF‑filer med deres krypterte passord.</li>
        <li><strong>Uten masterpassord:</strong> Du kan bare slette oppføringer – passordene forblir skjult.</li>
        <li><strong>Med masterpassord (autentisert):</strong> Du kan vise, kopiere, eksportere og slette passord.</li>
        <li><strong>Eksport:</strong> Velg et format (JSON, CSV, TXT) og lagre listen. Hvis et masterpassord er angitt, kan du velge om passordene skal eksporteres i klartekst eller fortsatt kryptert.</li>
        <li><strong>Import:</strong> En tidligere eksportert ZIP‑fil med alle innstillinger (inkludert passord) kan importeres via "Innstillinger → Eksporter / importer innstillinger". OBS: Eksisterende data overskrives!</li>
        </ul>

        <p><strong>4. Passordgenerator</strong></p>
        <ul>
        <li>I passorddialogen (f.eks. ved beskyttelse av en PDF) finner du en terningknapp 🎲 til høyre for inntastingsfeltet.</li>
        <li>Klikk på den for å åpne passordgeneratoren. Du kan stille inn lengde, tegnsett (store bokstaver, små bokstaver, siffer, symboler) og et skilletegn for bedre lesbarhet.</li>
        <li>Det genererte passordet kan brukes direkte og kopieres ved behov.</li>
        </ul>

        <p><strong>5. Viktige sikkerhetsmerknader</strong></p>
        <ul>
        <li>Lagrede passord lagres kryptert med AES‑256. Nøkkelen utledes fra masterpassordet ditt (hvis angitt) eller fra en fast verdi (uten masterpassord).</li>
        <li>Uten masterpassord er passordene riktignok kryptert, men nøkkelen finnes innebygd i programmet – en angriper med tilgang til filene dine kan dekryptere dem. Derfor anbefaler vi på det sterkeste å bruke et masterpassord.</li>
        <li>Passorddatabasen ligger i mappen `Data/passwords.json`. Ta jevnlige sikkerhetskopier, spesielt før du fjerner masterpassordet.</li>
        <li>Hvis masterpassordet mistes, er alle lagrede passord uopprettelig tapt.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Inverteringsmodus",
        'invert_mode_classic': "Klassisk (inverter alle farger)",
        'invert_mode_smart': "Smart (inverter kun lysstyrke)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Gråtone terskelverdi",
        'gray_threshold_10': "10% (streng)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (myk)",
        'threshold_changed': "Terskelverdi satt til {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Gråtone terskelverdi – Forklaring",
        'threshold_guide_text': "Gråtone terskelverdien bestemmer hvilke piksler i smart mørk modus som anses som 'grå' og inverteres.\n\n"
                                "• En lav verdi (10%) inverterer bare nesten perfekte gråtoner – fargede elementer forblir fullstendig bevart.\n"
                                "• En høy verdi (50%) inverterer også lett fargede piksler – dette øker kontrasten, men kan forvrenge farger.\n\n"
                                "Den optimale verdien avhenger av dokumentet. For rene tekstdokumenter er 30–40% ofte ideelt, for fargede grafikker heller 10–20%.\n\n"
                                "Du kan justere verdien når som helst via menyen 'Innstillinger' – PDF-en vil bli lastet på nytt umiddelbart.\n\n"
                                "Merk:\n* Bilder og fotografier kan bare vises korrekt i lys modus!\n* Inverteringsinnstillingene vises bare når mørk modus er aktivert.",
        'threshold_guide_voice': "Gråtone terskelverdien bestemmer hvor sterkt den smarte mørke modusen griper inn. En lav verdi sparer farger, en høy verdi øker kontrasten.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Åpner PDF...",
        'progress_loading_document': "Laster dokument...",
        'progress_pdf_opened': "PDF åpnet",
        'progress_creating_backup': "Oppretter sikkerhetskopi...",
        'progress_backup_description': "Sikrer originalfil...",
        'progress_backup_created': "Sikkerhetskopi opprettet",
        'progress_backup_saved_as': "Lagret som: {0}",
        'progress_analyzing_start': "Starter analyse...",
        'progress_searching_empty': "Søker etter tomme sider...",
        'progress_page_empty': "Side {0} er tom",
        'progress_page_keep': "Behold side {0}",
        'progress_analysis_complete': "Analyse fullført",
        'progress_empty_found': "Fant {0} tomme sider",
        'progress_current_page': "Gjeldende side",
        'progress_mark_delete': "Markeres for sletting",
        'progress_range_selected': "Sideområde {0}-{1}",
        'progress_deleting_pages': "Sletter {0} sider",
        'progress_creating_new_pdf': "Oppretter ny PDF...",
        'progress_transferring_pages': "Overfører sider",
        'progress_keeping_page': "Side {0} vil bli beholdt ({1}/{2})",
        'progress_saving_pdf': "Lagrer PDF...",
        'progress_optimizing': "Optimaliserer filstørrelse...",
        'progress_finalizing': "Fullfører...",
        'progress_new_size': "Ny størrelse: {0:.2f} MB",
        'progress_cancelling': "Avbryter...",
        'progress_cancel_message': "{0} avbrytes",
        'progress_pages_found_moving': "Fant {0} sider, {1} å flytte",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analyserer PDF...",
        'ocr_status_optimizing': "Bildeoptimalisering pågår...",
        'ocr_status_recognizing': "Tekstgjenkjenning pågår...",
        'ocr_status_embedding': "Bygger inn tekst...",
        'ocr_status_finalizing': "Fullfører PDF...",

        # PDF-Laden
        'progress_preparing': "Forbereder...",
        'progress_loading': "Laster PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Sletter sider...",
        'progress_moving_title': "Flytter sider...",
        'pages_found': "Sider funnet",
        'progress_creating_new_order': "Oppretter ny rekkefølge...",
        'progress_sorting_pages': "Sorterer sider...",
        'progress_moving_to_begin': "Flytter {0} sider til begynnelsen",
        'progress_transferring_count': "Overfører {0} sider",
        'progress_transferring_before_target': "Overfører sider før målet",
        'progress_moving_pages': "Flytter {0} sider",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_sikkerhetskopi_",
        'filename_protected_suffix': "_beskyttet_",
        'filename_copy_suffix': "_Kopi",
        'filename_page_single': "_Side_",
        'filename_page_range': "_Sider_",
        'filename_export_page': "_Side_{0:03}",
        'filename_export_range': "_Sider_{0}-{1}",
        'filename_export_multiple': "_Sider_{0}",
        'filename_with_text': "_med_Tekst",
        'filename_with_signature': "_med_Signatur",
        'filename_with_image': "_med_Bilde",
        'filename_with_forms': "_med_Former",
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
        'view_toggle_navbar': "Vis knapperad",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Kan ikke slette alle sider",
		'pages_cannot_delete_last_page': 'Den siste siden kan ikke slettes!',
		'pages_cannot_delete_all_pages': 'Minst én side må være igjen i dokumentet!',
		'delete_pages_confirm': 'Er du sikker på at du vil slette {0} sider?',
		'delete_pages_confirm_voice': 'Er du sikker på at du vil slette {0} sider?',
		'pages_deleted': '{0} sider ble slettet.',
		'warning': 'Advarsel',
		'error': 'Feil',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Ingen form valgt",
        'form_customized': "Form tilpasset",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Velg",
        'btn_use': "Bruk",
        'master_password_for_spasswords': "For å lagre og bruke passord, må du først opprette et hovedpassord.\n\nVil du opprette hovedpassordet nå?",
        'open_saved_dialog_title': "Åpne lagret fil",
        'open_saved_question': "Vil du åpne den lagrede filen nå?",
        'password': "Passord",
        'password_manager_master_required': "Passordbehandleren er bare tilgjengelig hvis et hovedpassord er opprettet.\n\nVil du opprette hovedpassordet nå?",
        'password_master_required_for_select': "For å vise og velge lagrede passord, må du først autentisere deg med hovedpassordet ditt.\n\nVil du autentisere deg nå?",
        'password_not_available': "Det valgte passordet er ikke tilgjengelig eller kunne ikke dekrypteres.",
        'password_options_title': "Passoralternativer",
        'password_save_choice_change': "Sett nytt passord",
        'password_save_choice_keep': "Bruk eksisterende passord",
        'password_save_choice_none': "Lagre ukryptert",
        'password_save_hint': "Opprett først et hovedpassord for å lagre passord sikkert.",
        'password_save_master_required': "Lagre passord (bare mulig med hovedpassord)",
        'password_save_question': "Den gjeldende PDF-en er passordbeskyttet. Vil du bruke det eksisterende passordet, sette et nytt eller lagre ukryptert?",
        'password_select': "Velg passord",
        'password_select_none': "Ingen passord valgt.\n\nVennligst velg et passord fra listen.",
        'password_select_one': "Vennligst velg nøyaktig ett passord.\n\nDu har merket flere passord.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_sikkerhetskopi",
        'filename_insert_suffix': "_med_innsetting",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_sider_slettet",
        'filename_pages_moved': "_sider_flyttet",
        'filename_rotated_all_suffix': "_alle_sider_rotert",
        'filename_rotated_suffix': "_side_rotert",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurasjon av filnavn ved endringer i PDF",
        'filename_keep_suffixes': "Behold tidligere utvidelser (f.eks. _med_tekst)",
        'filename_keep_suffixes_false': "Erstatt",
        'filename_keep_suffixes_true': "Behold",
        'filename_preview_label': "Forhåndsvisning av filnavn:",
        'filename_preview_overwrite_hint': "Forhåndsvisning ikke tilgjengelig – originalen vil bli overskrevet.",
        'filename_separator': "Skilletegn mellom ord",
        'filename_separator_none': "Ingen skilletegn",
        'filename_separator_space': "Mellomrom ( )",
        'filename_separator_underscore': "Understrek (_)",
        'filename_settings_saved': "Filnavninnstillinger lagret",
        'filename_settings_title': "Filnavnformatering og sikkerhetskopi",
        'filename_timestamp_position': "Plassering av tidsstempel",
        'filename_timestamp_position_after': "Etter grunnnavnet",
        'filename_timestamp_position_before': "Helt foran",
        'filename_timestamp_position_end': "På slutten",
        'filename_use_timestamp': "Bruk tidsstempel",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Oppførsel ved endringer:</b><ul><li>Slette og sette inn sider</li><li>Sette inn tekst, signatur, bilde og former</li><li>OCR</li></ul></html>",
        'backup_section': "Sikkerhetskopi for sideoperasjoner (Slett, Flytt)",
        'behavior_info': "Merk: Ved 'Overskriv original' ignoreres tidsstempler og suffikser – filen beholder navnet sitt.",
        'behavior_new_file': "Alltid opprett ny fil (med tidsstempel og suffiks)",
        'behavior_overwrite': "Overskriv original (ingen ny fil)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Alle sider ble rotert.\n\nOriginalen forble uendret.\nNy fil: {0}",
        'all_pages_rotated_voice': "Alle sider rotert, ny fil opprettet.",
        'empty_pages_deleted_new_file': "{0} tomme sider ble slettet.\n\nOriginalen forble uendret.\nNy fil: {1}",
        'empty_pages_deleted_voice': "{0} tomme sider slettet, ny fil opprettet.",
        'ocr_keep_original': "Behold original (åpne manuelt senere)",
        'ocr_new_file_question': "Den nye søkbare PDF-en ble lagret som:\n{0}\n\nVil du åpne den nå?",
        'ocr_open_new': "Åpne ny OCR-fil",
        'ocr_original_kept': "Den opprinnelige filen forblir åpen. OCR-filen er lagret.",
        'page_deleted_new_file': "Side {0} ble slettet.\n\nOriginalen forble uendret.\nNy fil: {1}",
        'page_deleted_voice': "Side {0} slettet, ny fil opprettet.",
        'page_rotated_new_file': "Side {0} ble rotert.\n\nOriginalen forble uendret.\nNy fil: {1}",
        'page_rotated_voice': "Side {0} rotert, ny fil opprettet.",
        'pages_deleted_new_file': "{0} sider ble slettet.\n\nDen originale filen forble uendret.\nNy fil: {1}",
        'pages_deleted_new_file_voice': "{0} sider slettet, ny fil opprettet.",
        'pages_inserted_new_file': "{0} sider ble satt inn.\n\nDen originale filen forble uendret.\nNy fil: {1}",
        'pages_inserted_new_file_ask': "{0} sider ble satt inn.\n\nOriginalen forble uendret.\nNy fil: {1}\n\nVil du åpne den nå?",
        'pages_inserted_voice_new': "{0} sider satt inn, ny fil opprettet.",
        'pages_moved_new_file': "{0} sider ble flyttet.\n\nDen originale filen forble uendret.\nNy fil: {1}",
        'pages_moved_new_file_voice': "{0} sider flyttet, ny fil opprettet.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ikke vis igjen",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Sikkerhetskopiinnstilling</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Sikkerhetskopi PÅ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Ved alle endringer som overskriver originalen</strong> (tekst, signatur, bilde, form, OCR, rotere, sette inn, slette/flytte sider) opprettes <strong>automatisk en sikkerhetskopi med tidsstempel</strong> før endringen brukes.</p>
                <p style="margin: 5px 0 5px 20px;">• Sikkerhetskopien ligger ved siden av den originale filen (f.eks. <code>Dokument_sikkerhetskopi_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Hvis du i tillegg har aktivert alternativet <strong>„Overskriv original“</strong>, opprettes det også en sikkerhetskopi.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Sikkerhetskopi AV</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Ingen sikkerhetskopi opprettes</strong> – verken ved overskriving eller ved sideoperasjoner.</p>
                <p style="margin: 5px 0 5px 20px;">• Den originale filen kan gå tapt ugjenkallelig ved overskriving.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Anbefales bare for erfarne brukere!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tips:</strong> Sikkerhetskopiinnstillingen er uavhengig av alternativet „Overskriv original“. Du kan kombinere begge.<br>
                Du kan skjule denne meldingen permanent.
            </div>
        </div>
        """,
        'backup_info_title': "Sikkerhetskopi-oppførsel",
        'backup_info_voice': "Melding om sikkerhetskopi-oppførsel ved sideoperasjoner. Sikkerhetskopi PÅ overskriver original, sikkerhetskopi AV oppretter ny fil.",
        'show_backup_info': "Info om sikkerhetskopiinnstilling",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ikke vis igjen",
        'overwrite_enable_backup': "Aktiver sikkerhetskopi (anbefales)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Overskriv original</p>
            <p>Hvis du aktiverer dette alternativet, lagres endringer (tekst, signatur, bilde, form, OCR, rotere, sette inn) <strong>direkte i originalen</strong> – <strong>ingen ny fil opprettes</strong>.</p>
            <p>• Filnavnet forblir uendret.<br>
            • Tidsstempler og suffikser ignoreres.<br>
            • <strong>Uten sikkerhetskopi kan originalen gå tapt ugjenkallelig.</strong></p>
            <p style="color: #FFD700;">Anbefaling: Aktiver i tillegg sikkerhetskopialternativet for å få automatiske sikkerhetskopier.</p>
        </div>
        """,
        'overwrite_info_title': "Overskriv original",
        'overwrite_info_voice': "Advarsel: Overskriv original – ingen ny fil. Sikkerhetskopi anbefales.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} sider ble satt inn.\n\nDen originale filen ble overskrevet.\nEn sikkerhetskopi ble opprettet.",
        'pages_inserted_overwrite_no_backup': "{0} sider ble satt inn.\n\nDen originale filen ble overskrevet.\nINGEN sikkerhetskopi ble opprettet.",
        'texts_saved_overwrite_with_backup': "Endringene ble lagret i originalen.\n\nEn sikkerhetskopi ble opprettet.",
        'texts_saved_overwrite_no_backup': "Endringene ble lagret i originalen.\n\nINGEN sikkerhetskopi ble opprettet.",
        'texts_crosses_saved_new_file': "{0} {1} og {2} {3} ble satt inn.\n\nDen originale filen forble uendret.\nEn ny fil ble opprettet.\n\nDen nye PDF-en lastes...",
        'texts_saved_new_file': "{0} {1} ble satt inn.\n\nDen originale filen forble uendret.\nEn ny fil ble opprettet.\n\nDen nye PDF-en lastes...",
        'crosses_saved_new_file': "{0} {1} ble satt inn.\n\nDen originale filen forble uendret.\nEn ny fil ble opprettet.\n\nDen nye PDF-en lastes...",
        'elements_saved_new_file': "{0} elementer ble satt inn.\n\nDen originale filen forble uendret.\nEn ny fil ble opprettet.\n\nDen nye PDF-en lastes...",
        'signatures_saved_overwrite_with_backup': "Signaturen(e) ble lagret i originalen.\n\nEn sikkerhetskopi ble opprettet.",
        'signatures_saved_overwrite_no_backup': "Signaturen(e) ble lagret i originalen.\n\nINGEN sikkerhetskopi ble opprettet.",
        'images_saved_overwrite_with_backup': "Bildet(e) ble lagret i originalen.\n\nEn sikkerhetskopi ble opprettet.",
        'images_saved_overwrite_no_backup': "Bildet(e) ble lagret i originalen.\n\nINGEN sikkerhetskopi ble opprettet.",
        'forms_saved_overwrite_with_backup': "Formen(e) ble lagret i originalen.\n\nEn sikkerhetskopi ble opprettet.",
        'forms_saved_overwrite_no_backup': "Formen(e) ble lagret i originalen.\n\nINGEN sikkerhetskopi ble opprettet.",
        'signatures_saved_new_file': "{0} signaturer ble satt inn.\n\nDen originale filen forble uendret.\nEn ny fil ble opprettet.\n\nDen nye PDF-en lastes...",
        'images_saved_new_file': "{0} bilder ble satt inn.\n\nDen originale filen forble uendret.\nEn ny fil ble opprettet.\n\nDen nye PDF-en lastes...",
        'forms_saved_new_file': "{0} former ble satt inn.\n\nDen originale filen forble uendret.\nEn ny fil ble opprettet.\n\nDen nye PDF-en lastes...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Advarsel: Denne PDF-en inneholder roterte sider. Plasseringen kan avvike.",
        'page_rotated_warning_title': "Roterte side oppdaget",
        'page_rotated_warning_message': "Den gjeldende siden {0} er rotert {1}°.\n\nInnsetting av elementer på roterte sider støttes ikke.\n\nVil du rotere siden til oppreist posisjon nå?",
        'page_rotated_warning_voice': "Advarsel: Siden er rotert. Vennligst roter den først.",
        'paste_on_rotated_page_simple_warning': "Innsetting på side {0} er ikke mulig!\n\nDenne siden er rotert {1}°.\n\nVennligst roter siden til 0° først (Meny: Rediger → Rett opp side).\n\nAdvarsel:\nDet tidligere kopierte elementet vil gå tapt hvis du ikke lagrer før du roterer siden.",
        'paste_on_rotated_page_voice': "Innsetting avbrutt. Siden er rotert. Vennligst rett opp siden først.",
        'page_rotated_cancel': "Avbryt",
        'page_rotated_rotate_until_upright': "Roter siden gjentatte ganger (til den er oppreist)",
        'page_rotated_now_upright': "Siden er nå oppreist. Du kan nå sette inn.",
        'page_rotated_still_not_upright': "Siden kunne ikke roteres til oppreist posisjon. Vennligst korriger manuelt.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hjelp: Rett opp roterte sider",
        'help_rotated_pages_voice': "Hjelp for å rette opp roterte sider åpnes.",
        'btn_help': "Hjelp",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Rotert side – Innsetting fungerer ikke korrekt</p>

            <p>Hvis innsetting av tekster, signaturer eller former på en rotert side ikke fungerer korrekt, kan du rette opp siden med en ekstern PDF-redigerer.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Løsning med eksternt verktøy (f.eks. macOS Forhåndsvisning)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksporter side</strong><br>
                &nbsp;&nbsp;Klikk i menyen på <strong>Fil → Eksporter som sider</strong> eller bruk en annen metode for å lagre ønsket side som en enkelt PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Åpne siden i et eksternt program</strong><br>
                &nbsp;&nbsp;Åpne den eksporterte PDF-en i en PDF-redigerer (f.eks. <strong>macOS Forhåndsvisning</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Roter siden</strong><br>
                &nbsp;&nbsp;Roter siden slik at den står oppreist (i Forhåndsvisning: <strong>Verktøy → Roter</strong> eller <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Lagre</strong><br>
                &nbsp;&nbsp;Lagre den korrigerte siden (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Set inn siden på nytt i det originale dokumentet</strong><br>
                &nbsp;&nbsp;Gå tilbake til PDFDarkView og sett inn den korrigerte siden på ønsket posisjon:<br>
                &nbsp;&nbsp;<strong>Rediger → Sett inn sider</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativ: Roter siden i originalen</p>
                <p style="margin: 5px 0 5px 20px;">• Bruk den innebygde rotasjonsfunksjonen (<strong>Rediger → Roter side</strong>) for å rette opp siden trinn for trinn.<br>
                • Etter hver rotasjon kan du sjekke om innsetting nå fungerer.<br>
                • Dette er ofte den raskere løsningen – prøv dette først!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tips:</strong> Hvis du ofte støter på roterte sider, kan du permanent skjule advarselen i innsettingsdialogen.<br>
                Plasseringen kan da avvike – bruk dette alternativet bare hvis du kjenner konsekvensene.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Rett opp sider",
        'menu_rotate_normalize_tooltip': "Roter side eller tilbakestill til 0°",
        'normalize_current_page': "Før gjeldende side til oppreist posisjon (sett til 0°)",
        'normalize_all_pages': "Før alle sider til oppreist posisjon (sett til 0°)",
        'page_normalized': "Side {0} ble satt til oppreist posisjon.",
        'all_pages_normalized': "Alle sider ble satt til oppreist posisjon.",
        'page_already_upright': "Side {0} er allerede oppreist.",
        'all_pages_already_upright': "Alle sider er allerede oppreiste.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF-en inneholder ingen søkbar tekst.</p><p>Vil du utføre OCR for å eksportere til {0}?</p>",
        'export_ocr_voice': "PDF-en inneholder ingen tekst. OCR kreves for eksport til {0}.",
        'export_no_ocr_possible': "Eksport uten OCR er ikke mulig. Vennligst utfør OCR via menyen.",
        'ocr_failed_export_not_possible': "OCR mislyktes. Eksport kan ikke utføres.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF-en åpnes i Forhåndsvisning. Vennligst start utskriftsprosessen der.",
        'print_preview_manual': "PDF-en er åpnet. Vennligst utfør utskriftskommandoen manuelt (f.eks. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Slå sammen PDF-er",
        'merge_pdfs': "Slå sammen PDF-er",
        'merge_progress_title': "Slår sammen PDF-er...",
        'merge_pdfs_list': "PDF-er i rekkefølge (Dra og slipp for å sortere)",
        'merge_add_pdf': "Legg til PDF",
        'merge_remove': "Fjern",
        'merge_move_up': "Opp",
        'merge_move_down': "Ned",
        'merge_pdfs_info': "💡 Tips: Du kan endre rekkefølgen ved å dra og slippe",
        'merge_no_pdfs': "Ingen PDF-er valgt. Klikk på 'Legg til PDF'.",
        'merge_info': "{0} PDF-er valgt (omtrent {1} sider)",
        'merge_open_file': "Åpne fil",
        'merge_merge': "Slå sammen",
        'merge_error': "Feil ved sammenslåing",
        'merge_min_two_pdfs_error': "Vennligst velg minst to PDF-filer å slå sammen.",
        'merge_select_pdfs': "Velg PDF-er å slå sammen",
        'merge_error_file': "Feil ved behandling",
        'merge_cancelled': "Sammenslåingen ble avbrutt",
        'merge_preparing': "Forbereder...",
        'merge_processing': "Behandler PDF {0} av {1}",
        'merge_saving': "Lagrer sammenslått PDF...",
        'merge_complete': "Ferdig!",
        'merge_success_title': "Sammenslåing vellykket",
        'merge_success_voice': "{0} PDF-er ble vellykket slått sammen.",
        'merge_success_message': "{0} PDF-er ble vellykket slått sammen.\n\nDet nye dokumentet har nå {1} sider.\n\nNy fil:\n{2}\n\nLagringssted:\n{3}\n{2}\n\nVil du åpne denne PDF-en?",
        'replace_file_title': "Erstatt fil?",
        'replace_file_message': "En PDF er allerede åpen. Vil du erstatte den med den nye filen?",
        'btn_yes': "Ja",
        'btn_no': "Nei",
        'filename_merge_suffix': "sammenslått",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Åpner {0}...",
        'progress_merge_reading': "Leser {0}...",
        'progress_merge_adding': "Legger til {0} sider...",
        'progress_merge_optimizing': "Optimaliserer PDF...",
        'progress_merge_writing': "Skriver PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "lukking av PDF-en",
        'action_close_window': "lukking av vinduet",
        'action_open_new_pdf': "åpning av en ny PDF",
        'action_quit_app': "avslutning av programmet",
        'changes_saved': "Endringene er lagret.",
        'file_close_title': "Lukk PDF-fil",
        'save_before_action': "Skal endringene lagres før {0}? Ja eller Nei?",
        'save_before_action_voice': "Skal endringene lagres før {0}? Ja eller Nei?",
        'save_before_close_question': "Skal endringene lagres før lukking? Ja eller Nei?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Søkbar PDF opprettet:\n\n{0}\n\n<b>prøv igjen om nødvendig",
        "ocr_rotate_title": "Juster sider før OCR",
        "ocr_rotate_question": "PDF-en inneholder roterte sider.\nVil du justere alle sider til 0° før OCR?\nDette forbedrer tekstgjenkjenningen betydelig.",
        "ocr_rotate_yes": "Ja, juster",
        "ocr_rotate_no": "Nei, start OCR direkte",
        "ocr_rotate_voice": "PDF-en inneholder roterte sider. Bør alle sider justeres før OCR?",
        "ocr_not_performed_message": "Ingen tekst til stede. Vennligst utfør OCR (meny \"Rediger\" → \"Utfør OCR\" eller tast Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-innstillinger",
        "ocr_language_btn": "Velg OCR-språk",
        "ocr_language": "OCR-språk",
        "ocr_language_current": "Gjeldende språk:",
        "ocr_param_info": "Informasjon om parameter",

        "ocr_force_ocr_label": "Tving OCR",
        "ocr_deskew_label": "Korriger skjevhet",
        "ocr_clean_label": "Rens bilde",
        "ocr_oversample_label": "Oppløsning (DPI)",
        "ocr_pagesegmode_label": "Sideoppdeling",
        "ocr_oem_label": "OCR-motor modus",
        "ocr_optimize_label": "PDF-komprimering",
        "ocr_jobs_label": "Parallelle prosesser",
        "ocr_verbose_label": "Loggdetaljer",

        "ocr_force_ocr_tooltip": "Tving OCR på hver side, selv om tekst allerede finnes",
        "ocr_deskew_tooltip": "Juster skjeve skanninger automatisk",
        "ocr_clean_tooltip": "Fjern støy og artefakter fra bildet",
        "ocr_oversample_tooltip": "Skaler opp bildet før OCR til denne DPI",
        "ocr_pagesegmode_tooltip": "Bestemmer hvordan siden deles inn i tekstområder",
        "ocr_oem_tooltip": "Velger Tesseracts OCR-motor",
        "ocr_optimize_tooltip": "Komprimeringsnivå for utdata-PDF",
        "ocr_jobs_tooltip": "Antall parallelle OCR-prosesser",
        "ocr_verbose_tooltip": "Detaljnivå for loggutdata",
        "ocr_settings_explain_btn": "Forklaring",

        "ocr_force_ocr_explain": "Tvinger tekstgjenkjenning på <b>hver</b> side, selv om den allerede inneholder tekst.\n\nAnbefaling: <b>På</b> for skannede PDF-er, <b>Av</b> for opprinnelige PDF-er med eksisterende tekst.",

        "ocr_deskew_explain": "Korrigerer lett skjeve skanninger (opptil ca. 5°).\n\nAnbefaling: <b>På</b> for skannede dokumenter, <b>Av</b> hvis sidene allerede er perfekt rette.",

        "ocr_clean_explain": "Fjerner støy, prikker og små artefakter fra bildet.\n<b>VIKTIG:</b> For arabiske, thailandske eller vietnamesiske tekster med diakritiske tegn (prikker over/under bokstaver) bør dette alternativet <b>deaktiveres</b>, ellers kan viktige tegn gå tapt.",

        "ocr_oversample_explain": "Skalerer bildet <b>før</b> tekstgjenkjenning til angitt DPI.<br><br>• <b>72-150 DPI:</b> Veldig raskt, men lav gjenkjenningsrate<br>• <b>200-300 DPI:</b> Optimalt område (Standard: 300)<br>• <b>400+ DPI:</b> Knapt bedre gjenkjenning, men betydelig større filer<br><br>Anbefaling: 300 DPI for komplekse skrifter (arabisk, kinesisk, japansk), 200 DPI for vestlige språk.",

        "ocr_pagesegmode_explain": "Bestemmer hvordan Tesseract deler siden inn i tekstområder.\n\n• <b>3 - Automatisk (Standard):</b> Godt for blandede oppsett\n• <b>4 - Enkelt kolonne:</b> For enkeltkolonnetekster\n• <b>5 - Vertikal blokk:</b> For vertikale skrifter (japansk, kinesisk)\n• <b>6 - Enhetlig tekstblokk:</b> Optimalt for flytende tekst uten kolonner\n• <b>11 - Rått bilde:</b> For dårlige skanninger / håndskrift\n\nAnbefaling: <b>6</b> for enkle tekstdokumenter, <b>3</b> for komplekse oppsett.",

        "ocr_oem_explain": "Velger Tesseracts OCR-motor.\n\n• <b>0 - Legacy:</b> Gammel motor (rask, men mindre nøyaktig)\n• <b>1 - LSTM:</b> Nevral motor (saktere, men mer nøyaktig)\n• <b>2 - Legacy + LSTM:</b> Kombinerer begge resultatene\n• <b>3 - Standard (LSTM foretrukket):</b> Beste valg for de fleste tilfeller\n\nAnbefaling: <b>3</b> for maksimal gjenkjenningsnøyaktighet.",

        "ocr_optimize_explain": "Komprimerer utdata-PDF.\n\n• <b>0:</b> Ingen optimalisering (raskest behandling)\n• <b>1:</b> Lett optimalisering (godt kompromiss)\n• <b>2:</b> Moderat optimalisering\n• <b>3:</b> Sterk optimalisering (minste fil, men saktere)\n\nAnbefaling: <b>1</b> for daglig bruk.",

        "ocr_jobs_explain": "Antall parallelle prosesser for OCR.\n\n• <b>1:</b> Sakte, men lavest minneforbruk\n• <b>4-8:</b> Optimalt for moderne flerkjerneprosessorer\n• <b>12+:</b> Knapt raskere behandling med høyt minneforbruk\n\nAnbefaling: Antall CPU-kjerner (f.eks. <b>4</b> på 4-kjernesystemer).",

        "ocr_verbose_explain": "Detaljnivå for loggutdata i konsollen.\n\n• <b>0:</b> Ingen utdata\n• <b>1:</b> Fremdrift og statusmeldinger\n• <b>2:</b> Detaljert utdata\n• <b>3:</b> Full feilsøkingsutdata (svært omfattende)\n\nAnbefaling: <b>1</b> for normal drift.",

        "ocr_reset_title": "Innstillinger tilbakestilt",
        "ocr_reset_message": "Alle OCR-innstillinger er tilbakestilt til standardverdier.",
        "info_tooltip": "Mer informasjon om denne parameteren",
        "ocr_reset_defaults": "Tilbakestill til standard",

        "ocr_psm_0": "Automatisk (Legacy-motor)",
        "ocr_psm_1": "Automatisk kolonnedeteksjon",
        "ocr_psm_3": "Automatisk (Standard)",
        "ocr_psm_4": "Enkelt kolonne",
        "ocr_psm_5": "Vertikal blokk",
        "ocr_psm_6": "Enhetlig tekstblokk",
        "ocr_psm_7": "Enkelt tekstlinje",
        "ocr_psm_8": "Enkelt ord",
        "ocr_psm_11": "Rått bilde (ingen opplagsanalyse)",

        "ocr_oem_0": "Legacy-motor (rask)",
        "ocr_oem_1": "LSTM-motor (nevral, nøyaktig)",
        "ocr_oem_2": "Legacy + LSTM kombinert",
        "ocr_oem_3": "Standard (LSTM foretrukket)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-språk...",
        "ocr_language_title": "Velg OCR-språk",
        "ocr_language_instruction": "Velg språk for tekstgjenkjenning (OCR).\nForsiktig: Flere språk går på bekostning av ytelse og nøyaktighet!\nDu oppnår de beste resultatene hvis du bare velger ett språk.",
        "ocr_language_predefined": "Forhåndsdefinerte kombinasjoner",
        "ocr_language_custom": "Tilpasset...",
        "ocr_language_selected": "Valgte OCR-språk",
        "ocr_language_changed": "OCR-språk endret til {0}",
        "ocr_language_auto_detect": "Tilgjengelige språk oppdages automatisk.",
        "ocr_language_none_found": "Ingen Tesseract-språkdata funnet! Vennligst installer språkpakker (f.eks. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Tilpasset språkvalg",
        "ocr_language_available": "Tilgjengelige språk (installert):",
        "ocr_language_select_hint": "Velg ett eller flere språk:",
        "ocr_language_confirm": "Bruk",
        "ocr_language_reset": "Tilbakestill til standard (deu+eng+vie)",
        "ocr_language_priorities": "Anbefalte språk (forhåndsinstallert):",

        "select_all_languages": "Velg alle",
        "clear_all_languages": "Tøm valg",
        "install_language_packs": "Installer manglende språkpakker...",
        "install_hint": "💡 Tips: Ikke alle språk er installert på systemet ditt. Via denne knappen får du hjelp til installasjon.",
        "ocr_language_install_title": "Installasjon av Tesseract-språkpakker",

        "ocr_missing_languages": "Manglende OCR-språkpakker",
        "ocr_missing_languages_message": "Følgende valgte språk er ikke installert på systemet ditt:\n\n{0}\n\nVennligst installer de manglende språkpakkene (se hjelp under 'Installasjonshjelp').\n\nVil du åpne installasjonshjelpen nå?",
        "ocr_missing_languages_voice": "Manglende språkpakker. Vennligst installer de manglende språkene.",
        "ocr_install_help_now": "Åpne hjelp",
        "ocr_continue_anyway": "Forsøk likevel",
        "ocr_language_error_title": "OCR-språkfeil",
        "ocr_language_error_message": "Feil under tekstgjenkjenning: {0}\n\nVennligst kontroller OCR-språkinnstillingene dine (Innstillinger → OCR-språk).",
        "ocr_install_help_button": "Installasjonshjelp",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Installer Tesseract-språkpakker</p>

        <p>For at OCR skal fungere på et bestemt språk, må de tilsvarende språkdataene være installert på systemet ditt. Følg instruksjonene for operativsystemet ditt:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Åpne <strong>Terminal</strong> (Finder → Programmer → Verktøy → Terminal).</li>
        <li>Installer alle tilgjengelige språk med:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Dette kan ta noen minutter.)</li>
        <li>Eller bare individuelle språk (f.eks. vietnamesisk):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Med nåværende Homebrew-versjoner må <code>*.traineddata</code> kanskje lastes ned manuelt (se nedenfor).</li>
        <li>Etter installasjon: Lukk denne dialogboksen og åpne OCR-språkvalget på nytt – de nye språkene vises automatisk.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Åpne en terminal (Ctrl+Alt+T).</li>
        <li>Installer ønsket språk, f.eks. for vietnamesisk:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Viktige språkkoder: <code>deu</code> (tysk), <code>eng</code> (engelsk), <code>vie</code> (vietnamesisk), <code>spa</code> (spansk), <code>fra</code> (fransk), <code>ita</code> (italiensk), <code>nld</code> (nederlandsk), <code>fin</code> (finsk), <code>swe</code> (svensk), <code>nor</code> (norsk).</li>
        <li>Vis alle tilgjengelige pakker:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuell)</p>
        <ol>
        <li>Last ned ønskede <code>*.traineddata</code>-filer fra:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (f.eks. <code>vie.traineddata</code> for vietnamesisk).</li>
        <li>Kopier filene til Tesseracts språkmappe, vanligvis:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Juster i henhold til individuell installasjon.)</li>
        <li>Start programmet på nytt (eller åpne OCR-språkvalget på nytt).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativ for alle systemer</p>
        <ul>
        <li>Installer <strong>OCRmyPDF</strong> og <strong>Tesseract</strong> med en pakkebehandler etter eget valg. De fleste installasjoner inneholder allerede noen standardspråk (engelsk, tysk, fransk).</li>
        <li>Manglende språk kan installeres når som helst – OCR-språkvalget viser bare de faktisk eksisterende språkene.</li>
        </ul>

        <hr>
        <p><b>✅ Etter installasjon:</b> Ingen omstart av programmet er nødvendig – de nylig lagt til språkene vises umiddelbart i listen.</p>
        <p><b>📖 Hjelp med språkkoder:</b> En fullstendig liste er tilgjengelig i <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract-dokumentasjonen</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans-skrifter",
        "info_noto_font_voice": "Installasjonsveiledning for Noto Sans-skrifter",
        "btn_info_noto_font_install": "Skriftinfo",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Slik installerer du de gratis Noto-skriftene fra Google</h2>

        <p><strong>Noto-skriftene</strong> er en åpen kildekode-skriftfamilie fra Google. Målet deres er å se <em>"ingen tofu"</em> (dvs. ingen tomme bokser □) og å vise hvert tegn fra Unicode-standarden korrekt. De er det ideelle tillegget for applikasjoner som må vise tekster på mange forskjellige språk.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installasjon på macOS</h3>

        <p><strong>Metode 1: Med Homebrew (for viderekomne)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metode 2: Via "Font Book" (Anbefalt)</strong></p>

        <ol>
        <li>Last ned den offisielle skriftpakken:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pakk ut ZIP-filen</li>
        <li>Kopier filene til <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installasjon på Windows (10 & 11)</h3>

        <p><strong>Metode 1: Microsoft Store (Anbefalt)</strong><br>
        Søk etter "Google Noto Fonts" eller "Noto Sans" og klikk <strong>Installer</strong>.</p>

        <p><strong>Metode 2: Manuell installasjon</strong></p>

        <ol>
        <li>Last ned:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pakk ut ZIP</li>
        <li>Velg .ttf / .otf filer</li>
        <li>Høyreklikk → <strong>Installer</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        eller<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Navn\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installasjon på Linux</h3>

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

        <p>Bekreftelse:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Administrer bokmerker",
        "bookmark_add": "Legg til bokmerke",
        "bookmark_add_tooltip": "Lagre gjeldende side som bokmerke",
        "bookmark_remove": "Fjern bokmerke",
        "bookmark_remove_tooltip": "Slett det merkede bokmerket",
        "bookmark_remove_all": "Fjern alle",
        "bookmark_remove_all_tooltip": "Slett alle bokmerker i denne PDF-en",
        "bookmark_jump": "Gå til bokmerke",
        "bookmark_jump_tooltip": "Gå til valgt side",
        "bookmark_name": "Navn",
        "bookmark_page": "Side",
        "bookmark_no_bookmarks": "Ingen bokmerker til stede.\nKlikk på 'Legg til' for å lagre gjeldende side som bokmerke.",
        "bookmark_added": "Bokmerke for side {0} lagt til: {1}",
        "bookmark_removed": "Bokmerke fjernet: {0}",
        "bookmark_all_removed": "Alle bokmerker er fjernet.",
        "bookmark_name_default": "Side {0}",
        "bookmark_name_prompt": "Navn for bokmerket:\n(lang tekst vil bli forkortet til 50 tegn)",
        "bookmark_name_prompt_title": "Bokmerkenavn",
        "bookmark_confirm_remove_all": "Er du sikker på at du vil fjerne alle {0} bokmerker?",
        "menu_bookmarks": "Bokmerker",
        "bookmark_manage": "Administrer bokmerker",
        "bookmark_next": "Neste bokmerke",
        "bookmark_prev": "Forrige bokmerke",
        "bookmark_page_display": "Side {0}",
        "bookmark_exists": "Det finnes allerede et bokmerke for denne siden med dette navnet.",
        "bookmark_select_first": "Velg først et bokmerke.",
        "bookmark_confirm_remove": "Er du sikker på at du vil fjerne bokmerket 'Side {0}: {1}'?",
        "bookmark_jumped_to": "Gikk til bokmerke '{0}' på side {1}.",
        "bookmark_jumped_to_voice": "Bokmerke {0}, side {1}",
        "btn_close": "Lukk",

        "bookmark_list": "Dine bokmerker",
        "bookmark_rename": "Gi nytt navn til bokmerke",
        "bookmark_rename_tooltip": "Endre navnet på det valgte bokmerket",
        "bookmark_rename_title": "Gi nytt navn til bokmerke",
        "bookmark_rename_prompt": "Nytt navn for bokmerke på side {0}:\n(maks. 50 tegn)",
        "bookmark_renamed": "Bokmerke '{0}' er omdøpt til '{1}'.",
        "bookmark_item_tooltip": "Side {0}: {1}\nDobbeltklikk for å gå",
        "bookmark_name_exists_question": "Det finnes allerede et bokmerke med navnet '{0}' på denne siden.\nGi likevel nytt navn?",

        "context_bookmarks": "Bokmerker",
        "context_bookmark_add_here": "Legg til bokmerke for denne siden",
        "context_bookmarks_existing": "Eksisterende bokmerker:",
        "context_bookmarks_jump": "Gå til bokmerke:",
        "context_bookmarks_none": "Ingen bokmerker til stede",
        "context_bookmarks_clear_all": "Fjern alle {0} bokmerker",

        "bookmark_search_placeholder": "Søk i bokmerker... (navn eller side)",
        "bookmark_search_results": "%d bokmerker funnet for \"%s\"",
        "bookmark_no_search_results": "Ingen bokmerker funnet for \"%s\"",
        "bookmark_no_search_results_label": "Ingen resultater for \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Rediger PDF-metadata",
        "metadata_title": "Tittel",
        "metadata_title_placeholder": "Dokumenttittel",
        "metadata_title_tooltip": "Tittelen på dokumentet (vises i tittellinjen)",
        "metadata_author": "Forfatter",
        "metadata_author_placeholder": "Forfatterens navn",
        "metadata_author_tooltip": "Skaperen av dokumentet",
        "metadata_subject": "Emne",
        "metadata_subject_placeholder": "Dokumentets emne",
        "metadata_subject_tooltip": "En kort beskrivelse av innholdet",
        "metadata_keywords": "Nøkkelord",
        "metadata_keywords_placeholder": "Nøkkelord, atskilt med komma",
        "metadata_keywords_tooltip": "Nøkkelord for å kategorisere dokumentet",
        "metadata_creator": "Skaper",
        "metadata_creator_placeholder": "Programmet som opprettet PDF-en",
        "metadata_creator_tooltip": "Programvaren som dokumentet ble opprettet med",
        "metadata_producer": "Produsent",
        "metadata_producer_placeholder": "Programmet som konverterte PDF-en",
        "metadata_producer_tooltip": "Programvaren som konverterte PDF-en",
        "metadata_creation_date": "Opprettelsesdato",
        "metadata_creation_date_tooltip": "Datoen for dokumentopprettelse",
        "metadata_mod_date": "Endringsdato",
        "metadata_mod_date_tooltip": "Datoen for siste endring",
        "metadata_pdf_info": "📄 PDF-informasjon",
        "metadata_pages": "Antall sider",
        "metadata_file_size": "Filstørrelse",
        "metadata_pdf_version": "PDF-versjon",
        "metadata_encrypted": "Kryptert",
        "metadata_encrypted_yes": "Ja (passordbeskyttet)",
        "metadata_encrypted_no": "Nei",
        "metadata_reload": "📂 Last inn på nytt fra PDF",
        "metadata_reset": "Forkast endringer",
        "metadata_reloaded": "Metadata er lastet inn på nytt fra PDF-en.",
        "metadata_reset_done": "Alle metadatofelt er tilbakestilt.",
        "metadata_no_file": "Ingen PDF-fil lastet.",
        "metadata_save_error": "Feil ved lagring av metadata",
        "metadata_saved": "Metadata er lagret.",
        "metadata_pdf_version_unknown": "PDF (ukjent)",
        "metadata_saved_message": "Metadata er lagret.",
        "metadata_saved_voice": "Metadata lagret.",

        "metadata_custom": "🔧 Tilpasset metadata",
        "metadata_custom_placeholder": "{\n  \"mitt_felt\": \"min_verdi\",\n  \"annet_felt\": 123\n}",
        "metadata_custom_tooltip": "JSON-format for tilpasset metadata (valgfritt)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Mal \"{0}\" valgt - Dobbeltklikk for å sette inn",
        "text_use_template": "Bruk tekstblokk",
        "text_type": "Type",
        "text_search_templates": "Søk i tekstblokker...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Eksport / Import informasjon",
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

        <h3>📦 Hva eksporteres? (Oversikt)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Generelle programinnstillinger</span></li>
            <li class="detail">• Mørk/Lys modus</li>
            <li class="detail">• Mørk modus inversjon for bilder</li>
            <li class="detail">• Grå terskelverdi</li>
            <li class="detail">• Språk</li>
            <li class="detail">• Vindusgeometri</li>
            <li class="detail">• Zoom-modus</li>
            <li class="detail">• Navigasjon (Navigasjonslinje synlig)</li>
            <li class="detail">• Taleutdata (på/av)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Sikkerhetskopi-innstillinger</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Filnavngivning (Tidsstempel, Skilletegn, Suffikser)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Innstillinger for innsettinger</span></li>
            <li class="detail">• Signaturer</li>
            <li class="detail">• Tekst og tekstblokker</li>
            <li class="detail">• Kryss, bilder og former</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-innstillinger</span></li>
            <li class="detail">• Språk</li>
            <li class="detail">• Tving OCR · Sidemodus</li>
            <li class="detail">• Bildeforbehandling: Korriger skjevhet, Rens, Oversampling</li>
            <li class="detail">• Antall parallelle jobber</li>
            <li class="detail">• Inversjonsmodus</li>
            <li class="detail">• Grå terskelverdi</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bokmerker</span></li>
            <li class="detail">• Alle bokmerker per PDF-fil (Side, Navn, Opprettelsestid)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Passorddatabase</span></li>
            <li class="detail">• Lagrede PDF-passord (valgfritt kryptert eller ren tekst)</li>
            <li class="detail">• Masterpassord-hash (hvis angitt)</li>
            <li class="detail">• Verifikasjonsdata</li>
        </ul>

        <h4>⚠️ Viktige merknader</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Ved import:</strong>
            <ul>
                <li><span class="warning">➜ ALLE gjeldende innstillinger vil bli fullstendig overskrevet</span></li>
                <li>• En omstart av programmet er obligatorisk</li>
                <li>• Eksisterende signaturer, tekstblokker og bokmerker vil bli erstattet</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Masterpassord og eksportmodus:</strong>
            <ul>
                <li>• Når masterpassordet er aktivt, kan du velge:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dekryptert</strong></span> (passord er i ren tekst i ZIP-en)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Kryptert</strong></span> (bare lesbart med masterpassord på målsystemet)</li>
                <li>• Masterpassord-hash-en lagres <strong>alltid</strong> kryptert</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Sikkerhetsmelding:</strong>
            <ul>
                <li>• Den eksporterte ZIP-filen inneholder sensitive data (<strong>passord, bokmerker, signaturer</strong>)</li>
                <li>• Oppbevar den sikkert (f.eks. kryptert USB-pinne, passordbehandler)</li>
                <li>• Hvis filen går tapt, er lagrede PDF-passord uopprettelig tapt</li>
            </ul>
        </div>

        <h4>📁 Eksportformat</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Innstillingene lagres i én ZIP-fil:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Denne ZIP-en inneholder den fullstendige <code>settings.json</code> (fra konfigurasjonen din) samt eventuelle innebygde signaturbilde-filer og krypterte passord.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Signaturer - Veiledning",
        'signature_guide_html': """
        📝 <strong>Signaturer - Kort veiledning</strong><br>
        <ul>
        <li>Sett opp hovedpassord</li>
        <li>Konfigurer signaturer i menyen <em>Innstillinger</em> (størrelse, tidsstempel, …)</li>
        <li>Sett inn med <strong>HØYREKLIKK</strong> på ønsket posisjon (hovedpassord kreves én gang per økt)</li>
        <li>Flytt signaturen med musen eller piltastene</li>
        <li>Sett inn flere signaturer etter hverandre</li>
        <li>Tilpass hver signatur individuelt</li>
        <li>Forkast enkelt signatur</li>
        <li>Lagre / forkast alle signaturer samtidig</li>
        <li>Alternativt kan menylinjen også brukes.</li>
        </ul>
        """,
        'signature_guide_voice': "Kort veiledning for signaturer. Sett opp hovedpassord. Konfigurer signaturer i innstillinger. Sett inn med høyreklikk.",

        'image_guide_title': "Sett inn bilder - Veiledning",
        'image_guide_html': """
        📷 <strong>Sette inn bilder i PDF - Kort veiledning</strong><br>
        <ol>
        <li>Høyreklikk på ønsket posisjon</li>
        <li><em>„Sett inn bilde“</em> → Velg bilde</li>
        <li>Posisjoner bildet: Dra med musen</li>
        <li>Juster størrelse: Dra i hjørner/kanter</li>
        <li>Behold sideforholdet: Tast <strong>[A]</strong></li>
        <li>Ytterligere justeringer: Høyreklikk på bildet</li>
        </ol>
        <p><strong>Tips:</strong> I kontekstmenyen kan du justere innstillingene.</p>
        """,
        'image_guide_voice': "Kort veiledning for bilder. Høyreklikk, sett inn bilde, velg. Posisjoner med musen, juster størrelse i hjørner. Sideforhold med tast A.",

        'form_guide_title': "Sett inn former - Veiledning",
        'form_guide_html': """
        📐 <strong>Sette inn former i PDF - Kort veiledning</strong><br>
        <ol>
        <li>Velg formtype (rektangel, ellipse, linje, pil)</li>
        <li>Klikk på posisjon:
            <ul>
            <li>For rektangel/ellipse: Ett klikk plasserer formen</li>
            <li>For linje/pil: To klikk for start- og sluttpunkt</li>
            </ul>
        </li>
        <li>Posisjoner formen: Dra med musen</li>
        <li>Juster størrelse: Dra i hjørner/kanter</li>
        <li>Lagre form: <strong>Enter</strong></li>
        <li>Forkast form: <strong>ESC</strong></li>
        <li>Ytterligere justeringer: Høyreklikk på formen</li>
        </ol>
        <p><strong>Tips:</strong> I kontekstmenyen kan du justere innstillingene.</p>
        """,
        'form_guide_voice': "Kort veiledning for former. Velg formtype. For rektangel eller ellipse klikk én gang, for linje eller pil to ganger. Posisjoner med musen, juster størrelse i hjørner. Lagre med Enter, forkast med Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "forrige",
        "btn_next_result": "neste",
        "ocr_text_window": "OCR-tekstvindu",
        "bookmark_existing": "Eksisterende bokmerker",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR-sammenligning Mac - Windows",
        'ocr_method_mac_win_title': "OCR-forskjeller mellom Mac og Windows",
        'ocr_method_mac_win_voice': "Mac er bedre",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Forskjeller mellom macOS og Windows</strong></p>

        <p><strong>macOS (anbefalt)</strong></p>
        <p>Verktøy:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resultat:</p>
        <ul>
        <li>Et søkbart PDF med innebygd tekst som i stor grad bevarer det opprinnelige oppsettet.</li>
        </ul>
        <p>Fordeler:</p>
        <ul>
        <li>Utmerket kvalitet på tekstgjenkjenning (også på skjeve sider).</li>
        <li>Bevaring av vektorgrafikk og fonter.</li>
        <li>GUI-fremskrittslinje via underprosessevaluering.</li>
        <li>Full kontroll over alle OCR-parametere (Deskew, Clean, Oversample, optimalisering).</li>
        <li>Tekstsøk er direkte tilgjengelig i hovedvinduet (PDF-visning).</li>
        </ul>
        <p>Ulemper:</p>
        <ul>
        <li>Krever ytterligere systemverktøy (ocrmypdf, Ghostscript, unpaper, pngquant – inkludert i App Bundle).</li>
        <li>Mer kompleks feilhåndtering (deadlocks, tidsavbrudd).</li>
        </ul>

        <p><strong>Windows (stabilt alternativ)</strong></p>
        <p>Verktøy:</p>
        <ul>
        <li>pytesseract (direkte tilkobling til Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resultat:</p>
        <ul>
        <li>Et søkbart PDF som visuelt tilsvarer et bilde-PDF, men er søkbart via den gjennomsiktige teksten.</li>
        </ul>
        <p>Fordeler:</p>
        <ul>
        <li>Ingen kommer til meg akkurat nå.</li>
        </ul>
        <p>Ulemper:</p>
        <ul>
        <li>PDF-en er i hovedsak et bilde med usynlig tekst; oppsettet kan avvike noe for komplekse dokumenter (kolonner, tabeller).</li>
        <li>Ingen automatisk skjevhetskorreksjon (--deskew) eller bildeopprydding (--clean).</li>
        <li>GUI-fremskrittslinjen oppdateres bare grovt basert på antall behandlede sider.</li>
        <li>OCR-hastigheten er litt langsommere (fordi hver side behandles separat).</li>
        <li>Tekstsøk omdirigeres til OCR-tekstvinduet.</li>
        </ul>

        <p><strong>Felles trekk</strong></p>
        <ul>
        <li>Begge metodene oppretter et søkbart PDF i samme katalog som kildefilen.</li>
        <li>OCR-innstillingene (språk, DPI, sidsegmenteringsmodus, OCR-motormodus) kan konfigureres via OCRSettingsDialog og gjelder i begge implementasjonene.</li>
        </ul>

        <p><strong>Anbefaling:</strong></p>
        <ul>
        <li>macOS: ocrmypdf-binæren gir de beste resultatene – Kjøp en Mac og bruk versjonen (PDFDarkView for Mac-er med Apple Silicon eller Intel-brikke). OCR-resultatene er bedre enn under Windows!</li>
        <li>Windows: Bruk pytesseract-løsningen. Den er stabil og gir en helt tilstrekkelig kvalitet for de fleste dokumenter.</li>
        </ul>

        <p><strong>Viktig merknad:</strong></p>
        <ul>
        <li>Begge versjoner er fullt integrert i brukergrensesnittet – brukeren merker ingen forskjell.</li>
        <li>Programmet bestemmer automatisk hvilken OCR-motor som skal brukes basert på operativsystemet.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Opprett signatur (fra skanning)",
        "signature_create_title": "Velg skannet signatur (PDF/bilde)",
        "image_pdf_filter": "Bilder og PDF",
        "signature_pdf_empty": "PDF-en inneholder ingen sider.",
        "signature_created_success": "Signatur opprettet: {0}",
        "signature_create_error": "Feil ved oppretting av signatur:\n{0}",
        "rembg_missing": "rembg er ikke installert.\nInstaller: pip install rembg\nFeil: {0}",
        "signature_name_title": "Filnavn for signaturen",
        "signature_name_message": "Skriv inn et filnavn for den nye signaturen (lagres som PNG med gjennomsiktig bakgrunn):",
        "signature_name_label": "Filnavn:",
        "signature_name_voice": "Skriv inn filnavn for signatur",
        "signature_processing": "Behandler...",
        "signature_creation_title": "Oppretter signatur",
        "signature_overwrite_warning": "Filen '{0}' finnes allerede. Overskrive?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Forbered PDF for signatur",
        "signature_prepare_instruction":"Velg en PDF som inneholder en skannet signatur på én side.\n\nFor optimal gjenkjenning må følgende være oppfylt:\n• Signaturen er skrevet med svart blekk (kulepenn eller fineliner) på hvitt papir.\n• Signaturen befinner seg i den øvre tredjedelen av en ellers tom A4-side.\n• PDF-en er skannet med minst 300 dpi.\n• Signaturen er tydelig og ikke for tynn.\n• Det er ingen forstyrrende bakgrunnsmønstre eller linjer.",
        "signature_prepare_voice":"Velg en PDF med en skannet signatur. Vær oppmerksom på god kvalitet og kontrast.",
        "sig_thickness_label":"Linjetykkelse:",
        "sig_thickness_normal":"Normal (tynn)",
        "sig_thickness_bold":"Fet (anbefalt)",
        "sig_thickness_very_bold":"Veldig fet",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Legg til GUI- og OCR-språk - Veiledning",
        'language_guide_title': "Legg til GUI- og OCR-språk",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Last ned ønsket oversettelsesfil <code>translations_xy.py</code> fra<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        og plasser den i følgende katalog:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Åpne nettleseren din.</li>
        <li>Gå til: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Søk på høyre skjermkant etter "Releases" og velg den som er merket <strong>"latest"</strong>.</li>
        <li>På den følgende utgivelsessiden laster du ned filen <code>Source Code.zip</code> helt nederst.</li>
        <li>Pakk ut ZIP-filen.</li>
        <li>Søk i den utpakkede mappen etter alle språkfilene du trenger, og kopier dem til katalogen:<br/>
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
        "menu_watermark":"Sett inn vannmerke",
        "fullpage_text_watermark_title":"Tekst som vannmerke",
        "fullpage_image_watermark_title":"Bilde som vannmerke",
        "filename_with_watermark":"_med_vannmerke",
        "watermark_text":"Tekst:",
        "watermark_text_placeholder":"Din vannmerketekst...",
        "watermark_font_family":"Skrifttype:",
        "watermark_font_size":"Skriftstørrelse:",
        "watermark_format":"Formatering:",
        "watermark_bold":"Fet",
        "watermark_italic":"Kursiv",
        "watermark_color":"Farge:",
        "watermark_choose_color":"Velg farge...",
        "watermark_opacity":"Dekkevne / Gjennomsiktighet:",
        "watermark_direction":"Leseretning:",
        "watermark_direction_l_r":"Venstre → Høyre",
        "watermark_direction_bl_tr":"Nede venstre → Oppe høyre",
        "watermark_direction_tl_br":"Oppe venstre → Nede",
        "watermark_direction_b_t":"Nede → Oppe",
        "watermark_direction_t_b":"Oppe → Nede",
        "watermark_preview":"Forhåndsvisning:",
        "watermark_preview_sample":"Eksempeltekst",
        "watermark_empty_text":"Vennligst skriv inn tekst.",
        "watermark_applied":"Vannmerket er brukt på alle sider.",
        "watermark_saved":"Vannmerke lagret.",
        "image_scale":"Størrelse:",
        "image_preview":"Bildeforhåndsvisning:",
        "no_image_selected":"Ingen bilde valgt",
        "browse":"Bla gjennom...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Sensureringer",
        "redact_add_black": "Sensurering (svart)",
        "redact_add_white": "Sensurering (hvit / slett)",
        "redact_added_black": "Svart sensurering lagt til",
        "redact_added_white": "Hvit sensurering lagt til",
        "redact_apply_all": "Bruk alle sensureringer og lagre",
        "redact_discard_all": "Forkast alle sensureringer",
        "redact_discard": "Forkast denne sensureringen",
        "no_redactions": "Ingen sensureringer",
        "redact_confirm_title": "Bruk sensureringer permanent",
        "redact_confirm_message": "Advarsel: De merkede områdene vil bli permanent slettet (svart eller hvitt).\nEn sikkerhetskopi vil bli opprettet (hvis aktivert).\n\nFortsette?",
        "redact_apply": "Ja, sensurer nå",
        "redact_saved": "{0} sensurering(er) ble brukt og lagret.",
        "redact_saved_voice": "{0} sensurering(er) brukt",
        "redact_error": "Feil under sensurering",
        "filename_redacted":"_sensurert",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Sett inn sidetall',
        'page_numbers_format': 'Tallformat:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabisk)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romersk små)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romersk store)',
        'page_numbers_format_letter': 'A, B, C ... (bokstaver)',
        'page_numbers_format_custom': 'Tilpasset',
        'page_numbers_custom_pattern': 'Mønster:',
        'page_numbers_custom_placeholder': 'f.eks. "Side {nummer}" eller "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Bruk {nummer} for gjeldende sidetall og {total} for totalt antall',
        'page_numbers_position': 'Posisjon:',
        'page_numbers_pos_tl': 'Oppe venstre',
        'page_numbers_pos_tc': 'Oppe midten',
        'page_numbers_pos_tr': 'Oppe høyre',
        'page_numbers_pos_ml': 'Midten venstre',
        'page_numbers_pos_mc': 'Sentrert',
        'page_numbers_pos_mr': 'Midten høyre',
        'page_numbers_pos_bl': 'Nede venstre',
        'page_numbers_pos_bc': 'Nede midten',
        'page_numbers_pos_br': 'Nede høyre',
        'page_numbers_margins': 'Marginer:',
        'page_numbers_margin_x': 'Horisontal avstand:',
        'page_numbers_margin_y': 'Vertikal avstand:',
        'page_numbers_range': 'Sideområde:',
        'page_numbers_all_pages': 'Alle sider',
        'page_numbers_custom_range': 'Tilpasset område',
        'page_numbers_from': 'Fra:',
        'page_numbers_to': 'Til:',
        'page_numbers_progress': 'Setter inn sidetall...',
        'page_numbers_start': 'Starter innsetting av sidetall...',
        'page_numbers_cancel': 'Innsetting av sidetall avbrutt',
        'page_numbers_success': 'Sidetall ble lagt til.\n\nVil du åpne den nye PDF-en?\n\n{0}',
        'page_numbers_complete': 'Sidetall lagt til',
        'page_numbers_error_format': 'Feil under innsetting av sidetall: {0}',
        'page_numbers_content_type': 'Innholdstype:',
        'page_numbers_tab_simple': 'Enkelt tall',
        'page_numbers_tab_range': 'Side X av Y',
        'page_numbers_tab_date': 'Dato',
        'page_numbers_tab_custom': 'Fri tekst',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Side {aktuell} av {gesamt}',
        'page_numbers_range_custom': 'Tilpasset',
        'page_numbers_range_placeholder': 'f.eks. "Side {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Datoformat:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. januar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Tilpasset',
        'page_numbers_date_placeholder': 'f.eks. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Posisjon:',
        'page_numbers_date_before': 'Dato før sidetall',
        'page_numbers_date_after': 'Dato etter sidetall',
        'page_numbers_date_only': 'Kun dato (uten sidetall)',
        'page_numbers_custom_text': 'Tilpasset tekst:',
        'page_numbers_custom_placeholder_text': 'Bruk {seite} for sidetall og {gesamt} for totalt antall\nf.eks. "Konfidensielt - Side {seite}" eller "{seite} av {gesamt}"',
        "filename_with_page_number":"_med_sidenummer",
        "filename_with_page_declaration":"_med_sideangivelse",
        "filename_with_pagenumber":"_med_sidenummer",
        "filename_with_date":"_med_dato",
        "filename_with_my_page_declaration":"_med_egen_sideangivelse",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Ulagrede endringer",
        "unsaved_changes_message_darkmode": "Det er ulagrede innsettinger.\nVil du lagre dem før du bytter?",
        "save_and_switch": "Lagre og bytt",
        "discard_and_switch": "Bytt nå",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Eksporter sider som bilder',
        'export_images_menu': 'Eksporter som bilder (PNG/JPEG)',
        'export_images_format': 'Bildeformat:',
        'export_images_dpi': 'Oppløsning (DPI):',
        'export_images_quality': 'JPEG-kvalitet:',
        'export_images_range': 'Sideområde:',
        'export_images_all_pages': 'Alle sider',
        'export_images_custom_range': 'Tilpasset område',
        'export_images_from': 'Fra:',
        'export_images_to': 'Til:',
        'export_images_options': 'Alternativer:',
        'export_images_single_files': 'Hver side som separat fil',
        'export_images_subfolder': 'Eksporter til undermappe',
        'export_images_subfolder_info': 'Til undermappe "PDFnavn_bilder"',
        'export_images_same_folder': 'I samme mappe som PDF-en',
        'export_images_apply_darkmode': 'Bruk PDFDarkView-innstillinger (Mørk modus)',
        'export_images_target_folder': 'Målmappe:',
        'export_images_browse': 'Bla gjennom...',
        'export_images_preview': 'Forhåndsvisning:',
        'export_images_preview_info': 'Velg innstillinger for eksport',
        'export_images_preview_info_detail': '{0} sider som {1}\nOppløsning: {2} DPI\nFilnavn: {3}\n{4}',
        'export_images_select_folder': 'Velg målmappe',
        'export_images_start': 'Starter bildeeksport...',
        'export_images_progress': 'Eksporterer bilder...',
        'export_images_saving': 'Lagrer side {0} av {1}...',
        'export_images_success': 'Eksport vellykket!\n\n{0} bilder ble lagret i:\n{1}',
        'export_images_complete': 'Bildeeksport fullført',
        'export_images_open_folder': '📁 Åpne mappe',
        'export_images_cancel': 'Bildeeksport avbrutt',
        'export_images_error_format': 'Feil under eksport av bilder: {0}',
        'export_images_pdf2image_missing': 'Biblioteket "pdf2image" er ikke installert.\n\nInstaller det med:\npip install pdf2image\n\nFor Windows trenger du også Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A-konvertering for langtidsarkivering',
        'pdfa_menu': 'PDF/A-konvertering (arkivklar)',
        'pdfa_info': 'Konverterer PDF-en til PDF/A-format.\n\nPDF/A er spesielt utviklet for langtidsarkivering og sikrer at dokumentet vises riktig i fremtiden.',
        'pdfa_standard': 'PDF/A-standard:',
        'pdfa_standard_select': 'Versjon:',
        'pdfa_1': 'PDF/A-1 (enkel, bredt kompatibel)',
        'pdfa_2': 'PDF/A-2 (moderne, bedre komprimering)',
        'pdfa_3': 'PDF/A-3 (nyeste versjon, tillater vedlegg)',
        'pdfa_standards_explanation': '📖 Forklaring av standarder:\n\n'
            '• PDF/A-1: Grunnleggende, kompatibel med eldre systemer (ca. 2005)\n'
            '• PDF/A-2: Mer moderne, bedre komprimering, gjennomsiktighetsstøtte (ca. 2011)\n'
            '• PDF/A-3: Nyeste versjon, tillater innbygging av vedlegg (ca. 2013)\n\n'
            'Anbefaling: PDF/A-2 er et godt kompromiss mellom kompatibilitet og moderne funksjoner.',
        'pdfa_options': 'Alternativer:',
        'pdfa_compress_enable': 'Komprimer PDF (mindre fil)',
        'pdfa_metadata_preserve': 'Bevar metadata (tittel, forfatter, etc.)',
        'pdfa_target_folder': 'Målmappe:',
        'pdfa_browse': 'Bla gjennom...',
        'pdfa_select_folder': 'Velg målmappe',
        'pdfa_ocr_info_unknown': '🔍 Kunne ikke sjekke tekstinnhold.',
        'pdfa_ocr_info_not_needed': '✅ Tekst tilgjengelig - OCR er ikke nødvendig.\nPDF/A kan opprettes direkte.',
        'pdfa_ocr_info_recommended': '⚠️ Ikke tilstrekkelig tekst funnet.\n\nFor søkbare PDF-er anbefaler vi å kjøre OCR først.\nMerk: PDF/A fungerer uten OCR - men teksten vil ikke være søkbar.',
        'pdfa_ocr_info_error': '❌ Feil under sjekking: {0}',
        'pdfa_start': 'Starter PDF/A-konvertering...',
        'pdfa_progress': 'PDF/A-konvertering pågår...',
        'pdfa_success': 'PDF/A-konvertering vellykket!\n\nLagret som:\n{0}\n\nVil du åpne den nye PDF-en?',
        'pdfa_complete': 'PDF/A-konvertering fullført',
        'pdfa_cancel': 'PDF/A-konvertering avbrutt',
        'pdfa_error_format': 'Feil under PDF/A-konvertering:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Biblioteket "ocrmypdf" er ikke installert.\n\nInstaller det med:\npip install ocrmypdf',
        'btn_convert': 'Konverter',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimaliser PDF (reduser filstørrelse)',
        'optimize_menu': 'Optimaliser PDF (filstørrelse)',
        'optimize_info': 'Reduserer filstørrelsen til PDF-en gjennom ulike optimaliseringsmetoder.\n\nJo høyere komprimeringsnivå, jo mindre blir filen - med mulig kvalitetstap i bilder.',
        'optimize_level': 'Komprimeringsnivå:',
        'optimize_level_low': 'Lav (rask, liten besparelse)',
        'optimize_level_medium': 'Middels (godt kompromiss)',
        'optimize_level_high': 'Høy (stor besparelse)',
        'optimize_level_maximum': 'Maksimum (maksimal besparelse, treg)',
        'optimize_level_explanation': 'Anbefaling: "Middels" er et godt kompromiss mellom hastighet og filstørrelse.',
        'optimize_options': 'Alternativer:',
        'optimize_compress_images': 'Komprimer bilder (reduser JPEG-kvalitet)',
        'optimize_clean_objects': 'Fjern ubrukte objekter',
        'optimize_preserve_metadata': 'Bevar metadata (tittel, forfatter, etc.)',
        'optimize_image_quality': 'Bildekvalitet:',
        'optimize_range': 'Sideområde:',
        'optimize_all_pages': 'Alle sider',
        'optimize_custom_range': 'Tilpasset område',
        'optimize_from': 'Fra:',
        'optimize_to': 'Til:',
        'optimize_target_folder': 'Målmappe:',
        'optimize_browse': 'Bla gjennom...',
        'optimize_select_folder': 'Velg målmappe',
        'optimize_info_box': 'Informasjon',
        'optimize_info_text': 'Optimalisering kan ta flere minutter for store PDF-er.\n\nBilder lagres med redusert kvalitet, noe som kan redusere filstørrelsen betydelig.',
        'optimize_start': 'Starter PDF-optimalisering...',
        'optimize_progress': 'Optimaliserer PDF...',
        'optimize_cancel': 'PDF-optimalisering avbrutt',
        'optimize_complete': 'PDF-optimalisering fullført',
        'optimize_error_format': 'Feil under PDF-optimalisering:\n\n{0}',
        'optimize_success_message': 'PDF-optimalisering vellykket!\n\nLagret som:\n{0}\n\nFør: {1}\nEtter: {2}\nBesparelse: {3:.1f}%\n\n{4}\n\nVil du åpne den optimaliserte PDF-en?',
        'optimize_success_message_no_size': 'PDF-optimalisering vellykket!\n\nLagret som:\n{0}\n\nStørrelsesinformasjon ikke tilgjengelig.\n\nVil du åpne den optimaliserte PDF-en?',
        'optimize_result_positive': 'Filen ble redusert med {0:.1f}%.',
        'optimize_result_zero': 'Ingen endring i filstørrelse.',
        'optimize_result_negative': 'Filen har økt med {0:.1f}%.\nOptimalisering ble hoppet over, den originale filen ble bevart.',
        'btn_optimize': 'Start optimalisering',
        'filename_optimize_low_suffix': '_optimalisert_lav',
        'filename_optimize_medium_suffix': '_optimalisert',
        'filename_optimize_high_suffix': '_optimalisert_høy',
        'filename_optimize_maximum_suffix': '_optimalisert_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Beskjær PDF',
        'crop_menu': 'Beskjær PDF (Crop)',
        'crop_range': 'Bruk på:',
        'crop_all_pages': 'Alle sider',
        'crop_current_page': 'Kun gjeldende side',
        'crop_values': 'Beskjæringsverdier (i punkter):',
        'crop_left': 'Venstre:',
        'crop_right': 'Høyre:',
        'crop_top': 'Topp:',
        'crop_bottom': 'Bunn:',
        'crop_presets': 'Forhåndsinnstillinger:',
        'crop_preset_white': 'Oppdag hvite marginer',
        'crop_reset': 'Tilbakestill',
        'crop_mouse_hint': '🖱️ Dra et rektangel for å grovt velge området.\nDeretter kan du justere verdiene nøyaktig i SpinBoxene.\nManuell justering med musen er ikke mulig.',
        'crop_apply': 'Beskjær',
        'crop_scope_all': 'Alle sider',
        'crop_scope_current': 'Gjeldende side',
        'crop_new_size': 'Ny størrelse: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Ingen PDF lastet',
        'crop_preview_error': 'Feil ved lasting av forhåndsvisning',
        'crop_start': 'Starter beskjæring...',
        'crop_progress': 'Beskjærer PDF...',
        'crop_success': 'PDF beskjært!\n\nLagret som:\n{0}\n\nVil du åpne den beskårne PDF-en?',
        'crop_complete': 'Beskjæring fullført',
        'crop_cancel': 'Beskjæring avbrutt',
        'crop_error_format': 'Feil under beskjæring:\n\n{0}',
        'filename_crop_suffix': '_beskåret',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Flat ut PDF (Flatten)',
        'flatten_menu': 'Flat ut PDF (Flatten)',
        'flatten_info': 'Å flate ut en PDF "brenner" alle redigerbare elementer inn i sideinnholdet.\n\nEtter dette er skjemafelt, merknader, tekster, kryss, signaturer, bilder og former ikke lenger individuelt redigerbare.',
        'flatten_explanation_title': '📖 Hva er dette bra for?',
        'flatten_explanation_text': 'Utflating er nødvendig i følgende situasjoner:\n\n'
            '• 📄 Du vil forberede dokumentet for utskrift\n'
            '• 🔒 Du vil forhindre at noen endrer skjemafelt\n'
            '• 📎 Du vil "permanent" legge inn merknader og kommentarer i dokumentet\n'
            '• 🖼️ Du vil permanent forankre innsatte tekster, kryss, signaturer, bilder og former i dokumentet\n'
            '• 📦 Du vil forberede filen for arkivering\n\n'
            'Utflating gjør PDF-en mindre og forhindrer at elementer flyttes eller slettes ved et uhell.',
        'flatten_what_title': 'Hva flates ut?',
        'flatten_what_list': '• ✅ Skjemafelt (tekstfelt, avmerkingsbokser, knapper)\n'
            '• ✅ Merknader (kommentarer, uthevinger, notater)\n'
            '• ✅ Overlegg (tekster, kryss, signaturer, bilder, former)',
        'flatten_options': 'Alternativer:',
        'flatten_forms': 'Flat ut skjemafelt',
        'flatten_annotations': 'Flat ut merknader',
        'flatten_overlays': 'Flat ut overlegg (tekster, kryss, signaturer, bilder, former)',
        'flatten_target_folder': 'Målmappe:',
        'flatten_browse': 'Bla gjennom...',
        'flatten_select_folder': 'Velg målmappe',
        'flatten_warning': '⚠️ Viktig: Utflating er en irreversibel prosess!\n\nEtter utflating kan redigerbare elementer ikke lenger endres eller slettes individuelt.\nLag en sikkerhetskopi på forhånd om nødvendig.',
        'flatten_apply': 'Flat ut',
        'flatten_start': 'Starter utflating...',
        'flatten_progress': 'Flater ut PDF...',
        'flatten_success': 'PDF flatet ut!\n\nLagret som:\n{0}\n\nVil du åpne den utflatede PDF-en?',
        'flatten_complete': 'Utflating fullført',
        'flatten_cancel': 'Utflating avbrutt',
        'flatten_error_format': 'Feil under utflating:\n\n{0}',
        'filename_flatten_suffix': '_flatet_ut',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF-overlegg (Overlay)',
        'overlay_menu': 'PDF-overlegg (Overlay)',
        'overlay_info': 'Legger en PDF (overlegg) oppå en annen PDF.\n\nOverleggs-PDF-en plasseres på basis-PDF-en. Dette er nyttig for vannmerker, logoer, brevhoder eller stempler.',
        'overlay_explanation_title': '📖 Hva er dette bra for?',
        'overlay_explanation_text': 'Overlegg er nødvendig i følgende situasjoner:\n\n'
            '• 🏢 Plassere et firmalogo som vannmerke på hver side\n'
            '• 📄 Plassere et brevhode på en tom PDF\n'
            '• 🖊️ Plassere et stempel-overlegg på et dokument\n'
            '• 🔖 Plassere et vannmerke på alle sider\n'
            '• 📑 Plassere et skjema-overlegg på en mal',
        'overlay_type': 'Overleggstype:',
        'overlay_type_fullpage': 'Hel side (dekkende)',
        'overlay_type_transparent': 'Hel side (gjennomsiktig - anbefalt)',
        'overlay_type_stamp': 'Stempel (posisjonerbart)',
        'overlay_type_info_fullpage': '📄 Overleggs-PDF-en plasseres nøyaktig over hele siden.\nDen hvite bakgrunnen kan fjernes slik at bare innholdet er synlig.',
        'overlay_type_info_transparent': '🔍 Overleggs-PDF-en plasseres over hele siden med gjennomsiktig bakgrunn.\nDen hvite bakgrunnen fjernes automatisk - ideelt for vannmerker og logoer!',
        'overlay_type_info_stamp': '🖊️ Overleggs-PDF-en posisjoneres og skaleres som et stempel.\nPerfekt for logoer, stempler eller signaturer på spesifikke posisjoner.',
        'overlay_remove_background': 'Fjern hvit bakgrunn:',
        'overlay_remove_background_enable': 'Fjern hvit bakgrunn fra overleggs-PDF-en (gjør overlegget gjennomsiktig)',
        'overlay_remove_background_tooltip': 'Fjerner hvite områder fra overleggs-PDF-en slik at den underliggende teksten blir synlig.',
        'overlay_threshold': 'Terskelverdi:',
        'overlay_threshold_hint': '(1-254, høyere = mer hvitt fjernes)',
        'overlay_select_file': 'Velg overleggs-PDF:',
        'overlay_file_placeholder': 'Vennligst velg en PDF-fil for overlegget',
        'overlay_browse': 'Bla gjennom...',
        'overlay_select_overlay': 'Velg overleggs-PDF',
        'overlay_range': 'Sideområde:',
        'overlay_all_pages': 'Alle sider',
        'overlay_custom_range': 'Tilpasset område',
        'overlay_from': 'Fra:',
        'overlay_to': 'Til:',
        'overlay_position': 'Posisjon:',
        'overlay_position_center': 'Midten',
        'overlay_position_top_left': 'Oppe venstre',
        'overlay_position_top_right': 'Oppe høyre',
        'overlay_position_bottom_left': 'Nede venstre',
        'overlay_position_bottom_right': 'Nede høyre',
        'overlay_size': 'Størrelse:',
        'overlay_size_original': 'Original størrelse',
        'overlay_size_fit_page': 'Tilpass til side',
        'overlay_size_custom': 'Tilpasset (%)',
        'overlay_opacity': 'Gjennomsiktighet:',
        'overlay_target_folder': 'Målmappe:',
        'overlay_browse_folder': 'Bla gjennom...',
        'overlay_select_folder': 'Velg målmappe',
        'overlay_warning': '⚠️ Merk: Overleggs-PDF-en plasseres på basis-PDF-en og "brennes" inn i den.\n\nElementene i overleggs-PDF-en kan ikke lenger redigeres individuelt etter lagring.',
        'overlay_apply': 'Overlegg',
        'overlay_start': 'Starter overlegg...',
        'overlay_progress': 'Legger overlegg på PDF...',
        'overlay_success': 'PDF overlagt!\n\nLagret som:\n{0}\n\nVil du åpne den overlagte PDF-en?',
        'overlay_complete': 'Overlegg fullført',
        'overlay_cancel': 'Overlegg avbrutt',
        'overlay_error_format': 'Feil under overlegg:\n\n{0}',
        'overlay_no_file': 'Ingen overleggs-PDF valgt.\n\nVennligst velg en PDF-fil for overlegg.',
        'filename_overlay_suffix': '_overlagt',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Trekk ut bilder fra PDF',
        'extract_images_menu': 'Trekk ut alle bilder',
        'extract_images_info': 'Trekker ut alle bilder fra PDF-en og lagrer dem som separate filer.\n\nBildene lagres i sitt opprinnelige format eller konverteres til et valgt format.',
        'extract_images_format': 'Bildeformat:',
        'extract_images_quality': 'JPEG-kvalitet:',
        'extract_images_options': 'Alternativer:',
        'extract_images_subfolder': 'Trekk ut til undermappe ("PDFnavn_bilder")',
        'extract_images_unique': 'Kun unike bilder (unngå duplikater)',
        'extract_images_range': 'Sideområde:',
        'extract_images_all_pages': 'Alle sider',
        'extract_images_custom_range': 'Tilpasset område',
        'extract_images_from': 'Fra:',
        'extract_images_to': 'Til:',
        'extract_images_target_folder': 'Målmappe:',
        'extract_images_browse': 'Bla gjennom...',
        'extract_images_select_folder': 'Velg målmappe',
        'extract_images_info_box': 'Informasjon',
        'extract_images_info_text': 'Uttrekking kan ta flere minutter for store PDF-er.\n\nBilder lagres med sitt opprinnelige navn (side_bilde).',
        'extract_images_extract': 'Trekk ut',
        'extract_images_start': 'Starter uttrekking...',
        'extract_images_progress': 'Trekker ut bilder...',
        'extract_images_success': '✅ Bilder ble trukket ut!\n\n{0} bilder ble lagret i:\n{1}',
        'extract_images_complete': 'Uttrekking av bilder fullført',
        'extract_images_cancel': 'Uttrekking avbrutt',
        'extract_images_error_format': 'Feil under uttrekking av bilder:\n\n{0}',
        'extract_images_open_folder': '📁 Åpne mappe',
        'extract_images_no_images': 'Ingen bilder funnet i PDF-en.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Flere sider på én side (N-Up)',
        'nup_menu': 'Flere sider på én side (N-Up)',
        'nup_info': 'Arrangerer flere PDF-sider på én side.\n\nIdeelt for kompakte utskrifter, oversikter eller handouts.',
        'nup_layout': 'Oppsett:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Forhåndsvisning:',
        'nup_preview_info': '{0} sider → {1} sider per ark → {2} ark\nOppsett: {3}',
        'nup_order': 'Rekkefølge:',
        'nup_order_horizontal': 'Horisontal (rad for rad)',
        'nup_order_vertical': 'Vertikal (kolonne for kolonne)',
        'nup_order_horizontal_reverse': 'Horisontal baklengs',
        'nup_order_vertical_reverse': 'Vertikal baklengs',
        'nup_range': 'Sideområde:',
        'nup_all_pages': 'Alle sider',
        'nup_custom_range': 'Tilpasset område',
        'nup_from': 'Fra:',
        'nup_to': 'Til:',
        'nup_options': 'Alternativer:',
        'nup_margins': 'Marginer:',
        'nup_margin_between': 'Avstand mellom sider:',
        'nup_page_numbers': 'Sett inn sidetall',
        'nup_target_folder': 'Målmappe:',
        'nup_browse': 'Bla gjennom...',
        'nup_select_folder': 'Velg målmappe',
        'nup_create': 'Opprett',
        'nup_start': 'Starter N-Up...',
        'nup_progress': 'Oppretter N-Up...',
        'nup_success': 'N-Up opprettet!\n\nLagret som:\n{0}\n\nVil du åpne den nye PDF-en?',
        'nup_complete': 'N-Up fullført',
        'nup_cancel': 'N-Up avbrutt',
        'nup_error_format': 'Feil under N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Endre sidestørrelse',
        'pagesize_menu': 'Endre sidestørrelse',
        'pagesize_info': 'Endrer sidestørrelsen på PDF-en.\n\nInnholdet tilpasses automatisk til den nye størrelsen.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Velg et standardformat:',
        'pagesize_custom': 'Tilpasset størrelse:',
        'pagesize_width': 'Bredde:',
        'pagesize_height': 'Høyde:',
        'pagesize_orientation': 'Retning:',
        'pagesize_portrait': 'Stående',
        'pagesize_landscape': 'Liggende',
        'pagesize_scale_options': 'Skaleringsalternativer:',
        'pagesize_fit': 'Tilpass (behold sideforhold)',
        'pagesize_stretch': 'Strekk (forvri)',
        'pagesize_center': 'Sentrer (original størrelse)',
        'pagesize_range': 'Sideområde:',
        'pagesize_all_pages': 'Alle sider',
        'pagesize_custom_range': 'Tilpasset område',
        'pagesize_from': 'Fra:',
        'pagesize_to': 'Til:',
        'pagesize_target_folder': 'Målmappe:',
        'pagesize_browse': 'Bla gjennom...',
        'pagesize_select_folder': 'Velg målmappe',
        'pagesize_apply': 'Bruk',
        'pagesize_start': 'Starter endring av sidestørrelse...',
        'pagesize_progress': 'Endrer sidestørrelse...',
        'pagesize_success': 'Sidestørrelse endret!\n\nLagret som:\n{0}\n\nVil du åpne den nye PDF-en?',
        'pagesize_complete': 'Endring av sidestørrelse fullført',
        'pagesize_cancel': 'Endring av sidestørrelse avbrutt',
        'pagesize_error_format': 'Feil under endring av sidestørrelse:\n\n{0}',
        'pagesize_preview_info': 'Ny størrelse: {0} x {1} pt',
        'filename_pagesize_suffix': '_ny_størrelse',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-informasjon',
        'pdf_info_menu': 'Vis PDF-info',
        'pdf_info_voice': 'Viser PDF-informasjon',
        'pdf_info_error': 'Feil under visning av PDF-info:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Vis tastatursnarveier",
        "shortcuts_dialog_title": "Tastatursnarveier",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FIL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Åpne PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Lukk PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Lagre som...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Beskytt dokument</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Skriv ut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Skriv ut umiddelbart (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Avslutt applikasjonen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Eksporter som Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Eksporter som DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Eksporter som TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Eksporter som bilder (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Trekk ut bilder</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTBEHANDLING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Flere sider)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A-konvertering (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Flat ut PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF-overlegg</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimaliser PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDIGER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Søk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Legg til bokmerke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Administrer bokmerker</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Neste bokmerke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Forrige bokmerke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Kjør OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SIDEADMINISTRASJON</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Roter gjeldende side</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Roter alle sider</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normaliser gjeldende side</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normaliser alle sider</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Slett sider</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Trekk ut sider</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Sett inn sider</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Flytt sider</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Slå sammen PDF-er</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Endre sidestørrelse</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 SETT INN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Sett inn tekst</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Sett inn kryss</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Sett inn signatur 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Sett inn signatur 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Sett inn bilde</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Sett inn rektangel</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Sett inn ellipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Sett inn linje</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Sett inn pil</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Sett inn sidetall</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Tekst-vannmerke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Bilde-vannmerke</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ SENSUERINGER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Sensurering (svart)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Sensurering (hvit)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Bruk alle sensureringer</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ AVANSERT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Beskjær PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Rediger metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VISNING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Bytt Mørk/Lys modus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Vis tekstvindu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Sidebredde (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>To sider (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Oversikt (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ INNSTILLINGER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Passordadministrasjon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR-innstillinger</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Signaturinnstillinger</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Filnavnformatering</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Eksporter innstillinger</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importer innstillinger</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Vis PDF-info</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Slå taleutgang på/av</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokuser menylinje</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Ny versjon tilgjengelig",
        "update_available_message": "Det er en ny versjon <b>{0}</b>.\n\nBesøk utgivelsessiden for å laste ned oppdateringen:\n{1}",
        "update_available_voice": "Ny versjon {0} tilgjengelig. Last ned oppdateringen fra GitHub-siden.",
        "update_open_release": "Åpne utgivelsesside",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Last ned alle oversettelser",
        "ask_download_all_translations": """I tillegg til tysk, engelsk og vietnamesisk er det {total_languages} andre GUI-språk tilgjengelig.\n\nSkal disse tilbys / oppdateres?\n\nMerk:\nUnødvendige språk kan du senere slette manuelt i katalogen:\n{translations_path}
        \nHvis du avbryter, kan du laste ned GUI-språkene senere via menyen 'Verktøy → Oppdater oversettelser'.""",
        "menu_update_translations": "Oppdater oversettelser",
        "translations_updated": "Oversettelser oppdatert",
        "translations_update_success": "{} oversettelser ble oppdatert ({} nye, {} oppdatert).",
        "translations_update_error": "Feil ved oppdatering av oversettelser",
        "translations_update_no_changes": "Alle oversettelser er allerede oppdatert.",
        "translations_update_offline": "Ingen internettforbindelse. Oversettelser kunne ikke oppdateres.",
        "translations_update_in_progress": "Oversettelser oppdateres i bakgrunnen...",
        "translations_downloading": "Laster ned oversettelser...",
        "translations_path_hint": "Brukermappe for oversettelser",
        "translations_update_not_available_title": "Oppdatering ikke tilgjengelig",
        "translations_update_not_available_message": """Oppdatering av oversettelser er kun tilgjengelig i den installerte versjonen.\n\nI utviklingsmodus er oversettelsene allerede oppdatert.""",
        "translations_update_no_internet_title": "Ingen internettforbindelse",
        "translations_update_no_internet_message": """Kunne ikke opprette internettforbindelse.\n\nOversettelser kan ikke lastes ned fra GitHub.\n\nMulige løsninger:
        • Kontroller internettforbindelsen din
        • Deaktiver eventuell brannmur midlertidig
        • Prøv igjen senere
        \nDu kan også laste ned oversettelsene manuelt fra GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Oppdatering pågår allerede",
        "btn_retry": "Prøv igjen",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Velkommen til PDF Dark View",
        "welcome_title_not_supported": "Velkommen til PDF Dark View",
        "welcome_message": "Velkommen til PDF Dark View!\n\nSystemspraket ditt ble gjenkjent som '{language}'.\nVil du bruke dette språket for brukergrensesnittet?\n\nDu kan endre språket når som helst via 'Innstillinger → Språk'.",
        "welcome_message_language_not_available": "Velkommen til PDF Dark View!\n\nSystemspraket ditt ble gjenkjent som '{language}'.\nDette språket er ennå ikke installert.\n\nVil du laste ned oversettelsene for {language} nå fra GitHub?\n\n(Språket vil deretter automatisk bli brukt for brukergrensesnittet.)",
        "welcome_message_language_not_supported": "Velkommen til PDF Dark View!\n\nSystemspraket ditt ble gjenkjent som '{language}'.\nDessverre er det ingen oversettelser for dette språket ennå.\n\nBrukergrensesnittet vil bli vist på {fallback_language}.\n\nDu kan endre språket når som helst via 'Innstillinger → Språk'.\nHvis du vil, kan du også bidra med en oversettelse for ditt språk:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Ja, bruk systemspråk",
        "welcome_keep_english": "Nei, behold engelsk",
        "welcome_download_language": "Ja, last ned {language}",

        # ============================================
        # 107. SIST BRUKTE STIER
        # ============================================

        'menu_recent': 'Sist brukt',
        'menu_recent_dirs': 'Mapper...',
        'menu_recent_files': 'Filer...',
        'recent_manage': 'Administrer...',
        'recent_enable_tracking': 'Lagre sist brukte stier (personvern)',
        'recent_enable_info': 'Deaktiver dette alternativet for ikke å lagre stier',
        'recent_tracking_disabled': 'Stisporing er deaktivert',
        'recent_enabled': 'aktivert',
        'recent_disabled': 'deaktivert',
        'recent_tracking_status': 'Stisporing {0}',
        'recent_dialog_title': 'Sist brukte stier',
        'recent_tab_directories': 'Mapper',
        'recent_tab_files': 'Filer',
        'recent_dirs_instruction': 'Dobbeltklikk for å åpne fildialog i mappen',
        'recent_files_instruction': 'Dobbeltklikk for å åpne PDF direkte',
        'recent_no_directories': '(ingen lagrede mapper)',
        'recent_no_files': '(ingen lagrede filer)',
        'recent_default_current': '⭐ Standard: {0}',
        'recent_set_as_default': '⭐ Sett som standard',
        'recent_default_set_title': 'Standardmappe er satt',
        'recent_default_set_message': 'Mappen "{0}" er satt som standard for åpning av PDF-er.',
        'recent_default_set_voice': 'Standardmappe er satt',
        'recent_directory_not_found': 'Mappe ikke funnet',
        'recent_file_not_found': 'Fil ikke funnet',
        'recent_remove_selected': 'Fjern',
        'recent_remove_title': 'Fjern sti',
        'recent_remove_confirm': 'Vil du virkelig fjerne stien "{0}" fra listen?',
        'recent_path_removed': 'Sti er fjernet',
        'recent_clear_all': 'Fjern alle',
        'recent_clear_title': 'Fjern alle stier',
        'recent_clear_confirm_type': 'Vil du virkelig slette alle {0}?',
        'recent_cleared': 'Listen er tømt',
        'recent_path_not_found_title': 'Sti ikke funnet',
        'recent_path_not_found_message': 'Stien "{0}" finnes ikke lenger.',
        'recent_open_file': 'Åpne fil',
        'btn_open_recent': 'Åpne',
        'recent_open_file_question': 'Vil du åpne "{0}" som PDF?',
        'recent_not_pdf': 'Den valgte filen er ikke en PDF.',
        'recent_more_entries': 'Flere oppføringer...',
        'btn_remove': 'Fjern',
        'btn_clear': 'Tøm alle',
        'recent_context_open': 'Åpne',
        'recent_context_reveal': 'Vis i Finder',
        'recent_context_set_default': '⭐ Sett som standard',
        'recent_context_open_terminal': '💻 Åpne terminal',
        'recent_context_file_info': 'Filinfo',
        'recent_context_open_with_default': '📄 Åpne med standardapp',
        'recent_context_remove': 'Fjern fra liste',
        'recent_context_clear_all': 'Fjern alle',
        'recent_file_info_title': 'Filinformasjon',
        'recent_file_info_name': 'Navn',
        'recent_file_info_path': 'Sti',
        'recent_file_info_size': 'Størrelse',
        'recent_file_info_modified': 'Endret',
        'recent_file_info_pages': 'Sider',
        'recent_error_reveal': 'Feil ved åpning i Finder',
        'recent_error_terminal': 'Feil ved åpning av terminal',
        'recent_error_info': 'Feil ved henting av filinfo',
        'open_user_data_folder': 'Vis brukerdatamappe',

        # ============================================
        # 108. SLETTE LIKE/ULIKE SIDER
        # ============================================
        "pages_delete_even": "Slett alle like sider",
        "pages_delete_odd":  "Slett alle ulike sider",
        "progress_even_pages": "Sletter like sider",
        "progress_odd_pages": "Sletter ulike sider",
        "progress_mark_delete_even": "{} like side(r) merket for sletting",
        "progress_mark_delete_odd":  "{} ulike side(r) merket for sletting",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programmet avsluttes",

    }

