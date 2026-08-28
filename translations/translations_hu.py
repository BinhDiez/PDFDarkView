
# ============================================
# translations_hu.py - Magyar szótár
# Vollständig sortiert nach Kategorien
# ============================================

def load_hungarian_strings():
    """Lädt alle ungarischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF betöltése",
        'btn_text_window': "OCR szöveg",
        'btn_first': "Első oldal",
        'btn_prev': "Előző oldal",
        'btn_next': "Következő oldal",
        'btn_last': "Utolsó oldal",
        'btn_print': "Nyomtatás",
        'btn_darkmode_light': "Világos mód",
        'btn_darkmode_dark': "Sötét mód",
        'btn_delete_pages': "Oldalak törlése",
        'btn_extract_pages': "Oldalak kivonása",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Mégse",
        'btn_save': "Mentés",
        'btn_close': "Bezárás",
        'btn_delete': "Törlés",
        'btn_delete_all': "Összes törlése",
        'btn_copy': "Másolás",
        'btn_export': "Exportálás",
        'btn_show': "Jelszó megjelenítése",
        'btn_hide': "Jelszó elrejtése",
        'btn_authenticate': "Hitelesítés",
        'btn_settings': "Beállítások",
        'btn_protect': "Védelem",
        'btn_remove_password': "Jelszó eltávolítása",
        'btn_manage': "Jelszókezelés",
        'btn_retry': "Újrapróbálkozás",
        'btn_select_all': "Összes kijelölése",
        'btn_clear_selection': "Kijelölés megszüntetése",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "{0}. oldal / {1}",
        'page_count': "/ {0}",
        'goto_page': "Ugrás oldalra",
        'page_simple': "{0}. oldal",
        'full_view_page': "Teljes nézet, {0}. oldal",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Adja meg a keresett kifejezést + Enter",
        'search_results': "Találatok: {0} / {1}",
        'search_nav_hint': "Enter: következő (Shift+Enter: előző) találat",
        'search_no_results': "Nincs találat",
        'search_error': "Keresési hiba",
        'search_active': "Keresőmező aktiválva",
        'search_closed': "Keresés befejezve",
        'search_position': "{0}. oldal, {1}",
        'search_pos_top': "legfelül",
        'search_pos_upper': "fent",
        'search_pos_middle': "középen",
        'search_pos_lower': "lent",
        'search_pos_bottom': "legalul",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Szövegfelismerés sikeresen befejeződött!",
        'ocr_success_title': "OCR sikeres",
        'ocr_success_message': "A dokumentum mostantól kereshető.",
        'ocr_failed': "OCR sikertelen",
        'ocr_in_progress': "OCR folyamatban",
        'ocr_preparing': "PDF előkészítése...",
        'ocr_analyzing': "PDF elemzése...",
        'ocr_optimizing': "Képoptimalizálás...",
        'ocr_recognizing': "Szövegfelismerés...",
        'ocr_embedding': "Szöveg beágyazása...",
        'ocr_finalizing': "PDF véglegesítése...",
        'ocr_not_available': "OCR nem érhető el",
        'ocr_install_message': "Az OCR-eszközök nem találhatók.\n\nTelepítse a következőket:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR szükséges",
        'ocr_question': "A PDF nem tartalmaz kereshető szöveget.\nSzeretne OCR-t futtatni a {0} lehetővé tételéhez?",
        'ocr_perform': "OCR futtatása",
        'ocr_later': "Később",
        'ocr_starting': "Garantált OCR indítása...",
        'ocr_success_voice': "OCR sikeres. A PDF mostantól kereshető.",
        'ocr_partial_success': "Az OCR lefutott, de a csere során problémák merültek fel.\n\nA kereshető verzió ide lett mentve:\n{0}\n\nHiba: {1}",
        'ocr_partial_title': "OCR részben sikeres",
        'ocr_partial_voice': "OCR lefutott, de a csere sikertelen.",
        'original_file': "Eredeti fájl:",
        'old_size': "Régi méret:    {0} bájt",
        'new_size': "Új méret: {0} bájt",
        'size_change': "Változás: {0}{1} bájt",
        'backup_created_file': "Biztonsági másolat készült:\n{0}",
        'backup_not_created': "Nem készült biztonsági másolat (a beállítás ki van kapcsolva)",
        'page_header': "=== {0}. oldal ===\n{1}\n",
        'scanned_page_header': "=== {0}. oldal (szkennelt) ===\n[Ez az oldal csak szkennelt szöveget tartalmaz]\n[Kézzel futtasson OCR-t]\n",
        'scanned_warning': "⚠️ SZKENNELT SZÖVEG - OCR SZÜKSÉGES",
        'guaranteed_title': "Kereshető PDF létrehozva",
        'guaranteed_message': "<b>Garantált kereshető verzió létrehozva!</b>\n\nMivel az automatikus OCR sikertelen volt, egy alternatív kereshető PDF készült:\n\n{0}\n\n<b>Ez a fájl tartalmazza:</b>\n• A kinyert szöveget (ha volt)\n• Útmutatást a szkennelt oldalakhoz\n• Teljes mértékben kereshető",
        'guaranteed_voice': "Garantált kereshető PDF létrehozva.",
        'instruction_title': "OCR-ÚTMUTATÓ",
        'instruction_file': "Eredeti fájl: {0}",
        'instruction_text': "Az automatikus szövegfelismerés (OCR) sikertelen volt.\nKézzel futtasson OCR-t:\n\n1. OCRmyPDF-PARANCSOR:\n   ocrmypdf --force-ocr \"[FÁJL]\" \"kimenet.pdf\"\n\n2. ADOBE ACROBAT (macOS/Windows):\n   • Nyissa meg a PDF-et az Acrobatban\n   • Eszközök > PDF szerkesztése\n   • Válassza a 'Szövegfelismerés' lehetőséget\n\n3. PREVIEW (macOS):\n   • Nyissa meg a PDF-et az Előnézetben\n   • Fájl > Exportálás...\n   • Quartz-szűrő: 'Fájlméret csökkentése'\n   • Kapcsolja be az 'OCR futtatása' lehetőséget\n\n4. ONLINE OCR SZOLGÁLTATÁSOK:\n   • smallpdf.com/hu/ocr-pdf\n   • ilovepdf.com/hu/ocr-pdf\n   • adobe.com/hu/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR-útmutató létrehozva",
        'instruction_created_message': "Részletes útmutató készült:\n\n{0}\n\nKövesse a lépéseket a kézi OCR-hez.",
        'instruction_created_voice': "OCR-útmutató létrehozva.",
        'ocr_impossible': "OCR nem lehetséges",
        'ocr_impossible_message': "Az OCR nem futtatható.\n\nDolgozza fel a(z) '{0}' fájlt kézzel OCR-szoftverrel.",
        'ocr_impossible_voice': "OCR nem lehetséges. Dolgozza fel kézzel.",
        'emergency_title': "Vész-OCR",
        'emergency_message': "Vészhelyzeti PDF készült:\n\n{0}\n\nDolgozza fel ezt a fájlt kézzel OCR-rel.",
        'emergency_voice': "Vészhelyzeti PDF létrehozva. Futtasson OCR-t kézzel.",
        'critical_error': "Kritikus hiba",
        'critical_error_message': "Az OCR nem indítható el.\n\nIndítsa újra a programot, és ellenőrizze az OCR telepítését.",
        'critical_error_voice': "Kritikus OCR-hiba",
        'ocr_question_html': "<p>A PDF nem tartalmaz kereshető szöveget.<p>Szeretne OCR-t futtatni a <b>{0}</b> lehetővé tételéhez?</p>",
        'ocr_question_voice': "OCR szükséges. A PDF nem tartalmaz kereshető szöveget. Szeretne OCR-t futtatni a {0} lehetővé tételéhez?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "nincs PDF betöltve",
        'no_pdf_message': "Nincs PDF betöltve",
        'pdf_not_found': "A PDF-fájl nem található",
        'file_size': "Fájlméret",
        'bytes': "bájt",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Biztonsági másolat készült",
        'backup_disabled': "Biztonsági másolat kikapcsolva",
        'backup_activated': "Biztonsági másolat készítése bekapcsolva",
        'backup_deactivated': "Biztonsági másolat készítése kikapcsolva",
        'backup_status': "Biztonsági másolat: {0}",
        'backup_on': "✔ bekapcsolva",
        'backup_off': "✘ kikapcsolva",
        'close_pdf': "PDF bezárása: {0}",
        'pdf_not_found_format': "A PDF-fájl nem található: {0}",
        'error_pdf_load_format': "Hiba a PDF betöltésekor: {0}",
        'load_failed_format': "Betöltés sikertelen:\n{0}",
        'decrypted_suffix': "(visszafejtve)",
        'decryption_failed': "Visszafejtés sikertelen.",
        'decryption_error': "Hiba a visszafejtés során",
        'decryption_success': "Sikeres visszafejtés",
        'decryption_success_message': "A PDF visszafejtve és elmentve ide:\n\n{0}",
        'decryption_success_voice': "A PDF visszafejtve és elmentve.",
        'password_remove_error': "Hiba a jelszó eltávolításakor",
        'save_unencrypted': "Titkosítatlan PDF mentése másként",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Mentés másként...",
        'save_copy': "Másolat mentése",
        'save_success': "PDF elmentve ide: {0}",
        'save_encrypted': "Védett PDF elmentve ide: {0}",
        'save_error': "A PDF mentése nem sikerült",
        'encryption_question': "Szeretné jelszóval védeni a PDF-et?",
        'encryption_yes': "Igen",
        'encryption_no': "Nem",
        'encryption_cancel': "Mégse",
        'save_cancel': "Mentés megszakítva",
        'save_encrypted_voice': "Fájl titkosítva és elmentve.",
        'save_success_voice': "A PDF-fájl titkosítatlanul elmentve.",
        'save_error_format': "A PDF mentése nem sikerült:\n{0}",
        'export_pages_success': "Pages-exportálás sikeres",
        'export_pages_error': "Pages-exportálás sikertelen",
        'export_pages_error_format': "Pages-exportálás sikertelen: {0}",
        'export_word_success': "Word-exportálás sikeres",
        'export_word_error': "Word-exportálás sikertelen",
        'export_word_error_format': "Word-exportálás sikertelen: {0}",
        'export_text_success': "Szövegexportálás sikeres",
        'export_text_error': "Szövegexportálás sikertelen",
        'export_text_error_format': "Szövegexportálás sikertelen: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Jelszó szükséges",
        'password_enter': "Adja meg a jelszót",
        'password_confirm': "Jelszó megerősítése",
        'password_new': "Új jelszó",
        'password_current': "Aktuális jelszó",
        'password_save': "Jelszó mentése (titkosítva)",
        'password_saved': "✓ A fájlhoz tartozó jelszó elmentve",
        'password_wrong': "Hibás jelszó",
        'password_mismatch': "A jelszavak nem egyeznek",
        'password_too_short': "A jelszó túl rövid",
        'password_min_length': "A jelszónak legalább 4 karakter hosszúnak kell lennie",
        'password_strength': "Jelszó erőssége",
        'password_strength_very_weak': "Nagyon gyenge",
        'password_strength_weak': "Gyenge",
        'password_strength_medium': "Közepes",
        'password_strength_strong': "Erős",
        'password_strength_very_strong': "Nagyon erős",
        'password_char_count': "({0} karakter)",
        'password_match': "✓ Egyezik",
        'password_no_match': "✗ A jelszavak nem egyeznek",
        'password_show': "Mutat",
        'password_hide': "Elrejt",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Jelszókezelés",
        'password_table_filename': "Fájlnév",
        'password_table_password': "Jelszó",
        'password_count': "{0} elmentett jelszó",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Nincsenek elmentett jelszavak",
        'password_copied': "{0} jelszó kimásolva",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Biztosan törli a(z) '{0}' jelszavát?",
        'password_delete_multiple': "Biztosan törli a kiválasztott {0} jelszót?",
        'password_delete_all_confirm': "Biztosan törli az összes ({0}) elmentett jelszót?",
        'password_deleted': "{0} jelszó törölve",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Az összes jelszó törölve",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Jelszógenerátor",
        'generator_generated': "Generált jelszó:",
        'generator_regenerate': "Újragenerálás",
        'generator_copy': "Másolás",
        'generator_use': "Használat",
        'generator_settings': "Beállítások",
        'generator_length': "Hossz:",
        'generator_group_every': "Elválasztójel minden",
        'generator_group_chars': "karakter után.    Elválasztó:",
        'generator_uppercase': "Nagybetűk (A-Z)",
        'generator_lowercase': "Kisbetűk (a-z)",
        'generator_digits': "Számok (0-9)",
        'generator_symbols': "Speciális karakterek (!@#$%^&*)",
        'generator_exclude': "Kizárt:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Master jelszó szükséges",
        'master_password_setup': "Master jelszó beállítása",
        'master_password_change': "Master jelszó módosítása",
        'master_password_enter': "Adja meg a master jelszavát",
        'master_password_choose': "Válasszon erős master jelszót (legalább 8 karakter)",
        'master_password_new': "Adja meg az új master jelszavát",
        'master_password_confirm': "Jelszó megerősítése",
        'master_password_authenticate': "Hitelesítés",
        'master_password_success': "A master jelszó sikeresen beállítva.",
        'master_password_changed': "A master jelszó sikeresen módosítva.",
        'master_password_removed': "A master jelszó és az összes jelszó törölve.",
        'master_password_remove': "Master jelszó eltávolítása",
        'master_password_remove_confirm': "BIZTOS, hogy az ÖSSZES jelszót törölni szeretné?\n\nEz a művelet VISSZAVONHATATLAN!",
        'master_password_export_before': "Szeretne előtte biztonsági másolatot exportálni?",
        'master_password_export_delete': "Exportálás és törlés",
        'master_password_delete_now': "Azonnali törlés",
        'master_password_for_signatures': "Az aláírások használatához be kell állítania egy master jelszót.\n\nSzeretné most beállítani a master jelszót?",
        'master_password_for_private': "A privát szövegblokkok használatához be kell állítania egy master jelszót.\n\nSzeretné most beállítani a master jelszót?",
        'master_password_info': """
            <b>🔐 MASTER JELSZÓ NÉLKÜL:</b><br>
            • A jelszavak megjelenítése, másolása és exportálása nem lehetséges<br>
            • Jelszavak törlése mindig lehetséges (master jelszó nélkül is)<br><br>

            <b>🔐 MASTER JELSZÓVAL:</b><br>
            • Minden funkció elérhető hitelesítés után<br>
            • A jelszavak a master jelszóval lesznek titkosítva<br>
            • Minimális hossz: 8 karakter<br>
            • Biztonságos SHA-256 hash tárolás<br><br>

            <b>FONTOS:</b><br>
            • Ha elveszíti a master jelszót, a jelszavak nem állíthatók vissza<br>
            • A master jelszó eltávolításakor az ÖSSZES jelszó törlődik<br>
            • Törlés előtt exportálási lehetőség áll rendelkezésre<br>
            • A master jelszó bármikor módosítható
        """,
        'signature_auth_disabled': "Jelszókérés kikapcsolása az aláírásokhoz",
        'template_auth_disabled': "Jelszókérés kikapcsolása a privát szövegblokkokhoz",
        'master_password_for_signatures_settings': "Az aláírások használatához be kell állítania egy master jelszót.\n\nLépjen a Beállítások - Jelszókezelés menüpontba",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF védelme",
        'protect_info': "A(z) '{0}' fájl jelszóval lesz védve.",
        'protect_instruction': "Adja meg kétszer a kívánt jelszót a dokumentum védelméhez, vagy használja a beviteli mező mellett található jelszógenerátort.",
        'protect_success': "A PDF sikeresen védve és elmentve ide:\n{0}\n\nJelszó: {1}\n\nSzeretné most megnyitni a védett PDF-et?",
        'protect_open': "Igen",
        'protect_skip': "Nem",
        'protect_error': "Hiba a PDF védelme során",
        'protect_open_title': "védett PDF megnyitása",
        'protect_question': "Kész. Szeretné most megnyitni a védett PDF-et? Igen vagy Nem?",
        'password_cancel': "Jelszó párbeszédablak megszakítva",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Oldalak törlése",
        'pages_extract': "Oldalak kivonása",
        'pages_insert': "Oldalak beszúrása",
        'pages_move': "Oldalak áthelyezése",
        'pages_delete_options': "Törlési opciók",
        'pages_delete_empty': "Összes üres oldal törlése",
        'pages_delete_current': "Aktuális oldal törlése",
        'pages_delete_range': "Oldaltartomány törlése",
        'pages_extract_options': "Kivonási opciók",
        'pages_extract_current': "Aktuális oldal kivonása",
        'pages_extract_range': "Oldaltartomány kivonása",
        'pages_insert_position': "Beszúrás helye",
        'pages_insert_before': "Beszúrás az oldal elé:",
        'pages_insert_select': "PDF kiválasztása",
        'pages_insert_none': "Nincs PDF kiválasztva",
        'pages_move_source': "Áthelyezendő oldalak",
        'pages_move_from': "Oldaltól:",
        'pages_move_to': "Oldalig:",
        'pages_move_target': "Célhely",
        'pages_move_before': "Áthelyezés az oldal elé:",
        'pages_move_hint': "Megjegyzés: 1. oldal = eleje, {0} = vége",
        'pages_range_invalid': "A kezdőoldalnak kisebbnek vagy egyenlőnek kell lennie a végoldallal.",
        'pages_position_invalid': "A célhely nem lehet az áthelyezendő tartományon belül.",
        'pages_no_pdf_selected': "Nincs PDF kiválasztva.",
        'pages_deleted': "{0} oldal törölve.",
        'pages_extracted': "Kivonva: {0}\nElmentve ide: {1}\nFájlméret: {2:.1f} KB",
        'pages_inserted': "{0} oldal beszúrva",
        'pages_moved': "{0} oldal áthelyezve.",
        'pages_deleted_none': "Nem lett oldal törölve.",
        'pages_delete_progress': "Oldalak törlése...",
        'pages_deleted_with_backup': "{0} oldal törölve.\n\nBiztonsági másolat: {1}",
        'pages_deleted_voice': "Biztonsági másolat készült és {0} oldal törölve.",
        'info': "Információ",
        'error_dialog_creation': "A párbeszédablak nem hozható létre",
        'extract_page_single': "{0}. oldal kivonása",
        'extract_page_range': "{0}-{1}. oldalak kivonása",
        'extract_success_voice': "Oldalak sikeresen kivonva",
        'extract_error_format': "Hiba a kivonás során: {0}",
        'pages_inserted_voice': "{0} oldal beszúrva.",
        'insert_error_format': "Hiba a beszúrás során: {0}",
        'pages_move_progress': "Oldalak áthelyezése...",
        'pages_moved_with_backup': "{0} oldal áthelyezve.\n\nBiztonsági másolat: {1}",
        'move_success_title': "Sikeres áthelyezés",
        'pages_moved_voice': "{0} oldal sikeresen áthelyezve",
        'mark_removed': "A(z) {0}. oldal jelölése eltávolítva",
        'mark_empty': "A(z) {0}. oldal üresnek jelölve",
        'mark_export_removed': "A(z) {0}. oldal exportjelölése eltávolítva",
        'mark_export': "A(z) {0}. oldal exportra jelölve",
        'no_empty_pages': "Nincsenek üres oldalak törlésre jelölve",
        'delete_empty_confirm': "Szeretné törölni az összes ({0}) megjelölt üres oldalt?",
        'delete_empty_confirm_voice': "Törölje most az összes ({0}) megjelölt üres oldalt? Igen vagy Nem.",
        'empty_pages_deleted': "{0} üres oldal törölve",
        'no_export_pages': "Nincsenek exportra jelölt oldalak",
        'overwrite_title': "Meglévő fájl felülírása",
        'overwrite_question': "A(z)\n\n{0}\n\nfájl már létezik.\nSzeretné felülírni?",
        'overwrite_voice': "Felülírja a már létező fájlt? Igen vagy Nem.",
        'page_skipped': "A(z) {0}. oldal kihagyva",
        'export_complete': "Exportálás befejezve.",
        'export_complete_voice': "Az exportálás befejeződött.",
        'no_pages_exported': "Nem lett oldal exportálva",
        'export_cancelled': "Exportálás megszakítva",
        'pages_exported': "{0} oldal exportálva ide: {1}",
        'export_page_title': "Oldal exportálása",
        'page_exported': "{0}. oldal exportálva ide: {1}",
        'export_error': "Hiba az exportálás során",
        'export_marked_title': "Megjelölt oldalak exportálása",
        'rotate_all_title': "összes oldal elforgatása",
        'rotate_all_question': "Szeretné az összes oldalt 90 fokkal jobbra forgatni?",
        'rotate_all_voice': "Szeretné az összes oldalt 90 fokkal jobbra forgatni? Igen vagy Nem?",
        'all_pages_rotated': "Minden oldal elforgatva",
        'page_rotated': "{0}. oldal elforgatva",
        'rotate_error': "Az oldal nem forgatható",
        'delete_page_confirm': "Szeretné törölni a(z) {0}. oldalt?",
        'delete_page_confirm_voice': "Biztosan törölni szeretné a(z) {0}. oldalt? Igen vagy Nem.",
        'page_deleted': "{0}. oldal törölve",
        'delete_error': "Az oldal nem törölhető",
        'pages_deleted_voice': "{0} oldal törölve",
        'pages_exported_split': "{0} oldal sikeresen exportálva.",
        'pages_skipped': "{0} oldal kihagyva.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Oldalak kivonása (bővített)",
        'pdf_splitter_title': "PDF osztó és kivonó",
        'pdf_splitter_load': " PDF-fájl kiválasztása",
        'pdf_splitter_info': "Válasszon egy lehetőséget a PDF-dokumentumhoz",
        'pdf_splitter_basic': "Alapvető műveletek",
        'pdf_splitter_single': "Felosztás egyes oldalakra",
        'pdf_splitter_range': "Oldalak kivonása:",
        'pdf_splitter_range_placeholder': "pl. 1-3,5,7-9",
        'pdf_splitter_clean': "Tisztítási műveletek",
        'pdf_splitter_remove_empty': "Összes üres oldal eltávolítása",
        'pdf_splitter_remove': "Oldaltartomány törlése:",
        'pdf_splitter_remove_placeholder': "pl. 2,4-6",
        'pdf_splitter_process': "PDF feldolgozása",
        'pdf_splitter_loaded': "PDF betöltve. Válasszon egy lehetőséget",
        'pdf_read_error': "A PDF nem olvasható",
        'pages': "Oldalak",
        'pages_created': "Oldalak létrehozva",
        'range_empty': "Adjon meg egy oldaltartományt",
        'range_invalid': "Érvénytelen oldaltartomány",
        'range_created': "Új PDF készült a kiválasztott oldalakkal:\n{0}",
        'empty_removed': "{0} üres oldal eltávolítva.\nKimenet: {1}",
        'remove_empty': "Adja meg az eltávolítandó oldalakat",
        'remove_invalid': "Érvénytelen oldalak az eltávolításhoz",
        'remove_done': "Tisztított PDF létrehozva:\n{0}",
        'open_folder': "Mappa megnyitása",
        'show_in_finder': "Megjelenítés a Finderben",
        'pdf_splitter_no_pdf': "Először töltsön be egy PDF-fájlt.",
        'process_error': "Hiba a PDF feldolgozása során",
        'pages_created_voice': "{0} oldal létrehozva",
        'range_created_voice': "PDF létrehozva a kiválasztott oldalakkal",
        'empty_removed_voice': "{0} üres oldal eltávolítva",
        'remove_done_voice': "Tisztított PDF létrehozva",
        'pdf_splitter_split_groups': "Minden összefüggő csoport külön fájlba",
        'range_created_single': "Új PDF létrehozva:\n{0}",
        'range_created_multiple': "{0} PDF-fájl létrehozva.",
        'range_created_voice_single': "Egy PDF létrehozva a kiválasztott oldalakkal",
        'range_created_voice_multiple': "{0} PDF-fájl létrehozva",
        'empty_removed_none_left': "Nincsenek megmaradt oldalak",
        'empty_removed_all_empty': "Minden oldal üresnek lett felismerve, így eltávolításra kerülne. Nem jött létre fájl.",
        'preview_single': "Előnézet: {0}",
        'preview_enter_range': "Adjon meg egy oldaltartományt.",
        'preview_invalid_range': "Érvénytelen oldaltartomány.",
        'preview_file': "Előnézet: {0}",
        'preview_files': "Előnézet: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Nyomtatás indítása",
        'print_sent': "Nyomtatási feladat elküldve",
        'print_now': "Azonnali nyomtatás",
        'print_error': "Hiba az azonnali nyomtatás során",
        'print_limited': "Nyomtatási funkció korlátozva ezen a rendszeren",
        'print_error_format': "Hiba az azonnali nyomtatás során: {0}",
        'warning': "Figyelmeztetés",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Váltás világos módba",
        'mode_switch_to_dark': "Váltás sötét módba",
        'mode_dark_activated': "Sötét mód aktiválva",
        'mode_light_activated': "Világos mód aktiválva",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Teljes nézet",
        'zoom_two_pages': "Két oldal egymás mellett",
        'zoom_overview': "Áttekintő mód",
        'zoom_cannot_during_search': "Nagyítás nem lehetséges keresés közben",
        'zoom_exit_first': "Először lépjen ki a nagyításból",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Húzd és vidd engedélyezve",
        'drag_disabled': "Húzd és vidd letiltva",
        'drag_page_grab': "{0}. oldal megfogva",
        'drag_page_dropped': "{0}. oldal beszúrva a(z) {1}. helyre",
        'drag_position_invalid': "Érvénytelen hely",
        'drag_same_position': "A(z) {0}. oldal a(z) {0}. helyen marad",
        'drag_error': "Hiba az áthelyezés során",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Szövegbevitel bővített formázással és szövegblokk-kezeléssel",
        'text_templates': "Elérhető szövegblokkok:",
        'text_name': "Név",
        'text_preview': "Szövegelőnézet",
        'text_enter': "Szöveg:",
        'text_font_size': "Betűméret:",
        'text_formatting': "Formázás:",
        'text_bold': "Félkövér",
        'text_italic': "Dőlt",
        'text_underline': "Aláhúzott",
        'text_alignment': "Igazítás:",
        'text_left': "Balra",
        'text_center': "Középre",
        'text_right': "Jobbra",
        'text_color': "Szövegszín:",
        'text_opacity': "Átlátszatlanság:",
        'text_word_wrap': "Sortörés:",
        'text_auto': "Automatikus",
        'text_page_width_95': "Oldalszélesség (95%)",
        'text_page_width_85': "Nagyon széles (85%)",
        'text_page_width_75': "Szélesebb (75%)",
        'text_page_width_60': "Széles (60%)",
        'text_page_width_50': "Közepes (50%)",
        'text_page_width_30': "Keskeny (30%)",
        'text_page_width_20': "Keskenyebb (20%)",
        'text_page_width_10': "Nagyon keskeny (10%)",
        'text_no_wrap': "Nincs sortörés",
        'text_private': "Privát szövegblokk (hitelesítés szükséges)",
        'text_preview_label': "Előnézet:",
        'text_preview_placeholder': "Itt jelenik meg a szöveg előnézete...",
        'text_no_text': "(Nincs szöveg)",
        'text_save_template': "💾 Mentés blokkként",
        'text_delete_template': "🗑 Kiválasztott szövegblokk törlése",
        'text_show_private': "Privátak mutatása",
        'text_hide_private': "Privátak elrejtése",
        'text_use': "✅ Szöveg használata",
        'text_saved': "Szövegblokk elmentve:\n{0}",
        'text_saved_voice': "Szövegblokk elmentve",
        'text_deleted': "Szövegblokk törölve",
        'text_no_text_to_save': "Nincs mentendő szöveg.",
        'text_no_templates': "Nincsenek szövegblokkok",
        'text_private_master_required': "Privát blokkok csak akkor használhatók, ha be van állítva master jelszó.\n\nSzeretné most beállítani a master jelszót?",
        'text_filename': "Fájlnév a szövegblokkhoz (a 'Text_' és '.txt' nélkül):",
        'text_filename_hint': "Példa: 'Telefon HomeOffice' néven 'Text_Telefon HomeOffice.txt' fájlba mentve",
        'text_save_hint': "A szövegblokk automatikusan a formázással együtt lesz mentve.",
        'text_guide_title': "Szövegbevitel – Útmutató",
        'text_delete_confirm': "Biztosan törli a szövegblokkot?\n\nFájl: {0}\nSzöveg: {1}...",
        'text_make_public': "Megjelölés nyilvánosként",
        'text_make_private': "Megjelölés privátként",
        'text_privacy_changed': "Privát állapot megváltozott",
        'text_private_always': "Privátak mindig láthatók (beállítás)",
        'text_mode_required': "Először kapcsolja be a szövegmódot",
        'text_continue_editing': "Szerkesztés folytatása – kurzor a szöveg végén",
        'text_no_input': "Nem lett szöveg megadva – szöveg elvetve",
        'save_dialog_question': "Hogyan szeretne továbbhaladni?",
        'text_save_question': "Mentse az összes szöveget és ikszet, igazítsa, folytassa a szerkesztést vagy vesse el?",
        'copy_cross': "Iksz kimásolva",
        'paste_cross': "Iksz beillesztve",
        'paste_text': "Szöveg beillesztve",
        'cross_discarded': "Iksz elvetve",
        'all_discarded': "Minden elvetve",
        'text_discarded': "Szöveg elvetve",
        'no_texts_to_save': "Nincs mentendő szöveg",
        'no_valid_texts': "Nincs érvényes szöveg a mentéshez",
        'text_word_singular': "szöveg",
        'text_word_plural': "szöveg",
        'cross_word_singular': "iksz",
        'cross_word_plural': "iksz",
        'texts_saved_title': "Szövegek elmentve",
        'texts_crosses_saved': "{0} {1} és {2} {3} beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'texts_crosses_saved_voice': "{0} {1} és {2} {3} elmentve.",
        'texts_saved': "{0} {1} beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'texts_saved_voice': "{0} {1} elmentve.",
        'crosses_saved': "{0} {1} beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'crosses_saved_voice': "{0} {1} elmentve.",
        'elements_saved': "{0} elem beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'elements_saved_voice': "{0} elem elmentve.",
        'text_window_load_error': "A szövegablak nem tölthető be",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Szövegbevitel és szövegblokkok – Részletes útmutató**

        **1. Szöveg beillesztése és szerkesztése**
        - Kattintson jobb egérgombbal a dokumentum kívánt helyére, és válassza a "Szöveg beillesztése" lehetőséget.
        - Megnyílik egy párbeszédablak, ahol megadhatja a szöveget és formázhatja:
        • Betűméret, félkövér, dőlt, aláhúzott
        • Szövegszín (tetszőlegesen választható)
        • Átlátszatlanság (fedettség) csúszkával
        • Sortörés (különböző szélességek, pl. oldalszélesség, keskeny, nincs sortörés)
        - A megerősítés után a szöveg megjelenik a kattintás helyén. Egérrel vagy nyílbillentyűkkel mozgathatja.
        - Dupla kattintás a szövegre szerkesztési módot nyit; ESC billentyűvel kiléphet.

        **2. Szövegblokkok (sablonok) kezelése**
        - A szöveg párbeszédablak bal oldalán láthatja az összes mentett szövegblokk listáját.
        - **Blokk mentése:** Adja meg a szöveget, formázza meg, majd kattintson a "💾 Mentés blokkként" gombra. Adjon meg egy fájlnevet (kiterjesztés nélkül).
        - **Blokk betöltése:** Kattintson a kívánt névre a listában. A szöveg és a formázás átkerül, és szükség esetén tovább igazítható.
        - **Törlés:** Jobb egérgombbal kattintson egy blokkra, majd törölheti vagy módosíthatja a privát állapotát.

        **3. Privát szövegblokkok (master jelszó)**
        - Ha beállított master jelszót (Beállítások → Jelszókezelés), a blokkokat megjelölheti "privátként".
        - Ehhez jelölje be a "Privát szövegblokk" jelölőnégyzetet a párbeszédablakban mentés előtt.
        - A privát blokkok csak akkor jelennek meg a listában, ha egyszer (munkamenetenként) megadta a master jelszót (hitelesítés a lakat ikonnal vagy az első hozzáféréskor).
        - Így megvédheti bizalmas szövegblokkjait az illetéktelen hozzáféréstől.

        **4. Ikszek beillesztése**
        - A helyi menüből grafikus ikszet is beilleszthet (pl. jelölőnégyzetekhez).
        - Az ikszek mérete, vonalvastagsága és színe globálisan beállítható a "Beállítások" → "Iksz-beállítások" menüben.
        - Jobb egérgombbal kattintva egy meglévő ikszre egyénileg módosíthatja.

        **5. Csoportos műveletek**
        - Ha több szöveget vagy ikszt helyezett el egy oldalon, a helyi menüben (jobb egérgombbal a szövegmódban) egyszerre mentheti vagy vetheti el az összes elemet.
        - Mentéskor az összes elem beágyazódik a PDF-be, és vektorgrafikaként marad meg.

        **6. Billentyűparancsok szövegmódban**
        - Nyílbillentyűk: elem mozgatása
        - Ctrl+nyílbillentyűk: nagyobb lépések
        - Enter: mentési párbeszédablak megnyitása (összes mentése / igazítás / elvetés)
        - ESC: aktuális elem elvetése
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Szövegbevitel és szövegblokkok – Részletes útmutató</strong></p>

        <p><strong>1. Szöveg beillesztése és szerkesztése</strong></p>
        <ul>
        <li>Kattintson jobb egérgombbal a dokumentum kívánt helyére, és válassza a "Szöveg beillesztése" lehetőséget.</li>
        <li>Megnyílik egy párbeszédablak, ahol megadhatja a szöveget és formázhatja:<br/>
        • Betűméret, félkövér, dőlt, aláhúzott<br/>
        • Szövegszín (tetszőlegesen választható)<br/>
        • Átlátszatlanság (fedettség) csúszkával<br/>
        • Sortörés (különböző szélességek, pl. oldalszélesség, keskeny, nincs sortörés)</li>
        <li>A megerősítés után a szöveg megjelenik a kattintás helyén. Egérrel vagy nyílbillentyűkkel mozgathatja.</li>
        <li>Dupla kattintás a szövegre szerkesztési módot nyit; ESC billentyűvel kiléphet.</li>
        </ul>

        <p><strong>2. Szövegblokkok (sablonok) kezelése</strong></p>
        <ul>
        <li>A szöveg párbeszédablak bal oldalán láthatja az összes mentett szövegblokk listáját.</li>
        <li><strong>Blokk mentése:</strong> Adja meg a szöveget, formázza meg, majd kattintson a "💾 Mentés blokkként" gombra. Adjon meg egy fájlnevet (kiterjesztés nélkül).</li>
        <li><strong>Blokk betöltése:</strong> Kattintson a kívánt névre a listában. A szöveg és a formázás átkerül, és szükség esetén tovább igazítható.</li>
        <li><strong>Törlés:</strong> Jobb egérgombbal kattintson egy blokkra, majd törölheti vagy módosíthatja a privát állapotát.</li>
        </ul>

        <p><strong>3. Privát szövegblokkok (master jelszó)</strong></p>
        <ul>
        <li>Ha beállított master jelszót (Beállítások → Jelszókezelés), a blokkokat megjelölheti "privátként".</li>
        <li>Ehhez jelölje be a "Privát szövegblokk" jelölőnégyzetet a párbeszédablakban mentés előtt.</li>
        <li>A privát blokkok csak akkor jelennek meg a listában, ha egyszer (munkamenetenként) megadta a master jelszót (hitelesítés a lakat ikonnal vagy az első hozzáféréskor).</li>
        <li>Így megvédheti bizalmas szövegblokkjait az illetéktelen hozzáféréstől.</li>
        </ul>

        <p><strong>4. Ikszek beillesztése</strong></p>
        <ul>
        <li>A helyi menüből grafikus ikszet is beilleszthet (pl. jelölőnégyzetekhez).</li>
        <li>Az ikszek mérete, vonalvastagsága és színe globálisan beállítható a "Beállítások" → "Iksz-beállítások" menüben.</li>
        <li>Jobb egérgombbal kattintva egy meglévő ikszre egyénileg módosíthatja.</li>
        </ul>

        <p><strong>5. Csoportos műveletek</strong></p>
        <ul>
        <li>Ha több szöveget vagy ikszt helyezett el egy oldalon, a helyi menüben (jobb egérgombbal a szövegmódban) egyszerre mentheti vagy vetheti el az összes elemet.</li>
        <li>Mentéskor az összes elem beágyazódik a PDF-be, és vektorgrafikaként marad meg.</li>
        </ul>

        <p><strong>6. Billentyűparancsok szövegmódban</strong></p>
        <ul>
        <li>Nyílbillentyűk: elem mozgatása</li>
        <li>Ctrl+nyílbillentyűk: nagyobb lépések</li>
        <li>Enter: mentési párbeszédablak megnyitása (összes mentése / igazítás / elvetés)</li>
        <li>ESC: aktuális elem elvetése</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Iksz-beállítások",
        'cross_properties': "Iksz tulajdonságai",
        'cross_size': "Méret (px):",
        'cross_line_width': "Vonalvastagság:",
        'cross_color': "Szín:",
        'cross_choose_color': "Választás",
        'cross_fine_tuning': "Finomhangolás mentéskor (pixel)",
        'cross_offset_x': "X-eltolás:",
        'cross_offset_y': "Y-eltolás:",
        'cross_offset_x_tooltip': "Negatív értékek balra, pozitívak jobbra tolják az ikszet mentéskor",
        'cross_offset_y_tooltip': "Negatív értékek felfelé, pozitívak lefelé tolják az ikszet mentéskor",
        'cross_preview': "Előnézet",
        'cross_save': "Beállítások átvétele",
        'cross_customized': "Iksz igazítva",
        'cross_settings_applied': "Iksz-beállítások elmentve.\nMéret: {0}px, vonalvastagság: {1}px\n{2}",
        'cross_updated_count': "{0} meglévő iksz frissítve.",
        'cross_no_crosses': "Nincsenek meglévő ikszek.",
        'cross_settings_applied_all': "Iksz-beállítások átvéve mind a(z) {0} ikszre",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Aláírás-beállítások",
        'signature_1': "1. aláírás",
        'signature_2': "2. aláírás",
        'signature_select': "Aláírás kiválasztása",
        'signature_add': "➕ Új aláírás hozzáadása...",
        'signature_size': "{0}. aláírás mérete (%):",
        'signature_common': "Általános beállítások",
        'signature_timestamp': "Időbélyeg automatikus hozzáadása",
        'signature_location': "Alapértelmezett hely:",
        'signature_timestamp_size': "Időbélyeg betűmérete:",
        'signature_no_files': "-- Nincsenek aláírások --",
        'signature_insert': "Aláírás beillesztése",
        'signature_insert_1': "1. aláírás beillesztése",
        'signature_insert_2': "2. aláírás beillesztése",
        'signature_customize': " Aláírás igazítása",
        'signature_discard': " Aláírás elvetése",
        'signature_save_all': " Összes aláírás mentése",
        'signature_discard_all': " Összes aláírás elvetése",
        'signature_guide_title': "Aláírások – Útmutató",
        'signature_guide': """
