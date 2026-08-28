
# ============================================
# translations_zu.py - Zulu Wörterbuch (isiZulu)
# Vollständig sortiert nach Kategorien
# ============================================

def load_zulu_strings():
    """Lädt alle Zulu-Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View ngu BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Layisha i-PDF",
        'btn_text_window': "Umbhalo we-OCR",
        'btn_first': "Ikhasi lokuqala",
        'btn_prev': "Ikhasi eledlule",
        'btn_next': "Ikhasi elilandelayo",
        'btn_last': "Ikhasi lokugcina",
        'btn_print': "Phrinta",
        'btn_darkmode_light': "Imodi ekhanyayo",
        'btn_darkmode_dark': "Imodi emnyama",
        'btn_delete_pages': "Susa amakhasi",
        'btn_extract_pages': "Khipha amakhasi",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "Kulungile",
        'btn_cancel': "Khansela",
        'btn_save': "Londoloza",
        'btn_close': "Vala",
        'btn_delete': "Susa",
        'btn_delete_all': "Susa konke",
        'btn_copy': "Kopisha",
        'btn_export': "Thumela ngaphandle",
        'btn_show': "Khombisa iphasiwedi",
        'btn_hide': "Fihla iphasiwedi",
        'btn_authenticate': "Qinisekisa",
        'btn_settings': "Izilungiselelo",
        'btn_protect': "Vikela",
        'btn_remove_password': "Susa iphasiwedi",
        'btn_manage': "Phatha amaphasiwedi",
        'btn_retry': "Zama futhi",
        'btn_select_all': "Khetha konke",
        'btn_clear_selection': "Susa ukukhetha",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Ikhasi {0} kweyi {1}",
        'page_count': "kweyi {0}",
        'goto_page': "Iya ekhasi",
        'page_simple': "Ikhasi {0}",
        'full_view_page': "Ukubuka konke ikhasi {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Faka igama ozofuna nalo + Enter",
        'search_results': "Imiphumela: {0} kweyi {1}",
        'search_nav_hint': "Enter: elilandelayo (Shift+Enter: eledlule)",
        'search_no_results': "Ayikho imiphumela",
        'search_error': "Iphutha ekusesheni",
        'search_active': "Ibha yokusesha isebenza",
        'search_closed': "Ukusesha kuphelile",
        'search_position': "Ikhasi {0} {1}",
        'search_pos_top': "phezulu",
        'search_pos_upper': "ingxenye engenhla",
        'search_pos_middle': "maphakathi",
        'search_pos_lower': "ingxenye engezansi",
        'search_pos_bottom': "phansi",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Ukuqashelwa kombhalo kuphumelele!",
        'ocr_success_title': "I-OCR iphumelele",
        'ocr_success_message': "Umbhalo manje usesheka kalula.",
        'ocr_failed': "I-OCR yehlulekile",
        'ocr_in_progress': "I-OCR iyaqhubeka",
        'ocr_preparing': "Ilungisa i-PDF...",
        'ocr_analyzing': "Ihlaziya i-PDF...",
        'ocr_optimizing': "Ithuthukisa isithombe...",
        'ocr_recognizing': "Iyabona umbhalo...",
        'ocr_embedding': "Ifaka umbhalo...",
        'ocr_finalizing': "Iqeda i-PDF...",
        'ocr_not_available': "I-OCR ayitholakali",
        'ocr_install_message': "Amathuluzi e-OCR awatholakali.\n\nSicela ufake:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "I-OCR iyadingeka",
        'ocr_question': "Le PDF ayinawo umbhalo osephethe ukusesha.\nUyafuna ukwenza i-OCR ukuze unikwe amandla {0}?",
        'ocr_perform': "Yenza i-OCR",
        'ocr_later': "Kamuva",
        'ocr_starting': "Iqala i-OCR eqinisekisiwe...",
        'ocr_success_voice': "I-OCR iphumelele. I-PDF manje iyasesheka.",
        'ocr_partial_success': "I-OCR yenziwe, kodwa kube nenkinga ekushintsheni.\n\nInguqulo eseshekayo igcinwe lapha:\n{0}\n\nIphutha: {1}",
        'ocr_partial_title': "I-OCR iphumelele kancane",
        'ocr_partial_voice': "I-OCR yenziwe, kodwa ukushintsha kwehlulekile.",
        'original_file': "Ifayela lokuqala:",
        'old_size': "Usayizi wakudala:    {0} bytes",
        'new_size': "Usayizi omusha: {0} bytes",
        'size_change': "Ushintsho: {0}{1} bytes",
        'backup_created_file': "Isipele sakhiwe:\n{0}",
        'backup_not_created': "Isipele: asikakhiwa (izilungiselelo zivaliwe)",
        'page_header': "=== Ikhasi {0} ===\n{1}\n",
        'scanned_page_header': "=== Ikhasi {0} (eliskeniwe) ===\n[Leli khasi linombhalo oskeniwe kuphela]\n[Sicela wenze i-OCR ngesandla]\n",
        'scanned_warning': "⚠️ UMBHALO OSKENIWE - I-OCR IYADINGEKA",
        'guaranteed_title': "I-PDF eseshekayo idaliwe",
        'guaranteed_message': "<b>Inguqulo eqinisekisiwe eseshekayo idaliwe!</b>\n\nNjengoba i-OCR ezenzakalelayo yehlulekile, enye i-PDF eseshekayo idaliwe:\n\n{0}\n\n<b>Leli fayela liqukethe:</b>\n• Umbhalo okhishiwe (uma ukhona)\n• Imibono kumakhasi askeniwe\n• Iyasesheka ngokugcwele",
        'guaranteed_voice': "I-PDF eqinisekisiwe eseshekayo idaliwe.",
        'instruction_title': "Umhlahlandlela we-OCR",
        'instruction_file': "Ifayela lokuqala: {0}",
        'instruction_text': "Ukuqashelwa kombhalo okuzenzakalelayo (OCR) kwehlulekile.\nSicela wenze i-OCR ngesandla:\n\n1. NGOKUSEBENZISA I-OCRmyPDF (umugqa womyalo):\n   ocrmypdf --force-ocr \"[IFAYELA]\" \"okukhiphayo.pdf\"\n\n2. NGOKUSEBENZISA I-ADOBE ACROBAT (macOS/Windows):\n   • Vula i-PDF ku-Acrobat\n   • Amathuluzi > Hlela i-PDF\n   • Khetha 'Qashela umbhalo'\n\n3. NGOKUSEBENZISA I-PREVIEW (macOS):\n   • Vula i-PDF ku-Preview\n   • Ifayela > Thumela ngaphandle...\n   • Isihluzi se-Quartz: 'Yehlisa usayizi wefayela'\n   • Vula 'Yenza i-OCR'\n\n4. IZINSIZA EKUHLAWULENI I-OCR:\n   • smallpdf.com/zu/ocr-pdf\n   • ilovepdf.com/zu/ocr-pdf\n   • adobe.com/za/acrobat/online/pdf-to-word.html",
        'instruction_created': "Umhlahlandlela we-OCR udaliwe",
        'instruction_created_message': "Umhlahlandlela onemininingwane udaliwe:\n\n{0}\n\nSicela ulandele izinyathelo zokwenza i-OCR ngesandla.",
        'instruction_created_voice': "Umhlahlandlela we-OCR udaliwe.",
        'ocr_impossible': "I-OCR ayinakwenzeka",
        'ocr_impossible_message': "I-OCR ayikwazanga ukwenziwa.\n\nSicela ucubungule '{0}' ngesandla usebenzisa isofthiwe ye-OCR.",
        'ocr_impossible_voice': "I-OCR ayinakwenzeka. Sicela ucubungule ngesandla.",
        'emergency_title': "I-OCR ephuthumayo",
        'emergency_message': "I-PDF ephuthumayo idaliwe:\n\n{0}\n\nSicela ucubungule leli fayela ngesandla usebenzisa i-OCR.",
        'emergency_voice': "I-PDF ephuthumayo idaliwe. Sicela wenze i-OCR ngesandla.",
        'critical_error': "Iphutha elibi",
        'critical_error_message': "I-OCR ayikwazanga ukuqalwa.\n\nSicela uqale kabusha uhlelo futhi uhlole ukufakwa kwe-OCR.",
        'critical_error_voice': "Iphutha elibi le-OCR",
        'ocr_question_html': "<p>Le PDF ayinawo umbhalo osephethe ukusesha.<p>Uyafuna ukwenza i-OCR ukuze unikwe amandla <b>{0}</b>?</p>",
        'ocr_question_voice': "I-OCR iyadingeka. I-PDF ayinawo umbhalo osephethe ukusesha. Uyafuna ukwenza i-OCR ukuze unikwe amandla {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "Ayikho i-PDF elayishiwe",
        'no_pdf_message': "Ayikho i-PDF elayishiwe",
        'pdf_not_found': "Ifayela le-PDF alitholakali",
        'file_size': "Usayizi wefayela",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Isipele sakhiwe",
        'backup_disabled': "Isipele sivaliwe",
        'backup_activated': "Ukudala isipele kuvuliwe",
        'backup_deactivated': "Ukudala isipele kuvaliwe",
        'backup_status': "Isipele: {0}",
        'backup_on': "✔ kuvuliwe",
        'backup_off': "✘ kuvaliwe",
        'close_pdf': "Ukuvala i-PDF: {0}",
        'pdf_not_found_format': "Ifayela le-PDF alitholakali: {0}",
        'error_pdf_load_format': "Iphutha ekulayisheni i-PDF: {0}",
        'load_failed_format': "Ukulayisha kwehlulekile:\n{0}",
        'decrypted_suffix': "(ikuphiwe)",
        'decryption_failed': "Ukuphumula kwehlulekile.",
        'decryption_error': "Iphutha ekuphumuleni",
        'decryption_success': "Kuphunyuliwe ngempumelelo",
        'decryption_success_message': "I-PDF ikhishiwe futhi igcinwe lapha:\n\n{0}",
        'decryption_success_voice': "I-PDF ikhishiwe futhi igcinwe.",
        'password_remove_error': "Iphutha ekususeni iphasiwedi",
        'save_unencrypted': "Londoloza i-PDF engagondliwe njenge",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Londoloza njenge...",
        'save_copy': "Londoloza ikhophi",
        'save_success': "I-PDF igcinwe lapha: {0}",
        'save_encrypted': "I-PDF evikelekile igcinwe lapha: {0}",
        'save_error': "I-PDF ayikwazanga ukugcinwa",
        'encryption_question': "Uyafuna ukuvikela i-PDF ngephasiwedi?",
        'encryption_yes': "Yebo",
        'encryption_no': "Cha",
        'encryption_cancel': "Khansela",
        'save_cancel': "Ukulondoloza kukhanseliwe",
        'save_encrypted_voice': "Ifayela lifihliwe futhi lagcinwa.",
        'save_success_voice': "Ifayela le-PDF ligcinwe lingafihliwe.",
        'save_error_format': "I-PDF ayikwazanga ukugcinwa:\n{0}",
        'export_pages_success': "Ukuthumela ngaphandle ku-Pages kuphumelele",
        'export_pages_error': "Ukuthumela ngaphandle ku-Pages kwehlulekile",
        'export_pages_error_format': "Ukuthumela ngaphandle ku-Pages kwehlulekile: {0}",
        'export_word_success': "Ukuthumela ngaphandle ku-Word kuphumelele",
        'export_word_error': "Ukuthumela ngaphandle ku-Word kwehlulekile",
        'export_word_error_format': "Ukuthumela ngaphandle ku-Word kwehlulekile: {0}",
        'export_text_success': "Ukuthumela umbhalo ngaphandle kuphumelele",
        'export_text_error': "Ukuthumela umbhalo ngaphandle kwehlulekile",
        'export_text_error_format': "Ukuthumela umbhalo ngaphandle kwehlulekile: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Iphasiwedi iyadingeka",
        'password_enter': "Sicela ufake iphasiwedi",
        'password_confirm': "Qinisekisa iphasiwedi",
        'password_new': "Iphasiwedi entsha",
        'password_current': "Iphasiwedi yamanje",
        'password_save': "Londoloza iphasiwedi (efihliwe)",
        'password_saved': "✓ Iphasiwedi yaleli fayela igcinwe",
        'password_wrong': "Iphasiwedi ayilungile",
        'password_mismatch': "Amaphasiwedi awafani",
        'password_too_short': "Iphasiwedi imfushane kakhulu",
        'password_min_length': "Iphasiwedi kumele ibe okungenani izinhlamvu ezi-4",
        'password_strength': "Amandla ephasiwedi",
        'password_strength_very_weak': "Abuthaka kakhulu",
        'password_strength_weak': "Abuthaka",
        'password_strength_medium': "Maphakathi",
        'password_strength_strong': "Aqinile",
        'password_strength_very_strong': "Aqine kakhulu",
        'password_char_count': "(izinhlamvu ezi-{0})",
        'password_match': "✓ Ziyafana",
        'password_no_match': "✗ Amaphasiwedi awafani",
        'password_show': "Khombisa",
        'password_hide': "Fihla",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Ukuphathwa kwamaphasiwedi",
        'password_table_filename': "Igama lefayela",
        'password_table_password': "Iphasiwedi",
        'password_count': "Amaphasiwedi agcinwe {0}",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Awekho amaphasiwedi agcinwe",
        'password_copied': "Amaphasiwedi {0} akopishiwe",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Uqinisekile ukuthi ufuna ukususa iphasiwedi ye-' {0}'?",
        'password_delete_multiple': "Uqinisekile ukuthi ufuna ukususa amaphasiwedi {0} akhethiwe?",
        'password_delete_all_confirm': "Uqinisekile ukuthi ufuna ukususa wonke amaphasiwedi agcinwe angu- {0}?",
        'password_deleted': "Amaphasiwedi {0} asusiwe",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Wonke amaphasiwedi asusiwe",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Umkhiqizi wephasiwedi",
        'generator_generated': "Iphasiwedi ekhiqiziwe:",
        'generator_regenerate': "Khiqiza kabusha",
        'generator_copy': "Kopisha",
        'generator_use': "Sebenzisa",
        'generator_settings': "Izilungiselelo",
        'generator_length': "Ubude:",
        'generator_group_every': "Isihlukanisi njalo",
        'generator_group_chars': "izinhlamvu. Isihlukanisi:",
        'generator_uppercase': "Izinhlamvu ezinkulu (A-Z)",
        'generator_lowercase': "Izinhlamvu ezincane (a-z)",
        'generator_digits': "Izinombolo (0-9)",
        'generator_symbols': "Izimpawu ezikhethekile (!@#$%^&*)",
        'generator_exclude': "Okungafakwa:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Iphasiwedi eyinhloko iyadingeka",
        'master_password_setup': "Setha iphasiwedi eyinhloko",
        'master_password_change': "Shintsha iphasiwedi eyinhloko",
        'master_password_enter': "Sicela ufake iphasiwedi yakho eyinhloko",
        'master_password_choose': "Khetha iphasiwedi eyinhloko eqinile (okungenani izinhlamvu eziyi-8)",
        'master_password_new': "Sicela ufake iphasiwedi yakho entsha eyinhloko",
        'master_password_confirm': "Qinisekisa iphasiwedi",
        'master_password_authenticate': "Qinisekisa",
        'master_password_success': "Iphasiwedi eyinhloko isethwe ngempumelelo.",
        'master_password_changed': "Iphasiwedi eyinhloko ishintshiwe ngempumelelo.",
        'master_password_removed': "Iphasiwedi eyinhloko nawo wonke amaphasiwedi asusiwe.",
        'master_password_remove': "Susa iphasiwedi eyinhloko",
        'master_password_remove_confirm': "UQINISEKILE YINI UKUTHI UFAZA UKUSUSA WONKE AMAPHASIWEDI?\n\nLesi senzo ASIKWAZI UKUHLEHLISWA!",
        'master_password_export_before': "Ufuna ukuthumela ngaphandle isipele kuqala?",
        'master_password_export_delete': "Thumela ngaphandle bese ususa",
        'master_password_delete_now': "Susa manje",
        'master_password_for_signatures': "Ukuze usebenzise amasiginesha, kumele usethe iphasiwedi eyinhloko.\n\nUyafuna ukusetha iphasiwedi eyinhloko manje?",
        'master_password_for_private': "Ukuze usebenzise izingxenye zombhalo eziyimfihlo, kumele usethe iphasiwedi eyinhloko.\n\nUyafuna ukusetha iphasiwedi eyinhloko manje?",
        'master_password_info': """
            <b>🔐 NGAPHANDLE KWEPHASIWEDI EYINHLOKO:</b><br>
            • Ukubonisa, ukukopisha nokuthumela ngaphandle amaphasiwedi akunakwenzeka<br>
            • Ukususa amaphasiweki kungenzeka njalo (noma ngaphandle kwephasiwedi eyinhloko)<br><br>

            <b>🔐 NGEPHASIWEDI EYINHLOKO:</b><br>
            • Yonke imisebenzi iyatholakala ngemva kokuqinisekisa<br>
            • Amaphasiwedi afihlwa ngephasiwedi eyinhloko<br>
            • Ubuncane ubude: 8 izinhlamvu<br>
            • Ukugcinwa okuphephile kwe-SHA-256 hash<br><br>

            <b>KUBALULEKILE:</b><br>
            • Uma ulahlekelwa iphasiwedi eyinhloko: amaphasiwedi awakwazi ukutholwa kabusha<br>
            • Lapho ususa iphasiwedi eyinhloko: WONKE amaphasiwedi ayasuswa<br>
            • Inketho yokuthumela ngaphandle ikhona ngaphambi kokususa<br>
            • Iphasiwedi eyinhloko ingashintshwa noma nini
        """,
        'signature_auth_disabled': "Vala ukucela iphasiweki kumasiginesha",
        'template_auth_disabled': "Vala ukucela iphasiwedi ezingxenyeni zombhalo eziyimfihlo",
        'master_password_for_signatures_settings': "Ukuze usebenzise amasiginesha, kumele usethe iphasiwedi eyinhloko.\n\nIya Ezilungiselelweni - Ukuphathwa kwamaphasiwedi",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Vikela i-PDF",
        'protect_info': "Ifayela '{0}' lizovikelwa ngephasiwedi.",
        'protect_instruction': "Sicela ufake iphasiwedi oyifunayo kabili ukuze uvikele umbhalo, noma usebenzise umkhiqizi wephasiwedi ongakwesokudla kwebhokisi lokufaka.",
        'protect_success': "I-PDF ivikeleke ngempumelelo futhi igcinwe lapha:\n{0}\n\nIphasiwedi: {1}\n\nUyafuna ukuvula i-PDF evikelekile manje?",
        'protect_open': "Yebo",
        'protect_skip': "Cha",
        'protect_error': "Iphutha ekuvikeleni i-PDF",
        'protect_open_title': "Vula i-PDF evikelekile",
        'protect_question': "Kwenziwe. Uyafuna ukuvula i-PDF evikelekile manje? Yebo noma Cha?",
        'password_cancel': "Ingxoxo yephasiwedi ikhanseliwe",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Susa amakhasi",
        'pages_extract': "Khipha amakhasi",
        'pages_insert': "Faka amakhasi",
        'pages_move': "Hambisa amakhasi",
        'pages_delete_options': "Izinketho zokususa",
        'pages_delete_empty': "Susa wonke amakhasi angenalutho",
        'pages_delete_current': "Susa ikhasi lamanje",
        'pages_delete_range': "Susa uhla lwamakhasi",
        'pages_extract_options': "Izinketho zokukhipha",
        'pages_extract_current': "Khipha ikhasi lamanje",
        'pages_extract_range': "Khipha uhla lwamakhasi",
        'pages_insert_position': "Indawo yokufaka",
        'pages_insert_before': "Faka ngaphambi kwekhasi:",
        'pages_insert_select': "Khetha i-PDF",
        'pages_insert_none': "Ayikho i-PDF ekhethiwe",
        'pages_move_source': "Amakhasi okuhambisa",
        'pages_move_from': "Kusukela ekhasi:",
        'pages_move_to': "Kuya ekhasi:",
        'pages_move_target': "Indawo okuyiwa kuyo",
        'pages_move_before': "Hambisa ngaphambi kwekhasi:",
        'pages_move_hint': "Qaphela: ikhasi 1 = ekuqaleni, {0} = ekugcineni",
        'pages_range_invalid': "Ikhasi lokuqala kumele libe lincane noma lilingane nekhasi lokugcina.",
        'pages_position_invalid': "Indawo okuyiwa kuyo akumele ibe ngaphakathi kohla oluhambiswayo.",
        'pages_no_pdf_selected': "Ayikho i-PDF ekhethiwe.",
        'pages_deleted': "Amakhasi angu-{0} asusiwe.",
        'pages_extracted': "Kukhishiwe: {0}\nKugcinwe lapha: {1}\nUsayizi wefayela: {2:.1f} KB",
        'pages_inserted': "Kufakwe amakhasi angu-{0}",
        'pages_moved': "Kuhambisiwe amakhasi angu-{0}.",
        'pages_deleted_none': "Akukho khasi elisusiwe.",
        'pages_delete_progress': "Kususwa amakhasi...",
        'pages_deleted_with_backup': "Amakhasi angu-{0} asusiwe.\n\nIsipele: {1}",
        'pages_deleted_voice': "Isipele sakhiwe futhi amakhasi angu-{0} asusiwe.",
        'info': "Qaphela",
        'error_dialog_creation': "Ingxoxo ayikwazanga ukwakhiwa",
        'extract_page_single': "Khipha ikhasi {0}",
        'extract_page_range': "Khipha amakhasi {0}-{1}",
        'extract_success_voice': "Amakhasi akhishwe ngempumelelo",
        'extract_error_format': "Iphutha ekukhipheni: {0}",
        'pages_inserted_voice': "Kufakwe amakhasi angu-{0}.",
        'insert_error_format': "Iphutha ekufakeni: {0}",
        'pages_move_progress': "Kuhambiswa amakhasi...",
        'pages_moved_with_backup': "Kuhambisiwe amakhasi angu-{0}.\n\nIsipele: {1}",
        'move_success_title': "Kuhambisiwe ngempumelelo",
        'pages_moved_voice': "Amakhasi angu-{0} ahambisiwe ngempumelelo",
        'mark_removed': "Umaka wekhasi {0} ususiwe",
        'mark_empty': "Ikhasi {0} limakwe njengeligenalutho",
        'mark_export_removed': "Umaka wokuthumela ngaphandle wekhasi {0} ususiwe",
        'mark_export': "Ikhasi {0} limakwe ukuze lithunyelwe ngaphandle",
        'no_empty_pages': "Awekho amakhasi angenalutho amakelwe ukususwa",
        'delete_empty_confirm': "Ufuna ukususa wonke amakhasi angenalutho amakelwe angu-{0}?",
        'delete_empty_confirm_voice': "Susa wonke amakhasi angenalutho amakelwe angu-{0} manje? Yebo noma Cha.",
        'empty_pages_deleted': "Amakhasi angenalutho angu-{0} asusiwe",
        'no_export_pages': "Awekho amakhasi amakelwe ukuthunyelwa ngaphandle",
        'overwrite_title': "Bhala phezu kwefayela elikhona",
        'overwrite_question': "Ifayela\n\n{0}\n\nselivele likhona.\nUyafuna ukulibhala phezu?",
        'overwrite_voice': "Ngibhale phezu kwefayela elikhona? Yebo noma Cha.",
        'page_skipped': "Ikhasi {0} leqiwe",
        'export_complete': "Ukuthumela ngaphandle kuqediwe.",
        'export_complete_voice': "Ukuthumela ngaphandle kuqediwe.",
        'no_pages_exported': "Akukho khasi elithunyelwe ngaphandle",
        'export_cancelled': "Ukuthumela ngaphandle kukhanseliwe",
        'pages_exported': "Amakhasi angu-{0} athunyelwe ngaphandle kwa-{1}",
        'export_page_title': "Thumela ikhasi ngaphandle",
        'page_exported': "Ikhasi {0} lithunyelwe ngaphandle kwa-{1}",
        'export_error': "Iphutha ekuthumeleni ngaphandle",
        'export_marked_title': "Thumela ngaphandle amakhasi amakelwe",
        'rotate_all_title': "Zungezisa wonke amakhasi",
        'rotate_all_question': "Uyafuna ukuzungezisa wonke amakhasi ngama-90 degrees uye kwesokudla?",
        'rotate_all_voice': "Uyafuna ukuzungezisa wonke amakhasi ngama-90 degrees uye kwesokudla? Yebo noma Cha?",
        'all_pages_rotated': "Wonke amakhasi azungezisiwe",
        'page_rotated': "Ikhasi {0} lizungezisiwe",
        'rotate_error': "Ikhasi alikwazanga ukuzungeziswa",
        'delete_page_confirm': "Ufuna ukususa ikhasi {0}?",
        'delete_page_confirm_voice': "Uqinisekile ukuthi ufuna ukususa ikhasi {0}? Yebo noma Cha.",
        'page_deleted': "Ikhasi {0} lisusiwe",
        'delete_error': "Ikhasi alikwazanga ukususwa",
        'pages_deleted_voice': "Amakhasi angu-{0} asusiwe",
        'pages_exported_split': "Amakhasi angu-{0} athunyelwe ngaphandle ngempumelelo.",
        'pages_skipped': "Amakhasi angu-{0} aleqiwe.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Khipha amakhasi (okuthuthukile)",
        'pdf_splitter_title': "Isihlukanisi neSikhiphi se-PDF",
        'pdf_splitter_load': " Khetha ifayela le-PDF",
        'pdf_splitter_info': "Sicela ukhethe inketho yombhalo wakho we-PDF",
        'pdf_splitter_basic': "Imisebenzi eyisisekelo",
        'pdf_splitter_single': "Hlukanisa amakhasi ngamanye",
        'pdf_splitter_range': "Khipha amakhasi:",
        'pdf_splitter_range_placeholder': "isb. 1-3,5,7-9",
        'pdf_splitter_clean': "Imisebenzi yokuhlanza",
        'pdf_splitter_remove_empty': "Susa wonke amakhasi angenalutho",
        'pdf_splitter_remove': "Susa uhla lwamakhasi:",
        'pdf_splitter_remove_placeholder': "isb. 2,4-6",
        'pdf_splitter_process': "Cubungula i-PDF",
        'pdf_splitter_loaded': "I-PDF ilayishiwe. Sicela ukhethe inketho",
        'pdf_read_error': "I-PDF ayikwazanga ukufundwa",
        'pages': "Amakhasi",
        'pages_created': "Amakhasi adaliwe",
        'range_empty': "Sicela ufake uhla lwamakhasi",
        'range_invalid': "Uhla lwamakhasi aluvumelekile",
        'range_created': "Kwenziwe i-PDF entsha enamakhasi akhethiwe:\n{0}",
        'empty_removed': "Amakhasi angenalutho angu-{0} asusiwe.\nOkukhiphayo: {1}",
        'remove_empty': "Sicela ufake amakhasi ozowasusa",
        'remove_invalid': "Amakhasi ozowasusa awavumelekile",
        'remove_done': "Kwenziwe i-PDF ehlanziwe:\n{0}",
        'open_folder': "Vula ifolda",
        'show_in_finder': "Bonisa ku-Finder",
        'pdf_splitter_no_pdf': "Sicela uqale ulayishe ifayela le-PDF.",
        'process_error': "Iphutha ekucubunguleni i-PDF",
        'pages_created_voice': "Amakhasi angu-{0} adaliwe",
        'range_created_voice': "Kwenziwe i-PDF enamakhasi akhethiwe",
        'empty_removed_voice': "Amakhasi angenalutho angu-{0} asusiwe",
        'remove_done_voice': "Kwenziwe i-PDF ehlanziwe",
        'pdf_splitter_split_groups': "Iqembu ngalinye eliqhubekayo lifakwa kufayela elihlukile",
        'range_created_single': "Kwenziwe i-PDF entsha:\n{0}",
        'range_created_multiple': "Kwenziwe amafayela e-PDF angu-{0}.",
        'range_created_voice_single': "Kwenziwe i-PDF eyodwa enamakhasi akhethiwe",
        'range_created_voice_multiple': "Kwenziwe amafayela e-PDF angu-{0}",
        'empty_removed_none_left': "Awekho amakhasi asele",
        'empty_removed_all_empty': "Wonke amakhasi atholakale engenalutho futhi angasuswa. Akukho fayela elenziwe.",
        'preview_single': "Isibonelo: {0}",
        'preview_enter_range': "Sicela ufake uhla lwamakhasi.",
        'preview_invalid_range': "Uhla lwamakhasi aluvumelekile.",
        'preview_file': "Isibonelo: {0}",
        'preview_files': "Isibonelo: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Qala ukuphrinta",
        'print_sent': "Umsebenzi wokuphrinta uthunyelwe",
        'print_now': "Phrinta manje",
        'print_error': "Iphutha ekuphrinteni ngokushesha",
        'print_limited': "Umsebenzi wokuphrinta unomkhawulo kulesi sistimu",
        'print_error_format': "Iphutha ekuphrinteni ngokushesha: {0}",
        'warning': "Isexwayiso",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Shintshela kumodi ekhanyayo",
        'mode_switch_to_dark': "Shintshela kumodi emnyama",
        'mode_dark_activated': "Imodi emnyama isebenze",
        'mode_light_activated': "Imodi ekhanyayo isebenze",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Ukubuka konke",
        'zoom_two_pages': "Amakhasi amabili eceleni",
        'zoom_overview': "Imodi yokubuka konke",
        'zoom_cannot_during_search': "Awukwazi ukusondeza ngesikhathi usesha",
        'zoom_exit_first': "Sicela uqale uphume kusondezo",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Ukuhudula nokuwisa kuvuliwe",
        'drag_disabled': "Ukuhudula nokuwisa kuvaliwe",
        'drag_page_grab': "Ukubamba ikhasi {0}",
        'drag_page_dropped': "Ikhasi {0} lifakwe endaweni {1}",
        'drag_position_invalid': "Indawo ayivumelekile",
        'drag_same_position': "Ikhasi {0} lisale endaweni {0}",
        'drag_error': "Iphutha ekuhambiseni",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Ukufaka umbhalo ngokufometha okuthuthukile nokuphathwa kwezingxenye zombhalo",
        'text_templates': "Izingxenye zombhalo ezitholakalayo:",
        'text_name': "Igama",
        'text_preview': "Isibonelo sombhalo",
        'text_enter': "Umbhalo:",
        'text_font_size': "Usayizi wefonti:",
        'text_formatting': "Ukufometha:",
        'text_bold': "Ngqindilili",
        'text_italic': "Malukeke",
        'text_underline': "Dweba umugqa ngaphansi",
        'text_alignment': "Ukuqondanisa:",
        'text_left': "Kwesokunxele",
        'text_center': "Maphakathi",
        'text_right': "Kwesokudla",
        'text_color': "Umbala wombhalo:",
        'text_opacity': "Ukungaboni kahle:",
        'text_word_wrap': "Ukugoqa umugqa:",
        'text_auto': "Okuzenzakalelayo",
        'text_page_width_95': "Ububanzi bekhasi (95%)",
        'text_page_width_85': "Banzi kakhulu (85%)",
        'text_page_width_75': "Banzi (75%)",
        'text_page_width_60': "Banzi (60%)",
        'text_page_width_50': "Maphakathi (50%)",
        'text_page_width_30': "Mincane (30%)",
        'text_page_width_20': "Mincane kakhulu (20%)",
        'text_page_width_10': "Mincane kakhulu (10%)",
        'text_no_wrap': "Akukho kugoqa",
        'text_private': "Ingxenye yombhalo eyimfihlo (idinga ukuqinisekiswa)",
        'text_preview_label': "Isibonelo:",
        'text_preview_placeholder': "Isibonelo sombhalo sizoboniswa lapha...",
        'text_no_text': "(Akukho mbhalo)",
        'text_save_template': "💾 Londoloza njengengxenye",
        'text_delete_template': "🗑 Susa ingxenye yombhalo ekhethiwe",
        'text_show_private': "Bonisa okuyimfihlo",
        'text_hide_private': "Fihla okuyimfihlo",
        'text_use': "✅ Sebenzisa umbhalo",
        'text_saved': "Ingxenye yombhalo igcinwe njenge:\n{0}",
        'text_saved_voice': "Ingxenye yombhalo igcinwe",
        'text_deleted': "Ingxenye yombhalo isusiwe",
        'text_no_text_to_save': "Awukho mbhalo ongagcinwa.",
        'text_no_templates': "Azikho izingxenye zombhalo ezitholakalayo",
        'text_private_master_required': "Izingxenye eziyimfihlo zingasetshenziswa kuphela uma iphasiwedi eyinhloko isethiwe.\n\nUyafuna ukusetha iphasiwedi eyinhloko manje?",
        'text_filename': "Igama lefayela lengxenye yombhalo (ngaphandle kuka-'Text_' no-'.txt'):",
        'text_filename_hint': "Isibonelo: 'Ucingo Lwasekhaya' luzogcinwa ngokuthi 'Text_Ucingo Lwasekhaya.txt'",
        'text_save_hint': "Ingxenye yombhalo izogcinwa ngokuzenzakalelayo inefomethi.",
        'text_guide_title': "Ukufaka umbhalo - Umhlahlandlela",
        'text_delete_confirm': "Uqinisekile ukuthi ufuna ukususa le ngxenye yombhalo?\n\nIfayela: {0}\nUmbhalo: {1}...",
        'text_make_public': "Maka njengokwasesidlangalaleni",
        'text_make_private': "Maka njengokuyimfihlo",
        'text_privacy_changed': "Isimo sobumfihlo sishintshiwe",
        'text_private_always': "Okuyimfihlo kubonakala njalo (isilungiselelo)",
        'text_mode_required': "Sicela uqale uvule imodi yombhalo",
        'text_continue_editing': "Qhubeka nokuhlela - ikhesa isekugcineni kombhalo",
        'text_no_input': "Akukho mbhalo ofakiwe - umbhalo ulahliwe",
        'save_dialog_question': "Ufuna ukuqhubeka kanjani?",
        'text_save_question': "Ngilondoloze yonke imibhalo neziphambano, ngizilungise, ngiqhubeke nokuhlela noma ngizilahle?",
        'copy_cross': "Isiphambano sikopishiwe",
        'paste_cross': "Isiphambano sinamathiselwe",
        'paste_text': "Umbhalo unamathiselwe",
        'cross_discarded': "Isiphambano silahliwe",
        'all_discarded': "Konke kulahliwe",
        'text_discarded': "Umbhalo ulahliwe",
        'no_texts_to_save': "Ayikho imibhalo ongayigcina",
        'no_valid_texts': "Ayikho imibhalo evumelekile ongayigcina",
        'text_word_singular': "umbhalo",
        'text_word_plural': "imibhalo",
        'cross_word_singular': "isiphambano",
        'cross_word_plural': "iziphambano",
        'texts_saved_title': "Imibhalo igciniwe",
        'texts_crosses_saved': "{0} {1} kanye {2} {3} kufakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'texts_crosses_saved_voice': "{0} {1} kanye {2} {3} kugciniwe.",
        'texts_saved': "{0} {1} kufakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'texts_saved_voice': "{0} {1} kugciniwe.",
        'crosses_saved': "{0} {1} kufakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'crosses_saved_voice': "{0} {1} kugciniwe.",
        'elements_saved': "Izinto ezingu-{0} zifakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'elements_saved_voice': "Izinto ezingu-{0} zigciniwe.",
        'text_window_load_error': "Iwindi lombhalo alikwazanga ukulayishwa",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Ukufaka umbhalo nezingxenye zombhalo – Umhlahlandlela onemininingwane**

        **1. Ukufaka nokuhlela umbhalo**
        - Chofoza ngakwesokudla endaweni oyifunayo embhalweni bese ukhetha "Faka umbhalo".
        - Kuzovuleka ingxoxo lapho ungafaka khona umbhalo wakho futhi uwufometha:
        • Usayizi wefonti, ngqindilili, malukeke, dweba umugqa ngaphansi
        • Umbala wombhalo (uyakwazi ukukhetha)
        • Ukungaboni kahle (ngokusebenzisa isilayidi)
        • Ukugoqa umugqa (ububanzi obuhlukahlukene, isb. ububanzi bekhasi, okuncane, akukho kugoqa)
        - Ngemva kokuqinisekisa, umbhalo uzovela endaweni ochofoze kuyo. Ungawuhambisa ngemawusi noma ngezinkinobho zomcibisholo.
        - Chofoza kabili embhalweni ukuze uvule imodi yokuhlela; cindezela i-ESC ukuze uphume.

        **2. Ukuphatha izingxenye zombhalo (izifanekiso)**
        - Engxoxweni yombhalo, uzobona uhlu lwazo zonke izingxenye zombhalo ezigciniwe ngakwesokunxele.
        - **Ukugcina ingxenye:** Faka umbhalo wakho, wufometha, bese uchofoza ku-"💾 Londoloza njengengxenye". Faka igama lefayela (ngaphandle kwesandiso).
        - **Ukulayisha ingxenye:** Chofoza egameni olifunayo ohlwini. Umbhalo nefomethi yakhe kuzothathwa futhi kungalungiswa uma kudingeka.
        - **Ukususa:** Ngokuchofoza ngakwesokudla engxenyeni, ungayisusa noma ushintshe isimo sayo sobumfihlo.

        **3. Izingxenye zombhalo eziyimfihlo (Iphasiwedi eyinhloko)**
        - Uma usethe iphasiwedi eyinhloko (ngaphansi kwezilungiselelo → Ukuphathwa kwamaphasiwedi), ungamaka izingxenye njengeziyimfihlo.
        - Vula ibhokisi lokuhlola elithi "Ingxenye yombhalo eyimfihlo" engxoxweni ngaphambi kokugcina.
        - Izingxenye eziyimfihlo zizoboniswa ohlwini kuphela uma usufake iphasiwedi yakho eyinhloko kanye ngeseshini (ukuqinisekisa ngophawu lokukhiya noma ekufinyeleleni kokuqala).
        - Ngale ndlela ungavikela izingxenye zombhalo eziyimfihlo ekufinyeleleni kwabanye.

        **4. Ukufaka iziphambano**
        - Ngemenyu yomongo, ungakwazi futhi ukufaka isiphambano esiyisithombe (isb. kumabhokisi okuhlola).
        - Usayizi, ubukhulu bomugqa kanye nombala weziphambano kungalungiswa emhlabeni wonke ezilungiselelweni (imenyu "Izilungiselelo" → "Izilungiselelo zeziphambano").
        - Ngokuchofoza ngakwesokudla esiphambanweni esikhona, ungakwazi ukusishintsha ngokukhethekile.

        **5. Izenzo ezinengqikithi**
        - Uma ufake imibhalo eminingi noma iziphambano ekhasini elilodwa, ungakwazi ukugcina noma ukulahla zonke izinto ndawonye ngemenyu yomongo (chofoza ngakwesokudla kumodi yombhalo).
        - Lapho ugcina, zonke izinto zizofakwa ku-PDF futhi zihlale ziyizithombe ze-vector.

        **6. Izinqamuli zekhibhodi kumodi yombhalo**
        - Izinkinobho zomcibisholo: hambisa into
        - Ctrl+izinkinobho zomcibisholo: izinyathelo ezinkulu
        - Enter: vula ingxoxo yokugcina (gcina konke / lungisa / lahla)
        - ESC: lahla into yamanje
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Ukufaka umbhalo nezingxenye zombhalo – Umhlahlandlela onemininingwane</strong></p>

        <p><strong>1. Ukufaka nokuhlela umbhalo</strong></p>
        <ul>
        <li>Chofoza ngakwesokudla endaweni oyifunayo embhalweni bese ukhetha "Faka umbhalo".</li>
        <li>Kuzovuleka ingxoxo lapho ungafaka khona umbhalo wakho futhi uwufometha:<br/>
        • Usayizi wefonti, ngqindilili, malukeke, dweba umugqa ngaphansi<br/>
        • Umbala wombhalo (uyakwazi ukukhetha)<br/>
        • Ukungaboni kahle (ngokusebenzisa isilayidi)<br/>
        • Ukugoqa umugqa (ububanzi obuhlukahlukene, isb. ububanzi bekhasi, okuncane, akukho kugoqa)</li>
        <li>Ngemva kokuqinisekisa, umbhalo uzovela endaweni ochofoze kuyo. Ungawuhambisa ngemawusi noma ngezinkinobho zomcibisholo.</li>
        <li>Chofoza kabili embhalweni ukuze uvule imodi yokuhlela; cindezela i-ESC ukuze uphume.</li>
        </ul>

        <p><strong>2. Ukuphatha izingxenye zombhalo (izifanekiso)</strong></p>
        <ul>
        <li>Engxoxweni yombhalo, uzobona uhlu lwazo zonke izingxenye zombhalo ezigciniwe ngakwesokunxele.</li>
        <li><strong>Ukugcina ingxenye:</strong> Faka umbhalo wakho, wufometha, bese uchofoza ku-"💾 Londoloza njengengxenye". Faka igama lefayela (ngaphandle kwesandiso).</li>
        <li><strong>Ukulayisha ingxenye:</strong> Chofoza egameni olifunayo ohlwini. Umbhalo nefomethi yakhe kuzothathwa futhi kungalungiswa uma kudingeka.</li>
        <li><strong>Ukususa:</strong> Ngokuchofoza ngakwesokudla engxenyeni, ungayisusa noma ushintshe isimo sayo sobumfihlo.</li>
        </ul>

        <p><strong>3. Izingxenye zombhalo eziyimfihlo (Iphasiwedi eyinhloko)</strong></p>
        <ul>
        <li>Uma usethe iphasiwedi eyinhloko (ngaphansi kwezilungiselelo → Ukuphathwa kwamaphasiwedi), ungamaka izingxenye njengeziyimfihlo.</li>
        <li>Vula ibhokisi lokuhlola elithi "Ingxenye yombhalo eyimfihlo" engxoxweni ngaphambi kokugcina.</li>
        <li>Izingxenye eziyimfihlo zizoboniswa ohlwini kuphela uma usufake iphasiwedi yakho eyinhloko kanye ngeseshini (ukuqinisekisa ngophawu lokukhiya noma ekufinyeleleni kokuqala).</li>
        <li>Ngale ndlela ungavikela izingxenye zombhalo eziyimfihlo ekufinyeleleni kwabanye.</li>
        </ul>

        <p><strong>4. Ukufaka iziphambano</strong></p>
        <ul>
        <li>Ngemenyu yomongo, ungakwazi futhi ukufaka isiphambano esiyisithombe (isb. kumabhokisi okuhlola).</li>
        <li>Usayizi, ubukhulu bomugqa kanye nombala weziphambano kungalungiswa emhlabeni wonke ezilungiselelweni (imenyu "Izilungiselelo" → "Izilungiselelo zeziphambano").</li>
        <li>Ngokuchofoza ngakwesokudla esiphambanweni esikhona, ungakwazi ukusishintsha ngokukhethekile.</li>
        </ul>

        <p><strong>5. Izenzo ezinengqikithi</strong></p>
        <ul>
        <li>Uma ufake imibhalo eminingi noma iziphambano ekhasini elilodwa, ungakwazi ukugcina noma ukulahla zonke izinto ndawonye ngemenyu yomongo (chofoza ngakwesokudla kumodi yombhalo).</li>
        <li>Lapho ugcina, zonke izinto zizofakwa ku-PDF futhi zihlale ziyizithombe ze-vector.</li>
        </ul>

        <p><strong>6. Izinqamuli zekhibhodi kumodi yombhalo</strong></p>
        <ul>
        <li>Izinkinobho zomcibisholo: hambisa into</li>
        <li>Ctrl+izinkinobho zomcibisholo: izinyathelo ezinkulu</li>
        <li>Enter: vula ingxoxo yokugcina (gcina konke / lungisa / lahla)</li>
        <li>ESC: lahla into yamanje</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Izilungiselelo zeziphambano",
        'cross_properties': "Izici zesiphambano",
        'cross_size': "Usayizi (px):",
        'cross_line_width': "Ubukhulu bomugqa:",
        'cross_color': "Umbala:",
        'cross_choose_color': "Khetha",
        'cross_fine_tuning': "Ukulungisa kahle lapho ugcina (amaphikseli)",
        'cross_offset_x': "I-offset engu-X:",
        'cross_offset_y': "I-offset engu-Y:",
        'cross_offset_x_tooltip': "Amanani amabi ahambisa isiphambano kwesokunxele lapho ugcina, amahle ayakwesokudla",
        'cross_offset_y_tooltip': "Amanani amabi ahambisa isiphambano phezulu lapho ugcina, amahle phansi",
        'cross_preview': "Isibonelo",
        'cross_save': "Sebenzisa izilungiselelo",
        'cross_customized': "Isiphambano silungisiwe",
        'cross_settings_applied': "Izilungiselelo zesiphambano zigciniwe.\nUsayizi: {0}px, Ubukhulu bomugqa: {1}px\n{2}",

        'cross_updated_count': "Iziphambano ezikhona ezing-{0} zibuyekezwe.",
        'cross_no_crosses': "Awekho ama-cross akhona.",
        'cross_settings_applied_all': "Izilungiselelo zeziphambano zisetshenziswe kuwo wonke ama-cross angu-{0}",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Izilungiselelo zamasignesha",
        'signature_1': "Isignesha 1",
        'signature_2': "Isignesha 2",
        'signature_select': "Khetha isignesha",
        'signature_add': "➕ Faka isignesha entsha...",
        'signature_size': "Usayizi wesignesha {0} (%):",
        'signature_common': "Izilungiselelo ezijwayelekile",
        'signature_timestamp': "Faka isikhathi ngokuzenzakalelayo",
        'signature_location': "Indawo ejwayelekile:",
        'signature_timestamp_size': "Usayizi wefonti yesikhathi:",
        'signature_no_files': "-- Azikho izignesha ezitholakalayo --",
        'signature_insert': "Faka isignesha",
        'signature_insert_1': "Faka isignesha 1",
        'signature_insert_2': "Faka isignesha 2",
        'signature_customize': " Lungisa le signesha",
        'signature_discard': " Lahla le signesha",
        'signature_save_all': " Londoloza wonke amasignesha",
        'signature_discard_all': " Lahla wonke amasignesha",
        'signature_guide_title': "Amasignesha - Umhlahlandlela",
        'signature_guide': """
