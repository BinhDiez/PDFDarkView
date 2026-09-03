
# ============================================
# translations_sk.py - Slovenský slovník
# Vollständig sortiert nach Kategorien
# ============================================

def load_slovak_strings():
    """Lädt alle slowakischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Otvoriť PDF",
        'btn_text_window': "Text OCR",
        'btn_first': "Prvá strana",
        'btn_prev': "Predchádzajúca strana",
        'btn_next': "Ďalšia strana",
        'btn_last': "Posledná strana",
        'btn_print': "Tlačiť",
        'btn_darkmode_light': "Svetlý režim",
        'btn_darkmode_dark': "Tmavý režim",
        'btn_delete_pages': "Odstrániť strany",
        'btn_extract_pages': "Extrahovať strany",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Zrušiť",
        'btn_save': "Uložiť",
        'btn_close': "Zatvoriť",
        'btn_delete': "Odstrániť",
        'btn_delete_all': "Odstrániť všetko",
        'btn_copy': "Kopírovať",
        'btn_export': "Exportovať",
        'btn_show': "Zobraziť heslo",
        'btn_hide': "Skryť heslo",
        'btn_authenticate': "Overiť",
        'btn_settings': "Nastavenia",
        'btn_protect': "Chrániť",
        'btn_remove_password': "Odstrániť heslo",
        'btn_manage': "Správa hesiel",
        'btn_retry': "Skúsiť znova",
        'btn_select_all': "Vybrať všetko",
        'btn_clear_selection': "Zrušiť výber",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Strana {0} z {1}",
        'page_count': "z {0}",
        'goto_page': "Prejsť na stranu",
        'page_simple': "Strana {0}",
        'full_view_page': "Celý náhľad strany {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Zadajte hľadaný výraz + Enter",
        'search_results': "Výsledky: {0} z {1}",
        'search_nav_hint': "Enter: ďalší (Shift+Enter: predchádzajúci) výsledok",
        'search_no_results': "Žiadne výsledky",
        'search_error': "Chyba vyhľadávania",
        'search_active': "Vyhľadávacie pole aktivované",
        'search_closed': "Vyhľadávanie ukončené",
        'search_position': "Strana {0} {1}",
        'search_pos_top': "úplne hore",
        'search_pos_upper': "hore",
        'search_pos_middle': "v strede",
        'search_pos_lower': "dole",
        'search_pos_bottom': "úplne dole",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Rozpoznávanie textu úspešne dokončené!",
        'ocr_success_title': "OCR úspešné",
        'ocr_success_message': "Dokument je teraz prehľadávateľný.",
        'ocr_failed': "OCR zlyhalo",
        'ocr_in_progress': "Prebieha OCR",
        'ocr_preparing': "Pripravujem PDF...",
        'ocr_analyzing': "Analyzujem PDF...",
        'ocr_optimizing': "Optimalizácia obrázkov...",
        'ocr_recognizing': "Rozpoznávanie textu...",
        'ocr_embedding': "Vkladanie textu...",
        'ocr_finalizing': "Finalizácia PDF...",
        'ocr_not_available': "OCR nie je k dispozícii",
        'ocr_install_message': "Nástroje OCR neboli nájdené.\n\nNainštalujte prosím:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Vyžaduje sa OCR",
        'ocr_question': "PDF neobsahuje prehľadávateľný text.\nChcete vykonať OCR na umožnenie {0}?",
        'ocr_perform': "Vykonať OCR",
        'ocr_later': "Neskôr",
        'ocr_starting': "Spúšťam garantované OCR...",
        'ocr_success_voice': "OCR úspešné. PDF je teraz prehľadávateľné.",
        'ocr_partial_success': "OCR bolo vykonané, ale pri nahrádzaní sa vyskytli problémy.\n\nPrehľadávateľná verzia bola uložená do:\n{0}\n\nChyba: {1}",
        'ocr_partial_title': "OCR čiastočne úspešné",
        'ocr_partial_voice': "OCR vykonané, ale nahradenie zlyhalo.",
        'original_file': "Pôvodný súbor:",
        'old_size': "Stará veľkosť:    {0} bajtov",
        'new_size': "Nová veľkosť: {0} bajtov",
        'size_change': "Zmena: {0}{1} bajtov",
        'backup_created_file': "Záloha vytvorená:\n{0}",
        'backup_not_created': "Záloha nevytvorená (nastavenie vypnuté)",
        'page_header': "=== Strana {0} ===\n{1}\n",
        'scanned_page_header': "=== Strana {0} (skenovaná) ===\n[Táto strana obsahuje iba skenovaný text]\n[Vykonajte OCR ručne]\n",
        'scanned_warning': "⚠️ SKENOVANÝ TEXT - VYŽADUJE OCR",
        'guaranteed_title': "Vytvorené prehľadávateľné PDF",
        'guaranteed_message': "<b>Vytvorená garantovaná prehľadávateľná verzia!</b>\n\nPretože automatické OCR zlyhalo, bola vytvorená alternatívna prehľadávateľná PDF:\n\n{0}\n\n<b>Tento súbor obsahuje:</b>\n• Extrahovaný text (ak existoval)\n• Pokyny pre skenované strany\n• Je plne prehľadávateľný",
        'guaranteed_voice': "Vytvorené garantované prehľadávateľné PDF.",
        'instruction_title': "NÁVOD NA OCR",
        'instruction_file': "Pôvodný súbor: {0}",
        'instruction_text': "Automatické rozpoznávanie textu (OCR) zlyhalo.\nVykonajte OCR ručne:\n\n1. S OCRmyPDF (príkazový riadok):\n   ocrmypdf --force-ocr \"[SÚBOR]\" \"vystup.pdf\"\n\n2. S ADOBE ACROBAT (macOS/Windows):\n   • Otvorte PDF v Acrobate\n   • Nástroje > Upraviť PDF\n   • Vyberte 'Rozpoznanie textu'\n\n3. S PREVIEW (macOS):\n   • Otvorte PDF v náhľade\n   • Súbor > Exportovať...\n   • Filter Quartz: 'Zmenšiť veľkosť súboru'\n   • Povoliť 'Vykonať OCR'\n\n4. ONLINE OCR SLUŽBY:\n   • smallpdf.com/sk/ocr-pdf\n   • ilovepdf.com/sk/ocr-pdf\n   • adobe.com/sk/acrobat/online/pdf-to-word.html",
        'instruction_created': "Vytvorený návod na OCR",
        'instruction_created_message': "Podrobný návod bol vytvorený:\n\n{0}\n\nPostupujte podľa krokov pre ručné OCR.",
        'instruction_created_voice': "Vytvorený návod na OCR.",
        'ocr_impossible': "OCR nie je možné",
        'ocr_impossible_message': "Nie je možné vykonať OCR.\n\nSpracujte '{0}' ručne pomocou OCR softvéru.",
        'ocr_impossible_voice': "OCR nie je možné. Spracujte ručne.",
        'emergency_title': "Núdzové OCR",
        'emergency_message': "Bol vytvorený núdzový súbor PDF:\n\n{0}\n\nSpracujte tento súbor ručne pomocou OCR.",
        'emergency_voice': "Vytvorené núdzové PDF. Vykonajte OCR ručne.",
        'critical_error': "Kritická chyba",
        'critical_error_message': "Nie je možné spustiť OCR.\n\nReštartujte program a skontrolujte inštaláciu OCR.",
        'critical_error_voice': "Kritická chyba OCR",
        'ocr_question_html': "<p>PDF neobsahuje prehľadávateľný text.<p>Chcete vykonať OCR na umožnenie <b>{0}</b>?</p>",
        'ocr_question_voice': "Vyžaduje sa OCR. PDF neobsahuje prehľadávateľný text. Chcete vykonať OCR na umožnenie {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "nenahrané žiadne PDF",
        'no_pdf_message': "Nie je nahrané žiadne PDF",
        'pdf_not_found': "Súbor PDF nenájdený",
        'file_size': "Veľkosť súboru",
        'bytes': "bajtov",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Záloha vytvorená",
        'backup_disabled': "Zálohovanie vypnuté",
        'backup_activated': "Vytváranie záloh zapnuté",
        'backup_deactivated': "Vytváranie záloh vypnuté",
        'backup_status': "Záloha: {0}",
        'backup_on': "✔ zapnuté",
        'backup_off': "✘ vypnuté",
        'close_pdf': "Zatváram PDF: {0}",
        'pdf_not_found_format': "Súbor PDF nenájdený: {0}",
        'error_pdf_load_format': "Chyba pri načítaní PDF: {0}",
        'load_failed_format': "Načítanie zlyhalo:\n{0}",
        'decrypted_suffix': "(dešifrované)",
        'decryption_failed': "Dešifrovanie zlyhalo.",
        'decryption_error': "Chyba pri dešifrovaní",
        'decryption_success': "Úspešne dešifrované",
        'decryption_success_message': "PDF bolo dešifrované a uložené do:\n\n{0}",
        'decryption_success_voice': "PDF bolo dešifrované a uložené.",
        'password_remove_error': "Chyba pri odstraňovaní hesla",
        'save_unencrypted': "Uložiť nešifrované PDF ako",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Uložiť ako...",
        'save_copy': "Uložiť kópiu",
        'save_success': "PDF uložené do: {0}",
        'save_encrypted': "Chránené PDF uložené do: {0}",
        'save_error': "PDF sa nepodarilo uložiť",
        'encryption_question': "Chcete chrániť PDF heslom?",
        'encryption_yes': "Áno",
        'encryption_no': "Nie",
        'encryption_cancel': "Zrušiť",
        'save_cancel': "Ukladanie zrušené",
        'save_encrypted_voice': "Súbor zašifrovaný a uložený.",
        'save_success_voice': "Súbor PDF bol uložený nešifrovaný.",
        'save_error_format': "PDF sa nepodarilo uložiť:\n{0}",
        'export_pages_success': "Export do Pages úspešný",
        'export_pages_error': "Export do Pages zlyhal",
        'export_pages_error_format': "Export do Pages zlyhal: {0}",
        'export_word_success': "Export do Wordu úspešný",
        'export_word_error': "Export do Wordu zlyhal",
        'export_word_error_format': "Export do Wordu zlyhal: {0}",
        'export_text_success': "Export do textu úspešný",
        'export_text_error': "Export do textu zlyhal",
        'export_text_error_format': "Export do textu zlyhal: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Vyžaduje sa heslo",
        'password_enter': "Zadajte heslo",
        'password_confirm': "Potvrďte heslo",
        'password_new': "Nové heslo",
        'password_current': "Aktuálne heslo",
        'password_save': "Uložiť heslo (šifrované)",
        'password_saved': "✓ Heslo pre tento súbor je uložené",
        'password_wrong': "Nesprávne heslo",
        'password_mismatch': "Heslá sa nezhodujú",
        'password_too_short': "Heslo je príliš krátke",
        'password_min_length': "Heslo musí mať aspoň 4 znaky",
        'password_strength': "Sila hesla",
        'password_strength_very_weak': "Veľmi slabé",
        'password_strength_weak': "Slabé",
        'password_strength_medium': "Stredné",
        'password_strength_strong': "Silné",
        'password_strength_very_strong': "Veľmi silné",
        'password_char_count': "({0} znakov)",
        'password_match': "✓ Zhoda",
        'password_no_match': "✗ Heslá sa nezhodujú",
        'password_show': "Zobraziť",
        'password_hide': "Skryť",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Správa hesiel",
        'password_table_filename': "Názov súboru",
        'password_table_password': "Heslo",
        'password_count': "{0} uložených hesiel",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Žiadne uložené heslá",
        'password_copied': "Skopírovaných {0} hesiel",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Naozaj chcete odstrániť heslo pre '{0}'?",
        'password_delete_multiple': "Naozaj chcete odstrániť {0} vybraných hesiel?",
        'password_delete_all_confirm': "Naozaj chcete odstrániť všetkých {0} uložených hesiel?",
        'password_deleted': "Odstránených {0} hesiel",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Všetky heslá boli odstránené",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generátor hesiel",
        'generator_generated': "Vygenerované heslo:",
        'generator_regenerate': "Vygenerovať znova",
        'generator_copy': "Kopírovať",
        'generator_use': "Použiť",
        'generator_settings': "Nastavenia",
        'generator_length': "Dĺžka:",
        'generator_group_every': "Oddeľovač každých",
        'generator_group_chars': "znakov.    Oddeľovač:",
        'generator_uppercase': "Veľké písmená (A-Z)",
        'generator_lowercase': "Malé písmená (a-z)",
        'generator_digits': "Číslice (0-9)",
        'generator_symbols': "Špeciálne znaky (!@#$%^&*)",
        'generator_exclude': "Vylúčené:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Vyžaduje sa hlavné heslo",
        'master_password_setup': "Nastaviť hlavné heslo",
        'master_password_change': "Zmeniť hlavné heslo",
        'master_password_enter': "Zadajte svoje hlavné heslo",
        'master_password_choose': "Vyberte silné hlavné heslo (aspoň 8 znakov)",
        'master_password_new': "Zadajte svoje nové hlavné heslo",
        'master_password_confirm': "Potvrďte heslo",
        'master_password_authenticate': "Overiť",
        'master_password_success': "Hlavné heslo bolo úspešne nastavené.",
        'master_password_changed': "Hlavné heslo bolo úspešne zmenené.",
        'master_password_removed': "Hlavné heslo a všetky heslá boli odstránené.",
        'master_password_remove': "Odstrániť hlavné heslo",
        'master_password_remove_confirm': "Ste si ISTÝ, že chcete odstrániť VŠETKY heslá?\n\nTáto akcia je NEVRATNÁ!",
        'master_password_export_before': "Chcete predtým exportovať záložnú kópiu?",
        'master_password_export_delete': "Exportovať a odstrániť",
        'master_password_delete_now': "Odstrániť teraz",
        'master_password_for_signatures': "Na používanie podpisov musíte nastaviť hlavné heslo.\n\nChcete teraz nastaviť hlavné heslo?",
        'master_password_for_private': "Na používanie súkromných textových blokov musíte nastaviť hlavné heslo.\n\nChcete teraz nastaviť hlavné heslo?",
        'master_password_info': """
            <b>🔐 BEZ HLAVNÉHO HESLA:</b><br>
            • Nie je možné zobrazovať, kopírovať a exportovať heslá<br>
            • Mazanie hesiel je vždy možné (aj bez hlavného hesla)<br><br>

            <b>🔐 S HLAVNÝM HESLOM:</b><br>
            • Všetky funkcie dostupné po overení<br>
            • Heslá sú šifrované hlavným heslom<br>
            • Minimálna dĺžka: 8 znakov<br>
            • Bezpečné ukladanie hashov SHA-256<br><br>

            <b>DÔLEŽITÉ:</b><br>
            • Pri strate hlavného hesla: heslá nemožno obnoviť<br>
            • Pri odstránení hlavného hesla: VŠETKY heslá budú vymazané<br>
            • Pred vymazaním je k dispozícii možnosť exportu<br>
            • Hlavné heslo možno kedykoľvek zmeniť
        """,
        'signature_auth_disabled': "Vypnúť otázku na heslo pre podpisy",
        'template_auth_disabled': "Vypnúť otázku na heslo pre súkromné textové bloky",
        'master_password_for_signatures_settings': "Na používanie podpisov musíte nastaviť hlavné heslo.\n\nPrejdite do Nastavenia - Správa hesiel",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Chrániť PDF",
        'protect_info': "Súbor '{0}' bude chránený heslom.",
        'protect_instruction': "Zadajte dvakrát požadované heslo na ochranu dokumentu, alebo použite generátor hesiel napravo od vstupného poľa.",
        'protect_success': "PDF bolo úspešne chránené a uložené do:\n{0}\n\nHeslo: {1}\n\nChcete teraz otvoriť chránené PDF?",
        'protect_open': "Áno",
        'protect_skip': "Nie",
        'protect_error': "Chyba pri ochrane PDF",
        'protect_open_title': "otvoriť chránené PDF",
        'protect_question': "Hotovo. Chcete teraz otvoriť chránené PDF? Áno alebo Nie?",
        'password_cancel': "Dialóg hesla zrušený",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Odstrániť strany",
        'pages_extract': "Extrahovať strany",
        'pages_insert': "Vložiť strany",
        'pages_move': "Presunúť strany",
        'pages_delete_options': "Možnosti odstránenia",
        'pages_delete_empty': "Odstrániť všetky prázdne strany",
        'pages_delete_current': "Odstrániť aktuálnu stranu",
        'pages_delete_range': "Odstrániť rozsah strán",
        'pages_extract_options': "Možnosti extrakcie",
        'pages_extract_current': "Extrahovať aktuálnu stranu",
        'pages_extract_range': "Extrahovať rozsah strán",
        'pages_insert_position': "Miesto vloženia",
        'pages_insert_before': "Vložiť pred stranu:",
        'pages_insert_select': "Vybrať PDF",
        'pages_insert_none': "Nie je vybraté žiadne PDF",
        'pages_move_source': "Strany na presunutie",
        'pages_move_from': "Od strany:",
        'pages_move_to': "Do strany:",
        'pages_move_target': "Cieľové miesto",
        'pages_move_before': "Presunúť pred stranu:",
        'pages_move_hint': "Poznámka: strana 1 = začiatok, {0} = koniec",
        'pages_range_invalid': "Počiatočná strana musí byť menšia alebo rovná koncovej strane.",
        'pages_position_invalid': "Cieľové miesto nesmie ležať v presúvanom rozsahu.",
        'pages_no_pdf_selected': "Nie je vybraté žiadne PDF.",
        'pages_deleted': "Bolo odstránených {0} strán.",
        'pages_extracted': "Extrahované: {0}\nUložené do: {1}\nVeľkosť súboru: {2:.1f} KB",
        'pages_inserted': "Vložených {0} strán",
        'pages_moved': "Bolo presunutých {0} strán.",
        'pages_deleted_none': "Neboli odstránené žiadne strany.",
        'pages_delete_progress': "Odstraňujem strany...",
        'pages_deleted_with_backup': "Bolo odstránených {0} strán.\n\nZáloha: {1}",
        'pages_deleted_voice': "Bola vytvorená záloha a odstránených {0} strán.",
        'info': "Informácia",
        'error_dialog_creation': "Nie je možné vytvoriť dialóg",
        'extract_page_single': "Extrahovať stranu {0}",
        'extract_page_range': "Extrahovať strany {0}-{1}",
        'extract_success_voice': "Strany úspešne extrahované",
        'extract_error_format': "Chyba pri extrakcii: {0}",
        'pages_inserted_voice': "Bolo vložených {0} strán.",
        'insert_error_format': "Chyba pri vkladaní: {0}",
        'pages_move_progress': "Presúvam strany...",
        'pages_moved_with_backup': "Bolo presunutých {0} strán.\n\nZáloha: {1}",
        'move_success_title': "Úspešne presunuté",
        'pages_moved_voice': "{0} strán úspešne presunutých",
        'mark_removed': "Označenie strany {0} odstránené",
        'mark_empty': "Strana {0} označená ako prázdna",
        'mark_export_removed': "Označenie exportu strany {0} odstránené",
        'mark_export': "Strana {0} označená na export",
        'no_empty_pages': "Nie sú označené žiadne prázdne strany na odstránenie",
        'delete_empty_confirm': "Chcete odstrániť všetkých {0} označených prázdnych strán?",
        'delete_empty_confirm_voice': "Odstrániť teraz všetkých {0} označených prázdnych strán? Áno alebo Nie.",
        'empty_pages_deleted': "Odstránených {0} prázdnych strán",
        'no_export_pages': "Nie sú označené žiadne strany na export",
        'overwrite_title': "Prepísať existujúci súbor",
        'overwrite_question': "Súbor\n\n{0}\n\nuž existuje.\nChcete ho prepísať?",
        'overwrite_voice': "Prepísať existujúci súbor? Áno alebo Nie.",
        'page_skipped': "Strana {0} bola preskočená",
        'export_complete': "Export dokončený.",
        'export_complete_voice': "Export je dokončený.",
        'no_pages_exported': "Nebola exportovaná žiadna strana",
        'export_cancelled': "Export zrušený",
        'pages_exported': "{0} strán exportovaných do {1}",
        'export_page_title': "Exportovať stranu",
        'page_exported': "Strana {0} exportovaná do {1}",
        'export_error': "Chyba pri exporte",
        'export_marked_title': "Exportovať označené strany",
        'rotate_all_title': "otočiť všetky strany",
        'rotate_all_question': "Chcete otočiť všetky strany o 90 stupňov doprava?",
        'rotate_all_voice': "Chcete otočiť všetky strany o 90 stupňov doprava? Áno alebo Nie?",
        'all_pages_rotated': "Všetky strany otočené",
        'page_rotated': "Strana {0} otočená",
        'rotate_error': "Stranu nie je možné otočiť",
        'delete_page_confirm': "Chcete odstrániť stranu {0}?",
        'delete_page_confirm_voice': "Naozaj chcete odstrániť stranu {0}? Áno alebo Nie.",
        'page_deleted': "Strana {0} odstránená",
        'delete_error': "Stranu nie je možné odstrániť",
        'pages_deleted_voice': "Odstránených {0} strán",
        'pages_exported_split': "{0} strán bolo úspešne exportovaných.",
        'pages_skipped': "{0} strán bolo preskočených.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extrahovať strany (rozšírené)",
        'pdf_splitter_title': "Rozdeľovač a extraktor PDF",
        'pdf_splitter_load': " Vybrať súbor PDF",
        'pdf_splitter_info': "Vyberte možnosť pre váš PDF dokument",
        'pdf_splitter_basic': "Základné operácie",
        'pdf_splitter_single': "Rozdeliť na jednotlivé strany",
        'pdf_splitter_range': "Extrahovať strany:",
        'pdf_splitter_range_placeholder': "napr. 1-3,5,7-9",
        'pdf_splitter_clean': "Čistiace operácie",
        'pdf_splitter_remove_empty': "Odstrániť všetky prázdne strany",
        'pdf_splitter_remove': "Odstrániť rozsah strán:",
        'pdf_splitter_remove_placeholder': "napr. 2,4-6",
        'pdf_splitter_process': "Spracovať PDF",
        'pdf_splitter_loaded': "PDF nahrané. Vyberte možnosť",
        'pdf_read_error': "PDF sa nepodarilo prečítať",
        'pages': "Strany",
        'pages_created': "Strany boli vytvorené",
        'range_empty': "Zadajte rozsah strán",
        'range_invalid': "Neplatný rozsah strán",
        'range_created': "Bolo vytvorené nové PDF s vybranými stranami:\n{0}",
        'empty_removed': "Odstránených {0} prázdnych strán.\nVýstup: {1}",
        'remove_empty': "Zadajte strany na odstránenie",
        'remove_invalid': "Neplatné strany na odstránenie",
        'remove_done': "Vyčistené PDF vytvorené:\n{0}",
        'open_folder': "Otvoriť priečinok",
        'show_in_finder': "Zobraziť vo Finderi",
        'pdf_splitter_no_pdf': "Najprv nahrajte súbor PDF.",
        'process_error': "Chyba pri spracovaní PDF",
        'pages_created_voice': "Vytvorených {0} strán",
        'range_created_voice': "Vytvorené PDF s vybranými stranami",
        'empty_removed_voice': "Odstránených {0} prázdnych strán",
        'remove_done_voice': "Vyčistené PDF vytvorené",
        'pdf_splitter_split_groups': "Každá súvislá skupina do samostatného súboru",
        'range_created_single': "Vytvorené nové PDF:\n{0}",
        'range_created_multiple': "Vytvorených {0} PDF súborov.",
        'range_created_voice_single': "Vytvorené jedno PDF s vybranými stranami",
        'range_created_voice_multiple': "Vytvorených {0} PDF súborov",
        'empty_removed_none_left': "Žiadne zostávajúce strany",
        'empty_removed_all_empty': "Všetky strany boli rozpoznané ako prázdne a boli by odstránené. Nebol vytvorený žiadny súbor.",
        'preview_single': "Náhľad: {0}",
        'preview_enter_range': "Zadajte rozsah strán.",
        'preview_invalid_range': "Neplatný rozsah strán.",
        'preview_file': "Náhľad: {0}",
        'preview_files': "Náhľad: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Spúšťam tlač",
        'print_sent': "Tlačová úloha odoslaná",
        'print_now': "Tlačiť teraz",
        'print_error': "Chyba pri okamžitej tlači",
        'print_limited': "Funkcia tlače je v tomto systéme obmedzená",
        'print_error_format': "Chyba pri okamžitej tlači: {0}",
        'warning': "Upozornenie",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Prepnúť do svetlého režimu",
        'mode_switch_to_dark': "Prepnúť do tmavého režimu",
        'mode_dark_activated': "Tmavý režim aktivovaný",
        'mode_light_activated': "Svetlý režim aktivovaný",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Celý náhľad",
        'zoom_two_pages': "Dve strany vedľa seba",
        'zoom_overview': "Režim prehľadu",
        'zoom_cannot_during_search': "Zoom nie je možné počas vyhľadávania",
        'zoom_exit_first': "Najprv ukončite zoom",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop povolený",
        'drag_disabled': "Drag & Drop zakázaný",
        'drag_page_grab': "Strana {0} uchopená",
        'drag_page_dropped': "Strana {0} vložená na pozíciu {1}",
        'drag_position_invalid': "Neplatná pozícia",
        'drag_same_position': "Strana {0} zostáva na pozícii {0}",
        'drag_error': "Chyba pri presúvaní",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Vstup textu s rozšíreným formátovaním a správou textových blokov",
        'text_templates': "Dostupné textové bloky:",
        'text_name': "Názov",
        'text_preview': "Náhľad textu",
        'text_enter': "Text:",
        'text_font_size': "Veľkosť písma:",
        'text_formatting': "Formátovanie:",
        'text_bold': "Tučné",
        'text_italic': "Kurzíva",
        'text_underline': "Podčiarknuté",
        'text_alignment': "Zarovnanie:",
        'text_left': "Vľavo",
        'text_center': "Na stred",
        'text_right': "Vpravo",
        'text_color': "Farba textu:",
        'text_opacity': "Krytie:",
        'text_word_wrap': "Zalamovanie riadkov:",
        'text_auto': "Automatické",
        'text_page_width_95': "Šírka strany (95%)",
        'text_page_width_85': "Veľmi široké (85%)",
        'text_page_width_75': "Širšie (75%)",
        'text_page_width_60': "Široké (60%)",
        'text_page_width_50': "Stredné (50%)",
        'text_page_width_30': "Úzke (30%)",
        'text_page_width_20': "Užšie (20%)",
        'text_page_width_10': "Veľmi úzke (10%)",
        'text_no_wrap': "Bez zalamovania",
        'text_private': "Súkromný textový blok (vyžaduje overenie)",
        'text_preview_label': "Náhľad:",
        'text_preview_placeholder': "Tu sa zobrazí náhľad textu...",
        'text_no_text': "(Žiadny text)",
        'text_save_template': "💾 Uložiť ako blok",
        'text_delete_template': "🗑 Odstrániť vybraný textový blok",
        'text_show_private': "Zobraziť súkromné",
        'text_hide_private': "Skryť súkromné",
        'text_use': "✅ Použiť text",
        'text_saved': "Textový blok uložený ako:\n{0}",
        'text_saved_voice': "Textový blok uložený",
        'text_deleted': "Textový blok odstránený",
        'text_no_text_to_save': "Žiadny text na uloženie.",
        'text_no_templates': "Nenašli sa žiadne textové bloky",
        'text_private_master_required': "Súkromné bloky možno použiť iba vtedy, ak je nastavené hlavné heslo.\n\nChcete teraz nastaviť hlavné heslo?",
        'text_filename': "Názov súboru pre textový blok (bez 'Text_' a '.txt'):",
        'text_filename_hint': "Príklad: 'Telefón HomeOffice' sa uloží ako 'Text_Telefón HomeOffice.txt'",
        'text_save_hint': "Textový blok sa automaticky uloží s formátovaním.",
        'text_guide_title': "Vstup textu - Návod",
        'text_delete_confirm': "Naozaj chcete odstrániť textový blok?\n\nSúbor: {0}\nText: {1}...",
        'text_make_public': "Označiť ako verejné",
        'text_make_private': "Označiť ako súkromné",
        'text_privacy_changed': "Zmenený stav súkromia",
        'text_private_always': "Súkromné vždy viditeľné (nastavenie)",
        'text_mode_required': "Najprv aktivujte režim textu",
        'text_continue_editing': "Pokračovať v úpravách - kurzor na konci textu",
        'text_no_input': "Nebol zadaný žiadny text - text zahodený",
        'save_dialog_question': "Ako chcete pokračovať?",
        'text_save_question': "Uložiť všetky texty a krížiky, upraviť, pokračovať v úpravách alebo zahodiť?",
        'copy_cross': "Krížik skopírovaný",
        'paste_cross': "Krížik vložený",
        'paste_text': "Text vložený",
        'cross_discarded': "Krížik zahodený",
        'all_discarded': "Všetko zahodené",
        'text_discarded': "Text zahodený",
        'no_texts_to_save': "Žiadne texty na uloženie",
        'no_valid_texts': "Žiadne platné texty na uloženie",
        'text_word_singular': "text",
        'text_word_plural': "texty",
        'cross_word_singular': "krížik",
        'cross_word_plural': "krížiky",
        'texts_saved_title': "Texty uložené",
        'texts_crosses_saved': "{0} {1} a {2} {3} bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'texts_crosses_saved_voice': "Uložených {0} {1} a {2} {3}.",
        'texts_saved': "{0} {1} bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'texts_saved_voice': "Uložených {0} {1}.",
        'crosses_saved': "{0} {1} bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'crosses_saved_voice': "Uložených {0} {1}.",
        'elements_saved': "{0} prvkov bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'elements_saved_voice': "Uložených {0} prvkov.",
        'text_window_load_error': "Nie je možné načítať okno textu",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Vstup textu a textové bloky – Podrobný návod**

        **1. Vloženie a úprava textu**
        - Kliknite pravým tlačidlom myši na požadované miesto v dokumente a zvoľte "Vložiť text".
        - Otvorí sa dialógové okno, v ktorom môžete zadať text a formátovať ho:
        • Veľkosť písma, tučné, kurzíva, podčiarknutie
        • Farba textu (ľubovoľná)
        • Priehľadnosť (krytie) pomocou posuvníka
        • Zalamovanie riadkov (rôzne šírky, napr. šírka strany, úzke, bez zalamovania)
        - Po potvrdení sa text objaví v mieste kliknutia. Môžete ho presúvať myšou alebo klávesmi so šípkami.
        - Dvojité kliknutie na text otvorí režim úprav; ESC ho ukončí.

        **2. Správa textových blokov (šablón)**
        - V dialógu textu vľavo vidíte zoznam všetkých uložených textových blokov.
        - **Uloženie bloku:** Zadajte text, naformátujte ho a kliknite na "💾 Uložiť ako blok". Zadajte názov súboru (bez prípony).
        - **Načítanie bloku:** Kliknite na požadovaný názov v zozname. Text a formátovanie sa prevezmú a možno ich podľa potreby upraviť.
        - **Odstránenie:** Kliknite pravým tlačidlom na blok, môžete ho odstrániť alebo zmeniť jeho stav súkromia.

        **3. Súkromné textové bloky (hlavné heslo)**
        - Ak ste nastavili hlavné heslo (v Nastavenia → Správa hesiel), môžete bloky označiť ako "súkromné".
        - Zaškrtnite políčko "Súkromný textový blok" v dialógu pred uložením.
        - Súkromné bloky sa v zozname zobrazia iba po jednorazovom overení hlavným heslom v danej relácii (overenie cez ikonu zámku alebo pri prvom prístupe).
        - Takto môžete chrániť dôverné textové bloky pred neoprávneným prístupom.

        **4. Vkladanie krížikov**
        - Z kontextovej ponuky môžete tiež vložiť grafický krížik (napr. pre zaškrtávacie políčka).
        - Veľkosť, hrúbku čiary a farbu krížikov možno globálne upraviť v nastaveniach (menu "Nastavenia" → "Nastavenia krížikov").
        - Kliknite pravým tlačidlom na existujúci krížik pre jeho individuálnu úpravu.

        **5. Hromadné akcie**
        - Ak ste na jednu stranu umiestnili viac textov alebo krížikov, môžete ich všetky naraz uložiť alebo zahodiť z kontextovej ponuky (pravým tlačidlom v režime textu).
        - Pri ukladaní sa všetky prvky vložia do PDF a zostanú ako vektorová grafika.

        **6. Klávesové skratky v režime textu**
        - Šípky: presun prvku
        - Ctrl+šípky: väčšie kroky
        - Enter: otvorenie dialógu na uloženie (uložiť všetko / upraviť / zahodiť)
        - ESC: zahodiť aktuálny prvok
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Vstup textu a textové bloky – Podrobný návod</strong></p>

        <p><strong>1. Vloženie a úprava textu</strong></p>
        <ul>
        <li>Kliknite pravým tlačidlom myši na požadované miesto v dokumente a zvoľte "Vložiť text".</li>
        <li>Otvorí sa dialógové okno, v ktorom môžete zadať text a formátovať ho:<br/>
        • Veľkosť písma, tučné, kurzíva, podčiarknutie<br/>
        • Farba textu (ľubovoľná)<br/>
        • Priehľadnosť (krytie) pomocou posuvníka<br/>
        • Zalamovanie riadkov (rôzne šírky, napr. šírka strany, úzke, bez zalamovania)</li>
        <li>Po potvrdení sa text objaví v mieste kliknutia. Môžete ho presúvať myšou alebo klávesmi so šípkami.</li>
        <li>Dvojité kliknutie na text otvorí režim úprav; ESC ho ukončí.</li>
        </ul>

        <p><strong>2. Správa textových blokov (šablón)</strong></p>
        <ul>
        <li>V dialógu textu vľavo vidíte zoznam všetkých uložených textových blokov.</li>
        <li><strong>Uloženie bloku:</strong> Zadajte text, naformátujte ho a kliknite na "💾 Uložiť ako blok". Zadajte názov súboru (bez prípony).</li>
        <li><strong>Načítanie bloku:</strong> Kliknite na požadovaný názov v zozname. Text a formátovanie sa prevezmú a možno ich podľa potreby upraviť.</li>
        <li><strong>Odstránenie:</strong> Kliknite pravým tlačidlom na blok, môžete ho odstrániť alebo zmeniť jeho stav súkromia.</li>
        </ul>

        <p><strong>3. Súkromné textové bloky (hlavné heslo)</strong></p>
        <ul>
        <li>Ak ste nastavili hlavné heslo (v Nastavenia → Správa hesiel), môžete bloky označiť ako "súkromné".</li>
        <li>Zaškrtnite políčko "Súkromný textový blok" v dialógu pred uložením.</li>
        <li>Súkromné bloky sa v zozname zobrazia iba po jednorazovom overení hlavným heslom v danej relácii (overenie cez ikonu zámku alebo pri prvom prístupe).</li>
        <li>Takto môžete chrániť dôverné textové bloky pred neoprávneným prístupom.</li>
        </ul>

        <p><strong>4. Vkladanie krížikov</strong></p>
        <ul>
        <li>Z kontextovej ponuky môžete tiež vložiť grafický krížik (napr. pre zaškrtávacie políčka).</li>
        <li>Veľkosť, hrúbku čiary a farbu krížikov možno globálne upraviť v nastaveniach (menu "Nastavenia" → "Nastavenia krížikov").</li>
        <li>Kliknite pravým tlačidlom na existujúci krížik pre jeho individuálnu úpravu.</li>
        </ul>

        <p><strong>5. Hromadné akcie</strong></p>
        <ul>
        <li>Ak ste na jednu stranu umiestnili viac textov alebo krížikov, môžete ich všetky naraz uložiť alebo zahodiť z kontextovej ponuky (pravým tlačidlom v režime textu).</li>
        <li>Pri ukladaní sa všetky prvky vložia do PDF a zostanú ako vektorová grafika.</li>
        </ul>

        <p><strong>6. Klávesové skratky v režime textu</strong></p>
        <ul>
        <li>Šípky: presun prvku</li>
        <li>Ctrl+šípky: väčšie kroky</li>
        <li>Enter: otvorenie dialógu na uloženie (uložiť všetko / upraviť / zahodiť)</li>
        <li>ESC: zahodiť aktuálny prvok</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Nastavenia krížikov",
        'cross_properties': "Vlastnosti krížika",
        'cross_size': "Veľkosť (px):",
        'cross_line_width': "Hrúbka čiary:",
        'cross_color': "Farba:",
        'cross_choose_color': "Vybrať",
        'cross_fine_tuning': "Doladenie pri ukladaní (pixely)",
        'cross_offset_x': "Posun X:",
        'cross_offset_y': "Posun Y:",
        'cross_offset_x_tooltip': "Záporné hodnoty posúvajú krížik pri ukladaní doľava, kladné doprava",
        'cross_offset_y_tooltip': "Záporné hodnoty posúvajú krížik pri ukladaní hore, kladné dole",
        'cross_preview': "Náhľad",
        'cross_save': "Použiť nastavenia",
        'cross_customized': "Krížik upravený",
        'cross_settings_applied': "Nastavenia krížikov uložené.\nVeľkosť: {0}px, hrúbka čiary: {1}px\n{2}",
        'cross_updated_count': "Aktualizovaných {0} existujúcich krížikov.",
        'cross_no_crosses': "Nenašli sa žiadne existujúce krížiky.",
        'cross_settings_applied_all': "Nastavenia krížikov aplikované na všetkých {0} krížikov",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Nastavenia podpisov",
        'signature_1': "Podpis 1",
        'signature_2': "Podpis 2",
        'signature_select': "Vybrať podpis",
        'signature_add': "➕ Pridať nový podpis...",
        'signature_size': "Veľkosť podpisu {0} (%):",
        'signature_common': "Všeobecné nastavenia",
        'signature_timestamp': "Automaticky pridať časovú pečiatku",
        'signature_location': "Predvolené miesto:",
        'signature_timestamp_size': "Veľkosť písma časovej pečiatky:",
        'signature_no_files': "-- Nenašli sa žiadne podpisy --",
        'signature_insert': "Vložiť podpis",
        'signature_insert_1': "Vložiť podpis 1",
        'signature_insert_2': "Vložiť podpis 2",
        'signature_customize': " Prispôsobiť podpis",
        'signature_discard': " Zahodiť tento podpis",
        'signature_save_all': " Uložiť všetky podpisy",
        'signature_discard_all': " Zahodiť všetky podpisy",
        'signature_guide_title': "Podpisy - Návod",
        'signature_guide': """