📝 Aláírások – Rövid útmutató

- Állítson be master jelszót
- Konfigurálja az aláírásokat a Beállítások menüben
  (méret, időbélyeg ...)
- JOBB GOMBBAL kattintson a kívánt helyre a beillesztéshez
  (master jelszó munkamenetenként egyszer szükséges)
- Mozgassa az aláírást egérrel vagy nyílbillentyűkkel
- Több aláírás is beilleszthető egymás után
- Minden aláírás egyénileg igazítható
- Egyedi aláírás elvetése
- Összes aláírás egyidejű mentése / elvetése
- Alternatívaként a menüsor is használható.
        """,
        'signature_placeholder': "Nincs előnézet",
        'signature_info': "{0}. aláírás: {1}×{2} px ({3}%-a {4}×{5}-nek)",
        'signature_info_placeholder': "{0}. aláírás beállításai",
        'signature_inserted': "{0}. aláírás beillesztve a(z) {1}. oldalra",
        'signature_deleted': "Aláírás törölve",
        'signature_copied': "Aláírás kimásolva",
        'signature_pasted': "{0}. aláírás beillesztve",
        'signature_saved': "{0} aláírás beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'signature_saved_voice': "{0} aláírás elmentve",
        'mode_replace_signature_format': "Kilépés a módból és {0}. aláírás beillesztése",
        'mode_conflict_voice_signature': "A(z) {0} mód aktív. Kilépjen és illessze be az aláírást?",
        'signature_not_configured': "A(z) {0}. aláírás nincs konfigurálva",
        'signature_file_not_found': "Az aláírás fájl nem található",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nincs kimásolt aláírás",
        'no_signatures_to_save': "Nincs mentendő aláírás",
        'signature_save_question': "Mentse az összes aláírást, igazítson vagy vesse el ezt?",
        'signatures_saved_title': "Aláírások elmentve",
        'signatures_saved': "{0} aláírás beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'signatures_saved_voice': "{0} aláírás elmentve.",
        'all_signatures_discarded': "Összes aláírás elvetve",
        'signature_settings_saved': "Aláírás-beállítások elmentve",
        'signature_cancelled': "Aláírás elvetve",
        'signature_active_title': "Aláírás aktív",
        'signature_replace_question': "Már van egy aktív aláírás.\n\nSzeretné lecserélni a jelenlegi aláírást?",
        'signature_replace': "Aláírás cseréje",
        'signature_replace_voice': "Lecserélje a jelenlegi aláírást vagy megszakítja?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Képbeállítások",
        'image_common': "Általános képbeállítások",
        'image_keep_aspect': "Képarány megtartása húzáskor",
        'image_default_size': "Alapértelmezett méret (%):",
        'image_dark_invert': "Képek invertálása sötét módban",
        'image_dark_invert_tooltip': "Bekapcsolva: a képek invertálva lesznek a jobb láthatóság érdekében",
        'image_fine_tuning': "Finomhangolás (pixel)",
        'image_offset_x': "X-eltolás:",
        'image_offset_y': "Y-eltolás:",
        'image_offset_x_tooltip': "Negatív értékek balra, pozitívak jobbra tolják a képet mentéskor",
        'image_offset_y_tooltip': "Negatív értékek felfelé, pozitívak lefelé tolják a képet mentéskor",
        'image_select': "Kép kiválasztása",
        'image_insert': "Kép beillesztése",
        'image_customize': " Kép igazítása",
        'image_aspect': " Képarány megtartása",
        'image_discard': " Kép elvetése",
        'image_save_all': " Összes kép mentése",
        'image_discard_all': " Összes kép elvetése",
        'image_filter': "Képek",
        'image_guide_title': "Képek beillesztése – Útmutató",
        'image_guide': """
📷 Képek beillesztése PDF-be – Rövid útmutató:

