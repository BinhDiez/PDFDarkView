
# ============================================
# translations_et.py - Eesti sõnastik (Estnisch)
# Vollständig sortiert nach Kategorien
# ============================================

def load_estonian_strings():
    """Lädt alle estnischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Ava PDF",
        'btn_text_window': "OCR tekst",
        'btn_first': "Esimene lehekülg",
        'btn_prev': "Eelmine lehekülg",
        'btn_next': "Järgmine lehekülg",
        'btn_last': "Viimane lehekülg",
        'btn_print': "Prindi",
        'btn_darkmode_light': "Hele režiim",
        'btn_darkmode_dark': "Tume režiim",
        'btn_delete_pages': "Kustuta leheküljed",
        'btn_extract_pages': "Eralda leheküljed",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Tühista",
        'btn_save': "Salvesta",
        'btn_close': "Sulge",
        'btn_delete': "Kustuta",
        'btn_delete_all': "Kustuta kõik",
        'btn_copy': "Kopeeri",
        'btn_export': "Ekspordi",
        'btn_show': "Näita parooli",
        'btn_hide': "Peida parool",
        'btn_authenticate': "Autendi",
        'btn_settings': "Seaded",
        'btn_protect': "Kaitse",
        'btn_remove_password': "Eemalda parool",
        'btn_manage': "Paroolihaldus",
        'btn_retry': "Proovi uuesti",
        'btn_select_all': "Vali kõik",
        'btn_clear_selection': "Tühista valik",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Lehekülg {0} / {1}",
        'page_count': "/ {0}",
        'goto_page': "Mine leheküljele",
        'page_simple': "Lehekülg {0}",
        'full_view_page': "Täisvaade lehekülg {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Sisesta otsitav + Enter",
        'search_results': "Tulemusi: {0} / {1}",
        'search_nav_hint': "Enter: järgmine (Shift+Enter: eelmine) tulemus",
        'search_no_results': "Tulemusi pole",
        'search_error': "Otsingu viga",
        'search_active': "Otsinguväli aktiveeritud",
        'search_closed': "Otsing lõpetatud",
        'search_position': "Lehekülg {0} {1}",
        'search_pos_top': "päris üleval",
        'search_pos_upper': "üleval",
        'search_pos_middle': "keskel",
        'search_pos_lower': "all",
        'search_pos_bottom': "päris all",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Tekstituvastus õnnestus!",
        'ocr_success_title': "OCR õnnestus",
        'ocr_success_message': "Dokument on nüüd otsitav.",
        'ocr_failed': "OCR ebaõnnestus",
        'ocr_in_progress': "OCR töös",
        'ocr_preparing': "PDF-i ettevalmistamine...",
        'ocr_analyzing': "PDF-i analüüsimine...",
        'ocr_optimizing': "Pildi optimeerimine...",
        'ocr_recognizing': "Tekstituvastus...",
        'ocr_embedding': "Teksti sisestamine...",
        'ocr_finalizing': "PDF-i lõpetamine...",
        'ocr_not_available': "OCR pole saadaval",
        'ocr_install_message': "OCR-tööriistu ei leitud.\n\nPalun installige:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR vajalik",
        'ocr_question': "PDF ei sisalda otsitavat teksti.\nKas soovite teha OCR-i, et võimaldada {0}?",
        'ocr_perform': "Teosta OCR",
        'ocr_later': "Hiljem",
        'ocr_starting': "Garanteeritud OCR-i käivitamine...",
        'ocr_success_voice': "OCR õnnestus. PDF on nüüd otsitav.",
        'ocr_partial_success': "OCR tehti, kuid asendamisel tekkis probleeme.\n\nOtsitav versioon salvestati asukohta:\n{0}\n\nViga: {1}",
        'ocr_partial_title': "OCR osaliselt õnnestus",
        'ocr_partial_voice': "OCR tehtud, kuid asendamine ebaõnnestus.",
        'original_file': "Algne fail:",
        'old_size': "Vana suurus:    {0} baiti",
        'new_size': "Uus suurus: {0} baiti",
        'size_change': "Muutus: {0}{1} baiti",
        'backup_created_file': "Varukoopia loodud:\n{0}",
        'backup_not_created': "Varukoopiat pole loodud (seade väljas)",
        'page_header': "=== Lehekülg {0} ===\n{1}\n",
        'scanned_page_header': "=== Lehekülg {0} (skaneeritud) ===\n[See lehekülg sisaldab ainult skaneeritud teksti]\n[Palun tehke OCR käsitsi]\n",
        'scanned_warning': "⚠️ SKANEERITUD TEKST - OCR VAJALIK",
        'guaranteed_title': "Otsitav PDF loodud",
        'guaranteed_message': "<b>Garanteeritud otsitav versioon loodud!</b>\n\nKuna automaatne OCR ebaõnnestus, loodi alternatiivne otsitav PDF:\n\n{0}\n\n<b>See fail sisaldab:</b>\n• Eraldatud teksti (kui see oli olemas)\n• Juhiseid skaneeritud lehtede jaoks\n• On täielikult otsitav",
        'guaranteed_voice': "Garanteeritud otsitav PDF loodud.",
        'instruction_title': "OCR-I JUHEND",
        'instruction_file': "Algne fail: {0}",
        'instruction_text': "Automaatne tekstituvastus (OCR) ebaõnnestus.\nTehke OCR käsitsi:\n\n1. OCRmyPDF-ga (käsurida):\n   ocrmypdf --force-ocr \"[FAIL]\" \"väljund.pdf\"\n\n2. ADOBE ACROBAT-iga (macOS/Windows):\n   • Avage PDF Acrobatis\n   • Tööriistad > Redigeeri PDF-i\n   • Valige 'Tekstituvastus'\n\n3. PREVIEW-ga (macOS):\n   • Avage PDF eelvaates\n   • Fail > Ekspordi...\n   • Quartz-filter: 'Vähenda faili suurust'\n   • Lubage 'Teosta OCR'\n\n4. ONLINE OCR TEENUSED:\n   • smallpdf.com/et/ocr-pdf\n   • ilovepdf.com/et/ocr-pdf\n   • adobe.com/et/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR-i juhend loodud",
        'instruction_created_message': "Detailne juhend loodi:\n\n{0}\n\nJärgige samme käsitsi OCR-i tegemiseks.",
        'instruction_created_voice': "OCR-i juhend loodud.",
        'ocr_impossible': "OCR pole võimalik",
        'ocr_impossible_message': "OCR-i ei saanud teostada.\n\nTöötlege '{0}' käsitsi OCR-tarkvaraga.",
        'ocr_impossible_voice': "OCR pole võimalik. Palun töötlege käsitsi.",
        'emergency_title': "Häda-OCR",
        'emergency_message': "Häda-PDF loodi:\n\n{0}\n\nTöötlege see fail käsitsi OCR-iga.",
        'emergency_voice': "Häda-PDF loodud. Tehke OCR käsitsi.",
        'critical_error': "Kriitiline viga",
        'critical_error_message': "OCR-i ei saanud käivitada.\n\nTaaskäivitage programm ja kontrollige OCR-i paigaldust.",
        'critical_error_voice': "Kriitiline OCR viga",
        'ocr_question_html': "<p>PDF ei sisalda otsitavat teksti.<p>Kas soovite teha OCR-i, et võimaldada <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR vajalik. PDF ei sisalda otsitavat teksti. Kas soovite teha OCR-i, et võimaldada {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "PDF-i pole laaditud",
        'no_pdf_message': "PDF-i pole laaditud",
        'pdf_not_found': "PDF-faili ei leitud",
        'file_size': "Faili suurus",
        'bytes': "baiti",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Varukoopia loodud",
        'backup_disabled': "Varukoopia väljas",
        'backup_activated': "Varukoopia loomine sisse lülitatud",
        'backup_deactivated': "Varukoopia loomine välja lülitatud",
        'backup_status': "Varukoopia: {0}",
        'backup_on': "✔ sees",
        'backup_off': "✘ väljas",
        'close_pdf': "Sule PDF: {0}",
        'pdf_not_found_format': "PDF-faili ei leitud: {0}",
        'error_pdf_load_format': "Viga PDF-i laadimisel: {0}",
        'load_failed_format': "Laadimine ebaõnnestus:\n{0}",
        'decrypted_suffix': "(dekrüpteeritud)",
        'decryption_failed': "Dekrüpteerimine ebaõnnestus.",
        'decryption_error': "Viga dekrüpteerimisel",
        'decryption_success': "Dekrüpteerimine õnnestus",
        'decryption_success_message': "PDF dekrüpteeriti ja salvestati asukohta:\n\n{0}",
        'decryption_success_voice': "PDF dekrüpteeriti ja salvestati.",
        'password_remove_error': "Viga parooli eemaldamisel",
        'save_unencrypted': "Salvesta krüptimata PDF kui",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Salvesta kui...",
        'save_copy': "Salvesta koopia",
        'save_success': "PDF salvestatud asukohta: {0}",
        'save_encrypted': "Kaitstud PDF salvestatud asukohta: {0}",
        'save_error': "PDF-i ei õnnestunud salvestada",
        'encryption_question': "Kas soovite PDF-i parooliga kaitsta?",
        'encryption_yes': "Jah",
        'encryption_no': "Ei",
        'encryption_cancel': "Tühista",
        'save_cancel': "Salvestamine tühistatud",
        'save_encrypted_voice': "Fail krüpteeriti ja salvestati.",
        'save_success_voice': "PDF-fail salvestati krüptimata.",
        'save_error_format': "PDF-i ei õnnestunud salvestada:\n{0}",
        'export_pages_success': "Pages-i eksport õnnestus",
        'export_pages_error': "Pages-i eksport ebaõnnestus",
        'export_pages_error_format': "Pages-i eksport ebaõnnestus: {0}",
        'export_word_success': "Wordi eksport õnnestus",
        'export_word_error': "Wordi eksport ebaõnnestus",
        'export_word_error_format': "Wordi eksport ebaõnnestus: {0}",
        'export_text_success': "Teksti eksport õnnestus",
        'export_text_error': "Teksti eksport ebaõnnestus",
        'export_text_error_format': "Teksti eksport ebaõnnestus: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Parool vajalik",
        'password_enter': "Palun sisestage parool",
        'password_confirm': "Kinnitage parool",
        'password_new': "Uus parool",
        'password_current': "Praegune parool",
        'password_save': "Salvesta parool (krüpteeritult)",
        'password_saved': "✓ Selle faili parool on salvestatud",
        'password_wrong': "Vale parool",
        'password_mismatch': "Paroolid ei ühti",
        'password_too_short': "Parool on liiga lühike",
        'password_min_length': "Parool peab olema vähemalt 4 tähemärki pikk",
        'password_strength': "Parooli tugevus",
        'password_strength_very_weak': "Väga nõrk",
        'password_strength_weak': "Nõrk",
        'password_strength_medium': "Keskmine",
        'password_strength_strong': "Tugev",
        'password_strength_very_strong': "Väga tugev",
        'password_char_count': "({0} tähemärki)",
        'password_match': "✓ Ühtivad",
        'password_no_match': "✗ Paroolid ei ühti",
        'password_show': "Näita",
        'password_hide': "Peida",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Paroolihaldus",
        'password_table_filename': "Failinimi",
        'password_table_password': "Parool",
        'password_count': "{0} salvestatud parooli",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Pole salvestatud paroole",
        'password_copied': "{0} parooli kopeeritud",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Kas soovite kindlasti kustutada parooli faili '{0}' jaoks?",
        'password_delete_multiple': "Kas soovite kindlasti kustutada {0} valitud parooli?",
        'password_delete_all_confirm': "Kas soovite kindlasti kustutada kõik {0} salvestatud parooli?",
        'password_deleted': "{0} parooli kustutatud",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Kõik paroolid kustutati",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Parooligeneraator",
        'generator_generated': "Genereeritud parool:",
        'generator_regenerate': "Genereeri uuesti",
        'generator_copy': "Kopeeri",
        'generator_use': "Kasuta",
        'generator_settings': "Seaded",
        'generator_length': "Pikkus:",
        'generator_group_every': "Eraldaja iga",
        'generator_group_chars': "märgi järel.    Eraldaja:",
        'generator_uppercase': "Suurtähed (A-Z)",
        'generator_lowercase': "Väiketähed (a-z)",
        'generator_digits': "Numbrid (0-9)",
        'generator_symbols': "Sümbolid (!@#$%^&*)",
        'generator_exclude': "Välja jäetud:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Peaparool vajalik",
        'master_password_setup': "Sea peaparool",
        'master_password_change': "Muuda peaparooli",
        'master_password_enter': "Palun sisestage oma peaparool",
        'master_password_choose': "Valige tugev peaparool (vähemalt 8 tähemärki)",
        'master_password_new': "Palun sisestage oma uus peaparool",
        'master_password_confirm': "Kinnitage parool",
        'master_password_authenticate': "Autendi",
        'master_password_success': "Peaparool edukalt seatud.",
        'master_password_changed': "Peaparool edukalt muudetud.",
        'master_password_removed': "Peaparool ja kõik paroolid kustutati.",
        'master_password_remove': "Eemalda peaparool",
        'master_password_remove_confirm': "Kas olete KINDLALT veendunud, et soovite KÕIK paroolid kustutada?\n\nSee toiming on PÖÖRDAMATU!",
        'master_password_export_before': "Kas soovite enne varukoopia eksportida?",
        'master_password_export_delete': "Ekspordi ja kustuta",
        'master_password_delete_now': "Kustuta kohe",
        'master_password_for_signatures': "Allkirjade kasutamiseks peate seadistama peaparooli.\n\nKas soovite nüüd peaparooli seadistada?",
        'master_password_for_private': "Privaatsete tekstiblokkide kasutamiseks peate seadistama peaparooli.\n\nKas soovite nüüd peaparooli seadistada?",
        'master_password_info': """
            <b>🔐 ILMA PEAPAROOLITA:</b><br>
            • Paroolide kuvamine, kopeerimine ja eksportimine pole võimalik<br>
            • Paroolide kustutamine on alati võimalik (ka ilma peaparoolita)<br><br>

            <b>🔐 PEAPAROOLIGA:</b><br>
            • Kõik funktsioonid saadaval pärast autentimist<br>
            • Paroolid krüpteeritakse peaparooliga<br>
            • Minimaalne pikkus: 8 tähemärki<br>
            • Turvaline SHA-256 räsi salvestus<br><br>

            <b>TÄHTIS:</b><br>
            • Peaparooli kaotamisel pole paroole võimalik taastada<br>
            • Peaparooli eemaldamisel KUSTUTATAKSE KÕIK paroolid<br>
            • Enne kustutamist on saadaval ekspordi võimalus<br>
            • Peaparooli saab igal ajal muuta
        """,
        'signature_auth_disabled': "Keela parooliküsimine allkirjade jaoks",
        'template_auth_disabled': "Keela parooliküsimine privaatsete tekstiblokkide jaoks",
        'master_password_for_signatures_settings': "Allkirjade kasutamiseks peate seadistama peaparooli.\n\nMinge Seaded - Paroolihaldus",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Kaitse PDF",
        'protect_info': "Faili '{0}' kaitstakse parooliga.",
        'protect_instruction': "Palun sisestage soovitud parool kaks korda, et dokumenti kaitsta, või kasutage parooligeneraatorit sisestusvälja paremal küljel.",
        'protect_success': "PDF kaitsti edukalt ja salvestati asukohta:\n{0}\n\nParool: {1}\n\nKas soovite kaitstud PDF-i nüüd avada?",
        'protect_open': "Jah",
        'protect_skip': "Ei",
        'protect_error': "Viga PDF-i kaitsmisel",
        'protect_open_title': "kaitstud PDF avamine",
        'protect_question': "Valmis. Kas soovite kaitstud PDF-i nüüd avada? Jah või Ei?",
        'password_cancel': "Parooli dialoog tühistati",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Kustuta leheküljed",
        'pages_extract': "Eralda leheküljed",
        'pages_insert': "Lisa leheküljed",
        'pages_move': "Liiguta leheküljed",
        'pages_delete_options': "Kustutamise valikud",
        'pages_delete_empty': "Kustuta kõik tühjad leheküljed",
        'pages_delete_current': "Kustuta praegune lehekülg",
        'pages_delete_range': "Kustuta lehekülgede vahemik",
        'pages_extract_options': "Eraldamise valikud",
        'pages_extract_current': "Eralda praegune lehekülg",
        'pages_extract_range': "Eralda lehekülgede vahemik",
        'pages_insert_position': "Sisestamise koht",
        'pages_insert_before': "Sisesta enne lehekülge:",
        'pages_insert_select': "Vali PDF",
        'pages_insert_none': "PDF-i pole valitud",
        'pages_move_source': "Teisaldatavad leheküljed",
        'pages_move_from': "Leheküljelt:",
        'pages_move_to': "Leheküljeni:",
        'pages_move_target': "Sihtkoht",
        'pages_move_before': "Teisalda enne lehekülge:",
        'pages_move_hint': "Märkus: lehekülg 1 = algus, {0} = lõpp",
        'pages_range_invalid': "Alguse lehekülg peab olema väiksem või võrdne lõpu leheküljega.",
        'pages_position_invalid': "Sihtkoht ei tohi asuda teisaldatavas vahemikus.",
        'pages_no_pdf_selected': "PDF-i pole valitud.",
        'pages_deleted': "Kustutati {0} lehekülge.",
        'pages_extracted': "Eraldati: {0}\nSalvestati asukohta: {1}\nFaili suurus: {2:.1f} KB",
        'pages_inserted': "Lisati {0} lehekülge",
        'pages_moved': "Teisaldati {0} lehekülge.",
        'pages_deleted_none': "Ühtegi lehekülge ei kustutatud.",
        'pages_delete_progress': "Lehekülgede kustutamine...",
        'pages_deleted_with_backup': "Kustutati {0} lehekülge.\n\nVarukoopia: {1}",
        'pages_deleted_voice': "Loodi varukoopia ja kustutati {0} lehekülge.",
        'info': "Teave",
        'error_dialog_creation': "Dialoogi ei õnnestunud luua",
        'extract_page_single': "Eralda lehekülg {0}",
        'extract_page_range': "Eralda leheküljed {0}-{1}",
        'extract_success_voice': "Leheküljed edukalt eraldatud",
        'extract_error_format': "Viga eraldamisel: {0}",
        'pages_inserted_voice': "Lisati {0} lehekülge.",
        'insert_error_format': "Viga lisamisel: {0}",
        'pages_move_progress': "Lehekülgede teisaldamine...",
        'pages_moved_with_backup': "Teisaldati {0} lehekülge.\n\nVarukoopia: {1}",
        'move_success_title': "Edukalt teisaldatud",
        'pages_moved_voice': "{0} lehekülge edukalt teisaldatud",
        'mark_removed': "Lehekülje {0} märge eemaldatud",
        'mark_empty': "Lehekülg {0} märgitud tühjaks",
        'mark_export_removed': "Lehekülje {0} ekspordi märge eemaldatud",
        'mark_export': "Lehekülg {0} märgitud ekspordiks",
        'no_empty_pages': "Kustutamiseks pole tühje lehekülgi märgitud",
        'delete_empty_confirm': "Kas soovite kustutada kõik {0} märgitud tühja lehekülge?",
        'delete_empty_confirm_voice': "Kas kustutada nüüd kõik {0} märgitud tühja lehekülge? Jah või Ei.",
        'empty_pages_deleted': "{0} tühja lehekülge kustutatud",
        'no_export_pages': "Ekspordiks pole lehekülgi märgitud",
        'overwrite_title': "Kas kirjutada olemasolev fail üle?",
        'overwrite_question': "Fail\n\n{0}\n\non juba olemas.\nKas soovite selle üle kirjutada?",
        'overwrite_voice': "Kas kirjutada olemasolev fail üle? Jah või Ei.",
        'page_skipped': "Lehekülg {0} jäeti vahele",
        'export_complete': "Eksport lõpetatud.",
        'export_complete_voice': "Eksport on lõpetatud.",
        'no_pages_exported': "Ühtegi lehekülge ei eksporditud",
        'export_cancelled': "Eksport tühistati",
        'pages_exported': "{0} lehekülge eksporditud asukohta {1}",
        'export_page_title': "Ekspordi lehekülg",
        'page_exported': "Lehekülg {0} eksporditud asukohta {1}",
        'export_error': "Viga eksportimisel",
        'export_marked_title': "Ekspordi märgitud leheküljed",
        'rotate_all_title': "pööra kõiki lehekülgi",
        'rotate_all_question': "Kas soovite kõiki lehekülgi 90 kraadi paremale pöörata?",
        'rotate_all_voice': "Kas soovite kõiki lehekülgi 90 kraadi paremale pöörata? Jah või Ei?",
        'all_pages_rotated': "Kõik leheküljed pööratud",
        'page_rotated': "Lehekülg {0} pööratud",
        'rotate_error': "Lehekülge ei õnnestunud pöörata",
        'delete_page_confirm': "Kas soovite kustutada lehekülje {0}?",
        'delete_page_confirm_voice': "Kas soovite kindlasti kustutada lehekülje {0}? Jah või Ei.",
        'page_deleted': "Lehekülg {0} kustutatud",
        'delete_error': "Lehekülge ei õnnestunud kustutada",
        'pages_deleted_voice': "{0} lehekülge kustutatud",
        'pages_exported_split': "{0} lehekülge eksporditi edukalt.",
        'pages_skipped': "{0} lehekülge jäeti vahele.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Eralda leheküljed (täpsemalt)",
        'pdf_splitter_title': "PDF-i poolitaja ja eraldaja",
        'pdf_splitter_load': " Vali PDF-fail",
        'pdf_splitter_info': "Palun valige oma PDF-dokumendi jaoks valik",
        'pdf_splitter_basic': "Põhitoimingud",
        'pdf_splitter_single': "Jaga üksikuteks lehekülgedeks",
        'pdf_splitter_range': "Eralda leheküljed:",
        'pdf_splitter_range_placeholder': "nt 1-3,5,7-9",
        'pdf_splitter_clean': "Puhastustoimingud",
        'pdf_splitter_remove_empty': "Eemalda kõik tühjad leheküljed",
        'pdf_splitter_remove': "Kustuta lehekülgede vahemik:",
        'pdf_splitter_remove_placeholder': "nt 2,4-6",
        'pdf_splitter_process': "Töötle PDF",
        'pdf_splitter_loaded': "PDF laaditud. Palun valige valik",
        'pdf_read_error': "PDF-i ei õnnestunud lugeda",
        'pages': "Leheküljed",
        'pages_created': "Leheküljed loodud",
        'range_empty': "Palun sisestage lehekülgede vahemik",
        'range_invalid': "Vigane lehekülgede vahemik",
        'range_created': "Loodi uus PDF valitud lehekülgedega:\n{0}",
        'empty_removed': "{0} tühja lehekülge eemaldati.\nVäljund: {1}",
        'remove_empty': "Palun sisestage eemaldatavad leheküljed",
        'remove_invalid': "Vigased eemaldatavad leheküljed",
        'remove_done': "Puhastatud PDF loodi:\n{0}",
        'open_folder': "Ava kaust",
        'show_in_finder': "Kuva Finderis",
        'pdf_splitter_no_pdf': "Palun laadige esmalt PDF-fail.",
        'process_error': "Viga PDF-i töötlemisel",
        'pages_created_voice': "{0} lehekülge loodud",
        'range_created_voice': "Loodi PDF valitud lehekülgedega",
        'empty_removed_voice': "{0} tühja lehekülge eemaldati",
        'remove_done_voice': "Puhastatud PDF loodi",
        'pdf_splitter_split_groups': "Iga pidev grupp eraldi faili",
        'range_created_single': "Loodi uus PDF:\n{0}",
        'range_created_multiple': "Loodi {0} PDF-faili.",
        'range_created_voice_single': "Loodi üks PDF valitud lehekülgedega",
        'range_created_voice_multiple': "Loodi {0} PDF-faili",
        'empty_removed_none_left': "Ühtegi lehekülge pole järele jäänud",
        'empty_removed_all_empty': "Kõik leheküljed tuvastati tühjadena ja need eemaldataks. Ühtegi faili ei loodud.",
        'preview_single': "Eelvaade: {0}",
        'preview_enter_range': "Palun sisestage lehekülgede vahemik.",
        'preview_invalid_range': "Vigane lehekülgede vahemik.",
        'preview_file': "Eelvaade: {0}",
        'preview_files': "Eelvaade: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Prinditöö alustamine",
        'print_sent': "Prinditöö saadetud",
        'print_now': "Prindi kohe",
        'print_error': "Viga kohese printimisega",
        'print_limited': "Prindifunktsioon on selles süsteemis piiratud",
        'print_error_format': "Viga kohese printimisega: {0}",
        'warning': "Hoiatus",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Lülitu heledasse režiimi",
        'mode_switch_to_dark': "Lülitu tumedasse režiimi",
        'mode_dark_activated': "Tume režiim aktiveeritud",
        'mode_light_activated': "Hele režiim aktiveeritud",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Täisvaade",
        'zoom_two_pages': "Kaks lehekülge kõrvuti",
        'zoom_overview': "Ülevaaterežiim",
        'zoom_cannot_during_search': "Suumimine pole otsingu ajal võimalik",
        'zoom_exit_first': "Palun väljuge kõigepealt suumist",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Lohista ja aseta on sisse lülitatud",
        'drag_disabled': "Lohista ja aseta on välja lülitatud",
        'drag_page_grab': "Lehekülg {0} haaratud",
        'drag_page_dropped': "Lehekülg {0} lisatud asukohta {1}",
        'drag_position_invalid': "Vigane asukoht",
        'drag_same_position': "Lehekülg {0} jääb asukohta {0}",
        'drag_error': "Viga teisaldamisel",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Tekstisisestus täiustatud vorminduse ja tekstiblokkide haldusega",
        'text_templates': "Saadaval olevad tekstiblokid:",
        'text_name': "Nimi",
        'text_preview': "Teksti eelvaade",
        'text_enter': "Tekst:",
        'text_font_size': "Fondi suurus:",
        'text_formatting': "Vormindus:",
        'text_bold': "Rasvane",
        'text_italic': "Kaldkiri",
        'text_underline': "Allajoonitud",
        'text_alignment': "Joondus:",
        'text_left': "Vasakule",
        'text_center': "Keskele",
        'text_right': "Paremale",
        'text_color': "Teksti värv:",
        'text_opacity': "Läbipaistmatus:",
        'text_word_wrap': "Reaümbrus:",
        'text_auto': "Automaatne",
        'text_page_width_95': "Lehe laius (95%)",
        'text_page_width_85': "Väga lai (85%)",
        'text_page_width_75': "Laiem (75%)",
        'text_page_width_60': "Lai (60%)",
        'text_page_width_50': "Keskmine (50%)",
        'text_page_width_30': "Kitsas (30%)",
        'text_page_width_20': "Kitsam (20%)",
        'text_page_width_10': "Väga kitsas (10%)",
        'text_no_wrap': "Pole reaümbrust",
        'text_private': "Privaatne tekstiblokk (vajab autentimist)",
        'text_preview_label': "Eelvaade:",
        'text_preview_placeholder': "Siin kuvatakse teksti eelvaade...",
        'text_no_text': "(Pole teksti)",
        'text_save_template': "💾 Salvesta blokina",
        'text_delete_template': "🗑 Kustuta valitud tekstiblokk",
        'text_show_private': "Näita privaatseid",
        'text_hide_private': "Peida privaatsed",
        'text_use': "✅ Kasuta teksti",
        'text_saved': "Tekstiblokk salvestatud kui:\n{0}",
        'text_saved_voice': "Tekstiblokk salvestatud",
        'text_deleted': "Tekstiblokk kustutatud",
        'text_no_text_to_save': "Pole salvestatavat teksti.",
        'text_no_templates': "Ühtegi tekstiblokki ei leitud",
        'text_private_master_required': "Privaatseid blokke saab kasutada ainult siis, kui peaparool on seadistatud.\n\nKas soovite nüüd peaparooli seadistada?",
        'text_filename': "Tekstibloki failinimi (ilma 'Text_' ja '.txt'):",
        'text_filename_hint': "Näide: 'Telefon Kodukontor' salvestatakse kui 'Text_Telefon Kodukontor.txt'",
        'text_save_hint': "Tekstiblokk salvestatakse automaatselt koos vormindusega.",
        'text_guide_title': "Tekstisisestus – Juhend",
        'text_delete_confirm': "Kas soovite kindlasti kustutada tekstibloki?\n\nFail: {0}\nTekst: {1}...",
        'text_make_public': "Märgi avalikuks",
        'text_make_private': "Märgi privaatseks",
        'text_privacy_changed': "Privaatsuse olekut muudetud",
        'text_private_always': "Privaatsed alati nähtavad (seade)",
        'text_mode_required': "Palun lülitage esmalt sisse tekstirežiim",
        'text_continue_editing': "Jätka redigeerimist – kursor teksti lõpus",
        'text_no_input': "Teksti ei sisestatud – tekst loobutud",
        'save_dialog_question': "Kuidas soovite jätkata?",
        'text_save_question': "Kas salvestada kõik tekstid ja ristid, kohandada, jätkata redigeerimist või loobuda?",
        'copy_cross': "Rist kopeeritud",
        'paste_cross': "Rist lisatud",
        'paste_text': "Tekst lisatud",
        'cross_discarded': "Rist loobutud",
        'all_discarded': "Kõik loobutud",
        'text_discarded': "Tekst loobutud",
        'no_texts_to_save': "Pole salvestatavaid tekste",
        'no_valid_texts': "Pole kehtivaid tekste salvestamiseks",
        'text_word_singular': "tekst",
        'text_word_plural': "teksti",
        'cross_word_singular': "rist",
        'cross_word_plural': "risti",
        'texts_saved_title': "Tekstid salvestatud",
        'texts_crosses_saved': "{0} {1} ja {2} {3} lisati PDF-i.\n\nPDF laaditi uuesti...",
        'texts_crosses_saved_voice': "{0} {1} ja {2} {3} salvestatud.",
        'texts_saved': "{0} {1} lisati PDF-i.\n\nPDF laaditi uuesti...",
        'texts_saved_voice': "{0} {1} salvestatud.",
        'crosses_saved': "{0} {1} lisati PDF-i.\n\nPDF laaditi uuesti...",
        'crosses_saved_voice': "{0} {1} salvestatud.",
        'elements_saved': "{0} elementi lisati PDF-i.\n\nPDF laaditi uuesti...",
        'elements_saved_voice': "{0} elementi salvestatud.",
        'text_window_load_error': "Tekstiakent ei õnnestunud laadida",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Tekstisisestus ja tekstiblokid – Üksikasjalik juhend**

        **1. Teksti lisamine ja redigeerimine**
        - Paremklõpsake dokumendis soovitud kohas ja valige "Lisa tekst".
        - Avaneb dialoog, kus saate teksti sisestada ja vormindada:
        • Fondi suurus, rasvane, kaldkiri, allajoonitud
        • Teksti värv (vabalt valitav)
        • Läbipaistmatus (katvus) liuguri abil
        • Reaümbrus (erinevad laiused, nt lehe laius, kitsas, pole reaümbrust)
        - Kinnitamise järel ilmub tekst klõpsukohta. Saate seda hiire või nooleklahvidega liigutada.
        - Topeltklõps tekstil avab redigeerimisrežiimi; ESC väljub sellest.

        **2. Tekstiblokkide (mallide) haldamine**
        - Teksti dialoogi vasakus servas näete kõigi salvestatud tekstiblokkide loendit.
        - **Bloki salvestamine:** Sisestage tekst, vormindage see ja klõpsake nuppu "💾 Salvesta blokina". Sisestage failinimi (ilma laiendita).
        - **Bloki laadimine:** Klõpsake loendis soovitud nimel. Tekst ja vormindus võetakse üle ja neid saab vajadusel kohandada.
        - **Kustutamine:** Paremklõpsake blokil, et see kustutada või selle privaatsuse olekut muuta.

        **3. Privaatsed tekstiblokid (peaparool)**
        - Kui olete seadistanud peaparooli (jaotises Seaded → Paroolihaldus), saate blokke märkida "privaatseks".
        - Enne salvestamist märkige dialoogis ruut "Privaatne tekstiblokk".
        - Privaatseid blokke kuvatakse loendis ainult siis, kui olete üks kord sessiooni jooksul sisestanud oma peaparooli (autentimine lukusümboli kaudu või esimesel juurdepääsul).
        - Nii saate kaitsta konfidentsiaalseid tekstiblokke volitamata juurdepääsu eest.

        **4. Ristide lisamine**
        - Kontekstimenüüst saate lisada ka graafilise risti (nt märkeruutude jaoks).
        - Ristide suurust, joone paksust ja värvi saab globaalselt seadetes kohandada (menüü "Seaded" → "Risti seaded").
        - Paremklõpsake olemasoleval ristil, et seda individuaalselt muuta.

        **5. Grupitoimingud**
        - Kui olete ühele leheküljele paigutanud mitu teksti või risti, saate need kõik korraga salvestada või loobuda kontekstimenüüst (paremklõps tekstirežiimis).
        - Salvestamisel sisestatakse kõik elemendid PDF-i ja need jäävad vektorgraafikana alles.

        **6. Klaviatuuri otseteed tekstirežiimis**
        - Nooleklahvid: elemendi liigutamine
        - Ctrl+nooleklahvid: suuremad sammud
        - Enter: salvestusdialoogi avamine (salvesta kõik / kohanda / loobu)
        - ESC: praegusest elemendist loobumine
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Tekstisisestus ja tekstiblokid – Üksikasjalik juhend</strong></p>

        <p><strong>1. Teksti lisamine ja redigeerimine</strong></p>
        <ul>
        <li>Paremklõpsake dokumendis soovitud kohas ja valige "Lisa tekst".</li>
        <li>Avaneb dialoog, kus saate teksti sisestada ja vormindada:<br/>
        • Fondi suurus, rasvane, kaldkiri, allajoonitud<br/>
        • Teksti värv (vabalt valitav)<br/>
        • Läbipaistmatus (katvus) liuguri abil<br/>
        • Reaümbrus (erinevad laiused, nt lehe laius, kitsas, pole reaümbrust)</li>
        <li>Kinnitamise järel ilmub tekst klõpsukohta. Saate seda hiire või nooleklahvidega liigutada.</li>
        <li>Topeltklõps tekstil avab redigeerimisrežiimi; ESC väljub sellest.</li>
        </ul>

        <p><strong>2. Tekstiblokkide (mallide) haldamine</strong></p>
        <ul>
        <li>Teksti dialoogi vasakus servas näete kõigi salvestatud tekstiblokkide loendit.</li>
        <li><strong>Bloki salvestamine:</strong> Sisestage tekst, vormindage see ja klõpsake nuppu "💾 Salvesta blokina". Sisestage failinimi (ilma laiendita).</li>
        <li><strong>Bloki laadimine:</strong> Klõpsake loendis soovitud nimel. Tekst ja vormindus võetakse üle ja neid saab vajadusel kohandada.</li>
        <li><strong>Kustutamine:</strong> Paremklõpsake blokil, et see kustutada või selle privaatsuse olekut muuta.</li>
        </ul>

        <p><strong>3. Privaatsed tekstiblokid (peaparool)</strong></p>
        <ul>
        <li>Kui olete seadistanud peaparooli (jaotises Seaded → Paroolihaldus), saate blokke märkida "privaatseks".</li>
        <li>Enne salvestamist märkige dialoogis ruut "Privaatne tekstiblokk".</li>
        <li>Privaatseid blokke kuvatakse loendis ainult siis, kui olete üks kord sessiooni jooksul sisestanud oma peaparooli (autentimine lukusümboli kaudu või esimesel juurdepääsul).</li>
        <li>Nii saate kaitsta konfidentsiaalseid tekstiblokke volitamata juurdepääsu eest.</li>
        </ul>

        <p><strong>4. Ristide lisamine</strong></p>
        <ul>
        <li>Kontekstimenüüst saate lisada ka graafilise risti (nt märkeruutude jaoks).</li>
        <li>Ristide suurust, joone paksust ja värvi saab globaalselt seadetes kohandada (menüü "Seaded" → "Risti seaded").</li>
        <li>Paremklõpsake olemasoleval ristil, et seda individuaalselt muuta.</li>
        </ul>

        <p><strong>5. Grupitoimingud</strong></p>
        <ul>
        <li>Kui olete ühele leheküljele paigutanud mitu teksti või risti, saate need kõik korraga salvestada või loobuda kontekstimenüüst (paremklõps tekstirežiimis).</li>
        <li>Salvestamisel sisestatakse kõik elemendid PDF-i ja need jäävad vektorgraafikana alles.</li>
        </ul>

        <p><strong>6. Klaviatuuri otseteed tekstirežiimis</strong></p>
        <ul>
        <li>Nooleklahvid: elemendi liigutamine</li>
        <li>Ctrl+nooleklahvid: suuremad sammud</li>
        <li>Enter: salvestusdialoogi avamine (salvesta kõik / kohanda / loobu)</li>
        <li>ESC: praegusest elemendist loobumine</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Risti seaded",
        'cross_properties': "Risti omadused",
        'cross_size': "Suurus (px):",
        'cross_line_width': "Joone paksus:",
        'cross_color': "Värv:",
        'cross_choose_color': "Vali",
        'cross_fine_tuning': "Täppisseadistamine salvestamisel (pikslit)",
        'cross_offset_x': "X-nihe:",
        'cross_offset_y': "Y-nihe:",
        'cross_offset_x_tooltip': "Negatiivsed väärtused nihutavad risti salvestamisel vasakule, positiivsed paremale",
        'cross_offset_y_tooltip': "Negatiivsed väärtused nihutavad risti salvestamisel üles, positiivsed alla",
        'cross_preview': "Eelvaade",
        'cross_save': "Rakenda seaded",
        'cross_customized': "Risti kohandatud",
        'cross_settings_applied': "Risti seaded salvestatud.\nSuurus: {0}px, joone paksus: {1}px\n{2}",
        'cross_updated_count': "{0} olemasolevat risti värskendati.",
        'cross_no_crosses': "Ühtegi olemasolevat risti ei leitud.",
        'cross_settings_applied_all': "Risti seaded rakendatud kõigile {0} ristile",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Allkirja seaded",
        'signature_1': "Allkiri 1",
        'signature_2': "Allkiri 2",
        'signature_select': "Vali allkiri",
        'signature_add': "➕ Lisa uus allkiri...",
        'signature_size': "Allkirja {0} suurus (%):",
        'signature_common': "Üldised seaded",
        'signature_timestamp': "Lisa ajatempel automaatselt",
        'signature_location': "Vaikimisi asukoht:",
        'signature_timestamp_size': "Ajatempli fondi suurus:",
        'signature_no_files': "-- Allkirju ei leitud --",
        'signature_insert': "Lisa allkiri",
        'signature_insert_1': "Lisa allkiri 1",
        'signature_insert_2': "Lisa allkiri 2",
        'signature_customize': " Kohanda allkirja",
        'signature_discard': " Loobu sellest allkirjast",
        'signature_save_all': " Salvesta kõik allkirjad",
        'signature_discard_all': " Loobu kõigist allkirjadest",
        'signature_guide_title': "Allkirjad – Juhend",
        'signature_guide': """
