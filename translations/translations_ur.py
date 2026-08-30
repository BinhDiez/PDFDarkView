
# ============================================
# translations_ur.py - Urdu Wörterbuch für PDFDarkView
# Vollständig sortiert nach Kategorien
# ============================================

def load_urdu_strings():
    """Lädt alle Urdu Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF لوڈ کریں",
        'btn_text_window': "OCR متن",
        'btn_first': "پہلا صفحہ",
        'btn_prev': "پچھلا صفحہ",
        'btn_next': "اگلا صفحہ",
        'btn_last': "آخری صفحہ",
        'btn_print': "پرنٹ کریں",
        'btn_darkmode_light': "روشن موڈ",
        'btn_darkmode_dark': "تاریک موڈ",
        'btn_delete_pages': "صفحات حذف کریں",
        'btn_extract_pages': "صفحات نکالیں",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "ٹھیک ہے",
        'btn_cancel': "منسوخ کریں",
        'btn_save': "محفوظ کریں",
        'btn_close': "بند کریں",
        'btn_delete': "حذف کریں",
        'btn_delete_all': "سب حذف کریں",
        'btn_copy': "نقل کریں",
        'btn_export': "برآمد کریں",
        'btn_show': "پاس ورڈ دکھائیں",
        'btn_hide': "پاس ورڈ چھپائیں",
        'btn_authenticate': "تصدیق کریں",
        'btn_settings': "ترتیبات",
        'btn_protect': "محفوظ کریں",
        'btn_remove_password': "پاس ورڈ ہٹائیں",
        'btn_manage': "پاس ورڈ کا انتظام",
        'btn_retry': "دوبارہ کوشش کریں",
        'btn_select_all': "سب منتخب کریں",
        'btn_clear_selection': "انتخاب منسوخ کریں",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "{1} میں سے صفحہ {0}",
        'page_count': "{0} میں سے",
        'goto_page': "صفحہ پر جائیں",
        'page_simple': "صفحہ {0}",
        'full_view_page': "مکمل منظر صفحہ {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "تلاش کا لفظ ٹائپ کریں + Enter",
        'search_results': "نتائج: {1} میں سے {0}",
        'search_nav_hint': "Enter: اگلا (Shift+Enter: پچھلا) نتیجہ",
        'search_no_results': "کوئی نتیجہ نہیں",
        'search_error': "تلاش کی خرابی",
        'search_active': "تلاش کا فیلڈ فعال ہے",
        'search_closed': "تلاش ختم ہوئی",
        'search_position': "صفحہ {0} {1}",
        'search_pos_top': "بالکل اوپر",
        'search_pos_upper': "اوپر",
        'search_pos_middle': "وسط میں",
        'search_pos_lower': "نیچے",
        'search_pos_bottom': "بالکل نیچے",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "متن کی شناخت کامیابی سے مکمل ہوگئی!",
        'ocr_success_title': "OCR کامیاب",
        'ocr_success_message': "دستاویز اب تلاش کے قابل ہے۔",
        'ocr_failed': "OCR ناکام",
        'ocr_in_progress': "OCR جاری ہے",
        'ocr_preparing': "PDF تیار کی جا رہی ہے...",
        'ocr_analyzing': "PDF کا تجزیہ کیا جا رہا ہے...",
        'ocr_optimizing': "تصویر کی اصلاح جاری ہے...",
        'ocr_recognizing': "متن کی شناخت کا کام جاری ہے...",
        'ocr_embedding': "متن ایمبیڈ کیا جا رہا ہے...",
        'ocr_finalizing': "PDF کو حتمی شکل دی جا رہی ہے...",
        'ocr_not_available': "OCR دستیاب نہیں",
        'ocr_install_message': "OCR ٹولز نہیں ملے۔\n\nبراہ کرم انسٹال کریں:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR ضروری ہے",
        'ocr_question': "PDF میں تلاش کے قابل متن نہیں ہے۔\nکیا آپ {0} کو فعال کرنے کے لیے OCR کرنا چاہتے ہیں؟",
        'ocr_perform': "OCR کریں",
        'ocr_later': "بعد میں",
        'ocr_starting': "یقینی OCR شروع ہو رہا ہے...",
        'ocr_success_voice': "OCR کامیاب۔ PDF اب تلاش کے قابل ہے۔",
        'ocr_partial_success': "OCR کیا گیا، لیکن تبدیل کرتے وقت مسائل تھے۔\n\nتلاش کے قابل ورژن یہاں محفوظ کیا گیا:\n{0}\n\nخرابی: {1}",
        'ocr_partial_title': "OCR جزوی طور پر کامیاب",
        'ocr_partial_voice': "OCR کیا گیا، لیکن تبدیل کرنا ناکام رہا۔",
        'original_file': "اصل فائل:",
        'old_size': "پرانے فائل کا سائز:    {0} بائٹس",
        'new_size': "نئے فائل کا سائز: {0} بائٹس",
        'size_change': "تبدیلی: {0}{1} بائٹس",
        'backup_created_file': "بیک اپ بنایا گیا:\n{0}",
        'backup_not_created': "بیک اپ: نہیں بنایا گیا (ترتیب غیر فعال)",
        'page_header': "=== صفحہ {0} ===\n{1}\n",
        'scanned_page_header': "=== صفحہ {0} (اسکین شدہ) ===\n[اس صفحہ میں صرف اسکین شدہ متن ہے]\n[براہ کرم دستی طور پر OCR کریں]\n",
        'scanned_warning': "⚠️ اسکین شدہ متن - OCR ضروری ہے",
        'guaranteed_title': "تلاش کے قابل PDF بنائی گئی",
        'guaranteed_message': "<b>یقینی تلاش کے قابل ورژن بنایا گیا!</b>\n\nچونکہ خودکار OCR ناکام ہو گیا، ایک\nمتبادل تلاش کے قابل PDF بنائی گئی:\n\n{0}\n\n<b>اس فائل میں شامل ہے:</b>\n• نکالا گیا متن (اگر موجود ہو)\n• اسکین شدہ صفحات کے لیے نوٹس\n• مکمل طور پر تلاش کے قابل ہے",
        'guaranteed_voice': "یقینی تلاش کے قابل PDF بنائی گئی۔",
        'instruction_title': "OCR کے لیے ہدایات",
        'instruction_file': "اصل فائل: {0}",
        'instruction_text': "خودکار متن کی شناخت (OCR) ناکام ہو گئی۔\nبراہ کرم دستی طور پر OCR کریں:\n\n1. OCRmyPDF کے ساتھ (کمانڈ لائن):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. ADOBE ACROBAT کے ساتھ (macOS/Windows):\n   • Acrobat میں PDF کھولیں\n   • Tools > Edit PDF\n   • 'Text Recognition' منتخب کریں\n\n3. PREVIEW کے ساتھ (macOS):\n   • Preview میں PDF کھولیں\n   • File > Export...\n   • Quartz Filter: 'Reduce File Size'\n   • 'OCR کریں' فعال کریں\n\n4. آن لائن OCR خدمات:\n   • smallpdf.com/de/ocr-pdf\n   • ilovepdf.com/de/ocr-pdf\n   • adobe.com/de/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR ہدایات بنائی گئیں",
        'instruction_created_message': "ایک تفصیلی ہدایت بنائی گئی:\n\n{0}\n\nبراہ کرم دستی OCR کے لیے اقدامات پر عمل کریں۔",
        'instruction_created_voice': "OCR ہدایات بنائی گئیں۔",
        'ocr_impossible': "OCR ممکن نہیں",
        'ocr_impossible_message': "OCR نہیں کیا جا سکا۔\n\nبراہ کرم '{0}' کو دستی طور پر OCR سافٹ ویئر سے پروسیس کریں۔",
        'ocr_impossible_voice': "OCR ممکن نہیں۔ براہ کرم دستی طور پر پروسیس کریں۔",
        'emergency_title': "ایمرجنسی OCR",
        'emergency_message': "ایک ایمرجنسی PDF بنائی گئی:\n\n{0}\n\nبراہ کرم اس فائل کو دستی طور پر OCR سے پروسیس کریں۔",
        'emergency_voice': "ایمرجنسی PDF بنائی گئی۔ براہ کرم دستی طور پر OCR کریں۔",
        'critical_error': "شدید خرابی",
        'critical_error_message': "OCR شروع نہیں کیا جا سکا۔\n\nبراہ کرم پروگرام دوبارہ شروع کریں اور\nOCR کی تنصیب چیک کریں۔",
        'critical_error_voice': "شدید OCR خرابی",
        'ocr_question_html': "<p>PDF میں تلاش کے قابل متن نہیں ہے۔<p>کیا آپ <b>{0}</b> کو فعال کرنے کے لیے OCR کرنا چاہتے ہیں؟</p>",
        'ocr_question_voice': "OCR ضروری ہے۔ PDF میں تلاش کے قابل متن نہیں ہے۔ کیا آپ {0} کو فعال کرنے کے لیے OCR کرنا چاہتے ہیں؟",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "کوئی PDF لوڈ نہیں کی گئی",
        'no_pdf_message': "کوئی PDF لوڈ نہیں کی گئی",
        'pdf_not_found': "PDF فائل نہیں ملی",
        'file_size': "فائل کا سائز",
        'bytes': "بائٹس",
        'kb': "کلو بائٹ",
        'mb': "میگا بائٹ",
        'backup_created': "بیک اپ بنایا گیا",
        'backup_disabled': "بیک اپ غیر فعال",
        'backup_activated': "بیک اپ بنانا فعال",
        'backup_deactivated': "بیک اپ بنانا غیر فعال",
        'backup_status': "بیک اپ: {0}",
        'backup_on': "✔ فعال",
        'backup_off': "✘ غیر فعال",
        'close_pdf': "PDF بند کی جا رہی ہے: {0}",
        'pdf_not_found_format': "PDF فائل نہیں ملی: {0}",
        'error_pdf_load_format': "PDF لوڈ کرتے وقت خرابی: {0}",
        'load_failed_format': "لوڈ ناکام:\n{0}",
        'decrypted_suffix': "(ڈیکرپٹ شدہ)",
        'decryption_failed': "ڈیکرپشن ناکام۔",
        'decryption_error': "ڈیکرپٹ کرتے وقت خرابی",
        'decryption_success': "کامیابی سے ڈیکرپٹ ہو گئی",
        'decryption_success_message': "PDF ڈیکرپٹ کر کے یہاں محفوظ کی گئی:\n\n{0}",
        'decryption_success_voice': "PDF ڈیکرپٹ کر کے محفوظ کر دی گئی۔",
        'password_remove_error': "پاس ورڈ ہٹاتے وقت خرابی",
        'save_unencrypted': "غیر خفیہ شدہ PDF محفوظ کریں",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "بطور محفوظ کریں...",
        'save_copy': "نقل محفوظ کریں",
        'save_success': "PDF یہاں محفوظ کی گئی: {0}",
        'save_encrypted': "محفوظ شدہ PDF یہاں محفوظ کی گئی: {0}",
        'save_error': "PDF محفوظ نہیں کی جا سکی",
        'encryption_question': "کیا آپ PDF کو پاس ورڈ سے محفوظ کرنا چاہتے ہیں؟",
        'encryption_yes': "ہاں",
        'encryption_no': "نہیں",
        'encryption_cancel': "منسوخ کریں",
        'save_cancel': "محفوظ کرنا منسوخ کر دیا گیا",
        'save_encrypted_voice': "فائل خفیہ کر کے محفوظ کر دی گئی۔",
        'save_success_voice': "PDF فائل غیر خفیہ شدہ محفوظ کر دی گئی۔",
        'save_error_format': "PDF محفوظ نہیں کی جا سکی:\n{0}",
        'export_pages_success': "Pages برآمد کامیاب",
        'export_pages_error': "Pages برآمد ناکام",
        'export_pages_error_format': "Pages برآمد ناکام: {0}",
        'export_word_success': "Word برآمد کامیاب",
        'export_word_error': "Word برآمد ناکام",
        'export_word_error_format': "Word برآمد ناکام: {0}",
        'export_text_success': "متن برآمد کامیاب",
        'export_text_error': "متن برآمد ناکام",
        'export_text_error_format': "متن برآمد ناکام: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "پاس ورڈ درکار ہے",
        'password_enter': "براہ کرم پاس ورڈ ٹائپ کریں",
        'password_confirm': "پاس ورڈ کی تصدیق کریں",
        'password_new': "نیا پاس ورڈ",
        'password_current': "موجودہ پاس ورڈ",
        'password_save': "پاس ورڈ محفوظ کریں (خفیہ شدہ)",
        'password_saved': "✓ اس فائل کے لیے پاس ورڈ محفوظ کر لیا گیا ہے",
        'password_wrong': "غلط پاس ورڈ",
        'password_mismatch': "پاس ورڈز مماثل نہیں ہیں",
        'password_too_short': "پاس ورڈ بہت چھوٹا ہے",
        'password_min_length': "پاس ورڈ کم از کم 4 حروف کا ہونا چاہیے",
        'password_strength': "پاس ورڈ کی مضبوطی",
        'password_strength_very_weak': "انتہائی کمزور",
        'password_strength_weak': "کمزور",
        'password_strength_medium': "درمیانہ",
        'password_strength_strong': "مضبوط",
        'password_strength_very_strong': "انتہائی مضبوط",
        'password_char_count': "({0} حروف)",
        'password_match': "✓ مماثل",
        'password_no_match': "✗ پاس ورڈز مماثل نہیں ہیں",
        'password_show': "دکھائیں",
        'password_hide': "چھپائیں",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "پاس ورڈ کا انتظام",
        'password_table_filename': "فائل کا نام",
        'password_table_password': "پاس ورڈ",
        'password_count': "{0} محفوظ شدہ پاس ورڈ",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "کوئی محفوظ شدہ پاس ورڈ نہیں",
        'password_copied': "{0} پاس ورڈ نقل کیا گیا",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "کیا آپ واقعی '{0}' کے لیے پاس ورڈ حذف کرنا چاہتے ہیں؟",
        'password_delete_multiple': "کیا آپ واقعی منتخب کردہ {0} پاس ورڈز حذف کرنا چاہتے ہیں؟",
        'password_delete_all_confirm': "کیا آپ واقعی تمام {0} محفوظ شدہ پاس ورڈز حذف کرنا چاہتے ہیں؟",
        'password_deleted': "{0} پاس ورڈ حذف کر دیا گیا",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "تمام پاس ورڈز حذف کر دیے گئے",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "پاس ورڈ جنریٹر",
        'generator_generated': "تیار کردہ پاس ورڈ:",
        'generator_regenerate': "دوبارہ تیار کریں",
        'generator_copy': "نقل کریں",
        'generator_use': "استعمال کریں",
        'generator_settings': "ترتیبات",
        'generator_length': "لمبائی:",
        'generator_group_every': "محدود کنندہ ہر",
        'generator_group_chars': "حروف۔    محدود کنندہ:",
        'generator_uppercase': "بڑے حروف (A-Z)",
        'generator_lowercase': "چھوٹے حروف (a-z)",
        'generator_digits': "اعداد (0-9)",
        'generator_symbols': "خاص علامات (!@#$%^&*)",
        'generator_exclude': "خارج کریں:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "ماسٹر پاس ورڈ درکار ہے",
        'master_password_setup': "ماسٹر پاس ورڈ مرتب کریں",
        'master_password_change': "ماسٹر پاس ورڈ تبدیل کریں",
        'master_password_enter': "براہ کرم اپنا ماسٹر پاس ورڈ ٹائپ کریں",
        'master_password_choose': "ایک مضبوط ماسٹر پاس ورڈ منتخب کریں (کم از کم 8 حروف)",
        'master_password_new': "براہ کرم اپنا نیا ماسٹر پاس ورڈ ٹائپ کریں",
        'master_password_confirm': "پاس ورڈ کی تصدیق کریں",
        'master_password_authenticate': "تصدیق کریں",
        'master_password_success': "ماسٹر پاس ورڈ کامیابی سے مرتب ہو گیا۔",
        'master_password_changed': "ماسٹر پاس ورڈ کامیابی سے تبدیل ہو گیا۔",
        'master_password_removed': "ماسٹر پاس ورڈ اور تمام پاس ورڈز حذف کر دیے گئے۔",
        'master_password_remove': "ماسٹر پاس ورڈ ہٹائیں",
        'master_password_remove_confirm': "کیا آپ واقعی تمام پاس ورڈز حذف کرنا چاہتے ہیں؟\n\nیہ عمل واپس نہیں لیا جا سکتا!",
        'master_password_export_before': "کیا آپ پہلے بیک اپ نقل برآمد کرنا چاہتے ہیں؟",
        'master_password_export_delete': "برآمد کریں اور حذف کریں",
        'master_password_delete_now': "ابھی حذف کریں",
        'master_password_for_signatures': "دستخط استعمال کرنے کے لیے، آپ کو ماسٹر پاس ورڈ مرتب کرنا ہوگا۔\n\nکیا آپ ابھی ماسٹر پاس ورڈ مرتب کرنا چاہتے ہیں؟",
        'master_password_for_private': "ذاتی متن کے بلاکس استعمال کرنے کے لیے، آپ کو ماسٹر پاس ورڈ مرتب کرنا ہوگا۔\n\nکیا آپ ابھی ماسٹر پاس ورڈ مرتب کرنا چاہتے ہیں؟",
        'master_password_info': """
            <b>🔐 ماسٹر پاس ورڈ کے بغیر:</b><br>
            • پاس ورڈ دیکھنا، نقل کرنا اور برآمد کرنا ممکن نہیں<br>
            • پاس ورڈ حذف کرنا ہمیشہ ممکن ہے (ماسٹر پاس ورڈ کے بغیر بھی)<br><br>

            <b>🔐 ماسٹر پاس ورڈ کے ساتھ:</b><br>
            • تصدیق کے بعد تمام افعال دستیاب ہیں<br>
            • پاس ورڈ ماسٹر پاس ورڈ سے خفیہ کیے جاتے ہیں<br>
            • کم از کم لمبائی: 8 حروف<br>
            • محفوظ SHA-256 ہیش اسٹوریج<br><br>

            <b>اہم:</b><br>
            • ماسٹر پاس ورڈ کھو جانے پر: پاس ورڈز بحال نہیں کیے جا سکتے<br>
            • ماسٹر پاس ورڈ ہٹانے پر: تمام پاس ورڈز حذف ہو جائیں گے<br>
            • حذف کرنے سے پہلے برآمد کرنے کا اختیار دستیاب ہے<br>
            • ماسٹر پاس ورڈ کسی بھی وقت تبدیل کیا جا سکتا ہے
        """,
        'signature_auth_disabled': "دستخطوں کے لیے پاس ورڈ پوچھنا غیر فعال کریں",
        'template_auth_disabled': "ذاتی متن کے بلاکس کے لیے پاس ورڈ پوچھنا غیر فعال کریں",
        'master_password_for_signatures_settings': "دستخط استعمال کرنے کے لیے، آپ کو ماسٹر پاس ورڈ مرتب کرنا ہوگا۔\n\nاس کے لیے ترتیبات - پاس ورڈ کا انتظام پر جائیں",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF محفوظ کریں",
        'protect_info': "فائل '{0}' کو پاس ورڈ سے محفوظ کیا جائے گا۔",
        'protect_instruction': "براہ کرم دستاویز کو محفوظ کرنے کے لیے مطلوبہ پاس ورڈ دو بار ٹائپ کریں، یا ان پٹ فیلڈ کے دائیں جانب پاس ورڈ جنریٹر استعمال کریں۔",
        'protect_success': "PDF کامیابی سے محفوظ کر کے یہاں محفوظ کی گئی:\n{0}\n\nپاس ورڈ: {1}\n\nکیا آپ اب محفوظ شدہ PDF کھولنا چاہتے ہیں؟",
        'protect_open': "ہاں",
        'protect_skip': "نہیں",
        'protect_error': "PDF محفوظ کرتے وقت خرابی",
        'protect_open_title': "محفوظ شدہ PDF کھولیں",
        'protect_question': "مکمل۔ کیا آپ اب محفوظ شدہ PDF کھولنا چاہتے ہیں؟ ہاں یا نہیں؟",
        'password_cancel': "پاس ورڈ ڈائیلاگ منسوخ کر دیا گیا",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "صفحات حذف کریں",
        'pages_extract': "صفحات نکالیں",
        'pages_insert': "صفحات داخل کریں",
        'pages_move': "صفحات منتقل کریں",
        'pages_delete_options': "حذف کرنے کے اختیارات",
        'pages_delete_empty': "تمام خالی صفحات حذف کریں",
        'pages_delete_current': "موجودہ صفحہ حذف کریں",
        'pages_delete_range': "صفحات کی حد حذف کریں",
        'pages_extract_options': "نکالنے کے اختیارات",
        'pages_extract_current': "موجودہ صفحہ نکالیں",
        'pages_extract_range': "صفحات کی حد نکالیں",
        'pages_insert_position': "داخل کرنے کی جگہ",
        'pages_insert_before': "صفحہ سے پہلے داخل کریں:",
        'pages_insert_select': "PDF منتخب کریں",
        'pages_insert_none': "کوئی PDF منتخب نہیں کی گئی",
        'pages_move_source': "منتقل کرنے کے لیے صفحات",
        'pages_move_from': "صفحہ سے:",
        'pages_move_to': "صفحہ تک:",
        'pages_move_target': "ہدف کی جگہ",
        'pages_move_before': "صفحہ سے پہلے منتقل کریں:",
        'pages_move_hint': "نوٹ: صفحہ 1 = شروع، {0} = آخر",
        'pages_range_invalid': "شروع کا صفحہ آخر کے صفحہ سے چھوٹا یا برابر ہونا چاہیے۔",
        'pages_position_invalid': "ہدف کی جگہ منتقل کی جانے والی حد کے اندر نہیں ہو سکتی۔",
        'pages_no_pdf_selected': "کوئی PDF منتخب نہیں کی گئی۔",
        'pages_deleted': "{0} صفحات حذف کر دیے گئے۔",
        'pages_extracted': "نکالے گئے: {0}\nمحفوظ کیے گئے: {1}\nفائل کا سائز: {2:.1f} KB",
        'pages_inserted': "{0} صفحات داخل کر دیے گئے",
        'pages_moved': "{0} صفحات منتقل کر دیے گئے۔",
        'pages_deleted_none': "کوئی صفحات حذف نہیں کیے گئے۔",
        'pages_delete_progress': "صفحات حذف کیے جا رہے ہیں...",
        'pages_deleted_with_backup': "{0} صفحات حذف کر دیے گئے۔\n\nبیک اپ: {1}",
        'pages_deleted_voice': "ایک بیک اپ بنایا گیا اور {0} صفحات حذف کر دیے گئے۔",
        'info': "نوٹ",
        'error_dialog_creation': "ڈائیلاگ نہیں بنایا جا سکا",
        'extract_page_single': "صفحہ {0} نکالیں",
        'extract_page_range': "صفحات {0}-{1} نکالیں",
        'extract_success_voice': "صفحات کامیابی سے نکالے گئے",
        'extract_error_format': "نکالتے وقت خرابی: {0}",
        'pages_inserted_voice': "{0} صفحات داخل کر دیے گئے۔",
        'insert_error_format': "داخل کرتے وقت خرابی: {0}",
        'pages_move_progress': "صفحات منتقل کیے جا رہے ہیں...",
        'pages_moved_with_backup': "{0} صفحات منتقل کر دیے گئے۔\n\nبیک اپ: {1}",
        'move_success_title': "کامیابی سے منتقل کر دیے گئے",
        'pages_moved_voice': "{0} صفحات کامیابی سے منتقل کر دیے گئے",
        'mark_removed': "صفحہ {0} سے نشان ہٹا دیا گیا",
        'mark_empty': "صفحہ {0} کو خالی کے طور پر نشان زد کیا گیا",
        'mark_export_removed': "صفحہ {0} سے برآمد کا نشان ہٹا دیا گیا",
        'mark_export': "صفحہ {0} برآمد کے لیے نشان زد کیا گیا",
        'no_empty_pages': "حذف کرنے کے لیے کوئی خالی صفحات نشان زد نہیں",
        'delete_empty_confirm': "کیا آپ تمام {0} نشان زد خالی صفحات حذف کرنا چاہتے ہیں؟",
        'delete_empty_confirm_voice': "اب تمام {0} نشان زد خالی صفحات حذف کریں؟ ہاں یا نہیں۔",
        'empty_pages_deleted': "{0} خالی صفحات حذف کر دیے گئے",
        'no_export_pages': "برآمد کے لیے کوئی صفحات نشان زد نہیں",
        'overwrite_title': "موجودہ فائل پر لکھیں",
        'overwrite_question': "فائل\n\n{0}\n\nپہلے سے موجود ہے۔\nکیا آپ اس پر لکھنا چاہتے ہیں؟",
        'overwrite_voice': "پہلے سے موجود فائل پر لکھیں؟ ہاں یا نہیں۔",
        'page_skipped': "صفحہ {0} چھوڑ دیا گیا",
        'export_complete': "برآمد مکمل۔",
        'export_complete_voice': "برآمد مکمل ہو گئی۔",
        'no_pages_exported': "کوئی صفحہ برآمد نہیں کیا گیا",
        'export_cancelled': "برآمد منسوخ کر دی گئی",
        'pages_exported': "{0} صفحات {1} میں برآمد کیے گئے",
        'export_page_title': "صفحہ برآمد کریں",
        'page_exported': "صفحہ {0} {1} میں برآمد کیا گیا",
        'export_error': "برآمد کرتے وقت خرابی",
        'export_marked_title': "نشان زد صفحات برآمد کریں",
        'rotate_all_title': "تمام صفحات گھمائیں",
        'rotate_all_question': "کیا آپ تمام صفحات کو 90 ڈگری دائیں طرف گھمانا چاہتے ہیں؟",
        'rotate_all_voice': "کیا آپ تمام صفحات کو 90 ڈگری دائیں طرف گھمانا چاہتے ہیں؟ ہاں یا نہیں؟",
        'all_pages_rotated': "تمام صفحات گھما دیے گئے",
        'page_rotated': "صفحہ {0} گھما دیا گیا",
        'rotate_error': "صفحہ نہیں گھمایا جا سکا",
        'delete_page_confirm': "کیا آپ صفحہ {0} حذف کرنا چاہتے ہیں؟",
        'delete_page_confirm_voice': "کیا آپ واقعی صفحہ {0} حذف کرنا چاہتے ہیں؟ ہاں یا نہیں۔",
        'page_deleted': "صفحہ {0} حذف کر دیا گیا",
        'delete_error': "صفحہ حذف نہیں کیا جا سکا",
        'pages_deleted_voice': "{0} صفحات حذف کر دیے گئے",
        'pages_exported_split': "{0} صفحات کامیابی سے برآمد کیے گئے۔",
        'pages_skipped': "{0} صفحات چھوڑ دیے گئے۔",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "صفحات نکالیں (اعلیٰ)",
        'pdf_splitter_title': "PDF سپلٹر اور نکالنے والا",
        'pdf_splitter_load': " PDF فائل منتخب کریں",
        'pdf_splitter_info': "براہ کرم اپنی PDF دستاویز کے لیے ایک آپشن منتخب کریں",
        'pdf_splitter_basic': "بنیادی آپریشنز",
        'pdf_splitter_single': "ہر صفحے کو الگ فائل میں تقسیم کریں",
        'pdf_splitter_range': "صفحات نکالیں:",
        'pdf_splitter_range_placeholder': "مثلاً 1-3,5,7-9",
        'pdf_splitter_clean': "صفائی کے آپریشنز",
        'pdf_splitter_remove_empty': "تمام خالی صفحات ہٹائیں",
        'pdf_splitter_remove': "صفحات کی حد حذف کریں:",
        'pdf_splitter_remove_placeholder': "مثلاً 2,4-6",
        'pdf_splitter_process': "PDF پر کارروائی کریں",
        'pdf_splitter_loaded': "PDF لوڈ ہو گئی۔ براہ کرم ایک آپشن منتخب کریں",
        'pdf_read_error': "PDF نہیں پڑھی جا سکی",
        'pages': "صفحات",
        'pages_created': "صفحات بنائے گئے",
        'range_empty': "براہ کرم صفحات کی حد ٹائپ کریں",
        'range_invalid': "غلط صفحات کی حد",
        'range_created': "منتخب کردہ صفحات کے ساتھ نئی PDF بنائی گئی:\n{0}",
        'empty_removed': "{0} خالی صفحات ہٹا دیے گئے۔\nآؤٹ پٹ: {1}",
        'remove_empty': "براہ کرم ہٹانے کے لیے صفحات ٹائپ کریں",
        'remove_invalid': "ہٹانے کے لیے غلط صفحات",
        'remove_done': "صفائی شدہ PDF بنائی گئی:\n{0}",
        'open_folder': "فولڈر کھولیں",
        'show_in_finder': "فائنڈر میں دکھائیں",
        'pdf_splitter_no_pdf': "براہ کرم پہلے PDF فائل لوڈ کریں۔",
        'process_error': "PDF پر کارروائی کرتے وقت خرابی",
        'pages_created_voice': "{0} صفحات بنائے گئے",
        'range_created_voice': "منتخب کردہ صفحات کے ساتھ PDF بنائی گئی",
        'empty_removed_voice': "{0} خالی صفحات ہٹا دیے گئے",
        'remove_done_voice': "صفائی شدہ PDF بنائی گئی",
        'pdf_splitter_split_groups': "ہر متصل گروپ کو الگ فائل میں",
        'range_created_single': "نئی PDF بنائی گئی:\n{0}",
        'range_created_multiple': "{0} PDF فائلیں بنائی گئیں۔",
        'range_created_voice_single': "منتخب کردہ صفحات کے ساتھ ایک PDF بنائی گئی",
        'range_created_voice_multiple': "{0} PDF فائلیں بنائی گئیں",
        'empty_removed_none_left': "کوئی صفحہ باقی نہیں",
        'empty_removed_all_empty': "تمام صفحات خالی پائے گئے اور ہٹا دیے جائیں گے۔ کوئی فائل نہیں بنائی گئی۔",
        'preview_single': "پیش منظر: {0}",
        'preview_enter_range': "براہ کرم صفحات کی حد ٹائپ کریں۔",
        'preview_invalid_range': "غلط صفحات کی حد۔",
        'preview_file': "پیش منظر: {0}",
        'preview_files': "پیش منظر: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "پرنٹنگ کا عمل شروع ہو رہا ہے",
        'print_sent': "پرنٹ جاب بھیج دی گئی",
        'print_now': "ابھی پرنٹ کریں",
        'print_error': "فوری پرنٹ میں خرابی",
        'print_limited': "اس سسٹم پر پرنٹ فنکشن محدود ہے",
        'print_error_format': "فوری پرنٹ میں خرابی: {0}",
        'warning': "نوٹ",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "روشن موڈ میں سوئچ کریں",
        'mode_switch_to_dark': "تاریک موڈ میں سوئچ کریں",
        'mode_dark_activated': "تاریک موڈ فعال ہو گیا",
        'mode_light_activated': "روشن موڈ فعال ہو گیا",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "مکمل منظر",
        'zoom_two_pages': "دو صفحات ساتھ ساتھ",
        'zoom_overview': "جائزہ موڈ",
        'zoom_cannot_during_search': "تلاش کے دوران زوم ممکن نہیں",
        'zoom_exit_first': "براہ کرم پہلے زوم ختم کریں",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "ڈریگ اینڈ ڈراپ فعال",
        'drag_disabled': "ڈریگ اینڈ ڈراپ غیر فعال",
        'drag_page_grab': "صفحہ {0} پکڑیں",
        'drag_page_dropped': "صفحہ {0} پوزیشن {1} پر داخل کر دیا گیا",
        'drag_position_invalid': "غلط پوزیشن",
        'drag_same_position': "صفحہ {0} پوزیشن {0} پر ہے",
        'drag_error': "منتقل کرتے وقت خرابی",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "اعلیٰ فارمیٹنگ اور متن کے بلاک کے انتظام کے ساتھ متن کا اندراج",
        'text_templates': "دستیاب متن کے بلاکس:",
        'text_name': "نام",
        'text_preview': "متن کا پیش منظر",
        'text_enter': "متن:",
        'text_font_size': "فونٹ کا سائز:",
        'text_formatting': "فارمیٹنگ:",
        'text_bold': "موٹا",
        'text_italic': "ترچھا",
        'text_underline': "زیر خط",
        'text_alignment': "ترتیب:",
        'text_left': "بائیں",
        'text_center': "مرکز",
        'text_right': "دائیں",
        'text_color': "متن کا رنگ:",
        'text_opacity': "دھندلاپن:",
        'text_word_wrap': "لائن بریک:",
        'text_auto': "خودکار",
        'text_page_width_95': "صفحے کی چوڑائی (95%)",
        'text_page_width_85': "بہت چوڑا (85%)",
        'text_page_width_75': "چوڑا (75%)",
        'text_page_width_60': "چوڑا (60%)",
        'text_page_width_50': "درمیانہ (50%)",
        'text_page_width_30': "تنگ (30%)",
        'text_page_width_20': "تنگ (20%)",
        'text_page_width_10': "بہت تنگ (10%)",
        'text_no_wrap': "کوئی بریک نہیں",
        'text_private': "ذاتی متن کا بلاک (تصدیق درکار ہے)",
        'text_preview_label': "پیش منظر:",
        'text_preview_placeholder': "یہاں متن کا پیش منظر دکھایا جائے گا...",
        'text_no_text': "(کوئی متن نہیں)",
        'text_save_template': "💾 بلاک کے طور پر محفوظ کریں",
        'text_delete_template': "🗑 منتخب کردہ متن کا بلاک حذف کریں",
        'text_show_private': "ذاتی دکھائیں",
        'text_hide_private': "ذاتی چھپائیں",
        'text_use': "✅ متن استعمال کریں",
        'text_saved': "متن کا بلاک بطور محفوظ کیا گیا:\n{0}",
        'text_saved_voice': "متن کا بلاک محفوظ کر دیا گیا",
        'text_deleted': "متن کا بلاک حذف کر دیا گیا",
        'text_no_text_to_save': "محفوظ کرنے کے لیے کوئی متن نہیں۔",
        'text_no_templates': "کوئی متن کے بلاک نہیں ملے",
        'text_private_master_required': "ذاتی بلاکس صرف اس صورت میں استعمال کیے جا سکتے ہیں جب ماسٹر پاس ورڈ مرتب کیا گیا ہو۔\n\nکیا آپ ابھی ماسٹر پاس ورڈ مرتب کرنا چاہتے ہیں؟",
        'text_filename': "متن کے بلاک کے لیے فائل کا نام ('Text_' اور '.txt' کے بغیر):",
        'text_filename_hint': "مثال: 'Telefon HomeOffice' 'Text_Telefon HomeOffice.txt' کے طور پر محفوظ کیا جائے گا",
        'text_save_hint': "متن کا بلاک خودکار طور پر فارمیٹنگ کے ساتھ محفوظ کیا جائے گا۔",
        'text_guide_title': "متن کا اندراج - رہنما",
        'text_delete_confirm': "کیا آپ واقعی متن کا بلاک حذف کرنا چاہتے ہیں؟\n\nفائل: {0}\nمتن: {1}...",
        'text_make_public': "عوامی کے طور پر نشان زد کریں",
        'text_make_private': "ذاتی کے طور پر نشان زد کریں",
        'text_privacy_changed': "رازداری کی حالت تبدیل کر دی گئی",
        'text_private_always': "ذاتی ہمیشہ نظر آئیں (ترتیب)",
        'text_mode_required': "براہ کرم پہلے متن موڈ فعال کریں",
        'text_continue_editing': "ترمیم جاری رکھیں - کرسر متن کے آخر میں",
        'text_no_input': "کوئی متن داخل نہیں کیا گیا - متن مسترد کر دیا گیا",
        'save_dialog_question': "آپ کیسے آگے بڑھنا چاہتے ہیں؟",
        'text_save_question': "تمام متن اور کراس محفوظ کریں، ایڈجسٹ کریں، ترمیم جاری رکھیں یا مسترد کریں؟",
        'copy_cross': "کراس نقل کر دیا گیا",
        'paste_cross': "کراس چسپاں کر دیا گیا",
        'paste_text': "متن چسپاں کر دیا گیا",
        'cross_discarded': "کراس مسترد کر دیا گیا",
        'all_discarded': "سب مسترد کر دیے گئے",
        'text_discarded': "متن مسترد کر دیا گیا",
        'no_texts_to_save': "محفوظ کرنے کے لیے کوئی متن نہیں",
        'no_valid_texts': "محفوظ کرنے کے لیے کوئی درست متن نہیں",
        'text_word_singular': "متن",
        'text_word_plural': "متون",
        'cross_word_singular': "کراس",
        'cross_word_plural': "کراسز",
        'texts_saved_title': "متون محفوظ کر دیے گئے",
        'texts_crosses_saved': "{0} {1} اور {2} {3} PDF میں داخل کر دیے گئے۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'texts_crosses_saved_voice': "{0} {1} اور {2} {3} محفوظ کر دیے گئے۔",
        'texts_saved': "{0} {1} PDF میں داخل کر دیے گئے۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'texts_saved_voice': "{0} {1} محفوظ کر دیے گئے۔",
        'crosses_saved': "{0} {1} PDF میں داخل کر دیے گئے۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'crosses_saved_voice': "{0} {1} محفوظ کر دیے گئے۔",
        'elements_saved': "{0} عناصر PDF میں داخل کر دیے گئے۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'elements_saved_voice': "{0} عناصر محفوظ کر دیے گئے۔",
        'text_window_load_error': "متن کی ونڈو لوڈ نہیں کی جا سکی",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **متن کا اندراج اور متن کے بلاکس – تفصیلی رہنما**

        **1. متن داخل کریں اور ترمیم کریں**
        - دستاویز میں مطلوبہ جگہ پر دائیں کلک کریں اور "متن داخل کریں" منتخب کریں۔
        - ایک ڈائیلاگ کھلے گا جہاں آپ اپنا متن ٹائپ کر سکتے ہیں اور فارمیٹ کر سکتے ہیں:
        • فونٹ کا سائز، موٹا، ترچھا، زیر خط
        • متن کا رنگ (آزادانہ طور پر منتخب کیا جا سکتا ہے)
        • سلائیڈر کے ذریعے دھندلاپن
        • لائن بریک (مختلف چوڑائیاں، مثلاً صفحے کی چوڑائی، تنگ، کوئی بریک نہیں)
        - تصدیق کے بعد، متن کلک کی گئی جگہ پر ظاہر ہوگا۔ آپ اسے ماؤس یا تیر والی کلیدوں سے منتقل کر سکتے ہیں۔
        - متن پر ڈبل کلک کرنے سے ترمیم موڈ کھل جاتا ہے؛ ESC سے باہر نکلیں۔

        **2. متن کے بلاکس (ٹیمپلیٹس) کا انتظام کریں**
        - متن کے ڈائیلاگ میں آپ بائیں جانب تمام محفوظ کردہ متن کے بلاکس کی فہرست دیکھیں گے۔
        - **بلاک محفوظ کرنا:** اپنا متن ٹائپ کریں، فارمیٹ کریں اور "💾 بلاک کے طور پر محفوظ کریں" پر کلک کریں۔ ایک فائل کا نام ٹائپ کریں (بغیر ایکسٹینشن کے)۔
        - **بلاک لوڈ کرنا:** فہرست میں مطلوبہ نام پر کلک کریں۔ متن اور فارمیٹنگ لے لی جائے گی اور ضرورت پڑنے پر ایڈجسٹ کی جا سکتی ہے۔
        - **حذف کرنا:** ایک بلاک پر دائیں کلک کر کے آپ اسے حذف کر سکتے ہیں یا اس کی ذاتی حیثیت تبدیل کر سکتے ہیں۔

        **3. ذاتی متن کے بلاکس (ماسٹر پاس ورڈ)**
        - اگر آپ نے ماسٹر پاس ورڈ مرتب کیا ہے (ترتیبات → پاس ورڈ کا انتظام کے تحت)، تو آپ بلاکس کو "ذاتی" کے طور پر نشان زد کر سکتے ہیں۔
        - محفوظ کرنے سے پہلے ڈائیلاگ میں "ذاتی متن کا بلاک" چیک باکس کو فعال کریں۔
        - ذاتی بلاکس فہرست میں صرف اس وقت دکھائے جائیں گے جب آپ ہر سیشن میں ایک بار اپنا ماسٹر پاس ورڈ داخل کریں گے (تالے کے آئیکن کے ذریعے یا پہلی رسائی پر تصدیق)۔
        - اس طرح آپ خفیہ متن کے بلاکس کو غیر مجاز رسائی سے بچا سکتے ہیں۔

        **4. کراس داخل کریں**
        - سیاق و سباق کے مینو کے ذریعے آپ ایک گرافیکل کراس بھی داخل کر سکتے ہیں (مثلاً چیک باکسز کے لیے)۔
        - کراس کا سائز، لائن کی موٹائی اور رنگ آپ ترتیبات میں عالمی طور پر ایڈجسٹ کر سکتے ہیں (مینو "ترتیبات" → "کراس کی ترتیبات")۔
        - موجودہ کراس پر دائیں کلک کر کے آپ اسے انفرادی طور پر تبدیل کر سکتے ہیں۔

        **5. اجتماعی اقدامات**
        - اگر آپ نے ایک صفحے پر متعدد متن یا کراس رکھے ہیں، تو سیاق و سباق کے مینو کے ذریعے (متن موڈ میں دائیں کلک) آپ تمام عناصر کو ایک ساتھ محفوظ یا مسترد کر سکتے ہیں۔
        - محفوظ کرتے وقت، تمام عناصر PDF میں ایمبیڈ ہو جاتے ہیں اور ویکٹر گرافک کے طور پر رہتے ہیں۔

        **6. متن موڈ میں کی بورڈ شارٹ کٹس**
        - تیر والی کلیدیں: عنصر کو منتقل کریں
        - Ctrl+تیر والی کلیدیں: بڑے اقدامات میں منتقل کریں
        - Enter: محفوظ کرنے کا ڈائیلاگ کھولیں (سب محفوظ کریں / ایڈجسٹ کریں / مسترد کریں)
        - ESC: موجودہ عنصر کو مسترد کریں
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 متن کا اندراج اور متن کے بلاکس – تفصیلی رہنما</strong></p>

        <p><strong>1. متن داخل کریں اور ترمیم کریں</strong></p>
        <ul>
        <li>دستاویز میں مطلوبہ جگہ پر دائیں کلک کریں اور "متن داخل کریں" منتخب کریں۔</li>
        <li>ایک ڈائیلاگ کھلے گا جہاں آپ اپنا متن ٹائپ کر سکتے ہیں اور فارمیٹ کر سکتے ہیں:<br/>
        • فونٹ کا سائز، موٹا، ترچھا، زیر خط<br/>
        • متن کا رنگ (آزادانہ طور پر منتخب کیا جا سکتا ہے)<br/>
        • سلائیڈر کے ذریعے دھندلاپن<br/>
        • لائن بریک (مختلف چوڑائیاں، مثلاً صفحے کی چوڑائی، تنگ، کوئی بریک نہیں)</li>
        <li>تصدیق کے بعد، متن کلک کی گئی جگہ پر ظاہر ہوگا۔ آپ اسے ماؤس یا تیر والی کلیدوں سے منتقل کر سکتے ہیں۔</li>
        <li>متن پر ڈبل کلک کرنے سے ترمیم موڈ کھل جاتا ہے؛ ESC سے باہر نکلیں۔</li>
        </ul>

        <p><strong>2. متن کے بلاکس (ٹیمپلیٹس) کا انتظام کریں</strong></p>
        <ul>
        <li>متن کے ڈائیلاگ میں آپ بائیں جانب تمام محفوظ کردہ متن کے بلاکس کی فہرست دیکھیں گے۔</li>
        <li><strong>بلاک محفوظ کرنا:</strong> اپنا متن ٹائپ کریں، فارمیٹ کریں اور "💾 بلاک کے طور پر محفوظ کریں" پر کلک کریں۔ ایک فائل کا نام ٹائپ کریں (بغیر ایکسٹینشن کے)۔</li>
        <li><strong>بلاک لوڈ کرنا:</strong> فہرست میں مطلوبہ نام پر کلک کریں۔ متن اور فارمیٹنگ لے لی جائے گی اور ضرورت پڑنے پر ایڈجسٹ کی جا سکتی ہے۔</li>
        <li><strong>حذف کرنا:</strong> ایک بلاک پر دائیں کلک کر کے آپ اسے حذف کر سکتے ہیں یا اس کی ذاتی حیثیت تبدیل کر سکتے ہیں۔</li>
        </ul>

        <p><strong>3. ذاتی متن کے بلاکس (ماسٹر پاس ورڈ)</strong></p>
        <ul>
        <li>اگر آپ نے ماسٹر پاس ورڈ مرتب کیا ہے (ترتیبات → پاس ورڈ کا انتظام کے تحت)، تو آپ بلاکس کو "ذاتی" کے طور پر نشان زد کر سکتے ہیں۔</li>
        <li>محفوظ کرنے سے پہلے ڈائیلاگ میں "ذاتی متن کا بلاک" چیک باکس کو فعال کریں۔</li>
        <li>ذاتی بلاکس فہرست میں صرف اس وقت دکھائے جائیں گے جب آپ ہر سیشن میں ایک بار اپنا ماسٹر پاس ورڈ داخل کریں گے (تالے کے آئیکن کے ذریعے یا پہلی رسائی پر تصدیق)۔</li>
        <li>اس طرح آپ خفیہ متن کے بلاکس کو غیر مجاز رسائی سے بچا سکتے ہیں۔</li>
        </ul>

        <p><strong>4. کراس داخل کریں</strong></p>
        <ul>
        <li>سیاق و سباق کے مینو کے ذریعے آپ ایک گرافیکل کراس بھی داخل کر سکتے ہیں (مثلاً چیک باکسز کے لیے)۔</li>
        <li>کراس کا سائز، لائن کی موٹائی اور رنگ آپ ترتیبات میں عالمی طور پر ایڈجسٹ کر سکتے ہیں (مینو "ترتیبات" → "کراس کی ترتیبات")۔</li>
        <li>موجودہ کراس پر دائیں کلک کر کے آپ اسے انفرادی طور پر تبدیل کر سکتے ہیں۔</li>
        </ul>

        <p><strong>5. اجتماعی اقدامات</strong></p>
        <ul>
        <li>اگر آپ نے ایک صفحے پر متعدد متن یا کراس رکھے ہیں، تو سیاق و سباق کے مینو کے ذریعے (متن موڈ میں دائیں کلک) آپ تمام عناصر کو ایک ساتھ محفوظ یا مسترد کر سکتے ہیں۔</li>
        <li>محفوظ کرتے وقت، تمام عناصر PDF میں ایمبیڈ ہو جاتے ہیں اور ویکٹر گرافک کے طور پر رہتے ہیں۔</li>
        </ul>

        <p><strong>6. متن موڈ میں کی بورڈ شارٹ کٹس</strong></p>
        <ul>
        <li>تیر والی کلیدیں: عنصر کو منتقل کریں</li>
        <li>Ctrl+تیر والی کلیدیں: بڑے اقدامات میں منتقل کریں</li>
        <li>Enter: محفوظ کرنے کا ڈائیلاگ کھولیں (سب محفوظ کریں / ایڈجسٹ کریں / مسترد کریں)</li>
        <li>ESC: موجودہ عنصر کو مسترد کریں</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "کراس کی ترتیبات",
        'cross_properties': "کراس کی خصوصیات",
        'cross_size': "سائز (px):",
        'cross_line_width': "لائن کی موٹائی:",
        'cross_color': "رنگ:",
        'cross_choose_color': "منتخب کریں",
        'cross_fine_tuning': "محفوظ کرتے وقت باریک ایڈجسٹمنٹ (پکسلز)",
        'cross_offset_x': "X-آفسیٹ:",
        'cross_offset_y': "Y-آفسیٹ:",
        'cross_offset_x_tooltip': "منفی اقدار محفوظ کرتے وقت کراس کو بائیں طرف منتقل کرتی ہیں، مثبت اقدار دائیں طرف",
        'cross_offset_y_tooltip': "منفی اقدار محفوظ کرتے وقت کراس کو اوپر منتقل کرتی ہیں، مثبت اقدار نیچے",
        'cross_preview': "پیش منظر",
        'cross_save': "ترتیبات لاگو کریں",
        'cross_customized': "کراس ایڈجسٹ کر دیا گیا",
        'cross_settings_applied': "کراس کی ترتیبات محفوظ کر دی گئیں۔\nسائز: {0}px، لائن کی موٹائی: {1}px\n{2}",
        'cross_updated_count': "{0} موجودہ کراسز اپ ڈیٹ کر دیے گئے۔",
        'cross_no_crosses': "کوئی موجودہ کراسز نہیں ملے۔",
        'cross_settings_applied_all': "تمام {0} کراسز کے لیے کراس کی ترتیبات لاگو کر دی گئیں",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "دستخط کی ترتیبات",
        'signature_1': "دستخط 1",
        'signature_2': "دستخط 2",
        'signature_select': "دستخط منتخب کریں",
        'signature_add': "➕ نیا دستخط شامل کریں...",
        'signature_size': "دستخط {0} کے لیے سائز (%):",
        'signature_common': "عام ترتیبات",
        'signature_timestamp': "خودکار طور پر ٹائم اسٹیمپ شامل کریں",
        'signature_location': "طے شدہ مقام:",
        'signature_timestamp_size': "ٹائم اسٹیمپ فونٹ کا سائز:",
        'signature_no_files': "-- کوئی دستخط نہیں ملے --",
        'signature_insert': "دستخط داخل کریں",
        'signature_insert_1': "دستخط 1 داخل کریں",
        'signature_insert_2': "دستخط 2 داخل کریں",
        'signature_customize': " دستخط ایڈجسٹ کریں",
        'signature_discard': " یہ دستخط مسترد کریں",
        'signature_save_all': " تمام دستخط محفوظ کریں",
        'signature_discard_all': " تمام دستخط مسترد کریں",
        'signature_guide_title': "دستخط - رہنما",
        'signature_guide': """