📝 Podpisy - Stručný návod

- Nastavte hlavné heslo
- Nakonfigurujte podpisy v menu Nastavenia
  (veľkosť, časová pečiatka ...)
- Vložte PRAVÝM KLIKNUTÍM na požadované miesto
  (hlavné heslo vyžadované raz za reláciu)
- Podpis presuňte myšou alebo šípkami
- Je možné vložiť viac podpisov za sebou
- Každý podpis možno individuálne prispôsobiť
- Zahodiť jednotlivý podpis
- Uložiť / zahodiť všetky podpisy naraz
- Je možné tiež použiť lištu menu.
        """,
        'signature_placeholder': "Náhľad nie je k dispozícii",
        'signature_info': "Podpis {0}: {1}×{2} px ({3}% z {4}×{5})",
        'signature_info_placeholder': "Nastavenia podpisu {0}",
        'signature_inserted': "Podpis {0} vložený na stranu {1}",
        'signature_deleted': "Podpis odstránený",
        'signature_copied': "Podpis skopírovaný",
        'signature_pasted': "Podpis {0} vložený",
        'signature_saved': "{0} podpisov bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'signature_saved_voice': "Uložených {0} podpisov",
        'mode_replace_signature_format': "Ukončiť režim a vložiť podpis {0}",
        'mode_conflict_voice_signature': "Režim {0} je aktívny. Ukončiť a vložiť podpis?",
        'signature_not_configured': "Podpis {0} nie je nakonfigurovaný",
        'signature_file_not_found': "Súbor podpisu nenájdený",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Žiadny skopírovaný podpis",
        'no_signatures_to_save': "Žiadne podpisy na uloženie",
        'signature_save_question': "Uložiť všetky podpisy, upraviť alebo zahodiť tento?",
        'signatures_saved_title': "Podpisy uložené",
        'signatures_saved': "{0} podpisov bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'signatures_saved_voice': "Uložených {0} podpisov.",
        'all_signatures_discarded': "Všetky podpisy zahodené",
        'signature_settings_saved': "Nastavenia podpisov uložené",
        'signature_cancelled': "Podpis zahodený",
        'signature_active_title': "Podpis aktívny",
        'signature_replace_question': "Podpis je už aktívny.\n\nChcete nahradiť aktuálny podpis?",
        'signature_replace': "Nahradiť podpis",
        'signature_replace_voice': "Nahradiť aktuálny podpis alebo zrušiť?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Nastavenia obrázkov",
        'image_common': "Všeobecné nastavenia obrázkov",
        'image_keep_aspect': "Zachovať pomer strán pri ťahaní",
        'image_default_size': "Predvolená veľkosť (%):",
        'image_dark_invert': "Invertovať farby obrázkov v tmavom režime",
        'image_dark_invert_tooltip': "Zapnuté: obrázky sú invertované pre lepšiu viditeľnosť",
        'image_fine_tuning': "Doladenie (pixely)",
        'image_offset_x': "Posun X:",
        'image_offset_y': "Posun Y:",
        'image_offset_x_tooltip': "Záporné hodnoty posúvajú obrázok pri ukladaní doľava, kladné doprava",
        'image_offset_y_tooltip': "Záporné hodnoty posúvajú obrázok pri ukladaní hore, kladné dole",
        'image_select': "Vybrať obrázok",
        'image_insert': "Vložiť obrázok",
        'image_customize': " Prispôsobiť obrázok",
        'image_aspect': " Zachovať pomer strán",
        'image_discard': " Zahodiť tento obrázok",
        'image_save_all': " Uložiť všetky obrázky",
        'image_discard_all': " Zahodiť všetky obrázky",
        'image_filter': "Obrázky",
        'image_guide_title': "Vkladanie obrázkov - Návod",
        'image_guide': """
📷 Vkladanie obrázkov do PDF - Stručný návod:

1. Pravým kliknutím na požadované miesto
2. "Vložiť obrázok" → vyberte obrázok
3. Umiestnite obrázok: ťahaním myšou
4. Upravte veľkosť: ťahaním za rohy/hrany
5. Zachovať pomer strán: kláves [A]
6. Ďalšie úpravy: pravým kliknutím na obrázok