📝 Allkirjad – Lühijuhend

- Seadista peaparool
- Seadista allkirjad menüüs Seaded
  (suurus, ajatempel ...)
- Lisa PAREMKLÕPSUGA soovitud asukohta
  (peaparooli on vaja üks kord sessiooni jooksul)
- Liiguta allkirja hiire või nooleklahvidega
- Mitu allkirja saab lisada üksteise järel
- Iga allkirja saab individuaalselt kohandada
- Loobu üksikust allkirjast
- Salvesta / loobu kõigist allkirjadest korraga
- Alternatiivina saab kasutada ka menüüriba.
        """,
        'signature_placeholder': "Eelvaade pole saadaval",
        'signature_info': "Allkiri {0}: {1}×{2} px ({3}% väärtusest {4}×{5})",
        'signature_info_placeholder': "Allkirja {0} seaded",
        'signature_inserted': "Allkiri {0} lisatud leheküljele {1}",
        'signature_deleted': "Allkiri kustutatud",
        'signature_copied': "Allkiri kopeeritud",
        'signature_pasted': "Allkiri {0} lisatud",
        'signature_saved': "{0} allkirja lisati PDF-i.\n\nPDF laaditi uuesti...",
        'signature_saved_voice': "{0} allkirja salvestatud",
        'mode_replace_signature_format': "Välju režiimist ja lisa allkiri {0}",
        'mode_conflict_voice_signature': "Režiim {0} on aktiivne. Kas väljuda ja lisada allkiri?",
        'signature_not_configured': "Allkiri {0} pole seadistatud",
        'signature_file_not_found': "Allkirja faili ei leitud",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Pole kopeeritud allkirja",
        'no_signatures_to_save': "Pole salvestatavaid allkirju",
        'signature_save_question': "Kas salvestada kõik allkirjad, kohandada või loobuda sellest?",
        'signatures_saved_title': "Allkirjad salvestatud",
        'signatures_saved': "{0} allkirja lisati PDF-i.\n\nPDF laaditi uuesti...",
        'signatures_saved_voice': "{0} allkirja salvestatud.",
        'all_signatures_discarded': "Kõigist allkirjadest loobutud",
        'signature_settings_saved': "Allkirja seaded salvestatud",
        'signature_cancelled': "Allkirjast loobutud",
        'signature_active_title': "Allkiri aktiivne",
        'signature_replace_question': "Allkiri on juba aktiivne.\n\nKas soovite praeguse allkirja asendada?",
        'signature_replace': "Asenda allkiri",
        'signature_replace_voice': "Kas asendada praegune allkiri või tühistada?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Pildi seaded",
        'image_common': "Üldised pildi seaded",
        'image_keep_aspect': "Säilita kuvasuhe lohistamisel",
        'image_default_size': "Vaikimisi suurus (%):",
        'image_dark_invert': "Inverteeri pilte tumedas režiimis",
        'image_dark_invert_tooltip': "Sisse lülitatud: pildid inverteeritakse parema nähtavuse tagamiseks",
        'image_fine_tuning': "Täppisseadistamine (pikslit)",
        'image_offset_x': "X-nihe:",
        'image_offset_y': "Y-nihe:",
        'image_offset_x_tooltip': "Negatiivsed väärtused nihutavad pilti salvestamisel vasakule, positiivsed paremale",
        'image_offset_y_tooltip': "Negatiivsed väärtused nihutavad pilti salvestamisel üles, positiivsed alla",
        'image_select': "Vali pilt",
        'image_insert': "Lisa pilt",
        'image_customize': " Kohanda pilti",
        'image_aspect': " Säilita kuvasuhe",
        'image_discard': " Loobu sellest pildist",
        'image_save_all': " Salvesta kõik pildid",
        'image_discard_all': " Loobu kõigist piltidest",
        'image_filter': "Pildid",
        'image_guide_title': "Piltide lisamine – Juhend",
        'image_guide': """
📷 Piltide lisamine PDF-i – Lühijuhend:

1. Paremklõpsake soovitud kohas
2. "Lisa pilt" → valige pilt
3. Paigutage pilt: lohistage hiirega
4. Kohandage suurust: lohistage nurkadest/servadest
5. Kuvasuhte säilitamine: klahv [A]
6. Täiendavad kohandused: paremklõpsake pildil

