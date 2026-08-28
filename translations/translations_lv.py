
# ============================================
# translations_lv.py - Latviešu vārdnīca (Lettisch)
# Vollständig sortiert nach Kategorien
# ============================================

def load_latvian_strings():
    """Lädt alle lettischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Atvērt PDF",
        'btn_text_window': "OCR teksts",
        'btn_first': "Pirmā lapa",
        'btn_prev': "Iepriekšējā lapa",
        'btn_next': "Nākamā lapa",
        'btn_last': "Pēdējā lapa",
        'btn_print': "Drukāt",
        'btn_darkmode_light': "Gaišais režīms",
        'btn_darkmode_dark': "Tumšais režīms",
        'btn_delete_pages': "Dzēst lapas",
        'btn_extract_pages': "Izgūt lapas",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "Labi",
        'btn_cancel': "Atcelt",
        'btn_save': "Saglabāt",
        'btn_close': "Aizvērt",
        'btn_delete': "Dzēst",
        'btn_delete_all': "Dzēst visu",
        'btn_copy': "Kopēt",
        'btn_export': "Eksportēt",
        'btn_show': "Rādīt paroli",
        'btn_hide': "Slēpt paroli",
        'btn_authenticate': "Autentificēties",
        'btn_settings': "Iestatījumi",
        'btn_protect': "Aizsargāt",
        'btn_remove_password': "Noņemt paroli",
        'btn_manage': "Paroļu pārvaldība",
        'btn_retry': "Mēģināt vēlreiz",
        'btn_select_all': "Izvēlēties visu",
        'btn_clear_selection': "Notīrīt izvēli",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Lapa {0} no {1}",
        'page_count': "no {0}",
        'goto_page': "Pāriet uz lapu",
        'page_simple': "Lapa {0}",
        'full_view_page': "Pilns skats, lapa {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Ievadiet meklējamo vārdu + Enter",
        'search_results': "Rezultāti: {0} no {1}",
        'search_nav_hint': "Enter: nākamais (Shift+Enter: iepriekšējais) rezultāts",
        'search_no_results': "Nav rezultātu",
        'search_error': "Meklēšanas kļūda",
        'search_active': "Meklēšanas lauks aktivizēts",
        'search_closed': "Meklēšana pabeigta",
        'search_position': "Lapa {0} {1}",
        'search_pos_top': "pašā augšā",
        'search_pos_upper': "augšā",
        'search_pos_middle': "vidū",
        'search_pos_lower': "apakšā",
        'search_pos_bottom': "pašā apakšā",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Teksta atpazīšana veiksmīgi pabeigta!",
        'ocr_success_title': "OCR veiksmīgs",
        'ocr_success_message': "Dokuments tagad ir meklējams.",
        'ocr_failed': "OCR neizdevās",
        'ocr_in_progress': "OCR notiek",
        'ocr_preparing': "Sagatavo PDF...",
        'ocr_analyzing': "Analizē PDF...",
        'ocr_optimizing': "Attēla optimizācija...",
        'ocr_recognizing': "Teksta atpazīšana...",
        'ocr_embedding': "Teksta iegulšana...",
        'ocr_finalizing': "PDF pabeigšana...",
        'ocr_not_available': "OCR nav pieejams",
        'ocr_install_message': "OCR rīki netika atrasti.\n\nLūdzu, instalējiet:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Nepieciešams OCR",
        'ocr_question': "PDF nesatur meklējamu tekstu.\nVai vēlaties veikt OCR, lai iespējotu {0}?",
        'ocr_perform': "Veikt OCR",
        'ocr_later': "Vēlāk",
        'ocr_starting': "Uzsāk garantētu OCR...",
        'ocr_success_voice': "OCR veiksmīgs. PDF tagad ir meklējams.",
        'ocr_partial_success': "OCR tika veikts, bet radās problēmas ar aizstāšanu.\n\nMeklējamā versija tika saglabāta šeit:\n{0}\n\nKļūda: {1}",
        'ocr_partial_title': "OCR daļēji veiksmīgs",
        'ocr_partial_voice': "OCR veikts, bet aizstāšana neizdevās.",
        'original_file': "Oriģinālais fails:",
        'old_size': "Vecais izmērs:    {0} baiti",
        'new_size': "Jaunais izmērs: {0} baiti",
        'size_change': "Izmaiņas: {0}{1} baiti",
        'backup_created_file': "Rezerves kopija izveidota:\n{0}",
        'backup_not_created': "Rezerves kopija nav izveidota (iestatījums izslēgts)",
        'page_header': "=== Lapa {0} ===\n{1}\n",
        'scanned_page_header': "=== Lapa {0} (skenēta) ===\n[Šī lapa satur tikai skenētu tekstu]\n[Lūdzu, veiciet OCR manuāli]\n",
        'scanned_warning': "⚠️ SKENĒTS TEKSTS - NEPIECIEŠAMS OCR",
        'guaranteed_title': "Meklējams PDF izveidots",
        'guaranteed_message': "<b>Garantēta meklējama versija izveidota!</b>\n\nTā kā automātiskais OCR neizdevās, tika izveidots alternatīvs meklējams PDF:\n\n{0}\n\n<b>Šis fails satur:</b>\n• Iegūtu tekstu (ja tāds bija)\n• Norādes skenētām lapām\n• Ir pilnībā meklējams",
        'guaranteed_voice': "Garantēts meklējams PDF izveidots.",
        'instruction_title': "OCR NORĀDĪJUMI",
        'instruction_file': "Oriģinālais fails: {0}",
        'instruction_text': "Automātiskā teksta atpazīšana (OCR) neizdevās.\nLūdzu, veiciet OCR manuāli:\n\n1. AR OCRmyPDF (komandrinda):\n   ocrmypdf --force-ocr \"[FAILS]\" \"izvade.pdf\"\n\n2. AR ADOBE ACROBAT (macOS/Windows):\n   • Atveriet PDF programmā Acrobat\n   • Rīki > Rediģēt PDF\n   • Izvēlieties 'Teksta atpazīšana'\n\n3. AR PREVIEW (macOS):\n   • Atveriet PDF programmā Preview\n   • Fails > Eksportēt...\n   • Quartz filtrs: 'Samazināt faila izmēru'\n   • Aktivizējiet 'Veikt OCR'\n\n4. TIEŠSAISTES OCR PAKALPOJUMI:\n   • smallpdf.com/lv/ocr-pdf\n   • ilovepdf.com/lv/ocr-pdf\n   • adobe.com/lv/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR norādījumi izveidoti",
        'instruction_created_message': "Detalizēti norādījumi tika izveidoti:\n\n{0}\n\nIzpildiet darbības manuālam OCR.",
        'instruction_created_voice': "OCR norādījumi izveidoti.",
        'ocr_impossible': "OCR nav iespējams",
        'ocr_impossible_message': "OCR nevarēja veikt.\n\nLūdzu, apstrādājiet '{0}' manuāli ar OCR programmatūru.",
        'ocr_impossible_voice': "OCR nav iespējams. Lūdzu, apstrādājiet manuāli.",
        'emergency_title': "Ārkārtas OCR",
        'emergency_message': "Ārkārtas PDF tika izveidots:\n\n{0}\n\nLūdzu, apstrādājiet šo failu manuāli ar OCR.",
        'emergency_voice': "Ārkārtas PDF izveidots. Lūdzu, veiciet OCR manuāli.",
        'critical_error': "Kritiska kļūda",
        'critical_error_message': "OCR nevarēja palaist.\n\nRestartējiet programmu un pārbaudiet OCR instalāciju.",
        'critical_error_voice': "Kritiska OCR kļūda",
        'ocr_question_html': "<p>PDF nesatur meklējamu tekstu.<p>Vai vēlaties veikt OCR, lai iespējotu <b>{0}</b>?</p>",
        'ocr_question_voice': "Nepieciešams OCR. PDF nesatur meklējamu tekstu. Vai vēlaties veikt OCR, lai iespējotu {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "nav ielādēts PDF",
        'no_pdf_message': "Nav ielādēts neviens PDF",
        'pdf_not_found': "PDF fails nav atrasts",
        'file_size': "Faila izmērs",
        'bytes': "baiti",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Rezerves kopija izveidota",
        'backup_disabled': "Rezerves kopija izslēgta",
        'backup_activated': "Rezerves kopijas izveide ieslēgta",
        'backup_deactivated': "Rezerves kopijas izveide izslēgta",
        'backup_status': "Rezerves kopija: {0}",
        'backup_on': "✔ ieslēgta",
        'backup_off': "✘ izslēgta",
        'close_pdf': "Aizver PDF: {0}",
        'pdf_not_found_format': "PDF fails nav atrasts: {0}",
        'error_pdf_load_format': "Kļūda, ielādējot PDF: {0}",
        'load_failed_format': "Ielāde neizdevās:\n{0}",
        'decrypted_suffix': "(atšifrēts)",
        'decryption_failed': "Atšifrēšana neizdevās.",
        'decryption_error': "Kļūda atšifrēšanā",
        'decryption_success': "Veiksmīgi atšifrēts",
        'decryption_success_message': "PDF tika atšifrēts un saglabāts šeit:\n\n{0}",
        'decryption_success_voice': "PDF tika atšifrēts un saglabāts.",
        'password_remove_error': "Kļūda, noņemot paroli",
        'save_unencrypted': "Saglabāt nešifrētu PDF kā",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Saglabāt kā...",
        'save_copy': "Saglabāt kopiju",
        'save_success': "PDF saglabāts šeit: {0}",
        'save_encrypted': "Aizsargāts PDF saglabāts šeit: {0}",
        'save_error': "PDF nevarēja saglabāt",
        'encryption_question': "Vai vēlaties aizsargāt PDF ar paroli?",
        'encryption_yes': "Jā",
        'encryption_no': "Nē",
        'encryption_cancel': "Atcelt",
        'save_cancel': "Saglabāšana atcelta",
        'save_encrypted_voice': "Fails šifrēts un saglabāts.",
        'save_success_voice': "PDF fails tika saglabāts nešifrēts.",
        'save_error_format': "PDF nevarēja saglabāt:\n{0}",
        'export_pages_success': "Eksports uz Pages veiksmīgs",
        'export_pages_error': "Eksports uz Pages neizdevās",
        'export_pages_error_format': "Eksports uz Pages neizdevās: {0}",
        'export_word_success': "Eksports uz Word veiksmīgs",
        'export_word_error': "Eksports uz Word neizdevās",
        'export_word_error_format': "Eksports uz Word neizdevās: {0}",
        'export_text_success': "Teksta eksports veiksmīgs",
        'export_text_error': "Teksta eksports neizdevās",
        'export_text_error_format': "Teksta eksports neizdevās: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Nepieciešama parole",
        'password_enter': "Lūdzu, ievadiet paroli",
        'password_confirm': "Apstipriniet paroli",
        'password_new': "Jauna parole",
        'password_current': "Pašreizējā parole",
        'password_save': "Saglabāt paroli (šifrētu)",
        'password_saved': "✓ Parole šim failam ir saglabāta",
        'password_wrong': "Nepareiza parole",
        'password_mismatch': "Paroles nesakrīt",
        'password_too_short': "Parole ir pārāk īsa",
        'password_min_length': "Parolei jābūt vismaz 4 rakstzīmes garai",
        'password_strength': "Paroles stiprums",
        'password_strength_very_weak': "Ļoti vāja",
        'password_strength_weak': "Vāja",
        'password_strength_medium': "Vidēja",
        'password_strength_strong': "Stipra",
        'password_strength_very_strong': "Ļoti stipra",
        'password_char_count': "({0} rakstzīmes)",
        'password_match': "✓ Sakrīt",
        'password_no_match': "✗ Paroles nesakrīt",
        'password_show': "Rādīt",
        'password_hide': "Slēpt",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Paroļu pārvaldība",
        'password_table_filename': "Faila nosaukums",
        'password_table_password': "Parole",
        'password_count': "{0} saglabātas paroles",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Nav saglabātu paroļu",
        'password_copied': "{0} paroles nokopētas",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Vai tiešām vēlaties dzēst paroli failam '{0}'?",
        'password_delete_multiple': "Vai tiešām vēlaties dzēst {0} izvēlētās paroles?",
        'password_delete_all_confirm': "Vai tiešām vēlaties dzēst visas {0} saglabātās paroles?",
        'password_deleted': "{0} paroles dzēstas",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Visas paroles dzēstas",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Paroļu ģenerators",
        'generator_generated': "Ģenerētā parole:",
        'generator_regenerate': "Ģenerēt no jauna",
        'generator_copy': "Kopēt",
        'generator_use': "Izmantot",
        'generator_settings': "Iestatījumi",
        'generator_length': "Garums:",
        'generator_group_every': "Atdalītājs ik pēc",
        'generator_group_chars': "rakstzīmēm.    Atdalītājs:",
        'generator_uppercase': "Lielie burti (A-Z)",
        'generator_lowercase': "Mazie burti (a-z)",
        'generator_digits': "Cipari (0-9)",
        'generator_symbols': "Speciālās rakstzīmes (!@#$%^&*)",
        'generator_exclude': "Izslēgtās:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Nepieciešama galvenā parole",
        'master_password_setup': "Iestatīt galveno paroli",
        'master_password_change': "Mainīt galveno paroli",
        'master_password_enter': "Lūdzu, ievadiet savu galveno paroli",
        'master_password_choose': "Izvēlieties spēcīgu galveno paroli (vismaz 8 rakstzīmes)",
        'master_password_new': "Lūdzu, ievadiet savu jauno galveno paroli",
        'master_password_confirm': "Apstipriniet paroli",
        'master_password_authenticate': "Autentificēties",
        'master_password_success': "Galvenā parole veiksmīgi iestatīta.",
        'master_password_changed': "Galvenā parole veiksmīgi mainīta.",
        'master_password_removed': "Galvenā parole un visas paroles tika dzēstas.",
        'master_password_remove': "Noņemt galveno paroli",
        'master_password_remove_confirm': "Vai esat PILNĪGI PĀRLIECINĀTS, ka vēlaties dzēst VISAS paroles?\n\nŠī darbība ir NEATGRIEZENISKA!",
        'master_password_export_before': "Vai vēlaties pirms tam eksportēt rezerves kopiju?",
        'master_password_export_delete': "Eksportēt un dzēst",
        'master_password_delete_now': "Dzēst tūlīt",
        'master_password_for_signatures': "Lai izmantotu parakstus, jums ir jāiestata galvenā parole.\n\nVai vēlaties tagad iestatīt galveno paroli?",
        'master_password_for_private': "Lai izmantotu privātos teksta blokus, jums ir jāiestata galvenā parole.\n\nVai vēlaties tagad iestatīt galveno paroli?",
        'master_password_info': """
            <b>🔐 BEZ GALVENĀS PAROLES:</b><br>
            • Nav iespējams rādīt, kopēt un eksportēt paroles<br>
            • Paroļu dzēšana vienmēr ir iespējama (arī bez galvenās paroles)<br><br>

            <b>🔐 AR GALVENO PAROLI:</b><br>
            • Visas funkcijas pieejamas pēc autentifikācijas<br>
            • Paroles tiek šifrētas ar galveno paroli<br>
            • Minimālais garums: 8 rakstzīmes<br>
            • Droša SHA-256 hash glabāšana<br><br>

            <b>SVARĪGI:</b><br>
            • Ja pazaudējat galveno paroli, paroles nav atjaunojamas<br>
            • Noņemot galveno paroli, VISAS paroles tiek dzēstas<br>
            • Pirms dzēšanas ir pieejama eksportēšanas iespēja<br>
            • Galveno paroli var mainīt jebkurā laikā
        """,
        'signature_auth_disabled': "Izslēgt paroles pieprasījumu parakstiem",
        'template_auth_disabled': "Izslēgt paroles pieprasījumu privātiem teksta blokiem",
        'master_password_for_signatures_settings': "Lai izmantotu parakstus, jums ir jāiestata galvenā parole.\n\nDodieties uz Iestatījumi - Paroļu pārvaldība",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Aizsargāt PDF",
        'protect_info': "Fails '{0}' tiks aizsargāts ar paroli.",
        'protect_instruction': "Lūdzu, ievadiet vēlamo paroli divreiz, lai aizsargātu dokumentu, vai izmantojiet paroļu ģeneratoru pa labi no ievades lauka.",
        'protect_success': "PDF tika veiksmīgi aizsargāts un saglabāts šeit:\n{0}\n\nParole: {1}\n\nVai vēlaties tagad atvērt aizsargāto PDF?",
        'protect_open': "Jā",
        'protect_skip': "Nē",
        'protect_error': "Kļūda, aizsargājot PDF",
        'protect_open_title': "atvērt aizsargāto PDF",
        'protect_question': "Pabeigts. Vai vēlaties tagad atvērt aizsargāto PDF? Jā vai Nē?",
        'password_cancel': "Paroles dialogs atcelts",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Dzēst lapas",
        'pages_extract': "Izgūt lapas",
        'pages_insert': "Ievietot lapas",
        'pages_move': "Pārvietot lapas",
        'pages_delete_options': "Dzēšanas opcijas",
        'pages_delete_empty': "Dzēst visas tukšās lapas",
        'pages_delete_current': "Dzēst pašreizējo lapu",
        'pages_delete_range': "Dzēst lapu diapazonu",
        'pages_extract_options': "Izgūšanas opcijas",
        'pages_extract_current': "Izgūt pašreizējo lapu",
        'pages_extract_range': "Izgūt lapu diapazonu",
        'pages_insert_position': "Ievietošanas vieta",
        'pages_insert_before': "Ievietot pirms lapas:",
        'pages_insert_select': "Izvēlēties PDF",
        'pages_insert_none': "Nav izvēlēts PDF",
        'pages_move_source': "Pārvietojamās lapas",
        'pages_move_from': "No lapas:",
        'pages_move_to': "Līdz lapai:",
        'pages_move_target': "Mērķa pozīcija",
        'pages_move_before': "Pārvietot pirms lapas:",
        'pages_move_hint': "Piezīme: 1. lapa = sākums, {0} = beigas",
        'pages_range_invalid': "Sākuma lapai jābūt mazākai vai vienādai ar beigu lapu.",
        'pages_position_invalid': "Mērķa pozīcija nedrīkst atrasties pārvietojamajā diapazonā.",
        'pages_no_pdf_selected': "Nav izvēlēts neviens PDF.",
        'pages_deleted': "Tika dzēstas {0} lapas.",
        'pages_extracted': "Izgūts: {0}\nSaglabāts šeit: {1}\nFaila izmērs: {2:.1f} KB",
        'pages_inserted': "Ievietotas {0} lapas",
        'pages_moved': "Tika pārvietotas {0} lapas.",
        'pages_deleted_none': "Neviena lapa netika dzēsta.",
        'pages_delete_progress': "Dzēš lapas...",
        'pages_deleted_with_backup': "Tika dzēstas {0} lapas.\n\nRezerves kopija: {1}",
        'pages_deleted_voice': "Tika izveidota rezerves kopija un dzēstas {0} lapas.",
        'info': "Informācija",
        'error_dialog_creation': "Dialogu nevarēja izveidot",
        'extract_page_single': "Izgūt lapu {0}",
        'extract_page_range': "Izgūt lapas {0}-{1}",
        'extract_success_voice': "Lapas veiksmīgi izgūtas",
        'extract_error_format': "Kļūda, izgūstot: {0}",
        'pages_inserted_voice': "Tika ievietotas {0} lapas.",
        'insert_error_format': "Kļūda, ievietojot: {0}",
        'pages_move_progress': "Pārvieto lapas...",
        'pages_moved_with_backup': "Tika pārvietotas {0} lapas.\n\nRezerves kopija: {1}",
        'move_success_title': "Veiksmīgi pārvietots",
        'pages_moved_voice': "{0} lapas veiksmīgi pārvietotas",
        'mark_removed': "Lapas {0} atzīme noņemta",
        'mark_empty': "Lapa {0} atzīmēta kā tukša",
        'mark_export_removed': "Lapas {0} eksporta atzīme noņemta",
        'mark_export': "Lapa {0} atzīmēta eksportam",
        'no_empty_pages': "Nav atzīmētu tukšu lapu dzēšanai",
        'delete_empty_confirm': "Vai vēlaties dzēst visas {0} atzīmētās tukšās lapas?",
        'delete_empty_confirm_voice': "Vai tagad dzēst visas {0} atzīmētās tukšās lapas? Jā vai Nē.",
        'empty_pages_deleted': "{0} tukšas lapas dzēstas",
        'no_export_pages': "Nav atzīmētu lapu eksportam",
        'overwrite_title': "Pārrakstīt esošo failu",
        'overwrite_question': "Fails\n\n{0}\n\njau pastāv.\nVai vēlaties to pārrakstīt?",
        'overwrite_voice': "Vai pārrakstīt esošo failu? Jā vai Nē.",
        'page_skipped': "Lapa {0} tika izlaista",
        'export_complete': "Eksports pabeigts.",
        'export_complete_voice': "Eksports ir pabeigts.",
        'no_pages_exported': "Neviena lapa netika eksportēta",
        'export_cancelled': "Eksports atcelts",
        'pages_exported': "{0} lapas eksportētas uz {1}",
        'export_page_title': "Eksportēt lapu",
        'page_exported': "Lapa {0} eksportēta uz {1}",
        'export_error': "Kļūda eksportēšanā",
        'export_marked_title': "Eksportēt atzīmētās lapas",
        'rotate_all_title': "pagriezt visas lapas",
        'rotate_all_question': "Vai vēlaties pagriezt visas lapas par 90 grādiem pa labi?",
        'rotate_all_voice': "Vai vēlaties pagriezt visas lapas par 90 grādiem pa labi? Jā vai Nē?",
        'all_pages_rotated': "Visas lapas pagrieztas",
        'page_rotated': "Lapa {0} pagriezta",
        'rotate_error': "Lapu nevarēja pagriezt",
        'delete_page_confirm': "Vai vēlaties dzēst lapu {0}?",
        'delete_page_confirm_voice': "Vai tiešām vēlaties dzēst lapu {0}? Jā vai Nē.",
        'page_deleted': "Lapa {0} dzēsta",
        'delete_error': "Lapu nevarēja dzēst",
        'pages_deleted_voice': "{0} lapas dzēstas",
        'pages_exported_split': "{0} lapas tika veiksmīgi eksportētas.",
        'pages_skipped': "{0} lapas tika izlaistas.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Izgūt lapas (paplašināti)",
        'pdf_splitter_title': "PDF dalītājs un izgūtājs",
        'pdf_splitter_load': " Izvēlēties PDF failu",
        'pdf_splitter_info': "Lūdzu, izvēlieties opciju savam PDF dokumentam",
        'pdf_splitter_basic': "Pamatoperācijas",
        'pdf_splitter_single': "Sadalīt atsevišķās lapās",
        'pdf_splitter_range': "Izgūt lapas:",
        'pdf_splitter_range_placeholder': "piem., 1-3,5,7-9",
        'pdf_splitter_clean': "Tīrīšanas operācijas",
        'pdf_splitter_remove_empty': "Noņemt visas tukšās lapas",
        'pdf_splitter_remove': "Dzēst lapu diapazonu:",
        'pdf_splitter_remove_placeholder': "piem., 2,4-6",
        'pdf_splitter_process': "Apstrādāt PDF",
        'pdf_splitter_loaded': "PDF ielādēts. Lūdzu, izvēlieties opciju",
        'pdf_read_error': "PDF nevarēja nolasīt",
        'pages': "Lapas",
        'pages_created': "Lapas izveidotas",
        'range_empty': "Lūdzu, ievadiet lapu diapazonu",
        'range_invalid': "Nederīgs lapu diapazons",
        'range_created': "Tika izveidots jauns PDF ar izvēlētajām lapām:\n{0}",
        'empty_removed': "{0} tukšas lapas noņemtas.\nIzvade: {1}",
        'remove_empty': "Lūdzu, ievadiet lapas, ko noņemt",
        'remove_invalid': "Nederīgas lapas noņemšanai",
        'remove_done': "Iztīrīts PDF izveidots:\n{0}",
        'open_folder': "Atvērt mapi",
        'show_in_finder': "Rādīt Finderī",
        'pdf_splitter_no_pdf': "Lūdzu, vispirms ielādējiet PDF failu.",
        'process_error': "Kļūda, apstrādājot PDF",
        'pages_created_voice': "{0} lapas izveidotas",
        'range_created_voice': "PDF ar izvēlētajām lapām izveidots",
        'empty_removed_voice': "{0} tukšas lapas noņemtas",
        'remove_done_voice': "Iztīrīts PDF izveidots",
        'pdf_splitter_split_groups': "Katru nepārtrauktu grupu atsevišķā failā",
        'range_created_single': "Jauns PDF izveidots:\n{0}",
        'range_created_multiple': "Izveidoti {0} PDF faili.",
        'range_created_voice_single': "Izveidots viens PDF ar izvēlētajām lapām",
        'range_created_voice_multiple': "Izveidoti {0} PDF faili",
        'empty_removed_none_left': "Nav palikušas lapas",
        'empty_removed_all_empty': "Visas lapas tika atpazītas kā tukšas un tiktu noņemtas. Netika izveidots neviens fails.",
        'preview_single': "Priekšskatījums: {0}",
        'preview_enter_range': "Lūdzu, ievadiet lapu diapazonu.",
        'preview_invalid_range': "Nederīgs lapu diapazons.",
        'preview_file': "Priekšskatījums: {0}",
        'preview_files': "Priekšskatījums: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Uzsāk drukāšanu",
        'print_sent': "Drukāšanas uzdevums nosūtīts",
        'print_now': "Drukāt tūlīt",
        'print_error': "Kļūda tūlītējā drukāšanā",
        'print_limited': "Drukāšanas funkcija šajā sistēmā ir ierobežota",
        'print_error_format': "Kļūda tūlītējā drukāšanā: {0}",
        'warning': "Brīdinājums",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Pārslēgties uz gaišo režīmu",
        'mode_switch_to_dark': "Pārslēgties uz tumšo režīmu",
        'mode_dark_activated': "Tumšais režīms aktivizēts",
        'mode_light_activated': "Gaišais režīms aktivizēts",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Pilns skats",
        'zoom_two_pages': "Divas lapas blakus",
        'zoom_overview': "Pārskata režīms",
        'zoom_cannot_during_search': "Tālummaiņa nav iespējama meklēšanas laikā",
        'zoom_exit_first': "Lūdzu, vispirms iziet no tālummaiņas",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Velc un met ieslēgts",
        'drag_disabled': "Velc un met izslēgts",
        'drag_page_grab': "Lapa {0} satverta",
        'drag_page_dropped': "Lapa {0} ievietota pozīcijā {1}",
        'drag_position_invalid': "Nederīga pozīcija",
        'drag_same_position': "Lapa {0} paliek pozīcijā {0}",
        'drag_error': "Kļūda pārvietošanā",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Teksta ievade ar paplašinātu formatējumu un teksta bloku pārvaldību",
        'text_templates': "Pieejamie teksta bloki:",
        'text_name': "Nosaukums",
        'text_preview': "Teksta priekšskatījums",
        'text_enter': "Teksts:",
        'text_font_size': "Fonta lielums:",
        'text_formatting': "Formatējums:",
        'text_bold': "Treknraksts",
        'text_italic': "Slīpraksts",
        'text_underline': "Pasvītrots",
        'text_alignment': "Izlīdzinājums:",
        'text_left': "Pa kreisi",
        'text_center': "Centrēts",
        'text_right': "Pa labi",
        'text_color': "Teksta krāsa:",
        'text_opacity': "Necaurredzamība:",
        'text_word_wrap': "Rindiņu pārnese:",
        'text_auto': "Automātiski",
        'text_page_width_95': "Lapas platums (95%)",
        'text_page_width_85': "Ļoti plats (85%)",
        'text_page_width_75': "Platāks (75%)",
        'text_page_width_60': "Plats (60%)",
        'text_page_width_50': "Vidējs (50%)",
        'text_page_width_30': "Šaurs (30%)",
        'text_page_width_20': "Šaurāks (20%)",
        'text_page_width_10': "Ļoti šaurs (10%)",
        'text_no_wrap': "Bez pārneses",
        'text_private': "Privāts teksta bloks (nepieciešama autentifikācija)",
        'text_preview_label': "Priekšskatījums:",
        'text_preview_placeholder': "Šeit tiks parādīts teksta priekšskatījums...",
        'text_no_text': "(Nav teksta)",
        'text_save_template': "💾 Saglabāt kā bloku",
        'text_delete_template': "🗑 Dzēst izvēlēto teksta bloku",
        'text_show_private': "Rādīt privātos",
        'text_hide_private': "Slēpt privātos",
        'text_use': "✅ Izmantot tekstu",
        'text_saved': "Teksta bloks saglabāts kā:\n{0}",
        'text_saved_voice': "Teksta bloks saglabāts",
        'text_deleted': "Teksta bloks dzēsts",
        'text_no_text_to_save': "Nav teksta, ko saglabāt.",
        'text_no_templates': "Nav atrasts neviens teksta bloks",
        'text_private_master_required': "Privātos blokus var izmantot tikai tad, ja ir iestatīta galvenā parole.\n\nVai vēlaties tagad iestatīt galveno paroli?",
        'text_filename': "Faila nosaukums teksta blokam (bez 'Text_' un '.txt'):",
        'text_filename_hint': "Piemērs: 'Telefons MājasBirojs' tiks saglabāts kā 'Text_Telefons MājasBirojs.txt'",
        'text_save_hint': "Teksta bloks tiks automātiski saglabāts ar formatējumu.",
        'text_guide_title': "Teksta ievade – Rokasgrāmata",
        'text_delete_confirm': "Vai tiešām vēlaties dzēst teksta bloku?\n\nFails: {0}\nTeksts: {1}...",
        'text_make_public': "Atzīmēt kā publisku",
        'text_make_private': "Atzīmēt kā privātu",
        'text_privacy_changed': "Privātuma statuss mainīts",
        'text_private_always': "Privātie vienmēr redzami (iestatījums)",
        'text_mode_required': "Lūdzu, vispirms ieslēdziet teksta režīmu",
        'text_continue_editing': "Turpināt rediģēšanu – kursors teksta beigās",
        'text_no_input': "Nav ievadīts teksts – teksts atmests",
        'save_dialog_question': "Kā vēlaties turpināt?",
        'text_save_question': "Vai saglabāt visus tekstus un krustiņus, pielāgot, turpināt rediģēšanu vai atmest?",
        'copy_cross': "Krustiņš nokopēts",
        'paste_cross': "Krustiņš ievietots",
        'paste_text': "Teksts ievietots",
        'cross_discarded': "Krustiņš atmests",
        'all_discarded': "Viss atmests",
        'text_discarded': "Teksts atmests",
        'no_texts_to_save': "Nav tekstu, ko saglabāt",
        'no_valid_texts': "Nav derīgu tekstu, ko saglabāt",
        'text_word_singular': "teksts",
        'text_word_plural': "teksti",
        'cross_word_singular': "krustiņš",
        'cross_word_plural': "krustiņi",
        'texts_saved_title': "Teksti saglabāti",
        'texts_crosses_saved': "{0} {1} un {2} {3} tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'texts_crosses_saved_voice': "{0} {1} un {2} {3} saglabāti.",
        'texts_saved': "{0} {1} tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'texts_saved_voice': "{0} {1} saglabāti.",
        'crosses_saved': "{0} {1} tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'crosses_saved_voice': "{0} {1} saglabāti.",
        'elements_saved': "{0} elementi tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'elements_saved_voice': "{0} elementi saglabāti.",
        'text_window_load_error': "Teksta logu nevarēja ielādēt",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Teksta ievade un teksta bloki – Detalizēta rokasgrāmata**

        **1. Teksta ievietošana un rediģēšana**
        - Ar peles labo pogu noklikšķiniet vēlamajā vietā dokumentā un izvēlieties "Ievietot tekstu".
        - Atvērsies dialogs, kurā varat ievadīt un formatēt tekstu:
        • Fonta lielums, treknraksts, slīpraksts, pasvītrojums
        • Teksta krāsa (brīvi izvēlama)
        • Caurspīdīgums (necaurredzamība) ar slīdni
        • Rindiņu pārnese (dažādi platumi, piem., lapas platums, šaurs, bez pārneses)
        - Pēc apstiprinājuma teksts parādīsies klikšķa vietā. To var pārvietot ar peli vai bultiņtaustiņiem.
        - Dubultklikšķis uz teksta atver rediģēšanas režīmu; ESC to aizver.

        **2. Teksta bloku (veidņu) pārvaldība**
        - Teksta dialoga kreisajā pusē redzat visu saglabāto teksta bloku sarakstu.
        - **Bloka saglabāšana:** Ievadiet tekstu, noformējiet to un noklikšķiniet uz "💾 Saglabāt kā bloku". Ievadiet faila nosaukumu (bez paplašinājuma).
        - **Bloka ielāde:** Noklikšķiniet uz vēlamā nosaukuma sarakstā. Teksts un formatējums tiks pārņemts un vajadzības gadījumā pielāgots.
        - **Dzēšana:** Ar peles labo pogu noklikšķiniet uz bloka, lai to dzēstu vai mainītu tā privātuma statusu.

        **3. Privātie teksta bloki (galvenā parole)**
        - Ja esat iestatījis galveno paroli (sadaļā Iestatījumi → Paroļu pārvaldība), varat atzīmēt blokus kā "privātus".
        - Pirms saglabāšanas atzīmējiet izvēles rūtiņu "Privāts teksta bloks" dialogā.
        - Privātie bloki tiek rādīti sarakstā tikai tad, ja esat vienu reizi sesijas laikā ievadījis savu galveno paroli (autentifikācija, izmantojot atslēgas ikonu vai pirmo piekļuvi).
        - Tādējādi varat aizsargāt konfidenciālus teksta blokus no nesankcionētas piekļuves.

        **4. Krustiņu ievietošana**
        - Izmantojot kontekstizvēlni, varat ievietot arī grafisku krustiņu (piem., atzīmēšanas rūtiņām).
        - Krustiņu izmēru, līnijas biezumu un krāsu var globāli pielāgot iestatījumos (izvēlne "Iestatījumi" → "Krustiņu iestatījumi").
        - Ar peles labo pogu noklikšķiniet uz esoša krustiņa, lai to individuāli mainītu.

        **5. Grupu darbības**
        - Ja vienā lapā esat ievietojis vairākus tekstus vai krustiņus, varat tos visus vienlaikus saglabāt vai atmest no kontekstizvēlnes (peles labā poga teksta režīmā).
        - Saglabājot, visi elementi tiek iestrādāti PDF un paliek kā vektorgrafika.

        **6. Tastatūras īsceļi teksta režīmā**
        - Bultiņtaustiņi: elementa pārvietošana
        - Ctrl+bultiņtaustiņi: lielāki soļi
        - Enter: saglabāšanas dialoga atvēršana (saglabāt visu / pielāgot / atmest)
        - ESC: pašreizējā elementa atmešana
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Teksta ievade un teksta bloki – Detalizēta rokasgrāmata</strong></p>

        <p><strong>1. Teksta ievietošana un rediģēšana</strong></p>
        <ul>
        <li>Ar peles labo pogu noklikšķiniet vēlamajā vietā dokumentā un izvēlieties "Ievietot tekstu".</li>
        <li>Atvērsies dialogs, kurā varat ievadīt un formatēt tekstu:<br/>
        • Fonta lielums, treknraksts, slīpraksts, pasvītrojums<br/>
        • Teksta krāsa (brīvi izvēlama)<br/>
        • Caurspīdīgums (necaurredzamība) ar slīdni<br/>
        • Rindiņu pārnese (dažādi platumi, piem., lapas platums, šaurs, bez pārneses)</li>
        <li>Pēc apstiprinājuma teksts parādīsies klikšķa vietā. To var pārvietot ar peli vai bultiņtaustiņiem.</li>
        <li>Dubultklikšķis uz teksta atver rediģēšanas režīmu; ESC to aizver.</li>
        </ul>

        <p><strong>2. Teksta bloku (veidņu) pārvaldība</strong></p>
        <ul>
        <li>Teksta dialoga kreisajā pusē redzat visu saglabāto teksta bloku sarakstu.</li>
        <li><strong>Bloka saglabāšana:</strong> Ievadiet tekstu, noformējiet to un noklikšķiniet uz "💾 Saglabāt kā bloku". Ievadiet faila nosaukumu (bez paplašinājuma).</li>
        <li><strong>Bloka ielāde:</strong> Noklikšķiniet uz vēlamā nosaukuma sarakstā. Teksts un formatējums tiks pārņemts un vajadzības gadījumā pielāgots.</li>
        <li><strong>Dzēšana:</strong> Ar peles labo pogu noklikšķiniet uz bloka, lai to dzēstu vai mainītu tā privātuma statusu.</li>
        </ul>

        <p><strong>3. Privātie teksta bloki (galvenā parole)</strong></p>
        <ul>
        <li>Ja esat iestatījis galveno paroli (sadaļā Iestatījumi → Paroļu pārvaldība), varat atzīmēt blokus kā "privātus".</li>
        <li>Pirms saglabāšanas atzīmējiet izvēles rūtiņu "Privāts teksta bloks" dialogā.</li>
        <li>Privātie bloki tiek rādīti sarakstā tikai tad, ja esat vienu reizi sesijas laikā ievadījis savu galveno paroli (autentifikācija, izmantojot atslēgas ikonu vai pirmo piekļuvi).</li>
        <li>Tādējādi varat aizsargāt konfidenciālus teksta blokus no nesankcionētas piekļuves.</li>
        </ul>

        <p><strong>4. Krustiņu ievietošana</strong></p>
        <ul>
        <li>Izmantojot kontekstizvēlni, varat ievietot arī grafisku krustiņu (piem., atzīmēšanas rūtiņām).</li>
        <li>Krustiņu izmēru, līnijas biezumu un krāsu var globāli pielāgot iestatījumos (izvēlne "Iestatījumi" → "Krustiņu iestatījumi").</li>
        <li>Ar peles labo pogu noklikšķiniet uz esoša krustiņa, lai to individuāli mainītu.</li>
        </ul>

        <p><strong>5. Grupu darbības</strong></p>
        <ul>
        <li>Ja vienā lapā esat ievietojis vairākus tekstus vai krustiņus, varat tos visus vienlaikus saglabāt vai atmest no kontekstizvēlnes (peles labā poga teksta režīmā).</li>
        <li>Saglabājot, visi elementi tiek iestrādāti PDF un paliek kā vektorgrafika.</li>
        </ul>

        <p><strong>6. Tastatūras īsceļi teksta režīmā</strong></p>
        <ul>
        <li>Bultiņtaustiņi: elementa pārvietošana</li>
        <li>Ctrl+bultiņtaustiņi: lielāki soļi</li>
        <li>Enter: saglabāšanas dialoga atvēršana (saglabāt visu / pielāgot / atmest)</li>
        <li>ESC: pašreizējā elementa atmešana</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Krustiņu iestatījumi",
        'cross_properties': "Krustiņa īpašības",
        'cross_size': "Izmērs (px):",
        'cross_line_width': "Līnijas biezums:",
        'cross_color': "Krāsa:",
        'cross_choose_color': "Izvēlēties",
        'cross_fine_tuning': "Smalka regulēšana saglabājot (pikseļi)",
        'cross_offset_x': "X nobīde:",
        'cross_offset_y': "Y nobīde:",
        'cross_offset_x_tooltip': "Negatīvas vērtības pārvieto krustiņu pa kreisi, pozitīvas – pa labi",
        'cross_offset_y_tooltip': "Negatīvas vērtības pārvieto krustiņu uz augšu, pozitīvas – uz leju",
        'cross_preview': "Priekšskatījums",
        'cross_save': "Pielietot iestatījumus",
        'cross_customized': "Krustiņš pielāgots",
        'cross_settings_applied': "Krustiņu iestatījumi saglabāti.\nIzmērs: {0}px, līnijas biezums: {1}px\n{2}",
        'cross_updated_count': "{0} esošie krustiņi atjaunināti.",
        'cross_no_crosses': "Nav atrasts neviens esošs krustiņš.",
        'cross_settings_applied_all': "Krustiņu iestatījumi piemēroti visiem {0} krustiņiem",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Parakstu iestatījumi",
        'signature_1': "Paraksts 1",
        'signature_2': "Paraksts 2",
        'signature_select': "Izvēlēties parakstu",
        'signature_add': "➕ Pievienot jaunu parakstu...",
        'signature_size': "Paraksta {0} izmērs (%):",
        'signature_common': "Vispārīgie iestatījumi",
        'signature_timestamp': "Automātiski pievienot laika zīmogu",
        'signature_location': "Noklusējuma vieta:",
        'signature_timestamp_size': "Laika zīmoga fonta lielums:",
        'signature_no_files': "-- Nav atrasts neviens paraksts --",
        'signature_insert': "Ievietot parakstu",
        'signature_insert_1': "Ievietot parakstu 1",
        'signature_insert_2': "Ievietot parakstu 2",
        'signature_customize': " Pielāgot parakstu",
        'signature_discard': " Atmest šo parakstu",
        'signature_save_all': " Saglabāt visus parakstus",
        'signature_discard_all': " Atmest visus parakstus",
        'signature_guide_title': "Paraksti – Rokasgrāmata",
        'signature_guide': """
