
# ============================================
# translations_af.py - Afrikaanse woordeboek
# Vollständig sortiert nach Kategorien
# ============================================

def load_afrikaans_strings():
    """Lädt alle afrikaansen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View deur BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Laai PDF",
        'btn_text_window': "OCR-teks",
        'btn_first': "Eerste bladsy",
        'btn_prev': "Vorige bladsy",
        'btn_next': "Volgende bladsy",
        'btn_last': "Laaste bladsy",
        'btn_print': "Druk",
        'btn_darkmode_light': "Ligte modus",
        'btn_darkmode_dark': "Donker modus",
        'btn_delete_pages': "Verwyder bladsye",
        'btn_extract_pages': "Onttrek bladsye",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Kanselleer",
        'btn_save': "Stoor",
        'btn_close': "Sluit",
        'btn_delete': "Verwyder",
        'btn_delete_all': "Verwyder alles",
        'btn_copy': "Kopieer",
        'btn_export': "Uitvoer",
        'btn_show': "Wys wagwoord",
        'btn_hide': "Versteek wagwoord",
        'btn_authenticate': "Staatmaak",
        'btn_settings': "Instellings",
        'btn_protect': "Beskerm",
        'btn_remove_password': "Verwyder wagwoord",
        'btn_manage': "Wagwoordbestuur",
        'btn_retry': "Probeer weer",
        'btn_select_all': "Kies alles",
        'btn_clear_selection': "Maak keuse skoon",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Bladsy {0} van {1}",
        'page_count': "van {0}",
        'goto_page': "Gaan na bladsy",
        'page_simple': "Bladsy {0}",
        'full_view_page': "Volle aansig bladsy {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Voer soekterm in + Enter",
        'search_results': "Resultate: {0} van {1}",
        'search_nav_hint': "Enter: volgende (Shift+Enter: vorige) resultaat",
        'search_no_results': "Geen resultate",
        'search_error': "Soekfout",
        'search_active': "Soekveld geaktiveer",
        'search_closed': "Soek beëindig",
        'search_position': "Bladsy {0} {1}",
        'search_pos_top': "heel bo",
        'search_pos_upper': "bo",
        'search_pos_middle': "middel",
        'search_pos_lower': "onder",
        'search_pos_bottom': "heel onder",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Teksherkenning suksesvol voltooi!",
        'ocr_success_title': "OCR suksesvol",
        'ocr_success_message': "Die dokument is nou deursoekbaar.",
        'ocr_failed': "OCR misluk",
        'ocr_in_progress': "OCR besig",
        'ocr_preparing': "Berei PDF voor...",
        'ocr_analyzing': "Ontleed PDF...",
        'ocr_optimizing': "Beeldoptimalisering besig...",
        'ocr_recognizing': "Teksherkenning besig...",
        'ocr_embedding': "Voeg teks in...",
        'ocr_finalizing': "Finaliseer PDF...",
        'ocr_not_available': "OCR nie beskikbaar nie",
        'ocr_install_message': "OCR-nutsmiddels is nie gevind nie.\n\nInstalleer asseblief:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR vereis",
        'ocr_question': "Die PDF bevat geen deursoekbare teks nie.\nWil u OCR uitvoer om {0} moontlik te maak?",
        'ocr_perform': "Voer OCR uit",
        'ocr_later': "Later",
        'ocr_starting': "Begin gewaarborgde OCR...",
        'ocr_success_voice': "OCR suksesvol. PDF is nou deursoekbaar.",
        'ocr_partial_success': "OCR is uitgevoer, maar daar was probleme met vervanging.\n\nDie deursoekbare weergawe is gestoor onder:\n{0}\n\nFout: {1}",
        'ocr_partial_title': "OCR gedeeltelik suksesvol",
        'ocr_partial_voice': "OCR uitgevoer, maar vervanging misluk.",
        'original_file': "Oorspronklike lêer:",
        'old_size': "Ou grootte:    {0} grepe",
        'new_size': "Nuwe grootte: {0} grepe",
        'size_change': "Verandering: {0}{1} grepe",
        'backup_created_file': "Rugsteun geskep:\n{0}",
        'backup_not_created': "Rugsteun nie geskep nie (instelling afgeskakel)",
        'page_header': "=== Bladsy {0} ===\n{1}\n",
        'scanned_page_header': "=== Bladsy {0} (geskandeer) ===\n[Dié bladsy bevat slegs geskandeerde teks]\n[Voer asseblief OCR met die hand uit]\n",
        'scanned_warning': "⚠️ GESKANDEERDE TEKS - OCR VEREIS",
        'guaranteed_title': "Deursoekbare PDF geskep",
        'guaranteed_message': "<b>Gewaarborgde deursoekbare weergawe geskep!</b>\n\nAangesien die outomatiese OCR misluk het, is 'n alternatiewe deursoekbare PDF geskep:\n\n{0}\n\n<b>Dié lêer bevat:</b>\n• Onttrekte teks (indien teenwoordig)\n• Wenke vir geskandeerde bladsye\n• Is ten volle deursoekbaar",
        'guaranteed_voice': "Gewaarborgde deursoekbare PDF geskep.",
        'instruction_title': "OCR-INSTRUKSIES",
        'instruction_file': "Oorspronklike lêer: {0}",
        'instruction_text': "Die outomatiese teksherkenning (OCR) het misluk.\nVoer OCR met die hand uit:\n\n1. MET OCRmyPDF (opdragreël):\n   ocrmypdf --force-ocr \"[LÊER]\" \"uitvoer.pdf\"\n\n2. MET ADOBE ACROBAT (macOS/Windows):\n   • Maak PDF in Acrobat oop\n   • Gereedskap > Wysig PDF\n   • Kies 'Teksherkenning'\n\n3. MET PREVIEW (macOS):\n   • Maak PDF in Voorskou oop\n   • Lêer > Voer uit...\n   • Quartz-filter: 'Verklein lêergrootte'\n   • Aktiveer 'Voer OCR uit'\n\n4. AANLYN OCR-DIENSTE:\n   • smallpdf.com/af/ocr-pdf\n   • ilovepdf.com/af/ocr-pdf\n   • adobe.com/af/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR-instruksies geskep",
        'instruction_created_message': "'n Gedetailleerde instruksie is geskep:\n\n{0}\n\nVolg die stappe vir handmatige OCR.",
        'instruction_created_voice': "OCR-instruksies geskep.",
        'ocr_impossible': "OCR nie moontlik nie",
        'ocr_impossible_message': "OCR kon nie uitgevoer word nie.\n\nVerwerk '{0}' met die hand met OCR-sagteware.",
        'ocr_impossible_voice': "OCR nie moontlik nie. Verwerk asseblief met die hand.",
        'emergency_title': "Nood-OCR",
        'emergency_message': "'n Nood-PDF is geskep:\n\n{0}\n\nVerwerk dié lêer met die hand met OCR.",
        'emergency_voice': "Nood-PDF geskep. Voer asseblief OCR met die hand uit.",
        'critical_error': "Kritiese fout",
        'critical_error_message': "OCR kon nie begin word nie.\n\nBegin die program weer en kontroleer die OCR-installasie.",
        'critical_error_voice': "Kritiese OCR-fout",
        'ocr_question_html': "<p>Die PDF bevat geen deursoekbare teks nie.<p>Wil u OCR uitvoer om <b>{0}</b> moontlik te maak?</p>",
        'ocr_question_voice': "OCR vereis. Die PDF bevat geen deursoekbare teks nie. Wil u OCR uitvoer om {0} moontlik te maak?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "geen PDF gelaai nie",
        'no_pdf_message': "Geen PDF is gelaai nie",
        'pdf_not_found': "PDF-lêer nie gevind nie",
        'file_size': "Lêergrootte",
        'bytes': "grepe",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Rugsteun geskep",
        'backup_disabled': "Rugsteun afgeskakel",
        'backup_activated': "Rugsteun skepping geaktiveer",
        'backup_deactivated': "Rugsteun skepping gedeaktiveer",
        'backup_status': "Rugsteun: {0}",
        'backup_on': "✔ geaktiveer",
        'backup_off': "✘ gedeaktiveer",
        'close_pdf': "Sluit PDF: {0}",
        'pdf_not_found_format': "PDF-lêer nie gevind nie: {0}",
        'error_pdf_load_format': "Fout met laai van PDF: {0}",
        'load_failed_format': "Laai misluk:\n{0}",
        'decrypted_suffix': "(ontsleutel)",
        'decryption_failed': "Ontsleuteling misluk.",
        'decryption_error': "Fout met ontsleuteling",
        'decryption_success': "Suksesvol ontsleutel",
        'decryption_success_message': "PDF is ontsleutel en gestoor onder:\n\n{0}",
        'decryption_success_voice': "PDF is ontsleutel en gestoor.",
        'password_remove_error': "Fout met verwydering van wagwoord",
        'save_unencrypted': "Stoor onversleutelde PDF as",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Stoor as...",
        'save_copy': "Stoor kopie",
        'save_success': "PDF gestoor onder: {0}",
        'save_encrypted': "Beskermde PDF gestoor onder: {0}",
        'save_error': "PDF kon nie gestoor word nie",
        'encryption_question': "Wil u die PDF met 'n wagwoord beskerm?",
        'encryption_yes': "Ja",
        'encryption_no': "Nee",
        'encryption_cancel': "Kanselleer",
        'save_cancel': "Stoor gekanselleer",
        'save_encrypted_voice': "Lêer versleutel en gestoor.",
        'save_success_voice': "Die PDF-lêer is onversleutel gestoor.",
        'save_error_format': "PDF kon nie gestoor word nie:\n{0}",
        'export_pages_success': "Pages-uitvoer suksesvol",
        'export_pages_error': "Pages-uitvoer misluk",
        'export_pages_error_format': "Pages-uitvoer misluk: {0}",
        'export_word_success': "Word-uitvoer suksesvol",
        'export_word_error': "Word-uitvoer misluk",
        'export_word_error_format': "Word-uitvoer misluk: {0}",
        'export_text_success': "Teksuitvoer suksesvol",
        'export_text_error': "Teksuitvoer misluk",
        'export_text_error_format': "Teksuitvoer misluk: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Wagwoord vereis",
        'password_enter': "Voer asseblief die wagwoord in",
        'password_confirm': "Bevestig wagwoord",
        'password_new': "Nuwe wagwoord",
        'password_current': "Huidige wagwoord",
        'password_save': "Stoor wagwoord (versleutel)",
        'password_saved': "✓ Wagwoord vir dié lêer is gestoor",
        'password_wrong': "Verkeerde wagwoord",
        'password_mismatch': "Wagwoorde stem nie ooreen nie",
        'password_too_short': "Wagwoord te kort",
        'password_min_length': "Die wagwoord moet minstens 4 karakters lank wees",
        'password_strength': "Wagwoordsterkte",
        'password_strength_very_weak': "Baie swak",
        'password_strength_weak': "Swak",
        'password_strength_medium': "Gemiddeld",
        'password_strength_strong': "Sterk",
        'password_strength_very_strong': "Baie sterk",
        'password_char_count': "({0} karakters)",
        'password_match': "✓ Stem ooreen",
        'password_no_match': "✗ Wagwoorde stem nie ooreen nie",
        'password_show': "Wys",
        'password_hide': "Versteek",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Wagwoordbestuur",
        'password_table_filename': "Lêernaam",
        'password_table_password': "Wagwoord",
        'password_count': "{0} gestoorde wagwoord{1}",
        'password_count_singular': "",
        'password_count_plural': "e",
        'password_none': "Geen gestoorde wagwoorde nie",
        'password_copied': "{0} wagwoord{1} gekopieer",
        'password_copied_singular': "",
        'password_copied_plural': "e",
        'password_delete_confirm': "Wil u werklik die wagwoord vir '{0}' verwyder?",
        'password_delete_multiple': "Wil u werklik die {0} geselekteerde wagwoorde verwyder?",
        'password_delete_all_confirm': "Wil u werklik al {0} gestoorde wagwoorde verwyder?",
        'password_deleted': "{0} wagwoord{1} verwyder",
        'password_deleted_singular': "",
        'password_deleted_plural': "e",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Alle wagwoorde is verwyder",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Wagwoordgenerator",
        'generator_generated': "Gegenereerde wagwoord:",
        'generator_regenerate': "Genereer weer",
        'generator_copy': "Kopieer",
        'generator_use': "Gebruik",
        'generator_settings': "Instellings",
        'generator_length': "Lengte:",
        'generator_group_every': "Skeidingsteken elke",
        'generator_group_chars': "karakters.    Skeier:",
        'generator_uppercase': "Hoofletters (A-Z)",
        'generator_lowercase': "Kleinletters (a-z)",
        'generator_digits': "Syfers (0-9)",
        'generator_symbols': "Spesiale karakters (!@#$%^&*)",
        'generator_exclude': "Uitgesluit:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Meesterwagwoord vereis",
        'master_password_setup': "Stel meesterwagwoord op",
        'master_password_change': "Verander meesterwagwoord",
        'master_password_enter': "Voer asseblief u meesterwagwoord in",
        'master_password_choose': "Kies 'n sterk meesterwagwoord (minstens 8 karakters)",
        'master_password_new': "Voer asseblief u nuwe meesterwagwoord in",
        'master_password_confirm': "Bevestig wagwoord",
        'master_password_authenticate': "Staatmaak",
        'master_password_success': "Meesterwagwoord is suksesvol opgestel.",
        'master_password_changed': "Meesterwagwoord is suksesvol verander.",
        'master_password_removed': "Meesterwagwoord en alle wagwoorde is verwyder.",
        'master_password_remove': "Verwyder meesterwagwoord",
        'master_password_remove_confirm': "Is u HEELTEMAL SEKER dat u AL die wagwoorde wil verwyder?\n\nHierdie aksie is ONOMKEERBAAR!",
        'master_password_export_before': "Wil u eers 'n rugsteun uitvoer?",
        'master_password_export_delete': "Voer uit en verwyder",
        'master_password_delete_now': "Verwyder nou",
        'master_password_for_signatures': "Om handtekeninge te kan gebruik, moet u 'n meesterwagwoord opstel.\n\nWil u nou 'n meesterwagwoord opstel?",
        'master_password_for_private': "Om privaat teksblokke te kan gebruik, moet u 'n meesterwagwoord opstel.\n\nWil u nou 'n meesterwagwoord opstel?",
        'master_password_info': """
            <b>🔐 SONDER MEESTERWAGWOORD:</b><br>
            • Geen vertoon, kopiëring en uitvoer van wagwoorde moontlik nie<br>
            • Verwydering van wagwoorde is altyd moontlik (selfs sonder meesterwagwoord)<br><br>

            <b>🔐 MET MEESTERWAGWOORD:</b><br>
            • Alle funksies beskikbaar na staafmaking<br>
            • Wagwoorde word met die meesterwagwoord versleutel<br>
            • Minimum lengte: 8 karakters<br>
            • Veilige SHA-256 hash-berging<br><br>

            <b>BELANGRIK:</b><br>
            • By verlies van die meesterwagwoord: wagwoorde nie herwinbaar nie<br>
            • By verwydering van die meesterwagwoord: AL die wagwoorde word verwyder<br>
            • Uitvoer-opsie beskikbaar voor verwydering<br>
            • Meesterwagwoord kan enige tyd verander word
        """,
        'signature_auth_disabled': "Deaktiveer wagwoordaanvraag vir handtekeninge",
        'template_auth_disabled': "Deaktiveer wagwoordaanvraag vir privaat teksblokke",
        'master_password_for_signatures_settings': "Om handtekeninge te kan gebruik, moet u 'n meesterwagwoord opstel.\n\nGaan na Instellings - Wagwoordbestuur",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Beskerm PDF",
        'protect_info': "Die lêer '{0}' sal met 'n wagwoord beskerm word.",
        'protect_instruction': "Voer asseblief 2 keer die gewenste wagwoord in om die dokument te beskerm, of gebruik die wagwoordgenerator regs van die invoerveld.",
        'protect_success': "PDF is suksesvol beskerm en gestoor onder:\n{0}\n\nWagwoord: {1}\n\nWil u die beskermde PDF nou oopmaak?",
        'protect_open': "Ja",
        'protect_skip': "Nee",
        'protect_error': "Fout met beskerming van PDF",
        'protect_open_title': "beskermde PDF oopmaak",
        'protect_question': "Klaar. Wil u die beskermde PDF nou oopmaak? Ja of Nee?",
        'password_cancel': "Wagwoorddialoog gekanselleer",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Verwyder bladsye",
        'pages_extract': "Onttrek bladsye",
        'pages_insert': "Voeg bladsye in",
        'pages_move': "Skuif bladsye",
        'pages_delete_options': "Verwyderopsies",
        'pages_delete_empty': "Verwyder alle leë bladsye",
        'pages_delete_current': "Verwyder huidige bladsy",
        'pages_delete_range': "Verwyder bladsybereik",
        'pages_extract_options': "Onttrekopsies",
        'pages_extract_current': "Onttrek huidige bladsy",
        'pages_extract_range': "Onttrek bladsybereik",
        'pages_insert_position': "Invoegposisie",
        'pages_insert_before': "Voeg in voor bladsy:",
        'pages_insert_select': "Kies PDF",
        'pages_insert_none': "Geen PDF gekies nie",
        'pages_move_source': "Bladsye om te skuif",
        'pages_move_from': "Van bladsy:",
        'pages_move_to': "Tot bladsy:",
        'pages_move_target': "Teikenposisie",
        'pages_move_before': "Skuif voor bladsy:",
        'pages_move_hint': "Wenk: bladsy 1 = begin, {0} = einde",
        'pages_range_invalid': "Die beginbladsy moet kleiner of gelyk aan die eindbladsy wees.",
        'pages_position_invalid': "Die teikenposisie mag nie binne die te skuif bereik wees nie.",
        'pages_no_pdf_selected': "Geen PDF is gekies nie.",
        'pages_deleted': "{0} bladsye is verwyder.",
        'pages_extracted': "Onttrek: {0}\nGestoor onder: {1}\nLêergrootte: {2:.1f} KB",
        'pages_inserted': "{0} bladsye ingevoeg",
        'pages_moved': "{0} bladsye is geskuif.",
        'pages_deleted_none': "Geen bladsye is verwyder nie.",
        'pages_delete_progress': "Besig om bladsye te verwyder...",
        'pages_deleted_with_backup': "{0} bladsye is verwyder.\n\nRugsteun: {1}",
        'pages_deleted_voice': "'n Rugsteun is geskep en {0} bladsye is verwyder.",
        'info': "Inligting",
        'error_dialog_creation': "Dialoog kon nie geskep word nie",
        'extract_page_single': "Onttrek bladsy {0}",
        'extract_page_range': "Onttrek bladsye {0}-{1}",
        'extract_success_voice': "Bladsye suksesvol onttrek",
        'extract_error_format': "Fout met onttrekking: {0}",
        'pages_inserted_voice': "{0} bladsye is ingevoeg.",
        'insert_error_format': "Fout met invoeging: {0}",
        'pages_move_progress': "Besig om bladsye te skuif...",
        'pages_moved_with_backup': "{0} bladsye is geskuif.\n\nRugsteun: {1}",
        'move_success_title': "Suksesvol geskuif",
        'pages_moved_voice': "{0} bladsye suksesvol geskuif",
        'mark_removed': "Merk van bladsy {0} verwyder",
        'mark_empty': "Bladsy {0} as leeg gemerk",
        'mark_export_removed': "Uitvoermerk van bladsy {0} verwyder",
        'mark_export': "Bladsy {0} vir uitvoer gemerk",
        'no_empty_pages': "Geen leë bladsye gemerk om te verwyder nie",
        'delete_empty_confirm': "Wil u al {0} gemerkte leë bladsye verwyder?",
        'delete_empty_confirm_voice': "Nou al {0} gemerkte leë bladsye verwyder? Ja of Nee.",
        'empty_pages_deleted': "{0} leë bladsye verwyder",
        'no_export_pages': "Geen bladsye vir uitvoer gemerk nie",
        'overwrite_title': "Oorskryf bestaande lêer",
        'overwrite_question': "Die lêer\n\n{0}\n\nbestaan reeds.\nWil u dit oorskryf?",
        'overwrite_voice': "Oorskryf bestaande lêer? Ja of Nee.",
        'page_skipped': "Bladsy {0} is oorgeslaan",
        'export_complete': "Uitvoer voltooi.",
        'export_complete_voice': "Die uitvoer is voltooi.",
        'no_pages_exported': "Geen bladsy uitgevoer nie",
        'export_cancelled': "Uitvoer gekanselleer",
        'pages_exported': "{0} bladsye uitgevoer na {1}",
        'export_page_title': "Voer bladsy uit",
        'page_exported': "Bladsy {0} uitgevoer na {1}",
        'export_error': "Fout met uitvoer",
        'export_marked_title': "Voer gemerkte bladsye uit",
        'rotate_all_title': "draai alle bladsye",
        'rotate_all_question': "Wil u alle bladsye 90 grade na regs draai?",
        'rotate_all_voice': "Wil u alle bladsye 90 grade na regs draai? Ja of Nee?",
        'all_pages_rotated': "Alle bladsye gedraai",
        'page_rotated': "Bladsy {0} gedraai",
        'rotate_error': "Bladsy kon nie gedraai word nie",
        'delete_page_confirm': "Wil u bladsy {0} verwyder?",
        'delete_page_confirm_voice': "Wil u werklik bladsy {0} verwyder? Ja of Nee.",
        'page_deleted': "Bladsy {0} verwyder",
        'delete_error': "Bladsy kon nie verwyder word nie",
        'pages_deleted_voice': "{0} bladsye verwyder",
        'pages_exported_split': "{0} bladsye is suksesvol uitgevoer.",
        'pages_skipped': "{0} bladsye is oorgeslaan.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Onttrek bladsye (gevorderd)",
        'pdf_splitter_title': "PDF Splitter & Onttrekker",
        'pdf_splitter_load': " Kies PDF-lêer",
        'pdf_splitter_info': "Kies asseblief 'n opsie vir u PDF-dokument",
        'pdf_splitter_basic': "Basiese bewerkings",
        'pdf_splitter_single': "Deel op in enkele bladsye",
        'pdf_splitter_range': "Onttrek bladsye:",
        'pdf_splitter_range_placeholder': "bv. 1-3,5,7-9",
        'pdf_splitter_clean': "Skoonmaakbewerkings",
        'pdf_splitter_remove_empty': "Verwyder alle leë bladsye",
        'pdf_splitter_remove': "Verwyder bladsybereik:",
        'pdf_splitter_remove_placeholder': "bv. 2,4-6",
        'pdf_splitter_process': "Verwerk PDF",
        'pdf_splitter_loaded': "PDF gelaai. Kies asseblief 'n opsie",
        'pdf_read_error': "PDF kon nie gelees word nie",
        'pages': "Bladsye",
        'pages_created': "Bladsye is geskep",
        'range_empty': "Voer asseblief 'n bladsybereik in",
        'range_invalid': "Ongeldige bladsybereik",
        'range_created': "Nuwe PDF met die geselekteerde bladsye is geskep:\n{0}",
        'empty_removed': "{0} leë bladsye verwyder.\nUitset: {1}",
        'remove_empty': "Voer asseblief bladsye in om te verwyder",
        'remove_invalid': "Ongeldige bladsye om te verwyder",
        'remove_done': "Skoongemaakte PDF geskep:\n{0}",
        'open_folder': "Maak gids oop",
        'show_in_finder': "Wys in Finder",
        'pdf_splitter_no_pdf': "Laai asseblief eers 'n PDF-lêer.",
        'process_error': "Fout met verwerking van PDF",
        'pages_created_voice': "{0} bladsye is geskep",
        'range_created_voice': "PDF met die geselekteerde bladsye is geskep",
        'empty_removed_voice': "{0} leë bladsye is verwyder",
        'remove_done_voice': "Skoongemaakte PDF is geskep",
        'pdf_splitter_split_groups': "Elke aaneenlopende groep in aparte lêer",
        'range_created_single': "Nuwe PDF geskep:\n{0}",
        'range_created_multiple': "{0} PDF-lêers is geskep.",
        'range_created_voice_single': "Een PDF met die geselekteerde bladsye is geskep",
        'range_created_voice_multiple': "{0} PDF-lêers is geskep",
        'empty_removed_none_left': "Geen bladsye oor nie",
        'empty_removed_all_empty': "Alle bladsye is as leeg herken en sou verwyder word. Geen lêer is geskep nie.",
        'preview_single': "Voorskou: {0}",
        'preview_enter_range': "Voer asseblief 'n bladsybereik in.",
        'preview_invalid_range': "Ongeldige bladsybereik.",
        'preview_file': "Voorskou: {0}",
        'preview_files': "Voorskou: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Begin drukproses",
        'print_sent': "Druktaak gestuur",
        'print_now': "Druk nou",
        'print_error': "Fout met onmiddellike druk",
        'print_limited': "Drukfunksie op hierdie stelsel beperk",
        'print_error_format': "Fout met onmiddellike druk: {0}",
        'warning': "Waarskuwing",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Skakel oor na ligte modus",
        'mode_switch_to_dark': "Skakel oor na donker modus",
        'mode_dark_activated': "Donker modus geaktiveer",
        'mode_light_activated': "Ligte modus geaktiveer",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Volle aansig",
        'zoom_two_pages': "Twee bladsye langs mekaar",
        'zoom_overview': "Oorsigmodus",
        'zoom_cannot_during_search': "Zoom nie moontlik tydens soek nie",
        'zoom_exit_first': "Verlaat eers die zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop geaktiveer",
        'drag_disabled': "Drag & Drop gedeaktiveer",
        'drag_page_grab': "Bladsy {0} gryp",
        'drag_page_dropped': "Bladsy {0} by posisie {1} ingevoeg",
        'drag_position_invalid': "Ongeldige posisie",
        'drag_same_position': "Bladsy {0} bly op posisie {0}",
        'drag_error': "Fout met skuif",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Teksinvoer met uitgebreide formatering en teksblokbestuur",
        'text_templates': "Beskikbare teksblokke:",
        'text_name': "Naam",
        'text_preview': "Teksvoorskou",
        'text_enter': "Teks:",
        'text_font_size': "Lettergrootte:",
        'text_formatting': "Formatering:",
        'text_bold': "Vet",
        'text_italic': "Kursief",
        'text_underline': "Onderstreep",
        'text_alignment': "Belyning:",
        'text_left': "Links",
        'text_center': "Gesentreer",
        'text_right': "Regs",
        'text_color': "Tekskleur:",
        'text_opacity': "Deursigtigheid:",
        'text_word_wrap': "Woordomvou:",
        'text_auto': "Outomaties",
        'text_page_width_95': "Bladsywydte (95%)",
        'text_page_width_85': "Baie wyd (85%)",
        'text_page_width_75': "Wyer (75%)",
        'text_page_width_60': "Wyd (60%)",
        'text_page_width_50': "Medium (50%)",
        'text_page_width_30': "Smal (30%)",
        'text_page_width_20': "Smaller (20%)",
        'text_page_width_10': "Baie smal (10%)",
        'text_no_wrap': "Geen omvou nie",
        'text_private': "Privaat teksblok (vereis staafmaking)",
        'text_preview_label': "Voorskou:",
        'text_preview_placeholder': "Hier sal 'n voorskou van die teks vertoon word...",
        'text_no_text': "(Geen teks)",
        'text_save_template': "💾 Stoor as blok",
        'text_delete_template': "🗑 Verwyder geselekteerde teksblok",
        'text_show_private': "Wys private",
        'text_hide_private': "Versteek private",
        'text_use': "✅ Gebruik teks",
        'text_saved': "Teksblok gestoor as:\n{0}",
        'text_saved_voice': "Teksblok gestoor",
        'text_deleted': "Teksblok verwyder",
        'text_no_text_to_save': "Geen teks om te stoor nie.",
        'text_no_templates': "Geen teksblokke gevind nie",
        'text_private_master_required': "Private blokke kan slegs gebruik word as 'n meesterwagwoord opgestel is.\n\nWil u nou 'n meesterwagwoord opstel?",
        'text_filename': "Lêernaam vir teksblok (sonder 'Text_' en '.txt'):",
        'text_filename_hint': "Voorbeeld: 'Telefoon Huiskantoor' word gestoor as 'Text_Telefoon Huiskantoor.txt'",
        'text_save_hint': "Die teksblok word outomaties met formatering gestoor.",
        'text_guide_title': "Teksinvoer - Handleiding",
        'text_delete_confirm': "Wil u werklik die teksblok verwyder?\n\nLêer: {0}\nTeks: {1}...",
        'text_make_public': "Merk as publiek",
        'text_make_private': "Merk as privaat",
        'text_privacy_changed': "Privaatstatus verander",
        'text_private_always': "Private altyd sigbaar (instelling)",
        'text_mode_required': "Aktiveer eers teksmodus",
        'text_continue_editing': "Gaan voort met redigering - wyser aan einde van teks",
        'text_no_input': "Geen teks ingevoer nie - teks verwerp",
        'save_dialog_question': "Hoe wil u voortgaan?",
        'text_save_question': "Stoor alle tekste en kruise, pas aan, gaan voort met redigering of verwerp?",
        'copy_cross': "Kruis gekopieer",
        'paste_cross': "Kruis ingevoeg",
        'paste_text': "Teks ingevoeg",
        'cross_discarded': "Kruis verwerp",
        'all_discarded': "Alles verwerp",
        'text_discarded': "Teks verwerp",
        'no_texts_to_save': "Geen tekste om te stoor nie",
        'no_valid_texts': "Geen geldige tekste om te stoor nie",
        'text_word_singular': "teks",
        'text_word_plural': "tekste",
        'cross_word_singular': "kruis",
        'cross_word_plural': "kruise",
        'texts_saved_title': "Tekste gestoor",
        'texts_crosses_saved': "{0} {1} en {2} {3} is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'texts_crosses_saved_voice': "{0} {1} en {2} {3} gestoor.",
        'texts_saved': "{0} {1} is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'texts_saved_voice': "{0} {1} gestoor.",
        'crosses_saved': "{0} {1} is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'crosses_saved_voice': "{0} {1} gestoor.",
        'elements_saved': "{0} elemente is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'elements_saved_voice': "{0} elemente gestoor.",
        'text_window_load_error': "Teksvenster kon nie gelaai word nie",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Teksinvoer en teksblokke – Uitgebreide handleiding**

        **1. Teks invoeg en redigeer**
        - Kliek met die regter muisknop op die gewenste plek in die dokument en kies "Voeg teks in".
        - 'n Dialoog open waar u u teks kan invoer en formateer:
        • Lettergrootte, vet, kursief, onderstreep
        • Tekskleur (vrylik kiesbaar)
        • Deursigtigheid (ondeursigtigheid) via skuifbalk
        • Woordomvou (verskillende wydtes, bv. bladsywydte, smal, geen omvou)
        - Na bevestiging verskyn die teks by die kliekposisie. U kan dit met die muis of pyltjies skuif.
        - Dubbelkliek op die teks open die redigeermodus; ESC verlaat dit weer.

        **2. Teksblokke (sjablone) bestuur**
        - In die teksdialoog links sien u 'n lys van alle gestoorde teksblokke.
        - **Stoor van 'n blok:** Voer u teks in, formateer dit en kliek op "💾 Stoor as blok". Gee 'n lêernaam in (sonder uitbreiding).
        - **Laai van 'n blok:** Kliek op die gewenste naam in die lys. Die teks en formatering word oorgeneem en kan indien nodig aangepas word.
        - **Verwyder:** Met regskliek op 'n blok kan u dit verwyder of die privaatstatus verander.

        **3. Private teksblokke (meesterwagwoord)**
        - As u 'n meesterwagwoord opgestel het (onder Instellings → Wagwoordbestuur), kan u blokke as "privaat" merk.
        - Aktiveer die merkblokkie "Privaat teksblok" in die dialoog voordat u stoor.
        - Private blokke word slegs in die lys vertoon as u een keer per sessie u meesterwagwoord ingevoer het (staafmaking via die sluitelpictogram of met die eerste toegang).
        - Sodoende kan u vertroulike teksblokke teen ongemagtigde toegang beskerm.

        **4. Kruise invoeg**
        - Via die kontekskieslys kan u ook 'n grafiese kruis (bv. vir merkblokkies) invoeg.
        - Die grootte, lynwydte en kleur van kruise kan u globaal in die instellings aanpas (kieslys "Instellings" → "Kruisinstellings").
        - Met regskliek op 'n bestaande kruis kan u dit individueel verander.

        **5. Versamelaksies**
        - As u verskeie tekste of kruise op 'n bladsy geplaas het, kan u via die kontekskieslys (regskliek in teksmodus) alle elemente gelyktydig stoor of verwerp.
        - By stoor word alle elemente in die PDF ingebed en bly as vektorgrafika behoue.

        **6. Sleutelbordkortpaaie in teksmodus**
        - Pyltjies: element skuif
        - Ctrl+pyltjies: groter stappe
        - Enter: stoor-dialoog open (alles stoor / aanpas / verwerp)
        - ESC: huidige element verwerp
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Teksinvoer en teksblokke – Uitgebreide handleiding</strong></p>

        <p><strong>1. Teks invoeg en redigeer</strong></p>
        <ul>
        <li>Kliek met die regter muisknop op die gewenste plek in die dokument en kies "Voeg teks in".</li>
        <li>'n Dialoog open waar u u teks kan invoer en formateer:<br/>
        • Lettergrootte, vet, kursief, onderstreep<br/>
        • Tekskleur (vrylik kiesbaar)<br/>
        • Deursigtigheid (ondeursigtigheid) via skuifbalk<br/>
        • Woordomvou (verskillende wydtes, bv. bladsywydte, smal, geen omvou)</li>
        <li>Na bevestiging verskyn die teks by die kliekposisie. U kan dit met die muis of pyltjies skuif.</li>
        <li>Dubbelkliek op die teks open die redigeermodus; ESC verlaat dit weer.</li>
        </ul>

        <p><strong>2. Teksblokke (sjablone) bestuur</strong></p>
        <ul>
        <li>In die teksdialoog links sien u 'n lys van alle gestoorde teksblokke.</li>
        <li><strong>Stoor van 'n blok:</strong> Voer u teks in, formateer dit en kliek op "💾 Stoor as blok". Gee 'n lêernaam in (sonder uitbreiding).</li>
        <li><strong>Laai van 'n blok:</strong> Kliek op die gewenste naam in die lys. Die teks en formatering word oorgeneem en kan indien nodig aangepas word.</li>
        <li><strong>Verwyder:</strong> Met regskliek op 'n blok kan u dit verwyder of die privaatstatus verander.</li>
        </ul>

        <p><strong>3. Private teksblokke (meesterwagwoord)</strong></p>
        <ul>
        <li>As u 'n meesterwagwoord opgestel het (onder Instellings → Wagwoordbestuur), kan u blokke as "privaat" merk.</li>
        <li>Aktiveer die merkblokkie "Privaat teksblok" in die dialoog voordat u stoor.</li>
        <li>Private blokke word slegs in die lys vertoon as u een keer per sessie u meesterwagwoord ingevoer het (staafmaking via die sluitelpictogram of met die eerste toegang).</li>
        <li>Sodoende kan u vertroulike teksblokke teen ongemagtigde toegang beskerm.</li>
        </ul>

        <p><strong>4. Kruise invoeg</strong></p>
        <ul>
        <li>Via die kontekskieslys kan u ook 'n grafiese kruis (bv. vir merkblokkies) invoeg.</li>
        <li>Die grootte, lynwydte en kleur van kruise kan u globaal in die instellings aanpas (kieslys "Instellings" → "Kruisinstellings").</li>
        <li>Met regskliek op 'n bestaande kruis kan u dit individueel verander.</li>
        </ul>

        <p><strong>5. Versamelaksies</strong></p>
        <ul>
        <li>As u verskeie tekste of kruise op 'n bladsy geplaas het, kan u via die kontekskieslys (regskliek in teksmodus) alle elemente gelyktydig stoor of verwerp.</li>
        <li>By stoor word alle elemente in die PDF ingebed en bly as vektorgrafika behoue.</li>
        </ul>

        <p><strong>6. Sleutelbordkortpaaie in teksmodus</strong></p>
        <ul>
        <li>Pyltjies: element skuif</li>
        <li>Ctrl+pyltjies: groter stappe</li>
        <li>Enter: stoor-dialoog open (alles stoor / aanpas / verwerp)</li>
        <li>ESC: huidige element verwerp</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Kruisinstellings",
        'cross_properties': "Kruiseienskappe",
        'cross_size': "Grootte (px):",
        'cross_line_width': "Lynwydte:",
        'cross_color': "Kleur:",
        'cross_choose_color': "Kies",
        'cross_fine_tuning': "Fyninstelling by stoor (pixels)",
        'cross_offset_x': "X-afwyking:",
        'cross_offset_y': "Y-afwyking:",
        'cross_offset_x_tooltip': "Negatiewe waardes skuif die kruis links by stoor, positief na regs",
        'cross_offset_y_tooltip': "Negatiewe waardes skuif die kruis op by stoor, positief af",
        'cross_preview': "Voorskou",
        'cross_save': "Pas instellings toe",
        'cross_customized': "Kruis aangepas",
        'cross_settings_applied': "Kruisinstellings gestoor.\nGrootte: {0}px, lynwydte: {1}px\n{2}",
        'cross_updated_count': "{0} bestaande kruise is bygewerk.",
        'cross_no_crosses': "Geen bestaande kruise gevind nie.",
        'cross_settings_applied_all': "Kruisinstellings vir al {0} kruise toegepas",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Handtekeninginstellings",
        'signature_1': "Handtekening 1",
        'signature_2': "Handtekening 2",
        'signature_select': "Kies handtekening",
        'signature_add': "➕ Voeg nuwe handtekening by...",
        'signature_size': "Grootte vir handtekening {0} (%):",
        'signature_common': "Algemene instellings",
        'signature_timestamp': "Voeg tydstempel outomaties by",
        'signature_location': "Standaard plek:",
        'signature_timestamp_size': "Tydstempel lettergrootte:",
        'signature_no_files': "-- Geen handtekeninge gevind nie --",
        'signature_insert': "Voeg handtekening in",
        'signature_insert_1': "Voeg handtekening 1 in",
        'signature_insert_2': "Voeg handtekening 2 in",
        'signature_customize': " Pas handtekening aan",
        'signature_discard': " Verwerp hierdie handtekening",
        'signature_save_all': " Stoor alle handtekeninge",
        'signature_discard_all': " Verwerp alle handtekeninge",
        'signature_guide_title': "Handtekeninge - Handleiding",
        'signature_guide': """
