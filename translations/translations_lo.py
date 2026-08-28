
#  ============================================
# translations_lo.py - Laotisches Wörterbuch
# Vollständig sortiert nach Kategorien
# ============================================

def load_lao_strings():
    """Lädt alle laotischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View ໂດຍ BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "ເປີດ PDF",
        'btn_text_window': "ຂໍ້ຄວາມ OCR",
        'btn_first': "ໜ້າທຳອິດ",
        'btn_prev': "ໜ້າກ່ອນໜ້າ",
        'btn_next': "ໜ້າຕໍ່ໄປ",
        'btn_last': "ໜ້າສຸດທ້າຍ",
        'btn_print': "ພິມ",
        'btn_darkmode_light': "ໂໝດສະຫວ່າງ",
        'btn_darkmode_dark': "ໂໝດມືດ",
        'btn_delete_pages': "ລຶບໜ້າ",
        'btn_extract_pages': "ສະກັດໜ້າ",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "ຕົກລົງ",
        'btn_cancel': "ຍົກເລີກ",
        'btn_save': "ບັນທຶກ",
        'btn_close': "ປິດ",
        'btn_delete': "ລຶບ",
        'btn_delete_all': "ລຶບທັງໝົດ",
        'btn_copy': "ສຳເນົາ",
        'btn_export': "ສົ່ງອອກ",
        'btn_show': "ສະແດງລະຫັດຜ່ານ",
        'btn_hide': "ເຊື່ອງລະຫັດຜ່ານ",
        'btn_authenticate': "ຢືນຢັນຕົວຕົນ",
        'btn_settings': "ຕັ້ງຄ່າ",
        'btn_protect': "ປ້ອງກັນ",
        'btn_remove_password': "ລຶບລະຫັດຜ່ານ",
        'btn_manage': "ຈັດການລະຫັດຜ່ານ",
        'btn_retry': "ລອງອີກຄັ້ງ",
        'btn_select_all': "ເລືອກທັງໝົດ",
        'btn_clear_selection': "ຍົກເລີກການເລືອກ",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "ໜ້າ {0} ຈາກ {1}",
        'page_count': "ຈາກ {0}",
        'goto_page': "ໄປທີ່ໜ້າ",
        'page_simple': "ໜ້າ {0}",
        'full_view_page': "ເບິ່ງເຕັມໜ້າ {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "ປ້ອນຄຳສຳລັບຄົ້ນຫາ + Enter",
        'search_results': "ຜົນໄດ້ຮັບ: {0} ຈາກ {1}",
        'search_nav_hint': "Enter: ຕໍ່ໄປ (Shift+Enter: ກ່ອນໜ້າ)",
        'search_no_results': "ບໍ່ພົບຜົນໄດ້ຮັບ",
        'search_error': "ຂໍ້ຜິດພາດໃນການຄົ້ນຫາ",
        'search_active': "ເປີດຊ່ອງຄົ້ນຫາ",
        'search_closed': "ສິ້ນສຸດການຄົ້ນຫາ",
        'search_position': "ໜ້າ {0} {1}",
        'search_pos_top': "ເທິງສຸດ",
        'search_pos_upper': "ຕອນເທິງ",
        'search_pos_middle': "ກາງ",
        'search_pos_lower': "ຕອນລຸ່ມ",
        'search_pos_bottom': "ລຸ່ມສຸດ",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "ການຮັບຮູ້ຂໍ້ຄວາມສຳເລັດ!",
        'ocr_success_title': "OCR ສຳເລັດ",
        'ocr_success_message': "ເອກະສານນີ້ສາມາດຄົ້ນຫາໄດ້ແລ້ວ",
        'ocr_failed': "OCR ລົ້ມເຫຼວ",
        'ocr_in_progress': "ກຳລັງດຳເນີນການ OCR",
        'ocr_preparing': "ກຳລັງກະກຽມ PDF...",
        'ocr_analyzing': "ກຳລັງວິເຄາະ PDF...",
        'ocr_optimizing': "ກຳລັງປັບປຸງຮູບພາບ...",
        'ocr_recognizing': "ກຳລັງຮັບຮູ້ຂໍ້ຄວາມ...",
        'ocr_embedding': "ກຳລັງຝັງຂໍ້ຄວາມ...",
        'ocr_finalizing': "ກຳລັງສຳເລັດ PDF...",
        'ocr_not_available': "OCR ບໍ່ພ້ອມໃຊ້ງານ",
        'ocr_install_message': "ບໍ່ພົບເຄື່ອງມື OCR.\n\nກະລຸນາຕິດຕັ້ງ:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "ຈຳເປັນຕ້ອງໃຊ້ OCR",
        'ocr_question': "PDF ນີ້ບໍ່ມີຂໍ້ຄວາມທີ່ສາມາດຄົ້ນຫາໄດ້.\nທ່ານຕ້ອງການເຮັດ OCR ເພື່ອໃຫ້ {0} ໄດ້ຫຼືບໍ່?",
        'ocr_perform': "ເຮັດ OCR",
        'ocr_later': "ພາຍຫຼັງ",
        'ocr_starting': "ກຳລັງເລີ່ມ OCR ແບບຮັບປະກັນ...",
        'ocr_success_voice': "OCR ສຳເລັດ. PDF ສາມາດຄົ້ນຫາໄດ້ແລ້ວ",
        'ocr_partial_success': "ດຳເນີນການ OCR ແລ້ວ, ແຕ່ມີບັນຫາໃນການແທນທີ່.\n\nບັນທຶກສະບັບທີ່ສາມາດຄົ້ນຫາໄດ້ທີ່:\n{0}\n\nຂໍ້ຜິດພາດ: {1}",
        'ocr_partial_title': "OCR ສຳເລັດບາງສ່ວນ",
        'ocr_partial_voice': "ດຳເນີນການ OCR ແລ້ວ, ແຕ່ການແທນທີ່ລົ້ມເຫຼວ",
        'original_file': "ໄຟລ໌ຕົ້ນສະບັບ:",
        'old_size': "ຂະໜາດເກົ່າ:    {0} ໄບຕ໌",
        'new_size': "ຂະໜາດໃໝ່: {0} ໄບຕ໌",
        'size_change': "ປ່ຽນແປງ: {0}{1} ໄບຕ໌",
        'backup_created_file': "ສ້າງສຳຮອງແລ້ວ:\n{0}",
        'backup_not_created': "ສຳຮອງ: ບໍ່ໄດ້ສ້າງ (ປິດການຕັ້ງຄ່າ)",
        'page_header': "=== ໜ້າ {0} ===\n{1}\n",
        'scanned_page_header': "=== ໜ້າ {0} (ສະແກນ) ===\n[ໜ້ານີ້ມີສະເພາະຂໍ້ຄວາມທີ່ສະແກນ]\n[ກະລຸນາເຮັດ OCR ດ້ວຍຕົນເອງ]\n",
        'scanned_warning': "⚠️ ຂໍ້ຄວາມທີ່ສະແກນ - ຈຳເປັນຕ້ອງໃຊ້ OCR",
        'guaranteed_title': "ສ້າງ PDF ທີ່ສາມາດຄົ້ນຫາໄດ້ແລ້ວ",
        'guaranteed_message': "<b>ສ້າງສະບັບທີ່ສາມາດຄົ້ນຫາໄດ້ແບບຮັບປະກັນແລ້ວ!</b>\n\nເນື່ອງຈາກ OCR ອັດຕະໂນມັດລົ້ມເຫຼວ, ຈຶ່ງໄດ້ສ້າງ PDF ທາງເລືອກທີ່ສາມາດຄົ້ນຫາໄດ້:\n\n{0}\n\n<b>ໄຟລ໌ນີ້ປະກອບດ້ວຍ:</b>\n• ຂໍ້ຄວາມທີ່ສະກັດໄດ້ (ຖ້າມີ)\n• ຄຳແນະນຳສຳລັບໜ້າທີ່ສະແກນ\n• ສາມາດຄົ້ນຫາໄດ້ຢ່າງສົມບູນ",
        'guaranteed_voice': "ສ້າງ PDF ທີ່ສາມາດຄົ້ນຫາໄດ້ແບບຮັບປະກັນແລ້ວ",
        'instruction_title': "ຄຳແນະນຳສຳລັບ OCR",
        'instruction_file': "ໄຟລ໌ຕົ້ນສະບັບ: {0}",
        'instruction_text': "ການຮັບຮູ້ຂໍ້ຄວາມອັດຕະໂນມັດ (OCR) ລົ້ມເຫຼວ.\nກະລຸນາເຮັດ OCR ດ້ວຍຕົນເອງ:\n\n1. ດ້ວຍ OCRmyPDF (ບັນທັດຄຳສັ່ງ):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. ດ້ວຍ ADOBE ACROBAT (macOS/Windows):\n   • ເປີດ PDF ໃນ Acrobat\n   • ເຄື່ອງມື > ແກ້ໄຂ PDF\n   • ເລືອກ 'ຮັບຮູ້ຂໍ້ຄວາມ'\n\n3. ດ້ວຍ PREVIEW (macOS):\n   • ເປີດ PDF ໃນ Preview\n   • ໄຟລ໌ > ສົ່ງອອກ...\n   • ຕົວກອງ Quartz: 'ຫຼຸດຂະໜາດໄຟລ໌'\n   • ເປີດໃຊ້ງານ 'ເຮັດ OCR'\n\n4. ບໍລິການ OCR ອອນໄລນ໌:\n   • smallpdf.com/lo/ocr-pdf\n   • ilovepdf.com/lo/ocr-pdf\n   • adobe.com/la/acrobat/online/pdf-to-word.html",
        'instruction_created': "ສ້າງຄຳແນະນຳ OCR ແລ້ວ",
        'instruction_created_message': "ສ້າງຄຳແນະນຳລາຍລະອຽດແລ້ວ:\n\n{0}\n\nກະລຸນາເຮັດຕາມຂັ້ນຕອນສຳລັບ OCR ດ້ວຍຕົນເອງ",
        'instruction_created_voice': "ສ້າງຄຳແນະນຳ OCR ແລ້ວ",
        'ocr_impossible': "OCR ບໍ່ສາມາດເຮັດໄດ້",
        'ocr_impossible_message': "ບໍ່ສາມາດເຮັດ OCR ໄດ້.\n\nກະລຸນາປະມວນຜົນ '{0}' ດ້ວຍຕົນເອງດ້ວຍຊອບແວ OCR",
        'ocr_impossible_voice': "OCR ບໍ່ສາມາດເຮັດໄດ້. ກະລຸນາປະມວນຜົນດ້ວຍຕົນເອງ",
        'emergency_title': "OCR ສຸກເສີນ",
        'emergency_message': "ສ້າງ PDF ສຸກເສີນແລ້ວ:\n\n{0}\n\nກະລຸນາປະມວນຜົນໄຟລ໌ນີ້ດ້ວຍຕົນເອງດ້ວຍ OCR",
        'emergency_voice': "ສ້າງ PDF ສຸກເສີນແລ້ວ. ກະລຸນາເຮັດ OCR ດ້ວຍຕົນເອງ",
        'critical_error': "ຂໍ້ຜິດພາດຮ້າຍແຮງ",
        'critical_error_message': "ບໍ່ສາມາດເລີ່ມ OCR ໄດ້.\n\nກະລຸນາເລີ່ມໂປຣແກຣມໃໝ່ ແລະ ກວດສອບການຕິດຕັ້ງ OCR",
        'critical_error_voice': "ຂໍ້ຜິດພາດຮ້າຍແຮງ OCR",
        'ocr_question_html': "<p>PDF ນີ້ບໍ່ມີຂໍ້ຄວາມທີ່ຄົ້ນຫາໄດ້.<p>ທ່ານຕ້ອງການເຮັດ OCR ເພື່ອໃຫ້ <b>{0}</b> ໄດ້ຫຼືບໍ່?</p>",
        'ocr_question_voice': "ຈຳເປັນຕ້ອງໃຊ້ OCR. PDF ບໍ່ມີຂໍ້ຄວາມທີ່ຄົ້ນຫາໄດ້. ທ່ານຕ້ອງການເຮັດ OCR ເພື່ອໃຫ້ {0} ໄດ້ຫຼືບໍ່?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ບໍ່ມີ PDF ຖືກໂຫຼດ",
        'no_pdf_message': "ບໍ່ມີ PDF ຖືກໂຫຼດ",
        'pdf_not_found': "ບໍ່ພົບໄຟລ໌ PDF",
        'file_size': "ຂະໜາດໄຟລ໌",
        'bytes': "ໄບຕ໌",
        'kb': "ກິໂລໄບຕ໌",
        'mb': "ເມກາໄບຕ໌",
        'backup_created': "ສ້າງສຳຮອງແລ້ວ",
        'backup_disabled': "ປິດການສຳຮອງຂໍ້ມູນ",
        'backup_activated': "ເປີດການສ້າງສຳຮອງ",
        'backup_deactivated': "ປິດການສ້າງສຳຮອງ",
        'backup_status': "ສຳຮອງ: {0}",
        'backup_on': "✔ ເປີດ",
        'backup_off': "✘ ປິດ",
        'close_pdf': "ປິດ PDF: {0}",
        'pdf_not_found_format': "ບໍ່ພົບໄຟລ໌ PDF: {0}",
        'error_pdf_load_format': "ຂໍ້ຜິດພາດໃນການໂຫຼດ PDF: {0}",
        'load_failed_format': "ໂຫຼດບໍ່ສຳເລັດ:\n{0}",
        'decrypted_suffix': "(ຖອດລະຫັດແລ້ວ)",
        'decryption_failed': "ການຖອດລະຫັດລົ້ມເຫຼວ",
        'decryption_error': "ຂໍ້ຜິດພາດໃນການຖອດລະຫັດ",
        'decryption_success': "ຖອດລະຫັດສຳເລັດ",
        'decryption_success_message': "ຖອດລະຫັດ PDF ແລະ ບັນທຶກທີ່:\n\n{0}",
        'decryption_success_voice': "ຖອດລະຫັດ PDF ແລະ ບັນທຶກແລ້ວ",
        'password_remove_error': "ຂໍ້ຜິດພາດໃນການລຶບລະຫັດຜ່ານ",
        'save_unencrypted': "ບັນທຶກ PDF ທີ່ບໍ່ໄດ້ເຂົ້າລະຫັດເປັນ",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "ບັນທຶກເປັນ...",
        'save_copy': "ບັນທຶກສຳເນົາ",
        'save_success': "ບັນທຶກ PDF ທີ່: {0}",
        'save_encrypted': "ບັນທຶກ PDF ທີ່ປ້ອງກັນທີ່: {0}",
        'save_error': "ບໍ່ສາມາດບັນທຶກ PDF ໄດ້",
        'encryption_question': "ທ່ານຕ້ອງການປ້ອງກັນ PDF ດ້ວຍລະຫັດຜ່ານຫຼືບໍ່?",
        'encryption_yes': "ແມ່ນ",
        'encryption_no': "ບໍ່",
        'encryption_cancel': "ຍົກເລີກ",
        'save_cancel': "ຍົກເລີກການບັນທຶກ",
        'save_encrypted_voice': "ເຂົ້າລະຫັດ ແລະ ບັນທຶກໄຟລ໌ແລ້ວ",
        'save_success_voice': "ບັນທຶກໄຟລ໌ PDF ໂດຍບໍ່ໄດ້ເຂົ້າລະຫັດແລ້ວ",
        'save_error_format': "ບໍ່ສາມາດບັນທຶກ PDF ໄດ້:\n{0}",
        'export_pages_success': "ສົ່ງອອກ Pages ສຳເລັດ",
        'export_pages_error': "ສົ່ງອອກ Pages ລົ້ມເຫຼວ",
        'export_pages_error_format': "ສົ່ງອອກ Pages ລົ້ມເຫຼວ: {0}",
        'export_word_success': "ສົ່ງອອກ Word ສຳເລັດ",
        'export_word_error': "ສົ່ງອອກ Word ລົ້ມເຫຼວ",
        'export_word_error_format': "ສົ່ງອອກ Word ລົ້ມເຫຼວ: {0}",
        'export_text_success': "ສົ່ງອອກຂໍ້ຄວາມສຳເລັດ",
        'export_text_error': "ສົ່ງອອກຂໍ້ຄວາມລົ້ມເຫຼວ",
        'export_text_error_format': "ສົ່ງອອກຂໍ້ຄວາມລົ້ມເຫຼວ: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "ຈຳເປັນຕ້ອງໃຊ້ລະຫັດຜ່ານ",
        'password_enter': "ກະລຸນາປ້ອນລະຫັດຜ່ານ",
        'password_confirm': "ຢືນຢັນລະຫັດຜ່ານ",
        'password_new': "ລະຫັດຜ່ານໃໝ່",
        'password_current': "ລະຫັດຜ່ານປັດຈຸບັນ",
        'password_save': "ບັນທຶກລະຫັດຜ່ານ (ເຂົ້າລະຫັດ)",
        'password_saved': "✓ ບັນທຶກລະຫັດຜ່ານສຳລັບໄຟລ໌ນີ້ແລ້ວ",
        'password_wrong': "ລະຫັດຜ່ານຜິດ",
        'password_mismatch': "ລະຫັດຜ່ານບໍ່ກົງກັນ",
        'password_too_short': "ລະຫັດຜ່ານສັ້ນເກີນໄປ",
        'password_min_length': "ລະຫັດຜ່ານຕ້ອງມີຄວາມຍາວຢ່າງໜ້ອຍ 4 ຕົວອັກສອນ",
        'password_strength': "ຄວາມເຂັ້ມແຂງຂອງລະຫັດຜ່ານ",
        'password_strength_very_weak': "ອ່ອນຫຼາຍ",
        'password_strength_weak': "ອ່ອນ",
        'password_strength_medium': "ປານກາງ",
        'password_strength_strong': "ແຂງແຮງ",
        'password_strength_very_strong': "ແຂງແຮງຫຼາຍ",
        'password_char_count': "({0} ຕົວອັກສອນ)",
        'password_match': "✓ ກົງກັນ",
        'password_no_match': "✗ ລະຫັດຜ່ານບໍ່ກົງກັນ",
        'password_show': "ສະແດງ",
        'password_hide': "ເຊື່ອງ",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "ການຈັດການລະຫັດຜ່ານ",
        'password_table_filename': "ຊື່ໄຟລ໌",
        'password_table_password': "ລະຫັດຜ່ານ",
        'password_count': "ບັນທຶກລະຫັດຜ່ານ {0} ລາຍການ",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "ບໍ່ມີລະຫັດຜ່ານທີ່ບັນທຶກໄວ້",
        'password_copied': "ສຳເນົາລະຫັດຜ່ານ {0} ລາຍການແລ້ວ",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບລະຫັດຜ່ານສຳລັບ '{0}'?",
        'password_delete_multiple': "ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບລະຫັດຜ່ານທີ່ເລືອກ {0} ລາຍການ?",
        'password_delete_all_confirm': "ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບລະຫັດຜ່ານທີ່ບັນທຶກໄວ້ທັງໝົດ {0} ລາຍການ?",
        'password_deleted': "ລຶບລະຫັດຜ່ານ {0} ລາຍການແລ້ວ",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "ລຶບລະຫັດຜ່ານທັງໝົດແລ້ວ",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "ເຄື່ອງສ້າງລະຫັດຜ່ານ",
        'generator_generated': "ລະຫັດຜ່ານທີ່ສ້າງ:",
        'generator_regenerate': "ສ້າງໃໝ່",
        'generator_copy': "ສຳເນົາ",
        'generator_use': "ໃຊ້",
        'generator_settings': "ຕັ້ງຄ່າ",
        'generator_length': "ຄວາມຍາວ:",
        'generator_group_every': "ຕົວຄັ້ນທຸກໆ",
        'generator_group_chars': "ຕົວອັກສອນ. ຕົວຄັ້ນ:",
        'generator_uppercase': "ຕົວພິມໃຫຍ່ (A-Z)",
        'generator_lowercase': "ຕົວພິມນ້ອຍ (a-z)",
        'generator_digits': "ຕົວເລກ (0-9)",
        'generator_symbols': "ສັນຍາລັກພິເສດ (!@#$%^&*)",
        'generator_exclude': "ບໍ່ລວມ:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "ຈຳເປັນຕ້ອງໃຊ້ລະຫັດຜ່ານຫຼັກ",
        'master_password_setup': "ຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ",
        'master_password_change': "ປ່ຽນລະຫັດຜ່ານຫຼັກ",
        'master_password_enter': "ກະລຸນາປ້ອນລະຫັດຜ່ານຫຼັກຂອງທ່ານ",
        'master_password_choose': "ເລືອກລະຫັດຜ່ານຫຼັກທີ່ແຂງແຮງ (ຢ່າງໜ້ອຍ 8 ຕົວອັກສອນ)",
        'master_password_new': "ກະລຸນາປ້ອນລະຫັດຜ່ານຫຼັກໃໝ່ຂອງທ່ານ",
        'master_password_confirm': "ຢືນຢັນລະຫັດຜ່ານ",
        'master_password_authenticate': "ຢືນຢັນຕົວຕົນ",
        'master_password_success': "ຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກສຳເລັດ",
        'master_password_changed': "ປ່ຽນລະຫັດຜ່ານຫຼັກສຳເລັດ",
        'master_password_removed': "ລຶບລະຫັດຜ່ານຫຼັກ ແລະ ລະຫັດຜ່ານທັງໝົດແລ້ວ",
        'master_password_remove': "ລຶບລະຫັດຜ່ານຫຼັກ",
        'master_password_remove_confirm': "ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບລະຫັດຜ່ານທັງໝົດ?\n\nການດຳເນີນການນີ້ບໍ່ສາມາດກັບຄືນໄດ້!",
        'master_password_export_before': "ທ່ານຕ້ອງການສົ່ງອອກສຳຮອງກ່ອນຫຼືບໍ່?",
        'master_password_export_delete': "ສົ່ງອອກ ແລະ ລຶບ",
        'master_password_delete_now': "ລຶບດຽວນີ້",
        'master_password_for_signatures': "ເພື່ອໃຊ້ລາຍເຊັນ, ທ່ານຕ້ອງຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ.\n\nທ່ານຕ້ອງການຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກດຽວນີ້ບໍ່?",
        'master_password_for_private': "ເພື່ອໃຊ້ບລັອກຂໍ້ຄວາມສ່ວນຕົວ, ທ່ານຕ້ອງຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ.\n\nທ່ານຕ້ອງການຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກດຽວນີ້ບໍ່?",
        'master_password_info': """
            <b>🔐 ບໍ່ມີລະຫັດຜ່ານຫຼັກ:</b><br>
            • ບໍ່ສາມາດສະແດງ, ສຳເນົາ ແລະ ສົ່ງອອກລະຫັດຜ່ານໄດ້<br>
            • ສາມາດລຶບລະຫັດຜ່ານໄດ້ສະເໝີ (ເຖິງວ່າບໍ່ມີລະຫັດຜ່ານຫຼັກ)<br><br>

            <b>🔐 ມີລະຫັດຜ່ານຫຼັກ:</b><br>
            • ຟັງຊັນທັງໝົດພ້ອມໃຊ້ງານຫຼັງຢືນຢັນຕົວຕົນ<br>
            • ລະຫັດຜ່ານຖືກເຂົ້າລະຫັດດ້ວຍລະຫັດຜ່ານຫຼັກ<br>
            • ຄວາມຍາວຂັ້ນຕ່ຳ: 8 ຕົວອັກສອນ<br>
            • ເກັບຮັກສາແຮດ SHA-256 ຢ່າງປອດໄພ<br><br>

            <b>ສຳຄັນ:</b><br>
            • ຖ້າລືມລະຫັດຜ່ານຫຼັກ: ບໍ່ສາມາດກູ້ຄືນລະຫັດຜ່ານໄດ້<br>
            • ເມື່ອລຶບລະຫັດຜ່ານຫຼັກ: ລະຫັດຜ່ານທັງໝົດຖືກລຶບ<br>
            • ມີຕົວເລືອກສົ່ງອອກກ່ອນລຶບ<br>
            • ສາມາດປ່ຽນລະຫັດຜ່ານຫຼັກໄດ້ທຸກເວລາ
        """,
        'signature_auth_disabled': "ປິດການຖາມລະຫັດຜ່ານສຳລັບລາຍເຊັນ",
        'template_auth_disabled': "ປິດການຖາມລະຫັດຜ່ານສຳລັບບລັອກຂໍ້ຄວາມສ່ວນຕົວ",
        'master_password_for_signatures_settings': "ເພື່ອໃຊ້ລາຍເຊັນ, ທ່ານຕ້ອງຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ.\n\nໄປທີ່ ການຕັ້ງຄ່າ - ການຈັດການລະຫັດຜ່ານ",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "ປ້ອງກັນ PDF",
        'protect_info': "ໄຟລ໌ '{0}' ຈະຖືກປ້ອງກັນດ້ວຍລະຫັດຜ່ານ",
        'protect_instruction': "ກະລຸນາປ້ອນລະຫັດຜ່ານທີ່ຕ້ອງການສອງຄັ້ງເພື່ອປ້ອງກັນເອກະສານ, ຫຼື ໃຊ້ເຄື່ອງສ້າງລະຫັດຜ່ານທາງດ້ານຂວາຂອງຊ່ອງປ້ອນຂໍ້ມູນ",
        'protect_success': "ປ້ອງກັນ PDF ສຳເລັດ ແລະ ບັນທຶກທີ່:\n{0}\n\nລະຫັດຜ່ານ: {1}\n\nທ່ານຕ້ອງການເປີດ PDF ທີ່ປ້ອງກັນດຽວນີ້ບໍ່?",
        'protect_open': "ແມ່ນ",
        'protect_skip': "ບໍ່",
        'protect_error': "ຂໍ້ຜິດພາດໃນການປ້ອງກັນ PDF",
        'protect_open_title': "ເປີດ PDF ທີ່ປ້ອງກັນ",
        'protect_question': "ສຳເລັດ. ທ່ານຕ້ອງການເປີດ PDF ທີ່ປ້ອງກັນດຽວນີ້ບໍ່? ແມ່ນ ຫຼື ບໍ່?",
        'password_cancel': "ຍົກເລີກການສົນທະນາລະຫັດຜ່ານ",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "ລຶບໜ້າ",
        'pages_extract': "ສະກັດໜ້າ",
        'pages_insert': "ແຊກໜ້າ",
        'pages_move': "ຍ້າຍໜ້າ",
        'pages_delete_options': "ຕົວເລືອກການລຶບ",
        'pages_delete_empty': "ລຶບໜ້າວ່າງທັງໝົດ",
        'pages_delete_current': "ລຶບໜ້າປັດຈຸບັນ",
        'pages_delete_range': "ລຶບຊ່ວງໜ້າ",
        'pages_extract_options': "ຕົວເລືອກການສະກັດ",
        'pages_extract_current': "ສະກັດໜ້າປັດຈຸບັນ",
        'pages_extract_range': "ສະກັດຊ່ວງໜ້າ",
        'pages_insert_position': "ຕຳແໜ່ງແຊກ",
        'pages_insert_before': "ແຊກກ່ອນໜ້າ:",
        'pages_insert_select': "ເລືອກ PDF",
        'pages_insert_none': "ບໍ່ໄດ້ເລືອກ PDF",
        'pages_move_source': "ໜ້າທີ່ຈະຍ້າຍ",
        'pages_move_from': "ຈາກໜ້າ:",
        'pages_move_to': "ຮອດໜ້າ:",
        'pages_move_target': "ຕຳແໜ່ງເປົ້າໝາຍ",
        'pages_move_before': "ຍ້າຍກ່ອນໜ້າ:",
        'pages_move_hint': "ໝາຍເຫດ: ໜ້າ 1 = ຕົ້ນ, {0} = ປາຍ",
        'pages_range_invalid': "ໜ້າເລີ່ມຕົ້ນຕ້ອງນ້ອຍກວ່າ ຫຼື ເທົ່າກັບໜ້າສິ້ນສຸດ",
        'pages_position_invalid': "ຕຳແໜ່ງເປົ້າໝາຍຕ້ອງບໍ່ຢູ່ໃນຊ່ວງທີ່ກຳລັງຍ້າຍ",
        'pages_no_pdf_selected': "ບໍ່ໄດ້ເລືອກ PDF",
        'pages_deleted': "ລຶບ {0} ໜ້າແລ້ວ",
        'pages_extracted': "ສະກັດ: {0}\nບັນທຶກທີ່: {1}\nຂະໜາດໄຟລ໌: {2:.1f} KB",
        'pages_inserted': "ແຊກ {0} ໜ້າ",
        'pages_moved': "ຍ້າຍ {0} ໜ້າແລ້ວ",
        'pages_deleted_none': "ບໍ່ມີການລຶບໜ້າ",
        'pages_delete_progress': "ກຳລັງລຶບໜ້າ...",
        'pages_deleted_with_backup': "ລຶບ {0} ໜ້າແລ້ວ\n\nສຳຮອງ: {1}",
        'pages_deleted_voice': "ສ້າງສຳຮອງ ແລະ ລຶບ {0} ໜ້າແລ້ວ",
        'info': "ໝາຍເຫດ",
        'error_dialog_creation': "ບໍ່ສາມາດສ້າງການສົນທະນາໄດ້",
        'extract_page_single': "ສະກັດໜ້າ {0}",
        'extract_page_range': "ສະກັດໜ້າ {0}-{1}",
        'extract_success_voice': "ສະກັດໜ້າສຳເລັດ",
        'extract_error_format': "ຂໍ້ຜິດພາດໃນການສະກັດ: {0}",
        'pages_inserted_voice': "ແຊກ {0} ໜ້າແລ້ວ",
        'insert_error_format': "ຂໍ້ຜິດພາດໃນການແຊກ: {0}",
        'pages_move_progress': "ກຳລັງຍ້າຍໜ້າ...",
        'pages_moved_with_backup': "ຍ້າຍ {0} ໜ້າແລ້ວ\n\nສຳຮອງ: {1}",
        'move_success_title': "ຍ້າຍສຳເລັດ",
        'pages_moved_voice': "ຍ້າຍ {0} ໜ້າສຳເລັດ",
        'mark_removed': "ລຶບເຄື່ອງໝາຍຈາກໜ້າ {0}",
        'mark_empty': "ໝາຍໜ້າວ່າງທີ່ໜ້າ {0}",
        'mark_export_removed': "ລຶບເຄື່ອງໝາຍສົ່ງອອກຈາກໜ້າ {0}",
        'mark_export': "ໝາຍໜ້າ {0} ສຳລັບສົ່ງອອກ",
        'no_empty_pages': "ບໍ່ມີໜ້າວ່າງທີ່ໝາຍໄວ້ເພື່ອລຶບ",
        'delete_empty_confirm': "ທ່ານຕ້ອງການລຶບໜ້າວ່າງທີ່ໝາຍໄວ້ທັງໝົດ {0} ໜ້າບໍ່?",
        'delete_empty_confirm_voice': "ລຶບໜ້າວ່າງທີ່ໝາຍໄວ້ທັງໝົດ {0} ໜ້າດຽວນີ້? ແມ່ນ ຫຼື ບໍ່",
        'empty_pages_deleted': "ລຶບໜ້າວ່າງ {0} ໜ້າ",
        'no_export_pages': "ບໍ່ມີໜ້າທີ່ໝາຍໄວ້ສຳລັບສົ່ງອອກ",
        'overwrite_title': "ແທນທີ່ໄຟລ໌ທີ່ມີຢູ່",
        'overwrite_question': "ໄຟລ໌\n\n{0}\n\nມີຢູ່ແລ້ວ.\nທ່ານຕ້ອງການແທນທີ່ມັນບໍ່?",
        'overwrite_voice': "ແທນທີ່ໄຟລ໌ທີ່ມີຢູ່? ແມ່ນ ຫຼື ບໍ່",
        'page_skipped': "ຂ້າມໜ້າ {0}",
        'export_complete': "ສົ່ງອອກສຳເລັດ",
        'export_complete_voice': "ການສົ່ງອອກສຳເລັດ",
        'no_pages_exported': "ບໍ່ມີໜ້າຖືກສົ່ງອອກ",
        'export_cancelled': "ຍົກເລີກການສົ່ງອອກ",
        'pages_exported': "ສົ່ງອອກ {0} ໜ້າໄປຍັງ {1}",
        'export_page_title': "ສົ່ງອອກໜ້າ",
        'page_exported': "ສົ່ງອອກໜ້າ {0} ໄປຍັງ {1}",
        'export_error': "ຂໍ້ຜິດພາດໃນການສົ່ງອອກ",
        'export_marked_title': "ສົ່ງອອກໜ້າທີ່ໝາຍໄວ້",
        'rotate_all_title': "ໝຸນທຸກໜ້າ",
        'rotate_all_question': "ທ່ານຕ້ອງການໝຸນທຸກໜ້າ 90 ອົງສາໄປທາງຂວາບໍ່?",
        'rotate_all_voice': "ທ່ານຕ້ອງການໝຸນທຸກໜ້າ 90 ອົງສາໄປທາງຂວາບໍ່? ແມ່ນ ຫຼື ບໍ່?",
        'all_pages_rotated': "ໝຸນທຸກໜ້າແລ້ວ",
        'page_rotated': "ໝຸນໜ້າ {0} ແລ້ວ",
        'rotate_error': "ບໍ່ສາມາດໝຸນໜ້າໄດ້",
        'delete_page_confirm': "ທ່ານຕ້ອງການລຶບໜ້າ {0} ບໍ່?",
        'delete_page_confirm_voice': "ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບໜ້າ {0}? ແມ່ນ ຫຼື ບໍ່",
        'page_deleted': "ລຶບໜ້າ {0} ແລ້ວ",
        'delete_error': "ບໍ່ສາມາດລຶບໜ້າໄດ້",
        'pages_deleted_voice': "ລຶບ {0} ໜ້າແລ້ວ",
        'pages_exported_split': "ສົ່ງອອກ {0} ໜ້າສຳເລັດ",
        'pages_skipped': "ຂ້າມ {0} ໜ້າ",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "ສະກັດໜ້າ (ຂັ້ນສູງ)",
        'pdf_splitter_title': "ຕົວແບ່ງ ແລະ ສະກັດ PDF",
        'pdf_splitter_load': " ເລືອກໄຟລ໌ PDF",
        'pdf_splitter_info': "ກະລຸນາເລືອກຕົວເລືອກສຳລັບເອກະສານ PDF ຂອງທ່ານ",
        'pdf_splitter_basic': "ການດຳເນີນການພື້ນຖານ",
        'pdf_splitter_single': "ແບ່ງເປັນໜ້າເດັ່ຽວ",
        'pdf_splitter_range': "ສະກັດໜ້າ:",
        'pdf_splitter_range_placeholder': "ຕົວຢ່າງ: 1-3,5,7-9",
        'pdf_splitter_clean': "ການດຳເນີນການເຮັດຄວາມສະອາດ",
        'pdf_splitter_remove_empty': "ລຶບໜ້າວ່າງທັງໝົດ",
        'pdf_splitter_remove': "ລຶບຊ່ວງໜ້າ:",
        'pdf_splitter_remove_placeholder': "ຕົວຢ່າງ: 2,4-6",
        'pdf_splitter_process': "ປະມວນຜົນ PDF",
        'pdf_splitter_loaded': "ໂຫຼດ PDF ແລ້ວ. ກະລຸນາເລືອກຕົວເລືອກ",
        'pdf_read_error': "ບໍ່ສາມາດອ່ານ PDF ໄດ້",
        'pages': "ໜ້າ",
        'pages_created': "ສ້າງໜ້າແລ້ວ",
        'range_empty': "ກະລຸນາປ້ອນຊ່ວງໜ້າ",
        'range_invalid': "ຊ່ວງໜ້າບໍ່ຖືກຕ້ອງ",
        'range_created': "ສ້າງ PDF ໃໝ່ດ້ວຍໜ້າທີ່ເລືອກ:\n{0}",
        'empty_removed': "ລຶບໜ້າວ່າງ {0} ໜ້າ\nຜົນໄດ້ຮັບ: {1}",
        'remove_empty': "ກະລຸນາປ້ອນໜ້າທີ່ຈະລຶບ",
        'remove_invalid': "ໜ້າທີ່ຈະລຶບບໍ່ຖືກຕ້ອງ",
        'remove_done': "ສ້າງ PDF ທີ່ເຮັດຄວາມສະອາດແລ້ວ:\n{0}",
        'open_folder': "ເປີດໂຟນເດີ",
        'show_in_finder': "ສະແດງໃນ Finder",
        'pdf_splitter_no_pdf': "ກະລຸນາໂຫຼດໄຟລ໌ PDF ກ່ອນ",
        'process_error': "ຂໍ້ຜິດພາດໃນການປະມວນຜົນ PDF",
        'pages_created_voice': "ສ້າງ {0} ໜ້າແລ້ວ",
        'range_created_voice': "ສ້າງ PDF ດ້ວຍໜ້າທີ່ເລືອກແລ້ວ",
        'empty_removed_voice': "ລຶບໜ້າວ່າງ {0} ໜ້າແລ້ວ",
        'remove_done_voice': "ສ້າງ PDF ທີ່ເຮັດຄວາມສະອາດແລ້ວ",
        'pdf_splitter_split_groups': "ແຕ່ລະກຸ່ມຕໍ່ເນື່ອງເປັນໄຟລ໌ແຍກ",
        'range_created_single': "ສ້າງ PDF ໃໝ່:\n{0}",
        'range_created_multiple': "ສ້າງໄຟລ໌ PDF {0} ໄຟລ໌",
        'range_created_voice_single': "ສ້າງ PDF ໜຶ່ງໄຟລ໌ດ້ວຍໜ້າທີ່ເລືອກ",
        'range_created_voice_multiple': "ສ້າງໄຟລ໌ PDF {0} ໄຟລ໌",
        'empty_removed_none_left': "ບໍ່ມີໜ້າເຫຼືອ",
        'empty_removed_all_empty': "ທຸກໜ້າຖືກກວດພົບວ່າວ່າງ ແລະ ຈະຖືກລຶບ. ບໍ່ໄດ້ສ້າງໄຟລ໌",
        'preview_single': "ສະແດງຕົວຢ່າງ: {0}",
        'preview_enter_range': "ກະລຸນາປ້ອນຊ່ວງໜ້າ",
        'preview_invalid_range': "ຊ່ວງໜ້າບໍ່ຖືກຕ້ອງ",
        'preview_file': "ສະແດງຕົວຢ່າງ: {0}",
        'preview_files': "ສະແດງຕົວຢ່າງ: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "ເລີ່ມພິມ",
        'print_sent': "ສົ່ງງານພິມແລ້ວ",
        'print_now': "ພິມດຽວນີ້",
        'print_error': "ຂໍ້ຜິດພາດໃນການພິມດຽວນີ້",
        'print_limited': "ຟັງຊັນການພິມຈຳກັດໃນລະບົບນີ້",
        'print_error_format': "ຂໍ້ຜິດພາດໃນການພິມດຽວນີ້: {0}",
        'warning': "ຄຳເຕືອນ",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "ປ່ຽນໄປໂໝດສະຫວ່າງ",
        'mode_switch_to_dark': "ປ່ຽນໄປໂໝດມືດ",
        'mode_dark_activated': "ເປີດໂໝດມືດ",
        'mode_light_activated': "ເປີດໂໝດສະຫວ່າງ",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "ເບິ່ງເຕັມໜ້າ",
        'zoom_two_pages': "ສອງໜ້າຄູ່ກັນ",
        'zoom_overview': "ໂໝດພາບລວມ",
        'zoom_cannot_during_search': "ບໍ່ສາມາດຊູມໃນລະຫວ່າງການຄົ້ນຫາໄດ້",
        'zoom_exit_first': "ກະລຸນາອອກຈາກໂໝດຊູມກ່ອນ",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "ເປີດໃຊ້ການລາກແລ້ວວາງ",
        'drag_disabled': "ປິດໃຊ້ການລາກແລ້ວວາງ",
        'drag_page_grab': "ຈັບໜ້າ {0}",
        'drag_page_dropped': "ວາງໜ້າ {0} ທີ່ຕຳແໜ່ງ {1}",
        'drag_position_invalid': "ຕຳແໜ່ງບໍ່ຖືກຕ້ອງ",
        'drag_same_position': "ໜ້າ {0} ຍັງຄົງຢູ່ທີ່ຕຳແໜ່ງ {0}",
        'drag_error': "ຂໍ້ຜິດພາດໃນການຍ້າຍ",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "ປ້ອນຂໍ້ຄວາມພ້ອມການຈັດຮູບແບບຂັ້ນສູງ ແລະ ການຈັດການບລັອກຂໍ້ຄວາມ",
        'text_templates': "ບລັອກຂໍ້ຄວາມທີ່ມີ:",
        'text_name': "ຊື່",
        'text_preview': "ຕົວຢ່າງຂໍ້ຄວາມ",
        'text_enter': "ຂໍ້ຄວາມ:",
        'text_font_size': "ຂະໜາດຕົວອັກສອນ:",
        'text_formatting': "ການຈັດຮູບແບບ:",
        'text_bold': "ຕົວໜາ",
        'text_italic': "ຕົວອຽງ",
        'text_underline': "ຂີດກ້ອງ",
        'text_alignment': "ການຈັດຕຳແໜ່ງ:",
        'text_left': "ຊ້າຍ",
        'text_center': "ກາງ",
        'text_right': "ຂວາ",
        'text_color': "ສີຂໍ້ຄວາມ:",
        'text_opacity': "ຄວາມທຶບໃສ:",
        'text_word_wrap': "ຕັດຂໍ້ຄວາມ:",
        'text_auto': "ອັດຕະໂນມັດ",
        'text_page_width_95': "ຄວາມກວ້າງໜ້າ (95%)",
        'text_page_width_85': "ກວ້າງຫຼາຍ (85%)",
        'text_page_width_75': "ກວ້າງ (75%)",
        'text_page_width_60': "ກວ້າງປານກາງ (60%)",
        'text_page_width_50': "ປານກາງ (50%)",
        'text_page_width_30': "ແຄບ (30%)",
        'text_page_width_20': "ແຄບກວ່າ (20%)",
        'text_page_width_10': "ແຄບຫຼາຍ (10%)",
        'text_no_wrap': "ບໍ່ຕັດ",
        'text_private': "ບລັອກຂໍ້ຄວາມສ່ວນຕົວ (ຕ້ອງຢືນຢັນຕົວຕົນ)",
        'text_preview_label': "ຕົວຢ່າງ:",
        'text_preview_placeholder': "ຕົວຢ່າງຂໍ້ຄວາມຈະສະແດງຢູ່ນີ້...",
        'text_no_text': "(ບໍ່ມີຂໍ້ຄວາມ)",
        'text_save_template': "💾 ບັນທຶກເປັນບລັອກ",
        'text_delete_template': "🗑 ລຶບບລັອກຂໍ້ຄວາມທີ່ເລືອກ",
        'text_show_private': "ສະແດງສ່ວນຕົວ",
        'text_hide_private': "ເຊື່ອງສ່ວນຕົວ",
        'text_use': "✅ ໃຊ້ຂໍ້ຄວາມ",
        'text_saved': "ບັນທຶກບລັອກຂໍ້ຄວາມເປັນ:\n{0}",
        'text_saved_voice': "ບັນທຶກບລັອກຂໍ້ຄວາມແລ້ວ",
        'text_deleted': "ລຶບບລັອກຂໍ້ຄວາມແລ້ວ",
        'text_no_text_to_save': "ບໍ່ມີຂໍ້ຄວາມທີ່ຈະບັນທຶກ",
        'text_no_templates': "ບໍ່ພົບບລັອກຂໍ້ຄວາມ",
        'text_private_master_required': "ບລັອກສ່ວນຕົວສາມາດໃຊ້ໄດ້ສະເພາະເມື່ອຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກແລ້ວ.\n\nທ່ານຕ້ອງການຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກດຽວນີ້ບໍ່?",
        'text_filename': "ຊື່ໄຟລ໌ສຳລັບບລັອກຂໍ້ຄວາມ (ໂດຍບໍ່ມີ 'Text_' ແລະ '.txt'):",
        'text_filename_hint': "ຕົວຢ່າງ: 'ໂທລະສັບບ້ານ' ຈະຖືກບັນທຶກເປັນ 'Text_ໂທລະສັບບ້ານ.txt'",
        'text_save_hint': "ບລັອກຂໍ້ຄວາມຈະຖືກບັນທຶກພ້ອມການຈັດຮູບແບບໂດຍອັດຕະໂນມັດ",
        'text_guide_title': "ການປ້ອນຂໍ້ຄວາມ - ຄຳແນະນຳ",
        'text_delete_confirm': "ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບບລັອກຂໍ້ຄວາມນີ້?\n\nໄຟລ໌: {0}\nຂໍ້ຄວາມ: {1}...",
        'text_make_public': "ໝາຍເປັນສາທາລະນະ",
        'text_make_private': "ໝາຍເປັນສ່ວນຕົວ",
        'text_privacy_changed': "ປ່ຽນສະຖານະສ່ວນຕົວແລ້ວ",
        'text_private_always': "ສ່ວນຕົວສະແດງສະເໝີ (ການຕັ້ງຄ່າ)",
        'text_mode_required': "ກະລຸນາເປີດໂໝດຂໍ້ຄວາມກ່ອນ",
        'text_continue_editing': "ແກ້ໄຂຕໍ່ - ເຄີເຊີຢູ່ທ້າຍຂໍ້ຄວາມ",
        'text_no_input': "ບໍ່ໄດ້ປ້ອນຂໍ້ຄວາມ - ຖິ້ມຂໍ້ຄວາມ",
        'save_dialog_question': "ທ່ານຕ້ອງການດຳເນີນການຕໍ່ໄປແນວໃດ?",
        'text_save_question': "ບັນທຶກຂໍ້ຄວາມ ແລະ ກາກບອກທັງໝົດ, ປັບແຕ່ງ, ແກ້ໄຂຕໍ່ ຫຼື ຖິ້ມ?",
        'copy_cross': "ສຳເນົາກາກບອກ",
        'paste_cross': "ວາງກາກບອກ",
        'paste_text': "ວາງຂໍ້ຄວາມ",
        'cross_discarded': "ຖິ້ມກາກບອກ",
        'all_discarded': "ຖິ້ມທັງໝົດ",
        'text_discarded': "ຖິ້ມຂໍ້ຄວາມ",
        'no_texts_to_save': "ບໍ່ມີຂໍ້ຄວາມທີ່ຈະບັນທຶກ",
        'no_valid_texts': "ບໍ່ມີຂໍ້ຄວາມທີ່ຖືກຕ້ອງສຳລັບບັນທຶກ",
        'text_word_singular': "ຂໍ້ຄວາມ",
        'text_word_plural': "ຂໍ້ຄວາມ",
        'cross_word_singular': "ກາກບອກ",
        'cross_word_plural': "ກາກບອກ",
        'texts_saved_title': "ບັນທຶກຂໍ້ຄວາມແລ້ວ",
        'texts_crosses_saved': "ແຊກ {0} {1} ແລະ {2} {3} ລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'texts_crosses_saved_voice': "ບັນທຶກ {0} {1} ແລະ {2} {3} ແລ້ວ",
        'texts_saved': "ແຊກ {0} {1} ລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'texts_saved_voice': "ບັນທຶກ {0} {1} ແລ້ວ",
        'crosses_saved': "ແຊກ {0} {1} ລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'crosses_saved_voice': "ບັນທຶກ {0} {1} ແລ້ວ",
        'elements_saved': "ແຊກ {0} ລາຍການລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'elements_saved_voice': "ບັນທຶກ {0} ລາຍການແລ້ວ",
        'text_window_load_error': "ບໍ່ສາມາດໂຫຼດໜ້າຕ່າງຂໍ້ຄວາມໄດ້",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **ການປ້ອນຂໍ້ຄວາມ ແລະ ບລັອກຂໍ້ຄວາມ – ຄຳແນະນຳລະອຽດ**

        **1. ການແຊກ ແລະ ແກ້ໄຂຂໍ້ຄວາມ**
        - ຄລິກຂວາທີ່ຕຳແໜ່ງທີ່ຕ້ອງການໃນເອກະສານ ແລະ ເລືອກ "ແຊກຂໍ້ຄວາມ"
        - ຈະເປີດການສົນທະນາທີ່ທ່ານສາມາດປ້ອນ ແລະ ຈັດຮູບແບບຂໍ້ຄວາມ:
        • ຂະໜາດຕົວອັກສອນ, ຕົວໜາ, ຕົວອຽງ, ຂີດກ້ອງ
        • ສີຂໍ້ຄວາມ (ເລືອກໄດ້ອິດສະຫຼະ)
        • ຄວາມໂປ່ງໃສ (ຄວາມທຶບໃສ) ດ້ວຍແຖບເລື່ອນ
        • ການຕັດຂໍ້ຄວາມ (ຄວາມກວ້າງຕ່າງໆ ເຊັ່ນ ຄວາມກວ້າງໜ້າ, ແຄບ, ບໍ່ຕັດ)
        - ຫຼັງຢືນຢັນ, ຂໍ້ຄວາມຈະປາກົດຢູ່ຕຳແໜ່ງທີ່ຄລິກ. ທ່ານສາມາດຍ້າຍມັນດ້ວຍເມົ້າ ຫຼື ປຸ່ມລູກສອນ
        - ດັບເບິນຄລິກໃສ່ຂໍ້ຄວາມເພື່ອເປີດໂໝດແກ້ໄຂ; ກົດ ESC ເພື່ອອອກ

        **2. ການຈັດການບລັອກຂໍ້ຄວາມ (ແມ່ແບບ)**
        - ໃນການສົນທະນາຂໍ້ຄວາມ, ທ່ານຈະເຫັນລາຍການບລັອກຂໍ້ຄວາມທັງໝົດທີ່ບັນທຶກໄວ້ທາງຊ້າຍ
        - **ບັນທຶກບລັອກ:** ປ້ອນຂໍ້ຄວາມ, ຈັດຮູບແບບ ແລະ ຄລິກ "💾 ບັນທຶກເປັນບລັອກ" ປ້ອນຊື່ໄຟລ໌ (ໂດຍບໍ່ມີນາມສະກຸນ)
        - **ໂຫຼດບລັອກ:** ຄລິກຊື່ທີ່ຕ້ອງການໃນລາຍການ. ຂໍ້ຄວາມ ແລະ ການຈັດຮູບແບບຈະຖືກນຳໃຊ້ ແລະ ສາມາດປັບແຕ່ງໄດ້
        - **ລຶບ:** ຄລິກຂວາໃສ່ບລັອກເພື່ອລຶບ ຫຼື ປ່ຽນສະຖານະສ່ວນຕົວ

        **3. ບລັອກຂໍ້ຄວາມສ່ວນຕົວ (ລະຫັດຜ່ານຫຼັກ)**
        - ຖ້າທ່ານຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກແລ້ວ (ໃນການຕັ້ງຄ່າ → ການຈັດການລະຫັດຜ່ານ), ທ່ານສາມາດໝາຍບລັອກເປັນ "ສ່ວນຕົວ"
        - ເປີດໃຊ້ງານກ່ອງໝາຍ "ບລັອກຂໍ້ຄວາມສ່ວນຕົວ" ໃນການສົນທະນາກ່ອນບັນທຶກ
        - ບລັອກສ່ວນຕົວຈະສະແດງໃນລາຍການສະເພາະເມື່ອທ່ານປ້ອນລະຫັດຜ່ານຫຼັກໜຶ່ງຄັ້ງໃນແຕ່ລະເຊດຊັນ (ຢືນຢັນຕົວຕົນຜ່ານໄອຄອນກະແຈ ຫຼື ເມື່ອເຂົ້າເຖິງຄັ້ງທຳອິດ)
        - ວິທີນີ້ຊ່ວຍປ້ອງກັນບລັອກຂໍ້ຄວາມທີ່ເປັນຄວາມລັບຈາກການເຂົ້າເຖິງຂອງຜູ້ອື່ນ

        **4. ການແຊກກາກບອກ**
        - ຜ່ານເມນູບໍລິບົດ, ທ່ານສາມາດແຊກກາກບອກກຣາຟິກ (ເຊັ່ນ ສຳລັບກ່ອງໝາຍ)
        - ຂະໜາດ, ຄວາມໜາຂອງເສັ້ນ ແລະ ສີຂອງກາກບອກສາມາດປັບໄດ້ທົ່ວໂລກໃນການຕັ້ງຄ່າ (ເມນູ "ການຕັ້ງຄ່າ" → "ການຕັ້ງຄ່າກາກບອກ")
        - ຄລິກຂວາໃສ່ກາກບອກທີ່ມີຢູ່ເພື່ອປ່ຽນແປງແຍກຕ່າງຫາກ

        **5. ການດຳເນີນການກຸ່ມ**
        - ຖ້າທ່ານວາງຂໍ້ຄວາມ ຫຼື ກາກບອກຫຼາຍລາຍການໃນໜ້າດຽວ, ທ່ານສາມາດບັນທຶກ ຫຼື ຖິ້ມອົງປະກອບທັງໝົດພ້ອມກັນຜ່ານເມນູບໍລິບົດ (ຄລິກຂວາໃນໂໝດຂໍ້ຄວາມ)
        - ເມື່ອບັນທຶກ, ອົງປະກອບທັງໝົດຈະຖືກຝັງລົງໃນ PDF ແລະ ຄົງຢູ່ໃນຮູບແບບກຣາຟິກເວັກເຕີ

        **6. ປຸ່ມລັດໃນໂໝດຂໍ້ຄວາມ**
        - ປຸ່ມລູກສອນ: ຍ້າຍອົງປະກອບ
        - Ctrl+ປຸ່ມລູກສອນ: ຍ້າຍທີລະຫຼາຍ
        - Enter: ເປີດການສົນທະນາບັນທຶກ (ບັນທຶກທັງໝົດ / ປັບແຕ່ງ / ຖິ້ມ)
        - ESC: ຖິ້ມອົງປະກອບປັດຈຸບັນ
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 ການປ້ອນຂໍ້ຄວາມ ແລະ ບລັອກຂໍ້ຄວາມ – ຄຳແນະນຳລະອຽດ</strong></p>

        <p><strong>1. ການແຊກ ແລະ ແກ້ໄຂຂໍ້ຄວາມ</strong></p>
        <ul>
        <li>ຄລິກຂວາທີ່ຕຳແໜ່ງທີ່ຕ້ອງການໃນເອກະສານ ແລະ ເລືອກ "ແຊກຂໍ້ຄວາມ"</li>
        <li>ຈະເປີດການສົນທະນາທີ່ທ່ານສາມາດປ້ອນ ແລະ ຈັດຮູບແບບຂໍ້ຄວາມ:<br/>
        • ຂະໜາດຕົວອັກສອນ, ຕົວໜາ, ຕົວອຽງ, ຂີດກ້ອງ<br/>
        • ສີຂໍ້ຄວາມ (ເລືອກໄດ້ອິດສະຫຼະ)<br/>
        • ຄວາມໂປ່ງໃສ (ຄວາມທຶບໃສ) ດ້ວຍແຖບເລື່ອນ<br/>
        • ການຕັດຂໍ້ຄວາມ (ຄວາມກວ້າງຕ່າງໆ ເຊັ່ນ ຄວາມກວ້າງໜ້າ, ແຄບ, ບໍ່ຕັດ)</li>
        <li>ຫຼັງຢືນຢັນ, ຂໍ້ຄວາມຈະປາກົດຢູ່ຕຳແໜ່ງທີ່ຄລິກ. ທ່ານສາມາດຍ້າຍມັນດ້ວຍເມົ້າ ຫຼື ປຸ່ມລູກສອນ</li>
        <li>ດັບເບິນຄລິກໃສ່ຂໍ້ຄວາມເພື່ອເປີດໂໝດແກ້ໄຂ; ກົດ ESC ເພື່ອອອກ</li>
        </ul>

        <p><strong>2. ການຈັດການບລັອກຂໍ້ຄວາມ (ແມ່ແບບ)</strong></p>
        <ul>
        <li>ໃນການສົນທະນາຂໍ້ຄວາມ, ທ່ານຈະເຫັນລາຍການບລັອກຂໍ້ຄວາມທັງໝົດທີ່ບັນທຶກໄວ້ທາງຊ້າຍ</li>
        <li><strong>ບັນທຶກບລັອກ:</strong> ປ້ອນຂໍ້ຄວາມ, ຈັດຮູບແບບ ແລະ ຄລິກ "💾 ບັນທຶກເປັນບລັອກ" ປ້ອນຊື່ໄຟລ໌ (ໂດຍບໍ່ມີນາມສະກຸນ)</li>
        <li><strong>ໂຫຼດບລັອກ:</strong> ຄລິກຊື່ທີ່ຕ້ອງການໃນລາຍການ. ຂໍ້ຄວາມ ແລະ ການຈັດຮູບແບບຈະຖືກນຳໃຊ້ ແລະ ສາມາດປັບແຕ່ງໄດ້</li>
        <li><strong>ລຶບ:</strong> ຄລິກຂວາໃສ່ບລັອກເພື່ອລຶບ ຫຼື ປ່ຽນສະຖານະສ່ວນຕົວ</li>
        </ul>

        <p><strong>3. ບລັອກຂໍ້ຄວາມສ່ວນຕົວ (ລະຫັດຜ່ານຫຼັກ)</strong></p>
        <ul>
        <li>ຖ້າທ່ານຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກແລ້ວ (ໃນການຕັ້ງຄ່າ → ການຈັດການລະຫັດຜ່ານ), ທ່ານສາມາດໝາຍບລັອກເປັນ "ສ່ວນຕົວ"</li>
        <li>ເປີດໃຊ້ງານກ່ອງໝາຍ "ບລັອກຂໍ້ຄວາມສ່ວນຕົວ" ໃນການສົນທະນາກ່ອນບັນທຶກ</li>
        <li>ບລັອກສ່ວນຕົວຈະສະແດງໃນລາຍການສະເພາະເມື່ອທ່ານປ້ອນລະຫັດຜ່ານຫຼັກໜຶ່ງຄັ້ງໃນແຕ່ລະເຊດຊັນ (ຢືນຢັນຕົວຕົນຜ່ານໄອຄອນກະແຈ ຫຼື ເມື່ອເຂົ້າເຖິງຄັ້ງທຳອິດ)</li>
        <li>ວິທີນີ້ຊ່ວຍປ້ອງກັນບລັອກຂໍ້ຄວາມທີ່ເປັນຄວາມລັບຈາກການເຂົ້າເຖິງຂອງຜູ້ອື່ນ</li>
        </ul>

        <p><strong>4. ການແຊກກາກບອກ</strong></p>
        <ul>
        <li>ຜ່ານເມນູບໍລິບົດ, ທ່ານສາມາດແຊກກາກບອກກຣາຟິກ (ເຊັ່ນ ສຳລັບກ່ອງໝາຍ)</li>
        <li>ຂະໜາດ, ຄວາມໜາຂອງເສັ້ນ ແລະ ສີຂອງກາກບອກສາມາດປັບໄດ້ທົ່ວໂລກໃນການຕັ້ງຄ່າ (ເມນູ "ການຕັ້ງຄ່າ" → "ການຕັ້ງຄ່າກາກບອກ")</li>
        <li>ຄລິກຂວາໃສ່ກາກບອກທີ່ມີຢູ່ເພື່ອປ່ຽນແປງແຍກຕ່າງຫາກ</li>
        </ul>

        <p><strong>5. ການດຳເນີນການກຸ່ມ</strong></p>
        <ul>
        <li>ຖ້າທ່ານວາງຂໍ້ຄວາມ ຫຼື ກາກບອກຫຼາຍລາຍການໃນໜ້າດຽວ, ທ່ານສາມາດບັນທຶກ ຫຼື ຖິ້ມອົງປະກອບທັງໝົດພ້ອມກັນຜ່ານເມນູບໍລິບົດ (ຄລິກຂວາໃນໂໝດຂໍ້ຄວາມ)</li>
        <li>ເມື່ອບັນທຶກ, ອົງປະກອບທັງໝົດຈະຖືກຝັງລົງໃນ PDF ແລະ ຄົງຢູ່ໃນຮູບແບບກຣາຟິກເວັກເຕີ</li>
        </ul>

        <p><strong>6. ປຸ່ມລັດໃນໂໝດຂໍ້ຄວາມ</strong></p>
        <ul>
        <li>ປຸ່ມລູກສອນ: ຍ້າຍອົງປະກອບ</li>
        <li>Ctrl+ປຸ່ມລູກສອນ: ຍ້າຍທີລະຫຼາຍ</li>
        <li>Enter: ເປີດການສົນທະນາບັນທຶກ (ບັນທຶກທັງໝົດ / ປັບແຕ່ງ / ຖິ້ມ)</li>
        <li>ESC: ຖິ້ມອົງປະກອບປັດຈຸບັນ</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "ການຕັ້ງຄ່າກາກບອກ",
        'cross_properties': "ຄຸນສົມບັດກາກບອກ",
        'cross_size': "ຂະໜາດ (px):",
        'cross_line_width': "ຄວາມໜາຂອງເສັ້ນ:",
        'cross_color': "ສີ:",
        'cross_choose_color': "ເລືອກ",
        'cross_fine_tuning': "ປັບລະອຽດເມື່ອບັນທຶກ (ພິກເຊວ)",
        'cross_offset_x': "ອອບເຊັດ X:",
        'cross_offset_y': "ອອບເຊັດ Y:",
        'cross_offset_x_tooltip': "ຄ່າລົບຈະເລື່ອນກາກບອກໄປຊ້າຍເມື່ອບັນທຶກ, ຄ່າບວກໄປຂວາ",
        'cross_offset_y_tooltip': "ຄ່າລົບຈະເລື່ອນກາກບອກຂຶ້ນເມື່ອບັນທຶກ, ຄ່າບວກລົງ",
        'cross_preview': "ຕົວຢ່າງ",
        'cross_save': "ໃຊ້ການຕັ້ງຄ່າ",
        'cross_customized': "ປັບກາກບອກແລ້ວ",
        'cross_settings_applied': "ບັນທຶກການຕັ້ງຄ່າກາກບອກ\nຂະໜາດ: {0}px, ຄວາມໜາເສັ້ນ: {1}px\n{2}",
        'cross_updated_count': "ອັບເດດກາກບອກທີ່ມີຢູ່ {0} ລາຍການແລ້ວ",
        'cross_no_crosses': "ບໍ່ພົບກາກບອກທີ່ມີຢູ່",
        'cross_settings_applied_all': "ໃຊ້ການຕັ້ງຄ່າກາກບອກກັບກາກບອກທັງໝົດ {0} ລາຍການ",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "ການຕັ້ງຄ່າລາຍເຊັນ",
        'signature_1': "ລາຍເຊັນ 1",
        'signature_2': "ລາຍເຊັນ 2",
        'signature_select': "ເລືອກລາຍເຊັນ",
        'signature_add': "➕ ເພີ່ມລາຍເຊັນໃໝ່...",
        'signature_size': "ຂະໜາດສຳລັບລາຍເຊັນ {0} (%):",
        'signature_common': "ການຕັ້ງຄ່າທົ່ວໄປ",
        'signature_timestamp': "ເພີ່ມປະທັບເວລາອັດຕະໂນມັດ",
        'signature_location': "ສະຖານທີ່ເລີ່ມຕົ້ນ:",
        'signature_timestamp_size': "ຂະໜາດຕົວອັກສອນປະທັບເວລາ:",
        'signature_no_files': "-- ບໍ່ພົບລາຍເຊັນ --",
        'signature_insert': "ແຊກລາຍເຊັນ",
        'signature_insert_1': "ແຊກລາຍເຊັນ 1",
        'signature_insert_2': "ແຊກລາຍເຊັນ 2",
        'signature_customize': " ປັບແຕ່ງລາຍເຊັນນີ້",
        'signature_discard': " ຖິ້ມລາຍເຊັນນີ້",
        'signature_save_all': " ບັນທຶກລາຍເຊັນທັງໝົດ",
        'signature_discard_all': " ຖິ້ມລາຍເຊັນທັງໝົດ",
        'signature_guide_title': "ລາຍເຊັນ - ຄຳແນະນຳ",
        'signature_guide': """