📝 Paraksti – Īsa rokasgrāmata

- Iestatiet galveno paroli
- Konfigurējiet parakstus izvēlnē Iestatījumi
  (izmērs, laika zīmogs ...)
- Ievietojiet ar LABO POGU vēlamajā vietā
  (galvenā parole nepieciešama vienu reizi sesijā)
- Pārvietojiet parakstu ar peli vai bultiņtaustiņiem
- Vairākus parakstus var ievietot vienu pēc otra
- Katru parakstu var pielāgot individuāli
- Atmest atsevišķu parakstu
- Saglabāt / atmest visus parakstus vienlaikus
- Var izmantot arī izvēļņu joslu.
        """,
        'signature_placeholder': "Priekšskatījums nav pieejams",
        'signature_info': "Paraksts {0}: {1}×{2} px ({3}% no {4}×{5})",
        'signature_info_placeholder': "Paraksta {0} iestatījumi",
        'signature_inserted': "Paraksts {0} ievietots lapā {1}",
        'signature_deleted': "Paraksts dzēsts",
        'signature_copied': "Paraksts nokopēts",
        'signature_pasted': "Paraksts {0} ievietots",
        'signature_saved': "{0} paraksti tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'signature_saved_voice': "{0} paraksti saglabāti",
        'mode_replace_signature_format': "Iziet no režīma un ievietot parakstu {0}",
        'mode_conflict_voice_signature': "Režīms {0} ir aktīvs. Vai iziet un ievietot parakstu?",
        'signature_not_configured': "Paraksts {0} nav konfigurēts",
        'signature_file_not_found': "Paraksta fails nav atrasts",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Nav nokopēta paraksta",
        'no_signatures_to_save': "Nav parakstu, ko saglabāt",
        'signature_save_question': "Vai saglabāt visus parakstus, pielāgot vai atmest šo?",
        'signatures_saved_title': "Paraksti saglabāti",
        'signatures_saved': "{0} paraksti tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'signatures_saved_voice': "{0} paraksti saglabāti.",
        'all_signatures_discarded': "Visi paraksti atmesti",
        'signature_settings_saved': "Parakstu iestatījumi saglabāti",
        'signature_cancelled': "Paraksts atmests",
        'signature_active_title': "Paraksts aktīvs",
        'signature_replace_question': "Jau ir aktīvs paraksts.\n\nVai vēlaties aizstāt pašreizējo parakstu?",
        'signature_replace': "Aizstāt parakstu",
        'signature_replace_voice': "Vai aizstāt pašreizējo parakstu vai atcelt?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Attēlu iestatījumi",
        'image_common': "Vispārīgie attēlu iestatījumi",
        'image_keep_aspect': "Saglabāt malu attiecību velkot",
        'image_default_size': "Noklusējuma izmērs (%):",
        'image_dark_invert': "Invertēt attēlus tumšajā režīmā",
        'image_dark_invert_tooltip': "Ieslēgts: attēli tiek invertēti labākai redzamībai",
        'image_fine_tuning': "Smalka regulēšana (pikseļi)",
        'image_offset_x': "X nobīde:",
        'image_offset_y': "Y nobīde:",
        'image_offset_x_tooltip': "Negatīvas vērtības pārvieto attēlu pa kreisi, pozitīvas – pa labi",
        'image_offset_y_tooltip': "Negatīvas vērtības pārvieto attēlu uz augšu, pozitīvas – uz leju",
        'image_select': "Izvēlēties attēlu",
        'image_insert': "Ievietot attēlu",
        'image_customize': " Pielāgot attēlu",
        'image_aspect': " Saglabāt malu attiecību",
        'image_discard': " Atmest šo attēlu",
        'image_save_all': " Saglabāt visus attēlus",
        'image_discard_all': " Atmest visus attēlus",
        'image_filter': "Attēli",
        'image_guide_title': "Attēlu ievietošana – Rokasgrāmata",
        'image_guide': """
📷 Attēlu ievietošana PDF – Īsa rokasgrāmata:

1. Ar peles labo pogu noklikšķiniet vēlamajā vietā
2. "Ievietot attēlu" → izvēlieties attēlu
3. Novietojiet attēlu: velciet ar peli
4. Pielāgojiet izmēru: velciet stūrus/malas
5. Saglabāt malu attiecību: taustiņš [A]
6. Papildu pielāgojumi: ar peles labo pogu uz attēla