📝 Handtekeninge - Kort handleiding

- Stel meesterwagwoord op
- Konfigureer handtekeninge in die Instellings-kieslys
  (grootte, tydstempel ...)
- Voeg in met REGSKLIEK op die gewenste posisie
  (meesterwagwoord een keer per sessie vereis)
- Skuif handtekening met die muis of pyltjies
- Veelvuldige handtekeninge kan een na die ander ingevoeg word
- Elke handtekening kan individueel aangepas word
- Enkele handtekening verwerp
- Alle handtekeninge gelyktydig stoor / verwerp
- Alternatiewelik kan die kieslysbalk ook gebruik word.
        """,
        'signature_placeholder': "Geen voorskou beskikbaar nie",
        'signature_info': "Handtekening {0}: {1}×{2} px ({3}% van {4}×{5})",
        'signature_info_placeholder': "Instellings vir handtekening {0}",
        'signature_inserted': "Handtekening {0} op bladsy {1} ingevoeg",
        'signature_deleted': "Handtekening verwyder",
        'signature_copied': "Handtekening gekopieer",
        'signature_pasted': "Handtekening {0} ingevoeg",
        'signature_saved': "{0} handtekeninge is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'signature_saved_voice': "{0} handtekeninge gestoor",
        'mode_replace_signature_format': "Verlaat modus en voeg handtekening {0} in",
        'mode_conflict_voice_signature': "{0} modus is aktief. Verlaat en handtekening invoeg?",
        'signature_not_configured': "Handtekening {0} nie gekonfigureer nie",
        'signature_file_not_found': "Handtekeninglêer nie gevind nie",
        'timestamp_format': "{0}, die {1}",
        'no_copied_signature': "Geen gekopieerde handtekening nie",
        'no_signatures_to_save': "Geen handtekeninge om te stoor nie",
        'signature_save_question': "Stoor alle handtekeninge, pas aan of verwerp hierdie een?",
        'signatures_saved_title': "Handtekeninge gestoor",
        'signatures_saved': "{0} handtekeninge is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'signatures_saved_voice': "{0} handtekeninge gestoor.",
        'all_signatures_discarded': "Alle handtekeninge verwerp",
        'signature_settings_saved': "Handtekeninginstellings gestoor",
        'signature_cancelled': "Handtekening verwerp",
        'signature_active_title': "Handtekening aktief",
        'signature_replace_question': "Daar is reeds 'n aktiewe handtekening.\n\nWil u die huidige handtekening vervang?",
        'signature_replace': "Vervang handtekening",
        'signature_replace_voice': "Huidige handtekening vervang of kanselleer?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Beeldinstellings",
        'image_common': "Algemene beeldinstellings",
        'image_keep_aspect': "Behou aspekverhouding tydens sleep",
        'image_default_size': "Standaard grootte (%):",
        'image_dark_invert': "Inverteer beelde in donker modus",
        'image_dark_invert_tooltip': "Geaktiveer: beelde word geïnverteer vir beter sigbaarheid",
        'image_fine_tuning': "Fyninstelling (pixels)",
        'image_offset_x': "X-afwyking:",
        'image_offset_y': "Y-afwyking:",
        'image_offset_x_tooltip': "Negatiewe waardes skuif die beeld links by stoor, positief na regs",
        'image_offset_y_tooltip': "Negatiewe waardes skuif die beeld op by stoor, positief af",
        'image_select': "Kies beeld",
        'image_insert': "Voeg beeld in",
        'image_customize': " Pas beeld aan",
        'image_aspect': " Behou aspekverhouding",
        'image_discard': " Verwerp hierdie beeld",
        'image_save_all': " Stoor alle beelde",
        'image_discard_all': " Verwerp alle beelde",
        'image_filter': "Beelde",
        'image_guide_title': "Beelde invoeg - Handleiding",
        'image_guide': """
📷 Beelde in PDF invoeg - Kort handleiding:

1. Regskliek op die gewenste posisie
2. "Voeg beeld in" → kies beeld
3. Plaas beeld: sleep met die muis
4. Pas grootte aan: sleep aan die hoeke/kante
5. Behou aspekverhouding: [A] sleutel
6. Verdere aanpassings: regskliek op beeld