📝 Amasignesha - Umhlahlandlela osheshayo

- Setha iphasiwedi eyinhloko
- Hlela amasignesha kumenyu yezilungiselelo
  (usayizi, isikhathi ...)
- Faka ngokuchofoza kwesokudla endaweni oyifunayo
  (iphasiwedi eyinhloko iyadingeka kanye ngeseshini)
- Hambisa isignesha ngemawusi noma ngezinkinobho zomcibisholo
- Ungafaka amasignesha amaningi ngokulandelana
- Isignesha ngayinye ingalungiswa ngokukhethekile
- Lahla isignesha eyodwa
- Londoloza / lahla wonke amasignesha kanyekanye
- Ungasebenzisa nomugqa wemenyu.
        """,
        'signature_placeholder': "Asikho isibonelo esitholakalayo",
        'signature_info': "Isignesha {0}: {1}×{2} px ({3}% ye-{4}×{5})",
        'signature_info_placeholder': "Izilungiselelo zesignesha {0}",
        'signature_inserted': "Isignesha {0} ifakwe ekhasini {1}",
        'signature_deleted': "Isignesha isusiwe",
        'signature_copied': "Isignesha ikopishiwe",
        'signature_pasted': "Isignesha {0} inamathiselwe",
        'signature_saved': "Amasignesha angu-{0} afakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'signature_saved_voice': "Amasignesha angu-{0} agciniwe",
        'mode_replace_signature_format': "Qeda imodi bese ufaka isignesha {0}",
        'mode_conflict_voice_signature': "Imodi ye-{0} isebenza. Ukuyiqeda bese ufaka isignesha?",
        'signature_not_configured': "Isignesha {0} ayihlelekile",
        'signature_file_not_found': "Ifayela lesignesha alitholakali",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Asikho isignesha esikopishiwe",
        'no_signatures_to_save': "Awekho amasignesha ongawagcina",
        'signature_save_question': "Londoloza wonke amasignesha, ulungise noma ulahle lona?",
        'signatures_saved_title': "Amasignesha agciniwe",
        'signatures_saved': "Amasignesha angu-{0} afakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'signatures_saved_voice': "Amasignesha angu-{0} agciniwe.",
        'all_signatures_discarded': "Wonke amasignesha alahliwe",
        'signature_settings_saved': "Izilungiselelo ze-signesha zigciniwe",
        'signature_cancelled': "Isignesha ilahliwe",
        'signature_active_title': "Isignesha iyasebenza",
        'signature_replace_question': "Kunesignesha esebenzayo kakade.\n\nUfuna ukushintsha isignesha yamanje?",
        'signature_replace': "Shintsha isignesha",
        'signature_replace_voice': "Shintsha isignesha yamanje noma khansela?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Izilungiselelo zezithombe",
        'image_common': "Izilungiselelo ezijwayelekile zezithombe",
        'image_keep_aspect': "Gcina isilinganiso ngenkathi uhudula",
        'image_default_size': "Usayizi omisiwe (%):",
        'image_dark_invert': "Phendula izithombe kwimodi emnyama",
        'image_dark_invert_tooltip': "Kuvuliwe: izithombe zizophendulwa ukuze zibonakale kangcono",
        'image_fine_tuning': "Ukulungisa okuhle (amaphikseli)",
        'image_offset_x': "I-offset engu-X:",
        'image_offset_y': "I-offset engu-Y:",
        'image_offset_x_tooltip': "Amanani amabi ahambisa isithombe kwesokunxele lapho ugcina, amahle ayakwesokudla",
        'image_offset_y_tooltip': "Amanani amabi ahambisa isithombe phezulu lapho ugcina, amahle phansi",
        'image_select': "Khetha isithombe",
        'image_insert': "Faka isithombe",
        'image_customize': " Lungisa lesi sithombe",
        'image_aspect': " Gcina isilinganiso",
        'image_discard': " Lahla lesi sithombe",
        'image_save_all': " Londoloza zonke izithombe",
        'image_discard_all': " Lahla zonke izithombe",
        'image_filter': "Izithombe",
        'image_guide_title': "Faka isithombe - Umhlahlandlela",
        'image_guide': """
📷 Ukufaka isithombe ku-PDF - Umhlahlandlela osheshayo:

1. Chofoza ngakwesokudla endaweni oyifunayo
2. "Faka isithombe" → Khetha isithombe
3. Beka isithombe: hudula ngemawusi
4. Lungisa usayizi: hudula emakhoneni/emaphethelweni
5. Gcina isilinganiso: cindezela inkinobho [A]
6. Okunye ukulungisa: chofoza ngakwesokudla esithombeni