📝 ລາຍເຊັນ - ຄຳແນະນຳດ່ວນ

- ຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ
- ກຳນົດຄ່າລາຍເຊັນໃນເມນູການຕັ້ງຄ່າ
  (ຂະໜາດ, ປະທັບເວລາ ...)
- ແຊກດ້ວຍຄລິກຂວາທີ່ຕຳແໜ່ງທີ່ຕ້ອງການ
  (ຕ້ອງໃຊ້ລະຫັດຜ່ານຫຼັກໜຶ່ງຄັ້ງຕໍ່ເຊດຊັນ)
- ຍ້າຍລາຍເຊັນດ້ວຍເມົ້າ ຫຼື ປຸ່ມລູກສອນ
- ສາມາດແຊກລາຍເຊັນຫຼາຍລາຍການຕໍ່ເນື່ອງກັນ
- ແຕ່ລະລາຍເຊັນສາມາດປັບແຕ່ງແຍກຕ່າງຫາກ
- ຖິ້ມລາຍເຊັນແຕ່ລະລາຍການ
- ບັນທຶກ / ຖິ້ມລາຍເຊັນທັງໝົດພ້ອມກັນ
- ຫຼື ໃຊ້ແຖບເມນູກໍ່ໄດ້
        """,
        'signature_placeholder': "ບໍ່ມີຕົວຢ່າງ",
        'signature_info': "ລາຍເຊັນ {0}: {1}×{2} px ({3}% ຂອງ {4}×{5})",
        'signature_info_placeholder': "ການຕັ້ງຄ່າສຳລັບລາຍເຊັນ {0}",
        'signature_inserted': "ແຊກລາຍເຊັນ {0} ທີ່ໜ້າ {1}",
        'signature_deleted': "ລຶບລາຍເຊັນ",
        'signature_copied': "ສຳເນົາລາຍເຊັນ",
        'signature_pasted': "ວາງລາຍເຊັນ {0}",
        'signature_saved': "ແຊກລາຍເຊັນ {0} ລາຍການລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'signature_saved_voice': "ບັນທຶກລາຍເຊັນ {0} ລາຍການ",
        'mode_replace_signature_format': "ສິ້ນສຸດໂໝດ ແລະ ແຊກລາຍເຊັນ {0}",
        'mode_conflict_voice_signature': "ໂໝດ {0} ເປີດຢູ່. ສິ້ນສຸດ ແລະ ແຊກລາຍເຊັນ?",
        'signature_not_configured': "ບໍ່ໄດ້ກຳນົດຄ່າລາຍເຊັນ {0}",
        'signature_file_not_found': "ບໍ່ພົບໄຟລ໌ລາຍເຊັນ",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "ບໍ່ມີລາຍເຊັນທີ່ສຳເນົາໄວ້",
        'no_signatures_to_save': "ບໍ່ມີລາຍເຊັນທີ່ຈະບັນທຶກ",
        'signature_save_question': "ບັນທຶກລາຍເຊັນທັງໝົດ, ປັບແຕ່ງ ຫຼື ຖິ້ມອັນນີ້?",
        'signatures_saved_title': "ບັນທຶກລາຍເຊັນແລ້ວ",
        'signatures_saved': "ແຊກລາຍເຊັນ {0} ລາຍການລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'signatures_saved_voice': "ບັນທຶກລາຍເຊັນ {0} ລາຍການ",
        'all_signatures_discarded': "ຖິ້ມລາຍເຊັນທັງໝົດ",
        'signature_settings_saved': "ບັນທຶກການຕັ້ງຄ່າລາຍເຊັນ",
        'signature_cancelled': "ຖິ້ມລາຍເຊັນ",
        'signature_active_title': "ລາຍເຊັນກຳລັງເຮັດວຽກ",
        'signature_replace_question': "ມີລາຍເຊັນທີ່ກຳລັງເຮັດວຽກຢູ່ແລ້ວ.\n\nທ່ານຕ້ອງການແທນທີ່ລາຍເຊັນປັດຈຸບັນບໍ່?",
        'signature_replace': "ແທນທີ່ລາຍເຊັນ",
        'signature_replace_voice': "ແທນທີ່ລາຍເຊັນປັດຈຸບັນ ຫຼື ຍົກເລີກ?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "ການຕັ້ງຄ່າຮູບພາບ",
        'image_common': "ການຕັ້ງຄ່າຮູບພາບທົ່ວໄປ",
        'image_keep_aspect': "ຮັກສາອັດຕາສ່ວນເມື່ອລາກ",
        'image_default_size': "ຂະໜາດເລີ່ມຕົ້ນ (%):",
        'image_dark_invert': "ກັບສີຮູບພາບໃນໂໝດມືດ",
        'image_dark_invert_tooltip': "ເປີດ: ຮູບພາບຈະຖືກກັບສີເພື່ອໃຫ້ເຫັນໄດ້ດີຂຶ້ນ",
        'image_fine_tuning': "ປັບລະອຽດ (ພິກເຊວ)",
        'image_offset_x': "ອອບເຊັດ X:",
        'image_offset_y': "ອອບເຊັດ Y:",
        'image_offset_x_tooltip': "ຄ່າລົບຈະເລື່ອນຮູບພາບໄປຊ້າຍເມື່ອບັນທຶກ, ຄ່າບວກໄປຂວາ",
        'image_offset_y_tooltip': "ຄ່າລົບຈະເລື່ອນຮູບພາບຂຶ້ນເມື່ອບັນທຶກ, ຄ່າບວກລົງ",
        'image_select': "ເລືອກຮູບພາບ",
        'image_insert': "ແຊກຮູບພາບ",
        'image_customize': " ປັບແຕ່ງຮູບພາບນີ້",
        'image_aspect': " ຮັກສາອັດຕາສ່ວນ",
        'image_discard': " ຖິ້ມຮູບພາບນີ້",
        'image_save_all': " ບັນທຶກຮູບພາບທັງໝົດ",
        'image_discard_all': " ຖິ້ມຮູບພາບທັງໝົດ",
        'image_filter': "ຮູບພາບ",
        'image_guide_title': "ແຊກຮູບພາບ - ຄຳແນະນຳ",
        'image_guide': """