📝 دستخط - مختصر رہنما

- ماسٹر پاس ورڈ مرتب کریں
- مینو ترتیبات میں دستخط ترتیب دیں
  (سائز، ٹائم اسٹیمپ ...)
- مطلوبہ جگہ پر دائیں کلک کے ذریعے داخل کریں
  (ہر سیشن میں ایک بار ماسٹر پاس ورڈ درکار ہے)
- ماؤس یا تیر والی کلیدوں سے دستخط منتقل کریں
- ایک کے بعد ایک متعدد دستخط داخل کیے جا سکتے ہیں
- ہر دستخط کو انفرادی طور پر ایڈجسٹ کیا جا سکتا ہے
- ایک دستخط مسترد کریں
- تمام دستخط ایک ساتھ محفوظ کریں / مسترد کریں
- متبادل طور پر مینو بار بھی استعمال کیا جا سکتا ہے۔
        """,
        'signature_placeholder': "کوئی پیش منظر دستیاب نہیں",
        'signature_info': "دستخط {0}: {1}×{2} px ({3}% of {4}×{5})",
        'signature_info_placeholder': "دستخط {0} کے لیے ترتیبات",
        'signature_inserted': "دستخط {0} صفحہ {1} پر داخل کر دیا گیا",
        'signature_deleted': "دستخط حذف کر دیا گیا",
        'signature_copied': "دستخط نقل کر دیا گیا",
        'signature_pasted': "دستخط {0} داخل کر دیا گیا",
        'signature_saved': "{0} دستخط PDF میں داخل کر دیے گئے۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'signature_saved_voice': "{0} دستخط محفوظ کر دیے گئے",
        'mode_replace_signature_format': "موڈ ختم کریں اور دستخط {0} داخل کریں",
        'mode_conflict_voice_signature': "{0} موڈ فعال ہے۔ ختم کر کے دستخط داخل کریں؟",
        'signature_not_configured': "دستخط {0} ترتیب نہیں دیا گیا",
        'signature_file_not_found': "دستخط کی فائل نہیں ملی",
        'timestamp_format': "{0}، {1} کو",
        'no_copied_signature': "کوئی نقل شدہ دستخط نہیں",
        'no_signatures_to_save': "محفوظ کرنے کے لیے کوئی دستخط نہیں",
        'signature_save_question': "تمام دستخط محفوظ کریں، ایڈجسٹ کریں یا اسے مسترد کریں؟",
        'signatures_saved_title': "دستخط محفوظ کر دیے گئے",
        'signatures_saved': "{0} دستخط PDF میں داخل کر دیے گئے۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'signatures_saved_voice': "{0} دستخط محفوظ کر دیے گئے۔",
        'all_signatures_discarded': "تمام دستخط مسترد کر دیے گئے",
        'signature_settings_saved': "دستخط کی ترتیبات محفوظ کر دی گئیں",
        'signature_cancelled': "دستخط مسترد کر دیا گیا",
        'signature_active_title': "دستخط فعال ہے",
        'signature_replace_question': "پہلے سے ایک دستخط فعال ہے۔\n\nکیا آپ موجودہ دستخط کو تبدیل کرنا چاہتے ہیں؟",
        'signature_replace': "دستخط تبدیل کریں",
        'signature_replace_voice': "موجودہ دستخط تبدیل کریں یا منسوخ کریں؟",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "تصویر کی ترتیبات",
        'image_common': "عام تصویر کی ترتیبات",
        'image_keep_aspect': "گھسیٹتے وقت پہلو کا تناسب برقرار رکھیں",
        'image_default_size': "طے شدہ سائز (%):",
        'image_dark_invert': "تاریک موڈ میں تصاویر الٹ دیں",
        'image_dark_invert_tooltip': "فعال: بہتر نمائش کے لیے تصاویر الٹ دی جائیں گی",
        'image_fine_tuning': "باریک ایڈجسٹمنٹ (پکسلز)",
        'image_offset_x': "X-آفسیٹ:",
        'image_offset_y': "Y-آفسیٹ:",
        'image_offset_x_tooltip': "منفی اقدار محفوظ کرتے وقت تصویر کو بائیں طرف منتقل کرتی ہیں، مثبت اقدار دائیں طرف",
        'image_offset_y_tooltip': "منفی اقدار محفوظ کرتے وقت تصویر کو اوپر منتقل کرتی ہیں، مثبت اقدار نیچے",
        'image_select': "تصویر منتخب کریں",
        'image_insert': "تصویر داخل کریں",
        'image_customize': " تصویر ایڈجسٹ کریں",
        'image_aspect': " پہلو کا تناسب برقرار رکھیں",
        'image_discard': " یہ تصویر مسترد کریں",
        'image_save_all': " تمام تصاویر محفوظ کریں",
        'image_discard_all': " تمام تصاویر مسترد کریں",
        'image_filter': "تصاویر",
        'image_guide_title': "تصویر داخل کریں - رہنما",
        'image_guide': """
📷 PDF میں تصویر داخل کریں - مختصر رہنما:

1. مطلوبہ جگہ پر دائیں کلک کریں
2. "تصویر داخل کریں" → تصویر منتخب کریں
3. تصویر کی پوزیشننگ: ماؤس سے گھسیٹیں
4. سائز ایڈجسٹ کریں: کونوں/کناروں پر گھسیٹیں
5. پہلو کا تناسب برقرار رکھیں: [A] کلید
6. مزید ایڈجسٹمنٹ: تصویر پر دائیں کلک کریں

