
# ============================================
# translations_lt.py - Lietuvių kalbos žodynas (Littauisch)
# Vollständig sortiert nach Kategorien
# ============================================

def load_lithuanian_strings():
    """Lädt alle litauischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Atidaryti PDF",
        'btn_text_window': "OCR tekstas",
        'btn_first': "Pirmas puslapis",
        'btn_prev': "Ankstesnis puslapis",
        'btn_next': "Kitas puslapis",
        'btn_last': "Paskutinis puslapis",
        'btn_print': "Spausdinti",
        'btn_darkmode_light': "Šviesus režimas",
        'btn_darkmode_dark': "Tamsus režimas",
        'btn_delete_pages': "Ištrinti puslapius",
        'btn_extract_pages': "Išskirti puslapius",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "Gerai",
        'btn_cancel': "Atšaukti",
        'btn_save': "Išsaugoti",
        'btn_close': "Uždaryti",
        'btn_delete': "Ištrinti",
        'btn_delete_all': "Ištrinti viską",
        'btn_copy': "Kopijuoti",
        'btn_export': "Eksportuoti",
        'btn_show': "Rodyti slaptažodį",
        'btn_hide': "Slėpti slaptažodį",
        'btn_authenticate': "Autentifikuoti",
        'btn_settings': "Nustatymai",
        'btn_protect': "Apsaugoti",
        'btn_remove_password': "Pašalinti slaptažodį",
        'btn_manage': "Slaptažodžių valdymas",
        'btn_retry': "Bandyti dar kartą",
        'btn_select_all': "Pasirinkti viską",
        'btn_clear_selection': "Panaikinti pasirinkimą",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "{0} puslapis iš {1}",
        'page_count': "iš {0}",
        'goto_page': "Eiti į puslapį",
        'page_simple': "{0} puslapis",
        'full_view_page': "Visas vaizdas, {0} puslapis",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Įveskite paieškos žodį + Enter",
        'search_results': "Rezultatai: {0} iš {1}",
        'search_nav_hint': "Enter: kitas (Shift+Enter: ankstesnis) rezultatas",
        'search_no_results': "Nėra rezultatų",
        'search_error': "Paieškos klaida",
        'search_active': "Paieškos laukas aktyvuotas",
        'search_closed': "Paieška baigta",
        'search_position': "{0} puslapis {1}",
        'search_pos_top': "pačiame viršuje",
        'search_pos_upper': "viršuje",
        'search_pos_middle': "viduryje",
        'search_pos_lower': "apačioje",
        'search_pos_bottom': "pačioje apačioje",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Teksto atpažinimas sėkmingai baigtas!",
        'ocr_success_title': "OCR sėkmingas",
        'ocr_success_message': "Dokumentas dabar yra ieškomas.",
        'ocr_failed': "OCR nepavyko",
        'ocr_in_progress': "OCR vykdomas",
        'ocr_preparing': "Ruošiamas PDF...",
        'ocr_analyzing': "Analizuojamas PDF...",
        'ocr_optimizing': "Vaizdo optimizavimas...",
        'ocr_recognizing': "Teksto atpažinimas...",
        'ocr_embedding': "Teksto įterpimas...",
        'ocr_finalizing': "PDF baigiamas...",
        'ocr_not_available': "OCR neprieinamas",
        'ocr_install_message': "OCR įrankiai nerasti.\n\nĮdiekite:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Reikalingas OCR",
        'ocr_question': "PDF faile nėra ieškomo teksto.\nAr norite atlikti OCR, kad įjungtumėte {0}?",
        'ocr_perform': "Atlikti OCR",
        'ocr_later': "Vėliau",
        'ocr_starting': "Pradedamas garantuotas OCR...",
        'ocr_success_voice': "OCR sėkmingas. PDF dabar ieškomas.",
        'ocr_partial_success': "OCR atliktas, bet pakeičiant iškilo problemų.\n\nIeškoma versija išsaugota čia:\n{0}\n\nKlaida: {1}",
        'ocr_partial_title': "OCR iš dalies sėkmingas",
        'ocr_partial_voice': "OCR atliktas, bet pakeisti nepavyko.",
        'original_file': "Originalus failas:",
        'old_size': "Senas dydis:    {0} baitai",
        'new_size': "Naujas dydis: {0} baitai",
        'size_change': "Pokytis: {0}{1} baitai",
        'backup_created_file': "Atsarginė kopija sukurta:\n{0}",
        'backup_not_created': "Atsarginė kopija nesukurta (nustatymas išjungtas)",
        'page_header': "=== {0} puslapis ===\n{1}\n",
        'scanned_page_header': "=== {0} puslapis (nuskaitytas) ===\n[Šiame puslapyje yra tik nuskaitytas tekstas]\n[Atlikite OCR rankiniu būdu]\n",
        'scanned_warning': "⚠️ NUSKAITYTAS TEKSTAS - REIKALINGAS OCR",
        'guaranteed_title': "Sukurtas ieškomas PDF",
        'guaranteed_message': "<b>Sukurta garantuota ieškoma versija!</b>\n\nKadangi automatinis OCR nepavyko, buvo sukurtas alternatyvus ieškomas PDF:\n\n{0}\n\n<b>Šis failas turi:</b>\n• Išgautą tekstą (jei buvo)\n• Instrukcijas nuskaitytiems puslapiams\n• Yra visiškai ieškomas",
        'guaranteed_voice': "Sukurtas garantuotas ieškomas PDF.",
        'instruction_title': "OCR INSTRUKCIJA",
        'instruction_file': "Originalus failas: {0}",
        'instruction_text': "Automatinis teksto atpažinimas (OCR) nepavyko.\nAtlikite OCR rankiniu būdu:\n\n1. SU OCRmyPDF (komandų eilutė):\n   ocrmypdf --force-ocr \"[FAILAS]\" \"išvestis.pdf\"\n\n2. SU ADOBE ACROBAT (macOS/Windows):\n   • Atidarykite PDF programoje Acrobat\n   • Įrankiai > Redaguoti PDF\n   • Pasirinkite 'Teksto atpažinimas'\n\n3. SU PREVIEW (macOS):\n   • Atidarykite PDF programoje Preview\n   • Failas > Eksportuoti...\n   • Quartz filtras: 'Sumažinti failo dydį'\n   • Įjunkite 'Atlikti OCR'\n\n4. INTERNETINĖS OCR PASLAUGOS:\n   • smallpdf.com/lt/ocr-pdf\n   • ilovepdf.com/lt/ocr-pdf\n   • adobe.com/lt/acrobat/online/pdf-to-word.html",
        'instruction_created': "Sukurta OCR instrukcija",
        'instruction_created_message': "Išsami instrukcija sukurta:\n\n{0}\n\nAtlikite veiksmus rankiniam OCR.",
        'instruction_created_voice': "Sukurta OCR instrukcija.",
        'ocr_impossible': "OCR neįmanomas",
        'ocr_impossible_message': "OCR nepavyko atlikti.\n\nApdorokite '{0}' rankiniu būdu su OCR programine įranga.",
        'ocr_impossible_voice': "OCR neįmanomas. Apdorokite rankiniu būdu.",
        'emergency_title': "Avarinis OCR",
        'emergency_message': "Sukurtas avarinis PDF:\n\n{0}\n\nApdorokite šį failą rankiniu būdu su OCR.",
        'emergency_voice': "Sukurtas avarinis PDF. Atlikite OCR rankiniu būdu.",
        'critical_error': "Kritinė klaida",
        'critical_error_message': "OCR nepavyko paleisti.\n\nPaleiskite programą iš naujo ir patikrinkite OCR diegimą.",
        'critical_error_voice': "Kritinė OCR klaida",
        'ocr_question_html': "<p>PDF faile nėra ieškomo teksto.<p>Ar norite atlikti OCR, kad įjungtumėte <b>{0}</b>?</p>",
        'ocr_question_voice': "Reikalingas OCR. PDF faile nėra ieškomo teksto. Ar norite atlikti OCR, kad įjungtumėte {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "neįkeltas PDF",
        'no_pdf_message': "Nėra įkelto PDF",
        'pdf_not_found': "PDF failas nerastas",
        'file_size': "Failo dydis",
        'bytes': "baitai",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Atsarginė kopija sukurta",
        'backup_disabled': "Atsarginė kopija išjungta",
        'backup_activated': "Atsarginių kopijų kūrimas įjungtas",
        'backup_deactivated': "Atsarginių kopijų kūrimas išjungtas",
        'backup_status': "Atsarginė kopija: {0}",
        'backup_on': "✔ įjungta",
        'backup_off': "✘ išjungta",
        'close_pdf': "Uždaromas PDF: {0}",
        'pdf_not_found_format': "PDF failas nerastas: {0}",
        'error_pdf_load_format': "Klaida įkeliant PDF: {0}",
        'load_failed_format': "Įkelti nepavyko:\n{0}",
        'decrypted_suffix': "(iššifruotas)",
        'decryption_failed': "Iššifruoti nepavyko.",
        'decryption_error': "Klaida iššifruojant",
        'decryption_success': "Sėkmingai iššifruota",
        'decryption_success_message': "PDF iššifruotas ir išsaugotas čia:\n\n{0}",
        'decryption_success_voice': "PDF iššifruotas ir išsaugotas.",
        'password_remove_error': "Klaida šalinant slaptažodį",
        'save_unencrypted': "Išsaugoti nešifruotą PDF kaip",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Išsaugoti kaip...",
        'save_copy': "Išsaugoti kopiją",
        'save_success': "PDF išsaugotas čia: {0}",
        'save_encrypted': "Apsaugotas PDF išsaugotas čia: {0}",
        'save_error': "PDF nepavyko išsaugoti",
        'encryption_question': "Ar norite apsaugoti PDF slaptažodžiu?",
        'encryption_yes': "Taip",
        'encryption_no': "Ne",
        'encryption_cancel': "Atšaukti",
        'save_cancel': "Išsaugojimas atšauktas",
        'save_encrypted_voice': "Failas užšifruotas ir išsaugotas.",
        'save_success_voice': "PDF failas išsaugotas nešifruotas.",
        'save_error_format': "PDF nepavyko išsaugoti:\n{0}",
        'export_pages_success': "Eksportas į Pages sėkmingas",
        'export_pages_error': "Eksportas į Pages nepavyko",
        'export_pages_error_format': "Eksportas į Pages nepavyko: {0}",
        'export_word_success': "Eksportas į Word sėkmingas",
        'export_word_error': "Eksportas į Word nepavyko",
        'export_word_error_format': "Eksportas į Word nepavyko: {0}",
        'export_text_success': "Teksto eksportas sėkmingas",
        'export_text_error': "Teksto eksportas nepavyko",
        'export_text_error_format': "Teksto eksportas nepavyko: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Reikalingas slaptažodis",
        'password_enter': "Įveskite slaptažodį",
        'password_confirm': "Patvirtinkite slaptažodį",
        'password_new': "Naujas slaptažodis",
        'password_current': "Dabartinis slaptažodis",
        'password_save': "Išsaugoti slaptažodį (užšifruotą)",
        'password_saved': "✓ Šio failo slaptažodis išsaugotas",
        'password_wrong': "Neteisingas slaptažodis",
        'password_mismatch': "Slaptažodžiai nesutampa",
        'password_too_short': "Slaptažodis per trumpas",
        'password_min_length': "Slaptažodis turi būti bent 4 simbolių ilgio",
        'password_strength': "Slaptažodžio stiprumas",
        'password_strength_very_weak': "Labai silpnas",
        'password_strength_weak': "Silpnas",
        'password_strength_medium': "Vidutinis",
        'password_strength_strong': "Stiprus",
        'password_strength_very_strong': "Labai stiprus",
        'password_char_count': "({0} simboliai)",
        'password_match': "✓ Sutampa",
        'password_no_match': "✗ Slaptažodžiai nesutampa",
        'password_show': "Rodyti",
        'password_hide': "Slėpti",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Slaptažodžių valdymas",
        'password_table_filename': "Failo pavadinimas",
        'password_table_password': "Slaptažodis",
        'password_count': "{0} išsaugotų slaptažodžių",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Nėra išsaugotų slaptažodžių",
        'password_copied': "{0} slaptažodžiai nukopijuoti",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Ar tikrai norite ištrinti slaptažodį failui '{0}'?",
        'password_delete_multiple': "Ar tikrai norite ištrinti {0} pasirinktus slaptažodžius?",
        'password_delete_all_confirm': "Ar tikrai norite ištrinti visus {0} išsaugotus slaptažodžius?",
        'password_deleted': "{0} slaptažodžiai ištrinti",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Visi slaptažodžiai ištrinti",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Slaptažodžių generatorius",
        'generator_generated': "Sugeneruotas slaptažodis:",
        'generator_regenerate': "Generuoti iš naujo",
        'generator_copy': "Kopijuoti",
        'generator_use': "Naudoti",
        'generator_settings': "Nustatymai",
        'generator_length': "Ilgis:",
        'generator_group_every': "Skyriklis kas",
        'generator_group_chars': "simbolių.    Skyriklis:",
        'generator_uppercase': "Didžiosios raidės (A-Z)",
        'generator_lowercase': "Mažosios raidės (a-z)",
        'generator_digits': "Skaitmenys (0-9)",
        'generator_symbols': "Specialieji simboliai (!@#$%^&*)",
        'generator_exclude': "Neįtraukti:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Reikalingas pagrindinis slaptažodis",
        'master_password_setup': "Nustatyti pagrindinį slaptažodį",
        'master_password_change': "Keisti pagrindinį slaptažodį",
        'master_password_enter': "Įveskite savo pagrindinį slaptažodį",
        'master_password_choose': "Pasirinkite stiprų pagrindinį slaptažodį (bent 8 simboliai)",
        'master_password_new': "Įveskite savo naują pagrindinį slaptažodį",
        'master_password_confirm': "Patvirtinkite slaptažodį",
        'master_password_authenticate': "Autentifikuoti",
        'master_password_success': "Pagrindinis slaptažodis sėkmingai nustatytas.",
        'master_password_changed': "Pagrindinis slaptažodis sėkmingai pakeistas.",
        'master_password_removed': "Pagrindinis slaptažodis ir visi slaptažodžiai ištrinti.",
        'master_password_remove': "Pašalinti pagrindinį slaptažodį",
        'master_password_remove_confirm': "Ar tikrai esate TIKRAS, kad norite ištrinti VISUS slaptažodžius?\n\nŠis veiksmas yra NEGRĮŽTAMAS!",
        'master_password_export_before': "Ar norite prieš tai eksportuoti atsarginę kopiją?",
        'master_password_export_delete': "Eksportuoti ir ištrinti",
        'master_password_delete_now': "Ištrinti dabar",
        'master_password_for_signatures': "Norėdami naudoti parašus, turite nustatyti pagrindinį slaptažodį.\n\nAr norite dabar nustatyti pagrindinį slaptažodį?",
        'master_password_for_private': "Norėdami naudoti privačius teksto blokus, turite nustatyti pagrindinį slaptažodį.\n\nAr norite dabar nustatyti pagrindinį slaptažodį?",
        'master_password_info': """
            <b>🔐 BE PAGRINDINIO SLAPTAŽODŽIO:</b><br>
            • Neįmanoma rodyti, kopijuoti ir eksportuoti slaptažodžių<br>
            • Slaptažodžių trynimas visada galimas (net ir be pagrindinio slaptažodžio)<br><br>

            <b>🔐 SU PAGRINDINIU SLAPTAŽODŽIU:</b><br>
            • Visos funkcijos prieinamos po autentifikacijos<br>
            • Slaptažodžiai užšifruojami pagrindiniu slaptažodžiu<br>
            • Minimalus ilgis: 8 simboliai<br>
            • Saugus SHA-256 maišos saugojimas<br><br>

            <b>SVARBU:</b><br>
            • Pametus pagrindinį slaptažodį, slaptažodžiai nebeatkuriami<br>
            • Pašalinus pagrindinį slaptažodį, VISI slaptažodžiai ištrinami<br>
            • Prieš trynimą galima eksportuoti atsarginę kopiją<br>
            • Pagrindinį slaptažodį galima keisti bet kada
        """,
        'signature_auth_disabled': "Išjungti slaptažodžio klausimą parašams",
        'template_auth_disabled': "Išjungti slaptažodžio klausimą privatiems teksto blokams",
        'master_password_for_signatures_settings': "Norėdami naudoti parašus, turite nustatyti pagrindinį slaptažodį.\n\nEikite į Nustatymai - Slaptažodžių valdymas",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Apsaugoti PDF",
        'protect_info': "Failas '{0}' bus apsaugotas slaptažodžiu.",
        'protect_instruction': "Įveskite norimą slaptažodį du kartus, kad apsaugotumėte dokumentą, arba naudokite slaptažodžių generatorių, esantį dešinėje įvesties lauko pusėje.",
        'protect_success': "PDF sėkmingai apsaugotas ir išsaugotas čia:\n{0}\n\nSlaptažodis: {1}\n\nAr norite dabar atidaryti apsaugotą PDF?",
        'protect_open': "Taip",
        'protect_skip': "Ne",
        'protect_error': "Klaida apsaugant PDF",
        'protect_open_title': "atidaryti apsaugotą PDF",
        'protect_question': "Atlikta. Ar norite dabar atidaryti apsaugotą PDF? Taip ar Ne?",
        'password_cancel': "Slaptažodžio dialogas atšauktas",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Ištrinti puslapius",
        'pages_extract': "Išskirti puslapius",
        'pages_insert': "Įterpti puslapius",
        'pages_move': "Perkelti puslapius",
        'pages_delete_options': "Trynimo parinktys",
        'pages_delete_empty': "Ištrinti visus tuščius puslapius",
        'pages_delete_current': "Ištrinti dabartinį puslapį",
        'pages_delete_range': "Ištrinti puslapių intervalą",
        'pages_extract_options': "Išskyrimo parinktys",
        'pages_extract_current': "Išskirti dabartinį puslapį",
        'pages_extract_range': "Išskirti puslapių intervalą",
        'pages_insert_position': "Įterpimo vieta",
        'pages_insert_before': "Įterpti prieš puslapį:",
        'pages_insert_select': "Pasirinkti PDF",
        'pages_insert_none': "Nepasirinktas PDF",
        'pages_move_source': "Perkeliami puslapiai",
        'pages_move_from': "Nuo puslapio:",
        'pages_move_to': "Iki puslapio:",
        'pages_move_target': "Tikslinė vieta",
        'pages_move_before': "Perkelti prieš puslapį:",
        'pages_move_hint': "Pastaba: 1 puslapis = pradžia, {0} = pabaiga",
        'pages_range_invalid': "Pradžios puslapis turi būti mažesnis arba lygus pabaigos puslapiui.",
        'pages_position_invalid': "Tikslinė vieta negali būti perkeliamame intervale.",
        'pages_no_pdf_selected': "Nepasirinktas PDF.",
        'pages_deleted': "Ištrinta {0} puslapių.",
        'pages_extracted': "Išskirta: {0}\nIšsaugota čia: {1}\nFailo dydis: {2:.1f} KB",
        'pages_inserted': "Įterpta {0} puslapių",
        'pages_moved': "Perkelta {0} puslapių.",
        'pages_deleted_none': "Nė vienas puslapis neištrintas.",
        'pages_delete_progress': "Trinami puslapiai...",
        'pages_deleted_with_backup': "Ištrinta {0} puslapių.\n\nAtsarginė kopija: {1}",
        'pages_deleted_voice': "Sukurta atsarginė kopija ir ištrinta {0} puslapių.",
        'info': "Informacija",
        'error_dialog_creation': "Nepavyko sukurti dialogo",
        'extract_page_single': "Išskirti {0} puslapį",
        'extract_page_range': "Išskirti {0}-{1} puslapius",
        'extract_success_voice': "Puslapiai sėkmingai išskirti",
        'extract_error_format': "Klaida išskiriant: {0}",
        'pages_inserted_voice': "Įterpta {0} puslapių.",
        'insert_error_format': "Klaida įterpiant: {0}",
        'pages_move_progress': "Perkeliami puslapiai...",
        'pages_moved_with_backup': "Perkelta {0} puslapių.\n\nAtsarginė kopija: {1}",
        'move_success_title': "Sėkmingai perkelta",
        'pages_moved_voice': "{0} puslapiai sėkmingai perkelti",
        'mark_removed': "{0} puslapio žymė pašalinta",
        'mark_empty': "{0} puslapis pažymėtas kaip tuščias",
        'mark_export_removed': "{0} puslapio eksporto žymė pašalinta",
        'mark_export': "{0} puslapis pažymėtas eksportui",
        'no_empty_pages': "Nėra tuščių puslapių, pažymėtų trynimui",
        'delete_empty_confirm': "Ar norite ištrinti visus {0} pažymėtus tuščius puslapius?",
        'delete_empty_confirm_voice': "Ar dabar ištrinti visus {0} pažymėtus tuščius puslapius? Taip ar Ne.",
        'empty_pages_deleted': "{0} tuščių puslapių ištrinta",
        'no_export_pages': "Nėra puslapių, pažymėtų eksportui",
        'overwrite_title': "Perrašyti esamą failą",
        'overwrite_question': "Failas\n\n{0}\n\nyra egzistuoja.\nAr norite jį perrašyti?",
        'overwrite_voice': "Perrašyti esamą failą? Taip ar Ne.",
        'page_skipped': "{0} puslapis praleistas",
        'export_complete': "Eksportas baigtas.",
        'export_complete_voice': "Eksportas baigtas.",
        'no_pages_exported': "Nė vienas puslapis neeksportuotas",
        'export_cancelled': "Eksportas atšauktas",
        'pages_exported': "{0} puslapiai eksportuoti į {1}",
        'export_page_title': "Eksportuoti puslapį",
        'page_exported': "{0} puslapis eksportuotas į {1}",
        'export_error': "Klaida eksportuojant",
        'export_marked_title': "Eksportuoti pažymėtus puslapius",
        'rotate_all_title': "pasukti visus puslapius",
        'rotate_all_question': "Ar norite pasukti visus puslapius 90 laipsnių į dešinę?",
        'rotate_all_voice': "Ar norite pasukti visus puslapius 90 laipsnių į dešinę? Taip ar Ne?",
        'all_pages_rotated': "Visi puslapiai pasukti",
        'page_rotated': "{0} puslapis pasuktas",
        'rotate_error': "Puslapio pasukti nepavyko",
        'delete_page_confirm': "Ar norite ištrinti {0} puslapį?",
        'delete_page_confirm_voice': "Ar tikrai norite ištrinti {0} puslapį? Taip ar Ne.",
        'page_deleted': "{0} puslapis ištrintas",
        'delete_error': "Puslapio ištrinti nepavyko",
        'pages_deleted_voice': "{0} puslapiai ištrinti",
        'pages_exported_split': "{0} puslapiai sėkmingai eksportuoti.",
        'pages_skipped': "{0} puslapiai praleisti.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Išskirti puslapius (išplėstiniai)",
        'pdf_splitter_title': "PDF skaidytuvas ir išskyriklis",
        'pdf_splitter_load': " Pasirinkti PDF failą",
        'pdf_splitter_info': "Pasirinkite parinktį savo PDF dokumentui",
        'pdf_splitter_basic': "Pagrindinės operacijos",
        'pdf_splitter_single': "Padalinti į atskirus puslapius",
        'pdf_splitter_range': "Išskirti puslapius:",
        'pdf_splitter_range_placeholder': "pvz., 1-3,5,7-9",
        'pdf_splitter_clean': "Valymo operacijos",
        'pdf_splitter_remove_empty': "Pašalinti visus tuščius puslapius",
        'pdf_splitter_remove': "Ištrinti puslapių intervalą:",
        'pdf_splitter_remove_placeholder': "pvz., 2,4-6",
        'pdf_splitter_process': "Apdoroti PDF",
        'pdf_splitter_loaded': "PDF įkeltas. Pasirinkite parinktį",
        'pdf_read_error': "PDF nepavyko perskaityti",
        'pages': "Puslapiai",
        'pages_created': "Puslapiai sukurti",
        'range_empty': "Įveskite puslapių intervalą",
        'range_invalid': "Neteisingas puslapių intervalas",
        'range_created': "Sukurtas naujas PDF su pasirinktais puslapiais:\n{0}",
        'empty_removed': "{0} tuščių puslapių pašalinta.\nIšvestis: {1}",
        'remove_empty': "Įveskite puslapius, kuriuos norite pašalinti",
        'remove_invalid': "Neteisingi puslapiai šalinimui",
        'remove_done': "Sukurtas išvalytas PDF:\n{0}",
        'open_folder': "Atidaryti aplanką",
        'show_in_finder': "Rodyti Finder'yje",
        'pdf_splitter_no_pdf': "Pirmiausia įkelkite PDF failą.",
        'process_error': "Klaida apdorojant PDF",
        'pages_created_voice': "{0} puslapiai sukurti",
        'range_created_voice': "Sukurtas PDF su pasirinktais puslapiais",
        'empty_removed_voice': "{0} tuščių puslapių pašalinta",
        'remove_done_voice': "Sukurtas išvalytas PDF",
        'pdf_splitter_split_groups': "Kiekvieną ištisinę grupę į atskirą failą",
        'range_created_single': "Sukurtas naujas PDF:\n{0}",
        'range_created_multiple': "Sukurti {0} PDF failai.",
        'range_created_voice_single': "Sukurtas vienas PDF su pasirinktais puslapiais",
        'range_created_voice_multiple': "Sukurti {0} PDF failai",
        'empty_removed_none_left': "Nėra likusių puslapių",
        'empty_removed_all_empty': "Visi puslapiai atpažinti kaip tušti ir būtų pašalinti. Nebuvo sukurtas joks failas.",
        'preview_single': "Peržiūra: {0}",
        'preview_enter_range': "Įveskite puslapių intervalą.",
        'preview_invalid_range': "Neteisingas puslapių intervalas.",
        'preview_file': "Peržiūra: {0}",
        'preview_files': "Peržiūra: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Pradedamas spausdinimas",
        'print_sent': "Spausdinimo užduotis išsiųsta",
        'print_now': "Spausdinti dabar",
        'print_error': "Klaida momentiniame spausdinime",
        'print_limited': "Spausdinimo funkcija šioje sistemoje apribota",
        'print_error_format': "Klaida momentiniame spausdinime: {0}",
        'warning': "Įspėjimas",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Perjungti į šviesų režimą",
        'mode_switch_to_dark': "Perjungti į tamsų režimą",
        'mode_dark_activated': "Tamsus režimas aktyvuotas",
        'mode_light_activated': "Šviesus režimas aktyvuotas",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Visas vaizdas",
        'zoom_two_pages': "Du puslapiai greta",
        'zoom_overview': "Apžvalgos režimas",
        'zoom_cannot_during_search': "Mastelis nepasiekiamas paieškos metu",
        'zoom_exit_first': "Pirmiausia išeikite iš mastelio",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Vilk ir paleisk įjungtas",
        'drag_disabled': "Vilk ir paleisk išjungtas",
        'drag_page_grab': "{0} puslapis paimtas",
        'drag_page_dropped': "{0} puslapis įterptas į {1} vietą",
        'drag_position_invalid': "Neteisinga vieta",
        'drag_same_position': "{0} puslapis lieka {0} vietoje",
        'drag_error': "Klaida perkeliant",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Teksto įvedimas su išplėstiniu formatavimu ir teksto blokų valdymu",
        'text_templates': "Galimi teksto blokai:",
        'text_name': "Pavadinimas",
        'text_preview': "Teksto peržiūra",
        'text_enter': "Tekstas:",
        'text_font_size': "Šrifto dydis:",
        'text_formatting': "Formatavimas:",
        'text_bold': "Paryškintas",
        'text_italic': "Kursyvas",
        'text_underline': "Pabrauktas",
        'text_alignment': "Lygiuotė:",
        'text_left': "Kairėje",
        'text_center': "Centre",
        'text_right': "Dešinėje",
        'text_color': "Teksto spalva:",
        'text_opacity': "Nepermatomumas:",
        'text_word_wrap': "Žodžių kėlimas:",
        'text_auto': "Automatinis",
        'text_page_width_95': "Puslapio plotis (95%)",
        'text_page_width_85': "Labai platus (85%)",
        'text_page_width_75': "Plačiau (75%)",
        'text_page_width_60': "Platus (60%)",
        'text_page_width_50': "Vidutinis (50%)",
        'text_page_width_30': "Siauras (30%)",
        'text_page_width_20': "Siauresnis (20%)",
        'text_page_width_10': "Labai siauras (10%)",
        'text_no_wrap': "Be kėlimo",
        'text_private': "Privatus teksto blokas (reikalinga autentifikacija)",
        'text_preview_label': "Peržiūra:",
        'text_preview_placeholder': "Čia bus rodoma teksto peržiūra...",
        'text_no_text': "(Nėra teksto)",
        'text_save_template': "💾 Išsaugoti kaip bloką",
        'text_delete_template': "🗑 Ištrinti pasirinktą teksto bloką",
        'text_show_private': "Rodyti privačius",
        'text_hide_private': "Slėti privačius",
        'text_use': "✅ Naudoti tekstą",
        'text_saved': "Teksto blokas išsaugotas kaip:\n{0}",
        'text_saved_voice': "Teksto blokas išsaugotas",
        'text_deleted': "Teksto blokas ištrintas",
        'text_no_text_to_save': "Nėra teksto, kurį būtų galima išsaugoti.",
        'text_no_templates': "Nerasta teksto blokų",
        'text_private_master_required': "Privačius blokus galima naudoti tik tada, kai nustatytas pagrindinis slaptažodis.\n\nAr norite dabar nustatyti pagrindinį slaptažodį?",
        'text_filename': "Teksto bloko failo pavadinimas (be 'Text_' ir '.txt'):",
        'text_filename_hint': "Pavyzdys: 'Telefonas NamųBiuras' bus išsaugotas kaip 'Text_Telefonas NamųBiuras.txt'",
        'text_save_hint': "Teksto blokas bus automatiškai išsaugotas su formatavimu.",
        'text_guide_title': "Teksto įvedimas – Gidas",
        'text_delete_confirm': "Ar tikrai norite ištrinti teksto bloką?\n\nFailas: {0}\nTekstas: {1}...",
        'text_make_public': "Pažymėti kaip viešą",
        'text_make_private': "Pažymėti kaip privatų",
        'text_privacy_changed': "Privatumo būsena pakeista",
        'text_private_always': "Privatūs visada matomi (nustatymas)",
        'text_mode_required': "Pirmiausia įjunkite teksto režimą",
        'text_continue_editing': "Tęsti redagavimą – žymeklis teksto pabaigoje",
        'text_no_input': "Neįvestas tekstas – tekstas atmestas",
        'save_dialog_question': "Kaip norite tęsti?",
        'text_save_question': "Išsaugoti visus tekstus ir kryželius, koreguoti, tęsti redagavimą ar atmesti?",
        'copy_cross': "Kryželis nukopijuotas",
        'paste_cross': "Kryželis įterptas",
        'paste_text': "Tekstas įterptas",
        'cross_discarded': "Kryželis atmestas",
        'all_discarded': "Viskas atmesta",
        'text_discarded': "Tekstas atmestas",
        'no_texts_to_save': "Nėra tekstų, kuriuos būtų galima išsaugoti",
        'no_valid_texts': "Nėra tinkamų tekstų išsaugojimui",
        'text_word_singular': "tekstas",
        'text_word_plural': "tekstai",
        'cross_word_singular': "kryželis",
        'cross_word_plural': "kryželiai",
        'texts_saved_title': "Tekstai išsaugoti",
        'texts_crosses_saved': "{0} {1} ir {2} {3} įterpti į PDF.\n\nPDF perkrautas...",
        'texts_crosses_saved_voice': "{0} {1} ir {2} {3} išsaugota.",
        'texts_saved': "{0} {1} įterpti į PDF.\n\nPDF perkrautas...",
        'texts_saved_voice': "{0} {1} išsaugota.",
        'crosses_saved': "{0} {1} įterpti į PDF.\n\nPDF perkrautas...",
        'crosses_saved_voice': "{0} {1} išsaugota.",
        'elements_saved': "{0} elementai įterpti į PDF.\n\nPDF perkrautas...",
        'elements_saved_voice': "{0} elementai išsaugoti.",
        'text_window_load_error': "Teksto lango nepavyko įkelti",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Teksto įvedimas ir teksto blokai – Išsamus gidas**

        **1. Teksto įterpimas ir redagavimas**
        - Dešiniuoju pelės klavišu spustelėkite norimą vietą dokumente ir pasirinkite "Įterpti tekstą".
        - Atsidarys dialogas, kuriame galėsite įvesti ir formatuoti tekstą:
        • Šrifto dydis, paryškintas, kursyvas, pabrauktas
        • Teksto spalva (laisvai pasirenkama)
        • Permatomumas (nepermatomumas) slankikliu
        • Žodžių kėlimas (įvairūs pločiai, pvz., puslapio plotis, siauras, be kėlimo)
        - Patvirtinus tekstas atsiras spustelėjimo vietoje. Jį galite perkelti pele arba rodyklių klavišais.
        - Dukart spustelėjus tekstą atsidaro redagavimo režimas; ESC jį uždaro.

        **2. Teksto blokų (šablonų) valdymas**
        - Teksto dialogo kairėje pusėje matote visų išsaugotų teksto blokų sąrašą.
        - **Bloko išsaugojimas:** Įveskite tekstą, suformatuokite jį ir spustelėkite "💾 Išsaugoti kaip bloką". Įveskite failo pavadinimą (be plėtinio).
        - **Bloko įkėlimas:** Spustelėkite norimą pavadinimą sąraše. Tekstas ir formatavimas bus perkelti ir, jei reikia, gali būti koreguojami.
        - **Trynimas:** Dešiniuoju pelės klavišu spustelėkite bloką, kad jį ištrintumėte ar pakeistumėte jo privatumo būseną.

        **3. Privatūs teksto blokai (pagrindinis slaptažodis)**
        - Jei nustatėte pagrindinį slaptažodį (skiltyje Nustatymai → Slaptažodžių valdymas), galite pažymėti blokus kaip "privačius".
        - Prieš išsaugodami pažymėkite langelį "Privatus teksto blokas" dialoge.
        - Privatūs blokai sąraše rodomi tik tada, kai vieną kartą sesijos metu įvedėte savo pagrindinį slaptažodį (autentifikacija per spynos piktogramą arba pirmą kartą pasiekus).
        - Taip galite apsaugoti konfidencialius teksto blokus nuo neleistinos prieigos.

        **4. Kryželių įterpimas**
        - Kontekstiniame meniu taip pat galite įterpti grafinį kryželį (pvz., žymimiesiems langeliams).
        - Kryželių dydį, linijos storį ir spalvą galite globaliai koreguoti nustatymuose (meniu "Nustatymai" → "Kryželių nustatymai").
        - Dešiniuoju pelės klavišu spustelėkite esamą kryželį, kad jį individualiai pakeistumėte.

        **5. Grupinės operacijos**
        - Jei viename puslapyje įdėjote kelis tekstus ar kryželius, galite juos visus vienu metu išsaugoti arba atmesti iš kontekstinio meniu (dešinysis pelės klavišas teksto režime).
        - Išsaugant visi elementai įterpiami į PDF ir lieka kaip vektorinė grafika.

        **6. Spartieji klavišai teksto režime**
        - Rodyklių klavišai: elemento perkėlimas
        - Ctrl+rodyklių klavišai: didesni žingsniai
        - Enter: išsaugojimo dialogo atidarymas (išsaugoti viską / koreguoti / atmesti)
        - ESC: dabartinio elemento atmetimas
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Teksto įvedimas ir teksto blokai – Išsamus gidas</strong></p>

        <p><strong>1. Teksto įterpimas ir redagavimas</strong></p>
        <ul>
        <li>Dešiniuoju pelės klavišu spustelėkite norimą vietą dokumente ir pasirinkite "Įterpti tekstą".</li>
        <li>Atsidarys dialogas, kuriame galėsite įvesti ir formatuoti tekstą:<br/>
        • Šrifto dydis, paryškintas, kursyvas, pabrauktas<br/>
        • Teksto spalva (laisvai pasirenkama)<br/>
        • Permatomumas (nepermatomumas) slankikliu<br/>
        • Žodžių kėlimas (įvairūs pločiai, pvz., puslapio plotis, siauras, be kėlimo)</li>
        <li>Patvirtinus tekstas atsiras spustelėjimo vietoje. Jį galite perkelti pele arba rodyklių klavišais.</li>
        <li>Dukart spustelėjus tekstą atsidaro redagavimo režimas; ESC jį uždaro.</li>
        </ul>

        <p><strong>2. Teksto blokų (šablonų) valdymas</strong></p>
        <ul>
        <li>Teksto dialogo kairėje pusėje matote visų išsaugotų teksto blokų sąrašą.</li>
        <li><strong>Bloko išsaugojimas:</strong> Įveskite tekstą, suformatuokite jį ir spustelėkite "💾 Išsaugoti kaip bloką". Įveskite failo pavadinimą (be plėtinio).</li>
        <li><strong>Bloko įkėlimas:</strong> Spustelėkite norimą pavadinimą sąraše. Tekstas ir formatavimas bus perkelti ir, jei reikia, gali būti koreguojami.</li>
        <li><strong>Trynimas:</strong> Dešiniuoju pelės klavišu spustelėkite bloką, kad jį ištrintumėte ar pakeistumėte jo privatumo būseną.</li>
        </ul>

        <p><strong>3. Privatūs teksto blokai (pagrindinis slaptažodis)</strong></p>
        <ul>
        <li>Jei nustatėte pagrindinį slaptažodį (skiltyje Nustatymai → Slaptažodžių valdymas), galite pažymėti blokus kaip "privačius".</li>
        <li>Prieš išsaugodami pažymėkite langelį "Privatus teksto blokas" dialoge.</li>
        <li>Privatūs blokai sąraše rodomi tik tada, kai vieną kartą sesijos metu įvedėte savo pagrindinį slaptažodį (autentifikacija per spynos piktogramą arba pirmą kartą pasiekus).</li>
        <li>Taip galite apsaugoti konfidencialius teksto blokus nuo neleistinos prieigos.</li>
        </ul>

        <p><strong>4. Kryželių įterpimas</strong></p>
        <ul>
        <li>Kontekstiniame meniu taip pat galite įterpti grafinį kryželį (pvz., žymimiesiems langeliams).</li>
        <li>Kryželių dydį, linijos storį ir spalvą galite globaliai koreguoti nustatymuose (meniu "Nustatymai" → "Kryželių nustatymai").</li>
        <li>Dešiniuoju pelės klavišu spustelėkite esamą kryželį, kad jį individualiai pakeistumėte.</li>
        </ul>

        <p><strong>5. Grupinės operacijos</strong></p>
        <ul>
        <li>Jei viename puslapyje įdėjote kelis tekstus ar kryželius, galite juos visus vienu metu išsaugoti arba atmesti iš kontekstinio meniu (dešinysis pelės klavišas teksto režime).</li>
        <li>Išsaugant visi elementai įterpiami į PDF ir lieka kaip vektorinė grafika.</li>
        </ul>

        <p><strong>6. Spartieji klavišai teksto režime</strong></p>
        <ul>
        <li>Rodyklių klavišai: elemento perkėlimas</li>
        <li>Ctrl+rodyklių klavišai: didesni žingsniai</li>
        <li>Enter: išsaugojimo dialogo atidarymas (išsaugoti viską / koreguoti / atmesti)</li>
        <li>ESC: dabartinio elemento atmetimas</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Kryželių nustatymai",
        'cross_properties': "Kryželio savybės",
        'cross_size': "Dydis (px):",
        'cross_line_width': "Linijos storis:",
        'cross_color': "Spalva:",
        'cross_choose_color': "Pasirinkti",
        'cross_fine_tuning': "Smulkus derinimas išsaugant (pikseliai)",
        'cross_offset_x': "X poslinkis:",
        'cross_offset_y': "Y poslinkis:",
        'cross_offset_x_tooltip': "Neigiamos reikšmės perkelia kryželį į kairę, teigiamos – į dešinę",
        'cross_offset_y_tooltip': "Neigiamos reikšmės perkelia kryželį aukštyn, teigiamos – žemyn",
        'cross_preview': "Peržiūra",
        'cross_save': "Taikyti nustatymus",
        'cross_customized': "Kryželis pritaikytas",
        'cross_settings_applied': "Kryželių nustatymai išsaugoti.\nDydis: {0}px, linijos storis: {1}px\n{2}",
        'cross_updated_count': "{0} esami kryželiai atnaujinti.",
        'cross_no_crosses': "Nerasta jokių esamų kryželių.",
        'cross_settings_applied_all': "Kryželių nustatymai pritaikyti visiems {0} kryželiams",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Parašų nustatymai",
        'signature_1': "Parašas 1",
        'signature_2': "Parašas 2",
        'signature_select': "Pasirinkti parašą",
        'signature_add': "➕ Pridėti naują parašą...",
        'signature_size': "{0} parašo dydis (%):",
        'signature_common': "Bendrieji nustatymai",
        'signature_timestamp': "Automatiškai pridėti laiko žymą",
        'signature_location': "Numatytoji vieta:",
        'signature_timestamp_size': "Laiko žymos šrifto dydis:",
        'signature_no_files': "-- Nerasta parašų --",
        'signature_insert': "Įterpti parašą",
        'signature_insert_1': "Įterpti 1 parašą",
        'signature_insert_2': "Įterpti 2 parašą",
        'signature_customize': " Pritaikyti parašą",
        'signature_discard': " Atmesti šį parašą",
        'signature_save_all': " Išsaugoti visus parašus",
        'signature_discard_all': " Atmesti visus parašus",
        'signature_guide_title': "Parašai – Gidas",
        'signature_guide': """