1. Jobb gombbal kattintson a kívánt helyre
2. "Kép beillesztése" → kép kiválasztása
3. Helyezze el a képet: húzza az egérrel
4. Méret módosítása: húzza a sarkoknál/széleknél
5. Képarány megtartása: [A] billentyű
6. További igazítások: jobb gombbal a képre

Tipp: A helyi menüben módosíthatja a beállításokat.
        """,
        'image_inserted': "Kép beillesztve a(z) {1}. oldalra",
        'image_deleted': "Kép elvetve",
        'image_copied': "Kép kimásolva",
        'image_pasted': "Kép beillesztve",
        'image_saved': "{0} kép beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'image_saved_voice': "{0} kép elmentve",
        'image_aspect_on': "bekapcsolva",
        'image_aspect_off': "kikapcsolva",
        'image_aspect_toggle': "Képarány megtartása {0}",
        'image_reset': "Kép visszaállítva eredeti méretre",
        'image_replaced': "Kép lecserélve",
        'image_invalid': "Érvénytelen kép",
        'mode_replace_image': "Kép beillesztése",
        'mode_conflict_voice_image': "A(z) {0} mód aktív. Kilépjen és illessze be a képet?",
        'image_active_title': "Kép aktív",
        'image_replace_question': "Már van egy aktív kép.\n\nSzeretné lecserélni a jelenlegi képet?",
        'image_replace': "Kép cseréje",
        'image_replace_voice': "Lecserélje a jelenlegi képet vagy megszakítja?",
        'image_filter_all': "Képek (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Minden fájl (*.*)",
        'no_copied_image': "Nincs kimásolt kép",
        'image_discarded': "Kép elvetve",
        'image_save_question': "Mentse az összes képet, igazítson vagy vesse el ezt?",
        'no_images_to_save': "Nincs mentendő kép",
        'no_valid_images': "Nincs érvényes kép a mentéshez",
        'images_saved_title': "Képek elmentve",
        'images_saved': "{0} kép beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'images_saved_voice': "{0} kép elmentve.",
        'all_images_discarded': "Összes kép elvetve",
        'image_settings_updated': "Képbeállítások frissítve",
        'image_replace_title': "Új kép kiválasztása",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Alakzat-beállítások",
        'form_basic': "Alapbeállítások",
        'form_default_type': "Alapértelmezett alaktípus:",
        'form_rectangle': "Téglalap",
        'form_ellipse': "Ellipszis",
        'form_line': "Vonal",
        'form_arrow': "Nyíl",
        'form_line_width': "Vonalvastagság:",
        'form_colors': "Színek",
        'form_line_color': "Vonal színe:",
        'form_fill_color': "Kitöltő szín:",
        'form_choose_color': "Választás",
        'form_transparent': "Átlátszó háttér (csak vonal)",
        'form_filled': "kitöltve",
        'form_dark_mode': "Sötét mód",
        'form_dark_invert': "Színek invertálása sötét módban",
        'form_fine_tuning': "Finomhangolás (pixel)",
        'form_offset_x': "X-eltolás:",
        'form_offset_y': "Y-eltolás:",
        'form_offset_x_tooltip': "Negatív értékek balra, pozitívak jobbra tolják az alakzatot mentéskor",
        'form_offset_y_tooltip': "Negatív értékek felfelé, pozitívak lefelé tolják az alakzatot mentéskor",
        'form_preview': "Előnézet",
        'form_insert': "Alakzat beillesztése",
        'form_rectangle_insert': "Téglalap",
        'form_ellipse_insert': "Ellipszis/kör",
        'form_line_insert': "Vonal (2 kattintás)",
        'form_arrow_insert': "Nyíl (2 kattintás)",
        'form_customize': " Alakzat igazítása",
        'form_transparent_toggle': " Átlátszó háttér",
        'form_discard': " Alakzat elvetése",
        'form_save_all': " Összes alakzat mentése",
        'form_discard_all': " Összes alakzat elvetése",
        'form_guide_title': "Alakzatok beillesztése – Útmutató",
        'form_guide': """
📐 Alakzatok beillesztése PDF-be – Rövid útmutató:

1. Válassza ki az alaktípust (téglalap, ellipszis, vonal, nyíl)
2. Kattintson a helyére
   - Téglalap/ellipszis: egy kattintás elhelyezi az alakzatot
   - Vonal/nyíl: két kattintás a kezdő- és végponthoz
3. Helyezze el az alakzatot: húzza az egérrel
4. Méret módosítása: húzza a sarkoknál/széleknél
5. Alakzat mentése: Enter
6. Alakzat elvetése: ESC
7. További igazítások: jobb gombbal az alakzatra

