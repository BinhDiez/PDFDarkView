
# ============================================
# translations_cs.py - Český slovník
# Vollständig sortiert nach Kategorien
# ============================================

def load_czech_strings():
    """Lädt alle tschechischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Otevřít PDF",
        'btn_text_window': "Text OCR",
        'btn_first': "První stránka",
        'btn_prev': "Předchozí stránka",
        'btn_next': "Další stránka",
        'btn_last': "Poslední stránka",
        'btn_print': "Tisk",
        'btn_darkmode_light': "Světlý režim",
        'btn_darkmode_dark': "Tmavý režim",
        'btn_delete_pages': "Smazat stránky",
        'btn_extract_pages': "Extrahovat stránky",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Zrušit",
        'btn_save': "Uložit",
        'btn_close': "Zavřít",
        'btn_delete': "Smazat",
        'btn_delete_all': "Smazat vše",
        'btn_copy': "Kopírovat",
        'btn_export': "Exportovat",
        'btn_show': "Zobrazit heslo",
        'btn_hide': "Skrýt heslo",
        'btn_authenticate': "Ověřit",
        'btn_settings': "Nastavení",
        'btn_protect': "Chránit",
        'btn_remove_password': "Odstranit heslo",
        'btn_manage': "Správa hesel",
        'btn_retry': "Zkusit znovu",
        'btn_select_all': "Vybrat vše",
        'btn_clear_selection': "Zrušit výběr",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Stránka {0} z {1}",
        'page_count': "z {0}",
        'goto_page': "Přejít na stránku",
        'page_simple': "Stránka {0}",
        'full_view_page': "Plný náhled stránky {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Zadejte hledaný výraz + Enter",
        'search_results': "Výsledky: {0} z {1}",
        'search_nav_hint': "Enter: další (Shift+Enter: předchozí) výsledek",
        'search_no_results': "Žádné výsledky",
        'search_error': "Chyba vyhledávání",
        'search_active': "Vyhledávací pole aktivováno",
        'search_closed': "Vyhledávání ukončeno",
        'search_position': "Stránka {0} {1}",
        'search_pos_top': "úplně nahoře",
        'search_pos_upper': "nahoře",
        'search_pos_middle': "uprostřed",
        'search_pos_lower': "dole",
        'search_pos_bottom': "úplně dole",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Rozpoznávání textu úspěšně dokončeno!",
        'ocr_success_title': "OCR úspěšné",
        'ocr_success_message': "Dokument je nyní prohledávatelný.",
        'ocr_failed': "OCR selhalo",
        'ocr_in_progress': "Probíhá OCR",
        'ocr_preparing': "Připravuji PDF...",
        'ocr_analyzing': "Analyzuji PDF...",
        'ocr_optimizing': "Optimalizace obrázků...",
        'ocr_recognizing': "Rozpoznávání textu...",
        'ocr_embedding': "Vkládání textu...",
        'ocr_finalizing': "Finalizace PDF...",
        'ocr_not_available': "OCR není k dispozici",
        'ocr_install_message': "Nástroje OCR nebyly nalezeny.\n\nNainstalujte prosím:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR vyžadováno",
        'ocr_question': "PDF neobsahuje prohledávatelný text.\nChcete provést OCR pro umožnění {0}?",
        'ocr_perform': "Provést OCR",
        'ocr_later': "Později",
        'ocr_starting': "Spouštím garantované OCR...",
        'ocr_success_voice': "OCR úspěšné. PDF je nyní prohledávatelné.",
        'ocr_partial_success': "OCR bylo provedeno, ale při nahrazování došlo k problémům.\n\nProhledávatelná verze byla uložena do:\n{0}\n\nChyba: {1}",
        'ocr_partial_title': "OCR částečně úspěšné",
        'ocr_partial_voice': "OCR provedeno, ale nahrazení selhalo.",
        'original_file': "Původní soubor:",
        'old_size': "Stará velikost:    {0} bajtů",
        'new_size': "Nová velikost: {0} bajtů",
        'size_change': "Změna: {0}{1} bajtů",
        'backup_created_file': "Záloha vytvořena:\n{0}",
        'backup_not_created': "Záloha nevytvořena (vypnuto v nastavení)",
        'page_header': "=== Stránka {0} ===\n{1}\n",
        'scanned_page_header': "=== Stránka {0} (skenovaná) ===\n[Tato stránka obsahuje pouze skenovaný text]\n[Proveďte OCR ručně]\n",
        'scanned_warning': "⚠️ SKENOVANÝ TEXT - VYŽADUJE OCR",
        'guaranteed_title': "Vytvořeno prohledávatelné PDF",
        'guaranteed_message': "<b>Vytvořena garantovaná prohledávatelná verze!</b>\n\nProtože automatické OCR selhalo, byla vytvořena alternativní prohledávatelná PDF:\n\n{0}\n\n<b>Tento soubor obsahuje:</b>\n• Extrahovaný text (pokud existoval)\n• Pokyny pro skenované stránky\n• Je plně prohledávatelný",
        'guaranteed_voice': "Vytvořeno garantované prohledávatelné PDF.",
        'instruction_title': "NÁVOD PRO OCR",
        'instruction_file': "Původní soubor: {0}",
        'instruction_text': "Automatické rozpoznávání textu (OCR) selhalo.\nProveďte OCR ručně:\n\n1. S OCRmyPDF (příkazový řádek):\n   ocrmypdf --force-ocr \"[SOUBOR]\" \"vystup.pdf\"\n\n2. S ADOBE ACROBAT (macOS/Windows):\n   • Otevřete PDF v Acrobatu\n   • Nástroje > Upravit PDF\n   • Vyberte 'Rozpoznání textu'\n\n3. S PREVIEW (macOS):\n   • Otevřete PDF v náhledu\n   • Soubor > Exportovat...\n   • Filtr Quartz: 'Zmenšit velikost souboru'\n   • Povolit 'Provést OCR'\n\n4. ONLINE OCR SLUŽBY:\n   • smallpdf.com/cz/ocr-pdf\n   • ilovepdf.com/cz/ocr-pdf\n   • adobe.com/cz/acrobat/online/pdf-to-word.html",
        'instruction_created': "Vytvořen návod pro OCR",
        'instruction_created_message': "Podrobný návod byl vytvořen:\n\n{0}\n\nPostupujte podle kroků pro ruční OCR.",
        'instruction_created_voice': "Vytvořen návod pro OCR.",
        'ocr_impossible': "OCR není možné",
        'ocr_impossible_message': "OCR nelze provést.\n\nZpracujte '{0}' ručně pomocí OCR softwaru.",
        'ocr_impossible_voice': "OCR není možné. Zpracujte ručně.",
        'emergency_title': "Nouzové OCR",
        'emergency_message': "Bylo vytvořeno nouzové PDF:\n\n{0}\n\nZpracujte tento soubor ručně pomocí OCR.",
        'emergency_voice': "Vytvořeno nouzové PDF. Proveďte OCR ručně.",
        'critical_error': "Kritická chyba",
        'critical_error_message': "Nelze spustit OCR.\n\nRestartujte program a zkontrolujte instalaci OCR.",
        'critical_error_voice': "Kritická chyba OCR",
        'ocr_question_html': "<p>PDF neobsahuje prohledávatelný text.<p>Chcete provést OCR pro umožnění <b>{0}</b>?</p>",
        'ocr_question_voice': "Vyžadováno OCR. PDF neobsahuje prohledávatelný text. Chcete provést OCR pro umožnění {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "není načteno žádné PDF",
        'no_pdf_message': "Není načteno žádné PDF",
        'pdf_not_found': "PDF soubor nenalezen",
        'file_size': "Velikost souboru",
        'bytes': "bajtů",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Záloha vytvořena",
        'backup_disabled': "Zálohování vypnuto",
        'backup_activated': "Vytváření záloh zapnuto",
        'backup_deactivated': "Vytváření záloh vypnuto",
        'backup_status': "Záloha: {0}",
        'backup_on': "✔ zapnuto",
        'backup_off': "✘ vypnuto",
        'close_pdf': "Zavírám PDF: {0}",
        'pdf_not_found_format': "PDF soubor nenalezen: {0}",
        'error_pdf_load_format': "Chyba při načítání PDF: {0}",
        'load_failed_format': "Načítání selhalo:\n{0}",
        'decrypted_suffix': "(dešifrováno)",
        'decryption_failed': "Dešifrování selhalo.",
        'decryption_error': "Chyba při dešifrování",
        'decryption_success': "Úspěšně dešifrováno",
        'decryption_success_message': "PDF bylo dešifrováno a uloženo do:\n\n{0}",
        'decryption_success_voice': "PDF bylo dešifrováno a uloženo.",
        'password_remove_error': "Chyba při odstraňování hesla",
        'save_unencrypted': "Uložit nešifrované PDF jako",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Uložit jako...",
        'save_copy': "Uložit kopii",
        'save_success': "PDF uloženo do: {0}",
        'save_encrypted': "Chráněné PDF uloženo do: {0}",
        'save_error': "PDF nelze uložit",
        'encryption_question': "Chcete PDF chránit heslem?",
        'encryption_yes': "Ano",
        'encryption_no': "Ne",
        'encryption_cancel': "Zrušit",
        'save_cancel': "Ukládání zrušeno",
        'save_encrypted_voice': "Soubor zašifrován a uložen.",
        'save_success_voice': "Soubor PDF byl uložen nešifrovaný.",
        'save_error_format': "PDF nelze uložit:\n{0}",
        'export_pages_success': "Export do Pages úspěšný",
        'export_pages_error': "Export do Pages selhal",
        'export_pages_error_format': "Export do Pages selhal: {0}",
        'export_word_success': "Export do Wordu úspěšný",
        'export_word_error': "Export do Wordu selhal",
        'export_word_error_format': "Export do Wordu selhal: {0}",
        'export_text_success': "Export do textu úspěšný",
        'export_text_error': "Export do textu selhal",
        'export_text_error_format': "Export do textu selhal: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Heslo vyžadováno",
        'password_enter': "Zadejte heslo",
        'password_confirm': "Potvrďte heslo",
        'password_new': "Nové heslo",
        'password_current': "Aktuální heslo",
        'password_save': "Uložit heslo (šifrovaně)",
        'password_saved': "✓ Heslo pro tento soubor je uloženo",
        'password_wrong': "Nesprávné heslo",
        'password_mismatch': "Hesla se neshodují",
        'password_too_short': "Heslo je příliš krátké",
        'password_min_length': "Heslo musí mít alespoň 4 znaky",
        'password_strength': "Síla hesla",
        'password_strength_very_weak': "Velmi slabé",
        'password_strength_weak': "Slabé",
        'password_strength_medium': "Střední",
        'password_strength_strong': "Silné",
        'password_strength_very_strong': "Velmi silné",
        'password_char_count': "({0} znaků)",
        'password_match': "✓ Shoda",
        'password_no_match': "✗ Hesla se neshodují",
        'password_show': "Zobrazit",
        'password_hide': "Skrýt",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Správa hesel",
        'password_table_filename': "Název souboru",
        'password_table_password': "Heslo",
        'password_count': "{0} uložených hesel",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Žádná uložená hesla",
        'password_copied': "Zkopírováno {0} hesel",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Opravdu chcete smazat heslo pro '{0}'?",
        'password_delete_multiple': "Opravdu chcete smazat {0} vybraných hesel?",
        'password_delete_all_confirm': "Opravdu chcete smazat všech {0} uložených hesel?",
        'password_deleted': "Smazáno {0} hesel",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Všechna hesla byla smazána",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generátor hesel",
        'generator_generated': "Vygenerované heslo:",
        'generator_regenerate': "Vygenerovat znovu",
        'generator_copy': "Kopírovat",
        'generator_use': "Použít",
        'generator_settings': "Nastavení",
        'generator_length': "Délka:",
        'generator_group_every': "Oddělovač každých",
        'generator_group_chars': "znaků.    Oddělovač:",
        'generator_uppercase': "Velká písmena (A-Z)",
        'generator_lowercase': "Malá písmena (a-z)",
        'generator_digits': "Číslice (0-9)",
        'generator_symbols': "Speciální znaky (!@#$%^&*)",
        'generator_exclude': "Vyloučeno:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Hlavní heslo vyžadováno",
        'master_password_setup': "Nastavit hlavní heslo",
        'master_password_change': "Změnit hlavní heslo",
        'master_password_enter': "Zadejte své hlavní heslo",
        'master_password_choose': "Zvolte silné hlavní heslo (alespoň 8 znaků)",
        'master_password_new': "Zadejte své nové hlavní heslo",
        'master_password_confirm': "Potvrďte heslo",
        'master_password_authenticate': "Ověřit",
        'master_password_success': "Hlavní heslo bylo úspěšně nastaveno.",
        'master_password_changed': "Hlavní heslo bylo úspěšně změněno.",
        'master_password_removed': "Hlavní heslo a všechna hesla byla smazána.",
        'master_password_remove': "Odstranit hlavní heslo",
        'master_password_remove_confirm': "Jste si JISTÍ, že chcete smazat VŠECHNA hesla?\n\nTato akce je NEVRATNÁ!",
        'master_password_export_before': "Chcete předem exportovat záložní kopii?",
        'master_password_export_delete': "Exportovat a smazat",
        'master_password_delete_now': "Smazat nyní",
        'master_password_for_signatures': "Pro použití podpisů musíte nastavit hlavní heslo.\n\nChcete nyní nastavit hlavní heslo?",
        'master_password_for_private': "Pro použití soukromých textových bloků musíte nastavit hlavní heslo.\n\nChcete nyní nastavit hlavní heslo?",
        'master_password_info': """
            <b>🔐 BEZ HLAVNÍHO HESLA:</b><br>
            • Není možné zobrazovat, kopírovat a exportovat hesla<br>
            • Mazání hesel je vždy možné (i bez hlavního hesla)<br><br>

            <b>🔐 S HLAVNÍM HESLEM:</b><br>
            • Všechny funkce dostupné po ověření<br>
            • Hesla jsou šifrována hlavním heslem<br>
            • Minimální délka: 8 znaků<br>
            • Bezpečné ukládání hashů SHA-256<br><br>

            <b>DŮLEŽITÉ:</b><br>
            • Při ztrátě hlavního hesla: hesla nelze obnovit<br>
            • Při odstranění hlavního hesla: VŠECHNA hesla budou smazána<br>
            • Před smazáním je k dispozici možnost exportu<br>
            • Hlavní heslo lze kdykoli změnit
        """,
        'signature_auth_disabled': "Vypnout dotaz na heslo pro podpisy",
        'template_auth_disabled': "Vypnout dotaz na heslo pro soukromé textové bloky",
        'master_password_for_signatures_settings': "Pro použití podpisů musíte nastavit hlavní heslo.\n\nPřejděte do Nastavení - Správa hesel",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Chránit PDF",
        'protect_info': "Soubor '{0}' bude chráněn heslem.",
        'protect_instruction': "Zadejte dvakrát požadované heslo pro ochranu dokumentu, nebo použijte generátor hesel napravo od vstupního pole.",
        'protect_success': "PDF bylo úspěšně chráněno a uloženo do:\n{0}\n\nHeslo: {1}\n\nChcete nyní otevřít chráněné PDF?",
        'protect_open': "Ano",
        'protect_skip': "Ne",
        'protect_error': "Chyba při ochraně PDF",
        'protect_open_title': "otevřít chráněné PDF",
        'protect_question': "Hotovo. Chcete nyní otevřít chráněné PDF? Ano nebo Ne?",
        'password_cancel': "Dialog hesla zrušen",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Smazat stránky",
        'pages_extract': "Extrahovat stránky",
        'pages_insert': "Vložit stránky",
        'pages_move': "Přesunout stránky",
        'pages_delete_options': "Možnosti mazání",
        'pages_delete_empty': "Smazat všechny prázdné stránky",
        'pages_delete_current': "Smazat aktuální stránku",
        'pages_delete_range': "Smazat rozsah stránek",
        'pages_extract_options': "Možnosti extrakce",
        'pages_extract_current': "Extrahovat aktuální stránku",
        'pages_extract_range': "Extrahovat rozsah stránek",
        'pages_insert_position': "Místo vložení",
        'pages_insert_before': "Vložit před stránku:",
        'pages_insert_select': "Vybrat PDF",
        'pages_insert_none': "Není vybráno žádné PDF",
        'pages_move_source': "Stránky k přesunutí",
        'pages_move_from': "Od stránky:",
        'pages_move_to': "Do stránky:",
        'pages_move_target': "Cílové místo",
        'pages_move_before': "Přesunout před stránku:",
        'pages_move_hint': "Poznámka: stránka 1 = začátek, {0} = konec",
        'pages_range_invalid': "Počáteční stránka musí být menší nebo rovna koncové stránce.",
        'pages_position_invalid': "Cílové místo nesmí ležet v přesouvaném rozsahu.",
        'pages_no_pdf_selected': "Není vybráno žádné PDF.",
        'pages_deleted': "Bylo smazáno {0} stránek.",
        'pages_extracted': "Extrahováno: {0}\nUloženo do: {1}\nVelikost souboru: {2:.1f} KB",
        'pages_inserted': "Vloženo {0} stránek",
        'pages_moved': "Bylo přesunuto {0} stránek.",
        'pages_deleted_none': "Nebyly smazány žádné stránky.",
        'pages_delete_progress': "Mažu stránky...",
        'pages_deleted_with_backup': "Bylo smazáno {0} stránek.\n\nZáloha: {1}",
        'pages_deleted_voice': "Byla vytvořena záloha a smazáno {0} stránek.",
        'info': "Informace",
        'error_dialog_creation': "Nelze vytvořit dialog",
        'extract_page_single': "Extrahovat stránku {0}",
        'extract_page_range': "Extrahovat stránky {0}-{1}",
        'extract_success_voice': "Stránky úspěšně extrahovány",
        'extract_error_format': "Chyba při extrakci: {0}",
        'pages_inserted_voice': "Bylo vloženo {0} stránek.",
        'insert_error_format': "Chyba při vkládání: {0}",
        'pages_move_progress': "Přesouvám stránky...",
        'pages_moved_with_backup': "Bylo přesunuto {0} stránek.\n\nZáloha: {1}",
        'move_success_title': "Úspěšně přesunuto",
        'pages_moved_voice': "{0} stránek úspěšně přesunuto",
        'mark_removed': "Označení stránky {0} odstraněno",
        'mark_empty': "Stránka {0} označena jako prázdná",
        'mark_export_removed': "Označení exportu stránky {0} odstraněno",
        'mark_export': "Stránka {0} označena k exportu",
        'no_empty_pages': "Nejsou označeny žádné prázdné stránky k smazání",
        'delete_empty_confirm': "Chcete smazat všech {0} označených prázdných stránek?",
        'delete_empty_confirm_voice': "Smazat nyní všech {0} označených prázdných stránek? Ano nebo Ne.",
        'empty_pages_deleted': "Smazáno {0} prázdných stránek",
        'no_export_pages': "Nejsou označeny žádné stránky k exportu",
        'overwrite_title': "Přepsat existující soubor",
        'overwrite_question': "Soubor\n\n{0}\n\njiž existuje.\nChcete jej přepsat?",
        'overwrite_voice': "Přepsat existující soubor? Ano nebo Ne.",
        'page_skipped': "Stránka {0} byla přeskočena",
        'export_complete': "Export dokončen.",
        'export_complete_voice': "Export je dokončen.",
        'no_pages_exported': "Nebyla exportována žádná stránka",
        'export_cancelled': "Export zrušen",
        'pages_exported': "{0} stránek exportováno do {1}",
        'export_page_title': "Exportovat stránku",
        'page_exported': "Stránka {0} exportována do {1}",
        'export_error': "Chyba při exportu",
        'export_marked_title': "Exportovat označené stránky",
        'rotate_all_title': "otočit všechny stránky",
        'rotate_all_question': "Chcete otočit všechny stránky o 90 stupňů doprava?",
        'rotate_all_voice': "Chcete otočit všechny stránky o 90 stupňů doprava? Ano nebo Ne?",
        'all_pages_rotated': "Všechny stránky otočeny",
        'page_rotated': "Stránka {0} otočena",
        'rotate_error': "Stránku nelze otočit",
        'delete_page_confirm': "Chcete smazat stránku {0}?",
        'delete_page_confirm_voice': "Opravdu chcete smazat stránku {0}? Ano nebo Ne.",
        'page_deleted': "Stránka {0} smazána",
        'delete_error': "Stránku nelze smazat",
        'pages_deleted_voice': "Smazáno {0} stránek",
        'pages_exported_split': "{0} stránek bylo úspěšně exportováno.",
        'pages_skipped': "{0} stránek bylo přeskočeno.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extrahovat stránky (rozšířené)",
        'pdf_splitter_title': "Rozdělovač a extraktor PDF",
        'pdf_splitter_load': " Vybrat PDF soubor",
        'pdf_splitter_info': "Vyberte možnost pro váš PDF dokument",
        'pdf_splitter_basic': "Základní operace",
        'pdf_splitter_single': "Rozdělit na jednotlivé stránky",
        'pdf_splitter_range': "Extrahovat stránky:",
        'pdf_splitter_range_placeholder': "např. 1-3,5,7-9",
        'pdf_splitter_clean': "Čisticí operace",
        'pdf_splitter_remove_empty': "Odstranit všechny prázdné stránky",
        'pdf_splitter_remove': "Smazat rozsah stránek:",
        'pdf_splitter_remove_placeholder': "např. 2,4-6",
        'pdf_splitter_process': "Zpracovat PDF",
        'pdf_splitter_loaded': "PDF načteno. Vyberte možnost",
        'pdf_read_error': "PDF nelze přečíst",
        'pages': "Stránky",
        'pages_created': "Stránky byly vytvořeny",
        'range_empty': "Zadejte rozsah stránek",
        'range_invalid': "Neplatný rozsah stránek",
        'range_created': "Bylo vytvořeno nové PDF s vybranými stránkami:\n{0}",
        'empty_removed': "Odstraněno {0} prázdných stránek.\nVýstup: {1}",
        'remove_empty': "Zadejte stránky k odstranění",
        'remove_invalid': "Neplatné stránky k odstranění",
        'remove_done': "Vyčištěné PDF vytvořeno:\n{0}",
        'open_folder': "Otevřít složku",
        'show_in_finder': "Zobrazit ve Finderu",
        'pdf_splitter_no_pdf': "Nejprve načtěte PDF soubor.",
        'process_error': "Chyba při zpracování PDF",
        'pages_created_voice': "Vytvořeno {0} stránek",
        'range_created_voice': "Vytvořeno PDF s vybranými stránkami",
        'empty_removed_voice': "Odstraněno {0} prázdných stránek",
        'remove_done_voice': "Vyčištěné PDF vytvořeno",
        'pdf_splitter_split_groups': "Každá souvislá skupina do samostatného souboru",
        'range_created_single': "Vytvořeno nové PDF:\n{0}",
        'range_created_multiple': "Vytvořeno {0} PDF souborů.",
        'range_created_voice_single': "Vytvořeno jedno PDF s vybranými stránkami",
        'range_created_voice_multiple': "Vytvořeno {0} PDF souborů",
        'empty_removed_none_left': "Žádné zbývající stránky",
        'empty_removed_all_empty': "Všechny stránky byly rozpoznány jako prázdné a byly by odstraněny. Nebyl vytvořen žádný soubor.",
        'preview_single': "Náhled: {0}",
        'preview_enter_range': "Zadejte rozsah stránek.",
        'preview_invalid_range': "Neplatný rozsah stránek.",
        'preview_file': "Náhled: {0}",
        'preview_files': "Náhled: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Spouštím tisk",
        'print_sent': "Tisková úloha odeslána",
        'print_now': "Tisknout nyní",
        'print_error': "Chyba při okamžitém tisku",
        'print_limited': "Funkce tisku na tomto systému omezena",
        'print_error_format': "Chyba při okamžitém tisku: {0}",
        'warning': "Upozornění",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Přepnout do světlého režimu",
        'mode_switch_to_dark': "Přepnout do tmavého režimu",
        'mode_dark_activated': "Tmavý režim aktivován",
        'mode_light_activated': "Světlý režim aktivován",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Plný náhled",
        'zoom_two_pages': "Dvě stránky vedle sebe",
        'zoom_overview': "Režim přehledu",
        'zoom_cannot_during_search': "Zoom není možné během vyhledávání",
        'zoom_exit_first': "Nejprve ukončete zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop povolen",
        'drag_disabled': "Drag & Drop zakázán",
        'drag_page_grab': "Stránka {0} uchopena",
        'drag_page_dropped': "Stránka {0} vložena na pozici {1}",
        'drag_position_invalid': "Neplatná pozice",
        'drag_same_position': "Stránka {0} zůstává na pozici {0}",
        'drag_error': "Chyba při přesouvání",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Vstup textu s rozšířeným formátováním a správou textových bloků",
        'text_templates': "Dostupné textové bloky:",
        'text_name': "Název",
        'text_preview': "Náhled textu",
        'text_enter': "Text:",
        'text_font_size': "Velikost písma:",
        'text_formatting': "Formátování:",
        'text_bold': "Tučné",
        'text_italic': "Kurzíva",
        'text_underline': "Podtržené",
        'text_alignment': "Zarovnání:",
        'text_left': "Vlevo",
        'text_center': "Na střed",
        'text_right': "Vpravo",
        'text_color': "Barva textu:",
        'text_opacity': "Krytí:",
        'text_word_wrap': "Zalamování řádků:",
        'text_auto': "Automatické",
        'text_page_width_95': "Šířka stránky (95%)",
        'text_page_width_85': "Velmi široké (85%)",
        'text_page_width_75': "Širší (75%)",
        'text_page_width_60': "Široké (60%)",
        'text_page_width_50': "Střední (50%)",
        'text_page_width_30': "Úzké (30%)",
        'text_page_width_20': "Užší (20%)",
        'text_page_width_10': "Velmi úzké (10%)",
        'text_no_wrap': "Bez zalamování",
        'text_private': "Soukromý textový blok (vyžaduje ověření)",
        'text_preview_label': "Náhled:",
        'text_preview_placeholder': "Zde se zobrazí náhled textu...",
        'text_no_text': "(Žádný text)",
        'text_save_template': "💾 Uložit jako blok",
        'text_delete_template': "🗑 Smazat vybraný textový blok",
        'text_show_private': "Zobrazit soukromé",
        'text_hide_private': "Skrýt soukromé",
        'text_use': "✅ Použít text",
        'text_saved': "Textový blok uložen jako:\n{0}",
        'text_saved_voice': "Textový blok uložen",
        'text_deleted': "Textový blok smazán",
        'text_no_text_to_save': "Žádný text k uložení.",
        'text_no_templates': "Nenalezeny žádné textové bloky",
        'text_private_master_required': "Soukromé bloky lze použít pouze tehdy, je-li nastaveno hlavní heslo.\n\nChcete nyní nastavit hlavní heslo?",
        'text_filename': "Název souboru pro textový blok (bez 'Text_' a '.txt'):",
        'text_filename_hint': "Příklad: 'Telefon HomeOffice' se uloží jako 'Text_Telefon HomeOffice.txt'",
        'text_save_hint': "Textový blok bude automaticky uložen s formátováním.",
        'text_guide_title': "Vstup textu - Návod",
        'text_delete_confirm': "Opravdu chcete smazat textový blok?\n\nSoubor: {0}\nText: {1}...",
        'text_make_public': "Označit jako veřejné",
        'text_make_private': "Označit jako soukromé",
        'text_privacy_changed': "Změněn stav soukromí",
        'text_private_always': "Soukromé vždy viditelné (nastavení)",
        'text_mode_required': "Nejprve aktivujte režim textu",
        'text_continue_editing': "Pokračovat v úpravách - kurzor na konci textu",
        'text_no_input': "Nebyl zadán žádný text - text zahozen",
        'save_dialog_question': "Jak chcete pokračovat?",
        'text_save_question': "Uložit všechny texty a křížky, upravit, pokračovat v úpravách nebo zahodit?",
        'copy_cross': "Křížek zkopírován",
        'paste_cross': "Křížek vložen",
        'paste_text': "Text vložen",
        'cross_discarded': "Křížek zahozen",
        'all_discarded': "Vše zahozeno",
        'text_discarded': "Text zahozen",
        'no_texts_to_save': "Žádné texty k uložení",
        'no_valid_texts': "Žádné platné texty k uložení",
        'text_word_singular': "text",
        'text_word_plural': "texty",
        'cross_word_singular': "křížek",
        'cross_word_plural': "křížky",
        'texts_saved_title': "Texty uloženy",
        'texts_crosses_saved': "{0} {1} a {2} {3} bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'texts_crosses_saved_voice': "Uloženo {0} {1} a {2} {3}.",
        'texts_saved': "{0} {1} bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'texts_saved_voice': "Uloženo {0} {1}.",
        'crosses_saved': "{0} {1} bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'crosses_saved_voice': "Uloženo {0} {1}.",
        'elements_saved': "{0} prvků bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'elements_saved_voice': "Uloženo {0} prvků.",
        'text_window_load_error': "Nelze načíst okno textu",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Vstup textu a textové bloky – Podrobný návod**

        **1. Vložení a úprava textu**
        - Klepněte pravým tlačítkem myši na požadované místo v dokumentu a zvolte "Vložit text".
        - Otevře se dialogové okno, ve kterém můžete zadat text a formátovat jej:
        • Velikost písma, tučné, kurzíva, podtržení
        • Barva textu (libovolná)
        • Průhlednost (krytí) pomocí posuvníku
        • Zalamování řádků (různé šířky, např. šířka stránky, úzké, bez zalamování)
        - Po potvrzení se text objeví v místě klepnutí. Můžete jej přesouvat myší nebo klávesami se šipkami.
        - Dvojité kliknutí na text otevře režim úprav; ESC jej ukončí.

        **2. Správa textových bloků (šablon)**
        - V dialogu textu vlevo vidíte seznam všech uložených textových bloků.
        - **Uložení bloku:** Zadejte text, naformátujte jej a klepněte na "💾 Uložit jako blok". Zadejte název souboru (bez přípony).
        - **Načtení bloku:** Klepněte na požadovaný název v seznamu. Text a formátování se převezmou a lze je podle potřeby upravit.
        - **Smazání:** Klepněte pravým tlačítkem na blok, můžete jej smazat nebo změnit jeho stav soukromí.

        **3. Soukromé textové bloky (hlavní heslo)**
        - Pokud jste nastavili hlavní heslo (v Nastavení → Správa hesel), můžete bloky označit jako "soukromé".
        - Zaškrtněte políčko "Soukromý textový blok" v dialogu před uložením.
        - Soukromé bloky se v seznamu zobrazí pouze po jednorázovém ověření hlavním heslem v dané relaci (ověření přes ikonu zámku nebo při prvním přístupu).
        - Tímto způsobem můžete chránit důvěrné textové bloky před neoprávněným přístupem.

        **4. Vkládání křížků**
        - Z kontextové nabídky můžete také vložit grafický křížek (např. pro zaškrtávací políčka).
        - Velikost, tloušťku čáry a barvu křížků lze globálně upravit v nastavení (menu "Nastavení" → "Nastavení křížků").
        - Klepněte pravým tlačítkem na existující křížek pro jeho individuální úpravu.

        **5. Hromadné akce**
        - Pokud jste na jednu stránku umístili více textů nebo křížků, můžete je všechny najednou uložit nebo zahodit z kontextové nabídky (pravým tlačítkem v režimu textu).
        - Při ukládání se všechny prvky vloží do PDF a zůstanou jako vektorová grafika.

        **6. Klávesové zkratky v režimu textu**
        - Šipky: přesun prvku
        - Ctrl+šipky: větší kroky
        - Enter: otevření dialogu pro uložení (uložit vše / upravit / zahodit)
        - ESC: zahodit aktuální prvek
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Vstup textu a textové bloky – Podrobný návod</strong></p>

        <p><strong>1. Vložení a úprava textu</strong></p>
        <ul>
        <li>Klepněte pravým tlačítkem myši na požadované místo v dokumentu a zvolte "Vložit text".</li>
        <li>Otevře se dialogové okno, ve kterém můžete zadat text a formátovat jej:<br/>
        • Velikost písma, tučné, kurzíva, podtržení<br/>
        • Barva textu (libovolná)<br/>
        • Průhlednost (krytí) pomocí posuvníku<br/>
        • Zalamování řádků (různé šířky, např. šířka stránky, úzké, bez zalamování)</li>
        <li>Po potvrzení se text objeví v místě klepnutí. Můžete jej přesouvat myší nebo klávesami se šipkami.</li>
        <li>Dvojité kliknutí na text otevře režim úprav; ESC jej ukončí.</li>
        </ul>

        <p><strong>2. Správa textových bloků (šablon)</strong></p>
        <ul>
        <li>V dialogu textu vlevo vidíte seznam všech uložených textových bloků.</li>
        <li><strong>Uložení bloku:</strong> Zadejte text, naformátujte jej a klepněte na "💾 Uložit jako blok". Zadejte název souboru (bez přípony).</li>
        <li><strong>Načtení bloku:</strong> Klepněte na požadovaný název v seznamu. Text a formátování se převezmou a lze je podle potřeby upravit.</li>
        <li><strong>Smazání:</strong> Klepněte pravým tlačítkem na blok, můžete jej smazat nebo změnit jeho stav soukromí.</li>
        </ul>

        <p><strong>3. Soukromé textové bloky (hlavní heslo)</strong></p>
        <ul>
        <li>Pokud jste nastavili hlavní heslo (v Nastavení → Správa hesel), můžete bloky označit jako "soukromé".</li>
        <li>Zaškrtněte políčko "Soukromý textový blok" v dialogu před uložením.</li>
        <li>Soukromé bloky se v seznamu zobrazí pouze po jednorázovém ověření hlavním heslem v dané relaci (ověření přes ikonu zámku nebo při prvním přístupu).</li>
        <li>Tímto způsobem můžete chránit důvěrné textové bloky před neoprávněným přístupem.</li>
        </ul>

        <p><strong>4. Vkládání křížků</strong></p>
        <ul>
        <li>Z kontextové nabídky můžete také vložit grafický křížek (např. pro zaškrtávací políčka).</li>
        <li>Velikost, tloušťku čáry a barvu křížků lze globálně upravit v nastavení (menu "Nastavení" → "Nastavení křížků").</li>
        <li>Klepněte pravým tlačítkem na existující křížek pro jeho individuální úpravu.</li>
        </ul>

        <p><strong>5. Hromadné akce</strong></p>
        <ul>
        <li>Pokud jste na jednu stránku umístili více textů nebo křížků, můžete je všechny najednou uložit nebo zahodit z kontextové nabídky (pravým tlačítkem v režimu textu).</li>
        <li>Při ukládání se všechny prvky vloží do PDF a zůstanou jako vektorová grafika.</li>
        </ul>

        <p><strong>6. Klávesové zkratky v režimu textu</strong></p>
        <ul>
        <li>Šipky: přesun prvku</li>
        <li>Ctrl+šipky: větší kroky</li>
        <li>Enter: otevření dialogu pro uložení (uložit vše / upravit / zahodit)</li>
        <li>ESC: zahodit aktuální prvek</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Nastavení křížků",
        'cross_properties': "Vlastnosti křížku",
        'cross_size': "Velikost (px):",
        'cross_line_width': "Tloušťka čáry:",
        'cross_color': "Barva:",
        'cross_choose_color': "Vybrat",
        'cross_fine_tuning': "Doladění při ukládání (pixely)",
        'cross_offset_x': "Posun X:",
        'cross_offset_y': "Posun Y:",
        'cross_offset_x_tooltip': "Záporné hodnoty posouvají křížek při ukládání doleva, kladné doprava",
        'cross_offset_y_tooltip': "Záporné hodnoty posouvají křížek při ukládání nahoru, kladné dolů",
        'cross_preview': "Náhled",
        'cross_save': "Použít nastavení",
        'cross_customized': "Křížek upraven",
        'cross_settings_applied': "Nastavení křížků uloženo.\nVelikost: {0}px, tloušťka čáry: {1}px\n{2}",
        'cross_updated_count': "Aktualizováno {0} existujících křížků.",
        'cross_no_crosses': "Nenalezeny žádné existující křížky.",
        'cross_settings_applied_all': "Nastavení křížků aplikováno na všech {0} křížků",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Nastavení podpisů",
        'signature_1': "Podpis 1",
        'signature_2': "Podpis 2",
        'signature_select': "Vybrat podpis",
        'signature_add': "➕ Přidat nový podpis...",
        'signature_size': "Velikost podpisu {0} (%):",
        'signature_common': "Obecná nastavení",
        'signature_timestamp': "Automaticky přidat časové razítko",
        'signature_location': "Výchozí místo:",
        'signature_timestamp_size': "Velikost písma časového razítka:",
        'signature_no_files': "-- Nebyly nalezeny žádné podpisy --",
        'signature_insert': "Vložit podpis",
        'signature_insert_1': "Vložit podpis 1",
        'signature_insert_2': "Vložit podpis 2",
        'signature_customize': " Přizpůsobit podpis",
        'signature_discard': " Zahodit tento podpis",
        'signature_save_all': " Uložit všechny podpisy",
        'signature_discard_all': " Zahodit všechny podpisy",
        'signature_guide_title': "Podpisy - Návod",
        'signature_guide': """