Wenk: In die kontekskieslys kan u die instellings aanpas.
        """,
        'image_inserted': "Beeld {0} op bladsy {1} ingevoeg",
        'image_deleted': "Beeld verwerp",
        'image_copied': "Beeld gekopieer",
        'image_pasted': "Beeld ingevoeg",
        'image_saved': "{0} beelde is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'image_saved_voice': "{0} beelde gestoor",
        'image_aspect_on': "geaktiveer",
        'image_aspect_off': "gedeaktiveer",
        'image_aspect_toggle': "Behou aspekverhouding {0}",
        'image_reset': "Beeld terug na oorspronklike grootte",
        'image_replaced': "Beeld vervang",
        'image_invalid': "Ongeldige beeld",
        'mode_replace_image': "Voeg beeld in",
        'mode_conflict_voice_image': "{0} modus is aktief. Verlaat en beeld invoeg?",
        'image_active_title': "Beeld aktief",
        'image_replace_question': "Daar is reeds 'n aktiewe beeld.\n\nWil u die huidige beeld vervang?",
        'image_replace': "Vervang beeld",
        'image_replace_voice': "Huidige beeld vervang of kanselleer?",
        'image_filter_all': "Beelde (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Alle lêers (*.*)",
        'no_copied_image': "Geen gekopieerde beeld nie",
        'image_discarded': "Beeld verwerp",
        'image_save_question': "Stoor alle beelde, pas aan of verwerp hierdie een?",
        'no_images_to_save': "Geen beelde om te stoor nie",
        'no_valid_images': "Geen geldige beelde om te stoor nie",
        'images_saved_title': "Beelde gestoor",
        'images_saved': "{0} beelde is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'images_saved_voice': "{0} beelde gestoor.",
        'all_images_discarded': "Alle beelde verwerp",
        'image_settings_updated': "Beeldinstellings bygewerk",
        'image_replace_title': "Kies nuwe beeld",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Vorminstellings",
        'form_basic': "Basiese instellings",
        'form_default_type': "Standaard vormtipe:",
        'form_rectangle': "Reghoek",
        'form_ellipse': "Ellips",
        'form_line': "Lyn",
        'form_arrow': "Pyl",
        'form_line_width': "Lynwydte:",
        'form_colors': "Kleure",
        'form_line_color': "Lynkleur:",
        'form_fill_color': "Vulkleur:",
        'form_choose_color': "Kies",
        'form_transparent': "Deursigtige agtergrond (slegs lyn)",
        'form_filled': "gevul",
        'form_dark_mode': "Donker modus",
        'form_dark_invert': "Inverteer kleure in donker modus",
        'form_fine_tuning': "Fyninstelling (pixels)",
        'form_offset_x': "X-afwyking:",
        'form_offset_y': "Y-afwyking:",
        'form_offset_x_tooltip': "Negatiewe waardes skuif die vorm links by stoor, positief na regs",
        'form_offset_y_tooltip': "Negatiewe waardes skuif die vorm op by stoor, positief af",
        'form_preview': "Voorskou",
        'form_insert': "Voeg vorm in",
        'form_rectangle_insert': "Reghoek",
        'form_ellipse_insert': "Ellips/sirkel",
        'form_line_insert': "Lyn (2 kliek)",
        'form_arrow_insert': "Pyl (2 kliek)",
        'form_customize': " Pas vorm aan",
        'form_transparent_toggle': " Deursigtige agtergrond",
        'form_discard': " Verwerp hierdie vorm",
        'form_save_all': " Stoor alle vorms",
        'form_discard_all': " Verwerp alle vorms",
        'form_guide_title': "Vorms invoeg - Handleiding",
        'form_guide': """
📐 Vorms in PDF invoeg - Kort handleiding:

1. Kies vormtipe (reghoek, ellips, lyn, pyl)
2. Kliek op posisie
   - By reghoek/ellips: een kliek plaas die vorm
   - By lyn/pyl: twee kliek vir begin- en eindpunt
3. Plaas vorm: sleep met die muis
4. Pas grootte aan: sleep aan die hoeke/kante
5. Stoor vorm: Enter
6. Verwerp vorm: ESC
7. Verdere aanpassings: regskliek op vorm

