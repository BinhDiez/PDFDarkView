
# ============================================
# translations_sv.py - Svensk ordbok
# Fullständigt sorterad efter kategorier
# Kommentarer på tyska för konsekvens
# ============================================

def load_swedish_strings():
    """Laddar alla svenska strängar"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View av BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Öppna PDF",
        'btn_text_window': "OCR‑text",
        'btn_first': "Första sidan",
        'btn_prev': "Föregående sida",
        'btn_next': "Nästa sida",
        'btn_last': "Sista sidan",
        'btn_print': "Skriv ut",
        'btn_darkmode_light': "Ljust läge",
        'btn_darkmode_dark': "Mörkt läge",
        'btn_delete_pages': "Ta bort sidor",
        'btn_extract_pages': "Extrahera sidor",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Avbryt",
        'btn_save': "Spara",
        'btn_close': "Stäng",
        'btn_delete': "Ta bort",
        'btn_delete_all': "Ta bort alla",
        'btn_copy': "Kopiera",
        'btn_export': "Exportera",
        'btn_show': "Visa lösenord",
        'btn_hide': "Dölj lösenord",
        'btn_authenticate': "Autentisera",
        'btn_settings': "Inställningar",
        'btn_protect': "Skydda",
        'btn_remove_password': "Ta bort lösenord",
        'btn_manage': "Lösenordshantering",
        'btn_retry': "Försök igen",
        'btn_select_all': "Markera alla",
        'btn_clear_selection': "Avmarkera",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Sida {0} av {1}",
        'page_count': "av {0}",
        'goto_page': "Gå till sida",
        'page_simple': "Sida {0}",
        'full_view_page': "Full visning sida {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Ange sökterm + Retur",
        'search_results': "Resultat: {0} av {1}",
        'search_nav_hint': "Retur: nästa  (Shift+Retur: föregående) träff",
        'search_no_results': "Inga träffar",
        'search_error': "Sökfel",
        'search_active': "Sökfält aktiverat",
        'search_closed': "Sökning avslutad",
        'search_position': "Sida {0} {1}",
        'search_pos_top': "längst upp",
        'search_pos_upper': "upptill",
        'search_pos_middle': "mitten",
        'search_pos_lower': "nedtill",
        'search_pos_bottom': "längst ner",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Textigenkänning slutförd!",
        'ocr_success_title': "OCR lyckades",
        'ocr_success_message': "Dokumentet är nu sökbart.",
        'ocr_failed': "OCR misslyckades",
        'ocr_in_progress': "OCR pågår",
        'ocr_preparing': "Förbereder PDF...",
        'ocr_analyzing': "Analyserar PDF...",
        'ocr_optimizing': "Bildoptimering pågår...",
        'ocr_recognizing': "Textigenkänning pågår...",
        'ocr_embedding': "Bäddar in text...",
        'ocr_finalizing': "Slutför PDF...",
        'ocr_not_available': "OCR inte tillgängligt",
        'ocr_install_message': "OCR‑verktyg hittades inte.\n\nInstallera:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR krävs",
        'ocr_question': "PDF:en innehåller ingen sökbar text.\nVill du köra OCR för att möjliggöra {0}?",
        'ocr_perform': "Kör OCR",
        'ocr_later': "Senare",
        'ocr_starting': "Startar garanterad OCR...",
        'ocr_success_voice': "OCR lyckades. PDF är nu sökbar.",
        'ocr_partial_success': "OCR utfördes, men det uppstod problem vid ersättning.\n\nDen sökbara versionen sparades som:\n{0}\n\nFel: {1}",
        'ocr_partial_title': "OCR delvis lyckat",
        'ocr_partial_voice': "OCR utfördes, men ersättning misslyckades.",
        'original_file': "Originalfil:",
        'old_size': "Gamla filstorleken:    {0} byte",
        'new_size': "Nya filstorleken: {0} byte",
        'size_change': "Ändring: {0}{1} byte",
        'backup_created_file': "Säkerhetskopia skapad:\n{0}",
        'backup_not_created': "Säkerhetskopia: ej skapad (inställning avaktiverad)",
        'page_header': "=== Sida {0} ===\n{1}\n",
        'scanned_page_header': "=== Sida {0} (skannad) ===\n[Denna sida innehåller endast skannad text]\n[Utför OCR manuellt]\n",
        'scanned_warning': "⚠️ SKANNAD TEXT - OCR KRÄVS",
        'guaranteed_title': "Sökbar PDF skapad",
        'guaranteed_message': "<b>Garanterad sökbar version skapad!</b>\n\nEftersom automatisk OCR misslyckades, skapades en alternativ sökbar PDF:\n\n{0}\n\n<b>Denna fil innehåller:</b>\n• Extraherad text (om tillgänglig)\n• Anvisningar för skannade sidor\n• Är fullt sökbar",
        'guaranteed_voice': "Garanterad sökbar PDF skapad.",
        'instruction_title': "INSTRUKTION FÖR OCR",
        'instruction_file': "Originalfil: {0}",
        'instruction_text': "Automatisk textigenkänning (OCR) misslyckades.\nUtför OCR manuellt:\n\n1. MED OCRmyPDF (kommandorad):\n   ocrmypdf --force-ocr \"[FIL]\" \"utdata.pdf\"\n\n2. MED ADOBE ACROBAT (macOS/Windows):\n   • Öppna PDF i Acrobat\n   • Verktyg > Redigera PDF\n   • Välj 'Känn igen text'\n\n3. MED FÖRHANDSVISNING (macOS):\n   • Öppna PDF i Förhandsvisning\n   • Arkiv > Exportera...\n   • Quartz‑filter: 'Minska filstorlek'\n   • Aktivera 'Utför OCR'\n\n4. ONLINE OCR‑TJÄNSTER:\n   • smallpdf.com/sv/ocr-pdf\n   • ilovepdf.com/sv/ocr-pdf\n   • adobe.com/se/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR‑instruktion skapad",
        'instruction_created_message': "En detaljerad instruktion skapades:\n\n{0}\n\nFölj stegen för manuell OCR.",
        'instruction_created_voice': "OCR‑instruktion skapad.",
        'ocr_impossible': "OCR inte möjlig",
        'ocr_impossible_message': "OCR kunde inte utföras.\n\nBearbeta '{0}' manuellt med OCR‑programvara.",
        'ocr_impossible_voice': "OCR inte möjlig. Utför manuell bearbetning.",
        'emergency_title': "Nöd‑OCR",
        'emergency_message': "En nöd‑PDF skapades:\n\n{0}\n\nBearbeta denna fil manuellt med OCR.",
        'emergency_voice': "Nöd‑PDF skapad. Utför OCR manuellt.",
        'critical_error': "Kritiskt fel",
        'critical_error_message': "OCR kunde inte startas.\n\nStarta om programmet och\nkontrollera OCR‑installationen.",
        'critical_error_voice': "Kritiskt OCR‑fel",
        'ocr_question_html': "<p>PDF:en innehåller ingen sökbar text.<p>Vill du köra OCR för att möjliggöra <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR krävs. PDF:en innehåller ingen sökbar text. Vill du köra OCR för att möjliggöra {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ingen PDF inläst",
        'no_pdf_message': "Ingen PDF är inläst",
        'pdf_not_found': "PDF‑fil hittades inte",
        'file_size': "Filstorlek",
        'bytes': "byte",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Säkerhetskopia skapad",
        'backup_disabled': "Säkerhetskopia inaktiverad",
        'backup_activated': "Säkerhetskopiering aktiverad",
        'backup_deactivated': "Säkerhetskopiering avaktiverad",
        'backup_status': "Säkerhetskopia: {0}",
        'backup_on': "✔ aktiverad",
        'backup_off': "✘ inaktiverad",
        'close_pdf': "Stänger PDF: {0}",
        'pdf_not_found_format': "PDF‑fil hittades inte: {0}",
        'error_pdf_load_format': "Fel vid inläsning av PDF: {0}",
        'load_failed_format': "Inläsning misslyckades:\n{0}",
        'decrypted_suffix': "(dekrypterad)",
        'decryption_failed': "Dekryptering misslyckades.",
        'decryption_error': "Fel vid dekryptering",
        'decryption_success': "Dekryptering lyckades",
        'decryption_success_message': "PDF dekrypterades och sparades som:\n\n{0}",
        'decryption_success_voice': "PDF dekrypterades och sparades.",
        'password_remove_error': "Fel vid borttagning av lösenord",
        'save_unencrypted': "Spara okrypterad PDF som",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Spara som...",
        'save_copy': "Spara kopia",
        'save_success': "PDF sparad som: {0}",
        'save_encrypted': "Skyddad PDF sparad som: {0}",
        'save_error': "PDF kunde inte sparas",
        'encryption_question': "Vill du skydda PDF:en med ett lösenord?",
        'encryption_yes': "Ja",
        'encryption_no': "Nej",
        'encryption_cancel': "Avbryt",
        'save_cancel': "Sparande avbröts",
        'save_encrypted_voice': "Fil krypterad och sparad.",
        'save_success_voice': "PDF‑filen sparades okrypterad.",
        'save_error_format': "PDF kunde inte sparas:\n{0}",
        'export_pages_success': "Pages‑export lyckades",
        'export_pages_error': "Pages‑export misslyckades",
        'export_pages_error_format': "Pages‑export misslyckades: {0}",
        'export_word_success': "Word‑export lyckades",
        'export_word_error': "Word‑export misslyckades",
        'export_word_error_format': "Word‑export misslyckades: {0}",
        'export_text_success': "Textexport lyckades",
        'export_text_error': "Textexport misslyckades",
        'export_text_error_format': "Textexport misslyckades: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Lösenord krävs",
        'password_enter': "Ange lösenord",
        'password_confirm': "Bekräfta lösenord",
        'password_new': "Nytt lösenord",
        'password_current': "Nuvarande lösenord",
        'password_save': "Spara lösenord (krypterat)",
        'password_saved': "✓ Lösenord för denna fil är sparat",
        'password_wrong': "Fel lösenord",
        'password_mismatch': "Lösenorden stämmer inte överens",
        'password_too_short': "Lösenordet är för kort",
        'password_min_length': "Lösenordet måste vara minst 4 tecken långt",
        'password_strength': "Lösenordsstyrka",
        'password_strength_very_weak': "Mycket svagt",
        'password_strength_weak': "Svagt",
        'password_strength_medium': "Medel",
        'password_strength_strong': "Starkt",
        'password_strength_very_strong': "Mycket starkt",
        'password_char_count': "({0} tecken)",
        'password_match': "✓ Överensstämmer",
        'password_no_match': "✗ Lösenorden stämmer inte överens",
        'password_show': "Visa",
        'password_hide': "Dölj",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Lösenordshantering",
        'password_table_filename': "Filnamn",
        'password_table_password': "Lösenord",
        'password_count': "{0} sparat lösenord",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Inga sparade lösenord",
        'password_copied': "{0} lösenord kopierat",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Vill du verkligen ta bort lösenordet för '{0}'?",
        'password_delete_multiple': "Vill du verkligen ta bort de {0} valda lösenorden?",
        'password_delete_all_confirm': "Vill du verkligen ta bort alla {0} sparade lösenord?",
        'password_deleted': "{0} lösenord borttaget",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Alla lösenord har tagits bort",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Lösenordsgenerator",
        'generator_generated': "Genererat lösenord:",
        'generator_regenerate': "Generera igen",
        'generator_copy': "Kopiera",
        'generator_use': "Använd",
        'generator_settings': "Inställningar",
        'generator_length': "Längd:",
        'generator_group_every': "Avgränsare varje",
        'generator_group_chars': "tecken.   Avgränsare:",
        'generator_uppercase': "Versaler (A‑Z)",
        'generator_lowercase': "Gemener (a‑z)",
        'generator_digits': "Siffror (0‑9)",
        'generator_symbols': "Symboler (!@#$%^&*)",
        'generator_exclude': "Uteslutna:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Huvudlösenord krävs",
        'master_password_setup': "Skapa huvudlösenord",
        'master_password_change': "Ändra huvudlösenord",
        'master_password_enter': "Ange ditt huvudlösenord",
        'master_password_choose': "Välj ett starkt huvudlösenord (minst 8 tecken)",
        'master_password_new': "Ange ditt nya huvudlösenord",
        'master_password_confirm': "Bekräfta lösenord",
        'master_password_authenticate': "Autentisera",
        'master_password_success': "Huvudlösenord skapat.",
        'master_password_changed': "Huvudlösenord ändrat.",
        'master_password_removed': "Huvudlösenord och alla lösenord borttagna.",
        'master_password_remove': "Ta bort huvudlösenord",
        'master_password_remove_confirm': "Är du SÄKER på att du vill ta bort ALLA lösenord?\n\nDenna åtgärd är OÅTERKALLELIG!",
        'master_password_export_before': "Vill du exportera en säkerhetskopia först?",
        'master_password_export_delete': "Exportera och ta bort",
        'master_password_delete_now': "Ta bort nu",
        'master_password_for_signatures': "För att använda signaturer måste du skapa ett huvudlösenord.\n\nVill du skapa ett huvudlösenord nu?",
        'master_password_for_private': "För att använda privata textblock måste du skapa ett huvudlösenord.\n\nVill du skapa ett huvudlösenord nu?",
        'master_password_info': """
            <b>🔐 UTAN HUVUDLÖSENORD:</b><br>
            • Ingen visning, kopiering eller export av lösenord möjlig<br>
            • Borttagning av lösenord är alltid möjlig (även utan huvudlösenord)<br><br>

            <b>🔐 MED HUVUDLÖSENORD:</b><br>
            • Alla funktioner tillgängliga efter autentisering<br>
            • Lösenord krypteras med huvudlösenordet<br>
            • Minsta längd: 8 tecken<br>
            • Säker SHA‑256 hash‑lagring<br><br>

            <b>VIKTIGT:</b><br>
            • Om huvudlösenordet förloras kan lösenorden inte återställas<br>
            • När huvudlösenordet tas bort raderas ALLA lösenord<br>
            • Exportmöjlighet före borttagning<br>
            • Huvudlösenordet kan alltid ändras
        """,
        'signature_auth_disabled': "Inaktivera lösenordsfråga för signaturer",
        'template_auth_disabled': "Inaktivera lösenordsfråga för privata textblock",
        'master_password_for_signatures_settings': "För att använda signaturer måste du skapa ett huvudlösenord.\n\nGå till Inställningar – Lösenordshantering",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Skydda PDF",
        'protect_info': "Filen '{0}' kommer att skyddas med ett lösenord.",
        'protect_instruction': "Ange önskat lösenord två gånger för att skydda dokumentet, eller använd lösenordsgeneratorn till höger om inmatningsfältet.",
        'protect_success': "PDF skyddades och sparades som:\n{0}\n\nLösenord: {1}\n\nVill du öppna den skyddade PDF:en nu?",
        'protect_open': "Ja",
        'protect_skip': "Nej",
        'protect_error': "Fel vid skydd av PDF",
        'protect_open_title': "öppna skyddad PDF",
        'protect_question': "Klart. Vill du öppna den skyddade PDF:en nu? Ja eller Nej?",
        'password_cancel': "Lösenordsdialog avbruten",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Ta bort sidor",
        'pages_extract': "Extrahera sidor",
        'pages_insert': "Infoga sidor",
        'pages_move': "Flytta sidor",
        'pages_delete_options': "Borttagningsalternativ",
        'pages_delete_empty': "Ta bort alla tomma sidor",
        'pages_delete_current': "Ta bort aktuell sida",
        'pages_delete_range': "Ta bort sidintervall",
        'pages_extract_options': "Extraheringsalternativ",
        'pages_extract_current': "Extrahera aktuell sida",
        'pages_extract_range': "Extrahera sidintervall",
        'pages_insert_position': "Infogningsposition",
        'pages_insert_before': "Infoga före sida:",
        'pages_insert_select': "Välj PDF",
        'pages_insert_none': "Ingen PDF vald",
        'pages_move_source': "Sidor att flytta",
        'pages_move_from': "Från sida:",
        'pages_move_to': "Till sida:",
        'pages_move_target': "Målposition",
        'pages_move_before': "Flytta före sida:",
        'pages_move_hint': "Obs: sida 1 = början, {0} = slut",
        'pages_range_invalid': "Startsidan måste vara mindre än eller lika med slutsidan.",
        'pages_position_invalid': "Målpositionen får inte ligga inom det intervall som ska flyttas.",
        'pages_no_pdf_selected': "Ingen PDF är vald.",
        'pages_deleted': "{0} sidor togs bort.",
        'pages_extracted': "Extraherad: {0}\nSparad som: {1}\nFilstorlek: {2:.1f} KB",
        'pages_inserted': "{0} sidor infogade",
        'pages_moved': "{0} sidor flyttades.",
        'pages_deleted_none': "Inga sidor togs bort.",
        'pages_delete_progress': "Tar bort sidor...",
        'pages_deleted_with_backup': "{0} sidor togs bort.\n\nSäkerhetskopia: {1}",
        'pages_deleted_voice': "En säkerhetskopia skapades och {0} sidor togs bort.",
        'info': "Information",
        'error_dialog_creation': "Dialog kunde inte skapas",
        'extract_page_single': "Extrahera sida {0}",
        'extract_page_range': "Extrahera sidorna {0}‑{1}",
        'extract_success_voice': "Sidor extraherade",
        'extract_error_format': "Fel vid extrahering: {0}",
        'pages_inserted_voice': "{0} sidor infogade.",
        'insert_error_format': "Fel vid infogning: {0}",
        'pages_move_progress': "Flyttar sidor...",
        'pages_moved_with_backup': "{0} sidor flyttades.\n\nSäkerhetskopia: {1}",
        'move_success_title': "Flytt lyckades",
        'pages_moved_voice': "{0} sidor flyttades",
        'mark_removed': "Markering borttagen från sida {0}",
        'mark_empty': "Sida {0} markerad som tom",
        'mark_export_removed': "Exportmarkering borttagen från sida {0}",
        'mark_export': "Sida {0} markerad för export",
        'no_empty_pages': "Inga tomma sidor markerade för borttagning",
        'delete_empty_confirm': "Vill du ta bort alla {0} markerade tomma sidor?",
        'delete_empty_confirm_voice': "Ta bort alla {0} markerade tomma sidor nu? Ja eller Nej.",
        'empty_pages_deleted': "{0} tomma sidor borttagna",
        'no_export_pages': "Inga sidor markerade för export",
        'overwrite_title': "Skriv över befintlig fil",
        'overwrite_question': "Filen\n\n{0}\n\nfinns redan.\nVill du skriva över den?",
        'overwrite_voice': "Skriv över befintlig fil? Ja eller Nej.",
        'page_skipped': "Sida {0} hoppades över",
        'export_complete': "Export klar.",
        'export_complete_voice': "Exporten är klar.",
        'no_pages_exported': "Ingen sida exporterad",
        'export_cancelled': "Export avbruten",
        'pages_exported': "{0} sidor exporterade till {1}",
        'export_page_title': "Exportera sida",
        'page_exported': "Sida {0} exporterad till {1}",
        'export_error': "Fel vid export",
        'export_marked_title': "Exportera markerade sidor",
        'rotate_all_title': "rotera alla sidor",
        'rotate_all_question': "Vill du rotera alla sidor 90 grader åt höger?",
        'rotate_all_voice': "Vill du rotera alla sidor 90 grader åt höger? Ja eller Nej?",
        'all_pages_rotated': "Alla sidor roterade",
        'page_rotated': "Sida {0} roterad",
        'rotate_error': "Sidan kunde inte roteras",
        'delete_page_confirm': "Vill du ta bort sida {0}?",
        'delete_page_confirm_voice': "Vill du verkligen ta bort sida {0}? Ja eller Nej.",
        'page_deleted': "Sida {0} borttagen",
        'delete_error': "Sidan kunde inte tas bort",
        'pages_deleted_voice': "{0} sidor borttagna",
        'pages_exported_split': "{0} sidor exporterades.",
        'pages_skipped': "{0} sidor hoppades över.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extrahera sidor (avancerat)",
        'pdf_splitter_title': "PDF‑splittrare och extraktor",
        'pdf_splitter_load': " Välj PDF‑fil",
        'pdf_splitter_info': "Välj ett alternativ för ditt PDF‑dokument",
        'pdf_splitter_basic': "Grundläggande operationer",
        'pdf_splitter_single': "Dela upp i enskilda sidor",
        'pdf_splitter_range': "Extrahera sidor:",
        'pdf_splitter_range_placeholder': "t.ex. 1‑3,5,7‑9",
        'pdf_splitter_clean': "Rengöringsoperationer",
        'pdf_splitter_remove_empty': "Ta bort alla tomma sidor",
        'pdf_splitter_remove': "Ta bort sidintervall:",
        'pdf_splitter_remove_placeholder': "t.ex. 2,4‑6",
        'pdf_splitter_process': "Bearbeta PDF",
        'pdf_splitter_loaded': "PDF inläst. Välj ett alternativ",
        'pdf_read_error': "PDF kunde inte läsas",
        'pages': "Sidor",
        'pages_created': "Sidor skapades",
        'range_empty': "Ange ett sidintervall",
        'range_invalid': "Ogiltigt sidintervall",
        'range_created': "Ny PDF med valda sidor skapades:\n{0}",
        'empty_removed': "{0} tomma sidor borttagna.\nUtdata: {1}",
        'remove_empty': "Ange sidor att ta bort",
        'remove_invalid': "Ogiltiga sidor att ta bort",
        'remove_done': "Rengjord PDF skapad:\n{0}",
        'open_folder': "Öppna mapp",
        'show_in_finder': "Visa i Finder",
        'pdf_splitter_no_pdf': "Läs först in en PDF‑fil.",
        'process_error': "Fel vid bearbetning av PDF",
        'pages_created_voice': "{0} sidor skapades",
        'range_created_voice': "PDF med valda sidor skapades",
        'empty_removed_voice': "{0} tomma sidor togs bort",
        'remove_done_voice': "Rengjord PDF skapades",
        'pdf_splitter_split_groups': "Varje sammanhängande grupp i separat fil",
        'range_created_single': "Ny PDF skapad:\n{0}",
        'range_created_multiple': "{0} PDF‑filer skapades.",
        'range_created_voice_single': "En PDF med valda sidor skapades",
        'range_created_voice_multiple': "{0} PDF‑filer skapades",
        'empty_removed_none_left': "Inga sidor kvar",
        'empty_removed_all_empty': "Alla sidor upptäcktes som tomma och skulle tas bort. Ingen fil skapades.",
        'preview_single': "Förhandsgranskning: {0}",
        'preview_enter_range': "Ange ett sidintervall.",
        'preview_invalid_range': "Ogiltigt sidintervall.",
        'preview_file': "Förhandsgranskning: {0}",
        'preview_files': "Förhandsgranskning: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Startar utskrift",
        'print_sent': "Utskriftsjobb skickat",
        'print_now': "Skriv ut nu",
        'print_error': "Fel vid direktutskrift",
        'print_limited': "Utskriftsfunktionen är begränsad på detta system",
        'print_error_format': "Fel vid direktutskrift: {0}",
        'warning': "Obs",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Växla till ljust läge",
        'mode_switch_to_dark': "Växla till mörkt läge",
        'mode_dark_activated': "Mörkt läge aktiverat",
        'mode_light_activated': "Ljust läge aktiverat",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Full visning",
        'zoom_two_pages': "Två sidor bredvid varandra",
        'zoom_overview': "Översiktsläge",
        'zoom_cannot_during_search': "Zoom inte möjligt under sökning",
        'zoom_exit_first': "Lämna först zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Dra och släpp aktiverat",
        'drag_disabled': "Dra och släpp inaktiverat",
        'drag_page_grab': "Griper sida {0}",
        'drag_page_dropped': "Sida {0} infogad på position {1}",
        'drag_position_invalid': "Ogiltig position",
        'drag_same_position': "Sida {0} förblir på position {0}",
        'drag_error': "Fel vid flytt",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Textinmatning med avancerad formatering och textblockhantering",
        'text_templates': "Tillgängliga textblock:",
        'text_name': "Namn",
        'text_preview': "Textförhandsgranskning",
        'text_enter': "Text:",
        'text_font_size': "Teckenstorlek:",
        'text_formatting': "Formatering:",
        'text_bold': "Fet",
        'text_italic': "Kursiv",
        'text_underline': "Understruken",
        'text_alignment': "Justering:",
        'text_left': "Vänster",
        'text_center': "Centrerad",
        'text_right': "Höger",
        'text_color': "Textfärg:",
        'text_opacity': "Opacitet:",
        'text_word_wrap': "Radbrytning:",
        'text_auto': "Automatisk",
        'text_page_width_95': "Sidbredd (95%)",
        'text_page_width_85': "Mycket bred (85%)",
        'text_page_width_75': "Bredare (75%)",
        'text_page_width_60': "Bred (60%)",
        'text_page_width_50': "Medium (50%)",
        'text_page_width_30': "Smal (30%)",
        'text_page_width_20': "Smallare (20%)",
        'text_page_width_10': "Mycket smal (10%)",
        'text_no_wrap': "Ingen radbrytning",
        'text_private': "Privat textblock (kräver autentisering)",
        'text_preview_label': "Förhandsgranskning:",
        'text_preview_placeholder': "Här visas en förhandsgranskning av texten...",
        'text_no_text': "(Ingen text)",
        'text_save_template': "💾 Spara som block",
        'text_delete_template': "🗑 Ta bort valt textblock",
        'text_show_private': "Visa privata",
        'text_hide_private': "Dölj privata",
        'text_use': "✅ Använd text",
        'text_saved': "Textblock sparat som:\n{0}",
        'text_saved_voice': "Textblock sparat",
        'text_deleted': "Textblock borttaget",
        'text_no_text_to_save': "Ingen text att spara.",
        'text_no_templates': "Inga textblock hittades",
        'text_private_master_required': "Privata block kan bara användas om ett huvudlösenord har skapats.\n\nVill du skapa ett huvudlösenord nu?",
        'text_filename': "Filnamn för textblock (utan 'Text_' och '.txt'):",
        'text_filename_hint': "Exempel: 'Telefon Hem' sparas som 'Text_Telefon Hem.txt'",
        'text_save_hint': "Textblocket sparas automatiskt med formatering.",
        'text_guide_title': "Textinmatning - Guide",
        'text_delete_confirm': "Vill du verkligen ta bort textblocket?\n\nFil: {0}\nText: {1}...",
        'text_make_public': "Markera som offentlig",
        'text_make_private': "Markera som privat",
        'text_privacy_changed': "Sekretessstatus ändrad",
        'text_private_always': "Privata alltid synliga (inställning)",
        'text_mode_required': "Aktivera först textläge",
        'text_continue_editing': "Fortsätt redigera – markör i slutet av texten",
        'text_no_input': "Ingen text angiven – text kasserad",
        'save_dialog_question': "Hur vill du fortsätta?",
        'text_save_question': "Spara alla texter och kryss, justera, fortsätt redigera eller kassera?",
        'copy_cross': "Kryss kopierat",
        'paste_cross': "Kryss inklistrat",
        'paste_text': "Text inklistrad",
        'cross_discarded': "Kryss kasserat",
        'all_discarded': "Allt kasserat",
        'text_discarded': "Text kasserad",
        'no_texts_to_save': "Inga texter att spara",
        'no_valid_texts': "Inga giltiga texter att spara",
        'text_word_singular': "text",
        'text_word_plural': "texter",
        'cross_word_singular': "kryss",
        'cross_word_plural': "kryss",
        'texts_saved_title': "Texter sparade",
        'texts_crosses_saved': "{0} {1} och {2} {3} infogades i PDF:en.\n\nPDF omläst...",
        'texts_crosses_saved_voice': "{0} {1} och {2} {3} sparade.",
        'texts_saved': "{0} {1} infogades i PDF:en.\n\nPDF omläst...",
        'texts_saved_voice': "{0} {1} sparade.",
        'crosses_saved': "{0} {1} infogades i PDF:en.\n\nPDF omläst...",
        'crosses_saved_voice': "{0} {1} sparade.",
        'elements_saved': "{0} element infogades i PDF:en.\n\nPDF omläst...",
        'elements_saved_voice': "{0} element sparade.",
        'text_window_load_error': "Textfönster kunde inte laddas",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Textinmatning och textblock – Detaljerad guide**

        **1. Infoga och redigera text**
        - Högerklicka på önskad plats i dokumentet och välj "Infoga text".
        - En dialogruta öppnas där du kan ange och formatera din text:
        • Teckenstorlek, Fet, Kursiv, Understruken
        • Textfärg (fritt val)
        • Genomskinlighet via reglage
        • Radbrytning (olika bredder, t.ex. sidbredd, smal, ingen brytning)
        - Efter bekräftelse visas texten på klickpositionen. Du kan flytta den med musen eller piltangenterna.
        - Dubbelklicka på texten öppnar redigeringsläget; ESC lämnar det.

        **2. Hantera textblock (mallar)**
        - I textdialogrutan ser du till vänster en lista över alla sparade textblock.
        - **Spara ett block:** Ange din text, formatera den och klicka på "💾 Spara som block". Ange ett filnamn (utan ändelse).
        - **Ladda ett block:** Klicka på önskat namn i listan. Texten och formateringen övertas och kan justeras vid behov.
        - **Ta bort:** Högerklicka på ett block för att ta bort det eller ändra dess sekretessstatus.

        **3. Privata textblock (huvudlösenord)**
        - Om du har skapat ett huvudlösenord (under Inställningar → Lösenordshantering) kan du markera block som "privata".
        - Aktivera kryssrutan "Privat textblock" i dialogrutan innan du sparar.
        - Privata block visas bara i listan när du en gång per session har angett ditt huvudlösenord (autentisering via hänglåssymbolen eller vid första åtkomst).
        - På så sätt skyddar du konfidentiella textblock från obehörig åtkomst.

        **4. Infoga kryss**
        - Via snabbmenyn kan du också infoga ett grafiskt kryss (t.ex. för kryssrutor).
        - Storleken, linjetjockleken och färgen på kryss kan justeras globalt i inställningarna (meny "Inställningar" → "Kryssinställningar").
        - Högerklicka på ett befintligt kryss för att ändra det individuellt.

        **5. Samlingsåtgärder**
        - Om du har placerat flera texter eller kryss på en sida kan du spara eller kassera alla element samtidigt via snabbmenyn (högerklick i textläge).
        - Vid sparande bäddas alla element in i PDF:en och förblir som vektorgrafik.

        **6. Tangentbordsgenvägar i textläge**
        - Piltangenter: flytta element
        - Ctrl+Piltangenter: större steg
        - Retur: öppna spara-dialog (spara allt / justera / kassera)
        - ESC: kassera aktuellt element
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Textinmatning och textblock – Detaljerad guide</strong></p>

        <p><strong>1. Infoga och redigera text</strong></p>
        <ul>
        <li>Högerklicka på önskad plats i dokumentet och välj "Infoga text".</li>
        <li>En dialogruta öppnas där du kan ange och formatera din text:<br/>
        • Teckenstorlek, Fet, Kursiv, Understruken<br/>
        • Textfärg (fritt val)<br/>
        • Genomskinlighet via reglage<br/>
        • Radbrytning (olika bredder, t.ex. sidbredd, smal, ingen brytning)</li>
        <li>Efter bekräftelse visas texten på klickpositionen. Du kan flytta den med musen eller piltangenterna.</li>
        <li>Dubbelklicka på texten öppnar redigeringsläget; ESC lämnar det.</li>
        </ul>

        <p><strong>2. Hantera textblock (mallar)</strong></p>
        <ul>
        <li>I textdialogrutan ser du till vänster en lista över alla sparade textblock.</li>
        <li><strong>Spara ett block:</strong> Ange din text, formatera den och klicka på "💾 Spara som block". Ange ett filnamn (utan ändelse).</li>
        <li><strong>Ladda ett block:</strong> Klicka på önskat namn i listan. Texten och formateringen övertas och kan justeras vid behov.</li>
        <li><strong>Ta bort:</strong> Högerklicka på ett block för att ta bort det eller ändra dess sekretessstatus.</li>
        </ul>

        <p><strong>3. Privata textblock (huvudlösenord)</strong></p>
        <ul>
        <li>Om du har skapat ett huvudlösenord (under Inställningar → Lösenordshantering) kan du markera block som "privata".</li>
        <li>Aktivera kryssrutan "Privat textblock" i dialogrutan innan du sparar.</li>
        <li>Privata block visas bara i listan när du en gång per session har angett ditt huvudlösenord (autentisering via hänglåssymbolen eller vid första åtkomst).</li>
        <li>På så sätt skyddar du konfidentiella textblock från obehörig åtkomst.</li>
        </ul>

        <p><strong>4. Infoga kryss</strong></p>
        <ul>
        <li>Via snabbmenyn kan du också infoga ett grafiskt kryss (t.ex. för kryssrutor).</li>
        <li>Storleken, linjetjockleken och färgen på kryss kan justeras globalt i inställningarna (meny "Inställningar" → "Kryssinställningar").</li>
        <li>Högerklicka på ett befintligt kryss för att ändra det individuellt.</li>
        </ul>

        <p><strong>5. Samlingsåtgärder</strong></p>
        <ul>
        <li>Om du har placerat flera texter eller kryss på en sida kan du spara eller kassera alla element samtidigt via snabbmenyn (högerklick i textläge).</li>
        <li>Vid sparande bäddas alla element in i PDF:en och förblir som vektorgrafik.</li>
        </ul>

        <p><strong>6. Tangentbordsgenvägar i textläge</strong></p>
        <ul>
        <li>Piltangenter: flytta element</li>
        <li>Ctrl+Piltangenter: större steg</li>
        <li>Retur: öppna spara-dialog (spara allt / justera / kassera)</li>
        <li>ESC: kassera aktuellt element</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Kryssinställningar",
        'cross_properties': "Krysegenskaper",
        'cross_size': "Storlek (px):",
        'cross_line_width': "Linjetjocklek:",
        'cross_color': "Färg:",
        'cross_choose_color': "Välj",
        'cross_fine_tuning': "Finjustering vid sparande (pixlar)",
        'cross_offset_x': "X‑förskjutning:",
        'cross_offset_y': "Y‑förskjutning:",
        'cross_offset_x_tooltip': "Negativa värden flyttar krysset åt vänster vid sparande, positiva åt höger",
        'cross_offset_y_tooltip': "Negativa värden flyttar krysset uppåt vid sparande, positiva nedåt",
        'cross_preview': "Förhandsgranskning",
        'cross_save': "Använd inställningar",
        'cross_customized': "Kryss anpassat",
        'cross_settings_applied': "Kryssinställningar sparade.\nStorlek: {0}px, Linjetjocklek: {1}px\n{2}",
        'cross_updated_count': "{0} befintliga kryss uppdaterades.",
        'cross_no_crosses': "Inga befintliga kryss hittades.",
        'cross_settings_applied_all': "Kryssinställningar tillämpade på alla {0} kryss",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Signaturinställningar",
        'signature_1': "Signatur 1",
        'signature_2': "Signatur 2",
        'signature_select': "Välj signatur",
        'signature_add': "➕ Lägg till ny signatur...",
        'signature_size': "Storlek för signatur {0} (%):",
        'signature_common': "Allmänna inställningar",
        'signature_timestamp': "Lägg automatiskt till tidsstämpel",
        'signature_location': "Standardplats:",
        'signature_timestamp_size': "Teckenstorlek för tidsstämpel:",
        'signature_no_files': "-- Inga signaturer hittades --",
        'signature_insert': "Infoga signatur",
        'signature_insert_1': "Infoga signatur 1",
        'signature_insert_2': "Infoga signatur 2",
        'signature_customize': " Anpassa signatur",
        'signature_discard': " Kassera denna signatur",
        'signature_save_all': " Spara alla signaturer",
        'signature_discard_all': " Kassera alla signaturer",
        'signature_guide_title': "Signaturer - Guide",
        'signature_guide': """
