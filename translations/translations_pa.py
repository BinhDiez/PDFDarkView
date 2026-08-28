
# ============================================
# translations_pa.py - Punjabi Wörterbuch für PDFDarkView
# Vollständig sortiert nach Kategorien
# ============================================

def load_punjabi_strings():
    """Lädt alle Punjabi Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF ਲੋਡ ਕਰੋ",
        'btn_text_window': "OCR ਟੈਕਸਟ",
        'btn_first': "ਪਹਿਲਾ ਪੰਨਾ",
        'btn_prev': "ਪਿਛਲਾ ਪੰਨਾ",
        'btn_next': "ਅਗਲਾ ਪੰਨਾ",
        'btn_last': "ਆਖਰੀ ਪੰਨਾ",
        'btn_print': "ਛਾਪੋ",
        'btn_darkmode_light': "ਹਲਕਾ ਮੋਡ",
        'btn_darkmode_dark': "ਡਾਰਕ ਮੋਡ",
        'btn_delete_pages': "ਪੰਨੇ ਮਿਟਾਓ",
        'btn_extract_pages': "ਪੰਨੇ ਕੱਢੋ",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "ਠੀਕ ਹੈ",
        'btn_cancel': "ਰੱਦ ਕਰੋ",
        'btn_save': "ਸੰਭਾਲੋ",
        'btn_close': "ਬੰਦ ਕਰੋ",
        'btn_delete': "ਮਿਟਾਓ",
        'btn_delete_all': "ਸਭ ਮਿਟਾਓ",
        'btn_copy': "ਕਾਪੀ ਕਰੋ",
        'btn_export': "ਐਕਸਪੋਰਟ ਕਰੋ",
        'btn_show': "ਪਾਸਵਰਡ ਦਿਖਾਓ",
        'btn_hide': "ਪਾਸਵਰਡ ਲੁਕਾਓ",
        'btn_authenticate': "ਪ੍ਰਮਾਣਿਤ ਕਰੋ",
        'btn_settings': "ਸੈਟਿੰਗਾਂ",
        'btn_protect': "ਸੁਰੱਖਿਅਤ ਕਰੋ",
        'btn_remove_password': "ਪਾਸਵਰਡ ਹਟਾਓ",
        'btn_manage': "ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ",
        'btn_retry': "ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕਰੋ",
        'btn_select_all': "ਸਭ ਚੁਣੋ",
        'btn_clear_selection': "ਚੋਣ ਰੱਦ ਕਰੋ",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "{1} ਵਿੱਚੋਂ ਪੰਨਾ {0}",
        'page_count': "{0} ਵਿੱਚੋਂ",
        'goto_page': "ਪੰਨੇ ਤੇ ਜਾਓ",
        'page_simple': "ਪੰਨਾ {0}",
        'full_view_page': "ਪੂਰਾ ਦ੍ਰਿਸ਼ ਪੰਨਾ {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "ਖੋਜ ਸ਼ਬਦ ਟਾਈਪ ਕਰੋ + ਐਂਟਰ",
        'search_results': "ਮਿਲਾਨ: {1} ਵਿੱਚੋਂ {0}",
        'search_nav_hint': "ਐਂਟਰ: ਅਗਲਾ (Shift+Enter: ਪਿਛਲਾ) ਨਤੀਜਾ",
        'search_no_results': "ਕੋਈ ਨਤੀਜਾ ਨਹੀਂ ਮਿਲਿਆ",
        'search_error': "ਖੋਜ ਗਲਤੀ",
        'search_active': "ਖੋਜ ਫੀਲਡ ਸਰਗਰਮ",
        'search_closed': "ਖੋਜ ਸਮਾਪਤ",
        'search_position': "ਪੰਨਾ {0} {1}",
        'search_pos_top': "ਬਿਲਕੁਲ ਉੱਪਰ",
        'search_pos_upper': "ਉੱਪਰ",
        'search_pos_middle': "ਵਿਚਕਾਰ",
        'search_pos_lower': "ਹੇਠਾਂ",
        'search_pos_bottom': "ਬਿਲਕੁਲ ਹੇਠਾਂ",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "ਟੈਕਸਟ ਪਛਾਣ ਸਫਲਤਾਪੂਰਵਕ ਪੂਰੀ ਹੋਈ!",
        'ocr_success_title': "OCR ਸਫਲ",
        'ocr_success_message': "ਦਸਤਾਵੇਜ਼ ਹੁਣ ਖੋਜਣ ਯੋਗ ਹੈ।",
        'ocr_failed': "OCR ਅਸਫਲ",
        'ocr_in_progress': "OCR ਜਾਰੀ ਹੈ",
        'ocr_preparing': "PDF ਤਿਆਰ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'ocr_analyzing': "PDF ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'ocr_optimizing': "ਚਿੱਤਰ ਅਨੁਕੂਲਤਾ ਚੱਲ ਰਹੀ ਹੈ...",
        'ocr_recognizing': "ਟੈਕਸਟ ਪਛਾਣ ਕਾਰਜ ਚੱਲ ਰਿਹਾ ਹੈ...",
        'ocr_embedding': "ਟੈਕਸਟ ਏਮਬੈਡ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'ocr_finalizing': "PDF ਨੂੰ ਅੰਤਿਮ ਰੂਪ ਦਿੱਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'ocr_not_available': "OCR ਉਪਲਬਧ ਨਹੀਂ",
        'ocr_install_message': "OCR ਟੂਲ ਨਹੀਂ ਮਿਲੇ।\n\nਕਿਰਪਾ ਕਰਕੇ ਇੰਸਟਾਲ ਕਰੋ:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR ਦੀ ਲੋੜ ਹੈ",
        'ocr_question': "PDF ਵਿੱਚ ਕੋਈ ਖੋਜਣ ਯੋਗ ਟੈਕਸਟ ਨਹੀਂ ਹੈ।\nਕੀ ਤੁਸੀਂ {0} ਨੂੰ ਸਮਰੱਥ ਕਰਨ ਲਈ OCR ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'ocr_perform': "OCR ਕਰੋ",
        'ocr_later': "ਬਾਅਦ ਵਿੱਚ",
        'ocr_starting': "ਗਾਰੰਟੀਸ਼ੁਦਾ OCR ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'ocr_success_voice': "OCR ਸਫਲ। PDF ਹੁਣ ਖੋਜਣ ਯੋਗ ਹੈ।",
        'ocr_partial_success': "OCR ਕੀਤਾ ਗਿਆ, ਪਰ ਬਦਲਣ ਵੇਲੇ ਸਮੱਸਿਆਵਾਂ ਆਈਆਂ।\n\nਖੋਜਣ ਯੋਗ ਸੰਸਕਰਣ ਇਸ ਵਿੱਚ ਸੰਭਾਲਿਆ ਗਿਆ:\n{0}\n\nਗਲਤੀ: {1}",
        'ocr_partial_title': "OCR ਅੰਸ਼ਕ ਤੌਰ ਤੇ ਸਫਲ",
        'ocr_partial_voice': "OCR ਕੀਤਾ ਗਿਆ, ਪਰ ਬਦਲਣਾ ਅਸਫਲ ਰਿਹਾ।",
        'original_file': "ਅਸਲ ਫਾਈਲ:",
        'old_size': "ਪੁਰਾਣੀ ਫਾਈਲ ਦਾ ਆਕਾਰ:    {0} ਬਾਈਟ",
        'new_size': "ਨਵੀਂ ਫਾਈਲ ਦਾ ਆਕਾਰ: {0} ਬਾਈਟ",
        'size_change': "ਤਬਦੀਲੀ: {0}{1} ਬਾਈਟ",
        'backup_created_file': "ਬੈਕਅੱਪ ਬਣਾਇਆ:\n{0}",
        'backup_not_created': "ਬੈਕਅੱਪ: ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ (ਸੈਟਿੰਗ ਅਸਮਰੱਥ)",
        'page_header': "=== ਪੰਨਾ {0} ===\n{1}\n",
        'scanned_page_header': "=== ਪੰਨਾ {0} (ਸਕੈਨ ਕੀਤਾ) ===\n[ਇਸ ਪੰਨੇ ਵਿੱਚ ਸਿਰਫ ਸਕੈਨ ਕੀਤਾ ਟੈਕਸਟ ਹੈ]\n[ਕਿਰਪਾ ਕਰਕੇ ਮੈਨੂਅਲੀ OCR ਕਰੋ]\n",
        'scanned_warning': "⚠️ ਸਕੈਨ ਕੀਤਾ ਟੈਕਸਟ - OCR ਦੀ ਲੋੜ ਹੈ",
        'guaranteed_title': "ਖੋਜਣ ਯੋਗ PDF ਬਣਾਈ ਗਈ",
        'guaranteed_message': "<b>ਗਾਰੰਟੀਸ਼ੁਦਾ ਖੋਜਣ ਯੋਗ ਸੰਸਕਰਣ ਬਣਾਇਆ ਗਿਆ!</b>\n\nਕਿਉਂਕਿ ਆਟੋਮੈਟਿਕ OCR ਅਸਫਲ ਰਿਹਾ, ਇੱਕ\nਵਿਕਲਪਿਕ ਖੋਜਣ ਯੋਗ PDF ਬਣਾਈ ਗਈ:\n\n{0}\n\n<b>ਇਸ ਫਾਈਲ ਵਿੱਚ ਸ਼ਾਮਲ ਹੈ:</b>\n• ਕੱਢਿਆ ਗਿਆ ਟੈਕਸਟ (ਜੇਕਰ ਮੌਜੂਦ ਹੈ)\n• ਸਕੈਨ ਕੀਤੇ ਪੰਨਿਆਂ ਲਈ ਨੋਟਿਸ\n• ਪੂਰੀ ਤਰ੍ਹਾਂ ਖੋਜਣ ਯੋਗ ਹੈ",
        'guaranteed_voice': "ਗਾਰੰਟੀਸ਼ੁਦਾ ਖੋਜਣ ਯੋਗ PDF ਬਣਾਈ ਗਈ।",
        'instruction_title': "OCR ਲਈ ਨਿਰਦੇਸ਼",
        'instruction_file': "ਅਸਲ ਫਾਈਲ: {0}",
        'instruction_text': "ਆਟੋਮੈਟਿਕ ਟੈਕਸਟ ਪਛਾਣ (OCR) ਅਸਫਲ ਰਹੀ।\nਕਿਰਪਾ ਕਰਕੇ ਮੈਨੂਅਲੀ OCR ਕਰੋ:\n\n1. OCRmyPDF (ਕਮਾਂਡ ਲਾਈਨ):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. ADOBE ACROBAT (macOS/Windows):\n   • Acrobat ਵਿੱਚ PDF ਖੋਲ੍ਹੋ\n   • Tools > Edit PDF\n   • 'Text Recognition' ਚੁਣੋ\n\n3. PREVIEW (macOS):\n   • Preview ਵਿੱਚ PDF ਖੋਲ੍ਹੋ\n   • File > Export...\n   • Quartz Filter: 'Reduce File Size'\n   • 'OCR ਕਰੋ' ਸਰਗਰਮ ਕਰੋ\n\n4. ਔਨਲਾਈਨ OCR ਸੇਵਾਵਾਂ:\n   • smallpdf.com/de/ocr-pdf\n   • ilovepdf.com/de/ocr-pdf\n   • adobe.com/de/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR ਨਿਰਦੇਸ਼ ਬਣਾਏ ਗਏ",
        'instruction_created_message': "ਇੱਕ ਵਿਸਤ੍ਰਿਤ ਨਿਰਦੇਸ਼ ਬਣਾਇਆ ਗਿਆ:\n\n{0}\n\nਕਿਰਪਾ ਕਰਕੇ ਮੈਨੂਅਲ OCR ਲਈ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।",
        'instruction_created_voice': "OCR ਨਿਰਦੇਸ਼ ਬਣਾਏ ਗਏ।",
        'ocr_impossible': "OCR ਸੰਭਵ ਨਹੀਂ",
        'ocr_impossible_message': "OCR ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਿਆ।\n\nਕਿਰਪਾ ਕਰਕੇ '{0}' ਨੂੰ ਮੈਨੂਅਲੀ OCR ਸੌਫਟਵੇਅਰ ਨਾਲ ਪ੍ਰਕਿਰਿਆ ਕਰੋ।",
        'ocr_impossible_voice': "OCR ਸੰਭਵ ਨਹੀਂ। ਕਿਰਪਾ ਕਰਕੇ ਮੈਨੂਅਲੀ ਪ੍ਰਕਿਰਿਆ ਕਰੋ।",
        'emergency_title': "ਐਮਰਜੈਂਸੀ OCR",
        'emergency_message': "ਇੱਕ ਐਮਰਜੈਂਸੀ PDF ਬਣਾਈ ਗਈ:\n\n{0}\n\nਕਿਰਪਾ ਕਰਕੇ ਇਸ ਫਾਈਲ ਨੂੰ ਮੈਨੂਅਲੀ OCR ਨਾਲ ਪ੍ਰਕਿਰਿਆ ਕਰੋ।",
        'emergency_voice': "ਐਮਰਜੈਂਸੀ PDF ਬਣਾਈ ਗਈ। ਕਿਰਪਾ ਕਰਕੇ ਮੈਨੂਅਲੀ OCR ਕਰੋ।",
        'critical_error': "ਗੰਭੀਰ ਗਲਤੀ",
        'critical_error_message': "OCR ਸ਼ੁਰੂ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਿਆ।\n\nਕਿਰਪਾ ਕਰਕੇ ਪ੍ਰੋਗਰਾਮ ਮੁੜ ਚਾਲੂ ਕਰੋ ਅਤੇ\nOCR ਇੰਸਟਾਲੇਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ।",
        'critical_error_voice': "ਗੰਭੀਰ OCR ਗਲਤੀ",
        'ocr_question_html': "<p>PDF ਵਿੱਚ ਕੋਈ ਖੋਜਣ ਯੋਗ ਟੈਕਸਟ ਨਹੀਂ ਹੈ।<p>ਕੀ ਤੁਸੀਂ <b>{0}</b> ਨੂੰ ਸਮਰੱਥ ਕਰਨ ਲਈ OCR ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?</p>",
        'ocr_question_voice': "OCR ਦੀ ਲੋੜ ਹੈ। PDF ਵਿੱਚ ਕੋਈ ਖੋਜਣ ਯੋਗ ਟੈਕਸਟ ਨਹੀਂ ਹੈ। ਕੀ ਤੁਸੀਂ {0} ਨੂੰ ਸਮਰੱਥ ਕਰਨ ਲਈ OCR ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ਕੋਈ PDF ਲੋਡ ਨਹੀਂ ਕੀਤੀ ਗਈ",
        'no_pdf_message': "ਕੋਈ PDF ਲੋਡ ਨਹੀਂ ਕੀਤੀ ਗਈ",
        'pdf_not_found': "PDF ਫਾਈਲ ਨਹੀਂ ਮਿਲੀ",
        'file_size': "ਫਾਈਲ ਦਾ ਆਕਾਰ",
        'bytes': "ਬਾਈਟ",
        'kb': "ਕੇਬੀ",
        'mb': "ਐਮਬੀ",
        'backup_created': "ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ",
        'backup_disabled': "ਬੈਕਅੱਪ ਅਸਮਰੱਥ",
        'backup_activated': "ਬੈਕਅੱਪ ਬਣਾਉਣਾ ਸਰਗਰਮ",
        'backup_deactivated': "ਬੈਕਅੱਪ ਬਣਾਉਣਾ ਅਸਰਗਰਮ",
        'backup_status': "ਬੈਕਅੱਪ: {0}",
        'backup_on': "✔ ਸਰਗਰਮ",
        'backup_off': "✘ ਅਸਰਗਰਮ",
        'close_pdf': "PDF ਬੰਦ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ: {0}",
        'pdf_not_found_format': "PDF ਫਾਈਲ ਨਹੀਂ ਮਿਲੀ: {0}",
        'error_pdf_load_format': "PDF ਲੋਡ ਕਰਨ ਵੇਲੇ ਗਲਤੀ: {0}",
        'load_failed_format': "ਲੋਡ ਅਸਫਲ:\n{0}",
        'decrypted_suffix': "(ਡੀਕ੍ਰਿਪਟ ਕੀਤੀ)",
        'decryption_failed': "ਡੀਕ੍ਰਿਪਸ਼ਨ ਅਸਫਲ ਰਿਹਾ।",
        'decryption_error': "ਡੀਕ੍ਰਿਪਟ ਕਰਨ ਵੇਲੇ ਗਲਤੀ",
        'decryption_success': "ਸਫਲਤਾਪੂਰਵਕ ਡੀਕ੍ਰਿਪਟ ਕੀਤਾ ਗਿਆ",
        'decryption_success_message': "PDF ਨੂੰ ਡੀਕ੍ਰਿਪਟ ਕਰਕੇ ਇਸ ਵਿੱਚ ਸੰਭਾਲਿਆ ਗਿਆ:\n\n{0}",
        'decryption_success_voice': "PDF ਨੂੰ ਡੀਕ੍ਰਿਪਟ ਕਰਕੇ ਸੰਭਾਲਿਆ ਗਿਆ।",
        'password_remove_error': "ਪਾਸਵਰਡ ਹਟਾਉਣ ਵੇਲੇ ਗਲਤੀ",
        'save_unencrypted': "ਅਣਐਨਕ੍ਰਿਪਟਡ PDF ਸੰਭਾਲੋ",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "ਇਸ ਤਰ੍ਹਾਂ ਸੰਭਾਲੋ...",
        'save_copy': "ਕਾਪੀ ਸੰਭਾਲੋ",
        'save_success': "PDF ਇਸ ਵਿੱਚ ਸੰਭਾਲੀ ਗਈ: {0}",
        'save_encrypted': "ਸੁਰੱਖਿਅਤ PDF ਇਸ ਵਿੱਚ ਸੰਭਾਲੀ ਗਈ: {0}",
        'save_error': "PDF ਸੰਭਾਲੀ ਨਹੀਂ ਜਾ ਸਕੀ",
        'encryption_question': "ਕੀ ਤੁਸੀਂ PDF ਨੂੰ ਪਾਸਵਰਡ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'encryption_yes': "ਹਾਂ",
        'encryption_no': "ਨਹੀਂ",
        'encryption_cancel': "ਰੱਦ ਕਰੋ",
        'save_cancel': "ਸੰਭਾਲਣਾ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'save_encrypted_voice': "ਫਾਈਲ ਐਨਕ੍ਰਿਪਟ ਕਰਕੇ ਸੰਭਾਲੀ ਗਈ।",
        'save_success_voice': "PDF ਫਾਈਲ ਅਣਐਨਕ੍ਰਿਪਟਡ ਸੰਭਾਲੀ ਗਈ।",
        'save_error_format': "PDF ਸੰਭਾਲੀ ਨਹੀਂ ਜਾ ਸਕੀ:\n{0}",
        'export_pages_success': "Pages ਐਕਸਪੋਰਟ ਸਫਲ",
        'export_pages_error': "Pages ਐਕਸਪੋਰਟ ਅਸਫਲ",
        'export_pages_error_format': "Pages ਐਕਸਪੋਰਟ ਅਸਫਲ: {0}",
        'export_word_success': "Word ਐਕਸਪੋਰਟ ਸਫਲ",
        'export_word_error': "Word ਐਕਸਪੋਰਟ ਅਸਫਲ",
        'export_word_error_format': "Word ਐਕਸਪੋਰਟ ਅਸਫਲ: {0}",
        'export_text_success': "ਟੈਕਸਟ ਐਕਸਪੋਰਟ ਸਫਲ",
        'export_text_error': "ਟੈਕਸਟ ਐਕਸਪੋਰਟ ਅਸਫਲ",
        'export_text_error_format': "ਟੈਕਸਟ ਐਕਸਪੋਰਟ ਅਸਫਲ: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "ਪਾਸਵਰਡ ਦੀ ਲੋੜ ਹੈ",
        'password_enter': "ਕਿਰਪਾ ਕਰਕੇ ਪਾਸਵਰਡ ਟਾਈਪ ਕਰੋ",
        'password_confirm': "ਪਾਸਵਰਡ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ",
        'password_new': "ਨਵਾਂ ਪਾਸਵਰਡ",
        'password_current': "ਮੌਜੂਦਾ ਪਾਸਵਰਡ",
        'password_save': "ਪਾਸਵਰਡ ਸੰਭਾਲੋ (ਐਨਕ੍ਰਿਪਟ ਕੀਤਾ)",
        'password_saved': "✓ ਇਸ ਫਾਈਲ ਲਈ ਪਾਸਵਰਡ ਸੰਭਾਲਿਆ ਗਿਆ ਹੈ",
        'password_wrong': "ਗਲਤ ਪਾਸਵਰਡ",
        'password_mismatch': "ਪਾਸਵਰਡ ਮੇਲ ਨਹੀਂ ਖਾਂਦੇ",
        'password_too_short': "ਪਾਸਵਰਡ ਬਹੁਤ ਛੋਟਾ ਹੈ",
        'password_min_length': "ਪਾਸਵਰਡ ਘੱਟੋ-ਘੱਟ 4 ਅੱਖਰਾਂ ਦਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ",
        'password_strength': "ਪਾਸਵਰਡ ਦੀ ਤਾਕਤ",
        'password_strength_very_weak': "ਬਹੁਤ ਕਮਜ਼ੋਰ",
        'password_strength_weak': "ਕਮਜ਼ੋਰ",
        'password_strength_medium': "ਮੱਧਮ",
        'password_strength_strong': "ਮਜ਼ਬੂਤ",
        'password_strength_very_strong': "ਬਹੁਤ ਮਜ਼ਬੂਤ",
        'password_char_count': "({0} ਅੱਖਰ)",
        'password_match': "✓ ਮੇਲ ਖਾਂਦਾ ਹੈ",
        'password_no_match': "✗ ਪਾਸਵਰਡ ਮੇਲ ਨਹੀਂ ਖਾਂਦੇ",
        'password_show': "ਦਿਖਾਓ",
        'password_hide': "ਲੁਕਾਓ",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ",
        'password_table_filename': "ਫਾਈਲ ਦਾ ਨਾਂ",
        'password_table_password': "ਪਾਸਵਰਡ",
        'password_count': "{0} ਸੰਭਾਲੇ ਗਏ ਪਾਸਵਰਡ",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "ਕੋਈ ਸੰਭਾਲਿਆ ਪਾਸਵਰਡ ਨਹੀਂ",
        'password_copied': "{0} ਪਾਸਵਰਡ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "ਕੀ ਤੁਸੀਂ ਸੱਚਮੁੱਚ '{0}' ਲਈ ਪਾਸਵਰਡ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'password_delete_multiple': "ਕੀ ਤੁਸੀਂ ਸੱਚਮੁੱਚ ਚੁਣੇ ਗਏ {0} ਪਾਸਵਰਡ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'password_delete_all_confirm': "ਕੀ ਤੁਸੀਂ ਸੱਚਮੁੱਚ ਸਾਰੇ {0} ਸੰਭਾਲੇ ਗਏ ਪਾਸਵਰਡ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'password_deleted': "{0} ਪਾਸਵਰਡ ਮਿਟਾਏ ਗਏ",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "ਸਾਰੇ ਪਾਸਵਰਡ ਮਿਟਾ ਦਿੱਤੇ ਗਏ",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "ਪਾਸਵਰਡ ਜਨਰੇਟਰ",
        'generator_generated': "ਜਨਰੇਟ ਕੀਤਾ ਗਿਆ ਪਾਸਵਰਡ:",
        'generator_regenerate': "ਮੁੜ ਜਨਰੇਟ ਕਰੋ",
        'generator_copy': "ਕਾਪੀ ਕਰੋ",
        'generator_use': "ਵਰਤੋਂ ਕਰੋ",
        'generator_settings': "ਸੈਟਿੰਗਾਂ",
        'generator_length': "ਲੰਬਾਈ:",
        'generator_group_every': "ਵਿਭਾਜਕ ਹਰ",
        'generator_group_chars': "ਅੱਖਰ।    ਵਿਭਾਜਕ:",
        'generator_uppercase': "ਵੱਡੇ ਅੱਖਰ (A-Z)",
        'generator_lowercase': "ਛੋਟੇ ਅੱਖਰ (a-z)",
        'generator_digits': "ਅੰਕ (0-9)",
        'generator_symbols': "ਵਿਸ਼ੇਸ਼ ਚਿੰਨ੍ਹ (!@#$%^&*)",
        'generator_exclude': "ਬਾਹਰ ਕਰੋ:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਦੀ ਲੋੜ ਹੈ",
        'master_password_setup': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰੋ",
        'master_password_change': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਬਦਲੋ",
        'master_password_enter': "ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ ਮਾਸਟਰ ਪਾਸਵਰਡ ਟਾਈਪ ਕਰੋ",
        'master_password_choose': "ਇੱਕ ਮਜ਼ਬੂਤ ਮਾਸਟਰ ਪਾਸਵਰਡ ਚੁਣੋ (ਘੱਟੋ-ਘੱਟ 8 ਅੱਖਰ)",
        'master_password_new': "ਕਿਰਪਾ ਕਰਕੇ ਆਪਣਾ ਨਵਾਂ ਮਾਸਟਰ ਪਾਸਵਰਡ ਟਾਈਪ ਕਰੋ",
        'master_password_confirm': "ਪਾਸਵਰਡ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ",
        'master_password_authenticate': "ਪ੍ਰਮਾਣਿਤ ਕਰੋ",
        'master_password_success': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਸਫਲਤਾਪੂਰਵਕ ਸੈੱਟਅੱਪ ਕੀਤਾ ਗਿਆ।",
        'master_password_changed': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਸਫਲਤਾਪੂਰਵਕ ਬਦਲਿਆ ਗਿਆ।",
        'master_password_removed': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਅਤੇ ਸਾਰੇ ਪਾਸਵਰਡ ਮਿਟਾ ਦਿੱਤੇ ਗਏ।",
        'master_password_remove': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਹਟਾਓ",
        'master_password_remove_confirm': "ਕੀ ਤੁਸੀਂ ਪੱਕਾ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਕਿ ਤੁਸੀਂ ਸਾਰੇ ਪਾਸਵਰਡ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?\n\nਇਹ ਕਿਰਿਆ ਅਟੱਲ ਹੈ!",
        'master_password_export_before': "ਕੀ ਤੁਸੀਂ ਪਹਿਲਾਂ ਇੱਕ ਬੈਕਅੱਪ ਕਾਪੀ ਐਕਸਪੋਰਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'master_password_export_delete': "ਐਕਸਪੋਰਟ ਕਰੋ ਅਤੇ ਮਿਟਾਓ",
        'master_password_delete_now': "ਹੁਣੇ ਮਿਟਾਓ",
        'master_password_for_signatures': "ਦਸਤਖਤ ਵਰਤਣ ਲਈ, ਤੁਹਾਨੂੰ ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣੇ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'master_password_for_private': "ਨਿੱਜੀ ਟੈਕਸਟ ਬਲਾਕ ਵਰਤਣ ਲਈ, ਤੁਹਾਨੂੰ ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣੇ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'master_password_info': """
            <b>🔐 ਮਾਸਟਰ ਪਾਸਵਰਡ ਤੋਂ ਬਿਨਾਂ:</b><br>
            • ਪਾਸਵਰਡ ਵੇਖਣਾ, ਕਾਪੀ ਕਰਨਾ ਅਤੇ ਐਕਸਪੋਰਟ ਕਰਨਾ ਸੰਭਵ ਨਹੀਂ<br>
            • ਪਾਸਵਰਡ ਮਿਟਾਉਣਾ ਹਮੇਸ਼ਾ ਸੰਭਵ ਹੈ (ਮਾਸਟਰ ਪਾਸਵਰਡ ਤੋਂ ਬਿਨਾਂ ਵੀ)<br><br>

            <b>🔐 ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ:</b><br>
            • ਪ੍ਰਮਾਣੀਕਰਨ ਤੋਂ ਬਾਅਦ ਸਾਰੇ ਫੰਕਸ਼ਨ ਉਪਲਬਧ<br>
            • ਪਾਸਵਰਡ ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ ਐਨਕ੍ਰਿਪਟ ਕੀਤੇ ਜਾਂਦੇ ਹਨ<br>
            • ਘੱਟੋ-ਘੱਟ ਲੰਬਾਈ: 8 ਅੱਖਰ<br>
            • ਸੁਰੱਖਿਅਤ SHA-256 ਹੈਸ਼ ਸਟੋਰੇਜ<br><br>

            <b>ਮਹੱਤਵਪੂਰਨ:</b><br>
            • ਮਾਸਟਰ ਪਾਸਵਰਡ ਗੁਆਉਣ ਤੇ: ਪਾਸਵਰਡ ਮੁੜ ਪ੍ਰਾਪਤ ਨਹੀਂ ਕੀਤੇ ਜਾ ਸਕਦੇ<br>
            • ਮਾਸਟਰ ਪਾਸਵਰਡ ਹਟਾਉਣ ਤੇ: ਸਾਰੇ ਪਾਸਵਰਡ ਮਿਟਾ ਦਿੱਤੇ ਜਾਣਗੇ<br>
            • ਮਿਟਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਐਕਸਪੋਰਟ ਵਿਕਲਪ ਉਪਲਬਧ<br>
            • ਮਾਸਟਰ ਪਾਸਵਰਡ ਕਿਸੇ ਵੀ ਸਮੇਂ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ
        """,
        'signature_auth_disabled': "ਦਸਤਖਤਾਂ ਲਈ ਪਾਸਵਰਡ ਪੁੱਛਣਾ ਅਸਮਰੱਥ ਕਰੋ",
        'template_auth_disabled': "ਨਿੱਜੀ ਟੈਕਸਟ ਬਲਾਕਾਂ ਲਈ ਪਾਸਵਰਡ ਪੁੱਛਣਾ ਅਸਮਰੱਥ ਕਰੋ",
        'master_password_for_signatures_settings': "ਦਸਤਖਤ ਵਰਤਣ ਲਈ, ਤੁਹਾਨੂੰ ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।\n\nਇਸ ਲਈ ਸੈਟਿੰਗਾਂ - ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ ਤੇ ਜਾਓ",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰੋ",
        'protect_info': "ਫਾਈਲ '{0}' ਨੂੰ ਇੱਕ ਪਾਸਵਰਡ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਵੇਗਾ।",
        'protect_instruction': "ਕਿਰਪਾ ਕਰਕੇ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ ਇੱਛਤ ਪਾਸਵਰਡ ਦੋ ਵਾਰ ਟਾਈਪ ਕਰੋ, ਜਾਂ ਇਨਪੁਟ ਫੀਲਡ ਦੇ ਸੱਜੇ ਪਾਸੇ ਵਾਲੇ ਪਾਸਵਰਡ ਜਨਰੇਟਰ ਦੀ ਵਰਤੋਂ ਕਰੋ।",
        'protect_success': "PDF ਨੂੰ ਸਫਲਤਾਪੂਰਵਕ ਸੁਰੱਖਿਅਤ ਕਰਕੇ ਇਸ ਵਿੱਚ ਸੰਭਾਲਿਆ ਗਿਆ:\n{0}\n\nਪਾਸਵਰਡ: {1}\n\nਕੀ ਤੁਸੀਂ ਹੁਣ ਸੁਰੱਖਿਅਤ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'protect_open': "ਹਾਂ",
        'protect_skip': "ਨਹੀਂ",
        'protect_error': "PDF ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਵੇਲੇ ਗਲਤੀ",
        'protect_open_title': "ਸੁਰੱਖਿਅਤ PDF ਖੋਲ੍ਹੋ",
        'protect_question': "ਮੁਕੰਮਲ। ਕੀ ਤੁਸੀਂ ਹੁਣ ਸੁਰੱਖਿਅਤ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ? ਹਾਂ ਜਾਂ ਨਹੀਂ?",
        'password_cancel': "ਪਾਸਵਰਡ ਡਾਇਲਾਗ ਰੱਦ ਕੀਤਾ ਗਿਆ",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "ਪੰਨੇ ਮਿਟਾਓ",
        'pages_extract': "ਪੰਨੇ ਕੱਢੋ",
        'pages_insert': "ਪੰਨੇ ਪਾਓ",
        'pages_move': "ਪੰਨੇ ਹਿਲਾਓ",
        'pages_delete_options': "ਮਿਟਾਉਣ ਦੇ ਵਿਕਲਪ",
        'pages_delete_empty': "ਸਾਰੇ ਖਾਲੀ ਪੰਨੇ ਮਿਟਾਓ",
        'pages_delete_current': "ਮੌਜੂਦਾ ਪੰਨਾ ਮਿਟਾਓ",
        'pages_delete_range': "ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ ਮਿਟਾਓ",
        'pages_extract_options': "ਕੱਢਣ ਦੇ ਵਿਕਲਪ",
        'pages_extract_current': "ਮੌਜੂਦਾ ਪੰਨਾ ਕੱਢੋ",
        'pages_extract_range': "ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ ਕੱਢੋ",
        'pages_insert_position': "ਪਾਉਣ ਦੀ ਸਥਿਤੀ",
        'pages_insert_before': "ਪੰਨੇ ਤੋਂ ਪਹਿਲਾਂ ਪਾਓ:",
        'pages_insert_select': "PDF ਚੁਣੋ",
        'pages_insert_none': "ਕੋਈ PDF ਨਹੀਂ ਚੁਣੀ ਗਈ",
        'pages_move_source': "ਹਿਲਾਉਣ ਲਈ ਪੰਨੇ",
        'pages_move_from': "ਪੰਨੇ ਤੋਂ:",
        'pages_move_to': "ਪੰਨੇ ਤੱਕ:",
        'pages_move_target': "ਟੀਚਾ ਸਥਿਤੀ",
        'pages_move_before': "ਪੰਨੇ ਤੋਂ ਪਹਿਲਾਂ ਹਿਲਾਓ:",
        'pages_move_hint': "ਨੋਟ: ਪੰਨਾ 1 = ਸ਼ੁਰੂਆਤ, {0} = ਅੰਤ",
        'pages_range_invalid': "ਸ਼ੁਰੂਆਤੀ ਪੰਨਾ ਅੰਤਮ ਪੰਨੇ ਤੋਂ ਛੋਟਾ ਜਾਂ ਬਰਾਬਰ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।",
        'pages_position_invalid': "ਟੀਚਾ ਸਥਿਤੀ ਹਿਲਾਉਣ ਵਾਲੀ ਰੇਂਜ ਦੇ ਅੰਦਰ ਨਹੀਂ ਹੋ ਸਕਦੀ।",
        'pages_no_pdf_selected': "ਕੋਈ PDF ਨਹੀਂ ਚੁਣੀ ਗਈ।",
        'pages_deleted': "{0} ਪੰਨੇ ਮਿਟਾ ਦਿੱਤੇ ਗਏ।",
        'pages_extracted': "ਕੱਢੇ ਗਏ: {0}\nਸੰਭਾਲੇ ਗਏ: {1}\nਫਾਈਲ ਦਾ ਆਕਾਰ: {2:.1f} KB",
        'pages_inserted': "{0} ਪੰਨੇ ਪਾ ਦਿੱਤੇ ਗਏ",
        'pages_moved': "{0} ਪੰਨੇ ਹਿਲਾ ਦਿੱਤੇ ਗਏ।",
        'pages_deleted_none': "ਕੋਈ ਪੰਨਾ ਨਹੀਂ ਮਿਟਾਇਆ ਗਿਆ।",
        'pages_delete_progress': "ਪੰਨੇ ਮਿਟਾਏ ਜਾ ਰਹੇ ਹਨ...",
        'pages_deleted_with_backup': "{0} ਪੰਨੇ ਮਿਟਾ ਦਿੱਤੇ ਗਏ।\n\nਬੈਕਅੱਪ: {1}",
        'pages_deleted_voice': "ਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ ਅਤੇ {0} ਪੰਨੇ ਮਿਟਾ ਦਿੱਤੇ ਗਏ।",
        'info': "ਨੋਟ",
        'error_dialog_creation': "ਡਾਇਲਾਗ ਨਹੀਂ ਬਣਾਇਆ ਜਾ ਸਕਿਆ",
        'extract_page_single': "ਪੰਨਾ {0} ਕੱਢੋ",
        'extract_page_range': "ਪੰਨੇ {0}-{1} ਕੱਢੋ",
        'extract_success_voice': "ਪੰਨੇ ਸਫਲਤਾਪੂਰਵਕ ਕੱਢੇ ਗਏ",
        'extract_error_format': "ਕੱਢਣ ਵੇਲੇ ਗਲਤੀ: {0}",
        'pages_inserted_voice': "{0} ਪੰਨੇ ਪਾ ਦਿੱਤੇ ਗਏ।",
        'insert_error_format': "ਪਾਉਣ ਵੇਲੇ ਗਲਤੀ: {0}",
        'pages_move_progress': "ਪੰਨੇ ਹਿਲਾਏ ਜਾ ਰਹੇ ਹਨ...",
        'pages_moved_with_backup': "{0} ਪੰਨੇ ਹਿਲਾ ਦਿੱਤੇ ਗਏ।\n\nਬੈਕਅੱਪ: {1}",
        'move_success_title': "ਸਫਲਤਾਪੂਰਵਕ ਹਿਲਾਏ ਗਏ",
        'pages_moved_voice': "{0} ਪੰਨੇ ਸਫਲਤਾਪੂਰਵਕ ਹਿਲਾਏ ਗਏ",
        'mark_removed': "ਪੰਨਾ {0} ਤੋਂ ਨਿਸ਼ਾਨ ਹਟਾਇਆ ਗਿਆ",
        'mark_empty': "ਪੰਨਾ {0} ਖਾਲੀ ਵਜੋਂ ਨਿਸ਼ਾਨਬੱਧ ਕੀਤਾ ਗਿਆ",
        'mark_export_removed': "ਪੰਨਾ {0} ਤੋਂ ਐਕਸਪੋਰਟ ਨਿਸ਼ਾਨ ਹਟਾਇਆ ਗਿਆ",
        'mark_export': "ਪੰਨਾ {0} ਐਕਸਪੋਰਟ ਲਈ ਨਿਸ਼ਾਨਬੱਧ ਕੀਤਾ ਗਿਆ",
        'no_empty_pages': "ਮਿਟਾਉਣ ਲਈ ਕੋਈ ਖਾਲੀ ਪੰਨਾ ਨਿਸ਼ਾਨਬੱਧ ਨਹੀਂ",
        'delete_empty_confirm': "ਕੀ ਤੁਸੀਂ ਸਾਰੇ {0} ਨਿਸ਼ਾਨਬੱਧ ਖਾਲੀ ਪੰਨੇ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'delete_empty_confirm_voice': "ਹੁਣ ਸਾਰੇ {0} ਨਿਸ਼ਾਨਬੱਧ ਖਾਲੀ ਪੰਨੇ ਮਿਟਾਉਣੇ ਹਨ? ਹਾਂ ਜਾਂ ਨਹੀਂ।",
        'empty_pages_deleted': "{0} ਖਾਲੀ ਪੰਨੇ ਮਿਟਾ ਦਿੱਤੇ ਗਏ",
        'no_export_pages': "ਐਕਸਪੋਰਟ ਲਈ ਕੋਈ ਪੰਨਾ ਨਿਸ਼ਾਨਬੱਧ ਨਹੀਂ",
        'overwrite_title': "ਮੌਜੂਦਾ ਫਾਈਲ ਨੂੰ ਓਵਰਰਾਈਟ ਕਰੋ",
        'overwrite_question': "ਫਾਈਲ\n\n{0}\n\nਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਹੈ।\nਕੀ ਤੁਸੀਂ ਇਸਨੂੰ ਓਵਰਰਾਈਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'overwrite_voice': "ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਫਾਈਲ ਨੂੰ ਓਵਰਰਾਈਟ ਕਰਨਾ ਹੈ? ਹਾਂ ਜਾਂ ਨਹੀਂ।",
        'page_skipped': "ਪੰਨਾ {0} ਛੱਡ ਦਿੱਤਾ ਗਿਆ",
        'export_complete': "ਐਕਸਪੋਰਟ ਮੁਕੰਮਲ।",
        'export_complete_voice': "ਐਕਸਪੋਰਟ ਮੁਕੰਮਲ ਹੋ ਗਿਆ।",
        'no_pages_exported': "ਕੋਈ ਪੰਨਾ ਐਕਸਪੋਰਟ ਨਹੀਂ ਕੀਤਾ ਗਿਆ",
        'export_cancelled': "ਐਕਸਪੋਰਟ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'pages_exported': "{0} ਪੰਨੇ {1} ਵਿੱਚ ਐਕਸਪੋਰਟ ਕੀਤੇ ਗਏ",
        'export_page_title': "ਪੰਨਾ ਐਕਸਪੋਰਟ ਕਰੋ",
        'page_exported': "ਪੰਨਾ {0} {1} ਵਿੱਚ ਐਕਸਪੋਰਟ ਕੀਤਾ ਗਿਆ",
        'export_error': "ਐਕਸਪੋਰਟ ਕਰਨ ਵੇਲੇ ਗਲਤੀ",
        'export_marked_title': "ਨਿਸ਼ਾਨਬੱਧ ਪੰਨੇ ਐਕਸਪੋਰਟ ਕਰੋ",
        'rotate_all_title': "ਸਾਰੇ ਪੰਨੇ ਘੁਮਾਓ",
        'rotate_all_question': "ਕੀ ਤੁਸੀਂ ਸਾਰੇ ਪੰਨੇ 90 ਡਿਗਰੀ ਸੱਜੇ ਪਾਸੇ ਘੁਮਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'rotate_all_voice': "ਕੀ ਤੁਸੀਂ ਸਾਰੇ ਪੰਨੇ 90 ਡਿਗਰੀ ਸੱਜੇ ਪਾਸੇ ਘੁਮਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ? ਹਾਂ ਜਾਂ ਨਹੀਂ?",
        'all_pages_rotated': "ਸਾਰੇ ਪੰਨੇ ਘੁਮਾ ਦਿੱਤੇ ਗਏ",
        'page_rotated': "ਪੰਨਾ {0} ਘੁਮਾ ਦਿੱਤਾ ਗਿਆ",
        'rotate_error': "ਪੰਨਾ ਨਹੀਂ ਘੁਮਾਇਆ ਜਾ ਸਕਿਆ",
        'delete_page_confirm': "ਕੀ ਤੁਸੀਂ ਪੰਨਾ {0} ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'delete_page_confirm_voice': "ਕੀ ਤੁਸੀਂ ਸੱਚਮੁੱਚ ਪੰਨਾ {0} ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ? ਹਾਂ ਜਾਂ ਨਹੀਂ।",
        'page_deleted': "ਪੰਨਾ {0} ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ",
        'delete_error': "ਪੰਨਾ ਨਹੀਂ ਮਿਟਾਇਆ ਜਾ ਸਕਿਆ",
        'pages_deleted_voice': "{0} ਪੰਨੇ ਮਿਟਾ ਦਿੱਤੇ ਗਏ",
        'pages_exported_split': "{0} ਪੰਨੇ ਸਫਲਤਾਪੂਰਵਕ ਐਕਸਪੋਰਟ ਕੀਤੇ ਗਏ।",
        'pages_skipped': "{0} ਪੰਨੇ ਛੱਡ ਦਿੱਤੇ ਗਏ।",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "ਪੰਨੇ ਕੱਢੋ (ਉੱਨਤ)",
        'pdf_splitter_title': "PDF ਸਪਲਿਟਰ ਅਤੇ ਐਕਸਟ੍ਰੈਕਟਰ",
        'pdf_splitter_load': " PDF ਫਾਈਲ ਚੁਣੋ",
        'pdf_splitter_info': "ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੇ PDF ਦਸਤਾਵੇਜ਼ ਲਈ ਇੱਕ ਵਿਕਲਪ ਚੁਣੋ",
        'pdf_splitter_basic': "ਮੁੱਢਲੀਆਂ ਕਾਰਵਾਈਆਂ",
        'pdf_splitter_single': "ਹਰੇਕ ਪੰਨੇ ਨੂੰ ਵੱਖਰੀ ਫਾਈਲ ਵਿੱਚ ਵੰਡੋ",
        'pdf_splitter_range': "ਪੰਨੇ ਕੱਢੋ:",
        'pdf_splitter_range_placeholder': "ਉਦਾ. 1-3,5,7-9",
        'pdf_splitter_clean': "ਸਫਾਈ ਕਾਰਵਾਈਆਂ",
        'pdf_splitter_remove_empty': "ਸਾਰੇ ਖਾਲੀ ਪੰਨੇ ਹਟਾਓ",
        'pdf_splitter_remove': "ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ ਮਿਟਾਓ:",
        'pdf_splitter_remove_placeholder': "ਉਦਾ. 2,4-6",
        'pdf_splitter_process': "PDF ਪ੍ਰਕਿਰਿਆ ਕਰੋ",
        'pdf_splitter_loaded': "PDF ਲੋਡ ਕੀਤੀ ਗਈ। ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ ਵਿਕਲਪ ਚੁਣੋ",
        'pdf_read_error': "PDF ਨਹੀਂ ਪੜ੍ਹੀ ਜਾ ਸਕੀ",
        'pages': "ਪੰਨੇ",
        'pages_created': "ਪੰਨੇ ਬਣਾਏ ਗਏ",
        'range_empty': "ਕਿਰਪਾ ਕਰਕੇ ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ ਟਾਈਪ ਕਰੋ",
        'range_invalid': "ਅਵੈਧ ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ",
        'range_created': "ਚੁਣੇ ਗਏ ਪੰਨਿਆਂ ਨਾਲ ਨਵੀਂ PDF ਬਣਾਈ ਗਈ:\n{0}",
        'empty_removed': "{0} ਖਾਲੀ ਪੰਨੇ ਹਟਾ ਦਿੱਤੇ ਗਏ।\nਆਉਟਪੁੱਟ: {1}",
        'remove_empty': "ਕਿਰਪਾ ਕਰਕੇ ਹਟਾਉਣ ਲਈ ਪੰਨੇ ਟਾਈਪ ਕਰੋ",
        'remove_invalid': "ਹਟਾਉਣ ਲਈ ਅਵੈਧ ਪੰਨੇ",
        'remove_done': "ਸਾਫ਼ ਕੀਤੀ PDF ਬਣਾਈ ਗਈ:\n{0}",
        'open_folder': "ਫੋਲਡਰ ਖੋਲ੍ਹੋ",
        'show_in_finder': "ਫਾਈਂਡਰ ਵਿੱਚ ਦਿਖਾਓ",
        'pdf_splitter_no_pdf': "ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਇੱਕ PDF ਫਾਈਲ ਲੋਡ ਕਰੋ।",
        'process_error': "PDF ਪ੍ਰਕਿਰਿਆ ਕਰਨ ਵੇਲੇ ਗਲਤੀ",
        'pages_created_voice': "{0} ਪੰਨੇ ਬਣਾਏ ਗਏ",
        'range_created_voice': "ਚੁਣੇ ਗਏ ਪੰਨਿਆਂ ਨਾਲ PDF ਬਣਾਈ ਗਈ",
        'empty_removed_voice': "{0} ਖਾਲੀ ਪੰਨੇ ਹਟਾ ਦਿੱਤੇ ਗਏ",
        'remove_done_voice': "ਸਾਫ਼ ਕੀਤੀ PDF ਬਣਾਈ ਗਈ",
        'pdf_splitter_split_groups': "ਹਰੇਕ ਲਗਾਤਾਰ ਸਮੂਹ ਨੂੰ ਵੱਖਰੀ ਫਾਈਲ ਵਿੱਚ",
        'range_created_single': "ਨਵੀਂ PDF ਬਣਾਈ ਗਈ:\n{0}",
        'range_created_multiple': "{0} PDF ਫਾਈਲਾਂ ਬਣਾਈਆਂ ਗਈਆਂ।",
        'range_created_voice_single': "ਚੁਣੇ ਗਏ ਪੰਨਿਆਂ ਨਾਲ ਇੱਕ PDF ਬਣਾਈ ਗਈ",
        'range_created_voice_multiple': "{0} PDF ਫਾਈਲਾਂ ਬਣਾਈਆਂ ਗਈਆਂ",
        'empty_removed_none_left': "ਕੋਈ ਪੰਨਾ ਬਾਕੀ ਨਹੀਂ",
        'empty_removed_all_empty': "ਸਾਰੇ ਪੰਨੇ ਖਾਲੀ ਵਜੋਂ ਪਛਾਣੇ ਗਏ ਅਤੇ ਹਟਾ ਦਿੱਤੇ ਜਾਣਗੇ। ਕੋਈ ਫਾਈਲ ਨਹੀਂ ਬਣਾਈ ਗਈ।",
        'preview_single': "ਪੂਰਵ ਦਰਸ਼ਨ: {0}",
        'preview_enter_range': "ਕਿਰਪਾ ਕਰਕੇ ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ ਟਾਈਪ ਕਰੋ।",
        'preview_invalid_range': "ਅਵੈਧ ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ।",
        'preview_file': "ਪੂਰਵ ਦਰਸ਼ਨ: {0}",
        'preview_files': "ਪੂਰਵ ਦਰਸ਼ਨ: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "ਛਪਾਈ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ",
        'print_sent': "ਛਪਾਈ ਕੰਮ ਭੇਜਿਆ ਗਿਆ",
        'print_now': "ਹੁਣੇ ਛਾਪੋ",
        'print_error': "ਤੁਰੰਤ ਛਪਾਈ ਵਿੱਚ ਗਲਤੀ",
        'print_limited': "ਇਸ ਸਿਸਟਮ ਤੇ ਛਪਾਈ ਫੰਕਸ਼ਨ ਸੀਮਤ ਹੈ",
        'print_error_format': "ਤੁਰੰਤ ਛਪਾਈ ਵਿੱਚ ਗਲਤੀ: {0}",
        'warning': "ਨੋਟ",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "ਹਲਕੇ ਮੋਡ ਵਿੱਚ ਬਦਲੋ",
        'mode_switch_to_dark': "ਡਾਰਕ ਮੋਡ ਵਿੱਚ ਬਦਲੋ",
        'mode_dark_activated': "ਡਾਰਕ ਮੋਡ ਸਰਗਰਮ",
        'mode_light_activated': "ਹਲਕਾ ਮੋਡ ਸਰਗਰਮ",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "ਪੂਰਾ ਦ੍ਰਿਸ਼",
        'zoom_two_pages': "ਦੋ ਪੰਨੇ ਇਕ ਦੂਜੇ ਨਾਲ",
        'zoom_overview': "ਸੰਖੇਪ ਮੋਡ",
        'zoom_cannot_during_search': "ਖੋਜ ਦੌਰਾਨ ਜ਼ੂਮ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ",
        'zoom_exit_first': "ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਜ਼ੂਮ ਬੰਦ ਕਰੋ",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "ਡ੍ਰੈਗ ਐਂਡ ਡ੍ਰੌਪ ਸਰਗਰਮ",
        'drag_disabled': "ਡ੍ਰੈਗ ਐਂਡ ਡ੍ਰੌਪ ਅਸਰਗਰਮ",
        'drag_page_grab': "ਪੰਨਾ {0} ਫੜਿਆ ਜਾ ਰਿਹਾ ਹੈ",
        'drag_page_dropped': "ਪੰਨਾ {0} ਸਥਿਤੀ {1} ਤੇ ਪਾ ਦਿੱਤਾ ਗਿਆ",
        'drag_position_invalid': "ਅਵੈਧ ਸਥਿਤੀ",
        'drag_same_position': "ਪੰਨਾ {0} ਸਥਿਤੀ {0} ਤੇ ਰਹਿੰਦਾ ਹੈ",
        'drag_error': "ਹਿਲਾਉਣ ਵੇਲੇ ਗਲਤੀ",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "ਉੱਨਤ ਫਾਰਮੈਟਿੰਗ ਅਤੇ ਟੈਕਸਟ ਬਲਾਕ ਪ੍ਰਬੰਧਨ ਦੇ ਨਾਲ ਟੈਕਸਟ ਇਨਪੁਟ",
        'text_templates': "ਉਪਲਬਧ ਟੈਕਸਟ ਬਲਾਕ:",
        'text_name': "ਨਾਂ",
        'text_preview': "ਟੈਕਸਟ ਪੂਰਵ ਦਰਸ਼ਨ",
        'text_enter': "ਟੈਕਸਟ:",
        'text_font_size': "ਫੌਂਟ ਦਾ ਆਕਾਰ:",
        'text_formatting': "ਫਾਰਮੈਟਿੰਗ:",
        'text_bold': "ਬੋਲਡ",
        'text_italic': "ਤਿਰਛਾ",
        'text_underline': "ਰੇਖਾਂਕਿਤ",
        'text_alignment': "ਇਕਸਾਰਤਾ:",
        'text_left': "ਖੱਬੇ",
        'text_center': "ਕੇਂਦਰ ਵਿੱਚ",
        'text_right': "ਸੱਜੇ",
        'text_color': "ਟੈਕਸਟ ਰੰਗ:",
        'text_opacity': "ਅਪਾਰਦਰਸ਼ਤਾ:",
        'text_word_wrap': "ਲਾਈਨ ਬ੍ਰੇਕ:",
        'text_auto': "ਆਟੋਮੈਟਿਕ",
        'text_page_width_95': "ਪੰਨੇ ਦੀ ਚੌੜਾਈ (95%)",
        'text_page_width_85': "ਬਹੁਤ ਚੌੜਾ (85%)",
        'text_page_width_75': "ਚੌੜਾ (75%)",
        'text_page_width_60': "ਚੌੜਾ (60%)",
        'text_page_width_50': "ਮੱਧਮ (50%)",
        'text_page_width_30': "ਤੰਗ (30%)",
        'text_page_width_20': "ਤੰਗ (20%)",
        'text_page_width_10': "ਬਹੁਤ ਤੰਗ (10%)",
        'text_no_wrap': "ਕੋਈ ਬ੍ਰੇਕ ਨਹੀਂ",
        'text_private': "ਨਿੱਜੀ ਟੈਕਸਟ ਬਲਾਕ (ਪ੍ਰਮਾਣੀਕਰਨ ਦੀ ਲੋੜ ਹੈ)",
        'text_preview_label': "ਪੂਰਵ ਦਰਸ਼ਨ:",
        'text_preview_placeholder': "ਇੱਥੇ ਟੈਕਸਟ ਦਾ ਪੂਰਵ ਦਰਸ਼ਨ ਦਿਖਾਇਆ ਜਾਵੇਗਾ...",
        'text_no_text': "(ਕੋਈ ਟੈਕਸਟ ਨਹੀਂ)",
        'text_save_template': "💾 ਬਲਾਕ ਵਜੋਂ ਸੰਭਾਲੋ",
        'text_delete_template': "🗑 ਚੁਣਿਆ ਟੈਕਸਟ ਬਲਾਕ ਮਿਟਾਓ",
        'text_show_private': "ਨਿੱਜੀ ਦਿਖਾਓ",
        'text_hide_private': "ਨਿੱਜੀ ਲੁਕਾਓ",
        'text_use': "✅ ਟੈਕਸਟ ਵਰਤੋਂ",
        'text_saved': "ਟੈਕਸਟ ਬਲਾਕ ਵਜੋਂ ਸੰਭਾਲਿਆ ਗਿਆ:\n{0}",
        'text_saved_voice': "ਟੈਕਸਟ ਬਲਾਕ ਸੰਭਾਲਿਆ ਗਿਆ",
        'text_deleted': "ਟੈਕਸਟ ਬਲਾਕ ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ",
        'text_no_text_to_save': "ਸੰਭਾਲਣ ਲਈ ਕੋਈ ਟੈਕਸਟ ਨਹੀਂ।",
        'text_no_templates': "ਕੋਈ ਟੈਕਸਟ ਬਲਾਕ ਨਹੀਂ ਮਿਲਿਆ",
        'text_private_master_required': "ਨਿੱਜੀ ਬਲਾਕ ਸਿਰਫ ਉਦੋਂ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜੇਕਰ ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕੀਤਾ ਗਿਆ ਹੋਵੇ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣੇ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'text_filename': "ਟੈਕਸਟ ਬਲਾਕ ਲਈ ਫਾਈਲ ਦਾ ਨਾਂ ('Text_' ਅਤੇ '.txt' ਤੋਂ ਬਿਨਾਂ):",
        'text_filename_hint': "ਉਦਾਹਰਨ: 'Telefon HomeOffice' 'Text_Telefon HomeOffice.txt' ਵਜੋਂ ਸੰਭਾਲਿਆ ਜਾਵੇਗਾ",
        'text_save_hint': "ਟੈਕਸਟ ਬਲਾਕ ਆਪਣੇ ਆਪ ਫਾਰਮੈਟਿੰਗ ਦੇ ਨਾਲ ਸੰਭਾਲਿਆ ਜਾਵੇਗਾ।",
        'text_guide_title': "ਟੈਕਸਟ ਇਨਪੁਟ - ਮਾਰਗਦਰਸ਼ਨ",
        'text_delete_confirm': "ਕੀ ਤੁਸੀਂ ਸੱਚਮੁੱਚ ਟੈਕਸਟ ਬਲਾਕ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?\n\nਫਾਈਲ: {0}\nਟੈਕਸਟ: {1}...",
        'text_make_public': "ਜਨਤਕ ਵਜੋਂ ਨਿਸ਼ਾਨਬੱਧ ਕਰੋ",
        'text_make_private': "ਨਿੱਜੀ ਵਜੋਂ ਨਿਸ਼ਾਨਬੱਧ ਕਰੋ",
        'text_privacy_changed': "ਪਰਾਈਵੇਸੀ ਸਥਿਤੀ ਬਦਲੀ ਗਈ",
        'text_private_always': "ਨਿੱਜੀ ਹਮੇਸ਼ਾ ਦਿਖਾਈ ਦੇਣ (ਸੈਟਿੰਗ)",
        'text_mode_required': "ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਟੈਕਸਟ ਮੋਡ ਸਰਗਰਮ ਕਰੋ",
        'text_continue_editing': "ਸੰਪਾਦਨ ਜਾਰੀ ਰੱਖੋ - ਕਰਸਰ ਟੈਕਸਟ ਦੇ ਅੰਤ ਤੇ",
        'text_no_input': "ਕੋਈ ਟੈਕਸਟ ਟਾਈਪ ਨਹੀਂ ਕੀਤਾ ਗਿਆ - ਟੈਕਸਟ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'save_dialog_question': "ਤੁਸੀਂ ਕਿਵੇਂ ਅੱਗੇ ਵਧਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'text_save_question': "ਸਾਰੇ ਟੈਕਸਟ ਅਤੇ ਕਰਾਸ ਸੰਭਾਲੋ, ਵਿਵਸਥਿਤ ਕਰੋ, ਸੰਪਾਦਨ ਜਾਰੀ ਰੱਖੋ ਜਾਂ ਰੱਦ ਕਰੋ?",
        'copy_cross': "ਕਰਾਸ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'paste_cross': "ਕਰਾਸ ਪੇਸਟ ਕੀਤਾ ਗਿਆ",
        'paste_text': "ਟੈਕਸਟ ਪੇਸਟ ਕੀਤਾ ਗਿਆ",
        'cross_discarded': "ਕਰਾਸ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'all_discarded': "ਸਭ ਰੱਦ ਕੀਤੇ ਗਏ",
        'text_discarded': "ਟੈਕਸਟ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'no_texts_to_save': "ਸੰਭਾਲਣ ਲਈ ਕੋਈ ਟੈਕਸਟ ਨਹੀਂ",
        'no_valid_texts': "ਸੰਭਾਲਣ ਲਈ ਕੋਈ ਵੈਧ ਟੈਕਸਟ ਨਹੀਂ",
        'text_word_singular': "ਟੈਕਸਟ",
        'text_word_plural': "ਟੈਕਸਟ",
        'cross_word_singular': "ਕਰਾਸ",
        'cross_word_plural': "ਕਰਾਸ",
        'texts_saved_title': "ਟੈਕਸਟ ਸੰਭਾਲੇ ਗਏ",
        'texts_crosses_saved': "{0} {1} ਅਤੇ {2} {3} PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'texts_crosses_saved_voice': "{0} {1} ਅਤੇ {2} {3} ਸੰਭਾਲੇ ਗਏ।",
        'texts_saved': "{0} {1} PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'texts_saved_voice': "{0} {1} ਸੰਭਾਲੇ ਗਏ।",
        'crosses_saved': "{0} {1} PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'crosses_saved_voice': "{0} {1} ਸੰਭਾਲੇ ਗਏ।",
        'elements_saved': "{0} ਤੱਤ PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'elements_saved_voice': "{0} ਤੱਤ ਸੰਭਾਲੇ ਗਏ।",
        'text_window_load_error': "ਟੈਕਸਟ ਵਿੰਡੋ ਲੋਡ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕੀ",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **ਟੈਕਸਟ ਇਨਪੁਟ ਅਤੇ ਟੈਕਸਟ ਬਲਾਕ – ਵਿਸਤ੍ਰਿਤ ਮਾਰਗਦਰਸ਼ਨ**

        **1. ਟੈਕਸਟ ਪਾਓ ਅਤੇ ਸੰਪਾਦਿਤ ਕਰੋ**
        - ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਲੋੜੀਂਦੀ ਥਾਂ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰੋ ਅਤੇ "ਟੈਕਸਟ ਪਾਓ" ਚੁਣੋ।
        - ਇੱਕ ਡਾਇਲਾਗ ਖੁਲ੍ਹੇਗਾ ਜਿੱਥੇ ਤੁਸੀਂ ਆਪਣਾ ਟੈਕਸਟ ਟਾਈਪ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਫਾਰਮੈਟ ਕਰ ਸਕਦੇ ਹੋ:
        • ਫੌਂਟ ਦਾ ਆਕਾਰ, ਬੋਲਡ, ਤਿਰਛਾ, ਰੇਖਾਂਕਿਤ
        • ਟੈਕਸਟ ਰੰਗ (ਮੁਫ਼ਤ ਚੋਣਯੋਗ)
        • ਸਲਾਈਡਰ ਰਾਹੀਂ ਪਾਰਦਰਸ਼ਤਾ (ਅਪਾਰਦਰਸ਼ਤਾ)
        • ਲਾਈਨ ਬ੍ਰੇਕ (ਵੱਖ-ਵੱਖ ਚੌੜਾਈਆਂ, ਜਿਵੇਂ ਪੰਨੇ ਦੀ ਚੌੜਾਈ, ਤੰਗ, ਕੋਈ ਬ੍ਰੇਕ ਨਹੀਂ)
        - ਪੁਸ਼ਟੀ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਟੈਕਸਟ ਕਲਿਕ ਕੀਤੀ ਥਾਂ ਤੇ ਦਿਖਾਈ ਦੇਵੇਗਾ। ਤੁਸੀਂ ਇਸਨੂੰ ਮਾਊਸ ਜਾਂ ਤੀਰ ਕੁੰਜੀਆਂ ਨਾਲ ਹਿਲਾ ਸਕਦੇ ਹੋ।
        - ਟੈਕਸਟ ਤੇ ਡਬਲ-ਕਲਿਕ ਕਰਨ ਨਾਲ ਸੰਪਾਦਨ ਮੋਡ ਖੁੱਲ੍ਹਦਾ ਹੈ; ESC ਨਾਲ ਤੁਸੀਂ ਇਸ ਤੋਂ ਬਾਹਰ ਆ ਸਕਦੇ ਹੋ।

        **2. ਟੈਕਸਟ ਬਲਾਕ (ਟੈਂਪਲੇਟ) ਪ੍ਰਬੰਧਿਤ ਕਰੋ**
        - ਟੈਕਸਟ ਡਾਇਲਾਗ ਵਿੱਚ ਤੁਸੀਂ ਖੱਬੇ ਪਾਸੇ ਸਾਰੇ ਸੰਭਾਲੇ ਗਏ ਟੈਕਸਟ ਬਲਾਕਾਂ ਦੀ ਸੂਚੀ ਵੇਖੋਗੇ।
        - **ਬਲਾਕ ਸੰਭਾਲਣਾ:** ਆਪਣਾ ਟੈਕਸਟ ਟਾਈਪ ਕਰੋ, ਫਾਰਮੈਟ ਕਰੋ ਅਤੇ "💾 ਬਲਾਕ ਵਜੋਂ ਸੰਭਾਲੋ" ਤੇ ਕਲਿਕ ਕਰੋ। ਇੱਕ ਫਾਈਲ ਨਾਂ ਟਾਈਪ ਕਰੋ (ਬਿਨਾਂ ਐਕਸਟੈਨਸ਼ਨ ਦੇ)।
        - **ਬਲਾਕ ਲੋਡ ਕਰਨਾ:** ਸੂਚੀ ਵਿੱਚ ਲੋੜੀਂਦੇ ਨਾਂ ਤੇ ਕਲਿਕ ਕਰੋ। ਟੈਕਸਟ ਅਤੇ ਫਾਰਮੈਟਿੰਗ ਲੈ ਲਈ ਜਾਵੇਗੀ ਅਤੇ ਲੋੜ ਅਨੁਸਾਰ ਵਿਵਸਥਿਤ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।
        - **ਮਿਟਾਉਣਾ:** ਇੱਕ ਬਲਾਕ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰਕੇ ਤੁਸੀਂ ਇਸਨੂੰ ਮਿਟਾ ਸਕਦੇ ਹੋ ਜਾਂ ਇਸਦੀ ਨਿੱਜੀ ਸਥਿਤੀ ਬਦਲ ਸਕਦੇ ਹੋ।

        **3. ਨਿੱਜੀ ਟੈਕਸਟ ਬਲਾਕ (ਮਾਸਟਰ ਪਾਸਵਰਡ)**
        - ਜੇਕਰ ਤੁਸੀਂ ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕੀਤਾ ਹੈ (ਸੈਟਿੰਗਾਂ → ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ ਦੇ ਅਧੀਨ), ਤੁਸੀਂ ਬਲਾਕਾਂ ਨੂੰ "ਨਿੱਜੀ" ਵਜੋਂ ਨਿਸ਼ਾਨਬੱਧ ਕਰ ਸਕਦੇ ਹੋ।
        - ਸੰਭਾਲਣ ਤੋਂ ਪਹਿਲਾਂ ਡਾਇਲਾਗ ਵਿੱਚ "ਨਿੱਜੀ ਟੈਕਸਟ ਬਲਾਕ" ਚੈਕਬਾਕਸ ਸਰਗਰਮ ਕਰੋ।
        - ਨਿੱਜੀ ਬਲਾਕ ਸੂਚੀ ਵਿੱਚ ਸਿਰਫ ਉਦੋਂ ਦਿਖਾਏ ਜਾਣਗੇ ਜਦੋਂ ਤੁਸੀਂ ਪ੍ਰਤੀ ਸੈਸ਼ਨ ਇੱਕ ਵਾਰ ਆਪਣਾ ਮਾਸਟਰ ਪਾਸਵਰਡ ਟਾਈਪ ਕੀਤਾ ਹੋਵੇ (ਲਾਕ ਆਈਕਨ ਰਾਹੀਂ ਜਾਂ ਪਹਿਲੀ ਪਹੁੰਚ ਤੇ ਪ੍ਰਮਾਣੀਕਰਨ)।
        - ਇਸ ਤਰ੍ਹਾਂ ਤੁਸੀਂ ਗੁਪਤ ਟੈਕਸਟ ਬਲਾਕਾਂ ਨੂੰ ਦੂਜਿਆਂ ਦੀ ਪਹੁੰਚ ਤੋਂ ਸੁਰੱਖਿਅਤ ਕਰ ਸਕਦੇ ਹੋ।

        **4. ਕਰਾਸ ਪਾਓ**
        - ਸੰਦਰਭ ਮੀਨੂ ਰਾਹੀਂ ਤੁਸੀਂ ਇੱਕ ਗ੍ਰਾਫਿਕਲ ਕਰਾਸ (ਜਿਵੇਂ ਚੈਕਬਾਕਸ ਲਈ) ਪਾ ਸਕਦੇ ਹੋ।
        - ਕਰਾਸ ਦਾ ਆਕਾਰ, ਲਾਈਨ ਦੀ ਮੋਟਾਈ ਅਤੇ ਰੰਗ ਤੁਸੀਂ ਸੈਟਿੰਗਾਂ ਵਿੱਚ ਗਲੋਬਲ ਤੌਰ ਤੇ ਵਿਵਸਥਿਤ ਕਰ ਸਕਦੇ ਹੋ (ਮੀਨੂ "ਸੈਟਿੰਗਾਂ" → "ਅੰਕਰੌਇਜ਼ੇਨ-ਸੈਟਿੰਗਾਂ")।
        - ਇੱਕ ਮੌਜੂਦਾ ਕਰਾਸ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰਕੇ ਤੁਸੀਂ ਇਸਨੂੰ ਵਿਅਕਤੀਗਤ ਤੌਰ ਤੇ ਬਦਲ ਸਕਦੇ ਹੋ।

        **5. ਸਮੂਹਿਕ ਕਾਰਵਾਈਆਂ**
        - ਜੇਕਰ ਤੁਸੀਂ ਇੱਕ ਪੰਨੇ ਤੇ ਕਈ ਟੈਕਸਟ ਜਾਂ ਕਰਾਸ ਰੱਖੇ ਹਨ, ਤਾਂ ਸੰਦਰਭ ਮੀਨੂ ਰਾਹੀਂ (ਟੈਕਸਟ ਮੋਡ ਵਿੱਚ ਸੱਜਾ-ਕਲਿਕ) ਤੁਸੀਂ ਸਾਰੇ ਤੱਤ ਇਕੱਠੇ ਸੰਭਾਲ ਸਕਦੇ ਹੋ ਜਾਂ ਰੱਦ ਕਰ ਸਕਦੇ ਹੋ।
        - ਸੰਭਾਲਣ ਵੇਲੇ ਸਾਰੇ ਤੱਤ PDF ਵਿੱਚ ਏਮਬੈਡ ਹੋ ਜਾਂਦੇ ਹਨ ਅਤੇ ਵੈਕਟਰ ਗ੍ਰਾਫਿਕ ਵਜੋਂ ਰਹਿੰਦੇ ਹਨ।

        **6. ਟੈਕਸਟ ਮੋਡ ਵਿੱਚ ਕੀਬੋਰਡ ਸ਼ਾਰਟਕੱਟ**
        - ਤੀਰ ਕੁੰਜੀਆਂ: ਤੱਤ ਹਿਲਾਓ
        - Ctrl+ਤੀਰ ਕੁੰਜੀਆਂ: ਵੱਡੇ ਕਦਮਾਂ ਨਾਲ ਹਿਲਾਓ
        - ਐਂਟਰ: ਸੰਭਾਲ ਡਾਇਲਾਗ ਖੋਲ੍ਹੋ (ਸਾਰੇ ਸੰਭਾਲੋ / ਵਿਵਸਥਿਤ ਕਰੋ / ਰੱਦ ਕਰੋ)
        - ESC: ਮੌਜੂਦਾ ਤੱਤ ਰੱਦ ਕਰੋ
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 ਟੈਕਸਟ ਇਨਪੁਟ ਅਤੇ ਟੈਕਸਟ ਬਲਾਕ – ਵਿਸਤ੍ਰਿਤ ਮਾਰਗਦਰਸ਼ਨ</strong></p>

        <p><strong>1. ਟੈਕਸਟ ਪਾਓ ਅਤੇ ਸੰਪਾਦਿਤ ਕਰੋ</strong></p>
        <ul>
        <li>ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਲੋੜੀਂਦੀ ਥਾਂ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰੋ ਅਤੇ "ਟੈਕਸਟ ਪਾਓ" ਚੁਣੋ।</li>
        <li>ਇੱਕ ਡਾਇਲਾਗ ਖੁਲ੍ਹੇਗਾ ਜਿੱਥੇ ਤੁਸੀਂ ਆਪਣਾ ਟੈਕਸਟ ਟਾਈਪ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਫਾਰਮੈਟ ਕਰ ਸਕਦੇ ਹੋ:<br/>
        • ਫੌਂਟ ਦਾ ਆਕਾਰ, ਬੋਲਡ, ਤਿਰਛਾ, ਰੇਖਾਂਕਿਤ<br/>
        • ਟੈਕਸਟ ਰੰਗ (ਮੁਫ਼ਤ ਚੋਣਯੋਗ)<br/>
        • ਸਲਾਈਡਰ ਰਾਹੀਂ ਪਾਰਦਰਸ਼ਤਾ (ਅਪਾਰਦਰਸ਼ਤਾ)<br/>
        • ਲਾਈਨ ਬ੍ਰੇਕ (ਵੱਖ-ਵੱਖ ਚੌੜਾਈਆਂ, ਜਿਵੇਂ ਪੰਨੇ ਦੀ ਚੌੜਾਈ, ਤੰਗ, ਕੋਈ ਬ੍ਰੇਕ ਨਹੀਂ)</li>
        <li>ਪੁਸ਼ਟੀ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਟੈਕਸਟ ਕਲਿਕ ਕੀਤੀ ਥਾਂ ਤੇ ਦਿਖਾਈ ਦੇਵੇਗਾ। ਤੁਸੀਂ ਇਸਨੂੰ ਮਾਊਸ ਜਾਂ ਤੀਰ ਕੁੰਜੀਆਂ ਨਾਲ ਹਿਲਾ ਸਕਦੇ ਹੋ।</li>
        <li>ਟੈਕਸਟ ਤੇ ਡਬਲ-ਕਲਿਕ ਕਰਨ ਨਾਲ ਸੰਪਾਦਨ ਮੋਡ ਖੁੱਲ੍ਹਦਾ ਹੈ; ESC ਨਾਲ ਤੁਸੀਂ ਇਸ ਤੋਂ ਬਾਹਰ ਆ ਸਕਦੇ ਹੋ।</li>
        </ul>

        <p><strong>2. ਟੈਕਸਟ ਬਲਾਕ (ਟੈਂਪਲੇਟ) ਪ੍ਰਬੰਧਿਤ ਕਰੋ</strong></p>
        <ul>
        <li>ਟੈਕਸਟ ਡਾਇਲਾਗ ਵਿੱਚ ਤੁਸੀਂ ਖੱਬੇ ਪਾਸੇ ਸਾਰੇ ਸੰਭਾਲੇ ਗਏ ਟੈਕਸਟ ਬਲਾਕਾਂ ਦੀ ਸੂਚੀ ਵੇਖੋਗੇ।</li>
        <li><strong>ਬਲਾਕ ਸੰਭਾਲਣਾ:</strong> ਆਪਣਾ ਟੈਕਸਟ ਟਾਈਪ ਕਰੋ, ਫਾਰਮੈਟ ਕਰੋ ਅਤੇ "💾 ਬਲਾਕ ਵਜੋਂ ਸੰਭਾਲੋ" ਤੇ ਕਲਿਕ ਕਰੋ। ਇੱਕ ਫਾਈਲ ਨਾਂ ਟਾਈਪ ਕਰੋ (ਬਿਨਾਂ ਐਕਸਟੈਨਸ਼ਨ ਦੇ)।</li>
        <li><strong>ਬਲਾਕ ਲੋਡ ਕਰਨਾ:</strong> ਸੂਚੀ ਵਿੱਚ ਲੋੜੀਂਦੇ ਨਾਂ ਤੇ ਕਲਿਕ ਕਰੋ। ਟੈਕਸਟ ਅਤੇ ਫਾਰਮੈਟਿੰਗ ਲੈ ਲਈ ਜਾਵੇਗੀ ਅਤੇ ਲੋੜ ਅਨੁਸਾਰ ਵਿਵਸਥਿਤ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।</li>
        <li><strong>ਮਿਟਾਉਣਾ:</strong> ਇੱਕ ਬਲਾਕ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰਕੇ ਤੁਸੀਂ ਇਸਨੂੰ ਮਿਟਾ ਸਕਦੇ ਹੋ ਜਾਂ ਇਸਦੀ ਨਿੱਜੀ ਸਥਿਤੀ ਬਦਲ ਸਕਦੇ ਹੋ।</li>
        </ul>

        <p><strong>3. ਨਿੱਜੀ ਟੈਕਸਟ ਬਲਾਕ (ਮਾਸਟਰ ਪਾਸਵਰਡ)</strong></p>
        <ul>
        <li>ਜੇਕਰ ਤੁਸੀਂ ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕੀਤਾ ਹੈ (ਸੈਟਿੰਗਾਂ → ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ ਦੇ ਅਧੀਨ), ਤੁਸੀਂ ਬਲਾਕਾਂ ਨੂੰ "ਨਿੱਜੀ" ਵਜੋਂ ਨਿਸ਼ਾਨਬੱਧ ਕਰ ਸਕਦੇ ਹੋ।</li>
        <li>ਸੰਭਾਲਣ ਤੋਂ ਪਹਿਲਾਂ ਡਾਇਲਾਗ ਵਿੱਚ "ਨਿੱਜੀ ਟੈਕਸਟ ਬਲਾਕ" ਚੈਕਬਾਕਸ ਸਰਗਰਮ ਕਰੋ।</li>
        <li>ਨਿੱਜੀ ਬਲਾਕ ਸੂਚੀ ਵਿੱਚ ਸਿਰਫ ਉਦੋਂ ਦਿਖਾਏ ਜਾਣਗੇ ਜਦੋਂ ਤੁਸੀਂ ਪ੍ਰਤੀ ਸੈਸ਼ਨ ਇੱਕ ਵਾਰ ਆਪਣਾ ਮਾਸਟਰ ਪਾਸਵਰਡ ਟਾਈਪ ਕੀਤਾ ਹੋਵੇ (ਲਾਕ ਆਈਕਨ ਰਾਹੀਂ ਜਾਂ ਪਹਿਲੀ ਪਹੁੰਚ ਤੇ ਪ੍ਰਮਾਣੀਕਰਨ)।</li>
        <li>ਇਸ ਤਰ੍ਹਾਂ ਤੁਸੀਂ ਗੁਪਤ ਟੈਕਸਟ ਬਲਾਕਾਂ ਨੂੰ ਦੂਜਿਆਂ ਦੀ ਪਹੁੰਚ ਤੋਂ ਸੁਰੱਖਿਅਤ ਕਰ ਸਕਦੇ ਹੋ।</li>
        </ul>

        <p><strong>4. ਕਰਾਸ ਪਾਓ</strong></p>
        <ul>
        <li>ਸੰਦਰਭ ਮੀਨੂ ਰਾਹੀਂ ਤੁਸੀਂ ਇੱਕ ਗ੍ਰਾਫਿਕਲ ਕਰਾਸ (ਜਿਵੇਂ ਚੈਕਬਾਕਸ ਲਈ) ਪਾ ਸਕਦੇ ਹੋ।</li>
        <li>ਕਰਾਸ ਦਾ ਆਕਾਰ, ਲਾਈਨ ਦੀ ਮੋਟਾਈ ਅਤੇ ਰੰਗ ਤੁਸੀਂ ਸੈਟਿੰਗਾਂ ਵਿੱਚ ਗਲੋਬਲ ਤੌਰ ਤੇ ਵਿਵਸਥਿਤ ਕਰ ਸਕਦੇ ਹੋ (ਮੀਨੂ "ਸੈਟਿੰਗਾਂ" → "ਅੰਕਰੌਇਜ਼ੇਨ-ਸੈਟਿੰਗਾਂ")।</li>
        <li>ਇੱਕ ਮੌਜੂਦਾ ਕਰਾਸ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰਕੇ ਤੁਸੀਂ ਇਸਨੂੰ ਵਿਅਕਤੀਗਤ ਤੌਰ ਤੇ ਬਦਲ ਸਕਦੇ ਹੋ।</li>
        </ul>

        <p><strong>5. ਸਮੂਹਿਕ ਕਾਰਵਾਈਆਂ</strong></p>
        <ul>
        <li>ਜੇਕਰ ਤੁਸੀਂ ਇੱਕ ਪੰਨੇ ਤੇ ਕਈ ਟੈਕਸਟ ਜਾਂ ਕਰਾਸ ਰੱਖੇ ਹਨ, ਤਾਂ ਸੰਦਰਭ ਮੀਨੂ ਰਾਹੀਂ (ਟੈਕਸਟ ਮੋਡ ਵਿੱਚ ਸੱਜਾ-ਕਲਿਕ) ਤੁਸੀਂ ਸਾਰੇ ਤੱਤ ਇਕੱਠੇ ਸੰਭਾਲ ਸਕਦੇ ਹੋ ਜਾਂ ਰੱਦ ਕਰ ਸਕਦੇ ਹੋ।</li>
        <li>ਸੰਭਾਲਣ ਵੇਲੇ ਸਾਰੇ ਤੱਤ PDF ਵਿੱਚ ਏਮਬੈਡ ਹੋ ਜਾਂਦੇ ਹਨ ਅਤੇ ਵੈਕਟਰ ਗ੍ਰਾਫਿਕ ਵਜੋਂ ਰਹਿੰਦੇ ਹਨ।</li>
        </ul>

        <p><strong>6. ਟੈਕਸਟ ਮੋਡ ਵਿੱਚ ਕੀਬੋਰਡ ਸ਼ਾਰਟਕੱਟ</strong></p>
        <ul>
        <li>ਤੀਰ ਕੁੰਜੀਆਂ: ਤੱਤ ਹਿਲਾਓ</li>
        <li>Ctrl+ਤੀਰ ਕੁੰਜੀਆਂ: ਵੱਡੇ ਕਦਮਾਂ ਨਾਲ ਹਿਲਾਓ</li>
        <li>ਐਂਟਰ: ਸੰਭਾਲ ਡਾਇਲਾਗ ਖੋਲ੍ਹੋ (ਸਾਰੇ ਸੰਭਾਲੋ / ਵਿਵਸਥਿਤ ਕਰੋ / ਰੱਦ ਕਰੋ)</li>
        <li>ESC: ਮੌਜੂਦਾ ਤੱਤ ਰੱਦ ਕਰੋ</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "ਅੰਕਰੌਇਜ਼ੇਨ-ਸੈਟਿੰਗਾਂ",
        'cross_properties': "ਕਰਾਸ-ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ",
        'cross_size': "ਆਕਾਰ (px):",
        'cross_line_width': "ਲਾਈਨ ਦੀ ਮੋਟਾਈ:",
        'cross_color': "ਰੰਗ:",
        'cross_choose_color': "ਚੁਣੋ",
        'cross_fine_tuning': "ਸੰਭਾਲਣ ਵੇਲੇ ਸੂਖਮ ਵਿਵਸਥਾ (ਪਿਕਸਲ)",
        'cross_offset_x': "X-ਆਫਸੈੱਟ:",
        'cross_offset_y': "Y-ਆਫਸੈੱਟ:",
        'cross_offset_x_tooltip': "ਨਕਾਰਾਤਮਕ ਮੁੱਲ ਸੰਭਾਲਣ ਵੇਲੇ ਕਰਾਸ ਨੂੰ ਖੱਬੇ ਪਾਸੇ ਲੈ ਜਾਂਦੇ ਹਨ, ਸਕਾਰਾਤਮਕ ਮੁੱਲ ਸੱਜੇ ਪਾਸੇ",
        'cross_offset_y_tooltip': "ਨਕਾਰਾਤਮਕ ਮੁੱਲ ਸੰਭਾਲਣ ਵੇਲੇ ਕਰਾਸ ਨੂੰ ਉੱਪਰ ਲੈ ਜਾਂਦੇ ਹਨ, ਸਕਾਰਾਤਮਕ ਮੁੱਲ ਹੇਠਾਂ",
        'cross_preview': "ਪੂਰਵ ਦਰਸ਼ਨ",
        'cross_save': "ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਕਰੋ",
        'cross_customized': "ਕਰਾਸ ਵਿਵਸਥਿਤ ਕੀਤਾ ਗਿਆ",
        'cross_settings_applied': "ਕਰਾਸ-ਸੈਟਿੰਗਾਂ ਸੰਭਾਲੀਆਂ ਗਈਆਂ।\nਆਕਾਰ: {0}px, ਲਾਈਨ ਦੀ ਮੋਟਾਈ: {1}px\n{2}",
        'cross_updated_count': "{0} ਮੌਜੂਦਾ ਕਰਾਸ ਅੱਪਡੇਟ ਕੀਤੇ ਗਏ।",
        'cross_no_crosses': "ਕੋਈ ਮੌਜੂਦਾ ਕਰਾਸ ਨਹੀਂ ਮਿਲਿਆ।",
        'cross_settings_applied_all': "ਸਾਰੇ {0} ਕਰਾਸ ਲਈ ਕਰਾਸ ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਕੀਤੀਆਂ ਗਈਆਂ",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "ਦਸਤਖਤ-ਸੈਟਿੰਗਾਂ",
        'signature_1': "ਦਸਤਖਤ 1",
        'signature_2': "ਦਸਤਖਤ 2",
        'signature_select': "ਦਸਤਖਤ ਚੁਣੋ",
        'signature_add': "➕ ਨਵਾਂ ਦਸਤਖਤ ਸ਼ਾਮਲ ਕਰੋ...",
        'signature_size': "ਦਸਤਖਤ {0} ਲਈ ਆਕਾਰ (%):",
        'signature_common': "ਆਮ ਸੈਟਿੰਗਾਂ",
        'signature_timestamp': "ਆਪਣੇ ਆਪ ਟਾਈਮਸਟੈਂਪ ਸ਼ਾਮਲ ਕਰੋ",
        'signature_location': "ਡਿਫੌਲਟ ਸਥਾਨ:",
        'signature_timestamp_size': "ਟਾਈਮਸਟੈਂਪ ਫੌਂਟ ਦਾ ਆਕਾਰ:",
        'signature_no_files': "-- ਕੋਈ ਦਸਤਖਤ ਨਹੀਂ ਮਿਲਿਆ --",
        'signature_insert': "ਦਸਤਖਤ ਪਾਓ",
        'signature_insert_1': "ਦਸਤਖਤ 1 ਪਾਓ",
        'signature_insert_2': "ਦਸਤਖਤ 2 ਪਾਓ",
        'signature_customize': " ਦਸਤਖਤ ਵਿਵਸਥਿਤ ਕਰੋ",
        'signature_discard': " ਇਹ ਦਸਤਖਤ ਰੱਦ ਕਰੋ",
        'signature_save_all': " ਸਾਰੇ ਦਸਤਖਤ ਸੰਭਾਲੋ",
        'signature_discard_all': " ਸਾਰੇ ਦਸਤਖਤ ਰੱਦ ਕਰੋ",
        'signature_guide_title': "ਦਸਤਖਤ - ਮਾਰਗਦਰਸ਼ਨ",
        'signature_guide': """
📝 ਦਸਤਖਤ - ਸੰਖੇਪ ਮਾਰਗਦਰਸ਼ਨ

- ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰੋ
- ਮੀਨੂ ਸੈਟਿੰਗਾਂ ਵਿੱਚ ਦਸਤਖਤ ਕੌਂਫਿਗਰ ਕਰੋ
  (ਆਕਾਰ, ਟਾਈਮਸਟੈਂਪ ...)
- ਲੋੜੀਂਦੀ ਥਾਂ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰਕੇ ਪਾਓ
  (ਪ੍ਰਤੀ ਸੈਸ਼ਨ ਇੱਕ ਵਾਰ ਮਾਸਟਰ ਪਾਸਵਰਡ ਦੀ ਲੋੜ ਹੈ)
- ਮਾਊਸ ਜਾਂ ਤੀਰ ਕੁੰਜੀਆਂ ਨਾਲ ਦਸਤਖਤ ਹਿਲਾਓ
- ਇੱਕ ਤੋਂ ਬਾਅਦ ਇੱਕ ਕਈ ਦਸਤਖਤ ਪਾਏ ਜਾ ਸਕਦੇ ਹਨ
- ਹਰੇਕ ਦਸਤਖਤ ਨੂੰ ਵਿਅਕਤੀਗਤ ਤੌਰ ਤੇ ਵਿਵਸਥਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ
- ਇੱਕਲਾ ਦਸਤਖਤ ਰੱਦ ਕਰੋ
- ਸਾਰੇ ਦਸਤਖਤ ਇੱਕ ਵਾਰ ਸੰਭਾਲੋ / ਰੱਦ ਕਰੋ
- ਵਿਕਲਪਿਕ ਤੌਰ ਤੇ ਮੀਨੂ ਬਾਰ ਦੀ ਵੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ।
        """,
        'signature_placeholder': "ਕੋਈ ਪੂਰਵ ਦਰਸ਼ਨ ਉਪਲਬਧ ਨਹੀਂ",
        'signature_info': "ਦਸਤਖਤ {0}: {1}×{2} px ({3}% of {4}×{5})",
        'signature_info_placeholder': "ਦਸਤਖਤ {0} ਲਈ ਸੈਟਿੰਗਾਂ",
        'signature_inserted': "ਦਸਤਖਤ {0} ਪੰਨਾ {1} ਤੇ ਪਾ ਦਿੱਤਾ ਗਿਆ",
        'signature_deleted': "ਦਸਤਖਤ ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ",
        'signature_copied': "ਦਸਤਖਤ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'signature_pasted': "ਦਸਤਖਤ {0} ਪਾ ਦਿੱਤਾ ਗਿਆ",
        'signature_saved': "{0} ਦਸਤਖਤ PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'signature_saved_voice': "{0} ਦਸਤਖਤ ਸੰਭਾਲੇ ਗਏ",
        'mode_replace_signature_format': "ਮੋਡ ਖਤਮ ਕਰੋ ਅਤੇ ਦਸਤਖਤ {0} ਪਾਓ",
        'mode_conflict_voice_signature': "{0} ਮੋਡ ਸਰਗਰਮ ਹੈ। ਖਤਮ ਕਰਕੇ ਦਸਤਖਤ ਪਾਉਣਾ ਹੈ?",
        'signature_not_configured': "ਦਸਤਖਤ {0} ਕੌਂਫਿਗਰ ਨਹੀਂ ਕੀਤਾ ਗਿਆ",
        'signature_file_not_found': "ਦਸਤਖਤ ਫਾਈਲ ਨਹੀਂ ਮਿਲੀ",
        'timestamp_format': "{0}, {1} ਨੂੰ",
        'no_copied_signature': "ਕੋਈ ਕਾਪੀ ਕੀਤਾ ਦਸਤਖਤ ਨਹੀਂ",
        'no_signatures_to_save': "ਸੰਭਾਲਣ ਲਈ ਕੋਈ ਦਸਤਖਤ ਨਹੀਂ",
        'signature_save_question': "ਸਾਰੇ ਦਸਤਖਤ ਸੰਭਾਲੋ, ਵਿਵਸਥਿਤ ਕਰੋ ਜਾਂ ਇਸਨੂੰ ਰੱਦ ਕਰੋ?",
        'signatures_saved_title': "ਦਸਤਖਤ ਸੰਭਾਲੇ ਗਏ",
        'signatures_saved': "{0} ਦਸਤਖਤ PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'signatures_saved_voice': "{0} ਦਸਤਖਤ ਸੰਭਾਲੇ ਗਏ।",
        'all_signatures_discarded': "ਸਾਰੇ ਦਸਤਖਤ ਰੱਦ ਕਰ ਦਿੱਤੇ ਗਏ",
        'signature_settings_saved': "ਦਸਤਖਤ-ਸੈਟਿੰਗਾਂ ਸੰਭਾਲੀਆਂ ਗਈਆਂ",
        'signature_cancelled': "ਦਸਤਖਤ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'signature_active_title': "ਦਸਤਖਤ ਸਰਗਰਮ",
        'signature_replace_question': "ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਦਸਤਖਤ ਸਰਗਰਮ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਮੌਜੂਦਾ ਦਸਤਖਤ ਨੂੰ ਬਦਲਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'signature_replace': "ਦਸਤਖਤ ਬਦਲੋ",
        'signature_replace_voice': "ਮੌਜੂਦਾ ਦਸਤਖਤ ਬਦਲਣਾ ਹੈ ਜਾਂ ਰੱਦ ਕਰਨਾ ਹੈ?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "ਚਿੱਤਰ ਸੈਟਿੰਗਾਂ",
        'image_common': "ਆਮ ਚਿੱਤਰ ਸੈਟਿੰਗਾਂ",
        'image_keep_aspect': "ਡ੍ਰੈਗ ਕਰਦੇ ਸਮੇਂ ਆਕਾਰ ਅਨੁਪਾਤ ਬਰਕਰਾਰ ਰੱਖੋ",
        'image_default_size': "ਡਿਫੌਲਟ ਆਕਾਰ (%):",
        'image_dark_invert': "ਡਾਰਕ ਮੋਡ ਵਿੱਚ ਚਿੱਤਰ ਉਲਟਾਓ",
        'image_dark_invert_tooltip': "ਸਰਗਰਮ: ਬਿਹਤਰ ਦਿੱਖ ਲਈ ਚਿੱਤਰ ਉਲਟਾਏ ਜਾਣਗੇ",
        'image_fine_tuning': "ਸੂਖਮ ਵਿਵਸਥਾ (ਪਿਕਸਲ)",
        'image_offset_x': "X-ਆਫਸੈੱਟ:",
        'image_offset_y': "Y-ਆਫਸੈੱਟ:",
        'image_offset_x_tooltip': "ਨਕਾਰਾਤਮਕ ਮੁੱਲ ਸੰਭਾਲਣ ਵੇਲੇ ਚਿੱਤਰ ਨੂੰ ਖੱਬੇ ਪਾਸੇ ਲੈ ਜਾਂਦੇ ਹਨ, ਸਕਾਰਾਤਮਕ ਮੁੱਲ ਸੱਜੇ ਪਾਸੇ",
        'image_offset_y_tooltip': "ਨਕਾਰਾਤਮਕ ਮੁੱਲ ਸੰਭਾਲਣ ਵੇਲੇ ਚਿੱਤਰ ਨੂੰ ਉੱਪਰ ਲੈ ਜਾਂਦੇ ਹਨ, ਸਕਾਰਾਤਮਕ ਮੁੱਲ ਹੇਠਾਂ",
        'image_select': "ਚਿੱਤਰ ਚੁਣੋ",
        'image_insert': "ਚਿੱਤਰ ਪਾਓ",
        'image_customize': " ਚਿੱਤਰ ਵਿਵਸਥਿਤ ਕਰੋ",
        'image_aspect': " ਆਕਾਰ ਅਨੁਪਾਤ ਬਰਕਰਾਰ ਰੱਖੋ",
        'image_discard': " ਇਹ ਚਿੱਤਰ ਰੱਦ ਕਰੋ",
        'image_save_all': " ਸਾਰੇ ਚਿੱਤਰ ਸੰਭਾਲੋ",
        'image_discard_all': " ਸਾਰੇ ਚਿੱਤਰ ਰੱਦ ਕਰੋ",
        'image_filter': "ਚਿੱਤਰ",
        'image_guide_title': "ਚਿੱਤਰ ਪਾਓ - ਮਾਰਗਦਰਸ਼ਨ",
        'image_guide': """
📷 PDF ਵਿੱਚ ਚਿੱਤਰ ਪਾਓ - ਸੰਖੇਪ ਮਾਰਗਦਰਸ਼ਨ:

1. ਲੋੜੀਂਦੀ ਥਾਂ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰੋ
2. "ਚਿੱਤਰ ਪਾਓ" → ਚਿੱਤਰ ਚੁਣੋ
3. ਚਿੱਤਰ ਸਥਿਤ ਕਰੋ: ਮਾਊਸ ਨਾਲ ਡ੍ਰੈਗ ਕਰੋ
4. ਆਕਾਰ ਵਿਵਸਥਿਤ ਕਰੋ: ਕੋਨਿਆਂ/ਕਿਨਾਰਿਆਂ ਤੇ ਡ੍ਰੈਗ ਕਰੋ
5. ਆਕਾਰ ਅਨੁਪਾਤ ਬਰਕਰਾਰ ਰੱਖੋ: [A] ਕੁੰਜੀ
6. ਹੋਰ ਵਿਵਸਥਾਵਾਂ: ਚਿੱਤਰ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰੋ

ਟਿਪ: ਸੰਦਰਭ ਮੀਨੂ ਵਿੱਚ ਤੁਸੀਂ ਸੈਟਿੰਗਾਂ ਵਿਵਸਥਿਤ ਕਰ ਸਕਦੇ ਹੋ।
        """,
        'image_inserted': "ਚਿੱਤਰ {0} ਪੰਨਾ {1} ਤੇ ਪਾ ਦਿੱਤਾ ਗਿਆ",
        'image_deleted': "ਚਿੱਤਰ ਰੱਦ ਕਰ ਦਿੱਤਾ ਗਿਆ",
        'image_copied': "ਚਿੱਤਰ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'image_pasted': "ਚਿੱਤਰ ਪਾ ਦਿੱਤਾ ਗਿਆ",
        'image_saved': "{0} ਚਿੱਤਰ PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'image_saved_voice': "{0} ਚਿੱਤਰ ਸੰਭਾਲੇ ਗਏ",
        'image_aspect_on': "ਸਰਗਰਮ",
        'image_aspect_off': "ਅਸਰਗਰਮ",
        'image_aspect_toggle': "ਆਕਾਰ ਅਨੁਪਾਤ ਬਰਕਰਾਰ ਰੱਖੋ {0}",
        'image_reset': "ਚਿੱਤਰ ਮੂਲ ਆਕਾਰ ਤੇ ਰੀਸੈਟ ਕੀਤਾ ਗਿਆ",
        'image_replaced': "ਚਿੱਤਰ ਬਦਲਿਆ ਗਿਆ",
        'image_invalid': "ਕੋਈ ਵੈਧ ਚਿੱਤਰ ਨਹੀਂ",
        'mode_replace_image': "ਚਿੱਤਰ ਪਾਓ",
        'mode_conflict_voice_image': "{0} ਮੋਡ ਸਰਗਰਮ ਹੈ। ਖਤਮ ਕਰਕੇ ਚਿੱਤਰ ਪਾਉਣਾ ਹੈ?",
        'image_active_title': "ਚਿੱਤਰ ਸਰਗਰਮ",
        'image_replace_question': "ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਚਿੱਤਰ ਸਰਗਰਮ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਮੌਜੂਦਾ ਚਿੱਤਰ ਨੂੰ ਬਦਲਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'image_replace': "ਚਿੱਤਰ ਬਦਲੋ",
        'image_replace_voice': "ਮੌਜੂਦਾ ਚਿੱਤਰ ਬਦਲਣਾ ਹੈ ਜਾਂ ਰੱਦ ਕਰਨਾ ਹੈ?",
        'image_filter_all': "ਚਿੱਤਰ (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;ਸਭ ਫਾਈਲਾਂ (*.*)",
        'no_copied_image': "ਕੋਈ ਕਾਪੀ ਕੀਤਾ ਚਿੱਤਰ ਨਹੀਂ",
        'image_discarded': "ਚਿੱਤਰ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'image_save_question': "ਸਾਰੇ ਚਿੱਤਰ ਸੰਭਾਲੋ, ਵਿਵਸਥਿਤ ਕਰੋ ਜਾਂ ਇਸਨੂੰ ਰੱਦ ਕਰੋ?",
        'no_images_to_save': "ਸੰਭਾਲਣ ਲਈ ਕੋਈ ਚਿੱਤਰ ਨਹੀਂ",
        'no_valid_images': "ਸੰਭਾਲਣ ਲਈ ਕੋਈ ਵੈਧ ਚਿੱਤਰ ਨਹੀਂ",
        'images_saved_title': "ਚਿੱਤਰ ਸੰਭਾਲੇ ਗਏ",
        'images_saved': "{0} ਚਿੱਤਰ PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'images_saved_voice': "{0} ਚਿੱਤਰ ਸੰਭਾਲੇ ਗਏ।",
        'all_images_discarded': "ਸਾਰੇ ਚਿੱਤਰ ਰੱਦ ਕਰ ਦਿੱਤੇ ਗਏ",
        'image_settings_updated': "ਚਿੱਤਰ ਸੈਟਿੰਗਾਂ ਅੱਪਡੇਟ ਕੀਤੀਆਂ ਗਈਆਂ",
        'image_replace_title': "ਨਵਾਂ ਚਿੱਤਰ ਚੁਣੋ",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "ਆਕਾਰ ਸੈਟਿੰਗਾਂ",
        'form_basic': "ਮੁੱਢਲੀਆਂ ਸੈਟਿੰਗਾਂ",
        'form_default_type': "ਡਿਫੌਲਟ ਆਕਾਰ ਕਿਸਮ:",
        'form_rectangle': "ਆਇਤ",
        'form_ellipse': "ਅੰਡਾਕਾਰ",
        'form_line': "ਰੇਖਾ",
        'form_arrow': "ਤੀਰ",
        'form_line_width': "ਰੇਖਾ ਦੀ ਮੋਟਾਈ:",
        'form_colors': "ਰੰਗ",
        'form_line_color': "ਰੇਖਾ ਦਾ ਰੰਗ:",
        'form_fill_color': "ਭਰਾਈ ਰੰਗ:",
        'form_choose_color': "ਚੁਣੋ",
        'form_transparent': "ਪਾਰਦਰਸ਼ੀ ਪਿਛੋਕੜ (ਸਿਰਫ ਰੇਖਾ)",
        'form_filled': "ਭਰਿਆ ਹੋਇਆ",
        'form_dark_mode': "ਡਾਰਕ ਮੋਡ",
        'form_dark_invert': "ਡਾਰਕ ਮੋਡ ਵਿੱਚ ਰੰਗ ਉਲਟਾਓ",
        'form_fine_tuning': "ਸੂਖਮ ਵਿਵਸਥਾ (ਪਿਕਸਲ)",
        'form_offset_x': "X-ਆਫਸੈੱਟ:",
        'form_offset_y': "Y-ਆਫਸੈੱਟ:",
        'form_offset_x_tooltip': "ਨਕਾਰਾਤਮਕ ਮੁੱਲ ਸੰਭਾਲਣ ਵੇਲੇ ਆਕਾਰ ਨੂੰ ਖੱਬੇ ਪਾਸੇ ਲੈ ਜਾਂਦੇ ਹਨ, ਸਕਾਰਾਤਮਕ ਮੁੱਲ ਸੱਜੇ ਪਾਸੇ",
        'form_offset_y_tooltip': "ਨਕਾਰਾਤਮਕ ਮੁੱਲ ਸੰਭਾਲਣ ਵੇਲੇ ਆਕਾਰ ਨੂੰ ਉੱਪਰ ਲੈ ਜਾਂਦੇ ਹਨ, ਸਕਾਰਾਤਮਕ ਮੁੱਲ ਹੇਠਾਂ",
        'form_preview': "ਪੂਰਵ ਦਰਸ਼ਨ",
        'form_insert': "ਆਕਾਰ ਪਾਓ",
        'form_rectangle_insert': "ਆਇਤ",
        'form_ellipse_insert': "ਅੰਡਾਕਾਰ/ਚੱਕਰ",
        'form_line_insert': "ਰੇਖਾ (2 ਕਲਿੱਕ)",
        'form_arrow_insert': "ਤੀਰ (2 ਕਲਿੱਕ)",
        'form_customize': " ਆਕਾਰ ਵਿਵਸਥਿਤ ਕਰੋ",
        'form_transparent_toggle': " ਪਾਰਦਰਸ਼ੀ ਪਿਛੋਕੜ",
        'form_discard': " ਇਹ ਆਕਾਰ ਰੱਦ ਕਰੋ",
        'form_save_all': " ਸਾਰੇ ਆਕਾਰ ਸੰਭਾਲੋ",
        'form_discard_all': " ਸਾਰੇ ਆਕਾਰ ਰੱਦ ਕਰੋ",
        'form_guide_title': "ਆਕਾਰ ਪਾਓ - ਮਾਰਗਦਰਸ਼ਨ",
        'form_guide': """
📐 PDF ਵਿੱਚ ਆਕਾਰ ਪਾਓ - ਸੰਖੇਪ ਮਾਰਗਦਰਸ਼ਨ:

1. ਆਕਾਰ ਕਿਸਮ ਚੁਣੋ (ਆਇਤ, ਅੰਡਾਕਾਰ, ਰੇਖਾ, ਤੀਰ)
2. ਸਥਿਤੀ ਤੇ ਕਲਿੱਕ ਕਰੋ
   - ਆਇਤ/ਅੰਡਾਕਾਰ ਲਈ: ਇੱਕ ਕਲਿੱਕ ਆਕਾਰ ਰੱਖਦਾ ਹੈ
   - ਰੇਖਾ/ਤੀਰ ਲਈ: ਸ਼ੁਰੂ ਅਤੇ ਅੰਤ ਬਿੰਦੂ ਲਈ ਦੋ ਕਲਿੱਕ
3. ਆਕਾਰ ਸਥਿਤ ਕਰੋ: ਮਾਊਸ ਨਾਲ ਡ੍ਰੈਗ ਕਰੋ
4. ਆਕਾਰ ਵਿਵਸਥਿਤ ਕਰੋ: ਕੋਨਿਆਂ/ਕਿਨਾਰਿਆਂ ਤੇ ਡ੍ਰੈਗ ਕਰੋ
5. ਆਕਾਰ ਸੰਭਾਲੋ: ਐਂਟਰ
6. ਆਕਾਰ ਰੱਦ ਕਰੋ: ESC
7. ਹੋਰ ਵਿਵਸਥਾਵਾਂ: ਆਕਾਰ ਤੇ ਸੱਜਾ-ਕਲਿੱਕ ਕਰੋ

ਟਿਪ: ਸੰਦਰਭ ਮੀਨੂ ਵਿੱਚ ਤੁਸੀਂ ਸੈਟਿੰਗਾਂ ਵਿਵਸਥਿਤ ਕਰ ਸਕਦੇ ਹੋ।
        """,
        'form_inserted': "{0} ਪੰਨਾ {1} ਤੇ ਪਾ ਦਿੱਤਾ ਗਿਆ",
        'form_deleted': "ਆਕਾਰ ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ",
        'form_copied': "ਆਕਾਰ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'form_pasted': "ਆਕਾਰ ਪਾ ਦਿੱਤਾ ਗਿਆ",
        'form_saved': "{0} ਆਕਾਰ PDF ਵਿੱਚ ਪਾ ਦਿੱਤੇ ਗਏ।\n\nPDF ਮੁੜ ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'form_saved_voice': "{0} ਆਕਾਰ ਸੰਭਾਲੇ ਗਏ",
        'form_reset': "ਆਕਾਰ ਡਿਫੌਲਟ ਆਕਾਰ ਤੇ ਰੀਸੈਟ ਕੀਤਾ ਗਿਆ",
        'form_transparent_on': "ਸਰਗਰਮ",
        'form_transparent_off': "ਅਸਰਗਰਮ",
        'form_transparent_toggled': "ਪਾਰਦਰਸ਼ੀ ਪਿਛੋਕੜ {0}",
        'form_line_cancel': "ਰੇਖਾ ਖਿੱਚਣਾ ਰੱਦ ਕੀਤਾ ਗਿਆ",
        'form_second_click': "ਹੁਣ {0} ਲਈ ਅੰਤ ਬਿੰਦੂ ਤੇ ਕਲਿੱਕ ਕਰੋ",
        'mode_replace_form': "ਆਕਾਰ ਪਾਓ",
        'mode_conflict_voice_form': "{0} ਮੋਡ ਸਰਗਰਮ ਹੈ। ਖਤਮ ਕਰਕੇ ਇੱਕ ਆਕਾਰ ਪਾਉਣਾ ਹੈ?",
        'form_settings_updated': "ਆਕਾਰ-ਸੈਟਿੰਗਾਂ ਅੱਪਡੇਟ ਕੀਤੀਆਂ ਗਈਆਂ",
        'form_unknown': "ਆਕਾਰ",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. ਸ਼ੁਰੂ ਸਥਿਤੀ ਤੇ ਕਲਿੱਕ ਕਰੋ",
        'form_line_guide_2': "2. ਅੰਤ ਸਥਿਤੀ ਤੇ ਕਲਿੱਕ ਕਰੋ",
        'form_line_guide_3': "ਰੇਖਾ ਦੋ ਬਿੰਦੂਆਂ ਦੇ ਵਿਚਕਾਰ ਖਿੱਚੀ ਜਾਵੇਗੀ।",
        'form_line_status_1': "ਪਹਿਲੇ ਕਲਿੱਕ ਦੀ ਉਡੀਕ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'form_line_status_2': "ਪਹਿਲਾ ਬਿੰਦੂ ਸੈੱਟ ਕੀਤਾ ਗਿਆ: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "ਹੁਣ ਅੰਤ ਬਿੰਦੂ ਤੇ ਕਲਿੱਕ ਕਰੋ...",
        'form_line_status_4': "ਦੋਵੇਂ ਬਿੰਦੂ ਸੈੱਟ ਕੀਤੇ ਗਏ।\nਸੰਭਾਲਣ ਲਈ 'ਮੁਕੰਮਲ' ਤੇ ਕਲਿੱਕ ਕਰੋ।",
        'form_line_reset': "ਰੀਸੈਟ ਕਰੋ",
        'form_line_finish': "ਮੁਕੰਮਲ",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "ਕਾਪੀ ਕਰੋ (Cmd+C)",
        'paste': "ਪੇਸਟ ਕਰੋ (Cmd+V)",
        'copied': "ਕਾਪੀ ਕੀਤਾ: {0}",
        'no_element_to_copy': "ਕਾਪੀ ਕਰਨ ਲਈ ਕੋਈ ਤੱਤ ਨਹੀਂ ਚੁਣਿਆ ਗਿਆ",
        'no_copied_data': "ਕੋਈ ਕਾਪੀ ਕੀਤਾ ਡਾਟਾ ਨਹੀਂ",
        'no_valid_position': "ਪੇਸਟ ਕਰਨ ਲਈ ਕੋਈ ਵੈਧ ਸਥਿਤੀ ਨਹੀਂ",
        'copy_text': "ਟੈਕਸਟ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'copy_image': "ਚਿੱਤਰ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'copy_form': "ਆਕਾਰ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'copy_signature': "ਦਸਤਖਤ ਕਾਪੀ ਕੀਤਾ ਗਿਆ",
        'element_text': "ਟੈਕਸਟ",
        'element_image': "ਚਿੱਤਰ",
        'element_form': "ਆਕਾਰ",
        'element_signature': "ਦਸਤਖਤ",
        'element_unknown': "ਤੱਤ",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "ਮੋਡ ਟਕਰਾਅ",
        'mode_conflict_message': "'{0}' ਮੋਡ ਪਹਿਲਾਂ ਹੀ ਸਰਗਰਮ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਇਸਨੂੰ ਖਤਮ ਕਰਕੇ {1} ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'mode_replace': "ਮੋਡ ਖਤਮ ਕਰੋ ਅਤੇ {0} ਕਰੋ",
        'mode_cancel': "ਰੱਦ ਕਰੋ",
        'mode_replace_text': "ਟੈਕਸਟ ਪਾਓ",
        'mode_replace_cross': "ਕਰਾਸ ਪਾਓ",
        'mode_replace_signature': "ਦਸਤਖਤ ਪਾਓ",
        'mode_replace_image': "ਚਿੱਤਰ ਪਾਓ",
        'mode_replace_form': "ਆਕਾਰ ਪਾਓ",
        'mode_conflict_voice': "{0} ਮੋਡ ਸਰਗਰਮ ਹੈ। ਖਤਮ ਕਰਕੇ ਟੈਕਸਟ ਪਾਉਣਾ ਹੈ?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "ਟੈਕਸਟ ਇਨਪੁਟ",
        'active_mode_signature': "ਦਸਤਖਤ",
        'active_mode_image': "ਚਿੱਤਰ",
        'active_mode_form': "ਆਕਾਰ",
        'active_mode_and': " ਅਤੇ ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "ਪਾਓ",                    # Hauptmenü
        'insert_another_text': "ਟੈਕਸਟ ਪਾਓ",          # Vereinfacht
        'insert_another_cross': "ਕਰਾਸ ਪਾਓ",        # Vereinfacht
        'insert_another_signature_1': "ਦਸਤਖਤ 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "ਦਸਤਖਤ 2",      # Untermenü-Eintrag
        'insert_another_image': "ਚਿੱਤਰ ਪਾਓ",         # Vereinfacht
        'insert_another_form_rect': "ਆਇਤ",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "ਅੰਡਾਕਾਰ",        # Untermenü-Eintrag
        'insert_another_form_line': "ਰੇਖਾ (2 ਕਲਿੱਕ)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "ਤੀਰ (2 ਕਲਿੱਕ)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} ਸੰਭਾਲੋ",
        'save_dialog_message': "{0} ਪੰਨਾ {1} ਤੇ ਸੰਭਾਲਿਆ ਜਾਵੇਗਾ।\n\nਤੁਸੀਂ ਕਿਵੇਂ ਅੱਗੇ ਵਧਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'save_all': "ਸਾਰੇ {0} ਸੰਭਾਲੋ",
        'save_single': "{0} ਸੰਭਾਲੋ",
        'save_customize': "{0} ਵਿਵਸਥਿਤ ਕਰੋ",
        'save_discard': "ਇਹ {0} ਰੱਦ ਕਰੋ",
        'save_continue': "ਸੰਪਾਦਨ ਜਾਰੀ ਰੱਖੋ",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " ਪੰਨਾ {0} ਤੇ ਜਾਓ",
        'context_rotate': " ਪੰਨਾ {0} ਘੁਮਾਓ",
        'context_delete': " ਪੰਨਾ {0} ਮਿਟਾਓ",
        'context_export': " ਪੰਨਾ {0} ਐਕਸਪੋਰਟ ਕਰੋ",
        'context_mark_as': " ਪੰਨੇ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਨਿਸ਼ਾਨਬੱਧ ਕਰੋ...",
        'context_mark_empty': " ਖਾਲੀ ਪੰਨਾ",
        'context_unmark_empty': " ਹੁਣ ਖਾਲੀ ਨਹੀਂ",
        'context_mark_export': " ਐਕਸਪੋਰਟ ਲਈ ਨਿਸ਼ਾਨਬੱਧ ਕਰੋ",
        'context_unmark_export': " ਹੁਣ ਐਕਸਪੋਰਟ ਨਾ ਕਰੋ",
        'context_batch_actions': " ਸਮੂਹਿਕ ਕਾਰਵਾਈਆਂ",
        'context_batch_delete_empty': " ਸਾਰੇ {0} ਖਾਲੀ ਪੰਨੇ ਮਿਟਾਓ",
        'context_batch_export_single': " ਸਾਰੇ {0} ਪੰਨੇ (ਇੱਕ ਫਾਈਲ)",
        'context_batch_export_split': " ਸਾਰੇ {0} ਪੰਨੇ (ਵੱਖਰੇ)",
        'context_drag_start': " ਡ੍ਰੈਗ ਐਂਡ ਡ੍ਰੌਪ ਸ਼ੁਰੂ ਕਰੋ",
        'context_drag_stop': " ਡ੍ਰੈਗ ਐਂਡ ਡ੍ਰੌਪ ਬੰਦ ਕਰੋ",
        'context_insert': " ਪਾਓ",
        'context_insert_pages': " ਪੰਨੇ ਪਾਓ",
        'context_zoom': "ਜ਼ੂਮ",
        'discard_mixed': "ਸਾਰੇ {0} {1} ਅਤੇ {2} {3} ਰੱਦ ਕਰੋ",
        'save_mixed': "{0} {1} ਅਤੇ {2} {3} ਸੰਭਾਲੋ",
        'discard_texts': "ਸਾਰੇ {0} ਟੈਕਸਟ ਰੱਦ ਕਰੋ",
        'discard_text_single': "1 ਟੈਕਸਟ ਰੱਦ ਕਰੋ",
        'save_texts': "{0} ਟੈਕਸਟ ਸੰਭਾਲੋ",
        'save_text_single': "1 ਟੈਕਸਟ ਸੰਭਾਲੋ",
        'discard_crosses': "ਸਾਰੇ {0} ਕਰਾਸ ਰੱਦ ਕਰੋ",
        'discard_cross_single': "1 ਕਰਾਸ ਰੱਦ ਕਰੋ",
        'save_crosses': "{0} ਕਰਾਸ ਸੰਭਾਲੋ",
        'save_cross_single': "1 ਕਰਾਸ ਸੰਭਾਲੋ",
        'discard_signatures': "ਸਾਰੇ {0} ਦਸਤਖਤ ਰੱਦ ਕਰੋ",
        'save_signature_single': "1 ਦਸਤਖਤ ਸੰਭਾਲੋ",
        'save_signatures': "{0} ਦਸਤਖਤ ਸੰਭਾਲੋ",
        'discard_images': "ਸਾਰੇ {0} ਚਿੱਤਰ ਰੱਦ ਕਰੋ",
        'save_image_single': "1 ਚਿੱਤਰ ਸੰਭਾਲੋ",
        'save_images': "{0} ਚਿੱਤਰ ਸੰਭਾਲੋ",
        'discard_forms': "ਸਾਰੇ {0} ਆਕਾਰ ਰੱਦ ਕਰੋ",
        'save_form_single': "1 ਆਕਾਰ ਸੰਭਾਲੋ",
        'save_forms': "{0} ਆਕਾਰ ਸੰਭਾਲੋ",
        'cross_discard': "ਇਹ ਕਰਾਸ ਰੱਦ ਕਰੋ",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 ਐਕਸਪੋਰਟ / ਆਯਾਤ ਜਾਣਕਾਰੀ",
        'export_what': "📋 ਕੀ ਐਕਸਪੋਰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ?",
        'export_general': "ਆਮ ਸੈਟਿੰਗਾਂ",
        'export_general_items': "• ਸਪੀਚ ਆਉਟਪੁੱਟ (ਚਾਲੂ/ਬੰਦ, ਗਤੀ)\n• ਡਾਰਕ/ਹਲਕਾ ਮੋਡ\n• ਬੈਕਅੱਪ ਸੈਟਿੰਗਾਂ\n• OCR ਸੈਟਿੰਗਾਂ",
        'export_image_form': "ਚਿੱਤਰ ਅਤੇ ਆਕਾਰ ਸੈਟਿੰਗਾਂ",
        'export_image_form_items': "• ਚਿੱਤਰ ਸੈਟਿੰਗਾਂ (ਆਕਾਰ ਅਨੁਪਾਤ, ਡਿਫੌਲਟ ਆਕਾਰ)\n• ਆਕਾਰ ਸੈਟਿੰਗਾਂ (ਰੇਖਾ ਦੀ ਮੋਟਾਈ, ਰੰਗ)\n• ਦਸਤਖਤ ਸੈਟਿੰਗਾਂ (ਪਾਥ, ਆਕਾਰ, ਟਾਈਮਸਟੈਂਪ)",
        'export_passwords': "ਪਾਸਵਰਡ ਡਾਟਾਬੇਸ",
        'export_passwords_items': "• ਸਾਰੇ ਸੰਭਾਲੇ ਗਏ PDF ਪਾਸਵਰਡ\n• ਐਨਕ੍ਰਿਪਟਡ ਜਾਂ ਡੀਕ੍ਰਿਪਟਡ ਚੋਣਵੇਂ ਤੌਰ ਤੇ",
        'export_master': "ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈਟਿੰਗਾਂ",
        'export_master_items': "• ਮਾਸਟਰ ਪਾਸਵਰਡ ਹੈਸ਼\n• ਦਸਤਖਤ/ਟੈਕਸਟ ਬਲਾਕਾਂ ਲਈ ਸੈਟਿੰਗਾਂ",
        'export_signatures': "ਦਸਤਖਤ ਅਤੇ ਟੈਕਸਟ ਬਲਾਕ",
        'export_signatures_items': "• ਸਾਰੀਆਂ ਚਿੱਤਰ ਫਾਈਲਾਂ (ਦਸਤਖਤ)\n• ਫਾਰਮੈਟਿੰਗ ਦੇ ਨਾਲ ਸਾਰੇ ਟੈਕਸਟ ਬਲਾਕ\n• ਨਿੱਜੀ/ਜਨਤਕ ਨਿਸ਼ਾਨੀਆਂ",
        'export_import_warning': "⚠️ ਮਹੱਤਵਪੂਰਨ ਨੋਟਿਸ",
        'export_import_note': "• ਆਯਾਤ ਕਰਦੇ ਸਮੇਂ ਸਾਰੀਆਂ ਮੌਜੂਦਾ ਸੈਟਿੰਗਾਂ ਓਵਰਰਾਈਟ ਹੋ ਜਾਣਗੀਆਂ\n• ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ\n• ਮੌਜੂਦਾ ਦਸਤਖਤ/ਟੈਕਸਟ ਬਲਾਕ ਬਦਲ ਦਿੱਤੇ ਜਾਣਗੇ",
        'export_master_note': "• ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਹੋਣ ਤੇ ਤੁਸੀਂ ਚੁਣ ਸਕਦੇ ਹੋ:\n  - ਡੀਕ੍ਰਿਪਟਡ (ਪਾਸਵਰਡ ਸਪਸ਼ਟ ਟੈਕਸਟ ਵਿੱਚ)\n  - ਐਨਕ੍ਰਿਪਟਡ (ਸਿਰਫ ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ ਪੜ੍ਹਿਆ ਜਾ ਸਕਦਾ ਹੈ)",
        'export_security': "• ਐਕਸਪੋਰਟ ਕੀਤੀ ZIP ਫਾਈਲ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ ਡਾਟਾ ਹੁੰਦਾ ਹੈ\n• ਕਿਰਪਾ ਕਰਕੇ ਸੁਰੱਖਿਅਤ ਰੱਖੋ (ਜਿਵੇਂ ਐਨਕ੍ਰਿਪਟਡ USB ਸਟਿੱਕ)\n• ਫਾਈਲ ਗੁਆਉਣ ਤੇ: ਪਾਸਵਰਡ ਅਟੱਲ ਤੌਰ ਤੇ ਗੁਆਚ ਜਾਣਗੇ",
        'export_format': "📁 ਐਕਸਪੋਰਟ ਫਾਰਮੈਟ",
        'export_format_desc': "ਸੈਟਿੰਗਾਂ ਇੱਕ ਸਿੰਗਲ ZIP ਫਾਈਲ ਵਿੱਚ ਸੰਭਾਲੀਆਂ ਜਾਣਗੀਆਂ:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "ਸੈਟਿੰਗਾਂ ਸਫਲਤਾਪੂਰਵਕ ਐਕਸਪੋਰਟ ਕੀਤੀਆਂ ਗਈਆਂ",
        'export_failed': "ਐਕਸਪੋਰਟ ਅਸਫਲ",
        'export_import_question': "ਕੀ ਤੁਸੀਂ ਹੁਣ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'export_password_question': "ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਪਾਸਵਰਡ ਡੀਕ੍ਰਿਪਟਡ ਐਕਸਪੋਰਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?\n(ਨਹੀਂ ਤਾਂ ਉਹ ਐਨਕ੍ਰਿਪਟਡ ਐਕਸਪੋਰਟ ਕੀਤੇ ਜਾਣਗੇ)",
        'export_decrypt': "ਡੀਕ੍ਰਿਪਟਡ ਐਕਸਪੋਰਟ ਕਰੋ",
        'export_encrypt': "ਐਨਕ੍ਰਿਪਟਡ ਐਕਸਪੋਰਟ ਕਰੋ",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " ਜਾਣਕਾਰੀ",
        'info_title': "PDF Dark View ਬਾਰੇ",
        'info_version': "ਵਰਜਨ",
        'info_author': "ਟੋਰਾਲਫ ਸ਼ੁਲਟਜ਼ (ਬਿਨਡੀਜ਼) ਦੁਆਰਾ ਵਿਕਸਤ",
        'info_copyright': "© 2026 ਬਿਨਡੀਜ਼",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "ਬਾਰੇ",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ਇੱਕ ਪਹੁੰਚਯੋਗ PDF ਦਰਸ਼ਕ ਹੈ ਜੋ ਵਿਸ਼ੇਸ਼ ਤੌਰ ਤੇ ਨਜ਼ਰ ਕਮਜ਼ੋਰੀ ਵਾਲੇ ਲੋਕਾਂ ਲਈ ਵਿਕਸਤ ਕੀਤਾ ਗਿਆ ਹੈ।</p>

            <p><strong>ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ:</strong></p>
            <ul>
                <li>ਕੰਟ੍ਰਾਸਟ ਭਰਪੂਰ, ਅਨੁਕੂਲਿਤ ਇੰਟਰਫੇਸ</li>
                <li>ਪੂਰਾ ਕੀਬੋਰਡ ਕੰਟਰੋਲ</li>
                <li>ਏਕੀਕ੍ਰਿਤ ਸਪੀਚ ਆਉਟਪੁੱਟ</li>
                <li>ਸਕੈਨ ਕੀਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਲਈ OCR</li>
                <li>ਵਿਆਪਕ ਸੰਪਾਦਨ ਸਾਧਨ</li>
            </ul>

            <p>50 ਤੋਂ ਵੱਧ ਭਾਸ਼ਾਵਾਂ ਸਮਰਥਿਤ ਹਨ – ਤਾਂ ਜੋ PDF ਸਾਰਿਆਂ ਲਈ ਪਹੁੰਚਯੋਗ ਹੋਣ।</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ",
        'info_features_intro': "PDF Dark View ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖੀਆਂ ਸੰਭਾਵਨਾਵਾਂ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>ਡਿਸਪਲੇ ਅਤੇ ਨੇਵੀਗੇਸ਼ਨ</strong> – ਡਾਰਕ/ਹਲਕਾ ਮੋਡ, ਪੰਨੇ ਪਲਟਣਾ, ਜ਼ੂਮ, ਪੰਨੇ ਤੇ ਛਾਲ</li>
            <li><strong>OCR (ਟੈਕਸਟ ਪਛਾਣ)</strong> – ਸਕੈਨ ਕੀਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਖੋਜਣਯੋਗ ਅਤੇ ਕਾਪੀ ਕਰਨਯੋਗ ਬਣਾਉਣਾ</li>
            <li><strong>ਸੰਪਾਦਨ</strong> – ਟੈਕਸਟ, ਕਰਾਸ, ਦਸਤਖਤ, ਚਿੱਤਰ ਅਤੇ ਆਕਾਰ ਪਾਉਣਾ</li>
            <li><strong>ਪੰਨਾ ਪ੍ਰਬੰਧਨ</strong> – ਮਿਟਾਉਣਾ, ਕੱਢਣਾ, ਪਾਉਣਾ, ਡ੍ਰੈਗ ਐਂਡ ਡ੍ਰੌਪ ਨਾਲ ਹਿਲਾਉਣਾ</li>
            <li><strong>ਐਕਸਪੋਰਟ</strong> – Word, Pages ਜਾਂ ਟੈਕਸਟ ਵਜੋਂ</li>
            <li><strong>ਸੁਰੱਖਿਆ</strong> – ਪਾਸਵਰਡ ਸੁਰੱਖਿਆ ਅਤੇ ਪ੍ਰਬੰਧਨ</li>
            <li><strong>ਪਹੁੰਚਯੋਗਤਾ</strong> – ਸਪੀਚ ਆਉਟਪੁੱਟ, ਕੀਬੋਰਡ ਕੰਟਰੋਲ, ਉੱਚ ਕੰਟ੍ਰਾਸਟ</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "ਓਪਰੇਸ਼ਨ",
        'info_accessibility': "♿ ਪਹੁੰਚਯੋਗਤਾ – ਪੂਰਾ ਕੀਬੋਰਡ ਕੰਟਰੋਲ",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 ਆਮ</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF ਖੋਲ੍ਹੋ</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> ਖੋਜ ਕਰੋ</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> ਡਾਰਕ/ਹਲਕਾ ਮੋਡ ਟੌਗਲ ਕਰੋ</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> ਛਾਪੋ</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> ਬਾਹਰ ਨਿਕਲੋ</div>

        <div class="shortcut-cat">📖 ਨੇਵੀਗੇਸ਼ਨ</div>
        <div class="shortcut-row"><kbd>ਤੀਰ ਕੁੰਜੀਆਂ</kbd> ਪੰਨੇ ਦਰ ਪੰਨੇ ਪਲਟੋ</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> ਪੰਨੇ ਤੇ ਜਾਓ</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> ਪਹਿਲਾ ਪੰਨਾ</div>
        <div class="shortcut-row"><kbd>Ende</kbd> ਆਖਰੀ ਪੰਨਾ</div>

        <div class="shortcut-cat">✏️ ਸੰਪਾਦਨ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> ਟੈਕਸਟ ਪਾਓ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> ਪੰਨੇ ਮਿਟਾਓ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> ਪੰਨੇ ਕੱਢੋ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> ਪੰਨੇ ਪਾਓ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> ਪੰਨੇ ਹਿਲਾਓ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> ਪੰਨਾ ਘੁਮਾਓ</div>

        <div class="shortcut-cat">🖼️ ਤੱਤ ਹਿਲਾਓ</div>
        <div class="shortcut-row"><kbd>ਤੀਰ ਕੁੰਜੀਆਂ</kbd> ਟੈਕਸਟ/ਚਿੱਤਰ/ਦਸਤਖਤ ਹਿਲਾਓ</div>
        <div class="shortcut-row"><kbd>Ctrl+ਤੀਰ ਕੁੰਜੀਆਂ</kbd> ਵੱਡੇ ਕਦਮਾਂ ਨਾਲ ਹਿਲਾਓ</div>
        <div class="shortcut-row"><kbd>Enter</kbd> ਸੰਭਾਲੋ</div>
        <div class="shortcut-row"><kbd>ESC</kbd> ਰੱਦ ਕਰੋ</div>

        <div class="shortcut-cat">🗣️ ਸਪੀਚ ਆਉਟਪੁੱਟ</div>
        <div class="shortcut-row"><kbd>F2</kbd> ਸਪੀਚ ਆਉਟਪੁੱਟ ਚਾਲੂ/ਬੰਦ</div>
        """,
        'info_contextmenu': "📌 ਮਹੱਤਵਪੂਰਨ: ਸਾਰੇ ਫੰਕਸ਼ਨ ਸੰਦਰਭ ਮੀਨੂ (ਸੱਜਾ-ਕਲਿਕ) ਰਾਹੀਂ ਵੀ ਪਹੁੰਚਯੋਗ ਹਨ!",
        'info_accessibility_hint': "💡 ਟਿਪ: ਸਪੀਚ ਆਉਟਪੁੱਟ (F2) ਅਭਿਮੁਖਤਾ ਨੂੰ ਸੌਖਾ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਮੀਨੂ ਅਤੇ ਡਾਇਲਾਗਾਂ ਤੇ ਪ੍ਰਤੀਕ੍ਰਿਆ ਦਿੰਦਾ ਹੈ।",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "ਲਾਇਸੰਸ ਅਤੇ ਇੰਪ੍ਰਿੰਟ",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 ਇੰਪ੍ਰਿੰਟ</strong><br>
        § 5 TMG ਅਨੁਸਾਰ ਜਾਣਕਾਰੀ:<br>
        ਟੋਰਾਲਫ ਸ਼ੁਲਟਜ਼<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        ਈ-ਮੇਲ: binhdiez64@gmail.com<br>
        ਸਮੱਗਰੀ ਲਈ ਜ਼ਿੰਮੇਵਾਰ: ਟੋਰਾਲਫ ਸ਼ੁਲਟਜ਼ (ਬਿਨਡੀਜ਼)<br><br>

        <strong>⚠️ ਜ਼ਿੰਮੇਵਾਰੀ ਤੋਂ ਇਨਕਾਰ</strong><br>
        ਸੌਫਟਵੇਅਰ ਨੂੰ ਬਹੁਤ ਸਾਵਧਾਨੀ ਨਾਲ ਵਿਕਸਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਸ਼ੁੱਧਤਾ, ਸੰਪੂਰਨਤਾ ਅਤੇ ਕਾਰਜਸ਼ੀਲਤਾ ਦੀ ਕੋਈ ਗਾਰੰਟੀ ਨਹੀਂ ਦਿੱਤੀ ਜਾਂਦੀ। ਵਰਤੋਂ ਆਪਣੀ ਜ਼ਿੰਮੇਵਾਰੀ ਤੇ ਹੈ।<br><br>

        <strong>📄 MIT-ਲਾਇਸੰਸ (ਨਿੱਜੀ ਵਰਤੋਂ)</strong><br>
        ਕਾਪੀਰਾਈਟ (c) 2026 ਟੋਰਾਲਫ ਸ਼ੁਲਟਜ਼ (ਬਿਨਡੀਜ਼)<br>
        ਇਜਾਜ਼ਤ: ਮੁਫ਼ਤ ਵਰਤੋਂ, ਨਿੱਜੀ ਤਬਦੀਲੀਆਂ, ਨਿੱਜੀ ਕਾਪੀਆਂ।<br>
        ਇਜਾਜ਼ਤ ਨਹੀਂ: ਵਿਕਰੀ, ਵਪਾਰਕ ਵਰਤੋਂ, ਕਾਪੀਰਾਈਟ ਨੋਟਿਸ ਹਟਾਉਣਾ।<br><br>

        <strong>🔧 ਤੀਜੀ-ਧਿਰ ਕੰਪੋਨੈਂਟਸ</strong><br>
        ਇਸ ਸੌਫਟਵੇਅਰ ਵਿੱਚ GPL, AGPL, Apache 2.0, BSD ਅਤੇ MIT-ਲਾਇਸੰਸਾਂ ਅਧੀਨ ਕੰਪੋਨੈਂਟਸ ਸ਼ਾਮਲ ਹਨ।<br>
        ਮੁੜ ਵੰਡਣ ਵੇਲੇ ਸੰਬੰਧਿਤ ਲਾਇਸੰਸ ਸ਼ਰਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਨੀ ਲਾਜ਼ਮੀ ਹੈ।<br><br>

        <strong>🌐 ਓਪਨ ਸੋਰਸ</strong><br>
        ਸਰੋਤ ਕੋਡ ਉਪਲਬਧ ਹੈ ਅਤੇ ਸੰਬੰਧਿਤ ਲਾਇਸੰਸ ਸ਼ਰਤਾਂ ਅਨੁਸਾਰ ਦੇਖਿਆ, ਬਦਲਿਆ ਅਤੇ ਮੁੜ ਵੰਡਿਆ ਜਾ ਸਕਦਾ ਹੈ।<br><br>

        © 2026 ਟੋਰਾਲਫ ਸ਼ੁਲਟਜ਼ (ਬਿਨਡੀਜ਼)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "ਧੰਨਵਾਦ",
        'info_credits': "ਓਪਨ-ਸੋਰਸ ਭਾਈਚਾਰੇ ਦਾ ਧੰਨਵਾਦ",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF ਪ੍ਰਕਿਰਿਆ</li>
            <li><strong>PyQt5</strong> – ਗ੍ਰਾਫਿਕਲ ਇੰਟਰਫੇਸ</li>
            <li><strong>Tesseract OCR</strong> – ਟੈਕਸਟ ਪਛਾਣ</li>
            <li><strong>OCRmyPDF</strong> – OCR ਏਕੀਕਰਣ</li>
            <li><strong>python-docx</strong> – Word ਐਕਸਪੋਰਟ</li>
            <li><strong>qtawesome</strong> – ਆਈਕਾਨ</li>
            <li><strong>DeepSeek</strong> – ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਸਹਾਇਤਾ (50+ ਭਾਸ਼ਾਵਾਂ)</li>
            <li><strong>ਸਾਰੇ ਉਪਭੋਗਤਾ</strong> – ਕੀਮਤੀ ਫੀਡਬੈਕ ਲਈ</li>
            <li><strong>ਓਪਨ-ਸੋਰਸ ਭਾਈਚਾਰਾ</strong> – ਸ਼ਾਨਦਾਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਲਈ</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "ਭਾਸ਼ਾਵਾਂ",
        'info_languages_header': "🌍 ਭਾਸ਼ਾ ਸਮਰਥਨ",
        'info_languages_html': """
        <div style="line-height:1.6;">
            <p>PDF Dark View ਵਰਤਮਾਨ ਵਿੱਚ <strong>62 ਭਾਸ਼ਾਵਾਂ</strong> ਸਮਰਥਨ ਕਰਦਾ ਹੈ – ਤਾਂ ਜੋ ਸੌਫਟਵੇਅਰ ਵਿਸ਼ਵ ਪੱਧਰ ਤੇ ਪਹੁੰਚਯੋਗ ਹੋ ਸਕੇ।</p>

            <p><strong>📖 ਪੂਰੀ ਭਾਸ਼ਾਵਾਂ ਦੀ ਸੂਚੀ (ਮਾਰਚ 2026 ਤੱਕ):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 ਅਫਰੀਕੀ</li>
                    <li>🇦🇱 ਅਲਬਾਨੀਆਈ (Shqip)</li>
                    <li>🇩🇿 ਅਰਬੀ (العربية)</li>
                    <li>🇮🇩 ਬਾਲੀਨੀ (Basa Bali)</li>
                    <li>🇧🇩 ਬੰਗਾਲੀ (বাংলা)</li>
                    <li>🇲🇲 ਬਰਮੀ (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 ਬੋਸਨੀਆਈ (Bosanski)</li>
                    <li>🇧🇬 ਬੁਲਗਾਰੀਆਈ (Български)</li>
                    <li>🇨🇳 ਚੀਨੀ (中文)</li>
                    <li>🇩🇰 ਡੈਨਿਸ਼ (Dansk)</li>
                    <li>🇩🇪 ਜਰਮਨ (Deutsch)</li>
                    <li>🇬🇧 ਅੰਗਰੇਜ਼ੀ (English)</li>
                    <li>🇪🇪 ਏਸਟੋਨੀਆਈ (Eesti)</li>
                    <li>🇫🇮 ਫਿਨਿਸ਼ (Suomi)</li>
                    <li>🇫🇷 ਫ੍ਰੈਂਚ (Français)</li>
                    <li>🇬🇷 ਯੂਨਾਨੀ (Ελληνικά)</li>
                    <li>🇮🇱 ਹਿਬਰੂ (עברית)</li>
                    <li>🇮🇳 ਹਿੰਦੀ (हिन्दी)</li>
                    <li>🇭🇷 ਕਰੋਏਸ਼ੀਆਈ (Hrvatski)</li>
                    <li>🇭🇺 ਹੰਗਰੀਆਈ (Magyar)</li>
                    <li>🇮🇩 ਇੰਡੋਨੇਸ਼ੀਆਈ (Bahasa Indonesia)</li>
                    <li>🇮🇪 ਆਇਰਿਸ਼ (Gaeilge)</li>
                    <li>🇮🇸 ਆਈਸਲੈਂਡਿਕ (Íslenska)</li>
                    <li>🇮🇹 ਇਤਾਲਵੀ (Italiano)</li>
                    <li>🇯🇵 ਜਪਾਨੀ (日本語)</li>
                    <li>🇰🇭 ਖਮੇਰ (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 ਕੋਰੀਆਈ (한국어)</li>
                    <li>🇱🇦 ਲਾਓਟੀਆਈ (ພາສາລາວ)</li>
                    <li>🇱🇻 ਲਾਤਵੀਆਈ (Latviešu)</li>
                    <li>🇱🇹 ਲਿਥੁਆਨੀਆਈ (Lietuvių)</li>
                    <li>🇱🇺 ਲਕਜ਼ਮਬਰਗਿਸ਼ (Lëtzebuergesch)</li>
                    <li>🇲🇾 ਮਲਯ (Bahasa Melayu)</li>
                    <li>🇮🇳 ਮਰਾਠੀ (मराठी)</li>
                    <li>🇲🇳 ਮੰਗੋਲੀਆਈ (Монгол)</li>
                    <li>🇳🇵 ਨੇਪਾਲੀ (नेपाली)</li>
                    <li>🇳🇱 ਡੱਚ (Nederlands)</li>
                    <li>🇳🇴 ਨਾਰਵੇਜੀਅਨ (Norsk)</li>
                    <li>🇦🇫 ਪਸ਼ਤੋ (پښتو)</li>
                    <li>🇮🇷 ਫ਼ਾਰਸੀ (فارسی)</li>
                    <li>🇵🇱 ਪੋਲਿਸ਼ (Polski)</li>
                    <li>🇵🇹 ਪੁਰਤਗਾਲੀ (Português)</li>
                    <li>🇮🇳 ਪੰਜਾਬੀ (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 ਰੋਮਾਨੀਆਈ (Română)</li>
                    <li>🇷🇺 ਰੂਸੀ (Русский)</li>
                    <li>🇸🇪 ਸਵੀਡਿਸ਼ (Svenska)</li>
                    <li>🇷🇸 ਸਰਬੀਆਈ (Српски)</li>
                    <li>🇸🇰 ਸਲੋਵਾਕ (Slovenčina)</li>
                    <li>🇸🇮 ਸਲੋਵੇਨੀਆਈ (Slovenščina)</li>
                    <li>🇪🇸 ਸਪੇਨੀ (Español)</li>
                    <li>🇹🇿 ਸਵਾਹਿਲੀ (Kiswahili)</li>
                    <li>🇵🇭 ਟਾਗਾਲੋਗ (Filipino)</li>
                    <li>🇮🇳 ਤਾਮਿਲ (தமிழ்)</li>
                    <li>🇮🇳 ਤੇਲਗੂ (తెలుగు)</li>
                    <li>🇹🇭 ਥਾਈ (ไทย)</li>
                    <li>🇨🇿 ਚੈੱਕ (Čeština)</li>
                    <li>🇹🇷 ਤੁਰਕੀ (Türkçe)</li>
                    <li>🇺🇦 ਯੂਕਰੇਨੀਆਈ (Українська)</li>
                    <li>🇵🇰 ਉਰਦੂ (اردو)</li>
                    <li>🇻🇳 ਵੀਅਤਨਾਮੀ (Tiếng Việt)</li>
                    <li>🇸🇳 ਵੋਲੋਫ (Wolof)</li>
                    <li>🇺🇸 ਯਿੱਦਿਸ਼ (ייִדיש)</li>
                    <li>🇿🇦 ਜ਼ੁਲੂ (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 ਆਪਣੀਆਂ ਭਾਸ਼ਾਵਾਂ ਸ਼ਾਮਲ ਕਰੋ:</strong><br>
                ਕੀ ਤੁਸੀਂ ਕੋਈ ਅਜਿਹੀ ਭਾਸ਼ਾ ਚਾਹੁੰਦੇ ਹੋ ਜੋ ਅਜੇ ਸ਼ਾਮਲ ਨਹੀਂ ਹੈ? ਬਸ ਆਪਣੀ ਖੁਦ ਦੀ ਡਿਕਸ਼ਨਰੀ ਫਾਈਲ (<code>sprache_xx.py</code>) ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਨਾਲ ਰੱਖੋ – ਸੌਫਟਵੇਅਰ ਇਸਨੂੰ ਆਪਣੇ ਆਪ ਪਛਾਣ ਲਵੇਗਾ। ਜੇਕਰ ਕਿਸੇ ਖਾਸ ਅਨੁਵਾਦ ਵਿੱਚ ਦਿਲਚਸਪੀ ਹੋਵੇ ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ ਮੇਰੇ ਨਾਲ ਸੰਪਰਕ ਕਰੋ।
            </div>

            <p><strong>🙏 ਵਿਸ਼ੇਸ਼ ਧੰਨਵਾਦ:</strong> 62 ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਸਾਰੀਆਂ ਡਿਕਸ਼ਨਰੀਆਂ ਦੇ ਅਨੁਵਾਦ ਵਿੱਚ ਸਹਾਇਤਾ ਲਈ ਡੀਪਸੀਕ ਦਾ।</p>

            <p>📧 ਅਨੁਵਾਦਾਂ ਲਈ ਸੰਪਰਕ: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "ਗਲਤੀ",
        'error_occurred': "ਇੱਕ ਗਲਤੀ ਵਾਪਰੀ",
        'error_pdf_load': "PDF ਲੋਡ ਕਰਨ ਵੇਲੇ ਗਲਤੀ",
        'error_pdf_save': "PDF ਸੰਭਾਲਣ ਵੇਲੇ ਗਲਤੀ",
        'error_ocr': "ਟੈਕਸਟ ਪਛਾਣ ਵਿੱਚ ਗਲਤੀ",
        'error_no_pdf': "ਕੋਈ PDF ਲੋਡ ਨਹੀਂ ਕੀਤੀ ਗਈ",
        'error_page_not_found': "ਪੰਨਾ ਨਹੀਂ ਮਿਲਿਆ",
        'error_invalid_range': "ਅਵੈਧ ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ",
        'error_file_not_found': "ਫਾਈਲ ਨਹੀਂ ਮਿਲੀ",
        'error_permission': "ਕੋਈ ਇਜਾਜ਼ਤ ਨਹੀਂ",
        'error_unknown': "ਅਣਜਾਣ ਗਲਤੀ",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "ਸਫਲ",
        'success_operation': "ਕਾਰਵਾਈ ਸਫਲਤਾਪੂਰਵਕ ਪੂਰੀ ਹੋਈ",
        'success_saved': "ਸਫਲਤਾਪੂਰਵਕ ਸੰਭਾਲਿਆ ਗਿਆ",
        'success_exported': "ਸਫਲਤਾਪੂਰਵਕ ਐਕਸਪੋਰਟ ਕੀਤਾ ਗਿਆ",
        'success_imported': "ਸਫਲਤਾਪੂਰਵਕ ਆਯਾਤ ਕੀਤਾ ਗਿਆ",
        'success_deleted': "ਸਫਲਤਾਪੂਰਵਕ ਮਿਟਾਇਆ ਗਿਆ",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "ਪੁਸ਼ਟੀ",
        'confirm_yes': "ਹਾਂ",
        'confirm_no': "ਨਹੀਂ",
        'confirm_ok': "ਠੀਕ ਹੈ",
        'confirm_cancel': "ਰੱਦ ਕਰੋ",
        'confirm_delete': "ਮਿਟਾਓ",
        'confirm_overwrite': "ਓਵਰਰਾਈਟ ਕਰੋ",
        'confirm_continue': "ਜਾਰੀ ਰੱਖੋ",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'progress_saving': "PDF ਸੰਭਾਲੀ ਜਾ ਰਹੀ ਹੈ...",
        'progress_exporting': "PDF ਐਕਸਪੋਰਟ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'progress_processing': "ਪ੍ਰਕਿਰਿਆ ਚੱਲ ਰਹੀ ਹੈ...",
        'progress_wait': "ਕਿਰਪਾ ਕਰਕੇ ਉਡੀਕ ਕਰੋ...",
        'progress_preparing': "ਤਿਆਰੀ...",
        'progress_finalizing': "ਅੰਤਿਮ ਰੂਪ ਦਿੱਤਾ ਜਾ ਰਿਹਾ ਹੈ...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "ਚਿੱਟਾ",
        'color_black': "ਕਾਲਾ",
        'color_red': "ਲਾਲ",
        'color_green': "ਹਰਾ",
        'color_blue': "ਨੀਲਾ",
        'color_yellow': "ਪੀਲਾ",
        'color_magenta': "ਮੈਜੈਂਟਾ",
        'color_cyan': "ਸਾਇਆਨ",
        'color_orange': "ਸੰਤਰੀ",
        'color_gray': "ਸਲੇਟੀ",
        'color_custom': "ਰੰਗ ਚੋਣ",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&ਫਾਈਲ",
        'menu_edit': "&ਸੰਪਾਦਨ",
        'menu_view': "&ਦ੍ਰਿਸ਼",
        'menu_tools': "&ਔਜ਼ਾਰ",
        'menu_settings': "&ਸੈਟਿੰਗਾਂ",
        'menu_help': "&ਮਦਦ",
        'menu_language': "🌐 ਭਾਸ਼ਾ",
        'menu_guides': "&ਮਾਰਗਦਰਸ਼ਨ",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&ਖੋਲ੍ਹੋ",
        'file_save_as': "&ਇਸ ਤਰ੍ਹਾਂ ਸੰਭਾਲੋ...",
        'file_protect': "ਦਸਤਾਵੇਜ਼ &ਸੁਰੱਖਿਅਤ ਕਰੋ...",
        'file_export': "&ਐਕਸਪੋਰਟ ਕਰੋ",
        'file_export_pages': "Pages ਵਜੋਂ ਐਕਸਪੋਰਟ ਕਰੋ",
        'file_export_word': "DOCX ਵਜੋਂ ਐਕਸਪੋਰਟ ਕਰੋ",
        'file_export_text': "TXT ਵਜੋਂ ਐਕਸਪੋਰਟ ਕਰੋ",
        'file_print_now': "&ਹੁਣੇ ਛਾਪੋ",
        'file_print': "&ਛਾਪੋ",
        'file_close': "&ਬੰਦ ਕਰੋ",
        'file_quit': "&ਬਾਹਰ ਨਿਕਲੋ",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&ਖੋਜ ਕਰੋ",
        'edit_ocr': " OCR ਕਰੋ",
        'edit_rotate': "ਪੰਨਾ &ਘੁਮਾਓ",
        'edit_rotate_all': "&ਸਾਰੇ ਪੰਨੇ ਘੁਮਾਓ",
        'edit_delete_pages': "ਪੰਨੇ &ਮਿਟਾਓ",
        'edit_extract_pages': "ਪੰਨੇ &ਕੱਢੋ",
        'edit_insert_pages': "ਪੰਨੇ &ਪਾਓ",
        'edit_move_pages': "ਪੰਨੇ &ਹਿਲਾਓ",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " ਟੈਕਸਟ ਅਤੇ ਕਰਾਸ ਪਾਓ",
        'text_insert': " ਟੈਕਸਟ ਪਾਓ",
        'cross_insert': " ਕਰਾਸ ਪਾਓ",
        'text_customize': " ਟੈਕਸਟ ਵਿਵਸਥਿਤ ਕਰੋ",
        'cross_customize': " ਇਸ ਕਰਾਸ ਨੂੰ ਵਿਵਸਥਿਤ ਕਰੋ",
        'cross_customize_all': " ਸਾਰੇ ਕਰਾਸ ਵਿਵਸਥਿਤ ਕਰੋ",
        'text_discard': " ਇਸ ਟੈਕਸਟ / ਕਰਾਸ ਨੂੰ ਰੱਦ ਕਰੋ",
        'text_discard_all': " ਸਾਰੇ ਟੈਕਸਟ ਅਤੇ ਕਰਾਸ ਰੱਦ ਕਰੋ",
        'text_save_all': " ਸਾਰੇ ਟੈਕਸਟ ਅਤੇ ਕਰਾਸ ਸੰਭਾਲੋ",
        'text_guide': " ਟੈਕਸਟ ਇਨਪੁਟ / ਟੈਕਸਟ ਬਲਾਕ - ਮਾਰਗਦਰਸ਼ਨ",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " ਦਸਤਖਤ ਪਾਓ",
        'signature_settings_menu': " ਸੈਟਿੰਗਾਂ...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " ਚਿੱਤਰ ਪਾਓ",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " ਆਕਾਰ ਪਾਓ",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&ਟੈਕਸਟ ਵਿੰਡੋ ਦਿਖਾਓ",
        'view_zoom': "&ਜ਼ੂਮ",
        'view_zoom_page': "&ਪੰਨੇ ਦੀ ਚੌੜਾਈ (ਸਟੈਂਡਰਡ)",
        'view_zoom_two': "&ਦੋ ਪੰਨੇ",
        'view_zoom_overview': "&ਸੰਖੇਪ (ਇੱਕ ਤੋਂ ਵੱਧ ਪੰਨੇ)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&ਪਹੁੰਚਯੋਗਤਾ ਸਹਾਇਤਾ",
        'settings_voice': "ਸਪੀਚ ਆਉਟਪੁੱਟ",
        'settings_voice_tooltip': "ਸਕ੍ਰੀਨ ਰੀਡਰ ਦੇ ਸਪੀਚ ਆਉਟਪੁੱਟ ਨੂੰ ਵਾਧੂ ਜਾਣਕਾਰੀ ਨਾਲ ਪੂਰਕ ਕਰਦਾ ਹੈ",
        'settings_signature': "&ਦਸਤਖਤ-ਸੈਟਿੰਗਾਂ",
        'settings_password': "&ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ",
        'settings_backup': "ਤਬਦੀਲੀਆਂ ਤੋਂ ਪਹਿਲਾਂ ਬੈਕਅੱਪ ਬਣਾਓ",
        'settings_export_import': "&ਸੈਟਿੰਗਾਂ ਐਕਸਪੋਰਟ ਕਰੋ / ਆਯਾਤ ਕਰੋ",
        'settings_export': "&ਸਾਰੀਆਂ ਸੈਟਿੰਗਾਂ ਐਕਸਪੋਰਟ ਕਰੋ...",
        'settings_import': "&ਸਾਰੀਆਂ ਸੈਟਿੰਗਾਂ ਆਯਾਤ ਕਰੋ...",
        'settings_export_info': "&ਕੀ ਐਕਸਪੋਰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "ਚਾਲੂ",
        'voice_off': "ਬੰਦ",
        'voice_toggle': "ਸਪੀਚ ਆਉਟਪੁੱਟ {0}",
        'voice_speed': "ਗਤੀ {0} ਪ੍ਰਤੀਸ਼ਤ",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "ਟੂਲ ਨਹੀਂ ਮਿਲਿਆ:\n{0}\n\nBASE_DIR: {1}\nਯਕੀਨੀ ਬਣਾਓ ਕਿ PDF ਟੂਲ ਡਾਇਰੈਕਟਰੀ {1} ਵਿੱਚ ਸਥਾਪਤ ਹਨ।",
        'tool_started': "{0} ਸ਼ੁਰੂ ਹੋ ਗਿਆ",
        'tool_start_failed': "ਸ਼ੁਰੂ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਿਆ",
        'process_error_failed_to_start': "ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਨਹੀਂ ਕੀਤੀ ਜਾ ਸਕੀ। ਕੀ ਫਾਈਲ ਮੌਜੂਦ ਹੈ?",
        'process_error_crashed': "ਸ਼ੁਰੂ ਕਰਦੇ ਸਮੇਂ ਪ੍ਰਕਿਰਿਆ ਕਰੈਸ਼ ਹੋ ਗਈ।",
        'process_error_timeout': "ਪ੍ਰਕਿਰਿਆ ਟਾਈਮਆਊਟ ਹੋ ਗਈ।",
        'process_error_write': "ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਲਿਖਣ ਦੀ ਗਲਤੀ।",
        'process_error_read': "ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਪੜ੍ਹਨ ਦੀ ਗਲਤੀ।",
        'process_error_unknown': "ਅਣਜਾਣ ਪ੍ਰਕਿਰਿਆ ਗਲਤੀ",
        'process_command': "ਕਮਾਂਡ",
        'process_normal_exit': "ਆਮ ਤੌਰ ਤੇ ਖਤਮ ਹੋਇਆ",
        'process_crashed': "ਕਰੈਸ਼ ਹੋਇਆ",
        'process_nonzero_exit': "{0} ਗਲਤੀ ਕੋਡ {1} ਨਾਲ ਖਤਮ ਹੋਇਆ",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "ਰੱਦ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'move_cancelling': "ਹਿਲਾਉਣਾ ਰੱਦ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ",
        'opening_pdf': "PDF ਖੋਲ੍ਹੀ ਜਾ ਰਹੀ ਹੈ...",
        'loading_document': "ਦਸਤਾਵੇਜ਼ ਲੋਡ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'pdf_opened': "PDF ਖੋਲ੍ਹੀ ਗਈ",
        'pages_found_moving': "{0} ਪੰਨੇ ਮਿਲੇ, {1} ਹਿਲਾਉਣ ਲਈ",
        'creating_backup': "ਬੈਕਅੱਪ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ...",
        'backup_description': "ਅਸਲ ਫਾਈਲ ਸੁਰੱਖਿਅਤ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'backup_saved_as': "ਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ: {0}",
        'error_format': "ਗਲਤੀ: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "ਖੋਜ ਰੀਸੈਟ ਕੀਤੀ ਗਈ",
        'page_header_simple': "=== ਪੰਨਾ {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ – ਮਾਰਗਦਰਸ਼ਨ",
        'password_guide_voice': "ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ ਦਾ ਮਾਰਗਦਰਸ਼ਨ। ਕਿਰਪਾ ਕਰਕੇ ਨੋਟਿਸ ਪੜ੍ਹੋ।",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ – ਵਿਸਤ੍ਰਿਤ ਮਾਰਗਦਰਸ਼ਨ</strong></p>

        <p><strong>1. PDF ਲਈ ਪਾਸਵਰਡ ਸੁਰੱਖਿਆ</strong></p>
        <ul>
        <li>ਪਾਸਵਰਡ-ਸੁਰੱਖਿਅਤ PDF ਖੋਲ੍ਹਣ ਵੇਲੇ ਇੱਕ ਡਾਇਲਾਗ ਦਿਖਾਈ ਦਿੰਦਾ ਹੈ ਜਿੱਥੇ ਤੁਸੀਂ ਪਾਸਵਰਡ ਟਾਈਪ ਕਰ ਸਕਦੇ ਹੋ।</li>
        <li>ਤੁਸੀਂ ਪਾਸਵਰਡ ਨੂੰ ਐਨਕ੍ਰਿਪਟ ਕਰਕੇ ਸੰਭਾਲ ਸਕਦੇ ਹੋ, ਤਾਂ ਜੋ ਤੁਹਾਨੂੰ ਇਸਨੂੰ ਹਰ ਵਾਰ ਮੁੜ ਟਾਈਪ ਨਾ ਕਰਨਾ ਪਵੇ (ਚੈਕਬਾਕਸ "ਪਾਸਵਰਡ ਸੰਭਾਲੋ")।</li>
        <li>"ਪਾਸਵਰਡ ਹਟਾਓ" ਬਟਨ ਨਾਲ ਤੁਸੀਂ PDF ਦੀ ਇੱਕ ਡੀਕ੍ਰਿਪਟਡ ਕਾਪੀ ਬਣਾ ਸਕਦੇ ਹੋ ਅਤੇ ਡਾਟਾਬੇਸ ਤੋਂ ਪਾਸਵਰਡ ਮਿਟਾ ਸਕਦੇ ਹੋ।</li>
        </ul>

        <p><strong>2. ਮਾਸਟਰ ਪਾਸਵਰਡ</strong></p>
        <ul>
        <li>ਮਾਸਟਰ ਪਾਸਵਰਡ ਸਾਰੇ ਸੰਭਾਲੇ ਗਏ PDF ਪਾਸਵਰਡਾਂ ਦੀ ਪਹੁੰਚ ਦੀ ਰੱਖਿਆ ਕਰਦਾ ਹੈ।</li>
        <li><strong>ਸੈੱਟਅੱਪ:</strong> "ਸੈਟਿੰਗਾਂ → ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ → ਮਾਸਟਰ ਪੀਡਬਲਯੂ ਸੈਟਿੰਗਾਂ" ਤੇ ਜਾਓ ਅਤੇ "ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟਅੱਪ ਕਰੋ" ਤੇ ਕਲਿੱਕ ਕਰੋ। ਇੱਕ ਮਜ਼ਬੂਤ ਪਾਸਵਰਡ ਚੁਣੋ (ਘੱਟੋ-ਘੱਟ 8 ਅੱਖਰ)।</li>
        <li><strong>ਬਦਲੋ:</strong> ਸਫਲ ਪ੍ਰਮਾਣੀਕਰਨ ਤੋਂ ਬਾਅਦ ਤੁਸੀਂ ਮਾਸਟਰ ਪਾਸਵਰਡ ਬਦਲ ਸਕਦੇ ਹੋ।</li>
        <li><strong>ਹਟਾਓ:</strong> ਜੇਕਰ ਤੁਸੀਂ ਮਾਸਟਰ ਪਾਸਵਰਡ ਮਿਟਾਉਂਦੇ ਹੋ, ਤਾਂ ਸਾਰੇ ਸੰਭਾਲੇ ਗਏ ਪਾਸਵਰਡ ਅਟੱਲ ਤੌਰ ਤੇ ਮਿਟਾ ਦਿੱਤੇ ਜਾਣਗੇ। ਤੁਸੀਂ ਪਹਿਲਾਂ ਇੱਕ ਬੈਕਅੱਪ ਐਕਸਪੋਰਟ ਕਰ ਸਕਦੇ ਹੋ।</li>
        <li>ਪ੍ਰਤੀ ਸੈਸ਼ਨ ਇੱਕ ਵਾਰ ਤੁਹਾਨੂੰ ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ, ਸੁਰੱਖਿਅਤ ਫੰਕਸ਼ਨਾਂ (ਜਿਵੇਂ ਪਾਸਵਰਡ ਵੇਖਣਾ) ਨੂੰ ਪਹੁੰਚ ਕਰਨ ਦੇ ਯੋਗ ਹੋਣ ਲਈ।</li>
        </ul>

        <p><strong>3. ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ (ਸੂਚੀ)</strong></p>
        <ul>
        <li>"ਸੈਟਿੰਗਾਂ → ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ" ਅਧੀਨ ਤੁਸੀਂ ਉਹਨਾਂ ਦੇ ਐਨਕ੍ਰਿਪਟਡ ਪਾਸਵਰਡਾਂ ਦੇ ਨਾਲ ਸਾਰੀਆਂ ਸੰਭਾਲੀਆਂ ਗਈਆਂ PDF ਦੀ ਇੱਕ ਟੇਬਲ ਖੋਲ੍ਹਦੇ ਹੋ।</li>
        <li><strong>ਮਾਸਟਰ ਪਾਸਵਰਡ ਤੋਂ ਬਿਨਾਂ:</strong> ਤੁਸੀਂ ਸਿਰਫ ਐਂਟਰੀਆਂ ਮਿਟਾ ਸਕਦੇ ਹੋ – ਪਾਸਵਰਡ ਲੁਕੇ ਰਹਿੰਦੇ ਹਨ।</li>
        <li><strong>ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ (ਪ੍ਰਮਾਣਿਤ):</strong> ਤੁਸੀਂ ਪਾਸਵਰਡ ਵੇਖ ਸਕਦੇ ਹੋ, ਕਾਪੀ ਕਰ ਸਕਦੇ ਹੋ, ਐਕਸਪੋਰਟ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਮਿਟਾ ਸਕਦੇ ਹੋ।</li>
        <li><strong>ਐਕਸਪੋਰਟ:</strong> ਇੱਕ ਫਾਰਮੈਟ ਚੁਣੋ (JSON, CSV, TXT) ਅਤੇ ਸੂਚੀ ਸੰਭਾਲੋ। ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਹੋਣ ਤੇ ਤੁਸੀਂ ਫੈਸਲਾ ਕਰ ਸਕਦੇ ਹੋ ਕਿ ਪਾਸਵਰਡ ਸਪਸ਼ਟ ਟੈਕਸਟ ਵਿੱਚ ਐਕਸਪੋਰਟ ਕਰਨੇ ਹਨ ਜਾਂ ਐਨਕ੍ਰਿਪਟਡ ਰਹਿਣੇ ਹਨ।</li>
        <li><strong>ਆਯਾਤ:</strong> ਪਹਿਲਾਂ ਐਕਸਪੋਰਟ ਕੀਤੀ ZIP ਫਾਈਲ (ਸੈਟਿੰਗਾਂ ਸਮੇਤ) "ਸੈਟਿੰਗਾਂ → ਸੈਟਿੰਗਾਂ ਐਕਸਪੋਰਟ/ਆਯਾਤ" ਰਾਹੀਂ ਮੁੜ ਪੜ੍ਹੀ ਜਾ ਸਕਦੀ ਹੈ। ਸਾਵਧਾਨ: ਮੌਜੂਦਾ ਡਾਟਾ ਓਵਰਰਾਈਟ ਹੋ ਜਾਵੇਗਾ!</li>
        </ul>

        <p><strong>4. ਪਾਸਵਰਡ ਜਨਰੇਟਰ</strong></p>
        <ul>
        <li>ਪਾਸਵਰਡ ਡਾਇਲਾਗ ਵਿੱਚ (ਜਿਵੇਂ PDF ਸੁਰੱਖਿਅਤ ਕਰਦੇ ਸਮੇਂ) ਤੁਹਾਨੂੰ ਇਨਪੁਟ ਫੀਲਡ ਦੇ ਸੱਜੇ ਪਾਸੇ ਇੱਕ ਪਾਸਾ ਬਟਨ 🎲 ਮਿਲੇਗਾ।</li>
        <li>ਪਾਸਵਰਡ ਜਨਰੇਟਰ ਖੋਲ੍ਹਣ ਲਈ ਇਸ ਤੇ ਕਲਿੱਕ ਕਰੋ। ਤੁਸੀਂ ਲੰਬਾਈ, ਅੱਖਰ ਸੈੱਟ (ਵੱਡੇ ਅੱਖਰ, ਛੋਟੇ ਅੱਖਰ, ਅੰਕ, ਵਿਸ਼ੇਸ਼ ਚਿੰਨ੍ਹ) ਅਤੇ ਬਿਹਤਰ ਪੜ੍ਹਨਯੋਗਤਾ ਲਈ ਵਿਭਾਜਕ ਸੈੱਟ ਕਰ ਸਕਦੇ ਹੋ।</li>
        <li>ਉਤਪੰਨ ਪਾਸਵਰਡ ਸਿੱਧਾ ਲਿਆ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਲੋੜ ਪੈਣ ਤੇ ਕਾਪੀ ਵੀ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।</li>
        </ul>

        <p><strong>5. ਮਹੱਤਵਪੂਰਨ ਸੁਰੱਖਿਆ ਨੋਟਿਸ</strong></p>
        <ul>
        <li>ਸੰਭਾਲੇ ਗਏ ਪਾਸਵਰਡ AES-256 ਐਨਕ੍ਰਿਪਟਡ ਰੂਪ ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਕੁੰਜੀ ਤੁਹਾਡੇ ਮਾਸਟਰ ਪਾਸਵਰਡ ਤੋਂ ਪ੍ਰਾਪਤ ਕੀਤੀ ਜਾਂਦੀ ਹੈ (ਜੇਕਰ ਸੈੱਟ ਹੈ) ਜਾਂ ਇੱਕ ਨਿਸ਼ਚਿਤ ਮੁੱਲ ਤੋਂ (ਮਾਸਟਰ ਪਾਸਵਰਡ ਤੋਂ ਬਿਨਾਂ)।</li>
        <li>ਮਾਸਟਰ ਪਾਸਵਰਡ ਤੋਂ ਬਿਨਾਂ ਪਾਸਵਰਡ ਐਨਕ੍ਰਿਪਟਡ ਹੋਣ ਦੇ ਬਾਵਜੂਦ, ਕੁੰਜੀ ਪ੍ਰੋਗਰਾਮ ਵਿੱਚ ਸਟੋਰ ਕੀਤੀ ਜਾਂਦੀ ਹੈ – ਤੁਹਾਡੀਆਂ ਫਾਈਲਾਂ ਤੱਕ ਪਹੁੰਚ ਰੱਖਣ ਵਾਲਾ ਹਮਲਾਵਰ ਉਹਨਾਂ ਨੂੰ ਡੀਕ੍ਰਿਪਟ ਕਰ ਸਕਦਾ ਹੈ। ਇਸ ਲਈ ਅਸੀਂ ਮਾਸਟਰ ਪਾਸਵਰਡ ਦੀ ਵਰਤੋਂ ਦੀ ਦ੍ਰਿੜਤਾ ਨਾਲ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।</li>
        <li>ਪਾਸਵਰਡ ਡਾਟਾਬੇਸ `Daten/passwords.json` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹੈ। ਨਿਯਮਤ ਬੈਕਅੱਪ ਬਣਾਓ, ਖਾਸ ਕਰਕੇ ਮਾਸਟਰ ਪਾਸਵਰਡ ਹਟਾਉਣ ਤੋਂ ਪਹਿਲਾਂ।</li>
        <li>ਮਾਸਟਰ ਪਾਸਵਰਡ ਗੁਆਉਣ ਤੇ ਸਾਰੇ ਸੰਭਾਲੇ ਗਏ ਪਾਸਵਰਡ ਅਟੱਲ ਤੌਰ ਤੇ ਗੁਆਚ ਜਾਂਦੇ ਹਨ।</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # Neu ab 2026-03-19
        # (32 Info und alles ab 53 in den anderen Wörterbüchern ersetzen)
        # ============================================

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "ਉਲਟਾਉਣ ਦਾ ਮੋਡ",
        'invert_mode_classic': "ਕਲਾਸਿਕ (ਸਾਰੇ ਰੰਗ ਉਲਟਾਓ)",
        'invert_mode_smart': "ਬੁੱਧੀਮਾਨ (ਸਿਰਫ ਚਮਕ ਉਲਟਾਓ)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "ਗ੍ਰੇਸਕੇਲ ਥ੍ਰੈਸ਼ਹੋਲਡ",
        'gray_threshold_10': "10% (ਸਖ਼ਤ)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (ਸਟੈਂਡਰਡ)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (ਨਰਮ)",
        'threshold_changed': "ਥ੍ਰੈਸ਼ਹੋਲਡ {0}% ਤੇ ਸੈੱਟ ਕੀਤਾ ਗਿਆ",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "ਗ੍ਰੇਸਕੇਲ ਥ੍ਰੈਸ਼ਹੋਲਡ – ਵਿਆਖਿਆ",
        'threshold_guide_text': "ਗ੍ਰੇਸਕੇਲ ਥ੍ਰੈਸ਼ਹੋਲਡ ਇਹ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਬੁੱਧੀਮਾਨ ਡਾਰਕ ਮੋਡ ਵਿੱਚ ਕਿਹੜੇ ਪਿਕਸਲ 'ਸਲੇਟੀ' ਮੰਨੇ ਜਾਣਗੇ ਅਤੇ ਉਲਟਾਏ ਜਾਣਗੇ।\n\n"
                                "• ਇੱਕ ਘੱਟ ਮੁੱਲ (10%) ਲਗਭਗ ਸੰਪੂਰਨ ਸਲੇਟੀ ਟੋਨਾਂ ਨੂੰ ਉਲਟਾਉਂਦਾ ਹੈ – ਰੰਗੀਨ ਤੱਤ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਰਹਿੰਦੇ ਹਨ।\n"
                                "• ਇੱਕ ਉੱਚ ਮੁੱਲ (50%) ਥੋੜ੍ਹੇ ਰੰਗੀਨ ਪਿਕਸਲਾਂ ਨੂੰ ਵੀ ਉਲਟਾਉਂਦਾ ਹੈ – ਇਸ ਨਾਲ ਕੰਟ੍ਰਾਸਟ ਵਧਦਾ ਹੈ, ਪਰ ਰੰਗ ਵਿਗੜ ਸਕਦੇ ਹਨ।\n\n"
                                "ਅਨੁਕੂਲ ਮੁੱਲ ਦਸਤਾਵੇਜ਼ ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ। ਸ਼ੁੱਧ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ਾਂ ਲਈ 30–40% ਅਕਸਰ ਆਦਰਸ਼ ਹੁੰਦਾ ਹੈ, ਰੰਗੀਨ ਗ੍ਰਾਫਿਕਸ ਲਈ 10–20%।\n\n"
                                "ਤੁਸੀਂ 'ਸੈਟਿੰਗਾਂ' ਮੀਨੂ ਰਾਹੀਂ ਕਿਸੇ ਵੀ ਸਮੇਂ ਮੁੱਲ ਵਿਵਸਥਿਤ ਕਰ ਸਕਦੇ ਹੋ – PDF ਫਿਰ ਤੁਰੰਤ ਮੁੜ ਲੋਡ ਹੋ ਜਾਵੇਗੀ।\n\n"
                                "ਧਿਆਨ ਦਿਓ:\n* ਫੋਟੋਆਂ ਅਤੇ ਚਿੱਤਰ ਸਿਰਫ ਹਲਕੇ ਮੋਡ ਵਿੱਚ ਹੀ ਸਹੀ ਢੰਗ ਨਾਲ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ!\n* ਉਲਟਾਉਣ ਦੀਆਂ ਸੈਟਿੰਗਾਂ ਸਿਰਫ ਡਾਰਕ ਮੋਡ ਸਰਗਰਮ ਹੋਣ ਤੇ ਹੀ ਦਿਖਾਈਆਂ ਜਾਂਦੀਆਂ ਹਨ।",
        'threshold_guide_voice': "ਗ੍ਰੇਸਕੇਲ ਥ੍ਰੈਸ਼ਹੋਲਡ ਇਹ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਬੁੱਧੀਮਾਨ ਡਾਰਕ ਮੋਡ ਕਿੰਨਾ ਦਖ਼ਲ ਦਿੰਦਾ ਹੈ। ਘੱਟ ਮੁੱਲ ਰੰਗਾਂ ਦੀ ਰੱਖਿਆ ਕਰਦਾ ਹੈ, ਉੱਚ ਮੁੱਲ ਕੰਟ੍ਰਾਸਟ ਵਧਾਉਂਦਾ ਹੈ।",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF ਖੋਲ੍ਹੀ ਜਾ ਰਹੀ ਹੈ...",
        'progress_loading_document': "ਦਸਤਾਵੇਜ਼ ਲੋਡ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_pdf_opened': "PDF ਖੋਲ੍ਹੀ ਗਈ",
        'progress_creating_backup': "ਬੈਕਅੱਪ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_backup_description': "ਅਸਲ ਫਾਈਲ ਸੁਰੱਖਿਅਤ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'progress_backup_created': "ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ",
        'progress_backup_saved_as': "ਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ: {0}",
        'progress_analyzing_start': "ਵਿਸ਼ਲੇਸ਼ਣ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_searching_empty': "ਖਾਲੀ ਪੰਨੇ ਖੋਜੇ ਜਾ ਰਹੇ ਹਨ...",
        'progress_page_empty': "ਪੰਨਾ {0} ਖਾਲੀ ਹੈ",
        'progress_page_keep': "ਪੰਨਾ {0} ਰੱਖਿਆ ਜਾਵੇਗਾ",
        'progress_analysis_complete': "ਵਿਸ਼ਲੇਸ਼ਣ ਮੁਕੰਮਲ",
        'progress_empty_found': "{0} ਖਾਲੀ ਪੰਨੇ ਮਿਲੇ",
        'progress_current_page': "ਮੌਜੂਦਾ ਪੰਨਾ",
        'progress_mark_delete': "ਮਿਟਾਉਣ ਲਈ ਨਿਸ਼ਾਨਬੱਧ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ",
        'progress_range_selected': "ਪੰਨਿਆਂ ਦੀ ਰੇਂਜ {0}-{1}",
        'progress_deleting_pages': "{0} ਪੰਨੇ ਮਿਟਾਏ ਜਾ ਰਹੇ ਹਨ",
        'progress_creating_new_pdf': "ਨਵੀਂ PDF ਬਣਾਈ ਜਾ ਰਹੀ ਹੈ...",
        'progress_transferring_pages': "ਪੰਨੇ ਟ੍ਰਾਂਸਫਰ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ",
        'progress_keeping_page': "ਪੰਨਾ {0} ਰੱਖਿਆ ਜਾਵੇਗਾ ({1}/{2})",
        'progress_saving_pdf': "PDF ਸੰਭਾਲੀ ਜਾ ਰਹੀ ਹੈ...",
        'progress_optimizing': "ਫਾਈਲ ਆਕਾਰ ਅਨੁਕੂਲਿਤ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_finalizing': "ਅੰਤਿਮ ਰੂਪ ਦਿੱਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_new_size': "ਨਵਾਂ ਆਕਾਰ: {0:.2f} MB",
        'progress_cancelling': "ਰੱਦ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_cancel_message': "{0} ਰੱਦ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ",
        'progress_pages_found_moving': "{0} ਪੰਨੇ ਮਿਲੇ, {1} ਹਿਲਾਉਣ ਲਈ",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF ਦਾ ਵਿਸ਼ਲੇਸ਼ਣ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'ocr_status_optimizing': "ਚਿੱਤਰ ਅਨੁਕੂਲਤਾ ਚੱਲ ਰਹੀ ਹੈ...",
        'ocr_status_recognizing': "ਟੈਕਸਟ ਪਛਾਣ ਕਾਰਜ ਚੱਲ ਰਿਹਾ ਹੈ...",
        'ocr_status_embedding': "ਟੈਕਸਟ ਏਮਬੈਡ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...",
        'ocr_status_finalizing': "PDF ਨੂੰ ਅੰਤਿਮ ਰੂਪ ਦਿੱਤਾ ਜਾ ਰਿਹਾ ਹੈ...",

        # PDF-Laden
        'progress_preparing': "ਤਿਆਰੀ...",
        'progress_loading': "PDF ਲੋਡ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",

        # Seitenoperationen
        'progress_deleting_title': "ਪੰਨੇ ਮਿਟਾਏ ਜਾ ਰਹੇ ਹਨ...",
        'progress_moving_title': "ਪੰਨੇ ਹਿਲਾਏ ਜਾ ਰਹੇ ਹਨ...",
        'pages_found': "ਪੰਨੇ ਮਿਲੇ",
        'progress_creating_new_order': "ਨਵਾਂ ਕ੍ਰਮ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_sorting_pages': "ਪੰਨੇ ਕ੍ਰਮਬੱਧ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ...",
        'progress_moving_to_begin': "{0} ਪੰਨੇ ਸ਼ੁਰੂਆਤ ਵਿੱਚ ਹਿਲਾਏ ਜਾ ਰਹੇ ਹਨ",
        'progress_transferring_count': "{0} ਪੰਨੇ ਟ੍ਰਾਂਸਫਰ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ",
        'progress_transferring_before_target': "ਟੀਚੇ ਤੋਂ ਪਹਿਲਾਂ ਪੰਨੇ ਟ੍ਰਾਂਸਫਰ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ",
        'progress_moving_pages': "{0} ਪੰਨੇ ਹਿਲਾਏ ਜਾ ਰਹੇ ਹਨ",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_ਬੈਕਅੱਪ_",
        'filename_protected_suffix': "_ਸੁਰੱਖਿਅਤ_",
        'filename_copy_suffix': "_ਕਾਪੀ",
        'filename_page_single': "_ਪੰਨਾ_",
        'filename_page_range': "_ਪੰਨੇ_",
        'filename_export_page': "_ਪੰਨਾ_{0:03}",
        'filename_export_range': "_ਪੰਨੇ_{0}-{1}",
        'filename_export_multiple': "_ਪੰਨੇ_{0}",
        'filename_with_text': "_ਟੈਕਸਟ_ਸਮੇਤ",
        'filename_with_signature': "_ਦਸਤਖਤ_ਸਮੇਤ",
        'filename_with_image': "_ਚਿੱਤਰ_ਸਮੇਤ",
        'filename_with_forms': "_ਆਕਾਰਾਂ_ਸਮੇਤ",
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
        'view_toggle_navbar': "ਬਟਨ ਬਾਰ ਦਿਖਾਓ",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "ਸਾਰੇ ਪੰਨੇ ਮਿਟਾਏ ਨਹੀਂ ਜਾ ਸਕਦੇ",
		'pages_cannot_delete_last_page': 'ਆਖਰੀ ਪੰਨਾ ਮਿਟਾਇਆ ਨਹੀਂ ਜਾ ਸਕਦਾ!',
		'pages_cannot_delete_all_pages': 'ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਘੱਟੋ-ਘੱਟ ਇੱਕ ਪੰਨਾ ਰਹਿਣਾ ਚਾਹੀਦਾ ਹੈ!',
		'delete_pages_confirm': 'ਕੀ ਤੁਸੀਂ {0} ਪੰਨੇ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
		'delete_pages_confirm_voice': 'ਕੀ ਤੁਸੀਂ {0} ਪੰਨੇ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
		'pages_deleted': '{0} ਪੰਨੇ ਸਫਲਤਾਪੂਰਵਕ ਮਿਟਾ ਦਿੱਤੇ ਗਏ।',
		'warning': 'ਚੇਤਾਵਨੀ',
		'error': 'ਗਲਤੀ',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "ਕੋਈ ਫਾਰਮ ਚੁਣਿਆ ਨਹੀਂ ਗਿਆ",
        'form_customized': "ਫਾਰਮ ਅਨੁਕੂਲਿਤ ਕੀਤਾ ਗਿਆ",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "ਚੁਣੋ",
        'btn_use': "ਵਰਤੋ",
        'master_password_for_spasswords': "ਪਾਸਵਰਡ ਸਟੋਰ ਕਰਨ ਅਤੇ ਵਰਤਣ ਲਈ, ਪਹਿਲਾਂ ਇੱਕ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'open_saved_dialog_title': "ਸੇਵ ਕੀਤੀ ਫਾਈਲ ਖੋਲ੍ਹੋ",
        'open_saved_question': "ਕੀ ਤੁਸੀਂ ਸੇਵ ਕੀਤੀ ਫਾਈਲ ਹੁਣ ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'password': "ਪਾਸਵਰਡ",
        'password_manager_master_required': "ਪਾਸਵਰਡ ਮੈਨੇਜਰ ਸਿਰਫ ਉਦੋਂ ਉਪਲਬਧ ਹੁੰਦਾ ਹੈ ਜਦੋਂ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੋਵੇ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'password_master_required_for_select': "ਸੇਵ ਕੀਤੇ ਪਾਸਵਰਡ ਦੇਖਣ ਅਤੇ ਚੁਣਨ ਲਈ, ਤੁਹਾਨੂੰ ਪਹਿਲਾਂ ਆਪਣੇ ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣ ਪ੍ਰਮਾਣਿਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'password_not_available': "ਚੁਣਿਆ ਪਾਸਵਰਡ ਉਪਲਬਧ ਨਹੀਂ ਹੈ ਜਾਂ ਡੀਕ੍ਰਿਪਟ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਿਆ।",
        'password_options_title': "ਪਾਸਵਰਡ ਵਿਕਲਪ",
        'password_save_choice_change': "ਨਵਾਂ ਪਾਸਵਰਡ ਸੈੱਟ ਕਰੋ",
        'password_save_choice_keep': "ਮੌਜੂਦਾ ਪਾਸਵਰਡ ਵਰਤੋ",
        'password_save_choice_none': "ਬਿਨਾਂ ਏਨਕ੍ਰਿਪਸ਼ਨ ਦੇ ਸੇਵ ਕਰੋ",
        'password_save_hint': "ਪਾਸਵਰਡ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਸਟੋਰ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈੱਟ ਕਰੋ।",
        'password_save_master_required': "ਪਾਸਵਰਡ ਸੇਵ ਕਰੋ (ਕੇਵਲ ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ ਹੀ ਸੰਭਵ ਹੈ)",
        'password_save_question': "ਮੌਜੂਦਾ PDF ਪਾਸਵਰਡ ਨਾਲ ਸੁਰੱਖਿਅਤ ਹੈ। ਕੀ ਤੁਸੀਂ ਮੌਜੂਦਾ ਪਾਸਵਰਡ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਨਵਾਂ ਸੈੱਟ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਬਿਨਾਂ ਏਨਕ੍ਰਿਪਸ਼ਨ ਦੇ ਸੇਵ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'password_select': "ਪਾਸਵਰਡ ਚੁਣੋ",
        'password_select_none': "ਕੋਈ ਪਾਸਵਰਡ ਨਹੀਂ ਚੁਣਿਆ ਗਿਆ।\n\nਕਿਰਪਾ ਕਰਕੇ ਸੂਚੀ ਵਿੱਚੋਂ ਇੱਕ ਪਾਸਵਰਡ ਚੁਣੋ।",
        'password_select_one': "ਕਿਰਪਾ ਕਰਕੇ ਠੀਕ ਇੱਕ ਪਾਸਵਰਡ ਚੁਣੋ।\n\nਤੁਸੀਂ ਕਈ ਪਾਸਵਰਡ ਨਿਸ਼ਾਨਦੇਹ ਕੀਤੇ ਹਨ।",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_ਬੈਕਅੱਪ",
        'filename_insert_suffix': "_ਸੰਮਿਲਨ_ਨਾਲ",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_ਸਫ਼ੇ_ਮਿਟਾਏ",
        'filename_pages_moved': "_ਸਫ਼ੇ_ਖਿਸਕਾਏ",
        'filename_rotated_all_suffix': "_ਸਾਰੇ_ਸਫ਼ੇ_ਘੁੰਮਾਏ",
        'filename_rotated_suffix': "_ਸਫ਼ਾ_ਘੁਮਾਇਆ",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "PDF ਬਦਲਣ ਵੇਲੇ ਫਾਈਲ ਨਾਵਾਂ ਦੀ ਸੰਰਚਨਾ",
        'filename_keep_suffixes': "ਪਿਛਲੀਆਂ ਐਕਸਟੈਂਸ਼ਨਾਂ ਰੱਖੋ (ਜਿਵੇਂ _ਟੈਕਸਟ_ਨਾਲ)",
        'filename_keep_suffixes_false': "ਬਦਲੋ",
        'filename_keep_suffixes_true': "ਰੱਖੋ",
        'filename_preview_label': "ਫਾਈਲ ਨਾਮ ਦੀ ਪੂਰਵ ਝਲਕ:",
        'filename_preview_overwrite_hint': "ਪੂਰਵ ਝਲਕ ਉਪਲਬਧ ਨਹੀਂ – ਅਸਲੀ ਫਾਈਲ ਉੱਪਰ ਲਿਖੀ ਜਾਵੇਗੀ।",
        'filename_separator': "ਸ਼ਬਦਾਂ ਵਿਚਕਾਰ ਵੱਖਰਾ ਕਰਨ ਵਾਲਾ",
        'filename_separator_none': "ਕੋਈ ਵੱਖਰਾ ਕਰਨ ਵਾਲਾ ਨਹੀਂ",
        'filename_separator_space': "ਸਪੇਸ ( )",
        'filename_separator_underscore': "ਅੰਡਰਸਕੋਰ (_)",
        'filename_settings_saved': "ਫਾਈਲ ਨਾਮ ਸੈਟਿੰਗਾਂ ਸੇਵ ਹੋਈਆਂ",
        'filename_settings_title': "ਫਾਈਲ ਨਾਮ ਫਾਰਮੈਟਿੰਗ ਅਤੇ ਬੈਕਅੱਪ",
        'filename_timestamp_position': "ਟਾਈਮਸਟੈਂਪ ਦੀ ਸਥਿਤੀ",
        'filename_timestamp_position_after': "ਮੂਲ ਨਾਮ ਤੋਂ ਬਾਅਦ",
        'filename_timestamp_position_before': "ਬਿਲਕੁਲ ਅੱਗੇ",
        'filename_timestamp_position_end': "ਅੰਤ ਤੇ",
        'filename_use_timestamp': "ਟਾਈਮਸਟੈਂਪ ਵਰਤੋ",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>ਬਦਲਾਅ ਵੇਲੇ ਵਿਵਹਾਰ:</b><ul><li>ਸਫ਼ੇ ਮਿਟਾਉਣਾ ਅਤੇ ਸੰਮਿਲਿਤ ਕਰਨਾ</li><li>ਟੈਕਸਟ, ਦਸਤਖਤ, ਚਿੱਤਰ ਅਤੇ ਆਕਾਰ ਸੰਮਿਲਿਤ ਕਰਨਾ</li><li>OCR</li></ul></html>",
        'backup_section': "ਸਫ਼ਾ ਕਾਰਵਾਈਆਂ ਲਈ ਬੈਕਅੱਪ (ਮਿਟਾਓ, ਖਿਸਕਾਓ)",
        'behavior_info': "ਨੋਟ: 'ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖੋ' ਤੇ ਟਾਈਮਸਟੈਂਪ ਅਤੇ ਪਿਛੇਤਰਾਂ ਨੂੰ ਨਜ਼ਰਅੰਦਾਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ – ਫਾਈਲ ਆਪਣਾ ਨਾਮ ਰੱਖਦੀ ਹੈ।",
        'behavior_new_file': "ਹਮੇਸ਼ਾ ਨਵੀਂ ਫਾਈਲ ਬਣਾਓ (ਟਾਈਮਸਟੈਂਪ ਅਤੇ ਪਿਛੇਤਰ ਸਮੇਤ)",
        'behavior_overwrite': "ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖੋ (ਕੋਈ ਨਵੀਂ ਫਾਈਲ ਨਹੀਂ)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "ਸਾਰੇ ਸਫ਼ੇ ਘੁੰਮਾ ਦਿੱਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {0}",
        'all_pages_rotated_voice': "ਸਾਰੇ ਸਫ਼ੇ ਘੁੰਮਾਏ, ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ।",
        'empty_pages_deleted_new_file': "{0} ਖਾਲੀ ਸਫ਼ੇ ਮਿਟਾ ਦਿੱਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {1}",
        'empty_pages_deleted_voice': "{0} ਖਾਲੀ ਸਫ਼ੇ ਮਿਟਾਏ, ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ।",
        'ocr_keep_original': "ਅਸਲੀ ਰੱਖੋ (ਬਾਅਦ ਵਿੱਚ ਹੱਥੀਂ ਖੋਲ੍ਹੋ)",
        'ocr_new_file_question': "ਨਵੀਂ ਖੋਜਯੋਗ PDF ਇਸ ਥਾਂ ਤੇ ਸੇਵ ਕੀਤੀ ਗਈ:\n{0}\n\nਕੀ ਤੁਸੀਂ ਇਸਨੂੰ ਹੁਣ ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'ocr_open_new': "ਨਵੀਂ OCR ਫਾਈਲ ਖੋਲ੍ਹੋ",
        'ocr_original_kept': "ਅਸਲੀ ਫਾਈਲ ਖੁੱਲ੍ਹੀ ਰਹਿੰਦੀ ਹੈ। OCR ਫਾਈਲ ਸੇਵ ਹੋ ਗਈ ਹੈ।",
        'page_deleted_new_file': "ਸਫ਼ਾ {0} ਮਿਟਾ ਦਿੱਤਾ ਗਿਆ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {1}",
        'page_deleted_voice': "ਸਫ਼ਾ {0} ਮਿਟਾਇਆ, ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ।",
        'page_rotated_new_file': "ਸਫ਼ਾ {0} ਘੁਮਾ ਦਿੱਤਾ ਗਿਆ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {1}",
        'page_rotated_voice': "ਸਫ਼ਾ {0} ਘੁਮਾਇਆ, ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ।",
        'pages_deleted_new_file': "{0} ਸਫ਼ੇ ਮਿਟਾ ਦਿੱਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {1}",
        'pages_deleted_new_file_voice': "{0} ਸਫ਼ੇ ਮਿਟਾਏ, ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ।",
        'pages_inserted_new_file': "{0} ਸਫ਼ੇ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {1}",
        'pages_inserted_new_file_ask': "{0} ਸਫ਼ੇ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {1}\n\nਕੀ ਤੁਸੀਂ ਇਸਨੂੰ ਹੁਣ ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'pages_inserted_voice_new': "{0} ਸਫ਼ੇ ਸੰਮਿਲਿਤ ਕੀਤੇ, ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ।",
        'pages_moved_new_file': "{0} ਸਫ਼ੇ ਖਿਸਕਾ ਦਿੱਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਨਵੀਂ ਫਾਈਲ: {1}",
        'pages_moved_new_file_voice': "{0} ਸਫ਼ੇ ਖਿਸਕਾਏ, ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ।",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "ਦੁਬਾਰਾ ਨਾ ਦਿਖਾਓ",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 ਬੈਕਅੱਪ ਸੈਟਿੰਗ</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ ਬੈਕਅੱਪ ਚਾਲੂ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">ਸਾਰੀਆਂ ਤਬਦੀਲੀਆਂ ਤੇ ਜੋ ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖਦੀਆਂ ਹਨ</strong> (ਟੈਕਸਟ, ਦਸਤਖਤ, ਚਿੱਤਰ, ਆਕਾਰ, OCR, ਘੁਮਾਉਣਾ, ਸੰਮਿਲਿਤ ਕਰਨਾ, ਸਫ਼ੇ ਮਿਟਾਉਣਾ/ਖਿਸਕਾਉਣਾ) ਤਬਦੀਲੀ ਨੂੰ ਲਾਗੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ <strong>ਟਾਈਮਸਟੈਂਪ ਸਹਿਤ ਆਪਣੇ ਆਪ ਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ</strong>।</p>
                <p style="margin: 5px 0 5px 20px;">• ਬੈਕਅੱਪ ਅਸਲੀ ਫਾਈਲ ਦੇ ਨਾਲ ਲੱਗਦਾ ਹੁੰਦਾ ਹੈ (ਜਿਵੇਂ <code>ਦਸਤਾਵੇਜ਼_ਬੈਕਅੱਪ_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• ਜੇਕਰ ਤੁਸੀਂ ਵਾਧੂ ਤੌਰ ਤੇ <strong>„ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖੋ“</strong> ਵਿਕਲਪ ਸਰਗਰਮ ਕੀਤਾ ਹੈ, ਤਾਂ ਵੀ ਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ।</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 ਬੈਕਅੱਪ ਬੰਦ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>ਕੋਈ ਬੈਕਅੱਪ ਨਹੀਂ ਬਣਾਇਆ ਜਾਂਦਾ</strong> – ਨਾ ਉੱਪਰ ਲਿਖਦੇ ਸਮੇਂ, ਨਾ ਸਫ਼ਾ ਕਾਰਵਾਈਆਂ ਦੌਰਾਨ।</p>
                <p style="margin: 5px 0 5px 20px;">• ਉੱਪਰ ਲਿਖਣ ਤੇ ਅਸਲੀ ਫਾਈਲ ਅਟੱਲ ਤੌਰ ਤੇ ਖਤਮ ਹੋ ਸਕਦੀ ਹੈ।</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">ਸਿਰਫ ਤਜਰਬੇਕਾਰ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ਟਿਪ:</strong> ਬੈਕਅੱਪ ਸੈਟਿੰਗ „ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖੋ“ ਵਿਕਲਪ ਤੋਂ ਸੁਤੰਤਰ ਹੈ। ਤੁਸੀਂ ਦੋਵੇਂ ਜੋੜ ਸਕਦੇ ਹੋ।<br>
                ਤੁਸੀਂ ਇਸ ਸੁਨੇਹੇ ਨੂੰ ਸਥਾਈ ਤੌਰ ਤੇ ਲੁਕਾ ਸਕਦੇ ਹੋ।
            </div>
        </div>
        """,
        'backup_info_title': "ਬੈਕਅੱਪ ਵਿਵਹਾਰ",
        'backup_info_voice': "ਸਫ਼ਾ ਕਾਰਵਾਈਆਂ ਤੇ ਬੈਕਅੱਪ ਵਿਵਹਾਰ ਬਾਰੇ ਸੂਚਨਾ। ਬੈਕਅੱਪ ਚਾਲੂ ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖਦਾ ਹੈ, ਬੈਕਅੱਪ ਬੰਦ ਨਵੀਂ ਫਾਈਲ ਬਣਾਉਂਦਾ ਹੈ।",
        'show_backup_info': "ਬੈਕਅੱਪ ਸੈਟਿੰਗ ਬਾਰੇ ਜਾਣਕਾਰੀ",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "ਦੁਬਾਰਾ ਨਾ ਦਿਖਾਓ",
        'overwrite_enable_backup': "ਬੈਕਅੱਪ ਸਰਗਰਮ ਕਰੋ (ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖੋ</p>
            <p>ਜੇਕਰ ਤੁਸੀਂ ਇਸ ਵਿਕਲਪ ਨੂੰ ਸਰਗਰਮ ਕਰਦੇ ਹੋ, ਤਾਂ ਤਬਦੀਲੀਆਂ (ਟੈਕਸਟ, ਦਸਤਖਤ, ਚਿੱਤਰ, ਆਕਾਰ, OCR, ਘੁਮਾਉਣਾ, ਸੰਮਿਲਿਤ ਕਰਨਾ) <strong>ਸਿੱਧੇ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਹੁੰਦੀਆਂ ਹਨ</strong> – <strong>ਕੋਈ ਨਵੀਂ ਫਾਈਲ ਨਹੀਂ ਬਣਾਈ ਜਾਂਦੀ</strong>।</p>
            <p>• ਫਾਈਲ ਦਾ ਨਾਮ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹਿੰਦਾ ਹੈ।<br>
            • ਟਾਈਮਸਟੈਂਪ ਅਤੇ ਪਿਛੇਤਰਾਂ ਨੂੰ ਨਜ਼ਰਅੰਦਾਜ਼ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।<br>
            • <strong>ਬੈਕਅੱਪ ਤੋਂ ਬਿਨਾਂ, ਅਸਲੀ ਫਾਈਲ ਅਟੱਲ ਤੌਰ ਤੇ ਖਤਮ ਹੋ ਸਕਦੀ ਹੈ।</strong></p>
            <p style="color: #FFD700;">ਸਿਫਾਰਸ਼: ਆਟੋਮੈਟਿਕ ਬੈਕਅੱਪ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਵਾਧੂ ਤੌਰ ਤੇ ਬੈਕਅੱਪ ਵਿਕਲਪ ਨੂੰ ਸਰਗਰਮ ਕਰੋ।</p>
        </div>
        """,
        'overwrite_info_title': "ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖੋ",
        'overwrite_info_voice': "ਚੇਤਾਵਨੀ: ਅਸਲੀ ਨੂੰ ਉੱਪਰ ਲਿਖੋ – ਕੋਈ ਨਵੀਂ ਫਾਈਲ ਨਹੀਂ। ਬੈਕਅੱਪ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} ਸਫ਼ੇ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਉੱਪਰ ਲਿਖੀ ਗਈ ਸੀ।\nਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'pages_inserted_overwrite_no_backup': "{0} ਸਫ਼ੇ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਹਨ।\n\nਅਸਲੀ ਫਾਈਲ ਉੱਪਰ ਲਿਖੀ ਗਈ ਸੀ।\nਕੋਈ ਬੈਕਅੱਪ ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'texts_saved_overwrite_with_backup': "ਤਬਦੀਲੀਆਂ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਹੋ ਗਈਆਂ।\n\nਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'texts_saved_overwrite_no_backup': "ਤਬਦੀਲੀਆਂ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਹੋ ਗਈਆਂ।\n\nਕੋਈ ਬੈਕਅੱਪ ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'texts_crosses_saved_new_file': "{0} {1} ਅਤੇ {2} {3} ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਸਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ ਸੀ।\n\nਨਵੀਂ PDF ਲੋਡ ਹੋ ਰਹੀ ਹੈ...",
        'texts_saved_new_file': "{0} {1} ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਸਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ ਸੀ।\n\nਨਵੀਂ PDF ਲੋਡ ਹੋ ਰਹੀ ਹੈ...",
        'crosses_saved_new_file': "{0} {1} ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਸਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ ਸੀ।\n\nਨਵੀਂ PDF ਲੋਡ ਹੋ ਰਹੀ ਹੈ...",
        'elements_saved_new_file': "{0} ਤੱਤ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਸਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ ਸੀ।\n\nਨਵੀਂ PDF ਲੋਡ ਹੋ ਰਹੀ ਹੈ...",
        'signatures_saved_overwrite_with_backup': "ਦਸਤਖਤ(ਆਂ) ਨੂੰ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕੀਤਾ ਗਿਆ ਸੀ।\n\nਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'signatures_saved_overwrite_no_backup': "ਦਸਤਖਤ(ਆਂ) ਨੂੰ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕੀਤਾ ਗਿਆ ਸੀ।\n\nਕੋਈ ਬੈਕਅੱਪ ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'images_saved_overwrite_with_backup': "ਚਿੱਤਰ(ਆਂ) ਨੂੰ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕੀਤਾ ਗਿਆ ਸੀ।\n\nਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'images_saved_overwrite_no_backup': "ਚਿੱਤਰ(ਆਂ) ਨੂੰ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕੀਤਾ ਗਿਆ ਸੀ।\n\nਕੋਈ ਬੈਕਅੱਪ ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'forms_saved_overwrite_with_backup': "ਆਕਾਰ(ਆਂ) ਨੂੰ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕੀਤਾ ਗਿਆ ਸੀ।\n\nਇੱਕ ਬੈਕਅੱਪ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'forms_saved_overwrite_no_backup': "ਆਕਾਰ(ਆਂ) ਨੂੰ ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕੀਤਾ ਗਿਆ ਸੀ।\n\nਕੋਈ ਬੈਕਅੱਪ ਨਹੀਂ ਬਣਾਇਆ ਗਿਆ ਸੀ।",
        'signatures_saved_new_file': "{0} ਦਸਤਖਤ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਸਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ ਸੀ।\n\nਨਵੀਂ PDF ਲੋਡ ਹੋ ਰਹੀ ਹੈ...",
        'images_saved_new_file': "{0} ਚਿੱਤਰ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਸਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ ਸੀ।\n\nਨਵੀਂ PDF ਲੋਡ ਹੋ ਰਹੀ ਹੈ...",
        'forms_saved_new_file': "{0} ਆਕਾਰ ਸੰਮਿਲਿਤ ਕੀਤੇ ਗਏ ਸਨ।\n\nਅਸਲੀ ਫਾਈਲ ਬਿਨਾਂ ਬਦਲਾਅ ਦੇ ਰਹੀ।\nਇੱਕ ਨਵੀਂ ਫਾਈਲ ਬਣਾਈ ਗਈ ਸੀ।\n\nਨਵੀਂ PDF ਲੋਡ ਹੋ ਰਹੀ ਹੈ...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "ਚੇਤਾਵਨੀ: ਇਸ PDF ਵਿੱਚ ਘੁੰਮਾਏ ਹੋਏ ਸਫ਼ੇ ਹਨ। ਸਥਿਤੀ ਵੱਖਰੀ ਹੋ ਸਕਦੀ ਹੈ।",
        'page_rotated_warning_title': "ਘੁੰਮਾਇਆ ਸਫ਼ਾ ਖੋਜਿਆ ਗਿਆ",
        'page_rotated_warning_message': "ਮੌਜੂਦਾ ਸਫ਼ਾ {0} {1}° ਘੁੰਮਾਇਆ ਗਿਆ ਹੈ।\n\nਘੁੰਮਾਏ ਹੋਏ ਸਫ਼ਿਆਂ ਤੇ ਤੱਤ ਸੰਮਿਲਿਤ ਕਰਨਾ ਸਮਰਥਿਤ ਨਹੀਂ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣ ਸਫ਼ੇ ਨੂੰ ਸਿੱਧੀ ਸਥਿਤੀ ਵਿੱਚ ਘੁਮਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'page_rotated_warning_voice': "ਚੇਤਾਵਨੀ: ਸਫ਼ਾ ਘੁੰਮਾਇਆ ਗਿਆ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਇਸਨੂੰ ਘੁਮਾਓ।",
        'paste_on_rotated_page_simple_warning': "ਸਫ਼ੇ {0} ਤੇ ਸੰਮਿਲਿਤ ਕਰਨਾ ਸੰਭਵ ਨਹੀਂ!\n\nਇਹ ਸਫ਼ਾ {1}° ਘੁੰਮਾਇਆ ਗਿਆ ਹੈ।\n\nਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਸਫ਼ੇ ਨੂੰ 0° ਤੇ ਘੁਮਾਓ (ਮੇਨੂ: ਸੰਪਾਦਨ ਕਰੋ → ਸਫ਼ਾ ਅਲਾਈਨ ਕਰੋ)।\n\nਚੇਤਾਵਨੀ:\nਪਹਿਲਾਂ ਕਾਪੀ ਕੀਤਾ ਤੱਤ ਖਤਮ ਹੋ ਜਾਵੇਗਾ ਜੇਕਰ ਤੁਸੀਂ ਸਫ਼ਾ ਘੁਮਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਸੇਵ ਨਹੀਂ ਕਰਦੇ।",
        'paste_on_rotated_page_voice': "ਸੰਮਿਲਨ ਰੱਦ ਕੀਤਾ ਗਿਆ। ਸਫ਼ਾ ਘੁੰਮਾਇਆ ਗਿਆ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਸਫ਼ਾ ਅਲਾਈਨ ਕਰੋ।",
        'page_rotated_cancel': "ਰੱਦ ਕਰੋ",
        'page_rotated_rotate_until_upright': "ਸਫ਼ੇ ਨੂੰ ਵਾਰ-ਵਾਰ ਘੁਮਾਓ (ਸਿੱਧਾ ਹੋਣ ਤੱਕ)",
        'page_rotated_now_upright': "ਸਫ਼ਾ ਹੁਣ ਸਿੱਧਾ ਹੈ। ਤੁਸੀਂ ਹੁਣ ਸੰਮਿਲਿਤ ਕਰ ਸਕਦੇ ਹੋ।",
        'page_rotated_still_not_upright': "ਸਫ਼ੇ ਨੂੰ ਸਿੱਧੀ ਸਥਿਤੀ ਵਿੱਚ ਨਹੀਂ ਘੁਮਾਇਆ ਜਾ ਸਕਿਆ। ਕਿਰਪਾ ਕਰਕੇ ਹੱਥੀਂ ਸੁਧਾਰੋ।",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "ਮਦਦ: ਘੁੰਮਾਏ ਹੋਏ ਸਫ਼ੇ ਸੁਧਾਰੋ",
        'help_rotated_pages_voice': "ਘੁੰਮਾਏ ਹੋਏ ਸਫ਼ੇ ਸੁਧਾਰਨ ਲਈ ਮਦਦ ਖੁੱਲ੍ਹ ਰਹੀ ਹੈ।",
        'btn_help': "ਮਦਦ",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 ਸਮੱਸਿਆ: ਘੁੰਮਾਇਆ ਸਫ਼ਾ – ਸੰਮਿਲਿਤ ਕਰਨਾ ਸਹੀ ਢੰਗ ਨਾਲ ਕੰਮ ਨਹੀਂ ਕਰਦਾ</p>

            <p>ਜੇਕਰ ਘੁੰਮਾਏ ਸਫ਼ੇ ਤੇ ਟੈਕਸਟ, ਦਸਤਖਤ ਜਾਂ ਆਕਾਰ ਸੰਮਿਲਿਤ ਕਰਨਾ ਸਹੀ ਢੰਗ ਨਾਲ ਕੰਮ ਨਹੀਂ ਕਰਦਾ, ਤਾਂ ਤੁਸੀਂ ਬਾਹਰੀ PDF ਸੰਪਾਦਕ ਨਾਲ ਸਫ਼ਾ ਸੁਧਾਰ ਸਕਦੇ ਹੋ।</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ ਬਾਹਰੀ ਸਾਧਨ ਨਾਲ ਹੱਲ (ਜਿਵੇਂ macOS ਪੂਰਵਦਰਸ਼ਨ)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>ਸਫ਼ਾ ਐਕਸਪੋਰਟ ਕਰੋ</strong><br>
                &nbsp;&nbsp;ਮੇਨੂ ਵਿੱਚ <strong>ਫਾਈਲ → ਸਫ਼ਿਆਂ ਵਜੋਂ ਐਕਸਪੋਰਟ ਕਰੋ</strong> ਤੇ ਕਲਿੱਕ ਕਰੋ ਜਾਂ ਕਿਸੇ ਹੋਰ ਢੰਗ ਨਾਲ ਲੋੜੀਂਦੇ ਸਫ਼ੇ ਨੂੰ ਇੱਕਲੇ PDF ਵਜੋਂ ਸੇਵ ਕਰੋ।</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>ਬਾਹਰੀ ਪ੍ਰੋਗਰਾਮ ਵਿੱਚ ਸਫ਼ਾ ਖੋਲ੍ਹੋ</strong><br>
                &nbsp;&nbsp;ਐਕਸਪੋਰਟ ਕੀਤੇ PDF ਨੂੰ PDF ਸੰਪਾਦਕ ਵਿੱਚ ਖੋਲ੍ਹੋ (ਜਿਵੇਂ <strong>macOS ਪੂਰਵਦਰਸ਼ਨ</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>ਸਫ਼ਾ ਘੁਮਾਓ</strong><br>
                &nbsp;&nbsp;ਸਫ਼ੇ ਨੂੰ ਘੁਮਾਓ ਤਾਂ ਜੋ ਉਹ ਸਿੱਧਾ ਹੋ ਜਾਵੇ (ਪੂਰਵਦਰਸ਼ਨ ਵਿੱਚ: <strong>ਸੰਦ → ਘੁਮਾਓ</strong> ਜਾਂ <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>ਸੇਵ ਕਰੋ</strong><br>
                &nbsp;&nbsp;ਸੁਧਾਰੇ ਸਫ਼ੇ ਨੂੰ ਸੇਵ ਕਰੋ (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>ਸਫ਼ੇ ਨੂੰ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਮੁੜ ਸੰਮਿਲਿਤ ਕਰੋ</strong><br>
                &nbsp;&nbsp;PDFDarkView ਤੇ ਵਾਪਸ ਜਾਓ ਅਤੇ ਸੁਧਾਰੇ ਸਫ਼ੇ ਨੂੰ ਲੋੜੀਂਦੀ ਸਥਿਤੀ ਤੇ ਸੰਮਿਲਿਤ ਕਰੋ:<br>
                &nbsp;&nbsp;<strong>ਸੰਪਾਦਨ ਕਰੋ → ਸਫ਼ੇ ਸੰਮਿਲਿਤ ਕਰੋ</strong>।</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 ਵਿਕਲਪ: ਅਸਲੀ ਫਾਈਲ ਵਿੱਚ ਸਫ਼ਾ ਘੁਮਾਓ</p>
                <p style="margin: 5px 0 5px 20px;">• ਬਿਲਟ-ਇਨ ਘੁਮਾਉਣ ਫੰਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰੋ (<strong>ਸੰਪਾਦਨ ਕਰੋ → ਸਫ਼ਾ ਘੁਮਾਓ</strong>) ਸਫ਼ੇ ਨੂੰ ਕਦਮ-ਦਰ-ਕਦਮ ਸੁਧਾਰਨ ਲਈ।<br>
                • ਹਰੇਕ ਘੁਮਾਉਣ ਤੋਂ ਬਾਅਦ ਤੁਸੀਂ ਜਾਂਚ ਕਰ ਸਕਦੇ ਹੋ ਕਿ ਸੰਮਿਲਿਤ ਕਰਨਾ ਹੁਣ ਕੰਮ ਕਰਦਾ ਹੈ ਜਾਂ ਨਹੀਂ।<br>
                • ਇਹ ਅਕਸਰ ਤੇਜ਼ ਹੱਲ ਹੁੰਦਾ ਹੈ – ਪਹਿਲਾਂ ਇਸਨੂੰ ਅਜ਼ਮਾਓ!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ਟਿਪ:</strong> ਜੇਕਰ ਤੁਸੀਂ ਅਕਸਰ ਘੁੰਮਾਏ ਸਫ਼ਿਆਂ ਦਾ ਸਾਹਮਣਾ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਸੰਮਿਲਨ ਡਾਇਲਾਗ ਵਿੱਚ ਚੇਤਾਵਨੀ ਨੂੰ ਸਥਾਈ ਤੌਰ ਤੇ ਲੁਕਾ ਸਕਦੇ ਹੋ।<br>
                ਸਥਿਤੀ ਫਿਰ ਵੱਖਰੀ ਹੋ ਸਕਦੀ ਹੈ – ਇਸ ਵਿਕਲਪ ਦੀ ਵਰਤੋਂ ਸਿਰਫ ਉਦੋਂ ਕਰੋ ਜੇਕਰ ਤੁਸੀਂ ਨਤੀਜਿਆਂ ਨੂੰ ਜਾਣਦੇ ਹੋ।
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "ਸਫ਼ੇ ਅਲਾਈਨ ਕਰੋ",
        'menu_rotate_normalize_tooltip': "ਸਫ਼ਾ ਘੁਮਾਓ ਜਾਂ 0° ਤੇ ਰੀਸੈਟ ਕਰੋ",
        'normalize_current_page': "ਮੌਜੂਦਾ ਸਫ਼ੇ ਨੂੰ ਸਿੱਧੀ ਸਥਿਤੀ ਵਿੱਚ ਲਿਆਓ (0° ਤੇ ਸੈੱਟ ਕਰੋ)",
        'normalize_all_pages': "ਸਾਰੇ ਸਫ਼ਿਆਂ ਨੂੰ ਸਿੱਧੀ ਸਥਿਤੀ ਵਿੱਚ ਲਿਆਓ (0° ਤੇ ਸੈੱਟ ਕਰੋ)",
        'page_normalized': "ਸਫ਼ਾ {0} ਸਿੱਧੀ ਸਥਿਤੀ ਵਿੱਚ ਸੈੱਟ ਕੀਤਾ ਗਿਆ।",
        'all_pages_normalized': "ਸਾਰੇ ਸਫ਼ੇ ਸਿੱਧੀ ਸਥਿਤੀ ਵਿੱਚ ਸੈੱਟ ਕੀਤੇ ਗਏ।",
        'page_already_upright': "ਸਫ਼ਾ {0} ਪਹਿਲਾਂ ਹੀ ਸਿੱਧਾ ਹੈ।",
        'all_pages_already_upright': "ਸਾਰੇ ਸਫ਼ੇ ਪਹਿਲਾਂ ਹੀ ਸਿੱਧੇ ਹਨ।",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF ਵਿੱਚ ਕੋਈ ਖੋਜਯੋਗ ਟੈਕਸਟ ਨਹੀਂ ਹੈ।</p><p>ਕੀ ਤੁਸੀਂ {0} ਵਿੱਚ ਐਕਸਪੋਰਟ ਕਰਨ ਲਈ OCR ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?</p>",
        'export_ocr_voice': "PDF ਵਿੱਚ ਕੋਈ ਟੈਕਸਟ ਨਹੀਂ ਹੈ। {0} ਵਿੱਚ ਐਕਸਪੋਰਟ ਕਰਨ ਲਈ OCR ਦੀ ਲੋੜ ਹੈ।",
        'export_no_ocr_possible': "OCR ਤੋਂ ਬਿਨਾਂ ਐਕਸਪੋਰਟ ਸੰਭਵ ਨਹੀਂ। ਕਿਰਪਾ ਕਰਕੇ ਮੇਨੂ ਰਾਹੀਂ OCR ਕਰੋ।",
        'ocr_failed_export_not_possible': "OCR ਅਸਫਲ ਰਿਹਾ। ਐਕਸਪੋਰਟ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ।",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF ਪੂਰਵਦਰਸ਼ਨ ਵਿੱਚ ਖੁੱਲ੍ਹੇਗਾ। ਕਿਰਪਾ ਕਰਕੇ ਉੱਥੇ ਪ੍ਰਿੰਟਿੰਗ ਪ੍ਰਕਿਰਿਆ ਸ਼ੁਰੂ ਕਰੋ।",
        'print_preview_manual': "PDF ਖੋਲ੍ਹਿਆ ਗਿਆ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਪ੍ਰਿੰਟ ਕਮਾਂਡ ਹੱਥੀਂ ਚਲਾਓ (ਜਿਵੇਂ Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDF ਨੂੰ ਮਰਜ ਕਰੋ",
        'merge_pdfs': "PDF ਨੂੰ ਮਰਜ ਕਰੋ",
        'merge_progress_title': "PDF ਮਰਜ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ...",
        'merge_pdfs_list': "ਕ੍ਰਮ ਵਿੱਚ PDF (ਖਿੱਚੋ ਅਤੇ ਸੁੱਟੋ ਕ੍ਰਮਬੱਧ ਕਰਨ ਲਈ)",
        'merge_add_pdf': "PDF ਸ਼ਾਮਲ ਕਰੋ",
        'merge_remove': "ਹਟਾਓ",
        'merge_move_up': "ਉੱਪਰ",
        'merge_move_down': "ਹੇਠਾਂ",
        'merge_pdfs_info': "💡 ਟਿਪ: ਤੁਸੀਂ ਖਿੱਚ ਕੇ ਸੁੱਟ ਕੇ ਕ੍ਰਮ ਬਦਲ ਸਕਦੇ ਹੋ",
        'merge_no_pdfs': "ਕੋਈ PDF ਨਹੀਂ ਚੁਣਿਆ ਗਿਆ। 'PDF ਸ਼ਾਮਲ ਕਰੋ' ਤੇ ਕਲਿੱਕ ਕਰੋ।",
        'merge_info': "{0} PDF ਚੁਣੇ ਗਏ (ਲਗਭਗ {1} ਸਫ਼ੇ)",
        'merge_open_file': "ਫਾਈਲ ਖੋਲ੍ਹੋ",
        'merge_merge': "ਮਰਜ ਕਰੋ",
        'merge_error': "ਮਰਜ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ",
        'merge_min_two_pdfs_error': "ਕਿਰਪਾ ਕਰਕੇ ਮਰਜ ਕਰਨ ਲਈ ਘੱਟੋ-ਘੱਟ ਦੋ PDF ਫਾਈਲਾਂ ਚੁਣੋ।",
        'merge_select_pdfs': "ਮਰਜ ਕਰਨ ਲਈ PDF ਚੁਣੋ",
        'merge_error_file': "ਪ੍ਰੋਸੈਸਿੰਗ ਦੌਰਾਨ ਗਲਤੀ",
        'merge_cancelled': "ਮਰਜ ਰੱਦ ਕਰ ਦਿੱਤਾ ਗਿਆ",
        'merge_preparing': "ਤਿਆਰੀ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'merge_processing': "{1} ਵਿੱਚੋਂ PDF {0} ਪ੍ਰੋਸੈਸ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ",
        'merge_saving': "ਮਰਜ ਕੀਤੀ PDF ਸੇਵ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...",
        'merge_complete': "ਮੁਕੰਮਲ!",
        'merge_success_title': "ਮਰਜ ਸਫਲ ਰਿਹਾ",
        'merge_success_voice': "{0} PDF ਸਫਲਤਾਪੂਰਵਕ ਮਰਜ ਕੀਤੇ ਗਏ।",
        'merge_success_message': "{0} PDF ਸਫਲਤਾਪੂਰਵਕ ਮਰਜ ਕੀਤੇ ਗਏ।\n\nਨਵੇਂ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਹੁਣ {1} ਸਫ਼ੇ ਹਨ।\n\nਨਵੀਂ ਫਾਈਲ:\n{2}\n\nਸੇਵ ਸਥਾਨ:\n{3}\n{2}\n\nਕੀ ਤੁਸੀਂ ਇਹ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'replace_file_title': "ਫਾਈਲ ਬਦਲਣੀ ਹੈ?",
        'replace_file_message': "ਪਹਿਲਾਂ ਹੀ ਇੱਕ PDF ਖੁੱਲ੍ਹੀ ਹੈ। ਕੀ ਤੁਸੀਂ ਇਸਨੂੰ ਨਵੀਂ ਫਾਈਲ ਨਾਲ ਬਦਲਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        'btn_yes': "ਹਾਂ",
        'btn_no': "ਨਹੀਂ",
        'filename_merge_suffix': "ਮਰਜ ਕੀਤਾ",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "{0} ਖੋਲ੍ਹਿਆ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_merge_reading': "{0} ਪੜ੍ਹਿਆ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_merge_adding': "{0} ਸਫ਼ੇ ਸ਼ਾਮਲ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ...",
        'progress_merge_optimizing': "PDF ਨੂੰ ਅਨੁਕੂਲ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ...",
        'progress_merge_writing': "PDF ਲਿਖੀ ਜਾ ਰਹੀ ਹੈ...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF ਨੂੰ ਬੰਦ ਕਰਨਾ",
        'action_close_window': "ਵਿੰਡੋ ਨੂੰ ਬੰਦ ਕਰਨਾ",
        'action_open_new_pdf': "ਇੱਕ ਨਵੀਂ PDF ਖੋਲ੍ਹਣਾ",
        'action_quit_app': "ਐਪਲੀਕੇਸ਼ਨ ਤੋਂ ਬਾਹਰ ਨਿਕਲਣਾ",
        'changes_saved': "ਤਬਦੀਲੀਆਂ ਸੇਵ ਹੋ ਗਈਆਂ।",
        'file_close_title': "PDF ਫਾਈਲ ਬੰਦ ਕਰੋ",
        'save_before_action': "ਕੀ {0} ਤੋਂ ਪਹਿਲਾਂ ਤਬਦੀਲੀਆਂ ਸੇਵ ਕੀਤੀਆਂ ਜਾਣ? ਹਾਂ ਜਾਂ ਨਹੀਂ?",
        'save_before_action_voice': "ਕੀ {0} ਤੋਂ ਪਹਿਲਾਂ ਤਬਦੀਲੀਆਂ ਸੇਵ ਕੀਤੀਆਂ ਜਾਣ? ਹਾਂ ਜਾਂ ਨਹੀਂ?",
        'save_before_close_question': "ਕੀ ਬੰਦ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਤਬਦੀਲੀਆਂ ਸੇਵ ਕੀਤੀਆਂ ਜਾਣ? ਹਾਂ ਜਾਂ ਨਹੀਂ?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>ਖੋਜਯੋਗ PDF ਬਣਾਇਆ ਗਿਆ:\n\n{0}\n\n<b>ਜੇ ਲੋੜ ਹੋਵੇ ਤਾਂ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ",
        "ocr_rotate_title": "OCR ਤੋਂ ਪਹਿਲਾਂ ਪੰਨਿਆਂ ਨੂੰ ਇਕਸਾਰ ਕਰੋ",
        "ocr_rotate_question": "PDF ਵਿੱਚ ਘੁੰਮਾਏ ਹੋਏ ਪੰਨੇ ਹਨ।\nਕੀ ਤੁਸੀਂ OCR ਤੋਂ ਪਹਿਲਾਂ ਸਾਰੇ ਪੰਨਿਆਂ ਨੂੰ 0° ਤੇ ਇਕਸਾਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?\nਇਸ ਨਾਲ ਟੈਕਸਟ ਪਛਾਣ ਵਿੱਚ ਮਹੱਤਵਪੂਰਨ ਸੁਧਾਰ ਹੁੰਦਾ ਹੈ।",
        "ocr_rotate_yes": "ਹਾਂ, ਇਕਸਾਰ ਕਰੋ",
        "ocr_rotate_no": "ਨਹੀਂ, ਸਿੱਧਾ OCR ਸ਼ੁਰੂ ਕਰੋ",
        "ocr_rotate_voice": "PDF ਵਿੱਚ ਘੁੰਮਾਏ ਹੋਏ ਪੰਨੇ ਹਨ। ਕੀ OCR ਤੋਂ ਪਹਿਲਾਂ ਸਾਰੇ ਪੰਨੇ ਇਕਸਾਰ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ?",
        "ocr_not_performed_message": "ਕੋਈ ਟੈਕਸਟ ਮੌਜੂਦ ਨਹੀਂ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ OCR ਕਰੋ (ਮੇਨੂ \"ਸੰਪਾਦਿਤ ਕਰੋ\" → \"OCR ਕਰੋ\" ਜਾਂ Ctrl+R ਕੁੰਜੀ)।",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR ਸੈਟਿੰਗਾਂ",
        "ocr_language_btn": "OCR ਭਾਸ਼ਾ ਚੁਣੋ",
        "ocr_language": "OCR ਭਾਸ਼ਾ(ਵਾਂ)",
        "ocr_language_current": "ਮੌਜੂਦਾ ਭਾਸ਼ਾ:",
        "ocr_param_info": "ਪੈਰਾਮੀਟਰ ਬਾਰੇ ਜਾਣਕਾਰੀ",

        "ocr_force_ocr_label": "OCR ਲਾਗੂ ਕਰੋ",
        "ocr_deskew_label": "ਟੇਢਾਪਨ ਠੀਕ ਕਰੋ",
        "ocr_clean_label": "ਚਿੱਤਰ ਸਾਫ਼ ਕਰੋ",
        "ocr_oversample_label": "ਰੈਜ਼ੋਲਿਊਸ਼ਨ (DPI)",
        "ocr_pagesegmode_label": "ਪੰਨਾ ਵੰਡ",
        "ocr_oem_label": "OCR ਇੰਜਣ ਮੋਡ",
        "ocr_optimize_label": "PDF ਸੰਕੁਚਨ",
        "ocr_jobs_label": "ਸਮਾਨਾਂਤਰ ਪ੍ਰਕਿਰਿਆਵਾਂ",
        "ocr_verbose_label": "ਲੌਗ ਵੇਰਵਾ",

        "ocr_force_ocr_tooltip": "ਹਰ ਪੰਨੇ ਤੇ OCR ਲਾਗੂ ਕਰੋ, ਭਾਵੇਂ ਟੈਕਸਟ ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਹੋਵੇ",
        "ocr_deskew_tooltip": "ਟੇਢੇ ਸਕੈਨਾਂ ਨੂੰ ਆਪਣੇ ਆਪ ਇਕਸਾਰ ਕਰੋ",
        "ocr_clean_tooltip": "ਚਿੱਤਰ ਤੋਂ ਰੌਲਾ ਅਤੇ ਨਕਲੀ ਚੀਜ਼ਾਂ ਹਟਾਓ",
        "ocr_oversample_tooltip": "OCR ਤੋਂ ਪਹਿਲਾਂ ਚਿੱਤਰ ਨੂੰ ਇਸ DPI ਤੱਕ ਵੱਡਾ ਕਰੋ",
        "ocr_pagesegmode_tooltip": "ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਪੰਨੇ ਨੂੰ ਟੈਕਸਟ ਖੇਤਰਾਂ ਵਿੱਚ ਕਿਵੇਂ ਵੰਡਿਆ ਜਾਵੇ",
        "ocr_oem_tooltip": "Tesseract ਦਾ OCR ਇੰਜਣ ਚੁਣਦਾ ਹੈ",
        "ocr_optimize_tooltip": "ਆਉਟਪੁਟ PDF ਦਾ ਸੰਕੁਚਨ ਪੱਧਰ",
        "ocr_jobs_tooltip": "ਸਮਾਨਾਂਤਰ OCR ਪ੍ਰਕਿਰਿਆਵਾਂ ਦੀ ਗਿਣਤੀ",
        "ocr_verbose_tooltip": "ਲੌਗ ਆਉਟਪੁਟ ਦਾ ਵੇਰਵਾ ਪੱਧਰ",
        "ocr_settings_explain_btn": "ਵਿਆਖਿਆ",

        "ocr_force_ocr_explain": "<b>ਹਰ</b> ਪੰਨੇ ਤੇ ਟੈਕਸਟ ਪਛਾਣ ਨੂੰ ਲਾਗੂ ਕਰਦਾ ਹੈ (ਭਾਵੇਂ ਇਸ ਵਿੱਚ ਪਹਿਲਾਂ ਤੋਂ ਟੈਕਸਟ ਹੋਵੇ)।\n\nਸਿਫਾਰਸ: ਸਕੈਨ ਕੀਤੇ PDF ਲਈ <b>ਚਾਲੂ</b>, ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਟੈਕਸਟ ਵਾਲੇ ਮੂਲ PDF ਲਈ <b>ਬੰਦ</b>।",

        "ocr_deskew_explain": "ਥੋੜ੍ਹੇ ਟੇਢੇ ਸਕੈਨਾਂ ਨੂੰ ਠੀਕ ਕਰਦਾ ਹੈ (ਲਗਭਗ 5° ਤੱਕ)।\n\nਸਿਫਾਰਸ: ਸਕੈਨ ਕੀਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਲਈ <b>ਚਾਲੂ</b>, ਜੇ ਪੰਨੇ ਪਹਿਲਾਂ ਤੋਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਸਿੱਧੇ ਹਨ ਤਾਂ <b>ਬੰਦ</b>।",

        "ocr_clean_explain": "ਚਿੱਤਰ ਤੋਂ ਰੌਲਾ, ਬਿੰਦੀਆਂ ਅਤੇ ਛੋਟੀਆਂ ਨਕਲੀ ਚੀਜ਼ਾਂ ਨੂੰ ਹਟਾਉਂਦਾ ਹੈ।\n<b>ਮਹੱਤਵਪੂਰਨ:</b> ਅਰਬੀ, ਥਾਈ ਜਾਂ ਵੀਅਤਨਾਮੀ ਟੈਕਸਟਾਂ ਲਈ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਵਿਸ਼ੇਸਕ ਚਿੰਨ੍ਹ ਹਨ (ਅੱਖਰਾਂ ਦੇ ਉੱਪਰ/ਹੇਠਾਂ ਬਿੰਦੀਆਂ) ਇਸ ਵਿਕਲਪ ਨੂੰ <b>ਅਕਿਰਿਆਸ਼ੀਲ</b> ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਨਹੀਂ ਤਾਂ ਮਹੱਤਵਪੂਰਨ ਅੱਖਰ ਖਤਮ ਹੋ ਸਕਦੇ ਹਨ।",

        "ocr_oversample_explain": "ਨਿਰਧਾਰਤ DPI ਤੇ <b>ਟੈਕਸਟ ਪਛਾਣ ਤੋਂ ਪਹਿਲਾਂ</b> ਚਿੱਤਰ ਨੂੰ ਵੱਡਾ ਕਰਦਾ ਹੈ।<br><br>• <b>72-150 DPI:</b> ਬਹੁਤ ਤੇਜ਼, ਪਰ ਘੱਟ ਪਛਾਣ ਦਰ<br>• <b>200-300 DPI:</b> ਅਨੁਕੂਲ ਸੀਮਾ (ਮੂਲ: 300)<br>• <b>400+ DPI:</b> ਮੁਸ਼ਕਿਲ ਨਾਲ ਬਿਹਤਰ ਪਛਾਣ, ਪਰ ਮਹੱਤਵਪੂਰਨ ਤੌਰ ਤੇ ਵੱਡੀਆਂ ਫਾਈਲਾਂ<br><br>ਸਿਫਾਰਸ: ਗੁੰਝਲਦਾਰ ਲਿਪੀਆਂ ਲਈ 300 DPI (ਅਰਬੀ, ਚੀਨੀ, ਜਾਪਾਨੀ), ਪੱਛਮੀ ਭਾਸ਼ਾਵਾਂ ਲਈ 200 DPI।",

        "ocr_pagesegmode_explain": "ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ Tesseract ਪੰਨੇ ਨੂੰ ਟੈਕਸਟ ਖੇਤਰਾਂ ਵਿੱਚ ਕਿਵੇਂ ਵੰਡਦਾ ਹੈ।\n\n• <b>3 - ਆਟੋਮੈਟਿਕ (ਮੂਲ):</b> ਮਿਸ਼ਰਤ ਲੇਆਉਟ ਲਈ ਚੰਗਾ\n• <b>4 - ਇਕੱਲਾ ਕਾਲਮ:</b> ਇਕੱਲੇ-ਕਾਲਮ ਟੈਕਸਟਾਂ ਲਈ\n• <b>5 - ਲੰਬਕਾਰੀ ਬਲਾਕ:</b> ਲੰਬਕਾਰੀ ਲਿਪੀਆਂ ਲਈ (ਜਾਪਾਨੀ, ਚੀਨੀ)\n• <b>6 - ਇਕਸਾਰ ਟੈਕਸਟ ਬਲਾਕ:</b> ਬਿਨਾਂ ਕਾਲਮਾਂ ਦੇ ਵਗਦੇ ਟੈਕਸਟ ਲਈ ਅਨੁਕੂਲ\n• <b>11 - ਕੱਚਾ ਚਿੱਤਰ:</b> ਖਰਾਬ ਸਕੈਨਾਂ / ਹੱਥ ਲਿਖਤ ਲਈ\n\nਸਿਫਾਰਸ: ਸਧਾਰਨ ਟੈਕਸਟ ਦਸਤਾਵੇਜ਼ਾਂ ਲਈ <b>6</b>, ਗੁੰਝਲਦਾਰ ਲੇਆਉਟ ਲਈ <b>3</b>।",

        "ocr_oem_explain": "Tesseract ਦਾ OCR ਇੰਜਣ ਚੁਣਦਾ ਹੈ।\n\n• <b>0 - Legacy:</b> ਪੁਰਾਣਾ ਇੰਜਣ (ਤੇਜ਼, ਪਰ ਘੱਟ ਸਹੀ)\n• <b>1 - LSTM:</b> ਨਿਊਰਲ ਇੰਜਣ (ਹੌਲੀ, ਪਰ ਵਧੇਰੇ ਸਹੀ)\n• <b>2 - Legacy + LSTM:</b> ਦੋਵੇਂ ਨਤੀਜਿਆਂ ਨੂੰ ਜੋੜਦਾ ਹੈ\n• <b>3 - ਮੂਲ (LSTM ਤਰਜੀਹੀ):</b> ਜ਼ਿਆਦਾਤਰ ਮਾਮਲਿਆਂ ਲਈ ਵਧੀਆ ਵਿਕਲਪ\n\nਸਿਫਾਰਸ: ਵੱਧ ਤੋਂ ਵੱਧ ਪਛਾਣ ਸ਼ੁੱਧਤਾ ਲਈ <b>3</b>।",

        "ocr_optimize_explain": "ਆਉਟਪੁਟ PDF ਨੂੰ ਸੰਕੁਚਿਤ ਕਰਦਾ ਹੈ।\n\n• <b>0:</b> ਕੋਈ ਅਨੁਕੂਲਨ ਨਹੀਂ (ਸਭ ਤੋਂ ਤੇਜ਼ ਪ੍ਰਕਿਰਿਆ)\n• <b>1:</b> ਹਲਕਾ ਅਨੁਕੂਲਨ (ਚੰਗਾ ਸਮਝੌਤਾ)\n• <b>2:</b> ਦਰਮਿਆਨਾ ਅਨੁਕੂਲਨ\n• <b>3:</b> ਮਜ਼ਬੂਤ ਅਨੁਕੂਲਨ (ਸਭ ਤੋਂ ਛੋਟੀ ਫਾਈਲ, ਪਰ ਹੌਲੀ)\n\nਸਿਫਾਰਸ: ਰੋਜ਼ਾਨਾ ਵਰਤੋਂ ਲਈ <b>1</b>।",

        "ocr_jobs_explain": "OCR ਲਈ ਸਮਾਨਾਂਤਰ ਪ੍ਰਕਿਰਿਆਵਾਂ ਦੀ ਗਿਣਤੀ।\n\n• <b>1:</b> ਹੌਲੀ, ਪਰ ਸਭ ਤੋਂ ਘੱਟ ਮੈਮੋਰੀ ਖਪਤ\n• <b>4-8:</b> ਆਧੁਨਿਕ ਮਲਟੀ-ਕੋਰ ਪ੍ਰੋਸੈਸਰਾਂ ਲਈ ਅਨੁਕੂਲ\n• <b>12+:</b> ਉੱਚ ਮੈਮੋਰੀ ਵਰਤੋਂ ਦੇ ਨਾਲ ਮੁਸ਼ਕਿਲ ਨਾਲ ਤੇਜ਼ ਪ੍ਰਕਿਰਿਆ\n\nਸਿਫਾਰਸ: CPU ਕੋਰਾਂ ਦੀ ਗਿਣਤੀ (ਜਿਵੇਂ 4-ਕੋਰ ਸਿਸਟਮਾਂ ਤੇ <b>4</b>)।",

        "ocr_verbose_explain": "ਕੰਸੋਲ ਵਿੱਚ ਲੌਗ ਆਉਟਪੁਟ ਦਾ ਵੇਰਵਾ ਪੱਧਰ।\n\n• <b>0:</b> ਕੋਈ ਆਉਟਪੁਟ ਨਹੀਂ\n• <b>1:</b> ਪ੍ਰਗਤੀ ਅਤੇ ਸਥਿਤੀ ਸੰਦੇਸ਼\n• <b>2:</b> ਵਿਸਤ੍ਰਿਤ ਆਉਟਪੁਟ\n• <b>3:</b> ਪੂਰੀ ਡੀਬਗ ਆਉਟਪੁਟ (ਬਹੁਤ ਵਿਆਪਕ)\n\nਸਿਫਾਰਸ: ਆਮ ਕਾਰਜ ਲਈ <b>1</b>।",

        "ocr_reset_title": "ਸੈਟਿੰਗਾਂ ਰੀਸੈਟ ਕੀਤੀਆਂ ਗਈਆਂ",
        "ocr_reset_message": "ਸਾਰੀਆਂ OCR ਸੈਟਿੰਗਾਂ ਮੂਲ ਮੁੱਲਾਂ ਤੇ ਰੀਸੈਟ ਕਰ ਦਿੱਤੀਆਂ ਗਈਆਂ ਹਨ।",
        "info_tooltip": "ਇਸ ਪੈਰਾਮੀਟਰ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ",
        "ocr_reset_defaults": "ਮੂਲ ਤੇ ਰੀਸੈਟ ਕਰੋ",

        "ocr_psm_0": "ਆਟੋਮੈਟਿਕ (Legacy ਇੰਜਣ)",
        "ocr_psm_1": "ਆਟੋਮੈਟਿਕ ਕਾਲਮ ਖੋਜ",
        "ocr_psm_3": "ਆਟੋਮੈਟਿਕ (ਮੂਲ)",
        "ocr_psm_4": "ਇਕੱਲਾ ਕਾਲਮ",
        "ocr_psm_5": "ਲੰਬਕਾਰੀ ਬਲਾਕ",
        "ocr_psm_6": "ਇਕਸਾਰ ਟੈਕਸਟ ਬਲਾਕ",
        "ocr_psm_7": "ਇਕੱਲੀ ਟੈਕਸਟ ਲਾਈਨ",
        "ocr_psm_8": "ਇਕੱਲਾ ਸ਼ਬਦ",
        "ocr_psm_11": "ਕੱਚਾ ਚਿੱਤਰ (ਕੋਈ ਲੇਆਉਟ ਵਿਸ਼ਲੇਸ਼ਣ ਨਹੀਂ)",

        "ocr_oem_0": "Legacy ਇੰਜਣ (ਤੇਜ਼)",
        "ocr_oem_1": "LSTM ਇੰਜਣ (ਨਿਊਰਲ, ਸਹੀ)",
        "ocr_oem_2": "Legacy + LSTM ਸੰਯੁਕਤ",
        "ocr_oem_3": "ਮੂਲ (LSTM ਤਰਜੀਹੀ)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR ਭਾਸ਼ਾ(ਵਾਂ)...",
        "ocr_language_title": "OCR ਭਾਸ਼ਾ(ਵਾਂ) ਚੁਣੋ",
        "ocr_language_instruction": "ਟੈਕਸਟ ਪਛਾਣ (OCR) ਲਈ ਭਾਸ਼ਾ(ਵਾਂ) ਚੁਣੋ।\nਸਾਵਧਾਨ: ਕਈ ਭਾਸ਼ਾਵਾਂ ਪ੍ਰਦਰਸ਼ਨ ਅਤੇ ਸ਼ੁੱਧਤਾ ਦੀ ਕੀਮਤ ਤੇ ਆਉਂਦੀਆਂ ਹਨ!\nਤੁਸੀਂ ਸਭ ਤੋਂ ਵਧੀਆ ਨਤੀਜੇ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹੋ ਜੇਕਰ ਤੁਸੀਂ ਸਿਰਫ ਇੱਕ ਭਾਸ਼ਾ ਚੁਣਦੇ ਹੋ।",
        "ocr_language_predefined": "ਪੂਰਵ-ਪਰਿਭਾਸ਼ਿਤ ਸੰਜੋਗ",
        "ocr_language_custom": "ਕਸਟਮ...",
        "ocr_language_selected": "ਚੁਣੀਆਂ ਗਈਆਂ OCR ਭਾਸ਼ਾਵਾਂ",
        "ocr_language_changed": "OCR ਭਾਸ਼ਾ ਨੂੰ {0} ਵਿੱਚ ਬਦਲ ਦਿੱਤਾ ਗਿਆ",
        "ocr_language_auto_detect": "ਉਪਲਬਧ ਭਾਸ਼ਾਵਾਂ ਆਪਣੇ ਆਪ ਖੋਜੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।",
        "ocr_language_none_found": "ਕੋਈ Tesseract ਭਾਸ਼ਾ ਡੇਟਾ ਨਹੀਂ ਮਿਲਿਆ! ਕਿਰਪਾ ਕਰਕੇ ਭਾਸ਼ਾ ਪੈਕੇਜ ਸਥਾਪਿਤ ਕਰੋ (ਜਿਵੇਂ 'tesseract-ocr-deu', 'tesseract-ocr-eng')।",
        "ocr_language_select_custom": "ਕਸਟਮ ਭਾਸ਼ਾ ਚੋਣ",
        "ocr_language_available": "ਉਪਲਬਧ ਭਾਸ਼ਾਵਾਂ (ਸਥਾਪਿਤ):",
        "ocr_language_select_hint": "ਇੱਕ ਜਾਂ ਵੱਧ ਭਾਸ਼ਾਵਾਂ ਚੁਣੋ:",
        "ocr_language_confirm": "ਲਾਗੂ ਕਰੋ",
        "ocr_language_reset": "ਮੂਲ ਤੇ ਰੀਸੈਟ ਕਰੋ (deu+eng+vie)",
        "ocr_language_priorities": "ਸਿਫਾਰਸ਼ ਕੀਤੀਆਂ ਭਾਸ਼ਾਵਾਂ (ਪਹਿਲਾਂ ਤੋਂ ਸਥਾਪਿਤ):",

        "select_all_languages": "ਸਭ ਚੁਣੋ",
        "clear_all_languages": "ਚੋਣ ਸਾਫ਼ ਕਰੋ",
        "install_language_packs": "ਗੁੰਮ ਭਾਸ਼ਾ ਪੈਕੇਜ ਸਥਾਪਿਤ ਕਰੋ...",
        "install_hint": "💡 ਸੁਝਾਅ: ਤੁਹਾਡੇ ਸਿਸਟਮ ਤੇ ਸਾਰੀਆਂ ਭਾਸ਼ਾਵਾਂ ਸਥਾਪਿਤ ਨਹੀਂ ਹਨ। ਇਸ ਬਟਨ ਰਾਹੀਂ ਤੁਹਾਨੂੰ ਸਥਾਪਨਾ ਲਈ ਸਹਾਇਤਾ ਮਿਲੇਗੀ।",
        "ocr_language_install_title": "Tesseract ਭਾਸ਼ਾ ਪੈਕੇਜਾਂ ਦੀ ਸਥਾਪਨਾ",

        "ocr_missing_languages": "ਗੁੰਮ OCR ਭਾਸ਼ਾ ਪੈਕੇਜ",
        "ocr_missing_languages_message": "ਹੇਠ ਲਿਖੀਆਂ ਚੁਣੀਆਂ ਗਈਆਂ ਭਾਸ਼ਾਵਾਂ ਤੁਹਾਡੇ ਸਿਸਟਮ ਤੇ ਸਥਾਪਿਤ ਨਹੀਂ ਹਨ:\n\n{0}\n\nਕਿਰਪਾ ਕਰਕੇ ਗੁੰਮ ਭਾਸ਼ਾ ਪੈਕੇਜ ਸਥਾਪਿਤ ਕਰੋ ('ਸਥਾਪਨਾ ਸਹਾਇਤਾ' ਅਧੀਨ ਸਹਾਇਤਾ ਵੇਖੋ)।\n\nਕੀ ਤੁਸੀਂ ਹੁਣ ਸਥਾਪਨਾ ਸਹਾਇਤਾ ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        "ocr_missing_languages_voice": "ਗੁੰਮ ਭਾਸ਼ਾ ਪੈਕੇਜ। ਕਿਰਪਾ ਕਰਕੇ ਗੁੰਮ ਭਾਸ਼ਾਵਾਂ ਸਥਾਪਿਤ ਕਰੋ।",
        "ocr_install_help_now": "ਸਹਾਇਤਾ ਖੋਲ੍ਹੋ",
        "ocr_continue_anyway": "ਫਿਰ ਵੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ",
        "ocr_language_error_title": "OCR ਭਾਸ਼ਾ ਗਲਤੀ",
        "ocr_language_error_message": "ਟੈਕਸਟ ਪਛਾਣ ਦੌਰਾਨ ਗਲਤੀ: {0}\n\nਕਿਰਪਾ ਕਰਕੇ ਆਪਣੀਆਂ OCR ਭਾਸ਼ਾ ਸੈਟਿੰਗਾਂ ਜਾਂਚ ਕਰੋ (ਸੈਟਿੰਗਾਂ → OCR ਭਾਸ਼ਾ)।",
        "ocr_install_help_button": "ਸਥਾਪਨਾ ਸਹਾਇਤਾ",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract ਭਾਸ਼ਾ ਪੈਕੇਜ ਸਥਾਪਿਤ ਕਰੋ</p>

        <p>OCR ਨੂੰ ਕਿਸੇ ਖਾਸ ਭਾਸ਼ਾ ਵਿੱਚ ਕੰਮ ਕਰਨ ਲਈ, ਸੰਬੰਧਿਤ ਭਾਸ਼ਾ ਡੇਟਾ ਤੁਹਾਡੇ ਸਿਸਟਮ ਤੇ ਸਥਾਪਿਤ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ। ਆਪਣੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਲਈ ਹਿਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li><strong>ਟਰਮੀਨਲ</strong> ਖੋਲ੍ਹੋ (Finder → ਪ੍ਰੋਗਰਾਮ → ਉਪਯੋਗਤਾਵਾਂ → ਟਰਮੀਨਲ)।</li>
        <li>ਸਾਰੀਆਂ ਉਪਲਬਧ ਭਾਸ਼ਾਵਾਂ ਸਥਾਪਿਤ ਕਰੋ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (ਇਸ ਵਿੱਚ ਕੁਝ ਮਿੰਟ ਲੱਗ ਸਕਦੇ ਹਨ।)</li>
        <li>ਜਾਂ ਸਿਰਫ ਵਿਅਕਤੀਗਤ ਭਾਸ਼ਾਵਾਂ (ਜਿਵੇਂ ਵੀਅਤਨਾਮੀ):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        ਮੌਜੂਦਾ Homebrew ਸੰਸਕਰਣਾਂ ਦੇ ਨਾਲ, <code>*.traineddata</code> ਨੂੰ ਹੱਥੀਂ ਡਾਊਨਲੋਡ ਕਰਨ ਦੀ ਲੋੜ ਹੋ ਸਕਦੀ ਹੈ (ਹੇਠਾਂ ਵੇਖੋ)।</li>
        <li>ਸਥਾਪਨਾ ਤੋਂ ਬਾਅਦ: ਇਸ ਡਾਇਲਾਗ ਨੂੰ ਬੰਦ ਕਰੋ ਅਤੇ OCR ਭਾਸ਼ਾ ਚੋਣ ਨੂੰ ਦੁਬਾਰਾ ਖੋਲ੍ਹੋ – ਨਵੀਆਂ ਭਾਸ਼ਾਵਾਂ ਆਪਣੇ ਆਪ ਦਿਖਾਈ ਦੇਣਗੀਆਂ।</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>ਇੱਕ ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ (Ctrl+Alt+T)।</li>
        <li>ਲੋੜੀਂਦੀ ਭਾਸ਼ਾ ਸਥਾਪਿਤ ਕਰੋ, ਜਿਵੇਂ ਵੀਅਤਨਾਮੀ ਲਈ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        ਮਹੱਤਵਪੂਰਨ ਭਾਸ਼ਾ ਕੋਡ: <code>deu</code> (ਜਰਮਨ), <code>eng</code> (ਅੰਗਰੇਜ਼ੀ), <code>vie</code> (ਵੀਅਤਨਾਮੀ), <code>spa</code> (ਸਪੈਨਿਸ਼), <code>fra</code> (ਫਰੈਂਚ), <code>ita</code> (ਇਤਾਲਵੀ), <code>nld</code> (ਡੱਚ), <code>fin</code> (ਫਿਨਿਸ਼), <code>swe</code> (ਸਵੀਡਿਸ਼), <code>nor</code> (ਨਾਰਵੇਜੀਅਨ)।</li>
        <li>ਸਾਰੇ ਉਪਲਬਧ ਪੈਕੇਜ ਦਿਖਾਓ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ਹੱਥੀਂ)</p>
        <ol>
        <li>ਲੋੜੀਂਦੀਆਂ <code>*.traineddata</code> ਫਾਈਲਾਂ ਇੱਥੋਂ ਡਾਊਨਲੋਡ ਕਰੋ:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ਜਿਵੇਂ ਵੀਅਤਨਾਮੀ ਲਈ <code>vie.traineddata</code>)।</li>
        <li>ਫਾਈਲਾਂ ਨੂੰ Tesseract ਭਾਸ਼ਾ ਫੋਲਡਰ ਵਿੱਚ ਕਾਪੀ ਕਰੋ, ਆਮ ਤੌਰ ਤੇ:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (ਵਿਅਕਤੀਗਤ ਸਥਾਪਨਾ ਦੇ ਅਨੁਸਾਰ ਐਡਜਸਟ ਕਰੋ।)</li>
        <li>ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰੋ (ਜਾਂ OCR ਭਾਸ਼ਾ ਚੋਣ ਨੂੰ ਦੁਬਾਰਾ ਖੋਲ੍ਹੋ)।</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 ਸਾਰੇ ਸਿਸਟਮਾਂ ਲਈ ਵਿਕਲਪ</p>
        <ul>
        <li>ਆਪਣੀ ਪਸੰਦ ਦੇ ਪੈਕੇਜ ਮੈਨੇਜਰ ਨਾਲ <strong>OCRmyPDF</strong> ਅਤੇ <strong>Tesseract</strong> ਸਥਾਪਿਤ ਕਰੋ। ਜ਼ਿਆਦਾਤਰ ਸਥਾਪਨਾਵਾਂ ਵਿੱਚ ਪਹਿਲਾਂ ਹੀ ਕੁਝ ਮਿਆਰੀ ਭਾਸ਼ਾਵਾਂ ਸ਼ਾਮਲ ਹੁੰਦੀਆਂ ਹਨ (ਅੰਗਰੇਜ਼ੀ, ਜਰਮਨ, ਫਰੈਂਚ)।</li>
        <li>ਗੁੰਮ ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਕਿਸੇ ਵੀ ਸਮੇਂ ਸਥਾਪਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ – OCR ਭਾਸ਼ਾ ਚੋਣ ਸਿਰਫ ਅਸਲ ਵਿੱਚ ਮੌਜੂਦ ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਸੂਚੀਬੱਧ ਕਰਦੀ ਹੈ।</li>
        </ul>

        <hr>
        <p><b>✅ ਸਥਾਪਨਾ ਤੋਂ ਬਾਅਦ:</b> ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰਨ ਦੀ ਕੋਈ ਲੋੜ ਨਹੀਂ – ਨਵੀਂ ਜੋੜੀਆਂ ਗਈਆਂ ਭਾਸ਼ਾਵਾਂ ਤੁਰੰਤ ਸੂਚੀ ਵਿੱਚ ਦਿਖਾਈ ਦੇਣਗੀਆਂ।</p>
        <p><b>📖 ਭਾਸ਼ਾ ਕੋਡਾਂ ਲਈ ਸਹਾਇਤਾ:</b> ਇੱਕ ਪੂਰੀ ਸੂਚੀ <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract ਦਸਤਾਵੇਜ਼</a> ਵਿੱਚ ਉਪਲਬਧ ਹੈ।</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans ਫੌਂਟ",
        "info_noto_font_voice": "Noto Sans ਫੌਂਟ ਸਥਾਪਨਾ ਗਾਈਡ",
        "btn_info_noto_font_install": "ਫੌਂਟ ਜਾਣਕਾਰੀ",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Google ਦੇ ਮੁਫਤ Noto ਫੌਂਟਾਂ ਨੂੰ ਕਿਵੇਂ ਸਥਾਪਿਤ ਕਰੀਏ</h2>

        <p><strong>Noto ਫੌਂਟ</strong> Google ਦਾ ਇੱਕ ਓਪਨ-ਸੋਰਸ ਫੌਂਟ ਪਰਿਵਾਰ ਹੈ। ਉਹਨਾਂ ਦਾ ਟੀਚਾ <em>"ਕੋਈ ਟੋਫੂ ਨਹੀਂ"</em> (ਭਾਵ ਖਾਲੀ ਬਕਸੇ □ ਨਹੀਂ) ਦੇਖਣਾ ਅਤੇ ਯੂਨੀਕੋਡ ਮਿਆਰ ਦੇ ਹਰ ਅੱਖਰ ਨੂੰ ਸਹੀ ਢੰਗ ਨਾਲ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰਨਾ ਹੈ। ਉਹ ਉਹਨਾਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਲਈ ਆਦਰਸ਼ ਵਾਧਾ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਬਹੁਤ ਸਾਰੀਆਂ ਵੱਖ-ਵੱਖ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਟੈਕਸਟ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 macOS ਤੇ ਸਥਾਪਨਾ</h3>

        <p><strong>ਢੰਗ 1: Homebrew ਨਾਲ (ਉੱਨਤ ਉਪਭੋਗਤਾਵਾਂ ਲਈ)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>ਢੰਗ 2: "ਫੌਂਟ ਬੁੱਕ" ਰਾਹੀਂ (ਸਿਫਾਰਸ਼ੀ)</strong></p>

        <ol>
        <li>ਅਧਿਕਾਰਤ ਫੌਂਟ ਪੈਕੇਜ ਡਾਊਨਲੋਡ ਕਰੋ:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP ਫਾਈਲ ਕੱਢੋ</li>
        <li>ਫਾਈਲਾਂ ਨੂੰ <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code> ਵਿੱਚ ਕਾਪੀ ਕਰੋ</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Windows ਤੇ ਸਥਾਪਨਾ (10 ਅਤੇ 11)</h3>

        <p><strong>ਢੰਗ 1: Microsoft Store (ਸਿਫਾਰਸ਼ੀ)</strong><br>
        "Google Noto Fonts" ਜਾਂ "Noto Sans" ਖੋਜੋ ਅਤੇ <strong>ਸਥਾਪਿਤ ਕਰੋ</strong> ਤੇ ਕਲਿੱਕ ਕਰੋ।</p>

        <p><strong>ਢੰਗ 2: ਹੱਥੀਂ ਸਥਾਪਨਾ</strong></p>

        <ol>
        <li>ਡਾਊਨਲੋਡ ਕਰੋ:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP ਕੱਢੋ</li>
        <li>.ttf / .otf ਫਾਈਲਾਂ ਚੁਣੋ</li>
        <li>ਸੱਜਾ-ਕਲਿੱਕ → <strong>ਸਥਾਪਿਤ ਕਰੋ</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        ਜਾਂ<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\ਨਾਮ\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Linux ਤੇ ਸਥਾਪਨਾ</h3>

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

        <p>ਤਸਦੀਕ:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "ਬੁੱਕਮਾਰਕ ਪ੍ਰਬੰਧਿਤ ਕਰੋ",
        "bookmark_add": "ਬੁੱਕਮਾਰਕ ਸ਼ਾਮਲ ਕਰੋ",
        "bookmark_add_tooltip": "ਮੌਜੂਦਾ ਪੰਨੇ ਨੂੰ ਬੁੱਕਮਾਰਕ ਵਜੋਂ ਸੁਰੱਖਿਅਤ ਕਰੋ",
        "bookmark_remove": "ਬੁੱਕਮਾਰਕ ਹਟਾਓ",
        "bookmark_remove_tooltip": "ਨਿਸ਼ਾਨਬੱਧ ਬੁੱਕਮਾਰਕ ਨੂੰ ਮਿਟਾਓ",
        "bookmark_remove_all": "ਸਭ ਹਟਾਓ",
        "bookmark_remove_all_tooltip": "ਇਸ PDF ਦੇ ਸਾਰੇ ਬੁੱਕਮਾਰਕ ਮਿਟਾਓ",
        "bookmark_jump": "ਬੁੱਕਮਾਰਕ ਤੇ ਜਾਓ",
        "bookmark_jump_tooltip": "ਚੁਣੇ ਪੰਨੇ ਤੇ ਜਾਓ",
        "bookmark_name": "ਨਾਮ",
        "bookmark_page": "ਪੰਨਾ",
        "bookmark_no_bookmarks": "ਕੋਈ ਬੁੱਕਮਾਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ।\nਮੌਜੂਦਾ ਪੰਨੇ ਨੂੰ ਬੁੱਕਮਾਰਕ ਵਜੋਂ ਸੁਰੱਖਿਅਤ ਕਰਨ ਲਈ 'ਸ਼ਾਮਲ ਕਰੋ' ਤੇ ਕਲਿੱਕ ਕਰੋ।",
        "bookmark_added": "ਪੰਨਾ {0} ਲਈ ਬੁੱਕਮਾਰਕ ਸ਼ਾਮਲ ਕੀਤਾ ਗਿਆ: {1}",
        "bookmark_removed": "ਬੁੱਕਮਾਰਕ ਹਟਾ ਦਿੱਤਾ ਗਿਆ: {0}",
        "bookmark_all_removed": "ਸਾਰੇ ਬੁੱਕਮਾਰਕ ਹਟਾ ਦਿੱਤੇ ਗਏ ਹਨ।",
        "bookmark_name_default": "ਪੰਨਾ {0}",
        "bookmark_name_prompt": "ਬੁੱਕਮਾਰਕ ਲਈ ਨਾਮ:\n(ਲੰਬੇ ਟੈਕਸਟ ਨੂੰ 50 ਅੱਖਰਾਂ ਤੱਕ ਛੋਟਾ ਕੀਤਾ ਜਾਵੇਗਾ)",
        "bookmark_name_prompt_title": "ਬੁੱਕਮਾਰਕ ਨਾਮ",
        "bookmark_confirm_remove_all": "ਕੀ ਤੁਸੀਂ ਪੱਕਾ ਸਾਰੇ {0} ਬੁੱਕਮਾਰਕ ਹਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        "menu_bookmarks": "ਬੁੱਕਮਾਰਕ",
        "bookmark_manage": "ਬੁੱਕਮਾਰਕ ਪ੍ਰਬੰਧਿਤ ਕਰੋ",
        "bookmark_next": "ਅਗਲਾ ਬੁੱਕਮਾਰਕ",
        "bookmark_prev": "ਪਿਛਲਾ ਬੁੱਕਮਾਰਕ",
        "bookmark_page_display": "ਪੰਨਾ {0}",
        "bookmark_exists": "ਇਸ ਪੰਨੇ ਲਈ ਇਸ ਨਾਮ ਦਾ ਬੁੱਕਮਾਰਕ ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਹੈ।",
        "bookmark_select_first": "ਕਿਰਪਾ ਕਰਕੇ ਪਹਿਲਾਂ ਇੱਕ ਬੁੱਕਮਾਰਕ ਚੁਣੋ।",
        "bookmark_confirm_remove": "ਕੀ ਤੁਸੀਂ ਪੱਕਾ 'ਪੰਨਾ {0}: {1}' ਬੁੱਕਮਾਰਕ ਹਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?",
        "bookmark_jumped_to": "ਪੰਨਾ {1} ਤੇ ਬੁੱਕਮਾਰਕ '{0}' ਤੇ ਚਲੇ ਗਏ।",
        "bookmark_jumped_to_voice": "ਬੁੱਕਮਾਰਕ {0}, ਪੰਨਾ {1}",
        "btn_close": "ਬੰਦ ਕਰੋ",

        "bookmark_list": "ਤੁਹਾਡੇ ਬੁੱਕਮਾਰਕ",
        "bookmark_rename": "ਬੁੱਕਮਾਰਕ ਦਾ ਨਾਮ ਬਦਲੋ",
        "bookmark_rename_tooltip": "ਚੁਣੇ ਬੁੱਕਮਾਰਕ ਦਾ ਨਾਮ ਬਦਲੋ",
        "bookmark_rename_title": "ਬੁੱਕਮਾਰਕ ਦਾ ਨਾਮ ਬਦਲੋ",
        "bookmark_rename_prompt": "ਪੰਨਾ {0} ਤੇ ਬੁੱਕਮਾਰਕ ਲਈ ਨਵਾਂ ਨਾਮ:\n(ਵੱਧ ਤੋਂ ਵੱਧ 50 ਅੱਖਰ)",
        "bookmark_renamed": "ਬੁੱਕਮਾਰਕ '{0}' ਦਾ ਨਾਮ ਬਦਲ ਕੇ '{1}' ਕਰ ਦਿੱਤਾ ਗਿਆ।",
        "bookmark_item_tooltip": "ਪੰਨਾ {0}: {1}\nਜਾਣ ਲਈ ਡਬਲ-ਕਲਿੱਕ ਕਰੋ",
        "bookmark_name_exists_question": "ਇਸ ਪੰਨੇ ਤੇ ਪਹਿਲਾਂ ਤੋਂ '{0}' ਨਾਮ ਦਾ ਬੁੱਕਮਾਰਕ ਮੌਜੂਦ ਹੈ।\nਫਿਰ ਵੀ ਨਾਮ ਬਦਲਣਾ ਹੈ?",

        "context_bookmarks": "ਬੁੱਕਮਾਰਕ",
        "context_bookmark_add_here": "ਇਸ ਪੰਨੇ ਲਈ ਬੁੱਕਮਾਰਕ ਸ਼ਾਮਲ ਕਰੋ",
        "context_bookmarks_existing": "ਮੌਜੂਦਾ ਬੁੱਕਮਾਰਕ:",
        "context_bookmarks_jump": "ਬੁੱਕਮਾਰਕ ਤੇ ਜਾਓ:",
        "context_bookmarks_none": "ਕੋਈ ਬੁੱਕਮਾਰਕ ਮੌਜੂਦ ਨਹੀਂ ਹੈ",
        "context_bookmarks_clear_all": "ਸਾਰੇ {0} ਬੁੱਕਮਾਰਕ ਹਟਾਓ",

        "bookmark_search_placeholder": "ਬੁੱਕਮਾਰਕ ਖੋਜੋ... (ਨਾਮ ਜਾਂ ਪੰਨਾ)",
        "bookmark_search_results": "\"%s\" ਲਈ %d ਬੁੱਕਮਾਰਕ ਮਿਲੇ",
        "bookmark_no_search_results": "\"%s\" ਲਈ ਕੋਈ ਬੁੱਕਮਾਰਕ ਨਹੀਂ ਮਿਲਿਆ",
        "bookmark_no_search_results_label": "\"%s\" ਲਈ ਕੋਈ ਨਤੀਜਾ ਨਹੀਂ",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF ਮੈਟਾਡੇਟਾ ਸੰਪਾਦਿਤ ਕਰੋ",
        "metadata_title": "ਸਿਰਲੇਖ",
        "metadata_title_placeholder": "ਦਸਤਾਵੇਜ਼ ਸਿਰਲੇਖ",
        "metadata_title_tooltip": "ਦਸਤਾਵੇਜ਼ ਦਾ ਸਿਰਲੇਖ (ਸਿਰਲੇਖ ਪੱਟੀ ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ)",
        "metadata_author": "ਲੇਖਕ",
        "metadata_author_placeholder": "ਲੇਖਕ ਦਾ ਨਾਮ",
        "metadata_author_tooltip": "ਦਸਤਾਵੇਜ਼ ਦਾ ਸਿਰਜਣਹਾਰ",
        "metadata_subject": "ਵਿਸ਼ਾ",
        "metadata_subject_placeholder": "ਦਸਤਾਵੇਜ਼ ਦਾ ਵਿਸ਼ਾ",
        "metadata_subject_tooltip": "ਸਮੱਗਰੀ ਦਾ ਸੰਖੇਪ ਵਰਣਨ",
        "metadata_keywords": "ਕੀਵਰਡ",
        "metadata_keywords_placeholder": "ਕਾਮਿਆਂ ਦੁਆਰਾ ਵੱਖ ਕੀਤੇ ਗਏ ਕੀਵਰਡ",
        "metadata_keywords_tooltip": "ਦਸਤਾਵੇਜ਼ ਨੂੰ ਸ਼੍ਰੇਣੀਬੱਧ ਕਰਨ ਲਈ ਕੀਵਰਡ",
        "metadata_creator": "ਸਿਰਜਣਹਾਰ",
        "metadata_creator_placeholder": "ਐਪਲੀਕੇਸ਼ਨ ਜਿਸਨੇ PDF ਬਣਾਇਆ",
        "metadata_creator_tooltip": "ਸਾਫਟਵੇਅਰ ਜਿਸ ਨਾਲ ਦਸਤਾਵੇਜ਼ ਬਣਾਇਆ ਗਿਆ ਸੀ",
        "metadata_producer": "ਨਿਰਮਾਤਾ",
        "metadata_producer_placeholder": "ਐਪਲੀਕੇਸ਼ਨ ਜਿਸਨੇ PDF ਬਦਲਿਆ",
        "metadata_producer_tooltip": "ਸਾਫਟਵੇਅਰ ਜਿਸਨੇ PDF ਬਦਲਿਆ",
        "metadata_creation_date": "ਸਿਰਜਣਾ ਮਿਤੀ",
        "metadata_creation_date_tooltip": "ਦਸਤਾਵੇਜ਼ ਸਿਰਜਣਾ ਦੀ ਮਿਤੀ",
        "metadata_mod_date": "ਸੋਧ ਮਿਤੀ",
        "metadata_mod_date_tooltip": "ਆਖਰੀ ਸੋਧ ਦੀ ਮਿਤੀ",
        "metadata_pdf_info": "📄 PDF ਜਾਣਕਾਰੀ",
        "metadata_pages": "ਪੰਨਿਆਂ ਦੀ ਗਿਣਤੀ",
        "metadata_file_size": "ਫਾਈਲ ਅਕਾਰ",
        "metadata_pdf_version": "PDF ਵਰਜਨ",
        "metadata_encrypted": "ਏਨਕ੍ਰਿਪਟ ਕੀਤਾ",
        "metadata_encrypted_yes": "ਹਾਂ (ਪਾਸਵਰਡ ਸੁਰੱਖਿਅਤ)",
        "metadata_encrypted_no": "ਨਹੀਂ",
        "metadata_reload": "📂 PDF ਤੋਂ ਮੁੜ ਲੋਡ ਕਰੋ",
        "metadata_reset": "ਤਬਦੀਲੀਆਂ ਨੂੰ ਰੱਦ ਕਰੋ",
        "metadata_reloaded": "ਮੈਟਾਡੇਟਾ PDF ਤੋਂ ਮੁੜ ਲੋਡ ਕੀਤਾ ਗਿਆ ਸੀ।",
        "metadata_reset_done": "ਸਾਰੇ ਮੈਟਾਡੇਟਾ ਖੇਤਰ ਰੀਸੈਟ ਕਰ ਦਿੱਤੇ ਗਏ ਹਨ।",
        "metadata_no_file": "ਕੋਈ PDF ਫਾਈਲ ਲੋਡ ਨਹੀਂ ਕੀਤੀ ਗਈ।",
        "metadata_save_error": "ਮੈਟਾਡੇਟਾ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਵਿੱਚ ਗਲਤੀ",
        "metadata_saved": "ਮੈਟਾਡੇਟਾ ਸਫਲਤਾਪੂਰਵਕ ਸੁਰੱਖਿਅਤ ਕਰ ਲਿਆ ਗਿਆ।",
        "metadata_pdf_version_unknown": "PDF (ਅਣਜਾਣ)",
        "metadata_saved_message": "ਮੈਟਾਡੇਟਾ ਸਫਲਤਾਪੂਰਵਕ ਸੁਰੱਖਿਅਤ ਕਰ ਲਿਆ ਗਿਆ।",
        "metadata_saved_voice": "ਮੈਟਾਡੇਟਾ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ।",

        "metadata_custom": "🔧 ਕਸਟਮ ਮੈਟਾਡੇਟਾ",
        "metadata_custom_placeholder": "{\n  \"ਮੇਰਾ_ਖੇਤਰ\": \"ਮੇਰਾ_ਮੁੱਲ\",\n  \"ਹੋਰ_ਖੇਤਰ\": 123\n}",
        "metadata_custom_tooltip": "ਕਸਟਮ ਮੈਟਾਡੇਟਾ ਲਈ JSON ਫਾਰਮੈਟ (ਵਿਕਲਪਿਕ)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "ਟੈਂਪਲੇਟ \"{0}\" ਚੁਣਿਆ ਗਿਆ - ਪਾਉਣ ਲਈ ਡਬਲ-ਕਲਿੱਕ ਕਰੋ",
        "text_use_template": "ਟੈਕਸਟ ਬਲਾਕ ਵਰਤੋ",
        "text_type": "ਕਿਸਮ",
        "text_search_templates": "ਟੈਕਸਟ ਬਲਾਕ ਖੋਜੋ...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 ਨਿਰਯਾਤ / ਆਯਾਤ ਜਾਣਕਾਰੀ",
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

        <h3>📦 ਕੀ ਨਿਰਯਾਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ? (ਸੰਖੇਪ ਜਾਣਕਾਰੀ)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">ਆਮ ਐਪਲੀਕੇਸ਼ਨ ਸੈਟਿੰਗਾਂ</span></li>
            <li class="detail">• ਡਾਰਕ/ਲਾਈਟ ਮੋਡ</li>
            <li class="detail">• ਚਿੱਤਰਾਂ ਲਈ ਡਾਰਕ-ਮੋਡ ਉਲਟਾ</li>
            <li class="detail">• ਸਲੇਟੀ ਥ੍ਰੈਸ਼ਹੋਲਡ ਮੁੱਲ</li>
            <li class="detail">• ਭਾਸ਼ਾ</li>
            <li class="detail">• ਵਿੰਡੋ ਜਿਓਮੈਟਰੀ</li>
            <li class="detail">• ਜ਼ੂਮ ਮੋਡ</li>
            <li class="detail">• ਨੈਵੀਗੇਸ਼ਨ (ਨੈਵੀਗੇਸ਼ਨ ਬਾਰ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ)</li>
            <li class="detail">• ਸਪੀਚ ਆਉਟਪੁਟ (ਚਾਲੂ/ਬੰਦ)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ਬੈਕਅੱਪ ਸੈਟਿੰਗਾਂ</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ਫਾਈਲ ਨਾਮਕਰਨ (ਟਾਈਮਸਟੈਂਪ, ਵਿਭਾਜਕ, ਪਿਛੇਤਰ)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ਇਸ ਦੇ ਸੰਮਿਲਨ ਲਈ ਸੈਟਿੰਗਾਂ</span></li>
            <li class="detail">• ਦਸਤਖਤ</li>
            <li class="detail">• ਟੈਕਸਟ ਅਤੇ ਟੈਕਸਟ ਬਲਾਕ</li>
            <li class="detail">• ਨਿਸ਼ਾਨ, ਚਿੱਤਰ ਅਤੇ ਆਕਾਰ</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR ਸੈਟਿੰਗਾਂ</span></li>
            <li class="detail">• ਭਾਸ਼ਾ</li>
            <li class="detail">• OCR ਲਾਗੂ ਕਰੋ · ਪੰਨਾ ਮੋਡ</li>
            <li class="detail">• ਚਿੱਤਰ ਪੂਰਵ-ਪ੍ਰਕਿਰਿਆ: ਟੇਢਾਪਨ ਠੀਕ ਕਰੋ, ਸਾਫ਼ ਕਰੋ, ਓਵਰਸੈਂਪਲਿੰਗ</li>
            <li class="detail">• ਸਮਾਨਾਂਤਰ ਕੰਮਾਂ ਦੀ ਗਿਣਤੀ</li>
            <li class="detail">• ਉਲਟਾ ਮੋਡ</li>
            <li class="detail">• ਸਲੇਟੀ ਥ੍ਰੈਸ਼ਹੋਲਡ ਮੁੱਲ</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ਬੁੱਕਮਾਰਕ</span></li>
            <li class="detail">• ਪ੍ਰਤੀ PDF ਫਾਈਲ ਸਾਰੇ ਬੁੱਕਮਾਰਕ (ਪੰਨਾ, ਨਾਮ, ਸਿਰਜਣਾ ਸਮਾਂ)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ਪਾਸਵਰਡ ਡਾਟਾਬੇਸ</span></li>
            <li class="detail">• ਸੁਰੱਖਿਅਤ ਕੀਤੇ PDF ਪਾਸਵਰਡ (ਵਿਕਲਪਿਕ ਤੌਰ ਤੇ ਏਨਕ੍ਰਿਪਟ ਕੀਤੇ ਜਾਂ ਸਾਦਾ ਟੈਕਸਟ)</li>
            <li class="detail">• ਮਾਸਟਰ ਪਾਸਵਰਡ ਹੈਸ਼ (ਜੇ ਸੈਟ ਕੀਤਾ ਗਿਆ ਹੈ)</li>
            <li class="detail">• ਪੁਸ਼ਟੀਕਰਨ ਡੇਟਾ</li>
        </ul>

        <h4>⚠️ ਮਹੱਤਵਪੂਰਨ ਨੋਟਸ</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 ਆਯਾਤ ਕਰਦੇ ਸਮੇਂ:</strong>
            <ul>
                <li><span class="warning">➜ ਸਾਰੀਆਂ ਮੌਜੂਦਾ ਸੈਟਿੰਗਾਂ ਪੂਰੀ ਤਰ੍ਹਾਂ ਓਵਰਰਾਈਟ ਕਰ ਦਿੱਤੀਆਂ ਜਾਣਗੀਆਂ</span></li>
                <li>• ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਮੁੜ ਚਾਲੂ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ</li>
                <li>• ਮੌਜੂਦਾ ਦਸਤਖਤ, ਟੈਕਸਟ ਬਲਾਕ ਅਤੇ ਬੁੱਕਮਾਰਕ ਬਦਲ ਦਿੱਤੇ ਜਾਣਗੇ</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 ਮਾਸਟਰ ਪਾਸਵਰਡ ਅਤੇ ਨਿਰਯਾਤ ਮੋਡ:</strong>
            <ul>
                <li>• ਜਦੋਂ ਮਾਸਟਰ ਪਾਸਵਰਡ ਸਰਗਰਮ ਹੁੰਦਾ ਹੈ, ਤੁਸੀਂ ਚੁਣ ਸਕਦੇ ਹੋ:</li>
                <li>  - <span style="color: #98FB98;"><strong>ਡੀਕ੍ਰਿਪਟ ਕੀਤਾ</strong></span> (ਪਾਸਵਰਡ ZIP ਵਿੱਚ ਸਾਦੇ ਟੈਕਸਟ ਵਿੱਚ ਹਨ)</li>
                <li>  - <span style="color: #FFA07A;"><strong>ਏਨਕ੍ਰਿਪਟ ਕੀਤਾ</strong></span> (ਕੇਵਲ ਮਾਸਟਰ ਪਾਸਵਰਡ ਨਾਲ ਟਾਰਗੇਟ ਸਿਸਟਮ ਤੇ ਪੜ੍ਹਨਯੋਗ)</li>
                <li>• ਮਾਸਟਰ ਪਾਸਵਰਡ ਹੈਸ਼ ਆਪਣੇ ਆਪ ਨੂੰ <strong>ਹਮੇਸ਼ਾ</strong> ਏਨਕ੍ਰਿਪਟ ਕਰਕੇ ਸਟੋਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ ਸੁਰੱਖਿਆ ਨੋਟਿਸ:</strong>
            <ul>
                <li>• ਨਿਰਯਾਤ ਕੀਤੀ ZIP ਫਾਈਲ ਵਿੱਚ ਸੰਵੇਦਨਸ਼ੀਲ ਡੇਟਾ ਹੁੰਦਾ ਹੈ (<strong>ਪਾਸਵਰਡ, ਬੁੱਕਮਾਰਕ, ਦਸਤਖਤ</strong>)</li>
                <li>• ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖੋ (ਜਿਵੇਂ ਏਨਕ੍ਰਿਪਟਡ USB ਸਟਿਕ, ਪਾਸਵਰਡ ਮੈਨੇਜਰ)</li>
                <li>• ਜੇਕਰ ਫਾਈਲ ਗੁੰਮ ਹੋ ਜਾਂਦੀ ਹੈ, ਤਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤੇ PDF ਪਾਸਵਰਡ ਅਟੱਲ ਤੌਰ ਤੇ ਗੁੰਮ ਹੋ ਜਾਂਦੇ ਹਨ</li>
            </ul>
        </div>

        <h4>📁 ਨਿਰਯਾਤ ਫਾਰਮੈਟ</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            ਸੈਟਿੰਗਾਂ ਨੂੰ ਇੱਕੋ ZIP ਫਾਈਲ ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ਇਸ ZIP ਵਿੱਚ ਸੰਪੂਰਨ <code>settings.json</code> (ਤੁਹਾਡੀ ਕੌਂਫਿਗਰੇਸ਼ਨ ਤੋਂ) ਦੇ ਨਾਲ-ਨਾਲ ਸੰਭਾਵਤ ਤੌਰ ਤੇ ਏਮਬੇਡ ਕੀਤੀਆਂ ਦਸਤਖਤ ਚਿੱਤਰ ਫਾਈਲਾਂ ਅਤੇ ਏਨਕ੍ਰਿਪਟਡ ਪਾਸਵਰਡ ਸ਼ਾਮਲ ਹਨ।
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "ਦਸਤਖਤ - ਗਾਈਡ",
        'signature_guide_html': """
        📝 <strong>ਦਸਤਖਤ - ਤੁਰੰਤ ਗਾਈਡ</strong><br>
        <ul>
        <li>ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈਟ ਕਰੋ</li>
        <li><em>ਸੈਟਿੰਗਾਂ</em> ਮੀਨੂ ਵਿੱਚ ਦਸਤਖਤ ਸੰਰਚਿਤ ਕਰੋ (ਆਕਾਰ, ਟਾਈਮ ਸਟੈਂਪ, …)</li>
        <li>ਲੋੜੀਂਦੀ ਸਥਿਤੀ ਤੇ <strong>ਸੱਜਾ-ਕਲਿਕ</strong> ਕਰਕੇ ਪਾਓ (ਮਾਸਟਰ ਪਾਸਵਰਡ ਪ੍ਰਤੀ ਸੈਸ਼ਨ ਇੱਕ ਵਾਰ ਲੋੜੀਂਦਾ ਹੈ)</li>
        <li>ਮਾਊਸ ਜਾਂ ਤੀਰ ਕੁੰਜੀਆਂ ਨਾਲ ਦਸਤਖਤ ਨੂੰ ਹਿਲਾਓ</li>
        <li>ਇੱਕ ਤੋਂ ਬਾਅਦ ਇੱਕ ਕਈ ਦਸਤਖਤ ਪਾਓ</li>
        <li>ਹਰ ਦਸਤਖਤ ਨੂੰ ਵਿਅਕਤੀਗਤ ਰੂਪ ਵਿੱਚ ਅਨੁਕੂਲ ਬਣਾਓ</li>
        <li>ਕਿਸੇ ਇੱਕ ਦਸਤਖਤ ਨੂੰ ਰੱਦ ਕਰੋ</li>
        <li>ਸਾਰੇ ਦਸਤਖਤ ਇੱਕ ਵਾਰ ਸੇਵ / ਰੱਦ ਕਰੋ</li>
        <li>ਵਿਕਲਪਕ ਤੌਰ ਤੇ, ਮੀਨੂ ਬਾਰ ਵੀ ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ।</li>
        </ul>
        """,
        'signature_guide_voice': "ਦਸਤਖਤਾਂ ਲਈ ਤੁਰੰਤ ਗਾਈਡ। ਮਾਸਟਰ ਪਾਸਵਰਡ ਸੈਟ ਕਰੋ। ਸੈਟਿੰਗਾਂ ਵਿੱਚ ਦਸਤਖਤ ਸੰਰਚਿਤ ਕਰੋ। ਸੱਜਾ-ਕਲਿਕ ਨਾਲ ਪਾਓ।",

        'image_guide_title': "ਚਿੱਤਰ ਪਾਓ - ਗਾਈਡ",
        'image_guide_html': """
        📷 <strong>PDF ਵਿੱਚ ਚਿੱਤਰ ਪਾਓ - ਤੁਰੰਤ ਗਾਈਡ</strong><br>
        <ol>
        <li>ਲੋੜੀਂਦੀ ਸਥਿਤੀ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰੋ</li>
        <li><em>„ਚਿੱਤਰ ਪਾਓ“</em> → ਚਿੱਤਰ ਚੁਣੋ</li>
        <li>ਚਿੱਤਰ ਸਥਿਤ ਕਰੋ: ਮਾਊਸ ਨਾਲ ਖਿੱਚੋ</li>
        <li>ਆਕਾਰ ਅਨੁਕੂਲ ਕਰੋ: ਕੋਨਿਆਂ/ਕਿਨਾਰਿਆਂ ਤੇ ਖਿੱਚੋ</li>
        <li>ਪਹਿਲੂ ਅਨੁਪਾਤ ਬਰਕਰਾਰ ਰੱਖੋ: <strong>[A]</strong> ਕੁੰਜੀ</li>
        <li>ਹੋਰ ਅਨੁਕੂਲਤਾਵਾਂ: ਚਿੱਤਰ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰੋ</li>
        </ol>
        <p><strong>ਸੁਝਾਅ:</strong> ਸੰਦਰਭ ਮੀਨੂ ਵਿੱਚ ਤੁਸੀਂ ਸੈਟਿੰਗਾਂ ਨੂੰ ਅਨੁਕੂਲ ਕਰ ਸਕਦੇ ਹੋ।</p>
        """,
        'image_guide_voice': "ਚਿੱਤਰਾਂ ਲਈ ਤੁਰੰਤ ਗਾਈਡ। ਸੱਜਾ-ਕਲਿਕ, ਚਿੱਤਰ ਪਾਓ, ਚੁਣੋ। ਮਾਊਸ ਨਾਲ ਸਥਿਤ ਕਰੋ, ਕੋਨਿਆਂ ਤੇ ਆਕਾਰ ਅਨੁਕੂਲ ਕਰੋ। A ਕੁੰਜੀ ਨਾਲ ਪਹਿਲੂ ਅਨੁਪਾਤ।",

        'form_guide_title': "ਆਕਾਰ ਪਾਓ - ਗਾਈਡ",
        'form_guide_html': """
        📐 <strong>PDF ਵਿੱਚ ਆਕਾਰ ਪਾਓ - ਤੁਰੰਤ ਗਾਈਡ</strong><br>
        <ol>
        <li>ਆਕਾਰ ਕਿਸਮ ਚੁਣੋ (ਆਇਤ, ਅੰਡਾਕਾਰ, ਰੇਖਾ, ਤੀਰ)</li>
        <li>ਸਥਿਤੀ ਤੇ ਕਲਿਕ ਕਰੋ:
            <ul>
            <li>ਆਇਤ/ਅੰਡਾਕਾਰ ਲਈ: ਇੱਕ ਕਲਿਕ ਆਕਾਰ ਰੱਖਦਾ ਹੈ</li>
            <li>ਰੇਖਾ/ਤੀਰ ਲਈ: ਸ਼ੁਰੂ ਅਤੇ ਅੰਤ ਬਿੰਦੂ ਲਈ ਦੋ ਕਲਿਕ</li>
            </ul>
        </li>
        <li>ਆਕਾਰ ਸਥਿਤ ਕਰੋ: ਮਾਊਸ ਨਾਲ ਖਿੱਚੋ</li>
        <li>ਆਕਾਰ ਅਨੁਕੂਲ ਕਰੋ: ਕੋਨਿਆਂ/ਕਿਨਾਰਿਆਂ ਤੇ ਖਿੱਚੋ</li>
        <li>ਆਕਾਰ ਸੇਵ ਕਰੋ: <strong>Enter</strong></li>
        <li>ਆਕਾਰ ਰੱਦ ਕਰੋ: <strong>ESC</strong></li>
        <li>ਹੋਰ ਅਨੁਕੂਲਤਾਵਾਂ: ਆਕਾਰ ਤੇ ਸੱਜਾ-ਕਲਿਕ ਕਰੋ</li>
        </ol>
        <p><strong>ਸੁਝਾਅ:</strong> ਸੰਦਰਭ ਮੀਨੂ ਵਿੱਚ ਤੁਸੀਂ ਸੈਟਿੰਗਾਂ ਨੂੰ ਅਨੁਕੂਲ ਕਰ ਸਕਦੇ ਹੋ।</p>
        """,
        'form_guide_voice': "ਆਕਾਰਾਂ ਲਈ ਤੁਰੰਤ ਗਾਈਡ। ਆਕਾਰ ਕਿਸਮ ਚੁਣੋ। ਆਇਤ ਜਾਂ ਅੰਡਾਕਾਰ ਲਈ ਇੱਕ ਵਾਰ ਕਲਿਕ ਕਰੋ, ਰੇਖਾ ਜਾਂ ਤੀਰ ਲਈ ਦੋ ਵਾਰ। ਮਾਊਸ ਨਾਲ ਸਥਿਤ ਕਰੋ, ਕੋਨਿਆਂ ਤੇ ਆਕਾਰ ਅਨੁਕੂਲ ਕਰੋ। Enter ਨਾਲ ਸੇਵ ਕਰੋ, Escape ਨਾਲ ਰੱਦ ਕਰੋ।",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "ਪਿਛਲਾ",
        "btn_next_result": "ਅਗਲਾ",
        "ocr_text_window": "OCR ਟੈਕਸਟ ਵਿੰਡੋ",
        "bookmark_existing": "ਮੌਜੂਦਾ ਬੁੱਕਮਾਰਕ",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR ਤੁਲਨਾ Mac - Windows",
        'ocr_method_mac_win_title': "Mac ਅਤੇ Windows ਵਿਚਕਾਰ OCR ਅੰਤਰ",
        'ocr_method_mac_win_voice': "Mac ਬਿਹਤਰ ਹੈ",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – macOS ਅਤੇ Windows ਵਿਚਕਾਰ ਅੰਤਰ</strong></p>

        <p><strong>macOS (ਸਿਫਾਰਸ਼ੀ)</strong></p>
        <p>ਟੂਲ:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>ਨਤੀਜਾ:</p>
        <ul>
        <li>ਇੱਕ ਖੋਜਯੋਗ PDF ਜਿਸ ਵਿੱਚ ਏਮਬੈੱਡਡ ਟੈਕਸਟ ਹੈ ਜੋ ਮੂਲ ਲੇਆਉਟ ਨੂੰ ਵੱਡੇ ਪੱਧਰ ਤੇ ਸੁਰੱਖਿਅਤ ਰੱਖਦਾ ਹੈ।</li>
        </ul>
        <p>ਫਾਇਦੇ:</p>
        <ul>
        <li>ਟੈਕਸਟ ਪਛਾਣ ਦੀ ਸ਼ਾਨਦਾਰ ਗੁਣਵੱਤਾ (ਟੇਢੇ ਪੰਨਿਆਂ ਤੇ ਵੀ)।</li>
        <li>ਵੈਕਟਰ ਗ੍ਰਾਫਿਕਸ ਅਤੇ ਫੌਂਟਾਂ ਦੀ ਸੰਭਾਲ।</li>
        <li>ਉਪ-ਪ੍ਰਕਿਰਿਆ ਮੁਲਾਂਕਣ ਰਾਹੀਂ GUI ਤਰੱਕੀ ਬਾਰ।</li>
        <li>ਸਾਰੇ OCR ਮਾਪਦੰਡਾਂ ਤੇ ਪੂਰਾ ਨਿਯੰਤਰਣ (Deskew, Clean, Oversample, ਅਨੁਕੂਲਨ)।</li>
        <li>ਟੈਕਸਟ ਖੋਜ ਮੁੱਖ ਵਿੰਡੋ (PDF ਦ੍ਰਿਸ਼) ਵਿੱਚ ਸਿੱਧੀ ਉਪਲਬਧ ਹੈ।</li>
        </ul>
        <p>ਨੁਕਸਾਨ:</p>
        <ul>
        <li>ਵਾਧੂ ਸਿਸਟਮ ਟੂਲਸ ਦੀ ਲੋੜ ਹੈ (ocrmypdf, Ghostscript, unpaper, pngquant – ਐਪ ਬੰਡਲ ਵਿੱਚ ਸ਼ਾਮਲ)।</li>
        <li>ਗੁੰਝਲਦਾਰ ਗਲਤੀ ਪ੍ਰਬੰਧਨ (ਡੈੱਡਲੌਕ, ਟਾਈਮਆਉਟ)।</li>
        </ul>

        <p><strong>Windows (ਸਥਿਰ ਵਿਕਲਪ)</strong></p>
        <p>ਟੂਲ:</p>
        <ul>
        <li>pytesseract (Tesseract ਨਾਲ ਸਿੱਧਾ ਕੁਨੈਕਸ਼ਨ) + reportlab + PyPDF2</li>
        </ul>
        <p>ਨਤੀਜਾ:</p>
        <ul>
        <li>ਇੱਕ ਖੋਜਯੋਗ PDF ਜੋ ਵਿਜ਼ੂਅਲ ਤੌਰ ਤੇ ਇੱਕ ਚਿੱਤਰ PDF ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੈ, ਪਰ ਪਾਰਦਰਸ਼ੀ ਟੈਕਸਟ ਰਾਹੀਂ ਖੋਜਯੋਗ ਹੈ।</li>
        </ul>
        <p>ਫਾਇਦੇ:</p>
        <ul>
        <li>ਹੁਣ ਕੋਈ ਨਹੀਂ ਸੁਝਦਾ।</li>
        </ul>
        <p>ਨੁਕਸਾਨ:</p>
        <ul>
        <li>PDF ਅਸਲ ਵਿੱਚ ਅਦਿੱਖ ਟੈਕਸਟ ਵਾਲੀ ਇੱਕ ਤਸਵੀਰ ਹੈ; ਗੁੰਝਲਦਾਰ ਦਸਤਾਵੇਜ਼ਾਂ (ਕਾਲਮ, ਸਾਰਣੀਆਂ) ਵਿੱਚ ਲੇਆਉਟ ਥੋੜ੍ਹਾ ਭਟਕ ਸਕਦਾ ਹੈ।</li>
        <li>ਕੋਈ ਆਟੋਮੈਟਿਕ ਟੇਢਾਪਨ ਸੁਧਾਰ (--deskew) ਜਾਂ ਚਿੱਤਰ ਸਫਾਈ (--clean) ਨਹੀਂ ਹੈ।</li>
        <li>GUI ਤਰੱਕੀ ਬਾਰ ਸਿਰਫ ਪ੍ਰੋਸੈਸ ਕੀਤੇ ਪੰਨਿਆਂ ਦੀ ਗਿਣਤੀ ਦੇ ਆਧਾਰ ਤੇ ਮੋਟੇ ਤੌਰ ਤੇ ਅਪਡੇਟ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।</li>
        <li>OCR ਸਪੀਡ ਥੋੜ੍ਹੀ ਹੌਲੀ ਹੈ (ਕਿਉਂਕਿ ਹਰ ਪੰਨਾ ਵੱਖਰੇ ਤੌਰ ਤੇ ਪ੍ਰੋਸੈਸ ਕੀਤਾ ਜਾਂਦਾ ਹੈ)।</li>
        <li>ਟੈਕਸਟ ਖੋਜ ਨੂੰ OCR ਟੈਕਸਟ ਵਿੰਡੋ ਵੱਲ ਰੀਡਾਇਰੈਕਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।</li>
        </ul>

        <p><strong>ਸਾਂਝੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ</strong></p>
        <ul>
        <li>ਦੋਵੇਂ ਵਿਧੀਆਂ ਸਰੋਤ ਫਾਈਲ ਵਾਂਗ ਉਸੇ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ ਖੋਜਯੋਗ PDF ਬਣਾਉਂਦੀਆਂ ਹਨ।</li>
        <li>OCR ਸੈਟਿੰਗਾਂ (ਭਾਸ਼ਾ, DPI, ਪੰਨਾ-ਸੈਗਮੈਂਟੇਸ਼ਨ ਮੋਡ, OCR ਇੰਜਣ ਮੋਡ) ਨੂੰ OCRSettingsDialog ਰਾਹੀਂ ਸੰਰਚਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ ਅਤੇ ਦੋਵੇਂ ਲਾਗੂਕਰਨਾਂ ਵਿੱਚ ਪ੍ਰਭਾਵੀ ਹੁੰਦੀਆਂ ਹਨ।</li>
        </ul>

        <p><strong>ਸਿਫਾਰਸ਼:</strong></p>
        <ul>
        <li>macOS: ocrmypdf ਬਾਈਨਰੀ ਸਭ ਤੋਂ ਵਧੀਆ ਨਤੀਜੇ ਦਿੰਦੀ ਹੈ – ਇੱਕ Mac ਖਰੀਦੋ ਅਤੇ ਵਰਜਨ ਦੀ ਵਰਤੋਂ ਕਰੋ (Apple Silicon ਜਾਂ Intel ਚਿੱਪ ਵਾਲੇ Mac ਲਈ PDFDarkView)। Windows ਨਾਲੋਂ OCR ਨਤੀਜੇ ਬਿਹਤਰ ਹਨ!</li>
        <li>Windows: pytesseract ਹੱਲ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇਹ ਸਥਿਰ ਹੈ ਅਤੇ ਜ਼ਿਆਦਾਤਰ ਦਸਤਾਵੇਜ਼ਾਂ ਲਈ ਪੂਰੀ ਤਰ੍ਹਾਂ ਕਾਫੀ ਗੁਣਵੱਤਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।</li>
        </ul>

        <p><strong>ਮਹੱਤਵਪੂਰਨ ਨੋਟ:</strong></p>
        <ul>
        <li>ਦੋਵੇਂ ਵਰਜਨ ਪੂਰੀ ਤਰ੍ਹਾਂ ਉਪਭੋਗਤਾ ਇੰਟਰਫੇਸ ਵਿੱਚ ਏਕੀਕ੍ਰਿਤ ਹਨ – ਉਪਭੋਗਤਾ ਕੋਈ ਅੰਤਰ ਮਹਿਸੂਸ ਨਹੀਂ ਕਰਦਾ।</li>
        <li>ਪ੍ਰੋਗਰਾਮ ਆਪਰੇਟਿੰਗ ਸਿਸਟਮ ਦੇ ਆਧਾਰ ਤੇ ਆਪਣੇ ਆਪ ਫੈਸਲਾ ਕਰਦਾ ਹੈ ਕਿ ਕਿਸ OCR ਇੰਜਣ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਹੈ।</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "ਦਸਤਖਤ ਬਣਾਓ (ਸਕੈਨ ਤੋਂ)",
        "signature_create_title": "ਸਕੈਨ ਕੀਤਾ ਦਸਤਖਤ ਚੁਣੋ (PDF/ਚਿੱਤਰ)",
        "image_pdf_filter": "ਚਿੱਤਰ ਅਤੇ PDF",
        "signature_pdf_empty": "PDF ਵਿੱਚ ਕੋਈ ਪੰਨੇ ਨਹੀਂ ਹਨ।",
        "signature_created_success": "ਦਸਤਖਤ ਸਫਲਤਾਪੂਰਵਕ ਬਣਾਇਆ ਗਿਆ: {0}",
        "signature_create_error": "ਦਸਤਖਤ ਬਣਾਉਂਦੇ ਸਮੇਂ ਗਲਤੀ:\n{0}",
        "rembg_missing": "rembg ਸਥਾਪਿਤ ਨਹੀਂ ਹੈ।\nਕਿਰਪਾ ਕਰਕੇ ਸਥਾਪਿਤ ਕਰੋ: pip install rembg\nਗਲਤੀ: {0}",
        "signature_name_title": "ਦਸਤਖਤ ਲਈ ਫਾਈਲ ਨਾਮ",
        "signature_name_message": "ਕਿਰਪਾ ਕਰਕੇ ਨਵੇਂ ਦਸਤਖਤ ਲਈ ਫਾਈਲ ਨਾਮ ਦਾਖਲ ਕਰੋ (ਪਾਰਦਰਸ਼ੀ ਪਿਛੋਕੜ ਦੇ ਨਾਲ PNG ਵਜੋਂ ਸੇਵ ਕੀਤਾ ਜਾਵੇਗਾ):",
        "signature_name_label": "ਫਾਈਲ ਨਾਮ:",
        "signature_name_voice": "ਦਸਤਖਤ ਲਈ ਫਾਈਲ ਨਾਮ ਦਾਖਲ ਕਰੋ",
        "signature_processing": "ਪ੍ਰੋਸੈਸਿੰਗ ਚੱਲ ਰਹੀ ਹੈ...",
        "signature_creation_title": "ਦਸਤਖਤ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ",
        "signature_overwrite_warning": "ਫਾਈਲ '{0}' ਪਹਿਲਾਂ ਤੋਂ ਮੌਜੂਦ ਹੈ। ਓਵਰਰਾਈਟ ਕਰਨਾ ਹੈ?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"ਦਸਤਖਤ ਲਈ PDF ਤਿਆਰ ਕਰੋ",
        "signature_prepare_instruction":"ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ PDF ਚੁਣੋ ਜਿਸ ਵਿੱਚ ਇੱਕ ਸਿੰਗਲ ਪੰਨੇ ਤੇ ਸਕੈਨ ਕੀਤਾ ਦਸਤਖਤ ਹੋਵੇ।\n\nਅਨੁਕੂਲ ਪਛਾਣ ਲਈ ਯਕੀਨੀ ਬਣਾਓ:\n• ਦਸਤਖਤ ਚਿੱਟੇ ਕਾਗਜ਼ ਤੇ ਕਾਲੀ ਸਿਆਹੀ (ਬਾਲਪੁਆਇੰਟ ਜਾਂ ਫਾਈਨਲਾਈਨਰ) ਨਾਲ ਲਿਖਿਆ ਹੋਵੇ।\n• ਦਸਤਖਤ ਬਾਕੀ ਖਾਲੀ A4 ਪੰਨੇ ਦੇ ਉਪਰਲੇ ਤੀਜੇ ਹਿੱਸੇ ਵਿੱਚ ਹੋਵੇ।\n• PDF ਨੂੰ ਘੱਟੋ-ਘੱਟ 300 dpi ਤੇ ਸਕੈਨ ਕੀਤਾ ਗਿਆ ਹੋਵੇ।\n• ਦਸਤਖਤ ਸਪੱਸ਼ਟ ਅਤੇ ਬਹੁਤ ਪਤਲਾ ਨਾ ਹੋਵੇ।\n• ਕੋਈ ਪਰੇਸ਼ਾਨ ਕਰਨ ਵਾਲੇ ਪਿਛੋਕੜ ਪੈਟਰਨ ਜਾਂ ਲਕੀਰਾਂ ਮੌਜੂਦ ਨਾ ਹੋਣ।",
        "signature_prepare_voice":"ਕਿਰਪਾ ਕਰਕੇ ਸਕੈਨ ਕੀਤੇ ਦਸਤਖਤ ਵਾਲੀ PDF ਚੁਣੋ। ਚੰਗੀ ਗੁਣਵੱਤਾ ਅਤੇ ਕੰਟਰਾਸਟ ਵੱਲ ਧਿਆਨ ਦਿਓ।",
        "sig_thickness_label":"ਲਕੀਰ ਦੀ ਮੋਟਾਈ:",
        "sig_thickness_normal":"ਸਧਾਰਨ (ਪਤਲੀ)",
        "sig_thickness_bold":"ਬੋਲਡ (ਸਿਫਾਰਸ਼ੀ)",
        "sig_thickness_very_bold":"ਬਹੁਤ ਬੋਲਡ",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI ਅਤੇ OCR ਭਾਸ਼ਾਵਾਂ ਸ਼ਾਮਲ ਕਰੋ - ਗਾਈਡ",
        'language_guide_title': "GUI ਅਤੇ OCR ਭਾਸ਼ਾਵਾਂ ਸ਼ਾਮਲ ਕਰੋ",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>ਲੋੜੀਂਦੀ ਅਨੁਵਾਦ ਫਾਈਲ <code>translations_xy.py</code> ਨੂੰ ਇੱਥੋਂ ਡਾਊਨਲੋਡ ਕਰੋ<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        ਅਤੇ ਹੇਠ ਲਿਖੀ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਰੱਖੋ:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>ਆਪਣਾ ਵੈੱਬ ਬ੍ਰਾਊਜ਼ਰ ਖੋਲ੍ਹੋ।</li>
        <li>ਇਸ ਤੇ ਜਾਓ: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>ਸਕ੍ਰੀਨ ਦੇ ਸੱਜੇ ਕਿਨਾਰੇ ਤੇ "Releases" ਲੱਭੋ ਅਤੇ <strong>"latest"</strong> ਨਾਲ ਚਿੰਨ੍ਹਿਤ ਚੁਣੋ।</li>
        <li>ਅਗਲੇ ਰੀਲੀਜ਼ ਪੰਨੇ ਤੇ, ਸਭ ਤੋਂ ਹੇਠਾਂ <code>Source Code.zip</code> ਫਾਈਲ ਡਾਊਨਲੋਡ ਕਰੋ।</li>
        <li>ZIP ਫਾਈਲ ਨੂੰ ਅਨਜ਼ਿਪ ਕਰੋ।</li>
        <li>ਅਨਜ਼ਿਪ ਕੀਤੇ ਫੋਲਡਰ ਵਿੱਚ ਉਹ ਸਾਰੀਆਂ ਭਾਸ਼ਾ ਫਾਈਲਾਂ ਲੱਭੋ ਜਿਨ੍ਹਾਂ ਦੀ ਤੁਹਾਨੂੰ ਲੋੜ ਹੈ, ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਕਾਪੀ ਕਰੋ:<br/>
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
        "menu_watermark":"ਵਾਟਰਮਾਰਕ ਪਾਓ",
        "fullpage_text_watermark_title":"ਟੈਕਸਟ ਵਾਟਰਮਾਰਕ ਵਜੋਂ",
        "fullpage_image_watermark_title":"ਚਿੱਤਰ ਵਾਟਰਮਾਰਕ ਵਜੋਂ",
        "filename_with_watermark":"_ਵਾਟਰਮਾਰਕ_ਸਹਿਤ",
        "watermark_text":"ਟੈਕਸਟ:",
        "watermark_text_placeholder":"ਤੁਹਾਡਾ ਵਾਟਰਮਾਰਕ ਟੈਕਸਟ...",
        "watermark_font_family":"ਫੌਂਟ:",
        "watermark_font_size":"ਫੌਂਟ ਆਕਾਰ:",
        "watermark_format":"ਫਾਰਮੈਟਿੰਗ:",
        "watermark_bold":"ਮੋਟਾ",
        "watermark_italic":"ਤਿਰਛਾ",
        "watermark_color":"ਰੰਗ:",
        "watermark_choose_color":"ਰੰਗ ਚੁਣੋ...",
        "watermark_opacity":"ਅਪਾਰਦਰਸ਼ਤਾ / ਪਾਰਦਰਸ਼ਤਾ:",
        "watermark_direction":"ਪੜ੍ਹਨ ਦੀ ਦਿਸ਼ਾ:",
        "watermark_direction_l_r":"ਖੱਬੇ → ਸੱਜੇ",
        "watermark_direction_bl_tr":"ਹੇਠਾਂ ਖੱਬੇ → ਉੱਪਰ ਸੱਜੇ",
        "watermark_direction_tl_br":"ਉੱਪਰ ਖੱਬੇ → ਹੇਠਾਂ",
        "watermark_direction_b_t":"ਹੇਠਾਂ → ਉੱਪਰ",
        "watermark_direction_t_b":"ਉੱਪਰ → ਹੇਠਾਂ",
        "watermark_preview":"ਪੂਰਵ-ਦ੍ਰਿਸ਼:",
        "watermark_preview_sample":"ਨਮੂਨਾ ਟੈਕਸਟ",
        "watermark_empty_text":"ਕਿਰਪਾ ਕਰਕੇ ਟੈਕਸਟ ਦਾਖਲ ਕਰੋ।",
        "watermark_applied":"ਵਾਟਰਮਾਰਕ ਸਾਰੇ ਪੰਨਿਆਂ ਤੇ ਲਾਗੂ ਕੀਤਾ ਗਿਆ ਹੈ।",
        "watermark_saved":"ਵਾਟਰਮਾਰਕ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ।",
        "image_scale":"ਆਕਾਰ:",
        "image_preview":"ਚਿੱਤਰ ਪੂਰਵ-ਦ੍ਰਿਸ਼:",
        "no_image_selected":"ਕੋਈ ਚਿੱਤਰ ਚੁਣਿਆ ਨਹੀਂ ਗਿਆ",
        "browse":"ਬਰਾਊਜ਼ ਕਰੋ...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "ਰੀਡੈਕਸ਼ਨਾਂ",
        "redact_add_black":"ਰੀਡੈਕਸ਼ਨ (ਕਾਲਾ)",
        "redact_add_white":"ਰੀਡੈਕਸ਼ਨ (ਚਿੱਟਾ / ਮਿਟਾਓ)",
        "redact_added_black":"ਕਾਲੀ ਰੀਡੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕੀਤੀ ਗਈ",
        "redact_added_white":"ਚਿੱਟੀ ਰੀਡੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕੀਤੀ ਗਈ",
        "redact_apply_all":"ਸਾਰੀਆਂ ਰੀਡੈਕਸ਼ਨਾਂ ਲਾਗੂ ਕਰੋ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕਰੋ",
        "redact_discard_all":"ਸਾਰੀਆਂ ਰੀਡੈਕਸ਼ਨਾਂ ਰੱਦ ਕਰੋ",
        "redact_discard":"ਇਸ ਰੀਡੈਕਸ਼ਨ ਨੂੰ ਰੱਦ ਕਰੋ",
        "no_redactions":"ਕੋਈ ਰੀਡੈਕਸ਼ਨਾਂ ਨਹੀਂ",
        "redact_confirm_title":"ਰੀਡੈਕਸ਼ਨਾਂ ਨੂੰ ਸਥਾਈ ਤੌਰ ਤੇ ਲਾਗੂ ਕਰੋ",
        "redact_confirm_message":"ਚੇਤਾਵਨੀ: ਚਿੰਨ੍ਹਿਤ ਖੇਤਰਾਂ ਨੂੰ ਸਥਾਈ ਤੌਰ ਤੇ ਮਿਟਾ ਦਿੱਤਾ ਜਾਵੇਗਾ (ਕਾਲਾ ਜਾਂ ਚਿੱਟਾ)।\nਬੈਕਅੱਪ ਬਣਾਇਆ ਜਾਵੇਗਾ (ਜੇਕਰ ਸਮਰੱਥ ਕੀਤਾ ਗਿਆ ਹੋਵੇ)।\n\nਜਾਰੀ ਰੱਖਣਾ ਹੈ?",
        "redact_apply":"ਹਾਂ, ਹੁਣੇ ਰੀਡੈਕਟ ਕਰੋ",
        "redact_saved":"{0} ਰੀਡੈਕਸ਼ਨ(ਆਂ) ਨੂੰ ਸਫਲਤਾਪੂਰਵਕ ਲਾਗੂ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ।",
        "redact_saved_voice":"{0} ਰੀਡੈਕਸ਼ਨ(ਆਂ) ਲਾਗੂ ਕੀਤੀਆਂ ਗਈਆਂ",
        "redact_error":"ਰੀਡੈਕਸ਼ਨ ਦੌਰਾਨ ਗਲਤੀ",
        "filename_redacted":"_ਰੀਡੈਕਟ_ਕੀਤਾ",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'ਪੰਨਾ ਨੰਬਰ ਪਾਓ',
        'page_numbers_format': 'ਨੰਬਰ ਫਾਰਮੈਟ:',
        'page_numbers_format_arabic': '1, 2, 3 ... (ਅਰਬੀ)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (ਰੋਮਨ ਛੋਟੇ)',
        'page_numbers_format_roman_upper': 'I, II, III ... (ਰੋਮਨ ਵੱਡੇ)',
        'page_numbers_format_letter': 'A, B, C ... (ਅੱਖਰ)',
        'page_numbers_format_custom': 'ਕਸਟਮ',
        'page_numbers_custom_pattern': 'ਪੈਟਰਨ:',
        'page_numbers_custom_placeholder': 'ਜਿਵੇਂ "ਪੰਨਾ {nummer}" ਜਾਂ "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'ਮੌਜੂਦਾ ਪੰਨਾ ਨੰਬਰ ਲਈ {nummer} ਅਤੇ ਕੁੱਲ ਲਈ {total} ਵਰਤੋਂ',
        'page_numbers_position': 'ਸਥਿਤੀ:',
        'page_numbers_pos_tl': 'ਉੱਪਰ ਖੱਬੇ',
        'page_numbers_pos_tc': 'ਉੱਪਰ ਕੇਂਦਰ',
        'page_numbers_pos_tr': 'ਉੱਪਰ ਸੱਜੇ',
        'page_numbers_pos_ml': 'ਵਿਚਕਾਰ ਖੱਬੇ',
        'page_numbers_pos_mc': 'ਕੇਂਦਰਿਤ',
        'page_numbers_pos_mr': 'ਵਿਚਕਾਰ ਸੱਜੇ',
        'page_numbers_pos_bl': 'ਹੇਠਾਂ ਖੱਬੇ',
        'page_numbers_pos_bc': 'ਹੇਠਾਂ ਕੇਂਦਰ',
        'page_numbers_pos_br': 'ਹੇਠਾਂ ਸੱਜੇ',
        'page_numbers_margins': 'ਮਾਰਜਿਨ:',
        'page_numbers_margin_x': 'ਖਿਤਿਜੀ ਦੂਰੀ:',
        'page_numbers_margin_y': 'ਲੰਬਕਾਰੀ ਦੂਰੀ:',
        'page_numbers_range': 'ਪੰਨਾ ਰੇਂਜ:',
        'page_numbers_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'page_numbers_custom_range': 'ਕਸਟਮ ਰੇਂਜ',
        'page_numbers_from': 'ਤੋਂ:',
        'page_numbers_to': 'ਤੱਕ:',
        'page_numbers_progress': 'ਪੰਨਾ ਨੰਬਰ ਪਾਏ ਜਾ ਰਹੇ ਹਨ...',
        'page_numbers_start': 'ਪੰਨਾ ਨੰਬਰ ਪਾਉਣਾ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'page_numbers_cancel': 'ਪੰਨਾ ਨੰਬਰ ਪਾਉਣਾ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'page_numbers_success': 'ਪੰਨਾ ਨੰਬਰ ਸਫਲਤਾਪੂਰਵਕ ਜੋੜੇ ਗਏ।\n\nਕੀ ਤੁਸੀਂ ਨਵਾਂ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?\n\n{0}',
        'page_numbers_complete': 'ਪੰਨਾ ਨੰਬਰ ਜੋੜੇ ਗਏ',
        'page_numbers_error_format': 'ਪੰਨਾ ਨੰਬਰ ਪਾਉਂਦੇ ਸਮੇਂ ਗਲਤੀ: {0}',
        'page_numbers_content_type': 'ਸਮੱਗਰੀ ਕਿਸਮ:',
        'page_numbers_tab_simple': 'ਸਧਾਰਨ ਨੰਬਰ',
        'page_numbers_tab_range': 'ਪੰਨਾ X ਦਾ Y',
        'page_numbers_tab_date': 'ਤਾਰੀਖ',
        'page_numbers_tab_custom': 'ਖੁੱਲ੍ਹਾ ਟੈਕਸਟ',
        'page_numbers_range_format': 'ਫਾਰਮੈਟ:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'ਪੰਨਾ {aktuell} ਦਾ {gesamt}',
        'page_numbers_range_custom': 'ਕਸਟਮ',
        'page_numbers_range_placeholder': 'ਜਿਵੇਂ "ਪੰਨਾ {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'ਤਾਰੀਖ ਫਾਰਮੈਟ:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 ਜਨਵਰੀ 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'ਕਸਟਮ',
        'page_numbers_date_placeholder': 'ਜਿਵੇਂ %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'ਸਥਿਤੀ:',
        'page_numbers_date_before': 'ਪੰਨਾ ਨੰਬਰ ਤੋਂ ਪਹਿਲਾਂ ਤਾਰੀਖ',
        'page_numbers_date_after': 'ਪੰਨਾ ਨੰਬਰ ਤੋਂ ਬਾਅਦ ਤਾਰੀਖ',
        'page_numbers_date_only': 'ਸਿਰਫ਼ ਤਾਰੀਖ (ਪੰਨਾ ਨੰਬਰ ਤੋਂ ਬਿਨਾਂ)',
        'page_numbers_custom_text': 'ਕਸਟਮ ਟੈਕਸਟ:',
        'page_numbers_custom_placeholder_text': 'ਪੰਨਾ ਨੰਬਰ ਲਈ {seite} ਅਤੇ ਕੁੱਲ ਲਈ {gesamt} ਵਰਤੋਂ\nਜਿਵੇਂ "ਗੁਪਤ - ਪੰਨਾ {seite}" ਜਾਂ "{seite} ਦਾ {gesamt}"',
        "filename_with_page_number":"_ਪੰਨਾ_ਨੰਬਰ_ਸਹਿਤ",
        "filename_with_page_declaration":"_ਪੰਨਾ_ਘੋਸ਼ਣਾ_ਸਹਿਤ",
        "filename_with_pagenumber":"_ਪੰਨਾ_ਨੰਬਰ_ਸਹਿਤ",
        "filename_with_date":"_ਤਾਰੀਖ_ਸਹਿਤ",
        "filename_with_my_page_declaration":"_ਕਸਟਮ_ਪੰਨਾ_ਘੋਸ਼ਣਾ_ਸਹਿਤ",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "ਸੁਰੱਖਿਅਤ ਨਾ ਕੀਤੀਆਂ ਗਈਆਂ ਤਬਦੀਲੀਆਂ",
        "unsaved_changes_message_darkmode": "ਬਿਨਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤੇ ਪਾਉਣੇ ਮੌਜੂਦ ਹਨ।\nਸਵਿਚ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਕੀ ਤੁਸੀਂ ਉਹਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?",
        "save_and_switch": "ਸੁਰੱਖਿਅਤ ਕਰੋ ਅਤੇ ਸਵਿਚ ਕਰੋ",
        "discard_and_switch": "ਹੁਣੇ ਸਵਿਚ ਕਰੋ",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'ਪੰਨਿਆਂ ਨੂੰ ਚਿੱਤਰਾਂ ਵਜੋਂ ਨਿਰਯਾਤ ਕਰੋ',
        'export_images_menu': 'ਚਿੱਤਰਾਂ ਵਜੋਂ ਨਿਰਯਾਤ ਕਰੋ (PNG/JPEG)',
        'export_images_format': 'ਚਿੱਤਰ ਫਾਰਮੈਟ:',
        'export_images_dpi': 'ਰੈਜ਼ੋਲਿਊਸ਼ਨ (DPI):',
        'export_images_quality': 'JPEG ਗੁਣਵੱਤਾ:',
        'export_images_range': 'ਪੰਨਾ ਰੇਂਜ:',
        'export_images_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'export_images_custom_range': 'ਕਸਟਮ ਰੇਂਜ',
        'export_images_from': 'ਤੋਂ:',
        'export_images_to': 'ਤੱਕ:',
        'export_images_options': 'ਵਿਕਲਪ:',
        'export_images_single_files': 'ਹਰੇਕ ਪੰਨਾ ਵੱਖਰੀ ਫਾਈਲ ਵਜੋਂ',
        'export_images_subfolder': 'ਉਪ-ਫੋਲਡਰ ਵਿੱਚ ਨਿਰਯਾਤ ਕਰੋ',
        'export_images_subfolder_info': '"PDFਨਾਂ_ਚਿੱਤਰ" ਉਪ-ਫੋਲਡਰ ਵਿੱਚ',
        'export_images_same_folder': 'PDF ਵਾਲੀ ਫੋਲਡਰ ਵਿੱਚ ਹੀ',
        'export_images_apply_darkmode': 'PDFDarkView ਸੈਟਿੰਗਾਂ ਲਾਗੂ ਕਰੋ (ਡਾਰਕ ਮੋਡ)',
        'export_images_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'export_images_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'export_images_preview': 'ਪੂਰਵ-ਦ੍ਰਿਸ਼:',
        'export_images_preview_info': 'ਨਿਰਯਾਤ ਲਈ ਸੈਟਿੰਗਾਂ ਚੁਣੋ',
        'export_images_preview_info_detail': '{0} ਪੰਨੇ {1} ਵਜੋਂ\nਰੈਜ਼ੋਲਿਊਸ਼ਨ: {2} DPI\nਫਾਈਲਨਾਂ: {3}\n{4}',
        'export_images_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'export_images_start': 'ਚਿੱਤਰ ਨਿਰਯਾਤ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'export_images_progress': 'ਚਿੱਤਰ ਨਿਰਯਾਤ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ...',
        'export_images_saving': 'ਪੰਨਾ {0} ਦਾ {1} ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'export_images_success': 'ਨਿਰਯਾਤ ਸਫਲ ਰਿਹਾ!\n\n{0} ਚਿੱਤਰ ਇੱਥੇ ਸੁਰੱਖਿਅਤ ਕੀਤੇ ਗਏ:\n{1}',
        'export_images_complete': 'ਚਿੱਤਰ ਨਿਰਯਾਤ ਪੂਰਾ ਹੋਇਆ',
        'export_images_open_folder': '📁 ਫੋਲਡਰ ਖੋਲ੍ਹੋ',
        'export_images_cancel': 'ਚਿੱਤਰ ਨਿਰਯਾਤ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'export_images_error_format': 'ਚਿੱਤਰ ਨਿਰਯਾਤ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ: {0}',
        'export_images_pdf2image_missing': '"pdf2image" ਲਾਇਬ੍ਰੇਰੀ ਸਥਾਪਿਤ ਨਹੀਂ ਹੈ।\n\nਕਿਰਪਾ ਕਰਕੇ ਇਸ ਨਾਲ ਸਥਾਪਿਤ ਕਰੋ:\npip install pdf2image\n\nWindows ਲਈ ਤੁਹਾਨੂੰ Poppler ਦੀ ਵੀ ਲੋੜ ਹੈ:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'ਲੰਬੇ ਸਮੇਂ ਦੀ ਆਰਕਾਈਵਿੰਗ ਲਈ PDF/A ਪਰਿਵਰਤਨ',
        'pdfa_menu': 'PDF/A ਪਰਿਵਰਤਨ (ਆਰਕਾਈਵ-ਯੋਗ)',
        'pdfa_info': 'PDF ਨੂੰ PDF/A ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਦਾ ਹੈ।\n\nPDF/A ਨੂੰ ਖਾਸ ਤੌਰ ਤੇ ਲੰਬੇ ਸਮੇਂ ਦੀ ਆਰਕਾਈਵਿੰਗ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਦਸਤਾਵੇਜ਼ ਭਵਿੱਖ ਵਿੱਚ ਸਹੀ ਢੰਗ ਨਾਲ ਪ੍ਰਦਰਸ਼ਿਤ ਹੋਵੇ।',
        'pdfa_standard': 'PDF/A ਮਿਆਰ:',
        'pdfa_standard_select': 'ਵਰਜਨ:',
        'pdfa_1': 'PDF/A-1 (ਸਧਾਰਨ, ਵਿਆਪਕ ਤੌਰ ਤੇ ਅਨੁਕੂਲ)',
        'pdfa_2': 'PDF/A-2 (ਆਧੁਨਿਕ, ਬਿਹਤਰ ਕੰਪਰੈਸ਼ਨ)',
        'pdfa_3': 'PDF/A-3 (ਨਵੀਨਤਮ ਵਰਜਨ, ਅਟੈਚਮੈਂਟਾਂ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ)',
        'pdfa_standards_explanation': '📖 ਮਿਆਰਾਂ ਦੀ ਵਿਆਖਿਆ:\n\n'
            '• PDF/A-1: ਬੁਨਿਆਦੀ, ਪੁਰਾਣੇ ਸਿਸਟਮਾਂ ਨਾਲ ਅਨੁਕੂਲ (ਲਗਭਗ 2005)\n'
            '• PDF/A-2: ਵਧੇਰੇ ਆਧੁਨਿਕ, ਬਿਹਤਰ ਕੰਪਰੈਸ਼ਨ, ਪਾਰਦਰਸ਼ਤਾ ਸਹਾਇਤਾ (ਲਗਭਗ 2011)\n'
            '• PDF/A-3: ਨਵੀਨਤਮ ਵਰਜਨ, ਫਾਈਲ ਅਟੈਚਮੈਂਟਾਂ ਨੂੰ ਐਂਬੈਡ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ (ਲਗਭਗ 2013)\n\n'
            'ਸਿਫ਼ਾਰਸ਼: PDF/A-2 ਅਨੁਕੂਲਤਾ ਅਤੇ ਆਧੁਨਿਕ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿਚਕਾਰ ਇੱਕ ਚੰਗਾ ਸਮਝੌਤਾ ਹੈ।',
        'pdfa_options': 'ਵਿਕਲਪ:',
        'pdfa_compress_enable': 'PDF ਕੰਪਰੈੱਸ ਕਰੋ (ਛੋਟੀ ਫਾਈਲ)',
        'pdfa_metadata_preserve': 'ਮੈਟਾਡੇਟਾ ਸੁਰੱਖਿਅਤ ਰੱਖੋ (ਸਿਰਲੇਖ, ਲੇਖਕ, ਆਦਿ)',
        'pdfa_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'pdfa_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'pdfa_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'pdfa_ocr_info_unknown': '🔍 ਟੈਕਸਟ ਸਮੱਗਰੀ ਦੀ ਜਾਂਚ ਨਹੀਂ ਕਰ ਸਕਿਆ।',
        'pdfa_ocr_info_not_needed': '✅ ਟੈਕਸਟ ਉਪਲਬਧ ਹੈ - OCR ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ।\nPDF/A ਸਿੱਧਾ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।',
        'pdfa_ocr_info_recommended': '⚠️ ਕਾਫ਼ੀ ਟੈਕਸਟ ਨਹੀਂ ਮਿਲਿਆ।\n\nਖੋਜਯੋਗ PDF ਲਈ ਅਸੀਂ ਪਹਿਲਾਂ OCR ਚਲਾਉਣ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕਰਦੇ ਹਾਂ।\nਨੋਟ: PDF/A OCR ਤੋਂ ਬਿਨਾਂ ਵੀ ਕੰਮ ਕਰਦਾ ਹੈ - ਪਰ ਟੈਕਸਟ ਖੋਜਯੋਗ ਨਹੀਂ ਹੋਵੇਗਾ।',
        'pdfa_ocr_info_error': '❌ ਜਾਂਚ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ: {0}',
        'pdfa_start': 'PDF/A ਪਰਿਵਰਤਨ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'pdfa_progress': 'PDF/A ਪਰਿਵਰਤਨ ਜਾਰੀ ਹੈ...',
        'pdfa_success': 'PDF/A ਪਰਿਵਰਤਨ ਸਫਲ ਰਿਹਾ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਕੀ ਤੁਸੀਂ ਨਵਾਂ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'pdfa_complete': 'PDF/A ਪਰਿਵਰਤਨ ਪੂਰਾ ਹੋਇਆ',
        'pdfa_cancel': 'PDF/A ਪਰਿਵਰਤਨ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'pdfa_error_format': 'PDF/A ਪਰਿਵਰਤਨ ਦੌਰਾਨ ਗਲਤੀ:\n\n{0}',
        'pdfa_ocrmypdf_missing': '"ocrmypdf" ਲਾਇਬ੍ਰੇਰੀ ਸਥਾਪਿਤ ਨਹੀਂ ਹੈ।\n\nਕਿਰਪਾ ਕਰਕੇ ਇਸ ਨਾਲ ਸਥਾਪਿਤ ਕਰੋ:\npip install ocrmypdf',
        'btn_convert': 'ਬਦਲੋ',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF ਅਨੁਕੂਲ ਬਣਾਓ (ਫਾਈਲ ਆਕਾਰ ਘਟਾਓ)',
        'optimize_menu': 'PDF ਅਨੁਕੂਲ ਬਣਾਓ (ਫਾਈਲ ਆਕਾਰ)',
        'optimize_info': 'ਵੱਖ-ਵੱਖ ਅਨੁਕੂਲਤਾ ਵਿਧੀਆਂ ਰਾਹੀਂ PDF ਫਾਈਲ ਦਾ ਆਕਾਰ ਘਟਾਉਂਦਾ ਹੈ।\n\nਕੰਪਰੈਸ਼ਨ ਪੱਧਰ ਜਿੰਨਾ ਉੱਚਾ, ਫਾਈਲ ਓਨੀ ਛੋਟੀ - ਚਿੱਤਰਾਂ ਵਿੱਚ ਸੰਭਾਵੀ ਗੁਣਵੱਤਾ ਦੇ ਨੁਕਸਾਨ ਨਾਲ।',
        'optimize_level': 'ਕੰਪਰੈਸ਼ਨ ਪੱਧਰ:',
        'optimize_level_low': 'ਘੱਟ (ਤੇਜ਼, ਘੱਟ ਬਚਤ)',
        'optimize_level_medium': 'ਦਰਮਿਆਨੀ (ਚੰਗਾ ਸਮਝੌਤਾ)',
        'optimize_level_high': 'ਉੱਚਾ (ਵੱਡੀ ਬਚਤ)',
        'optimize_level_maximum': 'ਵੱਧ ਤੋਂ ਵੱਧ (ਵੱਧ ਤੋਂ ਵੱਧ ਬਚਤ, ਹੌਲੀ)',
        'optimize_level_explanation': 'ਸਿਫ਼ਾਰਸ਼: "ਦਰਮਿਆਨੀ" ਗਤੀ ਅਤੇ ਫਾਈਲ ਆਕਾਰ ਵਿਚਕਾਰ ਇੱਕ ਚੰਗਾ ਸਮਝੌਤਾ ਹੈ।',
        'optimize_options': 'ਵਿਕਲਪ:',
        'optimize_compress_images': 'ਚਿੱਤਰ ਕੰਪਰੈੱਸ ਕਰੋ (JPEG ਗੁਣਵੱਤਾ ਘਟਾਓ)',
        'optimize_clean_objects': 'ਬੇਕਾਰ ਵਸਤੂਆਂ ਹਟਾਓ',
        'optimize_preserve_metadata': 'ਮੈਟਾਡੇਟਾ ਸੁਰੱਖਿਅਤ ਰੱਖੋ (ਸਿਰਲੇਖ, ਲੇਖਕ, ਆਦਿ)',
        'optimize_image_quality': 'ਚਿੱਤਰ ਗੁਣਵੱਤਾ:',
        'optimize_range': 'ਪੰਨਾ ਰੇਂਜ:',
        'optimize_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'optimize_custom_range': 'ਕਸਟਮ ਰੇਂਜ',
        'optimize_from': 'ਤੋਂ:',
        'optimize_to': 'ਤੱਕ:',
        'optimize_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'optimize_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'optimize_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'optimize_info_box': 'ਜਾਣਕਾਰੀ',
        'optimize_info_text': 'ਵੱਡੇ PDF ਲਈ ਅਨੁਕੂਲਤਾ ਵਿੱਚ ਕੁਝ ਮਿੰਟ ਲੱਗ ਸਕਦੇ ਹਨ।\n\nਚਿੱਤਰਾਂ ਨੂੰ ਘਟਾਈ ਗੁਣਵੱਤਾ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ, ਜੋ ਫਾਈਲ ਆਕਾਰ ਨੂੰ ਮਹੱਤਵਪੂਰਨ ਤੌਰ ਤੇ ਘਟਾ ਸਕਦਾ ਹੈ।',
        'optimize_start': 'PDF ਅਨੁਕੂਲਤਾ ਸ਼ੁਰੂ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ...',
        'optimize_progress': 'PDF ਅਨੁਕੂਲ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ...',
        'optimize_cancel': 'PDF ਅਨੁਕੂਲਤਾ ਰੱਦ ਕੀਤੀ ਗਈ',
        'optimize_complete': 'PDF ਅਨੁਕੂਲਤਾ ਪੂਰੀ ਹੋਈ',
        'optimize_error_format': 'PDF ਅਨੁਕੂਲਤਾ ਦੌਰਾਨ ਗਲਤੀ:\n\n{0}',
        'optimize_success_message': 'PDF ਅਨੁਕੂਲਤਾ ਸਫਲ ਰਹੀ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਪਹਿਲਾਂ: {1}\nਬਾਅਦ: {2}\nਬਚਤ: {3:.1f}%\n\n{4}\n\nਕੀ ਤੁਸੀਂ ਅਨੁਕੂਲਿਤ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'optimize_success_message_no_size': 'PDF ਅਨੁਕੂਲਤਾ ਸਫਲ ਰਹੀ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਆਕਾਰ ਦੀ ਜਾਣਕਾਰੀ ਉਪਲਬਧ ਨਹੀਂ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਅਨੁਕੂਲਿਤ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'optimize_result_positive': 'ਫਾਈਲ {0:.1f}% ਘਟਾਈ ਗਈ।',
        'optimize_result_zero': 'ਫਾਈਲ ਆਕਾਰ ਵਿੱਚ ਕੋਈ ਤਬਦੀਲੀ ਨਹੀਂ।',
        'optimize_result_negative': 'ਫਾਈਲ {0:.1f}% ਵਧੀ ਹੈ।\nਅਨੁਕੂਲਤਾ ਨੂੰ ਛੱਡ ਦਿੱਤਾ ਗਿਆ, ਮੂਲ ਫਾਈਲ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਿਆ ਗਿਆ।',
        'btn_optimize': 'ਅਨੁਕੂਲਤਾ ਸ਼ੁਰੂ ਕਰੋ',
        'filename_optimize_low_suffix': '_ਅਨੁਕੂਲਿਤ_ਘੱਟ',
        'filename_optimize_medium_suffix': '_ਅਨੁਕੂਲਿਤ',
        'filename_optimize_high_suffix': '_ਅਨੁਕੂਲਿਤ_ਉੱਚਾ',
        'filename_optimize_maximum_suffix': '_ਅਨੁਕੂਲਿਤ_ਵੱਧ',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF ਕ੍ਰਾਪ ਕਰੋ',
        'crop_menu': 'PDF ਕ੍ਰਾਪ ਕਰੋ (Crop)',
        'crop_range': 'ਇਸ ਤੇ ਲਾਗੂ ਕਰੋ:',
        'crop_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'crop_current_page': 'ਸਿਰਫ਼ ਮੌਜੂਦਾ ਪੰਨਾ',
        'crop_values': 'ਕ੍ਰਾਪ ਮੁੱਲ (ਪੁਆਇੰਟਾਂ ਵਿੱਚ):',
        'crop_left': 'ਖੱਬੇ:',
        'crop_right': 'ਸੱਜੇ:',
        'crop_top': 'ਉੱਪਰ:',
        'crop_bottom': 'ਹੇਠਾਂ:',
        'crop_presets': 'ਪੂਰਵ-ਨਿਰਧਾਰਤ:',
        'crop_preset_white': 'ਚਿੱਟੇ ਮਾਰਜਿਨ ਖੋਜੋ',
        'crop_reset': 'ਰੀਸੈਟ ਕਰੋ',
        'crop_mouse_hint': '🖱️ ਖੇਤਰ ਨੂੰ ਮੋਟੇ ਤੌਰ ਤੇ ਚੁਣਨ ਲਈ ਇੱਕ ਆਇਤ ਖਿੱਚੋ।\nਫਿਰ ਤੁਸੀਂ SpinBoxes ਵਿੱਚ ਮੁੱਲਾਂ ਨੂੰ ਸਹੀ ਢੰਗ ਨਾਲ ਵਿਵਸਥਿਤ ਕਰ ਸਕਦੇ ਹੋ।\nਮਾਊਸ ਨਾਲ ਹੱਥੀਂ ਵਿਵਸਥਾ ਸੰਭਵ ਨਹੀਂ ਹੈ।',
        'crop_apply': 'ਕ੍ਰਾਪ ਕਰੋ',
        'crop_scope_all': 'ਸਾਰੇ ਪੰਨੇ',
        'crop_scope_current': 'ਮੌਜੂਦਾ ਪੰਨਾ',
        'crop_new_size': 'ਨਵਾਂ ਆਕਾਰ: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'ਕੋਈ PDF ਲੋਡ ਨਹੀਂ ਕੀਤਾ ਗਿਆ',
        'crop_preview_error': 'ਪੂਰਵ-ਦ੍ਰਿਸ਼ ਲੋਡ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ',
        'crop_start': 'ਕ੍ਰਾਪ ਕਰਨਾ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'crop_progress': 'PDF ਕ੍ਰਾਪ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'crop_success': 'PDF ਸਫਲਤਾਪੂਰਵਕ ਕ੍ਰਾਪ ਕੀਤਾ ਗਿਆ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਕੀ ਤੁਸੀਂ ਕ੍ਰਾਪ ਕੀਤਾ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'crop_complete': 'ਕ੍ਰਾਪ ਕਰਨਾ ਪੂਰਾ ਹੋਇਆ',
        'crop_cancel': 'ਕ੍ਰਾਪ ਕਰਨਾ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'crop_error_format': 'ਕ੍ਰਾਪ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ:\n\n{0}',
        'filename_crop_suffix': '_ਕ੍ਰਾਪ_ਕੀਤਾ',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF ਸਮਤਲ ਕਰੋ (Flatten)',
        'flatten_menu': 'PDF ਸਮਤਲ ਕਰੋ (Flatten)',
        'flatten_info': 'PDF ਨੂੰ ਸਮਤਲ ਕਰਨਾ ਸਾਰੇ ਸੰਪਾਦਨਯੋਗ ਤੱਤਾਂ ਨੂੰ ਪੰਨੇ ਦੀ ਸਮੱਗਰੀ ਵਿੱਚ "ਬੇਕ" ਕਰਦਾ ਹੈ।\n\nਇਸ ਤੋਂ ਬਾਅਦ, ਫਾਰਮ ਫੀਲਡਾਂ, ਐਨੋਟੇਸ਼ਨਾਂ, ਟੈਕਸਟ, ਕ੍ਰਾਸ, ਦਸਤਖਤ, ਚਿੱਤਰ ਅਤੇ ਆਕਾਰ ਵੱਖਰੇ ਤੌਰ ਤੇ ਸੰਪਾਦਨਯੋਗ ਨਹੀਂ ਰਹਿੰਦੇ।',
        'flatten_explanation_title': '📖 ਇਹ ਕਿਸ ਲਈ ਚੰਗਾ ਹੈ?',
        'flatten_explanation_text': 'ਸਮਤਲ ਕਰਨਾ ਹੇਠ ਲਿਖੀਆਂ ਸਥਿਤੀਆਂ ਵਿੱਚ ਲੋੜੀਂਦਾ ਹੈ:\n\n'
            '• 📄 ਤੁਸੀਂ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਛਪਾਈ ਲਈ ਤਿਆਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ\n'
            '• 🔒 ਤੁਸੀਂ ਕਿਸੇ ਨੂੰ ਫਾਰਮ ਫੀਲਡਾਂ ਬਦਲਣ ਤੋਂ ਰੋਕਣਾ ਚਾਹੁੰਦੇ ਹੋ\n'
            '• 📎 ਤੁਸੀਂ ਐਨੋਟੇਸ਼ਨਾਂ ਅਤੇ ਟਿੱਪਣੀਆਂ ਨੂੰ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ "ਸਥਾਈ" ਐਂਬੈਡ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ\n'
            '• 🖼️ ਤੁਸੀਂ ਪਾਏ ਗਏ ਟੈਕਸਟ, ਕ੍ਰਾਸ, ਦਸਤਖਤ, ਚਿੱਤਰ ਅਤੇ ਆਕਾਰਾਂ ਨੂੰ ਦਸਤਾਵੇਜ਼ ਵਿੱਚ ਸਥਾਈ ਤੌਰ ਤੇ ਐਂਕਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ\n'
            '• 📦 ਤੁਸੀਂ ਫਾਈਲ ਨੂੰ ਆਰਕਾਈਵਿੰਗ ਲਈ ਤਿਆਰ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ\n\n'
            'ਸਮਤਲ ਕਰਨਾ PDF ਨੂੰ ਛੋਟਾ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਤੱਤਾਂ ਨੂੰ ਗਲਤੀ ਨਾਲ ਹਿਲਾਉਣ ਜਾਂ ਮਿਟਾਉਣ ਤੋਂ ਰੋਕਦਾ ਹੈ।',
        'flatten_what_title': 'ਕੀ ਸਮਤਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ?',
        'flatten_what_list': '• ✅ ਫਾਰਮ ਫੀਲਡਾਂ (ਟੈਕਸਟ ਫੀਲਡਾਂ, ਚੈੱਕਬਾਕਸ, ਬਟਨ)\n'
            '• ✅ ਐਨੋਟੇਸ਼ਨਾਂ (ਟਿੱਪਣੀਆਂ, ਹਾਈਲਾਈਟਾਂ, ਨੋਟਾਂ)\n'
            '• ✅ ਓਵਰਲੇ (ਟੈਕਸਟ, ਕ੍ਰਾਸ, ਦਸਤਖਤ, ਚਿੱਤਰ, ਆਕਾਰ)',
        'flatten_options': 'ਵਿਕਲਪ:',
        'flatten_forms': 'ਫਾਰਮ ਫੀਲਡਾਂ ਸਮਤਲ ਕਰੋ',
        'flatten_annotations': 'ਐਨੋਟੇਸ਼ਨਾਂ ਸਮਤਲ ਕਰੋ',
        'flatten_overlays': 'ਓਵਰਲੇ ਸਮਤਲ ਕਰੋ (ਟੈਕਸਟ, ਕ੍ਰਾਸ, ਦਸਤਖਤ, ਚਿੱਤਰ, ਆਕਾਰ)',
        'flatten_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'flatten_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'flatten_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'flatten_warning': '⚠️ ਮਹੱਤਵਪੂਰਨ: ਸਮਤਲ ਕਰਨਾ ਇੱਕ ਅਟੱਲ ਪ੍ਰਕਿਰਿਆ ਹੈ!\n\nਸਮਤਲ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸੰਪਾਦਨਯੋਗ ਤੱਤਾਂ ਨੂੰ ਵੱਖਰੇ ਤੌਰ ਤੇ ਬਦਲਿਆ ਜਾਂ ਮਿਟਾਇਆ ਨਹੀਂ ਜਾ ਸਕਦਾ।\nਲੋੜ ਪੈਣ ਤੇ ਪਹਿਲਾਂ ਬੈਕਅੱਪ ਬਣਾਓ।',
        'flatten_apply': 'ਸਮਤਲ ਕਰੋ',
        'flatten_start': 'ਸਮਤਲ ਕਰਨਾ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'flatten_progress': 'PDF ਸਮਤਲ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'flatten_success': 'PDF ਸਫਲਤਾਪੂਰਵਕ ਸਮਤਲ ਕੀਤਾ ਗਿਆ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਕੀ ਤੁਸੀਂ ਸਮਤਲ ਕੀਤਾ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'flatten_complete': 'ਸਮਤਲ ਕਰਨਾ ਪੂਰਾ ਹੋਇਆ',
        'flatten_cancel': 'ਸਮਤਲ ਕਰਨਾ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'flatten_error_format': 'ਸਮਤਲ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ:\n\n{0}',
        'filename_flatten_suffix': '_ਸਮਤਲ_ਕੀਤਾ',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF ਓਵਰਲੇ (Overlay)',
        'overlay_menu': 'PDF ਓਵਰਲੇ (Overlay)',
        'overlay_info': 'ਇੱਕ PDF (ਓਵਰਲੇ) ਨੂੰ ਦੂਜੇ PDF ਦੇ ਉੱਪਰ ਰੱਖਦਾ ਹੈ।\n\nਓਵਰਲੇ PDF ਨੂੰ ਬੇਸ PDF ਦੇ ਉੱਪਰ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ। ਇਹ ਵਾਟਰਮਾਰਕ, ਲੋਗੋ, ਲੈਟਰਹੈੱਡ ਜਾਂ ਸਟੈਂਪ ਲਈ ਉਪਯੋਗੀ ਹੈ।',
        'overlay_explanation_title': '📖 ਇਹ ਕਿਸ ਲਈ ਚੰਗਾ ਹੈ?',
        'overlay_explanation_text': 'ਓਵਰਲੇ ਹੇਠ ਲਿਖੀਆਂ ਸਥਿਤੀਆਂ ਵਿੱਚ ਲੋੜੀਂਦਾ ਹੈ:\n\n'
            '• 🏢 ਕੰਪਨੀ ਦਾ ਲੋਗੋ ਵਾਟਰਮਾਰਕ ਵਜੋਂ ਹਰੇਕ ਪੰਨੇ ਤੇ ਰੱਖੋ\n'
            '• 📄 ਖਾਲੀ PDF ਤੇ ਲੈਟਰਹੈੱਡ ਰੱਖੋ\n'
            '• 🖊️ ਦਸਤਾਵੇਜ਼ ਤੇ ਸਟੈਂਪ ਓਵਰਲੇ ਰੱਖੋ\n'
            '• 🔖 ਸਾਰੇ ਪੰਨਿਆਂ ਤੇ ਵਾਟਰਮਾਰਕ ਰੱਖੋ\n'
            '• 📑 ਟੈਂਪਲੇਟ ਤੇ ਫਾਰਮ ਓਵਰਲੇ ਰੱਖੋ',
        'overlay_type': 'ਓਵਰਲੇ ਕਿਸਮ:',
        'overlay_type_fullpage': 'ਪੂਰਾ ਪੰਨਾ (ਢੱਕਣ ਵਾਲਾ)',
        'overlay_type_transparent': 'ਪੂਰਾ ਪੰਨਾ (ਪਾਰਦਰਸ਼ੀ - ਸਿਫ਼ਾਰਸ਼ੀ)',
        'overlay_type_stamp': 'ਸਟੈਂਪ (ਸਥਿਤੀ ਦੇਣ ਯੋਗ)',
        'overlay_type_info_fullpage': '📄 ਓਵਰਲੇ PDF ਨੂੰ ਪੂਰੇ ਪੰਨੇ ਦੇ ਉੱਪਰ ਸਹੀ ਢੰਗ ਨਾਲ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ।\nਚਿੱਟਾ ਪਿਛੋਕੜ ਹਟਾਇਆ ਜਾ ਸਕਦਾ ਹੈ ਤਾਂ ਕਿ ਸਿਰਫ਼ ਸਮੱਗਰੀ ਦਿਖਾਈ ਦੇਵੇ।',
        'overlay_type_info_transparent': '🔍 ਓਵਰਲੇ PDF ਨੂੰ ਪਾਰਦਰਸ਼ੀ ਪਿਛੋਕੜ ਦੇ ਨਾਲ ਪੂਰੇ ਪੰਨੇ ਦੇ ਉੱਪਰ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ।\nਚਿੱਟਾ ਪਿਛੋਕੜ ਆਪਣੇ ਆਪ ਹਟਾਇਆ ਜਾਂਦਾ ਹੈ - ਵਾਟਰਮਾਰਕ ਅਤੇ ਲੋਗੋ ਲਈ ਆਦਰਸ਼!',
        'overlay_type_info_stamp': '🖊️ ਓਵਰਲੇ PDF ਨੂੰ ਸਟੈਂਪ ਵਜੋਂ ਸਥਿਤੀ ਅਤੇ ਸਕੇਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।\nਖਾਸ ਸਥਾਨਾਂ ਤੇ ਲੋਗੋ, ਸਟੈਂਪ ਜਾਂ ਦਸਤਖਤ ਲਈ ਵਧੀਆ।',
        'overlay_remove_background': 'ਚਿੱਟਾ ਪਿਛੋਕੜ ਹਟਾਓ:',
        'overlay_remove_background_enable': 'ਓਵਰਲੇ PDF ਤੋਂ ਚਿੱਟਾ ਪਿਛੋਕੜ ਹਟਾਓ (ਓਵਰਲੇ ਨੂੰ ਪਾਰਦਰਸ਼ੀ ਬਣਾਉਂਦਾ ਹੈ)',
        'overlay_remove_background_tooltip': 'ਓਵਰਲੇ PDF ਤੋਂ ਚਿੱਟੇ ਖੇਤਰਾਂ ਨੂੰ ਹਟਾਉਂਦਾ ਹੈ ਤਾਂ ਕਿ ਹੇਠਾਂ ਦਾ ਟੈਕਸਟ ਦਿਖਾਈ ਦੇਵੇ।',
        'overlay_threshold': 'ਥ੍ਰੈਸ਼ਹੋਲਡ ਮੁੱਲ:',
        'overlay_threshold_hint': '(1-254, ਵੱਧ = ਵੱਧ ਚਿੱਟਾ ਹਟਾਇਆ ਜਾਂਦਾ ਹੈ)',
        'overlay_select_file': 'ਓਵਰਲੇ PDF ਚੁਣੋ:',
        'overlay_file_placeholder': 'ਕਿਰਪਾ ਕਰਕੇ ਓਵਰਲੇ ਲਈ PDF ਫਾਈਲ ਚੁਣੋ',
        'overlay_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'overlay_select_overlay': 'ਓਵਰਲੇ PDF ਚੁਣੋ',
        'overlay_range': 'ਪੰਨਾ ਰੇਂਜ:',
        'overlay_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'overlay_custom_range': 'ਕਸਟਮ ਰੇਂਜ',
        'overlay_from': 'ਤੋਂ:',
        'overlay_to': 'ਤੱਕ:',
        'overlay_position': 'ਸਥਿਤੀ:',
        'overlay_position_center': 'ਕੇਂਦਰ',
        'overlay_position_top_left': 'ਉੱਪਰ ਖੱਬੇ',
        'overlay_position_top_right': 'ਉੱਪਰ ਸੱਜੇ',
        'overlay_position_bottom_left': 'ਹੇਠਾਂ ਖੱਬੇ',
        'overlay_position_bottom_right': 'ਹੇਠਾਂ ਸੱਜੇ',
        'overlay_size': 'ਆਕਾਰ:',
        'overlay_size_original': 'ਮੂਲ ਆਕਾਰ',
        'overlay_size_fit_page': 'ਪੰਨੇ ਨਾਲ ਮੇਲ ਕਰੋ',
        'overlay_size_custom': 'ਕਸਟਮ (%)',
        'overlay_opacity': 'ਪਾਰਦਰਸ਼ਤਾ:',
        'overlay_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'overlay_browse_folder': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'overlay_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'overlay_warning': '⚠️ ਨੋਟ: ਓਵਰਲੇ PDF ਨੂੰ ਬੇਸ PDF ਦੇ ਉੱਪਰ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਇਸ ਵਿੱਚ "ਬੇਕ" ਕੀਤਾ ਜਾਂਦਾ ਹੈ।\n\nਸੁਰੱਖਿਅਤ ਕਰਨ ਤੋਂ ਬਾਅਦ ਓਵਰਲੇ PDF ਦੇ ਤੱਤਾਂ ਨੂੰ ਵੱਖਰੇ ਤੌਰ ਤੇ ਸੰਪਾਦਿਤ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਦਾ।',
        'overlay_apply': 'ਓਵਰਲੇ ਕਰੋ',
        'overlay_start': 'ਓਵਰਲੇ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'overlay_progress': 'PDF ਓਵਰਲੇ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'overlay_success': 'PDF ਸਫਲਤਾਪੂਰਵਕ ਓਵਰਲੇ ਕੀਤਾ ਗਿਆ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਕੀ ਤੁਸੀਂ ਓਵਰਲੇ ਕੀਤਾ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'overlay_complete': 'ਓਵਰਲੇ ਪੂਰਾ ਹੋਇਆ',
        'overlay_cancel': 'ਓਵਰਲੇ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'overlay_error_format': 'ਓਵਰਲੇ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ:\n\n{0}',
        'overlay_no_file': 'ਕੋਈ ਓਵਰਲੇ PDF ਨਹੀਂ ਚੁਣਿਆ ਗਿਆ।\n\nਕਿਰਪਾ ਕਰਕੇ ਓਵਰਲੇ ਕਰਨ ਲਈ PDF ਫਾਈਲ ਚੁਣੋ।',
        'filename_overlay_suffix': '_ਓਵਰਲੇ_ਕੀਤਾ',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'PDF ਤੋਂ ਚਿੱਤਰ ਕੱਢੋ',
        'extract_images_menu': 'ਸਾਰੇ ਚਿੱਤਰ ਕੱਢੋ',
        'extract_images_info': 'PDF ਤੋਂ ਸਾਰੇ ਚਿੱਤਰ ਕੱਢਦਾ ਹੈ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਵੱਖਰੀਆਂ ਫਾਈਲਾਂ ਵਜੋਂ ਸੁਰੱਖਿਅਤ ਕਰਦਾ ਹੈ।\n\nਚਿੱਤਰਾਂ ਨੂੰ ਉਹਨਾਂ ਦੇ ਮੂਲ ਫਾਰਮੈਟ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਜਾਂ ਚੁਣੇ ਗਏ ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲਿਆ ਜਾਂਦਾ ਹੈ।',
        'extract_images_format': 'ਚਿੱਤਰ ਫਾਰਮੈਟ:',
        'extract_images_quality': 'JPEG ਗੁਣਵੱਤਾ:',
        'extract_images_options': 'ਵਿਕਲਪ:',
        'extract_images_subfolder': 'ਉਪ-ਫੋਲਡਰ ਵਿੱਚ ਕੱਢੋ ("PDFਨਾਂ_ਚਿੱਤਰ")',
        'extract_images_unique': 'ਸਿਰਫ਼ ਵਿਲੱਖਣ ਚਿੱਤਰ (ਨਕਲਾਂ ਤੋਂ ਬਚੋ)',
        'extract_images_range': 'ਪੰਨਾ ਰੇਂਜ:',
        'extract_images_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'extract_images_custom_range': 'ਕਸਟਮ ਰੇਂਜ',
        'extract_images_from': 'ਤੋਂ:',
        'extract_images_to': 'ਤੱਕ:',
        'extract_images_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'extract_images_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'extract_images_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'extract_images_info_box': 'ਜਾਣਕਾਰੀ',
        'extract_images_info_text': 'ਵੱਡੇ PDF ਲਈ ਕੱਢਣ ਵਿੱਚ ਕੁਝ ਮਿੰਟ ਲੱਗ ਸਕਦੇ ਹਨ।\n\nਚਿੱਤਰਾਂ ਨੂੰ ਉਹਨਾਂ ਦੇ ਮੂਲ ਨਾਮ ਨਾਲ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਂਦਾ ਹੈ (ਪੰਨਾ_ਚਿੱਤਰ)।',
        'extract_images_extract': 'ਕੱਢੋ',
        'extract_images_start': 'ਕੱਢਣਾ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'extract_images_progress': 'ਚਿੱਤਰ ਕੱਢੇ ਜਾ ਰਹੇ ਹਨ...',
        'extract_images_success': '✅ ਚਿੱਤਰ ਸਫਲਤਾਪੂਰਵਕ ਕੱਢੇ ਗਏ!\n\n{0} ਚਿੱਤਰ ਇੱਥੇ ਸੁਰੱਖਿਅਤ ਕੀਤੇ ਗਏ:\n{1}',
        'extract_images_complete': 'ਚਿੱਤਰ ਕੱਢਣਾ ਪੂਰਾ ਹੋਇਆ',
        'extract_images_cancel': 'ਕੱਢਣਾ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'extract_images_error_format': 'ਚਿੱਤਰ ਕੱਢਦੇ ਸਮੇਂ ਗਲਤੀ:\n\n{0}',
        'extract_images_open_folder': '📁 ਫੋਲਡਰ ਖੋਲ੍ਹੋ',
        'extract_images_no_images': 'PDF ਵਿੱਚ ਕੋਈ ਚਿੱਤਰ ਨਹੀਂ ਮਿਲੇ।',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'ਇੱਕ ਪੰਨੇ ਤੇ ਕਈ ਪੰਨੇ (N-Up)',
        'nup_menu': 'ਇੱਕ ਪੰਨੇ ਤੇ ਕਈ ਪੰਨੇ (N-Up)',
        'nup_info': 'ਕਈ PDF ਪੰਨਿਆਂ ਨੂੰ ਇੱਕ ਪੰਨੇ ਤੇ ਵਿਵਸਥਿਤ ਕਰਦਾ ਹੈ।\n\nਸੰਖੇਪ ਪ੍ਰਿੰਟ, ਸੰਖੇਪ ਜਾਂ ਹੈਂਡਆਉਟ ਲਈ ਆਦਰਸ਼।',
        'nup_layout': 'ਲੇਆਉਟ:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'ਪੂਰਵ-ਦ੍ਰਿਸ਼:',
        'nup_preview_info': '{0} ਪੰਨੇ → {1} ਪੰਨੇ ਪ੍ਰਤੀ ਸ਼ੀਟ → {2} ਸ਼ੀਟਾਂ\nਲੇਆਉਟ: {3}',
        'nup_order': 'ਕ੍ਰਮ:',
        'nup_order_horizontal': 'ਖਿਤਿਜੀ (ਕਤਾਰ ਦਰ ਕਤਾਰ)',
        'nup_order_vertical': 'ਲੰਬਕਾਰੀ (ਕਾਲਮ ਦਰ ਕਾਲਮ)',
        'nup_order_horizontal_reverse': 'ਖਿਤਿਜੀ ਉਲਟਾ',
        'nup_order_vertical_reverse': 'ਲੰਬਕਾਰੀ ਉਲਟਾ',
        'nup_range': 'ਪੰਨਾ ਰੇਂਜ:',
        'nup_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'nup_custom_range': 'ਕਸਟਮ ਰੇਂਜ',
        'nup_from': 'ਤੋਂ:',
        'nup_to': 'ਤੱਕ:',
        'nup_options': 'ਵਿਕਲਪ:',
        'nup_margins': 'ਮਾਰਜਿਨ:',
        'nup_margin_between': 'ਪੰਨਿਆਂ ਵਿਚਕਾਰ ਦੂਰੀ:',
        'nup_page_numbers': 'ਪੰਨਾ ਨੰਬਰ ਪਾਓ',
        'nup_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'nup_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'nup_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'nup_create': 'ਬਣਾਓ',
        'nup_start': 'N-Up ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'nup_progress': 'N-Up ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ...',
        'nup_success': 'N-Up ਸਫਲਤਾਪੂਰਵਕ ਬਣਾਇਆ ਗਿਆ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਕੀ ਤੁਸੀਂ ਨਵਾਂ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'nup_complete': 'N-Up ਪੂਰਾ ਹੋਇਆ',
        'nup_cancel': 'N-Up ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'nup_error_format': 'N-Up ਦੌਰਾਨ ਗਲਤੀ:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'ਪੰਨਾ ਆਕਾਰ ਬਦਲੋ',
        'pagesize_menu': 'ਪੰਨਾ ਆਕਾਰ ਬਦਲੋ',
        'pagesize_info': 'PDF ਦਾ ਪੰਨਾ ਆਕਾਰ ਬਦਲਦਾ ਹੈ।\n\nਸਮੱਗਰੀ ਆਪਣੇ ਆਪ ਨਵੇਂ ਆਕਾਰ ਵਿੱਚ ਅਨੁਕੂਲ ਹੋ ਜਾਂਦੀ ਹੈ।',
        'pagesize_format': 'ਫਾਰਮੈਟ:',
        'pagesize_select': 'ਇੱਕ ਮਿਆਰੀ ਫਾਰਮੈਟ ਚੁਣੋ:',
        'pagesize_custom': 'ਕਸਟਮ ਆਕਾਰ:',
        'pagesize_width': 'ਚੌੜਾਈ:',
        'pagesize_height': 'ਉਚਾਈ:',
        'pagesize_orientation': 'ਓਰੀਐਂਟੇਸ਼ਨ:',
        'pagesize_portrait': 'ਪੋਰਟਰੇਟ',
        'pagesize_landscape': 'ਲੈਂਡਸਕੇਪ',
        'pagesize_scale_options': 'ਸਕੇਲਿੰਗ ਵਿਕਲਪ:',
        'pagesize_fit': 'ਮੇਲ ਕਰੋ (ਪਹਿਲੂ ਅਨੁਪਾਤ ਬਰਕਰਾਰ ਰੱਖੋ)',
        'pagesize_stretch': 'ਖਿੱਚੋ (ਵਿਗਾੜੋ)',
        'pagesize_center': 'ਕੇਂਦਰਿਤ ਕਰੋ (ਮੂਲ ਆਕਾਰ)',
        'pagesize_range': 'ਪੰਨਾ ਰੇਂਜ:',
        'pagesize_all_pages': 'ਸਾਰੇ ਪੰਨੇ',
        'pagesize_custom_range': 'ਕਸਟਮ ਰੇਂਜ',
        'pagesize_from': 'ਤੋਂ:',
        'pagesize_to': 'ਤੱਕ:',
        'pagesize_target_folder': 'ਟੀਚਾ ਫੋਲਡਰ:',
        'pagesize_browse': 'ਬਰਾਊਜ਼ ਕਰੋ...',
        'pagesize_select_folder': 'ਟੀਚਾ ਫੋਲਡਰ ਚੁਣੋ',
        'pagesize_apply': 'ਲਾਗੂ ਕਰੋ',
        'pagesize_start': 'ਪੰਨਾ ਆਕਾਰ ਬਦਲਣਾ ਸ਼ੁਰੂ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ...',
        'pagesize_progress': 'ਪੰਨਾ ਆਕਾਰ ਬਦਲਿਆ ਜਾ ਰਿਹਾ ਹੈ...',
        'pagesize_success': 'ਪੰਨਾ ਆਕਾਰ ਸਫਲਤਾਪੂਰਵਕ ਬਦਲਿਆ ਗਿਆ!\n\nਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਗਿਆ:\n{0}\n\nਕੀ ਤੁਸੀਂ ਨਵਾਂ PDF ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'pagesize_complete': 'ਪੰਨਾ ਆਕਾਰ ਬਦਲਣਾ ਪੂਰਾ ਹੋਇਆ',
        'pagesize_cancel': 'ਪੰਨਾ ਆਕਾਰ ਬਦਲਣਾ ਰੱਦ ਕੀਤਾ ਗਿਆ',
        'pagesize_error_format': 'ਪੰਨਾ ਆਕਾਰ ਬਦਲਦੇ ਸਮੇਂ ਗਲਤੀ:\n\n{0}',
        'pagesize_preview_info': 'ਨਵਾਂ ਆਕਾਰ: {0} x {1} pt',
        'filename_pagesize_suffix': '_ਨਵਾਂ_ਆਕਾਰ',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF ਜਾਣਕਾਰੀ',
        'pdf_info_menu': 'PDF ਜਾਣਕਾਰੀ ਦਿਖਾਓ',
        'pdf_info_voice': 'PDF ਜਾਣਕਾਰੀ ਪ੍ਰਦਰਸ਼ਿਤ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ',
        'pdf_info_error': 'PDF ਜਾਣਕਾਰੀ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰਦੇ ਸਮੇਂ ਗਲਤੀ:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "ਕੀਬੋਰਡ ਸ਼ਾਰਟਕੱਟ ਦਿਖਾਓ",
        "shortcuts_dialog_title": "ਕੀਬੋਰਡ ਸ਼ਾਰਟਕੱਟ",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 ਫਾਈਲ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF ਖੋਲ੍ਹੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF ਬੰਦ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>ਇਸ ਤਰ੍ਹਾਂ ਸੁਰੱਖਿਅਤ ਕਰੋ...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>ਦਸਤਾਵੇਜ਼ ਸੁਰੱਖਿਅਤ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>ਪ੍ਰਿੰਟ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>ਤੁਰੰਤ ਪ੍ਰਿੰਟ ਕਰੋ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>ਐਪਲੀਕੇਸ਼ਨ ਬੰਦ ਕਰੋ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 ਨਿਰਯਾਤ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Pages ਵਜੋਂ ਨਿਰਯਾਤ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>DOCX ਵਜੋਂ ਨਿਰਯਾਤ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>TXT ਵਜੋਂ ਨਿਰਯਾਤ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ਚਿੱਤਰਾਂ ਵਜੋਂ ਨਿਰਯਾਤ ਕਰੋ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>ਚਿੱਤਰ ਕੱਢੋ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ਦਸਤਾਵੇਜ਼ ਪ੍ਰੋਸੈਸਿੰਗ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (ਕਈ ਪੰਨੇ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A ਪਰਿਵਰਤਨ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF ਸਮਤਲ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF ਓਵਰਲੇ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF ਅਨੁਕੂਲ ਬਣਾਓ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ ਸੰਪਾਦਨ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>ਖੋਜੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>ਬੁੱਕਮਾਰਕ ਸ਼ਾਮਲ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ਬੁੱਕਮਾਰਕਾਂ ਦਾ ਪ੍ਰਬੰਧ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>ਅਗਲਾ ਬੁੱਕਮਾਰਕ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>ਪਿਛਲਾ ਬੁੱਕਮਾਰਕ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR ਚਲਾਓ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 ਪੰਨਾ ਪ੍ਰਬੰਧਨ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>ਮੌਜੂਦਾ ਪੰਨਾ ਘੁਮਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>ਸਾਰੇ ਪੰਨੇ ਘੁਮਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>ਮੌਜੂਦਾ ਪੰਨਾ ਆਮ ਬਣਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>ਸਾਰੇ ਪੰਨੇ ਆਮ ਬਣਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ਪੰਨੇ ਮਿਟਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>ਪੰਨੇ ਕੱਢੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>ਪੰਨੇ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>ਪੰਨੇ ਹਿਲਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDFs ਮਰਜ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>ਪੰਨਾ ਆਕਾਰ ਬਦਲੋ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 ਪਾਓ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>ਟੈਕਸਟ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>ਕ੍ਰਾਸ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>ਦਸਤਖਤ 1 ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>ਦਸਤਖਤ 2 ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ਚਿੱਤਰ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>ਆਇਤ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>ਅੰਡਾਕਾਰ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>ਲਕੀਰ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>ਤੀਰ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>ਪੰਨਾ ਨੰਬਰ ਪਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ਟੈਕਸਟ ਵਾਟਰਮਾਰਕ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>ਚਿੱਤਰ ਵਾਟਰਮਾਰਕ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ ਰੀਡੈਕਸ਼ਨਾਂ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ਰੀਡੈਕਸ਼ਨ (ਕਾਲਾ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ਰੀਡੈਕਸ਼ਨ (ਚਿੱਟਾ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>ਸਾਰੀਆਂ ਰੀਡੈਕਸ਼ਨਾਂ ਲਾਗੂ ਕਰੋ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ਉੱਨਤ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF ਕ੍ਰਾਪ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ਮੈਟਾਡੇਟਾ ਸੰਪਾਦਿਤ ਕਰੋ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ ਦ੍ਰਿਸ਼</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ਡਾਰਕ/ਲਾਈਟ ਮੋਡ ਟੌਗਲ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>ਟੈਕਸਟ ਵਿੰਡੋ ਦਿਖਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>ਪੰਨਾ ਚੌੜਾਈ (ਜ਼ੂਮ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>ਦੋ ਪੰਨੇ (ਜ਼ੂਮ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>ਸੰਖੇਪ (ਜ਼ੂਮ)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ਸੈਟਿੰਗਾਂ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>ਪਾਸਵਰਡ ਪ੍ਰਬੰਧਨ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR ਸੈਟਿੰਗਾਂ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>ਦਸਤਖਤ ਸੈਟਿੰਗਾਂ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>ਫਾਈਲਨਾਂ ਫਾਰਮੈਟਿੰਗ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>ਸੈਟਿੰਗਾਂ ਨਿਰਯਾਤ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>ਸੈਟਿੰਗਾਂ ਆਯਾਤ ਕਰੋ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ ਜਾਣਕਾਰੀ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF ਜਾਣਕਾਰੀ ਦਿਖਾਓ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>ਵੌਇਸ ਆਉਟਪੁੱਟ ਟੌਗਲ ਕਰੋ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>ਮੀਨੂ ਬਾਰ ਤੇ ਫੋਕਸ ਕਰੋ</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "ਨਵਾਂ ਵਰਜਨ ਉਪਲਬਧ",
        "update_available_message": "ਇੱਕ ਨਵਾਂ ਵਰਜਨ <b>{0}</b> ਉਪਲਬਧ ਹੈ।\n\nਅੱਪਡੇਟ ਡਾਊਨਲੋਡ ਕਰਨ ਲਈ ਰੀਲੀਜ਼ ਪੰਨੇ 'ਤੇ ਜਾਓ:\n{1}",
        "update_available_voice": "ਨਵਾਂ ਵਰਜਨ {0} ਉਪਲਬਧ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ GitHub ਪੰਨੇ ਤੋਂ ਅੱਪਡੇਟ ਡਾਊਨਲੋਡ ਕਰੋ।",
        "update_open_release": "ਰੀਲੀਜ਼ ਪੰਨਾ ਖੋਲ੍ਹੋ",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "ਸਾਰੇ ਅਨੁਵਾਦ ਡਾਊਨਲੋਡ ਕਰੋ",
        "ask_download_all_translations": """ਜਰਮਨ, ਅੰਗਰੇਜ਼ੀ ਅਤੇ ਵੀਅਤਨਾਮੀ ਤੋਂ ਇਲਾਵਾ, {total_languages} ਹੋਰ GUI ਭਾਸ਼ਾਵਾਂ ਉਪਲਬਧ ਹਨ।\n\nਕੀ ਇਹਨਾਂ ਨੂੰ ਪ੍ਰਦਾਨ / ਅੱਪਡੇਟ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ?\n\nਨੋਟ:\nਲੋੜ ਤੋਂ ਵੱਧ ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਤੁਸੀਂ ਬਾਅਦ ਵਿੱਚ ਡਾਇਰੈਕਟਰੀ ਤੋਂ ਹੱਥੀਂ ਮਿਟਾ ਸਕਦੇ ਹੋ:\n{translations_path}
        \nਜੇਕਰ ਤੁਸੀਂ ਰੱਦ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ GUI ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਬਾਅਦ ਵਿੱਚ 'ਟੂਲਸ → ਅਨੁਵਾਦ ਅੱਪਡੇਟ ਕਰੋ' ਮੀਨੂ ਰਾਹੀਂ ਡਾਊਨਲੋਡ ਕਰ ਸਕਦੇ ਹੋ।""",
        "menu_update_translations": "ਅਨੁਵਾਦ ਅੱਪਡੇਟ ਕਰੋ",
        "translations_updated": "ਅਨੁਵਾਦ ਅੱਪਡੇਟ ਕੀਤੇ ਗਏ",
        "translations_update_success": "{} ਅਨੁਵਾਦ ਸਫਲਤਾਪੂਰਵਕ ਅੱਪਡੇਟ ਕੀਤੇ ਗਏ ({} ਨਵੇਂ, {} ਅੱਪਡੇਟ ਕੀਤੇ)।",
        "translations_update_error": "ਅਨੁਵਾਦ ਅੱਪਡੇਟ ਕਰਨ ਵਿੱਚ ਗਲਤੀ",
        "translations_update_no_changes": "ਸਾਰੇ ਅਨੁਵਾਦ ਪਹਿਲਾਂ ਹੀ ਅੱਪ-ਟੂ-ਡੇਟ ਹਨ।",
        "translations_update_offline": "ਕੋਈ ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ ਨਹੀਂ। ਅਨੁਵਾਦ ਅੱਪਡੇਟ ਨਹੀਂ ਕੀਤੇ ਜਾ ਸਕੇ।",
        "translations_update_in_progress": "ਅਨੁਵਾਦ ਪਿਛੋਕੜ ਵਿੱਚ ਅੱਪਡੇਟ ਕੀਤੇ ਜਾ ਰਹੇ ਹਨ...",
        "translations_downloading": "ਅਨੁਵਾਦ ਡਾਊਨਲੋਡ ਹੋ ਰਹੇ ਹਨ...",
        "translations_path_hint": "ਅਨੁਵਾਦਾਂ ਲਈ ਉਪਭੋਗਤਾ ਡਾਇਰੈਕਟਰੀ",
        "translations_update_not_available_title": "ਅੱਪਡੇਟ ਉਪਲਬਧ ਨਹੀਂ",
        "translations_update_not_available_message": """ਅਨੁਵਾਦ ਅੱਪਡੇਟ ਕਰਨਾ ਸਿਰਫ਼ ਸਥਾਪਿਤ ਵਰਜਨ ਵਿੱਚ ਉਪਲਬਧ ਹੈ।\n\nਵਿਕਾਸ ਮੋਡ ਵਿੱਚ, ਅਨੁਵਾਦ ਪਹਿਲਾਂ ਹੀ ਅੱਪ-ਟੂ-ਡੇਟ ਹਨ।""",
        "translations_update_no_internet_title": "ਕੋਈ ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ ਨਹੀਂ",
        "translations_update_no_internet_message": """ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ ਸਥਾਪਤ ਨਹੀਂ ਕੀਤਾ ਜਾ ਸਕਿਆ।\n\nGitHub ਤੋਂ ਅਨੁਵਾਦ ਡਾਊਨਲੋਡ ਨਹੀਂ ਕੀਤੇ ਜਾ ਸਕਦੇ।\n\nਸੰਭਾਵੀ ਹੱਲ:
        • ਆਪਣੇ ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ ਦੀ ਜਾਂਚ ਕਰੋ
        • ਕਿਸੇ ਵੀ ਫਾਇਰਵਾਲ ਨੂੰ ਅਸਥਾਈ ਤੌਰ 'ਤੇ ਅਯੋਗ ਕਰੋ
        • ਬਾਅਦ ਵਿੱਚ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ
        \nਤੁਸੀਂ GitHub ਤੋਂ ਹੱਥੀਂ ਵੀ ਅਨੁਵਾਦ ਡਾਊਨਲੋਡ ਕਰ ਸਕਦੇ ਹੋ:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "ਅੱਪਡੇਟ ਪਹਿਲਾਂ ਹੀ ਚੱਲ ਰਿਹਾ ਹੈ",
        "btn_retry": "ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "PDF Dark View ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ",
        "welcome_title_not_supported": "PDF Dark View ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ",
        "welcome_message": "PDF Dark View ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!\n\nਤੁਹਾਡੀ ਸਿਸਟਮ ਭਾਸ਼ਾ '{language}' ਵਜੋਂ ਪਛਾਣੀ ਗਈ।\nਕੀ ਤੁਸੀਂ ਇਸ ਭਾਸ਼ਾ ਨੂੰ ਉਪਭੋਗਤਾ ਇੰਟਰਫੇਸ ਲਈ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ?\n\nਤੁਸੀਂ 'ਸੈਟਿੰਗਜ਼ → ਭਾਸ਼ਾ' ਰਾਹੀਂ ਕਿਸੇ ਵੀ ਸਮੇਂ ਭਾਸ਼ਾ ਬਦਲ ਸਕਦੇ ਹੋ।",
        "welcome_message_language_not_available": "PDF Dark View ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!\n\nਤੁਹਾਡੀ ਸਿਸਟਮ ਭਾਸ਼ਾ '{language}' ਵਜੋਂ ਪਛਾਣੀ ਗਈ।\nਇਹ ਭਾਸ਼ਾ ਅਜੇ ਸਥਾਪਿਤ ਨਹੀਂ ਹੈ।\n\nਕੀ ਤੁਸੀਂ ਹੁਣ GitHub ਤੋਂ {language} ਲਈ ਅਨੁਵਾਦ ਡਾਊਨਲੋਡ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ?\n\n(ਭਾਸ਼ਾ ਫਿਰ ਆਪਣੇ ਆਪ ਉਪਭੋਗਤਾ ਇੰਟਰਫੇਸ ਲਈ ਵਰਤੀ ਜਾਵੇਗੀ।)",
        "welcome_message_language_not_supported": "PDF Dark View ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!\n\nਤੁਹਾਡੀ ਸਿਸਟਮ ਭਾਸ਼ਾ '{language}' ਵਜੋਂ ਪਛਾਣੀ ਗਈ।\nਬਦਕਿਸਮਤੀ ਨਾਲ, ਇਸ ਭਾਸ਼ਾ ਲਈ ਅਜੇ ਕੋਈ ਅਨੁਵਾਦ ਨਹੀਂ ਹਨ।\n\nਉਪਭੋਗਤਾ ਇੰਟਰਫੇਸ {fallback_language} ਵਿੱਚ ਦਿਖਾਇਆ ਜਾਵੇਗਾ।\n\nਤੁਸੀਂ 'ਸੈਟਿੰਗਜ਼ → ਭਾਸ਼ਾ' ਰਾਹੀਂ ਕਿਸੇ ਵੀ ਸਮੇਂ ਭਾਸ਼ਾ ਬਦਲ ਸਕਦੇ ਹੋ।\nਜੇਕਰ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਆਪਣੀ ਭਾਸ਼ਾ ਲਈ ਅਨੁਵਾਦ ਵੀ ਦੇ ਸਕਦੇ ਹੋ:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "ਹਾਂ, ਸਿਸਟਮ ਭਾਸ਼ਾ ਵਰਤੋ",
        "welcome_keep_english": "ਨਹੀਂ, ਅੰਗਰੇਜ਼ੀ ਰੱਖੋ",
        "welcome_download_language": "ਹਾਂ, {language} ਡਾਊਨਲੋਡ ਕਰੋ",

        # ============================================
        # 107. ਹਾਲ ਹੀ ਵਿੱਚ ਵਰਤੇ ਗਏ ਪਾਥ
        # ============================================

        'menu_recent': 'ਹਾਲ ਹੀ ਵਿੱਚ ਵਰਤੇ ਗਏ',
        'menu_recent_dirs': 'ਡਾਇਰੈਕਟਰੀਆਂ...',
        'menu_recent_files': 'ਫਾਈਲਾਂ...',
        'recent_manage': 'ਪ੍ਰਬੰਧਿਤ ਕਰੋ...',
        'recent_enable_tracking': 'ਹਾਲ ਹੀ ਦੇ ਪਾਥ ਸੁਰੱਖਿਅਤ ਕਰੋ (ਪਰਦੇਦਾਰੀ)',
        'recent_enable_info': 'ਪਾਥ ਸੁਰੱਖਿਅਤ ਨਾ ਕਰਨ ਲਈ ਇਸ ਵਿਕਲਪ ਨੂੰ ਅਸਮਰੱਥ ਕਰੋ',
        'recent_tracking_disabled': 'ਪਾਥ ਟਰੈਕਿੰਗ ਅਸਮਰੱਥ ਹੈ',
        'recent_enabled': 'ਸਮਰੱਥ',
        'recent_disabled': 'ਅਸਮਰੱਥ',
        'recent_tracking_status': 'ਪਾਥ ਟਰੈਕਿੰਗ {0}',
        'recent_dialog_title': 'ਹਾਲ ਹੀ ਵਿੱਚ ਵਰਤੇ ਗਏ ਪਾਥ',
        'recent_tab_directories': 'ਡਾਇਰੈਕਟਰੀਆਂ',
        'recent_tab_files': 'ਫਾਈਲਾਂ',
        'recent_dirs_instruction': 'ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਫਾਈਲ ਡਾਇਲਾਗ ਖੋਲ੍ਹਣ ਲਈ ਡਬਲ-ਕਲਿੱਕ ਕਰੋ',
        'recent_files_instruction': 'PDF ਸਿੱਧਾ ਖੋਲ੍ਹਣ ਲਈ ਡਬਲ-ਕਲਿੱਕ ਕਰੋ',
        'recent_no_directories': '(ਕੋਈ ਡਾਇਰੈਕਟਰੀ ਸੁਰੱਖਿਅਤ ਨਹੀਂ)',
        'recent_no_files': '(ਕੋਈ ਫਾਈਲ ਸੁਰੱਖਿਅਤ ਨਹੀਂ)',
        'recent_default_current': '⭐ ਮੂਲ: {0}',
        'recent_set_as_default': '⭐ ਮੂਲ ਵਜੋਂ ਸੈੱਟ ਕਰੋ',
        'recent_default_set_title': 'ਮੂਲ ਡਾਇਰੈਕਟਰੀ ਸੈੱਟ ਕੀਤੀ ਗਈ',
        'recent_default_set_message': '"{0}" ਡਾਇਰੈਕਟਰੀ ਨੂੰ PDF ਖੋਲ੍ਹਣ ਲਈ ਮੂਲ ਵਜੋਂ ਸੈੱਟ ਕੀਤਾ ਗਿਆ ਹੈ।',
        'recent_default_set_voice': 'ਮੂਲ ਡਾਇਰੈਕਟਰੀ ਸੈੱਟ ਕੀਤੀ ਗਈ',
        'recent_directory_not_found': 'ਡਾਇਰੈਕਟਰੀ ਨਹੀਂ ਲੱਭੀ',
        'recent_file_not_found': 'ਫਾਈਲ ਨਹੀਂ ਲੱਭੀ',
        'recent_remove_selected': 'ਹਟਾਓ',
        'recent_remove_title': 'ਪਾਥ ਹਟਾਓ',
        'recent_remove_confirm': 'ਕੀ ਤੁਸੀਂ ਸੱਚਮੁੱਚ "{0}" ਪਾਥ ਨੂੰ ਸੂਚੀ ਵਿੱਚੋਂ ਹਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'recent_path_removed': 'ਪਾਥ ਹਟਾ ਦਿੱਤਾ ਗਿਆ',
        'recent_clear_all': 'ਸਭ ਹਟਾਓ',
        'recent_clear_title': 'ਸਭ ਪਾਥ ਹਟਾਓ',
        'recent_clear_confirm_type': 'ਕੀ ਤੁਸੀਂ ਸੱਚਮੁੱਚ ਸਭ {0} ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'recent_cleared': 'ਸੂਚੀ ਸਾਫ਼ ਕਰ ਦਿੱਤੀ ਗਈ',
        'recent_path_not_found_title': 'ਪਾਥ ਨਹੀਂ ਲੱਭਿਆ',
        'recent_path_not_found_message': '"{0}" ਪਾਥ ਹੁਣ ਮੌਜੂਦ ਨਹੀਂ ਹੈ।',
        'recent_open_file': 'ਫਾਈਲ ਖੋਲ੍ਹੋ',
        'btn_open_recent': 'ਖੋਲ੍ਹੋ',
        'recent_open_file_question': 'ਕੀ ਤੁਸੀਂ "{0}" ਨੂੰ PDF ਵਜੋਂ ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ?',
        'recent_not_pdf': 'ਚੁਣੀ ਗਈ ਫਾਈਲ PDF ਨਹੀਂ ਹੈ।',
        'recent_more_entries': 'ਹੋਰ ਐਂਟਰੀਆਂ...',
        'btn_remove': 'ਹਟਾਓ',
        'btn_clear': 'ਸਭ ਸਾਫ਼ ਕਰੋ',
        'recent_context_open': 'ਖੋਲ੍ਹੋ',
        'recent_context_reveal': 'Finder ਵਿੱਚ ਦਿਖਾਓ',
        'recent_context_set_default': '⭐ ਮੂਲ ਵਜੋਂ ਸੈੱਟ ਕਰੋ',
        'recent_context_open_terminal': '💻 ਟਰਮੀਨਲ ਖੋਲ੍ਹੋ',
        'recent_context_file_info': 'ਫਾਈਲ ਜਾਣਕਾਰੀ',
        'recent_context_open_with_default': '📄 ਮੂਲ ਐਪ ਨਾਲ ਖੋਲ੍ਹੋ',
        'recent_context_remove': 'ਸੂਚੀ ਵਿੱਚੋਂ ਹਟਾਓ',
        'recent_context_clear_all': 'ਸਭ ਹਟਾਓ',
        'recent_file_info_title': 'ਫਾਈਲ ਜਾਣਕਾਰੀ',
        'recent_file_info_name': 'ਨਾਮ',
        'recent_file_info_path': 'ਪਾਥ',
        'recent_file_info_size': 'ਆਕਾਰ',
        'recent_file_info_modified': 'ਸੋਧਿਆ ਗਿਆ',
        'recent_file_info_pages': 'ਸਫ਼ੇ',
        'recent_error_reveal': 'Finder ਵਿੱਚ ਖੋਲ੍ਹਣ ਵਿੱਚ ਗਲਤੀ',
        'recent_error_terminal': 'ਟਰਮੀਨਲ ਖੋਲ੍ਹਣ ਵਿੱਚ ਗਲਤੀ',
        'recent_error_info': 'ਫਾਈਲ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਵਿੱਚ ਗਲਤੀ',
        'open_user_data_folder': 'ਉਪਭੋਗਤਾ ਡਾਟਾ ਡਾਇਰੈਕਟਰੀ ਦਿਖਾਓ',

        # ============================================
        # 108. ਜੋੜ/ਵਿਸਮ ਸਫ਼ੇ ਮਿਟਾਓ
        # ============================================
        "pages_delete_even": "ਸਭ ਜੋੜ ਸਫ਼ੇ ਮਿਟਾਓ",
        "pages_delete_odd":  "ਸਭ ਵਿਸਮ ਸਫ਼ੇ ਮਿਟਾਓ",
        "progress_even_pages": "ਜੋੜ ਸਫ਼ੇ ਮਿਟਾਏ ਜਾ ਰਹੇ ਹਨ",
        "progress_odd_pages": "ਵਿਸਮ ਸਫ਼ੇ ਮਿਟਾਏ ਜਾ ਰਹੇ ਹਨ",
        "progress_mark_delete_even": "{} ਜੋੜ ਸਫ਼ੇ ਮਿਟਾਉਣ ਲਈ ਚਿੰਨ੍ਹਿਤ ਕੀਤੇ ਗਏ",
        "progress_mark_delete_odd":  "{} ਵਿਸਮ ਸਫ਼ੇ ਮਿਟਾਉਣ ਲਈ ਚਿੰਨ੍ਹਿਤ ਕੀਤੇ ਗਏ",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "ਪ੍ਰੋਗਰਾਮ ਬੰਦ ਹੋ ਰਿਹਾ ਹੈ",

    }