📷 ແຊກຮູບພາບໃນ PDF - ຄຳແນະນຳດ່ວນ:

1. ຄລິກຂວາທີ່ຕຳແໜ່ງທີ່ຕ້ອງການ
2. "ແຊກຮູບພາບ" → ເລືອກຮູບພາບ
3. ວາງຮູບພາບ: ລາກດ້ວຍເມົ້າ
4. ປັບຂະໜາດ: ລາກທີ່ມຸມ/ຂອບ
5. ຮັກສາອັດຕາສ່ວນ: ກົດປຸ່ມ [A]
6. ປັບແຕ່ງເພີ່ມເຕີມ: ຄລິກຂວາໃສ່ຮູບພາບ

ເຄັດລັບ: ໃນເມນູບໍລິບົດທ່ານສາມາດປັບການຕັ້ງຄ່າໄດ້
        """,
        'image_inserted': "ແຊກຮູບພາບ {0} ທີ່ໜ້າ {1}",
        'image_deleted': "ຖິ້ມຮູບພາບ",
        'image_copied': "ສຳເນົາຮູບພາບ",
        'image_pasted': "ວາງຮູບພາບ",
        'image_saved': "ແຊກຮູບພາບ {0} ລາຍການລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'image_saved_voice': "ບັນທຶກຮູບພາບ {0} ລາຍການ",
        'image_aspect_on': "ເປີດ",
        'image_aspect_off': "ປິດ",
        'image_aspect_toggle': "ຮັກສາອັດຕາສ່ວນ {0}",
        'image_reset': "ຣີເຊັດຮູບພາບເປັນຂະໜາດເດີມ",
        'image_replaced': "ແທນທີ່ຮູບພາບ",
        'image_invalid': "ຮູບພາບບໍ່ຖືກຕ້ອງ",
        'mode_replace_image': "ແຊກຮູບພາບ",
        'mode_conflict_voice_image': "ໂໝດ {0} ເປີດຢູ່. ສິ້ນສຸດ ແລະ ແຊກຮູບພາບ?",
        'image_active_title': "ຮູບພາບກຳລັງເຮັດວຽກ",
        'image_replace_question': "ມີຮູບພາບທີ່ກຳລັງເຮັດວຽກຢູ່ແລ້ວ.\n\nທ່ານຕ້ອງການແທນທີ່ຮູບພາບປັດຈຸບັນບໍ່?",
        'image_replace': "ແທນທີ່ຮູບພາບ",
        'image_replace_voice': "ແທນທີ່ຮູບພາບປັດຈຸບັນ ຫຼື ຍົກເລີກ?",
        'image_filter_all': "ຮູບພາບ (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;ໄຟລ໌ທັງໝົດ (*.*)",
        'no_copied_image': "ບໍ່ມີຮູບພາບທີ່ສຳເນົາໄວ້",
        'image_discarded': "ຖິ້ມຮູບພາບ",
        'image_save_question': "ບັນທຶກຮູບພາບທັງໝົດ, ປັບແຕ່ງ ຫຼື ຖິ້ມອັນນີ້?",
        'no_images_to_save': "ບໍ່ມີຮູບພາບທີ່ຈະບັນທຶກ",
        'no_valid_images': "ບໍ່ມີຮູບພາບທີ່ຖືກຕ້ອງສຳລັບບັນທຶກ",
        'images_saved_title': "ບັນທຶກຮູບພາບແລ້ວ",
        'images_saved': "ແຊກຮູບພາບ {0} ລາຍການລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'images_saved_voice': "ບັນທຶກຮູບພາບ {0} ລາຍການ",
        'all_images_discarded': "ຖິ້ມຮູບພາບທັງໝົດ",
        'image_settings_updated': "ອັບເດດການຕັ້ງຄ່າຮູບພາບ",
        'image_replace_title': "ເລືອກຮູບພາບໃໝ່",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "ການຕັ້ງຄ່າຮູບຮ່າງ",
        'form_basic': "ການຕັ້ງຄ່າພື້ນຖານ",
        'form_default_type': "ປະເພດເລີ່ມຕົ້ນ:",
        'form_rectangle': "ສີ່ແຈສາກ",
        'form_ellipse': "ຮູບໄຂ່",
        'form_line': "ເສັ້ນ",
        'form_arrow': "ລູກສອນ",
        'form_line_width': "ຄວາມໜາຂອງເສັ້ນ:",
        'form_colors': "ສີ",
        'form_line_color': "ສີເສັ້ນ:",
        'form_fill_color': "ສີພື້ນ:",
        'form_choose_color': "ເລືອກ",
        'form_transparent': "ພື້ນຫຼັງໂປ່ງໃສ (ສະເພາະເສັ້ນ)",
        'form_filled': "ເຕີມສີ",
        'form_dark_mode': "ໂໝດມືດ",
        'form_dark_invert': "ກັບສີໃນໂໝດມືດ",
        'form_fine_tuning': "ປັບລະອຽດ (ພິກເຊວ)",
        'form_offset_x': "ອອບເຊັດ X:",
        'form_offset_y': "ອອບເຊັດ Y:",
        'form_offset_x_tooltip': "ຄ່າລົບຈະເລື່ອນຮູບຮ່າງໄປຊ້າຍເມື່ອບັນທຶກ, ຄ່າບວກໄປຂວາ",
        'form_offset_y_tooltip': "ຄ່າລົບຈະເລື່ອນຮູບຮ່າງຂຶ້ນເມື່ອບັນທຶກ, ຄ່າບວກລົງ",
        'form_preview': "ຕົວຢ່າງ",
        'form_insert': "ແຊກຮູບຮ່າງ",
        'form_rectangle_insert': "ສີ່ແຈສາກ",
        'form_ellipse_insert': "ຮູບໄຂ່/ວົງມົນ",
        'form_line_insert': "ເສັ້ນ (2 ຄລິກ)",
        'form_arrow_insert': "ລູກສອນ (2 ຄລິກ)",
        'form_customize': " ປັບແຕ່ງຮູບຮ່າງນີ້",
        'form_transparent_toggle': " ພື້ນຫຼັງໂປ່ງໃສ",
        'form_discard': " ຖິ້ມຮູບຮ່າງນີ້",
        'form_save_all': " ບັນທຶກຮູບຮ່າງທັງໝົດ",
        'form_discard_all': " ຖິ້ມຮູບຮ່າງທັງໝົດ",
        'form_guide_title': "ແຊກຮູບຮ່າງ - ຄຳແນະນຳ",
        'form_guide': """
📐 ແຊກຮູບຮ່າງໃນ PDF - ຄຳແນະນຳດ່ວນ:

1. ເລືອກປະເພດ (ສີ່ແຈສາກ, ຮູບໄຂ່, ເສັ້ນ, ລູກສອນ)
2. ຄລິກທີ່ຕຳແໜ່ງ
   - ສຳລັບສີ່ແຈສາກ/ຮູບໄຂ່: ຄລິກຄັ້ງດຽວວາງຮູບຮ່າງ
   - ສຳລັບເສັ້ນ/ລູກສອນ: ຄລິກສອງຄັ້ງສຳລັບຈຸດເລີ່ມ ແລະ ຈຸດສິ້ນສຸດ
3. ວາງຮູບຮ່າງ: ລາກດ້ວຍເມົ້າ
4. ປັບຂະໜາດ: ລາກທີ່ມຸມ/ຂອບ
5. ບັນທຶກຮູບຮ່າງ: Enter
6. ຖິ້ມຮູບຮ່າງ: ESC
7. ປັບແຕ່ງເພີ່ມເຕີມ: ຄລິກຂວາໃສ່ຮູບຮ່າງ