Näpunäide: Kontekstimenüüst saate seadeid muuta.
        """,
        'image_inserted': "Pilt {0} lisatud leheküljele {1}",
        'image_deleted': "Pildist loobutud",
        'image_copied': "Pilt kopeeritud",
        'image_pasted': "Pilt lisatud",
        'image_saved': "{0} pilti lisati PDF-i.\n\nPDF laaditi uuesti...",
        'image_saved_voice': "{0} pilti salvestatud",
        'image_aspect_on': "sees",
        'image_aspect_off': "väljas",
        'image_aspect_toggle': "Kuvasuhte säilitamine {0}",
        'image_reset': "Pilt taastatud algsele suurusele",
        'image_replaced': "Pilt asendatud",
        'image_invalid': "Vigane pilt",
        'mode_replace_image': "Lisa pilt",
        'mode_conflict_voice_image': "Režiim {0} on aktiivne. Kas väljuda ja lisada pilt?",
        'image_active_title': "Pilt aktiivne",
        'image_replace_question': "Pilt on juba aktiivne.\n\nKas soovite praeguse pildi asendada?",
        'image_replace': "Asenda pilt",
        'image_replace_voice': "Kas asendada praegune pilt või tühistada?",
        'image_filter_all': "Pildid (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Kõik failid (*.*)",
        'no_copied_image': "Pole kopeeritud pilti",
        'image_discarded': "Pildist loobutud",
        'image_save_question': "Kas salvestada kõik pildid, kohandada või loobuda sellest?",
        'no_images_to_save': "Pole salvestatavaid pilte",
        'no_valid_images': "Pole kehtivaid pilte salvestamiseks",
        'images_saved_title': "Pildid salvestatud",
        'images_saved': "{0} pilti lisati PDF-i.\n\nPDF laaditi uuesti...",
        'images_saved_voice': "{0} pilti salvestatud.",
        'all_images_discarded': "Kõigist piltidest loobutud",
        'image_settings_updated': "Pildi seaded värskendatud",
        'image_replace_title': "Vali uus pilt",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Kujundite seaded",
        'form_basic': "Põhiseaded",
        'form_default_type': "Vaikimisi kujundi tüüp:",
        'form_rectangle': "Ristkülik",
        'form_ellipse': "Ellips",
        'form_line': "Joon",
        'form_arrow': "Nool",
        'form_line_width': "Joone paksus:",
        'form_colors': "Värvid",
        'form_line_color': "Joone värv:",
        'form_fill_color': "Täitevärv:",
        'form_choose_color': "Vali",
        'form_transparent': "Läbipaistev taust (ainult joon)",
        'form_filled': "täidetud",
        'form_dark_mode': "Tume režiim",
        'form_dark_invert': "Inverteeri värve tumedas režiimis",
        'form_fine_tuning': "Täppisseadistamine (pikslit)",
        'form_offset_x': "X-nihe:",
        'form_offset_y': "Y-nihe:",
        'form_offset_x_tooltip': "Negatiivsed väärtused nihutavad kujundit salvestamisel vasakule, positiivsed paremale",
        'form_offset_y_tooltip': "Negatiivsed väärtused nihutavad kujundit salvestamisel üles, positiivsed alla",
        'form_preview': "Eelvaade",
        'form_insert': "Lisa kujund",
        'form_rectangle_insert': "Ristkülik",
        'form_ellipse_insert': "Ellips/ring",
        'form_line_insert': "Joon (2 klõpsu)",
        'form_arrow_insert': "Nool (2 klõpsu)",
        'form_customize': " Kohanda kujundit",
        'form_transparent_toggle': " Läbipaistev taust",
        'form_discard': " Loobu sellest kujundist",
        'form_save_all': " Salvesta kõik kujundid",
        'form_discard_all': " Loobu kõigist kujunditest",
        'form_guide_title': "Kujundite lisamine – Juhend",
        'form_guide': """
📐 Kujundite lisamine PDF-i – Lühijuhend:

1. Valige kujundi tüüp (ristkülik, ellips, joon, nool)
2. Klõpsake asukohta
   - Ristkülik/ellips: üks klõps paigutab kujundi
   - Joon/nool: kaks klõpsu algus- ja lõpp-punkti jaoks
3. Paigutage kujund: lohistage hiirega
4. Kohandage suurust: lohistage nurkadest/servadest
5. Salvesta kujund: Enter
6. Loobu kujundist: ESC
7. Täiendavad kohandused: paremklõpsake kujundil