📝 Signaturer - Snabbguide

- Skapa huvudlösenord
- Konfigurera signaturer i menyn Inställningar
  (storlek, tidsstämpel ...)
- Infoga med HÖGERKLICK på önskad plats
  (huvudlösenord krävs en gång per session)
- Flytta signaturen med musen eller piltangenterna
- Flera signaturer kan infogas efter varandra
- Varje signatur kan anpassas individuellt
- Kassera en enskild signatur
- Spara / kassera alla signaturer på en gång
- Alternativt kan menyraden användas.
        """,
        'signature_placeholder': "Ingen förhandsgranskning tillgänglig",
        'signature_info': "Signatur {0}: {1}×{2} px ({3}% av {4}×{5})",
        'signature_info_placeholder': "Inställningar för signatur {0}",
        'signature_inserted': "Signatur {0} infogad på sida {1}",
        'signature_deleted': "Signatur borttagen",
        'signature_copied': "Signatur kopierad",
        'signature_pasted': "Signatur {0} inklistrad",
        'signature_saved': "{0} signaturer infogades i PDF:en.\n\nPDF omläst...",
        'signature_saved_voice': "{0} signaturer sparade",
        'mode_replace_signature_format': "Avsluta läge och infoga signatur {0}",
        'mode_conflict_voice_signature': "{0}‑läge är aktivt. Avsluta och infoga signatur?",
        'signature_not_configured': "Signatur {0} inte konfigurerad",
        'signature_file_not_found': "Signaturfil hittades inte",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Ingen kopierad signatur tillgänglig",
        'no_signatures_to_save': "Inga signaturer att spara",
        'signature_save_question': "Spara alla signaturer, justera eller kassera denna?",
        'signatures_saved_title': "Signaturer sparade",
        'signatures_saved': "{0} signaturer infogades i PDF:en.\n\nPDF omläst...",
        'signatures_saved_voice': "{0} signaturer sparade.",
        'all_signatures_discarded': "Alla signaturer kasserade",
        'signature_settings_saved': "Signaturinställningar sparade",
        'signature_cancelled': "Signatur kasserad",
        'signature_active_title': "Signatur aktiv",
        'signature_replace_question': "En signatur är redan aktiv.\n\nVill du ersätta den aktuella signaturen?",
        'signature_replace': "Ersätt signatur",
        'signature_replace_voice': "Ersätt aktuell signatur eller avbryt?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Bildinställningar",
        'image_common': "Allmänna bildinställningar",
        'image_keep_aspect': "Bevara proportioner vid dragning",
        'image_default_size': "Standardstorlek (%):",
        'image_dark_invert': "Invertera bilder i mörkt läge",
        'image_dark_invert_tooltip': "Aktiverat: bilder inverteras för bättre synlighet",
        'image_fine_tuning': "Finjustering (pixlar)",
        'image_offset_x': "X‑förskjutning:",
        'image_offset_y': "Y‑förskjutning:",
        'image_offset_x_tooltip': "Negativa värden flyttar bilden åt vänster vid sparande, positiva åt höger",
        'image_offset_y_tooltip': "Negativa värden flyttar bilden uppåt vid sparande, positiva nedåt",
        'image_select': "Välj bild",
        'image_insert': "Infoga bild",
        'image_customize': " Anpassa bild",
        'image_aspect': " Bevara proportioner",
        'image_discard': " Kassera denna bild",
        'image_save_all': " Spara alla bilder",
        'image_discard_all': " Kassera alla bilder",
        'image_filter': "Bilder",
        'image_guide_title': "Infoga bild - Guide",
        'image_guide': """
