
# ============================================
# translations_is.py - Íslensk orðabók (Isländisch)
# Vollständig sortiert nach Kategorien
# ============================================

def load_icelandic_strings():
    """Lädt alle isländischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View eftir BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Opna PDF",
        'btn_text_window': "OCR texti",
        'btn_first': "Fyrsta síða",
        'btn_prev': "Fyrri síða",
        'btn_next': "Næsta síða",
        'btn_last': "Síðasta síða",
        'btn_print': "Prenta",
        'btn_darkmode_light': "Ljós stilling",
        'btn_darkmode_dark': "Dökk stilling",
        'btn_delete_pages': "Eyða síðum",
        'btn_extract_pages': "Draga út síður",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "Í lagi",
        'btn_cancel': "Hætta við",
        'btn_save': "Vista",
        'btn_close': "Loka",
        'btn_delete': "Eyða",
        'btn_delete_all': "Eyða öllu",
        'btn_copy': "Afrita",
        'btn_export': "Flytja út",
        'btn_show': "Sýna lykilorð",
        'btn_hide': "Fela lykilorð",
        'btn_authenticate': "Auðkenna",
        'btn_settings': "Stillingar",
        'btn_protect': "Vernda",
        'btn_remove_password': "Fjarlægja lykilorð",
        'btn_manage': "Lykilorðastjórnun",
        'btn_retry': "Reyna aftur",
        'btn_select_all': "Velja allt",
        'btn_clear_selection': "Hreinsa val",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Síða {0} af {1}",
        'page_count': "af {0}",
        'goto_page': "Fara á síðu",
        'page_simple': "Síða {0}",
        'full_view_page': "Full útsýni síða {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Sláðu inn leitarorð + Enter",
        'search_results': "Niðurstöður: {0} af {1}",
        'search_nav_hint': "Enter: næsta (Shift+Enter: fyrri) niðurstaða",
        'search_no_results': "Engar niðurstöður",
        'search_error': "Villa í leit",
        'search_active': "Leitarsvæði virkt",
        'search_closed': "Leit lokið",
        'search_position': "Síða {0} {1}",
        'search_pos_top': "efst",
        'search_pos_upper': "fyrir ofan",
        'search_pos_middle': "miðja",
        'search_pos_lower': "neðan",
        'search_pos_bottom': "neðst",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Textagreining tókst!",
        'ocr_success_title': "OCR tókst",
        'ocr_success_message': "Skjalið er nú leitanlegt.",
        'ocr_failed': "OCR mistókst",
        'ocr_in_progress': "OCR í vinnslu",
        'ocr_preparing': "Undirbý PDF...",
        'ocr_analyzing': "Greini PDF...",
        'ocr_optimizing': "Myndfínstilling...",
        'ocr_recognizing': "Textagreining...",
        'ocr_embedding': "Texti innbyggður...",
        'ocr_finalizing': "Lýk PDF...",
        'ocr_not_available': "OCR ekki tiltækt",
        'ocr_install_message': "OCR-tól fundust ekki.\n\nVinsamlegast settu upp:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR nauðsynlegt",
        'ocr_question': "PDF inniheldur ekki leitanlegan texta.\nViltu framkvæma OCR til að gera {0} kleift?",
        'ocr_perform': "Framkvæma OCR",
        'ocr_later': "Seinna",
        'ocr_starting': "Ræsi tryggt OCR...",
        'ocr_success_voice': "OCR tókst. PDF er nú leitanlegt.",
        'ocr_partial_success': "OCR var framkvæmt, en upp komu vandamál við skiptingu.\n\nLeitanleg útgáfa var vistuð undir:\n{0}\n\nVilla: {1}",
        'ocr_partial_title': "OCR að hluta til tókst",
        'ocr_partial_voice': "OCR framkvæmt, en skipting mistókst.",
        'original_file': "Upprunaleg skrá:",
        'old_size': "Gömul stærð:    {0} bæti",
        'new_size': "Ný stærð: {0} bæti",
        'size_change': "Breyting: {0}{1} bæti",
        'backup_created_file': "Öryggisafrit búið til:\n{0}",
        'backup_not_created': "Öryggisafrit ekki búið til (stilling óvirk)",
        'page_header': "=== Síða {0} ===\n{1}\n",
        'scanned_page_header': "=== Síða {0} (skönnuð) ===\n[Þessi síða inniheldur aðeins skannaðan texta]\n[Vinsamlegast framkvæmdu OCR handvirkt]\n",
        'scanned_warning': "⚠️ SKANNAÐUR TEXTI - OCR NAUÐSYNLEGT",
        'guaranteed_title': "Leitanlegt PDF búið til",
        'guaranteed_message': "<b>Tryggð leitanleg útgáfa búin til!</b>\n\nÞar sem sjálfvirkt OCR mistókst var búin til önnur leitanleg PDF:\n\n{0}\n\n<b>Þessi skrá inniheldur:</b>\n• Útdrátt texta (ef til staðar)\n• Leiðbeiningar fyrir skannaðar síður\n• Er fullkomlega leitanleg",
        'guaranteed_voice': "Tryggt leitanlegt PDF búið til.",
        'instruction_title': "OCR LEIÐBEININGAR",
        'instruction_file': "Upprunaleg skrá: {0}",
        'instruction_text': "Sjálfvirk textagreining (OCR) mistókst.\nVinsamlegast framkvæmdu OCR handvirkt:\n\n1. MEÐ OCRmyPDF (skipanalína):\n   ocrmypdf --force-ocr \"[SKRÁ]\" \"útgangur.pdf\"\n\n2. MEÐ ADOBE ACROBAT (macOS/Windows):\n   • Opnaðu PDF í Acrobat\n   • Verkfæri > Breyta PDF\n   • Veldu 'Textagreining'\n\n3. MEÐ PREVIEW (macOS):\n   • Opnaðu PDF í forskoðun\n   • Skrá > Flytja út...\n   • Quartz sía: 'Minnka skráarstærð'\n   • Virkjaðu 'Framkvæma OCR'\n\n4. NETÞJÓNUSTUR OCR:\n   • smallpdf.com/is/ocr-pdf\n   • ilovepdf.com/is/ocr-pdf\n   • adobe.com/is/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR leiðbeiningar búnar til",
        'instruction_created_message': "Ítarlegar leiðbeiningar voru búnar til:\n\n{0}\n\nVinsamlegast fylgdu skrefunum fyrir handvirkt OCR.",
        'instruction_created_voice': "OCR leiðbeiningar búnar til.",
        'ocr_impossible': "OCR ekki mögulegt",
        'ocr_impossible_message': "Ekki var hægt að framkvæma OCR.\n\nVinsamlegast vinnslu '{0}' handvirkt með OCR hugbúnaði.",
        'ocr_impossible_voice': "OCR ekki mögulegt. Vinsamlegast vinnslu handvirkt.",
        'emergency_title': "NEYÐAR-OCR",
        'emergency_message': "Neyðar-PDF var búið til:\n\n{0}\n\nVinsamlegast vinnslu þessa skrá handvirkt með OCR.",
        'emergency_voice': "Neyðar-PDF búið til. Vinsamlegast framkvæmdu OCR handvirkt.",
        'critical_error': "Alvarleg villa",
        'critical_error_message': "Ekki var hægt að ræsa OCR.\n\nEndurræstu forritið og athugaðu OCR uppsetningu.",
        'critical_error_voice': "Alvarleg OCR villa",
        'ocr_question_html': "<p>PDF inniheldur ekki leitanlegan texta.<p>Viltu framkvæma OCR til að gera <b>{0}</b> kleift?</p>",
        'ocr_question_voice': "OCR nauðsynlegt. PDF inniheldur ekki leitanlegan texta. Viltu framkvæma OCR til að gera {0} kleift?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ekkert PDF hlaðið",
        'no_pdf_message': "Ekkert PDF er hlaðið",
        'pdf_not_found': "PDF skrá fannst ekki",
        'file_size': "Skráarstærð",
        'bytes': "bæti",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Öryggisafrit búið til",
        'backup_disabled': "Öryggisafrit óvirkt",
        'backup_activated': "Öryggisafritun virkjuð",
        'backup_deactivated': "Öryggisafritun óvirkjuð",
        'backup_status': "Öryggisafrit: {0}",
        'backup_on': "✔ virkt",
        'backup_off': "✘ óvirkt",
        'close_pdf': "Loka PDF: {0}",
        'pdf_not_found_format': "PDF skrá fannst ekki: {0}",
        'error_pdf_load_format': "Villa við að hlaða PDF: {0}",
        'load_failed_format': "Hleðsla mistókst:\n{0}",
        'decrypted_suffix': "(afkóðað)",
        'decryption_failed': "Afkóðun mistókst.",
        'decryption_error': "Villa við afkóðun",
        'decryption_success': "Tókst að afkóða",
        'decryption_success_message': "PDF var afkóðað og vistað undir:\n\n{0}",
        'decryption_success_voice': "PDF var afkóðað og vistað.",
        'password_remove_error': "Villa við að fjarlægja lykilorð",
        'save_unencrypted': "Vista ódulritað PDF sem",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Vista sem...",
        'save_copy': "Vista afrit",
        'save_success': "PDF vistað undir: {0}",
        'save_encrypted': "Verndað PDF vistað undir: {0}",
        'save_error': "Ekki var hægt að vista PDF",
        'encryption_question': "Viltu vernda PDF með lykilorði?",
        'encryption_yes': "Já",
        'encryption_no': "Nei",
        'encryption_cancel': "Hætta við",
        'save_cancel': "Vistun hætt við",
        'save_encrypted_voice': "Skrá dulrituð og vistuð.",
        'save_success_voice': "PDF skráin var vistuð ódulrituð.",
        'save_error_format': "Ekki var hægt að vista PDF:\n{0}",
        'export_pages_success': "Útflutningur í Pages tókst",
        'export_pages_error': "Útflutningur í Pages mistókst",
        'export_pages_error_format': "Útflutningur í Pages mistókst: {0}",
        'export_word_success': "Útflutningur í Word tókst",
        'export_word_error': "Útflutningur í Word mistókst",
        'export_word_error_format': "Útflutningur í Word mistókst: {0}",
        'export_text_success': "Textaútflutningur tókst",
        'export_text_error': "Textaútflutningur mistókst",
        'export_text_error_format': "Textaútflutningur mistókst: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Lykilorð nauðsynlegt",
        'password_enter': "Vinsamlegast sláðu inn lykilorð",
        'password_confirm': "Staðfestu lykilorð",
        'password_new': "Nýtt lykilorð",
        'password_current': "Núverandi lykilorð",
        'password_save': "Vista lykilorð (dulritað)",
        'password_saved': "✓ Lykilorð fyrir þessa skrá er vistað",
        'password_wrong': "Rangt lykilorð",
        'password_mismatch': "Lykilorð eru ekki eins",
        'password_too_short': "Lykilorð of stutt",
        'password_min_length': "Lykilorð verður að vera að minnsta kosti 4 stafir",
        'password_strength': "Styrkur lykilorðs",
        'password_strength_very_weak': "Mjög veikt",
        'password_strength_weak': "Veikt",
        'password_strength_medium': "Miðlungs",
        'password_strength_strong': "Sterkt",
        'password_strength_very_strong': "Mjög sterkt",
        'password_char_count': "({0} stafir)",
        'password_match': "✓ Samræmist",
        'password_no_match': "✗ Lykilorð eru ekki eins",
        'password_show': "Sýna",
        'password_hide': "Fela",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Lykilorðastjórnun",
        'password_table_filename': "Skráarheiti",
        'password_table_password': "Lykilorð",
        'password_count': "{0} vistuð lykilorð",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Engin vistuð lykilorð",
        'password_copied': "{0} lykilorð afrituð",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Ertu viss um að þú viljir eyða lykilorði fyrir '{0}'?",
        'password_delete_multiple': "Ertu viss um að þú viljir eyða {0} völdum lykilorðum?",
        'password_delete_all_confirm': "Ertu viss um að þú viljir eyða öllum {0} vistuðum lykilorðum?",
        'password_deleted': "{0} lykilorðum eytt",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Öllum lykilorðum eytt",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Lykilorðagjafi",
        'generator_generated': "Myndað lykilorð:",
        'generator_regenerate': "Mynda aftur",
        'generator_copy': "Afrita",
        'generator_use': "Nota",
        'generator_settings': "Stillingar",
        'generator_length': "Lengd:",
        'generator_group_every': "Aðgreining á hverjum",
        'generator_group_chars': "staf.    Aðgreinir:",
        'generator_uppercase': "Hástafir (A-Z)",
        'generator_lowercase': "Lágstafir (a-z)",
        'generator_digits': "Tölustafir (0-9)",
        'generator_symbols': "Sértákn (!@#$%^&*)",
        'generator_exclude': "Undanskilið:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Aðallykilorð nauðsynlegt",
        'master_password_setup': "Setja upp aðallykilorð",
        'master_password_change': "Breyta aðallykilorði",
        'master_password_enter': "Vinsamlegast sláðu inn aðallykilorðið þitt",
        'master_password_choose': "Veldu sterkt aðallykilorð (að minnsta kosti 8 stafir)",
        'master_password_new': "Vinsamlegast sláðu inn nýja aðallykilorðið þitt",
        'master_password_confirm': "Staðfestu lykilorð",
        'master_password_authenticate': "Auðkenna",
        'master_password_success': "Aðallykilorð var sett upp.",
        'master_password_changed': "Aðallykilorði var breytt.",
        'master_password_removed': "Aðallykilorði og öllum lykilorðum var eytt.",
        'master_password_remove': "Fjarlægja aðallykilorð",
        'master_password_remove_confirm': "Ertu ALGJÖRLEGA viss um að þú viljir eyða ÖLLUM lykilorðum?\n\nÞessi aðgerð er ÓAFTAKRÆF!",
        'master_password_export_before': "Viltu flytja út öryggisafrit fyrst?",
        'master_password_export_delete': "Flytja út og eyða",
        'master_password_delete_now': "Eyða núna",
        'master_password_for_signatures': "Til að geta notað undirskriftir þarftu að setja upp aðallykilorð.\n\nViltu setja upp aðallykilorð núna?",
        'master_password_for_private': "Til að geta notað einkatextabúta þarftu að setja upp aðallykilorð.\n\nViltu setja upp aðallykilorð núna?",
        'master_password_info': """
            <b>🔐 ÁN AÐALYKILORÐS:</b><br>
            • Ekki hægt að sýna, afrita og flytja út lykilorð<br>
            • Eyðing lykilorða er alltaf möguleg (jafnvel án aðallykilorðs)<br><br>

            <b>🔐 MEÐ AÐALYKILORÐI:</b><br>
            • Allar aðgerðir tiltækar eftir auðkenningu<br>
            • Lykilorð eru dulrituð með aðallykilorðinu<br>
            • Lágmarkslengd: 8 stafir<br>
            • Örugg SHA-256 kjötkássageymsla<br><br>

            <b>MIKILVÆGT:</b><br>
            • Ef þú týnir aðallykilorðinu er ekki hægt að endurheimta lykilorð<br>
            • Þegar aðallykilorði er eytt, verður ÖLLUM lykilorðum eytt<br>
            • Hægt er að flytja út afrit áður en eytt er<br>
            • Hægt er að breyta aðallykilorði hvenær sem er
        """,
        'signature_auth_disabled': "Slökkva á lykilorðabeiðni fyrir undirskriftir",
        'template_auth_disabled': "Slökkva á lykilorðabeiðni fyrir einkatextabúta",
        'master_password_for_signatures_settings': "Til að geta notað undirskriftir þarftu að setja upp aðallykilorð.\n\nFarðu í Stillingar - Lykilorðastjórnun",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Vernda PDF",
        'protect_info': "Skráin '{0}' verður vernduð með lykilorði.",
        'protect_instruction': "Vinsamlegast sláðu inn óskað lykilorð tvisvar til að vernda skjalið, eða notaðu lykilorðagjafann hægra megin við innsláttarsvæðið.",
        'protect_success': "PDF var verndað og vistað undir:\n{0}\n\nLykilorð: {1}\n\nViltu opna hina vernduðu PDF núna?",
        'protect_open': "Já",
        'protect_skip': "Nei",
        'protect_error': "Villa við að vernda PDF",
        'protect_open_title': "opna verndaða PDF",
        'protect_question': "Búið. Viltu opna hina vernduðu PDF núna? Já eða Nei?",
        'password_cancel': "Lykilorðaglugga hætt við",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Eyða síðum",
        'pages_extract': "Draga út síður",
        'pages_insert': "Setja inn síður",
        'pages_move': "Færa síður",
        'pages_delete_options': "Eyðingarvalkostir",
        'pages_delete_empty': "Eyða öllum tómum síðum",
        'pages_delete_current': "Eyða núverandi síðu",
        'pages_delete_range': "Eyða síðubili",
        'pages_extract_options': "Útdráttarvalkostir",
        'pages_extract_current': "Draga út núverandi síðu",
        'pages_extract_range': "Draga út síðubil",
        'pages_insert_position': "Innsetningarstaða",
        'pages_insert_before': "Setja inn fyrir síðu:",
        'pages_insert_select': "Velja PDF",
        'pages_insert_none': "Ekkert PDF valið",
        'pages_move_source': "Síður til að færa",
        'pages_move_from': "Frá síðu:",
        'pages_move_to': "Til síðu:",
        'pages_move_target': "Markstaða",
        'pages_move_before': "Færa fyrir síðu:",
        'pages_move_hint': "Athugasemd: síða 1 = byrjun, {0} = endir",
        'pages_range_invalid': "Upphafssíða verður að vera minni eða jöfn lokasíðu.",
        'pages_position_invalid': "Markstaða má ekki vera innan þess bils sem verið er að færa.",
        'pages_no_pdf_selected': "Ekkert PDF er valið.",
        'pages_deleted': "{0} síðum var eytt.",
        'pages_extracted': "Dregið út: {0}\nVistað undir: {1}\nSkráarstærð: {2:.1f} KB",
        'pages_inserted': "{0} síðum bætt við",
        'pages_moved': "{0} síðum var fært.",
        'pages_deleted_none': "Engum síðum var eytt.",
        'pages_delete_progress': "Eyði síðum...",
        'pages_deleted_with_backup': "{0} síðum var eytt.\n\nÖryggisafrit: {1}",
        'pages_deleted_voice': "Öryggisafrit búið til og {0} síðum eytt.",
        'info': "Upplýsingar",
        'error_dialog_creation': "Ekki var hægt að búa til glugga",
        'extract_page_single': "Draga út síðu {0}",
        'extract_page_range': "Draga út síður {0}-{1}",
        'extract_success_voice': "Síðum dregið út",
        'extract_error_format': "Villa við útdrátt: {0}",
        'pages_inserted_voice': "{0} síðum bætt við.",
        'insert_error_format': "Villa við innsetningu: {0}",
        'pages_move_progress': "Færi síður...",
        'pages_moved_with_backup': "{0} síðum var fært.\n\nÖryggisafrit: {1}",
        'move_success_title': "Færsla tókst",
        'pages_moved_voice': "{0} síðum fært",
        'mark_removed': "Merking af síðu {0} fjarlægð",
        'mark_empty': "Síða {0} merkt sem tóm",
        'mark_export_removed': "Útflutningsmerking af síðu {0} fjarlægð",
        'mark_export': "Síða {0} merkt til útflutnings",
        'no_empty_pages': "Engar tómar síður merktar til eyðingar",
        'delete_empty_confirm': "Viltu eyða öllum {0} merktu tómu síðunum?",
        'delete_empty_confirm_voice': "Eyða nú öllum {0} merktu tómu síðunum? Já eða Nei.",
        'empty_pages_deleted': "{0} tómum síðum eytt",
        'no_export_pages': "Engar síður merktar til útflutnings",
        'overwrite_title': "Skrifa yfir núverandi skrá",
        'overwrite_question': "Skráin\n\n{0}\n\ner þegar til.\nViltu skrifa yfir hana?",
        'overwrite_voice': "Skrifa yfir núverandi skrá? Já eða Nei.",
        'page_skipped': "Síðu {0} var sleppt",
        'export_complete': "Útflutningi lokið.",
        'export_complete_voice': "Útflutningi er lokið.",
        'no_pages_exported': "Engri síðu var flutt út",
        'export_cancelled': "Útflutningi hætt við",
        'pages_exported': "{0} síðum flutt út í {1}",
        'export_page_title': "Flytja út síðu",
        'page_exported': "Síðu {0} flutt út í {1}",
        'export_error': "Villa við útflutning",
        'export_marked_title': "Flytja út merktar síður",
        'rotate_all_title': "snúa öllum síðum",
        'rotate_all_question': "Viltu snúa öllum síðum um 90 gráður til hægri?",
        'rotate_all_voice': "Viltu snúa öllum síðum um 90 gráður til hægri? Já eða Nei?",
        'all_pages_rotated': "Öllum síðum snúið",
        'page_rotated': "Síðu {0} snúið",
        'rotate_error': "Ekki var hægt að snúa síðu",
        'delete_page_confirm': "Viltu eyða síðu {0}?",
        'delete_page_confirm_voice': "Ertu viss um að þú viljir eyða síðu {0}? Já eða Nei.",
        'page_deleted': "Síðu {0} eytt",
        'delete_error': "Ekki var hægt að eyða síðu",
        'pages_deleted_voice': "{0} síðum eytt",
        'pages_exported_split': "{0} síðum var flutt út.",
        'pages_skipped': "{0} síðum var sleppt.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Draga út síður (ítarlegt)",
        'pdf_splitter_title': "PDF skiptir & útdráttur",
        'pdf_splitter_load': " Velja PDF skrá",
        'pdf_splitter_info': "Vinsamlegast veldu valkost fyrir PDF skjalið þitt",
        'pdf_splitter_basic': "Grunn aðgerðir",
        'pdf_splitter_single': "Skipta í einstakar síður",
        'pdf_splitter_range': "Draga út síður:",
        'pdf_splitter_range_placeholder': "t.d. 1-3,5,7-9",
        'pdf_splitter_clean': "Hreinsunaraðgerðir",
        'pdf_splitter_remove_empty': "Fjarlægja allar tómar síður",
        'pdf_splitter_remove': "Eyða síðubili:",
        'pdf_splitter_remove_placeholder': "t.d. 2,4-6",
        'pdf_splitter_process': "Vinna PDF",
        'pdf_splitter_loaded': "PDF hlaðið. Vinsamlegast veldu valkost",
        'pdf_read_error': "Ekki var hægt að lesa PDF",
        'pages': "Síður",
        'pages_created': "Síður búnar til",
        'range_empty': "Vinsamlegast sláðu inn síðubil",
        'range_invalid': "Ógilt síðubil",
        'range_created': "Nýtt PDF með völdum síðum var búið til:\n{0}",
        'empty_removed': "{0} tómum síðum fjarlægt.\nÚttak: {1}",
        'remove_empty': "Vinsamlegast sláðu inn síður til að fjarlægja",
        'remove_invalid': "Ógildar síður til að fjarlægja",
        'remove_done': "Hreinsað PDF búið til:\n{0}",
        'open_folder': "Opna möppu",
        'show_in_finder': "Sýna í Finder",
        'pdf_splitter_no_pdf': "Vinsamlegast hladdu fyrst inn PDF skrá.",
        'process_error': "Villa við vinnslu PDF",
        'pages_created_voice': "{0} síður búnar til",
        'range_created_voice': "PDF með völdum síðum búið til",
        'empty_removed_voice': "{0} tómum síðum fjarlægt",
        'remove_done_voice': "Hreinsað PDF búið til",
        'pdf_splitter_split_groups': "Hvern samfelldan hóp í sér skrá",
        'range_created_single': "Nýtt PDF búið til:\n{0}",
        'range_created_multiple': "{0} PDF skrár búnar til.",
        'range_created_voice_single': "Eitt PDF með völdum síðum búið til",
        'range_created_voice_multiple': "{0} PDF skrár búnar til",
        'empty_removed_none_left': "Engar síður eftir",
        'empty_removed_all_empty': "Allar síður voru auðkenndar sem tómar og myndu verða fjarlægðar. Engin skrá var búin til.",
        'preview_single': "Forskoðun: {0}",
        'preview_enter_range': "Vinsamlegast sláðu inn síðubil.",
        'preview_invalid_range': "Ógilt síðubil.",
        'preview_file': "Forskoðun: {0}",
        'preview_files': "Forskoðun: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Hef prentun",
        'print_sent': "Prentverk sent",
        'print_now': "Prenta strax",
        'print_error': "Villa við straxprentun",
        'print_limited': "Prentunaraðgerð takmörkuð á þessu kerfi",
        'print_error_format': "Villa við straxprentun: {0}",
        'warning': "Aðvörun",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Skipta yfir í ljósa stillingu",
        'mode_switch_to_dark': "Skipta yfir í dökka stillingu",
        'mode_dark_activated': "Dökk stilling virkjuð",
        'mode_light_activated': "Ljós stilling virkjuð",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Fullt útsýni",
        'zoom_two_pages': "Tvær síður hlið við hlið",
        'zoom_overview': "Yfirlitsstilling",
        'zoom_cannot_during_search': "Ekki er hægt að stækka meðan leit stendur",
        'zoom_exit_first': "Vinsamlegast farðu fyrst úr stækkun",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Dragðu og slepptu virkt",
        'drag_disabled': "Dragðu og slepptu óvirkt",
        'drag_page_grab': "Síða {0} gripin",
        'drag_page_dropped': "Síða {0} sett inn á stöð {1}",
        'drag_position_invalid': "Ógild staða",
        'drag_same_position': "Síða {0} er áfram á stöð {0}",
        'drag_error': "Villa við að færa",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Textainnsláttur með ítarlegri sniðmátum og textabútastjórnun",
        'text_templates': "Tiltækir textabútar:",
        'text_name': "Heiti",
        'text_preview': "Textaforskoðun",
        'text_enter': "Texti:",
        'text_font_size': "Leturstærð:",
        'text_formatting': "Snið:",
        'text_bold': "Feitletrað",
        'text_italic': "Skáletrað",
        'text_underline': "Undirstrikað",
        'text_alignment': "Jöfnun:",
        'text_left': "Vinstri",
        'text_center': "Miðja",
        'text_right': "Hægri",
        'text_color': "Textalitur:",
        'text_opacity': "Gegnsæi:",
        'text_word_wrap': "Orðaskipting:",
        'text_auto': "Sjálfvirk",
        'text_page_width_95': "Síðubreidd (95%)",
        'text_page_width_85': "Mjög breitt (85%)",
        'text_page_width_75': "Breitt (75%)",
        'text_page_width_60': "Breitt (60%)",
        'text_page_width_50': "Miðlungs (50%)",
        'text_page_width_30': "Mjótt (30%)",
        'text_page_width_20': "Mjórra (20%)",
        'text_page_width_10': "Mjög mjótt (10%)",
        'text_no_wrap': "Engin skipting",
        'text_private': "Einkatextabútur (krefst auðkenningar)",
        'text_preview_label': "Forskoðun:",
        'text_preview_placeholder': "Hér birtist forskoðun textans...",
        'text_no_text': "(Enginn texti)",
        'text_save_template': "💾 Vista sem bút",
        'text_delete_template': "🗑 Eyða völdum textabút",
        'text_show_private': "Sýna einka",
        'text_hide_private': "Fela einka",
        'text_use': "✅ Nota texta",
        'text_saved': "Textabútur vistaður sem:\n{0}",
        'text_saved_voice': "Textabútur vistaður",
        'text_deleted': "Textabútur eytt",
        'text_no_text_to_save': "Enginn texti til að vista.",
        'text_no_templates': "Engir textabútar fundust",
        'text_private_master_required': "Einkabúta er aðeins hægt að nota ef aðallykilorð er sett upp.\n\nViltu setja upp aðallykilorð núna?",
        'text_filename': "Skráarheiti fyrir textabút (án 'Text_' og '.txt'):",
        'text_filename_hint': "Dæmi: 'Sími Heimaskrifstofa' verður vistað sem 'Text_Sími Heimaskrifstofa.txt'",
        'text_save_hint': "Textabúturinn verður sjálfkrafa vistaður með sniði.",
        'text_guide_title': "Textainnsláttur - Leiðbeiningar",
        'text_delete_confirm': "Ertu viss um að þú viljir eyða textabútnum?\n\nSkrá: {0}\nTexti: {1}...",
        'text_make_public': "Merkja sem opinberan",
        'text_make_private': "Merkja sem einka",
        'text_privacy_changed': "Einkastöðu breytt",
        'text_private_always': "Einka alltaf sýnileg (stilling)",
        'text_mode_required': "Vinsamlegast virkjaðu fyrst textastillingu",
        'text_continue_editing': "Halda áfram að breyta - bendill í lok texta",
        'text_no_input': "Enginn texti sleginn inn - texta eytt",
        'save_dialog_question': "Hvernig viltu halda áfram?",
        'text_save_question': "Vista alla texta og krossa, aðlaga, halda áfram að breyta eða eyða?",
        'copy_cross': "Kross afritaður",
        'paste_cross': "Kross settur inn",
        'paste_text': "Texti settur inn",
        'cross_discarded': "Krossi eytt",
        'all_discarded': "Öllu eytt",
        'text_discarded': "Texta eytt",
        'no_texts_to_save': "Engir textar til að vista",
        'no_valid_texts': "Engir gildir textar til að vista",
        'text_word_singular': "texti",
        'text_word_plural': "textar",
        'cross_word_singular': "kross",
        'cross_word_plural': "krossar",
        'texts_saved_title': "Textar vistaðir",
        'texts_crosses_saved': "{0} {1} og {2} {3} voru sett inn í PDF.\n\nPDF endurhlaðið...",
        'texts_crosses_saved_voice': "{0} {1} og {2} {3} vistuð.",
        'texts_saved': "{0} {1} voru sett inn í PDF.\n\nPDF endurhlaðið...",
        'texts_saved_voice': "{0} {1} vistuð.",
        'crosses_saved': "{0} {1} voru sett inn í PDF.\n\nPDF endurhlaðið...",
        'crosses_saved_voice': "{0} {1} vistuð.",
        'elements_saved': "{0} þættir voru settir inn í PDF.\n\nPDF endurhlaðið...",
        'elements_saved_voice': "{0} þáttum vistað.",
        'text_window_load_error': "Ekki var hægt að hlaða textaglugga",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Textainnsláttur og textabútar – Ítarlegar leiðbeiningar**

        **1. Að setja inn og breyta texta**
        - Hægrismelltu á þann stað í skjalinu sem þú vilt og veldu „Setja inn texta“.
        - Gluggi opnast þar sem þú getur slegið inn og sniðið textann:
        • Leturstærð, feitletrað, skáletrað, undirstrikað
        • Textalitur (frjálst val)
        • Gagnsæi (þekjuefni) með sleða
        • Orðaskipting (mismunandi breidd, t.d. síðubreidd, mjótt, engin skipting)
        - Eftir staðfestingu birtist textinn á smellistaðnum. Þú getur fært hann með músinni eða örvalyklum.
        - Tvísmelltu á textann til að opna breytingarham; ESC lýkur honum.

        **2. Að stjórna textabútum (sniðmátum)**
        - Vinstra megin í textaglugganum sérðu lista yfir alla vistaða textabúta.
        - **Að vista bút:** Sláðu inn textann, sniðaðu hann og smelltu á „💾 Vista sem bút“. Sláðu inn skráarheiti (án endingar).
        - **Að hlaða bút:** Smelltu á æskilegt heiti í listanum. Textinn og sniðið verða tekin inn og hægt er að aðlaga þau ef þörf krefur.
        - **Að eyða:** Hægrismelltu á bút til að eyða honum eða breyta einkastöðu hans.

        **3. Einkatextabútar (aðallykilorð)**
        - Ef þú hefur sett upp aðallykilorð (í Stillingar → Lykilorðastjórnun) geturðu merkt búta sem „einka“.
        - Virkjaðu gátreitinn „Einkatextabútur“ í glugganum áður en þú vistar.
        - Einkabútar birtast aðeins í listanum ef þú hefur einu sinni á lotu slegið inn aðallykilorðið þitt (auðkenning í gegnum lásmyndina eða við fyrstu aðgang).
        - Þannig geturðu verndað trúnaðartextabúta gegn óviðkomandi aðgangi.

        **4. Að setja inn krossa**
        - Í samhengisvalmyndinni geturðu einnig sett inn grafískan kross (t.d. fyrir gátreiti).
        - Stærð, línuþykkt og lit krossa er hægt að stilla á heimsvísu í stillingum (valmynd „Stillingar“ → „Krossastillingar“).
        - Hægrismelltu á núverandi kross til að breyta honum einstaklingsbundið.

        **5. Hópaðgerðir**
        - Ef þú hefur sett marga texta eða krossa á eina síðu geturðu vistað eða eytt þeim öllum í einu úr samhengisvalmyndinni (hægrismelltu í textaham).
        - Við vistun verða allir þættir innbyggðir í PDF og haldast sem vigurmyndir.

        **6. Flýtilyklar í textaham**
        - Örvalyklar: færa þátt
        - Ctrl+örvalyklar: stærri skref
        - Enter: opna vistunarvalmynd (vista allt / aðlaga / eyða)
        - ESC: eyða núverandi þætti
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Textainnsláttur og textabútar – Ítarlegar leiðbeiningar</strong></p>

        <p><strong>1. Að setja inn og breyta texta</strong></p>
        <ul>
        <li>Hægrismelltu á þann stað í skjalinu sem þú vilt og veldu „Setja inn texta“.</li>
        <li>Gluggi opnast þar sem þú getur slegið inn og sniðið textann:<br/>
        • Leturstærð, feitletrað, skáletrað, undirstrikað<br/>
        • Textalitur (frjálst val)<br/>
        • Gagnsæi (þekjuefni) með sleða<br/>
        • Orðaskipting (mismunandi breidd, t.d. síðubreidd, mjótt, engin skipting)</li>
        <li>Eftir staðfestingu birtist textinn á smellistaðnum. Þú getur fært hann með músinni eða örvalyklum.</li>
        <li>Tvísmelltu á textann til að opna breytingarham; ESC lýkur honum.</li>
        </ul>

        <p><strong>2. Að stjórna textabútum (sniðmátum)</strong></p>
        <ul>
        <li>Vinstra megin í textaglugganum sérðu lista yfir alla vistaða textabúta.</li>
        <li><strong>Að vista bút:</strong> Sláðu inn textann, sniðaðu hann og smelltu á „💾 Vista sem bút“. Sláðu inn skráarheiti (án endingar).</li>
        <li><strong>Að hlaða bút:</strong> Smelltu á æskilegt heiti í listanum. Textinn og sniðið verða tekin inn og hægt er að aðlaga þau ef þörf krefur.</li>
        <li><strong>Að eyða:</strong> Hægrismelltu á bút til að eyða honum eða breyta einkastöðu hans.</li>
        </ul>

        <p><strong>3. Einkatextabútar (aðallykilorð)</strong></p>
        <ul>
        <li>Ef þú hefur sett upp aðallykilorð (í Stillingar → Lykilorðastjórnun) geturðu merkt búta sem „einka“.</li>
        <li>Virkjaðu gátreitinn „Einkatextabútur“ í glugganum áður en þú vistar.</li>
        <li>Einkabútar birtast aðeins í listanum ef þú hefur einu sinni á lotu slegið inn aðallykilorðið þitt (auðkenning í gegnum lásmyndina eða við fyrstu aðgang).</li>
        <li>Þannig geturðu verndað trúnaðartextabúta gegn óviðkomandi aðgangi.</li>
        </ul>

        <p><strong>4. Að setja inn krossa</strong></p>
        <ul>
        <li>Í samhengisvalmyndinni geturðu einnig sett inn grafískan kross (t.d. fyrir gátreiti).</li>
        <li>Stærð, línuþykkt og lit krossa er hægt að stilla á heimsvísu í stillingum (valmynd „Stillingar“ → „Krossastillingar“).</li>
        <li>Hægrismelltu á núverandi kross til að breyta honum einstaklingsbundið.</li>
        </ul>

        <p><strong>5. Hópaðgerðir</strong></p>
        <ul>
        <li>Ef þú hefur sett marga texta eða krossa á eina síðu geturðu vistað eða eytt þeim öllum í einu úr samhengisvalmyndinni (hægrismelltu í textaham).</li>
        <li>Við vistun verða allir þættir innbyggðir í PDF og haldast sem vigurmyndir.</li>
        </ul>

        <p><strong>6. Flýtilyklar í textaham</strong></p>
        <ul>
        <li>Örvalyklar: færa þátt</li>
        <li>Ctrl+örvalyklar: stærri skref</li>
        <li>Enter: opna vistunarvalmynd (vista allt / aðlaga / eyða)</li>
        <li>ESC: eyða núverandi þætti</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Krossastillingar",
        'cross_properties': "Eiginleikar kross",
        'cross_size': "Stærð (px):",
        'cross_line_width': "Línuþykkt:",
        'cross_color': "Litur:",
        'cross_choose_color': "Velja",
        'cross_fine_tuning': "Nákvæmni við vistun (pixlar)",
        'cross_offset_x': "X-færsla:",
        'cross_offset_y': "Y-færsla:",
        'cross_offset_x_tooltip': "Neikvæð gildi færa krossinn til vinstri við vistun, jákvæð til hægri",
        'cross_offset_y_tooltip': "Neikvæð gildi færa krossinn upp við vistun, jákvæð niður",
        'cross_preview': "Forskoðun",
        'cross_save': "Beita stillingum",
        'cross_customized': "Kross aðlagaður",
        'cross_settings_applied': "Krossastillingar vistaðar.\nStærð: {0}px, línuþykkt: {1}px\n{2}",
        'cross_updated_count': "{0} núverandi krossar uppfærðir.",
        'cross_no_crosses': "Engir núverandi krossar fundust.",
        'cross_settings_applied_all': "Krossastillingar beittar á alla {0} krossa",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Undirskriftastillingar",
        'signature_1': "Undirskrift 1",
        'signature_2': "Undirskrift 2",
        'signature_select': "Veldu undirskrift",
        'signature_add': "➕ Bæta við nýrri undirskrift...",
        'signature_size': "Stærð fyrir undirskrift {0} (%):",
        'signature_common': "Almennar stillingar",
        'signature_timestamp': "Bæta sjálfkrafa við tímastimpli",
        'signature_location': "Sjálfgefin staðsetning:",
        'signature_timestamp_size': "Leturstærð tímastimpils:",
        'signature_no_files': "-- Engar undirskriftir fundust --",
        'signature_insert': "Setja inn undirskrift",
        'signature_insert_1': "Setja inn undirskrift 1",
        'signature_insert_2': "Setja inn undirskrift 2",
        'signature_customize': " Aðlaga undirskrift",
        'signature_discard': " Eyða þessari undirskrift",
        'signature_save_all': " Vista allar undirskriftir",
        'signature_discard_all': " Eyða öllum undirskriftum",
        'signature_guide_title': "Undirskriftir – Leiðbeiningar",
        'signature_guide': """