Tipp: A helyi menüben módosíthatja a beállításokat.
        """,
        'form_inserted': "{0} beillesztve a(z) {1}. oldalra",
        'form_deleted': "Alakzat törölve",
        'form_copied': "Alakzat kimásolva",
        'form_pasted': "Alakzat beillesztve",
        'form_saved': "{0} alakzat beillesztve a PDF-be.\n\nA PDF újratöltve...",
        'form_saved_voice': "{0} alakzat elmentve",
        'form_reset': "Alakzat visszaállítva alapértelmezett méretre",
        'form_transparent_on': "bekapcsolva",
        'form_transparent_off': "kikapcsolva",
        'form_transparent_toggled': "Átlátszó háttér {0}",
        'form_line_cancel': "Vonalrajzolás megszakítva",
        'form_second_click': "Most kattintson a {0} végpontjára",
        'mode_replace_form': "Alakzat beillesztése",
        'mode_conflict_voice_form': "A(z) {0} mód aktív. Kilépjen és illessze be az alakzatot?",
        'form_settings_updated': "Alakzat-beállítások frissítve",
        'form_unknown': "Alakzat",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Kattintson a kezdőpontra",
        'form_line_guide_2': "2. Kattintson a végpontra",
        'form_line_guide_3': "A vonal a két pont között lesz megrajzolva.",
        'form_line_status_1': "Várakozás az első kattintásra...",
        'form_line_status_2': "Első pont beállítva: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Most kattintson a végpontra...",
        'form_line_status_4': "Mindkét pont beállítva.\nKattintson a 'Kész' gombra a mentéshez.",
        'form_line_reset': "Visszaállítás",
        'form_line_finish': "Kész",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Másolás (Cmd+C)",
        'paste': "Beillesztés (Cmd+V)",
        'copied': "Kimásolva: {0}",
        'no_element_to_copy': "Nincs kijelölt elem másoláshoz",
        'no_copied_data': "Nincsenek kimásolt adatok",
        'no_valid_position': "Nincs érvényes hely a beillesztéshez",
        'copy_text': "Szöveg kimásolva",
        'copy_image': "Kép kimásolva",
        'copy_form': "Alakzat kimásolva",
        'copy_signature': "Aláírás kimásolva",
        'element_text': "Szöveg",
        'element_image': "Kép",
        'element_form': "Alakzat",
        'element_signature': "Aláírás",
        'element_unknown': "Elem",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Módütközés",
        'mode_conflict_message': "A(z) '{0}' mód már aktív.\n\nSzeretné kilépni belőle és {1}?",
        'mode_replace': "Kilépés a módból és {0}",
        'mode_cancel': "Mégse",
        'mode_replace_text': "szöveg beillesztése",
        'mode_replace_cross': "iksz beillesztése",
        'mode_replace_signature': "aláírás beillesztése",
        'mode_replace_image': "kép beillesztése",
        'mode_replace_form': "alakzat beillesztése",
        'mode_conflict_voice': "A(z) {0} mód aktív. Kilépjen és illessze be a szöveget?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Szövegbevitel",
        'active_mode_signature': "Aláírás",
        'active_mode_image': "Kép",
        'active_mode_form': "Alakzat",
        'active_mode_and': " és ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Beillesztés",
        'insert_another_text': "Szöveg beillesztése",
        'insert_another_cross': "Iksz beillesztése",
        'insert_another_signature_1': "1. aláírás",
        'insert_another_signature_2': "2. aláírás",
        'insert_another_image': "Kép beillesztése",
        'insert_another_form_rect': "Téglalap",
        'insert_another_form_ellipse': "Ellipszis",
        'insert_another_form_line': "Vonal (2 kattintás)",
        'insert_another_form_arrow': "Nyíl (2 kattintás)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} mentése",
        'save_dialog_message': "{0} mentésre kerül a(z) {1}. oldalra.\n\nHogyan szeretne továbbhaladni?",
        'save_all': "Összes {0} mentése",
        'save_single': "{0} mentése",
        'save_customize': "{0} igazítása",
        'save_discard': "A(z) {0} elvetése",
        'save_continue': "Szerkesztés folytatása",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Ugrás a(z) {0}. oldalra",
        'context_rotate': " {0}. oldal elforgatása",
        'context_delete': " {0}. oldal törlése",
        'context_export': " {0}. oldal exportálása",
        'context_mark_as': " Oldal megjelölése mint...",
        'context_mark_empty': " Üres oldal",
        'context_unmark_empty': " Már nem üres",
        'context_mark_export': " Megjelölés exportálásra",
        'context_unmark_export': " Ne exportálja többé",
        'context_batch_actions': " Csoportos műveletek",
        'context_batch_delete_empty': " Összes ({0}) üres oldal törlése",
        'context_batch_export_single': " Összes ({0}) oldal exportálása (egy fájl)",
        'context_batch_export_split': " Összes ({0}) oldal exportálása (különállóan)",
        'context_drag_start': " Húzd és vidd indítása",
        'context_drag_stop': " Húzd és vidd befejezése",
        'context_insert': " Beillesztés",
        'context_insert_pages': " Oldalak beillesztése",
        'context_zoom': "Nagyítás",
        'discard_mixed': "Összes {0} {1} és {2} {3} elvetése",
        'save_mixed': "{0} {1} és {2} {3} mentése",
        'discard_texts': "Összes {0} szöveg elvetése",
        'discard_text_single': "1 szöveg elvetése",
        'save_texts': "{0} szöveg mentése",
        'save_text_single': "1 szöveg mentése",
        'discard_crosses': "Összes {0} iksz elvetése",
        'discard_cross_single': "1 iksz elvetése",
        'save_crosses': "{0} iksz mentése",
        'save_cross_single': "1 iksz mentése",
        'discard_signatures': "Összes {0} aláírás elvetése",
        'save_signature_single': "1 aláírás mentése",
        'save_signatures': "{0} aláírás mentése",
        'discard_images': "Összes {0} kép elvetése",
        'save_image_single': "1 kép mentése",
        'save_images': "{0} kép mentése",
        'discard_forms': "Összes {0} alakzat elvetése",
        'save_form_single': "1 alakzat mentése",
        'save_forms': "{0} alakzat mentése",
        'cross_discard': "Iksz elvetése",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Exportálási / importálási információk",
        'export_what': "📋 Mit exportálunk?",
        'export_general': "Általános beállítások",
        'export_general_items': "• Beszédkiadás (be/ki, sebesség)\n• Sötét/világos mód\n• Biztonsági másolat beállításai\n• OCR-beállítások",
        'export_image_form': "Kép- és alakzatbeállítások",
        'export_image_form_items': "• Képbeállítások (képarány, alapértelmezett méret)\n• Alakzat-beállítások (vonalvastagság, színek)\n• Aláírás-beállítások (útvonalak, méretek, időbélyeg)",
        'export_passwords': "Jelszó-adatbázis",
        'export_passwords_items': "• Az összes mentett PDF-jelszó\n• Választhatóan titkosítva vagy visszafejtve",
        'export_master': "Master jelszó beállításai",
        'export_master_items': "• Master jelszó hash\n• Aláírások/szövegblokkok beállításai",
        'export_signatures': "Aláírások és szövegblokkok",
        'export_signatures_items': "• Az összes képfájl (aláírások)\n• Az összes szövegblokk formázással\n• Privát/nyilvános jelölések",
        'export_import_warning': "⚠️ Fontos megjegyzések",
        'export_import_note': "• Importáláskor az ÖSSZES aktuális beállítás felülíródik\n• Az alkalmazás újraindítása szükséges\n• A meglévő aláírások/szövegblokkok lecserélődnek",
        'export_master_note': "• Ha master jelszó van beállítva, választhat:\n  - Visszafejtve (jelszavak plaintextben)\n  - Titkosítva (csak master jelszóval olvasható)",
        'export_security': "• Az exportált ZIP-fájl bizalmas adatokat tartalmaz\n• Tartsa biztonságos helyen (pl. titkosított USB-meghajtón)\n• A fájl elvesztése esetén a jelszavak végleg elvesznek",
        'export_format': "📁 Exportálási formátum",
        'export_format_desc': "A beállítások egyetlen ZIP-fájlba kerülnek mentésre:",
        'export_filename': "PDFDarkView_Beallitasok_ÉÉÉÉHHNN_ÓÓPPMP.zip",
        'export_success': "Beállítások sikeresen exportálva",
        'export_failed': "Exportálás sikertelen",
        'export_import_question': "Szeretné most újraindítani az alkalmazást?",
        'export_password_question': "Master jelszó van beállítva.\n\nSzeretné a jelszavakat visszafejtve exportálni?\n(ellenkező esetben titkosítva lesznek exportálva)",
        'export_decrypt': "Exportálás visszafejtve",
        'export_encrypt': "Exportálás titkosítva",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Információ",
        'info_title': "A PDF Dark View névjegye",
        'info_version': "Verzió",
        'info_author': "Fejlesztő: Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Névjegy",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> egy akadálymentes PDF-megjelenítő, amelyet kifejezetten látássérült személyek számára fejlesztettek ki.</p>

            <p><strong>Főbb jellemzők:</strong></p>
            <ul>
                <li>Kontrasztos, testreszabható felület</li>
                <li>Teljes billentyűzetes vezérlés</li>
                <li>Beépített beszédfelolvasás</li>
                <li>OCR a szkennelt dokumentumokhoz</li>
                <li>Kiterjedt szerkesztőeszközök</li>
            </ul>

            <p>Több mint 50 nyelv támogatott – így a PDF-ek mindenki számára hozzáférhetőek.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkciók",
        'info_features_intro': "A PDF Dark View a következő lehetőségeket kínálja Önnek:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Megjelenítés és navigáció</strong> – Sötét/Világos mód, lapozás, nagyítás, ugrás oldalra</li>
            <li><strong>OCR (szövegfelismerés)</strong> – Tegye a szkennelt dokumentumokat kereshetővé és másolhatóvá</li>
            <li><strong>Szerkesztés</strong> – Szövegek, X-ek, aláírások, képek és alakzatok beszúrása</li>
            <li><strong>Oldalkezelés</strong> – Törlés, kinyerés, beszúrás, áthelyezés fogd és vidd módszerrel</li>
            <li><strong>Exportálás</strong> – Wordbe, Pagesbe vagy szövegként</li>
            <li><strong>Biztonság</strong> – Jelszavas védelem és -kezelés</li>
            <li><strong>Akadálymentesség</strong> – Beszédfelolvasás, billentyűzetes vezérlés, magas kontraszt</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Kezelés",
        'info_accessibility': "♿ Akadálymentesség – teljes billentyűzetes vezérlés",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Általános</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF megnyitása</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Keresés</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Sötét/Világos mód váltása</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Nyomtatás</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Kilépés</div>

        <div class="shortcut-cat">📖 Navigáció</div>
        <div class="shortcut-row"><kbd>Nyílbillentyűk</kbd> Lapozás oldalról oldalra</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Ugrás oldalra</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Első oldal</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Utolsó oldal</div>

        <div class="shortcut-cat">✏️ Szerkesztés</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Szöveg beszúrása</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Oldalak törlése</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Oldalak kinyerése</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Oldalak beszúrása</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Oldalak áthelyezése</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Oldal forgatása</div>

        <div class="shortcut-cat">🖼️ Elemek áthelyezése</div>
        <div class="shortcut-row"><kbd>Nyílbillentyűk</kbd> Szöveg/kép/aláírás áthelyezése</div>
        <div class="shortcut-row"><kbd>Ctrl+Nyílbillentyűk</kbd> Nagyobb lépések</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Mentés</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Elvetés</div>

        <div class="shortcut-cat">🗣️ Beszédfelolvasás</div>
        <div class="shortcut-row"><kbd>F2</kbd> Beszédfelolvasás be/ki</div>
        """,
        'info_contextmenu': "📌 Fontos: Minden funkció elérhető a helyi menüből is (jobb egérgomb)!",
        'info_accessibility_hint': "💡 Tipp: A beszédfelolvasás (F2) megkönnyíti a tájékozódást és visszajelzést ad a menükről és párbeszédablakokról.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licenc & Impresszum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSZUM</strong><br>
        Információ a § 5 TMG szerint:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Németország<br>
        E-mail: binhdiez64@gmail.com<br>
        A tartalomért felelős: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Felelősségkorlátozás</strong><br>
        A szoftver a legnagyobb gondossággal készült. A pontosságért, teljességért és funkcionalitásért nem vállalunk garanciát. A használat saját felelősségre történik.<br><br>

        <strong>📄 MIT licenc (magáncélú használat)</strong><br>
        Szerzői jog (c) 2026 Toralf Schulz (BinhDiez)<br>
        Engedélyezett: ingyenes használat, magáncélú módosítások, személyes másolatok.<br>
        Nem engedélyezett: eladás, kereskedelmi felhasználás, szerzői jogi értesítések eltávolítása.<br><br>

        <strong>🔧 Harmadik féltől származó komponensek</strong><br>
        Ez a szoftver GPL, AGPL, Apache 2.0, BSD és MIT licencek alá tartozó komponenseket tartalmaz.<br>
        Továbbterjesztéskor be kell tartani a megfelelő licencfeltételeket.<br><br>

        <strong>🌐 Nyílt forráskód</strong><br>
        A forráskód elérhető, és a megfelelő licencfeltételeknek megfelelően megtekinthető, módosítható és továbbterjeszthető.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Köszönetnyilvánítás",
        'info_credits': "Köszönet a nyílt forráskódú közösségnek",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-feldolgozás</li>
            <li><strong>PyQt5</strong> – Grafikus felület</li>
            <li><strong>Tesseract OCR</strong> – Szövegfelismerés</li>
            <li><strong>OCRmyPDF</strong> – OCR-integráció</li>
            <li><strong>python-docx</strong> – Word export</li>
            <li><strong>qtawesome</strong> – Ikonok</li>
            <li><strong>DeepSeek</strong> – Támogatás a fordításokhoz (50+ nyelv)</li>
            <li><strong>Minden felhasználó</strong> – Az értékes visszajelzésekért</li>
            <li><strong>A nyílt forráskódú közösség</strong> – A nagyszerű könyvtárakért</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Nyelvek",
        'info_languages_header': "🌍 Nyelvi támogatás",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>A PDF Dark View jelenleg <strong>62 nyelvet</strong> támogat – így a szoftver világszerte akadálymentesen használható.</p>

            <p><strong>📖 Teljes nyelvi lista (Állapot: 2026. március):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albán (Shqip)</li>
                    <li>🇩🇿 Arab (العربية)</li>
                    <li>🇮🇩 Balinéz (Basa Bali)</li>
                    <li>🇧🇩 Bengáli (বাংলা)</li>
                    <li>🇲🇲 Burmai (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnyák (Bosanski)</li>
                    <li>🇧🇬 Bolgár (Български)</li>
                    <li>🇨🇳 Kínai (中文)</li>
                    <li>🇩🇰 Dán (Dansk)</li>
                    <li>🇩🇪 Német (Deutsch)</li>
                    <li>🇬🇧 Angol (English)</li>
                    <li>🇪🇪 Észt (Eesti)</li>
                    <li>🇫🇮 Finn (Suomi)</li>
                    <li>🇫🇷 Francia (Français)</li>
                    <li>🇬🇷 Görög (Ελληνικά)</li>
                    <li>🇮🇱 Héber (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Horvát (Hrvatski)</li>
                    <li>🇭🇺 Magyar (Magyar)</li>
                    <li>🇮🇩 Indonéz (Bahasa Indonesia)</li>
                    <li>🇮🇪 Ír (Gaeilge)</li>
                    <li>🇮🇸 Izlandi (Íslenska)</li>
                    <li>🇮🇹 Olasz (Italiano)</li>
                    <li>🇯🇵 Japán (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreai (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Lett (Latviešu)</li>
                    <li>🇱🇹 Litván (Lietuvių)</li>
                    <li>🇱🇺 Luxemburgi (Lëtzebuergesch)</li>
                    <li>🇲🇾 Maláj (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongol (Монгол)</li>
                    <li>🇳🇵 Nepáli (नेपाली)</li>
                    <li>🇳🇱 Holland (Nederlands)</li>
                    <li>🇳🇴 Norvég (Norsk)</li>
                    <li>🇦🇫 Pastu (پښتو)</li>
                    <li>🇮🇷 Perzsa (فارسی)</li>
                    <li>🇵🇱 Lengyel (Polski)</li>
                    <li>🇵🇹 Portugál (Português)</li>
                    <li>🇮🇳 Pandzsábi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Román (Română)</li>
                    <li>🇷🇺 Orosz (Русский)</li>
                    <li>🇸🇪 Svéd (Svenska)</li>
                    <li>🇷🇸 Szerb (Српски)</li>
                    <li>🇸🇰 Szlovák (Slovenčina)</li>
                    <li>🇸🇮 Szlovén (Slovenščina)</li>
                    <li>🇪🇸 Spanyol (Español)</li>
                    <li>🇹🇿 Szuahéli (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Cseh (Čeština)</li>
                    <li>🇹🇷 Török (Türkçe)</li>
                    <li>🇺🇦 Ukrán (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnami (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddis (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Saját nyelvek hozzáadása:</strong><br>
                Szeretne egy olyan nyelvet, amely még nem szerepel? Egyszerűen helyezze el a saját szótárfájlját (<code>sprache_xx.py</code>) az alkalmazás mellé – a szoftver automatikusan felismeri azt. Ha érdekli egy speciális fordítás, forduljon hozzám bizalommal.
            </div>

            <p><strong>🙏 Külön köszönet:</strong> A DeepSeek-nek az összes szótár 62 nyelvre történő fordításában nyújtott támogatásért.</p>

            <p>📧 Fordításokkal kapcsolatos kapcsolat: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Hiba",
        'error_occurred': "Hiba történt",
        'error_pdf_load': "Hiba a PDF betöltésekor",
        'error_pdf_save': "Hiba a PDF mentésekor",
        'error_ocr': "Hiba a szövegfelismerés során",
        'error_no_pdf': "Nincs PDF betöltve",
        'error_page_not_found': "Az oldal nem található",
        'error_invalid_range': "Érvénytelen oldaltartomány",
        'error_file_not_found': "A fájl nem található",
        'error_permission': "Nincs jogosultság",
        'error_unknown': "Ismeretlen hiba",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Siker",
        'success_operation': "A művelet sikeresen befejeződött",
        'success_saved': "Sikeresen elmentve",
        'success_exported': "Sikeresen exportálva",
        'success_imported': "Sikeresen importálva",
        'success_deleted': "Sikeresen törölve",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Megerősítés",
        'confirm_yes': "Igen",
        'confirm_no': "Nem",
        'confirm_ok': "OK",
        'confirm_cancel': "Mégse",
        'confirm_delete': "Törlés",
        'confirm_overwrite': "Felülírás",
        'confirm_continue': "Folytatás",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF betöltése...",
        'progress_saving': "PDF mentése...",
        'progress_exporting': "PDF exportálása...",
        'progress_processing': "Feldolgozás folyamatban...",
        'progress_wait': "Kérem várjon...",
        'progress_preparing': "Előkészítés...",
        'progress_finalizing': "Véglegesítés...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Fehér",
        'color_black': "Fekete",
        'color_red': "Piros",
        'color_green': "Zöld",
        'color_blue': "Kék",
        'color_yellow': "Sárga",
        'color_magenta': "Bíbor",
        'color_cyan': "Cián",
        'color_orange': "Narancssárga",
        'color_gray': "Szürke",
        'color_custom': "Színválasztás",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fájl",
        'menu_edit': "&Szerkesztés",
        'menu_view': "&Nézet",
        'menu_tools': "&Eszközök",
        'menu_settings': "&Beállítások",
        'menu_help': "&Súgó",
        'menu_language': "🌐 Nyelv",
        'menu_guides': "&Útmutatók",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Megnyitás",
        'file_save_as': "&Mentés másként...",
        'file_protect': "Dokumentum &védelme...",
        'file_export': "&Exportálás",
        'file_export_pages': "Exportálás Pages formátumba",
        'file_export_word': "Exportálás DOCX formátumba",
        'file_export_text': "Exportálás TXT formátumba",
        'file_print_now': "&Azonnali nyomtatás",
        'file_print': "&Nyomtatás",
        'file_close': "&Bezárás",
        'file_quit': "&Kilépés",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Keresés",
        'edit_ocr': " OCR futtatása",
        'edit_rotate': "Oldal &elforgatása",
        'edit_rotate_all': "&Összes oldal elforgatása",
        'edit_delete_pages': "Oldalak &törlése",
        'edit_extract_pages': "Oldalak &kivonása",
        'edit_insert_pages': "Oldalak &beszúrása",
        'edit_move_pages': "Oldalak &áthelyezése",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Szöveg és iksz beillesztése",
        'text_insert': " Szöveg beillesztése",
        'cross_insert': " Iksz beillesztése",
        'text_customize': " Szöveg igazítása",
        'cross_customize': " Iksz igazítása",
        'cross_customize_all': " Összes iksz igazítása",
        'text_discard': " Szöveg / iksz elvetése",
        'text_discard_all': " Összes szöveg és iksz elvetése",
        'text_save_all': " Összes szöveg és iksz mentése",
        'text_guide': " Szövegbevitel / szövegblokkok – Útmutató",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Aláírás beillesztése",
        'signature_settings_menu': " Beállítások...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Kép beillesztése",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Alakzat beillesztése",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Szövegablak megjelenítése",
        'view_zoom': "&Nagyítás",
        'view_zoom_page': "&Oldalszélesség (alapértelmezett)",
        'view_zoom_two': "&Két oldal",
        'view_zoom_overview': "&Áttekintés (több oldal)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Akadálymentesítés",
        'settings_voice': "Beszédkimenet",
        'settings_voice_tooltip': "kiegészíti a képernyőolvasók beszédét további információkkal",
        'settings_signature': "&Aláírás-beállítások",
        'settings_password': "&Jelszókezelés",
        'settings_backup': "Biztonsági másolat készítése a módosítások előtt",
        'settings_export_import': "&Beállítások exportálása / importálása",
        'settings_export': "&Összes beállítás exportálása...",
        'settings_import': "&Összes beállítás importálása...",
        'settings_export_info': "&Mit exportálunk?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "be",
        'voice_off': "ki",
        'voice_toggle': "Beszédkimenet {0}",
        'voice_speed': "Sebesség {0} százalék",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Az eszköz nem található:\n{0}\n\nBASE_DIR: {1}\nGyőződjön meg róla, hogy a PDF-eszközök a {1} könyvtárban vannak telepítve.",
        'tool_started': "{0} elindítva",
        'tool_start_failed': "Nem indítható el",
        'process_error_failed_to_start': "A folyamat nem indítható el. Létezik a fájl?",
        'process_error_crashed': "A folyamat összeomlott az indítás során.",
        'process_error_timeout': "A folyamat időtúllépése bekövetkezett.",
        'process_error_write': "Írási hiba a folyamatban.",
        'process_error_read': "Olvasási hiba a folyamatban.",
        'process_error_unknown': "Ismeretlen folyamathiba",
        'process_command': "Parancs",
        'process_normal_exit': "normál befejezés",
        'process_crashed': "összeomlott",
        'process_nonzero_exit': "{0} hibakóddal ({1}) fejeződött be",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Megszakítás...",
        'move_cancelling': "Áthelyezés megszakítása",
        'opening_pdf': "PDF megnyitása...",
        'loading_document': "Dokumentum betöltése...",
        'pdf_opened': "PDF megnyitva",
        'pages_found_moving': "{0} oldal található, {1} áthelyezendő",
        'creating_backup': "Biztonsági másolat készítése...",
        'backup_description': "Eredeti fájl biztonsági mentése...",
        'backup_saved_as': "Biztonsági másolat elmentve: {0}",
        'error_format': "Hiba: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Keresés visszaállítva",
        'page_header_simple': "=== {0}. oldal ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Jelszókezelés – Útmutató",
        'password_guide_voice': "Útmutató a jelszókezeléshez. Kérjük, olvassa el a megjegyzéseket.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Jelszókezelés – Részletes útmutató</strong></p>

        <p><strong>1. PDF-ek jelszavas védelme</strong></p>
        <ul>
        <li>Jelszóval védett PDF megnyitásakor egy párbeszédablak jelenik meg, ahol megadhatja a jelszót.</li>
        <li>A jelszót titkosítva elmentheti, hogy ne kelljen minden alkalommal újra beírnia („Jelszó mentése” jelölőnégyzet).</li>
        <li>A „Jelszó eltávolítása” gombbal létrehozhatja a PDF visszafejtett másolatát, és törölheti a jelszót az adatbázisból.</li>
        </ul>

        <p><strong>2. Master jelszó</strong></p>
        <ul>
        <li>A master jelszó védi a hozzáférést az összes mentett PDF-jelszóhoz.</li>
        <li><strong>Beállítás:</strong> Lépjen a „Beállítások → Jelszókezelés → Master jelszó beállításai” menüpontba, és kattintson a „Master jelszó beállítása” gombra. Válasszon erős jelszót (legalább 8 karakter).</li>
        <li><strong>Módosítás:</strong> Sikeres hitelesítés után módosíthatja a master jelszót.</li>
        <li><strong>Eltávolítás:</strong> Ha törli a master jelszót, az ÖSSZES mentett jelszó véglegesen törlődik. Előtte exportálhat biztonsági másolatot.</li>
        <li>Munkamenetenként egyszer hitelesítenie kell magát a master jelszóval, hogy hozzáférjen a védett funkciókhoz (pl. jelszavak megjelenítése).</li>
        </ul>

        <p><strong>3. Jelszókezelés (lista)</strong></p>
        <ul>
        <li>A „Beállítások → Jelszókezelés” menüpontban megnyílik az összes mentett PDF táblázata a titkosított jelszavakkal.</li>
        <li><strong>Master jelszó nélkül:</strong> Csak bejegyzéseket törölhet – a jelszavak rejtve maradnak.</li>
        <li><strong>Master jelszóval (hitelesítve):</strong> Megjelenítheti, másolhatja, exportálhatja és törölheti a jelszavakat.</li>
        <li><strong>Exportálás:</strong> Válasszon formátumot (JSON, CSV, TXT), és mentse a listát. Ha master jelszó van beállítva, eldöntheti, hogy a jelszavakat visszafejtve vagy titkosítva exportálja.</li>
        <li><strong>Importálás:</strong> Egy korábban exportált ZIP-fájl (az összes beállítással) visszaolvasható a „Beállítások → Beállítások exportálása / importálása” menüpontban. Figyelem: a meglévő adatok felülíródnak!</li>
        </ul>

        <p><strong>4. Jelszógenerátor</strong></p>
        <ul>
        <li>A jelszó párbeszédablakban (pl. PDF védelmekor) a beviteli mező jobb oldalán található egy dobókocka gomb 🎲.</li>
        <li>Kattintson rá a jelszógenerátor megnyitásához. Beállíthatja a hosszt, karakterkészleteket (nagybetűk, kisbetűk, számok, speciális karakterek) és elválasztójelet a jobb olvashatóság érdekében.</li>
        <li>A generált jelszó közvetlenül átvehető és szükség esetén másolható.</li>
        </ul>

        <p><strong>5. Fontos biztonsági megjegyzések</strong></p>
        <ul>
        <li>A mentett jelszavak AES-256 titkosítással vannak tárolva. A kulcs a master jelszóból (ha be van állítva) vagy egy fix értékből (master jelszó nélkül) származik.</li>
        <li>Master jelszó nélkül a jelszavak ugyan titkosítva vannak, de a kulcs a programban található – egy támadó, aki hozzáfér a fájljaihoz, visszafejtheti azokat. Ezért erősen ajánljuk a master jelszó használatát.</li>
        <li>A jelszó-adatbázis a `Data/passwords.json` fájlban található. Rendszeresen készítsen biztonsági másolatot, különösen a master jelszó eltávolítása előtt.</li>
        <li>Ha elveszíti a master jelszót, az összes mentett jelszó véglegesen elveszik.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Invertálási mód",
        'invert_mode_classic': "Klasszikus (minden szín invertálása)",
        'invert_mode_smart': "Intelligens (csak a fényerő invertálása)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Szürkeskálás küszöbérték",
        'gray_threshold_10': "10% (szigorú)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Alapértelmezett)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (lágy)",
        'threshold_changed': "Küszöbérték beállítva: {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Szürkeskálás küszöbérték – Magyarázat",
        'threshold_guide_text': "A szürkeskálás küszöbérték határozza meg, hogy az intelligens sötét módban mely pixelek számítanak 'szürkének' és invertálódnak.\n\n"
                                "• Az alacsony érték (10%) csak a majdnem tökéletes szürkeárnyalatokat invertálja – a színes elemek teljesen megmaradnak.\n"
                                "• A magas érték (50%) a kissé színes pixeleket is invertálja – ez növeli a kontrasztot, de torzíthatja a színeket.\n\n"
                                "Az optimális érték a dokumentumtól függ. Tiszta szöveges dokumentumokhoz a 30–40% gyakran ideális, színes grafikákhoz inkább 10–20%.\n\n"
                                "Az értéket bármikor módosíthatja a 'Beállítások' menüben – a PDF ezután azonnal újratöltődik.\n\n"
                                "Megjegyzés:\n* A fényképek és képek csak világos módban jeleníthetők meg helyesen!\n* Az invertálási beállítások csak akkor jelennek meg, ha a sötét mód aktív.",
        'threshold_guide_voice': "A szürkeskálás küszöbérték határozza meg, hogy az intelligens sötét mód milyen erősen avatkozik be. Az alacsony érték kíméli a színeket, a magas érték növeli a kontrasztot.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF megnyitása...",
        'progress_loading_document': "Dokumentum betöltése...",
        'progress_pdf_opened': "PDF megnyitva",
        'progress_creating_backup': "Biztonsági másolat készítése...",
        'progress_backup_description': "Eredeti fájl biztosítása...",
        'progress_backup_created': "Biztonsági másolat létrehozva",
        'progress_backup_saved_as': "Mentve mint: {0}",
        'progress_analyzing_start': "Elemzés indítása...",
        'progress_searching_empty': "Üres oldalak keresése...",
        'progress_page_empty': "A(z) {0}. oldal üres",
        'progress_page_keep': "A(z) {0}. oldal megtartása",
        'progress_analysis_complete': "Elemzés befejezve",
        'progress_empty_found': "{0} üres oldal található",
        'progress_current_page': "Aktuális oldal",
        'progress_mark_delete': "Törlésre jelölve",
        'progress_range_selected': "Oldaltartomány {0}-{1}",
        'progress_deleting_pages': "{0} oldal törlése",
        'progress_creating_new_pdf': "Új PDF létrehozása...",
        'progress_transferring_pages': "Oldalak átvitele",
        'progress_keeping_page': "A(z) {0}. oldal megtartva ({1}/{2})",
        'progress_saving_pdf': "PDF mentése...",
        'progress_optimizing': "Fájlméret optimalizálása...",
        'progress_finalizing': "Véglegesítés...",
        'progress_new_size': "Új méret: {0:.2f} MB",
        'progress_cancelling': "Megszakítás...",
        'progress_cancel_message': "{0} megszakítása folyamatban",
        'progress_pages_found_moving': "{0} oldal található, {1} áthelyezendő",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF elemzése...",
        'ocr_status_optimizing': "Képoptimalizálás folyamatban...",
        'ocr_status_recognizing': "Szövegfelismerés folyamatban...",
        'ocr_status_embedding': "Szöveg beágyazása...",
        'ocr_status_finalizing': "PDF véglegesítése...",

        # PDF-Laden
        'progress_preparing': "Előkészítés...",
        'progress_loading': "PDF betöltése...",

        # Seitenoperationen
        'progress_deleting_title': "Oldalak törlése...",
        'progress_moving_title': "Oldalak áthelyezése...",
        'pages_found': "Talált oldalak",
        'progress_creating_new_order': "Új sorrend létrehozása...",
        'progress_sorting_pages': "Oldalak rendezése...",
        'progress_moving_to_begin': "{0} oldal áthelyezése az elejére",
        'progress_transferring_count': "{0} oldal átvitele",
        'progress_transferring_before_target': "Oldalak átvitele a cél előtt",
        'progress_moving_pages': "{0} oldal áthelyezése",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_biztonsagi_mentes_",
        'filename_protected_suffix': "_vedett_",
        'filename_copy_suffix': "_Masolat",
        'filename_page_single': "_Oldal_",
        'filename_page_range': "_Oldalak_",
        'filename_export_page': "_Oldal_{0:03}",
        'filename_export_range': "_Oldalak_{0}-{1}",
        'filename_export_multiple': "_Oldalak_{0}",
        'filename_with_text': "_szoveggel",
        'filename_with_signature': "_alairassal",
        'filename_with_image': "_keppel",
        'filename_with_forms': "_alakzatokkal",
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
        'view_toggle_navbar': "Gombsáv megjelenítése",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Nem törölhető az összes oldal",
		'pages_cannot_delete_last_page': 'Az utolsó oldal nem törölhető!',
		'pages_cannot_delete_all_pages': 'Legalább egy oldalnak maradnia kell a dokumentumban!',
		'delete_pages_confirm': 'Biztosan törölni szeretne {0} oldalt?',
		'delete_pages_confirm_voice': 'Biztosan törölni szeretne {0} oldalt?',
		'pages_deleted': '{0} oldal sikeresen törölve.',
		'warning': 'Figyelmeztetés',
		'error': 'Hiba',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nincs űrlap kiválasztva",
        'form_customized': "Űrlap testreszabva",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Kiválaszt",
        'btn_use': "Használ",
        'master_password_for_spasswords': "Jelszavak tárolásához és használatához először be kell állítani egy mesterjelszót.\n\nSzeretné most beállítani a mesterjelszót?",
        'open_saved_dialog_title': "Mentett fájl megnyitása",
        'open_saved_question': "Szeretné most megnyitni a mentett fájlt?",
        'password': "Jelszó",
        'password_manager_master_required': "A jelszókezelő csak akkor érhető el, ha be van állítva mesterjelszó.\n\nSzeretné most beállítani a mesterjelszót?",
        'password_master_required_for_select': "A mentett jelszavak megtekintéséhez és kiválasztásához először hitelesítenie kell magát a mesterjelszavával.\n\nSzeretné most hitelesíteni magát?",
        'password_not_available': "A kiválasztott jelszó nem elérhető vagy nem sikerült visszafejteni.",
        'password_options_title': "Jelszó beállítások",
        'password_save_choice_change': "Új jelszó beállítása",
        'password_save_choice_keep': "Meglévő jelszó használata",
        'password_save_choice_none': "Titkosítás nélkül mentés",
        'password_save_hint': "Először állítson be egy mesterjelszót a jelszavak biztonságos tárolásához.",
        'password_save_master_required': "Jelszó mentése (csak mesterjelszóval lehetséges)",
        'password_save_question': "Az aktuális PDF jelszóval védett. Szeretné használni a meglévő jelszót, újat beállítani vagy titkosítás nélkül menteni?",
        'password_select': "Jelszó kiválasztása",
        'password_select_none': "Nincs jelszó kiválasztva.\n\nKérjük, válasszon egy jelszót a listából.",
        'password_select_one': "Kérjük, pontosan egy jelszót válasszon.\n\nTöbb jelszót is megjelölt.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_biztonsagi_masolat",
        'filename_insert_suffix': "_beszurassal",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_oldalak_torolve",
        'filename_pages_moved': "_oldalak_atmozgatva",
        'filename_rotated_all_suffix': "_osszes_oldal_forgatva",
        'filename_rotated_suffix': "_oldal_forgatva",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Fájlnevek konfigurálása PDF módosításakor",
        'filename_keep_suffixes': "Korábbi kiterjesztések megtartása (pl. _szoveggel)",
        'filename_keep_suffixes_false': "Csere",
        'filename_keep_suffixes_true': "Megtartás",
        'filename_preview_label': "Fájlnév előnézete:",
        'filename_preview_overwrite_hint': "Előnézet nem elérhető – az eredeti felülírásra kerül.",
        'filename_separator': "Szavak közötti elválasztó",
        'filename_separator_none': "Nincs elválasztó",
        'filename_separator_space': "Szóköz ( )",
        'filename_separator_underscore': "Aláhúzás (_)",
        'filename_settings_saved': "Fájlnév beállítások mentve",
        'filename_settings_title': "Fájlnév formázás és biztonsági másolat",
        'filename_timestamp_position': "Időbélyeg pozíciója",
        'filename_timestamp_position_after': "Az alapnév után",
        'filename_timestamp_position_before': "Legelöl",
        'filename_timestamp_position_end': "A végén",
        'filename_use_timestamp': "Időbélyeg használata",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Viselkedés módosításokkor:</b><ul><li>Oldalak törlése és beszúrása</li><li>Szöveg, aláírás, kép és alakzatok beszúrása</li><li>OCR</li></ul></html>",
        'backup_section': "Biztonsági másolat oldalműveletekhez (Törlés, Áthelyezés)",
        'behavior_info': "Megjegyzés: 'Eredeti felülírása' esetén az időbélyegek és utótagok figyelmen kívül lesznek – a fájl megtartja a nevét.",
        'behavior_new_file': "Mindig új fájl létrehozása (időbélyeggel és utótaggal)",
        'behavior_overwrite': "Eredeti felülírása (nincs új fájl)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Az összes oldal el lett forgatva.\n\nAz eredeti változatlan maradt.\nÚj fájl: {0}",
        'all_pages_rotated_voice': "Az összes oldal elforgatva, új fájl létrehozva.",
        'empty_pages_deleted_new_file': "{0} üres oldal törlésre került.\n\nAz eredeti változatlan maradt.\nÚj fájl: {1}",
        'empty_pages_deleted_voice': "{0} üres oldal törölve, új fájl létrehozva.",
        'ocr_keep_original': "Eredeti megtartása (később kézzel megnyitni)",
        'ocr_new_file_question': "Az új kereshető PDF a következő helyre lett mentve:\n{0}\n\nSzeretné most megnyitni?",
        'ocr_open_new': "Új OCR fájl megnyitása",
        'ocr_original_kept': "Az eredeti fájl nyitva marad. Az OCR fájl elmentésre került.",
        'page_deleted_new_file': "{0}. oldal törlésre került.\n\nAz eredeti változatlan maradt.\nÚj fájl: {1}",
        'page_deleted_voice': "{0}. oldal törölve, új fájl létrehozva.",
        'page_rotated_new_file': "{0}. oldal el lett forgatva.\n\nAz eredeti változatlan maradt.\nÚj fájl: {1}",
        'page_rotated_voice': "{0}. oldal elforgatva, új fájl létrehozva.",
        'pages_deleted_new_file': "{0} oldal törlésre került.\n\nAz eredeti fájl változatlan maradt.\nÚj fájl: {1}",
        'pages_deleted_new_file_voice': "{0} oldal törölve, új fájl létrehozva.",
        'pages_inserted_new_file': "{0} oldal beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nÚj fájl: {1}",
        'pages_inserted_new_file_ask': "{0} oldal beszúrásra került.\n\nAz eredeti változatlan maradt.\nÚj fájl: {1}\n\nSzeretné most megnyitni?",
        'pages_inserted_voice_new': "{0} oldal beszúrva, új fájl létrehozva.",
        'pages_moved_new_file': "{0} oldal áthelyezésre került.\n\nAz eredeti fájl változatlan maradt.\nÚj fájl: {1}",
        'pages_moved_new_file_voice': "{0} oldal áthelyezve, új fájl létrehozva.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ne mutassa többé",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Biztonsági másolat beállítása</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Biztonsági másolat BEKAPCSOLVA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Minden olyan módosításnál, amely felülírja az eredetit</strong> (szöveg, aláírás, kép, alakzat, OCR, forgatás, beszúrás, oldalak törlése/áthelyezése) <strong>automatikusan létrejön egy időbélyeggel ellátott biztonsági másolat</strong> a módosítás alkalmazása előtt.</p>
                <p style="margin: 5px 0 5px 20px;">• A biztonsági másolat az eredeti fájl mellett található (pl. <code>Dokumentum_biztonsagi_masolat_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Ha emellett aktiválta a <strong>„Eredeti felülírása“</strong> opciót, akkor is létrejön a biztonsági másolat.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Biztonsági másolat KIKAPCSOLVA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Nem jön létre biztonsági másolat</strong> – sem felülíráskor, sem oldalműveleteknél.</p>
                <p style="margin: 5px 0 5px 20px;">• Az eredeti fájl felülíráskor helyrehozhatatlanul elveszhet.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Csak tapasztalt felhasználóknak ajánlott!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tipp:</strong> A biztonsági másolat beállítása független az „Eredeti felülírása“ opciótól. Mindkettőt kombinálhatja.<br>
                Ezt az üzenetet véglegesen elrejtheti.
            </div>
        </div>
        """,
        'backup_info_title': "Biztonsági másolat viselkedése",
        'backup_info_voice': "Értesítés a biztonsági másolat viselkedéséről oldalműveleteknél. Biztonsági másolat bekapcsolva felülírja az eredetit, kikapcsolva új fájlt hoz létre.",
        'show_backup_info': "Információ a biztonsági másolat beállításáról",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ne mutassa többé",
        'overwrite_enable_backup': "Biztonsági másolat engedélyezése (ajánlott)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Eredeti felülírása</p>
            <p>Ha engedélyezi ezt az opciót, a módosítások (szöveg, aláírás, kép, alakzat, OCR, forgatás, beszúrás) <strong>közvetlenül az eredetibe kerülnek mentésre</strong> – <strong>nem jön létre új fájl</strong>.</p>
            <p>• A fájlnév változatlan marad.<br>
            • Az időbélyegek és utótagok figyelmen kívül lesznek.<br>
            • <strong>Biztonsági másolat nélkül az eredeti helyrehozhatatlanul elveszhet.</strong></p>
            <p style="color: #FFD700;">Javaslat: Az automatikus biztonsági másolatokhoz engedélyezze ezen felül a biztonsági másolat opciót.</p>
        </div>
        """,
        'overwrite_info_title': "Eredeti felülírása",
        'overwrite_info_voice': "Figyelmeztetés: Eredeti felülírása – nincs új fájl. Biztonsági másolat ajánlott.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} oldal beszúrásra került.\n\nAz eredeti fájl felülírásra került.\nLétrejött egy biztonsági másolat.",
        'pages_inserted_overwrite_no_backup': "{0} oldal beszúrásra került.\n\nAz eredeti fájl felülírásra került.\nNEM jött létre biztonsági másolat.",
        'texts_saved_overwrite_with_backup': "A módosítások az eredetiben lettek mentve.\n\nLétrejött egy biztonsági másolat.",
        'texts_saved_overwrite_no_backup': "A módosítások az eredetiben lettek mentve.\n\nNEM jött létre biztonsági másolat.",
        'texts_crosses_saved_new_file': "{0} {1} és {2} {3} beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nLétrejött egy új fájl.\n\nAz új PDF betöltése...",
        'texts_saved_new_file': "{0} {1} beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nLétrejött egy új fájl.\n\nAz új PDF betöltése...",
        'crosses_saved_new_file': "{0} {1} beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nLétrejött egy új fájl.\n\nAz új PDF betöltése...",
        'elements_saved_new_file': "{0} elem beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nLétrejött egy új fájl.\n\nAz új PDF betöltése...",
        'signatures_saved_overwrite_with_backup': "Az aláírás(ok) az eredetiben lettek mentve.\n\nLétrejött egy biztonsági másolat.",
        'signatures_saved_overwrite_no_backup': "Az aláírás(ok) az eredetiben lettek mentve.\n\nNEM jött létre biztonsági másolat.",
        'images_saved_overwrite_with_backup': "A kép(ek) az eredetiben lettek mentve.\n\nLétrejött egy biztonsági másolat.",
        'images_saved_overwrite_no_backup': "A kép(ek) az eredetiben lettek mentve.\n\nNEM jött létre biztonsági másolat.",
        'forms_saved_overwrite_with_backup': "Az alakzat(ok) az eredetiben lettek mentve.\n\nLétrejött egy biztonsági másolat.",
        'forms_saved_overwrite_no_backup': "Az alakzat(ok) az eredetiben lettek mentve.\n\nNEM jött létre biztonsági másolat.",
        'signatures_saved_new_file': "{0} aláírás beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nLétrejött egy új fájl.\n\nAz új PDF betöltése...",
        'images_saved_new_file': "{0} kép beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nLétrejött egy új fájl.\n\nAz új PDF betöltése...",
        'forms_saved_new_file': "{0} alakzat beszúrásra került.\n\nAz eredeti fájl változatlan maradt.\nLétrejött egy új fájl.\n\nAz új PDF betöltése...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Figyelmeztetés: Ez a PDF elforgatott oldalakat tartalmaz. A pozicionálás eltérhet.",
        'page_rotated_warning_title': "Elforgatott oldal észlelve",
        'page_rotated_warning_message': "Az aktuális {0}. oldal {1}°-kal el van forgatva.\n\nElemek beszúrása elforgatott oldalakon nem támogatott.\n\nSzeretné most egyenes pozícióba forgatni az oldalt?",
        'page_rotated_warning_voice': "Figyelmeztetés: Az oldal el van forgatva. Kérjük, először forgassa el.",
        'paste_on_rotated_page_simple_warning': "Beszúrás a(z) {0}. oldalra nem lehetséges!\n\nEz az oldal {1}°-kal el van forgatva.\n\nKérjük, először forgassa el az oldalt 0°-ra (Menü: Szerkesztés → Oldal igazítása).\n\nFigyelmeztetés:\nA korábban másolt elem elveszik, ha nem ment az oldal elforgatása előtt.",
        'paste_on_rotated_page_voice': "Beszúrás megszakítva. Az oldal el van forgatva. Kérjük, először igazítsa az oldalt.",
        'page_rotated_cancel': "Mégse",
        'page_rotated_rotate_until_upright': "Oldal ismételt elforgatása (amíg egyenes nem lesz)",
        'page_rotated_now_upright': "Az oldal most már egyenes. Most már beszúrhat.",
        'page_rotated_still_not_upright': "Az oldalt nem sikerült egyenes pozícióba forgatni. Kérjük, javítsa kézzel.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Súgó: Elforgatott oldalak javítása",
        'help_rotated_pages_voice': "Megnyílik a súgó az elforgatott oldalak javításához.",
        'btn_help': "Súgó",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Probléma: Elforgatott oldal – A beszúrás nem működik megfelelően</p>

            <p>Ha szövegek, aláírások vagy alakzatok beszúrása elforgatott oldalon nem működik megfelelően, egy külső PDF-szerkesztővel javíthatja az oldalt.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Megoldás külső eszközzel (pl. macOS Előnézet)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Oldal exportálása</strong><br>
                &nbsp;&nbsp;Kattintson a menüben a <strong>Fájl → Exportálás oldalakként</strong> menüpontra, vagy használjon más módszert a kívánt oldal egyetlen PDF-ként történő mentéséhez.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Oldal megnyitása külső programban</strong><br>
                &nbsp;&nbsp;Nyissa meg az exportált PDF-et egy PDF-szerkesztőben (pl. <strong>macOS Előnézet</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Oldal elforgatása</strong><br>
                &nbsp;&nbsp;Forgassa el az oldalt úgy, hogy az egyenes legyen (Előnézetben: <strong>Eszközök → Forgatás</strong> vagy <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Mentés</strong><br>
                &nbsp;&nbsp;Mentse a kijavított oldalt (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Oldal visszaszúrása az eredeti dokumentumba</strong><br>
                &nbsp;&nbsp;Térjen vissza a PDFDarkView-ba, és szúrja be a kijavított oldalt a kívánt pozícióba:<br>
                &nbsp;&nbsp;<strong>Szerkesztés → Oldalak beszúrása</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatíva: Oldal elforgatása az eredetiben</p>
                <p style="margin: 5px 0 5px 20px;">• Használja a beépített forgatási funkciót (<strong>Szerkesztés → Oldal forgatása</strong>) az oldal lépésről lépésre történő javításához.<br>
                • Minden elforgatás után ellenőrizheti, hogy a beszúrás most már működik-e.<br>
                • Ez gyakran a gyorsabb megoldás – először ezt próbálja ki!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tipp:</strong> Ha gyakran találkozik elforgatott oldalakkal, véglegesen elrejtheti a figyelmeztetést a beszúrási párbeszédablakban.<br>
                A pozicionálás ekkor eltérhet – ezt az opciót csak akkor használja, ha ismeri a következményeket.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Oldalak igazítása",
        'menu_rotate_normalize_tooltip': "Oldal elforgatása vagy visszaállítás 0°-ra",
        'normalize_current_page': "Aktuális oldal egyenes pozícióba hozása (0°-ra állítás)",
        'normalize_all_pages': "Összes oldal egyenes pozícióba hozása (0°-ra állítás)",
        'page_normalized': "A(z) {0}. oldal egyenes pozícióba lett állítva.",
        'all_pages_normalized': "Az összes oldal egyenes pozícióba lett állítva.",
        'page_already_upright': "A(z) {0}. oldal már egyenes.",
        'all_pages_already_upright': "Az összes oldal már egyenes.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>A PDF nem tartalmaz kereshető szöveget.</p><p>Szeretne OCR-t végezni a {0} exportálásához?</p>",
        'export_ocr_voice': "A PDF nem tartalmaz szöveget. OCR szükséges a {0} exportálásához.",
        'export_no_ocr_possible': "Exportálás OCR nélkül nem lehetséges. Kérjük, végezzen OCR-t a menün keresztül.",
        'ocr_failed_export_not_possible': "Az OCR sikertelen. Az exportálás nem végezhető el.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "A PDF megnyílik az Előnézetben. Kérjük, ott indítsa el a nyomtatási folyamatot.",
        'print_preview_manual': "A PDF megnyílt. Kérjük, hajtsa végre a nyomtatási parancsot manuálisan (pl. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDF-ek egyesítése",
        'merge_pdfs': "PDF-ek egyesítése",
        'merge_progress_title': "PDF-ek egyesítése folyamatban...",
        'merge_pdfs_list': "PDF-ek sorrendben (Rendezze húzással)",
        'merge_add_pdf': "PDF hozzáadása",
        'merge_remove': "Eltávolítás",
        'merge_move_up': "Fel",
        'merge_move_down': "Le",
        'merge_pdfs_info': "💡 Tipp: A sorrendet húzással megváltoztathatja",
        'merge_no_pdfs': "Nincs PDF kiválasztva. Kattintson a 'PDF hozzáadása' gombra.",
        'merge_info': "{0} PDF kiválasztva (kb. {1} oldal)",
        'merge_open_file': "Fájl megnyitása",
        'merge_merge': "Egyesítés",
        'merge_error': "Hiba az egyesítés során",
        'merge_min_two_pdfs_error': "Kérjük, legalább két PDF-fájlt válasszon ki az egyesítéshez.",
        'merge_select_pdfs': "PDF-ek kiválasztása egyesítéshez",
        'merge_error_file': "Hiba a feldolgozás során",
        'merge_cancelled': "Az egyesítés meg lett szakítva",
        'merge_preparing': "Előkészítés...",
        'merge_processing': "{1} PDF-ből a(z) {0}. feldolgozása",
        'merge_saving': "Egyesített PDF mentése...",
        'merge_complete': "Kész!",
        'merge_success_title': "Egyesítés sikeres",
        'merge_success_voice': "{0} PDF sikeresen egyesítve.",
        'merge_success_message': "{0} PDF sikeresen egyesítve.\n\nAz új dokumentum most {1} oldalt tartalmaz.\n\nÚj fájl:\n{2}\n\nMentési hely:\n{3}\n{2}\n\nSzeretné megnyitni ezt a PDF-et?",
        'replace_file_title': "Fájl cseréje?",
        'replace_file_message': "Már van egy PDF nyitva. Szeretné lecserélni az új fájlra?",
        'btn_yes': "Igen",
        'btn_no': "Nem",
        'filename_merge_suffix': "egyesitett",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "{0} megnyitása...",
        'progress_merge_reading': "{0} olvasása...",
        'progress_merge_adding': "{0} oldal hozzáadása...",
        'progress_merge_optimizing': "PDF optimalizálása...",
        'progress_merge_writing': "PDF írása...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "a PDF bezárását",
        'action_close_window': "az ablak bezárását",
        'action_open_new_pdf': "egy új PDF megnyitását",
        'action_quit_app': "az alkalmazásból való kilépést",
        'changes_saved': "A módosítások el lettek mentve.",
        'file_close_title': "PDF fájl bezárása",
        'save_before_action': "Menteni kell a módosításokat a {0} előtt? Igen vagy Nem?",
        'save_before_action_voice': "Menteni kell a módosításokat a {0} előtt? Igen vagy Nem?",
        'save_before_close_question': "Menteni kell a módosításokat bezárás előtt? Igen vagy Nem?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Kereshető PDF létrehozva:\n\n{0}\n\n<b>ha szükséges, próbálja újra",
        "ocr_rotate_title": "Oldalak igazítása OCR előtt",
        "ocr_rotate_question": "A PDF elforgatott oldalakat tartalmaz.\nSzeretné az összes oldalt 0°-ra igazítani az OCR előtt?\nEz jelentősen javítja a szövegfelismerést.",
        "ocr_rotate_yes": "Igen, igazítsa",
        "ocr_rotate_no": "Nem, indítsa az OCR-t közvetlenül",
        "ocr_rotate_voice": "A PDF elforgatott oldalakat tartalmaz. Igazítani kell az összes oldalt az OCR előtt?",
        "ocr_not_performed_message": "Nincs szöveg. Kérjük, végezzen OCR-t („Szerkesztés” menü → „OCR végrehajtása” vagy Ctrl+R billentyű).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR beállítások",
        "ocr_language_btn": "OCR nyelv kiválasztása",
        "ocr_language": "OCR nyelv(ek)",
        "ocr_language_current": "Aktuális nyelv:",
        "ocr_param_info": "Információ a paraméterről",

        "ocr_force_ocr_label": "OCR kényszerítése",
        "ocr_deskew_label": "Ferdeesés korrekciója",
        "ocr_clean_label": "Kép tisztítása",
        "ocr_oversample_label": "Felbontás (DPI)",
        "ocr_pagesegmode_label": "Oldal felosztása",
        "ocr_oem_label": "OCR motor mód",
        "ocr_optimize_label": "PDF tömörítés",
        "ocr_jobs_label": "Párhuzamos folyamatok",
        "ocr_verbose_label": "Napló részletessége",

        "ocr_force_ocr_tooltip": "OCR kényszerítése minden oldalon, még akkor is, ha már van szöveg",
        "ocr_deskew_tooltip": "Ferde szkennelt képek automatikus igazítása",
        "ocr_clean_tooltip": "Zaj és műtermékek eltávolítása a képből",
        "ocr_oversample_tooltip": "Kép nagyítása OCR előtt erre a DPI-re",
        "ocr_pagesegmode_tooltip": "Meghatározza, hogy az oldal hogyan legyen szövegterületekre osztva",
        "ocr_oem_tooltip": "Kiválasztja a Tesseract OCR motorját",
        "ocr_optimize_tooltip": "A kimeneti PDF tömörítési szintje",
        "ocr_jobs_tooltip": "Párhuzamos OCR folyamatok száma",
        "ocr_verbose_tooltip": "A napló kimenet részletességének szintje",
        "ocr_settings_explain_btn": "Magyarázat",

        "ocr_force_ocr_explain": "Kényszeríti a szövegfelismerést <b>minden</b> oldalon, még akkor is, ha az már tartalmaz szöveget.\n\nJavaslat: <b>Be</b> a szkennelt PDF-eknél, <b>Ki</b> a már meglévő szöveggel rendelkező natív PDF-eknél.",

        "ocr_deskew_explain": "Kijavítja az enyhén ferde szkenneléseket (kb. 5°-ig).\n\nJavaslat: <b>Be</b> a szkennelt dokumentumoknál, <b>Ki</b> ha az oldalak már tökéletesen egyenesek.",

        "ocr_clean_explain": "Eltávolítja a zajt, pontokat és apró műtermékeket a képből.\n<b>FONTOS:</b> Az arab, thai vagy vietnámi szövegeknél, amelyek diakritikus jeleket tartalmaznak (pontok a betűk felett/alatt), ezt az opciót <b>ki kell kapcsolni</b>, különben fontos karakterek elveszhetnek.",

        "ocr_oversample_explain": "A képet <b>a szövegfelismerés előtt</b> a megadott DPI-re nagyítja.<br><br>• <b>72-150 DPI:</b> Nagyon gyors, de alacsony felismerési arány<br>• <b>200-300 DPI:</b> Optimális tartomány (Alapértelmezett: 300)<br>• <b>400+ DPI:</b> Alig jobb felismerés, de lényegesen nagyobb fájlok<br><br>Javaslat: 300 DPI az összetett írásokhoz (arab, kínai, japán), 200 DPI a nyugati nyelvekhez.",

        "ocr_pagesegmode_explain": "Meghatározza, hogy a Tesseract hogyan osztja fel az oldalt szövegterületekre.\n\n• <b>3 - Automatikus (Alapértelmezett):</b> Jó a vegyes elrendezésekhez\n• <b>4 - Egyetlen oszlop:</b> Egyszlopos szövegekhez\n• <b>5 - Függőleges blokk:</b> Függőleges írásokhoz (japán, kínai)\n• <b>6 - Egységes szövegblokk:</b> Optimális oszlopok nélküli folyamatos szöveghez\n• <b>11 - Nyers kép:</b> Rossz szkennelésekhez / kézírásokhoz\n\nJavaslat: <b>6</b> az egyszerű szöveges dokumentumokhoz, <b>3</b> az összetett elrendezésekhez.",

        "ocr_oem_explain": "Kiválasztja a Tesseract OCR motorját.\n\n• <b>0 - Legacy:</b> Régi motor (gyors, de kevésbé pontos)\n• <b>1 - LSTM:</b> Neurális motor (lassabb, de pontosabb)\n• <b>2 - Legacy + LSTM:</b> Kombinálja mindkét eredményt\n• <b>3 - Alapértelmezett (LSTM előnyben részesítve):</b> A legjobb választás a legtöbb esetben\n\nJavaslat: <b>3</b> a maximális felismerési pontossághoz.",

        "ocr_optimize_explain": "Tömöríti a kimeneti PDF-et.\n\n• <b>0:</b> Nincs optimalizálás (leggyorsabb feldolgozás)\n• <b>1:</b> Könnyű optimalizálás (jó kompromisszum)\n• <b>2:</b> Mérsékelt optimalizálás\n• <b>3:</b> Erős optimalizálás (legkisebb fájl, de lassabb)\n\nJavaslat: <b>1</b> a mindennapi használatra.",

        "ocr_jobs_explain": "A párhuzamos OCR folyamatok száma.\n\n• <b>1:</b> Lassú, de a legalacsonyabb memóriafogyasztás\n• <b>4-8:</b> Optimális a modern többmagos processzorokhoz\n• <b>12+:</b> Alig gyorsabb feldolgozás magas memóriahasználat mellett\n\nJavaslat: A CPU magok száma (pl. <b>4</b> a 4 magos rendszereken).",

        "ocr_verbose_explain": "A napló kimenet részletességének szintje a konzolban.\n\n• <b>0:</b> Nincs kimenet\n• <b>1:</b> Folyamat és állapotüzenetek\n• <b>2:</b> Részletes kimenet\n• <b>3:</b> Teljes hibakeresési kimenet (nagyon terjedelmes)\n\nJavaslat: <b>1</b> a normál működéshez.",

        "ocr_reset_title": "Beállítások visszaállítva",
        "ocr_reset_message": "Az összes OCR beállítás vissza lett állítva az alapértelmezett értékekre.",
        "info_tooltip": "További információk erről a paraméterről",
        "ocr_reset_defaults": "Visszaállítás az alapértelmezettre",

        "ocr_psm_0": "Automatikus (Legacy motor)",
        "ocr_psm_1": "Automatikus oszlopfelismerés",
        "ocr_psm_3": "Automatikus (Alapértelmezett)",
        "ocr_psm_4": "Egyetlen oszlop",
        "ocr_psm_5": "Függőleges blokk",
        "ocr_psm_6": "Egységes szövegblokk",
        "ocr_psm_7": "Egyetlen szövegsor",
        "ocr_psm_8": "Egyetlen szó",
        "ocr_psm_11": "Nyers kép (elrendezés elemzése nélkül)",

        "ocr_oem_0": "Legacy motor (gyors)",
        "ocr_oem_1": "LSTM motor (neuronális, pontos)",
        "ocr_oem_2": "Legacy + LSTM kombinált",
        "ocr_oem_3": "Alapértelmezett (LSTM előnyben)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR nyelv(ek)...",
        "ocr_language_title": "OCR nyelv(ek) kiválasztása",
        "ocr_language_instruction": "Válassza ki a nyelv(ek)et a szövegfelismeréshez (OCR).\nFigyelem: A több nyelv a teljesítmény és a pontosság rovására megy!\nA legjobb eredményeket akkor éri el, ha csak egy nyelvet választ.",
        "ocr_language_predefined": "Előre meghatározott kombinációk",
        "ocr_language_custom": "Egyéni...",
        "ocr_language_selected": "Kiválasztott OCR nyelvek",
        "ocr_language_changed": "OCR nyelv módosítva erre: {0}",
        "ocr_language_auto_detect": "Az elérhető nyelvek automatikusan felismerésre kerülnek.",
        "ocr_language_none_found": "Nem található Tesseract nyelvi adat! Kérjük, telepítse a nyelvi csomagokat (pl. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Egyéni nyelvválasztás",
        "ocr_language_available": "Elérhető nyelvek (telepítve):",
        "ocr_language_select_hint": "Válasszon egy vagy több nyelvet:",
        "ocr_language_confirm": "Alkalmaz",
        "ocr_language_reset": "Visszaállítás az alapértelmezettre (deu+eng+vie)",
        "ocr_language_priorities": "Ajánlott nyelvek (előtelepített):",

        "select_all_languages": "Összes kiválasztása",
        "clear_all_languages": "Kijelölés törlése",
        "install_language_packs": "Hiányzó nyelvi csomagok telepítése...",
        "install_hint": "💡 Tipp: Nem minden nyelv van telepítve a rendszerére. Ezen a gombon keresztül segítséget kap a telepítéshez.",
        "ocr_language_install_title": "Tesseract nyelvi csomagok telepítése",

        "ocr_missing_languages": "Hiányzó OCR nyelvi csomagok",
        "ocr_missing_languages_message": "A következő kiválasztott nyelvek nincsenek telepítve a rendszerére:\n\n{0}\n\nKérjük, telepítse a hiányzó nyelvi csomagokat (lásd a súgót a 'Telepítési súgó' alatt).\n\nSzeretné most megnyitni a telepítési súgót?",
        "ocr_missing_languages_voice": "Hiányzó nyelvi csomagok. Kérjük, telepítse a hiányzó nyelveket.",
        "ocr_install_help_now": "Súgó megnyitása",
        "ocr_continue_anyway": "Mindenképpen próbálkozzon",
        "ocr_language_error_title": "OCR nyelvi hiba",
        "ocr_language_error_message": "Hiba a szövegfelismerés során: {0}\n\nKérjük, ellenőrizze OCR nyelvi beállításait (Beállítások → OCR nyelv).",
        "ocr_install_help_button": "Telepítési súgó",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract nyelvi csomagok telepítése</p>

        <p>Ahhoz, hogy az OCR egy adott nyelven működjön, a megfelelő nyelvi adatoknak telepítve kell lenniük a rendszerére. Kövesse az operációs rendszerére vonatkozó utasításokat:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Nyissa meg a <strong>Terminált</strong> (Finder → Programok → Segédprogramok → Terminál).</li>
        <li>Telepítse az összes elérhető nyelvet a következővel:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Ez eltarthat néhány percig.)</li>
        <li>Vagy csak egyedi nyelveket (pl. vietnámi):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        A jelenlegi Homebrew verzióknál előfordulhat, hogy a <code>*.traineddata</code> fájlt manuálisan kell letölteni (lásd alább).</li>
        <li>Telepítés után: Zárja be ezt a párbeszédablakot, és nyissa meg újra az OCR nyelvválasztót – az új nyelvek automatikusan megjelennek.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Nyisson meg egy terminált (Ctrl+Alt+T).</li>
        <li>Telepítse a kívánt nyelvet, pl. vietnámihoz:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Fontos nyelvkódok: <code>deu</code> (német), <code>eng</code> (angol), <code>vie</code> (vietnámi), <code>spa</code> (spanyol), <code>fra</code> (francia), <code>ita</code> (olasz), <code>nld</code> (holland), <code>fin</code> (finn), <code>swe</code> (svéd), <code>nor</code> (norvég).</li>
        <li>Az összes elérhető csomag megjelenítése:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuális)</p>
        <ol>
        <li>Töltse le a kívánt <code>*.traineddata</code> fájlokat a következő címről:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (pl. <code>vie.traineddata</code> a vietnámihoz).</li>
        <li>Másolja a fájlokat a Tesseract nyelvi mappájába, általában:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Igazítsa az egyéni telepítéshez.)</li>
        <li>Indítsa újra az alkalmazást (vagy nyissa meg újra az OCR nyelvválasztót).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatíva minden rendszerhez</p>
        <ul>
        <li>Telepítse az <strong>OCRmyPDF</strong> és a <strong>Tesseract</strong> programokat az Ön által választott csomagkezelővel. A legtöbb telepítés már tartalmaz néhány szabványos nyelvet (angol, német, francia).</li>
        <li>A hiányzó nyelvek bármikor telepíthetők – az OCR nyelvválasztó csak a ténylegesen létező nyelveket sorolja fel.</li>
        </ul>

        <hr>
        <p><b>✅ Telepítés után:</b> Nem szükséges az alkalmazás újraindítása – az újonnan hozzáadott nyelvek azonnal megjelennek a listában.</p>
        <p><b>📖 Segítség a nyelvkódokhoz:</b> A teljes lista megtalálható a <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract dokumentációjában</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans betűtípusok",
        "info_noto_font_voice": "Noto Sans betűtípusok telepítési útmutatója",
        "btn_info_noto_font_install": "Betűtípus információ",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ A Google ingyenes Noto betűtípusainak telepítése</h2>

        <p>A <strong>Noto betűtípusok</strong> a Google nyílt forráskódú betűtípuscsaládja. Céljuk, hogy ne lássanak <em>"tofut"</em> (azaz üres dobozokat □), és hogy a Unicode szabvány minden karakterét helyesen jelenítsék meg. Ideális kiegészítői azoknak az alkalmazásoknak, amelyeknek sok különböző nyelven kell szövegeket megjeleníteniük.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Telepítés macOS rendszeren</h3>

        <p><strong>1. módszer: Homebrew használatával (haladóknak)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>2. módszer: A "Font Book" segítségével (Ajánlott)</strong></p>

        <ol>
        <li>Töltse le a hivatalos betűtípus-csomagot:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Csomagolja ki a ZIP fájlt</li>
        <li>Másolja a fájlokat ide: <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Telepítés Windows rendszeren (10 és 11)</h3>

        <p><strong>1. módszer: Microsoft Store (Ajánlott)</strong><br>
        Keressen rá, hogy "Google Noto Fonts" vagy "Noto Sans", majd kattintson a <strong>Telepítés</strong> gombra.</p>

        <p><strong>2. módszer: Manuális telepítés</strong></p>

        <ol>
        <li>Letöltés:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP kibontása</li>
        <li>Válassza ki a .ttf / .otf fájlokat</li>
        <li>Jobb gomb → <strong>Telepítés</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        vagy<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Név\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Telepítés Linux rendszeren</h3>

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

        <p>Ellenőrzés:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Könyvjelzők kezelése",
        "bookmark_add": "Könyvjelző hozzáadása",
        "bookmark_add_tooltip": "Aktuális oldal mentése könyvjelzőként",
        "bookmark_remove": "Könyvjelző eltávolítása",
        "bookmark_remove_tooltip": "A megjelölt könyvjelző törlése",
        "bookmark_remove_all": "Összes eltávolítása",
        "bookmark_remove_all_tooltip": "A PDF összes könyvjelzőjének törlése",
        "bookmark_jump": "Ugrás a könyvjelzőre",
        "bookmark_jump_tooltip": "Ugrás a kiválasztott oldalra",
        "bookmark_name": "Név",
        "bookmark_page": "Oldal",
        "bookmark_no_bookmarks": "Nincsenek könyvjelzők.\nKattintson a 'Hozzáadás' gombra az aktuális oldal könyvjelzőként való mentéséhez.",
        "bookmark_added": "Könyvjelző hozzáadva a(z) {0}. oldalhoz: {1}",
        "bookmark_removed": "Könyvjelző eltávolítva: {0}",
        "bookmark_all_removed": "Az összes könyvjelző eltávolításra került.",
        "bookmark_name_default": "{0}. oldal",
        "bookmark_name_prompt": "A könyvjelző neve:\n(a hosszú szöveg 50 karakterre rövidül)",
        "bookmark_name_prompt_title": "Könyvjelző neve",
        "bookmark_confirm_remove_all": "Biztosan el kívánja távolítani az összes ({0}) könyvjelzőt?",
        "menu_bookmarks": "Könyvjelzők",
        "bookmark_manage": "Könyvjelzők kezelése",
        "bookmark_next": "Következő könyvjelző",
        "bookmark_prev": "Előző könyvjelző",
        "bookmark_page_display": "{0}. oldal",
        "bookmark_exists": "Ehhez az oldalhoz már létezik könyvjelző ezzel a névvel.",
        "bookmark_select_first": "Először válasszon ki egy könyvjelzőt.",
        "bookmark_confirm_remove": "Biztosan el kívánja távolítani a(z) '{0}. oldal: {1}' könyvjelzőt?",
        "bookmark_jumped_to": "Ugrás a(z) '{0}' könyvjelzőre a(z) {1}. oldalon.",
        "bookmark_jumped_to_voice": "{0} könyvjelző, {1}. oldal",
        "btn_close": "Bezárás",

        "bookmark_list": "Az Ön könyvjelzői",
        "bookmark_rename": "Könyvjelző átnevezése",
        "bookmark_rename_tooltip": "A kiválasztott könyvjelző nevének megváltoztatása",
        "bookmark_rename_title": "Könyvjelző átnevezése",
        "bookmark_rename_prompt": "Új név a(z) {0}. oldalon lévő könyvjelzőhöz:\n(max. 50 karakter)",
        "bookmark_renamed": "A(z) '{0}' könyvjelző átnevezve '{1}' névre.",
        "bookmark_item_tooltip": "{0}. oldal: {1}\nKattintson duplán az ugráshoz",
        "bookmark_name_exists_question": "Már létezik '{0}' nevű könyvjelző ezen az oldalon.\nMindenképpen átnevezi?",

        "context_bookmarks": "Könyvjelzők",
        "context_bookmark_add_here": "Könyvjelző hozzáadása ehhez az oldalhoz",
        "context_bookmarks_existing": "Meglévő könyvjelzők:",
        "context_bookmarks_jump": "Ugrás a könyvjelzőre:",
        "context_bookmarks_none": "Nincsenek könyvjelzők",
        "context_bookmarks_clear_all": "Mind a {0} könyvjelző eltávolítása",

        "bookmark_search_placeholder": "Könyvjelzők keresése... (név vagy oldal)",
        "bookmark_search_results": "%d könyvjelző található a következőre: \"%s\"",
        "bookmark_no_search_results": "Nem található könyvjelző a következőre: \"%s\"",
        "bookmark_no_search_results_label": "Nincs találat a következőre: \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF metaadatok szerkesztése",
        "metadata_title": "Cím",
        "metadata_title_placeholder": "Dokumentum címe",
        "metadata_title_tooltip": "A dokumentum címe (a címsorban jelenik meg)",
        "metadata_author": "Szerző",
        "metadata_author_placeholder": "A szerző neve",
        "metadata_author_tooltip": "A dokumentum létrehozója",
        "metadata_subject": "Tárgy",
        "metadata_subject_placeholder": "A dokumentum tárgya",
        "metadata_subject_tooltip": "A tartalom rövid leírása",
        "metadata_keywords": "Kulcsszavak",
        "metadata_keywords_placeholder": "Vesszővel elválasztott kulcsszavak",
        "metadata_keywords_tooltip": "Kulcsszavak a dokumentum kategorizálásához",
        "metadata_creator": "Létrehozó",
        "metadata_creator_placeholder": "A PDF-et létrehozó alkalmazás",
        "metadata_creator_tooltip": "A szoftver, amellyel a dokumentum készült",
        "metadata_producer": "Gyártó",
        "metadata_producer_placeholder": "A PDF-et konvertáló alkalmazás",
        "metadata_producer_tooltip": "A szoftver, amely konvertálta a PDF-et",
        "metadata_creation_date": "Létrehozás dátuma",
        "metadata_creation_date_tooltip": "A dokumentum létrehozásának dátuma",
        "metadata_mod_date": "Módosítás dátuma",
        "metadata_mod_date_tooltip": "Az utolsó módosítás dátuma",
        "metadata_pdf_info": "📄 PDF információk",
        "metadata_pages": "Oldalszám",
        "metadata_file_size": "Fájlméret",
        "metadata_pdf_version": "PDF verzió",
        "metadata_encrypted": "Titkosított",
        "metadata_encrypted_yes": "Igen (jelszóval védett)",
        "metadata_encrypted_no": "Nem",
        "metadata_reload": "📂 Újratöltés PDF-ből",
        "metadata_reset": "Változások elvetése",
        "metadata_reloaded": "A metaadatok újratöltődtek a PDF-ből.",
        "metadata_reset_done": "Az összes metaadat mező visszaállításra került.",
        "metadata_no_file": "Nincs betöltve PDF fájl.",
        "metadata_save_error": "Hiba a metaadatok mentésekor",
        "metadata_saved": "A metaadatok sikeresen elmentve.",
        "metadata_pdf_version_unknown": "PDF (ismeretlen)",
        "metadata_saved_message": "A metaadatok sikeresen elmentve.",
        "metadata_saved_voice": "Metaadatok elmentve.",

        "metadata_custom": "🔧 Egyéni metaadatok",
        "metadata_custom_placeholder": "{\n  \"sajat_mezo\": \"sajat_ertek\",\n  \"masik_mezo\": 123\n}",
        "metadata_custom_tooltip": "JSON formátum egyéni metaadatokhoz (opcionális)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Sablon kiválasztva: \"{0}\" - Kattintson duplán a beillesztéshez",
        "text_use_template": "Szövegblokk használata",
        "text_type": "Típus",
        "text_search_templates": "Szövegblokkok keresése...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Exportálási / Importálási információk",
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

        <h3>📦 Mit exportálunk? (Áttekintés)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Általános alkalmazásbeállítások</span></li>
            <li class="detail">• Sötét/Világos mód</li>
            <li class="detail">• Sötét mód invertálása képekhez</li>
            <li class="detail">• Szürke küszöbérték</li>
            <li class="detail">• Nyelv</li>
            <li class="detail">• Ablak geometria</li>
            <li class="detail">• Nagyítási mód</li>
            <li class="detail">• Navigáció (Navigációs sáv látható)</li>
            <li class="detail">• Beszédkimenet (be/ki)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Biztonsági mentési beállítások</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Fájl elnevezése (Időbélyeg, Elválasztó, Utótagok)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Beillesztések beállításai</span></li>
            <li class="detail">• Aláírások</li>
            <li class="detail">• Szöveg és szövegblokkok</li>
            <li class="detail">• X-ek, képek és alakzatok</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR beállítások</span></li>
            <li class="detail">• Nyelv</li>
            <li class="detail">• OCR kényszerítése · Oldalmód</li>
            <li class="detail">• Kép előfeldolgozása: Ferdeség korrekció, Tisztítás, Túlmintavételezés</li>
            <li class="detail">• Párhuzamos feladatok száma</li>
            <li class="detail">• Invertálási mód</li>
            <li class="detail">• Szürke küszöbérték</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Könyvjelzők</span></li>
            <li class="detail">• Összes könyvjelző PDF fájlonként (Oldal, Név, Létrehozási idő)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Jelszó adatbázis</span></li>
            <li class="detail">• Mentett PDF jelszavak (opcionálisan titkosítva vagy egyszerű szövegként)</li>
            <li class="detail">• Mesterjelszó hash (ha be van állítva)</li>
            <li class="detail">• Ellenőrző adatok</li>
        </ul>

        <h4>⚠️ Fontos tudnivalók</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Importáláskor:</strong>
            <ul>
                <li><span class="warning">➜ Az ÖSSZES aktuális beállítás teljesen felülíródik</span></li>
                <li>• Az alkalmazás újraindítása kötelező</li>
                <li>• A meglévő aláírások, szövegblokkok és könyvjelzők lecserélődnek</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Mesterjelszó és exportálási mód:</strong>
            <ul>
                <li>• Aktív mesterjelszó esetén választhat:</li>
                <li>  - <span style="color: #98FB98;"><strong>Visszafejtett</strong></span> (a jelszavak egyszerű szövegként vannak a ZIP-ben)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Titkosított</strong></span> (csak a mesterjelszóval olvasható a célrendszeren)</li>
                <li>• A mesterjelszó hash <strong>mindig</strong> titkosítva kerül tárolásra</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Biztonsági figyelmeztetés:</strong>
            <ul>
                <li>• Az exportált ZIP fájl érzékeny adatokat tartalmaz (<strong>jelszavak, könyvjelzők, aláírások</strong>)</li>
                <li>• Kérjük, biztonságos helyen tárolja (pl. titkosított USB stick, jelszókezelő)</li>
                <li>• Ha a fájl elveszik, a mentett PDF jelszavak visszavonhatatlanul elvesznek</li>
            </ul>
        </div>

        <h4>📁 Exportálási formátum</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            A beállítások egyetlen ZIP fájlba kerülnek mentésre:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ez a ZIP tartalmazza a teljes <code>settings.json</code> fájlt (az Ön konfigurációjából), valamint esetleges beágyazott aláírás képfájlokat és titkosított jelszavakat.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Aláírások - Útmutató",
        'signature_guide_html': """
        📝 <strong>Aláírások - Gyors útmutató</strong><br>
        <ul>
        <li>Fő jelszó beállítása</li>
        <li>Aláírások konfigurálása a <em>Beállítások</em> menüben (méret, időbélyeg, …)</li>
        <li>Beszúrás <strong>JOBB KLIKKEL</strong> a kívánt pozícióba (fő jelszó munkamenetenként egyszer szükséges)</li>
        <li>Aláírás mozgatása egérrel vagy nyílbillentyűkkel</li>
        <li>Több aláírás egymás utáni beszúrása</li>
        <li>Minden aláírás egyedi testreszabása</li>
        <li>Egyedi aláírás elvetése</li>
        <li>Összes aláírás egyidejű mentése / elvetése</li>
        <li>Alternatív megoldásként a menüsor is használható.</li>
        </ul>
        """,
        'signature_guide_voice': "Gyors útmutató aláírásokhoz. Fő jelszó beállítása. Aláírások konfigurálása a beállításokban. Beszúrás jobb klikkel.",

        'image_guide_title': "Képek beszúrása - Útmutató",
        'image_guide_html': """
        📷 <strong>Képek beszúrása PDF-be - Gyors útmutató</strong><br>
        <ol>
        <li>Jobb klikk a kívánt pozícióban</li>
        <li><em>„Kép beszúrása“</em> → Kép kiválasztása</li>
        <li>Kép pozicionálása: Húzza az egérrel</li>
        <li>Méret módosítása: Húzza a sarkoknál/széleknél</li>
        <li>Képarány megtartása: <strong>[A]</strong> billentyű</li>
        <li>További beállítások: Jobb klikk a képen</li>
        </ol>
        <p><strong>Tipp:</strong> A helyi menüben módosíthatja a beállításokat.</p>
        """,
        'image_guide_voice': "Gyors útmutató képekhez. Jobb klikk, kép beszúrása, válasszon. Pozicionálás egérrel, méret módosítása a sarkoknál. Képarány A billentyűvel.",

        'form_guide_title': "Alakzatok beszúrása - Útmutató",
        'form_guide_html': """
        📐 <strong>Alakzatok beszúrása PDF-be - Gyors útmutató</strong><br>
        <ol>
        <li>Alakzat típusának kiválasztása (téglalap, ellipszis, vonal, nyíl)</li>
        <li>Kattintson a pozícióra:
            <ul>
            <li>Téglalap/ellipszis esetén: Egy kattintás elhelyezi az alakzatot</li>
            <li>Vonal/nyíl esetén: Két kattintás a kezdő- és végponthoz</li>
            </ul>
        </li>
        <li>Alakzat pozicionálása: Húzza az egérrel</li>
        <li>Méret módosítása: Húzza a sarkoknál/széleknél</li>
        <li>Alakzat mentése: <strong>Enter</strong></li>
        <li>Alakzat elvetése: <strong>ESC</strong></li>
        <li>További beállítások: Jobb klikk az alakzaton</li>
        </ol>
        <p><strong>Tipp:</strong> A helyi menüben módosíthatja a beállításokat.</p>
        """,
        'form_guide_voice': "Gyors útmutató alakzatokhoz. Válassza ki az alakzat típusát. Téglalap vagy ellipszis esetén kattintson egyszer, vonal vagy nyíl esetén kétszer. Pozicionálás egérrel, méret módosítása a sarkoknál. Mentés Enterrel, elvetés Escapvel.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "előző",
        "btn_next_result": "következő",
        "ocr_text_window": "OCR szövegablak",
        "bookmark_existing": "Meglévő könyvjelzők",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR összehasonlítás Mac - Windows",
        'ocr_method_mac_win_title': "OCR különbségek Mac és Windows között",
        'ocr_method_mac_win_voice': "A Mac jobb",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Különbségek a macOS és a Windows között</strong></p>

        <p><strong>macOS (ajánlott)</strong></p>
        <p>Eszköz:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Eredmény:</p>
        <ul>
        <li>Kereshető PDF beágyazott szöveggel, amely nagyrészt megőrzi az eredeti elrendezést.</li>
        </ul>
        <p>Előnyök:</p>
        <ul>
        <li>Kiváló szövegfelismerési minőség (még ferde oldalakon is).</li>
        <li>Vektorgrafikák és betűtípusok megtartása.</li>
        <li>GUI folyamatjelző sáv alprocessz értékelésen keresztül.</li>
        <li>Teljes körű vezérlés az összes OCR paraméter felett (Deskew, Clean, Oversample, optimalizálás).</li>
        <li>A szöveges keresés közvetlenül a főablakban (PDF nézet) érhető el.</li>
        </ul>
        <p>Hátrányok:</p>
        <ul>
        <li>További rendszereszközöket igényel (ocrmypdf, Ghostscript, unpaper, pngquant – az App Bundle tartalmazza).</li>
        <li>Bonyolultabb hibakezelés (holtpontok, időtúllépések).</li>
        </ul>

        <p><strong>Windows (stabil alternatíva)</strong></p>
        <p>Eszköz:</p>
        <ul>
        <li>pytesseract (közvetlen kapcsolat a Tesseracthez) + reportlab + PyPDF2</li>
        </ul>
        <p>Eredmény:</p>
        <ul>
        <li>Kereshető PDF, amely vizuálisan egy kép-PDF-nek felel meg, de az átlátszó szöveg révén kereshető.</li>
        </ul>
        <p>Előnyök:</p>
        <ul>
        <li>Egy sem jut eszembe jelenleg.</li>
        </ul>
        <p>Hátrányok:</p>
        <ul>
        <li>A PDF lényegében egy kép láthatatlan szöveggel; az elrendezés összetett dokumentumoknál (oszlopok, táblázatok) kissé eltérhet.</li>
        <li>Nincs automatikus ferdeségkorrekció (--deskew) vagy képtisztítás (--clean).</li>
        <li>A GUI folyamatjelző sáv csak durván frissül a feldolgozott oldalak száma alapján.</li>
        <li>Az OCR sebessége kissé lassabb (mivel minden oldalt külön dolgoz fel).</li>
        <li>A szöveges keresés az OCR szövegablakba kerül átirányításra.</li>
        </ul>

        <p><strong>Közös jellemzők</strong></p>
        <ul>
        <li>Mindkét eljárás kereshető PDF-et hoz létre a forrásfájllal azonos könyvtárban.</li>
        <li>Az OCR beállítások (nyelv, DPI, oldalszegmentálási mód, OCR motor mód) az OCRSettingsDialog segítségével konfigurálhatók, és mindkét implementációban érvényesek.</li>
        </ul>

        <p><strong>Ajánlás:</strong></p>
        <ul>
        <li>macOS: Az ocrmypdf bináris a legjobb eredményeket nyújtja – Vegyen egy Mac-et, és használja a verziót (PDFDarkView Apple Silicon vagy Intel chippel ellátott Mac-ekhez). Az OCR eredmények jobbak, mint a Windows alatt!</li>
        <li>Windows: Használja a pytesseract megoldást. Stabil, és a legtöbb dokumentumhoz teljesen megfelelő minőséget biztosít.</li>
        </ul>

        <p><strong>Fontos megjegyzés:</strong></p>
        <ul>
        <li>Mindkét verzió teljesen integrált a felhasználói felületbe – a felhasználó nem észlel különbséget.</li>
        <li>A program automatikusan dönti el, hogy melyik OCR motort használja az operációs rendszer alapján.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Aláírás létrehozása (szkennelésből)",
        "signature_create_title": "Válassza ki a beszkennelt aláírást (PDF/kép)",
        "image_pdf_filter": "Képek és PDF",
        "signature_pdf_empty": "A PDF nem tartalmaz oldalakat.",
        "signature_created_success": "Aláírás sikeresen létrehozva: {0}",
        "signature_create_error": "Hiba az aláírás létrehozásakor:\n{0}",
        "rembg_missing": "A rembg nincs telepítve.\nTelepítse: pip install rembg\nHiba: {0}",
        "signature_name_title": "Fájlnév az aláíráshoz",
        "signature_name_message": "Adjon meg egy fájlnevet az új aláíráshoz (PNG-ként kerül mentésre átlátszó háttérrel):",
        "signature_name_label": "Fájlnév:",
        "signature_name_voice": "Adja meg a fájlnevet az aláíráshoz",
        "signature_processing": "Feldolgozás folyamatban...",
        "signature_creation_title": "Aláírás létrehozása",
        "signature_overwrite_warning": "A(z) '{0}' fájl már létezik. Felülírja?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"PDF előkészítése aláíráshoz",
        "signature_prepare_instruction":"Válasszon ki egy PDF-et, amely egyetlen oldalon egy beszkennelt aláírást tartalmaz.\n\nAz optimális felismerés érdekében:\n• Az aláírás fekete tintával (golyóstoll vagy finomfilc) fehér papírra legyen írva.\n• Az aláírás az egyébként üres A4-es oldal felső harmadában legyen.\n• A PDF-et legalább 300 dpi-vel szkennelték.\n• Az aláírás világos és ne legyen túl vékony.\n• Ne legyenek zavaró háttérminták vagy vonalak.",
        "signature_prepare_voice":"Válasszon ki egy PDF-et beszkennelt aláírással. Ügyeljen a jó minőségre és kontrasztra.",
        "sig_thickness_label":"Vonalvastagság:",
        "sig_thickness_normal":"Normál (vékony)",
        "sig_thickness_bold":"Vastag (ajánlott)",
        "sig_thickness_very_bold":"Nagyon vastag",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI és OCR nyelvek hozzáadása - Útmutató",
        'language_guide_title': "GUI és OCR nyelvek hozzáadása",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Töltse le a kívánt fordítási fájlt <code>translations_xy.py</code> innen:<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        és helyezze el a következő könyvtárba:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Nyissa meg a webböngészőjét.</li>
        <li>Menjen ide: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>A képernyő jobb szélén keresse a "Releases" részt, és válassza a <strong>"latest"</strong> feliratút.</li>
        <li>A következő kiadási oldalon töltse le legalul a <code>Source Code.zip</code> fájlt.</li>
        <li>Csomagolja ki a ZIP fájlt.</li>
        <li>A kicsomagolt mappában keresse meg az összes szükséges nyelvi fájlt, és másolja őket a következő könyvtárba:<br/>
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
        "menu_watermark":"Vízjel beszúrása",
        "fullpage_text_watermark_title":"Szöveg vízjellként",
        "fullpage_image_watermark_title":"Kép vízjellként",
        "filename_with_watermark":"_vízjellel",
        "watermark_text":"Szöveg:",
        "watermark_text_placeholder":"Az Ön vízjel szövege...",
        "watermark_font_family":"Betűtípus:",
        "watermark_font_size":"Betűméret:",
        "watermark_format":"Formázás:",
        "watermark_bold":"Félkövér",
        "watermark_italic":"Dőlt",
        "watermark_color":"Szín:",
        "watermark_choose_color":"Színválasztás...",
        "watermark_opacity":"Átlátszatlanság / Átlátszóság:",
        "watermark_direction":"Olvasási irány:",
        "watermark_direction_l_r":"Bal → Jobb",
        "watermark_direction_bl_tr":"Bal alsó → Jobb felső",
        "watermark_direction_tl_br":"Bal felső → Alsó",
        "watermark_direction_b_t":"Alsó → Felső",
        "watermark_direction_t_b":"Felső → Alsó",
        "watermark_preview":"Előnézet:",
        "watermark_preview_sample":"Mintaszöveg",
        "watermark_empty_text":"Kérjük, adjon meg szöveget.",
        "watermark_applied":"A vízjel az összes oldalra alkalmazva.",
        "watermark_saved":"Vízjel elmentve.",
        "image_scale":"Méret:",
        "image_preview":"Kép előnézete:",
        "no_image_selected":"Nincs kép kiválasztva",
        "browse":"Tallózás...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Kitakarások",
        "redact_add_black": "Kitakarás (fekete)",
        "redact_add_white": "Kitakarás (fehér / törlés)",
        "redact_added_black": "Fekete kitakarás hozzáadva",
        "redact_added_white": "Fehér kitakarás hozzáadva",
        "redact_apply_all": "Összes kitakarás alkalmazása és mentés",
        "redact_discard_all": "Összes kitakarás elvetése",
        "redact_discard": "Kitakarás elvetése",
        "no_redactions": "Nincsenek kitakarások",
        "redact_confirm_title": "Kitakarások végleges alkalmazása",
        "redact_confirm_message": "Figyelmeztetés: A megjelölt területek véglegesen törlődnek (fekete vagy fehér).\nBiztonsági másolat készül (ha engedélyezve van).\n\nFolytatja?",
        "redact_apply": "Igen, takarjon ki most",
        "redact_saved": "{0} kitakarás sikeresen alkalmazva és elmentve.",
        "redact_saved_voice": "{0} kitakarás alkalmazva",
        "redact_error": "Hiba a kitakarás során",
        "filename_redacted":"_kitakarva",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Oldalszámok beszúrása',
        'page_numbers_format': 'Számformátum:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arab)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (római kisbetűs)',
        'page_numbers_format_roman_upper': 'I, II, III ... (római nagybetűs)',
        'page_numbers_format_letter': 'A, B, C ... (betűk)',
        'page_numbers_format_custom': 'Egyéni',
        'page_numbers_custom_pattern': 'Minta:',
        'page_numbers_custom_placeholder': 'pl. "Oldal {nummer}" vagy "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Használja a {nummer} elemet az aktuális oldalszámhoz és a {total} elemet az összes számhoz',
        'page_numbers_position': 'Pozíció:',
        'page_numbers_pos_tl': 'Bal felső',
        'page_numbers_pos_tc': 'Felső közép',
        'page_numbers_pos_tr': 'Jobb felső',
        'page_numbers_pos_ml': 'Bal közép',
        'page_numbers_pos_mc': 'Középre',
        'page_numbers_pos_mr': 'Jobb közép',
        'page_numbers_pos_bl': 'Bal alsó',
        'page_numbers_pos_bc': 'Alsó közép',
        'page_numbers_pos_br': 'Jobb alsó',
        'page_numbers_margins': 'Margók:',
        'page_numbers_margin_x': 'Vízszintes távolság:',
        'page_numbers_margin_y': 'Függőleges távolság:',
        'page_numbers_range': 'Oldaltartomány:',
        'page_numbers_all_pages': 'Minden oldal',
        'page_numbers_custom_range': 'Egyéni tartomány',
        'page_numbers_from': 'Tól:',
        'page_numbers_to': 'Ig:',
        'page_numbers_progress': 'Oldalszámok beszúrása...',
        'page_numbers_start': 'Oldalszámok beszúrásának indítása...',
        'page_numbers_cancel': 'Oldalszámok beszúrása megszakítva',
        'page_numbers_success': 'Az oldalszámok sikeresen hozzáadva.\n\nSzeretné megnyitni az új PDF-et?\n\n{0}',
        'page_numbers_complete': 'Oldalszámok hozzáadva',
        'page_numbers_error_format': 'Hiba az oldalszámok beszúrásakor: {0}',
        'page_numbers_content_type': 'Tartalomtípus:',
        'page_numbers_tab_simple': 'Egyszerű szám',
        'page_numbers_tab_range': 'X. oldal az Y-ból',
        'page_numbers_tab_date': 'Dátum',
        'page_numbers_tab_custom': 'Szabad szöveg',
        'page_numbers_range_format': 'Formátum:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': '{aktuell}. oldal a(z) {gesamt}-ból',
        'page_numbers_range_custom': 'Egyéni',
        'page_numbers_range_placeholder': 'pl. "{aktuell}. oldal / {gesamt}"',
        'page_numbers_date_format': 'Dátumformátum:',
        'page_numbers_date_short': '2024.01.01.',
        'page_numbers_date_long': '2024. január 1.',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Egyéni',
        'page_numbers_date_placeholder': 'pl. %Y.%m.%d. %H:%M',
        'page_numbers_date_position': 'Pozíció:',
        'page_numbers_date_before': 'Dátum az oldalszám előtt',
        'page_numbers_date_after': 'Dátum az oldalszám után',
        'page_numbers_date_only': 'Csak dátum (oldalszám nélkül)',
        'page_numbers_custom_text': 'Egyéni szöveg:',
        'page_numbers_custom_placeholder_text': 'Használja a {seite} elemet az oldalszámhoz és a {gesamt} elemet az összes számhoz\npl. "Bizalmas - {seite}. oldal" vagy "{seite} / {gesamt}"',
        "filename_with_page_number":"_oldalszámmal",
        "filename_with_page_declaration":"_oldal_megjelolessel",
        "filename_with_pagenumber":"_oldalszámmal",
        "filename_with_date":"_dátummal",
        "filename_with_my_page_declaration":"_egyéni_oldal_megjelolessel",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Mentetlen változtatások",
        "unsaved_changes_message_darkmode": "Vannak mentetlen beszúrások.\nSzeretné menteni őket a váltás előtt?",
        "save_and_switch": "Mentés és váltás",
        "discard_and_switch": "Váltás most",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Oldalak exportálása képekként',
        'export_images_menu': 'Exportálás képekként (PNG/JPEG)',
        'export_images_format': 'Képformátum:',
        'export_images_dpi': 'Felbontás (DPI):',
        'export_images_quality': 'JPEG minőség:',
        'export_images_range': 'Oldaltartomány:',
        'export_images_all_pages': 'Minden oldal',
        'export_images_custom_range': 'Egyéni tartomány',
        'export_images_from': 'Tól:',
        'export_images_to': 'Ig:',
        'export_images_options': 'Beállítások:',
        'export_images_single_files': 'Minden oldal külön fájlként',
        'export_images_subfolder': 'Exportálás alkönyvtárba',
        'export_images_subfolder_info': 'Az "PDFnév_képek" alkönyvtárba',
        'export_images_same_folder': 'Ugyanabba a könyvtárba, mint a PDF',
        'export_images_apply_darkmode': 'PDFDarkView beállítások alkalmazása (Sötét mód)',
        'export_images_target_folder': 'Célkönyvtár:',
        'export_images_browse': 'Tallózás...',
        'export_images_preview': 'Előnézet:',
        'export_images_preview_info': 'Válassza ki az exportálási beállításokat',
        'export_images_preview_info_detail': '{0} oldal {1} formátumban\nFelbontás: {2} DPI\nFájlnév: {3}\n{4}',
        'export_images_select_folder': 'Válassza ki a célkönyvtárat',
        'export_images_start': 'Képek exportálásának indítása...',
        'export_images_progress': 'Képek exportálása...',
        'export_images_saving': '{0}. oldal mentése / {1}...',
        'export_images_success': 'Az exportálás sikeres volt!\n\n{0} kép mentve ide:\n{1}',
        'export_images_complete': 'Képek exportálása befejezve',
        'export_images_open_folder': '📁 Könyvtár megnyitása',
        'export_images_cancel': 'Képek exportálása megszakítva',
        'export_images_error_format': 'Hiba a képek exportálásakor: {0}',
        'export_images_pdf2image_missing': 'A "pdf2image" könyvtár nincs telepítve.\n\nKérjük, telepítse a következővel:\npip install pdf2image\n\nWindows rendszeren a Poppler is szükséges:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konvertálás hosszú távú archiváláshoz',
        'pdfa_menu': 'PDF/A konvertálás (archiválásra alkalmas)',
        'pdfa_info': 'A PDF-et PDF/A formátumba konvertálja.\n\nA PDF/A kifejezetten hosszú távú archiválásra készült, és biztosítja, hogy a dokumentum a jövőben is helyesen jelenjen meg.',
        'pdfa_standard': 'PDF/A szabvány:',
        'pdfa_standard_select': 'Verzió:',
        'pdfa_1': 'PDF/A-1 (egyszerű, széles körben kompatibilis)',
        'pdfa_2': 'PDF/A-2 (modernebb, jobb tömörítés)',
        'pdfa_3': 'PDF/A-3 (legújabb verzió, csatolmányokat engedélyez)',
        'pdfa_standards_explanation': '📖 A szabványok magyarázata:\n\n'
            '• PDF/A-1: Alap, kompatibilis régebbi rendszerekkel (kb. 2005)\n'
            '• PDF/A-2: Modernebb, jobb tömörítés, átlátszóság támogatás (kb. 2011)\n'
            '• PDF/A-3: Legújabb verzió, fájlcsatolmányok beágyazását engedélyezi (kb. 2013)\n\n'
            'Ajánlás: A PDF/A-2 jó kompromisszum a kompatibilitás és a modern funkciók között.',
        'pdfa_options': 'Beállítások:',
        'pdfa_compress_enable': 'PDF tömörítése (kisebb fájl)',
        'pdfa_metadata_preserve': 'Metaadatok megtartása (cím, szerző stb.)',
        'pdfa_target_folder': 'Célkönyvtár:',
        'pdfa_browse': 'Tallózás...',
        'pdfa_select_folder': 'Válassza ki a célkönyvtárat',
        'pdfa_ocr_info_unknown': '🔍 A szövegtartalom nem ellenőrizhető.',
        'pdfa_ocr_info_not_needed': '✅ Szöveg elérhető - OCR nem szükséges.\nA PDF/A közvetlenül létrehozható.',
        'pdfa_ocr_info_recommended': '⚠️ Nem található elegendő szöveg.\n\nKereshető PDF-ekhez javasoljuk az OCR előzetes futtatását.\nMegjegyzés: A PDF/A OCR nélkül is működik - de a szöveg nem lesz kereshető.',
        'pdfa_ocr_info_error': '❌ Hiba az ellenőrzés során: {0}',
        'pdfa_start': 'PDF/A konvertálás indítása...',
        'pdfa_progress': 'PDF/A konvertálás folyamatban...',
        'pdfa_success': 'PDF/A konvertálás sikeres!\n\nMentve mint:\n{0}\n\nSzeretné megnyitni az új PDF-et?',
        'pdfa_complete': 'PDF/A konvertálás befejezve',
        'pdfa_cancel': 'PDF/A konvertálás megszakítva',
        'pdfa_error_format': 'Hiba a PDF/A konvertálás során:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'A "ocrmypdf" könyvtár nincs telepítve.\n\nKérjük, telepítse a következővel:\npip install ocrmypdf',
        'btn_convert': 'Konvertálás',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF optimalizálása (fájlméret csökkentése)',
        'optimize_menu': 'PDF optimalizálása (fájlméret)',
        'optimize_info': 'Csökkenti a PDF fájlméretét különböző optimalizálási módszerekkel.\n\nMinél magasabb a tömörítési szint, annál kisebb lesz a fájl - a képek minőségének esetleges csökkenésével.',
        'optimize_level': 'Tömörítési szint:',
        'optimize_level_low': 'Alacsony (gyors, kis megtakarítás)',
        'optimize_level_medium': 'Közepes (jó kompromisszum)',
        'optimize_level_high': 'Magas (nagy megtakarítás)',
        'optimize_level_maximum': 'Maximális (maximális megtakarítás, lassú)',
        'optimize_level_explanation': 'Ajánlás: A "Közepes" jó kompromisszum a sebesség és a fájlméret között.',
        'optimize_options': 'Beállítások:',
        'optimize_compress_images': 'Képek tömörítése (JPEG minőség csökkentése)',
        'optimize_clean_objects': 'Nem használt objektumok eltávolítása',
        'optimize_preserve_metadata': 'Metaadatok megtartása (cím, szerző stb.)',
        'optimize_image_quality': 'Képminőség:',
        'optimize_range': 'Oldaltartomány:',
        'optimize_all_pages': 'Minden oldal',
        'optimize_custom_range': 'Egyéni tartomány',
        'optimize_from': 'Tól:',
        'optimize_to': 'Ig:',
        'optimize_target_folder': 'Célkönyvtár:',
        'optimize_browse': 'Tallózás...',
        'optimize_select_folder': 'Válassza ki a célkönyvtárat',
        'optimize_info_box': 'Információ',
        'optimize_info_text': 'Az optimalizálás nagy PDF-eknél több percet is igénybe vehet.\n\nA képek csökkentett minőséggel kerülnek mentésre, ami jelentősen csökkentheti a fájlméretet.',
        'optimize_start': 'PDF optimalizálás indítása...',
        'optimize_progress': 'PDF optimalizálása...',
        'optimize_cancel': 'PDF optimalizálás megszakítva',
        'optimize_complete': 'PDF optimalizálás befejezve',
        'optimize_error_format': 'Hiba a PDF optimalizálás során:\n\n{0}',
        'optimize_success_message': 'PDF optimalizálás sikeres!\n\nMentve mint:\n{0}\n\nElőtte: {1}\nUtána: {2}\nMegtakarítás: {3:.1f}%\n\n{4}\n\nSzeretné megnyitni az optimalizált PDF-et?',
        'optimize_success_message_no_size': 'PDF optimalizálás sikeres!\n\nMentve mint:\n{0}\n\nA méretinformáció nem elérhető.\n\nSzeretné megnyitni az optimalizált PDF-et?',
        'optimize_result_positive': 'A fájl {0:.1f}%-kal csökkent.',
        'optimize_result_zero': 'A fájlméret nem változott.',
        'optimize_result_negative': 'A fájl {0:.1f}%-kal nőtt.\nAz optimalizálás kihagyva, az eredeti fájl megmaradt.',
        'btn_optimize': 'Optimalizálás indítása',
        'filename_optimize_low_suffix': '_optimalizalt_alacsony',
        'filename_optimize_medium_suffix': '_optimalizalt',
        'filename_optimize_high_suffix': '_optimalizalt_magas',
        'filename_optimize_maximum_suffix': '_optimalizalt_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF kivágása',
        'crop_menu': 'PDF kivágása (Crop)',
        'crop_range': 'Alkalmazás:',
        'crop_all_pages': 'Minden oldal',
        'crop_current_page': 'Csak az aktuális oldal',
        'crop_values': 'Kivágási értékek (pontokban):',
        'crop_left': 'Bal:',
        'crop_right': 'Jobb:',
        'crop_top': 'Felső:',
        'crop_bottom': 'Alsó:',
        'crop_presets': 'Előbeállítások:',
        'crop_preset_white': 'Fehér margók észlelése',
        'crop_reset': 'Visszaállítás',
        'crop_mouse_hint': '🖱️ Húzzon egy téglalapot a terület durva kijelöléséhez.\nEzután pontosan beállíthatja az értékeket a SpinBoxokban.\nA manuális beállítás egérrel nem lehetséges.',
        'crop_apply': 'Kivágás',
        'crop_scope_all': 'Minden oldal',
        'crop_scope_current': 'Aktuális oldal',
        'crop_new_size': 'Új méret: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Nincs betöltött PDF',
        'crop_preview_error': 'Hiba az előnézet betöltésekor',
        'crop_start': 'Kivágás indítása...',
        'crop_progress': 'PDF kivágása...',
        'crop_success': 'PDF sikeresen kivágva!\n\nMentve mint:\n{0}\n\nSzeretné megnyitni a kivágott PDF-et?',
        'crop_complete': 'Kivágás befejezve',
        'crop_cancel': 'Kivágás megszakítva',
        'crop_error_format': 'Hiba a kivágás során:\n\n{0}',
        'filename_crop_suffix': '_kivagva',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF kisimítása (Flatten)',
        'flatten_menu': 'PDF kisimítása (Flatten)',
        'flatten_info': 'A PDF kisimítása "beégeti" az összes szerkeszthető elemet az oldal tartalmába.\n\nEzt követően az űrlapmezők, megjegyzések, szövegek, keresztek, aláírások, képek és alakzatok már nem szerkeszthetők egyenként.',
        'flatten_explanation_title': '📖 Mire jó ez?',
        'flatten_explanation_text': 'A kisimítás a következő helyzetekben szükséges:\n\n'
            '• 📄 Szeretné előkészíteni a dokumentumot nyomtatásra\n'
            '• 🔒 Szeretné megakadályozni, hogy valaki megváltoztassa az űrlapmezőket\n'
            '• 📎 Szeretné "tartósan" beágyazni a megjegyzéseket és kommentárokat a dokumentumba\n'
            '• 🖼️ Szeretné tartósan rögzíteni a beszúrt szövegeket, kereszteket, aláírásokat, képeket és alakzatokat a dokumentumban\n'
            '• 📦 Szeretné előkészíteni a fájlt archiválásra\n\n'
            'A kisimítás kisebbé teszi a PDF-et, és megakadályozza az elemek véletlen elmozdítását vagy törlését.',
        'flatten_what_title': 'Mi kerül kisimításra?',
        'flatten_what_list': '• ✅ Űrlapmezők (szövegmezők, jelölőnégyzetek, gombok)\n'
            '• ✅ Megjegyzések (kommentárok, kiemelések, jegyzetek)\n'
            '• ✅ Rétegek (szövegek, keresztek, aláírások, képek, alakzatok)',
        'flatten_options': 'Beállítások:',
        'flatten_forms': 'Űrlapmezők kisimítása',
        'flatten_annotations': 'Megjegyzések kisimítása',
        'flatten_overlays': 'Rétegek kisimítása (szövegek, keresztek, aláírások, képek, alakzatok)',
        'flatten_target_folder': 'Célkönyvtár:',
        'flatten_browse': 'Tallózás...',
        'flatten_select_folder': 'Válassza ki a célkönyvtárat',
        'flatten_warning': '⚠️ Fontos: A kisimítás visszafordíthatatlan folyamat!\n\nA kisimítás után a szerkeszthető elemeket már nem lehet egyenként módosítani vagy törölni.\nSzükség esetén előzetesen készítsen biztonsági másolatot.',
        'flatten_apply': 'Kisimítás',
        'flatten_start': 'Kisimítás indítása...',
        'flatten_progress': 'PDF kisimítása...',
        'flatten_success': 'PDF sikeresen kisimítva!\n\nMentve mint:\n{0}\n\nSzeretné megnyitni a kisimított PDF-et?',
        'flatten_complete': 'Kisimítás befejezve',
        'flatten_cancel': 'Kisimítás megszakítva',
        'flatten_error_format': 'Hiba a kisimítás során:\n\n{0}',
        'filename_flatten_suffix': '_kisimitva',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF rétegezés (Overlay)',
        'overlay_menu': 'PDF rétegezés (Overlay)',
        'overlay_info': 'Egy PDF-et (réteget) helyez egy másik PDF fölé.\n\nA réteg PDF az alap PDF-re kerül. Ez hasznos vízjelekhez, logókhoz, fejlécekhez vagy bélyegzőkhöz.',
        'overlay_explanation_title': '📖 Mire jó ez?',
        'overlay_explanation_text': 'A rétegezés a következő helyzetekben szükséges:\n\n'
            '• 🏢 Vállalati logo elhelyezése vízjellként minden oldalon\n'
            '• 📄 Fejléc elhelyezése üres PDF-en\n'
            '• 🖊️ Bélyegző réteg elhelyezése dokumentumon\n'
            '• 🔖 Vízjel elhelyezése minden oldalon\n'
            '• 📑 Űrlap réteg elhelyezése sablonon',
        'overlay_type': 'Réteg típusa:',
        'overlay_type_fullpage': 'Teljes oldal (lefedő)',
        'overlay_type_transparent': 'Teljes oldal (átlátszó - ajánlott)',
        'overlay_type_stamp': 'Bélyegző (pozícionálható)',
        'overlay_type_info_fullpage': '📄 A réteg PDF pontosan a teljes oldal fölé kerül.\nA fehér háttér eltávolítható, így csak a tartalom marad látható.',
        'overlay_type_info_transparent': '🔍 A réteg PDF átlátszó háttérrel kerül a teljes oldal fölé.\nA fehér háttér automatikusan eltávolításra kerül - ideális vízjelekhez és logókhoz!',
        'overlay_type_info_stamp': '🖊️ A réteg PDF bélyegzőként kerül pozícionálásra és méretezésre.\nTökéletes logókhoz, bélyegzőkhöz vagy aláírásokhoz meghatározott pozíciókban.',
        'overlay_remove_background': 'Fehér háttér eltávolítása:',
        'overlay_remove_background_enable': 'Fehér háttér eltávolítása a réteg PDF-ből (átlátszóvá teszi a réteget)',
        'overlay_remove_background_tooltip': 'Eltávolítja a fehér területeket a réteg PDF-ből, hogy az alatta lévő szöveg láthatóvá váljon.',
        'overlay_threshold': 'Küszöbérték:',
        'overlay_threshold_hint': '(1-254, magasabb = több fehér kerül eltávolításra)',
        'overlay_select_file': 'Réteg PDF kiválasztása:',
        'overlay_file_placeholder': 'Kérjük, válasszon PDF fájlt a réteghez',
        'overlay_browse': 'Tallózás...',
        'overlay_select_overlay': 'Réteg PDF kiválasztása',
        'overlay_range': 'Oldaltartomány:',
        'overlay_all_pages': 'Minden oldal',
        'overlay_custom_range': 'Egyéni tartomány',
        'overlay_from': 'Tól:',
        'overlay_to': 'Ig:',
        'overlay_position': 'Pozíció:',
        'overlay_position_center': 'Közép',
        'overlay_position_top_left': 'Bal felső',
        'overlay_position_top_right': 'Jobb felső',
        'overlay_position_bottom_left': 'Bal alsó',
        'overlay_position_bottom_right': 'Jobb alsó',
        'overlay_size': 'Méret:',
        'overlay_size_original': 'Eredeti méret',
        'overlay_size_fit_page': 'Oldalhoz igazítás',
        'overlay_size_custom': 'Egyéni (%)',
        'overlay_opacity': 'Átlátszóság:',
        'overlay_target_folder': 'Célkönyvtár:',
        'overlay_browse_folder': 'Tallózás...',
        'overlay_select_folder': 'Válassza ki a célkönyvtárat',
        'overlay_warning': '⚠️ Megjegyzés: A réteg PDF az alap PDF-re kerül, és "beég" abba.\n\nA réteg PDF elemei mentés után már nem szerkeszthetők egyenként.',
        'overlay_apply': 'Rétegezés',
        'overlay_start': 'Rétegezés indítása...',
        'overlay_progress': 'PDF rétegezése...',
        'overlay_success': 'PDF sikeresen rétegezve!\n\nMentve mint:\n{0}\n\nSzeretné megnyitni a rétegezett PDF-et?',
        'overlay_complete': 'Rétegezés befejezve',
        'overlay_cancel': 'Rétegezés megszakítva',
        'overlay_error_format': 'Hiba a rétegezés során:\n\n{0}',
        'overlay_no_file': 'Nincs réteg PDF kiválasztva.\n\nKérjük, válasszon PDF fájlt a rétegezéshez.',
        'filename_overlay_suffix': '_retegzett',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Képek kinyerése PDF-ből',
        'extract_images_menu': 'Összes kép kinyerése',
        'extract_images_info': 'Kinyeri az összes képet a PDF-ből, és külön fájlokként menti el.\n\nA képek eredeti formátumban kerülnek mentésre, vagy átalakításra a kiválasztott formátumba.',
        'extract_images_format': 'Képformátum:',
        'extract_images_quality': 'JPEG minőség:',
        'extract_images_options': 'Beállítások:',
        'extract_images_subfolder': 'Kinyerés alkönyvtárba ("PDFnév_képek")',
        'extract_images_unique': 'Csak egyedi képek (duplikátumok elkerülése)',
        'extract_images_range': 'Oldaltartomány:',
        'extract_images_all_pages': 'Minden oldal',
        'extract_images_custom_range': 'Egyéni tartomány',
        'extract_images_from': 'Tól:',
        'extract_images_to': 'Ig:',
        'extract_images_target_folder': 'Célkönyvtár:',
        'extract_images_browse': 'Tallózás...',
        'extract_images_select_folder': 'Válassza ki a célkönyvtárat',
        'extract_images_info_box': 'Információ',
        'extract_images_info_text': 'A kinyerés nagy PDF-eknél több percet is igénybe vehet.\n\nA képek eredeti nevükkel kerülnek mentésre (oldal_kép).',
        'extract_images_extract': 'Kinyerés',
        'extract_images_start': 'Kinyerés indítása...',
        'extract_images_progress': 'Képek kinyerése...',
        'extract_images_success': '✅ Képek sikeresen kinyerve!\n\n{0} kép mentve ide:\n{1}',
        'extract_images_complete': 'Képek kinyerése befejezve',
        'extract_images_cancel': 'Kinyerés megszakítva',
        'extract_images_error_format': 'Hiba a képek kinyerése során:\n\n{0}',
        'extract_images_open_folder': '📁 Könyvtár megnyitása',
        'extract_images_no_images': 'Nem találhatók képek a PDF-ben.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Több oldal egy oldalon (N-Up)',
        'nup_menu': 'Több oldal egy oldalon (N-Up)',
        'nup_info': 'Több PDF-oldalt rendez egy oldalra.\n\nIdeális tömör nyomtatásokhoz, áttekintésekhez vagy kézikönyvekhez.',
        'nup_layout': 'Elrendezés:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Előnézet:',
        'nup_preview_info': '{0} oldal → {1} oldal laponként → {2} lap\nElrendezés: {3}',
        'nup_order': 'Sorrend:',
        'nup_order_horizontal': 'Vízszintes (soronként)',
        'nup_order_vertical': 'Függőleges (oszloponként)',
        'nup_order_horizontal_reverse': 'Vízszintes fordított',
        'nup_order_vertical_reverse': 'Függőleges fordított',
        'nup_range': 'Oldaltartomány:',
        'nup_all_pages': 'Minden oldal',
        'nup_custom_range': 'Egyéni tartomány',
        'nup_from': 'Tól:',
        'nup_to': 'Ig:',
        'nup_options': 'Beállítások:',
        'nup_margins': 'Margók:',
        'nup_margin_between': 'Oldalak közötti távolság:',
        'nup_page_numbers': 'Oldalszámok beszúrása',
        'nup_target_folder': 'Célkönyvtár:',
        'nup_browse': 'Tallózás...',
        'nup_select_folder': 'Válassza ki a célkönyvtárat',
        'nup_create': 'Létrehozás',
        'nup_start': 'N-Up indítása...',
        'nup_progress': 'N-Up létrehozása...',
        'nup_success': 'N-Up sikeresen létrehozva!\n\nMentve mint:\n{0}\n\nSzeretné megnyitni az új PDF-et?',
        'nup_complete': 'N-Up befejezve',
        'nup_cancel': 'N-Up megszakítva',
        'nup_error_format': 'Hiba az N-Up során:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Oldalméret módosítása',
        'pagesize_menu': 'Oldalméret módosítása',
        'pagesize_info': 'Módosítja a PDF oldalméretét.\n\nA tartalom automatikusan alkalmazkodik az új mérethez.',
        'pagesize_format': 'Formátum:',
        'pagesize_select': 'Válasszon szabványos formátumot:',
        'pagesize_custom': 'Egyéni méret:',
        'pagesize_width': 'Szélesség:',
        'pagesize_height': 'Magasság:',
        'pagesize_orientation': 'Tájolás:',
        'pagesize_portrait': 'Álló',
        'pagesize_landscape': 'Fekvő',
        'pagesize_scale_options': 'Méretezési beállítások:',
        'pagesize_fit': 'Igazítás (képarány megtartása)',
        'pagesize_stretch': 'Nyújtás (torzítás)',
        'pagesize_center': 'Középre (eredeti méret)',
        'pagesize_range': 'Oldaltartomány:',
        'pagesize_all_pages': 'Minden oldal',
        'pagesize_custom_range': 'Egyéni tartomány',
        'pagesize_from': 'Tól:',
        'pagesize_to': 'Ig:',
        'pagesize_target_folder': 'Célkönyvtár:',
        'pagesize_browse': 'Tallózás...',
        'pagesize_select_folder': 'Válassza ki a célkönyvtárat',
        'pagesize_apply': 'Alkalmazás',
        'pagesize_start': 'Oldalméret módosítás indítása...',
        'pagesize_progress': 'Oldalméret módosítása...',
        'pagesize_success': 'Oldalméret sikeresen módosítva!\n\nMentve mint:\n{0}\n\nSzeretné megnyitni az új PDF-et?',
        'pagesize_complete': 'Oldalméret módosítás befejezve',
        'pagesize_cancel': 'Oldalméret módosítás megszakítva',
        'pagesize_error_format': 'Hiba az oldalméret módosítása során:\n\n{0}',
        'pagesize_preview_info': 'Új méret: {0} x {1} pt',
        'filename_pagesize_suffix': '_uj_meret',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF információk',
        'pdf_info_menu': 'PDF információk megjelenítése',
        'pdf_info_voice': 'PDF információk megjelenítése',
        'pdf_info_error': 'Hiba a PDF információk megjelenítése során:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Billentyűparancsok megjelenítése",
        "shortcuts_dialog_title": "Billentyűparancsok",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FÁJL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF megnyitása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF bezárása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Mentés másként...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Dokumentum védelme</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Nyomtatás</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Azonnali nyomtatás (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Alkalmazás bezárása</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORTÁLÁS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Exportálás Pages-ként</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Exportálás DOCX-ként</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Exportálás TXT-ként</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Exportálás képekként (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Képek kinyerése</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTUMFELDOLGOZÁS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Több oldal)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konvertálás (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF kisimítása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF rétegezése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF optimalizálása</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ SZERKESZTÉS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Keresés</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Könyvjelző hozzáadása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Könyvjelzők kezelése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Következő könyvjelző</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Előző könyvjelző</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR futtatása</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 OLDALKEZELÉS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Aktuális oldal elforgatása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Összes oldal elforgatása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Aktuális oldal normalizálása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Összes oldal normalizálása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Oldalak törlése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Oldalak kinyerése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Oldalak beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Oldalak áthelyezése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDF-ek egyesítése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Oldalméret módosítása</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 BESZÚRÁS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Szöveg beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Kereszt beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Aláírás 1 beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Aláírás 2 beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Kép beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Téglalap beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ellipszis beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Vonal beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Nyíl beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Oldalszámok beszúrása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Szöveges vízjel</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Képes vízjel</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ KITAKARÁSOK</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Kitakarás (fekete)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Kitakarás (fehér)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Összes kitakarás alkalmazása</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ HALADÓ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF kivágása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Metaadatok szerkesztése</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ NÉZET</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Sötét/Világos mód váltása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Szövegablak megjelenítése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Oldalszélesség (Nagyítás)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Két oldal (Nagyítás)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Áttekintés (Nagyítás)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ BEÁLLÍTÁSOK</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Jelszókezelés</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR beállítások</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Aláírás beállítások</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Fájlnév formázás</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Beállítások exportálása</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Beállítások importálása</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMÁCIÓ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF információk megjelenítése</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Hangos kimenet be/ki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Menüsáv fókuszálása</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Új verzió elérhető",
        "update_available_message": "Elérhető egy új verzió <b>{0}</b>.\n\nLátogassa meg a kiadási oldalt a frissítés letöltéséhez:\n{1}",
        "update_available_voice": "Új verzió {0} elérhető. Töltse le a frissítést a GitHub oldalról.",
        "update_open_release": "Kiadási oldal megnyitása",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Összes fordítás letöltése",
        "ask_download_all_translations": """A német, angol és vietnami mellett további {total_languages} GUI nyelv érhető el.\n\nBiztosítani / frissíteni kell őket?\n\nMegjegyzés:\nA szükségtelen nyelveket később manuálisan törölheti a következő könyvtárból:\n{translations_path}
        \nHa megszakítja, a GUI nyelveket később letöltheti az 'Eszközök → Fordítások frissítése' menüponton keresztül.""",
        "menu_update_translations": "Fordítások frissítése",
        "translations_updated": "Fordítások frissítve",
        "translations_update_success": "{} fordítás sikeresen frissítve ({} új, {} frissített).",
        "translations_update_error": "Hiba a fordítások frissítése során",
        "translations_update_no_changes": "Minden fordítás már naprakész.",
        "translations_update_offline": "Nincs internetkapcsolat. A fordításokat nem lehetett frissíteni.",
        "translations_update_in_progress": "A fordítások háttérben frissülnek...",
        "translations_downloading": "Fordítások letöltése...",
        "translations_path_hint": "Felhasználói könyvtár a fordításokhoz",
        "translations_update_not_available_title": "A frissítés nem érhető el",
        "translations_update_not_available_message": """A fordítások frissítése csak a telepített verzióban érhető el.\n\nFejlesztési módban a fordítások már naprakészek.""",
        "translations_update_no_internet_title": "Nincs internetkapcsolat",
        "translations_update_no_internet_message": """Nem sikerült internetkapcsolatot létesíteni.\n\nA fordítások nem tölthetők le a GitHub-ról.\n\nLehetséges megoldások:
        • Ellenőrizze az internetkapcsolatát
        • Ideiglenesen tiltsa le az esetleges tűzfalat
        • Próbálja újra később
        \nA fordításokat manuálisan is letöltheti a GitHub-ról:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "A frissítés már folyamatban van",
        "btn_retry": "Újrapróbálkozás",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Üdvözöljük a PDF Dark View-ban",
        "welcome_title_not_supported": "Üdvözöljük a PDF Dark View-ban",
        "welcome_message": "Üdvözöljük a PDF Dark View-ban!\n\nA rendszer nyelve '{language}' néven lett felismerve.\nSzeretné ezt a nyelvet használni a felhasználói felülethez?\n\nA nyelvet bármikor módosíthatja a 'Beállítások → Nyelv' menüpontban.",
        "welcome_message_language_not_available": "Üdvözöljük a PDF Dark View-ban!\n\nA rendszer nyelve '{language}' néven lett felismerve.\nEz a nyelv még nincs telepítve.\n\nSzeretné most letölteni a {language} nyelvű fordításokat a GitHub-ról?\n\n(A nyelv ezután automatikusan használatra kerül a felhasználói felülethez.)",
        "welcome_message_language_not_supported": "Üdvözöljük a PDF Dark View-ban!\n\nA rendszer nyelve '{language}' néven lett felismerve.\nSajnos ehhez a nyelvhez még nincsenek fordítások.\n\nA felhasználói felület {fallback_language} nyelven jelenik meg.\n\nA nyelvet bármikor módosíthatja a 'Beállítások → Nyelv' menüpontban.\nHa szeretné, saját maga is hozzájárulhat egy fordításhoz az Ön nyelvén:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Igen, használja a rendszer nyelvét",
        "welcome_keep_english": "Nem, tartsa meg az angolt",
        "welcome_download_language": "Igen, töltse le a {language} nyelvet",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "A program bezáródik",

    }