📝 Podpisy - Stručný návod

- Nastavte hlavní heslo
- Nakonfigurujte podpisy v menu Nastavení
  (velikost, časové razítko ...)
- Vložte PRAVÝM KLIKNUTÍM na požadované místo
  (hlavní heslo vyžadováno jednou za relaci)
- Podpis přesuňte myší nebo šipkami
- Lze vložit více podpisů za sebou
- Každý podpis lze individuálně přizpůsobit
- Zahodit jednotlivý podpis
- Uložit / zahodit všechny podpisy najednou
- Lze také použít lištu menu.
        """,
        'signature_placeholder': "Náhled není k dispozici",
        'signature_info': "Podpis {0}: {1}×{2} px ({3}% z {4}×{5})",
        'signature_info_placeholder': "Nastavení podpisu {0}",
        'signature_inserted': "Podpis {0} vložen na stránku {1}",
        'signature_deleted': "Podpis smazán",
        'signature_copied': "Podpis zkopírován",
        'signature_pasted': "Podpis {0} vložen",
        'signature_saved': "{0} podpisů bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'signature_saved_voice': "Uloženo {0} podpisů",
        'mode_replace_signature_format': "Ukončit režim a vložit podpis {0}",
        'mode_conflict_voice_signature': "Režim {0} je aktivní. Ukončit a vložit podpis?",
        'signature_not_configured': "Podpis {0} není nakonfigurován",
        'signature_file_not_found': "Soubor podpisu nenalezen",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Žádný zkopírovaný podpis",
        'no_signatures_to_save': "Žádné podpisy k uložení",
        'signature_save_question': "Uložit všechny podpisy, upravit nebo zahodit tento?",
        'signatures_saved_title': "Podpisy uloženy",
        'signatures_saved': "{0} podpisů bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'signatures_saved_voice': "Uloženo {0} podpisů.",
        'all_signatures_discarded': "Všechny podpisy zahozeny",
        'signature_settings_saved': "Nastavení podpisů uložena",
        'signature_cancelled': "Podpis zahozen",
        'signature_active_title': "Podpis aktivní",
        'signature_replace_question': "Podpis je již aktivní.\n\nChcete nahradit aktuální podpis?",
        'signature_replace': "Nahradit podpis",
        'signature_replace_voice': "Nahradit aktuální podpis nebo zrušit?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Nastavení obrázků",
        'image_common': "Obecná nastavení obrázků",
        'image_keep_aspect': "Zachovat poměr stran při tažení",
        'image_default_size': "Výchozí velikost (%):",
        'image_dark_invert': "Invertovat barvy obrázků v tmavém režimu",
        'image_dark_invert_tooltip': "Zapnuto: obrázky jsou invertovány pro lepší viditelnost",
        'image_fine_tuning': "Doladění (pixely)",
        'image_offset_x': "Posun X:",
        'image_offset_y': "Posun Y:",
        'image_offset_x_tooltip': "Záporné hodnoty posouvají obrázek při ukládání doleva, kladné doprava",
        'image_offset_y_tooltip': "Záporné hodnoty posouvají obrázek při ukládání nahoru, kladné dolů",
        'image_select': "Vybrat obrázek",
        'image_insert': "Vložit obrázek",
        'image_customize': " Přizpůsobit obrázek",
        'image_aspect': " Zachovat poměr stran",
        'image_discard': " Zahodit tento obrázek",
        'image_save_all': " Uložit všechny obrázky",
        'image_discard_all': " Zahodit všechny obrázky",
        'image_filter': "Obrázky",
        'image_guide_title': "Vkládání obrázků - Návod",
        'image_guide': """