Padoms: Kontekstizvēlnē varat mainīt iestatījumus.
        """,
        'image_inserted': "Attēls {0} ievietots lapā {1}",
        'image_deleted': "Attēls atmests",
        'image_copied': "Attēls nokopēts",
        'image_pasted': "Attēls ievietots",
        'image_saved': "{0} attēli tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'image_saved_voice': "{0} attēli saglabāti",
        'image_aspect_on': "ieslēgts",
        'image_aspect_off': "izslēgts",
        'image_aspect_toggle': "Saglabāt malu attiecību {0}",
        'image_reset': "Attēls atjaunots sākotnējā izmērā",
        'image_replaced': "Attēls aizstāts",
        'image_invalid': "Nederīgs attēls",
        'mode_replace_image': "Ievietot attēlu",
        'mode_conflict_voice_image': "Režīms {0} ir aktīvs. Vai iziet un ievietot attēlu?",
        'image_active_title': "Attēls aktīvs",
        'image_replace_question': "Jau ir aktīvs attēls.\n\nVai vēlaties aizstāt pašreizējo attēlu?",
        'image_replace': "Aizstāt attēlu",
        'image_replace_voice': "Vai aizstāt pašreizējo attēlu vai atcelt?",
        'image_filter_all': "Attēli (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Visi faili (*.*)",
        'no_copied_image': "Nav nokopēta attēla",
        'image_discarded': "Attēls atmests",
        'image_save_question': "Vai saglabāt visus attēlus, pielāgot vai atmest šo?",
        'no_images_to_save': "Nav attēlu, ko saglabāt",
        'no_valid_images': "Nav derīgu attēlu, ko saglabāt",
        'images_saved_title': "Attēli saglabāti",
        'images_saved': "{0} attēli tika ievietoti PDF.\n\nPDF tika pārlādēts...",
        'images_saved_voice': "{0} attēli saglabāti.",
        'all_images_discarded': "Visi attēli atmesti",
        'image_settings_updated': "Attēlu iestatījumi atjaunināti",
        'image_replace_title': "Izvēlēties jaunu attēlu",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Formu iestatījumi",
        'form_basic': "Pamata iestatījumi",
        'form_default_type': "Noklusējuma formas veids:",
        'form_rectangle': "Taisnstūris",
        'form_ellipse': "Elipse",
        'form_line': "Līnija",
        'form_arrow': "Bulta",
        'form_line_width': "Līnijas biezums:",
        'form_colors': "Krāsas",
        'form_line_color': "Līnijas krāsa:",
        'form_fill_color': "Aizpildījuma krāsa:",
        'form_choose_color': "Izvēlēties",
        'form_transparent': "Caurspīdīgs fons (tikai līnija)",
        'form_filled': "aizpildīts",
        'form_dark_mode': "Tumšais režīms",
        'form_dark_invert': "Invertēt krāsas tumšajā režīmā",
        'form_fine_tuning': "Smalka regulēšana (pikseļi)",
        'form_offset_x': "X nobīde:",
        'form_offset_y': "Y nobīde:",
        'form_offset_x_tooltip': "Negatīvas vērtības pārvieto formu pa kreisi, pozitīvas – pa labi",
        'form_offset_y_tooltip': "Negatīvas vērtības pārvieto formu uz augšu, pozitīvas – uz leju",
        'form_preview': "Priekšskatījums",
        'form_insert': "Ievietot formu",
        'form_rectangle_insert': "Taisnstūris",
        'form_ellipse_insert': "Elipse/ aplis",
        'form_line_insert': "Līnija (2 klikšķi)",
        'form_arrow_insert': "Bulta (2 klikšķi)",
        'form_customize': " Pielāgot formu",
        'form_transparent_toggle': " Caurspīdīgs fons",
        'form_discard': " Atmest šo formu",
        'form_save_all': " Saglabāt visas formas",
        'form_discard_all': " Atmest visas formas",
        'form_guide_title': "Formu ievietošana – Rokasgrāmata",
        'form_guide': """
📐 Formu ievietošana PDF – Īsa rokasgrāmata:

1. Izvēlieties formas veidu (taisnstūris, elipse, līnija, bulta)
2. Noklikšķiniet vietā
   - Taisnstūris/elipse: viens klikšķis novieto formu
   - Līnija/bulta: divi klikšķi sākuma un beigu punktam
3. Novietojiet formu: velciet ar peli
4. Pielāgojiet izmēru: velciet stūrus/malas
5. Saglabāt formu: Enter
6. Atmest formu: ESC
7. Papildu pielāgojumi: ar peles labo pogu uz formas