📝 Parašai – Trumpas gidas

- Nustatykite pagrindinį slaptažodį
- Konfigūruokite parašus meniu Nustatymai
  (dydis, laiko žyma ...)
- Įterpkite su DEŠINIU PELĖS KLAVIŠU norimoje vietoje
  (pagrindinio slaptažodžio reikia vieną kartą per sesiją)
- Perkelkite parašą pele arba rodyklių klavišais
- Galima įterpti kelis parašus vieną po kito
- Kiekvieną parašą galima pritaikyti individualiai
- Atmesti atskirą parašą
- Išsaugoti / atmesti visus parašus vienu metu
- Taip pat galima naudoti meniu juostą.
        """,
        'signature_placeholder': "Peržiūra nepasiekiama",
        'signature_info': "{0} parašas: {1}×{2} px ({3}% nuo {4}×{5})",
        'signature_info_placeholder': "{0} parašo nustatymai",
        'signature_inserted': "{0} parašas įterptas į {1} puslapį",
        'signature_deleted': "Parašas ištrintas",
        'signature_copied': "Parašas nukopijuotas",
        'signature_pasted': "{0} parašas įterptas",
        'signature_saved': "{0} parašai įterpti į PDF.\n\nPDF perkrautas...",
        'signature_saved_voice': "{0} parašai išsaugoti",
        'mode_replace_signature_format': "Išeiti iš režimo ir įterpti {0} parašą",
        'mode_conflict_voice_signature': "{0} režimas aktyvus. Ar išeiti ir įterpti parašą?",
        'signature_not_configured': "{0} parašas nesukonfigūruotas",
        'signature_file_not_found': "Parašo failas nerastas",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nėra nukopijuoto parašo",
        'no_signatures_to_save': "Nėra parašų, kuriuos būtų galima išsaugoti",
        'signature_save_question': "Išsaugoti visus parašus, koreguoti ar atmesti šį?",
        'signatures_saved_title': "Parašai išsaugoti",
        'signatures_saved': "{0} parašai įterpti į PDF.\n\nPDF perkrautas...",
        'signatures_saved_voice': "{0} parašai išsaugoti.",
        'all_signatures_discarded': "Visi parašai atmesti",
        'signature_settings_saved': "Parašų nustatymai išsaugoti",
        'signature_cancelled': "Parašas atmestas",
        'signature_active_title': "Parašas aktyvus",
        'signature_replace_question': "Jau yra aktyvus parašas.\n\nAr norite pakeisti dabartinį parašą?",
        'signature_replace': "Pakeisti parašą",
        'signature_replace_voice': "Ar pakeisti dabartinį parašą ar atšaukti?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Vaizdų nustatymai",
        'image_common': "Bendrieji vaizdų nustatymai",
        'image_keep_aspect': "Išlaikyti kraštinių santykį tempiant",
        'image_default_size': "Numatytasis dydis (%):",
        'image_dark_invert': "Invertuoti vaizdus tamsiame režime",
        'image_dark_invert_tooltip': "Įjungta: vaizdai invertuojami geresniam matomumui",
        'image_fine_tuning': "Smulkus derinimas (pikseliai)",
        'image_offset_x': "X poslinkis:",
        'image_offset_y': "Y poslinkis:",
        'image_offset_x_tooltip': "Neigiamos reikšmės perkelia vaizdą į kairę, teigiamos – į dešinę",
        'image_offset_y_tooltip': "Neigiamos reikšmės perkelia vaizdą aukštyn, teigiamos – žemyn",
        'image_select': "Pasirinkti vaizdą",
        'image_insert': "Įterpti vaizdą",
        'image_customize': " Pritaikyti vaizdą",
        'image_aspect': " Išlaikyti kraštinių santykį",
        'image_discard': " Atmesti šį vaizdą",
        'image_save_all': " Išsaugoti visus vaizdus",
        'image_discard_all': " Atmesti visus vaizdus",
        'image_filter': "Vaizdai",
        'image_guide_title': "Vaizdų įterpimas – Gidas",
        'image_guide': """
📷 Vaizdų įterpimas į PDF – Trumpas gidas:

1. Dešiniuoju pelės klavišu spustelėkite norimą vietą
2. "Įterpti vaizdą" → pasirinkite vaizdą
3. Padėkite vaizdą: tempkite pele
4. Koreguokite dydį: tempkite už kampų/kraštų
5. Išlaikyti kraštinių santykį: klavišas [A]
6. Papildomi koregavimai: dešiniuoju pelės klavišu ant vaizdo