📷 Vkládání obrázků do PDF - Stručný návod:

1. Pravým kliknutím na požadované místo
2. "Vložit obrázek" → vyberte obrázek
3. Umístěte obrázek: tažením myší
4. Upravte velikost: tažením za rohy/hrany
5. Zachovat poměr stran: klávesa [A]
6. Další úpravy: pravým kliknutím na obrázek

Tip: V kontextové nabídce můžete upravit nastavení.
        """,
        'image_inserted': "Obrázek {0} vložen na stránku {1}",
        'image_deleted': "Obrázek zahozen",
        'image_copied': "Obrázek zkopírován",
        'image_pasted': "Obrázek vložen",
        'image_saved': "{0} obrázků bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'image_saved_voice': "Uloženo {0} obrázků",
        'image_aspect_on': "zapnuto",
        'image_aspect_off': "vypnuto",
        'image_aspect_toggle': "Zachovat poměr stran {0}",
        'image_reset': "Obrázek obnoven na původní velikost",
        'image_replaced': "Obrázek nahrazen",
        'image_invalid': "Neplatný obrázek",
        'mode_replace_image': "Vložit obrázek",
        'mode_conflict_voice_image': "Režim {0} je aktivní. Ukončit a vložit obrázek?",
        'image_active_title': "Obrázek aktivní",
        'image_replace_question': "Obrázek je již aktivní.\n\nChcete nahradit aktuální obrázek?",
        'image_replace': "Nahradit obrázek",
        'image_replace_voice': "Nahradit aktuální obrázek nebo zrušit?",
        'image_filter_all': "Obrázky (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Všechny soubory (*.*)",
        'no_copied_image': "Žádný zkopírovaný obrázek",
        'image_discarded': "Obrázek zahozen",
        'image_save_question': "Uložit všechny obrázky, upravit nebo zahodit tento?",
        'no_images_to_save': "Žádné obrázky k uložení",
        'no_valid_images': "Žádné platné obrázky k uložení",
        'images_saved_title': "Obrázky uloženy",
        'images_saved': "{0} obrázků bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'images_saved_voice': "Uloženo {0} obrázků.",
        'all_images_discarded': "Všechny obrázky zahozeny",
        'image_settings_updated': "Nastavení obrázků aktualizováno",
        'image_replace_title': "Vybrat nový obrázek",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Nastavení tvarů",
        'form_basic': "Základní nastavení",
        'form_default_type': "Výchozí typ tvaru:",
        'form_rectangle': "Obdélník",
        'form_ellipse': "Elipsa",
        'form_line': "Čára",
        'form_arrow': "Šipka",
        'form_line_width': "Tloušťka čáry:",
        'form_colors': "Barvy",
        'form_line_color': "Barva čáry:",
        'form_fill_color': "Barva výplně:",
        'form_choose_color': "Vybrat",
        'form_transparent': "Průhledné pozadí (pouze čára)",
        'form_filled': "vyplněno",
        'form_dark_mode': "Tmavý režim",
        'form_dark_invert': "Invertovat barvy v tmavém režimu",
        'form_fine_tuning': "Doladění (pixely)",
        'form_offset_x': "Posun X:",
        'form_offset_y': "Posun Y:",
        'form_offset_x_tooltip': "Záporné hodnoty posouvají tvar při ukládání doleva, kladné doprava",
        'form_offset_y_tooltip': "Záporné hodnoty posouvají tvar při ukládání nahoru, kladné dolů",
        'form_preview': "Náhled",
        'form_insert': "Vložit tvar",
        'form_rectangle_insert': "Obdélník",
        'form_ellipse_insert': "Elipsa/kruh",
        'form_line_insert': "Čára (2 kliknutí)",
        'form_arrow_insert': "Šipka (2 kliknutí)",
        'form_customize': " Přizpůsobit tvar",
        'form_transparent_toggle': " Průhledné pozadí",
        'form_discard': " Zahodit tento tvar",
        'form_save_all': " Uložit všechny tvary",
        'form_discard_all': " Zahodit všechny tvary",
        'form_guide_title': "Vkládání tvarů - Návod",
        'form_guide': """
📐 Vkládání tvarů do PDF - Stručný návod:

1. Vyberte typ tvaru (obdélník, elipsa, čára, šipka)
2. Klikněte na místo
   - Obdélník/elipsa: jedno kliknutí umístí tvar
   - Čára/šipka: dvě kliknutí pro počáteční a koncový bod
3. Umístěte tvar: tažením myší
4. Upravte velikost: tažením za rohy/hrany
5. Uložit tvar: Enter
6. Zahodit tvar: ESC
7. Další úpravy: pravým kliknutím na tvar

