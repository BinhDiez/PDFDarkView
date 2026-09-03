
# ============================================
# translations_fa.py - Wörterbuch Persisch (Farsi)
# Vollständig sortiert nach Kategorien
# ============================================

def load_persian_strings():
    """Lädt alle persischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View توسط BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "بارگذاری PDF",
        'btn_text_window': "متن OCR",
        'btn_first': "صفحه اول",
        'btn_prev': "صفحه قبل",
        'btn_next': "صفحه بعد",
        'btn_last': "صفحه آخر",
        'btn_print': "چاپ",
        'btn_darkmode_light': "حالت روشن",
        'btn_darkmode_dark': "حالت تاریک",
        'btn_delete_pages': "حذف صفحات",
        'btn_extract_pages': "استخراج صفحات",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "تأیید",
        'btn_cancel': "لغو",
        'btn_save': "ذخیره",
        'btn_close': "بستن",
        'btn_delete': "حذف",
        'btn_delete_all': "حذف همه",
        'btn_copy': "کپی",
        'btn_export': "خروجی",
        'btn_show': "نمایش رمز عبور",
        'btn_hide': "مخفی کردن رمز عبور",
        'btn_authenticate': "احراز هویت",
        'btn_settings': "تنظیمات",
        'btn_protect': "محافظت",
        'btn_remove_password': "حذف رمز عبور",
        'btn_manage': "مدیریت رمز عبور",
        'btn_retry': "تلاش مجدد",
        'btn_select_all': "انتخاب همه",
        'btn_clear_selection': "لغو انتخاب",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "صفحه {0} از {1}",
        'page_count': "از {0}",
        'goto_page': "برو به صفحه",
        'page_simple': "صفحه {0}",
        'full_view_page': "نمایش کامل صفحه {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "عبارت جستجو را وارد کنید + Enter",
        'search_results': "نتایج: {0} از {1}",
        'search_nav_hint': "Enter: بعدی  (Shift+Enter: قبلی)",
        'search_no_results': "نتیجه‌ای یافت نشد",
        'search_error': "خطا در جستجو",
        'search_active': "فیلد جستجو فعال شد",
        'search_closed': "جستجو پایان یافت",
        'search_position': "صفحه {0} {1}",
        'search_pos_top': "بالای صفحه",
        'search_pos_upper': "بخش بالایی",
        'search_pos_middle': "وسط",
        'search_pos_lower': "بخش پایینی",
        'search_pos_bottom': "پایین صفحه",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "تشخیص متن با موفقیت انجام شد!",
        'ocr_success_title': "OCR موفق",
        'ocr_success_message': "اکنون سند قابل جستجو است.",
        'ocr_failed': "OCR ناموفق",
        'ocr_in_progress': "OCR در حال انجام",
        'ocr_preparing': "در حال آماده‌سازی PDF...",
        'ocr_analyzing': "در حال تحلیل PDF...",
        'ocr_optimizing': "بهینه‌سازی تصویر...",
        'ocr_recognizing': "تشخیص متن...",
        'ocr_embedding': "درج متن...",
        'ocr_finalizing': "نهایی‌سازی PDF...",
        'ocr_not_available': "OCR در دسترس نیست",
        'ocr_install_message': "ابزارهای OCR یافت نشد.\n\nلطفاً نصب کنید:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR ضروری است",
        'ocr_question': "این PDF شامل متن قابل جستجو نیست.\nآیا می‌خواهید OCR را انجام دهید تا {0} ممکن شود؟",
        'ocr_perform': "انجام OCR",
        'ocr_later': "بعداً",
        'ocr_starting': "شروع OCR تضمینی...",
        'ocr_success_voice': "OCR موفق. PDF اکنون قابل جستجو است.",
        'ocr_partial_success': "OCR انجام شد، اما هنگام جایگزینی مشکلی پیش آمد.\n\nنسخه قابل جستجو در مسیر زیر ذخیره شد:\n{0}\n\nخطا: {1}",
        'ocr_partial_title': "OCR تا حدی موفق",
        'ocr_partial_voice': "OCR انجام شد، اما جایگزینی ناموفق بود.",
        'original_file': "فایل اصلی:",
        'old_size': "حجم قبلی:    {0} بایت",
        'new_size': "حجم جدید: {0} بایت",
        'size_change': "تغییر: {0}{1} بایت",
        'backup_created_file': "پشتیبان تهیه شد:\n{0}",
        'backup_not_created': "پشتیبان: تهیه نشد (تنظیم غیرفعال)",
        'page_header': "=== صفحه {0} ===\n{1}\n",
        'scanned_page_header': "=== صفحه {0} (اسکن شده) ===\n[این صفحه فقط شامل متن اسکن شده است]\n[لطفاً OCR را به صورت دستی انجام دهید]\n",
        'scanned_warning': "⚠️ متن اسکن شده - OCR ضروری است",
        'guaranteed_title': "PDF قابل جستجو ایجاد شد",
        'guaranteed_message': "<b>نسخه تضمینی قابل جستجو ایجاد شد!</b>\n\nاز آنجا که OCR خودکار ناموفق بود، یک PDF قابل جستجوی جایگزین ایجاد شد:\n\n{0}\n\n<b>این فایل شامل:</b>\n• متن استخراج شده (در صورت وجود)\n• نکاتی برای صفحات اسکن شده\n• کاملاً قابل جستجو است",
        'guaranteed_voice': "PDF قابل جستجوی تضمینی ایجاد شد.",
        'instruction_title': "راهنمای OCR",
        'instruction_file': "فایل اصلی: {0}",
        'instruction_text': "تشخیص خودکار متن (OCR) ناموفق بود.\nلطفاً OCR را به صورت دستی انجام دهید:\n\n1. با OCRmyPDF (خط فرمان):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. با ADOBE ACROBAT (macOS/Windows):\n   • PDF را در Acrobat باز کنید\n   • ابزارها > ویرایش PDF\n   • 'تشخیص متن' را انتخاب کنید\n\n3. با PREVIEW (macOS):\n   • PDF را در Preview باز کنید\n   • فایل > صادرات...\n   • فیلتر Quartz: 'کاهش حجم فایل'\n   • گزینه 'انجام OCR' را فعال کنید\n\n4. سرویس‌های آنلاین OCR:\n   • smallpdf.com/fa/ocr-pdf\n   • ilovepdf.com/fa/ocr-pdf\n   • adobe.com/ir_fa/acrobat/online/pdf-to-word.html",
        'instruction_created': "راهنمای OCR ایجاد شد",
        'instruction_created_message': "یک راهنمای دقیق ایجاد شد:\n\n{0}\n\nلطفاً مراحل را برای OCR دستی دنبال کنید.",
        'instruction_created_voice': "راهنمای OCR ایجاد شد.",
        'ocr_impossible': "OCR امکان‌پذیر نیست",
        'ocr_impossible_message': "OCR قابل انجام نیست.\n\nلطفاً '{0}' را به صورت دستی با نرم‌افزار OCR پردازش کنید.",
        'ocr_impossible_voice': "OCR امکان‌پذیر نیست. لطفاً دستی پردازش کنید.",
        'emergency_title': "OCR اضطراری",
        'emergency_message': "یک PDF اضطراری ایجاد شد:\n\n{0}\n\nلطفاً این فایل را به صورت دستی با OCR پردازش کنید.",
        'emergency_voice': "PDF اضطراری ایجاد شد. لطفاً OCR دستی انجام دهید.",
        'critical_error': "خطای بحرانی",
        'critical_error_message': "OCR نمی‌تواند شروع شود.\n\nلطفاً برنامه را مجدداً راه‌اندازی کنید و نصب OCR را بررسی کنید.",
        'critical_error_voice': "خطای بحرانی OCR",
        'ocr_question_html': "<p>این PDF شامل متن قابل جستجو نیست.<p>آیا می‌خواهید OCR را انجام دهید تا <b>{0}</b> ممکن شود؟</p>",
        'ocr_question_voice': "OCR ضروری است. PDF شامل متن قابل جستجو نیست. آیا می‌خواهید OCR را انجام دهید تا {0} ممکن شود؟",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "هیچ PDF بارگذاری نشده",
        'no_pdf_message': "هیچ PDF بارگذاری نشده است",
        'pdf_not_found': "فایل PDF یافت نشد",
        'file_size': "حجم فایل",
        'bytes': "بایت",
        'kb': "کیلوبایت",
        'mb': "مگابایت",
        'backup_created': "پشتیبان تهیه شد",
        'backup_disabled': "پشتیبان‌گیری غیرفعال است",
        'backup_activated': "ایجاد پشتیبان فعال شد",
        'backup_deactivated': "ایجاد پشتیبان غیرفعال شد",
        'backup_status': "پشتیبان: {0}",
        'backup_on': "✔ فعال",
        'backup_off': "✘ غیرفعال",
        'close_pdf': "بستن PDF: {0}",
        'pdf_not_found_format': "فایل PDF یافت نشد: {0}",
        'error_pdf_load_format': "خطا در بارگذاری PDF: {0}",
        'load_failed_format': "بارگذاری ناموفق:\n{0}",
        'decrypted_suffix': "(رمزگشایی شده)",
        'decryption_failed': "رمزگشایی ناموفق.",
        'decryption_error': "خطا در رمزگشایی",
        'decryption_success': "رمزگشایی موفق",
        'decryption_success_message': "PDF رمزگشایی و در مسیر زیر ذخیره شد:\n\n{0}",
        'decryption_success_voice': "PDF رمزگشایی و ذخیره شد.",
        'password_remove_error': "خطا در حذف رمز عبور",
        'save_unencrypted': "ذخیره PDF بدون رمز به عنوان",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "ذخیره به عنوان...",
        'save_copy': "ذخیره یک کپی",
        'save_success': "PDF در مسیر زیر ذخیره شد: {0}",
        'save_encrypted': "PDF محافظت شده در مسیر زیر ذخیره شد: {0}",
        'save_error': "PDF ذخیره نشد",
        'encryption_question': "آیا می‌خواهید PDF را با رمز عبور محافظت کنید؟",
        'encryption_yes': "بله",
        'encryption_no': "خیر",
        'encryption_cancel': "لغو",
        'save_cancel': "ذخیره لغو شد",
        'save_encrypted_voice': "فایل رمزگذاری و ذخیره شد.",
        'save_success_voice': "فایل PDF بدون رمز ذخیره شد.",
        'save_error_format': "PDF ذخیره نشد:\n{0}",
        'export_pages_success': "خروجی Pages موفق",
        'export_pages_error': "خروجی Pages ناموفق",
        'export_pages_error_format': "خروجی Pages ناموفق: {0}",
        'export_word_success': "خروجی Word موفق",
        'export_word_error': "خروجی Word ناموفق",
        'export_word_error_format': "خروجی Word ناموفق: {0}",
        'export_text_success': "خروجی متن موفق",
        'export_text_error': "خروجی متن ناموفق",
        'export_text_error_format': "خروجی متن ناموفق: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "رمز عبور لازم است",
        'password_enter': "لطفاً رمز عبور را وارد کنید",
        'password_confirm': "تأیید رمز عبور",
        'password_new': "رمز عبور جدید",
        'password_current': "رمز عبور فعلی",
        'password_save': "ذخیره رمز عبور (رمزگذاری شده)",
        'password_saved': "✓ رمز عبور برای این فایل ذخیره شد",
        'password_wrong': "رمز عبور اشتباه است",
        'password_mismatch': "رمزهای عبور مطابقت ندارند",
        'password_too_short': "رمز عبور خیلی کوتاه است",
        'password_min_length': "رمز عبور باید حداقل ۴ کاراکتر باشد",
        'password_strength': "قدرت رمز عبور",
        'password_strength_very_weak': "بسیار ضعیف",
        'password_strength_weak': "ضعیف",
        'password_strength_medium': "متوسط",
        'password_strength_strong': "قوی",
        'password_strength_very_strong': "بسیار قوی",
        'password_char_count': "({0} کاراکتر)",
        'password_match': "✓ مطابقت دارد",
        'password_no_match': "✗ رمزهای عبور مطابقت ندارند",
        'password_show': "نمایش",
        'password_hide': "مخفی",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "مدیریت رمز عبور",
        'password_table_filename': "نام فایل",
        'password_table_password': "رمز عبور",
        'password_count': "{0} رمز عبور ذخیره شده",
        'password_count_singular': "",
        'password_count_plural': "ها",
        'password_none': "هیچ رمز عبوری ذخیره نشده",
        'password_copied': "{0} رمز عبور کپی شد",
        'password_copied_singular': "",
        'password_copied_plural': "ها",
        'password_delete_confirm': "آیا مطمئن هستید که می‌خواهید رمز عبور برای '{0}' را حذف کنید؟",
        'password_delete_multiple': "آیا مطمئن هستید که می‌خواهید {0} رمز عبور انتخاب شده را حذف کنید؟",
        'password_delete_all_confirm': "آیا مطمئن هستید که می‌خواهید همه {0} رمز عبور ذخیره شده را حذف کنید؟",
        'password_deleted': "{0} رمز عبور حذف شد",
        'password_deleted_singular': "",
        'password_deleted_plural': "ها",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "ند",
        'password_all_deleted': "همه رمزهای عبور حذف شدند",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "تولیدکننده رمز عبور",
        'generator_generated': "رمز عبور تولید شده:",
        'generator_regenerate': "تولید مجدد",
        'generator_copy': "کپی",
        'generator_use': "استفاده",
        'generator_settings': "تنظیمات",
        'generator_length': "طول:",
        'generator_group_every': "جداکننده هر",
        'generator_group_chars': "کاراکتر. جداکننده:",
        'generator_uppercase': "حروف بزرگ (A-Z)",
        'generator_lowercase': "حروف کوچک (a-z)",
        'generator_digits': "اعداد (0-9)",
        'generator_symbols': "نمادها (!@#$%^&*)",
        'generator_exclude': "مستثنی شده:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "رمز عبور اصلی لازم است",
        'master_password_setup': "تنظیم رمز عبور اصلی",
        'master_password_change': "تغییر رمز عبور اصلی",
        'master_password_enter': "لطفاً رمز عبور اصلی خود را وارد کنید",
        'master_password_choose': "یک رمز عبور اصلی قوی انتخاب کنید (حداقل ۸ کاراکتر)",
        'master_password_new': "لطفاً رمز عبور اصلی جدید خود را وارد کنید",
        'master_password_confirm': "تأیید رمز عبور",
        'master_password_authenticate': "احراز هویت",
        'master_password_success': "رمز عبور اصلی با موفقیت تنظیم شد.",
        'master_password_changed': "رمز عبور اصلی با موفقیت تغییر کرد.",
        'master_password_removed': "رمز عبور اصلی و همه رمزهای عبور حذف شدند.",
        'master_password_remove': "حذف رمز عبور اصلی",
        'master_password_remove_confirm': "آیا مطمئن هستید که می‌خواهید همه رمزهای عبور را حذف کنید؟\n\nاین عمل قابل بازگشت نیست!",
        'master_password_export_before': "آیا می‌خواهید قبل از حذف یک نسخه پشتیبان تهیه کنید؟",
        'master_password_export_delete': "خروجی و حذف",
        'master_password_delete_now': "همین حالا حذف کن",
        'master_password_for_signatures': "برای استفاده از امضاها، باید یک رمز عبور اصلی تنظیم کنید.\n\nآیا می‌خواهید اکنون رمز عبور اصلی تنظیم کنید؟",
        'master_password_for_private': "برای استفاده از بلوک‌های متنی خصوصی، باید یک رمز عبور اصلی تنظیم کنید.\n\nآیا می‌خواهید اکنون رمز عبور اصلی تنظیم کنید؟",
        'master_password_info': """
            <b>🔐 بدون رمز عبور اصلی:</b><br>
            • نمایش، کپی و خروجی رمزهای عبور امکان‌پذیر نیست<br>
            • حذف رمزهای عبور همیشه امکان‌پذیر است (حتی بدون رمز اصلی)<br><br>

            <b>🔐 با رمز عبور اصلی:</b><br>
            • همه عملکردها پس از احراز هویت در دسترس هستند<br>
            • رمزهای عبور با رمز اصلی رمزگذاری می‌شوند<br>
            • حداقل طول: ۸ کاراکتر<br>
            • ذخیره امن با هش SHA-256<br><br>

            <b>مهم:</b><br>
            • در صورت گم شدن رمز اصلی: رمزهای عبور قابل بازیابی نیستند<br>
            • هنگام حذف رمز اصلی: همه رمزهای عبور حذف می‌شوند<br>
            • گزینه خروجی قبل از حذف موجود است<br>
            • رمز اصلی قابل تغییر در هر زمان
        """,
        'signature_auth_disabled': "غیرفعال کردن پرسش رمز عبور برای امضاها",
        'template_auth_disabled': "غیرفعال کردن پرسش رمز عبور برای بلوک‌های متنی خصوصی",
        'master_password_for_signatures_settings': "برای استفاده از امضاها، باید یک رمز عبور اصلی تنظیم کنید.\n\nبه تنظیمات - مدیریت رمز عبور بروید",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "محافظت از PDF",
        'protect_info': "فایل '{0}' با رمز عبور محافظت خواهد شد.",
        'protect_instruction': "لطفاً رمز عبور مورد نظر را دو بار وارد کنید تا سند محافظت شود، یا از تولیدکننده رمز عبور در سمت راست فیلد ورودی استفاده کنید.",
        'protect_success': "PDF با موفقیت محافظت و در مسیر زیر ذخیره شد:\n{0}\n\nرمز عبور: {1}\n\nآیا می‌خواهید PDF محافظت شده را اکنون باز کنید؟",
        'protect_open': "بله",
        'protect_skip': "خیر",
        'protect_error': "خطا در محافظت از PDF",
        'protect_open_title': "باز کردن PDF محافظت شده",
        'protect_question': "انجام شد. آیا می‌خواهید PDF محافظت شده را اکنون باز کنید؟ بله یا خیر؟",
        'password_cancel': "گفتگوی رمز عبور لغو شد",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "حذف صفحات",
        'pages_extract': "استخراج صفحات",
        'pages_insert': "درج صفحات",
        'pages_move': "جابجایی صفحات",
        'pages_delete_options': "گزینه‌های حذف",
        'pages_delete_empty': "حذف همه صفحات خالی",
        'pages_delete_current': "حذف صفحه فعلی",
        'pages_delete_range': "حذف محدوده صفحات",
        'pages_extract_options': "گزینه‌های استخراج",
        'pages_extract_current': "استخراج صفحه فعلی",
        'pages_extract_range': "استخراج محدوده صفحات",
        'pages_insert_position': "موقعیت درج",
        'pages_insert_before': "درج قبل از صفحه:",
        'pages_insert_select': "انتخاب PDF",
        'pages_insert_none': "هیچ PDF انتخاب نشده",
        'pages_move_source': "صفحات برای جابجایی",
        'pages_move_from': "از صفحه:",
        'pages_move_to': "تا صفحه:",
        'pages_move_target': "موقعیت هدف",
        'pages_move_before': "جابجایی قبل از صفحه:",
        'pages_move_hint': "نکته: صفحه ۱ = ابتدا، {0} = انتها",
        'pages_range_invalid': "صفحه شروع باید کوچکتر یا مساوی صفحه پایان باشد.",
        'pages_position_invalid': "موقعیت هدف نمی‌تواند درون محدوده جابجایی باشد.",
        'pages_no_pdf_selected': "هیچ PDF انتخاب نشده است.",
        'pages_deleted': "تعداد {0} صفحه حذف شد.",
        'pages_extracted': "استخراج شده: {0}\nذخیره شده در: {1}\nحجم فایل: {2:.1f} KB",
        'pages_inserted': "{0} صفحه درج شد",
        'pages_moved': "تعداد {0} صفحه جابجا شد.",
        'pages_deleted_none': "هیچ صفحه‌ای حذف نشد.",
        'pages_delete_progress': "در حال حذف صفحات...",
        'pages_deleted_with_backup': "تعداد {0} صفحه حذف شد.\n\nپشتیبان: {1}",
        'pages_deleted_voice': "یک نسخه پشتیبان تهیه شد و {0} صفحه حذف شد.",
        'info': "نکته",
        'error_dialog_creation': "گفتگو ایجاد نشد",
        'extract_page_single': "استخراج صفحه {0}",
        'extract_page_range': "استخراج صفحات {0}-{1}",
        'extract_success_voice': "صفحات با موفقیت استخراج شدند",
        'extract_error_format': "خطا در استخراج: {0}",
        'pages_inserted_voice': "تعداد {0} صفحه درج شد.",
        'insert_error_format': "خطا در درج: {0}",
        'pages_move_progress': "در حال جابجایی صفحات...",
        'pages_moved_with_backup': "تعداد {0} صفحه جابجا شد.\n\nپشتیبان: {1}",
        'move_success_title': "جابجایی موفق",
        'pages_moved_voice': "{0} صفحه با موفقیت جابجا شد",
        'mark_removed': "علامت صفحه {0} حذف شد",
        'mark_empty': "صفحه {0} به عنوان خالی علامت‌گذاری شد",
        'mark_export_removed': "علامت خروجی صفحه {0} حذف شد",
        'mark_export': "صفحه {0} برای خروجی علامت‌گذاری شد",
        'no_empty_pages': "هیچ صفحه خالی برای حذف علامت‌گذاری نشده",
        'delete_empty_confirm': "آیا می‌خواهید همه {0} صفحه خالی علامت‌گذاری شده را حذف کنید؟",
        'delete_empty_confirm_voice': "همین حالا همه {0} صفحه خالی علامت‌گذاری شده حذف شوند؟ بله یا خیر.",
        'empty_pages_deleted': "{0} صفحه خالی حذف شد",
        'no_export_pages': "هیچ صفحه‌ای برای خروجی علامت‌گذاری نشده",
        'overwrite_title': "جایگزینی فایل موجود",
        'overwrite_question': "فایل\n\n{0}\n\nاز قبل وجود دارد.\nآیا می‌خواهید آن را جایگزین کنید؟",
        'overwrite_voice': "جایگزینی فایل موجود؟ بله یا خیر.",
        'page_skipped': "صفحه {0} نادیده گرفته شد",
        'export_complete': "خروجی کامل شد.",
        'export_complete_voice': "خروجی کامل شد.",
        'no_pages_exported': "هیچ صفحه‌ای خروجی گرفته نشد",
        'export_cancelled': "خروجی لغو شد",
        'pages_exported': "{0} صفحه به {1} خروجی داده شد",
        'export_page_title': "خروجی صفحه",
        'page_exported': "صفحه {0} به {1} خروجی داده شد",
        'export_error': "خطا در خروجی",
        'export_marked_title': "خروجی صفحات علامت‌گذاری شده",
        'rotate_all_title': "چرخاندن همه صفحات",
        'rotate_all_question': "آیا می‌خواهید همه صفحات را ۹۰ درجه به راست بچرخانید؟",
        'rotate_all_voice': "آیا می‌خواهید همه صفحات را ۹۰ درجه به راست بچرخانید؟ بله یا خیر؟",
        'all_pages_rotated': "همه صفحات چرخانده شدند",
        'page_rotated': "صفحه {0} چرخانده شد",
        'rotate_error': "صفحه چرخانده نشد",
        'delete_page_confirm': "آیا می‌خواهید صفحه {0} را حذف کنید؟",
        'delete_page_confirm_voice': "آیا مطمئن هستید که می‌خواهید صفحه {0} را حذف کنید؟ بله یا خیر.",
        'page_deleted': "صفحه {0} حذف شد",
        'delete_error': "صفحه حذف نشد",
        'pages_deleted_voice': "{0} صفحه حذف شد",
        'pages_exported_split': "{0} صفحه با موفقیت خروجی داده شد.",
        'pages_skipped': "{0} صفحه نادیده گرفته شد.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "استخراج صفحات (پیشرفته)",
        'pdf_splitter_title': "تقسیم‌کننده و استخراج‌کننده PDF",
        'pdf_splitter_load': " انتخاب فایل PDF",
        'pdf_splitter_info': "لطفاً یک گزینه برای سند PDF خود انتخاب کنید",
        'pdf_splitter_basic': "عملیات پایه",
        'pdf_splitter_single': "تقسیم به صفحات جداگانه",
        'pdf_splitter_range': "استخراج صفحات:",
        'pdf_splitter_range_placeholder': "مثال: ۱-۳,۵,۷-۹",
        'pdf_splitter_clean': "عملیات پاک‌سازی",
        'pdf_splitter_remove_empty': "حذف همه صفحات خالی",
        'pdf_splitter_remove': "حذف محدوده صفحات:",
        'pdf_splitter_remove_placeholder': "مثال: ۲,۴-۶",
        'pdf_splitter_process': "پردازش PDF",
        'pdf_splitter_loaded': "PDF بارگذاری شد. لطفاً یک گزینه انتخاب کنید",
        'pdf_read_error': "PDF خوانده نشد",
        'pages': "صفحات",
        'pages_created': "صفحات ایجاد شدند",
        'range_empty': "لطفاً یک محدوده صفحه وارد کنید",
        'range_invalid': "محدوده صفحه نامعتبر",
        'range_created': "PDF جدید با صفحات انتخاب شده ایجاد شد:\n{0}",
        'empty_removed': "{0} صفحه خالی حذف شد.\nخروجی: {1}",
        'remove_empty': "لطفاً صفحاتی را برای حذف وارد کنید",
        'remove_invalid': "صفحات برای حذف نامعتبر",
        'remove_done': "PDF پاک‌سازی شده ایجاد شد:\n{0}",
        'open_folder': "باز کردن پوشه",
        'show_in_finder': "نمایش در Finder",
        'pdf_splitter_no_pdf': "لطفاً ابتدا یک فایل PDF بارگذاری کنید.",
        'process_error': "خطا در پردازش PDF",
        'pages_created_voice': "{0} صفحه ایجاد شد",
        'range_created_voice': "PDF با صفحات انتخاب شده ایجاد شد",
        'empty_removed_voice': "{0} صفحه خالی حذف شد",
        'remove_done_voice': "PDF پاک‌سازی شده ایجاد شد",
        'pdf_splitter_split_groups': "هر گروه پیوسته در یک فایل جداگانه",
        'range_created_single': "PDF جدید ایجاد شد:\n{0}",
        'range_created_multiple': "{0} فایل PDF ایجاد شد.",
        'range_created_voice_single': "یک PDF با صفحات انتخاب شده ایجاد شد",
        'range_created_voice_multiple': "{0} فایل PDF ایجاد شد",
        'empty_removed_none_left': "هیچ صفحه‌ای باقی نمانده",
        'empty_removed_all_empty': "همه صفحات به عنوان خالی تشخیص داده شده و حذف خواهند شد. هیچ فایلی ایجاد نشد.",
        'preview_single': "پیش‌نمایش: {0}",
        'preview_enter_range': "لطفاً یک محدوده صفحه وارد کنید.",
        'preview_invalid_range': "محدوده صفحه نامعتبر.",
        'preview_file': "پیش‌نمایش: {0}",
        'preview_files': "پیش‌نمایش: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "شروع چاپ",
        'print_sent': "درخواست چاپ ارسال شد",
        'print_now': "چاپ فوری",
        'print_error': "خطا در چاپ فوری",
        'print_limited': "عملکرد چاپ در این سیستم محدود است",
        'print_error_format': "خطا در چاپ فوری: {0}",
        'warning': "توجه",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "تغییر به حالت روشن",
        'mode_switch_to_dark': "تغییر به حالت تاریک",
        'mode_dark_activated': "حالت تاریک فعال شد",
        'mode_light_activated': "حالت روشن فعال شد",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "نمایش کامل",
        'zoom_two_pages': "دو صفحه در کنار هم",
        'zoom_overview': "حالت نمای کلی",
        'zoom_cannot_during_search': "بزرگنمایی در حین جستجو ممکن نیست",
        'zoom_exit_first': "لطفاً ابتدا بزرگنمایی را پایان دهید",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "کشیدن و رها کردن فعال شد",
        'drag_disabled': "کشیدن و رها کردن غیرفعال شد",
        'drag_page_grab': "صفحه {0} گرفته شد",
        'drag_page_dropped': "صفحه {0} در موقعیت {1} درج شد",
        'drag_position_invalid': "موقعیت نامعتبر",
        'drag_same_position': "صفحه {0} در موقعیت {0} باقی ماند",
        'drag_error': "خطا در جابجایی",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "ورودی متن با قالب‌بندی پیشرفته و مدیریت بلوک‌های متنی",
        'text_templates': "بلوک‌های متنی موجود:",
        'text_name': "نام",
        'text_preview': "پیش‌نمایش متن",
        'text_enter': "متن:",
        'text_font_size': "اندازه قلم:",
        'text_formatting': "قالب‌بندی:",
        'text_bold': "پررنگ",
        'text_italic': "مورب",
        'text_underline': "زیرخط‌دار",
        'text_alignment': "تراز:",
        'text_left': "چپ",
        'text_center': "وسط",
        'text_right': "راست",
        'text_color': "رنگ متن:",
        'text_opacity': "شفافیت:",
        'text_word_wrap': "شکستن خط:",
        'text_auto': "خودکار",
        'text_page_width_95': "عرض صفحه (۹۵٪)",
        'text_page_width_85': "بسیار عریض (۸۵٪)",
        'text_page_width_75': "عریض (۷۵٪)",
        'text_page_width_60': "نسبتاً عریض (۶۰٪)",
        'text_page_width_50': "متوسط (۵۰٪)",
        'text_page_width_30': "باريك (۳۰٪)",
        'text_page_width_20': "باريك‌تر (۲۰٪)",
        'text_page_width_10': "بسیار باريك (۱۰٪)",
        'text_no_wrap': "بدون شکستن",
        'text_private': "بلوک متنی خصوصی (نیاز به احراز هویت)",
        'text_preview_label': "پیش‌نمایش:",
        'text_preview_placeholder': "پیش‌نمایش متن در اینجا نمایش داده می‌شود...",
        'text_no_text': "(بدون متن)",
        'text_save_template': "💾 ذخیره به عنوان بلوک",
        'text_delete_template': "🗑 حذف بلوک متنی انتخاب شده",
        'text_show_private': "نمایش خصوصی",
        'text_hide_private': "مخفی کردن خصوصی",
        'text_use': "✅ استفاده از متن",
        'text_saved': "بلوک متنی به عنوان ذخیره شد:\n{0}",
        'text_saved_voice': "بلوک متنی ذخیره شد",
        'text_deleted': "بلوک متنی حذف شد",
        'text_no_text_to_save': "متنی برای ذخیره وجود ندارد.",
        'text_no_templates': "هیچ بلوک متنی یافت نشد",
        'text_private_master_required': "بلوک‌های خصوصی فقط در صورتی قابل استفاده هستند که رمز عبور اصلی تنظیم شده باشد.\n\nآیا می‌خواهید اکنون رمز عبور اصلی تنظیم کنید؟",
        'text_filename': "نام فایل برای بلوک متنی (بدون 'Text_' و '.txt'):",
        'text_filename_hint': "مثال: 'تلفن خانه' به عنوان 'Text_تلفن خانه.txt' ذخیره می‌شود",
        'text_save_hint': "بلوک متنی به طور خودکار با قالب‌بندی ذخیره می‌شود.",
        'text_guide_title': "ورودی متن - راهنما",
        'text_delete_confirm': "آیا مطمئن هستید که می‌خواهید این بلوک متنی را حذف کنید؟\n\nفایل: {0}\nمتن: {1}...",
        'text_make_public': "علامت‌گذاری به عنوان عمومی",
        'text_make_private': "علامت‌گذاری به عنوان خصوصی",
        'text_privacy_changed': "وضعیت خصوصی تغییر کرد",
        'text_private_always': "خصوصی همیشه قابل مشاهده (تنظیمات)",
        'text_mode_required': "لطفاً ابتدا حالت متن را فعال کنید",
        'text_continue_editing': "ادامه ویرایش - مکان‌نما در انتهای متن",
        'text_no_input': "متنی وارد نشده - متن دور ریخته شد",
        'save_dialog_question': "چگونه می‌خواهید ادامه دهید؟",
        'text_save_question': "ذخیره همه متون و ضربدرها، تنظیم، ادامه ویرایش یا دور ریختن؟",
        'copy_cross': "ضربدر کپی شد",
        'paste_cross': "ضربدر چسبانده شد",
        'paste_text': "متن چسبانده شد",
        'cross_discarded': "ضربدر دور ریخته شد",
        'all_discarded': "همه دور ریخته شدند",
        'text_discarded': "متن دور ریخته شد",
        'no_texts_to_save': "متنی برای ذخیره وجود ندارد",
        'no_valid_texts': "متن معتبری برای ذخیره وجود ندارد",
        'text_word_singular': "متن",
        'text_word_plural': "متن‌ها",
        'cross_word_singular': "ضربدر",
        'cross_word_plural': "ضربدرها",
        'texts_saved_title': "متون ذخیره شدند",
        'texts_crosses_saved': "{0} {1} و {2} {3} در PDF درج شدند.\n\nPDF دوباره بارگذاری شد...",
        'texts_crosses_saved_voice': "{0} {1} و {2} {3} ذخیره شد.",
        'texts_saved': "{0} {1} در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'texts_saved_voice': "{0} {1} ذخیره شد.",
        'crosses_saved': "{0} {1} در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'crosses_saved_voice': "{0} {1} ذخیره شد.",
        'elements_saved': "{0} عنصر در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'elements_saved_voice': "{0} عنصر ذخیره شد.",
        'text_window_load_error': "پنجره متن بارگذاری نشد",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **ورودی متن و بلوک‌های متنی – راهنمای جامع**

        **1. درج و ویرایش متن**
        - روی محل مورد نظر در سند کلیک راست کرده و "درج متن" را انتخاب کنید.
        - یک گفتگو باز می‌شود که در آن می‌توانید متن خود را وارد و قالب‌بندی کنید:
        • اندازه قلم، پررنگ، مورب، زیرخط‌دار
        • رنگ متن (قابل انتخاب آزاد)
        • شفافیت (تیرگی) با لغزنده
        • شکستن خط (عرض‌های مختلف، مثلاً عرض صفحه، باریک، بدون شکستن)
        - پس از تأیید، متن در محل کلیک ظاهر می‌شود. می‌توانید آن را با ماوس یا کلیدهای جهت‌دار جابجا کنید.
        - دوبار کلیک روی متن حالت ویرایش را باز می‌کند؛ با ESC خارج شوید.

        **2. مدیریت بلوک‌های متنی (الگوها)**
        - در گفتگوی متن، در سمت چپ لیستی از تمام بلوک‌های متنی ذخیره شده را می‌بینید.
        - **ذخیره یک بلوک:** متن خود را وارد کنید، قالب‌بندی کنید و روی "💾 ذخیره به عنوان بلوک" کلیک کنید. یک نام فایل وارد کنید (بدون پسوند).
        - **بارگذاری یک بلوک:** روی نام مورد نظر در لیست کلیک کنید. متن و قالب‌بندی اعمال می‌شود و در صورت نیاز قابل تنظیم است.
        - **حذف:** با کلیک راست روی یک بلوک می‌توانید آن را حذف یا وضعیت خصوصی آن را تغییر دهید.

        **3. بلوک‌های متنی خصوصی (رمز عبور اصلی)**
        - اگر رمز عبور اصلی را تنظیم کرده‌اید (در تنظیمات → مدیریت رمز عبور)، می‌توانید بلوک‌ها را به عنوان "خصوصی" علامت‌گذاری کنید.
        - برای این کار، قبل از ذخیره، کادر "بلوک متنی خصوصی" را در گفتگو فعال کنید.
        - بلوک‌های خصوصی فقط در صورتی در لیست نمایش داده می‌شوند که یک بار در هر نشست رمز عبور اصلی خود را وارد کرده باشید (احراز هویت با نماد قفل یا در اولین دسترسی).
        - به این ترتیب می‌توانید از بلوک‌های متنی محرمانه در برابر دسترسی دیگران محافظت کنید.

        **4. درج ضربدر**
        - از طریق منوی زمینه می‌توانید یک ضربدر گرافیکی (مثلاً برای کادر علامت‌گذاری) درج کنید.
        - اندازه، ضخامت خط و رنگ ضربدرها را می‌توانید به صورت سراسری در تنظیمات تنظیم کنید (منوی "تنظیمات" → "تنظیمات ضربدر").
        - با کلیک راست روی یک ضربدر موجود می‌توانید آن را به طور جداگانه تغییر دهید.

        **5. اقدامات گروهی**
        - اگر چندین متن یا ضربدر در یک صفحه قرار داده‌اید، می‌توانید از طریق منوی زمینه (کلیک راست در حالت متن) همه عناصر را با هم ذخیره یا دور بریزید.
        - هنگام ذخیره، همه عناصر در PDF جاسازی می‌شوند و به عنوان گرافیک برداری باقی می‌مانند.

        **6. میانبرهای صفحه کلید در حالت متن**
        - کلیدهای جهت‌دار: جابجایی عنصر
        - Ctrl+کلیدهای جهت‌دار: گام‌های بزرگتر
        - Enter: باز کردن گفتگوی ذخیره (ذخیره همه / تنظیم / دور ریختن)
        - ESC: دور ریختن عنصر فعلی
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 ورودی متن و بلوک‌های متنی – راهنمای جامع</strong></p>

        <p><strong>1. درج و ویرایش متن</strong></p>
        <ul>
        <li>روی محل مورد نظر در سند کلیک راست کرده و "درج متن" را انتخاب کنید.</li>
        <li>یک گفتگو باز می‌شود که در آن می‌توانید متن خود را وارد و قالب‌بندی کنید:<br/>
        • اندازه قلم، پررنگ، مورب، زیرخط‌دار<br/>
        • رنگ متن (قابل انتخاب آزاد)<br/>
        • شفافیت (تیرگی) با لغزنده<br/>
        • شکستن خط (عرض‌های مختلف، مثلاً عرض صفحه، باریک، بدون شکستن)</li>
        <li>پس از تأیید، متن در محل کلیک ظاهر می‌شود. می‌توانید آن را با ماوس یا کلیدهای جهت‌دار جابجا کنید.</li>
        <li>دوبار کلیک روی متن حالت ویرایش را باز می‌کند؛ با ESC خارج شوید.</li>
        </ul>

        <p><strong>2. مدیریت بلوک‌های متنی (الگوها)</strong></p>
        <ul>
        <li>در گفتگوی متن، در سمت چپ لیستی از تمام بلوک‌های متنی ذخیره شده را می‌بینید.</li>
        <li><strong>ذخیره یک بلوک:</strong> متن خود را وارد کنید، قالب‌بندی کنید و روی "💾 ذخیره به عنوان بلوک" کلیک کنید. یک نام فایل وارد کنید (بدون پسوند).</li>
        <li><strong>بارگذاری یک بلوک:</strong> روی نام مورد نظر در لیست کلیک کنید. متن و قالب‌بندی اعمال می‌شود و در صورت نیاز قابل تنظیم است.</li>
        <li><strong>حذف:</strong> با کلیک راست روی یک بلوک می‌توانید آن را حذف یا وضعیت خصوصی آن را تغییر دهید.</li>
        </ul>

        <p><strong>3. بلوک‌های متنی خصوصی (رمز عبور اصلی)</strong></p>
        <ul>
        <li>اگر رمز عبور اصلی را تنظیم کرده‌اید (در تنظیمات → مدیریت رمز عبور)، می‌توانید بلوک‌ها را به عنوان "خصوصی" علامت‌گذاری کنید.</li>
        <li>برای این کار، قبل از ذخیره، کادر "بلوک متنی خصوصی" را در گفتگو فعال کنید.</li>
        <li>بلوک‌های خصوصی فقط در صورتی در لیست نمایش داده می‌شوند که یک بار در هر نشست رمز عبور اصلی خود را وارد کرده باشید (احراز هویت با نماد قفل یا در اولین دسترسی).</li>
        <li>به این ترتیب می‌توانید از بلوک‌های متنی محرمانه در برابر دسترسی دیگران محافظت کنید.</li>
        </ul>

        <p><strong>4. درج ضربدر</strong></p>
        <ul>
        <li>از طریق منوی زمینه می‌توانید یک ضربدر گرافیکی (مثلاً برای کادر علامت‌گذاری) درج کنید.</li>
        <li>اندازه، ضخامت خط و رنگ ضربدرها را می‌توانید به صورت سراسری در تنظیمات تنظیم کنید (منوی "تنظیمات" → "تنظیمات ضربدر").</li>
        <li>با کلیک راست روی یک ضربدر موجود می‌توانید آن را به طور جداگانه تغییر دهید.</li>
        </ul>

        <p><strong>5. اقدامات گروهی</strong></p>
        <ul>
        <li>اگر چندین متن یا ضربدر در یک صفحه قرار داده‌اید، می‌توانید از طریق منوی زمینه (کلیک راست در حالت متن) همه عناصر را با هم ذخیره یا دور بریزید.</li>
        <li>هنگام ذخیره، همه عناصر در PDF جاسازی می‌شوند و به عنوان گرافیک برداری باقی می‌مانند.</li>
        </ul>

        <p><strong>6. میانبرهای صفحه کلید در حالت متن</strong></p>
        <ul>
        <li>کلیدهای جهت‌دار: جابجایی عنصر</li>
        <li>Ctrl+کلیدهای جهت‌دار: گام‌های بزرگتر</li>
        <li>Enter: باز کردن گفتگوی ذخیره (ذخیره همه / تنظیم / دور ریختن)</li>
        <li>ESC: دور ریختن عنصر فعلی</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "تنظیمات ضربدر",
        'cross_properties': "ویژگی‌های ضربدر",
        'cross_size': "اندازه (پیکسل):",
        'cross_line_width': "ضخامت خط:",
        'cross_color': "رنگ:",
        'cross_choose_color': "انتخاب",
        'cross_fine_tuning': "تنظیم دقیق هنگام ذخیره (پیکسل)",
        'cross_offset_x': "افست X:",
        'cross_offset_y': "افست Y:",
        'cross_offset_x_tooltip': "مقادیر منفی ضربدر را هنگام ذخیره به چپ منتقل می‌کند، مثبت به راست",
        'cross_offset_y_tooltip': "مقادیر منفی ضربدر را هنگام ذخیره به بالا منتقل می‌کند، مثبت به پایین",
        'cross_preview': "پیش‌نمایش",
        'cross_save': "اعمال تنظیمات",
        'cross_customized': "ضربدر تنظیم شد",
        'cross_settings_applied': "تنظیمات ضربدر ذخیره شد.\nاندازه: {0}px، ضخامت خط: {1}px\n{2}",
        'cross_updated_count': "تعداد {0} ضربدر موجود به‌روزرسانی شد.",
        'cross_no_crosses': "هیچ ضربدر موجودی یافت نشد.",
        'cross_settings_applied_all': "تنظیمات ضربدر برای همه {0} ضربدر اعمال شد",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "تنظیمات امضا",
        'signature_1': "امضای ۱",
        'signature_2': "امضای ۲",
        'signature_select': "انتخاب امضا",
        'signature_add': "➕ افزودن امضای جدید...",
        'signature_size': "اندازه برای امضای {0} (٪):",
        'signature_common': "تنظیمات عمومی",
        'signature_timestamp': "افزودن خودکار مهر زمان",
        'signature_location': "مکان پیش‌فرض:",
        'signature_timestamp_size': "اندازه قلم مهر زمان:",
        'signature_no_files': "-- هیچ امضایی یافت نشد --",
        'signature_insert': "درج امضا",
        'signature_insert_1': "درج امضای ۱",
        'signature_insert_2': "درج امضای ۲",
        'signature_customize': " تنظیم این امضا",
        'signature_discard': " دور ریختن این امضا",
        'signature_save_all': " ذخیره همه امضاها",
        'signature_discard_all': " دور ریختن همه امضاها",
        'signature_guide_title': "امضاها - راهنما",
        'signature_guide': """