Patarimas: Kontekstiniame meniu galite keisti nustatymus.
        """,
        'image_inserted': "Vaizdas įterptas į {1} puslapį",
        'image_deleted': "Vaizdas atmestas",
        'image_copied': "Vaizdas nukopijuotas",
        'image_pasted': "Vaizdas įterptas",
        'image_saved': "{0} vaizdai įterpti į PDF.\n\nPDF perkrautas...",
        'image_saved_voice': "{0} vaizdai išsaugoti",
        'image_aspect_on': "įjungta",
        'image_aspect_off': "išjungta",
        'image_aspect_toggle': "Išlaikyti kraštinių santykį {0}",
        'image_reset': "Vaizdas grąžintas į pradinį dydį",
        'image_replaced': "Vaizdas pakeistas",
        'image_invalid': "Neteisingas vaizdas",
        'mode_replace_image': "Įterpti vaizdą",
        'mode_conflict_voice_image': "{0} režimas aktyvus. Ar išeiti ir įterpti vaizdą?",
        'image_active_title': "Vaizdas aktyvus",
        'image_replace_question': "Jau yra aktyvus vaizdas.\n\nAr norite pakeisti dabartinį vaizdą?",
        'image_replace': "Pakeisti vaizdą",
        'image_replace_voice': "Ar pakeisti dabartinį vaizdą ar atšaukti?",
        'image_filter_all': "Vaizdai (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Visi failai (*.*)",
        'no_copied_image': "Nėra nukopijuoto vaizdo",
        'image_discarded': "Vaizdas atmestas",
        'image_save_question': "Išsaugoti visus vaizdus, koreguoti ar atmesti šį?",
        'no_images_to_save': "Nėra vaizdų, kuriuos būtų galima išsaugoti",
        'no_valid_images': "Nėra tinkamų vaizdų išsaugojimui",
        'images_saved_title': "Vaizdai išsaugoti",
        'images_saved': "{0} vaizdai įterpti į PDF.\n\nPDF perkrautas...",
        'images_saved_voice': "{0} vaizdai išsaugoti.",
        'all_images_discarded': "Visi vaizdai atmesti",
        'image_settings_updated': "Vaizdų nustatymai atnaujinti",
        'image_replace_title': "Pasirinkti naują vaizdą",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Formų nustatymai",
        'form_basic': "Pagrindiniai nustatymai",
        'form_default_type': "Numatytasis formos tipas:",
        'form_rectangle': "Stačiakampis",
        'form_ellipse': "Elipsė",
        'form_line': "Linija",
        'form_arrow': "Rodyklė",
        'form_line_width': "Linijos storis:",
        'form_colors': "Spalvos",
        'form_line_color': "Linijos spalva:",
        'form_fill_color': "Užpildo spalva:",
        'form_choose_color': "Pasirinkti",
        'form_transparent': "Skaidrus fonas (tik linija)",
        'form_filled': "užpildyta",
        'form_dark_mode': "Tamsus režimas",
        'form_dark_invert': "Invertuoti spalvas tamsiame režime",
        'form_fine_tuning': "Smulkus derinimas (pikseliai)",
        'form_offset_x': "X poslinkis:",
        'form_offset_y': "Y poslinkis:",
        'form_offset_x_tooltip': "Neigiamos reikšmės perkelia formą į kairę, teigiamos – į dešinę",
        'form_offset_y_tooltip': "Neigiamos reikšmės perkelia formą aukštyn, teigiamos – žemyn",
        'form_preview': "Peržiūra",
        'form_insert': "Įterpti formą",
        'form_rectangle_insert': "Stačiakampis",
        'form_ellipse_insert': "Elipsė/apskritimas",
        'form_line_insert': "Linija (2 spustelėjimai)",
        'form_arrow_insert': "Rodyklė (2 spustelėjimai)",
        'form_customize': " Pritaikyti formą",
        'form_transparent_toggle': " Skaidrus fonas",
        'form_discard': " Atmesti šią formą",
        'form_save_all': " Išsaugoti visas formas",
        'form_discard_all': " Atmesti visas formas",
        'form_guide_title': "Formų įterpimas – Gidas",
        'form_guide': """
📐 Formų įterpimas į PDF – Trumpas gidas:

1. Pasirinkite formos tipą (stačiakampis, elipsė, linija, rodyklė)
2. Spustelėkite vietą
   - Stačiakampis/elipsė: vienas spustelėjimas įdeda formą
   - Linija/rodyklė: du spustelėjimai pradžios ir pabaigos taškams
3. Padėkite formą: tempkite pele
4. Koreguokite dydį: tempkite už kampų/kraštų
5. Išsaugoti formą: Enter
6. Atmesti formą: ESC
7. Papildomi koregavimai: dešiniuoju pelės klavišu ant formos