📝 Undirskriftir – Stuttar leiðbeiningar

- Settu upp aðallykilorð
- Stilla undirskriftir í valmyndinni Stillingar
  (stærð, tímastimpill ...)
- Settu inn með HÆGRISMELI á þeim stað sem þú vilt
  (aðallykilorð nauðsynlegt einu sinni á lotu)
- Færðu undirskriftina með músinni eða örvalyklum
- Hægt er að setja inn margar undirskriftir hverja á eftir annarri
- Hverja undirskrift er hægt að aðlaga sérstaklega
- Eyða einstakri undirskrift
- Vista / eyða öllum undirskriftum í einu
- Einnig er hægt að nota valmyndastikuna.
        """,
        'signature_placeholder': "Engin forskoðun tiltæk",
        'signature_info': "Undirskrift {0}: {1}×{2} px ({3}% af {4}×{5})",
        'signature_info_placeholder': "Stillingar fyrir undirskrift {0}",
        'signature_inserted': "Undirskrift {0} sett inn á síðu {1}",
        'signature_deleted': "Undirskrift eytt",
        'signature_copied': "Undirskrift afrituð",
        'signature_pasted': "Undirskrift {0} sett inn",
        'signature_saved': "{0} undirskriftum bætt við PDF.\n\nPDF endurhlaðið...",
        'signature_saved_voice': "{0} undirskriftir vistaðar",
        'mode_replace_signature_format': "Hætta í ham og setja inn undirskrift {0}",
        'mode_conflict_voice_signature': "{0} ham er virkur. Hætta og setja inn undirskrift?",
        'signature_not_configured': "Undirskrift {0} ekki stillt",
        'signature_file_not_found': "Undirskriftaskrá fannst ekki",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Engin afrituð undirskrift",
        'no_signatures_to_save': "Engar undirskriftir til að vista",
        'signature_save_question': "Vista allar undirskriftir, aðlaga eða eyða þessari?",
        'signatures_saved_title': "Undirskriftir vistaðar",
        'signatures_saved': "{0} undirskriftum bætt við PDF.\n\nPDF endurhlaðið...",
        'signatures_saved_voice': "{0} undirskriftir vistaðar.",
        'all_signatures_discarded': "Öllum undirskriftum eytt",
        'signature_settings_saved': "Undirskriftastillingar vistaðar",
        'signature_cancelled': "Undirskrift eytt",
        'signature_active_title': "Undirskrift virk",
        'signature_replace_question': "Undirskrift er þegar virk.\n\nViltu skipta út núverandi undirskrift?",
        'signature_replace': "Skipta út undirskrift",
        'signature_replace_voice': "Skipta út núverandi undirskrift eða hætta við?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Myndastillingar",
        'image_common': "Almennar myndastillingar",
        'image_keep_aspect': "Halda hlutföllum við drátt",
        'image_default_size': "Sjálfgefín stærð (%):",
        'image_dark_invert': "Ummynda myndir í dökkri stillingu",
        'image_dark_invert_tooltip': "Virkjað: myndir eru ummyndaðar fyrir betri sýnileika",
        'image_fine_tuning': "Nákvæmnistilling (pixlar)",
        'image_offset_x': "X-færsla:",
        'image_offset_y': "Y-færsla:",
        'image_offset_x_tooltip': "Neikvæð gildi færa myndina til vinstri við vistun, jákvæð til hægri",
        'image_offset_y_tooltip': "Neikvæð gildi færa myndina upp við vistun, jákvæð niður",
        'image_select': "Velja mynd",
        'image_insert': "Setja inn mynd",
        'image_customize': " Aðlaga mynd",
        'image_aspect': " Halda hlutföllum",
        'image_discard': " Eyða þessari mynd",
        'image_save_all': " Vista allar myndir",
        'image_discard_all': " Eyða öllum myndum",
        'image_filter': "Myndir",
        'image_guide_title': "Myndir settar inn – Leiðbeiningar",
        'image_guide': """