ٹپ: سیاق و سباق کے مینو میں آپ ترتیبات ایڈجسٹ کر سکتے ہیں۔
        """,
        'image_inserted': "تصویر {0} صفحہ {1} پر داخل کر دی گئی",
        'image_deleted': "تصویر مسترد کر دی گئی",
        'image_copied': "تصویر نقل کر دی گئی",
        'image_pasted': "تصویر داخل کر دی گئی",
        'image_saved': "{0} تصاویر PDF میں داخل کر دی گئیں۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'image_saved_voice': "{0} تصاویر محفوظ کر دی گئیں",
        'image_aspect_on': "فعال",
        'image_aspect_off': "غیر فعال",
        'image_aspect_toggle': "پہلو کا تناسب برقرار رکھیں {0}",
        'image_reset': "تصویر اصل سائز پر ری سیٹ کر دی گئی",
        'image_replaced': "تصویر تبدیل کر دی گئی",
        'image_invalid': "کوئی درست تصویر نہیں",
        'mode_replace_image': "تصویر داخل کریں",
        'mode_conflict_voice_image': "{0} موڈ فعال ہے۔ ختم کر کے تصویر داخل کریں؟",
        'image_active_title': "تصویر فعال ہے",
        'image_replace_question': "پہلے سے ایک تصویر فعال ہے۔\n\nکیا آپ موجودہ تصویر کو تبدیل کرنا چاہتے ہیں؟",
        'image_replace': "تصویر تبدیل کریں",
        'image_replace_voice': "موجودہ تصویر تبدیل کریں یا منسوخ کریں؟",
        'image_filter_all': "تصاویر (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;تمام فائلیں (*.*)",
        'no_copied_image': "کوئی نقل شدہ تصویر نہیں",
        'image_discarded': "تصویر مسترد کر دی گئی",
        'image_save_question': "تمام تصاویر محفوظ کریں، ایڈجسٹ کریں یا اسے مسترد کریں؟",
        'no_images_to_save': "محفوظ کرنے کے لیے کوئی تصاویر نہیں",
        'no_valid_images': "محفوظ کرنے کے لیے کوئی درست تصاویر نہیں",
        'images_saved_title': "تصاویر محفوظ کر دی گئیں",
        'images_saved': "{0} تصاویر PDF میں داخل کر دی گئیں۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'images_saved_voice': "{0} تصاویر محفوظ کر دی گئیں۔",
        'all_images_discarded': "تمام تصاویر مسترد کر دی گئیں",
        'image_settings_updated': "تصویر کی ترتیبات اپ ڈیٹ کر دی گئیں",
        'image_replace_title': "نئی تصویر منتخب کریں",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "شکلوں کی ترتیبات",
        'form_basic': "بنیادی ترتیبات",
        'form_default_type': "طے شدہ شکل کی قسم:",
        'form_rectangle': "مستطیل",
        'form_ellipse': "بیضوی",
        'form_line': "لکیر",
        'form_arrow': "تیر",
        'form_line_width': "لکیر کی موٹائی:",
        'form_colors': "رنگ",
        'form_line_color': "لکیر کا رنگ:",
        'form_fill_color': "بھرنے کا رنگ:",
        'form_choose_color': "منتخب کریں",
        'form_transparent': "شفاف پس منظر (صرف لکیر)",
        'form_filled': "بھرا ہوا",
        'form_dark_mode': "تاریک موڈ",
        'form_dark_invert': "تاریک موڈ میں رنگ الٹ دیں",
        'form_fine_tuning': "باریک ایڈجسٹمنٹ (پکسلز)",
        'form_offset_x': "X-آفسیٹ:",
        'form_offset_y': "Y-آفسیٹ:",
        'form_offset_x_tooltip': "منفی اقدار محفوظ کرتے وقت شکل کو بائیں طرف منتقل کرتی ہیں، مثبت اقدار دائیں طرف",
        'form_offset_y_tooltip': "منفی اقدار محفوظ کرتے وقت شکل کو اوپر منتقل کرتی ہیں، مثبت اقدار نیچے",
        'form_preview': "پیش منظر",
        'form_insert': "شکل داخل کریں",
        'form_rectangle_insert': "مستطیل",
        'form_ellipse_insert': "بیضوی/دائرہ",
        'form_line_insert': "لکیر (2 کلک)",
        'form_arrow_insert': "تیر (2 کلک)",
        'form_customize': " شکل ایڈجسٹ کریں",
        'form_transparent_toggle': " شفاف پس منظر",
        'form_discard': " یہ شکل مسترد کریں",
        'form_save_all': " تمام شکلیں محفوظ کریں",
        'form_discard_all': " تمام شکلیں مسترد کریں",
        'form_guide_title': "شکلیں داخل کریں - رہنما",
        'form_guide': """
📐 PDF میں شکلیں داخل کریں - مختصر رہنما:

1. شکل کی قسم منتخب کریں (مستطیل، بیضوی، لکیر، تیر)
2. پوزیشن پر کلک کریں
   - مستطیل/بیضوی کے لیے: ایک کلک شکل رکھتا ہے
   - لکیر/تیر کے لیے: شروع اور اختتامی نقطہ کے لیے دو کلک
3. شکل کی پوزیشننگ: ماؤس سے گھسیٹیں
4. سائز ایڈجسٹ کریں: کونوں/کناروں پر گھسیٹیں
5. شکل محفوظ کریں: Enter
6. شکل مسترد کریں: ESC
7. مزید ایڈجسٹمنٹ: شکل پر دائیں کلک کریں