Ithiphu: Kumenyu yomongo, ungakwazi ukulungisa izilungiselelo.
        """,
        'image_inserted': "Isithombe {0} sifakwe ekhasini {1}",
        'image_deleted': "Isithombe silahliwe",
        'image_copied': "Isithombe sikopishiwe",
        'image_pasted': "Isithombe sinamathiselwe",
        'image_saved': "Izithombe ezingu-{0} zifakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'image_saved_voice': "Izithombe ezingu-{0} zigciniwe",
        'image_aspect_on': "kuvuliwe",
        'image_aspect_off': "kuvaliwe",
        'image_aspect_toggle': "Gcina isilinganiso {0}",
        'image_reset': "Isithombe sibuyiselwe kusayizi woqobo",
        'image_replaced': "Isithombe seshintshiwe",
        'image_invalid': "Akusona isithombe esivumelekile",
        'mode_replace_image': "Faka isithombe",
        'mode_conflict_voice_image': "Imodi ye-{0} isebenza. Ukuyiqeda bese ufaka isithombe?",
        'image_active_title': "Isithombe siyasebenza",
        'image_replace_question': "Kunesithombe esisebenzayo kakade.\n\nUfuna ukushintsha isithombe samanje?",
        'image_replace': "Shintsha isithombe",
        'image_replace_voice': "Shintsha isithombe samanje noma khansela?",
        'image_filter_all': "Izithombe (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Wonke amafayela (*.*)",
        'no_copied_image': "Asikho isithombe esikopishiwe",
        'image_discarded': "Isithombe silahliwe",
        'image_save_question': "Londoloza zonke izithombe, ulungise noma ulahle lena?",
        'no_images_to_save': "Azikho izithombe ongazigcina",
        'no_valid_images': "Azikho izithombe ezivumelekile ongazigcina",
        'images_saved_title': "Izithombe zigciniwe",
        'images_saved': "Izithombe ezingu-{0} zifakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'images_saved_voice': "Izithombe ezingu-{0} zigciniwe.",
        'all_images_discarded': "Zonke izithombe zilahliwe",
        'image_settings_updated': "Izilungiselelo zezithombe zibuyekezwe",
        'image_replace_title': "Khetha isithombe esisha",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Izilungiselelo zezimo",
        'form_basic': "Izilungiselelo eziyisisekelo",
        'form_default_type': "Uhlobo lwesimo olumisiwe:",
        'form_rectangle': "Unxande",
        'form_ellipse': "I-ellipse",
        'form_line': "Umugqa",
        'form_arrow': "Umcibisholo",
        'form_line_width': "Ubukhulu bomugqa:",
        'form_colors': "Imibala",
        'form_line_color': "Umbala womugqa:",
        'form_fill_color': "Umbala wokugcwalisa:",
        'form_choose_color': "Khetha",
        'form_transparent': "Ingemuva elihle (umugqa kuphela)",
        'form_filled': "kugcwalisiwe",
        'form_dark_mode': "Imodi emnyama",
        'form_dark_invert': "Phendula imibala kwimodi emnyama",
        'form_fine_tuning': "Ukulungisa okuhle (amaphikseli)",
        'form_offset_x': "I-offset engu-X:",
        'form_offset_y': "I-offset engu-Y:",
        'form_offset_x_tooltip': "Amanani amabi ahambisa isimo kwesokunxele lapho ugcina, amahle ayakwesokudla",
        'form_offset_y_tooltip': "Amanani amabi ahambisa isimo phezulu lapho ugcina, amahle phansi",
        'form_preview': "Isibonelo",
        'form_insert': "Faka isimo",
        'form_rectangle_insert': "Unxande",
        'form_ellipse_insert': "I-ellipse/Indilinga",
        'form_line_insert': "Umugqa (ukuchofoza kabili)",
        'form_arrow_insert': "Umcibisholo (ukuchofoza kabili)",
        'form_customize': " Lungisa lesi simo",
        'form_transparent_toggle': " Ingemuva elihle",
        'form_discard': " Lahla lesi simo",
        'form_save_all': " Londoloza zonke izimo",
        'form_discard_all': " Lahla zonke izimo",
        'form_guide_title': "Faka isimo - Umhlahlandlela",
        'form_guide': """
📐 Ukufaka isimo ku-PDF - Umhlahlandlela osheshayo:

1. Khetha uhlobo lwesimo (Unxande, I-ellipse, Umugqa, Umcibisholo)
2. Chofoza endaweni
   - Kunxande/i-ellipse: ukuchofoza kanye kubeka isimo
   - Emugqeni/umcibisholo: ukuchofoza kabili ukuze ubeke indawo yokuqala neyokugcina
3. Beka isimo: hudula ngemawusi
4. Lungisa usayizi: hudula emakhoneni/emaphethelweni
5. Londoloza isimo: Enter
6. Lahla isimo: ESC
7. Okunye ukulungisa: chofoza ngakwesokudla esimweni