Padoms: Kontekstizvēlnē varat mainīt iestatījumus.
        """,
        'form_inserted': "{0} ievietots lapā {1}",
        'form_deleted': "Forma dzēsta",
        'form_copied': "Forma nokopēta",
        'form_pasted': "Forma ievietota",
        'form_saved': "{0} formas tika ievietotas PDF.\n\nPDF tika pārlādēts...",
        'form_saved_voice': "{0} formas saglabātas",
        'form_reset': "Forma atjaunota noklusējuma izmērā",
        'form_transparent_on': "ieslēgts",
        'form_transparent_off': "izslēgts",
        'form_transparent_toggled': "Caurspīdīgs fons {0}",
        'form_line_cancel': "Līnijas zīmēšana atcelta",
        'form_second_click': "Tagad noklikšķiniet {0} beigu punktu",
        'mode_replace_form': "Ievietot formu",
        'mode_conflict_voice_form': "Režīms {0} ir aktīvs. Vai iziet un ievietot formu?",
        'form_settings_updated': "Formu iestatījumi atjaunināti",
        'form_unknown': "Forma",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Noklikšķiniet sākuma punktu",
        'form_line_guide_2': "2. Noklikšķiniet beigu punktu",
        'form_line_guide_3': "Līnija tiks novilkta starp abiem punktiem.",
        'form_line_status_1': "Gaida pirmo klikšķi...",
        'form_line_status_2': "Pirmais punkts iestatīts: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Tagad noklikšķiniet beigu punktu...",
        'form_line_status_4': "Abi punkti iestatīti.\nNoklikšķiniet 'Gatavs', lai saglabātu.",
        'form_line_reset': "Atiestatīt",
        'form_line_finish': "Gatavs",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopēt (Cmd+C)",
        'paste': "Ielīmēt (Cmd+V)",
        'copied': "Nokopēts: {0}",
        'no_element_to_copy': "Nav izvēlēts neviens elements kopēšanai",
        'no_copied_data': "Nav nokopētu datu",
        'no_valid_position': "Nav derīgas vietas ielīmēšanai",
        'copy_text': "Teksts nokopēts",
        'copy_image': "Attēls nokopēts",
        'copy_form': "Forma nokopēta",
        'copy_signature': "Paraksts nokopēts",
        'element_text': "Teksts",
        'element_image': "Attēls",
        'element_form': "Forma",
        'element_signature': "Paraksts",
        'element_unknown': "Elements",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Režīmu konflikts",
        'mode_conflict_message': "Režīms '{0}' jau ir aktīvs.\n\nVai vēlaties no tā iziet un {1}?",
        'mode_replace': "Iziet no režīma un {0}",
        'mode_cancel': "Atcelt",
        'mode_replace_text': "ievietot tekstu",
        'mode_replace_cross': "ievietot krustiņu",
        'mode_replace_signature': "ievietot parakstu",
        'mode_replace_image': "ievietot attēlu",
        'mode_replace_form': "ievietot formu",
        'mode_conflict_voice': "Režīms {0} ir aktīvs. Vai iziet un ievietot tekstu?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Teksta ievade",
        'active_mode_signature': "Paraksts",
        'active_mode_image': "Attēls",
        'active_mode_form': "Forma",
        'active_mode_and': " un ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Ievietot",
        'insert_another_text': "Ievietot tekstu",
        'insert_another_cross': "Ievietot krustiņu",
        'insert_another_signature_1': "Paraksts 1",
        'insert_another_signature_2': "Paraksts 2",
        'insert_another_image': "Ievietot attēlu",
        'insert_another_form_rect': "Taisnstūris",
        'insert_another_form_ellipse': "Elipse",
        'insert_another_form_line': "Līnija (2 klikšķi)",
        'insert_another_form_arrow': "Bulta (2 klikšķi)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Saglabāt {0}",
        'save_dialog_message': "{0} tiks saglabāts lapā {1}.\n\nKā vēlaties turpināt?",
        'save_all': "Saglabāt visus {0}",
        'save_single': "Saglabāt {0}",
        'save_customize': "Pielāgot {0}",
        'save_discard': "Atmest šo {0}",
        'save_continue': "Turpināt rediģēšanu",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Pāriet uz lapu {0}",
        'context_rotate': " Pagriezt lapu {0}",
        'context_delete': " Dzēst lapu {0}",
        'context_export': " Eksportēt lapu {0}",
        'context_mark_as': " Atzīmēt lapu kā...",
        'context_mark_empty': " Tukša lapa",
        'context_unmark_empty': " Vairs nav tukša",
        'context_mark_export': " Atzīmēt eksportam",
        'context_unmark_export': " Vairs neeksportēt",
        'context_batch_actions': " Grupu darbības",
        'context_batch_delete_empty': " Dzēst visas {0} tukšās lapas",
        'context_batch_export_single': " Eksportēt visas {0} lapas (viens fails)",
        'context_batch_export_split': " Eksportēt visas {0} lapas (atsevišķi)",
        'context_drag_start': " Sākt vilkšanu",
        'context_drag_stop': " Beigt vilkšanu",
        'context_insert': " Ievietot",
        'context_insert_pages': " Ievietot lapas",
        'context_zoom': "Tālummaiņa",
        'discard_mixed': "Atmest visus {0} {1} un {2} {3}",
        'save_mixed': "Saglabāt {0} {1} un {2} {3}",
        'discard_texts': "Atmest visus {0} tekstus",
        'discard_text_single': "Atmest 1 tekstu",
        'save_texts': "Saglabāt {0} tekstus",
        'save_text_single': "Saglabāt 1 tekstu",
        'discard_crosses': "Atmest visus {0} krustiņus",
        'discard_cross_single': "Atmest 1 krustiņu",
        'save_crosses': "Saglabāt {0} krustiņus",
        'save_cross_single': "Saglabāt 1 krustiņu",
        'discard_signatures': "Atmest visus {0} parakstus",
        'save_signature_single': "Saglabāt 1 parakstu",
        'save_signatures': "Saglabāt {0} parakstus",
        'discard_images': "Atmest visus {0} attēlus",
        'save_image_single': "Saglabāt 1 attēlu",
        'save_images': "Saglabāt {0} attēlus",
        'discard_forms': "Atmest visas {0} formas",
        'save_form_single': "Saglabāt 1 formu",
        'save_forms': "Saglabāt {0} formas",
        'cross_discard': "Atmest šo krustiņu",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Eksporta / importa informācija",
        'export_what': "📋 Kas tiek eksportēts?",
        'export_general': "Vispārīgie iestatījumi",
        'export_general_items': "• Balss izvade (ieslēgts/izslēgts, ātrums)\n• Tumšais/gaišais režīms\n• Rezerves kopiju iestatījumi\n• OCR iestatījumi",
        'export_image_form': "Attēlu un formu iestatījumi",
        'export_image_form_items': "• Attēlu iestatījumi (malu attiecība, noklusējuma izmērs)\n• Formu iestatījumi (līnijas biezums, krāsas)\n• Parakstu iestatījumi (ceļi, izmēri, laika zīmogs)",
        'export_passwords': "Paroļu datubāze",
        'export_passwords_items': "• Visas saglabātās PDF paroles\n• Pēc izvēles šifrētas vai atšifrētas",
        'export_master': "Galvenās paroles iestatījumi",
        'export_master_items': "• Galvenās paroles hash\n• Iestatījumi parakstiem/teksta blokiem",
        'export_signatures': "Paraksti un teksta bloki",
        'export_signatures_items': "• Visi attēlu faili (paraksti)\n• Visi teksta bloki ar formatējumu\n• Privātie/publiskie marķējumi",
        'export_import_warning': "⚠️ Svarīgas piezīmes",
        'export_import_note': "• Importējot VISI pašreizējie iestatījumi tiks pārrakstīti\n• Nepieciešama lietojumprogrammas restartēšana\n• Esošie paraksti/teksta bloki tiks aizstāti",
        'export_master_note': "• Ja galvenā parole ir iestatīta, varat izvēlēties:\n  - Atšifrēts (paroles vienkāršā tekstā)\n  - Šifrēts (lasāmas tikai ar galveno paroli)",
        'export_security': "• Eksportētais ZIP fails satur konfidenciālus datus\n• Uzglabājiet to droši (piem., šifrētā USB zibatmiņā)\n• Zaudējot failu, paroles tiek neatgriezeniski zaudētas",
        'export_format': "📁 Eksporta formāts",
        'export_format_desc': "Iestatījumi tiek saglabāti vienā ZIP failā:",
        'export_filename': "PDFDarkView_Iestatijumi_GGGGMMDD_HHMMSS.zip",
        'export_success': "Iestatījumi veiksmīgi eksportēti",
        'export_failed': "Eksports neizdevās",
        'export_import_question': "Vai vēlaties tagad restartēt lietojumprogrammu?",
        'export_password_question': "Galvenā parole ir iestatīta.\n\nVai vēlaties eksportēt paroles atšifrētā veidā?\n(pretējā gadījumā tās tiks eksportētas šifrētas)",
        'export_decrypt': "Eksportēt atšifrētas",
        'export_encrypt': "Eksportēt šifrētas",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informācija",
        'info_title': "Par PDF Dark View",
        'info_version': "Versija",
        'info_author': "Izstrādāja Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Par",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ir pieejams PDF skatītājs, kas īpaši izstrādāts cilvēkiem ar redzes traucējumiem.</p>

            <p><strong>Galvenās īpašības:</strong></p>
            <ul>
                <li>Kontrastains, pielāgojams interfeiss</li>
                <li>Pilnīga tastatūras vadība</li>
                <li>Iebūvēta runas sintēze</li>
                <li>OCR skenētiem dokumentiem</li>
                <li>Plaši rediģēšanas rīki</li>
            </ul>

            <p>Tiek atbalstītas vairāk nekā 50 valodas – lai PDF faili būtu pieejami ikvienam.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkcijas",
        'info_features_intro': "PDF Dark View piedāvā jums šādas iespējas:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Attēlošana un navigācija</strong> – Tumšais/Gaišais režīms, lapu šķirstīšana, tālummaiņa, pārlēkt uz lapu</li>
            <li><strong>OCR (teksta atpazīšana)</strong> – Padariet skenētos dokumentus meklējamus un kopējamus</li>
            <li><strong>Rediģēšana</strong> – Tekstu, krustu, parakstu, attēlu un formu ievietošana</li>
            <li><strong>Lapu pārvaldība</strong> – Dzēšana, izvilkšana, ievietošana, pārvietošana, velkot un metot</li>
            <li><strong>Eksports</strong> – Uz Word, Pages vai kā tekstu</li>
            <li><strong>Drošība</strong> – Paroles aizsardzība un pārvaldība</li>
            <li><strong>Pieejamība</strong> – Runas sintēze, tastatūras vadība, augsts kontrasts</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Lietošana",
        'info_accessibility': "♿ Pieejamība – pilnīga tastatūras vadība",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Vispārīgi</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Atvērt PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Meklēt</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Pārslēgt tumšo/gaišo režīmu</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Drukāt</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Iziet</div>

        <div class="shortcut-cat">📖 Navigācija</div>
        <div class="shortcut-row"><kbd>Bultiņu taustiņi</kbd> Šķirstīt lapu pa lapai</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Iet uz lapu</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Pirmā lapa</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Pēdējā lapa</div>

        <div class="shortcut-cat">✏️ Rediģēšana</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Ievietot tekstu</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Dzēst lapas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Izvilkt lapas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Ievietot lapas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Pārvietot lapas</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Pagriezt lapu</div>

        <div class="shortcut-cat">🖼️ Elementu pārvietošana</div>
        <div class="shortcut-row"><kbd>Bultiņu taustiņi</kbd> Pārvietot tekstu/attēlu/parakstu</div>
        <div class="shortcut-row"><kbd>Ctrl+Bultiņu taustiņi</kbd> Lielāki soļi</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Saglabāt</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Atmest</div>

        <div class="shortcut-cat">🗣️ Runas sintēze</div>
        <div class="shortcut-row"><kbd>F2</kbd> Ieslēgt/izslēgt runas sintēzi</div>
        """,
        'info_contextmenu': "📌 Svarīgi: Visas funkcijas ir pieejamas arī caur konteksta izvēlni (peles labā poga)!",
        'info_accessibility_hint': "💡 Padoms: Runas sintēze (F2) atvieglo orientēšanos un sniedz atgriezenisko saiti par izvēlnēm un dialoga logiem.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licence & Impressums",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESUMS</strong><br>
        Informācija saskaņā ar § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Vācija<br>
        E-pasts: binhdiez64@gmail.com<br>
        Atbildīgais par saturu: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Atbildības ierobežojums</strong><br>
        Programmatūra ir izstrādāta ar vislielāko rūpību. Netiek sniegta nekāda garantija par precizitāti, pilnīgumu un funkcionalitāti. Lietošana notiek uz paša risku.<br><br>

        <strong>📄 MIT licence (privātai lietošanai)</strong><br>
        Autortiesības (c) 2026 Toralf Schulz (BinhDiez)<br>
        Atļauts: bezmaksas lietošana, privātas izmaiņas, personīgas kopijas.<br>
        Nav atļauts: pārdošana, komerciāla lietošana, autortiesību paziņojumu noņemšana.<br><br>

        <strong>🔧 Trešo pušu komponenti</strong><br>
        Šī programmatūra satur komponentus saskaņā ar GPL, AGPL, Apache 2.0, BSD un MIT licencēm.<br>
        Izplatot tālāk, ir jāievēro attiecīgie licenču noteikumi.<br><br>

        <strong>🌐 Atvērtais kods</strong><br>
        Pirmkods ir pieejams, un to var apskatīt, modificēt un izplatīt tālāk saskaņā ar attiecīgajiem licenču noteikumiem.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Pateicības",
        'info_credits': "Paldies atvērtā koda kopienai",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF apstrāde</li>
            <li><strong>PyQt5</strong> – Grafiskais interfeiss</li>
            <li><strong>Tesseract OCR</strong> – Teksta atpazīšana</li>
            <li><strong>OCRmyPDF</strong> – OCR integrācija</li>
            <li><strong>python-docx</strong> – Eksports uz Word</li>
            <li><strong>qtawesome</strong> – Ikonas</li>
            <li><strong>DeepSeek</strong> – Atbalsts tulkojumos (50+ valodas)</li>
            <li><strong>Visi lietotāji</strong> – Par vērtīgo atgriezenisko saiti</li>
            <li><strong>Atvērtā koda kopienai</strong> – Par lieliskajām bibliotēkām</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Valodas",
        'info_languages_header': "🌍 Valodu atbalsts",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View pašlaik atbalsta <strong>62 valodas</strong> – lai programmatūru varētu lietot pieejami visā pasaulē.</p>

            <p><strong>📖 Pilns valodu saraksts (Uz 2026. gada martu):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikandu</li>
                    <li>🇦🇱 Albāņu (Shqip)</li>
                    <li>🇩🇿 Arābu (العربية)</li>
                    <li>🇮🇩 Baliešu (Basa Bali)</li>
                    <li>🇧🇩 Bengāļu (বাংলা)</li>
                    <li>🇲🇲 Birmiešu (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosniešu (Bosanski)</li>
                    <li>🇧🇬 Bulgāru (Български)</li>
                    <li>🇨🇳 Ķīniešu (中文)</li>
                    <li>🇩🇰 Dāņu (Dansk)</li>
                    <li>🇩🇪 Vācu (Deutsch)</li>
                    <li>🇬🇧 Angļu (English)</li>
                    <li>🇪🇪 Igaunu (Eesti)</li>
                    <li>🇫🇮 Somu (Suomi)</li>
                    <li>🇫🇷 Franču (Français)</li>
                    <li>🇬🇷 Grieķu (Ελληνικά)</li>
                    <li>🇮🇱 Ivrits (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Horvātu (Hrvatski)</li>
                    <li>🇭🇺 Ungāru (Magyar)</li>
                    <li>🇮🇩 Indonēziešu (Bahasa Indonesia)</li>
                    <li>🇮🇪 Īru (Gaeilge)</li>
                    <li>🇮🇸 Islandiešu (Íslenska)</li>
                    <li>🇮🇹 Itāļu (Italiano)</li>
                    <li>🇯🇵 Japāņu (日本語)</li>
                    <li>🇰🇭 Khmeru (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korejiešu (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Latviešu (Latviešu)</li>
                    <li>🇱🇹 Lietuviešu (Lietuvių)</li>
                    <li>🇱🇺 Luksemburgiešu (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajiešu (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathu (मराठी)</li>
                    <li>🇲🇳 Mongoļu (Монгол)</li>
                    <li>🇳🇵 Nepāliešu (नेपाली)</li>
                    <li>🇳🇱 Holandiešu (Nederlands)</li>
                    <li>🇳🇴 Norvēģu (Norsk)</li>
                    <li>🇦🇫 Puštu (پښتو)</li>
                    <li>🇮🇷 Persiešu (فارسی)</li>
                    <li>🇵🇱 Poļu (Polski)</li>
                    <li>🇵🇹 Portugāļu (Português)</li>
                    <li>🇮🇳 Pendžabu (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumāņu (Română)</li>
                    <li>🇷🇺 Krievu (Русский)</li>
                    <li>🇸🇪 Zviedru (Svenska)</li>
                    <li>🇷🇸 Serbu (Српски)</li>
                    <li>🇸🇰 Slovāku (Slovenčina)</li>
                    <li>🇸🇮 Slovēņu (Slovenščina)</li>
                    <li>🇪🇸 Spāņu (Español)</li>
                    <li>🇹🇿 Svahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalu (Filipino)</li>
                    <li>🇮🇳 Tamilu (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Taizemiešu (ไทย)</li>
                    <li>🇨🇿 Čehu (Čeština)</li>
                    <li>🇹🇷 Turku (Türkçe)</li>
                    <li>🇺🇦 Ukraiņu (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vjetnamiešu (Tiếng Việt)</li>
                    <li>🇸🇳 Volofu (Wolof)</li>
                    <li>🇺🇸 Jidišs (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Pievienojiet savas valodas:</strong><br>
                Vai vēlaties valodu, kas vēl nav iekļauta? Vienkārši ievietojiet savu vārdnīcas failu (<code>sprache_xx.py</code>) blakus lietotnei – programmatūra to atpazīs automātiski. Ja interesējaties par īpašu tulkojumu, lūdzu, sazinieties ar mani.
            </div>

            <p><strong>🙏 Īpašs paldies:</strong> DeepSeek par atbalstu visu vārdnīcu tulkošanā 62 valodās.</p>

            <p>📧 Kontakti tulkojumiem: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Kļūda",
        'error_occurred': "Radusies kļūda",
        'error_pdf_load': "Kļūda, ielādējot PDF",
        'error_pdf_save': "Kļūda, saglabājot PDF",
        'error_ocr': "Kļūda teksta atpazīšanā",
        'error_no_pdf': "Nav ielādēts PDF",
        'error_page_not_found': "Lapa nav atrasta",
        'error_invalid_range': "Nederīgs lapu diapazons",
        'error_file_not_found': "Fails nav atrasts",
        'error_permission': "Nav atļaujas",
        'error_unknown': "Nezināma kļūda",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Veiksmīgi",
        'success_operation': "Darbība veiksmīgi pabeigta",
        'success_saved': "Veiksmīgi saglabāts",
        'success_exported': "Veiksmīgi eksportēts",
        'success_imported': "Veiksmīgi importēts",
        'success_deleted': "Veiksmīgi dzēsts",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Apstiprinājums",
        'confirm_yes': "Jā",
        'confirm_no': "Nē",
        'confirm_ok': "Labi",
        'confirm_cancel': "Atcelt",
        'confirm_delete': "Dzēst",
        'confirm_overwrite': "Pārrakstīt",
        'confirm_continue': "Turpināt",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Ielādē PDF...",
        'progress_saving': "Saglabā PDF...",
        'progress_exporting': "Eksportē PDF...",
        'progress_processing': "Apstrādā...",
        'progress_wait': "Lūdzu, uzgaidiet...",
        'progress_preparing': "Sagatavo...",
        'progress_finalizing': "Pabeidz...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Balts",
        'color_black': "Melns",
        'color_red': "Sarkans",
        'color_green': "Zaļš",
        'color_blue': "Zils",
        'color_yellow': "Dzeltens",
        'color_magenta': "Purpurs",
        'color_cyan': "Ciāns",
        'color_orange': "Oranžs",
        'color_gray': "Pelēks",
        'color_custom': "Krāsas izvēle",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Fails",
        'menu_edit': "&Rediģēt",
        'menu_view': "&Skats",
        'menu_tools': "&Rīki",
        'menu_settings': "&Iestatījumi",
        'menu_help': "&Palīdzība",
        'menu_language': "🌐 Valoda",
        'menu_guides': "&Rokasgrāmatas",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Atvērt",
        'file_save_as': "&Saglabāt kā...",
        'file_protect': "&Aizsargāt dokumentu...",
        'file_export': "&Eksportēt",
        'file_export_pages': "Eksportēt uz Pages",
        'file_export_word': "Eksportēt uz DOCX",
        'file_export_text': "Eksportēt uz TXT",
        'file_print_now': "&Drukāt tūlīt",
        'file_print': "&Drukāt",
        'file_close': "&Aizvērt",
        'file_quit': "&Iziet",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Meklēt",
        'edit_ocr': " Veikt OCR",
        'edit_rotate': "&Pagriezt lapu",
        'edit_rotate_all': "Pagriezt &visas lapas",
        'edit_delete_pages': "&Dzēst lapas",
        'edit_extract_pages': "&Izgūt lapas",
        'edit_insert_pages': "&Ievietot lapas",
        'edit_move_pages': "&Pārvietot lapas",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Ievietot tekstu un krustiņus",
        'text_insert': " Ievietot tekstu",
        'cross_insert': " Ievietot krustiņu",
        'text_customize': " Pielāgot tekstu",
        'cross_customize': " Pielāgot šo krustiņu",
        'cross_customize_all': " Pielāgot visus krustiņus",
        'text_discard': " Atmest šo tekstu/krustiņu",
        'text_discard_all': " Atmest visus tekstus un krustiņus",
        'text_save_all': " Saglabāt visus tekstus un krustiņus",
        'text_guide': " Teksta ievade / teksta bloki – rokasgrāmata",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Ievietot parakstu",
        'signature_settings_menu': " Iestatījumi...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Ievietot attēlu",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Ievietot formas",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Rādīt teksta logu",
        'view_zoom': "&Tālummaiņa",
        'view_zoom_page': "&Lapas platums (noklusējums)",
        'view_zoom_two': "&Divas lapas",
        'view_zoom_overview': "&Pārskats (vairākas lapas)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Pieejamība",
        'settings_voice': "Balss izvade",
        'settings_voice_tooltip': "papildina ekrāna lasītāju balss izvadi ar papildu informāciju",
        'settings_signature': "&Parakstu iestatījumi",
        'settings_password': "&Paroļu pārvaldība",
        'settings_backup': "Izveidot rezerves kopiju pirms izmaiņām",
        'settings_export_import': "&Eksportēt iestatījumus / importēt iestatījumus",
        'settings_export': "&Eksportēt visus iestatījumus...",
        'settings_import': "&Importēt visus iestatījumus...",
        'settings_export_info': "&Kas tiek eksportēts?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "ieslēgts",
        'voice_off': "izslēgts",
        'voice_toggle': "Balss izvade {0}",
        'voice_speed': "Ātrums {0} procenti",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Rīks nav atrasts:\n{0}\n\nBASE_DIR: {1}\nPārliecinieties, ka PDF rīki ir instalēti direktorijā {1}.",
        'tool_started': "{0} palaists",
        'tool_start_failed': "Nevarēja palaist",
        'process_error_failed_to_start': "Procesu nevarēja palaist. Vai fails pastāv?",
        'process_error_crashed': "Procesa palaišanas laikā tas avarēja.",
        'process_error_timeout': "Sasniegts procesa taimauts.",
        'process_error_write': "Rakstīšanas kļūda procesā.",
        'process_error_read': "Lasīšanas kļūda procesā.",
        'process_error_unknown': "Nezināma procesa kļūda",
        'process_command': "Komanda",
        'process_normal_exit': "normāli pabeigts",
        'process_crashed': "avarēja",
        'process_nonzero_exit': "{0} tika pabeigts ar kļūdas kodu {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Atcelšana...",
        'move_cancelling': "Pārvietošana tiek atcelta",
        'opening_pdf': "Atver PDF...",
        'loading_document': "Ielādē dokumentu...",
        'pdf_opened': "PDF atvērts",
        'pages_found_moving': "Atrastas {0} lapas, {1} pārvietošanai",
        'creating_backup': "Izveido rezerves kopiju...",
        'backup_description': "Dublē oriģinālo failu...",
        'backup_saved_as': "Rezerves kopija saglabāta kā: {0}",
        'error_format': "Kļūda: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Meklēšana atiestatīta",
        'page_header_simple': "=== Lapa {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Paroļu pārvaldība – Rokasgrāmata",
        'password_guide_voice': "Rokasgrāmata paroļu pārvaldībai. Lūdzu, izlasiet piezīmes.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Paroļu pārvaldība – Detalizēta rokasgrāmata</strong></p>

        <p><strong>1. PDF aizsardzība ar paroli</strong></p>
        <ul>
        <li>Atverot ar paroli aizsargātu PDF, tiek parādīts dialogs, kurā varat ievadīt paroli.</li>
        <li>Paroli var saglabāt šifrētu, lai tā nebūtu jāievada katru reizi (izvēles rūtiņa "Saglabāt paroli").</li>
        <li>Ar pogu "Noņemt paroli" varat izveidot atšifrētu PDF kopiju un izdzēst paroli no datubāzes.</li>
        </ul>

        <p><strong>2. Galvenā parole</strong></p>
        <ul>
        <li>Galvenā parole aizsargā piekļuvi visām saglabātajām PDF parolēm.</li>
        <li><strong>Iestatīšana:</strong> Dodieties uz "Iestatījumi → Paroļu pārvaldība → Galvenās paroles iestatījumi" un noklikšķiniet uz "Iestatīt galveno paroli". Izvēlieties spēcīgu paroli (vismaz 8 rakstzīmes).</li>
        <li><strong>Mainīšana:</strong> Pēc veiksmīgas autentifikācijas varat mainīt galveno paroli.</li>
        <li><strong>Noņemšana:</strong> Ja noņemsit galveno paroli, VISAS saglabātās paroles tiks neatgriezeniski dzēstas. Pirms tam varat eksportēt rezerves kopiju.</li>
        <li>Vienu reizi sesijā jums ir jāautentificējas ar galveno paroli, lai piekļūtu aizsargātām funkcijām (piem., paroļu rādīšanai).</li>
        </ul>

        <p><strong>3. Paroļu pārvaldība (saraksts)</strong></p>
        <ul>
        <li>Sadaļā "Iestatījumi → Paroļu pārvaldība" tiek atvērta tabula ar visiem saglabātajiem PDF failiem un to šifrētajām parolēm.</li>
        <li><strong>Bez galvenās paroles:</strong> Varat tikai dzēst ierakstus – paroles paliek slēptas.</li>
        <li><strong>Ar galveno paroli (autentificēts):</strong> Varat rādīt, kopēt, eksportēt un dzēst paroles.</li>
        <li><strong>Eksports:</strong> Izvēlieties formātu (JSON, CSV, TXT) un saglabājiet sarakstu. Ja galvenā parole ir iestatīta, varat izvēlēties, vai paroles eksportēt atšifrētā vai šifrētā veidā.</li>
        <li><strong>Imports:</strong> Iepriekš eksportētu ZIP failu (visi iestatījumi) var atkārtoti importēt, izmantojot "Iestatījumi → Eksportēt iestatījumus / importēt iestatījumus". Uzmanību: esošie dati tiks pārrakstīti!</li>
        </ul>

        <p><strong>4. Paroļu ģenerators</strong></p>
        <ul>
        <li>Paroles dialogā (piem., aizsargājot PDF) pa labi no ievades lauka atrodas kauliņa poga 🎲.</li>
        <li>Noklikšķiniet uz tās, lai atvērtu paroļu ģeneratoru. Varat iestatīt garumu, rakstzīmju kopas (lielie burti, mazie burti, cipari, speciālās rakstzīmes) un atdalītāju labākai lasāmībai.</li>
        <li>Ģenerēto paroli var tieši izmantot un vajadzības gadījumā kopēt.</li>
        </ul>

        <p><strong>5. Svarīgas drošības piezīmes</strong></p>
        <ul>
        <li>Saglabātās paroles tiek glabātas šifrētas ar AES-256. Atslēga tiek atvasināta no jūsu galvenās paroles (ja tā ir iestatīta) vai no fiksētas vērtības (bez galvenās paroles).</li>
        <li>Bez galvenās paroles paroles ir šifrētas, bet atslēga ir iebūvēta programmā – uzbrucējs ar piekļuvi jūsu failiem varētu tās atšifrēt. Tāpēc mēs stingri iesakām izmantot galveno paroli.</li>
        <li>Paroļu datubāze atrodas failā `Data/passwords.json`. Regulāri veidojiet rezerves kopijas, īpaši pirms galvenās paroles noņemšanas.</li>
        <li>Ja pazaudējat galveno paroli, visas saglabātās paroles tiek neatgriezeniski zaudētas.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Apgriešanas režīms",
        'invert_mode_classic': "Klasiskais (apgriezt visas krāsas)",
        'invert_mode_smart': "Viedais (apgriezt tikai spilgtumu)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Pelēktoņu slieksnis",
        'gray_threshold_10': "10% (stingrs)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Noklusējums)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (mīksts)",
        'threshold_changed': "Slieksnis iestatīts uz {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Pelēktoņu slieksnis – Skaidrojums",
        'threshold_guide_text': "Pelēktoņu slieksnis nosaka, kuri pikseļi viedajā tumšajā režīmā tiek uzskatīti par 'pelēkiem' un tiek apgriezti.\n\n"
                                "• Zema vērtība (10%) apgriež tikai gandrīz perfektus pelēkos toņus – krāsainie elementi paliek pilnībā saglabāti.\n"
                                "• Augsta vērtība (50%) apgriež arī nedaudz krāsainus pikseļus – tas palielina kontrastu, bet var izkropļot krāsas.\n\n"
                                "Optimālā vērtība ir atkarīga no dokumenta. Tīri teksta dokumentiem 30–40% bieži ir ideāli, krāsainai grafikai drīzāk 10–20%.\n\n"
                                "Jūs varat pielāgot vērtību jebkurā laikā, izmantojot 'Iestatījumu' izvēlni – PDF tiks nekavējoties pārlādēts.\n\n"
                                "Piezīme:\n* Fotoattēlus un attēlus var pareizi attēlot tikai gaišajā režīmā!\n* Apgriešanas iestatījumi tiek rādīti tikai tad, kad ir aktivizēts tumšais režīms.",
        'threshold_guide_voice': "Pelēktoņu slieksnis nosaka, cik spēcīgi viedais tumšais režīms iejaukjas. Zema vērtība saudzē krāsas, augsta vērtība palielina kontrastu.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Tiek atvērts PDF...",
        'progress_loading_document': "Tiek ielādēts dokuments...",
        'progress_pdf_opened': "PDF atvērts",
        'progress_creating_backup': "Tiek veidota dublējuma kopija...",
        'progress_backup_description': "Tiek drošināts oriģinālais fails...",
        'progress_backup_created': "Dublējuma kopija izveidota",
        'progress_backup_saved_as': "Saglabāts kā: {0}",
        'progress_analyzing_start': "Tiek sākta analīze...",
        'progress_searching_empty': "Tiek meklētas tukšas lapas...",
        'progress_page_empty': "{0}. lapa ir tukša",
        'progress_page_keep': "Saglabāt {0}. lapu",
        'progress_analysis_complete': "Analīze pabeigta",
        'progress_empty_found': "Atrastas {0} tukšas lapas",
        'progress_current_page': "Pašreizējā lapa",
        'progress_mark_delete': "Tiek atzīmēts dzēšanai",
        'progress_range_selected': "Lapu diapazons {0}-{1}",
        'progress_deleting_pages': "Tiek dzēstas {0} lapas",
        'progress_creating_new_pdf': "Tiek izveidots jauns PDF...",
        'progress_transferring_pages': "Tiek pārsūtītas lapas",
        'progress_keeping_page': "{0}. lapa tiks saglabāta ({1}/{2})",
        'progress_saving_pdf': "Tiek saglabāts PDF...",
        'progress_optimizing': "Tiek optimizēts faila izmērs...",
        'progress_finalizing': "Tiek pabeigts...",
        'progress_new_size': "Jaunais izmērs: {0:.2f} MB",
        'progress_cancelling': "Tiek atcelts...",
        'progress_cancel_message': "{0} tiek atcelts",
        'progress_pages_found_moving': "Atrastas {0} lapas, {1} jāpārvieto",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Tiek analizēts PDF...",
        'ocr_status_optimizing': "Notiek attēlu optimizācija...",
        'ocr_status_recognizing': "Notiek teksta atpazīšana...",
        'ocr_status_embedding': "Tiek iegults teksts...",
        'ocr_status_finalizing': "Tiek pabeigts PDF...",

        # PDF-Laden
        'progress_preparing': "Gatavošana...",
        'progress_loading': "Tiek ielādēts PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Lapu dzēšana...",
        'progress_moving_title': "Lapu pārvietošana...",
        'pages_found': "Atrastas lapas",
        'progress_creating_new_order': "Tiek izveidota jauna secība...",
        'progress_sorting_pages': "Lapu kārtošana...",
        'progress_moving_to_begin': "Pārvietot {0} lapas uz sākumu",
        'progress_transferring_count': "Pārsūtīt {0} lapas",
        'progress_transferring_before_target': "Pārsūtīt lapas pirms mērķa",
        'progress_moving_pages': "Pārvietot {0} lapas",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_dublikats_",
        'filename_protected_suffix': "_aizsargats_",
        'filename_copy_suffix': "_Kopija",
        'filename_page_single': "_Lapa_",
        'filename_page_range': "_Lapas_",
        'filename_export_page': "_Lapa_{0:03}",
        'filename_export_range': "_Lapas_{0}-{1}",
        'filename_export_multiple': "_Lapas_{0}",
        'filename_with_text': "_ar_Tekstu",
        'filename_with_signature': "_ar_Paraktu",
        'filename_with_image': "_ar_Attelu",
        'filename_with_forms': "_ar_Formam",
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
        'view_toggle_navbar': "Rādīt pogu joslu",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Nevar dzēst visas lapas",
		'pages_cannot_delete_last_page': 'Pēdējo lapu nevar dzēst!',
		'pages_cannot_delete_all_pages': 'Dokumentā jāpaliek vismaz vienai lapai!',
		'delete_pages_confirm': 'Vai tiešām vēlaties dzēst {0} lapas?',
		'delete_pages_confirm_voice': 'Vai tiešām vēlaties dzēst {0} lapas?',
		'pages_deleted': '{0} lapas veiksmīgi dzēstas.',
		'warning': 'Brīdinājums',
		'error': 'Kļūda',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nav atlasīta forma",
        'form_customized': "Forma pielāgota",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Izvēlēties",
        'btn_use': "Izmantot",
        'master_password_for_spasswords': "Lai saglabātu un izmantotu paroles, vispirms ir jāiestata galvenā parole.\n\nVai vēlaties iestatīt galveno paroli tagad?",
        'open_saved_dialog_title': "Atvērt saglabāto failu",
        'open_saved_question': "Vai vēlaties atvērt saglabāto failu tagad?",
        'password': "Parole",
        'password_manager_master_required': "Paroļu pārvaldnieks ir pieejams tikai tad, ja ir iestatīta galvenā parole.\n\nVai vēlaties iestatīt galveno paroli tagad?",
        'password_master_required_for_select': "Lai skatītu un izvēlētos saglabātās paroles, vispirms ir jāautentificējas ar savu galveno paroli.\n\nVai vēlaties autentificēties tagad?",
        'password_not_available': "Izvēlētā parole nav pieejama vai to nevarēja atšifrēt.",
        'password_options_title': "Paroles opcijas",
        'password_save_choice_change': "Iestatīt jaunu paroli",
        'password_save_choice_keep': "Izmantot esošo paroli",
        'password_save_choice_none': "Saglabāt nešifrētu",
        'password_save_hint': "Vispirms iestatiet galveno paroli, lai droši saglabātu paroles.",
        'password_save_master_required': "Saglabāt paroli (iespējams tikai ar galveno paroli)",
        'password_save_question': "Pašreizējais PDF ir aizsargāts ar paroli. Vai vēlaties izmantot esošo paroli, iestatīt jaunu vai saglabāt nešifrētu?",
        'password_select': "Izvēlēties paroli",
        'password_select_none': "Nav izvēlēta neviena parole.\n\nLūdzu, izvēlieties paroli no saraksta.",
        'password_select_one': "Lūdzu, izvēlieties tieši vienu paroli.\n\nJūs esat atzīmējis vairākas paroles.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_dublējums",
        'filename_insert_suffix': "_ar_ievietošanu",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_lappuses_dzēstas",
        'filename_pages_moved': "_lappuses_pārvietotas",
        'filename_rotated_all_suffix': "_visas_lappuses_pagrieztas",
        'filename_rotated_suffix': "_lappuse_pagriezta",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Failu nosaukumu konfigurācija, mainot PDF",
        'filename_keep_suffixes': "Saglabāt iepriekšējos paplašinājumus (piem., _ar_tekstu)",
        'filename_keep_suffixes_false': "Aizstāt",
        'filename_keep_suffixes_true': "Saglabāt",
        'filename_preview_label': "Faila nosaukuma priekšskatījums:",
        'filename_preview_overwrite_hint': "Priekšskatījums nav pieejams – oriģināls tiks pārrakstīts.",
        'filename_separator': "Vārdu atdalītājs",
        'filename_separator_none': "Nav atdalītāja",
        'filename_separator_space': "Atstarpe ( )",
        'filename_separator_underscore': "Pasvītra (_)",
        'filename_settings_saved': "Faila nosaukuma iestatījumi saglabāti",
        'filename_settings_title': "Faila nosaukuma formatēšana un dublēšana",
        'filename_timestamp_position': "Laika zīmoga pozīcija",
        'filename_timestamp_position_after': "Pēc pamatnosaukuma",
        'filename_timestamp_position_before': "Pavisam priekšā",
        'filename_timestamp_position_end': "Beigās",
        'filename_use_timestamp': "Izmantot laika zīmogu",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Uzvedība, veicot izmaiņas:</b><ul><li>Lappušu dzēšana un ievietošana</li><li>Teksta, paraksta, attēla un formu ievietošana</li><li>OCR</li></ul></html>",
        'backup_section': "Dublējums lappušu operācijām (Dzēst, Pārvietot)",
        'behavior_info': "Piezīme: Izvēloties 'Pārrakstīt oriģinālu', laika zīmogi un piedēkļi tiek ignorēti – fails saglabā savu nosaukumu.",
        'behavior_new_file': "Vienmēr izveidot jaunu failu (ar laika zīmogu un piedēkli)",
        'behavior_overwrite': "Pārrakstīt oriģinālu (nav jauna faila)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Visas lappuses tika pagrieztas.\n\nOriģināls palika nemainīgs.\nJauns fails: {0}",
        'all_pages_rotated_voice': "Visas lappuses pagrieztas, izveidots jauns fails.",
        'empty_pages_deleted_new_file': "{0} tukšas lappuses tika dzēstas.\n\nOriģināls palika nemainīgs.\nJauns fails: {1}",
        'empty_pages_deleted_voice': "{0} tukšas lappuses dzēstas, izveidots jauns fails.",
        'ocr_keep_original': "Saglabāt oriģinālu (atvērt manuāli vēlāk)",
        'ocr_new_file_question': "Jaunais meklējamais PDF tika saglabāts kā:\n{0}\n\nVai vēlaties to atvērt tagad?",
        'ocr_open_new': "Atvērt jaunu OCR failu",
        'ocr_original_kept': "Oriģinālais fails paliek atvērts. OCR fails ir saglabāts.",
        'page_deleted_new_file': "Lappuse {0} tika dzēsta.\n\nOriģināls palika nemainīgs.\nJauns fails: {1}",
        'page_deleted_voice': "Lappuse {0} dzēsta, izveidots jauns fails.",
        'page_rotated_new_file': "Lappuse {0} tika pagriezta.\n\nOriģināls palika nemainīgs.\nJauns fails: {1}",
        'page_rotated_voice': "Lappuse {0} pagriezta, izveidots jauns fails.",
        'pages_deleted_new_file': "Tika dzēstas {0} lappuses.\n\nOriģinālais fails palika nemainīgs.\nJauns fails: {1}",
        'pages_deleted_new_file_voice': "{0} lappuses dzēstas, izveidots jauns fails.",
        'pages_inserted_new_file': "Tika ievietotas {0} lappuses.\n\nOriģinālais fails palika nemainīgs.\nJauns fails: {1}",
        'pages_inserted_new_file_ask': "Tika ievietotas {0} lappuses.\n\nOriģināls palika nemainīgs.\nJauns fails: {1}\n\nVai vēlaties to atvērt tagad?",
        'pages_inserted_voice_new': "{0} lappuses ievietotas, izveidots jauns fails.",
        'pages_moved_new_file': "Tika pārvietotas {0} lappuses.\n\nOriģinālais fails palika nemainīgs.\nJauns fails: {1}",
        'pages_moved_new_file_voice': "{0} lappuses pārvietotas, izveidots jauns fails.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Vairs nerādīt",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Dublējuma iestatījums</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Dublējums IESLĒGTS</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Visām izmaiņām, kas pārraksta oriģinālu</strong> (teksts, paraksts, attēls, forma, OCR, pagriešana, ievietošana, lappušu dzēšana/pārvietošana) <strong>automātiski tiek izveidots dublējums ar laika zīmogu</strong> pirms izmaiņu piemērošanas.</p>
                <p style="margin: 5px 0 5px 20px;">• Dublējums atrodas blakus oriģinālajam failam (piem., <code>Dokuments_dublējums_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Ja papildus esat aktivizējis opciju <strong>„Pārrakstīt oriģinālu“</strong>, arī tad tiek izveidots dublējums.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Dublējums IZSLĒGTS</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Netiek izveidots nekāds dublējums</strong> – ne pārrakstot, ne veicot lappušu operācijas.</p>
                <p style="margin: 5px 0 5px 20px;">• Oriģinālais fails, to pārrakstot, var tikt neatgriezeniski zaudēts.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Ieteicams tikai pieredzējušiem lietotājiem!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Padoms:</strong> Dublējuma iestatījums ir neatkarīgs no opcijas „Pārrakstīt oriģinālu“. Jūs varat abus kombinēt.<br>
                Jūs varat šo ziņojumu neatgriezeniski paslēpt.
            </div>
        </div>
        """,
        'backup_info_title': "Dublējuma uzvedība",
        'backup_info_voice': "Paziņojums par dublējuma uzvedību lappušu operācijās. Dublējums ieslēgts pārraksta oriģinālu, dublējums izslēgts izveido jaunu failu.",
        'show_backup_info': "Informācija par dublējuma iestatījumu",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Vairs nerādīt",
        'overwrite_enable_backup': "Aktivizēt dublējumu (ieteicams)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Pārrakstīt oriģinālu</p>
            <p>Ja aktivizējat šo opciju, izmaiņas (teksts, paraksts, attēls, forma, OCR, pagriešana, ievietošana) tiek <strong>saglabātas tieši oriģinālā</strong> – <strong>netiek izveidots neviens jauns fails</strong>.</p>
            <p>• Faila nosaukums paliek nemainīgs.<br>
            • Laika zīmogi un piedēkļi tiek ignorēti.<br>
            • <strong>Bez dublējuma oriģināls var tikt neatgriezeniski zaudēts.</strong></p>
            <p style="color: #FFD700;">Ieteikums: Papildus aktivizējiet dublējuma opciju, lai iegūtu automātiskas drošības kopijas.</p>
        </div>
        """,
        'overwrite_info_title': "Pārrakstīt oriģinālu",
        'overwrite_info_voice': "Brīdinājums: Pārrakstīt oriģinālu – nav jauna faila. Dublējums ieteicams.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Tika ievietotas {0} lappuses.\n\nOriģinālais fails tika pārrakstīts.\nTika izveidots dublējums.",
        'pages_inserted_overwrite_no_backup': "Tika ievietotas {0} lappuses.\n\nOriģinālais fails tika pārrakstīts.\nNETIKA izveidots dublējums.",
        'texts_saved_overwrite_with_backup': "Izmaiņas tika saglabātas oriģinālā.\n\nTika izveidots dublējums.",
        'texts_saved_overwrite_no_backup': "Izmaiņas tika saglabātas oriģinālā.\n\nNETIKA izveidots dublējums.",
        'texts_crosses_saved_new_file': "{0} {1} un {2} {3} tika ievietoti.\n\nOriģinālais fails palika nemainīgs.\nTika izveidots jauns fails.\n\nNotiek jaunā PDF ielāde...",
        'texts_saved_new_file': "{0} {1} tika ievietoti.\n\nOriģinālais fails palika nemainīgs.\nTika izveidots jauns fails.\n\nNotiek jaunā PDF ielāde...",
        'crosses_saved_new_file': "{0} {1} tika ievietoti.\n\nOriģinālais fails palika nemainīgs.\nTika izveidots jauns fails.\n\nNotiek jaunā PDF ielāde...",
        'elements_saved_new_file': "{0} elementi tika ievietoti.\n\nOriģinālais fails palika nemainīgs.\nTika izveidots jauns fails.\n\nNotiek jaunā PDF ielāde...",
        'signatures_saved_overwrite_with_backup': "Paraksts(i) tika saglabāts(i) oriģinālā.\n\nTika izveidots dublējums.",
        'signatures_saved_overwrite_no_backup': "Paraksts(i) tika saglabāts(i) oriģinālā.\n\nNETIKA izveidots dublējums.",
        'images_saved_overwrite_with_backup': "Attēls(i) tika saglabāts(i) oriģinālā.\n\nTika izveidots dublējums.",
        'images_saved_overwrite_no_backup': "Attēls(i) tika saglabāts(i) oriģinālā.\n\nNETIKA izveidots dublējums.",
        'forms_saved_overwrite_with_backup': "Forma(s) tika saglabāta(s) oriģinālā.\n\nTika izveidots dublējums.",
        'forms_saved_overwrite_no_backup': "Forma(s) tika saglabāta(s) oriģinālā.\n\nNETIKA izveidots dublējums.",
        'signatures_saved_new_file': "{0} paraksti tika ievietoti.\n\nOriģinālais fails palika nemainīgs.\nTika izveidots jauns fails.\n\nNotiek jaunā PDF ielāde...",
        'images_saved_new_file': "{0} attēli tika ievietoti.\n\nOriģinālais fails palika nemainīgs.\nTika izveidots jauns fails.\n\nNotiek jaunā PDF ielāde...",
        'forms_saved_new_file': "{0} formas tika ievietotas.\n\nOriģinālais fails palika nemainīgs.\nTika izveidots jauns fails.\n\nNotiek jaunā PDF ielāde...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Brīdinājums: Šis PDF satur pagrieztas lappuses. Pozicionēšana var atšķirties.",
        'page_rotated_warning_title': "Konstatēta pagriezta lappuse",
        'page_rotated_warning_message': "Pašreizējā lappuse {0} ir pagriezta par {1}°.\n\nElementu ievietošana uz pagrieztām lappusēm netiek atbalstīta.\n\nVai vēlaties tagad pagriezt lappusi vertikālā stāvoklī?",
        'page_rotated_warning_voice': "Brīdinājums: Lappuse ir pagriezta. Lūdzu, vispirms to pagrieziet.",
        'paste_on_rotated_page_simple_warning': "Ievietošana lappusē {0} nav iespējama!\n\nŠī lappuse ir pagriezta par {1}°.\n\nLūdzu, vispirms pagrieziet lappusi uz 0° (Izvēlne: Rediģēt → Izlīdzināt lappusi).\n\nBrīdinājums:\nIepriekš nokopētais elements tiks zaudēts, ja nesaglabāsiet pirms lappuses pagriešanas.",
        'paste_on_rotated_page_voice': "Ievietošana pārtraukta. Lappuse ir pagriezta. Lūdzu, vispirms izlīdziniet lappusi.",
        'page_rotated_cancel': "Atcelt",
        'page_rotated_rotate_until_upright': "Pagriezt lappusi atkārtoti (līdz vertikālai)",
        'page_rotated_now_upright': "Lappuse tagad ir vertikāla. Tagad varat ievietot.",
        'page_rotated_still_not_upright': "Neizdevās pagriezt lappusi vertikālā stāvoklī. Lūdzu, labojiet manuāli.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Palīdzība: Pagrieztu lappušu labošana",
        'help_rotated_pages_voice': "Tiek atvērta palīdzība pagrieztu lappušu labošanai.",
        'btn_help': "Palīdzība",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problēma: Pagriezta lappuse – Ievietošana nedarbojas pareizi</p>

            <p>Ja tekstu, parakstu vai formu ievietošana uz pagrieztas lappuses nedarbojas pareizi, varat labot lappusi ar ārējo PDF redaktoru.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Risinājums ar ārēju rīku (piem., macOS Priekšskatījums)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Eksportēt lappusi</strong><br>
                &nbsp;&nbsp;Izvēlnē noklikšķiniet uz <strong>Fails → Eksportēt kā lappuses</strong> vai izmantojiet citu metodi, lai saglabātu vēlamo lappusi kā atsevišķu PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Atvērt lappusi ārējā programmā</strong><br>
                &nbsp;&nbsp;Atveriet eksportēto PDF PDF redaktorā (piem., <strong>macOS Priekšskatījums</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Pagriezt lappusi</strong><br>
                &nbsp;&nbsp;Pagrieziet lappusi tā, lai tā būtu vertikāla (Priekšskatījumā: <strong>Rīki → Pagriezt</strong> vai <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Saglabāt</strong><br>
                &nbsp;&nbsp;Saglabājiet laboto lappusi (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Ievietot lappusi atpakaļ oriģinālajā dokumentā</strong><br>
                &nbsp;&nbsp;Atgriezieties PDFDarkView un ievietojiet laboto lappusi vēlamajā pozīcijā:<br>
                &nbsp;&nbsp;<strong>Rediģēt → Ievietot lappuses</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatīva: Pagriezt lappusi oriģinālā</p>
                <p style="margin: 5px 0 5px 20px;">• Izmantojiet iebūvēto pagriešanas funkciju (<strong>Rediģēt → Pagriezt lappusi</strong>), lai lappusi labotu soli pa solim.<br>
                • Pēc katras pagriešanas varat pārbaudīt, vai ievietošana tagad darbojas.<br>
                • Tas bieži ir ātrāks risinājums – izmēģiniet to vispirms!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Padoms:</strong> Ja bieži saskaraties ar pagrieztām lappusēm, varat neatgriezeniski paslēpt brīdinājumu ievietošanas dialoglodziņā.<br>
                Pozicionēšana tad var atšķirties – izmantojiet šo opciju tikai tad, ja zināt sekas.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Izlīdzināt lappuses",
        'menu_rotate_normalize_tooltip': "Pagriezt lappusi vai atiestatīt uz 0°",
        'normalize_current_page': "Novediet pašreizējo lappusi vertikālā stāvoklī (iestatiet uz 0°)",
        'normalize_all_pages': "Novediet visas lappuses vertikālā stāvoklī (iestatiet uz 0°)",
        'page_normalized': "Lappuse {0} tika iestatīta vertikālā stāvoklī.",
        'all_pages_normalized': "Visas lappuses tika iestatītas vertikālā stāvoklī.",
        'page_already_upright': "Lappuse {0} jau ir vertikāla.",
        'all_pages_already_upright': "Visas lappuses jau ir vertikālas.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF nesatur meklējamu tekstu.</p><p>Vai vēlaties veikt OCR, lai eksportētu uz {0}?</p>",
        'export_ocr_voice': "PDF nesatur tekstu. Eksportam uz {0} ir nepieciešams OCR.",
        'export_no_ocr_possible': "Eksports bez OCR nav iespējams. Lūdzu, veiciet OCR, izmantojot izvēlni.",
        'ocr_failed_export_not_possible': "OCR neizdevās. Eksportu nevar veikt.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF tiks atvērts Priekšskatījumā. Lūdzu, sāciet drukas procesu tur.",
        'print_preview_manual': "PDF ir atvērts. Lūdzu, izpildiet drukas komandu manuāli (piem., Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Apvienot PDF failus",
        'merge_pdfs': "Apvienot PDF failus",
        'merge_progress_title': "Notiek PDF failu apvienošana...",
        'merge_pdfs_list': "PDF faili secībā (Velciet un nometiet, lai kārtotu)",
        'merge_add_pdf': "Pievienot PDF",
        'merge_remove': "Noņemt",
        'merge_move_up': "Uz augšu",
        'merge_move_down': "Uz leju",
        'merge_pdfs_info': "💡 Padoms: Jūs varat mainīt secību, velkot un metot",
        'merge_no_pdfs': "Nav izvēlēts neviens PDF fails. Noklikšķiniet uz 'Pievienot PDF'.",
        'merge_info': "Izvēlēti {0} PDF faili (apmēram {1} lappuses)",
        'merge_open_file': "Atvērt failu",
        'merge_merge': "Apvienot",
        'merge_error': "Kļūda apvienošanas laikā",
        'merge_min_two_pdfs_error': "Lūdzu, izvēlieties vismaz divus PDF failus apvienošanai.",
        'merge_select_pdfs': "Izvēlieties PDF failus apvienošanai",
        'merge_error_file': "Kļūda apstrādes laikā",
        'merge_cancelled': "Apvienošana tika atcelta",
        'merge_preparing': "Sagatavošana...",
        'merge_processing': "Apstrādā PDF {0} no {1}",
        'merge_saving': "Saglabā apvienoto PDF...",
        'merge_complete': "Pabeigts!",
        'merge_success_title': "Apvienošana veiksmīga",
        'merge_success_voice': "{0} PDF faili tika veiksmīgi apvienoti.",
        'merge_success_message': "{0} PDF faili tika veiksmīgi apvienoti.\n\nJaunajā dokumentā tagad ir {1} lappuses.\n\nJauns fails:\n{2}\n\nSaglabāšanas vieta:\n{3}\n{2}\n\nVai vēlaties atvērt šo PDF?",
        'replace_file_title': "Aizstāt failu?",
        'replace_file_message': "PDF jau ir atvērts. Vai vēlaties to aizstāt ar jauno failu?",
        'btn_yes': "Jā",
        'btn_no': "Nē",
        'filename_merge_suffix': "apvienots",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Atver {0}...",
        'progress_merge_reading': "Nolasa {0}...",
        'progress_merge_adding': "Pievieno {0} lappuses...",
        'progress_merge_optimizing': "Optimizē PDF...",
        'progress_merge_writing': "Raksta PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF aizvēršanu",
        'action_close_window': "loga aizvēršanu",
        'action_open_new_pdf': "jauna PDF atvēršanu",
        'action_quit_app': "lietotnes iziešanu",
        'changes_saved': "Izmaiņas tika saglabātas.",
        'file_close_title': "Aizvērt PDF failu",
        'save_before_action': "Vai pirms {0} ir jāsaglabā izmaiņas? Jā vai Nē?",
        'save_before_action_voice': "Vai pirms {0} ir jāsaglabā izmaiņas? Jā vai Nē?",
        'save_before_close_question': "Vai pirms aizvēršanas ir jāsaglabā izmaiņas? Jā vai Nē?",

         # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Izveidots meklējams PDF:\n\n{0}\n\n<b>mēģiniet vēlreiz, ja nepieciešams",
        "ocr_rotate_title": "Izlīdzināt lapas pirms OCR",
        "ocr_rotate_question": "PDF satur pagrieztas lapas.\nVai vēlaties izlīdzināt visas lapas 0° pirms OCR?\nTas ievērojami uzlabo teksta atpazīšanu.",
        "ocr_rotate_yes": "Jā, izlīdzināt",
        "ocr_rotate_no": "Nē, sākt OCR tieši",
        "ocr_rotate_voice": "PDF satur pagrieztas lapas. Vai pirms OCR ir jāizlīdzina visas lapas?",
        "ocr_not_performed_message": "Nav teksta. Lūdzu, veiciet OCR (izvēlne \"Rediģēt\" → \"Veikt OCR\" vai taustiņš Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR iestatījumi",
        "ocr_language_btn": "Izvēlēties OCR valodu",
        "ocr_language": "OCR valoda(s)",
        "ocr_language_current": "Pašreizējā valoda:",
        "ocr_param_info": "Informācija par parametru",

        "ocr_force_ocr_label": "Piespiest OCR",
        "ocr_deskew_label": "Labot slīpumu",
        "ocr_clean_label": "Notīrīt attēlu",
        "ocr_oversample_label": "Izšķirtspēja (DPI)",
        "ocr_pagesegmode_label": "Lapas sadalījums",
        "ocr_oem_label": "OCR dzinēja režīms",
        "ocr_optimize_label": "PDF saspiešana",
        "ocr_jobs_label": "Paralēlie procesi",
        "ocr_verbose_label": "Žurnāla detalizācija",

        "ocr_force_ocr_tooltip": "Piespiest OCR katrā lapā, pat ja teksts jau pastāv",
        "ocr_deskew_tooltip": "Automātiski izlīdzināt slīpus skenējumus",
        "ocr_clean_tooltip": "Noņemt troksni un artefaktus no attēla",
        "ocr_oversample_tooltip": "Palielināt attēlu pirms OCR līdz šim DPI",
        "ocr_pagesegmode_tooltip": "Nosaka, kā lapa tiek sadalīta teksta apgabalos",
        "ocr_oem_tooltip": "Izvēlas Tesseract OCR dzinēju",
        "ocr_optimize_tooltip": "Izvades PDF saspiešanas līmenis",
        "ocr_jobs_tooltip": "Paralēlo OCR procesu skaits",
        "ocr_verbose_tooltip": "Žurnāla izvades detalizācijas līmenis",
        "ocr_settings_explain_btn": "Skaidrojums",

        "ocr_force_ocr_explain": "Piespiež teksta atpazīšanu <b>katrā</b> lapā, pat ja tā jau satur tekstu.\n\nIeteikums: <b>Ieslēgt</b> skenētiem PDF, <b>Izslēgt</b> vietējiem PDF ar jau esošu tekstu.",

        "ocr_deskew_explain": "Labo nedaudz slīpus skenējumus (līdz aptuveni 5°).\n\nIeteikums: <b>Ieslēgt</b> skenētiem dokumentiem, <b>Izslēgt</b>, ja lapas jau ir pilnīgi taisnas.",

        "ocr_clean_explain": "Noņem troksni, punktus un mazus artefaktus no attēla.\n<b>SVARĪGI:</b> Arābu, taju vai vjetnamiešu tekstiem ar diakritiskajām zīmēm (punkti virs/zem burtiem) šī opcija ir <b>jāizslēdz</b>, pretējā gadījumā var tikt zaudētas svarīgas rakstzīmes.",

        "ocr_oversample_explain": "Palielina attēlu <b>pirms</b> teksta atpazīšanas līdz norādītajam DPI.<br><br>• <b>72-150 DPI:</b> Ļoti ātri, bet zems atpazīšanas līmenis<br>• <b>200-300 DPI:</b> Optimālais diapazons (Noklusējums: 300)<br>• <b>400+ DPI:</b> Tikai nedaudz labāka atpazīšana, bet ievērojami lielāki faili<br><br>Ieteikums: 300 DPI sarežģītiem rakstiem (arābu, ķīniešu, japāņu), 200 DPI rietumu valodām.",

        "ocr_pagesegmode_explain": "Nosaka, kā Tesseract sadala lapu teksta apgabalos.\n\n• <b>3 - Automātiski (Noklusējums):</b> Labs jauktiem izkārtojumiem\n• <b>4 - Viena kolonna:</b> Vienas kolonnas tekstiem\n• <b>5 - Vertikāls bloks:</b> Vertikāliem rakstiem (japāņu, ķīniešu)\n• <b>6 - Vienveidīgs teksta bloks:</b> Optimāls plūstošam tekstam bez kolonnām\n• <b>11 - Neapstrādāts attēls:</b> Sliktiem skenējumiem / rokrakstiem\n\nIeteikums: <b>6</b> vienkāršiem teksta dokumentiem, <b>3</b> sarežģītiem izkārtojumiem.",

        "ocr_oem_explain": "Izvēlas Tesseract OCR dzinēju.\n\n• <b>0 - Legacy:</b> Vecais dzinējs (ātrs, bet mazāk precīzs)\n• <b>1 - LSTM:</b> Neironu dzinējs (lēnāks, bet precīzāks)\n• <b>2 - Legacy + LSTM:</b> Apvieno abus rezultātus\n• <b>3 - Noklusējums (LSTM vēlams):</b> Labākā izvēle vairumā gadījumu\n\nIeteikums: <b>3</b> maksimālai atpazīšanas precizitātei.",

        "ocr_optimize_explain": "Saspiež izvades PDF.\n\n• <b>0:</b> Bez optimizācijas (ātrākā apstrāde)\n• <b>1:</b> Viegla optimizācija (labs kompromiss)\n• <b>2:</b> Mērena optimizācija\n• <b>3:</b> Spēcīga optimizācija (mazākais fails, bet lēnāks)\n\nIeteikums: <b>1</b> ikdienas lietošanai.",

        "ocr_jobs_explain": "Paralēlo procesu skaits OCR.\n\n• <b>1:</b> Lēns, bet viszemākais atmiņas patēriņš\n• <b>4-8:</b> Optimāls mūsdienu daudzkodolu procesoriem\n• <b>12+:</b> Tikai nedaudz ātrāka apstrāde ar augstu atmiņas patēriņu\n\nIeteikums: CPU kodolu skaits (piem., <b>4</b> 4-kodolu sistēmās).",

        "ocr_verbose_explain": "Žurnāla izvades detalizācijas līmenis konsolē.\n\n• <b>0:</b> Nav izvades\n• <b>1:</b> Progress un statusa ziņojumi\n• <b>2:</b> Detalizēta izvade\n• <b>3:</b> Pilna atkļūdošanas izvade (ļoti apjomīga)\n\nIeteikums: <b>1</b> normālai darbībai.",

        "ocr_reset_title": "Iestatījumi ir atiestatīti",
        "ocr_reset_message": "Visi OCR iestatījumi ir atiestatīti uz noklusējuma vērtībām.",
        "info_tooltip": "Vairāk informācijas par šo parametru",
        "ocr_reset_defaults": "Atiestatīt uz noklusējumu",

        "ocr_psm_0": "Automātiski (Legacy dzinējs)",
        "ocr_psm_1": "Automātiska kolonnu noteikšana",
        "ocr_psm_3": "Automātiski (Noklusējums)",
        "ocr_psm_4": "Viena kolonna",
        "ocr_psm_5": "Vertikāls bloks",
        "ocr_psm_6": "Vienveidīgs teksta bloks",
        "ocr_psm_7": "Viena teksta rinda",
        "ocr_psm_8": "Viens vārds",
        "ocr_psm_11": "Neapstrādāts attēls (bez izkārtojuma analīzes)",

        "ocr_oem_0": "Legacy dzinējs (ātrs)",
        "ocr_oem_1": "LSTM dzinējs (neironu, precīzs)",
        "ocr_oem_2": "Legacy + LSTM kombinēts",
        "ocr_oem_3": "Noklusējums (LSTM vēlams)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR valoda(s)...",
        "ocr_language_title": "Izvēlēties OCR valodu(as)",
        "ocr_language_instruction": "Izvēlieties valodu(as) teksta atpazīšanai (OCR).\nUzmanību: Vairākas valodas ietekmē veiktspēju un precizitāti!\nVislabākos rezultātus sasniegsiet, ja izvēlēsieties tikai vienu valodu.",
        "ocr_language_predefined": "Iepriekš noteiktas kombinācijas",
        "ocr_language_custom": "Pielāgots...",
        "ocr_language_selected": "Izvēlētās OCR valodas",
        "ocr_language_changed": "OCR valoda mainīta uz {0}",
        "ocr_language_auto_detect": "Pieejamās valodas tiek atklātas automātiski.",
        "ocr_language_none_found": "Nav atrasti Tesseract valodas dati! Lūdzu, instalējiet valodu pakotnes (piem., 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Pielāgota valodas izvēle",
        "ocr_language_available": "Pieejamās valodas (instalētas):",
        "ocr_language_select_hint": "Izvēlieties vienu vai vairākas valodas:",
        "ocr_language_confirm": "Lietot",
        "ocr_language_reset": "Atiestatīt uz noklusējumu (deu+eng+vie)",
        "ocr_language_priorities": "Ieteicamās valodas (iepriekš instalētas):",

        "select_all_languages": "Izvēlēties visu",
        "clear_all_languages": "Notīrīt izvēli",
        "install_language_packs": "Instalēt trūkstošās valodu pakotnes...",
        "install_hint": "💡 Padoms: Ne visas valodas ir instalētas jūsu sistēmā. Izmantojot šo pogu, saņemsiet palīdzību instalēšanai.",
        "ocr_language_install_title": "Tesseract valodu pakotņu instalēšana",

        "ocr_missing_languages": "Trūkstošās OCR valodu pakotnes",
        "ocr_missing_languages_message": "Šīs izvēlētās valodas nav instalētas jūsu sistēmā:\n\n{0}\n\nLūdzu, instalējiet trūkstošās valodu pakotnes (skatiet palīdzību sadaļā 'Instalēšanas palīdzība').\n\nVai vēlaties tagad atvērt instalēšanas palīdzību?",
        "ocr_missing_languages_voice": "Trūkstošas valodu pakotnes. Lūdzu, instalējiet trūkstošās valodas.",
        "ocr_install_help_now": "Atvērt palīdzību",
        "ocr_continue_anyway": "Tomēr mēģināt",
        "ocr_language_error_title": "OCR valodas kļūda",
        "ocr_language_error_message": "Kļūda teksta atpazīšanas laikā: {0}\n\nLūdzu, pārbaudiet savus OCR valodas iestatījumus (Iestatījumi → OCR valoda).",
        "ocr_install_help_button": "Instalēšanas palīdzība",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalēt Tesseract valodu pakotnes</p>

        <p>Lai OCR darbotos noteiktā valodā, attiecīgajiem valodas datiem jābūt instalētiem jūsu sistēmā. Izpildiet norādījumus savai operētājsistēmai:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Atveriet <strong>Termināli</strong> (Finder → Programmas → Utilītas → Terminālis).</li>
        <li>Instalējiet visas pieejamās valodas ar:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Tas var aizņemt dažas minūtes.)</li>
        <li>Vai tikai atsevišķas valodas (piem., vjetnamiešu):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Ar pašreizējām Homebrew versijām, <code>*.traineddata</code> var būt jālejupielādē manuāli (skatīt zemāk).</li>
        <li>Pēc instalēšanas: Aizveriet šo dialogu un atveriet OCR valodas izvēli vēlreiz – jaunās valodas parādīsies automātiski.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Atveriet termināli (Ctrl+Alt+T).</li>
        <li>Instalējiet vēlamo valodu, piem., vjetnamiešu:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Svarīgi valodu kodi: <code>deu</code> (vācu), <code>eng</code> (angļu), <code>vie</code> (vjetnamiešu), <code>spa</code> (spāņu), <code>fra</code> (franču), <code>ita</code> (itāļu), <code>nld</code> (holandiešu), <code>fin</code> (somu), <code>swe</code> (zviedru), <code>nor</code> (norvēģu).</li>
        <li>Parādīt visas pieejamās pakotnes:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuāli)</p>
        <ol>
        <li>Lejupielādējiet vēlamos <code>*.traineddata</code> failus no:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (piem., <code>vie.traineddata</code> vjetnamiešu valodai).</li>
        <li>Kopējiet failus uz Tesseract valodu mapi, parasti:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Pielāgojiet atbilstoši individuālai instalācijai.)</li>
        <li>Restartējiet lietojumprogrammu (vai atveriet OCR valodas izvēli vēlreiz).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatīva visām sistēmām</p>
        <ul>
        <li>Instalējiet <strong>OCRmyPDF</strong> un <strong>Tesseract</strong> ar jūsu izvēlēto pakotņu pārvaldnieku. Lielākajā daļā instalāciju jau ir dažas standarta valodas (angļu, vācu, franču).</li>
        <li>Trūkstošās valodas var instalēt jebkurā laikā – OCR valodas izvēle parāda tikai faktiski esošās valodas.</li>
        </ul>

        <hr>
        <p><b>✅ Pēc instalēšanas:</b> Nav nepieciešams restartēt lietojumprogrammu – jaunpievienotās valodas uzreiz parādīsies sarakstā.</p>
        <p><b>📖 Palīdzība par valodu kodiem:</b> Pilns saraksts ir pieejams <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract dokumentācijā</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans burtveidoli",
        "info_noto_font_voice": "Noto Sans burtveidolu instalēšanas ceļvedis",
        "btn_info_noto_font_install": "Burtveidola informācija",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Kā instalēt Google bezmaksas Noto burtveidolus</h2>

        <p><strong>Noto burtveidoli</strong> ir Google atvērtā koda burtveidolu saime. To mērķis ir neredzēt <em>"nekādu tofu"</em> (t.i., bez tukšām kastītēm □) un pareizi attēlot katru Unicode standarta rakstzīmi. Tie ir ideāls papildinājums lietojumprogrammām, kurām jāattēlo teksti daudzās dažādās valodās.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalēšana macOS</h3>

        <p><strong>Metode 1: Ar Homebrew (pieredzējušiem lietotājiem)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metode 2: Izmantojot "Font Book" (Ieteicams)</strong></p>

        <ol>
        <li>Lejupielādējiet oficiālo burtveidolu pakotni:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Atarhivējiet ZIP failu</li>
        <li>Kopējiet failus uz <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalēšana Windows (10 un 11)</h3>

        <p><strong>Metode 1: Microsoft Store (Ieteicams)</strong><br>
        Meklējiet "Google Noto Fonts" vai "Noto Sans" un noklikšķiniet <strong>Instalēt</strong>.</p>

        <p><strong>Metode 2: Manuāla instalēšana</strong></p>

        <ol>
        <li>Lejupielāde:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Atarhivējiet ZIP</li>
        <li>Izvēlieties .ttf / .otf failus</li>
        <li>Labais klikšķis → <strong>Instalēt</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        vai<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Vārds\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalēšana Linux</h3>

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

        <p>Pārbaude:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Pārvaldīt grāmatzīmes",
        "bookmark_add": "Pievienot grāmatzīmi",
        "bookmark_add_tooltip": "Saglabāt pašreizējo lapu kā grāmatzīmi",
        "bookmark_remove": "Noņemt grāmatzīmi",
        "bookmark_remove_tooltip": "Dzēst atzīmēto grāmatzīmi",
        "bookmark_remove_all": "Noņemt visas",
        "bookmark_remove_all_tooltip": "Dzēst visas šī PDF grāmatzīmes",
        "bookmark_jump": "Pārlēkt uz grāmatzīmi",
        "bookmark_jump_tooltip": "Pārlēkt uz izvēlēto lapu",
        "bookmark_name": "Nosaukums",
        "bookmark_page": "Lapa",
        "bookmark_no_bookmarks": "Nav grāmatzīmju.\nNoklikšķiniet uz 'Pievienot', lai saglabātu pašreizējo lapu kā grāmatzīmi.",
        "bookmark_added": "Pievienota grāmatzīme lapai {0}: {1}",
        "bookmark_removed": "Grāmatzīme noņemta: {0}",
        "bookmark_all_removed": "Visas grāmatzīmes ir noņemtas.",
        "bookmark_name_default": "Lapa {0}",
        "bookmark_name_prompt": "Grāmatzīmes nosaukums:\n(garš teksts tiks saīsināts līdz 50 rakstzīmēm)",
        "bookmark_name_prompt_title": "Grāmatzīmes nosaukums",
        "bookmark_confirm_remove_all": "Vai tiešām vēlaties noņemt visas {0} grāmatzīmes?",
        "menu_bookmarks": "Grāmatzīmes",
        "bookmark_manage": "Pārvaldīt grāmatzīmes",
        "bookmark_next": "Nākamā grāmatzīme",
        "bookmark_prev": "Iepriekšējā grāmatzīme",
        "bookmark_page_display": "Lapa {0}",
        "bookmark_exists": "Grāmatzīme šai lapai ar šo nosaukumu jau pastāv.",
        "bookmark_select_first": "Vispirms izvēlieties grāmatzīmi.",
        "bookmark_confirm_remove": "Vai tiešām vēlaties noņemt grāmatzīmi 'Lapa {0}: {1}'?",
        "bookmark_jumped_to": "Pārlēkts uz grāmatzīmi '{0}' {1}. lapā.",
        "bookmark_jumped_to_voice": "Grāmatzīme {0}, {1}. lapa",
        "btn_close": "Aizvērt",

        "bookmark_list": "Jūsu grāmatzīmes",
        "bookmark_rename": "Pārdēvēt grāmatzīmi",
        "bookmark_rename_tooltip": "Mainīt izvēlētās grāmatzīmes nosaukumu",
        "bookmark_rename_title": "Pārdēvēt grāmatzīmi",
        "bookmark_rename_prompt": "Jauns nosaukums grāmatzīmei {0}. lapā:\n(maks. 50 rakstzīmes)",
        "bookmark_renamed": "Grāmatzīme '{0}' ir pārdēvēta par '{1}'.",
        "bookmark_item_tooltip": "{0}. lapa: {1}\nDubultklikšķis, lai pārlēktu",
        "bookmark_name_exists_question": "Grāmatzīme ar nosaukumu '{0}' jau pastāv šajā lapā.\nVienalga pārdēvēt?",

        "context_bookmarks": "Grāmatzīmes",
        "context_bookmark_add_here": "Pievienot grāmatzīmi šai lapai",
        "context_bookmarks_existing": "Esošās grāmatzīmes:",
        "context_bookmarks_jump": "Pārlēkt uz grāmatzīmi:",
        "context_bookmarks_none": "Nav grāmatzīmju",
        "context_bookmarks_clear_all": "Noņemt visas {0} grāmatzīmes",

        "bookmark_search_placeholder": "Meklēt grāmatzīmes... (nosaukums vai lapa)",
        "bookmark_search_results": "Atrastas %d grāmatzīmes \"%s\"",
        "bookmark_no_search_results": "Nav atrastas grāmatzīmes \"%s\"",
        "bookmark_no_search_results_label": "Nav rezultātu \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Rediģēt PDF metadatus",
        "metadata_title": "Nosaukums",
        "metadata_title_placeholder": "Dokumenta nosaukums",
        "metadata_title_tooltip": "Dokumenta nosaukums (tiek parādīts nosaukuma joslā)",
        "metadata_author": "Autors",
        "metadata_author_placeholder": "Autora vārds",
        "metadata_author_tooltip": "Dokumenta veidotājs",
        "metadata_subject": "Tēma",
        "metadata_subject_placeholder": "Dokumenta tēma",
        "metadata_subject_tooltip": "Īss satura apraksts",
        "metadata_keywords": "Atslēgvārdi",
        "metadata_keywords_placeholder": "Atslēgvārdi, atdalīti ar komatiem",
        "metadata_keywords_tooltip": "Atslēgvārdi dokumenta kategorizēšanai",
        "metadata_creator": "Veidotājs",
        "metadata_creator_placeholder": "Lietojumprogramma, kas izveidoja PDF",
        "metadata_creator_tooltip": "Programmatūra, ar kuru dokuments tika izveidots",
        "metadata_producer": "Producents",
        "metadata_producer_placeholder": "Lietojumprogramma, kas konvertēja PDF",
        "metadata_producer_tooltip": "Programmatūra, kas konvertēja PDF",
        "metadata_creation_date": "Izveides datums",
        "metadata_creation_date_tooltip": "Dokumenta izveides datums",
        "metadata_mod_date": "Modifikācijas datums",
        "metadata_mod_date_tooltip": "Pēdējās modifikācijas datums",
        "metadata_pdf_info": "📄 PDF informācija",
        "metadata_pages": "Lapu skaits",
        "metadata_file_size": "Faila lielums",
        "metadata_pdf_version": "PDF versija",
        "metadata_encrypted": "Šifrēts",
        "metadata_encrypted_yes": "Jā (aizsargāts ar paroli)",
        "metadata_encrypted_no": "Nē",
        "metadata_reload": "📂 Pārlādēt no PDF",
        "metadata_reset": "Atmest izmaiņas",
        "metadata_reloaded": "Metadati ir pārlādēti no PDF.",
        "metadata_reset_done": "Visi metadatu lauki ir atiestatīti.",
        "metadata_no_file": "Nav ielādēts PDF fails.",
        "metadata_save_error": "Kļūda, saglabājot metadatus",
        "metadata_saved": "Metadati ir veiksmīgi saglabāti.",
        "metadata_pdf_version_unknown": "PDF (nezināms)",
        "metadata_saved_message": "Metadati ir veiksmīgi saglabāti.",
        "metadata_saved_voice": "Metadati saglabāti.",

        "metadata_custom": "🔧 Pielāgoti metadati",
        "metadata_custom_placeholder": "{\n  \"mans_lauks\": \"mana_vērtība\",\n  \"cits_lauks\": 123\n}",
        "metadata_custom_tooltip": "JSON formāts pielāgotiem metadatiem (neobligāti)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Izvēlēta veidne \"{0}\" - Divreiz noklikšķiniet, lai ievietotu",
        "text_use_template": "Izmantot teksta bloku",
        "text_type": "Tips",
        "text_search_templates": "Meklēt teksta blokus...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Eksporta / Importa informācija",
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

        <h3>📦 Kas tiek eksportēts? (Pārskats)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Vispārējie lietojumprogrammas iestatījumi</span></li>
            <li class="detail">• Tumšais/Gaišais režīms</li>
            <li class="detail">• Tumšā režīma inversija attēliem</li>
            <li class="detail">• Pelēkā sliekšņa vērtība</li>
            <li class="detail">• Valoda</li>
            <li class="detail">• Loga ģeometrija</li>
            <li class="detail">• Tālummaiņas režīms</li>
            <li class="detail">• Navigācija (Navigācijas josla redzama)</li>
            <li class="detail">• Runas izvade (ieslēgts/izslēgts)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Dublēšanas iestatījumi</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Failu nosaukšana (Laika zīmogs, Atdalītājs, Piedēkļi)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Iestatījumi ievietošanai</span></li>
            <li class="detail">• Paraksti</li>
            <li class="detail">• Teksts un teksta bloki</li>
            <li class="detail">• Atzīmes, attēli un formas</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR iestatījumi</span></li>
            <li class="detail">• Valoda</li>
            <li class="detail">• Piespiest OCR · Lapas režīms</li>
            <li class="detail">• Attēla pirmapstrāde: Labot slīpumu, Notīrīt, Pārparaugu ņemšana</li>
            <li class="detail">• Paralēlo darbu skaits</li>
            <li class="detail">• Inversijas režīms</li>
            <li class="detail">• Pelēkā sliekšņa vērtība</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Grāmatzīmes</span></li>
            <li class="detail">• Visas grāmatzīmes vienā PDF failā (Lapa, Nosaukums, Izveides laiks)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Paroļu datubāze</span></li>
            <li class="detail">• Saglabātās PDF paroles (pēc izvēles šifrētas vai vienkāršs teksts)</li>
            <li class="detail">• Galvenās paroles jaucējvērtība (ja iestatīta)</li>
            <li class="detail">• Verifikācijas dati</li>
        </ul>

        <h4>⚠️ Svarīgas piezīmes</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Importējot:</strong>
            <ul>
                <li><span class="warning">➜ VISI pašreizējie iestatījumi tiks pilnībā pārrakstīti</span></li>
                <li>• Lietojumprogrammas restartēšana ir obligāta</li>
                <li>• Esošie paraksti, teksta bloki un grāmatzīmes tiks aizstāti</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Galvenā parole un eksporta režīms:</strong>
            <ul>
                <li>• Kad galvenā parole ir aktīva, varat izvēlēties:</li>
                <li>  - <span style="color: #98FB98;"><strong>Atšifrēts</strong></span> (paroles ir vienkāršā tekstā ZIP failā)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Šifrēts</strong></span> (tikai lasāms ar galveno paroli mērķa sistēmā)</li>
                <li>• Galvenās paroles jaucējvērtība <strong>vienmēr</strong> tiek glabāta šifrēta</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Drošības paziņojums:</strong>
            <ul>
                <li>• Eksportētais ZIP fails satur sensitīvus datus (<strong>paroles, grāmatzīmes, parakstus</strong>)</li>
                <li>• Lūdzu, glabājiet to drošībā (piem., šifrētā USB diskā, paroļu pārvaldniekā)</li>
                <li>• Ja fails tiek zaudēts, saglabātās PDF paroles tiek neatgriezeniski zaudētas</li>
            </ul>
        </div>

        <h4>📁 Eksporta formāts</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Iestatījumi tiek saglabāti vienā ZIP failā:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Šis ZIP satur pilnu <code>settings.json</code> (no jūsu konfigurācijas) kā arī iespējamos iegultos paraksta attēlu failus un šifrētās paroles.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Paraksti - Ceļvedis",
        'signature_guide_html': """
        📝 <strong>Paraksti - Īsais ceļvedis</strong><br>
        <ul>
        <li>Iestatīt galveno paroli</li>
        <li>Konfigurēt parakstus izvēlnē <em>Iestatījumi</em> (izmērs, laika zīmogs, …)</li>
        <li>Ievietot ar <strong>LABO KLIKŠĶI</strong> vēlamajā pozīcijā (galvenā parole nepieciešama vienu reizi sesijā)</li>
        <li>Pārvietot parakstu ar peli vai bulttaustiņiem</li>
        <li>Ievietot vairākus parakstus pēc kārtas</li>
        <li>Pielāgot katru parakstu individuāli</li>
        <li>Noraidīt atsevišķu parakstu</li>
        <li>Saglabāt / noraidīt visus parakstus vienlaikus</li>
        <li>Alternatīvi, var izmantot arī izvēļņu joslu.</li>
        </ul>
        """,
        'signature_guide_voice': "Īsais ceļvedis parakstiem. Iestatīt galveno paroli. Konfigurēt parakstus iestatījumos. Ievietot ar labo klikšķi.",

        'image_guide_title': "Ievietot attēlus - Ceļvedis",
        'image_guide_html': """
        📷 <strong>Attēlu ievietošana PDF - Īsais ceļvedis</strong><br>
        <ol>
        <li>Labais klikšķis vēlamajā pozīcijā</li>
        <li><em>„Ievietot attēlu“</em> → Izvēlēties attēlu</li>
        <li>Novietot attēlu: Vilkt ar peli</li>
        <li>Pielāgot izmēru: Vilkt aiz stūriem/malām</li>
        <li>Saglabāt malu attiecību: Taustiņš <strong>[A]</strong></li>
        <li>Turpmāki pielāgojumi: Labais klikšķis uz attēla</li>
        </ol>
        <p><strong>Padoms:</strong> Konteksta izvēlnē varat pielāgot iestatījumus.</p>
        """,
        'image_guide_voice': "Īsais ceļvedis attēliem. Labais klikšķis, ievietot attēlu, izvēlēties. Novietot ar peli, pielāgot izmēru aiz stūriem. Malu attiecība ar taustiņu A.",

        'form_guide_title': "Ievietot formas - Ceļvedis",
        'form_guide_html': """
        📐 <strong>Formu ievietošana PDF - Īsais ceļvedis</strong><br>
        <ol>
        <li>Izvēlēties formas tipu (taisnstūris, elipse, līnija, bultiņa)</li>
        <li>Noklikšķināt uz pozīcijas:
            <ul>
            <li>Taisnstūrim/elipsei: Viens klikšķis novieto formu</li>
            <li>Līnijai/bultiņai: Divi klikšķi sākuma un beigu punktam</li>
            </ul>
        </li>
        <li>Novietot formu: Vilkt ar peli</li>
        <li>Pielāgot izmēru: Vilkt aiz stūriem/malām</li>
        <li>Saglabāt formu: <strong>Enter</strong></li>
        <li>Noraidīt formu: <strong>ESC</strong></li>
        <li>Turpmāki pielāgojumi: Labais klikšķis uz formas</li>
        </ol>
        <p><strong>Padoms:</strong> Konteksta izvēlnē varat pielāgot iestatījumus.</p>
        """,
        'form_guide_voice': "Īsais ceļvedis formām. Izvēlēties formas tipu. Taisnstūrim vai elipsei noklikšķiniet vienu reizi, līnijai vai bultiņai divas reizes. Novietot ar peli, pielāgot izmēru aiz stūriem. Saglabāt ar Enter, noraidīt ar Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "iepriekšējais",
        "btn_next_result": "nākamais",
        "ocr_text_window": "OCR teksta logs",
        "bookmark_existing": "Esošās grāmatzīmes",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR salīdzinājums Mac - Windows",
        'ocr_method_mac_win_title': "OCR atšķirības starp Mac un Windows",
        'ocr_method_mac_win_voice': "Mac ir labāks",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Atšķirības starp macOS un Windows</strong></p>

        <p><strong>macOS (ieteicams)</strong></p>
        <p>Rīks:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Rezultāts:</p>
        <ul>
        <li>Meklējams PDF ar iegultu tekstu, kas lielā mērā saglabā sākotnējo izkārtojumu.</li>
        </ul>
        <p>Priekšrocības:</p>
        <ul>
        <li>Lieliska teksta atpazīšanas kvalitāte (pat šķībās lapās).</li>
        <li>Vektorgrafikas un fontu saglabāšana.</li>
        <li>GUI progresa josla, izmantojot apakšprocesa novērtēšanu.</li>
        <li>Pilnīga kontrole pār visiem OCR parametriem (Deskew, Clean, Oversample, optimizācija).</li>
        <li>Teksta meklēšana ir tieši pieejama galvenajā logā (PDF skats).</li>
        </ul>
        <p>Trūkumi:</p>
        <ul>
        <li>Nepieciešami papildu sistēmas rīki (ocrmypdf, Ghostscript, unpaper, pngquant – iekļauti lietotnes komplektā).</li>
        <li>Sarežģītāka kļūdu apstrāde (bloķēšanās, taimauti).</li>
        </ul>

        <p><strong>Windows (stabila alternatīva)</strong></p>
        <p>Rīks:</p>
        <ul>
        <li>pytesseract (tiešs savienojums ar Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Rezultāts:</p>
        <ul>
        <li>Meklējams PDF, kas vizuāli atbilst attēla PDF, bet ir meklējams caur caurspīdīgo tekstu.</li>
        </ul>
        <p>Priekšrocības:</p>
        <ul>
        <li>Neviena neienāk prātā šobrīd.</li>
        </ul>
        <p>Trūkumi:</p>
        <ul>
        <li>PDF būtībā ir attēls ar neredzamu tekstu; izkārtojums sarežģītos dokumentos (kolonnas, tabulas) var nedaudz atšķirties.</li>
        <li>Nav automātiskas slīpuma korekcijas (--deskew) vai attēla tīrīšanas (--clean).</li>
        <li>GUI progresa josla tiek atjaunināta tikai aptuveni, pamatojoties uz apstrādāto lappušu skaitu.</li>
        <li>OCR ātrums ir nedaudz lēnāks (jo katra lapa tiek apstrādāta atsevišķi).</li>
        <li>Teksta meklēšana tiek novirzīta uz OCR teksta logu.</li>
        </ul>

        <p><strong>Kopīgās iezīmes</strong></p>
        <ul>
        <li>Abas metodes izveido meklējamu PDF tajā pašā direktorijā, kur atrodas avota fails.</li>
        <li>OCR iestatījumus (valoda, DPI, lapas segmentācijas režīms, OCR dzinēja režīms) var konfigurēt, izmantojot OCRSettingsDialog, un tie darbojas abās implementācijās.</li>
        </ul>

        <p><strong>Ieteikums:</strong></p>
        <ul>
        <li>macOS: ocrmypdf binārais fails sniedz vislabākos rezultātus – Pērciet Mac un izmantojiet versiju (PDFDarkView Mac datoriem ar Apple Silicon vai Intel mikroshēmu). OCR rezultāti ir labāki nekā Windows!</li>
        <li>Windows: Izmantojiet pytesseract risinājumu. Tas ir stabils un sniedz pilnīgi pietiekamu kvalitāti lielākajai daļai dokumentu.</li>
        </ul>

        <p><strong>Svarīga piezīme:</strong></p>
        <ul>
        <li>Abas versijas ir pilnībā integrētas lietotāja saskarnē – lietotājs nepamana nekādu atšķirību.</li>
        <li>Programma automātiski izlemj, kuru OCR dzinēju izmantot, pamatojoties uz operētājsistēmu.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Izveidot parakstu (no skenēšanas)",
        "signature_create_title": "Izvēlēties skenētu parakstu (PDF/attēls)",
        "image_pdf_filter": "Attēli un PDF",
        "signature_pdf_empty": "PDF nesatur lapas.",
        "signature_created_success": "Paraksts veiksmīgi izveidots: {0}",
        "signature_create_error": "Kļūda, veidojot parakstu:\n{0}",
        "rembg_missing": "rembg nav instalēts.\nLūdzu, instalējiet: pip install rembg\nKļūda: {0}",
        "signature_name_title": "Faila nosaukums parakstam",
        "signature_name_message": "Lūdzu, ievadiet faila nosaukumu jaunajam parakstam (tiks saglabāts kā PNG ar caurspīdīgu fonu):",
        "signature_name_label": "Faila nosaukums:",
        "signature_name_voice": "Ievadiet faila nosaukumu parakstam",
        "signature_processing": "Apstrāde notiek...",
        "signature_creation_title": "Paraksts tiek izveidots",
        "signature_overwrite_warning": "Fails '{0}' jau pastāv. Pārrakstīt?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Sagatavot PDF parakstam",
        "signature_prepare_instruction":"Lūdzu, izvēlieties PDF, kas vienā lapā satur skenētu parakstu.\n\nLai sasniegtu optimālu atpazīšanu:\n• Parakstam jābūt uzrakstītam ar melnu tinti (lodīšu pildspalvu vai smalku flomāsteru) uz balta papīra.\n• Parakstam jāatrodas citādi tukšas A4 lapas augšējā trešdaļā.\n• PDF jābūt skenētam ar vismaz 300 dpi.\n• Parakstam jābūt skaidram un ne pārāk tievam.\n• Nedrīkst būt traucējošu fona rakstu vai līniju.",
        "signature_prepare_voice":"Lūdzu, izvēlieties PDF ar skenētu parakstu. Pievērsiet uzmanību labai kvalitātei un kontrastam.",
        "sig_thickness_label":"Līnijas biezums:",
        "sig_thickness_normal":"Normāls (plāns)",
        "sig_thickness_bold":"Treknrakstā (ieteicams)",
        "sig_thickness_very_bold":"Ļoti trekns",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Pievienot GUI un OCR valodas - Ceļvedis",
        'language_guide_title': "Pievienot GUI un OCR valodas",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Lejupielādējiet vēlamo tulkojuma failu <code>translations_xy.py</code> no<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        un ievietojiet to šajā direktorijā:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Atveriet savu tīmekļa pārlūkprogrammu.</li>
        <li>Dodieties uz: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Meklējiet ekrāna labajā malā "Releases" un izvēlieties to, kas atzīmēts ar <strong>"latest"</strong>.</li>
        <li>Nākamajā laidiena lapā lejupielādējiet failu <code>Source Code.zip</code> pašā apakšā.</li>
        <li>Izpakojiet ZIP failu.</li>
        <li>Izpakojot mapē, atrodiet visus nepieciešamos valodas failus un kopējiet tos direktorijā:<br/>
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
        "menu_watermark":"Ievietot ūdenszīmi",
        "fullpage_text_watermark_title":"Teksts kā ūdenszīme",
        "fullpage_image_watermark_title":"Attēls kā ūdenszīme",
        "filename_with_watermark":"_ar_ūdenszīmi",
        "watermark_text":"Teksts:",
        "watermark_text_placeholder":"Jūsu ūdenszīmes teksts...",
        "watermark_font_family":"Fonts:",
        "watermark_font_size":"Fonta lielums:",
        "watermark_format":"Formatējums:",
        "watermark_bold":"Treknraksts",
        "watermark_italic":"Slīpraksts",
        "watermark_color":"Krāsa:",
        "watermark_choose_color":"Izvēlieties krāsu...",
        "watermark_opacity":"Necaurredzamība / Caurspīdīgums:",
        "watermark_direction":"Lasīšanas virziens:",
        "watermark_direction_l_r":"Kreisā → Labā",
        "watermark_direction_bl_tr":"Apakšā kreisā → Augšā labā",
        "watermark_direction_tl_br":"Augšā kreisā → Apakšā",
        "watermark_direction_b_t":"Apakšā → Augšā",
        "watermark_direction_t_b":"Augšā → Apakšā",
        "watermark_preview":"Priekšskatījums:",
        "watermark_preview_sample":"Piemēra teksts",
        "watermark_empty_text":"Lūdzu, ievadiet tekstu.",
        "watermark_applied":"Ūdenszīme tika piemērota visām lapām.",
        "watermark_saved":"Ūdenszīme saglabāta.",
        "image_scale":"Izmērs:",
        "image_preview":"Attēla priekšskatījums:",
        "no_image_selected":"Nav izvēlēts neviens attēls",
        "browse":"Pārlūkot...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Izsvītrojumi",
        "redact_add_black": "Izsvītrojums (melns)",
        "redact_add_white": "Izsvītrojums (balts / dzēst)",
        "redact_added_black": "Pievienots melns izsvītrojums",
        "redact_added_white": "Pievienots balts izsvītrojums",
        "redact_apply_all": "Piemērot visus izsvītrojumus un saglabāt",
        "redact_discard_all": "Atmest visus izsvītrojumus",
        "redact_discard": "Atmest šo izsvītrojumu",
        "no_redactions": "Nav izsvītrojumu",
        "redact_confirm_title": "Piemērot izsvītrojumus pastāvīgi",
        "redact_confirm_message": "Brīdinājums: Atzīmētie apgabali tiks neatgriezeniski dzēsti (melni vai balti).\nTiks izveidota rezerves kopija (ja iespējots).\n\nTurpināt?",
        "redact_apply": "Jā, izsvītrot tagad",
        "redact_saved": "{0} izsvītrojums(-i) veiksmīgi piemērots(-i) un saglabāts(-i).",
        "redact_saved_voice": "{0} izsvītrojums(-i) piemērots(-i)",
        "redact_error": "Kļūda izsvītrošanas laikā",
        "filename_redacted":"_izsvītrots",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Ievietot lappušu numurus',
        'page_numbers_format': 'Numura formāts:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arābu)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (romiešu mazie)',
        'page_numbers_format_roman_upper': 'I, II, III ... (romiešu lielie)',
        'page_numbers_format_letter': 'A, B, C ... (burti)',
        'page_numbers_format_custom': 'Pielāgots',
        'page_numbers_custom_pattern': 'Raksts:',
        'page_numbers_custom_placeholder': 'piem., "Lapa {nummer}" vai "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Izmantojiet {nummer} pašreizējam lappuses numuram un {total} kopējam skaitam',
        'page_numbers_position': 'Pozīcija:',
        'page_numbers_pos_tl': 'Augšā kreisā',
        'page_numbers_pos_tc': 'Augšā centrā',
        'page_numbers_pos_tr': 'Augšā labā',
        'page_numbers_pos_ml': 'Vidū kreisā',
        'page_numbers_pos_mc': 'Centrēts',
        'page_numbers_pos_mr': 'Vidū labā',
        'page_numbers_pos_bl': 'Apakšā kreisā',
        'page_numbers_pos_bc': 'Apakšā centrā',
        'page_numbers_pos_br': 'Apakšā labā',
        'page_numbers_margins': 'Maliņas:',
        'page_numbers_margin_x': 'Horizontālais attālums:',
        'page_numbers_margin_y': 'Vertikālais attālums:',
        'page_numbers_range': 'Lappušu diapazons:',
        'page_numbers_all_pages': 'Visas lapas',
        'page_numbers_custom_range': 'Pielāgots diapazons',
        'page_numbers_from': 'No:',
        'page_numbers_to': 'Līdz:',
        'page_numbers_progress': 'Ievieto lappušu numurus...',
        'page_numbers_start': 'Sāk lappušu numuru ievietošanu...',
        'page_numbers_cancel': 'Lappušu numuru ievietošana atcelta',
        'page_numbers_success': 'Lappušu numuri tika veiksmīgi pievienoti.\n\nVai vēlaties atvērt jauno PDF?\n\n{0}',
        'page_numbers_complete': 'Lappušu numuri pievienoti',
        'page_numbers_error_format': 'Kļūda, ievietojot lappušu numurus: {0}',
        'page_numbers_content_type': 'Satura veids:',
        'page_numbers_tab_simple': 'Vienkāršs numurs',
        'page_numbers_tab_range': 'Lapa X no Y',
        'page_numbers_tab_date': 'Datums',
        'page_numbers_tab_custom': 'Brīvs teksts',
        'page_numbers_range_format': 'Formāts:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Lapa {aktuell} no {gesamt}',
        'page_numbers_range_custom': 'Pielāgots',
        'page_numbers_range_placeholder': 'piem., "Lapa {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Datuma formāts:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '2024. gada 1. janvāris',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Pielāgots',
        'page_numbers_date_placeholder': 'piem., %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Pozīcija:',
        'page_numbers_date_before': 'Datums pirms lappuses numura',
        'page_numbers_date_after': 'Datums pēc lappuses numura',
        'page_numbers_date_only': 'Tikai datums (bez lappuses numura)',
        'page_numbers_custom_text': 'Pielāgots teksts:',
        'page_numbers_custom_placeholder_text': 'Izmantojiet {seite} lappuses numuram un {gesamt} kopējam skaitam\npiem., "Konfidenciāli - Lapa {seite}" vai "{seite} no {gesamt}"',
        "filename_with_page_number":"_ar_lappuses_numuru",
        "filename_with_page_declaration":"_ar_lappuses_deklarāciju",
        "filename_with_pagenumber":"_ar_lappuses_numuru",
        "filename_with_date":"_ar_datumu",
        "filename_with_my_page_declaration":"_ar_pielāgotu_lappuses_deklarāciju",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Nesaglabātas izmaiņas",
        "unsaved_changes_message_darkmode": "Ir nesaglabāti ievietojumi.\nVai vēlaties tos saglabāt pirms pārslēgšanas?",
        "save_and_switch": "Saglabāt un pārslēgt",
        "discard_and_switch": "Pārslēgt tagad",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Eksportēt lapas kā attēlus',
        'export_images_menu': 'Eksportēt kā attēlus (PNG/JPEG)',
        'export_images_format': 'Attēla formāts:',
        'export_images_dpi': 'Izšķirtspēja (DPI):',
        'export_images_quality': 'JPEG kvalitāte:',
        'export_images_range': 'Lappušu diapazons:',
        'export_images_all_pages': 'Visas lapas',
        'export_images_custom_range': 'Pielāgots diapazons',
        'export_images_from': 'No:',
        'export_images_to': 'Līdz:',
        'export_images_options': 'Opcijas:',
        'export_images_single_files': 'Katra lapa kā atsevišķs fails',
        'export_images_subfolder': 'Eksportēt uz apakšmapi',
        'export_images_subfolder_info': 'Uz apakšmapi "PDFnosaukums_attēli"',
        'export_images_same_folder': 'Tajā pašā mapē kā PDF',
        'export_images_apply_darkmode': 'Piemērot PDFDarkView iestatījumus (Tumšais režīms)',
        'export_images_target_folder': 'Mērķa mape:',
        'export_images_browse': 'Pārlūkot...',
        'export_images_preview': 'Priekšskatījums:',
        'export_images_preview_info': 'Izvēlieties eksporta iestatījumus',
        'export_images_preview_info_detail': '{0} lapas kā {1}\nIzšķirtspēja: {2} DPI\nFaila nosaukums: {3}\n{4}',
        'export_images_select_folder': 'Izvēlieties mērķa mapi',
        'export_images_start': 'Sāk attēlu eksportu...',
        'export_images_progress': 'Eksportē attēlus...',
        'export_images_saving': 'Saglabā lapu {0} no {1}...',
        'export_images_success': 'Eksports veiksmīgs!\n\n{0} attēli tika saglabāti:\n{1}',
        'export_images_complete': 'Attēlu eksports pabeigts',
        'export_images_open_folder': '📁 Atvērt mapi',
        'export_images_cancel': 'Attēlu eksports atcelts',
        'export_images_error_format': 'Kļūda, eksportējot attēlus: {0}',
        'export_images_pdf2image_missing': 'Bibliotēka "pdf2image" nav instalēta.\n\nLūdzu, instalējiet to ar:\npip install pdf2image\n\nWindows sistēmā jums ir nepieciešams arī Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A konvertēšana ilgtermiņa arhivēšanai',
        'pdfa_menu': 'PDF/A konvertēšana (piemērota arhivēšanai)',
        'pdfa_info': 'Konvertē PDF uz PDF/A formātu.\n\nPDF/A ir īpaši izstrādāts ilgtermiņa arhivēšanai un nodrošina, ka dokuments nākotnē tiks pareizi attēlots.',
        'pdfa_standard': 'PDF/A standarts:',
        'pdfa_standard_select': 'Versija:',
        'pdfa_1': 'PDF/A-1 (vienkāršs, plaši saderīgs)',
        'pdfa_2': 'PDF/A-2 (mūsdienīgs, labāka saspiešana)',
        'pdfa_3': 'PDF/A-3 (jaunākā versija, atļauj pielikumus)',
        'pdfa_standards_explanation': '📖 Standartu skaidrojums:\n\n'
            '• PDF/A-1: Pamata, saderīgs ar vecākām sistēmām (apmēram 2005)\n'
            '• PDF/A-2: Mūsdienīgāks, labāka saspiešana, caurspīdīguma atbalsts (apmēram 2011)\n'
            '• PDF/A-3: Jaunākā versija, atļauj iegult failu pielikumus (apmēram 2013)\n\n'
            'Ieteikums: PDF/A-2 ir labs kompromiss starp saderību un mūsdienīgām funkcijām.',
        'pdfa_options': 'Opcijas:',
        'pdfa_compress_enable': 'Saspiest PDF (mazāks fails)',
        'pdfa_metadata_preserve': 'Saglabāt metadatus (nosaukumu, autoru utt.)',
        'pdfa_target_folder': 'Mērķa mape:',
        'pdfa_browse': 'Pārlūkot...',
        'pdfa_select_folder': 'Izvēlieties mērķa mapi',
        'pdfa_ocr_info_unknown': '🔍 Nevarēja pārbaudīt teksta saturu.',
        'pdfa_ocr_info_not_needed': '✅ Teksts pieejams - OCR nav nepieciešams.\nPDF/A var izveidot tieši.',
        'pdfa_ocr_info_recommended': '⚠️ Nav atrasts pietiekams teksts.\n\nMeklējamiem PDF iesakām vispirms palaist OCR.\nPiezīme: PDF/A darbojas arī bez OCR - bet teksts nebūs meklējams.',
        'pdfa_ocr_info_error': '❌ Kļūda pārbaudes laikā: {0}',
        'pdfa_start': 'Sāk PDF/A konvertēšanu...',
        'pdfa_progress': 'PDF/A konvertēšana notiek...',
        'pdfa_success': 'PDF/A konvertēšana veiksmīga!\n\nSaglabāts kā:\n{0}\n\nVai vēlaties atvērt jauno PDF?',
        'pdfa_complete': 'PDF/A konvertēšana pabeigta',
        'pdfa_cancel': 'PDF/A konvertēšana atcelta',
        'pdfa_error_format': 'Kļūda PDF/A konvertēšanas laikā:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Bibliotēka "ocrmypdf" nav instalēta.\n\nLūdzu, instalējiet to ar:\npip install ocrmypdf',
        'btn_convert': 'Konvertēt',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimizēt PDF (samazināt faila izmēru)',
        'optimize_menu': 'Optimizēt PDF (faila izmērs)',
        'optimize_info': 'Samazina PDF faila izmēru, izmantojot dažādas optimizācijas metodes.\n\nJo augstāks saspiešanas līmenis, jo mazāks fails - ar iespējamu kvalitātes zudumu attēlos.',
        'optimize_level': 'Saspiešanas līmenis:',
        'optimize_level_low': 'Zems (ātrs, neliels ietaupījums)',
        'optimize_level_medium': 'Vidējs (labs kompromiss)',
        'optimize_level_high': 'Augsts (liels ietaupījums)',
        'optimize_level_maximum': 'Maksimāls (maksimāls ietaupījums, lēns)',
        'optimize_level_explanation': 'Ieteikums: "Vidējs" ir labs kompromiss starp ātrumu un faila izmēru.',
        'optimize_options': 'Opcijas:',
        'optimize_compress_images': 'Saspiest attēlus (samazināt JPEG kvalitāti)',
        'optimize_clean_objects': 'Noņemt neizmantotos objektus',
        'optimize_preserve_metadata': 'Saglabāt metadatus (nosaukumu, autoru utt.)',
        'optimize_image_quality': 'Attēla kvalitāte:',
        'optimize_range': 'Lappušu diapazons:',
        'optimize_all_pages': 'Visas lapas',
        'optimize_custom_range': 'Pielāgots diapazons',
        'optimize_from': 'No:',
        'optimize_to': 'Līdz:',
        'optimize_target_folder': 'Mērķa mape:',
        'optimize_browse': 'Pārlūkot...',
        'optimize_select_folder': 'Izvēlieties mērķa mapi',
        'optimize_info_box': 'Informācija',
        'optimize_info_text': 'Optimizācija var ilgt vairākas minūtes lieliem PDF failiem.\n\nAttēli tiek saglabāti ar samazinātu kvalitāti, kas var ievērojami samazināt faila izmēru.',
        'optimize_start': 'Sāk PDF optimizāciju...',
        'optimize_progress': 'Optimizē PDF...',
        'optimize_cancel': 'PDF optimizācija atcelta',
        'optimize_complete': 'PDF optimizācija pabeigta',
        'optimize_error_format': 'Kļūda PDF optimizācijas laikā:\n\n{0}',
        'optimize_success_message': 'PDF optimizācija veiksmīga!\n\nSaglabāts kā:\n{0}\n\nPirms: {1}\nPēc: {2}\nIetaupījums: {3:.1f}%\n\n{4}\n\nVai vēlaties atvērt optimizēto PDF?',
        'optimize_success_message_no_size': 'PDF optimizācija veiksmīga!\n\nSaglabāts kā:\n{0}\n\nIzmēra informācija nav pieejama.\n\nVai vēlaties atvērt optimizēto PDF?',
        'optimize_result_positive': 'Fails tika samazināts par {0:.1f}%.',
        'optimize_result_zero': 'Faila izmērs nav mainījies.',
        'optimize_result_negative': 'Fails ir palielinājies par {0:.1f}%.\nOptimizācija izlaista, oriģinālais fails saglabāts.',
        'btn_optimize': 'Sākt optimizāciju',
        'filename_optimize_low_suffix': '_optimizēts_zems',
        'filename_optimize_medium_suffix': '_optimizēts',
        'filename_optimize_high_suffix': '_optimizēts_augsts',
        'filename_optimize_maximum_suffix': '_optimizēts_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Apgriezt PDF',
        'crop_menu': 'Apgriezt PDF (Crop)',
        'crop_range': 'Piemērot:',
        'crop_all_pages': 'Visas lapas',
        'crop_current_page': 'Tikai pašreizējā lapa',
        'crop_values': 'Apgriešanas vērtības (punktos):',
        'crop_left': 'Kreisā:',
        'crop_right': 'Labā:',
        'crop_top': 'Augšā:',
        'crop_bottom': 'Apakšā:',
        'crop_presets': 'Iepriekš iestatītie:',
        'crop_preset_white': 'Atklāt baltas maliņas',
        'crop_reset': 'Atiestatīt',
        'crop_mouse_hint': '🖱️ Velciet taisnstūri, lai aptuveni izvēlētos apgabalu.\nPēc tam varat precīzi noregulēt vērtības SpinBox lodziņos.\nManuāla regulēšana ar peli nav iespējama.',
        'crop_apply': 'Apgriezt',
        'crop_scope_all': 'Visas lapas',
        'crop_scope_current': 'Pašreizējā lapa',
        'crop_new_size': 'Jauns izmērs: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Nav ielādēts neviens PDF',
        'crop_preview_error': 'Kļūda, ielādējot priekšskatījumu',
        'crop_start': 'Sāk apgriešanu...',
        'crop_progress': 'Apgriež PDF...',
        'crop_success': 'PDF veiksmīgi apgriezts!\n\nSaglabāts kā:\n{0}\n\nVai vēlaties atvērt apgriezto PDF?',
        'crop_complete': 'Apgriešana pabeigta',
        'crop_cancel': 'Apgriešana atcelta',
        'crop_error_format': 'Kļūda apgriešanas laikā:\n\n{0}',
        'filename_crop_suffix': '_apgriezts',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Izlīdzināt PDF (Flatten)',
        'flatten_menu': 'Izlīdzināt PDF (Flatten)',
        'flatten_info': 'PDF izlīdzināšana "iecepina" visus rediģējamos elementus lapas saturā.\n\nPēc tam veidlapu lauki, anotācijas, teksti, krusti, paraksti, attēli un formas vairs nav atsevišķi rediģējami.',
        'flatten_explanation_title': '📖 Kam tas ir noderīgi?',
        'flatten_explanation_text': 'Izlīdzināšana ir nepieciešama šādās situācijās:\n\n'
            '• 📄 Vēlaties sagatavot dokumentu drukāšanai\n'
            '• 🔒 Vēlaties novērst, lai kāds mainītu veidlapu laukus\n'
            '• 📎 Vēlaties "pastāvīgi" iegult anotācijas un komentārus dokumentā\n'
            '• 🖼️ Vēlaties pastāvīgi iegult tekstus, krustus, parakstus, attēlus un formas dokumentā\n'
            '• 📦 Vēlaties sagatavot failu arhivēšanai\n\n'
            'Izlīdzināšana padara PDF mazāku un novērš elementu nejaušu pārvietošanu vai dzēšanu.',
        'flatten_what_title': 'Kas tiek izlīdzināts?',
        'flatten_what_list': '• ✅ Veidlapu lauki (teksta lauki, izvēles rūtiņas, pogas)\n'
            '• ✅ Anotācijas (komentāri, izcēlumi, piezīmes)\n'
            '• ✅ Pārklājumi (teksti, krusti, paraksti, attēli, formas)',
        'flatten_options': 'Opcijas:',
        'flatten_forms': 'Izlīdzināt veidlapu laukus',
        'flatten_annotations': 'Izlīdzināt anotācijas',
        'flatten_overlays': 'Izlīdzināt pārklājumus (tekstus, krustus, parakstus, attēlus, formas)',
        'flatten_target_folder': 'Mērķa mape:',
        'flatten_browse': 'Pārlūkot...',
        'flatten_select_folder': 'Izvēlieties mērķa mapi',
        'flatten_warning': '⚠️ Svarīgi: Izlīdzināšana ir neatgriezenisks process!\n\nPēc izlīdzināšanas rediģējamos elementus vairs nevar atsevišķi mainīt vai dzēst.\nJa nepieciešams, iepriekš izveidojiet rezerves kopiju.',
        'flatten_apply': 'Izlīdzināt',
        'flatten_start': 'Sāk izlīdzināšanu...',
        'flatten_progress': 'Izlīdzina PDF...',
        'flatten_success': 'PDF veiksmīgi izlīdzināts!\n\nSaglabāts kā:\n{0}\n\nVai vēlaties atvērt izlīdzināto PDF?',
        'flatten_complete': 'Izlīdzināšana pabeigta',
        'flatten_cancel': 'Izlīdzināšana atcelta',
        'flatten_error_format': 'Kļūda izlīdzināšanas laikā:\n\n{0}',
        'filename_flatten_suffix': '_izlīdzināts',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF pārklājums (Overlay)',
        'overlay_menu': 'PDF pārklājums (Overlay)',
        'overlay_info': 'Uzliek vienu PDF (pārklājumu) virs cita PDF.\n\nPārklājuma PDF tiek uzlikts uz pamata PDF. Tas ir noderīgi ūdenszīmēm, logotipiem, veidlapu galvenēm vai zīmogiem.',
        'overlay_explanation_title': '📖 Kam tas ir noderīgi?',
        'overlay_explanation_text': 'Pārklājums ir nepieciešams šādās situācijās:\n\n'
            '• 🏢 Uzlikt uzņēmuma logotipu kā ūdenszīmi uz katras lapas\n'
            '• 📄 Uzlikt veidlapas galveni uz tukša PDF\n'
            '• 🖊️ Uzlikt zīmoga pārklājumu uz dokumenta\n'
            '• 🔖 Uzlikt ūdenszīmi uz visām lapām\n'
            '• 📑 Uzlikt veidlapas pārklājumu uz šablona',
        'overlay_type': 'Pārklājuma veids:',
        'overlay_type_fullpage': 'Visa lapa (pārklājošs)',
        'overlay_type_transparent': 'Visa lapa (caurspīdīgs - ieteicams)',
        'overlay_type_stamp': 'Zīmogs (pozicionējams)',
        'overlay_type_info_fullpage': '📄 Pārklājuma PDF tiek uzlikts precīzi virs visas lapas.\nBalto fonu var noņemt, lai būtu redzams tikai saturs.',
        'overlay_type_info_transparent': '🔍 Pārklājuma PDF tiek uzlikts virs visas lapas ar caurspīdīgu fonu.\nBaltais fons tiek automātiski noņemts - ideāli ūdenszīmēm un logotipiem!',
        'overlay_type_info_stamp': '🖊️ Pārklājuma PDF tiek pozicionēts un mērogots kā zīmogs.\nLieliski piemērots logotipiem, zīmogiem vai parakstiem noteiktās pozīcijās.',
        'overlay_remove_background': 'Noņemt balto fonu:',
        'overlay_remove_background_enable': 'Noņemt balto fonu no pārklājuma PDF (padara pārklājumu caurspīdīgu)',
        'overlay_remove_background_tooltip': 'Noņem baltos apgabalus no pārklājuma PDF, lai apakšējais teksts būtu redzams.',
        'overlay_threshold': 'Sliekšņa vērtība:',
        'overlay_threshold_hint': '(1-254, augstāka = vairāk baltā tiek noņemts)',
        'overlay_select_file': 'Izvēlieties pārklājuma PDF:',
        'overlay_file_placeholder': 'Lūdzu, izvēlieties PDF failu pārklājumam',
        'overlay_browse': 'Pārlūkot...',
        'overlay_select_overlay': 'Izvēlieties pārklājuma PDF',
        'overlay_range': 'Lappušu diapazons:',
        'overlay_all_pages': 'Visas lapas',
        'overlay_custom_range': 'Pielāgots diapazons',
        'overlay_from': 'No:',
        'overlay_to': 'Līdz:',
        'overlay_position': 'Pozīcija:',
        'overlay_position_center': 'Centrs',
        'overlay_position_top_left': 'Augšā kreisā',
        'overlay_position_top_right': 'Augšā labā',
        'overlay_position_bottom_left': 'Apakšā kreisā',
        'overlay_position_bottom_right': 'Apakšā labā',
        'overlay_size': 'Izmērs:',
        'overlay_size_original': 'Oriģinālais izmērs',
        'overlay_size_fit_page': 'Pielāgot lapai',
        'overlay_size_custom': 'Pielāgots (%)',
        'overlay_opacity': 'Caurspīdīgums:',
        'overlay_target_folder': 'Mērķa mape:',
        'overlay_browse_folder': 'Pārlūkot...',
        'overlay_select_folder': 'Izvēlieties mērķa mapi',
        'overlay_warning': '⚠️ Piezīme: Pārklājuma PDF tiek uzlikts uz pamata PDF un "iecepināts" tajā.\n\nPārklājuma PDF elementi pēc saglabāšanas vairs nav atsevišķi rediģējami.',
        'overlay_apply': 'Pārklāt',
        'overlay_start': 'Sāk pārklājumu...',
        'overlay_progress': 'Pārklāj PDF...',
        'overlay_success': 'PDF veiksmīgi pārklāts!\n\nSaglabāts kā:\n{0}\n\nVai vēlaties atvērt pārklāto PDF?',
        'overlay_complete': 'Pārklājums pabeigts',
        'overlay_cancel': 'Pārklājums atcelts',
        'overlay_error_format': 'Kļūda pārklājuma laikā:\n\n{0}',
        'overlay_no_file': 'Nav izvēlēts neviens pārklājuma PDF.\n\nLūdzu, izvēlieties PDF failu pārklāšanai.',
        'filename_overlay_suffix': '_pārklāts',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Izvilkt attēlus no PDF',
        'extract_images_menu': 'Izvilkt visus attēlus',
        'extract_images_info': 'Izvelk visus attēlus no PDF un saglabā tos kā atsevišķus failus.\n\nAttēli tiek saglabāti to oriģinālajā formātā vai konvertēti izvēlētajā formātā.',
        'extract_images_format': 'Attēla formāts:',
        'extract_images_quality': 'JPEG kvalitāte:',
        'extract_images_options': 'Opcijas:',
        'extract_images_subfolder': 'Izvilkt uz apakšmapi ("PDFnosaukums_attēli")',
        'extract_images_unique': 'Tikai unikāli attēli (izvairīties no dublikātiem)',
        'extract_images_range': 'Lappušu diapazons:',
        'extract_images_all_pages': 'Visas lapas',
        'extract_images_custom_range': 'Pielāgots diapazons',
        'extract_images_from': 'No:',
        'extract_images_to': 'Līdz:',
        'extract_images_target_folder': 'Mērķa mape:',
        'extract_images_browse': 'Pārlūkot...',
        'extract_images_select_folder': 'Izvēlieties mērķa mapi',
        'extract_images_info_box': 'Informācija',
        'extract_images_info_text': 'Izvilšana var ilgt vairākas minūtes lieliem PDF failiem.\n\nAttēli tiek saglabāti ar to oriģinālo nosaukumu (lapa_attēls).',
        'extract_images_extract': 'Izvilkt',
        'extract_images_start': 'Sāk izvilkšanu...',
        'extract_images_progress': 'Izvelk attēlus...',
        'extract_images_success': '✅ Attēli veiksmīgi izvilkti!\n\n{0} attēli tika saglabāti:\n{1}',
        'extract_images_complete': 'Attēlu izvilkšana pabeigta',
        'extract_images_cancel': 'Izvilkšana atcelta',
        'extract_images_error_format': 'Kļūda, izvelkot attēlus:\n\n{0}',
        'extract_images_open_folder': '📁 Atvērt mapi',
        'extract_images_no_images': 'PDF nav atrasts neviens attēls.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Vairākas lapas vienā lapā (N-Up)',
        'nup_menu': 'Vairākas lapas vienā lapā (N-Up)',
        'nup_info': 'Izkārto vairākas PDF lapas vienā lapā.\n\nIdeāli kompaktai drukāšanai, pārskatiem vai izdales materiāliem.',
        'nup_layout': 'Izkārtojums:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Priekšskatījums:',
        'nup_preview_info': '{0} lapas → {1} lapas uz lapas → {2} lapas\nIzkārtojums: {3}',
        'nup_order': 'Secība:',
        'nup_order_horizontal': 'Horizontāli (rinda pēc rindas)',
        'nup_order_vertical': 'Vertikāli (kolonna pēc kolonnas)',
        'nup_order_horizontal_reverse': 'Horizontāli pretēji',
        'nup_order_vertical_reverse': 'Vertikāli pretēji',
        'nup_range': 'Lappušu diapazons:',
        'nup_all_pages': 'Visas lapas',
        'nup_custom_range': 'Pielāgots diapazons',
        'nup_from': 'No:',
        'nup_to': 'Līdz:',
        'nup_options': 'Opcijas:',
        'nup_margins': 'Maliņas:',
        'nup_margin_between': 'Atstarpe starp lapām:',
        'nup_page_numbers': 'Ievietot lappušu numurus',
        'nup_target_folder': 'Mērķa mape:',
        'nup_browse': 'Pārlūkot...',
        'nup_select_folder': 'Izvēlieties mērķa mapi',
        'nup_create': 'Izveidot',
        'nup_start': 'Sāk N-Up...',
        'nup_progress': 'Izveido N-Up...',
        'nup_success': 'N-Up veiksmīgi izveidots!\n\nSaglabāts kā:\n{0}\n\nVai vēlaties atvērt jauno PDF?',
        'nup_complete': 'N-Up pabeigts',
        'nup_cancel': 'N-Up atcelts',
        'nup_error_format': 'Kļūda N-Up laikā:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Mainīt lapas izmēru',
        'pagesize_menu': 'Mainīt lapas izmēru',
        'pagesize_info': 'Maina PDF lapas izmēru.\n\nSaturs tiek automātiski pielāgots jaunajam izmēram.',
        'pagesize_format': 'Formāts:',
        'pagesize_select': 'Izvēlieties standarta formātu:',
        'pagesize_custom': 'Pielāgots izmērs:',
        'pagesize_width': 'Platums:',
        'pagesize_height': 'Augstums:',
        'pagesize_orientation': 'Orientācija:',
        'pagesize_portrait': 'Portrets',
        'pagesize_landscape': 'Ainava',
        'pagesize_scale_options': 'Mērogošanas opcijas:',
        'pagesize_fit': 'Pielāgot (saglabāt malu attiecību)',
        'pagesize_stretch': 'Izstiept (izkropļot)',
        'pagesize_center': 'Centrēt (oriģinālais izmērs)',
        'pagesize_range': 'Lappušu diapazons:',
        'pagesize_all_pages': 'Visas lapas',
        'pagesize_custom_range': 'Pielāgots diapazons',
        'pagesize_from': 'No:',
        'pagesize_to': 'Līdz:',
        'pagesize_target_folder': 'Mērķa mape:',
        'pagesize_browse': 'Pārlūkot...',
        'pagesize_select_folder': 'Izvēlieties mērķa mapi',
        'pagesize_apply': 'Piemērot',
        'pagesize_start': 'Sāk lapas izmēra maiņu...',
        'pagesize_progress': 'Maina lapas izmēru...',
        'pagesize_success': 'Lapas izmērs veiksmīgi mainīts!\n\nSaglabāts kā:\n{0}\n\nVai vēlaties atvērt jauno PDF?',
        'pagesize_complete': 'Lapas izmēra maiņa pabeigta',
        'pagesize_cancel': 'Lapas izmēra maiņa atcelta',
        'pagesize_error_format': 'Kļūda, mainot lapas izmēru:\n\n{0}',
        'pagesize_preview_info': 'Jauns izmērs: {0} x {1} pt',
        'filename_pagesize_suffix': '_jauns_izmērs',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF informācija',
        'pdf_info_menu': 'Rādīt PDF informāciju',
        'pdf_info_voice': 'Tiek rādīta PDF informācija',
        'pdf_info_error': 'Kļūda, rādot PDF informāciju:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Rādīt tastatūras īsceļus",
        "shortcuts_dialog_title": "Tastatūras īsceļi",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FAILS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Atvērt PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Aizvērt PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Saglabāt kā...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Aizsargāt dokumentu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Drukāt</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Drukāt uzreiz (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Iziet no lietotnes</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORTS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Eksportēt kā Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Eksportēt kā DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Eksportēt kā TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Eksportēt kā attēlus (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Izvilkt attēlus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTU APSTRĀDE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Vairākas lapas)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A konvertēšana (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Izlīdzināt PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Pārklāt PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimizēt PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ REDIĢĒŠANA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Meklēt</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Pievienot grāmatzīmi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Pārvaldīt grāmatzīmes</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Nākamā grāmatzīme</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Iepriekšējā grāmatzīme</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Palaist OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 LAPU PĀRVALDĪBA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Pagriezt pašreizējo lapu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Pagriezt visas lapas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalizēt pašreizējo lapu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalizēt visas lapas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Dzēst lapas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Izvilkt lapas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Ievietot lapas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Pārvietot lapas</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Apvienot PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Mainīt lapas izmēru</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 IEVIETOŠANA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Ievietot tekstu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Ievietot krustu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Ievietot parakstu 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Ievietot parakstu 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Ievietot attēlu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Ievietot taisnstūri</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ievietot elipsi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Ievietot līniju</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Ievietot bultiņu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Ievietot lappušu numurus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Teksta ūdenszīme</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Attēla ūdenszīme</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ IZSVĪTROJUMI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Izsvītrojums (melns)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Izsvītrojums (balts)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Piemērot visus izsvītrojumus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ PAPILDU FUNKCIJAS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Apgriezt PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Rediģēt metadatus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ SKATS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Pārslēgt Tumšo/Gaišo režīmu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Rādīt teksta logu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Lapas platums (Tuvināšana)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Divas lapas (Tuvināšana)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Pārskats (Tuvināšana)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ IESTATĪJUMI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Paroļu pārvaldība</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR iestatījumi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Paraksta iestatījumi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Faila nosaukuma formatējums</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Eksportēt iestatījumus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importēt iestatījumus</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMĀCIJA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Rādīt PDF informāciju</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Ieslēgt/izslēgt balss izvadi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Fokusēt izvēlņu joslu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Ir pieejama jauna versija",
        "update_available_message": "Ir pieejama jauna versija <b>{0}</b>.\n\nApmeklējiet izlaiduma lapu, lai lejupielādētu atjauninājumu:\n{1}",
        "update_available_voice": "Jauna versija {0} ir pieejama. Lūdzu, lejupielādējiet atjauninājumu no GitHub lapas.",
        "update_open_release": "Atvērt izlaiduma lapu",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Lejupielādēt visus tulkojumus",
        "ask_download_all_translations": """Papildus vācu, angļu un vjetnamiešu valodai ir pieejamas vēl {total_languages} GUI valodas.\n\nVai tās jānodrošina / jāatjaunina?\n\nPiezīme:\nNevajadzīgās valodas vēlāk varat manuāli dzēst direktorijā:\n{translations_path}
        \nJa atceļat, GUI valodas vēlāk varat lejupielādēt, izmantojot izvēlni 'Rīki → Atjaunināt tulkojumus'.""",
        "menu_update_translations": "Atjaunināt tulkojumus",
        "translations_updated": "Tulkojumi atjaunināti",
        "translations_update_success": "{} tulkojumi tika veiksmīgi atjaunināti ({} jauni, {} atjaunināti).",
        "translations_update_error": "Kļūda, atjauninot tulkojumus",
        "translations_update_no_changes": "Visi tulkojumi jau ir aktuāli.",
        "translations_update_offline": "Nav interneta savienojuma. Tulkojumus nevarēja atjaunināt.",
        "translations_update_in_progress": "Tulkojumi tiek atjaunināti fonā...",
        "translations_downloading": "Lejupielādē tulkojumus...",
        "translations_path_hint": "Lietotāja direktorija tulkojumiem",
        "translations_update_not_available_title": "Atjauninājums nav pieejams",
        "translations_update_not_available_message": """Tulkojumu atjaunināšana ir pieejama tikai instalētajā versijā.\n\nIzstrādes režīmā tulkojumi jau ir aktuāli.""",
        "translations_update_no_internet_title": "Nav interneta savienojuma",
        "translations_update_no_internet_message": """Nevar izveidot interneta savienojumu.\n\nTulkojumus nevar lejupielādēt no GitHub.\n\nIespējamie risinājumi:
        • Pārbaudiet savu interneta savienojumu
        • Uz laiku atspējojiet iespējamo ugunsmūri
        • Mēģiniet vēlreiz vēlāk
        \nVarat arī manuāli lejupielādēt tulkojumus no GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Atjaunināšana jau notiek",
        "btn_retry": "Mēģināt vēlreiz",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Laipni lūdzam PDF Dark View",
        "welcome_title_not_supported": "Laipni lūdzam PDF Dark View",
        "welcome_message": "Laipni lūdzam PDF Dark View!\n\nJūsu sistēmas valoda tika atpazīta kā '{language}'.\nVai vēlaties izmantot šo valodu lietotāja saskarnei?\n\nValodu varat mainīt jebkurā laikā, izmantojot 'Iestatījumi → Valoda'.",
        "welcome_message_language_not_available": "Laipni lūdzam PDF Dark View!\n\nJūsu sistēmas valoda tika atpazīta kā '{language}'.\nŠī valoda vēl nav instalēta.\n\nVai vēlaties tagad lejupielādēt tulkojumus valodai {language} no GitHub?\n\n(Valoda pēc tam tiks automātiski izmantota lietotāja saskarnei.)",
        "welcome_message_language_not_supported": "Laipni lūdzam PDF Dark View!\n\nJūsu sistēmas valoda tika atpazīta kā '{language}'.\nDiemžēl šai valodai vēl nav tulkojumu.\n\nLietotāja saskarne tiks rādīta valodā {fallback_language}.\n\nValodu varat mainīt jebkurā laikā, izmantojot 'Iestatījumi → Valoda'.\nJa vēlaties, varat pats piedalīties tulkojuma izveidē savā valodā:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Jā, izmantot sistēmas valodu",
        "welcome_keep_english": "Nē, paturēt angļu valodu",
        "welcome_download_language": "Jā, lejupielādēt {language}",

        # ============================================
        # 107. PĒDĒJIE IZMANTOTIE CEĻI
        # ============================================

        'menu_recent': 'Pēdējie izmantotie',
        'menu_recent_dirs': 'Direktoriji...',
        'menu_recent_files': 'Faili...',
        'recent_manage': 'Pārvaldīt...',
        'recent_enable_tracking': 'Saglabāt pēdējos ceļus (privātums)',
        'recent_enable_info': 'Atspējojiet šo opciju, lai nesaglabātu ceļus',
        'recent_tracking_disabled': 'Ceļu izsekošana ir atspējota',
        'recent_enabled': 'iespējots',
        'recent_disabled': 'atspējots',
        'recent_tracking_status': 'Ceļu izsekošana {0}',
        'recent_dialog_title': 'Pēdējie izmantotie ceļi',
        'recent_tab_directories': 'Direktoriji',
        'recent_tab_files': 'Faili',
        'recent_dirs_instruction': 'Veiciet dubultklikšķi, lai atvērtu failu dialoga logu direktorijā',
        'recent_files_instruction': 'Veiciet dubultklikšķi, lai tieši atvērtu PDF',
        'recent_no_directories': '(nav saglabātu direktoriju)',
        'recent_no_files': '(nav saglabātu failu)',
        'recent_default_current': '⭐ Noklusējums: {0}',
        'recent_set_as_default': '⭐ Iestatīt kā noklusējumu',
        'recent_default_set_title': 'Noklusējuma direktorijs iestatīts',
        'recent_default_set_message': 'Direktorijs "{0}" ir iestatīts kā noklusējums PDF failu atvēršanai.',
        'recent_default_set_voice': 'Noklusējuma direktorijs ir iestatīts',
        'recent_directory_not_found': 'Direktorijs nav atrasts',
        'recent_file_not_found': 'Fails nav atrasts',
        'recent_remove_selected': 'Noņemt',
        'recent_remove_title': 'Noņemt ceļu',
        'recent_remove_confirm': 'Vai tiešām vēlaties noņemt ceļu "{0}" no saraksta?',
        'recent_path_removed': 'Ceļš ir noņemts',
        'recent_clear_all': 'Noņemt visus',
        'recent_clear_title': 'Noņemt visus ceļus',
        'recent_clear_confirm_type': 'Vai tiešām vēlaties dzēst visus {0}?',
        'recent_cleared': 'Saraksts ir notīrīts',
        'recent_path_not_found_title': 'Ceļš nav atrasts',
        'recent_path_not_found_message': 'Ceļš "{0}" vairs nepastāv.',
        'recent_open_file': 'Atvērt failu',
        'btn_open_recent': 'Atvērt',
        'recent_open_file_question': 'Vai vēlaties atvērt "{0}" kā PDF?',
        'recent_not_pdf': 'Atlasītais fails nav PDF.',
        'recent_more_entries': 'Vairāk ierakstu...',
        'btn_remove': 'Noņemt',
        'btn_clear': 'Notīrīt visus',
        'recent_context_open': 'Atvērt',
        'recent_context_reveal': 'Parādīt Finder',
        'recent_context_set_default': '⭐ Iestatīt kā noklusējumu',
        'recent_context_open_terminal': '💻 Atvērt termināli',
        'recent_context_file_info': 'Faila informācija',
        'recent_context_open_with_default': '📄 Atvērt ar noklusējuma lietotni',
        'recent_context_remove': 'Noņemt no saraksta',
        'recent_context_clear_all': 'Noņemt visus',
        'recent_file_info_title': 'Faila informācija',
        'recent_file_info_name': 'Nosaukums',
        'recent_file_info_path': 'Ceļš',
        'recent_file_info_size': 'Izmērs',
        'recent_file_info_modified': 'Mainīts',
        'recent_file_info_pages': 'Lapas',
        'recent_error_reveal': 'Kļūda, atverot Finder',
        'recent_error_terminal': 'Kļūda, atverot termināli',
        'recent_error_info': 'Kļūda, iegūstot faila informāciju',
        'open_user_data_folder': 'Parādīt lietotāja datu direktoriju',

        # ============================================
        # 108. PĀRA/NEPĀRA LAPU DZĒŠANA
        # ============================================
        "pages_delete_even": "Dzēst visas pāra lapas",
        "pages_delete_odd":  "Dzēst visas nepāra lapas",
        "progress_even_pages": "Notiek pāra lapu dzēšana",
        "progress_odd_pages": "Notiek nepāra lapu dzēšana",
        "progress_mark_delete_even": "{} pāra lapa(s) atzīmēta(s) dzēšanai",
        "progress_mark_delete_odd":  "{} nepāra lapa(s) atzīmēta(s) dzēšanai",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programma tiek slēgta",

    }
