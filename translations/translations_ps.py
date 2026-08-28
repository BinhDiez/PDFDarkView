
# ============================================
# translations_ps.py - Paschtu Wörterbuch
# Vollständig sortiert nach Kategorien
# ============================================

def load_pashto_strings():
    """Lädt alle paschtuischen Strings (Paschtu, arabische Schrift)"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF تیاره لید د BinhDiez لخوا",
        'app_name': "PDF تیاره لید",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF بار کړئ",
        'btn_text_window': "OCR متن",
        'btn_first': "لومړی مخ",
        'btn_prev': "مخکنی مخ",
        'btn_next': "راتلونکی مخ",
        'btn_last': "وروستی مخ",
        'btn_print': "چاپ کړئ",
        'btn_darkmode_light': "روښانه حالت",
        'btn_darkmode_dark': "تیاره حالت",
        'btn_delete_pages': "مخونه ړنګ کړئ",
        'btn_extract_pages': "مخونه استخراج کړئ",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "سمه ده",
        'btn_cancel': "لغوه کړئ",
        'btn_save': "خوندي کړئ",
        'btn_close': "وتړئ",
        'btn_delete': "ړنګ کړئ",
        'btn_delete_all': "ټول ړنګ کړئ",
        'btn_copy': "کاپي کړئ",
        'btn_export': "صادر کړئ",
        'btn_show': "پټ نوم ښکاره کړئ",
        'btn_hide': "پټ نوم پټ کړئ",
        'btn_authenticate': "تصدیق کړئ",
        'btn_settings': "تنظیمات",
        'btn_protect': "خوندي کړئ",
        'btn_remove_password': "پټ نوم لرې کړئ",
        'btn_manage': "د پټ نوم مدیریت",
        'btn_retry': "بیا هڅه وکړئ",
        'btn_select_all': "ټول وټاکئ",
        'btn_clear_selection': "انتخاب لغوه کړئ",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "مخ {0} له {1}",
        'page_count': "له {0}",
        'goto_page': "مخ ته لاړ شئ",
        'page_simple': "مخ {0}",
        'full_view_page': "بشپړ لید مخ {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "د لټون کلیمه دننه کړئ + Enter",
        'search_results': "پایلې: {0} له {1}",
        'search_nav_hint': "Enter: بل (Shift+Enter: مخکنی)",
        'search_no_results': "پایله و نه موندل شوه",
        'search_error': "د لټون تېروتنه",
        'search_active': "د لټون ساحه فعاله شوه",
        'search_closed': "لټون پای ته ورسېد",
        'search_position': "مخ {0} {1}",
        'search_pos_top': "پورته",
        'search_pos_upper': "پورتنۍ برخه",
        'search_pos_middle': "منځ",
        'search_pos_lower': "لاندنۍ برخه",
        'search_pos_bottom': "لاندې",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "د متن پېژندنه په بریالیتوب سره بشپړه شوه!",
        'ocr_success_title': "OCR بریالی شو",
        'ocr_success_message': "اسناد اوس د لټون وړ دي.",
        'ocr_failed': "OCR ناکام شو",
        'ocr_in_progress': "OCR روان دی",
        'ocr_preparing': "PDF چمتو کېږي...",
        'ocr_analyzing': "PDF تحلیل کېږي...",
        'ocr_optimizing': "انځور اصلاح کېږي...",
        'ocr_recognizing': "متن پېژندل کېږي...",
        'ocr_embedding': "متن ځای پر ځای کېږي...",
        'ocr_finalizing': "PDF نهايي کېږي...",
        'ocr_not_available': "OCR شتون نلري",
        'ocr_install_message': "د OCR وسایل و نه موندل شول.\n\nلطفاً نصب یې کړئ:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR اړین دی",
        'ocr_question': "په PDF کې د لټون وړ متن نشته.\nآیا غواړئ OCR ترسره کړئ ترڅو {0} فعال شي؟",
        'ocr_perform': "OCR ترسره کړئ",
        'ocr_later': "وروسته",
        'ocr_starting': "ضمانت شوی OCR پیلېږي...",
        'ocr_success_voice': "OCR بریالی شو. PDF اوس د لټون وړ دی.",
        'ocr_partial_success': "OCR ترسره شو، خو په بدلولو کې ستونزه وه.\n\nد لټون وړ نسخه دلته خوندي شوه:\n{0}\n\nتېروتنه: {1}",
        'ocr_partial_title': "OCR بریالی شو خو نیمګړی",
        'ocr_partial_voice': "OCR ترسره شو، خو بدلون ناکام شو.",
        'original_file': "اصلي فایل:",
        'old_size': "زوړ اندازه:    {0} بایټ",
        'new_size': "نوې اندازه: {0} بایټ",
        'size_change': "بدلون: {0}{1} بایټ",
        'backup_created_file': "بیک اپ جوړ شو:\n{0}",
        'backup_not_created': "بیک اپ: نه دی جوړ شوی (تنظیم غیر فعال دی)",
        'page_header': "=== مخ {0} ===\n{1}\n",
        'scanned_page_header': "=== مخ {0} (سکین شوی) ===\n[دا مخ یوازې سکین شوی متن لري]\n[لطفاً په لاسي ډول OCR وکړئ]\n",
        'scanned_warning': "⚠️ سکین شوی متن - OCR اړین دی",
        'guaranteed_title': "د لټون وړ PDF جوړ شو",
        'guaranteed_message': "<b>ضمانت شوی د لټون وړ نسخه جوړه شوه!</b>\n\nڅرنګه چې اتوماتیک OCR ناکام شو، یو بدیل د لټون وړ PDF جوړه شوه:\n\n{0}\n\n<b>دا فایل لري:</b>\n• استخراج شوی متن (که شتون ولري)\n• د سکین شویو مخونو لپاره لارښوونې\n• په بشپړه توګه د لټون وړ",
        'guaranteed_voice': "ضمانت شوی د لټون وړ PDF جوړه شوه.",
        'instruction_title': "د OCR لپاره لارښود",
        'instruction_file': "اصلي فایل: {0}",
        'instruction_text': "اتوماتیک متن پېژندنه (OCR) ناکامه شوه.\nلطفاً په لاسي ډول OCR ترسره کړئ:\n\n1. د OCRmyPDF سره (کمانډ لاین):\n   ocrmypdf --force-ocr \"[فایل]\" \"output.pdf\"\n\n2. د ADOBE ACROBAT سره (macOS/Windows):\n   • PDF په Acrobat کې پرانیزئ\n   • وسایل > PDF سمول\n   • 'متن پېژندنه' غوره کړئ\n\n3. د PREVIEW سره (macOS):\n   • PDF په Preview کې پرانیزئ\n   • فایل > صادرول...\n   • د Quartz فلټر: 'د فایل اندازه کم کړئ'\n   • 'OCR ترسره کړئ' فعال کړئ\n\n4. آنلاین OCR خدمتونه:\n   • smallpdf.com/ps/ocr-pdf\n   • ilovepdf.com/ps/ocr-pdf\n   • adobe.com/af/acrobat/online/pdf-to-word.html",
        'instruction_created': "د OCR لارښود جوړ شو",
        'instruction_created_message': "یو تفصیلي لارښود جوړ شو:\n\n{0}\n\nلطفاً د لاسي OCR لپاره ګامونه تعقیب کړئ.",
        'instruction_created_voice': "د OCR لارښود جوړ شو.",
        'ocr_impossible': "OCR ممکن نه دی",
        'ocr_impossible_message': "OCR ترسره کېدلای نه شي.\n\nلطفاً د '{0}' په لاسي ډول د OCR سافټویر سره پروسس کړئ.",
        'ocr_impossible_voice': "OCR ممکن نه دی. لطفاً په لاسي ډول پروسس کړئ.",
        'emergency_title': "بیړنی OCR",
        'emergency_message': "یو بیړنی PDF جوړ شو:\n\n{0}\n\nلطفاً دا فایل په لاسي ډول د OCR سره پروسس کړئ.",
        'emergency_voice': "بیړنی PDF جوړ شو. لطفاً په لاسي ډول OCR ترسره کړئ.",
        'critical_error': "جدي تېروتنه",
        'critical_error_message': "OCR پیل کېدلای نه شي.\n\nلطفاً برنامه بیا پیل کړئ او د OCR نصب وګورئ.",
        'critical_error_voice': "د OCR جدي تېروتنه",
        'ocr_question_html': "<p>په PDF کې د لټون وړ متن نشته.<p>آیا غواړئ OCR ترسره کړئ ترڅو <b>{0}</b> فعال شي؟</p>",
        'ocr_question_voice': "OCR اړین دی. PDF د لټون وړ متن نلري. آیا غواړئ OCR ترسره کړئ ترڅو {0} فعال شي؟",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "هېڅ PDF نه دی بار شوی",
        'no_pdf_message': "هېڅ PDF نه دی بار شوی",
        'pdf_not_found': "د PDF فایل و نه موندل شو",
        'file_size': "د فایل اندازه",
        'bytes': "بایټ",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "بیک اپ جوړ شو",
        'backup_disabled': "بیک اپ غیر فعال دی",
        'backup_activated': "د بیک اپ جوړول فعال شول",
        'backup_deactivated': "د بیک اپ جوړول غیر فعال شول",
        'backup_status': "بیک اپ: {0}",
        'backup_on': "✔ فعال",
        'backup_off': "✘ غیر فعال",
        'close_pdf': "PDF تړل کېږي: {0}",
        'pdf_not_found_format': "د PDF فایل و نه موندل شو: {0}",
        'error_pdf_load_format': "د PDF بارولو کې تېروتنه: {0}",
        'load_failed_format': "بارول ناکام شول:\n{0}",
        'decrypted_suffix': "(کوډ شوی خلاص شو)",
        'decryption_failed': "کوډ خلاصول ناکام شول.",
        'decryption_error': "د کوډ خلاصولو کې تېروتنه",
        'decryption_success': "په بریالیتوب سره کوډ خلاص شو",
        'decryption_success_message': "PDF کوډ خلاص شو او دلته خوندي شو:\n\n{0}",
        'decryption_success_voice': "PDF کوډ خلاص شو او خوندي شو.",
        'password_remove_error': "د پټ نوم لرې کولو کې تېروتنه",
        'save_unencrypted': "بې کوډه PDF دې توګه خوندي کړئ",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "دې توګه خوندي کړئ...",
        'save_copy': "یوه کاپي خوندي کړئ",
        'save_success': "PDF دلته خوندي شو: {0}",
        'save_encrypted': "خوندي شوی PDF دلته خوندي شو: {0}",
        'save_error': "PDF خوندي کېدلای نه شي",
        'encryption_question': "آیا غواړئ PDF د پټ نوم سره خوندي کړئ؟",
        'encryption_yes': "هو",
        'encryption_no': "نه",
        'encryption_cancel': "لغوه کړئ",
        'save_cancel': "خوندي کول لغوه شول",
        'save_encrypted_voice': "فایل کوډ شو او خوندي شو.",
        'save_success_voice': "د PDF فایل بې کوډه خوندي شو.",
        'save_error_format': "PDF خوندي کېدلای نه شي:\n{0}",
        'export_pages_success': "Pages صادرول بریالي شول",
        'export_pages_error': "Pages صادرول ناکام شول",
        'export_pages_error_format': "Pages صادرول ناکام شول: {0}",
        'export_word_success': "Word صادرول بریالي شول",
        'export_word_error': "Word صادرول ناکام شول",
        'export_word_error_format': "Word صادرول ناکام شول: {0}",
        'export_text_success': "متن صادرول بریالي شول",
        'export_text_error': "متن صادرول ناکام شول",
        'export_text_error_format': "متن صادرول ناکام شول: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "پټ نوم اړین دی",
        'password_enter': "لطفاً پټ نوم دننه کړئ",
        'password_confirm': "پټ نوم تایید کړئ",
        'password_new': "نوی پټ نوم",
        'password_current': "اوسنی پټ نوم",
        'password_save': "پټ نوم خوندي کړئ (کوډ شوی)",
        'password_saved': "✓ د دې فایل لپاره پټ نوم خوندي شو",
        'password_wrong': "پټ نوم غلط دی",
        'password_mismatch': "پټ نومونه سره برابر نه دي",
        'password_too_short': "پټ نوم ډېر لنډ دی",
        'password_min_length': "پټ نوم لږ تر لږه ۴ توري اوږد وي",
        'password_strength': "د پټ نوم ځواک",
        'password_strength_very_weak': "ډېر کمزوری",
        'password_strength_weak': "کمزوری",
        'password_strength_medium': "منځنی",
        'password_strength_strong': "پیاوړی",
        'password_strength_very_strong': "ډېر پیاوړی",
        'password_char_count': "({0} توري)",
        'password_match': "✓ سره برابر دی",
        'password_no_match': "✗ پټ نومونه سره برابر نه دي",
        'password_show': "ښکاره کړئ",
        'password_hide': "پټ کړئ",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "د پټ نوم مدیریت",
        'password_table_filename': "د فایل نوم",
        'password_table_password': "پټ نوم",
        'password_count': "{0} پټ نومونه خوندي شوي",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "هېڅ پټ نوم نه دی خوندي شوی",
        'password_copied': "{0} پټ نومونه کاپي شول",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "آیا تاسو ډاډه یاست چې غواړئ د '{0}' لپاره پټ نوم ړنګ کړئ؟",
        'password_delete_multiple': "آیا تاسو ډاډه یاست چې غواړئ ټاکل شوي {0} پټ نومونه ړنګ کړئ؟",
        'password_delete_all_confirm': "آیا تاسو ډاډه یاست چې غواړئ ټول {0} خوندي شوي پټ نومونه ړنګ کړئ؟",
        'password_deleted': "{0} پټ نومونه ړنګ شول",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "ټول پټ نومونه ړنګ شول",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "د پټ نوم جوړونکی",
        'generator_generated': "جوړ شوی پټ نوم:",
        'generator_regenerate': "بیا جوړ کړئ",
        'generator_copy': "کاپي کړئ",
        'generator_use': "وکاروئ",
        'generator_settings': "تنظیمات",
        'generator_length': "اوږدوالی:",
        'generator_group_every': "هر",
        'generator_group_chars': "توري یو جلا کوونکی. جلا کوونکی:",
        'generator_uppercase': "لوی توري (A-Z)",
        'generator_lowercase': "وړوکي توري (a-z)",
        'generator_digits': "شمېرې (0-9)",
        'generator_symbols': "ځانګړي نښانې (!@#$%^&*)",
        'generator_exclude': "نه شاملول:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "ماسټر پټ نوم اړین دی",
        'master_password_setup': "ماسټر پټ نوم تنظیم کړئ",
        'master_password_change': "ماسټر پټ نوم بدل کړئ",
        'master_password_enter': "لطفاً خپل ماسټر پټ نوم دننه کړئ",
        'master_password_choose': "یو پیاوړی ماسټر پټ نوم وټاکئ (لږ تر لږه ۸ توري)",
        'master_password_new': "لطفاً خپل نوی ماسټر پټ نوم دننه کړئ",
        'master_password_confirm': "پټ نوم تایید کړئ",
        'master_password_authenticate': "تصدیق کړئ",
        'master_password_success': "ماسټر پټ نوم په بریالیتوب سره تنظیم شو.",
        'master_password_changed': "ماسټر پټ نوم په بریالیتوب سره بدل شو.",
        'master_password_removed': "ماسټر پټ نوم او ټول پټ نومونه لرې شول.",
        'master_password_remove': "ماسټر پټ نوم لرې کړئ",
        'master_password_remove_confirm': "آیا تاسو ډاډه یاست چې غواړئ ټول پټ نومونه ړنګ کړئ؟\n\nدا کړنه بېرته نه راګرځېدونکې ده!",
        'master_password_export_before': "آیا غواړئ مخکې بیک اپ صادر کړئ؟",
        'master_password_export_delete': "صادر کړئ او ړنګ کړئ",
        'master_password_delete_now': "همدا اوس ړنګ کړئ",
        'master_password_for_signatures': "د لاسلیک کارولو لپاره، تاسو باید یو ماسټر پټ نوم تنظیم کړئ.\n\nآیا غواړئ همدا اوس ماسټر پټ نوم تنظیم کړئ؟",
        'master_password_for_private': "د شخصي متن بلاکونو کارولو لپاره، تاسو باید یو ماسټر پټ نوم تنظیم کړئ.\n\nآیا غواړئ همدا اوس ماسټر پټ نوم تنظیم کړئ؟",
        'master_password_info': """
            <b>🔐 د ماسټر پټ نوم پرته:</b><br>
            • د پټ نومونو ښودل، کاپي کول او صادرول ممکن نه دي<br>
            • د پټ نومونو ړنګول تل ممکن دي (حتی د ماسټر پټ نوم پرته)<br><br>

            <b>🔐 د ماسټر پټ نوم سره:</b><br>
            • د تصدیق وروسته ټولې دندې شتون لري<br>
            • پټ نومونه د ماسټر پټ نوم سره کوډ کېږي<br>
            • لږ تر لږه اوږدوالی: ۸ توري<br>
            • د SHA-256 هش خوندي زېرمه<br><br>

            <b>مهم:</b><br>
            • د ماسټر پټ نوم هېرولو سره: پټ نومونه بېرته نه موندل کېږي<br>
            • د ماسټر پټ نوم لرې کولو سره: ټول پټ نومونه ړنګېږي<br>
            • د ړنګولو دمخه د صادرولو اختیار شتون لري<br>
            • ماسټر پټ نوم هر وخت بدلېدای شي
        """,
        'signature_auth_disabled': "د لاسلیکونو لپاره د پټ نوم پوښتنه غیر فعال کړئ",
        'template_auth_disabled': "د شخصي متن بلاکونو لپاره د پټ نوم پوښتنه غیر فعال کړئ",
        'master_password_for_signatures_settings': "د لاسلیک کارولو لپاره، تاسو باید یو ماسټر پټ نوم تنظیم کړئ.\n\nتنظیمات - د پټ نوم مدیریت ته لاړ شئ",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF خوندي کړئ",
        'protect_info': "فایل '{0}' به د پټ نوم سره خوندي شي.",
        'protect_instruction': "لطفاً د سند خوندي کولو لپاره غوښتل شوی پټ نوم دوه ځله دننه کړئ، یا د ننوتنې ساحې ښي خوا ته د پټ نوم جوړونکی وکاروئ.",
        'protect_success': "PDF په بریالیتوب سره خوندي شو او دلته خوندي شو:\n{0}\n\nپټ نوم: {1}\n\nآیا غواړئ خوندي شوی PDF همدا اوس پرانیزئ؟",
        'protect_open': "هو",
        'protect_skip': "نه",
        'protect_error': "د PDF خوندي کولو کې تېروتنه",
        'protect_open_title': "خوندي شوی PDF پرانیزئ",
        'protect_question': "ترسره شو. آیا غواړئ خوندي شوی PDF همدا اوس پرانیزئ؟ هو یا نه؟",
        'password_cancel': "د پټ نوم کړکۍ لغوه شوه",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "مخونه ړنګ کړئ",
        'pages_extract': "مخونه استخراج کړئ",
        'pages_insert': "مخونه ورزیات کړئ",
        'pages_move': "مخونه ولېږدوئ",
        'pages_delete_options': "د ړنګولو اختیارونه",
        'pages_delete_empty': "ټول خالي مخونه ړنګ کړئ",
        'pages_delete_current': "اوسنی مخ ړنګ کړئ",
        'pages_delete_range': "د مخونو سلسله ړنګ کړئ",
        'pages_extract_options': "د استخراج اختیارونه",
        'pages_extract_current': "اوسنی مخ استخراج کړئ",
        'pages_extract_range': "د مخونو سلسله استخراج کړئ",
        'pages_insert_position': "د ورزیاتولو ځای",
        'pages_insert_before': "د مخ څخه مخکې ورزیات کړئ:",
        'pages_insert_select': "PDF وټاکئ",
        'pages_insert_none': "هېڅ PDF نه دی ټاکل شوی",
        'pages_move_source': "د لېږدولو لپاره مخونه",
        'pages_move_from': "له مخ:",
        'pages_move_to': "تر مخ پورې:",
        'pages_move_target': "هدف ځای",
        'pages_move_before': "د مخ څخه مخکې ولېږدوئ:",
        'pages_move_hint': "یادونه: مخ ۱ = پیل، {0} = پای",
        'pages_range_invalid': "پیل مخ باید د پای مخ څخه کوچنی یا برابر وي.",
        'pages_position_invalid': "هدف ځای باید د لېږدول کېدونکي سلسلې دننه نه وي.",
        'pages_no_pdf_selected': "هېڅ PDF نه دی ټاکل شوی.",
        'pages_deleted': "{0} مخونه ړنګ شول.",
        'pages_extracted': "استخراج شوی: {0}\nخوندي شوی ځای: {1}\nد فایل اندازه: {2:.1f} KB",
        'pages_inserted': "{0} مخونه ورزیات شول",
        'pages_moved': "{0} مخونه ولېږدول شول.",
        'pages_deleted_none': "هېڅ مخ و نه ړنګ شو.",
        'pages_delete_progress': "مخونه ړنګېږي...",
        'pages_deleted_with_backup': "{0} مخونه ړنګ شول.\n\nبیک اپ: {1}",
        'pages_deleted_voice': "بیک اپ جوړ شو او {0} مخونه ړنګ شول.",
        'info': "یادونه",
        'error_dialog_creation': "کړکۍ نشي جوړېدای",
        'extract_page_single': "مخ {0} استخراج کړئ",
        'extract_page_range': "مخونه {0}-{1} استخراج کړئ",
        'extract_success_voice': "مخونه په بریالیتوب سره استخراج شول",
        'extract_error_format': "د استخراج پرمهال تېروتنه: {0}",
        'pages_inserted_voice': "{0} مخونه ورزیات شول.",
        'insert_error_format': "د ورزیاتولو پرمهال تېروتنه: {0}",
        'pages_move_progress': "مخونه لېږدول کېږي...",
        'pages_moved_with_backup': "{0} مخونه ولېږدول شول.\n\nبیک اپ: {1}",
        'move_success_title': "په بریالیتوب سره ولېږدول شو",
        'pages_moved_voice': "{0} مخونه په بریالیتوب سره ولېږدول شول",
        'mark_removed': "د مخ {0} نښه لرې شوه",
        'mark_empty': "مخ {0} د خالي په توګه ونښه شو",
        'mark_export_removed': "د مخ {0} د صادرولو نښه لرې شوه",
        'mark_export': "مخ {0} د صادرولو لپاره ونښه شو",
        'no_empty_pages': "د ړنګولو لپاره هېڅ خالي مخ نه دی نښه شوی",
        'delete_empty_confirm': "آیا غواړئ ټول {0} نښه شوي خالي مخونه ړنګ کړئ؟",
        'delete_empty_confirm_voice': "همدا اوس ټول {0} نښه شوي خالي مخونه ړنګ کړم؟ هو یا نه.",
        'empty_pages_deleted': "{0} خالي مخونه ړنګ شول",
        'no_export_pages': "د صادرولو لپاره هېڅ مخ نه دی نښه شوی",
        'overwrite_title': "اوسنی فایل له سره ولیکئ",
        'overwrite_question': "فایل\n\n{0}\n\nپخوا شتون لري.\nآیا غواړئ هغه له سره ولیکئ؟",
        'overwrite_voice': "اوسنی فایل له سره ولیکئ؟ هو یا نه.",
        'page_skipped': "مخ {0} پرېښودل شو",
        'export_complete': "صادرول بشپړ شول.",
        'export_complete_voice': "صادرول بشپړ شول.",
        'no_pages_exported': "هېڅ مخ و نه صادر شو",
        'export_cancelled': "صادرول لغوه شول",
        'pages_exported': "{0} مخونه {1} ته صادر شول",
        'export_page_title': "مخ صادر کړئ",
        'page_exported': "مخ {0} {1} ته صادر شو",
        'export_error': "د صادرولو پرمهال تېروتنه",
        'export_marked_title': "نښه شوي مخونه صادر کړئ",
        'rotate_all_title': "ټول مخونه وګرځوئ",
        'rotate_all_question': "آیا غواړئ ټول مخونه ۹۰ درجې ښي خوا ته وګرځوئ؟",
        'rotate_all_voice': "آیا غواړئ ټول مخونه ۹۰ درجې ښي خوا ته وګرځوئ؟ هو یا نه؟",
        'all_pages_rotated': "ټول مخونه وګرځول شول",
        'page_rotated': "مخ {0} وګرځول شو",
        'rotate_error': "مخ نشي ګرځېدای",
        'delete_page_confirm': "آیا غواړئ مخ {0} ړنګ کړئ؟",
        'delete_page_confirm_voice': "آیا تاسو ډاډه یاست چې غواړئ مخ {0} ړنګ کړئ؟ هو یا نه.",
        'page_deleted': "مخ {0} ړنګ شو",
        'delete_error': "مخ نشي ړنګېدای",
        'pages_deleted_voice': "{0} مخونه ړنګ شول",
        'pages_exported_split': "{0} مخونه په بریالیتوب سره صادر شول.",
        'pages_skipped': "{0} مخونه پرېښودل شول.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "مخونه استخراج کړئ (پرمختللی)",
        'pdf_splitter_title': "PDF وېشونکی او استخراجونکی",
        'pdf_splitter_load': " د PDF فایل وټاکئ",
        'pdf_splitter_info': "لطفاً د خپل PDF سند لپاره یو اختیار وټاکئ",
        'pdf_splitter_basic': "اساسي عملیات",
        'pdf_splitter_single': "په جلا جلا مخونو وېشئ",
        'pdf_splitter_range': "مخونه استخراج کړئ:",
        'pdf_splitter_range_placeholder': "د مثال په توګه 1-3,5,7-9",
        'pdf_splitter_clean': "پاکولو عملیات",
        'pdf_splitter_remove_empty': "ټول خالي مخونه لرې کړئ",
        'pdf_splitter_remove': "د مخونو سلسله ړنګ کړئ:",
        'pdf_splitter_remove_placeholder': "د مثال په توګه 2,4-6",
        'pdf_splitter_process': "PDF پروسس کړئ",
        'pdf_splitter_loaded': "PDF بار شو. لطفاً یو اختیار وټاکئ",
        'pdf_read_error': "PDF نشي لوستل کېدای",
        'pages': "مخونه",
        'pages_created': "مخونه جوړ شول",
        'range_empty': "لطفاً د مخونو سلسله دننه کړئ",
        'range_invalid': "د مخونو سلسله ناسمه ده",
        'range_created': "د ټاکل شویو مخونو سره نوې PDF جوړه شوه:\n{0}",
        'empty_removed': "{0} خالي مخونه لرې شول.\nپایله: {1}",
        'remove_empty': "لطفاً د لرې کولو لپاره مخونه دننه کړئ",
        'remove_invalid': "د لرې کولو لپاره ناسم مخونه",
        'remove_done': "پاکه شوې PDF جوړه شوه:\n{0}",
        'open_folder': "فولډر پرانیزئ",
        'show_in_finder': "په Finder کې وښایاست",
        'pdf_splitter_no_pdf': "لطفاً لومړی یو د PDF فایل بار کړئ.",
        'process_error': "د PDF پروسس کولو کې تېروتنه",
        'pages_created_voice': "{0} مخونه جوړ شول",
        'range_created_voice': "د ټاکل شویو مخونو سره PDF جوړه شوه",
        'empty_removed_voice': "{0} خالي مخونه لرې شول",
        'remove_done_voice': "پاکه شوې PDF جوړه شوه",
        'pdf_splitter_split_groups': "هره نښلېدونکې ډله په جلا فایل کې",
        'range_created_single': "نوې PDF جوړه شوه:\n{0}",
        'range_created_multiple': "{0} د PDF فایلونه جوړ شول.",
        'range_created_voice_single': "د ټاکل شویو مخونو سره یوه PDF جوړه شوه",
        'range_created_voice_multiple': "{0} د PDF فایلونه جوړ شول",
        'empty_removed_none_left': "هېڅ مخ پاتې نه شو",
        'empty_removed_all_empty': "ټول مخونه خالي وپېژندل شول او لرې به شي. هېڅ فایل و نه جوړ شو.",
        'preview_single': "مخکتنه: {0}",
        'preview_enter_range': "لطفاً د مخونو سلسله دننه کړئ.",
        'preview_invalid_range': "د مخونو سلسله ناسمه ده.",
        'preview_file': "مخکتنه: {0}",
        'preview_files': "مخکتنه: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "چاپ پیل کړئ",
        'print_sent': "د چاپ دنده واستول شوه",
        'print_now': "همدا اوس چاپ کړئ",
        'print_error': "د سمدستي چاپ پرمهال تېروتنه",
        'print_limited': "په دې سیسټم کې د چاپ دنده محدوده ده",
        'print_error_format': "د سمدستي چاپ پرمهال تېروتنه: {0}",
        'warning': "خبرداری",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "روښانه حالت ته واړوئ",
        'mode_switch_to_dark': "تیاره حالت ته واړوئ",
        'mode_dark_activated': "تیاره حالت فعال شو",
        'mode_light_activated': "روښانه حالت فعال شو",

        # ============================================
        # 17. ZOOM-MODI (Fortsetzung)
        # ============================================
        'zoom_exit_first': "لطفاً لومړی له لویولو وتئ",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "کشول او غورځول فعال شو",
        'drag_disabled': "کشول او غورځول غیر فعال شو",
        'drag_page_grab': "مخ {0} نیول کېږي",
        'drag_page_dropped': "مخ {0} په {1} موقعیت کې ځای پر ځای شو",
        'drag_position_invalid': "ناسم موقعیت",
        'drag_same_position': "مخ {0} په خپل {0} موقعیت پاتې شو",
        'drag_error': "د لېږدولو پرمهال تېروتنه",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "د متن داخلول د پرمختللي بڼې جوړونې او د متن بلاک مدیریت سره",
        'text_templates': "شته متن بلاکونه:",
        'text_name': "نوم",
        'text_preview': "د متن مخکتنه",
        'text_enter': "متن:",
        'text_font_size': "د فونټ اندازه:",
        'text_formatting': "بڼه جوړونه:",
        'text_bold': "غټ",
        'text_italic': "رېوند",
        'text_underline': "کرښه لاندې",
        'text_alignment': "سمون:",
        'text_left': "کیڼ",
        'text_center': "منځ",
        'text_right': "ښي",
        'text_color': "د متن رنګ:",
        'text_opacity': "تیتوالی:",
        'text_word_wrap': "د کرښې ماتول:",
        'text_auto': "اتوماتیک",
        'text_page_width_95': "د مخ پلنوالی (۹۵٪)",
        'text_page_width_85': "ډېر پلن (۸۵٪)",
        'text_page_width_75': "پلن (۷۵٪)",
        'text_page_width_60': "پلن (۶۰٪)",
        'text_page_width_50': "منځنی (۵۰٪)",
        'text_page_width_30': "تنګ (۳۰٪)",
        'text_page_width_20': "ترهغه تنګ (۲۰٪)",
        'text_page_width_10': "ډېر تنګ (۱۰٪)",
        'text_no_wrap': "بې کرښې ماتولو",
        'text_private': "شخصي متن بلاک (تصدیق ته اړتیا ده)",
        'text_preview_label': "مخکتنه:",
        'text_preview_placeholder': "د متن مخکتنه به دلته ښودل شي...",
        'text_no_text': "(متن نشته)",
        'text_save_template': "💾 د بلاک په توګه خوندي کړئ",
        'text_delete_template': "🗑 ټاکل شوی متن بلاک ړنګ کړئ",
        'text_show_private': "شخصي ښکاره کړئ",
        'text_hide_private': "شخصي پټ کړئ",
        'text_use': "✅ متن وکاروئ",
        'text_saved': "متن بلاک د دې په توګه خوندي شو:\n{0}",
        'text_saved_voice': "متن بلاک خوندي شو",
        'text_deleted': "متن بلاک ړنګ شو",
        'text_no_text_to_save': "د خوندي کولو لپاره متن نشته.",
        'text_no_templates': "هېڅ متن بلاک و نه موندل شو",
        'text_private_master_required': "شخصي بلاکونه یوازې هغه وخت کارېدای شي چې ماسټر پټ نوم تنظیم شوی وي.\n\nآیا غواړئ همدا اوس ماسٴتر پټ نوم تنظیم کړئ؟",
        'text_filename': "د متن بلاک لپاره د فایل نوم (د 'Text_' او '.txt' پرته):",
        'text_filename_hint': "بېلګه: 'کورنی تلیفون' به د 'Text_کورنی تلیفون.txt' په توګه خوندي شي",
        'text_save_hint': "متن بلاک به د بڼې جوړونې سره یوځای اتومات خوندي شي.",
        'text_guide_title': "د متن داخلول - لارښود",
        'text_delete_confirm': "آیا تاسو ډاډه یاست چې غواړئ دا متن بلاک ړنګ کړئ؟\n\nفایل: {0}\nمتن: {1}...",
        'text_make_public': "د عامه په توګه ونښه کړئ",
        'text_make_private': "د شخصي په توګه ونښه کړئ",
        'text_privacy_changed': "شخصیت بدل شو",
        'text_private_always': "شخصي تل ښکاره (تنظیم)",
        'text_mode_required': "لطفاً لومړی د متن حالت فعال کړئ",
        'text_continue_editing': "سمون ته دوام ورکړئ - کرسر د متن په پای کې دی",
        'text_no_input': "هېڅ متن و نه داخل شو - متن رد شو",
        'save_dialog_question': "تاسو څنګه ادامه ورکول غواړئ؟",
        'text_save_question': "ټول متنونه او صلیبونه خوندي کړئ، تنظیم یې کړئ، سمون ته دوام ورکړئ یا رد یې کړئ؟",
        'copy_cross': "صلیب کاپي شو",
        'paste_cross': "صلیب چاپ شو",
        'paste_text': "متن چاپ شو",
        'cross_discarded': "صلیب رد شو",
        'all_discarded': "ټول رد شول",
        'text_discarded': "متن رد شو",
        'no_texts_to_save': "د خوندي کولو لپاره هېڅ متن نشته",
        'no_valid_texts': "د خوندي کولو لپاره هېڅ سم متن نشته",
        'text_word_singular': "متن",
        'text_word_plural': "متنونه",
        'cross_word_singular': "صلیب",
        'cross_word_plural': "صلیبونه",
        'texts_saved_title': "متنونه خوندي شول",
        'texts_crosses_saved': "{0} {1} او {2} {3} PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'texts_crosses_saved_voice': "{0} {1} او {2} {3} خوندي شول.",
        'texts_saved': "{0} {1} PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'texts_saved_voice': "{0} {1} خوندي شول.",
        'crosses_saved': "{0} {1} PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'crosses_saved_voice': "{0} {1} خوندي شول.",
        'elements_saved': "{0} عناصر PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'elements_saved_voice': "{0} عناصر خوندي شول.",
        'text_window_load_error': "د متن کړکۍ نشي بارېدای",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **د متن داخلول او متن بلاکونه – تفصیلي لارښود**

        **۱. متن داخلول او سمول**
        - په سند کې په مطلوب ځای کې ښی کلیک وکړئ او "متن داخل کړئ" وټاکئ.
        - یوه کړکۍ به پرانیزي چېرته چې تاسو خپل متن داخلولای شئ او بڼه یې جوړولای شئ:
        • د فونټ اندازه، غټ، رېوند، کرښه لاندې
        • د متن رنګ (په خپله خوښه غوره کېدای شي)
        • تیتوالی (د سلایډر په مرسته)
        • د کرښې ماتول (بېلابېل پلنوالی، لکه د مخ پلنوالی، تنګ، بې کرښې ماتولو)
        - د تایید وروسته، متن به د کلیک شوي ځای کې ښکاره شي. تاسو کولای شئ د موږک یا تیر تڼیو په مرسته یې وخوځوئ.
        - په متن دوه ځله کلیک کول د سمون حالت پرانیزي؛ د ESC تڼۍ سره وځئ.

        **۲. د متن بلاکونو (ټېمپلیټونو) مدیریت**
        - د متن کړکۍ کې، تاسو به په کیڼ اړخ کې د ټولو خوندي شویو متن بلاکونو لړلیک وینئ.
        - **بلاک خوندي کول:** خپل متن دننه کړئ، بڼه یې جوړه کړئ او "💾 د بلاک په توګه خوندي کړئ" کلیک وکړئ. یو د فایل نوم دننه کړئ (د پسوند پرته).
        - **بلاک بارول:** په لړلیک کې په مطلوب نوم کلیک وکړئ. متن او بڼه به پلی شي او که اړتیا وي، تنظیمېدای شي.
        - **ړنګول:** په یو بلاک ښی کلیک کولو سره تاسو کولای شئ هغه ړنګ کړئ یا د هغه شخصیت بدل کړئ.

        **۳. شخصي متن بلاکونه (ماسټر پټ نوم)**
        - که تاسو ماسټر پټ نوم تنظیم کړی وي (د تنظیماتو → د پټ نوم مدیریت لاندې)، تاسو کولای شئ بلاکونه د "شخصي" په توګه ونښه کړئ.
        - د دې لپاره، د خوندي کولو دمخه په کړکۍ کې "شخصي متن بلاک" بکس ټیک کړئ.
        - شخصي بلاکونه به یوازې هغه وخت په لړلیک کې ښکاره شي چې تاسو یو ځل په هر ناسته کې خپل ماسټر پټ نوم دننه کړی وي (د تالۍ نښې له لارې یا د لومړي لاسرسي پرمهال تصدیق).
        - په دې توګه تاسو کولای شئ محرم متن بلاکونه د نورو لاسرسي څخه وساتئ.

        **۴. صلیب داخلول**
        - د شرایطو مینو له لارې، تاسو کولای شئ یو ګرافیکي صلیب (د بېلګې په توګه د چکبکس لپاره) هم داخل کړئ.
        - د صلیب اندازه، د کرښې ټوپوالی او رنګ د تنظیماتو کې نړیوال ډول تنظیمېدای شي (مینو "تنظیمات" → "د صلیب تنظیمات").
        - په یو موجود صلیب ښی کلیک کولو سره تاسو کولای شئ هغه په جلا توګه بدل کړئ.

        **۵. ډله‌ییز کړنې**
        - که تاسو په یوه مخ کې ګڼ شمېر متنونه یا صلیبونه ځای پر ځای کړي وي، تاسو کولای شئ د شرایطو مینو له لارې (د متن حالت کې ښی کلیک) ټول عناصر یوځای خوندي یا رد کړئ.
        - د خوندي کولو پرمهال، ټول عناصر به PDF کې ځای پر ځای شي او د ویکټور ګرافیک په توګه پاتې شي.

        **۶. د متن حالت کې د کیبورډ شارټ کټونه**
        - تیر تڼۍ: عنصر خوځوئ
        - Ctrl+تیر تڼۍ: لوی ګامونو سره خوځوئ
        - Enter: د خوندي کولو کړکۍ پرانیزئ (ټول خوندي کړئ / تنظیم یې کړئ / رد یې کړئ)
        - ESC: اوسنی عنصر رد کړئ
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 د متن داخلول او متن بلاکونه – تفصیلي لارښود</strong></p>

        <p><strong>۱. متن داخلول او سمول</strong></p>
        <ul>
        <li>په سند کې په مطلوب ځای کې ښی کلیک وکړئ او "متن داخل کړئ" وټاکئ.</li>
        <li>یوه کړکۍ به پرانیزي چېرته چې تاسو خپل متن داخلولای شئ او بڼه یې جوړولای شئ:<br/>
        • د فونټ اندازه، غټ، رېوند، کرښه لاندې<br/>
        • د متن رنګ (په خپله خوښه غوره کېدای شي)<br/>
        • تیتوالی (د سلایډر په مرسته)<br/>
        • د کرښې ماتول (بېلابېل پلنوالی، لکه د مخ پلنوالی، تنګ، بې کرښې ماتولو)</li>
        <li>د تایید وروسته، متن به د کلیک شوي ځای کې ښکاره شي. تاسو کولای شئ د موږک یا تیر تڼیو په مرسته یې وخوځوئ.</li>
        <li>په متن دوه ځله کلیک کول د سمون حالت پرانیزي؛ د ESC تڼۍ سره وځئ.</li>
        </ul>

        <p><strong>۲. د متن بلاکونو (ټېمپلیټونو) مدیریت</strong></p>
        <ul>
        <li>د متن کړکۍ کې، تاسو به په کیڼ اړخ کې د ټولو خوندي شویو متن بلاکونو لړلیک وینئ.</li>
        <li><strong>بلاک خوندي کول:</strong> خپل متن دننه کړئ، بڼه یې جوړه کړئ او "💾 د بلاک په توګه خوندي کړئ" کلیک وکړئ. یو د فایل نوم دننه کړئ (د پسوند پرته).</li>
        <li><strong>بلاک بارول:</strong> په لړلیک کې په مطلوب نوم کلیک وکړئ. متن او بڼه به پلی شي او که اړتیا وي، تنظیمېدای شي.</li>
        <li><strong>ړنګول:</strong> په یو بلاک ښی کلیک کولو سره تاسو کولای شئ هغه ړنګ کړئ یا د هغه شخصیت بدل کړئ.</li>
        </ul>

        <p><strong>۳. شخصي متن بلاکونه (ماسټر پټ نوم)</strong></p>
        <ul>
        <li>که تاسو ماسټر پټ نوم تنظیم کړی وي (د تنظیماتو → د پټ نوم مدیریت لاندې)، تاسو کولای شئ بلاکونه د "شخصي" په توګه ونښه کړئ.</li>
        <li>د دې لپاره، د خوندي کولو دمخه په کړکۍ کې "شخصي متن بلاک" بکس ټیک کړئ.</li>
        <li>شخصي بلاکونه به یوازې هغه وخت په لړلیک کې ښکاره شي چې تاسو یو ځل په هر ناسته کې خپل ماسټر پټ نوم دننه کړی وي (د تالۍ نښې له لارې یا د لومړي لاسرسي پرمهال تصدیق).</li>
        <li>په دې توګه تاسو کولای شئ محرم متن بلاکونه د نورو لاسرسي څخه وساتئ.</li>
        </ul>

        <p><strong>۴. صلیب داخلول</strong></p>
        <ul>
        <li>د شرایطو مینو له لارې، تاسو کولای شئ یو ګرافیکي صلیب (د بېلګې په توګه د چکبکس لپاره) هم داخل کړئ.</li>
        <li>د صلیب اندازه، د کرښې ټوپوالی او رنګ د تنظیماتو کې نړیوال ډول تنظیمېدای شي (مینو "تنظیمات" → "د صلیب تنظیمات").</li>
        <li>په یو موجود صلیب ښی کلیک کولو سره تاسو کولای شئ هغه په جلا توګه بدل کړئ.</li>
        </ul>

        <p><strong>۵. ډله‌ییز کړنې</strong></p>
        <ul>
        <li>که تاسو په یوه مخ کې ګڼ شمېر متنونه یا صلیبونه ځای پر ځای کړي وي، تاسو کولای شئ د شرایطو مینو له لارې (د متن حالت کې ښی کلیک) ټول عناصر یوځای خوندي یا رد کړئ.</li>
        <li>د خوندي کولو پرمهال، ټول عناصر به PDF کې ځای پر ځای شي او د ویکټور ګرافیک په توګه پاتې شي.</li>
        </ul>

        <p><strong>۶. د متن حالت کې د کیبورډ شارټ کټونه</strong></p>
        <ul>
        <li>تیر تڼۍ: عنصر خوځوئ</li>
        <li>Ctrl+تیر تڼۍ: لوی ګامونو سره خوځوئ</li>
        <li>Enter: د خوندي کولو کړکۍ پرانیزئ (ټول خوندي کړئ / تنظیم یې کړئ / رد یې کړئ)</li>
        <li>ESC: اوسنی عنصر رد کړئ</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "د صلیب تنظیمات",
        'cross_properties': "د صلیب ځانګړتیاوې",
        'cross_size': "اندازه (px):",
        'cross_line_width': "د کرښې ټوپوالی:",
        'cross_color': "رنګ:",
        'cross_choose_color': "وټاکئ",
        'cross_fine_tuning': "د خوندي کولو پرمهال دقیق تنظیم (پېکسل)",
        'cross_offset_x': "X جبران:",
        'cross_offset_y': "Y جبران:",
        'cross_offset_x_tooltip': "منفي ارزښت د خوندي کولو پرمهال صلیب کیڼ لور ته اړوي، مثبت ښي لور ته",
        'cross_offset_y_tooltip': "منفي ارزښت د خوندي کولو پرمهال صلیب پورته اړوي، مثبت ښکته",
        'cross_preview': "مخکتنه",
        'cross_save': "تنظیمات پلی کړئ",
        'cross_customized': "صلیب تنظیم شو",
        'cross_settings_applied': "د صلیب تنظیمات خوندي شول.\nاندازه: {0}px، د کرښې ټوپوالی: {1}px\n{2}",
        'cross_updated_count': "{0} موجوده صلیبونه تازه شول.",
        'cross_no_crosses': "هېڅ موجود صلیب و نه موندل شو.",
        'cross_settings_applied_all': "د صلیب تنظیمات د ټولو {0} صلیبونو لپاره پلی شول",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "د لاسلیک تنظیمات",
        'signature_1': "لاسلیک ۱",
        'signature_2': "لاسلیک ۲",
        'signature_select': "لاسلیک وټاکئ",
        'signature_add': "➕ نوی لاسلیک ورزیات کړئ...",
        'signature_size': "د لاسلیک {0} لپاره اندازه (٪):",
        'signature_common': "عام تنظیمات",
        'signature_timestamp': "د وخت ټاپه په اتومات ډول ورزیات کړئ",
        'signature_location': "تلوالی ځای:",
        'signature_timestamp_size': "د وخت ټاپې د فونټ اندازه:",
        'signature_no_files': "-- هېڅ لاسلیک و نه موندل شو --",
        'signature_insert': "لاسلیک داخل کړئ",
        'signature_insert_1': "لاسلیک ۱ داخل کړئ",
        'signature_insert_2': "لاسلیک ۲ داخل کړئ",
        'signature_customize': " دا لاسلیک تنظیم کړئ",
        'signature_discard': " دا لاسلیک رد کړئ",
        'signature_save_all': " ټول لاسلیکونه خوندي کړئ",
        'signature_discard_all': " ټول لاسلیکونه رد کړئ",
        'signature_guide_title': "لاسلیکونه - لارښود",
        'signature_guide': """