ເຄັດລັບ: ໃນເມນູບໍລິບົດທ່ານສາມາດປັບການຕັ້ງຄ່າໄດ້
        """,
        'form_inserted': "ແຊກ {0} ທີ່ໜ້າ {1}",
        'form_deleted': "ລຶບຮູບຮ່າງ",
        'form_copied': "ສຳເນົາຮູບຮ່າງ",
        'form_pasted': "ວາງຮູບຮ່າງ",
        'form_saved': "ແຊກຮູບຮ່າງ {0} ລາຍການລົງໃນ PDF\n\nໂຫຼດ PDF ໃໝ່...",
        'form_saved_voice': "ບັນທຶກຮູບຮ່າງ {0} ລາຍການ",
        'form_reset': "ຣີເຊັດຮູບຮ່າງເປັນຂະໜາດເລີ່ມຕົ້ນ",
        'form_transparent_on': "ເປີດ",
        'form_transparent_off': "ປິດ",
        'form_transparent_toggled': "ພື້ນຫຼັງໂປ່ງໃສ {0}",
        'form_line_cancel': "ຍົກເລີກການແຕ້ມເສັ້ນ",
        'form_second_click': "ຕອນນີ້ຄລິກຈຸດສິ້ນສຸດສຳລັບ {0}",
        'mode_replace_form': "ແຊກຮູບຮ່າງ",
        'mode_conflict_voice_form': "ໂໝດ {0} ເປີດຢູ່. ສິ້ນສຸດ ແລະ ແຊກຮູບຮ່າງ?",
        'form_settings_updated': "ອັບເດດການຕັ້ງຄ່າຮູບຮ່າງ",
        'form_unknown': "ຮູບຮ່າງ",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. ຄລິກທີ່ຕຳແໜ່ງເລີ່ມຕົ້ນ",
        'form_line_guide_2': "2. ຄລິກທີ່ຕຳແໜ່ງສິ້ນສຸດ",
        'form_line_guide_3': "ເສັ້ນຈະຖືກແຕ້ມລະຫວ່າງສອງຈຸດ",
        'form_line_status_1': "ລໍຖ້າຄລິກທຳອິດ...",
        'form_line_status_2': "ຕັ້ງຈຸດທຳອິດແລ້ວ: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "ຕອນນີ້ຄລິກຈຸດສິ້ນສຸດ...",
        'form_line_status_4': "ຕັ້ງຈຸດທັງສອງແລ້ວ\nຄລິກ 'ສຳເລັດ' ເພື່ອບັນທຶກ",
        'form_line_reset': "ຣີເຊັດ",
        'form_line_finish': "ສຳເລັດ",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "ສຳເນົາ (Cmd+C)",
        'paste': "ວາງ (Cmd+V)",
        'copied': "ສຳເນົາ: {0}",
        'no_element_to_copy': "ບໍ່ມີລາຍການທີ່ເລືອກສຳລັບສຳເນົາ",
        'no_copied_data': "ບໍ່ມີຂໍ້ມູນທີ່ສຳເນົາໄວ້",
        'no_valid_position': "ບໍ່ມີຕຳແໜ່ງທີ່ຖືກຕ້ອງສຳລັບວາງ",
        'copy_text': "ສຳເນົາຂໍ້ຄວາມ",
        'copy_image': "ສຳເນົາຮູບພາບ",
        'copy_form': "ສຳເນົາຮູບຮ່າງ",
        'copy_signature': "ສຳເນົາລາຍເຊັນ",
        'element_text': "ຂໍ້ຄວາມ",
        'element_image': "ຮູບພາບ",
        'element_form': "ຮູບຮ່າງ",
        'element_signature': "ລາຍເຊັນ",
        'element_unknown': "ລາຍການ",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "ຂໍ້ຂັດແຍ່ງໂໝດ",
        'mode_conflict_message': "ໂໝດ '{0}' ກຳລັງເຮັດວຽກຢູ່.\n\nທ່ານຕ້ອງການສິ້ນສຸດ ແລະ {1} ບໍ່?",
        'mode_replace': "ສິ້ນສຸດໂໝດ ແລະ {0}",
        'mode_cancel': "ຍົກເລີກ",
        'mode_replace_text': "ແຊກຂໍ້ຄວາມ",
        'mode_replace_cross': "ແຊກກາກບອກ",
        'mode_replace_signature': "ແຊກລາຍເຊັນ",
        'mode_replace_image': "ແຊກຮູບພາບ",
        'mode_replace_form': "ແຊກຮູບຮ່າງ",
        'mode_conflict_voice': "ໂໝດ {0} ເປີດຢູ່. ສິ້ນສຸດ ແລະ ແຊກຂໍ້ຄວາມ?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "ປ້ອນຂໍ້ຄວາມ",
        'active_mode_signature': "ລາຍເຊັນ",
        'active_mode_image': "ຮູບພາບ",
        'active_mode_form': "ຮູບຮ່າງ",
        'active_mode_and': " ແລະ ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "ແຊກ",
        'insert_another_text': "ແຊກຂໍ້ຄວາມ",
        'insert_another_cross': "ແຊກກາກບອກ",
        'insert_another_signature_1': "ລາຍເຊັນ 1",
        'insert_another_signature_2': "ລາຍເຊັນ 2",
        'insert_another_image': "ແຊກຮູບພາບ",
        'insert_another_form_rect': "ສີ່ແຈສາກ",
        'insert_another_form_ellipse': "ຮູບໄຂ່",
        'insert_another_form_line': "ເສັ້ນ (2 ຄລິກ)",
        'insert_another_form_arrow': "ລູກສອນ (2 ຄລິກ)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "ບັນທຶກ {0}",
        'save_dialog_message': "ຈະບັນທຶກ {0} ທີ່ໜ້າ {1}\n\nທ່ານຕ້ອງການດຳເນີນການຕໍ່ໄປແນວໃດ?",
        'save_all': "ບັນທຶກ {0} ທັງໝົດ",
        'save_single': "ບັນທຶກ {0}",
        'save_customize': "ປັບແຕ່ງ {0}",
        'save_discard': "ຖິ້ມ {0} ນີ້",
        'save_continue': "ແກ້ໄຂຕໍ່",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " ໄປທີ່ໜ້າ {0}",
        'context_rotate': " ໝຸນໜ້າ {0}",
        'context_delete': " ລຶບໜ້າ {0}",
        'context_export': " ສົ່ງອອກໜ້າ {0}",
        'context_mark_as': " ໝາຍໜ້າເປັນ...",
        'context_mark_empty': " ໜ້າວ່າງ",
        'context_unmark_empty': " ບໍ່ວ່າງອີກຕໍ່ໄປ",
        'context_mark_export': " ໝາຍສຳລັບສົ່ງອອກ",
        'context_unmark_export': " ຍົກເລີກເຄື່ອງໝາຍສົ່ງອອກ",
        'context_batch_actions': " ການດຳເນີນການກຸ່ມ",
        'context_batch_delete_empty': " ລຶບໜ້າວ່າງທັງໝົດ {0} ໜ້າ",
        'context_batch_export_single': " ສົ່ງອອກ {0} ໜ້າທັງໝົດ (ໄຟລ໌ດຽວ)",
        'context_batch_export_split': " ສົ່ງອອກ {0} ໜ້າທັງໝົດ (ແຍກໄຟລ໌)",
        'context_drag_start': " ເລີ່ມລາກແລ້ວວາງ",
        'context_drag_stop': " ຢຸດລາກແລ້ວວາງ",
        'context_insert': " ແຊກ",
        'context_insert_pages': " ແຊກໜ້າ",
        'context_zoom': "ຊູມ",
        'discard_mixed': "ຖິ້ມ {0} {1} ແລະ {2} {3} ທັງໝົດ",
        'save_mixed': "ບັນທຶກ {0} {1} ແລະ {2} {3}",
        'discard_texts': "ຖິ້ມຂໍ້ຄວາມ {0} ທັງໝົດ",
        'discard_text_single': "ຖິ້ມ 1 ຂໍ້ຄວາມ",
        'save_texts': "ບັນທຶກ {0} ຂໍ້ຄວາມ",
        'save_text_single': "ບັນທຶກ 1 ຂໍ້ຄວາມ",
        'discard_crosses': "ຖິ້ມກາກບອກ {0} ທັງໝົດ",
        'discard_cross_single': "ຖິ້ມ 1 ກາກບອກ",
        'save_crosses': "ບັນທຶກ {0} ກາກບອກ",
        'save_cross_single': "ບັນທຶກ 1 ກາກບອກ",
        'discard_signatures': "ຖິ້ມລາຍເຊັນ {0} ທັງໝົດ",
        'save_signature_single': "ບັນທຶກ 1 ລາຍເຊັນ",
        'save_signatures': "ບັນທຶກ {0} ລາຍເຊັນ",
        'discard_images': "ຖິ້ມຮູບພາບ {0} ທັງໝົດ",
        'save_image_single': "ບັນທຶກ 1 ຮູບພາບ",
        'save_images': "ບັນທຶກ {0} ຮູບພາບ",
        'discard_forms': "ຖິ້ມຮູບຮ່າງ {0} ທັງໝົດ",
        'save_form_single': "ບັນທຶກ 1 ຮູບຮ່າງ",
        'save_forms': "ບັນທຶກ {0} ຮູບຮ່າງ",
        'cross_discard': "ຖິ້ມກາກບອກນີ້",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 ຂໍ້ມູນການສົ່ງອອກ/ນຳເຂົ້າ",
        'export_what': "📋 ສົ່ງອອກຫຍັງ?",
        'export_general': "ການຕັ້ງຄ່າທົ່ວໄປ",
        'export_general_items': "• ສຽງເວົ້າ (ເປີດ/ປິດ, ຄວາມໄວ)\n• ໂໝດມືດ/ສະຫວ່າງ\n• ການຕັ້ງຄ່າສຳຮອງ\n• ການຕັ້ງຄ່າ OCR",
        'export_image_form': "ການຕັ້ງຄ່າຮູບພາບ ແລະ ຮູບຮ່າງ",
        'export_image_form_items': "• ການຕັ້ງຄ່າຮູບພາບ (ອັດຕາສ່ວນ, ຂະໜາດເລີ່ມຕົ້ນ)\n• ການຕັ້ງຄ່າຮູບຮ່າງ (ຄວາມໜາເສັ້ນ, ສີ)\n• ການຕັ້ງຄ່າລາຍເຊັນ (ເສັ້ນທາງ, ຂະໜາດ, ປະທັບເວລາ)",
        'export_passwords': "ຖານຂໍ້ມູນລະຫັດຜ່ານ",
        'export_passwords_items': "• ລະຫັດຜ່ານ PDF ທີ່ບັນທຶກໄວ້ທັງໝົດ\n• ສາມາດເລືອກເຂົ້າລະຫັດ ຫຼື ຖອດລະຫັດໄດ້",
        'export_master': "ການຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ",
        'export_master_items': "• ແຮດລະຫັດຜ່ານຫຼັກ\n• ການຕັ້ງຄ່າສຳລັບລາຍເຊັນ/ບລັອກຂໍ້ຄວາມ",
        'export_signatures': "ລາຍເຊັນ ແລະ ບລັອກຂໍ້ຄວາມ",
        'export_signatures_items': "• ໄຟລ໌ຮູບພາບທັງໝົດ (ລາຍເຊັນ)\n• ບລັອກຂໍ້ຄວາມທັງໝົດພ້ອມການຈັດຮູບແບບ\n• ເຄື່ອງໝາຍສ່ວນຕົວ/ສາທາລະນະ",
        'export_import_warning': "⚠️ ໝາຍເຫດສຳຄັນ",
        'export_import_note': "• ເມື່ອນຳເຂົ້າ, ການຕັ້ງຄ່າປັດຈຸບັນທັງໝົດຈະຖືກຂຽນທັບ\n• ຕ້ອງຣີສະຕາດແອັບພລິເຄຊັນ\n• ລາຍເຊັນ/ບລັອກຂໍ້ຄວາມທີ່ມີຢູ່ຈະຖືກແທນທີ່",
        'export_master_note': "• ຖ້າຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ, ທ່ານສາມາດເລືອກ:\n  - ຖອດລະຫັດ (ລະຫັດຜ່ານເປັນຂໍ້ຄວາມທຳມະດາ)\n  - ເຂົ້າລະຫັດ (ອ່ານໄດ້ດ້ວຍລະຫັດຫຼັກເທົ່ານັ້ນ)",
        'export_security': "• ໄຟລ໌ ZIP ທີ່ສົ່ງອອກມີຂໍ້ມູນທີ່ເປັນຄວາມລັບ\n• ກະລຸນາເກັບໄວ້ຢ່າງປອດໄພ (ເຊັ່ນ ແຟລຊໄດຣຟ໌ທີ່ເຂົ້າລະຫັດ)\n• ຖ້າໄຟລ໌ຫາຍ: ລະຫັດຜ່ານບໍ່ສາມາດກູ້ຄືນໄດ້",
        'export_format': "📁 ຮູບແບບສົ່ງອອກ",
        'export_format_desc': "ການຕັ້ງຄ່າຈະຖືກບັນທຶກໃນໄຟລ໌ ZIP ດຽວ:",
        'export_filename': "PDFDarkView_ການຕັ້ງຄ່າ_YYYYMMDD_HHMMSS.zip",
        'export_success': "ສົ່ງອອກການຕັ້ງຄ່າສຳເລັດ",
        'export_failed': "ສົ່ງອອກບໍ່ສຳເລັດ",
        'export_import_question': "ທ່ານຕ້ອງການຣີສະຕາດແອັບພລິເຄຊັນດຽວນີ້ບໍ່?",
        'export_password_question': "ຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກແລ້ວ.\n\nທ່ານຕ້ອງການສົ່ງອອກລະຫັດຜ່ານແບບຖອດລະຫັດບໍ່?\n(ຖ້າບໍ່, ຈະສົ່ງອອກແບບເຂົ້າລະຫັດ)",
        'export_decrypt': "ສົ່ງອອກແບບຖອດລະຫັດ",
        'export_encrypt': "ສົ່ງອອກແບບເຂົ້າລະຫັດ",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " ຂໍ້ມູນ",
        'info_title': "ກ່ຽວກັບ PDF Dark View",
        'info_version': "ຮຸ່ນ",
        'info_author': "ພັດທະນາໂດຍ Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "ກ່ຽວກັບ",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ເປັນຕົວເບິ່ງ PDF ທີ່ສາມາດເຂົ້າເຖິງໄດ້, ຖືກພັດທະນາສະເພາະສຳລັບຜູ້ທີ່ມີຄວາມບົກພ່ອງທາງດ້ານສາຍຕາ.</p>

            <p><strong>ຄຸນສົມບັດຫຼັກ:</strong></p>
            <ul>
                <li>ໜ້າຕາທີ່ມີຄວາມຄົມຊັດສູງ, ປັບແຕ່ງໄດ້</li>
                <li>ການຄວບຄຸມແປ້ນພິມແບບຄົບຊຸດ</li>
                <li>ການອ່ານອອກສຽງໃນຕົວ</li>
                <li>OCR ສຳລັບເອກະສານທີ່ສະແກນ</li>
                <li>ເຄື່ອງມືແກ້ໄຂທີ່ຄົບຄົວ</li>
            </ul>

            <p>ຮອງຮັບຫຼາຍກວ່າ 50 ພາສາ – ເພື່ອໃຫ້ PDF ສາມາດເຂົ້າເຖິງໄດ້ສຳລັບທຸກຄົນ.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "ຄຸນສົມບັດ",
        'info_features_intro': "PDF Dark View ສະເໜີຄວາມສາມາດດັ່ງຕໍ່ໄປນີ້ໃຫ້ທ່ານ:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>ການສະແດງຜົນ ແລະ ການນຳທາງ</strong> – ໂໝດມືດ/ສະຫວ່າງ, ກັບໜ້າ, ຊູມ, ກະໂດດໄປໜ້າ</li>
            <li><strong>OCR (ການຮັບຮູ້ຂໍ້ຄວາມ)</strong> – ເຮັດໃຫ້ເອກະສານທີ່ສະແກນສາມາດຄົ້ນຫາ ແລະ ຄັດລອກໄດ້</li>
            <li><strong>ການແກ້ໄຂ</strong> – ໃສ່ຂໍ້ຄວາມ, ກາກບອກ, ລາຍເຊັນ, ຮູບພາບ ແລະ ຮູບຮ່າງ</li>
            <li><strong>ການຈັດການໜ້າ</strong> – ລຶບ, ສະກັດ, ໃສ່, ຍ້າຍດ້ວຍການລາກ ແລະ ວາງ</li>
            <li><strong>ການສົ່ງອອກ</strong> – ໄປ Word, Pages ຫຼື ເປັນຂໍ້ຄວາມ</li>
            <li><strong>ຄວາມປອດໄພ</strong> – ການປ້ອງກັນ ແລະ ຈັດການລະຫັດຜ່ານ</li>
            <li><strong>ການເຂົ້າເຖິງ</strong> – ການອ່ານອອກສຽງ, ການຄວບຄຸມແປ້ນພິມ, ຄວາມຄົມຊັດສູງ</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "ການນຳໃຊ້",
        'info_accessibility': "♿ ການເຂົ້າເຖິງ – ການຄວບຄຸມແປ້ນພິມແບບຄົບຊຸດ",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 ທົ່ວໄປ</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> ເປີດ PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> ຄົ້ນຫາ</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> ປ່ຽນໂໝດມືດ/ສະຫວ່າງ</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> ພິມ</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> ອອກ</div>

        <div class="shortcut-cat">📖 ການນຳທາງ</div>
        <div class="shortcut-row"><kbd>ປຸ່ມລູກສອນ</kbd> ກັບໜ້າຕາມລຳດັບ</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> ໄປທີ່ໜ້າ</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> ໜ້າທຳອິດ</div>
        <div class="shortcut-row"><kbd>Ende</kbd> ໜ້າສຸດທ້າຍ</div>

        <div class="shortcut-cat">✏️ ການແກ້ໄຂ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> ໃສ່ຂໍ້ຄວາມ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> ລຶບໜ້າ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> ສະກັດໜ້າ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> ໃສ່ໜ້າ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> ຍ້າຍໜ້າ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> ໝຸນໜ້າ</div>

        <div class="shortcut-cat">🖼️ ການຍ້າຍອົງປະກອບ</div>
        <div class="shortcut-row"><kbd>ປຸ່ມລູກສອນ</kbd> ຍ້າຍຂໍ້ຄວາມ/ຮູບພາບ/ລາຍເຊັນ</div>
        <div class="shortcut-row"><kbd>Ctrl+ປຸ່ມລູກສອນ</kbd> ຂັ້ນຕອນໃຫຍ່ກວ່າ</div>
        <div class="shortcut-row"><kbd>Enter</kbd> ບັນທຶກ</div>
        <div class="shortcut-row"><kbd>ESC</kbd> ຍົກເລີກ</div>

        <div class="shortcut-cat">🗣️ ການອ່ານອອກສຽງ</div>
        <div class="shortcut-row"><kbd>F2</kbd> ເປີດ/ປິດ ການອ່ານອອກສຽງ</div>
        """,
        'info_contextmenu': "📌 ສຳຄັນ: ທຸກຄຸນສົມບັດສາມາດເຂົ້າເຖິງໄດ້ຜ່ານເມນູບໍລິບົດ (ປຸ່ມເມົາສ໌ຂວາ) ເຊັ່ນກັນ!",
        'info_accessibility_hint': "💡 ຄຳແນະນຳ: ການອ່ານອອກສຽງ (F2) ຊ່ວຍໃຫ້ການວາງທິດທາງງ່າຍຂຶ້ນ ແລະ ໃຫ້ຄຳຕິຊົມກ່ຽວກັບເມນູ ແລະ ໜ້າຕ່າງຕ່າງໆ.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "ໃບອະນຸຍາດ & ຂໍ້ມູນຜູ້ເຜີຍແຜ່",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 ຂໍ້ມູນຜູ້ເຜີຍແຜ່</strong><br>
        ຂໍ້ມູນຕາມ § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, ເຢຍລະມັນ<br>
        ອີເມວ: binhdiez64@gmail.com<br>
        ຜູ້ຮັບຜິດຊອບເນື້ອໃນ: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ ການປະຕິເສດຄວາມຮັບຜິດຊອບ</strong><br>
        ຊອບແວນີ້ຖືກພັດທະນາຂຶ້ນດ້ວຍຄວາມລະມັດລະວັງສູງສຸດ. ບໍ່ມີການຮັບປະກັນຄວາມຖືກຕ້ອງ, ຄວາມສົມບູນ ແລະ ການທຳງານ. ການນຳໃຊ້ແມ່ນມີຄວາມສ່ຽງດ້ວຍຕົນເອງ.<br><br>

        <strong>📄 ໃບອະນຸຍາດ MIT (ການນຳໃຊ້ສ່ວນຕົວ)</strong><br>
        ລິຂະສິດ (c) 2026 Toralf Schulz (BinhDiez)<br>
        ອະນຸຍາດ: ການນຳໃຊ້ຟຣີ, ການດັດແກ້ສ່ວນຕົວ, ສຳເນົາສ່ວນຕົວ.<br>
        ບໍ່ອະນຸຍາດ: ການຂາຍ, ການນຳໃຊ້ທາງການຄ້າ, ການເອົາຂໍ້ຄວາມລິຂະສິດອອກ.<br><br>

        <strong>🔧 ອົງປະກອບພາກສ່ວນທີສາມ</strong><br>
        ຊອບແວນີ້ມີອົງປະກອບພາຍໃຕ້ໃບອະນຸຍາດ GPL, AGPL, Apache 2.0, BSD ແລະ MIT.<br>
        ເມື່ອແຈກຢາຍຕໍ່, ຕ້ອງປະຕິບັດຕາມເງື່ອນໄຂໃບອະນຸຍາດທີ່ກ່ຽວຂ້ອງ.<br><br>

        <strong>🌐 ແຫຼ່ງເປີດ</strong><br>
        ລະຫັດແຫຼ່ງຂໍ້ມູນສາມາດເຂົ້າເຖິງໄດ້ ແລະ ສາມາດເບິ່ງ, ດັດແກ້ ແລະ ແຈກຢາຍຕໍ່ໄດ້ຕາມເງື່ອນໄຂໃບອະນຸຍາດທີ່ກ່ຽວຂ້ອງ.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "ຄຳຂອບໃຈ",
        'info_credits': "ຂອບໃຈຊຸມຊົນແຫຼ່ງເປີດ",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – ການປະມວນຜົນ PDF</li>
            <li><strong>PyQt5</strong> – ໜ້າຕາກຣາຟິກ</li>
            <li><strong>Tesseract OCR</strong> – ການຮັບຮູ້ຂໍ້ຄວາມ</li>
            <li><strong>OCRmyPDF</strong> – ການເຊື່ອມໂຍງ OCR</li>
            <li><strong>python-docx</strong> – ການສົ່ງອອກ Word</li>
            <li><strong>qtawesome</strong> – ໄອຄອນ</li>
            <li><strong>DeepSeek</strong> – ການສະໜັບສະໜູນການແປພາສາ (50+ ພາສາ)</li>
            <li><strong>ຜູ້ໃຊ້ທຸກທ່ານ</strong> – ສຳລັບຄຳຕິຊົມອັນລ້ຳຄ່າ</li>
            <li><strong>ຊຸມຊົນແຫຼ່ງເປີດ</strong> – ສຳລັບໂປຣແກຣມຊ່ວຍເຫຼືອທີ່ດີເລີດ</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "ພາສາ",
        'info_languages_header': "🌍 ການຮອງຮັບພາສາ",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View ປະຈຸບັນຮອງຮັບ <strong>62 ພາສາ</strong> – ເພື່ອໃຫ້ຊອບແວສາມາດນຳໃຊ້ໄດ້ຢ່າງທົ່ວເຖິງໃນທົ່ວໂລກ.</p>

            <p><strong>📖 ລາຍຊື່ພາສາຄົບຖ້ວນ (ເຖິງເດືອນມີນາ 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 ອາຟຣິການ</li>
                    <li>🇦🇱 ອານບານີ (Shqip)</li>
                    <li>🇩🇿 ອາຣັບ (العربية)</li>
                    <li>🇮🇩 ບາລີ (Basa Bali)</li>
                    <li>🇧🇩 ເບັງກາລີ (বাংলা)</li>
                    <li>🇲🇲 ພະມ້າ (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 ບອສເນຍ (Bosanski)</li>
                    <li>🇧🇬 ບຸນກາລີ (Български)</li>
                    <li>🇨🇳 ຈີນ (中文)</li>
                    <li>🇩🇰 ດານິຊ (Dansk)</li>
                    <li>🇩🇪 ເຢຍລະມັນ (Deutsch)</li>
                    <li>🇬🇧 ອັງກິດ (English)</li>
                    <li>🇪🇪 ເອສໂຕເນຍ (Eesti)</li>
                    <li>🇫🇮 ແຟງລັງ (Suomi)</li>
                    <li>🇫🇷 ຝຣັ່ງ (Français)</li>
                    <li>🇬🇷 ເກຣັກ (Ελληνικά)</li>
                    <li>🇮🇱 ຮິບຣູ (עברית)</li>
                    <li>🇮🇳 ຮິນດີ (हिन्दी)</li>
                    <li>🇭🇷 ໂຄຣເອເຊຍ (Hrvatski)</li>
                    <li>🇭🇺 ຮັງກາລີ (Magyar)</li>
                    <li>🇮🇩 ອິນໂດເນເຊຍ (Bahasa Indonesia)</li>
                    <li>🇮🇪 ໄອຣິຊ (Gaeilge)</li>
                    <li>🇮🇸 ໄອສແລນ (Íslenska)</li>
                    <li>🇮🇹 ອິຕາລີ (Italiano)</li>
                    <li>🇯🇵 ຍີ່ປຸ່ນ (日本語)</li>
                    <li>🇰🇭 ຂະເໝນ (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 ເກົາຫຼີ (한국어)</li>
                    <li>🇱🇦 ລາວ (ພາສາລາວ)</li>
                    <li>🇱🇻 ລັດເວຍ (Latviešu)</li>
                    <li>🇱🇹 ລິທົວເນຍ (Lietuvių)</li>
                    <li>🇱🇺 ລຸກຊຳບວກ (Lëtzebuergesch)</li>
                    <li>🇲🇾 ມາເລ (Bahasa Melayu)</li>
                    <li>🇮🇳 ມາຣາທີ (मराठी)</li>
                    <li>🇲🇳 ມົງໂກລີ (Монгол)</li>
                    <li>🇳🇵 ເນປານ (नेपाली)</li>
                    <li>🇳🇱 ໂຮນລັງ (Nederlands)</li>
                    <li>🇳🇴 ນອກເວ (Norsk)</li>
                    <li>🇦🇫 ປາສຕູ (پښتو)</li>
                    <li>🇮🇷 ເປີເຊຍ (فارسی)</li>
                    <li>🇵🇱 ໂປໂລຍ (Polski)</li>
                    <li>🇵🇹 ປອກຕຸຍການ (Português)</li>
                    <li>🇮🇳 ປັນຈາບ (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 ລູມານີ (Română)</li>
                    <li>🇷🇺 ລັດເຊຍ (Русский)</li>
                    <li>🇸🇪 ສະວີເດນ (Svenska)</li>
                    <li>🇷🇸 ເຊີເບຍ (Српски)</li>
                    <li>🇸🇰 ສະໂລວາກີ (Slovenčina)</li>
                    <li>🇸🇮 ສະໂລເວເນຍ (Slovenščina)</li>
                    <li>🇪🇸 ສະເປນ (Español)</li>
                    <li>🇹🇿 ສະວາຮິລີ (Kiswahili)</li>
                    <li>🇵🇭 ຕາກາລັອກ (Filipino)</li>
                    <li>🇮🇳 ທາມິນ (தமிழ்)</li>
                    <li>🇮🇳 ເຕລູກູ (తెలుగు)</li>
                    <li>🇹🇭 ໄທ (ไทย)</li>
                    <li>🇨🇿 ເຊັກ (Čeština)</li>
                    <li>🇹🇷 ຕວກກີ (Türkçe)</li>
                    <li>🇺🇦 ອູແກຣນ (Українська)</li>
                    <li>🇵🇰 ອູດູ (اردو)</li>
                    <li>🇻🇳 ຫວຽດນາມ (Tiếng Việt)</li>
                    <li>🇸🇳 ໂວລົບ (Wolof)</li>
                    <li>🇺🇸 ຢິດດິຊ (ייִדיש)</li>
                    <li>🇿🇦 ຊູລູ (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 ເພີ່ມພາສາຂອງທ່ານເອງ:</strong><br>
                ຕ້ອງການພາສາທີ່ຍັງບໍ່ທັນມີບໍ? ພຽງແຕ່ວາງໄຟລ໌ວັດຈະນານຸກົມຂອງທ່ານເອງ (<code>sprache_xx.py</code>) ໄວ້ຂ້າງແອັບພລິເຄຊັນ – ຊອບແວຈະຮັບຮູ້ໂດຍອັດຕະໂນມັດ. ຖ້າທ່ານສົນໃຈການແປພາສາສະເພາະ, ກະລຸນາຕິດຕໍ່ຫາຂ້າພະເຈົ້າ.
            </div>

            <p><strong>🙏 ຄຳຂອບໃຈພິເສດ:</strong> DeepSeek ສຳລັບການສະໜັບສະໜູນໃນການແປວັດຈະນານຸກົມທັງໝົດເປັນ 62 ພາສາ.</p>

            <p>📧 ຕິດຕໍ່ສຳລັບການແປພາສາ: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "ຂໍ້ຜິດພາດ",
        'error_occurred': "ເກີດຂໍ້ຜິດພາດ",
        'error_pdf_load': "ຂໍ້ຜິດພາດໃນການໂຫຼດ PDF",
        'error_pdf_save': "ຂໍ້ຜິດພາດໃນການບັນທຶກ PDF",
        'error_ocr': "ຂໍ້ຜິດພາດໃນການຮັບຮູ້ຂໍ້ຄວາມ",
        'error_no_pdf': "ບໍ່ມີ PDF ຖືກໂຫຼດ",
        'error_page_not_found': "ບໍ່ພົບໜ້າ",
        'error_invalid_range': "ຊ່ວງໜ້າບໍ່ຖືກຕ້ອງ",
        'error_file_not_found': "ບໍ່ພົບໄຟລ໌",
        'error_permission': "ບໍ່ມີສິດ",
        'error_unknown': "ຂໍ້ຜິດພາດບໍ່ທາບສາເຫດ",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "ສຳເລັດ",
        'success_operation': "ດຳເນີນການສຳເລັດ",
        'success_saved': "ບັນທຶກສຳເລັດ",
        'success_exported': "ສົ່ງອອກສຳເລັດ",
        'success_imported': "ນຳເຂົ້າສຳເລັດ",
        'success_deleted': "ລຶບສຳເລັດ",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "ຢືນຢັນ",
        'confirm_yes': "ແມ່ນ",
        'confirm_no': "ບໍ່",
        'confirm_ok': "ຕົກລົງ",
        'confirm_cancel': "ຍົກເລີກ",
        'confirm_delete': "ລຶບ",
        'confirm_overwrite': "ຂຽນທັບ",
        'confirm_continue': "ດຳເນີນການຕໍ່",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "ກຳລັງໂຫຼດ PDF...",
        'progress_saving': "ກຳລັງບັນທຶກ PDF...",
        'progress_exporting': "ກຳລັງສົ່ງອອກ PDF...",
        'progress_processing': "ກຳລັງປະມວນຜົນ...",
        'progress_wait': "ກະລຸນາລໍຖ້າ...",
        'progress_preparing': "ກຳລັງກະກຽມ...",
        'progress_finalizing': "ກຳລັງສຳເລັດ...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "ຂາວ",
        'color_black': "ດຳ",
        'color_red': "ແດງ",
        'color_green': "ຂຽວ",
        'color_blue': "ນ້ຳເງິນ",
        'color_yellow': "ເຫຼືອງ",
        'color_magenta': "ບົວແດງ",
        'color_cyan': "ຟ້າ",
        'color_orange': "ສົ້ມ",
        'color_gray': "ເທົາ",
        'color_custom': "ເລືອກສີ",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&ໄຟລ໌",
        'menu_edit': "&ແກ້ໄຂ",
        'menu_view': "&ມຸມມອງ",
        'menu_tools': "&ເຄື່ອງມື",
        'menu_settings': "&ການຕັ້ງຄ່າ",
        'menu_help': "&ຊ່ວຍເຫຼືອ",
        'menu_language': "🌐 ພາສາ",
        'menu_guides': "&ຄຳແນະນຳ",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&ເປີດ",
        'file_save_as': "&ບັນທຶກເປັນ...",
        'file_protect': "&ປ້ອງກັນເອກະສານ...",
        'file_export': "&ສົ່ງອອກ",
        'file_export_pages': "ສົ່ງອອກເປັນ Pages",
        'file_export_word': "ສົ່ງອອກເປັນ DOCX",
        'file_export_text': "ສົ່ງອອກເປັນ TXT",
        'file_print_now': "&ພິມດຽວນີ້",
        'file_print': "&ພິມ",
        'file_close': "&ປິດ",
        'file_quit': "&ອອກ",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&ຄົ້ນຫາ",
        'edit_ocr': " ເຮັດ OCR",
        'edit_rotate': "&ໝຸນໜ້າ",
        'edit_rotate_all': "&ໝຸນທຸກໜ້າ",
        'edit_delete_pages': "&ລຶບໜ້າ",
        'edit_extract_pages': "&ສະກັດໜ້າ",
        'edit_insert_pages': "&ແຊກໜ້າ",
        'edit_move_pages': "&ຍ້າຍໜ້າ",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " ແຊກຂໍ້ຄວາມ ແລະ ກາກບອກ",
        'text_insert': " ແຊກຂໍ້ຄວາມ",
        'cross_insert': " ແຊກກາກບອກ",
        'text_customize': " ປັບແຕ່ງຂໍ້ຄວາມນີ້",
        'cross_customize': " ປັບແຕ່ງກາກບອກນີ້",
        'cross_customize_all': " ປັບແຕ່ງກາກບອກທັງໝົດ",
        'text_discard': " ຖິ້ມຂໍ້ຄວາມ/ກາກບອກນີ້",
        'text_discard_all': " ຖິ້ມຂໍ້ຄວາມ ແລະ ກາກບອກທັງໝົດ",
        'text_save_all': " ບັນທຶກຂໍ້ຄວາມ ແລະ ກາກບອກທັງໝົດ",
        'text_guide': " ການປ້ອນຂໍ້ຄວາມ / ບລັອກຂໍ້ຄວາມ - ຄຳແນະນຳ",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " ແຊກລາຍເຊັນ",
        'signature_settings_menu': " ການຕັ້ງຄ່າ...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " ແຊກຮູບພາບ",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " ແຊກຮູບຮ່າງ",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&ສະແດງໜ້າຕ່າງຂໍ້ຄວາມ",
        'view_zoom': "&ຊູມ",
        'view_zoom_page': "&ຄວາມກວ້າງໜ້າ (ຄ່າເລີ່ມຕົ້ນ)",
        'view_zoom_two': "&ສອງໜ້າ",
        'view_zoom_overview': "&ພາບລວມ (ຫຼາຍໜ້າ)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&ເຄື່ອງມືຊ່ວຍເຫຼືອ",
        'settings_voice': "ສຽງເວົ້າ",
        'settings_voice_tooltip': "ເພີ່ມສຽງເວົ້າຂອງໂປຣແກຣມອ່ານໜ້າຈໍດ້ວຍຂໍ້ມູນເພີ່ມເຕີມ",
        'settings_signature': "&ການຕັ້ງຄ່າລາຍເຊັນ",
        'settings_password': "&ການຈັດການລະຫັດຜ່ານ",
        'settings_backup': "ສ້າງສຳຮອງກ່ອນການປ່ຽນແປງ",
        'settings_export_import': "&ສົ່ງອອກ / ນຳເຂົ້າການຕັ້ງຄ່າ",
        'settings_export': "&ສົ່ງອອກການຕັ້ງຄ່າທັງໝົດ...",
        'settings_import': "&ນຳເຂົ້າການຕັ້ງຄ່າທັງໝົດ...",
        'settings_export_info': "&ສົ່ງອອກຫຍັງ?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "ເປີດ",
        'voice_off': "ປິດ",
        'voice_toggle': "ສຽງເວົ້າ {0}",
        'voice_speed': "ຄວາມໄວ {0} ເປີເຊັນ",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "ບໍ່ພົບເຄື່ອງມື:\n{0}\n\nBASE_DIR: {1}\nກະລຸນາກວດສອບໃຫ້ແນ່ໃຈວ່າຕິດຕັ້ງເຄື່ອງມື PDF ໃນໄດເລກະທໍລີ {1}",
        'tool_started': "ເລີ່ມ {0} ແລ້ວ",
        'tool_start_failed': "ບໍ່ສາມາດເລີ່ມໄດ້",
        'process_error_failed_to_start': "ບໍ່ສາມາດເລີ່ມຂະບວນການໄດ້. ໄຟລ໌ມີຢູ່ບໍ?",
        'process_error_crashed': "ຂະບວນການຢຸດເຮັດວຽກໃນລະຫວ່າງເລີ່ມຕົ້ນ",
        'process_error_timeout': "ຂະບວນການໝົດເວລາ",
        'process_error_write': "ຂໍ້ຜິດພາດໃນການຂຽນໄປຍັງຂະບວນການ",
        'process_error_read': "ຂໍ້ຜິດພາດໃນການອ່ານຈາກຂະບວນການ",
        'process_error_unknown': "ຂໍ້ຜິດພາດຂະບວນການບໍ່ທາບສາເຫດ",
        'process_command': "ຄຳສັ່ງ",
        'process_normal_exit': "ສິ້ນສຸດຕາມປົກກະຕິ",
        'process_crashed': "ຢຸດເຮັດວຽກ",
        'process_nonzero_exit': "{0} ສິ້ນສຸດດ້ວຍລະຫັດຂໍ້ຜິດພາດ {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "ກຳລັງຍົກເລີກ...",
        'move_cancelling': "ກຳລັງຍົກເລີກການຍ້າຍ",
        'opening_pdf': "ກຳລັງເປີດ PDF...",
        'loading_document': "ກຳລັງໂຫຼດເອກະສານ...",
        'pdf_opened': "ເປີດ PDF ແລ້ວ",
        'pages_found_moving': "ພົບ {0} ໜ້າ, {1} ສຳລັບການຍ້າຍ",
        'creating_backup': "ກຳລັງສ້າງສຳຮອງ...",
        'backup_description': "ກຳລັງສຳຮອງໄຟລ໌ຕົ້ນສະບັບ...",
        'backup_saved_as': "ສຳຮອງເປັນ: {0}",
        'error_format': "ຂໍ້ຜິດພາດ: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView ໂດຍ BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "ຣີເຊັດການຄົ້ນຫາ",
        'page_header_simple': "=== ໜ້າ {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "ການຈັດການລະຫັດຜ່ານ – ຄຳແນະນຳ",
        'password_guide_voice': "ຄຳແນະນຳສຳລັບການຈັດການລະຫັດຜ່ານ. ກະລຸນາອ່ານໝາຍເຫດ",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 ການຈັດການລະຫັດຜ່ານ – ຄຳແນະນຳລະອຽດ</strong></p>

        <p><strong>1. ການປ້ອງກັນດ້ວຍລະຫັດຜ່ານສຳລັບ PDF</strong></p>
        <ul>
        <li>ເມື່ອເປີດ PDF ທີ່ມີການປ້ອງກັນດ້ວຍລະຫັດຜ່ານ, ຈະມີການສົນທະນາໃຫ້ປ້ອນລະຫັດຜ່ານ.</li>
        <li>ທ່ານສາມາດບັນທຶກລະຫັດຜ່ານແບບເຂົ້າລະຫັດເພື່ອບໍ່ຕ້ອງປ້ອນທຸກຄັ້ງ (ກ່ອງ "ບັນທຶກລະຫັດຜ່ານ").</li>
        <li>ດ້ວຍປຸ່ມ "ລຶບລະຫັດຜ່ານ" ທ່ານສາມາດສ້າງສຳເນົາ PDF ທີ່ຖອດລະຫັດແລ້ວ ແລະ ລຶບລະຫັດຜ່ານອອກຈາກຖານຂໍ້ມູນ.</li>
        </ul>

        <p><strong>2. ລະຫັດຜ່ານຫຼັກ</strong></p>
        <ul>
        <li>ລະຫັດຜ່ານຫຼັກປ້ອງກັນການເຂົ້າເຖິງລະຫັດຜ່ານ PDF ທີ່ບັນທຶກໄວ້ທັງໝົດ.</li>
        <li><strong>ການຕັ້ງຄ່າ:</strong> ໄປທີ່ "ການຕັ້ງຄ່າ → ການຈັດການລະຫັດຜ່ານ → ການຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ" ແລະ ຄລິກ "ຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ". ເລືອກລະຫັດຜ່ານທີ່ແຂງແຮງ (ຢ່າງໜ້ອຍ 8 ຕົວອັກສອນ).</li>
        <li><strong>ການປ່ຽນ:</strong> ຫຼັງຢືນຢັນຕົວຕົນສຳເລັດ, ທ່ານສາມາດປ່ຽນລະຫັດຜ່ານຫຼັກໄດ້.</li>
        <li><strong>ການລຶບ:</strong> ຖ້າທ່ານລຶບລະຫັດຜ່ານຫຼັກ, ລະຫັດຜ່ານທີ່ບັນທຶກໄວ້ທັງໝົດຈະຖືກລຶບຢ່າງຖາວອນ. ທ່ານສາມາດສົ່ງອອກສຳຮອງກ່ອນໄດ້.</li>
        <li>ໜຶ່ງຄັ້ງຕໍ່ເຊດຊັນ, ທ່ານຕ້ອງຢືນຢັນຕົວຕົນດ້ວຍລະຫັດຜ່ານຫຼັກເພື່ອເຂົ້າເຖິງຟັງຊັນທີ່ປ້ອງກັນ (ເຊັ່ນ ການສະແດງລະຫັດຜ່ານ).</li>
        </ul>

        <p><strong>3. ການຈັດການລະຫັດຜ່ານ (ລາຍການ)</strong></p>
        <ul>
        <li>ພາຍໃຕ້ "ການຕັ້ງຄ່າ → ການຈັດການລະຫັດຜ່ານ" ທ່ານຈະເປີດຕາຕະລາງຂອງ PDF ທີ່ບັນທຶກໄວ້ທັງໝົດພ້ອມລະຫັດຜ່ານທີ່ເຂົ້າລະຫັດ.</li>
        <li><strong>ບໍ່ມີລະຫັດຜ່ານຫຼັກ:</strong> ທ່ານສາມາດລຶບລາຍການໄດ້ເທົ່ານັ້ນ – ລະຫັດຜ່ານຍັງຄົງຖືກເຊື່ອງໄວ້.</li>
        <li><strong>ມີລະຫັດຜ່ານຫຼັກ (ຢືນຢັນຕົວຕົນແລ້ວ):</strong> ທ່ານສາມາດເບິ່ງ, ສຳເນົາ, ສົ່ງອອກ ແລະ ລຶບລະຫັດຜ່ານໄດ້.</li>
        <li><strong>ສົ່ງອອກ:</strong> ເລືອກຮູບແບບ (JSON, CSV, TXT) ແລະ ບັນທຶກລາຍການ. ຖ້າຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກ, ທ່ານສາມາດຕັດສິນໃຈໄດ້ວ່າລະຫັດຜ່ານຈະຖືກສົ່ງອອກເປັນຂໍ້ຄວາມທຳມະດາ ຫຼື ເຂົ້າລະຫັດຕໍ່ໄປ.</li>
        <li><strong>ນຳເຂົ້າ:</strong> ໄຟລ໌ ZIP ທີ່ສົ່ງອອກກ່ອນໜ້ານີ້ພ້ອມການຕັ້ງຄ່າທັງໝົດ (ລວມລະຫັດຜ່ານ) ສາມາດອ່ານກັບຄືນໄດ້ຜ່ານ "ການຕັ້ງຄ່າ → ສົ່ງອອກ/ນຳເຂົ້າການຕັ້ງຄ່າ". ຂໍ້ຄວນລະວັງ: ຂໍ້ມູນທີ່ມີຢູ່ຈະຖືກຂຽນທັບ!</li>
        </ul>

        <p><strong>4. ເຄື່ອງສ້າງລະຫັດຜ່ານ</strong></p>
        <ul>
        <li>ໃນການສົນທະນາລະຫັດຜ່ານ (ເຊັ່ນ ເມື່ອປ້ອງກັນ PDF), ທ່ານຈະພົບປຸ່ມລູກເຕົ໋າ 🎲 ທາງດ້ານຂວາຂອງຊ່ອງປ້ອນຂໍ້ມູນ.</li>
        <li>ຄລິກເພື່ອເປີດເຄື່ອງສ້າງລະຫັດຜ່ານ. ທ່ານສາມາດຕັ້ງຄ່າຄວາມຍາວ, ຊຸດອັກຂະຫະ (ຕົວພິມໃຫຍ່, ຕົວພິມນ້ອຍ, ຕົວເລກ, ສັນຍາລັກພິເສດ) ແລະ ຕົວຄັ້ນເພື່ອໃຫ້ອ່ານງ່າຍຂຶ້ນ.</li>
        <li>ລະຫັດຜ່ານທີ່ສ້າງຂຶ້ນສາມາດນຳໃຊ້ໄດ້ທັນທີ ແລະ ສຳເນົາໄດ້ຖ້າຈຳເປັນ.</li>
        </ul>

        <p><strong>5. ໝາຍເຫດດ້ານຄວາມປອດໄພທີ່ສຳຄັນ</strong></p>
        <ul>
        <li>ລະຫັດຜ່ານທີ່ບັນທຶກໄວ້ຈະຖືກເກັບຮັກສາດ້ວຍການເຂົ້າລະຫັດ AES-256. ກະແຈໄດ້ມາຈາກລະຫັດຜ່ານຫຼັກຂອງທ່ານ (ຖ້າຕັ້ງຄ່າ) ຫຼື ຈາກຄ່າຄົງທີ່ (ບໍ່ມີລະຫັດຜ່ານຫຼັກ).</li>
        <li>ຖ້າບໍ່ມີລະຫັດຜ່ານຫຼັກ, ລະຫັດຜ່ານຈະຖືກເຂົ້າລະຫັດແຕ່ກະແຈຖືກເກັບໄວ້ໃນໂປຣແກຣມ – ຜູ້ໂຈມຕີທີ່ເຂົ້າເຖິງໄຟລ໌ຂອງທ່ານສາມາດຖອດລະຫັດໄດ້. ດັ່ງນັ້ນ, ພວກເຮົາແນະນຳຢ່າງຍິ່ງໃຫ້ໃຊ້ລະຫັດຜ່ານຫຼັກ.</li>
        <li>ຖານຂໍ້ມູນລະຫັດຜ່ານຢູ່ໃນໄດເລກະທໍລີ `Daten/passwords.json`. ເຮັດການສຳຮອງຂໍ້ມູນເປັນປະຈຳ, ໂດຍສະເພາະກ່ອນລຶບລະຫັດຜ່ານຫຼັກ.</li>
        <li>ຖ້າລືມລະຫັດຜ່ານຫຼັກ, ລະຫັດຜ່ານທີ່ບັນທຶກໄວ້ທັງໝົດຈະສູນເສຍຢ່າງຖາວອນ.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "ໂໝດການກັບສີ",
        'invert_mode_classic': "ແບບຄລາສສິກ (ກັບສີທັງໝົດ)",
        'invert_mode_smart': "ອັດສະລິຍະ (ກັບສະເພາະຄວາມສະຫວ່າງ)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "ຄ່າເກນລະດັບສີເທົາ",
        'gray_threshold_10': "10% (ເຄັ່ງຄັດ)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (ມາດຕະຖານ)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (ອ່ອນ)",
        'threshold_changed': "ຕັ້ງຄ່າເກນເປັນ {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "ຄ່າເກນລະດັບສີເທົາ – ຄຳອະທິບາຍ",
        'threshold_guide_text': "ຄ່າເກນລະດັບສີເທົາກຳນົດວ່າພິກເຊລໃດໃນໂໝດມືດອັດສະລິຍະຖືກຖືວ່າເປັນ 'ສີເທົາ' ແລະ ຖືກກັບສີ.\n\n"
                                "• ຄ່າຕໍ່າ (10%) ກັບສະເພາະສີເທົາທີ່ເກືອບສົມບູນ – ອົງປະກອບສີຍັງຄົງຖືກຮັກສາໄວ້ຢ່າງຄົບຖ້ວນ.\n"
                                "• ຄ່າສູງ (50%) ກັບສີພິກເຊລທີ່ມີສີເລັກນ້ອຍນຳ – ສິ່ງນີ້ເພີ່ມຄວາມຄົມຊັດ, ແຕ່ອາດຈະເຮັດໃຫ້ສີຜິດປົກກະຕິ.\n\n"
                                "ຄ່າທີ່ດີທີ່ສຸດຂຶ້ນກັບເອກະສານ. ສຳລັບເອກະສານຂໍ້ຄວາມລ້ວນ, 30–40% ມັກຈະເໝາະສົມ, ສຳລັບກຣາຟິກສີ ຄວນໃຊ້ 10–20%.\n\n"
                                "ທ່ານສາມາດປັບຄ່າໄດ້ທຸກເວລາຜ່ານເມນູ 'ການຕັ້ງຄ່າ' – PDF ຈະຖືກໂຫຼດຄືນທັນທີ.\n\n"
                                "ໝາຍເຫດ:\n* ຮູບຖ່າຍ ແລະ ຮູບພາບສາມາດສະແດງໄດ້ຖືກຕ້ອງພຽງແຕ່ໃນໂໝດສະຫວ່າງເທົ່ານັ້ນ!\n* ການຕັ້ງຄ່າການກັບສີຈະສະແດງພຽງແຕ່ເມື່ອໂໝດມືດຖືກເປີດໃຊ້ງານ.",
        'threshold_guide_voice': "ຄ່າເກນລະດັບສີເທົາກຳນົດວ່າໂໝດມືດອັດສະລິຍະເຂົ້າແຊກແຊງຫຼາຍສ່ຳໃດ. ຄ່າຕໍ່າຊ່ວຍຮັກສາສີ, ຄ່າສູງເພີ່ມຄວາມຄົມຊັດ.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "ກຳລັງເປີດ PDF...",
        'progress_loading_document': "ກຳລັງໂຫຼດເອກະສານ...",
        'progress_pdf_opened': "ເປີດ PDF ແລ້ວ",
        'progress_creating_backup': "ກຳລັງສ້າງສຳຮອງ...",
        'progress_backup_description': "ກຳລັງຮັກສາໄຟລ໌ຕົ້ນສະບັບ...",
        'progress_backup_created': "ສ້າງສຳຮອງແລ້ວ",
        'progress_backup_saved_as': "ບັນທຶກເປັນ: {0}",
        'progress_analyzing_start': "ກຳລັງເລີ່ມວິເຄາະ...",
        'progress_searching_empty': "ກຳລັງຊອກຫາໜ້າຫວ່າງ...",
        'progress_page_empty': "ໜ້າ {0} ຫວ່າງ",
        'progress_page_keep': "ເກັບໜ້າ {0} ໄວ້",
        'progress_analysis_complete': "ວິເຄາະສຳເລັດແລ້ວ",
        'progress_empty_found': "ພົບ {0} ໜ້າຫວ່າງ",
        'progress_current_page': "ໜ້າປັດຈຸບັນ",
        'progress_mark_delete': "ກຳລັງໝາຍເພື່ອລຶບ",
        'progress_range_selected': "ຂອບເຂດໜ້າ {0}-{1}",
        'progress_deleting_pages': "ກຳລັງລຶບ {0} ໜ້າ",
        'progress_creating_new_pdf': "ກຳລັງສ້າງ PDF ໃໝ່...",
        'progress_transferring_pages': "ກຳລັງໂອນໜ້າ",
        'progress_keeping_page': "ຈະເກັບໜ້າ {0} ໄວ້ ({1}/{2})",
        'progress_saving_pdf': "ກຳລັງບັນທຶກ PDF...",
        'progress_optimizing': "ກຳລັງເພີ່ມປະສິດທິພາບຂະໜາດໄຟລ໌...",
        'progress_finalizing': "ກຳລັງສຳເລັດຂັ້ນສຸດທ້າຍ...",
        'progress_new_size': "ຂະໜາດໃໝ່: {0:.2f} MB",
        'progress_cancelling': "ກຳລັງຍົກເລີກ...",
        'progress_cancel_message': "ກຳລັງຍົກເລີກ {0}",
        'progress_pages_found_moving': "ພົບ {0} ໜ້າ, {1} ສຳລັບຍ້າຍ",

        # OCR-Fortschritt
        'ocr_status_analyzing': "ກຳລັງວິເຄາະ PDF...",
        'ocr_status_optimizing': "ກຳລັງເພີ່ມປະສິດທິພາບຮູບພາບ...",
        'ocr_status_recognizing': "ກຳລັງຮັບຮູ້ຂໍ້ຄວາມ...",
        'ocr_status_embedding': "ກຳລັງຝັງຂໍ້ຄວາມ...",
        'ocr_status_finalizing': "ກຳລັງສຳເລັດ PDF...",

        # PDF-Laden
        'progress_preparing': "ກຳລັງກະກຽມ...",
        'progress_loading': "ກຳລັງໂຫຼດ PDF...",

        # Seitenoperationen
        'progress_deleting_title': "ກຳລັງລຶບໜ້າ...",
        'progress_moving_title': "ກຳລັງຍ້າຍໜ້າ...",
        'pages_found': "ພົບໜ້າ",
        'progress_creating_new_order': "ກຳລັງສ້າງລຳດັບໃໝ່...",
        'progress_sorting_pages': "ກຳລັງຈັດລຽງໜ້າ...",
        'progress_moving_to_begin': "ຍ້າຍ {0} ໜ້າໄປທີ່ຕົ້ນ",
        'progress_transferring_count': "ໂອນ {0} ໜ້າ",
        'progress_transferring_before_target': "ໂອນໜ້າກ່ອນເປົ້າໝາຍ",
        'progress_moving_pages': "ຍ້າຍ {0} ໜ້າ",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_ສຳຮອງ_",
        'filename_protected_suffix': "_ປ້ອງກັນ_",
        'filename_copy_suffix': "_ສຳເນົາ",
        'filename_page_single': "_ໜ້າ_",
        'filename_page_range': "_ໜ້າ_",
        'filename_export_page': "_ໜ້າ_{0:03}",
        'filename_export_range': "_ໜ້າ_{0}-{1}",
        'filename_export_multiple': "_ໜ້າ_{0}",
        'filename_with_text': "_ພ້ອມ_ຂໍ້ຄວາມ",
        'filename_with_signature': "_ພ້ອມ_ລາຍເຊັນ",
        'filename_with_image': "_ພ້ອມ_ຮູບພາບ",
        'filename_with_forms': "_ພ້ອມ_ຮູບຮ່າງ",
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
        'view_toggle_navbar': "ສະແດງແຖບປຸ່ມ",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "ບໍ່ສາມາດລຶບໜ້າທັງໝົດໄດ້",
		'pages_cannot_delete_last_page': 'ບໍ່ສາມາດລຶບໜ້າສຸດທ້າຍໄດ້!',
		'pages_cannot_delete_all_pages': 'ຕ້ອງມີຢ່າງໜ້ອຍໜຶ່ງໜ້າຢູ່ໃນເອກະສານ!',
		'delete_pages_confirm': 'ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບ {0} ໜ້າ?',
		'delete_pages_confirm_voice': 'ທ່ານແນ່ໃຈບໍ່ວ່າຕ້ອງການລຶບ {0} ໜ້າ?',
		'pages_deleted': 'ລຶບ {0} ໜ້າແລ້ວສຳເລັດ.',
		'warning': 'ຄຳເຕືອນ',
		'error': 'ຂໍ້ຜິດພາດ',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "ບໍ່ມີແບບຟອມຖືກເລືອກ",
        'form_customized': "ປັບແບບຟອມສຳເລັດແລ້ວ",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "ເລືອກ",
        'btn_use': "ໃຊ້",
        'master_password_for_spasswords': "ເພື່ອເກັບຮັກສາ ແລະ ໃຊ້ລະຫັດຜ່ານ, ທ່ານຕ້ອງຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກກ່ອນ.\n\nທ່ານຕ້ອງການຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກຕອນນີ້ບໍ?",
        'open_saved_dialog_title': "ເປີດໄຟລ໌ທີ່ບັນທຶກໄວ້",
        'open_saved_question': "ທ່ານຕ້ອງການເປີດໄຟລ໌ທີ່ບັນທຶກໄວ້ຕອນນີ້ບໍ?",
        'password': "ລະຫັດຜ່ານ",
        'password_manager_master_required': "ຕົວຈັດການລະຫັດຜ່ານສາມາດໃຊ້ໄດ້ສະເພາະເມື່ອຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກແລ້ວເທົ່ານັ້ນ.\n\nທ່ານຕ້ອງການຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກຕອນນີ້ບໍ?",
        'password_master_required_for_select': "ເພື່ອເບິ່ງ ແລະ ເລືອກລະຫັດຜ່ານທີ່ບັນທຶກໄວ້, ທ່ານຕ້ອງຢືນຢັນຕົວຕົນດ້ວຍລະຫັດຜ່ານຫຼັກຂອງທ່ານກ່ອນ.\n\nທ່ານຕ້ອງການຢືນຢັນຕົວຕົນຕອນນີ້ບໍ?",
        'password_not_available': "ລະຫັດຜ່ານທີ່ເລືອກບໍ່ມີ ຫຼື ບໍ່ສາມາດຖອດລະຫັດໄດ້.",
        'password_options_title': "ຕົວເລືອກລະຫັດຜ່ານ",
        'password_save_choice_change': "ຕັ້ງຄ່າລະຫັດຜ່ານໃໝ່",
        'password_save_choice_keep': "ໃຊ້ລະຫັດຜ່ານທີ່ມີຢູ່",
        'password_save_choice_none': "ບັນທຶກໂດຍບໍ່ເຂົ້າລະຫັດ",
        'password_save_hint': "ຕັ້ງຄ່າລະຫັດຜ່ານຫຼັກກ່ອນ ເພື່ອເກັບຮັກສາລະຫັດຜ່ານຢ່າງປອດໄພ.",
        'password_save_master_required': "ບັນທຶກລະຫັດຜ່ານ (ສາມາດເຮັດໄດ້ດ້ວຍລະຫັດຜ່ານຫຼັກເທົ່ານັ້ນ)",
        'password_save_question': "PDF ປັດຈຸບັນຖືກປ້ອງກັນດ້ວຍລະຫັດຜ່ານ. ທ່ານຕ້ອງການໃຊ້ລະຫັດຜ່ານທີ່ມີຢູ່, ຕັ້ງຄ່າອັນໃໝ່ ຫຼື ບັນທຶກໂດຍບໍ່ເຂົ້າລະຫັດ?",
        'password_select': "ເລືອກລະຫັດຜ່ານ",
        'password_select_none': "ບໍ່ໄດ້ເລືອກລະຫັດຜ່ານ.\n\nກະລຸນາເລືອກລະຫັດຜ່ານຈາກລາຍຊື່.",
        'password_select_one': "ກະລຸນາເລືອກລະຫັດຜ່ານພຽງອັນດຽວ.\n\nທ່ານໄດ້ໝາຍລະຫັດຜ່ານຫຼາຍອັນ.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_ສຳຮອງ",
        'filename_insert_suffix': "_ພ້ອມການແຊກ",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_ໜ້າ_ຖືກລຶບ",
        'filename_pages_moved': "_ໜ້າ_ຖືກຍ້າຍ",
        'filename_rotated_all_suffix': "_ທຸກໜ້າ_ຖືກໝຸນ",
        'filename_rotated_suffix': "_ໜ້າ_ຖືກໝຸນ",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "ການຕັ້ງຄ່າຊື່ໄຟລ໌ເມື່ອປ່ຽນ PDF",
        'filename_keep_suffixes': "ຮັກສານາມສະກຸນເກົ່າ (ຕົວຢ່າງ: _ພ້ອມຂໍ້ຄວາມ)",
        'filename_keep_suffixes_false': "ປ່ຽນແທນ",
        'filename_keep_suffixes_true': "ຮັກສາ",
        'filename_preview_label': "ຕົວຢ່າງຊື່ໄຟລ໌:",
        'filename_preview_overwrite_hint': "ຕົວຢ່າງບໍ່ມີ – ໄຟລ໌ຕົ້ນສະບັບຈະຖືກຂຽນທັບ.",
        'filename_separator': "ຕົວຄັ້ນລະຫວ່າງຄຳ",
        'filename_separator_none': "ບໍ່ມີຕົວຄັ້ນ",
        'filename_separator_space': "ຊ່ອງຫວ່າງ ( )",
        'filename_separator_underscore': "ຂີດກ້ອງ (_)",
        'filename_settings_saved': "ບັນທຶກການຕັ້ງຄ່າຊື່ໄຟລ໌ແລ້ວ",
        'filename_settings_title': "ການຈັດຮູບແບບຊື່ໄຟລ໌ ແລະ ການສຳຮອງ",
        'filename_timestamp_position': "ຕຳແໜ່ງຂອງເວລາປະທັບ",
        'filename_timestamp_position_after': "ຫຼັງຊື່ຫຼັກ",
        'filename_timestamp_position_before': "ຢູ່ທາງໜ້າສຸດ",
        'filename_timestamp_position_end': "ຢູ່ທ້າຍ",
        'filename_use_timestamp': "ໃຊ້ເວລາປະທັບ",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>ພຶດຕິກຳເມື່ອມີການປ່ຽນແປງ:</b><ul><li>ລຶບ ແລະ ແຊກໜ້າ</li><li>ແຊກຂໍ້ຄວາມ, ລາຍເຊັນ, ຮູບພາບ ແລະ ຮູບຮ່າງ</li><li>OCR</li></ul></html>",
        'backup_section': "ການສຳຮອງສຳລັບການດຳເນີນການໜ້າ (ລຶບ, ຍ້າຍ)",
        'behavior_info': "ຫມາຍເຫດ: ເມື່ອ 'ຂຽນທັບຕົ້ນສະບັບ' ເວລາປະທັບ ແລະ ນາມສະກຸນຈະຖືກບໍ່ນຳໃຊ້ – ໄຟລ໌ຈະຮັກສາຊື່ຂອງມັນໄວ້.",
        'behavior_new_file': "ສ້າງໄຟລ໌ໃໝ່ສະເໝີ (ພ້ອມເວລາປະທັບ ແລະ ນາມສະກຸນ)",
        'behavior_overwrite': "ຂຽນທັບຕົ້ນສະບັບ (ບໍ່ມີໄຟລ໌ໃໝ່)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "ທຸກໜ້າໄດ້ຖືກໝຸນ.\n\nຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {0}",
        'all_pages_rotated_voice': "ໝຸນທຸກໜ້າແລ້ວ, ສ້າງໄຟລ໌ໃໝ່.",
        'empty_pages_deleted_new_file': "{0} ໜ້າຫວ່າງຖືກລຶບ.\n\nຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {1}",
        'empty_pages_deleted_voice': "ລຶບ {0} ໜ້າຫວ່າງແລ້ວ, ສ້າງໄຟລ໌ໃໝ່.",
        'ocr_keep_original': "ຮັກສາຕົ້ນສະບັບ (ເປີດດ້ວຍຕົນເອງພາຍຫຼັງ)",
        'ocr_new_file_question': "PDF ໃໝ່ທີ່ສາມາດຄົ້ນຫາໄດ້ຖືກບັນທຶກໄວ້ທີ່:\n{0}\n\nທ່ານຕ້ອງການເປີດມັນຕອນນີ້ບໍ?",
        'ocr_open_new': "ເປີດໄຟລ໌ OCR ໃໝ່",
        'ocr_original_kept': "ໄຟລ໌ຕົ້ນສະບັບຍັງເປີດຢູ່. ໄຟລ໌ OCR ໄດ້ຖືກບັນທຶກແລ້ວ.",
        'page_deleted_new_file': "ໜ້າ {0} ຖືກລຶບ.\n\nຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {1}",
        'page_deleted_voice': "ລຶບໜ້າ {0} ແລ້ວ, ສ້າງໄຟລ໌ໃໝ່.",
        'page_rotated_new_file': "ໜ້າ {0} ຖືກໝຸນ.\n\nຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {1}",
        'page_rotated_voice': "ໝຸນໜ້າ {0} ແລ້ວ, ສ້າງໄຟລ໌ໃໝ່.",
        'pages_deleted_new_file': "ມີ {0} ໜ້າຖືກລຶບ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {1}",
        'pages_deleted_new_file_voice': "ລຶບ {0} ໜ້າແລ້ວ, ສ້າງໄຟລ໌ໃໝ່.",
        'pages_inserted_new_file': "ມີ {0} ໜ້າຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {1}",
        'pages_inserted_new_file_ask': "ມີ {0} ໜ້າຖືກແຊກ.\n\nຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {1}\n\nທ່ານຕ້ອງການເປີດມັນຕອນນີ້ບໍ?",
        'pages_inserted_voice_new': "ແຊກ {0} ໜ້າແລ້ວ, ສ້າງໄຟລ໌ໃໝ່.",
        'pages_moved_new_file': "ມີ {0} ໜ້າຖືກຍ້າຍ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່: {1}",
        'pages_moved_new_file_voice': "ຍ້າຍ {0} ໜ້າແລ້ວ, ສ້າງໄຟລ໌ໃໝ່.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "ຢ່າສະແດງອີກ",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 ການຕັ້ງຄ່າການສຳຮອງ</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ ເປີດການສຳຮອງ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">ສຳລັບການປ່ຽນແປງທັງໝົດທີ່ຂຽນທັບຕົ້ນສະບັບ</strong> (ຂໍ້ຄວາມ, ລາຍເຊັນ, ຮູບພາບ, ຮູບຮ່າງ, OCR, ໝຸນ, ແຊກ, ລຶບ/ຍ້າຍໜ້າ) ຈະຖືກສ້າງ <strong>ການສຳຮອງອັດຕະໂນມັດພ້ອມເວລາປະທັບ</strong> ກ່ອນທີ່ຈະນຳໃຊ້ການປ່ຽນແປງ.</p>
                <p style="margin: 5px 0 5px 20px;">• ການສຳຮອງຈະຢູ່ຂ້າງໄຟລ໌ຕົ້ນສະບັບ (ຕົວຢ່າງ: <code>ເອກະສານ_ສຳຮອງ_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• ຖ້າທ່ານເປີດຕົວເລືອກ <strong>„ຂຽນທັບຕົ້ນສະບັບ“</strong> ເພີ່ມເຕີມ, ການສຳຮອງກໍ່ຈະຖືກສ້າງຄືກັນ.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 ປິດການສຳຮອງ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>ບໍ່ມີການສຳຮອງຖືກສ້າງ</strong> – ທັງເວລາຂຽນທັບ ແລະ ເວລາດຳເນີນການໜ້າ.</p>
                <p style="margin: 5px 0 5px 20px;">• ໄຟລ໌ຕົ້ນສະບັບສາມາດສູນເສຍໄປຢ່າງຖາວອນເມື່ອຖືກຂຽນທັບ.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">ແນະນຳສຳລັບຜູ້ໃຊ້ທີ່ມີປະສົບການເທົ່ານັ້ນ!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ຄຳແນະນຳ:</strong> ການຕັ້ງຄ່າການສຳຮອງແມ່ນເປັນເອກະລາດຈາກຕົວເລືອກ „ຂຽນທັບຕົ້ນສະບັບ“. ທ່ານສາມາດລວມທັງສອງຢ່າງໄດ້.<br>
                ທ່ານສາມາດເຊື່ອງຂໍ້ຄວາມນີ້ແບບຖາວອນໄດ້.
            </div>
        </div>
        """,
        'backup_info_title': "ພຶດຕິກຳການສຳຮອງ",
        'backup_info_voice': "ແຈ້ງການກ່ຽວກັບພຶດຕິກຳການສຳຮອງເມື່ອດຳເນີນການໜ້າ. ເປີດການສຳຮອງຈະຂຽນທັບຕົ້ນສະບັບ, ປິດການສຳຮອງຈະສ້າງໄຟລ໌ໃໝ່.",
        'show_backup_info': "ຂໍ້ມູນກ່ຽວກັບການຕັ້ງຄ່າການສຳຮອງ",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "ຢ່າສະແດງອີກ",
        'overwrite_enable_backup': "ເປີດໃຊ້ງານການສຳຮອງ (ແນະນຳ)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ ຂຽນທັບຕົ້ນສະບັບ</p>
            <p>ຖ້າທ່ານເປີດຕົວເລືອກນີ້, ການປ່ຽນແປງ (ຂໍ້ຄວາມ, ລາຍເຊັນ, ຮູບພາບ, ຮູບຮ່າງ, OCR, ໝຸນ, ແຊກ) ຈະຖືກ <strong>ບັນທຶກໂດຍກົງໃສ່ຕົ້ນສະບັບ</strong> – <strong>ບໍ່ມີການສ້າງໄຟລ໌ໃໝ່</strong>.</p>
            <p>• ຊື່ໄຟລ໌ຍັງຄົງບໍ່ປ່ຽນແປງ.<br>
            • ເວລາປະທັບ ແລະ ນາມສະກຸນຈະຖືກບໍ່ນຳໃຊ້.<br>
            • <strong>ຖ້າບໍ່ມີການສຳຮອງ, ຕົ້ນສະບັບສາມາດສູນເສຍໄປຢ່າງຖາວອນ.</strong></p>
            <p style="color: #FFD700;">ຄຳແນະນຳ: ກະລຸນາເປີດຕົວເລືອກການສຳຮອງເພີ່ມເຕີມ ເພື່ອຮັບສຳເນົາຄວາມປອດໄພອັດຕະໂນມັດ.</p>
        </div>
        """,
        'overwrite_info_title': "ຂຽນທັບຕົ້ນສະບັບ",
        'overwrite_info_voice': "ຄຳເຕືອນ: ຂຽນທັບຕົ້ນສະບັບ – ບໍ່ມີໄຟລ໌ໃໝ່. ແນະນຳໃຫ້ສຳຮອງ.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "ມີ {0} ໜ້າຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຖືກຂຽນທັບ.\nການສຳຮອງຖືກສ້າງ.",
        'pages_inserted_overwrite_no_backup': "ມີ {0} ໜ້າຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຖືກຂຽນທັບ.\nບໍ່ມີການສຳຮອງຖືກສ້າງ.",
        'texts_saved_overwrite_with_backup': "ການປ່ຽນແປງຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nການສຳຮອງຖືກສ້າງ.",
        'texts_saved_overwrite_no_backup': "ການປ່ຽນແປງຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nບໍ່ມີການສຳຮອງຖືກສ້າງ.",
        'texts_crosses_saved_new_file': "{0} {1} ແລະ {2} {3} ຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່ຖືກສ້າງ.\n\nກຳລັງໂຫຼດ PDF ໃໝ່...",
        'texts_saved_new_file': "{0} {1} ຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່ຖືກສ້າງ.\n\nກຳລັງໂຫຼດ PDF ໃໝ່...",
        'crosses_saved_new_file': "{0} {1} ຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່ຖືກສ້າງ.\n\nກຳລັງໂຫຼດ PDF ໃໝ່...",
        'elements_saved_new_file': "{0} ອົງປະກອບຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່ຖືກສ້າງ.\n\nກຳລັງໂຫຼດ PDF ໃໝ່...",
        'signatures_saved_overwrite_with_backup': "ລາຍເຊັນຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nການສຳຮອງຖືກສ້າງ.",
        'signatures_saved_overwrite_no_backup': "ລາຍເຊັນຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nບໍ່ມີການສຳຮອງຖືກສ້າງ.",
        'images_saved_overwrite_with_backup': "ຮູບພາບຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nການສຳຮອງຖືກສ້າງ.",
        'images_saved_overwrite_no_backup': "ຮູບພາບຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nບໍ່ມີການສຳຮອງຖືກສ້າງ.",
        'forms_saved_overwrite_with_backup': "ຮູບຮ່າງຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nການສຳຮອງຖືກສ້າງ.",
        'forms_saved_overwrite_no_backup': "ຮູບຮ່າງຖືກບັນທຶກໄວ້ໃນຕົ້ນສະບັບ.\n\nບໍ່ມີການສຳຮອງຖືກສ້າງ.",
        'signatures_saved_new_file': "{0} ລາຍເຊັນຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່ຖືກສ້າງ.\n\nກຳລັງໂຫຼດ PDF ໃໝ່...",
        'images_saved_new_file': "{0} ຮູບພາບຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່ຖືກສ້າງ.\n\nກຳລັງໂຫຼດ PDF ໃໝ່...",
        'forms_saved_new_file': "{0} ຮູບຮ່າງຖືກແຊກ.\n\nໄຟລ໌ຕົ້ນສະບັບຍັງຄົງບໍ່ປ່ຽນແປງ.\nໄຟລ໌ໃໝ່ຖືກສ້າງ.\n\nກຳລັງໂຫຼດ PDF ໃໝ່...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "ຄຳເຕືອນ: PDF ນີ້ມີໜ້າທີ່ຖືກໝຸນ. ການວາງຕຳແໜ່ງອາດຈະຜິດພາດ.",
        'page_rotated_warning_title': "ກວດພົບໜ້າທີ່ຖືກໝຸນ",
        'page_rotated_warning_message': "ໜ້າປັດຈຸບັນ {0} ຖືກໝຸນ {1}°.\n\nການແຊກອົງປະກອບໃສ່ໜ້າທີ່ຖືກໝຸນບໍ່ຮອງຮັບ.\n\nທ່ານຕ້ອງການໝຸນໜ້າໄປສູ່ຕຳແໜ່ງຕັ້ງຕອນນີ້ບໍ?",
        'page_rotated_warning_voice': "ຄຳເຕືອນ: ໜ້າຖືກໝຸນ. ກະລຸນາໝຸນມັນກ່ອນ.",
        'paste_on_rotated_page_simple_warning': "ບໍ່ສາມາດແຊກໃສ່ໜ້າ {0} ໄດ້!\n\nໜ້ານີ້ຖືກໝຸນ {1}°.\n\nກະລຸນາໝຸນໜ້າໄປທີ່ 0° ກ່ອນ (ເມນູ: ແກ້ໄຂ → ຈັດຮຽງໜ້າ).\n\nຄຳເຕືອນ:\nອົງປະກອບທີ່ສຳເນົາໄວ້ກ່ອນຈະສູນເສຍ ຖ້າທ່ານບໍ່ບັນທຶກກ່ອນທີ່ຈະໝຸນໜ້າ.",
        'paste_on_rotated_page_voice': "ຍົກເລີກການແຊກ. ໜ້າຖືກໝຸນ. ກະລຸນາຈັດຮຽງໜ້າກ່ອນ.",
        'page_rotated_cancel': "ຍົກເລີກ",
        'page_rotated_rotate_until_upright': "ໝຸນໜ້າຊ້ຳໆ (ຈົນກວ່າຈະຕັ້ງ)",
        'page_rotated_now_upright': "ຕອນນີ້ໜ້າຕັ້ງແລ້ວ. ທ່ານສາມາດແຊກໄດ້.",
        'page_rotated_still_not_upright': "ບໍ່ສາມາດໝຸນໜ້າໄປສູ່ຕຳແໜ່ງຕັ້ງໄດ້. ກະລຸນາແກ້ໄຂດ້ວຍຕົນເອງ.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "ວິທີຊ່ວຍເຫຼືອ: ແກ້ໄຂໜ້າທີ່ຖືກໝຸນ",
        'help_rotated_pages_voice': "ກຳລັງເປີດວິທີຊ່ວຍເຫຼືອສຳລັບແກ້ໄຂໜ້າທີ່ຖືກໝຸນ.",
        'btn_help': "ວິທີຊ່ວຍເຫຼືອ",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 ບັນຫາ: ໜ້າທີ່ຖືກໝຸນ – ການແຊກບໍ່ເຮັດວຽກຢ່າງຖືກຕ້ອງ</p>

            <p>ຖ້າການແຊກຂໍ້ຄວາມ, ລາຍເຊັນ ຫຼື ຮູບຮ່າງໃສ່ໜ້າທີ່ຖືກໝຸນບໍ່ເຮັດວຽກຢ່າງຖືກຕ້ອງ, ທ່ານສາມາດແກ້ໄຂໜ້າດ້ວຍຕົວແກ້ໄຂ PDF ພາຍນອກ.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ ວິທີແກ້ໄຂດ້ວຍເຄື່ອງມືພາຍນອກ (ຕົວຢ່າງ: macOS Preview)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>ສົ່ງອອກໜ້າ</strong><br>
                &nbsp;&nbsp;ຄລິກໃນເມນູໃສ່ <strong>ໄຟລ໌ → ສົ່ງອອກເປັນໜ້າ</strong> ຫຼື ໃຊ້ວິທີອື່ນເພື່ອບັນທຶກໜ້າທີ່ຕ້ອງການເປັນ PDF ດຽວ.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>ເປີດໜ້າໃນໂປຣແກຣມພາຍນອກ</strong><br>
                &nbsp;&nbsp;ເປີດ PDF ທີ່ສົ່ງອອກໃນຕົວແກ້ໄຂ PDF (ຕົວຢ່າງ: <strong>macOS Preview</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>ໝຸນໜ້າ</strong><br>
                &nbsp;&nbsp;ໝຸນໜ້າໃຫ້ຕັ້ງຊື່ (ໃນ Preview: <strong>ເຄື່ອງມື → ໝຸນ</strong> ຫຼື <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>ບັນທຶກ</strong><br>
                &nbsp;&nbsp;ບັນທຶກໜ້າທີ່ແກ້ໄຂແລ້ວ (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>ແຊກໜ້າຄືນເຂົ້າໄປໃນເອກະສານຕົ້ນສະບັບ</strong><br>
                &nbsp;&nbsp;ກັບຄືນໄປ PDFDarkView ແລະ ແຊກໜ້າທີ່ແກ້ໄຂແລ້ວໃນຕຳແໜ່ງທີ່ຕ້ອງການ:<br>
                &nbsp;&nbsp;<strong>ແກ້ໄຂ → ແຊກໜ້າ</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 ທາງເລືອກອື່ນ: ໝຸນໜ້າໃນຕົ້ນສະບັບ</p>
                <p style="margin: 5px 0 5px 20px;">• ໃຊ້ຟັງຊັນໝຸນທີ່ມີໃນຕົວ (<strong>ແກ້ໄຂ → ໝຸນໜ້າ</strong>) ເພື່ອແກ້ໄຂໜ້າເທື່ອລະຂັ້ນຕອນ.<br>
                • ຫຼັງຈາກແຕ່ລະການໝຸນ, ທ່ານສາມາດກວດສອບວ່າການແຊກເຮັດວຽກຫຼືບໍ່.<br>
                • ນີ້ມັກຈະເປັນວິທີແກ້ໄຂທີ່ໄວກວ່າ – ລອງໃຊ້ກ່ອນ!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ຄຳແນະນຳ:</strong> ຖ້າທ່ານພົບໜ້າທີ່ຖືກໝຸນເລື້ອຍໆ, ທ່ານສາມາດເຊື່ອງຄຳເຕືອນໃນກ່ອງໂຕ້ຕອບການແຊກໄດ້ຢ່າງຖາວອນ.<br>
                ການວາງຕຳແໜ່ງອາດຈະຜິດພາດ – ໃຊ້ຕົວເລືອກນີ້ສະເພາະຖ້າທ່ານຮູ້ຜົນສະທ້ອນ.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "ຈັດຮຽງໜ້າ",
        'menu_rotate_normalize_tooltip': "ໝຸນໜ້າ ຫຼື ຣີເຊັດໄປທີ່ 0°",
        'normalize_current_page': "ນຳໜ້າປັດຈຸບັນໄປສູ່ຕຳແໜ່ງຕັ້ງ (ຕັ້ງຄ່າເປັນ 0°)",
        'normalize_all_pages': "ນຳທຸກໜ້າໄປສູ່ຕຳແໜ່ງຕັ້ງ (ຕັ້ງຄ່າເປັນ 0°)",
        'page_normalized': "ໜ້າ {0} ຖືກຕັ້ງຄ່າໄປສູ່ຕຳແໜ່ງຕັ້ງ.",
        'all_pages_normalized': "ທຸກໜ້າຖືກຕັ້ງຄ່າໄປສູ່ຕຳແໜ່ງຕັ້ງ.",
        'page_already_upright': "ໜ້າ {0} ຕັ້ງຢູ່ແລ້ວ.",
        'all_pages_already_upright': "ທຸກໜ້າຕັ້ງຢູ່ແລ້ວ.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF ບໍ່ມີຂໍ້ຄວາມທີ່ສາມາດຄົ້ນຫາໄດ້.</p><p>ທ່ານຕ້ອງການເຮັດ OCR ເພື່ອສົ່ງອອກໄປຍັງ {0} ບໍ?</p>",
        'export_ocr_voice': "PDF ບໍ່ມີຂໍ້ຄວາມ. ຕ້ອງການ OCR ສຳລັບການສົ່ງອອກໄປຍັງ {0}.",
        'export_no_ocr_possible': "ບໍ່ສາມາດສົ່ງອອກໂດຍບໍ່ມີ OCR. ກະລຸນາເຮັດ OCR ຜ່ານເມນູ.",
        'ocr_failed_export_not_possible': "OCR ລົ້ມເຫຼວ. ບໍ່ສາມາດສົ່ງອອກໄດ້.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF ຈະເປີດໃນ Preview. ກະລຸນາເລີ່ມຕົ້ນຂະບວນການພິມຢູ່ທີ່ນັ້ນ.",
        'print_preview_manual': "PDF ຖືກເປີດແລ້ວ. ກະລຸນາປະຕິບັດຄຳສັ່ງພິມດ້ວຍຕົນເອງ (ຕົວຢ່າງ: Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "ລວມ PDF",
        'merge_pdfs': "ລວມ PDF",
        'merge_progress_title': "ກຳລັງລວມ PDF...",
        'merge_pdfs_list': "PDF ຕາມລຳດັບ (ລາກ ແລະ ວາງເພື່ອຈັດລຽງ)",
        'merge_add_pdf': "ເພີ່ມ PDF",
        'merge_remove': "ລຶບອອກ",
        'merge_move_up': "ຂຶ້ນ",
        'merge_move_down': "ລົງ",
        'merge_pdfs_info': "💡 ຄຳແນະນຳ: ທ່ານສາມາດປ່ຽນລຳດັບໄດ້ໂດຍການລາກ ແລະ ວາງ",
        'merge_no_pdfs': "ບໍ່ມີ PDF ທີ່ຖືກເລືອກ. ຄລິກໃສ່ 'ເພີ່ມ PDF'.",
        'merge_info': "ເລືອກ {0} PDF (ປະມານ {1} ໜ້າ)",
        'merge_open_file': "ເປີດໄຟລ໌",
        'merge_merge': "ລວມ",
        'merge_error': "ຂໍ້ຜິດພາດໃນການລວມ",
        'merge_min_two_pdfs_error': "ກະລຸນາເລືອກໄຟລ໌ PDF ຢ່າງໜ້ອຍສອງໄຟລ໌ເພື່ອລວມ.",
        'merge_select_pdfs': "ເລືອກ PDF ເພື່ອລວມ",
        'merge_error_file': "ຂໍ້ຜິດພາດໃນການປະມວນຜົນ",
        'merge_cancelled': "ການລວມຖືກຍົກເລີກ",
        'merge_preparing': "ກຳລັງກະກຽມ...",
        'merge_processing': "ກຳລັງປະມວນຜົນ PDF {0} ຈາກ {1}",
        'merge_saving': "ກຳລັງບັນທຶກ PDF ທີ່ລວມແລ້ວ...",
        'merge_complete': "ສຳເລັດ!",
        'merge_success_title': "ການລວມສຳເລັດ",
        'merge_success_voice': "{0} PDF ຖືກລວມສຳເລັດ.",
        'merge_success_message': "{0} PDF ຖືກລວມສຳເລັດ.\n\nເອກະສານໃໝ່ຕອນນີ້ມີ {1} ໜ້າ.\n\nໄຟລ໌ໃໝ່:\n{2}\n\nບ່ອນບັນທຶກ:\n{3}\n{2}\n\nທ່ານຕ້ອງການເປີດ PDF ນີ້ບໍ?",
        'replace_file_title': "ປ່ຽນໄຟລ໌ບໍ?",
        'replace_file_message': "ມີ PDF ເປີດຢູ່ແລ້ວ. ທ່ານຕ້ອງການປ່ຽນມັນດ້ວຍໄຟລ໌ໃໝ່ບໍ?",
        'btn_yes': "ແມ່ນ",
        'btn_no': "ບໍ່",
        'filename_merge_suffix': "ລວມ",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "ກຳລັງເປີດ {0}...",
        'progress_merge_reading': "ກຳລັງອ່ານ {0}...",
        'progress_merge_adding': "ກຳລັງເພີ່ມ {0} ໜ້າ...",
        'progress_merge_optimizing': "ກຳລັງປັບປຸງ PDF...",
        'progress_merge_writing': "ກຳລັງຂຽນ PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "ການປິດ PDF",
        'action_close_window': "ການປິດປ່ອງຢ້ຽມ",
        'action_open_new_pdf': "ການເປີດ PDF ໃໝ່",
        'action_quit_app': "ການອອກຈາກແອັບພລິເຄຊັນ",
        'changes_saved': "ການປ່ຽນແປງຖືກບັນທຶກແລ້ວ.",
        'file_close_title': "ປິດໄຟລ໌ PDF",
        'save_before_action': "ຄວນບັນທຶກການປ່ຽນແປງກ່ອນ {0} ບໍ? ແມ່ນ ຫຼື ບໍ່?",
        'save_before_action_voice': "ຄວນບັນທຶກການປ່ຽນແປງກ່ອນ {0} ບໍ? ແມ່ນ ຫຼື ບໍ່?",
        'save_before_close_question': "ຄວນບັນທຶກການປ່ຽນແປງກ່ອນປິດບໍ? ແມ່ນ ຫຼື ບໍ່?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>ສ້າງ PDF ທີ່ສາມາດຄົ້ນຫາໄດ້:\n\n{0}\n\n<b>ລອງໃໝ່ອີກຄັ້ງຖ້າຈໍາເປັນ",
        "ocr_rotate_title": "ຈັດຮຽງໜ້າກ່ອນ OCR",
        "ocr_rotate_question": "PDF ມີໜ້າທີ່ຖືກໝຸນ.\nທ່ານຕ້ອງການຈັດຮຽງທຸກໜ້າໄປທີ່ 0° ກ່ອນ OCR ບໍ?\nສິ່ງນີ້ຊ່ວຍປັບປຸງການຮັບຮູ້ຂໍ້ຄວາມຢ່າງຫຼວງຫຼາຍ.",
        "ocr_rotate_yes": "ແມ່ນ, ຈັດຮຽງ",
        "ocr_rotate_no": "ບໍ່, ເລີ່ມ OCR ໂດຍກົງ",
        "ocr_rotate_voice": "PDF ມີໜ້າທີ່ຖືກໝຸນ. ຄວນຈັດຮຽງທຸກໜ້າກ່ອນ OCR ບໍ?",
        "ocr_not_performed_message": "ບໍ່ມີຂໍ້ຄວາມ. ກະລຸນາດໍາເນີນການ OCR (ເມນູ \"ແກ້ໄຂ\" → \"ດໍາເນີນການ OCR\" ຫຼືປຸ່ມ Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "ການຕັ້ງຄ່າ OCR",
        "ocr_language_btn": "ເລືອກພາສາ OCR",
        "ocr_language": "ພາສາ OCR",
        "ocr_language_current": "ພາສາປັດຈຸບັນ:",
        "ocr_param_info": "ຂໍ້ມູນກ່ຽວກັບພາຣາມິເຕີ",

        "ocr_force_ocr_label": "ບັງຄັບໃຊ້ OCR",
        "ocr_deskew_label": "ແກ້ໄຂຄວາມອຽງ",
        "ocr_clean_label": "ທໍາຄວາມສະອາດຮູບພາບ",
        "ocr_oversample_label": "ຄວາມລະອຽດ (DPI)",
        "ocr_pagesegmode_label": "ການແບ່ງສ່ວນໜ້າ",
        "ocr_oem_label": "ໂໝດເຄື່ອງຈັກ OCR",
        "ocr_optimize_label": "ການບີບອັດ PDF",
        "ocr_jobs_label": "ຂະບວນການຂະໜານ",
        "ocr_verbose_label": "ລາຍລະອຽດບັນທຶກ",

        "ocr_force_ocr_tooltip": "ບັງຄັບໃຊ້ OCR ໃນທຸກໜ້າ, ເຖິງແມ່ນວ່າຂໍ້ຄວາມມີຢູ່ແລ້ວກໍ່ຕາມ",
        "ocr_deskew_tooltip": "ຈັດຮຽງສະແກນທີ່ອຽງໂດຍອັດຕະໂນມັດ",
        "ocr_clean_tooltip": "ລຶບສິ່ງລົບກວນ ແລະສິ່ງປອມອອກຈາກຮູບພາບ",
        "ocr_oversample_tooltip": "ຂະຫຍາຍຮູບພາບກ່ອນ OCR ໄປຍັງ DPI ນີ້",
        "ocr_pagesegmode_tooltip": "ກໍານົດວິທີການແບ່ງໜ້າເປັນພື້ນທີ່ຂໍ້ຄວາມ",
        "ocr_oem_tooltip": "ເລືອກເຄື່ອງຈັກ OCR ຂອງ Tesseract",
        "ocr_optimize_tooltip": "ລະດັບການບີບອັດຂອງ PDF ຜົນຜະລິດ",
        "ocr_jobs_tooltip": "ຈໍານວນຂະບວນການ OCR ແບບຂະໜານ",
        "ocr_verbose_tooltip": "ລະດັບລາຍລະອຽດຂອງຜົນຜະລິດບັນທຶກ",
        "ocr_settings_explain_btn": "ຄໍາອະທິບາຍ",

        "ocr_force_ocr_explain": "ບັງຄັບການຮັບຮູ້ຂໍ້ຄວາມໃນ<b>ທຸກ</b>ໜ້າ, ເຖິງແມ່ນວ່າມັນມີຂໍ້ຄວາມຢູ່ແລ້ວກໍ່ຕາມ.\n\nຄໍາແນະນໍາ: <b>ເປີດ</b> ສໍາລັບ PDF ທີ່ສະແກນ, <b>ປິດ</b> ສໍາລັບ PDF ຕົ້ນສະບັບທີ່ມີຂໍ້ຄວາມຢູ່ແລ້ວ.",

        "ocr_deskew_explain": "ແກ້ໄຂການສະແກນທີ່ອຽງເລັກນ້ອຍ (ເຖິງປະມານ 5°).\n\nຄໍາແນະນໍາ: <b>ເປີດ</b> ສໍາລັບເອກະສານທີ່ສະແກນ, <b>ປິດ</b> ຖ້າໜ້າຕ່າງໆຕັ້ງຊື່ຢູ່ແລ້ວຢ່າງສົມບູນ.",

        "ocr_clean_explain": "ລຶບສິ່ງລົບກວນ, ຈຸດ ແລະສິ່ງປອມນ້ອຍໆອອກຈາກຮູບພາບ.\n<b>ສໍາຄັນ:</b> ສໍາລັບຂໍ້ຄວາມອາຣັບ, ໄທ ຫຼື ຫວຽດນາມ ທີ່ມີເຄື່ອງໝາຍວັນນະຍຸດ (ຈຸດຢູ່ເທິງ/ລຸ່ມຕົວອັກສອນ) ຄວນ<b>ປິດໃຊ້ງານ</b>ຕົວເລືອກນີ້, ຖ້າບໍ່ດັ່ງນັ້ນຕົວອັກສອນທີ່ສໍາຄັນອາດຈະສູນເສຍໄປ.",

        "ocr_oversample_explain": "ຂະຫຍາຍຮູບພາບ<b>ກ່ອນ</b>ການຮັບຮູ້ຂໍ້ຄວາມໄປຍັງ DPI ທີ່ກໍານົດ.<br><br>• <b>72-150 DPI:</b> ໄວຫຼາຍ, ແຕ່ອັດຕາການຮັບຮູ້ຕໍ່າ<br>• <b>200-300 DPI:</b> ຊ່ວງທີ່ດີທີ່ສຸດ (ຄ່າເລີ່ມຕົ້ນ: 300)<br>• <b>400+ DPI:</b> ແທບຈະບໍ່ມີການຮັບຮູ້ທີ່ດີກວ່າ, ແຕ່ໄຟລ໌ໃຫຍ່ກວ່າຫຼາຍ<br><br>ຄໍາແນະນໍາ: 300 DPI ສໍາລັບຕົວໜັງສືທີ່ຊັບຊ້ອນ (ອາຣັບ, ຈີນ, ຍີ່ປຸ່ນ), 200 DPI ສໍາລັບພາສາຕາເວັນຕົກ.",

        "ocr_pagesegmode_explain": "ກໍານົດວິທີການ Tesseract ແບ່ງໜ້າເປັນພື້ນທີ່ຂໍ້ຄວາມ.\n\n• <b>3 - ອັດຕະໂນມັດ (ຄ່າເລີ່ມຕົ້ນ):</b> ດີສໍາລັບຮູບແບບປະສົມ\n• <b>4 - ຖັນດຽວ:</b> ສໍາລັບຂໍ້ຄວາມຖັນດຽວ\n• <b>5 - ບລັອກແນວຕັ້ງ:</b> ສໍາລັບຕົວໜັງສືແນວຕັ້ງ (ຍີ່ປຸ່ນ, ຈີນ)\n• <b>6 - ບລັອກຂໍ້ຄວາມເປັນເອກະພາບ:</b> ດີທີ່ສຸດສໍາລັບຂໍ້ຄວາມໄຫຼໂດຍບໍ່ມີຖັນ\n• <b>11 - ຮູບພາບດິບ:</b> ສໍາລັບການສະແກນທີ່ບໍ່ດີ / ລາຍມື\n\nຄໍາແນະນໍາ: <b>6</b> ສໍາລັບເອກະສານຂໍ້ຄວາມງ່າຍດາຍ, <b>3</b> ສໍາລັບຮູບແບບທີ່ຊັບຊ້ອນ.",

        "ocr_oem_explain": "ເລືອກເຄື່ອງຈັກ OCR ຂອງ Tesseract.\n\n• <b>0 - Legacy:</b> ເຄື່ອງຈັກເກົ່າ (ໄວ, ແຕ່ບໍ່ຄ່ອຍຖືກຕ້ອງ)\n• <b>1 - LSTM:</b> ເຄື່ອງຈັກປະສາດ (ຊ້າກວ່າ, ແຕ່ຖືກຕ້ອງກວ່າ)\n• <b>2 - Legacy + LSTM:</b> ລວມທັງສອງຜົນໄດ້ຮັບ\n• <b>3 - ຄ່າເລີ່ມຕົ້ນ (LSTM ຕ້ອງການ):</b> ທາງເລືອກທີ່ດີທີ່ສຸດສໍາລັບກໍລະນີສ່ວນໃຫຍ່\n\nຄໍາແນະນໍາ: <b>3</b> ສໍາລັບຄວາມຖືກຕ້ອງສູງສຸດຂອງການຮັບຮູ້.",

        "ocr_optimize_explain": "ບີບອັດ PDF ຜົນຜະລິດ.\n\n• <b>0:</b> ບໍ່ມີການປັບປຸງ (ການປະມວນຜົນໄວທີ່ສຸດ)\n• <b>1:</b> ການປັບປຸງເບົາ (ການປະນີປະນອມທີ່ດີ)\n• <b>2:</b> ການປັບປຸງປານກາງ\n• <b>3:</b> ການປັບປຸງແຮງ (ໄຟລ໌ນ້ອຍທີ່ສຸດ, ແຕ່ຊ້າກວ່າ)\n\nຄໍາແນະນໍາ: <b>1</b> ສໍາລັບການນໍາໃຊ້ປະຈໍາວັນ.",

        "ocr_jobs_explain": "ຈໍານວນຂະບວນການຂະໜານສໍາລັບ OCR.\n\n• <b>1:</b> ຊ້າ, ແຕ່ການໃຊ້ຫນ່ວຍຄວາມຈໍາຕໍ່າສຸດ\n• <b>4-8:</b> ດີທີ່ສຸດສໍາລັບໂປເຊດເຊີຫຼາຍແກນທີ່ທັນສະໄໝ\n• <b>12+:</b> ແທບຈະບໍ່ມີການປະມວນຜົນໄວກວ່າດ້ວຍການໃຊ້ຫນ່ວຍຄວາມຈໍາສູງ\n\nຄໍາແນະນໍາ: ຈໍານວນແກນ CPU (ຕົວຢ່າງ: <b>4</b> ໃນລະບົບ 4 ແກນ).",

        "ocr_verbose_explain": "ລະດັບລາຍລະອຽດຂອງຜົນຜະລິດບັນທຶກໃນຄອນໂຊນ.\n\n• <b>0:</b> ບໍ່ມີຜົນຜະລິດ\n• <b>1:</b> ຄວາມຄືບຫນ້າ ແລະຂໍ້ຄວາມສະຖານະ\n• <b>2:</b> ຜົນຜະລິດລາຍລະອຽດ\n• <b>3:</b> ຜົນຜະລິດດີບັກເຕັມ (ກວ້າງຂວາງຫຼາຍ)\n\nຄໍາແນະນໍາ: <b>1</b> ສໍາລັບການດໍາເນີນງານປົກກະຕິ.",

        "ocr_reset_title": "ການຕັ້ງຄ່າຖືກຣີເຊັດ",
        "ocr_reset_message": "ການຕັ້ງຄ່າ OCR ທັງໝົດຖືກຣີເຊັດໃສ່ຄ່າເລີ່ມຕົ້ນ.",
        "info_tooltip": "ຂໍ້ມູນເພີ່ມເຕີມກ່ຽວກັບພາຣາມິເຕີນີ້",
        "ocr_reset_defaults": "ຣີເຊັດໃສ່ຄ່າເລີ່ມຕົ້ນ",

        "ocr_psm_0": "ອັດຕະໂນມັດ (ເຄື່ອງຈັກ Legacy)",
        "ocr_psm_1": "ການກວດຈັບຖັນອັດຕະໂນມັດ",
        "ocr_psm_3": "ອັດຕະໂນມັດ (ຄ່າເລີ່ມຕົ້ນ)",
        "ocr_psm_4": "ຖັນດຽວ",
        "ocr_psm_5": "ບລັອກແນວຕັ້ງ",
        "ocr_psm_6": "ບລັອກຂໍ້ຄວາມເປັນເອກະພາບ",
        "ocr_psm_7": "ແຖວຂໍ້ຄວາມດຽວ",
        "ocr_psm_8": "ຄໍາດຽວ",
        "ocr_psm_11": "ຮູບພາບດິບ (ບໍ່ມີການວິເຄາະຮູບແບບ)",

        "ocr_oem_0": "ເຄື່ອງຈັກ Legacy (ໄວ)",
        "ocr_oem_1": "ເຄື່ອງຈັກ LSTM (ປະສາດ, ຖືກຕ້ອງ)",
        "ocr_oem_2": "Legacy + LSTM ປະສົມ",
        "ocr_oem_3": "ຄ່າເລີ່ມຕົ້ນ (LSTM ຕ້ອງການ)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "ພາສາ OCR...",
        "ocr_language_title": "ເລືອກພາສາ OCR",
        "ocr_language_instruction": "ເລືອກພາສາສໍາລັບການຮັບຮູ້ຂໍ້ຄວາມ (OCR).\nລະວັງ: ພາສາຫຼາຍພາສາຈະສົ່ງຜົນກະທົບຕໍ່ປະສິດທິພາບ ແລະຄວາມຖືກຕ້ອງ!\nທ່ານຈະໄດ້ຮັບຜົນໄດ້ຮັບທີ່ດີທີ່ສຸດຖ້າທ່ານເລືອກພາສາດຽວເທົ່ານັ້ນ.",
        "ocr_language_predefined": "ການປະສົມທີ່ກໍານົດໄວ້ລ່ວງຫນ້າ",
        "ocr_language_custom": "ກໍາຫນົດເອງ...",
        "ocr_language_selected": "ພາສາ OCR ທີ່ເລືອກ",
        "ocr_language_changed": "ປ່ຽນພາສາ OCR ເປັນ {0}",
        "ocr_language_auto_detect": "ພາສາທີ່ມີຢູ່ຖືກກວດພົບໂດຍອັດຕະໂນມັດ.",
        "ocr_language_none_found": "ບໍ່ພົບຂໍ້ມູນພາສາ Tesseract! ກະລຸນາຕິດຕັ້ງຊຸດພາສາ (ຕົວຢ່າງ: 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "ການເລືອກພາສາທີ່ກໍາຫນົດເອງ",
        "ocr_language_available": "ພາສາທີ່ມີຢູ່ (ຕິດຕັ້ງແລ້ວ):",
        "ocr_language_select_hint": "ເລືອກຫນຶ່ງ ຫຼື ຫຼາຍພາສາ:",
        "ocr_language_confirm": "ນໍາໃຊ້",
        "ocr_language_reset": "ຣີເຊັດໃສ່ຄ່າເລີ່ມຕົ້ນ (deu+eng+vie)",
        "ocr_language_priorities": "ພາສາທີ່ແນະນໍາ (ຕິດຕັ້ງມາກ່ອນ):",

        "select_all_languages": "ເລືອກທັງໝົດ",
        "clear_all_languages": "ລຶບການເລືອກ",
        "install_language_packs": "ຕິດຕັ້ງຊຸດພາສາທີ່ຂາດຫາຍໄປ...",
        "install_hint": "💡 ຄໍາແນະນໍາ: ບໍ່ແມ່ນທຸກພາສາຖືກຕິດຕັ້ງໃນລະບົບຂອງທ່ານ. ໂດຍຜ່ານປຸ່ມນີ້ທ່ານຈະໄດ້ຮັບຄວາມຊ່ວຍເຫຼືອສໍາລັບການຕິດຕັ້ງ.",
        "ocr_language_install_title": "ການຕິດຕັ້ງຊຸດພາສາ Tesseract",

        "ocr_missing_languages": "ຊຸດພາສາ OCR ທີ່ຂາດຫາຍໄປ",
        "ocr_missing_languages_message": "ພາສາທີ່ເລືອກຕໍ່ໄປນີ້ບໍ່ໄດ້ຕິດຕັ້ງໃນລະບົບຂອງທ່ານ:\n\n{0}\n\nກະລຸນາຕິດຕັ້ງຊຸດພາສາທີ່ຂາດຫາຍໄປ (ເບິ່ງຄວາມຊ່ວຍເຫຼືອພາຍໃຕ້ 'ຄວາມຊ່ວຍເຫຼືອການຕິດຕັ້ງ').\n\nທ່ານຕ້ອງການເປີດຄວາມຊ່ວຍເຫຼືອການຕິດຕັ້ງດຽວນີ້ບໍ?",
        "ocr_missing_languages_voice": "ຊຸດພາສາຂາດຫາຍໄປ. ກະລຸນາຕິດຕັ້ງພາສາທີ່ຂາດຫາຍໄປ.",
        "ocr_install_help_now": "ເປີດຄວາມຊ່ວຍເຫຼືອ",
        "ocr_continue_anyway": "ລອງເບິ່ງກໍ່ໄດ້",
        "ocr_language_error_title": "ຂໍ້ຜິດພາດພາສາ OCR",
        "ocr_language_error_message": "ຂໍ້ຜິດພາດໃນລະຫວ່າງການຮັບຮູ້ຂໍ້ຄວາມ: {0}\n\nກະລຸນາກວດສອບການຕັ້ງຄ່າພາສາ OCR ຂອງທ່ານ (ການຕັ້ງຄ່າ → ພາສາ OCR).",
        "ocr_install_help_button": "ຄວາມຊ່ວຍເຫຼືອການຕິດຕັ້ງ",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 ຕິດຕັ້ງຊຸດພາສາ Tesseract</p>

        <p>ເພື່ອໃຫ້ OCR ເຮັດວຽກເປັນພາສາສະເພາະ, ຂໍ້ມູນພາສາທີ່ກົງກັນຕ້ອງໄດ້ຮັບການຕິດຕັ້ງໃນລະບົບຂອງທ່ານ. ປະຕິບັດຕາມຄໍາແນະນໍາສໍາລັບລະບົບປະຕິບັດການຂອງທ່ານ:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>ເປີດ <strong>Terminal</strong> (Finder → ໂປຣແກຣມ → ປະໂຫຍດ → Terminal).</li>
        <li>ຕິດຕັ້ງພາສາທີ່ມີຢູ່ທັງໝົດດ້ວຍ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (ອາດໃຊ້ເວລາສອງສາມນາທີ.)</li>
        <li>ຫຼືພຽງແຕ່ພາສາສ່ວນບຸກຄົນ (ຕົວຢ່າງ: ຫວຽດນາມ):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        ດ້ວຍເວີຊັນ Homebrew ປັດຈຸບັນ, ອາດຈໍາເປັນຕ້ອງດາວໂຫຼດ <code>*.traineddata</code> ດ້ວຍຕົນເອງ (ເບິ່ງຂ້າງລຸ່ມ).</li>
        <li>ຫຼັງຈາກການຕິດຕັ້ງ: ປິດກ່ອງໂຕ້ຕອບນີ້ ແລະເປີດການເລືອກພາສາ OCR ອີກຄັ້ງ – ພາສາໃຫມ່ຈະປາກົດຂຶ້ນໂດຍອັດຕະໂນມັດ.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>ເປີດຄອນໂຊນ (Ctrl+Alt+T).</li>
        <li>ຕິດຕັ້ງພາສາທີ່ຕ້ອງການ, ຕົວຢ່າງສໍາລັບຫວຽດນາມ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        ລະຫັດພາສາທີ່ສໍາຄັນ: <code>deu</code> (ເຢຍລະມັນ), <code>eng</code> (ອັງກິດ), <code>vie</code> (ຫວຽດນາມ), <code>spa</code> (ແອສປາໂຍນ), <code>fra</code> (ຝຣັ່ງ), <code>ita</code> (ອີຕາລີ), <code>nld</code> (ໂຮນລັງ), <code>fin</code> (ແຟງລັງ), <code>swe</code> (ສະວີເດັນ), <code>nor</code> (ນໍເວ).</li>
        <li>ສະແດງຊຸດທີ່ມີຢູ່ທັງໝົດ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ດ້ວຍຕົນເອງ)</p>
        <ol>
        <li>ດາວໂຫຼດໄຟລ໌ <code>*.traineddata</code> ທີ່ຕ້ອງການຈາກ:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ຕົວຢ່າງ: <code>vie.traineddata</code> ສໍາລັບຫວຽດນາມ).</li>
        <li>ສໍາເນົາໄຟລ໌ໄປຍັງໂຟນເດີພາສາ Tesseract, ປົກກະຕິ:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (ປັບຕາມການຕິດຕັ້ງສ່ວນບຸກຄົນ.)</li>
        <li>ເລີ່ມຕົ້ນແອັບພລິເຄຊັນໃຫມ່ (ຫຼືເປີດການເລືອກພາສາ OCR ອີກຄັ້ງ).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 ທາງເລືອກສໍາລັບທຸກລະບົບ</p>
        <ul>
        <li>ຕິດຕັ້ງ <strong>OCRmyPDF</strong> ແລະ <strong>Tesseract</strong> ດ້ວຍຕົວຈັດການຊຸດທີ່ທ່ານເລືອກ. ການຕິດຕັ້ງສ່ວນໃຫຍ່ມີພາສາມາດຕະຖານບາງພາສາແລ້ວ (ອັງກິດ, ເຢຍລະມັນ, ຝຣັ່ງ).</li>
        <li>ພາສາທີ່ຂາດຫາຍໄປສາມາດຕິດຕັ້ງໄດ້ທຸກເວລາ – ການເລືອກພາສາ OCR ຈະສະແດງພຽງແຕ່ພາສາທີ່ມີຢູ່ແທ້ເທົ່ານັ້ນ.</li>
        </ul>

        <hr>
        <p><b>✅ ຫຼັງຈາກການຕິດຕັ້ງ:</b> ບໍ່ຈໍາເປັນຕ້ອງເລີ່ມຕົ້ນແອັບພລິເຄຊັນໃຫມ່ – ພາສາທີ່ເພີ່ມໃຫມ່ຈະປາກົດຂຶ້ນທັນທີໃນລາຍຊື່.</p>
        <p><b>📖 ຄວາມຊ່ວຍເຫຼືອກ່ຽວກັບລະຫັດພາສາ:</b> ລາຍຊື່ເຕັມສາມາດເບິ່ງໄດ້ໃນ <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">ເອກະສານ Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "ຟອນ Noto Sans",
        "info_noto_font_voice": "ຄູ່ມືການຕິດຕັ້ງຟອນ Noto Sans",
        "btn_info_noto_font_install": "ຂໍ້ມູນຟອນ",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ ວິທີການຕິດຕັ້ງຟອນ Noto ຟຣີຈາກ Google</h2>

        <p><strong>ຟອນ Noto</strong> ແມ່ນຄອບຄົວຟອນແຫຼ່ງເປີດຈາກ Google. ເປົ້າໝາຍຂອງພວກມັນແມ່ນເພື່ອບໍ່ໃຫ້ເຫັນ <em>"ເຕົາຮູ້"</em> (ຄືບໍ່ມີກ່ອງຫວ່າງ □) ແລະສະແດງຕົວອັກສອນທຸກຕົວຈາກມາດຕະຖານ Unicode ຢ່າງຖືກຕ້ອງ. ພວກມັນແມ່ນສ່ວນເສີມທີ່ເຫມາະສົມສໍາລັບແອັບພລິເຄຊັນທີ່ຕ້ອງສະແດງຂໍ້ຄວາມເປັນຫຼາຍພາສາທີ່ແຕກຕ່າງກັນ.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 ການຕິດຕັ້ງໃນ macOS</h3>

        <p><strong>ວິທີທີ 1: ໃຊ້ Homebrew (ສໍາລັບຜູ້ຊ່ຽວຊານ)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>ວິທີທີ 2: ຜ່ານ "Font Book" (ແນະນໍາ)</strong></p>

        <ol>
        <li>ດາວໂຫຼດຊຸດຟອນທາງການ:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ຖອນໄຟລ໌ ZIP</li>
        <li>ສໍາເນົາໄຟລ໌ໄປຍັງ <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 ການຕິດຕັ້ງໃນ Windows (10 & 11)</h3>

        <p><strong>ວິທີທີ 1: Microsoft Store (ແນະນໍາ)</strong><br>
        ຄົ້ນຫາ "Google Noto Fonts" ຫຼື "Noto Sans" ແລະຄລິກ <strong>ຕິດຕັ້ງ</strong>.</p>

        <p><strong>ວິທີທີ 2: ການຕິດຕັ້ງດ້ວຍຕົນເອງ</strong></p>

        <ol>
        <li>ດາວໂຫຼດ:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ຖອນ ZIP</li>
        <li>ເລືອກໄຟລ໌ .ttf / .otf</li>
        <li>ຄລິກຂວາ → <strong>ຕິດຕັ້ງ</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        ຫຼື<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\ຊື່\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 ການຕິດຕັ້ງໃນ Linux</h3>

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

        <p>ການກວດສອບ:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "ຈັດການບຸກມາກ",
        "bookmark_add": "ເພີ່ມບຸກມາກ",
        "bookmark_add_tooltip": "ບັນທຶກຫນ້າປັດຈຸບັນເປັນບຸກມາກ",
        "bookmark_remove": "ລຶບບຸກມາກ",
        "bookmark_remove_tooltip": "ລົບບຸກມາກທີ່ຖືກໝາຍ",
        "bookmark_remove_all": "ລຶບທັງໝົດ",
        "bookmark_remove_all_tooltip": "ລົບບຸກມາກທັງໝົດຂອງ PDF ນີ້",
        "bookmark_jump": "ໄປທີ່ບຸກມາກ",
        "bookmark_jump_tooltip": "ໄປທີ່ຫນ້າທີ່ເລືອກ",
        "bookmark_name": "ຊື່",
        "bookmark_page": "ຫນ້າ",
        "bookmark_no_bookmarks": "ບໍ່ມີບຸກມາກ.\nຄລິກ 'ເພີ່ມ' ເພື່ອບັນທຶກຫນ້າປັດຈຸບັນເປັນບຸກມາກ.",
        "bookmark_added": "ເພີ່ມບຸກມາກສໍາລັບຫນ້າ {0}: {1}",
        "bookmark_removed": "ລຶບບຸກມາກ: {0}",
        "bookmark_all_removed": "ບຸກມາກທັງໝົດຖືກລຶບແລ້ວ.",
        "bookmark_name_default": "ຫນ້າ {0}",
        "bookmark_name_prompt": "ຊື່ສໍາລັບບຸກມາກ:\n(ຂໍ້ຄວາມຍາວຈະຖືກຕັດລົງເຫຼືອ 50 ຕົວອັກສອນ)",
        "bookmark_name_prompt_title": "ຊື່ບຸກມາກ",
        "bookmark_confirm_remove_all": "ທ່ານແນ່ໃຈບໍວ່າຕ້ອງການລຶບທັງ {0} ບຸກມາກ?",
        "menu_bookmarks": "ບຸກມາກ",
        "bookmark_manage": "ຈັດການບຸກມາກ",
        "bookmark_next": "ບຸກມາກຕໍ່ໄປ",
        "bookmark_prev": "ບຸກມາກກ່ອນຫນ້າ",
        "bookmark_page_display": "ຫນ້າ {0}",
        "bookmark_exists": "ມີບຸກມາກສໍາລັບຫນ້ານີ້ທີ່ມີຊື່ນີ້ຢູ່ແລ້ວ.",
        "bookmark_select_first": "ກະລຸນາເລືອກບຸກມາກກ່ອນ.",
        "bookmark_confirm_remove": "ທ່ານແນ່ໃຈບໍວ່າຕ້ອງການລຶບບຸກມາກ 'ຫນ້າ {0}: {1}'?",
        "bookmark_jumped_to": "ໄປທີ່ບຸກມາກ '{0}' ໃນຫນ້າ {1}.",
        "bookmark_jumped_to_voice": "ບຸກມາກ {0}, ຫນ້າ {1}",
        "btn_close": "ປິດ",

        "bookmark_list": "ບຸກມາກຂອງທ່ານ",
        "bookmark_rename": "ປ່ຽນຊື່ບຸກມາກ",
        "bookmark_rename_tooltip": "ປ່ຽນຊື່ຂອງບຸກມາກທີ່ເລືອກ",
        "bookmark_rename_title": "ປ່ຽນຊື່ບຸກມາກ",
        "bookmark_rename_prompt": "ຊື່ໃຫມ່ສໍາລັບບຸກມາກໃນຫນ້າ {0}:\n(ສູງສຸດ 50 ຕົວອັກສອນ)",
        "bookmark_renamed": "ປ່ຽນຊື່ບຸກມາກ '{0}' ເປັນ '{1}'.",
        "bookmark_item_tooltip": "ຫນ້າ {0}: {1}\nຄລິກສອງຄັ້ງເພື່ອໄປ",
        "bookmark_name_exists_question": "ມີບຸກມາກທີ່ມີຊື່ '{0}' ຢູ່ໃນຫນ້ານີ້ແລ້ວ.\nປ່ຽນຊື່ຕໍ່ໄປບໍ?",

        "context_bookmarks": "ບຸກມາກ",
        "context_bookmark_add_here": "ເພີ່ມບຸກມາກສໍາລັບຫນ້ານີ້",
        "context_bookmarks_existing": "ບຸກມາກທີ່ມີຢູ່ແລ້ວ:",
        "context_bookmarks_jump": "ໄປທີ່ບຸກມາກ:",
        "context_bookmarks_none": "ບໍ່ມີບຸກມາກ",
        "context_bookmarks_clear_all": "ລຶບທັງ {0} ບຸກມາກ",

        "bookmark_search_placeholder": "ຄົ້ນຫາບຸກມາກ... (ຊື່ ຫຼື ຫນ້າ)",
        "bookmark_search_results": "ພົບ %d ບຸກມາກສໍາລັບ \"%s\"",
        "bookmark_no_search_results": "ບໍ່ພົບບຸກມາກສໍາລັບ \"%s\"",
        "bookmark_no_search_results_label": "ບໍ່ມີຜົນໄດ້ຮັບສໍາລັບ \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "ແກ້ໄຂເມຕາເດຕາຂອງ PDF",
        "metadata_title": "ຫົວຂໍ້",
        "metadata_title_placeholder": "ຫົວຂໍ້ເອກະສານ",
        "metadata_title_tooltip": "ຫົວຂໍ້ຂອງເອກະສານ (ສະແດງຢູ່ໃນແຖບຫົວຂໍ້)",
        "metadata_author": "ຜູ້ຂຽນ",
        "metadata_author_placeholder": "ຊື່ຜູ້ຂຽນ",
        "metadata_author_tooltip": "ຜູ້ສ້າງເອກະສານ",
        "metadata_subject": "ຫົວຂໍ້",
        "metadata_subject_placeholder": "ຫົວຂໍ້ຂອງເອກະສານ",
        "metadata_subject_tooltip": "ຄໍາອະທິບາຍສັ້ນຂອງເນື້ອຫາ",
        "metadata_keywords": "ຄໍາສໍາຄັນ",
        "metadata_keywords_placeholder": "ຄໍາສໍາຄັນ, ຄັ້ນດ້ວຍຈຸດ",
        "metadata_keywords_tooltip": "ຄໍາສໍາຄັນສໍາລັບການຈັດປະເພດເອກະສານ",
        "metadata_creator": "ຜູ້ສ້າງ",
        "metadata_creator_placeholder": "ແອັບພລິເຄຊັນທີ່ສ້າງ PDF",
        "metadata_creator_tooltip": "ຊອບແວທີ່ໃຊ້ສ້າງເອກະສານ",
        "metadata_producer": "ຜູ້ຜະລິດ",
        "metadata_producer_placeholder": "ແອັບພລິເຄຊັນທີ່ປ່ຽນ PDF",
        "metadata_producer_tooltip": "ຊອບແວທີ່ປ່ຽນ PDF",
        "metadata_creation_date": "ວັນທີສ້າງ",
        "metadata_creation_date_tooltip": "ວັນທີສ້າງເອກະສານ",
        "metadata_mod_date": "ວັນທີດັດແກ້",
        "metadata_mod_date_tooltip": "ວັນທີດັດແກ້ຄັ້ງສຸດທ້າຍ",
        "metadata_pdf_info": "📄 ຂໍ້ມູນ PDF",
        "metadata_pages": "ຈໍານວນຫນ້າ",
        "metadata_file_size": "ຂະຫນາດໄຟລ໌",
        "metadata_pdf_version": "ເວີຊັນ PDF",
        "metadata_encrypted": "ຖືກເຂົ້າລະຫັດ",
        "metadata_encrypted_yes": "ແມ່ນ (ປ້ອງກັນດ້ວຍລະຫັດຜ່ານ)",
        "metadata_encrypted_no": "ບໍ່",
        "metadata_reload": "📂 ໂຫຼດຄືນຈາກ PDF",
        "metadata_reset": "ຍົກເລີກການປ່ຽນແປງ",
        "metadata_reloaded": "ເມຕາເດຕາຖືກໂຫຼດຄືນຈາກ PDF.",
        "metadata_reset_done": "ທຸກຊ່ອງຂໍ້ມູນເມຕາເດຕາຖືກຣີເຊັດ.",
        "metadata_no_file": "ບໍ່ມີໄຟລ໌ PDF ຖືກໂຫຼດ.",
        "metadata_save_error": "ຂໍ້ຜິດພາດໃນການບັນທຶກເມຕາເດຕາ",
        "metadata_saved": "ເມຕາເດຕາຖືກບັນທຶກສໍາເລັດ.",
        "metadata_pdf_version_unknown": "PDF (ບໍ່ຮູ້ຈັກ)",
        "metadata_saved_message": "ເມຕາເດຕາຖືກບັນທຶກສໍາເລັດ.",
        "metadata_saved_voice": "ບັນທຶກເມຕາເດຕາແລ້ວ.",

        "metadata_custom": "🔧 ເມຕາເດຕາທີ່ກໍາຫນົດເອງ",
        "metadata_custom_placeholder": "{\n  \"ຊ່ອງຂໍ້ມູນຂອງຂ້ອຍ\": \"ຄ່າຂອງຂ້ອຍ\",\n  \"ຊ່ອງຂໍ້ມູນອື່ນ\": 123\n}",
        "metadata_custom_tooltip": "ຮູບແບບ JSON ສໍາລັບເມຕາເດຕາທີ່ກໍາຫນົດເອງ (ທາງເລືອກ)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "ເລືອກແມ່ແບບ \"{0}\" ແລ້ວ - ຄລິກສອງຄັ້ງເພື່ອໃສ່",
        "text_use_template": "ໃຊ້ບລັອກຂໍ້ຄວາມ",
        "text_type": "ປະເພດ",
        "text_search_templates": "ຄົ້ນຫາບລັອກຂໍ້ຄວາມ...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 ຂໍ້ມູນການສົ່ງອອກ / ນໍາເຂົ້າ",
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

        <h3>📦 ມີຫຍັງແດ່ທີ່ຖືກສົ່ງອອກ? (ພາບລວມ)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">ການຕັ້ງຄ່າແອັບພລິເຄຊັນທົ່ວໄປ</span></li>
            <li class="detail">• ໂໝດມືດ/ສະຫວ່າງ</li>
            <li class="detail">• ການກັບກັນໂໝດມືດສໍາລັບຮູບພາບ</li>
            <li class="detail">• ຄ່າເກນສີເທົາ</li>
            <li class="detail">• ພາສາ</li>
            <li class="detail">• ເລຂາຄະນິດປ່ອງຢ້ຽມ</li>
            <li class="detail">• ໂໝດຂະຫຍາຍ</li>
            <li class="detail">• ການນໍາທາງ (ແຖບນໍາທາງເບິ່ງເຫັນ)</li>
            <li class="detail">• ຜົນຜະລິດສຽງ (ເປີດ/ປິດ)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ການຕັ້ງຄ່າສໍາຮອງ</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ການຕັ້ງຊື່ໄຟລ໌ (ປະທັບເວລາ, ຕົວຄັ້ນ, ຕົວຕໍ່ທ້າຍ)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ການຕັ້ງຄ່າສໍາລັບການໃສ່</span></li>
            <li class="detail">• ລາຍເຊັນ</li>
            <li class="detail">• ຂໍ້ຄວາມ &amp; ບລັອກຂໍ້ຄວາມ</li>
            <li class="detail">• ເຄື່ອງໝາຍ, ຮູບພາບ ແລະຮູບຮ່າງ</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ການຕັ້ງຄ່າ OCR</span></li>
            <li class="detail">• ພາສາ</li>
            <li class="detail">• ບັງຄັບໃຊ້ OCR · ໂໝດຫນ້າ</li>
            <li class="detail">• ການປຸງແຕ່ງຮູບພາບລ່ວງຫນ້າ: ແກ້ໄຂຄວາມອຽງ, ທໍາຄວາມສະອາດ, ການເກັບຕົວຢ່າງເກີນ</li>
            <li class="detail">• ຈໍານວນວຽກຂະໜານ</li>
            <li class="detail">• ໂໝດການກັບກັນ</li>
            <li class="detail">• ຄ່າເກນສີເທົາ</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ບຸກມາກ</span></li>
            <li class="detail">• ບຸກມາກທັງໝົດຕໍ່ໄຟລ໌ PDF (ຫນ້າ, ຊື່, ເວລາສ້າງ)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ຖານຂໍ້ມູນລະຫັດຜ່ານ</span></li>
            <li class="detail">• ລະຫັດຜ່ານ PDF ທີ່ບັນທຶກໄວ້ (ຖືກເຂົ້າລະຫັດ ຫຼື ຂໍ້ຄວາມທໍາມະດາຕາມທາງເລືອກ)</li>
            <li class="detail">• Hash ລະຫັດຜ່ານຫຼັກ (ຖ້າຕັ້ງໄວ້)</li>
            <li class="detail">• ຂໍ້ມູນການກວດສອບ</li>
        </ul>

        <h4>⚠️ ຂໍ້ສັງເກດທີ່ສໍາຄັນ</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 ເວລານໍາເຂົ້າ:</strong>
            <ul>
                <li><span class="warning">➜ ການຕັ້ງຄ່າປັດຈຸບັນທັງໝົດຈະຖືກຂຽນທັບຢ່າງສົມບູນ</span></li>
                <li>• ຕ້ອງຣີສະຕາດແອັບພລິເຄຊັນ</li>
                <li>• ລາຍເຊັນ, ບລັອກຂໍ້ຄວາມ ແລະບຸກມາກທີ່ມີຢູ່ຈະຖືກແທນທີ່</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 ລະຫັດຜ່ານຫຼັກ ແລະໂໝດການສົ່ງອອກ:</strong>
            <ul>
                <li>• ເມື່ອລະຫັດຜ່ານຫຼັກເຮັດວຽກ, ທ່ານສາມາດເລືອກ:</li>
                <li>  - <span style="color: #98FB98;"><strong>ຖອດລະຫັດແລ້ວ</strong></span> (ລະຫັດຜ່ານຢູ່ໃນຮູບແບບຂໍ້ຄວາມທໍາມະດາໃນ ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>ຖືກເຂົ້າລະຫັດແລ້ວ</strong></span> (ສາມາດອ່ານໄດ້ດ້ວຍລະຫັດຜ່ານຫຼັກເທົ່ານັ້ນໃນລະບົບປາຍທາງ)</li>
                <li>• Hash ລະຫັດຜ່ານຫຼັກແມ່ນຖືກເກັບຮັກສາໄວ້ <strong>ສະເໝີ</strong> ໃນຮູບແບບທີ່ຖືກເຂົ້າລະຫັດ</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ ແຈ້ງການຄວາມປອດໄພ:</strong>
            <ul>
                <li>• ໄຟລ໌ ZIP ທີ່ສົ່ງອອກມີຂໍ້ມູນທີ່ລະອຽດອ່ອນ (<strong>ລະຫັດຜ່ານ, ບຸກມາກ, ລາຍເຊັນ</strong>)</li>
                <li>• ກະລຸນາເກັບຮັກສາໄວ້ຢ່າງປອດໄພ (ຕົວຢ່າງ: USB ທີ່ຖືກເຂົ້າລະຫັດ, ຕົວຈັດການລະຫັດຜ່ານ)</li>
                <li>• ຖ້າໄຟລ໌ສູນເສຍ, ລະຫັດຜ່ານ PDF ທີ່ບັນທຶກໄວ້ຈະສູນເສຍໄປຢ່າງຖາວອນ</li>
            </ul>
        </div>

        <h4>📁 ຮູບແບບການສົ່ງອອກ</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            ການຕັ້ງຄ່າຖືກບັນທຶກໄວ້ໃນໄຟລ໌ ZIP ດຽວ:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP ນີ້ປະກອບດ້ວຍ <code>settings.json</code> ຄົບຖ້ວນ (ຈາກການຕັ້ງຄ່າຂອງທ່ານ) ພ້ອມທັງໄຟລ໌ຮູບພາບລາຍເຊັນທີ່ຝັງໄວ້ ແລະລະຫັດຜ່ານທີ່ຖືກເຂົ້າລະຫັດ.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "ລາຍເຊັນ - ຄູ່ມື",
        'signature_guide_html': """
        📝 <strong>ລາຍເຊັນ - ຄູ່ມືດ່ວນ</strong><br>
        <ul>
        <li>ຕັ້ງລະຫັດຜ່ານຫຼັກ</li>
        <li>ຕັ້ງຄ່າລາຍເຊັນໃນເມນູ <em>ການຕັ້ງຄ່າ</em> (ຂະໜາດ, ປະທັບເວລາ, …)</li>
        <li>ໃສ່ດ້ວຍ <strong>ຄລິກຂວາ</strong> ໃນຕໍາແໜ່ງທີ່ຕ້ອງການ (ຕ້ອງການລະຫັດຜ່ານຫຼັກໜຶ່ງຄັ້ງຕໍ່ເຊດຊັນ)</li>
        <li>ຍ້າຍລາຍເຊັນດ້ວຍເມົາສ໌ ຫຼື ລູກກະແຈລູກສອນ</li>
        <li>ໃສ່ລາຍເຊັນຫຼາຍລາຍຕິດຕໍ່ກັນ</li>
        <li>ປັບແຕ່ງແຕ່ລະລາຍເຊັນຕາມຄວາມຕ້ອງການ</li>
        <li>ຍົກເລີກລາຍເຊັນດຽວ</li>
        <li>ບັນທຶກ / ຍົກເລີກທຸກລາຍເຊັນໃນຄັ້ງດຽວ</li>
        <li>ທາງເລືອກ, ສາມາດໃຊ້ແຖບເມນູໄດ້ເຊັ່ນກັນ.</li>
        </ul>
        """,
        'signature_guide_voice': "ຄູ່ມືດ່ວນສຳລັບລາຍເຊັນ. ຕັ້ງລະຫັດຜ່ານຫຼັກ. ຕັ້ງຄ່າລາຍເຊັນໃນການຕັ້ງຄ່າ. ໃສ່ດ້ວຍຄລິກຂວາ.",

        'image_guide_title': "ໃສ່ຮູບພາບ - ຄູ່ມື",
        'image_guide_html': """
        📷 <strong>ການໃສ່ຮູບພາບໃສ່ PDF - ຄູ່ມືດ່ວນ</strong><br>
        <ol>
        <li>ຄລິກຂວາໃສ່ຕໍາແໜ່ງທີ່ຕ້ອງການ</li>
        <li><em>„ໃສ່ຮູບພາບ“</em> → ເລືອກຮູບພາບ</li>
        <li>ກຳນົດຕຳແໜ່ງຮູບພາບ: ລາກດ້ວຍເມົາສ໌</li>
        <li>ປັບຂະໜາດ: ລາກທີ່ມຸມ/ຂອບ</li>
        <li>ຮັກສາອັດຕາສ່ວນ: ປຸ່ມ <strong>[A]</strong></li>
        <li>ການປັບແຕ່ງເພີ່ມເຕີມ: ຄລິກຂວາໃສ່ຮູບພາບ</li>
        </ol>
        <p><strong>ຄຳແນະນຳ:</strong> ໃນເມນູບໍລິບົດ, ທ່ານສາມາດປັບການຕັ້ງຄ່າໄດ້.</p>
        """,
        'image_guide_voice': "ຄູ່ມືດ່ວນສຳລັບຮູບພາບ. ຄລິກຂວາ, ໃສ່ຮູບພາບ, ເລືອກ. ກຳນົດຕຳແໜ່ງດ້ວຍເມົາສ໌, ປັບຂະໜາດທີ່ມຸມ. ອັດຕາສ່ວນດ້ວຍປຸ່ມ A.",

        'form_guide_title': "ໃສ່ຮູບຮ່າງ - ຄູ່ມື",
        'form_guide_html': """
        📐 <strong>ການໃສ່ຮູບຮ່າງໃສ່ PDF - ຄູ່ມືດ່ວນ</strong><br>
        <ol>
        <li>ເລືອກປະເພດຮູບຮ່າງ (ສີ່ແຈສາກ, ຮູບໄຂ່, ເສັ້ນ, ລູກສອນ)</li>
        <li>ຄລິກໃສ່ຕໍາແໜ່ງ:
            <ul>
            <li>ສຳລັບສີ່ແຈສາກ/ຮູບໄຂ່: ຄລິກດຽວວາງຮູບຮ່າງ</li>
            <li>ສຳລັບເສັ້ນ/ລູກສອນ: ສອງຄລິກສຳລັບຈຸດເລີ່ມ ແລະສິ້ນສຸດ</li>
            </ul>
        </li>
        <li>ກຳນົດຕຳແໜ່ງຮູບຮ່າງ: ລາກດ້ວຍເມົາສ໌</li>
        <li>ປັບຂະໜາດ: ລາກທີ່ມຸມ/ຂອບ</li>
        <li>ບັນທຶກຮູບຮ່າງ: <strong>Enter</strong></li>
        <li>ຍົກເລີກຮູບຮ່າງ: <strong>ESC</strong></li>
        <li>ການປັບແຕ່ງເພີ່ມເຕີມ: ຄລິກຂວາໃສ່ຮູບຮ່າງ</li>
        </ol>
        <p><strong>ຄຳແນະນຳ:</strong> ໃນເມນູບໍລິບົດ, ທ່ານສາມາດປັບການຕັ້ງຄ່າໄດ້.</p>
        """,
        'form_guide_voice': "ຄູ່ມືດ່ວນສຳລັບຮູບຮ່າງ. ເລືອກປະເພດຮູບຮ່າງ. ສຳລັບສີ່ແຈສາກ ຫຼື ຮູບໄຂ່ຄລິກຄັ້ງດຽວ, ສຳລັບເສັ້ນ ຫຼື ລູກສອນຄລິກສອງຄັ້ງ. ກຳນົດຕຳແໜ່ງດ້ວຍເມົາສ໌, ປັບຂະໜາດທີ່ມຸມ. ບັນທຶກດ້ວຍ Enter, ຍົກເລີກດ້ວຍ Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "ກ່ອນໜ້າ",
        "btn_next_result": "ຕໍ່ໄປ",
        "ocr_text_window": "ໜ້າຕ່າງຂໍ້ຄວາມ OCR",
        "bookmark_existing": "ບຸກມາກທີ່ມີຢູ່",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "ການປຽບທຽບ OCR Mac - Windows",
        'ocr_method_mac_win_title': "ຄວາມແຕກຕ່າງຂອງ OCR ລະຫວ່າງ Mac ແລະ Windows",
        'ocr_method_mac_win_voice': "Mac ດີກວ່າ",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – ຄວາມແຕກຕ່າງລະຫວ່າງ macOS ແລະ Windows</strong></p>

        <p><strong>macOS (ແນະນຳ)</strong></p>
        <p>ເຄື່ອງມື:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>ຜົນໄດ້ຮັບ:</p>
        <ul>
        <li>PDF ທີ່ສາມາດຄົ້ນຫາໄດ້ດ້ວຍຂໍ້ຄວາມທີ່ຝັງຢູ່ ເຊິ່ງຮັກສາເຄົ້າເດີມສ່ວນໃຫຍ່.</li>
        </ul>
        <p>ຂໍ້ດີ:</p>
        <ul>
        <li>ຄຸນນະພາບການຮັບຮູ້ຂໍ້ຄວາມທີ່ດີເລີດ (ແມ້ແຕ່ໜ້າທີ່ບິດເບືອນ).</li>
        <li>ການຮັກສາເສັ້ນສະແດງ vector ແລະຕົວອັກສອນ.</li>
        <li>ແຖບຄວາມຄືບໜ້າ GUI ຜ່ານການປະເມີນຍ່ອຍຂະບວນການ.</li>
        <li>ການຄວບຄຸມຢ່າງສົມບູນຕໍ່ພາຣາມິເຕີ OCR ທັງໝົດ (Deskew, Clean, Oversample, ການເພີ່ມປະສິດທິພາບ).</li>
        <li>ການຄົ້ນຫາຂໍ້ຄວາມສາມາດໃຊ້ໄດ້ໂດຍກົງໃນໜ້າຕ່າງຫຼັກ (ມຸມມອງ PDF).</li>
        </ul>
        <p>ຂໍ້ເສຍ:</p>
        <ul>
        <li>ຕ້ອງການເຄື່ອງມືລະບົບເພີ່ມເຕີມ (ocrmypdf, Ghostscript, unpaper, pngquant – ລວມຢູ່ໃນຊຸດແອັບ).</li>
        <li>ການຈັດການຂໍ້ຜິດພາດທີ່ສັບສົນຫຼາຍ (ການຕາຍສະຫຼັບ, ເວລາຜ່ານ).</li>
        </ul>

        <p><strong>Windows (ທາງເລືອກທີ່ໝັ້ນຄົງ)</strong></p>
        <p>ເຄື່ອງມື:</p>
        <ul>
        <li>pytesseract (ການເຊື່ອມຕໍ່ໂດຍກົງກັບ Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>ຜົນໄດ້ຮັບ:</p>
        <ul>
        <li>PDF ທີ່ສາມາດຄົ້ນຫາໄດ້ ເຊິ່ງທາງສາຍຕາກົງກັບ PDF ຮູບພາບ, ແຕ່ສາມາດຄົ້ນຫາໄດ້ຜ່ານຂໍ້ຄວາມໂປ່ງໃສ.</li>
        </ul>
        <p>ຂໍ້ດີ:</p>
        <ul>
        <li>ບໍ່ມີອັນໃດໃນໃຈຕອນນີ້.</li>
        </ul>
        <p>ຂໍ້ເສຍ:</p>
        <ul>
        <li>PDF ແມ່ນສຳຄັນຄືຮູບພາບທີ່ມີຂໍ້ຄວາມເບິ່ງບໍ່ເຫັນ; ເຄົ້າອາດຈະບ່ຽງເບນເລັກນ້ອຍສຳລັບເອກະສານທີ່ຊັບຊ້ອນ (ຖັນ, ຕາຕະລາງ).</li>
        <li>ບໍ່ມີການແກ້ໄຂຄວາມອຽງອັດຕະໂນມັດ (--deskew) ຫຼື ການທຳຄວາມສະອາດຮູບພາບ (--clean).</li>
        <li>ແຖບຄວາມຄືບໜ້າ GUI ຖືກອັບເດດພຽງແຕ່ຫຍາຍໆໂດຍອີງໃສ່ຈຳນວນໜ້າທີ່ປະມວນຜົນ.</li>
        <li>ຄວາມໄວ OCR ຊ້າກວ່າເລັກນ້ອຍ (ເນື່ອງຈາກແຕ່ລະໜ້າຖືກປະມວນຜົນແຍກຕ່າງຫາກ).</li>
        <li>ການຄົ້ນຫາຂໍ້ຄວາມຖືກປ່ຽນເສັ້ນທາງໄປຍັງໜ້າຕ່າງຂໍ້ຄວາມ OCR.</li>
        </ul>

        <p><strong>ຈຸດທີ່ຄ້າຍຄືກັນ</strong></p>
        <ul>
        <li>ທັງສອງວິທີສ້າງ PDF ທີ່ສາມາດຄົ້ນຫາໄດ້ໃນໄດເລກະທໍລີດຽວກັນກັບໄຟລ໌ຕົ້ນສະບັບ.</li>
        <li>ການຕັ້ງຄ່າ OCR (ພາສາ, DPI, ໂໝດການແບ່ງສ່ວນໜ້າ, ໂໝດເຄື່ອງຈັກ OCR) ສາມາດຕັ້ງຄ່າໄດ້ຜ່ານ OCRSettingsDialog ແລະມີຜົນໃນທັງສອງການຈັດຕັ້ງປະຕິບັດ.</li>
        </ul>

        <p><strong>ຄຳແນະນຳ:</strong></p>
        <ul>
        <li>macOS: ໄຟລ໌ຖານສອງ ocrmypdf ໃຫ້ຜົນໄດ້ຮັບທີ່ດີທີ່ສຸດ – ຊື້ Mac ແລະໃຊ້ຮຸ່ນ (PDFDarkView ສຳລັບ Mac ທີ່ມີຊິບ Apple Silicon ຫຼື Intel). ຜົນໄດ້ຮັບ OCR ດີກວ່າຢູ່ Windows!</li>
        <li>Windows: ໃຊ້ວິທີແກ້ໄຂ pytesseract. ມັນໝັ້ນຄົງ ແລະໃຫ້ຄຸນນະພາບທີ່ພຽງພໍສຳລັບເອກະສານສ່ວນໃຫຍ່.</li>
        </ul>

        <p><strong>ຂໍ້ສັງເກດສຳຄັນ:</strong></p>
        <ul>
        <li>ທັງສອງຮຸ່ນຖືກລວມເຂົ້າກັນຢ່າງສົມບູນໃນສ່ວນຕິດຕໍ່ຜູ້ໃຊ້ – ຜູ້ໃຊ້ບໍ່ສັງເກດເຫັນຄວາມແຕກຕ່າງ.</li>
        <li>ໂປຣແກຣມຕັດສິນໃຈໂດຍອັດຕະໂນມັດວ່າຈະໃຊ້ເຄື່ອງຈັກ OCR ໃດໂດຍອີງໃສ່ລະບົບປະຕິບັດການ.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "ສ້າງລາຍເຊັນ (ຈາກການສະແກນ)",
        "signature_create_title": "ເລືອກລາຍເຊັນທີ່ສະແກນ (PDF/ຮູບພາບ)",
        "image_pdf_filter": "ຮູບພາບ ແລະ PDF",
        "signature_pdf_empty": "PDF ບໍ່ມີໜ້າ.",
        "signature_created_success": "ສ້າງລາຍເຊັນສຳເລັດ: {0}",
        "signature_create_error": "ຂໍ້ຜິດພາດໃນການສ້າງລາຍເຊັນ:\n{0}",
        "rembg_missing": "ບໍ່ມີການຕິດຕັ້ງ rembg.\nກະລຸນາຕິດຕັ້ງ: pip install rembg\nຂໍ້ຜິດພາດ: {0}",
        "signature_name_title": "ຊື່ໄຟລ໌ສຳລັບລາຍເຊັນ",
        "signature_name_message": "ກະລຸນາໃສ່ຊື່ໄຟລ໌ສຳລັບລາຍເຊັນໃໝ່ (ຈະຖືກບັນທຶກເປັນ PNG ທີ່ມີພື້ນຫຼັງໂປ່ງໃສ):",
        "signature_name_label": "ຊື່ໄຟລ໌:",
        "signature_name_voice": "ໃສ່ຊື່ໄຟລ໌ສຳລັບລາຍເຊັນ",
        "signature_processing": "ກຳລັງດຳເນີນການ...",
        "signature_creation_title": "ກຳລັງສ້າງລາຍເຊັນ",
        "signature_overwrite_warning": "ໄຟລ໌ '{0}' ມີຢູ່ແລ້ວ. ຂຽນທັບ?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"ກຽມ PDF ສຳລັບລາຍເຊັນ",
        "signature_prepare_instruction":"ກະລຸນາເລືອກ PDF ທີ່ມີລາຍເຊັນທີ່ສະແກນຢູ່ໃນໜ້າດຽວ.\n\nການຮັບຮູ້ທີ່ດີທີ່ສຸດຈະບັນລຸໄດ້ຫາກ:\n• ລາຍເຊັນຂຽນດ້ວຍຫມຶກດຳ (ປາກກາລູກກົມ ຫຼື ປາກກາປາຍແຫຼມ) ໃສ່ເຈ້ຍຂາວ.\n• ລາຍເຊັນຢູ່ໃນສ່ວນເທິງສາມສ່ວນຂອງໜ້າ A4 ທີ່ຫວ່າງ.\n• PDF ຖືກສະແກນດ້ວຍຄວາມລະອຽດຢ່າງໜ້ອຍ 300 dpi.\n• ລາຍເຊັນຊັດເຈນ ແລະບໍ່ບາງເກີນໄປ.\n• ບໍ່ມີຮູບແບບພື້ນຫຼັງ ຫຼື ເສັ້ນທີ່ລົບກວນ.",
        "signature_prepare_voice":"ກະລຸນາເລືອກ PDF ທີ່ມີລາຍເຊັນທີ່ສະແກນ. ໃສ່ໃຈໃສ່ຄຸນນະພາບດີ ແລະຄວາມຄົມຊັດ.",
        "sig_thickness_label":"ຄວາມໜາຂອງເສັ້ນ:",
        "sig_thickness_normal":"ປົກກະຕິ (ບາງ)",
        "sig_thickness_bold":"ໜາ (ແນະນຳ)",
        "sig_thickness_very_bold":"ໜາຫຼາຍ",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "ເພີ່ມພາສາ GUI ແລະ OCR - ຄູ່ມື",
        'language_guide_title': "ເພີ່ມພາສາ GUI ແລະ OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>ດາວໂຫຼດໄຟລ໌ແປພາສາທີ່ຕ້ອງການ <code>translations_xy.py</code> ຈາກ<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        ແລະວາງໄວ້ໃນໄດເລກະທໍລີຕໍ່ໄປນີ້:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>ເປີດຕົວທ່ອງເວັບຂອງທ່ານ.</li>
        <li>ໄປທີ່: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>ຊອກຫາທີ່ຂອບຂວາຂອງໜ້າຈໍສຳລັບ "Releases" ແລະເລືອກອັນທີ່ມີເຄື່ອງໝາຍ <strong>"latest"</strong>.</li>
        <li>ໃນໜ້າ Release ຕໍ່ໄປ, ດາວໂຫຼດໄຟລ໌ <code>Source Code.zip</code> ທາງລຸ່ມສຸດ.</li>
        <li>ແກ້ໄຂໄຟລ໌ ZIP.</li>
        <li>ຊອກຫາໃນໂຟນເດີທີ່ແກ້ໄຂແລ້ວທຸກໄຟລ໌ພາສາທີ່ທ່ານຕ້ອງການ, ແລະສຳເນົາພວກມັນໄປໃສ່ໄດເລກະທໍລີ:<br/>
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
        "menu_watermark":"ໃສ່ເຄື່ອງໝາຍນ້ຳ",
        "fullpage_text_watermark_title":"ຂໍ້ຄວາມເປັນເຄື່ອງໝາຍນ້ຳ",
        "fullpage_image_watermark_title":"ຮູບພາບເປັນເຄື່ອງໝາຍນ້ຳ",
        "filename_with_watermark":"_ມີເຄື່ອງໝາຍນ້ຳ",
        "watermark_text":"ຂໍ້ຄວາມ:",
        "watermark_text_placeholder":"ຂໍ້ຄວາມເຄື່ອງໝາຍນ້ຳຂອງທ່ານ...",
        "watermark_font_family":"ຟອນ:",
        "watermark_font_size":"ຂະໜາດຟອນ:",
        "watermark_format":"ການຈັດຮູບແບບ:",
        "watermark_bold":"ໜາ",
        "watermark_italic":"ອຽງ",
        "watermark_color":"ສີ:",
        "watermark_choose_color":"ເລືອກສີ...",
        "watermark_opacity":"ຄວາມທຶບ / ຄວາມໂປ່ງໃສ:",
        "watermark_direction":"ທິດທາງການອ່ານ:",
        "watermark_direction_l_r":"ຊ້າຍ → ຂວາ",
        "watermark_direction_bl_tr":"ລຸ່ມຊ້າຍ → ເທິງຂວາ",
        "watermark_direction_tl_br":"ເທິງຊ້າຍ → ລຸ່ມ",
        "watermark_direction_b_t":"ລຸ່ມ → ເທິງ",
        "watermark_direction_t_b":"ເທິງ → ລຸ່ມ",
        "watermark_preview":"ການເບິ່ງຕົວຢ່າງ:",
        "watermark_preview_sample":"ຂໍ້ຄວາມຕົວຢ່າງ",
        "watermark_empty_text":"ກະລຸນາໃສ່ຂໍ້ຄວາມ.",
        "watermark_applied":"ໄດ້ນຳໃຊ້ເຄື່ອງໝາຍນ້ຳໃສ່ທຸກໜ້າ.",
        "watermark_saved":"ບັນທຶກເຄື່ອງໝາຍນ້ຳແລ້ວ.",
        "image_scale":"ຂະໜາດ:",
        "image_preview":"ການເບິ່ງຕົວຢ່າງຮູບພາບ:",
        "no_image_selected":"ຍັງບໍ່ໄດ້ເລືອກຮູບພາບ",
        "browse":"ຊອກຫາ...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "ການລຶບຂໍ້ມູນ",
        "redact_add_black":"ການລຶບຂໍ້ມູນ (ດຳ)",
        "redact_add_white":"ການລຶບຂໍ້ມູນ (ຂາວ / ລຶບ)",
        "redact_added_black":"ເພີ່ມການລຶບຂໍ້ມູນສີດຳແລ້ວ",
        "redact_added_white":"ເພີ່ມການລຶບຂໍ້ມູນສີຂາວແລ້ວ",
        "redact_apply_all":"ນຳໃຊ້ການລຶບຂໍ້ມູນທັງໝົດ ແລະ ບັນທຶກ",
        "redact_discard_all":"ຍົກເລີກການລຶບຂໍ້ມູນທັງໝົດ",
        "redact_discard":"ຍົກເລີກການລຶບຂໍ້ມູນນີ້",
        "no_redactions":"ບໍ່ມີການລຶບຂໍ້ມູນ",
        "redact_confirm_title":"ນຳໃຊ້ການລຶບຂໍ້ມູນແບບຖາວອນ",
        "redact_confirm_message":"ຄຳເຕືອນ: ພື້ນທີ່ທີ່ໝາຍໄວ້ຈະຖືກລຶບຖາວອນ (ດຳ ຫຼື ຂາວ).\nຈະສ້າງສຳຮອງ (ຖ້າເປີດໃຊ້).\n\nສືບຕໍ່?",
        "redact_apply":"ແມ່ນ, ລຶບຂໍ້ມູນດຽວນີ້",
        "redact_saved":"ນຳໃຊ້ ແລະ ບັນທຶກ {0} ການລຶບຂໍ້ມູນສຳເລັດ.",
        "redact_saved_voice":"ນຳໃຊ້ {0} ການລຶບຂໍ້ມູນ",
        "redact_error":"ຂໍ້ຜິດພາດໃນລະຫວ່າງການລຶບຂໍ້ມູນ",
        "filename_redacted":"_ຖືກລຶບຂໍ້ມູນ",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'ໃສ່ເລກໜ້າ',
        'page_numbers_format': 'ຮູບແບບເລກ:',
        'page_numbers_format_arabic': '1, 2, 3 ... (ອາຣັບ)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (ໂລມັນນ້ອຍ)',
        'page_numbers_format_roman_upper': 'I, II, III ... (ໂລມັນໃຫຍ່)',
        'page_numbers_format_letter': 'A, B, C ... (ຕົວອັກສອນ)',
        'page_numbers_format_custom': 'ປັບແຕ່ງ',
        'page_numbers_custom_pattern': 'ຮູບແບບ:',
        'page_numbers_custom_placeholder': 'ຕົວຢ່າງ "ໜ້າ {nummer}" ຫຼື "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'ໃຊ້ {nummer} ສຳລັບເລກໜ້າປັດຈຸບັນ ແລະ {total} ສຳລັບຈຳນວນທັງໝົດ',
        'page_numbers_position': 'ຕຳແໜ່ງ:',
        'page_numbers_pos_tl': 'ເທິງຊ້າຍ',
        'page_numbers_pos_tc': 'ເທິງກາງ',
        'page_numbers_pos_tr': 'ເທິງຂວາ',
        'page_numbers_pos_ml': 'ກາງຊ້າຍ',
        'page_numbers_pos_mc': 'ກາງ',
        'page_numbers_pos_mr': 'ກາງຂວາ',
        'page_numbers_pos_bl': 'ລຸ່ມຊ້າຍ',
        'page_numbers_pos_bc': 'ລຸ່ມກາງ',
        'page_numbers_pos_br': 'ລຸ່ມຂວາ',
        'page_numbers_margins': 'ຂອບ:',
        'page_numbers_margin_x': 'ໄລຍະຫ່າງແນວນອນ:',
        'page_numbers_margin_y': 'ໄລຍະຫ່າງແນວຕັ້ງ:',
        'page_numbers_range': 'ຂອບເຂດໜ້າ:',
        'page_numbers_all_pages': 'ທຸກໜ້າ',
        'page_numbers_custom_range': 'ຂອບເຂດປັບແຕ່ງ',
        'page_numbers_from': 'ຈາກ:',
        'page_numbers_to': 'ຫາ:',
        'page_numbers_progress': 'ກຳລັງໃສ່ເລກໜ້າ...',
        'page_numbers_start': 'ເລີ່ມໃສ່ເລກໜ້າ...',
        'page_numbers_cancel': 'ຍົກເລີກການໃສ່ເລກໜ້າ',
        'page_numbers_success': 'ເພີ່ມເລກໜ້າສຳເລັດ.\n\nທ່ານຕ້ອງການເປີດ PDF ໃໝ່ບໍ?\n\n{0}',
        'page_numbers_complete': 'ເພີ່ມເລກໜ້າແລ້ວ',
        'page_numbers_error_format': 'ຂໍ້ຜິດພາດໃນການໃສ່ເລກໜ້າ: {0}',
        'page_numbers_content_type': 'ປະເພດເນື້ອຫາ:',
        'page_numbers_tab_simple': 'ເລກງ່າຍ',
        'page_numbers_tab_range': 'ໜ້າ X ຂອງ Y',
        'page_numbers_tab_date': 'ວັນທີ',
        'page_numbers_tab_custom': 'ຂໍ້ຄວາມອິດສະຫຼະ',
        'page_numbers_range_format': 'ຮູບແບບ:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'ໜ້າ {aktuell} ຂອງ {gesamt}',
        'page_numbers_range_custom': 'ປັບແຕ່ງ',
        'page_numbers_range_placeholder': 'ຕົວຢ່າງ "ໜ້າ {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'ຮູບແບບວັນທີ:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 ມັງກອນ 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'ປັບແຕ່ງ',
        'page_numbers_date_placeholder': 'ຕົວຢ່າງ %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'ຕຳແໜ່ງ:',
        'page_numbers_date_before': 'ວັນທີກ່ອນເລກໜ້າ',
        'page_numbers_date_after': 'ວັນທີຫຼັງເລກໜ້າ',
        'page_numbers_date_only': 'ສະເພາະວັນທີ (ບໍ່ມີເລກໜ້າ)',
        'page_numbers_custom_text': 'ຂໍ້ຄວາມປັບແຕ່ງ:',
        'page_numbers_custom_placeholder_text': 'ໃຊ້ {seite} ສຳລັບເລກໜ້າ ແລະ {gesamt} ສຳລັບຈຳນວນທັງໝົດ\nຕົວຢ່າງ "ລັບ - ໜ້າ {seite}" ຫຼື "{seite} ຂອງ {gesamt}"',
        "filename_with_page_number":"_ມີເລກໜ້າ",
        "filename_with_page_declaration":"_ມີຄຳປະກາດໜ້າ",
        "filename_with_pagenumber":"_ມີເລກໜ້າ",
        "filename_with_date":"_ມີວັນທີ",
        "filename_with_my_page_declaration":"_ມີຄຳປະກາດໜ້າປັບແຕ່ງ",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "ການປ່ຽນແປງທີ່ຍັງບໍ່ໄດ້ບັນທຶກ",
        "unsaved_changes_message_darkmode": "ມີການໃສ່ທີ່ຍັງບໍ່ໄດ້ບັນທຶກ.\nທ່ານຕ້ອງການບັນທຶກພວກມັນກ່ອນປ່ຽນບໍ?",
        "save_and_switch": "ບັນທຶກ ແລະ ປ່ຽນ",
        "discard_and_switch": "ປ່ຽນດຽວນີ້",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'ສົ່ງອອກໜ້າເປັນຮູບພາບ',
        'export_images_menu': 'ສົ່ງອອກເປັນຮູບພາບ (PNG/JPEG)',
        'export_images_format': 'ຮູບແບບຮູບພາບ:',
        'export_images_dpi': 'ຄວາມລະອຽດ (DPI):',
        'export_images_quality': 'ຄຸນນະພາບ JPEG:',
        'export_images_range': 'ຂອບເຂດໜ້າ:',
        'export_images_all_pages': 'ທຸກໜ້າ',
        'export_images_custom_range': 'ຂອບເຂດປັບແຕ່ງ',
        'export_images_from': 'ຈາກ:',
        'export_images_to': 'ຫາ:',
        'export_images_options': 'ຕົວເລືອກ:',
        'export_images_single_files': 'ແຕ່ລະໜ້າເປັນໄຟລ໌ແຍກ',
        'export_images_subfolder': 'ສົ່ງອອກໄປໂຟນເດີຍ່ອຍ',
        'export_images_subfolder_info': 'ໄປໂຟນເດີຍ່ອຍ "ຊື່PDF_ຮູບພາບ"',
        'export_images_same_folder': 'ໃນໂຟນເດີດຽວກັບ PDF',
        'export_images_apply_darkmode': 'ນຳໃຊ້ການຕັ້ງຄ່າ PDFDarkView (ໂໝດມືດ)',
        'export_images_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'export_images_browse': 'ຊອກຫາ...',
        'export_images_preview': 'ການເບິ່ງຕົວຢ່າງ:',
        'export_images_preview_info': 'ເລືອກການຕັ້ງຄ່າສຳລັບການສົ່ງອອກ',
        'export_images_preview_info_detail': '{0} ໜ້າເປັນ {1}\nຄວາມລະອຽດ: {2} DPI\nຊື່ໄຟລ໌: {3}\n{4}',
        'export_images_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'export_images_start': 'ເລີ່ມສົ່ງອອກຮູບພາບ...',
        'export_images_progress': 'ກຳລັງສົ່ງອອກຮູບພາບ...',
        'export_images_saving': 'ກຳລັງບັນທຶກໜ້າ {0} ຂອງ {1}...',
        'export_images_success': 'ການສົ່ງອອກສຳເລັດ!\n\nບັນທຶກຮູບພາບ {0} ໄວ້ທີ່:\n{1}',
        'export_images_complete': 'ການສົ່ງອອກຮູບພາບສຳເລັດ',
        'export_images_open_folder': '📁 ເປີດໂຟນເດີ',
        'export_images_cancel': 'ຍົກເລີກການສົ່ງອອກຮູບພາບ',
        'export_images_error_format': 'ຂໍ້ຜິດພາດໃນການສົ່ງອອກຮູບພາບ: {0}',
        'export_images_pdf2image_missing': 'ຫໍສະໝຸດ "pdf2image" ຍັງບໍ່ໄດ້ຕິດຕັ້ງ.\n\nກະລຸນາຕິດຕັ້ງມັນດ້ວຍ:\npip install pdf2image\n\nສຳລັບ Windows ທ່ານຍັງຕ້ອງການ Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'ການແປງ PDF/A ສຳລັບການເກັບຮັກສາໄລຍະຍາວ',
        'pdfa_menu': 'ການແປງ PDF/A (ເໝາະສຳລັບການເກັບຮັກສາ)',
        'pdfa_info': 'ແປງ PDF ເປັນຮູບແບບ PDF/A.\n\nPDF/A ຖືກອອກແບບສະເພາະສຳລັບການເກັບຮັກສາໄລຍະຍາວ ແລະ ຮັບປະກັນວ່າເອກະສານຈະຖືກສະແດງຢ່າງຖືກຕ້ອງໃນອະນາຄົດ.',
        'pdfa_standard': 'ມາດຕະຖານ PDF/A:',
        'pdfa_standard_select': 'ຮຸ່ນ:',
        'pdfa_1': 'PDF/A-1 (ງ່າຍ, ເຂົ້າກັນໄດ້ກວ້າງ)',
        'pdfa_2': 'PDF/A-2 (ທັນສະໄໝ, ການບີບອັດດີກວ່າ)',
        'pdfa_3': 'PDF/A-3 (ຮຸ່ນຫຼ້າສຸດ, ອະນຸຍາດໃຫ້ໄຟລ໌ແນບ)',
        'pdfa_standards_explanation': '📖 ຄຳອະທິບາຍມາດຕະຖານ:\n\n'
            '• PDF/A-1: ພື້ນຖານ, ເຂົ້າກັນໄດ້ກັບລະບົບເກົ່າ (ປະມານ 2005)\n'
            '• PDF/A-2: ທັນສະໄໝກວ່າ, ການບີບອັດດີກວ່າ, ຮອງຮັບຄວາມໂປ່ງໃສ (ປະມານ 2011)\n'
            '• PDF/A-3: ຮຸ່ນຫຼ້າສຸດ, ອະນຸຍາດໃຫ້ຝັງໄຟລ໌ແນບ (ປະມານ 2013)\n\n'
            'ຄຳແນະນຳ: PDF/A-2 ເປັນການປະນີປະນອມທີ່ດີລະຫວ່າງຄວາມເຂົ້າກັນໄດ້ ແລະ ຄຸນສົມບັດທັນສະໄໝ.',
        'pdfa_options': 'ຕົວເລືອກ:',
        'pdfa_compress_enable': 'ບີບອັດ PDF (ໄຟລ໌ນ້ອຍກວ່າ)',
        'pdfa_metadata_preserve': 'ຮັກສາເມຕາເດຕາ (ຫົວຂໍ້, ຜູ້ຂຽນ, ແລະອື່ນໆ)',
        'pdfa_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'pdfa_browse': 'ຊອກຫາ...',
        'pdfa_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'pdfa_ocr_info_unknown': '🔍 ບໍ່ສາມາດກວດສອບເນື້ອໃນຂໍ້ຄວາມ.',
        'pdfa_ocr_info_not_needed': '✅ ມີຂໍ້ຄວາມ - ບໍ່ຕ້ອງການ OCR.\nສາມາດສ້າງ PDF/A ໄດ້ໂດຍກົງ.',
        'pdfa_ocr_info_recommended': '⚠️ ບໍ່ພົບຂໍ້ຄວາມພຽງພໍ.\n\nສຳລັບ PDF ທີ່ສາມາດຄົ້ນຫາໄດ້ ພວກເຮົາແນະນຳໃຫ້ແລ່ນ OCR ກ່ອນ.\nຫມາຍເຫດ: PDF/A ເຮັດວຽກໄດ້ໂດຍບໍ່ມີ OCR - ແຕ່ຂໍ້ຄວາມຈະບໍ່ສາມາດຄົ້ນຫາໄດ້.',
        'pdfa_ocr_info_error': '❌ ຂໍ້ຜິດພາດໃນການກວດສອບ: {0}',
        'pdfa_start': 'ເລີ່ມການແປງ PDF/A...',
        'pdfa_progress': 'ກຳລັງແປງ PDF/A...',
        'pdfa_success': 'ການແປງ PDF/A ສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nທ່ານຕ້ອງການເປີດ PDF ໃໝ່ບໍ?',
        'pdfa_complete': 'ການແປງ PDF/A ສຳເລັດ',
        'pdfa_cancel': 'ຍົກເລີກການແປງ PDF/A',
        'pdfa_error_format': 'ຂໍ້ຜິດພາດໃນການແປງ PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'ຫໍສະໝຸດ "ocrmypdf" ຍັງບໍ່ໄດ້ຕິດຕັ້ງ.\n\nກະລຸນາຕິດຕັ້ງມັນດ້ວຍ:\npip install ocrmypdf',
        'btn_convert': 'ແປງ',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'ເພີ່ມປະສິດທິພາບ PDF (ຫຼຸດຂະໜາດໄຟລ໌)',
        'optimize_menu': 'ເພີ່ມປະສິດທິພາບ PDF (ຂະໜາດໄຟລ໌)',
        'optimize_info': 'ຫຼຸດຂະໜາດໄຟລ໌ PDF ໂດຍຜ່ານວິທີການເພີ່ມປະສິດທິພາບຕ່າງໆ.\n\nລະດັບການບີບອັດສູງຂຶ້ນ, ໄຟລ໌ຈະນ້ອຍລົງ - ໂດຍມີການສູນເສຍຄຸນນະພາບທີ່ອາດຈະເກີດຂຶ້ນໃນຮູບພາບ.',
        'optimize_level': 'ລະດັບການບີບອັດ:',
        'optimize_level_low': 'ຕ່ຳ (ໄວ, ປະຢັດເລັກນ້ອຍ)',
        'optimize_level_medium': 'ກາງ (ການປະນີປະນອມທີ່ດີ)',
        'optimize_level_high': 'ສູງ (ປະຢັດຫຼາຍ)',
        'optimize_level_maximum': 'ສູງສຸດ (ປະຢັດສູງສຸດ, ຊ້າ)',
        'optimize_level_explanation': 'ຄຳແນະນຳ: "ກາງ" ເປັນການປະນີປະນອມທີ່ດີລະຫວ່າງຄວາມໄວ ແລະ ຂະໜາດໄຟລ໌.',
        'optimize_options': 'ຕົວເລືອກ:',
        'optimize_compress_images': 'ບີບອັດຮູບພາບ (ຫຼຸດຄຸນນະພາບ JPEG)',
        'optimize_clean_objects': 'ເອົາວັດຖຸທີ່ບໍ່ໄດ້ໃຊ້ອອກ',
        'optimize_preserve_metadata': 'ຮັກສາເມຕາເດຕາ (ຫົວຂໍ້, ຜູ້ຂຽນ, ແລະອື່ນໆ)',
        'optimize_image_quality': 'ຄຸນນະພາບຮູບພາບ:',
        'optimize_range': 'ຂອບເຂດໜ້າ:',
        'optimize_all_pages': 'ທຸກໜ້າ',
        'optimize_custom_range': 'ຂອບເຂດປັບແຕ່ງ',
        'optimize_from': 'ຈາກ:',
        'optimize_to': 'ຫາ:',
        'optimize_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'optimize_browse': 'ຊອກຫາ...',
        'optimize_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'optimize_info_box': 'ຂໍ້ມູນ',
        'optimize_info_text': 'ການເພີ່ມປະສິດທິພາບອາດໃຊ້ເວລາຫຼາຍນາທີສຳລັບ PDF ໃຫຍ່.\n\nຮູບພາບຖືກບັນທຶກດ້ວຍຄຸນນະພາບທີ່ຫຼຸດລົງ, ເຊິ່ງສາມາດຫຼຸດຂະໜາດໄຟລ໌ຢ່າງຫຼວງຫຼາຍ.',
        'optimize_start': 'ເລີ່ມເພີ່ມປະສິດທິພາບ PDF...',
        'optimize_progress': 'ກຳລັງເພີ່ມປະສິດທິພາບ PDF...',
        'optimize_cancel': 'ຍົກເລີກການເພີ່ມປະສິດທິພາບ PDF',
        'optimize_complete': 'ການເພີ່ມປະສິດທິພາບ PDF ສຳເລັດ',
        'optimize_error_format': 'ຂໍ້ຜິດພາດໃນການເພີ່ມປະສິດທິພາບ PDF:\n\n{0}',
        'optimize_success_message': 'ການເພີ່ມປະສິດທິພາບ PDF ສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nກ່ອນ: {1}\nຫຼັງ: {2}\nປະຢັດ: {3:.1f}%\n\n{4}\n\nທ່ານຕ້ອງການເປີດ PDF ທີ່ເພີ່ມປະສິດທິພາບບໍ?',
        'optimize_success_message_no_size': 'ການເພີ່ມປະສິດທິພາບ PDF ສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nບໍ່ມີຂໍ້ມູນຂະໜາດ.\n\nທ່ານຕ້ອງການເປີດ PDF ທີ່ເພີ່ມປະສິດທິພາບບໍ?',
        'optimize_result_positive': 'ໄຟລ໌ຖືກຫຼຸດ {0:.1f}%.',
        'optimize_result_zero': 'ບໍ່ມີການປ່ຽນແປງຂະໜາດໄຟລ໌.',
        'optimize_result_negative': 'ໄຟລ໌ເພີ່ມຂຶ້ນ {0:.1f}%.\nຂ້າມການເພີ່ມປະສິດທິພາບ, ຮັກສາໄຟລ໌ຕົ້ນສະບັບໄວ້.',
        'btn_optimize': 'ເລີ່ມເພີ່ມປະສິດທິພາບ',
        'filename_optimize_low_suffix': '_ເພີ່ມປະສິດທິພາບ_ຕ່ຳ',
        'filename_optimize_medium_suffix': '_ເພີ່ມປະສິດທິພາບ',
        'filename_optimize_high_suffix': '_ເພີ່ມປະສິດທິພາບ_ສູງ',
        'filename_optimize_maximum_suffix': '_ເພີ່ມປະສິດທິພາບ_ສູງສຸດ',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'ຕັດ PDF',
        'crop_menu': 'ຕັດ PDF (Crop)',
        'crop_range': 'ນຳໃຊ້ກັບ:',
        'crop_all_pages': 'ທຸກໜ້າ',
        'crop_current_page': 'ສະເພາະໜ້າປັດຈຸບັນ',
        'crop_values': 'ຄ່າການຕັດ (ເປັນຈຸດ):',
        'crop_left': 'ຊ້າຍ:',
        'crop_right': 'ຂວາ:',
        'crop_top': 'ເທິງ:',
        'crop_bottom': 'ລຸ່ມ:',
        'crop_presets': 'ກຳນົດລ່ວງໜ້າ:',
        'crop_preset_white': 'ກວດຫາຂອບຂາວ',
        'crop_reset': 'ຣີເຊັດ',
        'crop_mouse_hint': '🖱️ ລາກຮູບສີ່ແຈສາກເພື່ອເລືອກພື້ນທີ່ໂດຍປະມານ.\nຫຼັງຈາກນັ້ນ ທ່ານສາມາດປັບຄ່າໃນ SpinBoxes ໄດ້ຢ່າງແນ່ນອນ.\nການປັບດ້ວຍມືໂດຍໃຊ້ເມົາສ໌ບໍ່ສາມາດເຮັດໄດ້.',
        'crop_apply': 'ຕັດ',
        'crop_scope_all': 'ທຸກໜ້າ',
        'crop_scope_current': 'ໜ້າປັດຈຸບັນ',
        'crop_new_size': 'ຂະໜາດໃໝ່: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'ບໍ່ມີ PDF ທີ່ໂຫຼດ',
        'crop_preview_error': 'ຂໍ້ຜິດພາດໃນການໂຫຼດຕົວຢ່າງ',
        'crop_start': 'ເລີ່ມຕັດ...',
        'crop_progress': 'ກຳລັງຕັດ PDF...',
        'crop_success': 'ຕັດ PDF ສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nທ່ານຕ້ອງການເປີດ PDF ທີ່ຕັດແລ້ວບໍ?',
        'crop_complete': 'ການຕັດສຳເລັດ',
        'crop_cancel': 'ຍົກເລີກການຕັດ',
        'crop_error_format': 'ຂໍ້ຜິດພາດໃນການຕັດ:\n\n{0}',
        'filename_crop_suffix': '_ຕັດແລ້ວ',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'ເຮັດໃຫ້ PDF ຮາບ (Flatten)',
        'flatten_menu': 'ເຮັດໃຫ້ PDF ຮາບ (Flatten)',
        'flatten_info': 'ການເຮັດໃຫ້ PDF ຮາບ "ເຜົາ" ອົງປະກອບທີ່ສາມາດແກ້ໄຂໄດ້ທັງໝົດເຂົ້າໄປໃນເນື້ອໃນໜ້າ.\n\nຫຼັງຈາກນັ້ນ, ຊ່ອງຟອມ, ຄຳອະທິບາຍ, ຂໍ້ຄວາມ, ໄມ້ກາງແຂນ, ລາຍເຊັນ, ຮູບພາບ ແລະ ຮູບຮ່າງບໍ່ສາມາດແກ້ໄຂແຕ່ລະອັນໄດ້ອີກຕໍ່ໄປ.',
        'flatten_explanation_title': '📖 ນີ້ໃຊ້ສຳລັບຫຍັງ?',
        'flatten_explanation_text': 'ການເຮັດໃຫ້ຮາບແມ່ນຈຳເປັນໃນສະຖານະການດັ່ງຕໍ່ໄປນີ້:\n\n'
            '• 📄 ທ່ານຕ້ອງການກຽມເອກະສານສຳລັບພິມ\n'
            '• 🔒 ທ່ານຕ້ອງການປ້ອງກັນບໍ່ໃຫ້ໃຜປ່ຽນຊ່ອງຟອມ\n'
            '• 📎 ທ່ານຕ້ອງການ "ຝັງ" ຄຳອະທິບາຍ ແລະ ຄຳເຫັນໄວ້ຢ່າງຖາວອນໃນເອກະສານ\n'
            '• 🖼️ ທ່ານຕ້ອງການຝັງຂໍ້ຄວາມ, ໄມ້ກາງແຂນ, ລາຍເຊັນ, ຮູບພາບ ແລະ ຮູບຮ່າງໄວ້ຢ່າງຖາວອນໃນເອກະສານ\n'
            '• 📦 ທ່ານຕ້ອງການກຽມໄຟລ໌ສຳລັບການເກັບຮັກສາ\n\n'
            'ການເຮັດໃຫ້ຮາບເຮັດໃຫ້ PDF ນ້ອຍລົງ ແລະ ປ້ອງກັນການຍ້າຍ ຫຼື ລຶບອົງປະກອບໂດຍບັງເອີນ.',
        'flatten_what_title': 'ຫຍັງຖືກເຮັດໃຫ້ຮາບ?',
        'flatten_what_list': '• ✅ ຊ່ອງຟອມ (ຊ່ອງຂໍ້ຄວາມ, ກ່ອງໝາຍ, ປຸ່ມ)\n'
            '• ✅ ຄຳອະທິບາຍ (ຄຳເຫັນ, ການເນັ້ນ, ບັນທຶກ)\n'
            '• ✅ ຊັ້ນຊ້ອນ (ຂໍ້ຄວາມ, ໄມ້ກາງແຂນ, ລາຍເຊັນ, ຮູບພາບ, ຮູບຮ່າງ)',
        'flatten_options': 'ຕົວເລືອກ:',
        'flatten_forms': 'ເຮັດໃຫ້ຊ່ອງຟອມຮາບ',
        'flatten_annotations': 'ເຮັດໃຫ້ຄຳອະທິບາຍຮາບ',
        'flatten_overlays': 'ເຮັດໃຫ້ຊັ້ນຊ້ອນຮາບ (ຂໍ້ຄວາມ, ໄມ້ກາງແຂນ, ລາຍເຊັນ, ຮູບພາບ, ຮູບຮ່າງ)',
        'flatten_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'flatten_browse': 'ຊອກຫາ...',
        'flatten_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'flatten_warning': '⚠️ ສຳຄັນ: ການເຮັດໃຫ້ຮາບແມ່ນຂະບວນການທີ່ບໍ່ສາມາດກັບຄືນໄດ້!\n\nຫຼັງຈາກເຮັດໃຫ້ຮາບ, ອົງປະກອບທີ່ສາມາດແກ້ໄຂໄດ້ບໍ່ສາມາດປ່ຽນ ຫຼື ລຶບແຕ່ລະອັນໄດ້ອີກຕໍ່ໄປ.\nສ້າງສຳຮອງໄວ້ກ່ອນຖ້າຈຳເປັນ.',
        'flatten_apply': 'ເຮັດໃຫ້ຮາບ',
        'flatten_start': 'ເລີ່ມເຮັດໃຫ້ຮາບ...',
        'flatten_progress': 'ກຳລັງເຮັດໃຫ້ PDF ຮາບ...',
        'flatten_success': 'ເຮັດໃຫ້ PDF ຮາບສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nທ່ານຕ້ອງການເປີດ PDF ທີ່ເຮັດໃຫ້ຮາບແລ້ວບໍ?',
        'flatten_complete': 'ການເຮັດໃຫ້ຮາບສຳເລັດ',
        'flatten_cancel': 'ຍົກເລີກການເຮັດໃຫ້ຮາບ',
        'flatten_error_format': 'ຂໍ້ຜິດພາດໃນການເຮັດໃຫ້ຮາບ:\n\n{0}',
        'filename_flatten_suffix': '_ເຮັດໃຫ້ຮາບ',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'ການຊ້ອນ PDF (Overlay)',
        'overlay_menu': 'ການຊ້ອນ PDF (Overlay)',
        'overlay_info': 'ວາງ PDF ໜຶ່ງ (ຊັ້ນຊ້ອນ) ໃສ່ເທິງ PDF ອື່ນ.\n\nPDF ຊັ້ນຊ້ອນຖືກວາງໃສ່ PDF ພື້ນຖານ. ນີ້ມີປະໂຫຍດສຳລັບເຄື່ອງໝາຍນ້ຳ, ໂລໂກ້, ຫົວຈົດໝາຍ ຫຼື ຕາຫຼັງ.',
        'overlay_explanation_title': '📖 ນີ້ໃຊ້ສຳລັບຫຍັງ?',
        'overlay_explanation_text': 'ການຊ້ອນແມ່ນຈຳເປັນໃນສະຖານະການດັ່ງຕໍ່ໄປນີ້:\n\n'
            '• 🏢 ວາງໂລໂກ້ບໍລິສັດເປັນເຄື່ອງໝາຍນ້ຳໃສ່ທຸກໜ້າ\n'
            '• 📄 ວາງຫົວຈົດໝາຍໃສ່ PDF ຫວ່າງ\n'
            '• 🖊️ ວາງຊັ້ນຊ້ອນຕາຫຼັງໃສ່ເອກະສານ\n'
            '• 🔖 ວາງເຄື່ອງໝາຍນ້ຳໃສ່ທຸກໜ້າ\n'
            '• 📑 ວາງຊັ້ນຊ້ອນຟອມໃສ່ແມ່ແບບ',
        'overlay_type': 'ປະເພດການຊ້ອນ:',
        'overlay_type_fullpage': 'ເຕັມໜ້າ (ປົກ)',
        'overlay_type_transparent': 'ເຕັມໜ້າ (ໂປ່ງໃສ - ແນະນຳ)',
        'overlay_type_stamp': 'ຕາຫຼັງ (ສາມາດກຳນົດຕຳແໜ່ງໄດ້)',
        'overlay_type_info_fullpage': '📄 PDF ຊັ້ນຊ້ອນຖືກວາງຢ່າງແນ່ນອນໃສ່ທົ່ວໜ້າ.\nສາມາດເອົາພື້ນຫຼັງສີຂາວອອກ ເພື່ອໃຫ້ສະເພາະເນື້ອໃນເທົ່ານັ້ນທີ່ເຫັນ.',
        'overlay_type_info_transparent': '🔍 PDF ຊັ້ນຊ້ອນຖືກວາງໃສ່ທົ່ວໜ້າດ້ວຍພື້ນຫຼັງໂປ່ງໃສ.\nພື້ນຫຼັງສີຂາວຖືກເອົາອອກໂດຍອັດຕະໂນມັດ - ເໝາະສຳລັບເຄື່ອງໝາຍນ້ຳ ແລະ ໂລໂກ້!',
        'overlay_type_info_stamp': '🖊️ PDF ຊັ້ນຊ້ອນຖືກກຳນົດຕຳແໜ່ງ ແລະ ປັບຂະໜາດເປັນຕາຫຼັງ.\nເໝາະສຳລັບໂລໂກ້, ຕາຫຼັງ ຫຼື ລາຍເຊັນໃນຕຳແໜ່ງສະເພາະ.',
        'overlay_remove_background': 'ເອົາພື້ນຫຼັງສີຂາວອອກ:',
        'overlay_remove_background_enable': 'ເອົາພື້ນຫຼັງສີຂາວອອກຈາກ PDF ຊັ້ນຊ້ອນ (ເຮັດໃຫ້ຊັ້ນຊ້ອນໂປ່ງໃສ)',
        'overlay_remove_background_tooltip': 'ເອົາພື້ນທີ່ສີຂາວອອກຈາກ PDF ຊັ້ນຊ້ອນ ເພື່ອໃຫ້ຂໍ້ຄວາມຂ້າງລຸ່ມເຫັນ.',
        'overlay_threshold': 'ຄ່າເກນ:',
        'overlay_threshold_hint': '(1-254, ສູງກວ່າ = ເອົາສີຂາວອອກຫຼາຍກວ່າ)',
        'overlay_select_file': 'ເລືອກ PDF ຊັ້ນຊ້ອນ:',
        'overlay_file_placeholder': 'ກະລຸນາເລືອກໄຟລ໌ PDF ສຳລັບຊັ້ນຊ້ອນ',
        'overlay_browse': 'ຊອກຫາ...',
        'overlay_select_overlay': 'ເລືອກ PDF ຊັ້ນຊ້ອນ',
        'overlay_range': 'ຂອບເຂດໜ້າ:',
        'overlay_all_pages': 'ທຸກໜ້າ',
        'overlay_custom_range': 'ຂອບເຂດປັບແຕ່ງ',
        'overlay_from': 'ຈາກ:',
        'overlay_to': 'ຫາ:',
        'overlay_position': 'ຕຳແໜ່ງ:',
        'overlay_position_center': 'ກາງ',
        'overlay_position_top_left': 'ເທິງຊ້າຍ',
        'overlay_position_top_right': 'ເທິງຂວາ',
        'overlay_position_bottom_left': 'ລຸ່ມຊ້າຍ',
        'overlay_position_bottom_right': 'ລຸ່ມຂວາ',
        'overlay_size': 'ຂະໜາດ:',
        'overlay_size_original': 'ຂະໜາດຕົ້ນສະບັບ',
        'overlay_size_fit_page': 'ປັບໃຫ້ເໝາະສົມກັບໜ້າ',
        'overlay_size_custom': 'ປັບແຕ່ງ (%)',
        'overlay_opacity': 'ຄວາມໂປ່ງໃສ:',
        'overlay_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'overlay_browse_folder': 'ຊອກຫາ...',
        'overlay_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'overlay_warning': '⚠️ ຫມາຍເຫດ: PDF ຊັ້ນຊ້ອນຖືກວາງໃສ່ PDF ພື້ນຖານ ແລະ "ເຜົາ" ເຂົ້າໄປໃນນັ້ນ.\n\nອົງປະກອບຂອງ PDF ຊັ້ນຊ້ອນບໍ່ສາມາດແກ້ໄຂແຕ່ລະອັນໄດ້ຫຼັງຈາກບັນທຶກ.',
        'overlay_apply': 'ຊ້ອນ',
        'overlay_start': 'ເລີ່ມຊ້ອນ...',
        'overlay_progress': 'ກຳລັງຊ້ອນ PDF...',
        'overlay_success': 'ຊ້ອນ PDF ສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nທ່ານຕ້ອງການເປີດ PDF ທີ່ຊ້ອນແລ້ວບໍ?',
        'overlay_complete': 'ການຊ້ອນສຳເລັດ',
        'overlay_cancel': 'ຍົກເລີກການຊ້ອນ',
        'overlay_error_format': 'ຂໍ້ຜິດພາດໃນການຊ້ອນ:\n\n{0}',
        'overlay_no_file': 'ບໍ່ມີ PDF ຊັ້ນຊ້ອນທີ່ເລືອກ.\n\nກະລຸນາເລືອກໄຟລ໌ PDF ສຳລັບຊ້ອນ.',
        'filename_overlay_suffix': '_ຊ້ອນແລ້ວ',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'ດຶງຮູບພາບອອກຈາກ PDF',
        'extract_images_menu': 'ດຶງຮູບພາບທັງໝົດອອກ',
        'extract_images_info': 'ດຶງຮູບພາບທັງໝົດອອກຈາກ PDF ແລະ ບັນທຶກພວກມັນເປັນໄຟລ໌ແຍກ.\n\nຮູບພາບຖືກບັນທຶກໃນຮູບແບບຕົ້ນສະບັບ ຫຼື ປ່ຽນເປັນຮູບແບບທີ່ເລືອກ.',
        'extract_images_format': 'ຮູບແບບຮູບພາບ:',
        'extract_images_quality': 'ຄຸນນະພາບ JPEG:',
        'extract_images_options': 'ຕົວເລືອກ:',
        'extract_images_subfolder': 'ດຶງໄປໂຟນເດີຍ່ອຍ ("ຊື່PDF_ຮູບພາບ")',
        'extract_images_unique': 'ສະເພາະຮູບພາບທີ່ເປັນເອກະລັກ (ຫຼີກເວັ້ນການຊ້ຳ)',
        'extract_images_range': 'ຂອບເຂດໜ້າ:',
        'extract_images_all_pages': 'ທຸກໜ້າ',
        'extract_images_custom_range': 'ຂອບເຂດປັບແຕ່ງ',
        'extract_images_from': 'ຈາກ:',
        'extract_images_to': 'ຫາ:',
        'extract_images_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'extract_images_browse': 'ຊອກຫາ...',
        'extract_images_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'extract_images_info_box': 'ຂໍ້ມູນ',
        'extract_images_info_text': 'ການດຶງອອກອາດໃຊ້ເວລາຫຼາຍນາທີສຳລັບ PDF ໃຫຍ່.\n\nຮູບພາບຖືກບັນທຶກດ້ວຍຊື່ຕົ້ນສະບັບ (ໜ້າ_ຮູບພາບ).',
        'extract_images_extract': 'ດຶງ',
        'extract_images_start': 'ເລີ່ມດຶງ...',
        'extract_images_progress': 'ກຳລັງດຶງຮູບພາບ...',
        'extract_images_success': '✅ ດຶງຮູບພາບສຳເລັດ!\n\nບັນທຶກຮູບພາບ {0} ໄວ້ທີ່:\n{1}',
        'extract_images_complete': 'ການດຶງຮູບພາບສຳເລັດ',
        'extract_images_cancel': 'ຍົກເລີກການດຶງ',
        'extract_images_error_format': 'ຂໍ້ຜິດພາດໃນການດຶງຮູບພາບ:\n\n{0}',
        'extract_images_open_folder': '📁 ເປີດໂຟນເດີ',
        'extract_images_no_images': 'ບໍ່ພົບຮູບພາບໃນ PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'ຫຼາຍໜ້າໃນໜ້າດຽວ (N-Up)',
        'nup_menu': 'ຫຼາຍໜ້າໃນໜ້າດຽວ (N-Up)',
        'nup_info': 'ຈັດຮຽງຫຼາຍໜ້າ PDF ໃນໜ້າດຽວ.\n\nເໝາະສຳລັບການພິມແບບກະທັດລັດ, ພາບລວມ ຫຼື ເອກະສານແຈກຢາຍ.',
        'nup_layout': 'ການຈັດວາງ:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'ການເບິ່ງຕົວຢ່າງ:',
        'nup_preview_info': '{0} ໜ້າ → {1} ໜ້າຕໍ່ແຜ່ນ → {2} ແຜ່ນ\nການຈັດວາງ: {3}',
        'nup_order': 'ລຳດັບ:',
        'nup_order_horizontal': 'ແນວນອນ (ແຖວຕໍ່ແຖວ)',
        'nup_order_vertical': 'ແນວຕັ້ງ (ຖັນຕໍ່ຖັນ)',
        'nup_order_horizontal_reverse': 'ແນວນອນກົງກັນຂ້າມ',
        'nup_order_vertical_reverse': 'ແນວຕັ້ງກົງກັນຂ້າມ',
        'nup_range': 'ຂອບເຂດໜ້າ:',
        'nup_all_pages': 'ທຸກໜ້າ',
        'nup_custom_range': 'ຂອບເຂດປັບແຕ່ງ',
        'nup_from': 'ຈາກ:',
        'nup_to': 'ຫາ:',
        'nup_options': 'ຕົວເລືອກ:',
        'nup_margins': 'ຂອບ:',
        'nup_margin_between': 'ໄລຍະຫ່າງລະຫວ່າງໜ້າ:',
        'nup_page_numbers': 'ໃສ່ເລກໜ້າ',
        'nup_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'nup_browse': 'ຊອກຫາ...',
        'nup_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'nup_create': 'ສ້າງ',
        'nup_start': 'ເລີ່ມ N-Up...',
        'nup_progress': 'ກຳລັງສ້າງ N-Up...',
        'nup_success': 'ສ້າງ N-Up ສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nທ່ານຕ້ອງການເປີດ PDF ໃໝ່ບໍ?',
        'nup_complete': 'N-Up ສຳເລັດ',
        'nup_cancel': 'ຍົກເລີກ N-Up',
        'nup_error_format': 'ຂໍ້ຜິດພາດໃນ N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'ປ່ຽນຂະໜາດໜ້າ',
        'pagesize_menu': 'ປ່ຽນຂະໜາດໜ້າ',
        'pagesize_info': 'ປ່ຽນຂະໜາດໜ້າຂອງ PDF.\n\nເນື້ອໃນຈະຖືກປັບອັດຕະໂນມັດໃຫ້ເໝາະສົມກັບຂະໜາດໃໝ່.',
        'pagesize_format': 'ຮູບແບບ:',
        'pagesize_select': 'ເລືອກຮູບແບບມາດຕະຖານ:',
        'pagesize_custom': 'ຂະໜາດປັບແຕ່ງ:',
        'pagesize_width': 'ຄວາມກວ້າງ:',
        'pagesize_height': 'ຄວາມສູງ:',
        'pagesize_orientation': 'ທິດທາງ:',
        'pagesize_portrait': 'ຕັ້ງ',
        'pagesize_landscape': 'ນອນ',
        'pagesize_scale_options': 'ຕົວເລືອກການປັບຂະໜາດ:',
        'pagesize_fit': 'ປັບ (ຮັກສາອັດຕາສ່ວນ)',
        'pagesize_stretch': 'ຍືດ (ບິດເບືອນ)',
        'pagesize_center': 'ກາງ (ຂະໜາດຕົ້ນສະບັບ)',
        'pagesize_range': 'ຂອບເຂດໜ້າ:',
        'pagesize_all_pages': 'ທຸກໜ້າ',
        'pagesize_custom_range': 'ຂອບເຂດປັບແຕ່ງ',
        'pagesize_from': 'ຈາກ:',
        'pagesize_to': 'ຫາ:',
        'pagesize_target_folder': 'ໂຟນເດີປາຍທາງ:',
        'pagesize_browse': 'ຊອກຫາ...',
        'pagesize_select_folder': 'ເລືອກໂຟນເດີປາຍທາງ',
        'pagesize_apply': 'ນຳໃຊ້',
        'pagesize_start': 'ເລີ່ມປ່ຽນຂະໜາດໜ້າ...',
        'pagesize_progress': 'ກຳລັງປ່ຽນຂະໜາດໜ້າ...',
        'pagesize_success': 'ປ່ຽນຂະໜາດໜ້າສຳເລັດ!\n\nບັນທຶກເປັນ:\n{0}\n\nທ່ານຕ້ອງການເປີດ PDF ໃໝ່ບໍ?',
        'pagesize_complete': 'ການປ່ຽນຂະໜາດໜ້າສຳເລັດ',
        'pagesize_cancel': 'ຍົກເລີກການປ່ຽນຂະໜາດໜ້າ',
        'pagesize_error_format': 'ຂໍ້ຜິດພາດໃນການປ່ຽນຂະໜາດໜ້າ:\n\n{0}',
        'pagesize_preview_info': 'ຂະໜາດໃໝ່: {0} x {1} pt',
        'filename_pagesize_suffix': '_ຂະໜາດໃໝ່',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'ຂໍ້ມູນ PDF',
        'pdf_info_menu': 'ສະແດງຂໍ້ມູນ PDF',
        'pdf_info_voice': 'ກຳລັງສະແດງຂໍ້ມູນ PDF',
        'pdf_info_error': 'ຂໍ້ຜິດພາດໃນການສະແດງຂໍ້ມູນ PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "ສະແດງທາງລັດແປ້ນພິມ",
        "shortcuts_dialog_title": "ທາງລັດແປ້ນພິມ",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 ໄຟລ໌</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>ເປີດ PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>ປິດ PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>ບັນທຶກເປັນ...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>ປົກປ້ອງເອກະສານ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>ພິມ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>ພິມທັນທີ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>ອອກຈາກແອັບພລິເຄຊັນ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 ສົ່ງອອກ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>ສົ່ງອອກເປັນ Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>ສົ່ງອອກເປັນ DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>ສົ່ງອອກເປັນ TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ສົ່ງອອກເປັນຮູບພາບ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>ດຶງຮູບພາບ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ການປະມວນຜົນເອກະສານ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (ຫຼາຍໜ້າ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>ການແປງ PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>ເຮັດໃຫ້ PDF ຮາບ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>ຊ້ອນ PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>ເພີ່ມປະສິດທິພາບ PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ ແກ້ໄຂ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>ຄົ້ນຫາ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>ເພີ່ມບຸກມາກ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ຈັດການບຸກມາກ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>ບຸກມາກຕໍ່ໄປ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>ບຸກມາກກ່ອນໜ້າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>ແລ່ນ OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 ການຈັດການໜ້າ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>ໝູນໜ້າປັດຈຸບັນ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>ໝູນທຸກໜ້າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>ເຮັດໃຫ້ໜ້າປັດຈຸບັນປົກກະຕິ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>ເຮັດໃຫ້ທຸກໜ້າປົກກະຕິ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ລຶບໜ້າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>ດຶງໜ້າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>ໃສ່ໜ້າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>ຍ້າຍໜ້າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>ລວມ PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>ປ່ຽນຂະໜາດໜ້າ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 ໃສ່</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>ໃສ່ຂໍ້ຄວາມ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>ໃສ່ໄມ້ກາງແຂນ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>ໃສ່ລາຍເຊັນ 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>ໃສ່ລາຍເຊັນ 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ໃສ່ຮູບພາບ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>ໃສ່ຮູບສີ່ແຈສາກ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>ໃສ່ຮູບຮີ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>ໃສ່ເສັ້ນ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>ໃສ່ລູກສອນ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>ໃສ່ເລກໜ້າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ເຄື່ອງໝາຍນ້ຳຂໍ້ຄວາມ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>ເຄື່ອງໝາຍນ້ຳຮູບພາບ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ ການລຶບຂໍ້ມູນ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ການລຶບຂໍ້ມູນ (ດຳ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ການລຶບຂໍ້ມູນ (ຂາວ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>ນຳໃຊ້ການລຶບຂໍ້ມູນທັງໝົດ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ຂັ້ນສູງ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>ຕັດ PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ແກ້ໄຂເມຕາເດຕາ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ ເບິ່ງ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ປ່ຽນໂໝດມືດ/ສະຫວ່າງ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>ສະແດງປ່ອງຢ້ຽມຂໍ້ຄວາມ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>ຄວາມກວ້າງໜ້າ (ຊູມ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>ສອງໜ້າ (ຊູມ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>ພາບລວມ (ຊູມ)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ການຕັ້ງຄ່າ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>ການຈັດການລະຫັດຜ່ານ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>ການຕັ້ງຄ່າ OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>ການຕັ້ງຄ່າລາຍເຊັນ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>ການຈັດຮູບແບບຊື່ໄຟລ໌</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>ສົ່ງອອກການຕັ້ງຄ່າ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>ນຳເຂົ້າການຕັ້ງຄ່າ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ ຂໍ້ມູນ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ສະແດງຂໍ້ມູນ PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>ເປີດ/ປິດ ການອອກສຽງ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>ເອົາໃສ່ແຖບເມນູ</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "ມີສະບັບໃໝ່",
        "update_available_message": "ມີສະບັບໃໝ່ <b>{0}</b>.\n\nໄປທີ່ໜ້າເຜີຍແຜ່ເພື່ອດາວໂຫຼດການອັບເດດ:\n{1}",
        "update_available_voice": "ມີສະບັບໃໝ່ {0}. ກະລຸນາດາວໂຫຼດການອັບເດດຈາກໜ້າ GitHub.",
        "update_open_release": "ເປີດໜ້າເຜີຍແຜ່",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "ດາວໂຫຼດຄຳແປທັງໝົດ",
        "ask_download_all_translations": """ນອກຈາກພາສາເຢຍລະມັນ, ອັງກິດ ແລະ ຫວຽດນາມ, ຍັງມີພາສາ GUI ອີກ {total_languages} ພາສາ.\n\nຄວນສະໜອງ / ອັບເດດບໍ?\n\nຫມາຍເຫດ:\nພາສາທີ່ບໍ່ຈຳເປັນ ທ່ານສາມາດລຶບດ້ວຍມືໃນພາຍຫຼັງໃນໄດເລກະທໍລີ:\n{translations_path}
        \nຖ້າທ່ານຍົກເລີກ, ທ່ານສາມາດດາວໂຫຼດພາສາ GUI ໃນພາຍຫຼັງຜ່ານເມນູ 'ເຄື່ອງມື → ອັບເດດຄຳແປ'.""",
        "menu_update_translations": "ອັບເດດຄຳແປ",
        "translations_updated": "ຄຳແປຖືກອັບເດດແລ້ວ",
        "translations_update_success": "ຄຳແປຈຳນວນ {} ຖືກອັບເດດສຳເລັດ ({} ໃໝ່, {} ອັບເດດ).",
        "translations_update_error": "ຂໍ້ຜິດພາດໃນການອັບເດດຄຳແປ",
        "translations_update_no_changes": "ຄຳແປທັງໝົດແມ່ນທັນສະໄໝແລ້ວ.",
        "translations_update_offline": "ບໍ່ມີການເຊື່ອມຕໍ່ອິນເຕີເນັດ. ບໍ່ສາມາດອັບເດດຄຳແປໄດ້.",
        "translations_update_in_progress": "ກຳລັງອັບເດດຄຳແປໃນພື້ນຫຼັງ...",
        "translations_downloading": "ກຳລັງດາວໂຫຼດຄຳແປ...",
        "translations_path_hint": "ໄດເລກະທໍລີຜູ້ໃຊ້ສຳລັບຄຳແປ",
        "translations_update_not_available_title": "ການອັບເດດບໍ່ມີ",
        "translations_update_not_available_message": """ການອັບເດດຄຳແປມີໃຫ້ໃນສະບັບທີ່ຕິດຕັ້ງເທົ່ານັ້ນ.\n\nໃນໂໝດພັດທະນາ, ຄຳແປແມ່ນທັນສະໄໝແລ້ວ.""",
        "translations_update_no_internet_title": "ບໍ່ມີການເຊື່ອມຕໍ່ອິນເຕີເນັດ",
        "translations_update_no_internet_message": """ບໍ່ສາມາດສ້າງການເຊື່ອມຕໍ່ອິນເຕີເນັດໄດ້.\n\nບໍ່ສາມາດດາວໂຫຼດຄຳແປຈາກ GitHub ໄດ້.\n\nວິທີແກ້ໄຂທີ່ເປັນໄປໄດ້:
        • ກວດສອບການເຊື່ອມຕໍ່ອິນເຕີເນັດຂອງທ່ານ
        • ປິດໄຟວໍໃດໆຊົ່ວຄາວ
        • ລອງໃໝ່ອີກຄັ້ງພາຍຫຼັງ
        \nທ່ານຍັງສາມາດດາວໂຫຼດຄຳແປດ້ວຍມືຈາກ GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "ການອັບເດດກຳລັງດຳເນີນຢູ່ແລ້ວ",
        "btn_retry": "ລອງໃໝ່ອີກຄັ້ງ",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "ຍິນດີຕ້ອນຮັບສູ່ PDF Dark View",
        "welcome_title_not_supported": "ຍິນດີຕ້ອນຮັບສູ່ PDF Dark View",
        "welcome_message": "ຍິນດີຕ້ອນຮັບສູ່ PDF Dark View!\n\nພາສາລະບົບຂອງທ່ານຖືກກວດພົບວ່າເປັນ '{language}'.\nທ່ານຕ້ອງການໃຊ້ພາສານີ້ສຳລັບສ່ວນຕິດຕໍ່ຜູ້ໃຊ້ບໍ?\n\nທ່ານສາມາດປ່ຽນພາສາໄດ້ທຸກເວລາຜ່ານ 'ການຕັ້ງຄ່າ → ພາສາ'.",
        "welcome_message_language_not_available": "ຍິນດີຕ້ອນຮັບສູ່ PDF Dark View!\n\nພາສາລະບົບຂອງທ່ານຖືກກວດພົບວ່າເປັນ '{language}'.\nພາສານີ້ຍັງບໍ່ທັນຕິດຕັ້ງ.\n\nທ່ານຕ້ອງການດາວໂຫຼດຄຳແປສຳລັບ {language} ດຽວນີ້ຈາກ GitHub ບໍ?\n\n(ພາສາຈະຖືກນຳໃຊ້ໂດຍອັດຕະໂນມັດສຳລັບສ່ວນຕິດຕໍ່ຜູ້ໃຊ້.)",
        "welcome_message_language_not_supported": "ຍິນດີຕ້ອນຮັບສູ່ PDF Dark View!\n\nພາສາລະບົບຂອງທ່ານຖືກກວດພົບວ່າເປັນ '{language}'.\nແຕ່ໜ້າເສຍດາຍ, ຍັງບໍ່ມີຄຳແປສຳລັບພາສານີ້.\n\nສ່ວນຕິດຕໍ່ຜູ້ໃຊ້ຈະສະແດງເປັນ {fallback_language}.\n\nທ່ານສາມາດປ່ຽນພາສາໄດ້ທຸກເວລາຜ່ານ 'ການຕັ້ງຄ່າ → ພາສາ'.\nຖ້າທ່ານຕ້ອງການ, ທ່ານຍັງສາມາດປະກອບສ່ວນຄຳແປສຳລັບພາສາຂອງທ່ານເອງ:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "ແມ່ນ, ໃຊ້ພາສາລະບົບ",
        "welcome_keep_english": "ບໍ່, ຮັກສາພາສາອັງກິດ",
        "welcome_download_language": "ແມ່ນ, ດາວໂຫຼດ {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "ກຳລັງປິດໂປຣແກຣມ",

    }