📷 Infoga bild i PDF - Snabbguide:

1. Högerklicka på önskad plats
2. "Infoga bild" → välj bild
3. Placera bilden: dra med musen
4. Justera storleken: dra i hörn/kanter
5. Bevara proportioner: [A]‑tangent
6. Ytterligare justeringar: högerklicka på bilden

Tips: Du kan justera inställningarna i snabbmenyn.
        """,
        'image_inserted': "Bild {0} infogad på sida {1}",
        'image_deleted': "Bild kasserad",
        'image_copied': "Bild kopierad",
        'image_pasted': "Bild inklistrad",
        'image_saved': "{0} bilder infogades i PDF:en.\n\nPDF omläst...",
        'image_saved_voice': "{0} bilder sparade",
        'image_aspect_on': "aktiverad",
        'image_aspect_off': "inaktiverad",
        'image_aspect_toggle': "Bevara proportioner {0}",
        'image_reset': "Bild återställd till originalstorlek",
        'image_replaced': "Bild ersatt",
        'image_invalid': "Inte en giltig bild",
        'mode_replace_image': "Infoga bild",
        'mode_conflict_voice_image': "{0}‑läge är aktivt. Avsluta och infoga bild?",
        'image_active_title': "Bild aktiv",
        'image_replace_question': "En bild är redan aktiv.\n\nVill du ersätta den aktuella bilden?",
        'image_replace': "Ersätt bild",
        'image_replace_voice': "Ersätt aktuell bild eller avbryt?",
        'image_filter_all': "Bilder (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Alla filer (*.*)",
        'no_copied_image': "Ingen kopierad bild tillgänglig",
        'image_discarded': "Bild kasserad",
        'image_save_question': "Spara alla bilder, justera eller kassera denna?",
        'no_images_to_save': "Inga bilder att spara",
        'no_valid_images': "Inga giltiga bilder att spara",
        'images_saved_title': "Bilder sparade",
        'images_saved': "{0} bilder infogades i PDF:en.\n\nPDF omläst...",
        'images_saved_voice': "{0} bilder sparade.",
        'all_images_discarded': "Alla bilder kasserade",
        'image_settings_updated': "Bildinställningar uppdaterade",
        'image_replace_title': "Välj ny bild",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Forminställningar",
        'form_basic': "Grundinställningar",
        'form_default_type': "Standardformtyp:",
        'form_rectangle': "Rektangel",
        'form_ellipse': "Ellips",
        'form_line': "Linje",
        'form_arrow': "Pil",
        'form_line_width': "Linjetjocklek:",
        'form_colors': "Färger",
        'form_line_color': "Linjefärg:",
        'form_fill_color': "Fyllningsfärg:",
        'form_choose_color': "Välj",
        'form_transparent': "Transparent bakgrund (endast linje)",
        'form_filled': "fylld",
        'form_dark_mode': "Mörkt läge",
        'form_dark_invert': "Invertera färger i mörkt läge",
        'form_fine_tuning': "Finjustering (pixlar)",
        'form_offset_x': "X‑förskjutning:",
        'form_offset_y': "Y‑förskjutning:",
        'form_offset_x_tooltip': "Negativa värden flyttar formen åt vänster vid sparande, positiva åt höger",
        'form_offset_y_tooltip': "Negativa värden flyttar formen uppåt vid sparande, positiva nedåt",
        'form_preview': "Förhandsgranskning",
        'form_insert': "Infoga form",
        'form_rectangle_insert': "Rektangel",
        'form_ellipse_insert': "Ellips/Cirkel",
        'form_line_insert': "Linje (2 klick)",
        'form_arrow_insert': "Pil (2 klick)",
        'form_customize': " Anpassa form",
        'form_transparent_toggle': " Transparent bakgrund",
        'form_discard': " Kassera denna form",
        'form_save_all': " Spara alla former",
        'form_discard_all': " Kassera alla former",
        'form_guide_title': "Infoga form - Guide",
        'form_guide': """
📐 Infoga form i PDF - Snabbguide:

1. Välj formtyp (rektangel, ellips, linje, pil)
2. Klicka på positionen
   - För rektangel/ellips: ett klick placerar formen
   - För linje/pil: två klick för start‑ och slutpunkt
3. Placera formen: dra med musen
4. Justera storleken: dra i hörn/kanter
5. Spara formen: Retur
6. Kassera formen: ESC
7. Ytterligare justeringar: högerklicka på formen