📝 لاسلیکونه - چټک لارښود

- ماسټر پټ نوم تنظیم کړئ
- لاسلیکونه د مینو تنظیماتو کې تنظیم کړئ
  (اندازه، د وخت ټاپه ...)
- په مطلوب ځای کې د ښي کلیک په مرسته داخل کړئ
  (په هر ناسته کې یو ځل ماسټر پټ نوم ته اړتیا ده)
- لاسلیک د موږک یا تیر تڼیو په مرسته وخوځوئ
- ګڼ لاسلیکونه یو له بل وروسته داخلېدای شي
- هر لاسلیک په جلا توګه تنظیمېدای شي
- یو واحد لاسلیک رد کړئ
- ټول لاسلیکونه یوځای خوندي / رد کړئ
- په بدیل ډول، د مینو پټۍ هم کارېدای شي.
        """,
        'signature_placeholder': "هېڅ مخکتنه نشته",
        'signature_info': "لاسلیک {0}: {1}×{2} px ({3}٪ د {4}×{5})",
        'signature_info_placeholder': "د لاسلیک {0} لپاره تنظیمات",
        'signature_inserted': "لاسلیک {0} په {1} مخ کې داخل شو",
        'signature_deleted': "لاسلیک ړنګ شو",
        'signature_copied': "لاسلیک کاپي شو",
        'signature_pasted': "لاسلیک {0} چاپ شو",
        'signature_saved': "{0} لاسلیکونه PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'signature_saved_voice': "{0} لاسلیکونه خوندي شول",
        'mode_replace_signature_format': "حالت پای ته ورسوئ او لاسلیک {0} داخل کړئ",
        'mode_conflict_voice_signature': "د {0} حالت فعال دی. پای ته یې ورسوم او لاسلیک داخل کړم؟",
        'signature_not_configured': "لاسلیک {0} نه دی تنظیم شوی",
        'signature_file_not_found': "د لاسلیک فایل و نه موندل شو",
        'timestamp_format': "{0}، {1}",
        'no_copied_signature': "هېڅ کاپي شوی لاسلیک نشته",
        'no_signatures_to_save': "د خوندي کولو لپاره هېڅ لاسلیک نشته",
        'signature_save_question': "ټول لاسلیکونه خوندي کړئ، تنظیم یې کړئ یا دا لاسلیک رد کړئ؟",
        'signatures_saved_title': "لاسلیکونه خوندي شول",
        'signatures_saved': "{0} لاسلیکونه PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'signatures_saved_voice': "{0} لاسلیکونه خوندي شول.",
        'all_signatures_discarded': "ټول لاسلیکونه رد شول",
        'signature_settings_saved': "د لاسلیک تنظیمات خوندي شول",
        'signature_cancelled': "لاسلیک رد شو",
        'signature_active_title': "لاسلیک فعال دی",
        'signature_replace_question': "له پخوا یو لاسلیک فعال دی.\n\nآیا غواړئ اوسنی لاسلیک بدل کړئ؟",
        'signature_replace': "لاسلیک بدل کړئ",
        'signature_replace_voice': "اوسنی لاسلیک بدل کړم یا لغوه یې کړم؟",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "د انځور تنظیمات",
        'image_common': "عام انځور تنظیمات",
        'image_keep_aspect': "د کشولو پرمهال تناسب وساتئ",
        'image_default_size': "تلوالی اندازه (٪):",
        'image_dark_invert': "په تیاره حالت کې انځورونه سربدل کړئ",
        'image_dark_invert_tooltip': "فعال: انځورونه به د ښه لید لپاره سربدل شي",
        'image_fine_tuning': "دقیق تنظیم (پېکسل)",
        'image_offset_x': "X جبران:",
        'image_offset_y': "Y جبران:",
        'image_offset_x_tooltip': "منفي ارزښت د خوندي کولو پرمهال انځور کیڼ لور ته اړوي، مثبت ښي لور ته",
        'image_offset_y_tooltip': "منفي ارزښت د خوندي کولو پرمهال انځور پورته اړوي، مثبت ښکته",
        'image_select': "انځور وټاکئ",
        'image_insert': "انځور داخل کړئ",
        'image_customize': " دا انځور تنظیم کړئ",
        'image_aspect': " تناسب وساتئ",
        'image_discard': " دا انځور رد کړئ",
        'image_save_all': " ټول انځورونه خوندي کړئ",
        'image_discard_all': " ټول انځورونه رد کړئ",
        'image_filter': "انځورونه",
        'image_guide_title': "انځور داخلول - لارښود",
        'image_guide': """