📝 امضاها - راهنمای سریع

- رمز عبور اصلی را تنظیم کنید
- امضاها را در منوی تنظیمات پیکربندی کنید
  (اندازه، مهر زمان ...)
- درج با کلیک راست در موقعیت مورد نظر
  (رمز اصلی یک بار در هر نشست لازم است)
- امضا را با ماوس یا کلیدهای جهت‌دار جابجا کنید
- چندین امضا می‌توانند پشت سر هم درج شوند
- هر امضا می‌تواند به طور جداگانه تنظیم شود
- دور ریختن یک امضای خاص
- ذخیره / دور ریختن همه امضاها به طور همزمان
- همچنین می‌توان از نوار منو استفاده کرد.
        """,
        'signature_placeholder': "پیش‌نمایش موجود نیست",
        'signature_info': "امضای {0}: {1}×{2} پیکسل ({3}٪ از {4}×{5})",
        'signature_info_placeholder': "تنظیمات برای امضای {0}",
        'signature_inserted': "امضای {0} در صفحه {1} درج شد",
        'signature_deleted': "امضا حذف شد",
        'signature_copied': "امضا کپی شد",
        'signature_pasted': "امضای {0} چسبانده شد",
        'signature_saved': "{0} امضا در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'signature_saved_voice': "{0} امضا ذخیره شد",
        'mode_replace_signature_format': "پایان حالت و درج امضای {0}",
        'mode_conflict_voice_signature': "حالت {0} فعال است. پایان و درج امضا؟",
        'signature_not_configured': "امضای {0} پیکربندی نشده",
        'signature_file_not_found': "فایل امضا یافت نشد",
        'timestamp_format': "{0}، {1}",
        'no_copied_signature': "هیچ امضای کپی شده‌ای وجود ندارد",
        'no_signatures_to_save': "هیچ امضایی برای ذخیره وجود ندارد",
        'signature_save_question': "ذخیره همه امضاها، تنظیم یا دور ریختن این یکی؟",
        'signatures_saved_title': "امضاها ذخیره شدند",
        'signatures_saved': "{0} امضا در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'signatures_saved_voice': "{0} امضا ذخیره شد.",
        'all_signatures_discarded': "همه امضاها دور ریخته شدند",
        'signature_settings_saved': "تنظیمات امضا ذخیره شد",
        'signature_cancelled': "امضا دور ریخته شد",
        'signature_active_title': "امضا فعال است",
        'signature_replace_question': "در حال حاضر یک امضا فعال است.\n\nآیا می‌خواهید امضای فعلی را جایگزین کنید؟",
        'signature_replace': "جایگزینی امضا",
        'signature_replace_voice': "جایگزینی امضای فعلی یا لغو؟",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "تنظیمات تصویر",
        'image_common': "تنظیمات عمومی تصویر",
        'image_keep_aspect': "حفظ نسبت تصویر هنگام کشیدن",
        'image_default_size': "اندازه پیش‌فرض (٪):",
        'image_dark_invert': "وارونه‌سازی تصاویر در حالت تاریک",
        'image_dark_invert_tooltip': "فعال: تصاویر برای دید بهتر وارونه می‌شوند",
        'image_fine_tuning': "تنظیم دقیق (پیکسل)",
        'image_offset_x': "افست X:",
        'image_offset_y': "افست Y:",
        'image_offset_x_tooltip': "مقادیر منفی تصویر را هنگام ذخیره به چپ منتقل می‌کند، مثبت به راست",
        'image_offset_y_tooltip': "مقادیر منفی تصویر را هنگام ذخیره به بالا منتقل می‌کند، مثبت به پایین",
        'image_select': "انتخاب تصویر",
        'image_insert': "درج تصویر",
        'image_customize': " تنظیم این تصویر",
        'image_aspect': " حفظ نسبت تصویر",
        'image_discard': " دور ریختن این تصویر",
        'image_save_all': " ذخیره همه تصاویر",
        'image_discard_all': " دور ریختن همه تصاویر",
        'image_filter': "تصاویر",
        'image_guide_title': "درج تصویر - راهنما",
        'image_guide': """
📷 درج تصویر در PDF - راهنمای سریع:

1. روی موقعیت مورد نظر کلیک راست کنید
2. "درج تصویر" → تصویر را انتخاب کنید
3. تصویر را قرار دهید: با ماوس بکشید
4. اندازه را تنظیم کنید: در گوشه‌ها/لبه‌ها بکشید
5. حفظ نسبت تصویر: کلید [A] را فشار دهید
6. تنظیمات بیشتر: روی تصویر کلیک راست کنید