Patarimas: Kontekstiniame meniu galite keisti nustatymus.
        """,
        'form_inserted': "{0} įterptas į {1} puslapį",
        'form_deleted': "Forma ištrinta",
        'form_copied': "Forma nukopijuota",
        'form_pasted': "Forma įterpta",
        'form_saved': "{0} formos įterptos į PDF.\n\nPDF perkrautas...",
        'form_saved_voice': "{0} formos išsaugotos",
        'form_reset': "Forma grąžinta į numatytąjį dydį",
        'form_transparent_on': "įjungta",
        'form_transparent_off': "išjungta",
        'form_transparent_toggled': "Skaidrus fonas {0}",
        'form_line_cancel': "Linijos piešimas atšauktas",
        'form_second_click': "Dabar spustelėkite {0} pabaigos tašką",
        'mode_replace_form': "Įterpti formą",
        'mode_conflict_voice_form': "{0} režimas aktyvus. Ar išeiti ir įterpti formą?",
        'form_settings_updated': "Formų nustatymai atnaujinti",
        'form_unknown': "Forma",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Spustelėkite pradžios tašką",
        'form_line_guide_2': "2. Spustelėkite pabaigos tašką",
        'form_line_guide_3': "Linija bus nubrėžta tarp dviejų taškų.",
        'form_line_status_1': "Laukiama pirmo spustelėjimo...",
        'form_line_status_2': "Pirmas taškas nustatytas: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Dabar spustelėkite pabaigos tašką...",
        'form_line_status_4': "Abu taškai nustatyti.\nSpustelėkite 'Baigti', kad išsaugotumėte.",
        'form_line_reset': "Atstatyti",
        'form_line_finish': "Baigti",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopijuoti (Cmd+C)",
        'paste': "Įklijuoti (Cmd+V)",
        'copied': "Nukopijuota: {0}",
        'no_element_to_copy': "Nėra pasirinkto elemento kopijavimui",
        'no_copied_data': "Nėra nukopijuotų duomenų",
        'no_valid_position': "Nėra tinkamos vietos įklijavimui",
        'copy_text': "Tekstas nukopijuotas",
        'copy_image': "Vaizdas nukopijuotas",
        'copy_form': "Forma nukopijuota",
        'copy_signature': "Parašas nukopijuotas",
        'element_text': "Tekstas",
        'element_image': "Vaizdas",
        'element_form': "Forma",
        'element_signature': "Parašas",
        'element_unknown': "Elementas",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Režimų konfliktas",
        'mode_conflict_message': "Režimas '{0}' jau aktyvus.\n\nAr norite iš jo išeiti ir {1}?",
        'mode_replace': "Išeiti iš režimo ir {0}",
        'mode_cancel': "Atšaukti",
        'mode_replace_text': "įterpti tekstą",
        'mode_replace_cross': "įterpti kryželį",
        'mode_replace_signature': "įterpti parašą",
        'mode_replace_image': "įterpti vaizdą",
        'mode_replace_form': "įterpti formą",
        'mode_conflict_voice': "{0} režimas aktyvus. Ar išeiti ir įterpti tekstą?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Teksto įvedimas",
        'active_mode_signature': "Parašas",
        'active_mode_image': "Vaizdas",
        'active_mode_form': "Forma",
        'active_mode_and': " ir ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Įterpti",
        'insert_another_text': "Įterpti tekstą",
        'insert_another_cross': "Įterpti kryželį",
        'insert_another_signature_1': "1 parašas",
        'insert_another_signature_2': "2 parašas",
        'insert_another_image': "Įterpti vaizdą",
        'insert_another_form_rect': "Stačiakampis",
        'insert_another_form_ellipse': "Elipsė",
        'insert_another_form_line': "Linija (2 spustelėjimai)",
        'insert_another_form_arrow': "Rodyklė (2 spustelėjimai)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Išsaugoti {0}",
        'save_dialog_message': "{0} bus išsaugotas {1} puslapyje.\n\nKaip norite tęsti?",
        'save_all': "Išsaugoti visus {0}",
        'save_single': "Išsaugoti {0}",
        'save_customize': "Koreguoti {0}",
        'save_discard': "Atmesti šį {0}",
        'save_continue': "Tęsti redagavimą",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Eiti į {0} puslapį",
        'context_rotate': " Pasukti {0} puslapį",
        'context_delete': " Ištrinti {0} puslapį",
        'context_export': " Eksportuoti {0} puslapį",
        'context_mark_as': " Pažymėti puslapį kaip...",
        'context_mark_empty': " Tuščias puslapis",
        'context_unmark_empty': " Nebėra tuščias",
        'context_mark_export': " Pažymėti eksportui",
        'context_unmark_export': " Nebe eksportuoti",
        'context_batch_actions': " Grupinės operacijos",
        'context_batch_delete_empty': " Ištrinti visus {0} tuščius puslapius",
        'context_batch_export_single': " Eksportuoti visus {0} puslapius (vienas failas)",
        'context_batch_export_split': " Eksportuoti visus {0} puslapius (atskirai)",
        'context_drag_start': " Pradėti vilkimą",
        'context_drag_stop': " Baigti vilkimą",
        'context_insert': " Įterpti",
        'context_insert_pages': " Įterpti puslapius",
        'context_zoom': "Mastelis",
        'discard_mixed': "Atmesti visus {0} {1} ir {2} {3}",
        'save_mixed': "Išsaugoti {0} {1} ir {2} {3}",
        'discard_texts': "Atmesti visus {0} tekstus",
        'discard_text_single': "Atmesti 1 tekstą",
        'save_texts': "Išsaugoti {0} tekstus",
        'save_text_single': "Išsaugoti 1 tekstą",
        'discard_crosses': "Atmesti visus {0} kryželius",
        'discard_cross_single': "Atmesti 1 kryželį",
        'save_crosses': "Išsaugoti {0} kryželius",
        'save_cross_single': "Išsaugoti 1 kryželį",
        'discard_signatures': "Atmesti visus {0} parašus",
        'save_signature_single': "Išsaugoti 1 parašą",
        'save_signatures': "Išsaugoti {0} parašus",
        'discard_images': "Atmesti visus {0} vaizdus",
        'save_image_single': "Išsaugoti 1 vaizdą",
        'save_images': "Išsaugoti {0} vaizdus",
        'discard_forms': "Atmesti visas {0} formas",
        'save_form_single': "Išsaugoti 1 formą",
        'save_forms': "Išsaugoti {0} formas",
        'cross_discard': "Atmesti šį kryželį",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Eksportavimo / importavimo informacija",
        'export_what': "📋 Kas eksportuojama?",
        'export_general': "Bendrieji nustatymai",
        'export_general_items': "• Balso išvestis (įjungta/išjungta, greitis)\n• Tamsus/šviesus režimas\n• Atsarginių kopijų nustatymai\n• OCR nustatymai",
        'export_image_form': "Vaizdų ir formų nustatymai",
        'export_image_form_items': "• Vaizdų nustatymai (kraštinių santykis, numatytasis dydis)\n• Formų nustatymai (linijos storis, spalvos)\n• Parašų nustatymai (keliai, dydžiai, laiko žyma)",
        'export_passwords': "Slaptažodžių duomenų bazė",
        'export_passwords_items': "• Visi išsaugoti PDF slaptažodžiai\n• Pasirinktinai užšifruoti arba iššifruoti",
        'export_master': "Pagrindinio slaptažodžio nustatymai",
        'export_master_items': "• Pagrindinio slaptažodžio maiša\n• Parašų/teksto blokų nustatymai",
        'export_signatures': "Parašai ir teksto blokai",
        'export_signatures_items': "• Visi vaizdų failai (parašai)\n• Visi teksto blokai su formatavimu\n• Privatūs/vieši žymėjimai",
        'export_import_warning': "⚠️ Svarbios pastabos",
        'export_import_note': "• Importuojant VISI dabartiniai nustatymai bus perrašyti\n• Būtinas programos paleidimas iš naujo\n• Esami parašai/teksto blokai bus pakeisti",
        'export_master_note': "• Jei nustatytas pagrindinis slaptažodis, galite pasirinkti:\n  - Iššifruoti (slaptažodžiai aiškiu tekstu)\n  - Užšifruoti (skaitomi tik su pagrindiniu slaptažodžiu)",
        'export_security': "• Eksportuotas ZIP failas turi konfidencialių duomenų\n• Laikykite jį saugiai (pvz., užšifruotame USB laikmenyje)\n• Pametus failą, slaptažodžiai negrįžtamai prarandami",
        'export_format': "📁 Eksportavimo formatas",
        'export_format_desc': "Nustatymai išsaugomi viename ZIP faile:",
        'export_filename': "PDFDarkView_Nustatymai_MMMMMMDD_HHMMSS.zip",
        'export_success': "Nustatymai sėkmingai eksportuoti",
        'export_failed': "Eksportuoti nepavyko",
        'export_import_question': "Ar norite dabar paleisti programą iš naujo?",
        'export_password_question': "Nustatytas pagrindinis slaptažodis.\n\nAr norite eksportuoti slaptažodžius iššifruotus?\n(kitaip jie bus eksportuoti užšifruoti)",
        'export_decrypt': "Eksportuoti iššifruotus",
        'export_encrypt': "Eksportuoti užšifruotus",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informacija",
        'info_title': "Apie PDF Dark View",
        'info_version': "Versija",
        'info_author': "Sukūrė Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Apie",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> yra prieinama PDF peržiūros programa, specialiai sukurta žmonėms su regos negalia.</p>

            <p><strong>Pagrindiniai bruožai:</strong></p>
            <ul>
                <li>Kontrastinga, pritaikoma sąsaja</li>
                <li>Visapusiškas valdymas klaviatūra</li>
                <li>Integruota balso sintezė</li>
                <li>OCR nuskaitytiems dokumentams</li>
                <li>Išsamūs redagavimo įrankiai</li>
            </ul>

            <p>Palaikoma daugiau nei 50 kalbų – kad PDF failai būtų prieinami visiems.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkcijos",
        'info_features_intro': "PDF Dark View suteikia jums šias galimybes:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Peržiūra ir navigacija</strong> – Tamsus/Šviesus režimas, puslapių vartymas, mastelis, peršokimas į puslapį</li>
            <li><strong>OCR (teksto atpažinimas)</strong> – Padarykite nuskaitytus dokumentus ieškomus ir kopijuojamus</li>
            <li><strong>Redagavimas</strong> – Tekstų, kryžių, parašų, vaizdų ir formų įterpimas</li>
            <li><strong>Puslapių valdymas</strong> – Trynimas, ištraukimas, įterpimas, perkėlimas vilkimu</li>
            <li><strong>Eksportas</strong> – Į Word, Pages arba kaip tekstą</li>
            <li><strong>Saugumas</strong> – Slaptažodžio apsauga ir valdymas</li>
            <li><strong>Prieinamumas</strong> – Balso sintezė, valdymas klaviatūra, didelis kontrastas</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Naudojimas",
        'info_accessibility': "♿ Prieinamumas – visapusiškas valdymas klaviatūra",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Bendra</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Atidaryti PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Ieškoti</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Perjungti tamsų/šviesų režimą</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Spausdinti</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Baigti</div>

        <div class="shortcut-cat">📖 Navigacija</div>
        <div class="shortcut-row"><kbd>Rodyklių klavišai</kbd> Vartyti puslapį po puslapio</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Eiti į puslapį</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Pirmas puslapis</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Paskutinis puslapis</div>

        <div class="shortcut-cat">✏️ Redagavimas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Įterpti tekstą</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Ištrinti puslapius</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Ištraukti puslapius</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Įterpti puslapius</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Perkelti puslapius</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Pasukti puslapį</div>

        <div class="shortcut-cat">🖼️ Elementų perkėlimas</div>
        <div class="shortcut-row"><kbd>Rodyklių klavišai</kbd> Perkelti tekstą/vaizdą/parašą</div>
        <div class="shortcut-row"><kbd>Ctrl+Rodyklių klavišai</kbd> Didesni žingsniai</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Išsaugoti</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Atmesti</div>

        <div class="shortcut-cat">🗣️ Balso sintezė</div>
        <div class="shortcut-row"><kbd>F2</kbd> Įjungti/išjungti balso sintezę</div>
        """,
        'info_contextmenu': "📌 Svarbu: Visas funkcijas taip pat galima pasiekti per kontekstinį meniu (dešinysis pelės mygtukas)!",
        'info_accessibility_hint': "💡 Patarimas: Balso sintezė (F2) palengvina orientaciją ir pateikia grįžtamąjį ryšį apie meniu ir dialogus.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licencija & Impresumas",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUMAS</strong><br>
        Informacija pagal § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Vokietija<br>
        El. paštas: binhdiez64@gmail.com<br>
        Atsakingas už turinį: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Atsakomybės apribojimas</strong><br>
        Programinė įranga buvo sukurta su didžiausiu kruopštumu. Nėra garantijos dėl tikslumo, išsamumo ir funkcionalumo. Naudojimas vyksta jūsų pačių rizika.<br><br>

        <strong>📄 MIT licencija (privatus naudojimas)</strong><br>
        Autorių teisės (c) 2026 Toralf Schulz (BinhDiez)<br>
        Leidžiama: nemokamas naudojimas, privatūs pakeitimai, asmeninės kopijos.<br>
        Neleidžiama: pardavimas, komercinis naudojimas, autorių teisių pranešimų pašalinimas.<br><br>

        <strong>🔧 Trečiųjų šalių komponentai</strong><br>
        Šioje programinėje įrangoje yra komponentų pagal GPL, AGPL, Apache 2.0, BSD ir MIT licencijas.<br>
        Perplatinant toliau, reikia laikytis atitinkamų licencijos sąlygų.<br><br>

        <strong>🌐 Atvirasis kodas</strong><br>
        Šaltinio kodas yra prieinamas ir gali būti peržiūrimas, keičiamas ir platinamas toliau pagal atitinkamas licencijos sąlygas.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Padėkos",
        'info_credits': "Dėkojame atvirojo kodo bendruomenei",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF apdorojimas</li>
            <li><strong>PyQt5</strong> – Grafinė sąsaja</li>
            <li><strong>Tesseract OCR</strong> – Teksto atpažinimas</li>
            <li><strong>OCRmyPDF</strong> – OCR integracija</li>
            <li><strong>python-docx</strong> – Eksportas į Word</li>
            <li><strong>qtawesome</strong> – Piktogramos</li>
            <li><strong>DeepSeek</strong> – Pagalba verčiant (50+ kalbų)</li>
            <li><strong>Visiems vartotojams</strong> – Už vertingą atsiliepimą</li>
            <li><strong>Atvirojo kodo bendruomenei</strong> – Už puikias bibliotekas</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Kalbos",
        'info_languages_header': "🌍 Kalbų palaikymas",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View šiuo metu palaiko <strong>62 kalbas</strong> – kad programinė įranga būtų prieinama visame pasaulyje.</p>

            <p><strong>📖 Visas kalbų sąrašas (2026 m. kovo mėn. duomenimis):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikanų</li>
                    <li>🇦🇱 Albanų (Shqip)</li>
                    <li>🇩🇿 Arabų (العربية)</li>
                    <li>🇮🇩 Baliečių (Basa Bali)</li>
                    <li>🇧🇩 Bengalų (বাংলা)</li>
                    <li>🇲🇲 Birmiečių (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnių (Bosanski)</li>
                    <li>🇧🇬 Bulgarų (Български)</li>
                    <li>🇨🇳 Kinų (中文)</li>
                    <li>🇩🇰 Danų (Dansk)</li>
                    <li>🇩🇪 Vokiečių (Deutsch)</li>
                    <li>🇬🇧 Anglų (English)</li>
                    <li>🇪🇪 Estų (Eesti)</li>
                    <li>🇫🇮 Suomių (Suomi)</li>
                    <li>🇫🇷 Prancūzų (Français)</li>
                    <li>🇬🇷 Graikų (Ελληνικά)</li>
                    <li>🇮🇱 Hebrajų (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatų (Hrvatski)</li>
                    <li>🇭🇺 Vengrų (Magyar)</li>
                    <li>🇮🇩 Indoneziečių (Bahasa Indonesia)</li>
                    <li>🇮🇪 Airių (Gaeilge)</li>
                    <li>🇮🇸 Islandų (Íslenska)</li>
                    <li>🇮🇹 Italų (Italiano)</li>
                    <li>🇯🇵 Japonų (日本語)</li>
                    <li>🇰🇭 Khmerų (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korėjiečių (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvių (Latviešu)</li>
                    <li>🇱🇹 Lietuvių (Lietuvių)</li>
                    <li>🇱🇺 Liuksemburgiečių (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajiečių (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathų (मराठी)</li>
                    <li>🇲🇳 Mongolų (Монгол)</li>
                    <li>🇳🇵 Nepalų (नेपाली)</li>
                    <li>🇳🇱 Olandų (Nederlands)</li>
                    <li>🇳🇴 Norvegų (Norsk)</li>
                    <li>🇦🇫 Puštūnų (پښتو)</li>
                    <li>🇮🇷 Persų (فارسی)</li>
                    <li>🇵🇱 Lenkų (Polski)</li>
                    <li>🇵🇹 Portugalų (Português)</li>
                    <li>🇮🇳 Pandžabų (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumunų (Română)</li>
                    <li>🇷🇺 Rusų (Русский)</li>
                    <li>🇸🇪 Švedų (Svenska)</li>
                    <li>🇷🇸 Serbų (Српски)</li>
                    <li>🇸🇰 Slovakų (Slovenčina)</li>
                    <li>🇸🇮 Slovėnų (Slovenščina)</li>
                    <li>🇪🇸 Ispanų (Español)</li>
                    <li>🇹🇿 Svahilių (Kiswahili)</li>
                    <li>🇵🇭 Tagalogų (Filipino)</li>
                    <li>🇮🇳 Tamilų (தமிழ்)</li>
                    <li>🇮🇳 Telugų (తెలుగు)</li>
                    <li>🇹🇭 Tajų (ไทย)</li>
                    <li>🇨🇿 Čekų (Čeština)</li>
                    <li>🇹🇷 Turkų (Türkçe)</li>
                    <li>🇺🇦 Ukrainiečių (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamiečių (Tiếng Việt)</li>
                    <li>🇸🇳 Volofų (Wolof)</li>
                    <li>🇺🇸 Jidiš (ייִדיש)</li>
                    <li>🇿🇦 Zulų (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Pridėkite savo kalbas:</strong><br>
                Norite kalbos, kuri dar nėra įtraukta? Tiesiog įdėkite savo žodyno failą (<code>sprache_xx.py</code>) šalia programos – programinė įranga jį atpažins automatiškai. Jei domitės konkrečiu vertimu, drąsiai susisiekite su manimi.
            </div>

            <p><strong>🙏 Ypatingas ačiū:</strong> DeepSeek už pagalbą verčiant visus žodynus į 62 kalbas.</p>

            <p>📧 Kontaktai vertimams: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Klaida",
        'error_occurred': "Įvyko klaida",
        'error_pdf_load': "Klaida įkeliant PDF",
        'error_pdf_save': "Klaida išsaugant PDF",
        'error_ocr': "Klaida atpažįstant tekstą",
        'error_no_pdf': "Nėra įkelto PDF",
        'error_page_not_found': "Puslapis nerastas",
        'error_invalid_range': "Neteisingas puslapių intervalas",
        'error_file_not_found': "Failas nerastas",
        'error_permission': "Nėra leidimo",
        'error_unknown': "Nežinoma klaida",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Sėkminga",
        'success_operation': "Operacija sėkmingai baigta",
        'success_saved': "Sėkmingai išsaugota",
        'success_exported': "Sėkmingai eksportuota",
        'success_imported': "Sėkmingai importuota",
        'success_deleted': "Sėkmingai ištrinta",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Patvirtinimas",
        'confirm_yes': "Taip",
        'confirm_no': "Ne",
        'confirm_ok': "Gerai",
        'confirm_cancel': "Atšaukti",
        'confirm_delete': "Ištrinti",
        'confirm_overwrite': "Perrašyti",
        'confirm_continue': "Tęsti",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Įkeliamas PDF...",
        'progress_saving': "Išsaugomas PDF...",
        'progress_exporting': "Eksportuojamas PDF...",
        'progress_processing': "Apdorojama...",
        'progress_wait': "Palaukite...",
        'progress_preparing': "Ruošiama...",
        'progress_finalizing': "Baigiama...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Balta",
        'color_black': "Juoda",
        'color_red': "Raudona",
        'color_green': "Žalia",
        'color_blue': "Mėlyna",
        'color_yellow': "Geltona",
        'color_magenta': "Purpurinė",
        'color_cyan': "Žydra",
        'color_orange': "Oranžinė",
        'color_gray': "Pilka",
        'color_custom': "Spalvos pasirinkimas",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Failas",
        'menu_edit': "&Redaguoti",
        'menu_view': "&Peržiūra",
        'menu_tools': "&Įrankiai",
        'menu_settings': "&Nustatymai",
        'menu_help': "&Pagalba",
        'menu_language': "🌐 Kalba",
        'menu_guides': "&Gidai",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Atidaryti",
        'file_save_as': "&Išsaugoti kaip...",
        'file_protect': "&Apsaugoti dokumentą...",
        'file_export': "&Eksportuoti",
        'file_export_pages': "Eksportuoti į Pages",
        'file_export_word': "Eksportuoti į DOCX",
        'file_export_text': "Eksportuoti į TXT",
        'file_print_now': "&Spausdinti dabar",
        'file_print': "&Spausdinti",
        'file_close': "&Uždaryti",
        'file_quit': "&Išeiti",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Ieškoti",
        'edit_ocr': " Atlikti OCR",
        'edit_rotate': "&Pasukti puslapį",
        'edit_rotate_all': "Pasukti &visus puslapius",
        'edit_delete_pages': "&Ištrinti puslapius",
        'edit_extract_pages': "&Išskirti puslapius",
        'edit_insert_pages': "&Įterpti puslapius",
        'edit_move_pages': "&Perkelti puslapius",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Įterpti tekstą ir kryželius",
        'text_insert': " Įterpti tekstą",
        'cross_insert': " Įterpti kryželį",
        'text_customize': " Koreguoti tekstą",
        'cross_customize': " Koreguoti šį kryželį",
        'cross_customize_all': " Koreguoti visus kryželius",
        'text_discard': " Atmesti šį tekstą/kryželį",
        'text_discard_all': " Atmesti visus tekstus ir kryželius",
        'text_save_all': " Išsaugoti visus tekstus ir kryželius",
        'text_guide': " Teksto įvedimas / teksto blokai – gidas",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Įterpti parašą",
        'signature_settings_menu': " Nustatymai...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Įterpti vaizdą",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Įterpti formas",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Rodyti teksto langą",
        'view_zoom': "&Mastelis",
        'view_zoom_page': "&Puslapio plotis (numatytasis)",
        'view_zoom_two': "&Du puslapiai",
        'view_zoom_overview': "&Apžvalga (keli puslapiai)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Prieinamumas",
        'settings_voice': "Balso išvestis",
        'settings_voice_tooltip': "papildo ekrano skaitytuvų balso išvestį papildoma informacija",
        'settings_signature': "&Parašų nustatymai",
        'settings_password': "&Slaptažodžių valdymas",
        'settings_backup': "Kurti atsarginę kopiją prieš pakeitimus",
        'settings_export_import': "&Eksportuoti nustatymus / importuoti nustatymus",
        'settings_export': "&Eksportuoti visus nustatymus...",
        'settings_import': "&Importuoti visus nustatymus...",
        'settings_export_info': "&Kas eksportuojama?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "įjungta",
        'voice_off': "išjungta",
        'voice_toggle': "Balso išvestis {0}",
        'voice_speed': "Greitis {0} procentų",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Įrankis nerastas:\n{0}\n\nBASE_DIR: {1}\nĮsitikinkite, kad PDF įrankiai įdiegti kataloge {1}.",
        'tool_started': "{0} paleistas",
        'tool_start_failed': "Nepavyko paleisti",
        'process_error_failed_to_start': "Nepavyko paleisti proceso. Ar failas egzistuoja?",
        'process_error_crashed': "Procesas sugriuvo paleidimo metu.",
        'process_error_timeout': "Pasiektas proceso skirtasis laikas.",
        'process_error_write': "Rašymo klaida procese.",
        'process_error_read': "Skaitymo klaida procese.",
        'process_error_unknown': "Nežinoma proceso klaida",
        'process_command': "Komanda",
        'process_normal_exit': "baigėsi normaliai",
        'process_crashed': "sugriuvo",
        'process_nonzero_exit': "{0} baigėsi klaidos kodu {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Atšaukiama...",
        'move_cancelling': "Perkėlimas atšaukiamas",
        'opening_pdf': "Atidaromas PDF...",
        'loading_document': "Įkeliamas dokumentas...",
        'pdf_opened': "PDF atidarytas",
        'pages_found_moving': "Rasta {0} puslapių, {1} perkėlimui",
        'creating_backup': "Kuriama atsarginė kopija...",
        'backup_description': "Originalaus failo kopijavimas...",
        'backup_saved_as': "Atsarginė kopija išsaugota kaip: {0}",
        'error_format': "Klaida: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Paieška atstatyta",
        'page_header_simple': "=== {0} puslapis ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Slaptažodžių valdymas – Gidas",
        'password_guide_voice': "Slaptažodžių valdymo gidas. Perskaitykite pastabas.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Slaptažodžių valdymas – Išsamus gidas</strong></p>

        <p><strong>1. PDF apsauga slaptažodžiu</strong></p>
        <ul>
        <li>Atidarius slaptažodžiu apsaugotą PDF, pasirodo dialogo langas, kuriame galite įvesti slaptažodį.</li>
        <li>Galite išsaugoti slaptažodį užšifruotą, kad nereikėtų jo įvesti kiekvieną kartą (žymimasis langelis „Išsaugoti slaptažodį“).</li>
        <li>Mygtuku „Pašalinti slaptažodį“ galite sukurti iššifruotą PDF kopiją ir ištrinti slaptažodį iš duomenų bazės.</li>
        </ul>

        <p><strong>2. Pagrindinis slaptažodis</strong></p>
        <ul>
        <li>Pagrindinis slaptažodis apsaugo prieigą prie visų išsaugotų PDF slaptažodžių.</li>
        <li><strong>Nustatymas:</strong> Eikite į „Nustatymai → Slaptažodžių valdymas → Pagrindinio slaptažodžio nustatymai“ ir spustelėkite „Nustatyti pagrindinį slaptažodį“. Pasirinkite stiprų slaptažodį (bent 8 simboliai).</li>
        <li><strong>Keitimas:</strong> Po sėkmingos autentifikacijos galite pakeisti pagrindinį slaptažodį.</li>
        <li><strong>Pašalinimas:</strong> Jei pašalinsite pagrindinį slaptažodį, VISI išsaugoti slaptažodžiai bus negrįžtamai ištrinti. Prieš tai galite eksportuoti atsarginę kopiją.</li>
        <li>Vieną kartą sesijos metu turite autentifikuotis su pagrindiniu slaptažodžiu, kad gautumėte prieigą prie apsaugotų funkcijų (pvz., slaptažodžių rodymo).</li>
        </ul>

        <p><strong>3. Slaptažodžių valdymas (sąrašas)</strong></p>
        <ul>
        <li>Skiltyje „Nustatymai → Slaptažodžių valdymas“ atsidaro lentelė su visais išsaugotais PDF failais ir jų užšifruotais slaptažodžiais.</li>
        <li><strong>Be pagrindinio slaptažodžio:</strong> Galite tik trinti įrašus – slaptažodžiai lieka paslėpti.</li>
        <li><strong>Su pagrindiniu slaptažodžiu (autentifikuota):</strong> Galite rodyti, kopijuoti, eksportuoti ir trinti slaptažodžius.</li>
        <li><strong>Eksportavimas:</strong> Pasirinkite formatą (JSON, CSV, TXT) ir išsaugokite sąrašą. Jei nustatytas pagrindinis slaptažodis, galite pasirinkti, ar slaptažodžiai eksportuojami iššifruoti, ar užšifruoti.</li>
        <li><strong>Importavimas:</strong> Anksčiau eksportuotą ZIP failą (visus nustatymus) galima vėl importuoti per „Nustatymai → Eksportuoti nustatymus / importuoti nustatymus“. Įspėjimas: esami duomenys bus perrašyti!</li>
        </ul>

        <p><strong>4. Slaptažodžių generatorius</strong></p>
        <ul>
        <li>Slaptažodžio dialogo lange (pvz., apsaugant PDF) įvesties lauko dešinėje yra kauliuko mygtukas 🎲.</li>
        <li>Spustelėkite jį, kad atidarytumėte slaptažodžių generatorių. Galite nustatyti ilgį, simbolių rinkinius (didžiosios raidės, mažosios raidės, skaitmenys, specialieji simboliai) ir skyriklį geresniam skaitomumui.</li>
        <li>Sugeneruotą slaptažodį galima tiesiogiai naudoti ir, jei reikia, nukopijuoti.</li>
        </ul>

        <p><strong>5. Svarbios saugumo pastabos</strong></p>
        <ul>
        <li>Išsaugoti slaptažodžiai saugomi užšifruoti AES-256 algoritmu. Raktas gaunamas iš jūsų pagrindinio slaptažodžio (jei jis nustatytas) arba iš fiksuotos reikšmės (be pagrindinio slaptažodžio).</li>
        <li>Be pagrindinio slaptažodžio slaptažodžiai yra užšifruoti, bet raktas yra įmontuotas programoje – užpuolikas, turintis prieigą prie jūsų failų, galėtų juos iššifruoti. Todėl primygtinai rekomenduojame naudoti pagrindinį slaptažodį.</li>
        <li>Slaptažodžių duomenų bazė yra faile `Data/passwords.json`. Reguliariai kurkite atsargines kopijas, ypač prieš pašalindami pagrindinį slaptažodį.</li>
        <li>Pametus pagrindinį slaptažodį, visi išsaugoti slaptažodžiai negrįžtamai prarandami.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Apvertimo režimas",
        'invert_mode_classic': "Klasikinis (apversti visas spalvas)",
        'invert_mode_smart': "Išmanusis (apversti tik ryškumą)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Pilkų tonų slenkstis",
        'gray_threshold_10': "10% (griežtas)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Numatytasis)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (minkštas)",
        'threshold_changed': "Slenkstis nustatytas į {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Pilkų tonų slenkstis – Paaiškinimas",
        'threshold_guide_text': "Pilkų tonų slenkstis nustato, kurie pikseliai išmaniuoju tamsiuoju režimu laikomi 'pilkais' ir yra apverčiami.\n\n"
                                "• Maža reikšmė (10%) apverčia tik beveik tobulus pilkus atspalvius – spalvoti elementai išlieka visiškai nepakitę.\n"
                                "• Didelė reikšmė (50%) apverčia ir šiek tiek spalvotus pikselius – tai padidina kontrastą, bet gali iškraipyti spalvas.\n\n"
                                "Optimali reikšmė priklauso nuo dokumento. Grynai tekstiniams dokumentams 30–40% dažnai yra idealu, spalvotai grafikai – 10–20%.\n\n"
                                "Vertę galite bet kada koreguoti per 'Nustatymų' meniu – PDF bus iš karto įkeltas iš naujo.\n\n"
                                "Pastaba:\n* Nuotraukos ir vaizdai gali būti tinkamai rodomi tik šviesiuoju režimu!\n* Apvertimo nustatymai rodomi tik tada, kai įjungtas tamsusis režimas.",
        'threshold_guide_voice': "Pilkų tonų slenkstis nustato, kiek stipriai įsikiša išmanusis tamsusis režimas. Maža reikšmė tausoja spalvas, didelė – didina kontrastą.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Atidaromas PDF...",
        'progress_loading_document': "Įkeliamas dokumentas...",
        'progress_pdf_opened': "PDF atidarytas",
        'progress_creating_backup': "Kuriama atsarginė kopija...",
        'progress_backup_description': "Saugomas originalus failas...",
        'progress_backup_created': "Atsarginė kopija sukurta",
        'progress_backup_saved_as': "Išsaugota kaip: {0}",
        'progress_analyzing_start': "Pradedama analizė...",
        'progress_searching_empty': "Ieškoma tuščių puslapių...",
        'progress_page_empty': "{0} puslapis tuščias",
        'progress_page_keep': "Palikti {0} puslapį",
        'progress_analysis_complete': "Analizė baigta",
        'progress_empty_found': "Rasta {0} tuščių puslapių",
        'progress_current_page': "Dabartinis puslapis",
        'progress_mark_delete': "Žymima ištrinti",
        'progress_range_selected': "Puslapių intervalas {0}-{1}",
        'progress_deleting_pages': "Ištrinami {0} puslapiai",
        'progress_creating_new_pdf': "Kuriamas naujas PDF...",
        'progress_transferring_pages': "Perkeliami puslapiai",
        'progress_keeping_page': "{0} puslapis bus paliktas ({1}/{2})",
        'progress_saving_pdf': "Išsaugomas PDF...",
        'progress_optimizing': "Optimizuojamas failo dydis...",
        'progress_finalizing': "Baigiama...",
        'progress_new_size': "Naujas dydis: {0:.2f} MB",
        'progress_cancelling': "Atšaukiama...",
        'progress_cancel_message': "{0} atšaukiama",
        'progress_pages_found_moving': "Rasta {0} puslapių, {1} perkelti",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analizuojamas PDF...",
        'ocr_status_optimizing': "Vykdomas vaizdo optimizavimas...",
        'ocr_status_recognizing': "Vykdomas teksto atpažinimas...",
        'ocr_status_embedding': "Įterpiamas tekstas...",
        'ocr_status_finalizing': "Baigiamas PDF...",

        # PDF-Laden
        'progress_preparing': "Ruošiama...",
        'progress_loading': "Įkeliamas PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Ištrinami puslapiai...",
        'progress_moving_title': "Perkeliami puslapiai...",
        'pages_found': "Rasta puslapių",
        'progress_creating_new_order': "Kuriama nauja tvarka...",
        'progress_sorting_pages': "Rūšiuojami puslapiai...",
        'progress_moving_to_begin': "Perkelti {0} puslapius į pradžią",
        'progress_transferring_count': "Perkelti {0} puslapius",
        'progress_transferring_before_target': "Perkelti puslapius prieš tikslą",
        'progress_moving_pages': "Perkelti {0} puslapius",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_atsargine_kopija_",
        'filename_protected_suffix': "_apsaugotas_",
        'filename_copy_suffix': "_Kopija",
        'filename_page_single': "_Puslapis_",
        'filename_page_range': "_Puslapiai_",
        'filename_export_page': "_Puslapis_{0:03}",
        'filename_export_range': "_Puslapiai_{0}-{1}",
        'filename_export_multiple': "_Puslapiai_{0}",
        'filename_with_text': "_su_Tekstu",
        'filename_with_signature': "_su_Parasu",
        'filename_with_image': "_su_Vaizdu",
        'filename_with_forms': "_su_Formomis",
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
        'view_toggle_navbar': "Rodyti mygtukų juostą",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Negalima ištrinti visų puslapių",
		'pages_cannot_delete_last_page': 'Paskutinis puslapis negali būti ištrintas!',
		'pages_cannot_delete_all_pages': 'Dokumente turi likti bent vienas puslapis!',
		'delete_pages_confirm': 'Ar tikrai norite ištrinti {0} puslapių?',
		'delete_pages_confirm_voice': 'Ar tikrai norite ištrinti {0} puslapių?',
		'pages_deleted': '{0} puslapių sėkmingai ištrinta.',
		'warning': 'Įspėjimas',
		'error': 'Klaida',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nepasirinkta forma",
        'form_customized': "Forma pritaikyta",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Pasirinkti",
        'btn_use': "Naudoti",
        'master_password_for_spasswords': "Norėdami išsaugoti ir naudoti slaptažodžius, pirmiausia turite nustatyti pagrindinį slaptažodį.\n\nAr norite nustatyti pagrindinį slaptažodį dabar?",
        'open_saved_dialog_title': "Atidaryti išsaugotą failą",
        'open_saved_question': "Ar norite atidaryti išsaugotą failą dabar?",
        'password': "Slaptažodis",
        'password_manager_master_required': "Slaptažodžių tvarkyklė pasiekiama tik tada, kai nustatytas pagrindinis slaptažodis.\n\nAr norite nustatyti pagrindinį slaptažodį dabar?",
        'password_master_required_for_select': "Norėdami peržiūrėti ir pasirinkti išsaugotus slaptažodžius, pirmiausia turite autentifikuotis naudodami pagrindinį slaptažodį.\n\nAr norite autentifikuotis dabar?",
        'password_not_available': "Pasirinktas slaptažodis nėra pasiekiamas arba nepavyko jo iššifruoti.",
        'password_options_title': "Slaptažodžio parinktys",
        'password_save_choice_change': "Nustatyti naują slaptažodį",
        'password_save_choice_keep': "Naudoti esamą slaptažodį",
        'password_save_choice_none': "Išsaugoti neužšifruotą",
        'password_save_hint': "Pirmiausia nustatykite pagrindinį slaptažodį, kad saugiai išsaugotumėte slaptažodžius.",
        'password_save_master_required': "Išsaugoti slaptažodį (įmanoma tik su pagrindiniu slaptažodžiu)",
        'password_save_question': "Dabartinis PDF yra apsaugotas slaptažodžiu. Ar norite naudoti esamą slaptažodį, nustatyti naują ar išsaugoti neužšifruotą?",
        'password_select': "Pasirinkti slaptažodį",
        'password_select_none': "Nepasirinktas joks slaptažodis.\n\nPasirinkite slaptažodį iš sąrašo.",
        'password_select_one': "Pasirinkite tiksliai vieną slaptažodį.\n\nPažymėjote kelis slaptažodžius.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_atsarginė",
        'filename_insert_suffix': "_su_įterpimu",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_puslapiai_ištrinti",
        'filename_pages_moved': "_puslapiai_perkelti",
        'filename_rotated_all_suffix': "_visi_puslapiai_pasukti",
        'filename_rotated_suffix': "_puslapis_pasuktas",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Failų pavadinimų konfigūracija keičiant PDF",
        'filename_keep_suffixes': "Išlaikyti ankstesnius plėtinius (pvz., _su_tekstu)",
        'filename_keep_suffixes_false': "Pakeisti",
        'filename_keep_suffixes_true': "Išlaikyti",
        'filename_preview_label': "Failo pavadinimo peržiūra:",
        'filename_preview_overwrite_hint': "Peržiūra negalima – originalas bus perrašytas.",
        'filename_separator': "Žodžių skirtukas",
        'filename_separator_none': "Jokio skirtuko",
        'filename_separator_space': "Tarpas ( )",
        'filename_separator_underscore': "Pabraukimas (_)",
        'filename_settings_saved': "Failo pavadinimo nustatymai išsaugoti",
        'filename_settings_title': "Failo pavadinimo formatavimas ir atsarginė kopija",
        'filename_timestamp_position': "Laiko žymos vieta",
        'filename_timestamp_position_after': "Po pagrindinio pavadinimo",
        'filename_timestamp_position_before': "Pačiame priekyje",
        'filename_timestamp_position_end': "Pabaigoje",
        'filename_use_timestamp': "Naudoti laiko žymą",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Elgsena keičiant:</b><ul><li>Puslapių trynimas ir įterpimas</li><li>Teksto, parašo, paveikslėlio ir formų įterpimas</li><li>OCR</li></ul></html>",
        'backup_section': "Atsarginė kopija puslapių operacijoms (Ištrinti, Perkelti)",
        'behavior_info': "Pastaba: Pasirinkus 'Perrašyti originalą', laiko žymos ir priesagos ignoruojamos – failas išlaiko savo pavadinimą.",
        'behavior_new_file': "Visada kurti naują failą (su laiko žyma ir priesaga)",
        'behavior_overwrite': "Perrašyti originalą (nėra naujo failo)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Visi puslapiai buvo pasukti.\n\nOriginalas liko nepakitęs.\nNaujas failas: {0}",
        'all_pages_rotated_voice': "Visi puslapiai pasukti, sukurtas naujas failas.",
        'empty_pages_deleted_new_file': "{0} tuščių puslapių buvo ištrinta.\n\nOriginalas liko nepakitęs.\nNaujas failas: {1}",
        'empty_pages_deleted_voice': "{0} tuščių puslapių ištrinta, sukurtas naujas failas.",
        'ocr_keep_original': "Išlaikyti originalą (vėliau atidaryti rankiniu būdu)",
        'ocr_new_file_question': "Naujas ieškomas PDF buvo išsaugotas kaip:\n{0}\n\nAr norite jį atidaryti dabar?",
        'ocr_open_new': "Atidaryti naują OCR failą",
        'ocr_original_kept': "Originalus failas lieka atidarytas. OCR failas išsaugotas.",
        'page_deleted_new_file': "Puslapis {0} buvo ištrintas.\n\nOriginalas liko nepakitęs.\nNaujas failas: {1}",
        'page_deleted_voice': "Puslapis {0} ištrintas, sukurtas naujas failas.",
        'page_rotated_new_file': "Puslapis {0} buvo pasuktas.\n\nOriginalas liko nepakitęs.\nNaujas failas: {1}",
        'page_rotated_voice': "Puslapis {0} pasuktas, sukurtas naujas failas.",
        'pages_deleted_new_file': "Buvo ištrinti {0} puslapiai.\n\nOriginalus failas liko nepakitęs.\nNaujas failas: {1}",
        'pages_deleted_new_file_voice': "{0} puslapių ištrinta, sukurtas naujas failas.",
        'pages_inserted_new_file': "Buvo įterpti {0} puslapiai.\n\nOriginalus failas liko nepakitęs.\nNaujas failas: {1}",
        'pages_inserted_new_file_ask': "Buvo įterpti {0} puslapiai.\n\nOriginalas liko nepakitęs.\nNaujas failas: {1}\n\nAr norite jį atidaryti dabar?",
        'pages_inserted_voice_new': "{0} puslapių įterpta, sukurtas naujas failas.",
        'pages_moved_new_file': "Buvo perkelti {0} puslapiai.\n\nOriginalus failas liko nepakitęs.\nNaujas failas: {1}",
        'pages_moved_new_file_voice': "{0} puslapių perkelta, sukurtas naujas failas.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Daugiau nerodyti",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Atsarginės kopijos nustatymas</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Atsarginė kopija ĮJUNGTA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Visiems pakeitimams, kurie perrašo originalą</strong> (tekstas, parašas, paveikslėlis, forma, OCR, pasukimas, įterpimas, puslapių trynimas/perkėlimas) <strong>automatiškai sukuriama atsarginė kopija su laiko žyma</strong> prieš pritaikant pakeitimą.</p>
                <p style="margin: 5px 0 5px 20px;">• Atsarginė kopija yra šalia originalaus failo (pvz., <code>Dokumentas_atsarginė_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Jei papildomai suaktyvinote parinktį <strong>„Perrašyti originalą“</strong>, taip pat sukuriama atsarginė kopija.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Atsarginė kopija IŠJUNGTA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Jokia atsarginė kopija nėra sukuriama</strong> – nei perrašant, nei atliekant puslapių operacijas.</p>
                <p style="margin: 5px 0 5px 20px;">• Originalus failas gali būti negrįžtamai prarastas perrašant.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Rekomenduojama tik patyrusiems naudotojams!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Patarimas:</strong> Atsarginės kopijos nustatymas nepriklauso nuo parinkties „Perrašyti originalą“. Galite derinti abu.<br>
                Šį pranešimą galite visam laikui paslėpti.
            </div>
        </div>
        """,
        'backup_info_title': "Atsarginės kopijos elgsena",
        'backup_info_voice': "Pranešimas apie atsarginės kopijos elgseną atliekant puslapių operacijas. Atsarginė kopija įjungta perrašo originalą, išjungta sukuria naują failą.",
        'show_backup_info': "Informacija apie atsarginės kopijos nustatymą",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Daugiau nerodyti",
        'overwrite_enable_backup': "Įjungti atsarginę kopiją (rekomenduojama)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Perrašyti originalą</p>
            <p>Jei suaktyvinsite šią parinktį, pakeitimai (tekstas, parašas, paveikslėlis, forma, OCR, pasukimas, įterpimas) <strong>išsaugomi tiesiogiai originale</strong> – <strong>naujas failas nėra kuriamas</strong>.</p>
            <p>• Failo pavadinimas lieka nepakitęs.<br>
            • Laiko žymos ir priesagos ignoruojamos.<br>
            • <strong>Be atsarginės kopijos originalas gali būti negrįžtamai prarastas.</strong></p>
            <p style="color: #FFD700;">Rekomendacija: Papildomai įjunkite atsarginės kopijos parinktį, kad gautumėte automatines atsargines kopijas.</p>
        </div>
        """,
        'overwrite_info_title': "Perrašyti originalą",
        'overwrite_info_voice': "Įspėjimas: Perrašyti originalą – nėra naujo failo. Rekomenduojama atsarginė kopija.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Buvo įterpti {0} puslapiai.\n\nOriginalus failas buvo perrašytas.\nSukurta atsarginė kopija.",
        'pages_inserted_overwrite_no_backup': "Buvo įterpti {0} puslapiai.\n\nOriginalus failas buvo perrašytas.\nNEbuvo sukurta atsarginė kopija.",
        'texts_saved_overwrite_with_backup': "Pakeitimai buvo išsaugoti originale.\n\nSukurta atsarginė kopija.",
        'texts_saved_overwrite_no_backup': "Pakeitimai buvo išsaugoti originale.\n\nNEbuvo sukurta atsarginė kopija.",
        'texts_crosses_saved_new_file': "{0} {1} ir {2} {3} buvo įterpti.\n\nOriginalus failas liko nepakitęs.\nSukurtas naujas failas.\n\nĮkeliamas naujas PDF...",
        'texts_saved_new_file': "{0} {1} buvo įterpti.\n\nOriginalus failas liko nepakitęs.\nSukurtas naujas failas.\n\nĮkeliamas naujas PDF...",
        'crosses_saved_new_file': "{0} {1} buvo įterpti.\n\nOriginalus failas liko nepakitęs.\nSukurtas naujas failas.\n\nĮkeliamas naujas PDF...",
        'elements_saved_new_file': "{0} elementų buvo įterpta.\n\nOriginalus failas liko nepakitęs.\nSukurtas naujas failas.\n\nĮkeliamas naujas PDF...",
        'signatures_saved_overwrite_with_backup': "Parašas(as) buvo išsaugotas(i) originale.\n\nSukurta atsarginė kopija.",
        'signatures_saved_overwrite_no_backup': "Parašas(as) buvo išsaugotas(i) originale.\n\nNEbuvo sukurta atsarginė kopija.",
        'images_saved_overwrite_with_backup': "Paveikslėlis(iai) buvo išsaugotas(i) originale.\n\nSukurta atsarginė kopija.",
        'images_saved_overwrite_no_backup': "Paveikslėlis(iai) buvo išsaugotas(i) originale.\n\nNEbuvo sukurta atsarginė kopija.",
        'forms_saved_overwrite_with_backup': "Forma(os) buvo išsaugota(os) originale.\n\nSukurta atsarginė kopija.",
        'forms_saved_overwrite_no_backup': "Forma(os) buvo išsaugota(os) originale.\n\nNEbuvo sukurta atsarginė kopija.",
        'signatures_saved_new_file': "{0} parašų buvo įterpta.\n\nOriginalus failas liko nepakitęs.\nSukurtas naujas failas.\n\nĮkeliamas naujas PDF...",
        'images_saved_new_file': "{0} paveikslėlių buvo įterpta.\n\nOriginalus failas liko nepakitęs.\nSukurtas naujas failas.\n\nĮkeliamas naujas PDF...",
        'forms_saved_new_file': "{0} formų buvo įterpta.\n\nOriginalus failas liko nepakitęs.\nSukurtas naujas failas.\n\nĮkeliamas naujas PDF...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Įspėjimas: Šiame PDF yra pasuktų puslapių. Pozicionavimas gali skirtis.",
        'page_rotated_warning_title': "Aptiktas pasuktas puslapis",
        'page_rotated_warning_message': "Dabartinis puslapis {0} yra pasuktas {1}°.\n\nElementų įterpimas ant pasuktų puslapių nepalaikomas.\n\nAr norite dabar pasukti puslapį į vertikalią padėtį?",
        'page_rotated_warning_voice': "Įspėjimas: Puslapis yra pasuktas. Pirmiausia jį pasukite.",
        'paste_on_rotated_page_simple_warning': "Įterpimas ant puslapio {0} negalimas!\n\nŠis puslapis yra pasuktas {1}°.\n\nPirmiausia pasukite puslapį į 0° (Meniu: Redaguoti → Sulygiuoti puslapį).\n\nĮspėjimas:\nAnksčiau nukopijuotas elementas bus prarastas, jei neišsaugosite prieš sukant puslapį.",
        'paste_on_rotated_page_voice': "Įterpimas atšauktas. Puslapis yra pasuktas. Pirmiausia sulygiuokite puslapį.",
        'page_rotated_cancel': "Atšaukti",
        'page_rotated_rotate_until_upright': "Kartoti puslapio pasukimą (kol bus vertikalus)",
        'page_rotated_now_upright': "Puslapis dabar yra vertikalus. Dabar galite įterpti.",
        'page_rotated_still_not_upright': "Nepavyko pasukti puslapio į vertikalią padėtį. Pataisykite rankiniu būdu.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Pagalba: Ištaisyti pasuktus puslapius",
        'help_rotated_pages_voice': "Atidaroma pagalba, skirta pasuktiems puslapiams taisyti.",
        'btn_help': "Pagalba",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problema: Pasuktas puslapis – Įterpimas neveikia tinkamai</p>

            <p>Jei tekstų, parašų ar formų įterpimas ant pasukto puslapio neveikia tinkamai, galite ištaisyti puslapį naudodami išorinį PDF redaktorių.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Sprendimas naudojant išorinį įrankį (pvz., macOS Peržiūra)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksportuoti puslapį</strong><br>
                &nbsp;&nbsp;Meniu spustelėkite <strong>Failas → Eksportuoti kaip puslapius</strong> arba naudokite kitą metodą norimam puslapiui išsaugoti kaip atskirą PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Atidaryti puslapį išorinėje programoje</strong><br>
                &nbsp;&nbsp;Atidarykite eksportuotą PDF PDF redaktoriuje (pvz., <strong>macOS Peržiūra</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Pasukti puslapį</strong><br>
                &nbsp;&nbsp;Pasukite puslapį taip, kad jis būtų vertikalus (Peržiūroje: <strong>Įrankiai → Pasukti</strong> arba <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Išsaugoti</strong><br>
                &nbsp;&nbsp;Išsaugokite pataisytą puslapį (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Vėl įterpti puslapį į originalų dokumentą</strong><br>
                &nbsp;&nbsp;Grįžkite į PDFDarkView ir įterpkite pataisytą puslapį norimoje vietoje:<br>
                &nbsp;&nbsp;<strong>Redaguoti → Įterpti puslapius</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatyva: Pasukti puslapį originale</p>
                <p style="margin: 5px 0 5px 20px;">• Naudokite įmontuotą pasukimo funkciją (<strong>Redaguoti → Pasukti puslapį</strong>), kad pataisytumėte puslapį žingsnis po žingsnio.<br>
                • Po kiekvieno pasukimo galite patikrinti, ar įterpimas dabar veikia.<br>
                • Tai dažnai yra greitesnis sprendimas – pabandykite pirmiausia!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Patarimas:</strong> Jei dažnai susiduriate su pasuktais puslapiais, galite visam laikui paslėpti įspėjimą įterpimo dialogo lange.<br>
                Pozicionavimas gali skirtis – naudokite šią parinktį tik jei žinote pasekmes.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Sulygiuoti puslapius",
        'menu_rotate_normalize_tooltip': "Pasukti puslapį arba atstatyti į 0°",
        'normalize_current_page': "Pervesti dabartinį puslapį į vertikalią padėtį (nustatyti 0°)",
        'normalize_all_pages': "Pervesti visus puslapius į vertikalią padėtį (nustatyti 0°)",
        'page_normalized': "Puslapis {0} nustatytas į vertikalią padėtį.",
        'all_pages_normalized': "Visi puslapiai nustatyti į vertikalią padėtį.",
        'page_already_upright': "Puslapis {0} jau yra vertikalus.",
        'all_pages_already_upright': "Visi puslapiai jau yra vertikalūs.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF neturi ieškomo teksto.</p><p>Ar norite atlikti OCR, kad eksportuotumėte į {0}?</p>",
        'export_ocr_voice': "PDF neturi teksto. Eksportui į {0} reikalingas OCR.",
        'export_no_ocr_possible': "Eksportas be OCR neįmanomas. Atlikite OCR per meniu.",
        'ocr_failed_export_not_possible': "OCR nepavyko. Eksportas negali būti atliktas.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF bus atidarytas Peržiūroje. Ten pradėkite spausdinimo procesą.",
        'print_preview_manual': "PDF atidarytas. Spausdinimo komandą vykdykite rankiniu būdu (pvz., Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Sujungti PDF failus",
        'merge_pdfs': "Sujungti PDF failus",
        'merge_progress_title': "Sujungiami PDF failai...",
        'merge_pdfs_list': "PDF failai eilės tvarka (Vilkite ir meskite rūšiavimui)",
        'merge_add_pdf': "Pridėti PDF",
        'merge_remove': "Pašalinti",
        'merge_move_up': "Aukštyn",
        'merge_move_down': "Žemyn",
        'merge_pdfs_info': "💡 Patarimas: Galite pakeisti eiliškumą vilkdami ir mesdami",
        'merge_no_pdfs': "Nepasirinkta jokių PDF failų. Spustelėkite 'Pridėti PDF'.",
        'merge_info': "Pasirinkta {0} PDF failų (apytiksliai {1} puslapiai)",
        'merge_open_file': "Atidaryti failą",
        'merge_merge': "Sujungti",
        'merge_error': "Klaida sujungiant",
        'merge_min_two_pdfs_error': "Pasirinkite bent du PDF failus sujungimui.",
        'merge_select_pdfs': "Pasirinkite PDF failus sujungimui",
        'merge_error_file': "Klaida apdorojant",
        'merge_cancelled': "Sujungimas atšauktas",
        'merge_preparing': "Ruošiamasi...",
        'merge_processing': "Apdorojamas PDF {0} iš {1}",
        'merge_saving': "Išsaugomas sujungtas PDF...",
        'merge_complete': "Baigta!",
        'merge_success_title': "Sujungimas pavyko",
        'merge_success_voice': "{0} PDF failai sėkmingai sujungti.",
        'merge_success_message': "{0} PDF failai sėkmingai sujungti.\n\nNaujame dokumente dabar yra {1} puslapiai.\n\nNaujas failas:\n{2}\n\nIšsaugojimo vieta:\n{3}\n{2}\n\nAr norite atidaryti šį PDF?",
        'replace_file_title': "Pakeisti failą?",
        'replace_file_message': "PDF jau atidarytas. Ar norite jį pakeisti nauju failu?",
        'btn_yes': "Taip",
        'btn_no': "Ne",
        'filename_merge_suffix': "sujungtas",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Atidaromas {0}...",
        'progress_merge_reading': "Skaitomas {0}...",
        'progress_merge_adding': "Pridedama {0} puslapių...",
        'progress_merge_optimizing': "Optimizuojamas PDF...",
        'progress_merge_writing': "Rašomas PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF uždarymo",
        'action_close_window': "lango uždarymo",
        'action_open_new_pdf': "naujo PDF atidarymo",
        'action_quit_app': "programos išjungimo",
        'changes_saved': "Pakeitimai išsaugoti.",
        'file_close_title': "Uždaryti PDF failą",
        'save_before_action': "Ar prieš {0} reikia išsaugoti pakeitimus? Taip arba Ne?",
        'save_before_action_voice': "Ar prieš {0} reikia išsaugoti pakeitimus? Taip arba Ne?",
        'save_before_close_question': "Ar prieš uždarant reikia išsaugoti pakeitimus? Taip arba Ne?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Sukurtas ieškomas PDF:\n\n{0}\n\n<b>jei reikia, bandykite dar kartą",
        "ocr_rotate_title": "Sulygiuoti puslapius prieš OCR",
        "ocr_rotate_question": "PDF yra pasuktų puslapių.\nAr norite prieš OCR sulygiuoti visus puslapius į 0°?\nTai žymiai pagerina teksto atpažinimą.",
        "ocr_rotate_yes": "Taip, sulygiuoti",
        "ocr_rotate_no": "Ne, paleisti OCR tiesiogiai",
        "ocr_rotate_voice": "PDF yra pasuktų puslapių. Ar prieš OCR reikia sulygiuoti visus puslapius?",
        "ocr_not_performed_message": "Nėra teksto. Atlikite OCR (meniu \"Redaguoti\" → \"Atlikti OCR\" arba klavišas Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR nustatymai",
        "ocr_language_btn": "Pasirinkti OCR kalbą",
        "ocr_language": "OCR kalba(-os)",
        "ocr_language_current": "Dabartinė kalba:",
        "ocr_param_info": "Informacija apie parametrą",

        "ocr_force_ocr_label": "Priverstinis OCR",
        "ocr_deskew_label": "Koreguoti pasvirimą",
        "ocr_clean_label": "Išvalyti vaizdą",
        "ocr_oversample_label": "Skiriamoji geba (DPI)",
        "ocr_pagesegmode_label": "Puslapio segmentavimas",
        "ocr_oem_label": "OCR variklio režimas",
        "ocr_optimize_label": "PDF glaudinimas",
        "ocr_jobs_label": "Lygiagretūs procesai",
        "ocr_verbose_label": "Žurnalo išsamumas",

        "ocr_force_ocr_tooltip": "Priverstinis OCR kiekviename puslapyje, net jei tekstas jau yra",
        "ocr_deskew_tooltip": "Automatiškai sulygiuoti pasvirusius nuskaitymus",
        "ocr_clean_tooltip": "Pašalinti triukšmą ir artefaktus iš vaizdo",
        "ocr_oversample_tooltip": "Padidinti vaizdą prieš OCR iki šio DPI",
        "ocr_pagesegmode_tooltip": "Nustato, kaip puslapis padalijamas į teksto sritis",
        "ocr_oem_tooltip": "Pasirenka Tesseract OCR variklį",
        "ocr_optimize_tooltip": "Išvesties PDF glaudinimo lygis",
        "ocr_jobs_tooltip": "Lygiagrečių OCR procesų skaičius",
        "ocr_verbose_tooltip": "Žurnalo išvesties išsamumo lygis",
        "ocr_settings_explain_btn": "Paaiškinimas",

        "ocr_force_ocr_explain": "Priverčia teksto atpažinimą <b>kiekviename</b> puslapyje, net jei jame jau yra teksto.\n\nRekomendacija: <b>Įjungti</b> nuskaitytiems PDF, <b>Išjungti</b> gimtiesiems PDF su jau esančiu tekstu.",

        "ocr_deskew_explain": "Koreguoja šiek tiek pasvirusius nuskaitymus (iki maždaug 5°).\n\nRekomendacija: <b>Įjungti</b> nuskaitytiems dokumentams, <b>Išjungti</b> jei puslapiai jau tobulyje tiesūs.",

        "ocr_clean_explain": "Pašalina triukšmą, taškus ir mažus artefaktus iš vaizdo.\n<b>SVARBU:</b> Arabų, tajų ar vietnamiečių tekstams su diakritiniais ženklais (taškais virš/po raidėmis) ši parinktis turėtų būti <b>Išjungta</b>, kitaip gali būti prarasti svarbūs simboliai.",

        "ocr_oversample_explain": "Padidina vaizdą <b>prieš</b> teksto atpažinimą iki nurodyto DPI.<br><br>• <b>72-150 DPI:</b> Labai greita, bet žemas atpažinimo lygis<br>• <b>200-300 DPI:</b> Optimalus diapazonas (Standartas: 300)<br>• <b>400+ DPI:</b> Vos geresnis atpažinimas, bet žymiai didesni failai<br><br>Rekomendacija: 300 DPI sudėtingiems raštams (arabų, kinų, japonų), 200 DPI vakarietiškoms kalboms.",

        "ocr_pagesegmode_explain": "Nustato, kaip Tesseract padalija puslapį į teksto sritis.\n\n• <b>3 - Automatinis (Standartas):</b> Geras mišriems maketams\n• <b>4 - Vienas stulpelis:</b> Vieno stulpelio tekstams\n• <b>5 - Vertikalus blokas:</b> Vertikaliems raštams (japonų, kinų)\n• <b>6 - Vienodas teksto blokas:</b> Optimalus tekančiam tekstui be stulpelių\n• <b>11 - Neapdorotas vaizdas:</b> Blogiems nuskaitymams / rankraščiams\n\nRekomendacija: <b>6</b> paprastiems teksto dokumentams, <b>3</b> sudėtingiems maketams.",

        "ocr_oem_explain": "Pasirenka Tesseract OCR variklį.\n\n• <b>0 - Legacy:</b> Senas variklis (greitas, bet mažiau tikslus)\n• <b>1 - LSTM:</b> Neuroninis variklis (lėtesnis, bet tikslesnis)\n• <b>2 - Legacy + LSTM:</b> Derina abu rezultatus\n• <b>3 - Standartas (LSTM pirmenybė):</b> Geriausias pasirinkimas daugeliu atvejų\n\nRekomendacija: <b>3</b> maksimaliam atpažinimo tikslumui.",

        "ocr_optimize_explain": "Glaudina išvesties PDF.\n\n• <b>0:</b> Be optimizavimo (greičiausias apdorojimas)\n• <b>1:</b> Lengvas optimizavimas (geras kompromisas)\n• <b>2:</b> Vidutinis optimizavimas\n• <b>3:</b> Stiprus optimizavimas (mažiausias failas, bet lėtesnis)\n\nRekomendacija: <b>1</b> kasdieniam naudojimui.",

        "ocr_jobs_explain": "Lygiagrečių procesų skaičius OCR.\n\n• <b>1:</b> Lėtas, bet mažiausias atminties suvartojimas\n• <b>4-8:</b> Optimalus šiuolaikiniams kelių branduolių procesoriams\n• <b>12+:</b> Vos greitesnis apdorojimas esant dideliam atminties suvartojimui\n\nRekomendacija: CPU branduolių skaičius (pvz., <b>4</b> 4 branduolių sistemose).",

        "ocr_verbose_explain": "Žurnalo išvesties išsamumo lygis konsolėje.\n\n• <b>0:</b> Be išvesties\n• <b>1:</b> Eiga ir būsenos pranešimai\n• <b>2:</b> Išsami išvestis\n• <b>3:</b> Pilna derinimo išvestis (labai išsami)\n\nRekomendacija: <b>1</b> normaliam veikimui.",

        "ocr_reset_title": "Nustatymai atstatyti",
        "ocr_reset_message": "Visi OCR nustatymai buvo atstatyti į standartines reikšmes.",
        "info_tooltip": "Daugiau informacijos apie šį parametrą",
        "ocr_reset_defaults": "Atstatyti į standartinius",

        "ocr_psm_0": "Automatinis (Legacy variklis)",
        "ocr_psm_1": "Automatinis stulpelių aptikimas",
        "ocr_psm_3": "Automatinis (Standartas)",
        "ocr_psm_4": "Vienas stulpelis",
        "ocr_psm_5": "Vertikalus blokas",
        "ocr_psm_6": "Vienodas teksto blokas",
        "ocr_psm_7": "Viena teksto eilutė",
        "ocr_psm_8": "Vienas žodis",
        "ocr_psm_11": "Neapdorotas vaizdas (be maketo analizės)",

        "ocr_oem_0": "Legacy variklis (greitas)",
        "ocr_oem_1": "LSTM variklis (neuroninis, tikslus)",
        "ocr_oem_2": "Legacy + LSTM kombinuotas",
        "ocr_oem_3": "Standartas (LSTM pirmenybė)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR kalba(-os)...",
        "ocr_language_title": "Pasirinkti OCR kalbą(-as)",
        "ocr_language_instruction": "Pasirinkite kalbą(-as) teksto atpažinimui (OCR).\nDėmesio: Kelios kalbos eina našumo ir tikslumo sąskaita!\nGeriausius rezultatus pasieksite, jei pasirinksite tik vieną kalbą.",
        "ocr_language_predefined": "Iš anksto nustatyti deriniai",
        "ocr_language_custom": "Individualus...",
        "ocr_language_selected": "Pasirinktos OCR kalbos",
        "ocr_language_changed": "OCR kalba pakeista į {0}",
        "ocr_language_auto_detect": "Galimos kalbos aptinkamos automatiškai.",
        "ocr_language_none_found": "Nerasta Tesseract kalbos duomenų! Įdiekite kalbos paketus (pvz., 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Individualus kalbos pasirinkimas",
        "ocr_language_available": "Galimos kalbos (įdiegtos):",
        "ocr_language_select_hint": "Pasirinkite vieną ar daugiau kalbų:",
        "ocr_language_confirm": "Taikyti",
        "ocr_language_reset": "Atstatyti į standartinį (deu+eng+vie)",
        "ocr_language_priorities": "Rekomenduojamos kalbos (iš anksto įdiegtos):",

        "select_all_languages": "Pasirinkti viską",
        "clear_all_languages": "Išvalyti pasirinkimą",
        "install_language_packs": "Įdiegti trūkstamus kalbos paketus...",
        "install_hint": "💡 Patarimas: Ne visos kalbos yra įdiegtos jūsų sistemoje. Šiuo mygtuku gausite pagalbą diegimui.",
        "ocr_language_install_title": "Tesseract kalbos paketų diegimas",

        "ocr_missing_languages": "Trūksta OCR kalbos paketų",
        "ocr_missing_languages_message": "Šios pasirinktos kalbos nėra įdiegtos jūsų sistemoje:\n\n{0}\n\nĮdiekite trūkstamus kalbos paketus (žr. pagalbą skiltyje 'Diegimo pagalba').\n\nAr norite atidaryti diegimo pagalbą dabar?",
        "ocr_missing_languages_voice": "Trūksta kalbos paketų. Įdiekite trūkstamas kalbas.",
        "ocr_install_help_now": "Atidaryti pagalbą",
        "ocr_continue_anyway": "Vis tiek bandyti",
        "ocr_language_error_title": "OCR kalbos klaida",
        "ocr_language_error_message": "Klaida teksto atpažinimo metu: {0}\n\nPatikrinkite savo OCR kalbos nustatymus (Nustatymai → OCR kalba).",
        "ocr_install_help_button": "Diegimo pagalba",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Įdiegti Tesseract kalbos paketus</p>

        <p>Kad OCR veiktų konkrečia kalba, atitinkami kalbos duomenys turi būti įdiegti jūsų sistemoje. Vykdykite instrukcijas, skirtas jūsų operacinei sistemai:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Atidarykite <strong>Terminalą</strong> (Finder → Programos → Pagalbinės programos → Terminalas).</li>
        <li>Įdiekite visas galimas kalbas su:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Tai gali užtrukti kelias minutes.)</li>
        <li>Arba tik atskiras kalbas (pvz., vietnamiečių):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Su dabartinėmis Homebrew versijomis, <code>*.traineddata</code> gali tekti atsisiųsti rankiniu būdu (žr. žemiau).</li>
        <li>Po diegimo: Uždarykite šį dialogo langą ir vėl atidarykite OCR kalbos pasirinkimą – naujos kalbos pasirodys automatiškai.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Atidarykite terminalą (Ctrl+Alt+T).</li>
        <li>Įdiekite norimą kalbą, pvz., vietnamiečių:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Svarbūs kalbos kodai: <code>deu</code> (vokiečių), <code>eng</code> (anglų), <code>vie</code> (vietnamiečių), <code>spa</code> (ispanų), <code>fra</code> (prancūzų), <code>ita</code> (italų), <code>nld</code> (olandų), <code>fin</code> (suomių), <code>swe</code> (švedų), <code>nor</code> (norvegų).</li>
        <li>Rodyti visus galimus paketus:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (rankiniu būdu)</p>
        <ol>
        <li>Atsisiųskite norimus <code>*.traineddata</code> failus iš:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (pvz., <code>vie.traineddata</code> vietnamiečių kalbai).</li>
        <li>Nukopijuokite failus į Tesseract kalbos aplanką, paprastai:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Pritaikykite pagal individualų diegimą.)</li>
        <li>Iš naujo paleiskite programą (arba vėl atidarykite OCR kalbos pasirinkimą).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatyva visoms sistemoms</p>
        <ul>
        <li>Įdiekite <strong>OCRmyPDF</strong> ir <strong>Tesseract</strong> su savo pasirinktu paketų tvarkykle. Daugumoje diegimų jau yra keletas standartinių kalbų (anglų, vokiečių, prancūzų).</li>
        <li>Trūkstamas kalbas galima įdiegti bet kuriuo metu – OCR kalbos pasirinkimas rodo tik faktiškai egzistuojančias kalbas.</li>
        </ul>

        <hr>
        <p><b>✅ Po diegimo:</b> Nereikia iš naujo paleisti programos – naujai pridėtos kalbos iš karto pasirodys sąraše.</p>
        <p><b>📖 Pagalba dėl kalbos kodų:</b> Išsamų sąrašą rasite <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract dokumentacijoje</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans šriftai",
        "info_noto_font_voice": "Noto Sans šriftų diegimo vadovas",
        "btn_info_noto_font_install": "Šrifto informacija",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Kaip įdiegti nemokamus Google Noto šriftus</h2>

        <p><strong>Noto šriftai</strong> yra Google atvirojo kodo šriftų šeima. Jų tikslas yra nematyti <em>"jokio tofu"</em> (t. y. jokių tuščių langelių □) ir teisingai atvaizduoti kiekvieną Unicode standarto simbolį. Jie yra idealus priedas programoms, kurios turi rodyti tekstus daugeliu skirtingų kalbų.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Diegimas macOS</h3>

        <p><strong>Metodas 1: Su Homebrew (pažengusiems)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metodas 2: Naudojant "Font Book" (Rekomenduojama)</strong></p>

        <ol>
        <li>Atsisiųskite oficialų šriftų paketą:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Išskleiskite ZIP failą</li>
        <li>Nukopijuokite failus į <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Diegimas Windows (10 ir 11)</h3>

        <p><strong>Metodas 1: Microsoft Store (Rekomenduojama)</strong><br>
        Ieškokite "Google Noto Fonts" arba "Noto Sans" ir spustelėkite <strong>Įdiegti</strong>.</p>

        <p><strong>Metodas 2: Rankinis diegimas</strong></p>

        <ol>
        <li>Atsisiųsti:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Išskleisti ZIP</li>
        <li>Pasirinkite .ttf / .otf failus</li>
        <li>Dešiniuoju pelės mygtuku → <strong>Įdiegti</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        arba<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Vardas\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Diegimas Linux</h3>

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

        <p>Patikrinimas:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Tvarkyti žymes",
        "bookmark_add": "Pridėti žymę",
        "bookmark_add_tooltip": "Išsaugoti esamą puslapį kaip žymę",
        "bookmark_remove": "Pašalinti žymę",
        "bookmark_remove_tooltip": "Ištrinti pažymėtą žymę",
        "bookmark_remove_all": "Pašalinti visas",
        "bookmark_remove_all_tooltip": "Ištrinti visas šio PDF žymes",
        "bookmark_jump": "Pereiti prie žymės",
        "bookmark_jump_tooltip": "Pereiti į pasirinktą puslapį",
        "bookmark_name": "Pavadinimas",
        "bookmark_page": "Puslapis",
        "bookmark_no_bookmarks": "Nėra žymių.\nSpustelėkite 'Pridėti', kad išsaugotumėte esamą puslapį kaip žymę.",
        "bookmark_added": "Pridėta žymė puslapiui {0}: {1}",
        "bookmark_removed": "Žymė pašalinta: {0}",
        "bookmark_all_removed": "Visos žymės buvo pašalintos.",
        "bookmark_name_default": "Puslapis {0}",
        "bookmark_name_prompt": "Žymės pavadinimas:\n(ilgas tekstas bus sutrumpintas iki 50 simbolių)",
        "bookmark_name_prompt_title": "Žymės pavadinimas",
        "bookmark_confirm_remove_all": "Ar tikrai norite pašalinti visas {0} žymes?",
        "menu_bookmarks": "Žymės",
        "bookmark_manage": "Tvarkyti žymes",
        "bookmark_next": "Kita žymė",
        "bookmark_prev": "Ankstesnė žymė",
        "bookmark_page_display": "Puslapis {0}",
        "bookmark_exists": "Žymė šiam puslapiui su šiuo pavadinimu jau egzistuoja.",
        "bookmark_select_first": "Pirmiausia pasirinkite žymę.",
        "bookmark_confirm_remove": "Ar tikrai norite pašalinti žymę 'Puslapis {0}: {1}'?",
        "bookmark_jumped_to": "Pereita prie žymės '{0}' {1} puslapyje.",
        "bookmark_jumped_to_voice": "Žymė {0}, puslapis {1}",
        "btn_close": "Uždaryti",

        "bookmark_list": "Jūsų žymės",
        "bookmark_rename": "Pervadinti žymę",
        "bookmark_rename_tooltip": "Pakeisti pasirinktos žymės pavadinimą",
        "bookmark_rename_title": "Pervadinti žymę",
        "bookmark_rename_prompt": "Naujas pavadinimas žymei {0} puslapyje:\n(maks. 50 simbolių)",
        "bookmark_renamed": "Žymė '{0}' pervadinta į '{1}'.",
        "bookmark_item_tooltip": "Puslapis {0}: {1}\nDukart spustelėkite, kad pereitumėte",
        "bookmark_name_exists_question": "Žymė pavadinimu '{0}' jau egzistuoja šiame puslapyje.\nVis tiek pervadinti?",

        "context_bookmarks": "Žymės",
        "context_bookmark_add_here": "Pridėti žymę šiam puslapiui",
        "context_bookmarks_existing": "Esamos žymės:",
        "context_bookmarks_jump": "Pereiti prie žymės:",
        "context_bookmarks_none": "Nėra žymių",
        "context_bookmarks_clear_all": "Pašalinti visas {0} žymes",

        "bookmark_search_placeholder": "Ieškoti žymių... (pavadinimas arba puslapis)",
        "bookmark_search_results": "Rasta %d žymių, atitinkančių \"%s\"",
        "bookmark_no_search_results": "Nerasta žymių, atitinkančių \"%s\"",
        "bookmark_no_search_results_label": "Nėra rezultatų, atitinkančių \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Redaguoti PDF metaduomenis",
        "metadata_title": "Pavadinimas",
        "metadata_title_placeholder": "Dokumento pavadinimas",
        "metadata_title_tooltip": "Dokumento pavadinimas (rodomas pavadinimo juostoje)",
        "metadata_author": "Autorius",
        "metadata_author_placeholder": "Autoriaus vardas",
        "metadata_author_tooltip": "Dokumento kūrėjas",
        "metadata_subject": "Tema",
        "metadata_subject_placeholder": "Dokumento tema",
        "metadata_subject_tooltip": "Trumpas turinio aprašymas",
        "metadata_keywords": "Raktiniai žodžiai",
        "metadata_keywords_placeholder": "Raktiniai žodžiai, atskirti kableliais",
        "metadata_keywords_tooltip": "Raktiniai žodžiai dokumentui kategorizuoti",
        "metadata_creator": "Kūrėjas",
        "metadata_creator_placeholder": "Programa, kuri sukūrė PDF",
        "metadata_creator_tooltip": "Programinė įranga, su kuria dokumentas buvo sukurtas",
        "metadata_producer": "Prodiuseris",
        "metadata_producer_placeholder": "Programa, kuri konvertavo PDF",
        "metadata_producer_tooltip": "Programinė įranga, kuri konvertavo PDF",
        "metadata_creation_date": "Sukūrimo data",
        "metadata_creation_date_tooltip": "Dokumento sukūrimo data",
        "metadata_mod_date": "Modifikavimo data",
        "metadata_mod_date_tooltip": "Paskutinio modifikavimo data",
        "metadata_pdf_info": "📄 PDF informacija",
        "metadata_pages": "Puslapių skaičius",
        "metadata_file_size": "Failo dydis",
        "metadata_pdf_version": "PDF versija",
        "metadata_encrypted": "Užšifruota",
        "metadata_encrypted_yes": "Taip (apsaugota slaptažodžiu)",
        "metadata_encrypted_no": "Ne",
        "metadata_reload": "📂 Įkelti iš naujo iš PDF",
        "metadata_reset": "Atmesti pakeitimus",
        "metadata_reloaded": "Metaduomenys buvo įkelti iš naujo iš PDF.",
        "metadata_reset_done": "Visi metaduomenų laukai buvo atstatyti.",
        "metadata_no_file": "Nėra įkelta PDF failo.",
        "metadata_save_error": "Klaida išsaugant metaduomenis",
        "metadata_saved": "Metaduomenys sėkmingai išsaugoti.",
        "metadata_pdf_version_unknown": "PDF (nežinoma)",
        "metadata_saved_message": "Metaduomenys sėkmingai išsaugoti.",
        "metadata_saved_voice": "Metaduomenys išsaugoti.",

        "metadata_custom": "🔧 Individualūs metaduomenys",
        "metadata_custom_placeholder": "{\n  \"mano_laukas\": \"mano_reikšmė\",\n  \"kitas_laukas\": 123\n}",
        "metadata_custom_tooltip": "JSON formatas individualiems metaduomenims (neprivaloma)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Pasirinktas šablonas \"{0}\" - Dukart spustelėkite, kad įterptumėte",
        "text_use_template": "Naudoti teksto bloką",
        "text_type": "Tipas",
        "text_search_templates": "Ieškoti teksto blokų...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Eksportavimo / Importavimo informacija",
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

        <h3>📦 Kas eksportuojama? (Apžvalga)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Bendrieji programos nustatymai</span></li>
            <li class="detail">• Tamsus/Šviesus režimas</li>
            <li class="detail">• Tamsaus režimo inversija vaizdams</li>
            <li class="detail">• Pilkos spalvos slenkstinė reikšmė</li>
            <li class="detail">• Kalba</li>
            <li class="detail">• Lango geometrija</li>
            <li class="detail">• Mastelio keitimo režimas</li>
            <li class="detail">• Navigacija (Navigacijos juosta matoma)</li>
            <li class="detail">• Balso išvestis (įjungta/išjungta)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Atsarginės kopijos nustatymai</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Failų pavadinimų suteikimas (Laiko žyma, Skirtukas, Priesagos)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Įterpimų nustatymai</span></li>
            <li class="detail">• Parašai</li>
            <li class="detail">• Tekstas ir teksto blokai</li>
            <li class="detail">• Varnelės, vaizdai ir formos</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR nustatymai</span></li>
            <li class="detail">• Kalba</li>
            <li class="detail">• Priverstinis OCR · Puslapio režimas</li>
            <li class="detail">• Išankstinis vaizdo apdorojimas: Koreguoti pasvirimą, Išvalyti, Per didelis mėginių ėmimas</li>
            <li class="detail">• Lygiagrečių užduočių skaičius</li>
            <li class="detail">• Inversijos režimas</li>
            <li class="detail">• Pilkos spalvos slenkstinė reikšmė</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Žymės</span></li>
            <li class="detail">• Visos žymės viename PDF faile (Puslapis, Pavadinimas, Sukūrimo laikas)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Slaptažodžių duomenų bazė</span></li>
            <li class="detail">• Išsaugoti PDF slaptažodžiai (pasirinktinai užšifruoti arba paprastas tekstas)</li>
            <li class="detail">• Pagrindinio slaptažodžio maiša (jei nustatyta)</li>
            <li class="detail">• Patvirtinimo duomenys</li>
        </ul>

        <h4>⚠️ Svarbios pastabos</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Importuojant:</strong>
            <ul>
                <li><span class="warning">➜ VISI dabartiniai nustatymai bus visiškai perrašyti</span></li>
                <li>• Programą būtina paleisti iš naujo</li>
                <li>• Esami parašai, teksto blokai ir žymės bus pakeisti</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Pagrindinis slaptažodis ir eksportavimo režimas:</strong>
            <ul>
                <li>• Kai pagrindinis slaptažodis aktyvus, galite pasirinkti:</li>
                <li>  - <span style="color: #98FB98;"><strong>Iššifruota</strong></span> (slaptažodžiai yra paprastu tekstu ZIP faile)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Užšifruota</strong></span> (galima skaityti tik su pagrindiniu slaptažodžiu tikslinėje sistemoje)</li>
                <li>• Pagrindinio slaptažodžio maiša <strong>visada</strong> saugoma užšifruota</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Saugumo pranešimas:</strong>
            <ul>
                <li>• Eksportuotame ZIP faile yra jautrių duomenų (<strong>slaptažodžiai, žymės, parašai</strong>)</li>
                <li>• Laikykite jį saugiai (pvz., užšifruotoje USB laikmenoje, slaptažodžių tvarkyklėje)</li>
                <li>• Jei failas prarandamas, išsaugoti PDF slaptažodžiai prarandami negrįžtamai</li>
            </ul>
        </div>

        <h4>📁 Eksportavimo formatas</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Nustatymai išsaugomi viename ZIP faile:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Šiame ZIP faile yra visas <code>settings.json</code> (iš jūsų konfigūracijos), taip pat galimi įterpti parašų vaizdų failai ir užšifruoti slaptažodžiai.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Parašai - Vadovas",
        'signature_guide_html': """
        📝 <strong>Parašai - Trumpas vadovas</strong><br>
        <ul>
        <li>Nustatyti pagrindinį slaptažodį</li>
        <li>Konfigūruoti parašus meniu <em>Nustatymai</em> (dydis, laiko žyma, …)</li>
        <li>Įterpti <strong>DEŠINIU SPUSTELĖJIMU</strong> norimoje vietoje (pagrindinis slaptažodis reikalingas vieną kartą per sesiją)</li>
        <li>Perkelti parašą pele arba rodyklių klavišais</li>
        <li>Įterpti kelis parašus iš eilės</li>
        <li>Pritaikyti kiekvieną parašą individualiai</li>
        <li>Atmesti atskirą parašą</li>
        <li>Išsaugoti / atmesti visus parašus vienu metu</li>
        <li>Alternatyviai, galima naudoti ir meniu juostą.</li>
        </ul>
        """,
        'signature_guide_voice': "Trumpas parašų vadovas. Nustatyti pagrindinį slaptažodį. Konfigūruoti parašus nustatymuose. Įterpti dešiniu spustelėjimu.",

        'image_guide_title': "Įterpti paveikslėlius - Vadovas",
        'image_guide_html': """
        📷 <strong>Paveikslėlių įterpimas į PDF - Trumpas vadovas</strong><br>
        <ol>
        <li>Dešinysis spustelėjimas norimoje vietoje</li>
        <li><em>„Įterpti paveikslėlį“</em> → Pasirinkite paveikslėlį</li>
        <li>Pozicionuoti paveikslėlį: Vilkite pele</li>
        <li>Reguliuoti dydį: Vilkite už kampų/kraštų</li>
        <li>Išlaikyti kraštinių santykį: Klavišas <strong>[A]</strong></li>
        <li>Kiti koregavimai: Dešinysis spustelėjimas ant paveikslėlio</li>
        </ol>
        <p><strong>Patarimas:</strong> Kontekstiniame meniu galite koreguoti nustatymus.</p>
        """,
        'image_guide_voice': "Trumpas paveikslėlių vadovas. Dešinysis spustelėjimas, įterpti paveikslėlį, pasirinkti. Pozicionuoti pele, reguliuoti dydį už kampų. Kraštinių santykis klavišu A.",

        'form_guide_title': "Įterpti formas - Vadovas",
        'form_guide_html': """
        📐 <strong>Formų įterpimas į PDF - Trumpas vadovas</strong><br>
        <ol>
        <li>Pasirinkite formos tipą (stačiakampis, elipsė, linija, rodyklė)</li>
        <li>Spustelėkite vietą:
            <ul>
            <li>Stačiakampiui/elipsei: Vienas spustelėjimas pastato formą</li>
            <li>Linijai/rodyklei: Du spustelėjimai pradžios ir pabaigos taškams</li>
            </ul>
        </li>
        <li>Pozicionuoti formą: Vilkite pele</li>
        <li>Reguliuoti dydį: Vilkite už kampų/kraštų</li>
        <li>Išsaugoti formą: <strong>Enter</strong></li>
        <li>Atmesti formą: <strong>ESC</strong></li>
        <li>Kiti koregavimai: Dešinysis spustelėjimas ant formos</li>
        </ol>
        <p><strong>Patarimas:</strong> Kontekstiniame meniu galite koreguoti nustatymus.</p>
        """,
        'form_guide_voice': "Trumpas formų vadovas. Pasirinkite formos tipą. Stačiakampiui ar elipsei spustelėkite vieną kartą, linijai ar rodyklei du kartus. Pozicionuoti pele, reguliuoti dydį už kampų. Išsaugoti Enter, atmesti Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "ankstesnis",
        "btn_next_result": "kitas",
        "ocr_text_window": "OCR teksto langas",
        "bookmark_existing": "Esamos žymės",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR palyginimas Mac - Windows",
        'ocr_method_mac_win_title': "OCR skirtumai tarp Mac ir Windows",
        'ocr_method_mac_win_voice': "Mac yra geresnis",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Skirtumai tarp macOS ir Windows</strong></p>

        <p><strong>macOS (rekomenduojama)</strong></p>
        <p>Įrankis:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Rezultatas:</p>
        <ul>
        <li>Ieškomas PDF su įterptu tekstu, kuris iš esmės išlaiko originalų išdėstymą.</li>
        </ul>
        <p>Privalumai:</p>
        <ul>
        <li>Puiki teksto atpažinimo kokybė (net ir kreivuose puslapiuose).</li>
        <li>Vektorinės grafikos ir šriftų išsaugojimas.</li>
        <li>GUI eigos juosta per antrinio proceso vertinimą.</li>
        <li>Visiška kontrolė visų OCR parametrų (Deskew, Clean, Oversample, optimizavimas).</li>
        <li>Teksto paieška pasiekiama tiesiogiai pagrindiniame lange (PDF rodinyje).</li>
        </ul>
        <p>Trūkumai:</p>
        <ul>
        <li>Reikia papildomų sistemos įrankių (ocrmypdf, Ghostscript, unpaper, pngquant – įtraukta į programos paketą).</li>
        <li>Sudėtingesnis klaidų valdymas (užstrigimai, laiko pertekliai).</li>
        </ul>

        <p><strong>Windows (stabili alternatyva)</strong></p>
        <p>Įrankis:</p>
        <ul>
        <li>pytesseract (tiesioginis ryšys su Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Rezultatas:</p>
        <ul>
        <li>Ieškomas PDF, kuris vizualiai atitinka vaizdo PDF, bet yra ieškomas per skaidrų tekstą.</li>
        </ul>
        <p>Privalumai:</p>
        <ul>
        <li>Šiuo metu nė vienas neateina į galvą.</li>
        </ul>
        <p>Trūkumai:</p>
        <ul>
        <li>PDF iš esmės yra vaizdas su nematomu tekstu; sudėtingų dokumentų (stulpeliai, lentelės) išdėstymas gali šiek tiek skirtis.</li>
        <li>Nėra automatinės pakreipimo korekcijos (--deskew) ar vaizdo valymo (--clean).</li>
        <li>GUI eigos juosta atnaujinama tik apytiksliai pagal apdorotų puslapių skaičių.</li>
        <li>OCR greitis yra šiek tiek lėtesnis (nes kiekvienas puslapis apdorojamas atskirai).</li>
        <li>Teksto paieška nukreipiama į OCR teksto langą.</li>
        </ul>

        <p><strong>Panašumai</strong></p>
        <ul>
        <li>Abu metodai sukuria ieškomą PDF tame pačiame kataloge kaip ir šaltinio failas.</li>
        <li>OCR nustatymai (kalba, DPI, puslapio segmentavimo režimas, OCR variklio režimas) gali būti konfigūruojami per OCRSettingsDialog ir galioja abiejuose diegimuose.</li>
        </ul>

        <p><strong>Rekomendacija:</strong></p>
        <ul>
        <li>macOS: ocrmypdf dvejetainis failas suteikia geriausius rezultatus – Nusipirkite Mac ir naudokite versiją (PDFDarkView, skirtas Mac su Apple Silicon arba Intel lustu). OCR rezultatai yra geresni nei Windows!</li>
        <li>Windows: Naudokite pytesseract sprendimą. Jis yra stabilus ir suteikia visiškai pakankamą kokybę daugeliui dokumentų.</li>
        </ul>

        <p><strong>Svarbi pastaba:</strong></p>
        <ul>
        <li>Abi versijos yra visiškai integruotos į vartotojo sąsają – vartotojas nepastebi jokio skirtumo.</li>
        <li>Programa automatiškai nusprendžia, kurį OCR variklį naudoti, atsižvelgdama į operacinę sistemą.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Sukurti parašą (iš nuskaitymo)",
        "signature_create_title": "Pasirinkti nuskaitytą parašą (PDF/vaizdas)",
        "image_pdf_filter": "Vaizdai ir PDF",
        "signature_pdf_empty": "PDF faile nėra puslapių.",
        "signature_created_success": "Parašas sėkmingai sukurtas: {0}",
        "signature_create_error": "Klaida kuriant parašą:\n{0}",
        "rembg_missing": "rembg nėra įdiegtas.\nPrašome įdiegti: pip install rembg\nKlaida: {0}",
        "signature_name_title": "Failo pavadinimas parašui",
        "signature_name_message": "Įveskite failo pavadinimą naujam parašui (bus išsaugotas kaip PNG su skaidriu fondu):",
        "signature_name_label": "Failo pavadinimas:",
        "signature_name_voice": "Įveskite failo pavadinimą parašui",
        "signature_processing": "Apdorojama...",
        "signature_creation_title": "Kuriamas parašas",
        "signature_overwrite_warning": "Failas '{0}' jau egzistuoja. Perrašyti?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Paruošti PDF parašui",
        "signature_prepare_instruction":"Pasirinkite PDF, kuriame viename puslapyje yra nuskaitytas parašas.\n\nOptimalus atpažinimas pasiekiamas, jei:\n• Parašas juodu rašalu (tušinuku arba plonasieniu flomasteriu) ant balto popieriaus.\n• Parašas yra viršutiniame trečdalyje kitu atveju tuščio A4 puslapio.\n• PDF nuskaitytas ne mažiau kaip 300 dpi raiška.\n• Parašas yra aiškus ir ne per plonas.\n• Nėra trukdančių fono raštų ar linijų.",
        "signature_prepare_voice":"Pasirinkite PDF su nuskaitytu parašu. Atkreipkite dėmesį į gerą kokybę ir kontrastą.",
        "sig_thickness_label":"Linijos storis:",
        "sig_thickness_normal":"Normalus (plonas)",
        "sig_thickness_bold":"Storas (rekomenduojama)",
        "sig_thickness_very_bold":"Labai storas",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Pridėti GUI ir OCR kalbas - Vadovas",
        'language_guide_title': "Pridėti GUI ir OCR kalbas",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Atsisiųskite norimą vertimo failą <code>translations_xy.py</code> iš<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        ir įdėkite jį į šį katalogą:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Atidarykite savo žiniatinklio naršyklę.</li>
        <li>Eikite į: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Dešiniajame ekrano krašte ieškokite „Releases“ ir pasirinkite pažymėtą <strong>"latest"</strong>.</li>
        <li>Kitame leidimo puslapyje apačioje atsisiųskite failą <code>Source Code.zip</code>.</li>
        <li>Išskleiskite ZIP failą.</li>
        <li>Išskleistame aplanke suraskite visus reikalingus kalbos failus ir nukopijuokite juos į katalogą:<br/>
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
        "menu_watermark":"Įterpti vandens ženklą",
        "fullpage_text_watermark_title":"Tekstas kaip vandens ženklas",
        "fullpage_image_watermark_title":"Vaizdas kaip vandens ženklas",
        "filename_with_watermark":"_su_vandens_zenklu",
        "watermark_text":"Tekstas:",
        "watermark_text_placeholder":"Jūsų vandens ženklo tekstas...",
        "watermark_font_family":"Šriftas:",
        "watermark_font_size":"Šrifto dydis:",
        "watermark_format":"Formatavimas:",
        "watermark_bold":"Paryškintas",
        "watermark_italic":"Kursyvas",
        "watermark_color":"Spalva:",
        "watermark_choose_color":"Pasirinkite spalvą...",
        "watermark_opacity":"Nepermatomumas / Skaidrumas:",
        "watermark_direction":"Skaitymo kryptis:",
        "watermark_direction_l_r":"Kairė → Dešinė",
        "watermark_direction_bl_tr":"Apačioje kairėje → Viršuje dešinėje",
        "watermark_direction_tl_br":"Viršuje kairėje → Apačioje",
        "watermark_direction_b_t":"Apačioje → Viršuje",
        "watermark_direction_t_b":"Viršuje → Apačioje",
        "watermark_preview":"Peržiūra:",
        "watermark_preview_sample":"Pavyzdinis tekstas",
        "watermark_empty_text":"Įveskite tekstą.",
        "watermark_applied":"Vandens ženklas pritaikytas visiems puslapiams.",
        "watermark_saved":"Vandens ženklas išsaugotas.",
        "image_scale":"Dydis:",
        "image_preview":"Vaizdo peržiūra:",
        "no_image_selected":"Nepasirinktas joks vaizdas",
        "browse":"Naršyti...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Ištrinimai",
        "redact_add_black": "Ištrinimas (juodas)",
        "redact_add_white": "Ištrinimas (baltas / ištrinti)",
        "redact_added_black": "Pridėtas juodas ištrinimas",
        "redact_added_white": "Pridėtas baltas ištrinimas",
        "redact_apply_all": "Taikyti visus ištrinimus ir išsaugoti",
        "redact_discard_all": "Atmesti visus ištrinimus",
        "redact_discard": "Atmesti šį ištrinimą",
        "no_redactions": "Nėra ištrinimų",
        "redact_confirm_title": "Taikyti ištrinimus visam laikui",
        "redact_confirm_message": "Įspėjimas: Pažymėtos sritys bus negrįžtamai ištrintos (juoda arba balta).\nBus sukurta atsarginė kopija (jei įjungta).\n\nTęsti?",
        "redact_apply": "Taip, ištrinti dabar",
        "redact_saved": "{0} ištrinimas(-ai) sėkmingai pritaikytas(-i) ir išsaugotas(-i).",
        "redact_saved_voice": "{0} ištrinimas(-ai) pritaikytas(-i)",
        "redact_error": "Klaida ištrinimo metu",
        "filename_redacted":"_ištrinta",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Įterpti puslapių numerius',
        'page_numbers_format': 'Numerio formatas:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabiški)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romėniški mažieji)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romėniški didieji)',
        'page_numbers_format_letter': 'A, B, C ... (raidės)',
        'page_numbers_format_custom': 'Pritaikytas',
        'page_numbers_custom_pattern': 'Šablonas:',
        'page_numbers_custom_placeholder': 'pvz., "Puslapis {nummer}" arba "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Naudokite {nummer} dabartiniam puslapio numeriui ir {total} bendram skaičiui',
        'page_numbers_position': 'Padėtis:',
        'page_numbers_pos_tl': 'Viršuje kairėje',
        'page_numbers_pos_tc': 'Viršuje centre',
        'page_numbers_pos_tr': 'Viršuje dešinėje',
        'page_numbers_pos_ml': 'Viduryje kairėje',
        'page_numbers_pos_mc': 'Centruota',
        'page_numbers_pos_mr': 'Viduryje dešinėje',
        'page_numbers_pos_bl': 'Apačioje kairėje',
        'page_numbers_pos_bc': 'Apačioje centre',
        'page_numbers_pos_br': 'Apačioje dešinėje',
        'page_numbers_margins': 'Paraštės:',
        'page_numbers_margin_x': 'Horizontalus atstumas:',
        'page_numbers_margin_y': 'Vertikalus atstumas:',
        'page_numbers_range': 'Puslapių diapazonas:',
        'page_numbers_all_pages': 'Visi puslapiai',
        'page_numbers_custom_range': 'Pritaikytas diapazonas',
        'page_numbers_from': 'Nuo:',
        'page_numbers_to': 'Iki:',
        'page_numbers_progress': 'Įterpiami puslapių numeriai...',
        'page_numbers_start': 'Pradedamas puslapių numerių įterpimas...',
        'page_numbers_cancel': 'Puslapių numerių įterpimas atšauktas',
        'page_numbers_success': 'Puslapių numeriai sėkmingai pridėti.\n\nAr norite atidaryti naują PDF?\n\n{0}',
        'page_numbers_complete': 'Puslapių numeriai pridėti',
        'page_numbers_error_format': 'Klaida įterpiant puslapių numerius: {0}',
        'page_numbers_content_type': 'Turinio tipas:',
        'page_numbers_tab_simple': 'Paprastas numeris',
        'page_numbers_tab_range': 'Puslapis X iš Y',
        'page_numbers_tab_date': 'Data',
        'page_numbers_tab_custom': 'Laisvas tekstas',
        'page_numbers_range_format': 'Formatas:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Puslapis {aktuell} iš {gesamt}',
        'page_numbers_range_custom': 'Pritaikytas',
        'page_numbers_range_placeholder': 'pvz., "Puslapis {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Datos formatas:',
        'page_numbers_date_short': '2024.01.01',
        'page_numbers_date_long': '2024 m. sausio 1 d.',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Pritaikytas',
        'page_numbers_date_placeholder': 'pvz., %Y.%m.%d %H:%M',
        'page_numbers_date_position': 'Padėtis:',
        'page_numbers_date_before': 'Data prieš puslapio numerį',
        'page_numbers_date_after': 'Data po puslapio numerio',
        'page_numbers_date_only': 'Tik data (be puslapio numerio)',
        'page_numbers_custom_text': 'Pritaikytas tekstas:',
        'page_numbers_custom_placeholder_text': 'Naudokite {seite} puslapio numeriui ir {gesamt} bendram skaičiui\npvz., "Konfidencialu - Puslapis {seite}" arba "{seite} iš {gesamt}"',
        "filename_with_page_number":"_su_puslapio_numeriu",
        "filename_with_page_declaration":"_su_puslapio_deklaracija",
        "filename_with_pagenumber":"_su_puslapio_numeriu",
        "filename_with_date":"_su_data",
        "filename_with_my_page_declaration":"_su_pritaikyta_puslapio_deklaracija",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Neišsaugoti pakeitimai",
        "unsaved_changes_message_darkmode": "Yra neišsaugotų įterpimų.\nAr norite juos išsaugoti prieš perjungiant?",
        "save_and_switch": "Išsaugoti ir perjungti",
        "discard_and_switch": "Perjungti dabar",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Eksportuoti puslapius kaip vaizdus',
        'export_images_menu': 'Eksportuoti kaip vaizdus (PNG/JPEG)',
        'export_images_format': 'Vaizdo formatas:',
        'export_images_dpi': 'Rezoliucija (DPI):',
        'export_images_quality': 'JPEG kokybė:',
        'export_images_range': 'Puslapių diapazonas:',
        'export_images_all_pages': 'Visi puslapiai',
        'export_images_custom_range': 'Pritaikytas diapazonas',
        'export_images_from': 'Nuo:',
        'export_images_to': 'Iki:',
        'export_images_options': 'Parinktys:',
        'export_images_single_files': 'Kiekvienas puslapis kaip atskiras failas',
        'export_images_subfolder': 'Eksportuoti į papildomą aplanką',
        'export_images_subfolder_info': 'Į papildomą aplanką "PDFpavadinimas_vaizdai"',
        'export_images_same_folder': 'Tame pačiame aplanke kaip PDF',
        'export_images_apply_darkmode': 'Taikyti PDFDarkView nustatymus (Tamsus režimas)',
        'export_images_target_folder': 'Tikslinis aplankas:',
        'export_images_browse': 'Naršyti...',
        'export_images_preview': 'Peržiūra:',
        'export_images_preview_info': 'Pasirinkite eksporto nustatymus',
        'export_images_preview_info_detail': '{0} puslapių kaip {1}\nRezoliucija: {2} DPI\nFailo pavadinimas: {3}\n{4}',
        'export_images_select_folder': 'Pasirinkite tikslinį aplanką',
        'export_images_start': 'Pradedamas vaizdų eksportas...',
        'export_images_progress': 'Eksportuojami vaizdai...',
        'export_images_saving': 'Išsaugomas puslapis {0} iš {1}...',
        'export_images_success': 'Eksportas sėkmingas!\n\n{0} vaizdų išsaugota:\n{1}',
        'export_images_complete': 'Vaizdų eksportas baigtas',
        'export_images_open_folder': '📁 Atidaryti aplanką',
        'export_images_cancel': 'Vaizdų eksportas atšauktas',
        'export_images_error_format': 'Klaida eksportuojant vaizdus: {0}',
        'export_images_pdf2image_missing': 'Biblioteka "pdf2image" nėra įdiegta.\n\nĮdiekite ją naudodami:\npip install pdf2image\n\nJei naudojate Windows, jums taip pat reikia Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konversija ilgalaikiam archyvavimui',
        'pdfa_menu': 'PDF/A konversija (tinkama archyvavimui)',
        'pdfa_info': 'Konvertuoja PDF į PDF/A formatą.\n\nPDF/A yra specialiai sukurtas ilgalaikiam archyvavimui ir užtikrina, kad dokumentas ateityje bus rodomas teisingai.',
        'pdfa_standard': 'PDF/A standartas:',
        'pdfa_standard_select': 'Versija:',
        'pdfa_1': 'PDF/A-1 (paprastas, plačiai suderinamas)',
        'pdfa_2': 'PDF/A-2 (modernus, geresnis suspaudimas)',
        'pdfa_3': 'PDF/A-3 (naujausia versija, leidžia priedus)',
        'pdfa_standards_explanation': '📖 Standartų paaiškinimas:\n\n'
            '• PDF/A-1: Pagrindinis, suderinamas su senesnėmis sistemomis (apie 2005 m.)\n'
            '• PDF/A-2: Modernesnis, geresnis suspaudimas, skaidrumo palaikymas (apie 2011 m.)\n'
            '• PDF/A-3: Naujausia versija, leidžia įterpti failų priedus (apie 2013 m.)\n\n'
            'Rekomendacija: PDF/A-2 yra geras kompromisas tarp suderinamumo ir šiuolaikinių funkcijų.',
        'pdfa_options': 'Parinktys:',
        'pdfa_compress_enable': 'Suspausti PDF (mažesnis failas)',
        'pdfa_metadata_preserve': 'Išsaugoti metaduomenis (pavadinimą, autorių ir kt.)',
        'pdfa_target_folder': 'Tikslinis aplankas:',
        'pdfa_browse': 'Naršyti...',
        'pdfa_select_folder': 'Pasirinkite tikslinį aplanką',
        'pdfa_ocr_info_unknown': '🔍 Nepavyko patikrinti teksto turinio.',
        'pdfa_ocr_info_not_needed': '✅ Tekstas yra - OCR nereikalingas.\nPDF/A gali būti sukurtas tiesiogiai.',
        'pdfa_ocr_info_recommended': '⚠️ Nerastas pakankamas tekstas.\n\nIeškomiems PDF rekomenduojame pirmiausia paleisti OCR.\nPastaba: PDF/A veikia ir be OCR - bet tekstas nebus ieškomas.',
        'pdfa_ocr_info_error': '❌ Klaida tikrinant: {0}',
        'pdfa_start': 'Pradedama PDF/A konversija...',
        'pdfa_progress': 'PDF/A konversija vykdoma...',
        'pdfa_success': 'PDF/A konversija sėkminga!\n\nIšsaugota kaip:\n{0}\n\nAr norite atidaryti naują PDF?',
        'pdfa_complete': 'PDF/A konversija baigta',
        'pdfa_cancel': 'PDF/A konversija atšaukta',
        'pdfa_error_format': 'Klaida PDF/A konversijos metu:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Biblioteka "ocrmypdf" nėra įdiegta.\n\nĮdiekite ją naudodami:\npip install ocrmypdf',
        'btn_convert': 'Konvertuoti',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimizuoti PDF (sumažinti failo dydį)',
        'optimize_menu': 'Optimizuoti PDF (failo dydis)',
        'optimize_info': 'Sumažina PDF failo dydį naudojant įvairius optimizavimo metodus.\n\nKuo aukštesnis suspaudimo lygis, tuo mažesnis failas - su galimu vaizdų kokybės praradimu.',
        'optimize_level': 'Suspaudimo lygis:',
        'optimize_level_low': 'Žemas (greitas, nedidelis sutaupymas)',
        'optimize_level_medium': 'Vidutinis (geras kompromisas)',
        'optimize_level_high': 'Aukštas (didelis sutaupymas)',
        'optimize_level_maximum': 'Maksimalus (maksimalus sutaupymas, lėtas)',
        'optimize_level_explanation': 'Rekomendacija: "Vidutinis" yra geras kompromisas tarp greičio ir failo dydžio.',
        'optimize_options': 'Parinktys:',
        'optimize_compress_images': 'Suspausti vaizdus (sumažinti JPEG kokybę)',
        'optimize_clean_objects': 'Pašalinti nenaudojamus objektus',
        'optimize_preserve_metadata': 'Išsaugoti metaduomenis (pavadinimą, autorių ir kt.)',
        'optimize_image_quality': 'Vaizdo kokybė:',
        'optimize_range': 'Puslapių diapazonas:',
        'optimize_all_pages': 'Visi puslapiai',
        'optimize_custom_range': 'Pritaikytas diapazonas',
        'optimize_from': 'Nuo:',
        'optimize_to': 'Iki:',
        'optimize_target_folder': 'Tikslinis aplankas:',
        'optimize_browse': 'Naršyti...',
        'optimize_select_folder': 'Pasirinkite tikslinį aplanką',
        'optimize_info_box': 'Informacija',
        'optimize_info_text': 'Optimizavimas gali užtrukti kelias minutes dideliems PDF failams.\n\nVaizdai išsaugomi su sumažinta kokybe, o tai gali žymiai sumažinti failo dydį.',
        'optimize_start': 'Pradedamas PDF optimizavimas...',
        'optimize_progress': 'Optimizuojamas PDF...',
        'optimize_cancel': 'PDF optimizavimas atšauktas',
        'optimize_complete': 'PDF optimizavimas baigtas',
        'optimize_error_format': 'Klaida PDF optimizavimo metu:\n\n{0}',
        'optimize_success_message': 'PDF optimizavimas sėkmingas!\n\nIšsaugota kaip:\n{0}\n\nPrieš: {1}\nPo: {2}\nSutaupymas: {3:.1f}%\n\n{4}\n\nAr norite atidaryti optimizuotą PDF?',
        'optimize_success_message_no_size': 'PDF optimizavimas sėkmingas!\n\nIšsaugota kaip:\n{0}\n\nDydžio informacija nėra prieinama.\n\nAr norite atidaryti optimizuotą PDF?',
        'optimize_result_positive': 'Failas sumažintas {0:.1f}%.',
        'optimize_result_zero': 'Failo dydis nepakito.',
        'optimize_result_negative': 'Failas padidėjo {0:.1f}%.\nOptimizavimas praleistas, originalus failas išsaugotas.',
        'btn_optimize': 'Pradėti optimizavimą',
        'filename_optimize_low_suffix': '_optimizuotas_zemas',
        'filename_optimize_medium_suffix': '_optimizuotas',
        'filename_optimize_high_suffix': '_optimizuotas_aukstas',
        'filename_optimize_maximum_suffix': '_optimizuotas_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Apkirpti PDF',
        'crop_menu': 'Apkirpti PDF (Crop)',
        'crop_range': 'Taikyti:',
        'crop_all_pages': 'Visi puslapiai',
        'crop_current_page': 'Tik dabartinis puslapis',
        'crop_values': 'Apkirpimo reikšmės (taškais):',
        'crop_left': 'Kairė:',
        'crop_right': 'Dešinė:',
        'crop_top': 'Viršus:',
        'crop_bottom': 'Apačia:',
        'crop_presets': 'Išankstiniai nustatymai:',
        'crop_preset_white': 'Aptikti baltas paraštes',
        'crop_reset': 'Atstatyti',
        'crop_mouse_hint': '🖱️ Tempkite stačiakampį, kad apytiksliai pasirinktumėte sritį.\nTada galite tiksliai sureguliuoti reikšmes SpinBox languose.\nRankinis reguliavimas pele nėra galimas.',
        'crop_apply': 'Apkirpti',
        'crop_scope_all': 'Visi puslapiai',
        'crop_scope_current': 'Dabartinis puslapis',
        'crop_new_size': 'Naujas dydis: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Neįkeltas joks PDF',
        'crop_preview_error': 'Klaida įkeliant peržiūrą',
        'crop_start': 'Pradedamas apkirpimas...',
        'crop_progress': 'Apkirpiamas PDF...',
        'crop_success': 'PDF sėkmingai apkirstytas!\n\nIšsaugota kaip:\n{0}\n\nAr norite atidaryti apkirstytą PDF?',
        'crop_complete': 'Apkirpimas baigtas',
        'crop_cancel': 'Apkirpimas atšauktas',
        'crop_error_format': 'Klaida apkirpimo metu:\n\n{0}',
        'filename_crop_suffix': '_apkirstytas',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Išlyginti PDF (Flatten)',
        'flatten_menu': 'Išlyginti PDF (Flatten)',
        'flatten_info': 'PDF išlyginimas "įkepina" visus redaguojamus elementus į puslapio turinį.\n\nPo to formos laukai, anotacijos, tekstai, kryžiai, parašai, vaizdai ir formos nebėra atskirai redaguojami.',
        'flatten_explanation_title': '📖 Kam tai naudinga?',
        'flatten_explanation_text': 'Išlyginimas reikalingas šiais atvejais:\n\n'
            '• 📄 Norite paruošti dokumentą spausdinimui\n'
            '• 🔒 Norite užkirsti kelią, kad kas nors pakeistų formos laukus\n'
            '• 📎 Norite "įtvirtinti" anotacijas ir komentarus dokumente\n'
            '• 🖼️ Norite tvirtai įtvirtinti įterptus tekstus, kryžius, parašus, vaizdus ir formas dokumente\n'
            '• 📦 Norite paruošti failą archyvavimui\n\n'
            'Išlyginimas sumažina PDF dydį ir apsaugo nuo atsitiktinio elementų perkėlimo ar ištrynimo.',
        'flatten_what_title': 'Kas išlyginama?',
        'flatten_what_list': '• ✅ Formos laukai (teksto laukai, žymimieji langeliai, mygtukai)\n'
            '• ✅ Anotacijos (komentarai, paryškinimai, pastabos)\n'
            '• ✅ Perdangos (tekstai, kryžiai, parašai, vaizdai, formos)',
        'flatten_options': 'Parinktys:',
        'flatten_forms': 'Išlyginti formos laukus',
        'flatten_annotations': 'Išlyginti anotacijas',
        'flatten_overlays': 'Išlyginti perdangas (tekstus, kryžius, parašus, vaizdus, formas)',
        'flatten_target_folder': 'Tikslinis aplankas:',
        'flatten_browse': 'Naršyti...',
        'flatten_select_folder': 'Pasirinkite tikslinį aplanką',
        'flatten_warning': '⚠️ Svarbu: Išlyginimas yra negrįžtamas procesas!\n\nPo išlyginimo redaguojamų elementų nebegalima atskirai keisti ar trinti.\nJei reikia, prieš tai sukurkite atsarginę kopiją.',
        'flatten_apply': 'Išlyginti',
        'flatten_start': 'Pradedamas išlyginimas...',
        'flatten_progress': 'Išlyginamas PDF...',
        'flatten_success': 'PDF sėkmingai išlygintas!\n\nIšsaugota kaip:\n{0}\n\nAr norite atidaryti išlygintą PDF?',
        'flatten_complete': 'Išlyginimas baigtas',
        'flatten_cancel': 'Išlyginimas atšauktas',
        'flatten_error_format': 'Klaida išlyginimo metu:\n\n{0}',
        'filename_flatten_suffix': '_islygintas',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF perdanga (Overlay)',
        'overlay_menu': 'PDF perdanga (Overlay)',
        'overlay_info': 'Uždeda vieną PDF (perdangą) ant kito PDF.\n\nPerdangos PDF uždedamas ant pagrindinio PDF. Tai naudinga vandens ženklams, logotipams, blankams ar antspaudams.',
        'overlay_explanation_title': '📖 Kam tai naudinga?',
        'overlay_explanation_text': 'Perdanga reikalinga šiais atvejais:\n\n'
            '• 🏢 Įmonės logotipo kaip vandens ženklo uždėjimas ant kiekvieno puslapio\n'
            '• 📄 Blanko uždėjimas ant tuščio PDF\n'
            '• 🖊️ Antspaudo perdangos uždėjimas ant dokumento\n'
            '• 🔖 Vandens ženklo uždėjimas ant visų puslapių\n'
            '• 📑 Formos perdangos uždėjimas ant šablono',
        'overlay_type': 'Perdangos tipas:',
        'overlay_type_fullpage': 'Visas puslapis (dengiantis)',
        'overlay_type_transparent': 'Visas puslapis (skaidrus - rekomenduojama)',
        'overlay_type_stamp': 'Antspaudas (galima nustatyti padėtį)',
        'overlay_type_info_fullpage': '📄 Perdangos PDF uždedamas tiksliai ant viso puslapio.\nBaltą foną galima pašalinti, kad matytųsi tik turinys.',
        'overlay_type_info_transparent': '🔍 Perdangos PDF uždedamas ant viso puslapio su skaidriu fonu.\nBaltas fonas pašalinamas automatiškai - idealu vandens ženklams ir logotipams!',
        'overlay_type_info_stamp': '🖊️ Perdangos PDF nustatomas ir keičiamas kaip antspaudas.\nPuikiai tinka logotipams, antspaudams ar parašams tam tikrose vietose.',
        'overlay_remove_background': 'Pašalinti baltą foną:',
        'overlay_remove_background_enable': 'Pašalinti baltą foną iš perdangos PDF (padaro perdangą skaidrią)',
        'overlay_remove_background_tooltip': 'Pašalina baltas sritis iš perdangos PDF, kad būtų matomas apatinis tekstas.',
        'overlay_threshold': 'Slenkstinė reikšmė:',
        'overlay_threshold_hint': '(1-254, didesnė = pašalinama daugiau baltos spalvos)',
        'overlay_select_file': 'Pasirinkite perdangos PDF:',
        'overlay_file_placeholder': 'Pasirinkite PDF failą perdangai',
        'overlay_browse': 'Naršyti...',
        'overlay_select_overlay': 'Pasirinkite perdangos PDF',
        'overlay_range': 'Puslapių diapazonas:',
        'overlay_all_pages': 'Visi puslapiai',
        'overlay_custom_range': 'Pritaikytas diapazonas',
        'overlay_from': 'Nuo:',
        'overlay_to': 'Iki:',
        'overlay_position': 'Padėtis:',
        'overlay_position_center': 'Centras',
        'overlay_position_top_left': 'Viršuje kairėje',
        'overlay_position_top_right': 'Viršuje dešinėje',
        'overlay_position_bottom_left': 'Apačioje kairėje',
        'overlay_position_bottom_right': 'Apačioje dešinėje',
        'overlay_size': 'Dydis:',
        'overlay_size_original': 'Originalus dydis',
        'overlay_size_fit_page': 'Pritaikyti puslapiui',
        'overlay_size_custom': 'Pritaikytas (%)',
        'overlay_opacity': 'Skaidrumas:',
        'overlay_target_folder': 'Tikslinis aplankas:',
        'overlay_browse_folder': 'Naršyti...',
        'overlay_select_folder': 'Pasirinkite tikslinį aplanką',
        'overlay_warning': '⚠️ Pastaba: Perdangos PDF uždedamas ant pagrindinio PDF ir "įkepinamas" į jį.\n\nPerdangos PDF elementai po išsaugojimo nebegali būti atskirai redaguojami.',
        'overlay_apply': 'Perdanga',
        'overlay_start': 'Pradedama perdanga...',
        'overlay_progress': 'Uždedama PDF perdanga...',
        'overlay_success': 'PDF perdanga sėkmingai uždėta!\n\nIšsaugota kaip:\n{0}\n\nAr norite atidaryti PDF su perdanga?',
        'overlay_complete': 'Perdanga baigta',
        'overlay_cancel': 'Perdanga atšaukta',
        'overlay_error_format': 'Klaida perdangos metu:\n\n{0}',
        'overlay_no_file': 'Nepasirinktas joks perdangos PDF.\n\nPasirinkite PDF failą perdangai.',
        'filename_overlay_suffix': '_su_perdanga',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Išgauti vaizdus iš PDF',
        'extract_images_menu': 'Išgauti visus vaizdus',
        'extract_images_info': 'Išgauna visus vaizdus iš PDF ir išsaugo juos kaip atskirus failus.\n\nVaizdai išsaugomi jų originaliu formatu arba konvertuojami į pasirinktą formatą.',
        'extract_images_format': 'Vaizdo formatas:',
        'extract_images_quality': 'JPEG kokybė:',
        'extract_images_options': 'Parinktys:',
        'extract_images_subfolder': 'Išgauti į papildomą aplanką ("PDFpavadinimas_vaizdai")',
        'extract_images_unique': 'Tik unikalūs vaizdai (išvengti dublikatų)',
        'extract_images_range': 'Puslapių diapazonas:',
        'extract_images_all_pages': 'Visi puslapiai',
        'extract_images_custom_range': 'Pritaikytas diapazonas',
        'extract_images_from': 'Nuo:',
        'extract_images_to': 'Iki:',
        'extract_images_target_folder': 'Tikslinis aplankas:',
        'extract_images_browse': 'Naršyti...',
        'extract_images_select_folder': 'Pasirinkite tikslinį aplanką',
        'extract_images_info_box': 'Informacija',
        'extract_images_info_text': 'Išgavimas gali užtrukti kelias minutes dideliems PDF failams.\n\nVaizdai išsaugomi su jų originaliu pavadinimu (puslapis_vaizdas).',
        'extract_images_extract': 'Išgauti',
        'extract_images_start': 'Pradedamas išgavimas...',
        'extract_images_progress': 'Išgaunami vaizdai...',
        'extract_images_success': '✅ Vaizdai sėkmingai išgauti!\n\n{0} vaizdų išsaugota:\n{1}',
        'extract_images_complete': 'Vaizdų išgavimas baigtas',
        'extract_images_cancel': 'Išgavimas atšauktas',
        'extract_images_error_format': 'Klaida išgaunant vaizdus:\n\n{0}',
        'extract_images_open_folder': '📁 Atidaryti aplanką',
        'extract_images_no_images': 'PDF nerasta jokių vaizdų.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Keli puslapiai viename puslapyje (N-Up)',
        'nup_menu': 'Keli puslapiai viename puslapyje (N-Up)',
        'nup_info': 'Išdėsto kelis PDF puslapius viename puslapyje.\n\nIdealu kompaktiškam spausdinimui, apžvalgoms ar dalomajai medžiagai.',
        'nup_layout': 'Išdėstymas:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Peržiūra:',
        'nup_preview_info': '{0} puslapių → {1} puslapis(-iai) lape → {2} lapai\nIšdėstymas: {3}',
        'nup_order': 'Eiliškumas:',
        'nup_order_horizontal': 'Horizontalus (eilutė po eilutės)',
        'nup_order_vertical': 'Vertikalus (stulpelis po stulpelio)',
        'nup_order_horizontal_reverse': 'Horizontalus atvirkštinis',
        'nup_order_vertical_reverse': 'Vertikalus atvirkštinis',
        'nup_range': 'Puslapių diapazonas:',
        'nup_all_pages': 'Visi puslapiai',
        'nup_custom_range': 'Pritaikytas diapazonas',
        'nup_from': 'Nuo:',
        'nup_to': 'Iki:',
        'nup_options': 'Parinktys:',
        'nup_margins': 'Paraštės:',
        'nup_margin_between': 'Tarpas tarp puslapių:',
        'nup_page_numbers': 'Įterpti puslapių numerius',
        'nup_target_folder': 'Tikslinis aplankas:',
        'nup_browse': 'Naršyti...',
        'nup_select_folder': 'Pasirinkite tikslinį aplanką',
        'nup_create': 'Sukurti',
        'nup_start': 'Pradedamas N-Up...',
        'nup_progress': 'Kuriamas N-Up...',
        'nup_success': 'N-Up sėkmingai sukurtas!\n\nIšsaugota kaip:\n{0}\n\nAr norite atidaryti naują PDF?',
        'nup_complete': 'N-Up baigtas',
        'nup_cancel': 'N-Up atšauktas',
        'nup_error_format': 'Klaida N-Up metu:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Keisti puslapio dydį',
        'pagesize_menu': 'Keisti puslapio dydį',
        'pagesize_info': 'Keičia PDF puslapio dydį.\n\nTurinys automatiškai pritaikomas prie naujo dydžio.',
        'pagesize_format': 'Formatas:',
        'pagesize_select': 'Pasirinkite standartinį formatą:',
        'pagesize_custom': 'Pritaikytas dydis:',
        'pagesize_width': 'Plotis:',
        'pagesize_height': 'Aukštis:',
        'pagesize_orientation': 'Orientacija:',
        'pagesize_portrait': 'Portretas',
        'pagesize_landscape': 'Peizažas',
        'pagesize_scale_options': 'Keitimo parinktys:',
        'pagesize_fit': 'Pritaikyti (išlaikyti kraštinių santykį)',
        'pagesize_stretch': 'Ištempti (iškraipyti)',
        'pagesize_center': 'Centruoti (originalus dydis)',
        'pagesize_range': 'Puslapių diapazonas:',
        'pagesize_all_pages': 'Visi puslapiai',
        'pagesize_custom_range': 'Pritaikytas diapazonas',
        'pagesize_from': 'Nuo:',
        'pagesize_to': 'Iki:',
        'pagesize_target_folder': 'Tikslinis aplankas:',
        'pagesize_browse': 'Naršyti...',
        'pagesize_select_folder': 'Pasirinkite tikslinį aplanką',
        'pagesize_apply': 'Taikyti',
        'pagesize_start': 'Pradedamas puslapio dydžio keitimas...',
        'pagesize_progress': 'Keičiamas puslapio dydis...',
        'pagesize_success': 'Puslapio dydis sėkmingai pakeistas!\n\nIšsaugota kaip:\n{0}\n\nAr norite atidaryti naują PDF?',
        'pagesize_complete': 'Puslapio dydžio keitimas baigtas',
        'pagesize_cancel': 'Puslapio dydžio keitimas atšauktas',
        'pagesize_error_format': 'Klaida keičiant puslapio dydį:\n\n{0}',
        'pagesize_preview_info': 'Naujas dydis: {0} x {1} pt',
        'filename_pagesize_suffix': '_naujas_dydis',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF informacija',
        'pdf_info_menu': 'Rodyti PDF informaciją',
        'pdf_info_voice': 'Rodoma PDF informacija',
        'pdf_info_error': 'Klaida rodant PDF informaciją:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Rodyti klaviatūros trumpinius",
        "shortcuts_dialog_title": "Klaviatūros trumpiniai",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FAILAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Atidaryti PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Uždaryti PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Išsaugoti kaip...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Apsaugoti dokumentą</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Spausdinti</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Spausdinti iškart (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Išeiti iš programos</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORTAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Eksportuoti kaip Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Eksportuoti kaip DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Eksportuoti kaip TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Eksportuoti kaip vaizdus (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Išgauti vaizdus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTŲ APDOROJIMAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Keli puslapiai)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konversija (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Išlyginti PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF perdanga</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimizuoti PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDAGAVIMAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Ieškoti</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Pridėti žymę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Tvarkyti žymes</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Kita žymė</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Ankstesnė žymė</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Paleisti OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 PUSLAPIŲ VALDYMAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Pasukti dabartinį puslapį</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Pasukti visus puslapius</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizuoti dabartinį puslapį</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizuoti visus puslapius</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Ištrinti puslapius</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Išgauti puslapius</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Įterpti puslapius</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Perkelti puslapius</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Sujungti PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Keisti puslapio dydį</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 ĮTERPIMAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Įterpti tekstą</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Įterpti kryžių</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Įterpti parašą 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Įterpti parašą 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Įterpti vaizdą</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Įterpti stačiakampį</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Įterpti elipsę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Įterpti liniją</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Įterpti rodyklę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Įterpti puslapių numerius</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Teksto vandens ženklas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Vaizdo vandens ženklas</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ IŠTRINIMAI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Ištrinimas (juodas)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Ištrinimas (baltas)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Taikyti visus ištrinimus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ IŠPLĖSTINĖ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Apkirpti PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Redaguoti metaduomenis</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ PERŽIŪRA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Perjungti Tamsų/Šviesų režimą</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Rodyti teksto langą</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Puslapio plotis (Didinimas)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Du puslapiai (Didinimas)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Apžvalga (Didinimas)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ NUOSTATOS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Slaptažodžių valdymas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR nuostatos</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Parašo nuostatos</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Failo pavadinimo formatavimas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Eksportuoti nuostatas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importuoti nuostatas</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMACIJA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Rodyti PDF informaciją</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Įjungti/išjungti balso išvestį</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokusuoti meniu juostą</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Yra nauja versija",
        "update_available_message": "Yra nauja versija <b>{0}</b>.\n\nAplankykite išleidimo puslapį, kad atsisiųstumėte naujinį:\n{1}",
        "update_available_voice": "Yra nauja versija {0}. Atsisiųskite naujinį iš GitHub puslapio.",
        "update_open_release": "Atidaryti išleidimo puslapį",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Atsisiųsti visus vertimus",
        "ask_download_all_translations": """Be vokiečių, anglų ir vietnamiečių kalbų, yra {total_languages} kitų GUI kalbų.\n\nAr jas reikia pateikti / atnaujinti?\n\nPastaba:\nNereikalingas kalbas galite vėliau ištrinti rankiniu būdu kataloge:\n{translations_path}
        \nJei atšauksite, GUI kalbas galėsite atsisiųsti vėliau per meniu 'Įrankiai → Atnaujinti vertimus'.""",
        "menu_update_translations": "Atnaujinti vertimus",
        "translations_updated": "Vertimai atnaujinti",
        "translations_update_success": "{} vertimai sėkmingai atnaujinti ({} nauji, {} atnaujinti).",
        "translations_update_error": "Klaida atnaujinant vertimus",
        "translations_update_no_changes": "Visi vertimai jau yra naujausi.",
        "translations_update_offline": "Nėra interneto ryšio. Vertimų nepavyko atnaujinti.",
        "translations_update_in_progress": "Vertimai atnaujinami fone...",
        "translations_downloading": "Atsisiunčiami vertimai...",
        "translations_path_hint": "Naudotojo katalogas vertimams",
        "translations_update_not_available_title": "Naujinys neprieinamas",
        "translations_update_not_available_message": """Vertimų atnaujinimas prieinamas tik įdiegtoje versijoje.\n\nKūrimo režime vertimai jau yra naujausi.""",
        "translations_update_no_internet_title": "Nėra interneto ryšio",
        "translations_update_no_internet_message": """Nepavyko užmegzti interneto ryšio.\n\nVertimų negalima atsisiųsti iš GitHub.\n\nGalimi sprendimai:
        • Patikrinkite savo interneto ryšį
        • Laikinai išjunkite galimą ugniasienę
        • Bandykite dar kartą vėliau
        \nVertimus taip pat galite atsisiųsti rankiniu būdu iš GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Naujinys jau vykdomas",
        "btn_retry": "Bandyti dar kartą",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Sveiki atvykę į PDF Dark View",
        "welcome_title_not_supported": "Sveiki atvykę į PDF Dark View",
        "welcome_message": "Sveiki atvykę į PDF Dark View!\n\nJūsų sistemos kalba buvo atpažinta kaip '{language}'.\nAr norite naudoti šią kalbą vartotojo sąsajai?\n\nKalbą galite bet kada pakeisti per 'Nustatymai → Kalba'.",
        "welcome_message_language_not_available": "Sveiki atvykę į PDF Dark View!\n\nJūsų sistemos kalba buvo atpažinta kaip '{language}'.\nŠi kalba dar nėra įdiegta.\n\nAr norite dabar atsisiųsti {language} kalbos vertimus iš GitHub?\n\n(Kalba bus automatiškai naudojama vartotojo sąsajai.)",
        "welcome_message_language_not_supported": "Sveiki atvykę į PDF Dark View!\n\nJūsų sistemos kalba buvo atpažinta kaip '{language}'.\nDeja, šiai kalbai dar nėra vertimų.\n\nVartotojo sąsaja bus rodoma {fallback_language} kalba.\n\nKalbą galite bet kada pakeisti per 'Nustatymai → Kalba'.\nJei norite, galite patys prisidėti prie vertimo savo kalba:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Taip, naudoti sistemos kalbą",
        "welcome_keep_english": "Ne, palikti anglų kalbą",
        "welcome_download_language": "Taip, atsisiųsti {language}",

        # ============================================
        # 107. PASTARUOJU NAUDOTI KELIAI
        # ============================================

        'menu_recent': 'Pastaruoju naudoti',
        'menu_recent_dirs': 'Katalogai...',
        'menu_recent_files': 'Failai...',
        'recent_manage': 'Tvarkyti...',
        'recent_enable_tracking': 'Išsaugoti pastaruosius kelius (privatumas)',
        'recent_enable_info': 'Išjunkite šią parinktį, kad nebūtų išsaugomi keliai',
        'recent_tracking_disabled': 'Kelių sekimas išjungtas',
        'recent_enabled': 'įjungta',
        'recent_disabled': 'išjungta',
        'recent_tracking_status': 'Kelių sekimas {0}',
        'recent_dialog_title': 'Pastaruoju naudoti keliai',
        'recent_tab_directories': 'Katalogai',
        'recent_tab_files': 'Failai',
        'recent_dirs_instruction': 'Dukart spustelėkite, kad atidarytumėte failų dialogo langą kataloge',
        'recent_files_instruction': 'Dukart spustelėkite, kad tiesiogiai atidarytumėte PDF',
        'recent_no_directories': '(nėra išsaugotų katalogų)',
        'recent_no_files': '(nėra išsaugotų failų)',
        'recent_default_current': '⭐ Numatyta: {0}',
        'recent_set_as_default': '⭐ Nustatyti kaip numatytąjį',
        'recent_default_set_title': 'Numatytasis katalogas nustatytas',
        'recent_default_set_message': 'Katalogas "{0}" nustatytas kaip numatytasis PDF atidarymui.',
        'recent_default_set_voice': 'Numatytasis katalogas nustatytas',
        'recent_directory_not_found': 'Katalogas nerastas',
        'recent_file_not_found': 'Failas nerastas',
        'recent_remove_selected': 'Pašalinti',
        'recent_remove_title': 'Pašalinti kelią',
        'recent_remove_confirm': 'Ar tikrai norite pašalinti kelią "{0}" iš sąrašo?',
        'recent_path_removed': 'Kelias pašalintas',
        'recent_clear_all': 'Pašalinti visus',
        'recent_clear_title': 'Pašalinti visus kelius',
        'recent_clear_confirm_type': 'Ar tikrai norite ištrinti visus {0}?',
        'recent_cleared': 'Sąrašas išvalytas',
        'recent_path_not_found_title': 'Kelias nerastas',
        'recent_path_not_found_message': 'Kelias "{0}" nebeegzistuoja.',
        'recent_open_file': 'Atidaryti failą',
        'btn_open_recent': 'Atidaryti',
        'recent_open_file_question': 'Ar norite atidaryti "{0}" kaip PDF?',
        'recent_not_pdf': 'Pasirinktas failas nėra PDF.',
        'recent_more_entries': 'Daugiau įrašų...',
        'btn_remove': 'Pašalinti',
        'btn_clear': 'Išvalyti visus',
        'recent_context_open': 'Atidaryti',
        'recent_context_reveal': 'Rodyti Finder',
        'recent_context_set_default': '⭐ Nustatyti kaip numatytąjį',
        'recent_context_open_terminal': '💻 Atidaryti terminalą',
        'recent_context_file_info': 'Failo informacija',
        'recent_context_open_with_default': '📄 Atidaryti su numatytąja programa',
        'recent_context_remove': 'Pašalinti iš sąrašo',
        'recent_context_clear_all': 'Pašalinti visus',
        'recent_file_info_title': 'Failo informacija',
        'recent_file_info_name': 'Pavadinimas',
        'recent_file_info_path': 'Kelias',
        'recent_file_info_size': 'Dydis',
        'recent_file_info_modified': 'Pakeistas',
        'recent_file_info_pages': 'Puslapiai',
        'recent_error_reveal': 'Klaida atidarant Finder',
        'recent_error_terminal': 'Klaida atidarant terminalą',
        'recent_error_info': 'Klaida gaunant failo informaciją',
        'open_user_data_folder': 'Rodyti naudotojo duomenų katalogą',

        # ============================================
        # 108. LYGINIŲ/NELYGINIŲ PUSLAPIŲ TRYNIMAS
        # ============================================
        "pages_delete_even": "Ištrinti visus lyginius puslapius",
        "pages_delete_odd":  "Ištrinti visus nelyginius puslapius",
        "progress_even_pages": "Trinami lyginiai puslapiai",
        "progress_odd_pages": "Trinami nelyginiai puslapiai",
        "progress_mark_delete_even": "{} lyginiai puslapiai pažymėti trynimui",
        "progress_mark_delete_odd":  "{} nelyginiai puslapiai pažymėti trynimui",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programa uždaroma",

    }