📷 په PDF کې انځور داخلول - چټک لارښود:

۱. په مطلوب ځای کې ښی کلیک وکړئ
۲. "انځور داخل کړئ" → انځور وټاکئ
۳. انځور ځای پر ځای کړئ: د موږک په مرسته یې کش کړئ
۴. اندازه یې تنظیم کړئ: په څنډو/ګوټیو کې یې کش کړئ
۵. تناسب وساتئ: د [A] تڼۍ فشار کړئ
۶. نور تنظیم: په انځور ښی کلیک وکړئ

لارښوونه: د شرایطو مینو کې تاسو کولای شئ تنظیمات بدل کړئ.
        """,
        'image_inserted': "انځور {0} په {1} مخ کې داخل شو",
        'image_deleted': "انځور رد شو",
        'image_copied': "انځور کاپي شو",
        'image_pasted': "انځور چاپ شو",
        'image_saved': "{0} انځورونه PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'image_saved_voice': "{0} انځورونه خوندي شول",
        'image_aspect_on': "فعال",
        'image_aspect_off': "غیر فعال",
        'image_aspect_toggle': "تناسب وساتئ {0}",
        'image_reset': "انځور خپل اصلي اندازې ته بېرته وګرځول شو",
        'image_replaced': "انځور بدل شو",
        'image_invalid': "سم انځور نه دی",
        'mode_replace_image': "انځور داخل کړئ",
        'mode_conflict_voice_image': "د {0} حالت فعال دی. پای ته یې ورسوم او انځور داخل کړم؟",
        'image_active_title': "انځور فعال دی",
        'image_replace_question': "له پخوا یو انځور فعال دی.\n\nآیا غواړئ اوسنی انځور بدل کړئ؟",
        'image_replace': "انځور بدل کړئ",
        'image_replace_voice': "اوسنی انځور بدل کړم یا لغوه یې کړم؟",
        'image_filter_all': "انځورونه (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;ټول فایلونه (*.*)",
        'no_copied_image': "هېڅ کاپي شوی انځور نشته",
        'image_discarded': "انځور رد شو",
        'image_save_question': "ټول انځورونه خوندي کړئ، تنظیم یې کړئ یا دا انځور رد کړئ؟",
        'no_images_to_save': "د خوندي کولو لپاره هېڅ انځور نشته",
        'no_valid_images': "د خوندي کولو لپاره هېڅ سم انځور نشته",
        'images_saved_title': "انځورونه خوندي شول",
        'images_saved': "{0} انځورونه PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'images_saved_voice': "{0} انځورونه خوندي شول.",
        'all_images_discarded': "ټول انځورونه رد شول",
        'image_settings_updated': "د انځور تنظیمات تازه شول",
        'image_replace_title': "نوی انځور وټاکئ",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "د شکلونو تنظیمات",
        'form_basic': "اساسي تنظیمات",
        'form_default_type': "تلوالی شکل ډول:",
        'form_rectangle': "مستطیل",
        'form_ellipse': "بیضوي",
        'form_line': "کرښه",
        'form_arrow': "غشی",
        'form_line_width': "د کرښې ټوپوالی:",
        'form_colors': "رنګونه",
        'form_line_color': "د کرښې رنګ:",
        'form_fill_color': "د ډکولو رنګ:",
        'form_choose_color': "وټاکئ",
        'form_transparent': "شفاف پس منظر (یوازې کرښه)",
        'form_filled': "ډک شوی",
        'form_dark_mode': "تیاره حالت",
        'form_dark_invert': "په تیاره حالت کې رنګونه سربدل کړئ",
        'form_fine_tuning': "دقیق تنظیم (پېکسل)",
        'form_offset_x': "X جبران:",
        'form_offset_y': "Y جبران:",
        'form_offset_x_tooltip': "منفي ارزښت د خوندي کولو پرمهال شکل کیڼ لور ته اړوي، مثبت ښي لور ته",
        'form_offset_y_tooltip': "منفي ارزښت د خوندي کولو پرمهال شکل پورته اړوي، مثبت ښکته",
        'form_preview': "مخکتنه",
        'form_insert': "شکل داخل کړئ",
        'form_rectangle_insert': "مستطیل",
        'form_ellipse_insert': "بیضوي/دایره",
        'form_line_insert': "کرښه (۲ کلیکونه)",
        'form_arrow_insert': "غشی (۲ کلیکونه)",
        'form_customize': " دا شکل تنظیم کړئ",
        'form_transparent_toggle': " شفاف پس منظر",
        'form_discard': " دا شکل رد کړئ",
        'form_save_all': " ټول شکلونه خوندي کړئ",
        'form_discard_all': " ټول شکلونه رد کړئ",
        'form_guide_title': "شکل داخلول - لارښود",
        'form_guide': """
📐 په PDF کې شکل داخلول - چټک لارښود:

۱. د شکل ډول وټاکئ (مستطیل، بیضوي، کرښه، غشی)
۲. په ځای کې کلیک وکړئ
   - د مستطیل/بیضوي لپاره: یو کلیک شکل ځای پر ځای کوي
   - د کرښې/غشي لپاره: د پیل او پای ټکي لپاره دوه کلیکونه
۳. شکل ځای پر ځای کړئ: د موږک په مرسته یې کش کړئ
۴. اندازه یې تنظیم کړئ: په څنډو/ګوټیو کې یې کش کړئ
۵. شکل خوندي کړئ: Enter
۶. شکل رد کړئ: ESC
۷. نور تنظیم: په شکل ښی کلیک وکړئ