Näpunäide: Kontekstimenüüst saate seadeid muuta.
        """,
        'form_inserted': "{0} lisatud leheküljele {1}",
        'form_deleted': "Kujund kustutatud",
        'form_copied': "Kujund kopeeritud",
        'form_pasted': "Kujund lisatud",
        'form_saved': "{0} kujundit lisati PDF-i.\n\nPDF laaditi uuesti...",
        'form_saved_voice': "{0} kujundit salvestatud",
        'form_reset': "Kujund taastatud vaikimisi suurusele",
        'form_transparent_on': "sees",
        'form_transparent_off': "väljas",
        'form_transparent_toggled': "Läbipaistev taust {0}",
        'form_line_cancel': "Joone joonistamine tühistatud",
        'form_second_click': "Klõpsake nüüd {0} lõpp-punkti",
        'mode_replace_form': "Lisa kujund",
        'mode_conflict_voice_form': "Režiim {0} on aktiivne. Kas väljuda ja lisada kujund?",
        'form_settings_updated': "Kujundite seaded värskendatud",
        'form_unknown': "Kujund",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klõpsake alguspunkti",
        'form_line_guide_2': "2. Klõpsake lõpp-punkti",
        'form_line_guide_3': "Joon tõmmatakse kahe punkti vahele.",
        'form_line_status_1': "Oodatakse esimest klõpsu...",
        'form_line_status_2': "Esimene punkt määratud: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Klõpsake nüüd lõpp-punkti...",
        'form_line_status_4': "Mõlemad punktid määratud.\nSalvestamiseks klõpsake nuppu 'Valmis'.",
        'form_line_reset': "Lähtesta",
        'form_line_finish': "Valmis",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopeeri (Cmd+C)",
        'paste': "Aseta (Cmd+V)",
        'copied': "Kopeeritud: {0}",
        'no_element_to_copy': "Kopeerimiseks pole elementi valitud",
        'no_copied_data': "Pole kopeeritud andmeid",
        'no_valid_position': "Asetamiseks pole kehtivat asukohta",
        'copy_text': "Tekst kopeeritud",
        'copy_image': "Pilt kopeeritud",
        'copy_form': "Kujund kopeeritud",
        'copy_signature': "Allkiri kopeeritud",
        'element_text': "Tekst",
        'element_image': "Pilt",
        'element_form': "Kujund",
        'element_signature': "Allkiri",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Režiimi konflikt",
        'mode_conflict_message': "Režiim '{0}' on juba aktiivne.\n\nKas soovite sellest väljuda ja {1}?",
        'mode_replace': "Välju režiimist ja {0}",
        'mode_cancel': "Tühista",
        'mode_replace_text': "lisada tekst",
        'mode_replace_cross': "lisada rist",
        'mode_replace_signature': "lisada allkiri",
        'mode_replace_image': "lisada pilt",
        'mode_replace_form': "lisada kujund",
        'mode_conflict_voice': "Režiim {0} on aktiivne. Kas väljuda ja lisada tekst?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Tekstisisestus",
        'active_mode_signature': "Allkiri",
        'active_mode_image': "Pilt",
        'active_mode_form': "Kujund",
        'active_mode_and': " ja ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Lisa",
        'insert_another_text': "Lisa tekst",
        'insert_another_cross': "Lisa rist",
        'insert_another_signature_1': "Allkiri 1",
        'insert_another_signature_2': "Allkiri 2",
        'insert_another_image': "Lisa pilt",
        'insert_another_form_rect': "Ristkülik",
        'insert_another_form_ellipse': "Ellips",
        'insert_another_form_line': "Joon (2 klõpsu)",
        'insert_another_form_arrow': "Nool (2 klõpsu)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Salvesta {0}",
        'save_dialog_message': "{0} salvestatakse leheküljele {1}.\n\nKuidas soovite jätkata?",
        'save_all': "Salvesta kõik {0}",
        'save_single': "Salvesta {0}",
        'save_customize': "Kohanda {0}",
        'save_discard': "Loobu sellest {0}",
        'save_continue': "Jätka redigeerimist",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Mine leheküljele {0}",
        'context_rotate': " Pööra lehekülg {0}",
        'context_delete': " Kustuta lehekülg {0}",
        'context_export': " Ekspordi lehekülg {0}",
        'context_mark_as': " Märgi lehekülg kui...",
        'context_mark_empty': " Tühi lehekülg",
        'context_unmark_empty': " Pole enam tühi",
        'context_mark_export': " Märgi ekspordiks",
        'context_unmark_export': " Ära enam ekspordi",
        'context_batch_actions': " Grupitoimingud",
        'context_batch_delete_empty': " Kustuta kõik {0} tühja lehekülge",
        'context_batch_export_single': " Ekspordi kõik {0} lehekülge (üks fail)",
        'context_batch_export_split': " Ekspordi kõik {0} lehekülge (eraldi)",
        'context_drag_start': " Alusta lohistamist",
        'context_drag_stop': " Lõpeta lohistamine",
        'context_insert': " Lisa",
        'context_insert_pages': " Lisa lehekülgi",
        'context_zoom': "Suum",
        'discard_mixed': "Loobu kõigist {0} {1} ja {2} {3}",
        'save_mixed': "Salvesta {0} {1} ja {2} {3}",
        'discard_texts': "Loobu kõigist {0} tekstist",
        'discard_text_single': "Loobu 1 tekstist",
        'save_texts': "Salvesta {0} teksti",
        'save_text_single': "Salvesta 1 tekst",
        'discard_crosses': "Loobu kõigist {0} ristist",
        'discard_cross_single': "Loobu 1 ristist",
        'save_crosses': "Salvesta {0} risti",
        'save_cross_single': "Salvesta 1 rist",
        'discard_signatures': "Loobu kõigist {0} allkirjast",
        'save_signature_single': "Salvesta 1 allkiri",
        'save_signatures': "Salvesta {0} allkirja",
        'discard_images': "Loobu kõigist {0} pildist",
        'save_image_single': "Salvesta 1 pilt",
        'save_images': "Salvesta {0} pilti",
        'discard_forms': "Loobu kõigist {0} kujundist",
        'save_form_single': "Salvesta 1 kujund",
        'save_forms': "Salvesta {0} kujundit",
        'cross_discard': "Loobu sellest ristist",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Ekspordi / impordi teave",
        'export_what': "📋 Mida eksporditakse?",
        'export_general': "Üldised seaded",
        'export_general_items': "• Kõneväljund (sees/väljas, kiirus)\n• Tume/ hele režiim\n• Varunduse seaded\n• OCR-i seaded",
        'export_image_form': "Pildi- ja kujundiseaded",
        'export_image_form_items': "• Pildi seaded (kuvasuhe, vaikimisi suurus)\n• Kujundi seaded (joone paksus, värvid)\n• Allkirja seaded (teed, suurused, ajatempel)",
        'export_passwords': "Paroolide andmebaas",
        'export_passwords_items': "• Kõik salvestatud PDF-paroolid\n• Valikuliselt krüpteeritud või dekrüpteeritud",
        'export_master': "Peaparooli seaded",
        'export_master_items': "• Peaparooli räsi\n• Allkirjade/tekstiblokkide seaded",
        'export_signatures': "Allkirjad ja tekstiblokid",
        'export_signatures_items': "• Kõik pildifailid (allkirjad)\n• Kõik tekstiblokid koos vormindusega\n• Privaatsed/avalikud märked",
        'export_import_warning': "⚠️ Olulised märkused",
        'export_import_note': "• Impordimisel KIRJUTATAKSE KÕIK praegused seaded ÜLE\n• Rakendus tuleb taaskäivitada\n• Olemasolevad allkirjad/tekstiblokid asendatakse",
        'export_master_note': "• Kui peaparool on määratud, saate valida:\n  - Dekrüpteeritud (paroolid selgetekstiliselt)\n  - Krüpteeritud (loetav ainult peaparooliga)",
        'export_security': "• Eksporditud ZIP-fail sisaldab konfidentsiaalseid andmeid\n• Hoidke seda turvaliselt (nt krüpteeritud USB-mälupulgal)\n• Faili kaotamisel on paroolid pöördumatult kadunud",
        'export_format': "📁 Ekspordi vorming",
        'export_format_desc': "Seaded salvestatakse ühte ZIP-faili:",
        'export_filename': "PDFDarkView_Seaded_YYYYMMDD_HHMMSS.zip",
        'export_success': "Seaded eksporditi edukalt",
        'export_failed': "Eksport ebaõnnestus",
        'export_import_question': "Kas soovite rakenduse nüüd taaskäivitada?",
        'export_password_question': "Peaparool on määratud.\n\nKas soovite paroolid eksportida dekrüpteeritult?\n(vastasel juhul eksporditakse need krüpteeritult)",
        'export_decrypt': "Ekspordi dekrüpteeritult",
        'export_encrypt': "Ekspordi krüpteeritult",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Teave",
        'info_title': "Teave PDF Dark View kohta",
        'info_version': "Versioon",
        'info_author': "Arendaja: Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Teave",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> on ligipääsetav PDF-vaatur, mis on spetsiaalselt välja töötatud nägemispuudega inimestele.</p>

            <p><strong>Põhiomadused:</strong></p>
            <ul>
                <li>Kontrastne, kohandatav liides</li>
                <li>Täielik klaviatuurijuhtimine</li>
                <li>Integreeritud kõne väljund</li>
                <li>OCR skannitud dokumentide jaoks</li>
                <li>Põhjalikud redigeerimistööriistad</li>
            </ul>

            <p>Toetatud on rohkem kui 50 keelt – nii et PDF-id on kõigile kättesaadavad.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funktsioonid",
        'info_features_intro': "PDF Dark View pakub teile järgmisi võimalusi:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Kuvamine ja navigeerimine</strong> – Tume/Hele režiim, lehitsemine, suumimine, hüpe lehele</li>
            <li><strong>OCR (tekstituvastus)</strong> – Muuda skannitud dokumendid otsitavaks ja kopeeritavaks</li>
            <li><strong>Redigeerimine</strong> – Teksti, ristide, allkirjade, piltide ja kujundite lisamine</li>
            <li><strong>Lehtede haldus</strong> – Kustutamine, eraldamine, lisamine, teisaldamine lohistamise teel</li>
            <li><strong>Eksport</strong> – Wordi, Pagesi või tekstina</li>
            <li><strong>Turvalisus</strong> – Paroolikaitse ja -haldus</li>
            <li><strong>Ligipääsetavus</strong> – Kõne väljund, klaviatuurijuhtimine, kõrge kontrastsus</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Kasutamine",
        'info_accessibility': "♿ Ligipääsetavus – täielik klaviatuurijuhtimine",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Üldine</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Ava PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Otsi</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Lülita tume/ hele režiim</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Prindi</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Välju</div>

        <div class="shortcut-cat">📖 Navigeerimine</div>
        <div class="shortcut-row"><kbd>Noolte klahvid</kbd> Lehitse leht lehe haaval</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Mine lehele</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Esimene leht</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Viimane leht</div>

        <div class="shortcut-cat">✏️ Redigeerimine</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Lisa tekst</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Kustuta lehed</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Eralda lehed</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Lisa lehed</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Teisalda lehed</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Pööra lehte</div>

        <div class="shortcut-cat">🖼️ Elementide teisaldamine</div>
        <div class="shortcut-row"><kbd>Noolte klahvid</kbd> Teisalda tekst/pilt/allkiri</div>
        <div class="shortcut-row"><kbd>Ctrl+Noolte klahvid</kbd> Suuremad sammud</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Salvesta</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Loobu</div>

        <div class="shortcut-cat">🗣️ Kõne väljund</div>
        <div class="shortcut-row"><kbd>F2</kbd> Lülita kõne väljund sisse/välja</div>
        """,
        'info_contextmenu': "📌 Tähtis: Kõik funktsioonid on saadaval ka kontekstimenüüst (parem hiirenupp)!",
        'info_accessibility_hint': "💡 Näpunäide: Kõne väljund (F2) hõlbustab orienteerumist ja annab tagasisidet menüüde ja dialoogide kohta.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Litsents & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Teave vastavalt § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Saksamaa<br>
        E-post: binhdiez64@gmail.com<br>
        Vastutav sisu eest: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Vastutuse välistamine</strong><br>
        Tarkvara on välja töötatud suurima hoolega. Täpsuse, täielikkuse ja funktsionaalsuse eest ei võeta mingit garantiid. Kasutamine toimub omal vastutusel.<br><br>

        <strong>📄 MIT-litsents (eraotstarbeline kasutamine)</strong><br>
        Autoriõigus (c) 2026 Toralf Schulz (BinhDiez)<br>
        Lubatud: tasuta kasutamine, eraviisilised muudatused, isiklikud koopiad.<br>
        Keelatud: müük, äriline kasutamine, autoriõiguste märgete eemaldamine.<br><br>

        <strong>🔧 Kolmandate osapoolte komponendid</strong><br>
        See tarkvara sisaldab komponente GPL, AGPL, Apache 2.0, BSD ja MIT litsentside alusel.<br>
        Edasilevitamisel tuleb järgida vastavaid litsentsitingimusi.<br><br>

        <strong>🌐 Avatud lähtekood</strong><br>
        Lähtekood on kättesaadav ning seda saab vaadata, muuta ja edasi levitada vastavalt vastavatele litsentsitingimustele.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Tänuavaldused",
        'info_credits': "Tänu avatud lähtekoodiga kogukonnale",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-i töötlus</li>
            <li><strong>PyQt5</strong> – Graafiline liides</li>
            <li><strong>Tesseract OCR</strong> – Tekstituvastus</li>
            <li><strong>OCRmyPDF</strong> – OCR-i integratsioon</li>
            <li><strong>python-docx</strong> – Wordi eksport</li>
            <li><strong>qtawesome</strong> – Ikoonid</li>
            <li><strong>DeepSeek</strong> – Tugi tõlgete juures (50+ keelt)</li>
            <li><strong>Kõik kasutajad</strong> – Väärtusliku tagasiside eest</li>
            <li><strong>Avatud lähtekoodiga kogukond</strong> – Suurepäraste teekide eest</li>
        </ul>
        """,


        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Keeled",
        'info_languages_header': "🌍 Keeletoetus",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View toetab praegu <strong>62 keelt</strong> – tagamaks, et tarkvara oleks kogu maailmas hõlpsasti kasutatav.</p>

            <p><strong>📖 Täielik keelte nimekiri (seisuga märts 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaani</li>
                    <li>🇦🇱 Albaania (Shqip)</li>
                    <li>🇩🇿 Araabia (العربية)</li>
                    <li>🇮🇩 Bali (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Birma (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnia (Bosanski)</li>
                    <li>🇧🇬 Bulgaaria (Български)</li>
                    <li>🇨🇳 Hiina (中文)</li>
                    <li>🇩🇰 Taani (Dansk)</li>
                    <li>🇩🇪 Saksa (Deutsch)</li>
                    <li>🇬🇧 Inglise (English)</li>
                    <li>🇪🇪 Eesti (Eesti)</li>
                    <li>🇫🇮 Soome (Suomi)</li>
                    <li>🇫🇷 Prantsuse (Français)</li>
                    <li>🇬🇷 Kreeka (Ελληνικά)</li>
                    <li>🇮🇱 Heebrea (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Horvaadi (Hrvatski)</li>
                    <li>🇭🇺 Ungari (Magyar)</li>
                    <li>🇮🇩 Indoneesia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Iiri (Gaeilge)</li>
                    <li>🇮🇸 Islandi (Íslenska)</li>
                    <li>🇮🇹 Itaalia (Italiano)</li>
                    <li>🇯🇵 Jaapani (日本語)</li>
                    <li>🇰🇭 Khmeeri (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korea (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Läti (Latviešu)</li>
                    <li>🇱🇹 Leedu (Lietuvių)</li>
                    <li>🇱🇺 Luksemburgi (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malai (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongoli (Монгол)</li>
                    <li>🇳🇵 Nepali (नेपाली)</li>
                    <li>🇳🇱 Hollandi (Nederlands)</li>
                    <li>🇳🇴 Norra (Norsk)</li>
                    <li>🇦🇫 Puštu (پښتو)</li>
                    <li>🇮🇷 Pärsia (فارسی)</li>
                    <li>🇵🇱 Poola (Polski)</li>
                    <li>🇵🇹 Portugali (Português)</li>
                    <li>🇮🇳 Pandžabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumeenia (Română)</li>
                    <li>🇷🇺 Vene (Русский)</li>
                    <li>🇸🇪 Rootsi (Svenska)</li>
                    <li>🇷🇸 Serbia (Српски)</li>
                    <li>🇸🇰 Slovaki (Slovenčina)</li>
                    <li>🇸🇮 Sloveeni (Slovenščina)</li>
                    <li>🇪🇸 Hispaania (Español)</li>
                    <li>🇹🇿 Suahiili (Kiswahili)</li>
                    <li>🇵🇭 Tagalogi (Filipino)</li>
                    <li>🇮🇳 Tamili (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Tai (ไทย)</li>
                    <li>🇨🇿 Tšehhi (Čeština)</li>
                    <li>🇹🇷 Türgi (Türkçe)</li>
                    <li>🇺🇦 Ukraina (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnami (Tiếng Việt)</li>
                    <li>🇸🇳 Volofi (Wolof)</li>
                    <li>🇺🇸 Jidiši (ייִדיש)</li>
                    <li>🇿🇦 Suulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Lisa oma keeled:</strong><br>
                Soovid keelt, mida veel ei ole? Aseta lihtsalt oma sõnaraamatu fail (<code>sprache_xx.py</code>) rakenduse kõrvale – tarkvara tunneb selle automaatselt ära. Kui oled huvitatud konkreetsest tõlkest, võta minuga julgelt ühendust.
            </div>

            <p><strong>🙏 Eriline tänu:</strong> DeepSeekile kõigi sõnaraamatute tõlkimise toetamise eest 62 keelde.</p>

            <p>📧 Kontakt tõlgete osas: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Viga",
        'error_occurred': "Ilmnes viga",
        'error_pdf_load': "Viga PDF-i laadimisel",
        'error_pdf_save': "Viga PDF-i salvestamisel",
        'error_ocr': "Viga tekstituvastusel",
        'error_no_pdf': "PDF-i pole laaditud",
        'error_page_not_found': "Lehekülge ei leitud",
        'error_invalid_range': "Vigane lehekülgede vahemik",
        'error_file_not_found': "Faili ei leitud",
        'error_permission': "Puuduvad õigused",
        'error_unknown': "Tundmatu viga",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Õnnestus",
        'success_operation': "Toiming õnnestus",
        'success_saved': "Edukalt salvestatud",
        'success_exported': "Edukalt eksporditud",
        'success_imported': "Edukalt imporditud",
        'success_deleted': "Edukalt kustutatud",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Kinnitus",
        'confirm_yes': "Jah",
        'confirm_no': "Ei",
        'confirm_ok': "OK",
        'confirm_cancel': "Tühista",
        'confirm_delete': "Kustuta",
        'confirm_overwrite': "Kirjuta üle",
        'confirm_continue': "Jätka",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Laadin PDF-i...",
        'progress_saving': "Salvestan PDF-i...",
        'progress_exporting': "Ekspordin PDF-i...",
        'progress_processing': "Töötlemine...",
        'progress_wait': "Palun oodake...",
        'progress_preparing': "Ettevalmistamine...",
        'progress_finalizing': "Lõpetamine...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Valge",
        'color_black': "Must",
        'color_red': "Punane",
        'color_green': "Roheline",
        'color_blue': "Sinine",
        'color_yellow': "Kollane",
        'color_magenta': "Magenta",
        'color_cyan': "Tsüaan",
        'color_orange': "Oranž",
        'color_gray': "Hall",
        'color_custom': "Värvi valik",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fail",
        'menu_edit': "&Redigeeri",
        'menu_view': "&Vaade",
        'menu_tools': "&Tööriistad",
        'menu_settings': "&Seaded",
        'menu_help': "&Abi",
        'menu_language': "🌐 Keel",
        'menu_guides': "&Juhendid",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Ava",
        'file_save_as': "&Salvesta kui...",
        'file_protect': "&Kaitse dokumenti...",
        'file_export': "&Ekspordi",
        'file_export_pages': "Ekspordi Pagesisse",
        'file_export_word': "Ekspordi DOCX-i",
        'file_export_text': "Ekspordi TXT-sse",
        'file_print_now': "&Prindi kohe",
        'file_print': "&Prindi",
        'file_close': "&Sulge",
        'file_quit': "&Välju",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Otsi",
        'edit_ocr': " Teosta OCR",
        'edit_rotate': "&Pööra lehekülge",
        'edit_rotate_all': "Pööra &kõiki lehekülgi",
        'edit_delete_pages': "&Kustuta leheküljed",
        'edit_extract_pages': "&Eralda leheküljed",
        'edit_insert_pages': "&Lisa leheküljed",
        'edit_move_pages': "&Teisalda leheküljed",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Lisa tekste ja riste",
        'text_insert': " Lisa tekst",
        'cross_insert': " Lisa rist",
        'text_customize': " Kohanda teksti",
        'cross_customize': " Kohanda seda risti",
        'cross_customize_all': " Kohanda kõiki riste",
        'text_discard': " Loobu sellest tekstist/ristist",
        'text_discard_all': " Loobu kõigist tekstidest ja ristidest",
        'text_save_all': " Salvesta kõik tekstid ja ristid",
        'text_guide': " Tekstisisestus / tekstiblokid – juhend",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Lisa allkiri",
        'signature_settings_menu': " Seaded...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Lisa pilt",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Lisa kujundeid",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Kuva tekstiaken",
        'view_zoom': "&Suum",
        'view_zoom_page': "&Lehe laius (vaikimisi)",
        'view_zoom_two': "&Kaks lehekülge",
        'view_zoom_overview': "&Ülevaade (mitu lehekülge)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Ligipääsetavus",
        'settings_voice': "Kõneväljund",
        'settings_voice_tooltip': "täiendab ekraanilugejate kõneväljundit lisateabega",
        'settings_signature': "&Allkirja seaded",
        'settings_password': "&Paroolihaldus",
        'settings_backup': "Loo varukoopia enne muudatusi",
        'settings_export_import': "&Ekspordi seaded / impordi seaded",
        'settings_export': "&Ekspordi kõik seaded...",
        'settings_import': "&Impordi kõik seaded...",
        'settings_export_info': "&Mida eksporditakse?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "sees",
        'voice_off': "väljas",
        'voice_toggle': "Kõneväljund {0}",
        'voice_speed': "Kiirus {0} protsenti",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Tööriista ei leitud:\n{0}\n\nBASE_DIR: {1}\nVeenduge, et PDF-i tööriistad on installitud kataloogi {1}.",
        'tool_started': "{0} käivitatud",
        'tool_start_failed': "Ei õnnestunud käivitada",
        'process_error_failed_to_start': "Protsessi ei õnnestunud käivitada. Kas fail on olemas?",
        'process_error_crashed': "Protsess jooksis käivitamise ajal kokku.",
        'process_error_timeout': "Protsessi ajalõpp saavutatud.",
        'process_error_write': "Kirjutamisviga protsessis.",
        'process_error_read': "Lugemisviga protsessis.",
        'process_error_unknown': "Tundmatu protsessiviga",
        'process_command': "Käsk",
        'process_normal_exit': "lõpetas normaalselt",
        'process_crashed': "jooksis kokku",
        'process_nonzero_exit': "{0} lõpetas veakoodiga {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Tühistamine...",
        'move_cancelling': "Teisaldamise tühistamine",
        'opening_pdf': "PDF-i avamine...",
        'loading_document': "Dokumendi laadimine...",
        'pdf_opened': "PDF avatud",
        'pages_found_moving': "Leiti {0} lehekülge, {1} teisaldamiseks",
        'creating_backup': "Varukoopia loomine...",
        'backup_description': "Algse faili varundamine...",
        'backup_saved_as': "Varukoopia salvestatud kui: {0}",
        'error_format': "Viga: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Otsing lähtestatud",
        'page_header_simple': "=== Lehekülg {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Paroolihaldus – Juhend",
        'password_guide_voice': "Juhend paroolihalduseks. Palun lugege märkusi.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Paroolihaldus – Üksikasjalik juhend</strong></p>

        <p><strong>1. PDF-ide paroolikaitse</strong></p>
        <ul>
        <li>Parooliga kaitstud PDF-i avamisel kuvatakse dialoog, kuhu saate parooli sisestada.</li>
        <li>Saate parooli krüpteeritult salvestada, et te ei peaks seda iga kord uuesti sisestama (märkeruut "Salvesta parool").</li>
        <li>Nupuga "Eemalda parool" saate luua dekrüpteeritud koopia PDF-ist ja kustutada parooli andmebaasist.</li>
        </ul>

        <p><strong>2. Peaparool</strong></p>
        <ul>
        <li>Peaparool kaitseb juurdepääsu kõigile salvestatud PDF-paroolidele.</li>
        <li><strong>Seadistamine:</strong> Minge "Seaded → Paroolihaldus → Peaparooli seaded" ja klõpsake "Sea peaparool". Valige tugev parool (vähemalt 8 tähemärki).</li>
        <li><strong>Muutmine:</strong> Pärast edukat autentimist saate peaparooli muuta.</li>
        <li><strong>Eemaldamine:</strong> Kui kustutate peaparooli, kustutatakse KÕIK salvestatud paroolid pöördumatult. Enne saate eksportida varukoopia.</li>
        <li>Üks kord sessiooni jooksul peate end peaparooliga autentima, et pääseda ligi kaitstud funktsioonidele (nt paroolide kuvamine).</li>
        </ul>

        <p><strong>3. Paroolihaldus (loend)</strong></p>
        <ul>
        <li>Jaotises "Seaded → Paroolihaldus" avaneb tabel kõigi salvestatud PDF-ide koos nende krüpteeritud paroolidega.</li>
        <li><strong>Ilma peaparoolita:</strong> Saate ainult kirjeid kustutada – paroolid jäävad peidetuks.</li>
        <li><strong>Peaparooliga (autenditud):</strong> Saate paroole kuvada, kopeerida, eksportida ja kustutada.</li>
        <li><strong>Eksport:</strong> Valige vorming (JSON, CSV, TXT) ja salvestage loend. Kui peaparool on määratud, saate valida, kas paroolid eksporditakse dekrüpteeritult või krüpteeritult.</li>
        <li><strong>Import:</strong> Varem eksporditud ZIP-faili (kõik seaded) saab uuesti importida jaotises "Seaded → Ekspordi seaded / impordi seaded". Hoiatus: olemasolevad andmed kirjutatakse üle!</li>
        </ul>

        <p><strong>4. Parooligeneraator</strong></p>
        <ul>
        <li>Parooli dialoogis (nt PDF-i kaitsmisel) on sisestusvälja paremal küljel täringunupp 🎲.</li>
        <li>Klõpsake seda, et avada parooligeneraator. Saate määrata pikkuse, märgikomplektid (suurtähed, väiketähed, numbrid, erimärgid) ja eraldaja parema loetavuse tagamiseks.</li>
        <li>Loodud parooli saab otse kasutada ja vajadusel kopeerida.</li>
        </ul>

        <p><strong>5. Olulised turvamärkused</strong></p>
        <ul>
        <li>Salvestatud paroolid säilitatakse AES-256 krüpteeritult. Võti tuletatakse teie peaparoolist (kui see on määratud) või fikseeritud väärtusest (ilma peaparoolita).</li>
        <li>Ilma peaparoolita on paroolid killl krüpteeritud, kuid võti on programmi sisse ehitatud – ründaja, kellel on juurdepääs teie failidele, võiks need dekrüpteerida. Seetõttu soovitame tungivalt kasutada peaparooli.</li>
        <li>Paroolide andmebaas asub failis `Data/passwords.json`. Tehke regulaarselt varukoopiaid, eriti enne peaparooli eemaldamist.</li>
        <li>Peaparooli kaotamisel on kõik salvestatud paroolid pöördumatult kadunud.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Inverteerimisrežiim",
        'invert_mode_classic': "Klassikaline (inverteeri kõik värvid)",
        'invert_mode_smart': "Nutikas (inverteeri ainult heledus)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Hallaskaala läviväärtus",
        'gray_threshold_10': "10% (range)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Vaikimisi)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (pehme)",
        'threshold_changed': "Läviväärtus seatud väärtusele {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Hallaskaala läviväärtus – Selgitus",
        'threshold_guide_text': "Hallaskaala läviväärtus määrab, milliseid piksleid nutikas tumedas režiimis käsitletakse 'hallidena' ja inverteeritakse.\n\n"
                                "• Madal väärtus (10%) inverteerib ainult peaaegu täiuslikke hallitoone – värvilised elemendid jäävad täielikult alles.\n"
                                "• Kõrge väärtus (50%) inverteerib ka kergelt värvilisi piksleid – see suurendab kontrasti, kuid võib värve moonutada.\n\n"
                                "Optimaalne väärtus sõltub dokumendist. Puhtalt tekstidokumentide jaoks on 30–40% sageli ideaalne, värvilise graafika jaoks pigem 10–20%.\n\n"
                                "Saate väärtust igal ajal menüü 'Seaded' kaudu kohandada – PDF laaditakse seejärel kohe uuesti.\n\n"
                                "Pange tähele:\n* Fotod ja pilte saab õigesti kuvada ainult heledas režiimis!\n* Inverteerimisseadeid kuvatakse ainult siis, kui tume režiim on aktiveeritud.",
        'threshold_guide_voice': "Hallaskaala läviväärtus määrab, kui tugevalt nutikas tume režiim sekkub. Madal väärtus säästab värve, kõrge väärtus suurendab kontrasti.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF-i avamine...",
        'progress_loading_document': "Dokumendi laadimine...",
        'progress_pdf_opened': "PDF avatud",
        'progress_creating_backup': "Varukoopia loomine...",
        'progress_backup_description': "Algse faili turvamine...",
        'progress_backup_created': "Varukoopia loodud",
        'progress_backup_saved_as': "Salvestatud kui: {0}",
        'progress_analyzing_start': "Analüüsi alustamine...",
        'progress_searching_empty': "Tühjade lehtede otsimine...",
        'progress_page_empty': "Leht {0} on tühi",
        'progress_page_keep': "Hoia leht {0} alles",
        'progress_analysis_complete': "Analüüs lõpetatud",
        'progress_empty_found': "Leitud {0} tühja lehte",
        'progress_current_page': "Praegune leht",
        'progress_mark_delete': "Märgistatakse kustutamiseks",
        'progress_range_selected': "Lehtede vahemik {0}-{1}",
        'progress_deleting_pages': "Kustutan {0} lehte",
        'progress_creating_new_pdf': "Uue PDF-i loomine...",
        'progress_transferring_pages': "Lehtede ülekandmine",
        'progress_keeping_page': "Leht {0} hoitakse alles ({1}/{2})",
        'progress_saving_pdf': "PDF-i salvestamine...",
        'progress_optimizing': "Faili suuruse optimeerimine...",
        'progress_finalizing': "Lõpetamine...",
        'progress_new_size': "Uus suurus: {0:.2f} MB",
        'progress_cancelling': "Tühistamine...",
        'progress_cancel_message': "{0} tühistatakse",
        'progress_pages_found_moving': "Leitud {0} lehte, {1} teisaldamiseks",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF-i analüüsimine...",
        'ocr_status_optimizing': "Pildi optimeerimine käib...",
        'ocr_status_recognizing': "Tekstituvastus töös...",
        'ocr_status_embedding': "Teksti manustamine...",
        'ocr_status_finalizing': "PDF-i lõpetamine...",

        # PDF-Laden
        'progress_preparing': "Ettevalmistus...",
        'progress_loading': "PDF-i laadimine...",

        # Seitenoperationen
        'progress_deleting_title': "Lehtede kustutamine...",
        'progress_moving_title': "Lehtede teisaldamine...",
        'pages_found': "Leitud lehed",
        'progress_creating_new_order': "Uue järjekorra loomine...",
        'progress_sorting_pages': "Lehtede sorteerimine...",
        'progress_moving_to_begin': "Teisalda {0} lehte algusesse",
        'progress_transferring_count': "Kannan üle {0} lehte",
        'progress_transferring_before_target': "Kannan lehed üle enne sihtmärki",
        'progress_moving_pages': "Teisalda {0} lehte",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_varukoopia_",
        'filename_protected_suffix': "_kaitstud_",
        'filename_copy_suffix': "_Koopia",
        'filename_page_single': "_Leht_",
        'filename_page_range': "_Lehed_",
        'filename_export_page': "_Leht_{0:03}",
        'filename_export_range': "_Lehed_{0}-{1}",
        'filename_export_multiple': "_Lehed_{0}",
        'filename_with_text': "_tekstiga",
        'filename_with_signature': "_allkirjaga",
        'filename_with_image': "_pildiga",
        'filename_with_forms': "_kujunditega",
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
        'view_toggle_navbar': "Nupuriba kuvamine",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Kõiki lehekülgi ei saa kustutada",
		'pages_cannot_delete_last_page': 'Viimast lehekülge ei saa kustutada!',
		'pages_cannot_delete_all_pages': 'Dokumenti peab jääma vähemalt üks lehekülg!',
		'delete_pages_confirm': 'Kas olete kindel, et soovite kustutada {0} lehekülge?',
		'delete_pages_confirm_voice': 'Kas olete kindel, et soovite kustutada {0} lehekülge?',
		'pages_deleted': '{0} lehekülge edukalt kustutatud.',
		'warning': 'Hoiatus',
		'error': 'Viga',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Vorm pole valitud",
        'form_customized': "Vorm kohandatud",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Vali",
        'btn_use': "Kasuta",
        'master_password_for_spasswords': "Paroolide salvestamiseks ja kasutamiseks tuleb kõigepealt seadistada peaparool.\n\nKas soovite peaparooli nüüd seadistada?",
        'open_saved_dialog_title': "Ava salvestatud fail",
        'open_saved_question': "Kas soovite salvestatud faili nüüd avada?",
        'password': "Parool",
        'password_manager_master_required': "Paroolihaldur on saadaval ainult siis, kui peaparool on seadistatud.\n\nKas soovite peaparooli nüüd seadistada?",
        'password_master_required_for_select': "Salvestatud paroolide kuvamiseks ja valimiseks peate esmalt autentima oma peaparooliga.\n\nKas soovite nüüd autentida?",
        'password_not_available': "Valitud parool pole saadaval või seda ei õnnestunud dekrüpteerida.",
        'password_options_title': "Parooli valikud",
        'password_save_choice_change': "Määra uus parool",
        'password_save_choice_keep': "Kasuta olemasolevat parooli",
        'password_save_choice_none': "Salvesta krüptimata",
        'password_save_hint': "Paroolide turvaliseks salvestamiseks seadistage esmalt peaparool.",
        'password_save_master_required': "Salvesta parool (võimalik ainult peaparooliga)",
        'password_save_question': "Praegune PDF on parooliga kaitstud. Kas soovite kasutada olemasolevat parooli, määrata uue või salvestada krüptimata?",
        'password_select': "Vali parool",
        'password_select_none': "Ühtegi parooli pole valitud.\n\nPalun valige loendist parool.",
        'password_select_one': "Palun valige täpselt üks parool.\n\nOlete märkinud mitu parooli.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_varukoopia",
        'filename_insert_suffix': "_sisestusega",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_lehed_kustutatud",
        'filename_pages_moved': "_lehed_teisaldatud",
        'filename_rotated_all_suffix': "_kõik_lehed_pööratud",
        'filename_rotated_suffix': "_leht_pööratud",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Failinimede konfigureerimine PDF-i muutmisel",
        'filename_keep_suffixes': "Säilita eelmised laiendid (nt _tekstiga)",
        'filename_keep_suffixes_false': "Asenda",
        'filename_keep_suffixes_true': "Säilita",
        'filename_preview_label': "Failinime eelvaade:",
        'filename_preview_overwrite_hint': "Eelvaade pole saadaval – originaal kirjutatakse üle.",
        'filename_separator': "Sõnade eraldaja",
        'filename_separator_none': "Eraldaja puudub",
        'filename_separator_space': "Tühik ( )",
        'filename_separator_underscore': "Alakriips (_)",
        'filename_settings_saved': "Failinime seaded salvestatud",
        'filename_settings_title': "Failinime vormindus ja varukoopia",
        'filename_timestamp_position': "Ajatempli asukoht",
        'filename_timestamp_position_after': "Pärast põhinime",
        'filename_timestamp_position_before': "Kõige ees",
        'filename_timestamp_position_end': "Lõpus",
        'filename_use_timestamp': "Kasuta ajatemplit",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Käitumine muudatuste korral:</b><ul><li>Lehtede kustutamine ja sisestamine</li><li>Teksti, allkirja, pildi ja kujundite sisestamine</li><li>OCR</li></ul></html>",
        'backup_section': "Varukoopia leheoperatsioonide jaoks (Kustutamine, Teisaldamine)",
        'behavior_info': "Märkus: 'Algse ülekirjutamise' korral eiratakse ajatempleid ja järelliiteid – fail säilitab oma nime.",
        'behavior_new_file': "Loo alati uus fail (ajatempli ja järelliitega)",
        'behavior_overwrite': "Kirjuta algne üle (uus fail puudub)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Kõik lehed pöörati.\n\nOriginaal jäi muutmata.\nUus fail: {0}",
        'all_pages_rotated_voice': "Kõik lehed pööratud, loodud uus fail.",
        'empty_pages_deleted_new_file': "{0} tühja lehte kustutati.\n\nOriginaal jäi muutmata.\nUus fail: {1}",
        'empty_pages_deleted_voice': "{0} tühja lehte kustutati, loodud uus fail.",
        'ocr_keep_original': "Säilita originaal (ava hiljem käsitsi)",
        'ocr_new_file_question': "Uus otsitav PDF salvestati asukohta:\n{0}\n\nKas soovite selle nüüd avada?",
        'ocr_open_new': "Ava uus OCR-fail",
        'ocr_original_kept': "Algne fail jääb avatuks. OCR-fail on salvestatud.",
        'page_deleted_new_file': "Leht {0} kustutati.\n\nOriginaal jäi muutmata.\nUus fail: {1}",
        'page_deleted_voice': "Leht {0} kustutati, loodud uus fail.",
        'page_rotated_new_file': "Leht {0} pöörati.\n\nOriginaal jäi muutmata.\nUus fail: {1}",
        'page_rotated_voice': "Leht {0} pöörati, loodud uus fail.",
        'pages_deleted_new_file': "Kustutati {0} lehte.\n\nAlgne fail jäi muutmata.\nUus fail: {1}",
        'pages_deleted_new_file_voice': "{0} lehte kustutati, loodud uus fail.",
        'pages_inserted_new_file': "Sisestati {0} lehte.\n\nAlgne fail jäi muutmata.\nUus fail: {1}",
        'pages_inserted_new_file_ask': "Sisestati {0} lehte.\n\nOriginaal jäi muutmata.\nUus fail: {1}\n\nKas soovite selle nüüd avada?",
        'pages_inserted_voice_new': "{0} lehte sisestati, loodud uus fail.",
        'pages_moved_new_file': "Teisaldati {0} lehte.\n\nAlgne fail jäi muutmata.\nUus fail: {1}",
        'pages_moved_new_file_voice': "{0} lehte teisaldati, loodud uus fail.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ära näita enam",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Varukoopia seaded</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Varukoopia SISSE LÜLITATUD</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Kõigi muudatuste puhul, mis kirjutavad originaali üle</strong> (tekst, allkiri, pilt, kujund, OCR, pööramine, sisestamine, lehtede kustutamine/teisaldamine) luuakse <strong>automaatselt ajatempliga varukoopia</strong> enne muudatuse rakendamist.</p>
                <p style="margin: 5px 0 5px 20px;">• Varukoopia asub algse faili kõrval (nt <code>Dokument_varukoopia_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Kui olete lisaks aktiveerinud valiku <strong>„Kirjuta algne üle“</strong>, luuakse samuti varukoopia.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Varukoopia VÄLJA LÜLITATUD</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Varukoopiat ei looda</strong> – ei ülekirjutamisel ega leheoperatsioonide korral.</p>
                <p style="margin: 5px 0 5px 20px;">• Algne fail võib ülekirjutamisel pöördumatult kaduma minna.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Soovitatav ainult kogenud kasutajatele!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Vihje:</strong> Varukoopia seaded on sõltumatud valikust „Kirjuta algne üle“. Saate mõlemat kombineerida.<br>
                Selle teate saate jäädavalt peita.
            </div>
        </div>
        """,
        'backup_info_title': "Varukoopia käitumine",
        'backup_info_voice': "Teade varukoopia käitumise kohta leheoperatsioonidel. Varukoopia sees kirjutab originaali üle, varukoopia väljas loob uue faili.",
        'show_backup_info': "Teave varukoopia seadete kohta",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ära näita enam",
        'overwrite_enable_backup': "Lülita varukoopia sisse (soovitatav)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Kirjuta algne üle</p>
            <p>Kui aktiveerite selle valiku, salvestatakse muudatused (tekst, allkiri, pilt, kujund, OCR, pööramine, sisestamine) <strong>otse originaali</strong> – <strong>uus faili ei looda</strong>.</p>
            <p>• Failinimi jääb muutumatuks.<br>
            • Ajatemplid ja järelliited eiratakse.<br>
            • <strong>Ilma varukoopiata võib originaal pöördumatult kaduma minna.</strong></p>
            <p style="color: #FFD700;">Soovitus: Automaatsete varukoopiate saamiseks lülitage lisaks sisse varukoopia valik.</p>
        </div>
        """,
        'overwrite_info_title': "Kirjuta algne üle",
        'overwrite_info_voice': "Hoiatus: Kirjuta algne üle – uut faili ei looda. Varukoopia on soovitatav.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Sisestati {0} lehte.\n\nAlgne fail kirjutati üle.\nLoodi varukoopia.",
        'pages_inserted_overwrite_no_backup': "Sisestati {0} lehte.\n\nAlgne fail kirjutati üle.\nEI loodud varukoopiat.",
        'texts_saved_overwrite_with_backup': "Muudatused salvestati originaalis.\n\nLoodi varukoopia.",
        'texts_saved_overwrite_no_backup': "Muudatused salvestati originaalis.\n\nEI loodud varukoopiat.",
        'texts_crosses_saved_new_file': "{0} {1} ja {2} {3} sisestati.\n\nAlgne fail jäi muutmata.\nLoodi uus fail.\n\nUus PDF laaditakse...",
        'texts_saved_new_file': "{0} {1} sisestati.\n\nAlgne fail jäi muutmata.\nLoodi uus fail.\n\nUus PDF laaditakse...",
        'crosses_saved_new_file': "{0} {1} sisestati.\n\nAlgne fail jäi muutmata.\nLoodi uus fail.\n\nUus PDF laaditakse...",
        'elements_saved_new_file': "{0} elementi sisestati.\n\nAlgne fail jäi muutmata.\nLoodi uus fail.\n\nUus PDF laaditakse...",
        'signatures_saved_overwrite_with_backup': "Allkiri/ad salvestati originaalis.\n\nLoodi varukoopia.",
        'signatures_saved_overwrite_no_backup': "Allkiri/ad salvestati originaalis.\n\nEI loodud varukoopiat.",
        'images_saved_overwrite_with_backup': "Pilt/Id salvestati originaalis.\n\nLoodi varukoopia.",
        'images_saved_overwrite_no_backup': "Pilt/Id salvestati originaalis.\n\nEI loodud varukoopiat.",
        'forms_saved_overwrite_with_backup': "Kujund/Id salvestati originaalis.\n\nLoodi varukoopia.",
        'forms_saved_overwrite_no_backup': "Kujund/Id salvestati originaalis.\n\nEI loodud varukoopiat.",
        'signatures_saved_new_file': "{0} allkirja sisestati.\n\nAlgne fail jäi muutmata.\nLoodi uus fail.\n\nUus PDF laaditakse...",
        'images_saved_new_file': "{0} pilti sisestati.\n\nAlgne fail jäi muutmata.\nLoodi uus fail.\n\nUus PDF laaditakse...",
        'forms_saved_new_file': "{0} kujundit sisestati.\n\nAlgne fail jäi muutmata.\nLoodi uus fail.\n\nUus PDF laaditakse...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Hoiatus: See PDF sisaldab pööratud lehti. Paigutus võib erineda.",
        'page_rotated_warning_title': "Tuvastati pööratud leht",
        'page_rotated_warning_message': "Praegune leht {0} on pööratud {1}°.\n\nElementide sisestamine pööratud lehtedele ei ole toetatud.\n\nKas soovite lehe nüüd püstasendisse pöörata?",
        'page_rotated_warning_voice': "Hoiatus: Leht on pööratud. Palun pöörake see kõigepealt.",
        'paste_on_rotated_page_simple_warning': "Sisestamine lehele {0} pole võimalik!\n\nSee leht on pööratud {1}°.\n\nPalun pöörake leht kõigepealt 0°-le (Menüü: Redigeeri → Joonda leht).\n\nHoiatus:\nVarem kopeeritud element läheb kaotsi, kui te ei salvesta enne lehe pööramist.",
        'paste_on_rotated_page_voice': "Sisestamine katkestati. Leht on pööratud. Palun joondage leht kõigepealt.",
        'page_rotated_cancel': "Loobu",
        'page_rotated_rotate_until_upright': "Pööra lehte korduvalt (kuni püstine)",
        'page_rotated_now_upright': "Leht on nüüd püstine. Nüüd saate sisestada.",
        'page_rotated_still_not_upright': "Lehte ei õnnestunud püstasendisse pöörata. Palun parandage käsitsi.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Abi: Pööratud lehtede parandamine",
        'help_rotated_pages_voice': "Aken pööratud lehtede parandamise abiga avaneb.",
        'btn_help': "Abi",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Probleem: Pööratud leht – Sisestamine ei tööta korralikult</p>

            <p>Kui tekstide, allkirjade või kujundite sisestamine pööratud lehel ei tööta korralikult, saate lehte parandada välise PDF-redaktoriga.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Lahendus välise tööriistaga (nt macOS eelvaade)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Ekspordi leht</strong><br>
                &nbsp;&nbsp;Klikkige menüüs <strong>Fail → Ekspordi lehtedena</strong> või kasutage mõnda muud meetodit soovitud lehe ühe PDF-failina salvestamiseks.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Ava leht välises programmis</strong><br>
                &nbsp;&nbsp;Avage eksporditud PDF PDF-redaktoris (nt <strong>macOS eelvaade</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Pööra lehte</strong><br>
                &nbsp;&nbsp;Pöörake lehte nii, et see oleks püstine (eelvaates: <strong>Tööriistad → Pööra</strong> või <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Salvesta</strong><br>
                &nbsp;&nbsp;Salvestage parandatud leht (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Sisesta leht uuesti algdokumenti</strong><br>
                &nbsp;&nbsp;Naaske PDFDarkView'i ja sisestage parandatud leht soovitud asukohta:<br>
                &nbsp;&nbsp;<strong>Redigeeri → Sisesta lehti</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatiiv: Pööra lehte originaalis</p>
                <p style="margin: 5px 0 5px 20px;">• Kasutage sisseehitatud pööramisfunktsiooni (<strong>Redigeeri → Pööra lehte</strong>) lehe samm-sammuliseks parandamiseks.<br>
                • Pärast iga pööramist saate kontrollida, kas sisestamine nüüd töötab.<br>
                • See on sageli kiirem lahendus – proovige seda kõigepealt!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Vihje:</strong> Kui puutute sageli kokku pööratud lehtedega, saate sisestusdialoogi hoiatusjäädavalt peita.<br>
                Paigutus võib siis erineda – kasutage seda valikut ainult siis, kui teate tagajärgi.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Joonda lehed",
        'menu_rotate_normalize_tooltip': "Pööra lehte või lähtesta 0°-le",
        'normalize_current_page': "Viige praegune leht püstasendisse (määrake 0°-le)",
        'normalize_all_pages': "Viige kõik lehed püstasendisse (määrake 0°-le)",
        'page_normalized': "Leht {0} viidi püstasendisse.",
        'all_pages_normalized': "Kõik lehed viidi püstasendisse.",
        'page_already_upright': "Leht {0} on juba püstine.",
        'all_pages_already_upright': "Kõik lehed on juba püstised.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF ei sisalda otsitavat teksti.</p><p>Kas soovite eksportimiseks {0} teha OCR-i?</p>",
        'export_ocr_voice': "PDF ei sisalda teksti. Eksportimiseks {0} on vaja OCR-i.",
        'export_no_ocr_possible': "Eksport ilma OCR-ita pole võimalik. Palun tehke OCR menüü kaudu.",
        'ocr_failed_export_not_possible': "OCR ebaõnnestus. Eksporti ei saa teostada.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF avaneb eelvaates. Palun käivitage seal printimisprotsess.",
        'print_preview_manual': "PDF on avatud. Palun käivitage printimiskäsk käsitsi (nt Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDF-ide ühendamine",
        'merge_pdfs': "Ühenda PDF-id",
        'merge_progress_title': "PDF-ide ühendamine...",
        'merge_pdfs_list': "PDF-id järjekorras (Lohistage sorteerimiseks)",
        'merge_add_pdf': "Lisa PDF",
        'merge_remove': "Eemalda",
        'merge_move_up': "Üles",
        'merge_move_down': "Alla",
        'merge_pdfs_info': "💡 Vihje: Järjekorda saate muuta lohistamisega",
        'merge_no_pdfs': "Ühtegi PDF-i pole valitud. Klõpsake nuppu 'Lisa PDF'.",
        'merge_info': "Valitud {0} PDF-i (umbes {1} lehte)",
        'merge_open_file': "Ava fail",
        'merge_merge': "Ühenda",
        'merge_error': "Viga ühendamisel",
        'merge_min_two_pdfs_error': "Palun valige ühendamiseks vähemalt kaks PDF-faili.",
        'merge_select_pdfs': "Valige ühendamiseks PDF-id",
        'merge_error_file': "Viga töötlemisel",
        'merge_cancelled': "Ühendamine tühistati",
        'merge_preparing': "Ettevalmistus...",
        'merge_processing': "Töötlen PDF-i {0} / {1}",
        'merge_saving': "Ühendatud PDF-i salvestamine...",
        'merge_complete': "Valmis!",
        'merge_success_title': "Ühendamine õnnestus",
        'merge_success_voice': "{0} PDF-i ühendati edukalt.",
        'merge_success_message': "{0} PDF-i ühendati edukalt.\n\nUues dokumendis on nüüd {1} lehte.\n\nUus fail:\n{2}\n\nSalvestuskoht:\n{3}\n{2}\n\nKas soovite selle PDF-i avada?",
        'replace_file_title': "Kas asendada fail?",
        'replace_file_message': "PDF on juba avatud. Kas soovite selle asendada uue failiga?",
        'btn_yes': "Jah",
        'btn_no': "Ei",
        'filename_merge_suffix': "uhendatud",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Avan {0}...",
        'progress_merge_reading': "Loen {0}...",
        'progress_merge_adding': "Lisan {0} lehte...",
        'progress_merge_optimizing': "Optimeerin PDF-i...",
        'progress_merge_writing': "Kirjutan PDF-i...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF-i sulgemist",
        'action_close_window': "akna sulgemist",
        'action_open_new_pdf': "uue PDF-i avamist",
        'action_quit_app': "rakendusest väljumist",
        'changes_saved': "Muudatused salvestati.",
        'file_close_title': "Sulge PDF-fail",
        'save_before_action': "Kas muudatused tuleks salvestada enne {0}? Jah või Ei?",
        'save_before_action_voice': "Kas muudatused tuleks salvestada enne {0}? Jah või Ei?",
        'save_before_close_question': "Kas muudatused tuleks salvestada enne sulgemist? Jah või Ei?",

         # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Loodud otsitav PDF:\n\n{0}\n\n<b>proovi vajadusel uuesti",
        "ocr_rotate_title": "Joonda lehed enne OCR-i",
        "ocr_rotate_question": "PDF sisaldab pööratud lehti.\nKas soovite kõik lehed enne OCR-i joondada 0°?\nSee parandab tekstituvastust märkimisväärselt.",
        "ocr_rotate_yes": "Jah, joonda",
        "ocr_rotate_no": "Ei, käivita OCR otse",
        "ocr_rotate_voice": "PDF sisaldab pööratud lehti. Kas kõik lehed tuleks enne OCR-i joondada?",
        "ocr_not_performed_message": "Teksti ei ole. Palun tehke OCR (menüü \"Muuda\" → \"Teosta OCR\" või klahv Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-i seaded",
        "ocr_language_btn": "Vali OCR-i keel",
        "ocr_language": "OCR-i keel(ed)",
        "ocr_language_current": "Praegune keel:",
        "ocr_param_info": "Teave parameetri kohta",

        "ocr_force_ocr_label": "Sunni OCR",
        "ocr_deskew_label": "Paranda kallet",
        "ocr_clean_label": "Puhasta pilt",
        "ocr_oversample_label": "Eraldusvõime (DPI)",
        "ocr_pagesegmode_label": "Lehe jaotus",
        "ocr_oem_label": "OCR-mootori režiim",
        "ocr_optimize_label": "PDF-i kompressioon",
        "ocr_jobs_label": "Paralleelsed protsessid",
        "ocr_verbose_label": "Logi detailsus",

        "ocr_force_ocr_tooltip": "Sunni OCR igal lehel, isegi kui tekst on juba olemas",
        "ocr_deskew_tooltip": "Joonda automaatselt viltused skaneeringud",
        "ocr_clean_tooltip": "Eemalda pildilt müra ja artefaktid",
        "ocr_oversample_tooltip": "Suurenda pilt enne OCR-i sellele DPI-le",
        "ocr_pagesegmode_tooltip": "Määrab, kuidas leht jagatakse tekstialadeks",
        "ocr_oem_tooltip": "Valib Tesseracti OCR-mootori",
        "ocr_optimize_tooltip": "Väljund PDF-i kompressiooni tase",
        "ocr_jobs_tooltip": "Paralleelsete OCR-protsesside arv",
        "ocr_verbose_tooltip": "Logi väljundi detailsuse tase",
        "ocr_settings_explain_btn": "Selgitus",

        "ocr_force_ocr_explain": "Sunni tekstituvastus <b>igal</b> lehel, isegi kui see sisaldab juba teksti.\n\nSoovitus: <b>Sisse</b> skaneeritud PDF-ide jaoks, <b>Välja</b> juba olemasoleva tekstiga algsete PDF-ide jaoks.",

        "ocr_deskew_explain": "Parandab kergelt viltuseid skaneeringuid (kuni umbes 5°).\n\nSoovitus: <b>Sisse</b> skaneeritud dokumentide jaoks, <b>Välja</b> kui lehed on juba täiesti sirged.",

        "ocr_clean_explain": "Eemaldab pildilt müra, täpid ja väikesed artefaktid.\n<b>TÄHTIS:</b> Araabia, tai või vietnami tekstide puhul, mis sisaldavad diakriitilisi märke (täpid tähtede kohal/all), tuleks see valik <b>keelata</b>, vastasel juhul võivad olulised märgid kaduda.",

        "ocr_oversample_explain": "Suurendab pilti <b>enne</b> tekstituvastust määratud DPI-le.<br><br>• <b>72-150 DPI:</b> Väga kiire, kuid madal tuvastamise määr<br>• <b>200-300 DPI:</b> Optimaalne vahemik (Vaikimisi: 300)<br>• <b>400+ DPI:</b> Peaaegu ei paranda tuvastamist, kuid oluliselt suuremad failid<br><br>Soovitus: 300 DPI keeruliste kirjade jaoks (araabia, hiina, jaapani), 200 DPI lääne keelte jaoks.",

        "ocr_pagesegmode_explain": "Määrab, kuidas Tesseract jagab lehe tekstialadeks.\n\n• <b>3 - Automaatne (Vaikimisi):</b> Hea segapaigutuste jaoks\n• <b>4 - Üksik veerg:</b> Üheveeruliste tekstide jaoks\n• <b>5 - Vertikaalne plokk:</b> Vertikaalsete kirjade jaoks (jaapani, hiina)\n• <b>6 - Ühtne tekstiplokk:</b> Optimaalne ilma veergudeta voolava teksti jaoks\n• <b>11 - Toorpilt:</b> Kehva skaneeringute / käekirja jaoks\n\nSoovitus: <b>6</b> lihtsate tekstidokumentide jaoks, <b>3</b> keeruliste paigutuste jaoks.",

        "ocr_oem_explain": "Valib Tesseracti OCR-mootori.\n\n• <b>0 - Legacy:</b> Vana mootor (kiire, kuid vähem täpne)\n• <b>1 - LSTM:</b> Närvimootor (aeglasem, kuid täpsem)\n• <b>2 - Legacy + LSTM:</b> Kombineerib mõlemad tulemused\n• <b>3 - Vaikimisi (LSTM eelistatud):</b> Parim valik enamikul juhtudel\n\nSoovitus: <b>3</b> maksimaalse tuvastuse täpsuse jaoks.",

        "ocr_optimize_explain": "Komprimeerib väljund PDF-i.\n\n• <b>0:</b> Optimeerimine puudub (kiireim töötlus)\n• <b>1:</b> Kerge optimeerimine (hea kompromiss)\n• <b>2:</b> Mõõdukas optimeerimine\n• <b>3:</b> Tugev optimeerimine (väikseim fail, kuid aeglasem)\n\nSoovitus: <b>1</b> igapäevaseks kasutamiseks.",

        "ocr_jobs_explain": "Paralleelsete protsesside arv OCR-ile.\n\n• <b>1:</b> Aeglane, kuid madalaim mälukasutus\n• <b>4-8:</b> Optimaalne kaasaegsete mitmetuumaliste protsessorite jaoks\n• <b>12+:</b> Peaaegu mitte kiirem töötlus kõrge mälukasutuse juures\n\nSoovitus: Protsessori tuumade arv (nt <b>4</b> 4-tuumalistes süsteemides).",

        "ocr_verbose_explain": "Logi väljundi detailsuse tase konsoolis.\n\n• <b>0:</b> Väljund puudub\n• <b>1:</b> Edenemine ja olekuteated\n• <b>2:</b> Üksikasjalik väljund\n• <b>3:</b> Täielik silumisväljund (väga mahukas)\n\nSoovitus: <b>1</b> tavaliseks tööks.",

        "ocr_reset_title": "Seaded on lähtestatud",
        "ocr_reset_message": "Kõik OCR-seaded on lähtestatud vaikeväärtustele.",
        "info_tooltip": "Rohkem teavet selle parameetri kohta",
        "ocr_reset_defaults": "Lähtesta vaikeväärtustele",

        "ocr_psm_0": "Automaatne (Legacy mootor)",
        "ocr_psm_1": "Automaatne veergude tuvastus",
        "ocr_psm_3": "Automaatne (Vaikimisi)",
        "ocr_psm_4": "Üksik veerg",
        "ocr_psm_5": "Vertikaalne plokk",
        "ocr_psm_6": "Ühtne tekstiplokk",
        "ocr_psm_7": "Üksik tekstirida",
        "ocr_psm_8": "Üksik sõna",
        "ocr_psm_11": "Toorpilt (ilma paigutuse analüüsita)",

        "ocr_oem_0": "Legacy mootor (kiire)",
        "ocr_oem_1": "LSTM mootor (närvi, täpne)",
        "ocr_oem_2": "Legacy + LSTM kombineeritud",
        "ocr_oem_3": "Vaikimisi (LSTM eelistatud)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-i keel(ed)...",
        "ocr_language_title": "Vali OCR-i keel(ed)",
        "ocr_language_instruction": "Valige tekstituvastuse (OCR) keel(ed).\nTähelepanu: Mitu keelt käivad jõudluse ja täpsuse arvelt!\nParimad tulemused saavutate, kui valite ainult ühe keele.",
        "ocr_language_predefined": "Eelmääratletud kombinatsioonid",
        "ocr_language_custom": "Kohandatud...",
        "ocr_language_selected": "Valitud OCR-i keeled",
        "ocr_language_changed": "OCR-i keel muudetud keeleks {0}",
        "ocr_language_auto_detect": "Saadaolevad keeled tuvastatakse automaatselt.",
        "ocr_language_none_found": "Tesseracti keeleandmeid ei leitud! Palun installige keelepaketid (nt 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Kohandatud keelevalik",
        "ocr_language_available": "Saadaolevad keeled (installitud):",
        "ocr_language_select_hint": "Valige üks või mitu keelt:",
        "ocr_language_confirm": "Rakenda",
        "ocr_language_reset": "Lähtesta vaikeväärtusele (deu+eng+vie)",
        "ocr_language_priorities": "Soovitatud keeled (eelinstallitud):",

        "select_all_languages": "Vali kõik",
        "clear_all_languages": "Tühista valik",
        "install_language_packs": "Installige puuduvad keelepaketid...",
        "install_hint": "💡 Näpunäide: Kõik keeled pole teie süsteemi installitud. Selle nupu kaudu saate installimiseks abi.",
        "ocr_language_install_title": "Tesseracti keelepakettide installimine",

        "ocr_missing_languages": "Puuduvad OCR-i keelepaketid",
        "ocr_missing_languages_message": "Järgmised valitud keeled pole teie süsteemi installitud:\n\n{0}\n\nPalun installige puuduvad keelepaketid (vt abi jaotises 'Installimisabi').\n\nKas soovite installimisabi kohe avada?",
        "ocr_missing_languages_voice": "Puuduvad keelepaketid. Palun installige puuduvad keeled.",
        "ocr_install_help_now": "Ava abi",
        "ocr_continue_anyway": "Proovi siiski",
        "ocr_language_error_title": "OCR-i keele viga",
        "ocr_language_error_message": "Viga tekstituvastusel: {0}\n\nPalun kontrollige oma OCR-i keeleseadeid (Seaded → OCR-i keel).",
        "ocr_install_help_button": "Installimisabi",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseracti keelepakettide installimine</p>

        <p>OCR-i toimimiseks konkreetses keeles peavad vastavad keeleandmed olema teie süsteemi installitud. Järgige oma operatsioonisüsteemi juhiseid:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Avage <strong>Terminal</strong> (Finder → Programmid → Utiliidid → Terminal).</li>
        <li>Installige kõik saadaolevad keeled käsuga:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (See võib võtta mõne minuti.)</li>
        <li>Või ainult üksikud keeled (nt vietnami keel):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Praeguste Homebrew versioonide puhul võib <code>*.traineddata</code> vaja minna käsitsi alla laadida (vt allpool).</li>
        <li>Pärast installimist: Sulgege see dialoog ja avage uuesti OCR-i keelevalik – uued keeled ilmuvad automaatselt.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Avage terminal (Ctrl+Alt+T).</li>
        <li>Installige soovitud keel, nt vietnami keele jaoks:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Olulised keelekoodid: <code>deu</code> (saksa), <code>eng</code> (inglise), <code>vie</code> (vietnami), <code>spa</code> (hispaania), <code>fra</code> (prantsuse), <code>ita</code> (itaalia), <code>nld</code> (hollandi), <code>fin</code> (soome), <code>swe</code> (rootsi), <code>nor</code> (norra).</li>
        <li>Kuva kõik saadaolevad paketid:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (käsitsi)</p>
        <ol>
        <li>Laadige soovitud <code>*.traineddata</code> failid alla saidilt:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (nt <code>vie.traineddata</code> vietnami keele jaoks).</li>
        <li>Kopeerige failid Tesseracti keelekausta, tavaliselt:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Kohandage vastavalt individuaalsele installatsioonile.)</li>
        <li>Käivitage rakendus uuesti (või avage uuesti OCR-i keelevalik).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatiiv kõikidele süsteemidele</p>
        <ul>
        <li>Installige <strong>OCRmyPDF</strong> ja <strong>Tesseract</strong> oma valitud paketihalduriga. Enamik installatsioone sisaldab juba mõningaid standardkeeli (inglise, saksa, prantsuse).</li>
        <li>Puuduvaid keeli saab installida igal ajal – OCR-i keelevalik kuvab ainult tegelikult olemasolevad keeled.</li>
        </ul>

        <hr>
        <p><b>✅ Pärast installimist:</b> Rakenduse taaskäivitamine pole vajalik – äsja lisatud keeled ilmuvad loendisse kohe.</p>
        <p><b>📖 Abi keelekoodidega:</b> Täieliku loendi leiate <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseracti dokumentatsioonist</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans fondid",
        "info_noto_font_voice": "Noto Sans fontide installimise juhend",
        "btn_info_noto_font_install": "Fondi info",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Kuidas installida Google'i tasuta Noto fonde</h2>

        <p><strong>Noto fondid</strong> on Google'i avatud lähtekoodiga fontide perekond. Nende eesmärk on mitte näha <em>"ühtegi tofut"</em> (st tühje kaste □) ja kuvada korrektselt iga Unicode'i standardi märki. Need on ideaalne täiendus rakendustele, mis peavad kuvama tekste paljudes erinevates keeltes.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installimine macOS-is</h3>

        <p><strong>Meetod 1: Homebrew'ga (edasijõudnutele)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Meetod 2: "Font Book" kaudu (Soovitatav)</strong></p>

        <ol>
        <li>Laadige alla ametlik fondipakett:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pakkige ZIP-fail lahti</li>
        <li>Kopeerige failid asukohta <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installimine Windowsis (10 & 11)</h3>

        <p><strong>Meetod 1: Microsoft Store (Soovitatav)</strong><br>
        Otsige "Google Noto Fonts" või "Noto Sans" ja klõpsake <strong>Install</strong>.</p>

        <p><strong>Meetod 2: Käsitsi installimine</strong></p>

        <ol>
        <li>Allalaadimine:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Pakkige ZIP lahti</li>
        <li>Valige .ttf / .otf failid</li>
        <li>Parempoolne klõps → <strong>Installi</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        või<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nimi\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installimine Linuxis</h3>

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

        <p>Kontroll:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Järjehoidjate haldamine",
        "bookmark_add": "Lisa järjehoidja",
        "bookmark_add_tooltip": "Salvesta praegune leht järjehoidjana",
        "bookmark_remove": "Eemalda järjehoidja",
        "bookmark_remove_tooltip": "Kustuta märgitud järjehoidja",
        "bookmark_remove_all": "Eemalda kõik",
        "bookmark_remove_all_tooltip": "Kustuta selle PDF-i kõik järjehoidjad",
        "bookmark_jump": "Hüppa järjehoidjale",
        "bookmark_jump_tooltip": "Hüppa valitud lehele",
        "bookmark_name": "Nimi",
        "bookmark_page": "Leht",
        "bookmark_no_bookmarks": "Järjehoidjaid pole.\nPraeguse lehe järjehoidjana salvestamiseks klõpsake nuppu 'Lisa'.",
        "bookmark_added": "Järjehoidja lehele {0} lisatud: {1}",
        "bookmark_removed": "Järjehoidja eemaldatud: {0}",
        "bookmark_all_removed": "Kõik järjehoidjad on eemaldatud.",
        "bookmark_name_default": "Leht {0}",
        "bookmark_name_prompt": "Järjehoidja nimi:\n(pikk tekst lühendatakse 50 tähemärgini)",
        "bookmark_name_prompt_title": "Järjehoidja nimi",
        "bookmark_confirm_remove_all": "Kas olete kindel, et soovite eemaldada kõik {0} järjehoidjat?",
        "menu_bookmarks": "Järjehoidjad",
        "bookmark_manage": "Halda järjehoidjaid",
        "bookmark_next": "Järgmine järjehoidja",
        "bookmark_prev": "Eelmine järjehoidja",
        "bookmark_page_display": "Leht {0}",
        "bookmark_exists": "Selle lehe jaoks selle nimega järjehoidja on juba olemas.",
        "bookmark_select_first": "Palun valige kõigepealt järjehoidja.",
        "bookmark_confirm_remove": "Kas olete kindel, et soovite eemaldada järjehoidja 'Leht {0}: {1}'?",
        "bookmark_jumped_to": "Hüpatud järjehoidjale '{0}' lehel {1}.",
        "bookmark_jumped_to_voice": "Järjehoidja {0}, leht {1}",
        "btn_close": "Sule",

        "bookmark_list": "Teie järjehoidjad",
        "bookmark_rename": "Nimeta järjehoidja ümber",
        "bookmark_rename_tooltip": "Muuda valitud järjehoidja nime",
        "bookmark_rename_title": "Nimeta järjehoidja ümber",
        "bookmark_rename_prompt": "Uus nimi järjehoidjale lehel {0}:\n(maks. 50 tähemärki)",
        "bookmark_renamed": "Järjehoidja '{0}' on ümber nimetatud kujule '{1}'.",
        "bookmark_item_tooltip": "Leht {0}: {1}\nHüppamiseks topeltklõps",
        "bookmark_name_exists_question": "Sellel lehel on juba olemas järjehoidja nimega '{0}'.\nKas nimeta ikkagi ümber?",

        "context_bookmarks": "Järjehoidjad",
        "context_bookmark_add_here": "Lisa sellele lehele järjehoidja",
        "context_bookmarks_existing": "Olemasolevad järjehoidjad:",
        "context_bookmarks_jump": "Hüppa järjehoidjale:",
        "context_bookmarks_none": "Järjehoidjaid pole",
        "context_bookmarks_clear_all": "Eemalda kõik {0} järjehoidjat",

        "bookmark_search_placeholder": "Otsi järjehoidjaid... (nimi või leht)",
        "bookmark_search_results": "Leitud %d järjehoidjat otsingule \"%s\"",
        "bookmark_no_search_results": "Otsingule \"%s\" ei leitud ühtegi järjehoidjat",
        "bookmark_no_search_results_label": "Otsingule \"%s\" tulemusi pole",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF-i metaandmete redigeerimine",
        "metadata_title": "Pealkiri",
        "metadata_title_placeholder": "Dokumendi pealkiri",
        "metadata_title_tooltip": "Dokumendi pealkiri (kuvatakse tiitliribal)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Autori nimi",
        "metadata_author_tooltip": "Dokumendi looja",
        "metadata_subject": "Teema",
        "metadata_subject_placeholder": "Dokumendi teema",
        "metadata_subject_tooltip": "Sisu lühikirjeldus",
        "metadata_keywords": "Märksõnad",
        "metadata_keywords_placeholder": "Komadega eraldatud märksõnad",
        "metadata_keywords_tooltip": "Dokumendi kategoriseerimise märksõnad",
        "metadata_creator": "Looja",
        "metadata_creator_placeholder": "Rakendus, mis lõi PDF-i",
        "metadata_creator_tooltip": "Tarkvara, millega dokument loodi",
        "metadata_producer": "Tootja",
        "metadata_producer_placeholder": "Rakendus, mis konverteeris PDF-i",
        "metadata_producer_tooltip": "Tarkvara, mis konverteeris PDF-i",
        "metadata_creation_date": "Loomise kuupäev",
        "metadata_creation_date_tooltip": "Dokumendi loomise kuupäev",
        "metadata_mod_date": "Muutmise kuupäev",
        "metadata_mod_date_tooltip": "Viimase muutmise kuupäev",
        "metadata_pdf_info": "📄 PDF-i teave",
        "metadata_pages": "Lehtede arv",
        "metadata_file_size": "Faili suurus",
        "metadata_pdf_version": "PDF-i versioon",
        "metadata_encrypted": "Krüptitud",
        "metadata_encrypted_yes": "Jah (parooliga kaitstud)",
        "metadata_encrypted_no": "Ei",
        "metadata_reload": "📂 Laadi PDF-ist uuesti",
        "metadata_reset": "Loobu muudatustest",
        "metadata_reloaded": "Metaandmed laaditi PDF-ist uuesti.",
        "metadata_reset_done": "Kõik metaandmete väljad on lähtestatud.",
        "metadata_no_file": "Ühtegi PDF-faili pole laaditud.",
        "metadata_save_error": "Viga metaandmete salvestamisel",
        "metadata_saved": "Metaandmed on edukalt salvestatud.",
        "metadata_pdf_version_unknown": "PDF (teadmata)",
        "metadata_saved_message": "Metaandmed on edukalt salvestatud.",
        "metadata_saved_voice": "Metaandmed salvestatud.",

        "metadata_custom": "🔧 Kohandatud metaandmed",
        "metadata_custom_placeholder": "{\n  \"minu_väli\": \"minu väärtus\",\n  \"teine_väli\": 123\n}",
        "metadata_custom_tooltip": "JSON-vorming kohandatud metaandmete jaoks (valikuline)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Valitud mall \"{0}\" - Sisestamiseks topeltklõps",
        "text_use_template": "Kasuta tekstiplokki",
        "text_type": "Tüüp",
        "text_search_templates": "Otsi tekstiplokke...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Ekspordi / Impordi teave",
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

        <h3>📦 Mida eksporditakse? (Ülevaade)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Üldised rakenduse seaded</span></li>
            <li class="detail">• Tume/Hele režiim</li>
            <li class="detail">• Piltide tumeda režiimi inverteerimine</li>
            <li class="detail">• Halli läviväärtus</li>
            <li class="detail">• Keel</li>
            <li class="detail">• Akna geomeetria</li>
            <li class="detail">• Suumirežiim</li>
            <li class="detail">• Navigeerimine (Navigeerimisriba nähtav)</li>
            <li class="detail">• Kõne väljund (sisse/välja)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Varundamise seaded</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Failide nimetamine (Ajatempel, Eraldaja, Järelliited)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Sisestuste seaded</span></li>
            <li class="detail">• Allkirjad</li>
            <li class="detail">• Tekst ja tekstiplokid</li>
            <li class="detail">• Risted, pildid ja kujundid</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-i seaded</span></li>
            <li class="detail">• Keel</li>
            <li class="detail">• Sunnitud OCR · Lehe režiim</li>
            <li class="detail">• Pildi eeltöötlus: Kalde parandus, Puhastus, Ülessämplimine</li>
            <li class="detail">• Paralleelsete tööde arv</li>
            <li class="detail">• Inverteerimise režiim</li>
            <li class="detail">• Halli läviväärtus</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Järjehoidjad</span></li>
            <li class="detail">• Kõik järjehoidjad PDF-faili kohta (Leht, Nimi, Loomise aeg)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Paroolide andmebaas</span></li>
            <li class="detail">• Salvestatud PDF-paroolid (valikuliselt krüptitud või lihttekstina)</li>
            <li class="detail">• Peaparooli räsi (kui on määratud)</li>
            <li class="detail">• Kinnituse andmed</li>
        </ul>

        <h4>⚠️ Olulised märkused</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Importimisel:</strong>
            <ul>
                <li><span class="warning">➜ KÕIK praegused seaded kirjutatakse täielikult üle</span></li>
                <li>• Rakenduse taaskäivitamine on kohustuslik</li>
                <li>• Olemasolevad allkirjad, tekstiplokid ja järjehoidjad asendatakse</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Peaparool ja ekspordi režiim:</strong>
            <ul>
                <li>• Kui peaparool on aktiivne, saate valida:</li>
                <li>  - <span style="color: #98FB98;"><strong>Dešifreeritud</strong></span> (paroolid on ZIP-is lihttekstina)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Krüptitud</strong></span> (loetav ainult peaparooliga sihtsüsteemis)</li>
                <li>• Peaparooli räsi salvestatakse <strong>alati</strong> krüptitult</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Turvamärkus:</strong>
            <ul>
                <li>• Eksporditud ZIP-fail sisaldab tundlikke andmeid (<strong>paroolid, järjehoidjad, allkirjad</strong>)</li>
                <li>• Palun hoidke seda turvaliselt (nt krüptitud USB-mälupulk, paroolihaldur)</li>
                <li>• Kui fail läheb kaotsi, on salvestatud PDF-paroolid pöördumatult kadunud</li>
            </ul>
        </div>

        <h4>📁 Ekspordi vorming</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Seaded salvestatakse ühte ZIP-faili:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            See ZIP sisaldab täielikku <code>settings.json</code> (teie konfiguratsioonist) ning võimalikke manustatud allkirja pildifaile ja krüptitud paroole.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Allkirjad - Juhend",
        'signature_guide_html': """
        📝 <strong>Allkirjad - Lühijuhend</strong><br>
        <ul>
        <li>Seadista peakood</li>
        <li>Seadista allkirjad menüüs <em>Seaded</em> (suurus, ajatempel, …)</li>
        <li>Sisesta <strong>PAREMKLÕPSUGA</strong> soovitud asukohta (peakood on vajalik üks kord seansi kohta)</li>
        <li>Liiguta allkirja hiire või nooleklahvidega</li>
        <li>Sisesta mitu allkirja järjest</li>
        <li>Kohanda iga allkirja eraldi</li>
        <li>Loobu üksikust allkirjast</li>
        <li>Salvesta / loobu kõigist allkirjadest korraga</li>
        <li>Alternatiivselt võib kasutada ka menüüriba.</li>
        </ul>
        """,
        'signature_guide_voice': "Lühijuhend allkirjadele. Seadista peakood. Seadista allkirjad seadetes. Sisesta paremklõpsuga.",

        'image_guide_title': "Piltide sisestamine - Juhend",
        'image_guide_html': """
        📷 <strong>Piltide sisestamine PDF-i - Lühijuhend</strong><br>
        <ol>
        <li>Paremklõps soovitud asukohal</li>
        <li><em>„Sisesta pilt“</em> → Vali pilt</li>
        <li>Paiguta pilt: Lohista hiirega</li>
        <li>Kohanda suurust: Lohista nurkadest/servadest</li>
        <li>Säilita kuvasuhe: Klahv <strong>[A]</strong></li>
        <li>Edasised kohandused: Paremklõps pildil</li>
        </ol>
        <p><strong>Vihje:</strong> Kontekstimenüüs saate seadeid kohandada.</p>
        """,
        'image_guide_voice': "Lühijuhend piltidele. Paremklõps, sisesta pilt, vali. Paiguta hiirega, kohanda suurust nurkadest. Kuvasuhe klahviga A.",

        'form_guide_title': "Vormide sisestamine - Juhend",
        'form_guide_html': """
        📐 <strong>Vormide sisestamine PDF-i - Lühijuhend</strong><br>
        <ol>
        <li>Vali vormi tüüp (ristkülik, ellips, joon, nool)</li>
        <li>Klõpsa asukohal:
            <ul>
            <li>Ristküliku/ellipsi puhul: Üks klõps paigutab vormi</li>
            <li>Joon/ nool: Kaks klõpsu algus- ja lõpp-punkti jaoks</li>
            </ul>
        </li>
        <li>Paiguta vorm: Lohista hiirega</li>
        <li>Kohanda suurust: Lohista nurkadest/servadest</li>
        <li>Salvesta vorm: <strong>Enter</strong></li>
        <li>Loobu vormist: <strong>ESC</strong></li>
        <li>Edasised kohandused: Paremklõps vormil</li>
        </ol>
        <p><strong>Vihje:</strong> Kontekstimenüüs saate seadeid kohandada.</p>
        """,
        'form_guide_voice': "Lühijuhend vormidele. Vali vormi tüüp. Ristküliku või ellipsi puhul klõpsa üks kord, joone või noole puhul kaks korda. Paiguta hiirega, kohanda suurust nurkadest. Salvesta Enteriga, loobu Escapiga.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "eelmine",
        "btn_next_result": "järgmine",
        "ocr_text_window": "OCR tekstiaknad",
        "bookmark_existing": "Olemasolevad järjehoidjad",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR võrdlus Mac - Windows",
        'ocr_method_mac_win_title': "OCR erinevused Maci ja Windowsi vahel",
        'ocr_method_mac_win_voice': "Mac on parem",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Erinevused macOS ja Windowsi vahel</strong></p>

        <p><strong>macOS (soovitatav)</strong></p>
        <p>Tööriist:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Tulemus:</p>
        <ul>
        <li>Otsitav PDF manustatud tekstiga, mis säilitab suures osas algse paigutuse.</li>
        </ul>
        <p>Eelised:</p>
        <ul>
        <li>Suurepärane tekstituvastuse kvaliteet (ka viltuste lehekülgede korral).</li>
        <li>Vektorgraafika ja fontide säilitamine.</li>
        <li>GUI edenemisriba alamprotsessi hindamise kaudu.</li>
        <li>Täielik kontroll kõigi OCR parameetrite üle (Deskew, Clean, Oversample, optimeerimine).</li>
        <li>Tekstiotsing on otse saadaval põhiaknas (PDF vaade).</li>
        </ul>
        <p>Puudused:</p>
        <ul>
        <li>Nõuab täiendavaid süsteemitööriistu (ocrmypdf, Ghostscript, unpaper, pngquant – sisalduvad rakenduse paketis).</li>
        <li>Keerulisem veakäsitlus (deadlocks, ajapiirangud).</li>
        </ul>

        <p><strong>Windows (stabiilne alternatiiv)</strong></p>
        <p>Tööriist:</p>
        <ul>
        <li>pytesseract (otsene ühendus Tesseractiga) + reportlab + PyPDF2</li>
        </ul>
        <p>Tulemus:</p>
        <ul>
        <li>Otsitav PDF, mis visuaalselt vastab pildi-PDF-ile, kuid on otsitav läbi läbipaistva teksti.</li>
        </ul>
        <p>Eelised:</p>
        <ul>
        <li>Praegu ei tule ühtegi meelde.</li>
        </ul>
        <p>Puudused:</p>
        <ul>
        <li>PDF on sisuliselt pilt nähtamatu tekstiga; paigutus võib keerukate dokumentide (veerud, tabelid) puhul veidi erineda.</li>
        <li>Puudub automaatne kaldekorrektsioon (--deskew) või pildi puhastamine (--clean).</li>
        <li>GUI edenemisriba värskendatakse vaid jämedalt töödeldud lehekülgede arvu alusel.</li>
        <li>OCR-i kiirus on veidi aeglasem (kuna iga lehekülge töödeldakse eraldi).</li>
        <li>Tekstiotsing suunatakse ümber OCR tekstiaknasse.</li>
        </ul>

        <p><strong>Ühisjooned</strong></p>
        <ul>
        <li>Mõlemad meetodid loovad otsitava PDF-i samasse kataloogi, kus asub lähtefail.</li>
        <li>OCR-i seadeid (keel, DPI, lehekülje segmentimise režiim, OCR-mootori režiim) saab konfigureerida OCRSettingsDialogi kaudu ja need kehtivad mõlemas implementatsioonis.</li>
        </ul>

        <p><strong>Soovitus:</strong></p>
        <ul>
        <li>macOS: ocrmypdf binaar annab parimad tulemused – Ostke Mac ja kasutage versiooni (PDFDarkView Macidele, millel on Apple Silicon või Intel kiip). OCR-i tulemused on paremad kui Windowsis!</li>
        <li>Windows: Kasutage pytesseract lahendust. See on stabiilne ja annab enamiku dokumentide jaoks täiesti piisava kvaliteedi.</li>
        </ul>

        <p><strong>Oluline märkus:</strong></p>
        <ul>
        <li>Mõlemad versioonid on täielikult integreeritud kasutajaliidesesse – kasutaja ei märka erinevust.</li>
        <li>Programm otsustab automaatselt, millist OCR-mootorit kasutada, lähtudes operatsioonisüsteemist.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Loo allkiri (skaneeringust)",
        "signature_create_title": "Vali skaneeritud allkiri (PDF/pilt)",
        "image_pdf_filter": "Pildid ja PDF",
        "signature_pdf_empty": "PDF ei sisalda lehekülgi.",
        "signature_created_success": "Allkiri on edukalt loodud: {0}",
        "signature_create_error": "Viga allkirja loomisel:\n{0}",
        "rembg_missing": "rembg pole installitud.\nPalun installige: pip install rembg\nViga: {0}",
        "signature_name_title": "Failinimi allkirja jaoks",
        "signature_name_message": "Palun sisestage uuele allkirjale failinimi (salvestatakse PNG-na läbipaistva taustaga):",
        "signature_name_label": "Failinimi:",
        "signature_name_voice": "Sisestage allkirja failinimi",
        "signature_processing": "Töötlemine käib...",
        "signature_creation_title": "Allkirja loomine",
        "signature_overwrite_warning": "Fail '{0}' on juba olemas. Kas soovite üle kirjutada?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Valmistage PDF allkirja jaoks ette",
        "signature_prepare_instruction":"Palun valige PDF, mis sisaldab ühel leheküljel skaneeritud allkirja.\n\nOptimaalseks tuvastamiseks veenduge, et:\n• Allkiri on kirjutatud musta tindiga (pastapliiats või peen viltpliiats) valgel paberil.\n• Allkiri asub muidu tühja A4 lehekülje ülemises kolmandikus.\n• PDF on skaneeritud vähemalt 300 dpi-ga.\n• Allkiri on selge ja mitte liiga peen.\n• Ei esine segavaid taustamustreid ega jooni.",
        "signature_prepare_voice":"Palun valige PDF skaneeritud allkirjaga. Pöörake tähelepanu heale kvaliteedile ja kontrastile.",
        "sig_thickness_label":"Joone paksus:",
        "sig_thickness_normal":"Tavaline (peenike)",
        "sig_thickness_bold":"Rasvane (soovitatav)",
        "sig_thickness_very_bold":"Väga rasvane",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI ja OCR keelte lisamine - Juhend",
        'language_guide_title': "GUI ja OCR keelte lisamine",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Laadige soovitud tõlkefail <code>translations_xy.py</code> alla aadressilt<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        ja asetage see järgmisesse kataloogi:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Avage oma veebibrauser.</li>
        <li>Minge aadressile: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Otsige ekraani paremast servast "Releases" ja valige see, mis on märgistatud <strong>"latest"</strong>.</li>
        <li>Järgmisel väljalaskelehel laadige alla fail <code>Source Code.zip</code> allosas.</li>
        <li>Pakige ZIP-fail lahti.</li>
        <li>Otsige lahtipakitud kaustast kõik vajalikud keelefailid ja kopeerige need kataloogi:<br/>
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
        "menu_watermark":"Sisesta vesimärk",
        "fullpage_text_watermark_title":"Tekst vesimärgina",
        "fullpage_image_watermark_title":"Pilt vesimärgina",
        "filename_with_watermark":"_vesimargiga",
        "watermark_text":"Tekst:",
        "watermark_text_placeholder":"Teie vesimärgi tekst...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Fondi suurus:",
        "watermark_format":"Vormindus:",
        "watermark_bold":"Rasvane",
        "watermark_italic":"Kursiiv",
        "watermark_color":"Värv:",
        "watermark_choose_color":"Vali värv...",
        "watermark_opacity":"Läbipaistmatus / Läbipaistvus:",
        "watermark_direction":"Lugemissuund:",
        "watermark_direction_l_r":"Vasak → Parem",
        "watermark_direction_bl_tr":"All vasak → Ülemine parem",
        "watermark_direction_tl_br":"Ülemine vasak → All",
        "watermark_direction_b_t":"All → Üles",
        "watermark_direction_t_b":"Üles → Alla",
        "watermark_preview":"Eelvaade:",
        "watermark_preview_sample":"Näidistekst",
        "watermark_empty_text":"Palun sisestage tekst.",
        "watermark_applied":"Vesimärk rakendati kõikidele lehekülgedele.",
        "watermark_saved":"Vesimärk salvestatud.",
        "image_scale":"Suurus:",
        "image_preview":"Pildi eelvaade:",
        "no_image_selected":"Pilti pole valitud",
        "browse":"Sirvi...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redigeerimised",
        "redact_add_black": "Redigeerimine (must)",
        "redact_add_white": "Redigeerimine (valge / kustuta)",
        "redact_added_black": "Lisatud must redigeerimine",
        "redact_added_white": "Lisatud valge redigeerimine",
        "redact_apply_all": "Rakenda kõik redigeerimised ja salvesta",
        "redact_discard_all": "Loobu kõikidest redigeerimistest",
        "redact_discard": "Loobu sellest redigeerimisest",
        "no_redactions": "Redigeerimisi pole",
        "redact_confirm_title": "Rakenda redigeerimised püsivalt",
        "redact_confirm_message": "Hoiatus: Märgistatud alad kustutatakse pöördumatult (must või valge).\nVarukoopia luuakse (kui see on lubatud).\n\nJätkata?",
        "redact_apply": "Jah, redigeeri kohe",
        "redact_saved": "{0} redigeerimist rakendati ja salvestati edukalt.",
        "redact_saved_voice": "{0} redigeerimist rakendatud",
        "redact_error": "Tõrge redigeerimisel",
        "filename_redacted":"_redigeeritud",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Sisesta leheküljenumbrid',
        'page_numbers_format': 'Numbri formaat:',
        'page_numbers_format_arabic': '1, 2, 3 ... (araabia)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Rooma väike)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Rooma suur)',
        'page_numbers_format_letter': 'A, B, C ... (tähed)',
        'page_numbers_format_custom': 'Kohandatud',
        'page_numbers_custom_pattern': 'Muster:',
        'page_numbers_custom_placeholder': 'nt "Lehekülg {nummer}" või "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Kasutage {nummer} praeguse leheküljenumbri ja {total} koguarvu jaoks',
        'page_numbers_position': 'Asukoht:',
        'page_numbers_pos_tl': 'Ülemine vasak',
        'page_numbers_pos_tc': 'Ülemine keskel',
        'page_numbers_pos_tr': 'Ülemine parem',
        'page_numbers_pos_ml': 'Keskel vasak',
        'page_numbers_pos_mc': 'Keskel',
        'page_numbers_pos_mr': 'Keskel parem',
        'page_numbers_pos_bl': 'Alumine vasak',
        'page_numbers_pos_bc': 'Alumine keskel',
        'page_numbers_pos_br': 'Alumine parem',
        'page_numbers_margins': 'Veerised:',
        'page_numbers_margin_x': 'Horisontaalne kaugus:',
        'page_numbers_margin_y': 'Vertikaalne kaugus:',
        'page_numbers_range': 'Lehekülgede vahemik:',
        'page_numbers_all_pages': 'Kõik leheküljed',
        'page_numbers_custom_range': 'Kohandatud vahemik',
        'page_numbers_from': 'Alates:',
        'page_numbers_to': 'Kuni:',
        'page_numbers_progress': 'Leheküljenumbrite sisestamine...',
        'page_numbers_start': 'Leheküljenumbrite sisestamise alustamine...',
        'page_numbers_cancel': 'Leheküljenumbrite sisestamine tühistatud',
        'page_numbers_success': 'Leheküljenumbrid lisati edukalt.\n\nKas soovite avada uue PDF-i?\n\n{0}',
        'page_numbers_complete': 'Leheküljenumbrid lisatud',
        'page_numbers_error_format': 'Tõrge leheküljenumbrite sisestamisel: {0}',
        'page_numbers_content_type': 'Sisu tüüp:',
        'page_numbers_tab_simple': 'Lihtne number',
        'page_numbers_tab_range': 'Lehekülg X / Y-st',
        'page_numbers_tab_date': 'Kuupäev',
        'page_numbers_tab_custom': 'Vaba tekst',
        'page_numbers_range_format': 'Formaat:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Lehekülg {aktuell} / {gesamt}',
        'page_numbers_range_custom': 'Kohandatud',
        'page_numbers_range_placeholder': 'nt "Lehekülg {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Kuupäeva formaat:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. jaanuar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Kohandatud',
        'page_numbers_date_placeholder': 'nt %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Asukoht:',
        'page_numbers_date_before': 'Kuupäev enne leheküljenumbrit',
        'page_numbers_date_after': 'Kuupäev pärast leheküljenumbrit',
        'page_numbers_date_only': 'Ainult kuupäev (ilma leheküljenumbrita)',
        'page_numbers_custom_text': 'Kohandatud tekst:',
        'page_numbers_custom_placeholder_text': 'Kasutage {seite} leheküljenumbri ja {gesamt} koguarvu jaoks\nnt "Konfidentsiaalne - Lehekülg {seite}" või "{seite} / {gesamt}"',
        "filename_with_page_number":"_lehekyljenumbriga",
        "filename_with_page_declaration":"_lehekylje_maaratega",
        "filename_with_pagenumber":"_lehekyljenumbriga",
        "filename_with_date":"_kuupaevaga",
        "filename_with_my_page_declaration":"_kohandatud_maaratega",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Salvestamata muudatused",
        "unsaved_changes_message_darkmode": "On salvestamata sisestusi.\nKas soovite need enne ümberlülitamist salvestada?",
        "save_and_switch": "Salvesta ja lülita",
        "discard_and_switch": "Lülita kohe",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Ekspordi leheküljed piltidena',
        'export_images_menu': 'Ekspordi piltidena (PNG/JPEG)',
        'export_images_format': 'Pildi formaat:',
        'export_images_dpi': 'Resolutsioon (DPI):',
        'export_images_quality': 'JPEG kvaliteet:',
        'export_images_range': 'Lehekülgede vahemik:',
        'export_images_all_pages': 'Kõik leheküljed',
        'export_images_custom_range': 'Kohandatud vahemik',
        'export_images_from': 'Alates:',
        'export_images_to': 'Kuni:',
        'export_images_options': 'Valikud:',
        'export_images_single_files': 'Iga lehekülg eraldi failina',
        'export_images_subfolder': 'Ekspordi alamkausta',
        'export_images_subfolder_info': 'Alamkausta "PDFnimi_pildid"',
        'export_images_same_folder': 'Samas kaustas kui PDF',
        'export_images_apply_darkmode': 'Rakenda PDFDarkView seaded (Tume režiim)',
        'export_images_target_folder': 'Sihtkaust:',
        'export_images_browse': 'Sirvi...',
        'export_images_preview': 'Eelvaade:',
        'export_images_preview_info': 'Valige ekspordi seaded',
        'export_images_preview_info_detail': '{0} lehekülge kui {1}\nResolutsioon: {2} DPI\nFailinimi: {3}\n{4}',
        'export_images_select_folder': 'Valige sihtkaust',
        'export_images_start': 'Pildi ekspordi alustamine...',
        'export_images_progress': 'Piltide eksportimine...',
        'export_images_saving': 'Lehekülje {0} salvestamine / {1}...',
        'export_images_success': 'Eksport õnnestus!\n\n{0} pilti salvestati:\n{1}',
        'export_images_complete': 'Piltide eksport lõpetatud',
        'export_images_open_folder': '📁 Ava kaust',
        'export_images_cancel': 'Piltide eksport tühistatud',
        'export_images_error_format': 'Tõrge piltide eksportimisel: {0}',
        'export_images_pdf2image_missing': 'Teek "pdf2image" pole installitud.\n\nPalun installige see käsuga:\npip install pdf2image\n\nWindowsi jaoks vajate ka Popplerit:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konverteerimine pikaajaliseks arhiveerimiseks',
        'pdfa_menu': 'PDF/A konverteerimine (arhiveerimiskõlbulik)',
        'pdfa_info': 'Konverteerib PDF-i PDF/A vormingusse.\n\nPDF/A on spetsiaalselt loodud pikaajaliseks arhiveerimiseks ja tagab, et dokument kuvatakse tulevikus õigesti.',
        'pdfa_standard': 'PDF/A standard:',
        'pdfa_standard_select': 'Versioon:',
        'pdfa_1': 'PDF/A-1 (lihtne, laialdaselt ühilduv)',
        'pdfa_2': 'PDF/A-2 (kaasaegne, parem tihendus)',
        'pdfa_3': 'PDF/A-3 (uusim versioon, lubab manuseid)',
        'pdfa_standards_explanation': '📖 Standardite selgitus:\n\n'
            '• PDF/A-1: Põhiline, ühilduv vanemate süsteemidega (umbes 2005)\n'
            '• PDF/A-2: Kaasaegsem, parem tihendus, läbipaistvuse tugi (umbes 2011)\n'
            '• PDF/A-3: Uusim versioon, lubab failimanuste manustamist (umbes 2013)\n\n'
            'Soovitus: PDF/A-2 on hea kompromiss ühilduvuse ja kaasaegsete funktsioonide vahel.',
        'pdfa_options': 'Valikud:',
        'pdfa_compress_enable': 'Tihenda PDF (väiksem fail)',
        'pdfa_metadata_preserve': 'Säilita metaandmed (pealkiri, autor jne)',
        'pdfa_target_folder': 'Sihtkaust:',
        'pdfa_browse': 'Sirvi...',
        'pdfa_select_folder': 'Valige sihtkaust',
        'pdfa_ocr_info_unknown': '🔍 Teksti sisu ei õnnestunud kontrollida.',
        'pdfa_ocr_info_not_needed': '✅ Tekst olemas - OCR ei ole vajalik.\nPDF/A saab luua otse.',
        'pdfa_ocr_info_recommended': '⚠️ Piisavat teksti ei leitud.\n\nOtsitavate PDF-ide jaoks soovitame kõigepealt käivitada OCR.\nMärkus: PDF/A töötab ka ilma OCR-ita - kuid tekst ei ole siis otsitav.',
        'pdfa_ocr_info_error': '❌ Tõrge kontrollimisel: {0}',
        'pdfa_start': 'PDF/A konverteerimise alustamine...',
        'pdfa_progress': 'PDF/A konverteerimine käib...',
        'pdfa_success': 'PDF/A konverteerimine õnnestus!\n\nSalvestatud kui:\n{0}\n\nKas soovite avada uue PDF-i?',
        'pdfa_complete': 'PDF/A konverteerimine lõpetatud',
        'pdfa_cancel': 'PDF/A konverteerimine tühistatud',
        'pdfa_error_format': 'Tõrge PDF/A konverteerimisel:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Teek "ocrmypdf" pole installitud.\n\nPalun installige see käsuga:\npip install ocrmypdf',
        'btn_convert': 'Konverteeri',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimeeri PDF (vähenda faili suurust)',
        'optimize_menu': 'Optimeeri PDF (faili suurus)',
        'optimize_info': 'Vähendab PDF-faili suurust erinevate optimeerimismeetodite abil.\n\nMida kõrgem on tihendustase, seda väiksemaks fail muutub - koos võimaliku kvaliteedikaoga piltides.',
        'optimize_level': 'Tihendustase:',
        'optimize_level_low': 'Madal (kiire, väike kokkuhoid)',
        'optimize_level_medium': 'Keskmine (hea kompromiss)',
        'optimize_level_high': 'Kõrge (suur kokkuhoid)',
        'optimize_level_maximum': 'Maksimaalne (maksimaalne kokkuhoid, aeglane)',
        'optimize_level_explanation': 'Soovitus: "Keskmine" on hea kompromiss kiiruse ja faili suuruse vahel.',
        'optimize_options': 'Valikud:',
        'optimize_compress_images': 'Tihenda pilte (vähenda JPEG kvaliteeti)',
        'optimize_clean_objects': 'Eemalda kasutamata objektid',
        'optimize_preserve_metadata': 'Säilita metaandmed (pealkiri, autor jne)',
        'optimize_image_quality': 'Pildi kvaliteet:',
        'optimize_range': 'Lehekülgede vahemik:',
        'optimize_all_pages': 'Kõik leheküljed',
        'optimize_custom_range': 'Kohandatud vahemik',
        'optimize_from': 'Alates:',
        'optimize_to': 'Kuni:',
        'optimize_target_folder': 'Sihtkaust:',
        'optimize_browse': 'Sirvi...',
        'optimize_select_folder': 'Valige sihtkaust',
        'optimize_info_box': 'Teave',
        'optimize_info_text': 'Optimeerimine võib suurte PDF-ide puhul võtta mitu minutit.\n\nPildid salvestatakse vähendatud kvaliteediga, mis võib faili suurust oluliselt vähendada.',
        'optimize_start': 'PDF optimeerimise alustamine...',
        'optimize_progress': 'PDF-i optimeerimine...',
        'optimize_cancel': 'PDF optimeerimine tühistatud',
        'optimize_complete': 'PDF optimeerimine lõpetatud',
        'optimize_error_format': 'Tõrge PDF optimeerimisel:\n\n{0}',
        'optimize_success_message': 'PDF optimeerimine õnnestus!\n\nSalvestatud kui:\n{0}\n\nEnne: {1}\nPärast: {2}\nKokkuhoid: {3:.1f}%\n\n{4}\n\nKas soovite avada optimeeritud PDF-i?',
        'optimize_success_message_no_size': 'PDF optimeerimine õnnestus!\n\nSalvestatud kui:\n{0}\n\nSuuruse teave pole saadaval.\n\nKas soovite avada optimeeritud PDF-i?',
        'optimize_result_positive': 'Faili vähendati {0:.1f}%.',
        'optimize_result_zero': 'Faili suurus ei muutunud.',
        'optimize_result_negative': 'Fail suurenes {0:.1f}%.\nOptimeerimine jäeti vahele, algne fail säilitati.',
        'btn_optimize': 'Alusta optimeerimist',
        'filename_optimize_low_suffix': '_optimeeritud_madal',
        'filename_optimize_medium_suffix': '_optimeeritud',
        'filename_optimize_high_suffix': '_optimeeritud_korge',
        'filename_optimize_maximum_suffix': '_optimeeritud_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Kärbi PDF',
        'crop_menu': 'Kärbi PDF (Crop)',
        'crop_range': 'Rakenda:',
        'crop_all_pages': 'Kõik leheküljed',
        'crop_current_page': 'Ainult praegune lehekülg',
        'crop_values': 'Kärpimise väärtused (punktides):',
        'crop_left': 'Vasak:',
        'crop_right': 'Parem:',
        'crop_top': 'Ülemine:',
        'crop_bottom': 'Alumine:',
        'crop_presets': 'Eelseaded:',
        'crop_preset_white': 'Tuvasta valged veerised',
        'crop_reset': 'Lähtesta',
        'crop_mouse_hint': '🖱️ Lohista ristkülik ala ligikaudseks valimiseks.\nSeejärel saate väärtusi SpinBoxides täpselt reguleerida.\nManuaalne reguleerimine hiirega ei ole võimalik.',
        'crop_apply': 'Kärbi',
        'crop_scope_all': 'Kõik leheküljed',
        'crop_scope_current': 'Praegune lehekülg',
        'crop_new_size': 'Uus suurus: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'PDF-i pole laaditud',
        'crop_preview_error': 'Tõrge eelvaate laadimisel',
        'crop_start': 'Kärpimise alustamine...',
        'crop_progress': 'PDF-i kärpimine...',
        'crop_success': 'PDF kärbitud edukalt!\n\nSalvestatud kui:\n{0}\n\nKas soovite avada kärbitud PDF-i?',
        'crop_complete': 'Kärpimine lõpetatud',
        'crop_cancel': 'Kärpimine tühistatud',
        'crop_error_format': 'Tõrge kärpimisel:\n\n{0}',
        'filename_crop_suffix': '_karbitud',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF-i silumine (Flatten)',
        'flatten_menu': 'PDF-i silumine (Flatten)',
        'flatten_info': 'PDF-i silumine "põletab" kõik redigeeritavad elemendid lehekülje sisusse.\n\nPärast seda ei saa vormivälju, annotatsioone, tekste, riste, allkirju, pilte ja kujundeid enam eraldi redigeerida.',
        'flatten_explanation_title': '📖 Milleks see hea on?',
        'flatten_explanation_text': 'Silumine on vajalik järgmistes olukordades:\n\n'
            '• 📄 Soovite dokumendi printimiseks ette valmistada\n'
            '• 🔒 Soovite takistada kellegi vormiväljade muutmist\n'
            '• 📎 Soovite annotatsioonid ja kommentaarid "püsivalt" dokumenti manustada\n'
            '• 🖼️ Soovite lisatud tekstid, ristid, allkirjad, pildid ja kujundid püsivalt dokumenti kinnitada\n'
            '• 📦 Soovite faili arhiveerimiseks ette valmistada\n\n'
            'Silumine muudab PDF-i väiksemaks ja takistab elementide juhuslikku liigutamist või kustutamist.',
        'flatten_what_title': 'Mida silutakse?',
        'flatten_what_list': '• ✅ Vormiväljad (tekstiväljad, märkeruudud, nupud)\n'
            '• ✅ Annotatsioonid (kommentaarid, esiletõstmised, märkmed)\n'
            '• ✅ Pealekihid (tekstid, ristid, allkirjad, pildid, kujundid)',
        'flatten_options': 'Valikud:',
        'flatten_forms': 'Silu vormiväljad',
        'flatten_annotations': 'Silu annotatsioonid',
        'flatten_overlays': 'Silu pealekihid (tekstid, ristid, allkirjad, pildid, kujundid)',
        'flatten_target_folder': 'Sihtkaust:',
        'flatten_browse': 'Sirvi...',
        'flatten_select_folder': 'Valige sihtkaust',
        'flatten_warning': '⚠️ Tähtis: Silumine on pöördumatu protsess!\n\nPärast silumist ei saa redigeeritavaid elemente enam eraldi muuta ega kustutada.\nVajadusel looge eelnevalt varukoopia.',
        'flatten_apply': 'Silu',
        'flatten_start': 'Silumise alustamine...',
        'flatten_progress': 'PDF-i silumine...',
        'flatten_success': 'PDF silutud edukalt!\n\nSalvestatud kui:\n{0}\n\nKas soovite avada silutud PDF-i?',
        'flatten_complete': 'Silumine lõpetatud',
        'flatten_cancel': 'Silumine tühistatud',
        'flatten_error_format': 'Tõrge silumisel:\n\n{0}',
        'filename_flatten_suffix': '_silutud',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF-i pealekate (Overlay)',
        'overlay_menu': 'PDF-i pealekate (Overlay)',
        'overlay_info': 'Asetab ühe PDF-i (pealekatte) teise PDF-i peale.\n\nPealekatte PDF asetatakse alus-PDF-ile. See on kasulik vesimärkide, logode, kirjaplankide või templitе jaoks.',
        'overlay_explanation_title': '📖 Milleks see hea on?',
        'overlay_explanation_text': 'Pealekate on vajalik järgmistes olukordades:\n\n'
            '• 🏢 Asetage ettevõtte logo vesimärgina igale leheküljele\n'
            '• 📄 Asetage kirjaplank tühjale PDF-ile\n'
            '• 🖊️ Asetage templi pealekate dokumendile\n'
            '• 🔖 Asetage vesimärk kõikidele lehekülgedele\n'
            '• 📑 Asetage vormi pealekate mallile',
        'overlay_type': 'Pealekatte tüüp:',
        'overlay_type_fullpage': 'Terve lehekülg (kattev)',
        'overlay_type_transparent': 'Terve lehekülg (läbipaistev - soovitatav)',
        'overlay_type_stamp': 'Tempel (positsioneeritav)',
        'overlay_type_info_fullpage': '📄 Pealekatte PDF asetatakse täpselt üle kogu lehekülje.\nValge taust saab eemaldada, nii et nähtavaks jääb ainult sisu.',
        'overlay_type_info_transparent': '🔍 Pealekatte PDF asetatakse üle kogu lehekülje läbipaistva taustaga.\nValge taust eemaldatakse automaatselt - ideaalne vesimärkide ja logode jaoks!',
        'overlay_type_info_stamp': '🖊️ Pealekatte PDF positsioneeritakse ja skaleeritakse templina.\nTäiuslik logode, templitе või allkirjade jaoks kindlates kohtades.',
        'overlay_remove_background': 'Eemalda valge taust:',
        'overlay_remove_background_enable': 'Eemalda pealekatte PDF-ist valge taust (muudab pealekatte läbipaistvaks)',
        'overlay_remove_background_tooltip': 'Eemaldab pealekatte PDF-ist valged alad, et allolev tekst oleks nähtav.',
        'overlay_threshold': 'Läviväärtus:',
        'overlay_threshold_hint': '(1-254, kõrgem = rohkem valget eemaldatakse)',
        'overlay_select_file': 'Valige pealekatte PDF:',
        'overlay_file_placeholder': 'Palun valige PDF-fail pealekatte jaoks',
        'overlay_browse': 'Sirvi...',
        'overlay_select_overlay': 'Valige pealekatte PDF',
        'overlay_range': 'Lehekülgede vahemik:',
        'overlay_all_pages': 'Kõik leheküljed',
        'overlay_custom_range': 'Kohandatud vahemik',
        'overlay_from': 'Alates:',
        'overlay_to': 'Kuni:',
        'overlay_position': 'Asukoht:',
        'overlay_position_center': 'Keskel',
        'overlay_position_top_left': 'Ülemine vasak',
        'overlay_position_top_right': 'Ülemine parem',
        'overlay_position_bottom_left': 'Alumine vasak',
        'overlay_position_bottom_right': 'Alumine parem',
        'overlay_size': 'Suurus:',
        'overlay_size_original': 'Algne suurus',
        'overlay_size_fit_page': 'Kohanda leheküljega',
        'overlay_size_custom': 'Kohandatud (%)',
        'overlay_opacity': 'Läbipaistvus:',
        'overlay_target_folder': 'Sihtkaust:',
        'overlay_browse_folder': 'Sirvi...',
        'overlay_select_folder': 'Valige sihtkaust',
        'overlay_warning': '⚠️ Märkus: Pealekatte PDF asetatakse alus-PDF-ile ja "põletatakse" sellesse.\n\nPealekatte PDF-i elemente ei saa pärast salvestamist enam eraldi redigeerida.',
        'overlay_apply': 'Pealekate',
        'overlay_start': 'Pealekatte alustamine...',
        'overlay_progress': 'PDF-i pealekate...',
        'overlay_success': 'PDF pealekate edukalt!\n\nSalvestatud kui:\n{0}\n\nKas soovite avada pealekattega PDF-i?',
        'overlay_complete': 'Pealekate lõpetatud',
        'overlay_cancel': 'Pealekate tühistatud',
        'overlay_error_format': 'Tõrge pealekattel:\n\n{0}',
        'overlay_no_file': 'Pealekatte PDF-i pole valitud.\n\nPalun valige PDF-fail pealekatte jaoks.',
        'filename_overlay_suffix': '_pealekattega',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Piltide ekstraheerimine PDF-ist',
        'extract_images_menu': 'Ekstraheer kõik pildid',
        'extract_images_info': 'Ekstraheerib kõik pildid PDF-ist ja salvestab need eraldi failidena.\n\nPildid salvestatakse nende algses vormingus või konverteeritakse valitud vormingusse.',
        'extract_images_format': 'Pildi formaat:',
        'extract_images_quality': 'JPEG kvaliteet:',
        'extract_images_options': 'Valikud:',
        'extract_images_subfolder': 'Ekstraheerimine alamkausta ("PDFnimi_pildid")',
        'extract_images_unique': 'Ainult unikaalsed pildid (duplikaatide vältimine)',
        'extract_images_range': 'Lehekülgede vahemik:',
        'extract_images_all_pages': 'Kõik leheküljed',
        'extract_images_custom_range': 'Kohandatud vahemik',
        'extract_images_from': 'Alates:',
        'extract_images_to': 'Kuni:',
        'extract_images_target_folder': 'Sihtkaust:',
        'extract_images_browse': 'Sirvi...',
        'extract_images_select_folder': 'Valige sihtkaust',
        'extract_images_info_box': 'Teave',
        'extract_images_info_text': 'Ekstraheerimine võib suurte PDF-ide puhul võtta mitu minutit.\n\nPildid salvestatakse nende algse nimega (lehekülg_pilt).',
        'extract_images_extract': 'Ekstraheerimine',
        'extract_images_start': 'Ekstraheerimise alustamine...',
        'extract_images_progress': 'Piltide ekstraheerimine...',
        'extract_images_success': '✅ Pildid ekstraheeritud edukalt!\n\n{0} pilti salvestati:\n{1}',
        'extract_images_complete': 'Piltide ekstraheerimine lõpetatud',
        'extract_images_cancel': 'Ekstraheerimine tühistatud',
        'extract_images_error_format': 'Tõrge piltide ekstraheerimisel:\n\n{0}',
        'extract_images_open_folder': '📁 Ava kaust',
        'extract_images_no_images': 'PDF-ist ei leitud pilte.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Mitu lehekülge ühel leheküljel (N-Up)',
        'nup_menu': 'Mitu lehekülge ühel leheküljel (N-Up)',
        'nup_info': 'Korraldab mitu PDF-i lehekülge ühele leheküljele.\n\nIdeaalne kompaktseteks printimisteks, ülevaadeteks või jagamismaterjalideks.',
        'nup_layout': 'Paigutus:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Eelvaade:',
        'nup_preview_info': '{0} lehekülge → {1} lehekülge lehel → {2} lehte\nPaigutus: {3}',
        'nup_order': 'Järjekord:',
        'nup_order_horizontal': 'Horisontaalne (rida rea kaupa)',
        'nup_order_vertical': 'Vertikaalne (veerg veeru kaupa)',
        'nup_order_horizontal_reverse': 'Horisontaalne tagurpidi',
        'nup_order_vertical_reverse': 'Vertikaalne tagurpidi',
        'nup_range': 'Lehekülgede vahemik:',
        'nup_all_pages': 'Kõik leheküljed',
        'nup_custom_range': 'Kohandatud vahemik',
        'nup_from': 'Alates:',
        'nup_to': 'Kuni:',
        'nup_options': 'Valikud:',
        'nup_margins': 'Veerised:',
        'nup_margin_between': 'Lehekülgede vaheline kaugus:',
        'nup_page_numbers': 'Sisesta leheküljenumbrid',
        'nup_target_folder': 'Sihtkaust:',
        'nup_browse': 'Sirvi...',
        'nup_select_folder': 'Valige sihtkaust',
        'nup_create': 'Loo',
        'nup_start': 'N-Up alustamine...',
        'nup_progress': 'N-Up loomine...',
        'nup_success': 'N-Up loodud edukalt!\n\nSalvestatud kui:\n{0}\n\nKas soovite avada uue PDF-i?',
        'nup_complete': 'N-Up lõpetatud',
        'nup_cancel': 'N-Up tühistatud',
        'nup_error_format': 'Tõrge N-Up loomisel:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Muuda lehekülje suurust',
        'pagesize_menu': 'Muuda lehekülje suurust',
        'pagesize_info': 'Muudab PDF-i lehekülje suurust.\n\nSisu kohandatakse automaatselt uuele suurusele.',
        'pagesize_format': 'Formaat:',
        'pagesize_select': 'Valige standardformaat:',
        'pagesize_custom': 'Kohandatud suurus:',
        'pagesize_width': 'Laius:',
        'pagesize_height': 'Kõrgus:',
        'pagesize_orientation': 'Orientatsioon:',
        'pagesize_portrait': 'Portree',
        'pagesize_landscape': 'Maastik',
        'pagesize_scale_options': 'Skaaleerimise valikud:',
        'pagesize_fit': 'Kohanda (säilita kuvasuhe)',
        'pagesize_stretch': 'Venita (moonuta)',
        'pagesize_center': 'Keskele (algne suurus)',
        'pagesize_range': 'Lehekülgede vahemik:',
        'pagesize_all_pages': 'Kõik leheküljed',
        'pagesize_custom_range': 'Kohandatud vahemik',
        'pagesize_from': 'Alates:',
        'pagesize_to': 'Kuni:',
        'pagesize_target_folder': 'Sihtkaust:',
        'pagesize_browse': 'Sirvi...',
        'pagesize_select_folder': 'Valige sihtkaust',
        'pagesize_apply': 'Rakenda',
        'pagesize_start': 'Lehekülje suuruse muutmise alustamine...',
        'pagesize_progress': 'Lehekülje suuruse muutmine...',
        'pagesize_success': 'Lehekülje suurus muudetud edukalt!\n\nSalvestatud kui:\n{0}\n\nKas soovite avada uue PDF-i?',
        'pagesize_complete': 'Lehekülje suuruse muutmine lõpetatud',
        'pagesize_cancel': 'Lehekülje suuruse muutmine tühistatud',
        'pagesize_error_format': 'Tõrge lehekülje suuruse muutmisel:\n\n{0}',
        'pagesize_preview_info': 'Uus suurus: {0} x {1} pt',
        'filename_pagesize_suffix': '_uus_suurus',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-i teave',
        'pdf_info_menu': 'Näita PDF-i teavet',
        'pdf_info_voice': 'PDF-i teabe kuvamine',
        'pdf_info_error': 'Tõrge PDF-i teabe kuvamisel:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Näita klaviatuuri otseteid",
        "shortcuts_dialog_title": "Klaviatuuri otseteed",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FAIL</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Ava PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Sulge PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Salvesta kui...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Kaitse dokument</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Prindi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Prindi kohe (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Sulge rakendus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Ekspordi kui Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Ekspordi kui DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Ekspordi kui TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Ekspordi kui pildid (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Ekstraheerimine pildid</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENDI TÖÖTLUS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Mitu lehekülge)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konverteerimine (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Silu PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Pealekate PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimeeri PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDIGEERIMINE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Otsi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Lisa järjehoidja</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Halda järjehoidjaid</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Järgmine järjehoidja</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Eelmine järjehoidja</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Käivita OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 LEHEKÜLGEDE HALDUS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Pööra praegust lehekülge</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Pööra kõiki lehekülgi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normaliseeri praegune lehekülg</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normaliseeri kõik leheküljed</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Kustuta leheküljed</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ekstraheerimine leheküljed</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Sisesta leheküljed</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Liiguta leheküljed</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Liida PDF-id</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Muuda lehekülje suurust</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 SISESTAMINE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Sisesta tekst</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Sisesta rist</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Sisesta allkiri 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Sisesta allkiri 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Sisesta pilt</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Sisesta ristkülik</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Sisesta ellips</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Sisesta joon</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Sisesta nool</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Sisesta leheküljenumbrid</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Teksti vesimärk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Pildi vesimärk</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDIGEERIMISED</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redigeerimine (must)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redigeerimine (valge)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rakenda kõik redigeerimised</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ TÄIUSTATUD</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Kärbi PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Muuda metaandmeid</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VAADE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Lülita Tume/Hele režiim</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Näita tekstiakent</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Lehekülje laius (Suum)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Kaks lehekülge (Suum)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Ülevaade (Suum)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ SEADED</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Paroolihaldus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR seaded</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Allkirja seaded</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Failinimede vormindus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Ekspordi seaded</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Impordi seaded</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ TEAVE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Näita PDF-i teavet</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Lülita kõneväljund sisse/välja</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokusseeri menüüriba</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Uus versioon saadaval",
        "update_available_message": "Saadaval on uus versioon <b>{0}</b>.\n\nKülastage väljalaskelehte, et alla laadida uuendus:\n{1}",
        "update_available_voice": "Uus versioon {0} on saadaval. Palun laadige uuendus GitHubi lehelt alla.",
        "update_open_release": "Ava väljalaskeleht",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Laadi alla kõik tõlked",
        "ask_download_all_translations": """Lisaks saksa, inglise ja vietnami keelele on saadaval veel {total_languages} GUI-keelt.\n\nKas need tuleks esitada / uuendada?\n\nMärkus:\nMittevajalikud keeled saate hiljem kataloogist käsitsi kustutada:\n{translations_path}
        \nKui tühistate, saate GUI-keeled hiljem alla laadida menüüst 'Tööriistad → Uuenda tõlkeid'.""",
        "menu_update_translations": "Uuenda tõlkeid",
        "translations_updated": "Tõlked uuendatud",
        "translations_update_success": "{} tõlget uuendati edukalt ({} uut, {} uuendatud).",
        "translations_update_error": "Tõlgete uuendamisel tekkis viga",
        "translations_update_no_changes": "Kõik tõlked on juba ajakohased.",
        "translations_update_offline": "Internetiühendus puudub. Tõlkeid ei saanud uuendada.",
        "translations_update_in_progress": "Tõlkeid uuendatakse taustal...",
        "translations_downloading": "Laadin tõlkeid alla...",
        "translations_path_hint": "Kasutaja kataloog tõlgete jaoks",
        "translations_update_not_available_title": "Uuendus pole saadaval",
        "translations_update_not_available_message": """Tõlgete uuendamine on saadaval ainult installitud versioonis.\n\nArendusrežiimis on tõlked juba ajakohased.""",
        "translations_update_no_internet_title": "Internetiühendus puudub",
        "translations_update_no_internet_message": """Internetiühendust ei õnnestunud luua.\n\nTõlkeid ei saa GitHubist alla laadida.\n\nVõimalikud lahendused:
        • Kontrollige oma internetiühendust
        • Keelake ajutiselt võimalik tulemüür
        • Proovige hiljem uuesti
        \nTõlkeid saate ka käsitsi GitHubist alla laadida:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Uuendus on juba käimas",
        "btn_retry": "Proovi uuesti",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Tere tulemast PDF Dark View'i",
        "welcome_title_not_supported": "Tere tulemast PDF Dark View'i",
        "welcome_message": "Tere tulemast PDF Dark View'i!\n\nTeie süsteemikeel tuvastati kui '{language}'.\nKas soovite seda keelt kasutajaliidese jaoks kasutada?\n\nSaate keelt igal ajal muuta menüüst 'Seaded → Keel'.",
        "welcome_message_language_not_available": "Tere tulemast PDF Dark View'i!\n\nTeie süsteemikeel tuvastati kui '{language}'.\nSee keel pole veel installitud.\n\nKas soovite nüüd GitHubist alla laadida tõlked keelele {language}?\n\n(Keelt kasutatakse seejärel automaatselt kasutajaliideses.)",
        "welcome_message_language_not_supported": "Tere tulemast PDF Dark View'i!\n\nTeie süsteemikeel tuvastati kui '{language}'.\nKahjuks pole sellele keelele veel tõlkeid.\n\nKasutajaliides kuvatakse keeles {fallback_language}.\n\nSaate keelt igal ajal muuta menüüst 'Seaded → Keel'.\nKui soovite, võite ka ise oma keelele tõlke kaasa aidata:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Jah, kasuta süsteemikeelt",
        "welcome_keep_english": "Ei, jäta inglise keel",
        "welcome_download_language": "Jah, laadi alla {language}",

        # ============================================
        # 107. HILJUTI KASUTATUD RAJAD
        # ============================================

        'menu_recent': 'Hiljuti kasutatud',
        'menu_recent_dirs': 'Kataloogid...',
        'menu_recent_files': 'Failid...',
        'recent_manage': 'Halda...',
        'recent_enable_tracking': 'Salvesta hiljuti kasutatud rajad (privaatsus)',
        'recent_enable_info': 'Keela see valik, et mitte salvestada ühtegi rada',
        'recent_tracking_disabled': 'Rajajälgimine on keelatud',
        'recent_enabled': 'lubatud',
        'recent_disabled': 'keelatud',
        'recent_tracking_status': 'Rajajälgimine {0}',
        'recent_dialog_title': 'Hiljuti kasutatud rajad',
        'recent_tab_directories': 'Kataloogid',
        'recent_tab_files': 'Failid',
        'recent_dirs_instruction': 'Topeltklõpsake failidialoogi avamiseks kataloogis',
        'recent_files_instruction': 'Topeltklõpsake PDF-i otse avamiseks',
        'recent_no_directories': '(ühtegi kataloogi pole salvestatud)',
        'recent_no_files': '(ühtegi faili pole salvestatud)',
        'recent_default_current': '⭐ Vaikimisi: {0}',
        'recent_set_as_default': '⭐ Määra vaikimisi',
        'recent_default_set_title': 'Vaikimisi kataloog on määratud',
        'recent_default_set_message': 'Kataloog "{0}" on määratud PDF-ide avamise vaikekataloogiks.',
        'recent_default_set_voice': 'Vaikimisi kataloog on määratud',
        'recent_directory_not_found': 'Kataloogi ei leitud',
        'recent_file_not_found': 'Faili ei leitud',
        'recent_remove_selected': 'Eemalda',
        'recent_remove_title': 'Eemalda rada',
        'recent_remove_confirm': 'Kas soovite tõesti eemaldada loendist raja "{0}"?',
        'recent_path_removed': 'Rada on eemaldatud',
        'recent_clear_all': 'Eemalda kõik',
        'recent_clear_title': 'Eemalda kõik rajad',
        'recent_clear_confirm_type': 'Kas soovite tõesti kustutada kõik {0}?',
        'recent_cleared': 'Loend on tühjendatud',
        'recent_path_not_found_title': 'Rada ei leitud',
        'recent_path_not_found_message': 'Rada "{0}" enam ei eksisteeri.',
        'recent_open_file': 'Ava fail',
        'btn_open_recent': 'Ava',
        'recent_open_file_question': 'Kas soovite avada "{0}" PDF-ina?',
        'recent_not_pdf': 'Valitud fail ei ole PDF.',
        'recent_more_entries': 'Veel kirjeid...',
        'btn_remove': 'Eemalda',
        'btn_clear': 'Tühjenda kõik',
        'recent_context_open': 'Ava',
        'recent_context_reveal': 'Näita Finderis',
        'recent_context_set_default': '⭐ Määra vaikimisi',
        'recent_context_open_terminal': '💻 Ava terminal',
        'recent_context_file_info': 'Faili teave',
        'recent_context_open_with_default': '📄 Ava vaikerakendusega',
        'recent_context_remove': 'Eemalda loendist',
        'recent_context_clear_all': 'Eemalda kõik',
        'recent_file_info_title': 'Faili teave',
        'recent_file_info_name': 'Nimi',
        'recent_file_info_path': 'Rada',
        'recent_file_info_size': 'Suurus',
        'recent_file_info_modified': 'Muudetud',
        'recent_file_info_pages': 'Leheküljed',
        'recent_error_reveal': 'Viga Finderis avamisel',
        'recent_error_terminal': 'Viga terminali avamisel',
        'recent_error_info': 'Viga failiteabe hankimisel',
        'open_user_data_folder': 'Näita kasutaja andmekataloogi',

        # ============================================
        # 108. PAARIS/PAARITUTE LEHEKÜLGEDE KUSTUTAMINE
        # ============================================
        "pages_delete_even": "Kustuta kõik paaris leheküljed",
        "pages_delete_odd":  "Kustuta kõik paaritud leheküljed",
        "progress_even_pages": "Paaris lehekülgede kustutamine",
        "progress_odd_pages": "Paaritute lehekülgede kustutamine",
        "progress_mark_delete_even": "{} paaris lehekülge on märgitud kustutamiseks",
        "progress_mark_delete_odd":  "{} paaritut lehekülge on märgitud kustutamiseks",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programm sulgub",

    }