📷 Myndir settar inn í PDF – Stuttar leiðbeiningar:

1. Hægrismelltu á þann stað sem þú vilt
2. „Setja inn mynd“ → veldu mynd
3. Staðsettu myndina: dragðu með músinni
4. Stilltu stærð: dragðu í hornum/brúnum
5. Halda hlutföllum: [A] takki
6. Frekari aðlögun: hægrismelltu á myndina

Ábending: Í samhengisvalmyndinni geturðu stillt valkosti.
        """,
        'image_inserted': "Mynd sett inn á síðu {1}",
        'image_deleted': "Mynd eytt",
        'image_copied': "Mynd afrituð",
        'image_pasted': "Mynd sett inn",
        'image_saved': "{0} myndum bætt við PDF.\n\nPDF endurhlaðið...",
        'image_saved_voice': "{0} myndir vistaðar",
        'image_aspect_on': "virkt",
        'image_aspect_off': "óvirkt",
        'image_aspect_toggle': "Halda hlutföllum {0}",
        'image_reset': "Mynd endurstillt á upprunalega stærð",
        'image_replaced': "Mynd skipt út",
        'image_invalid': "Ógild mynd",
        'mode_replace_image': "Setja inn mynd",
        'mode_conflict_voice_image': "{0} ham er virkur. Hætta og setja inn mynd?",
        'image_active_title': "Mynd virk",
        'image_replace_question': "Mynd er þegar virk.\n\nViltu skipta út núverandi mynd?",
        'image_replace': "Skipta út mynd",
        'image_replace_voice': "Skipta út núverandi mynd eða hætta við?",
        'image_filter_all': "Myndir (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Allar skrár (*.*)",
        'no_copied_image': "Engin afrituð mynd",
        'image_discarded': "Mynd eytt",
        'image_save_question': "Vista allar myndir, aðlaga eða eyða þessari?",
        'no_images_to_save': "Engar myndir til að vista",
        'no_valid_images': "Engar gildar myndir til að vista",
        'images_saved_title': "Myndir vistaðar",
        'images_saved': "{0} myndum bætt við PDF.\n\nPDF endurhlaðið...",
        'images_saved_voice': "{0} myndir vistaðar.",
        'all_images_discarded': "Öllum myndum eytt",
        'image_settings_updated': "Myndastillingar uppfærðar",
        'image_replace_title': "Veldu nýja mynd",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Lögunarstillingar",
        'form_basic': "Grunnstillingar",
        'form_default_type': "Sjálfgefín lögun:",
        'form_rectangle': "Ferhyrningur",
        'form_ellipse': "Sporbaugur",
        'form_line': "Lína",
        'form_arrow': "Ör",
        'form_line_width': "Línuþykkt:",
        'form_colors': "Litir",
        'form_line_color': "Línulitur:",
        'form_fill_color': "Fyllingarlitur:",
        'form_choose_color': "Velja",
        'form_transparent': "Gagnsær bakgrunnur (aðeins lína)",
        'form_filled': "fyllt",
        'form_dark_mode': "Dökk stilling",
        'form_dark_invert': "Ummynda liti í dökkri stillingu",
        'form_fine_tuning': "Nákvæmnistilling (pixlar)",
        'form_offset_x': "X-færsla:",
        'form_offset_y': "Y-færsla:",
        'form_offset_x_tooltip': "Neikvæð gildi færa lögunina til vinstri við vistun, jákvæð til hægri",
        'form_offset_y_tooltip': "Neikvæð gildi færa lögunina upp við vistun, jákvæð niður",
        'form_preview': "Forskoðun",
        'form_insert': "Setja inn lögun",
        'form_rectangle_insert': "Ferhyrningur",
        'form_ellipse_insert': "Sporbaugur/hringur",
        'form_line_insert': "Lína (2 smellir)",
        'form_arrow_insert': "Ör (2 smellir)",
        'form_customize': " Aðlaga lögun",
        'form_transparent_toggle': " Gagnsær bakgrunnur",
        'form_discard': " Eyða þessari lögun",
        'form_save_all': " Vista allar lagnir",
        'form_discard_all': " Eyða öllum lögunum",
        'form_guide_title': "Lögun settar inn – Leiðbeiningar",
        'form_guide': """
📐 Lögun settar inn í PDF – Stuttar leiðbeiningar:

1. Veldu lögunartegund (ferhyrningur, sporbaugur, lína, ör)
2. Smelltu á staðsetningu
   - Ferhyrningur/sporbaugur: einn smellur setur lögunina
   - Lína/ör: tveir smellir fyrir upphafs- og endapunkt
3. Staðsettu lögunina: dragðu með músinni
4. Stilltu stærð: dragðu í hornum/brúnum
5. Vista lögun: Enter
6. Eyða lögun: ESC
7. Frekari aðlögun: hægrismelltu á lögunina