نکته: در منوی زمینه می‌توانید تنظیمات را تغییر دهید.
        """,
        'image_inserted': "تصویر {0} در صفحه {1} درج شد",
        'image_deleted': "تصویر دور ریخته شد",
        'image_copied': "تصویر کپی شد",
        'image_pasted': "تصویر چسبانده شد",
        'image_saved': "{0} تصویر در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'image_saved_voice': "{0} تصویر ذخیره شد",
        'image_aspect_on': "فعال",
        'image_aspect_off': "غیرفعال",
        'image_aspect_toggle': "حفظ نسبت تصویر {0}",
        'image_reset': "تصویر به اندازه اصلی بازگردانده شد",
        'image_replaced': "تصویر جایگزین شد",
        'image_invalid': "تصویر معتبر نیست",
        'mode_replace_image': "درج تصویر",
        'mode_conflict_voice_image': "حالت {0} فعال است. پایان و درج تصویر؟",
        'image_active_title': "تصویر فعال است",
        'image_replace_question': "در حال حاضر یک تصویر فعال است.\n\nآیا می‌خواهید تصویر فعلی را جایگزین کنید؟",
        'image_replace': "جایگزینی تصویر",
        'image_replace_voice': "جایگزینی تصویر فعلی یا لغو؟",
        'image_filter_all': "تصاویر (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;همه فایل‌ها (*.*)",
        'no_copied_image': "هیچ تصویر کپی شده‌ای وجود ندارد",
        'image_discarded': "تصویر دور ریخته شد",
        'image_save_question': "ذخیره همه تصاویر، تنظیم یا دور ریختن این یکی؟",
        'no_images_to_save': "هیچ تصویری برای ذخیره وجود ندارد",
        'no_valid_images': "تصویر معتبری برای ذخیره وجود ندارد",
        'images_saved_title': "تصاویر ذخیره شدند",
        'images_saved': "{0} تصویر در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'images_saved_voice': "{0} تصویر ذخیره شد.",
        'all_images_discarded': "همه تصاویر دور ریخته شدند",
        'image_settings_updated': "تنظیمات تصویر به‌روزرسانی شد",
        'image_replace_title': "انتخاب تصویر جدید",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "تنظیمات اشکال",
        'form_basic': "تنظیمات پایه",
        'form_default_type': "نوع شکل پیش‌فرض:",
        'form_rectangle': "مستطیل",
        'form_ellipse': "بیضی",
        'form_line': "خط",
        'form_arrow': "پیکان",
        'form_line_width': "ضخامت خط:",
        'form_colors': "رنگ‌ها",
        'form_line_color': "رنگ خط:",
        'form_fill_color': "رنگ پرکننده:",
        'form_choose_color': "انتخاب",
        'form_transparent': "پس‌زمینه شفاف (فقط خط)",
        'form_filled': "پر شده",
        'form_dark_mode': "حالت تاریک",
        'form_dark_invert': "وارونه‌سازی رنگ‌ها در حالت تاریک",
        'form_fine_tuning': "تنظیم دقیق (پیکسل)",
        'form_offset_x': "افست X:",
        'form_offset_y': "افست Y:",
        'form_offset_x_tooltip': "مقادیر منفی شکل را هنگام ذخیره به چپ منتقل می‌کند، مثبت به راست",
        'form_offset_y_tooltip': "مقادیر منفی شکل را هنگام ذخیره به بالا منتقل می‌کند، مثبت به پایین",
        'form_preview': "پیش‌نمایش",
        'form_insert': "درج شکل",
        'form_rectangle_insert': "مستطیل",
        'form_ellipse_insert': "بیضی/دایره",
        'form_line_insert': "خط (۲ کلیک)",
        'form_arrow_insert': "پیکان (۲ کلیک)",
        'form_customize': " تنظیم این شکل",
        'form_transparent_toggle': " پس‌زمینه شفاف",
        'form_discard': " دور ریختن این شکل",
        'form_save_all': " ذخیره همه اشکال",
        'form_discard_all': " دور ریختن همه اشکال",
        'form_guide_title': "درج اشکال - راهنما",
        'form_guide': """
📐 درج اشکال در PDF - راهنمای سریع:

1. نوع شکل را انتخاب کنید (مستطیل، بیضی، خط، پیکان)
2. روی موقعیت کلیک کنید
   - برای مستطیل/بیضی: یک کلیک شکل را قرار می‌دهد
   - برای خط/پیکان: دو کلیک برای نقطه شروع و پایان
3. شکل را قرار دهید: با ماوس بکشید
4. اندازه را تنظیم کنید: در گوشه‌ها/لبه‌ها بکشید
5. ذخیره شکل: Enter
6. دور ریختن شکل: ESC
7. تنظیمات بیشتر: روی شکل کلیک راست کنید