Tip: V kontextové nabídce můžete upravit nastavení.
        """,
        'form_inserted': "{0} vložen na stránku {1}",
        'form_deleted': "Tvar smazán",
        'form_copied': "Tvar zkopírován",
        'form_pasted': "Tvar vložen",
        'form_saved': "{0} tvarů bylo vloženo do PDF.\n\nPDF bylo znovu načteno...",
        'form_saved_voice': "Uloženo {0} tvarů",
        'form_reset': "Tvar obnoven na výchozí velikost",
        'form_transparent_on': "zapnuto",
        'form_transparent_off': "vypnuto",
        'form_transparent_toggled': "Průhledné pozadí {0}",
        'form_line_cancel': "Kreslení čáry zrušeno",
        'form_second_click': "Nyní klikněte na koncový bod pro {0}",
        'mode_replace_form': "Vložit tvar",
        'mode_conflict_voice_form': "Režim {0} je aktivní. Ukončit a vložit tvar?",
        'form_settings_updated': "Nastavení tvarů aktualizováno",
        'form_unknown': "Tvar",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klikněte na počáteční bod",
        'form_line_guide_2': "2. Klikněte na koncový bod",
        'form_line_guide_3': "Čára bude nakreslena mezi těmito dvěma body.",
        'form_line_status_1': "Čekám na první kliknutí...",
        'form_line_status_2': "První bod nastaven: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Nyní klikněte na koncový bod...",
        'form_line_status_4': "Oba body nastaveny.\nKlikněte na 'Hotovo' pro uložení.",
        'form_line_reset': "Resetovat",
        'form_line_finish': "Hotovo",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopírovat (Cmd+C)",
        'paste': "Vložit (Cmd+V)",
        'copied': "Zkopírováno: {0}",
        'no_element_to_copy': "Není vybrán žádný prvek ke kopírování",
        'no_copied_data': "Žádná zkopírovaná data",
        'no_valid_position': "Žádné platné místo pro vložení",
        'copy_text': "Text zkopírován",
        'copy_image': "Obrázek zkopírován",
        'copy_form': "Tvar zkopírován",
        'copy_signature': "Podpis zkopírován",
        'element_text': "Text",
        'element_image': "Obrázek",
        'element_form': "Tvar",
        'element_signature': "Podpis",
        'element_unknown': "Prvek",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflikt režimů",
        'mode_conflict_message': "Režim '{0}' je již aktivní.\n\nChcete jej ukončit a {1}?",
        'mode_replace': "Ukončit režim a {0}",
        'mode_cancel': "Zrušit",
        'mode_replace_text': "vložit text",
        'mode_replace_cross': "vložit křížek",
        'mode_replace_signature': "vložit podpis",
        'mode_replace_image': "vložit obrázek",
        'mode_replace_form': "vložit tvar",
        'mode_conflict_voice': "Režim {0} je aktivní. Ukončit a vložit text?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Zadávání textu",
        'active_mode_signature': "Podpis",
        'active_mode_image': "Obrázek",
        'active_mode_form': "Tvar",
        'active_mode_and': " a ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Vložit",
        'insert_another_text': "Vložit text",
        'insert_another_cross': "Vložit křížek",
        'insert_another_signature_1': "Podpis 1",
        'insert_another_signature_2': "Podpis 2",
        'insert_another_image': "Vložit obrázek",
        'insert_another_form_rect': "Obdélník",
        'insert_another_form_ellipse': "Elipsa",
        'insert_another_form_line': "Čára (2 kliknutí)",
        'insert_another_form_arrow': "Šipka (2 kliknutí)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Uložit {0}",
        'save_dialog_message': "{0} bude uložen na stránku {1}.\n\nJak chcete pokračovat?",
        'save_all': "Uložit všechny {0}",
        'save_single': "Uložit {0}",
        'save_customize': "Přizpůsobit {0}",
        'save_discard': "Zahodit tento {0}",
        'save_continue': "Pokračovat v úpravách",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Přejít na stránku {0}",
        'context_rotate': " Otočit stránku {0}",
        'context_delete': " Smazat stránku {0}",
        'context_export': " Exportovat stránku {0}",
        'context_mark_as': " Označit stránku jako...",
        'context_mark_empty': " Prázdná stránka",
        'context_unmark_empty': " Již neprázdná",
        'context_mark_export': " Označit k exportu",
        'context_unmark_export': " Již neexportovat",
        'context_batch_actions': " Hromadné akce",
        'context_batch_delete_empty': " Smazat všech {0} prázdných stránek",
        'context_batch_export_single': " Exportovat všech {0} stránek (jeden soubor)",
        'context_batch_export_split': " Exportovat všech {0} stránek (odděleně)",
        'context_drag_start': " Spustit Drag & Drop",
        'context_drag_stop': " Ukončit Drag & Drop",
        'context_insert': " Vložit",
        'context_insert_pages': " Vložit stránky",
        'context_zoom': "Zoom",
        'discard_mixed': "Zahodit všech {0} {1} a {2} {3}",
        'save_mixed': "Uložit {0} {1} a {2} {3}",
        'discard_texts': "Zahodit všech {0} textů",
        'discard_text_single': "Zahodit 1 text",
        'save_texts': "Uložit {0} textů",
        'save_text_single': "Uložit 1 text",
        'discard_crosses': "Zahodit všech {0} křížků",
        'discard_cross_single': "Zahodit 1 křížek",
        'save_crosses': "Uložit {0} křížků",
        'save_cross_single': "Uložit 1 křížek",
        'discard_signatures': "Zahodit všech {0} podpisů",
        'save_signature_single': "Uložit 1 podpis",
        'save_signatures': "Uložit {0} podpisů",
        'discard_images': "Zahodit všech {0} obrázků",
        'save_image_single': "Uložit 1 obrázek",
        'save_images': "Uložit {0} obrázků",
        'discard_forms': "Zahodit všech {0} tvarů",
        'save_form_single': "Uložit 1 tvar",
        'save_forms': "Uložit {0} tvarů",
        'cross_discard': "Zahodit tento křížek",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informace o exportu / importu",
        'export_what': "📋 Co se exportuje?",
        'export_general': "Obecná nastavení",
        'export_general_items': "• Hlasové výstupy (zap./vyp., rychlost)\n• Tmavý/světlý režim\n• Nastavení záloh\n• Nastavení OCR",
        'export_image_form': "Nastavení obrázků a tvarů",
        'export_image_form_items': "• Nastavení obrázků (poměr stran, výchozí velikost)\n• Nastavení tvarů (tloušťka čáry, barvy)\n• Nastavení podpisů (cesty, velikosti, časové razítko)",
        'export_passwords': "Databáze hesel",
        'export_passwords_items': "• Všechna uložená hesla PDF\n• Volitelně šifrovaná nebo nešifrovaná",
        'export_master': "Nastavení hlavního hesla",
        'export_master_items': "• Hash hlavního hesla\n• Nastavení pro podpisy/textové bloky",
        'export_signatures': "Podpisy a textové bloky",
        'export_signatures_items': "• Všechny obrazové soubory (podpisy)\n• Všechny textové bloky s formátováním\n• Označení soukromé/veřejné",
        'export_import_warning': "⚠️ Důležité upozornění",
        'export_import_note': "• Při importu budou VŠECHNA aktuální nastavení přepsána\n• Je vyžadován restart aplikace\n• Stávající podpisy/textové bloky budou nahrazeny",
        'export_master_note': "• Pokud je nastaveno hlavní heslo, můžete zvolit:\n  - Nešifrované (hesla v plaintextu)\n  - Šifrované (čitelná pouze s hlavním heslem)",
        'export_security': "• Exportovaný ZIP soubor obsahuje důvěrná data\n• Uchovávejte jej bezpečně (např. na šifrovaném USB disku)\n• Při ztrátě souboru jsou hesla nenávratně ztracena",
        'export_format': "📁 Formát exportu",
        'export_format_desc': "Nastavení jsou uložena v jediném ZIP souboru:",
        'export_filename': "Nastaveni_PDFDarkView_YYYYMMDD_HHMMSS.zip",
        'export_success': "Nastavení byla úspěšně exportována",
        'export_failed': "Export selhal",
        'export_import_question': "Chcete nyní restartovat aplikaci?",
        'export_password_question': "Je nastaveno hlavní heslo.\n\nChcete exportovat hesla v nešifrované podobě?\n(jinak budou exportována šifrovaně)",
        'export_decrypt': "Exportovat nešifrovaně",
        'export_encrypt': "Exportovat šifrovaně",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informace",
        'info_title': "O aplikaci PDF Dark View",
        'info_version': "Verze",
        'info_author': "Vyvinul Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "O aplikaci",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> je přístupný PDF prohlížeč, vyvinutý speciálně pro osoby se zrakovým postižením.</p>

            <p><strong>Klíčové vlastnosti:</strong></p>
            <ul>
                <li>Kontrastní, přizpůsobitelné rozhraní</li>
                <li>Plné ovládání z klávesnice</li>
                <li>Integrovaný hlasový výstup</li>
                <li>OCR pro naskenované dokumenty</li>
                <li>Rozsáhlé nástroje pro úpravy</li>
            </ul>

            <p>Podporováno je více než 50 jazyků – aby byly PDF přístupné pro všechny.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkce",
        'info_features_intro': "PDF Dark View vám nabízí následující možnosti:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Zobrazení a navigace</strong> – Tmavý/světlý režim, procházení stránek, zoom, skok na stránku</li>
            <li><strong>OCR (rozpoznávání textu)</strong> – Zpřístupnění naskenovaných dokumentů pro vyhledávání a kopírování</li>
            <li><strong>Úpravy</strong> – Vkládání textu, křížků, podpisů, obrázků a tvarů</li>
            <li><strong>Správa stránek</strong> – Mazání, extrahování, vkládání, přesouvání metodou drag & drop</li>
            <li><strong>Export</strong> – Do Wordu, Pages nebo jako text</li>
            <li><strong>Zabezpečení</strong> – Ochrana a správa heslem</li>
            <li><strong>Přístupnost</strong> – Hlasový výstup, ovládání z klávesnice, vysoký kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Ovládání",
        'info_accessibility': "♿ Přístupnost – plné ovládání z klávesnice",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Obecné</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Otevřít PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Hledat</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Přepnout tmavý/světlý režim</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Tisk</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Ukončit</div>

        <div class="shortcut-cat">📖 Navigace</div>
        <div class="shortcut-row"><kbd>Šipky</kbd> Listovat stránku po stránce</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Přejít na stránku</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> První stránka</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Poslední stránka</div>

        <div class="shortcut-cat">✏️ Úpravy</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Vložit text</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Smazat stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extrahovat stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Vložit stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Přesunout stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Otočit stránku</div>

        <div class="shortcut-cat">🖼️ Přesouvání prvků</div>
        <div class="shortcut-row"><kbd>Šipky</kbd> Přesunout text/obrázek/podpis</div>
        <div class="shortcut-row"><kbd>Ctrl+Šipky</kbd> Větší kroky</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Uložit</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Zahodit</div>

        <div class="shortcut-cat">🗣️ Hlasový výstup</div>
        <div class="shortcut-row"><kbd>F2</kbd> Zapnout/vypnout hlasový výstup</div>
        """,
        'info_contextmenu': "📌 Důležité: Všechny funkce jsou také dostupné z kontextové nabídky (pravé tlačítko myši)!",
        'info_accessibility_hint': "💡 Tip: Hlasový výstup (F2) usnadňuje orientaci a poskytuje zpětnou vazbu k nabídkám a dialogům.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licence & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Údaje podle § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Německo<br>
        E-mail: binhdiez64@gmail.com<br>
        Odpovědný za obsah: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Vyloučení odpovědnosti</strong><br>
        Software byl vyvinut s největší pečlivostí. Nepřebíráme žádnou záruku za správnost, úplnost a funkčnost. Použití je na vlastní nebezpečí.<br><br>

        <strong>📄 Licence MIT (soukromé použití)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Povoleno: bezplatné používání, soukromé úpravy, osobní kopie.<br>
        Nepovoleno: prodej, komerční využití, odstranění autorských oznámení.<br><br>

        <strong>🔧 Komponenty třetích stran</strong><br>
        Tento software obsahuje komponenty pod licencemi GPL, AGPL, Apache 2.0, BSD a MIT.<br>
        Při dalším šíření je třeba dodržovat příslušné licenční podmínky.<br><br>

        <strong>🌐 Open Source</strong><br>
        Zdrojový kód je k dispozici a lze jej prohlížet, upravovat a dále šířit v souladu s příslušnými licenčními podmínkami.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Poděkování",
        'info_credits': "Díky komunitě open-source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Zpracování PDF</li>
            <li><strong>PyQt5</strong> – Grafické rozhraní</li>
            <li><strong>Tesseract OCR</strong> – Rozpoznávání textu</li>
            <li><strong>OCRmyPDF</strong> – Integrace OCR</li>
            <li><strong>python-docx</strong> – Export do Wordu</li>
            <li><strong>qtawesome</strong> – Ikony</li>
            <li><strong>DeepSeek</strong> – Podpora při překladech (50+ jazyků)</li>
            <li><strong>Všem uživatelům</strong> – Za cennou zpětnou vazbu</li>
            <li><strong>Komunitě open-source</strong> – Za skvělé knihovny</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Jazyky",
        'info_languages_header': "🌍 Jazyková podpora",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View v současné době podporuje <strong>62 jazyků</strong> – aby software mohl být používán bez bariér po celém světě.</p>

            <p><strong>📖 Úplný seznam jazyků (Stav: březen 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikánština</li>
                    <li>🇦🇱 Albánština (Shqip)</li>
                    <li>🇩🇿 Arabština (العربية)</li>
                    <li>🇮🇩 Balijština (Basa Bali)</li>
                    <li>🇧🇩 Bengálština (বাংলা)</li>
                    <li>🇲🇲 Barmština (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosňština (Bosanski)</li>
                    <li>🇧🇬 Bulharština (Български)</li>
                    <li>🇨🇳 Čínština (中文)</li>
                    <li>🇩🇰 Dánština (Dansk)</li>
                    <li>🇩🇪 Němčina (Deutsch)</li>
                    <li>🇬🇧 Angličtina (English)</li>
                    <li>🇪🇪 Estonština (Eesti)</li>
                    <li>🇫🇮 Finština (Suomi)</li>
                    <li>🇫🇷 Francouzština (Français)</li>
                    <li>🇬🇷 Řečtina (Ελληνικά)</li>
                    <li>🇮🇱 Hebrejština (עברית)</li>
                    <li>🇮🇳 Hindština (हिन्दी)</li>
                    <li>🇭🇷 Chorvatština (Hrvatski)</li>
                    <li>🇭🇺 Maďarština (Magyar)</li>
                    <li>🇮🇩 Indonéština (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irština (Gaeilge)</li>
                    <li>🇮🇸 Islandština (Íslenska)</li>
                    <li>🇮🇹 Italština (Italiano)</li>
                    <li>🇯🇵 Japonština (日本語)</li>
                    <li>🇰🇭 Khmérština (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korejština (한국어)</li>
                    <li>🇱🇦 Laoština (ພາສາລາວ)</li>
                    <li>🇱🇻 Lotyština (Latviešu)</li>
                    <li>🇱🇹 Litevština (Lietuvių)</li>
                    <li>🇱🇺 Lucemburština (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajština (Bahasa Melayu)</li>
                    <li>🇮🇳 Maráthština (मराठी)</li>
                    <li>🇲🇳 Mongolština (Монгол)</li>
                    <li>🇳🇵 Nepálština (नेपाली)</li>
                    <li>🇳🇱 Nizozemština (Nederlands)</li>
                    <li>🇳🇴 Norština (Norsk)</li>
                    <li>🇦🇫 Paštština (پښتو)</li>
                    <li>🇮🇷 Perština (فارسی)</li>
                    <li>🇵🇱 Polština (Polski)</li>
                    <li>🇵🇹 Portugalština (Português)</li>
                    <li>🇮🇳 Pandžábština (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumunština (Română)</li>
                    <li>🇷🇺 Ruština (Русский)</li>
                    <li>🇸🇪 Švédština (Svenska)</li>
                    <li>🇷🇸 Srbština (Српски)</li>
                    <li>🇸🇰 Slovenština (Slovenčina)</li>
                    <li>🇸🇮 Slovinština (Slovenščina)</li>
                    <li>🇪🇸 Španělština (Español)</li>
                    <li>🇹🇿 Svahilština (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamilština (தமிழ்)</li>
                    <li>🇮🇳 Telugština (తెలుగు)</li>
                    <li>🇹🇭 Thajština (ไทย)</li>
                    <li>🇨🇿 Čeština (Čeština)</li>
                    <li>🇹🇷 Turečtina (Türkçe)</li>
                    <li>🇺🇦 Ukrajinština (Українська)</li>
                    <li>🇵🇰 Urdština (اردو)</li>
                    <li>🇻🇳 Vietnamština (Tiếng Việt)</li>
                    <li>🇸🇳 Wolofština (Wolof)</li>
                    <li>🇺🇸 Jidiš (ייִדיש)</li>
                    <li>🇿🇦 Zuluština (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Přidání vlastních jazyků:</strong><br>
                Chcete jazyk, který ještě není zahrnut? Jednoduše umístěte svůj vlastní soubor slovníku (<code>sprache_xx.py</code>) vedle aplikace – software jej automaticky rozpozná. Máte-li zájem o konkrétní překlad, neváhejte mě kontaktovat.
            </div>

            <p><strong>🙏 Zvláštní poděkování:</strong> DeepSeek za podporu při překladu všech slovníků do 62 jazyků.</p>

            <p>📧 Kontakt pro překlady: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Chyba",
        'error_occurred': "Došlo k chybě",
        'error_pdf_load': "Chyba při načítání PDF",
        'error_pdf_save': "Chyba při ukládání PDF",
        'error_ocr': "Chyba při rozpoznávání textu",
        'error_no_pdf': "Není načteno žádné PDF",
        'error_page_not_found': "Stránka nenalezena",
        'error_invalid_range': "Neplatný rozsah stránek",
        'error_file_not_found': "Soubor nenalezen",
        'error_permission': "Nedostatečná oprávnění",
        'error_unknown': "Neznámá chyba",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Úspěch",
        'success_operation': "Operace úspěšně dokončena",
        'success_saved': "Úspěšně uloženo",
        'success_exported': "Úspěšně exportováno",
        'success_imported': "Úspěšně importováno",
        'success_deleted': "Úspěšně smazáno",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Potvrzení",
        'confirm_yes': "Ano",
        'confirm_no': "Ne",
        'confirm_ok': "OK",
        'confirm_cancel': "Zrušit",
        'confirm_delete': "Smazat",
        'confirm_overwrite': "Přepsat",
        'confirm_continue': "Pokračovat",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Načítám PDF...",
        'progress_saving': "Ukládám PDF...",
        'progress_exporting': "Exportuji PDF...",
        'progress_processing': "Zpracovávám...",
        'progress_wait': "Prosím čekejte...",
        'progress_preparing': "Připravuji...",
        'progress_finalizing': "Finalizuji...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Bílá",
        'color_black': "Černá",
        'color_red': "Červená",
        'color_green': "Zelená",
        'color_blue': "Modrá",
        'color_yellow': "Žlutá",
        'color_magenta': "Purpurová",
        'color_cyan': "Azurová",
        'color_orange': "Oranžová",
        'color_gray': "Šedá",
        'color_custom': "Výběr barvy",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Soubor",
        'menu_edit': "&Úpravy",
        'menu_view': "&Zobrazení",
        'menu_tools': "&Nástroje",
        'menu_settings': "&Nastavení",
        'menu_help': "&Nápověda",
        'menu_language': "🌐 Jazyk",
        'menu_guides': "&Návody",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Otevřít",
        'file_save_as': "&Uložit jako...",
        'file_protect': "&Chránit dokument...",
        'file_export': "&Exportovat",
        'file_export_pages': "Exportovat do Pages",
        'file_export_word': "Exportovat do DOCX",
        'file_export_text': "Exportovat do TXT",
        'file_print_now': "&Tisknout nyní",
        'file_print': "&Tisk",
        'file_close': "&Zavřít",
        'file_quit': "&Konec",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Hledat",
        'edit_ocr': " Provést OCR",
        'edit_rotate': "&Otočit stránku",
        'edit_rotate_all': "Otočit &všechny stránky",
        'edit_delete_pages': "&Smazat stránky",
        'edit_extract_pages': "&Extrahovat stránky",
        'edit_insert_pages': "&Vložit stránky",
        'edit_move_pages': "&Přesunout stránky",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Vložit text a křížky",
        'text_insert': " Vložit text",
        'cross_insert': " Vložit křížek",
        'text_customize': " Přizpůsobit text",
        'cross_customize': " Přizpůsobit tento křížek",
        'cross_customize_all': " Přizpůsobit všechny křížky",
        'text_discard': " Zahodit tento text / křížek",
        'text_discard_all': " Zahodit všechny texty a křížky",
        'text_save_all': " Uložit všechny texty a křížky",
        'text_guide': " Zadávání textu / textové bloky - návod",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Vložit podpis",
        'signature_settings_menu': " Nastavení...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Vložit obrázek",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Vložit tvary",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Zobrazit okno textu",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Šířka stránky (výchozí)",
        'view_zoom_two': "&Dvě stránky",
        'view_zoom_overview': "&Přehled (více stránek)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Usnadnění",
        'settings_voice': "Hlasový výstup",
        'settings_voice_tooltip': "doplňuje informace z čteček obrazovky o další údaje",
        'settings_signature': "&Nastavení podpisů",
        'settings_password': "&Správa hesel",
        'settings_backup': "Vytvořit zálohu před změnami",
        'settings_export_import': "&Exportovat nastavení / importovat nastavení",
        'settings_export': "&Exportovat všechna nastavení...",
        'settings_import': "&Importovat všechna nastavení...",
        'settings_export_info': "&Co se exportuje?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "zap.",
        'voice_off': "vyp.",
        'voice_toggle': "Hlasový výstup {0}",
        'voice_speed': "Rychlost {0} procent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Nástroj nenalezen:\n{0}\n\nBASE_DIR: {1}\nUjistěte se, že nástroje pro PDF jsou nainstalovány v adresáři {1}.",
        'tool_started': "{0} spuštěn",
        'tool_start_failed': "Nelze spustit",
        'process_error_failed_to_start': "Nelze spustit proces. Existuje soubor?",
        'process_error_crashed': "Proces spadl během spouštění.",
        'process_error_timeout': "Dosažen časový limit procesu.",
        'process_error_write': "Chyba zápisu v procesu.",
        'process_error_read': "Chyba čtení v procesu.",
        'process_error_unknown': "Neznámá chyba procesu",
        'process_command': "Příkaz",
        'process_normal_exit': "normálně ukončen",
        'process_crashed': "spadl",
        'process_nonzero_exit': "{0} byl ukončen s chybovým kódem {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Ruší se...",
        'move_cancelling': "Ruší se přesouvání",
        'opening_pdf': "Otevírám PDF...",
        'loading_document': "Načítám dokument...",
        'pdf_opened': "PDF otevřeno",
        'pages_found_moving': "Nalezeno {0} stránek, {1} k přesunutí",
        'creating_backup': "Vytvářím zálohu...",
        'backup_description': "Zálohuji původní soubor...",
        'backup_saved_as': "Zálohováno jako: {0}",
        'error_format': "Chyba: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Hledání resetováno",
        'page_header_simple': "=== Stránka {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Správa hesel – Návod",
        'password_guide_voice': "Návod ke správě hesel. Přečtěte si prosím poznámky.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Správa hesel – Podrobný návod</strong></p>

        <p><strong>1. Ochrana PDF heslem</strong></p>
        <ul>
        <li>Při otevírání PDF chráněného heslem se zobrazí dialog, do kterého můžete zadat heslo.</li>
        <li>Heslo můžete uložit v šifrované podobě, abyste ho nemuseli zadávat pokaždé znovu (zaškrtávací políčko „Uložit heslo“).</li>
        <li>Tlačítkem „Odstranit heslo“ můžete vytvořit dešifrovanou kopii PDF a heslo odstranit z databáze.</li>
        </ul>

        <p><strong>2. Hlavní heslo</strong></p>
        <ul>
        <li>Hlavní heslo chrání přístup ke všem uloženým heslům PDF.</li>
        <li><strong>Nastavení:</strong> Přejděte do „Nastavení → Správa hesel → Nastavení hlavního hesla“ a klikněte na „Nastavit hlavní heslo“. Zvolte silné heslo (alespoň 8 znaků).</li>
        <li><strong>Změna:</strong> Po úspěšném ověření můžete hlavní heslo změnit.</li>
        <li><strong>Odstranění:</strong> Pokud hlavní heslo odstraníte, budou VŠECHNA uložená hesla nenávratně smazána. Před odstraněním můžete exportovat záložní kopii.</li>
        <li>Jednou za relaci se musíte ověřit hlavním heslem, abyste získali přístup k chráněným funkcím (např. zobrazení hesel).</li>
        </ul>

        <p><strong>3. Správa hesel (seznam)</strong></p>
        <ul>
        <li>V „Nastavení → Správa hesel“ se otevře tabulka všech uložených PDF s jejich šifrovanými hesly.</li>
        <li><strong>Bez hlavního hesla:</strong> Můžete pouze mazat záznamy – hesla zůstávají skrytá.</li>
        <li><strong>S hlavním heslem (ověřeno):</strong> Můžete hesla zobrazovat, kopírovat, exportovat a mazat.</li>
        <li><strong>Export:</strong> Vyberte formát (JSON, CSV, TXT) a uložte seznam. Pokud je nastaveno hlavní heslo, můžete zvolit, zda se hesla exportují v nešifrované nebo šifrované podobě.</li>
        <li><strong>Import:</strong> Dříve exportovaný ZIP soubor (všechna nastavení) lze znovu načíst přes „Nastavení → Exportovat nastavení / importovat nastavení“. Upozornění: Stávající data budou přepsána!</li>
        </ul>

        <p><strong>4. Generátor hesel</strong></p>
        <ul>
        <li>V dialogu hesla (např. při zabezpečování PDF) je napravo od vstupního pole tlačítko s kostkou 🎲.</li>
        <li>Kliknutím na něj otevřete generátor hesel. Můžete nastavit délku, znakové sady (velká písmena, malá písmena, číslice, speciální znaky) a oddělovač pro lepší čitelnost.</li>
        <li>Vygenerované heslo lze přímo použít a v případě potřeby zkopírovat.</li>
        </ul>

        <p><strong>5. Důležité bezpečnostní poznámky</strong></p>
        <ul>
        <li>Uložená hesla jsou uchovávána šifrovaná pomocí AES-256. Klíč je odvozen z hlavního hesla (pokud je nastaveno) nebo z pevné hodnoty (bez hlavního hesla).</li>
        <li>Bez hlavního hesla jsou hesla sice šifrována, ale klíč je uložen v programu – útočník s přístupem k vašim souborům by je mohl dešifrovat. Proto důrazně doporučujeme používat hlavní heslo.</li>
        <li>Databáze hesel je uložena v souboru `Data/passwords.json`. Pravidelně zálohujte, zejména před odstraněním hlavního hesla.</li>
        <li>Při ztrátě hlavního hesla jsou všechna uložená hesla nenávratně ztracena.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Režim invertování",
        'invert_mode_classic': "Klasický (invertovat všechny barvy)",
        'invert_mode_smart': "Inteligentní (invertovat pouze jas)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Prahová hodnota stupňů šedi",
        'gray_threshold_10': "10% (přísná)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standardní)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (měkká)",
        'threshold_changed': "Prahová hodnota nastavena na {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Prahová hodnota stupňů šedi – Vysvětlení",
        'threshold_guide_text': "Prahová hodnota stupňů šedi určuje, které pixely jsou v inteligentním tmavém režimu považovány za 'šedé' a jsou invertovány.\n\n"
                                "• Nízká hodnota (10%) invertuje pouze téměř dokonalé odstíny šedi – barevné prvky zůstávají plně zachovány.\n"
                                "• Vysoká hodnota (50%) invertuje také mírně barevné pixely – to zvyšuje kontrast, ale může zkreslit barvy.\n\n"
                                "Optimální hodnota závisí na dokumentu. Pro čistě textové dokumenty je často ideální 30–40%, pro barevnou grafiku spíše 10–20%.\n\n"
                                "Hodnotu můžete kdykoli upravit prostřednictvím nabídky 'Nastavení' – PDF se pak okamžitě znovu načte.\n\n"
                                "Poznámka:\n* Fotografie a obrázky lze správně zobrazit pouze ve světlém režimu!\n* Nastavení invertování se zobrazí pouze tehdy, je-li aktivován tmavý režim.",
        'threshold_guide_voice': "Prahová hodnota stupňů šedi určuje, jak silně inteligentní tmavý režim zasahuje. Nízká hodnota šetří barvy, vysoká zvyšuje kontrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Otevírání PDF...",
        'progress_loading_document': "Načítání dokumentu...",
        'progress_pdf_opened': "PDF otevřeno",
        'progress_creating_backup': "Vytváření zálohy...",
        'progress_backup_description': "Zabezpečení původního souboru...",
        'progress_backup_created': "Záloha vytvořena",
        'progress_backup_saved_as': "Uloženo jako: {0}",
        'progress_analyzing_start': "Spuštění analýzy...",
        'progress_searching_empty': "Hledání prázdných stránek...",
        'progress_page_empty': "Stránka {0} je prázdná",
        'progress_page_keep': "Ponechat stránku {0}",
        'progress_analysis_complete': "Analýza dokončena",
        'progress_empty_found': "Nalezeno {0} prázdných stránek",
        'progress_current_page': "Aktuální stránka",
        'progress_mark_delete': "Označuje se k odstranění",
        'progress_range_selected': "Rozsah stránek {0}-{1}",
        'progress_deleting_pages': "Mazání {0} stránek",
        'progress_creating_new_pdf': "Vytváření nového PDF...",
        'progress_transferring_pages': "Přenášení stránek",
        'progress_keeping_page': "Stránka {0} bude ponechána ({1}/{2})",
        'progress_saving_pdf': "Ukládání PDF...",
        'progress_optimizing': "Optimalizace velikosti souboru...",
        'progress_finalizing': "Finalizace...",
        'progress_new_size': "Nová velikost: {0:.2f} MB",
        'progress_cancelling': "Rušení...",
        'progress_cancel_message': "{0} se ruší",
        'progress_pages_found_moving': "Nalezeno {0} stránek, {1} k přesunutí",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analýza PDF...",
        'ocr_status_optimizing': "Probíhá optimalizace obrazu...",
        'ocr_status_recognizing': "Probíhá rozpoznávání textu...",
        'ocr_status_embedding': "Vkládání textu...",
        'ocr_status_finalizing': "Finalizace PDF...",

        # PDF-Laden
        'progress_preparing': "Příprava...",
        'progress_loading': "Načítání PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Mazání stránek...",
        'progress_moving_title': "Přesouvání stránek...",
        'pages_found': "Nalezené stránky",
        'progress_creating_new_order': "Vytváření nového pořadí...",
        'progress_sorting_pages': "Řazení stránek...",
        'progress_moving_to_begin': "Přesunout {0} stránek na začátek",
        'progress_transferring_count': "Přenést {0} stránek",
        'progress_transferring_before_target': "Přenést stránky před cíl",
        'progress_moving_pages': "Přesunout {0} stránek",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_zaloha_",
        'filename_protected_suffix': "_chraneno_",
        'filename_copy_suffix': "_Kopie",
        'filename_page_single': "_Strana_",
        'filename_page_range': "_Strany_",
        'filename_export_page': "_Strana_{0:03}",
        'filename_export_range': "_Strany_{0}-{1}",
        'filename_export_multiple': "_Strany_{0}",
        'filename_with_text': "_s_Textem",
        'filename_with_signature': "_s_Podpisem",
        'filename_with_image': "_s_Obrazkem",
        'filename_with_forms': "_s_Tvary",
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
        'view_toggle_navbar': "Zobrazit lištu tlačítek",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Nelze smazat všechny stránky",
		'pages_cannot_delete_last_page': 'Poslední stránku nelze smazat!',
		'pages_cannot_delete_all_pages': 'V dokumentu musí zůstat alespoň jedna stránka!',
		'delete_pages_confirm': 'Opravdu chcete smazat {0} stránek?',
		'delete_pages_confirm_voice': 'Opravdu chcete smazat {0} stránek?',
		'pages_deleted': '{0} stránek bylo úspěšně smazáno.',
		'warning': 'Varování',
		'error': 'Chyba',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nebyl vybrán formulář",
        'form_customized': "Formulář přizpůsoben",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Vybrat",
        'btn_use': "Použít",
        'master_password_for_spasswords': "Pro ukládání a používání hesel je nejprve třeba nastavit hlavní heslo.\n\nChcete nyní nastavit hlavní heslo?",
        'open_saved_dialog_title': "Otevřít uložený soubor",
        'open_saved_question': "Chcete nyní otevřít uložený soubor?",
        'password': "Heslo",
        'password_manager_master_required': "Správce hesel je dostupný pouze pokud je nastaveno hlavní heslo.\n\nChcete nyní nastavit hlavní heslo?",
        'password_master_required_for_select': "Pro zobrazení a výběr uložených hesel se musíte nejprve autentizovat svým hlavním heslem.\n\nChcete se nyní autentizovat?",
        'password_not_available': "Vybrané heslo není dostupné nebo jej nelze dešifrovat.",
        'password_options_title': "Možnosti hesla",
        'password_save_choice_change': "Nastavit nové heslo",
        'password_save_choice_keep': "Použít stávající heslo",
        'password_save_choice_none': "Uložit nešifrovaně",
        'password_save_hint': "Nejprve nastavte hlavní heslo pro bezpečné ukládání hesel.",
        'password_save_master_required': "Uložit heslo (pouze s hlavním heslem)",
        'password_save_question': "Aktuální PDF je chráněno heslem. Chcete použít stávající heslo, nastavit nové nebo uložit nešifrovaně?",
        'password_select': "Vybrat heslo",
        'password_select_none': "Nebylo vybráno žádné heslo.\n\nVyberte prosím heslo ze seznamu.",
        'password_select_one': "Vyberte prosím právě jedno heslo.\n\nOznačili jste několik hesel.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_záloha",
        'filename_insert_suffix': "_s_vložením",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_stránky_smazány",
        'filename_pages_moved': "_stránky_přesunuty",
        'filename_rotated_all_suffix': "_všechny_stránky_otočeny",
        'filename_rotated_suffix': "_stránka_otočena",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurace názvů souborů při změnách PDF",
        'filename_keep_suffixes': "Zachovat předchozí přípony (např. _s_textem)",
        'filename_keep_suffixes_false': "Nahradit",
        'filename_keep_suffixes_true': "Zachovat",
        'filename_preview_label': "Náhled názvu souboru:",
        'filename_preview_overwrite_hint': "Náhled není k dispozici – originál bude přepsán.",
        'filename_separator': "Oddělovač mezi slovy",
        'filename_separator_none': "Žádný oddělovač",
        'filename_separator_space': "Mezera ( )",
        'filename_separator_underscore': "Podtržítko (_)",
        'filename_settings_saved': "Nastavení názvů souborů uložena",
        'filename_settings_title': "Formátování názvu souboru a záloha",
        'filename_timestamp_position': "Pozice časového razítka",
        'filename_timestamp_position_after': "Za základním názvem",
        'filename_timestamp_position_before': "Úplně vpředu",
        'filename_timestamp_position_end': "Na konci",
        'filename_use_timestamp': "Použít časové razítko",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Chování při změnách:</b><ul><li>Mazání a vkládání stránek</li><li>Vkládání textu, podpisu, obrázku a tvarů</li><li>OCR</li></ul></html>",
        'backup_section': "Záloha pro operace se stránkami (Mazání, Přesun)",
        'behavior_info': "Poznámka: Při 'Přepsat originál' se ignorují časová razítka a přípony – soubor si zachová svůj název.",
        'behavior_new_file': "Vždy vytvořit nový soubor (s časovým razítkem a příponou)",
        'behavior_overwrite': "Přepsat originál (žádný nový soubor)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Všechny stránky byly otočeny.\n\nOriginál zůstal nezměněn.\nNový soubor: {0}",
        'all_pages_rotated_voice': "Všechny stránky otočeny, vytvořen nový soubor.",
        'empty_pages_deleted_new_file': "{0} prázdných stránek bylo smazáno.\n\nOriginál zůstal nezměněn.\nNový soubor: {1}",
        'empty_pages_deleted_voice': "{0} prázdných stránek smazáno, vytvořen nový soubor.",
        'ocr_keep_original': "Zachovat originál (později ručně otevřít)",
        'ocr_new_file_question': "Nový prohledávatelný PDF byl uložen jako:\n{0}\n\nChcete jej nyní otevřít?",
        'ocr_open_new': "Otevřít nový OCR soubor",
        'ocr_original_kept': "Původní soubor zůstává otevřený. OCR soubor byl uložen.",
        'page_deleted_new_file': "Stránka {0} byla smazána.\n\nOriginál zůstal nezměněn.\nNový soubor: {1}",
        'page_deleted_voice': "Stránka {0} smazána, vytvořen nový soubor.",
        'page_rotated_new_file': "Stránka {0} byla otočena.\n\nOriginál zůstal nezměněn.\nNový soubor: {1}",
        'page_rotated_voice': "Stránka {0} otočena, vytvořen nový soubor.",
        'pages_deleted_new_file': "Bylo smazáno {0} stránek.\n\nPůvodní soubor zůstal nezměněn.\nNový soubor: {1}",
        'pages_deleted_new_file_voice': "{0} stránek smazáno, vytvořen nový soubor.",
        'pages_inserted_new_file': "Bylo vloženo {0} stránek.\n\nPůvodní soubor zůstal nezměněn.\nNový soubor: {1}",
        'pages_inserted_new_file_ask': "Bylo vloženo {0} stránek.\n\nOriginál zůstal nezměněn.\nNový soubor: {1}\n\nChcete jej nyní otevřít?",
        'pages_inserted_voice_new': "{0} stránek vloženo, vytvořen nový soubor.",
        'pages_moved_new_file': "Bylo přesunuto {0} stránek.\n\nPůvodní soubor zůstal nezměněn.\nNový soubor: {1}",
        'pages_moved_new_file_voice': "{0} stránek přesunuto, vytvořen nový soubor.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Již nezobrazovat",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Nastavení zálohy</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Záloha ZAPNUTA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Při všech změnách, které přepisují originál</strong> (text, podpis, obrázek, tvar, OCR, otáčení, vkládání, mazání/přesun stránek) je <strong>automaticky vytvořena záloha s časovým razítkem</strong> před provedením změny.</p>
                <p style="margin: 5px 0 5px 20px;">• Záloha je umístěna vedle původního souboru (např. <code>Dokument_záloha_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Pokud jste navíc aktivovali možnost <strong>„Přepsat originál“</strong>, je také vytvořena záloha.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Záloha VYPNUTA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Není vytvářena žádná záloha</strong> – ani při přepisování, ani při operacích se stránkami.</p>
                <p style="margin: 5px 0 5px 20px;">• Původní soubor může být při přepsání nenávratně ztracen.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Doporučeno pouze pro zkušené uživatele!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Nastavení zálohy je nezávislé na možnosti „Přepsat originál“. Můžete kombinovat obojí.<br>
                Tuto zprávu můžete trvale skrýt.
            </div>
        </div>
        """,
        'backup_info_title': "Chování zálohy",
        'backup_info_voice': "Oznámení o chování zálohy při operacích se stránkami. Záloha zapnuta přepisuje originál, záloha vypnuta vytváří nový soubor.",
        'show_backup_info': "Informace o nastavení zálohy",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Již nezobrazovat",
        'overwrite_enable_backup': "Aktivovat zálohu (doporučeno)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Přepsat originál</p>
            <p>Pokud aktivujete tuto možnost, změny (text, podpis, obrázek, tvar, OCR, otáčení, vkládání) jsou <strong>uloženy přímo do originálu</strong> – <strong>nevzniká žádný nový soubor</strong>.</p>
            <p>• Název souboru zůstává nezměněn.<br>
            • Časová razítka a přípony jsou ignorovány.<br>
            • <strong>Bez zálohy může být originál nenávratně ztracen.</strong></p>
            <p style="color: #FFD700;">Doporučení: Aktivujte dodatečně možnost zálohy pro automatické zálohování.</p>
        </div>
        """,
        'overwrite_info_title': "Přepsat originál",
        'overwrite_info_voice': "Upozornění: Přepsat originál – žádný nový soubor. Záloha doporučena.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Bylo vloženo {0} stránek.\n\nPůvodní soubor byl přepsán.\nByla vytvořena záloha.",
        'pages_inserted_overwrite_no_backup': "Bylo vloženo {0} stránek.\n\nPůvodní soubor byl přepsán.\nNebyla vytvořena žádná záloha.",
        'texts_saved_overwrite_with_backup': "Změny byly uloženy v originálu.\n\nByla vytvořena záloha.",
        'texts_saved_overwrite_no_backup': "Změny byly uloženy v originálu.\n\nNebyla vytvořena žádná záloha.",
        'texts_crosses_saved_new_file': "{0} {1} a {2} {3} bylo vloženo.\n\nPůvodní soubor zůstal nezměněn.\nByl vytvořen nový soubor.\n\nNové PDF se načítá...",
        'texts_saved_new_file': "{0} {1} bylo vloženo.\n\nPůvodní soubor zůstal nezměněn.\nByl vytvořen nový soubor.\n\nNové PDF se načítá...",
        'crosses_saved_new_file': "{0} {1} bylo vloženo.\n\nPůvodní soubor zůstal nezměněn.\nByl vytvořen nový soubor.\n\nNové PDF se načítá...",
        'elements_saved_new_file': "{0} prvků bylo vloženo.\n\nPůvodní soubor zůstal nezměněn.\nByl vytvořen nový soubor.\n\nNové PDF se načítá...",
        'signatures_saved_overwrite_with_backup': "Podpis(y) byl(y) uložen(y) v originálu.\n\nByla vytvořena záloha.",
        'signatures_saved_overwrite_no_backup': "Podpis(y) byl(y) uložen(y) v originálu.\n\nNebyla vytvořena žádná záloha.",
        'images_saved_overwrite_with_backup': "Obrázek(ky) byl(y) uložen(y) v originálu.\n\nByla vytvořena záloha.",
        'images_saved_overwrite_no_backup': "Obrázek(ky) byl(y) uložen(y) v originálu.\n\nNebyla vytvořena žádná záloha.",
        'forms_saved_overwrite_with_backup': "Tvar(y) byl(y) uložen(y) v originálu.\n\nByla vytvořena záloha.",
        'forms_saved_overwrite_no_backup': "Tvar(y) byl(y) uložen(y) v originálu.\n\nNebyla vytvořena žádná záloha.",
        'signatures_saved_new_file': "{0} podpisů bylo vloženo.\n\nPůvodní soubor zůstal nezměněn.\nByl vytvořen nový soubor.\n\nNové PDF se načítá...",
        'images_saved_new_file': "{0} obrázků bylo vloženo.\n\nPůvodní soubor zůstal nezměněn.\nByl vytvořen nový soubor.\n\nNové PDF se načítá...",
        'forms_saved_new_file': "{0} tvarů bylo vloženo.\n\nPůvodní soubor zůstal nezměněn.\nByl vytvořen nový soubor.\n\nNové PDF se načítá...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Upozornění: Toto PDF obsahuje otočené stránky. Umístění může být odchylné.",
        'page_rotated_warning_title': "Zjištěna otočená stránka",
        'page_rotated_warning_message': "Aktuální stránka {0} je otočena o {1}°.\n\nVkládání prvků na otočené stránky není podporováno.\n\nChcete nyní otočit stránku do vzpřímené polohy?",
        'page_rotated_warning_voice': "Upozornění: Stránka je otočená. Nejprve ji prosím otočte.",
        'paste_on_rotated_page_simple_warning': "Vložení na stránku {0} není možné!\n\nTato stránka je otočena o {1}°.\n\nNejprve prosím otočte stránku na 0° (Menu: Upravit → Zarovnat stránku).\n\nUpozornění:\nDříve zkopírovaný prvek bude ztracen, pokud neuložíte před otočením stránky.",
        'paste_on_rotated_page_voice': "Vkládání přerušeno. Stránka je otočená. Nejprve prosím zarovnejte stránku.",
        'page_rotated_cancel': "Zrušit",
        'page_rotated_rotate_until_upright': "Opakovaně otáčet stránku (dokud není vzpřímená)",
        'page_rotated_now_upright': "Stránka je nyní vzpřímená. Nyní můžete vkládat.",
        'page_rotated_still_not_upright': "Stránku nebylo možné otočit do vzpřímené polohy. Prosím opravte ručně.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Nápověda: Oprava otočených stránek",
        'help_rotated_pages_voice': "Nápověda pro opravu otočených stránek se otevírá.",
        'btn_help': "Nápověda",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problém: Otočená stránka – Vkládání nefunguje správně</p>

            <p>Pokud vkládání textů, podpisů nebo tvarů na otočenou stránku nefunguje správně, můžete stránku opravit externím PDF editorem.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Řešení s externím nástrojem (např. macOS Náhled)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Exportovat stránku</strong><br>
                &nbsp;&nbsp;Klikněte v nabídce na <strong>Soubor → Exportovat jako stránky</strong> nebo použijte jinou metodu k uložení požadované stránky jako jednotlivého PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Otevřít stránku v externím programu</strong><br>
                &nbsp;&nbsp;Otevřete exportované PDF v PDF editoru (např. <strong>macOS Náhled</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Otočit stránku</strong><br>
                &nbsp;&nbsp;Otočte stránku tak, aby byla vzpřímená (v Náhledu: <strong>Nástroje → Otočit</strong> nebo <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Uložit</strong><br>
                &nbsp;&nbsp;Uložte opravenou stránku (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Znovu vložit stránku do původního dokumentu</strong><br>
                &nbsp;&nbsp;Vraťte se do PDFDarkView a vložte opravenou stránku na požadované místo:<br>
                &nbsp;&nbsp;<strong>Upravit → Vložit stránky</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternativa: Otočit stránku v originálu</p>
                <p style="margin: 5px 0 5px 20px;">• Použijte vestavěnou funkci otáčení (<strong>Upravit → Otočit stránku</strong>) k postupnému opravení stránky.<br>
                • Po každém otočení můžete zkontrolovat, zda vkládání nyní funguje.<br>
                • To je často rychlejší řešení – vyzkoušejte nejprve toto!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Pokud často narážíte na otočené stránky, můžete varování v dialogu vkládání trvale skrýt.<br>
                Umístění pak může být odchylné – používejte tuto možnost pouze pokud znáte důsledky.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Zarovnat stránky",
        'menu_rotate_normalize_tooltip': "Otočit stránku nebo resetovat na 0°",
        'normalize_current_page': "Uvést aktuální stránku do vzpřímené polohy (nastavit na 0°)",
        'normalize_all_pages': "Uvést všechny stránky do vzpřímené polohy (nastavit na 0°)",
        'page_normalized': "Stránka {0} byla uvedena do vzpřímené polohy.",
        'all_pages_normalized': "Všechny stránky byly uvedeny do vzpřímené polohy.",
        'page_already_upright': "Stránka {0} je již vzpřímená.",
        'all_pages_already_upright': "Všechny stránky jsou již vzpřímené.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF neobsahuje žádný prohledávatelný text.</p><p>Chcete provést OCR pro export do {0}?</p>",
        'export_ocr_voice': "PDF neobsahuje žádný text. Pro export do {0} je vyžadováno OCR.",
        'export_no_ocr_possible': "Export bez OCR není možný. Proveďte prosím OCR přes nabídku.",
        'ocr_failed_export_not_possible': "OCR selhalo. Export nelze provést.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF se otevře v Náhledu. Spusťte tam prosím tiskový proces.",
        'print_preview_manual': "PDF bylo otevřeno. Proveďte prosím příkaz pro tisk ručně (např. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Sloučit PDF",
        'merge_pdfs': "Sloučit PDF",
        'merge_progress_title': "Sloučení PDF...",
        'merge_pdfs_list': "PDF v pořadí (Přetažením seřadit)",
        'merge_add_pdf': "Přidat PDF",
        'merge_remove': "Odebrat",
        'merge_move_up': "Nahoru",
        'merge_move_down': "Dolů",
        'merge_pdfs_info': "💡 Tip: Pořadí můžete změnit přetažením",
        'merge_no_pdfs': "Nebyla vybrána žádná PDF. Klikněte na 'Přidat PDF'.",
        'merge_info': "{0} PDF vybráno (přibližně {1} stránek)",
        'merge_open_file': "Otevřít soubor",
        'merge_merge': "Sloučit",
        'merge_error': "Chyba při slučování",
        'merge_min_two_pdfs_error': "Vyberte prosím alespoň dva PDF soubory ke sloučení.",
        'merge_select_pdfs': "Vybrat PDF ke sloučení",
        'merge_error_file': "Chyba při zpracování",
        'merge_cancelled': "Sloučení bylo zrušeno",
        'merge_preparing': "Příprava...",
        'merge_processing': "Zpracování PDF {0} z {1}",
        'merge_saving': "Ukládání sloučeného PDF...",
        'merge_complete': "Hotovo!",
        'merge_success_title': "Sloučení úspěšné",
        'merge_success_voice': "{0} PDF bylo úspěšně sloučeno.",
        'merge_success_message': "{0} PDF bylo úspěšně sloučeno.\n\nNový dokument má nyní {1} stránek.\n\nNový soubor:\n{2}\n\nMísto uložení:\n{3}\n{2}\n\nChcete toto PDF otevřít?",
        'replace_file_title': "Nahradit soubor?",
        'replace_file_message': "Již je otevřeno PDF. Chcete jej nahradit novým souborem?",
        'btn_yes': "Ano",
        'btn_no': "Ne",
        'filename_merge_suffix': "sloučeno",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Otevírání {0}...",
        'progress_merge_reading': "Čtení {0}...",
        'progress_merge_adding': "Přidávání {0} stránek...",
        'progress_merge_optimizing': "Optimalizace PDF...",
        'progress_merge_writing': "Zápis PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "zavření PDF",
        'action_close_window': "zavření okna",
        'action_open_new_pdf': "otevření nového PDF",
        'action_quit_app': "ukončení aplikace",
        'changes_saved': "Změny byly uloženy.",
        'file_close_title': "Zavřít PDF soubor",
        'save_before_action': "Mají být změny před {0} uloženy? Ano nebo Ne?",
        'save_before_action_voice': "Mají být změny před {0} uloženy? Ano nebo Ne?",
        'save_before_close_question': "Mají být změny před zavřením uloženy? Ano nebo Ne?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Vytvořen vyhledávatelný PDF:\n\n{0}\n\n<b>v případě potřeby zkuste znovu",
        "ocr_rotate_title": "Vyrovnání stránek před OCR",
        "ocr_rotate_question": "PDF obsahuje otočené stránky.\nChcete vyrovnat všechny stránky na 0° před OCR?\nToto výrazně zlepšuje rozpoznávání textu.",
        "ocr_rotate_yes": "Ano, vyrovnat",
        "ocr_rotate_no": "Ne, spustit OCR přímo",
        "ocr_rotate_voice": "PDF obsahuje otočené stránky. Mají být všechny stránky před OCR vyrovnány?",
        "ocr_not_performed_message": "Žádný text neexistuje. Proveďte OCR (nabídka \"Upravit\" → \"Provést OCR\" nebo klávesa Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Nastavení OCR",
        "ocr_language_btn": "Vybrat jazyk OCR",
        "ocr_language": "Jazyk(y) OCR",
        "ocr_language_current": "Aktuální jazyk:",
        "ocr_param_info": "Informace o parametru",

        "ocr_force_ocr_label": "Vynutit OCR",
        "ocr_deskew_label": "Opravit zešikmení",
        "ocr_clean_label": "Vyčistit obrázek",
        "ocr_oversample_label": "Rozlišení (DPI)",
        "ocr_pagesegmode_label": "Rozdělení stránky",
        "ocr_oem_label": "Režim OCR enginu",
        "ocr_optimize_label": "Komprese PDF",
        "ocr_jobs_label": "Paralelní procesy",
        "ocr_verbose_label": "Podrobnost logu",

        "ocr_force_ocr_tooltip": "Vynutit OCR na každé stránce, i když text již existuje",
        "ocr_deskew_tooltip": "Automaticky vyrovnat zešikmené skeny",
        "ocr_clean_tooltip": "Odstranit šum a artefakty z obrázku",
        "ocr_oversample_tooltip": "Zvětšit obrázek před OCR na toto DPI",
        "ocr_pagesegmode_tooltip": "Určuje, jak se stránka rozdělí na textové oblasti",
        "ocr_oem_tooltip": "Vybere OCR engine Tesseractu",
        "ocr_optimize_tooltip": "Úroveň komprese výstupního PDF",
        "ocr_jobs_tooltip": "Počet paralelních OCR procesů",
        "ocr_verbose_tooltip": "Úroveň podrobnosti výstupu logu",
        "ocr_settings_explain_btn": "Vysvětlení",

        "ocr_force_ocr_explain": "Vynutí rozpoznávání textu na <b>každé</b> stránce, i když již obsahuje text.\n\nDoporučení: <b>Zapnuto</b> pro skenované PDF, <b>Vypnuto</b> pro nativní PDF s již existujícím textem.",

        "ocr_deskew_explain": "Opravuje mírně zešikmené skeny (až asi 5°).\n\nDoporučení: <b>Zapnuto</b> pro skenované dokumenty, <b>Vypnuto</b> pokud jsou stránky již dokonale rovné.",

        "ocr_clean_explain": "Odstraňuje šum, tečky a malé artefakty z obrázku.\n<b>DŮLEŽITÉ:</b> Pro arabské, thajské nebo vietnamské texty s diakritickými znaménky (tečky nad/pod písmeny) by tato možnost měla být <b>vypnuta</b>, jinak mohou být ztraceny důležité znaky.",

        "ocr_oversample_explain": "Zvětší obrázek <b>před</b> rozpoznáváním textu na uvedené DPI.<br><br>• <b>72-150 DPI:</b> Velmi rychlé, ale nízká míra rozpoznávání<br>• <b>200-300 DPI:</b> Optimální rozsah (Standard: 300)<br>• <b>400+ DPI:</b> Téměř žádné lepší rozpoznávání, ale výrazně větší soubory<br><br>Doporučení: 300 DPI pro složitá písma (arabské, čínské, japonské), 200 DPI pro západní jazyky.",

        "ocr_pagesegmode_explain": "Určuje, jak Tesseract rozdělí stránku na textové oblasti.\n\n• <b>3 - Automaticky (Standard):</b> Dobré pro smíšené rozvržení\n• <b>4 - Jednotlivý sloupec:</b> Pro texty s jedním sloupcem\n• <b>5 - Vertikální blok:</b> Pro vertikální písma (japonské, čínské)\n• <b>6 - Jednotný textový blok:</b> Optimální pro plynulý text bez sloupců\n• <b>11 - Surový obrázek:</b> Pro špatné skeny / rukopisy\n\nDoporučení: <b>6</b> pro jednoduché textové dokumenty, <b>3</b> pro složitá rozvržení.",

        "ocr_oem_explain": "Vybere OCR engine Tesseractu.\n\n• <b>0 - Legacy:</b> Starý engine (rychlý, ale méně přesný)\n• <b>1 - LSTM:</b> Neuronový engine (pomalejší, ale přesnější)\n• <b>2 - Legacy + LSTM:</b> Kombinuje oba výsledky\n• <b>3 - Standard (LSTM preferován):</b> Nejlepší volba pro většinu případů\n\nDoporučení: <b>3</b> pro maximální přesnost rozpoznávání.",

        "ocr_optimize_explain": "Komprimuje výstupní PDF.\n\n• <b>0:</b> Žádná optimalizace (nejrychlejší zpracování)\n• <b>1:</b> Lehká optimalizace (dobrý kompromis)\n• <b>2:</b> Mírná optimalizace\n• <b>3:</b> Silná optimalizace (nejmenší soubor, ale pomalejší)\n\nDoporučení: <b>1</b> pro každodenní použití.",

        "ocr_jobs_explain": "Počet paralelních procesů pro OCR.\n\n• <b>1:</b> Pomalé, ale nejnižší spotřeba paměti\n• <b>4-8:</b> Optimální pro moderní vícejádrové procesory\n• <b>12+:</b> Téměř žádné rychlejší zpracování při vysoké spotřebě paměti\n\nDoporučení: Počet CPU jader (např. <b>4</b> na 4jádrových systémech).",

        "ocr_verbose_explain": "Úroveň podrobnosti výstupu logu v konzoli.\n\n• <b>0:</b> Žádný výstup\n• <b>1:</b> Průběh a stavové zprávy\n• <b>2:</b> Podrobný výstup\n• <b>3:</b> Úplný debug výstup (velmi obsáhlý)\n\nDoporučení: <b>1</b> pro normální provoz.",

        "ocr_reset_title": "Nastavení bylo resetováno",
        "ocr_reset_message": "Všechna nastavení OCR byla resetována na výchozí hodnoty.",
        "info_tooltip": "Více informací o tomto parametru",
        "ocr_reset_defaults": "Resetovat na výchozí",

        "ocr_psm_0": "Automaticky (Legacy engine)",
        "ocr_psm_1": "Automatické rozpoznávání sloupců",
        "ocr_psm_3": "Automaticky (Standard)",
        "ocr_psm_4": "Jednotlivý sloupec",
        "ocr_psm_5": "Vertikální blok",
        "ocr_psm_6": "Jednotný textový blok",
        "ocr_psm_7": "Jednotlivý řádek textu",
        "ocr_psm_8": "Jednotlivé slovo",
        "ocr_psm_11": "Surový obrázek (bez analýzy rozvržení)",

        "ocr_oem_0": "Legacy engine (rychlý)",
        "ocr_oem_1": "LSTM engine (neuronový, přesný)",
        "ocr_oem_2": "Legacy + LSTM kombinovaný",
        "ocr_oem_3": "Standard (LSTM preferován)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Jazyk(y) OCR...",
        "ocr_language_title": "Vybrat jazyk(y) OCR",
        "ocr_language_instruction": "Vyberte jazyk(y) pro rozpoznávání textu (OCR).\nPozor: Více jazyků jde na úkor výkonu a přesnosti!\nNejlepších výsledků dosáhnete, pokud vyberete pouze jeden jazyk.",
        "ocr_language_predefined": "Předdefinované kombinace",
        "ocr_language_custom": "Vlastní...",
        "ocr_language_selected": "Vybrané OCR jazyky",
        "ocr_language_changed": "OCR jazyk změněn na {0}",
        "ocr_language_auto_detect": "Dostupné jazyky jsou automaticky rozpoznávány.",
        "ocr_language_none_found": "Nenalezena žádná jazyková data Tesseractu! Nainstalujte jazykové balíčky (např. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Vlastní výběr jazyka",
        "ocr_language_available": "Dostupné jazyky (nainstalované):",
        "ocr_language_select_hint": "Vyberte jeden nebo více jazyků:",
        "ocr_language_confirm": "Použít",
        "ocr_language_reset": "Resetovat na výchozí (deu+eng+vie)",
        "ocr_language_priorities": "Doporučené jazyky (předinstalované):",

        "select_all_languages": "Vybrat vše",
        "clear_all_languages": "Zrušit výběr",
        "install_language_packs": "Nainstalovat chybějící jazykové balíčky...",
        "install_hint": "💡 Tip: Ne všechny jazyky jsou nainstalovány ve vašem systému. Pomocí tohoto tlačítka získáte pomoc s instalací.",
        "ocr_language_install_title": "Instalace jazykových balíčků Tesseract",

        "ocr_missing_languages": "Chybějící jazykové balíčky OCR",
        "ocr_missing_languages_message": "Následující vybrané jazyky nejsou nainstalovány ve vašem systému:\n\n{0}\n\nNainstalujte chybějící jazykové balíčky (viz nápověda v 'Nápověda k instalaci').\n\nChcete nyní otevřít nápovědu k instalaci?",
        "ocr_missing_languages_voice": "Chybějící jazykové balíčky. Nainstalujte chybějící jazyky.",
        "ocr_install_help_now": "Otevřít nápovědu",
        "ocr_continue_anyway": "Přesto zkusit",
        "ocr_language_error_title": "Chyba jazyka OCR",
        "ocr_language_error_message": "Chyba při rozpoznávání textu: {0}\n\nZkontrolujte své nastavení jazyka OCR (Nastavení → Jazyk OCR).",
        "ocr_install_help_button": "Nápověda k instalaci",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalace jazykových balíčků Tesseract</p>

        <p>Aby OCR fungovalo v určitém jazyce, musí být ve vašem systému nainstalována odpovídající jazyková data. Postupujte podle pokynů pro váš operační systém:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Otevřete <strong>Terminál</strong> (Finder → Programy → Utility → Terminál).</li>
        <li>Nainstalujte všechny dostupné jazyky pomocí:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
>(To může trvat několik minut.)</li>
        <li>Nebo pouze jednotlivé jazyky (např. vietnamštinu):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
U současných verzí Homebrew může být nutné stáhnout <code>*.traineddata</code> ručně (viz níže).</li>
        <li>Po instalaci: Zavřete tento dialog a znovu otevřete výběr jazyka OCR – nové jazyky se automaticky objeví.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Otevřete terminál (Ctrl+Alt+T).</li>
        <li>Nainstalujte požadovaný jazyk, např. pro vietnamštinu:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
Důležité jazykové kódy: <code>deu</code> (němčina), <code>eng</code> (angličtina), <code>vie</code> (vietnamština), <code>spa</code> (španělština), <code>fra</code> (francouzština), <code>ita</code> (italština), <code>nld</code> (holandština), <code>fin</code> (finština), <code>swe</code> (švédština), <code>nor</code> (norština).</li>
        <li>Zobrazit všechny dostupné balíčky:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ručně)</p>
        <ol>
        <li>Stáhněte požadované soubory <code>*.traineddata</code> z:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
(např. <code>vie.traineddata</code> pro vietnamštinu).</li>
        <li>Zkopírujte soubory do složky jazyků Tesseract, obvykle:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
(Přizpůsobte individuální instalaci.)</li>
        <li>Restartujte aplikaci (nebo znovu otevřete výběr jazyka OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternativa pro všechny systémy</p>
        <ul>
        <li>Nainstalujte <strong>OCRmyPDF</strong> a <strong>Tesseract</strong> pomocí správce balíčků dle vašeho výběru. Většina instalací již obsahuje některé standardní jazyky (angličtinu, němčinu, francouzštinu).</li>
        <li>Chybějící jazyky lze kdykoli doinstalovat – výběr jazyka OCR zobrazuje pouze skutečně existující jazyky.</li>
        </ul>

        <hr>
        <p><b>✅ Po instalaci:</b> Není třeba restartovat aplikaci – nově přidané jazyky se okamžitě objeví v seznamu.</p>
        <p><b>📖 Nápověda k jazykovým kódům:</b> Úplný seznam naleznete v <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentaci Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Písma Noto Sans",
        "info_noto_font_voice": "Průvodce instalací písem Noto Sans",
        "btn_info_noto_font_install": "Informace o písmu",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Jak nainstalovat bezplatná písma Noto od Google</h2>

        <p><strong>Písma Noto</strong> jsou rodina písem s otevřeným zdrojovým kódem od Google. Jejich cílem je nevidět <em>"žádné tofu"</em> (tj. žádné prázdné čtverečky □) a správně zobrazit každý znak ze standardu Unicode. Jsou ideálním doplňkem pro aplikace, které musí zobrazovat texty v mnoha různých jazycích.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalace na macOS</h3>

        <p><strong>Metoda 1: S Homebrew (pro pokročilé)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metoda 2: Přes "Knihu písem" (Doporučeno)</strong></p>

        <ol>
        <li>Stáhněte oficiální balíček písem:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Rozbalte soubor ZIP</li>
        <li>Zkopírujte soubory do <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalace na Windows (10 & 11)</h3>

        <p><strong>Metoda 1: Microsoft Store (Doporučeno)</strong><br>
Vyhledejte "Google Noto Fonts" nebo "Noto Sans" a klikněte na <strong>Nainstalovat</strong>.</p>

        <p><strong>Metoda 2: Ruční instalace</strong></p>

        <ol>
        <li>Stažení:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Rozbalte ZIP</li>
        <li>Vyberte soubory .ttf / .otf</li>
        <li>Pravé tlačítko → <strong>Nainstalovat</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        nebo<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Jméno\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalace na Linux</h3>

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

        <p>Ověření:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Správa záložek",
        "bookmark_add": "Přidat záložku",
        "bookmark_add_tooltip": "Uložit aktuální stránku jako záložku",
        "bookmark_remove": "Odstranit záložku",
        "bookmark_remove_tooltip": "Smazat označenou záložku",
        "bookmark_remove_all": "Odstranit vše",
        "bookmark_remove_all_tooltip": "Smazat všechny záložky tohoto PDF",
        "bookmark_jump": "Přejít na záložku",
        "bookmark_jump_tooltip": "Přejít na vybranou stránku",
        "bookmark_name": "Název",
        "bookmark_page": "Stránka",
        "bookmark_no_bookmarks": "Žádné záložky neexistují.\nKliknutím na 'Přidat' uložíte aktuální stránku jako záložku.",
        "bookmark_added": "Záložka pro stránku {0} přidána: {1}",
        "bookmark_removed": "Záložka odstraněna: {0}",
        "bookmark_all_removed": "Všechny záložky byly odstraněny.",
        "bookmark_name_default": "Stránka {0}",
        "bookmark_name_prompt": "Název záložky:\n(dlouhý text bude zkrácen na 50 znaků)",
        "bookmark_name_prompt_title": "Název záložky",
        "bookmark_confirm_remove_all": "Opravdu chcete odstranit všech {0} záložek?",
        "menu_bookmarks": "Záložky",
        "bookmark_manage": "Správa záložek",
        "bookmark_next": "Další záložka",
        "bookmark_prev": "Předchozí záložka",
        "bookmark_page_display": "Stránka {0}",
        "bookmark_exists": "Záložka pro tuto stránku s tímto názvem již existuje.",
        "bookmark_select_first": "Nejprve vyberte záložku.",
        "bookmark_confirm_remove": "Opravdu chcete odstranit záložku 'Stránka {0}: {1}'?",
        "bookmark_jumped_to": "Přejít na záložku '{0}' na stránce {1}.",
        "bookmark_jumped_to_voice": "Záložka {0}, stránka {1}",
        "btn_close": "Zavřít",

        "bookmark_list": "Vaše záložky",
        "bookmark_rename": "Přejmenovat záložku",
        "bookmark_rename_tooltip": "Změnit název vybrané záložky",
        "bookmark_rename_title": "Přejmenovat záložku",
        "bookmark_rename_prompt": "Nový název záložky na stránce {0}:\n(max. 50 znaků)",
        "bookmark_renamed": "Záložka '{0}' byla přejmenována na '{1}'.",
        "bookmark_item_tooltip": "Stránka {0}: {1}\nDvojklikem přejdete",
        "bookmark_name_exists_question": "Záložka s názvem '{0}' již na této stránce existuje.\nPřesto přejmenovat?",

        "context_bookmarks": "Záložky",
        "context_bookmark_add_here": "Přidat záložku pro tuto stránku",
        "context_bookmarks_existing": "Existující záložky:",
        "context_bookmarks_jump": "Přejít na záložku:",
        "context_bookmarks_none": "Žádné záložky neexistují",
        "context_bookmarks_clear_all": "Odstranit všech {0} záložek",

        "bookmark_search_placeholder": "Hledat záložky... (název nebo stránka)",
        "bookmark_search_results": "Nalezeno %d záložek pro \"%s\"",
        "bookmark_no_search_results": "Pro \"%s\" nebyly nalezeny žádné záložky",
        "bookmark_no_search_results_label": "Žádné výsledky pro \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Upravit PDF metadata",
        "metadata_title": "Název",
        "metadata_title_placeholder": "Název dokumentu",
        "metadata_title_tooltip": "Název dokumentu (zobrazuje se v záhlaví)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Jméno autora",
        "metadata_author_tooltip": "Tvůrce dokumentu",
        "metadata_subject": "Předmět",
        "metadata_subject_placeholder": "Předmět dokumentu",
        "metadata_subject_tooltip": "Stručný popis obsahu",
        "metadata_keywords": "Klíčová slova",
        "metadata_keywords_placeholder": "Klíčová slova oddělená čárkami",
        "metadata_keywords_tooltip": "Klíčová slova pro kategorizaci dokumentu",
        "metadata_creator": "Vytvořil",
        "metadata_creator_placeholder": "Aplikace, která vytvořila PDF",
        "metadata_creator_tooltip": "Software, se kterým byl dokument vytvořen",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Aplikace, která převedla PDF",
        "metadata_producer_tooltip": "Software, který převedl PDF",
        "metadata_creation_date": "Datum vytvoření",
        "metadata_creation_date_tooltip": "Datum vytvoření dokumentu",
        "metadata_mod_date": "Datum změny",
        "metadata_mod_date_tooltip": "Datum poslední změny",
        "metadata_pdf_info": "📄 Informace o PDF",
        "metadata_pages": "Počet stránek",
        "metadata_file_size": "Velikost souboru",
        "metadata_pdf_version": "Verze PDF",
        "metadata_encrypted": "Zašifrováno",
        "metadata_encrypted_yes": "Ano (chráněno heslem)",
        "metadata_encrypted_no": "Ne",
        "metadata_reload": "📂 Znovu načíst z PDF",
        "metadata_reset": "Zahodit změny",
        "metadata_reloaded": "Metadata byla znovu načtena z PDF.",
        "metadata_reset_done": "Všechna pole metadat byla resetována.",
        "metadata_no_file": "Není načten žádný PDF soubor.",
        "metadata_save_error": "Chyba při ukládání metadat",
        "metadata_saved": "Metadata byla úspěšně uložena.",
        "metadata_pdf_version_unknown": "PDF (neznámé)",
        "metadata_saved_message": "Metadata byla úspěšně uložena.",
        "metadata_saved_voice": "Metadata uložena.",

        "metadata_custom": "🔧 Vlastní metadata",
        "metadata_custom_placeholder": "{\n  \"moje_pole\": \"moje hodnota\",\n  \"jiné_pole\": 123\n}",
        "metadata_custom_tooltip": "JSON formát pro vlastní metadata (volitelné)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Šablona \"{0}\" vybrána - Dvojklikem vložíte",
        "text_use_template": "Použít textový blok",
        "text_type": "Typ",
        "text_search_templates": "Hledat textové bloky...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informace o exportu / importu",
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

        <h3>📦 Co se exportuje? (Přehled)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Obecná nastavení aplikace</span></li>
            <li class="detail">• Tmavý/Světlý režim</li>
            <li class="detail">• Invertování obrázků v tmavém režimu</li>
            <li class="detail">• Šedá prahová hodnota</li>
            <li class="detail">• Jazyk</li>
            <li class="detail">• Geometrie okna</li>
            <li class="detail">• Režim přiblížení</li>
            <li class="detail">• Navigace (Navigační lišta viditelná)</li>
            <li class="detail">• Hlasový výstup (zapnuto/vypnuto)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavení zálohování</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Pojmenování souborů (Časové razítko, Oddělovač, Přípony)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavení pro vkládání</span></li>
            <li class="detail">• Podpisy</li>
            <li class="detail">• Text &amp; textové bloky</li>
            <li class="detail">• Zaškrtnutí, obrázky a tvary</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavení OCR</span></li>
            <li class="detail">• Jazyk</li>
            <li class="detail">• Vynutit OCR · Režim stránky</li>
            <li class="detail">• Předzpracování obrázku: Oprava zešikmení, Vyčištění, Vzorkování</li>
            <li class="detail">• Počet paralelních úloh</li>
            <li class="detail">• Režim invertování</li>
            <li class="detail">• Šedá prahová hodnota</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Záložky</span></li>
            <li class="detail">• Všechny záložky na soubor PDF (Stránka, Název, Čas vytvoření)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Databáze hesel</span></li>
            <li class="detail">• Uložená PDF hesla (volitelně šifrovaná nebo prostý text)</li>
            <li class="detail">• Hash hlavního hesla (pokud je nastaveno)</li>
            <li class="detail">• Ověřovací údaje</li>
        </ul>

        <h4>⚠️ Důležité poznámky</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Při importu:</strong>
            <ul>
                <li><span class="warning">➜ VŠECHNA aktuální nastavení budou zcela přepsána</span></li>
                <li>• Restartování aplikace je povinné</li>
                <li>• Existující podpisy, textové bloky a záložky budou nahrazeny</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Hlavní heslo a režim exportu:</strong>
            <ul>
                <li>• Když je hlavní heslo aktivní, můžete si vybrat:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dešifrováno</strong></span> (hesla jsou v prostém textu v ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Šifrováno</strong></span> (lze číst pouze s hlavním heslem na cílovém systému)</li>
                <li>• Hash hlavního hesla je <strong>vždy</strong> ukládán šifrovaně</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Bezpečnostní upozornění:</strong>
            <ul>
                <li>• Exportovaný soubor ZIP obsahuje citlivá data (<strong>hesla, záložky, podpisy</strong>)</li>
                <li>• Uchovávejte jej v bezpečí (např. šifrovaný USB klíč, správce hesel)</li>
                <li>• Pokud soubor ztratíte, uložená PDF hesla jsou nenávratně ztracena</li>
            </ul>
        </div>

        <h4>📁 Formát exportu</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Nastavení se ukládají do jednoho souboru ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Tento ZIP obsahuje kompletní <code>settings.json</code> (z vaší konfigurace) a případně vložené soubory obrázků podpisů a šifrovaná hesla.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Podpisy - Průvodce",
        'signature_guide_html': """
        📝 <strong>Podpisy - Rychlý průvodce</strong><br>
        <ul>
        <li>Nastavte hlavní heslo</li>
        <li>Nakonfigurujte podpisy v nabídce <em>Nastavení</em> (velikost, časové razítko, …)</li>
        <li>Vložení pomocí <strong>PRAVÉHO TLAČÍTKA</strong> na požadovanou pozici (hlavní heslo vyžadováno jednou za relaci)</li>
        <li>Přesuňte podpis myší nebo šipkami</li>
        <li>Vložte několik podpisů za sebou</li>
        <li>Přizpůsobte každý podpis individuálně</li>
        <li>Zahoďte jednotlivý podpis</li>
        <li>Uložte / zahoďte všechny podpisy najednou</li>
        <<li>Alternativně lze použít i lištu nabídek.</li>
        </ul>
        """,
        'signature_guide_voice': "Rychlý průvodce podpisy. Nastavte hlavní heslo. Nakonfigurujte podpisy v nastavení. Vložte pravým tlačítkem.",

        'image_guide_title': "Vkládání obrázků - Průvodce",
        'image_guide_html': """
        📷 <strong>Vkládání obrázků do PDF - Rychlý průvodce</strong><br>
        <ol>
        <li>Pravé tlačítko na požadované pozici</li>
        <li><em>„Vložit obrázek“</em> → Vyberte obrázek</li>
        <li>Umístěte obrázek: Přetáhněte myší</li>
        <li>Upravte velikost: Přetáhněte za rohy/hrany</li>
        <li>Zachovejte poměr stran: Klávesa <strong>[A]</strong></li>
        <li>Další úpravy: Pravé tlačítko na obrázku</li>
        </ol>
        <p><strong>Tip:</strong> V kontextové nabídce můžete upravit nastavení.</p>
        """,
        'image_guide_voice': "Rychlý průvodce obrázky. Pravé tlačítko, vložit obrázek, vyberte. Umístěte myší, upravte velikost na rozích. Poměr stran klávesou A.",

        'form_guide_title': "Vkládání tvarů - Průvodce",
        'form_guide_html': """
        📐 <strong>Vkládání tvarů do PDF - Rychlý průvodce</strong><br>
        <ol>
        <li>Vyberte typ tvaru (obdélník, elipsa, čára, šipka)</li>
        <li>Klikněte na pozici:
            <ul>
            <li>U obdélníku/elipsy: Jedno kliknutí umístí tvar</li>
            <li>U čáry/šipky: Dvě kliknutí pro počáteční a koncový bod</li>
            </ul>
        </li>
        <li>Umístěte tvar: Přetáhněte myší</li>
        <li>Upravte velikost: Přetáhněte za rohy/hrany</li>
        <li>Uložte tvar: <strong>Enter</strong></li>
        <li>Zahoďte tvar: <strong>ESC</strong></li>
        <li>Další úpravy: Pravé tlačítko na tvaru</li>
        </ol>
        <p><strong>Tip:</strong> V kontextové nabídce můžete upravit nastavení.</p>
        """,
        'form_guide_voice': "Rychlý průvodce tvary. Vyberte typ tvaru. U obdélníku nebo elipsy klikněte jednou, u čáry nebo šipky dvakrát. Umístěte myší, upravte velikost na rozích. Uložte Enterem, zahoďte Esc.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "předchozí",
        "btn_next_result": "další",
        "ocr_text_window": "OCR textové okno",
        "bookmark_existing": "Existující záložky",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR srovnání Mac - Windows",
        'ocr_method_mac_win_title': "OCR rozdíly mezi Macem a Windows",
        'ocr_method_mac_win_voice': "Mac je lepší",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Rozdíly mezi macOS a Windows</strong></p>

        <p><strong>macOS (doporučeno)</strong></p>
        <p>Nástroj:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Výsledek:</p>
        <ul>
        <li>Prohledávatelné PDF s vloženým textem, které do značné míry zachovává původní rozvržení.</li>
        </ul>
        <p>Výhody:</p>
        <ul>
        <li>Vynikající kvalita rozpoznávání textu (i u nakloněných stránek).</li>
        <li>Zachování vektorové grafiky a písem.</li>
        <li>Lišta průběhu GUI prostřednictvím vyhodnocování podprocesu.</li>
        <li>Plná kontrola nad všemi parametry OCR (Deskew, Clean, Oversample, optimalizace).</li>
        <li>Vyhledávání textu je přímo dostupné v hlavním okně (zobrazení PDF).</li>
        </ul>
        <p>Nevýhody:</p>
        <ul>
        <li>Vyžaduje další systémové nástroje (ocrmypdf, Ghostscript, unpaper, pngquant – obsaženo v App Bundle).</li>
        <li>Složitější zpracování chyb (zablokování, časové limity).</li>
        </ul>

        <p><strong>Windows (stabilní alternativa)</strong></p>
        <p>Nástroj:</p>
        <ul>
        <li>pytesseract (přímé připojení k Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Výsledek:</p>
        <ul>
        <li>Prohledávatelné PDF, které vizuálně odpovídá obrázkovému PDF, ale je prohledávatelné díky průhlednému textu.</li>
        </ul>
        <p>Výhody:</p>
        <ul>
        <li>Žádné mě teď nenapadají.</li>
        </ul>
        <p>Nevýhody:</p>
        <ul>
        <li>PDF je v podstatě obrázek s neviditelným textem; rozvržení se může u složitých dokumentů (sloupce, tabulky) mírně lišit.</li>
        <li>Žádná automatická korekce zkosení (--deskew) nebo čištění obrázku (--clean).</li>
        <li>Lišta průběhu GUI se aktualizuje pouze hrubě na základě počtu zpracovaných stránek.</li>
        <li>Rychlost OCR je mírně pomalejší (protože každá stránka je zpracovávána samostatně).</li>
        <li>Vyhledávání textu je přesměrováno do OCR textového okna.</li>
        </ul>

        <p><strong>Společné rysy</strong></p>
        <ul>
        <li>Oba procesy vytvářejí prohledávatelné PDF ve stejném adresáři jako zdrojový soubor.</li>
        <li>Nastavení OCR (jazyk, DPI, režim segmentace stránky, režim enginu OCR) lze nakonfigurovat přes OCRSettingsDialog a platí v obou implementacích.</li>
        </ul>

        <p><strong>Doporučení:</strong></p>
        <ul>
        <li>macOS: Binární soubor ocrmypdf poskytuje nejlepší výsledky – Pořiďte si Mac a používejte verzi (PDFDarkView pro Macy s čipem Apple Silicon nebo Intel). Výsledky OCR jsou lepší než ve Windows!</li>
        <li>Windows: Použijte řešení pytesseract. Je stabilní a poskytuje pro většinu dokumentů zcela dostatečnou kvalitu.</li>
        </ul>

        <p><strong>Důležitá poznámka:</strong></p>
        <ul>
        <li>Obě verze jsou plně integrovány do uživatelského rozhraní – uživatel nepozoruje žádný rozdíl.</li>
        <li>Program automaticky rozhoduje, který engine OCR se použije, na základě operačního systému.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Vytvořit podpis (ze skenu)",
        "signature_create_title": "Vyberte skenovaný podpis (PDF/obrázek)",
        "image_pdf_filter": "Obrázky a PDF",
        "signature_pdf_empty": "PDF neobsahuje žádné stránky.",
        "signature_created_success": "Podpis byl úspěšně vytvořen: {0}",
        "signature_create_error": "Chyba při vytváření podpisu:\n{0}",
        "rembg_missing": "rembg není nainstalováno.\nNainstalujte prosím: pip install rembg\nChyba: {0}",
        "signature_name_title": "Název souboru pro podpis",
        "signature_name_message": "Zadejte prosím název souboru pro nový podpis (bude uložen jako PNG s průhledným pozadím):",
        "signature_name_label": "Název souboru:",
        "signature_name_voice": "Zadejte název souboru pro podpis",
        "signature_processing": "Zpracování probíhá...",
        "signature_creation_title": "Podpis se vytváří",
        "signature_overwrite_warning": "Soubor '{0}' již existuje. Přepsat?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Připravit PDF pro podpis",
        "signature_prepare_instruction":"Vyberte prosím PDF, které obsahuje na jedné stránce skenovaný podpis.\n\nOptimálního rozpoznání dosáhnete, pokud:\n• Podpis je napsán černým inkoustem (propiska nebo fineliner) na bílém papíře.\n• Podpis se nachází v horní třetině jinak prázdné stránky A4.\n• PDF bylo skenováno alespoň s 300 dpi.\n• Podpis je jasný a není příliš tenký.\n• Nejsou přítomny rušivé vzory pozadí nebo čáry.",
        "signature_prepare_voice":"Vyberte prosím PDF se skenovaným podpisem. Dbejte na dobrou kvalitu a kontrast.",
        "sig_thickness_label":"Tloušťka čáry:",
        "sig_thickness_normal":"Normální (tenká)",
        "sig_thickness_bold":"Tučná (doporučeno)",
        "sig_thickness_very_bold":"Velmi tučná",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Přidání jazyků GUI a OCR - Průvodce",
        'language_guide_title': "Přidání jazyků GUI a OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Stáhněte požadovaný překladový soubor <code>translations_xy.py</code> z<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        a umístěte jej do následujícího adresáře:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Otevřete svůj webový prohlížeč.</li>
        <li>Přejděte na: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Na pravém okraji obrazovky vyhledejte "Releases" a vyberte to označené <strong>"latest"</strong>.</li>
        <li>Na následující stránce vydání stáhněte úplně dole soubor <code>Source Code.zip</code>.</li>
        <li>Rozbalte soubor ZIP.</li>
        <li>V rozbalené složce vyhledejte všechny jazykové soubory, které potřebujete, a zkopírujte je do adresáře:<br/>
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
        "menu_watermark":"Vložit vodoznak",
        "fullpage_text_watermark_title":"Text jako vodoznak",
        "fullpage_image_watermark_title":"Obrázek jako vodoznak",
        "filename_with_watermark":"_s_vodoznakem",
        "watermark_text":"Text:",
        "watermark_text_placeholder":"Váš text vodoznaku...",
        "watermark_font_family":"Písmo:",
        "watermark_font_size":"Velikost písma:",
        "watermark_format":"Formátování:",
        "watermark_bold":"Tučné",
        "watermark_italic":"Kurzíva",
        "watermark_color":"Barva:",
        "watermark_choose_color":"Vyberte barvu...",
        "watermark_opacity":"Neprůhlednost / Průhlednost:",
        "watermark_direction":"Směr čtení:",
        "watermark_direction_l_r":"Zleva → Doprava",
        "watermark_direction_bl_tr":"Dole vlevo → Nahoře vpravo",
        "watermark_direction_tl_br":"Nahoře vlevo → Dole",
        "watermark_direction_b_t":"Dole → Nahoru",
        "watermark_direction_t_b":"Nahoru → Dolů",
        "watermark_preview":"Náhled:",
        "watermark_preview_sample":"Ukázkový text",
        "watermark_empty_text":"Zadejte prosím text.",
        "watermark_applied":"Vodoznak byl aplikován na všechny stránky.",
        "watermark_saved":"Vodoznak byl uložen.",
        "image_scale":"Velikost:",
        "image_preview":"Náhled obrázku:",
        "no_image_selected":"Nebyl vybrán žádný obrázek",
        "browse":"Procházet...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redakce",
        "redact_add_black": "Redakce (černá)",
        "redact_add_white": "Redakce (bílá / vymazání)",
        "redact_added_black": "Přidána černá redakce",
        "redact_added_white": "Přidána bílá redakce",
        "redact_apply_all": "Použít všechny redakce a uložit",
        "redact_discard_all": "Zahodit všechny redakce",
        "redact_discard": "Zahodit tuto redakci",
        "no_redactions": "Žádné redakce",
        "redact_confirm_title": "Trvale použít redakce",
        "redact_confirm_message": "Varování: Označené oblasti budou nenávratně smazány (černé nebo bílé).\nBude vytvořena záloha (pokud je povolena).\n\nPokračovat?",
        "redact_apply": "Ano, redigovat nyní",
        "redact_saved": "{0} redakce úspěšně použito a uloženo.",
        "redact_saved_voice": "{0} redakce použito",
        "redact_error": "Chyba při redakci",
        "filename_redacted":"_redigovano",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Vložit čísla stránek',
        'page_numbers_format': 'Formát čísel:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabské)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (římské malé)',
        'page_numbers_format_roman_upper': 'I, II, III ... (římské velké)',
        'page_numbers_format_letter': 'A, B, C ... (písmena)',
        'page_numbers_format_custom': 'Vlastní',
        'page_numbers_custom_pattern': 'Vzor:',
        'page_numbers_custom_placeholder': 'např. "Strana {nummer}" nebo "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Použijte {nummer} pro aktuální číslo stránky a {total} pro celkový počet',
        'page_numbers_position': 'Pozice:',
        'page_numbers_pos_tl': 'Vlevo nahoře',
        'page_numbers_pos_tc': 'Uprostřed nahoře',
        'page_numbers_pos_tr': 'Vpravo nahoře',
        'page_numbers_pos_ml': 'Vlevo uprostřed',
        'page_numbers_pos_mc': 'Vycentrováno',
        'page_numbers_pos_mr': 'Vpravo uprostřed',
        'page_numbers_pos_bl': 'Vlevo dole',
        'page_numbers_pos_bc': 'Uprostřed dole',
        'page_numbers_pos_br': 'Vpravo dole',
        'page_numbers_margins': 'Okraje:',
        'page_numbers_margin_x': 'Horizontální vzdálenost:',
        'page_numbers_margin_y': 'Vertikální vzdálenost:',
        'page_numbers_range': 'Rozsah stránek:',
        'page_numbers_all_pages': 'Všechny stránky',
        'page_numbers_custom_range': 'Vlastní rozsah',
        'page_numbers_from': 'Od:',
        'page_numbers_to': 'Do:',
        'page_numbers_progress': 'Vkládání čísel stránek...',
        'page_numbers_start': 'Spouštění vkládání čísel stránek...',
        'page_numbers_cancel': 'Vkládání čísel stránek zrušeno',
        'page_numbers_success': 'Čísla stránek byla úspěšně přidána.\n\nChcete otevřít nové PDF?\n\n{0}',
        'page_numbers_complete': 'Čísla stránek byla přidána',
        'page_numbers_error_format': 'Chyba při vkládání čísel stránek: {0}',
        'page_numbers_content_type': 'Typ obsahu:',
        'page_numbers_tab_simple': 'Jednoduché číslo',
        'page_numbers_tab_range': 'Strana X z Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Volný text',
        'page_numbers_range_format': 'Formát:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Strana {aktuell} z {gesamt}',
        'page_numbers_range_custom': 'Vlastní',
        'page_numbers_range_placeholder': 'např. "Strana {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Formát data:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. ledna 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Vlastní',
        'page_numbers_date_placeholder': 'např. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Pozice:',
        'page_numbers_date_before': 'Datum před číslem stránky',
        'page_numbers_date_after': 'Datum za číslem stránky',
        'page_numbers_date_only': 'Pouze datum (bez čísla stránky)',
        'page_numbers_custom_text': 'Vlastní text:',
        'page_numbers_custom_placeholder_text': 'Použijte {seite} pro číslo stránky a {gesamt} pro celkový počet\nnapř. "Důvěrné - Strana {seite}" nebo "{seite} z {gesamt}"',
        "filename_with_page_number":"_s_cislem_stranky",
        "filename_with_page_declaration":"_s_oznacenim_stranky",
        "filename_with_pagenumber":"_s_cislem_stranky",
        "filename_with_date":"_s_datem",
        "filename_with_my_page_declaration":"_s_vlastnim_oznacenim",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Neuložené změny",
        "unsaved_changes_message_darkmode": "Existují neuložená vložení.\nChcete je před přepnutím uložit?",
        "save_and_switch": "Uložit a přepnout",
        "discard_and_switch": "Přepnout nyní",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Exportovat stránky jako obrázky',
        'export_images_menu': 'Exportovat jako obrázky (PNG/JPEG)',
        'export_images_format': 'Formát obrázku:',
        'export_images_dpi': 'Rozlišení (DPI):',
        'export_images_quality': 'Kvalita JPEG:',
        'export_images_range': 'Rozsah stránek:',
        'export_images_all_pages': 'Všechny stránky',
        'export_images_custom_range': 'Vlastní rozsah',
        'export_images_from': 'Od:',
        'export_images_to': 'Do:',
        'export_images_options': 'Možnosti:',
        'export_images_single_files': 'Každá stránka jako samostatný soubor',
        'export_images_subfolder': 'Exportovat do podsložky',
        'export_images_subfolder_info': 'Do podsložky "nazevPDF_obrazky"',
        'export_images_same_folder': 'Ve stejné složce jako PDF',
        'export_images_apply_darkmode': 'Použít nastavení PDFDarkView (Tmavý režim)',
        'export_images_target_folder': 'Cílová složka:',
        'export_images_browse': 'Procházet...',
        'export_images_preview': 'Náhled:',
        'export_images_preview_info': 'Vyberte nastavení pro export',
        'export_images_preview_info_detail': '{0} stránek jako {1}\nRozlišení: {2} DPI\nNázev souboru: {3}\n{4}',
        'export_images_select_folder': 'Vyberte cílovou složku',
        'export_images_start': 'Spouštění exportu obrázků...',
        'export_images_progress': 'Export obrázků...',
        'export_images_saving': 'Ukládání stránky {0} z {1}...',
        'export_images_success': 'Export úspěšný!\n\n{0} obrázků bylo uloženo do:\n{1}',
        'export_images_complete': 'Export obrázků dokončen',
        'export_images_open_folder': '📁 Otevřít složku',
        'export_images_cancel': 'Export obrázků zrušen',
        'export_images_error_format': 'Chyba při exportu obrázků: {0}',
        'export_images_pdf2image_missing': 'Knihovna "pdf2image" není nainstalována.\n\nProsím nainstalujte ji pomocí:\npip install pdf2image\n\nPro Windows potřebujete také Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konverze pro dlouhodobou archivaci',
        'pdfa_menu': 'PDF/A konverze (vhodné pro archiv)',
        'pdfa_info': 'Převádí PDF do formátu PDF/A.\n\nPDF/A je speciálně vyvinut pro dlouhodobou archivaci a zajišťuje, že dokument bude v budoucnu správně zobrazen.',
        'pdfa_standard': 'PDF/A standard:',
        'pdfa_standard_select': 'Verze:',
        'pdfa_1': 'PDF/A-1 (jednoduchý, široce kompatibilní)',
        'pdfa_2': 'PDF/A-2 (moderní, lepší komprese)',
        'pdfa_3': 'PDF/A-3 (nejnovější verze, povoluje přílohy)',
        'pdfa_standards_explanation': '📖 Vysvětlení standardů:\n\n'
            '• PDF/A-1: Základní, kompatibilní se staršími systémy (cca 2005)\n'
            '• PDF/A-2: Modernější, lepší komprese, podpora průhlednosti (cca 2011)\n'
            '• PDF/A-3: Nejnovější verze, povoluje vkládání příloh (cca 2013)\n\n'
            'Doporučení: PDF/A-2 je dobrý kompromis mezi kompatibilitou a moderními funkcemi.',
        'pdfa_options': 'Možnosti:',
        'pdfa_compress_enable': 'Komprimovat PDF (menší soubor)',
        'pdfa_metadata_preserve': 'Zachovat metadata (název, autor, atd.)',
        'pdfa_target_folder': 'Cílová složka:',
        'pdfa_browse': 'Procházet...',
        'pdfa_select_folder': 'Vyberte cílovou složku',
        'pdfa_ocr_info_unknown': '🔍 Nelze zkontrolovat obsah textu.',
        'pdfa_ocr_info_not_needed': '✅ Text dostupný - OCR není vyžadováno.\nPDF/A lze vytvořit přímo.',
        'pdfa_ocr_info_recommended': '⚠️ Nebyl nalezen dostatečný text.\n\nPro vyhledávatelná PDF doporučujeme nejprve spustit OCR.\nPoznámka: PDF/A funguje i bez OCR - ale text pak nebude vyhledávatelný.',
        'pdfa_ocr_info_error': '❌ Chyba při kontrole: {0}',
        'pdfa_start': 'Spouštění PDF/A konverze...',
        'pdfa_progress': 'PDF/A konverze probíhá...',
        'pdfa_success': 'PDF/A konverze úspěšná!\n\nUloženo jako:\n{0}\n\nChcete otevřít nové PDF?',
        'pdfa_complete': 'PDF/A konverze dokončena',
        'pdfa_cancel': 'PDF/A konverze zrušena',
        'pdfa_error_format': 'Chyba při PDF/A konverzi:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Knihovna "ocrmypdf" není nainstalována.\n\nProsím nainstalujte ji pomocí:\npip install ocrmypdf',
        'btn_convert': 'Konvertovat',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimalizovat PDF (zmenšit velikost souboru)',
        'optimize_menu': 'Optimalizovat PDF (velikost souboru)',
        'optimize_info': 'Zmenšuje velikost PDF souboru pomocí různých optimalizačních metod.\n\nČím vyšší úroveň komprese, tím menší soubor - s možnou ztrátou kvality obrázků.',
        'optimize_level': 'Úroveň komprese:',
        'optimize_level_low': 'Nízká (rychlé, malá úspora)',
        'optimize_level_medium': 'Střední (dobrý kompromis)',
        'optimize_level_high': 'Vysoká (velká úspora)',
        'optimize_level_maximum': 'Maximální (maximální úspora, pomalé)',
        'optimize_level_explanation': 'Doporučení: "Střední" je dobrý kompromis mezi rychlostí a velikostí souboru.',
        'optimize_options': 'Možnosti:',
        'optimize_compress_images': 'Komprimovat obrázky (snížit kvalitu JPEG)',
        'optimize_clean_objects': 'Odstranit nepoužívané objekty',
        'optimize_preserve_metadata': 'Zachovat metadata (název, autor, atd.)',
        'optimize_image_quality': 'Kvalita obrázku:',
        'optimize_range': 'Rozsah stránek:',
        'optimize_all_pages': 'Všechny stránky',
        'optimize_custom_range': 'Vlastní rozsah',
        'optimize_from': 'Od:',
        'optimize_to': 'Do:',
        'optimize_target_folder': 'Cílová složka:',
        'optimize_browse': 'Procházet...',
        'optimize_select_folder': 'Vyberte cílovou složku',
        'optimize_info_box': 'Informace',
        'optimize_info_text': 'Optimalizace může u velkých PDF trvat několik minut.\n\nObrázky se ukládají se sníženou kvalitou, což může výrazně zmenšit velikost souboru.',
        'optimize_start': 'Spouštění PDF optimalizace...',
        'optimize_progress': 'Optimalizace PDF...',
        'optimize_cancel': 'PDF optimalizace zrušena',
        'optimize_complete': 'PDF optimalizace dokončena',
        'optimize_error_format': 'Chyba při PDF optimalizaci:\n\n{0}',
        'optimize_success_message': 'PDF optimalizace úspěšná!\n\nUloženo jako:\n{0}\n\nPřed: {1}\nPo: {2}\nÚspora: {3:.1f}%\n\n{4}\n\nChcete otevřít optimalizované PDF?',
        'optimize_success_message_no_size': 'PDF optimalizace úspěšná!\n\nUloženo jako:\n{0}\n\nInformace o velikosti není k dispozici.\n\nChcete otevřít optimalizované PDF?',
        'optimize_result_positive': 'Soubor byl zmenšen o {0:.1f}%.',
        'optimize_result_zero': 'Žádná změna velikosti souboru.',
        'optimize_result_negative': 'Soubor se zvětšil o {0:.1f}%.\nOptimalizace byla přeskočena, původní soubor byl zachován.',
        'btn_optimize': 'Spustit optimalizaci',
        'filename_optimize_low_suffix': '_optimalizovano_nizko',
        'filename_optimize_medium_suffix': '_optimalizovano',
        'filename_optimize_high_suffix': '_optimalizovano_vysoko',
        'filename_optimize_maximum_suffix': '_optimalizovano_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Oříznout PDF',
        'crop_menu': 'Oříznout PDF (Crop)',
        'crop_range': 'Použít na:',
        'crop_all_pages': 'Všechny stránky',
        'crop_current_page': 'Pouze aktuální stránku',
        'crop_values': 'Hodnoty oříznutí (v bodech):',
        'crop_left': 'Vlevo:',
        'crop_right': 'Vpravo:',
        'crop_top': 'Nahoře:',
        'crop_bottom': 'Dole:',
        'crop_presets': 'Předvolby:',
        'crop_preset_white': 'Detekovat bílé okraje',
        'crop_reset': 'Resetovat',
        'crop_mouse_hint': '🖱️ Přetáhněte obdélník pro hrubý výběr oblasti.\nPoté můžete přesně upravit hodnoty v SpinBoxech.\nRuční úprava myší není možná.',
        'crop_apply': 'Oříznout',
        'crop_scope_all': 'Všechny stránky',
        'crop_scope_current': 'Aktuální stránka',
        'crop_new_size': 'Nová velikost: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Není načteno žádné PDF',
        'crop_preview_error': 'Chyba při načítání náhledu',
        'crop_start': 'Spouštění oříznutí...',
        'crop_progress': 'Ořezávání PDF...',
        'crop_success': 'PDF úspěšně oříznuto!\n\nUloženo jako:\n{0}\n\nChcete otevřít oříznuté PDF?',
        'crop_complete': 'Oříznutí dokončeno',
        'crop_cancel': 'Oříznutí zrušeno',
        'crop_error_format': 'Chyba při ořezávání:\n\n{0}',
        'filename_crop_suffix': '_orezano',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Zploštění PDF (Flatten)',
        'flatten_menu': 'Zploštění PDF (Flatten)',
        'flatten_info': 'Zploštění PDF "vypálí" všechny upravitelné prvky do obsahu stránky.\n\nPoté již nelze jednotlivě upravovat pole formulářů, anotace, texty, křížky, podpisy, obrázky a tvary.',
        'flatten_explanation_title': '📖 K čemu je to dobré?',
        'flatten_explanation_text': 'Zploštění je potřeba v následujících situacích:\n\n'
            '• 📄 Chcete připravit dokument pro tisk\n'
            '• 🔒 Chcete zabránit změnám polí formulářů\n'
            '• 📎 Chcete "trvale" vložit anotace a komentáře do dokumentu\n'
            '• 🖼️ Chcete trvale ukotvit vložené texty, křížky, podpisy, obrázky a tvary v dokumentu\n'
            '• 📦 Chcete připravit soubor pro archivaci\n\n'
            'Zploštění zmenší PDF a zabraňuje náhodnému přesouvání nebo mazání prvků.',
        'flatten_what_title': 'Co se zplošťuje?',
        'flatten_what_list': '• ✅ Pole formulářů (textová pole, zaškrtávací políčka, tlačítka)\n'
            '• ✅ Anotace (komentáře, zvýraznění, poznámky)\n'
            '• ✅ Překryvy (texty, křížky, podpisy, obrázky, tvary)',
        'flatten_options': 'Možnosti:',
        'flatten_forms': 'Zploštit pole formulářů',
        'flatten_annotations': 'Zploštit anotace',
        'flatten_overlays': 'Zploštit překryvy (texty, křížky, podpisy, obrázky, tvary)',
        'flatten_target_folder': 'Cílová složka:',
        'flatten_browse': 'Procházet...',
        'flatten_select_folder': 'Vyberte cílovou složku',
        'flatten_warning': '⚠️ Důležité: Zploštění je nevratný proces!\n\nPo zploštění nelze upravitelné prvky jednotlivě měnit ani mazat.\nV případě potřeby si předem vytvořte zálohu.',
        'flatten_apply': 'Zploštit',
        'flatten_start': 'Spouštění zploštění...',
        'flatten_progress': 'Zplošťování PDF...',
        'flatten_success': 'PDF úspěšně zploštěno!\n\nUloženo jako:\n{0}\n\nChcete otevřít zploštěné PDF?',
        'flatten_complete': 'Zploštění dokončeno',
        'flatten_cancel': 'Zploštění zrušeno',
        'flatten_error_format': 'Chyba při zplošťování:\n\n{0}',
        'filename_flatten_suffix': '_zplosteno',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Překrytí PDF (Overlay)',
        'overlay_menu': 'Překrytí PDF (Overlay)',
        'overlay_info': 'Umístí jedno PDF (překryv) přes jiné PDF.\n\nPřekryvné PDF se umístí na základní PDF. To je užitečné pro vodoznaky, loga, hlavičkové papíry nebo razítka.',
        'overlay_explanation_title': '📖 K čemu je to dobré?',
        'overlay_explanation_text': 'Překrytí je potřeba v následujících situacích:\n\n'
            '• 🏢 Umístění loga společnosti jako vodoznaku na každou stránku\n'
            '• 📄 Umístění hlavičkového papíru na prázdné PDF\n'
            '• 🖊️ Umístění razítkového překryvu na dokument\n'
            '• 🔖 Umístění vodoznaku na všechny stránky\n'
            '• 📑 Umístění překryvu formuláře na šablonu',
        'overlay_type': 'Typ překryvu:',
        'overlay_type_fullpage': 'Celá stránka (krycí)',
        'overlay_type_transparent': 'Celá stránka (průhledný - doporučeno)',
        'overlay_type_stamp': 'Razítko (polohovatelné)',
        'overlay_type_info_fullpage': '📄 Překryvné PDF se umístí přesně přes celou stránku.\nBílé pozadí lze odstranit, takže zůstane viditelný pouze obsah.',
        'overlay_type_info_transparent': '🔍 Překryvné PDF se umístí přes celou stránku s průhledným pozadím.\nBílé pozadí se automaticky odstraní - ideální pro vodoznaky a loga!',
        'overlay_type_info_stamp': '🖊️ Překryvné PDF se umístí a přizpůsobí jako razítko.\nPerfektní pro loga, razítka nebo podpisy na určitých pozicích.',
        'overlay_remove_background': 'Odstranit bílé pozadí:',
        'overlay_remove_background_enable': 'Odstranit bílé pozadí z překryvného PDF (udělá překryv průhledným)',
        'overlay_remove_background_tooltip': 'Odstraňuje bílé oblasti z překryvného PDF, aby byl spodní text viditelný.',
        'overlay_threshold': 'Prahová hodnota:',
        'overlay_threshold_hint': '(1-254, vyšší = více bílé se odstraní)',
        'overlay_select_file': 'Vyberte překryvné PDF:',
        'overlay_file_placeholder': 'Prosím vyberte PDF soubor pro překryv',
        'overlay_browse': 'Procházet...',
        'overlay_select_overlay': 'Vyberte překryvné PDF',
        'overlay_range': 'Rozsah stránek:',
        'overlay_all_pages': 'Všechny stránky',
        'overlay_custom_range': 'Vlastní rozsah',
        'overlay_from': 'Od:',
        'overlay_to': 'Do:',
        'overlay_position': 'Pozice:',
        'overlay_position_center': 'Střed',
        'overlay_position_top_left': 'Vlevo nahoře',
        'overlay_position_top_right': 'Vpravo nahoře',
        'overlay_position_bottom_left': 'Vlevo dole',
        'overlay_position_bottom_right': 'Vpravo dole',
        'overlay_size': 'Velikost:',
        'overlay_size_original': 'Původní velikost',
        'overlay_size_fit_page': 'Přizpůsobit stránce',
        'overlay_size_custom': 'Vlastní (%)',
        'overlay_opacity': 'Průhlednost:',
        'overlay_target_folder': 'Cílová složka:',
        'overlay_browse_folder': 'Procházet...',
        'overlay_select_folder': 'Vyberte cílovou složku',
        'overlay_warning': '⚠️ Poznámka: Překryvné PDF se umístí na základní PDF a "vypálí" se do něj.\n\nPrvky překryvného PDF nelze po uložení jednotlivě upravovat.',
        'overlay_apply': 'Překrýt',
        'overlay_start': 'Spouštění překryvu...',
        'overlay_progress': 'Překrývání PDF...',
        'overlay_success': 'PDF úspěšně překryto!\n\nUloženo jako:\n{0}\n\nChcete otevřít překryté PDF?',
        'overlay_complete': 'Překrytí dokončeno',
        'overlay_cancel': 'Překrytí zrušeno',
        'overlay_error_format': 'Chyba při překrývání:\n\n{0}',
        'overlay_no_file': 'Nebylo vybráno žádné překryvné PDF.\n\nProsím vyberte PDF soubor pro překrytí.',
        'filename_overlay_suffix': '_prekryto',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extrahovat obrázky z PDF',
        'extract_images_menu': 'Extrahovat všechny obrázky',
        'extract_images_info': 'Extrahuje všechny obrázky z PDF a uloží je jako samostatné soubory.\n\nObrázky se ukládají v původním formátu nebo se převádějí do vybraného formátu.',
        'extract_images_format': 'Formát obrázku:',
        'extract_images_quality': 'Kvalita JPEG:',
        'extract_images_options': 'Možnosti:',
        'extract_images_subfolder': 'Extrahovat do podsložky ("nazevPDF_obrazky")',
        'extract_images_unique': 'Pouze unikátní obrázky (zabránit duplicitám)',
        'extract_images_range': 'Rozsah stránek:',
        'extract_images_all_pages': 'Všechny stránky',
        'extract_images_custom_range': 'Vlastní rozsah',
        'extract_images_from': 'Od:',
        'extract_images_to': 'Do:',
        'extract_images_target_folder': 'Cílová složka:',
        'extract_images_browse': 'Procházet...',
        'extract_images_select_folder': 'Vyberte cílovou složku',
        'extract_images_info_box': 'Informace',
        'extract_images_info_text': 'Extrakce může u velkých PDF trvat několik minut.\n\nObrázky se ukládají s původním názvem (stranka_obrazek).',
        'extract_images_extract': 'Extrahovat',
        'extract_images_start': 'Spouštění extrakce...',
        'extract_images_progress': 'Extrakce obrázků...',
        'extract_images_success': '✅ Obrázky úspěšně extrahovány!\n\n{0} obrázků bylo uloženo do:\n{1}',
        'extract_images_complete': 'Extrakce obrázků dokončena',
        'extract_images_cancel': 'Extrakce zrušena',
        'extract_images_error_format': 'Chyba při extrakci obrázků:\n\n{0}',
        'extract_images_open_folder': '📁 Otevřít složku',
        'extract_images_no_images': 'V PDF nebyly nalezeny žádné obrázky.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Více stránek na jedné stránce (N-Up)',
        'nup_menu': 'Více stránek na jedné stránce (N-Up)',
        'nup_info': 'Uspořádá více PDF stránek na jedné stránce.\n\nIdeální pro kompaktní tisky, přehledy nebo handouty.',
        'nup_layout': 'Rozložení:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Náhled:',
        'nup_preview_info': '{0} stránek → {1} stránek na list → {2} listů\nRozložení: {3}',
        'nup_order': 'Pořadí:',
        'nup_order_horizontal': 'Horizontální (řádek po řádku)',
        'nup_order_vertical': 'Vertikální (sloupec po sloupci)',
        'nup_order_horizontal_reverse': 'Horizontální obráceně',
        'nup_order_vertical_reverse': 'Vertikální obráceně',
        'nup_range': 'Rozsah stránek:',
        'nup_all_pages': 'Všechny stránky',
        'nup_custom_range': 'Vlastní rozsah',
        'nup_from': 'Od:',
        'nup_to': 'Do:',
        'nup_options': 'Možnosti:',
        'nup_margins': 'Okraje:',
        'nup_margin_between': 'Mezera mezi stránkami:',
        'nup_page_numbers': 'Vložit čísla stránek',
        'nup_target_folder': 'Cílová složka:',
        'nup_browse': 'Procházet...',
        'nup_select_folder': 'Vyberte cílovou složku',
        'nup_create': 'Vytvořit',
        'nup_start': 'Spouštění N-Up...',
        'nup_progress': 'Vytváření N-Up...',
        'nup_success': 'N-Up úspěšně vytvořeno!\n\nUloženo jako:\n{0}\n\nChcete otevřít nové PDF?',
        'nup_complete': 'N-Up dokončeno',
        'nup_cancel': 'N-Up zrušeno',
        'nup_error_format': 'Chyba při N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Změnit velikost stránky',
        'pagesize_menu': 'Změnit velikost stránky',
        'pagesize_info': 'Mění velikost stránky PDF.\n\nObsah se automaticky přizpůsobí nové velikosti.',
        'pagesize_format': 'Formát:',
        'pagesize_select': 'Vyberte standardní formát:',
        'pagesize_custom': 'Vlastní velikost:',
        'pagesize_width': 'Šířka:',
        'pagesize_height': 'Výška:',
        'pagesize_orientation': 'Orientace:',
        'pagesize_portrait': 'Na výšku',
        'pagesize_landscape': 'Na šířku',
        'pagesize_scale_options': 'Možnosti škálování:',
        'pagesize_fit': 'Přizpůsobit (zachovat poměr stran)',
        'pagesize_stretch': 'Natáhnout (deformovat)',
        'pagesize_center': 'Vycentrovat (původní velikost)',
        'pagesize_range': 'Rozsah stránek:',
        'pagesize_all_pages': 'Všechny stránky',
        'pagesize_custom_range': 'Vlastní rozsah',
        'pagesize_from': 'Od:',
        'pagesize_to': 'Do:',
        'pagesize_target_folder': 'Cílová složka:',
        'pagesize_browse': 'Procházet...',
        'pagesize_select_folder': 'Vyberte cílovou složku',
        'pagesize_apply': 'Použít',
        'pagesize_start': 'Spouštění změny velikosti stránky...',
        'pagesize_progress': 'Změna velikosti stránky...',
        'pagesize_success': 'Velikost stránky úspěšně změněna!\n\nUloženo jako:\n{0}\n\nChcete otevřít nové PDF?',
        'pagesize_complete': 'Změna velikosti stránky dokončena',
        'pagesize_cancel': 'Změna velikosti stránky zrušena',
        'pagesize_error_format': 'Chyba při změně velikosti stránky:\n\n{0}',
        'pagesize_preview_info': 'Nová velikost: {0} x {1} pt',
        'filename_pagesize_suffix': '_nova_velikost',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informace o PDF',
        'pdf_info_menu': 'Zobrazit informace o PDF',
        'pdf_info_voice': 'Zobrazují se informace o PDF',
        'pdf_info_error': 'Chyba při zobrazování informací o PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Zobrazit klávesové zkratky",
        "shortcuts_dialog_title": "Klávesové zkratky",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 SOUBOR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Otevřít PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Zavřít PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Uložit jako...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Ochrana dokumentu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Tisk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Tisknout ihned (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Ukončit aplikaci</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exportovat jako Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exportovat jako DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exportovat jako TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exportovat jako obrázky (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extrahovat obrázky</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ZPRACOVÁNÍ DOKUMENTŮ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Více stránek)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konverze (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Zploštit PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Překrytí PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimalizovat PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ ÚPRAVY</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Hledat</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Přidat záložku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Správa záložek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Další záložka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Předchozí záložka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Spustit OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SPRÁVA STRÁNEK</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Otočit aktuální stránku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Otočit všechny stránky</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizovat aktuální stránku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizovat všechny stránky</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Smazat stránky</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extrahovat stránky</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Vložit stránky</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Přesunout stránky</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Sloučit PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Změnit velikost stránky</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 VLOŽENÍ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Vložit text</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Vložit křížek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Vložit podpis 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Vložit podpis 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Vložit obrázek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Vložit obdélník</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Vložit elipsu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Vložit čáru</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Vložit šipku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Vložit čísla stránek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Textový vodoznak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Obrázkový vodoznak</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDAKCE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redakce (černá)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redakce (bílá)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Použít všechny redakce</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ POKROČILÉ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Oříznout PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Upravit metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ ZOBRAZENÍ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Přepnout Tmavý/Světlý režim</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Zobrazit textové okno</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Šířka stránky (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dvě stránky (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Přehled (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ NASTAVENÍ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Správa hesel</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Nastavení OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Nastavení podpisu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formátování názvů souborů</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Exportovat nastavení</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importovat nastavení</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMACE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Zobrazit informace o PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Zapnout/vypnout hlasový výstup</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Zaostřit na lištu nabídek</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nová verze je k dispozici",
        "update_available_message": "Je k dispozici nová verze <b>{0}</b>.\n\nNavštivte stránku vydání a stáhněte si aktualizaci:\n{1}",
        "update_available_voice": "Nová verze {0} je k dispozici. Stáhněte si aktualizaci ze stránky GitHub.",
        "update_open_release": "Otevřít stránku vydání",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Stáhnout všechny překlady",
        "ask_download_all_translations": """Kromě němčiny, angličtiny a vietnamštiny je k dispozici dalších {total_languages} GUI jazyků.\n\nMají být poskytnuty / aktualizovány?\n\nPoznámka:\nNepotřebné jazyky můžete později ručně smazat v adresáři:\n{translations_path}
        \nPokud zrušíte, můžete GUI jazyky stáhnout později pomocí nabídky 'Nástroje → Aktualizovat překlady'.""",
        "menu_update_translations": "Aktualizovat překlady",
        "translations_updated": "Překlady aktualizovány",
        "translations_update_success": "{} překladů bylo úspěšně aktualizováno ({} nových, {} aktualizovaných).",
        "translations_update_error": "Chyba při aktualizaci překladů",
        "translations_update_no_changes": "Všechny překlady jsou již aktuální.",
        "translations_update_offline": "Žádné internetové připojení. Překlady nemohly být aktualizovány.",
        "translations_update_in_progress": "Překlady se aktualizují na pozadí...",
        "translations_downloading": "Stahování překladů...",
        "translations_path_hint": "Uživatelský adresář pro překlady",
        "translations_update_not_available_title": "Aktualizace není k dispozici",
        "translations_update_not_available_message": """Aktualizace překladů je k dispozici pouze v nainstalované verzi.\n\nVe vývojovém režimu jsou překlady již aktuální.""",
        "translations_update_no_internet_title": "Žádné internetové připojení",
        "translations_update_no_internet_message": """Nelze navázat internetové připojení.\n\nPřeklady nelze stáhnout z GitHubu.\n\nMožná řešení:
        • Zkontrolujte své internetové připojení
        • Dočasně vypněte případný firewall
        • Zkuste to později znovu
        \nPřeklady si také můžete stáhnout ručně z GitHubu:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Aktualizace již probíhá",
        "btn_retry": "Zkusit znovu",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Vítejte v PDF Dark View",
        "welcome_title_not_supported": "Vítejte v PDF Dark View",
        "welcome_message": "Vítejte v PDF Dark View!\n\nVáš systémový jazyk byl rozpoznán jako '{language}'.\nChcete tento jazyk použít pro uživatelské rozhraní?\n\nJazyk můžete kdykoli změnit v 'Nastavení → Jazyk'.",
        "welcome_message_language_not_available": "Vítejte v PDF Dark View!\n\nVáš systémový jazyk byl rozpoznán jako '{language}'.\nTento jazyk zatím není nainstalován.\n\nChcete nyní stáhnout překlady pro {language} z GitHubu?\n\n(Jazyk pak bude automaticky použit pro uživatelské rozhraní.)",
        "welcome_message_language_not_supported": "Vítejte v PDF Dark View!\n\nVáš systémový jazyk byl rozpoznán jako '{language}'.\nBohužel pro tento jazyk zatím nejsou žádné překlady.\n\nUživatelské rozhraní bude zobrazeno v {fallback_language}.\n\nJazyk můžete kdykoli změnit v 'Nastavení → Jazyk'.\nPokud chcete, můžete sami přispět překladem pro svůj jazyk:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Ano, použít systémový jazyk",
        "welcome_keep_english": "Ne, ponechat angličtinu",
        "welcome_download_language": "Ano, stáhnout {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program se ukončuje",

    }