Wenk: In die kontekskieslys kan u die instellings aanpas.
        """,
        'form_inserted': "{0} op bladsy {1} ingevoeg",
        'form_deleted': "Vorm verwyder",
        'form_copied': "Vorm gekopieer",
        'form_pasted': "Vorm ingevoeg",
        'form_saved': "{0} vorms is in die PDF ingevoeg.\n\nPDF is herlaai...",
        'form_saved_voice': "{0} vorms gestoor",
        'form_reset': "Vorm terug na standaard grootte",
        'form_transparent_on': "geaktiveer",
        'form_transparent_off': "gedeaktiveer",
        'form_transparent_toggled': "Deursigtige agtergrond {0}",
        'form_line_cancel': "Lyntekening gekanselleer",
        'form_second_click': "Kliek nou eindpunt vir {0}",
        'mode_replace_form': "Voeg vorm in",
        'mode_conflict_voice_form': "{0} modus is aktief. Verlaat en vorm invoeg?",
        'form_settings_updated': "Vorminstellings bygewerk",
        'form_unknown': "Vorm",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Kliek op die beginposisie",
        'form_line_guide_2': "2. Kliek op die eindposisie",
        'form_line_guide_3': "Die lyn sal tussen beide punte geteken word.",
        'form_line_status_1': "Wag vir eerste kliek...",
        'form_line_status_2': "Eerste punt gestel: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Kliek nou die eindpunt...",
        'form_line_status_4': "Albei punte gestel.\nKliek op 'Klaar' om te stoor.",
        'form_line_reset': "Herstel",
        'form_line_finish': "Klaar",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopieer (Cmd+C)",
        'paste': "Plak (Cmd+V)",
        'copied': "Gekopieer: {0}",
        'no_element_to_copy': "Geen element gekies om te kopieer nie",
        'no_copied_data': "Geen gekopieerde data nie",
        'no_valid_position': "Geen geldige posisie om te plak nie",
        'copy_text': "Teks gekopieer",
        'copy_image': "Beeld gekopieer",
        'copy_form': "Vorm gekopieer",
        'copy_signature': "Handtekening gekopieer",
        'element_text': "Teks",
        'element_image': "Beeld",
        'element_form': "Vorm",
        'element_signature': "Handtekening",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Moduskonflik",
        'mode_conflict_message': "Die modus '{0}' is reeds aktief.\n\nWil u dit verlaat en {1}?",
        'mode_replace': "Verlaat modus en {0}",
        'mode_cancel': "Kanselleer",
        'mode_replace_text': "teks invoeg",
        'mode_replace_cross': "kruis invoeg",
        'mode_replace_signature': "handtekening invoeg",
        'mode_replace_image': "beeld invoeg",
        'mode_replace_form': "vorm invoeg",
        'mode_conflict_voice': "{0} modus is aktief. Verlaat en teks invoeg?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Teksinvoer",
        'active_mode_signature': "Handtekening",
        'active_mode_image': "Beeld",
        'active_mode_form': "Vorm",
        'active_mode_and': " en ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Voeg in",
        'insert_another_text': "Voeg teks in",
        'insert_another_cross': "Voeg kruis in",
        'insert_another_signature_1': "Handtekening 1",
        'insert_another_signature_2': "Handtekening 2",
        'insert_another_image': "Voeg beeld in",
        'insert_another_form_rect': "Reghoek",
        'insert_another_form_ellipse': "Ellips",
        'insert_another_form_line': "Lyn (2 kliek)",
        'insert_another_form_arrow': "Pyl (2 kliek)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Stoor {0}",
        'save_dialog_message': "{0} word op bladsy {1} gestoor.\n\nHoe wil u voortgaan?",
        'save_all': "Stoor alle {0}",
        'save_single': "Stoor {0}",
        'save_customize': "Pas {0} aan",
        'save_discard': "Verwerp hierdie {0}",
        'save_continue': "Gaan voort met redigering",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Gaan na bladsy {0}",
        'context_rotate': " Draai bladsy {0}",
        'context_delete': " Verwyder bladsy {0}",
        'context_export': " Voer bladsy {0} uit",
        'context_mark_as': " Merk bladsy as...",
        'context_mark_empty': " Leë bladsy",
        'context_unmark_empty': " Nie meer leeg nie",
        'context_mark_export': " Merk vir uitvoer",
        'context_unmark_export': " Moenie meer uitvoer nie",
        'context_batch_actions': " Versamelaksies",
        'context_batch_delete_empty': " Verwyder alle {0} leë bladsye",
        'context_batch_export_single': " Voer alle {0} bladsye uit (een lêer)",
        'context_batch_export_split': " Voer alle {0} bladsye uit (afsonderlik)",
        'context_drag_start': " Begin Drag & Drop",
        'context_drag_stop': " Beëindig Drag & Drop",
        'context_insert': " Voeg in",
        'context_insert_pages': " Voeg bladsye in",
        'context_zoom': "Zoom",
        'discard_mixed': "Verwerp alle {0} {1} en {2} {3}",
        'save_mixed': "Stoor {0} {1} en {2} {3}",
        'discard_texts': "Verwerp alle {0} tekste",
        'discard_text_single': "Verwerp 1 teks",
        'save_texts': "Stoor {0} tekste",
        'save_text_single': "Stoor 1 teks",
        'discard_crosses': "Verwerp alle {0} kruise",
        'discard_cross_single': "Verwerp 1 kruis",
        'save_crosses': "Stoor {0} kruise",
        'save_cross_single': "Stoor 1 kruis",
        'discard_signatures': "Verwerp alle {0} handtekeninge",
        'save_signature_single': "Stoor 1 handtekening",
        'save_signatures': "Stoor {0} handtekeninge",
        'discard_images': "Verwerp alle {0} beelde",
        'save_image_single': "Stoor 1 beeld",
        'save_images': "Stoor {0} beelde",
        'discard_forms': "Verwerp alle {0} vorms",
        'save_form_single': "Stoor 1 vorm",
        'save_forms': "Stoor {0} vorms",
        'cross_discard': "Verwerp hierdie kruis",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Uitvoer / invoer inligting",
        'export_what': "📋 Wat word uitgevoer?",
        'export_general': "Algemene instellings",
        'export_general_items': "• Spraakuitvoer (aan/af, spoed)\n• Donker/ligte modus\n• Rugsteuninstellings\n• OCR-instellings",
        'export_image_form': "Beeld- en vorminstellings",
        'export_image_form_items': "• Beeldinstellings (aspekverhouding, standaard grootte)\n• Vorminstellings (lynwydte, kleure)\n• Handtekeninginstellings (paaie, groottes, tydstempel)",
        'export_passwords': "Wagwoorddatabasis",
        'export_passwords_items': "• Alle gestoorde PDF-wagwoorde\n• Na keuse versleutel of ontsleutel",
        'export_master': "Meesterwagwoordinstellings",
        'export_master_items': "• Meesterwagwoord-hash\n• Instellings vir handtekeninge/teksblokke",
        'export_signatures': "Handtekeninge en teksblokke",
        'export_signatures_items': "• Alle beeldlêers (handtekeninge)\n• Alle teksblokke met formatering\n• Privaat/publieke merke",
        'export_import_warning': "⚠️ Belangrike wenke",
        'export_import_note': "• By invoer word ALLE huidige instellings oorskryf\n• 'n Herbegin van die toepassing is nodig\n• Bestaande handtekeninge/teksblokke word vervang",
        'export_master_note': "• By 'n gestelde meesterwagwoord kan u kies:\n  - Ontsleutel (wagwoorde in duidelike teks)\n  - Versleutel (slegs met meesterwagwoord leesbaar)",
        'export_security': "• Die uitgevoerde ZIP-lêer bevat vertroulike data\n• Hou dit veilig (bv. versleutelde USB-stick)\n• By verlies van die lêer is wagwoorde onherroeplik verlore",
        'export_format': "📁 Uitvoerformaat",
        'export_format_desc': "Die instellings word in 'n enkele ZIP-lêer gestoor:",
        'export_filename': "PDFDarkView_Instellings_JJJJMMDD_HHMMSS.zip",
        'export_success': "Instellings is suksesvol uitgevoer",
        'export_failed': "Uitvoer misluk",
        'export_import_question': "Wil u die toepassing nou herbegin?",
        'export_password_question': "'n Meesterwagwoord is gestel.\n\nWil u die wagwoorde ontsleutel uitvoer?\n(andersins word hulle versleutel uitgevoer)",
        'export_decrypt': "Voer ontsleutel uit",
        'export_encrypt': "Voer versleutel uit",

        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Inligting",
        'info_title': "Oor PDF Dark View",
        'info_version': "Weergawe",
        'info_author': "Ontwikkel deur Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Oor",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> is 'n toeganklike PDF-leser wat spesifiek ontwikkel is vir mense met gesiggestremdheid.</p>

            <p><strong>Kernkenmerke:</strong></p>
            <ul>
                <li>Kontrasryke, aanpasbare koppelvlak</li>
                <li>Volledige sleutelbordbeheer</li>
                <li>Geïntegreerde voorleesfunksie</li>
                <li>OCR vir geskandeerde dokumente</li>
                <li>Uitgebreide redigeernutsgoed</li>
            </ul>

            <p>Meer as 50 tale word ondersteun – sodat PDF's vir almal toeganklik is.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funksies",
        'info_features_intro': "PDF Dark View bied u die volgende moontlikhede:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Vertoning & Navigasie</strong> – Donker/Lig-modus, blaai deur bladsye, zoem, spring na bladsy</li>
            <li><strong>OCR (Teksherkenning)</strong> – Maak geskandeerde dokumente deursoekbaar en kopieerbaar</li>
            <li><strong>Redigering</strong> – Voeg teks, kruise, handtekeninge, beelde en vorms in</li>
            <li><strong>Bladsybestuur</strong> – Verwyder, onttrek, voeg in, skuif per sleep & los</li>
            <li><strong>Uitvoer</strong> – Na Word, Pages of as teks</li>
            <li><strong>Sekuriteit</strong> – Wagwoordbeskerming en -bestuur</li>
            <li><strong>Toeganklikheid</strong> – Voorleesfunksie, sleutelbordbeheer, hoë kontras</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Bediening",
        'info_accessibility': "♿ Toeganklikheid – volledige sleutelbordbeheer",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Algemeen</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF open</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Soek</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Skakel Donker/Lig-modus om</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Druk</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Sluit af</div>

        <div class="shortcut-cat">📖 Navigasie</div>
        <div class="shortcut-row"><kbd>Pyltjies</kbd> Blaai bladsy vir bladsy</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Gaan na bladsy</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Eerste bladsy</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Laaste bladsy</div>

        <div class="shortcut-cat">✏️ Redigering</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Voeg teks in</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Verwyder bladsye</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Onttrek bladsye</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Voeg bladsye in</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Skuif bladsye</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Draai bladsy</div>

        <div class="shortcut-cat">🖼️ Skuif elemente</div>
        <div class="shortcut-row"><kbd>Pyltjies</kbd> Skuif teks/beeld/handtekening</div>
        <div class="shortcut-row"><kbd>Ctrl+Pyltjies</kbd> Groter stappe</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Stoor</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Verwerp</div>

        <div class="shortcut-cat">🗣️ Voorleesfunksie</div>
        <div class="shortcut-row"><kbd>F2</kbd> Skakel voorleesfunksie aan/af</div>
        """,
        'info_contextmenu': "📌 Belangrik: Alle funksies is ook bereikbaar via die kontekskieslys (regter muisknoppie)!",
        'info_accessibility_hint': "💡 Wenk: Die voorleesfunksie (F2) vergemaklik oriëntasie en gee terugvoer oor spyskaarte en dialoogvensters.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lisensie & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Inligting volgens § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Duitsland<br>
        E-pos: binhdiez64@gmail.com<br>
        Verantwoordelik vir die inhoud: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Vrywaring</strong><br>
        Die sagteware is met die grootste sorg ontwikkel. Geen waarborg word aanvaar vir die korrektheid, volledigheid en funksionaliteit nie. Gebruik is op eie risiko.<br><br>

        <strong>📄 MIT-lisensie (private gebruik)</strong><br>
        Kopiereg (c) 2026 Toralf Schulz (BinhDiez)<br>
        Toegelaat: gratis gebruik, private veranderinge, persoonlike kopieë.<br>
        Nie toegelaat nie: Verkoop, kommersiële gebruik, verwydering van kopieregkennisgewings.<br><br>

        <strong>🔧 Derdeparty-komponente</strong><br>
        Hierdie sagteware bevat komponente onder GPL, AGPL, Apache 2.0, BSD en MIT-lisensies.<br>
        By verspreiding moet die onderskeie lisensievoorwaardes nagekom word.<br><br>

        <strong>🌐 Oop Bron</strong><br>
        Die bronkode is beskikbaar en kan ooreenkomstig die onderskeie lisensievoorwaardes bekyk, verander en versprei word.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Erkenning",
        'info_credits': "Dankie aan die oopbron-gemeenskap",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-verwerking</li>
            <li><strong>PyQt5</strong> – Grafiese koppelvlak</li>
            <li><strong>Tesseract OCR</strong> – Teksherkenning</li>
            <li><strong>OCRmyPDF</strong> – OCR-integrasie</li>
            <li><strong>python-docx</strong> – Word-uitvoer</li>
            <li><strong>qtawesome</strong> – Ikoon</li>
            <li><strong>DeepSeek</strong> – Ondersteuning met vertalings (50+ tale)</li>
            <li><strong>Alle gebruikers</strong> – Vir waardevolle terugvoer</li>
            <li><strong>Die oopbron-gemeenskap</strong> – Vir wonderlike biblioteke</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Tale",
        'info_languages_header': "🌍 Taalondersteuning",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View ondersteun tans <strong>62 tale</strong> – sodat die sagteware wêreldwyd toeganklik gebruik kan word.</p>

            <p><strong>📖 Volledige taallys (Stand: Maart 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanees (Shqip)</li>
                    <li>🇩🇿 Arabies (العربية)</li>
                    <li>🇮🇩 Balinees (Basa Bali)</li>
                    <li>🇧🇩 Bengaals (বাংলা)</li>
                    <li>🇲🇲 Birmaans (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnies (Bosanski)</li>
                    <li>🇧🇬 Bulgaars (Български)</li>
                    <li>🇨🇳 Chinees (中文)</li>
                    <li>🇩🇰 Deens (Dansk)</li>
                    <li>🇩🇪 Duits</li>
                    <li>🇬🇧 Engels (English)</li>
                    <li>🇪🇪 Estnies (Eesti)</li>
                    <li>🇫🇮 Fins (Suomi)</li>
                    <li>🇫🇷 Frans (Français)</li>
                    <li>🇬🇷 Grieks (Ελληνικά)</li>
                    <li>🇮🇱 Hebreeus (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroaties (Hrvatski)</li>
                    <li>🇭🇺 Hongaars (Magyar)</li>
                    <li>🇮🇩 Indonesies (Bahasa Indonesia)</li>
                    <li>🇮🇪 Iers (Gaeilge)</li>
                    <li>🇮🇸 Yslands (Íslenska)</li>
                    <li>🇮🇹 Italiaans (Italiano)</li>
                    <li>🇯🇵 Japannees (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreaans (한국어)</li>
                    <li>🇱🇦 Laos (ພາສາລາວ)</li>
                    <li>🇱🇻 Lets (Latviešu)</li>
                    <li>🇱🇹 Litaus (Lietuvių)</li>
                    <li>🇱🇺 Luxemburgs (Lëtzebuergesch)</li>
                    <li>🇲🇾 Maleis (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongools (Монгол)</li>
                    <li>🇳🇵 Nepalees (नेपाली)</li>
                    <li>🇳🇱 Nederlands (Nederlands)</li>
                    <li>🇳🇴 Noors (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persies (فارسی)</li>
                    <li>🇵🇱 Pools (Polski)</li>
                    <li>🇵🇹 Portugees (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Roemeens (Română)</li>
                    <li>🇷🇺 Russies (Русский)</li>
                    <li>🇸🇪 Sweeds (Svenska)</li>
                    <li>🇷🇸 Serwies (Српски)</li>
                    <li>🇸🇰 Slowaaks (Slovenčina)</li>
                    <li>🇸🇮 Sloweens (Slovenščina)</li>
                    <li>🇪🇸 Spaans (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thais (ไทย)</li>
                    <li>🇨🇿 Tsjeggies (Čeština)</li>
                    <li>🇹🇷 Turks (Türkçe)</li>
                    <li>🇺🇦 Oekraïens (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Viëtnamees (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddisj (ייִדיש)</li>
                    <li>🇿🇦 Zoeloe (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Voeg eie tale by:</strong><br>
                Wil u 'n taal hê wat nog nie ingesluit is nie? Plaas eenvoudig u eie woordeboeklêer (<code>sprache_xx.py</code>) langs die toepassing – die sagteware sal dit outomaties herken. As u belangstel in 'n spesifieke vertaling, kontak my gerus.
            </div>

            <p><strong>🙏 Spesiale dank:</strong> DeepSeek vir die ondersteuning met die vertaling van alle woordeboeke in 62 tale.</p>

            <p>📧 Kontak vir vertalings: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Fout",
        'error_occurred': "'n Fout het voorgekom",
        'error_pdf_load': "Fout met laai van PDF",
        'error_pdf_save': "Fout met stoor van PDF",
        'error_ocr': "Fout met teksherkenning",
        'error_no_pdf': "Geen PDF gelaai nie",
        'error_page_not_found': "Bladsy nie gevind nie",
        'error_invalid_range': "Ongeldige bladsybereik",
        'error_file_not_found': "Lêer nie gevind nie",
        'error_permission': "Geen toestemming nie",
        'error_unknown': "Onbekende fout",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Sukses",
        'success_operation': "Bewerking suksesvol voltooi",
        'success_saved': "Suksesvol gestoor",
        'success_exported': "Suksesvol uitgevoer",
        'success_imported': "Suksesvol ingevoer",
        'success_deleted': "Suksesvol verwyder",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Bevestig",
        'confirm_yes': "Ja",
        'confirm_no': "Nee",
        'confirm_ok': "OK",
        'confirm_cancel': "Kanselleer",
        'confirm_delete': "Verwyder",
        'confirm_overwrite': "Oorskryf",
        'confirm_continue': "Gaan voort",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Besig om PDF te laai...",
        'progress_saving': "Besig om PDF te stoor...",
        'progress_exporting': "Besig om PDF uit te voer...",
        'progress_processing': "Verwerking besig...",
        'progress_wait': "Wag asseblief...",
        'progress_preparing': "Voorbereiding...",
        'progress_finalizing': "Finalisering...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Wit",
        'color_black': "Swart",
        'color_red': "Rooi",
        'color_green': "Groen",
        'color_blue': "Blou",
        'color_yellow': "Geel",
        'color_magenta': "Magenta",
        'color_cyan': "Siaan",
        'color_orange': "Oranje",
        'color_gray': "Grys",
        'color_custom': "Kleurkies",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Lêer",
        'menu_edit': "&Wysig",
        'menu_view': "&Aansig",
        'menu_tools': "&Gereedskap",
        'menu_settings': "&Instellings",
        'menu_help': "&Hulp",
        'menu_language': "🌐 Taal",
        'menu_guides': "&Handleidings",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Maak oop",
        'file_save_as': "&Stoor as...",
        'file_protect': "&Beskerm dokument...",
        'file_export': "&Voer uit",
        'file_export_pages': "Voer na Pages uit",
        'file_export_word': "Voer na DOCX uit",
        'file_export_text': "Voer na TXT uit",
        'file_print_now': "&Druk nou",
        'file_print': "&Druk",
        'file_close': "&Sluit",
        'file_quit': "&Sluit af",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Soek",
        'edit_ocr': " Voer OCR uit",
        'edit_rotate': "&Draai bladsy",
        'edit_rotate_all': "Draai &alle bladsye",
        'edit_delete_pages': "&Verwyder bladsye",
        'edit_extract_pages': "&Onttrek bladsye",
        'edit_insert_pages': "&Voeg bladsye in",
        'edit_move_pages': "&Skuif bladsye",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Voeg teks en kruise in",
        'text_insert': " Voeg teks in",
        'cross_insert': " Voeg kruis in",
        'text_customize': " Pas teks aan",
        'cross_customize': " Pas hierdie kruis aan",
        'cross_customize_all': " Pas alle kruise aan",
        'text_discard': " Verwerp hierdie teks/kruis",
        'text_discard_all': " Verwerp alle tekste en kruise",
        'text_save_all': " Stoor alle tekste en kruise",
        'text_guide': " Teksinvoer / teksblokke - handleiding",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Voeg handtekening in",
        'signature_settings_menu': " Instellings...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Voeg beeld in",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Voeg vorms in",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Wys teksvenster",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Bladsywydte (standaard)",
        'view_zoom_two': "&Twee bladsye",
        'view_zoom_overview': "&Oorsig (veelvuldige bladsye)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Toeganklikheid",
        'settings_voice': "Spraakuitset",
        'settings_voice_tooltip': "vul die spraakuitset van skermlesers aan met bykomende inligting",
        'settings_signature': "&Handtekeninginstellings",
        'settings_password': "&Wagwoordbestuur",
        'settings_backup': "Skep rugsteun voor veranderinge",
        'settings_export_import': "&Voer instellings uit / voer instellings in",
        'settings_export': "&Voer alle instellings uit...",
        'settings_import': "&Voer alle instellings in...",
        'settings_export_info': "&Wat word uitgevoer?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "aan",
        'voice_off': "af",
        'voice_toggle': "Spraakuitset {0}",
        'voice_speed': "Spoed {0} persent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Nutsmiddel nie gevind nie:\n{0}\n\nBASE_DIR: {1}\nMaak seker dat die PDF-nutsmiddels in die gids {1} geïnstalleer is.",
        'tool_started': "{0} begin",
        'tool_start_failed': "Kon nie begin nie",
        'process_error_failed_to_start': "Proses kon nie begin word nie. Bestaan die lêer?",
        'process_error_crashed': "Proses het tydens begin ineen gestort.",
        'process_error_timeout': "Proses-tydperk bereik.",
        'process_error_write': "Skryffout in proses.",
        'process_error_read': "Leesfout in proses.",
        'process_error_unknown': "Onbekende prosesfout",
        'process_command': "Opdrag",
        'process_normal_exit': "normaal beëindig",
        'process_crashed': "ineen gestort",
        'process_nonzero_exit': "{0} is met foutkode {1} beëindig",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Besig om te kanselleer...",
        'move_cancelling': "Skuif word gekanselleer",
        'opening_pdf': "Maak PDF oop...",
        'loading_document': "Laai dokument...",
        'pdf_opened': "PDF oopgemaak",
        'pages_found_moving': "{0} bladsye gevind, {1} om te skuif",
        'creating_backup': "Skep rugsteun...",
        'backup_description': "Maak rugsteun van oorspronklike lêer...",
        'backup_saved_as': "Rugsteun gestoor as: {0}",
        'error_format': "Fout: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView deur BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Soek teruggestel",
        'page_header_simple': "=== Bladsy {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Wagwoordbestuur – Handleiding",
        'password_guide_voice': "Handleiding vir wagwoordbestuur. Lees asseblief die wenke.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Wagwoordbestuur – Uitgebreide handleiding</strong></p>

        <p><strong>1. Wagwoordbeskerming vir PDF's</strong></p>
        <ul>
        <li>By die oopmaak van 'n wagwoordbeskermde PDF verskyn 'n dialoog waar u die wagwoord kan invoer.</li>
        <li>U kan die wagwoord versleutel stoor sodat u dit nie elke keer hoef in te voer nie (merkblokkie "Stoor wagwoord").</li>
        <li>Met die knoppie "Verwyder wagwoord" kan u 'n ontsleutelde kopie van die PDF skep en die wagwoord uit die databasis verwyder.</li>
        </ul>

        <p><strong>2. Meesterwagwoord</strong></p>
        <ul>
        <li>Die meesterwagwoord beskerm toegang tot alle gestoorde PDF-wagwoorde.</li>
        <li><strong>Opstel:</strong> Gaan na "Instellings → Wagwoordbestuur → Meesterwagwoordinstellings" en kliek op "Stel meesterwagwoord op". Kies 'n sterk wagwoord (minstens 8 karakters).</li>
        <li><strong>Verander:</strong> Na suksesvolle staafmaking kan u die meesterwagwoord verander.</li>
        <li><strong>Verwyder:</strong> As u die meesterwagwoord verwyder, word AL die gestoorde wagwoorde onherroeplik verwyder. U kan vooraf 'n rugsteun uitvoer.</li>
        <li>Een keer per sessie moet u uself met die meesterwagwoord staafmaak om toegang tot beskermde funksies (bv. vertoon van wagwoorde) te kry.</li>
        </ul>

        <p><strong>3. Wagwoordbestuur (lys)</strong></p>
        <ul>
        <li>Onder "Instellings → Wagwoordbestuur" open 'n tabel van alle gestoorde PDF's met hul versleutelde wagwoorde.</li>
        <li><strong>Sonder meesterwagwoord:</strong> U kan slegs inskrywings verwyder – die wagwoorde bly versteek.</li>
        <li><strong>Met meesterwagwoord (gestaaf):</strong> U kan wagwoorde vertoon, kopieer, uitvoer en verwyder.</li>
        <li><strong>Uitvoer:</strong> Kies 'n formaat (JSON, CSV, TXT) en stoor die lys. By 'n gestelde meesterwagwoord kan u kies of die wagwoorde in duidelike teks of versleutel uitgevoer word.</li>
        <li><strong>Invoer:</strong> 'n Vorige uitgevoerde ZIP-lêer (alle instellings) kan via "Instellings → Voer instellings uit / voer instellings in" weer ingelees word. Let op: Bestaande data word oorskryf!</li>
        </ul>

        <p><strong>4. Wagwoordgenerator</strong></p>
        <ul>
        <li>In die wagwoorddialoog (bv. by die beskerming van 'n PDF) vind u regs van die invoerveld 'n dobbelsteen-knoppie 🎲.</li>
        <li>Kliek daarop om die wagwoordgenerator te open. U kan lengte, karakterstelle (hoofletters, kleinletters, syfers, spesiale karakters) en skeidingstekens vir beter leesbaarheid instel.</li>
        <li>Die gegenereerde wagwoord kan direk oorgeneem en indien nodig gekopieer word.</li>
        </ul>

        <p><strong>5. Belangrike veiligheidswenke</strong></p>
        <ul>
        <li>Gestoorde wagwoorde word met AES-256 versleutel gestoor. Die sleutel word van u meesterwagwoord (indien gestel) of van 'n vaste waarde (sonder meesterwagwoord) afgelei.</li>
        <li>Sonder meesterwagwoord is die wagwoorde wel versleutel, maar die sleutel is in die program ingebed – 'n aanvaller met toegang tot u lêers kan dit moontlik ontsleutel. Daarom beveel ons sterk aan om 'n meesterwagwoord te gebruik.</li>
        <li>Die wagwoorddatabasis is in die lêer `Data/passwords.json`. Maak gereeld rugsteun, veral voordat u die meesterwagwoord verwyder.</li>
        <li>By verlies van die meesterwagwoord is alle gestoorde wagwoorde onherroeplik verlore.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Inverteringsmodus",
        'invert_mode_classic': "Klassiek (inverteer alle kleure)",
        'invert_mode_smart': "Intelligent (inverteer slegs helderheid)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Grysskaal-drempelwaarde",
        'gray_threshold_10': "10% (streng)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standaard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (sag)",
        'threshold_changed': "Drempelwaarde gestel op {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Grysskaal-drempelwaarde – Verduideliking",
        'threshold_guide_text': "Die grysskaal-drempelwaarde bepaal watter piksels in die intelligente donker modus as 'grys' beskou word en geïnverteer word.\n\n"
                                "• 'n Lae waarde (10%) inverteer slegs byna perfekte grystone – gekleurde elemente bly volledig behoue.\n"
                                "• 'n Hoë waarde (50%) inverteer ook liggekleurde piksels – dit verhoog die kontras, maar kan kleure verwring.\n\n"
                                "Die optimale waarde hang af van die dokument. Vir suiwer teksdokumente is 30–40% dikwels ideaal, vir gekleurde grafieke eerder 10–20%.\n\n"
                                "U kan die waarde enige tyd via die 'Instellings'-kieslys aanpas – die PDF sal dan onmiddellik herlaai word.\n\n"
                                "Let wel:\n* Foto's en beelde kan slegs korrek in die Lig-modus vertoon word!\n* Die inverteringsinstellings word slegs vertoon wanneer die Donker-modus geaktiveer is.",
        'threshold_guide_voice': "Die grysskaal-drempelwaarde bepaal hoe sterk die intelligente donker modus ingryp. 'n Lae waarde bewaar kleure, 'n hoë waarde verhoog die kontras.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF word geopen...",
        'progress_loading_document': "Laai dokument...",
        'progress_pdf_opened': "PDF geopen",
        'progress_creating_backup': "Skep rugsteun...",
        'progress_backup_description': "Sekureer oorspronklike lêer...",
        'progress_backup_created': "Rugsteun geskep",
        'progress_backup_saved_as': "Gestoor as: {0}",
        'progress_analyzing_start': "Begin analise...",
        'progress_searching_empty': "Soek leë bladsye...",
        'progress_page_empty': "Bladsy {0} is leeg",
        'progress_page_keep': "Hou bladsy {0}",
        'progress_analysis_complete': "Analise voltooi",
        'progress_empty_found': "{0} leë bladsye gevind",
        'progress_current_page': "Huidige bladsy",
        'progress_mark_delete': "Word gemerk om te verwyder",
        'progress_range_selected': "Bladsyreeks {0}-{1}",
        'progress_deleting_pages': "Verwyder {0} bladsye",
        'progress_creating_new_pdf': "Skep nuwe PDF...",
        'progress_transferring_pages': "Dra bladsye oor",
        'progress_keeping_page': "Bladsy {0} word gehou ({1}/{2})",
        'progress_saving_pdf': "Stoor PDF...",
        'progress_optimizing': "Optimeer lêergrootte...",
        'progress_finalizing': "Finaliseer...",
        'progress_new_size': "Nuwe grootte: {0:.2f} MB",
        'progress_cancelling': "Word gekanselleer...",
        'progress_cancel_message': "{0} word gekanselleer",
        'progress_pages_found_moving': "{0} bladsye gevind, {1} om te skuif",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF word ontleed...",
        'ocr_status_optimizing': "Beeldoptimalisering aan die gang...",
        'ocr_status_recognizing': "Teksherkenning in werking...",
        'ocr_status_embedding': "Teks word ingebed...",
        'ocr_status_finalizing': "Finalisering van die PDF...",

        # PDF-Laden
        'progress_preparing': "Voorbereiding...",
        'progress_loading': "PDF word gelaai...",

        # Seitenoperationen
        'progress_deleting_title': "Verwyder bladsye...",
        'progress_moving_title': "Skuif bladsye...",
        'pages_found': "Bladsye gevind",
        'progress_creating_new_order': "Skep nuwe volgorde...",
        'progress_sorting_pages': "Sorteer bladsye...",
        'progress_moving_to_begin': "Skuif {0} bladsye na die begin",
        'progress_transferring_count': "Dra {0} bladsye oor",
        'progress_transferring_before_target': "Dra bladsye oor voor die teiken",
        'progress_moving_pages': "Skuif {0} bladsye",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_rugsteun_",
        'filename_protected_suffix': "_beskerm_",
        'filename_copy_suffix': "_Kopie",
        'filename_page_single': "_Bladsy_",
        'filename_page_range': "_Bladsye_",
        'filename_export_page': "_Bladsy_{0:03}",
        'filename_export_range': "_Bladsye_{0}-{1}",
        'filename_export_multiple': "_Bladsye_{0}",
        'filename_with_text': "_met_Teks",
        'filename_with_signature': "_met_Handtekening",
        'filename_with_image': "_met_Beeld",
        'filename_with_forms': "_met_Vorms",
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
        'view_toggle_navbar': "Wys knoppiebalk",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Nie alle bladsye kan verwyder word nie",
		'pages_cannot_delete_last_page': 'Die laaste bladsy kan nie verwyder word nie!',
		'pages_cannot_delete_all_pages': 'Ten minste een bladsy moet in die dokument bly!',
		'delete_pages_confirm': 'Is u seker dat u {0} bladsye wil verwyder?',
		'delete_pages_confirm_voice': 'Is u seker dat u {0} bladsye wil verwyder?',
		'pages_deleted': '{0} bladsye is suksesvol verwyder.',
		'warning': 'Waarskuwing',
		'error': 'Fout',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Geen vorm geselekteer",
        'form_customized': "Vorm aangepas",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Kies",
        'btn_use': "Gebruik",
        'master_password_for_spasswords': "Om wagwoorde te stoor en te gebruik, moet eers 'n meesterwagwoord ingestel word.\n\nWil u nou die meesterwagwoord instel?",
        'open_saved_dialog_title': "Gestoorde lêer oopmaak",
        'open_saved_question': "Wil u die gestoorde lêer nou oopmaak?",
        'password': "Wagwoord",
        'password_manager_master_required': "Die wagwoordbestuurder is slegs beskikbaar as 'n meesterwagwoord ingestel is.\n\nWil u nou die meesterwagwoord instel?",
        'password_master_required_for_select': "Om gestoorde wagwoorde te vertoon en te kies, moet u eers met u meesterwagwoord identifiseer.\n\nWil u nou identifiseer?",
        'password_not_available': "Die gekose wagwoord is nie beskikbaar nie of kon nie ontsyfer word nie.",
        'password_options_title': "Wagwoord-opsies",
        'password_save_choice_change': "Nuwe wagwoord instel",
        'password_save_choice_keep': "Bestaande wagwoord gebruik",
        'password_save_choice_none': "Ongeënkripteer stoor",
        'password_save_hint': "Stel eers 'n meesterwagwoord in om wagwoorde veilig te stoor.",
        'password_save_master_required': "Wagwoord stoor (slegs met meesterwagwoord moontlik)",
        'password_save_question': "Die huidige PDF is wagwoordbeskerm. Wil u die bestaande wagwoord gebruik, 'n nuwe een instel of ongeënkripteer stoor?",
        'password_select': "Kies wagwoord",
        'password_select_none': "Geen wagwoord gekies nie.\n\nKies asseblief 'n wagwoord uit die lys.",
        'password_select_one': "Kies asseblief presies een wagwoord.\n\nU het verskeie wagwoorde gemerk.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_rugsteun",
        'filename_insert_suffix': "_met_invoeging",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_bladsye_verwyder",
        'filename_pages_moved': "_bladsye_geskuif",
        'filename_rotated_all_suffix': "_alle_bladsye_gedraai",
        'filename_rotated_suffix': "_bladsy_gedraai",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurasie van lêername by PDF-veranderings",
        'filename_keep_suffixes': "Vorige uitbreidings (bv. _met_teks) behou",
        'filename_keep_suffixes_false': "Vervang",
        'filename_keep_suffixes_true': "Behou",
        'filename_preview_label': "Voorbeeld van lêernaam:",
        'filename_preview_overwrite_hint': "Voorbeeld nie beskikbaar nie – die oorspronklike word oorskryf.",
        'filename_separator': "Skeidingsteken tussen woorde",
        'filename_separator_none': "Geen skeidingsteken",
        'filename_separator_space': "Spasie ( )",
        'filename_separator_underscore': "Onderstreep (_)",
        'filename_settings_saved': "Lêernaam-instellings gestoor",
        'filename_settings_title': "Lêernaam-formatering & rugsteun",
        'filename_timestamp_position': "Posisie van die tydstempel",
        'filename_timestamp_position_after': "Na die basisnaam",
        'filename_timestamp_position_before': "Hele vooraan",
        'filename_timestamp_position_end': "Aan die einde",
        'filename_use_timestamp': "Gebruik tydstempel",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Gedrag by veranderings:</b><ul><li>Verwyder en voeg bladsye in</li><li>Voeg teks, handtekening, beeld en vorms in</li><li>OCR</li></ul></html>",
        'backup_section': "Rugsteun vir bladsy-operasies (Verwyder, Skuif)",
        'behavior_info': "Let wel: By 'Oorskryf oorspronklike' word tydstempel en agtervoegsels geïgnoreer – die lêer behou sy naam.",
        'behavior_new_file': "Skep altyd nuwe lêer (met tydstempel en agtervoegsel)",
        'behavior_overwrite': "Oorskryf oorspronklike (geen nuwe lêer)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Alle bladsye is gedraai.\n\nOorspronklike onveranderd gebly.\nNuwe lêer: {0}",
        'all_pages_rotated_voice': "Alle bladsye gedraai, nuwe lêer geskep.",
        'empty_pages_deleted_new_file': "{0} leë bladsye is verwyder.\n\nOorspronklike onveranderd gebly.\nNuwe lêer: {1}",
        'empty_pages_deleted_voice': "{0} leë bladsye verwyder, nuwe lêer geskep.",
        'ocr_keep_original': "Behou oorspronklike (later handmatig oopmaak)",
        'ocr_new_file_question': "Die nuwe deursoekbare PDF is gestoor onder:\n{0}\n\nWil u dit nou oopmaak?",
        'ocr_open_new': "Maak nuwe OCR-lêer oop",
        'ocr_original_kept': "Die oorspronklike lêer bly oop. Die OCR-lêer is gestoor.",
        'page_deleted_new_file': "Bladsy {0} is verwyder.\n\nOorspronklike onveranderd gebly.\nNuwe lêer: {1}",
        'page_deleted_voice': "Bladsy {0} verwyder, nuwe lêer geskep.",
        'page_rotated_new_file': "Bladsy {0} is gedraai.\n\nOorspronklike onveranderd gebly.\nNuwe lêer: {1}",
        'page_rotated_voice': "Bladsy {0} gedraai, nuwe lêer geskep.",
        'pages_deleted_new_file': "{0} bladsye is verwyder.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer: {1}",
        'pages_deleted_new_file_voice': "{0} bladsye verwyder, nuwe lêer geskep.",
        'pages_inserted_new_file': "{0} bladsye is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer: {1}",
        'pages_inserted_new_file_ask': "{0} bladsye is ingevoeg.\n\nOorspronklike onveranderd gebly.\nNuwe lêer: {1}\n\nWil u dit nou oopmaak?",
        'pages_inserted_voice_new': "{0} bladsye ingevoeg, nuwe lêer geskep.",
        'pages_moved_new_file': "{0} bladsye is geskuif.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer: {1}",
        'pages_moved_new_file_voice': "{0} bladsye geskuif, nuwe lêer geskep.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Moenie weer wys nie",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Rugsteun-instelling</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Rugsteun AAN</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">By alle veranderings wat die oorspronklike oorskryf</strong> (teks, handtekening, beeld, vorm, OCR, draai, invoeg, bladsye verwyder/skuif) word <strong>outomaties 'n rugsteun met tydstempel</strong> geskep voordat die verandering toegepas word.</p>
                <p style="margin: 5px 0 5px 20px;">• Die rugsteun is langs die oorspronklike lêer (bv. <code>Dokument_rugsteun_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• As u bykomend die opsie <strong>„Oorskryf oorspronklike“</strong> geaktiveer het, word ook 'n rugsteun geskep.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Rugsteun AF</p>
                <p style="margin: 5px 0 5px 20px;">• Daar word <strong>geen rugsteun</strong> geskep nie – nie by oorskryf nie, ook nie by bladsy-operasies nie.</p>
                <p style="margin: 5px 0 5px 20px;">• Die oorspronklike lêer kan onherroeplik verlore gaan by oorskryf.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Slegs aanbeveel vir ervare gebruikers!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Wenk:</strong> Die rugsteun-instelling is onafhanklik van die opsie „Oorskryf oorspronklike“. U kan beide kombineer.<br>
                U kan hierdie boodskap permanent wegsteek.
            </div>
        </div>
        """,
        'backup_info_title': "Rugsteun-gedrag",
        'backup_info_voice': "Kennisgewing oor rugsteun-gedrag by bladsy-operasies. Rugsteun aan oorskryf oorspronklike, rugsteun af skep nuwe lêer.",
        'show_backup_info': "Inligting oor rugsteun-instelling",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Moenie weer wys nie",
        'overwrite_enable_backup': "Aktiveer rugsteun (aanbeveel)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Oorskryf oorspronklike</p>
            <p>As u hierdie opsie aktiveer, word veranderings (teks, handtekening, beeld, vorm, OCR, draai, invoeg) <strong>direk in die oorspronklike gestoor</strong> – daar word <strong>geen nuwe lêer geskep</strong> nie.</p>
            <p>• Die lêernaam bly onveranderd.<br>
            • Tydstempel en agtervoegsels word geïgnoreer.<br>
            • <strong>Sonder rugsteun kan die oorspronklike onherroeplik verlore gaan.</strong></p>
            <p style="color: #FFD700;">Aanbeveling: Aktiveer bykomend die rugsteun-opsie om outomatiese veiligheidskopieë te kry.</p>
        </div>
        """,
        'overwrite_info_title': "Oorskryf oorspronklike",
        'overwrite_info_voice': "Waarskuwing: Oorskryf oorspronklike – geen nuwe lêer nie. Rugsteun aanbeveel.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} bladsye is ingevoeg.\n\nDie oorspronklike lêer is oorskryf.\n'n Rugsteun is geskep.",
        'pages_inserted_overwrite_no_backup': "{0} bladsye is ingevoeg.\n\nDie oorspronklike lêer is oorskryf.\nGEEN rugsteun is geskep nie.",
        'texts_saved_overwrite_with_backup': "Die veranderings is in die oorspronklike gestoor.\n\n'n Rugsteun is geskep.",
        'texts_saved_overwrite_no_backup': "Die veranderings is in die oorspronklike gestoor.\n\nGEEN rugsteun is geskep nie.",
        'texts_crosses_saved_new_file': "{0} {1} en {2} {3} is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer is geskep.\n\nDie nuwe PDF word gelaai...",
        'texts_saved_new_file': "{0} {1} is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer is geskep.\n\nDie nuwe PDF word gelaai...",
        'crosses_saved_new_file': "{0} {1} is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer is geskep.\n\nDie nuwe PDF word gelaai...",
        'elements_saved_new_file': "{0} elemente is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer is geskep.\n\nDie nuwe PDF word gelaai...",
        'signatures_saved_overwrite_with_backup': "Die handtekening(e) is in die oorspronklike gestoor.\n\n'n Rugsteun is geskep.",
        'signatures_saved_overwrite_no_backup': "Die handtekening(e) is in die oorspronklike gestoor.\n\nGEEN rugsteun is geskep nie.",
        'images_saved_overwrite_with_backup': "Die beeld(e) is in die oorspronklike gestoor.\n\n'n Rugsteun is geskep.",
        'images_saved_overwrite_no_backup': "Die beeld(e) is in die oorspronklike gestoor.\n\nGEEN rugsteun is geskep nie.",
        'forms_saved_overwrite_with_backup': "Die vorm(e) is in die oorspronklike gestoor.\n\n'n Rugsteun is geskep.",
        'forms_saved_overwrite_no_backup': "Die vorm(e) is in die oorspronklike gestoor.\n\nGEEN rugsteun is geskep nie.",
        'signatures_saved_new_file': "{0} handtekeninge is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer is geskep.\n\nDie nuwe PDF word gelaai...",
        'images_saved_new_file': "{0} beelde is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer is geskep.\n\nDie nuwe PDF word gelaai...",
        'forms_saved_new_file': "{0} vorms is ingevoeg.\n\nDie oorspronklike lêer onveranderd gebly.\nNuwe lêer is geskep.\n\nDie nuwe PDF word gelaai...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Let wel: Hierdie PDF bevat gedraaide bladsye. Die posisionering kan afwyk.",
        'page_rotated_warning_title': "Gedraaide bladsy opgespoor",
        'page_rotated_warning_message': "Die huidige bladsy {0} is {1}° gedraai.\n\nDie invoeging van elemente op gedraaide bladsye word nie ondersteun nie.\n\nWil u die bladsy nou na regop posisie draai?",
        'page_rotated_warning_voice': "Let wel: Die bladsy is gedraai. Draai dit asseblief eers.",
        'paste_on_rotated_page_simple_warning': "Invoeging op bladsy {0} nie moontlik nie!\n\nHierdie bladsy is {1}° gedraai.\n\nDraai asseblief eers die bladsy na 0° (Spyskaart: Wysig → Rig bladsy uit).\n\nLet wel:\nDie voorheen gekopieerde element gaan verloor as u nie stoor voordat u die bladsy draai nie.",
        'paste_on_rotated_page_voice': "Invoeging gestaak. Bladsy is gedraai. Rig asseblief eers bladsy uit.",
        'page_rotated_cancel': "Kanselleer",
        'page_rotated_rotate_until_upright': "Draai bladsy herhaaldelik (tot regop)",
        'page_rotated_now_upright': "Die bladsy is nou regop. U kan nou invoeg.",
        'page_rotated_still_not_upright': "Die bladsy kon nie regop gedraai word nie. Korrigeer asseblief handmatig.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hulp: Gedraaide bladsye korrigeer",
        'help_rotated_pages_voice': "Hulp vir die korrigering van gedraaide bladsye word geopen.",
        'btn_help': "Hulp",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Probleem: Gedraaide bladsy – Invoeging werk nie korrek nie</p>

            <p>As die invoeging van tekste, handtekeninge of vorms op 'n gedraaide bladsy nie behoorlik werk nie, kan u die bladsy met 'n eksterne PDF-redigeerder korrigeer.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Oplossing met eksterne instrument (bv. macOS Voorskou)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksporteer bladsy</strong><br>
                &nbsp;&nbsp;Klik in die spyskaart op <strong>Lêer → Eksporteer as bladsye</strong> of gebruik 'n ander metode om die gewenste bladsy as 'n enkele PDF te stoor.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Maak bladsy in eksterne program oop</strong><br>
                &nbsp;&nbsp;Maak die geëksporteerde PDF oop in 'n PDF-redigeerder (bv. <strong>macOS Voorskou</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Draai bladsy</strong><br>
                &nbsp;&nbsp;Draai die bladsy sodat dit regop staan (in Voorskou: <strong>Gereedskap → Draai</strong> of <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Stoor</strong><br>
                &nbsp;&nbsp;Stoor die gekorrigeerde bladsy (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Voeg bladsy weer in die oorspronklike dokument in</strong><br>
                &nbsp;&nbsp;Keer terug na PDFDarkView en voeg die gekorrigeerde bladsy op die gewenste posisie in:<br>
                &nbsp;&nbsp;<strong>Wysig → Voeg bladsye in</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatief: Draai bladsy in oorspronklike</p>
                <p style="margin: 5px 0 5px 20px;">• Gebruik die ingeboude draaifunksie (<strong>Wysig → Draai bladsy</strong>) om die bladsy stapsgewys te korrigeer.<br>
                • Na elke draai kan u toets of die invoeging nou werk.<br>
                • Dit is dikwels die vinniger oplossing – probeer dit eers!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Wenk:</strong> As u gereeld op gedraaide bladsye afkom, kan u die waarskuwing in die invoegdialoog permanent wegsteek.<br>
                Die posisionering kan dan egter afwyk – gebruik hierdie opsie slegs as u die gevolge ken.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Rig bladsye uit",
        'menu_rotate_normalize_tooltip': "Draai bladsy of stel terug na 0°",
        'normalize_current_page': "Bring huidige bladsy na regop posisie (stel op 0°)",
        'normalize_all_pages': "Bring alle bladsye na regop posisie (stel op 0°)",
        'page_normalized': "Bladsy {0} is na regop posisie gestel.",
        'all_pages_normalized': "Alle bladsye is na regop posisie gestel.",
        'page_already_upright': "Bladsy {0} is reeds regop.",
        'all_pages_already_upright': "Alle bladsye is reeds regop.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>Die PDF bevat geen deursoekbare teks nie.</p><p>Wil u OCR uitvoer om na {0} te eksporteer?</p>",
        'export_ocr_voice': "Die PDF bevat geen teks nie. OCR benodig vir uitvoer na {0}.",
        'export_no_ocr_possible': "Uitvoer sonder OCR nie moontlik nie. Voer asseblief OCR uit via die spyskaart.",
        'ocr_failed_export_not_possible': "OCR misluk. Uitvoer kan nie uitgevoer word nie.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF word in Voorskou geopen. Begin asseblief die drukproses daar.",
        'print_preview_manual': "PDF is geopen. Voer asseblief die drukopdrag handmatig uit (bv. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDF's samesmelt",
        'merge_pdfs': "PDF's samesmelt",
        'merge_progress_title': "PDF's word saamgesmelt...",
        'merge_pdfs_list': "PDF's in volgorde (Sleep en los om te sorteer)",
        'merge_add_pdf': "Voeg PDF by",
        'merge_remove': "Verwyder",
        'merge_move_up': "Op",
        'merge_move_down': "Af",
        'merge_pdfs_info': "💡 Wenk: U kan die volgorde per sleep en los verander",
        'merge_no_pdfs': "Geen PDF's gekies nie. Klik op 'Voeg PDF by'.",
        'merge_info': "{0} PDF's gekies (ong. {1} bladsye)",
        'merge_open_file': "Maak lêer oop",
        'merge_merge': "Smelt saam",
        'merge_error': "Fout tydens samesmelting",
        'merge_min_two_pdfs_error': "Kies asseblief ten minste twee PDF-lêers om saam te smelt.",
        'merge_select_pdfs': "Kies PDF's om saam te smelt",
        'merge_error_file': "Fout met verwerking",
        'merge_cancelled': "Samesmelting is gekanselleer",
        'merge_preparing': "Voorbereiding...",
        'merge_processing': "Verwerk PDF {0} van {1}",
        'merge_saving': "Stoor saamgesmelte PDF...",
        'merge_complete': "Klaar!",
        'merge_success_title': "Samesmelting suksesvol",
        'merge_success_voice': "{0} PDF's is suksesvol saamgesmelt.",
        'merge_success_message': "{0} PDF's is suksesvol saamgesmelt.\n\nDie nuwe dokument het nou {1} bladsye.\n\nNuwe lêer:\n{2}\n\nStoorplek:\n{3}\n{2}\n\nWil u hierdie PDF oopmaak?",
        'replace_file_title': "Vervang lêer?",
        'replace_file_message': "'n PDF is reeds oop. Wil u dit met die nuwe lêer vervang?",
        'btn_yes': "Ja",
        'btn_no': "Nee",
        'filename_merge_suffix': "saamgesmelt",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Maak {0} oop...",
        'progress_merge_reading': "Lees {0}...",
        'progress_merge_adding': "Voeg {0} bladsye by...",
        'progress_merge_optimizing': "Optimeer PDF...",
        'progress_merge_writing': "Skryf PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "die sluiting van die PDF",
        'action_close_window': "die sluiting van die venster",
        'action_open_new_pdf': "die opening van 'n nuwe PDF",
        'action_quit_app': "die beëindiging van die toepassing",
        'changes_saved': "Die veranderings is gestoor.",
        'file_close_title': "Sluit PDF-lêer",
        'save_before_action': "Moet die veranderings voor {0} gestoor word? Ja of Nee?",
        'save_before_action_voice': "Moet die veranderings voor {0} gestoor word? Ja of Nee?",
        'save_before_close_question': "Moet die veranderings voor sluiting gestoor word? Ja of Nee?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Deursoekbare PDF geskep:\n\n{0}\n\n<b>probeer weer indien nodig",
        "ocr_rotate_title": "Rig bladsye in voor OCR",
        "ocr_rotate_question": "Die PDF bevat gedraaide bladsye.\nWil u alle bladsye voor OCR op 0° rig?\nDit verbeter tekenherkenning aansienlik.",
        "ocr_rotate_yes": "Ja, rig in",
        "ocr_rotate_no": "Nee, begin direk met OCR",
        "ocr_rotate_voice": "Die PDF bevat gedraaide bladsye. Moet alle bladsye voor OCR ingerig word?",
        "ocr_not_performed_message": "Geen teks teenwoordig nie. Voer asseblief OCR uit (Spyskaart \"Wysig\" → \"Voer OCR uit\" of sleutel Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-instellinges",
        "ocr_language_btn": "Kies OCR-taal",
        "ocr_language": "OCR-taal(te)",
        "ocr_language_current": "Huidige taal:",
        "ocr_param_info": "Inligting oor parameter",

        "ocr_force_ocr_label": "Dwing OCR af",
        "ocr_deskew_label": "Korrigeer skuinsheid",
        "ocr_clean_label": "Suiwer beeld",
        "ocr_oversample_label": "Resolusie (DPI)",
        "ocr_pagesegmode_label": "Bladsy-indeling",
        "ocr_oem_label": "OCR-enjin-modus",
        "ocr_optimize_label": "PDF-kompressie",
        "ocr_jobs_label": "Parallele prosesse",
        "ocr_verbose_label": "Log-besonderhede",

        "ocr_force_ocr_tooltip": "Dwing OCR op elke bladsy af, selfs al is teks teenwoordig",
        "ocr_deskew_tooltip": "Rig skewe skanderings outomaties in",
        "ocr_clean_tooltip": "Verwyder geraas en artefakte uit die beeld",
        "ocr_oversample_tooltip": "Skaal beeld voor OCR op na hierdie DPI",
        "ocr_pagesegmode_tooltip": "Bepaal hoe die bladsy in teksareas verdeel word",
        "ocr_oem_tooltip": "Kies die OCR-enjin van Tesseract",
        "ocr_optimize_tooltip": "Kompressievlak van die uitvoer-PDF",
        "ocr_jobs_tooltip": "Aantal parallelle OCR-prosesse",
        "ocr_verbose_tooltip": "Besonderheidsvlak van log-uitvoer",
        "ocr_settings_explain_btn": "Verduideliking",

        "ocr_force_ocr_explain": "Dwing tekenherkenning op <b>elke</b> bladsy af, selfs al bevat dit reeds teks.\n\nAanbeveling: <b>Aan</b> vir geskandeerde PDF's, <b>Af</b> vir natuurlike PDF's met reeds bestaande teks.",
        "ocr_deskew_explain": "Korrigeer effens skewe skanderings (tot ongeveer 5°).\n\nAanbeveling: <b>Aan</b> vir geskandeerde dokumente, <b>Af</b> as bladsye reeds perfek reguit is.",
        "ocr_clean_explain": "Verwyder geraas, kolletjies en klein artefakte uit die beeld.\n<b>BELANGRIK:</b> Vir Arabiese, Thaise of Vietnamese tekste met diakritiese tekens (punte bo/onder letters) moet hierdie opsie <b>gedeaktiveer</b> word, anders kan belangrike karakters verlore gaan.",
        "ocr_oversample_explain": "Skaal die beeld <b>voor</b> tekenherkenning op na die gespesifiseerde DPI.<br><br>• <b>72-150 DPI:</b> Baie vinnig, maar lae herkenningskoers<br>• <b>200-300 DPI:</b> Optimale gebied (Standaard: 300)<br>• <b>400+ DPI:</b> Min beter herkenning, maar aansienlik groter lêers<br><br>Aanbeveling: 300 DPI vir komplekse skrifte (Arabies, Chinees, Japannees), 200 DPI vir Westerse tale.",
        "ocr_pagesegmode_explain": "Bepaal hoe Tesseract die bladsy in teksareas verdeel.\n\n• <b>3 - Outomaties (Standaard):</b> Goed vir gemengde uitlegte\n• <b>4 - Enkele kolom:</b> Vir enkelkolom-tekste\n• <b>5 - Vertikale blok:</b> Vir vertikale skrifte (Japannees, Chinees)\n• <b>6 - Eenvormige teksblok:</b> Optimaal vir deurlopende teks sonder kolomme\n• <b>11 - Rou beeld:</b> Vir swak skanderings / handskrifte\n\nAanbeveling: <b>6</b> vir eenvoudige teksdokumente, <b>3</b> vir komplekse uitlegte.",
        "ocr_oem_explain": "Kies die OCR-enjin van Tesseract.\n\n• <b>0 - Legacy:</b> Ou enjin (vinnig, maar minder akkuraat)\n• <b>1 - LSTM:</b> Neurale enjin (stadiger, maar akkurater)\n• <b>2 - Legacy + LSTM:</b> Kombineer beide resultate\n• <b>3 - Standaard (LSTM verkies):</b> Beste keuse vir die meeste gevalle\n\nAanbeveling: <b>3</b> vir maksimum herkenningsakkuraatheid.",
        "ocr_optimize_explain": "Komprimeer die uitvoer-PDF.\n\n• <b>0:</b> Geen optimalisering (vinnigste verwerking)\n• <b>1:</b> Ligte optimalisering (goeie kompromie)\n• <b>2:</b> Matige optimalisering\n• <b>3:</b> Sterk optimalisering (kleinste lêer, maar stadiger)\n\nAanbeveling: <b>1</b> vir daaglikse gebruik.",
        "ocr_jobs_explain": "Aantal parallelle prosesse vir OCR.\n\n• <b>1:</b> Stadig, maar laagste geheueverbruik\n• <b>4-8:</b> Optimaal vir moderne multi-kern verwerkers\n• <b>12+:</b> Min vinniger verwerking teen hoë geheueverbruik\n\nAanbeveling: Aantal SVE-kerns (bv. <b>4</b> op 4-kern stelsels).",
        "ocr_verbose_explain": "Besonderheidsvlak van log-uitvoer in die konsole.\n\n• <b>0:</b> Geen uitvoer\n• <b>1:</b> Vordering en statusberigte\n• <b>2:</b> Gedetailleerde uitvoer\n• <b>3:</b> Volledige ontfoutingsuitvoer (baie omvattend)\n\nAanbeveling: <b>1</b> vir normale werking.",

        "ocr_reset_title": "Instellinges teruggestel",
        "ocr_reset_message": "Alle OCR-instellinges is na die standaardwaardes teruggestel.",
        "info_tooltip": "Meer inligting oor hierdie parameter",
        "ocr_reset_defaults": "Stel terug na standaard",

        "ocr_psm_0": "Outomaties (Legacy-enjin)",
        "ocr_psm_1": "Outomatiese kolomopsporing",
        "ocr_psm_3": "Outomaties (Standaard)",
        "ocr_psm_4": "Enkele kolom",
        "ocr_psm_5": "Vertikale blok",
        "ocr_psm_6": "Eenvormige teksblok",
        "ocr_psm_7": "Enkele teksreël",
        "ocr_psm_8": "Enkele woord",
        "ocr_psm_11": "Rou beeld (geen uitleg-analise nie)",

        "ocr_oem_0": "Legacy-enjin (vinnig)",
        "ocr_oem_1": "LSTM-enjin (neuraal, akkuraat)",
        "ocr_oem_2": "Legacy + LSTM gekombineer",
        "ocr_oem_3": "Standaard (LSTM verkies)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-taal(te)...",
        "ocr_language_title": "Kies OCR-taal(te)",
        "ocr_language_instruction": "Kies die taal(te) vir tekenherkenning (OCR).\nLet wel: Meerdere tale gaan ten koste van werkverrigting en akkuraatheid!\nU behaal die beste resultate as u slegs een taal kies.",
        "ocr_language_predefined": "Voorafgedefinieerde kombinasies",
        "ocr_language_custom": "Pasgemaak...",
        "ocr_language_selected": "Geselekteerde OCR-tale",
        "ocr_language_changed": "OCR-taal verander na {0}",
        "ocr_language_auto_detect": "Beskikbare tale word outomaties opgespoor.",
        "ocr_language_none_found": "Geen Tesseract-taaldatums gevind nie! Installeer asseblief taalpakette (bv. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Pasgemaakte taal keuse",
        "ocr_language_available": "Beskikbare tale (geïnstalleer):",
        "ocr_language_select_hint": "Kies een of meer tale uit:",
        "ocr_language_confirm": "Neem oor",
        "ocr_language_reset": "Stel terug na standaard (deu+eng+vie)",
        "ocr_language_priorities": "Aanbevole tale (vooraf geïnstalleer):",

        "select_all_languages": "Kies alle",
        "clear_all_languages": "Maak keuse skoon",
        "install_language_packs": "Installeer ontbrekende taalpakette...",
        "install_hint": "💡 Wenk: Nie alle tale is op u stelsel geïnstalleer nie. Gebruik hierdie knoppie om hulp met installasie te kry.",
        "ocr_language_install_title": "Installasie van Tesseract-taalpakette",

        "ocr_missing_languages": "Ontbrekende OCR-taalpakette",
        "ocr_missing_languages_message": "Die volgende geselekteerde tale is nie op u stelsel geïnstalleer nie:\n\n{0}\n\nInstalleer asseblief die ontbrekende taalpakette (sien hulp by 'Installasiehulp').\n\nWil u die installasiehulp nou oopmaak?",
        "ocr_missing_languages_voice": "Ontbrekende taalpakette. Installeer asseblief die ontbrekende tale.",
        "ocr_install_help_now": "Maak hulp oop",
        "ocr_continue_anyway": "Probeer nietemin",
        "ocr_language_error_title": "OCR-taal fout",
        "ocr_language_error_message": "Fout met tekenherkenning: {0}\n\nGaan asseblief u OCR-taal instellinges na (Instellinges → OCR-taal).",
        "ocr_install_help_button": "Installasiehulp",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Installeer Tesseract-taalpakette</p>

        <p>Sodat OCR in 'n spesifieke taal kan werk, moet die ooreenstemmende taaldatums op u stelsel geïnstalleer wees. Volg die instruksies vir u bedryfstelsel:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Maak die <strong>Terminal</strong> oop (Finder → Programme → Nutsprogramme → Terminal).</li>
        <li>Installeer alle beskikbare tale met:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Dit kan 'n paar minute duur.)</li>
        <li>Of slegs enkele tale (bv. Viëtnamees):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Met huidige Homebrew-weergawes moet die <code>*.traineddata</code> moontlik handmatig afgelaai word (sien onder).</li>
        <li>Na installasie: Maak hierdie dialoog toe en maak die OCR-taalkeuse weer oop – die nuwe tale sal outomaties verskyn.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Maak 'n terminaal oop (Ctrl+Alt+T).</li>
        <li>Installeer die verlangde taal, bv. vir Viëtnamees:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Belangrike taalkodes: <code>deu</code> (Duits), <code>eng</code> (Engels), <code>vie</code> (Viëtnamees), <code>spa</code> (Spaans), <code>fra</code> (Frans), <code>ita</code> (Italiaans), <code>nld</code> (Nederlands), <code>fin</code> (Fins), <code>swe</code> (Sweeds), <code>nor</code> (Noors).</li>
        <li>Wys alle beskikbare pakette:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (handmatig)</p>
        <ol>
        <li>Laai die verlangde <code>*.traineddata</code>-lêers af van:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (bv. <code>vie.traineddata</code> vir Viëtnamees).</li>
        <li>Kopieer die lêers na die Tesseract-taalvouer, gewoonlik:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Pas aan by individuele installasie.)</li>
        <li>Herbegin die toepassing (of maak die OCR-taalkeuse weer oop).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatief vir alle stelsels</p>
        <ul>
        <li>Installeer <strong>OCRmyPDF</strong> en <strong>Tesseract</strong> met 'n pakketbestuurder na u keuse. Die meeste installasies bevat reeds 'n paar standaard tale (Engels, Duits, Frans).</li>
        <li>Ontbrekende tale kan te eniger tyd bygevoeg word – die OCR-taalkeuse lys slegs die tale wat werklik teenwoordig is.</li>
        </ul>

        <hr>
        <p><b>✅ Na installasie:</b> Geen herbegin van die toepassing nodig nie – die nuut bygevoegde tale sal dadelik in die lys verskyn.</p>
        <p><b>📖 Hulp met taalkodes:</b> 'n Volledige lys is beskikbaar in die <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract-dokumentasie</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans Lettertipes",
        "info_noto_font_voice": "Noto Sans Lettertipe Installasiegids",
        "btn_info_noto_font_install": "Font Inligting",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Hoe om die gratis Google Noto-lettertipes te installeer</h2>

        <p>Die <strong>Noto-lettertipes</strong> is 'n oopbron-lettertipefamilie van Google. Hul doel is om <em>"geen tofu"</em> (d.w.s. geen leë blokkies □) meer te sien nie en werklik elke karakter uit die Unicode-standaard korrek weer te gee. Hulle is die ideale aanvulling vir toepassings wat teks in baie verskillende tale moet vertoon.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installasie onder macOS</h3>

        <p><strong>Metode 1: Met Homebrew (vir gevorderdes)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metode 2: Via die "Font Book" (Aanbeveel)</strong></p>

        <ol>
        <li>Laai die amptelike lettertipe-pakket af:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pak die ZIP-lêer uit</li>
        <li>Kopieer lêers na <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installasie onder Windows (10 & 11)</h3>

        <p><strong>Metode 1: Microsoft Store (Aanbeveel)</strong><br>
        Soek vir "Google Noto Fonts" of "Noto Sans" en klik op <strong>Installeer</strong>.</p>

        <p><strong>Metode 2: Handmatige installasie</strong></p>

        <ol>
        <li>Aflaai:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pak ZIP uit</li>
        <li>Kies .ttf / .otf lêers</li>
        <li>Regskliek → <strong>Installeer</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        of<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Naam\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installasie onder Linux</h3>

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

        <p>Verifiëring:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Bestuur bladwysers",
        "bookmark_add": "Voeg bladwyser by",
        "bookmark_add_tooltip": "Stoor huidige bladsy as bladwyser",
        "bookmark_remove": "Verwyder bladwyser",
        "bookmark_remove_tooltip": "Verwyder die gemerkte bladwyser",
        "bookmark_remove_all": "Verwyder alle",
        "bookmark_remove_all_tooltip": "Verwyder alle bladwysers van hierdie PDF",
        "bookmark_jump": "Spring na bladwyser",
        "bookmark_jump_tooltip": "Spring na geselekteerde bladsy",
        "bookmark_name": "Naam",
        "bookmark_page": "Bladsy",
        "bookmark_no_bookmarks": "Geen bladwysers teenwoordig nie.\nKlik op 'Voeg by' om die huidige bladsy as bladwyser te stoor.",
        "bookmark_added": "Bladwyser vir bladsy {0} bygevoeg: {1}",
        "bookmark_removed": "Bladwyser verwyder: {0}",
        "bookmark_all_removed": "Alle bladwysers is verwyder.",
        "bookmark_name_default": "Bladsy {0}",
        "bookmark_name_prompt": "Naam vir die bladwyser:\n(langer teks word tot 50 karakters verkort)",
        "bookmark_name_prompt_title": "Bladwyser Naam",
        "bookmark_confirm_remove_all": "Is u seker u wil alle {0} bladwysers verwyder?",
        "menu_bookmarks": "Bladwysers",
        "bookmark_manage": "Bestuur bladwysers",
        "bookmark_next": "Volgende bladwyser",
        "bookmark_prev": "Vorige bladwyser",
        "bookmark_page_display": "Bladsy {0}",
        "bookmark_exists": "'n Bladwyser vir hierdie bladsy met hierdie naam bestaan reeds.",
        "bookmark_select_first": "Kies asseblief eers 'n bladwyser.",
        "bookmark_confirm_remove": "Is u seker u wil die bladwyser 'Bladsy {0}: {1}' verwyder?",
        "bookmark_jumped_to": "Na bladwyser '{0}' op bladsy {1} gespring.",
        "bookmark_jumped_to_voice": "Bladwyser {0}, bladsy {1}",
        "btn_close": "Sluit",

        "bookmark_list": "U bladwysers",
        "bookmark_rename": "Hernoem bladwyser",
        "bookmark_rename_tooltip": "Verander die naam van die geselekteerde bladwyser",
        "bookmark_rename_title": "Hernoem bladwyser",
        "bookmark_rename_prompt": "Nuwe naam vir bladwyser op bladsy {0}:\n(maks. 50 karakters)",
        "bookmark_renamed": "Bladwyser '{0}' is hernoem na '{1}'.",
        "bookmark_item_tooltip": "Bladsy {0}: {1}\nDubbelklik om te spring",
        "bookmark_name_exists_question": "'n Bladwyser met die naam '{0}' bestaan reeds op hierdie bladsy.\nHernoem nietemin?",

        "context_bookmarks": "Bladwysers",
        "context_bookmark_add_here": "Voeg bladwyser vir hierdie bladsy by",
        "context_bookmarks_existing": "Bestaande bladwysers:",
        "context_bookmarks_jump": "Spring na bladwyser:",
        "context_bookmarks_none": "Geen bladwysers teenwoordig",
        "context_bookmarks_clear_all": "Verwyder alle {0} bladwysers",

        "bookmark_search_placeholder": "Soek bladwysers... (naam of bladsy)",
        "bookmark_search_results": "%d bladwysers gevind vir \"%s\"",
        "bookmark_no_search_results": "Geen bladwysers gevind vir \"%s\"",
        "bookmark_no_search_results_label": "Geen resultate vir \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Wysig PDF-metadata",
        "metadata_title": "Titel",
        "metadata_title_placeholder": "Dokumenttitel",
        "metadata_title_tooltip": "Die titel van die dokument (word in die titelbalk vertoon)",
        "metadata_author": "Outeur",
        "metadata_author_placeholder": "Naam van die outeur",
        "metadata_author_tooltip": "Die skepper van die dokument",
        "metadata_subject": "Onderwerp",
        "metadata_subject_placeholder": "Onderwerp van die dokument",
        "metadata_subject_tooltip": "'n Kort beskrywing van die inhoud",
        "metadata_keywords": "Sleutelwoorde",
        "metadata_keywords_placeholder": "Sleutelwoorde, geskei deur kommas",
        "metadata_keywords_tooltip": "Sleutelwoorde vir kategorisering van die dokument",
        "metadata_creator": "Skepper",
        "metadata_creator_placeholder": "Toepassing wat die PDF geskep het",
        "metadata_creator_tooltip": "Die sagteware waarmee die dokument geskep is",
        "metadata_producer": "Produsent",
        "metadata_producer_placeholder": "Toepassing wat die PDF omgeskakel het",
        "metadata_producer_tooltip": "Die sagteware wat die PDF omgeskakel het",
        "metadata_creation_date": "Skeppingsdatum",
        "metadata_creation_date_tooltip": "Die datum van dokument skepping",
        "metadata_mod_date": "Wysigingsdatum",
        "metadata_mod_date_tooltip": "Die datum van laaste wysiging",
        "metadata_pdf_info": "📄 PDF-inligting",
        "metadata_pages": "Aantal bladsye",
        "metadata_file_size": "Lêergrootte",
        "metadata_pdf_version": "PDF-weergawe",
        "metadata_encrypted": "Geënkripteer",
        "metadata_encrypted_yes": "Ja (wagwoord beskerm)",
        "metadata_encrypted_no": "Nee",
        "metadata_reload": "📂 Herlaai vanaf PDF",
        "metadata_reset": "Gooi veranderinge weg",
        "metadata_reloaded": "Metadata is herlaai vanaf die PDF.",
        "metadata_reset_done": "Alle metadata-velde is teruggestel.",
        "metadata_no_file": "Geen PDF-lêer gelaai nie.",
        "metadata_save_error": "Fout met stoor van metadata",
        "metadata_saved": "Metadata is suksesvol gestoor.",
        "metadata_pdf_version_unknown": "PDF (onbekend)",
        "metadata_saved_message": "Die metadata is suksesvol gestoor.",
        "metadata_saved_voice": "Metadata gestoor.",

        "metadata_custom": "🔧 Pasgemaakte metadata",
        "metadata_custom_placeholder": "{\n  \"my_veld\": \"my waarde\",\n  \"ander_veld\": 123\n}",
        "metadata_custom_tooltip": "JSON-formaat vir pasgemaakte metadata (opsioneel)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Sjabloon \"{0}\" gekies - Dubbelklik om in te voeg",
        "text_use_template": "Gebruik teksblok",
        "text_type": "Tipe",
        "text_search_templates": "Soek teksblokke...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Uitvoer / Invoer Inligting",
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

        <h3>📦 Wat word uitgevoer? (Oorsig)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Algemene toepassingsinstellinges</span></li>
            <li class="detail">• Donker/Lig Modus</li>
            <li class="detail">• Donker-modus invertering vir beelde</li>
            <li class="detail">• Grys drempelwaarde</li>
            <li class="detail">• Taal</li>
            <li class="detail">• Venster geometrie</li>
            <li class="detail">• Zoem-modus</li>
            <li class="detail">• Navigasie (Navbaar sigbaar)</li>
            <li class="detail">• Spraakuitvoer (aan/af)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Instellinges vir rugsteun</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Lêerbenoeming (Tydstempel, Skeier, Agtervoegsels)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Instellinges vir invoegings van</span></li>
            <li class="detail">• Handtekeninge</li>
            <li class="detail">• Teks &amp; Teksblokke</li>
            <li class="detail">• Kruisies, beelde en vorms</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-instellinges</span></li>
            <li class="detail">• Taal</li>
            <li class="detail">• Dwing OCR af · Bladsymodus</li>
            <li class="detail">• Beeld voorverwerking: Skuinsheid korrigeer, Suiwering, Oormonstering</li>
            <li class="detail">• Aantal parallelle take</li>
            <li class="detail">• Inverteringsmodus</li>
            <li class="detail">• Grys drempelwaarde</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bladwysers</span></li>
            <li class="detail">• Alle bladwysers per PDF-lêer (Bladsy, Naam, Skeppingstyd)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Wagwoord-databasis</span></li>
            <li class="detail">• Gestoorde PDF-wagwoorde (opsioneel geënkripteer of gewone teks)</li>
            <li class="detail">• Meesterwagwoord-hasis (indien gestel)</li>
            <li class="detail">• Verifikasiedata</li>
        </ul>

        <h4>⚠️ Belangrike kennisgewings</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 By invoer:</strong>
            <ul>
                <li><span class="warning">➜ ALLE huidige instellinges word volledig oorskryf</span></li>
                <li>• 'n Herbegin van die toepassing is verpligtend</li>
                <li>• Bestaande handtekeninge, teksblokke en bladwysers word vervang</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Meesterwagwoord &amp; Uitvoermodus:</strong>
            <ul>
                <li>• Met aktiewe meesterwagwoord kan u kies:</li>
                <li>  - <span style="color: #98FB98;"><strong>Ontsleutel</strong></span> (Wagwoorde lê in gewone teks in die ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Geënkripteer</strong></span> (Slegs leesbaar met meesterwagwoord op die teikenstelsel)</li>
                <li>• Die meesterwagwoord-hasis self word <strong>altyd</strong> geënkripteer gestoor</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Sekuriteitskennisgewing:</strong>
            <ul>
                <li>• Die uitgevoerde ZIP-lêer bevat vertroulike data (<strong>wagwoorde, bladwysers, handtekeninge</strong>)</li>
                <li>• Bêre dit asseblief veilig (bv. geënkripteerde USB-stick, wagwoordbestuurder)</li>
                <li>• As die lêer verlore raak, is gestoorde PDF-wagwoorde onherroeplik verlore</li>
            </ul>
        </div>

        <h4>📁 Uitvoerformaat</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Die instellinges word in 'n enkele ZIP-lêer gestoor:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Hierdie ZIP bevat die volledige <code>settings.json</code> (uit u konfigurasie) asook moontlik ingebedde handtekening-beeldlêers en geënkripteerde wagwoorde.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Handtekeninge - Gids",
        'signature_guide_html': """
        📝 <strong>Handtekeninge - Vinnige Gids</strong><br>
        <ul>
        <li>Stel meesterwagwoord in</li>
        <li>Konfigureer handtekeninge in die <em>Instellings</em> kieslys (grootte, tydstempel, …)</li>
        <li>Voeg in met <strong>REGSKLIK</strong> op die gewenste posisie (meesterwagwoord eenmalig per sessie benodig)</li>
        <li>Skuiwe handtekening met muis of pyltjies</li>
        <li>Voeg verskeie handtekeninge na mekaar in</li>
        <li>Pas elke handtekening individueel aan</li>
        <li>Gooi enkele handtekening weg</li>
        <li>Stoor / gooi alle handtekeninge gelyktydig weg</li>
        <li>Alternatief kan die kieslysbalk ook gebruik word.</li>
        </ul>
        """,
        'signature_guide_voice': "Vinnige gids vir handtekeninge. Stel meesterwagwoord in. Konfigureer handtekeninge in instellings. Voeg in met regsklik.",

        'image_guide_title': "Beelde invoeg - Gids",
        'image_guide_html': """
        📷 <strong>Beelde in PDF invoeg - Vinnige Gids</strong><br>
        <ol>
        <li>Regsklik op die gewenste posisie</li>
        <li><em>„Beeld invoeg“</em> → Kies beeld</li>
        <li>Posisioneer beeld: Sleep met muis</li>
        <li>Pas grootte aan: Sleep aan die hoeke/rande</li>
        <li>Behou aspekverhouding: Sleutel <strong>[A]</strong></li>
        <li>Verdere aanpassings: Regsklik op die beeld</li>
        </ol>
        <p><strong>Wenk:</strong> In die kontekskieslys kan u die instellings aanpas.</p>
        """,
        'image_guide_voice': "Vinnige gids vir beelde. Regsklik, beeld invoeg, kies. Posisioneer met muis, pas grootte aan by hoeke. Aspekverhouding met sleutel A.",

        'form_guide_title': "Vorms invoeg - Gids",
        'form_guide_html': """
        📐 <strong>Vorms in PDF invoeg - Vinnige Gids</strong><br>
        <ol>
        <li>Kies vormtipe (reghoek, ellips, lyn, pyl)</li>
        <li>Klik op posisie:
            <ul>
            <li>By reghoek/ellips: Een klik plaas die vorm</li>
            <li>By lyn/pyl: Twee kliks vir begin- en eindpunt</li>
            </ul>
        </li>
        <li>Posisioneer vorm: Sleep met muis</li>
        <li>Pas grootte aan: Sleep aan die hoeke/rande</li>
        <li>Stoor vorm: <strong>Enter</strong></li>
        <li>Gooi vorm weg: <strong>ESC</strong></li>
        <li>Verdere aanpassings: Regsklik op die vorm</li>
        </ol>
        <p><strong>Wenk:</strong> In die kontekskieslys kan u die instellings aanpas.</p>
        """,
        'form_guide_voice': "Vinnige gids vir vorms. Kies vormtipe. By reghoek of ellips een keer klik, by lyn of pyl twee keer klik. Posisioneer met muis, pas grootte aan by hoeke. Stoor met Enter, weggooi met Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "vorige",
        "btn_next_result": "volgende",
        "ocr_text_window": "OCR teksvenster",
        "bookmark_existing": "Bestaande boekmerke",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR vergelyking Mac - Windows",
        'ocr_method_mac_win_title': "OCR verskille tussen Mac en Windows",
        'ocr_method_mac_win_voice': "Mac is beter",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Verskille tussen macOS en Windows</strong></p>

        <p><strong>macOS (aanbeveel)</strong></p>
        <p>Instrument:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Resultaat:</p>
        <ul>
        <li>'n Deursoekbare PDF met ingebedde teks wat die oorspronklike uitleg grotendeels behou.</li>
        </ul>
        <p>Voordele:</p>
        <ul>
        <li>Uitstekende kwaliteit van teksherkenning (selfs by skewe bladsye).</li>
        <li>Behoud van vektorgrafika en lettertipes.</li>
        <li>GUI vorderingsbalk via subproses evaluering.</li>
        <li>Volledige beheer oor alle OCR-parameters (Deskew, Clean, Oversample, optimering).</li>
        <li>Tekssoektog is direk beskikbaar in die hoofvenster (PDF aansig).</li>
        </ul>
        <p>Nadele:</p>
        <ul>
        <li>Benodig addisionele stelselinstrumente (ocrmypdf, Ghostscript, unpaper, pngquant – vervat in die toepassingsbundel).</li>
        <li>Komplekser foutafhandeling (deadlocks, time-outs).</li>
        </ul>

        <p><strong>Windows (stabiele alternatief)</strong></p>
        <p>Instrument:</p>
        <ul>
        <li>pytesseract (direkte koppeling met Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Resultaat:</p>
        <ul>
        <li>'n Deursoekbare PDF wat opties ooreenstem met 'n beeld-PDF, maar deursoekbaar is deur die deursigtige teks.</li>
        </ul>
        <p>Voordele:</p>
        <ul>
        <li>Daar kom nou nie een by my op nie.</li>
        </ul>
        <p>Nadele:</p>
        <ul>
        <li>Die PDF is in wese 'n beeld met onsigtbare teks; die uitleg kan by komplekse dokumente (kolomme, tabelle) effens afwyk.</li>
        <li>Geen outomatiese skuinsregstelling (--deskew) of beeldskoonmaak (--clean) nie.</li>
        <li>Die GUI vorderingsbalk word slegs grof opgedateer op grond van die aantal verwerkte bladsye.</li>
        <li>OCR-spoed is effens stadiger (omdat elke bladsy afsonderlik verwerk word).</li>
        <li>Tekssoektog word na die OCR teksvenster herlei.</li>
        </ul>

        <p><strong>Ooreenkomste</strong></p>
        <ul>
        <li>Beide prosesse lewer 'n deursoekbare PDF in dieselfde gids as die bronlêer.</li>
        <li>Die OCR-instellings (taal, DPI, bladsy-segmenteringsmodus, OCR-enjinmodus) kan via die OCRSettingsDialog gekonfigureer word en is van toepassing in beide implementasies.</li>
        </ul>

        <p><strong>Aanbeveling:</strong></p>
        <ul>
        <li>macOS: Die ocrmypdf-binêre lêer lewer die beste resultate – Koop vir u 'n Mac en gebruik die weergawe (PDFDarkView vir Mac's met Apple Silicon of Intel-skyfie). Die OCR-resultate is beter as onder Windows!</li>
        <li>Windows: Gebruik die pytesseract-oplossing. Dit is stabiel en lewer vir die meeste dokumente 'n heeltemal voldoende kwaliteit.</li>
        </ul>

        <p><strong>Belangrike kennisgewing:</strong></p>
        <ul>
        <li>Beide weergawes is ten volle in die gebruikerskoppelvlak geïntegreer – die gebruiker merk geen verskil nie.</li>
        <li>Die program neem outomaties die beslissing watter OCR-enjin gebruik word, gebaseer op die bedryfstelsel.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Skep handtekening (uit skandering)",
        "signature_create_title": "Kies geskandeerde handtekening (PDF/Beeld)",
        "image_pdf_filter": "Beelde en PDF",
        "signature_pdf_empty": "Die PDF bevat geen bladsye nie.",
        "signature_created_success": "Handtekening suksesvol geskep: {0}",
        "signature_create_error": "Fout tydens skep van handtekening:\n{0}",
        "rembg_missing": "rembg is nie geïnstalleer nie.\nInstalleer asseblief: pip install rembg\nFout: {0}",
        "signature_name_title": "Lêernaam vir handtekening",
        "signature_name_message": "Voer asseblief 'n lêernaam vir die nuwe handtekening in (word gestoor as PNG met deursigtige agtergrond):",
        "signature_name_label": "Lêernaam:",
        "signature_name_voice": "Voer lêernaam vir handtekening in",
        "signature_processing": "Verwerking besig...",
        "signature_creation_title": "Handtekening word geskep",
        "signature_overwrite_warning": "Die lêer '{0}' bestaan reeds. Oorskryf?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Berei PDF voor vir handtekening",
        "signature_prepare_instruction":"Kies asseblief 'n PDF wat op 'n enkele bladsy 'n geskandeerde handtekening bevat.\n\nOptimale herkenning word bereik as:\n• Die handtekening met swart ink (balpunt of fineliner) op wit papier geskryf is.\n• Die handtekening in die boonste derde van die andersins leë A4-bladsy is.\n• Die PDF teen minstens 300 dpi geskandeer is.\n• Die handtekening duidelik en nie te dun is nie.\n• Geen steurende agtergrondpatrone of lyne teenwoordig is nie.",
        "signature_prepare_voice":"Kies asseblief 'n PDF met 'n geskandeerde handtekening. Let op goeie kwaliteit en kontras.",
        "sig_thickness_label":"Lyn dikte:",
        "sig_thickness_normal":"Normaal (dun)",
        "sig_thickness_bold":"Kragtig (aanbeveel)",
        "sig_thickness_very_bold":"Baie kragtig",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Voeg GUI en OCR tale by - Gids",
        'language_guide_title': "Voeg GUI en OCR tale by",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Laai die verlangde vertalingslêer <code>translations_xy.py</code> af van<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        en plaas dit in die volgende gids:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Maak u webblaaier oop.</li>
        <li>Gaan na: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Soek regs op die skermrand na "Releases" en kies die een gemerk <strong>"latest"</strong>.</li>
        <li>Laai op die volgende vrystellingbladsy heel onder die lêer <code>Source Code.zip</code> af.</li>
        <li>Pak die ZIP-lêer uit.</li>
        <li>Soek in die uitgepakte gids al die taallêers wat u benodig, en kopieer hulle na die gids:<br/>
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
        "menu_watermark":"Watermerk invoeg",
        "fullpage_text_watermark_title":"Teks as watermerk",
        "fullpage_image_watermark_title":"Beeld as watermerk",
        "filename_with_watermark":"_met_watermerk",
        "watermark_text":"Teks:",
        "watermark_text_placeholder":"Jou watermerk-teks...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Fontgrootte:",
        "watermark_format":"Formatering:",
        "watermark_bold":"Vet",
        "watermark_italic":"Skuins",
        "watermark_color":"Kleur:",
        "watermark_choose_color":"Kies kleur...",
        "watermark_opacity":"Dekkrag / Deursigtigheid:",
        "watermark_direction":"Leesrigting:",
        "watermark_direction_l_r":"Links → Regs",
        "watermark_direction_bl_tr":"Onder links → Bo regs",
        "watermark_direction_tl_br":"Bo links → Onder",
        "watermark_direction_b_t":"Onder → Bo",
        "watermark_direction_t_b":"Bo → Onder",
        "watermark_preview":"Voorskou:",
        "watermark_preview_sample":"Voorbeeldteks",
        "watermark_empty_text":"Voer asseblief 'n teks in.",
        "watermark_applied":"Watermerk is op alle bladsye toegepas.",
        "watermark_saved":"Watermerk gestoor.",
        "image_scale":"Grootte:",
        "image_preview":"Beeldvoorskou:",
        "no_image_selected":"Geen beeld gekies nie",
        "browse":"Blaai...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Uitwissings",
        "redact_add_black": "Uitwissing (swart)",
        "redact_add_white": "Uitwissing (wit / uitvee)",
        "redact_added_black": "Swart uitwissing bygevoeg",
        "redact_added_white": "Wit uitwissing bygevoeg",
        "redact_apply_all": "Pas alle uitwissings toe en stoor",
        "redact_discard_all": "Gooi alle uitwissings weg",
        "redact_discard": "Gooi hierdie uitwissing weg",
        "no_redactions": "Geen uitwissings nie",
        "redact_confirm_title": "Pas uitwissings permanent toe",
        "redact_confirm_message": "Waarskuwing: Gemerkte areas sal onherroeplik verwyder word (swart of wit).\n'n Rugsteun sal geskep word (indien geaktiveer).\n\nGaan voort?",
        "redact_apply": "Ja, nou uitwis",
        "redact_saved": "{0} uitwissing(s) suksesvol toegepas en gestoor.",
        "redact_saved_voice": "{0} uitwissing(s) toegepas",
        "redact_error": "Fout tydens uitwissing",
        "filename_redacted":"_met_uitwissing",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Bladsynommers invoeg',
        'page_numbers_format': 'Nommerformaat:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arabies)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Romeins klein)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Romeins groot)',
        'page_numbers_format_letter': 'A, B, C ... (Letters)',
        'page_numbers_format_custom': 'Pasgemaak',
        'page_numbers_custom_pattern': 'Patroon:',
        'page_numbers_custom_placeholder': 'Bv. "Bladsy {nummer}" of "{nummer} / {totaal}"',
        'page_numbers_custom_tooltip': 'Gebruik {nummer} vir huidige bladsynommer en {totaal} vir totale aantal',
        'page_numbers_position': 'Posisie:',
        'page_numbers_pos_tl': 'Bo links',
        'page_numbers_pos_tc': 'Bo middel',
        'page_numbers_pos_tr': 'Bo regs',
        'page_numbers_pos_ml': 'Middel links',
        'page_numbers_pos_mc': 'Gesentreer',
        'page_numbers_pos_mr': 'Middel regs',
        'page_numbers_pos_bl': 'Onder links',
        'page_numbers_pos_bc': 'Onder middel',
        'page_numbers_pos_br': 'Onder regs',
        'page_numbers_margins': 'Kantlyne:',
        'page_numbers_margin_x': 'Horisontale afstand:',
        'page_numbers_margin_y': 'Vertikale afstand:',
        'page_numbers_range': 'Bladsyreeks:',
        'page_numbers_all_pages': 'Alle bladsye',
        'page_numbers_custom_range': 'Pasgemaakte reeks',
        'page_numbers_from': 'Van:',
        'page_numbers_to': 'Tot:',
        'page_numbers_progress': 'Bladsynommers invoeg...',
        'page_numbers_start': 'Begin bladsynommers-invoeging...',
        'page_numbers_cancel': 'Bladsynommers-invoeging gekanselleer',
        'page_numbers_success': 'Bladsynommers is suksesvol bygevoeg.\n\nWil u die nuwe PDF oopmaak?\n\n{0}',
        'page_numbers_complete': 'Bladsynommers is bygevoeg',
        'page_numbers_error_format': 'Fout tydens invoeg van bladsynommers: {0}',
        'page_numbers_content_type': 'Inhoudtipe:',
        'page_numbers_tab_simple': 'Eenvoudige nommer',
        'page_numbers_tab_range': 'Bladsy X van Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Vrye teks',
        'page_numbers_range_format': 'Formaat:',
        'page_numbers_range_short': '{huidig}/{totaal}',
        'page_numbers_range_long': 'Bladsy {huidig} van {totaal}',
        'page_numbers_range_custom': 'Pasgemaak',
        'page_numbers_range_placeholder': 'Bv. "Bladsy {huidig} / {totaal}"',
        'page_numbers_date_format': 'Datumformaat:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Januarie 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Pasgemaak',
        'page_numbers_date_placeholder': 'Bv. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Posisie:',
        'page_numbers_date_before': 'Datum voor bladsynommer',
        'page_numbers_date_after': 'Datum na bladsynommer',
        'page_numbers_date_only': 'Slegs datum (geen bladsynommer)',
        'page_numbers_custom_text': 'Pasgemaakte teks:',
        'page_numbers_custom_placeholder_text': 'Gebruik {seite} vir bladsynommer en {gesamt} vir totale aantal\nBv. "Vertroulik - Bladsy {seite}" of "{seite} van {gesamt}"',
        "filename_with_page_number":"_met_bladsynommer",
        "filename_with_page_declaration":"_met_bladsy_aanduiding",
        "filename_with_pagenumber":"_met_bladsynommer",
        "filename_with_date":"_met_datum",
        "filename_with_my_page_declaration":"_met_eie_bladsy_aanduiding",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Ongeopgegaarde veranderinge",
        "unsaved_changes_message_darkmode": "Daar is nog onopgegaarde invoegings.\nWil u dit stoor voor u oorskakel?",
        "save_and_switch": "Stoor en skakel om",
        "discard_and_switch": "Skakel nou om",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Bladsye as beelde uitvoer',
        'export_images_menu': 'As beelde uitvoer (PNG/JPEG)',
        'export_images_format': 'Beeldformaat:',
        'export_images_dpi': 'Resolusie (DPI):',
        'export_images_quality': 'JPEG-kwaliteit:',
        'export_images_range': 'Bladsyreeks:',
        'export_images_all_pages': 'Alle bladsye',
        'export_images_custom_range': 'Pasgemaakte reeks',
        'export_images_from': 'Van:',
        'export_images_to': 'Tot:',
        'export_images_options': 'Opsies:',
        'export_images_single_files': 'Elke bladsy as aparte lêer',
        'export_images_subfolder': 'Uitvoer na subgids',
        'export_images_subfolder_info': 'Na subgids "PDFnaam_beelde"',
        'export_images_same_folder': 'In dieselfde gids as die PDF',
        'export_images_apply_darkmode': 'Pas PDFDarkView-instellings toe (Donker Modus)',
        'export_images_target_folder': 'Teikengids:',
        'export_images_browse': 'Blaai...',
        'export_images_preview': 'Voorskou:',
        'export_images_preview_info': 'Kies instellings vir uitvoer',
        'export_images_preview_info_detail': '{0} bladsye as {1}\nResolusie: {2} DPI\nLêernaam: {3}\n{4}',
        'export_images_select_folder': 'Kies teikengids',
        'export_images_start': 'Begin beeld-uitvoer...',
        'export_images_progress': 'Beelde word uitgevoer...',
        'export_images_saving': 'Stoor bladsy {0} van {1}...',
        'export_images_success': 'Suksesvol uitgevoer!\n\n{0} beelde is gestoor in:\n{1}',
        'export_images_complete': 'Beeld-uitvoer voltooi',
        'export_images_open_folder': '📁 Maak gids oop',
        'export_images_cancel': 'Beeld-uitvoer gekanselleer',
        'export_images_error_format': 'Fout tydens uitvoer van beelde: {0}',
        'export_images_pdf2image_missing': 'Die biblioteek "pdf2image" is nie geïnstalleer nie.\n\nInstalleer dit asseblief met:\npip install pdf2image\n\nVir Windows benodig u ook Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A-omskakeling vir langtermyn-argivering',
        'pdfa_menu': 'PDF/A-omskakeling (argiveringsgereed)',
        'pdfa_info': 'Skakel die PDF om na PDF/A-formaat.\n\nPDF/A is spesifiek ontwikkel vir langtermyn-argivering en verseker dat die dokument in die toekoms korrek vertoon word.',
        'pdfa_standard': 'PDF/A-standaard:',
        'pdfa_standard_select': 'Weergawe:',
        'pdfa_1': 'PDF/A-1 (eenvoudig, wyd versoenbaar)',
        'pdfa_2': 'PDF/A-2 (modern, beter kompressie)',
        'pdfa_3': 'PDF/A-3 (nuutste weergawe, laat aanhangsels toe)',
        'pdfa_standards_explanation': '📖 Verduideliking van standaarde:\n\n'
            '• PDF/A-1: Basies, versoenbaar met ouer stelsels (ongeveer 2005)\n'
            '• PDF/A-2: Moderner, beter kompressie, deursigtigheid-ondersteuning (ongeveer 2011)\n'
            '• PDF/A-3: Nuutste weergawe, laat inbedding van lêeraanhangsels toe (ongeveer 2013)\n\n'
            'Aanbeveling: PDF/A-2 is \'n goeie kompromie tussen versoenbaarheid en moderne funksies.',
        'pdfa_options': 'Opsies:',
        'pdfa_compress_enable': 'PDF komprimeer (kleiner lêer)',
        'pdfa_metadata_preserve': 'Metadata behou (titel, outeur, ens.)',
        'pdfa_target_folder': 'Teikengids:',
        'pdfa_browse': 'Blaai...',
        'pdfa_select_folder': 'Kies teikengids',
        'pdfa_ocr_info_unknown': '🔍 Kon nie teksinhoud toets nie.',
        'pdfa_ocr_info_not_needed': '✅ Teks beskikbaar - OCR is nie nodig nie.\nPDF/A kan direk geskep word.',
        'pdfa_ocr_info_recommended': '⚠️ Geen voldoende teks gevind nie.\n\nVir deursoekbare PDF\'s beveel ons aan om eers OCR uit te voer.\nLet wel: PDF/A werk ook sonder OCR - maar die teks is dan nie deursoekbaar nie.',
        'pdfa_ocr_info_error': '❌ Fout tydens toets: {0}',
        'pdfa_start': 'Begin PDF/A-omskakeling...',
        'pdfa_progress': 'PDF/A-omskakeling aan die gang...',
        'pdfa_success': 'PDF/A-omskakeling suksesvol!\n\nGestoor as:\n{0}\n\nWil u die nuwe PDF oopmaak?',
        'pdfa_complete': 'PDF/A-omskakeling voltooi',
        'pdfa_cancel': 'PDF/A-omskakeling gekanselleer',
        'pdfa_error_format': 'Fout tydens PDF/A-omskakeling:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Die biblioteek "ocrmypdf" is nie geïnstalleer nie.\n\nInstalleer dit asseblief met:\npip install ocrmypdf',
        'btn_convert': 'Omskakeling',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF optimiseer (lêergrootte verminder)',
        'optimize_menu': 'PDF optimiseer (lêergrootte)',
        'optimize_info': 'Verminder die lêergrootte van die PDF deur verskeie optimeringsmetodes.\n\nHoe hoër die kompressievlak, hoe kleiner word die lêer - met moontlike kwaliteitsverlies by beelde.',
        'optimize_level': 'Kompressievlak:',
        'optimize_level_low': 'Laag (vinnig, geringe besparing)',
        'optimize_level_medium': 'Gemiddeld (goeie kompromie)',
        'optimize_level_high': 'Hoog (sterk besparing)',
        'optimize_level_maximum': 'Maksimum (maksimale besparing, stadig)',
        'optimize_level_explanation': 'Aanbeveling: "Gemiddeld" is \'n goeie kompromie tussen spoed en lêergrootte.',
        'optimize_options': 'Opsies:',
        'optimize_compress_images': 'Beelde komprimeer (JPEG-kwaliteit verminder)',
        'optimize_clean_objects': 'Ongebruikte voorwerpe verwyder',
        'optimize_preserve_metadata': 'Metadata behou (titel, outeur, ens.)',
        'optimize_image_quality': 'Beeldkwaliteit:',
        'optimize_range': 'Bladsyreeks:',
        'optimize_all_pages': 'Alle bladsye',
        'optimize_custom_range': 'Pasgemaakte reeks',
        'optimize_from': 'Van:',
        'optimize_to': 'Tot:',
        'optimize_target_folder': 'Teikengids:',
        'optimize_browse': 'Blaai...',
        'optimize_select_folder': 'Kies teikengids',
        'optimize_info_box': 'Inligting',
        'optimize_info_text': 'Optimasie kan by groot PDF\'s verskeie minute neem.\n\nBeelde word met verminderde kwaliteit gestoor, wat die lêergrootte aansienlik kan verminder.',
        'optimize_start': 'Begin PDF-optimasie...',
        'optimize_progress': 'PDF word geoptimeer...',
        'optimize_cancel': 'PDF-optimasie gekanselleer',
        'optimize_complete': 'PDF-optimasie voltooi',
        'optimize_error_format': 'Fout tydens PDF-optimasie:\n\n{0}',
        'optimize_success_message': 'PDF-optimasie suksesvol!\n\nGestoor as:\n{0}\n\nVoorheen: {1}\nNou: {2}\nBesparing: {3:.1f}%\n\n{4}\n\nWil u die geoptimeerde PDF oopmaak?',
        'optimize_success_message_no_size': 'PDF-optimasie suksesvol!\n\nGestoor as:\n{0}\n\nGroote-inligting nie beskikbaar nie.\n\nWil u die geoptimeerde PDF oopmaak?',
        'optimize_result_positive': 'Die lêer is met {0:.1f}% verklein.',
        'optimize_result_zero': 'Geen verandering in lêergrootte nie.',
        'optimize_result_negative': 'Die lêer is met {0:.1f}% groter geword.\nOptimasie is oorgeslaan, die oorspronklike lêer is behou.',
        'btn_optimize': 'Begin optimasie',
        'filename_optimize_low_suffix': '_geoptimeer_laag',
        'filename_optimize_medium_suffix': '_geoptimeer',
        'filename_optimize_high_suffix': '_geoptimeer_hoog',
        'filename_optimize_maximum_suffix': '_geoptimeer_maks',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF sny',
        'crop_menu': 'PDF sny (Crop)',
        'crop_range': 'Toepas op:',
        'crop_all_pages': 'Alle bladsye',
        'crop_current_page': 'Slegs huidige bladsy',
        'crop_values': 'Sny-waardes (in punte):',
        'crop_left': 'Links:',
        'crop_right': 'Regs:',
        'crop_top': 'Bo:',
        'crop_bottom': 'Onder:',
        'crop_presets': 'Voorinstellings:',
        'crop_preset_white': 'Wit rande opspoor',
        'crop_reset': 'Herstel',
        'crop_mouse_hint': '🖱️ Sleep \'n reghoek om die area rofweg te kies.\nDaarna kan u die waardes in die SpinBoxe presies aanpas.\nHandmatige aanpassing met die muis is nie moontlik nie.',
        'crop_apply': 'Sny',
        'crop_scope_all': 'Alle bladsye',
        'crop_scope_current': 'Huidige bladsy',
        'crop_new_size': 'Nuwe grootte: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Geen PDF gelaai nie',
        'crop_preview_error': 'Fout tydens laai van voorskou',
        'crop_start': 'Begin sny...',
        'crop_progress': 'PDF word gesny...',
        'crop_success': 'PDF suksesvol gesny!\n\nGestoor as:\n{0}\n\nWil u die gesnyde PDF oopmaak?',
        'crop_complete': 'Sny voltooi',
        'crop_cancel': 'Sny gekanselleer',
        'crop_error_format': 'Fout tydens sny:\n\n{0}',
        'filename_crop_suffix': '_gesny',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF gelyk maak (Flatten)',
        'flatten_menu': 'PDF gelyk maak (Flatten)',
        'flatten_info': 'Om \'n PDF gelyk te maak (Flatten) "brand" alle bewerkbare elemente in die bladsy-inhoud vas.\n\nDaarna is vormvelde, aantekeninge, tekste, kruisies, handtekeninge, beelde en vorms nie meer individueel bewerkbaar nie.',
        'flatten_explanation_title': '📖 Waarvoor is dit goed?',
        'flatten_explanation_text': 'Om gelyk te maak word in die volgende situasies benodig:\n\n'
            '• 📄 U wil die dokument voorberei vir druk\n'
            '• 🔒 U wil verhoed dat iemand vormvelde verander\n'
            '• 📎 U wil aantekeninge en kommentare "vas" in die dokument inbed\n'
            '• 🖼️ U wil ingevoegde tekste, kruisies, handtekeninge, beelde en vorms permanent in die dokument anker\n'
            '• 📦 U wil die lêer voorberei vir argivering\n\n'
            'Om gelyk te maak maak die PDF kleiner en verhoed dat elemente per ongeluk geskuif of verwyder word.',
        'flatten_what_title': 'Wat word gelyk gemaak?',
        'flatten_what_list': '• ✅ Vormvelde (teksvelde, merkblokkies, knoppies)\n'
            '• ✅ Aantekeninge (kommentare, beklemtonings, notas)\n'
            '• ✅ Oorleggings (tekste, kruisies, handtekeninge, beelde, vorms)',
        'flatten_options': 'Opsies:',
        'flatten_forms': 'Vormvelde gelyk maak',
        'flatten_annotations': 'Aantekeninge gelyk maak',
        'flatten_overlays': 'Oorleggings gelyk maak (tekste, kruisies, handtekeninge, beelde, vorms)',
        'flatten_target_folder': 'Teikengids:',
        'flatten_browse': 'Blaai...',
        'flatten_select_folder': 'Kies teikengids',
        'flatten_warning': '⚠️ Belangrik: Om gelyk te maak is \'n onomkeerbare proses!\n\nNa die gelyk-making kan bewerkbare elemente nie meer individueel verander of verwyder word nie.\nSkep indien nodig vooraf \'n rugsteun.',
        'flatten_apply': 'Gelyk maak',
        'flatten_start': 'Begin gelyk maak...',
        'flatten_progress': 'PDF word gelyk gemaak...',
        'flatten_success': 'PDF suksesvol gelyk gemaak!\n\nGestoor as:\n{0}\n\nWil u die gelykgemaakte PDF oopmaak?',
        'flatten_complete': 'Gelyk making voltooi',
        'flatten_cancel': 'Gelyk making gekanselleer',
        'flatten_error_format': 'Fout tydens gelyk making:\n\n{0}',
        'filename_flatten_suffix': '_gelykgemaak',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF oorlegging (Overlay)',
        'overlay_menu': 'PDF oorlegging (Overlay)',
        'overlay_info': 'Lê \'n PDF (oorlegging) oor \'n ander PDF.\n\nDie oorlegging-PDF word op die basis-PDF geplaas. Dit is nuttig vir watermerke, logo\'s, briefhoofde of stempels.',
        'overlay_explanation_title': '📖 Waarvoor is dit goed?',
        'overlay_explanation_text': 'Oorlegging word in die volgende situasies benodig:\n\n'
            '• 🏢 Plaas \'n maatskappy-logo as watermerk op elke bladsy\n'
            '• 📄 Plaas \'n briefhoof op \'n leë PDF\n'
            '• 🖊️ Plaas \'n stempel-oorlegging op \'n dokument\n'
            '• 🔖 Plaas \'n watermerk op alle bladsye\n'
            '• 📑 Plaas \'n vorm-oorlegging op \'n sjabloon',
        'overlay_type': 'Oorlegging-tipe:',
        'overlay_type_fullpage': 'Volledige bladsy (bedekkend)',
        'overlay_type_transparent': 'Volledige bladsy (deursigtig - aanbeveel)',
        'overlay_type_stamp': 'Stempel (posisioneerbaar)',
        'overlay_type_info_fullpage': '📄 Die oorlegging-PDF word presies oor die hele bladsy geplaas.\nDie wit agtergrond kan verwyder word sodat slegs die inhoud sigbaar bly.',
        'overlay_type_info_transparent': '🔍 Die oorlegging-PDF word met deursigtige agtergrond oor die hele bladsy geplaas.\nDie wit agtergrond word outomaties verwyder - ideaal vir watermerke en logo\'s!',
        'overlay_type_info_stamp': '🖊️ Die oorlegging-PDF word as stempel geposisioneer en geskaleer.\nPerfek vir logo\'s, stempels of handtekeninge op spesifieke posisies.',
        'overlay_remove_background': 'Verwyder wit agtergrond:',
        'overlay_remove_background_enable': 'Verwyder wit agtergrond van die oorlegging-PDF (maak die oorlegging deursigtig)',
        'overlay_remove_background_tooltip': 'Verwyder wit areas uit die oorlegging-PDF sodat die onderliggende teks sigbaar word.',
        'overlay_threshold': 'Drempelwaarde:',
        'overlay_threshold_hint': '(1-254, hoër = meer wit word verwyder)',
        'overlay_select_file': 'Kies oorlegging-PDF:',
        'overlay_file_placeholder': 'Kies asseblief \'n PDF-lêer vir die oorlegging',
        'overlay_browse': 'Blaai...',
        'overlay_select_overlay': 'Kies oorlegging-PDF',
        'overlay_range': 'Bladsyreeks:',
        'overlay_all_pages': 'Alle bladsye',
        'overlay_custom_range': 'Pasgemaakte reeks',
        'overlay_from': 'Van:',
        'overlay_to': 'Tot:',
        'overlay_position': 'Posisie:',
        'overlay_position_center': 'Middel',
        'overlay_position_top_left': 'Bo links',
        'overlay_position_top_right': 'Bo regs',
        'overlay_position_bottom_left': 'Onder links',
        'overlay_position_bottom_right': 'Onder regs',
        'overlay_size': 'Grootte:',
        'overlay_size_original': 'Oorspronklike grootte',
        'overlay_size_fit_page': 'Pas by bladsy',
        'overlay_size_custom': 'Pasgemaak (%)',
        'overlay_opacity': 'Deursigtigheid:',
        'overlay_target_folder': 'Teikengids:',
        'overlay_browse_folder': 'Blaai...',
        'overlay_select_folder': 'Kies teikengids',
        'overlay_warning': '⚠️ Let wel: Die oorlegging-PDF word op die basis-PDF geplaas en daarin "ingebrand".\n\nDie elemente van die oorlegging-PDF kan na stoor nie meer individueel bewerk word nie.',
        'overlay_apply': 'Oorlê',
        'overlay_start': 'Begin oorlegging...',
        'overlay_progress': 'PDF word oorlê...',
        'overlay_success': 'PDF suksesvol oorlê!\n\nGestoor as:\n{0}\n\nWil u die oorlêde PDF oopmaak?',
        'overlay_complete': 'Oorlegging voltooi',
        'overlay_cancel': 'Oorlegging gekanselleer',
        'overlay_error_format': 'Fout tydens oorlegging:\n\n{0}',
        'overlay_no_file': 'Geen oorlegging-PDF gekies nie.\n\nKies asseblief \'n PDF-lêer om oor te lê.',
        'filename_overlay_suffix': '_oorlê',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Beelde uit PDF onttrek',
        'extract_images_menu': 'Alle beelde onttrek',
        'extract_images_info': 'Onttrek alle beelde uit die PDF en stoor dit as aparte lêers.\n\nDie beelde word met hul oorspronklike formaat of in \'n gekose formaat omgeskakel.',
        'extract_images_format': 'Beeldformaat:',
        'extract_images_quality': 'JPEG-kwaliteit:',
        'extract_images_options': 'Opsies:',
        'extract_images_subfolder': 'Onttrek na subgids ("PDFnaam_beelde")',
        'extract_images_unique': 'Slegs unieke beelde (duplikate vermy)',
        'extract_images_range': 'Bladsyreeks:',
        'extract_images_all_pages': 'Alle bladsye',
        'extract_images_custom_range': 'Pasgemaakte reeks',
        'extract_images_from': 'Van:',
        'extract_images_to': 'Tot:',
        'extract_images_target_folder': 'Teikengids:',
        'extract_images_browse': 'Blaai...',
        'extract_images_select_folder': 'Kies teikengids',
        'extract_images_info_box': 'Inligting',
        'extract_images_info_text': 'Onttrekking kan by groot PDF\'s verskeie minute neem.\n\nBeelde word met hul oorspronklike naam (bladsy_beeld) gestoor.',
        'extract_images_extract': 'Onttrek',
        'extract_images_start': 'Begin onttrekking...',
        'extract_images_progress': 'Beelde word onttrek...',
        'extract_images_success': '✅ Beelde suksesvol onttrek!\n\n{0} beelde is gestoor in:\n{1}',
        'extract_images_complete': 'Beeld-onttrekking voltooi',
        'extract_images_cancel': 'Onttrekking gekanselleer',
        'extract_images_error_format': 'Fout tydens onttrekking van beelde:\n\n{0}',
        'extract_images_open_folder': '📁 Maak gids oop',
        'extract_images_no_images': 'Geen beelde in die PDF gevind nie.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Veelvuldige bladsye op een bladsy (N-Up)',
        'nup_menu': 'Veelvuldige bladsye op een bladsy (N-Up)',
        'nup_info': 'Rangskik verskeie PDF-bladsye op een bladsy.\n\nIdeaal vir kompakte afdrukke, oorsigte of handouts.',
        'nup_layout': 'Uitleg:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Voorskou:',
        'nup_preview_info': '{0} bladsye → {1} bladsye per vel → {2} velle\nUitleg: {3}',
        'nup_order': 'Volgorde:',
        'nup_order_horizontal': 'Horisontaal (rygewys)',
        'nup_order_vertical': 'Vertikaal (kolomgewys)',
        'nup_order_horizontal_reverse': 'Horisontaal agtertoe',
        'nup_order_vertical_reverse': 'Vertikaal agtertoe',
        'nup_range': 'Bladsyreeks:',
        'nup_all_pages': 'Alle bladsye',
        'nup_custom_range': 'Pasgemaakte reeks',
        'nup_from': 'Van:',
        'nup_to': 'Tot:',
        'nup_options': 'Opsies:',
        'nup_margins': 'Kantlyne:',
        'nup_margin_between': 'Afstand tussen bladsye:',
        'nup_page_numbers': 'Voeg bladsynommers in',
        'nup_target_folder': 'Teikengids:',
        'nup_browse': 'Blaai...',
        'nup_select_folder': 'Kies teikengids',
        'nup_create': 'Skep',
        'nup_start': 'Begin N-Up...',
        'nup_progress': 'N-Up word geskep...',
        'nup_success': 'N-Up suksesvol geskep!\n\nGestoor as:\n{0}\n\nWil u die nuwe PDF oopmaak?',
        'nup_complete': 'N-Up voltooi',
        'nup_cancel': 'N-Up gekanselleer',
        'nup_error_format': 'Fout tydens N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Bladsygrootte verander',
        'pagesize_menu': 'Bladsygrootte verander',
        'pagesize_info': 'Verander die bladsygrootte van die PDF.\n\nDie inhoud word outomaties by die nuwe grootte aangepas.',
        'pagesize_format': 'Formaat:',
        'pagesize_select': 'Kies \'n standaardformaat:',
        'pagesize_custom': 'Pasgemaakte grootte:',
        'pagesize_width': 'Breedte:',
        'pagesize_height': 'Hoogte:',
        'pagesize_orientation': 'Oriëntasie:',
        'pagesize_portrait': 'Portret',
        'pagesize_landscape': 'Landskap',
        'pagesize_scale_options': 'Skaal-opsies:',
        'pagesize_fit': 'Pas aan (behou aspekverhouding)',
        'pagesize_stretch': 'Rek (vervorm)',
        'pagesize_center': 'Sentreer (oorspronklike grootte)',
        'pagesize_range': 'Bladsyreeks:',
        'pagesize_all_pages': 'Alle bladsye',
        'pagesize_custom_range': 'Pasgemaakte reeks',
        'pagesize_from': 'Van:',
        'pagesize_to': 'Tot:',
        'pagesize_target_folder': 'Teikengids:',
        'pagesize_browse': 'Blaai...',
        'pagesize_select_folder': 'Kies teikengids',
        'pagesize_apply': 'Pas toe',
        'pagesize_start': 'Begin bladsygrootte-verandering...',
        'pagesize_progress': 'Bladsygrootte word verander...',
        'pagesize_success': 'Bladsygrootte suksesvol verander!\n\nGestoor as:\n{0}\n\nWil u die nuwe PDF oopmaak?',
        'pagesize_complete': 'Bladsygrootte-verandering voltooi',
        'pagesize_cancel': 'Bladsygrootte-verandering gekanselleer',
        'pagesize_error_format': 'Fout tydens verandering van bladsygrootte:\n\n{0}',
        'pagesize_preview_info': 'Nuwe grootte: {0} x {1} pt',
        'filename_pagesize_suffix': '_nuwegrootte',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-inligting',
        'pdf_info_menu': 'Wys PDF-inligting',
        'pdf_info_voice': 'PDF-inligting word vertoon',
        'pdf_info_error': 'Fout tydens vertoon van PDF-inligting:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Wys sleutelbordkortpaaie",
        "shortcuts_dialog_title": "Sleutelbordkortpaaie",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 LÊER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF oopmaak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF sluit</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Stoor as...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Dokument beskerm</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Druk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Druk onmiddellik (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Sluit toepassing af</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 UITVOER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Uitvoer as Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Uitvoer as DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Uitvoer as TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Uitvoer as beelde (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Beelde onttrek</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTVERWERKING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Veelvuldige bladsye)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A-omskakeling (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF gelyk maak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF oorlegging</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF optimeer</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDIGEER</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Soek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Voeg boekmerk by</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Bestuur boekmerke</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Volgende boekmerk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Vorige boekmerk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Voer OCR uit</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 BLADSYBESTUUR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Draai huidige bladsy</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Draai alle bladsye</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normaliseer huidige bladsy</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normaliseer alle bladsye</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Verwyder bladsye</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Onttrek bladsye</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Voeg bladsye in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Skuif bladsye</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Voeg PDF's saam</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Verander bladsygrootte</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 VOEG IN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Voeg teks in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Voeg kruisie in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Voeg handtekening 1 in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Voeg handtekening 2 in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Voeg beeld in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Voeg reghoek in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Voeg ellips in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Voeg lyn in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Voeg pyl in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Voeg bladsynommers in</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Teks-watermerk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Beeld-watermerk</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ UITWISSINGS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Uitwissing (swart)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Uitwissing (wit)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Pas alle uitwissings toe</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ GEVORDERD</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Sny PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Wysig metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ AANSIG</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Skakel Donker/Lig Modus om</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Wys teksvenster</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Bladsybreedte (Zoem)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Twee bladsye (Zoem)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Oorsig (Zoem)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ INSTELLINGS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Wagwoordbestuur</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR-instellings</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Handtekening-instellings</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Lêernaam-formatering</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Voer instellings uit</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Voer instellings in</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INLIGTING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Wys PDF-inligting</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Skakel spraakuitvoer aan/af</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokus kieslysbalk</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nuwe weergawe beskikbaar",
        "update_available_message": "Daar is 'n nuwe weergawe <b>{0}</b>.\n\nBesoek die vrystellingbladsy om die opdatering af te laai:\n{1}",
        "update_available_voice": "Nuwe weergawe {0} beskikbaar. Laai asseblief die opdatering van die GitHub-bladsy af.",
        "update_open_release": "Maak vrystellingbladsy oop",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Laai alle vertalings af",
        "ask_download_all_translations": """Benewens Duits, Engels en Viëtnamees is daar nog {total_languages} ander GUI-tale beskikbaar.\n\nMoet dit verskaf / opgedateer word?\n\nLet wel:\nOnnodige tale kan later in die gids:\n{translations_path}
        handmatig verwyder word.\n\nAs u kanselleer, kan die GUI-tale later via die spyskaart 'Nutsgoed → Vertalings opdateer' afgelaai word.""",
        "menu_update_translations": "Vertalings opdateer",
        "translations_updated": "Vertalings opgedateer",
        "translations_update_success": "{} vertalings is suksesvol opgedateer ({} nuut, {} opgedateer).",
        "translations_update_error": "Fout tydens opdatering van vertalings",
        "translations_update_no_changes": "Alle vertalings is reeds op datum.",
        "translations_update_offline": "Geen internetverbinding nie. Vertalings kon nie opgedateer word nie.",
        "translations_update_in_progress": "Vertalings word op die agtergrond opgedateer...",
        "translations_downloading": "Laai vertalings af...",
        "translations_path_hint": "Gebruikersgids vir vertalings",
        "translations_update_not_available_title": "Opdatering nie beskikbaar nie",
        "translations_update_not_available_message": """Die opdatering van vertalings is slegs in die geïnstalleerde weergawe beskikbaar.\n\nIn ontwikkelingsmodus is die vertalings reeds op datum.""",
        "translations_update_no_internet_title": "Geen internetverbinding nie",
        "translations_update_no_internet_message": """Geen internetverbinding kon gemaak word nie.\n\nDie vertalings kan nie van GitHub afgelaai word nie.\n\nMoontlike oplossings:
        • Kontroleer u internetverbinding
        • Deaktiveer 'n moontlike firewall tydelik
        • Probeer later weer
        \nU kan die vertalings ook handmatig van GitHub af laai:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Opdatering is reeds besig",
        "btn_retry": "Probeer weer",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Welkom by PDF Dark View",
        "welcome_title_not_supported": "Welkom by PDF Dark View",
        "welcome_message": "Welkom by PDF Dark View!\n\nU stelseltaal is as '{language}' herken.\nWil u hierdie taal vir die gebruikerskoppelvlak gebruik?\n\nU kan die taal enige tyd via 'Instellings → Taal' verander.",
        "welcome_message_language_not_available": "Welkom by PDF Dark View!\n\nU stelseltaal is as '{language}' herken.\nHierdie taal is tans nog nie geïnstalleer nie.\n\nWil u die vertalings vir {language} nou van GitHub af laai?\n\n(Die taal sal dan outomaties vir die gebruikerskoppelvlak gebruik word.)",
        "welcome_message_language_not_supported": "Welkom by PDF Dark View!\n\nU stelseltaal is as '{language}' herken.\nOngelukkig is daar tans nog geen vertalings vir hierdie taal nie.\n\nDie gebruikerskoppelvlak sal dus op {fallback_language} vertoon word.\n\nU kan die taal enige tyd via 'Instellings → Taal' verander.\nAs u wil, kan u ook self 'n vertaling vir u taal bydra:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Ja, gebruik stelseltaal",
        "welcome_keep_english": "Nee, behou Engels",
        "welcome_download_language": "Ja, laai {language} af",

        # ============================================
        # 107. ONLANGS GEBRUIKTE PADDE
        # ============================================

        'menu_recent': 'Onlangs gebruik',
        'menu_recent_dirs': 'Gidse...',
        'menu_recent_files': 'Lêers...',
        'recent_manage': 'Bestuur...',
        'recent_enable_tracking': 'Stoor onlangs gebruikte paaie (privaatheid)',
        'recent_enable_info': 'Skakel hierdie opsie af om geen paaie te stoor nie',
        'recent_tracking_disabled': 'Padopsporing gedeaktiveer',
        'recent_enabled': 'geaktiveer',
        'recent_disabled': 'gedeaktiveer',
        'recent_tracking_status': 'Padopsporing {0}',
        'recent_dialog_title': 'Onlangs gebruikte paaie',
        'recent_tab_directories': 'Gidse',
        'recent_tab_files': 'Lêers',
        'recent_dirs_instruction': 'Dubbelklik om lêerdialoog in gids te open',
        'recent_files_instruction': 'Dubbelklik om PDF direk te open',
        'recent_no_directories': '(geen gidse gestoor)',
        'recent_no_files': '(geen lêers gestoor)',
        'recent_default_current': '⭐ Standaard: {0}',
        'recent_set_as_default': '⭐ Stel as standaard',
        'recent_default_set_title': 'Standaardgids gestel',
        'recent_default_set_message': 'The directory "{0}" has been set as the default for opening PDFs.',
        'recent_default_set_voice': 'Standaardgids is gestel',
        'recent_directory_not_found': 'Gids nie gevind nie',
        'recent_file_not_found': 'Lêer nie gevind nie',
        'recent_remove_selected': 'Verwyder',
        'recent_remove_title': 'Verwyder pad',
        'recent_remove_confirm': 'Wil u die pad "{0}" werklik uit die lys verwyder?',
        'recent_path_removed': 'Pad is verwyder',
        'recent_clear_all': 'Verwyder alles',
        'recent_clear_title': 'Verwyder alle paaie',
        'recent_clear_confirm_type': 'Wil u werklik alle {0} verwyder?',
        'recent_cleared': 'Lys is skoongemaak',
        'recent_path_not_found_title': 'Pad nie gevind nie',
        'recent_path_not_found_message': 'Die pad "{0}" bestaan nie meer nie.',
        'recent_open_file': 'Open lêer',
        'btn_open_recent': 'Open',
        'recent_open_file_question': 'Wil u "{0}" as PDF open?',
        'recent_not_pdf': 'Die geselekteerde lêer is nie n PDF nie.',
        'recent_more_entries': 'Meer inskrywings...',
        'btn_remove': 'Verwyder',
        'btn_clear': 'Verwyder alles',
        'recent_context_open': 'Open',
        'recent_context_reveal': 'Wys in Vinder',
        'recent_context_set_default': '⭐ Stel as standaard',
        'recent_context_open_terminal': '💻 Open Terminal',
        'recent_context_file_info': 'Lêerinligting',
        'recent_context_open_with_default': '📄 Open met standaardtoepassing',
        'recent_context_remove': 'Verwyder uit lys',
        'recent_context_clear_all': 'Verwyder alles',
        'recent_file_info_title': 'Lêerinligting',
        'recent_file_info_name': 'Naam',
        'recent_file_info_path': 'Pad',
        'recent_file_info_size': 'Grootte',
        'recent_file_info_modified': 'Gewysig',
        'recent_file_info_pages': 'Bladsye',
        'recent_error_reveal': 'Fout by opening in Vinder',
        'recent_error_terminal': 'Fout by opening van Terminal',
        'recent_error_info': 'Fout by oproep van lêerinligting',
        'open_user_data_folder': 'Wys gebruikersdatagids',

        # ============================================
        # 108. VERWYDER GELYKE/ONGELYKKE BLADSYE
        # ============================================
        "pages_delete_even": "Verwyder alle gelyke bladsye",
        "pages_delete_odd":  "Verwyder alle ongelyke bladsye",
        "progress_even_pages": "Besig om gelyke bladsye te verwyder",
        "progress_odd_pages": "Besig om ongelyke bladsye te verwyder",
        "progress_mark_delete_even": "{} gelyke bladsy(e) gemerk vir verwydering",
        "progress_mark_delete_odd":  "{} ongelyke bladsy(e) gemerk vir verwydering",

        # ============================================
        # 109. SLUIT PROGRAM
        # ============================================
        "app_quitting": "Program word gesluit",
    }