لارښوونه: د شرایطو مینو کې تاسو کولای شئ تنظیمات بدل کړئ.
        """,
        'form_inserted': "{0} په {1} مخ کې داخل شو",
        'form_deleted': "شکل ړنګ شو",
        'form_copied': "شکل کاپي شو",
        'form_pasted': "شکل چاپ شو",
        'form_saved': "{0} شکلونه PDF ته ورزیات شول.\n\nPDF بېرته بار شو...",
        'form_saved_voice': "{0} شکلونه خوندي شول",
        'form_reset': "شکل خپل تلوالي اندازې ته بېرته وګرځول شو",
        'form_transparent_on': "فعال",
        'form_transparent_off': "غیر فعال",
        'form_transparent_toggled': "شفاف پس منظر {0}",
        'form_line_cancel': "د کرښې رسمول لغوه شول",
        'form_second_click': "اوس د {0} لپاره پای ټکی کلیک کړئ",
        'mode_replace_form': "شکل داخل کړئ",
        'mode_conflict_voice_form': "د {0} حالت فعال دی. پای ته یې ورسوم او شکل داخل کړم؟",
        'form_settings_updated': "د شکل تنظیمات تازه شول",
        'form_unknown': "شکل",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "۱. د پیل ټکي کلیک وکړئ",
        'form_line_guide_2': "۲. د پای ټکي کلیک وکړئ",
        'form_line_guide_3': "کرښه به د دوو ټکو ترمنځ ورسول شي.",
        'form_line_status_1': "د لومړي کلیک انتظار...",
        'form_line_status_2': "لومړی ټکی وټاکل شو: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "اوس پای ټکی کلیک کړئ...",
        'form_line_status_4': "دواړه ټکي وټاکل شول.\nد خوندي کولو لپاره 'پای' کلیک کړئ.",
        'form_line_reset': "بېرته تنظیم کړئ",
        'form_line_finish': "پای",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "کاپي کړئ (Cmd+C)",
        'paste': "چاپ کړئ (Cmd+V)",
        'copied': "کاپي شو: {0}",
        'no_element_to_copy': "د کاپي کولو لپاره هېڅ عنصر نه دی ټاکل شوی",
        'no_copied_data': "هېڅ کاپي شوي معلومات نشته",
        'no_valid_position': "د چاپولو لپاره هېڅ سم ځای نشته",
        'copy_text': "متن کاپي شو",
        'copy_image': "انځور کاپي شو",
        'copy_form': "شکل کاپي شو",
        'copy_signature': "لاسلیک کاپي شو",
        'element_text': "متن",
        'element_image': "انځور",
        'element_form': "شکل",
        'element_signature': "لاسلیک",
        'element_unknown': "عنصر",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "د حالت ټکر",
        'mode_conflict_message': "د '{0}' حالت لا فعال دی.\n\nآیا غواړئ هغه پای ته ورسوئ او {1}؟",
        'mode_replace': "حالت پای ته ورسوئ او {0}",
        'mode_cancel': "لغوه کړئ",
        'mode_replace_text': "متن داخل کړئ",
        'mode_replace_cross': "صلیب داخل کړئ",
        'mode_replace_signature': "لاسلیک داخل کړئ",
        'mode_replace_image': "انځور داخل کړئ",
        'mode_replace_form': "شکل داخل کړئ",
        'mode_conflict_voice': "د {0} حالت فعال دی. پای ته یې ورسوم او متن داخل کړم؟",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "متن داخلول",
        'active_mode_signature': "لاسلیک",
        'active_mode_image': "انځور",
        'active_mode_form': "شکل",
        'active_mode_and': " او ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "داخلول",
        'insert_another_text': "متن داخل کړئ",
        'insert_another_cross': "صلیب داخل کړئ",
        'insert_another_signature_1': "لاسلیک ۱",
        'insert_another_signature_2': "لاسلیک ۲",
        'insert_another_image': "انځور داخل کړئ",
        'insert_another_form_rect': "مستطیل",
        'insert_another_form_ellipse': "بیضوي",
        'insert_another_form_line': "کرښه (۲ کلیکونه)",
        'insert_another_form_arrow': "غشی (۲ کلیکونه)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} خوندي کړئ",
        'save_dialog_message': "{0} به په {1} مخ کې خوندي شي.\n\nتاسو څنګه ادامه ورکول غواړئ؟",
        'save_all': "ټول {0} خوندي کړئ",
        'save_single': "{0} خوندي کړئ",
        'save_customize': "{0} تنظیم کړئ",
        'save_discard': "دا {0} رد کړئ",
        'save_continue': "سمون ته دوام ورکړئ",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " {0} مخ ته لاړ شئ",
        'context_rotate': " {0} مخ وګرځوئ",
        'context_delete': " {0} مخ ړنګ کړئ",
        'context_export': " {0} مخ صادر کړئ",
        'context_mark_as': " مخ دې توګه ونښه کړئ...",
        'context_mark_empty': " خالي مخ",
        'context_unmark_empty': " نور خالي نه دی",
        'context_mark_export': " د صادرولو لپاره ونښه کړئ",
        'context_unmark_export': " د صادرولو نښه لرې کړئ",
        'context_batch_actions': " ډله‌ییز کړنې",
        'context_batch_delete_empty': " ټول {0} خالي مخونه ړنګ کړئ",
        'context_batch_export_single': " ټول {0} مخونه (یو فایل)",
        'context_batch_export_split': " ټول {0} مخونه (جلا جلا)",
        'context_drag_start': " کشول او غورځول پیل کړئ",
        'context_drag_stop': " کشول او غورځول بند کړئ",
        'context_insert': " داخل کړئ",
        'context_insert_pages': " مخونه داخل کړئ",
        'context_zoom': "لويه کول",
        'discard_mixed': "ټول {0} {1} او {2} {3} رد کړئ",
        'save_mixed': "{0} {1} او {2} {3} خوندي کړئ",
        'discard_texts': "ټول {0} متنونه رد کړئ",
        'discard_text_single': "۱ متن رد کړئ",
        'save_texts': "{0} متنونه خوندي کړئ",
        'save_text_single': "۱ متن خوندي کړئ",
        'discard_crosses': "ټول {0} صلیبونه رد کړئ",
        'discard_cross_single': "۱ صلیب رد کړئ",
        'save_crosses': "{0} صلیبونه خوندي کړئ",
        'save_cross_single': "۱ صلیب خوندي کړئ",
        'discard_signatures': "ټول {0} لاسلیکونه رد کړئ",
        'save_signature_single': "۱ لاسلیک خوندي کړئ",
        'save_signatures': "{0} لاسلیکونه خوندي کړئ",
        'discard_images': "ټول {0} انځورونه رد کړئ",
        'save_image_single': "۱ انځور خوندي کړئ",
        'save_images': "{0} انځورونه خوندي کړئ",
        'discard_forms': "ټول {0} شکلونه رد کړئ",
        'save_form_single': "۱ شکل خوندي کړئ",
        'save_forms': "{0} شکلونه خوندي کړئ",
        'cross_discard': "دا صلیب رد کړئ",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 د صادرولو / واردولو معلومات",
        'export_what': "📋 څه صادرېږي؟",
        'export_general': "عام تنظیمات",
        'export_general_items': "• غږیز تولید (روان/بند، چټکتیا)\n• تیاره/روښانه حالت\n• د بیک اپ تنظیمات\n• د OCR تنظیمات",
        'export_image_form': "د انځور او شکل تنظیمات",
        'export_image_form_items': "• د انځور تنظیمات (تناسب، تلوالی اندازه)\n• د شکل تنظیمات (د کرښې ټوپوالی، رنګونه)\n• د لاسلیک تنظیمات (لارې، اندازې، د وخت ټاپه)",
        'export_passwords': "د پټ نوم ډېټابیس",
        'export_passwords_items': "• ټول خوندي شوي د PDF پټ نومونه\n• په انتخابی ډول کوډ شوي یا کوډ خلاص شوي",
        'export_master': "د ماسټر پټ نوم تنظیمات",
        'export_master_items': "• د ماسټر پټ نوم هش\n• د لاسلیکونو/متن بلاکونو لپاره تنظیمات",
        'export_signatures': "لاسلیکونه او متن بلاکونه",
        'export_signatures_items': "• ټول انځور فایلونه (لاسلیکونه)\n• ټول متن بلاکونه د بڼې جوړونې سره\n• شخصي/عامه نښې",
        'export_import_warning': "⚠️ مهم یادښتونه",
        'export_import_note': "• د واردولو پر مهال، ټول اوسني تنظیمات له سره لیکل کېږي\n• د غوښتنلیک بیا پیلول اړین دي\n• موجوده لاسلیکونه/متن بلاکونه به بدل شي",
        'export_master_note': "• که ماسټر پټ نوم ټاکل شوی وي، تاسو کولای شئ انتخاب کړئ:\n  - کوډ خلاص شوی (پټ نومونه د ساده متن په توګه)\n  - کوډ شوی (یوازې د ماسټر پټ نوم سره لوستل کېدای شي)",
        'export_security': "• صادر شوی ZIP فایل محرم معلومات لري\n• لطفاً یې په خوندي ځای کې وساتئ (د مثال په توګه کوډ شوی USB)\n• د فایل له لاسه ورکولو سره: پټ نومونه بېرته نه موندل کېږي",
        'export_format': "📁 د صادرولو بڼه",
        'export_format_desc': "تنظیمات به په یو واحد ZIP فایل کې خوندي شي:",
        'export_filename': "PDFDarkView_تنظیمات_YYYYMMDD_HHMMSS.zip",
        'export_success': "تنظیمات په بریالیتوب سره صادر شول",
        'export_failed': "صادرول ناکام شول",
        'export_import_question': "آیا غواړئ همدا اوس غوښتنلیک بیا پیل کړئ؟",
        'export_password_question': "ماسټر پټ نوم ټاکل شوی دی.\n\nآیا غواړئ پټ نومونه د کوډ خلاص شوي په توګه صادر کړئ؟\n(که نه، دوی به کوډ شوي صادر شي)",
        'export_decrypt': "کوډ خلاص شوی صادر کړئ",
        'export_encrypt': "کوډ شوی صادر کړئ",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " مالومات",
        'info_title': "د PDF ډارک ویو په اړه",
        'info_version': "نسخه",
        'info_author': "د تورالف شولټز (BinhDiez) لخوا رامینځته شوی",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "په اړه",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF ډارک ویو</strong> یو د لاسرسي وړ PDF لیدونکی دی، چې په ځانګړي ډول د لید معلولیت لرونکو خلکو لپاره رامینځته شوی.</p>

            <p><strong>اصلي ځانګړنې:</strong></p>
            <ul>
                <li>لوړ تضاد، دودیز کېدونکی انٹرفیس</li>
                <li>بشپړ کیبورډ کنټرول</li>
                <li>یوځای شوی غږیز تولید</li>
                <li>د سکین شویو اسنادو لپاره OCR</li>
                <li>پراخه سمون وسایل</li>
            </ul>

            <p>له ۵۰ څخه زیاتې ژبې ملاتړ کیږي – ترڅو PDF د ټولو لپاره د لاسرسي وړ وي.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "ځانګړنې",
        'info_features_intro': "PDF ډارک ویو تاسو ته لاندې امکانات وړاندې کوي:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>ښودنه او نیویګیشن</strong> – تیاره/روښانه حالت، مخونه اړول، زوم، مخ ته ورتلل</li>
            <li><strong>OCR (د متن پیژندنه)</strong> – سکین شوي اسناد د لټون او کاپي کولو وړ کړئ</li>
            <li><strong>سمون</strong> – متن، صلیبونه، لاسلیکونه، انځورونه او شکلونه داخل کړئ</li>
            <li><strong>د مخونو مدیریت</strong> – حذف کول، استخراج کول، داخلول، د کش او ډراپ له لارې حرکت کول</li>
            <li><strong>صادرول</strong> – Word، Pages یا د متن په توګه</li>
            <li><strong>امنیت</strong> – د پاسورډ ساتنه او مدیریت</li>
            <li><strong>لاسرسي</strong> – غږیز تولید، کیبورډ کنټرول، لوړ تضاد</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "کارونې",
        'info_accessibility': "♿ لاسرسي – بشپړ کیبورډ کنټرول",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 عمومي</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF خلاص کړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> لټون</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> تیاره/روښانه حالت بدل کړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> چاپ کړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> وتل</div>

        <div class="shortcut-cat">📖 نیویګیشن</div>
        <div class="shortcut-row"><kbd>تیر کیلي</kbd> مخ په مخ اړول</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> مخ ته لاړ شئ</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> لومړی مخ</div>
        <div class="shortcut-row"><kbd>Ende</kbd> وروستی مخ</div>

        <div class="shortcut-cat">✏️ سمون</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> متن داخل کړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> مخونه حذف کړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> مخونه استخراج کړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> مخونه داخل کړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> مخونه حرکت ورکړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> مخ وګرځوئ</div>

        <div class="shortcut-cat">🖼️ عناصر حرکت ورکول</div>
        <div class="shortcut-row"><kbd>تیر کیلي</kbd> متن/انځور/لاسلیک حرکت ورکړئ</div>
        <div class="shortcut-row"><kbd>Ctrl+تیر کیلي</kbd> لوی ګامونه</div>
        <div class="shortcut-row"><kbd>Enter</kbd> خوندي کړئ</div>
        <div class="shortcut-row"><kbd>ESC</kbd> رد کړئ</div>

        <div class="shortcut-cat">🗣️ غږیز تولید</div>
        <div class="shortcut-row"><kbd>F2</kbd> غږیز تولید پر/بند کړئ</div>
        """,
        'info_contextmenu': "📌 مهم: ټولې دندې د شرایطو مینو (د موږک ښي تڼۍ) له لارې هم د لاسرسي وړ دي!",
        'info_accessibility_hint': "💡 لارښوونه: غږیز تولید (F2) لارښوونه اسانه کوي او د مینو او ډیالوګونو په اړه غبرګون ورکوي.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "جواز & خپرونې معلومات",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 خپرونې معلومات</strong><br>
        د § 5 TMG له مخې معلومات:<br>
        تورالف شولټز<br>
        Schusterstraße 3, 65582 Diez, آلمان<br>
        برېښنالیک: binhdiez64@gmail.com<br>
        د منځپانګې مسؤل: تورالف شولټز (BinhDiez)<br><br>

        <strong>⚠️ مسؤلیت ردول</strong><br>
        سافټویر په لوړه احتیاط سره رامینځته شوی. د سمتی، بشپړتیا او فعالیت لپاره کومه ضمانت نه ورکول کیږي. کارونې په خپل مسؤلیت ترسره کیږي.<br><br>

        <strong>📄 MIT جواز (شخصي کارونې)</strong><br>
        د کاپي حق (c) 2026 تورالف شولټز (BinhDiez)<br>
        اجازه لري: وړیا کارونه، شخصي بدلونونه، شخصي کاپيونه.<br>
        اجازه نلري: پلورل، سوداګریزه کارونه، د کاپي حق خبرتیاوې لرې کول.<br><br>

        <strong>🔧 د دریمې ډلې برخې</strong><br>
        دا سافټویر د GPL، AGPL، Apache 2.0، BSD او MIT جوازونو لاندې برخې لري.<br>
        کله چې بیا ویشل کیږي، باید د اړوند جواز شرایط ومنل شي.<br><br>

        <strong>🌐 خلاص سرچینه</strong><br>
        سرچینه کوډ شتون لري او د اړوندو جواز شرایطو سره سم لیدل، بدلول او بیا وېشل کیدی شي.<br><br>

        © 2026 تورالف شولټز (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "مننه",
        'info_credits': "خلاص سرچینې ټولنې ته مننه",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF پروسس کول</li>
            <li><strong>PyQt5</strong> – ګرافیکي انٹرفیس</li>
            <li><strong>Tesseract OCR</strong> – د متن پیژندنه</li>
            <li><strong>OCRmyPDF</strong> – OCR ادغام</li>
            <li><strong>python-docx</strong> – Word ته صادرول</li>
            <li><strong>qtawesome</strong> – آیکونونه</li>
            <li><strong>DeepSeek</strong> – د ژباړو ملاتړ (۵۰+ ژبې)</li>
            <li><strong>ټول کارونکي</strong> – د ارزښتناکو غبرګونونو لپاره</li>
            <li><strong>خلاص سرچینې ټولنه</strong> – د عالي کتابتونونو لپاره</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "ژبې",
        'info_languages_header': "🌍 د ژبې ملاتړ",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View اوس مهال <strong>۶۲ ژبې</strong> ملاتړ کوي – ترڅو سافټویر په ټوله نړۍ کې د لاسرسي وړ وکارول شي.</p>

            <p><strong>📖 د ژبو بشپړ لیست (د مارچ ۲۰۲۶ پورې):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 افریقایي</li>
                    <li>🇦🇱 البانیایی (Shqip)</li>
                    <li>🇩🇿 عربي (العربية)</li>
                    <li>🇮🇩 بالیایي (Basa Bali)</li>
                    <li>🇧🇩 بنګالي (বাংলা)</li>
                    <li>🇲🇲 برمایی (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 بوسنیایی (Bosanski)</li>
                    <li>🇧🇬 بلغاریایی (Български)</li>
                    <li>🇨🇳 چینايي (中文)</li>
                    <li>🇩🇰 ډنمارکي (Dansk)</li>
                    <li>🇩🇪 آلماني (Deutsch)</li>
                    <li>🇬🇧 انګلیسي (English)</li>
                    <li>🇪🇪 استونيایی (Eesti)</li>
                    <li>🇫🇮 فنلنډي (Suomi)</li>
                    <li>🇫🇷 فرانسوي (Français)</li>
                    <li>🇬🇷 یوناني (Ελληνικά)</li>
                    <li>🇮🇱 عبراني (עברית)</li>
                    <li>🇮🇳 هندي (हिन्दी)</li>
                    <li>🇭🇷 کرواتي (Hrvatski)</li>
                    <li>🇭🇺 هنګري (Magyar)</li>
                    <li>🇮🇩 اندونیزیايي (Bahasa Indonesia)</li>
                    <li>🇮🇪 آیرلنډي (Gaeilge)</li>
                    <li>🇮🇸 آیسلنډي (Íslenska)</li>
                    <li>🇮🇹 ایټالوي (Italiano)</li>
                    <li>🇯🇵 جاپاني (日本語)</li>
                    <li>🇰🇭 خمیر (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 کوریایي (한국어)</li>
                    <li>🇱🇦 لاوتیايي (ພາສາລາວ)</li>
                    <li>🇱🇻 لاتویايي (Latviešu)</li>
                    <li>🇱🇹 لیتوانیايي (Lietuvių)</li>
                    <li>🇱🇺 لوګزامبورګي (Lëtzebuergesch)</li>
                    <li>🇲🇾 مالایي (Bahasa Melayu)</li>
                    <li>🇮🇳 مراټي (मराठी)</li>
                    <li>🇲🇳 مغولي (Монгол)</li>
                    <li>🇳🇵 نیپالي (नेपाली)</li>
                    <li>🇳🇱 هالنډي (Nederlands)</li>
                    <li>🇳🇴 ناروېژي (Norsk)</li>
                    <li>🇦🇫 پښتو (پښتو)</li>
                    <li>🇮🇷 فارسي (فارسی)</li>
                    <li>🇵🇱 پولنډي (Polski)</li>
                    <li>🇵🇹 پرتګالي (Português)</li>
                    <li>🇮🇳 پنجابي (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 رومانیايي (Română)</li>
                    <li>🇷🇺 روسي (Русский)</li>
                    <li>🇸🇪 سویډني (Svenska)</li>
                    <li>🇷🇸 صربي (Српски)</li>
                    <li>🇸🇰 سلواکي (Slovenčina)</li>
                    <li>🇸🇮 سلواني (Slovenščina)</li>
                    <li>🇪🇸 هسپانوي (Español)</li>
                    <li>🇹🇿 سواحلي (Kiswahili)</li>
                    <li>🇵🇭 تاګالوګ (Filipino)</li>
                    <li>🇮🇳 تامل (தமிழ்)</li>
                    <li>🇮🇳 تیلګو (తెలుగు)</li>
                    <li>🇹🇭 تای (ไทย)</li>
                    <li>🇨🇿 چېک (Čeština)</li>
                    <li>🇹🇷 ترکي (Türkçe)</li>
                    <li>🇺🇦 اوکرایني (Українська)</li>
                    <li>🇵🇰 اردو (اردو)</li>
                    <li>🇻🇳 ویتنامي (Tiếng Việt)</li>
                    <li>🇸🇳 وولوف (Wolof)</li>
                    <li>🇺🇸 یدش (ייִדיש)</li>
                    <li>🇿🇦 زولو (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 خپلې ژبې اضافه کړئ:</strong><br>
                غواړئ یوه ژبه چې لا تر اوسه نه ده شامله؟ یوازې خپل د قاموس فایل (<code>sprache_xx.py</code>) د غوښتنلیک تر څنګ کېږدئ – سافټویر به یې په اتوماتيک ډول وپیژني. که تاسو د یوې ځانګړې ژباړې سره لیوالتیا لرئ، مهرباني وکړئ له ما سره اړیکه ونیسئ.
            </div>

            <p><strong>🙏 ځانګړې مننه:</strong> DeepSeek ته د ټولو قاموسونو په ۶۲ ژبو کې د ژباړې لپاره د ملاتړ څخه.</p>

            <p>📧 د ژباړې لپاره اړیکه: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "د انعکاس حالت",
        'invert_mode_classic': "کلاسیک (ټول رنګونه انعکاس کړئ)",
        'invert_mode_smart': "هوشیار (یوازې روښانتیا انعکاس کړئ)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "خړ سکیل حد",
        'gray_threshold_10': "۱۰٪ (سخت)",
        'gray_threshold_20': "۲۰٪",
        'gray_threshold_30': "۳۰٪ (تلوالیز)",
        'gray_threshold_40': "۴۰٪",
        'gray_threshold_50': "۵۰٪ (نرم)",
        'threshold_changed': "حد د {0}٪ په توګه وټاکل شو",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "خړ سکیل حد – توضیح",
        'threshold_guide_text': "خړ سکیل حد ټاکي چې په هوشیار تیاره حالت کې کوم پکسلونه د 'خړ' په توګه ګڼل کیږي او انعکاس کیږي.\n\n"
                                "• ټیټ ارزښت (۱۰٪) یوازې نږدې بشپړ خړ ټونونه انعکاس کوي – رنګین عناصر په بشپړه توګه ساتل کیږي.\n"
                                "• لوړ ارزښت (۵۰٪) یو څه رنګین پکسلونه هم انعکاس کوي – دا تضاد زیاتوي، مګر کولی شي رنګونه خراب کړي.\n\n"
                                "غوره ارزښت په سند پورې اړه لري. د خالص متن اسنادو لپاره ۳۰–۴۰٪ ډیری وختونه مثالی دی، د رنګین ګرافیکونو لپاره ۱۰–۲۰٪ غوره دی.\n\n"
                                "تاسو کولی شئ هر وخت د 'ترتیباتو' مینو له لارې ارزښت تنظیم کړئ – PDF به سمدستي بیا پورته شي.\n\n"
                                "یادونه:\n* عکسونه او انځورونه یوازې په روښانه حالت کې په سمه توګه ښودل کیدی شي!\n* د انعکاس ترتیبات یوازې هغه وخت ښودل کیږي کله چې تیاره حالت فعال شوی وي.",
        'threshold_guide_voice': "خړ سکیل حد ټاکي چې هوشیار تیاره حالت څومره قوي مداخله کوي. ټیټ ارزښت رنګونه ساتي، لوړ ارزښت تضاد زیاتوي.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF خلاصیږي...",
        'progress_loading_document': "سند پورته کیږي...",
        'progress_pdf_opened': "PDF خلاص شو",
        'progress_creating_backup': "بیک اپ جوړیږي...",
        'progress_backup_description': "اصلي فایل خوندي کیږي...",
        'progress_backup_created': "بیک اپ جوړ شو",
        'progress_backup_saved_as': "د {0} په توګه خوندي شو",
        'progress_analyzing_start': "تحلیل پیل کیږي...",
        'progress_searching_empty': "خالي مخونه لټول کیږي...",
        'progress_page_empty': "مخ {0} خالي دی",
        'progress_page_keep': "مخ {0} وساتئ",
        'progress_analysis_complete': "تحلیل بشپړ شو",
        'progress_empty_found': "{0} خالي مخونه وموندل شول",
        'progress_current_page': "اوسنی مخ",
        'progress_mark_delete': "د حذف کولو لپاره نښه کیږي",
        'progress_range_selected': "د مخونو ساحه {0}-{1}",
        'progress_deleting_pages': "{0} مخونه حذف کیږي",
        'progress_creating_new_pdf': "نوی PDF جوړیږي...",
        'progress_transferring_pages': "مخونه لیږدول کیږي",
        'progress_keeping_page': "مخ {0} به وساتل شي ({1}/{2})",
        'progress_saving_pdf': "PDF خوندي کیږي...",
        'progress_optimizing': "د فایل اندازه غوره کیږي...",
        'progress_finalizing': "نهایی کیږي...",
        'progress_new_size': "نوی اندازه: {0:.2f} MB",
        'progress_cancelling': "لغوه کیږي...",
        'progress_cancel_message': "{0} لغوه کیږي",
        'progress_pages_found_moving': "{0} مخونه وموندل شول، {1} د حرکت لپاره",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF تحلیل کیږي...",
        'ocr_status_optimizing': "د انځور اصلاح روانه ده...",
        'ocr_status_recognizing': "د متن پیژندنه روانه ده...",
        'ocr_status_embedding': "متن ځای پر ځای کیږي...",
        'ocr_status_finalizing': "PDF نهایی کیږي...",

        # PDF-Laden
        'progress_preparing': "تیاری...",
        'progress_loading': "PDF پورته کیږي...",

        # Seitenoperationen
        'progress_deleting_title': "مخونه حذف کیږي...",
        'progress_moving_title': "مخونه حرکت کوي...",
        'pages_found': "مخونه وموندل شول",
        'progress_creating_new_order': "نوی ترتیب جوړیږي...",
        'progress_sorting_pages': "مخونه مرتب کیږي...",
        'progress_moving_to_begin': "{0} مخونه پیل ته حرکت ورکړئ",
        'progress_transferring_count': "{0} مخونه لیږدئ",
        'progress_transferring_before_target': "مخونه د هدف دمخه لیږدئ",
        'progress_moving_pages': "{0} مخونه حرکت ورکړئ",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_بیک_اپ_",
        'filename_protected_suffix': "_خوندي_",
        'filename_copy_suffix': "_کاپي",
        'filename_page_single': "_مخ_",
        'filename_page_range': "_مخونه_",
        'filename_export_page': "_مخ_{0:03}",
        'filename_export_range': "_مخونه_{0}-{1}",
        'filename_export_multiple': "_مخونه_{0}",
        'filename_with_text': "_له_متن_سره",
        'filename_with_signature': "_له_لاسلیک_سره",
        'filename_with_image': "_له_انځور_سره",
        'filename_with_forms': "_له_شکلونو_سره",
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
        'view_toggle_navbar': "د تڼۍ بار وښایاست",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "ټول مخونه نه ړنګېدلی شي",
		'pages_cannot_delete_last_page': 'آخر مخ نه ړنګېدلی شي!',
		'pages_cannot_delete_all_pages': 'په لاسوند کې لږ تر لږه یو مخ پاتې شي!',
		'delete_pages_confirm': 'آیا تاسو د {0} مخونو ړنګولو ډاډه یاست؟',
		'delete_pages_confirm_voice': 'آیا تاسو د {0} مخونو ړنګولو ډاډه یاست؟',
		'pages_deleted': '{0} مخونه په بریالیتوب سره ړنګ شول.',
		'warning': 'خبرداری',
		'error': 'تېروتنه',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "هیڅ فورمه نه ده ټاکل شوې",
        'form_customized': "فورمه دودیزه شوه",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "انتخاب",
        'btn_use': "استعمال",
        'master_password_for_spasswords': "د پاسورډونو د خوندي کولو او کارولو لپاره، لومړی باید ماسټر پاسورډ جوړ شي.\n\nآيا تاسو غواړئ اوس ماسټر پاسورډ جوړ کړئ؟",
        'open_saved_dialog_title': "خوندي شوی فایل پرانیزئ",
        'open_saved_question': "آيا تاسو غواړئ خوندي شوی فایل اوس خلاص کړئ؟",
        'password': "پاسورډ",
        'password_manager_master_required': "د پاسورډ مدیر یوازې هغه وخت شتون لري کله چې ماسټر پاسورډ جوړ شوی وي.\n\nآيا تاسو غواړئ اوس ماسټر پاسورډ جوړ کړئ؟",
        'password_master_required_for_select': "د خوندي شویو پاسورډونو د لیدلو او انتخاب لپاره، تاسو باید لومړی خپل ماسټر پاسورډ سره تصدیق وکړئ.\n\nآيا تاسو غواړئ اوس تصدیق وکړئ؟",
        'password_not_available': "غوره شوی پاسورډ شتون نلري یا نشي کوډ کولی.",
        'password_options_title': "د پاسورډ اختیارونه",
        'password_save_choice_change': "نوی پاسورډ جوړ کړئ",
        'password_save_choice_keep': "موجود پاسورډ وکاروئ",
        'password_save_choice_none': "پرته له کوډ کولو خوندي کړئ",
        'password_save_hint': "لومړی ماسټر پاسورډ جوړ کړئ ترڅو پاسورډونه په خوندي توګه خوندي کړئ.",
        'password_save_master_required': "پاسورډ خوندي کړئ (یوازې د ماسټر پاسورډ سره ممکن دی)",
        'password_save_question': "اوسنی PDF د پاسورډ لخوا خوندي شوی. ایا تاسو غواړئ موجود پاسورډ وکاروئ، نوی جوړ کړئ یا پرته له کوډ کولو خوندي کړئ؟",
        'password_select': "پاسورډ وټاکئ",
        'password_select_none': "هیڅ پاسورډ نه دی غوره شوی.\n\nمهرباني وکړئ له لیست څخه یو پاسورډ وټاکئ.",
        'password_select_one': "مهرباني وکړئ یوازې یو پاسورډ وټاکئ.\n\nتاسو ډیری پاسورډونه په نښه کړي دي.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_بیک اپ",
        'filename_insert_suffix': "_له داخلولو سره",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_مخونه_ړنګ شوي",
        'filename_pages_moved': "_مخونه_لیږدول شوي",
        'filename_rotated_all_suffix': "_ټول_مخونه_څرخیدلي",
        'filename_rotated_suffix': "_مخ_څرخیدلی",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "د PDF د بدلولو په وخت کې د فایل نومونو تشکیلات",
        'filename_keep_suffixes': "مخکینۍ غځونې وساتئ (د مثال په توګه _له متن سره)",
        'filename_keep_suffixes_false': "ځای په ځای کړئ",
        'filename_keep_suffixes_true': "وساتئ",
        'filename_preview_label': "د فایل نوم مخکتنه:",
        'filename_preview_overwrite_hint': "مخکتنه شتون نلري – اصلي فایل به له سره ولیکل شي.",
        'filename_separator': "د کلمو ترمنځ جلا کوونکی",
        'filename_separator_none': "هیڅ جلا کوونکی",
        'filename_separator_space': "تش ځای ( )",
        'filename_separator_underscore': "لاندینی کرښه (_)",
        'filename_settings_saved': "د فایل نوم تنظیمات خوندي شول",
        'filename_settings_title': "د فایل نوم بڼه او بیک اپ",
        'filename_timestamp_position': "د وخت ټاپه موقعیت",
        'filename_timestamp_position_after': "د اساسي نوم وروسته",
        'filename_timestamp_position_before': "په بشپړه توګه مخکې",
        'filename_timestamp_position_end': "په پای کې",
        'filename_use_timestamp': "وخت ټاپه وکاروئ",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>د بدلونونو په وخت کې چلند:</b><ul><li>د مخونو ړنګول او داخلول</li><li>متن، لاسلیک، انځور او شکلونه داخلول</li><li>OCR</li></ul></html>",
        'backup_section': "د مخ عملیاتو لپاره بیک اپ (ړنګول، لیږدول)",
        'behavior_info': "یادونه: د 'اصلي له سره لیکل' په حالت کې د وخت ټاپې او ضمیمې له پامه غورځول کیږي – فایل خپل نوم ساتي.",
        'behavior_new_file': "تل نوی فایل جوړ کړئ (د وخت ټاپې او ضمیمې سره)",
        'behavior_overwrite': "اصلي له سره ولیکئ (نوی فایل نشته)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "ټول مخونه څرخیدلي.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {0}",
        'all_pages_rotated_voice': "ټول مخونه څرخیدلي، نوی فایل جوړ شو.",
        'empty_pages_deleted_new_file': "{0} تش مخونه ړنګ شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {1}",
        'empty_pages_deleted_voice': "{0} تش مخونه ړنګ شول، نوی فایل جوړ شو.",
        'ocr_keep_original': "اصلي وساتئ (وروسته په لاس سره خلاص کړئ)",
        'ocr_new_file_question': "نوی د لټون وړ PDF دلته خوندي شو:\n{0}\n\nآيا تاسو غواړئ دا اوس خلاص کړئ؟",
        'ocr_open_new': "نوی OCR فایل خلاص کړئ",
        'ocr_original_kept': "اصلي فایل خلاص پاتې کیږي. OCR فایل خوندي شوی دی.",
        'page_deleted_new_file': "مخ {0} ړنګ شو.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {1}",
        'page_deleted_voice': "مخ {0} ړنګ شو، نوی فایل جوړ شو.",
        'page_rotated_new_file': "مخ {0} څرخیدلی.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {1}",
        'page_rotated_voice': "مخ {0} څرخیدلی، نوی فایل جوړ شو.",
        'pages_deleted_new_file': "{0} مخونه ړنګ شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {1}",
        'pages_deleted_new_file_voice': "{0} مخونه ړنګ شول، نوی فایل جوړ شو.",
        'pages_inserted_new_file': "{0} مخونه داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {1}",
        'pages_inserted_new_file_ask': "{0} مخونه داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {1}\n\nآيا تاسو غواړئ دا اوس خلاص کړئ؟",
        'pages_inserted_voice_new': "{0} مخونه داخل شول، نوی فایل جوړ شو.",
        'pages_moved_new_file': "{0} مخونه لیږدول شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل: {1}",
        'pages_moved_new_file_voice': "{0} مخونه لیږدول شول، نوی فایل جوړ شو.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "بیا مه ښکاره کوه",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 د بیک اپ تنظیم</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ بیک اپ چالان دی</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">په ټولو هغو بدلونونو کې چې اصلي له سره لیکي</strong> (متن، لاسلیک، انځور، شکل، OCR، څرخول، داخلول، د مخونو ړنګول/لیږدول) د بدلون له پلي کیدو مخکې <strong>په اتوماتيک ډول د وخت ټاپې سره یو بیک اپ جوړیږي</strong>.</p>
                <p style="margin: 5px 0 5px 20px;">• بیک اپ د اصلي فایل تر څنګ پروت دی (د مثال په توګه <code>لاسوند_بیک_اپ_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• که تاسو په اضافي توګه د <strong>„اصلي له سره لیکل“</strong> اختیار چالان کړی وي، نو بیک اپ هم جوړیږي.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 بیک اپ بند دی</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>هیڅ بیک اپ نه جوړیږي</strong> – نه د له سره لیکلو پر مهال او نه د مخ عملیاتو پر مهال.</p>
                <p style="margin: 5px 0 5px 20px;">• اصلي فایل د له سره لیکلو پر مهال د نه راګرځیدونکي توګه له لاسه ورکولی شي.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">یوازې د تجربه لرونکو کاروونکو لپاره سپارښتنه کیږي!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>لارښوونه:</strong> د بیک اپ تنظیم د „اصلي له سره لیکل“ اختیار څخه خپلواک دی. تاسو دواړه سره یوځای کولی شئ.<br>
                تاسو کولی شئ دا پیغام د تل لپاره پټ کړئ.
            </div>
        </div>
        """,
        'backup_info_title': "د بیک اپ چلند",
        'backup_info_voice': "د مخ عملیاتو په وخت کې د بیک اپ چلند په اړه خبرتیا. بیک اپ چالان اصلي له سره لیکي، بیک اپ بند نوی فایل جوړوي.",
        'show_backup_info': "د بیک اپ تنظیم په اړه معلومات",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "بیا مه ښکاره کوه",
        'overwrite_enable_backup': "بیک اپ چالان کړئ (سپارښتنه کیږي)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ اصلي له سره لیکل</p>
            <p>که تاسو دا اختیار چالان کړئ، بدلونونه (متن، لاسلیک، انځور، شکل، OCR، څرخول، داخلول) <strong>په مستقیم ډول په اصلي فایل کې خوندي کیږي</strong> – <strong>هیڅ نوی فایل نه جوړیږي</strong>.</p>
            <p>• د فایل نوم نه بدلیږي.<br>
            • د وخت ټاپې او ضمیمې له پامه غورځول کیږي.<br>
            • <strong>د بیک اپ پرته، اصلي فایل د نه راګرځیدونکي توګه له لاسه ورکولی شي.</strong></p>
            <p style="color: #FFD700;">سپارښتنه: د اتوماتیک بیک اپونو ترلاسه کولو لپاره په اضافي توګه د بیک اپ اختیار چالان کړئ.</p>
        </div>
        """,
        'overwrite_info_title': "اصلي له سره لیکل",
        'overwrite_info_voice': "خبرتیا: اصلي له سره لیکل – نوی فایل نشته. بیک اپ سپارښتنه کیږي.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} مخونه داخل شول.\n\nاصلي فایل له سره لیکل شوی.\nیو بیک اپ جوړ شوی.",
        'pages_inserted_overwrite_no_backup': "{0} مخونه داخل شول.\n\nاصلي فایل له سره لیکل شوی.\nهیڅ بیک اپ نه دی جوړ شوی.",
        'texts_saved_overwrite_with_backup': "بدلونونه په اصلي فایل کې خوندي شول.\n\nیو بیک اپ جوړ شوی.",
        'texts_saved_overwrite_no_backup': "بدلونونه په اصلي فایل کې خوندي شول.\n\nهیڅ بیک اپ نه دی جوړ شوی.",
        'texts_crosses_saved_new_file': "{0} {1} او {2} {3} داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل جوړ شوی.\n\nنوی PDF بار کیږي...",
        'texts_saved_new_file': "{0} {1} داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل جوړ شوی.\n\nنوی PDF بار کیږي...",
        'crosses_saved_new_file': "{0} {1} داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل جوړ شوی.\n\nنوی PDF بار کیږي...",
        'elements_saved_new_file': "{0} عناصر داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل جوړ شوی.\n\nنوی PDF بار کیږي...",
        'signatures_saved_overwrite_with_backup': "لاسلیک(ونه) په اصلي فایل کې خوندي شول.\n\nیو بیک اپ جوړ شوی.",
        'signatures_saved_overwrite_no_backup': "لاسلیک(ونه) په اصلي فایل کې خوندي شول.\n\nهیڅ بیک اپ نه دی جوړ شوی.",
        'images_saved_overwrite_with_backup': "انځور(ونه) په اصلي فایل کې خوندي شول.\n\nیو بیک اپ جوړ شوی.",
        'images_saved_overwrite_no_backup': "انځور(ونه) په اصلي فایل کې خوندي شول.\n\nهیڅ بیک اپ نه دی جوړ شوی.",
        'forms_saved_overwrite_with_backup': "شکل(ونه) په اصلي فایل کې خوندي شول.\n\nیو بیک اپ جوړ شوی.",
        'forms_saved_overwrite_no_backup': "شکل(ونه) په اصلي فایل کې خوندي شول.\n\nهیڅ بیک اپ نه دی جوړ شوی.",
        'signatures_saved_new_file': "{0} لاسلیکونه داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل جوړ شوی.\n\nنوی PDF بار کیږي...",
        'images_saved_new_file': "{0} انځورونه داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل جوړ شوی.\n\nنوی PDF بار کیږي...",
        'forms_saved_new_file': "{0} شکلونه داخل شول.\n\nاصلي فایل نه دی بدل شوی.\nنوی فایل جوړ شوی.\n\nنوی PDF بار کیږي...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "خبرتیا: دا PDF څرخیدلي مخونه لري. موقعیت توپیر لري.",
        'page_rotated_warning_title': "څرخیدلی مخ کشف شو",
        'page_rotated_warning_message': "اوسنی مخ {0} د {1}° لخوا څرخیدلی.\n\nپه څرخیدلو مخونو کې د عناصرو داخلول ملاتړ نه کیږي.\n\nآيا تاسو غواړئ اوس مخ په مستقیم حالت کې وڅرخوئ؟",
        'page_rotated_warning_voice': "خبرتیا: مخ څرخیدلی. مهرباني وکړئ لومړی یې وڅرخوئ.",
        'paste_on_rotated_page_simple_warning': "په مخ {0} باندې داخلول ممکن نه دي!\n\nدا مخ د {1}° لخوا څرخیدلی.\n\nمهرباني وکړئ لومړی مخ 0° ته وڅرخوئ (مینو: سمول → مخ برابرول).\n\nخبرتیا:\nمخکې کاپي شوی عنصر به له لاسه ورکړي که تاسو د مخ له څرخولو دمخه خوندي نه کړئ.",
        'paste_on_rotated_page_voice': "داخلول لغوه شول. مخ څرخیدلی. مهرباني وکړئ لومړی مخ برابر کړئ.",
        'page_rotated_cancel': "لغوه کول",
        'page_rotated_rotate_until_upright': "مخ په پرله پسې توګه وڅرخوئ (تر څو مستقیم شي)",
        'page_rotated_now_upright': "مخ اوس مستقیم دی. تاسو اوس داخلولی شئ.",
        'page_rotated_still_not_upright': "مخ مستقیم حالت ته نه شو څرخیدلی. مهرباني وکړئ په لاس سره سم کړئ.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "مرسته: څرخیدلي مخونه سم کړئ",
        'help_rotated_pages_voice': "د څرخیدلو مخونو د سمولو لپاره مرسته خلاصیږي.",
        'btn_help': "مرسته",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 ستونزه: څرخیدلی مخ – داخلول په سمه توګه کار نه کوي</p>

            <p>که چیرې په څرخیدلي مخ باندې د متنونو، لاسلیکونو یا شکلونو داخلول په سمه توګه کار ونه کړي، تاسو کولی شئ د بهرني PDF مدیر په واسطه مخ سم کړئ.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ د بهرني وسیلې سره حل (د مثال په توګه د macOS مخکتنه)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>مخ صادر کړئ</strong><br>
                &nbsp;&nbsp;په مینو کې د <strong>فایل → د مخونو په توګه صادر کړئ</strong> کلیک وکړئ یا بله طریقه وکاروئ ترڅو مطلوب مخ د واحد PDF په توګه خوندي کړئ.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>مخ په بهرني پروګرام کې خلاص کړئ</strong><br>
                &nbsp;&nbsp;صادر شوی PDF په PDF مدیر کې خلاص کړئ (د مثال په توګه <strong>macOS مخکتنه</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>مخ وڅرخوئ</strong><br>
                &nbsp;&nbsp;مخ داسې وڅرخوئ چې مستقیم وي (په مخکتنه کې: <strong>وسیلې → څرخول</strong> یا <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>خوندي کړئ</strong><br>
                &nbsp;&nbsp;سم شوی مخ خوندي کړئ (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>مخ بیرته اصلي لاسوند کې دننه کړئ</strong><br>
                &nbsp;&nbsp;PDFDarkView ته بیرته راشئ او سم شوی مخ په مطلوب ځای کې داخل کړئ:<br>
                &nbsp;&nbsp;<strong>سمول → مخونه داخل کړئ</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 بدیل: په اصلي فایل کې مخ وڅرخوئ</p>
                <p style="margin: 5px 0 5px 20px;">• دننه جوړ شوی د څرخولو دنده وکاروئ (<strong>سمول → مخ وڅرخوئ</strong>) ترڅو مخ په تدریجي ډول سم کړئ.<br>
                • د هر څرخولو وروسته تاسو کولی شئ وګورئ چې آیا داخلول اوس کار کوي.<br>
                • دا اکثراً چټک حل دی – لومړی دا وازموئ!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>لارښوونه:</strong> که تاسو په مکرر ډول څرخیدلي مخونو سره مخ کیږئ، تاسو کولی شئ د داخلولو په ډیالوګ کې خبرتیا د تل لپاره پټه کړئ.<br>
                موقعیت بیا توپیر لري – دا اختیار یوازې وکاروئ که تاسو پایلې پیژنئ.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "مخونه برابر کړئ",
        'menu_rotate_normalize_tooltip': "مخ وڅرخوئ یا 0° ته بیا تنظیم کړئ",
        'normalize_current_page': "اوسنی مخ مستقیم حالت ته راوړئ (0° ته یې تنظیم کړئ)",
        'normalize_all_pages': "ټول مخونه مستقیم حالت ته راوړئ (0° ته یې تنظیم کړئ)",
        'page_normalized': "مخ {0} مستقیم حالت ته تنظیم شو.",
        'all_pages_normalized': "ټول مخونه مستقیم حالت ته تنظیم شول.",
        'page_already_upright': "مخ {0} دمخه مستقیم دی.",
        'all_pages_already_upright': "ټول مخونه دمخه مستقیم دي.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF کوم د لټون وړ متن نلري.</p><p>آیا تاسو غواړئ د {0} ته د صادرولو لپاره OCR ترسره کړئ؟</p>",
        'export_ocr_voice': "PDF کوم متن نلري. د {0} ته د صادرولو لپاره OCR اړین دی.",
        'export_no_ocr_possible': "د OCR پرته صادرول ممکن نه دي. مهرباني وکړئ د مینو له لارې OCR ترسره کړئ.",
        'ocr_failed_export_not_possible': "OCR ناکام شو. صادرول نشي ترسره کیدی.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF به د مخکتنې په برخه کې خلاص شي. مهرباني وکړئ هلته د چاپ پروسه پیل کړئ.",
        'print_preview_manual': "PDF خلاص شوی دی. مهرباني وکړئ د چاپ امر په لاس سره ترسره کړئ (د مثال په توګه Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDFونه یوځای کړئ",
        'merge_pdfs': "PDFونه یوځای کړئ",
        'merge_progress_title': "PDFونه یوځای کیږي...",
        'merge_pdfs_list': "په ترتیب سره PDFونه (د ترتیب لپاره کش کړئ او پریږدئ)",
        'merge_add_pdf': "PDF ورګډ کړئ",
        'merge_remove': "لرې کړئ",
        'merge_move_up': "پورته",
        'merge_move_down': "ښکته",
        'merge_pdfs_info': "💡 لارښوونه: تاسو کولی شئ د کشولو او پریښودو له لارې ترتیب بدل کړئ",
        'merge_no_pdfs': "هیڅ PDF نه دی غوره شوی. د 'PDF ورګډ کړئ' باندې کلیک وکړئ.",
        'merge_info': "{0} PDFونه غوره شوي (نږدې {1} مخونه)",
        'merge_open_file': "فایل خلاص کړئ",
        'merge_merge': "یوځای کړئ",
        'merge_error': "د یوځای کولو پرمهال تېروتنه",
        'merge_min_two_pdfs_error': "مهرباني وکړئ د یوځای کولو لپاره لږ تر لږه دوه PDF فایلونه غوره کړئ.",
        'merge_select_pdfs': "د یوځای کولو لپاره PDFونه غوره کړئ",
        'merge_error_file': "د پروسس کولو پرمهال تېروتنه",
        'merge_cancelled': "یوځای کول لغوه شول",
        'merge_preparing': "تجهیز کیږي...",
        'merge_processing': "د {1} څخه PDF {0} پروسس کیږي",
        'merge_saving': "یوځای شوی PDF خوندي کیږي...",
        'merge_complete': "ترسره شو!",
        'merge_success_title': "یوځای کول بریالي شول",
        'merge_success_voice': "{0} PDFونه په بریالیتوب سره یوځای شول.",
        'merge_success_message': "{0} PDFونه په بریالیتوب سره یوځای شول.\n\nنوی لاسوند اوس {1} مخونه لري.\n\nنوی فایل:\n{2}\n\nد خوندي کولو ځای:\n{3}\n{2}\n\nآیا تاسو غواړئ دا PDF خلاص کړئ؟",
        'replace_file_title': "فایل بدل کړئ؟",
        'replace_file_message': "یو PDF دمخه خلاص دی. آیا تاسو غواړئ دا د نوي فایل سره بدل کړئ؟",
        'btn_yes': "هو",
        'btn_no': "نه",
        'filename_merge_suffix': "یوځای شوی",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "{0} خلاصیږي...",
        'progress_merge_reading': "{0} لوستل کیږي...",
        'progress_merge_adding': "{0} مخونه ورګډیږي...",
        'progress_merge_optimizing': "PDF غوره کیږي...",
        'progress_merge_writing': "PDF لیکل کیږي...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "د PDF بندول",
        'action_close_window': "د کړکۍ بندول",
        'action_open_new_pdf': "د نوي PDF خلاصول",
        'action_quit_app': "د اپلیکیشن څخه وتل",
        'changes_saved': "بدلونونه خوندي شول.",
        'file_close_title': "د PDF فایل بند کړئ",
        'save_before_action': "آیا باید د {0} دمخه بدلونونه خوندي شي؟ هو یا نه؟",
        'save_before_action_voice': "آیا باید د {0} دمخه بدلونونه خوندي شي؟ هو یا نه؟",
        'save_before_close_question': "آیا باید د بندولو دمخه بدلونونه خوندي شي؟ هو یا نه؟",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>د لټون وړ PDF جوړ شو:\n\n{0}\n\n<b>اړتیا وي بیا هڅه وکړئ",
        "ocr_rotate_title": "د OCR دمخه مخونه برابر کړئ",
        "ocr_rotate_question": "PDF څرخول شوي پاڼې لري.\nآیا تاسو غواړئ د OCR دمخه ټول پاڼې 0° ته برابر کړئ؟\nدا د متن پیژندنه د پام وړ ښه کوي.",
        "ocr_rotate_yes": "هو، برابر کړئ",
        "ocr_rotate_no": "نه، OCR مستقیم پیل کړئ",
        "ocr_rotate_voice": "PDF څرخول شوي پاڼې لري. ایا د OCR دمخه ټولې پاڼې باید برابرې شي؟",
        "ocr_not_performed_message": "کوم متن نشته. مهرباني وکړئ OCR ترسره کړئ (مینو \"سمول\" → \"OCR ترسره کړئ\" یا Ctrl+R کیلي).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "د OCR تنظیمات",
        "ocr_language_btn": "د OCR ژبه وټاکئ",
        "ocr_language": "د OCR ژبه(ګانې)",
        "ocr_language_current": "اوسنۍ ژبه:",
        "ocr_param_info": "د پیرامیټر په اړه معلومات",

        "ocr_force_ocr_label": "OCR مجبور کړئ",
        "ocr_deskew_label": "توروالی سم کړئ",
        "ocr_clean_label": "انځور پاک کړئ",
        "ocr_oversample_label": "رضولوشن (DPI)",
        "ocr_pagesegmode_label": "د پاڼې ویش",
        "ocr_oem_label": "د OCR انجن حالت",
        "ocr_optimize_label": "PDF فشار",
        "ocr_jobs_label": "موازي پروسې",
        "ocr_verbose_label": "د لاګ تفصیل",

        "ocr_force_ocr_tooltip": "په هر پاڼه کې OCR مجبور کړئ، حتی که متن له مخکې شتون ولري",
        "ocr_deskew_tooltip": "تور سکینونه په اتوماتیک ډول برابر کړئ",
        "ocr_clean_tooltip": "شور او مصنوعات له انځور څخه لرې کړئ",
        "ocr_oversample_tooltip": "د OCR دمخه انځور دې DPI ته لوی کړئ",
        "ocr_pagesegmode_tooltip": "ټاکي چې پاڼه څنګه د متن سیمو ویشل کیږي",
        "ocr_oem_tooltip": "د Tesseract OCR انجن غوره کوي",
        "ocr_optimize_tooltip": "د محصول PDF د فشار کچه",
        "ocr_jobs_tooltip": "د موازي OCR پروسو شمیر",
        "ocr_verbose_tooltip": "د لاګ محصول د تفصیل کچه",
        "ocr_settings_explain_btn": "تشریح",

        "ocr_force_ocr_explain": "په <b>هرې</b> پاڼه کې د متن پیژندنه مجبوروي (حتی که له مخکې متن ولري).\n\nسپارښتنه: <b>آن</b> د سکین شوي PDF لپاره، <b>بند</b> د اصلي PDF لپاره چې له مخکې متن لري.",

        "ocr_deskew_explain": "لږ تور سکینونه سم کوي (تر نږدې 5° پورې).\n\nسپارښتنه: <b>آن</b> د سکین شوي اسنادو لپاره، <b>بند</b> که پاڼې مخکې له دې په بشپړه توګه نېغې وي.",

        "ocr_clean_explain": "شور، ټکي او کوچني مصنوعات له انځور څخه لرې کوي.\n<b>مهم:</b> د عربي، تای یا ویتنامي متنونو لپاره چې د ډایکرټیک نښې لري (د تورو پورته/لاندې ټکي) دا اختیار باید <b>غیر فعال</b> شي، که نه نو مهم حروف له لاسه ورکول کیدی شي.",

        "ocr_oversample_explain": "انځور <b>د متن پیژندنې دمخه</b> ټاکلي DPI ته لوی کوي.<br><br>• <b>72-150 DPI:</b> ډیر چټک، مګر د پیژندنې ټیټه کچه<br>• <b>200-300 DPI:</b> غوره حد (تلوالی: 300)<br>• <b>400+ DPI:</b> په ستونزمنه توګه ښه پیژندنه، مګر د پام وړ لوی فایلونه<br><br>سپارښتنه: 300 DPI د پیچلو لیکدودونو لپاره (عربي، چیني، جاپاني)، 200 DPI د لویدیځو ژبو لپاره.",

        "ocr_pagesegmode_explain": "ټاکي چې Tesseract پاڼه څنګه د متن سیمو ویشي.\n\n• <b>3 - اتوماتیک (تلوالی):</b> د مخلوط ترتیباتو لپاره ښه\n• <b>4 - واحد کالم:</b> د واحد کالم متنونو لپاره\n• <b>5 - عمودی بلاک:</b> د عمودی لیکدودونو لپاره (جاپاني، چیني)\n• <b>6 - یو شان متن بلاک:</b> د کالمونو پرته د بهیدونکي متن لپاره غوره\n• <b>11 - خام انځور:</b> د خرابو سکینونو / لاس لیکلو لپاره\n\nسپارښتنه: <b>6</b> د ساده متن اسنادو لپاره، <b>3</b> د پیچلو ترتیباتو لپاره.",

        "ocr_oem_explain": "د Tesseract OCR انجن غوره کوي.\n\n• <b>0 - Legacy:</b> زوړ انجن (چټک، مګر لږ دقیق)\n• <b>1 - LSTM:</b> عصبي انجن (ورو، مګر ډیر دقیق)\n• <b>2 - Legacy + LSTM:</b> دواړه پایلې سره یوځای کوي\n• <b>3 - تلوالی (LSTM غوره دی):</b> د ډیرو مواردو لپاره غوره انتخاب\n\nسپارښتنه: <b>3</b> د اعظمي پیژندنې دقت لپاره.",

        "ocr_optimize_explain": "د محصول PDF فشاروي.\n\n• <b>0:</b> هیڅ اصلاح نه (چټکه پروسه)\n• <b>1:</b> لږ اصلاح (ښه جوړجاړی)\n• <b>2:</b> منځنۍ اصلاح\n• <b>3:</b> قوي اصلاح (ترینه کوچنۍ فایل، مګر ورو)\n\nسپارښتنه: <b>1</b> د ورځني استعمال لپاره.",

        "ocr_jobs_explain": "د OCR لپاره د موازي پروسو شمیر.\n\n• <b>1:</b> ورو، مګر ترټولو ټیټ حافظه مصرف\n• <b>4-8:</b> د عصري څو-کور پروسیسرونو لپاره غوره\n• <b>12+:</b> په ستونزمنه توګه چټکه پروسه د لوړ حافظې کارونې سره\n\nسپارښتنه: د CPU کورونو شمیر (لکه <b>4</b> په 4-کور سیسټمونو کې).",

        "ocr_verbose_explain": "په کونسول کې د لاګ محصول د تفصیل کچه.\n\n• <b>0:</b> هیڅ محصول نشته\n• <b>1:</b> پرمختګ او حالت پیغامونه\n• <b>2:</b> مفصل محصول\n• <b>3:</b> بشپړ ډیبګ محصول (ډیر پراخ)\n\nسپارښتنه: <b>1</b> د نورمال عملیاتو لپاره.",

        "ocr_reset_title": "تنظیمات بیا تنظیم شول",
        "ocr_reset_message": "د OCR ټول تنظیمات تلوالي ارزښتونو ته بیا تنظیم شول.",
        "info_tooltip": "د دې پیرامیټر په اړه نور معلومات",
        "ocr_reset_defaults": "تلوالي ته بیا تنظیم کړئ",

        "ocr_psm_0": "اتوماتیک (Legacy انجن)",
        "ocr_psm_1": "اتوماتیک کالم کشف",
        "ocr_psm_3": "اتوماتیک (تلوالی)",
        "ocr_psm_4": "واحد کالم",
        "ocr_psm_5": "عمودی بلاک",
        "ocr_psm_6": "یو شان متن بلاک",
        "ocr_psm_7": "واحد متن کرښه",
        "ocr_psm_8": "یوازنۍ کلمه",
        "ocr_psm_11": "خام انځور (د ترتیب تحلیل نشته)",

        "ocr_oem_0": "Legacy انجن (چټک)",
        "ocr_oem_1": "LSTM انجن (عصبي، دقیق)",
        "ocr_oem_2": "Legacy + LSTM یوځای شوی",
        "ocr_oem_3": "تلوالی (LSTM غوره دی)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "د OCR ژبه(ګانې)...",
        "ocr_language_title": "د OCR ژبه(ګانې) وټاکئ",
        "ocr_language_instruction": "د متن پیژندنې (OCR) لپاره ژبه(ګانې) وټاکئ.\nپاملرنه: څو ژبې د فعالیت او دقت په لګښت راځي!\nتاسو غوره پایلې ترلاسه کوئ که تاسو یوازې یوه ژبه وټاکئ.",
        "ocr_language_predefined": "له مخکې ټاکل شوي ترکیبونه",
        "ocr_language_custom": "دودیز...",
        "ocr_language_selected": "ټاکل شوي OCR ژبې",
        "ocr_language_changed": "د OCR ژبه {0} ته بدله شوه",
        "ocr_language_auto_detect": "شته ژبې په اتوماتیک ډول کشف کیږي.",
        "ocr_language_none_found": "د Tesseract ژبه مالومات وموندل شول! مهرباني وکړئ د ژبې بستې نصب کړئ (لکه 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "دودیز د ژبې انتخاب",
        "ocr_language_available": "شته ژبې (نصب شوي):",
        "ocr_language_select_hint": "یوه یا څو ژبې وټاکئ:",
        "ocr_language_confirm": "پلي کړئ",
        "ocr_language_reset": "تلوالي ته بیا تنظیم کړئ (deu+eng+vie)",
        "ocr_language_priorities": "سپارښتل شوې ژبې (له مخکې نصب شوي):",

        "select_all_languages": "ټول وټاکئ",
        "clear_all_languages": "انتخاب پاک کړئ",
        "install_language_packs": "د ورک شوو ژبو بستې نصب کړئ...",
        "install_hint": "💡 لارښوونه: ستاسو په سیسټم کې ټولې ژبې نصب شوي ندي. د دې تڼۍ له لارې به تاسو د نصبولو لپاره مرسته ترلاسه کړئ.",
        "ocr_language_install_title": "د Tesseract د ژبې بستو نصبول",

        "ocr_missing_languages": "ورک شوې د OCR ژبې بستې",
        "ocr_missing_languages_message": "لاندې ټاکل شوې ژبې ستاسو په سیسټم کې نصب شوي ندي:\n\n{0}\n\nمهرباني وکډئ ورک شوې د ژبې بستې نصب کړئ ('د نصبولو مرسته' کې مرسته وګورئ).\n\nآیا تاسو غواړئ اوس د نصبولو مرسته پرانیزئ؟",
        "ocr_missing_languages_voice": "ورک شوې د ژبې بستې. مهرباني وکړئ ورک شوې ژبې نصب کړئ.",
        "ocr_install_help_now": "مرسته پرانیزئ",
        "ocr_continue_anyway": "بیا هم هڅه وکړئ",
        "ocr_language_error_title": "د OCR ژبه تېروتنه",
        "ocr_language_error_message": "د متن پیژندنې پرمهال تېروتنه: {0}\n\nمهرباني وکړئ خپل د OCR ژبه تنظیمات وګورئ (تنظیمات → د OCR ژبه).",
        "ocr_install_help_button": "د نصبولو مرسته",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 د Tesseract د ژبې بستې نصب کړئ</p>

        <p>د دې لپاره چې OCR په یوه ځانګړې ژبه کار وکړي، اړونده د ژبې مالومات باید ستاسو په سیسټم کې نصب شوي وي. د خپل عملیاتي سیسټم لپاره لارښوونې تعقیب کړئ:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li><strong>ټرمینل</strong> پرانیزئ (Finder → پروګرامونه → اسانتیاوې → ټرمینل).</li>
        <li>ټولې شته ژبې د دې سره نصب کړئ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (دا څو دقیقې وخت نیسي.)</li>
        <li>یا یوازې انفرادي ژبې (لکه ویتنامي):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        د اوسني Homebrew نسخو سره، ممکن اړتیا وي چې <code>*.traineddata</code> په لاسي ډول ډاونلوډ شي (لاندې وګورئ).</li>
        <li>د نصبولو وروسته: دا ډیالوګ وتړئ او د OCR ژبه انتخاب بیا پرانیزئ – نوې ژبې به په اتوماتیک ډول ښکاره شي.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>یو ټرمینل پرانیزئ (Ctrl+Alt+T).</li>
        <li>مطلوبه ژبه نصب کړئ، د مثال په توګه د ویتنامي لپاره:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        مهم د ژبې کوډونه: <code>deu</code> (جرمني)، <code>eng</code> (انګلیسي)، <code>vie</code> (ویتنامي)، <code>spa</code> (هسپانوي)، <code>fra</code> (فرانسوي)، <code>ita</code> (ایټالوي)، <code>nld</code> (هالنډي)، <code>fin</code> (فینلینډي)، <code>swe</code> (سویډني)، <code>nor</code> (نارویژي).</li>
        <li>ټولې شته بستې وښایئ:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (لاسي)</p>
        <ol>
        <li>مطلوب <code>*.traineddata</code> فایلونه له دې ځایه ډاونلوډ کړئ:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (لکه <code>vie.traineddata</code> د ویتنامي لپاره).</li>
        <li>فایلونه د Tesseract د ژبې فولډر ته کاپي کړئ، معمولا:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (د انفرادي نصبولو سره سم تنظیم کړئ.)</li>
        <li>اپلیکیشن بیا پیل کړئ (یا د OCR ژبه انتخاب بیا پرانیزئ).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 د ټولو سیسټمونو لپاره بدیل</p>
        <ul>
        <li><strong>OCRmyPDF</strong> او <strong>Tesseract</strong> د خپلې خوښې د بستې مدیر سره نصب کړئ. ډیری نصبونو کې دمخه ځینې معیاري ژبې (انګلیسي، جرمني، فرانسوي) شاملې دي.</li>
        <li>ورک شوې ژبې په هر وخت کې نصب کیدی شي – د OCR ژبه انتخاب یوازې هغه ژبې لیست کوي چې په حقیقت کې شتون لري.</li>
        </ul>

        <hr>
        <p><b>✅ د نصبولو وروسته:</b> د اپلیکیشن بیا پیلولو اړتیا نشته – نوي اضافه شوې ژبې به سمدلاسه په لیست کې ښکاره شي.</p>
        <p><b>📖 د ژبې کوډونو لپاره مرسته:</b> یو بشپړ لیست د <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract اسناد</a> کې شتون لري.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "د Noto Sans توري",
        "info_noto_font_voice": "د Noto Sans تورو نصبولو لارښود",
        "btn_info_noto_font_install": "د توري مالومات",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word; direction: ltr; text-align: left;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ د Google څخه د وړیا Noto تورو نصبولو څرنګوالی</h2>

        <p><strong>Noto توري</strong> د Google څخه د خلاص سرچینې توری کورنۍ ده. د دوی هدف د <em>"هیڅ توفو"</em> (یعنې هیڅ خالي بکسونه □) لیدل او د یونیکوډ معیار څخه هر حرف په سمه توګه ښودل دي. دوی د هغو اپلیکیشنونو لپاره مثالي اضافه دي چې باید په ډیرو مختلفو ژبو کې متنونه وښیي.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 په macOS کې نصبول</h3>

        <p><strong>میتود 1: د Homebrew سره (د پرمختللو کاروونکو لپاره)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>میتود 2: د "فونټ کتاب" له لارې (سپارښتل شوی)</strong></p>

        <ol>
        <li>رسمي تورې بسته ډاونلوډ کړئ:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>د ZIP فایل استخراج کړئ</li>
        <li>فایلونه <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code> ته کاپي کړئ</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 په Windows کې نصبول (10 او 11)</h3>

        <p><strong>میتود 1: Microsoft Store (سپارښتل شوی)</strong><br>
        د "Google Noto Fonts" یا "Noto Sans" لټون وکړئ او په <strong>نصب کړئ</strong> کلیک وکړئ.</p>

        <p><strong>میتود 2: لاسي نصبول</strong></p>

        <ol>
        <li>ډاونلوډ:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP استخراج کړئ</li>
        <li>.ttf / .otf فایلونه وټاکئ</li>
        <li>ښي کلیک → <strong>نصب کړئ</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        یا<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\نوم\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 په Linux کې نصبول</h3>

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
        "bookmark_dialog_title": "نښانونه اداره کړئ",
        "bookmark_add": "نښان اضافه کړئ",
        "bookmark_add_tooltip": "اوسنۍ پاڼه د نښان په توګه خوندي کړئ",
        "bookmark_remove": "نښان لرې کړئ",
        "bookmark_remove_tooltip": "نښه شوی نښان ړنګ کړئ",
        "bookmark_remove_all": "ټول لرې کړئ",
        "bookmark_remove_all_tooltip": "د دې PDF ټول نښانونه ړنګ کړئ",
        "bookmark_jump": "نښان ته لاړ شئ",
        "bookmark_jump_tooltip": "ټاکل شوي پاڼې ته لاړ شئ",
        "bookmark_name": "نوم",
        "bookmark_page": "پاڼه",
        "bookmark_no_bookmarks": "هیڅ نښان نشته.\nد اوسنۍ پاڼې د نښان په توګه خوندي کولو لپاره 'اضافه کړئ' کلیک وکړئ.",
        "bookmark_added": "د پاڼې {0} لپاره نښان اضافه شو: {1}",
        "bookmark_removed": "نښان لرې شو: {0}",
        "bookmark_all_removed": "ټول نښانونه لرې شول.",
        "bookmark_name_default": "پاڼه {0}",
        "bookmark_name_prompt": "د نښان لپاره نوم:\n(اوږد متن به 50 تورو ته لنډ شي)",
        "bookmark_name_prompt_title": "د نښان نوم",
        "bookmark_confirm_remove_all": "آیا تاسو ډاډه یاست چې غواړئ ټول {0} نښانونه لرې کړئ؟",
        "menu_bookmarks": "نښانونه",
        "bookmark_manage": "نښانونه اداره کړئ",
        "bookmark_next": "بل نښان",
        "bookmark_prev": "مخکینی نښان",
        "bookmark_page_display": "پاڼه {0}",
        "bookmark_exists": "د دې پاڼې لپاره د دې نوم سره یو نښان له مخکې شتون لري.",
        "bookmark_select_first": "مهرباني وکړئ لومړی یو نښان وټاکئ.",
        "bookmark_confirm_remove": "آیا تاسو ډاډه یاست چې غواړئ د 'پاڼه {0}: {1}' نښان لرې کړئ؟",
        "bookmark_jumped_to": "په پاڼه {1} کې د نښان '{0}' ته لاړ شئ.",
        "bookmark_jumped_to_voice": "نښان {0}، پاڼه {1}",
        "btn_close": "تړل",

        "bookmark_list": "ستاسو نښانونه",
        "bookmark_rename": "نښان بیا نومول",
        "bookmark_rename_tooltip": "د ټاکل شوي نښان نوم بدل کړئ",
        "bookmark_rename_title": "نښان بیا نومول",
        "bookmark_rename_prompt": "په پاڼه {0} کې د نښان لپاره نوی نوم:\n(تر ټولو زیات 50 توري)",
        "bookmark_renamed": "نښان '{0}' په '{1}' بیا نومول شو.",
        "bookmark_item_tooltip": "پاڼه {0}: {1}\nد تګ لپاره دوه ځله کلیک وکړئ",
        "bookmark_name_exists_question": "په دې پاڼه کې له مخکې د '{0}' نوم سره یو نښان شتون لري.\nبیا هم نوم بدل کړئ؟",

        "context_bookmarks": "نښانونه",
        "context_bookmark_add_here": "د دې پاڼې لپاره نښان اضافه کړئ",
        "context_bookmarks_existing": "شته نښانونه:",
        "context_bookmarks_jump": "نښان ته لاړ شئ:",
        "context_bookmarks_none": "هیڅ نښان نشته",
        "context_bookmarks_clear_all": "ټول {0} نښانونه لرې کړئ",

        "bookmark_search_placeholder": "نښانونه وپلټئ... (نوم یا پاڼه)",
        "bookmark_search_results": "د \"%s\" لپاره %d نښانونه وموندل شول",
        "bookmark_no_search_results": "د \"%s\" لپاره هیڅ نښان ونه موندل شو",
        "bookmark_no_search_results_label": "د \"%s\" لپاره هیڅ پایله نشته",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "د PDF میټاډاټا سم کړئ",
        "metadata_title": "سرلیک",
        "metadata_title_placeholder": "د سند سرلیک",
        "metadata_title_tooltip": "د سند سرلیک (د سرلیک په بار کې ښودل شوی)",
        "metadata_author": "لیکوال",
        "metadata_author_placeholder": "د لیکوال نوم",
        "metadata_author_tooltip": "د سند جوړونکی",
        "metadata_subject": "موضوع",
        "metadata_subject_placeholder": "د سند موضوع",
        "metadata_subject_tooltip": "د منځپانګې لنډ توضیح",
        "metadata_keywords": "کلیدي کلمې",
        "metadata_keywords_placeholder": "کلیدي کلمې، د کوما په واسطه جلا شوي",
        "metadata_keywords_tooltip": "د سند طبقه بندي لپاره کلیدي کلمې",
        "metadata_creator": "جوړونکی",
        "metadata_creator_placeholder": "اپلیکیشن چې PDF یې جوړ کړی",
        "metadata_creator_tooltip": "سافټویر چې سند ورسره جوړ شوی",
        "metadata_producer": "تولیدونکی",
        "metadata_producer_placeholder": "اپلیکیشن چې PDF یې بدل کړی",
        "metadata_producer_tooltip": "سافټویر چې PDF یې بدل کړی",
        "metadata_creation_date": "د جوړیدو نیټه",
        "metadata_creation_date_tooltip": "د سند جوړیدو نیټه",
        "metadata_mod_date": "د بدلون نیټه",
        "metadata_mod_date_tooltip": "د وروستي بدلون نیټه",
        "metadata_pdf_info": "📄 د PDF معلومات",
        "metadata_pages": "د پاڼو شمیر",
        "metadata_file_size": "د فایل اندازه",
        "metadata_pdf_version": "د PDF نسخه",
        "metadata_encrypted": "کوډ شوی",
        "metadata_encrypted_yes": "هو (د پاسورډ لخوا خوندي شوی)",
        "metadata_encrypted_no": "نه",
        "metadata_reload": "📂 له PDF څخه بیا بار کړئ",
        "metadata_reset": "بدلونونه رد کړئ",
        "metadata_reloaded": "میټاډاټا له PDF څخه بیا بار شو.",
        "metadata_reset_done": "د میټاډاټا ټول ساحې بیا تنظیم شوې.",
        "metadata_no_file": "هیڅ PDF فایل نه دی بار شوی.",
        "metadata_save_error": "د میټاډاټا خوندي کولو کې تېروتنه",
        "metadata_saved": "میټاډاټا په بریالیتوب سره خوندي شو.",
        "metadata_pdf_version_unknown": "PDF (نامعلوم)",
        "metadata_saved_message": "میټاډاټا په بریالیتوب سره خوندي شو.",
        "metadata_saved_voice": "میټاډاټا خوندي شو.",

        "metadata_custom": "🔧 دودیز میټاډاټا",
        "metadata_custom_placeholder": "{\n  \"زما_ساحه\": \"زما_ارزښت\",\n  \"بله_ساحه\": 123\n}",
        "metadata_custom_tooltip": "د دودیز میټاډاټا لپاره JSON بڼه (اختیاري)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "د \"{0}\" قالب وټاکل شو - د داخلولو لپاره دوه ځله کلیک وکړئ",
        "text_use_template": "د متن بلاک وکاروئ",
        "text_type": "ډول",
        "text_search_templates": "د متن بلاکونه وپلټئ...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 د برونډ / وارداتو معلومات",
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

        <h3>📦 څه شی صادرېږي؟ (کتنه)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">د اپلیکیشن عمومي تنظیمات</span></li>
            <li class="detail">• تیاره/روښانه حالت</li>
            <li class="detail">• د انځورونو لپاره د تیاره حالت انعکاس</li>
            <li class="detail">• د خړ حد ارزښت</li>
            <li class="detail">• ژبه</li>
            <li class="detail">• د کړکۍ جیومیټري</li>
            <li class="detail">• لویول حالت</li>
            <li class="detail">• لارښود (د لارښود بار ښکاره دی)</li>
            <li class="detail">• د وینا محصول (آن/بند)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">د بیک اپ تنظیمات</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">د فایل نومول (د وخت ټاپه، جلاکوونکی، ضمیمې)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">د داخلولو لپاره تنظیمات</span></li>
            <li class="detail">• لاسلیکونه</li>
            <li class="detail">• متن او د متن بلاکونه</li>
            <li class="detail">• نښان، انځورونه او شکلونه</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">د OCR تنظیمات</span></li>
            <li class="detail">• ژبه</li>
            <li class="detail">• OCR مجبور کړئ · د پاڼې حالت</li>
            <li class="detail">• د انځور مخکې پروسس: توروالی سم کړئ، پاک کړئ، ډیر نمونه اخیستل</li>
            <li class="detail">• د موازي دندو شمیر</li>
            <li class="detail">• د انعکاس حالت</li>
            <li class="detail">• د خړ حد ارزښت</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">نښانونه</span></li>
            <li class="detail">• د هر PDF فایل لپاره ټول نښانونه (پاڼه، نوم، د جوړیدو وخت)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">د پاسورډ ډیټابیس</span></li>
            <li class="detail">• خوندي شوي PDF پاسورډونه (اختیاري کوډ شوي یا ساده متن)</li>
            <li class="detail">• د ماسټر پاسورډ هش (که ټاکل شوی وي)</li>
            <li class="detail">• تایید معلومات</li>
        </ul>

        <h4>⚠️ مهم یادښتونه</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 د واردولو پر مهال:</strong>
            <ul>
                <li><span class="warning">➜ ټول اوسني تنظیمات به په بشپړه توګه له سره ولیکل شي</span></li>
                <li>• د اپلیکیشن بیا پیلول اړین دي</li>
                <li>• شته لاسلیکونه، د متن بلاکونه او نښانونه به ځای په ځای شي</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 د ماسټر پاسورډ او صادرولو حالت:</strong>
            <ul>
                <li>• کله چې ماسټر پاسورډ فعال وي، تاسو کولی شئ انتخاب وکړئ:</li>
                <li>  - <span style="color: #98FB98;"><strong>کوډ خلاص شوی</strong></span> (پاسورډونه په ZIP کې په ساده متن کې دي)</li>
                <li>  - <span style="color: #FFA07A;"><strong>کوډ شوی</strong></span> (یوازې د ماسټر پاسورډ سره په هدف سیسټم کې لوستل کیدی شي)</li>
                <li>• د ماسټر پاسورډ هش <strong>تل</strong> کوډ شوی ساتل کیږي</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ امنیتي خبرتیا:</strong>
            <ul>
                <li>• صادره شوې ZIP فایل حساس معلومات لري (<strong>پاسورډونه، نښانونه، لاسلیکونه</strong>)</li>
                <li>• مهرباني وکړئ دا په خوندي ځای کې وساتئ (لکه کوډ شوی USB سټیک، د پاسورډ مدیر)</li>
                <li>• که فایل ورک شي، خوندي شوي PDF پاسورډونه به د نه جبران کیدونکي توګه ورک شي</li>
            </ul>
        </div>

        <h4>📁 د صادرولو بڼه</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            تنظیمات په یوه ZIP فایل کې خوندي کیږي:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            دې ZIP فایل کې بشپړ <code>settings.json</code> (ستاسو د ترتیب څخه) او همدارنګه ممکن ځای پر ځای شوي لاسلیک انځور فایلونه او کوډ شوي پاسورډونه شامل دي.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "لاسلیکونه - لارښود",
        'signature_guide_html': """
        📝 <strong>لاسلیکونه - چټک لارښود</strong><br>
        <ul>
        <li>ماسټر پټنوم ټاکل</li>
        <li>لاسلیکونه د <em>تنظیماتو</em> مینو کې تنظیم کړئ (اندازه، وخت ټاپ، …)</li>
        <li>په مطلوب ځای کې د <strong>ښي کلیک</strong> سره داخل کړئ (ماسټر پټنوم په هره ناسته کې یو ځل اړین دی)</li>
        <li>لاسلیک د موس یا تیر کیلي سره حرکت ورکړئ</li>
        <li>یو له بل پسې ډیری لاسلیکونه داخل کړئ</li>
        <li>هر لاسلیک په انفرادي ډول تنظیم کړئ</li>
        <li>یوازینی لاسلیک رد کړئ</li>
        <li>ټول لاسلیکونه یو ځل خوندي / رد کړئ</li>
        <li>په بدیل سره، د مینو بار هم کارول کیدی شي.</li>
        </ul>
        """,
        'signature_guide_voice': "د لاسلیکونو لپاره چټک لارښود. ماسټر پټنوم ټاکل. په تنظیماتو کې لاسلیکونه تنظیم کړئ. د ښي کلیک سره داخل کړئ.",

        'image_guide_title': "انځورونه داخل کړئ - لارښود",
        'image_guide_html': """
        📷 <strong>PDF ته انځورونه داخل کړئ - چټک لارښود</strong><br>
        <ol>
        <li>په مطلوب ځای کې ښي کلیک وکړئ</li>
        <li><em>„انځور داخل کړئ“</em> → انځور غوره کړئ</li>
        <li>انځور ځای په ځای کړئ: د موس سره کش کړئ</li>
        <li>اندازه تنظیم کړئ: په کونجونو/څنډو کې کش کړئ</li>
        <li>اړخ تناسب وساتئ: <strong>[A]</strong> کیلي</li>
        <li>نور تنظیمات: په انځور کې ښي کلیک وکړئ</li>
        </ol>
        <p><strong>لارښوونه:</strong> د شرایطو مینو کې تاسو تنظیمات تنظیم کولی شئ.</p>
        """,
        'image_guide_voice': "د انځورونو لپاره چټک لارښود. ښي کلیک، انځور داخل کړئ، غوره کړئ. د موس سره ځای په ځای کړئ، په کونجونو کې اندازه تنظیم کړئ. د A کیلي سره اړخ تناسب.",

        'form_guide_title': "شکله داخل کړئ - لارښود",
        'form_guide_html': """
        📐 <strong>PDF ته شکله داخل کړئ - چټک لارښود</strong><br>
        <ol>
        <li>د شکل ډول غوره کړئ (مستطیل، بیضوی، کرښه، تیر)</li>
        <li>په موقعیت کلیک وکړئ:
            <ul>
            <li>د مستطیل/بیضوي لپاره: یو کلیک شکل ځای په ځای کوي</li>
            <li>د کرښې/تیر لپاره: د پیل او پای نقطې لپاره دوه کلیکونه</li>
            </ul>
        </li>
        <li>شکل ځای په ځای کړئ: د موس سره کش کړئ</li>
        <li>اندازه تنظیم کړئ: په کونجونو/څنډو کې کش کړئ</li>
        <li>شکل خوندي کړئ: <strong>Enter</strong></li>
        <li>شکل رد کړئ: <strong>ESC</strong></li>
        <li>نور تنظیمات: په شکل کې ښي کلیک وکړئ</li>
        </ol>
        <p><strong>لارښوونه:</strong> د شرایطو مینو کې تاسو تنظیمات تنظیم کولی شئ.</p>
        """,
        'form_guide_voice': "د شکلونو لپاره چټک لارښود. د شکل ډول غوره کړئ. د مستطیل یا بیضوي لپاره یو ځل کلیک وکړئ، د کرښې یا تیر لپاره دوه ځله. د موس سره ځای په ځای کړئ، په کونجونو کې اندازه تنظیم کړئ. د Enter سره خوندي کړئ، د Escape سره رد کړئ.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "پخوانی",
        "btn_next_result": "راتلونکی",
        "ocr_text_window": "OCR متن کړکۍ",
        "bookmark_existing": "شته نښانونه",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR پرتله کول Mac - Windows",
        'ocr_method_mac_win_title': "د Mac او Windows ترمنځ OCR توپیرونه",
        'ocr_method_mac_win_voice': "Mac غوره دی",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – د macOS او Windows ترمنځ توپیرونه</strong></p>

        <p><strong>macOS (سپارښت شوی)</strong></p>
        <p>وسیله:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>پایلې:</p>
        <ul>
        <li>د لټون وړ PDF چې په کې ځای پر ځای شوی متن شامل دی او اصلي ترتیب په لویه کچه ساتي.</li>
        </ul>
        <p>ګټې:</p>
        <ul>
        <li>د متن پیژندنې غوره کیفیت (حتی په کږو پاڼو کې).</li>
        <li>د ویکتور ګرافیکونو او فونټونو ساتل.</li>
        <li>د فرعي پروسې ارزونې له لارې GUI پرمختګ بار.</li>
        <li>د ټولو OCR پیرامیټرو بشپړ کنټرول (Deskew, Clean, Oversample, اصلاح کول).</li>
        <li>د متن لټون په مستقیم ډول په اصلي کړکۍ (PDF لید) کې شتون لري.</li>
        </ul>
        <p>نیمګړتیاوې:</p>
        <ul>
        <li>اضافي سیسټم وسیلو ته اړتیا لري (ocrmypdf, Ghostscript, unpaper, pngquant – د اپلیکیشن بنډل کې شامل دي).</li>
        <li>پیچلي تېروتنې اداره کول (تړل کیدنه، وخت تیریدنه).</li>
        </ul>

        <p><strong>Windows (باثباته بدیل)</strong></p>
        <p>وسیله:</p>
        <ul>
        <li>pytesseract (Tesseract سره مستقیم اړیکه) + reportlab + PyPDF2</li>
        </ul>
        <p>پایلې:</p>
        <ul>
        <li>د لټون وړ PDF چې په لید کې د انځور PDF سره مطابقت لري، مګر د شفاف متن له لارې د لټون وړ دی.</li>
        </ul>
        <p>ګټې:</p>
        <ul>
        <li>اوس مهال کومه نه را په یاد کیږي.</li>
        </ul>
        <p>نیمګړتیاوې:</p>
        <ul>
        <li>PDF په اصل کې د نه لیدونکي متن سره یو انځور دی؛ ترتیب کیدای شي د پیچلو اسنادو (کالمونو، جدولونو) لپاره یو څه انحراف وکړي.</li>
        <li>هیڅ اتوماتیک کږوالي سمونه (--deskew) یا د انځور پاکول (--clean) نشته.</li>
        <li>GUI پرمختګ بار یوازې د پروسس شوي پاڼو شمیر پر بنسټ په ټولیز ډول تازه کیږي.</li>
        <li>OCR سرعت یو څه ورو دی (ځکه چې هر پاڼه په جلا توګه پروسس کیږي).</li>
        <li>د متن لټون د OCR متن کړکۍ ته لیږدول کیږي.</li>
        </ul>

        <p><strong>ګډې ځانګړتیاوې</strong></p>
        <ul>
        <li>دواړه میتودونه د سرچینې فایل سره په ورته لارښود کې د لټون وړ PDF رامینځته کوي.</li>
        <li>د OCR تنظیمات (ژبه، DPI، د پاڼې برخه بندولو حالت، د OCR انجن حالت) د OCRSettingsDialog له لارې تنظیم کیدی شي او په دواړو تطبیقاتو کې اغیزمن دي.</li>
        </ul>

        <p><strong>سپارښتنه:</strong></p>
        <ul>
        <li>macOS: د ocrmypdf بائنری غوره پایلې وړاندې کوي – Mac واخلئ او نسخه وکاروئ (د Apple Silicon یا Intel چپ سره د Mac لپاره PDFDarkView). د OCR پایلې د Windows په پرتله غوره دي!</li>
        <li>Windows: د pytesseract حل وکاروئ. دا باثباته دی او د ډیری اسنادو لپاره په بشپړ ډول کافي کیفیت وړاندې کوي.</li>
        </ul>

        <p><strong>مهم یادونه:</strong></p>
        <ul>
        <li>دواړه نسخې په بشپړه توګه د کارونکي انٹرفیس سره مدغم شوي دي – کارونکی هیڅ توپیر نه احساسوي.</li>
        <li>پروګرام پخپله پریکړه کوي چې کوم OCR انجن د عملیاتي سیسټم پر بنسټ وکاروي.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "لاسلیک جوړ کړئ (له سکین څخه)",
        "signature_create_title": "سکین شوی لاسلیک غوره کړئ (PDF/انځور)",
        "image_pdf_filter": "انځورونه او PDF",
        "signature_pdf_empty": "PDF کې هیڅ پاڼې ندي.",
        "signature_created_success": "لاسلیک په بریالیتوب سره جوړ شو: {0}",
        "signature_create_error": "د لاسلیک جوړولو پر مهال تېروتنه:\n{0}",
        "rembg_missing": "rembg نصب شوی نه دی.\nمهرباني وکړئ نصب کړئ: pip install rembg\nتېروتنه: {0}",
        "signature_name_title": "د لاسلیک لپاره د فایل نوم",
        "signature_name_message": "مهرباني وکړئ د نوي لاسلیک لپاره د فایل نوم دننه کړئ (د شفاف شالید سره د PNG په توګه به خوندي شي):",
        "signature_name_label": "د فایل نوم:",
        "signature_name_voice": "د لاسلیک لپاره د فایل نوم دننه کړئ",
        "signature_processing": "پروسس روان دی...",
        "signature_creation_title": "لاسلیک جوړیږي",
        "signature_overwrite_warning": "فایل '{0}' دمخه شتون لري. بیا لیکنه؟",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"د لاسلیک لپاره PDF چمتو کړئ",
        "signature_prepare_instruction":"مهرباني وکړئ یو PDF غوره کړئ چې په یوه پاڼه کې سکین شوی لاسلیک ولري.\n\nد غوره پیژندلو لپاره ډاډ ترلاسه کړئ چې:\n• لاسلیک په سپین کاغذ کې په تور رنګ (بالپوائنټ یا فاین لاینر) لیکل شوی وي.\n• لاسلیک د بل ډول خالي A4 پاڼې په پورتنۍ دریمه برخه کې موقعیت ولري.\n• PDF لږترلږه په 300 dpi سکین شوی وي.\n• لاسلیک روښانه وي او ډیر نری نه وي.\n• هیڅ ډول ګډوډونکی شالید نمونه یا کرښې شتون ونلري.",
        "signature_prepare_voice":"مهرباني وکړئ د سکین شوي لاسلیک سره PDF غوره کړئ. ښه کیفیت او توپیر ته پام وکړئ.",
        "sig_thickness_label":"د کرښې ضخامت:",
        "sig_thickness_normal":"نورمال (نری)",
        "sig_thickness_bold":"بولډ (سپارښت شوی)",
        "sig_thickness_very_bold":"ډیر بولډ",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI او OCR ژبو اضافه کړئ - لارښود",
        'language_guide_title': "GUI او OCR ژبو اضافه کړئ",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>غوښتل شوی ژباړې فایل <code>translations_xy.py</code> دلته ډاونلوډ کړئ<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        او په لاندې لارښود کې یې ځای په ځای کړئ:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>خپل ویب براوزر خلاص کړئ.</li>
        <li>دلته لاړ شئ: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>د سکرین ښي غاړې کې د "Releases" په لټه کې شئ او هغه غوره کړئ چې د <strong>"latest"</strong> سره نښه شوی.</li>
        <li>په راتلونکي خپرونې پاڼه کې، په ډیر ښکته کې د <code>Source Code.zip</code> فایل ډاونلوډ کړئ.</li>
        <li>ZIP فایل انزپ کړئ.</li>
        <li>په انزپ شوي فولډر کې ټول هغه ژبنیز فایلونه ولټوئ چې تاسو ورته اړتیا لرئ، او دوی لارښود ته کاپي کړئ:<br/>
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
        "menu_watermark":"د اوبو نښه داخلول",
        "fullpage_text_watermark_title":"متن د اوبو د نښې په توګه",
        "fullpage_image_watermark_title":"انځور د اوبو د نښې په توګه",
        "filename_with_watermark":"_د_اوبو_نښې_سره",
        "watermark_text":"متن:",
        "watermark_text_placeholder":"ستاسو د اوبو نښې متن...",
        "watermark_font_family":"فونټ:",
        "watermark_font_size":"د فونټ اندازه:",
        "watermark_format":"بڼه:",
        "watermark_bold":"زغرد",
        "watermark_italic":"تېر",
        "watermark_color":"رنګ:",
        "watermark_choose_color":"رنګ وټاکئ...",
        "watermark_opacity":"ناڅرګندتیا / څرګندتیا:",
        "watermark_direction":"د لوستلو لور:",
        "watermark_direction_l_r":"کیڼ → ښي",
        "watermark_direction_bl_tr":"لاندې کیڼ → پورته ښي",
        "watermark_direction_tl_br":"پورته کیڼ → لاندې",
        "watermark_direction_b_t":"لاندې → پورته",
        "watermark_direction_t_b":"پورته → لاندې",
        "watermark_preview":"مخکتنه:",
        "watermark_preview_sample":"نمونه متن",
        "watermark_empty_text":"مهرباني وکړئ متن داخل کړئ.",
        "watermark_applied":"د اوبو نښه په ټولو مخونو کې پلي شوه.",
        "watermark_saved":"د اوبو نښه خوندي شوه.",
        "image_scale":"اندازه:",
        "image_preview":"د انځور مخکتنه:",
        "no_image_selected":"هیڅ انځور نه دی ټاکل شوی",
        "browse":"لټون...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact":"سور تېرونه",
        "redact_add_black":"سور تېر (تور)",
        "redact_add_white":"سور تېر (سپین / ړنګول)",
        "redact_added_black":"تور سور تېر زیات شو",
        "redact_added_white":"سپین سور تېر زیات شو",
        "redact_apply_all":"ټول سور تېرونه پلي کړئ او خوندي یې کړئ",
        "redact_discard_all":"ټول سور تېرونه رد کړئ",
        "redact_discard":"دا سور تېر رد کړئ",
        "no_redactions":"هیڅ سور تېرونه نشته",
        "redact_confirm_title":"سور تېرونه په دایمي ډول پلي کړئ",
        "redact_confirm_message":"خبرداری: نښه شوي سیمې به په دایمي ډول ړنګ شي (تور یا سپین).\nبیک اپ به جوړ شي (که چیرې فعال شوی وي).\n\nپرمخ وړل؟",
        "redact_apply":"هو، اوس سور تېر کړئ",
        "redact_saved":"{0} سور تېر(ونه) په بریالیتوب سره پلي او خوندي شول.",
        "redact_saved_voice":"{0} سور تېر(ونه) پلي شول",
        "redact_error":"د سور تېر پرمهال تېروتنه",
        "filename_redacted":"_سور_تېر_شوی",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'د مخ شمېرې داخلول',
        'page_numbers_format': 'د شمېرې بڼه:',
        'page_numbers_format_arabic': '1, 2, 3 ... (عربي)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (رومي کوچني)',
        'page_numbers_format_roman_upper': 'I, II, III ... (رومي لوی)',
        'page_numbers_format_letter': 'A, B, C ... (توري)',
        'page_numbers_format_custom': 'دودیز',
        'page_numbers_custom_pattern': 'بڼه:',
        'page_numbers_custom_placeholder': 'لکه "مخ {nummer}" یا "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'د اوسني مخ شمېرې لپاره {nummer} او د ټول شمېر لپاره {total} وکاروئ',
        'page_numbers_position': 'موقعیت:',
        'page_numbers_pos_tl': 'پورته کیڼ',
        'page_numbers_pos_tc': 'پورته منځ',
        'page_numbers_pos_tr': 'پورته ښي',
        'page_numbers_pos_ml': 'منځ کیڼ',
        'page_numbers_pos_mc': 'منځ کې',
        'page_numbers_pos_mr': 'منځ ښي',
        'page_numbers_pos_bl': 'لاندې کیڼ',
        'page_numbers_pos_bc': 'لاندې منځ',
        'page_numbers_pos_br': 'لاندې ښي',
        'page_numbers_margins': 'څنډې:',
        'page_numbers_margin_x': 'افقي واټن:',
        'page_numbers_margin_y': 'عمودي واټن:',
        'page_numbers_range': 'د مخ سلسله:',
        'page_numbers_all_pages': 'ټول مخونه',
        'page_numbers_custom_range': 'دودیزه سلسله',
        'page_numbers_from': 'له:',
        'page_numbers_to': 'تر:',
        'page_numbers_progress': 'د مخ شمېرې داخلېږي...',
        'page_numbers_start': 'د مخ شمېرو داخلول پیلېږي...',
        'page_numbers_cancel': 'د مخ شمېرو داخلول لغوه شول',
        'page_numbers_success': 'د مخ شمېرې په بریالیتوب سره زیاتې شوې.\n\nآیا غواړئ نوی PDF پرانیزئ؟\n\n{0}',
        'page_numbers_complete': 'د مخ شمېرې زیاتې شوې',
        'page_numbers_error_format': 'د مخ شمېرو په داخلولو کې تېروتنه: {0}',
        'page_numbers_content_type': 'د مینځپانګې ډول:',
        'page_numbers_tab_simple': 'ساده شمېره',
        'page_numbers_tab_range': 'مخ X د Y څخه',
        'page_numbers_tab_date': 'نېټه',
        'page_numbers_tab_custom': 'خپلواک متن',
        'page_numbers_range_format': 'بڼه:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'مخ {aktuell} د {gesamt} څخه',
        'page_numbers_range_custom': 'دودیز',
        'page_numbers_range_placeholder': 'لکه "مخ {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'د نېټې بڼه:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 جنوري 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'دودیز',
        'page_numbers_date_placeholder': 'لکه %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'موقعیت:',
        'page_numbers_date_before': 'نېټه د مخ شمېرې مخکې',
        'page_numbers_date_after': 'نېټه د مخ شمېرې وروسته',
        'page_numbers_date_only': 'یوازې نېټه (د مخ شمېرې پرته)',
        'page_numbers_custom_text': 'دودیز متن:',
        'page_numbers_custom_placeholder_text': 'د مخ شمېرې لپاره {seite} او د ټول شمېر لپاره {gesamt} وکاروئ\nلکه "محرمانه - مخ {seite}" یا "{seite} د {gesamt} څخه"',
        "filename_with_page_number":"_د_مخ_شمېرې_سره",
        "filename_with_page_declaration":"_د_مخ_اعلامیې_سره",
        "filename_with_pagenumber":"_د_مخ_شمېرې_سره",
        "filename_with_date":"_د_نېټې_سره",
        "filename_with_my_page_declaration":"_د_دودیز_مخ_اعلامیې_سره",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "نه خوندي شوي بدلونونه",
        "unsaved_changes_message_darkmode": "نه خوندي شوي داخلونه شتون لري.\nآیا غواړئ د بدلولو مخکې یې خوندي کړئ؟",
        "save_and_switch": "خوندي کړئ او بدل کړئ",
        "discard_and_switch": "اوس بدل کړئ",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'مخونه د انځورونو په توګه صادر کړئ',
        'export_images_menu': 'د انځورونو په توګه صادر کړئ (PNG/JPEG)',
        'export_images_format': 'د انځور بڼه:',
        'export_images_dpi': 'رېزولوشن (DPI):',
        'export_images_quality': 'د JPEG کیفیت:',
        'export_images_range': 'د مخ سلسله:',
        'export_images_all_pages': 'ټول مخونه',
        'export_images_custom_range': 'دودیزه سلسله',
        'export_images_from': 'له:',
        'export_images_to': 'تر:',
        'export_images_options': 'اختیارونه:',
        'export_images_single_files': 'هر مخ د جلا فایل په توګه',
        'export_images_subfolder': 'فرعي فولډر ته صادر کړئ',
        'export_images_subfolder_info': '"PDFنوم_انځورونه" فرعي فولډر ته',
        'export_images_same_folder': 'د PDF په ورته فولډر کې',
        'export_images_apply_darkmode': 'د PDFDarkView ترتیبات پلي کړئ (تیاره حالت)',
        'export_images_target_folder': 'هدف فولډر:',
        'export_images_browse': 'لټون...',
        'export_images_preview': 'مخکتنه:',
        'export_images_preview_info': 'د صادرولو لپاره ترتیبات وټاکئ',
        'export_images_preview_info_detail': '{0} مخونه د {1} په توګه\nرېزولوشن: {2} DPI\nد فایل نوم: {3}\n{4}',
        'export_images_select_folder': 'هدف فولډر وټاکئ',
        'export_images_start': 'د انځور صادرول پیلېږي...',
        'export_images_progress': 'انځورونه صادرېږي...',
        'export_images_saving': 'مخ {0} د {1} څخه خوندي کېږي...',
        'export_images_success': 'صادرول بریالي شول!\n\n{0} انځورونه په دې کې خوندي شول:\n{1}',
        'export_images_complete': 'د انځور صادرول بشپړ شول',
        'export_images_open_folder': '📁 فولډر پرانیزئ',
        'export_images_cancel': 'د انځور صادرول لغوه شول',
        'export_images_error_format': 'د انځورونو په صادرولو کې تېروتنه: {0}',
        'export_images_pdf2image_missing': 'د "pdf2image" کتابتون نصب شوی نه دی.\n\nمهرباني وکړئ د دې سره یې نصب کړئ:\npip install pdf2image\n\nد Windows لپاره تاسو Poppler ته هم اړتیا لرئ:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'د اوږد مهاله آرشیف لپاره PDF/A بدلون',
        'pdfa_menu': 'PDF/A بدلون (د آرشیف وړ)',
        'pdfa_info': 'PDF د PDF/A بڼې ته بدلوي.\n\nPDF/A په ځانګړي ډول د اوږد مهاله آرشیف لپاره ډیزاین شوی او ډاډ ورکوي چې سند به په راتلونکي کې سم وښودل شي.',
        'pdfa_standard': 'د PDF/A معیار:',
        'pdfa_standard_select': 'نسخه:',
        'pdfa_1': 'PDF/A-1 (ساده، پراخه مطابقت لرونکی)',
        'pdfa_2': 'PDF/A-2 (عصري، غوره فشار)',
        'pdfa_3': 'PDF/A-3 (وروستۍ نسخه، ضمیمو ته اجازه ورکوي)',
        'pdfa_standards_explanation': '📖 د معیارونو تشریح:\n\n'
            '• PDF/A-1: بنسټیز، د زړو سیسټمونو سره مطابقت لري (شاوخوا 2005)\n'
            '• PDF/A-2: ډیر عصري، غوره فشار، د څرګندتیا ملاتړ (شاوخوا 2011)\n'
            '• PDF/A-3: وروستۍ نسخه، د فایل ضمیمو ځای پرځای کولو ته اجازه ورکوي (شاوخوا 2013)\n\n'
            'سپارښتنه: PDF/A-2 د مطابقت او عصري ځانګړتیاو ترمنځ یو ښه جوړجاړی دی.',
        'pdfa_options': 'اختیارونه:',
        'pdfa_compress_enable': 'PDF فشار کړئ (کوچنی فایل)',
        'pdfa_metadata_preserve': 'میټاډاټا وساتئ (سرلیک، لیکوال، او داسې نور)',
        'pdfa_target_folder': 'هدف فولډر:',
        'pdfa_browse': 'لټون...',
        'pdfa_select_folder': 'هدف فولډر وټاکئ',
        'pdfa_ocr_info_unknown': '🔍 د متن مینځپانګه ونه لیدل شوه.',
        'pdfa_ocr_info_not_needed': '✅ متن شتون لري - OCR اړین نه دی.\nPDF/A مستقیم جوړ کیدی شي.',
        'pdfa_ocr_info_recommended': '⚠️ کافي متن ونه موندل شو.\n\nد لټون وړ PDF لپاره موږ سپارښتنه کوو چې لومړی OCR چل کړئ.\nیادونه: PDF/A پرته له OCR څخه کار کوي - مګر متن به د لټون وړ نه وي.',
        'pdfa_ocr_info_error': '❌ د چک کولو پرمهال تېروتنه: {0}',
        'pdfa_start': 'د PDF/A بدلون پیلېږي...',
        'pdfa_progress': 'د PDF/A بدلون روان دی...',
        'pdfa_success': 'د PDF/A بدلون بریالی شو!\n\nد دې په توګه خوندي شو:\n{0}\n\nآیا غواړئ نوی PDF پرانیزئ؟',
        'pdfa_complete': 'د PDF/A بدلون بشپړ شو',
        'pdfa_cancel': 'د PDF/A بدلون لغوه شو',
        'pdfa_error_format': 'د PDF/A بدلون پرمهال تېروتنه:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'د "ocrmypdf" کتابتون نصب شوی نه دی.\n\nمهرباني وکړئ د دې سره یې نصب کړئ:\npip install ocrmypdf',
        'btn_convert': 'بدلول',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF اصلاح کړئ (د فایل اندازه کمه کړئ)',
        'optimize_menu': 'PDF اصلاح کړئ (د فایل اندازه)',
        'optimize_info': 'د مختلفو اصلاح میتودونو له لارې د PDF فایل اندازه کموي.\n\nد فشار کچه هرڅومره لوړه وي، فایل هم هومره کوچنی کیږي - د انځورونو کې د کیفیت د احتمالي ضایع کیدو سره.',
        'optimize_level': 'د فشار کچه:',
        'optimize_level_low': 'ټیټ (چټک، لږ سپما)',
        'optimize_level_medium': 'منځنی (ښه جوړجاړی)',
        'optimize_level_high': 'لوړ (لویه سپما)',
        'optimize_level_maximum': 'اعظمي (اعظمي سپما، ورو)',
        'optimize_level_explanation': 'سپارښتنه: "منځنی" د سرعت او فایل اندازې ترمنځ یو ښه جوړجاړی دی.',
        'optimize_options': 'اختیارونه:',
        'optimize_compress_images': 'انځورونه فشار کړئ (د JPEG کیفیت کم کړئ)',
        'optimize_clean_objects': 'ناکاره شوي توکي لرې کړئ',
        'optimize_preserve_metadata': 'میټاډاټا وساتئ (سرلیک، لیکوال، او داسې نور)',
        'optimize_image_quality': 'د انځور کیفیت:',
        'optimize_range': 'د مخ سلسله:',
        'optimize_all_pages': 'ټول مخونه',
        'optimize_custom_range': 'دودیزه سلسله',
        'optimize_from': 'له:',
        'optimize_to': 'تر:',
        'optimize_target_folder': 'هدف فولډر:',
        'optimize_browse': 'لټون...',
        'optimize_select_folder': 'هدف فولډر وټاکئ',
        'optimize_info_box': 'مالومات',
        'optimize_info_text': 'اصلاح کول ممکن د لویو PDF لپاره څو دقیقې وخت ونیسي.\n\nانځورونه د کم کیفیت سره خوندي کیږي، کوم چې د فایل اندازه د پام وړ کمولی شي.',
        'optimize_start': 'د PDF اصلاح پیلېږي...',
        'optimize_progress': 'PDF اصلاح کیږي...',
        'optimize_cancel': 'د PDF اصلاح لغوه شوه',
        'optimize_complete': 'د PDF اصلاح بشپړه شوه',
        'optimize_error_format': 'د PDF اصلاح پرمهال تېروتنه:\n\n{0}',
        'optimize_success_message': 'د PDF اصلاح بریالۍ شوه!\n\nد دې په توګه خوندي شو:\n{0}\n\nمخکې: {1}\nوروسته: {2}\nسپما: {3:.1f}%\n\n{4}\n\nآیا غواړئ اصلاح شوی PDF پرانیزئ؟',
        'optimize_success_message_no_size': 'د PDF اصلاح بریالۍ شوه!\n\nد دې په توګه خوندي شو:\n{0}\n\nد اندازې مالومات شتون نلري.\n\nآیا غواړئ اصلاح شوی PDF پرانیزئ؟',
        'optimize_result_positive': 'فایل د {0:.1f}% لخوا کم شو.',
        'optimize_result_zero': 'د فایل اندازه کې بدلون نه دی راغلی.',
        'optimize_result_negative': 'فایل د {0:.1f}% لخوا زیات شوی.\nاصلاح پرېښودل شوه، اصلي فایل وساتل شو.',
        'btn_optimize': 'اصلاح پیل کړئ',
        'filename_optimize_low_suffix': '_اصلاح_شوی_ټیټ',
        'filename_optimize_medium_suffix': '_اصلاح_شوی',
        'filename_optimize_high_suffix': '_اصلاح_شوی_لوړ',
        'filename_optimize_maximum_suffix': '_اصلاح_شوی_اعظمي',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF پرې کړئ',
        'crop_menu': 'PDF پرې کړئ (Crop)',
        'crop_range': 'په دې باندې پلي کړئ:',
        'crop_all_pages': 'ټول مخونه',
        'crop_current_page': 'یوازې اوسنی مخ',
        'crop_values': 'د پرې کولو ارزښتونه (په پوائنټونو کې):',
        'crop_left': 'کیڼ:',
        'crop_right': 'ښي:',
        'crop_top': 'پورته:',
        'crop_bottom': 'لاندې:',
        'crop_presets': 'مخکې تنظیم شوي:',
        'crop_preset_white': 'سپینې څنډې وپېژنئ',
        'crop_reset': 'بیا تنظیم کړئ',
        'crop_mouse_hint': '🖱️ سیمه نږدې انتخابولو لپاره مستطیل کش کړئ.\nبیا تاسو کولی شئ په SpinBoxes کې ارزښتونه په سمه توګه تنظیم کړئ.\nد ماوس سره لاسي تنظیم ممکن نه دی.',
        'crop_apply': 'پرې کړئ',
        'crop_scope_all': 'ټول مخونه',
        'crop_scope_current': 'اوسنی مخ',
        'crop_new_size': 'نوې اندازه: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'هیڅ PDF نه دی بار شوی',
        'crop_preview_error': 'د مخکتنې په بارولو کې تېروتنه',
        'crop_start': 'پرې کول پیلېږي...',
        'crop_progress': 'PDF پرې کیږي...',
        'crop_success': 'PDF په بریالیتوب سره پرې شو!\n\nد دې په توګه خوندي شو:\n{0}\n\nآیا غواړئ پرې شوی PDF پرانیزئ؟',
        'crop_complete': 'پرې کول بشپړ شول',
        'crop_cancel': 'پرې کول لغوه شول',
        'crop_error_format': 'د پرې کولو پرمهال تېروتنه:\n\n{0}',
        'filename_crop_suffix': '_پرې_شوی',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF مسطح کړئ (Flatten)',
        'flatten_menu': 'PDF مسطح کړئ (Flatten)',
        'flatten_info': 'PDF مسطح کول ټول د تدوین وړ عناصر د مخ مینځپانګې ته "پخوي".\n\nوروسته له دې، د فورمې ساحې، یادښتونه، متنونه، صلیبونه، لاسلیکونه، انځورونه او بڼې نور په جلا توګه د تدوین وړ نه دي.',
        'flatten_explanation_title': '📖 دا د څه لپاره ښه دی؟',
        'flatten_explanation_text': 'مسطح کول په لاندې حالتونو کې اړین دی:\n\n'
            '• 📄 تاسو غواړئ سند د چاپ لپاره چمتو کړئ\n'
            '• 🔒 تاسو غواړئ چې یو څوک د فورمې ساحې بدلې کړي مخنیوی وکړئ\n'
            '• 📎 تاسو غواړئ یادښتونه او تبصرې په سند کې "پایښت" ځای پرځای کړئ\n'
            '• 🖼️ تاسو غواړئ داخل شوي متنونه، صلیبونه، لاسلیکونه، انځورونه او بڼې په سند کې په پایښت سره ونښلوئ\n'
            '• 📦 تاسو غواړئ فایل د آرشیف لپاره چمتو کړئ\n\n'
            'مسطح کول PDF کوچنی کوي او د عناصرو د ناڅاپي حرکت یا ړنګیدو مخه نیسي.',
        'flatten_what_title': 'څه مسطح کیږي؟',
        'flatten_what_list': '• ✅ د فورمې ساحې (د متن ساحې، چیک بکسونه، تڼۍ)\n'
            '• ✅ یادښتونه (تبصرې، روښانه کول، یادښتونه)\n'
            '• ✅ پوښۍ (متنونه، صلیبونه، لاسلیکونه، انځورونه، بڼې)',
        'flatten_options': 'اختیارونه:',
        'flatten_forms': 'د فورمې ساحې مسطح کړئ',
        'flatten_annotations': 'یادښتونه مسطح کړئ',
        'flatten_overlays': 'پوښۍ مسطح کړئ (متنونه، صلیبونه، لاسلیکونه، انځورونه، بڼې)',
        'flatten_target_folder': 'هدف فولډر:',
        'flatten_browse': 'لټون...',
        'flatten_select_folder': 'هدف فولډر وټاکئ',
        'flatten_warning': '⚠️ مهم: مسطح کول یو نه بدلیدونکی پروسه ده!\n\nد مسطح کولو وروسته، د تدوین وړ عناصر نور په جلا توګه بدلیدلی یا ړنګیدلی نشي.\nکه اړتیا وي مخکې له مخه بیک اپ جوړ کړئ.',
        'flatten_apply': 'مسطح کړئ',
        'flatten_start': 'مسطح کول پیلېږي...',
        'flatten_progress': 'PDF مسطح کیږي...',
        'flatten_success': 'PDF په بریالیتوب سره مسطح شو!\n\nد دې په توګه خوندي شو:\n{0}\n\nآیا غواړئ مسطح شوی PDF پرانیزئ؟',
        'flatten_complete': 'مسطح کول بشپړ شول',
        'flatten_cancel': 'مسطح کول لغوه شول',
        'flatten_error_format': 'د مسطح کولو پرمهال تېروتنه:\n\n{0}',
        'filename_flatten_suffix': '_مسطح_شوی',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF پوښۍ (Overlay)',
        'overlay_menu': 'PDF پوښۍ (Overlay)',
        'overlay_info': 'یو PDF (پوښۍ) د بل PDF په پورته کېږدي.\n\nپوښۍ PDF د بنسټ PDF په پورته کېږدي. دا د اوبو نښې، لوګو، لیک سرلیک یا مهر لپاره ګټور دی.',
        'overlay_explanation_title': '📖 دا د څه لپاره ښه دی؟',
        'overlay_explanation_text': 'پوښۍ په لاندې حالتونو کې اړین دی:\n\n'
            '• 🏢 د شرکت لوګو د اوبو د نښې په توګه په هر مخ کېږدئ\n'
            '• 📄 په خالي PDF باندې لیک سرلیک کېږدئ\n'
            '• 🖊️ په سند باندې د مهر پوښۍ کېږدئ\n'
            '• 🔖 په ټولو مخونو باندې د اوبو نښه کېږدئ\n'
            '• 📑 په ټیمپلیټ باندې د فورمې پوښۍ کېږدئ',
        'overlay_type': 'د پوښۍ ډول:',
        'overlay_type_fullpage': 'بشپړ مخ (پوښونکی)',
        'overlay_type_transparent': 'بشپړ مخ (څرګند - سپارښتنه شوی)',
        'overlay_type_stamp': 'مهر (د موقعیت وړ)',
        'overlay_type_info_fullpage': '📄 پوښۍ PDF په سمه توګه په بشپړ مخ باندې کېږدي.\nسپینه شالید لرې کیدلی شي ترڅو یوازې مینځپانګه ښکاره شي.',
        'overlay_type_info_transparent': '🔍 پوښۍ PDF د څرګند شالید سره په بشپړ مخ باندې کېږدي.\nسپینه شالید په اتوماتيک ډول لرې کیږي - د اوبو نښې او لوګو لپاره غوره!',
        'overlay_type_info_stamp': '🖊️ پوښۍ PDF د مهر په توګه موقعیت او اندازه کوي.\nپه ځانګړو موقعیتونو کې د لوګو، مهر یا لاسلیک لپاره غوره.',
        'overlay_remove_background': 'سپینه شالید لرې کړئ:',
        'overlay_remove_background_enable': 'د پوښۍ PDF څخه سپینه شالید لرې کړئ (پوښۍ څرګندوي)',
        'overlay_remove_background_tooltip': 'د پوښۍ PDF څخه سپینې سیمې لرې کوي ترڅو لاندې متن ښکاره شي.',
        'overlay_threshold': 'حد ارزښت:',
        'overlay_threshold_hint': '(1-254، لوړ = ډیر سپین لرې کیږي)',
        'overlay_select_file': 'د پوښۍ PDF وټاکئ:',
        'overlay_file_placeholder': 'مهرباني وکړئ د پوښۍ لپاره PDF فایل وټاکئ',
        'overlay_browse': 'لټون...',
        'overlay_select_overlay': 'د پوښۍ PDF وټاکئ',
        'overlay_range': 'د مخ سلسله:',
        'overlay_all_pages': 'ټول مخونه',
        'overlay_custom_range': 'دودیزه سلسله',
        'overlay_from': 'له:',
        'overlay_to': 'تر:',
        'overlay_position': 'موقعیت:',
        'overlay_position_center': 'منځ',
        'overlay_position_top_left': 'پورته کیڼ',
        'overlay_position_top_right': 'پورته ښي',
        'overlay_position_bottom_left': 'لاندې کیڼ',
        'overlay_position_bottom_right': 'لاندې ښي',
        'overlay_size': 'اندازه:',
        'overlay_size_original': 'اصلي اندازه',
        'overlay_size_fit_page': 'مخ ته سمون ورکړئ',
        'overlay_size_custom': 'دودیز (%)',
        'overlay_opacity': 'څرګندتیا:',
        'overlay_target_folder': 'هدف فولډر:',
        'overlay_browse_folder': 'لټون...',
        'overlay_select_folder': 'هدف فولډر وټاکئ',
        'overlay_warning': '⚠️ یادونه: پوښۍ PDF د بنسټ PDF په پورته کېږدي او په کې "پخيږي".\n\nد پوښۍ PDF عناصر د خوندي کولو وروسته نور په جلا توګه د تدوین وړ نه دي.',
        'overlay_apply': 'پوښۍ',
        'overlay_start': 'پوښۍ پیلېږي...',
        'overlay_progress': 'PDF پوښل کیږي...',
        'overlay_success': 'PDF په بریالیتوب سره پوښل شو!\n\nد دې په توګه خوندي شو:\n{0}\n\nآیا غواړئ پوښل شوی PDF پرانیزئ؟',
        'overlay_complete': 'پوښۍ بشپړه شوه',
        'overlay_cancel': 'پوښۍ لغوه شوه',
        'overlay_error_format': 'د پوښلو پرمهال تېروتنه:\n\n{0}',
        'overlay_no_file': 'هیڅ پوښۍ PDF نه دی ټاکل شوی.\n\nمهرباني وکړئ د پوښلو لپاره PDF فایل وټاکئ.',
        'filename_overlay_suffix': '_پوښل_شوی',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'د PDF څخه انځورونه راوباسئ',
        'extract_images_menu': 'ټول انځورونه راوباسئ',
        'extract_images_info': 'د PDF څخه ټول انځورونه راوباسي او دوی د جلا فایلونو په توګه خوندي کوي.\n\nانځورونه په خپل اصلي بڼه خوندي کیږي یا ټاکل شوې بڼې ته بدلیږي.',
        'extract_images_format': 'د انځور بڼه:',
        'extract_images_quality': 'د JPEG کیفیت:',
        'extract_images_options': 'اختیارونه:',
        'extract_images_subfolder': 'فرعي فولډر ته راوباسئ ("PDFنوم_انځورونه")',
        'extract_images_unique': 'یوازې بې سارې انځورونه (تکرار څخه ډډه وکړئ)',
        'extract_images_range': 'د مخ سلسله:',
        'extract_images_all_pages': 'ټول مخونه',
        'extract_images_custom_range': 'دودیزه سلسله',
        'extract_images_from': 'له:',
        'extract_images_to': 'تر:',
        'extract_images_target_folder': 'هدف فولډر:',
        'extract_images_browse': 'لټون...',
        'extract_images_select_folder': 'هدف فولډر وټاکئ',
        'extract_images_info_box': 'مالومات',
        'extract_images_info_text': 'راباسل ممکن د لویو PDF لپاره څو دقیقې وخت ونیسي.\n\nانځورونه د خپل اصلي نوم سره خوندي کیږي (مخ_انځور).',
        'extract_images_extract': 'راباسئ',
        'extract_images_start': 'راباسل پیلېږي...',
        'extract_images_progress': 'انځورونه راوباسل کیږي...',
        'extract_images_success': '✅ انځورونه په بریالیتوب سره راووتل!\n\n{0} انځورونه په دې کې خوندي شول:\n{1}',
        'extract_images_complete': 'د انځورونو راباسل بشپړ شو',
        'extract_images_cancel': 'راباسل لغوه شو',
        'extract_images_error_format': 'د انځورونو په راباسلو کې تېروتنه:\n\n{0}',
        'extract_images_open_folder': '📁 فولډر پرانیزئ',
        'extract_images_no_images': 'په PDF کې هیڅ انځور ونه موندل شو.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'په یو مخ کې څو مخونه (N-Up)',
        'nup_menu': 'په یو مخ کې څو مخونه (N-Up)',
        'nup_info': 'ډیری PDF مخونه په یو مخ کې ترتیبوي.\n\nد کمپیکټ چاپونو، کتنو یا لاسوندونو لپاره غوره.',
        'nup_layout': 'ترتیب:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'مخکتنه:',
        'nup_preview_info': '{0} مخونه → {1} مخونه په هر پاڼه کې → {2} پاڼې\nترتیب: {3}',
        'nup_order': 'ترتیب:',
        'nup_order_horizontal': 'افقي (قطار په قطار)',
        'nup_order_vertical': 'عمودي (ستون په ستون)',
        'nup_order_horizontal_reverse': 'افقي معکوس',
        'nup_order_vertical_reverse': 'عمودي معکوس',
        'nup_range': 'د مخ سلسله:',
        'nup_all_pages': 'ټول مخونه',
        'nup_custom_range': 'دودیزه سلسله',
        'nup_from': 'له:',
        'nup_to': 'تر:',
        'nup_options': 'اختیارونه:',
        'nup_margins': 'څنډې:',
        'nup_margin_between': 'د مخونو ترمنځ واټن:',
        'nup_page_numbers': 'د مخ شمېرې داخل کړئ',
        'nup_target_folder': 'هدف فولډر:',
        'nup_browse': 'لټون...',
        'nup_select_folder': 'هدف فولډر وټاکئ',
        'nup_create': 'جوړ کړئ',
        'nup_start': 'N-Up پیلېږي...',
        'nup_progress': 'N-Up جوړیږي...',
        'nup_success': 'N-Up په بریالیتوب سره جوړ شو!\n\nد دې په توګه خوندي شو:\n{0}\n\nآیا غواړئ نوی PDF پرانیزئ؟',
        'nup_complete': 'N-Up بشپړ شو',
        'nup_cancel': 'N-Up لغوه شو',
        'nup_error_format': 'د N-Up پرمهال تېروتنه:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'د مخ اندازه بدل کړئ',
        'pagesize_menu': 'د مخ اندازه بدل کړئ',
        'pagesize_info': 'د PDF د مخ اندازه بدلوي.\n\nمینځپانګه په اتوماتيک ډول نوي اندازې سره سمون خوري.',
        'pagesize_format': 'بڼه:',
        'pagesize_select': 'یو معیاري بڼه وټاکئ:',
        'pagesize_custom': 'دودیزه اندازه:',
        'pagesize_width': 'پلنوالی:',
        'pagesize_height': 'لوړوالی:',
        'pagesize_orientation': 'لور:',
        'pagesize_portrait': 'عمودي',
        'pagesize_landscape': 'افقي',
        'pagesize_scale_options': 'د اندازه کولو اختیارونه:',
        'pagesize_fit': 'سمون ورکړئ (اړخ تناسب وساتئ)',
        'pagesize_stretch': 'غځول (تحریف)',
        'pagesize_center': 'منځ کې (اصلي اندازه)',
        'pagesize_range': 'د مخ سلسله:',
        'pagesize_all_pages': 'ټول مخونه',
        'pagesize_custom_range': 'دودیزه سلسله',
        'pagesize_from': 'له:',
        'pagesize_to': 'تر:',
        'pagesize_target_folder': 'هدف فولډر:',
        'pagesize_browse': 'لټون...',
        'pagesize_select_folder': 'هدف فولډر وټاکئ',
        'pagesize_apply': 'پلي کړئ',
        'pagesize_start': 'د مخ اندازه بدلول پیلېږي...',
        'pagesize_progress': 'د مخ اندازه بدلیږي...',
        'pagesize_success': 'د مخ اندازه په بریالیتوب سره بدله شوه!\n\nد دې په توګه خوندي شو:\n{0}\n\nآیا غواړئ نوی PDF پرانیزئ؟',
        'pagesize_complete': 'د مخ اندازه بدلول بشپړ شول',
        'pagesize_cancel': 'د مخ اندازه بدلول لغوه شول',
        'pagesize_error_format': 'د مخ اندازه بدلولو پرمهال تېروتنه:\n\n{0}',
        'pagesize_preview_info': 'نوې اندازه: {0} x {1} pt',
        'filename_pagesize_suffix': '_نوې_اندازه',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'د PDF مالومات',
        'pdf_info_menu': 'د PDF مالومات وښایئ',
        'pdf_info_voice': 'د PDF مالومات ښودل کیږي',
        'pdf_info_error': 'د PDF مالوماتو په ښودلو کې تېروتنه:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "د کیبورډ شارټ کټونه وښایئ",
        "shortcuts_dialog_title": "د کیبورډ شارټ کټونه",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 فایل</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF پرانیزئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF وتړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>د دې په توګه خوندي کړئ...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>سند خوندي کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>چاپ کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>سمدستي چاپ کړئ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>اپلیکیشن وتړئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 صادرول</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>د Pages په توګه صادر کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>د DOCX په توګه صادر کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>د TXT په توګه صادر کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>د انځورونو په توګه صادر کړئ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>انځورونه راوباسئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ د سند پروسس</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (څو مخونه)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A بدلون (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF مسطح کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF پوښۍ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF اصلاح کړئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ تدوین</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>لټون</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>نښه اضافه کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>نښې اداره کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>بله نښه</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>مخکینۍ نښه</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR چل کړئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 د مخ مدیریت</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>اوسنی مخ وګرځوئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>ټول مخونه وګرځوئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>اوسنی مخ نورمال کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>ټول مخونه نورمال کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>مخونه ړنګ کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>مخونه راوباسئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>مخونه داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>مخونه حرکت ورکړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDFs یوځای کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>د مخ اندازه بدل کړئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 داخلول</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>متن داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>صلیب داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>لاسلیک 1 داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>لاسلیک 2 داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>انځور داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>مستطیل داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>بیضوي داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>کرښه داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>تیر داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>د مخ شمېرې داخل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>د متن اوبو نښه</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>د انځور اوبو نښه</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ سور تېرونه</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>سور تېر (تور)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>سور تېر (سپین)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>ټول سور تېرونه پلي کړئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ پرمختللی</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF پرې کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>میټاډاټا تدوین کړئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ کتنه</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>تیاره/روښانه حالت بدل کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>د متن کړکۍ وښایئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>د مخ پلنوالی (زوم)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>دوه مخونه (زوم)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>کتنه (زوم)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ترتیبات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>د پاسورډ مدیریت</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>د OCR ترتیبات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>د لاسلیک ترتیبات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>د فایل نوم بڼه</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>ترتیبات صادر کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>ترتیبات وارد کړئ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ مالومات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>د PDF مالومات وښایئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>غږیز تولید فعال/غیر فعال کړئ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>د مینو بار باندې تمرکز وکړئ</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "نوی نسخه شتون لري",
        "update_available_message": "یو نوی نسخه <b>{0}</b> شتون لري.\n\nد تازه معلوماتو ډاونلوډ لپاره د خپرونې پاڼې څخه لیدنه وکړئ:\n{1}",
        "update_available_voice": "نوی نسخه {0} شتون لري. مهرباني وکړئ تازه معلومات د GitHub پاڼې څخه ډاونلوډ کړئ.",
        "update_open_release": "د خپرونې پاڼه پرانیزئ",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "ټول ژباړې ډاونلوډ کړئ",
        "ask_download_all_translations": """د جرمني، انګلیسي او ویتنامي سربېره، {total_languages} نورې GUI ژبې شتون لري.\n\nایا دوی باید چمتو / تازه شي؟\n\nیادونه:\nغیر ضروري ژبې تاسو وروسته په لارښود کې په لاسي ډول حذف کولی شئ:\n{translations_path}
        \nکه تاسو لغوه کړئ، تاسو کولی شئ GUI ژبې وروسته د 'وسیلې → ژباړې تازه کړئ' مینو له لارې ډاونلوډ کړئ.""",
        "menu_update_translations": "ژباړې تازه کړئ",
        "translations_updated": "ژباړې تازه شوې",
        "translations_update_success": "{} ژباړې په بریالیتوب سره تازه شوې ({} نوي، {} تازه شوي).",
        "translations_update_error": "د ژباړو په تازه کولو کې تېروتنه",
        "translations_update_no_changes": "ټولې ژباړې دمخه تازه دي.",
        "translations_update_offline": "د انټرنیټ اړیکه نشته. ژباړې نشي تازه کیدی.",
        "translations_update_in_progress": "ژباړې په شالید کې تازه کیږي...",
        "translations_downloading": "ژباړې ډاونلوډ کیږي...",
        "translations_path_hint": "د ژباړو لپاره د کارونکي لارښود",
        "translations_update_not_available_title": "تازه معلومات شتون نلري",
        "translations_update_not_available_message": """د ژباړو تازه کول یوازې په نصب شوي نسخه کې شتون لري.\n\nد پراختیا په حالت کې، ژباړې دمخه تازه دي.""",
        "translations_update_no_internet_title": "د انټرنیټ اړیکه نشته",
        "translations_update_no_internet_message": """د انټرنیټ اړیکه نشي ټینګولی.\n\nژباړې د GitHub څخه نشي ډاونلوډ کیدی.\n\nد حل لارې:
        • خپل انټرنیټ اړیکه وګورئ
        • کوم احتمالي فایروال لنډ مهال غیر فعال کړئ
        • وروسته بیا هڅه وکړئ
        \nتاسو کولی شئ ژباړې په لاسي ډول د GitHub څخه هم ډاونلوډ کړئ:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "تازه کول دمخه روان دي",
        "btn_retry": "بیا هڅه وکړئ",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "PDF Dark View ته ښه راغلاست",
        "welcome_title_not_supported": "PDF Dark View ته ښه راغلاست",
        "welcome_message": "PDF Dark View ته ښه راغلاست!\n\nستاسو د سیسټم ژبه د '{language}' په توګه وپیژندل شوه.\nآیا تاسو غواړئ دا ژبه د کاروونکي انٹرفیس لپاره وکاروئ?\n\nتاسو کولی شئ هر وخت د 'ترتیبات → ژبه' له لارې ژبه بدله کړئ.",
        "welcome_message_language_not_available": "PDF Dark View ته ښه راغلاست!\n\nستاسو د سیسټم ژبه د '{language}' په توګه وپیژندل شوه.\nدا ژبه لا نه ده نصب شوې.\n\nآیا تاسو غواړئ اوس د {language} لپاره ژباړې د GitHub څخه ډاونلوډ کړئ?\n\n(ژبه به بیا په اتوماتيک ډول د کاروونکي انٹرفیس لپاره وکارول شي.)",
        "welcome_message_language_not_supported": "PDF Dark View ته ښه راغلاست!\n\nستاسو د سیسټم ژبه د '{language}' په توګه وپیژندل شوه.\nله بده مرغه، د دې ژبې لپاره لا ژباړې نشته.\n\nد کاروونکي انٹرفیس به په {fallback_language} کې وښودل شي.\n\nتاسو کولی شئ هر وخت د 'ترتیبات → ژبه' له لارې ژبه بدله کړئ.\nکه تاسو وغواړئ، تاسو کولی شئ خپله د خپلې ژبې لپاره ژباړه کې مرسته وکړئ:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "هو، د سیسټم ژبه وکاروئ",
        "welcome_keep_english": "نه، انګلیسي وساتئ",
        "welcome_download_language": "هو، {language} ډاونلوډ کړئ",
        # ============================================
        # 107. ZULETZT VERWENDETE PFADE
        # ============================================

        'menu_recent': 'وروستي کارول شوي',
        'menu_recent_dirs': 'لارښودونه...',
        'menu_recent_files': 'فایلونه...',
        'recent_manage': 'مدیریت...',
        'recent_enable_tracking': 'وروستي لارې خوندي کړئ (محرمیت)',
        'recent_enable_info': 'د لارو نه خوندي کولو لپاره دا اختیار غیر فعال کړئ',
        'recent_tracking_disabled': 'د لارې تعقیب غیر فعال دی',
        'recent_enabled': 'فعال شوی',
        'recent_disabled': 'غیر فعال شوی',
        'recent_tracking_status': 'د لارې تعقیب {0}',
        'recent_dialog_title': 'وروستي کارول شوي لارې',
        'recent_tab_directories': 'لارښودونه',
        'recent_tab_files': 'فایلونه',
        'recent_dirs_instruction': 'د لارښود کې د فایل ډیالوګ پرانیستلو لپاره دوه ځله کلیک وکړئ',
        'recent_files_instruction': 'مستقیماً PDF پرانیستلو لپاره دوه ځله کلیک وکړئ',
        'recent_no_directories': '(هیچا لارښود خوندي شوی نه دی)',
        'recent_no_files': '(هیچا فایل خوندي شوی نه دی)',
        'recent_default_current': '⭐ تلوالی: {0}',
        'recent_set_as_default': '⭐ د تلوالي په توګه وټاکئ',
        'recent_default_set_title': 'تلوالی لارښود وټاکل شو',
        'recent_default_set_message': 'د "{0}" لارښود د PDF پرانیستلو لپاره د تلوالي په توګه وټاکل شو.',
        'recent_default_set_voice': 'تلوالی لارښود وټاکل شو',
        'recent_directory_not_found': 'لارښود ونه موندل شو',
        'recent_file_not_found': 'فایل ونه موندل شو',
        'recent_remove_selected': 'لرې کول',
        'recent_remove_title': 'لاره لرې کول',
        'recent_remove_confirm': 'ایا تاسو واقعیا غواړئ د "{0}" لاره له لیست څخه لرې کړئ؟',
        'recent_path_removed': 'لاره لرې شوه',
        'recent_clear_all': 'ټول لرې کول',
        'recent_clear_title': 'ټولې لارې لرې کول',
        'recent_clear_confirm_type': 'ایا تاسو واقعیا غواړئ ټول {0} ړنګ کړئ؟',
        'recent_cleared': 'لیست پاک شو',
        'recent_path_not_found_title': 'لاره ونه موندل شوه',
        'recent_path_not_found_message': 'د "{0}" لاره نور شتون نلري.',
        'recent_open_file': 'فایل پرانیستل',
        'btn_open_recent': 'پرانیستل',
        'recent_open_file_question': 'ایا تاسو غواړئ "{0}" د PDF په توګه پرانیزئ؟',
        'recent_not_pdf': 'ټاکل شوی فایل PDF نه دی.',
        'recent_more_entries': 'نورې داخلې...',
        'btn_remove': 'لرې کول',
        'btn_clear': 'ټول پاک کړئ',
        'recent_context_open': 'پرانیستل',
        'recent_context_reveal': 'په Finder کې ښودل',
        'recent_context_set_default': '⭐ د تلوالي په توګه وټاکئ',
        'recent_context_open_terminal': '💻 ټرمینل پرانیستل',
        'recent_context_file_info': 'د فایل معلومات',
        'recent_context_open_with_default': '📄 د تلوالي ایپ سره پرانیستل',
        'recent_context_remove': 'له لیست څخه لرې کول',
        'recent_context_clear_all': 'ټول لرې کول',
        'recent_file_info_title': 'د فایل معلومات',
        'recent_file_info_name': 'نوم',
        'recent_file_info_path': 'لاره',
        'recent_file_info_size': 'اندازه',
        'recent_file_info_modified': 'بدل شوی',
        'recent_file_info_pages': 'مخونه',
        'recent_error_reveal': 'په Finder کې د پرانیستلو تېروتنه',
        'recent_error_terminal': 'د ټرمینل پرانیستلو تېروتنه',
        'recent_error_info': 'د فایل معلوماتو ترلاسه کولو تېروتنه',
        'open_user_data_folder': 'د کارونکي ډاټا لارښود ښودل',

        # ============================================
        # 108. GERADE UNGERADE SEITEN LÖSCHEN
        # ============================================
        "pages_delete_even": "ټول جوړ مخونه ړنګ کړئ",
        "pages_delete_odd":  "ټول طاق مخونه ړنګ کړئ",
        "progress_even_pages": "جوړ مخونه ړنګیږي",
        "progress_odd_pages": "طاق مخونه ړنګیږي",
        "progress_mark_delete_even": "{} جوړ مخ(ونه) د ړنګولو لپاره نښه شوي",
        "progress_mark_delete_odd":  "{} طاق مخ(ونه) د ړنګولو لپاره نښه شوي",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "پروګرام بندیږي",

    }