Ábending: Í samhengisvalmyndinni geturðu stillt valkosti.
        """,
        'form_inserted': "{0} sett inn á síðu {1}",
        'form_deleted': "Lögun eytt",
        'form_copied': "Lögun afrituð",
        'form_pasted': "Lögun sett inn",
        'form_saved': "{0} lögunum bætt við PDF.\n\nPDF endurhlaðið...",
        'form_saved_voice': "{0} lagnir vistaðar",
        'form_reset': "Lögun endurstillt á sjálfgefna stærð",
        'form_transparent_on': "virkt",
        'form_transparent_off': "óvirkt",
        'form_transparent_toggled': "Gagnsær bakgrunnur {0}",
        'form_line_cancel': "Línuteikningu hætt við",
        'form_second_click': "Smelltu nú á endapunkt fyrir {0}",
        'mode_replace_form': "Setja inn lögun",
        'mode_conflict_voice_form': "{0} ham er virkur. Hætta og setja inn lögun?",
        'form_settings_updated': "Lögunarstillingar uppfærðar",
        'form_unknown': "Lögun",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Smelltu á upphafspunkt",
        'form_line_guide_2': "2. Smelltu á endapunkt",
        'form_line_guide_3': "Línan verður teiknuð milli punktanna tveggja.",
        'form_line_status_1': "Bíð eftir fyrsta smelli...",
        'form_line_status_2': "Fyrsti punktur settur: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Smelltu nú á endapunkt...",
        'form_line_status_4': "Báðir punktar settir.\nSmelltu á 'Lokið' til að vista.",
        'form_line_reset': "Endurstilla",
        'form_line_finish': "Lokið",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Afrita (Cmd+C)",
        'paste': "Líma (Cmd+V)",
        'copied': "Afritað: {0}",
        'no_element_to_copy': "Enginn þáttur valinn til afritunar",
        'no_copied_data': "Engin afrituð gögn",
        'no_valid_position': "Engin gild staðsetning til að líma",
        'copy_text': "Texti afritaður",
        'copy_image': "Mynd afrituð",
        'copy_form': "Lögun afrituð",
        'copy_signature': "Undirskrift afrituð",
        'element_text': "Texti",
        'element_image': "Mynd",
        'element_form': "Lögun",
        'element_signature': "Undirskrift",
        'element_unknown': "Þáttur",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Hamárekstur",
        'mode_conflict_message': "Hamurinn '{0}' er þegar virkur.\n\nViltu hætta í honum og {1}?",
        'mode_replace': "Hætta í ham og {0}",
        'mode_cancel': "Hætta við",
        'mode_replace_text': "setja inn texta",
        'mode_replace_cross': "setja inn kross",
        'mode_replace_signature': "setja inn undirskrift",
        'mode_replace_image': "setja inn mynd",
        'mode_replace_form': "setja inn lögun",
        'mode_conflict_voice': "{0} ham er virkur. Hætta og setja inn texta?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Textainnsláttur",
        'active_mode_signature': "Undirskrift",
        'active_mode_image': "Mynd",
        'active_mode_form': "Lögun",
        'active_mode_and': " og ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Setja inn",
        'insert_another_text': "Setja inn texta",
        'insert_another_cross': "Setja inn kross",
        'insert_another_signature_1': "Undirskrift 1",
        'insert_another_signature_2': "Undirskrift 2",
        'insert_another_image': "Setja inn mynd",
        'insert_another_form_rect': "Ferhyrningur",
        'insert_another_form_ellipse': "Sporbaugur",
        'insert_another_form_line': "Lína (2 smellir)",
        'insert_another_form_arrow': "Ör (2 smellir)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Vista {0}",
        'save_dialog_message': "{0} verður vistað/ur á síðu {1}.\n\nHvernig viltu halda áfram?",
        'save_all': "Vista alla {0}",
        'save_single': "Vista {0}",
        'save_customize': "Aðlaga {0}",
        'save_discard': "Eyða þessum/þessari {0}",
        'save_continue': "Halda áfram að breyta",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Fara á síðu {0}",
        'context_rotate': " Snúa síðu {0}",
        'context_delete': " Eyða síðu {0}",
        'context_export': " Flytja út síðu {0}",
        'context_mark_as': " Merkja síðu sem...",
        'context_mark_empty': " Tóm síða",
        'context_unmark_empty': " Ekki lengur tóm",
        'context_mark_export': " Merkja til útflutnings",
        'context_unmark_export': " Ekki lengur flytja út",
        'context_batch_actions': " Hópaðgerðir",
        'context_batch_delete_empty': " Eyða öllum {0} tómu síðunum",
        'context_batch_export_single': " Flytja út allar {0} síður (ein skrá)",
        'context_batch_export_split': " Flytja út allar {0} síður (sér)",
        'context_drag_start': " Byrja draga og sleppa",
        'context_drag_stop': " Hætta draga og sleppa",
        'context_insert': " Setja inn",
        'context_insert_pages': " Setja inn síður",
        'context_zoom': "Stækkun",
        'discard_mixed': "Eyða öllum {0} {1} og {2} {3}",
        'save_mixed': "Vista {0} {1} og {2} {3}",
        'discard_texts': "Eyða öllum {0} textum",
        'discard_text_single': "Eyða 1 texta",
        'save_texts': "Vista {0} texta",
        'save_text_single': "Vista 1 texta",
        'discard_crosses': "Eyða öllum {0} krossum",
        'discard_cross_single': "Eyða 1 krossi",
        'save_crosses': "Vista {0} krossa",
        'save_cross_single': "Vista 1 kross",
        'discard_signatures': "Eyða öllum {0} undirskriftum",
        'save_signature_single': "Vista 1 undirskrift",
        'save_signatures': "Vista {0} undirskriftum",
        'discard_images': "Eyða öllum {0} myndum",
        'save_image_single': "Vista 1 mynd",
        'save_images': "Vista {0} myndum",
        'discard_forms': "Eyða öllum {0} lögunum",
        'save_form_single': "Vista 1 lögun",
        'save_forms': "Vista {0} lögunum",
        'cross_discard': "Eyða þessum krossi",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Útflutnings- / innflutningsupplýsingar",
        'export_what': "📋 Hvað er flutt út?",
        'export_general': "Almennar stillingar",
        'export_general_items': "• Talútgangur (á/af, hraði)\n• Dökk/ljós stilling\n• Öryggisafritunarstillingar\n• OCR-stillingar",
        'export_image_form': "Mynda- og lögunarstillingar",
        'export_image_form_items': "• Myndastillingar (hlutföll, sjálfgefín stærð)\n• Lögunarstillingar (línuþykkt, litir)\n• Undirskriftastillingar (slóðir, stærðir, tímastimplar)",
        'export_passwords': "Lykilorðagagnagrunnur",
        'export_passwords_items': "• Öll vistuð PDF lykilorð\n• Að vild dulrituð eða afkóðuð",
        'export_master': "Aðallykilorðsstillingar",
        'export_master_items': "• Aðallykilorðskjötkássa\n• Stillingar fyrir undirskriftir/textabúta",
        'export_signatures': "Undirskriftir og textabútar",
        'export_signatures_items': "• Allar myndaskrár (undirskriftir)\n• Allir textabútar með sniði\n• Einka/opinber merking",
        'export_import_warning': "⚠️ Mikilvægar athugasemdir",
        'export_import_note': "• Við innflutning verða ALLAR núverandi stillingar skrifaðar yfir\n• Endurræsa þarf forritið\n• Núverandi undirskriftir/textabútar verða skipt út",
        'export_master_note': "• Ef aðallykilorð er sett upp geturðu valið:\n  - Afkóðað (lykilorð í skýrum texta)\n  - Dulritað (aðeins læsilegt með aðallykilorði)",
        'export_security': "• Útflutt ZIP skrá inniheldur trúnaðargögn\n• Geymdu hana örugglega (t.d. á dulrituðu USB-lykli)\n• Ef skrá tapast tapast lykilorðin endanlega",
        'export_format': "📁 Útflutningssnið",
        'export_format_desc': "Stillingarnar eru vistaðar í einni ZIP skrá:",
        'export_filename': "PDFDarkView_Stillingar_ÁÁÁÁMMDD_SSMM.zip",
        'export_success': "Stillingar voru fluttar út",
        'export_failed': "Útflutningur mistókst",
        'export_import_question': "Viltu endurræsa forritið núna?",
        'export_password_question': "Aðallykilorð er sett upp.\n\nViltu flytja út lykilorðin afkóðuð?\n(annars verða þau flutt út dulrituð)",
        'export_decrypt': "Flytja út afkóðuð",
        'export_encrypt': "Flytja út dulrituð",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Upplýsingar",
        'info_title': "Um PDF Dark View",
        'info_version': "Útgáfa",
        'info_author': "Þróað af Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Um",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> er aðgengilegur PDF-skoðari sem er sérstaklega þróaður fyrir sjónskerta einstaklinga.</p>

            <p><strong>Helstu eiginleikar:</strong></p>
            <ul>
                <li>Mikil andstæða, sérsniðið viðmót</li>
                <li>Full lyklaborðsstýring</li>
                <li>Innbyggð talgervill</li>
                <li>OCR fyrir skönnuð skjöl</li>
                <li>Ítarleg ritunarverkfæri</li>
            </ul>

            <p>Meira en 50 tungumál eru studd – þannig að PDF skjöl séu aðgengileg öllum.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Eiginleikar",
        'info_features_intro': "PDF Dark View býður þér upp á eftirfarandi möguleika:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Birting og flakk</strong> – Dökkur/Ljós hamur, blaðsíðublöðun, aðdráttur, stökk á síðu</li>
            <li><strong>OCR (textaþekking)</strong> – Gerðu skönnuð skjöl leit- og afritanleg</li>
            <li><strong>Ritun</strong> – Settu inn texta, krossa, undirskriftir, myndir og form</li>
            <li><strong>Síðustjórnun</strong> – Eyða, draga út, setja inn, færa með draga og sleppa</li>
            <li><strong>Útflutningur</strong> – Í Word, Pages eða sem texta</li>
            <li><strong>Öryggi</strong> – Aðgangsorðsvernd og -stjórnun</li>
            <li><strong>Aðgengi</strong> – Talgervill, lyklaborðsstýring, mikil andstæða</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Notkun",
        'info_accessibility': "♿ Aðgengi – full lyklaborðsstýring",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Almenn</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Opna PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Leita</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Skipta um dökk/ljós ham</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Prenta</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Hætta</div>

        <div class="shortcut-cat">📖 Flakk</div>
        <div class="shortcut-row"><kbd>Örvatakkarnir</kbd> Blaða síðu fyrir síðu</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Fara á síðu</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Fyrsta síða</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Síðasta síða</div>

        <div class="shortcut-cat">✏️ Ritun</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Setja inn texta</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Eyða síðum</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Draga út síður</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Setja inn síður</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Færa síður</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Snúa síðu</div>

        <div class="shortcut-cat">🖼️ Færa hluti</div>
        <div class="shortcut-row"><kbd>Örvatakkarnir</kbd> Færa texta/mynd/undirskrift</div>
        <div class="shortcut-row"><kbd>Ctrl+Örvatakkarnir</kbd> Stærri skref</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Vista</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Hætta við</div>

        <div class="shortcut-cat">🗣️ Talgervill</div>
        <div class="shortcut-row"><kbd>F2</kbd> Kveikja/slökkva á talgervli</div>
        """,
        'info_contextmenu': "📌 Mikilvægt: Allir eiginleikar eru einnig aðgengilegir í samhengisvalmyndinni (hægri músarhnappur)!",
        'info_accessibility_hint': "💡 Ábending: Talgervillinn (F2) auðveldar stefnumörkun og gefur viðbrögð um valmyndir og glugga.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Leyfi & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Upplýsingar samkvæmt § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Þýskalandi<br>
        Tölvupóstur: binhdiez64@gmail.com<br>
        Ábyrgðarmaður efnis: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Fyrirvari</strong><br>
        Hugbúnaðurinn var þróaður með mestu vandvirkni. Engin ábyrgð er tekin á réttmæti, heilleika og virkni. Notkun er á eigin ábyrgð.<br><br>

        <strong>📄 MIT leyfi (einkanotkun)</strong><br>
        Höfundarréttur (c) 2026 Toralf Schulz (BinhDiez)<br>
        Leyfilegt: ókeypis notkun, einkabreytingar, persónuleg afrit.<br>
        Ekki leyfilegt: sala, atvinnunotkun, fjarlæging höfundarréttartilkynninga.<br><br>

        <strong>🔧 Þriðja aðila þættir</strong><br>
        Þessi hugbúnaður inniheldur þætti undir GPL, AGPL, Apache 2.0, BSD og MIT leyfum.<br>
        Við endurdreifingu verður að fylgja viðeigandi leyfisskilyrðum.<br><br>

        <strong>🌐 Opinn hugbúnaður</strong><br>
        Frumkóðinn er aðgengilegur og hægt er að skoða hann, breyta honum og dreifa honum áfram samkvæmt viðeigandi leyfisskilyrðum.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Þakkir",
        'info_credits': "Þakkir til opna hugbúnaðarsamfélagsins",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-vinnsla</li>
            <li><strong>PyQt5</strong> – Grafískt viðmót</li>
            <li><strong>Tesseract OCR</strong> – Textaþekking</li>
            <li><strong>OCRmyPDF</strong> – OCR samþætting</li>
            <li><strong>python-docx</strong> – Word útflutningur</li>
            <li><strong>qtawesome</strong> – Tákn</li>
            <li><strong>DeepSeek</strong> – Aðstoð við þýðingar (50+ tungumál)</li>
            <li><strong>Allir notendur</strong> – Fyrir dýrmæta endurgjöf</li>
            <li><strong>Opna hugbúnaðarsamfélagið</strong> – Fyrir frábær forritasöfn</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Tungumál",
        'info_languages_header': "🌍 Tungumálastuðningur",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View styður nú <strong>62 tungumál</strong> – þannig að hægt sé að nota hugbúnaðinn aðgengilega um allan heim.</p>

            <p><strong>📖 Heill tungumálalisti (Staða: Mars 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afríkanska</li>
                    <li>🇦🇱 Albanska (Shqip)</li>
                    <li>🇩🇿 Arabíska (العربية)</li>
                    <li>🇮🇩 Balinesíska (Basa Bali)</li>
                    <li>🇧🇩 Bengalíska (বাংলা)</li>
                    <li>🇲🇲 Búrmíska (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosníska (Bosanski)</li>
                    <li>🇧🇬 Búlgarska (Български)</li>
                    <li>🇨🇳 Kínverska (中文)</li>
                    <li>🇩🇰 Danska (Dansk)</li>
                    <li>🇩🇪 Þýska (Deutsch)</li>
                    <li>🇬🇧 Enska (English)</li>
                    <li>🇪🇪 Eistneska (Eesti)</li>
                    <li>🇫🇮 Finnska (Suomi)</li>
                    <li>🇫🇷 Franska (Français)</li>
                    <li>🇬🇷 Gríska (Ελληνικά)</li>
                    <li>🇮🇱 Hebreska (עברית)</li>
                    <li>🇮🇳 Hindí (हिन्दी)</li>
                    <li>🇭🇷 Króatíska (Hrvatski)</li>
                    <li>🇭🇺 Ungverska (Magyar)</li>
                    <li>🇮🇩 Indónesíska (Bahasa Indonesia)</li>
                    <li>🇮🇪 Írska (Gaeilge)</li>
                    <li>🇮🇸 Íslenska (Íslenska)</li>
                    <li>🇮🇹 Ítalska (Italiano)</li>
                    <li>🇯🇵 Japanska (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Kóreska (한국어)</li>
                    <li>🇱🇦 Laó (ພາສາລາວ)</li>
                    <li>🇱🇻 Lettneska (Latviešu)</li>
                    <li>🇱🇹 Litháíska (Lietuvių)</li>
                    <li>🇱🇺 Lúxemborgíska (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajíska (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathí (मराठी)</li>
                    <li>🇲🇳 Mongólska (Монгол)</li>
                    <li>🇳🇵 Nepalska (नेपाली)</li>
                    <li>🇳🇱 Hollenska (Nederlands)</li>
                    <li>🇳🇴 Norska (Norsk)</li>
                    <li>🇦🇫 Pastú (پښتو)</li>
                    <li>🇮🇷 Persneska (فارسی)</li>
                    <li>🇵🇱 Pólska (Polski)</li>
                    <li>🇵🇹 Portúgalska (Português)</li>
                    <li>🇮🇳 Púnjabí (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rúmenska (Română)</li>
                    <li>🇷🇺 Rússneska (Русский)</li>
                    <li>🇸🇪 Sænska (Svenska)</li>
                    <li>🇷🇸 Serbneska (Српски)</li>
                    <li>🇸🇰 Slóvakíska (Slovenčina)</li>
                    <li>🇸🇮 Slóvenska (Slovenščina)</li>
                    <li>🇪🇸 Spænska (Español)</li>
                    <li>🇹🇿 Svahílí (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamílska (தமிழ்)</li>
                    <li>🇮🇳 Telúgú (తెలుగు)</li>
                    <li>🇹🇭 Taílenska (ไทย)</li>
                    <li>🇨🇿 Tékkneska (Čeština)</li>
                    <li>🇹🇷 Tyrkneska (Türkçe)</li>
                    <li>🇺🇦 Úkraínska (Українська)</li>
                    <li>🇵🇰 Úrdú (اردو)</li>
                    <li>🇻🇳 Víetnamska (Tiếng Việt)</li>
                    <li>🇸🇳 Vólof (Wolof)</li>
                    <li>🇺🇸 Jiddíska (ייִדיש)</li>
                    <li>🇿🇦 Zúlú (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Bættu við eigin tungumálum:</strong><br>
                Viltu tungumál sem er ekki enn innifalið? Settu bara þína eigin orðabókarskrá (<code>sprache_xx.py</code>) við hliðina á forritinu – hugbúnaðurinn þekkir hana sjálfkrafa. Ef þú hefur áhuga á sérstakri þýðingu skaltu endilega hafa samband við mig.
            </div>

            <p><strong>🙏 Sérstakar þakkir:</strong> DeepSeek fyrir stuðninginn við að þýða allar orðabækurnar á 62 tungumál.</p>

            <p>📧 Hafa samband varðandi þýðingar: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Villa",
        'error_occurred': "Villa kom upp",
        'error_pdf_load': "Villa við að hlaða PDF",
        'error_pdf_save': "Villa við að vista PDF",
        'error_ocr': "Villa við textagreiningu",
        'error_no_pdf': "Ekkert PDF hlaðið",
        'error_page_not_found': "Síða fannst ekki",
        'error_invalid_range': "Ógilt síðubil",
        'error_file_not_found': "Skrá fannst ekki",
        'error_permission': "Engin heimild",
        'error_unknown': "Óþekkt villa",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Tókst",
        'success_operation': "Aðgerð tókst",
        'success_saved': "Vistað",
        'success_exported': "Útflutt",
        'success_imported': "Innflutt",
        'success_deleted': "Eytt",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Staðfesting",
        'confirm_yes': "Já",
        'confirm_no': "Nei",
        'confirm_ok': "Í lagi",
        'confirm_cancel': "Hætta við",
        'confirm_delete': "Eyða",
        'confirm_overwrite': "Skrifa yfir",
        'confirm_continue': "Halda áfram",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Hleð PDF...",
        'progress_saving': "Vista PDF...",
        'progress_exporting': "Flyt út PDF...",
        'progress_processing': "Vinnsla...",
        'progress_wait': "Vinsamlegast bíðið...",
        'progress_preparing': "Undirbý...",
        'progress_finalizing': "Ljúka...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Hvítur",
        'color_black': "Svartur",
        'color_red': "Rauður",
        'color_green': "Grænn",
        'color_blue': "Blár",
        'color_yellow': "Gulur",
        'color_magenta': "Magenta",
        'color_cyan': "Blágrænn",
        'color_orange': "Appelsínugulur",
        'color_gray': "Grár",
        'color_custom': "Litaval",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Skrá",
        'menu_edit': "&Breyta",
        'menu_view': "&Skoða",
        'menu_tools': "&Verkfæri",
        'menu_settings': "&Stillingar",
        'menu_help': "&Hjálp",
        'menu_language': "🌐 Tungumál",
        'menu_guides': "&Leiðbeiningar",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Opna",
        'file_save_as': "&Vista sem...",
        'file_protect': "&Vernda skjal...",
        'file_export': "&Flytja út",
        'file_export_pages': "Flytja út í Pages",
        'file_export_word': "Flytja út í DOCX",
        'file_export_text': "Flytja út í TXT",
        'file_print_now': "&Prenta strax",
        'file_print': "&Prenta",
        'file_close': "&Loka",
        'file_quit': "&Hætta",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Leita",
        'edit_ocr': " Framkvæma OCR",
        'edit_rotate': "&Snúa síðu",
        'edit_rotate_all': "Snúa &öllum síðum",
        'edit_delete_pages': "&Eyða síðum",
        'edit_extract_pages': "&Draga út síður",
        'edit_insert_pages': "&Setja inn síður",
        'edit_move_pages': "&Færa síður",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Setja inn texta og krossa",
        'text_insert': " Setja inn texta",
        'cross_insert': " Setja inn kross",
        'text_customize': " Aðlaga texta",
        'cross_customize': " Aðlaga þennan kross",
        'cross_customize_all': " Aðlaga alla krossa",
        'text_discard': " Eyða þessum texta/krossi",
        'text_discard_all': " Eyða öllum textum og krossum",
        'text_save_all': " Vista alla texta og krossa",
        'text_guide': " Textainnsláttur / textabútar – leiðbeiningar",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Setja inn undirskrift",
        'signature_settings_menu': " Stillingar...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Setja inn mynd",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Setja inn lagnir",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Sýna textaglugga",
        'view_zoom': "&Stækkun",
        'view_zoom_page': "&Síðubreidd (sjálfgefið)",
        'view_zoom_two': "&Tvær síður",
        'view_zoom_overview': "&Yfirlit (margar síður)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Aðgengi",
        'settings_voice': "Talútgangur",
        'settings_voice_tooltip': "bætir við upplýsingum við tal skjálesara",
        'settings_signature': "&Undirskriftastillingar",
        'settings_password': "&Lykilorðastjórnun",
        'settings_backup': "Búa til öryggisafrit fyrir breytingar",
        'settings_export_import': "&Flytja út stillingar / flytja inn stillingar",
        'settings_export': "&Flytja út allar stillingar...",
        'settings_import': "&Flytja inn allar stillingar...",
        'settings_export_info': "&Hvað er flutt út?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "á",
        'voice_off': "af",
        'voice_toggle': "Talútgangur {0}",
        'voice_speed': "Hraði {0} prósent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Tól fannst ekki:\n{0}\n\nBASE_DIR: {1}\nGakktu úr skugga um að PDF-tólin séu sett upp í möppunni {1}.",
        'tool_started': "{0} ræst",
        'tool_start_failed': "Ekki tókst að ræsa",
        'process_error_failed_to_start': "Ekki var hægt að ræsa ferli. Er skráin til?",
        'process_error_crashed': "Ferli hrundi við ræsingu.",
        'process_error_timeout': "Ferli rann út á tíma.",
        'process_error_write': "Villa við skrif í ferli.",
        'process_error_read': "Villa við lestur úr ferli.",
        'process_error_unknown': "Óþekkt ferlisskekkja",
        'process_command': "Skipun",
        'process_normal_exit': "lauk eðlilega",
        'process_crashed': "hrun",
        'process_nonzero_exit': "{0} lauk með villukóða {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Hætti við...",
        'move_cancelling': "Hætti við færslu",
        'opening_pdf': "Opna PDF...",
        'loading_document': "Hleð skjali...",
        'pdf_opened': "PDF opnað",
        'pages_found_moving': "{0} síður fundust, {1} til að færa",
        'creating_backup': "Bý til öryggisafrit...",
        'backup_description': "Tek öryggisafrit af upprunalegri skrá...",
        'backup_saved_as': "Öryggisafrit vistað sem: {0}",
        'error_format': "Villa: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView eftir BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Leit endurstillt",
        'page_header_simple': "=== Síða {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Lykilorðastjórnun – Leiðbeiningar",
        'password_guide_voice': "Leiðbeiningar um lykilorðastjórnun. Vinsamlegast lestu athugasemdirnar.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Lykilorðastjórnun – Ítarlegar leiðbeiningar</strong></p>

        <p><strong>1. Lykilorðavörn fyrir PDF-skjöl</strong></p>
        <ul>
        <li>Þegar þú opnar PDF með lykilorði birtist gluggi þar sem þú getur slegið inn lykilorðið.</li>
        <li>Þú getur vistað lykilorðið dulritað svo þú þurfir ekki að slá það inn í hvert skipti (gátreiturinn „Vista lykilorð“).</li>
        <li>Með hnappinum „Fjarlægja lykilorð“ geturðu búið til afkóðaða afrit af PDF-inu og eytt lykilorðinu úr gagnagrunninum.</li>
        </ul>

        <p><strong>2. Aðallykilorð</strong></p>
        <ul>
        <li>Aðallykilorðið verndar aðgang að öllum vistuðum PDF-lykilorðum.</li>
        <li><strong>Uppsetning:</strong> Farðu í „Stillingar → Lykilorðastjórnun → Aðallykilorðsstillingar“ og smelltu á „Setja upp aðallykilorð“. Veldu sterkt lykilorð (a.m.k. 8 stafir).</li>
        <li><strong>Breyting:</strong> Eftir árangursríka auðkenningu geturðu breytt aðallykilorðinu.</li>
        <li><strong>Fjarlæging:</strong> Ef þú fjarlægir aðallykilorðið verður ÖLLUM vistuðum lykilorðum eytt. Þú getur flutt út öryggisafrit áður en þú gerir það.</li>
        <li>Einu sinni á lotu verður þú að auðkenna þig með aðallykilorðinu til að fá aðgang að vernduðum aðgerðum (t.d. að sýna lykilorð).</li>
        </ul>

        <p><strong>3. Lykilorðastjórnun (listi)</strong></p>
        <ul>
        <li>Í „Stillingar → Lykilorðastjórnun“ opnast tafla með öllum vistuðum PDF-skjölum og dulrituðum lykilorðum þeirra.</li>
        <li><strong>Án aðallykilorðs:</strong> Þú getur aðeins eytt færslum – lykilorðin eru falin.</li>
        <li><strong>Með aðallykilorði (auðkennt):</strong> Þú getur séð, afritað, flutt út og eytt lykilorðum.</li>
        <li><strong>Útflutningur:</strong> Veldu snið (JSON, CSV, TXT) og vistaðu listann. Ef aðallykilorð er sett upp geturðu valið hvort lykilorðin séu flutt út afkóðuð eða dulrituð.</li>
        <li><strong>Innflutningur:</strong> Fyrri útflutt ZIP-skrá (allar stillingar) er hægt að flytja inn aftur í gegnum „Stillingar → Flytja út stillingar / flytja inn stillingar“. Athugið: Núverandi gögn verða skrifuð yfir!</li>
        </ul>

        <p><strong>4. Lykilorðagjafi</strong></p>
        <ul>
        <li>Í lykilorðaglugganum (t.d. þegar þú verndar PDF) er hægra megin við innsláttarsvæðið teningahnappur 🎲.</li>
        <li>Smelltu á hann til að opna lykilorðagjafann. Þú getur stillt lengd, stafasett (hástafi, lágstafi, tölur, sértákn) og aðgreini fyrir betri læsileika.</li>
        <li>Hægt er að nota myndaða lykilorðið beint og afrita það ef þörf krefur.</li>
        </ul>

        <p><strong>5. Mikilvægar öryggisathugasemdir</strong></p>
        <ul>
        <li>Vistuð lykilorð eru geymd dulrituð með AES-256. Lykillinn er fenginn úr aðallykilorðinu þínu (ef það er sett upp) eða úr fastri tölu (án aðallykilorðs).</li>
        <li>Án aðallykilorðs eru lykilorðin dulrituð en lykillinn er innbyggður í forritinu – árásarmaður með aðgang að skránum þínum gæti afkóðað þau. Því mælum við eindregið með því að nota aðallykilorð.</li>
        <li>Lykilorðagagnagrunnurinn er í skránni `Data/passwords.json`. Gerðu reglulega öryggisafrit, sérstaklega áður en þú fjarlægir aðallykilorðið.</li>
        <li>Ef þú týnir aðallykilorðinu tapast öll vistuð lykilorð endanlega.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Öfug hamur",
        'invert_mode_classic': "Klassískur (snúa öllum litum við)",
        'invert_mode_smart': "Snjall (snúa aðeins birtustigi við)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Grátóna þröskuldur",
        'gray_threshold_10': "10% (strangur)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Sjálfgefið)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (mjúkur)",
        'threshold_changed': "Þröskuldur stilltur á {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Grátóna þröskuldur – Skýring",
        'threshold_guide_text': "Grátóna þröskuldurinn ákvarðar hvaða punktar í snjalla dökka hamnum teljast 'gráir' og eru snúnir við.\n\n"
                                "• Lágt gildi (10%) snýr aðeins við nánast fullkomnum grátónum – litaeiningar haldast óbreyttar.\n"
                                "• Hátt gildi (50%) snýr einnig við örlítið litríkum punktum – þetta eykur andstæðu, en getur raskað litum.\n\n"
                                "Ákjósanlegt gildi fer eftir skjalinu. Fyrir hrein textaskjöl er 30–40% oft ákjósanlegt, fyrir litaða grafík frekar 10–20%.\n\n"
                                "Þú getur stillt gildið hvenær sem er í 'Stillingar' valmyndinni – PDF-ið verður þá endurhlaðið strax.\n\n"
                                "Athugið:\n* Ljósmyndir og myndir geta aðeins birst rétt í ljósum ham!\n* Öfugu stillingarnar birtast aðeins þegar dökkur hamur er virkur.",
        'threshold_guide_voice': "Grátóna þröskuldurinn ákvarðar hversu mikið snjalli dökki hamurinn grípur inn í. Lágt gildi varðveitir liti, hátt gildi eykur andstæðu.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Opna PDF...",
        'progress_loading_document': "Hleð skjal...",
        'progress_pdf_opened': "PDF opnað",
        'progress_creating_backup': "Bý til öryggisafrit...",
        'progress_backup_description': "Tryggja upprunalega skrá...",
        'progress_backup_created': "Öryggisafrit búið til",
        'progress_backup_saved_as': "Vistað sem: {0}",
        'progress_analyzing_start': "Hefja greiningu...",
        'progress_searching_empty': "Leita að tómum síðum...",
        'progress_page_empty': "Síða {0} er tóm",
        'progress_page_keep': "Halda síðu {0}",
        'progress_analysis_complete': "Greiningu lokið",
        'progress_empty_found': "Fundnar {0} tómar síður",
        'progress_current_page': "Núverandi síða",
        'progress_mark_delete': "Merkt til eyðingar",
        'progress_range_selected': "Síðubil {0}-{1}",
        'progress_deleting_pages': "Eyði {0} síðum",
        'progress_creating_new_pdf': "Bý til nýtt PDF...",
        'progress_transferring_pages': "Flyt síður",
        'progress_keeping_page': "Síða {0} verður höfð ({1}/{2})",
        'progress_saving_pdf': "Vista PDF...",
        'progress_optimizing': "Hagræða skráarstærð...",
        'progress_finalizing': "Loka...",
        'progress_new_size': "Ný stærð: {0:.2f} MB",
        'progress_cancelling': "Hætti við...",
        'progress_cancel_message': "Hætt við {0}",
        'progress_pages_found_moving': "Fundnar {0} síður, {1} til að færa",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Greini PDF...",
        'ocr_status_optimizing': "Myndhagræðing í gangi...",
        'ocr_status_recognizing': "Textaþekking í gangi...",
        'ocr_status_embedding': "Felli texta inn...",
        'ocr_status_finalizing': "Lýk PDF...",

        # PDF-Laden
        'progress_preparing': "Undirbý...",
        'progress_loading': "Hleð PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Eyði síðum...",
        'progress_moving_title': "Færi síður...",
        'pages_found': "Síður fundnar",
        'progress_creating_new_order': "Bý til nýja röð...",
        'progress_sorting_pages': "Raða síðum...",
        'progress_moving_to_begin': "Færi {0} síður í byrjun",
        'progress_transferring_count': "Flyt {0} síður",
        'progress_transferring_before_target': "Flyt síður fyrir markmið",
        'progress_moving_pages': "Færi {0} síður",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_afrit_",
        'filename_protected_suffix': "_verndud_",
        'filename_copy_suffix': "_Afrit",
        'filename_page_single': "_Sida_",
        'filename_page_range': "_Sidur_",
        'filename_export_page': "_Sida_{0:03}",
        'filename_export_range': "_Sidur_{0}-{1}",
        'filename_export_multiple': "_Sidur_{0}",
        'filename_with_text': "_med_Texta",
        'filename_with_signature': "_med_Undirskrift",
        'filename_with_image': "_med_Mynd",
        'filename_with_forms': "_med_Formum",
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
        'view_toggle_navbar': "Sýna hnappastiku",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Ekki er hægt að eyða öllum síðum",
		'pages_cannot_delete_last_page': 'Ekki er hægt að eyða síðustu síðunni!',
		'pages_cannot_delete_all_pages': 'Að minnsta kosti ein síða verður að vera eftir í skjalinu!',
		'delete_pages_confirm': 'Ertu viss um að þú viljir eyða {0} síðum?',
		'delete_pages_confirm_voice': 'Ertu viss um að þú viljir eyða {0} síðum?',
		'pages_deleted': '{0} síðum var eytt.',
		'warning': 'Aðvörun',
		'error': 'Villa',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Ekkert form valið",
        'form_customized': "Formi sérsniðið",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Velja",
        'btn_use': "Nota",
        'master_password_for_spasswords': "Til að geyma og nota lykilorð verður fyrst að setja upp aðallykilorð.\n\nViltu setja upp aðallykilorðið núna?",
        'open_saved_dialog_title': "Opna vistaða skrá",
        'open_saved_question': "Viltu opna vistuðu skrána núna?",
        'password': "Lykilorð",
        'password_manager_master_required': "Lykilorðastjórinn er aðeins tiltækur ef aðallykilorð hefur verið sett upp.\n\nViltu setja upp aðallykilorðið núna?",
        'password_master_required_for_select': "Til að skoða og velja vistuð lykilorð verður þú fyrst að sannvotta þig með aðallykilorðinu þínu.\n\nViltu sannvotta núna?",
        'password_not_available': "Valda lykilorðið er ekki tiltækt eða ekki hægt að afkóða það.",
        'password_options_title': "Valkostir lykilorðs",
        'password_save_choice_change': "Setja nýtt lykilorð",
        'password_save_choice_keep': "Nota núverandi lykilorð",
        'password_save_choice_none': "Vista ódulritað",
        'password_save_hint': "Settu fyrst upp aðallykilorð til að geyma lykilorð á öruggan hátt.",
        'password_save_master_required': "Vista lykilorð (aðeins mögulegt með aðallykilorði)",
        'password_save_question': "Núverandi PDF er varið með lykilorði. Viltu nota núverandi lykilorð, setja nýtt eða vista ódulritað?",
        'password_select': "Veldu lykilorð",
        'password_select_none': "Ekkert lykilorð valið.\n\nVinsamlegast veldu lykilorð úr listanum.",
        'password_select_one': "Vinsamlegast veldu nákvæmlega eitt lykilorð.\n\nÞú hefur merkt við mörg lykilorð.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_afrit",
        'filename_insert_suffix': "_með_innsetningu",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_síðum_eytt",
        'filename_pages_moved': "_síðum_flutt",
        'filename_rotated_all_suffix': "_allar_síður_snúnar",
        'filename_rotated_suffix': "_síðu_snúið",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Stillingar skráarnafna við breytingar á PDF",
        'filename_keep_suffixes': "Halda fyrri viðskeytum (t.d. _með_texta)",
        'filename_keep_suffixes_false': "Skipta út",
        'filename_keep_suffixes_true': "Halda",
        'filename_preview_label': "Forskoðun á skráarnafni:",
        'filename_preview_overwrite_hint': "Forskoðun ekki tiltæk – upprunalega skráin verður skrifuð yfir.",
        'filename_separator': "Aðskiljari milli orða",
        'filename_separator_none': "Enginn aðskiljari",
        'filename_separator_space': "Bil ( )",
        'filename_separator_underscore': "Undirstrik (_)",
        'filename_settings_saved': "Stillingar skráarnafna vistaðar",
        'filename_settings_title': "Snið skráarnafns og afrit",
        'filename_timestamp_position': "Staðsetning tímapunkts",
        'filename_timestamp_position_after': "Eftir grunnnafni",
        'filename_timestamp_position_before': "Alveg fremst",
        'filename_timestamp_position_end': "Aftast",
        'filename_use_timestamp': "Nota tímapunkt",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Hegðun við breytingar:</b><ul><li>Eyða og setja inn síður</li><li>Setja inn texta, undirskrift, mynd og form</li><li>OCR</li></ul></html>",
        'backup_section': "Afrit fyrir síðuaðgerðir (Eyða, Færa)",
        'behavior_info': "Athugið: Við 'Skrifa yfir upprunalega' eru tímapunktar og viðskeyti hunsuð – skráin heldur nafni sínu.",
        'behavior_new_file': "Alltaf búa til nýja skrá (með tímapunkti og viðskeyti)",
        'behavior_overwrite': "Skrifa yfir upprunalega (engin ný skrá)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Öllum síðum var snúið.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {0}",
        'all_pages_rotated_voice': "Öllum síðum snúið, búin til ný skrá.",
        'empty_pages_deleted_new_file': "{0} tómar síður voru eytt.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {1}",
        'empty_pages_deleted_voice': "{0} tómum síðum eytt, búin til ný skrá.",
        'ocr_keep_original': "Halda upprunalegu (opna handvirkt síðar)",
        'ocr_new_file_question': "Nýja leitanlega PDF skráin var vistuð sem:\n{0}\n\nViltu opna hana núna?",
        'ocr_open_new': "Opna nýja OCR skrá",
        'ocr_original_kept': "Upprunalega skráin helst opin. OCR skráin hefur verið vistuð.",
        'page_deleted_new_file': "Síðu {0} var eytt.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {1}",
        'page_deleted_voice': "Síðu {0} eytt, búin til ný skrá.",
        'page_rotated_new_file': "Síðu {0} var snúið.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {1}",
        'page_rotated_voice': "Síðu {0} snúið, búin til ný skrá.",
        'pages_deleted_new_file': "{0} síðum var eytt.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {1}",
        'pages_deleted_new_file_voice': "{0} síðum eytt, búin til ný skrá.",
        'pages_inserted_new_file': "{0} síðum var bætt við.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {1}",
        'pages_inserted_new_file_ask': "{0} síðum var bætt við.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {1}\n\nViltu opna hana núna?",
        'pages_inserted_voice_new': "{0} síðum bætt við, búin til ný skrá.",
        'pages_moved_new_file': "{0} síðum var fært.\n\nUpprunalega skráin breyttist ekki.\nNý skrá: {1}",
        'pages_moved_new_file_voice': "{0} síðum fært, búin til ný skrá.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Ekki sýna aftur",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Afritastilling</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Afrit KVEIKT</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Við allar breytingar sem skrifa yfir upprunalegu</strong> (texta, undirskrift, mynd, form, OCR, snúa, setja inn, eyða/færa síður) er <strong>sjálfkrafa búið til afrit með tímapunkti</strong> áður en breytingin er beitt.</p>
                <p style="margin: 5px 0 5px 20px;">• Afritið er við hlið upprunalegu skrárinnar (t.d. <code>Skjal_afrit_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Ef þú hefur einnig virkjað valkostinn <strong>„Skrifa yfir upprunalega“</strong> er einnig búið til afrit.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Afrit SLÖKKT</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Ekkert afrit er búið til</strong> – hvorki við yfirskrift né við síðuaðgerðir.</p>
                <p style="margin: 5px 0 5px 20px;">• Upprunalega skráin getur tapast óafturkræflega við yfirskrift.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Aðeins mælt með fyrir reynda notendur!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Ábending:</strong> Afritastillingin er óháð valkostinum „Skrifa yfir upprunalega“. Þú getur sameinað bæði.<br>
                Þú getur falið þessa skilaboð varanlega.
            </div>
        </div>
        """,
        'backup_info_title': "Hegðun afrits",
        'backup_info_voice': "Tilkynning um hegðun afrits við síðuaðgerðir. Afrit kveikt skrifar yfir upprunalegu, afrit slökkt býr til nýja skrá.",
        'show_backup_info': "Upplýsingar um afritastillingu",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Ekki sýna aftur",
        'overwrite_enable_backup': "Virkja afrit (mælt með)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Skrifa yfir upprunalega</p>
            <p>Ef þú virkjar þennan valkost, eru breytingar (texti, undirskrift, mynd, form, OCR, snúa, setja inn) <strong>vistaðar beint í upprunalegu skránni</strong> – <strong>engin ný skrá er búin til</strong>.</p>
            <p>• Skráarnafnið helst óbreytt.<br>
            • Tímapunktar og viðskeyti eru hunsuð.<br>
            • <strong>Án afrits getur upprunalega skráin tapast óafturkræflega.</strong></p>
            <p style="color: #FFD700;">Ráðlegging: Virkjaðu einnig afritavalkostinn til að fá sjálfvirk öryggisafrit.</p>
        </div>
        """,
        'overwrite_info_title': "Skrifa yfir upprunalega",
        'overwrite_info_voice': "Viðvörun: Skrifa yfir upprunalega – engin ný skrá. Afrit mælt með.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} síðum var bætt við.\n\nUpprunalega skráin var skrifuð yfir.\nBúið var til afrit.",
        'pages_inserted_overwrite_no_backup': "{0} síðum var bætt við.\n\nUpprunalega skráin var skrifuð yfir.\nEKKERT afrit var búið til.",
        'texts_saved_overwrite_with_backup': "Breytingarnar voru vistaðar í upprunalegu.\n\nBúið var til afrit.",
        'texts_saved_overwrite_no_backup': "Breytingarnar voru vistaðar í upprunalegu.\n\nEKKERT afrit var búið til.",
        'texts_crosses_saved_new_file': "{0} {1} og {2} {3} var bætt við.\n\nUpprunalega skráin breyttist ekki.\nBúin var til ný skrá.\n\nNýja PDF skráin hleðst...",
        'texts_saved_new_file': "{0} {1} var bætt við.\n\nUpprunalega skráin breyttist ekki.\nBúin var til ný skrá.\n\nNýja PDF skráin hleðst...",
        'crosses_saved_new_file': "{0} {1} var bætt við.\n\nUpprunalega skráin breyttist ekki.\nBúin var til ný skrá.\n\nNýja PDF skráin hleðst...",
        'elements_saved_new_file': "{0} þáttum var bætt við.\n\nUpprunalega skráin breyttist ekki.\nBúin var til ný skrá.\n\nNýja PDF skráin hleðst...",
        'signatures_saved_overwrite_with_backup': "Undirskrift(irnar) voru vistaðar í upprunalegu.\n\nBúið var til afrit.",
        'signatures_saved_overwrite_no_backup': "Undirskrift(irnar) voru vistaðar í upprunalegu.\n\nEKKERT afrit var búið til.",
        'images_saved_overwrite_with_backup': "Mynd(irnar) voru vistaðar í upprunalegu.\n\nBúið var til afrit.",
        'images_saved_overwrite_no_backup': "Mynd(irnar) voru vistaðar í upprunalegu.\n\nEKKERT afrit var búið til.",
        'forms_saved_overwrite_with_backup': "Form(in) voru vistuð í upprunalegu.\n\nBúið var til afrit.",
        'forms_saved_overwrite_no_backup': "Form(in) voru vistuð í upprunalegu.\n\nEKKERT afrit var búið til.",
        'signatures_saved_new_file': "{0} undirskriftum var bætt við.\n\nUpprunalega skráin breyttist ekki.\nBúin var til ný skrá.\n\nNýja PDF skráin hleðst...",
        'images_saved_new_file': "{0} myndum var bætt við.\n\nUpprunalega skráin breyttist ekki.\nBúin var til ný skrá.\n\nNýja PDF skráin hleðst...",
        'forms_saved_new_file': "{0} formum var bætt við.\n\nUpprunalega skráin breyttist ekki.\nBúin var til ný skrá.\n\nNýja PDF skráin hleðst...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Viðvörun: Þetta PDF inniheldur snúnar síður. Staðsetning getur verið frábrugðin.",
        'page_rotated_warning_title': "Snúin síða greind",
        'page_rotated_warning_message': "Núverandi síða {0} er snúin um {1}°.\n\nInnsetning þátta á snúnar síður er ekki studd.\n\nViltu snúa síðunni í upprétta stöðu núna?",
        'page_rotated_warning_voice': "Viðvörun: Síðan er snúin. Vinsamlegast snúið henni fyrst.",
        'paste_on_rotated_page_simple_warning': "Innsetning á síðu {0} ekki möguleg!\n\nÞessi síða er snúin um {1}°.\n\nVinsamlegast snúið síðunni fyrst í 0° (Valmynd: Breyta → Jafna síðu).\n\nViðvörun:\nFyrri afritaði þátturinn tapast ef þú vistar ekki áður en þú snýrð síðunni.",
        'paste_on_rotated_page_voice': "Innsetning hætt við. Síða er snúin. Vinsamlegast jafnaðu síðuna fyrst.",
        'page_rotated_cancel': "Hætta við",
        'page_rotated_rotate_until_upright': "Snúa síðu ítrekað (þar til upprétt)",
        'page_rotated_now_upright': "Síðan er nú upprétt. Þú getur nú sett inn.",
        'page_rotated_still_not_upright': "Ekki tókst að snúa síðunni í upprétta stöðu. Vinsamlegast leiðréttu handvirkt.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hjálp: Leiðrétta snúnar síður",
        'help_rotated_pages_voice': "Hjálp til að leiðrétta snúnar síður opnast.",
        'btn_help': "Hjálp",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Vandamál: Snúin síða – Innsetning virkar ekki rétt</p>

            <p>Ef innsetning texta, undirskrifta eða forma á snúinni síðu virkar ekki rétt, getur þú leiðrétt síðuna með ytri PDF ritli.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Lausn með ytra tóli (t.d. macOS Preview)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Flytja út síðu</strong><br>
                &nbsp;&nbsp;Smelltu í valmyndinni á <strong>Skrá → Flytja út sem síður</strong> eða notaðu aðra aðferð til að vista viðkomandi síðu sem eina PDF skrá.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Opna síðu í ytra forriti</strong><br>
                &nbsp;&nbsp;Opnaðu útflutta PDF skrána í PDF ritli (t.d. <strong>macOS Preview</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Snúa síðu</strong><br>
                &nbsp;&nbsp;Snúðu síðunni þannig að hún sé upprétt (í Preview: <strong>Verkfæri → Snúa</strong> eða <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Vista</strong><br>
                &nbsp;&nbsp;Vistaðu leiðréttu síðuna (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Setja síðuna aftur inn í upprunalega skjalið</strong><br>
                &nbsp;&nbsp;Farðu aftur í PDFDarkView og settu inn leiðréttu síðuna á viðkomandi stað:<br>
                &nbsp;&nbsp;<strong>Breyta → Setja inn síður</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Annað val: Snúa síðu í upprunalegu</p>
                <p style="margin: 5px 0 5px 20px;">• Notaðu innbyggða snúningsaðgerðina (<strong>Breyta → Snúa síðu</strong>) til að leiðrétta síðuna skref fyrir skref.<br>
                • Eftir hverja snúning geturðu athugað hvort innsetning virki núna.<br>
                • Þetta er oft hraðari lausnin – prófaðu hana fyrst!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Ábending:</strong> Ef þú rekst oft á snúnar síður geturðu falið viðvörunina í innsetningarglugganum varanlega.<br>
                Staðsetning getur þá verið frábrugðin – notaðu þennan valkost aðeins ef þú þekkir afleiðingarnar.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Jafna síður",
        'menu_rotate_normalize_tooltip': "Snúa síðu eða endurstilla í 0°",
        'normalize_current_page': "Færa núverandi síðu í upprétta stöðu (setja á 0°)",
        'normalize_all_pages': "Færa allar síður í upprétta stöðu (setja á 0°)",
        'page_normalized': "Síða {0} var sett í upprétta stöðu.",
        'all_pages_normalized': "Allar síður voru settar í upprétta stöðu.",
        'page_already_upright': "Síða {0} er nú þegar upprétt.",
        'all_pages_already_upright': "Allar síður eru nú þegar uppréttar.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF skráin inniheldur engan leitanlegan texta.</p><p>Viltu framkvæma OCR til að flytja út í {0}?</p>",
        'export_ocr_voice': "PDF skráin inniheldur engan texta. OCR er nauðsynlegt fyrir útflutning í {0}.",
        'export_no_ocr_possible': "Útflutningur án OCR ekki mögulegur. Vinsamlegast framkvæmdu OCR í gegnum valmyndina.",
        'ocr_failed_export_not_possible': "OCR mistókst. Ekki er hægt að framkvæma útflutning.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF skráin opnast í Preview. Vinsamlegast byrjaðu prentunarferlið þar.",
        'print_preview_manual': "PDF skráin hefur verið opnuð. Vinsamlegast framkvæmdu prentunarskipunina handvirkt (t.d. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Sameina PDF skrár",
        'merge_pdfs': "Sameina PDF skrár",
        'merge_progress_title': "Sameina PDF skrár...",
        'merge_pdfs_list': "PDF skrár í röð (Dragðu og slepptu til að raða)",
        'merge_add_pdf': "Bæta við PDF",
        'merge_remove': "Fjarlægja",
        'merge_move_up': "Upp",
        'merge_move_down': "Niður",
        'merge_pdfs_info': "💡 Ábending: Þú getur breytt röðinni með því að draga og sleppa",
        'merge_no_pdfs': "Engar PDF skrár valdar. Smelltu á 'Bæta við PDF'.",
        'merge_info': "{0} PDF skrár valdar (u.þ.b. {1} síður)",
        'merge_open_file': "Opna skrá",
        'merge_merge': "Sameina",
        'merge_error': "Villa við sameiningu",
        'merge_min_two_pdfs_error': "Vinsamlegast veldu að minnsta kosti tvær PDF skrár til að sameina.",
        'merge_select_pdfs': "Veldu PDF skrár til að sameina",
        'merge_error_file': "Villa við vinnslu",
        'merge_cancelled': "Sameiningu var hætt",
        'merge_preparing': "Undirbý...",
        'merge_processing': "Vinn PDF {0} af {1}",
        'merge_saving': "Vista sameinaða PDF skrá...",
        'merge_complete': "Lokið!",
        'merge_success_title': "Sameining tókst",
        'merge_success_voice': "{0} PDF skrám var sameinað með góðum árangri.",
        'merge_success_message': "{0} PDF skrám var sameinað með góðum árangri.\n\nNýja skjalið hefur nú {1} síður.\n\nNý skrá:\n{2}\n\nVistunarstaðsetning:\n{3}\n{2}\n\nViltu opna þessa PDF skrá?",
        'replace_file_title': "Skipta út skrá?",
        'replace_file_message': "PDF skrá er þegar opin. Viltu skipta henni út fyrir nýju skrána?",
        'btn_yes': "Já",
        'btn_no': "Nei",
        'filename_merge_suffix': "sameinuð",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Opna {0}...",
        'progress_merge_reading': "Lesa {0}...",
        'progress_merge_adding': "Bæta við {0} síðum...",
        'progress_merge_optimizing': "Hagræða PDF...",
        'progress_merge_writing': "Skrifa PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "að loka PDF skránni",
        'action_close_window': "að loka glugganum",
        'action_open_new_pdf': "að opna nýja PDF skrá",
        'action_quit_app': "að hætta í forritinu",
        'changes_saved': "Breytingarnar voru vistaðar.",
        'file_close_title': "Loka PDF skrá",
        'save_before_action': "Ætti að vista breytingarnar fyrir {0}? Já eða Nei?",
        'save_before_action_voice': "Ætti að vista breytingarnar fyrir {0}? Já eða Nei?",
        'save_before_close_question': "Ætti að vista breytingarnar fyrir lokun? Já eða Nei?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Leitanlegt PDF búið til:\n\n{0}\n\n<b>reyndu aftur ef þörf krefur",
        "ocr_rotate_title": "Jafna síður fyrir OCR",
        "ocr_rotate_question": "PDF-ið inniheldur snúnar síður.\nViltu jafna allar síður í 0° fyrir OCR?\nÞetta bætir textaþekkingu verulega.",
        "ocr_rotate_yes": "Já, jafna",
        "ocr_rotate_no": "Nei, hefja OCR beint",
        "ocr_rotate_voice": "PDF-ið inniheldur snúnar síður. Ætti að jafna allar síður fyrir OCR?",
        "ocr_not_performed_message": "Enginn texti til staðar. Vinsamlegast framkvæmdu OCR (valmynd \"Breyta\" → \"Framkvæma OCR\" eða takki Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR stillingar",
        "ocr_language_btn": "Veldu OCR tungumál",
        "ocr_language": "OCR tungumál",
        "ocr_language_current": "Núverandi tungumál:",
        "ocr_param_info": "Upplýsingar um breytu",

        "ocr_force_ocr_label": "Þvinga OCR",
        "ocr_deskew_label": "Leiðrétta skekkju",
        "ocr_clean_label": "Hreinsa mynd",
        "ocr_oversample_label": "Upplausn (DPI)",
        "ocr_pagesegmode_label": "Skipting síðu",
        "ocr_oem_label": "OCR vélastilling",
        "ocr_optimize_label": "Þjöppun PDF",
        "ocr_jobs_label": "Samhliða ferli",
        "ocr_verbose_label": "Smáatriði annáls",

        "ocr_force_ocr_tooltip": "Þvinga OCR á hverri síðu, jafnvel þótt texti sé þegar til staðar",
        "ocr_deskew_tooltip": "Jafna skökkuð skönnun sjálfkrafa",
        "ocr_clean_tooltip": "Fjarlægja hávaða og listaverk úr myndinni",
        "ocr_oversample_tooltip": "Stækka mynd fyrir OCR í þennan DPI",
        "ocr_pagesegmode_tooltip": "Ákvarðar hvernig síðunni er skipt í textasvæði",
        "ocr_oem_tooltip": "Velur OCR vél Tesseract",
        "ocr_optimize_tooltip": "Þjöppunarstig úttaks PDF",
        "ocr_jobs_tooltip": "Fjöldi samhliða OCR ferla",
        "ocr_verbose_tooltip": "Smáatriðastig annálsúttaks",
        "ocr_settings_explain_btn": "Skýring",

        "ocr_force_ocr_explain": "Þvingar textaþekkingu á <b>hverri</b> síðu, jafnvel þótt hún innihaldi nú þegar texta.\n\nRáðlegging: <b>Kveikt</b> fyrir skönnuð PDF, <b>Slökkt</b> fyrir innfædd PDF með nú þegar til staðar texta.",

        "ocr_deskew_explain": "Leiðréttir örlítið skökkuð skönnun (allt að um 5°).\n\nRáðlegging: <b>Kveikt</b> fyrir skönnuð skjöl, <b>Slökkt</b> ef síður eru þegar fullkomlega beinar.",

        "ocr_clean_explain": "Fjarlægir hávaða, punkta og lítil listaverk úr myndinni.\n<b>MIKILVÆGT:</b> Fyrir arabíska, taílenska eða víetnamska texta með sérhljóðamerkingum (punktar fyrir ofan/neðan stafi) ætti þennan valmöguleika að vera <b>óvirkjan</b>, annars geta mikilvægir stafir tapast.",

        "ocr_oversample_explain": "Stækkar myndina <b>fyrir</b> textaþekkingu í tilgreindan DPI.<br><br>• <b>72-150 DPI:</b> Mjög hratt, en lágt þekkingarhlutfall<br>• <b>200-300 DPI:</b> Ákjósanlegt bil (Sjálfgefið: 300)<br>• <b>400+ DPI:</b> Varla betri þekking, en verulega stærri skrár<br><br>Ráðlegging: 300 DPI fyrir flókin letur (arabíska, kínverska, japanska), 200 DPI fyrir vestræn tungumál.",

        "ocr_pagesegmode_explain": "Ákvarðar hvernig Tesseract skiptir síðunni í textasvæði.\n\n• <b>3 - Sjálfvirkt (Sjálfgefið):</b> Gott fyrir blandað útlit\n• <b>4 - Stakur dálkur:</b> Fyrir texta með einum dálki\n• <b>5 - Lóðréttur blokkur:</b> Fyrir lóðrétt letur (japanska, kínverska)\n• <b>6 - Samræmdur textablokkur:</b> Ákjósanlegt fyrir rennandi texta án dálka\n• <b>11 - Hrá mynd:</b> Fyrir slæm skönnun / handrit\n\nRáðlegging: <b>6</b> fyrir einföld textaskjöl, <b>3</b> fyrir flókið útlit.",

        "ocr_oem_explain": "Velur OCR vél Tesseract.\n\n• <b>0 - Legacy:</b> Gömlu vélin (hröð, en ónákvæmari)\n• <b>1 - LSTM:</b> Taugavél (hægari, en nákvæmari)\n• <b>2 - Legacy + LSTM:</b> Sameinar bæði niðurstöðurnar\n• <b>3 - Sjálfgefið (LSTM valið):</b> Besta valið fyrir flest tilfelli\n\nRáðlegging: <b>3</b> fyrir hámarks nákvæmni þekkingar.",

        "ocr_optimize_explain": "Þjappar úttaks PDF.\n\n• <b>0:</b> Engin hagræðing (hröðustu vinnsla)\n• <b>1:</b> Lítil hagræðing (gott málamiðlun)\n• <b>2:</b> Miðlungs hagræðing\n• <b>3:</b> Sterk hagræðing (minnsta skráin, en hægari)\n\nRáðlegging: <b>1</b> fyrir daglega notkun.",

        "ocr_jobs_explain": "Fjöldi samhliða ferla fyrir OCR.\n\n• <b>1:</b> Hægt, en lægsta minnisnotkun\n• <b>4-8:</b> Ákjósanlegt fyrir nútíma fjölkjarna örgjörva\n• <b>12+:</b> Valla hraðari vinnsla við háa minnisnotkun\n\nRáðlegging: Fjöldi örgjörvakjarna (t.d. <b>4</b> á 4-kjarna kerfum).",

        "ocr_verbose_explain": "Smáatriðastig annálsúttaks í samstöðinni.\n\n• <b>0:</b> Ekkert úttak\n• <b>1:</b> Framvinda og stöðuskilaboð\n• <b>2:</b> Nákvæmt úttak\n• <b>3:</b> Fullt kembiúttak (mjög umfangsmikið)\n\nRáðlegging: <b>1</b> fyrir eðlilega notkun.",

        "ocr_reset_title": "Stillingum endurstillt",
        "ocr_reset_message": "Öllum OCR stillingum hefur verið endurstillt í sjálfgefin gildi.",
        "info_tooltip": "Nánari upplýsingar um þessa breytu",
        "ocr_reset_defaults": "Endurstilla í sjálfgefið",

        "ocr_psm_0": "Sjálfvirkt (Legacy vélin)",
        "ocr_psm_1": "Sjálfvirk dálkagreining",
        "ocr_psm_3": "Sjálfvirkt (Sjálfgefið)",
        "ocr_psm_4": "Stakur dálkur",
        "ocr_psm_5": "Lóðréttur blokkur",
        "ocr_psm_6": "Samræmdur textablokkur",
        "ocr_psm_7": "Ein textalína",
        "ocr_psm_8": "Eitt orð",
        "ocr_psm_11": "Hrá mynd (engin útlitgreining)",

        "ocr_oem_0": "Legacy vélin (hröð)",
        "ocr_oem_1": "LSTM vélin (tauga, nákvæm)",
        "ocr_oem_2": "Legacy + LSTM sameinuð",
        "ocr_oem_3": "Sjálfgefið (LSTM valið)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR tungumál...",
        "ocr_language_title": "Veldu OCR tungumál",
        "ocr_language_instruction": "Veldu tungumál fyrir textaþekkingu (OCR).\nVarúð: Mörg tungumál koma á kostnað afkösts og nákvæmni!\nÞú færð bestu niðurstöðurnar ef þú velur aðeins eitt tungumál.",
        "ocr_language_predefined": "Fyrirfram skilgreindar samsetningar",
        "ocr_language_custom": "Sérsniðið...",
        "ocr_language_selected": "Valin OCR tungumál",
        "ocr_language_changed": "OCR tungumáli breytt í {0}",
        "ocr_language_auto_detect": "Tiltæk tungumál greinast sjálfkrafa.",
        "ocr_language_none_found": "Engin Tesseract tungumálagögn fundust! Vinsamlegast settu upp tungumálapakka (t.d. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Sérsniðið tungumálaval",
        "ocr_language_available": "Tiltæk tungumál (uppsett):",
        "ocr_language_select_hint": "Veldu eitt eða fleiri tungumál:",
        "ocr_language_confirm": "Beita",
        "ocr_language_reset": "Endurstilla í sjálfgefið (deu+eng+vie)",
        "ocr_language_priorities": "Mælt tungumál (foruppsett):",

        "select_all_languages": "Velja allt",
        "clear_all_languages": "Hreinsa val",
        "install_language_packs": "Setja upp vantar tungumálapakka...",
        "install_hint": "💡 Ábending: Ekki öll tungumál eru uppsett á kerfinu þínu. Með þessum hnappi færðu hjálp við uppsetningu.",
        "ocr_language_install_title": "Uppsetning Tesseract tungumálapakka",

        "ocr_missing_languages": "Vantar OCR tungumálapakka",
        "ocr_missing_languages_message": "Eftirfarandi völdu tungumál eru ekki uppsett á kerfinu þínu:\n\n{0}\n\nVinsamlegast settu upp vantaða tungumálapakka (sjá hjálp undir 'Uppsetningarhjálp').\n\nViltu opna uppsetningarhjálpina núna?",
        "ocr_missing_languages_voice": "Vantar tungumálapakka. Vinsamlegast settu upp tungumálin sem vantar.",
        "ocr_install_help_now": "Opna hjálp",
        "ocr_continue_anyway": "Reyna samt",
        "ocr_language_error_title": "Villa í OCR tungumáli",
        "ocr_language_error_message": "Villa við textaþekkingu: {0}\n\nVinsamlegast athugaðu stillingar þínar á OCR tungumáli (Stillingar → OCR tungumál).",
        "ocr_install_help_button": "Uppsetningarhjálp",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Settu upp Tesseract tungumálapakka</p>

        <p>Til að OCR virki á tilteknu tungumáli verða samsvarandi tungumálagögn að vera uppsett á kerfinu þínu. Fylgdu leiðbeiningunum fyrir stýrikerfið þitt:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Opnaðu <strong>Skjáhermi</strong> (Finder → Forrit → Tól → Skjáhermi).</li>
        <li>Settu upp öll tiltæk tungumál með:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Þetta getur tekið nokkrar mínútur.)</li>
        <li>Eða aðeins einstök tungumál (t.d. víetnamska):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Með núverandi Homebrew útgáfum gæti þurft að sækja <code>*.traineddata</code> handvirkt (sjá hér að neðan).</li>
        <li>Eftir uppsetningu: Lokaðu þessum glugga og opnaðu OCR tungumálaval aftur – nýju tungumálin birtast sjálfkrafa.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Opnaðu skjáhermi (Ctrl+Alt+T).</li>
        <li>Settu upp æskilegt tungumál, t.d. fyrir víetnamska:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Mikilvægir tungumálakóðar: <code>deu</code> (þýska), <code>eng</code> (enska), <code>vie</code> (víetnamska), <code>spa</code> (spænska), <code>fra</code> (franska), <code>ita</code> (ítalska), <code>nld</code> (hollenska), <code>fin</code> (finnska), <code>swe</code> (sænska), <code>nor</code> (norska).</li>
        <li>Sýna alla tiltæka pakka:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (handvirkt)</p>
        <ol>
        <li>Sæktu æskilegar <code>*.traineddata</code> skrár frá:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (t.d. <code>vie.traineddata</code> fyrir víetnamska).</li>
        <li>Afritaðu skrárnar í Tesseract tungumálamöppuna, venjulega:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Aðlagaðu eftir einstaklingsuppsetningu.)</li>
        <li>Endurræstu forritið (eða opnaðu OCR tungumálaval aftur).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Valkostur fyrir öll kerfi</p>
        <ul>
        <li>Settu upp <strong>OCRmyPDF</strong> og <strong>Tesseract</strong> með pakkastjóra að eigin vali. Flestar uppsetningar innihalda nú þegar nokkur staðlað tungumál (enska, þýska, franska).</li>
        <li>Hægt er að setja upp tungumál sem vantar hvenær sem er – OCR tungumálaval sýnir aðeins tungumálin sem raunverulega eru til staðar.</li>
        </ul>

        <hr>
        <p><b>✅ Eftir uppsetningu:</b> Ekki þarf að endurræsa forritið – nýtilkomnu tungumálin birtast strax á listanum.</p>
        <p><b>📖 Hjálp með tungumálakóða:</b> Heill listi er fáanlegur í <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract skjölun</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans letur",
        "info_noto_font_voice": "Leiðbeiningar um uppsetningu Noto Sans leturs",
        "btn_info_noto_font_install": "Leturupplýsingar",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Hvernig seturðu upp ókeypis Noto letur frá Google</h2>

        <p><strong>Noto letur</strong> eru opinn uppspretta leturfjölskylda frá Google. Markmið þeirra er að sjá <em>"ekki tófú"</em> (þ.e. enga tóma kassa □) og sýna hvern staf úr Unicode staðlinum rétt. Þau eru hið fullkomna viðbót fyrir forrit sem þurfa að sýna texta á mörgum mismunandi tungumálum.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Uppsetning á macOS</h3>

        <p><strong>Aðferð 1: Með Homebrew (fyrir lengra komna)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Aðferð 2: Í gegnum "Font Book" (Mælt með)</strong></p>

        <ol>
        <li>Sæktu opinbera leturpakka:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Afþjappaðu ZIP skránni</li>
        <li>Afritaðu skrárnar inn í <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Uppsetning á Windows (10 & 11)</h3>

        <p><strong>Aðferð 1: Microsoft Store (Mælt með)</strong><br>
        Leitaðu að "Google Noto Fonts" eða "Noto Sans" og smelltu á <strong>Setja upp</strong>.</p>

        <p><strong>Aðferð 2: Handvirk uppsetning</strong></p>

        <ol>
        <li>Sæktu:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Afþjappaðu ZIP</li>
        <li>Veldu .ttf / .otf skrár</li>
        <li>Hægrismelltu → <strong>Setja upp</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        eða<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Nafn\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Uppsetning á Linux</h3>

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

        <p>Staðfesting:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Stjórna bókamerkjum",
        "bookmark_add": "Bæta við bókamerki",
        "bookmark_add_tooltip": "Vista núverandi síðu sem bókamerki",
        "bookmark_remove": "Fjarlægja bókamerki",
        "bookmark_remove_tooltip": "Eyða merktu bókamerki",
        "bookmark_remove_all": "Fjarlægja öll",
        "bookmark_remove_all_tooltip": "Eyða öllum bókamerkjum þessa PDF",
        "bookmark_jump": "Fara í bókamerki",
        "bookmark_jump_tooltip": "Fara á valda síðu",
        "bookmark_name": "Nafn",
        "bookmark_page": "Síða",
        "bookmark_no_bookmarks": "Engin bókamerki til staðar.\nSmelltu á 'Bæta við' til að vista núverandi síðu sem bókamerki.",
        "bookmark_added": "Bókamerki fyrir síðu {0} bætt við: {1}",
        "bookmark_removed": "Bókamerki fjarlægt: {0}",
        "bookmark_all_removed": "Öll bókamerki hafa verið fjarlægð.",
        "bookmark_name_default": "Síða {0}",
        "bookmark_name_prompt": "Nafn fyrir bókamerkið:\n(langur texti verður styttur í 50 stafi)",
        "bookmark_name_prompt_title": "Nafn bókamerkis",
        "bookmark_confirm_remove_all": "Ertu viss um að þú viljir fjarlægja öll {0} bókamerki?",
        "menu_bookmarks": "Bókamerki",
        "bookmark_manage": "Stjórna bókamerkjum",
        "bookmark_next": "Næsta bókamerki",
        "bookmark_prev": "Fyrra bókamerki",
        "bookmark_page_display": "Síða {0}",
        "bookmark_exists": "Bókamerki fyrir þessa síðu með þessu nafni er þegar til staðar.",
        "bookmark_select_first": "Veldu fyrst bókamerki.",
        "bookmark_confirm_remove": "Ertu viss um að þú viljir fjarlægja bókamerkið 'Síða {0}: {1}'?",
        "bookmark_jumped_to": "Farið í bókamerki '{0}' á síðu {1}.",
        "bookmark_jumped_to_voice": "Bókamerki {0}, síða {1}",
        "btn_close": "Loka",

        "bookmark_list": "Bókamerkin þín",
        "bookmark_rename": "Endurnefna bókamerki",
        "bookmark_rename_tooltip": "Breyta nafni valda bókamerkisins",
        "bookmark_rename_title": "Endurnefna bókamerki",
        "bookmark_rename_prompt": "Nýtt nafn fyrir bókamerki á síðu {0}:\n(hámark 50 stafir)",
        "bookmark_renamed": "Bókamerki '{0}' hefur verið endurnefnt í '{1}'.",
        "bookmark_item_tooltip": "Síða {0}: {1}\nTvísmelltu til að fara",
        "bookmark_name_exists_question": "Bókamerki með nafninu '{0}' er þegar til á þessari síðu.\nEndurnefna samt?",

        "context_bookmarks": "Bókamerki",
        "context_bookmark_add_here": "Bæta við bókamerki fyrir þessa síðu",
        "context_bookmarks_existing": "Núverandi bókamerki:",
        "context_bookmarks_jump": "Fara í bókamerki:",
        "context_bookmarks_none": "Engin bókamerki til staðar",
        "context_bookmarks_clear_all": "Fjarlægja öll {0} bókamerki",

        "bookmark_search_placeholder": "Leita að bókamerkjum... (nafn eða síða)",
        "bookmark_search_results": "%d bókamerki fundust fyrir \"%s\"",
        "bookmark_no_search_results": "Engin bókamerki fundust fyrir \"%s\"",
        "bookmark_no_search_results_label": "Engar niðurstöður fyrir \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Breyta PDF lýsigögnum",
        "metadata_title": "Titill",
        "metadata_title_placeholder": "Titill skjals",
        "metadata_title_tooltip": "Titill skjalsins (birtist í titilbar)",
        "metadata_author": "Höfundur",
        "metadata_author_placeholder": "Nafn höfundar",
        "metadata_author_tooltip": "Skapari skjalsins",
        "metadata_subject": "Efni",
        "metadata_subject_placeholder": "Efni skjalsins",
        "metadata_subject_tooltip": "Stutt lýsing á innihaldi",
        "metadata_keywords": "Lykilorð",
        "metadata_keywords_placeholder": "Lykilorð aðskilin með kommum",
        "metadata_keywords_tooltip": "Lykilorð til að flokka skjalið",
        "metadata_creator": "Skapari",
        "metadata_creator_placeholder": "Forritið sem bjó til PDF-ið",
        "metadata_creator_tooltip": "Hugbúnaðurinn sem skjalið var búið til með",
        "metadata_producer": "Framleiðandi",
        "metadata_producer_placeholder": "Forritið sem breytti PDF-inu",
        "metadata_producer_tooltip": "Hugbúnaðurinn sem breytti PDF-inu",
        "metadata_creation_date": "Dagsetning stofnunar",
        "metadata_creation_date_tooltip": "Dagsetning stofnunar skjals",
        "metadata_mod_date": "Breytingadagsetning",
        "metadata_mod_date_tooltip": "Dagsetning síðustu breytingar",
        "metadata_pdf_info": "📄 PDF upplýsingar",
        "metadata_pages": "Fjöldi síðna",
        "metadata_file_size": "Skráarstærð",
        "metadata_pdf_version": "PDF útgáfa",
        "metadata_encrypted": "Dulritað",
        "metadata_encrypted_yes": "Já (verndað með lykilorði)",
        "metadata_encrypted_no": "Nei",
        "metadata_reload": "📂 Endurhlaða úr PDF",
        "metadata_reset": "Hafna breytingum",
        "metadata_reloaded": "Lýsigögnum hefur verið endurhlaðið úr PDF-inu.",
        "metadata_reset_done": "Öllum lýsigagnareitum hefur verið endurstillt.",
        "metadata_no_file": "Engin PDF skrá hlaðin inn.",
        "metadata_save_error": "Villa við að vista lýsigögn",
        "metadata_saved": "Lýsigögnum var vistað með góðum árangri.",
        "metadata_pdf_version_unknown": "PDF (óþekkt)",
        "metadata_saved_message": "Lýsigögnum var vistað með góðum árangri.",
        "metadata_saved_voice": "Lýsigögnum vistað.",

        "metadata_custom": "🔧 Sérsniðin lýsigögn",
        "metadata_custom_placeholder": "{\n  \"minn_reitur\": \"gildi_mitt\",\n  \"annar_reitur\": 123\n}",
        "metadata_custom_tooltip": "JSON snið fyrir sérsniðin lýsigögn (valfrjálst)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Sniðmát \"{0}\" valið - Tvísmelltu til að setja inn",
        "text_use_template": "Nota textablokk",
        "text_type": "Tegund",
        "text_search_templates": "Leita að textablokkum...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Upplýsingar um útflutning / innflutning",
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

        <h3>📦 Hvað er flutt út? (Yfirlit)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Almennar forritsstillingar</span></li>
            <li class="detail">• Dökkur/Ljós hamur</li>
            <li class="detail">• Öfugur dökkur hamur fyrir myndir</li>
            <li class="detail">• Grátt þröskuldsgildi</li>
            <li class="detail">• Tungumál</li>
            <li class="detail">• Glugga rúmfræði</li>
            <li class="detail">• Aðdráttarhamur</li>
            <li class="detail">• Flakk (Flakkstika sýnileg)</li>
            <li class="detail">• Talúttak (kveikt/slökkt)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Öryggisafritunarstillingar</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Skráarheiti (Tímasetning, Aðskiljari, Viðskeyti)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Stillingar fyrir innsetningar</span></li>
            <li class="detail">• Undirskriftir</li>
            <li class="detail">• Texti &amp; textablokkir</li>
            <li class="detail">• Krossar, myndir og form</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR stillingar</span></li>
            <li class="detail">• Tungumál</li>
            <li class="detail">• Þvinga OCR · Síðuhamur</li>
            <li class="detail">• Forvinnsla mynda: Leiðrétta skekkju, Hreinsa, Yfirsýnatöku</li>
            <li class="detail">• Fjöldi samhliða verka</li>
            <li class="detail">• Öfugur hamur</li>
            <li class="detail">• Grátt þröskuldsgildi</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bókamerki</span></li>
            <li class="detail">• Öll bókamerki á PDF skrá (Síða, Nafn, Stofnunartími)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Lykilorðagagnagrunnur</span></li>
            <li class="detail">• Vistuð PDF lykilorð (valkvætt dulrituð eða hreinn texti)</li>
            <li class="detail">• Aðallykilorða kjötkássa (ef sett)</li>
            <li class="detail">• Staðfestingargögn</li>
        </ul>

        <h4>⚠️ Mikilvægar athugasemdir</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Við innflutning:</strong>
            <ul>
                <li><span class="warning">➜ ÖLLUM núverandi stillingum verður skrifað yfir</span></li>
                <li>• Endurræsa þarf forritið</li>
                <li>• Núverandi undirskriftir, textablokkir og bókamerki verða skipt út</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Aðallykilorð og útflutningshamur:</strong>
            <ul>
                <li>• Þegar aðallykilorð er virkt geturðu valið:</li>
                <li>  - <span style="color: #98FB98;"><strong>Afkóðað</strong></span> (lykilorð eru í hreinum texta í ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Dulritað</strong></span> (aðeins læsilegt með aðallykilorði á markkerfinu)</li>
                <li>• Aðallykilorða kjötkássan er <strong>alltaf</strong> geymd dulrituð</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Öryggisathugasemd:</strong>
            <ul>
                <li>• Útflutta ZIP skráin inniheldur viðkvæm gögn (<strong>lykilorð, bókamerki, undirskriftir</strong>)</li>
                <li>• Vinsamlegast geymdu hana á öruggan hátt (t.d. dulritaður USB blettur, lykilorðastjóri)</li>
                <li>• Ef skráin tapast eru vistuð PDF lykilorð glötuð fyrir fullt og allt</li>
            </ul>
        </div>

        <h4>📁 Útflutningssnið</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Stillingarnar eru vistaðar í einni ZIP skrá:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Þetta ZIP inniheldur heildstæða <code>settings.json</code> (úr stillingunum þínum) ásamt mögulega innbyggðum undirskriftarmyndaskrám og dulrituðum lykilorðum.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Undirskriftir - Leiðbeiningar",
        'signature_guide_html': """
        📝 <strong>Undirskriftir - Stutt leiðbeining</strong><br>
        <ul>
        <li>Setja aðallykilorð</li>
        <li>Stilla undirskriftir í <em>Stillingar</em> valmynd (stærð, tímastimpill, …)</li>
        <li>Setja inn með <strong>HÆGRISMELLI</strong> á æskilegan stað (aðallykilorð þarf einu sinni á lotu)</li>
        <li>Færa undirskrift með mús eða örvum</li>
        <li>Setja inn margar undirskriftir í röð</li>
        <li>Sérsníða hverja undirskrift fyrir sig</li>
        <li>Hafna einstakri undirskrift</li>
        <li>Vista / hafna öllum undirskriftum í einu</li>
        <li>Einnig er hægt að nota valmyndastikuna.</li>
        </ul>
        """,
        'signature_guide_voice': "Stutt leiðbeining fyrir undirskriftir. Setja aðallykilorð. Stilla undirskriftir í stillingum. Setja inn með hægrismelli.",

        'image_guide_title': "Setja inn myndir - Leiðbeiningar",
        'image_guide_html': """
        📷 <strong>Setja inn myndir í PDF - Stutt leiðbeining</strong><br>
        <ol>
        <li>Hægrismellur á æskilegum stað</li>
        <li><em>„Setja inn mynd“</em> → Velja mynd</li>
        <li>Staðsetja mynd: Draga með mús</li>
        <li>Stilla stærð: Draga við horn/jaðra</li>
        <li>Varðveita hlutfall: <strong>[A]</strong> takki</li>
        <li>Freari aðlögun: Hægrismellur á mynd</li>
        </ol>
        <p><strong>Ábending:</strong> Í samhengisvalmynd getur þú stillt stillingarnar.</p>
        """,
        'image_guide_voice': "Stutt leiðbeining fyrir myndir. Hægrismellur, setja inn mynd, velja. Staðsetja með mús, stilla stærð við horn. Hlutfall með A takka.",

        'form_guide_title': "Setja inn form - Leiðbeiningar",
        'form_guide_html': """
        📐 <strong>Setja inn form í PDF - Stutt leiðbeining</strong><br>
        <ol>
        <li>Velja formgerð (rétthyrningur, sporbaugur, lína, ör)</li>
        <li>Smella á staðsetningu:
            <ul>
            <li>Fyrir rétthyrning/sporbaug: Einn smellur setur formið</li>
            <li>Fyrir línu/ör: Tveir smellir fyrir upphafs- og endapunkt</li>
            </ul>
        </li>
        <li>Staðsetja form: Draga með mús</li>
        <li>Stilla stærð: Draga við horn/jaðra</li>
        <li>Vista form: <strong>Enter</strong></li>
        <li>Hafna formi: <strong>ESC</strong></li>
        <li>Freari aðlögun: Hægrismellur á formi</li>
        </ol>
        <p><strong>Ábending:</strong> Í samhengisvalmynd getur þú stillt stillingarnar.</p>
        """,
        'form_guide_voice': "Stutt leiðbeining fyrir form. Velja formgerð. Fyrir rétthyrning eða sporbaug smelltu einu sinni, fyrir línu eða ör tvisvar. Staðsetja með mús, stilla stærð við horn. Vista með Enter, hafna með Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "fyrri",
        "btn_next_result": "næsti",
        "ocr_text_window": "OCR textagluggi",
        "bookmark_existing": "Núverandi bókamerki",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR samanburður Mac - Windows",
        'ocr_method_mac_win_title': "OCR munur á Mac og Windows",
        'ocr_method_mac_win_voice': "Mac er betri",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Munur á macOS og Windows</strong></p>

        <p><strong>macOS (mælt með)</strong></p>
        <p>Tól:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Niðurstaða:</p>
        <ul>
        <li>Leitanlegt PDF með innfellt texta sem varðveitir að mestu upprunalegt útlit.</li>
        </ul>
        <p>Kostir:</p>
        <ul>
        <li>Framúrskarandi gæði textaþekkingar (jafnvel á skakklum síðum).</li>
        <li>Varðveisla vigurgrafík og leturgerða.</li>
        <li>GUI framvindustika með undirferlis mati.</li>
        <li>Full stjórn á öllum OCR breytum (Deskew, Clean, Oversample, hagræðing).</li>
        <li>Textaleit er beint aðgengileg í aðalglugga (PDF sýn).</li>
        </ul>
        <p>Ókostir:</p>
        <ul>
        <li>Krefst viðbótarkerfisverkfæra (ocrmypdf, Ghostscript, unpaper, pngquant – innifalið í forritspakkanum).</li>
        <li>Flóknari villumeðhöndlun (stöðvun, tímapör).</li>
        </ul>

        <p><strong>Windows (stöðugur valkostur)</strong></p>
        <p>Tól:</p>
        <ul>
        <li>pytesseract (bein tenging við Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Niðurstaða:</p>
        <ul>
        <li>Leitanlegt PDF sem sjónrænt samsvarar mynda-PDF, en er leitanlegt í gegnum gagnsæjan texta.</li>
        </ul>
        <p>Kostir:</p>
        <ul>
        <li>Engir koma mér í hug um þessar mundir.</li>
        </ul>
        <p>Ókostir:</p>
        <ul>
        <li>PDF er í raun mynd með ósýnilegum texta; útlit getur vikið lítillega í flóknum skjölum (dálkar, töflur).</li>
        <li>Engin sjálfvirk skakkaleiðrétting (--deskew) eða myndhreinsun (--clean).</li>
        <li>GUI framvindustikan er aðeins uppfærð gróflega byggt á fjölda unninna síðna.</li>
        <li>OCR hraði er örlítið hægari (þar sem hver síða er unnin sérstaklega).</li>
        <li>Textaleit er beint í OCR textagluggann.</li>
        </ul>

        <p><strong>Sameiginlegt</strong></p>
        <ul>
        <li>Báðar aðferðir búa til leitanlegt PDF í sömu möppu og upprunaskráin.</li>
        <li>OCR stillingar (tungumál, DPI, síðuskilgreiningarhamur, OCR vélastilling) er hægt að stilla í gegnum OCRSettingsDialog og gilda í báðum útfærslum.</li>
        </ul>

        <p><strong>Meðmæli:</strong></p>
        <ul>
        <li>macOS: ocrmypdf tvinnforritið gefur bestu niðurstöðurnar – Keyptu þér Mac og notaðu útgáfuna (PDFDarkView fyrir Mac með Apple Silicon eða Intel flís). OCR niðurstöður eru betri en á Windows!</li>
        <li>Windows: Notaðu pytesseract lausnina. Hún er stöðug og gefur fullnægjandi gæði fyrir flest skjöl.</li>
        </ul>

        <p><strong>Mikilvæg athugasemd:</strong></p>
        <ul>
        <li>Báðar útgáfur eru fullkomlega samþættar notendaviðmótinu – notandinn tekur ekki eftir neinum mun.</li>
        <li>Forritið ákveður sjálfkrafa hvaða OCR vél sé notuð út frá stýrikerfinu.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Búa til undirskrift (úr skönnun)",
        "signature_create_title": "Veldu skannaða undirskrift (PDF/mynd)",
        "image_pdf_filter": "Myndir og PDF",
        "signature_pdf_empty": "PDF-ið inniheldur engar síður.",
        "signature_created_success": "Undirskrift tókst að búa til: {0}",
        "signature_create_error": "Villa við gerð undirskriftar:\n{0}",
        "rembg_missing": "rembg er ekki uppsett.\nUppsettur: pip install rembg\nVilla: {0}",
        "signature_name_title": "Skráarheiti fyrir undirskrift",
        "signature_name_message": "Sláðu inn skráarheiti fyrir nýju undirskriftina (vistuð sem PNG með gagnsæjum bakgrunni):",
        "signature_name_label": "Skráarheiti:",
        "signature_name_voice": "Sláðu inn skráarheiti fyrir undirskrift",
        "signature_processing": "Vinnsla í gangi...",
        "signature_creation_title": "Undirskrift er gerð",
        "signature_overwrite_warning": "Skráin '{0}' er þegar til. Yfirskrifa?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Undirbúa PDF fyrir undirskrift",
        "signature_prepare_instruction":"Vinsamlegast veldu PDF sem inniheldur á einni síðu skannaða undirskrift.\n\nBestu þekkingu færðu ef:\n• Undirskriftin er skrifuð með svartu bleki (kúlupenna eða fineliner) á hvítum pappír.\n• Undirskriftin er í efsta þriðjungi annars tómu A4 síðunnar.\n• PDF-ið var skannað með að minnsta kosti 300 dpi.\n• Undirskriftin er skýr og ekki of þunn.\n• Engin truflandi bakgrunnsmynstur eða línur eru til staðar.",
        "signature_prepare_voice":"Vinsamlegast veldu PDF með skannaðri undirskrift. Gefðu gaum að góðum gæðum og birtuskilum.",
        "sig_thickness_label":"Línuþykkt:",
        "sig_thickness_normal":"Eðlileg (þunn)",
        "sig_thickness_bold":"Feitletruð (mælt með)",
        "sig_thickness_very_bold":"Mjög feitletruð",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Bæta við GUI og OCR tungumálum - Leiðbeiningar",
        'language_guide_title': "Bæta við GUI og OCR tungumálum",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Sæktu æskilega þýðingarskrá <code>translations_xy.py</code> frá<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        og settu hana í eftirfarandi möppu:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Opnaðu vafrann þinn.</li>
        <li>Farðu á: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Leitaðu hægra megin á skjánum að "Releases" og veldu það sem merkt er <strong>"latest"</strong>.</li>
        <li>Á næstu útgáfusíðu, hladdu niður <code>Source Code.zip</code> skránni neðst.</li>
        <li>Afþjappaðu ZIP skránna.</li>
        <li>Leitaðu í afþjappaða möppunni að öllum tungumálaskrám sem þú þarft og afritaðu þær í möppuna:<br/>
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
        "menu_watermark":"Setja inn vatnsmerki",
        "fullpage_text_watermark_title":"Texti sem vatnsmerki",
        "fullpage_image_watermark_title":"Mynd sem vatnsmerki",
        "filename_with_watermark":"_með_vatnsmerki",
        "watermark_text":"Texti:",
        "watermark_text_placeholder":"Vatnsmerkjatextinn þinn...",
        "watermark_font_family":"Leturgerð:",
        "watermark_font_size":"Leturstærð:",
        "watermark_format":"Snið:",
        "watermark_bold":"Feitletrað",
        "watermark_italic":"Skáletrað",
        "watermark_color":"Litur:",
        "watermark_choose_color":"Veldu lit...",
        "watermark_opacity":"Þéttleiki / Gagnsæi:",
        "watermark_direction":"Lestrarstefna:",
        "watermark_direction_l_r":"Vinstri → Hægri",
        "watermark_direction_bl_tr":"Neðst vinstri → Efst hægri",
        "watermark_direction_tl_br":"Efst vinstri → Neðst",
        "watermark_direction_b_t":"Neðst → Efst",
        "watermark_direction_t_b":"Efst → Neðst",
        "watermark_preview":"Forsýn:",
        "watermark_preview_sample":"Dæmi um texta",
        "watermark_empty_text":"Vinsamlegast sláðu inn texta.",
        "watermark_applied":"Vatnsmerki hefur verið sett á allar síður.",
        "watermark_saved":"Vatnsmerki vistað.",
        "image_scale":"Stærð:",
        "image_preview":"Forsýn myndar:",
        "no_image_selected":"Engin mynd valin",
        "browse":"Flettu...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Eyðingar",
        "redact_add_black": "Eyðing (svart)",
        "redact_add_white": "Eyðing (hvítt / stroka)",
        "redact_added_black": "Svartri eyðingu bætt við",
        "redact_added_white": "Hvítri eyðingu bætt við",
        "redact_apply_all": "Beita öllum eyðingum og vista",
        "redact_discard_all": "Hafna öllum eyðingum",
        "redact_discard": "Hafna þessari eyðingu",
        "no_redactions": "Engar eyðingar",
        "redact_confirm_title": "Beita eyðingum varanlega",
        "redact_confirm_message": "Viðvörun: Merkt svæði verða varanlega eytt (svart eða hvítt).\nÖryggisafrit verður búið til (ef virkjað).\n\nHalda áfram?",
        "redact_apply": "Já, eyða núna",
        "redact_saved": "{0} eyðingu(um) var beitt og vistað.",
        "redact_saved_voice": "{0} eyðingu(um) beitt",
        "redact_error": "Villa við eyðingu",
        "filename_redacted":"_eytt",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Setja inn síðunúmer',
        'page_numbers_format': 'Númerasnið:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabískt)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (rómverskt lágstafir)',
        'page_numbers_format_roman_upper': 'I, II, III ... (rómverskt hástafir)',
        'page_numbers_format_letter': 'A, B, C ... (stafir)',
        'page_numbers_format_custom': 'Sérsniðið',
        'page_numbers_custom_pattern': 'Mynstur:',
        'page_numbers_custom_placeholder': 't.d. "Síða {nummer}" eða "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Notaðu {nummer} fyrir núverandi síðunúmer og {total} fyrir heildarfjölda',
        'page_numbers_position': 'Staðsetning:',
        'page_numbers_pos_tl': 'Efst vinstri',
        'page_numbers_pos_tc': 'Efst miðju',
        'page_numbers_pos_tr': 'Efst hægri',
        'page_numbers_pos_ml': 'Miðju vinstri',
        'page_numbers_pos_mc': 'Miðjað',
        'page_numbers_pos_mr': 'Miðju hægri',
        'page_numbers_pos_bl': 'Neðst vinstri',
        'page_numbers_pos_bc': 'Neðst miðju',
        'page_numbers_pos_br': 'Neðst hægri',
        'page_numbers_margins': 'Jaðrar:',
        'page_numbers_margin_x': 'Lárétt fjarlægð:',
        'page_numbers_margin_y': 'Lóðrétt fjarlægð:',
        'page_numbers_range': 'Síðubil:',
        'page_numbers_all_pages': 'Allar síður',
        'page_numbers_custom_range': 'Sérsniðið bil',
        'page_numbers_from': 'Frá:',
        'page_numbers_to': 'Til:',
        'page_numbers_progress': 'Set inn síðunúmer...',
        'page_numbers_start': 'Ræsi innsetningu síðunúmera...',
        'page_numbers_cancel': 'Innsetningu síðunúmera hætt',
        'page_numbers_success': 'Síðunúmerum var bætt við.\n\nViltu opna nýja PDF-skrána?\n\n{0}',
        'page_numbers_complete': 'Síðunúmerum bætt við',
        'page_numbers_error_format': 'Villa við innsetningu síðunúmera: {0}',
        'page_numbers_content_type': 'Tegund efnis:',
        'page_numbers_tab_simple': 'Einfalt númer',
        'page_numbers_tab_range': 'Síða X af Y',
        'page_numbers_tab_date': 'Dagsetning',
        'page_numbers_tab_custom': 'Frjáls texti',
        'page_numbers_range_format': 'Snið:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Síða {aktuell} af {gesamt}',
        'page_numbers_range_custom': 'Sérsniðið',
        'page_numbers_range_placeholder': 't.d. "Síða {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Dagsetningasnið:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. janúar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Sérsniðið',
        'page_numbers_date_placeholder': 't.d. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Staðsetning:',
        'page_numbers_date_before': 'Dagsetning fyrir síðunúmer',
        'page_numbers_date_after': 'Dagsetning á eftir síðunúmeri',
        'page_numbers_date_only': 'Aðeins dagsetning (án síðunúmers)',
        'page_numbers_custom_text': 'Sérsniðinn texti:',
        'page_numbers_custom_placeholder_text': 'Notaðu {seite} fyrir síðunúmer og {gesamt} fyrir heildarfjölda\nt.d. "Trúnaðarmál - Síða {seite}" eða "{seite} af {gesamt}"',
        "filename_with_page_number":"_með_síðunúmeri",
        "filename_with_page_declaration":"_með_síðuyfirlýsingu",
        "filename_with_pagenumber":"_með_síðunúmeri",
        "filename_with_date":"_með_dagsetningu",
        "filename_with_my_page_declaration":"_með_sérsniðinni_síðuyfirlýsingu",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Óvistaðar breytingar",
        "unsaved_changes_message_darkmode": "Það eru óvistaðar innsetningar.\nViltu vista þær áður en þú skiptir?",
        "save_and_switch": "Vista og skipta",
        "discard_and_switch": "Skipta núna",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Flytja út síður sem myndir',
        'export_images_menu': 'Flytja út sem myndir (PNG/JPEG)',
        'export_images_format': 'Myndasnið:',
        'export_images_dpi': 'Upplausn (DPI):',
        'export_images_quality': 'JPEG gæði:',
        'export_images_range': 'Síðubil:',
        'export_images_all_pages': 'Allar síður',
        'export_images_custom_range': 'Sérsniðið bil',
        'export_images_from': 'Frá:',
        'export_images_to': 'Til:',
        'export_images_options': 'Valkostir:',
        'export_images_single_files': 'Hver síða sem sérstök skrá',
        'export_images_subfolder': 'Flytja út í undirmöppu',
        'export_images_subfolder_info': 'Í undirmöppu "PDFnafn_myndir"',
        'export_images_same_folder': 'Í sömu möppu og PDF',
        'export_images_apply_darkmode': 'Beita PDFDarkView stillingum (Dökkur hamur)',
        'export_images_target_folder': 'Markmappa:',
        'export_images_browse': 'Flettu...',
        'export_images_preview': 'Forsýn:',
        'export_images_preview_info': 'Veldu stillingar fyrir útflutning',
        'export_images_preview_info_detail': '{0} síður sem {1}\nUpplausn: {2} DPI\nSkráarheiti: {3}\n{4}',
        'export_images_select_folder': 'Veldu markmöppu',
        'export_images_start': 'Ræsi útflutning mynda...',
        'export_images_progress': 'Flyt út myndir...',
        'export_images_saving': 'Vista síðu {0} af {1}...',
        'export_images_success': 'Útflutningur tókst!\n\n{0} myndum var vistað í:\n{1}',
        'export_images_complete': 'Útflutningi mynda lokið',
        'export_images_open_folder': '📁 Opna möppu',
        'export_images_cancel': 'Útflutningi mynda hætt',
        'export_images_error_format': 'Villa við útflutning mynda: {0}',
        'export_images_pdf2image_missing': 'Safnið "pdf2image" er ekki uppsett.\n\nVinsamlegast uppsettu það með:\npip install pdf2image\n\nFyrir Windows þarftu einnig Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A umbreyting fyrir langtímageymslu',
        'pdfa_menu': 'PDF/A umbreyting (tilbúið fyrir geymslu)',
        'pdfa_info': 'Umbreytir PDF skránni í PDF/A snið.\n\nPDF/A er sérstaklega hannað fyrir langtímageymslu og tryggir að skjalið birtist rétt í framtíðinni.',
        'pdfa_standard': 'PDF/A staðall:',
        'pdfa_standard_select': 'Útgáfa:',
        'pdfa_1': 'PDF/A-1 (einfalt, víðtækt samhæft)',
        'pdfa_2': 'PDF/A-2 (nútímalegra, betri þjöppun)',
        'pdfa_3': 'PDF/A-3 (nýjasta útgáfa, leyfir viðhengi)',
        'pdfa_standards_explanation': '📖 Skýring á stöðlum:\n\n'
            '• PDF/A-1: Grunnur, samhæft við eldri kerfi (um 2005)\n'
            '• PDF/A-2: Nútímalegra, betri þjöppun, stuðningur við gagnsæi (um 2011)\n'
            '• PDF/A-3: Nýjasta útgáfa, leyfir innfellingu viðhengja (um 2013)\n\n'
            'Ráðlegging: PDF/A-2 er góð málamiðlun milli samhæfni og nútímalegra eiginleika.',
        'pdfa_options': 'Valkostir:',
        'pdfa_compress_enable': 'Þjappa PDF (minni skrá)',
        'pdfa_metadata_preserve': 'Varðveita lýsigögn (titill, höfundur osfrv.)',
        'pdfa_target_folder': 'Markmappa:',
        'pdfa_browse': 'Flettu...',
        'pdfa_select_folder': 'Veldu markmöppu',
        'pdfa_ocr_info_unknown': '🔍 Gat ekki athugað textainnihald.',
        'pdfa_ocr_info_not_needed': '✅ Texti tiltækur - OCR er ekki nauðsynlegt.\nPDF/A er hægt að búa til beint.',
        'pdfa_ocr_info_recommended': '⚠️ Ekki fannst nægjanlegur texti.\n\nFyrir leitanleg PDF mælum við með að keyra OCR fyrst.\nAthugið: PDF/A virkar án OCR - en textinn verður ekki leitanlegur.',
        'pdfa_ocr_info_error': '❌ Villa við athugun: {0}',
        'pdfa_start': 'Ræsi PDF/A umbreytingu...',
        'pdfa_progress': 'PDF/A umbreyting í gangi...',
        'pdfa_success': 'PDF/A umbreyting tókst!\n\nVistað sem:\n{0}\n\nViltu opna nýju PDF-skrána?',
        'pdfa_complete': 'PDF/A umbreytingu lokið',
        'pdfa_cancel': 'PDF/A umbreytingu hætt',
        'pdfa_error_format': 'Villa við PDF/A umbreytingu:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Safnið "ocrmypdf" er ekki uppsett.\n\nVinsamlegast uppsettu það með:\npip install ocrmypdf',
        'btn_convert': 'Umbreyta',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Hagræða PDF (minnka skráarstærð)',
        'optimize_menu': 'Hagræða PDF (skráarstærð)',
        'optimize_info': 'Minnkar skráarstærð PDF skrárinnar með ýmsum hagræðingaraðferðum.\n\nÞví hærra sem þjöppunarstigið er, því minni verður skráin - með mögulegu gæðatapi í myndum.',
        'optimize_level': 'Þjöppunarstig:',
        'optimize_level_low': 'Lágt (hratt, lítil sparnaður)',
        'optimize_level_medium': 'Miðlungs (góð málamiðlun)',
        'optimize_level_high': 'Hátt (mikill sparnaður)',
        'optimize_level_maximum': 'Hámark (hámarks sparnaður, hægt)',
        'optimize_level_explanation': 'Ráðlegging: "Miðlungs" er góð málamiðlun milli hraða og skráarstærðar.',
        'optimize_options': 'Valkostir:',
        'optimize_compress_images': 'Þjappa myndum (minnka JPEG gæði)',
        'optimize_clean_objects': 'Fjarlægja ónotaða hluti',
        'optimize_preserve_metadata': 'Varðveita lýsigögn (titill, höfundur osfrv.)',
        'optimize_image_quality': 'Myndgæði:',
        'optimize_range': 'Síðubil:',
        'optimize_all_pages': 'Allar síður',
        'optimize_custom_range': 'Sérsniðið bil',
        'optimize_from': 'Frá:',
        'optimize_to': 'Til:',
        'optimize_target_folder': 'Markmappa:',
        'optimize_browse': 'Flettu...',
        'optimize_select_folder': 'Veldu markmöppu',
        'optimize_info_box': 'Upplýsingar',
        'optimize_info_text': 'Hagræðing getur tekið nokkrar mínútur fyrir stórar PDF skrár.\n\nMyndum er vistað með minni gæðum, sem getur dregið verulega úr skráarstærð.',
        'optimize_start': 'Ræsi PDF hagræðingu...',
        'optimize_progress': 'Hagræði PDF...',
        'optimize_cancel': 'PDF hagræðingu hætt',
        'optimize_complete': 'PDF hagræðingu lokið',
        'optimize_error_format': 'Villa við PDF hagræðingu:\n\n{0}',
        'optimize_success_message': 'PDF hagræðing tókst!\n\nVistað sem:\n{0}\n\nÁður: {1}\nEftir: {2}\nSparnaður: {3:.1f}%\n\n{4}\n\nViltu opna hagræddu PDF-skrána?',
        'optimize_success_message_no_size': 'PDF hagræðing tókst!\n\nVistað sem:\n{0}\n\nUpplýsingar um stærð ekki tiltækar.\n\nViltu opna hagræddu PDF-skrána?',
        'optimize_result_positive': 'Skráin minnkaði um {0:.1f}%.',
        'optimize_result_zero': 'Engin breyting á skráarstærð.',
        'optimize_result_negative': 'Skráin stækkaði um {0:.1f}%.\nHagræðingu sleppt, upprunaleg skrá varðveitt.',
        'btn_optimize': 'Ræsa hagræðingu',
        'filename_optimize_low_suffix': '_hagrætt_lágt',
        'filename_optimize_medium_suffix': '_hagrætt',
        'filename_optimize_high_suffix': '_hagrætt_hátt',
        'filename_optimize_maximum_suffix': '_hagrætt_hámark',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Skera PDF',
        'crop_menu': 'Skera PDF (Crop)',
        'crop_range': 'Beita á:',
        'crop_all_pages': 'Allar síður',
        'crop_current_page': 'Aðeins núverandi síða',
        'crop_values': 'Skurðargildi (í punktum):',
        'crop_left': 'Vinstri:',
        'crop_right': 'Hægri:',
        'crop_top': 'Efst:',
        'crop_bottom': 'Neðst:',
        'crop_presets': 'Forstillt:',
        'crop_preset_white': 'Greina hvíta jaðra',
        'crop_reset': 'Endurstilla',
        'crop_mouse_hint': '🖱️ Dragðu rétthyrning til að velja svæðið gróflega.\nSíðan geturðu stillt gildin nákvæmlega í SpinBoxunum.\nHandvirk stilling með mús er ekki möguleg.',
        'crop_apply': 'Skera',
        'crop_scope_all': 'Allar síður',
        'crop_scope_current': 'Núverandi síða',
        'crop_new_size': 'Ný stærð: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Engin PDF hlaðin',
        'crop_preview_error': 'Villa við að hlaða forskoðun',
        'crop_start': 'Ræsi skurð...',
        'crop_progress': 'Skera PDF...',
        'crop_success': 'PDF skorin með góðum árangri!\n\nVistað sem:\n{0}\n\nViltu opna skornu PDF-skrána?',
        'crop_complete': 'Skurði lokið',
        'crop_cancel': 'Skurði hætt',
        'crop_error_format': 'Villa við skurð:\n\n{0}',
        'filename_crop_suffix': '_skorin',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Slétta PDF (Flatten)',
        'flatten_menu': 'Slétta PDF (Flatten)',
        'flatten_info': 'Að slétta PDF "brennir" öllum breytanlegum þáttum inn í síðuefnið.\n\nEftir það eru formareitir, skýringar, textar, krossar, undirskriftir, myndir og form ekki lengur breytanleg hvert fyrir sig.',
        'flatten_explanation_title': '📖 Hverju er þetta gagnlegt?',
        'flatten_explanation_text': 'Slétting er nauðsynleg í eftirfarandi tilvikum:\n\n'
            '• 📄 Þú vilt undirbúa skjalið fyrir prentun\n'
            '• 🔒 Þú vilt koma í veg fyrir að einhver breyti formareitum\n'
            '• 📎 Þú vilt "fella" skýringar og athugasemdir varanlega inn í skjalið\n'
            '• 🖼️ Þú vilt festa texta, krossa, undirskriftir, myndir og form varanlega í skjalinu\n'
            '• 📦 Þú vilt undirbúa skrána fyrir geymslu\n\n'
            'Slétting gerir PDF minni og kemur í veg fyrir að þættir séu færðir eða eytt fyrir slysni.',
        'flatten_what_title': 'Hvað er sléttað?',
        'flatten_what_list': '• ✅ Formareitir (textareitir, gátreitir, hnappar)\n'
            '• ✅ Skýringar (athugasemdir, áherslur, minnispunktar)\n'
            '• ✅ Yfirlög (textar, krossar, undirskriftir, myndir, form)',
        'flatten_options': 'Valkostir:',
        'flatten_forms': 'Slétta formareiti',
        'flatten_annotations': 'Slétta skýringar',
        'flatten_overlays': 'Slétta yfirlög (textar, krossar, undirskriftir, myndir, form)',
        'flatten_target_folder': 'Markmappa:',
        'flatten_browse': 'Flettu...',
        'flatten_select_folder': 'Veldu markmöppu',
        'flatten_warning': '⚠️ Mikilvægt: Slétting er óafturkræft ferli!\n\nEftir sléttingu er ekki hægt að breyta eða eyða breytanlegum þáttum hver fyrir sig.\nBúðu til öryggisafrit fyrirfram ef nauðsynlegt.',
        'flatten_apply': 'Slétta',
        'flatten_start': 'Ræsi sléttingu...',
        'flatten_progress': 'Slétti PDF...',
        'flatten_success': 'PDF slétt með góðum árangri!\n\nVistað sem:\n{0}\n\nViltu opna sléttu PDF-skrána?',
        'flatten_complete': 'Sléttingu lokið',
        'flatten_cancel': 'Sléttingu hætt',
        'flatten_error_format': 'Villa við sléttingu:\n\n{0}',
        'filename_flatten_suffix': '_slétt',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Yfirlag PDF (Overlay)',
        'overlay_menu': 'Yfirlag PDF (Overlay)',
        'overlay_info': 'Setur eina PDF (yfirlag) ofan á aðra PDF.\n\nYfirlags PDF skráin er sett ofan á grunn-PDF. Þetta er gagnlegt fyrir vatnsmerki, lógó, bréfhausa eða stimpla.',
        'overlay_explanation_title': '📖 Hverju er þetta gagnlegt?',
        'overlay_explanation_text': 'Yfirlag er nauðsynlegt í eftirfarandi tilvikum:\n\n'
            '• 🏢 Setja lógó fyrirtækis sem vatnsmerki á hverja síðu\n'
            '• 📄 Setja bréfhaus á tóma PDF\n'
            '• 🖊️ Setja stimpil yfirlag á skjal\n'
            '• 🔖 Setja vatnsmerki á allar síður\n'
            '• 📑 Setja form yfirlag á sniðmát',
        'overlay_type': 'Tegund yfirlags:',
        'overlay_type_fullpage': 'Heil síða (þekjandi)',
        'overlay_type_transparent': 'Heil síða (gagnsætt - mælt með)',
        'overlay_type_stamp': 'Stimpill (staðsetjanlegur)',
        'overlay_type_info_fullpage': '📄 Yfirlags PDF er sett nákvæmlega yfir alla síðuna.\nHægt er að fjarlægja hvíta bakgrunninn svo aðeins efnið sé sýnilegt.',
        'overlay_type_info_transparent': '🔍 Yfirlags PDF er sett yfir alla síðuna með gagnsæjum bakgrunni.\nHvíti bakgrunnurinn er fjarlægður sjálfkrafa - fullkomið fyrir vatnsmerki og lógó!',
        'overlay_type_info_stamp': '🖊️ Yfirlags PDF er staðsett og skölum sem stimpill.\nFullkomið fyrir lógó, stimpla eða undirskriftir á ákveðnum stöðum.',
        'overlay_remove_background': 'Fjarlægja hvítan bakgrunn:',
        'overlay_remove_background_enable': 'Fjarlægja hvítan bakgrunn úr yfirlags PDF (gerir yfirlagið gagnsætt)',
        'overlay_remove_background_tooltip': 'Fjarlægir hvít svæði úr yfirlags PDF svo að undirliggjandi texti verði sýnilegur.',
        'overlay_threshold': 'Þröskuldsgildi:',
        'overlay_threshold_hint': '(1-254, hærra = meira hvítt er fjarlægt)',
        'overlay_select_file': 'Veldu yfirlags PDF:',
        'overlay_file_placeholder': 'Vinsamlegast veldu PDF skrá fyrir yfirlagið',
        'overlay_browse': 'Flettu...',
        'overlay_select_overlay': 'Veldu yfirlags PDF',
        'overlay_range': 'Síðubil:',
        'overlay_all_pages': 'Allar síður',
        'overlay_custom_range': 'Sérsniðið bil',
        'overlay_from': 'Frá:',
        'overlay_to': 'Til:',
        'overlay_position': 'Staðsetning:',
        'overlay_position_center': 'Miðja',
        'overlay_position_top_left': 'Efst vinstri',
        'overlay_position_top_right': 'Efst hægri',
        'overlay_position_bottom_left': 'Neðst vinstri',
        'overlay_position_bottom_right': 'Neðst hægri',
        'overlay_size': 'Stærð:',
        'overlay_size_original': 'Upprunaleg stærð',
        'overlay_size_fit_page': 'Aðlaga að síðu',
        'overlay_size_custom': 'Sérsniðið (%)',
        'overlay_opacity': 'Gagnsæi:',
        'overlay_target_folder': 'Markmappa:',
        'overlay_browse_folder': 'Flettu...',
        'overlay_select_folder': 'Veldu markmöppu',
        'overlay_warning': '⚠️ Athugið: Yfirlags PDF er sett ofan á grunn-PDF og "brennt" inn í hana.\n\nÞættir yfirlags PDF geta ekki lengur verið breyttir hver fyrir sig eftir vistun.',
        'overlay_apply': 'Yfirlag',
        'overlay_start': 'Ræsi yfirlag...',
        'overlay_progress': 'Set yfirlag á PDF...',
        'overlay_success': 'PDF yfirlag sett með góðum árangri!\n\nVistað sem:\n{0}\n\nViltu opna PDF skrána með yfirlagi?',
        'overlay_complete': 'Yfirlagi lokið',
        'overlay_cancel': 'Yfirlagi hætt',
        'overlay_error_format': 'Villa við yfirlag:\n\n{0}',
        'overlay_no_file': 'Engin yfirlags PDF valin.\n\nVinsamlegast veldu PDF skrá fyrir yfirlag.',
        'filename_overlay_suffix': '_með_yfirlagi',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Draga myndir úr PDF',
        'extract_images_menu': 'Draga allar myndir',
        'extract_images_info': 'Dregur allar myndir úr PDF og vistar þær sem sérstakar skrár.\n\nMyndir eru vistaðar í upprunalegu sniði eða breytt í valið snið.',
        'extract_images_format': 'Myndasnið:',
        'extract_images_quality': 'JPEG gæði:',
        'extract_images_options': 'Valkostir:',
        'extract_images_subfolder': 'Draga í undirmöppu ("PDFnafn_myndir")',
        'extract_images_unique': 'Aðeins einstakar myndir (forðast tvírit)',
        'extract_images_range': 'Síðubil:',
        'extract_images_all_pages': 'Allar síður',
        'extract_images_custom_range': 'Sérsniðið bil',
        'extract_images_from': 'Frá:',
        'extract_images_to': 'Til:',
        'extract_images_target_folder': 'Markmappa:',
        'extract_images_browse': 'Flettu...',
        'extract_images_select_folder': 'Veldu markmöppu',
        'extract_images_info_box': 'Upplýsingar',
        'extract_images_info_text': 'Útdráttur getur tekið nokkrar mínútur fyrir stórar PDF skrár.\n\nMyndum er vistað með upprunalegu heiti (síða_mynd).',
        'extract_images_extract': 'Draga út',
        'extract_images_start': 'Ræsi útdrátt...',
        'extract_images_progress': 'Dreg myndir...',
        'extract_images_success': '✅ Myndir dregnar út með góðum árangri!\n\n{0} myndum var vistað í:\n{1}',
        'extract_images_complete': 'Útdrætti mynda lokið',
        'extract_images_cancel': 'Útdrætti hætt',
        'extract_images_error_format': 'Villa við útdrátt mynda:\n\n{0}',
        'extract_images_open_folder': '📁 Opna möppu',
        'extract_images_no_images': 'Engar myndir fundust í PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Fleiri síður á einni síðu (N-Up)',
        'nup_menu': 'Fleiri síður á einni síðu (N-Up)',
        'nup_info': 'Raðar mörgum PDF síðum á eina síðu.\n\nTilvalið fyrir þéttar prentanir, yfirlit eða handbækur.',
        'nup_layout': 'Skipulag:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Forsýn:',
        'nup_preview_info': '{0} síður → {1} síður á blað → {2} blöð\nSkipulag: {3}',
        'nup_order': 'Röð:',
        'nup_order_horizontal': 'Lárétt (röð fyrir röð)',
        'nup_order_vertical': 'Lóðrétt (dálkur fyrir dálk)',
        'nup_order_horizontal_reverse': 'Lárétt öfugt',
        'nup_order_vertical_reverse': 'Lóðrétt öfugt',
        'nup_range': 'Síðubil:',
        'nup_all_pages': 'Allar síður',
        'nup_custom_range': 'Sérsniðið bil',
        'nup_from': 'Frá:',
        'nup_to': 'Til:',
        'nup_options': 'Valkostir:',
        'nup_margins': 'Jaðrar:',
        'nup_margin_between': 'Bil milli síðna:',
        'nup_page_numbers': 'Setja inn síðunúmer',
        'nup_target_folder': 'Markmappa:',
        'nup_browse': 'Flettu...',
        'nup_select_folder': 'Veldu markmöppu',
        'nup_create': 'Búa til',
        'nup_start': 'Ræsi N-Up...',
        'nup_progress': 'Bý til N-Up...',
        'nup_success': 'N-Up búið til með góðum árangri!\n\nVistað sem:\n{0}\n\nViltu opna nýju PDF-skrána?',
        'nup_complete': 'N-Up lokið',
        'nup_cancel': 'N-Up hætt',
        'nup_error_format': 'Villa við N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Breyta síðustærð',
        'pagesize_menu': 'Breyta síðustærð',
        'pagesize_info': 'Breyttir síðustærð PDF skrárinnar.\n\nEfnið aðlagast sjálfkrafa nýrri stærð.',
        'pagesize_format': 'Snið:',
        'pagesize_select': 'Veldu staðlað snið:',
        'pagesize_custom': 'Sérsniðin stærð:',
        'pagesize_width': 'Breidd:',
        'pagesize_height': 'Hæð:',
        'pagesize_orientation': 'Stefna:',
        'pagesize_portrait': 'Andlitsmynd',
        'pagesize_landscape': 'Álagsmynd',
        'pagesize_scale_options': 'Skölunarvalkostir:',
        'pagesize_fit': 'Aðlaga (halda hlutfalli)',
        'pagesize_stretch': 'Teygja (afmynda)',
        'pagesize_center': 'Miðja (upprunaleg stærð)',
        'pagesize_range': 'Síðubil:',
        'pagesize_all_pages': 'Allar síður',
        'pagesize_custom_range': 'Sérsniðið bil',
        'pagesize_from': 'Frá:',
        'pagesize_to': 'Til:',
        'pagesize_target_folder': 'Markmappa:',
        'pagesize_browse': 'Flettu...',
        'pagesize_select_folder': 'Veldu markmöppu',
        'pagesize_apply': 'Beita',
        'pagesize_start': 'Ræsi breytingu á síðustærð...',
        'pagesize_progress': 'Breyti síðustærð...',
        'pagesize_success': 'Síðustærð breytt með góðum árangri!\n\nVistað sem:\n{0}\n\nViltu opna nýju PDF-skrána?',
        'pagesize_complete': 'Breytingu á síðustærð lokið',
        'pagesize_cancel': 'Breytingu á síðustærð hætt',
        'pagesize_error_format': 'Villa við breytingu á síðustærð:\n\n{0}',
        'pagesize_preview_info': 'Ný stærð: {0} x {1} pt',
        'filename_pagesize_suffix': '_ný_stærð',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF upplýsingar',
        'pdf_info_menu': 'Sýna PDF upplýsingar',
        'pdf_info_voice': 'Sýni PDF upplýsingar',
        'pdf_info_error': 'Villa við að sýna PDF upplýsingar:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Sýna flýtileiðir á lyklaborði",
        "shortcuts_dialog_title": "Flýtileiðir á lyklaborði",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 SKRÁ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Opna PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Loka PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Vista sem...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Vernda skjal</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Prenta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Prenta strax (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Hætta í forriti</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 FLYTJA ÚT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Flytja út sem Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Flytja út sem DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Flytja út sem TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Flytja út sem myndir (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Draga myndir</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ VINNSLA SKJALA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Fleiri síður)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A umbreyting (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Slétta PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Yfirlag PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Hagræða PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ BREYTA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Leita</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Bæta við bókamarki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Stjórna bókamerkjum</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Næsta bókamerki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Fyrra bókamerki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Keyra OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SÍÐUSTJÓRNUN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Snúa núverandi síðu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Snúa öllum síðum</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Eðlileg gera núverandi síðu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Eðlileg gera allar síður</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Eyða síðum</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Draga síður</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Setja inn síður</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Færa síður</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Sameina PDF skrár</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Breyta síðustærð</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 SETJA INN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Setja inn texta</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Setja inn kross</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Setja inn undirskrift 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Setja inn undirskrift 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Setja inn mynd</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Setja inn rétthyrning</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Setja inn sporbaug</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Setja inn línu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Setja inn ör</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Setja inn síðunúmer</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Texta vatnsmerki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Mynd vatnsmerki</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ EYDINGAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Eyðing (svart)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Eyðing (hvítt)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Beita öllum eyðingum</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ÍTAREÐI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Skera PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Breyta lýsigögnum</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ SÝN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Víxla á milli Dökkra/Ljóss hams</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Sýna textaglugga</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Síðubreidd (Aðdráttur)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Tvær síður (Aðdráttur)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Yfirlit (Aðdráttur)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ STILLINGAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Lykilorðastjórnun</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR stillingar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Undirskriftarstillingar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Snið skráarheita</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Flytja út stillingar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Flytja inn stillingar</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ UPPLÝSINGAR</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Sýna PDF upplýsingar</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Víxla raddúttaki</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Einbeita á valmyndastiku</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Ný útgáfa í boði",
        "update_available_message": "Ný útgáfa <b>{0}</b> er í boði.\n\nFarðu á útgáfusíðuna til að sækja uppfærsluna:\n{1}",
        "update_available_voice": "Ný útgáfa {0} í boði. Sæktu uppfærsluna af GitHub síðunni.",
        "update_open_release": "Opna útgáfusíðu",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Sækja allar þýðingar",
        "ask_download_all_translations": """Auk þýsku, ensku og víetnömsku eru {total_languages} önnur GUI tungumál í boði.\n\nÆtti að útvega / uppfæra þau?\n\nAthugasemd:\nÞú getur síðar eytt óþarfa tungumálum handvirkt í möppunni:\n{translations_path}
        \nEf þú hættir við geturðu sótt GUI tungumálin síðar í gegnum valmyndina 'Verkfæri → Uppfæra þýðingar'.""",
        "menu_update_translations": "Uppfæra þýðingar",
        "translations_updated": "Þýðingar uppfærðar",
        "translations_update_success": "{} þýðingar voru uppfærðar ({} nýjar, {} uppfærðar).",
        "translations_update_error": "Villa við uppfærslu þýðinga",
        "translations_update_no_changes": "Allar þýðingar eru þegar uppfærðar.",
        "translations_update_offline": "Engin nettenging. Ekki var hægt að uppfæra þýðingar.",
        "translations_update_in_progress": "Þýðingar eru uppfærðar í bakgrunni...",
        "translations_downloading": "Sæki þýðingar...",
        "translations_path_hint": "Notendamappa fyrir þýðingar",
        "translations_update_not_available_title": "Uppfærsla ekki tiltæk",
        "translations_update_not_available_message": """Uppfærsla þýðinga er aðeins tiltæk í uppsettu útgáfunni.\n\nÍ þróunarham eru þýðingar þegar uppfærðar.""",
        "translations_update_no_internet_title": "Engin nettenging",
        "translations_update_no_internet_message": """Ekki var hægt að koma á nettengingu.\n\nEkki er hægt að sækja þýðingar frá GitHub.\n\nMögulegar lausnir:
        • Athugaðu nettenginguna þína
        • Slökktu tímabundið á eldvegg
        • Reyndu aftur síðar
        \nÞú getur einnig sótt þýðingarnar handvirkt frá GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Uppfærsla er þegar í gangi",
        "btn_retry": "Reyna aftur",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Velkomin(n) í PDF Dark View",
        "welcome_title_not_supported": "Velkomin(n) í PDF Dark View",
        "welcome_message": "Velkomin(n) í PDF Dark View!\n\nKerfismálið þitt var greint sem '{language}'.\nViltu nota þetta tungumál fyrir notendaviðmótið?\n\nÞú getur breytt tungumálinu hvenær sem er í 'Stillingar → Tungumál'.",
        "welcome_message_language_not_available": "Velkomin(n) í PDF Dark View!\n\nKerfismálið þitt var greint sem '{language}'.\nÞetta tungumál er ekki enn uppsett.\n\nViltu sækja þýðingarnar fyrir {language} núna frá GitHub?\n\n(Tungumálið verður síðan sjálfkrafa notað fyrir notendaviðmótið.)",
        "welcome_message_language_not_supported": "Velkomin(n) í PDF Dark View!\n\nKerfismálið þitt var greint sem '{language}'.\nÞví miður eru engar þýðingar fyrir þetta tungumál ennþá.\n\nNotendaviðmótið verður birt á {fallback_language}.\n\nÞú getur breytt tungumálinu hvenær sem er í 'Stillingar → Tungumál'.\nEf þú vilt geturðu einnig lagt til þýðingu fyrir tungumálið þitt:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Já, nota kerfismál",
        "welcome_keep_english": "Nei, halda ensku",
        "welcome_download_language": "Já, sækja {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Forritið lokar",

    }