Ithiphu: Kumenyu yomongo, ungakwazi ukulungisa izilungiselelo.
        """,
        'form_inserted': "{0} kufakwe ekhasini {1}",
        'form_deleted': "Isimo sisusiwe",
        'form_copied': "Isimo sikopishiwe",
        'form_pasted': "Isimo sinamathiselwe",
        'form_saved': "Izimo ezingu-{0} zifakwe ku-PDF.\n\nI-PDF iphinde yalayishwa...",
        'form_saved_voice': "Izimo ezingu-{0} zigciniwe",
        'form_reset': "Isimo sibuyiselwe kusayizi omisiwe",
        'form_transparent_on': "kuvuliwe",
        'form_transparent_off': "kuvaliwe",
        'form_transparent_toggled': "Ingemuva elihle {0}",
        'form_line_cancel': "Ukudweba umugqa kukhanseliwe",
        'form_second_click': "Manje chofoza indawo yokugcina ye-{0}",
        'mode_replace_form': "Faka isimo",
        'mode_conflict_voice_form': "Imodi ye-{0} isebenza. Ukuyiqeda bese ufaka isimo?",
        'form_settings_updated': "Izilungiselelo zezimo zibuyekezwe",
        'form_unknown': "Isimo",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Chofoza indawo yokuqala",
        'form_line_guide_2': "2. Chofoza indawo yokugcina",
        'form_line_guide_3': "Umugqa uzodwetshwa phakathi kwalezi zindawo ezimbili.",
        'form_line_status_1': "Ilinde ukuchofoza kokuqala...",
        'form_line_status_2': "Indawo yokuqala isethiwe: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Manje chofoza indawo yokugcina...",
        'form_line_status_4': "Zombili izindawo zisethiwe.\nChofoza 'Qeda' ukuze ugcine.",
        'form_line_reset': "Setha kabusha",
        'form_line_finish': "Qeda",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopisha (Cmd+C)",
        'paste': "Namathisela (Cmd+V)",
        'copied': "Kukopishiwe: {0}",
        'no_element_to_copy': "Akukho nto ekhethiwe ongayikopisha",
        'no_copied_data': "Awekho amadatha akopishiwe",
        'no_valid_position': "Ayikho indawo evumelekile yokunamathisela",
        'copy_text': "Umbhalo ukopishiwe",
        'copy_image': "Isithombe sikopishiwe",
        'copy_form': "Isimo sikopishiwe",
        'copy_signature': "Isignesha ikopishiwe",
        'element_text': "Umbhalo",
        'element_image': "Isithombe",
        'element_form': "Isimo",
        'element_signature': "Isignesha",
        'element_unknown': "Into",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Ukungqubuzana kwemodi",
        'mode_conflict_message': "Imodi '{0}' isivele isebenza.\n\nUfuna ukuyiqeda bese {1}?",
        'mode_replace': "Qeda imodi bese {0}",
        'mode_cancel': "Khansela",
        'mode_replace_text': "ufaka umbhalo",
        'mode_replace_cross': "ufaka isiphambano",
        'mode_replace_signature': "ufaka isignesha",
        'mode_replace_image': "ufaka isithombe",
        'mode_replace_form': "ufaka isimo",
        'mode_conflict_voice': "Imodi ye-{0} isebenza. Ukuyiqeda bese ufaka umbhalo?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Ukufaka umbhalo",
        'active_mode_signature': "Isignesha",
        'active_mode_image': "Isithombe",
        'active_mode_form': "Isimo",
        'active_mode_and': " futhi ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Faka",
        'insert_another_text': "Faka umbhalo",
        'insert_another_cross': "Faka isiphambano",
        'insert_another_signature_1': "Isignesha 1",
        'insert_another_signature_2': "Isignesha 2",
        'insert_another_image': "Faka isithombe",
        'insert_another_form_rect': "Unxande",
        'insert_another_form_ellipse': "I-ellipse",
        'insert_another_form_line': "Umugqa (ukuchofoza kabili)",
        'insert_another_form_arrow': "Umcibisholo (ukuchofoza kabili)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Londoloza {0}",
        'save_dialog_message': "I-{0} izogcinwa ekhasini {1}.\n\nUfuna ukuqhubeka kanjani?",
        'save_all': "Londoloza konke {0}",
        'save_single': "Londoloza {0}",
        'save_customize': "Lungisa {0}",
        'save_discard': "Lahla le {0}",
        'save_continue': "Qhubeka nokuhlela",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Iya ekhasini {0}",
        'context_rotate': " Zungezisa ikhasi {0}",
        'context_delete': " Susa ikhasi {0}",
        'context_export': " Thumela ikhasi {0} ngaphandle",
        'context_mark_as': " Maka ikhasi njenge...",
        'context_mark_empty': " Ikhasi elingenalutho",
        'context_unmark_empty': " Alisenalutho",
        'context_mark_export': " Maka ukuze lithunyelwe ngaphandle",
        'context_unmark_export': " Susa umaka wokuthumela ngaphandle",
        'context_batch_actions': " Izenzo ezinengqikithi",
        'context_batch_delete_empty': " Susa wonke amakhasi angenalutho angu-{0}",
        'context_batch_export_single': " Thumela wonke amakhasi angu-{0} ngaphandle (ifayela elilodwa)",
        'context_batch_export_split': " Thumela wonke amakhasi angu-{0} ngaphandle (ehlukanisiwe)",
        'context_drag_start': " Qala ukuhudula nokuwisa",
        'context_drag_stop': " Misa ukuhudula nokuwisa",
        'context_insert': " Faka",
        'context_insert_pages': " Faka amakhasi",
        'context_zoom': "Sondeza",
        'discard_mixed': "Lahla konke okungu-{0} {1} kanye okungu-{2} {3}",
        'save_mixed': "Londoloza okungu-{0} {1} kanye okungu-{2} {3}",
        'discard_texts': "Lahla yonke imibhalo engu-{0}",
        'discard_text_single': "Lahla umbhalo o-1",
        'save_texts': "Londoloza imibhalo engu-{0}",
        'save_text_single': "Londoloza umbhalo o-1",
        'discard_crosses': "Lahla zonke iziphambano ezingu-{0}",
        'discard_cross_single': "Lahla isiphambano esi-1",
        'save_crosses': "Londoloza iziphambano ezingu-{0}",
        'save_cross_single': "Londoloza isiphambano esi-1",
        'discard_signatures': "Lahla wonke amasignesha angu-{0}",
        'save_signature_single': "Londoloza isignesha ey-1",
        'save_signatures': "Londoloza amasignesha angu-{0}",
        'discard_images': "Lahla zonke izithombe ezingu-{0}",
        'save_image_single': "Londoloza isithombe esi-1",
        'save_images': "Londoloza izithombe ezingu-{0}",
        'discard_forms': "Lahla zonke izimo ezingu-{0}",
        'save_form_single': "Londoloza isimo esi-1",
        'save_forms': "Londoloza izimo ezingu-{0}",
        'cross_discard': "Lahla lesi siphambano",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Ulwazi lokuthumela ngaphandle / ukungenisa",
        'export_what': "📋 Kuthunyelwani ngaphandle?",
        'export_general': "Izilungiselelo ezijwayelekile",
        'export_general_items': "• Ukukhishwa kwezwi (kuvuliwe/kuvaliwe, isivinini)\n• Imodi emnyama/ekhanyayo\n• Izilungiselelo zesipele\n• Izilungiselelo ze-OCR",
        'export_image_form': "Izilungiselelo zezithombe nezimo",
        'export_image_form_items': "• Izilungiselelo zezithombe (isilinganiso, usayizi omisiwe)\n• Izilungiselelo zezimo (ubukhulu bomugqa, imibala)\n• Izilungiselelo zamasignesha (izindlela, usayizi, isikhathi)",
        'export_passwords': "Isizindalwazi samaphasiwedi",
        'export_passwords_items': "• Wonke amaphasiwedi e-PDF agciniwe\n• Ngokukhetha afihliwe noma akhishiwe",
        'export_master': "Izilungiselelo zephasiwedi eyinhloko",
        'export_master_items': "• I-hash yephasiwedi eyinhloko\n• Izilungiselelo zamasignesha/izingxenye zombhalo",
        'export_signatures': "Amasignesha nezingxenye zombhalo",
        'export_signatures_items': "• Wonke amafayela ezithombe (amasignesha)\n• Zonke izingxenye zombhalo ezinefomethi\n• Izimpawu zobumfihlo/ezomphakathi",
        'export_import_warning': "⚠️ Imibono ebalulekile",
        'export_import_note': "• Lapho ungenisa, ZONKE izilungiselelo zamanje ziyabhintshelwa phezu\n• Ukuqala kabusha uhlelo kuyadingeka\n• Amasignesha/izingxenye zombhalo ezikhona ziyashintshwa",
        'export_master_note': "• Uma iphasiwedi eyinhloko isethiwe, ungakhetha:\n  - Akhishiwe (amaphasiwendi abonakala njengombhalo ocacile)\n  - Afihliwe (angafundwa kuphela ngephasiwedi eyinhloko)",
        'export_security': "• Ifayela le-ZIP elithunyelwe ngaphandle liqukethe idatha ebucayi\n• Sicela uligcine ngokuphephile (isb. ku-USB efihliwe)\n• Uma ifayela lilahleka: amaphasiwedi awakwazi ukutholakala kabusha",
        'export_format': "📁 Ifomethi yokuthumela ngaphandle",
        'export_format_desc': "Izilungiselelo zizogcinwa kwifayela elilodwa le-ZIP:",
        'export_filename': "PDFDarkView_Izilungiselelo_YYYYMMDD_HHMMSS.zip",
        'export_success': "Izilungiselelo zithunyelwe ngaphandle ngempumelelo",
        'export_failed': "Ukuthumela ngaphandle kwehlulekile",
        'export_import_question': "Ufuna ukuqala kabusha uhlelo manje?",
        'export_password_question': "Iphasiwedi eyinhloko isethiwe.\n\nUfuna ukuthumela amaphasiwedi ngaphandle ekhishiwe?\n(uma kungenjalo azothunyelwa efihliwe)",
        'export_decrypt': "Thumela ngaphandle ekhishiwe",
        'export_encrypt': "Thumela ngaphandle efihliwe",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Ulwazi",
        'info_title': "Mayelana ne-PDF Dark View",
        'info_version': "Inguqulo",
        'info_author': "Ithuthukiswe ngu-Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Mayelana",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>I-PDF Dark View</strong> iyisibukeli se-PDF esifinyelelekayo, esithuthukiswe ngokukhethekile kubantu abanezinkinga zokubona.</p>

            <p><strong>Izici Eziyinhloko:</strong></p>
            <ul>
                <li>Isikhombi esinombala ophikisanayo, esingashintshwa</li>
                <li>Ukulawulwa okuphelele kwekhibhodi</li>
                <li>Ukuphuma kwezwi okuhlanganisiwe</li>
                <li>I-OCR yemibhalo eskeniwe</li>
                <li>Amathuluzi okuhlela abanzi</li>
            </ul>

            <p>Sekela izilimi ezingaphezu kwe-50 – ukuze ama-PDF afinyeleleke kuwo wonke umuntu.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Izici",
        'info_features_intro': "I-PDF Dark View ikunikeza la mathuba alandelayo:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Ukubukisa nokuzulazula</strong> – Imodi emnyama/ekhanyayo, ukuphenya amakhasi, ukusondeza, ukugxumela ekhasini</li>
            <li><strong>I-OCR (Ukuqaphela umbhalo)</strong> – Yenza imibhalo eskeniwe ibe nokuseshwa nokukopishwa</li>
            <li><strong>Ukuhlela</strong> – Faka umbhalo, iziphambano, amasiginesha, izithombe nezinhlobo</li>
            <li><strong>Ukuphatha Amakhasi</strong> – Susa, khipha, faka, hambisa ngokuhudula nokubeka</li>
            <li><strong>Ukuthumela ngaphandle</strong> – Ku-Word, Pages noma njengombhalo</li>
            <li><strong>Ukuvikeleka</strong> – Ukuvikelwa nokuphathwa kwephasiwedi</li>
            <li><strong>Ukufinyeleleka</strong> – Ukuphuma kwezwi, ukulawula ngekhibhodi, umbala ophikisanayo ophezulu</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Ukusebenzisa",
        'info_accessibility': "♿ Ukufinyeleleka – ukulawulwa okuphelele kwekhibhodi",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Jikelele</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Vula i-PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Sesha</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Shintsha imodi emnyama/ekhanyayo</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Phrinta</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Phuma</div>

        <div class="shortcut-cat">📖 Ukuzulazula</div>
        <div class="shortcut-row"><kbd>Okhiye bamatshe</kbd> Phenya ikhasi ngelinye</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Iya ekhasini</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Ikhasi lokuqala</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Ikhasi lokugcina</div>

        <div class="shortcut-cat">✏️ Ukuhlela</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Faka umbhalo</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Susa amakhasi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Khipha amakhasi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Faka amakhasi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Hambisa amakhasi</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Phendulela ikhasi</div>

        <div class="shortcut-cat">🖼️ Ukuhambisa izakhi</div>
        <div class="shortcut-row"><kbd>Okhiye bamatshe</kbd> Hambisa umbhalo/isithombe/isiginesha</div>
        <div class="shortcut-row"><kbd>Ctrl+Okhiye bamatshe</kbd> Izinyathelo ezinkulu</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Gcina</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Lahla</div>

        <div class="shortcut-cat">🗣️ Ukuphuma kwezwi</div>
        <div class="shortcut-row"><kbd>F2</kbd> Vula/vala ukuphuma kwezwi</div>
        """,
        'info_contextmenu': "📌 Okubalulekile: Yonke imisebenzi iyatholakala nange-menue yomongo (inkinobho yesokudla yegundane)!",
        'info_accessibility_hint': "💡 Ithiphu: Ukuphuma kwezwi (F2) kwenza kube lula ukuzithola futhi kunikeza impendulo ngamamenyu nezingxoxo.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Ilayisense & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Ulwazi ngokwe-§ 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        I-imeyili: binhdiez64@gmail.com<br>
        Ophethe okuqukethwe: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Ukuzikhipha emthwalweni</strong><br>
        Isoftware ithuthukiswe ngokucophelela okukhulu. Akukho siqinisekiso esinikezwayo ngokunemba, ukuphelela nokusebenza. Ukusetshenziswa kusengcupheni yakho.<br><br>

        <strong>📄 Ilayisense ye-MIT (ukusetshenziswa kwangasese)</strong><br>
        Ilungelo lobunikazi (c) 2026 Toralf Schulz (BinhDiez)<br>
        Okuvunyelwe: ukusetshenziswa kwamahhala, izinguquko zangasese, amakhophi omuntu siqu.<br>
        Okungavunyelwe: ukuthengisa, ukusetshenziswa kwezentengiso, ukususa izaziso zamalungelo obunikazi.<br><br>

        <strong>🔧 Izingxenye zomuntu wesithathu</strong><br>
        Le software iqukethe izingxenye ngaphansi kwamalayisense e-GPL, AGPL, Apache 2.0, BSD ne-MIT.<br>
        Lapho usabalalisa futhi, kufanele kuthotshwe imigomo yelayisense efanele.<br><br>

        <strong>🌐 Umthombo Ovulekile</strong><br>
        Ikhodi yomthombo iyatholakala futhi ingabukwa, iguqulwe futhi isatshalaliswe kabusha ngokwemigomo yelayisense efanele.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Ukubonga",
        'info_credits': "Siyabonga emphakathini womthombo ovulekile",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Ukucubungula i-PDF</li>
            <li><strong>PyQt5</strong> – Isikhombi sezithombe</li>
            <li><strong>Tesseract OCR</strong> – Ukuqaphela umbhalo</li>
            <li><strong>OCRmyPDF</strong> – Ukuhlanganiswa kwe-OCR</li>
            <li><strong>python-docx</strong> – Ukuthumela ngaphandle ku-Word</li>
            <li><strong>qtawesome</strong> – Izithonjana</li>
            <li><strong>DeepSeek</strong> – Ukusekelwa ekuhumusheni (50+ izilimi)</li>
            <li><strong>Bonke abasebenzisi</strong> – Ngempendulo ebekiwe</li>
            <li><strong>Umphakathi womthombo ovulekile</strong> – Ngemithombo emihle</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Izilimi",
        'info_languages_header': "🌍 Ukusekelwa Kwezilimi",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>I-PDF Dark View okwamanje isekela <strong>izilimi ezingama-62</strong> – ukuze isofthiwe isetshenziswe kalula emhlabeni wonke.</p>

            <p><strong>📖 Uhlu oluphelele lwezilimi (NgoMashi 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 IsiBhunu</li>
                    <li>🇦🇱 Isi-Albania (Shqip)</li>
                    <li>🇩🇿 Isi-Arabhu (العربية)</li>
                    <li>🇮🇩 Isi-Bali (Basa Bali)</li>
                    <li>🇧🇩 Isi-Bengali (বাংলা)</li>
                    <li>🇲🇲 Isi-Burmese (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Isi-Bosnia (Bosanski)</li>
                    <li>🇧🇬 Isi-Bulgariya (Български)</li>
                    <li>🇨🇳 IsiShayina (中文)</li>
                    <li>🇩🇰 Isi-Danish (Dansk)</li>
                    <li>🇩🇪 IsiJalimani (Deutsch)</li>
                    <li>🇬🇧 IsiNgisi (English)</li>
                    <li>🇪🇪 Isi-Estonia (Eesti)</li>
                    <li>🇫🇮 Isi-Finnish (Suomi)</li>
                    <li>🇫🇷 IsiFulentshi (Français)</li>
                    <li>🇬🇷 IsiGreki (Ελληνικά)</li>
                    <li>🇮🇱 IsiHebheru (עברית)</li>
                    <li>🇮🇳 IsiHindi (हिन्दी)</li>
                    <li>🇭🇷 Isi-Croatia (Hrvatski)</li>
                    <li>🇭🇺 Isi-Hungary (Magyar)</li>
                    <li>🇮🇩 Isi-Indonesia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Isi-Irish (Gaeilge)</li>
                    <li>🇮🇸 Isi-Icelandic (Íslenska)</li>
                    <li>🇮🇹 IsiNtaliyane (Italiano)</li>
                    <li>🇯🇵 Isi-Japanese (日本語)</li>
                    <li>🇰🇭 Isi-Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Isi-Korean (한국어)</li>
                    <li>🇱🇦 Isi-Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Isi-Latvia (Latviešu)</li>
                    <li>🇱🇹 Isi-Lithuania (Lietuvių)</li>
                    <li>🇱🇺 Isi-Luxembourg (Lëtzebuergesch)</li>
                    <li>🇲🇾 Isi-Malay (Bahasa Melayu)</li>
                    <li>🇮🇳 Isi-Marathi (मराठी)</li>
                    <li>🇲🇳 Isi-Mongolia (Монгол)</li>
                    <li>🇳🇵 Isi-Nepali (नेपाली)</li>
                    <li>🇳🇱 Isi-Dutch (Nederlands)</li>
                    <li>🇳🇴 Isi-Norway (Norsk)</li>
                    <li>🇦🇫 Isi-Pashto (پښتو)</li>
                    <li>🇮🇷 Isi-Persian (فارسی)</li>
                    <li>🇵🇱 Isi-Polish (Polski)</li>
                    <li>🇵🇹 Isi-Portuguese (Português)</li>
                    <li>🇮🇳 Isi-Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Isi-Romania (Română)</li>
                    <li>🇷🇺 Isi-Russian (Русский)</li>
                    <li>🇸🇪 Isi-Swedish (Svenska)</li>
                    <li>🇷🇸 Isi-Serbia (Српски)</li>
                    <li>🇸🇰 Isi-Slovak (Slovenčina)</li>
                    <li>🇸🇮 Isi-Slovenia (Slovenščina)</li>
                    <li>🇪🇸 Isi-Spanish (Español)</li>
                    <li>🇹🇿 IsiSwahili (Kiswahili)</li>
                    <li>🇵🇭 Isi-Tagalog (Filipino)</li>
                    <li>🇮🇳 Isi-Tamil (தமிழ்)</li>
                    <li>🇮🇳 Isi-Telugu (తెలుగు)</li>
                    <li>🇹🇭 Isi-Thai (ไทย)</li>
                    <li>🇨🇿 Isi-Czech (Čeština)</li>
                    <li>🇹🇷 Isi-Turkish (Türkçe)</li>
                    <li>🇺🇦 Isi-Ukraine (Українська)</li>
                    <li>🇵🇰 Isi-Urdu (اردو)</li>
                    <li>🇻🇳 Isi-Vietnamese (Tiếng Việt)</li>
                    <li>🇸🇳 Isi-Wolof (Wolof)</li>
                    <li>🇺🇸 Isi-Yiddish (ייִדיש)</li>
                    <li>🇿🇦 IsiZulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Faka izilimi zakho:</strong><br>
                Ufuna ulimi olungakafakwa? Vele ubeke ifayela lakho lesichazamazwi (<code>sprache_xx.py</code>) eduze nohlelo – isofthiwe izolibona ngokuzenzakalela. Uma unentshisekelo ekuhumusheni okukhethekile, sicela ungithinte.
            </div>

            <p><strong>🙏 Ukubonga okukhethekile:</strong> I-DeepSeek ngokusekela ekuhumusheni zonke izichazamazwi ngezilimi ezingama-62.</p>

            <p>📧 Oxhumana nabo ngezihumusho: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Iphutha",
        'error_occurred': "Kuvele iphutha",
        'error_pdf_load': "Iphutha ekulayisheni i-PDF",
        'error_pdf_save': "Iphutha ekugcineni i-PDF",
        'error_ocr': "Iphutha ekuqashelweni kombhalo",
        'error_no_pdf': "Ayikho i-PDF elayishiwe",
        'error_page_not_found': "Ikhasi alitholakali",
        'error_invalid_range': "Uhla lwamakhasi aluvumelekile",
        'error_file_not_found': "Ifayela alitholakali",
        'error_permission': "Awunayo imvume",
        'error_unknown': "Iphutha elingaziwa",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Kuyaphumelela",
        'success_operation': "Umsebenzi uphumelele",
        'success_saved': "Kugcinwe ngempumelelo",
        'success_exported': "Kuthunyelwe ngaphandle ngempumelelo",
        'success_imported': "Kungeniswe ngempumelelo",
        'success_deleted': "Kususiwe ngempumelelo",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Qinisekisa",
        'confirm_yes': "Yebo",
        'confirm_no': "Cha",
        'confirm_ok': "Kulungile",
        'confirm_cancel': "Khansela",
        'confirm_delete': "Susa",
        'confirm_overwrite': "Bhala phezu",
        'confirm_continue': "Qhubeka",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Iyalayisha i-PDF...",
        'progress_saving': "Iyalondoloza i-PDF...",
        'progress_exporting': "Ithumela ngaphandle i-PDF...",
        'progress_processing': "Iyacubungula...",
        'progress_wait': "Sicela ulinde...",
        'progress_preparing': "Iyalungiselela...",
        'progress_finalizing': "Iyaqeda...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Mhlophe",
        'color_black': "Mnyama",
        'color_red': "Bomvu",
        'color_green': "Luhlaza",
        'color_blue': "Luhlaza okwesibhakabhaka",
        'color_yellow': "Phuzi",
        'color_magenta': "Consi",
        'color_cyan': "Luhlaza okwesibhakabhaka okukhanyayo",
        'color_orange': "Iwolintshi",
        'color_gray': "Mpunga",
        'color_custom': "Ukukhetha umbala",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Ifayela",
        'menu_edit': "&Hlela",
        'menu_view': "&Buka",
        'menu_tools': "&Amathuluzi",
        'menu_settings': "&Izilungiselelo",
        'menu_help': "&Usizo",
        'menu_language': "🌐 Ulimi",
        'menu_guides': "&Imihlahlandlela",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Vula",
        'file_save_as': "&Londoloza njenge...",
        'file_protect': "&Vikela umbhalo...",
        'file_export': "&Thumela ngaphandle",
        'file_export_pages': "Thumela ngaphandle njenge-Pages",
        'file_export_word': "Thumela ngaphandle njenge-DOCX",
        'file_export_text': "Thumela ngaphandle njenge-TXT",
        'file_print_now': "&Phrinta manje",
        'file_print': "&Phrinta",
        'file_close': "&Vala",
        'file_quit': "&Phuma",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Sesha",
        'edit_ocr': " Yenza i-OCR",
        'edit_rotate': "&Zungezisa ikhasi",
        'edit_rotate_all': "&Zungezisa wonke amakhasi",
        'edit_delete_pages': "&Susa amakhasi",
        'edit_extract_pages': "&Khipha amakhasi",
        'edit_insert_pages': "&Faka amakhasi",
        'edit_move_pages': "&Hambisa amakhasi",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Faka umbhalo neziphambano",
        'text_insert': " Faka umbhalo",
        'cross_insert': " Faka isiphambano",
        'text_customize': " Lungisa lo mbhalo",
        'cross_customize': " Lungisa lesi siphambano",
        'cross_customize_all': " Lungisa zonke iziphambano",
        'text_discard': " Lahla lo mbhalo / lesi siphambano",
        'text_discard_all': " Lahla yonke imibhalo neziphambano",
        'text_save_all': " Londoloza yonke imibhalo neziphambano",
        'text_guide': " Ukufaka umbhalo / izingxenye zombhalo - Umhlahlandlela",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Faka isignesha",
        'signature_settings_menu': " Izilungiselelo...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Faka isithombe",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Faka isimo",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Bonisa iwindi lombhalo",
        'view_zoom': "&Sondeza",
        'view_zoom_page': "&Ububanzi bekhasi (okuzenzakalelayo)",
        'view_zoom_two': "&Amakhasi amabili",
        'view_zoom_overview': "&Ukubuka konke (amakhasi amaningi)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Amathuluzi okufinyeleleka",
        'settings_voice': "Ukukhishwa kwezwi",
        'settings_voice_tooltip': "kwengeza ulwazi olwengeziwe ekukhishweni kwezwi kwezifundi zesikrini",
        'settings_signature': "&Izilungiselelo zamasignesha",
        'settings_password': "&Ukuphathwa kwamaphasiwedi",
        'settings_backup': "Yenza isipele ngaphambi kwezinguquko",
        'settings_export_import': "&Thumela ngaphandle / ngenisa izilungiselelo",
        'settings_export': "&Thumela zonke izilungiselelo ngaphandle...",
        'settings_import': "&Ngenisa zonke izilungiselelo...",
        'settings_export_info': "&Kuthunyelwani ngaphandle?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "kuvuliwe",
        'voice_off': "kuvaliwe",
        'voice_toggle': "Ukukhishwa kwezwi {0}",
        'voice_speed': "Isivinini singu-{0} amaphesenti",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Ithuluzi alitholakali:\n{0}\n\nBASE_DIR: {1}\nQinisekisa ukuthi amathuluzi e-PDF afakiwe kumkhombandlela {1}.",
        'tool_started': "{0} iqaliwe",
        'tool_start_failed': "Ayikwazanga ukuqalwa",
        'process_error_failed_to_start': "Inqubo ayikwazanga ukuqalwa. Ingabe ifayela likhona?",
        'process_error_crashed': "Inqubo yaphahlazeka ngenkathi iqala.",
        'process_error_timeout': "Isikhathi senqubo siphelile.",
        'process_error_write': "Iphutha ekubhaleni kwinqubo.",
        'process_error_read': "Iphutha ekufundeni kwinqubo.",
        'process_error_unknown': "Iphutha lenqubo elingaziwa",
        'process_command': "Umyalo",
        'process_normal_exit': "iphume ngokujwayelekile",
        'process_crashed': "yaphahlazeka",
        'process_nonzero_exit': "{0} iphume ngekhodi yephutha {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Kuyakhanselwa...",
        'move_cancelling': "Ukuhambisa kuyakhanselwa",
        'opening_pdf': "I-PDF iyavulwa...",
        'loading_document': "Umbhalo uyalayishwa...",
        'pdf_opened': "I-PDF ivuliwe",
        'pages_found_moving': "Kutholakale amakhasi angu-{0}, angu-{1} okuhambisa",
        'creating_backup': "Kwenziwa isipele...",
        'backup_description': "Kwenziwa isipele sefayela lokuqala...",
        'backup_saved_as': "Kugcinwe njengesipele: {0}",
        'error_format': "Iphutha: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDark View ngu BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Ukusesha kusethiwe kabusha",
        'page_header_simple': "=== Ikhasi {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Ukuphathwa kwamaphasiwedi – Umhlahlandlela",
        'password_guide_voice': "Umhlahlandlela wokuphathwa kwamaphasiwedi. Sicela ufunde imibono.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Ukuphathwa kwamaphasiwedi – Umhlahlandlela onemininingwane</strong></p>

        <p><strong>1. Ukuvikelwa kwephasiwedi kuma-PDF</strong></p>
        <ul>
        <li>Lapho uvula i-PDF evikelwe ngephasiwedi, kuvela ingxoxo lapho ungafaka khona iphasiwedi.</li>
        <li>Ungagcina iphasiwedi ifihliwe ukuze ungayifaki njalo (ibhokisi lokuhlola "Londoloza iphasiwedi").</li>
        <li>Ngenkinobho ethi "Susa iphasiwedi", ungakwazi ukwenza ikhophi ye-PDF ekhishiwe futhi ususe iphasiwedi kusizindalwazi.</li>
        </ul>

        <p><strong>2. Iphasiwedi eyinhloko</strong></p>
        <ul>
        <li>Iphasiwedi eyinhloko ivikela ukufinyelela kuwo wonke amaphasiwedi e-PDF agciniwe.</li>
        <li><strong>Ukusetha:</strong> Iya kokuthi "Izilungiselelo → Ukuphathwa kwamaphasiwedi → Izilungiselelo zephasiwedi eyinhloko" bese uchofoza ku-"Setha iphasiwedi eyinhloko". Khetha iphasiwedi eqinile (okungenani izinhlamvu eziyi-8).</li>
        <li><strong>Ukushintsha:</strong> Ngemva kokuqinisekisa ngempumelelo, ungashintsha iphasiwedi yakho eyinhloko.</li>
        <li><strong>Ukususa:</strong> Uma ususa iphasiwedi eyinhloko, WONKE amaphasiwedi agciniwe ayosuswa unomphela. Ungakwazi ukuthumela isipele ngaphandle kuqala.</li>
        <li>Kanye ngeseshini, kumele uqinisekise ngephasiwedi yakho eyinhloko ukuze ufinyelele imisebenzi evikelekile (isb. ukubonisa amaphasiwedi).</li>
        </ul>

        <p><strong>3. Ukuphathwa kwamaphasiwedi (uhlu)</strong></p>
        <ul>
        <li>Ngaphansi kwe-"Izilungiselelo → Ukuphathwa kwamaphasiwedi", uvula ithebula lawo wonke ama-PDF agciniwe anamaphasiwedi awo afihliwe.</li>
        <li><strong>Ngaphandle kwephasiwedi eyinhloko:</strong> Ungakwazi ukususa okufakiwe kuphela – amaphasiwedi ahlala efihliwe.</li>
        <li><strong>Ngephasiwedi eyinhloko (iqinisekisiwe):</strong> Ungakwazi ukubona, ukukopisha, ukuthumela ngaphandle nokususa amaphasiwedi.</li>
        <li><strong>Ukuthumela ngaphandle:</strong> Khetha ifomethi (JSON, CSV, TXT) bese ugcina uhlu. Uma iphasiwedi eyinhloko isethiwe, ungakhetha ukuthi amaphasiwedi athunyelwe ngaphandle njengombhalo ocacile noma ahlale efihliwe.</li>
        <li><strong>Ukungenisa:</strong> Ifayela le-ZIP elithunyelwe ngaphandle ngaphambilini elinazo zonke izilungiselelo (kuhlanganise namaphasiwedi) lingafundwa kabusha nge-"Izilungiselelo → Thumela ngaphandle / ngenisa izilungiselelo". Qaphela: Idatha ekhona izobhalwa phezu!</li>
        </ul>

        <p><strong>4. Umkhiqizi wephasiwedi</strong></p>
        <ul>
        <li>Engxoxweni yephasiwedi (isb. lapho uvika i-PDF), uthola inkinobho yedayisi 🎲 ngakwesokudla kwebhokisi lokufaka.</li>
        <li>Chofoza kuyo ukuze uvule umkhiqizi wephasiwedi. Ungakwazi ukusetha ubude, amasethi ezinhlamvu (izinhlamvu ezinkulu, ezincane, izinombolo, izimpawu ezikhethekile) kanye nesihlukanisi ukuze kube lula ukufunda.</li>
        <li>Iphasiwedi ekhiqiziwe ingasetshenziswa ngqo futhi ingakopishwa uma kudingeka.</li>
        </ul>

        <p><strong>5. Imibono ebalulekile yokuphepha</strong></p>
        <ul>
        <li>Amaphasiwedi agciniwe agcinwa ngokufihlwa kwe-AES-256. Ukhiye ususelwa kwiphasiwedi yakho eyinhloko (uma isethiwe) noma enanini elingaguquki (ngaphandle kwephasiwedi eyinhloko).</li>
        <li>Ngaphandle kwephasiwedi eyinhloko, amaphasiwedi ayafihlwa kodwa ukhiye ugcinwa ohlelweni – umhlaseli onokufinyelela kumafayela akho angawakhumula. Ngakho-ke, sincoma ngokuqinile ukusebenzisa iphasiwedi eyinhloko.</li>
        <li>Isizindalwazi samaphasiwedi sikumkhombandlela `Daten/passwords.json`. Yenza izipele njalo, ikakhulukazi ngaphambi kokususa iphasiwedi eyinhloko.</li>
        <li>Uma ulahlekelwa iphasiwedi eyinhloko, wonke amaphasiwedi agciniwe ayolahleka unomphela.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Imodi yokuguqula",
        'invert_mode_classic': "Yakudala (guqula yonke imibala)",
        'invert_mode_smart': "Ehlakaniphile (guqula ukukhanya kuphela)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Umkhawulo wesilinganiso sempunga",
        'gray_threshold_10': "10% (qinile)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Okumisiwe)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (ethambile)",
        'threshold_changed': "Umkhawulo usethwe ku-{0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Umkhawulo wesilinganiso sempunga – Incazelo",
        'threshold_guide_text': "Umkhawulo wesilinganiso sempunga unquma ukuthi amapikseli amuphi kumodi emnyama ehlakaniphile abhekwa njenge 'mpunga' futhi aguqulwe.\n\n"
                                "• Inani eliphansi (10%) liguqula kuphela izithunzi ezicishe zifikelele empunga – izakhi ezinemibala zihlala zigcinwe ngokuphelele.\n"
                                "• Inani eliphezulu (50%) libuye liguqule amapikseli anemibala encane – lokhu kwandisa ukuphikisana, kodwa kungahle kuhlanekezela imibala.\n\n"
                                "Inani elifanele lincike kudokhumenti. Emibhalweni emsulwa, u-30–40% uvame ukuba ngcono, kwimifanekiso enemibala kungcono u-10–20%.\n\n"
                                "Ungalungisa inani noma nini ngenkathi ngemenyu 'Izilungiselelo' – i-PDF izophinde ilayishwe ngokushesha.\n\n"
                                "Qaphela:\n* Izithombe nezithombe zingaboniswa kahle kuphela kumodi ekhanyayo!\n* Izilungiselelo zokuguqula ziyaboniswa kuphela lapho imodi emnyama icushiwe.",
        'threshold_guide_voice': "Umkhawulo wesilinganiso sempunga unquma ukuthi imodi emnyama ehlakaniphile ingenelela kangakanani. Inani eliphansi liyagcina imibala, inani eliphezulu liyakhulisa ukuphikisana.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Kuvulwa i-PDF...",
        'progress_loading_document': "Kulayishwa umbhalo...",
        'progress_pdf_opened': "I-PDF ivuliwe",
        'progress_creating_backup': "Kwenziwa isipele...",
        'progress_backup_description': "Kuvikelwa ifayela loqobo...",
        'progress_backup_created': "Isipele senziwe",
        'progress_backup_saved_as': "Kugcinwe njenge: {0}",
        'progress_analyzing_start': "Kuqalwa ukuhlaziya...",
        'progress_searching_empty': "Kuseshwa amakhasi angenalutho...",
        'progress_page_empty': "Ikhasi {0} alinalutho",
        'progress_page_keep': "Gcina ikhasi {0}",
        'progress_analysis_complete': "Ukuhlaziya sekuqediwe",
        'progress_empty_found': "Kutholakale amakhasi angama-{0} angenalutho",
        'progress_current_page': "Ikhasi lamanje",
        'progress_mark_delete': "Kumakwa ukuthi kususwe",
        'progress_range_selected': "Ububanzi bamakhasi {0}-{1}",
        'progress_deleting_pages': "Kususwa amakhasi angama-{0}",
        'progress_creating_new_pdf': "Kwenziwa i-PDF entsha...",
        'progress_transferring_pages': "Kudluliswa amakhasi",
        'progress_keeping_page': "Ikhasi {0} lizogcinwa ({1}/{2})",
        'progress_saving_pdf': "Kugcinwa i-PDF...",
        'progress_optimizing': "Kwenziwa kahle usayizi wefayela...",
        'progress_finalizing': "Kuphethwa...",
        'progress_new_size': "Usayizi omusha: {0:.2f} MB",
        'progress_cancelling': "Kuyahoxiswa...",
        'progress_cancel_message': "{0} kuyahoxiswa",
        'progress_pages_found_moving': "Kutholakale amakhasi angama-{0}, angama-{1} okuhambisa",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Kuhlaziywa i-PDF...",
        'ocr_status_optimizing': "Ukwenziwa kahla kwesithombe kuyaqhubeka...",
        'ocr_status_recognizing': "Ukuqaphela umbhalo kuyaqhubeka...",
        'ocr_status_embedding': "Kushumekwa umbhalo...",
        'ocr_status_finalizing': "Kuphethwa i-PDF...",

        # PDF-Laden
        'progress_preparing': "Kulungiselelwa...",
        'progress_loading': "Kulayishwa i-PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Kususwa amakhasi...",
        'progress_moving_title': "Kuhambiswa amakhasi...",
        'pages_found': "Amakhasi atholakele",
        'progress_creating_new_order': "Kwenziwa uhlelo olusha...",
        'progress_sorting_pages': "Kuhlelwa amakhasi...",
        'progress_moving_to_begin': "Hambisa amakhasi angama-{0} ekuqaleni",
        'progress_transferring_count': "Dlulisa amakhasi angama-{0}",
        'progress_transferring_before_target': "Dlulisa amakhasi ngaphambi kwethagethi",
        'progress_moving_pages': "Hambisa amakhasi angama-{0}",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_isipele_",
        'filename_protected_suffix': "_evikelwe_",
        'filename_copy_suffix': "_Ikhophi",
        'filename_page_single': "_Ikhasi_",
        'filename_page_range': "_Amakhasi_",
        'filename_export_page': "_Ikhasi_{0:03}",
        'filename_export_range': "_Amakhasi_{0}-{1}",
        'filename_export_multiple': "_Amakhasi_{0}",
        'filename_with_text': "_ngombhalo",
        'filename_with_signature': "_ngeziginesha",
        'filename_with_image': "_ngesithombe",
        'filename_with_forms': "_ngezinhlobo",
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
        'view_toggle_navbar': "Bonisa umugqa wezinkinobho",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Akukwazi ukususa wonke amakhasi",
		'pages_cannot_delete_last_page': 'Ikhasi lokugcina alikwazi ukususwa!',
		'pages_cannot_delete_all_pages': 'Kumele kusale okungenani ikhasi elilodwa kudokhumenti!',
		'delete_pages_confirm': 'Uyaqiniseka ukuthi ufuna ukususa amakhasi angu-{0}?',
		'delete_pages_confirm_voice': 'Uyaqiniseka ukuthi ufuna ukususa amakhasi angu-{0}?',
		'pages_deleted': 'Amakhasi angu-{0} asuswe ngempumelelo.',
		'warning': 'Isixwayiso',
		'error': 'Iphutha',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Ayikho ifomu ekhethiwe",
        'form_customized': "Ifomu ishintshiwe",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Khetha",
        'btn_use': "Sebenzisa",
        'master_password_for_spasswords': "Ukuze ugcine futhi usebenzise amaphasiwedi, kufanele kuqala usethe iphasiwedi eyinhloko.\n\nIngabe ufuna ukusetha iphasiwedi eyinhloko manje?",
        'open_saved_dialog_title': "Vula ifayela eligciniwe",
        'open_saved_question': "Ingabe ufuna ukuvula ifayela eligciniwe manje?",
        'password': "Iphasiwedi",
        'password_manager_master_required': "Umphathi wamaphasiwedi uyatholakala kuphela uma iphasiwedi eyinhloko isethiwe.\n\nIngabe ufuna ukusetha iphasiwedi eyinhloko manje?",
        'password_master_required_for_select': "Ukuze ubone futhi ukhethe amaphasiwedi agciniwe, kufanele uqale uqinisekise ngephasiwedi yakho eyinhloko.\n\nIngabe ufuna ukuqinisekisa manje?",
        'password_not_available': "Iphasiwedi ekhethiwe ayitholakali noma ayikwazanga ukuqoshwa kabusha.",
        'password_options_title': "Izinketho zephasiwedi",
        'password_save_choice_change': "Setha iphasiwedi entsha",
        'password_save_choice_keep': "Sebenzisa iphasiwedi ekhona",
        'password_save_choice_none': "Gcina ngaphandle kokubethela",
        'password_save_hint': "Qala usethe iphasiwedi eyinhloko ukuze ugcine amaphasiwedi ngokuphepha.",
        'password_save_master_required': "Gcina iphasiwedi (kungenzeka kuphela ngephasiwedi eyinhloko)",
        'password_save_question': "I-PDF yamanje ivikelwe ngephasiwedi. Ingabe ufuna ukusebenzisa iphasiwedi ekhona, usethe entsha, noma ugcine ngaphandle kokubethela?",
        'password_select': "Khetha iphasiwedi",
        'password_select_none': "Ayikho iphasiwedi ekhethiwe.\n\nSicela ukhethe iphasiwedi ohlwini.",
        'password_select_one': "Sicela ukhethe iphasiwedi eyodwa kuphela.\n\nUmake amaphasiwedi amaningi.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_isipele",
        'filename_insert_suffix': "_nokufaka",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_amakhasi_asusiwe",
        'filename_pages_moved': "_amakhasi_ahanjisiwe",
        'filename_rotated_all_suffix': "_wonke_amakhasi_aphenduliwe",
        'filename_rotated_suffix': "_ikhasi_eliphenduliwe",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Ukuhlelwa kwamagama efayela uma ushintsha i-PDF",
        'filename_keep_suffixes': "Gcina izandiso zangaphambilini (isb. _ngombhalo)",
        'filename_keep_suffixes_false': "Shintsha",
        'filename_keep_suffixes_true': "Gcina",
        'filename_preview_label': "Isibonelo segama lefayela:",
        'filename_preview_overwrite_hint': "Isibonelo asitholakali – okwangempela kuzobhalwa phezu kwaso.",
        'filename_separator': "Isihlukanisi phakathi kwamagama",
        'filename_separator_none': "Akukho sihlukanisi",
        'filename_separator_space': "Isikhala ( )",
        'filename_separator_underscore': "Umugqa ongaphansi (_)",
        'filename_settings_saved': "Izilungiselelo zegama lefayela zigciniwe",
        'filename_settings_title': "Ukufomatha igama lefayela nesipele",
        'filename_timestamp_position': "Indawo yesitembu sesikhathi",
        'filename_timestamp_position_after': "Ngemva kwegama lesisekelo",
        'filename_timestamp_position_before': "Phambili kakhulu",
        'filename_timestamp_position_end': "Ekugcineni",
        'filename_use_timestamp': "Sebenzisa isitembu sesikhathi",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Ukuziphatha lapho ushintsha:</b><ul><li>Ukususa nokufaka amakhasi</li><li>Ukufaka umbhalo, isiginesha, isithombe namajamo</li><li>OCR</li></ul></html>",
        'backup_section': "Isipele semisebenzi yamakhasi (Susa, Hambisa)",
        'behavior_info': "Inothi: Lapho 'Kubhala phezu kwangempela', izitembu zesikhathi nezijobelelo ziyanakwa – ifayela ligcina igama lalo.",
        'behavior_new_file': "Yenza ifayela elisha njalo (ngesitembu sesikhathi nesijobelelo)",
        'behavior_overwrite': "Bhala phezu kwangempela (alikho ifayela elisha)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Wonke amakhasi aphenduliwe.\n\nOkwangempela akushintshanga.\nIfayela elisha: {0}",
        'all_pages_rotated_voice': "Wonke amakhasi aphenduliwe, kwenziwe ifayela elisha.",
        'empty_pages_deleted_new_file': "Amakhasi angu-{0} angenalutho asusiwe.\n\nOkwangempela akushintshanga.\nIfayela elisha: {1}",
        'empty_pages_deleted_voice': "Amakhasi angenalutho angu-{0} asusiwe, kwenziwe ifayela elisha.",
        'ocr_keep_original': "Gcina okwangempela (vula ngesandla kamuva)",
        'ocr_new_file_question': "I-PDF entsha engaseshwa igcinwe lapha:\n{0}\n\nIngabe ufuna ukuyivula manje?",
        'ocr_open_new': "Vula ifayela elisha le-OCR",
        'ocr_original_kept': "Ifayela langempela lihlala livuliwe. Ifayela le-OCR ligciniwe.",
        'page_deleted_new_file': "Ikhasi {0} lisusiwe.\n\nOkwangempela akushintshanga.\nIfayela elisha: {1}",
        'page_deleted_voice': "Ikhasi {0} lisusiwe, kwenziwe ifayela elisha.",
        'page_rotated_new_file': "Ikhasi {0} liphenduliwe.\n\nOkwangempela akushintshanga.\nIfayela elisha: {1}",
        'page_rotated_voice': "Ikhasi {0} liphenduliwe, kwenziwe ifayela elisha.",
        'pages_deleted_new_file': "Amakhasi angu-{0} asusiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha: {1}",
        'pages_deleted_new_file_voice': "Amakhasi angu-{0} asusiwe, kwenziwe ifayela elisha.",
        'pages_inserted_new_file': "Amakhasi angu-{0} afakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha: {1}",
        'pages_inserted_new_file_ask': "Amakhasi angu-{0} afakiwe.\n\nOkwangempela akushintshanga.\nIfayela elisha: {1}\n\nIngabe ufuna ukuyivula manje?",
        'pages_inserted_voice_new': "Amakhasi angu-{0} afakiwe, kwenziwe ifayela elisha.",
        'pages_moved_new_file': "Amakhasi angu-{0} ahanjisiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha: {1}",
        'pages_moved_new_file_voice': "Amakhasi angu-{0} ahanjisiwe, kwenziwe ifayela elisha.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ungaphinde ubonise",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Isilungiselelo sezipele</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Isipele SIVULIWE</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Kuzo zonke izinguquko ezibhala phezu kwangempela</strong> (umbhalo, isiginesha, isithombe, ijamo, OCR, ukuphendula, ukufaka, ukususa/ukuhambisa amakhasi) <strong>isipele esinezitembu zesikhathi senziwa ngokuzenzakalelayo</strong> ngaphambi kokuthi ushintsho lusetshenziswe.</p>
                <p style="margin: 5px 0 5px 20px;">• Isipele sitholakala eceleni kwefayela langempela (isb. <code>Umbhalo_isipele_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Uma uphinde wasebenzisa inketho <strong>„Bhala phezu kwangempela“</strong>, nayo isipele siyenzeka.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Isipele SIVALIWE</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Ayikho isipele eyenziwayo</strong> – noma lapho ubhala phezu, noma lapho wenza imisebenzi yamakhasi.</p>
                <p style="margin: 5px 0 5px 20px;">• Ifayela langempela lingalahleka ungalokothi ulithole uma ubhala phezu kwalo.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Iyanconywa kubasebenzisi abanolwazi kuphela!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Ithiphu:</strong> Isilungiselelo sezipele sizimele kunenketho ethi „Bhala phezu kwangempela“. Ungahlanganisa kokubili.<br>
                Ungawufihla unomphela lo mlayezo.
            </div>
        </div>
        """,
        'backup_info_title': "Ukuziphatha kwesipele",
        'backup_info_voice': "Isaziso mayelana nokuziphatha kwesipele emisebenzini yamakhasi. Isipele sivuliwe sibhala phezu kwangempela, isipele sivaliwe senza ifayela elisha.",
        'show_backup_info': "Ulwazi mayelana nesilungiselelo sezipele",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ungaphinde ubonise",
        'overwrite_enable_backup': "Nika amandla isipele (kuyaconywa)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Bhala phezu kwangempela</p>
            <p>Uma uvula le nketho, izinguquko (umbhalo, isiginesha, isithombe, ijamo, OCR, ukuphendula, ukufaka) <strong>zigcinwa ngqo kokwangempela</strong> – <strong>akukho fayela elisha elenziwayo</strong>.</p>
            <p>• Igama lefayela alishintshi.<br>
            • Izitembu zesikhathi nezijobelelo ziyanakwa.<br>
            • <strong>Ngaphandle kwesipele, okwangempela kungalahleka ungalokothi ulithole.</strong></p>
            <p style="color: #FFD700;">Isincomo: Phinda wenze nketho yesipele ukuze uthole izipele ezizenzakalelayo.</p>
        </div>
        """,
        'overwrite_info_title': "Bhala phezu kwangempela",
        'overwrite_info_voice': "Isixwayiso: Bhala phezu kwangempela – alikho ifayela elisha. Isipele siyaconywa.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Amakhasi angu-{0} afakiwe.\n\nIfayela langempela libhalwe phezu kwalo.\nIsipele senziwe.",
        'pages_inserted_overwrite_no_backup': "Amakhasi angu-{0} afakiwe.\n\nIfayela langempela libhalwe phezu kwalo.\nAKUKHO sipele esenziwe.",
        'texts_saved_overwrite_with_backup': "Izingushuko zigcinwe kokwangempela.\n\nIsipele senziwe.",
        'texts_saved_overwrite_no_backup': "Izingushuko zigcinwe kokwangempela.\n\nAKUKHO sipele esenziwe.",
        'texts_crosses_saved_new_file': "{0} {1} kanye no-{2} {3} bafakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha lenziwe.\n\nI-PDF entsha iyalayisha...",
        'texts_saved_new_file': "{0} {1} bafakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha lenziwe.\n\nI-PDF entsha iyalayisha...",
        'crosses_saved_new_file': "{0} {1} bafakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha lenziwe.\n\nI-PDF entsha iyalayisha...",
        'elements_saved_new_file': "Izinto ezingu-{0} zifakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha lenziwe.\n\nI-PDF entsha iyalayisha...",
        'signatures_saved_overwrite_with_backup': "Isiginesha (ama) sigcinwe kokwangempela.\n\nIsipele senziwe.",
        'signatures_saved_overwrite_no_backup': "Isiginesha (ama) sigcinwe kokwangempela.\n\nAKUKHO sipele esenziwe.",
        'images_saved_overwrite_with_backup': "Isithombe (ama) sigcinwe kokwangempela.\n\nIsipele senziwe.",
        'images_saved_overwrite_no_backup': "Isithombe (ama) sigcinwe kokwangempela.\n\nAKUKHO sipele esenziwe.",
        'forms_saved_overwrite_with_backup': "Ijamo (ama) ligcinwe kokwangempela.\n\nIsipele senziwe.",
        'forms_saved_overwrite_no_backup': "Ijamo (ama) ligcinwe kokwangempela.\n\nAKUKHO sipele esenziwe.",
        'signatures_saved_new_file': "Amasiginesha angu-{0} afakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha lenziwe.\n\nI-PDF entsha iyalayisha...",
        'images_saved_new_file': "Izithombe ezingu-{0} zifakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha lenziwe.\n\nI-PDF entsha iyalayisha...",
        'forms_saved_new_file': "Amajamo angu-{0} afakiwe.\n\nIfayela langempela alishintshanga.\nIfayela elisha lenziwe.\n\nI-PDF entsha iyalayisha...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Isixwayiso: Le PDF inamakhasi aphenduliwe. Ukuma kungahluka.",
        'page_rotated_warning_title': "Ikhasi eliphenduliwe litholiwe",
        'page_rotated_warning_message': "Ikhasi lamanje {0} liphenduliwe ngo-{1}°.\n\nUkufaka izinto emakhasi aphenduliwe akusekelwa.\n\nIngabe ufuna ukuphendula ikhasi endaweni eqondile manje?",
        'page_rotated_warning_voice': "Isixwayiso: Ikhasi liphenduliwe. Sicela uliphendule kuqala.",
        'paste_on_rotated_page_simple_warning': "Ukufaka ekhasi {0} akunakwenzeka!\n\nLeli khasi liphenduliwe ngo-{1}°.\n\nSicela uqale uphendule ikhasi libe ngu-0° (Imenyu: Hlela → Qondanisa ikhasi).\n\nIsixwayiso:\nInto oyikopishe ngaphambili izolahleka uma ungagcini ngaphambi kokuphendula ikhasi.",
        'paste_on_rotated_page_voice': "Ukufaka kukhanseliwe. Ikhasi liphenduliwe. Sicela uqale uqondanise ikhasi.",
        'page_rotated_cancel': "Khansela",
        'page_rotated_rotate_until_upright': "Phendula ikhasi kaningi (kuze kube liqondile)",
        'page_rotated_now_upright': "Ikhasi manje seliqondile. Manje usungafaka.",
        'page_rotated_still_not_upright': "Ikhasi alikwazanga ukuphindulelwa endaweni eqondile. Sicela ulungise ngesandla.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Usizo: Lungisa amakhasi aphenduliwe",
        'help_rotated_pages_voice': "Usizo lokulungisa amakhasi aphenduliwe luyavulwa.",
        'btn_help': "Usizo",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Inkinga: Ikhasi eliphenduliwe – Ukufaka akusebenzi kahle</p>

            <p>Uma ukufaka imibhalo, amasiginesha noma amajamo ekhasini eliphenduliwe kungasebenzi kahle, ungayilungisa ikhasi ngesihleli se-PDF sangaphandle.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Isixazululo ngethuluzi langaphandle (isb. Isibonisi se-macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Thela ikhasi ngaphandle</strong><br>
                &nbsp;&nbsp;Chofoza kumenyu ku <strong>Ifayela → Thela njengamakhasi</strong> noma sebenzisa enye indlela ukugcina ikhasi olifunayo njenge-PDF eyodwa.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Vula ikhasi kuhlelo lwangaphandle</strong><br>
                &nbsp;&nbsp;Vula i-PDF ekhiphile kusihleli se-PDF (isb. <strong>Isibonisi se-macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Phendula ikhasi</strong><br>
                &nbsp;&nbsp;Phendula ikhasi ukuze liqondane (ku-Isibonisi: <strong>Amathuluzi → Phendula</strong> noma <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Gcina</strong><br>
                &nbsp;&nbsp;Gcina ikhasi elilungisiwe (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Faka kabusha ikhasi kudokhumenti langempela</strong><br>
                &nbsp;&nbsp;Buyela ku-PDFDarkView bese ufaka ikhasi elilungisiwe endaweni oyifunayo:<br>
                &nbsp;&nbsp;<strong>Hlela → Faka amakhasi</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Okunye: Phendula ikhasi kokwangempela</p>
                <p style="margin: 5px 0 5px 20px;">• Sebenzisa umsebenzi wokuphendula owakhelwe ngaphakathi (<strong>Hlela → Phendula ikhasi</strong>) ukulungisa ikhasi isinyathelo ngesinyathelo.<br>
                • Ngemva kokuphendula ngakunye, ungahlola ukuthi ukufaka kusebenza yini manje.<br>
            • Lesi isixazululo esisheshayo – zama lesi kuqala!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Ithiphu:</strong> Uma uvame ukuhlangabezana namakhasi aphenduliwe, ungayifihla unomphela isixwayiso kukhokhelo lokufaka.<br>
                Ukuma kungase kwehluke – sebenzisa le nketho kuphela uma wazi imiphumela.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Qondanisa amakhasi",
        'menu_rotate_normalize_tooltip': "Phendula ikhasi noma setha kabusha ku-0°",
        'normalize_current_page': "Letha ikhasi lamanje endaweni eqondile (setha ku-0°)",
        'normalize_all_pages': "Letha wonke amakhasi endaweni eqondile (setha ku-0°)",
        'page_normalized': "Ikhasi {0} lisethiwe endaweni eqondile.",
        'all_pages_normalized': "Wonke amakhasi asethiwe endaweni eqondile.",
        'page_already_upright': "Ikhasi {0} selivele liqondile.",
        'all_pages_already_upright': "Wonke amakhasi aseqondile kakade.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>I-PDF ayinawo umbhalo ongasheshwa.</p><p>Ingabe ufuna ukwenza i-OCR ukuze ukhiphele ku-{0}?</p>",
        'export_ocr_voice': "I-PDF ayinawo umbhalo. I-OCR iyadingeka ukuze ukhiphele ku-{0}.",
        'export_no_ocr_possible': "Ukukhipha ngaphandle kwe-OCR akunakwenzeka. Sicela wenze i-OCR ngekhoza.",
        'ocr_failed_export_not_possible': "I-OCR yehlulekile. Ukukhipha akukwazi ukwenziwa.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "I-PDF izovulwa ku-Isibonisi. Sicela uqale inqubo yokuphrinta lapho.",
        'print_preview_manual': "I-PDF ivuliwe. Sicela usebenzise umyalo wokuphrinta ngesandla (isb. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Hlanganisa ama-PDF",
        'merge_pdfs': "Hlanganisa ama-PDF",
        'merge_progress_title': "Kuhlanganiswa ama-PDF...",
        'merge_pdfs_list': "Ama-PDF ngokulandelana (Hudula bese uyeka ukuze uhlele)",
        'merge_add_pdf': "Engeza i-PDF",
        'merge_remove': "Susa",
        'merge_move_up': "Phezulu",
        'merge_move_down': "Phansi",
        'merge_pdfs_info': "💡 Ithiphu: Ungashintsha ukulandelana ngokuhudula nokuyeka",
        'merge_no_pdfs': "Ayikho i-PDF ekhethiwe. Chofoza ku-'Engeza i-PDF'.",
        'merge_info': "Ama-PDF angu-{0} akhethiwe (cishe amakhasi angu-{1})",
        'merge_open_file': "Vula ifayela",
        'merge_merge': "Hlanganisa",
        'merge_error': "Iphutha ngenkathi kuhlanganiswa",
        'merge_min_two_pdfs_error': "Sicela ukhethe okungenani amafayela amabili e-PDF ukuhlanganisa.",
        'merge_select_pdfs': "Khetha ama-PDF ozowahlanganisa",
        'merge_error_file': "Iphutha ngenkathi kucutshungulwa",
        'merge_cancelled': "Ukuhlanganisa kukhanseliwe",
        'merge_preparing': "Kulungiselela...",
        'merge_processing': "Kucutshungulwa i-PDF {0} kwezingu-{1}",
        'merge_saving': "Kugcinwa i-PDF ehlanganisiwe...",
        'merge_complete': "Kwenziwe!",
        'merge_success_title': "Ukuhlanganisa kuphumelele",
        'merge_success_voice': "Ama-PDF angu-{0} ahlanganiswe ngempumelelo.",
        'merge_success_message': "Ama-PDF angu-{0} ahlanganiswe ngempumelelo.\n\nIdokhumenti entsha manje inamakhasi angu-{1}.\n\nIfayela elisha:\n{2}\n\nIndawo yokugcina:\n{3}\n{2}\n\nIngabe ufuna ukuvula le PDF?",
        'replace_file_title': "Shintsha ifayela?",
        'replace_file_message': "I-PDF isivele ivuliwe. Ingabe ufuna ukuyishintsha ngefa elisha?",
        'btn_yes': "Yebo",
        'btn_no': "Cha",
        'filename_merge_suffix': "kuhlanganisiwe",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Kuvulwa {0}...",
        'progress_merge_reading': "Kufundwa {0}...",
        'progress_merge_adding': "Kungezwa amakhasi angu-{0}...",
        'progress_merge_optimizing': "Kwenziwa i-PDF ibe ngcono...",
        'progress_merge_writing': "Kubhalwa i-PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "ukuvala i-PDF",
        'action_close_window': "ukuvala iwindi",
        'action_open_new_pdf': "ukuvula i-PDF entsha",
        'action_quit_app': "ukuphuma ohlelweni",
        'changes_saved': "Izinguquko zigciniwe.",
        'file_close_title': "Vala ifayela le-PDF",
        'save_before_action': "Ingabe izinguquko kufanele zigcinwe ngaphambi kokuthi {0}? Yebo noma Cha?",
        'save_before_action_voice': "Ingabe izinguquko kufanele zigcinwe ngaphambi kokuthi {0}? Yebo noma Cha?",
        'save_before_close_question': "Ingabe izinguquko kufanele zigcinwe ngaphambi kokuvala? Yebo noma Cha?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>I-PDF engatholakala idalwe:\n\n{0}\n\n<b>Zama futhi uma kudingeka",
        "ocr_rotate_title": "Qondanisa amakhasi ngaphambi kwe-OCR",
        "ocr_rotate_question": "I-PDF inamakhasi azungezisiwe.\nIngabe ufuna ukuqondanisa wonke amakhasi ku-0° ngaphambi kwe-OCR?\nLokhu kuthuthukisa kakhulu ukubonwa kombhalo.",
        "ocr_rotate_yes": "Yebo, qondanisa",
        "ocr_rotate_no": "Cha, qala i-OCR ngqo",
        "ocr_rotate_voice": "I-PDF inamakhasi azungezisiwe. Ingabe wonke amakhasi kufanele aqondaniswe ngaphambi kwe-OCR?",
        "ocr_not_performed_message": "Ayikho imibhalo. Sicela wenze i-OCR (imenyu \"Hlela\" → \"Yenza i-OCR\" noma ukhiye Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Izilungiselelo ze-OCR",
        "ocr_language_btn": "Khetha ulimi lwe-OCR",
        "ocr_language": "Ulimi lwe-OCR",
        "ocr_language_current": "Ulimi lwamanje:",
        "ocr_param_info": "Ulwazi mayelana nepharamitha",

        "ocr_force_ocr_label": "Phoqa i-OCR",
        "ocr_deskew_label": "Lungisa ukutsheka",
        "ocr_clean_label": "Hlanza isithombe",
        "ocr_oversample_label": "Ukucaciswa (DPI)",
        "ocr_pagesegmode_label": "Ukuhlukaniswa kwekhasi",
        "ocr_oem_label": "Imodi yenjini ye-OCR",
        "ocr_optimize_label": "Ukucindezelwa kwe-PDF",
        "ocr_jobs_label": "Izinqubo ezihambisanayo",
        "ocr_verbose_label": "Imininingwane yelogi",

        "ocr_force_ocr_tooltip": "Phoqa i-OCR kulo lonke ikhasi, noma ngabe umbhalo usuvele ukhona",
        "ocr_deskew_tooltip": "Qondanisa ngokuzenzakalela izithwebuli ezitshekile",
        "ocr_clean_tooltip": "Susa umsindo nama-artifact esithombeni",
        "ocr_oversample_tooltip": "Khulisa isithombe ngaphambi kwe-OCR kule DPI",
        "ocr_pagesegmode_tooltip": "Kunquma ukuthi ikhasi lihlukaniswa kanjani izindawo zombhalo",
        "ocr_oem_tooltip": "Kukhetha injini ye-OCR ye-Tesseract",
        "ocr_optimize_tooltip": "Izinga lokucindezelwa kwe-PDF ephumayo",
        "ocr_jobs_tooltip": "Inani lezinqubo ze-OCR ezihambisanayo",
        "ocr_verbose_tooltip": "Izinga lemininingwane yokukhishwa kwelogi",
        "ocr_settings_explain_btn": "Incazelo",

        "ocr_force_ocr_explain": "Kuphoqa ukubonwa kombhalo kukho nelle khasi, noma ngabe selivele liqukethe umbhalo.\n\nIsincomo: <b>Vula</b> kuma-PDF askeniwe, <b>Vala</b> kuma-PDF endabuko anombhalo osekhona.",

        "ocr_deskew_explain": "Kulungisa izithwebuli ezitshekile kancane (kufika cishe ku-5°).\n\nIsincomo: <b>Vula</b> emibhalweni eskeniwe, <b>Vala</b> uma amakhasi eseqondile kahle.",

        "ocr_clean_explain": "Kususa umsindo, amachashazi kanye nama-artifact amancane esithombeni.\n<b>KUBALULEKILE:</b> Emibhalweni yesi-Arabhu, isi-Thai noma isi-Vietnamese enezimpawu ezi-diacritical (amachashazi ngaphezulu/ngaphansi kwezinhlamvu) le nketho kufanele <b>ingasebenzi</b>, ngaphandle kwalokho izinhlamvu ezibalulekile zingalahleka.",

        "ocr_oversample_explain": "Kukhulisa isithombe <b>ngaphambi</b> kokubonwa kombhalo kuye ku-DPI okukhishiwe.<br><br>• <b>72-150 DPI:</b> Kushesha kakhulu, kodwa izinga eliphansi lokubona<br>• <b>200-300 DPI:</b> Ububanzi obulungile (Okumisiwe: 300)<br>• <b>400+ DPI:</b> Akuboni kangcono, kodwa amafayela amakhulu kakhulu<br><br>Isincomo: 300 DPI ezibhalweni eziyinkimbinkimbi (isi-Arabhu, isiShayina, isiJapane), 200 DPI ezilimini zasentshonalanga.",

        "ocr_pagesegmode_explain": "Kunquma ukuthi i-Tesseract ihlukanisa kanjani ikhasi izindawo zombhalo.\n\n• <b>3 - Ngokuzenzakalela (Okumisiwe):</b> Kuhle ngezihlelo ezixubile\n• <b>4 - Ikholomu eyodwa:</b> Emibhalweni enekholomu eyodwa\n• <b>5 - Ibhulokhi eqondile:</b> Ezibhalweni eziqondile (isiJapane, isiShayina)\n• <b>6 - Ibhulokhi yombhalo efanayo:</b> Kulungile embhalweni ogelezayo ongenazikholomu\n• <b>11 - Isithombe esingahluziwe:</b> Eziphathweni ezingezinhle / okubhalwe ngesandla\n\nIsincomo: <b>6</b> emibhalweni elula, <b>3</b> ezihlelweni eziyinkimbinkimbi.",

        "ocr_oem_explain": "Kukhetha injini ye-OCR ye-Tesseract.\n\n• <b>0 - I-Legacy:</b> Injini endala (iyashesha, kodwa ayinembile kangako)\n• <b>1 - I-LSTM:</b> Injini ye-neural (iyahamba kancane, kodwa inembile kakhulu)\n• <b>2 - I-Legacy + LSTM ihlanganisiwe:</b> Ihlanganisa yomibili imiphumela\n• <b>3 - Okumisiwe (i-LSTM iyathandwa):</b> Inketho engcono kakhulu ezimweni eziningi\n\nIsincomo: <b>3</b> ukuze uthole ukunemba okuphezulu kokubona.",

        "ocr_optimize_explain": "Icindezela i-PDF ephumayo.\n\n• <b>0:</b> Akukho ukuthuthukiswa (ukucubungula okushesha kakhulu)\n• <b>1:</b> Ukuthuthukiswa okulula (ukuvumelana okuhle)\n• <b>2:</b> Ukuthuthukiswa okumaphakathi\n• <b>3:</b> Ukuthuthukiswa okuqinile (ifayela elincane kakhulu, kodwa lihamba kancane)\n\nIsincomo: <b>1</b> ekusetshenzisweni kwansuku zonke.",

        "ocr_jobs_explain": "Inani lezinqubo ezihambisanayo ze-OCR.\n\n• <b>1:</b> Kuyahamba kancane, kodwa ukusetshenziswa kwenkumbulo okuphansi kakhulu\n• <b>4-8:</b> Kulungile kuma-processor e-multi-core yesimanje\n• <b>12+:</b> Akusheshi kakhulu ngokusetshenziswa kwenkumbulo ephezulu\n\nIsincomo: Inani lama-core e-CPU (isb. <b>4</b> ezinhlelweni ezinama-core ama-4).",

        "ocr_verbose_explain": "Izinga lemininingwane yokukhishwa kwelogi kukhonsole.\n\n• <b>0:</b> Akukho okukhishwayo\n• <b>1:</b> Inqubekelaphambili nemiyalezo yesimo\n• <b>2:</b> Ukukhishwa okuningiliziwe\n• <b>3:</b> Ukukhishwa okuphelele kokulungisa amaphutha (kubanzi kakhulu)\n\nIsincomo: <b>1</b> ekusebenzeni okujwayelekile.",

        "ocr_reset_title": "Izilungiselelo zisethwe kabusha",
        "ocr_reset_message": "Zonke izilungiselelo ze-OCR zisethwe kabusha kumanani amisiwe.",
        "info_tooltip": "Ulwazi oluthe xaxa ngale pharamitha",
        "ocr_reset_defaults": "Setha kabusha kokumisiwe",

        "ocr_psm_0": "Ngokuzenzakalela (injini ye-Legacy)",
        "ocr_psm_1": "Ukutholwa kwekholomu ngokuzenzakalela",
        "ocr_psm_3": "Ngokuzenzakalela (Okumisiwe)",
        "ocr_psm_4": "Ikholomu eyodwa",
        "ocr_psm_5": "Ibhulokhi eqondile",
        "ocr_psm_6": "Ibhulokhi yombhalo efanayo",
        "ocr_psm_7": "Umugqa wombhalo owodwa",
        "ocr_psm_8": "Igama elilodwa",
        "ocr_psm_11": "Isithombe esingahluziwe (akukho ukuhlaziywa kwesakhiwo)",

        "ocr_oem_0": "Injini ye-Legacy (iyashesha)",
        "ocr_oem_1": "Injini ye-LSTM (i-neural, inembile)",
        "ocr_oem_2": "I-Legacy + LSTM ihlanganisiwe",
        "ocr_oem_3": "Okumisiwe (i-LSTM iyathandwa)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Ulimi lwe-OCR...",
        "ocr_language_title": "Khetha ulimi lwe-OCR",
        "ocr_language_instruction": "Khetha ulimi ukuze ubone umbhalo (OCR).\nIsixwayiso: Izilimi eziningi ziphazamisa ukusebenza nokunemba!\nUthola imiphumela engcono uma ukhetha ulimi olulodwa kuphela.",
        "ocr_language_predefined": "Izinhlanganisela ezichazwe ngaphambili",
        "ocr_language_custom": "Okwenziwe ngokwezifiso...",
        "ocr_language_selected": "Izilimi ze-OCR ezikhethiwe",
        "ocr_language_changed": "Ulimi lwe-OCR lushintshwe lwaba {0}",
        "ocr_language_auto_detect": "Izilimi ezitholakalayo zitholakala ngokuzenzakalela.",
        "ocr_language_none_found": "Ayikho idatha yolimi ye-Tesseract etholakele! Sicela ufake amaphakheji olimi (isb. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Ukukhetha ulimi ngokwezifiso",
        "ocr_language_available": "Izilimi ezitholakalayo (ezifakiwe):",
        "ocr_language_select_hint": "Khetha ulimi olulodwa noma eziningi:",
        "ocr_language_confirm": "Sebenzisa",
        "ocr_language_reset": "Setha kabusha kokumisiwe (deu+eng+vie)",
        "ocr_language_priorities": "Izilimi ezinconyiwe (ezifakwe kusengaphambili):",

        "select_all_languages": "Khetha konke",
        "clear_all_languages": "Sula ukukhetha",
        "install_language_packs": "Faka amaphakheji olimi angekho...",
        "install_hint": "💡 Ithiphu: Akuzona zonke izilimi ezifakiwe kusistimu yakho. Ngale nkinobho uzothola usizo lokufaka.",
        "ocr_language_install_title": "Ukufakwa kwamaphakheji olimi lwe-Tesseract",

        "ocr_missing_languages": "Amaphakheji olimi lwe-OCR angekho",
        "ocr_missing_languages_message": "Izilimi ezilandelayo ezikhethiwe azifakiwe kusistimu yakho:\n\n{0}\n\nSicela ufake amaphakheji olimi angekho (bheka usizo ngaphansi kosizo lokufaka).\n\nIngabe ufuna ukuvula usizo lokufaka manje?",
        "ocr_missing_languages_voice": "Amaphakheji olimi angekho. Sicela ufake izilimi ezingekho.",
        "ocr_install_help_now": "Vula usizo",
        "ocr_continue_anyway": "Zama noma kunjalo",
        "ocr_language_error_title": "Iphutha lolimi lwe-OCR",
        "ocr_language_error_message": "Iphutha ngesikhathi sokubona umbhalo: {0}\n\nSicela uhlole izilungiselelo zakho zolimi lwe-OCR (Izilungiselelo → Ulimi lwe-OCR).",
        "ocr_install_help_button": "Usizo lokufaka",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Faka amaphakheji olimi lwe-Tesseract</p>

        <p>Ukuze i-OCR isebenze ngolimi oluthile, idatha yolimi ehambisanayo kufanele ifakwe kusistimu yakho. Landela imiyalelo yohlelo lwakho lokusebenza:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Vula i-<strong>Terminal</strong> (Finder → Izinhlelo → Izinsiza → Terminal).</li>
        <li>Faka zonke izilimi ezitholakalayo nge:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Lokhu kungathatha imizuzu embalwa.)</li>
        <li>Noma izilimi ezithile kuphela (isb. isi-Vietnamese):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
>Ngezinguqulo zamanje ze-Homebrew, i-<code>*.traineddata</code> ingadinga ukulandwa ngesandla (bheka ngezansi).</li>
        <li>Ngemva kokufaka: Vala leli dilogovu bese uvula kabusha ukukhetha ulimi lwe-OCR – izilimi ezintsha zizovela ngokuzenzakalela.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Vula itheminali (Ctrl+Alt+T).</li>
        <li>Faka ulimi olufunayo, isb. isi-Vietnamese:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Amakhodi olimi abalulekile: <code>deu</code> (isiJalimane), <code>eng</code> (isiNgisi), <code>vie</code> (isi-Vietnamese), <code>spa</code> (isiSpeyini), <code>fra</code> (isiFulentshi), <code>ita</code> (isiNtaliyane), <code>nld</code> (isiDashi), <code>fin</code> (isiFinilandi), <code>swe</code> (isiSwidi), <code>nor</code> (isiNorweyi).</li>
        <li>Bonisa wonke amaphakheji atholakalayo:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ngesandla)</p>
        <ol>
        <li>Landa amafayela <code>*.traineddata</code> ofunayo kusuka:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (isb. <code>vie.traineddata</code> ngesi-Vietnamese).</li>
        <li>Kophela amafayela kufolda yolimi lwe-Tesseract, ngokuvamile:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Lungise ngokufaka ngakunye.)</li>
        <li>Qala kabusha uhlelo (noma uvule kabusha ukukhetha ulimi lwe-OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Okunye kuzo zonke izinhlelo</p>
        <ul>
        <li>Faka i-<strong>OCRmyPDF</strong> ne-<strong>Tesseract</strong> ngesiphathi sephakheji osikhethayo. Ukufakwa okuningi sekuvele kungezinye izilimi ezijwayelekile (isiNgisi, isiJalimane, isiFulentshi).</li>
        <li>Izilimi ezingekho zingafakwa noma nini – ukukhetha ulimi lwe-OCR kubala izilimi ezikhona kuphela.</li>
        </ul>

        <hr>
        <p><b>✅ Ngemva kokufaka:</b> Akudingeki uqale kabusha uhlelo – izilimi ezisanda kwengezwa zizovela ngokushesha ohlwini.</p>
        <p><b>📖 Usizo ngamakhodi olimi:</b> Uhlu oluphelele luyatholakala ku-<a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">imibhalo ye-Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Izinhlamvu ze-Noto Sans",
        "info_noto_font_voice": "Umhlahlandlela wokufaka izinhlamvu ze-Noto Sans",
        "btn_info_noto_font_install": "Ulwazi lwefonti",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Ungazifaka kanjani izinhlamvu ze-Noto zamahhala ezivela ku-Google</h2>

        <p><strong>Izinhlamvu ze-Noto</strong> ziwumndeni wezinhlamvu ezivulekile ezivela ku-Google. Umgomo wazo uwukungaboni <em>"i-tofu"</em> (okungukuthi, amabhokisi angenalutho □) nokubonisa ngokufanele wonke uhlamvu olusemazingeni e-Unicode. Ziyisengezo esihle ezinhlelweni ezidinga ukubonisa imibhalo ngezilimi eziningi ezahlukahlukene.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Ukufaka ku-macOS</h3>

        <p><strong>Indlela 1: Nge-Homebrew (yabasebenzisi abathuthukile)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Indlela 2: Nge-"Font Book" (Kuyanconywa)</strong></p>

        <ol>
        <li>Landa iphakheji yezinhlamvu esemthethweni:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Khipha ifayela le-ZIP</li>
        <li>Kophela amafayela ku-<code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Ukufaka ku-Windows (10 & 11)</h3>

        <p><strong>Indlela 1: I-Microsoft Store (Kuyanconywa)</strong><br>
        Sesha u-"Google Noto Fonts" noma "Noto Sans" bese uchofoza <strong>Faka</strong>.</p>

        <p><strong>Indlela 2: Ukufaka ngesandla</strong></p>

        <ol>
        <li>Landa:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Khipha i-ZIP</li>
        <li>Khetha amafayela .ttf / .otf</li>
        <li>Chofoza ngokunene → <strong>Faka</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        noma<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Igama\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Ukufaka ku-Linux</h3>

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

        <p>Ukuqinisekisa:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Phatha amabhukumaki",
        "bookmark_add": "Faka ibhukumaki",
        "bookmark_add_tooltip": "Gcina ikhasi lamanje njengebhukumaki",
        "bookmark_remove": "Susa ibhukumaki",
        "bookmark_remove_tooltip": "Susa ibhukumaki elimakiwe",
        "bookmark_remove_all": "Susa konke",
        "bookmark_remove_all_tooltip": "Susa wonke amabhukumaki ale PDF",
        "bookmark_jump": "Gijimela ebhukumakini",
        "bookmark_jump_tooltip": "Gijimela ekhathini elikhethiwe",
        "bookmark_name": "Igama",
        "bookmark_page": "Ikhasi",
        "bookmark_no_bookmarks": "Awekho amabhukumaki.\nChofoza 'Faka' ukugcina ikhasi lamanje njengebhukumaki.",
        "bookmark_added": "Ibhumaki lekhasi {0} lifakiwe: {1}",
        "bookmark_removed": "Ibhukumaki lisusiwe: {0}",
        "bookmark_all_removed": "Wonke amabhukumaki asusiwe.",
        "bookmark_name_default": "Ikhasi {0}",
        "bookmark_name_prompt": "Igama lebhukumaki:\n(umbhalo omude uzofushaniswa ube izinhlamvu ezingama-50)",
        "bookmark_name_prompt_title": "Igama lebhukumaki",
        "bookmark_confirm_remove_all": "Uqinisekile ukuthi ufuna ukususa wonke amabhukumaki angu-{0}?",
        "menu_bookmarks": "Amabhukumaki",
        "bookmark_manage": "Phatha amabhukumaki",
        "bookmark_next": "Ibhukumaki elilandelayo",
        "bookmark_prev": "Ibhukumaki eledlule",
        "bookmark_page_display": "Ikhasi {0}",
        "bookmark_exists": "Ibhukumaki laleli khasi negama elifanayo selivele likhona.",
        "bookmark_select_first": "Sicela ukhethe ibhukumaki kuqala.",
        "bookmark_confirm_remove": "Uqinisekile ukuthi ufuna ukususa ibhukumaki 'Ikhasi {0}: {1}'?",
        "bookmark_jumped_to": "Kugijinyelwe ebhukumakini '{0}' ekhathini {1}.",
        "bookmark_jumped_to_voice": "Ibhukumaki {0}, ikhasi {1}",
        "btn_close": "Vala",

        "bookmark_list": "Amabhukumaki akho",
        "bookmark_rename": "Qamba kabusha ibhukumaki",
        "bookmark_rename_tooltip": "Shintsha igama lebhukumaki elikhethiwe",
        "bookmark_rename_title": "Qamba kabusha ibhukumaki",
        "bookmark_rename_prompt": "Igama elisha lebhukumaki ekhathini {0}:\n(izinhlamvu ezingama-50 ubuningi)",
        "bookmark_renamed": "Ibhukumaki '{0}' liqanjwe kabusha laba '{1}'.",
        "bookmark_item_tooltip": "Ikhasi {0}: {1}\nChofoza kabili ukuze ugijime",
        "bookmark_name_exists_question": "Ibhukumaki elinegama elithi '{0}' selivele likhona kuleli khasi.\ngijime Noma kunjalo?",

        "context_bookmarks": "Amabhukumaki",
        "context_bookmark_add_here": "Faka ibhukumaki laleli khasi",
        "context_bookmarks_existing": "Amabhukumaki akhona:",
        "context_bookmarks_jump": "Gijimela ebhukumakini:",
        "context_bookmarks_none": "Awekho amabhukumaki",
        "context_bookmarks_clear_all": "Susa wonke amabhukumaki angu-{0}",

        "bookmark_search_placeholder": "Sesha amabhukumaki... (igama noma ikhasi)",
        "bookmark_search_results": "Kutholakale amabhukumaki angu-%d ku \"%s\"",
        "bookmark_no_search_results": "Awekho amabhukumaki atholakele ku \"%s\"",
        "bookmark_no_search_results_label": "Ayikho imiphumela ku \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Hlela imethadatha ye-PDF",
        "metadata_title": "Isihloko",
        "metadata_title_placeholder": "Isihloko sombhalo",
        "metadata_title_tooltip": "Isihloko sombhalo (siboniswa kubha yesihloko)",
        "metadata_author": "Umlobi",
        "metadata_author_placeholder": "Igama lomlobi",
        "metadata_author_tooltip": "Umdali wombhalo",
        "metadata_subject": "Isihloko",
        "metadata_subject_placeholder": "Isihloko sombhalo",
        "metadata_subject_tooltip": "Incazelo emfushane yokuqukethwe",
        "metadata_keywords": "Amagama asemqoka",
        "metadata_keywords_placeholder": "Amagama asemqoka ahlukaniswe ngokoma",
        "metadata_keywords_tooltip": "Amagama asemqoka wokuhlela umbhalo",
        "metadata_creator": "Umdali",
        "metadata_creator_placeholder": "Uhlelo oludale i-PDF",
        "metadata_creator_tooltip": "Isoftware okudalwe ngayo umbhalo",
        "metadata_producer": "Umkhiqizi",
        "metadata_producer_placeholder": "Uhlelo oluguqule i-PDF",
        "metadata_producer_tooltip": "Isoftware eguqule i-PDF",
        "metadata_creation_date": "Usuku lokudalwa",
        "metadata_creation_date_tooltip": "Usuku lombhalo owadalwa ngalo",
        "metadata_mod_date": "Usuku lokuguqulwa",
        "metadata_mod_date_tooltip": "Usuku lokugcina lokuguqulwa",
        "metadata_pdf_info": "📄 Ulwazi lwe-PDF",
        "metadata_pages": "Inani lamakhasi",
        "metadata_file_size": "Usayizi wefayela",
        "metadata_pdf_version": "Inguqulo ye-PDF",
        "metadata_encrypted": "Kubethelwe",
        "metadata_encrypted_yes": "Yebo (kuvikelwe ngephasiwedi)",
        "metadata_encrypted_no": "Cha",
        "metadata_reload": "📂 Layisha kabusha kusuka ku-PDF",
        "metadata_reset": "Lahla izinguquko",
        "metadata_reloaded": "Imethadatha iphinde yalayishwa kusuka ku-PDF.",
        "metadata_reset_done": "Zonke izinkambu zemethadatha zisethwe kabusha.",
        "metadata_no_file": "Ayikho ifayela le-PDF elilayishiwe.",
        "metadata_save_error": "Iphutha ekugcineni imethadatha",
        "metadata_saved": "Imethadatha igcinwe ngempumelelo.",
        "metadata_pdf_version_unknown": "PDF (akukaziwa)",
        "metadata_saved_message": "Imethadatha igcinwe ngempumelelo.",
        "metadata_saved_voice": "Imethadatha igciniwe.",

        "metadata_custom": "🔧 Imethadatha eyenziwe ngokwezifiso",
        "metadata_custom_placeholder": "{\n  \"inkambu_yami\": \"inani_lami\",\n  \"enye_inkambu\": 123\n}",
        "metadata_custom_tooltip": "Ifomethi ye-JSON yemethadatha eyenziwe ngokwezifiso (ongakukhetha)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Isifanekiso \"{0}\" sikhethiwe - Chofoza kabili ukufaka",
        "text_use_template": "Sebenzisa ibhulokhi yombhalo",
        "text_type": "Uhlobo",
        "text_search_templates": "Sesha amabhulokhi ombhalo...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Ulwazi lokukhipha / ukungenisa",
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

        <h3>📦 Yini ekhiphayo? (Umbono jikelele)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Izilungiselelo ezijwayelekile zohlelo</span></li>
            <li class="detail">• Imodi emnyama/ekhanyayo</li>
            <li class="detail">• Ukuguqulwa kwemodi emnyama yezithombe</li>
            <li class="detail">• Inani lomkhawulo wempunga</li>
            <li class="detail">• Ulimi</li>
            <li class="detail">• Ijiyomethri yewindi</li>
            <li class="detail">• Imodi yokusondeza</li>
            <li class="detail">• Ukuzulazula (Ibha yokuzulazula iyabonakala)</li>
            <li class="detail">• Ukukhishwa kwenkulumo (kuvuliwe/kucishiwe)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Izilungiselelo zesipele</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Ukuqanjwa kwamafayela (Isitembu sesikhathi, Isihlukanisi, Izejwayele)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Izilungiselelo zokufakwa kwe</span></li>
            <li class="detail">• Amasiginesha</li>
            <li class="detail">• Umbhalo namabhulokhi ombhalo</li>
            <li class="detail">• Izimpawu zokumaka, izithombe nezimo</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Izilungiselelo ze-OCR</span></li>
            <li class="detail">• Ulimi</li>
            <li class="detail">• Phoqa i-OCR · Imodi yekhasi</li>
            <li class="detail">• Ukucubungula isithombe kusengaphambili: Lungisa ukutsheka, Hlanza, Ukusampula ngokweqile</li>
            <li class="detail">• Inani lemisebenzi ehambisanayo</li>
            <li class="detail">• Imodi yokuguqula</li>
            <li class="detail">• Inani lomkhawulo wempunga</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Amabhukumaki</span></li>
            <li class="detail">• Wonke amabhukumaki ngefayela ngalinye le-PDF (Ikhasi, Igama, Isikhathi sokudalwa)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Isizindalwazi samaphasiwedi</span></li>
            <li class="detail">• Amaphasiwedi e-PDF agciniwe (abhethelwe noma umbhalo ocacile ngokukhetha)</li>
            <li class="detail">• I-hashi yephasiwedi eyinhloko (uma isetiwe)</li>
            <li class="detail">• Idatha yokuqinisekisa</li>
        </ul>

        <h4>⚠️ Amanothi abalulekile</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Lapho ungenisa:</strong>
            <ul>
                <li><span class="warning">➜ Zonke izilungiselelo zamanje zizobhalwa ngaphezulu ngokuphelele</span></li>
                <li>• Ukuqala kabusha kohlelo kuyisibopho</li>
                <li>• Amasiginesha akhona, amabhulokhi ombhalo namabhukumaki azothathelwa indawo</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Iphasiwedi eyinhloko nemodi yokukhipha:</strong>
            <ul>
                <li>• Lapho iphasiwedi eyinhloko isebenza, ungakhetha:</li>
                <li>  - <span style="color: #98FB98;"><strong>Okubethelwe okusuliwe</strong></span> (amaphasiwedi asemibhalweni ecacile ku-ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Okubethelwe</strong></span> (kufundeka kuphela ngephasiwedi eyinhloko kusistimu okuhlosiwe)</li>
                <li>• I-hashi yephasiwedi eyinhloko <strong>ihlale</strong> igcinwe ibethelwe</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Isaziso sokuphepha:</strong>
            <ul>
                <li>• Ifayela le-ZIP elikhiphiwe liqukethe idatha ebucayi (<strong>amaphasiwedi, amabhukumaki, amasiginesha</strong>)</li>
                <li>• Sicela uligcine ngokuphephile (isb. i-USB stick ebetheliwe, isiphathi samaphasiwedi)</li>
                <li>• Uma ifayela ulahleka, amaphasiwedi e-PDF agciniwe alahleka ngokungaphenduki</li>
            </ul>
        </div>

        <h4>📁 Ifomethi yokukhipha</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Izilungiselelo zigcinwa kufayela elilodwa le-ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Le ZIP iqukethe i-<code>settings.json</code> ephelele (kusuka ekucushweni kwakho) kanye namafayela wezithombe zesiginesha ashumekiwe namaphasiwedi abethelwe.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Amasiginesi - Umhlahlandlela",
        'signature_guide_html': """
        📝 <strong>Amasiginesi - Umhlahlandlela osheshayo</strong><br>
        <ul>
        <li>Misa iphasiwedi eyinhloko</li>
        <li>Lungiselela amasiginesi kumenyu <em>Izilungiselelo</em> (usayizi, isitembu sesikhathi, …)</li>
        <li>Faka nge <strong>UKUCHOFYA KWESOKUDLA</strong> endaweni oyifunayo (iphasiwedi eyinhloko iyadingeka kanye ngeseshini)</li>
        <li>Hambisa isiginesi ngegundane noma izinkinobho zomcibisholo</li>
        <li>Faka amasiginesi amaningi ngokulandelana</li>
        <li>Yenza isiginesi ngasinye ngokwakho</li>
        <li>Lahla isiginesi eyodwa</li>
        <li>Gcina / lahla wonke amasiginesi ngasikhathi sinye</li>
        <li>Okunye, ungasebenzisa nebha yemenyu.</li>
        </ul>
        """,
        'signature_guide_voice': "Umhlahlandlela osheshayo wamasiginesi. Misa iphasiwedi eyinhloko. Lungiselela amasiginesi ezilungiselelweni. Faka ngokuchofya kwesokudla.",

        'image_guide_title': "Ukufaka izithombe - Umhlahlandlela",
        'image_guide_html': """
        📷 <strong>Ukufaka izithombe ku-PDF - Umhlahlandlela osheshayo</strong><br>
        <ol>
        <li>Chofya kwesokudla endaweni oyifunayo</li>
        <li><em>„Faka isithombe“</em> → Khetha isithombe</li>
        <li>Beka isithombe: Hudula ngegundane</li>
        <li>Lungisa usayizi: Hudula emakhoneni/emaphethelweni</li>
        <li>Gcina isilinganiso sezinhlangothi: Ukhiye <strong>[A]</strong></li>
        <li>Okunye ukulungisa: Chofya kwesokudla esithombeni</li>
        </ol>
        <p><strong>Ithiphu:</strong> Kumenyu yomongo ungakwazi ukulungisa izilungiselelo.</p>
        """,
        'image_guide_voice': "Umhlahlandlela osheshayo wezithombe. Chofya kwesokudla, faka isithombe, khetha. Beka ngegundane, lungisa usayizi emakhoneni. Isilinganiso ngekhiye A.",

        'form_guide_title': "Ukufaka izimo - Umhlahlandlela",
        'form_guide_html': """
        📐 <strong>Ukufaka izimo ku-PDF - Umhlahlandlela osheshayo</strong><br>
        <ol>
        <li>Khetha uhlobo lwesimo (unxande, indilinga, umugqa, umcibisholo)</li>
        <li>Chofya endaweni:
            <ul>
            <li>Kunxande/indilinga: Ukuchofya okukodwa kubeka isimo</li>
            <li>Kumugqa/umcibisholo: Ukuchofya okubili kwephoyinti lokuqala nelokugcina</li>
            </ul>
        </li>
        <li>Beka isimo: Hudula ngegundane</li>
        <li>Lungisa usayizi: Hudula emakhoneni/emaphethelweni</li>
        <li>Gcina isimo: <strong>Enter</strong></li>
        <li>Lahla isimo: <strong>ESC</strong></li>
        <li>Okunye ukulungisa: Chofya kwesokudla esimweni</li>
        </ol>
        <p><strong>Ithiphu:</strong> Kumenyu yomongo ungakwazi ukulungisa izilungiselelo.</p>
        """,
        'form_guide_voice': "Umhlahlandlela osheshayo wezimo. Khetha uhlobo lwesimo. Kunxande noma indilinga chofya kanye, kumugqa noma umcibisholo chofya kabili. Beka ngegundane, lungisa usayizi emakhoneni. Gcina nge-Enter, lahla nge-Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "eyandulele",
        "btn_next_result": "elandelayo",
        "ocr_text_window": "Iwindi lombhalo we-OCR",
        "bookmark_existing": "Amabhukhimaki akhona",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Ukuqhathanisa kwe-OCR Mac - Windows",
        'ocr_method_mac_win_title': "Umehluko we-OCR phakathi kwe-Mac ne-Windows",
        'ocr_method_mac_win_voice': "I-Mac ingcono",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Umehluko phakathi kwe-macOS ne-Windows</strong></p>

        <p><strong>macOS (iyatuswa)</strong></p>
        <p>Ithuluzi:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Umphumela:</p>
        <ul>
        <li>I-PDF eseshekwayo enombhalo oshumekiwe ogcina kakhulu ukwakheka kwasekuqaleni.</li>
        </ul>
        <p>Izinzuzo:</p>
        <ul>
        <li>Ikhwalithi enhle kakhulu yokubona umbhalo (noma emakhasini agwegwile).</li>
        <li>Ukugcinwa kwemidwebo ye-vector nezinhlamvu zamagama.</li>
        <li>Ibha yenqubekelaphambili ye-GUI ngokuhlolwa kwenqubo engaphansi.</li>
        <li>Ukulawula okuphelele kuyo yonke imingcele ye-OCR (Deskew, Clean, Oversample, ukwenziwa ngcono).</li>
        <li>Ukusesha kombhalo kutholakala ngqo ewindini eliyinhloko (ukubuka kwe-PDF).</li>
        </ul>
        <p>Izingozi:</p>
        <ul>
        <li>Idinga amathuluzi engeziwe ohlelo (ocrmypdf, Ghostscript, unpaper, pngquant – kufakiwe ku-App Bundle).</li>
        <li>Ukuphathwa kwamaphutha okuyinkimbinkimbi (ama-deadlock, ama-timeout).</li>
        </ul>

        <p><strong>Windows (okunye okuzinzile)</strong></p>
        <p>Ithuluzi:</p>
        <ul>
        <li>pytesseract (ukuxhumana okuqondile ne-Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Umphumela:</p>
        <ul>
        <li>I-PDF eseshekwayo ebonakalayo ihambisana ne-PDF yesithombe, kodwa iyasesheka ngombhalo osobala.</li>
        </ul>
        <p>Izinzuzo:</p>
        <ul>
        <li>Ayikho engingayicabanga njengamanje.</li>
        </ul>
        <p>Izingozi:</p>
        <ul>
        <li>I-PDF iyisithombe esinombhalo ongabonakali; ukwakheka kungahle kwehluke kancane kumadokhumenti ayinkimbinkimbi (amakholomu, amathebula).</li>
        <li>Akukho ukulungiswa kokutshekeka okuzenzakalelayo (--deskew) noma ukuhlanza isithombe (--clean).</li>
        <li>Ibha yenqubekelaphambili ye-GUI ivuselelwa kuphela ngokulinganisela ngokusekelwe enanini lamakhasi acutshunguliwe.</li>
        <li>Isivinini se-OCR sihamba kancane (ngoba ikhasi ngalinye licutshungulwa ngokwahlukana).</li>
        <li>Ukusesha kombhalo kuqondiswa kabusha ewindini lombhalo le-OCR.</li>
        </ul>

        <p><strong>Izinto ezifanayo</strong></p>
        <ul>
        <li>Zombili izindlela zidala i-PDF eseshekwayo kunkomba efanayo nefayela lomthombo.</li>
        <li>Izilungiselelo ze-OCR (ulimi, i-DPI, imodi yokuhlukanisa ikhasi, imodi yenjini ye-OCR) zingalungiselelwa nge-OCRSettingsDialog futhi ziyasebenza kuzo zombili izinhlobo zokusebenza.</li>
        </ul>

        <p><strong>Isincomo:</strong></p>
        <ul>
        <li>macOS: I-ocrmypdf binary inikeza imiphumela engcono kakhulu – Thenga i-Mac futhi usebenzise inguqulo (i-PDFDarkView yama-Mac ane-Apple Silicon noma i-Intel chip). Imiphumela ye-OCR ingcono kunangaphansi kwe-Windows!</li>
        <li>Windows: Sebenzisa isixazululo se-pytesseract. Izinzile futhi inikeza ikhwalithi eyanele ngokuphelele emadokhumenti amaningi.</li>
        </ul>

        <p><strong>Inothi elibalulekile:</strong></p>
        <ul>
        <li>Zombili izinguqulo zihlanganiswe ngokuphelele kusixhumi esibonakalayo somsebenzisi – umsebenzisi akaboni mehluko.</li>
        <li>Uhlelo lunquma ngokuzenzakalelayo ukuthi iyiphi injini ye-OCR ezosetshenziswa ngokusekelwe ohlelweni olusebenzayo.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Dala isiginesi (kusukela kuskeni)",
        "signature_create_title": "Khetha isiginesi eskeniwe (PDF/isithombe)",
        "image_pdf_filter": "Izithombe ne-PDF",
        "signature_pdf_empty": "I-PDF ayinakho amakhasi.",
        "signature_created_success": "Isiginesi idalwe ngempumelelo: {0}",
        "signature_create_error": "Iphutha ngenkathi kudalwa isiginesi:\n{0}",
        "rembg_missing": "i-rembg ayifakiwe.\nSicela uyifake: pip install rembg\nIphutha: {0}",
        "signature_name_title": "Igama lefayela lesiginesi",
        "signature_name_message": "Sicela ufake igama lefayela lesiginesi entsha (izogcinwa njenge-PNG enengemuva elibushelelezi):",
        "signature_name_label": "Igama lefayela:",
        "signature_name_voice": "Faka igama lefayela lesiginesi",
        "signature_processing": "Kucutshungulwa...",
        "signature_creation_title": "Isiginesi iyadalwa",
        "signature_overwrite_warning": "Ifayela '{0}' selivele likhona. Ngabe liyabhaliwana?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Lungiselela i-PDF yesiginesi",
        "signature_prepare_instruction":"Sicela ukhethe i-PDF equkethe ekhasini elilodwa isiginesi eskeniwe.\n\nUkuze uthole ukuqashelwa okuhle kakhulu, qiniseka ukuthi:\n• Isiginesi ibhalwe ngoyinki omnyama (ipeni lebhola noma i-fineliner) ephepheni elimhlophe.\n• Isiginesi isengxenyeni yesithathu engaphezulu yekhasi le-A4 elingenalutho.\n• I-PDF iskenwe okungenani ngo-300 dpi.\n• Isiginesi icacile futhi ayizacile kakhulu.\n• Ayikho amaphethini angemuva aphazamisayo noma imigqa.",
        "signature_prepare_voice":"Sicela ukhethe i-PDF enesiginesi eskeniwe. Nakana ikhwalithi enhle nokugqama.",
        "sig_thickness_label":"Ubukhulu bomugqa:",
        "sig_thickness_normal":"Okujwayelekile (okuzacile)",
        "sig_thickness_bold":"Okugqamile (okutuswayo)",
        "sig_thickness_very_bold":"Okugqamile kakhulu",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Engeza izilimi ze-GUI ne-OCR - Umhlahlandlela",
        'language_guide_title': "Engeza izilimi ze-GUI ne-OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Landa ifayela lokuhumusha olifunayo <code>translations_xy.py</code> kusuka<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        futhi ulifake kunkomba elandelayo:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Vula isiphequluli sakho sewebhu.</li>
        <li>Iya ku: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Phezu komphetho wesokudla sesikrini, thola "Releases" bese ukhetha lokhu okumakwe <strong>"latest"</strong>.</li>
        <li>Ekhasi elilandelayo lokukhishwa, landa ifayela <code>Source Code.zip</code> ngezansi kakhulu.</li>
        <li>Khipha i-ZIP ifayela.</li>
        <li>Kufolda okhishiwe, thola wonke amafayela olimi owadingayo, bese uwakopisha kunkomba:<br/>
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
        "menu_watermark":"Faka uphawu lwamanzi",
        "fullpage_text_watermark_title":"Umbhalo njengophawu lwamanzi",
        "fullpage_image_watermark_title":"Isithombe njengophawu lwamanzi",
        "filename_with_watermark":"_nophawu_lwamanzi",
        "watermark_text":"Umbhalo:",
        "watermark_text_placeholder":"Umbhalo wakho wophawu lwamanzi...",
        "watermark_font_family":"Ifonti:",
        "watermark_font_size":"Usayizi wefonti:",
        "watermark_format":"Ukufomatha:",
        "watermark_bold":"Okuqinile",
        "watermark_italic":"Okutshekile",
        "watermark_color":"Umbala:",
        "watermark_choose_color":"Khetha umbala...",
        "watermark_opacity":"Ukungafihli / Ukufihli:",
        "watermark_direction":"Inkomba yokufunda:",
        "watermark_direction_l_r":"Kunxele → Kwesokudla",
        "watermark_direction_bl_tr":"Phansi kwesokunxele → Phezulu kwesokudla",
        "watermark_direction_tl_br":"Phezulu kwesokunxele → Phansi",
        "watermark_direction_b_t":"Phansi → Phezulu",
        "watermark_direction_t_b":"Phezulu → Phansi",
        "watermark_preview":"Ukubuka kuqala:",
        "watermark_preview_sample":"Umbhalo oyisibonelo",
        "watermark_empty_text":"Sicela ufake umbhalo.",
        "watermark_applied":"Uphawu lwamanzi lusetshenziswe kuwo wonke amakhasi.",
        "watermark_saved":"Uphawu lwamanzi lulondoloziwe.",
        "image_scale":"Usayizi:",
        "image_preview":"Ukubuka isithombe kuqala:",
        "no_image_selected":"Asikho isithombe esikhethiwe",
        "browse":"Phenya...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Izindaba ezifihliwe",
        "redact_add_black": "Ukufihla (okumnyama)",
        "redact_add_white": "Ukufihla (okumhlophe / susa)",
        "redact_added_black": "Ukufihla okumnyama kwengeziwe",
        "redact_added_white": "Ukufihla okumhlophe kwengeziwe",
        "redact_apply_all": "Sebenzisa konke ukufihla bese ulondoloza",
        "redact_discard_all": "Yeka konke ukufihla",
        "redact_discard": "Yeka lokhu kufihla",
        "no_redactions": "Akukho ukufihla",
        "redact_confirm_title": "Sebenzisa ukufihla ngokuphelele",
        "redact_confirm_message": "Isixwayiso: Izindawo eziphawuliwe zizosuswa ngokuphelele (okumnyama noma okumhlophe).\nKuzokwenziwa isipele (uma kuvuliwe).\n\nQhubeka?",
        "redact_apply": "Yebo, fihla manje",
        "redact_saved": "Ukufihla okungu-{0} kusetshenzisiwe futhi kwalondolozwa ngempumelelo.",
        "redact_saved_voice": "Ukufihla okungu-{0} kusetshenzisiwe",
        "redact_error": "Iphutha ngesikhathi sokufihla",
        "filename_redacted":"_kufihliwe",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Faka izinombolo zamakhasi',
        'page_numbers_format': 'Ifomethi yezinombolo:',
        'page_numbers_format_arabic': '1, 2, 3 ... (isi-Arabhu)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (isi-Romani encane)',
        'page_numbers_format_roman_upper': 'I, II, III ... (isi-Romani enkulu)',
        'page_numbers_format_letter': 'A, B, C ... (Izinhlamvu)',
        'page_numbers_format_custom': 'Okwenziwe ngokwezifiso',
        'page_numbers_custom_pattern': 'Iphethini:',
        'page_numbers_custom_placeholder': 'isb. "Ikhasi {nummer}" noma "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Sebenzisa {nummer} kunombolo yekhasi lamanje kanye {total} enanini eliphelele',
        'page_numbers_position': 'Indawo:',
        'page_numbers_pos_tl': 'Phezulu kwesokunxele',
        'page_numbers_pos_tc': 'Phezulu maphakathi',
        'page_numbers_pos_tr': 'Phezulu kwesokudla',
        'page_numbers_pos_ml': 'Maphakathi kwesokunxele',
        'page_numbers_pos_mc': 'Maphakathi',
        'page_numbers_pos_mr': 'Maphakathi kwesokudla',
        'page_numbers_pos_bl': 'Phansi kwesokunxele',
        'page_numbers_pos_bc': 'Phansi maphakathi',
        'page_numbers_pos_br': 'Phansi kwesokudla',
        'page_numbers_margins': 'Imingcele:',
        'page_numbers_margin_x': 'Ibanga elivundlile:',
        'page_numbers_margin_y': 'Ibanga eliqondile:',
        'page_numbers_range': 'Ububanzi bamakhasi:',
        'page_numbers_all_pages': 'Wonke amakhasi',
        'page_numbers_custom_range': 'Ububanzi obwenziwe ngokwezifiso',
        'page_numbers_from': 'Kusuka:',
        'page_numbers_to': 'Kuya:',
        'page_numbers_progress': 'Kufakwa izinombolo zamakhasi...',
        'page_numbers_start': 'Kuqalwa ukufakwa kwezinombolo zamakhasi...',
        'page_numbers_cancel': 'Ukufakwa kwezinombolo zamakhasi kukhanseliwe',
        'page_numbers_success': 'Izinombolo zamakhasi zengezwe ngempumelelo.\n\nIngabe ufuna ukuvula i-PDF entsha?\n\n{0}',
        'page_numbers_complete': 'Izinombolo zamakhasi zengeziwe',
        'page_numbers_error_format': 'Iphutha ngesikhathi sokufaka izinombolo zamakhasi: {0}',
        'page_numbers_content_type': 'Uhlobo lokuqukethwe:',
        'page_numbers_tab_simple': 'Inombolo elula',
        'page_numbers_tab_range': 'Ikhasi X kwe-Y',
        'page_numbers_tab_date': 'Usuku',
        'page_numbers_tab_custom': 'Umbhalo okhululekile',
        'page_numbers_range_format': 'Ifomethi:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Ikhasi {aktuell} kwe-{gesamt}',
        'page_numbers_range_custom': 'Okwenziwe ngokwezifiso',
        'page_numbers_range_placeholder': 'isb. "Ikhasi {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Ifomethi yosuku:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 Januwari 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Okwenziwe ngokwezifiso',
        'page_numbers_date_placeholder': 'isb. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Indawo:',
        'page_numbers_date_before': 'Usuku ngaphambi kwenombolo yekhasi',
        'page_numbers_date_after': 'Usuku ngemuva kwenombolo yekhasi',
        'page_numbers_date_only': 'Usuku kuphela (ngaphandle kwenombolo yekhasi)',
        'page_numbers_custom_text': 'Umbhalo owenziwe ngokwezifiso:',
        'page_numbers_custom_placeholder_text': 'Sebenzisa {seite} kunombolo yekhasi kanye {gesamt} enanini eliphelele\nisb. "Okuyimfihlo - Ikhasi {seite}" noma "{seite} kwe-{gesamt}"',
        "filename_with_page_number":"_nenombolo_yekhasi",
        "filename_with_page_declaration":"_nesimemezelo_sekhasi",
        "filename_with_pagenumber":"_nenombolo_yekhasi",
        "filename_with_date":"_nosuku",
        "filename_with_my_page_declaration":"_nesimemezelo_sekhasi_esenziwe_ngokwezifiso",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Izinguquko ezingalondoloziwe",
        "unsaved_changes_message_darkmode": "Kukhona ukufakwa okungalondoloziwe.\nIngabe ufuna ukukulondoloza ngaphambi kokushintsha?",
        "save_and_switch": "Londoloza bese ushintsha",
        "discard_and_switch": "Shintsha manje",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Thengisa amakhasi njengezithombe',
        'export_images_menu': 'Thengisa njengezithombe (PNG/JPEG)',
        'export_images_format': 'Ifomethi yesithombe:',
        'export_images_dpi': 'Ukucaca (DPI):',
        'export_images_quality': 'Ikhwalithi ye-JPEG:',
        'export_images_range': 'Ububanzi bamakhasi:',
        'export_images_all_pages': 'Wonke amakhasi',
        'export_images_custom_range': 'Ububanzi obwenziwe ngokwezifiso',
        'export_images_from': 'Kusuka:',
        'export_images_to': 'Kuya:',
        'export_images_options': 'Izinketho:',
        'export_images_single_files': 'Ikhasi ngalinye njengefayela elihlukile',
        'export_images_subfolder': 'Thengisa kufolda engaphansi',
        'export_images_subfolder_info': 'Kufolda engaphansi "igamaPDF_izithombe"',
        'export_images_same_folder': 'Kufolda efanayo ne-PDF',
        'export_images_apply_darkmode': 'Sebenzisa izilungiselelo ze-PDFDarkView (Imodi Emnyama)',
        'export_images_target_folder': 'Ifolda okuyiwa kuyo:',
        'export_images_browse': 'Phenya...',
        'export_images_preview': 'Ukubuka kuqala:',
        'export_images_preview_info': 'Khetha izilungiselelo zokuthengisa',
        'export_images_preview_info_detail': 'Amakhasi angu-{0} njenge-{1}\nUkucaca: {2} DPI\nIgama lefayela: {3}\n{4}',
        'export_images_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'export_images_start': 'Kuqalwa ukuthengiswa kwezithombe...',
        'export_images_progress': 'Kuthengiswa izithombe...',
        'export_images_saving': 'Kulondolozwa ikhasi {0} kwe-{1}...',
        'export_images_success': 'Ukuthengisa kuphumelele!\n\nIzithombe ezingu-{0} zilondolozwe ku:\n{1}',
        'export_images_complete': 'Ukuthengiswa kwezithombe sekuqediwe',
        'export_images_open_folder': '📁 Vula ifolda',
        'export_images_cancel': 'Ukuthengiswa kwezithombe kukhanseliwe',
        'export_images_error_format': 'Iphutha ngesikhathi sokuthengisa izithombe: {0}',
        'export_images_pdf2image_missing': 'Umtapo wolwazi "pdf2image" awufakiwe.\n\nSicela uwufake ngalokhu:\npip install pdf2image\n\nKuma-Windows udinga i-Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Ukuguqulwa kwe-PDF/A kokugcinwa isikhathi eside',
        'pdfa_menu': 'Ukuguqulwa kwe-PDF/A (kulungele ukugcinwa)',
        'pdfa_info': 'Iguqula i-PDF ibe yifomethi ye-PDF/A.\n\nI-PDF/A iklanyelwe ngokukhethekile ukugcinwa isikhathi eside futhi iqinisekisa ukuthi idokhumenti izoboniswa kahle esikhathini esizayo.',
        'pdfa_standard': 'Izinga le-PDF/A:',
        'pdfa_standard_select': 'Inguqulo:',
        'pdfa_1': 'PDF/A-1 (elula, ehambelana kabanzi)',
        'pdfa_2': 'PDF/A-2 (yesimanje, ukucindezela okungcono)',
        'pdfa_3': 'PDF/A-3 (inguqulo yakamuva, ivumela okunamathiselwe)',
        'pdfa_standards_explanation': '📖 Incazelo yamazinga:\n\n'
            '• PDF/A-1: Eyisisekelo, ehambelana nezinhlelo ezindala (cishe 2005)\n'
            '• PDF/A-2: Yesimanje, ukucindezela okungcono, ukwesekwa kokufihli (cishe 2011)\n'
            '• PDF/A-3: Inguqulo yakamuva, ivumela ukufakwa kokunamathiselwe (cishe 2013)\n\n'
            'Isincomo: I-PDF/A-2 iyisivumelwano esihle phakathi kokuhambelana nezici zesimanje.',
        'pdfa_options': 'Izinketho:',
        'pdfa_compress_enable': 'Cindezela i-PDF (ifayela elincane)',
        'pdfa_metadata_preserve': 'Gcina imethadatha (isihloko, umbhali, njll.)',
        'pdfa_target_folder': 'Ifolda okuyiwa kuyo:',
        'pdfa_browse': 'Phenya...',
        'pdfa_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'pdfa_ocr_info_unknown': '🔍 Ayikwazanga ukuhlola okuqukethwe kombhalo.',
        'pdfa_ocr_info_not_needed': '✅ Umbhalo uyatholakala - i-OCR ayidingeki.\nI-PDF/A ingakhiwa ngqo.',
        'pdfa_ocr_info_recommended': '⚠️ Umbhalo onele awutholakalanga.\n\nKuma-PDF angaseshwa, sincoma ukuthi uqale usebenzise i-OCR.\nQaphela: I-PDF/A iyasebenza ngaphandle kwe-OCR - kodwa umbhalo ngeke usesheke.',
        'pdfa_ocr_info_error': '❌ Iphutha ngesikhathi sokuhlola: {0}',
        'pdfa_start': 'Kuqalwa ukuguqulwa kwe-PDF/A...',
        'pdfa_progress': 'Ukuguqulwa kwe-PDF/A kuyaqhubeka...',
        'pdfa_success': 'Ukuguqulwa kwe-PDF/A kuphumelele!\n\nKulondolozwe njenge:\n{0}\n\nIngabe ufuna ukuvula i-PDF entsha?',
        'pdfa_complete': 'Ukuguqulwa kwe-PDF/A sekuqediwe',
        'pdfa_cancel': 'Ukuguqulwa kwe-PDF/A kukhanseliwe',
        'pdfa_error_format': 'Iphutha ngesikhathi sokuguqulwa kwe-PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Umtapo wolwazi "ocrmypdf" awufakiwe.\n\nSicela uwufake ngalokhu:\npip install ocrmypdf',
        'btn_convert': 'Guqula',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        "filename_pdfa3_suffix": "_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Yenza i-PDF ibe ngcono (yehlisa usayizi wefayela)',
        'optimize_menu': 'Yenza i-PDF ibe ngcono (usayizi wefayela)',
        'optimize_info': 'Yehlisa usayizi wefayela le-PDF ngezindlela ezahlukene zokwenza ngcono.\n\nUma izinga lokucindezela liphezulu, ifayela lincane - ngokulahlekelwa okungenzeka kwekhwalithi ezithombeni.',
        'optimize_level': 'Izinga lokucindezela:',
        'optimize_level_low': 'Eliphansi (isheshayo, ukonga okuncane)',
        'optimize_level_medium': 'Ephakathi (isivumelwano esihle)',
        'optimize_level_high': 'Eliphezulu (ukonga okukhulu)',
        'optimize_level_maximum': 'Okuphezulu kakhulu (ukonga okuphezulu, kuhamba kancane)',
        'optimize_level_explanation': 'Isincomo: "Ephakathi" isivumelwano esihle phakathi kwejubane nosayizi wefayela.',
        'optimize_options': 'Izinketho:',
        'optimize_compress_images': 'Cindezela izithombe (yehlisa ikhwalithi ye-JPEG)',
        'optimize_clean_objects': 'Susa izinto ezingasetshenziswa',
        'optimize_preserve_metadata': 'Gcina imethadatha (isihloko, umbhali, njll.)',
        'optimize_image_quality': 'Ikhwalithi yesithombe:',
        'optimize_range': 'Ububanzi bamakhasi:',
        'optimize_all_pages': 'Wonke amakhasi',
        'optimize_custom_range': 'Ububanzi obwenziwe ngokwezifiso',
        'optimize_from': 'Kusuka:',
        'optimize_to': 'Kuya:',
        'optimize_target_folder': 'Ifolda okuyiwa kuyo:',
        'optimize_browse': 'Phenya...',
        'optimize_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'optimize_info_box': 'Ulwazi',
        'optimize_info_text': 'Ukwenziwa ngcono kungathatha imizuzu embalwa kuma-PDF amakhulu.\n\nIzithombe zigcinwa ngekhwalithi encishisiwe, okunganciphisa kakhulu usayizi wefayela.',
        'optimize_start': 'Kuqalwa ukwenziwa ngcono kwe-PDF...',
        'optimize_progress': 'Kwenziwa ngcono i-PDF...',
        'optimize_cancel': 'Ukwenziwa ngcono kwe-PDF kukhanseliwe',
        'optimize_complete': 'Ukwenziwa ngcono kwe-PDF sekuqediwe',
        'optimize_error_format': 'Iphutha ngesikhathi sokwenza ngcono i-PDF:\n\n{0}',
        'optimize_success_message': 'Ukwenziwa ngcono kwe-PDF kuphumelele!\n\nKulondolozwe njenge:\n{0}\n\nNgaphambili: {1}\nManje: {2}\nUkonga: {3:.1f}%\n\n{4}\n\nIngabe ufuna ukuvula i-PDF eyenziwe ngcono?',
        'optimize_success_message_no_size': 'Ukwenziwa ngcono kwe-PDF kuphumelele!\n\nKulondolozwe njenge:\n{0}\n\nUlwazi ngosayizi alutholakali.\n\nIngabe ufuna ukuvula i-PDF eyenziwe ngcono?',
        'optimize_result_positive': 'Ifayela lehliswe ngo-{0:.1f}%.',
        'optimize_result_zero': 'Akukho shintsho kusayizi wefayela.',
        'optimize_result_negative': 'Ifayela likhule ngo-{0:.1f}%.\nUkwenziwa ngcono kweqiwe, ifayela lokuqala lagcinwa.',
        'btn_optimize': 'Qala ukwenza ngcono',
        'filename_optimize_low_suffix': '_yenziwe_ngcono_ephansi',
        'filename_optimize_medium_suffix': '_yenziwe_ngcono',
        'filename_optimize_high_suffix': '_yenziwe_ngcono_ephezulu',
        'filename_optimize_maximum_suffix': '_yenziwe_ngcono_ephezulu_kakhulu',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Sika i-PDF',
        'crop_menu': 'Sika i-PDF (Crop)',
        'crop_range': 'Sebenzisa ku:',
        'crop_all_pages': 'Wonke amakhasi',
        'crop_current_page': 'Ikhasi lamanje kuphela',
        'crop_values': 'Amanani okusika (ngamaphoyinti):',
        'crop_left': 'Kunxele:',
        'crop_right': 'Kwesokudla:',
        'crop_top': 'Phezulu:',
        'crop_bottom': 'Phansi:',
        'crop_presets': 'Izilungiselelo ezimisiwe:',
        'crop_preset_white': 'Thola imingcele emhlophe',
        'crop_reset': 'Setha kabusha',
        'crop_mouse_hint': '🖱️ Donsa unxande ukuze ukhethe indawo ngokulinganiselayo.\nBese ungakwazi ukulungisa amanani ngokunembile kuma-SpinBox.\nUkulungisa ngesandla ngemouse akunakwenzeka.',
        'crop_apply': 'Sika',
        'crop_scope_all': 'Wonke amakhasi',
        'crop_scope_current': 'Ikhasi lamanje',
        'crop_new_size': 'Usayizi omusha: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Ayikho i-PDF elayishiwe',
        'crop_preview_error': 'Iphutha ngesikhathi sokulayisha ukubuka kuqala',
        'crop_start': 'Kuqalwa ukusika...',
        'crop_progress': 'Kusikwa i-PDF...',
        'crop_success': 'I-PDF isikiwe ngempumelelo!\n\nKulondolozwe njenge:\n{0}\n\nIngabe ufuna ukuvula i-PDF esikiwe?',
        'crop_complete': 'Ukusika sekuqediwe',
        'crop_cancel': 'Ukusika kukhanseliwe',
        'crop_error_format': 'Iphutha ngesikhathi sokwsika:\n\n{0}',
        'filename_crop_suffix': '_sikiwe',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Yenza i-PDF icwebe (Flatten)',
        'flatten_menu': 'Yenza i-PDF icwebe (Flatten)',
        'flatten_info': 'Ukwenza i-PDF icwebe "kushisa" zonke izinto ezihlelekayo kokuqukethwe kwekhasi.\n\nNgemuva kwalokho, izinkambu zefomu, imibhalo engezansi, imibhalo, iziphambano, amasiginesha, izithombe nezimo azisahleleki ngazinye.',
        'flatten_explanation_title': '📖 Lokhu kuyini okuhle?',
        'flatten_explanation_text': 'Ukwenza icwebe kuyadingeka ezimweni ezilandelayo:\n\n'
            '• 📄 Ufuna ukulungisa idokhumenti ukuze iphrintwe\n'
            '• 🔒 Ufuna ukuvimbela umuntu ukuthi ashintshe izinkambu zefomu\n'
            '• 📎 Ufuna "ukufaka" imibhalo engezansi namazwana ngokuphelele kudokhumenti\n'
            '• 🖼️ Ufuna ukubopha imibhalo, iziphambano, amasiginesha, izithombe nezimo ngokuphelele kudokhumenti\n'
            '• 📦 Ufuna ukulungisa ifayela ukuze ligcinwe\n\n'
            'Ukwenza icwebe kwenza i-PDF ibe ncane futhi kuvimbela izinto ukuthi zinganyakaziswa noma zisuswe ngengozi.',
        'flatten_what_title': 'Yini eyenziwa icwebe?',
        'flatten_what_list': '• ✅ Izinkambu zefomu (izinkambu zombhalo, amabhokisi okuhlola, izinkinobho)\n'
            '• ✅ Imibhalo engezansi (amazwana, okugqanyisiwe, amanothi)\n'
            '• ✅ Izendlalelo ezingaphezulu (imibhalo, iziphambano, amasiginesha, izithombe, izimo)',
        'flatten_options': 'Izinketho:',
        'flatten_forms': 'Yenza izinkambu zefomu zicwebe',
        'flatten_annotations': 'Yenza imibhalo engezansi icwebe',
        'flatten_overlays': 'Yenza izendlalelo ezingaphezulu zicwebe (imibhalo, iziphambano, amasiginesha, izithombe, izimo)',
        'flatten_target_folder': 'Ifolda okuyiwa kuyo:',
        'flatten_browse': 'Phenya...',
        'flatten_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'flatten_warning': '⚠️ Kubalulekile: Ukwenza icwebe kuyinqubo engenakuhlehliswa!\n\nNgemuva kokwenza icwebe, izinto ezihlelekayo azisakwazi ukushintshwa noma ukususwa ngazinye.\nYenza isipele ngaphambi kwesikhathi uma kudingeka.',
        'flatten_apply': 'Yenza icwebe',
        'flatten_start': 'Kuqalwa ukwenziwa icwebe...',
        'flatten_progress': 'Kwenziwa i-PDF icwebe...',
        'flatten_success': 'I-PDF yenziwe icwebe ngempumelelo!\n\nKulondolozwe njenge:\n{0}\n\nIngabe ufuna ukuvula i-PDF eyenziwe icwebe?',
        'flatten_complete': 'Ukwenza icwebe sekuqediwe',
        'flatten_cancel': 'Ukwenza icwebe kukhanseliwe',
        'flatten_error_format': 'Iphutha ngesikhathi sokwenza icwebe:\n\n{0}',
        'filename_flatten_suffix': '_yenziwe_icwebe',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Isendlalelo se-PDF (Overlay)',
        'overlay_menu': 'Isendlalelo se-PDF (Overlay)',
        'overlay_info': 'Ibeka i-PDF eyodwa (isendlalelo) phezu kwenye i-PDF.\n\nI-PDF yesendlalelo ibekwa phezu kwe-PDF eyisisekelo. Lokhu kuwusizo lwamaphawu amanzi, amalogo, izihloko zezincwadi noma izitembu.',
        'overlay_explanation_title': '📖 Lokhu kuyini okuhle?',
        'overlay_explanation_text': 'Isendlalelo siyadingeka ezimweni ezilandelayo:\n\n'
            '• 🏢 Beka ilogo yenkampani njengophawu lwamanzi kukhasi ngalinye\n'
            '• 📄 Beka isihloko sezincwadi kwi-PDF engenalutho\n'
            '• 🖊️ Beka isendlalelo sesitembu kudokhumenti\n'
            '• 🔖 Beka uphawu lwamanzi kuwo wonke amakhasi\n'
            '• 📑 Beka isendlalelo sefomu kusifanekiso',
        'overlay_type': 'Uhlobo lwesendlalelo:',
        'overlay_type_fullpage': 'Ikhasi lonke (elimbozayo)',
        'overlay_type_transparent': 'Ikhasi lonke (elikhanyayo - kunconywa)',
        'overlay_type_stamp': 'Isitembu (esingabekwa endaweni)',
        'overlay_type_info_fullpage': '📄 I-PDF yesendlalelo ibekwa ngqo phezu kwekhasi lonke.\nIngemuva elimhlophe lingasuswa ukuze kuphela okuqukethwe okuhlale kubonakala.',
        'overlay_type_info_transparent': '🔍 I-PDF yesendlalelo ibekwa phezu kwekhasi lonke ngengemuva elikhanyayo.\nIngemuva elimhlophe liyasuswa ngokuzenzakalelayo - kuhle kakhulu lwamaphawu amanzi namalogo!',
        'overlay_type_info_stamp': '🖊️ I-PDF yesendlalelo ibekwa endaweni futhi ilinganiswe njengesitembu.\nKuhle kakhulu lwamalogo, izitembu noma amasiginesha ezindaweni ezithile.',
        'overlay_remove_background': 'Susa ingemuva elimhlophe:',
        'overlay_remove_background_enable': 'Susa ingemuva elimhlophe kwi-PDF yesendlalelo (yenza isendlalelo sikhanyise)',
        'overlay_remove_background_tooltip': 'Isusa izindawo ezimhlophe kwi-PDF yesendlalelo ukuze umbhalo ongaphansi ubonakale.',
        'overlay_threshold': 'Inani lomkhawulo:',
        'overlay_threshold_hint': '(1-254, okuphezulu = okumhlophe okuningi kususwa)',
        'overlay_select_file': 'Khetha i-PDF yesendlalelo:',
        'overlay_file_placeholder': 'Sicela ukhethe ifayela le-PDF lesendlalelo',
        'overlay_browse': 'Phenya...',
        'overlay_select_overlay': 'Khetha i-PDF yesendlalelo',
        'overlay_range': 'Ububanzi bamakhasi:',
        'overlay_all_pages': 'Wonke amakhasi',
        'overlay_custom_range': 'Ububanzi obwenziwe ngokwezifiso',
        'overlay_from': 'Kusuka:',
        'overlay_to': 'Kuya:',
        'overlay_position': 'Indawo:',
        'overlay_position_center': 'Maphakathi',
        'overlay_position_top_left': 'Phezulu kwesokunxele',
        'overlay_position_top_right': 'Phezulu kwesokudla',
        'overlay_position_bottom_left': 'Phansi kwesokunxele',
        'overlay_position_bottom_right': 'Phansi kwesokudla',
        'overlay_size': 'Usayizi:',
        'overlay_size_original': 'Usayizi wokuqala',
        'overlay_size_fit_page': 'Linganisa nekhasi',
        'overlay_size_custom': 'Okwenziwe ngokwezifiso (%)',
        'overlay_opacity': 'Ukukhanya:',
        'overlay_target_folder': 'Ifolda okuyiwa kuyo:',
        'overlay_browse_folder': 'Phenya...',
        'overlay_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'overlay_warning': '⚠️ Qaphela: I-PDF yesendlalelo ibekwa phezu kwe-PDF eyisisekelo futhi "iyashiswa" kuyo.\n\nIzinto ze-PDF yesendlalelo azisakwazi ukuhleleka ngazinye ngemuva kokulondoloza.',
        'overlay_apply': 'Beka isendlalelo',
        'overlay_start': 'Kuqalwa ukubekwa kwesendlalelo...',
        'overlay_progress': 'Kubekwa isendlalelo se-PDF...',
        'overlay_success': 'I-PDF ibekwe isendlalelo ngempumelelo!\n\nKulondolozwe njenge:\n{0}\n\nIngabe ufuna ukuvula i-PDF enesendlalelo?',
        'overlay_complete': 'Ukubekwa kwesendlalelo sekuqediwe',
        'overlay_cancel': 'Ukubekwa kwesendlalelo kukhanseliwe',
        'overlay_error_format': 'Iphutha ngesikhathi sokubeka isendlalelo:\n\n{0}',
        'overlay_no_file': 'Ayikho i-PDF yesendlalelo ekhethiwe.\n\nSicela ukhethe ifayela le-PDF ukuze ubeke isendlalelo.',
        'filename_overlay_suffix': '_nesendlalelo',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Khipha izithombe kwi-PDF',
        'extract_images_menu': 'Khipha zonke izithombe',
        'extract_images_info': 'Ikhipha zonke izithombe kwi-PDF futhi izigcine njengamafayela ahlukene.\n\nIzithombe zigcinwa ngefomethi yazo yokuqala noma ziguqulwe zibe yifomethi ekhethiwe.',
        'extract_images_format': 'Ifomethi yesithombe:',
        'extract_images_quality': 'Ikhwalithi ye-JPEG:',
        'extract_images_options': 'Izinketho:',
        'extract_images_subfolder': 'Khipha kufolda engaphansi ("igamaPDF_izithombe")',
        'extract_images_unique': 'Izithombe eziyingqayizivele kuphela (gwema ukuphindaphinda)',
        'extract_images_range': 'Ububanzi bamakhasi:',
        'extract_images_all_pages': 'Wonke amakhasi',
        'extract_images_custom_range': 'Ububanzi obwenziwe ngokwezifiso',
        'extract_images_from': 'Kusuka:',
        'extract_images_to': 'Kuya:',
        'extract_images_target_folder': 'Ifolda okuyiwa kuyo:',
        'extract_images_browse': 'Phenya...',
        'extract_images_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'extract_images_info_box': 'Ulwazi',
        'extract_images_info_text': 'Ukukhipha kungathatha imizuzu embalwa kuma-PDF amakhulu.\n\nIzithombe zigcinwa ngegama lazo lokuqala (ikhasi_isithombe).',
        'extract_images_extract': 'Khipha',
        'extract_images_start': 'Kuqalwa ukukhipha...',
        'extract_images_progress': 'Kukhiptwa izithombe...',
        'extract_images_success': '✅ Izithombe zikhishwe ngempumelelo!\n\nIzithombe ezingu-{0} zilondolozwe ku:\n{1}',
        'extract_images_complete': 'Ukukhipha izithombe sekuqediwe',
        'extract_images_cancel': 'Ukukhipha kukhanseliwe',
        'extract_images_error_format': 'Iphutha ngesikhathi sokukhipha izithombe:\n\n{0}',
        'extract_images_open_folder': '📁 Vula ifolda',
        'extract_images_no_images': 'Azikho izithombe ezitholakala ku-PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Amakhasi amaningi ekhasi elilodwa (N-Up)',
        'nup_menu': 'Amakhasi amaningi ekhasi elilodwa (N-Up)',
        'nup_info': 'Ihlela amakhasi amaningi e-PDF ekhasi elilodwa.\n\nKuhle kakhulu lokuphrinta okuhlanganisiwe, ukubuka konke noma ama-handout.',
        'nup_layout': 'Isakhiwo:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Ukubuka kuqala:',
        'nup_preview_info': 'Amakhasi angu-{0} → amakhasi angu-{1} ishidi ngalinye → amashidi angu-{2}\nIsakhiwo: {3}',
        'nup_order': 'Ukulandelana:',
        'nup_order_horizontal': 'Okulundlile (umugqa ngomugqa)',
        'nup_order_vertical': 'Okumi mpo (ikholomu ngekholomu)',
        'nup_order_horizontal_reverse': 'Okulundlile okuphambene',
        'nup_order_vertical_reverse': 'Okumi mpo okuphambene',
        'nup_range': 'Ububanzi bamakhasi:',
        'nup_all_pages': 'Wonke amakhasi',
        'nup_custom_range': 'Ububanzi obwenziwe ngokwezifiso',
        'nup_from': 'Kusuka:',
        'nup_to': 'Kuya:',
        'nup_options': 'Izinketho:',
        'nup_margins': 'Imingcele:',
        'nup_margin_between': 'Isikhala phakathi kwamakhasi:',
        'nup_page_numbers': 'Faka izinombolo zamakhasi',
        'nup_target_folder': 'Ifolda okuyiwa kuyo:',
        'nup_browse': 'Phenya...',
        'nup_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'nup_create': 'Dala',
        'nup_start': 'Kuqalwa i-N-Up...',
        'nup_progress': 'Kwenziwa i-N-Up...',
        'nup_success': 'I-N-Up idaliwe ngempumelelo!\n\nKulondolozwe njenge:\n{0}\n\nIngabe ufuna ukuvula i-PDF entsha?',
        'nup_complete': 'I-N-Up sekuqediwe',
        'nup_cancel': 'I-N-Up ikhanseliwe',
        'nup_error_format': 'Iphutha ngesikhathi se-N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Shintsha usayizi wekhasi',
        'pagesize_menu': 'Shintsha usayizi wekhasi',
        'pagesize_info': 'Ishintsha usayizi wekhasi le-PDF.\n\nOkuqukethwe kulungiswa ngokuzenzakalelayo kusayizi omusha.',
        'pagesize_format': 'Ifomethi:',
        'pagesize_select': 'Khetha ifomethi ejwayelekile:',
        'pagesize_custom': 'Usayizi owenziwe ngokwezifiso:',
        'pagesize_width': 'Ububanzi:',
        'pagesize_height': 'Ukuphakama:',
        'pagesize_orientation': 'Inkomba:',
        'pagesize_portrait': 'Okumi mpo',
        'pagesize_landscape': 'Okulundlile',
        'pagesize_scale_options': 'Izinketho zokulinganisa:',
        'pagesize_fit': 'Linganisa (gcina isilinganiso)',
        'pagesize_stretch': 'Welula (hlanekela)',
        'pagesize_center': 'Maphakathi (usayizi wokuqala)',
        'pagesize_range': 'Ububanzi bamakhasi:',
        'pagesize_all_pages': 'Wonke amakhasi',
        'pagesize_custom_range': 'Ububanzi obwenziwe ngokwezifiso',
        'pagesize_from': 'Kusuka:',
        'pagesize_to': 'Kuya:',
        'pagesize_target_folder': 'Ifolda okuyiwa kuyo:',
        'pagesize_browse': 'Phenya...',
        'pagesize_select_folder': 'Khetha ifolda okuyiwa kuyo',
        'pagesize_apply': 'Sebenzisa',
        'pagesize_start': 'Kuqalwa ukushintshwa kosayizi wekhasi...',
        'pagesize_progress': 'Kushintshwa usayizi wekhasi...',
        'pagesize_success': 'Usayizi wekhasi ushintshiwe ngempumelelo!\n\nKulondolozwe njenge:\n{0}\n\nIngabe ufuna ukuvula i-PDF entsha?',
        'pagesize_complete': 'Ukushintshwa kosayizi wekhasi sekuqediwe',
        'pagesize_cancel': 'Ukushintshwa kosayizi wekhasi kukhanseliwe',
        'pagesize_error_format': 'Iphutha ngesikhathi sokushintsha usayizi wekhasi:\n\n{0}',
        'pagesize_preview_info': 'Usayizi omusha: {0} x {1} pt',
        'filename_pagesize_suffix': '_usayizi_omusha',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Ulwazi lwe-PDF',
        'pdf_info_menu': 'Bonisa ulwazi lwe-PDF',
        'pdf_info_voice': 'Kuboniswa ulwazi lwe-PDF',
        'pdf_info_error': 'Iphutha ngesikhathi sokubonisa ulwazi lwe-PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Bonisa izinqamuleli zekhibhodi",
        "shortcuts_dialog_title": "Izinqamuleli Zekhibhodi",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 IFAYELA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Vula i-PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Vala i-PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Londoloza njenge...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Vikela idokhumenti</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Phrinta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Phrinta ngokushesha (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Phuma ohlelweni</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 THENGISA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Thengisa njenge-Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Thengisa njenge-DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Thengisa njenge-TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Thengisa njengezithombe (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Khipha izithombe</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ UKUCUBUNGULA IDOKHUMENTI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Amakhasi amaningi)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Ukuguqulwa kwe-PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Yenza i-PDF icwebe</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Isendlalelo se-PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Yenza i-PDF ibe ngcono</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ HLELA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Sesha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Faka ibhukumaka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Phatha amabhukumaka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Ibhukumaka elilandelayo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Ibhukumaka elandulelayo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Sebenzisa i-OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 UKUPHATHWA KWAMAKHASI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Zungeza ikhasi lamanje</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Zungeza wonke amakhasi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Jwayeja ikhasi lamanje</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Jwayeja wonke amakhasi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Susa amakhasi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Khipha amakhasi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Faka amakhasi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Hambisa amakhasi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Hlanganisa ama-PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Shintsha usayizi wekhasi</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 FAKA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Faka umbhalo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Faka isiphambano</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Faka isiginesha 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Faka isiginesha 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Faka isithombe</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Faka unxande</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Faka i-ellipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Faka umugqa</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Faka umcibisholo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Faka izinombolo zamakhasi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Uphawu lwamanzi lombhalo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Uphawu lwamanzi lwesithombe</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ UKUFIHLA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Ukufihla (okumnyama)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Ukufihla (okumhlophe)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Sebenzisa konke ukufihla</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ OKUTHUTHUKILE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Sika i-PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Hlela imethadatha</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ BUKA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Shintsha Imodi Emnyama/Khanyayo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Bonisa iwindi lombhalo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Ububanzi bekhasi (Sondeza)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Amakhasi amabili (Sondeza)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Ukubuka konke (Sondeza)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ IZILUNGISELELO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Ukuphathwa kwephasiwedi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Izilungiselelo ze-OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Izilungiselelo zesiginesha</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Ukufomatha kwegama lefayela</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Thengisa izilungiselelo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Ngenisa izilungiselelo</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ ULWAZI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Bonisa ulwazi lwe-PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Vula/vala ukuphuma kwezwi</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Gxila kubha yemenyu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Inguqulo entsha iyatholakala",
        "update_available_message": "Kukhona inguqulo entsha <b>{0}</b>.\n\nVakashela ikhasi lokukhishwa ukuze ulande isibuyekezo:\n{1}",
        "update_available_voice": "Inguqulo entsha {0} iyatholakala. Sicela ulande isibuyekezo ekhasini le-GitHub.",
        "update_open_release": "Vula ikhasi lokukhishwa",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Landa zonke izinguqulo",
        "ask_download_all_translations": """Ngaphandle kwesiJalimane, isiNgisi nesiVietnam, kunezinye izilimi ze-GUI ezingama-{total_languages} ezitholakalayo.\n\nIngabe kufanele zinikezwe / zibuyekezwe?\n\nQaphela:\nIzilimi ezingadingeki ungazisula ngokwakho kamuva kumkhombandlela:\n{translations_path}
        \nUma uhoxisa, ungazilanda izilimi ze-GUI kamuva ngemenyu 'Amathuluzi → Buyekeza izinguquko'.""",
        "menu_update_translations": "Buyekeza izinguquko",
        "translations_updated": "Izinguquko zibuyekeziwe",
        "translations_update_success": "Izinguquko ezingama-{} zibuyekeziwe ngempumelelo ({} ezintsha, {} ezibuyekeziwe).",
        "translations_update_error": "Iphutha ekubuyekezeni izinguquko",
        "translations_update_no_changes": "Zonke izinguquko sezisesikhathini.",
        "translations_update_offline": "Akukho ukuxhuma kwe-inthanethi. Izinguquko azikwazanga ukubuyekezwa.",
        "translations_update_in_progress": "Izinguquko ziyabuyekezwa ngemuva...",
        "translations_downloading": "Kulandwa izinguquko...",
        "translations_path_hint": "Umkhombandlela womsebenzisi wezinguquko",
        "translations_update_not_available_title": "Isibuyekezo asitholakali",
        "translations_update_not_available_message": """Ukubuyekeza izinguquko kutholakala kuphela kunguqulo efakiwe.\n\nKumodi yokuthuthukisa, izinguquko sezisesikhathini.""",
        "translations_update_no_internet_title": "Akukho ukuxhuma kwe-inthanethi",
        "translations_update_no_internet_message": """Akukwazanga ukusungula ukuxhuma kwe-inthanethi.\n\nIzinguquko azikwazi ukulandwa ku-GitHub.\n\nIzixazululo ezingenzeka:
        • Hlola ukuxhuma kwakho kwe-inthanethi
        • Khubaza noma iyiphi i-firewall okwesikhashana
        • Zama futhi kamuva
        \nUngazilanda futhi izinguquko ngokwakho ku-GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Isibuyekezo sesivele siyaqhubeka",
        "btn_retry": "Zama futhi",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Siyakwamukela ku-PDF Dark View",
        "welcome_title_not_supported": "Siyakwamukela ku-PDF Dark View",
        "welcome_message": "Siyakwamukela ku-PDF Dark View!\n\nUlimi lwakho lwesistimu lutholwe njengo-'{language}'.\nIngabe ufuna ukusebenzisa lolu limi kusibonisi somsebenzisi?\n\nUngashintsha ulimi noma nini ngokusebenzisa 'Izilungiselelo → Ulimi'.",
        "welcome_message_language_not_available": "Siyakwamukela ku-PDF Dark View!\n\nUlimi lwakho lwesistimu lutholwe njengo-'{language}'.\nLolu limi alukafakwa.\n\nIngabe ufuna ukulanda izinguquko zika-{language} manje ku-GitHub?\n\n(Ulimi luzosetshenziswa ngokuzenzakalelayo kusibonisi somsebenzisi.)",
        "welcome_message_language_not_supported": "Siyakwamukela ku-PDF Dark View!\n\nUlimi lwakho lwesistimu lutholwe njengo-'{language}'.\nNgeshwa, azikho izinguquko zalolu limi okwamanje.\n\nIsibonisi somsebenzisi sizoboniswa ngo-{fallback_language}.\n\nUngashintsha ulimi noma nini ngokusebenzisa 'Izilungiselelo → Ulimi'.\nUma uthanda, ungafaka isandla ngenguqulo yolimi lwakho:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Yebo, sebenzisa ulimi lwesistimu",
        "welcome_keep_english": "Cha, gcina isiNgisi",
        "welcome_download_language": "Yebo, landa {language}",

        # ============================================
        # 107. IZINDLU EZISETSHENZISWE MUVA NJE
        # ============================================

        'menu_recent': 'Esisetshenziswe muva nje',
        'menu_recent_dirs': 'Izingqiziyana...',
        'menu_recent_files': 'Amafayela...',
        'recent_manage': 'Phatha...',
        'recent_enable_tracking': 'Gcina izindlu ezisetshenziswe muva nje (imfihlo)',
        'recent_enable_info': 'Vala le nketho ukuze ungazigcini izindlu',
        'recent_tracking_disabled': 'Ukulandelela izindlu kukhutshaziwe',
        'recent_enabled': 'kunikwe amandla',
        'recent_disabled': 'kukhutshaziwe',
        'recent_tracking_status': 'Ukulandelela izindlu {0}',
        'recent_dialog_title': 'Izindlu ezisetshenziswe muva nje',
        'recent_tab_directories': 'Izingqiziyana',
        'recent_tab_files': 'Amafayela',
        'recent_dirs_instruction': 'Chofoza kabili ukuvula ibhokisi lengxoxo yefayela engqiziyaneni',
        'recent_files_instruction': 'Chofoza kabili ukuvula i-PDF ngqo',
        'recent_no_directories': '(ayikho ingqiziyana egciniwe)',
        'recent_no_files': '(awukho ifayela eligciniwe)',
        'recent_default_current': '⭐ Okumisiwe: {0}',
        'recent_set_as_default': '⭐ Setha njengokumisiwe',
        'recent_default_set_title': 'Ingqiziyana emisiwe isethiwe',
        'recent_default_set_message': 'Ingqiziyana "{0}" isethiwe njengemisiwe yokuvula ama-PDF.',
        'recent_default_set_voice': 'Ingqiziyana emisiwe isethiwe',
        'recent_directory_not_found': 'Ingqiziyana ayitholakali',
        'recent_file_not_found': 'Ifayela alitholakali',
        'recent_remove_selected': 'Susa',
        'recent_remove_title': 'Susa indlela',
        'recent_remove_confirm': 'Ungakuqinisekisa ukuthi ufuna ukususa indlela "{0}" ohlwini?',
        'recent_path_removed': 'Indlela isusiwe',
        'recent_clear_all': 'Susa konke',
        'recent_clear_title': 'Susa zonke izindlu',
        'recent_clear_confirm_type': 'Ungakuqinisekisa ukuthi ufuna ukususa konke okungu-{0}?',
        'recent_cleared': 'Uhlu luhlanzekile',
        'recent_path_not_found_title': 'Indlela ayitholakali',
        'recent_path_not_found_message': 'Indlela "{0}" ayisekho.',
        'recent_open_file': 'Vula ifayela',
        'btn_open_recent': 'Vula',
        'recent_open_file_question': 'Ungathanda ukuvula "{0}" njenge-PDF?',
        'recent_not_pdf': 'Ifayela elikhethiwe aliyona i-PDF.',
        'recent_more_entries': 'Okunye okungenayo...',
        'btn_remove': 'Susa',
        'btn_clear': 'Hlanza konke',
        'recent_context_open': 'Vula',
        'recent_context_reveal': 'Bonisa ku-Finder',
        'recent_context_set_default': '⭐ Setha njengokumisiwe',
        'recent_context_open_terminal': '💻 Vula i-Terminal',
        'recent_context_file_info': 'Ulwazi lwefayela',
        'recent_context_open_with_default': '📄 Vula ngohlelo olumisiwe',
        'recent_context_remove': 'Susa ohlwini',
        'recent_context_clear_all': 'Susa konke',
        'recent_file_info_title': 'Ulwazi lwefayela',
        'recent_file_info_name': 'Igama',
        'recent_file_info_path': 'Indlela',
        'recent_file_info_size': 'Ubukhulu',
        'recent_file_info_modified': 'Kushintshiwe',
        'recent_file_info_pages': 'Amakhasi',
        'recent_error_reveal': 'Iphutha ukuvula ku-Finder',
        'recent_error_terminal': 'Iphutha ukuvula i-Terminal',
        'recent_error_info': 'Iphutha ukuthola ulwazi lwefayela',
        'open_user_data_folder': 'Bonisa ingqiziyana yedatha yomsebenzisi',

        # ============================================
        # 108. SUSWA AMAKHASI ALINGANAYO/ANGALINGANI
        # ============================================
        "pages_delete_even": "Susa wonke amakhasi alinganayo",
        "pages_delete_odd":  "Susa wonke amakhasi angalingani",
        "progress_even_pages": "Kususwa amakhasi alinganayo",
        "progress_odd_pages": "Kususwa amakhasi angalingani",
        "progress_mark_delete_even": "Amakhasi {} alinganayo amakiwe ukuze asuswe",
        "progress_mark_delete_odd":  "Amakhasi {} angalingani amakiwe ukuze asuswe",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Uhlelo luyavalwa",

    }