نکته: در منوی زمینه می‌توانید تنظیمات را تغییر دهید.
        """,
        'form_inserted': "{0} در صفحه {1} درج شد",
        'form_deleted': "شکل حذف شد",
        'form_copied': "شکل کپی شد",
        'form_pasted': "شکل چسبانده شد",
        'form_saved': "{0} شکل در PDF درج شد.\n\nPDF دوباره بارگذاری شد...",
        'form_saved_voice': "{0} شکل ذخیره شد",
        'form_reset': "شکل به اندازه استاندارد بازگردانده شد",
        'form_transparent_on': "فعال",
        'form_transparent_off': "غیرفعال",
        'form_transparent_toggled': "پس‌زمینه شفاف {0}",
        'form_line_cancel': "کشیدن خط لغو شد",
        'form_second_click': "اکنون نقطه پایان را برای {0} کلیک کنید",
        'mode_replace_form': "درج شکل",
        'mode_conflict_voice_form': "حالت {0} فعال است. پایان و درج شکل؟",
        'form_settings_updated': "تنظیمات اشکال به‌روزرسانی شد",
        'form_unknown': "شکل",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "۱. روی موقعیت شروع کلیک کنید",
        'form_line_guide_2': "۲. روی موقعیت پایان کلیک کنید",
        'form_line_guide_3': "خط بین دو نقطه رسم خواهد شد.",
        'form_line_status_1': "منتظر اولین کلیک...",
        'form_line_status_2': "نقطه اول تعیین شد: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "اکنون نقطه پایان را کلیک کنید...",
        'form_line_status_4': "هر دو نقطه تعیین شدند.\nبرای ذخیره روی 'پایان' کلیک کنید.",
        'form_line_reset': "بازنشانی",
        'form_line_finish': "پایان",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "کپی (Cmd+C)",
        'paste': "چسباندن (Cmd+V)",
        'copied': "کپی شد: {0}",
        'no_element_to_copy': "هیچ عنصری برای کپی انتخاب نشده",
        'no_copied_data': "هیچ داده کپی شده‌ای وجود ندارد",
        'no_valid_position': "موقعیت معتبری برای چسباندن وجود ندارد",
        'copy_text': "متن کپی شد",
        'copy_image': "تصویر کپی شد",
        'copy_form': "شکل کپی شد",
        'copy_signature': "امضا کپی شد",
        'element_text': "متن",
        'element_image': "تصویر",
        'element_form': "شکل",
        'element_signature': "امضا",
        'element_unknown': "عنصر",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "تداخل حالت",
        'mode_conflict_message': "حالت '{0}' در حال حاضر فعال است.\n\nآیا می‌خواهید آن را پایان داده و {1}؟",
        'mode_replace': "پایان حالت و {0}",
        'mode_cancel': "لغو",
        'mode_replace_text': "درج متن",
        'mode_replace_cross': "درج ضربدر",
        'mode_replace_signature': "درج امضا",
        'mode_replace_image': "درج تصویر",
        'mode_replace_form': "درج شکل",
        'mode_conflict_voice': "حالت {0} فعال است. پایان و درج متن؟",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "ورودی متن",
        'active_mode_signature': "امضا",
        'active_mode_image': "تصویر",
        'active_mode_form': "شکل",
        'active_mode_and': " و ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "درج",
        'insert_another_text': "درج متن",
        'insert_another_cross': "درج ضربدر",
        'insert_another_signature_1': "امضای ۱",
        'insert_another_signature_2': "امضای ۲",
        'insert_another_image': "درج تصویر",
        'insert_another_form_rect': "مستطیل",
        'insert_another_form_ellipse': "بیضی",
        'insert_another_form_line': "خط (۲ کلیک)",
        'insert_another_form_arrow': "پیکان (۲ کلیک)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "ذخیره {0}",
        'save_dialog_message': "{0} در صفحه {1} ذخیره خواهد شد.\n\nچگونه می‌خواهید ادامه دهید؟",
        'save_all': "ذخیره همه {0}",
        'save_single': "ذخیره {0}",
        'save_customize': "تنظیم {0}",
        'save_discard': "دور ریختن این {0}",
        'save_continue': "ادامه ویرایش",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " رفتن به صفحه {0}",
        'context_rotate': " چرخاندن صفحه {0}",
        'context_delete': " حذف صفحه {0}",
        'context_export': " خروجی صفحه {0}",
        'context_mark_as': " علامت‌گذاری صفحه به عنوان...",
        'context_mark_empty': " صفحه خالی",
        'context_unmark_empty': " دیگر خالی نیست",
        'context_mark_export': " علامت‌گذاری برای خروجی",
        'context_unmark_export': " لغو علامت خروجی",
        'context_batch_actions': " اقدامات گروهی",
        'context_batch_delete_empty': " حذف همه {0} صفحه خالی",
        'context_batch_export_single': " همه {0} صفحه (یک فایل)",
        'context_batch_export_split': " همه {0} صفحه (جداگانه)",
        'context_drag_start': " شروع کشیدن و رها کردن",
        'context_drag_stop': " پایان کشیدن و رها کردن",
        'context_insert': " درج",
        'context_insert_pages': " درج صفحات",
        'context_zoom': "بزرگنمایی",
        'discard_mixed': "دور ریختن همه {0} {1} و {2} {3}",
        'save_mixed': "ذخیره {0} {1} و {2} {3}",
        'discard_texts': "دور ریختن همه {0} متن",
        'discard_text_single': "دور ریختن ۱ متن",
        'save_texts': "ذخیره {0} متن",
        'save_text_single': "ذخیره ۱ متن",
        'discard_crosses': "دور ریختن همه {0} ضربدر",
        'discard_cross_single': "دور ریختن ۱ ضربدر",
        'save_crosses': "ذخیره {0} ضربدر",
        'save_cross_single': "ذخیره ۱ ضربدر",
        'discard_signatures': "دور ریختن همه {0} امضا",
        'save_signature_single': "ذخیره ۱ امضا",
        'save_signatures': "ذخیره {0} امضا",
        'discard_images': "دور ریختن همه {0} تصویر",
        'save_image_single': "ذخیره ۱ تصویر",
        'save_images': "ذخیره {0} تصویر",
        'discard_forms': "دور ریختن همه {0} شکل",
        'save_form_single': "ذخیره ۱ شکل",
        'save_forms': "ذخیره {0} شکل",
        'cross_discard': "دور ریختن این ضربدر",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 اطلاعات خروجی / ورودی",
        'export_what': "📋 چه چیزی خروجی می‌شود؟",
        'export_general': "تنظیمات عمومی",
        'export_general_items': "• خروجی صدا (روشن/خاموش، سرعت)\n• حالت تاریک/روشن\n• تنظیمات پشتیبان\n• تنظیمات OCR",
        'export_image_form': "تنظیمات تصویر و اشکال",
        'export_image_form_items': "• تنظیمات تصویر (نسبت تصویر، اندازه پیش‌فرض)\n• تنظیمات اشکال (ضخامت خط، رنگ‌ها)\n• تنظیمات امضا (مسیرها، اندازه‌ها، مهر زمان)",
        'export_passwords': "پایگاه داده رمز عبور",
        'export_passwords_items': "• تمام رمزهای عبور PDF ذخیره شده\n• قابل انتخاب رمزگذاری شده یا رمزگشایی شده",
        'export_master': "تنظیمات رمز عبور اصلی",
        'export_master_items': "• هش رمز عبور اصلی\n• تنظیمات برای امضاها/بلوک‌های متنی",
        'export_signatures': "امضاها و بلوک‌های متنی",
        'export_signatures_items': "• تمام فایل‌های تصویر (امضاها)\n• تمام بلوک‌های متنی با قالب‌بندی\n• نشانه‌های خصوصی/عمومی",
        'export_import_warning': "⚠️ نکات مهم",
        'export_import_note': "• در هنگام ورود، همه تنظیمات فعلی بازنویسی می‌شوند\n• راه‌اندازی مجدد برنامه ضروری است\n• امضاها/بلوک‌های متنی موجود جایگزین می‌شوند",
        'export_master_note': "• اگر رمز عبور اصلی تنظیم شده باشد، می‌توانید انتخاب کنید:\n  - رمزگشایی شده (رمزهای عبور به صورت متن ساده)\n  - رمزگذاری شده (فقط با رمز اصلی قابل خواندن)",
        'export_security': "• فایل ZIP خروجی حاوی داده‌های حساس است\n• لطفاً آن را به طور امن نگهداری کنید (مثلاً درایو USB رمزگذاری شده)\n• در صورت گم شدن فایل: رمزهای عبور غیرقابل بازیابی",
        'export_format': "📁 فرمت خروجی",
        'export_format_desc': "تنظیمات در یک فایل ZIP ذخیره می‌شوند:",
        'export_filename': "PDFDarkView_Tanẓimāt_YYYYMMDD_HHMMSS.zip",
        'export_success': "تنظیمات با موفقیت خروجی داده شد",
        'export_failed': "خروجی ناموفق",
        'export_import_question': "آیا می‌خواهید برنامه را اکنون مجدداً راه‌اندازی کنید؟",
        'export_password_question': "رمز عبور اصلی تنظیم شده است.\n\nآیا می‌خواهید رمزهای عبور را به صورت رمزگشایی شده خروجی دهید؟\n(در غیر این صورت به صورت رمزگذاری شده خروجی داده می‌شوند)",
        'export_decrypt': "خروجی رمزگشایی شده",
        'export_encrypt': "خروجی رمزگذاری شده",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " اطلاعات",
        'info_title': "درباره PDF دارک ویو",
        'info_version': "نسخه",
        'info_author': "توسعه یافته توسط تورالف شولتز (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "درباره",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> یک نمایشگر PDF قابل دسترس است که به طور ویژه برای افراد دارای اختلال بینایی توسعه یافته است.</p>

            <p><strong>ویژگی‌های اصلی:</strong></p>
            <ul>
                <li>رابط کاربری با کنتراست بالا و قابل تنظیم</li>
                <li>کنترل کامل با صفحه کلید</li>
                <li>خروجی صوتی یکپارچه</li>
                <li>OCR برای اسناد اسکن شده</li>
                <li>ابزارهای ویرایش جامع</li>
            </ul>

            <p>بیش از 50 زبان پشتیبانی می‌شود – تا PDFها برای همه قابل دسترس باشند.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "ویژگی‌ها",
        'info_features_intro': "PDF Dark View امکانات زیر را به شما ارائه می‌دهد:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>نمایش و ناوبری</strong> – حالت تاریک/روشن، ورق زدن صفحات، بزرگنمایی، پرش به صفحه</li>
            <li><strong>OCR (تشخیص متن)</strong> – قابل جستجو و کپی کردن اسناد اسکن شده</li>
            <li><strong>ویرایش</strong> – درج متن، ضربدر، امضا، تصاویر و اشکال</li>
            <li><strong>مدیریت صفحات</strong> – حذف، استخراج، درج، جابجایی با کشیدن و رها کردن</li>
            <li><strong>خروجی</strong> – به Word، Pages یا به عنوان متن</li>
            <li><strong>امنیت</strong> – محافظت و مدیریت با رمز عبور</li>
            <li><strong>دسترسی‌پذیری</strong> – خروجی صوتی، کنترل با صفحه کلید، کنتراست بالا</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "عملکرد",
        'info_accessibility': "♿ دسترسی‌پذیری – کنترل کامل با صفحه کلید",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 عمومی</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> باز کردن PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> جستجو</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> تغییر حالت تاریک/روشن</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> چاپ</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> خروج</div>

        <div class="shortcut-cat">📖 ناوبری</div>
        <div class="shortcut-row"><kbd>کلیدهای جهت‌نما</kbd> ورق زدن صفحه به صفحه</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> رفتن به صفحه</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> صفحه اول</div>
        <div class="shortcut-row"><kbd>Ende</kbd> صفحه آخر</div>

        <div class="shortcut-cat">✏️ ویرایش</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> درج متن</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> حذف صفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> استخراج صفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> درج صفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> جابجایی صفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> چرخش صفحه</div>

        <div class="shortcut-cat">🖼️ جابجایی عناصر</div>
        <div class="shortcut-row"><kbd>کلیدهای جهت‌نما</kbd> جابجایی متن/تصویر/امضا</div>
        <div class="shortcut-row"><kbd>Ctrl+کلیدهای جهت‌نما</kbd> گام‌های بزرگتر</div>
        <div class="shortcut-row"><kbd>Enter</kbd> ذخیره</div>
        <div class="shortcut-row"><kbd>ESC</kbd> لغو</div>

        <div class="shortcut-cat">🗣️ خروجی صوتی</div>
        <div class="shortcut-row"><kbd>F2</kbd> روشن/خاموش کردن خروجی صوتی</div>
        """,
        'info_contextmenu': "📌 مهم: همه عملکردها از طریق منوی زمینه (دکمه راست ماوس) نیز قابل دسترسی هستند!",
        'info_accessibility_hint': "💡 نکته: خروجی صوتی (F2) جهت‌یابی را آسان‌تر می‌کند و بازخوردی درباره منوها و دیالوگ‌ها ارائه می‌دهد.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "مجوز & نشان",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 نشان</strong><br>
        اطلاعات مطابق با § 5 TMG:<br>
        تورالف شولتز<br>
        Schusterstraße 3, 65582 Diez, آلمان<br>
        ایمیل: binhdiez64@gmail.com<br>
        مسئول محتوا: تورالف شولتز (BinhDiez)<br><br>

        <strong>⚠️ سلب مسئولیت</strong><br>
        نرم‌افزار با نهایت دقت توسعه یافته است. هیچ تضمینی برای صحت، کامل بودن و عملکرد ارائه نمی‌شود. استفاده بر عهده خود کاربر است.<br><br>

        <strong>📄 مجوز MIT (استفاده خصوصی)</strong><br>
        کپی‌رایت (c) 2026 تورالف شولتز (BinhDiez)<br>
        مجاز: استفاده رایگان، تغییرات خصوصی، کپی‌های شخصی.<br>
        غیرمجاز: فروش، استفاده تجاری، حذف اطلاعیه‌های کپی‌رایت.<br><br>

        <strong>🔧 اجزای شخص ثالث</strong><br>
        این نرم‌افزار حاوی اجزایی تحت مجوزهای GPL، AGPL، Apache 2.0، BSD و MIT است.<br>
        هنگام توزیع مجدد، باید شرایط مجوز مربوطه رعایت شود.<br><br>

        <strong>🌐 متن‌باز</strong><br>
        کد منبع در دسترس است و می‌توان آن را مطابق با شرایط مجوز مربوطه مشاهده، تغییر و توزیع کرد.<br><br>

        © 2026 تورالف شولتز (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "قدردانی‌ها",
        'info_credits': "تشکر از جامعه متن‌باز",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – پردازش PDF</li>
            <li><strong>PyQt5</strong> – رابط گرافیکی</li>
            <li><strong>Tesseract OCR</strong> – تشخیص متن</li>
            <li><strong>OCRmyPDF</strong> – یکپارچه‌سازی OCR</li>
            <li><strong>python-docx</strong> – خروجی به Word</li>
            <li><strong>qtawesome</strong> – آیکون‌ها</li>
            <li><strong>DeepSeek</strong> – پشتیبانی در ترجمه‌ها (50+ زبان)</li>
            <li><strong>همه کاربران</strong> – برای بازخورد ارزشمند</li>
            <li><strong>جامعه متن‌باز</strong> – برای کتابخانه‌های عالی</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "زبان‌ها",
        'info_languages_header': "🌍 پشتیبانی از زبان",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View در حال حاضر از <strong>۶۲ زبان</strong> پشتیبانی می‌کند – تا نرم‌افزار بتواند در سراسر جهان به‌صورت قابل دسترس استفاده شود.</p>

            <p><strong>📖 لیست کامل زبان‌ها (وضعیت: مارس ۲۰۲۶):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 آفریکانس</li>
                    <li>🇦🇱 آلبانیایی (Shqip)</li>
                    <li>🇩🇿 عربی (العربية)</li>
                    <li>🇮🇩 بالیایی (Basa Bali)</li>
                    <li>🇧🇩 بنگالی (বাংলা)</li>
                    <li>🇲🇲 برمه‌ای (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 بوسنیایی (Bosanski)</li>
                    <li>🇧🇬 بلغاری (Български)</li>
                    <li>🇨🇳 چینی (中文)</li>
                    <li>🇩🇰 دانمارکی (Dansk)</li>
                    <li>🇩🇪 آلمانی (Deutsch)</li>
                    <li>🇬🇧 انگلیسی (English)</li>
                    <li>🇪🇪 استونیایی (Eesti)</li>
                    <li>🇫🇮 فنلاندی (Suomi)</li>
                    <li>🇫🇷 فرانسوی (Français)</li>
                    <li>🇬🇷 یونانی (Ελληνικά)</li>
                    <li>🇮🇱 عبری (עברית)</li>
                    <li>🇮🇳 هندی (हिन्दी)</li>
                    <li>🇭🇷 کرواتی (Hrvatski)</li>
                    <li>🇭🇺 مجارستانی (Magyar)</li>
                    <li>🇮🇩 اندونزیایی (Bahasa Indonesia)</li>
                    <li>🇮🇪 ایرلندی (Gaeilge)</li>
                    <li>🇮🇸 ایسلندی (Íslenska)</li>
                    <li>🇮🇹 ایتالیایی (Italiano)</li>
                    <li>🇯🇵 ژاپنی (日本語)</li>
                    <li>🇰🇭 خمر (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 کرهای (한국어)</li>
                    <li>🇱🇦 لائوسی (ພາສາລາວ)</li>
                    <li>🇱🇻 لتونیایی (Latviešu)</li>
                    <li>🇱🇹 لیتوانیایی (Lietuvių)</li>
                    <li>🇱🇺 لوکزامبورگی (Lëtzebuergesch)</li>
                    <li>🇲🇾 مالایی (Bahasa Melayu)</li>
                    <li>🇮🇳 ماراتی (मराठी)</li>
                    <li>🇲🇳 مغولی (Монгол)</li>
                    <li>🇳🇵 نپالی (नेपाली)</li>
                    <li>🇳🇱 هلندی (Nederlands)</li>
                    <li>🇳🇴 نروژی (Norsk)</li>
                    <li>🇦🇫 پشتو (پښتو)</li>
                    <li>🇮🇷 فارسی (فارسی)</li>
                    <li>🇵🇱 لهستانی (Polski)</li>
                    <li>🇵🇹 پرتغالی (Português)</li>
                    <li>🇮🇳 پنجابی (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 رومانیایی (Română)</li>
                    <li>🇷🇺 روسی (Русский)</li>
                    <li>🇸🇪 سوئدی (Svenska)</li>
                    <li>🇷🇸 صربی (Српски)</li>
                    <li>🇸🇰 اسلواکی (Slovenčina)</li>
                    <li>🇸🇮 اسلوونیایی (Slovenščina)</li>
                    <li>🇪🇸 اسپانیایی (Español)</li>
                    <li>🇹🇿 سواحیلی (Kiswahili)</li>
                    <li>🇵🇭 تاگالوگ (Filipino)</li>
                    <li>🇮🇳 تامیل (தமிழ்)</li>
                    <li>🇮🇳 تلوگو (తెలుగు)</li>
                    <li>🇹🇭 تایلندی (ไทย)</li>
                    <li>🇨🇿 چکی (Čeština)</li>
                    <li>🇹🇷 ترکی (Türkçe)</li>
                    <li>🇺🇦 اوکراینی (Українська)</li>
                    <li>🇵🇰 اردو (اردو)</li>
                    <li>🇻🇳 ویتنامی (Tiếng Việt)</li>
                    <li>🇸🇳 ولوف (Wolof)</li>
                    <li>🇺🇸 ییدیش (ייִדיש)</li>
                    <li>🇿🇦 زولو (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 افزودن زبان‌های خود:</strong><br>
                زبانی را می‌خواهید که هنوز گنجانده نشده است؟ فقط فایل دیکشنری خود (<code>sprache_xx.py</code>) را در کنار برنامه قرار دهید – نرم‌افزار آن را به طور خودکار تشخیص می‌دهد. اگر به ترجمه خاصی علاقه‌مند هستید، لطفاً با من تماس بگیرید.
            </div>

            <p><strong>🙏 تشکر ویژه:</strong> از DeepSeek برای پشتیبانی در ترجمه همه دیکشنری‌ها به ۶۲ زبان.</p>

            <p>📧 تماس برای ترجمه: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "خطا",
        'error_occurred': "خطایی رخ داد",
        'error_pdf_load': "خطا در بارگذاری PDF",
        'error_pdf_save': "خطا در ذخیره PDF",
        'error_ocr': "خطا در تشخیص متن",
        'error_no_pdf': "هیچ PDF بارگذاری نشده",
        'error_page_not_found': "صفحه یافت نشد",
        'error_invalid_range': "محدوده صفحه نامعتبر",
        'error_file_not_found': "فایل یافت نشد",
        'error_permission': "عدم دسترسی",
        'error_unknown': "خطای ناشناخته",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "موفق",
        'success_operation': "عملیات با موفقیت انجام شد",
        'success_saved': "با موفقیت ذخیره شد",
        'success_exported': "با موفقیت خروجی داده شد",
        'success_imported': "با موفقیت ورودی داده شد",
        'success_deleted': "با موفقیت حذف شد",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "تأیید",
        'confirm_yes': "بله",
        'confirm_no': "خیر",
        'confirm_ok': "تأیید",
        'confirm_cancel': "لغو",
        'confirm_delete': "حذف",
        'confirm_overwrite': "جایگزینی",
        'confirm_continue': "ادامه",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "در حال بارگذاری PDF...",
        'progress_saving': "در حال ذخیره PDF...",
        'progress_exporting': "در حال خروجی PDF...",
        'progress_processing': "در حال پردازش...",
        'progress_wait': "لطفاً صبر کنید...",
        'progress_preparing': "در حال آماده‌سازی...",
        'progress_finalizing': "در حال نهایی‌سازی...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "سفید",
        'color_black': "سیاه",
        'color_red': "قرمز",
        'color_green': "سبز",
        'color_blue': "آبی",
        'color_yellow': "زرد",
        'color_magenta': "ارغوانی",
        'color_cyan': "فیروزه‌ای",
        'color_orange': "نارنجی",
        'color_gray': "خاکستری",
        'color_custom': "انتخاب رنگ",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&فایل",
        'menu_edit': "&ویرایش",
        'menu_view': "&نمایش",
        'menu_tools': "&ابزارها",
        'menu_settings': "&تنظیمات",
        'menu_help': "&راهنما",
        'menu_language': "🌐 زبان",
        'menu_guides': "&راهنماها",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&باز کردن",
        'file_save_as': "&ذخیره به عنوان...",
        'file_protect': "&محافظت از سند...",
        'file_export': "&خروجی",
        'file_export_pages': "خروجی به Pages",
        'file_export_word': "خروجی به DOCX",
        'file_export_text': "خروجی به TXT",
        'file_print_now': "&چاپ فوری",
        'file_print': "&چاپ",
        'file_close': "&بستن",
        'file_quit': "&خروج",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&جستجو",
        'edit_ocr': " انجام OCR",
        'edit_rotate': "&چرخاندن صفحه",
        'edit_rotate_all': "&چرخاندن همه صفحات",
        'edit_delete_pages': "&حذف صفحات",
        'edit_extract_pages': "&استخراج صفحات",
        'edit_insert_pages': "&درج صفحات",
        'edit_move_pages': "&جابجایی صفحات",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " درج متن و ضربدر",
        'text_insert': " درج متن",
        'cross_insert': " درج ضربدر",
        'text_customize': " تنظیم این متن",
        'cross_customize': " تنظیم این ضربدر",
        'cross_customize_all': " تنظیم همه ضربدرها",
        'text_discard': " دور ریختن این متن/ضربدر",
        'text_discard_all': " دور ریختن همه متون و ضربدرها",
        'text_save_all': " ذخیره همه متون و ضربدرها",
        'text_guide': " ورودی متن / بلوک‌های متنی - راهنما",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " درج امضا",
        'signature_settings_menu': " تنظیمات...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " درج تصویر",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " درج اشکال",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&نمایش پنجره متن",
        'view_zoom': "&بزرگنمایی",
        'view_zoom_page': "&عرض صفحه (پیش‌فرض)",
        'view_zoom_two': "&دو صفحه",
        'view_zoom_overview': "&نمای کلی (چند صفحه)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&ابزارهای کمکی",
        'settings_voice': "خروجی صوتی",
        'settings_voice_tooltip': "خروجی صوتی صفحه‌خوان را با اطلاعات اضافی تکمیل می‌کند",
        'settings_signature': "&تنظیمات امضا",
        'settings_password': "&مدیریت رمز عبور",
        'settings_backup': "ایجاد پشتیبان قبل از تغییرات",
        'settings_export_import': "&خروجی / ورودی تنظیمات",
        'settings_export': "&خروجی همه تنظیمات...",
        'settings_import': "&ورودی همه تنظیمات...",
        'settings_export_info': "&چه چیزی خروجی می‌شود؟",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "روشن",
        'voice_off': "خاموش",
        'voice_toggle': "خروجی صوتی {0}",
        'voice_speed': "سرعت روی {0} درصد",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "ابزار یافت نشد:\n{0}\n\nBASE_DIR: {1}\nلطفاً مطمئن شوید که ابزارهای PDF در دایرکتوری {1} نصب شده‌اند.",
        'tool_started': "{0} شروع شد",
        'tool_start_failed': "شروع نشد",
        'process_error_failed_to_start': "فرآیند نمی‌تواند شروع شود. آیا فایل وجود دارد؟",
        'process_error_crashed': "فرآیند هنگام شروع از کار افتاد.",
        'process_error_timeout': "مهلت فرآیند به پایان رسید.",
        'process_error_write': "خطای نوشتن در فرآیند.",
        'process_error_read': "خطای خواندن از فرآیند.",
        'process_error_unknown': "خطای ناشناخته فرآیند",
        'process_command': "دستور",
        'process_normal_exit': "به طور عادی پایان یافت",
        'process_crashed': "از کار افتاد",
        'process_nonzero_exit': "{0} با کد خطای {1} پایان یافت",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "در حال لغو...",
        'move_cancelling': "در حال لغو جابجایی",
        'opening_pdf': "در حال باز کردن PDF...",
        'loading_document': "در حال بارگذاری سند...",
        'pdf_opened': "PDF باز شد",
        'pages_found_moving': "{0} صفحه یافت شد، {1} برای جابجایی",
        'creating_backup': "در حال ایجاد پشتیبان...",
        'backup_description': "در حال پشتیبان‌گیری از فایل اصلی...",
        'backup_saved_as': "پشتیبان‌گیری شده به عنوان: {0}",
        'error_format': "خطا: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView توسط BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "جستجو بازنشانی شد",
        'page_header_simple': "=== صفحه {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "مدیریت رمز عبور – راهنما",
        'password_guide_voice': "راهنمای مدیریت رمز عبور. لطفاً نکات را بخوانید.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 مدیریت رمز عبور – راهنمای جامع</strong></p>

        <p><strong>1. محافظت با رمز عبور برای PDF</strong></p>
        <ul>
        <li>هنگام باز کردن یک PDF محافظت شده با رمز عبور، گفتگویی ظاهر می‌شود که می‌توانید رمز عبور را وارد کنید.</li>
        <li>می‌توانید رمز عبور را به صورت رمزگذاری شده ذخیره کنید تا هر بار نیازی به وارد کردن مجدد آن نباشد (کادر "ذخیره رمز عبور").</li>
        <li>با دکمه "حذف رمز عبور" می‌توانید یک کپی رمزگشایی شده از PDF ایجاد کرده و رمز عبور را از پایگاه داده حذف کنید.</li>
        </ul>

        <p><strong>2. رمز عبور اصلی</strong></p>
        <ul>
        <li>رمز عبور اصلی از دسترسی به تمام رمزهای عبور PDF ذخیره شده محافظت می‌کند.</li>
        <li><strong>تنظیم:</strong> به "تنظیمات → مدیریت رمز عبور → تنظیمات رمز اصلی" بروید و روی "تنظیم رمز عبور اصلی" کلیک کنید. یک رمز عبور قوی انتخاب کنید (حداقل ۸ کاراکتر).</li>
        <li><strong>تغییر:</strong> پس از احراز هویت موفق، می‌توانید رمز عبور اصلی را تغییر دهید.</li>
        <li><strong>حذف:</strong> اگر رمز عبور اصلی را حذف کنید، تمام رمزهای عبور ذخیره شده برای همیشه پاک می‌شوند. می‌توانید قبل از آن یک نسخه پشتیبان خروجی بگیرید.</li>
        <li>یک بار در هر نشست باید با رمز عبور اصلی احراز هویت کنید تا به عملکردهای محافظت شده (مثلاً نمایش رمزهای عبور) دسترسی پیدا کنید.</li>
        </ul>

        <p><strong>3. مدیریت رمز عبور (لیست)</strong></p>
        <ul>
        <li>در "تنظیمات → مدیریت رمز عبور" یک جدول از تمام PDFهای ذخیره شده با رمزهای عبور رمزگذاری شده آنها باز می‌شود.</li>
        <li><strong>بدون رمز عبور اصلی:</strong> فقط می‌توانید ورودی‌ها را حذف کنید – رمزهای عبور پنهان می‌مانند.</li>
        <li><strong>با رمز عبور اصلی (احراز هویت شده):</strong> می‌توانید رمزهای عبور را مشاهده، کپی، خروجی و حذف کنید.</li>
        <li><strong>خروجی:</strong> یک قالب (JSON، CSV، TXT) انتخاب کرده و لیست را ذخیره کنید. اگر رمز اصلی تنظیم شده باشد، می‌توانید تصمیم بگیرید که رمزهای عبور به صورت متن ساده یا همچنان رمزگذاری شده خروجی شوند.</li>
        <li><strong>ورودی:</strong> یک فایل ZIP که قبلاً خروجی گرفته شده با تمام تنظیمات (شامل رمزهای عبور) می‌تواند از طریق "تنظیمات → خروجی/ورودی تنظیمات" دوباره خوانده شود. توجه: داده‌های موجود بازنویسی می‌شوند!</li>
        </ul>

        <p><strong>4. تولیدکننده رمز عبور</strong></p>
        <ul>
        <li>در گفتگوی رمز عبور (مثلاً هنگام محافظت از PDF)، یک دکمه تاس 🎲 در سمت راست فیلد ورودی پیدا می‌کنید.</li>
        <li>روی آن کلیک کنید تا تولیدکننده رمز عبور باز شود. می‌توانید طول، مجموعه کاراکترها (حروف بزرگ، حروف کوچک، اعداد، نمادهای خاص) و جداکننده را برای خوانایی بهتر تنظیم کنید.</li>
        <li>رمز عبور تولید شده می‌تواند مستقیماً استفاده شود و در صورت نیاز کپی شود.</li>
        </ul>

        <p><strong>5. نکات امنیتی مهم</strong></p>
        <ul>
        <li>رمزهای عبور ذخیره شده با رمزگذاری AES-256 ذخیره می‌شوند. کلید از رمز عبور اصلی شما (در صورت تنظیم) یا از یک مقدار ثابت (بدون رمز اصلی) مشتق می‌شود.</li>
        <li>بدون رمز عبور اصلی، رمزهای عبور اگرچه رمزگذاری شده‌اند، اما کلید در برنامه ذخیره شده است – یک مهاجم با دسترسی به فایل‌های شما می‌تواند آنها را رمزگشایی کند. بنابراین، ما قویاً استفاده از رمز عبور اصلی را توصیه می‌کنیم.</li>
        <li>پایگاه داده رمز عبور در دایرکتوری `Daten/passwords.json` قرار دارد. به طور منظم پشتیبان تهیه کنید، به خصوص قبل از حذف رمز عبور اصلی.</li>
        <li>در صورت گم شدن رمز عبور اصلی، تمام رمزهای عبور ذخیره شده برای همیشه از بین می‌روند.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "حالت وارونگی",
        'invert_mode_classic': "کلاسیک (وارونگی همه رنگ‌ها)",
        'invert_mode_smart': "هوشمند (وارونگی فقط روشنایی)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "آستانه مقیاس خاکستری",
        'gray_threshold_10': "10% (سخت)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (پیش‌فرض)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (نرم)",
        'threshold_changed': "آستانه روی {0}% تنظیم شد",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "آستانه مقیاس خاکستری – توضیح",
        'threshold_guide_text': "آستانه مقیاس خاکستری تعیین می‌کند کدام پیکسل‌ها در حالت تاریک هوشمند به عنوان 'خاکستری' در نظر گرفته شده و وارونه می‌شوند.\n\n"
                                "• مقدار پایین (10%) فقط سایه‌های تقریباً کامل خاکستری را وارونه می‌کند – عناصر رنگی کاملاً حفظ می‌شوند.\n"
                                "• مقدار بالا (50%) همچنین پیکسل‌های کمی رنگی را وارونه می‌کند – این کار کنتراست را افزایش می‌دهد، اما می‌تواند رنگ‌ها را تحریف کند.\n\n"
                                "مقدار بهینه به سند بستگی دارد. برای اسناد متنی خالص، 30–40% اغلب ایده‌آل است، برای گرافیک‌های رنگی بیشتر 10–20%.\n\n"
                                "شما می‌توانید مقدار را در هر زمان از طریق منوی 'تنظیمات' تنظیم کنید – PDF بلافاصله دوباره بارگذاری می‌شود.\n\n"
                                "توجه:\n* عکس‌ها و تصاویر فقط در حالت روشن می‌توانند به درستی نمایش داده شوند!\n* تنظیمات وارونگی فقط زمانی نمایش داده می‌شوند که حالت تاریک فعال باشد.",
        'threshold_guide_voice': "آستانه مقیاس خاکستری تعیین می‌کند که حالت تاریک هوشمند چقدر مداخله می‌کند. مقدار پایین رنگ‌ها را حفظ می‌کند، مقدار بالا کنتراست را افزایش می‌دهد.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "در حال باز کردن PDF...",
        'progress_loading_document': "در حال بارگذاری سند...",
        'progress_pdf_opened': "PDF باز شد",
        'progress_creating_backup': "در حال ایجاد پشتیبان...",
        'progress_backup_description': "در حال ایمن‌سازی فایل اصلی...",
        'progress_backup_created': "پشتیبان ایجاد شد",
        'progress_backup_saved_as': "ذخیره شده به عنوان: {0}",
        'progress_analyzing_start': "شروع تحلیل...",
        'progress_searching_empty': "جستجوی صفحات خالی...",
        'progress_page_empty': "صفحه {0} خالی است",
        'progress_page_keep': "نگهداری صفحه {0}",
        'progress_analysis_complete': "تحلیل کامل شد",
        'progress_empty_found': "{0} صفحه خالی یافت شد",
        'progress_current_page': "صفحه فعلی",
        'progress_mark_delete': "در حال علامت‌گذاری برای حذف",
        'progress_range_selected': "محدوده صفحات {0}-{1}",
        'progress_deleting_pages': "در حال حذف {0} صفحه",
        'progress_creating_new_pdf': "در حال ایجاد PDF جدید...",
        'progress_transferring_pages': "در حال انتقال صفحات",
        'progress_keeping_page': "صفحه {0} نگهداری می‌شود ({1}/{2})",
        'progress_saving_pdf': "در حال ذخیره PDF...",
        'progress_optimizing': "در حال بهینه‌سازی اندازه فایل...",
        'progress_finalizing': "در حال نهایی‌سازی...",
        'progress_new_size': "اندازه جدید: {0:.2f} MB",
        'progress_cancelling': "در حال لغو...",
        'progress_cancel_message': "{0} در حال لغو شدن است",
        'progress_pages_found_moving': "{0} صفحه یافت شد، {1} برای جابجایی",

        # OCR-Fortschritt
        'ocr_status_analyzing': "در حال تحلیل PDF...",
        'ocr_status_optimizing': "بهینه‌سازی تصویر در حال انجام...",
        'ocr_status_recognizing': "تشخیص متن در حال انجام...",
        'ocr_status_embedding': "درج متن...",
        'ocr_status_finalizing': "نهایی‌سازی PDF...",

        # PDF-Laden
        'progress_preparing': "در حال آماده‌سازی...",
        'progress_loading': "در حال بارگذاری PDF...",

        # Seitenoperationen
        'progress_deleting_title': "در حال حذف صفحات...",
        'progress_moving_title': "در حال جابجایی صفحات...",
        'pages_found': "صفحات یافت شد",
        'progress_creating_new_order': "در حال ایجاد ترتیب جدید...",
        'progress_sorting_pages': "در حال مرتب‌سازی صفحات...",
        'progress_moving_to_begin': "جابجایی {0} صفحه به ابتدا",
        'progress_transferring_count': "انتقال {0} صفحه",
        'progress_transferring_before_target': "انتقال صفحات قبل از هدف",
        'progress_moving_pages': "جابجایی {0} صفحه",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_پشتیبان_",
        'filename_protected_suffix': "_محافظت_شده_",
        'filename_copy_suffix': "_نسخه",
        'filename_page_single': "_صفحه_",
        'filename_page_range': "_صفحات_",
        'filename_export_page': "_صفحه_{0:03}",
        'filename_export_range': "_صفحات_{0}-{1}",
        'filename_export_multiple': "_صفحات_{0}",
        'filename_with_text': "_با_متن",
        'filename_with_signature': "_با_امضا",
        'filename_with_image': "_با_تصویر",
        'filename_with_forms': "_با_اشکال",
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
        'view_toggle_navbar': "نمایش نوار دکمه‌ها",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "امکان حذف تمام صفحات وجود ندارد",
		'pages_cannot_delete_last_page': 'آخرین صفحه قابل حذف نیست!',
		'pages_cannot_delete_all_pages': 'حداقل یک صفحه باید در سند باقی بماند!',
		'delete_pages_confirm': 'آیا از حذف {0} صفحه اطمینان دارید؟',
		'delete_pages_confirm_voice': 'آیا از حذف {0} صفحه اطمینان دارید؟',
		'pages_deleted': '{0} صفحه با موفقیت حذف شدند.',
		'warning': 'هشدار',
		'error': 'خطا',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "هیچ فرمی انتخاب نشده است",
        'form_customized': "فرم سفارشی‌سازی شد",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "انتخاب",
        'btn_use': "استفاده",
        'master_password_for_spasswords': "برای ذخیره و استفاده از رمزهای عبور، ابتدا باید رمز عبور اصلی تنظیم شود.\n\nآیا می‌خواهید رمز عبور اصلی را اکنون تنظیم کنید؟",
        'open_saved_dialog_title': "باز کردن فایل ذخیره شده",
        'open_saved_question': "آیا می‌خواهید فایل ذخیره شده را اکنون باز کنید؟",
        'password': "رمز عبور",
        'password_manager_master_required': "مدیریت رمز عبور فقط در صورت تنظیم رمز عبور اصلی در دسترس است.\n\nآیا می‌خواهید رمز عبور اصلی را اکنون تنظیم کنید؟",
        'password_master_required_for_select': "برای مشاهده و انتخاب رمزهای عبور ذخیره شده، ابتدا باید با رمز عبور اصلی خود احراز هویت کنید.\n\nآیا می‌خواهید اکنون احراز هویت کنید؟",
        'password_not_available': "رمز عبور انتخاب شده در دسترس نیست یا نمی‌توان آن را رمزگشایی کرد.",
        'password_options_title': "گزینه‌های رمز عبور",
        'password_save_choice_change': "تنظیم رمز عبور جدید",
        'password_save_choice_keep': "استفاده از رمز عبور موجود",
        'password_save_choice_none': "ذخیره بدون رمزگذاری",
        'password_save_hint': "برای ذخیره امن رمزهای عبور، ابتدا یک رمز عبور اصلی تنظیم کنید.",
        'password_save_master_required': "ذخیره رمز عبور (فقط با رمز عبور اصلی امکان‌پذیر است)",
        'password_save_question': "PDF فعلی با رمز عبور محافظت می‌شود. آیا می‌خواهید از رمز عبور موجود استفاده کنید، رمز جدید تنظیم کنید یا بدون رمزگذاری ذخیره کنید؟",
        'password_select': "انتخاب رمز عبور",
        'password_select_none': "هیچ رمز عبوری انتخاب نشده است.\n\nلطفاً یک رمز عبور از لیست انتخاب کنید.",
        'password_select_one': "لطفاً دقیقاً یک رمز عبور انتخاب کنید.\n\nشما چندین رمز عبور را علامت گذاری کرده‌اید.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_پشتیبان",
        'filename_insert_suffix': "_با_درج",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_صفحات_حذف_شده",
        'filename_pages_moved': "_صفحات_جابه‌جا_شده",
        'filename_rotated_all_suffix': "_همه_صفحات_چرخانده_شدند",
        'filename_rotated_suffix': "_صفحه_چرخانده_شد",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "پیکربندی نام فایل‌ها هنگام تغییر PDF",
        'filename_keep_suffixes': "نگهداری پسوندهای قبلی (مثلاً _با_متن)",
        'filename_keep_suffixes_false': "جایگزینی",
        'filename_keep_suffixes_true': "نگهداری",
        'filename_preview_label': "پیش‌نمایش نام فایل:",
        'filename_preview_overwrite_hint': "پیش‌نمایش در دسترس نیست – فایل اصلی بازنویسی خواهد شد.",
        'filename_separator': "جداکننده بین کلمات",
        'filename_separator_none': "بدون جداکننده",
        'filename_separator_space': "فاصله ( )",
        'filename_separator_underscore': "زیرخط (_)",
        'filename_settings_saved': "تنظیمات نام فایل ذخیره شد",
        'filename_settings_title': "قالب‌بندی نام فایل و پشتیبان",
        'filename_timestamp_position': "موقعیت زمان‌مهر",
        'filename_timestamp_position_after': "پس از نام پایه",
        'filename_timestamp_position_before': "در ابتدا",
        'filename_timestamp_position_end': "در انتها",
        'filename_use_timestamp': "استفاده از زمان‌مهر",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>رفتار هنگام تغییرات:</b><ul><li>حذف و درج صفحات</li><li>درج متن، امضا، تصویر و اشکال</li><li>OCR</li></ul></html>",
        'backup_section': "پشتیبان برای عملیات صفحات (حذف، جابه‌جایی)",
        'behavior_info': "توجه: در 'بازنویسی اصلی' زمان‌مهرها و پسوندها نادیده گرفته می‌شوند – فایل نام خود را حفظ می‌کند.",
        'behavior_new_file': "همیشه فایل جدید ایجاد کن (با زمان‌مهر و پسوند)",
        'behavior_overwrite': "بازنویسی اصلی (بدون فایل جدید)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "همه صفحات چرخانده شدند.\n\nاصلی بدون تغییر باقی ماند.\nفایل جدید: {0}",
        'all_pages_rotated_voice': "همه صفحات چرخانده شدند، فایل جدید ایجاد شد.",
        'empty_pages_deleted_new_file': "{0} صفحه خالی حذف شد.\n\nاصلی بدون تغییر باقی ماند.\nفایل جدید: {1}",
        'empty_pages_deleted_voice': "{0} صفحه خالی حذف شد، فایل جدید ایجاد شد.",
        'ocr_keep_original': "نگهداری اصلی (بعداً به صورت دستی باز کن)",
        'ocr_new_file_question': "PDF جدید قابل جستجو در این مکان ذخیره شد:\n{0}\n\nآیا می‌خواهید آن را اکنون باز کنید؟",
        'ocr_open_new': "باز کردن فایل OCR جدید",
        'ocr_original_kept': "فایل اصلی باز باقی می‌ماند. فایل OCR ذخیره شده است.",
        'page_deleted_new_file': "صفحه {0} حذف شد.\n\nاصلی بدون تغییر باقی ماند.\nفایل جدید: {1}",
        'page_deleted_voice': "صفحه {0} حذف شد، فایل جدید ایجاد شد.",
        'page_rotated_new_file': "صفحه {0} چرخانده شد.\n\nاصلی بدون تغییر باقی ماند.\nفایل جدید: {1}",
        'page_rotated_voice': "صفحه {0} چرخانده شد، فایل جدید ایجاد شد.",
        'pages_deleted_new_file': "{0} صفحه حذف شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nفایل جدید: {1}",
        'pages_deleted_new_file_voice': "{0} صفحه حذف شد، فایل جدید ایجاد شد.",
        'pages_inserted_new_file': "{0} صفحه درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nفایل جدید: {1}",
        'pages_inserted_new_file_ask': "{0} صفحه درج شد.\n\nاصلی بدون تغییر باقی ماند.\nفایل جدید: {1}\n\nآیا می‌خواهید آن را اکنون باز کنید؟",
        'pages_inserted_voice_new': "{0} صفحه درج شد، فایل جدید ایجاد شد.",
        'pages_moved_new_file': "{0} صفحه جابه‌جا شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nفایل جدید: {1}",
        'pages_moved_new_file_voice': "{0} صفحه جابه‌جا شد، فایل جدید ایجاد شد.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "دیگر نشان نده",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 تنظیمات پشتیبان</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ پشتیبان فعال</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">در تمام تغییراتی که اصلی را بازنویسی می‌کنند</strong> (متن، امضا، تصویر، شکل، OCR، چرخاندن، درج، حذف/جابه‌جایی صفحات) <strong>به طور خودکار یک پشتیبان با زمان‌مهر</strong> قبل از اعمال تغییر ایجاد می‌شود.</p>
                <p style="margin: 5px 0 5px 20px;">• پشتیبان در کنار فایل اصلی قرار دارد (مثلاً <code>Dokument_پشتیبان_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• اگر علاوه بر این گزینه <strong>„بازنویسی اصلی“</strong> را فعال کرده باشید، نیز یک پشتیبان ایجاد می‌شود.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 پشتیبان غیرفعال</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>هیچ پشتیبانی ایجاد نمی‌شود</strong> – نه هنگام بازنویسی و نه هنگام عملیات صفحات.</p>
                <p style="margin: 5px 0 5px 20px;">• فایل اصلی ممکن است هنگام بازنویسی به طور غیرقابل برگشتی از بین برود.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">فقط برای کاربران با تجربه توصیه می‌شود!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>نکته:</strong> تنظیمات پشتیبان مستقل از گزینه „بازنویسی اصلی“ است. می‌توانید هر دو را ترکیب کنید.<br>
                می‌توانید این پیام را به طور دائمی پنهان کنید.
            </div>
        </div>
        """,
        'backup_info_title': "رفتار پشتیبان",
        'backup_info_voice': "اطلاعیه در مورد رفتار پشتیبان در عملیات صفحات. پشتیبان فعال اصلی را بازنویسی می‌کند، پشتیبان غیرفعال فایل جدید ایجاد می‌کند.",
        'show_backup_info': "اطلاعات در مورد تنظیمات پشتیبان",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "دیگر نشان نده",
        'overwrite_enable_backup': "فعال کردن پشتیبان (توصیه می‌شود)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ بازنویسی اصلی</p>
            <p>اگر این گزینه را فعال کنید، تغییرات (متن، امضا، تصویر، شکل، OCR، چرخاندن، درج) <strong>مستقیماً در اصلی ذخیره می‌شوند</strong> – <strong>هیچ فایل جدیدی ایجاد نمی‌شود</strong>.</p>
            <p>• نام فایل بدون تغییر باقی می‌ماند.<br>
            • زمان‌مهرها و پسوندها نادیده گرفته می‌شوند.<br>
            • <strong>بدون پشتیبان، اصلی ممکن است به طور غیرقابل برگشتی از بین برود.</strong></p>
            <p style="color: #FFD700;">توصیه: برای دریافت پشتیبان‌های خودکار، گزینه پشتیبان را نیز فعال کنید.</p>
        </div>
        """,
        'overwrite_info_title': "بازنویسی اصلی",
        'overwrite_info_voice': "هشدار: بازنویسی اصلی – بدون فایل جدید. پشتیبان توصیه می‌شود.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} صفحه درج شد.\n\nفایل اصلی بازنویسی شد.\nیک پشتیبان ایجاد شد.",
        'pages_inserted_overwrite_no_backup': "{0} صفحه درج شد.\n\nفایل اصلی بازنویسی شد.\nهیچ پشتیبانی ایجاد نشد.",
        'texts_saved_overwrite_with_backup': "تغییرات در اصلی ذخیره شد.\n\nیک پشتیبان ایجاد شد.",
        'texts_saved_overwrite_no_backup': "تغییرات در اصلی ذخیره شد.\n\nهیچ پشتیبانی ایجاد نشد.",
        'texts_crosses_saved_new_file': "{0} {1} و {2} {3} درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nیک فایل جدید ایجاد شد.\n\nPDF جدید در حال بارگذاری است...",
        'texts_saved_new_file': "{0} {1} درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nیک فایل جدید ایجاد شد.\n\nPDF جدید در حال بارگذاری است...",
        'crosses_saved_new_file': "{0} {1} درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nیک فایل جدید ایجاد شد.\n\nPDF جدید در حال بارگذاری است...",
        'elements_saved_new_file': "{0} عنصر درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nیک فایل جدید ایجاد شد.\n\nPDF جدید در حال بارگذاری است...",
        'signatures_saved_overwrite_with_backup': "امضا(ها) در اصلی ذخیره شد.\n\nیک پشتیبان ایجاد شد.",
        'signatures_saved_overwrite_no_backup': "امضا(ها) در اصلی ذخیره شد.\n\nهیچ پشتیبانی ایجاد نشد.",
        'images_saved_overwrite_with_backup': "تصویر(ها) در اصلی ذخیره شد.\n\nیک پشتیبان ایجاد شد.",
        'images_saved_overwrite_no_backup': "تصویر(ها) در اصلی ذخیره شد.\n\nهیچ پشتیبانی ایجاد نشد.",
        'forms_saved_overwrite_with_backup': "شکل(ها) در اصلی ذخیره شد.\n\nیک پشتیبان ایجاد شد.",
        'forms_saved_overwrite_no_backup': "شکل(ها) در اصلی ذخیره شد.\n\nهیچ پشتیبانی ایجاد نشد.",
        'signatures_saved_new_file': "{0} امضا درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nیک فایل جدید ایجاد شد.\n\nPDF جدید در حال بارگذاری است...",
        'images_saved_new_file': "{0} تصویر درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nیک فایل جدید ایجاد شد.\n\nPDF جدید در حال بارگذاری است...",
        'forms_saved_new_file': "{0} شکل درج شد.\n\nفایل اصلی بدون تغییر باقی ماند.\nیک فایل جدید ایجاد شد.\n\nPDF جدید در حال بارگذاری است...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "هشدار: این PDF شامل صفحات چرخانده شده است. موقعیت‌یابی ممکن است متفاوت باشد.",
        'page_rotated_warning_title': "صفحه چرخانده شده تشخیص داده شد",
        'page_rotated_warning_message': "صفحه فعلی {0} به میزان {1}° چرخانده شده است.\n\nدرج عناصر در صفحات چرخانده شده پشتیبانی نمی‌شود.\n\nآیا می‌خواهید صفحه را اکنون به حالت عمودی بچرخانید؟",
        'page_rotated_warning_voice': "هشدار: صفحه چرخانده شده است. لطفاً ابتدا آن را بچرخانید.",
        'paste_on_rotated_page_simple_warning': "درج در صفحه {0} امکان‌پذیر نیست!\n\nاین صفحه به میزان {1}° چرخانده شده است.\n\nلطفاً ابتدا صفحه را به 0° بچرخانید (منو: ویرایش → تراز کردن صفحه).\n\nهشدار:\nعنصر قبلاً کپی شده در صورتی که قبل از چرخاندن صفحه ذخیره نکنید، از بین خواهد رفت.",
        'paste_on_rotated_page_voice': "درج لغو شد. صفحه چرخانده شده است. لطفاً ابتدا صفحه را تراز کنید.",
        'page_rotated_cancel': "لغو",
        'page_rotated_rotate_until_upright': "چرخاندن مکرر صفحه (تا زمانی که عمودی شود)",
        'page_rotated_now_upright': "صفحه اکنون عمودی است. اکنون می‌توانید درج کنید.",
        'page_rotated_still_not_upright': "صفحه را نمی‌توان به حالت عمودی چرخاند. لطفاً به صورت دستی اصلاح کنید.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "راهنما: تصحیح صفحات چرخانده شده",
        'help_rotated_pages_voice': "راهنما برای تصحیح صفحات چرخانده شده باز می‌شود.",
        'btn_help': "راهنما",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 مشکل: صفحه چرخانده شده – درج به درستی کار نمی‌کند</p>

            <p>اگر درج متون، امضاها یا اشکال در یک صفحه چرخانده شده به درستی کار نمی‌کند، می‌توانید صفحه را با یک ویرایشگر PDF خارجی تصحیح کنید.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ راه‌حل با ابزار خارجی (مثلاً macOS Preview)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>خروجی گرفتن از صفحه</strong><br>
                &nbsp;&nbsp;در منو روی <strong>فایل → خروجی گرفتن به عنوان صفحات</strong> کلیک کنید یا از روش دیگری برای ذخیره صفحه مورد نظر به عنوان یک PDF استفاده کنید.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>باز کردن صفحه در برنامه خارجی</strong><br>
                &nbsp;&nbsp;PDF خروجی گرفته شده را در یک ویرایشگر PDF باز کنید (مثلاً <strong>macOS Preview</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>چرخاندن صفحه</strong><br>
                &nbsp;&nbsp;صفحه را بچرخانید تا عمودی شود (در Preview: <strong>ابزارها → چرخاندن</strong> یا <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>ذخیره</strong><br>
                &nbsp;&nbsp;صفحه تصحیح شده را ذخیره کنید (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>درج مجدد صفحه در سند اصلی</strong><br>
                &nbsp;&nbsp;به PDFDarkView بازگردید و صفحه تصحیح شده را در موقعیت مورد نظر درج کنید:<br>
                &nbsp;&nbsp;<strong>ویرایش → درج صفحات</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 جایگزین: چرخاندن صفحه در اصلی</p>
                <p style="margin: 5px 0 5px 20px;">• از عملکرد چرخاندن داخلی استفاده کنید (<strong>ویرایش → چرخاندن صفحه</strong>) برای تصحیح تدریجی صفحه.<br>
                • پس از هر بار چرخاندن می‌توانید بررسی کنید که آیا درج اکنون کار می‌کند.<br>
                • این اغلب راه‌حل سریع‌تری است – ابتدا آن را امتحان کنید!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>نکته:</strong> اگر اغلب با صفحات چرخانده شده مواجه می‌شوید، می‌توانید هشدار را در گفتگوی درج به طور دائمی پنهان کنید.<br>
                موقعیت‌یابی ممکن است سپس متفاوت باشد – فقط در صورتی از این گزینه استفاده کنید که عواقب آن را می‌دانید.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "تراز کردن صفحات",
        'menu_rotate_normalize_tooltip': "چرخاندن صفحه یا بازنشانی به 0°",
        'normalize_current_page': "آوردن صفحه فعلی به حالت عمودی (تنظیم به 0°)",
        'normalize_all_pages': "آوردن همه صفحات به حالت عمودی (تنظیم به 0°)",
        'page_normalized': "صفحه {0} به حالت عمودی تنظیم شد.",
        'all_pages_normalized': "همه صفحات به حالت عمودی تنظیم شدند.",
        'page_already_upright': "صفحه {0} در حال حاضر عمودی است.",
        'all_pages_already_upright': "همه صفحات در حال حاضر عمودی هستند.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF شامل هیچ متن قابل جستجویی نیست.</p><p>آیا می‌خواهید برای خروجی به {0} OCR انجام دهید؟</p>",
        'export_ocr_voice': "PDF شامل متنی نیست. برای خروجی به {0} به OCR نیاز است.",
        'export_no_ocr_possible': "خروجی بدون OCR امکان‌پذیر نیست. لطفاً از طریق منو OCR را انجام دهید.",
        'ocr_failed_export_not_possible': "OCR ناموفق بود. خروجی قابل انجام نیست.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF در Preview باز می‌شود. لطفاً فرآیند چاپ را در آنجا شروع کنید.",
        'print_preview_manual': "PDF باز شد. لطفاً دستور چاپ را به صورت دستی اجرا کنید (مثلاً Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "ادغام PDFها",
        'merge_pdfs': "ادغام PDFها",
        'merge_progress_title': "در حال ادغام PDFها...",
        'merge_pdfs_list': "PDFها به ترتیب (بکشید و رها کنید برای مرتب‌سازی)",
        'merge_add_pdf': "افزودن PDF",
        'merge_remove': "حذف",
        'merge_move_up': "به بالا",
        'merge_move_down': "به پایین",
        'merge_pdfs_info': "💡 نکته: می‌توانید ترتیب را با کشیدن و رها کردن تغییر دهید",
        'merge_no_pdfs': "هیچ PDFای انتخاب نشده است. روی 'افزودن PDF' کلیک کنید.",
        'merge_info': "{0} PDF انتخاب شد (تقریباً {1} صفحه)",
        'merge_open_file': "باز کردن فایل",
        'merge_merge': "ادغام",
        'merge_error': "خطا در هنگام ادغام",
        'merge_min_two_pdfs_error': "لطفاً حداقل دو فایل PDF برای ادغام انتخاب کنید.",
        'merge_select_pdfs': "انتخاب PDFها برای ادغام",
        'merge_error_file': "خطا در هنگام پردازش",
        'merge_cancelled': "ادغام لغو شد",
        'merge_preparing': "در حال آماده‌سازی...",
        'merge_processing': "پردازش PDF {0} از {1}",
        'merge_saving': "ذخیره PDF ادغام شده...",
        'merge_complete': "انجام شد!",
        'merge_success_title': "ادغام موفقیت‌آمیز بود",
        'merge_success_voice': "{0} PDF با موفقیت ادغام شدند.",
        'merge_success_message': "{0} PDF با موفقیت ادغام شدند.\n\nسند جدید اکنون {1} صفحه دارد.\n\nفایل جدید:\n{2}\n\nمکان ذخیره:\n{3}\n{2}\n\nآیا می‌خواهید این PDF را باز کنید؟",
        'replace_file_title': "آیا فایل جایگزین شود؟",
        'replace_file_message': "در حال حاضر یک PDF باز است. آیا می‌خواهید آن را با فایل جدید جایگزین کنید؟",
        'btn_yes': "بله",
        'btn_no': "خیر",
        'filename_merge_suffix': "ادغام‌شده",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "در حال باز کردن {0}...",
        'progress_merge_reading': "در حال خواندن {0}...",
        'progress_merge_adding': "در حال افزودن {0} صفحه...",
        'progress_merge_optimizing': "در حال بهینه‌سازی PDF...",
        'progress_merge_writing': "در حال نوشتن PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "بستن PDF",
        'action_close_window': "بستن پنجره",
        'action_open_new_pdf': "باز کردن یک PDF جدید",
        'action_quit_app': "خروج از برنامه",
        'changes_saved': "تغییرات ذخیره شد.",
        'file_close_title': "بستن فایل PDF",
        'save_before_action': "آیا تغییرات قبل از {0} ذخیره شوند؟ بله یا خیر؟",
        'save_before_action_voice': "آیا تغییرات قبل از {0} ذخیره شوند؟ بله یا خیر؟",
        'save_before_close_question': "آیا تغییرات قبل از بستن ذخیره شوند؟ بله یا خیر؟",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>PDF قابل جستجو ایجاد شد:\n\n{0}\n\n<b>در صورت نیاز دوباره تلاش کنید",
        "ocr_rotate_title": "تراز کردن صفحات قبل از OCR",
        "ocr_rotate_question": "PDF شامل صفحات چرخیده است.\nآیا می‌خواهید همه صفحات را قبل از OCR در 0° تراز کنید؟\nاین کار تشخیص متن را به طور قابل توجهی بهبود می‌بخشد.",
        "ocr_rotate_yes": "بله، تراز کن",
        "ocr_rotate_no": "نه، OCR را مستقیماً شروع کن",
        "ocr_rotate_voice": "PDF شامل صفحات چرخیده است. آیا همه صفحات قبل از OCR تراز شوند؟",
        "ocr_not_performed_message": "متنی وجود ندارد. لطفاً OCR را انجام دهید (منوی \"ویرایش\" → \"انجام OCR\" یا کلید Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "تنظیمات OCR",
        "ocr_language_btn": "انتخاب زبان OCR",
        "ocr_language": "زبان(های) OCR",
        "ocr_language_current": "زبان فعلی:",
        "ocr_param_info": "اطلاعات در مورد پارامتر",

        "ocr_force_ocr_label": "اجبار OCR",
        "ocr_deskew_label": "تصحيح کجی",
        "ocr_clean_label": "پاکسازی تصویر",
        "ocr_oversample_label": "رزولوشن (DPI)",
        "ocr_pagesegmode_label": "تقسیم صفحه",
        "ocr_oem_label": "حالت موتور OCR",
        "ocr_optimize_label": "فشرده‌سازی PDF",
        "ocr_jobs_label": "فرآیندهای موازی",
        "ocr_verbose_label": "جزئیات لاگ",

        "ocr_force_ocr_tooltip": "اجبار OCR در هر صفحه، حتی اگر متن از قبل وجود داشته باشد",
        "ocr_deskew_tooltip": "تراز خودکار اسکن‌های کج",
        "ocr_clean_tooltip": "حذف نویز و مصنوعات از تصویر",
        "ocr_oversample_tooltip": "بزرگنمایی تصویر قبل از OCR به این DPI",
        "ocr_pagesegmode_tooltip": "تعیین می‌کند که صفحه چگونه به نواحی متنی تقسیم شود",
        "ocr_oem_tooltip": "موتور OCR Tesseract را انتخاب می‌کند",
        "ocr_optimize_tooltip": "سطح فشرده‌سازی PDF خروجی",
        "ocr_jobs_tooltip": "تعداد فرآیندهای موازی OCR",
        "ocr_verbose_tooltip": "سطح جزئیات خروجی لاگ",
        "ocr_settings_explain_btn": "توضیح",

        "ocr_force_ocr_explain": "تشخیص متن را در <b>هر</b> صفحه اجباری می‌کند، حتی اگر از قبل حاوی متن باشد.\n\nتوصیه: <b>فعال</b> برای PDFهای اسکن شده، <b>غیرفعال</b> برای PDFهای اصلی با متن از قبل موجود.",

        "ocr_deskew_explain": "اسکن‌های کمی کج را تصحیح می‌کند (تا حدود 5 درجه).\n\nتوصیه: <b>فعال</b> برای اسناد اسکن شده، <b>غیرفعال</b> اگر صفحات از قبل کاملاً صاف هستند.",

        "ocr_clean_explain": "نویز، نقطه‌ها و مصنوعات کوچک را از تصویر حذف می‌کند.\n<b>مهم:</b> برای متون عربی، تایلندی یا ویتنامی با علائم دیاکریتیک (نقطه‌های بالا/پایین حروف) این گزینه باید <b>غیرفعال</b> شود، در غیر این صورت ممکن است نویسه‌های مهم از دست بروند.",

        "ocr_oversample_explain": "تصویر را <b>قبل از</b> تشخیص متن به DPI مشخص شده بزرگنمایی می‌کند.<br><br>• <b>72-150 DPI:</b> بسیار سریع، اما نرخ تشخیص پایین<br>• <b>200-300 DPI:</b> محدوده بهینه (پیش‌فرض: 300)<br>• <b>400+ DPI:</b> تشخیص تقریباً بهتر نیست، اما فایل‌ها به طور قابل توجهی بزرگتر می‌شوند<br><br>توصیه: 300 DPI برای خطوط پیچیده (عربی، چینی، ژاپنی)، 200 DPI برای زبان‌های غربی.",

        "ocr_pagesegmode_explain": "تعیین می‌کند که Tesseract چگونه صفحه را به نواحی متنی تقسیم می‌کند.\n\n• <b>3 - خودکار (پیش‌فرض):</b> خوب برای چیدمان‌های مختلط\n• <b>4 - ستون واحد:</b> برای متون تک‌ستونی\n• <b>5 - بلوک عمودی:</b> برای خطوط عمودی (ژاپنی، چینی)\n• <b>6 - بلوک متنی یکنواخت:</b> بهینه برای متن روان بدون ستون\n• <b>11 - تصویر خام:</b> برای اسکن‌های ضعیف / دستخط\n\nتوصیه: <b>6</b> برای اسناد متنی ساده، <b>3</b> برای چیدمان‌های پیچیده.",

        "ocr_oem_explain": "موتور OCR Tesseract را انتخاب می‌کند.\n\n• <b>0 - Legacy:</b> موتور قدیمی (سریع، اما کمتر دقیق)\n• <b>1 - LSTM:</b> موتور عصبی (کندتر، اما دقیق‌تر)\n• <b>2 - Legacy + LSTM:</b> هر دو نتیجه را ترکیب می‌کند\n• <b>3 - پیش‌فرض (LSTM ترجیح داده می‌شود):</b> بهترین انتخاب برای بیشتر موارد\n\nتوصیه: <b>3</b> برای حداکثر دقت تشخیص.",

        "ocr_optimize_explain": "PDF خروجی را فشرده می‌کند.\n\n• <b>0:</b> بدون بهینه‌سازی (سریعترین پردازش)\n• <b>1:</b> بهینه‌سازی سبک (سازش خوب)\n• <b>2:</b> بهینه‌سازی متوسط\n• <b>3:</b> بهینه‌سازی قوی (کوچکترین فایل، اما کندتر)\n\nتوصیه: <b>1</b> برای استفاده روزانه.",

        "ocr_jobs_explain": "تعداد فرآیندهای موازی برای OCR.\n\n• <b>1:</b> کند، اما کمترین مصرف حافظه\n• <b>4-8:</b> بهینه برای پردازنده‌های چند هسته‌ای مدرن\n• <b>12+:</b> پردازش تقریباً سریعتر با مصرف حافظه بالا\n\nتوصیه: تعداد هسته‌های CPU (مثلاً <b>4</b> در سیستم‌های 4 هسته‌ای).",

        "ocr_verbose_explain": "سطح جزئیات خروجی لاگ در کنسول.\n\n• <b>0:</b> بدون خروجی\n• <b>1:</b> پیشرفت و پیام‌های وضعیت\n• <b>2:</b> خروجی دقیق\n• <b>3:</b> خروجی کامل اشکال‌زدایی (بسیار حجیم)\n\nتوصیه: <b>1</b> برای عملکرد عادی.",

        "ocr_reset_title": "تنظیمات بازنشانی شد",
        "ocr_reset_message": "تمام تنظیمات OCR به مقادیر پیش‌فرض بازنشانی شدند.",
        "info_tooltip": "اطلاعات بیشتر در مورد این پارامتر",
        "ocr_reset_defaults": "بازنشانی به پیش‌فرض",

        "ocr_psm_0": "خودکار (موتور Legacy)",
        "ocr_psm_1": "تشخیص خودکار ستون",
        "ocr_psm_3": "خودکار (پیش‌فرض)",
        "ocr_psm_4": "ستون واحد",
        "ocr_psm_5": "بلوک عمودی",
        "ocr_psm_6": "بلوک متنی یکنواخت",
        "ocr_psm_7": "خط متن واحد",
        "ocr_psm_8": "کلمه واحد",
        "ocr_psm_11": "تصویر خام (بدون تحلیل چیدمان)",

        "ocr_oem_0": "موتور Legacy (سریع)",
        "ocr_oem_1": "موتور LSTM (عصبی، دقیق)",
        "ocr_oem_2": "Legacy + LSTM ترکیبی",
        "ocr_oem_3": "پیش‌فرض (LSTM ترجیح داده می‌شود)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "زبان(های) OCR...",
        "ocr_language_title": "انتخاب زبان(های) OCR",
        "ocr_language_instruction": "زبان(های) را برای تشخیص متن (OCR) انتخاب کنید.\nتوجه: چندین زبان به هزینه عملکرد و دقت تمام می‌شود!\nبهترین نتایج را زمانی به دست می‌آورید که فقط یک زبان را انتخاب کنید.",
        "ocr_language_predefined": "ترکیبات از پیش تعریف شده",
        "ocr_language_custom": "سفارشی...",
        "ocr_language_selected": "زبان‌های OCR انتخاب شده",
        "ocr_language_changed": "زبان OCR به {0} تغییر یافت",
        "ocr_language_auto_detect": "زبان‌های موجود به طور خودکار شناسایی می‌شوند.",
        "ocr_language_none_found": "داده‌های زبان Tesseract یافت نشد! لطفاً بسته‌های زبانی را نصب کنید (مثلاً 'tesseract-ocr-deu'، 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "انتخاب زبان سفارشی",
        "ocr_language_available": "زبان‌های موجود (نصب شده):",
        "ocr_language_select_hint": "یک یا چند زبان را انتخاب کنید:",
        "ocr_language_confirm": "اعمال",
        "ocr_language_reset": "بازنشانی به پیش‌فرض (deu+eng+vie)",
        "ocr_language_priorities": "زبان‌های توصیه شده (پیش‌نصب):",

        "select_all_languages": "انتخاب همه",
        "clear_all_languages": "پاک کردن انتخاب",
        "install_language_packs": "نصب بسته‌های زبانی گمشده...",
        "install_hint": "💡 نکته: همه زبان‌ها روی سیستم شما نصب نیستند. از طریق این دکمه برای نصب راهنمایی دریافت خواهید کرد.",
        "ocr_language_install_title": "نصب بسته‌های زبانی Tesseract",

        "ocr_missing_languages": "بسته‌های زبانی OCR گمشده",
        "ocr_missing_languages_message": "زبان‌های انتخاب شده زیر روی سیستم شما نصب نیستند:\n\n{0}\n\nلطفاً بسته‌های زبانی گمشده را نصب کنید (راهنما را در 'راهنمای نصب' ببینید).\n\nآیا می‌خواهید現在 راهنمای نصب را باز کنید؟",
        "ocr_missing_languages_voice": "بسته‌های زبانی گمشده. لطفاً زبان‌های گمشده را نصب کنید.",
        "ocr_install_help_now": "باز کردن راهنما",
        "ocr_continue_anyway": "به هر حال تلاش کن",
        "ocr_language_error_title": "خطای زبان OCR",
        "ocr_language_error_message": "خطا در هنگام تشخیص متن: {0}\n\nلطفاً تنظیمات زبان OCR خود را بررسی کنید (تنظیمات → زبان OCR).",
        "ocr_install_help_button": "راهنمای نصب",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 نصب بسته‌های زبانی Tesseract</p>

        <p>برای اینکه OCR به زبان خاصی کار کند، داده‌های زبانی مربوطه باید روی سیستم شما نصب شوند. دستورالعمل‌های سیستم عامل خود را دنبال کنید:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li><strong>ترمینال</strong> را باز کنید (Finder → Programs → Utilities → Terminal).</li>
        <li>همه زبان‌های موجود را با دستور زیر نصب کنید:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (این کار ممکن است چند دقیقه طول بکشد.)</li>
        <li>یا فقط زبان‌های جداگانه (مثلاً ویتنامی):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        در نسخه‌های فعلی Homebrew، ممکن است <code>*.traineddata</code> نیاز به دانلود دستی داشته باشد (به زیر مراجعه کنید).</li>
        <li>پس از نصب: این کادر محاوره‌ای را ببندید و انتخاب زبان OCR را دوباره باز کنید – زبان‌های جدید به طور خودکار ظاهر می‌شوند.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>یک ترمینال باز کنید (Ctrl+Alt+T).</li>
        <li>زبان مورد نظر را نصب کنید، مثلاً برای ویتنامی:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        کدهای زبان مهم: <code>deu</code> (آلمانی)، <code>eng</code> (انگلیسی)، <code>vie</code> (ویتنامی)، <code>spa</code> (اسپانیایی)، <code>fra</code> (فرانسوی)، <code>ita</code> (ایتالیایی)، <code>nld</code> (هلندی)، <code>fin</code> (فنلاندی)، <code>swe</code> (سوئدی)، <code>nor</code> (نروژی).</li>
        <li>نمایش همه بسته‌های موجود:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (دستی)</p>
        <ol>
        <li>فایل‌های <code>*.traineddata</code> مورد نظر را از این آدرس دانلود کنید:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (مثلاً <code>vie.traineddata</code> برای ویتنامی).</li>
        <li>فایل‌ها را در پوشه زبان Tesseract کپی کنید، معمولاً:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (با توجه به نصب فردی تنظیم کنید.)</li>
        <li>برنامه را مجدداً راه‌اندازی کنید (یا انتخاب زبان OCR را دوباره باز کنید).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 جایگزین برای همه سیستم‌ها</p>
        <ul>
        <li><strong>OCRmyPDF</strong> و <strong>Tesseract</strong> را با یک مدیر بسته به انتخاب خود نصب کنید. بیشتر نصب‌ها از قبل دارای برخی زبان‌های استاندارد (انگلیسی، آلمانی، فرانسوی) هستند.</li>
        <li>زبان‌های گمشده را می‌توان در هر زمان نصب کرد – انتخاب زبان OCR فقط زبان‌های واقعاً موجود را فهرست می‌کند.</li>
        </ul>

        <hr>
        <p><b>✅ پس از نصب:</b> نیازی به راه‌اندازی مجدد برنامه نیست – زبان‌های تازه اضافه شده بلافاصله در لیست ظاهر می‌شوند.</p>
        <p><b>📖 راهنمای کدهای زبان:</b> یک لیست کامل در <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">مستندات Tesseract</a> موجود است.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "فونت‌های Noto Sans",
        "info_noto_font_voice": "راهنمای نصب فونت‌های Noto Sans",
        "btn_info_noto_font_install": "اطلاعات فونت",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word; direction: ltr; text-align: left;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ نحوه نصب فونت‌های رایگان Noto از گوگل</h2>

        <p><strong>فونت‌های Noto</strong> یک خانواده فونت منبع باز از گوگل هستند. هدف آنها دیدن <em>"بدون توفو"</em> (یعنی بدون جعبه‌های خالی □) و نمایش صحیح هر نویسه از استاندارد یونیکد است. آنها افزودنی ایده‌آل برای برنامه‌هایی هستند که نیاز به نمایش متون به زبان‌های مختلف دارند.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 نصب در macOS</h3>

        <p><strong>روش 1: با Homebrew (برای کاربران پیشرفته)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>روش 2: از طریق "Font Book" (توصیه می‌شود)</strong></p>

        <ol>
        <li>بسته فونت رسمی را دانلود کنید:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>فایل ZIP را استخراج کنید</li>
        <li>فایل‌ها را در <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code> کپی کنید</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 نصب در Windows (10 & 11)</h3>

        <p><strong>روش 1: Microsoft Store (توصیه می‌شود)</strong><br>
        جستجو کنید "Google Noto Fonts" یا "Noto Sans" و روی <strong>نصب</strong> کلیک کنید.</p>

        <p><strong>روش 2: نصب دستی</strong></p>

        <ol>
        <li>دانلود:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>استخراج ZIP</li>
        <li>فایل‌های .ttf / .otf را انتخاب کنید</li>
        <li>کلیک راست → <strong>نصب</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        یا<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\نام\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 نصب در Linux</h3>

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

        <p>تأیید:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "مدیریت نشانک‌ها",
        "bookmark_add": "افزودن نشانک",
        "bookmark_add_tooltip": "ذخیره صفحه فعلی به عنوان نشانک",
        "bookmark_remove": "حذف نشانک",
        "bookmark_remove_tooltip": "حذف نشانک علامت‌گذاری شده",
        "bookmark_remove_all": "حذف همه",
        "bookmark_remove_all_tooltip": "حذف تمام نشانک‌های این PDF",
        "bookmark_jump": "پرش به نشانک",
        "bookmark_jump_tooltip": "پرش به صفحه انتخاب شده",
        "bookmark_name": "نام",
        "bookmark_page": "صفحه",
        "bookmark_no_bookmarks": "هیچ نشانکی وجود ندارد.\nبرای ذخیره صفحه فعلی به عنوان نشانک روی 'افزودن' کلیک کنید.",
        "bookmark_added": "نشانک برای صفحه {0} اضافه شد: {1}",
        "bookmark_removed": "نشانک حذف شد: {0}",
        "bookmark_all_removed": "همه نشانک‌ها حذف شدند.",
        "bookmark_name_default": "صفحه {0}",
        "bookmark_name_prompt": "نام برای نشانک:\n(متن طولانی به 50 کاراکتر کوتاه می‌شود)",
        "bookmark_name_prompt_title": "نام نشانک",
        "bookmark_confirm_remove_all": "آیا مطمئن هستید که می‌خواهید همه {0} نشانک را حذف کنید؟",
        "menu_bookmarks": "نشانک‌ها",
        "bookmark_manage": "مدیریت نشانک‌ها",
        "bookmark_next": "نشانک بعدی",
        "bookmark_prev": "نشانک قبلی",
        "bookmark_page_display": "صفحه {0}",
        "bookmark_exists": "نشانکی برای این صفحه با این نام از قبل وجود دارد.",
        "bookmark_select_first": "لطفاً ابتدا یک نشانک انتخاب کنید.",
        "bookmark_confirm_remove": "آیا مطمئن هستید که می‌خواهید نشانک 'صفحه {0}: {1}' را حذف کنید؟",
        "bookmark_jumped_to": "پرش به نشانک '{0}' در صفحه {1}.",
        "bookmark_jumped_to_voice": "نشانک {0}، صفحه {1}",
        "btn_close": "بستن",

        "bookmark_list": "نشانک‌های شما",
        "bookmark_rename": "تغییر نام نشانک",
        "bookmark_rename_tooltip": "تغییر نام نشانک انتخاب شده",
        "bookmark_rename_title": "تغییر نام نشانک",
        "bookmark_rename_prompt": "نام جدید برای نشانک در صفحه {0}:\n(حداکثر 50 کاراکتر)",
        "bookmark_renamed": "نشانک '{0}' به '{1}' تغییر نام یافت.",
        "bookmark_item_tooltip": "صفحه {0}: {1}\nبرای پرش دوبار کلیک کنید",
        "bookmark_name_exists_question": "نشانکی با نام '{0}' از قبل در این صفحه وجود دارد.\nبه هر حال تغییر نام بدهیم؟",

        "context_bookmarks": "نشانک‌ها",
        "context_bookmark_add_here": "افزودن نشانک برای این صفحه",
        "context_bookmarks_existing": "نشانک‌های موجود:",
        "context_bookmarks_jump": "پرش به نشانک:",
        "context_bookmarks_none": "هیچ نشانکی وجود ندارد",
        "context_bookmarks_clear_all": "حذف همه {0} نشانک",

        "bookmark_search_placeholder": "جستجوی نشانک‌ها... (نام یا صفحه)",
        "bookmark_search_results": "%d نشانک برای \"%s\" یافت شد",
        "bookmark_no_search_results": "هیچ نشانکی برای \"%s\" یافت نشد",
        "bookmark_no_search_results_label": "نتیجه‌ای برای \"%s\" وجود ندارد",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "ویرایش فراداده PDF",
        "metadata_title": "عنوان",
        "metadata_title_placeholder": "عنوان سند",
        "metadata_title_tooltip": "عنوان سند (در نوار عنوان نمایش داده می‌شود)",
        "metadata_author": "نویسنده",
        "metadata_author_placeholder": "نام نویسنده",
        "metadata_author_tooltip": "ایجاد کننده سند",
        "metadata_subject": "موضوع",
        "metadata_subject_placeholder": "موضوع سند",
        "metadata_subject_tooltip": "توضیح کوتاه از محتوا",
        "metadata_keywords": "کلمات کلیدی",
        "metadata_keywords_placeholder": "کلمات کلیدی، جدا شده با کاما",
        "metadata_keywords_tooltip": "کلمات کلیدی برای دسته‌بندی سند",
        "metadata_creator": "سازنده",
        "metadata_creator_placeholder": "برنامه‌ای که PDF را ایجاد کرده است",
        "metadata_creator_tooltip": "نرم‌افزاری که سند با آن ایجاد شده است",
        "metadata_producer": "تولید کننده",
        "metadata_producer_placeholder": "برنامه‌ای که PDF را تبدیل کرده است",
        "metadata_producer_tooltip": "نرم‌افزاری که PDF را تبدیل کرده است",
        "metadata_creation_date": "تاریخ ایجاد",
        "metadata_creation_date_tooltip": "تاریخ ایجاد سند",
        "metadata_mod_date": "تاریخ تغییر",
        "metadata_mod_date_tooltip": "تاریخ آخرین تغییر",
        "metadata_pdf_info": "📄 اطلاعات PDF",
        "metadata_pages": "تعداد صفحات",
        "metadata_file_size": "اندازه فایل",
        "metadata_pdf_version": "نسخه PDF",
        "metadata_encrypted": "رمزگذاری شده",
        "metadata_encrypted_yes": "بله (محافظت شده با رمز عبور)",
        "metadata_encrypted_no": "خیر",
        "metadata_reload": "📂 بارگیری مجدد از PDF",
        "metadata_reset": "رد تغییرات",
        "metadata_reloaded": "فراداده از PDF بارگیری مجدد شد.",
        "metadata_reset_done": "تمام فیلدهای فراداده بازنشانی شدند.",
        "metadata_no_file": "هیچ فایل PDF بارگیری نشده است.",
        "metadata_save_error": "خطا در ذخیره فراداده",
        "metadata_saved": "فراداده با موفقیت ذخیره شد.",
        "metadata_pdf_version_unknown": "PDF (ناشناخته)",
        "metadata_saved_message": "فراداده با موفقیت ذخیره شد.",
        "metadata_saved_voice": "فراداده ذخیره شد.",

        "metadata_custom": "🔧 فراداده سفارشی",
        "metadata_custom_placeholder": "{\n  \"فیلد_من\": \"مقدار_من\",\n  \"فیلد_دیگر\": 123\n}",
        "metadata_custom_tooltip": "فرمت JSON برای فراداده سفارشی (اختیاری)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "قالب \"{0}\" انتخاب شد - برای درج دوبار کلیک کنید",
        "text_use_template": "استفاده از بلوک متن",
        "text_type": "نوع",
        "text_search_templates": "جستجوی بلوک‌های متن...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 اطلاعات صادرات / واردات",
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

        <h3>📦 چه چیزی صادر می‌شود؟ (نمای کلی)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">تنظیمات عمومی برنامه</span></li>
            <li class="detail">• حالت تاریک/روشن</li>
            <li class="detail">• وارونگی حالت تاریک برای تصاویر</li>
            <li class="detail">• مقدار آستانه خاکستری</li>
            <li class="detail">• زبان</li>
            <li class="detail">• هندسه پنجره</li>
            <li class="detail">• حالت بزرگنمایی</li>
            <li class="detail">• ناوبری (نوار ناوبری قابل مشاهده)</li>
            <li class="detail">• خروجی صدا (روشن/خاموش)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">تنظیمات پشتیبان</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">نام‌گذاری فایل (مهر زمان، جداکننده، پسوندها)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">تنظیمات برای درج</span></li>
            <li class="detail">• امضاها</li>
            <li class="detail">• متن و بلوک‌های متنی</li>
            <li class="detail">• علامت‌ها، تصاویر و اشکال</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">تنظیمات OCR</span></li>
            <li class="detail">• زبان</li>
            <li class="detail">• اجبار OCR · حالت صفحه</li>
            <li class="detail">• پیش‌پردازش تصویر: تصحیح کجی، پاکسازی، Oversampling</li>
            <li class="detail">• تعداد کارهای موازی</li>
            <li class="detail">• حالت وارونگی</li>
            <li class="detail">• مقدار آستانه خاکستری</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">نشانک‌ها</span></li>
            <li class="detail">• همه نشانک‌ها در هر فایل PDF (صفحه، نام، زمان ایجاد)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">پایگاه داده رمزهای عبور</span></li>
            <li class="detail">• رمزهای عبور PDF ذخیره شده (اختیاری رمزگذاری شده یا متن ساده)</li>
            <li class="detail">• هش رمز عبور اصلی (اگر تنظیم شده باشد)</li>
            <li class="detail">• داده‌های تأیید</li>
        </ul>

        <h4>⚠️ یادداشت‌های مهم</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 هنگام واردات:</strong>
            <ul>
                <li><span class="warning">➜ تمام تنظیمات فعلی به طور کامل بازنویسی خواهند شد</span></li>
                <li>• راه‌اندازی مجدد برنامه الزامی است</li>
                <li>• امضاها، بلوک‌های متنی و نشانک‌های موجود جایگزین خواهند شد</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 رمز عبور اصلی و حالت صادرات:</strong>
            <ul>
                <li>• هنگامی که رمز عبور اصلی فعال است، می‌توانید انتخاب کنید:</li>
                <li>  - <span style="color: #98FB98;"><strong>رمزگشایی شده</strong></span> (رمزهای عبور به صورت متن ساده در ZIP هستند)</li>
                <li>  - <span style="color: #FFA07A;"><strong>رمزگذاری شده</strong></span> (فقط با رمز عبور اصلی در سیستم مقصد قابل خواندن هستند)</li>
                <li>• هش رمز عبور اصلی <strong>همیشه</strong> به صورت رمزگذاری شده ذخیره می‌شود</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ نکته امنیتی:</strong>
            <ul>
                <li>• فایل ZIP صادر شده حاوی داده‌های حساس است (<strong>رمزهای عبور، نشانک‌ها، امضاها</strong>)</li>
                <li>• لطفاً آن را در امنیت نگهداری کنید (مثلاً فلش USB رمزگذاری شده، مدیر رمز عبور)</li>
                <li>• اگر فایل گم شود، رمزهای عبور PDF ذخیره شده به طور غیرقابل بازیابی گم می‌شوند</li>
            </ul>
        </div>

        <h4>📁 فرمت صادرات</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            تنظیمات در یک فایل ZIP ذخیره می‌شوند:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            این ZIP شامل <code>settings.json</code> کامل (از پیکربندی شما) و همچنین فایل‌های تصویر امضای جاسازی شده و رمزهای عبور رمزگذاری شده است.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "امضاها - راهنما",
        'signature_guide_html': """
        📝 <strong>امضاها - راهنمای سریع</strong><br>
        <ul>
        <li>تنظیم رمز عبور اصلی</li>
        <li>پیکربندی امضاها در منوی <em>تنظیمات</em> (اندازه، زمان‌مهر، …)</li>
        <li>درج با <strong>کلیک راست</strong> در موقعیت دلخواه (رمز عبور اصلی یک بار در هر نشست لازم است)</li>
        <li>جابجایی امضا با ماوس یا کلیدهای جهت‌نما</li>
        <li>درج چندین امضا پشت سر هم</li>
        <li>سفارشی‌سازی هر امضا به صورت جداگانه</li>
        <li>رد امضای تکی</li>
        <li>ذخیره / رد کردن همه امضاها به یک باره</li>
        <li>به طور جایگزین، می‌توان از نوار منو نیز استفاده کرد.</li>
        </ul>
        """,
        'signature_guide_voice': "راهنمای سریع برای امضاها. رمز عبور اصلی را تنظیم کنید. امضاها را در تنظیمات پیکربندی کنید. درج با کلیک راست.",

        'image_guide_title': "درج تصاویر - راهنما",
        'image_guide_html': """
        📷 <strong>درج تصاویر در PDF - راهنمای سریع</strong><br>
        <ol>
        <li>کلیک راست در موقعیت دلخواه</li>
        <li><em>„درج تصویر“</em> → انتخاب تصویر</li>
        <li>موقعیت‌گذاری تصویر: کشیدن با ماوس</li>
        <li>تنظیم اندازه: کشیدن در گوشه‌ها/لبه‌ها</li>
        <li>حفظ نسبت ابعاد: کلید <strong>[A]</strong></li>
        <li>تنظیمات بیشتر: کلیک راست روی تصویر</li>
        </ol>
        <p><strong>نکته:</strong> در منوی زمینه می‌توانید تنظیمات را تغییر دهید.</p>
        """,
        'image_guide_voice': "راهنمای سریع برای تصاویر. کلیک راست، درج تصویر، انتخاب کنید. موقعیت‌گذاری با ماوس، تنظیم اندازه در گوشه‌ها. نسبت ابعاد با کلید A.",

        'form_guide_title': "درج اشکال - راهنما",
        'form_guide_html': """
        📐 <strong>درج اشکال در PDF - راهنمای سریع</strong><br>
        <ol>
        <li>انتخاب نوع شکل (مستطیل، بیضی، خط، پیکان)</li>
        <li>کلیک در موقعیت:
            <ul>
            <li>برای مستطیل/بیضی: یک کلیک شکل را قرار می‌دهد</li>
            <li>برای خط/پیکان: دو کلیک برای نقطه شروع و پایان</li>
            </ul>
        </li>
        <li>موقعیت‌گذاری شکل: کشیدن با ماوس</li>
        <li>تنظیم اندازه: کشیدن در گوشه‌ها/لبه‌ها</li>
        <li>ذخیره شکل: <strong>Enter</strong></li>
        <li>رد شکل: <strong>ESC</strong></li>
        <li>تنظیمات بیشتر: کلیک راست روی شکل</li>
        </ol>
        <p><strong>نکته:</strong> در منوی زمینه می‌توانید تنظیمات را تغییر دهید.</p>
        """,
        'form_guide_voice': "راهنمای سریع برای اشکال. نوع شکل را انتخاب کنید. برای مستطیل یا بیضی یک بار کلیک کنید، برای خط یا پیکان دو بار کلیک کنید. موقعیت‌گذاری با ماوس، تنظیم اندازه در گوشه‌ها. ذخیره با Enter، رد با Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "قبلی",
        "btn_next_result": "بعدی",
        "ocr_text_window": "پنجره متن OCR",
        "bookmark_existing": "نشانک‌های موجود",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "مقایسه OCR مک - ویندوز",
        'ocr_method_mac_win_title': "تفاوت‌های OCR بین مک و ویندوز",
        'ocr_method_mac_win_voice': "مک بهتر است",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – تفاوت‌های بین macOS و ویندوز</strong></p>

        <p><strong>macOS (توصیه می‌شود)</strong></p>
        <p>ابزار:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>نتیجه:</p>
        <ul>
        <li>یک PDF قابل جستجو با متن جاسازی‌شده که تا حد زیادی طرح اصلی را حفظ می‌کند.</li>
        </ul>
        <p>مزایا:</p>
        <ul>
        <li>کیفیت عالی تشخیص متن (حتی در صفحات کج).</li>
        <li>حفظ گرافیک برداری و فونت‌ها.</li>
        <li>نوار پیشرفت رابط کاربری از طریق ارزیابی زیرفرآیند.</li>
        <li>کنترل کامل بر تمام پارامترهای OCR (Deskew، Clean، Oversample، بهینه‌سازی).</li>
        <li>جستجوی متن مستقیماً در پنجره اصلی (نمایش PDF) در دسترس است.</li>
        </ul>
        <p>معایب:</p>
        <ul>
        <li>نیاز به ابزارهای سیستم اضافی دارد (ocrmypdf، Ghostscript، unpaper، pngquant – در بسته برنامه گنجانده شده است).</li>
        <li>مدیریت خطای پیچیده‌تر (بن‌بست‌ها، زمان‌های انتظار).</li>
        </ul>

        <p><strong>ویندوز (جایگزین پایدار)</strong></p>
        <p>ابزار:</p>
        <ul>
        <li>pytesseract (اتصال مستقیم به Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>نتیجه:</p>
        <ul>
        <li>یک PDF قابل جستجو که از نظر بصری معادل یک PDF تصویری است، اما از طریق متن شفاف قابل جستجو است.</li>
        </ul>
        <p>مزایا:</p>
        <ul>
        <li>در حال حاضر به نظرم نمی‌رسد.</li>
        </ul>
        <p>معایب:</p>
        <ul>
        <li>PDF اساساً یک تصویر با متن نامرئی است؛ طرح ممکن است در اسناد پیچیده (ستون‌ها، جداول) کمی انحراف داشته باشد.</li>
        <li>هیچ تصحیح خودکار کجی (--deskew) یا پاکسازی تصویر (--clean) وجود ندارد.</li>
        <li>نوار پیشرفت رابط کاربری فقط به طور تقریبی بر اساس تعداد صفحات پردازش شده به روز می‌شود.</li>
        <li>سرعت OCR کمی کندتر است (زیرا هر صفحه جداگانه پردازش می‌شود).</li>
        <li>جستجوی متن به پنجره متن OCR هدایت می‌شود.</li>
        </ul>

        <p><strong>ویژگی‌های مشترک</strong></p>
        <ul>
        <li>هر دو روش یک PDF قابل جستجو در همان دایرکتوری فایل منبع ایجاد می‌کنند.</li>
        <li>تنظیمات OCR (زبان، DPI، حالت بخش‌بندی صفحه، حالت موتور OCR) را می‌توان از طریق OCRSettingsDialog پیکربندی کرد و در هر دو پیاده‌سازی معتبر است.</li>
        </ul>

        <p><strong>توصیه:</strong></p>
        <ul>
        <li>macOS: باینری ocrmypdf بهترین نتایج را ارائه می‌دهد – یک مک بخرید و از نسخه استفاده کنید (PDFDarkView برای مک‌های دارای تراشه Apple Silicon یا Intel). نتایج OCR بهتر از ویندوز است!</li>
        <li>ویندوز: از راهکار pytesseract استفاده کنید. پایدار است و برای اکثر اسناد کیفیت کاملاً کافی ارائه می‌دهد.</li>
        </ul>

        <p><strong>نکته مهم:</strong></p>
        <ul>
        <li>هر دو نسخه به طور کامل در رابط کاربر ادغام شده‌اند – کاربر هیچ تفاوتی متوجه نمی‌شود.</li>
        <li>برنامه به طور خودکار بر اساس سیستم عامل تصمیم می‌گیرد که از کدام موتور OCR استفاده کند.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "ایجاد امضا (از اسکن)",
        "signature_create_title": "انتخاب امضای اسکن شده (PDF/تصویر)",
        "image_pdf_filter": "تصاویر و PDF",
        "signature_pdf_empty": "PDF شامل هیچ صفحه‌ای نیست.",
        "signature_created_success": "امضا با موفقیت ایجاد شد: {0}",
        "signature_create_error": "خطا در ایجاد امضا:\n{0}",
        "rembg_missing": "rembg نصب نشده است.\nلطفاً نصب کنید: pip install rembg\nخطا: {0}",
        "signature_name_title": "نام فایل برای امضا",
        "signature_name_message": "لطفاً یک نام فایل برای امضای جدید وارد کنید (به صورت PNG با پس‌زمینه شفاف ذخیره می‌شود):",
        "signature_name_label": "نام فایل:",
        "signature_name_voice": "نام فایل را برای امضا وارد کنید",
        "signature_processing": "پردازش در حال انجام...",
        "signature_creation_title": "در حال ایجاد امضا",
        "signature_overwrite_warning": "فایل '{0}' از قبل وجود دارد. بازنویسی شود؟",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"آماده‌سازی PDF برای امضا",
        "signature_prepare_instruction":"لطفاً یک PDF انتخاب کنید که در یک صفحه شامل یک امضای اسکن شده باشد.\n\nبرای تشخیص بهینه، اطمینان حاصل کنید که:\n• امضا با جوهر سیاه (خودکار یا روان‌نویس) روی کاغذ سفید نوشته شده باشد.\n• امضا در یک سوم بالایی صفحه A4 که در غیر این صورت خالی است قرار داشته باشد.\n• PDF با حداقل 300 dpi اسکن شده باشد.\n• امضا واضح و خیلی نازک نباشد.\n• هیچ الگوی پس‌زمینه مزاحم یا خطوطی وجود نداشته باشد.",
        "signature_prepare_voice":"لطفاً یک PDF با امضای اسکن شده انتخاب کنید. به کیفیت خوب و کنتراست توجه کنید.",
        "sig_thickness_label":"ضخامت خط:",
        "sig_thickness_normal":"معمولی (نازک)",
        "sig_thickness_bold":"پررنگ (توصیه می‌شود)",
        "sig_thickness_very_bold":"بسیار پررنگ",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "اضافه کردن زبان‌های رابط کاربری و OCR - راهنما",
        'language_guide_title': "اضافه کردن زبان‌های رابط کاربری و OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>رابط کاربری</h2>
        <p>فایل ترجمه مورد نظر <code>translations_xy.py</code> را از<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        دانلود کرده و در دایرکتوری زیر قرار دهید:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>مرورگر وب خود را باز کنید.</li>
        <li>به آدرس زیر بروید: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>در لبه سمت راست صفحه به دنبال "Releases" بگردید و موردی که با <strong>"latest"</strong> مشخص شده را انتخاب کنید.</li>
        <li>در صفحه انتشار بعدی، فایل <code>Source Code.zip</code> را در پایین دانلود کنید.</li>
        <li>فایل ZIP را از حالت فشرده خارج کنید.</li>
        <li>در پوشه از حالت فشرده خارج شده، تمام فایل‌های زبانی مورد نیاز خود را جستجو کرده و در دایرکتوری کپی کنید:<br/>
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
        "menu_watermark":"درج نشانه آب",
        "fullpage_text_watermark_title":"متن به عنوان نشانه آب",
        "fullpage_image_watermark_title":"تصویر به عنوان نشانه آب",
        "filename_with_watermark":"_با_نشانه_آب",
        "watermark_text":"متن:",
        "watermark_text_placeholder":"متن نشانه آب شما...",
        "watermark_font_family":"فونت:",
        "watermark_font_size":"اندازه فونت:",
        "watermark_format":"قالب‌بندی:",
        "watermark_bold":"پررنگ",
        "watermark_italic":"کج",
        "watermark_color":"رنگ:",
        "watermark_choose_color":"انتخاب رنگ...",
        "watermark_opacity":"تیرگی / شفافیت:",
        "watermark_direction":"جهت خواندن:",
        "watermark_direction_l_r":"چپ → راست",
        "watermark_direction_bl_tr":"پایین چپ → بالا راست",
        "watermark_direction_tl_br":"بالا چپ → پایین",
        "watermark_direction_b_t":"پایین → بالا",
        "watermark_direction_t_b":"بالا → پایین",
        "watermark_preview":"پیش‌نمایش:",
        "watermark_preview_sample":"متن نمونه",
        "watermark_empty_text":"لطفاً متن را وارد کنید.",
        "watermark_applied":"نشانه آب در تمام صفحات اعمال شد.",
        "watermark_saved":"نشانه آب ذخیره شد.",
        "image_scale":"اندازه:",
        "image_preview":"پیش‌نمایش تصویر:",
        "no_image_selected":"هیچ تصویری انتخاب نشده است",
        "browse":"مرور...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "ویرایش‌های محرمانه",
        "redact_add_black": "ویرایش محرمانه (سیاه)",
        "redact_add_white": "ویرایش محرمانه (سفید / پاک‌کن)",
        "redact_added_black": "ویرایش محرمانه سیاه اضافه شد",
        "redact_added_white": "ویرایش محرمانه سفید اضافه شد",
        "redact_apply_all": "اعمال تمام ویرایش‌های محرمانه و ذخیره",
        "redact_discard_all": "رد تمام ویرایش‌های محرمانه",
        "redact_discard": "رد این ویرایش محرمانه",
        "no_redactions": "هیچ ویرایش محرمانه‌ای وجود ندارد",
        "redact_confirm_title": "اعمال دائمی ویرایش‌های محرمانه",
        "redact_confirm_message": "هشدار: مناطق علامت‌گذاری شده به طور غیرقابل برگشت حذف خواهند شد (سیاه یا سفید).\nیک نسخه پشتیبان ایجاد خواهد شد (در صورت فعال بودن).\n\nادامه؟",
        "redact_apply": "بله، اکنون ویرایش کن",
        "redact_saved": "{0} ویرایش محرمانه با موفقیت اعمال و ذخیره شد.",
        "redact_saved_voice": "{0} ویرایش محرمانه اعمال شد",
        "redact_error": "خطا در ویرایش محرمانه",
        "filename_redacted":"_ویرایش_شده",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'درج شماره صفحات',
        'page_numbers_format': 'قالب شماره:',
        'page_numbers_format_arabic': '1، 2، 3 ... (عربی)',
        'page_numbers_format_roman_lower': 'i، ii، iii ... (رومی کوچک)',
        'page_numbers_format_roman_upper': 'I، II، III ... (رومی بزرگ)',
        'page_numbers_format_letter': 'A، B، C ... (حروف)',
        'page_numbers_format_custom': 'سفارشی',
        'page_numbers_custom_pattern': 'الگو:',
        'page_numbers_custom_placeholder': 'مثلاً "صفحه {nummer}" یا "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'از {nummer} برای شماره صفحه فعلی و {total} برای تعداد کل استفاده کنید',
        'page_numbers_position': 'موقعیت:',
        'page_numbers_pos_tl': 'بالا چپ',
        'page_numbers_pos_tc': 'بالا وسط',
        'page_numbers_pos_tr': 'بالا راست',
        'page_numbers_pos_ml': 'وسط چپ',
        'page_numbers_pos_mc': 'وسط',
        'page_numbers_pos_mr': 'وسط راست',
        'page_numbers_pos_bl': 'پایین چپ',
        'page_numbers_pos_bc': 'پایین وسط',
        'page_numbers_pos_br': 'پایین راست',
        'page_numbers_margins': 'حاشیه‌ها:',
        'page_numbers_margin_x': 'فاصله افقی:',
        'page_numbers_margin_y': 'فاصله عمودی:',
        'page_numbers_range': 'محدوده صفحات:',
        'page_numbers_all_pages': 'تمام صفحات',
        'page_numbers_custom_range': 'محدوده سفارشی',
        'page_numbers_from': 'از:',
        'page_numbers_to': 'تا:',
        'page_numbers_progress': 'درج شماره صفحات...',
        'page_numbers_start': 'شروع درج شماره صفحات...',
        'page_numbers_cancel': 'درج شماره صفحات لغو شد',
        'page_numbers_success': 'شماره صفحات با موفقیت اضافه شدند.\n\nآیا می‌خواهید PDF جدید را باز کنید؟\n\n{0}',
        'page_numbers_complete': 'شماره صفحات اضافه شد',
        'page_numbers_error_format': 'خطا در درج شماره صفحات: {0}',
        'page_numbers_content_type': 'نوع محتوا:',
        'page_numbers_tab_simple': 'شماره ساده',
        'page_numbers_tab_range': 'صفحه X از Y',
        'page_numbers_tab_date': 'تاریخ',
        'page_numbers_tab_custom': 'متن آزاد',
        'page_numbers_range_format': 'قالب:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'صفحه {aktuell} از {gesamt}',
        'page_numbers_range_custom': 'سفارشی',
        'page_numbers_range_placeholder': 'مثلاً "صفحه {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'قالب تاریخ:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 ژانویه 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'سفارشی',
        'page_numbers_date_placeholder': 'مثلاً %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'موقعیت:',
        'page_numbers_date_before': 'تاریخ قبل از شماره صفحه',
        'page_numbers_date_after': 'تاریخ بعد از شماره صفحه',
        'page_numbers_date_only': 'فقط تاریخ (بدون شماره صفحه)',
        'page_numbers_custom_text': 'متن سفارشی:',
        'page_numbers_custom_placeholder_text': 'از {seite} برای شماره صفحه و {gesamt} برای تعداد کل استفاده کنید\nمثلاً "محرمانه - صفحه {seite}" یا "{seite} از {gesamt}"',
        "filename_with_page_number":"_با_شماره_صفحه",
        "filename_with_page_declaration":"_با_اعلام_صفحه",
        "filename_with_pagenumber":"_با_شماره_صفحه",
        "filename_with_date":"_با_تاریخ",
        "filename_with_my_page_declaration":"_با_اعلام_صفحه_سفارشی",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "تغییرات ذخیره نشده",
        "unsaved_changes_message_darkmode": "درج‌های ذخیره نشده وجود دارد.\nآیا می‌خواهید قبل از تغییر، آنها را ذخیره کنید؟",
        "save_and_switch": "ذخیره و تغییر",
        "discard_and_switch": "تغییر اکنون",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'خروجی صفحات به عنوان تصویر',
        'export_images_menu': 'خروجی به عنوان تصویر (PNG/JPEG)',
        'export_images_format': 'فرمت تصویر:',
        'export_images_dpi': 'رزولوشن (DPI):',
        'export_images_quality': 'کیفیت JPEG:',
        'export_images_range': 'محدوده صفحات:',
        'export_images_all_pages': 'تمام صفحات',
        'export_images_custom_range': 'محدوده سفارشی',
        'export_images_from': 'از:',
        'export_images_to': 'تا:',
        'export_images_options': 'گزینه‌ها:',
        'export_images_single_files': 'هر صفحه به عنوان یک فایل جداگانه',
        'export_images_subfolder': 'خروجی به زیرپوشه',
        'export_images_subfolder_info': 'به زیرپوشه "نامPDF_تصاویر"',
        'export_images_same_folder': 'در همان پوشه PDF',
        'export_images_apply_darkmode': 'اعمال تنظیمات PDFDarkView (حالت تیره)',
        'export_images_target_folder': 'پوشه مقصد:',
        'export_images_browse': 'مرور...',
        'export_images_preview': 'پیش‌نمایش:',
        'export_images_preview_info': 'تنظیمات خروجی را انتخاب کنید',
        'export_images_preview_info_detail': '{0} صفحه به عنوان {1}\nرزولوشن: {2} DPI\nنام فایل: {3}\n{4}',
        'export_images_select_folder': 'پوشه مقصد را انتخاب کنید',
        'export_images_start': 'شروع خروجی تصاویر...',
        'export_images_progress': 'خروجی تصاویر...',
        'export_images_saving': 'ذخیره صفحه {0} از {1}...',
        'export_images_success': 'خروجی با موفقیت انجام شد!\n\n{0} تصویر در این مکان ذخیره شد:\n{1}',
        'export_images_complete': 'خروجی تصاویر کامل شد',
        'export_images_open_folder': '📁 باز کردن پوشه',
        'export_images_cancel': 'خروجی تصاویر لغو شد',
        'export_images_error_format': 'خطا در خروجی تصاویر: {0}',
        'export_images_pdf2image_missing': 'کتابخانه "pdf2image" نصب نشده است.\n\nلطفاً آن را با دستور زیر نصب کنید:\npip install pdf2image\n\nبرای ویندوز به Poppler نیز نیاز دارید:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'تبدیل PDF/A برای بایگانی طولانی مدت',
        'pdfa_menu': 'تبدیل PDF/A (مناسب برای بایگانی)',
        'pdfa_info': 'PDF را به فرمت PDF/A تبدیل می‌کند.\n\nPDF/A به طور خاص برای بایگانی طولانی مدت طراحی شده است و تضمین می‌کند که سند در آینده به درستی نمایش داده شود.',
        'pdfa_standard': 'استاندارد PDF/A:',
        'pdfa_standard_select': 'نسخه:',
        'pdfa_1': 'PDF/A-1 (ساده، سازگاری گسترده)',
        'pdfa_2': 'PDF/A-2 (مدرن، فشرده‌سازی بهتر)',
        'pdfa_3': 'PDF/A-3 (جدیدترین نسخه، اجازه پیوست‌ها)',
        'pdfa_standards_explanation': '📖 توضیح استانداردها:\n\n'
            '• PDF/A-1: پایه، سازگار با سیستم‌های قدیمی (حدود 2005)\n'
            '• PDF/A-2: مدرن‌تر، فشرده‌سازی بهتر، پشتیبانی از شفافیت (حدود 2011)\n'
            '• PDF/A-3: جدیدترین نسخه، اجازه درج پیوست‌های فایل (حدود 2013)\n\n'
            'توصیه: PDF/A-2 یک سازش خوب بین سازگاری و ویژگی‌های مدرن است.',
        'pdfa_options': 'گزینه‌ها:',
        'pdfa_compress_enable': 'فشرده‌سازی PDF (فایل کوچکتر)',
        'pdfa_metadata_preserve': 'حفظ فراداده (عنوان، نویسنده و غیره)',
        'pdfa_target_folder': 'پوشه مقصد:',
        'pdfa_browse': 'مرور...',
        'pdfa_select_folder': 'پوشه مقصد را انتخاب کنید',
        'pdfa_ocr_info_unknown': '🔍 امکان بررسی محتوای متن وجود ندارد.',
        'pdfa_ocr_info_not_needed': '✅ متن موجود است - OCR مورد نیاز نیست.\nPDF/A را می‌توان مستقیماً ایجاد کرد.',
        'pdfa_ocr_info_recommended': '⚠️ متن کافی یافت نشد.\n\nبرای PDFهای قابل جستجو، توصیه می‌کنیم ابتدا OCR را اجرا کنید.\nتوجه: PDF/A بدون OCR نیز کار می‌کند - اما متن قابل جستجو نخواهد بود.',
        'pdfa_ocr_info_error': '❌ خطا در بررسی: {0}',
        'pdfa_start': 'شروع تبدیل PDF/A...',
        'pdfa_progress': 'تبدیل PDF/A در حال انجام...',
        'pdfa_success': 'تبدیل PDF/A با موفقیت انجام شد!\n\nذخیره شده به عنوان:\n{0}\n\nآیا می‌خواهید PDF جدید را باز کنید؟',
        'pdfa_complete': 'تبدیل PDF/A کامل شد',
        'pdfa_cancel': 'تبدیل PDF/A لغو شد',
        'pdfa_error_format': 'خطا در تبدیل PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'کتابخانه "ocrmypdf" نصب نشده است.\n\nلطفاً آن را با دستور زیر نصب کنید:\npip install ocrmypdf',
        'btn_convert': 'تبدیل',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'بهینه‌سازی PDF (کاهش حجم فایل)',
        'optimize_menu': 'بهینه‌سازی PDF (حجم فایل)',
        'optimize_info': 'حجم فایل PDF را از طریق روش‌های مختلف بهینه‌سازی کاهش می‌دهد.\n\nهرچه سطح فشرده‌سازی بالاتر باشد، فایل کوچکتر می‌شود - با امکان کاهش کیفیت در تصاویر.',
        'optimize_level': 'سطح فشرده‌سازی:',
        'optimize_level_low': 'کم (سریع، صرفه‌جویی کم)',
        'optimize_level_medium': 'متوسط (سازش خوب)',
        'optimize_level_high': 'زیاد (صرفه‌جویی زیاد)',
        'optimize_level_maximum': 'حداکثر (حداکثر صرفه‌جویی، کند)',
        'optimize_level_explanation': 'توصیه: "متوسط" سازش خوبی بین سرعت و حجم فایل است.',
        'optimize_options': 'گزینه‌ها:',
        'optimize_compress_images': 'فشرده‌سازی تصاویر (کاهش کیفیت JPEG)',
        'optimize_clean_objects': 'حذف اشیاء استفاده نشده',
        'optimize_preserve_metadata': 'حفظ فراداده (عنوان، نویسنده و غیره)',
        'optimize_image_quality': 'کیفیت تصویر:',
        'optimize_range': 'محدوده صفحات:',
        'optimize_all_pages': 'تمام صفحات',
        'optimize_custom_range': 'محدوده سفارشی',
        'optimize_from': 'از:',
        'optimize_to': 'تا:',
        'optimize_target_folder': 'پوشه مقصد:',
        'optimize_browse': 'مرور...',
        'optimize_select_folder': 'پوشه مقصد را انتخاب کنید',
        'optimize_info_box': 'اطلاعات',
        'optimize_info_text': 'بهینه‌سازی ممکن است برای PDFهای بزرگ چند دقیقه طول بکشد.\n\nتصاویر با کیفیت کاهش یافته ذخیره می‌شوند که می‌تواند حجم فایل را به طور قابل توجهی کاهش دهد.',
        'optimize_start': 'شروع بهینه‌سازی PDF...',
        'optimize_progress': 'بهینه‌سازی PDF...',
        'optimize_cancel': 'بهینه‌سازی PDF لغو شد',
        'optimize_complete': 'بهینه‌سازی PDF کامل شد',
        'optimize_error_format': 'خطا در بهینه‌سازی PDF:\n\n{0}',
        'optimize_success_message': 'بهینه‌سازی PDF با موفقیت انجام شد!\n\nذخیره شده به عنوان:\n{0}\n\nقبل: {1}\nبعد: {2}\nصرفه‌جویی: {3:.1f}%\n\n{4}\n\nآیا می‌خواهید PDF بهینه‌سازی شده را باز کنید؟',
        'optimize_success_message_no_size': 'بهینه‌سازی PDF با موفقیت انجام شد!\n\nذخیره شده به عنوان:\n{0}\n\nاطلاعات حجم در دسترس نیست.\n\nآیا می‌خواهید PDF بهینه‌سازی شده را باز کنید؟',
        'optimize_result_positive': 'فایل {0:.1f}% کاهش یافت.',
        'optimize_result_zero': 'تغییری در حجم فایل ایجاد نشد.',
        'optimize_result_negative': 'فایل {0:.1f}% افزایش یافت.\nبهینه‌سازی نادیده گرفته شد، فایل اصلی حفظ شد.',
        'btn_optimize': 'شروع بهینه‌سازی',
        'filename_optimize_low_suffix': '_بهینه_سازی_کم',
        'filename_optimize_medium_suffix': '_بهینه_سازی',
        'filename_optimize_high_suffix': '_بهینه_سازی_زیاد',
        'filename_optimize_maximum_suffix': '_بهینه_سازی_حداکثر',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'برش PDF',
        'crop_menu': 'برش PDF (Crop)',
        'crop_range': 'اعمال به:',
        'crop_all_pages': 'تمام صفحات',
        'crop_current_page': 'فقط صفحه فعلی',
        'crop_values': 'مقادیر برش (بر حسب نقطه):',
        'crop_left': 'چپ:',
        'crop_right': 'راست:',
        'crop_top': 'بالا:',
        'crop_bottom': 'پایین:',
        'crop_presets': 'پیش‌تنظیمات:',
        'crop_preset_white': 'تشخیص حاشیه‌های سفید',
        'crop_reset': 'بازنشانی',
        'crop_mouse_hint': '🖱️ یک مستطیل بکشید تا منطقه را تقریباً انتخاب کنید.\nسپس می‌توانید مقادیر را در SpinBoxها به دقت تنظیم کنید.\nتنظیم دستی با ماوس امکان‌پذیر نیست.',
        'crop_apply': 'برش',
        'crop_scope_all': 'تمام صفحات',
        'crop_scope_current': 'صفحه فعلی',
        'crop_new_size': 'اندازه جدید: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'هیچ PDF بارگذاری نشده است',
        'crop_preview_error': 'خطا در بارگذاری پیش‌نمایش',
        'crop_start': 'شروع برش...',
        'crop_progress': 'برش PDF...',
        'crop_success': 'PDF با موفقیت برش خورد!\n\nذخیره شده به عنوان:\n{0}\n\nآیا می‌خواهید PDF برش خورده را باز کنید؟',
        'crop_complete': 'برش کامل شد',
        'crop_cancel': 'برش لغو شد',
        'crop_error_format': 'خطا در برش:\n\n{0}',
        'filename_crop_suffix': '_برش_خورده',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'مسطح‌سازی PDF (Flatten)',
        'flatten_menu': 'مسطح‌سازی PDF (Flatten)',
        'flatten_info': 'مسطح‌سازی PDF تمام عناصر قابل ویرایش را در محتوای صفحه "می‌سوزاند".\n\nپس از آن، فیلدهای فرم، حاشیه‌نویسی‌ها، متون، ضربدرها، امضاها، تصاویر و اشکال دیگر به صورت جداگانه قابل ویرایش نیستند.',
        'flatten_explanation_title': '📖 این برای چه کاری مفید است؟',
        'flatten_explanation_text': 'مسطح‌سازی در شرایط زیر مورد نیاز است:\n\n'
            '• 📄 می‌خواهید سند را برای چاپ آماده کنید\n'
            '• 🔒 می‌خواهید از تغییر فیلدهای فرم توسط دیگران جلوگیری کنید\n'
            '• 📎 می‌خواهید حاشیه‌نویسی‌ها و نظرات را به طور "دائم" در سند جاسازی کنید\n'
            '• 🖼️ می‌خواهید متون، ضربدرها، امضاها، تصاویر و اشکال درج شده را به طور دائم در سند تثبیت کنید\n'
            '• 📦 می‌خواهید فایل را برای بایگانی آماده کنید\n\n'
            'مسطح‌سازی PDF را کوچکتر می‌کند و از جابه‌جایی یا حذف تصادفی عناصر جلوگیری می‌کند.',
        'flatten_what_title': 'چه چیزی مسطح می‌شود؟',
        'flatten_what_list': '• ✅ فیلدهای فرم (فیلدهای متن، کادرهای انتخاب، دکمه‌ها)\n'
            '• ✅ حاشیه‌نویسی‌ها (نظرات، برجسته‌سازی‌ها، یادداشت‌ها)\n'
            '• ✅ لایه‌های رویی (متون، ضربدرها، امضاها، تصاویر، اشکال)',
        'flatten_options': 'گزینه‌ها:',
        'flatten_forms': 'مسطح‌سازی فیلدهای فرم',
        'flatten_annotations': 'مسطح‌سازی حاشیه‌نویسی‌ها',
        'flatten_overlays': 'مسطح‌سازی لایه‌های رویی (متون، ضربدرها، امضاها، تصاویر، اشکال)',
        'flatten_target_folder': 'پوشه مقصد:',
        'flatten_browse': 'مرور...',
        'flatten_select_folder': 'پوشه مقصد را انتخاب کنید',
        'flatten_warning': '⚠️ مهم: مسطح‌سازی یک فرآیند غیرقابل بازگشت است!\n\nپس از مسطح‌سازی، عناصر قابل ویرایش دیگر قابل تغییر یا حذف جداگانه نیستند.\nدر صورت لزوم قبلاً یک نسخه پشتیبان ایجاد کنید.',
        'flatten_apply': 'مسطح‌سازی',
        'flatten_start': 'شروع مسطح‌سازی...',
        'flatten_progress': 'مسطح‌سازی PDF...',
        'flatten_success': 'PDF با موفقیت مسطح شد!\n\nذخیره شده به عنوان:\n{0}\n\nآیا می‌خواهید PDF مسطح شده را باز کنید؟',
        'flatten_complete': 'مسطح‌سازی کامل شد',
        'flatten_cancel': 'مسطح‌سازی لغو شد',
        'flatten_error_format': 'خطا در مسطح‌سازی:\n\n{0}',
        'filename_flatten_suffix': '_مسطح_شده',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'رویه‌گذاری PDF (Overlay)',
        'overlay_menu': 'رویه‌گذاری PDF (Overlay)',
        'overlay_info': 'یک PDF (رویه) را روی PDF دیگر قرار می‌دهد.\n\nPDF رویه روی PDF پایه قرار می‌گیرد. این برای نشانه‌های آب، لوگوها، سربرگ‌ها یا مهرها مفید است.',
        'overlay_explanation_title': '📖 این برای چه کاری مفید است؟',
        'overlay_explanation_text': 'رویه‌گذاری در شرایط زیر مورد نیاز است:\n\n'
            '• 🏢 قرار دادن لوگوی شرکت به عنوان نشانه آب در هر صفحه\n'
            '• 📄 قرار دادن سربرگ روی PDF خالی\n'
            '• 🖊️ قرار دادن رویه مهر روی سند\n'
            '• 🔖 قرار دادن نشانه آب روی تمام صفحات\n'
            '• 📑 قرار دادن رویه فرم روی قالب',
        'overlay_type': 'نوع رویه:',
        'overlay_type_fullpage': 'صفحه کامل (پوشاننده)',
        'overlay_type_transparent': 'صفحه کامل (شفاف - توصیه می‌شود)',
        'overlay_type_stamp': 'مهر (قابل موقعیت‌یابی)',
        'overlay_type_info_fullpage': '📄 PDF رویه دقیقاً روی کل صفحه قرار می‌گیرد.\nپس‌زمینه سفید را می‌توان حذف کرد تا فقط محتوا قابل مشاهده باشد.',
        'overlay_type_info_transparent': '🔍 PDF رویه با پس‌زمینه شفاف روی کل صفحه قرار می‌گیرد.\nپس‌زمینه سفید به طور خودکار حذف می‌شود - ایده‌آل برای نشانه‌های آب و لوگوها!',
        'overlay_type_info_stamp': '🖊️ PDF رویه به عنوان مهر موقعیت‌یابی و مقیاس‌بندی می‌شود.\nعالی برای لوگوها، مهرها یا امضاها در موقعیت‌های خاص.',
        'overlay_remove_background': 'حذف پس‌زمینه سفید:',
        'overlay_remove_background_enable': 'حذف پس‌زمینه سفید از PDF رویه (رویه را شفاف می‌کند)',
        'overlay_remove_background_tooltip': 'مناطق سفید را از PDF رویه حذف می‌کند تا متن زیرین قابل مشاهده شود.',
        'overlay_threshold': 'مقدار آستانه:',
        'overlay_threshold_hint': '(1-254، بالاتر = سفید بیشتری حذف می‌شود)',
        'overlay_select_file': 'انتخاب PDF رویه:',
        'overlay_file_placeholder': 'لطفاً یک فایل PDF برای رویه انتخاب کنید',
        'overlay_browse': 'مرور...',
        'overlay_select_overlay': 'انتخاب PDF رویه',
        'overlay_range': 'محدوده صفحات:',
        'overlay_all_pages': 'تمام صفحات',
        'overlay_custom_range': 'محدوده سفارشی',
        'overlay_from': 'از:',
        'overlay_to': 'تا:',
        'overlay_position': 'موقعیت:',
        'overlay_position_center': 'مرکز',
        'overlay_position_top_left': 'بالا چپ',
        'overlay_position_top_right': 'بالا راست',
        'overlay_position_bottom_left': 'پایین چپ',
        'overlay_position_bottom_right': 'پایین راست',
        'overlay_size': 'اندازه:',
        'overlay_size_original': 'اندازه اصلی',
        'overlay_size_fit_page': 'تناسب با صفحه',
        'overlay_size_custom': 'سفارشی (%)',
        'overlay_opacity': 'شفافیت:',
        'overlay_target_folder': 'پوشه مقصد:',
        'overlay_browse_folder': 'مرور...',
        'overlay_select_folder': 'پوشه مقصد را انتخاب کنید',
        'overlay_warning': '⚠️ توجه: PDF رویه روی PDF پایه قرار می‌گیرد و در آن "سوخته" می‌شود.\n\nعناصر PDF رویه پس از ذخیره دیگر قابل ویرایش جداگانه نیستند.',
        'overlay_apply': 'رویه‌گذاری',
        'overlay_start': 'شروع رویه‌گذاری...',
        'overlay_progress': 'رویه‌گذاری PDF...',
        'overlay_success': 'PDF با موفقیت رویه‌گذاری شد!\n\nذخیره شده به عنوان:\n{0}\n\nآیا می‌خواهید PDF رویه‌گذاری شده را باز کنید؟',
        'overlay_complete': 'رویه‌گذاری کامل شد',
        'overlay_cancel': 'رویه‌گذاری لغو شد',
        'overlay_error_format': 'خطا در رویه‌گذاری:\n\n{0}',
        'overlay_no_file': 'هیچ PDF رویه‌ای انتخاب نشده است.\n\nلطفاً یک فایل PDF برای رویه‌گذاری انتخاب کنید.',
        'filename_overlay_suffix': '_رویه_گذاری_شده',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'استخراج تصاویر از PDF',
        'extract_images_menu': 'استخراج تمام تصاویر',
        'extract_images_info': 'تمام تصاویر را از PDF استخراج کرده و به عنوان فایل‌های جداگانه ذخیره می‌کند.\n\nتصاویر در قالب اصلی خود ذخیره می‌شوند یا به قالب انتخابی تبدیل می‌شوند.',
        'extract_images_format': 'فرمت تصویر:',
        'extract_images_quality': 'کیفیت JPEG:',
        'extract_images_options': 'گزینه‌ها:',
        'extract_images_subfolder': 'استخراج به زیرپوشه ("نامPDF_تصاویر")',
        'extract_images_unique': 'فقط تصاویر منحصر به فرد (جلوگیری از تکراری)',
        'extract_images_range': 'محدوده صفحات:',
        'extract_images_all_pages': 'تمام صفحات',
        'extract_images_custom_range': 'محدوده سفارشی',
        'extract_images_from': 'از:',
        'extract_images_to': 'تا:',
        'extract_images_target_folder': 'پوشه مقصد:',
        'extract_images_browse': 'مرور...',
        'extract_images_select_folder': 'پوشه مقصد را انتخاب کنید',
        'extract_images_info_box': 'اطلاعات',
        'extract_images_info_text': 'استخراج ممکن است برای PDFهای بزرگ چند دقیقه طول بکشد.\n\nتصاویر با نام اصلی خود ذخیره می‌شوند (صفحه_تصویر).',
        'extract_images_extract': 'استخراج',
        'extract_images_start': 'شروع استخراج...',
        'extract_images_progress': 'استخراج تصاویر...',
        'extract_images_success': '✅ تصاویر با موفقیت استخراج شدند!\n\n{0} تصویر در این مکان ذخیره شد:\n{1}',
        'extract_images_complete': 'استخراج تصاویر کامل شد',
        'extract_images_cancel': 'استخراج لغو شد',
        'extract_images_error_format': 'خطا در استخراج تصاویر:\n\n{0}',
        'extract_images_open_folder': '📁 باز کردن پوشه',
        'extract_images_no_images': 'هیچ تصویری در PDF یافت نشد.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'چند صفحه در یک صفحه (N-Up)',
        'nup_menu': 'چند صفحه در یک صفحه (N-Up)',
        'nup_info': 'چندین صفحه PDF را در یک صفحه مرتب می‌کند.\n\nایده‌آل برای چاپ‌های فشرده، نمای کلی یا جزوات.',
        'nup_layout': 'چیدمان:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'پیش‌نمایش:',
        'nup_preview_info': '{0} صفحه → {1} صفحه در هر برگ → {2} برگ\nچیدمان: {3}',
        'nup_order': 'ترتیب:',
        'nup_order_horizontal': 'افقی (ردیف به ردیف)',
        'nup_order_vertical': 'عمودی (ستون به ستون)',
        'nup_order_horizontal_reverse': 'افقی معکوس',
        'nup_order_vertical_reverse': 'عمودی معکوس',
        'nup_range': 'محدوده صفحات:',
        'nup_all_pages': 'تمام صفحات',
        'nup_custom_range': 'محدوده سفارشی',
        'nup_from': 'از:',
        'nup_to': 'تا:',
        'nup_options': 'گزینه‌ها:',
        'nup_margins': 'حاشیه‌ها:',
        'nup_margin_between': 'فاصله بین صفحات:',
        'nup_page_numbers': 'درج شماره صفحات',
        'nup_target_folder': 'پوشه مقصد:',
        'nup_browse': 'مرور...',
        'nup_select_folder': 'پوشه مقصد را انتخاب کنید',
        'nup_create': 'ایجاد',
        'nup_start': 'شروع N-Up...',
        'nup_progress': 'ایجاد N-Up...',
        'nup_success': 'N-Up با موفقیت ایجاد شد!\n\nذخیره شده به عنوان:\n{0}\n\nآیا می‌خواهید PDF جدید را باز کنید؟',
        'nup_complete': 'N-Up کامل شد',
        'nup_cancel': 'N-Up لغو شد',
        'nup_error_format': 'خطا در N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'تغییر اندازه صفحه',
        'pagesize_menu': 'تغییر اندازه صفحه',
        'pagesize_info': 'اندازه صفحه PDF را تغییر می‌دهد.\n\nمحتوا به طور خودکار با اندازه جدید تطبیق داده می‌شود.',
        'pagesize_format': 'فرمت:',
        'pagesize_select': 'یک فرمت استاندارد انتخاب کنید:',
        'pagesize_custom': 'اندازه سفارشی:',
        'pagesize_width': 'عرض:',
        'pagesize_height': 'ارتفاع:',
        'pagesize_orientation': 'جهت:',
        'pagesize_portrait': 'عمودی',
        'pagesize_landscape': 'افقی',
        'pagesize_scale_options': 'گزینه‌های مقیاس‌بندی:',
        'pagesize_fit': 'تطبیق (حفظ نسبت ابعاد)',
        'pagesize_stretch': 'کشش (تحریف)',
        'pagesize_center': 'مرکز (اندازه اصلی)',
        'pagesize_range': 'محدوده صفحات:',
        'pagesize_all_pages': 'تمام صفحات',
        'pagesize_custom_range': 'محدوده سفارشی',
        'pagesize_from': 'از:',
        'pagesize_to': 'تا:',
        'pagesize_target_folder': 'پوشه مقصد:',
        'pagesize_browse': 'مرور...',
        'pagesize_select_folder': 'پوشه مقصد را انتخاب کنید',
        'pagesize_apply': 'اعمال',
        'pagesize_start': 'شروع تغییر اندازه صفحه...',
        'pagesize_progress': 'تغییر اندازه صفحه...',
        'pagesize_success': 'اندازه صفحه با موفقیت تغییر کرد!\n\nذخیره شده به عنوان:\n{0}\n\nآیا می‌خواهید PDF جدید را باز کنید؟',
        'pagesize_complete': 'تغییر اندازه صفحه کامل شد',
        'pagesize_cancel': 'تغییر اندازه صفحه لغو شد',
        'pagesize_error_format': 'خطا در تغییر اندازه صفحه:\n\n{0}',
        'pagesize_preview_info': 'اندازه جدید: {0} x {1} pt',
        'filename_pagesize_suffix': '_اندازه_جدید',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'اطلاعات PDF',
        'pdf_info_menu': 'نمایش اطلاعات PDF',
        'pdf_info_voice': 'در حال نمایش اطلاعات PDF',
        'pdf_info_error': 'خطا در نمایش اطلاعات PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "نمایش میانبرهای صفحه کلید",
        "shortcuts_dialog_title": "میانبرهای صفحه کلید",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 فایل</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>باز کردن PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>بستن PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>ذخیره به عنوان...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>محافظت از سند</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>چاپ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>چاپ فوری (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>خروج از برنامه</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 خروجی</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>خروجی به عنوان Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>خروجی به عنوان DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>خروجی به عنوان TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>خروجی به عنوان تصویر (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>استخراج تصاویر</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ پردازش سند</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (چند صفحه)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>تبدیل PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>مسطح‌سازی PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>رویه‌گذاری PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>بهینه‌سازی PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ ویرایش</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>جستجو</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>افزودن نشانک</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>مدیریت نشانک‌ها</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>نشانک بعدی</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>نشانک قبلی</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>اجرای OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 مدیریت صفحات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>چرخش صفحه فعلی</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>چرخش تمام صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>نرمال‌سازی صفحه فعلی</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>نرمال‌سازی تمام صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>حذف صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>استخراج صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>درج صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>جابه‌جایی صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>ادغام PDFها</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>تغییر اندازه صفحه</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 درج</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>درج متن</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>درج ضربدر</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>درج امضا 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>درج امضا 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>درج تصویر</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>درج مستطیل</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>درج بیضی</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>درج خط</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>درج پیکان</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>درج شماره صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>نشانه آب متنی</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>نشانه آب تصویری</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ ویرایش‌های محرمانه</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ویرایش محرمانه (سیاه)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ویرایش محرمانه (سفید)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>اعمال تمام ویرایش‌های محرمانه</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ پیشرفته</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>برش PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ویرایش فراداده</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ نمایش</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>تغییر حالت تیره/روشن</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>نمایش پنجره متن</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>عرض صفحه (بزرگنمایی)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>دو صفحه (بزرگنمایی)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>نمای کلی (بزرگنمایی)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ تنظیمات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>مدیریت رمز عبور</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>تنظیمات OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>تنظیمات امضا</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>قالب‌بندی نام فایل</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>خروجی تنظیمات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>وارد کردن تنظیمات</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ اطلاعات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>نمایش اطلاعات PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>روشن/خاموش کردن خروجی صوتی</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>فوکوس بر نوار منو</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "نسخه جدید در دسترس است",
        "update_available_message": "نسخه جدید <b>{0}</b> در دسترس است.\n\nبرای دانلود به‌روزرسانی، از صفحه انتشار دیدن کنید:\n{1}",
        "update_available_voice": "نسخه جدید {0} در دسترس است. لطفاً به‌روزرسانی را از صفحه گیت‌هاب دانلود کنید.",
        "update_open_release": "باز کردن صفحه انتشار",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "دانلود همه ترجمه‌ها",
        "ask_download_all_translations": """علاوه بر آلمانی، انگلیسی و ویتنامی، {total_languages} زبان رابط کاربری دیگر نیز در دسترس است.\n\nآیا باید ارائه / به‌روزرسانی شوند؟\n\nتوجه:\nزبان‌های غیرضروری را می‌توانید بعداً به‌صورت دستی در دایرکتوری حذف کنید:\n{translations_path}
        \nاگر لغو کنید، می‌توانید زبان‌های رابط کاربری را بعداً از طریق منوی 'ابزارها → به‌روزرسانی ترجمه‌ها' دانلود کنید.""",
        "menu_update_translations": "به‌روزرسانی ترجمه‌ها",
        "translations_updated": "ترجمه‌ها به‌روزرسانی شدند",
        "translations_update_success": "{} ترجمه با موفقیت به‌روزرسانی شدند ({} جدید، {} به‌روزرسانی شده).",
        "translations_update_error": "خطا در به‌روزرسانی ترجمه‌ها",
        "translations_update_no_changes": "همه ترجمه‌ها در حال حاضر به‌روز هستند.",
        "translations_update_offline": "اتصال به اینترنت وجود ندارد. ترجمه‌ها قابل به‌روزرسانی نبودند.",
        "translations_update_in_progress": "ترجمه‌ها در پس‌زمینه به‌روزرسانی می‌شوند...",
        "translations_downloading": "در حال دانلود ترجمه‌ها...",
        "translations_path_hint": "دایرکتوری کاربر برای ترجمه‌ها",
        "translations_update_not_available_title": "به‌روزرسانی در دسترس نیست",
        "translations_update_not_available_message": """به‌روزرسانی ترجمه‌ها فقط در نسخه نصب‌شده در دسترس است.\n\nدر حالت توسعه، ترجمه‌ها در حال حاضر به‌روز هستند.""",
        "translations_update_no_internet_title": "اتصال به اینترنت وجود ندارد",
        "translations_update_no_internet_message": """امکان برقراری اتصال به اینترنت وجود ندارد.\n\nترجمه‌ها قابل دانلود از گیت‌هاب نیستند.\n\nراه‌حل‌های ممکن:
        • اتصال اینترنت خود را بررسی کنید
        • فایروال احتمالی را به‌طور موقت غیرفعال کنید
        • بعداً دوباره تلاش کنید
        \nهمچنین می‌توانید ترجمه‌ها را به‌صورت دستی از گیت‌هاب دانلود کنید:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "به‌روزرسانی در حال انجام است",
        "btn_retry": "تلاش مجدد",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "به PDF Dark View خوش آمدید",
        "welcome_title_not_supported": "به PDF Dark View خوش آمدید",
        "welcome_message": "به PDF Dark View خوش آمدید!\n\nزبان سیستم شما به‌عنوان '{language}' شناسایی شد.\nآیا می‌خواهید از این زبان برای رابط کاربری استفاده کنید؟\n\nمی‌توانید در هر زمان از طریق 'تنظیمات → زبان' زبان را تغییر دهید.",
        "welcome_message_language_not_available": "به PDF Dark View خوش آمدید!\n\nزبان سیستم شما به‌عنوان '{language}' شناسایی شد.\nاین زبان هنوز نصب نشده است.\n\nآیا می‌خواهید ترجمه‌های {language} را اکنون از گیت‌هاب دانلود کنید؟\n\n(زبان سپس به‌طور خودکار برای رابط کاربری استفاده می‌شود.)",
        "welcome_message_language_not_supported": "به PDF Dark View خوش آمدید!\n\nزبان سیستم شما به‌عنوان '{language}' شناسایی شد.\nمتأسفانه هنوز ترجمه‌ای برای این زبان وجود ندارد.\n\nرابط کاربری به {fallback_language} نمایش داده می‌شود.\n\nمی‌توانید در هر زمان از طریق 'تنظیمات → زبان' زبان را تغییر دهید.\nاگر مایل هستید، می‌توانید خود نیز ترجمه‌ای برای زبان خود ارائه دهید:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "بله، استفاده از زبان سیستم",
        "welcome_keep_english": "خیر، حفظ زبان انگلیسی",
        "welcome_download_language": "بله، دانلود {language}",

        # ============================================
        # 107. مسیرهای اخیر
        # ============================================

        'menu_recent': 'اخیراً استفاده شده',
        'menu_recent_dirs': 'پوشه‌ها...',
        'menu_recent_files': 'فایل‌ها...',
        'recent_manage': 'مدیریت...',
        'recent_enable_tracking': 'ذخیره مسیرهای اخیر (حریم خصوصی)',
        'recent_enable_info': 'برای ذخیره نکردن مسیرها، این گزینه را غیرفعال کنید',
        'recent_tracking_disabled': 'ردیابی مسیر غیرفعال است',
        'recent_enabled': 'فعال',
        'recent_disabled': 'غیرفعال',
        'recent_tracking_status': 'ردیابی مسیر {0}',
        'recent_dialog_title': 'مسیرهای اخیر',
        'recent_tab_directories': 'پوشه‌ها',
        'recent_tab_files': 'فایل‌ها',
        'recent_dirs_instruction': 'برای باز کردن کادر محاوره‌ای فایل در پوشه، دوبار کلیک کنید',
        'recent_files_instruction': 'برای باز کردن مستقیم PDF، دوبار کلیک کنید',
        'recent_no_directories': '(هیچ پوشه‌ای ذخیره نشده)',
        'recent_no_files': '(هیچ فایلی ذخیره نشده)',
        'recent_default_current': '⭐ پیش‌فرض: {0}',
        'recent_set_as_default': '⭐ تنظیم به‌عنوان پیش‌فرض',
        'recent_default_set_title': 'پوشه پیش‌فرض تنظیم شد',
        'recent_default_set_message': 'پوشه "{0}" به‌عنوان پیش‌فرض برای باز کردن PDF تنظیم شد.',
        'recent_default_set_voice': 'پوشه پیش‌فرض تنظیم شد',
        'recent_directory_not_found': 'پوشه یافت نشد',
        'recent_file_not_found': 'فایل یافت نشد',
        'recent_remove_selected': 'حذف',
        'recent_remove_title': 'حذف مسیر',
        'recent_remove_confirm': 'آیا واقعاً می‌خواهید مسیر "{0}" را از لیست حذف کنید؟',
        'recent_path_removed': 'مسیر حذف شد',
        'recent_clear_all': 'حذف همه',
        'recent_clear_title': 'حذف همه مسیرها',
        'recent_clear_confirm_type': 'آیا واقعاً می‌خواهید همه {0} را حذف کنید؟',
        'recent_cleared': 'لیست پاک شد',
        'recent_path_not_found_title': 'مسیر یافت نشد',
        'recent_path_not_found_message': 'مسیر "{0}" دیگر وجود ندارد.',
        'recent_open_file': 'باز کردن فایل',
        'btn_open_recent': 'باز کردن',
        'recent_open_file_question': 'آیا می‌خواهید "{0}" را به‌عنوان PDF باز کنید؟',
        'recent_not_pdf': 'فایل انتخاب شده PDF نیست.',
        'recent_more_entries': 'ورودی‌های بیشتر...',
        'btn_remove': 'حذف',
        'btn_clear': 'پاک کردن همه',
        'recent_context_open': 'باز کردن',
        'recent_context_reveal': 'نمایش در Finder',
        'recent_context_set_default': '⭐ تنظیم به‌عنوان پیش‌فرض',
        'recent_context_open_terminal': '💻 باز کردن ترمینال',
        'recent_context_file_info': 'اطلاعات فایل',
        'recent_context_open_with_default': '📄 باز کردن با برنامه پیش‌فرض',
        'recent_context_remove': 'حذف از لیست',
        'recent_context_clear_all': 'حذف همه',
        'recent_file_info_title': 'اطلاعات فایل',
        'recent_file_info_name': 'نام',
        'recent_file_info_path': 'مسیر',
        'recent_file_info_size': 'اندازه',
        'recent_file_info_modified': 'تاریخ تغییر',
        'recent_file_info_pages': 'صفحات',
        'recent_error_reveal': 'خطا در باز کردن در Finder',
        'recent_error_terminal': 'خطا در باز کردن ترمینال',
        'recent_error_info': 'خطا در دریافت اطلاعات فایل',
        'open_user_data_folder': 'نمایش پوشه داده‌های کاربر',

        # ============================================
        # 108. حذف صفحات زوج/فرد
        # ============================================
        "pages_delete_even": "حذف تمام صفحات زوج",
        "pages_delete_odd":  "حذف تمام صفحات فرد",
        "progress_even_pages": "در حال حذف صفحات زوج",
        "progress_odd_pages": "در حال حذف صفحات فرد",
        "progress_mark_delete_even": "{} صفحه زوج برای حذف علامت‌گذاری شد",
        "progress_mark_delete_odd":  "{} صفحه فرد برای حذف علامت‌گذاری شد",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "برنامه در حال خروج است",

    }