ٹپ: سیاق و سباق کے مینو میں آپ ترتیبات ایڈجسٹ کر سکتے ہیں۔
        """,
        'form_inserted': "{0} صفحہ {1} پر داخل کر دیا گیا",
        'form_deleted': "شکل حذف کر دی گئی",
        'form_copied': "شکل نقل کر دی گئی",
        'form_pasted': "شکل داخل کر دی گئی",
        'form_saved': "{0} شکلیں PDF میں داخل کر دی گئیں۔\n\nPDF دوبارہ لوڈ ہو رہی ہے...",
        'form_saved_voice': "{0} شکلیں محفوظ کر دی گئیں",
        'form_reset': "شکل طے شدہ سائز پر ری سیٹ کر دی گئی",
        'form_transparent_on': "فعال",
        'form_transparent_off': "غیر فعال",
        'form_transparent_toggled': "شفاف پس منظر {0}",
        'form_line_cancel': "لکیر کھینچنا منسوخ کر دیا گیا",
        'form_second_click': "اب {0} کے لیے اختتامی نقطہ پر کلک کریں",
        'mode_replace_form': "شکل داخل کریں",
        'mode_conflict_voice_form': "{0} موڈ فعال ہے۔ ختم کر کے ایک شکل داخل کریں؟",
        'form_settings_updated': "شکلوں کی ترتیبات اپ ڈیٹ کر دی گئیں",
        'form_unknown': "شکل",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. شروع کی پوزیشن پر کلک کریں",
        'form_line_guide_2': "2. اختتام کی پوزیشن پر کلک کریں",
        'form_line_guide_3': "لکیر دونوں نقطوں کے درمیان کھینچی جائے گی۔",
        'form_line_status_1': "پہلے کلک کا انتظار ہے...",
        'form_line_status_2': "پہلا نقطہ مقرر ہو گیا: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "اب اختتامی نقطہ پر کلک کریں...",
        'form_line_status_4': "دونوں نقطے مقرر ہو گئے۔\nمحفوظ کرنے کے لیے 'مکمل' پر کلک کریں۔",
        'form_line_reset': "ری سیٹ کریں",
        'form_line_finish': "مکمل",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "نقل کریں (Cmd+C)",
        'paste': "چسپاں کریں (Cmd+V)",
        'copied': "نقل کر دیا گیا: {0}",
        'no_element_to_copy': "نقل کرنے کے لیے کوئی عنصر منتخب نہیں کیا گیا",
        'no_copied_data': "کوئی نقل شدہ ڈیٹا نہیں",
        'no_valid_position': "چسپاں کرنے کے لیے کوئی درست پوزیشن نہیں",
        'copy_text': "متن نقل کر دیا گیا",
        'copy_image': "تصویر نقل کر دی گئی",
        'copy_form': "شکل نقل کر دی گئی",
        'copy_signature': "دستخط نقل کر دیا گیا",
        'element_text': "متن",
        'element_image': "تصویر",
        'element_form': "شکل",
        'element_signature': "دستخط",
        'element_unknown': "عنصر",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "موڈ کا تصادم",
        'mode_conflict_message': "'{0}' موڈ پہلے سے فعال ہے۔\n\nکیا آپ اسے ختم کر کے {1} کرنا چاہتے ہیں؟",
        'mode_replace': "موڈ ختم کریں اور {0} کریں",
        'mode_cancel': "منسوخ کریں",
        'mode_replace_text': "متن داخل کریں",
        'mode_replace_cross': "کراس داخل کریں",
        'mode_replace_signature': "دستخط داخل کریں",
        'mode_replace_image': "تصویر داخل کریں",
        'mode_replace_form': "شکل داخل کریں",
        'mode_conflict_voice': "{0} موڈ فعال ہے۔ ختم کر کے متن داخل کریں؟",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "متن کا اندراج",
        'active_mode_signature': "دستخط",
        'active_mode_image': "تصویر",
        'active_mode_form': "شکل",
        'active_mode_and': " اور ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "داخل کریں",                    # Hauptmenü
        'insert_another_text': "متن داخل کریں",          # Vereinfacht
        'insert_another_cross': "کراس داخل کریں",        # Vereinfacht
        'insert_another_signature_1': "دستخط 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "دستخط 2",      # Untermenü-Eintrag
        'insert_another_image': "تصویر داخل کریں",         # Vereinfacht
        'insert_another_form_rect': "مستطیل",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "بیضوی",        # Untermenü-Eintrag
        'insert_another_form_line': "لکیر (2 کلک)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "تیر (2 کلک)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} محفوظ کریں",
        'save_dialog_message': "{0} صفحہ {1} پر محفوظ کیا جائے گا۔\n\nآپ کیسے آگے بڑھنا چاہتے ہیں؟",
        'save_all': "تمام {0} محفوظ کریں",
        'save_single': "{0} محفوظ کریں",
        'save_customize': "{0} ایڈجسٹ کریں",
        'save_discard': "یہ {0} مسترد کریں",
        'save_continue': "ترمیم جاری رکھیں",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " صفحہ {0} پر جائیں",
        'context_rotate': " صفحہ {0} گھمائیں",
        'context_delete': " صفحہ {0} حذف کریں",
        'context_export': " صفحہ {0} برآمد کریں",
        'context_mark_as': " صفحہ کو بطور نشان زد کریں...",
        'context_mark_empty': " خالی صفحہ",
        'context_unmark_empty': " مزید خالی نہیں",
        'context_mark_export': " برآمد کے لیے نشان زد کریں",
        'context_unmark_export': " مزید برآمد نہ کریں",
        'context_batch_actions': " اجتماعی اقدامات",
        'context_batch_delete_empty': " تمام {0} خالی صفحات حذف کریں",
        'context_batch_export_single': " تمام {0} صفحات (ایک فائل)",
        'context_batch_export_split': " تمام {0} صفحات (الگ الگ)",
        'context_drag_start': " ڈریگ اینڈ ڈراپ شروع کریں",
        'context_drag_stop': " ڈریگ اینڈ ڈراپ ختم کریں",
        'context_insert': " داخل کریں",
        'context_insert_pages': " صفحات داخل کریں",
        'context_zoom': "زوم",
        'discard_mixed': "تمام {0} {1} اور {2} {3} مسترد کریں",
        'save_mixed': "{0} {1} اور {2} {3} محفوظ کریں",
        'discard_texts': "تمام {0} متن مسترد کریں",
        'discard_text_single': "1 متن مسترد کریں",
        'save_texts': "{0} متن محفوظ کریں",
        'save_text_single': "1 متن محفوظ کریں",
        'discard_crosses': "تمام {0} کراسز مسترد کریں",
        'discard_cross_single': "1 کراس مسترد کریں",
        'save_crosses': "{0} کراسز محفوظ کریں",
        'save_cross_single': "1 کراس محفوظ کریں",
        'discard_signatures': "تمام {0} دستخط مسترد کریں",
        'save_signature_single': "1 دستخط محفوظ کریں",
        'save_signatures': "{0} دستخط محفوظ کریں",
        'discard_images': "تمام {0} تصاویر مسترد کریں",
        'save_image_single': "1 تصویر محفوظ کریں",
        'save_images': "{0} تصاویر محفوظ کریں",
        'discard_forms': "تمام {0} شکلیں مسترد کریں",
        'save_form_single': "1 شکل محفوظ کریں",
        'save_forms': "{0} شکلیں محفوظ کریں",
        'cross_discard': "یہ کراس مسترد کریں",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 برآمد / درآمد کی معلومات",
        'export_what': "📋 کیا برآمد کیا جاتا ہے؟",
        'export_general': "عام ترتیبات",
        'export_general_items': "• تقریر آؤٹ پٹ (آن/آف، رفتار)\n• تاریک/روشن موڈ\n• بیک اپ ترتیبات\n• OCR ترتیبات",
        'export_image_form': "تصویر اور شکل کی ترتیبات",
        'export_image_form_items': "• تصویر کی ترتیبات (پہلو کا تناسب، طے شدہ سائز)\n• شکل کی ترتیبات (لکیر کی موٹائی، رنگ)\n• دستخط کی ترتیبات (پاتھ، سائز، ٹائم اسٹیمپ)",
        'export_passwords': "پاس ورڈ ڈیٹا بیس",
        'export_passwords_items': "• تمام محفوظ کردہ PDF پاس ورڈز\n• اختیاری طور پر خفیہ شدہ یا ڈیکرپٹ شدہ",
        'export_master': "ماسٹر پاس ورڈ کی ترتیبات",
        'export_master_items': "• ماسٹر پاس ورڈ ہیش\n• دستخطوں/متن کے بلاکس کے لیے ترتیبات",
        'export_signatures': "دستخط اور متن کے بلاکس",
        'export_signatures_items': "• تمام تصویری فائلیں (دستخط)\n• فارمیٹنگ کے ساتھ تمام متن کے بلاکس\n• ذاتی/عوامی نشانات",
        'export_import_warning': "⚠️ اہم نوٹس",
        'export_import_note': "• درآمد کرتے وقت، تمام موجودہ ترتیبات پر لکھ دی جائیں گی\n• درخواست کو دوبارہ شروع کرنا ضروری ہے\n• موجودہ دستخط/متن کے بلاکس تبدیل کر دیے جائیں گے",
        'export_master_note': "• اگر ماسٹر پاس ورڈ مقرر ہے تو آپ منتخب کر سکتے ہیں:\n  - ڈیکرپٹ شدہ (پاس ورڈز صاف متن میں)\n  - خفیہ شدہ (صرف ماسٹر پاس ورڈ سے پڑھے جا سکتے ہیں)",
        'export_security': "• برآمد شدہ ZIP فائل میں حساس ڈیٹا ہوتا ہے\n• براہ کرم محفوظ طریقے سے رکھیں (مثلاً خفیہ شدہ USB اسٹک)\n• فائل کھو جانے پر: پاس ورڈز ناقابل واپسی طور پر ضائع ہو جائیں گے",
        'export_format': "📁 برآمد کا فارمیٹ",
        'export_format_desc': "ترتیبات ایک واحد ZIP فائل میں محفوظ کی جائیں گی:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "ترتیبات کامیابی سے برآمد کر دی گئیں",
        'export_failed': "برآمد ناکام",
        'export_import_question': "کیا آپ اب درخواست کو دوبارہ شروع کرنا چاہتے ہیں؟",
        'export_password_question': "ایک ماسٹر پاس ورڈ مقرر ہے۔\n\nکیا آپ پاس ورڈز ڈیکرپٹ شدہ برآمد کرنا چاہتے ہیں؟\n(ورنہ وہ خفیہ شدہ برآمد کیے جائیں گے)",
        'export_decrypt': "ڈیکرپٹ شدہ برآمد کریں",
        'export_encrypt': "خفیہ شدہ برآمد کریں",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " معلومات",
        'info_title': "PDF Dark View کے بارے میں",
        'info_version': "ورژن",
        'info_author': "ٹورالف شلٹز (BinhDiez) کے ذریعہ تیار کردہ",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "تعارف",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ایک قابل رسائی PDF ناظر ہے جو خاص طور پر بصارت سے محروم افراد کے لیے تیار کیا گیا ہے۔</p>

            <p><strong>کلیدی خصوصیات:</strong></p>
            <ul>
                <li>اعلیٰ تضاد، حسب ضرورت انٹرفیس</li>
                <li>مکمل کی بورڈ کنٹرول</li>
                <li>انٹیگریٹڈ اسپیچ آؤٹ پٹ</li>
                <li>اسکین شدہ دستاویزات کے لیے OCR</li>
                <li>وسیع ترمیمی اوزار</li>
            </ul>

            <p>50 سے زائد زبانیں سپورٹ کی جاتی ہیں – تاکہ PDFs سب کے لیے قابل رسائی ہوں۔</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "خصوصیات",
        'info_features_intro': "PDF Dark View آپ کو درج ذیل امکانات فراہم کرتا ہے:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>ڈسپلے اور نیویگیشن</strong> – تاریک/روشن موڈ، صفحات پلٹنا، زوم، صفحہ پر جائیں</li>
            <li><strong>OCR (متن کی شناخت)</strong> – اسکین شدہ دستاویزات کو تلاش کے قابل اور نقل کے قابل بنائیں</li>
            <li><strong>ترمیم</strong> – متن، کراس، دستخط، تصاویر اور شکلیں داخل کریں</li>
            <li><strong>صفحہ کا انتظام</strong> – حذف کریں، نکالیں، داخل کریں، ڈریگ اینڈ ڈراپ سے منتقل کریں</li>
            <li><strong>برآمد</strong> – بطور Word، Pages یا متن</li>
            <li><strong>سلامتی</strong> – پاس ورڈ کا تحفظ اور انتظام</li>
            <li><strong>رسائی</strong> – اسپیچ آؤٹ پٹ، کی بورڈ کنٹرول، اعلیٰ تضاد</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "آپریشن",
        'info_accessibility': "♿ رسائی – مکمل کی بورڈ کنٹرول",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 عمومی</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF کھولیں</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> تلاش کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> تاریک/روشن موڈ تبدیل کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> پرنٹ کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> باہر نکلیں</div>

        <div class="shortcut-cat">📖 نیویگیشن</div>
        <div class="shortcut-row"><kbd>تیر والی کلیدیں</kbd> صفحہ بہ صفحہ پلٹیں</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> صفحہ پر جائیں</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> پہلا صفحہ</div>
        <div class="shortcut-row"><kbd>Ende</kbd> آخری صفحہ</div>

        <div class="shortcut-cat">✏️ ترمیم</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> متن داخل کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> صفحات حذف کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> صفحات نکالیں</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> صفحات داخل کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> صفحات منتقل کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> صفحہ گھمائیں</div>

        <div class="shortcut-cat">🖼️ عناصر منتقل کریں</div>
        <div class="shortcut-row"><kbd>تیر والی کلیدیں</kbd> متن/تصویر/دستخط منتقل کریں</div>
        <div class="shortcut-row"><kbd>Ctrl+تیر والی کلیدیں</kbd> بڑے اقدامات میں منتقل کریں</div>
        <div class="shortcut-row"><kbd>Enter</kbd> محفوظ کریں</div>
        <div class="shortcut-row"><kbd>ESC</kbd> مسترد کریں</div>

        <div class="shortcut-cat">🗣️ اسپیچ آؤٹ پٹ</div>
        <div class="shortcut-row"><kbd>F2</kbd> اسپیچ آؤٹ پٹ آن/آف کریں</div>
        """,
        'info_contextmenu': "📌 اہم: تمام افعال سیاق و سباق کے مینو (دائیں کلک) کے ذریعے بھی قابل رسائی ہیں!",
        'info_accessibility_hint': "💡 ٹپ: اسپیچ آؤٹ پٹ (F2) رہنمائی کو آسان بناتا ہے اور مینوز اور ڈائیلاگز پر فیڈ بیک دیتا ہے۔",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "لائسنس اور امپرنٹ",

        # Landessprachlicher Lizenztext
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 امپرنٹ</strong><br>
        § 5 TMG کے مطابق معلومات:<br>
        ٹورالف شلٹز<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        ای میل: binhdiez64@gmail.com<br>
        مواد کے ذمہ دار: ٹورالف شلٹز (BinhDiez)<br><br>

        <strong>⚠️ ذمہ داری سے انکار</strong><br>
        سافٹ ویئر انتہائی احتیاط سے تیار کیا گیا ہے۔ درستگی، مکمل ہونے اور فعالیت کی ضمانت نہیں دی جاتی۔ استعمال اپنی ذمہ داری پر ہے۔<br><br>

        <strong>📄 MIT-لائسنس (ذاتی استعمال)</strong><br>
        کاپی رائٹ (c) 2026 ٹورالف شلٹز (BinhDiez)<br>
        اجازت شدہ: مفت استعمال، ذاتی تبدیلیاں، ذاتی کاپیاں۔<br>
        اجازت نہیں: فروخت، تجارتی استعمال، کاپی رائٹ اطلاعات کو ہٹانا۔<br><br>

        <strong>🔧 تیسری پارٹی کے اجزاء</strong><br>
        اس سافٹ ویئر میں GPL، AGPL، Apache 2.0، BSD اور MIT-لائسنس کے تحت اجزاء شامل ہیں۔<br>
        دوبارہ تقسیم کرتے وقت، متعلقہ لائسنس کی شرائط پر عمل کرنا ضروری ہے۔<br><br>

        <strong>🌐 اوپن سورس</strong><br>
        سورس کوڈ دستیاب ہے اور متعلقہ لائسنس کی شرائط کے مطابق دیکھا، تبدیل کیا اور دوبارہ تقسیم کیا جا سکتا ہے۔<br><br>

        © 2026 ٹورالف شلٹز (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "شکریہ",
        'info_credits': "اوپن سورس کمیونٹی کا شکریہ",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF پروسیسنگ</li>
            <li><strong>PyQt5</strong> – گرافیکل انٹرفیس</li>
            <li><strong>Tesseract OCR</strong> – متن کی شناخت</li>
            <li><strong>OCRmyPDF</strong> – OCR انٹیگریشن</li>
            <li><strong>python-docx</strong> – Word برآمد</li>
            <li><strong>qtawesome</strong> – آئیکنز</li>
            <li><strong>DeepSeek</strong> – ترجمے میں مدد (50+ زبانیں)</li>
            <li><strong>تمام صارفین</strong> – قیمتی فیڈ بیک کے لیے</li>
            <li><strong>اوپن سورس کمیونٹی</strong> – عظیم لائبریریوں کے لیے</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "زبانیں",
        'info_languages_header': "🌍 زبان کی حمایت",
        'info_languages_html': """
        <div style="line-height:1.6;">
            <p>PDF Dark View فی الحال <strong>62 زبانیں</strong> سپورٹ کرتا ہے – تاکہ سافٹ ویئر دنیا بھر میں قابل رسائی ہو سکے۔</p>

            <p><strong>📖 مکمل زبانوں کی فہرست (مارچ 2026 تک):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 افریکانز</li>
                    <li>🇦🇱 البانوی (Shqip)</li>
                    <li>🇩🇿 عربی (العربية)</li>
                    <li>🇮🇩 بالینی (Basa Bali)</li>
                    <li>🇧🇩 بنگالی (বাংলা)</li>
                    <li>🇲🇲 برمی (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 بوسنیائی (Bosanski)</li>
                    <li>🇧🇬 بلغاری (Български)</li>
                    <li>🇨🇳 چینی (中文)</li>
                    <li>🇩🇰 ڈینش (Dansk)</li>
                    <li>🇩🇪 جرمن (Deutsch)</li>
                    <li>🇬🇧 انگریزی (English)</li>
                    <li>🇪🇪 اسٹونین (Eesti)</li>
                    <li>🇫🇮 فینیش (Suomi)</li>
                    <li>🇫🇷 فرانسیسی (Français)</li>
                    <li>🇬🇷 یونانی (Ελληνικά)</li>
                    <li>🇮🇱 عبرانی (עברית)</li>
                    <li>🇮🇳 ہندی (हिन्दी)</li>
                    <li>🇭🇷 کروشیائی (Hrvatski)</li>
                    <li>🇭🇺 ہنگیرین (Magyar)</li>
                    <li>🇮🇩 انڈونیشیائی (Bahasa Indonesia)</li>
                    <li>🇮🇪 آئرش (Gaeilge)</li>
                    <li>🇮🇸 آئس لینڈک (Íslenska)</li>
                    <li>🇮🇹 اطالوی (Italiano)</li>
                    <li>🇯🇵 جاپانی (日本語)</li>
                    <li>🇰🇭 خمیر (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 کورین (한국어)</li>
                    <li>🇱🇦 لاؤ (ພາສາລາວ)</li>
                    <li>🇱🇻 لیٹوین (Latviešu)</li>
                    <li>🇱🇹 لیتھوانیائی (Lietuvių)</li>
                    <li>🇱🇺 لکسمبرگش (Lëtzebuergesch)</li>
                    <li>🇲🇾 مالے (Bahasa Melayu)</li>
                    <li>🇮🇳 مراٹھی (मराठी)</li>
                    <li>🇲🇳 منگولین (Монгол)</li>
                    <li>🇳🇵 نیپالی (नेपाली)</li>
                    <li>🇳🇱 ڈچ (Nederlands)</li>
                    <li>🇳🇴 نارویجین (Norsk)</li>
                    <li>🇦🇫 پشتو (پښتو)</li>
                    <li>🇮🇷 فارسی (فارسی)</li>
                    <li>🇵🇱 پولش (Polski)</li>
                    <li>🇵🇹 پرتگالی (Português)</li>
                    <li>🇮🇳 پنجابی (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 رومانیائی (Română)</li>
                    <li>🇷🇺 روسی (Русский)</li>
                    <li>🇸🇪 سویڈش (Svenska)</li>
                    <li>🇷🇸 سربیائی (Српски)</li>
                    <li>🇸🇰 سلوواک (Slovenčina)</li>
                    <li>🇸🇮 سلووینیائی (Slovenščina)</li>
                    <li>🇪🇸 ہسپانوی (Español)</li>
                    <li>🇹🇿 سواحلی (Kiswahili)</li>
                    <li>🇵🇭 ٹیگالوگ (Filipino)</li>
                    <li>🇮🇳 تامل (தமிழ்)</li>
                    <li>🇮🇳 تیلگو (తెలుగు)</li>
                    <li>🇹🇭 تھائی (ไทย)</li>
                    <li>🇨🇿 چیک (Čeština)</li>
                    <li>🇹🇷 ترکی (Türkçe)</li>
                    <li>🇺🇦 یوکرینی (Українська)</li>
                    <li>🇵🇰 اردو (اردو)</li>
                    <li>🇻🇳 ویتنامی (Tiếng Việt)</li>
                    <li>🇸🇳 وولوف (Wolof)</li>
                    <li>🇺🇸 یدش (ייִדיש)</li>
                    <li>🇿🇦 زولو (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 اپنی زبانیں شامل کریں:</strong><br>
                کیا آپ کوئی ایسی زبان چاہتے ہیں جو ابھی شامل نہیں ہے؟ بس اپنی ڈکشنری فائل (<code>sprache_xx.py</code>) ایپلیکیشن کے پاس رکھیں – سافٹ ویئر خود بخود اسے پہچان لے گا۔ کسی خاص ترجمے میں دلچسپی ہو تو براہ کرم مجھ سے رابطہ کریں۔
            </div>

            <p><strong>🙏 خصوصی شکریہ:</strong> 62 زبانوں میں تمام ڈکشنریز کے ترجمے میں مدد کے لیے ڈیپ سیک کا۔</p>

            <p>📧 ترجمے کے لیے رابطہ: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "خرابی",
        'error_occurred': "ایک خرابی پیش آ گئی",
        'error_pdf_load': "PDF لوڈ کرتے وقت خرابی",
        'error_pdf_save': "PDF محفوظ کرتے وقت خرابی",
        'error_ocr': "متن کی شناخت میں خرابی",
        'error_no_pdf': "کوئی PDF لوڈ نہیں کی گئی",
        'error_page_not_found': "صفحہ نہیں ملا",
        'error_invalid_range': "غلط صفحات کی حد",
        'error_file_not_found': "فائل نہیں ملی",
        'error_permission': "اجازت نہیں ہے",
        'error_unknown': "نامعلوم خرابی",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "کامیاب",
        'success_operation': "آپریشن کامیابی سے مکمل ہو گیا",
        'success_saved': "کامیابی سے محفوظ ہو گیا",
        'success_exported': "کامیابی سے برآمد ہو گیا",
        'success_imported': "کامیابی سے درآمد ہو گیا",
        'success_deleted': "کامیابی سے حذف ہو گیا",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "تصدیق",
        'confirm_yes': "ہاں",
        'confirm_no': "نہیں",
        'confirm_ok': "ٹھیک ہے",
        'confirm_cancel': "منسوخ کریں",
        'confirm_delete': "حذف کریں",
        'confirm_overwrite': "پر لکھیں",
        'confirm_continue': "جاری رکھیں",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF لوڈ ہو رہی ہے...",
        'progress_saving': "PDF محفوظ ہو رہی ہے...",
        'progress_exporting': "PDF برآمد ہو رہی ہے...",
        'progress_processing': "پروسیسنگ جاری ہے...",
        'progress_wait': "براہ کرم انتظار کریں...",
        'progress_preparing': "تیاری...",
        'progress_finalizing': "حتمی شکل دی جا رہی ہے...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "سفید",
        'color_black': "سیاہ",
        'color_red': "سرخ",
        'color_green': "سبز",
        'color_blue': "نیلا",
        'color_yellow': "پیلا",
        'color_magenta': "ماجنٹا",
        'color_cyan': "سائن",
        'color_orange': "نارنجی",
        'color_gray': "سرمئی",
        'color_custom': "رنگ کا انتخاب",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&فائل",
        'menu_edit': "&ترمیم",
        'menu_view': "&منظر",
        'menu_tools': "&آلات",
        'menu_settings': "&ترتیبات",
        'menu_help': "&مدد",
        'menu_language': "🌐 زبان",
        'menu_guides': "&رہنما",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&کھولیں",
        'file_save_as': "&بطور محفوظ کریں...",
        'file_protect': "دستاویز &محفوظ کریں...",
        'file_export': "&برآمد کریں",
        'file_export_pages': "Pages کے طور پر برآمد کریں",
        'file_export_word': "DOCX کے طور پر برآمد کریں",
        'file_export_text': "TXT کے طور پر برآمد کریں",
        'file_print_now': "&ابھی پرنٹ کریں",
        'file_print': "&پرنٹ کریں",
        'file_close': "&بند کریں",
        'file_quit': "&باہر نکلیں",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&تلاش کریں",
        'edit_ocr': " OCR کریں",
        'edit_rotate': "صفحہ &گھمائیں",
        'edit_rotate_all': "&تمام صفحات گھمائیں",
        'edit_delete_pages': "صفحات &حذف کریں",
        'edit_extract_pages': "صفحات &نکالیں",
        'edit_insert_pages': "صفحات &داخل کریں",
        'edit_move_pages': "صفحات &منتقل کریں",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " متن اور کراس داخل کریں",
        'text_insert': " متن داخل کریں",
        'cross_insert': " کراس داخل کریں",
        'text_customize': " متن ایڈجسٹ کریں",
        'cross_customize': " اس کراس کو ایڈجسٹ کریں",
        'cross_customize_all': " تمام کراسز ایڈجسٹ کریں",
        'text_discard': " یہ متن/کراس مسترد کریں",
        'text_discard_all': " تمام متن اور کراسز مسترد کریں",
        'text_save_all': " تمام متن اور کراسز محفوظ کریں",
        'text_guide': " متن کا اندراج / متن کے بلاکس - رہنما",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " دستخط داخل کریں",
        'signature_settings_menu': " ترتیبات...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " تصویر داخل کریں",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " شکلیں داخل کریں",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&متن کی ونڈو دکھائیں",
        'view_zoom': "&زوم",
        'view_zoom_page': "&صفحے کی چوڑائی (طے شدہ)",
        'view_zoom_two': "&دو صفحات",
        'view_zoom_overview': "&جائزہ (متعدد صفحات)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&رسائی کی معاونت",
        'settings_voice': "اسپیچ آؤٹ پٹ",
        'settings_voice_tooltip': "اسکرین ریڈرز کی اسپیچ آؤٹ پٹ کو اضافی معلومات کے ساتھ مکمل کرتا ہے",
        'settings_signature': "&دستخط کی ترتیبات",
        'settings_password': "&پاس ورڈ کا انتظام",
        'settings_backup': "تبدیلیوں سے پہلے بیک اپ بنائیں",
        'settings_export_import': "&ترتیبات برآمد کریں / درآمد کریں",
        'settings_export': "&تمام ترتیبات برآمد کریں...",
        'settings_import': "&تمام ترتیبات درآمد کریں...",
        'settings_export_info': "&کیا برآمد کیا جاتا ہے؟",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "آن",
        'voice_off': "آف",
        'voice_toggle': "اسپیچ آؤٹ پٹ {0}",
        'voice_speed': "رفتار {0} فیصد",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "ٹول نہیں ملا:\n{0}\n\nBASE_DIR: {1}\nیقینی بنائیں کہ PDF ٹولز ڈائرکٹری {1} میں نصب ہیں۔",
        'tool_started': "{0} شروع ہو گیا",
        'tool_start_failed': "شروع نہیں کیا جا سکا",
        'process_error_failed_to_start': "عمل شروع نہیں کیا جا سکا۔ کیا فائل موجود ہے؟",
        'process_error_crashed': "شروع کرتے وقت عمل کریش ہو گیا۔",
        'process_error_timeout': "عمل کا ٹائم آؤٹ ہو گیا۔",
        'process_error_write': "عمل میں لکھنے کی خرابی۔",
        'process_error_read': "عمل میں پڑھنے کی خرابی۔",
        'process_error_unknown': "نامعلوم عمل کی خرابی",
        'process_command': "کمانڈ",
        'process_normal_exit': "عام طور پر ختم ہوا",
        'process_crashed': "کریش ہو گیا",
        'process_nonzero_exit': "{0} خرابی کوڈ {1} کے ساتھ ختم ہوا",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "منسوخ کیا جا رہا ہے...",
        'move_cancelling': "منتقل کرنا منسوخ کیا جا رہا ہے",
        'opening_pdf': "PDF کھولی جا رہی ہے...",
        'loading_document': "دستاویز لوڈ کی جا رہی ہے...",
        'pdf_opened': "PDF کھل گئی",
        'pages_found_moving': "{0} صفحات ملے، {1} منتقل کرنے کے لیے",
        'creating_backup': "بیک اپ بنایا جا رہا ہے...",
        'backup_description': "اصل فائل محفوظ کی جا رہی ہے...",
        'backup_saved_as': "بطور محفوظ کیا گیا: {0}",
        'error_format': "خرابی: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "تلاش ری سیٹ کر دی گئی",
        'page_header_simple': "=== صفحہ {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "پاس ورڈ کا انتظام – رہنما",
        'password_guide_voice': "پاس ورڈ کے انتظام کا رہنما۔ براہ کرم نوٹس پڑھیں۔",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 پاس ورڈ کا انتظام – تفصیلی رہنما</strong></p>

        <p><strong>1. PDF کے لیے پاس ورڈ کا تحفظ</strong></p>
        <ul>
        <li>پاس ورڈ سے محفوظ PDF کھولتے وقت ایک ڈائیلاگ ظاہر ہوتا ہے جہاں آپ پاس ورڈ داخل کر سکتے ہیں۔</li>
        <li>آپ پاس ورڈ کو خفیہ کر کے محفوظ کر سکتے ہیں، تاکہ آپ کو ہر بار اسے دوبارہ داخل نہ کرنا پڑے (چیک باکس "پاس ورڈ محفوظ کریں")۔</li>
        <li>"پاس ورڈ ہٹائیں" بٹن کے ذریعے آپ PDF کی ایک ڈیکرپٹ شدہ کاپی بنا سکتے ہیں اور ڈیٹا بیس سے پاس ورڈ حذف کر سکتے ہیں۔</li>
        </ul>

        <p><strong>2. ماسٹر پاس ورڈ</strong></p>
        <ul>
        <li>ماسٹر پاس ورڈ تمام محفوظ کردہ PDF پاس ورڈز کی رسائی کی حفاظت کرتا ہے۔</li>
        <li><strong>ترتیب دینا:</strong> "ترتیبات → پاس ورڈ کا انتظام → ماسٹر پی ڈبلیو ترتیبات" پر جائیں اور "ماسٹر پاس ورڈ مرتب کریں" پر کلک کریں۔ ایک مضبوط ماسٹر پاس ورڈ منتخب کریں (کم از کم 8 حروف)۔</li>
        <li><strong>تبدیل کرنا:</strong> کامیاب تصدیق کے بعد آپ ماسٹر پاس ورڈ تبدیل کر سکتے ہیں۔</li>
        <li><strong>ہٹانا:</strong> اگر آپ ماسٹر پاس ورڈ حذف کرتے ہیں، تو تمام محفوظ کردہ پاس ورڈز ناقابل واپسی طور پر حذف ہو جائیں گے۔ آپ پہلے بیک اپ برآمد کر سکتے ہیں۔</li>
        <li>ہر سیشن میں ایک بار آپ کو ماسٹر پاس ورڈ سے تصدیق کرنی ہوگی، محفوظ افعال (مثلاً پاس ورڈ دیکھنا) تک رسائی حاصل کرنے کے لیے۔</li>
        </ul>

        <p><strong>3. پاس ورڈ کا انتظام (فہرست)</strong></p>
        <ul>
        <li>"ترتیبات → پاس ورڈ کا انتظام" کے تحت آپ ان کے خفیہ شدہ پاس ورڈز کے ساتھ تمام محفوظ کردہ PDF کی ایک ٹیبل کھولیں گے۔</li>
        <li><strong>ماسٹر پاس ورڈ کے بغیر:</strong> آپ صرف اندراجات حذف کر سکتے ہیں – پاس ورڈز پوشیدہ رہتے ہیں۔</li>
        <li><strong>ماسٹر پاس ورڈ کے ساتھ (تصدیق شدہ):</strong> آپ پاس ورڈ دیکھ سکتے ہیں، نقل کر سکتے ہیں، برآمد کر سکتے ہیں اور حذف کر سکتے ہیں۔</li>
        <li><strong>برآمد:</strong> ایک فارمیٹ منتخب کریں (JSON, CSV, TXT) اور فہرست محفوظ کریں۔ اگر ماسٹر پاس ورڈ مقرر ہے تو آپ فیصلہ کر سکتے ہیں کہ پاس ورڈز صاف متن میں برآمد کیے جائیں یا خفیہ شدہ رہیں۔</li>
        <li><strong>درآمد:</strong> پہلے برآمد کردہ ZIP فائل (ترتیبات سمیت) "ترتیبات → ترتیبات برآمد کریں / درآمد کریں" کے ذریعے دوبارہ پڑھی جا سکتی ہے۔ خبردار: موجودہ ڈیٹا پر لکھ دیا جائے گا!</li>
        </ul>

        <p><strong>4. پاس ورڈ جنریٹر</strong></p>
        <ul>
        <li>پاس ورڈ ڈائیلاگ میں (مثلاً PDF کو محفوظ کرتے وقت) آپ کو ان پٹ فیلڈ کے دائیں جانب ایک پانسے کا بٹن 🎲 ملے گا۔</li>
        <li>پاس ورڈ جنریٹر کھولنے کے لیے اس پر کلک کریں۔ آپ لمبائی، حروف کا سیٹ (بڑے حروف، چھوٹے حروف، اعداد، خاص علامات) اور بہتر پڑھنے کے لیے محدود کنندہ مقرر کر سکتے ہیں۔</li>
        <li>تیار کردہ پاس ورڈ براہ راست لیا جا سکتا ہے اور ضرورت پڑنے پر نقل بھی کیا جا سکتا ہے۔</li>
        </ul>

        <p><strong>5. اہم حفاظتی نوٹس</strong></p>
        <ul>
        <li>محفوظ کردہ پاس ورڈز AES-256 خفیہ شدہ شکل میں ذخیرہ کیے جاتے ہیں۔ کلید آپ کے ماسٹر پاس ورڈ سے (اگر مقرر ہے) یا ایک مقررہ قدر سے (ماسٹر پاس ورڈ کے بغیر) حاصل کی جاتی ہے۔</li>
        <li>ماسٹر پاس ورڈ کے بغیر، پاس ورڈز خفیہ ہیں لیکن کلید پروگرام میں ذخیرہ ہے – آپ کی فائلوں تک رسائی رکھنے والا حملہ آور انہیں ڈیکرپٹ کر سکتا ہے۔ اس لیے ہم ماسٹر پاس ورڈ کے استعمال کی سختی سے سفارش کرتے ہیں۔</li>
        <li>پاس ورڈ ڈیٹا بیس ڈائرکٹری `Daten/passwords.json` میں ہے۔ باقاعدہ بیک اپ بنائیں، خاص طور پر ماسٹر پاس ورڈ ہٹانے سے پہلے۔</li>
        <li>ماسٹر پاس ورڈ کھو جانے پر، تمام محفوظ کردہ پاس ورڈز ناقابل واپسی طور پر ضائع ہو جائیں گے۔</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # Neu ab 2026-03-19
        # ============================================

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "الٹنے کا موڈ",
        'invert_mode_classic': "کلاسک (تمام رنگ الٹ دیں)",
        'invert_mode_smart': "ذہین (صرف چمک الٹ دیں)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "گرے اسکیل تھریش ہولڈ",
        'gray_threshold_10': "10% (سخت)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (طے شدہ)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (نرم)",
        'threshold_changed': "تھریش ہولڈ {0}% پر مقرر کیا گیا",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "گرے اسکیل تھریش ہولڈ – وضاحت",
        'threshold_guide_text': "گرے اسکیل تھریش ہولڈ اس بات کا تعین کرتا ہے کہ ذہین تاریک موڈ میں کون سے پکسلز 'سرمئی' سمجھے جائیں گے اور الٹ دیے جائیں گے۔\n\n"
                                "• کم قدر (10%) صرف قریب قریب کامل سرمئی ٹونز کو الٹ دیتی ہے – رنگین عناصر مکمل طور پر محفوظ رہتے ہیں۔\n"
                                "• زیادہ قدر (50%) تھوڑے سے رنگین پکسلز کو بھی الٹ دیتی ہے – اس سے تضاد بڑھتا ہے، لیکن رنگ بگڑ سکتے ہیں۔\n\n"
                                "بہترین قدر دستاویز پر منحصر ہے۔ خالص متن کی دستاویزات کے لیے 30–40% اکثر مثالی ہے، رنگین گرافکس کے لیے 10–20%۔\n\n"
                                "آپ 'ترتیبات' مینو کے ذریعے کسی بھی وقت قدر کو ایڈجسٹ کر سکتے ہیں – پھر PDF فوری طور پر دوبارہ لوڈ ہو جائے گی۔\n\n"
                                "نوٹ کریں:\n* تصاویر اور فوٹوز صرف روشن موڈ میں ہی درست طریقے سے دکھائی جا سکتی ہیں!\n* الٹنے کی ترتیبات صرف اس وقت دکھائی جاتی ہیں جب تاریک موڈ فعال ہو۔",
        'threshold_guide_voice': "گرے اسکیل تھریش ہولڈ اس بات کا تعین کرتا ہے کہ ذہین تاریک موڈ کتنا مداخلت کرتا ہے۔ کم قدر رنگوں کو محفوظ رکھتی ہے، زیادہ قدر تضاد کو بڑھاتی ہے۔",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF کھولی جا رہی ہے...",
        'progress_loading_document': "دستاویز لوڈ کی جا رہی ہے...",
        'progress_pdf_opened': "PDF کھل گئی",
        'progress_creating_backup': "بیک اپ بنایا جا رہا ہے...",
        'progress_backup_description': "اصل فائل محفوظ کی جا رہی ہے...",
        'progress_backup_created': "بیک اپ بنایا گیا",
        'progress_backup_saved_as': "بطور محفوظ کیا گیا: {0}",
        'progress_analyzing_start': "تجزیہ شروع ہو رہا ہے...",
        'progress_searching_empty': "خالی صفحات تلاش کیے جا رہے ہیں...",
        'progress_page_empty': "صفحہ {0} خالی ہے",
        'progress_page_keep': "صفحہ {0} رکھا جائے گا",
        'progress_analysis_complete': "تجزیہ مکمل ہو گیا",
        'progress_empty_found': "{0} خالی صفحات ملے",
        'progress_current_page': "موجودہ صفحہ",
        'progress_mark_delete': "حذف کرنے کے لیے نشان زد کیا جا رہا ہے",
        'progress_range_selected': "صفحات کی حد {0}-{1}",
        'progress_deleting_pages': "{0} صفحات حذف کیے جا رہے ہیں",
        'progress_creating_new_pdf': "نئی PDF بنائی جا رہی ہے...",
        'progress_transferring_pages': "صفحات منتقل کیے جا رہے ہیں",
        'progress_keeping_page': "صفحہ {0} رکھا جائے گا ({1}/{2})",
        'progress_saving_pdf': "PDF محفوظ کی جا رہی ہے...",
        'progress_optimizing': "فائل کا سائز بہتر کیا جا رہا ہے...",
        'progress_finalizing': "حتمی شکل دی جا رہی ہے...",
        'progress_new_size': "نیا سائز: {0:.2f} MB",
        'progress_cancelling': "منسوخ کیا جا رہا ہے...",
        'progress_cancel_message': "{0} منسوخ کیا جا رہا ہے",
        'progress_pages_found_moving': "{0} صفحات ملے، {1} منتقل کرنے کے لیے",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF کا تجزیہ کیا جا رہا ہے...",
        'ocr_status_optimizing': "تصویر کی اصلاح جاری ہے...",
        'ocr_status_recognizing': "متن کی شناخت کا کام جاری ہے...",
        'ocr_status_embedding': "متن ایمبیڈ کیا جا رہا ہے...",
        'ocr_status_finalizing': "PDF کو حتمی شکل دی جا رہی ہے...",

        # PDF-Laden
        'progress_preparing': "تیاری...",
        'progress_loading': "PDF لوڈ ہو رہی ہے...",

        # Seitenoperationen
        'progress_deleting_title': "صفحات حذف کیے جا رہے ہیں...",
        'progress_moving_title': "صفحات منتقل کیے جا رہے ہیں...",
        'pages_found': "صفحات مل گئے",
        'progress_creating_new_order': "نیا ترتیب بنایا جا رہا ہے...",
        'progress_sorting_pages': "صفحات ترتیب دیے جا رہے ہیں...",
        'progress_moving_to_begin': "{0} صفحات شروع میں منتقل کیے جا رہے ہیں",
        'progress_transferring_count': "{0} صفحات منتقل کیے جا رہے ہیں",
        'progress_transferring_before_target': "ہدف سے پہلے صفحات منتقل کیے جا رہے ہیں",
        'progress_moving_pages': "{0} صفحات منتقل کیے جا رہے ہیں",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_بیک اپ_",
        'filename_protected_suffix': "_محفوظ_",
        'filename_copy_suffix': "_نقل",
        'filename_page_single': "_صفحہ_",
        'filename_page_range': "_صفحات_",
        'filename_export_page': "_صفحہ_{0:03}",
        'filename_export_range': "_صفحات_{0}-{1}",
        'filename_export_multiple': "_صفحات_{0}",
        'filename_with_text': "_متن_کے_ساتھ",
        'filename_with_signature': "_دستخط_کے_ساتھ",
        'filename_with_image': "_تصویر_کے_ساتھ",
        'filename_with_forms': "_شکلوں_کے_ساتھ",
        # ---------------------------------------------------------
        # Zentrale Verwaltung des Formats der Zeitstempel
        # ---------------------------------------------------------
        'filename_timestamp_format': "%Y%m%d_%H%M%S",
        'filename_timestamp_micro': "%Y%m%d_%H%M%S_%f",

        # ============================================
        # 56. ANSICHT – BUTTONLEISTE EIN-/AUSBLENDEN
        # ============================================
        'view_toggle_navbar': "بٹن بار دکھائیں",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "تمام صفحات حذف نہیں کیے جا سکتے",
		'pages_cannot_delete_last_page': 'آخری صفحہ حذف نہیں کیا جا سکتا!',
		'pages_cannot_delete_all_pages': 'دستاویز میں کم از کم ایک صفحہ باقی رہنا چاہیے!',
		'delete_pages_confirm': 'کیا آپ {0} صفحات حذف کرنے کے لیے یقین رکھتے ہیں؟',
		'delete_pages_confirm_voice': 'کیا آپ {0} صفحات حذف کرنے کے لیے یقین رکھتے ہیں؟',
		'pages_deleted': '{0} صفحات کامیابی سے حذف ہو گئے۔',
		'warning': 'انتباہ',
		'error': 'نقص',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "کوئی فارم منتخب نہیں کیا گیا",
        'form_customized': "فارم حسب ضرورت بنایا گیا",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "منتخب کریں",
        'btn_use': "استعمال کریں",
        'master_password_for_spasswords': "پاس ورڈز کو ذخیرہ کرنے اور استعمال کرنے کے لیے، پہلے ماسٹر پاس ورڈ ترتیب دینا ہوگا۔\n\nکیا آپ اب ماسٹر پاس ورڈ ترتیب دینا چاہتے ہیں؟",
        'open_saved_dialog_title': "محفوظ شدہ فائل کھولیں",
        'open_saved_question': "کیا آپ محفوظ شدہ فائل اب کھولنا چاہتے ہیں؟",
        'password': "پاس ورڈ",
        'password_manager_master_required': "پاس ورڈ مینیجر صرف اس وقت دستیاب ہوتا ہے جب ماسٹر پاس ورڈ ترتیب دیا گیا ہو۔\n\nکیا آپ اب ماسٹر پاس ورڈ ترتیب دینا چاہتے ہیں؟",
        'password_master_required_for_select': "محفوظ شدہ پاس ورڈز دیکھنے اور منتخب کرنے کے لیے، آپ کو پہلے اپنے ماسٹر پاس ورڈ سے تصدیق کرنی ہوگی۔\n\nکیا آپ اب تصدیق کرنا چاہتے ہیں؟",
        'password_not_available': "منتخب کردہ پاس ورڈ دستیاب نہیں ہے یا اسے ڈکرپٹ نہیں کیا جا سکا۔",
        'password_options_title': "پاس ورڈ کے اختیارات",
        'password_save_choice_change': "نیا پاس ورڈ ترتیب دیں",
        'password_save_choice_keep': "موجودہ پاس ورڈ استعمال کریں",
        'password_save_choice_none': "بغیر خفیہ کاری کے محفوظ کریں",
        'password_save_hint': "پاس ورڈز کو محفوظ طریقے سے ذخیرہ کرنے کے لیے پہلے ماسٹر پاس ورڈ ترتیب دیں۔",
        'password_save_master_required': "پاس ورڈ محفوظ کریں (صرف ماسٹر پاس ورڈ کے ساتھ ممکن ہے)",
        'password_save_question': "موجودہ PDF پاس ورڈ سے محفوظ ہے۔ کیا آپ موجودہ پاس ورڈ استعمال کرنا چاہتے ہیں، نیا ترتیب دینا چاہتے ہیں یا بغیر خفیہ کاری کے محفوظ کرنا چاہتے ہیں؟",
        'password_select': "پاس ورڈ منتخب کریں",
        'password_select_none': "کوئی پاس ورڈ منتخب نہیں کیا گیا۔\n\nبراہ کرم فہرست میں سے ایک پاس ورڈ منتخب کریں۔",
        'password_select_one': "براہ کرم بالکل ایک پاس ورڈ منتخب کریں۔\n\nآپ نے متعدد پاس ورڈز کو نشان زد کیا ہے۔",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_بیک اپ",
        'filename_insert_suffix': "_شمولیت_کے_ساتھ",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_صفحات_حذف_شدہ",
        'filename_pages_moved': "_صفحات_منتقل_شدہ",
        'filename_rotated_all_suffix': "_تمام_صفحات_گھمائے_گئے",
        'filename_rotated_suffix': "_صفحہ_گھمایا_گیا",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "PDF تبدیل کرتے وقت فائل ناموں کی ترتیب",
        'filename_keep_suffixes': "پچھلی توسیعات رکھیں (مثال کے طور پر _متن_کے_ساتھ)",
        'filename_keep_suffixes_false': "تبدیل کریں",
        'filename_keep_suffixes_true': "رکھیں",
        'filename_preview_label': "فائل نام کا پیش منظر:",
        'filename_preview_overwrite_hint': "پیش منظر دستیاب نہیں – اصل فائل پر لکھ دیا جائے گا۔",
        'filename_separator': "الفاظ کے درمیان جداکار",
        'filename_separator_none': "کوئی جداکار نہیں",
        'filename_separator_space': "خالی جگہ ( )",
        'filename_separator_underscore': "زیر خط (_)",
        'filename_settings_saved': "فائل نام کی ترتیبات محفوظ کر دی گئیں",
        'filename_settings_title': "فائل نام کی فارمیٹنگ اور بیک اپ",
        'filename_timestamp_position': "ٹائم سٹیمپ کی پوزیشن",
        'filename_timestamp_position_after': "بنیادی نام کے بعد",
        'filename_timestamp_position_before': "بالکل آگے",
        'filename_timestamp_position_end': "آخر میں",
        'filename_use_timestamp': "ٹائم سٹیمپ استعمال کریں",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>تبدیلیوں کے وقت رویہ:</b><ul><li>صفحات کو حذف کرنا اور داخل کرنا</li><li>متن، دستخط، تصویر اور اشکال داخل کرنا</li><li>OCR</li></ul></html>",
        'backup_section': "صفحات کی کارروائیوں کے لیے بیک اپ (حذف کریں، منتقل کریں)",
        'behavior_info': "نوٹ: 'اصل پر لکھیں' پر ٹائم سٹیمپ اور لاحقوں کو نظر انداز کیا جاتا ہے – فائل اپنا نام برقرار رکھتی ہے۔",
        'behavior_new_file': "ہمیشہ نئی فائل بنائیں (ٹائم سٹیمپ اور لاحقے کے ساتھ)",
        'behavior_overwrite': "اصل پر لکھیں (کوئی نئی فائل نہیں)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "تمام صفحات گھما دیے گئے۔\n\nاصل تبدیل شدہ حالت میں رہا۔\nنئی فائل: {0}",
        'all_pages_rotated_voice': "تمام صفحات گھمائے گئے، نئی فائل بنائی گئی۔",
        'empty_pages_deleted_new_file': "{0} خالی صفحات حذف کر دیے گئے۔\n\nاصل تبدیل شدہ حالت میں رہا۔\nنئی فائل: {1}",
        'empty_pages_deleted_voice': "{0} خالی صفحات حذف کیے گئے، نئی فائل بنائی گئی۔",
        'ocr_keep_original': "اصل رکھیں (بعد میں دستی طور پر کھولیں)",
        'ocr_new_file_question': "نئی قابل تلاش PDF یہاں محفوظ کر دی گئی:\n{0}\n\nکیا آپ اسے اب کھولنا چاہتے ہیں؟",
        'ocr_open_new': "نئی OCR فائل کھولیں",
        'ocr_original_kept': "اصل فائل کھلی رہتی ہے۔ OCR فائل محفوظ کر دی گئی ہے۔",
        'page_deleted_new_file': "صفحہ {0} حذف کر دیا گیا۔\n\nاصل تبدیل شدہ حالت میں رہا۔\nنئی فائل: {1}",
        'page_deleted_voice': "صفحہ {0} حذف کیا گیا، نئی فائل بنائی گئی۔",
        'page_rotated_new_file': "صفحہ {0} گھما دیا گیا۔\n\nاصل تبدیل شدہ حالت میں رہا۔\nنئی فائل: {1}",
        'page_rotated_voice': "صفحہ {0} گھمایا گیا، نئی فائل بنائی گئی۔",
        'pages_deleted_new_file': "{0} صفحات حذف کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nنئی فائل: {1}",
        'pages_deleted_new_file_voice': "{0} صفحات حذف کیے گئے، نئی فائل بنائی گئی۔",
        'pages_inserted_new_file': "{0} صفحات داخل کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nنئی فائل: {1}",
        'pages_inserted_new_file_ask': "{0} صفحات داخل کر دیے گئے۔\n\nاصل تبدیل شدہ حالت میں رہا۔\nنئی فائل: {1}\n\nکیا آپ اسے اب کھولنا چاہتے ہیں؟",
        'pages_inserted_voice_new': "{0} صفحات داخل کیے گئے، نئی فائل بنائی گئی۔",
        'pages_moved_new_file': "{0} صفحات منتقل کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nنئی فائل: {1}",
        'pages_moved_new_file_voice': "{0} صفحات منتقل کیے گئے، نئی فائل بنائی گئی۔",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "دوبارہ نہ دکھائیں",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 بیک اپ ترتیب</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ بیک اپ آن ہے</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">ان تمام تبدیلیوں پر جو اصل پر لکھتی ہیں</strong> (متن، دستخط، تصویر، شکل، OCR، گھمانا، داخل کرنا، صفحات حذف کرنا/منتقل کرنا) تبدیلی لاگو کرنے سے پہلے <strong>خودکار طور پر ٹائم سٹیمپ کے ساتھ ایک بیک اپ بنایا جاتا ہے</strong>۔</p>
                <p style="margin: 5px 0 5px 20px;">• بیک اپ اصل فائل کے پاس ہوتا ہے (مثال کے طور پر <code>دستاویز_بیک_اپ_20260412_120000.pdf</code>)۔</p>
                <p style="margin: 5px 0 5px 20px;">• اگر آپ نے اضافی طور پر <strong>„اصل پر لکھیں“</strong> کا اختیار فعال کیا ہے، تو بھی ایک بیک اپ بنایا جاتا ہے۔</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 بیک اپ آف ہے</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>کوئی بیک اپ نہیں بنایا جاتا</strong> – نہ اوور رائٹ کرتے وقت، نہ صفحات کی کارروائیوں پر۔</p>
                <p style="margin: 5px 0 5px 20px;">• اوور رائٹ کرتے وقت اصل فائل ناقابل واپسی طور پر ضائع ہو سکتی ہے۔</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">صرف تجربہ کار صارفین کے لیے تجویز کیا جاتا ہے!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ٹپ:</strong> بیک اپ ترتیب „اصل پر لکھیں“ کے اختیار سے آزاد ہے۔ آپ دونوں کو یکجا کر سکتے ہیں۔<br>
                آپ اس پیغام کو مستقل طور پر چھپا سکتے ہیں۔
            </div>
        </div>
        """,
        'backup_info_title': "بیک اپ کا رویہ",
        'backup_info_voice': "صفحات کی کارروائیوں پر بیک اپ رویہ کے بارے میں اطلاع۔ بیک اپ آن اصل پر لکھتا ہے، بیک اپ آف نئی فائل بناتا ہے۔",
        'show_backup_info': "بیک اپ ترتیب کے بارے میں معلومات",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "دوبارہ نہ دکھائیں",
        'overwrite_enable_backup': "بیک اپ کو فعال کریں (تجویز کردہ)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ اصل پر لکھیں</p>
            <p>اگر آپ یہ اختیار فعال کرتے ہیں، تو تبدیلیاں (متن، دستخط، تصویر، شکل، OCR، گھمانا، داخل کرنا) <strong>براہ راست اصل فائل پر محفوظ ہوتی ہیں</strong> – <strong>کوئی نئی فائل نہیں بنتی</strong>۔</p>
            <p>• فائل کا نام تبدیل نہیں ہوتا۔<br>
            • ٹائم سٹیمپ اور لاحقوں کو نظر انداز کیا جاتا ہے۔<br>
            • <strong>بیک اپ کے بغیر، اصل فائل ناقابل واپسی طور پر ضائع ہو سکتی ہے۔</strong></p>
            <p style="color: #FFD700;">تجویز: خودکار بیک اپ حاصل کرنے کے لیے اضافی طور پر بیک اپ کا اختیار فعال کریں۔</p>
        </div>
        """,
        'overwrite_info_title': "اصل پر لکھیں",
        'overwrite_info_voice': "انتباہ: اصل پر لکھیں – کوئی نئی فائل نہیں۔ بیک اپ تجویز کردہ ہے۔",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} صفحات داخل کر دیے گئے۔\n\nاصل فائل پر لکھ دی گئی۔\nایک بیک اپ بنایا گیا۔",
        'pages_inserted_overwrite_no_backup': "{0} صفحات داخل کر دیے گئے۔\n\nاصل فائل پر لکھ دی گئی۔\nکوئی بیک اپ نہیں بنایا گیا۔",
        'texts_saved_overwrite_with_backup': "تبدیلیاں اصل فائل پر محفوظ کر دی گئیں۔\n\nایک بیک اپ بنایا گیا۔",
        'texts_saved_overwrite_no_backup': "تبدیلیاں اصل فائل پر محفوظ کر دی گئیں۔\n\nکوئی بیک اپ نہیں بنایا گیا۔",
        'texts_crosses_saved_new_file': "{0} {1} اور {2} {3} داخل کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nایک نئی فائل بنائی گئی۔\n\nنئی PDF لوڈ ہو رہی ہے...",
        'texts_saved_new_file': "{0} {1} داخل کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nایک نئی فائل بنائی گئی۔\n\nنئی PDF لوڈ ہو رہی ہے...",
        'crosses_saved_new_file': "{0} {1} داخل کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nایک نئی فائل بنائی گئی۔\n\nنئی PDF لوڈ ہو رہی ہے...",
        'elements_saved_new_file': "{0} عناصر داخل کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nایک نئی فائل بنائی گئی۔\n\nنئی PDF لوڈ ہو رہی ہے...",
        'signatures_saved_overwrite_with_backup': "دستخط(ات) اصل فائل پر محفوظ کر دیے گئے۔\n\nایک بیک اپ بنایا گیا۔",
        'signatures_saved_overwrite_no_backup': "دستخط(ات) اصل فائل پر محفوظ کر دیے گئے۔\n\nکوئی بیک اپ نہیں بنایا گیا۔",
        'images_saved_overwrite_with_backup': "تصویر(یں) اصل فائل پر محفوظ کر دی گئیں۔\n\nایک بیک اپ بنایا گیا۔",
        'images_saved_overwrite_no_backup': "تصویر(یں) اصل فائل پر محفوظ کر دی گئیں۔\n\nکوئی بیک اپ نہیں بنایا گیا۔",
        'forms_saved_overwrite_with_backup': "شکل(یں) اصل فائل پر محفوظ کر دی گئیں۔\n\nایک بیک اپ بنایا گیا۔",
        'forms_saved_overwrite_no_backup': "شکل(یں) اصل فائل پر محفوظ کر دی گئیں۔\n\nکوئی بیک اپ نہیں بنایا گیا۔",
        'signatures_saved_new_file': "{0} دستخط داخل کر دیے گئے۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nایک نئی فائل بنائی گئی۔\n\nنئی PDF لوڈ ہو رہی ہے...",
        'images_saved_new_file': "{0} تصویریں داخل کر دی گئیں۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nایک نئی فائل بنائی گئی۔\n\nنئی PDF لوڈ ہو رہی ہے...",
        'forms_saved_new_file': "{0} شکلیں داخل کر دی گئیں۔\n\nاصل فائل تبدیل شدہ حالت میں رہی۔\nایک نئی فائل بنائی گئی۔\n\nنئی PDF لوڈ ہو رہی ہے...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "انتباہ: اس PDF میں گھمائے گئے صفحات ہیں۔ پوزیشننگ مختلف ہو سکتی ہے۔",
        'page_rotated_warning_title': "گھمایا ہوا صفحہ دریافت ہوا",
        'page_rotated_warning_message': "موجودہ صفحہ {0} {1}° گھمایا گیا ہے۔\n\nگھمائے گئے صفحات پر عناصر داخل کرنا تعاون یافتہ نہیں ہے۔\n\nکیا آپ صفحہ کو اب سیدھی پوزیشن پر گھمانا چاہتے ہیں؟",
        'page_rotated_warning_voice': "انتباہ: صفحہ گھمایا گیا ہے۔ براہ کرم پہلے اسے گھمائیں۔",
        'paste_on_rotated_page_simple_warning': "صفحہ {0} پر داخل کرنا ممکن نہیں!\n\nیہ صفحہ {1}° گھمایا گیا ہے۔\n\nبراہ کرم پہلے صفحہ کو 0° پر گھمائیں (مینو: ترمیم کریں → صفحہ سیدھ کریں)۔\n\nانتباہ:\nپہلے کاپی کیا گیا عنصر ضائع ہو جائے گا اگر آپ صفحہ گھمانے سے پہلے محفوظ نہیں کرتے۔",
        'paste_on_rotated_page_voice': "داخل کرنا منسوخ کر دیا گیا۔ صفحہ گھمایا گیا ہے۔ براہ کرم پہلے صفحہ سیدھ کریں۔",
        'page_rotated_cancel': "منسوخ کریں",
        'page_rotated_rotate_until_upright': "صفحہ کو بار بار گھمائیں (جب تک سیدھا نہ ہو جائے)",
        'page_rotated_now_upright': "صفحہ اب سیدھا ہے۔ اب آپ داخل کر سکتے ہیں۔",
        'page_rotated_still_not_upright': "صفحہ کو سیدھی پوزیشن پر نہیں گھمایا جا سکا۔ براہ کرم دستی طور پر درست کریں۔",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "مدد: گھمائے گئے صفحات کو درست کریں",
        'help_rotated_pages_voice': "گھمائے گئے صفحات کو درست کرنے کے لیے مدد کھل رہی ہے۔",
        'btn_help': "مدد",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 مسئلہ: گھمایا ہوا صفحہ – داخل کرنا صحیح طریقے سے کام نہیں کر رہا</p>

            <p>اگر گھمائے ہوئے صفحہ پر متن، دستخط یا شکلیں داخل کرنا صحیح طریقے سے کام نہیں کر رہا، تو آپ بیرونی PDF ایڈیٹر کے ذریعے صفحہ کو درست کر سکتے ہیں۔</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ بیرونی ٹول کے ساتھ حل (مثال کے طور پر macOS پیش منظر)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>صفحہ برآمد کریں</strong><br>
                &nbsp;&nbsp;مینو میں <strong>فائل → بطور صفحات برآمد کریں</strong> پر کلک کریں یا کوئی دوسرا طریقہ استعمال کریں تاکہ مطلوبہ صفحہ کو ایک PDF کے طور پر محفوظ کیا جا سکے۔</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>بیرونی پروگرام میں صفحہ کھولیں</strong><br>
                &nbsp;&nbsp;برآمد شدہ PDF کو PDF ایڈیٹر میں کھولیں (مثال کے طور پر <strong>macOS پیش منظر</strong>, Adobe Acrobat, PDF Expert)۔</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>صفحہ گھمائیں</strong><br>
                &nbsp;&nbsp;صفحہ کو اس طرح گھمائیں کہ وہ سیدھا ہو جائے (پیش منظر میں: <strong>اوزار → گھمائیں</strong> یا <strong>⌘ + R</strong>)۔</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>محفوظ کریں</strong><br>
                &nbsp;&nbsp;درست شدہ صفحہ محفوظ کریں (<strong>⌘ + S</strong>)۔</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>صفحہ کو دوبارہ اصل دستاویز میں داخل کریں</strong><br>
                &nbsp;&nbsp;PDFDarkView پر واپس جائیں اور درست شدہ صفحہ کو مطلوبہ پوزیشن پر داخل کریں:<br>
                &nbsp;&nbsp;<strong>ترمیم کریں → صفحات داخل کریں</strong>۔</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 متبادل: اصل فائل میں صفحہ گھمائیں</p>
                <p style="margin: 5px 0 5px 20px;">• بلٹ ان گھمانے کے فنکشن کا استعمال کریں (<strong>ترمیم کریں → صفحہ گھمائیں</strong>) صفحہ کو قدم بہ قدم درست کرنے کے لیے۔<br>
                • ہر گھماؤ کے بعد آپ جانچ سکتے ہیں کہ آیا داخل کرنا اب کام کرتا ہے۔<br>
                • یہ اکثر تیز تر حل ہوتا ہے – پہلے اسے آزمائیں!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ٹپ:</strong> اگر آپ اکثر گھمائے ہوئے صفحات کا سامنا کرتے ہیں، تو آپ داخل کرنے والے ڈائیلاگ میں انتباہ کو مستقل طور پر چھپا سکتے ہیں۔<br>
                پوزیشننگ پھر مختلف ہو سکتی ہے – یہ اختیار صرف اس صورت میں استعمال کریں جب آپ نتائج جانتے ہوں۔
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "صفحات سیدھ کریں",
        'menu_rotate_normalize_tooltip': "صفحہ گھمائیں یا 0° پر دوبارہ ترتیب دیں",
        'normalize_current_page': "موجودہ صفحہ کو سیدھی پوزیشن پر لائیں (0° پر سیٹ کریں)",
        'normalize_all_pages': "تمام صفحات کو سیدھی پوزیشن پر لائیں (0° پر سیٹ کریں)",
        'page_normalized': "صفحہ {0} کو سیدھی پوزیشن پر سیٹ کر دیا گیا۔",
        'all_pages_normalized': "تمام صفحات کو سیدھی پوزیشن پر سیٹ کر دیا گیا۔",
        'page_already_upright': "صفحہ {0} پہلے سے ہی سیدھا ہے۔",
        'all_pages_already_upright': "تمام صفحات پہلے سے ہی سیدھے ہیں۔",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF میں کوئی قابل تلاش متن نہیں ہے۔</p><p>کیا آپ {0} میں برآمد کرنے کے لیے OCR کرنا چاہتے ہیں؟</p>",
        'export_ocr_voice': "PDF میں کوئی متن نہیں ہے۔ {0} میں برآمد کرنے کے لیے OCR کی ضرورت ہے۔",
        'export_no_ocr_possible': "OCR کے بغیر برآمد ممکن نہیں۔ براہ کرم مینو کے ذریعے OCR کریں۔",
        'ocr_failed_export_not_possible': "OCR ناکام رہا۔ برآمد نہیں کیا جا سکتا۔",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF پیش منظر میں کھلے گا۔ براہ کرم پرنٹنگ کا عمل وہاں شروع کریں۔",
        'print_preview_manual': "PDF کھل گیا ہے۔ براہ کرم پرنٹ کمانڈ کو دستی طور پر چلائیں (مثال کے طور پر Ctrl+P)۔",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDFs کو ضم کریں",
        'merge_pdfs': "PDFs کو ضم کریں",
        'merge_progress_title': "PDFs کو ضم کیا جا رہا ہے...",
        'merge_pdfs_list': "ترتیب وار PDFs (ترتیب دینے کے لیے گھسیٹیں اور چھوڑیں)",
        'merge_add_pdf': "PDF شامل کریں",
        'merge_remove': "ہٹائیں",
        'merge_move_up': "اوپر",
        'merge_move_down': "نیچے",
        'merge_pdfs_info': "💡 ٹپ: آپ گھسیٹ کر چھوڑ کر ترتیب بدل سکتے ہیں",
        'merge_no_pdfs': "کوئی PDF منتخب نہیں کیا گیا۔ 'PDF شامل کریں' پر کلک کریں۔",
        'merge_info': "{0} PDFs منتخب کی گئیں (تقریباً {1} صفحات)",
        'merge_open_file': "فائل کھولیں",
        'merge_merge': "ضم کریں",
        'merge_error': "ضم کرتے وقت خرابی",
        'merge_min_two_pdfs_error': "براہ کرم ضم کرنے کے لیے کم از کم دو PDF فائلیں منتخب کریں۔",
        'merge_select_pdfs': "ضم کرنے کے لیے PDFs منتخب کریں",
        'merge_error_file': "پروسیسنگ کے دوران خرابی",
        'merge_cancelled': "ضم کرنا منسوخ کر دیا گیا",
        'merge_preparing': "تیاری کر رہا ہے...",
        'merge_processing': "{1} میں سے PDF {0} پر کارروائی کر رہا ہے",
        'merge_saving': "ضم شدہ PDF محفوظ کر رہا ہے...",
        'merge_complete': "مکمل!",
        'merge_success_title': "ضم کرنا کامیاب رہا",
        'merge_success_voice': "{0} PDFs کامیابی سے ضم ہو گئیں۔",
        'merge_success_message': "{0} PDFs کامیابی سے ضم ہو گئیں۔\n\nنئی دستاویز میں اب {1} صفحات ہیں۔\n\nنئی فائل:\n{2}\n\nمحفوظ کرنے کا مقام:\n{3}\n{2}\n\nکیا آپ یہ PDF کھولنا چاہتے ہیں؟",
        'replace_file_title': "فائل تبدیل کریں؟",
        'replace_file_message': "پہلے سے ہی ایک PDF کھلا ہوا ہے۔ کیا آپ اسے نئی فائل سے تبدیل کرنا چاہتے ہیں؟",
        'btn_yes': "ہاں",
        'btn_no': "نہیں",
        'filename_merge_suffix': "ضم شدہ",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "{0} کھولا جا رہا ہے...",
        'progress_merge_reading': "{0} پڑھا جا رہا ہے...",
        'progress_merge_adding': "{0} صفحات شامل کیے جا رہے ہیں...",
        'progress_merge_optimizing': "PDF کو بہتر بنایا جا رہا ہے...",
        'progress_merge_writing': "PDF لکھا جا رہا ہے...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF بند کرنا",
        'action_close_window': "ونڈو بند کرنا",
        'action_open_new_pdf': "نئی PDF کھولنا",
        'action_quit_app': "ایپلیکیشن سے باہر جانا",
        'changes_saved': "تبدیلیاں محفوظ کر دی گئیں۔",
        'file_close_title': "PDF فائل بند کریں",
        'save_before_action': "کیا {0} سے پہلے تبدیلیاں محفوظ کی جائیں؟ ہاں یا نہیں؟",
        'save_before_action_voice': "کیا {0} سے پہلے تبدیلیاں محفوظ کی جائیں؟ ہاں یا نہیں؟",
        'save_before_close_question': "کیا بند کرنے سے پہلے تبدیلیاں محفوظ کی جائیں؟ ہاں یا نہیں؟",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>قابل تلاش PDF تخلیق ہوا:\n\n{0}\n\n<b>اگر ضرورت ہو تو دوبارہ کوشش کریں",
        "ocr_rotate_title": "OCR سے پہلے صفحات کو سیدھ کریں",
        "ocr_rotate_question": "PDF میں گھمائے ہوئے صفحات ہیں۔\nکیا آپ OCR سے پہلے تمام صفحات کو 0° پر سیدھ کرنا چاہتے ہیں؟\nاس سے متن کی شناخت میں نمایاں بہتری آتی ہے۔",
        "ocr_rotate_yes": "ہاں، سیدھ کریں",
        "ocr_rotate_no": "نہیں، براہ راست OCR شروع کریں",
        "ocr_rotate_voice": "PDF میں گھمائے ہوئے صفحات ہیں۔ کیا OCR سے پہلے تمام صفحات کو سیدھ کیا جانا چاہئے؟",
        "ocr_not_performed_message": "کوئی متن موجود نہیں۔ براہ کرم OCR کریں (مینو \"ترمیم\" → \"OCR کریں\" یا Ctrl+R کلید)。",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR ترتیبات",
        "ocr_language_btn": "OCR زبان منتخب کریں",
        "ocr_language": "OCR زبان(یں)",
        "ocr_language_current": "موجودہ زبان:",
        "ocr_param_info": "پیرامیٹر کے بارے میں معلومات",

        "ocr_force_ocr_label": "OCR مجبور کریں",
        "ocr_deskew_label": "جھکاؤ درست کریں",
        "ocr_clean_label": "تصویر صاف کریں",
        "ocr_oversample_label": "ریزولوشن (DPI)",
        "ocr_pagesegmode_label": "صفحہ کی تقسیم",
        "ocr_oem_label": "OCR انجن موڈ",
        "ocr_optimize_label": "PDF کمپریشن",
        "ocr_jobs_label": "متوازی عمل",
        "ocr_verbose_label": "لاگ کی تفصیل",

        "ocr_force_ocr_tooltip": "ہر صفحے پر OCR مجبور کریں، چاہے متن پہلے سے موجود ہو",
        "ocr_deskew_tooltip": "خودکار طور پر جھکے ہوئے اسکینز کو سیدھ کریں",
        "ocr_clean_tooltip": "تصویر سے شور اور آرٹیفیکٹس ہٹائیں",
        "ocr_oversample_tooltip": "OCR سے پہلے تصویر کو اس DPI تک بڑا کریں",
        "ocr_pagesegmode_tooltip": "یہ طے کرتا ہے کہ صفحہ کو متن کے علاقوں میں کیسے تقسیم کیا جائے",
        "ocr_oem_tooltip": "Tesseract کا OCR انجن منتخب کرتا ہے",
        "ocr_optimize_tooltip": "آؤٹ پٹ PDF کی کمپریشن سطح",
        "ocr_jobs_tooltip": "متوازی OCR عملوں کی تعداد",
        "ocr_verbose_tooltip": "لاگ آؤٹ پٹ کی تفصیل کی سطح",
        "ocr_settings_explain_btn": "وضاحت",

        "ocr_force_ocr_explain": "<b>ہر</b> صفحے پر متن کی شناخت مجبور کرتا ہے (چاہے اس میں پہلے سے متن موجود ہو)۔\n\nتجویز: اسکین شدہ PDF کے لیے <b>آن</b>، پہلے سے موجود متن والے اصلی PDF کے لیے <b>آف</b>۔",

        "ocr_deskew_explain": "ہلکے جھکے ہوئے اسکینز کو درست کرتا ہے (تقریباً 5° تک)۔\n\nتجویز: اسکین شدہ دستاویزات کے لیے <b>آن</b>، اگر صفحات پہلے سے مکمل طور پر سیدھے ہیں تو <b>آف</b>۔",

        "ocr_clean_explain": "تصویر سے شور، نقطوں اور چھوٹے آرٹیفیکٹس کو ہٹاتا ہے۔\n<b>اہم:</b> عربی، تھائی یا ویتنامی متون کے لیے جن میں علاماتِ تشدید ہیں (حروف کے اوپر/نیچے نقطے) اس آپشن کو <b>غیرفعال</b> کیا جانا چاہئے، ورنہ اہم حروف ضائع ہو سکتے ہیں۔",

        "ocr_oversample_explain": "مخصوص DPI پر <b>متن کی شناخت سے پہلے</b> تصویر کو بڑا کرتا ہے۔<br><br>• <b>72-150 DPI:</b> بہت تیز، لیکن کم شناخت کی شرح<br>• <b>200-300 DPI:</b> بہترین حدود (طے شدہ: 300)<br>• <b>400+ DPI:</b> بمشکل بہتر شناخت، لیکن نمایاں طور پر بڑی فائلیں<br><br>تجویز: پیچیدہ رسم الخط کے لیے 300 DPI (عربی، چینی، جاپانی)، مغربی زبانوں کے لیے 200 DPI۔",

        "ocr_pagesegmode_explain": "یہ طے کرتا ہے کہ Tesseract صفحہ کو متن کے علاقوں میں کیسے تقسیم کرتا ہے۔\n\n• <b>3 - خودکار (طے شدہ):</b> مخلوط ترتیب کے لیے اچھا\n• <b>4 - ایک کالم:</b> ایک کالم والے متن کے لیے\n• <b>5 - عمودی بلاک:</b> عمودی رسم الخط کے لیے (جاپانی، چینی)\n• <b>6 - یکساں متن کا بلاک:</b> بغیر کالم کے بہتے ہوئے متن کے لیے بہترین\n• <b>11 - خام تصویر:</b> خراب اسکین / ہاتھ کی تحریر کے لیے\n\nتجویز: سادہ متن کی دستاویزات کے لیے <b>6</b>، پیچیدہ ترتیب کے لیے <b>3</b>۔",

        "ocr_oem_explain": "Tesseract کا OCR انجن منتخب کرتا ہے۔\n\n• <b>0 - Legacy:</b> پرانا انجن (تیز، لیکن کم درست)\n• <b>1 - LSTM:</b> اعصابی انجن (سست، لیکن زیادہ درست)\n• <b>2 - Legacy + LSTM:</b> دونوں نتائج کو یکجا کرتا ہے\n• <b>3 - طے شدہ (LSTM ترجیح دی جاتی ہے):</b> زیادہ تر معاملات کے لیے بہترین انتخاب\n\nتجویز: زیادہ سے زیادہ شناخت کی درستگی کے لیے <b>3</b>۔",

        "ocr_optimize_explain": "آؤٹ پٹ PDF کو سکیڑتا ہے۔\n\n• <b>0:</b> کوئی اصلاح نہیں (تیز ترین پروسیسنگ)\n• <b>1:</b> ہلکی اصلاح (اچھا سمجھوتہ)\n• <b>2:</b> معتدل اصلاح\n• <b>3:</b> مضبوط اصلاح (سب سے چھوٹی فائل، لیکن سست)\n\nتجویز: روزمرہ استعمال کے لیے <b>1</b>۔",

        "ocr_jobs_explain": "OCR کے لیے متوازی عملوں کی تعداد۔\n\n• <b>1:</b> سست، لیکن سب سے کم میموری استعمال\n• <b>4-8:</b> جدید ملٹی کور پروسیسرز کے لیے بہترین\n• <b>12+:</b> زیادہ میموری استعمال کے ساتھ بمشکل تیز پروسیسنگ\n\nتجویز: CPU کور کی تعداد (مثلاً 4 کور والے نظاموں پر <b>4</b>)۔",

        "ocr_verbose_explain": "کنسول میں لاگ آؤٹ پٹ کی تفصیل کی سطح۔\n\n• <b>0:</b> کوئی آؤٹ پٹ نہیں\n• <b>1:</b> پیش رفت اور حیثیت کے پیغامات\n• <b>2:</b> تفصیلی آؤٹ پٹ\n• <b>3:</b> مکمل ڈیبگ آؤٹ پٹ (بہت وسیع)\n\nتجویز: عام آپریشن کے لیے <b>1</b>۔",

        "ocr_reset_title": "ترتیبات دوبارہ طے کر دی گئیں",
        "ocr_reset_message": "تمام OCR ترتیبات کو طے شدہ اقدار پر دوبارہ ترتیب دے دیا گیا۔",
        "info_tooltip": "اس پیرامیٹر کے بارے میں مزید معلومات",
        "ocr_reset_defaults": "طے شدہ پر دوبارہ ترتیب دیں",

        "ocr_psm_0": "خودکار (Legacy انجن)",
        "ocr_psm_1": "خودکار کالم کا پتہ لگانا",
        "ocr_psm_3": "خودکار (طے شدہ)",
        "ocr_psm_4": "ایک کالم",
        "ocr_psm_5": "عمودی بلاک",
        "ocr_psm_6": "یکساں متن کا بلاک",
        "ocr_psm_7": "متن کی ایک لائن",
        "ocr_psm_8": "ایک لفظ",
        "ocr_psm_11": "خام تصویر (کوئی ترتیب تجزیہ نہیں)",

        "ocr_oem_0": "Legacy انجن (تیز)",
        "ocr_oem_1": "LSTM انجن (اعصابی، درست)",
        "ocr_oem_2": "Legacy + LSTM یکجا",
        "ocr_oem_3": "طے شدہ (LSTM ترجیح دی جاتی ہے)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR زبان(یں)...",
        "ocr_language_title": "OCR زبان(یں) منتخب کریں",
        "ocr_language_instruction": "متن کی شناخت (OCR) کے لیے زبان(یں) منتخب کریں۔\nاحتیاط: متعدد زبانیں کارکردگی اور درستگی کی قیمت پر آتی ہیں!\nآپ بہترین نتائج حاصل کرتے ہیں اگر آپ صرف ایک زبان منتخب کریں۔",
        "ocr_language_predefined": "پہلے سے طے شدہ مجموعے",
        "ocr_language_custom": "اپنی مرضی...",
        "ocr_language_selected": "منتخب کردہ OCR زبانیں",
        "ocr_language_changed": "OCR زبان {0} میں تبدیل کر دی گئی",
        "ocr_language_auto_detect": "دستیاب زبانیں خودکار طریقے سے دریافت ہو جاتی ہیں۔",
        "ocr_language_none_found": "کوئی Tesseract زبان کا ڈیٹا نہیں ملا! براہ کرم زبان کے پیکجز انسٹال کریں (مثلاً 'tesseract-ocr-deu', 'tesseract-ocr-eng')۔",
        "ocr_language_select_custom": "اپنی مرضی کی زبان کا انتخاب",
        "ocr_language_available": "دستیاب زبانیں (انسٹال شدہ):",
        "ocr_language_select_hint": "ایک یا زیادہ زبانیں منتخب کریں:",
        "ocr_language_confirm": "لگائیں",
        "ocr_language_reset": "طے شدہ پر دوبارہ ترتیب دیں (deu+eng+vie)",
        "ocr_language_priorities": "تجویز کردہ زبانیں (پہلے سے انسٹال شدہ):",

        "select_all_languages": "سب منتخب کریں",
        "clear_all_languages": "انتخاب صاف کریں",
        "install_language_packs": "گمشدہ زبان کے پیکجز انسٹال کریں...",
        "install_hint": "💡 اشارہ: آپ کے سسٹم پر تمام زبانیں انسٹال نہیں ہیں۔ اس بٹن کے ذریعے آپ کو انسٹالیشن میں مدد ملے گی۔",
        "ocr_language_install_title": "Tesseract زبان کے پیکجز کی انسٹالیشن",

        "ocr_missing_languages": "گمشدہ OCR زبان کے پیکجز",
        "ocr_missing_languages_message": "درج ذیل منتخب کردہ زبانیں آپ کے سسٹم پر انسٹال نہیں ہیں:\n\n{0}\n\nبراہ کرم گمشدہ زبان کے پیکجز انسٹال کریں ('انسٹالیشن مدد' کے تحت مدد دیکھیں)۔\n\nکیا آپ اب انسٹالیشن مدد کھولنا چاہتے ہیں؟",
        "ocr_missing_languages_voice": "گمشدہ زبان کے پیکجز۔ براہ کرم گمشدہ زبانیں انسٹال کریں۔",
        "ocr_install_help_now": "مدد کھولیں",
        "ocr_continue_anyway": "بہرحال کوشش کریں",
        "ocr_language_error_title": "OCR زبان کی خرابی",
        "ocr_language_error_message": "متن کی شناخت کے دوران خرابی: {0}\n\nبراہ کرم اپنی OCR زبان کی ترتیبات چیک کریں (ترتیبات → OCR زبان)۔",
        "ocr_install_help_button": "انسٹالیشن مدد",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract زبان کے پیکجز انسٹال کریں</p>

        <p>OCR کو کسی خاص زبان میں کام کرنے کے لیے، متعلقہ زبان کا ڈیٹا آپ کے سسٹم پر انسٹال ہونا ضروری ہے۔ اپنے آپریٹنگ سسٹم کے لیے ہدایات پر عمل کریں:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li><strong>ٹرمینل</strong> کھولیں (Finder → پروگرام → افادیت → ٹرمینل)۔</li>
        <li>تمام دستیاب زبانیں انسٹال کریں:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
> (اس میں کچھ منٹ لگ سکتے ہیں۔)</li>
        <li>یا صرف انفرادی زبانیں (مثلاً ویتنامی):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
> موجودہ Homebrew ورژن کے ساتھ، <code>*.traineddata</code> کو دستی طور پر ڈاؤن لوڈ کرنے کی ضرورت پڑ سکتی ہے (نیچے دیکھیں)۔</li>
        <li>انسٹالیشن کے بعد: اس ڈائیلاگ کو بند کریں اور OCR زبان کے انتخاب کو دوبارہ کھولیں – نئی زبانیں خودکار طور پر ظاہر ہو جائیں گی۔</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>ٹرمینل کھولیں (Ctrl+Alt+T)۔</li>
        <li>مطلوبہ زبان انسٹال کریں، مثلاً ویتنامی کے لیے:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        اہم زبان کے کوڈز: <code>deu</code> (جرمن), <code>eng</code> (انگریزی), <code>vie</code> (ویتنامی), <code>spa</code> (ہسپانوی), <code>fra</code> (فرانسیسی), <code>ita</code> (اطالوی), <code>nld</code> (ڈچ), <code>fin</code> (فینیش), <code>swe</code> (سویڈش), <code>nor</code> (نارویجین)۔</li>
        <li>تمام دستیاب پیکجز دکھائیں:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (دستی)</p>
        <ol>
        <li>مطلوبہ <code>*.traineddata</code> فائلیں یہاں سے ڈاؤن لوڈ کریں:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (مثلاً ویتنامی کے لیے <code>vie.traineddata</code>)۔</li>
        <li>فائلوں کو Tesseract کی زبان والی فولڈر میں کاپی کریں، عام طور پر:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (انفرادی انسٹالیشن کے مطابق ترتیب دیں۔)</li>
        <li>ایپلیکیشن کو دوبارہ شروع کریں (یا OCR زبان کے انتخاب کو دوبارہ کھولیں)۔</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 تمام سسٹمز کے لیے متبادل</p>
        <ul>
        <li>اپنی پسند کے پیکیج مینیجر کے ساتھ <strong>OCRmyPDF</strong> اور <strong>Tesseract</strong> انسٹال کریں۔ زیادہ تر انسٹالیشنز میں پہلے سے ہی کچھ معیاری زبانیں موجود ہوتی ہیں (انگریزی، جرمن، فرانسیسی)۔</li>
        <li>گمشدہ زبانیں کسی بھی وقت انسٹال کی جا سکتی ہیں – OCR زبان کا انتخاب صرف حقیقت میں موجود زبانوں کی فہرست دیتا ہے۔</li>
        </ul>

        <hr>
        <p><b>✅ انسٹالیشن کے بعد:</b> ایپلیکیشن کو دوبارہ شروع کرنے کی ضرورت نہیں – نئی شامل کردہ زبانیں فوری طور پر فہرست میں ظاہر ہو جائیں گی۔</p>
        <p><b>📖 زبان کے کوڈز کے لیے مدد:</b> ایک مکمل فہرست <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract دستاویزات</a> میں دستیاب ہے۔</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans فونٹس",
        "info_noto_font_voice": "Noto Sans فونٹس انسٹالیشن گائیڈ",
        "btn_info_noto_font_install": "فونٹ کی معلومات",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word; direction: ltr; text-align: left;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Google کے مفت Noto فونٹس کیسے انسٹال کریں</h2>

        <p><strong>Noto فونٹس</strong> Google کا ایک اوپن سورس فونٹ فیملی ہے۔ ان کا مقصد <em>"کوئی ٹوفو نہیں"</em> (یعنی خالی خانے □ نہیں) دیکھنا اور یونیکوڈ معیار کے ہر حرف کو صحیح طریقے سے دکھانا ہے۔ یہ ان ایپلیکیشنز کے لیے مثالی اضافہ ہیں جنہیں بہت سی مختلف زبانوں میں متن دکھانے کی ضرورت ہوتی ہے۔</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 macOS پر انسٹالیشن</h3>

        <p><strong>طریقہ 1: Homebrew کے ساتھ (اعلی درجے کے صارفین کے لیے)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>طریقہ 2: "فونٹ بک" کے ذریعے (تجویز کردہ)</strong></p>

        <ol>
        <li>سرکاری فونٹ پیکج ڈاؤن لوڈ کریں:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP فائل نکالیں</li>
        <li>فائلوں کو <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code> میں کاپی کریں</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Windows پر انسٹالیشن (10 اور 11)</h3>

        <p><strong>طریقہ 1: Microsoft Store (تجویز کردہ)</strong><br>
        "Google Noto Fonts" یا "Noto Sans" تلاش کریں اور <strong>انسٹال کریں</strong> پر کلک کریں۔</p>

        <p><strong>طریقہ 2: دستی انسٹالیشن</strong></p>

        <ol>
        <li>ڈاؤن لوڈ کریں:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP نکالیں</li>
        <li>.ttf / .otf فائلیں منتخب کریں</li>
        <li>دائیں کلک کریں → <strong>انسٹال کریں</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        یا<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\نام\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Linux پر انسٹالیشن</h3>

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

        <p>تصدیق:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "بک مارکس کا انتظام کریں",
        "bookmark_add": "بک مارک شامل کریں",
        "bookmark_add_tooltip": "موجودہ صفحہ کو بک مارک کے طور پر محفوظ کریں",
        "bookmark_remove": "بک مارک ہٹائیں",
        "bookmark_remove_tooltip": "نشان زدہ بک مارک کو حذف کریں",
        "bookmark_remove_all": "سب ہٹائیں",
        "bookmark_remove_all_tooltip": "اس PDF کے تمام بک مارکس حذف کریں",
        "bookmark_jump": "بک مارک پر جائیں",
        "bookmark_jump_tooltip": "منتخب کردہ صفحہ پر جائیں",
        "bookmark_name": "نام",
        "bookmark_page": "صفحہ",
        "bookmark_no_bookmarks": "کوئی بک مارک موجود نہیں۔\nموجودہ صفحہ کو بک مارک کے طور پر محفوظ کرنے کے لیے 'شامل کریں' پر کلک کریں۔",
        "bookmark_added": "صفحہ {0} کے لیے بک مارک شامل کیا گیا: {1}",
        "bookmark_removed": "بک مارک ہٹا دیا گیا: {0}",
        "bookmark_all_removed": "تمام بک مارکس ہٹا دیئے گئے۔",
        "bookmark_name_default": "صفحہ {0}",
        "bookmark_name_prompt": "بک مارک کے لیے نام:\n(لمبا متن 50 حروف تک مختصر کیا جائے گا)",
        "bookmark_name_prompt_title": "بک مارک کا نام",
        "bookmark_confirm_remove_all": "کیا آپ واقعی تمام {0} بک مارکس کو ہٹانا چاہتے ہیں؟",
        "menu_bookmarks": "بک مارکس",
        "bookmark_manage": "بک مارکس کا انتظام کریں",
        "bookmark_next": "اگلا بک مارک",
        "bookmark_prev": "پچھلا بک مارک",
        "bookmark_page_display": "صفحہ {0}",
        "bookmark_exists": "اس صفحہ کے لیے اس نام سے ایک بک مارک پہلے سے موجود ہے۔",
        "bookmark_select_first": "براہ کرم پہلے ایک بک مارک منتخب کریں۔",
        "bookmark_confirm_remove": "کیا آپ واقعی 'صفحہ {0}: {1}' بک مارک کو ہٹانا چاہتے ہیں؟",
        "bookmark_jumped_to": "صفحہ {1} پر بک مارک '{0}' پر چلے گئے۔",
        "bookmark_jumped_to_voice": "بک مارک {0}، صفحہ {1}",
        "btn_close": "بند کریں",

        "bookmark_list": "آپ کے بک مارکس",
        "bookmark_rename": "بک مارک کا نام تبدیل کریں",
        "bookmark_rename_tooltip": "منتخب کردہ بک مارک کا نام تبدیل کریں",
        "bookmark_rename_title": "بک مارک کا نام تبدیل کریں",
        "bookmark_rename_prompt": "صفحہ {0} پر بک مارک کے لیے نیا نام:\n(زیادہ سے زیادہ 50 حروف)",
        "bookmark_renamed": "بک مارک '{0}' کا نام تبدیل کر کے '{1}' کر دیا گیا۔",
        "bookmark_item_tooltip": "صفحہ {0}: {1}\nجانے کے لیے ڈبل کلک کریں",
        "bookmark_name_exists_question": "اس صفحہ پر پہلے سے '{0}' نام کا بک مارک موجود ہے۔\nبہرحال نام تبدیل کریں؟",

        "context_bookmarks": "بک مارکس",
        "context_bookmark_add_here": "اس صفحہ کے لیے بک مارک شامل کریں",
        "context_bookmarks_existing": "موجودہ بک مارکس:",
        "context_bookmarks_jump": "بک مارک پر جائیں:",
        "context_bookmarks_none": "کوئی بک مارک موجود نہیں",
        "context_bookmarks_clear_all": "تمام {0} بک مارکس ہٹائیں",

        "bookmark_search_placeholder": "بک مارکس تلاش کریں... (نام یا صفحہ)",
        "bookmark_search_results": "\"%s\" کے لیے %d بک مارکس ملے",
        "bookmark_no_search_results": "\"%s\" کے لیے کوئی بک مارک نہیں ملا",
        "bookmark_no_search_results_label": "\"%s\" کے لیے کوئی نتیجہ نہیں",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF میٹا ڈیٹا میں ترمیم کریں",
        "metadata_title": "عنوان",
        "metadata_title_placeholder": "دستاویز کا عنوان",
        "metadata_title_tooltip": "دستاویز کا عنوان (ٹائٹل بار میں دکھایا جاتا ہے)",
        "metadata_author": "مصنف",
        "metadata_author_placeholder": "مصنف کا نام",
        "metadata_author_tooltip": "دستاویز کا تخلیق کار",
        "metadata_subject": "موضوع",
        "metadata_subject_placeholder": "دستاویز کا موضوع",
        "metadata_subject_tooltip": "مواد کی مختصر وضاحت",
        "metadata_keywords": "کلیدی الفاظ",
        "metadata_keywords_placeholder": "کوما سے جدا کردہ کلیدی الفاظ",
        "metadata_keywords_tooltip": "دستاویز کی درجہ بندی کے لیے کلیدی الفاظ",
        "metadata_creator": "تخلیق کار",
        "metadata_creator_placeholder": "وہ ایپلیکیشن جس نے PDF تخلیق کیا",
        "metadata_creator_tooltip": "وہ سافٹ ویئر جس کے ساتھ دستاویز تخلیق کی گئی",
        "metadata_producer": "پروڈیوسر",
        "metadata_producer_placeholder": "وہ ایپلیکیشن جس نے PDF تبدیل کیا",
        "metadata_producer_tooltip": "وہ سافٹ ویئر جس نے PDF تبدیل کیا",
        "metadata_creation_date": "تخلیق کی تاریخ",
        "metadata_creation_date_tooltip": "دستاویز کی تخلیق کی تاریخ",
        "metadata_mod_date": "ترمیم کی تاریخ",
        "metadata_mod_date_tooltip": "آخری ترمیم کی تاریخ",
        "metadata_pdf_info": "📄 PDF معلومات",
        "metadata_pages": "صفحات کی تعداد",
        "metadata_file_size": "فائل کا حجم",
        "metadata_pdf_version": "PDF ورژن",
        "metadata_encrypted": "خفیہ کردہ",
        "metadata_encrypted_yes": "ہاں (پاس ورڈ سے محفوظ)",
        "metadata_encrypted_no": "نہیں",
        "metadata_reload": "📂 PDF سے دوبارہ لوڈ کریں",
        "metadata_reset": "تبدیلیاں مسترد کریں",
        "metadata_reloaded": "میٹا ڈیٹا PDF سے دوبارہ لوڈ کر دیا گیا۔",
        "metadata_reset_done": "تمام میٹا ڈیٹا فیلڈز دوبارہ ترتیب دے دی گئیں۔",
        "metadata_no_file": "کوئی PDF فائل لوڈ نہیں ہوئی۔",
        "metadata_save_error": "میٹا ڈیٹا محفوظ کرتے وقت خرابی",
        "metadata_saved": "میٹا ڈیٹا کامیابی سے محفوظ ہو گیا۔",
        "metadata_pdf_version_unknown": "PDF (نامعلوم)",
        "metadata_saved_message": "میٹا ڈیٹا کامیابی سے محفوظ ہو گیا۔",
        "metadata_saved_voice": "میٹا ڈیٹا محفوظ ہو گیا۔",

        "metadata_custom": "🔧 اپنی مرضی کا میٹا ڈیٹا",
        "metadata_custom_placeholder": "{\n  \"میرا_فیلڈ\": \"میری_قدر\",\n  \"دوسرا_فیلڈ\": 123\n}",
        "metadata_custom_tooltip": "اپنی مرضی کے میٹا ڈیٹا کے لیے JSON فارمیٹ (اختیاری)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "سانچہ \"{0}\" منتخب ہوا - داخل کرنے کے لیے ڈبل کلک کریں",
        "text_use_template": "متن کا بلاک استعمال کریں",
        "text_type": "قسم",
        "text_search_templates": "متن کے بلاکس تلاش کریں...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 برآمد / درآمد کی معلومات",
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
            direction: ltr;
            text-align: left;
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

        <h3>📦 کیا برآمد کیا جاتا ہے؟ (جائزہ)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">عام ایپلیکیشن ترتیبات</span></li>
            <li class="detail">• سیاہ/روشن موڈ</li>
            <li class="detail">• تصاویر کے لیے سیاہ موڈ کا الٹ</li>
            <li class="detail">• سرمئی حد قدر</li>
            <li class="detail">• زبان</li>
            <li class="detail">• ونڈو جیومیٹری</li>
            <li class="detail">• زوم موڈ</li>
            <li class="detail">• نیویگیشن (نیویگیشن بار نظر آتا ہے)</li>
            <li class="detail">• تقریر آؤٹ پٹ (آن/آف)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">بیک اپ ترتیبات</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">فائل کا نام دینا (ٹائم سٹیمپ، جداکار، لاحقے)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">داخل کرنے کی ترتیبات</span></li>
            <li class="detail">• دستخط</li>
            <li class="detail">• متن اور متن کے بلاک</li>
            <li class="detail">• نشان، تصاویر اور شکلیں</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR ترتیبات</span></li>
            <li class="detail">• زبان</li>
            <li class="detail">• OCR مجبور کریں · صفحہ موڈ</li>
            <li class="detail">• تصویر کی پیشگی پروسیسنگ: جھکاؤ درست کریں، صاف کریں، اوور سیمپلنگ</li>
            <li class="detail">• متوازی کاموں کی تعداد</li>
            <li class="detail">• الٹ موڈ</li>
            <li class="detail">• سرمئی حد قدر</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">بک مارکس</span></li>
            <li class="detail">• فی PDF فائل تمام بک مارکس (صفحہ، نام، تخلیق کا وقت)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">پاس ورڈ ڈیٹا بیس</span></li>
            <li class="detail">• محفوظ کردہ PDF پاس ورڈز (اختیاری طور پر خفیہ کردہ یا سادہ متن)</li>
            <li class="detail">• ماسٹر پاس ورڈ ہیش (اگر سیٹ کیا گیا ہو)</li>
            <li class="detail">• توثیق کا ڈیٹا</li>
        </ul>

        <h4>⚠️ اہم نوٹس</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 درآمد کرتے وقت:</strong>
            <ul>
                <li><span class="warning">➜ تمام موجودہ ترتیبات مکمل طور پر بدل دی جائیں گی</span></li>
                <li>• ایپلیکیشن کو دوبارہ شروع کرنا لازمی ہے</li>
                <li>• موجودہ دستخط، متن کے بلاک اور بک مارکس تبدیل کر دیئے جائیں گے</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 ماسٹر پاس ورڈ اور برآمد موڈ:</strong>
            <ul>
                <li>• جب ماسٹر پاس ورڈ فعال ہو، آپ انتخاب کر سکتے ہیں:</li>
                <li>  - <span style="color: #98FB98;"><strong>خفیہ کشودہ</strong></span> (پاس ورڈز ZIP میں سادہ متن میں ہوتے ہیں)</li>
                <li>  - <span style="color: #FFA07A;"><strong>خفیہ کردہ</strong></span> (صرف ماسٹر پاس ورڈ کے ساتھ ہدف کے نظام پر پڑھے جا سکتے ہیں)</li>
                <li>• ماسٹر پاس ورڈ ہیش <strong>ہمیشہ</strong> خفیہ کر کے محفوظ کیا جاتا ہے</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ سیکورٹی نوٹس:</strong>
            <ul>
                <li>• برآمد کردہ ZIP فائل میں حساس ڈیٹا ہوتا ہے (<strong>پاس ورڈز، بک مارکس، دستخط</strong>)</li>
                <li>• براہ کرم اسے محفوظ جگہ پر رکھیں (مثلاً خفیہ کردہ USB اسٹک، پاس ورڈ مینیجر)</li>
                <li>• اگر فائل گم ہو جائے تو، محفوظ کردہ PDF پاس ورڈز ناقابل واپسی طور پر ضائع ہو جائیں گے</li>
            </ul>
        </div>

        <h4>📁 برآمد فارمیٹ</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            ترتیبات ایک واحد ZIP فائل میں محفوظ کی جاتی ہیں:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            اس ZIP میں مکمل <code>settings.json</code> (آپ کی ترتیب سے) کے ساتھ ساتھ ممکنہ طور پر سرایت شدہ دستخط کی تصویری فائلیں اور خفیہ کردہ پاس ورڈز شامل ہیں۔
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "دستخط - رہنما",
        'signature_guide_html': """
        📝 <strong>دستخط - فوری رہنما</strong><br>
        <ul>
        <li>ماسٹر پاس ورڈ مرتب کریں</li>
        <li><em>ترتیبات</em> مینو میں دستخط ترتیب دیں (سائز، ٹائم اسٹیمپ، …)</li>
        <li>مطلوبہ مقام پر <strong>دائیں کلک</strong> کے ساتھ داخل کریں (ماسٹر پاس ورڈ فی سیشن ایک بار درکار ہے)</li>
        <li>ماؤس یا تیر والی کلیدوں سے دستخط منتقل کریں</li>
        <li>ایک کے بعد ایک کئی دستخط داخل کریں</li>
        <li>ہر دستخط کو انفرادی طور پر اپنی مرضی کے مطابق بنائیں</li>
        <li>ایک دستخط کو مسترد کریں</li>
        <li>تمام دستخط ایک ساتھ محفوظ / مسترد کریں</li>
        <li>متبادل طور پر، مینو بار بھی استعمال کیا جا سکتا ہے۔</li>
        </ul>
        """,
        'signature_guide_voice': "دستخطوں کے لیے فوری رہنما۔ ماسٹر پاس ورڈ مرتب کریں۔ ترتیبات میں دستخط ترتیب دیں۔ دائیں کلک کے ساتھ داخل کریں۔",

        'image_guide_title': "تصاویر داخل کریں - رہنما",
        'image_guide_html': """
        📷 <strong>پی ڈی ایف میں تصاویر داخل کریں - فوری رہنما</strong><br>
        <ol>
        <li>مطلوبہ مقام پر دائیں کلک کریں</li>
        <li><em>„تصویر داخل کریں“</em> → تصویر منتخب کریں</li>
        <li>تصویر کی پوزیشن مقرر کریں: ماؤس سے گھسیٹیں</li>
        <li>سائز ایڈجسٹ کریں: کونوں/کناروں سے گھسیٹیں</li>
        <li>پہلو تناسب برقرار رکھیں: <strong>[A]</strong> کلید</li>
        <li>مزید ایڈجسٹمنٹ: تصویر پر دائیں کلک کریں</li>
        </ol>
        <p><strong>ٹپ:</strong> سیاق و سباق کے مینو میں آپ ترتیبات ایڈجسٹ کر سکتے ہیں۔</p>
        """,
        'image_guide_voice': "تصاویر کے لیے فوری رہنما۔ دائیں کلک، تصویر داخل کریں، منتخب کریں۔ ماؤس سے پوزیشن مقرر کریں، کونوں پر سائز ایڈجسٹ کریں۔ A کلید سے پہلو تناسب۔",

        'form_guide_title': "شکلیں داخل کریں - رہنما",
        'form_guide_html': """
        📐 <strong>پی ڈی ایف میں شکلیں داخل کریں - فوری رہنما</strong><br>
        <ol>
        <li>شکل کی قسم منتخب کریں (مستطیل، بیضوی، لکیر، تیر)</li>
        <li>پوزیشن پر کلک کریں:
            <ul>
            <li>مستطیل/بیضوی کے لیے: ایک کلک شکل رکھتا ہے</li>
            <li>لکیر/تیر کے لیے: شروع اور اختتامی نقطہ کے لیے دو کلک</li>
            </ul>
        </li>
        <li>شکل کی پوزیشن مقرر کریں: ماؤس سے گھسیٹیں</li>
        <li>سائز ایڈجسٹ کریں: کونوں/کناروں سے گھسیٹیں</li>
        <li>شکل محفوظ کریں: <strong>Enter</strong></li>
        <li>شکل مسترد کریں: <strong>ESC</strong></li>
        <li>مزید ایڈجسٹمنٹ: شکل پر دائیں کلک کریں</li>
        </ol>
        <p><strong>ٹپ:</strong> سیاق و سباق کے مینو میں آپ ترتیبات ایڈجسٹ کر سکتے ہیں۔</p>
        """,
        'form_guide_voice': "شکلوں کے لیے فوری رہنما۔ شکل کی قسم منتخب کریں۔ مستطیل یا بیضوی کے لیے ایک بار کلک کریں، لکیر یا تیر کے لیے دو بار۔ ماؤس سے پوزیشن مقرر کریں، کونوں پر سائز ایڈجسٹ کریں۔ Enter سے محفوظ کریں، Escape سے مسترد کریں۔",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "پچھلا",
        "btn_next_result": "اگلا",
        "ocr_text_window": "OCR متن کی ونڈو",
        "bookmark_existing": "موجودہ بک مارکس",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR موازنہ Mac - Windows",
        'ocr_method_mac_win_title': "Mac اور Windows کے درمیان OCR فرق",
        'ocr_method_mac_win_voice': "Mac بہتر ہے",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – macOS اور Windows کے درمیان فرق</strong></p>

        <p><strong>macOS (تجویز کردہ)</strong></p>
        <p>ٹول:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>نتیجہ:</p>
        <ul>
        <li>ایک قابل تلاش PDF جس میں ایمبیڈڈ متن ہے جو اصل ترتیب کو بڑی حد تک محفوظ رکھتا ہے۔</li>
        </ul>
        <p>فوائد:</p>
        <ul>
        <li>متن کی شناخت کا بہترین معیار (ٹیڑھے صفحات پر بھی)۔</li>
        <li>ویکٹر گرافکس اور فونٹس کا تحفظ۔</li>
        <li>ذیلی عمل کی تشخیص کے ذریعے GUI پیشرفت بار۔</li>
        <li>تمام OCR پیرامیٹرز پر مکمل کنٹرول (Deskew، Clean، Oversample، اصلاح)۔</li>
        <li>متن کی تلاش براہ راست مرکزی ونڈو (PDF منظر) میں دستیاب ہے۔</li>
        </ul>
        <p>نقصانات:</p>
        <ul>
        <li>اضافی سسٹم ٹولز کی ضرورت ہے (ocrmypdf، Ghostscript، unpaper، pngquant – ایپ بنڈل میں شامل ہیں)۔</li>
        <li>پیچیدہ خرابی سے نمٹنے (ڈیڈ لاک، ٹائم آؤٹ)۔</li>
        </ul>

        <p><strong>Windows (مستحکم متبادل)</strong></p>
        <p>ٹول:</p>
        <ul>
        <li>pytesseract (Tesseract سے براہ راست رابطہ) + reportlab + PyPDF2</li>
        </ul>
        <p>نتیجہ:</p>
        <ul>
        <li>ایک قابل تلاش PDF جو بصری طور پر تصویری PDF سے مطابقت رکھتا ہے، لیکن شفاف متن کے ذریعے قابل تلاش ہے۔</li>
        </ul>
        <p>فوائد:</p>
        <ul>
        <li>فی الحال کوئی ذہن میں نہیں آ رہا۔</li>
        </ul>
        <p>نقصانات:</p>
        <ul>
        <li>PDF بنیادی طور پر پوشیدہ متن کے ساتھ ایک تصویر ہے؛ پیچیدہ دستاویزات (کالم، جدولیں) میں ترتیب قدرے ہٹ سکتی ہے۔</li>
        <li>کوئی خودکار جھکاؤ اصلاح (--deskew) یا تصویری صفائی (--clean) نہیں ہے۔</li>
        <li>GUI پیشرفت بار صرف پروسیس شدہ صفحات کی تعداد کی بنیاد پر تقریباً اپ ڈیٹ ہوتی ہے۔</li>
        <li>OCR کی رفتار قدرے سست ہے (کیونکہ ہر صفحہ الگ سے پروسیس ہوتا ہے)۔</li>
        <li>متن کی تلاش OCR متن کی ونڈو کی طرف ری ڈائریکٹ ہو جاتی ہے۔</li>
        </ul>

        <p><strong>عملی خصوصیات</strong></p>
        <ul>
        <li>دونوں طریقے ماخذ فائل کی طرح ایک ہی ڈائرکٹری میں قابل تلاش PDF تخلیق کرتے ہیں۔</li>
        <li>OCR ترتیبات (زبان، DPI، صفحہ تقسیم موڈ، OCR انجن موڈ) OCRSettingsDialog کے ذریعے ترتیب دی جا سکتی ہیں اور دونوں نفاذ میں موثر ہیں۔</li>
        </ul>

        <p><strong>تجویز:</strong></p>
        <ul>
        <li>macOS: ocrmypdf بائنری بہترین نتائج دیتی ہے – ایک Mac خریدیں اور ورژن استعمال کریں (Apple Silicon یا Intel چپ والے Mac کے لیے PDFDarkView)۔ OCR نتائج Windows سے بہتر ہیں!</li>
        <li>Windows: pytesseract حل استعمال کریں۔ یہ مستحکم ہے اور زیادہ تر دستاویزات کے لیے مکمل طور پر کافی معیار فراہم کرتا ہے۔</li>
        </ul>

        <p><strong>اہم نوٹ:</strong></p>
        <ul>
        <li>دونوں ورژن صارف انٹرفیس میں مکمل طور پر ضم ہیں – صارف کو کوئی فرق محسوس نہیں ہوتا۔</li>
        <li>پروگرام آپریٹنگ سسٹم کی بنیاد پر خود بخود فیصلہ کرتا ہے کہ کون سا OCR انجن استعمال کرنا ہے۔</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "دستخط تخلیق کریں (اسکین سے)",
        "signature_create_title": "اسکین شدہ دستخط منتخب کریں (PDF/تصویر)",
        "image_pdf_filter": "تصاویر اور PDF",
        "signature_pdf_empty": "PDF میں کوئی صفحہ نہیں ہے۔",
        "signature_created_success": "دستخط کامیابی سے تخلیق ہوا: {0}",
        "signature_create_error": "دستخط تخلیق کرتے وقت خرابی:\n{0}",
        "rembg_missing": "rembg انسٹال نہیں ہے۔\nبراہ کرم انسٹال کریں: pip install rembg\nخرابی: {0}",
        "signature_name_title": "دستخط کے لیے فائل کا نام",
        "signature_name_message": "براہ کرم نئے دستخط کے لیے فائل کا نام درج کریں (شفاف پس منظر کے ساتھ PNG کے طور پر محفوظ کیا جائے گا):",
        "signature_name_label": "فائل کا نام:",
        "signature_name_voice": "دستخط کے لیے فائل کا نام درج کریں",
        "signature_processing": "پروسیسنگ جاری ہے...",
        "signature_creation_title": "دستخط تخلیق کیا جا رہا ہے",
        "signature_overwrite_warning": "فائل '{0}' پہلے سے موجود ہے۔ اوور رائٹ کریں؟",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"دستخط کے لیے PDF تیار کریں",
        "signature_prepare_instruction":"براہ کرم ایک PDF منتخب کریں جس میں ایک صفحے پر اسکین شدہ دستخط ہو۔\n\nبہترین شناخت کے لیے یقینی بنائیں:\n• دستخط سفید کاغذ پر سیاہ سیاہی (بال پوائنٹ یا فائن لائنر) سے لکھا گیا ہو۔\n• دستخط دوسری صورت میں خالی A4 صفحہ کے اوپری تہائی حصے میں واقع ہو۔\n• PDF کم از کم 300 dpi پر اسکین کیا گیا ہو۔\n• دستخط واضح اور بہت پتلا نہ ہو۔\n• کوئی پریشان کن پس منظر کے نمونے یا لکیریں موجود نہ ہوں۔",
        "signature_prepare_voice":"براہ کرم اسکین شدہ دستخط کے ساتھ PDF منتخب کریں۔ اچھے معیار اور تضاد پر توجہ دیں۔",
        "sig_thickness_label":"لکیر کی موٹائی:",
        "sig_thickness_normal":"عام (پتلی)",
        "sig_thickness_bold":"موٹی (تجویز کردہ)",
        "sig_thickness_very_bold":"بہت موٹی",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI اور OCR زبانیں شامل کریں - رہنما",
        'language_guide_title': "GUI اور OCR زبانیں شامل کریں",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>مطلوبہ ترجمہ فائل <code>translations_xy.py</code> یہاں سے ڈاؤن لوڈ کریں<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        اور اسے درج ذیل ڈائرکٹری میں رکھیں:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>اپنا ویب براؤزر کھولیں۔</li>
        <li>یہاں جائیں: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>اسکرین کے دائیں کنارے پر "Releases" تلاش کریں اور <strong>"latest"</strong> کے نشان والے کو منتخب کریں۔</li>
        <li>اگلے ریلیز صفحہ پر، سب سے نیچے <code>Source Code.zip</code> فائل ڈاؤن لوڈ کریں۔</li>
        <li>ZIP فائل کو ان زپ کریں۔</li>
        <li>ان زپ شدہ فولڈر میں اپنی تمام ضروری زبانوں کی فائلیں تلاش کریں، اور انہیں ڈائرکٹری میں کاپی کریں:<br/>
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
        "menu_watermark":"واٹر مارک داخل کریں",
        "fullpage_text_watermark_title":"متن بطور واٹر مارک",
        "fullpage_image_watermark_title":"تصویر بطور واٹر مارک",
        "filename_with_watermark":"_واٹر_مارک_کے_ساتھ",
        "watermark_text":"متن:",
        "watermark_text_placeholder":"آپ کا واٹر مارک متن...",
        "watermark_font_family":"فونٹ:",
        "watermark_font_size":"فونٹ کا سائز:",
        "watermark_format":"فارمیٹنگ:",
        "watermark_bold":"موٹا",
        "watermark_italic":"ترچھا",
        "watermark_color":"رنگ:",
        "watermark_choose_color":"رنگ منتخب کریں...",
        "watermark_opacity":"دھندلاپن / شفافیت:",
        "watermark_direction":"پڑھنے کی سمت:",
        "watermark_direction_l_r":"بائیں → دائیں",
        "watermark_direction_bl_tr":"نیچے بائیں → اوپر دائیں",
        "watermark_direction_tl_br":"اوپر بائیں → نیچے",
        "watermark_direction_b_t":"نیچے → اوپر",
        "watermark_direction_t_b":"اوپر → نیچے",
        "watermark_preview":"پیش نظارہ:",
        "watermark_preview_sample":"نمونہ متن",
        "watermark_empty_text":"براہ کرم متن درج کریں۔",
        "watermark_applied":"واٹر مارک تمام صفحات پر لاگو کر دیا گیا ہے۔",
        "watermark_saved":"واٹر مارک محفوظ کر لیا گیا۔",
        "image_scale":"سائز:",
        "image_preview":"تصویر کا پیش نظارہ:",
        "no_image_selected":"کوئی تصویر منتخب نہیں کی گئی",
        "browse":"براؤز کریں...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact":"سیاہ کاریاں",
        "redact_add_black":"سیاہ کاری (کالا)",
        "redact_add_white":"سیاہ کاری (سفید / مٹائیں)",
        "redact_added_black":"کالی سیاہ کاری شامل کر دی گئی",
        "redact_added_white":"سفید سیاہ کاری شامل کر دی گئی",
        "redact_apply_all":"تمام سیاہ کاریاں لاگو کریں اور محفوظ کریں",
        "redact_discard_all":"تمام سیاہ کاریاں منسوخ کریں",
        "redact_discard":"اس سیاہ کاری کو منسوخ کریں",
        "no_redactions":"کوئی سیاہ کاری نہیں",
        "redact_confirm_title":"سیاہ کاریاں مستقل طور پر لاگو کریں",
        "redact_confirm_message":"انتباہ: نشان زدہ علاقے مستقل طور پر حذف کر دیے جائیں گے (کالا یا سفید)۔\nبیک اپ بنایا جائے گا (اگر فعال ہو)۔\n\nجاری رکھیں؟",
        "redact_apply":"ہاں، ابھی سیاہ کریں",
        "redact_saved":"{0} سیاہ کاری(اں) کامیابی سے لاگو اور محفوظ کر لی گئیں۔",
        "redact_saved_voice":"{0} سیاہ کاری(اں) لاگو کی گئیں",
        "redact_error":"سیاہ کاری کے دوران خرابی",
        "filename_redacted":"_سیاہ_کردہ",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'صفحہ نمبر داخل کریں',
        'page_numbers_format': 'نمبر کا فارمیٹ:',
        'page_numbers_format_arabic': '1, 2, 3 ... (عربی)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (رومن چھوٹے)',
        'page_numbers_format_roman_upper': 'I, II, III ... (رومن بڑے)',
        'page_numbers_format_letter': 'A, B, C ... (حروف)',
        'page_numbers_format_custom': 'اپنی مرضی',
        'page_numbers_custom_pattern': 'پیٹرن:',
        'page_numbers_custom_placeholder': 'مثال "صفحہ {nummer}" یا "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'موجودہ صفحہ نمبر کے لیے {nummer} اور کل تعداد کے لیے {total} استعمال کریں',
        'page_numbers_position': 'مقام:',
        'page_numbers_pos_tl': 'اوپر بائیں',
        'page_numbers_pos_tc': 'اوپر درمیان',
        'page_numbers_pos_tr': 'اوپر دائیں',
        'page_numbers_pos_ml': 'درمیان بائیں',
        'page_numbers_pos_mc': 'مرکز میں',
        'page_numbers_pos_mr': 'درمیان دائیں',
        'page_numbers_pos_bl': 'نیچے بائیں',
        'page_numbers_pos_bc': 'نیچے درمیان',
        'page_numbers_pos_br': 'نیچے دائیں',
        'page_numbers_margins': 'حاشیے:',
        'page_numbers_margin_x': 'افقی فاصلہ:',
        'page_numbers_margin_y': 'عمودی فاصلہ:',
        'page_numbers_range': 'صفحات کی حد:',
        'page_numbers_all_pages': 'تمام صفحات',
        'page_numbers_custom_range': 'اپنی مرضی کی حد',
        'page_numbers_from': 'سے:',
        'page_numbers_to': 'تک:',
        'page_numbers_progress': 'صفحہ نمبر داخل کیے جا رہے ہیں...',
        'page_numbers_start': 'صفحہ نمبر داخل کرنا شروع کیا جا رہا ہے...',
        'page_numbers_cancel': 'صفحہ نمبر داخل کرنا منسوخ کر دیا گیا',
        'page_numbers_success': 'صفحہ نمبر کامیابی سے شامل کر دیے گئے۔\n\nکیا آپ نیا PDF کھولنا چاہیں گے؟\n\n{0}',
        'page_numbers_complete': 'صفحہ نمبر شامل کر دیے گئے',
        'page_numbers_error_format': 'صفحہ نمبر داخل کرتے وقت خرابی: {0}',
        'page_numbers_content_type': 'مواد کی قسم:',
        'page_numbers_tab_simple': 'سادہ نمبر',
        'page_numbers_tab_range': 'صفحہ X میں سے Y',
        'page_numbers_tab_date': 'تاریخ',
        'page_numbers_tab_custom': 'آزاد متن',
        'page_numbers_range_format': 'فارمیٹ:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'صفحہ {aktuell} میں سے {gesamt}',
        'page_numbers_range_custom': 'اپنی مرضی',
        'page_numbers_range_placeholder': 'مثال "صفحہ {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'تاریخ کا فارمیٹ:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 جنوری 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'اپنی مرضی',
        'page_numbers_date_placeholder': 'مثال %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'مقام:',
        'page_numbers_date_before': 'صفحہ نمبر سے پہلے تاریخ',
        'page_numbers_date_after': 'صفحہ نمبر کے بعد تاریخ',
        'page_numbers_date_only': 'صرف تاریخ (صفحہ نمبر کے بغیر)',
        'page_numbers_custom_text': 'اپنی مرضی کا متن:',
        'page_numbers_custom_placeholder_text': 'صفحہ نمبر کے لیے {seite} اور کل کے لیے {gesamt} استعمال کریں\nمثال "خفیہ - صفحہ {seite}" یا "{seite} میں سے {gesamt}"',
        "filename_with_page_number":"_صفحہ_نمبر_کے_ساتھ",
        "filename_with_page_declaration":"_صفحہ_اعلان_کے_ساتھ",
        "filename_with_pagenumber":"_صفحہ_نمبر_کے_ساتھ",
        "filename_with_date":"_تاریخ_کے_ساتھ",
        "filename_with_my_page_declaration":"_اپنی_مرضی_کا_صفحہ_اعلان",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "غیر محفوظ تبدیلیاں",
        "unsaved_changes_message_darkmode": "غیر محفوظ داخلیں موجود ہیں۔\nکیا آپ تبدیل کرنے سے پہلے انہیں محفوظ کرنا چاہیں گے؟",
        "save_and_switch": "محفوظ کریں اور تبدیل کریں",
        "discard_and_switch": "ابھی تبدیل کریں",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'صفحات کو تصاویر کے طور پر برآمد کریں',
        'export_images_menu': 'تصاویر کے طور پر برآمد کریں (PNG/JPEG)',
        'export_images_format': 'تصویر کا فارمیٹ:',
        'export_images_dpi': 'ریزولوشن (DPI):',
        'export_images_quality': 'JPEG کوالٹی:',
        'export_images_range': 'صفحات کی حد:',
        'export_images_all_pages': 'تمام صفحات',
        'export_images_custom_range': 'اپنی مرضی کی حد',
        'export_images_from': 'سے:',
        'export_images_to': 'تک:',
        'export_images_options': 'اختیارات:',
        'export_images_single_files': 'ہر صفحہ علیحدہ فائل کے طور پر',
        'export_images_subfolder': 'ذیلی فولڈر میں برآمد کریں',
        'export_images_subfolder_info': '"PDFنام_تصاویر" ذیلی فولڈر میں',
        'export_images_same_folder': 'PDF والے فولڈر میں ہی',
        'export_images_apply_darkmode': 'PDFDarkView کی ترتیبات لاگو کریں (ڈارک موڈ)',
        'export_images_target_folder': 'ہدف فولڈر:',
        'export_images_browse': 'براؤز کریں...',
        'export_images_preview': 'پیش نظارہ:',
        'export_images_preview_info': 'برآمد کے لیے ترتیبات منتخب کریں',
        'export_images_preview_info_detail': '{0} صفحات بطور {1}\nریزولوشن: {2} DPI\nفائل کا نام: {3}\n{4}',
        'export_images_select_folder': 'ہدف فولڈر منتخب کریں',
        'export_images_start': 'تصاویر کی برآمد شروع کی جا رہی ہے...',
        'export_images_progress': 'تصاویر برآمد کی جا رہی ہیں...',
        'export_images_saving': 'صفحہ {0} میں سے {1} محفوظ کیا جا رہا ہے...',
        'export_images_success': 'برآمد کامیاب!\n\n{0} تصاویر یہاں محفوظ کی گئیں:\n{1}',
        'export_images_complete': 'تصاویر کی برآمد مکمل ہو گئی',
        'export_images_open_folder': '📁 فولڈر کھولیں',
        'export_images_cancel': 'تصاویر کی برآمد منسوخ کر دی گئی',
        'export_images_error_format': 'تصاویر برآمد کرتے وقت خرابی: {0}',
        'export_images_pdf2image_missing': 'لائبریری "pdf2image" انسٹال نہیں ہے۔\n\nبراہ کرم اس کے ساتھ انسٹال کریں:\npip install pdf2image\n\nWindows کے لیے آپ کو Poppler کی بھی ضرورت ہے:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'طویل مدتی آرکائیو کے لیے PDF/A تبدیلی',
        'pdfa_menu': 'PDF/A تبدیلی (آرکائیو کے لیے موزوں)',
        'pdfa_info': 'PDF کو PDF/A فارمیٹ میں تبدیل کرتا ہے۔\n\nPDF/A خاص طور پر طویل مدتی آرکائیو کے لیے ڈیزائن کیا گیا ہے اور اس بات کو یقینی بناتا ہے کہ دستاویز مستقبل میں صحیح طریقے سے ظاہر ہو۔',
        'pdfa_standard': 'PDF/A معیار:',
        'pdfa_standard_select': 'ورژن:',
        'pdfa_1': 'PDF/A-1 (سادہ، وسیع مطابقت)',
        'pdfa_2': 'PDF/A-2 (جدید، بہتر کمپریشن)',
        'pdfa_3': 'PDF/A-3 (تازہ ترین ورژن، منسلکات کی اجازت دیتا ہے)',
        'pdfa_standards_explanation': '📖 معیارات کی وضاحت:\n\n'
            '• PDF/A-1: بنیادی، پرانے سسٹمز کے ساتھ مطابقت رکھتا ہے (تقریباً 2005)\n'
            '• PDF/A-2: زیادہ جدید، بہتر کمپریشن، شفافیت کی حمایت (تقریباً 2011)\n'
            '• PDF/A-3: تازہ ترین ورژن، فائل منسلکات کو ایمبیڈ کرنے کی اجازت دیتا ہے (تقریباً 2013)\n\n'
            'تجویز: PDF/A-2 مطابقت اور جدید خصوصیات کے درمیان ایک اچھا سمجھوتہ ہے۔',
        'pdfa_options': 'اختیارات:',
        'pdfa_compress_enable': 'PDF کمپریس کریں (چھوٹی فائل)',
        'pdfa_metadata_preserve': 'میٹا ڈیٹا محفوظ رکھیں (عنوان، مصنف، وغیرہ)',
        'pdfa_target_folder': 'ہدف فولڈر:',
        'pdfa_browse': 'براؤز کریں...',
        'pdfa_select_folder': 'ہدف فولڈر منتخب کریں',
        'pdfa_ocr_info_unknown': '🔍 متن کے مواد کی جانچ نہیں کر سکا۔',
        'pdfa_ocr_info_not_needed': '✅ متن دستیاب ہے - OCR کی ضرورت نہیں۔\nPDF/A براہ راست بنایا جا سکتا ہے۔',
        'pdfa_ocr_info_recommended': '⚠️ کافی متن نہیں ملا۔\n\nقابل تلاش PDF کے لیے ہم پہلے OCR چلانے کی تجویز کرتے ہیں۔\nنوٹ: PDF/A OCR کے بغیر بھی کام کرتا ہے - لیکن متن قابل تلاش نہیں ہوگا۔',
        'pdfa_ocr_info_error': '❌ جانچ کے دوران خرابی: {0}',
        'pdfa_start': 'PDF/A تبدیلی شروع کی جا رہی ہے...',
        'pdfa_progress': 'PDF/A تبدیلی جاری ہے...',
        'pdfa_success': 'PDF/A تبدیلی کامیاب!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nکیا آپ نیا PDF کھولنا چاہیں گے؟',
        'pdfa_complete': 'PDF/A تبدیلی مکمل ہو گئی',
        'pdfa_cancel': 'PDF/A تبدیلی منسوخ کر دی گئی',
        'pdfa_error_format': 'PDF/A تبدیلی کے دوران خرابی:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'لائبریری "ocrmypdf" انسٹال نہیں ہے۔\n\nبراہ کرم اس کے ساتھ انسٹال کریں:\npip install ocrmypdf',
        'btn_convert': 'تبدیل کریں',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF کو بہتر بنائیں (فائل کا سائز کم کریں)',
        'optimize_menu': 'PDF کو بہتر بنائیں (فائل کا سائز)',
        'optimize_info': 'مختلف اصلاح کے طریقوں کے ذریعے PDF فائل کا سائز کم کرتا ہے۔\n\nکمپریشن کی سطح جتنی زیادہ ہوگی، فائل اتنی ہی چھوٹی ہوگی - تصاویر میں ممکنہ معیار کے نقصان کے ساتھ۔',
        'optimize_level': 'کمپریشن کی سطح:',
        'optimize_level_low': 'کم (تیز، کم بچت)',
        'optimize_level_medium': 'درمیانی (اچھا سمجھوتہ)',
        'optimize_level_high': 'زیادہ (بڑی بچت)',
        'optimize_level_maximum': 'زیادہ سے زیادہ (زیادہ سے زیادہ بچت، سست)',
        'optimize_level_explanation': 'تجویز: "درمیانی" رفتار اور فائل کے سائز کے درمیان ایک اچھا سمجھوتہ ہے۔',
        'optimize_options': 'اختیارات:',
        'optimize_compress_images': 'تصاویر کمپریس کریں (JPEG کوالٹی کم کریں)',
        'optimize_clean_objects': 'غیر استعمال شدہ اشیاء کو ہٹائیں',
        'optimize_preserve_metadata': 'میٹا ڈیٹا محفوظ رکھیں (عنوان، مصنف، وغیرہ)',
        'optimize_image_quality': 'تصویر کا معیار:',
        'optimize_range': 'صفحات کی حد:',
        'optimize_all_pages': 'تمام صفحات',
        'optimize_custom_range': 'اپنی مرضی کی حد',
        'optimize_from': 'سے:',
        'optimize_to': 'تک:',
        'optimize_target_folder': 'ہدف فولڈر:',
        'optimize_browse': 'براؤز کریں...',
        'optimize_select_folder': 'ہدف فولڈر منتخب کریں',
        'optimize_info_box': 'معلومات',
        'optimize_info_text': 'بڑی PDF کے لیے اصلاح میں کئی منٹ لگ سکتے ہیں۔\n\nتصاویر کم معیار کے ساتھ محفوظ کی جاتی ہیں، جو فائل کے سائز کو نمایاں طور پر کم کر سکتی ہیں۔',
        'optimize_start': 'PDF کی اصلاح شروع کی جا رہی ہے...',
        'optimize_progress': 'PDF کو بہتر بنایا جا رہا ہے...',
        'optimize_cancel': 'PDF کی اصلاح منسوخ کر دی گئی',
        'optimize_complete': 'PDF کی اصلاح مکمل ہو گئی',
        'optimize_error_format': 'PDF کی اصلاح کے دوران خرابی:\n\n{0}',
        'optimize_success_message': 'PDF کی اصلاح کامیاب!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nپہلے: {1}\nبعد: {2}\nبچت: {3:.1f}%\n\n{4}\n\nکیا آپ بہتر کردہ PDF کھولنا چاہیں گے؟',
        'optimize_success_message_no_size': 'PDF کی اصلاح کامیاب!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nسائز کی معلومات دستیاب نہیں۔\n\nکیا آپ بہتر کردہ PDF کھولنا چاہیں گے؟',
        'optimize_result_positive': 'فائل {0:.1f}% کم ہو گئی۔',
        'optimize_result_zero': 'فائل کے سائز میں کوئی تبدیلی نہیں۔',
        'optimize_result_negative': 'فائل {0:.1f}% بڑھ گئی۔\nاصلاح کو چھوڑ دیا گیا، اصل فائل کو محفوظ رکھا گیا۔',
        'btn_optimize': 'اصلاح شروع کریں',
        'filename_optimize_low_suffix': '_بہتر_کردہ_کم',
        'filename_optimize_medium_suffix': '_بہتر_کردہ',
        'filename_optimize_high_suffix': '_بہتر_کردہ_زیادہ',
        'filename_optimize_maximum_suffix': '_بہتر_کردہ_زیادہ_سے_زیادہ',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF کو کراپ کریں',
        'crop_menu': 'PDF کو کراپ کریں (Crop)',
        'crop_range': 'اس پر لاگو کریں:',
        'crop_all_pages': 'تمام صفحات',
        'crop_current_page': 'صرف موجودہ صفحہ',
        'crop_values': 'کراپ کی اقدار (پوائنٹس میں):',
        'crop_left': 'بائیں:',
        'crop_right': 'دائیں:',
        'crop_top': 'اوپر:',
        'crop_bottom': 'نیچے:',
        'crop_presets': 'پہلے سے طے شدہ:',
        'crop_preset_white': 'سفید حاشیے تلاش کریں',
        'crop_reset': 'ری سیٹ کریں',
        'crop_mouse_hint': '🖱️ علاقے کو تقریباً منتخب کرنے کے لیے ایک مستطیل گھسیٹیں۔\nپھر آپ SpinBoxes میں اقدار کو درست طریقے سے ایڈجسٹ کر سکتے ہیں۔\nماؤس کے ساتھ دستی ایڈجسٹمنٹ ممکن نہیں۔',
        'crop_apply': 'کراپ کریں',
        'crop_scope_all': 'تمام صفحات',
        'crop_scope_current': 'موجودہ صفحہ',
        'crop_new_size': 'نیا سائز: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'کوئی PDF لوڈ نہیں',
        'crop_preview_error': 'پیش نظارہ لوڈ کرتے وقت خرابی',
        'crop_start': 'کراپ کرنا شروع کیا جا رہا ہے...',
        'crop_progress': 'PDF کو کراپ کیا جا رہا ہے...',
        'crop_success': 'PDF کامیابی سے کراپ ہو گیا!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nکیا آپ کراپ شدہ PDF کھولنا چاہیں گے؟',
        'crop_complete': 'کراپ کرنا مکمل ہو گیا',
        'crop_cancel': 'کراپ کرنا منسوخ کر دیا گیا',
        'crop_error_format': 'کراپ کرتے وقت خرابی:\n\n{0}',
        'filename_crop_suffix': '_کراپ_شدہ',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF کو ہموار کریں (Flatten)',
        'flatten_menu': 'PDF کو ہموار کریں (Flatten)',
        'flatten_info': 'PDF کو ہموار کرنا تمام قابل ترمیم عناصر کو صفحہ کے مواد میں "جلا" دیتا ہے۔\n\nاس کے بعد، فارم فیلڈز، تشریحات، متون، صلیب، دستخط، تصاویر اور شکلیں انفرادی طور پر قابل ترمیم نہیں رہتیں۔',
        'flatten_explanation_title': '📖 یہ کس لیے اچھا ہے؟',
        'flatten_explanation_text': 'ہموار کرنا درج ذیل صورتوں میں ضروری ہے:\n\n'
            '• 📄 آپ دستاویز کو پرنٹنگ کے لیے تیار کرنا چاہتے ہیں\n'
            '• 🔒 آپ کسی کو فارم فیلڈز تبدیل کرنے سے روکنا چاہتے ہیں\n'
            '• 📎 آپ تشریحات اور تبصروں کو دستاویز میں "مستقل" ایمبیڈ کرنا چاہتے ہیں\n'
            '• 🖼️ آپ درج کردہ متون، صلیب، دستخط، تصاویر اور شکلوں کو دستاویز میں مستقل طور پر لنگر انداز کرنا چاہتے ہیں\n'
            '• 📦 آپ فائل کو آرکائیو کے لیے تیار کرنا چاہتے ہیں\n\n'
            'ہموار کرنا PDF کو چھوٹا بناتا ہے اور عناصر کو حادثاتی طور پر منتقل ہونے یا حذف ہونے سے روکتا ہے۔',
        'flatten_what_title': 'کیا ہموار کیا جاتا ہے؟',
        'flatten_what_list': '• ✅ فارم فیلڈز (ٹیکسٹ فیلڈز، چیک باکسز، بٹن)\n'
            '• ✅ تشریحات (تبصرے، نمایاں کردہ، نوٹس)\n'
            '• ✅ اوورلے (متون، صلیب، دستخط، تصاویر، شکلیں)',
        'flatten_options': 'اختیارات:',
        'flatten_forms': 'فارم فیلڈز کو ہموار کریں',
        'flatten_annotations': 'تشریحات کو ہموار کریں',
        'flatten_overlays': 'اوورلے کو ہموار کریں (متون، صلیب، دستخط، تصاویر، شکلیں)',
        'flatten_target_folder': 'ہدف فولڈر:',
        'flatten_browse': 'براؤز کریں...',
        'flatten_select_folder': 'ہدف فولڈر منتخب کریں',
        'flatten_warning': '⚠️ اہم: ہموار کرنا ایک ناقابل واپسی عمل ہے!\n\nہموار کرنے کے بعد، قابل ترمیم عناصر کو انفرادی طور پر تبدیل یا حذف نہیں کیا جا سکتا۔\nاگر ضرورت ہو تو پہلے بیک اپ بنائیں۔',
        'flatten_apply': 'ہموار کریں',
        'flatten_start': 'ہموار کرنا شروع کیا جا رہا ہے...',
        'flatten_progress': 'PDF کو ہموار کیا جا رہا ہے...',
        'flatten_success': 'PDF کامیابی سے ہموار ہو گیا!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nکیا آپ ہموار شدہ PDF کھولنا چاہیں گے؟',
        'flatten_complete': 'ہموار کرنا مکمل ہو گیا',
        'flatten_cancel': 'ہموار کرنا منسوخ کر دیا گیا',
        'flatten_error_format': 'ہموار کرتے وقت خرابی:\n\n{0}',
        'filename_flatten_suffix': '_ہموار_شدہ',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF اوورلے (Overlay)',
        'overlay_menu': 'PDF اوورلے (Overlay)',
        'overlay_info': 'ایک PDF (اوورلے) کو دوسرے PDF کے اوپر رکھتا ہے۔\n\nاوورلے PDF کو بیس PDF کے اوپر رکھا جاتا ہے۔ یہ واٹر مارکس، لوگو، لیٹر ہیڈ یا مہروں کے لیے مفید ہے۔',
        'overlay_explanation_title': '📖 یہ کس لیے اچھا ہے؟',
        'overlay_explanation_text': 'اوورلے درج ذیل صورتوں میں ضروری ہے:\n\n'
            '• 🏢 کمپنی کے لوگو کو واٹر مارک کے طور پر ہر صفحے پر رکھیں\n'
            '• 📄 خالی PDF پر لیٹر ہیڈ رکھیں\n'
            '• 🖊️ دستاویز پر مہر کا اوورلے رکھیں\n'
            '• 🔖 تمام صفحات پر واٹر مارک رکھیں\n'
            '• 📑 ٹیمپلیٹ پر فارم کا اوورلے رکھیں',
        'overlay_type': 'اوورلے کی قسم:',
        'overlay_type_fullpage': 'پورا صفحہ (ڈھانپنے والا)',
        'overlay_type_transparent': 'پورا صفحہ (شفاف - تجویز کردہ)',
        'overlay_type_stamp': 'مہر (قابل پوزیشننگ)',
        'overlay_type_info_fullpage': '📄 اوورلے PDF پورے صفحے کے اوپر بالکل رکھا جاتا ہے۔\nسفید پس منظر کو ہٹایا جا سکتا ہے تاکہ صرف مواد نظر آئے۔',
        'overlay_type_info_transparent': '🔍 اوورلے PDF شفاف پس منظر کے ساتھ پورے صفحے کے اوپر رکھا جاتا ہے۔\nسفید پس منظر خود بخود ہٹا دیا جاتا ہے - واٹر مارکس اور لوگو کے لیے بہترین!',
        'overlay_type_info_stamp': '🖊️ اوورلے PDF کو مہر کے طور پر پوزیشن اور اسکیل کیا جاتا ہے۔\nمخصوص مقامات پر لوگو، مہروں یا دستخطوں کے لیے بہترین۔',
        'overlay_remove_background': 'سفید پس منظر ہٹائیں:',
        'overlay_remove_background_enable': 'اوورلے PDF سے سفید پس منظر ہٹائیں (اوورلے کو شفاف بناتا ہے)',
        'overlay_remove_background_tooltip': 'اوورلے PDF سے سفید علاقوں کو ہٹاتا ہے تاکہ نیچے کا متن نظر آئے۔',
        'overlay_threshold': 'حد کی قدر:',
        'overlay_threshold_hint': '(1-254، زیادہ = زیادہ سفید ہٹایا جاتا ہے)',
        'overlay_select_file': 'اوورلے PDF منتخب کریں:',
        'overlay_file_placeholder': 'براہ کرم اوورلے کے لیے PDF فائل منتخب کریں',
        'overlay_browse': 'براؤز کریں...',
        'overlay_select_overlay': 'اوورلے PDF منتخب کریں',
        'overlay_range': 'صفحات کی حد:',
        'overlay_all_pages': 'تمام صفحات',
        'overlay_custom_range': 'اپنی مرضی کی حد',
        'overlay_from': 'سے:',
        'overlay_to': 'تک:',
        'overlay_position': 'مقام:',
        'overlay_position_center': 'مرکز',
        'overlay_position_top_left': 'اوپر بائیں',
        'overlay_position_top_right': 'اوپر دائیں',
        'overlay_position_bottom_left': 'نیچے بائیں',
        'overlay_position_bottom_right': 'نیچے دائیں',
        'overlay_size': 'سائز:',
        'overlay_size_original': 'اصل سائز',
        'overlay_size_fit_page': 'صفحے کے مطابق بنائیں',
        'overlay_size_custom': 'اپنی مرضی (%)',
        'overlay_opacity': 'شفافیت:',
        'overlay_target_folder': 'ہدف فولڈر:',
        'overlay_browse_folder': 'براؤز کریں...',
        'overlay_select_folder': 'ہدف فولڈر منتخب کریں',
        'overlay_warning': '⚠️ نوٹ: اوورلے PDF کو بیس PDF کے اوپر رکھا جاتا ہے اور اس میں "جلا" دیا جاتا ہے۔\n\nمحفوظ کرنے کے بعد اوورلے PDF کے عناصر کو انفرادی طور پر ترمیم نہیں کیا جا سکتا۔',
        'overlay_apply': 'اوورلے',
        'overlay_start': 'اوورلے شروع کیا جا رہا ہے...',
        'overlay_progress': 'PDF کو اوورلے کیا جا رہا ہے...',
        'overlay_success': 'PDF کامیابی سے اوورلے ہو گیا!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nکیا آپ اوورلے شدہ PDF کھولنا چاہیں گے؟',
        'overlay_complete': 'اوورلے مکمل ہو گیا',
        'overlay_cancel': 'اوورلے منسوخ کر دیا گیا',
        'overlay_error_format': 'اوورلے کرتے وقت خرابی:\n\n{0}',
        'overlay_no_file': 'کوئی اوورلے PDF منتخب نہیں کیا گیا۔\n\nبراہ کرم اوورلے کرنے کے لیے PDF فائل منتخب کریں۔',
        'filename_overlay_suffix': '_اوورلے_شدہ',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'PDF سے تصاویر نکالیں',
        'extract_images_menu': 'تمام تصاویر نکالیں',
        'extract_images_info': 'PDF سے تمام تصاویر نکالتا ہے اور انہیں علیحدہ فائلوں کے طور پر محفوظ کرتا ہے۔\n\nتصاویر ان کی اصل شکل میں محفوظ کی جاتی ہیں یا منتخب شدہ شکل میں تبدیل کی جاتی ہیں۔',
        'extract_images_format': 'تصویر کا فارمیٹ:',
        'extract_images_quality': 'JPEG کوالٹی:',
        'extract_images_options': 'اختیارات:',
        'extract_images_subfolder': 'ذیلی فولڈر میں نکالیں ("PDFنام_تصاویر")',
        'extract_images_unique': 'صرف منفرد تصاویر (نقل سے بچیں)',
        'extract_images_range': 'صفحات کی حد:',
        'extract_images_all_pages': 'تمام صفحات',
        'extract_images_custom_range': 'اپنی مرضی کی حد',
        'extract_images_from': 'سے:',
        'extract_images_to': 'تک:',
        'extract_images_target_folder': 'ہدف فولڈر:',
        'extract_images_browse': 'براؤز کریں...',
        'extract_images_select_folder': 'ہدف فولڈر منتخب کریں',
        'extract_images_info_box': 'معلومات',
        'extract_images_info_text': 'نکالنے میں بڑی PDF کے لیے کئی منٹ لگ سکتے ہیں۔\n\nتصاویر ان کے اصل نام کے ساتھ محفوظ کی جاتی ہیں (صفحہ_تصویر)۔',
        'extract_images_extract': 'نکالیں',
        'extract_images_start': 'نکالنا شروع کیا جا رہا ہے...',
        'extract_images_progress': 'تصاویر نکالی جا رہی ہیں...',
        'extract_images_success': '✅ تصاویر کامیابی سے نکال لی گئیں!\n\n{0} تصاویر یہاں محفوظ کی گئیں:\n{1}',
        'extract_images_complete': 'تصاویر کا نکالنا مکمل ہو گیا',
        'extract_images_cancel': 'نکالنا منسوخ کر دیا گیا',
        'extract_images_error_format': 'تصاویر نکالتے وقت خرابی:\n\n{0}',
        'extract_images_open_folder': '📁 فولڈر کھولیں',
        'extract_images_no_images': 'PDF میں کوئی تصویر نہیں ملی۔',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'ایک صفحے پر متعدد صفحات (N-Up)',
        'nup_menu': 'ایک صفحے پر متعدد صفحات (N-Up)',
        'nup_info': 'متعدد PDF صفحات کو ایک صفحے پر ترتیب دیتا ہے۔\n\nکومپیکٹ پرنٹس، جائزوں یا ہینڈ آؤٹ کے لیے بہترین۔',
        'nup_layout': 'ترتیب:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'پیش نظارہ:',
        'nup_preview_info': '{0} صفحات → فی شیٹ {1} صفحات → {2} شیٹس\nترتیب: {3}',
        'nup_order': 'ترتیب:',
        'nup_order_horizontal': 'افقی (قطار بہ قطار)',
        'nup_order_vertical': 'عمودی (کالم بہ کالم)',
        'nup_order_horizontal_reverse': 'افقی معکوس',
        'nup_order_vertical_reverse': 'عمودی معکوس',
        'nup_range': 'صفحات کی حد:',
        'nup_all_pages': 'تمام صفحات',
        'nup_custom_range': 'اپنی مرضی کی حد',
        'nup_from': 'سے:',
        'nup_to': 'تک:',
        'nup_options': 'اختیارات:',
        'nup_margins': 'حاشیے:',
        'nup_margin_between': 'صفحات کے درمیان فاصلہ:',
        'nup_page_numbers': 'صفحہ نمبر داخل کریں',
        'nup_target_folder': 'ہدف فولڈر:',
        'nup_browse': 'براؤز کریں...',
        'nup_select_folder': 'ہدف فولڈر منتخب کریں',
        'nup_create': 'بنائیں',
        'nup_start': 'N-Up شروع کیا جا رہا ہے...',
        'nup_progress': 'N-Up بنایا جا رہا ہے...',
        'nup_success': 'N-Up کامیابی سے بن گیا!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nکیا آپ نیا PDF کھولنا چاہیں گے؟',
        'nup_complete': 'N-Up مکمل ہو گیا',
        'nup_cancel': 'N-Up منسوخ کر دیا گیا',
        'nup_error_format': 'N-Up کے دوران خرابی:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'صفحہ کا سائز تبدیل کریں',
        'pagesize_menu': 'صفحہ کا سائز تبدیل کریں',
        'pagesize_info': 'PDF کے صفحہ کا سائز تبدیل کرتا ہے۔\n\nمواد خود بخود نئے سائز کے مطابق ڈھل جاتا ہے۔',
        'pagesize_format': 'فارمیٹ:',
        'pagesize_select': 'ایک معیاری فارمیٹ منتخب کریں:',
        'pagesize_custom': 'اپنی مرضی کا سائز:',
        'pagesize_width': 'چوڑائی:',
        'pagesize_height': 'اونچائی:',
        'pagesize_orientation': 'سمت:',
        'pagesize_portrait': 'عمودی',
        'pagesize_landscape': 'افقی',
        'pagesize_scale_options': 'اسکیلنگ کے اختیارات:',
        'pagesize_fit': 'مطابق بنائیں (پہلو کا تناسب برقرار رکھیں)',
        'pagesize_stretch': 'پھیلائیں (بگاڑیں)',
        'pagesize_center': 'مرکز میں (اصل سائز)',
        'pagesize_range': 'صفحات کی حد:',
        'pagesize_all_pages': 'تمام صفحات',
        'pagesize_custom_range': 'اپنی مرضی کی حد',
        'pagesize_from': 'سے:',
        'pagesize_to': 'تک:',
        'pagesize_target_folder': 'ہدف فولڈر:',
        'pagesize_browse': 'براؤز کریں...',
        'pagesize_select_folder': 'ہدف فولڈر منتخب کریں',
        'pagesize_apply': 'لاگو کریں',
        'pagesize_start': 'صفحہ کا سائز تبدیل کرنا شروع کیا جا رہا ہے...',
        'pagesize_progress': 'صفحہ کا سائز تبدیل کیا جا رہا ہے...',
        'pagesize_success': 'صفحہ کا سائز کامیابی سے تبدیل ہو گیا!\n\nاس طرح محفوظ کیا گیا:\n{0}\n\nکیا آپ نیا PDF کھولنا چاہیں گے؟',
        'pagesize_complete': 'صفحہ کا سائز تبدیل کرنا مکمل ہو گیا',
        'pagesize_cancel': 'صفحہ کا سائز تبدیل کرنا منسوخ کر دیا گیا',
        'pagesize_error_format': 'صفحہ کا سائز تبدیل کرتے وقت خرابی:\n\n{0}',
        'pagesize_preview_info': 'نیا سائز: {0} x {1} pt',
        'filename_pagesize_suffix': '_نیا_سائز',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF کی معلومات',
        'pdf_info_menu': 'PDF کی معلومات دکھائیں',
        'pdf_info_voice': 'PDF کی معلومات دکھائی جا رہی ہیں',
        'pdf_info_error': 'PDF کی معلومات دکھاتے وقت خرابی:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "کی بورڈ شارٹ کٹ دکھائیں",
        "shortcuts_dialog_title": "کی بورڈ شارٹ کٹس",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 فائل</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF کھولیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF بند کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>اس طرح محفوظ کریں...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>دستاویز کی حفاظت کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>پرنٹ کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>فوری پرنٹ کریں (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>ایپلیکیشن بند کریں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 برآمد</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Pages کے طور پر برآمد کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>DOCX کے طور پر برآمد کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>TXT کے طور پر برآمد کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>تصاویر کے طور پر برآمد کریں (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>تصاویر نکالیں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ دستاویز کی پروسیسنگ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (متعدد صفحات)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A تبدیلی (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF کو ہموار کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF اوورلے</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF کو بہتر بنائیں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ ترمیم</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>تلاش کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>بک مارک شامل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>بک مارکس کا انتظام کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>اگلا بک مارک</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>پچھلا بک مارک</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR چلائیں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 صفحہ کا انتظام</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>موجودہ صفحہ گھمائیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>تمام صفحات گھمائیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>موجودہ صفحہ معمول پر لائیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>تمام صفحات معمول پر لائیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>صفحات حذف کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>صفحات نکالیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>صفحات داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>صفحات منتقل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDFs کو ضم کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>صفحہ کا سائز تبدیل کریں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 داخل کریں</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>متن داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>صلیب داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>دستخط 1 داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>دستخط 2 داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>تصویر داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>مستطیل داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>بیضوی داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>لکیر داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>تیر داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>صفحہ نمبر داخل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ٹیکسٹ واٹر مارک</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>تصویری واٹر مارک</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ سیاہ کاریاں</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>سیاہ کاری (کالا)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>سیاہ کاری (سفید)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>تمام سیاہ کاریاں لاگو کریں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ جدید</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF کو کراپ کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>میٹا ڈیٹا ترمیم کریں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ منظر</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ڈارک/لائٹ موڈ تبدیل کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>ٹیکسٹ ونڈو دکھائیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>صفحہ کی چوڑائی (زوم)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>دو صفحات (زوم)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>جائزہ (زوم)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ترتیبات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>پاس ورڈ کا انتظام</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR ترتیبات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>دستخط کی ترتیبات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>فائل نام کی فارمیٹنگ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>ترتیبات برآمد کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>ترتیبات درآمد کریں</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ معلومات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF کی معلومات دکھائیں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>آواز کی آؤٹ پٹ آن/آف کریں</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>مینو بار پر توجہ مرکوز کریں</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "نیا ورژن دستیاب ہے",
        "update_available_message": "ایک نیا ورژن <b>{0}</b> دستیاب ہے۔\n\nاپ ڈیٹ ڈاؤن لوڈ کرنے کے لیے ریلیز پیج ملاحظہ کریں:\n{1}",
        "update_available_voice": "نیا ورژن {0} دستیاب ہے۔ براہ کرم GitHub پیج سے اپ ڈیٹ ڈاؤن لوڈ کریں۔",
        "update_open_release": "ریلیز پیج کھولیں",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "تمام ترجمے ڈاؤن لوڈ کریں",
        "ask_download_all_translations": """جرمن، انگریزی اور ویتنامی کے علاوہ، {total_languages} مزید GUI زبانیں دستیاب ہیں۔\n\nکیا انہیں فراہم / اپ ڈیٹ کیا جائے؟\n\nنوٹ:\nغیر ضروری زبانوں کو آپ بعد میں ڈائریکٹری سے دستی طور پر حذف کر سکتے ہیں:\n{translations_path}
        \nاگر آپ منسوخ کرتے ہیں، تو آپ GUI زبانیں بعد میں 'ٹولز → ترجمے اپ ڈیٹ کریں' مینو کے ذریعے ڈاؤن لوڈ کر سکتے ہیں۔""",
        "menu_update_translations": "ترجمے اپ ڈیٹ کریں",
        "translations_updated": "ترجمے اپ ڈیٹ کر دیے گئے",
        "translations_update_success": "{} ترجمے کامیابی سے اپ ڈیٹ کیے گئے ({} نئے، {} اپ ڈیٹ کیے گئے)۔",
        "translations_update_error": "ترجمے اپ ڈیٹ کرنے میں خرابی",
        "translations_update_no_changes": "تمام ترجمے پہلے سے ہی اپ ٹو ڈیٹ ہیں۔",
        "translations_update_offline": "کوئی انٹرنیٹ کنکشن نہیں۔ ترجمے اپ ڈیٹ نہیں کیے جا سکے۔",
        "translations_update_in_progress": "ترجمے بیک گراؤنڈ میں اپ ڈیٹ کیے جا رہے ہیں...",
        "translations_downloading": "ترجمے ڈاؤن لوڈ ہو رہے ہیں...",
        "translations_path_hint": "ترجموں کے لیے صارف ڈائریکٹری",
        "translations_update_not_available_title": "اپ ڈیٹ دستیاب نہیں",
        "translations_update_not_available_message": """ترجمے اپ ڈیٹ کرنا صرف انسٹال شدہ ورژن میں دستیاب ہے۔\n\nڈیولپمنٹ موڈ میں، ترجمے پہلے سے ہی اپ ٹو ڈیٹ ہیں۔""",
        "translations_update_no_internet_title": "کوئی انٹرنیٹ کنکشن نہیں",
        "translations_update_no_internet_message": """انٹرنیٹ کنکشن قائم نہیں کیا جا سکا۔\n\nGitHub سے ترجمے ڈاؤن لوڈ نہیں کیے جا سکتے۔\n\nممکنہ حل:
        • اپنے انٹرنیٹ کنکشن کی جانچ کریں
        • کسی بھی فائر وال کو عارضی طور پر غیر فعال کریں
        • بعد میں دوبارہ کوشش کریں
        \nآپ GitHub سے دستی طور پر بھی ترجمے ڈاؤن لوڈ کر سکتے ہیں:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "اپ ڈیٹ پہلے سے جاری ہے",
        "btn_retry": "دوبارہ کوشش کریں",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "PDF Dark View میں خوش آمدید",
        "welcome_title_not_supported": "PDF Dark View میں خوش آمدید",
        "welcome_message": "PDF Dark View میں خوش آمدید!\n\nآپ کی سسٹم زبان '{language}' کے طور پر شناخت کی گئی۔\nکیا آپ اس زبان کو صارف انٹرفیس کے لیے استعمال کرنا چاہتے ہیں؟\n\nآپ 'سیٹنگز → زبان' کے ذریعے کسی بھی وقت زبان تبدیل کر سکتے ہیں۔",
        "welcome_message_language_not_available": "PDF Dark View میں خوش آمدید!\n\nآپ کی سسٹم زبان '{language}' کے طور پر شناخت کی گئی۔\nیہ زبان ابھی تک انسٹال نہیں ہے۔\n\nکیا آپ اب GitHub سے {language} کے لیے ترجمے ڈاؤن لوڈ کرنا چاہتے ہیں؟\n\n(زبان پھر خود بخود صارف انٹرفیس کے لیے استعمال ہوگی۔)",
        "welcome_message_language_not_supported": "PDF Dark View میں خوش آمدید!\n\nآپ کی سسٹم زبان '{language}' کے طور پر شناخت کی گئی۔\nبدقسمتی سے، اس زبان کے لیے ابھی تک کوئی ترجمے نہیں ہیں۔\n\nصارف انٹرفیس {fallback_language} میں دکھایا جائے گا۔\n\nآپ 'سیٹنگز → زبان' کے ذریعے کسی بھی وقت زبان تبدیل کر سکتے ہیں۔\nاگر آپ چاہیں تو، آپ خود بھی اپنی زبان کے لیے ترجمہ میں حصہ ڈال سکتے ہیں:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "ہاں، سسٹم زبان استعمال کریں",
        "welcome_keep_english": "نہیں، انگریزی رکھیں",
        "welcome_download_language": "ہاں، {language} ڈاؤن لوڈ کریں",

        # ============================================
        # 107. حالیہ استعمال شدہ راستے
        # ============================================

        'menu_recent': 'حالیہ استعمال شدہ',
        'menu_recent_dirs': 'ڈائریکٹریز...',
        'menu_recent_files': 'فائلیں...',
        'recent_manage': 'منظم کریں...',
        'recent_enable_tracking': 'حالیہ راستے محفوظ کریں (پرائیویسی)',
        'recent_enable_info': 'راستے محفوظ نہ کرنے کے لیے اس آپشن کو غیر فعال کریں',
        'recent_tracking_disabled': 'راستے کی ٹریکنگ غیر فعال ہے',
        'recent_enabled': 'فعال',
        'recent_disabled': 'غیر فعال',
        'recent_tracking_status': 'راستے کی ٹریکنگ {0}',
        'recent_dialog_title': 'حالیہ استعمال شدہ راستے',
        'recent_tab_directories': 'ڈائریکٹریز',
        'recent_tab_files': 'فائلیں',
        'recent_dirs_instruction': 'ڈائریکٹری میں فائل ڈائیلاگ کھولنے کے لیے ڈبل کلک کریں',
        'recent_files_instruction': 'PDF براہ راست کھولنے کے لیے ڈبل کلک کریں',
        'recent_no_directories': '(کوئی محفوظ شدہ ڈائریکٹری نہیں)',
        'recent_no_files': '(کوئی محفوظ شدہ فائل نہیں)',
        'recent_default_current': '⭐ طے شدہ: {0}',
        'recent_set_as_default': '⭐ طے شدہ کے طور پر سیٹ کریں',
        'recent_default_set_title': 'طے شدہ ڈائریکٹری سیٹ کر دی گئی',
        'recent_default_set_message': '"{0}" ڈائریکٹری PDF کھولنے کے لیے طے شدہ کے طور پر سیٹ کر دی گئی ہے۔',
        'recent_default_set_voice': 'طے شدہ ڈائریکٹری سیٹ کر دی گئی',
        'recent_directory_not_found': 'ڈائریکٹری نہیں ملی',
        'recent_file_not_found': 'فائل نہیں ملی',
        'recent_remove_selected': 'ہٹائیں',
        'recent_remove_title': 'راستہ ہٹائیں',
        'recent_remove_confirm': 'کیا آپ واقعی "{0}" راستے کو فہرست سے ہٹانا چاہتے ہیں؟',
        'recent_path_removed': 'راستہ ہٹا دیا گیا',
        'recent_clear_all': 'سب ہٹائیں',
        'recent_clear_title': 'تمام راستے ہٹائیں',
        'recent_clear_confirm_type': 'کیا آپ واقعی تمام {0} حذف کرنا چاہتے ہیں؟',
        'recent_cleared': 'فہرست صاف کر دی گئی',
        'recent_path_not_found_title': 'راستہ نہیں ملا',
        'recent_path_not_found_message': '"{0}" راستہ اب موجود نہیں ہے۔',
        'recent_open_file': 'فائل کھولیں',
        'btn_open_recent': 'کھولیں',
        'recent_open_file_question': 'کیا آپ "{0}" کو PDF کے طور پر کھولنا چاہتے ہیں؟',
        'recent_not_pdf': 'منتخب کردہ فائل PDF نہیں ہے۔',
        'recent_more_entries': 'مزید اندراجات...',
        'btn_remove': 'ہٹائیں',
        'btn_clear': 'سب صاف کریں',
        'recent_context_open': 'کھولیں',
        'recent_context_reveal': 'Finder میں دکھائیں',
        'recent_context_set_default': '⭐ طے شدہ کے طور پر سیٹ کریں',
        'recent_context_open_terminal': '💻 ٹرمینل کھولیں',
        'recent_context_file_info': 'فائل کی معلومات',
        'recent_context_open_with_default': '📄 طے شدہ ایپ کے ساتھ کھولیں',
        'recent_context_remove': 'فہرست سے ہٹائیں',
        'recent_context_clear_all': 'سب ہٹائیں',
        'recent_file_info_title': 'فائل کی معلومات',
        'recent_file_info_name': 'نام',
        'recent_file_info_path': 'راستہ',
        'recent_file_info_size': 'سائز',
        'recent_file_info_modified': 'ترمیم شدہ',
        'recent_file_info_pages': 'صفحات',
        'recent_error_reveal': 'Finder میں کھولنے میں خرابی',
        'recent_error_terminal': 'ٹرمینل کھولنے میں خرابی',
        'recent_error_info': 'فائل کی معلومات حاصل کرنے میں خرابی',
        'open_user_data_folder': 'صارف کا ڈیٹا ڈائریکٹری دکھائیں',

        # ============================================
        # 108. جفت/طاق صفحات حذف کریں
        # ============================================
        "pages_delete_even": "تمام جفت صفحات حذف کریں",
        "pages_delete_odd":  "تمام طاق صفحات حذف کریں",
        "progress_even_pages": "جفت صفحات حذف کیے جا رہے ہیں",
        "progress_odd_pages": "طاق صفحات حذف کیے جا رہے ہیں",
        "progress_mark_delete_even": "{} جفت صفحہ(جات) حذف کرنے کے لیے نشان زد کیے گئے",
        "progress_mark_delete_odd":  "{} طاق صفحہ(جات) حذف کرنے کے لیے نشان زد کیے گئے",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "پروگرام بند ہو رہا ہے",

    }