Tips: Du kan justera inställningarna i snabbmenyn.
        """,
        'form_inserted': "{0} infogad på sida {1}",
        'form_deleted': "Form borttagen",
        'form_copied': "Form kopierad",
        'form_pasted': "Form inklistrad",
        'form_saved': "{0} former infogades i PDF:en.\n\nPDF omläst...",
        'form_saved_voice': "{0} former sparade",
        'form_reset': "Form återställd till standardstorlek",
        'form_transparent_on': "aktiverad",
        'form_transparent_off': "inaktiverad",
        'form_transparent_toggled': "Transparent bakgrund {0}",
        'form_line_cancel': "Linjeritning avbruten",
        'form_second_click': "Klicka nu på slutpunkten för {0}",
        'mode_replace_form': "Infoga form",
        'mode_conflict_voice_form': "{0}‑läge är aktivt. Avsluta och infoga en form?",
        'form_settings_updated': "Forminställningar uppdaterade",
        'form_unknown': "Form",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klicka på startpositionen",
        'form_line_guide_2': "2. Klicka på slutpositionen",
        'form_line_guide_3': "Linjen kommer att ritas mellan de två punkterna.",
        'form_line_status_1': "Väntar på första klick...",
        'form_line_status_2': "Första punkten angiven: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Klicka nu på slutpunkten...",
        'form_line_status_4': "Båda punkterna angivna.\nKlicka på 'Klar' för att spara.",
        'form_line_reset': "Återställ",
        'form_line_finish': "Klar",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopiera (Cmd+C)",
        'paste': "Klistra in (Cmd+V)",
        'copied': "Kopierat: {0}",
        'no_element_to_copy': "Inget element valt att kopiera",
        'no_copied_data': "Inga kopierade data tillgängliga",
        'no_valid_position': "Ingen giltig position att klistra in på",
        'copy_text': "Text kopierad",
        'copy_image': "Bild kopierad",
        'copy_form': "Form kopierad",
        'copy_signature': "Signatur kopierad",
        'element_text': "text",
        'element_image': "bild",
        'element_form': "form",
        'element_signature': "signatur",
        'element_unknown': "element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Lägeskonflikt",
        'mode_conflict_message': "Läget '{0}' är redan aktivt.\n\nVill du avsluta det och {1}?",
        'mode_replace': "Avsluta läge och {0}",
        'mode_cancel': "Avbryt",
        'mode_replace_text': "infoga text",
        'mode_replace_cross': "infoga kryss",
        'mode_replace_signature': "infoga signatur",
        'mode_replace_image': "infoga bild",
        'mode_replace_form': "infoga form",
        'mode_conflict_voice': "{0}‑läge är aktivt. Avsluta och infoga text?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Textinmatning",
        'active_mode_signature': "Signatur",
        'active_mode_image': "Bild",
        'active_mode_form': "Form",
        'active_mode_and': " och ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Infoga",                    # Hauptmenü
        'insert_another_text': "Infoga text",          # Vereinfacht
        'insert_another_cross': "Infoga kryss",        # Vereinfacht
        'insert_another_signature_1': "Signatur 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Signatur 2",      # Untermenü-Eintrag
        'insert_another_image': "Infoga bild",         # Vereinfacht
        'insert_another_form_rect': "Rektangel",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellips",        # Untermenü-Eintrag
        'insert_another_form_line': "Linje (2 klick)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Pil (2 klick)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Spara {0}",
        'save_dialog_message': "{0} kommer att sparas på sida {1}.\n\nHur vill du fortsätta?",
        'save_all': "Spara alla {0}",
        'save_single': "Spara {0}",
        'save_customize': "Justera {0}",
        'save_discard': "Kassera {0}",
        'save_continue': "Fortsätt redigera",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Gå till sida {0}",
        'context_rotate': " Rotera sida {0}",
        'context_delete': " Ta bort sida {0}",
        'context_export': " Exportera sida {0}",
        'context_mark_as': " Markera sida som...",
        'context_mark_empty': " Tom sida",
        'context_unmark_empty': " Inte längre tom",
        'context_mark_export': " Markera för export",
        'context_unmark_export': " Exportera inte",
        'context_batch_actions': " Samlingsåtgärder",
        'context_batch_delete_empty': " Ta bort alla {0} tomma sidor",
        'context_batch_export_single': " Alla {0} sidor (en fil)",
        'context_batch_export_split': " Alla {0} sidor (separata)",
        'context_drag_start': " Starta dra och släpp",
        'context_drag_stop': " Stoppa dra och släpp",
        'context_insert': " Infoga",
        'context_insert_pages': " Infoga sidor",
        'context_zoom': "Zoom",
        'discard_mixed': "Kassera {0} {1} och {2} {3}",
        'save_mixed': "Spara {0} {1} och {2} {3}",
        'discard_texts': "Kassera {0} texter",
        'discard_text_single': "Kassera 1 text",
        'save_texts': "Spara {0} texter",
        'save_text_single': "Spara 1 text",
        'discard_crosses': "Kassera {0} kryss",
        'discard_cross_single': "Kassera 1 kryss",
        'save_crosses': "Spara {0} kryss",
        'save_cross_single': "Spara 1 kryss",
        'discard_signatures': "Kassera {0} signaturer",
        'save_signature_single': "Spara 1 signatur",
        'save_signatures': "Spara {0} signaturer",
        'discard_images': "Kassera {0} bilder",
        'save_image_single': "Spara 1 bild",
        'save_images': "Spara {0} bilder",
        'discard_forms': "Kassera {0} former",
        'save_form_single': "Spara 1 form",
        'save_forms': "Spara {0} former",
        'cross_discard': "Kassera detta kryss",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Export‑ / importinformation",
        'export_what': "📋 Vad exporteras?",
        'export_general': "Allmänna inställningar",
        'export_general_items': "• Talutmatning (på/av, hastighet)\n• Mörkt/ljust läge\n• Säkerhetskopieringsinställningar\n• OCR‑inställningar",
        'export_image_form': "Bild‑ och forminställningar",
        'export_image_form_items': "• Bildinställningar (proportioner, standardstorlek)\n• Forminställningar (linjetjocklek, färger)\n• Signaturinställningar (sökvägar, storlekar, tidsstämpel)",
        'export_passwords': "Lösenordsdatabas",
        'export_passwords_items': "• Alla sparade PDF‑lösenord\n• Valfritt krypterade eller dekrypterade",
        'export_master': "Huvudlösenordsinställningar",
        'export_master_items': "• Hash för huvudlösenord\n• Inställningar för signaturer/textblock",
        'export_signatures': "Signaturer och textblock",
        'export_signatures_items': "• Alla bildfiler (signaturer)\n• Alla textblock med formatering\n• Privata/offentliga markeringar",
        'export_import_warning': "⚠️ Viktiga anmärkningar",
        'export_import_note': "• Vid import skrivs ALLA nuvarande inställningar över\n• En omstart av applikationen krävs\n• Befintliga signaturer/textblock ersätts",
        'export_master_note': "• Om ett huvudlösenord har angetts kan du välja:\n  - Dekrypterat (lösenord i klartext)\n  - Krypterat (endast läsbart med huvudlösenord)",
        'export_security': "• Den exporterade ZIP‑filen innehåller konfidentiella data\n• Förvara den säkert (t.ex. krypterat USB‑minne)\n• Om filen förloras är lösenorden oåterkalleligt förlorade",
        'export_format': "📁 Exportformat",
        'export_format_desc': "Inställningarna sparas i en enda ZIP‑fil:",
        'export_filename': "PDFDarkView_Inställningar_ÅÅÅÅMMDD_TTMMSS.zip",
        'export_success': "Inställningar exporterade",
        'export_failed': "Export misslyckades",
        'export_import_question': "Vill du starta om applikationen nu?",
        'export_password_question': "Ett huvudlösenord har angetts.\n\nVill du exportera lösenorden dekrypterade?\n(annars exporteras de krypterade)",
        'export_decrypt': "Exportera dekrypterat",
        'export_encrypt': "Exportera krypterat",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Om PDF Dark View",
        'info_version': "Version",
        'info_author': "Utvecklad av Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Om",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> är en tillgänglig PDF-visare som har utvecklats speciellt för personer med synnedsättning.</p>

            <p><strong>Kärnfunktioner:</strong></p>
            <ul>
                <li>Kontrastrik, anpassningsbar gränssnitt</li>
                <li>Fullständig tangentbordskontroll</li>
                <li>Integrerad talsyntes</li>
                <li>OCR för skannade dokument</li>
                <li>Omfattande redigeringsverktyg</li>
            </ul>

            <p>Mer än 50 språk stöds – så att PDF-filer är tillgängliga för alla.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funktioner",
        'info_features_intro': "PDF Dark View erbjuder dig följande möjligheter:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Visning och navigering</strong> – Mörkt/Ljust läge, bläddra sidor, zoom, hoppa till sida</li>
            <li><strong>OCR (textigenkänning)</strong> – Gör skannade dokument sökbara och kopierbara</li>
            <li><strong>Redigering</strong> – Infoga text, kryss, signaturer, bilder och former</li>
            <li><strong>Sidhantering</strong> – Ta bort, extrahera, infoga, flytta via dra och släpp</li>
            <li><strong>Export</strong> – Till Word, Pages eller som text</li>
            <li><strong>Säkerhet</strong> – Lösenordsskydd och -hantering</li>
            <li><strong>Tillgänglighet</strong> – Talsyntes, tangentbordskontroll, hög kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Användning",
        'info_accessibility': "♿ Tillgänglighet – fullständig tangentbordskontroll",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Allmänt</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Öppna PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Sök</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Växla mörkt/ljust läge</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Skriv ut</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Avsluta</div>

        <div class="shortcut-cat">📖 Navigering</div>
        <div class="shortcut-row"><kbd>Piltangenterna</kbd> Bläddra sida för sida</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Gå till sida</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Första sidan</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Sista sidan</div>

        <div class="shortcut-cat">✏️ Redigering</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Infoga text</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Ta bort sidor</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extrahera sidor</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Infoga sidor</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Flytta sidor</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rotera sida</div>

        <div class="shortcut-cat">🖼️ Flytta element</div>
        <div class="shortcut-row"><kbd>Piltangenterna</kbd> Flytta text/bild/signatur</div>
        <div class="shortcut-row"><kbd>Ctrl+Piltangenterna</kbd> Större steg</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Spara</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Förkasta</div>

        <div class="shortcut-cat">🗣️ Talsyntes</div>
        <div class="shortcut-row"><kbd>F2</kbd> Slå på/av talsyntes</div>
        """,
        'info_contextmenu': "📌 Viktigt: Alla funktioner är också tillgängliga via snabbmenyn (höger musknapp)!",
        'info_accessibility_hint': "💡 Tips: Talsyntesen (F2) underlättar orienteringen och ger återkoppling om menyer och dialoger.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licens & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Information enligt § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Tyskland<br>
        E-post: binhdiez64@gmail.com<br>
        Ansvarig för innehållet: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Friskrivning</strong><br>
        Programvaran har utvecklats med största omsorg. Ingen garanti lämnas för korrekthet, fullständighet och funktionalitet. Användning sker på egen risk.<br><br>

        <strong>📄 MIT-licens (privat användning)</strong><br>
        Upphovsrätt (c) 2026 Toralf Schulz (BinhDiez)<br>
        Tillåtet: gratis användning, privata ändringar, personliga kopior.<br>
        Inte tillåtet: försäljning, kommersiell användning, borttagning av upphovsrättsmeddelanden.<br><br>

        <strong>🔧 Tredjepartskomponenter</strong><br>
        Denna programvara innehåller komponenter under GPL, AGPL, Apache 2.0, BSD och MIT-licenser.<br>
        Vid vidaredistribution måste respektive licensvillkor följas.<br><br>

        <strong>🌐 Öppen källkod</strong><br>
        Källkoden är tillgänglig och kan ses, ändras och vidaredistribueras i enlighet med respektive licensvillkor.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Tack till",
        'info_credits': "Tack till open source-gemenskapen",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-bearbetning</li>
            <li><strong>PyQt5</strong> – Grafiskt gränssnitt</li>
            <li><strong>Tesseract OCR</strong> – Textigenkänning</li>
            <li><strong>OCRmyPDF</strong> – OCR-integration</li>
            <li><strong>python-docx</strong> – Word-export</li>
            <li><strong>qtawesome</strong> – Ikoner</li>
            <li><strong>DeepSeek</strong> – Stöd för översättningar (50+ språk)</li>
            <li><strong>Alla användare</strong> – För värdefull feedback</li>
            <li><strong>Open source-gemenskapen</strong> – För fantastiska bibliotek</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Språk",
        'info_languages_header': "🌍 Språkstöd",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View stöder för närvarande <strong>62 språk</strong> – så att programvaran kan användas tillgängligt över hela världen.</p>

            <p><strong>📖 Fullständig språklista (Status: mars 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanska (Shqip)</li>
                    <li>🇩🇿 Arabiska (العربية)</li>
                    <li>🇮🇩 Balinesiska (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Burmesiska (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosniska (Bosanski)</li>
                    <li>🇧🇬 Bulgariska (Български)</li>
                    <li>🇨🇳 Kinesiska (中文)</li>
                    <li>🇩🇰 Danska (Dansk)</li>
                    <li>🇩🇪 Tyska (Deutsch)</li>
                    <li>🇬🇧 Engelska (English)</li>
                    <li>🇪🇪 Estniska (Eesti)</li>
                    <li>🇫🇮 Finska (Suomi)</li>
                    <li>🇫🇷 Franska (Français)</li>
                    <li>🇬🇷 Grekiska (Ελληνικά)</li>
                    <li>🇮🇱 Hebreiska (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatiska (Hrvatski)</li>
                    <li>🇭🇺 Ungerska (Magyar)</li>
                    <li>🇮🇩 Indonesiska (Bahasa Indonesia)</li>
                    <li>🇮🇪 Iriska (Gaeilge)</li>
                    <li>🇮🇸 Isländska (Íslenska)</li>
                    <li>🇮🇹 Italienska (Italiano)</li>
                    <li>🇯🇵 Japanska (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreanska (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Lettiska (Latviešu)</li>
                    <li>🇱🇹 Litauiska (Lietuvių)</li>
                    <li>🇱🇺 Luxemburgiska (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajiska (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongoliska (Монгол)</li>
                    <li>🇳🇵 Nepalesiska (नेपाली)</li>
                    <li>🇳🇱 Nederländska (Nederlands)</li>
                    <li>🇳🇴 Norska (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persiska (فارسی)</li>
                    <li>🇵🇱 Polska (Polski)</li>
                    <li>🇵🇹 Portugisiska (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumänska (Română)</li>
                    <li>🇷🇺 Ryska (Русский)</li>
                    <li>🇸🇪 Svenska (Svenska)</li>
                    <li>🇷🇸 Serbiska (Српски)</li>
                    <li>🇸🇰 Slovakiska (Slovenčina)</li>
                    <li>🇸🇮 Slovenska (Slovenščina)</li>
                    <li>🇪🇸 Spanska (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thailändska (ไทย)</li>
                    <li>🇨🇿 Tjeckiska (Čeština)</li>
                    <li>🇹🇷 Turkiska (Türkçe)</li>
                    <li>🇺🇦 Ukrainska (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamesiska (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddisch (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Lägg till egna språk:</strong><br>
                Vill du ha ett språk som inte ingår än? Placera bara din egen ordboksfil (<code>sprache_xx.py</code>) bredvid applikationen – programvaran känner igen den automatiskt. Om du är intresserad av en specifik översättning, kontakta mig gärna.
            </div>

            <p><strong>🙏 Särskilt tack:</strong> DeepSeek för stödet med att översätta alla ordböcker till 62 språk.</p>

            <p>📧 Kontakt för översättningar: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Fel",
        'error_occurred': "Ett fel uppstod",
        'error_pdf_load': "Fel vid inläsning av PDF",
        'error_pdf_save': "Fel vid sparande av PDF",
        'error_ocr': "Fel vid textigenkänning",
        'error_no_pdf': "Ingen PDF inläst",
        'error_page_not_found': "Sidan hittades inte",
        'error_invalid_range': "Ogiltigt sidintervall",
        'error_file_not_found': "Filen hittades inte",
        'error_permission': "Ingen behörighet",
        'error_unknown': "Okänt fel",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Lyckades",
        'success_operation': "Åtgärden lyckades",
        'success_saved': "Sparat",
        'success_exported': "Exporterat",
        'success_imported': "Importerat",
        'success_deleted': "Borttaget",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Bekräftelse",
        'confirm_yes': "Ja",
        'confirm_no': "Nej",
        'confirm_ok': "OK",
        'confirm_cancel': "Avbryt",
        'confirm_delete': "Ta bort",
        'confirm_overwrite': "Skriv över",
        'confirm_continue': "Fortsätt",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Läser in PDF...",
        'progress_saving': "Sparar PDF...",
        'progress_exporting': "Exporterar PDF...",
        'progress_processing': "Bearbetar...",
        'progress_wait': "Vänligen vänta...",
        'progress_preparing': "Förbereder...",
        'progress_finalizing': "Slutför...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Vit",
        'color_black': "Svart",
        'color_red': "Röd",
        'color_green': "Grön",
        'color_blue': "Blå",
        'color_yellow': "Gul",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Orange",
        'color_gray': "Grå",
        'color_custom': "Färgväljare",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Arkiv",
        'menu_edit': "&Redigera",
        'menu_view': "&Visa",
        'menu_tools': "&Verktyg",
        'menu_settings': "&Inställningar",
        'menu_help': "&Hjälp",
        'menu_language': "🌐 Språk",
        'menu_guides': "&Guider",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Öppna",
        'file_save_as': "&Spara som...",
        'file_protect': "&Skydda dokument...",
        'file_export': "&Exportera",
        'file_export_pages': "Exportera som Pages",
        'file_export_word': "Exportera som DOCX",
        'file_export_text': "Exportera som TXT",
        'file_print_now': "&Skriv ut nu",
        'file_print': "&Skriv ut",
        'file_close': "&Stäng",
        'file_quit': "&Avsluta",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Sök",
        'edit_ocr': " Kör OCR",
        'edit_rotate': "&Rotera sida",
        'edit_rotate_all': "&Rotera alla sidor",
        'edit_delete_pages': "&Ta bort sidor",
        'edit_extract_pages': "&Extrahera sidor",
        'edit_insert_pages': "&Infoga sidor",
        'edit_move_pages': "&Flytta sidor",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Infoga text och kryss",
        'text_insert': " Infoga text",
        'cross_insert': " Infoga kryss",
        'text_customize': " Anpassa text",
        'cross_customize': " Anpassa detta kryss",
        'cross_customize_all': " Anpassa alla kryss",
        'text_discard': " Kassera denna text/detta kryss",
        'text_discard_all': " Kassera alla texter och kryss",
        'text_save_all': " Spara alla texter och kryss",
        'text_guide': " Textinmatning / textblock - Guide",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Infoga signatur",
        'signature_settings_menu': " Inställningar...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Infoga bild",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Infoga former",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Visa textfönster",
        'view_zoom': "&Zooma",
        'view_zoom_page': "&Sidbredd (standard)",
        'view_zoom_two': "&Två sidor",
        'view_zoom_overview': "&Översikt (flera sidor)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Tillgänglighet",
        'settings_voice': "Talutmatning",
        'settings_voice_tooltip': "kompletterar skärmläsares talutmatning med extra information",
        'settings_signature': "&Signaturinställningar",
        'settings_password': "&Lösenordshantering",
        'settings_backup': "Skapa säkerhetskopia före ändringar",
        'settings_export_import': "&Exportera / importera inställningar",
        'settings_export': "&Exportera alla inställningar...",
        'settings_import': "&Importera alla inställningar...",
        'settings_export_info': "&Vad exporteras?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "på",
        'voice_off': "av",
        'voice_toggle': "Talutmatning {0}",
        'voice_speed': "Hastighet {0} procent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Verktyg hittades inte:\n{0}\n\nBASE_DIR: {1}\nSe till att PDF‑verktygen är installerade i katalogen {1}.",
        'tool_started': "{0} startat",
        'tool_start_failed': "Kunde inte starta",
        'process_error_failed_to_start': "Processen kunde inte startas. Finns filen?",
        'process_error_crashed': "Processen kraschade vid start.",
        'process_error_timeout': "Process timeout nåddes.",
        'process_error_write': "Skrivfel till processen.",
        'process_error_read': "Läsfel från processen.",
        'process_error_unknown': "Okänt processfel",
        'process_command': "Kommando",
        'process_normal_exit': "avslutades normalt",
        'process_crashed': "kraschade",
        'process_nonzero_exit': "{0} avslutades med felkod {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Avbryter...",
        'move_cancelling': "Flytt avbryts",
        'opening_pdf': "Öppnar PDF...",
        'loading_document': "Läser in dokument...",
        'pdf_opened': "PDF öppnad",
        'pages_found_moving': "{0} sidor hittades, {1} att flytta",
        'creating_backup': "Skapar säkerhetskopia...",
        'backup_description': "Säkerhetskopierar originalfil...",
        'backup_saved_as': "Säkerhetskopierad som: {0}",
        'error_format': "Fel: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Sökning återställd",
        'page_header_simple': "=== Sida {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Lösenordshantering – Guide",
        'password_guide_voice': "Guide till lösenordshantering. Läs anmärkningarna.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Lösenordshantering – Detaljerad guide</strong></p>

        <p><strong>1. Lösenordsskydd för PDF‑filer</strong></p>
        <ul>
        <li>När du öppnar en lösenordsskyddad PDF visas en dialogruta där du kan ange lösenordet.</li>
        <li>Du kan spara lösenordet krypterat så att du inte behöver ange det varje gång (kryssruta "Spara lösenord").</li>
        <li>Med knappen "Ta bort lösenord" kan du skapa en dekrypterad kopia av PDF‑filen och ta bort lösenordet från databasen.</li>
        </ul>

        <p><strong>2. Huvudlösenord</strong></p>
        <ul>
        <li>Huvudlösenordet skyddar åtkomsten till alla sparade PDF‑lösenord.</li>
        <li><strong>Skapa:</strong> Gå till "Inställningar → Lösenordshantering → Huvudlösenordsinställningar" och klicka på "Skapa huvudlösenord". Välj ett starkt huvudlösenord (minst 8 tecken).</li>
        <li><strong>Ändra:</strong> Efter lyckad autentisering kan du ändra huvudlösenordet.</li>
        <li><strong>Ta bort:</strong> Om du tar bort huvudlösenordet raderas ALLA sparade lösenord oåterkalleligt. Du kan exportera en säkerhetskopia först.</li>
        <li>En gång per session måste du autentisera dig med huvudlösenordet för att få tillgång till skyddade funktioner (t.ex. visa lösenord).</li>
        </ul>

        <p><strong>3. Lösenordshantering (lista)</strong></p>
        <ul>
        <li>Under "Inställningar → Lösenordshantering" öppnas en tabell över alla sparade PDF‑filer med deras krypterade lösenord.</li>
        <li><strong>Utan huvudlösenord:</strong> Du kan bara ta bort poster – lösenorden förblir dolda.</li>
        <li><strong>Med huvudlösenord (autentiserad):</strong> Du kan visa, kopiera, exportera och ta bort lösenord.</li>
        <li><strong>Export:</strong> Välj ett format (JSON, CSV, TXT) och spara listan. Om ett huvudlösenord har angetts kan du välja om lösenorden ska exporteras i klartext eller fortfarande krypterade.</li>
        <li><strong>Import:</strong> En tidigare exporterad ZIP‑fil med alla inställningar (inklusive lösenord) kan importeras via "Inställningar → Exportera/importera inställningar". OBS: Befintliga data skrivs över!</li>
        </ul>

        <p><strong>4. Lösenordsgenerator</strong></p>
        <ul>
        <li>I lösenordsdialogen (t.ex. när du skyddar en PDF) finns en tärningsknapp 🎲 till höger om inmatningsfältet.</li>
        <li>Klicka på den för att öppna lösenordsgeneratorn. Du kan ställa in längd, teckenuppsättningar (versaler, gemener, siffror, symboler) och en avgränsare för bättre läsbarhet.</li>
        <li>Det genererade lösenordet kan användas direkt och kopieras vid behov.</li>
        </ul>

        <p><strong>5. Viktiga säkerhetsanmärkningar</strong></p>
        <ul>
        <li>Sparade lösenord lagras krypterade med AES‑256. Nyckeln härleds från ditt huvudlösenord (om angett) eller från ett fast värde (utan huvudlösenord).</li>
        <li>Utan huvudlösenord är lösenorden visserligen krypterade, men nyckeln finns inbäddad i programmet – en angripare med tillgång till dina filer skulle kunna dekryptera dem. Därför rekommenderar vi starkt att använda ett huvudlösenord.</li>
        <li>Lösenordsdatabasen finns i katalogen `Data/passwords.json`. Gör regelbundna säkerhetskopior, särskilt innan du tar bort huvudlösenordet.</li>
        <li>Om huvudlösenordet förloras är alla sparade lösenord oåterkalleligt förlorade.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Inverteringsläge",
        'invert_mode_classic': "Klassiskt (invertera alla färger)",
        'invert_mode_smart': "Smart (invertera endast ljusstyrka)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Gråskaletröskel",
        'gray_threshold_10': "10% (sträng)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (mjuk)",
        'threshold_changed': "Tröskelvärde satt till {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Gråskaletröskel – Förklaring",
        'threshold_guide_text': "Gråskaletröskeln bestämmer vilka pixlar i smart mörkt läge som anses vara 'grå' och inverteras.\n\n"
                                "• Ett lågt värde (10%) inverterar bara nästan perfekta gråtoner – färgade element förblir helt bevarade.\n"
                                "• Ett högt värde (50%) inverterar också lätt färgade pixlar – detta ökar kontrasten, men kan förvränga färger.\n\n"
                                "Det optimala värdet beror på dokumentet. För rena textdokument är 30–40% ofta idealiskt, för färggrafik snarare 10–20%.\n\n"
                                "Du kan justera värdet när som helst via menyn 'Inställningar' – PDF-filen laddas om omedelbart.\n\n"
                                "Observera:\n* Foton och bilder kan endast visas korrekt i ljust läge!\n* Inverteringsinställningarna visas endast när mörkt läge är aktiverat.",
        'threshold_guide_voice': "Gråskaletröskeln bestämmer hur starkt smart mörkt läge griper in. Ett lågt värde skonar färger, ett högt värde ökar kontrasten.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Öppnar PDF...",
        'progress_loading_document': "Laddar dokument...",
        'progress_pdf_opened': "PDF öppnad",
        'progress_creating_backup': "Skapar säkerhetskopia...",
        'progress_backup_description': "Säkrar originalfil...",
        'progress_backup_created': "Säkerhetskopia skapad",
        'progress_backup_saved_as': "Sparad som: {0}",
        'progress_analyzing_start': "Startar analys...",
        'progress_searching_empty': "Söker efter tomma sidor...",
        'progress_page_empty': "Sida {0} är tom",
        'progress_page_keep': "Behåll sida {0}",
        'progress_analysis_complete': "Analys slutförd",
        'progress_empty_found': "Hittade {0} tomma sidor",
        'progress_current_page': "Aktuell sida",
        'progress_mark_delete': "Markeras för borttagning",
        'progress_range_selected': "Sidintervall {0}-{1}",
        'progress_deleting_pages': "Tar bort {0} sidor",
        'progress_creating_new_pdf': "Skapar ny PDF...",
        'progress_transferring_pages': "Överför sidor",
        'progress_keeping_page': "Sida {0} kommer att behållas ({1}/{2})",
        'progress_saving_pdf': "Sparar PDF...",
        'progress_optimizing': "Optimerar filstorlek...",
        'progress_finalizing': "Slutför...",
        'progress_new_size': "Ny storlek: {0:.2f} MB",
        'progress_cancelling': "Avbryter...",
        'progress_cancel_message': "{0} avbryts",
        'progress_pages_found_moving': "Hittade {0} sidor, {1} att flytta",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analyserar PDF...",
        'ocr_status_optimizing': "Bildoptimering pågår...",
        'ocr_status_recognizing': "Textigenkänning pågår...",
        'ocr_status_embedding': "Bäddar in text...",
        'ocr_status_finalizing': "Slutför PDF...",

        # PDF-Laden
        'progress_preparing': "Förbereder...",
        'progress_loading': "Laddar PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Tar bort sidor...",
        'progress_moving_title': "Flyttar sidor...",
        'pages_found': "Sidor hittades",
        'progress_creating_new_order': "Skapar ny ordning...",
        'progress_sorting_pages': "Sorterar sidor...",
        'progress_moving_to_begin': "Flytta {0} sidor till början",
        'progress_transferring_count': "Överför {0} sidor",
        'progress_transferring_before_target': "Överför sidor före målet",
        'progress_moving_pages': "Flytta {0} sidor",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_säkerhetskopia_",
        'filename_protected_suffix': "_skyddad_",
        'filename_copy_suffix': "_Kopia",
        'filename_page_single': "_Sida_",
        'filename_page_range': "_Sidor_",
        'filename_export_page': "_Sida_{0:03}",
        'filename_export_range': "_Sidor_{0}-{1}",
        'filename_export_multiple': "_Sidor_{0}",
        'filename_with_text': "_med_Text",
        'filename_with_signature': "_med_Signatur",
        'filename_with_image': "_med_Bild",
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
        'view_toggle_navbar': "Visa knapprad",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Alla sidor kan inte tas bort",
		'pages_cannot_delete_last_page': 'Den sista sidan kan inte tas bort!',
		'pages_cannot_delete_all_pages': 'Minst en sida måste finnas kvar i dokumentet!',
		'delete_pages_confirm': 'Är du säker på att du vill ta bort {0} sidor?',
		'delete_pages_confirm_voice': 'Är du säker på att du vill ta bort {0} sidor?',
		'pages_deleted': '{0} sidor har tagits bort.',
		'warning': 'Varning',
		'error': 'Fel',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Inget formulär valt",
        'form_customized': "Formulär anpassat",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Välj",
        'btn_use': "Använd",
        'master_password_for_spasswords': "För att spara och använda lösenord måste du först skapa ett huvudlösenord.\n\nVill du skapa huvudlösenordet nu?",
        'open_saved_dialog_title': "Öppna sparad fil",
        'open_saved_question': "Vill du öppna den sparade filen nu?",
        'password': "Lösenord",
        'password_manager_master_required': "Lösenordshanteraren är endast tillgänglig om ett huvudlösenord har skapats.\n\nVill du skapa huvudlösenordet nu?",
        'password_master_required_for_select': "För att visa och välja sparade lösenord måste du först autentisera dig med ditt huvudlösenord.\n\nVill du autentisera dig nu?",
        'password_not_available': "Det valda lösenordet är inte tillgängligt eller kunde inte dekrypteras.",
        'password_options_title': "Lösenordsalternativ",
        'password_save_choice_change': "Ange nytt lösenord",
        'password_save_choice_keep': "Använd befintligt lösenord",
        'password_save_choice_none': "Spara okrypterat",
        'password_save_hint': "Skapa först ett huvudlösenord för att säkert spara lösenord.",
        'password_save_master_required': "Spara lösenord (endast möjligt med huvudlösenord)",
        'password_save_question': "Den aktuella PDF-filen är lösenordsskyddad. Vill du använda det befintliga lösenordet, skapa ett nytt eller spara okrypterat?",
        'password_select': "Välj lösenord",
        'password_select_none': "Inget lösenord valt.\n\nVälj ett lösenord från listan.",
        'password_select_one': "Välj exakt ett lösenord.\n\nDu har markerat flera lösenord.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_säkerhetskopia",
        'filename_insert_suffix': "_med_infogning",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_sidor_raderade",
        'filename_pages_moved': "_sidor_flyttade",
        'filename_rotated_all_suffix': "_alla_sidor_roterade",
        'filename_rotated_suffix': "_sida_roterad",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfiguration av filnamn vid ändringar av PDF",
        'filename_keep_suffixes': "Behåll tidigare tillägg (t.ex. _med_text)",
        'filename_keep_suffixes_false': "Ersätt",
        'filename_keep_suffixes_true': "Behåll",
        'filename_preview_label': "Förhandsgranskning av filnamn:",
        'filename_preview_overwrite_hint': "Förhandsgranskning inte tillgänglig – originalfilen kommer att skrivas över.",
        'filename_separator': "Avskiljare mellan ord",
        'filename_separator_none': "Ingen avskiljare",
        'filename_separator_space': "Mellanslag ( )",
        'filename_separator_underscore': "Understreck (_)",
        'filename_settings_saved': "Filnamnsinställningar sparade",
        'filename_settings_title': "Filnamnsformatering och säkerhetskopia",
        'filename_timestamp_position': "Position för tidsstämpel",
        'filename_timestamp_position_after': "Efter grundnamnet",
        'filename_timestamp_position_before': "Helt framför",
        'filename_timestamp_position_end': "I slutet",
        'filename_use_timestamp': "Använd tidsstämpel",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Beteende vid ändringar:</b><ul><li>Radera och infoga sidor</li><li>Infoga text, signatur, bild och former</li><li>OCR</li></ul></html>",
        'backup_section': "Säkerhetskopia för sidoperationer (Radera, Flytta)",
        'behavior_info': "Observera: Vid 'Skriv över original' ignoreras tidsstämplar och suffix – filen behåller sitt namn.",
        'behavior_new_file': "Skapa alltid ny fil (med tidsstämpel och suffix)",
        'behavior_overwrite': "Skriv över original (ingen ny fil)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Alla sidor roterades.\n\nOriginalet förblev oförändrat.\nNy fil: {0}",
        'all_pages_rotated_voice': "Alla sidor roterade, ny fil skapad.",
        'empty_pages_deleted_new_file': "{0} tomma sidor raderades.\n\nOriginalet förblev oförändrat.\nNy fil: {1}",
        'empty_pages_deleted_voice': "{0} tomma sidor raderade, ny fil skapad.",
        'ocr_keep_original': "Behåll original (öppna manuellt senare)",
        'ocr_new_file_question': "Den nya sökbara PDF-filen sparades som:\n{0}\n\nVill du öppna den nu?",
        'ocr_open_new': "Öppna ny OCR-fil",
        'ocr_original_kept': "Originalfilen förblir öppen. OCR-filen har sparats.",
        'page_deleted_new_file': "Sida {0} raderades.\n\nOriginalet förblev oförändrat.\nNy fil: {1}",
        'page_deleted_voice': "Sida {0} raderades, ny fil skapad.",
        'page_rotated_new_file': "Sida {0} roterades.\n\nOriginalet förblev oförändrat.\nNy fil: {1}",
        'page_rotated_voice': "Sida {0} roterades, ny fil skapad.",
        'pages_deleted_new_file': "{0} sidor raderades.\n\nOriginalfilen förblev oförändrad.\nNy fil: {1}",
        'pages_deleted_new_file_voice': "{0} sidor raderade, ny fil skapad.",
        'pages_inserted_new_file': "{0} sidor infogades.\n\nOriginalfilen förblev oförändrad.\nNy fil: {1}",
        'pages_inserted_new_file_ask': "{0} sidor infogades.\n\nOriginalet förblev oförändrat.\nNy fil: {1}\n\nVill du öppna den nu?",
        'pages_inserted_voice_new': "{0} sidor infogade, ny fil skapad.",
        'pages_moved_new_file': "{0} sidor flyttades.\n\nOriginalfilen förblev oförändrad.\nNy fil: {1}",
        'pages_moved_new_file_voice': "{0} sidor flyttade, ny fil skapad.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Visa inte igen",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Säkerhetskopieringsinställning</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Säkerhetskopia PÅ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Vid alla ändringar som skriver över original</strong> (text, signatur, bild, form, OCR, rotera, infoga, radera/flytta sidor) skapas <strong>automatiskt en säkerhetskopia med tidsstämpel</strong> innan ändringen tillämpas.</p>
                <p style="margin: 5px 0 5px 20px;">• Säkerhetskopian ligger bredvid originalfilen (t.ex. <code>Dokument_säkerhetskopia_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Om du dessutom har aktiverat alternativet <strong>„Skriv över original“</strong>, skapas också en säkerhetskopia.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Säkerhetskopia AV</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Ingen säkerhetskopia skapas</strong> – varken vid överskrivning eller vid sidoperationer.</p>
                <p style="margin: 5px 0 5px 20px;">• Originalfilen kan oåterkalleligen förloras vid överskrivning.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Rekommenderas endast för erfarna användare!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tips:</strong> Säkerhetskopieringsinställningen är oberoende av alternativet „Skriv över original“. Du kan kombinera båda.<br>
                Du kan dölja det här meddelandet permanent.
            </div>
        </div>
        """,
        'backup_info_title': "Säkerhetskopieringsbeteende",
        'backup_info_voice': "Meddelande om säkerhetskopieringsbeteende vid sidoperationer. Säkerhetskopia på skriver över original, av skapar ny fil.",
        'show_backup_info': "Info om säkerhetskopieringsinställning",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Visa inte igen",
        'overwrite_enable_backup': "Aktivera säkerhetskopia (rekommenderas)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Skriv över original</p>
            <p>Om du aktiverar det här alternativet sparas ändringar (text, signatur, bild, form, OCR, rotera, infoga) <strong>direkt i originalfilen</strong> – <strong>ingen ny fil skapas</strong>.</p>
            <p>• Filnamnet förblir oförändrat.<br>
            • Tidsstämplar och suffix ignoreras.<br>
            • <strong>Utan säkerhetskopia kan originalfilen oåterkalleligen förloras.</strong></p>
            <p style="color: #FFD700;">Rekommendation: Aktivera även säkerhetskopieringsalternativet för att få automatiska säkerhetskopior.</p>
        </div>
        """,
        'overwrite_info_title': "Skriv över original",
        'overwrite_info_voice': "Varning: Skriv över original – ingen ny fil. Säkerhetskopia rekommenderas.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} sidor infogades.\n\nOriginalfilen skrevs över.\nEn säkerhetskopia skapades.",
        'pages_inserted_overwrite_no_backup': "{0} sidor infogades.\n\nOriginalfilen skrevs över.\nINGEN säkerhetskopia skapades.",
        'texts_saved_overwrite_with_backup': "Ändringarna sparades i originalfilen.\n\nEn säkerhetskopia skapades.",
        'texts_saved_overwrite_no_backup': "Ändringarna sparades i originalfilen.\n\nINGEN säkerhetskopia skapades.",
        'texts_crosses_saved_new_file': "{0} {1} och {2} {3} infogades.\n\nOriginalfilen förblev oförändrad.\nEn ny fil skapades.\n\nDen nya PDF-filen laddas...",
        'texts_saved_new_file': "{0} {1} infogades.\n\nOriginalfilen förblev oförändrad.\nEn ny fil skapades.\n\nDen nya PDF-filen laddas...",
        'crosses_saved_new_file': "{0} {1} infogades.\n\nOriginalfilen förblev oförändrad.\nEn ny fil skapades.\n\nDen nya PDF-filen laddas...",
        'elements_saved_new_file': "{0} element infogades.\n\nOriginalfilen förblev oförändrad.\nEn ny fil skapades.\n\nDen nya PDF-filen laddas...",
        'signatures_saved_overwrite_with_backup': "Signaturen(erna) sparades i originalfilen.\n\nEn säkerhetskopia skapades.",
        'signatures_saved_overwrite_no_backup': "Signaturen(erna) sparades i originalfilen.\n\nINGEN säkerhetskopia skapades.",
        'images_saved_overwrite_with_backup': "Bilden/bilderna sparades i originalfilen.\n\nEn säkerhetskopia skapades.",
        'images_saved_overwrite_no_backup': "Bilden/bilderna sparades i originalfilen.\n\nINGEN säkerhetskopia skapades.",
        'forms_saved_overwrite_with_backup': "Formen/Formerna sparades i originalfilen.\n\nEn säkerhetskopia skapades.",
        'forms_saved_overwrite_no_backup': "Formen/Formerna sparades i originalfilen.\n\nINGEN säkerhetskopia skapades.",
        'signatures_saved_new_file': "{0} signaturer infogades.\n\nOriginalfilen förblev oförändrad.\nEn ny fil skapades.\n\nDen nya PDF-filen laddas...",
        'images_saved_new_file': "{0} bilder infogades.\n\nOriginalfilen förblev oförändrad.\nEn ny fil skapades.\n\nDen nya PDF-filen laddas...",
        'forms_saved_new_file': "{0} former infogades.\n\nOriginalfilen förblev oförändrad.\nEn ny fil skapades.\n\nDen nya PDF-filen laddas...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Varning: Den här PDF-filen innehåller roterade sidor. Positioneringen kan avvika.",
        'page_rotated_warning_title': "Roterad sida upptäcktes",
        'page_rotated_warning_message': "Den aktuella sidan {0} är roterad {1}°.\n\nAtt infoga element på roterade sidor stöds inte.\n\nVill du rotera sidan till upprätt läge nu?",
        'page_rotated_warning_voice': "Varning: Sidan är roterad. Rotera den först.",
        'paste_on_rotated_page_simple_warning': "Infogning på sida {0} är inte möjlig!\n\nDen här sidan är roterad {1}°.\n\nRotera först sidan till 0° (Meny: Redigera → Rikta in sida).\n\nVarning:\nDet tidigare kopierade elementet går förlorat om du inte sparar innan du roterar sidan.",
        'paste_on_rotated_page_voice': "Infogning avbruten. Sidan är roterad. Rikta in sidan först.",
        'page_rotated_cancel': "Avbryt",
        'page_rotated_rotate_until_upright': "Rotera sidan upprepade gånger (tills den är upprätt)",
        'page_rotated_now_upright': "Sidan är nu upprätt. Du kan nu infoga.",
        'page_rotated_still_not_upright': "Sidan kunde inte roteras till upprätt läge. Korrigera manuellt.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hjälp: Korrigera roterade sidor",
        'help_rotated_pages_voice': "Hjälp för att korrigera roterade sidor öppnas.",
        'btn_help': "Hjälp",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Roterad sida – Infogning fungerar inte korrekt</p>

            <p>Om infogning av texter, signaturer eller former på en roterad sida inte fungerar korrekt kan du korrigera sidan med en extern PDF-redigerare.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Lösning med externt verktyg (t.ex. macOS Förhandsgranskning)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Exportera sida</strong><br>
                &nbsp;&nbsp;Klicka i menyn på <strong>Arkiv → Exportera som sidor</strong> eller använd en annan metod för att spara önskad sida som en enskild PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Öppna sidan i ett externt program</strong><br>
                &nbsp;&nbsp;Öppna den exporterade PDF-filen i en PDF-redigerare (t.ex. <strong>macOS Förhandsgranskning</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rotera sidan</strong><br>
                &nbsp;&nbsp;Rotera sidan så att den är upprätt (i Förhandsgranskning: <strong>Verktyg → Rotera</strong> eller <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Spara</strong><br>
                &nbsp;&nbsp;Spara den korrigerade sidan (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Infoga sidan igen i originaldokumentet</strong><br>
                &nbsp;&nbsp;Gå tillbaka till PDFDarkView och infoga den korrigerade sidan på önskad plats:<br>
                &nbsp;&nbsp;<strong>Redigera → Infoga sidor</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativ: Rotera sidan i originalfilen</p>
                <p style="margin: 5px 0 5px 20px;">• Använd den inbyggda rotationsfunktionen (<strong>Redigera → Rotera sida</strong>) för att korrigera sidan steg för steg.<br>
                • Efter varje rotation kan du kontrollera om infogning nu fungerar.<br>
                • Detta är ofta den snabbare lösningen – prova det först!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tips:</strong> Om du ofta stöter på roterade sidor kan du permanent dölja varningen i infogningsdialogen.<br>
                Positioneringen kan då avvika – använd det här alternativet endast om du känner till konsekvenserna.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Rikta in sidor",
        'menu_rotate_normalize_tooltip': "Rotera sida eller återställ till 0°",
        'normalize_current_page': "För den aktuella sidan till upprätt läge (ställ in på 0°)",
        'normalize_all_pages': "För alla sidor till upprätt läge (ställ in på 0°)",
        'page_normalized': "Sida {0} ställdes in i upprätt läge.",
        'all_pages_normalized': "Alla sidor ställdes in i upprätt läge.",
        'page_already_upright': "Sida {0} är redan upprätt.",
        'all_pages_already_upright': "Alla sidor är redan upprätta.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF-filen innehåller ingen sökbar text.</p><p>Vill du utföra OCR för att exportera till {0}?</p>",
        'export_ocr_voice': "PDF-filen innehåller ingen text. OCR krävs för export till {0}.",
        'export_no_ocr_possible': "Export utan OCR är inte möjlig. Utför OCR via menyn.",
        'ocr_failed_export_not_possible': "OCR misslyckades. Export kan inte utföras.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF-filen öppnas i Förhandsgranskning. Starta utskriftsprocessen där.",
        'print_preview_manual': "PDF-filen har öppnats. Utför utskriftskommandot manuellt (t.ex. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Slå ihop PDF-filer",
        'merge_pdfs': "Slå ihop PDF-filer",
        'merge_progress_title': "Slår ihop PDF-filer...",
        'merge_pdfs_list': "PDF-filer i ordning (Dra och släpp för att sortera)",
        'merge_add_pdf': "Lägg till PDF",
        'merge_remove': "Ta bort",
        'merge_move_up': "Upp",
        'merge_move_down': "Ner",
        'merge_pdfs_info': "💡 Tips: Du kan ändra ordningen genom att dra och släppa",
        'merge_no_pdfs': "Inga PDF-filer valda. Klicka på 'Lägg till PDF'.",
        'merge_info': "{0} PDF-filer valda (cirka {1} sidor)",
        'merge_open_file': "Öppna fil",
        'merge_merge': "Slå ihop",
        'merge_error': "Fel vid ihopslagning",
        'merge_min_two_pdfs_error': "Välj minst två PDF-filer att slå ihop.",
        'merge_select_pdfs': "Välj PDF-filer att slå ihop",
        'merge_error_file': "Fel vid bearbetning",
        'merge_cancelled': "Ihopslagningen avbröts",
        'merge_preparing': "Förbereder...",
        'merge_processing': "Bearbetar PDF {0} av {1}",
        'merge_saving': "Sparar ihop slagen PDF...",
        'merge_complete': "Klart!",
        'merge_success_title': "Ihopslagningen lyckades",
        'merge_success_voice': "{0} PDF-filer slogs ihop.",
        'merge_success_message': "{0} PDF-filer slogs ihop.\n\nDet nya dokumentet har nu {1} sidor.\n\nNy fil:\n{2}\n\nSpara plats:\n{3}\n{2}\n\nVill du öppna den här PDF-filen?",
        'replace_file_title': "Ersätta fil?",
        'replace_file_message': "En PDF-fil är redan öppen. Vill du ersätta den med den nya filen?",
        'btn_yes': "Ja",
        'btn_no': "Nej",
        'filename_merge_suffix': "ihopslagen",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Öppnar {0}...",
        'progress_merge_reading': "Läser {0}...",
        'progress_merge_adding': "Lägger till {0} sidor...",
        'progress_merge_optimizing': "Optimerar PDF...",
        'progress_merge_writing': "Skriver PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "stängning av PDF-filen",
        'action_close_window': "stängning av fönstret",
        'action_open_new_pdf': "öppning av en ny PDF",
        'action_quit_app': "avslutning av programmet",
        'changes_saved': "Ändringarna har sparats.",
        'file_close_title': "Stäng PDF-fil",
        'save_before_action': "Ska ändringarna sparas före {0}? Ja eller Nej?",
        'save_before_action_voice': "Ska ändringarna sparas före {0}? Ja eller Nej?",
        'save_before_close_question': "Ska ändringarna sparas före stängning? Ja eller Nej?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Sökbar PDF skapad:\n\n{0}\n\n<b>försök igen om det behövs",
        "ocr_rotate_title": "Justera sidor före OCR",
        "ocr_rotate_question": "PDF-filen innehåller roterade sidor.\nVill du justera alla sidor till 0° före OCR?\nDetta förbättrar textigenkänningen avsevärt.",
        "ocr_rotate_yes": "Ja, justera",
        "ocr_rotate_no": "Nej, starta OCR direkt",
        "ocr_rotate_voice": "PDF-filen innehåller roterade sidor. Bör alla sidor justeras före OCR?",
        "ocr_not_performed_message": "Ingen text finns. Utför OCR (menyn \"Redigera\" → \"Utför OCR\" eller tangent Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-inställningar",
        "ocr_language_btn": "Välj OCR-språk",
        "ocr_language": "OCR-språk",
        "ocr_language_current": "Aktuellt språk:",
        "ocr_param_info": "Information om parametern",

        "ocr_force_ocr_label": "Tvinga OCR",
        "ocr_deskew_label": "Korrigera skevhet",
        "ocr_clean_label": "Rensa bild",
        "ocr_oversample_label": "Upplösning (DPI)",
        "ocr_pagesegmode_label": "Sidindelning",
        "ocr_oem_label": "OCR-motorläge",
        "ocr_optimize_label": "PDF-komprimering",
        "ocr_jobs_label": "Parallella processer",
        "ocr_verbose_label": "Loggdetaljer",

        "ocr_force_ocr_tooltip": "Tvinga OCR på varje sida, även om text redan finns",
        "ocr_deskew_tooltip": "Justera skeva skanningar automatiskt",
        "ocr_clean_tooltip": "Ta bort brus och artefakter från bilden",
        "ocr_oversample_tooltip": "Skala upp bilden före OCR till denna DPI",
        "ocr_pagesegmode_tooltip": "Bestämmer hur sidan delas upp i textområden",
        "ocr_oem_tooltip": "Väljer Tesseracts OCR-motor",
        "ocr_optimize_tooltip": "Komprimeringsnivå för utdata-PDF",
        "ocr_jobs_tooltip": "Antal parallella OCR-processer",
        "ocr_verbose_tooltip": "Detaljnivå för loggutdata",
        "ocr_settings_explain_btn": "Förklaring",

        "ocr_force_ocr_explain": "Tvingar textigenkänning på <b>varje</b> sida, även om den redan innehåller text.\n\nRekommendation: <b>På</b> för skannade PDF-filer, <b>Av</b> för ursprungliga PDF-filer med redan befintlig text.",

        "ocr_deskew_explain": "Korrigerar lätt skeva skanningar (upp till ca 5°).\n\nRekommendation: <b>På</b> för skannade dokument, <b>Av</b> om sidorna redan är perfekt raka.",

        "ocr_clean_explain": "Tar bort brus, prickar och små artefakter från bilden.\n<b>VIKTIGT:</b> För arabiska, thailändska eller vietnamesiska texter med diakritiska tecken (prickar över/under bokstäver) bör detta alternativ <b>inaktiveras</b>, annars kan viktiga tecken gå förlorade.",

        "ocr_oversample_explain": "Skalar upp bilden <b>före</b> textigenkänning till angiven DPI.<br><br>• <b>72-150 DPI:</b> Mycket snabbt, men låg igenkänningsgrad<br>• <b>200-300 DPI:</b> Optimalt intervall (Standard: 300)<br>• <b>400+ DPI:</b> Knappt bättre igenkänning, men betydligt större filer<br><br>Rekommendation: 300 DPI för komplexa skrifter (arabiska, kinesiska, japanska), 200 DPI för västerländska språk.",

        "ocr_pagesegmode_explain": "Bestämmer hur Tesseract delar upp sidan i textområden.\n\n• <b>3 - Automatiskt (Standard):</b> Bra för blandade layouter\n• <b>4 - Enkel kolumn:</b> För texter med en kolumn\n• <b>5 - Vertikalt block:</b> För vertikala skrifter (japanska, kinesiska)\n• <b>6 - Enhetligt textblock:</b> Optimalt för flytande text utan kolumner\n• <b>11 - Rå bild:</b> För dåliga skanningar / handskrift\n\nRekommendation: <b>6</b> för enkla textdokument, <b>3</b> för komplexa layouter.",

        "ocr_oem_explain": "Väljer Tesseracts OCR-motor.\n\n• <b>0 - Legacy:</b> Gammal motor (snabb, men mindre exakt)\n• <b>1 - LSTM:</b> Neural motor (långsammare, men mer exakt)\n• <b>2 - Legacy + LSTM:</b> Kombinerar båda resultaten\n• <b>3 - Standard (LSTM föredras):</b> Bästa valet för de flesta fall\n\nRekommendation: <b>3</b> för maximal igenkänningsnoggrannhet.",

        "ocr_optimize_explain": "Komprimerar utdata-PDF.\n\n• <b>0:</b> Ingen optimering (snabbast bearbetning)\n• <b>1:</b> Lätt optimering (bra kompromiss)\n• <b>2:</b> Måttlig optimering\n• <b>3:</b> Stark optimering (minsta filen, men långsammare)\n\nRekommendation: <b>1</b> för dagligt bruk.",

        "ocr_jobs_explain": "Antal parallella processer för OCR.\n\n• <b>1:</b> Långsamt, men lägst minnesförbrukning\n• <b>4-8:</b> Optimalt för moderna flerkärniga processorer\n• <b>12+:</b> Knappt snabbare bearbetning med hög minnesanvändning\n\nRekommendation: Antal CPU-kärnor (t.ex. <b>4</b> på 4-kärniga system).",

        "ocr_verbose_explain": "Detaljnivå för loggutdata i konsolen.\n\n• <b>0:</b> Ingen utdata\n• <b>1:</b> Förlopp och statusmeddelanden\n• <b>2:</b> Detaljerad utdata\n• <b>3:</b> Fullständig felsökningsutdata (mycket omfattande)\n\nRekommendation: <b>1</b> för normal drift.",

        "ocr_reset_title": "Inställningarna har återställts",
        "ocr_reset_message": "Alla OCR-inställningar har återställts till standardvärden.",
        "info_tooltip": "Mer information om denna parameter",
        "ocr_reset_defaults": "Återställ till standard",

        "ocr_psm_0": "Automatiskt (Legacy-motor)",
        "ocr_psm_1": "Automatisk kolumndetektering",
        "ocr_psm_3": "Automatiskt (Standard)",
        "ocr_psm_4": "Enkel kolumn",
        "ocr_psm_5": "Vertikalt block",
        "ocr_psm_6": "Enhetligt textblock",
        "ocr_psm_7": "Enkel textrad",
        "ocr_psm_8": "Enstaka ord",
        "ocr_psm_11": "Rå bild (ingen layoutanalys)",

        "ocr_oem_0": "Legacy-motor (snabb)",
        "ocr_oem_1": "LSTM-motor (neural, exakt)",
        "ocr_oem_2": "Legacy + LSTM kombinerad",
        "ocr_oem_3": "Standard (LSTM föredras)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-språk...",
        "ocr_language_title": "Välj OCR-språk",
        "ocr_language_instruction": "Välj språk för textigenkänning (OCR).\nFörsiktighet: Flera språk går ut över prestanda och noggrannhet!\nDu får bäst resultat om du bara väljer ett språk.",
        "ocr_language_predefined": "Fördefinierade kombinationer",
        "ocr_language_custom": "Anpassad...",
        "ocr_language_selected": "Valda OCR-språk",
        "ocr_language_changed": "OCR-språk ändrat till {0}",
        "ocr_language_auto_detect": "Tillgängliga språk upptäcks automatiskt.",
        "ocr_language_none_found": "Ingen Tesseract-språkdata hittades! Installera språkpaket (t.ex. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Anpassat språkval",
        "ocr_language_available": "Tillgängliga språk (installerade):",
        "ocr_language_select_hint": "Välj ett eller flera språk:",
        "ocr_language_confirm": "Använd",
        "ocr_language_reset": "Återställ till standard (deu+eng+vie)",
        "ocr_language_priorities": "Rekommenderade språk (förinstallerade):",

        "select_all_languages": "Välj alla",
        "clear_all_languages": "Rensa val",
        "install_language_packs": "Installera saknade språkpaket...",
        "install_hint": "💡 Tips: Alla språk är inte installerade på ditt system. Via denna knapp får du hjälp med installationen.",
        "ocr_language_install_title": "Installation av Tesseract-språkpaket",

        "ocr_missing_languages": "Saknade OCR-språkpaket",
        "ocr_missing_languages_message": "Följande valda språk är inte installerade på ditt system:\n\n{0}\n\nInstallera de saknade språkpaketen (se hjälp under 'Installationshjälp').\n\nVill du öppna installationshjälpen nu?",
        "ocr_missing_languages_voice": "Saknade språkpaket. Installera de saknade språken.",
        "ocr_install_help_now": "Öppna hjälp",
        "ocr_continue_anyway": "Försök ändå",
        "ocr_language_error_title": "OCR-språkfel",
        "ocr_language_error_message": "Fel vid textigenkänning: {0}\n\nKontrollera dina OCR-språkinställningar (Inställningar → OCR-språk).",
        "ocr_install_help_button": "Installationshjälp",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Installera Tesseract-språkpaket</p>

        <p>För att OCR ska fungera på ett specifikt språk måste motsvarande språkdata vara installerade på ditt system. Följ instruktionerna för ditt operativsystem:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Öppna <strong>Terminalen</strong> (Finder → Program → Verktyg → Terminal).</li>
        <li>Installera alla tillgängliga språk med:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Detta kan ta några minuter.)</li>
        <li>Eller bara enskilda språk (t.ex. vietnamesiska):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Med nuvarande Homebrew-versioner kan <code>*.traineddata</code> behöva laddas ned manuellt (se nedan).</li>
        <li>Efter installation: Stäng denna dialogruta och öppna OCR-språkvalet igen – de nya språken visas automatiskt.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Öppna en terminal (Ctrl+Alt+T).</li>
        <li>Installera önskat språk, t.ex. för vietnamesiska:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Viktiga språkkoder: <code>deu</code> (tyska), <code>eng</code> (engelska), <code>vie</code> (vietnamesiska), <code>spa</code> (spanska), <code>fra</code> (franska), <code>ita</code> (italienska), <code>nld</code> (nederländska), <code>fin</code> (finska), <code>swe</code> (svenska), <code>nor</code> (norska).</li>
        <li>Visa alla tillgängliga paket:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuellt)</p>
        <ol>
        <li>Ladda ner önskade <code>*.traineddata</code>-filer från:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (t.ex. <code>vie.traineddata</code> för vietnamesiska).</li>
        <li>Kopiera filerna till Tesseracts språkmapp, vanligtvis:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Anpassa efter individuell installation.)</li>
        <li>Starta om applikationen (eller öppna OCR-språkvalet igen).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativ för alla system</p>
        <ul>
        <li>Installera <strong>OCRmyPDF</strong> och <strong>Tesseract</strong> med en pakethanterare efter eget val. De flesta installationer innehåller redan några standardspråk (engelska, tyska, franska).</li>
        <li>Saknade språk kan installeras när som helst – OCR-språkvalet listar endast de faktiskt existerande språken.</li>
        </ul>

        <hr>
        <p><b>✅ Efter installation:</b> Ingen omstart av applikationen behövs – de nyligen tillagda språken visas omedelbart i listan.</p>
        <p><b>📖 Hjälp med språkkoder:</b> En fullständig lista finns i <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract-dokumentationen</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans-teckensnitt",
        "info_noto_font_voice": "Guide för installation av Noto Sans-teckensnitt",
        "btn_info_noto_font_install": "Teckensnittsinfo",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Så här installerar du de kostnadsfria Noto-teckensnitten från Google</h2>

        <p><strong>Noto-teckensnitten</strong> är en öppen källkod-teckensnittsfamilj från Google. Deras mål är att inte se <em>"någon tofu"</em> (dvs. inga tomma rutor □) och att korrekt visa varje tecken från Unicode-standarden. De är det perfekta tillägget för applikationer som måste visa texter på många olika språk.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installation på macOS</h3>

        <p><strong>Metod 1: Med Homebrew (för avancerade användare)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metod 2: Via "Font Book" (Rekommenderas)</strong></p>

        <ol>
        <li>Ladda ner det officiella teckensnittspaketet:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Packa upp ZIP-filen</li>
        <li>Kopiera filerna till <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installation på Windows (10 & 11)</h3>

        <p><strong>Metod 1: Microsoft Store (Rekommenderas)</strong><br>
        Sök efter "Google Noto Fonts" eller "Noto Sans" och klicka på <strong>Installera</strong>.</p>

        <p><strong>Metod 2: Manuell installation</strong></p>

        <ol>
        <li>Ladda ner:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Packa upp ZIP</li>
        <li>Välj .ttf / .otf-filer</li>
        <li>Högerklicka → <strong>Installera</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        eller<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Namn\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installation på Linux</h3>

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

        <p>Verifiering:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Hantera bokmärken",
        "bookmark_add": "Lägg till bokmärke",
        "bookmark_add_tooltip": "Spara aktuell sida som bokmärke",
        "bookmark_remove": "Ta bort bokmärke",
        "bookmark_remove_tooltip": "Radera det markerade bokmärket",
        "bookmark_remove_all": "Ta bort alla",
        "bookmark_remove_all_tooltip": "Radera alla bokmärken för denna PDF",
        "bookmark_jump": "Gå till bokmärke",
        "bookmark_jump_tooltip": "Gå till vald sida",
        "bookmark_name": "Namn",
        "bookmark_page": "Sida",
        "bookmark_no_bookmarks": "Inga bokmärken.\nKlicka på 'Lägg till' för att spara aktuell sida som bokmärke.",
        "bookmark_added": "Bokmärke för sida {0} tillagt: {1}",
        "bookmark_removed": "Bokmärke borttaget: {0}",
        "bookmark_all_removed": "Alla bokmärken har tagits bort.",
        "bookmark_name_default": "Sida {0}",
        "bookmark_name_prompt": "Namn för bokmärket:\n(lång text kommer att förkortas till 50 tecken)",
        "bookmark_name_prompt_title": "Bokmärkesnamn",
        "bookmark_confirm_remove_all": "Är du säker på att du vill ta bort alla {0} bokmärken?",
        "menu_bookmarks": "Bokmärken",
        "bookmark_manage": "Hantera bokmärken",
        "bookmark_next": "Nästa bokmärke",
        "bookmark_prev": "Föregående bokmärke",
        "bookmark_page_display": "Sida {0}",
        "bookmark_exists": "Det finns redan ett bokmärke för denna sida med detta namn.",
        "bookmark_select_first": "Välj först ett bokmärke.",
        "bookmark_confirm_remove": "Är du säker på att du vill ta bort bokmärket 'Sida {0}: {1}'?",
        "bookmark_jumped_to": "Gick till bokmärke '{0}' på sida {1}.",
        "bookmark_jumped_to_voice": "Bokmärke {0}, sida {1}",
        "btn_close": "Stäng",

        "bookmark_list": "Dina bokmärken",
        "bookmark_rename": "Byt namn på bokmärke",
        "bookmark_rename_tooltip": "Ändra namnet på det valda bokmärket",
        "bookmark_rename_title": "Byt namn på bokmärke",
        "bookmark_rename_prompt": "Nytt namn för bokmärke på sida {0}:\n(max. 50 tecken)",
        "bookmark_renamed": "Bokmärket '{0}' har bytt namn till '{1}'.",
        "bookmark_item_tooltip": "Sida {0}: {1}\nDubbelklicka för att gå",
        "bookmark_name_exists_question": "Det finns redan ett bokmärke med namnet '{0}' på denna sida.\nByt namn ändå?",

        "context_bookmarks": "Bokmärken",
        "context_bookmark_add_here": "Lägg till bokmärke för denna sida",
        "context_bookmarks_existing": "Befintliga bokmärken:",
        "context_bookmarks_jump": "Gå till bokmärke:",
        "context_bookmarks_none": "Inga bokmärken",
        "context_bookmarks_clear_all": "Ta bort alla {0} bokmärken",

        "bookmark_search_placeholder": "Sök i bokmärken... (namn eller sida)",
        "bookmark_search_results": "%d bokmärken hittades för \"%s\"",
        "bookmark_no_search_results": "Inga bokmärken hittades för \"%s\"",
        "bookmark_no_search_results_label": "Inga resultat för \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Redigera PDF-metadata",
        "metadata_title": "Titel",
        "metadata_title_placeholder": "Dokumenttitel",
        "metadata_title_tooltip": "Dokumentets titel (visas i titelfältet)",
        "metadata_author": "Författare",
        "metadata_author_placeholder": "Författarens namn",
        "metadata_author_tooltip": "Skaparen av dokumentet",
        "metadata_subject": "Ämne",
        "metadata_subject_placeholder": "Dokumentets ämne",
        "metadata_subject_tooltip": "En kort beskrivning av innehållet",
        "metadata_keywords": "Nyckelord",
        "metadata_keywords_placeholder": "Nyckelord separerade med kommatecken",
        "metadata_keywords_tooltip": "Nyckelord för att kategorisera dokumentet",
        "metadata_creator": "Skapare",
        "metadata_creator_placeholder": "Applikation som skapade PDF:en",
        "metadata_creator_tooltip": "Programvaran som dokumentet skapades med",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Applikation som konverterade PDF:en",
        "metadata_producer_tooltip": "Programvaran som konverterade PDF:en",
        "metadata_creation_date": "Skapelsedatum",
        "metadata_creation_date_tooltip": "Datumet för dokumentets skapande",
        "metadata_mod_date": "Ändringsdatum",
        "metadata_mod_date_tooltip": "Datumet för senaste ändringen",
        "metadata_pdf_info": "📄 PDF-information",
        "metadata_pages": "Antal sidor",
        "metadata_file_size": "Filstorlek",
        "metadata_pdf_version": "PDF-version",
        "metadata_encrypted": "Krypterad",
        "metadata_encrypted_yes": "Ja (lösenordsskyddad)",
        "metadata_encrypted_no": "Nej",
        "metadata_reload": "📂 Ladda om från PDF",
        "metadata_reset": "Ignorera ändringar",
        "metadata_reloaded": "Metadata har laddats om från PDF:en.",
        "metadata_reset_done": "Alla metadatablad har återställts.",
        "metadata_no_file": "Ingen PDF-fil laddad.",
        "metadata_save_error": "Fel vid sparande av metadata",
        "metadata_saved": "Metadata har sparats.",
        "metadata_pdf_version_unknown": "PDF (okänd)",
        "metadata_saved_message": "Metadata har sparats.",
        "metadata_saved_voice": "Metadata sparade.",

        "metadata_custom": "🔧 Anpassad metadata",
        "metadata_custom_placeholder": "{\n  \"mitt_falt\": \"mitt_varde\",\n  \"annat_falt\": 123\n}",
        "metadata_custom_tooltip": "JSON-format för anpassad metadata (valfritt)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Mall \"{0}\" vald - Dubbelklicka för att infoga",
        "text_use_template": "Använd textblock",
        "text_type": "Typ",
        "text_search_templates": "Sök i textblock...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Export / Import information",
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

        <h3>📦 Vad exporteras? (Översikt)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Allmänna applikationsinställningar</span></li>
            <li class="detail">• Mörkt/Ljust läge</li>
            <li class="detail">• Mörkt läge inversion för bilder</li>
            <li class="detail">• Grått tröskelvärde</li>
            <li class="detail">• Språk</li>
            <li class="detail">• Fönstergeometri</li>
            <li class="detail">• Zoomläge</li>
            <li class="detail">• Navigering (Navigeringsfält synligt)</li>
            <li class="detail">• Talutdata (på/av)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Säkerhetskopieringsinställningar</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Filnamngivning (Tidsstämpel, Avskiljare, Suffix)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Inställningar för insättningar av</span></li>
            <li class="detail">• Signaturer</li>
            <li class="detail">• Text och textblock</li>
            <li class="detail">• Kryss, bilder och former</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-inställningar</span></li>
            <li class="detail">• Språk</li>
            <li class="detail">• Tvinga OCR · Sidläge</li>
            <li class="detail">• Bildförbehandling: Korrigera skevhet, Rengör, Översampling</li>
            <li class="detail">• Antal parallella jobb</li>
            <li class="detail">• Inversionsläge</li>
            <li class="detail">• Grått tröskelvärde</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bokmärken</span></li>
            <li class="detail">• Alla bokmärken per PDF-fil (Sida, Namn, Skapelsetid)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Lösenordsdatabas</span></li>
            <li class="detail">• Sparade PDF-lösenord (valfritt krypterade eller klartext)</li>
            <li class="detail">• Huvudlösenord hash (om angivet)</li>
            <li class="detail">• Verifieringsdata</li>
        </ul>

        <h4>⚠️ Viktiga anmärkningar</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Vid import:</strong>
            <ul>
                <li><span class="warning">➜ ALLA aktuella inställningar kommer att skrivas över fullständigt</span></li>
                <li>• En omstart av applikationen är obligatorisk</li>
                <li>• Befintliga signaturer, textblock och bokmärken kommer att ersättas</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Huvudlösenord och exportläge:</strong>
            <ul>
                <li>• När huvudlösenordet är aktivt kan du välja:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dekrypterad</strong></span> (lösenorden är i klartext i ZIP-filen)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Krypterad</strong></span> (endast läsbar med huvudlösenordet på målsystemet)</li>
                <li>• Huvudlösenordets hash lagras <strong>alltid</strong> krypterad</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Säkerhetsmeddelande:</strong>
            <ul>
                <li>• Den exporterade ZIP-filen innehåller känsliga uppgifter (<strong>lösenord, bokmärken, signaturer</strong>)</li>
                <li>• Förvara den säkert (t.ex. krypterat USB-minne, lösenordshanterare)</li>
                <li>• Om filen försvinner är sparade PDF-lösenord oåterkalleligt förlorade</li>
            </ul>
        </div>

        <h4>📁 Exportformat</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Inställningarna sparas i en enda ZIP-fil:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Denna ZIP innehåller den fullständiga <code>settings.json</code> (från din konfiguration) samt eventuellt inbäddade signaturbildfiler och krypterade lösenord.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Signaturer - Guide",
        'signature_guide_html': """
        📝 <strong>Signaturer - Snabbguide</strong><br>
        <ul>
        <li>Ställ in masterlösenord</li>
        <li>Konfigurera signaturer i menyn <em>Inställningar</em> (storlek, tidsstämpel, …)</li>
        <li>Infoga med <strong>HÖGERKLICK</strong> på önskad position (masterlösenord krävs en gång per session)</li>
        <li>Flytta signaturen med musen eller piltangenterna</li>
        <li>Infoga flera signaturer efter varandra</li>
        <li>Anpassa varje signatur individuellt</li>
        <li>Förkasta enskild signatur</li>
        <li>Spara / förkasta alla signaturer på en gång</li>
        <li>Alternativt kan menyraden också användas.</li>
        </ul>
        """,
        'signature_guide_voice': "Snabbguide för signaturer. Ställ in masterlösenord. Konfigurera signaturer i inställningar. Infoga med högerklick.",

        'image_guide_title': "Infoga bilder - Guide",
        'image_guide_html': """
        📷 <strong>Infoga bilder i PDF - Snabbguide</strong><br>
        <ol>
        <li>Högerklicka på önskad position</li>
        <li><em>„Infoga bild“</em> → Välj bild</li>
        <li>Positionera bilden: Dra med musen</li>
        <li>Justera storlek: Dra i hörnen/kanterna</li>
        <li>Bibehåll bildförhållande: Tangent <strong>[A]</strong></li>
        <li>Ytterligare justeringar: Högerklicka på bilden</li>
        </ol>
        <p><strong>Tips:</strong> I snabbmenyn kan du justera inställningarna.</p>
        """,
        'image_guide_voice': "Snabbguide för bilder. Högerklicka, infoga bild, välj. Positionera med musen, justera storlek i hörn. Bildförhållande med tangent A.",

        'form_guide_title': "Infoga former - Guide",
        'form_guide_html': """
        📐 <strong>Infoga former i PDF - Snabbguide</strong><br>
        <ol>
        <li>Välj formtyp (rektangel, ellips, linje, pil)</li>
        <li>Klicka på position:
            <ul>
            <li>För rektangel/ellips: Ett klick placerar formen</li>
            <li>För linje/pil: Två klick för start- och slutpunkt</li>
            </ul>
        </li>
        <li>Positionera formen: Dra med musen</li>
        <li>Justera storlek: Dra i hörnen/kanterna</li>
        <li>Spara form: <strong>Enter</strong></li>
        <li>Förkasta form: <strong>ESC</strong></li>
        <li>Ytterligare justeringar: Högerklicka på formen</li>
        </ol>
        <p><strong>Tips:</strong> I snabbmenyn kan du justera inställningarna.</p>
        """,
        'form_guide_voice': "Snabbguide för former. Välj formtyp. För rektangel eller ellips klicka en gång, för linje eller pil två gånger. Positionera med musen, justera storlek i hörn. Spara med Enter, förkasta med Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "föregående",
        "btn_next_result": "nästa",
        "ocr_text_window": "OCR-textfönster",
        "bookmark_existing": "Befintliga bokmärken",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR-jämförelse Mac - Windows",
        'ocr_method_mac_win_title': "OCR-skillnader mellan Mac och Windows",
        'ocr_method_mac_win_voice': "Mac är bättre",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Skillnader mellan macOS och Windows</strong></p>

        <p><strong>macOS (rekommenderas)</strong></p>
        <p>Verktyg:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resultat:</p>
        <ul>
        <li>En sökbar PDF med inbäddad text som till stor del bevarar den ursprungliga layouten.</li>
        </ul>
        <p>Fördelar:</p>
        <ul>
        <li>Utmärkt kvalitet på textigenkänning (även på sneda sidor).</li>
        <li>Bevarande av vektorgrafik och teckensnitt.</li>
        <li>GUI-förloppsindikator via underprocessutvärdering.</li>
        <li>Full kontroll över alla OCR-parametrar (Deskew, Clean, Oversample, optimering).</li>
        <li>Textsökning är direkt tillgänglig i huvudfönstret (PDF-visning).</li>
        </ul>
        <p>Nackdelar:</p>
        <ul>
        <li>Kräver ytterligare systemverktyg (ocrmypdf, Ghostscript, unpaper, pngquant – ingår i apppaketet).</li>
        <li>Mer komplex felhantering (deadlocks, tidsgränser).</li>
        </ul>

        <p><strong>Windows (stabilt alternativ)</strong></p>
        <p>Verktyg:</p>
        <ul>
        <li>pytesseract (direkt anslutning till Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resultat:</p>
        <ul>
        <li>En sökbar PDF som visuellt motsvarar en bild-PDF, men är sökbar via den genomskinliga texten.</li>
        </ul>
        <p>Fördelar:</p>
        <ul>
        <li>Inga kommer jag på just nu.</li>
        </ul>
        <p>Nackdelar:</p>
        <ul>
        <li>PDF är i huvudsak en bild med osynlig text; layouten kan avvika något för komplexa dokument (kolumner, tabeller).</li>
        <li>Ingen automatisk snedställningskorrigering (--deskew) eller bildrensning (--clean).</li>
        <li>GUI-förloppsindikatorn uppdateras endast grovt baserat på antalet bearbetade sidor.</li>
        <li>OCR-hastigheten är något långsammare (eftersom varje sida bearbetas separat).</li>
        <li>Textsökning omdirigeras till OCR-textfönstret.</li>
        </ul>

        <p><strong>Gemensamma drag</strong></p>
        <ul>
        <li>Båda metoderna skapar en sökbar PDF i samma katalog som källfilen.</li>
        <li>OCR-inställningarna (språk, DPI, sidsegmenteringsläge, OCR-motorläge) kan konfigureras via OCRSettingsDialog och gäller i båda implementeringarna.</li>
        </ul>

        <p><strong>Rekommendation:</strong></p>
        <ul>
        <li>macOS: ocrmypdf-binären ger de bästa resultaten – Köp en Mac och använd versionen (PDFDarkView för Mac med Apple Silicon eller Intel-chip). OCR-resultaten är bättre än under Windows!</li>
        <li>Windows: Använd pytesseract-lösningen. Den är stabil och ger fullt tillräcklig kvalitet för de flesta dokument.</li>
        </ul>

        <p><strong>Viktig anmärkning:</strong></p>
        <ul>
        <li>Båda versionerna är fullt integrerade i användargränssnittet – användaren märker ingen skillnad.</li>
        <li>Programmet bestämmer automatiskt vilken OCR-motor som ska användas baserat på operativsystemet.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Skapa signatur (från skanning)",
        "signature_create_title": "Välj skannad signatur (PDF/bild)",
        "image_pdf_filter": "Bilder och PDF",
        "signature_pdf_empty": "PDF-filen innehåller inga sidor.",
        "signature_created_success": "Signatur skapades: {0}",
        "signature_create_error": "Fel vid skapande av signatur:\n{0}",
        "rembg_missing": "rembg är inte installerat.\nInstallera: pip install rembg\nFel: {0}",
        "signature_name_title": "Filnamn för signaturen",
        "signature_name_message": "Ange ett filnamn för den nya signaturen (sparas som PNG med genomskinlig bakgrund):",
        "signature_name_label": "Filnamn:",
        "signature_name_voice": "Ange filnamn för signatur",
        "signature_processing": "Bearbetning pågår...",
        "signature_creation_title": "Skapar signatur",
        "signature_overwrite_warning": "Filen '{0}' finns redan. Skriv över?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Förbered PDF för signatur",
        "signature_prepare_instruction":"Välj en PDF som på en enda sida innehåller en skannad signatur.\n\nFör optimal igenkänning, se till att:\n• Signaturen är skriven med svart bläck (kulspetspenna eller finliner) på vitt papper.\n• Signaturen finns i den övre tredjedelen av en annars tom A4-sida.\n• PDF-filen är skannad med minst 300 dpi.\n• Signaturen är tydlig och inte för tunn.\n• Det finns inga störande bakgrundsmönster eller linjer.",
        "signature_prepare_voice":"Välj en PDF med en skannad signatur. Var uppmärksam på god kvalitet och kontrast.",
        "sig_thickness_label":"Linjetjocklek:",
        "sig_thickness_normal":"Normal (tunn)",
        "sig_thickness_bold":"Fet (rekommenderas)",
        "sig_thickness_very_bold":"Mycket fet",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Lägg till GUI- och OCR-språk - Guide",
        'language_guide_title': "Lägg till GUI- och OCR-språk",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Ladda ner önskad översättningsfil <code>translations_xy.py</code> från<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        och placera den i följande katalog:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Öppna din webbläsare.</li>
        <li>Gå till: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Sök på höger skärmkant efter "Releases" och välj den märkt <strong>"latest"</strong>.</li>
        <li>På nästa releasesida laddar du ner filen <code>Source Code.zip</code> längst ner.</li>
        <li>Packa upp ZIP-filen.</li>
        <li>Sök i den uppackade mappen efter alla språkfiler du behöver och kopiera dem till katalogen:<br/>
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
        "menu_watermark":"Infoga vattenstämpel",
        "fullpage_text_watermark_title":"Text som vattenstämpel",
        "fullpage_image_watermark_title":"Bild som vattenstämpel",
        "filename_with_watermark":"_med_vattenstämpel",
        "watermark_text":"Text:",
        "watermark_text_placeholder":"Din vattenstämpeltext...",
        "watermark_font_family":"Teckensnitt:",
        "watermark_font_size":"Teckenstorlek:",
        "watermark_format":"Formatering:",
        "watermark_bold":"Fet",
        "watermark_italic":"Kursiv",
        "watermark_color":"Färg:",
        "watermark_choose_color":"Välj färg...",
        "watermark_opacity":"Opacitet / Transparens:",
        "watermark_direction":"Läsriktning:",
        "watermark_direction_l_r":"Vänster → Höger",
        "watermark_direction_bl_tr":"Nere vänster → Uppe höger",
        "watermark_direction_tl_br":"Uppe vänster → Nere",
        "watermark_direction_b_t":"Nere → Uppe",
        "watermark_direction_t_b":"Uppe → Nere",
        "watermark_preview":"Förhandsgranskning:",
        "watermark_preview_sample":"Exempeltext",
        "watermark_empty_text":"Ange en text.",
        "watermark_applied":"Vattenstämpeln har applicerats på alla sidor.",
        "watermark_saved":"Vattenstämpel sparad.",
        "image_scale":"Storlek:",
        "image_preview":"Bildförhandsgranskning:",
        "no_image_selected":"Ingen bild vald",
        "browse":"Bläddra...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Raderingsmarkeringar",
        "redact_add_black": "Raderingsmarkering (svart)",
        "redact_add_white": "Raderingsmarkering (vit / radera)",
        "redact_added_black": "Svart raderingsmarkering tillagd",
        "redact_added_white": "Vit raderingsmarkering tillagd",
        "redact_apply_all": "Applicera alla raderingsmarkeringar och spara",
        "redact_discard_all": "Kassera alla raderingsmarkeringar",
        "redact_discard": "Kassera denna raderingsmarkering",
        "no_redactions": "Inga raderingsmarkeringar",
        "redact_confirm_title": "Applicera raderingsmarkeringar permanent",
        "redact_confirm_message": "Varning: De markerade områdena kommer att raderas permanent (svart eller vitt).\nEn säkerhetskopia kommer att skapas (om aktiverad).\n\nFortsätta?",
        "redact_apply": "Ja, radera nu",
        "redact_saved": "{0} raderingsmarkering(ar) har applicerats och sparats.",
        "redact_saved_voice": "{0} raderingsmarkering(ar) applicerade",
        "redact_error": "Fel under raderingsmarkering",
        "filename_redacted":"_raderad",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Infoga sidnummer',
        'page_numbers_format': 'Nummerformat:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabiska)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romerska små)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romerska stora)',
        'page_numbers_format_letter': 'A, B, C ... (bokstäver)',
        'page_numbers_format_custom': 'Anpassad',
        'page_numbers_custom_pattern': 'Mönster:',
        'page_numbers_custom_placeholder': 't.ex. "Sida {nummer}" eller "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Använd {nummer} för aktuellt sidnummer och {total} för totalt antal',
        'page_numbers_position': 'Position:',
        'page_numbers_pos_tl': 'Uppe vänster',
        'page_numbers_pos_tc': 'Uppe mitt',
        'page_numbers_pos_tr': 'Uppe höger',
        'page_numbers_pos_ml': 'Mitten vänster',
        'page_numbers_pos_mc': 'Centrerad',
        'page_numbers_pos_mr': 'Mitten höger',
        'page_numbers_pos_bl': 'Nere vänster',
        'page_numbers_pos_bc': 'Nere mitt',
        'page_numbers_pos_br': 'Nere höger',
        'page_numbers_margins': 'Marginaler:',
        'page_numbers_margin_x': 'Horisontellt avstånd:',
        'page_numbers_margin_y': 'Vertikalt avstånd:',
        'page_numbers_range': 'Sidintervall:',
        'page_numbers_all_pages': 'Alla sidor',
        'page_numbers_custom_range': 'Anpassat intervall',
        'page_numbers_from': 'Från:',
        'page_numbers_to': 'Till:',
        'page_numbers_progress': 'Infogar sidnummer...',
        'page_numbers_start': 'Startar infogning av sidnummer...',
        'page_numbers_cancel': 'Infogning av sidnummer avbruten',
        'page_numbers_success': 'Sidnummer har lagts till.\n\nVill du öppna den nya PDF-filen?\n\n{0}',
        'page_numbers_complete': 'Sidnummer har lagts till',
        'page_numbers_error_format': 'Fel vid infogning av sidnummer: {0}',
        'page_numbers_content_type': 'Innehållstyp:',
        'page_numbers_tab_simple': 'Enkelt nummer',
        'page_numbers_tab_range': 'Sida X av Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Fri text',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Sida {aktuell} av {gesamt}',
        'page_numbers_range_custom': 'Anpassad',
        'page_numbers_range_placeholder': 't.ex. "Sida {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Datumformat:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 januari 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Anpassad',
        'page_numbers_date_placeholder': 't.ex. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Position:',
        'page_numbers_date_before': 'Datum före sidnummer',
        'page_numbers_date_after': 'Datum efter sidnummer',
        'page_numbers_date_only': 'Endast datum (utan sidnummer)',
        'page_numbers_custom_text': 'Anpassad text:',
        'page_numbers_custom_placeholder_text': 'Använd {seite} för sidnummer och {gesamt} för totalt antal\nt.ex. "Sekretess - Sida {seite}" eller "{seite} av {gesamt}"',
        "filename_with_page_number":"_med_sidnummer",
        "filename_with_page_declaration":"_med_sidangivelse",
        "filename_with_pagenumber":"_med_sidnummer",
        "filename_with_date":"_med_datum",
        "filename_with_my_page_declaration":"_med_egen_sidangivelse",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Ej sparade ändringar",
        "unsaved_changes_message_darkmode": "Det finns ej sparade infogningar.\nVill du spara dem innan du växlar?",
        "save_and_switch": "Spara och växla",
        "discard_and_switch": "Växla nu",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Exportera sidor som bilder',
        'export_images_menu': 'Exportera som bilder (PNG/JPEG)',
        'export_images_format': 'Bildformat:',
        'export_images_dpi': 'Upplösning (DPI):',
        'export_images_quality': 'JPEG-kvalitet:',
        'export_images_range': 'Sidintervall:',
        'export_images_all_pages': 'Alla sidor',
        'export_images_custom_range': 'Anpassat intervall',
        'export_images_from': 'Från:',
        'export_images_to': 'Till:',
        'export_images_options': 'Alternativ:',
        'export_images_single_files': 'Varje sida som separat fil',
        'export_images_subfolder': 'Exportera till undermapp',
        'export_images_subfolder_info': 'Till undermappen "PDFnamn_bilder"',
        'export_images_same_folder': 'I samma mapp som PDF-filen',
        'export_images_apply_darkmode': 'Applicera PDFDarkView-inställningar (Mörkt läge)',
        'export_images_target_folder': 'Målmapp:',
        'export_images_browse': 'Bläddra...',
        'export_images_preview': 'Förhandsgranskning:',
        'export_images_preview_info': 'Välj inställningar för export',
        'export_images_preview_info_detail': '{0} sidor som {1}\nUpplösning: {2} DPI\nFilnamn: {3}\n{4}',
        'export_images_select_folder': 'Välj målmapp',
        'export_images_start': 'Startar bildexport...',
        'export_images_progress': 'Exporterar bilder...',
        'export_images_saving': 'Sparar sida {0} av {1}...',
        'export_images_success': 'Export lyckades!\n\n{0} bilder har sparats i:\n{1}',
        'export_images_complete': 'Bildexport slutförd',
        'export_images_open_folder': '📁 Öppna mapp',
        'export_images_cancel': 'Bildexport avbruten',
        'export_images_error_format': 'Fel vid export av bilder: {0}',
        'export_images_pdf2image_missing': 'Biblioteket "pdf2image" är inte installerat.\n\nInstallera det med:\npip install pdf2image\n\nFör Windows behöver du även Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A-konvertering för långtidsarkivering',
        'pdfa_menu': 'PDF/A-konvertering (arkivredo)',
        'pdfa_info': 'Konverterar PDF-filen till PDF/A-format.\n\nPDF/A är speciellt utvecklat för långtidsarkivering och säkerställer att dokumentet visas korrekt i framtiden.',
        'pdfa_standard': 'PDF/A-standard:',
        'pdfa_standard_select': 'Version:',
        'pdfa_1': 'PDF/A-1 (enkel, brett kompatibel)',
        'pdfa_2': 'PDF/A-2 (modern, bättre komprimering)',
        'pdfa_3': 'PDF/A-3 (senaste versionen, tillåter bilagor)',
        'pdfa_standards_explanation': '📖 Förklaring av standarder:\n\n'
            '• PDF/A-1: Grundläggande, kompatibel med äldre system (ca 2005)\n'
            '• PDF/A-2: Mer modern, bättre komprimering, transparensstöd (ca 2011)\n'
            '• PDF/A-3: Senaste versionen, tillåter inbäddning av bilagor (ca 2013)\n\n'
            'Rekommendation: PDF/A-2 är en bra kompromiss mellan kompatibilitet och moderna funktioner.',
        'pdfa_options': 'Alternativ:',
        'pdfa_compress_enable': 'Komprimera PDF (mindre fil)',
        'pdfa_metadata_preserve': 'Bevara metadata (titel, författare, etc.)',
        'pdfa_target_folder': 'Målmapp:',
        'pdfa_browse': 'Bläddra...',
        'pdfa_select_folder': 'Välj målmapp',
        'pdfa_ocr_info_unknown': '🔍 Kunde inte kontrollera textinnehållet.',
        'pdfa_ocr_info_not_needed': '✅ Text tillgänglig - OCR krävs inte.\nPDF/A kan skapas direkt.',
        'pdfa_ocr_info_recommended': '⚠️ Ingen tillräcklig text hittades.\n\nFör sökbara PDF rekommenderar vi att du kör OCR först.\nObs: PDF/A fungerar utan OCR - men texten blir inte sökbar.',
        'pdfa_ocr_info_error': '❌ Fel vid kontroll: {0}',
        'pdfa_start': 'Startar PDF/A-konvertering...',
        'pdfa_progress': 'PDF/A-konvertering pågår...',
        'pdfa_success': 'PDF/A-konvertering lyckades!\n\nSparad som:\n{0}\n\nVill du öppna den nya PDF-filen?',
        'pdfa_complete': 'PDF/A-konvertering slutförd',
        'pdfa_cancel': 'PDF/A-konvertering avbruten',
        'pdfa_error_format': 'Fel under PDF/A-konvertering:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Biblioteket "ocrmypdf" är inte installerat.\n\nInstallera det med:\npip install ocrmypdf',
        'btn_convert': 'Konvertera',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimera PDF (minska filstorlek)',
        'optimize_menu': 'Optimera PDF (filstorlek)',
        'optimize_info': 'Minskar filstorleken på PDF-filen genom olika optimeringsmetoder.\n\nJu högre komprimeringsnivå, desto mindre blir filen - med eventuell kvalitetsförlust i bilder.',
        'optimize_level': 'Komprimeringsnivå:',
        'optimize_level_low': 'Låg (snabb, liten besparing)',
        'optimize_level_medium': 'Medel (bra kompromiss)',
        'optimize_level_high': 'Hög (stor besparing)',
        'optimize_level_maximum': 'Maximum (maximal besparing, långsam)',
        'optimize_level_explanation': 'Rekommendation: "Medel" är en bra kompromiss mellan hastighet och filstorlek.',
        'optimize_options': 'Alternativ:',
        'optimize_compress_images': 'Komprimera bilder (minska JPEG-kvalitet)',
        'optimize_clean_objects': 'Ta bort oanvända objekt',
        'optimize_preserve_metadata': 'Bevara metadata (titel, författare, etc.)',
        'optimize_image_quality': 'Bildkvalitet:',
        'optimize_range': 'Sidintervall:',
        'optimize_all_pages': 'Alla sidor',
        'optimize_custom_range': 'Anpassat intervall',
        'optimize_from': 'Från:',
        'optimize_to': 'Till:',
        'optimize_target_folder': 'Målmapp:',
        'optimize_browse': 'Bläddra...',
        'optimize_select_folder': 'Välj målmapp',
        'optimize_info_box': 'Information',
        'optimize_info_text': 'Optimering kan ta flera minuter för stora PDF-filer.\n\nBilder sparas med reducerad kvalitet, vilket kan minska filstorleken avsevärt.',
        'optimize_start': 'Startar PDF-optimering...',
        'optimize_progress': 'Optimerar PDF...',
        'optimize_cancel': 'PDF-optimering avbruten',
        'optimize_complete': 'PDF-optimering slutförd',
        'optimize_error_format': 'Fel under PDF-optimering:\n\n{0}',
        'optimize_success_message': 'PDF-optimering lyckades!\n\nSparad som:\n{0}\n\nFöre: {1}\nEfter: {2}\nBesparing: {3:.1f}%\n\n{4}\n\nVill du öppna den optimerade PDF-filen?',
        'optimize_success_message_no_size': 'PDF-optimering lyckades!\n\nSparad som:\n{0}\n\nStorleksinformation ej tillgänglig.\n\nVill du öppna den optimerade PDF-filen?',
        'optimize_result_positive': 'Filen minskades med {0:.1f}%.',
        'optimize_result_zero': 'Ingen förändring av filstorlek.',
        'optimize_result_negative': 'Filen har ökat med {0:.1f}%.\nOptimering hoppades över, den ursprungliga filen bevarades.',
        'btn_optimize': 'Starta optimering',
        'filename_optimize_low_suffix': '_optimerad_lag',
        'filename_optimize_medium_suffix': '_optimerad',
        'filename_optimize_high_suffix': '_optimerad_hog',
        'filename_optimize_maximum_suffix': '_optimerad_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Beskär PDF',
        'crop_menu': 'Beskär PDF (Crop)',
        'crop_range': 'Applicera på:',
        'crop_all_pages': 'Alla sidor',
        'crop_current_page': 'Endast aktuell sida',
        'crop_values': 'Beskärningsvärden (i punkter):',
        'crop_left': 'Vänster:',
        'crop_right': 'Höger:',
        'crop_top': 'Topp:',
        'crop_bottom': 'Botten:',
        'crop_presets': 'Förinställningar:',
        'crop_preset_white': 'Upptäck vita marginaler',
        'crop_reset': 'Återställ',
        'crop_mouse_hint': '🖱️ Dra en rektangel för att grovt välja området.\nDärefter kan du justera värdena exakt i SpinBoxarna.\nManuell justering med musen är inte möjlig.',
        'crop_apply': 'Beskär',
        'crop_scope_all': 'Alla sidor',
        'crop_scope_current': 'Aktuell sida',
        'crop_new_size': 'Ny storlek: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Ingen PDF laddad',
        'crop_preview_error': 'Fel vid laddning av förhandsgranskning',
        'crop_start': 'Startar beskärning...',
        'crop_progress': 'Beskär PDF...',
        'crop_success': 'PDF beskuren!\n\nSparad som:\n{0}\n\nVill du öppna den beskurna PDF-filen?',
        'crop_complete': 'Beskärning slutförd',
        'crop_cancel': 'Beskärning avbruten',
        'crop_error_format': 'Fel vid beskärning:\n\n{0}',
        'filename_crop_suffix': '_beskuren',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Platta ut PDF (Flatten)',
        'flatten_menu': 'Platta ut PDF (Flatten)',
        'flatten_info': 'Att platta ut en PDF "bränner in" alla redigerbara element i sidinnehållet.\n\nEfter detta är formulärfält, anteckningar, texter, kryss, signaturer, bilder och former inte längre individuellt redigerbara.',
        'flatten_explanation_title': '📖 Vad är detta bra för?',
        'flatten_explanation_text': 'Utplattning är nödvändig i följande situationer:\n\n'
            '• 📄 Du vill förbereda dokumentet för utskrift\n'
            '• 🔒 Du vill förhindra att någon ändrar formulärfält\n'
            '• 📎 Du vill "permanent" bädda in anteckningar och kommentarer i dokumentet\n'
            '• 🖼️ Du vill permanent förankra infogade texter, kryss, signaturer, bilder och former i dokumentet\n'
            '• 📦 Du vill förbereda filen för arkivering\n\n'
            'Utplattning gör PDF-filen mindre och förhindrar att element flyttas eller raderas av misstag.',
        'flatten_what_title': 'Vad plattas ut?',
        'flatten_what_list': '• ✅ Formulärfält (textfält, kryssrutor, knappar)\n'
            '• ✅ Anteckningar (kommentarer, markeringar, noteringar)\n'
            '• ✅ Överlagringar (texter, kryss, signaturer, bilder, former)',
        'flatten_options': 'Alternativ:',
        'flatten_forms': 'Platta ut formulärfält',
        'flatten_annotations': 'Platta ut anteckningar',
        'flatten_overlays': 'Platta ut överlagringar (texter, kryss, signaturer, bilder, former)',
        'flatten_target_folder': 'Målmapp:',
        'flatten_browse': 'Bläddra...',
        'flatten_select_folder': 'Välj målmapp',
        'flatten_warning': '⚠️ Viktigt: Utplattning är en irreversibel process!\n\nEfter utplattning kan redigerbara element inte längre ändras eller raderas individuellt.\nSkapa en säkerhetskopia i förväg om det behövs.',
        'flatten_apply': 'Platta ut',
        'flatten_start': 'Startar utplattning...',
        'flatten_progress': 'Plattar ut PDF...',
        'flatten_success': 'PDF utplattad!\n\nSparad som:\n{0}\n\nVill du öppna den utplattade PDF-filen?',
        'flatten_complete': 'Utplattning slutförd',
        'flatten_cancel': 'Utplattning avbruten',
        'flatten_error_format': 'Fel vid utplattning:\n\n{0}',
        'filename_flatten_suffix': '_utplattad',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF-överlagring (Overlay)',
        'overlay_menu': 'PDF-överlagring (Overlay)',
        'overlay_info': 'Placerar en PDF (överlagring) ovanpå en annan PDF.\n\nÖverlagrings-PDF:en placeras på bas-PDF:en. Detta är användbart för vattenstämplar, logotyper, brevhuvuden eller stämplar.',
        'overlay_explanation_title': '📖 Vad är detta bra för?',
        'overlay_explanation_text': 'Överlagring är nödvändig i följande situationer:\n\n'
            '• 🏢 Placera ett företagslogotyp som vattenstämpel på varje sida\n'
            '• 📄 Placera ett brevhuvud på en tom PDF\n'
            '• 🖊️ Placera en stämpelöverlagring på ett dokument\n'
            '• 🔖 Placera en vattenstämpel på alla sidor\n'
            '• 📑 Placera en formuläröverlagring på en mall',
        'overlay_type': 'Överlagringstyp:',
        'overlay_type_fullpage': 'Helsida (täckande)',
        'overlay_type_transparent': 'Helsida (transparent - rekommenderas)',
        'overlay_type_stamp': 'Stämpel (positionerbar)',
        'overlay_type_info_fullpage': '📄 Överlagrings-PDF:en placeras exakt över hela sidan.\nDen vita bakgrunden kan tas bort så att endast innehållet syns.',
        'overlay_type_info_transparent': '🔍 Överlagrings-PDF:en placeras över hela sidan med transparent bakgrund.\nDen vita bakgrunden tas bort automatiskt - idealiskt för vattenstämplar och logotyper!',
        'overlay_type_info_stamp': '🖊️ Överlagrings-PDF:en positioneras och skalas som en stämpel.\nPerfekt för logotyper, stämplar eller signaturer på specifika positioner.',
        'overlay_remove_background': 'Ta bort vit bakgrund:',
        'overlay_remove_background_enable': 'Ta bort vit bakgrund från överlagrings-PDF:en (gör överlagringen transparent)',
        'overlay_remove_background_tooltip': 'Tar bort vita områden från överlagrings-PDF:en så att den underliggande texten blir synlig.',
        'overlay_threshold': 'Tröskelvärde:',
        'overlay_threshold_hint': '(1-254, högre = mer vitt tas bort)',
        'overlay_select_file': 'Välj överlagrings-PDF:',
        'overlay_file_placeholder': 'Välj en PDF-fil för överlagringen',
        'overlay_browse': 'Bläddra...',
        'overlay_select_overlay': 'Välj överlagrings-PDF',
        'overlay_range': 'Sidintervall:',
        'overlay_all_pages': 'Alla sidor',
        'overlay_custom_range': 'Anpassat intervall',
        'overlay_from': 'Från:',
        'overlay_to': 'Till:',
        'overlay_position': 'Position:',
        'overlay_position_center': 'Mitten',
        'overlay_position_top_left': 'Uppe vänster',
        'overlay_position_top_right': 'Uppe höger',
        'overlay_position_bottom_left': 'Nere vänster',
        'overlay_position_bottom_right': 'Nere höger',
        'overlay_size': 'Storlek:',
        'overlay_size_original': 'Ursprunglig storlek',
        'overlay_size_fit_page': 'Anpassa till sida',
        'overlay_size_custom': 'Anpassad (%)',
        'overlay_opacity': 'Transparens:',
        'overlay_target_folder': 'Målmapp:',
        'overlay_browse_folder': 'Bläddra...',
        'overlay_select_folder': 'Välj målmapp',
        'overlay_warning': '⚠️ Observera: Överlagrings-PDF:en placeras på bas-PDF:en och "bränns in" i den.\n\nElementen i överlagrings-PDF:en kan inte längre redigeras individuellt efter sparande.',
        'overlay_apply': 'Överlagra',
        'overlay_start': 'Startar överlagring...',
        'overlay_progress': 'Överlagrar PDF...',
        'overlay_success': 'PDF överlagrad!\n\nSparad som:\n{0}\n\nVill du öppna den överlagrade PDF-filen?',
        'overlay_complete': 'Överlagring slutförd',
        'overlay_cancel': 'Överlagring avbruten',
        'overlay_error_format': 'Fel vid överlagring:\n\n{0}',
        'overlay_no_file': 'Ingen överlagrings-PDF vald.\n\nVälj en PDF-fil för överlagring.',
        'filename_overlay_suffix': '_överlagrad',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extrahera bilder från PDF',
        'extract_images_menu': 'Extrahera alla bilder',
        'extract_images_info': 'Extraherar alla bilder från PDF-filen och sparar dem som separata filer.\n\nBilderna sparas i sitt ursprungliga format eller konverteras till ett valt format.',
        'extract_images_format': 'Bildformat:',
        'extract_images_quality': 'JPEG-kvalitet:',
        'extract_images_options': 'Alternativ:',
        'extract_images_subfolder': 'Extrahera till undermapp ("PDFnamn_bilder")',
        'extract_images_unique': 'Endast unika bilder (undvik dubbletter)',
        'extract_images_range': 'Sidintervall:',
        'extract_images_all_pages': 'Alla sidor',
        'extract_images_custom_range': 'Anpassat intervall',
        'extract_images_from': 'Från:',
        'extract_images_to': 'Till:',
        'extract_images_target_folder': 'Målmapp:',
        'extract_images_browse': 'Bläddra...',
        'extract_images_select_folder': 'Välj målmapp',
        'extract_images_info_box': 'Information',
        'extract_images_info_text': 'Extrahering kan ta flera minuter för stora PDF-filer.\n\nBilder sparas med sitt ursprungliga namn (sida_bild).',
        'extract_images_extract': 'Extrahera',
        'extract_images_start': 'Startar extrahering...',
        'extract_images_progress': 'Extraherar bilder...',
        'extract_images_success': '✅ Bilder extraherade!\n\n{0} bilder har sparats i:\n{1}',
        'extract_images_complete': 'Bildextrahering slutförd',
        'extract_images_cancel': 'Extrahering avbruten',
        'extract_images_error_format': 'Fel vid extrahering av bilder:\n\n{0}',
        'extract_images_open_folder': '📁 Öppna mapp',
        'extract_images_no_images': 'Inga bilder hittades i PDF-filen.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Flera sidor på en sida (N-Up)',
        'nup_menu': 'Flera sidor på en sida (N-Up)',
        'nup_info': 'Arrangerar flera PDF-sidor på en sida.\n\nIdealiskt för kompakta utskrifter, översikter eller handouts.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Förhandsgranskning:',
        'nup_preview_info': '{0} sidor → {1} sidor per ark → {2} ark\nLayout: {3}',
        'nup_order': 'Ordning:',
        'nup_order_horizontal': 'Horisontell (rad för rad)',
        'nup_order_vertical': 'Vertikal (kolumn för kolumn)',
        'nup_order_horizontal_reverse': 'Horisontell omvänd',
        'nup_order_vertical_reverse': 'Vertikal omvänd',
        'nup_range': 'Sidintervall:',
        'nup_all_pages': 'Alla sidor',
        'nup_custom_range': 'Anpassat intervall',
        'nup_from': 'Från:',
        'nup_to': 'Till:',
        'nup_options': 'Alternativ:',
        'nup_margins': 'Marginaler:',
        'nup_margin_between': 'Avstånd mellan sidor:',
        'nup_page_numbers': 'Infoga sidnummer',
        'nup_target_folder': 'Målmapp:',
        'nup_browse': 'Bläddra...',
        'nup_select_folder': 'Välj målmapp',
        'nup_create': 'Skapa',
        'nup_start': 'Startar N-Up...',
        'nup_progress': 'Skapar N-Up...',
        'nup_success': 'N-Up skapad!\n\nSparad som:\n{0}\n\nVill du öppna den nya PDF-filen?',
        'nup_complete': 'N-Up slutförd',
        'nup_cancel': 'N-Up avbruten',
        'nup_error_format': 'Fel vid N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Ändra sidstorlek',
        'pagesize_menu': 'Ändra sidstorlek',
        'pagesize_info': 'Ändrar sidstorleken på PDF-filen.\n\nInnehållet anpassas automatiskt till den nya storleken.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Välj ett standardformat:',
        'pagesize_custom': 'Anpassad storlek:',
        'pagesize_width': 'Bredd:',
        'pagesize_height': 'Höjd:',
        'pagesize_orientation': 'Orientering:',
        'pagesize_portrait': 'Stående',
        'pagesize_landscape': 'Liggande',
        'pagesize_scale_options': 'Skalningsalternativ:',
        'pagesize_fit': 'Anpassa (behåll bildförhållande)',
        'pagesize_stretch': 'Tänj (förvräng)',
        'pagesize_center': 'Centrera (ursprunglig storlek)',
        'pagesize_range': 'Sidintervall:',
        'pagesize_all_pages': 'Alla sidor',
        'pagesize_custom_range': 'Anpassat intervall',
        'pagesize_from': 'Från:',
        'pagesize_to': 'Till:',
        'pagesize_target_folder': 'Målmapp:',
        'pagesize_browse': 'Bläddra...',
        'pagesize_select_folder': 'Välj målmapp',
        'pagesize_apply': 'Applicera',
        'pagesize_start': 'Startar ändring av sidstorlek...',
        'pagesize_progress': 'Ändrar sidstorlek...',
        'pagesize_success': 'Sidstorlek ändrad!\n\nSparad som:\n{0}\n\nVill du öppna den nya PDF-filen?',
        'pagesize_complete': 'Ändring av sidstorlek slutförd',
        'pagesize_cancel': 'Ändring av sidstorlek avbruten',
        'pagesize_error_format': 'Fel vid ändring av sidstorlek:\n\n{0}',
        'pagesize_preview_info': 'Ny storlek: {0} x {1} pt',
        'filename_pagesize_suffix': '_ny_storlek',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-information',
        'pdf_info_menu': 'Visa PDF-info',
        'pdf_info_voice': 'Visar PDF-information',
        'pdf_info_error': 'Fel vid visning av PDF-info:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Visa tangentbordsgenvägar",
        "shortcuts_dialog_title": "Tangentbordsgenvägar",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FIL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Öppna PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Stäng PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Spara som...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Skydda dokument</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Skriv ut</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Skriv ut omedelbart (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Avsluta applikationen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORTERA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exportera som Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exportera som DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exportera som TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exportera som bilder (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extrahera bilder</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTBEHANDLING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Flera sidor)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A-konvertering (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Platta ut PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Överlagra PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimera PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDIGERA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Sök</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Lägg till bokmärke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Hantera bokmärken</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Nästa bokmärke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Föregående bokmärke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Kör OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SIDADMINISTRATION</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rotera aktuell sida</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rotera alla sidor</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalisera aktuell sida</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalisera alla sidor</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Ta bort sidor</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extrahera sidor</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Infoga sidor</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Flytta sidor</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Sammanfoga PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Ändra sidstorlek</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INFOGA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Infoga text</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Infoga kryss</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Infoga signatur 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Infoga signatur 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Infoga bild</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Infoga rektangel</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Infoga ellips</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Infoga linje</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Infoga pil</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Infoga sidnummer</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Text-vattenstämpel</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Bild-vattenstämpel</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ RADERINGSMARKERINGAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Raderingsmarkering (svart)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Raderingsmarkering (vit)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Applicera alla raderingsmarkeringar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ AVANCERAT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Beskär PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Redigera metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VISA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Växla Mörkt/Ljust läge</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Visa textfönster</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Sidbredd (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Två sidor (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Översikt (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ INSTÄLLNINGAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Lösenordshantering</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR-inställningar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Signaturinställningar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Filnamnsformatering</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Exportera inställningar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importera inställningar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Visa PDF-info</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Slå på/av talutmatning</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokusera menyrad</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Ny version tillgänglig",
        "update_available_message": "Det finns en ny version <b>{0}</b>.\n\nBesök releasesidan för att ladda ner uppdateringen:\n{1}",
        "update_available_voice": "Ny version {0} tillgänglig. Ladda ner uppdateringen från GitHub-sidan.",
        "update_open_release": "Öppna releasesida",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Ladda ner alla översättningar",
        "ask_download_all_translations": """Förutom tyska, engelska och vietnamesiska finns det {total_languages} andra GUI-språk tillgängliga.\n\nSka dessa tillhandahållas / uppdateras?\n\nObs:\nOnödiga språk kan du senare manuellt ta bort i katalogen:\n{translations_path}
        \nOm du avbryter kan du ladda ner GUI-språken senare via menyn 'Verktyg → Uppdatera översättningar'.""",
        "menu_update_translations": "Uppdatera översättningar",
        "translations_updated": "Översättningar uppdaterade",
        "translations_update_success": "{} översättningar uppdaterades ({} nya, {} uppdaterade).",
        "translations_update_error": "Fel vid uppdatering av översättningar",
        "translations_update_no_changes": "Alla översättningar är redan uppdaterade.",
        "translations_update_offline": "Ingen internetanslutning. Översättningar kunde inte uppdateras.",
        "translations_update_in_progress": "Översättningar uppdateras i bakgrunden...",
        "translations_downloading": "Laddar ner översättningar...",
        "translations_path_hint": "Användarkatalog för översättningar",
        "translations_update_not_available_title": "Uppdatering inte tillgänglig",
        "translations_update_not_available_message": """Uppdatering av översättningar är endast tillgänglig i den installerade versionen.\n\nI utvecklingsläge är översättningarna redan uppdaterade.""",
        "translations_update_no_internet_title": "Ingen internetanslutning",
        "translations_update_no_internet_message": """Kunde inte upprätta internetanslutning.\n\nÖversättningar kan inte laddas ner från GitHub.\n\nMöjliga lösningar:
        • Kontrollera din internetanslutning
        • Inaktivera eventuell brandvägg tillfälligt
        • Försök igen senare
        \nDu kan även ladda ner översättningarna manuellt från GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Uppdatering pågår redan",
        "btn_retry": "Försök igen",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Välkommen till PDF Dark View",
        "welcome_title_not_supported": "Välkommen till PDF Dark View",
        "welcome_message": "Välkommen till PDF Dark View!\n\nDitt systemspråk upptäcktes som '{language}'.\nVill du använda detta språk för användargränssnittet?\n\nDu kan när som helst ändra språket via 'Inställningar → Språk'.",
        "welcome_message_language_not_available": "Välkommen till PDF Dark View!\n\nDitt systemspråk upptäcktes som '{language}'.\nDetta språk är ännu inte installerat.\n\nVill du ladda ner översättningarna för {language} nu från GitHub?\n\n(Språket kommer sedan automatiskt att användas för användargränssnittet.)",
        "welcome_message_language_not_supported": "Välkommen till PDF Dark View!\n\nDitt systemspråk upptäcktes som '{language}'.\nTyvärr finns det inga översättningar för detta språk ännu.\n\nAnvändargränssnittet kommer att visas på {fallback_language}.\n\nDu kan när som helst ändra språket via 'Inställningar → Språk'.\nOm du vill kan du också bidra med en översättning för ditt språk:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Ja, använd systemspråk",
        "welcome_keep_english": "Nej, behåll engelska",
        "welcome_download_language": "Ja, ladda ner {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programmet avslutas",

    }