Tip: V kontextovej ponuke môžete upraviť nastavenia.
        """,
        'image_inserted': "Obrázok {0} vložený na stranu {1}",
        'image_deleted': "Obrázok zahodený",
        'image_copied': "Obrázok skopírovaný",
        'image_pasted': "Obrázok vložený",
        'image_saved': "{0} obrázkov bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'image_saved_voice': "Uložených {0} obrázkov",
        'image_aspect_on': "zapnuté",
        'image_aspect_off': "vypnuté",
        'image_aspect_toggle': "Zachovať pomer strán {0}",
        'image_reset': "Obrázok obnovený na pôvodnú veľkosť",
        'image_replaced': "Obrázok nahradený",
        'image_invalid': "Neplatný obrázok",
        'mode_replace_image': "Vložiť obrázok",
        'mode_conflict_voice_image': "Režim {0} je aktívny. Ukončiť a vložiť obrázok?",
        'image_active_title': "Obrázok aktívny",
        'image_replace_question': "Obrázok je už aktívny.\n\nChcete nahradiť aktuálny obrázok?",
        'image_replace': "Nahradiť obrázok",
        'image_replace_voice': "Nahradiť aktuálny obrázok alebo zrušiť?",
        'image_filter_all': "Obrázky (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Všetky súbory (*.*)",
        'no_copied_image': "Žiadny skopírovaný obrázok",
        'image_discarded': "Obrázok zahodený",
        'image_save_question': "Uložiť všetky obrázky, upraviť alebo zahodiť tento?",
        'no_images_to_save': "Žiadne obrázky na uloženie",
        'no_valid_images': "Žiadne platné obrázky na uloženie",
        'images_saved_title': "Obrázky uložené",
        'images_saved': "{0} obrázkov bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'images_saved_voice': "Uložených {0} obrázkov.",
        'all_images_discarded': "Všetky obrázky zahodené",
        'image_settings_updated': "Nastavenia obrázkov aktualizované",
        'image_replace_title': "Vybrať nový obrázok",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Nastavenia tvarov",
        'form_basic': "Základné nastavenia",
        'form_default_type': "Predvolený typ tvaru:",
        'form_rectangle': "Obdĺžnik",
        'form_ellipse': "Elipsa",
        'form_line': "Čiara",
        'form_arrow': "Šípka",
        'form_line_width': "Hrúbka čiary:",
        'form_colors': "Farby",
        'form_line_color': "Farba čiary:",
        'form_fill_color': "Farba výplne:",
        'form_choose_color': "Vybrať",
        'form_transparent': "Priehľadné pozadie (iba čiara)",
        'form_filled': "vyplnené",
        'form_dark_mode': "Tmavý režim",
        'form_dark_invert': "Invertovať farby v tmavom režime",
        'form_fine_tuning': "Doladenie (pixely)",
        'form_offset_x': "Posun X:",
        'form_offset_y': "Posun Y:",
        'form_offset_x_tooltip': "Záporné hodnoty posúvajú tvar pri ukladaní doľava, kladné doprava",
        'form_offset_y_tooltip': "Záporné hodnoty posúvajú tvar pri ukladaní hore, kladné dole",
        'form_preview': "Náhľad",
        'form_insert': "Vložiť tvar",
        'form_rectangle_insert': "Obdĺžnik",
        'form_ellipse_insert': "Elipsa/kruh",
        'form_line_insert': "Čiara (2 kliknutia)",
        'form_arrow_insert': "Šípka (2 kliknutia)",
        'form_customize': " Prispôsobiť tvar",
        'form_transparent_toggle': " Priehľadné pozadie",
        'form_discard': " Zahodiť tento tvar",
        'form_save_all': " Uložiť všetky tvary",
        'form_discard_all': " Zahodiť všetky tvary",
        'form_guide_title': "Vkladanie tvarov - Návod",
        'form_guide': """
📐 Vkladanie tvarov do PDF - Stručný návod:

1. Vyberte typ tvaru (obdĺžnik, elipsa, čiara, šípka)
2. Kliknite na miesto
   - Obdĺžnik/elipsa: jedno kliknutie umiestni tvar
   - Čiara/šípka: dve kliknutia pre počiatočný a koncový bod
3. Umiestnite tvar: ťahaním myšou
4. Upravte veľkosť: ťahaním za rohy/hrany
5. Uložiť tvar: Enter
6. Zahodiť tvar: ESC
7. Ďalšie úpravy: pravým kliknutím na tvar

Tip: V kontextovej ponuke môžete upraviť nastavenia.
        """,
        'form_inserted': "{0} vložený na stranu {1}",
        'form_deleted': "Tvar odstránený",
        'form_copied': "Tvar skopírovaný",
        'form_pasted': "Tvar vložený",
        'form_saved': "{0} tvarov bolo vložených do PDF.\n\nPDF bolo znovu načítané...",
        'form_saved_voice': "Uložených {0} tvarov",
        'form_reset': "Tvar obnovený na predvolenú veľkosť",
        'form_transparent_on': "zapnuté",
        'form_transparent_off': "vypnuté",
        'form_transparent_toggled': "Priehľadné pozadie {0}",
        'form_line_cancel': "Kreslenie čiary zrušené",
        'form_second_click': "Teraz kliknite na koncový bod pre {0}",
        'mode_replace_form': "Vložiť tvar",
        'mode_conflict_voice_form': "Režim {0} je aktívny. Ukončiť a vložiť tvar?",
        'form_settings_updated': "Nastavenia tvarov aktualizované",
        'form_unknown': "Tvar",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Kliknite na počiatočný bod",
        'form_line_guide_2': "2. Kliknite na koncový bod",
        'form_line_guide_3': "Čiara bude nakreslená medzi týmito dvoma bodmi.",
        'form_line_status_1': "Čakám na prvé kliknutie...",
        'form_line_status_2': "Prvý bod nastavený: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Teraz kliknite na koncový bod...",
        'form_line_status_4': "Oba body nastavené.\nKliknite na 'Hotovo' pre uloženie.",
        'form_line_reset': "Resetovať",
        'form_line_finish': "Hotovo",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopírovať (Cmd+C)",
        'paste': "Vložiť (Cmd+V)",
        'copied': "Skopírované: {0}",
        'no_element_to_copy': "Nie je vybraný žiadny prvok na kopírovanie",
        'no_copied_data': "Žiadne skopírované údaje",
        'no_valid_position': "Žiadne platné miesto na vloženie",
        'copy_text': "Text skopírovaný",
        'copy_image': "Obrázok skopírovaný",
        'copy_form': "Tvar skopírovaný",
        'copy_signature': "Podpis skopírovaný",
        'element_text': "Text",
        'element_image': "Obrázok",
        'element_form': "Tvar",
        'element_signature': "Podpis",
        'element_unknown': "Prvok",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflikt režimov",
        'mode_conflict_message': "Režim '{0}' je už aktívny.\n\nChcete ho ukončiť a {1}?",
        'mode_replace': "Ukončiť režim a {0}",
        'mode_cancel': "Zrušiť",
        'mode_replace_text': "vložiť text",
        'mode_replace_cross': "vložiť krížik",
        'mode_replace_signature': "vložiť podpis",
        'mode_replace_image': "vložiť obrázok",
        'mode_replace_form': "vložiť tvar",
        'mode_conflict_voice': "Režim {0} je aktívny. Ukončiť a vložiť text?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Zadávanie textu",
        'active_mode_signature': "Podpis",
        'active_mode_image': "Obrázok",
        'active_mode_form': "Tvar",
        'active_mode_and': " a ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Vložiť",
        'insert_another_text': "Vložiť text",
        'insert_another_cross': "Vložiť krížik",
        'insert_another_signature_1': "Podpis 1",
        'insert_another_signature_2': "Podpis 2",
        'insert_another_image': "Vložiť obrázok",
        'insert_another_form_rect': "Obdĺžnik",
        'insert_another_form_ellipse': "Elipsa",
        'insert_another_form_line': "Čiara (2 kliknutia)",
        'insert_another_form_arrow': "Šípka (2 kliknutia)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Uložiť {0}",
        'save_dialog_message': "{0} bude uložený na stranu {1}.\n\nAko chcete pokračovať?",
        'save_all': "Uložiť všetky {0}",
        'save_single': "Uložiť {0}",
        'save_customize': "Prispôsobiť {0}",
        'save_discard': "Zahodiť tento {0}",
        'save_continue': "Pokračovať v úpravách",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Prejsť na stranu {0}",
        'context_rotate': " Otočiť stranu {0}",
        'context_delete': " Odstrániť stranu {0}",
        'context_export': " Exportovať stranu {0}",
        'context_mark_as': " Označiť stranu ako...",
        'context_mark_empty': " Prázdna strana",
        'context_unmark_empty': " Už nie prázdna",
        'context_mark_export': " Označiť na export",
        'context_unmark_export': " Už neexportovať",
        'context_batch_actions': " Hromadné akcie",
        'context_batch_delete_empty': " Odstrániť všetkých {0} prázdnych strán",
        'context_batch_export_single': " Exportovať všetkých {0} strán (jeden súbor)",
        'context_batch_export_split': " Exportovať všetkých {0} strán (oddelené)",
        'context_drag_start': " Spustiť Drag & Drop",
        'context_drag_stop': " Ukončiť Drag & Drop",
        'context_insert': " Vložiť",
        'context_insert_pages': " Vložiť strany",
        'context_zoom': "Zoom",
        'discard_mixed': "Zahodiť všetkých {0} {1} a {2} {3}",
        'save_mixed': "Uložiť {0} {1} a {2} {3}",
        'discard_texts': "Zahodiť všetkých {0} textov",
        'discard_text_single': "Zahodiť 1 text",
        'save_texts': "Uložiť {0} textov",
        'save_text_single': "Uložiť 1 text",
        'discard_crosses': "Zahodiť všetkých {0} krížikov",
        'discard_cross_single': "Zahodiť 1 krížik",
        'save_crosses': "Uložiť {0} krížikov",
        'save_cross_single': "Uložiť 1 krížik",
        'discard_signatures': "Zahodiť všetkých {0} podpisov",
        'save_signature_single': "Uložiť 1 podpis",
        'save_signatures': "Uložiť {0} podpisov",
        'discard_images': "Zahodiť všetkých {0} obrázkov",
        'save_image_single': "Uložiť 1 obrázok",
        'save_images': "Uložiť {0} obrázkov",
        'discard_forms': "Zahodiť všetkých {0} tvarov",
        'save_form_single': "Uložiť 1 tvar",
        'save_forms': "Uložiť {0} tvarov",
        'cross_discard': "Zahodiť tento krížik",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informácie o exporte / importe",
        'export_what': "📋 Čo sa exportuje?",
        'export_general': "Všeobecné nastavenia",
        'export_general_items': "• Hlasové výstupy (zap./vyp., rýchlosť)\n• Tmavý/svetlý režim\n• Nastavenia záloh\n• Nastavenia OCR",
        'export_image_form': "Nastavenia obrázkov a tvarov",
        'export_image_form_items': "• Nastavenia obrázkov (pomer strán, predvolená veľkosť)\n• Nastavenia tvarov (hrúbka čiary, farby)\n• Nastavenia podpisov (cesty, veľkosti, časová pečiatka)",
        'export_passwords': "Databáza hesiel",
        'export_passwords_items': "• Všetky uložené heslá PDF\n• Voliteľne šifrované alebo nešifrované",
        'export_master': "Nastavenia hlavného hesla",
        'export_master_items': "• Hash hlavného hesla\n• Nastavenia pre podpisy/textové bloky",
        'export_signatures': "Podpisy a textové bloky",
        'export_signatures_items': "• Všetky obrazové súbory (podpisy)\n• Všetky textové bloky s formátovaním\n• Označenie súkromné/verejné",
        'export_import_warning': "⚠️ Dôležité upozornenia",
        'export_import_note': "• Pri importe budú VŠETKY aktuálne nastavenia prepísané\n• Je vyžadovaný reštart aplikácie\n• Existujúce podpisy/textové bloky budú nahradené",
        'export_master_note': "• Ak je nastavené hlavné heslo, môžete zvoliť:\n  - Nešifrované (heslá v plaintexte)\n  - Šifrované (čitateľné iba s hlavným heslom)",
        'export_security': "• Exportovaný ZIP súbor obsahuje dôverné údaje\n• Uchovávajte ho bezpečne (napr. na šifrovanom USB disku)\n• Pri strate súboru sú heslá nenávratne stratené",
        'export_format': "📁 Formát exportu",
        'export_format_desc': "Nastavenia sú uložené v jedinom ZIP súbore:",
        'export_filename': "Nastavenia_PDFDarkView_YYYYMMDD_HHMMSS.zip",
        'export_success': "Nastavenia boli úspešne exportované",
        'export_failed': "Export zlyhal",
        'export_import_question': "Chcete teraz reštartovať aplikáciu?",
        'export_password_question': "Je nastavené hlavné heslo.\n\nChcete exportovať heslá v nešifrovanej podobe?\n(inak budú exportované šifrovane)",
        'export_decrypt': "Exportovať nešifrovane",
        'export_encrypt': "Exportovať šifrovane",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informácie",
        'info_title': "O PDF Dark View",
        'info_version': "Verzia",
        'info_author': "Vyvinul Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "O programe",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> je prístupný PDF prehliadač, vyvinutý špeciálne pre ľudí so zrakovým postihnutím.</p>

            <p><strong>Kľúčové vlastnosti:</strong></p>
            <ul>
                <li>Kontrastné, prispôsobiteľné rozhranie</li>
                <li>Plné ovládanie z klávesnice</li>
                <li>Integrovaný hlasový výstup</li>
                <li>OCR pre naskenované dokumenty</li>
                <li>Rozsiahle nástroje na úpravu</li>
            </ul>

            <p>Podporovaných je viac ako 50 jazykov – aby boli PDF prístupné pre všetkých.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkcie",
        'info_features_intro': "PDF Dark View vám ponúka nasledujúce možnosti:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Zobrazenie a navigácia</strong> – Tmavý/Svetlý režim, listovanie stránkami, zoom, skok na stránku</li>
            <li><strong>OCR (rozpoznávanie textu)</strong> – Umožnite vyhľadávanie a kopírovanie v naskenovaných dokumentoch</li>
            <li><strong>Úpravy</strong> – Vkladanie textu, krížikov, podpisov, obrázkov a tvarov</li>
            <li><strong>Správa stránok</strong> – Mazanie, extrahovanie, vkladanie, presúvanie pomocou ťahania</li>
            <li><strong>Export</strong> – Do Wordu, Pages alebo ako text</li>
            <li><strong>Bezpečnosť</strong> – Ochrana a správa heslom</li>
            <li><strong>Prístupnosť</strong> – Hlasový výstup, ovládanie z klávesnice, vysoký kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Obsluha",
        'info_accessibility': "♿ Prístupnosť – plné ovládanie z klávesnice",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Všeobecné</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Otvoriť PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Hľadať</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Prepnúť tmavý/svetlý režim</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Tlačiť</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Ukončiť</div>

        <div class="shortcut-cat">📖 Navigácia</div>
        <div class="shortcut-row"><kbd>Klávesy so šípkami</kbd> Listovať stránku po stránke</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Prejsť na stránku</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Prvá stránka</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Posledná stránka</div>

        <div class="shortcut-cat">✏️ Úpravy</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Vložiť text</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Odstrániť stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extrahovať stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Vložiť stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Presunúť stránky</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Otočiť stránku</div>

        <div class="shortcut-cat">🖼️ Presúvanie prvkov</div>
        <div class="shortcut-row"><kbd>Klávesy so šípkami</kbd> Presunúť text/obrázok/podpis</div>
        <div class="shortcut-row"><kbd>Ctrl+Klávesy so šípkami</kbd> Väčšie kroky</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Uložiť</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Zahodiť</div>

        <div class="shortcut-cat">🗣️ Hlasový výstup</div>
        <div class="shortcut-row"><kbd>F2</kbd> Zapnúť/vypnúť hlasový výstup</div>
        """,
        'info_contextmenu': "📌 Dôležité: Všetky funkcie sú dostupné aj prostredníctvom kontextového menu (pravé tlačidlo myši)!",
        'info_accessibility_hint': "💡 Tip: Hlasový výstup (F2) uľahčuje orientáciu a poskytuje spätnú väzbu o menu a dialógových oknách.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licencia & Impresum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUM</strong><br>
        Informácie podľa § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Nemecko<br>
        E-mail: binhdiez64@gmail.com<br>
        Zodpovedný za obsah: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Vylúčenie zodpovednosti</strong><br>
        Softvér bol vyvinutý s maximálnou starostlivosťou. Neposkytuje sa žiadna záruka za správnosť, úplnosť a funkčnosť. Použitie je na vlastné riziko.<br><br>

        <strong>📄 Licencia MIT (súkromné použitie)</strong><br>
        Autorské práva (c) 2026 Toralf Schulz (BinhDiez)<br>
        Povolené: bezplatné používanie, súkromné zmeny, osobné kópie.<br>
        Nepovolené: predaj, komerčné použitie, odstránenie upozornení o autorských právach.<br><br>

        <strong>🔧 Komponenty tretích strán</strong><br>
        Tento softvér obsahuje komponenty pod licenciami GPL, AGPL, Apache 2.0, BSD a MIT.<br>
        Pri ďalšej distribúcii je potrebné dodržiavať príslušné licenčné podmienky.<br><br>

        <strong>🌐 Open Source</strong><br>
        Zdrojový kód je k dispozícii a možno ho prezerať, upravovať a ďalej distribuovať v súlade s príslušnými licenčnými podmienkami.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Poďakovanie",
        'info_credits': "Vďaka komunite open source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Spracovanie PDF</li>
            <li><strong>PyQt5</strong> – Grafické rozhranie</li>
            <li><strong>Tesseract OCR</strong> – Rozpoznávanie textu</li>
            <li><strong>OCRmyPDF</strong> – Integrácia OCR</li>
            <li><strong>python-docx</strong> – Export do Wordu</li>
            <li><strong>qtawesome</strong> – Ikony</li>
            <li><strong>DeepSeek</strong> – Podpora pri prekladoch (50+ jazykov)</li>
            <li><strong>Všetkým používateľom</strong> – Za cennú spätnú väzbu</li>
            <li><strong>Komunite open source</strong> – Za skvelé knižnice</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Jazyky",
        'info_languages_header': "🌍 Jazyková podpora",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View v súčasnosti podporuje <strong>62 jazykov</strong> – aby bolo možné softvér používať bez bariér na celom svete.</p>

            <p><strong>📖 Úplný zoznam jazykov (Stav: marec 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikánčina</li>
                    <li>🇦🇱 Albánčina (Shqip)</li>
                    <li>🇩🇿 Arabčina (العربية)</li>
                    <li>🇮🇩 Balijčina (Basa Bali)</li>
                    <li>🇧🇩 Bengálčina (বাংলা)</li>
                    <li>🇲🇲 Barmčina (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosniančina (Bosanski)</li>
                    <li>🇧🇬 Bulharčina (Български)</li>
                    <li>🇨🇳 Čínština (中文)</li>
                    <li>🇩🇰 Dánčina (Dansk)</li>
                    <li>🇩🇪 Nemčina (Deutsch)</li>
                    <li>🇬🇧 Angličtina (English)</li>
                    <li>🇪🇪 Estónčina (Eesti)</li>
                    <li>🇫🇮 Fínčina (Suomi)</li>
                    <li>🇫🇷 Francúzština (Français)</li>
                    <li>🇬🇷 Gréčtina (Ελληνικά)</li>
                    <li>🇮🇱 Hebrejčina (עברית)</li>
                    <li>🇮🇳 Hindčina (हिन्दी)</li>
                    <li>🇭🇷 Chorvátčina (Hrvatski)</li>
                    <li>🇭🇺 Maďarčina (Magyar)</li>
                    <li>🇮🇩 Indonézština (Bahasa Indonesia)</li>
                    <li>🇮🇪 Írčina (Gaeilge)</li>
                    <li>🇮🇸 Islandčina (Íslenska)</li>
                    <li>🇮🇹 Taliančina (Italiano)</li>
                    <li>🇯🇵 Japončina (日本語)</li>
                    <li>🇰🇭 Khmérčina (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Kórejčina (한국어)</li>
                    <li>🇱🇦 Laoština (ພາສາລາວ)</li>
                    <li>🇱🇻 Lotyština (Latviešu)</li>
                    <li>🇱🇹 Litovčina (Lietuvių)</li>
                    <li>🇱🇺 Luxemburčina (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajčina (Bahasa Melayu)</li>
                    <li>🇮🇳 Maráthčina (मराठी)</li>
                    <li>🇲🇳 Mongolčina (Монгол)</li>
                    <li>🇳🇵 Nepálčina (नेपाली)</li>
                    <li>🇳🇱 Holandčina (Nederlands)</li>
                    <li>🇳🇴 Nórčina (Norsk)</li>
                    <li>🇦🇫 Paštčina (پښتو)</li>
                    <li>🇮🇷 Perzština (فارسی)</li>
                    <li>🇵🇱 Poľština (Polski)</li>
                    <li>🇵🇹 Portugalčina (Português)</li>
                    <li>🇮🇳 Pandžábčina (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumunčina (Română)</li>
                    <li>🇷🇺 Ruština (Русский)</li>
                    <li>🇸🇪 Švédčina (Svenska)</li>
                    <li>🇷🇸 Srbčina (Српски)</li>
                    <li>🇸🇰 Slovenčina (Slovenčina)</li>
                    <li>🇸🇮 Slovinčina (Slovenščina)</li>
                    <li>🇪🇸 Španielčina (Español)</li>
                    <li>🇹🇿 Swahilčina (Kiswahili)</li>
                    <li>🇵🇭 Tagalčina (Filipino)</li>
                    <li>🇮🇳 Tamilčina (தமிழ்)</li>
                    <li>🇮🇳 Telugčina (తెలుగు)</li>
                    <li>🇹🇭 Thajčina (ไทย)</li>
                    <li>🇨🇿 Čeština (Čeština)</li>
                    <li>🇹🇷 Turečtina (Türkçe)</li>
                    <li>🇺🇦 Ukrajinčina (Українська)</li>
                    <li>🇵🇰 Urdčina (اردو)</li>
                    <li>🇻🇳 Vietnamčina (Tiếng Việt)</li>
                    <li>🇸🇳 Wolofčina (Wolof)</li>
                    <li>🇺🇸 Jidiš (ייִדיש)</li>
                    <li>🇿🇦 Zuluština (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Pridanie vlastných jazykov:</strong><br>
                Chcete jazyk, ktorý ešte nie je zahrnutý? Jednoducho umiestnite svoj vlastný súbor so slovníkom (<code>sprache_xx.py</code>) vedľa aplikácie – softvér ho automaticky rozpozná. Ak máte záujem o konkrétny preklad, neváhajte ma kontaktovať.
            </div>

            <p><strong>🙏 Osobitné poďakovanie:</strong> DeepSeek za podporu pri preklade všetkých slovníkov do 62 jazykov.</p>

            <p>📧 Kontakt pre preklady: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Chyba",
        'error_occurred': "Vyskytla sa chyba",
        'error_pdf_load': "Chyba pri načítaní PDF",
        'error_pdf_save': "Chyba pri ukladaní PDF",
        'error_ocr': "Chyba pri rozpoznávaní textu",
        'error_no_pdf': "Nie je nahrané žiadne PDF",
        'error_page_not_found': "Strana nenájdená",
        'error_invalid_range': "Neplatný rozsah strán",
        'error_file_not_found': "Súbor nenájdený",
        'error_permission': "Nedostatočné oprávnenia",
        'error_unknown': "Neznáma chyba",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Úspech",
        'success_operation': "Operácia úspešne dokončená",
        'success_saved': "Úspešne uložené",
        'success_exported': "Úspešne exportované",
        'success_imported': "Úspešne importované",
        'success_deleted': "Úspešne odstránené",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Potvrdenie",
        'confirm_yes': "Áno",
        'confirm_no': "Nie",
        'confirm_ok': "OK",
        'confirm_cancel': "Zrušiť",
        'confirm_delete': "Odstrániť",
        'confirm_overwrite': "Prepísať",
        'confirm_continue': "Pokračovať",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Načítavam PDF...",
        'progress_saving': "Ukladám PDF...",
        'progress_exporting': "Exportujem PDF...",
        'progress_processing': "Spracúvam...",
        'progress_wait': "Prosím čakajte...",
        'progress_preparing': "Pripravujem...",
        'progress_finalizing': "Finalizujem...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Biela",
        'color_black': "Čierna",
        'color_red': "Červená",
        'color_green': "Zelená",
        'color_blue': "Modrá",
        'color_yellow': "Žltá",
        'color_magenta': "Purpurová",
        'color_cyan': "Azúrová",
        'color_orange': "Oranžová",
        'color_gray': "Sivá",
        'color_custom': "Výber farby",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Súbor",
        'menu_edit': "&Upraviť",
        'menu_view': "&Zobraziť",
        'menu_tools': "&Nástroje",
        'menu_settings': "&Nastavenia",
        'menu_help': "&Pomocník",
        'menu_language': "🌐 Jazyk",
        'menu_guides': "&Návody",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Otvoriť",
        'file_save_as': "&Uložiť ako...",
        'file_protect': "&Chrániť dokument...",
        'file_export': "&Exportovať",
        'file_export_pages': "Exportovať do Pages",
        'file_export_word': "Exportovať do DOCX",
        'file_export_text': "Exportovať do TXT",
        'file_print_now': "&Tlačiť teraz",
        'file_print': "&Tlačiť",
        'file_close': "&Zatvoriť",
        'file_quit': "&Koniec",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Hľadať",
        'edit_ocr': " Vykonať OCR",
        'edit_rotate': "&Otočiť stranu",
        'edit_rotate_all': "Otočiť &všetky strany",
        'edit_delete_pages': "&Odstrániť strany",
        'edit_extract_pages': "&Extrahovať strany",
        'edit_insert_pages': "&Vložiť strany",
        'edit_move_pages': "&Presunúť strany",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Vložiť text a krížiky",
        'text_insert': " Vložiť text",
        'cross_insert': " Vložiť krížik",
        'text_customize': " Prispôsobiť text",
        'cross_customize': " Prispôsobiť tento krížik",
        'cross_customize_all': " Prispôsobiť všetky krížiky",
        'text_discard': " Zahodiť tento text / krížik",
        'text_discard_all': " Zahodiť všetky texty a krížiky",
        'text_save_all': " Uložiť všetky texty a krížiky",
        'text_guide': " Zadávanie textu / textové bloky - návod",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Vložiť podpis",
        'signature_settings_menu': " Nastavenia...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Vložiť obrázok",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Vložiť tvary",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Zobraziť okno textu",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Šírka strany (predvolené)",
        'view_zoom_two': "&Dve strany",
        'view_zoom_overview': "&Prehľad (viac strán)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Uľahčenie",
        'settings_voice': "Hlasový výstup",
        'settings_voice_tooltip': "dopĺňa informácie z čítačiek obrazovky o ďalšie údaje",
        'settings_signature': "&Nastavenia podpisov",
        'settings_password': "&Správa hesiel",
        'settings_backup': "Vytvoriť zálohu pred zmenami",
        'settings_export_import': "&Exportovať nastavenia / importovať nastavenia",
        'settings_export': "&Exportovať všetky nastavenia...",
        'settings_import': "&Importovať všetky nastavenia...",
        'settings_export_info': "&Čo sa exportuje?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "zap.",
        'voice_off': "vyp.",
        'voice_toggle': "Hlasový výstup {0}",
        'voice_speed': "Rýchlosť {0} percent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Nástroj nenájdený:\n{0}\n\nBASE_DIR: {1}\nUistite sa, že nástroje pre PDF sú nainštalované v adresári {1}.",
        'tool_started': "{0} spustený",
        'tool_start_failed': "Nedá sa spustiť",
        'process_error_failed_to_start': "Nedá sa spustiť proces. Existuje súbor?",
        'process_error_crashed': "Proces spadol počas spúšťania.",
        'process_error_timeout': "Dosiahnutý časový limit procesu.",
        'process_error_write': "Chyba zápisu v procese.",
        'process_error_read': "Chyba čítania v procese.",
        'process_error_unknown': "Neznáma chyba procesu",
        'process_command': "Príkaz",
        'process_normal_exit': "normálne ukončený",
        'process_crashed': "spadol",
        'process_nonzero_exit': "{0} bol ukončený s chybovým kódom {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Ruší sa...",
        'move_cancelling': "Ruší sa presúvanie",
        'opening_pdf': "Otváram PDF...",
        'loading_document': "Načítavam dokument...",
        'pdf_opened': "PDF otvorené",
        'pages_found_moving': "Nájdených {0} strán, {1} na presunutie",
        'creating_backup': "Vytváram zálohu...",
        'backup_description': "Zálohujem pôvodný súbor...",
        'backup_saved_as': "Zálohované ako: {0}",
        'error_format': "Chyba: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Hľadanie resetované",
        'page_header_simple': "=== Strana {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Správa hesiel – Návod",
        'password_guide_voice': "Návod na správu hesiel. Prečítajte si prosím poznámky.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Správa hesiel – Podrobný návod</strong></p>

        <p><strong>1. Ochrana PDF heslom</strong></p>
        <ul>
        <li>Pri otváraní PDF chráneného heslom sa zobrazí dialóg, do ktorého môžete zadať heslo.</li>
        <li>Heslo môžete uložiť v šifrovanej podobe, aby ste ho nemuseli zadávať zakaždým znova (zaškrtávacie políčko „Uložiť heslo“).</li>
        <li>Tlačidlom „Odstrániť heslo“ môžete vytvoriť dešifrovanú kópiu PDF a heslo odstrániť z databázy.</li>
        </ul>

        <p><strong>2. Hlavné heslo</strong></p>
        <ul>
        <li>Hlavné heslo chráni prístup ku všetkým uloženým heslám PDF.</li>
        <li><strong>Nastavenie:</strong> Prejdite do „Nastavenia → Správa hesiel → Nastavenia hlavného hesla“ a kliknite na „Nastaviť hlavné heslo“. Zvoľte silné heslo (aspoň 8 znakov).</li>
        <li><strong>Zmena:</strong> Po úspešnom overení môžete hlavné heslo zmeniť.</li>
        <li><strong>Odstránenie:</strong> Ak hlavné heslo odstránite, budú VŠETKY uložené heslá nenávratne vymazané. Pred odstránením môžete exportovať záložnú kópiu.</li>
        <li>Raz za reláciu sa musíte overiť hlavným heslom, aby ste získali prístup k chráneným funkciám (napr. zobrazenie hesiel).</li>
        </ul>

        <p><strong>3. Správa hesiel (zoznam)</strong></p>
        <ul>
        <li>V „Nastavenia → Správa hesiel“ sa otvorí tabuľka všetkých uložených PDF s ich šifrovanými heslami.</li>
        <li><strong>Bez hlavného hesla:</strong> Môžete iba mazať záznamy – heslá zostávajú skryté.</li>
        <li><strong>S hlavným heslom (overené):</strong> Môžete heslá zobrazovať, kopírovať, exportovať a mazať.</li>
        <li><strong>Export:</strong> Vyberte formát (JSON, CSV, TXT) a uložte zoznam. Ak je nastavené hlavné heslo, môžete zvoliť, či sa heslá exportujú v nešifrovanej alebo šifrovanej podobe.</li>
        <li><strong>Import:</strong> Predtým exportovaný ZIP súbor (všetky nastavenia) možno znovu načítať cez „Nastavenia → Exportovať nastavenia / importovať nastavenia“. Upozornenie: Existujúce údaje budú prepísané!</li>
        </ul>

        <p><strong>4. Generátor hesiel</strong></p>
        <ul>
        <li>V dialógu hesla (napr. pri zabezpečovaní PDF) je napravo od vstupného poľa tlačidlo s kockou 🎲.</li>
        <li>Kliknutím naň otvoríte generátor hesiel. Môžete nastaviť dĺžku, znakové sady (veľké písmená, malé písmená, číslice, špeciálne znaky) a oddeľovač pre lepšiu čitateľnosť.</li>
        <li>Vygenerované heslo možno priamo použiť a v prípade potreby skopírovať.</li>
        </ul>

        <p><strong>5. Dôležité bezpečnostné poznámky</strong></p>
        <ul>
        <li>Uložené heslá sú uchovávané šifrované pomocou AES-256. Kľúč je odvodený z hlavného hesla (ak je nastavené) alebo z pevnej hodnoty (bez hlavného hesla).</li>
        <li>Bez hlavného hesla sú heslá síce šifrované, ale kľúč je uložený v programe – útočník s prístupom k vašim súborom by ich mohol dešifrovať. Preto dôrazne odporúčame používať hlavné heslo.</li>
        <li>Databáza hesiel je uložená v súbore `Data/passwords.json`. Pravidelne zálohujte, najmä pred odstránením hlavného hesla.</li>
        <li>Pri strate hlavného hesla sú všetky uložené heslá nenávratne stratené.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Režim invertovania",
        'invert_mode_classic': "Klasický (invertovať všetky farby)",
        'invert_mode_smart': "Inteligentný (invertovať iba jas)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Prahová hodnota odtieňov sivej",
        'gray_threshold_10': "10% (prísny)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Štandardný)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (mäkký)",
        'threshold_changed': "Prahová hodnota nastavená na {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Prahová hodnota odtieňov sivej – Vysvetlenie",
        'threshold_guide_text': "Prahová hodnota odtieňov sivej určuje, ktoré pixely v inteligentnom tmavom režime sa považujú za 'sivé' a invertujú sa.\n\n"
                                "• Nízka hodnota (10%) invertuje iba takmer dokonalé odtiene sivej – farebné prvky zostávajú úplne zachované.\n"
                                "• Vysoká hodnota (50%) invertuje aj mierne farebné pixely – to zvyšuje kontrast, ale môže skresliť farby.\n\n"
                                "Optimálna hodnota závisí od dokumentu. Pre čisto textové dokumenty je 30–40% často ideálne, pre farebnú grafiku skôr 10–20%.\n\n"
                                "Hodnotu môžete kedykoľvek upraviť prostredníctvom ponuky 'Nastavenia' – PDF sa okamžite znova načíta.\n\n"
                                "Poznámka:\n* Fotografie a obrázky je možné správne zobraziť iba v svetlom režime!\n* Nastavenia invertovania sa zobrazujú iba vtedy, keď je aktivovaný tmavý režim.",
        'threshold_guide_voice': "Prahová hodnota odtieňov sivej určuje, ako silno inteligentný tmavý režim zasahuje. Nízka hodnota šetrí farby, vysoká zvyšuje kontrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Otváranie PDF...",
        'progress_loading_document': "Načítavanie dokumentu...",
        'progress_pdf_opened': "PDF otvorené",
        'progress_creating_backup': "Vytváranie zálohy...",
        'progress_backup_description': "Zabezpečovanie pôvodného súboru...",
        'progress_backup_created': "Záloha vytvorená",
        'progress_backup_saved_as': "Uložené ako: {0}",
        'progress_analyzing_start': "Spúšťanie analýzy...",
        'progress_searching_empty': "Hľadanie prázdnych stránok...",
        'progress_page_empty': "Stránka {0} je prázdna",
        'progress_page_keep': "Ponechať stránku {0}",
        'progress_analysis_complete': "Analýza dokončená",
        'progress_empty_found': "Nájdených {0} prázdnych stránok",
        'progress_current_page': "Aktuálna stránka",
        'progress_mark_delete': "Označuje sa na odstránenie",
        'progress_range_selected': "Rozsah stránok {0}-{1}",
        'progress_deleting_pages': "Odstraňuje sa {0} stránok",
        'progress_creating_new_pdf': "Vytváranie nového PDF...",
        'progress_transferring_pages': "Prenášanie stránok",
        'progress_keeping_page': "Stránka {0} bude ponechaná ({1}/{2})",
        'progress_saving_pdf': "Ukladanie PDF...",
        'progress_optimizing': "Optimalizácia veľkosti súboru...",
        'progress_finalizing': "Finalizácia...",
        'progress_new_size': "Nová veľkosť: {0:.2f} MB",
        'progress_cancelling': "Ruší sa...",
        'progress_cancel_message': "{0} sa ruší",
        'progress_pages_found_moving': "Nájdených {0} stránok, {1} na presun",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analýza PDF...",
        'ocr_status_optimizing': "Prebieha optimalizácia obrázka...",
        'ocr_status_recognizing': "Prebieha rozpoznávanie textu...",
        'ocr_status_embedding': "Vkladanie textu...",
        'ocr_status_finalizing': "Finalizácia PDF...",

        # PDF-Laden
        'progress_preparing': "Príprava...",
        'progress_loading': "Načítavanie PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Odstraňovanie stránok...",
        'progress_moving_title': "Presúvanie stránok...",
        'pages_found': "Nájdené stránky",
        'progress_creating_new_order': "Vytváranie nového poradia...",
        'progress_sorting_pages': "Zoraďovanie stránok...",
        'progress_moving_to_begin': "Presunúť {0} stránok na začiatok",
        'progress_transferring_count': "Preniesť {0} stránok",
        'progress_transferring_before_target': "Preniesť stránky pred cieľ",
        'progress_moving_pages': "Presunúť {0} stránok",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_zaloha_",
        'filename_protected_suffix': "_chraneny_",
        'filename_copy_suffix': "_Kopia",
        'filename_page_single': "_Strana_",
        'filename_page_range': "_Strany_",
        'filename_export_page': "_Strana_{0:03}",
        'filename_export_range': "_Strany_{0}-{1}",
        'filename_export_multiple': "_Strany_{0}",
        'filename_with_text': "_s_Textom",
        'filename_with_signature': "_s_Podpisom",
        'filename_with_image': "_s_Obrazkom",
        'filename_with_forms': "_s_Tvarmi",
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
        'view_toggle_navbar': "Zobraziť panel tlačidiel",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Nie je možné odstrániť všetky strany",
		'pages_cannot_delete_last_page': 'Posledná strana sa nedá odstrániť!',
		'pages_cannot_delete_all_pages': 'V dokumente musí zostať aspoň jedna strana!',
		'delete_pages_confirm': 'Naozaj chcete odstrániť {0} strán?',
		'delete_pages_confirm_voice': 'Naozaj chcete odstrániť {0} strán?',
		'pages_deleted': '{0} strán bolo úspešne odstránených.',
		'warning': 'Varovanie',
		'error': 'Chyba',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nie je vybraný formulár",
        'form_customized': "Formulár prispôsobený",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Vybrať",
        'btn_use': "Použiť",
        'master_password_for_spasswords': "Na ukladanie a používanie hesiel je potrebné najprv nastaviť hlavné heslo.\n\nChcete nastaviť hlavné heslo teraz?",
        'open_saved_dialog_title': "Otvoriť uložený súbor",
        'open_saved_question': "Chcete otvoriť uložený súbor teraz?",
        'password': "Heslo",
        'password_manager_master_required': "Správca hesiel je dostupný len vtedy, ak je nastavené hlavné heslo.\n\nChcete nastaviť hlavné heslo teraz?",
        'password_master_required_for_select': "Ak chcete zobraziť a vybrať uložené heslá, musíte sa najprv overiť svojím hlavným heslom.\n\nChcete sa overiť teraz?",
        'password_not_available': "Vybrané heslo nie je dostupné alebo ho nebolo možné dešifrovať.",
        'password_options_title': "Možnosti hesla",
        'password_save_choice_change': "Nastaviť nové heslo",
        'password_save_choice_keep': "Použiť existujúce heslo",
        'password_save_choice_none': "Uložiť nešifrované",
        'password_save_hint': "Najprv nastavte hlavné heslo na bezpečné ukladanie hesiel.",
        'password_save_master_required': "Uložiť heslo (možné len s hlavným heslom)",
        'password_save_question': "Aktuálny PDF je chránený heslom. Chcete použiť existujúce heslo, nastaviť nové alebo uložiť nešifrované?",
        'password_select': "Vybrať heslo",
        'password_select_none': "Nebolo vybrané žiadne heslo.\n\nVyberte heslo zo zoznamu.",
        'password_select_one': "Vyberte presne jedno heslo.\n\nOznačili ste viacero hesiel.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_záloha",
        'filename_insert_suffix': "_s_vložením",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_stránky_odstránené",
        'filename_pages_moved': "_stránky_presunuté",
        'filename_rotated_all_suffix': "_všetky_stránky_otočené",
        'filename_rotated_suffix': "_stránka_otočená",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfigurácia názvov súborov pri zmenách PDF",
        'filename_keep_suffixes': "Zachovať predchádzajúce prípony (napr. _s_textom)",
        'filename_keep_suffixes_false': "Nahradiť",
        'filename_keep_suffixes_true': "Zachovať",
        'filename_preview_label': "Ukážka názvu súboru:",
        'filename_preview_overwrite_hint': "Ukážka nie je k dispozícii – originál sa prepíše.",
        'filename_separator': "Oddeľovač medzi slovami",
        'filename_separator_none': "Žiadny oddeľovač",
        'filename_separator_space': "Medzera ( )",
        'filename_separator_underscore': "Podčiarkovník (_)",
        'filename_settings_saved': "Nastavenia názvu súboru boli uložené",
        'filename_settings_title': "Formátovanie názvu súboru a záloha",
        'filename_timestamp_position': "Pozícia časovej pečiatky",
        'filename_timestamp_position_after': "Za základným názvom",
        'filename_timestamp_position_before': "Úplne vpredu",
        'filename_timestamp_position_end': "Na konci",
        'filename_use_timestamp': "Použiť časovú pečiatku",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Správanie pri zmenách:</b><ul><li>Odstraňovanie a vkladanie stránok</li><li>Vkladanie textu, podpisu, obrázka a tvarov</li><li>OCR</li></ul></html>",
        'backup_section': "Záloha pre operácie so stránkami (Odstrániť, Presunúť)",
        'behavior_info': "Poznámka: Pri 'Prepísať originál' sa časové pečiatky a prípony ignorujú – súbor si zachováva svoj názov.",
        'behavior_new_file': "Vždy vytvoriť nový súbor (s časovou pečiatkou a príponou)",
        'behavior_overwrite': "Prepísať originál (žiadny nový súbor)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Všetky stránky boli otočené.\n\nOriginál zostal nezmenený.\nNový súbor: {0}",
        'all_pages_rotated_voice': "Všetky stránky otočené, vytvorený nový súbor.",
        'empty_pages_deleted_new_file': "{0} prázdnych stránok bolo odstránených.\n\nOriginál zostal nezmenený.\nNový súbor: {1}",
        'empty_pages_deleted_voice': "{0} prázdnych stránok odstránených, vytvorený nový súbor.",
        'ocr_keep_original': "Zachovať originál (neskôr otvoriť manuálne)",
        'ocr_new_file_question': "Nový vyhľadávateľný PDF bol uložený ako:\n{0}\n\nChcete ho teraz otvoriť?",
        'ocr_open_new': "Otvoriť nový OCR súbor",
        'ocr_original_kept': "Pôvodný súbor zostáva otvorený. OCR súbor bol uložený.",
        'page_deleted_new_file': "Stránka {0} bola odstránená.\n\nOriginál zostal nezmenený.\nNový súbor: {1}",
        'page_deleted_voice': "Stránka {0} odstránená, vytvorený nový súbor.",
        'page_rotated_new_file': "Stránka {0} bola otočená.\n\nOriginál zostal nezmenený.\nNový súbor: {1}",
        'page_rotated_voice': "Stránka {0} otočená, vytvorený nový súbor.",
        'pages_deleted_new_file': "Bolo odstránených {0} stránok.\n\nPôvodný súbor zostal nezmenený.\nNový súbor: {1}",
        'pages_deleted_new_file_voice': "{0} stránok odstránených, vytvorený nový súbor.",
        'pages_inserted_new_file': "Bolo vložených {0} stránok.\n\nPôvodný súbor zostal nezmenený.\nNový súbor: {1}",
        'pages_inserted_new_file_ask': "Bolo vložených {0} stránok.\n\nOriginál zostal nezmenený.\nNový súbor: {1}\n\nChcete ho teraz otvoriť?",
        'pages_inserted_voice_new': "{0} stránok vložených, vytvorený nový súbor.",
        'pages_moved_new_file': "Bolo presunutých {0} stránok.\n\nPôvodný súbor zostal nezmenený.\nNový súbor: {1}",
        'pages_moved_new_file_voice': "{0} stránok presunutých, vytvorený nový súbor.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Už nezobrazovať",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Nastavenie zálohy</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Záloha ZAPNUTÁ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Pri všetkých zmenách, ktoré prepisujú originál</strong> (text, podpis, obrázok, tvar, OCR, otáčanie, vkladanie, odstraňovanie/presúvanie stránok) sa <strong>automaticky vytvorí záloha s časovou pečiatkou</strong> pred vykonaním zmeny.</p>
                <p style="margin: 5px 0 5px 20px;">• Záloha sa nachádza vedľa pôvodného súboru (napr. <code>Dokument_záloha_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Ak ste dodatočne aktivovali možnosť <strong>„Prepísať originál“</strong>, vytvorí sa tiež záloha.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Záloha VYPNUTÁ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Žiadna záloha sa nevytvára</strong> – ani pri prepisovaní, ani pri operáciách so stránkami.</p>
                <p style="margin: 5px 0 5px 20px;">• Pôvodný súbor môže byť pri prepísaní nenávratne stratený.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Odporúča sa len pre skúsených používateľov!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Nastavenie zálohy je nezávislé od možnosti „Prepísať originál“. Môžete kombinovať obe.<br>
                Túto správu môžete natrvalo skryť.
            </div>
        </div>
        """,
        'backup_info_title': "Správanie zálohy",
        'backup_info_voice': "Oznámenie o správaní zálohy pri operáciách so stránkami. Záloha zapnutá prepisuje originál, záloha vypnutá vytvára nový súbor.",
        'show_backup_info': "Informácie o nastavení zálohy",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Už nezobrazovať",
        'overwrite_enable_backup': "Aktivovať zálohu (odporúča sa)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Prepísať originál</p>
            <p>Ak aktivujete túto možnosť, zmeny (text, podpis, obrázok, tvar, OCR, otáčanie, vkladanie) sa <strong>uložia priamo do originálu</strong> – <strong>nevytvorí sa žiadny nový súbor</strong>.</p>
            <p>• Názov súboru zostáva nezmenený.<br>
            • Časové pečiatky a prípony sa ignorujú.<br>
            • <strong>Bez zálohy môže byť originál nenávratne stratený.</strong></p>
            <p style="color: #FFD700;">Odporúčanie: Dodatočne aktivujte možnosť zálohy, aby ste získali automatické zálohy.</p>
        </div>
        """,
        'overwrite_info_title': "Prepísať originál",
        'overwrite_info_voice': "Upozornenie: Prepísať originál – žiadny nový súbor. Záloha sa odporúča.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Bolo vložených {0} stránok.\n\nPôvodný súbor bol prepísaný.\nBola vytvorená záloha.",
        'pages_inserted_overwrite_no_backup': "Bolo vložených {0} stránok.\n\nPôvodný súbor bol prepísaný.\nNEBOLA vytvorená žiadna záloha.",
        'texts_saved_overwrite_with_backup': "Zmeny boli uložené v origináli.\n\nBola vytvorená záloha.",
        'texts_saved_overwrite_no_backup': "Zmeny boli uložené v origináli.\n\nNEBOLA vytvorená žiadna záloha.",
        'texts_crosses_saved_new_file': "{0} {1} a {2} {3} boli vložené.\n\nPôvodný súbor zostal nezmenený.\nBol vytvorený nový súbor.\n\nNačítava sa nový PDF...",
        'texts_saved_new_file': "{0} {1} bolo vložených.\n\nPôvodný súbor zostal nezmenený.\nBol vytvorený nový súbor.\n\nNačítava sa nový PDF...",
        'crosses_saved_new_file': "{0} {1} bolo vložených.\n\nPôvodný súbor zostal nezmenený.\nBol vytvorený nový súbor.\n\nNačítava sa nový PDF...",
        'elements_saved_new_file': "{0} prvkov bolo vložených.\n\nPôvodný súbor zostal nezmenený.\nBol vytvorený nový súbor.\n\nNačítava sa nový PDF...",
        'signatures_saved_overwrite_with_backup': "Podpis(y) bol(i) uložený(é) v origináli.\n\nBola vytvorená záloha.",
        'signatures_saved_overwrite_no_backup': "Podpis(y) bol(i) uložený(é) v origináli.\n\nNEBOLA vytvorená žiadna záloha.",
        'images_saved_overwrite_with_backup': "Obrázok(ky) bol(i) uložený(é) v origináli.\n\nBola vytvorená záloha.",
        'images_saved_overwrite_no_backup': "Obrázok(ky) bol(i) uložený(é) v origináli.\n\nNEBOLA vytvorená žiadna záloha.",
        'forms_saved_overwrite_with_backup': "Tvar(y) bol(i) uložený(é) v origináli.\n\nBola vytvorená záloha.",
        'forms_saved_overwrite_no_backup': "Tvar(y) bol(i) uložený(é) v origináli.\n\nNEBOLA vytvorená žiadna záloha.",
        'signatures_saved_new_file': "{0} podpisov bolo vložených.\n\nPôvodný súbor zostal nezmenený.\nBol vytvorený nový súbor.\n\nNačítava sa nový PDF...",
        'images_saved_new_file': "{0} obrázkov bolo vložených.\n\nPôvodný súbor zostal nezmenený.\nBol vytvorený nový súbor.\n\nNačítava sa nový PDF...",
        'forms_saved_new_file': "{0} tvarov bolo vložených.\n\nPôvodný súbor zostal nezmenený.\nBol vytvorený nový súbor.\n\nNačítava sa nový PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Upozornenie: Tento PDF obsahuje otočené stránky. Umiestnenie sa môže líšiť.",
        'page_rotated_warning_title': "Zistená otočená stránka",
        'page_rotated_warning_message': "Aktuálna stránka {0} je otočená o {1}°.\n\nVkladanie prvkov na otočené stránky nie je podporované.\n\nChcete teraz otočiť stránku do zvislej polohy?",
        'page_rotated_warning_voice': "Upozornenie: Stránka je otočená. Najprv ju otočte.",
        'paste_on_rotated_page_simple_warning': "Vkladanie na stránku {0} nie je možné!\n\nTáto stránka je otočená o {1}°.\n\nNajprv otočte stránku na 0° (Ponuka: Upraviť → Zarovnať stránku).\n\nUpozornenie:\nPredtým skopírovaný prvok sa stratí, ak neuložíte pred otočením stránky.",
        'paste_on_rotated_page_voice': "Vkladanie bolo zrušené. Stránka je otočená. Najprv zarovnajte stránku.",
        'page_rotated_cancel': "Zrušiť",
        'page_rotated_rotate_until_upright': "Opakovane otáčať stránku (kým nie je zvislá)",
        'page_rotated_now_upright': "Stránka je teraz zvislá. Teraz môžete vkladať.",
        'page_rotated_still_not_upright': "Stránku nebolo možné otočiť do zvislej polohy. Opravte manuálne.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Pomocník: Oprava otočených stránok",
        'help_rotated_pages_voice': "Otvára sa pomocník pre opravu otočených stránok.",
        'btn_help': "Pomocník",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problém: Otočená stránka – Vkladanie nefunguje správne</p>

            <p>Ak vkladanie textov, podpisov alebo tvarov na otočenej stránke nefunguje správne, môžete stránku opraviť externým editorom PDF.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Riešenie s externým nástrojom (napr. macOS Náhľad)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Exportovať stránku</strong><br>
                &nbsp;&nbsp;Kliknite v ponuke na <strong>Súbor → Exportovať ako stránky</strong> alebo použite inú metódu na uloženie požadovanej stránky ako jedného PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Otvoriť stránku v externom programe</strong><br>
                &nbsp;&nbsp;Otvorte exportovaný PDF v editore PDF (napr. <strong>macOS Náhľad</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Otočiť stránku</strong><br>
                &nbsp;&nbsp;Otočte stránku tak, aby bola zvislá (v Náhľade: <strong>Nástroje → Otočiť</strong> alebo <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Uložiť</strong><br>
                &nbsp;&nbsp;Uložte opravenú stránku (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Znova vložiť stránku do pôvodného dokumentu</strong><br>
                &nbsp;&nbsp;Vráťte sa do PDFDarkView a vložte opravenú stránku na požadované miesto:<br>
                &nbsp;&nbsp;<strong>Upraviť → Vložiť stránky</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatíva: Otočiť stránku v origináli</p>
                <p style="margin: 5px 0 5px 20px;">• Použite vstavanú funkciu otáčania (<strong>Upraviť → Otočiť stránku</strong>) na postupné opravenie stránky.<br>
                • Po každom otočení môžete skontrolovať, či vkladanie teraz funguje.<br>
                • Toto je často rýchlejšie riešenie – vyskúšajte ho najprv!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> Ak často narážate na otočené stránky, môžete natrvalo skryť upozornenie v dialógovom okne vkladania.<br>
                Umiestnenie sa potom môže líšiť – používajte túto možnosť len vtedy, ak poznáte dôsledky.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Zarovnať stránky",
        'menu_rotate_normalize_tooltip': "Otočiť stránku alebo resetovať na 0°",
        'normalize_current_page': "Dostať aktuálnu stránku do zvislej polohy (nastaviť na 0°)",
        'normalize_all_pages': "Dostať všetky stránky do zvislej polohy (nastaviť na 0°)",
        'page_normalized': "Stránka {0} bola nastavená do zvislej polohy.",
        'all_pages_normalized': "Všetky stránky boli nastavené do zvislej polohy.",
        'page_already_upright': "Stránka {0} je už zvislá.",
        'all_pages_already_upright': "Všetky stránky sú už zvislé.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF neobsahuje žiadny vyhľadávateľný text.</p><p>Chcete vykonať OCR na export do {0}?</p>",
        'export_ocr_voice': "PDF neobsahuje žiadny text. Na export do {0} je potrebné OCR.",
        'export_no_ocr_possible': "Export bez OCR nie je možný. Vykonajte OCR cez ponuku.",
        'ocr_failed_export_not_possible': "OCR zlyhalo. Export nemožno vykonať.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF sa otvorí v Náhľade. Spustite tam proces tlače.",
        'print_preview_manual': "PDF bol otvorený. Vykonajte príkaz tlače manuálne (napr. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Zlúčiť PDF",
        'merge_pdfs': "Zlúčiť PDF",
        'merge_progress_title': "Zlúčenie PDF...",
        'merge_pdfs_list': "PDF v poradí (Presuňte myšou na zoradenie)",
        'merge_add_pdf': "Pridať PDF",
        'merge_remove': "Odstrániť",
        'merge_move_up': "Hore",
        'merge_move_down': "Dole",
        'merge_pdfs_info': "💡 Tip: Poradie môžete zmeniť presunutím myšou",
        'merge_no_pdfs': "Neboli vybrané žiadne PDF. Kliknite na 'Pridať PDF'.",
        'merge_info': "Vybraných {0} PDF (približne {1} stránok)",
        'merge_open_file': "Otvoriť súbor",
        'merge_merge': "Zlúčiť",
        'merge_error': "Chyba pri zlučovaní",
        'merge_min_two_pdfs_error': "Vyberte aspoň dva PDF súbory na zlúčenie.",
        'merge_select_pdfs': "Vyberte PDF na zlúčenie",
        'merge_error_file': "Chyba pri spracovaní",
        'merge_cancelled': "Zlúčenie bolo zrušené",
        'merge_preparing': "Príprava...",
        'merge_processing': "Spracúva sa PDF {0} z {1}",
        'merge_saving': "Ukladá sa zlúčený PDF...",
        'merge_complete': "Hotovo!",
        'merge_success_title': "Zlúčenie bolo úspešné",
        'merge_success_voice': "{0} PDF bolo úspešne zlúčených.",
        'merge_success_message': "{0} PDF bolo úspešne zlúčených.\n\nNový dokument má teraz {1} stránok.\n\nNový súbor:\n{2}\n\nMiesto uloženia:\n{3}\n{2}\n\nChcete otvoriť tento PDF?",
        'replace_file_title': "Nahradiť súbor?",
        'replace_file_message': "Už je otvorený PDF. Chcete ho nahradiť novým súborom?",
        'btn_yes': "Áno",
        'btn_no': "Nie",
        'filename_merge_suffix': "zlúčené",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Otvara sa {0}...",
        'progress_merge_reading': "Číta sa {0}...",
        'progress_merge_adding': "Pridáva sa {0} stránok...",
        'progress_merge_optimizing': "Optimalizuje sa PDF...",
        'progress_merge_writing': "Zapisuje sa PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "zatvorenie PDF",
        'action_close_window': "zatvorenie okna",
        'action_open_new_pdf': "otvorenie nového PDF",
        'action_quit_app': "ukončenie aplikácie",
        'changes_saved': "Zmeny boli uložené.",
        'file_close_title': "Zatvoriť PDF súbor",
        'save_before_action': "Majú sa zmeny uložiť pred {0}? Áno alebo Nie?",
        'save_before_action_voice': "Majú sa zmeny uložiť pred {0}? Áno alebo Nie?",
        'save_before_close_question': "Majú sa zmeny uložiť pred zatvorením? Áno alebo Nie?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Bol vytvorený vyhľadávateľný PDF:\n\n{0}\n\n<b>v prípade potreby to skúste znova",
        "ocr_rotate_title": "Vyrovnať stránky pred OCR",
        "ocr_rotate_question": "PDF obsahuje otočené stránky.\nChcete pred OCR vyrovnať všetky stránky na 0°?\nTo výrazne zlepšuje rozpoznávanie textu.",
        "ocr_rotate_yes": "Áno, vyrovnať",
        "ocr_rotate_no": "Nie, spustiť OCR priamo",
        "ocr_rotate_voice": "PDF obsahuje otočené stránky. Majú sa všetky stránky pred OCR vyrovnať?",
        "ocr_not_performed_message": "Nie je prítomný žiadny text. Vykonajte OCR (ponuka \"Upraviť\" → \"Vykonať OCR\" alebo kláves Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Nastavenia OCR",
        "ocr_language_btn": "Vybrať jazyk OCR",
        "ocr_language": "Jazyk(y) OCR",
        "ocr_language_current": "Aktuálny jazyk:",
        "ocr_param_info": "Informácie o parametri",

        "ocr_force_ocr_label": "Vynútiť OCR",
        "ocr_deskew_label": "Opraviť zošikmenie",
        "ocr_clean_label": "Vyčistiť obrázok",
        "ocr_oversample_label": "Rozlíšenie (DPI)",
        "ocr_pagesegmode_label": "Rozdelenie stránky",
        "ocr_oem_label": "Režim motora OCR",
        "ocr_optimize_label": "Kompresia PDF",
        "ocr_jobs_label": "Paralelné procesy",
        "ocr_verbose_label": "Podrobnosť záznamu",

        "ocr_force_ocr_tooltip": "Vynútiť OCR na každej stránke, aj keď text už existuje",
        "ocr_deskew_tooltip": "Automaticky vyrovnať zošikmené skenovanie",
        "ocr_clean_tooltip": "Odstrániť šum a artefakty z obrázka",
        "ocr_oversample_tooltip": "Zväčšiť obrázok pred OCR na toto DPI",
        "ocr_pagesegmode_tooltip": "Určuje, ako sa stránka rozdelí na textové oblasti",
        "ocr_oem_tooltip": "Vyberá OCR motor programu Tesseract",
        "ocr_optimize_tooltip": "Úroveň kompresie výstupného PDF",
        "ocr_jobs_tooltip": "Počet paralelných OCR procesov",
        "ocr_verbose_tooltip": "Úroveň podrobnosti výstupu záznamu",
        "ocr_settings_explain_btn": "Vysvetlenie",

        "ocr_force_ocr_explain": "Vynucuje rozpoznávanie textu na <b>každej</b> stránke, aj keď už obsahuje text.\n\nOdporúčanie: <b>Zap.</b> pre skenované PDF, <b>Vyp.</b> pre natívne PDF s už existujúcim textom.",

        "ocr_deskew_explain": "Opravuje mierne zošikmené skenovanie (až asi 5°).\n\nOdporúčanie: <b>Zap.</b> pre skenované dokumenty, <b>Vyp.</b> ak sú stránky už dokonale rovné.",

        "ocr_clean_explain": "Odstraňuje šum, bodky a malé artefakty z obrázka.\n<b>DÔLEŽITÉ:</b> Pre arabské, thajské alebo vietnamské texty s diakritickými znamienkami (bodky nad/pod písmenami) by táto možnosť mala byť <b>vypnutá</b>, inak môžu dôjsť k strate dôležitých znakov.",

        "ocr_oversample_explain": "Zväčšuje obrázok <b>pred</b> rozpoznávaním textu na uvedené DPI.<br><br>• <b>72-150 DPI:</b> Veľmi rýchle, ale nízka miera rozpoznávania<br>• <b>200-300 DPI:</b> Optimálny rozsah (Štandard: 300)<br>• <b>400+ DPI:</b> Len o málo lepšie rozpoznávanie, ale výrazne väčšie súbory<br><br>Odporúčanie: 300 DPI pre zložité písma (arabské, čínske, japonské), 200 DPI pre západné jazyky.",

        "ocr_pagesegmode_explain": "Určuje, ako program Tesseract rozdelí stránku na textové oblasti.\n\n• <b>3 - Automaticky (Štandard):</b> Dobré pre zmiešané rozloženia\n• <b>4 - Jednotlivý stĺpec:</b> Pre texty s jedným stĺpcom\n• <b>5 - Vertikálny blok:</b> Pre vertikálne písma (japonské, čínske)\n• <b>6 - Jednotný textový blok:</b> Optimálne pre plynulý text bez stĺpcov\n• <b>11 - Surový obrázok:</b> Pre zlé skenovanie / rukopis\n\nOdporúčanie: <b>6</b> pre jednoduché textové dokumenty, <b>3</b> pre zložité rozloženia.",

        "ocr_oem_explain": "Vyberá OCR motor programu Tesseract.\n\n• <b>0 - Legacy:</b> Starý motor (rýchly, ale menej presný)\n• <b>1 - LSTM:</b> Neurónový motor (pomalší, ale presnejší)\n• <b>2 - Legacy + LSTM:</b> Kombinuje oba výsledky\n• <b>3 - Štandard (LSTM preferovaný):</b> Najlepšia voľba pre väčšinu prípadov\n\nOdporúčanie: <b>3</b> pre maximálnu presnosť rozpoznávania.",

        "ocr_optimize_explain": "Komprimuje výstupné PDF.\n\n• <b>0:</b> Žiadna optimalizácia (najrýchlejšie spracovanie)\n• <b>1:</b> Ľahká optimalizácia (dobrý kompromis)\n• <b>2:</b> Mierna optimalizácia\n• <b>3:</b> Silná optimalizácia (najmenší súbor, ale pomalší)\n\nOdporúčanie: <b>1</b> pre každodenné použitie.",

        "ocr_jobs_explain": "Počet paralelných procesov pre OCR.\n\n• <b>1:</b> Pomalé, ale najnižšia spotreba pamäte\n• <b>4-8:</b> Optimálne pre moderné viacjadrové procesory\n• <b>12+:</b> Len o málo rýchlejšie spracovanie s vysokou spotrebou pamäte\n\nOdporúčanie: Počet jadier CPU (napr. <b>4</b> na 4-jadrových systémoch).",

        "ocr_verbose_explain": "Úroveň podrobnosti výstupu záznamu v konzole.\n\n• <b>0:</b> Žiadny výstup\n• <b>1:</b> Priebeh a stavové správy\n• <b>2:</b> Podrobný výstup\n• <b>3:</b> Úplný výstup ladenia (veľmi rozsiahly)\n\nOdporúčanie: <b>1</b> pre normálnu prevádzku.",

        "ocr_reset_title": "Nastavenia boli resetované",
        "ocr_reset_message": "Všetky nastavenia OCR boli resetované na štandardné hodnoty.",
        "info_tooltip": "Viac informácií o tomto parametri",
        "ocr_reset_defaults": "Resetovať na štandard",

        "ocr_psm_0": "Automaticky (motor Legacy)",
        "ocr_psm_1": "Automatická detekcia stĺpcov",
        "ocr_psm_3": "Automaticky (Štandard)",
        "ocr_psm_4": "Jednotlivý stĺpec",
        "ocr_psm_5": "Vertikálny blok",
        "ocr_psm_6": "Jednotný textový blok",
        "ocr_psm_7": "Jednotlivý riadok textu",
        "ocr_psm_8": "Jednotlivé slovo",
        "ocr_psm_11": "Surový obrázok (žiadna analýza rozloženia)",

        "ocr_oem_0": "Motor Legacy (rýchly)",
        "ocr_oem_1": "Motor LSTM (neurónový, presný)",
        "ocr_oem_2": "Legacy + LSTM kombinovaný",
        "ocr_oem_3": "Štandard (LSTM preferovaný)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Jazyk(y) OCR...",
        "ocr_language_title": "Vyberte jazyk(y) OCR",
        "ocr_language_instruction": "Vyberte jazyk(y) pre rozpoznávanie textu (OCR).\nPozor: Viaceré jazyky idú na úkor výkonu a presnosti!\nNajlepšie výsledky dosiahnete, ak vyberiete iba jeden jazyk.",
        "ocr_language_predefined": "Preddefinované kombinácie",
        "ocr_language_custom": "Vlastné...",
        "ocr_language_selected": "Vybrané jazyky OCR",
        "ocr_language_changed": "Jazyk OCR bol zmenený na {0}",
        "ocr_language_auto_detect": "Dostupné jazyky sa automaticky detegujú.",
        "ocr_language_none_found": "Nenašli sa žiadne jazykové údaje Tesseract! Nainštalujte jazykové balíky (napr. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Vlastný výber jazyka",
        "ocr_language_available": "Dostupné jazyky (nainštalované):",
        "ocr_language_select_hint": "Vyberte jeden alebo viac jazykov:",
        "ocr_language_confirm": "Použiť",
        "ocr_language_reset": "Resetovať na štandard (deu+eng+vie)",
        "ocr_language_priorities": "Odporúčané jazyky (predinštalované):",

        "select_all_languages": "Vybrať všetko",
        "clear_all_languages": "Zrušiť výber",
        "install_language_packs": "Nainštalovať chýbajúce jazykové balíky...",
        "install_hint": "💡 Tip: Nie všetky jazyky sú nainštalované vo vašom systéme. Pomocou tohto tlačidla získate pomoc s inštaláciou.",
        "ocr_language_install_title": "Inštalácia jazykových balíkov Tesseract",

        "ocr_missing_languages": "Chýbajúce jazykové balíky OCR",
        "ocr_missing_languages_message": "Nasledujúce vybrané jazyky nie sú nainštalované vo vašom systéme:\n\n{0}\n\nNainštalujte chýbajúce jazykové balíky (pozrite pomoc v 'Pomoc s inštaláciou').\n\nChcete teraz otvoriť pomoc s inštaláciou?",
        "ocr_missing_languages_voice": "Chýbajúce jazykové balíky. Nainštalujte chýbajúce jazyky.",
        "ocr_install_help_now": "Otvoriť pomoc",
        "ocr_continue_anyway": "Napriek tomu skúsiť",
        "ocr_language_error_title": "Chyba jazyka OCR",
        "ocr_language_error_message": "Chyba počas rozpoznávania textu: {0}\n\nSkontrolujte svoje nastavenia jazyka OCR (Nastavenia → Jazyk OCR).",
        "ocr_install_help_button": "Pomoc s inštaláciou",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Inštalácia jazykových balíkov Tesseract</p>

        <p>Aby OCR fungovalo v konkrétnom jazyku, príslušné jazykové údaje musia byť nainštalované vo vašom systéme. Postupujte podľa pokynov pre váš operačný systém:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Otvorte <strong>Terminál</strong> (Finder → Programy → Pomôcky → Terminál).</li>
        <li>Nainštalujte všetky dostupné jazyky pomocou:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Môže to trvať niekoľko minút.)</li>
        <li>Alebo iba jednotlivé jazyky (napr. vietnamčinu):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Pri súčasných verziách Homebrew môže byť potrebné stiahnuť <code>*.traineddata</code> ručne (pozri nižšie).</li>
        <li>Po inštalácii: Zatvorte tento dialóg a znova otvorte výber jazyka OCR – nové jazyky sa zobrazia automaticky.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Otvorte terminál (Ctrl+Alt+T).</li>
        <li>Nainštalujte požadovaný jazyk, napr. pre vietnamčinu:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Dôležité jazykové kódy: <code>deu</code> (nemčina), <code>eng</code> (angličtina), <code>vie</code> (vietnamčina), <code>spa</code> (španielčina), <code>fra</code> (francúzština), <code>ita</code> (taliančina), <code>nld</code> (holandčina), <code>fin</code> (fínčina), <code>swe</code> (švédčina), <code>nor</code> (nórčina).</li>
        <li>Zobraziť všetky dostupné balíky:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ručne)</p>
        <ol>
        <li>Stiahnite požadované súbory <code>*.traineddata</code> z:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (napr. <code>vie.traineddata</code> pre vietnamčinu).</li>
        <li>Skopírujte súbory do priečinka jazykov Tesseract, zvyčajne:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Prispôsobte individuálnej inštalácii.)</li>
        <li>Reštartujte aplikáciu (alebo znova otvorte výber jazyka OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatíva pre všetky systémy</p>
        <ul>
        <li>Nainštalujte <strong>OCRmyPDF</strong> a <strong>Tesseract</strong> pomocou správcu balíkov podľa vášho výberu. Väčšina inštalácií už obsahuje niektoré štandardné jazyky (angličtinu, nemčinu, francúzštinu).</li>
        <li>Chýbajúce jazyky je možné kedykoľvek nainštalovať – výber jazyka OCR zobrazuje iba skutočne existujúce jazyky.</li>
        </ul>

        <hr>
        <p><b>✅ Po inštalácii:</b> Nie je potrebné reštartovať aplikáciu – novo pridané jazyky sa okamžite zobrazia v zozname.</p>
        <p><b>📖 Pomoc s jazykovými kódmi:</b> Úplný zoznam je k dispozícii v <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentácii Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Písma Noto Sans",
        "info_noto_font_voice": "Sprievodca inštaláciou písiem Noto Sans",
        "btn_info_noto_font_install": "Informácie o písme",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Ako nainštalovať bezplatné písma Noto od spoločnosti Google</h2>

        <p><strong>Písma Noto</strong> sú rodina písiem s otvoreným zdrojovým kódom od spoločnosti Google. Ich cieľom je nevidieť <em>"žiadne tofu"</em> (t. j. žiadne prázdne políčka □) a správne zobraziť každý znak zo štandardu Unicode. Sú ideálnym doplnkom pre aplikácie, ktoré musia zobrazovať texty v mnohých rôznych jazykoch.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Inštalácia na macOS</h3>

        <p><strong>Metóda 1: S Homebrew (pre pokročilých)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metóda 2: Prostredníctvom "Font Book" (Odporúčané)</strong></p>

        <ol>
        <li>Stiahnite oficiálny balík písiem:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Rozbaľte súbor ZIP</li>
        <li>Skopírujte súbory do <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Inštalácia na Windows (10 & 11)</h3>

        <p><strong>Metóda 1: Microsoft Store (Odporúčané)</strong><br>
        Vyhľadajte "Google Noto Fonts" alebo "Noto Sans" a kliknite na <strong>Inštalovať</strong>.</p>

        <p><strong>Metóda 2: Ručná inštalácia</strong></p>

        <ol>
        <li>Stiahnuť:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Rozbaliť ZIP</li>
        <li>Vyberte súbory .ttf / .otf</li>
        <li>Kliknite pravým tlačidlom myši → <strong>Inštalovať</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        alebo<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Meno\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Inštalácia na Linux</h3>

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

        <p>Overenie:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Správa záložiek",
        "bookmark_add": "Pridať záložku",
        "bookmark_add_tooltip": "Uložiť aktuálnu stránku ako záložku",
        "bookmark_remove": "Odstrániť záložku",
        "bookmark_remove_tooltip": "Odstrániť označenú záložku",
        "bookmark_remove_all": "Odstrániť všetky",
        "bookmark_remove_all_tooltip": "Odstrániť všetky záložky tohto PDF",
        "bookmark_jump": "Prejsť na záložku",
        "bookmark_jump_tooltip": "Prejsť na vybranú stránku",
        "bookmark_name": "Názov",
        "bookmark_page": "Stránka",
        "bookmark_no_bookmarks": "Žiadne záložky.\nKliknutím na 'Pridať' uložíte aktuálnu stránku ako záložku.",
        "bookmark_added": "Záložka pre stránku {0} pridaná: {1}",
        "bookmark_removed": "Záložka odstránená: {0}",
        "bookmark_all_removed": "Všetky záložky boli odstránené.",
        "bookmark_name_default": "Stránka {0}",
        "bookmark_name_prompt": "Názov záložky:\n(dlhý text bude skrátený na 50 znakov)",
        "bookmark_name_prompt_title": "Názov záložky",
        "bookmark_confirm_remove_all": "Naozaj chcete odstrániť všetkých {0} záložiek?",
        "menu_bookmarks": "Záložky",
        "bookmark_manage": "Správa záložiek",
        "bookmark_next": "Ďalšia záložka",
        "bookmark_prev": "Predchádzajúca záložka",
        "bookmark_page_display": "Stránka {0}",
        "bookmark_exists": "Záložka pre túto stránku s týmto názvom už existuje.",
        "bookmark_select_first": "Najprv vyberte záložku.",
        "bookmark_confirm_remove": "Naozaj chcete odstrániť záložku 'Stránka {0}: {1}'?",
        "bookmark_jumped_to": "Prejdené na záložku '{0}' na stránke {1}.",
        "bookmark_jumped_to_voice": "Záložka {0}, stránka {1}",
        "btn_close": "Zatvoriť",

        "bookmark_list": "Vaše záložky",
        "bookmark_rename": "Premenovať záložku",
        "bookmark_rename_tooltip": "Zmeniť názov vybranej záložky",
        "bookmark_rename_title": "Premenovať záložku",
        "bookmark_rename_prompt": "Nový názov pre záložku na stránke {0}:\n(max. 50 znakov)",
        "bookmark_renamed": "Záložka '{0}' bola premenovaná na '{1}'.",
        "bookmark_item_tooltip": "Stránka {0}: {1}\nDvojitým kliknutím prejdete",
        "bookmark_name_exists_question": "Záložka s názvom '{0}' už na tejto stránke existuje.\nNapriek tomu premenovať?",

        "context_bookmarks": "Záložky",
        "context_bookmark_add_here": "Pridať záložku pre túto stránku",
        "context_bookmarks_existing": "Existujúce záložky:",
        "context_bookmarks_jump": "Prejsť na záložku:",
        "context_bookmarks_none": "Žiadne záložky",
        "context_bookmarks_clear_all": "Odstrániť všetkých {0} záložiek",

        "bookmark_search_placeholder": "Hľadať záložky... (názov alebo stránka)",
        "bookmark_search_results": "Zistených %d záložiek pre \"%s\"",
        "bookmark_no_search_results": "Žiadne záložky pre \"%s\"",
        "bookmark_no_search_results_label": "Žiadne výsledky pre \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Upraviť metadáta PDF",
        "metadata_title": "Názov",
        "metadata_title_placeholder": "Názov dokumentu",
        "metadata_title_tooltip": "Názov dokumentu (zobrazuje sa v hlavičke)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Meno autora",
        "metadata_author_tooltip": "Tvorca dokumentu",
        "metadata_subject": "Predmet",
        "metadata_subject_placeholder": "Predmet dokumentu",
        "metadata_subject_tooltip": "Stručný opis obsahu",
        "metadata_keywords": "Kľúčové slová",
        "metadata_keywords_placeholder": "Kľúčové slová oddelené čiarkami",
        "metadata_keywords_tooltip": "Kľúčové slová na kategorizáciu dokumentu",
        "metadata_creator": "Tvorca",
        "metadata_creator_placeholder": "Aplikácia, ktorá vytvorila PDF",
        "metadata_creator_tooltip": "Softvér, s ktorým bol dokument vytvorený",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Aplikácia, ktorá konvertovala PDF",
        "metadata_producer_tooltip": "Softvér, ktorý konvertoval PDF",
        "metadata_creation_date": "Dátum vytvorenia",
        "metadata_creation_date_tooltip": "Dátum vytvorenia dokumentu",
        "metadata_mod_date": "Dátum úpravy",
        "metadata_mod_date_tooltip": "Dátum poslednej úpravy",
        "metadata_pdf_info": "📄 Informácie o PDF",
        "metadata_pages": "Počet stránok",
        "metadata_file_size": "Veľkosť súboru",
        "metadata_pdf_version": "Verzia PDF",
        "metadata_encrypted": "Šifrované",
        "metadata_encrypted_yes": "Áno (chránené heslom)",
        "metadata_encrypted_no": "Nie",
        "metadata_reload": "📂 Znova načítať z PDF",
        "metadata_reset": "Zahodiť zmeny",
        "metadata_reloaded": "Metadáta boli znovu načítané z PDF.",
        "metadata_reset_done": "Všetky polia metadát boli resetované.",
        "metadata_no_file": "Žiadny súbor PDF nie je načítaný.",
        "metadata_save_error": "Chyba pri ukladaní metadát",
        "metadata_saved": "Metadáta boli úspešne uložené.",
        "metadata_pdf_version_unknown": "PDF (neznáme)",
        "metadata_saved_message": "Metadáta boli úspešne uložené.",
        "metadata_saved_voice": "Metadáta uložené.",

        "metadata_custom": "🔧 Vlastné metadáta",
        "metadata_custom_placeholder": "{\n  \"moje_pole\": \"moja_hodnota\",\n  \"iné_pole\": 123\n}",
        "metadata_custom_tooltip": "Formát JSON pre vlastné metadáta (voliteľné)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Šablóna \"{0}\" vybraná - Dvojitým kliknutím vložíte",
        "text_use_template": "Použiť textový blok",
        "text_type": "Typ",
        "text_search_templates": "Hľadať textové bloky...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informácie o exporte / importe",
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

        <h3>📦 Čo sa exportuje? (Prehľad)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Všeobecné nastavenia aplikácie</span></li>
            <li class="detail">• Tmavý/Svetlý režim</li>
            <li class="detail">• Inverzia tmavého režimu pre obrázky</li>
            <li class="detail">• Sivá prahová hodnota</li>
            <li class="detail">• Jazyk</li>
            <li class="detail">• Geometria okna</li>
            <li class="detail">• Režim priblíženia</li>
            <li class="detail">• Navigácia (Navigačný panel viditeľný)</li>
            <li class="detail">• Hlasový výstup (zap./vyp.)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavenia zálohovania</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Pomenovanie súborov (Časová značka, Oddeľovač, Prípony)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavenia pre vloženia</span></li>
            <li class="detail">• Podpisy</li>
            <li class="detail">• Text a textové bloky</li>
            <li class="detail">• Značky, obrázky a tvary</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nastavenia OCR</span></li>
            <li class="detail">• Jazyk</li>
            <li class="detail">• Vynútiť OCR · Režim stránky</li>
            <li class="detail">• Predspracovanie obrazu: Oprava zošikmenia, Vyčistenie, Nadmerné vzorkovanie</li>
            <li class="detail">• Počet paralelných úloh</li>
            <li class="detail">• Režim inverzie</li>
            <li class="detail">• Sivá prahová hodnota</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Záložky</span></li>
            <li class="detail">• Všetky záložky na súbor PDF (Stránka, Názov, Čas vytvorenia)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Databáza hesiel</span></li>
            <li class="detail">• Uložené heslá PDF (voliteľne šifrované alebo čistý text)</li>
            <li class="detail">• Haš hlavného hesla (ak je nastavené)</li>
            <li class="detail">• Overovacie údaje</li>
        </ul>

        <h4>⚠️ Dôležité poznámky</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Pri importe:</strong>
            <ul>
                <li><span class="warning">➜ VŠETKY aktuálne nastavenia budú úplne prepísané</span></li>
                <li>• Reštartovanie aplikácie je povinné</li>
                <li>• Existujúce podpisy, textové bloky a záložky budú nahradené</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Hlavné heslo a režim exportu:</strong>
            <ul>
                <li>• Keď je hlavné heslo aktívne, môžete si vybrať:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dešifrované</strong></span> (heslá sú v ZIP ako čistý text)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Šifrované</strong></span> (čitateľné len s hlavným heslom na cieľovom systéme)</li>
                <li>• Haš hlavného hesla je <strong>vždy</strong> uložený šifrovane</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Bezpečnostné upozornenie:</strong>
            <ul>
                <li>• Exportovaný súbor ZIP obsahuje citlivé údaje (<strong>heslá, záložky, podpisy</strong>)</li>
                <li>• Uchovávajte ho na bezpečnom mieste (napr. šifrovaný USB kľúč, správca hesiel)</li>
                <li>• Ak sa súbor stratí, uložené heslá PDF sú nenávratne stratené</li>
            </ul>
        </div>

        <h4>📁 Formát exportu</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Nastavenia sa ukladajú do jedného súboru ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Tento ZIP obsahuje úplný <code>settings.json</code> (z vašej konfigurácie) a prípadne vložené súbory obrázkov podpisov a šifrované heslá.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Podpisy - Sprievodca",
        'signature_guide_html': """
        📝 <strong>Podpisy - Rýchly sprievodca</strong><br>
        <ul>
        <li>Nastavte hlavné heslo</li>
        <li>Nakonfigurujte podpisy v ponuke <em>Nastavenia</em> (veľkosť, časová pečiatka, …)</li>
        <li>Vložte pomocou <strong>PRAVÉHO TLAČIDLA</strong> na požadovanú pozíciu (hlavné heslo vyžadované raz za reláciu)</li>
        <li>Presuňte podpis myšou alebo šípkami</li>
        <li>Vložte niekoľko podpisov za sebou</li>
        <li>Prispôsobte každý podpis individuálne</li>
        <li>Zahoďte jednotlivý podpis</li>
        <li>Uložte / zahoďte všetky podpisy naraz</li>
        <li>Alternatívne je možné použiť aj panel s ponukami.</li>
        </ul>
        """,
        'signature_guide_voice': "Rýchly sprievodca pre podpisy. Nastavte hlavné heslo. Nakonfigurujte podpisy v nastaveniach. Vložte pravým tlačidlom.",

        'image_guide_title': "Vkladanie obrázkov - Sprievodca",
        'image_guide_html': """
        📷 <strong>Vkladanie obrázkov do PDF - Rýchly sprievodca</strong><br>
        <ol>
        <li>Pravým tlačidlom na požadovanej pozícii</li>
        <li><em>„Vložiť obrázok“</em> → Vyberte obrázok</li>
        <li>Umiestnite obrázok: Potiahnite myšou</li>
        <li>Upravte veľkosť: Potiahnite za rohy/okraje</li>
        <li>Zachovajte pomer strán: Kláves <strong>[A]</strong></li>
        <li>Ďalšie úpravy: Pravým tlačidlom na obrázku</li>
        </ol>
        <p><strong>Tip:</strong> V kontextovej ponuke môžete upraviť nastavenia.</p>
        """,
        'image_guide_voice': "Rýchly sprievodca pre obrázky. Pravým tlačidlom, vložiť obrázok, vyberte. Umiestnite myšou, upravte veľkosť na rohoch. Pomer strán klávesom A.",

        'form_guide_title': "Vkladanie tvarov - Sprievodca",
        'form_guide_html': """
        📐 <strong>Vkladanie tvarov do PDF - Rýchly sprievodca</strong><br>
        <ol>
        <li>Vyberte typ tvaru (obdĺžnik, elipsa, čiara, šípka)</li>
        <li>Kliknite na pozíciu:
            <ul>
            <li>Pre obdĺžnik/elipsu: Jedno kliknutie umiestni tvar</li>
            <li>Pre čiaru/šípku: Dve kliknutia pre začiatočný a koncový bod</li>
            </ul>
        </li>
        <li>Umiestnite tvar: Potiahnite myšou</li>
        <li>Upravte veľkosť: Potiahnite za rohy/okraje</li>
        <li>Uložte tvar: <strong>Enter</strong></li>
        <li>Zahoďte tvar: <strong>ESC</strong></li>
        <li>Ďalšie úpravy: Pravým tlačidlom na tvare</li>
        </ol>
        <p><strong>Tip:</strong> V kontextovej ponuke môžete upraviť nastavenia.</p>
        """,
        'form_guide_voice': "Rýchly sprievodca pre tvary. Vyberte typ tvaru. Pre obdĺžnik alebo elipsu kliknite raz, pre čiaru alebo šípku dvakrát. Umiestnite myšou, upravte veľkosť na rohoch. Uložte Enterom, zahoďte Escapom.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "predchádzajúci",
        "btn_next_result": "nasledujúci",
        "ocr_text_window": "OCR textové okno",
        "bookmark_existing": "Existujúce záložky",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Porovnanie OCR Mac - Windows",
        'ocr_method_mac_win_title': "Rozdiely OCR medzi Mac a Windows",
        'ocr_method_mac_win_voice': "Mac je lepší",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Rozdiely medzi macOS a Windows</strong></p>

        <p><strong>macOS (odporúča sa)</strong></p>
        <p>Nástroj:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Výsledok:</p>
        <ul>
        <li>Vyhľadávateľný PDF s vloženým textom, ktorý do značnej miery zachováva pôvodný rozvrh.</li>
        </ul>
        <p>Výhody:</p>
        <ul>
        <li>Vynikajúca kvalita rozpoznávania textu (aj na krivých stranách).</li>
        <li>Zachovanie vektorovej grafiky a písiem.</li>
        <li>Lišta priebehu GUI prostredníctvom vyhodnocovania podprocesu.</li>
        <li>Úplná kontrola nad všetkými parametrami OCR (Deskew, Clean, Oversample, optimalizácia).</li>
        <li>Vyhľadávanie textu je priamo dostupné v hlavnom okne (zobrazenie PDF).</li>
        </ul>
        <p>Nevýhody:</p>
        <ul>
        <li>Vyžaduje ďalšie systémové nástroje (ocrmypdf, Ghostscript, unpaper, pngquant – sú súčasťou balíka aplikácie).</li>
        <li>Komplexnejšia správa chýb (zablokovania, časové limity).</li>
        </ul>

        <p><strong>Windows (stabilná alternatíva)</strong></p>
        <p>Nástroj:</p>
        <ul>
        <li>pytesseract (priame pripojenie k Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Výsledok:</p>
        <ul>
        <li>Vyhľadávateľný PDF, ktorý vizuálne zodpovedá obrázkovému PDF, ale je vyhľadávateľný vďaka priehľadnému textu.</li>
        </ul>
        <p>Výhody:</p>
        <ul>
        <li>Žiadne ma teraz nenapadajú.</li>
        </ul>
        <p>Nevýhody:</p>
        <ul>
        <li>PDF je v podstate obrázok s neviditeľným textom; rozvrh sa môže pri zložitých dokumentoch (stĺpce, tabuľky) mierne odchyľovať.</li>
        <li>Žiadna automatická korekcia zošikmenia (--deskew) ani čistenie obrazu (--clean).</li>
        <li>Lišta priebehu GUI sa aktualizuje iba hrubo na základe počtu spracovaných strán.</li>
        <li>Rýchlosť OCR je mierne pomalšia (pretože každá strana sa spracúva samostatne).</li>
        <li>Vyhľadávanie textu sa presmeruje do OCR textového okna.</li>
        </ul>

        <p><strong>Spoločné črty</strong></p>
        <ul>
        <li>Obe metódy vytvárajú vyhľadávateľný PDF v rovnakom adresári ako zdrojový súbor.</li>
        <li>Nastavenia OCR (jazyk, DPI, režim segmentácie stránky, režim motora OCR) je možné nakonfigurovať cez OCRSettingsDialog a sú platné v oboch implementáciách.</li>
        </ul>

        <p><strong>Odporúčanie:</strong></p>
        <ul>
        <li>macOS: Binárny súbor ocrmypdf poskytuje najlepšie výsledky – Kúpte si Mac a používajte verziu (PDFDarkView pre Macy s čipom Apple Silicon alebo Intel). Výsledky OCR sú lepšie ako v systéme Windows!</li>
        <li>Windows: Použite riešenie pytesseract. Je stabilné a poskytuje úplne dostatočnú kvalitu pre väčšinu dokumentov.</li>
        </ul>

        <p><strong>Dôležitá poznámka:</strong></p>
        <ul>
        <li>Obe verzie sú plne integrované do používateľského rozhrania – používateľ nebadá žiadny rozdiel.</li>
        <li>Program automaticky rozhoduje, ktorý motor OCR sa použije, na základe operačného systému.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Vytvoriť podpis (zo skenu)",
        "signature_create_title": "Vyberte naskenovaný podpis (PDF/obrázok)",
        "image_pdf_filter": "Obrázky a PDF",
        "signature_pdf_empty": "PDF neobsahuje žiadne strany.",
        "signature_created_success": "Podpis bol úspešne vytvorený: {0}",
        "signature_create_error": "Chyba pri vytváraní podpisu:\n{0}",
        "rembg_missing": "rembg nie je nainštalovaný.\nNainštalujte: pip install rembg\nChyba: {0}",
        "signature_name_title": "Názov súboru pre podpis",
        "signature_name_message": "Zadajte názov súboru pre nový podpis (uloží sa ako PNG s priehľadným pozadím):",
        "signature_name_label": "Názov súboru:",
        "signature_name_voice": "Zadajte názov súboru pre podpis",
        "signature_processing": "Spracovanie prebieha...",
        "signature_creation_title": "Vytvára sa podpis",
        "signature_overwrite_warning": "Súbor '{0}' už existuje. Prepísať?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Pripraviť PDF pre podpis",
        "signature_prepare_instruction":"Vyberte PDF, ktoré na jednej strane obsahuje naskenovaný podpis.\n\nOptimálne rozpoznanie dosiahnete, ak:\n• Podpis je napísaný čiernym atramentom (guľôčkové pero alebo fixka) na bielom papieri.\n• Podpis sa nachádza v hornej tretine inak prázdnej strany A4.\n• PDF bolo naskenované s rozlíšením aspoň 300 dpi.\n• Podpis je jasný a nie príliš tenký.\n• Nie sú prítomné žiadne rušivé vzory pozadia alebo čiary.",
        "signature_prepare_voice":"Vyberte PDF s naskenovaným podpisom. Dbajte na dobrú kvalitu a kontrast.",
        "sig_thickness_label":"Hrúbka čiary:",
        "sig_thickness_normal":"Normálna (tenká)",
        "sig_thickness_bold":"Tučná (odporúčané)",
        "sig_thickness_very_bold":"Veľmi tučná",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Pridanie jazykov GUI a OCR - Sprievodca",
        'language_guide_title': "Pridanie jazykov GUI a OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Stiahnite požadovaný prekladový súbor <code>translations_xy.py</code> z<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        a umiestnite ho do nasledujúceho adresára:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Otvorte svoj webový prehliadač.</li>
        <li>Prejdite na: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Na pravom okraji obrazovky vyhľadajte „Releases“ a vyberte to označené <strong>„latest“</strong>.</li>
        <li>Na nasledujúcej stránke vydania si v dolnej časti stiahnite súbor <code>Source Code.zip</code>.</li>
        <li>Rozbaľte súbor ZIP.</li>
        <li>V rozbalenom priečinku nájdite všetky jazykové súbory, ktoré potrebujete, a skopírujte ich do adresára:<br/>
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
        "menu_watermark":"Vložiť vodoznak",
        "fullpage_text_watermark_title":"Text ako vodoznak",
        "fullpage_image_watermark_title":"Obrázok ako vodoznak",
        "filename_with_watermark":"_s_vodoznakom",
        "watermark_text":"Text:",
        "watermark_text_placeholder":"Váš text vodoznaku...",
        "watermark_font_family":"Písmo:",
        "watermark_font_size":"Veľkosť písma:",
        "watermark_format":"Formátovanie:",
        "watermark_bold":"Tučné",
        "watermark_italic":"Kurzíva",
        "watermark_color":"Farba:",
        "watermark_choose_color":"Vyberte farbu...",
        "watermark_opacity":"Nepriehľadnosť / Priehľadnosť:",
        "watermark_direction":"Smer čítania:",
        "watermark_direction_l_r":"Vľavo → Vpravo",
        "watermark_direction_bl_tr":"Dole vľavo → Hore vpravo",
        "watermark_direction_tl_br":"Hore vľavo → Dole",
        "watermark_direction_b_t":"Dole → Hore",
        "watermark_direction_t_b":"Hore → Dole",
        "watermark_preview":"Náhľad:",
        "watermark_preview_sample":"Ukážkový text",
        "watermark_empty_text":"Zadajte text.",
        "watermark_applied":"Vodoznak bol aplikovaný na všetky strany.",
        "watermark_saved":"Vodoznak bol uložený.",
        "image_scale":"Veľkosť:",
        "image_preview":"Náhľad obrázka:",
        "no_image_selected":"Nebol vybraný žiadny obrázok",
        "browse":"Prehľadávať...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redakcie",
        "redact_add_black": "Redakcia (čierna)",
        "redact_add_white": "Redakcia (biela / vymazanie)",
        "redact_added_black": "Pridaná čierna redakcia",
        "redact_added_white": "Pridaná biela redakcia",
        "redact_apply_all": "Použiť všetky redakcie a uložiť",
        "redact_discard_all": "Zahodiť všetky redakcie",
        "redact_discard": "Zahodiť túto redakciu",
        "no_redactions": "Žiadne redakcie",
        "redact_confirm_title": "Trvalo použiť redakcie",
        "redact_confirm_message": "Varovanie: Označené oblasti budú nenávratne vymazané (čierne alebo biele).\nBude vytvorená záloha (ak je povolená).\n\nPokračovať?",
        "redact_apply": "Áno, redigovať teraz",
        "redact_saved": "{0} redakcia(e) úspešne použitá(e) a uložená(e).",
        "redact_saved_voice": "{0} redakcia(e) použitá(e)",
        "redact_error": "Chyba pri redakcii",
        "filename_redacted":"_redigované",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Vložiť čísla strán',
        'page_numbers_format': 'Formát čísla:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabské)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (rímske malé)',
        'page_numbers_format_roman_upper': 'I, II, III ... (rímske veľké)',
        'page_numbers_format_letter': 'A, B, C ... (písmená)',
        'page_numbers_format_custom': 'Vlastné',
        'page_numbers_custom_pattern': 'Vzor:',
        'page_numbers_custom_placeholder': 'napr. "Strana {nummer}" alebo "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Použite {nummer} pre aktuálne číslo strany a {total} pre celkový počet',
        'page_numbers_position': 'Pozícia:',
        'page_numbers_pos_tl': 'Hore vľavo',
        'page_numbers_pos_tc': 'Hore v strede',
        'page_numbers_pos_tr': 'Hore vpravo',
        'page_numbers_pos_ml': 'V strede vľavo',
        'page_numbers_pos_mc': 'Vycentrované',
        'page_numbers_pos_mr': 'V strede vpravo',
        'page_numbers_pos_bl': 'Dole vľavo',
        'page_numbers_pos_bc': 'Dole v strede',
        'page_numbers_pos_br': 'Dole vpravo',
        'page_numbers_margins': 'Okraje:',
        'page_numbers_margin_x': 'Horizontálna vzdialenosť:',
        'page_numbers_margin_y': 'Vertikálna vzdialenosť:',
        'page_numbers_range': 'Rozsah strán:',
        'page_numbers_all_pages': 'Všetky strany',
        'page_numbers_custom_range': 'Vlastný rozsah',
        'page_numbers_from': 'Od:',
        'page_numbers_to': 'Do:',
        'page_numbers_progress': 'Vkladanie čísel strán...',
        'page_numbers_start': 'Spúšťanie vkladania čísel strán...',
        'page_numbers_cancel': 'Vkladanie čísel strán zrušené',
        'page_numbers_success': 'Čísla strán boli úspešne pridané.\n\nChcete otvoriť nové PDF?\n\n{0}',
        'page_numbers_complete': 'Čísla strán boli pridané',
        'page_numbers_error_format': 'Chyba pri vkladaní čísel strán: {0}',
        'page_numbers_content_type': 'Typ obsahu:',
        'page_numbers_tab_simple': 'Jednoduché číslo',
        'page_numbers_tab_range': 'Strana X z Y',
        'page_numbers_tab_date': 'Dátum',
        'page_numbers_tab_custom': 'Voľný text',
        'page_numbers_range_format': 'Formát:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Strana {aktuell} z {gesamt}',
        'page_numbers_range_custom': 'Vlastné',
        'page_numbers_range_placeholder': 'napr. "Strana {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Formát dátumu:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. januára 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Vlastné',
        'page_numbers_date_placeholder': 'napr. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Pozícia:',
        'page_numbers_date_before': 'Dátum pred číslom strany',
        'page_numbers_date_after': 'Dátum za číslom strany',
        'page_numbers_date_only': 'Iba dátum (bez čísla strany)',
        'page_numbers_custom_text': 'Vlastný text:',
        'page_numbers_custom_placeholder_text': 'Použite {seite} pre číslo strany a {gesamt} pre celkový počet\nnapr. "Dôverné - Strana {seite}" alebo "{seite} z {gesamt}"',
        "filename_with_page_number":"_s_cislom_strany",
        "filename_with_page_declaration":"_s_oznacenim_strany",
        "filename_with_pagenumber":"_s_cislom_strany",
        "filename_with_date":"_s_datumom",
        "filename_with_my_page_declaration":"_s_vlastnym_oznacenim",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Neuložené zmeny",
        "unsaved_changes_message_darkmode": "Existujú neuložené vloženia.\nChcete ich uložiť pred prepnutím?",
        "save_and_switch": "Uložiť a prepnúť",
        "discard_and_switch": "Prepnúť teraz",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Exportovať strany ako obrázky',
        'export_images_menu': 'Exportovať ako obrázky (PNG/JPEG)',
        'export_images_format': 'Formát obrázka:',
        'export_images_dpi': 'Rozlíšenie (DPI):',
        'export_images_quality': 'Kvalita JPEG:',
        'export_images_range': 'Rozsah strán:',
        'export_images_all_pages': 'Všetky strany',
        'export_images_custom_range': 'Vlastný rozsah',
        'export_images_from': 'Od:',
        'export_images_to': 'Do:',
        'export_images_options': 'Možnosti:',
        'export_images_single_files': 'Každá strana ako samostatný súbor',
        'export_images_subfolder': 'Exportovať do podpriečinka',
        'export_images_subfolder_info': 'Do podpriečinka "nazovPDF_obrazky"',
        'export_images_same_folder': 'V rovnakom priečinku ako PDF',
        'export_images_apply_darkmode': 'Použiť nastavenia PDFDarkView (Tmavý režim)',
        'export_images_target_folder': 'Cieľový priečinok:',
        'export_images_browse': 'Prehľadávať...',
        'export_images_preview': 'Náhľad:',
        'export_images_preview_info': 'Vyberte nastavenia pre export',
        'export_images_preview_info_detail': '{0} strán ako {1}\nRozlíšenie: {2} DPI\nNázov súboru: {3}\n{4}',
        'export_images_select_folder': 'Vyberte cieľový priečinok',
        'export_images_start': 'Spúšťanie exportu obrázkov...',
        'export_images_progress': 'Exportovanie obrázkov...',
        'export_images_saving': 'Ukladanie strany {0} z {1}...',
        'export_images_success': 'Export úspešný!\n\n{0} obrázkov bolo uložených do:\n{1}',
        'export_images_complete': 'Export obrázkov dokončený',
        'export_images_open_folder': '📁 Otvoriť priečinok',
        'export_images_cancel': 'Export obrázkov zrušený',
        'export_images_error_format': 'Chyba pri exportovaní obrázkov: {0}',
        'export_images_pdf2image_missing': 'Knižnica "pdf2image" nie je nainštalovaná.\n\nNainštalujte ju pomocou:\npip install pdf2image\n\nPre Windows potrebujete aj Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konverzia pre dlhodobé archivovanie',
        'pdfa_menu': 'PDF/A konverzia (vhodné pre archív)',
        'pdfa_info': 'Konvertuje PDF do formátu PDF/A.\n\nPDF/A je špeciálne vyvinutý pre dlhodobé archivovanie a zaisťuje, že dokument bude v budúcnosti správne zobrazený.',
        'pdfa_standard': 'PDF/A štandard:',
        'pdfa_standard_select': 'Verzia:',
        'pdfa_1': 'PDF/A-1 (jednoduchý, široko kompatibilný)',
        'pdfa_2': 'PDF/A-2 (moderný, lepšia kompresia)',
        'pdfa_3': 'PDF/A-3 (najnovšia verzia, povoľuje prílohy)',
        'pdfa_standards_explanation': '📖 Vysvetlenie štandardov:\n\n'
            '• PDF/A-1: Základný, kompatibilný so staršími systémami (cca 2005)\n'
            '• PDF/A-2: Modernejší, lepšia kompresia, podpora priehľadnosti (cca 2011)\n'
            '• PDF/A-3: Najnovšia verzia, povoľuje vkladanie príloh (cca 2013)\n\n'
            'Odporúčanie: PDF/A-2 je dobrý kompromis medzi kompatibilitou a modernými funkciami.',
        'pdfa_options': 'Možnosti:',
        'pdfa_compress_enable': 'Komprimovať PDF (menší súbor)',
        'pdfa_metadata_preserve': 'Zachovať metadáta (názov, autor, atď.)',
        'pdfa_target_folder': 'Cieľový priečinok:',
        'pdfa_browse': 'Prehľadávať...',
        'pdfa_select_folder': 'Vyberte cieľový priečinok',
        'pdfa_ocr_info_unknown': '🔍 Nepodarilo sa skontrolovať textový obsah.',
        'pdfa_ocr_info_not_needed': '✅ Text dostupný - OCR nie je potrebné.\nPDF/A možno vytvoriť priamo.',
        'pdfa_ocr_info_recommended': '⚠️ Nenašiel sa dostatočný text.\n\nPre vyhľadávateľné PDF odporúčame najprv spustiť OCR.\nPoznámka: PDF/A funguje aj bez OCR - ale text nebude vyhľadávateľný.',
        'pdfa_ocr_info_error': '❌ Chyba pri kontrole: {0}',
        'pdfa_start': 'Spúšťanie PDF/A konverzie...',
        'pdfa_progress': 'PDF/A konverzia prebieha...',
        'pdfa_success': 'PDF/A konverzia úspešná!\n\nUložené ako:\n{0}\n\nChcete otvoriť nové PDF?',
        'pdfa_complete': 'PDF/A konverzia dokončená',
        'pdfa_cancel': 'PDF/A konverzia zrušená',
        'pdfa_error_format': 'Chyba pri PDF/A konverzii:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Knižnica "ocrmypdf" nie je nainštalovaná.\n\nNainštalujte ju pomocou:\npip install ocrmypdf',
        'btn_convert': 'Konvertovať',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimalizovať PDF (zmenšiť veľkosť súboru)',
        'optimize_menu': 'Optimalizovať PDF (veľkosť súboru)',
        'optimize_info': 'Zmenšuje veľkosť PDF súboru pomocou rôznych optimalizačných metód.\n\nČím vyššia úroveň kompresie, tým menší súbor - s možnou stratou kvality obrázkov.',
        'optimize_level': 'Úroveň kompresie:',
        'optimize_level_low': 'Nízka (rýchle, malá úspora)',
        'optimize_level_medium': 'Stredná (dobrý kompromis)',
        'optimize_level_high': 'Vysoká (veľká úspora)',
        'optimize_level_maximum': 'Maximálna (maximálna úspora, pomalé)',
        'optimize_level_explanation': 'Odporúčanie: "Stredná" je dobrý kompromis medzi rýchlosťou a veľkosťou súboru.',
        'optimize_options': 'Možnosti:',
        'optimize_compress_images': 'Komprimovať obrázky (znížiť kvalitu JPEG)',
        'optimize_clean_objects': 'Odstrániť nepoužívané objekty',
        'optimize_preserve_metadata': 'Zachovať metadáta (názov, autor, atď.)',
        'optimize_image_quality': 'Kvalita obrázka:',
        'optimize_range': 'Rozsah strán:',
        'optimize_all_pages': 'Všetky strany',
        'optimize_custom_range': 'Vlastný rozsah',
        'optimize_from': 'Od:',
        'optimize_to': 'Do:',
        'optimize_target_folder': 'Cieľový priečinok:',
        'optimize_browse': 'Prehľadávať...',
        'optimize_select_folder': 'Vyberte cieľový priečinok',
        'optimize_info_box': 'Informácia',
        'optimize_info_text': 'Optimalizácia môže pri veľkých PDF trvať niekoľko minút.\n\nObrázky sa ukladajú so zníženou kvalitou, čo môže výrazne zmenšiť veľkosť súboru.',
        'optimize_start': 'Spúšťanie PDF optimalizácie...',
        'optimize_progress': 'Optimalizácia PDF...',
        'optimize_cancel': 'PDF optimalizácia zrušená',
        'optimize_complete': 'PDF optimalizácia dokončená',
        'optimize_error_format': 'Chyba pri PDF optimalizácii:\n\n{0}',
        'optimize_success_message': 'PDF optimalizácia úspešná!\n\nUložené ako:\n{0}\n\nPredtým: {1}\nPotom: {2}\nÚspora: {3:.1f}%\n\n{4}\n\nChcete otvoriť optimalizované PDF?',
        'optimize_success_message_no_size': 'PDF optimalizácia úspešná!\n\nUložené ako:\n{0}\n\nInformácia o veľkosti nie je k dispozícii.\n\nChcete otvoriť optimalizované PDF?',
        'optimize_result_positive': 'Súbor bol zmenšený o {0:.1f}%.',
        'optimize_result_zero': 'Žiadna zmena veľkosti súboru.',
        'optimize_result_negative': 'Súbor sa zväčšil o {0:.1f}%.\nOptimalizácia bola preskočená, pôvodný súbor bol zachovaný.',
        'btn_optimize': 'Spustiť optimalizáciu',
        'filename_optimize_low_suffix': '_optimalizovane_nizke',
        'filename_optimize_medium_suffix': '_optimalizovane',
        'filename_optimize_high_suffix': '_optimalizovane_vysoke',
        'filename_optimize_maximum_suffix': '_optimalizovane_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Orezať PDF',
        'crop_menu': 'Orezať PDF (Crop)',
        'crop_range': 'Použiť na:',
        'crop_all_pages': 'Všetky strany',
        'crop_current_page': 'Iba aktuálna strana',
        'crop_values': 'Hodnoty orezania (v bodoch):',
        'crop_left': 'Vľavo:',
        'crop_right': 'Vpravo:',
        'crop_top': 'Hore:',
        'crop_bottom': 'Dole:',
        'crop_presets': 'Predvoľby:',
        'crop_preset_white': 'Detekovať biele okraje',
        'crop_reset': 'Resetovať',
        'crop_mouse_hint': '🖱️ Pretiahnite obdĺžnik pre hrubý výber oblasti.\nPotom môžete presne upraviť hodnoty v SpinBoxoch.\nManuálna úprava myšou nie je možná.',
        'crop_apply': 'Orezať',
        'crop_scope_all': 'Všetky strany',
        'crop_scope_current': 'Aktuálna strana',
        'crop_new_size': 'Nová veľkosť: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Nie je načítané žiadne PDF',
        'crop_preview_error': 'Chyba pri načítaní náhľadu',
        'crop_start': 'Spúšťanie orezania...',
        'crop_progress': 'Orezávanie PDF...',
        'crop_success': 'PDF úspešne orezané!\n\nUložené ako:\n{0}\n\nChcete otvoriť orezané PDF?',
        'crop_complete': 'Orezanie dokončené',
        'crop_cancel': 'Orezanie zrušené',
        'crop_error_format': 'Chyba pri orezávaní:\n\n{0}',
        'filename_crop_suffix': '_orezane',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Sploštenie PDF (Flatten)',
        'flatten_menu': 'Sploštenie PDF (Flatten)',
        'flatten_info': 'Sploštenie PDF "vypáli" všetky upraviteľné prvky do obsahu strany.\n\nPotom už nie je možné jednotlivo upravovať polia formulárov, anotácie, texty, krížiky, podpisy, obrázky a tvary.',
        'flatten_explanation_title': '📖 Na čo je to dobré?',
        'flatten_explanation_text': 'Sploštenie je potrebné v nasledujúcich situáciách:\n\n'
            '• 📄 Chcete pripraviť dokument na tlač\n'
            '• 🔒 Chcete zabrániť zmenám polí formulárov\n'
            '• 📎 Chcete "trvalo" vložiť anotácie a komentáre do dokumentu\n'
            '• 🖼️ Chcete trvalo ukotviť vložené texty, krížiky, podpisy, obrázky a tvary v dokumente\n'
            '• 📦 Chcete pripraviť súbor na archiváciu\n\n'
            'Sploštenie zmenšuje PDF a zabraňuje náhodnému presúvaniu alebo mazaniu prvkov.',
        'flatten_what_title': 'Čo sa splošťuje?',
        'flatten_what_list': '• ✅ Polia formulárov (textové polia, zaškrtávacie polia, tlačidlá)\n'
            '• ✅ Anotácie (komentáre, zvýraznenia, poznámky)\n'
            '• ✅ Prekryvy (texty, krížiky, podpisy, obrázky, tvary)',
        'flatten_options': 'Možnosti:',
        'flatten_forms': 'Sploštiť polia formulárov',
        'flatten_annotations': 'Sploštiť anotácie',
        'flatten_overlays': 'Sploštiť prekryvy (texty, krížiky, podpisy, obrázky, tvary)',
        'flatten_target_folder': 'Cieľový priečinok:',
        'flatten_browse': 'Prehľadávať...',
        'flatten_select_folder': 'Vyberte cieľový priečinok',
        'flatten_warning': '⚠️ Dôležité: Sploštenie je nezvratný proces!\n\nPo sploštení už nemožno upraviteľné prvky jednotlivo meniť ani mazať.\nV prípade potreby si vopred vytvorte zálohu.',
        'flatten_apply': 'Sploštiť',
        'flatten_start': 'Spúšťanie sploštenia...',
        'flatten_progress': 'Splošťovanie PDF...',
        'flatten_success': 'PDF úspešne sploštené!\n\nUložené ako:\n{0}\n\nChcete otvoriť sploštené PDF?',
        'flatten_complete': 'Sploštenie dokončené',
        'flatten_cancel': 'Sploštenie zrušené',
        'flatten_error_format': 'Chyba pri splošťovaní:\n\n{0}',
        'filename_flatten_suffix': '_splostene',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Prekrytie PDF (Overlay)',
        'overlay_menu': 'Prekrytie PDF (Overlay)',
        'overlay_info': 'Umiestňuje jeden PDF (prekryv) cez iný PDF.\n\nPrekryvné PDF sa umiestni na základné PDF. To je užitočné pre vodoznaky, logá, hlavičkové papiere alebo pečiatky.',
        'overlay_explanation_title': '📖 Na čo je to dobré?',
        'overlay_explanation_text': 'Prekrytie je potrebné v nasledujúcich situáciách:\n\n'
            '• 🏢 Umiestnenie loga spoločnosti ako vodoznaku na každú stranu\n'
            '• 📄 Umiestnenie hlavičkového papiera na prázdne PDF\n'
            '• 🖊️ Umiestnenie prekryvu pečiatky na dokument\n'
            '• 🔖 Umiestnenie vodoznaku na všetky strany\n'
            '• 📑 Umiestnenie prekryvu formulára na šablónu',
        'overlay_type': 'Typ prekrytia:',
        'overlay_type_fullpage': 'Celá strana (krycí)',
        'overlay_type_transparent': 'Celá strana (priehľadný - odporúčané)',
        'overlay_type_stamp': 'Pečiatka (polohovateľná)',
        'overlay_type_info_fullpage': '📄 Prekryvné PDF sa umiestni presne cez celú stranu.\nBiely pozadie možno odstrániť tak, že zostane viditeľný iba obsah.',
        'overlay_type_info_transparent': '🔍 Prekryvné PDF sa umiestni cez celú stranu s priehľadným pozadím.\nBiele pozadie sa automaticky odstráni - ideálne pre vodoznaky a logá!',
        'overlay_type_info_stamp': '🖊️ Prekryvné PDF sa umiestni a prispôsobí ako pečiatka.\nPerfektné pre logá, pečiatky alebo podpisy na určitých pozíciách.',
        'overlay_remove_background': 'Odstrániť biele pozadie:',
        'overlay_remove_background_enable': 'Odstrániť biele pozadie z prekryvného PDF (urobí prekryv priehľadným)',
        'overlay_remove_background_tooltip': 'Odstraňuje biele oblasti z prekryvného PDF, aby bol spodný text viditeľný.',
        'overlay_threshold': 'Prahová hodnota:',
        'overlay_threshold_hint': '(1-254, vyššia = viac bieleho sa odstráni)',
        'overlay_select_file': 'Vyberte prekryvné PDF:',
        'overlay_file_placeholder': 'Prosím, vyberte PDF súbor pre prekrytie',
        'overlay_browse': 'Prehľadávať...',
        'overlay_select_overlay': 'Vyberte prekryvné PDF',
        'overlay_range': 'Rozsah strán:',
        'overlay_all_pages': 'Všetky strany',
        'overlay_custom_range': 'Vlastný rozsah',
        'overlay_from': 'Od:',
        'overlay_to': 'Do:',
        'overlay_position': 'Pozícia:',
        'overlay_position_center': 'Stred',
        'overlay_position_top_left': 'Hore vľavo',
        'overlay_position_top_right': 'Hore vpravo',
        'overlay_position_bottom_left': 'Dole vľavo',
        'overlay_position_bottom_right': 'Dole vpravo',
        'overlay_size': 'Veľkosť:',
        'overlay_size_original': 'Pôvodná veľkosť',
        'overlay_size_fit_page': 'Prispôsobiť stránke',
        'overlay_size_custom': 'Vlastné (%)',
        'overlay_opacity': 'Priehľadnosť:',
        'overlay_target_folder': 'Cieľový priečinok:',
        'overlay_browse_folder': 'Prehľadávať...',
        'overlay_select_folder': 'Vyberte cieľový priečinok',
        'overlay_warning': '⚠️ Poznámka: Prekryvné PDF sa umiestni na základné PDF a "vypáli" sa do neho.\n\nPrvky prekryvného PDF už po uložení nemožno jednotlivo upravovať.',
        'overlay_apply': 'Prekryť',
        'overlay_start': 'Spúšťanie prekrytia...',
        'overlay_progress': 'Prekrývanie PDF...',
        'overlay_success': 'PDF úspešne prekryté!\n\nUložené ako:\n{0}\n\nChcete otvoriť prekryté PDF?',
        'overlay_complete': 'Prekrytie dokončené',
        'overlay_cancel': 'Prekrytie zrušené',
        'overlay_error_format': 'Chyba pri prekrývaní:\n\n{0}',
        'overlay_no_file': 'Nebolo vybrané žiadne prekryvné PDF.\n\nProsím, vyberte PDF súbor pre prekrytie.',
        'filename_overlay_suffix': '_prekryte',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extrahovať obrázky z PDF',
        'extract_images_menu': 'Extrahovať všetky obrázky',
        'extract_images_info': 'Extrahuje všetky obrázky z PDF a uloží ich ako samostatné súbory.\n\nObrázky sa ukladajú v pôvodnom formáte alebo sa konvertujú do vybraného formátu.',
        'extract_images_format': 'Formát obrázka:',
        'extract_images_quality': 'Kvalita JPEG:',
        'extract_images_options': 'Možnosti:',
        'extract_images_subfolder': 'Extrahovať do podpriečinka ("nazovPDF_obrazky")',
        'extract_images_unique': 'Iba unikátne obrázky (zabrániť duplicitám)',
        'extract_images_range': 'Rozsah strán:',
        'extract_images_all_pages': 'Všetky strany',
        'extract_images_custom_range': 'Vlastný rozsah',
        'extract_images_from': 'Od:',
        'extract_images_to': 'Do:',
        'extract_images_target_folder': 'Cieľový priečinok:',
        'extract_images_browse': 'Prehľadávať...',
        'extract_images_select_folder': 'Vyberte cieľový priečinok',
        'extract_images_info_box': 'Informácia',
        'extract_images_info_text': 'Extrakcia môže pri veľkých PDF trvať niekoľko minút.\n\nObrázky sa ukladajú s pôvodným názvom (strana_obrazok).',
        'extract_images_extract': 'Extrahovať',
        'extract_images_start': 'Spúšťanie extrakcie...',
        'extract_images_progress': 'Extrahovanie obrázkov...',
        'extract_images_success': '✅ Obrázky úspešne extrahované!\n\n{0} obrázkov bolo uložených do:\n{1}',
        'extract_images_complete': 'Extrakcia obrázkov dokončená',
        'extract_images_cancel': 'Extrakcia zrušená',
        'extract_images_error_format': 'Chyba pri extrahovaní obrázkov:\n\n{0}',
        'extract_images_open_folder': '📁 Otvoriť priečinok',
        'extract_images_no_images': 'V PDF neboli nájdené žiadne obrázky.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Viac strán na jednej strane (N-Up)',
        'nup_menu': 'Viac strán na jednej strane (N-Up)',
        'nup_info': 'Usporiada viacero PDF strán na jednej strane.\n\nIdeálne pre kompaktné tlače, prehľady alebo handouty.',
        'nup_layout': 'Rozloženie:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Náhľad:',
        'nup_preview_info': '{0} strán → {1} strán na list → {2} listov\nRozloženie: {3}',
        'nup_order': 'Poradie:',
        'nup_order_horizontal': 'Horizontálne (riadok po riadku)',
        'nup_order_vertical': 'Vertikálne (stĺpec po stĺpci)',
        'nup_order_horizontal_reverse': 'Horizontálne obrátene',
        'nup_order_vertical_reverse': 'Vertikálne obrátene',
        'nup_range': 'Rozsah strán:',
        'nup_all_pages': 'Všetky strany',
        'nup_custom_range': 'Vlastný rozsah',
        'nup_from': 'Od:',
        'nup_to': 'Do:',
        'nup_options': 'Možnosti:',
        'nup_margins': 'Okraje:',
        'nup_margin_between': 'Medzera medzi stranami:',
        'nup_page_numbers': 'Vložiť čísla strán',
        'nup_target_folder': 'Cieľový priečinok:',
        'nup_browse': 'Prehľadávať...',
        'nup_select_folder': 'Vyberte cieľový priečinok',
        'nup_create': 'Vytvoriť',
        'nup_start': 'Spúšťanie N-Up...',
        'nup_progress': 'Vytváranie N-Up...',
        'nup_success': 'N-Up úspešne vytvorené!\n\nUložené ako:\n{0}\n\nChcete otvoriť nové PDF?',
        'nup_complete': 'N-Up dokončené',
        'nup_cancel': 'N-Up zrušené',
        'nup_error_format': 'Chyba pri N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Zmeniť veľkosť strany',
        'pagesize_menu': 'Zmeniť veľkosť strany',
        'pagesize_info': 'Mení veľkosť strany PDF.\n\nObsah sa automaticky prispôsobí novej veľkosti.',
        'pagesize_format': 'Formát:',
        'pagesize_select': 'Vyberte štandardný formát:',
        'pagesize_custom': 'Vlastná veľkosť:',
        'pagesize_width': 'Šírka:',
        'pagesize_height': 'Výška:',
        'pagesize_orientation': 'Orientácia:',
        'pagesize_portrait': 'Na výšku',
        'pagesize_landscape': 'Na šírku',
        'pagesize_scale_options': 'Možnosti škálovania:',
        'pagesize_fit': 'Prispôsobiť (zachovať pomer strán)',
        'pagesize_stretch': 'Natiahnuť (deformovať)',
        'pagesize_center': 'Vycentrovať (pôvodná veľkosť)',
        'pagesize_range': 'Rozsah strán:',
        'pagesize_all_pages': 'Všetky strany',
        'pagesize_custom_range': 'Vlastný rozsah',
        'pagesize_from': 'Od:',
        'pagesize_to': 'Do:',
        'pagesize_target_folder': 'Cieľový priečinok:',
        'pagesize_browse': 'Prehľadávať...',
        'pagesize_select_folder': 'Vyberte cieľový priečinok',
        'pagesize_apply': 'Použiť',
        'pagesize_start': 'Spúšťanie zmeny veľkosti strany...',
        'pagesize_progress': 'Zmena veľkosti strany...',
        'pagesize_success': 'Veľkosť strany úspešne zmenená!\n\nUložené ako:\n{0}\n\nChcete otvoriť nové PDF?',
        'pagesize_complete': 'Zmena veľkosti strany dokončená',
        'pagesize_cancel': 'Zmena veľkosti strany zrušená',
        'pagesize_error_format': 'Chyba pri zmene veľkosti strany:\n\n{0}',
        'pagesize_preview_info': 'Nová veľkosť: {0} x {1} pt',
        'filename_pagesize_suffix': '_nova_velkost',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informácie o PDF',
        'pdf_info_menu': 'Zobraziť informácie o PDF',
        'pdf_info_voice': 'Zobrazujú sa informácie o PDF',
        'pdf_info_error': 'Chyba pri zobrazovaní informácií o PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Zobraziť klávesové skratky",
        "shortcuts_dialog_title": "Klávesové skratky",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 SÚBOR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Otvoriť PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Zavrieť PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Uložiť ako...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Ochrana dokumentu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Tlač</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Tlačiť okamžite (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Ukončiť aplikáciu</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exportovať ako Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exportovať ako DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exportovať ako TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exportovať ako obrázky (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extrahovať obrázky</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ SPRACOVANIE DOKUMENTOV</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Viac strán)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konverzia (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Sploštiť PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Prekrytie PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimalizovať PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ ÚPRAVY</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Hľadať</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Pridať záložku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Správa záložiek</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Ďalšia záložka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Predchádzajúca záložka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Spustiť OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SPRÁVA STRÁN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Otočiť aktuálnu stranu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Otočiť všetky strany</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizovať aktuálnu stranu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizovať všetky strany</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Zmazať strany</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extrahovať strany</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Vložiť strany</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Presunúť strany</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Zlúčiť PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Zmeniť veľkosť strany</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 VLOŽENIE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Vložiť text</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Vložiť krížik</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Vložiť podpis 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Vložiť podpis 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Vložiť obrázok</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Vložiť obdĺžnik</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Vložiť elipsu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Vložiť čiaru</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Vložiť šípku</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Vložiť čísla strán</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Textový vodoznak</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Obrázkový vodoznak</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDAKCIE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redakcia (čierna)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redakcia (biela)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Použiť všetky redakcie</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ POKROČILÉ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Orezať PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Upraviť metadáta</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ ZOBRAZENIE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Prepnúť Tmavý/Svetlý režim</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Zobraziť textové okno</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Šírka strany (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dve strany (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Prehľad (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ NASTAVENIA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Správa hesiel</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR nastavenia</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Nastavenia podpisu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formátovanie názvov súborov</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Exportovať nastavenia</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importovať nastavenia</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMÁCIE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Zobraziť informácie o PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Zapnúť/vypnúť hlasový výstup</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Zamerať lištu ponúk</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Nová verzia je k dispozícii",
        "update_available_message": "Je k dispozícii nová verzia <b>{0}</b>.\n\nNavštívte stránku vydania a stiahnite si aktualizáciu:\n{1}",
        "update_available_voice": "Nová verzia {0} je k dispozícii. Stiahnite si aktualizáciu zo stránky GitHub.",
        "update_open_release": "Otvoriť stránku vydania",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Stiahnuť všetky preklady",
        "ask_download_all_translations": """Okrem nemčiny, angličtiny a vietnamčiny je k dispozícii ďalších {total_languages} GUI jazykov.\n\nMajú byť poskytnuté / aktualizované?\n\nPoznámka:\nNepotrebné jazyky môžete neskôr manuálne vymazať v adresári:\n{translations_path}
        \nAk zrušíte, môžete GUI jazyky neskôr stiahnuť pomocou ponuky 'Nástroje → Aktualizovať preklady'.""",
        "menu_update_translations": "Aktualizovať preklady",
        "translations_updated": "Preklady aktualizované",
        "translations_update_success": "{} prekladov bolo úspešne aktualizovaných ({} nových, {} aktualizovaných).",
        "translations_update_error": "Chyba pri aktualizácii prekladov",
        "translations_update_no_changes": "Všetky preklady sú už aktuálne.",
        "translations_update_offline": "Žiadne internetové pripojenie. Preklady sa nepodarilo aktualizovať.",
        "translations_update_in_progress": "Preklady sa aktualizujú na pozadí...",
        "translations_downloading": "Sťahovanie prekladov...",
        "translations_path_hint": "Používateľský adresár pre preklady",
        "translations_update_not_available_title": "Aktualizácia nie je k dispozícii",
        "translations_update_not_available_message": """Aktualizácia prekladov je k dispozícii iba v nainštalovanej verzii.\n\nVo vývojovom režime sú preklady už aktuálne.""",
        "translations_update_no_internet_title": "Žiadne internetové pripojenie",
        "translations_update_no_internet_message": """Nepodarilo sa nadviazať internetové pripojenie.\n\nPreklady nemožno stiahnuť z GitHubu.\n\nMožné riešenia:
        • Skontrolujte svoje internetové pripojenie
        • Dočasne vypnite prípadný firewall
        • Skúste to neskôr znova
        \nPreklady si môžete stiahnuť aj manuálne z GitHubu:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Aktualizácia už prebieha",
        "btn_retry": "Skúsiť znova",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Vitajte v PDF Dark View",
        "welcome_title_not_supported": "Vitajte v PDF Dark View",
        "welcome_message": "Vitajte v PDF Dark View!\n\nVáš systémový jazyk bol rozpoznaný ako '{language}'.\nChcete použiť tento jazyk pre používateľské rozhranie?\n\nJazyk môžete kedykoľvek zmeniť v 'Nastavenia → Jazyk'.",
        "welcome_message_language_not_available": "Vitajte v PDF Dark View!\n\nVáš systémový jazyk bol rozpoznaný ako '{language}'.\nTento jazyk zatiaľ nie je nainštalovaný.\n\nChcete teraz stiahnuť preklady pre {language} z GitHubu?\n\n(Jazyk sa potom automaticky použije pre používateľské rozhranie.)",
        "welcome_message_language_not_supported": "Vitajte v PDF Dark View!\n\nVáš systémový jazyk bol rozpoznaný ako '{language}'.\nBohužiaľ, pre tento jazyk zatiaľ neexistujú žiadne preklady.\n\nPoužívateľské rozhranie bude zobrazené v {fallback_language}.\n\nJazyk môžete kedykoľvek zmeniť v 'Nastavenia → Jazyk'.\nAk chcete, môžete sami prispieť prekladom pre svoj jazyk:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Áno, použiť systémový jazyk",
        "welcome_keep_english": "Nie, ponechať angličtinu",
        "welcome_download_language": "Áno, stiahnuť {language}",

        # ============================================
        # 107. NAPOSLEDY POUŽITÉ CESTY
        # ============================================

        'menu_recent': 'Naposledy použité',
        'menu_recent_dirs': 'Adresáre...',
        'menu_recent_files': 'Súbory...',
        'recent_manage': 'Spravovať...',
        'recent_enable_tracking': 'Ukladať naposledy použité cesty (súkromie)',
        'recent_enable_info': 'Vypnite túto možnosť, aby ste neukladali cesty',
        'recent_tracking_disabled': 'Sledovanie ciest je zakázané',
        'recent_enabled': 'povolené',
        'recent_disabled': 'zakázané',
        'recent_tracking_status': 'Sledovanie ciest {0}',
        'recent_dialog_title': 'Naposledy použité cesty',
        'recent_tab_directories': 'Adresáre',
        'recent_tab_files': 'Súbory',
        'recent_dirs_instruction': 'Dvojklikom otvorte dialógové okno súboru v adresári',
        'recent_files_instruction': 'Dvojklikom otvorte PDF priamo',
        'recent_no_directories': '(žiadne uložené adresáre)',
        'recent_no_files': '(žiadne uložené súbory)',
        'recent_default_current': '⭐ Predvolený: {0}',
        'recent_set_as_default': '⭐ Nastaviť ako predvolený',
        'recent_default_set_title': 'Predvolený adresár nastavený',
        'recent_default_set_message': 'Adresár "{0}" bol nastavený ako predvolený na otváranie PDF.',
        'recent_default_set_voice': 'Predvolený adresár bol nastavený',
        'recent_directory_not_found': 'Adresár sa nenašiel',
        'recent_file_not_found': 'Súbor sa nenašiel',
        'recent_remove_selected': 'Odstrániť',
        'recent_remove_title': 'Odstrániť cestu',
        'recent_remove_confirm': 'Naozaj chcete odstrániť cestu "{0}" zo zoznamu?',
        'recent_path_removed': 'Cesta bola odstránená',
        'recent_clear_all': 'Odstrániť všetky',
        'recent_clear_title': 'Odstrániť všetky cesty',
        'recent_clear_confirm_type': 'Naozaj chcete vymazať všetky {0}?',
        'recent_cleared': 'Zoznam bol vymazaný',
        'recent_path_not_found_title': 'Cesta sa nenašla',
        'recent_path_not_found_message': 'Cesta "{0}" už neexistuje.',
        'recent_open_file': 'Otvoriť súbor',
        'btn_open_recent': 'Otvoriť',
        'recent_open_file_question': 'Chcete otvoriť "{0}" ako PDF?',
        'recent_not_pdf': 'Vybratý súbor nie je PDF.',
        'recent_more_entries': 'Ďalšie položky...',
        'btn_remove': 'Odstrániť',
        'btn_clear': 'Vymazať všetky',
        'recent_context_open': 'Otvoriť',
        'recent_context_reveal': 'Zobraziť vo Finderi',
        'recent_context_set_default': '⭐ Nastaviť ako predvolený',
        'recent_context_open_terminal': '💻 Otvoriť terminál',
        'recent_context_file_info': 'Informácie o súbore',
        'recent_context_open_with_default': '📄 Otvoriť predvolenou aplikáciou',
        'recent_context_remove': 'Odstrániť zo zoznamu',
        'recent_context_clear_all': 'Odstrániť všetky',
        'recent_file_info_title': 'Informácie o súbore',
        'recent_file_info_name': 'Názov',
        'recent_file_info_path': 'Cesta',
        'recent_file_info_size': 'Veľkosť',
        'recent_file_info_modified': 'Zmenené',
        'recent_file_info_pages': 'Stránky',
        'recent_error_reveal': 'Chyba pri otváraní vo Finderi',
        'recent_error_terminal': 'Chyba pri otváraní terminálu',
        'recent_error_info': 'Chyba pri získavaní informácií o súbore',
        'open_user_data_folder': 'Zobraziť adresár používateľských údajov',

        # ============================================
        # 108. VYMAZANIE PÁRNYCH/NEPÁRNYCH STRÁN
        # ============================================
        "pages_delete_even": "Vymazať všetky párne stránky",
        "pages_delete_odd":  "Vymazať všetky nepárne stránky",
        "progress_even_pages": "Vymazávanie párnych stránok",
        "progress_odd_pages": "Vymazávanie nepárnych stránok",
        "progress_mark_delete_even": "{} párna(e) stránka(y) označená(e) na vymazanie",
        "progress_mark_delete_odd":  "{} nepárna(e) stránka(y) označená(e) na vymazanie",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Program sa ukončuje",

    }
