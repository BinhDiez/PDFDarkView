
# ============================================
# translations_ar.py - القاموس العربي
# Vollständig sortiert nach Kategorien
# ============================================

def load_arabic_strings():
    """Lädt alle arabischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF دارك فيو بواسطة BinhDiez",
        'app_name': "PDF دارك فيو",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "فتح PDF",
        'btn_text_window': "نص OCR",
        'btn_first': "الصفحة الأولى",
        'btn_prev': "الصفحة السابقة",
        'btn_next': "الصفحة التالية",
        'btn_last': "آخر صفحة",
        'btn_print': "طباعة",
        'btn_darkmode_light': "الوضع الفاتح",
        'btn_darkmode_dark': "الوضع الداكن",
        'btn_delete_pages': "حذف الصفحات",
        'btn_extract_pages': "استخراج الصفحات",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "موافق",
        'btn_cancel': "إلغاء",
        'btn_save': "حفظ",
        'btn_close': "إغلاق",
        'btn_delete': "حذف",
        'btn_delete_all': "حذف الكل",
        'btn_copy': "نسخ",
        'btn_export': "تصدير",
        'btn_show': "إظهار كلمة المرور",
        'btn_hide': "إخفاء كلمة المرور",
        'btn_authenticate': "توثيق",
        'btn_settings': "إعدادات",
        'btn_protect': "حماية",
        'btn_remove_password': "إزالة كلمة المرور",
        'btn_manage': "إدارة كلمات المرور",
        'btn_retry': "إعادة المحاولة",
        'btn_select_all': "تحديد الكل",
        'btn_clear_selection': "مسح التحديد",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "الصفحة {0} من {1}",
        'page_count': "من {0}",
        'goto_page': "اذهب إلى الصفحة",
        'page_simple': "الصفحة {0}",
        'full_view_page': "عرض كامل للصفحة {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "أدخل مصطلح البحث + Enter",
        'search_results': "النتائج: {0} من {1}",
        'search_nav_hint': "Enter: التالي (Shift+Enter: السابق)",
        'search_no_results': "لا توجد نتائج",
        'search_error': "خطأ في البحث",
        'search_active': "حقل البحث مفعل",
        'search_closed': "انتهى البحث",
        'search_position': "الصفحة {0} {1}",
        'search_pos_top': "في الأعلى",
        'search_pos_upper': "أعلى",
        'search_pos_middle': "الوسط",
        'search_pos_lower': "أسفل",
        'search_pos_bottom': "في الأسفل",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "تم التعرف على النص بنجاح!",
        'ocr_success_title': "OCR ناجح",
        'ocr_success_message': "المستند قابل للبحث الآن.",
        'ocr_failed': "فشل OCR",
        'ocr_in_progress': "OCR قيد التنفيذ",
        'ocr_preparing': "جارٍ تحضير PDF...",
        'ocr_analyzing': "جارٍ تحليل PDF...",
        'ocr_optimizing': "تحسين الصورة...",
        'ocr_recognizing': "التعرف على النص...",
        'ocr_embedding': "دمج النص...",
        'ocr_finalizing': "إنهاء PDF...",
        'ocr_not_available': "OCR غير متوفر",
        'ocr_install_message': "لم يتم العثور على أدوات OCR.\n\nالرجاء تثبيت:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR مطلوب",
        'ocr_question': "لا يحتوي PDF على نص قابل للبحث.\nهل تريد إجراء OCR لتمكين {0}؟",
        'ocr_perform': "إجراء OCR",
        'ocr_later': "لاحقاً",
        'ocr_starting': "بدء OCR مضمون...",
        'ocr_success_voice': "OCR ناجح. PDF قابل للبحث الآن.",
        'ocr_partial_success': "تم إجراء OCR، ولكن حدثت مشاكل في الاستبدال.\n\nتم حفظ النسخة القابلة للبحث في:\n{0}\n\nالخطأ: {1}",
        'ocr_partial_title': "OCR جزئي النجاح",
        'ocr_partial_voice': "تم OCR، لكن الاستبدال فشل.",
        'original_file': "الملف الأصلي:",
        'old_size': "الحجم القديم:    {0} بايت",
        'new_size': "الحجم الجديد: {0} بايت",
        'size_change': "التغيير: {0}{1} بايت",
        'backup_created_file': "تم إنشاء نسخة احتياطية:\n{0}",
        'backup_not_created': "لم يتم إنشاء نسخة احتياطية (الإعداد معطل)",
        'page_header': "=== الصفحة {0} ===\n{1}\n",
        'scanned_page_header': "=== الصفحة {0} (ممسوحة ضوئياً) ===\n[تحتوي هذه الصفحة على نص ممسوح فقط]\n[الرجاء إجراء OCR يدوياً]\n",
        'scanned_warning': "⚠️ نص ممسوح - OCR مطلوب",
        'guaranteed_title': "تم إنشاء PDF قابل للبحث",
        'guaranteed_message': "<b>تم إنشاء نسخة مضمونة قابلة للبحث!</b>\n\nنظرًا لفشل OCR التلقائي، تم إنشاء PDF بديل قابل للبحث:\n\n{0}\n\n<b>يحتوي هذا الملف على:</b>\n• نص مستخرج (إذا كان موجوداً)\n• إرشادات للصفحات الممسوحة\n• قابل للبحث بالكامل",
        'guaranteed_voice': "تم إنشاء PDF مضمون قابل للبحث.",
        'instruction_title': "إرشادات OCR",
        'instruction_file': "الملف الأصلي: {0}",
        'instruction_text': "فشل التعرف التلقائي على النص (OCR).\nالرجاء إجراء OCR يدوياً:\n\n1. باستخدام OCRmyPDF (سطر الأوامر):\n   ocrmypdf --force-ocr \"[الملف]\" \"النتيجة.pdf\"\n\n2. باستخدام أدوبي أكروبات (macOS/Windows):\n   • افتح PDF في Acrobat\n   • أدوات > تحرير PDF\n   • اختر 'التعرف على النص'\n\n3. باستخدام المعاينة (macOS):\n   • افتح PDF في المعاينة\n   • ملف > تصدير...\n   • فلتر Quartz: 'تقليل حجم الملف'\n   • فعّل 'إجراء OCR'\n\n4. خدمات OCR عبر الإنترنت:\n   • smallpdf.com/ar/ocr-pdf\n   • ilovepdf.com/ar/ocr-pdf\n   • adobe.com/ar/acrobat/online/pdf-to-word.html",
        'instruction_created': "تم إنشاء إرشادات OCR",
        'instruction_created_message': "تم إنشاء إرشادات مفصلة:\n\n{0}\n\nاتبع الخطوات لإجراء OCR يدوي.",
        'instruction_created_voice': "تم إنشاء إرشادات OCR.",
        'ocr_impossible': "OCR غير ممكن",
        'ocr_impossible_message': "تعذر إجراء OCR.\n\nيرجى معالجة '{0}' يدوياً باستخدام برنامج OCR.",
        'ocr_impossible_voice': "OCR غير ممكن. يرجى المعالجة يدوياً.",
        'emergency_title': "OCR طارئ",
        'emergency_message': "تم إنشاء PDF طارئ:\n\n{0}\n\nيرجى معالجة هذا الملف يدوياً باستخدام OCR.",
        'emergency_voice': "تم إنشاء PDF طارئ. يرجى إجراء OCR يدوياً.",
        'critical_error': "خطأ جسيم",
        'critical_error_message': "تعذر بدء OCR.\n\nيرجى إعادة تشغيل البرنامج والتحقق من تثبيت OCR.",
        'critical_error_voice': "خطأ جسيم في OCR",
        'ocr_question_html': "<p>لا يحتوي PDF على نص قابل للبحث.<p>هل تريد إجراء OCR لتمكين <b>{0}</b>؟</p>",
        'ocr_question_voice': "OCR مطلوب. لا يحتوي PDF على نص قابل للبحث. هل تريد إجراء OCR لتمكين {0}؟",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "لا يوجد PDF محمل",
        'no_pdf_message': "لم يتم تحميل أي PDF",
        'pdf_not_found': "لم يتم العثور على ملف PDF",
        'file_size': "حجم الملف",
        'bytes': "بايت",
        'kb': "ك.ب",
        'mb': "م.ب",
        'backup_created': "تم إنشاء نسخة احتياطية",
        'backup_disabled': "النسخ الاحتياطي معطل",
        'backup_activated': "تم تفعيل إنشاء النسخ الاحتياطية",
        'backup_deactivated': "تم تعطيل إنشاء النسخ الاحتياطية",
        'backup_status': "النسخ الاحتياطي: {0}",
        'backup_on': "✔ مفعل",
        'backup_off': "✘ معطل",
        'close_pdf': "إغلاق PDF: {0}",
        'pdf_not_found_format': "لم يتم العثور على ملف PDF: {0}",
        'error_pdf_load_format': "خطأ في تحميل PDF: {0}",
        'load_failed_format': "فشل التحميل:\n{0}",
        'decrypted_suffix': "(مفكوك التشفير)",
        'decryption_failed': "فشل فك التشفير.",
        'decryption_error': "خطأ في فك التشفير",
        'decryption_success': "تم فك التشفير بنجاح",
        'decryption_success_message': "تم فك تشفير PDF وحفظه في:\n\n{0}",
        'decryption_success_voice': "تم فك تشفير PDF وحفظه.",
        'password_remove_error': "خطأ في إزالة كلمة المرور",
        'save_unencrypted': "حفظ PDF غير مشفر باسم",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "حفظ باسم...",
        'save_copy': "حفظ نسخة",
        'save_success': "تم حفظ PDF في: {0}",
        'save_encrypted': "تم حفظ PDF المحمي في: {0}",
        'save_error': "تعذر حفظ PDF",
        'encryption_question': "هل تريد حماية PDF بكلمة مرور؟",
        'encryption_yes': "نعم",
        'encryption_no': "لا",
        'encryption_cancel': "إلغاء",
        'save_cancel': "تم إلغاء الحفظ",
        'save_encrypted_voice': "تم تشفير الملف وحفظه.",
        'save_success_voice': "تم حفظ ملف PDF بدون تشفير.",
        'save_error_format': "تعذر حفظ PDF:\n{0}",
        'export_pages_success': "تم التصدير إلى Pages بنجاح",
        'export_pages_error': "فشل التصدير إلى Pages",
        'export_pages_error_format': "فشل التصدير إلى Pages: {0}",
        'export_word_success': "تم التصدير إلى Word بنجاح",
        'export_word_error': "فشل التصدير إلى Word",
        'export_word_error_format': "فشل التصدير إلى Word: {0}",
        'export_text_success': "تم تصدير النص بنجاح",
        'export_text_error': "فشل تصدير النص",
        'export_text_error_format': "فشل تصدير النص: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "كلمة المرور مطلوبة",
        'password_enter': "الرجاء إدخال كلمة المرور",
        'password_confirm': "تأكيد كلمة المرور",
        'password_new': "كلمة مرور جديدة",
        'password_current': "كلمة المرور الحالية",
        'password_save': "حفظ كلمة المرور (مشفرة)",
        'password_saved': "✓ تم حفظ كلمة المرور لهذا الملف",
        'password_wrong': "كلمة مرور خاطئة",
        'password_mismatch': "كلمتا المرور غير متطابقتين",
        'password_too_short': "كلمة المرور قصيرة جداً",
        'password_min_length': "يجب أن تتكون كلمة المرور من 4 أحرف على الأقل",
        'password_strength': "قوة كلمة المرور",
        'password_strength_very_weak': "ضعيفة جداً",
        'password_strength_weak': "ضعيفة",
        'password_strength_medium': "متوسطة",
        'password_strength_strong': "قوية",
        'password_strength_very_strong': "قوية جداً",
        'password_char_count': "({0} حرف)",
        'password_match': "✓ متطابقة",
        'password_no_match': "✗ كلمتا المرور غير متطابقتين",
        'password_show': "إظهار",
        'password_hide': "إخفاء",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "إدارة كلمات المرور",
        'password_table_filename': "اسم الملف",
        'password_table_password': "كلمة المرور",
        'password_count': "{0} كلمات مرور محفوظة",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "لا توجد كلمات مرور محفوظة",
        'password_copied': "تم نسخ {0} كلمات مرور",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "هل أنت متأكد من حذف كلمة المرور لـ '{0}'؟",
        'password_delete_multiple': "هل أنت متأكد من حذف {0} كلمات المرور المحددة؟",
        'password_delete_all_confirm': "هل أنت متأكد من حذف جميع كلمات المرور الـ {0} المحفوظة؟",
        'password_deleted': "تم حذف {0} كلمات مرور",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "تم حذف جميع كلمات المرور",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "مولد كلمات المرور",
        'generator_generated': "كلمة المرور المُنشأة:",
        'generator_regenerate': "إعادة الإنشاء",
        'generator_copy': "نسخ",
        'generator_use': "استخدام",
        'generator_settings': "الإعدادات",
        'generator_length': "الطول:",
        'generator_group_every': "فاصل كل",
        'generator_group_chars': "حرف.    الفاصل:",
        'generator_uppercase': "أحرف كبيرة (A-Z)",
        'generator_lowercase': "أحرف صغيرة (a-z)",
        'generator_digits': "أرقام (0-9)",
        'generator_symbols': "رموز (!@#$%^&*)",
        'generator_exclude': "المستثناة:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "كلمة المرور الرئيسية مطلوبة",
        'master_password_setup': "إعداد كلمة المرور الرئيسية",
        'master_password_change': "تغيير كلمة المرور الرئيسية",
        'master_password_enter': "الرجاء إدخال كلمة المرور الرئيسية",
        'master_password_choose': "اختر كلمة مرور رئيسية قوية (8 أحرف على الأقل)",
        'master_password_new': "الرجاء إدخال كلمة المرور الرئيسية الجديدة",
        'master_password_confirm': "تأكيد كلمة المرور",
        'master_password_authenticate': "توثيق",
        'master_password_success': "تم إعداد كلمة المرور الرئيسية بنجاح.",
        'master_password_changed': "تم تغيير كلمة المرور الرئيسية بنجاح.",
        'master_password_removed': "تم حذف كلمة المرور الرئيسية وجميع كلمات المرور.",
        'master_password_remove': "إزالة كلمة المرور الرئيسية",
        'master_password_remove_confirm': "هل أنت متأكد تماماً من حذف جميع كلمات المرور؟\n\nهذا الإجراء لا يمكن التراجع عنه!",
        'master_password_export_before': "هل ترغب في تصدير نسخة احتياطية أولاً؟",
        'master_password_export_delete': "تصدير وحذف",
        'master_password_delete_now': "حذف الآن",
        'master_password_for_signatures': "لاستخدام التوقيعات، يجب إعداد كلمة مرور رئيسية.\n\nهل ترغب في إعداد كلمة مرور رئيسية الآن؟",
        'master_password_for_private': "لاستخدام كتل النص الخاصة، يجب إعداد كلمة مرور رئيسية.\n\nهل ترغب في إعداد كلمة مرور رئيسية الآن؟",
        'master_password_info': """
            <b>🔐 بدون كلمة مرور رئيسية:</b><br>
            • لا يمكن عرض أو نسخ أو تصدير كلمات المرور<br>
            • يمكن دائماً حذف كلمات المرور (حتى بدون كلمة مرور رئيسية)<br><br>

            <b>🔐 مع كلمة مرور رئيسية:</b><br>
            • جميع الوظائف متاحة بعد التوثيق<br>
            • يتم تشفير كلمات المرور بكلمة المرور الرئيسية<br>
            • الحد الأدنى للطول: 8 أحرف<br>
            • تخزين آمن لهاش SHA-256<br><br>

            <b>مهم:</b><br>
            • في حال فقدان كلمة المرور الرئيسية، لا يمكن استعادة كلمات المرور<br>
            • عند إزالة كلمة المرور الرئيسية، يتم حذف جميع كلمات المرور<br>
            • خيار التصدير متاح قبل الحذف<br>
            • يمكن تغيير كلمة المرور الرئيسية في أي وقت
        """,
        'signature_auth_disabled': "تعطيل طلب كلمة المرور للتوقيعات",
        'template_auth_disabled': "تعطيل طلب كلمة المرور لكتل النص الخاصة",
        'master_password_for_signatures_settings': "لاستخدام التوقيعات، يجب إعداد كلمة مرور رئيسية.\n\nانتقل إلى الإعدادات - إدارة كلمات المرور",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "حماية PDF",
        'protect_info': "سيتم حماية الملف '{0}' بكلمة مرور.",
        'protect_instruction': "الرجاء إدخال كلمة المرور المطلوبة مرتين لحماية المستند، أو استخدم مولد كلمات المرور على يمين حقل الإدخال.",
        'protect_success': "تم حماية PDF بنجاح وحفظه في:\n{0}\n\nكلمة المرور: {1}\n\nهل ترغب في فتح PDF المحمي الآن؟",
        'protect_open': "نعم",
        'protect_skip': "لا",
        'protect_error': "خطأ في حماية PDF",
        'protect_open_title': "فتح PDF المحمي",
        'protect_question': "تم. هل ترغب في فتح PDF المحمي الآن؟ نعم أم لا؟",
        'password_cancel': "تم إلغاء حوار كلمة المرور",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "حذف الصفحات",
        'pages_extract': "استخراج الصفحات",
        'pages_insert': "إدراج صفحات",
        'pages_move': "نقل الصفحات",
        'pages_delete_options': "خيارات الحذف",
        'pages_delete_empty': "حذف جميع الصفحات الفارغة",
        'pages_delete_current': "حذف الصفحة الحالية",
        'pages_delete_range': "حذف نطاق من الصفحات",
        'pages_extract_options': "خيارات الاستخراج",
        'pages_extract_current': "استخراج الصفحة الحالية",
        'pages_extract_range': "استخراج نطاق من الصفحات",
        'pages_insert_position': "موضع الإدراج",
        'pages_insert_before': "إدراج قبل الصفحة:",
        'pages_insert_select': "اختر PDF",
        'pages_insert_none': "لم يتم اختيار PDF",
        'pages_move_source': "الصفحات المراد نقلها",
        'pages_move_from': "من صفحة:",
        'pages_move_to': "إلى صفحة:",
        'pages_move_target': "الموضع المستهدف",
        'pages_move_before': "نقل قبل الصفحة:",
        'pages_move_hint': "ملاحظة: الصفحة 1 = البداية، {0} = النهاية",
        'pages_range_invalid': "يجب أن تكون صفحة البداية أصغر أو تساوي صفحة النهاية.",
        'pages_position_invalid': "لا يمكن أن يكون الموضع المستهدف داخل النطاق المنقول.",
        'pages_no_pdf_selected': "لم يتم اختيار أي PDF.",
        'pages_deleted': "تم حذف {0} صفحات.",
        'pages_extracted': "المستخرج: {0}\nتم الحفظ في: {1}\nحجم الملف: {2:.1f} ك.ب",
        'pages_inserted': "تم إدراج {0} صفحات",
        'pages_moved': "تم نقل {0} صفحات.",
        'pages_deleted_none': "لم يتم حذف أي صفحات.",
        'pages_delete_progress': "جاري حذف الصفحات...",
        'pages_deleted_with_backup': "تم حذف {0} صفحات.\n\nالنسخة الاحتياطية: {1}",
        'pages_deleted_voice': "تم إنشاء نسخة احتياطية وحذف {0} صفحات.",
        'info': "معلومات",
        'error_dialog_creation': "تعذر إنشاء الحوار",
        'extract_page_single': "استخراج الصفحة {0}",
        'extract_page_range': "استخراج الصفحات {0}-{1}",
        'extract_success_voice': "تم استخراج الصفحات بنجاح",
        'extract_error_format': "خطأ في الاستخراج: {0}",
        'pages_inserted_voice': "تم إدراج {0} صفحات.",
        'insert_error_format': "خطأ في الإدراج: {0}",
        'pages_move_progress': "جاري نقل الصفحات...",
        'pages_moved_with_backup': "تم نقل {0} صفحات.\n\nالنسخة الاحتياطية: {1}",
        'move_success_title': "تم النقل بنجاح",
        'pages_moved_voice': "تم نقل {0} صفحات بنجاح",
        'mark_removed': "تمت إزالة علامة الصفحة {0}",
        'mark_empty': "تم وضع علامة على الصفحة {0} كفارغة",
        'mark_export_removed': "تمت إزالة علامة تصدير الصفحة {0}",
        'mark_export': "تم وضع علامة على الصفحة {0} للتصدير",
        'no_empty_pages': "لا توجد صفحات فارغة محددة للحذف",
        'delete_empty_confirm': "هل تريد حذف جميع الصفحات الفارغة المحددة ({0})؟",
        'delete_empty_confirm_voice': "هل تريد حذف جميع الصفحات الفارغة المحددة ({0}) الآن؟ نعم أم لا.",
        'empty_pages_deleted': "تم حذف {0} صفحات فارغة",
        'no_export_pages': "لا توجد صفحات محددة للتصدير",
        'overwrite_title': "استبدال الملف الموجود",
        'overwrite_question': "الملف\n\n{0}\n\nموجود بالفعل.\nهل تريد استبداله؟",
        'overwrite_voice': "استبدال الملف الموجود؟ نعم أم لا.",
        'page_skipped': "تم تخطي الصفحة {0}",
        'export_complete': "اكتمل التصدير.",
        'export_complete_voice': "اكتمل التصدير.",
        'no_pages_exported': "لم يتم تصدير أي صفحات",
        'export_cancelled': "تم إلغاء التصدير",
        'pages_exported': "تم تصدير {0} صفحات إلى {1}",
        'export_page_title': "تصدير صفحة",
        'page_exported': "تم تصدير الصفحة {0} إلى {1}",
        'export_error': "خطأ في التصدير",
        'export_marked_title': "تصدير الصفحات المحددة",
        'rotate_all_title': "تدوير جميع الصفحات",
        'rotate_all_question': "هل تريد تدوير جميع الصفحات 90 درجة لليمين؟",
        'rotate_all_voice': "هل تريد تدوير جميع الصفحات 90 درجة لليمين؟ نعم أم لا؟",
        'all_pages_rotated': "تم تدوير جميع الصفحات",
        'page_rotated': "تم تدوير الصفحة {0}",
        'rotate_error': "تعذر تدوير الصفحة",
        'delete_page_confirm': "هل تريد حذف الصفحة {0}؟",
        'delete_page_confirm_voice': "هل أنت متأكد من حذف الصفحة {0}؟ نعم أم لا.",
        'page_deleted': "تم حذف الصفحة {0}",
        'delete_error': "تعذر حذف الصفحة",
        'pages_deleted_voice': "تم حذف {0} صفحات",
        'pages_exported_split': "تم تصدير {0} صفحات بنجاح.",
        'pages_skipped': "تم تخطي {0} صفحات.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "استخراج الصفحات (متقدم)",
        'pdf_splitter_title': "مقسم ومستخرج PDF",
        'pdf_splitter_load': " اختيار ملف PDF",
        'pdf_splitter_info': "الرجاء اختيار خيار لمستند PDF الخاص بك",
        'pdf_splitter_basic': "العمليات الأساسية",
        'pdf_splitter_single': "تقسيم إلى صفحات فردية",
        'pdf_splitter_range': "استخراج الصفحات:",
        'pdf_splitter_range_placeholder': "مثال: 1-3,5,7-9",
        'pdf_splitter_clean': "عمليات التنظيف",
        'pdf_splitter_remove_empty': "إزالة جميع الصفحات الفارغة",
        'pdf_splitter_remove': "حذف نطاق الصفحات:",
        'pdf_splitter_remove_placeholder': "مثال: 2,4-6",
        'pdf_splitter_process': "معالجة PDF",
        'pdf_splitter_loaded': "تم تحميل PDF. الرجاء اختيار خيار",
        'pdf_read_error': "تعذر قراءة PDF",
        'pages': "الصفحات",
        'pages_created': "تم إنشاء الصفحات",
        'range_empty': "الرجاء إدخال نطاق من الصفحات",
        'range_invalid': "نطاق صفحات غير صالح",
        'range_created': "تم إنشاء PDF جديد بالصفحات المحددة:\n{0}",
        'empty_removed': "تمت إزالة {0} صفحات فارغة.\nالإخراج: {1}",
        'remove_empty': "الرجاء إدخال الصفحات المراد إزالتها",
        'remove_invalid': "صفحات غير صالحة للإزالة",
        'remove_done': "تم إنشاء PDF منقى:\n{0}",
        'open_folder': "فتح المجلد",
        'show_in_finder': "إظهار في Finder",
        'pdf_splitter_no_pdf': "الرجاء تحميل ملف PDF أولاً.",
        'process_error': "خطأ في معالجة PDF",
        'pages_created_voice': "تم إنشاء {0} صفحات",
        'range_created_voice': "تم إنشاء PDF بالصفحات المحددة",
        'empty_removed_voice': "تمت إزالة {0} صفحات فارغة",
        'remove_done_voice': "تم إنشاء PDF منقى",
        'pdf_splitter_split_groups': "كل مجموعة متصلة في ملف منفصل",
        'range_created_single': "تم إنشاء PDF جديد:\n{0}",
        'range_created_multiple': "تم إنشاء {0} ملفات PDF.",
        'range_created_voice_single': "تم إنشاء PDF واحد بالصفحات المحددة",
        'range_created_voice_multiple': "تم إنشاء {0} ملفات PDF",
        'empty_removed_none_left': "لا توجد صفحات متبقية",
        'empty_removed_all_empty': "تم التعرف على جميع الصفحات كفارغة وسيتم إزالتها. لم يتم إنشاء أي ملف.",
        'preview_single': "معاينة: {0}",
        'preview_enter_range': "الرجاء إدخال نطاق من الصفحات.",
        'preview_invalid_range': "نطاق صفحات غير صالح.",
        'preview_file': "معاينة: {0}",
        'preview_files': "معاينة: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "بدء الطباعة",
        'print_sent': "تم إرسال مهمة الطباعة",
        'print_now': "طباعة فورية",
        'print_error': "خطأ في الطباعة الفورية",
        'print_limited': "وظيفة الطباعة مقيدة على هذا النظام",
        'print_error_format': "خطأ في الطباعة الفورية: {0}",
        'warning': "تحذير",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "التبديل إلى الوضع الفاتح",
        'mode_switch_to_dark': "التبديل إلى الوضع الداكن",
        'mode_dark_activated': "تم تفعيل الوضع الداكن",
        'mode_light_activated': "تم تفعيل الوضع الفاتح",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "عرض كامل",
        'zoom_two_pages': "صفحتان جنباً إلى جنب",
        'zoom_overview': "وضع نظرة عامة",
        'zoom_cannot_during_search': "لا يمكن التكبير أثناء البحث",
        'zoom_exit_first': "الرجاء الخروج من التكبير أولاً",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "تم تفعيل السحب والإفلات",
        'drag_disabled': "تم تعطيل السحب والإفلات",
        'drag_page_grab': "تم الإمساك بالصفحة {0}",
        'drag_page_dropped': "تم إدراج الصفحة {0} في الموضع {1}",
        'drag_position_invalid': "موضع غير صالح",
        'drag_same_position': "تبقى الصفحة {0} في الموضع {0}",
        'drag_error': "خطأ في النقل",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "إدخال نص مع تنسيقات متقدمة وإدارة كتل النص",
        'text_templates': "كتل النص المتاحة:",
        'text_name': "الاسم",
        'text_preview': "معاينة النص",
        'text_enter': "النص:",
        'text_font_size': "حجم الخط:",
        'text_formatting': "التنسيق:",
        'text_bold': "عريض",
        'text_italic': "مائل",
        'text_underline': "تحته خط",
        'text_alignment': "المحاذاة:",
        'text_left': "يسار",
        'text_center': "وسط",
        'text_right': "يمين",
        'text_color': "لون النص:",
        'text_opacity': "الشفافية:",
        'text_word_wrap': "التفاف النص:",
        'text_auto': "تلقائي",
        'text_page_width_95': "عرض الصفحة (95%)",
        'text_page_width_85': "عريض جداً (85%)",
        'text_page_width_75': "أعرض (75%)",
        'text_page_width_60': "عريض (60%)",
        'text_page_width_50': "متوسط (50%)",
        'text_page_width_30': "ضيق (30%)",
        'text_page_width_20': "أضيق (20%)",
        'text_page_width_10': "ضيق جداً (10%)",
        'text_no_wrap': "بدون التفاف",
        'text_private': "كتلة نص خاصة (تتطلب توثيقاً)",
        'text_preview_label': "معاينة:",
        'text_preview_placeholder': "ستظهر هنا معاينة للنص...",
        'text_no_text': "(لا يوجد نص)",
        'text_save_template': "💾 حفظ ككتلة",
        'text_delete_template': "🗑 حذف كتلة النص المحددة",
        'text_show_private': "إظهار الخاصة",
        'text_hide_private': "إخفاء الخاصة",
        'text_use': "✅ استخدام النص",
        'text_saved': "تم حفظ كتلة النص كـ:\n{0}",
        'text_saved_voice': "تم حفظ كتلة النص",
        'text_deleted': "تم حذف كتلة النص",
        'text_no_text_to_save': "لا يوجد نص للحفظ.",
        'text_no_templates': "لم يتم العثور على كتل نصية",
        'text_private_master_required': "لا يمكن استخدام الكتل الخاصة إلا إذا تم إعداد كلمة مرور رئيسية.\n\nهل ترغب في إعداد كلمة مرور رئيسية الآن؟",
        'text_filename': "اسم ملف كتلة النص (بدون 'Text_' و '.txt'):",
        'text_filename_hint': "مثال: 'هاتف مكتبي' سيتم حفظه كـ 'Text_هاتف مكتبي.txt'",
        'text_save_hint': "سيتم حفظ كتلة النص تلقائياً مع التنسيق.",
        'text_guide_title': "إدخال النص – دليل",
        'text_delete_confirm': "هل أنت متأكد من حذف كتلة النص؟\n\nالملف: {0}\nالنص: {1}...",
        'text_make_public': "وضع علامة كعام",
        'text_make_private': "وضع علامة كخاص",
        'text_privacy_changed': "تم تغيير حالة الخصوصية",
        'text_private_always': "الخاصة تظهر دائماً (إعداد)",
        'text_mode_required': "الرجاء تفعيل وضع النص أولاً",
        'text_continue_editing': "متابعة التحرير – المؤشر في نهاية النص",
        'text_no_input': "لم يتم إدخال نص – تم تجاهل النص",
        'save_dialog_question': "كيف تريد المتابعة؟",
        'text_save_question': "حفظ جميع النصوص والعلامات، ضبط، متابعة التحرير أم تجاهل؟",
        'copy_cross': "تم نسخ العلامة",
        'paste_cross': "تم لصق العلامة",
        'paste_text': "تم لصق النص",
        'cross_discarded': "تم تجاهل العلامة",
        'all_discarded': "تم تجاهل الكل",
        'text_discarded': "تم تجاهل النص",
        'no_texts_to_save': "لا توجد نصوص للحفظ",
        'no_valid_texts': "لا توجد نصوص صالحة للحفظ",
        'text_word_singular': "نص",
        'text_word_plural': "نصوص",
        'cross_word_singular': "علامة",
        'cross_word_plural': "علامات",
        'texts_saved_title': "تم حفظ النصوص",
        'texts_crosses_saved': "تم إدراج {0} {1} و {2} {3} في PDF.\n\nتم إعادة تحميل PDF...",
        'texts_crosses_saved_voice': "تم حفظ {0} {1} و {2} {3}.",
        'texts_saved': "تم إدراج {0} {1} في PDF.\n\nتم إعادة تحميل PDF...",
        'texts_saved_voice': "تم حفظ {0} {1}.",
        'crosses_saved': "تم إدراج {0} {1} في PDF.\n\nتم إعادة تحميل PDF...",
        'crosses_saved_voice': "تم حفظ {0} {1}.",
        'elements_saved': "تم إدراج {0} عناصر في PDF.\n\nتم إعادة تحميل PDF...",
        'elements_saved_voice': "تم حفظ {0} عناصر.",
        'text_window_load_error': "تعذر تحميل نافذة النص",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **إدخال النص وكتل النص – دليل مفصل**

        **1. إدراج وتحرير النص**
        - انقر بزر الماوس الأيمن في المكان المطلوب في المستند واختر "إدراج نص".
        - سيتم فتح حوار حيث يمكنك إدخال النص وتنسيقه:
        • حجم الخط، عريض، مائل، تحته خط
        • لون النص (قابل للاختيار)
        • الشفافية (عتامة) عبر شريط التمرير
        • التفاف النص (عروض مختلفة، مثل عرض الصفحة، ضيق، بدون التفاف)
        - بعد التأكيد، سيظهر النص في موقع النقر. يمكنك تحريكه بالماوس أو مفاتيح الأسهم.
        - انقر نقراً مزدوجاً على النص لفتح وضع التحرير؛ ESC للخروج.

        **2. إدارة كتل النص (القوالب)**
        - على الجانب الأيسر من حوار النص، ترى قائمة بجميع كتل النص المحفوظة.
        - **حفظ كتلة:** أدخل النص، وقم بتنسيقه، وانقر على "💾 حفظ ككتلة". أدخل اسم ملف (بدون امتداد).
        - **تحميل كتلة:** انقر على الاسم المطلوب في القائمة. سيتم استيراد النص والتنسيق ويمكن تعديله إذا لزم الأمر.
        - **حذف:** انقر بزر الماوس الأيمن على كتلة لحذفها أو تغيير حالة خصوصيتها.

        **3. كتل النص الخاصة (كلمة المرور الرئيسية)**
        - إذا قمت بإعداد كلمة مرور رئيسية (في الإعدادات ← إدارة كلمات المرور)، يمكنك وضع علامة على الكتل كـ "خاصة".
        - حدد مربع الاختيار "كتلة نص خاصة" في الحوار قبل الحفظ.
        - تظهر الكتل الخاصة في القائمة فقط إذا قمت بإدخال كلمة المرور الرئيسية مرة واحدة في الجلسة (التوثيق عبر رمز القفل أو عند أول وصول).
        - بهذه الطريقة يمكنك حماية كتل النص السرية من الوصول غير المصرح به.

        **4. إدراج العلامات (علامات X)**
        - من القائمة السياقية، يمكنك أيضاً إدراج علامة X رسومية (مثل مربعات الاختيار).
        - يمكن ضبط حجم وسمك الخط ولون العلامات عالمياً في الإعدادات (القائمة "الإعدادات" ← "إعدادات العلامات").
        - انقر بزر الماوس الأيمن على علامة موجودة لتعديلها بشكل فردي.

        **5. الإجراءات الجماعية**
        - إذا قمت بوضع عدة نصوص أو علامات على صفحة واحدة، يمكنك حفظها أو تجاهلها جميعاً مرة واحدة من القائمة السياقية (انقر بزر الماوس الأيمن في وضع النص).
        - عند الحفظ، يتم دمج جميع العناصر في PDF وتبقى كرسومات متجهة.

        **6. اختصارات لوحة المفاتيح في وضع النص**
        - مفاتيح الأسهم: تحريك العنصر
        - Ctrl+مفاتيح الأسهم: خطوات أكبر
        - Enter: فتح حوار الحفظ (حفظ الكل / ضبط / تجاهل)
        - ESC: تجاهل العنصر الحالي
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html dir="rtl">
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 إدخال النص وكتل النص – دليل مفصل</strong></p>

        <p><strong>1. إدراج وتحرير النص</strong></p>
        <ul>
        <li>انقر بزر الماوس الأيمن في المكان المطلوب في المستند واختر "إدراج نص".</li>
        <li>سيتم فتح حوار حيث يمكنك إدخال النص وتنسيقه:<br/>
        • حجم الخط، عريض، مائل، تحته خط<br/>
        • لون النص (قابل للاختيار)<br/>
        • الشفافية (عتامة) عبر شريط التمرير<br/>
        • التفاف النص (عروض مختلفة، مثل عرض الصفحة، ضيق، بدون التفاف)</li>
        <li>بعد التأكيد، سيظهر النص في موقع النقر. يمكنك تحريكه بالماوس أو مفاتيح الأسهم.</li>
        <li>انقر نقراً مزدوجاً على النص لفتح وضع التحرير؛ ESC للخروج.</li>
        </ul>

        <p><strong>2. إدارة كتل النص (القوالب)</strong></p>
        <ul>
        <li>على الجانب الأيسر من حوار النص، ترى قائمة بجميع كتل النص المحفوظة.</li>
        <li><strong>حفظ كتلة:</strong> أدخل النص، وقم بتنسيقه، وانقر على "💾 حفظ ككتلة". أدخل اسم ملف (بدون امتداد).</li>
        <li><strong>تحميل كتلة:</strong> انقر على الاسم المطلوب في القائمة. سيتم استيراد النص والتنسيق ويمكن تعديله إذا لزم الأمر.</li>
        <li><strong>حذف:</strong> انقر بزر الماوس الأيمن على كتلة لحذفها أو تغيير حالة خصوصيتها.</li>
        </ul>

        <p><strong>3. كتل النص الخاصة (كلمة المرور الرئيسية)</strong></p>
        <ul>
        <li>إذا قمت بإعداد كلمة مرور رئيسية (في الإعدادات ← إدارة كلمات المرور)، يمكنك وضع علامة على الكتل كـ "خاصة".</li>
        <li>حدد مربع الاختيار "كتلة نص خاصة" في الحوار قبل الحفظ.</li>
        <li>تظهر الكتل الخاصة في القائمة فقط إذا قمت بإدخال كلمة المرور الرئيسية مرة واحدة في الجلسة (التوثيق عبر رمز القفل أو عند أول وصول).</li>
        <li>بهذه الطريقة يمكنك حماية كتل النص السرية من الوصول غير المصرح به.</li>
        </ul>

        <p><strong>4. إدراج العلامات (علامات X)</strong></p>
        <ul>
        <li>من القائمة السياقية، يمكنك أيضاً إدراج علامة X رسومية (مثل مربعات الاختيار).</li>
        <li>يمكن ضبط حجم وسمك الخط ولون العلامات عالمياً في الإعدادات (القائمة "الإعدادات" ← "إعدادات العلامات").</li>
        <li>انقر بزر الماوس الأيمن على علامة موجودة لتعديلها بشكل فردي.</li>
        </ul>

        <p><strong>5. الإجراءات الجماعية</strong></p>
        <ul>
        <li>إذا قمت بوضع عدة نصوص أو علامات على صفحة واحدة، يمكنك حفظها أو تجاهلها جميعاً مرة واحدة من القائمة السياقية (انقر بزر الماوس الأيمن في وضع النص).</li>
        <li>عند الحفظ، يتم دمج جميع العناصر في PDF وتبقى كرسومات متجهة.</li>
        </ul>

        <p><strong>6. اختصارات لوحة المفاتيح في وضع النص</strong></p>
        <ul>
        <li>مفاتيح الأسهم: تحريك العنصر</li>
        <li>Ctrl+مفاتيح الأسهم: خطوات أكبر</li>
        <li>Enter: فتح حوار الحفظ (حفظ الكل / ضبط / تجاهل)</li>
        <li>ESC: تجاهل العنصر الحالي</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "إعدادات العلامات",
        'cross_properties': "خصائص العلامة",
        'cross_size': "الحجم (بكسل):",
        'cross_line_width': "سماكة الخط:",
        'cross_color': "اللون:",
        'cross_choose_color': "اختيار",
        'cross_fine_tuning': "ضبط دقيق عند الحفظ (بكسل)",
        'cross_offset_x': "إزاحة X:",
        'cross_offset_y': "إزاحة Y:",
        'cross_offset_x_tooltip': "القيم السالبة تحرك العلامة لليسار عند الحفظ، الموجبة لليمين",
        'cross_offset_y_tooltip': "القيم السالبة تحرك العلامة لأعلى عند الحفظ، الموجبة لأسفل",
        'cross_preview': "معاينة",
        'cross_save': "تطبيق الإعدادات",
        'cross_customized': "تم تعديل العلامة",
        'cross_settings_applied': "تم حفظ إعدادات العلامات.\nالحجم: {0}بكسل، سماكة الخط: {1}بكسل\n{2}",
        'cross_updated_count': "تم تحديث {0} علامات موجودة.",
        'cross_no_crosses': "لم يتم العثور على علامات موجودة.",
        'cross_settings_applied_all': "تم تطبيق إعدادات العلامات على جميع العلامات الـ {0}",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "إعدادات التوقيع",
        'signature_1': "التوقيع 1",
        'signature_2': "التوقيع 2",
        'signature_select': "اختر توقيعاً",
        'signature_add': "➕ إضافة توقيع جديد...",
        'signature_size': "حجم التوقيع {0} (%):",
        'signature_common': "الإعدادات العامة",
        'signature_timestamp': "إضافة طابع زمني تلقائياً",
        'signature_location': "الموقع الافتراضي:",
        'signature_timestamp_size': "حجم خط الطابع الزمني:",
        'signature_no_files': "-- لم يتم العثور على توقيعات --",
        'signature_insert': "إدراج توقيع",
        'signature_insert_1': "إدراج التوقيع 1",
        'signature_insert_2': "إدراج التوقيع 2",
        'signature_customize': " تعديل التوقيع",
        'signature_discard': " تجاهل هذا التوقيع",
        'signature_save_all': " حفظ جميع التوقيعات",
        'signature_discard_all': " تجاهل جميع التوقيعات",
        'signature_guide_title': "التوقيعات – دليل",
        'signature_guide': """
📝 التوقيعات – دليل سريع

- قم بإعداد كلمة مرور رئيسية
- قم بتكوين التوقيعات في قائمة الإعدادات
  (الحجم، الطابع الزمني ...)
- أدرج بزر الماوس الأيمن في الموقع المطلوب
  (كلمة المرور الرئيسية مطلوبة مرة واحدة في الجلسة)
- حرك التوقيع بالماوس أو مفاتيح الأسهم
- يمكن إدراج عدة توقيعات واحداً تلو الآخر
- يمكن تعديل كل توقيع بشكل فردي
- تجاهل توقيع واحد
- حفظ / تجاهل جميع التوقيعات دفعة واحدة
- بدلاً من ذلك، يمكن استخدام شريط القوائم.
        """,
        'signature_placeholder': "المعاينة غير متوفرة",
        'signature_info': "التوقيع {0}: {1}×{2} بكسل ({3}% من {4}×{5})",
        'signature_info_placeholder': "إعدادات التوقيع {0}",
        'signature_inserted': "تم إدراج التوقيع {0} في الصفحة {1}",
        'signature_deleted': "تم حذف التوقيع",
        'signature_copied': "تم نسخ التوقيع",
        'signature_pasted': "تم لصق التوقيع {0}",
        'signature_saved': "تم إدراج {0} توقيعات في PDF.\n\nتم إعادة تحميل PDF...",
        'signature_saved_voice': "تم حفظ {0} توقيعات",
        'mode_replace_signature_format': "الخروج من الوضع وإدراج التوقيع {0}",
        'mode_conflict_voice_signature': "الوضع {0} نشط. هل تريد الخروج وإدراج توقيع؟",
        'signature_not_configured': "التوقيع {0} غير مهيأ",
        'signature_file_not_found': "لم يتم العثور على ملف التوقيع",
        'timestamp_format': "{0}، {1}",
        'no_copied_signature': "لا يوجد توقيع منسوخ",
        'no_signatures_to_save': "لا توجد توقيعات للحفظ",
        'signature_save_question': "حفظ جميع التوقيعات، تعديل أم تجاهل هذا؟",
        'signatures_saved_title': "تم حفظ التوقيعات",
        'signatures_saved': "تم إدراج {0} توقيعات في PDF.\n\nتم إعادة تحميل PDF...",
        'signatures_saved_voice': "تم حفظ {0} توقيعات.",
        'all_signatures_discarded': "تم تجاهل جميع التوقيعات",
        'signature_settings_saved': "تم حفظ إعدادات التوقيع",
        'signature_cancelled': "تم تجاهل التوقيع",
        'signature_active_title': "التوقيع نشط",
        'signature_replace_question': "يوجد بالفعل توقيع نشط.\n\nهل تريد استبدال التوقيع الحالي؟",
        'signature_replace': "استبدال التوقيع",
        'signature_replace_voice': "استبدال التوقيع الحالي أم إلغاء؟",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "إعدادات الصور",
        'image_common': "إعدادات الصور العامة",
        'image_keep_aspect': "الحفاظ على نسبة العرض إلى الارتفاع عند السحب",
        'image_default_size': "الحجم الافتراضي (%):",
        'image_dark_invert': "عكس ألوان الصور في الوضع الداكن",
        'image_dark_invert_tooltip': "مفعل: يتم عكس الصور لرؤية أفضل",
        'image_fine_tuning': "ضبط دقيق (بكسل)",
        'image_offset_x': "إزاحة X:",
        'image_offset_y': "إزاحة Y:",
        'image_offset_x_tooltip': "القيم السالبة تحرك الصورة لليسار عند الحفظ، الموجبة لليمين",
        'image_offset_y_tooltip': "القيم السالبة تحرك الصورة لأعلى عند الحفظ، الموجبة لأسفل",
        'image_select': "اختر صورة",
        'image_insert': "إدراج صورة",
        'image_customize': " تعديل الصورة",
        'image_aspect': " الحفاظ على نسبة العرض إلى الارتفاع",
        'image_discard': " تجاهل هذه الصورة",
        'image_save_all': " حفظ جميع الصور",
        'image_discard_all': " تجاهل جميع الصور",
        'image_filter': "الصور",
        'image_guide_title': "إدراج الصور – دليل",
        'image_guide': """
📷 إدراج الصور في PDF – دليل سريع:

1. انقر بزر الماوس الأيمن في الموقع المطلوب
2. "إدراج صورة" → اختر صورة
3. ضع الصورة: اسحب بالماوس
4. اضبط الحجم: اسحب من الزوايا/الحواف
5. الحفاظ على نسبة العرض إلى الارتفاع: مفتاح [A]
6. تعديلات إضافية: انقر بزر الماوس الأيمن على الصورة

نصيحة: في القائمة السياقية، يمكنك ضبط الإعدادات.
        """,
        'image_inserted': "تم إدراج صورة في الصفحة {1}",
        'image_deleted': "تم تجاهل الصورة",
        'image_copied': "تم نسخ الصورة",
        'image_pasted': "تم لصق الصورة",
        'image_saved': "تم إدراج {0} صور في PDF.\n\nتم إعادة تحميل PDF...",
        'image_saved_voice': "تم حفظ {0} صور",
        'image_aspect_on': "مفعل",
        'image_aspect_off': "معطل",
        'image_aspect_toggle': "الحفاظ على نسبة العرض إلى الارتفاع {0}",
        'image_reset': "تم إعادة الصورة إلى حجمها الأصلي",
        'image_replaced': "تم استبدال الصورة",
        'image_invalid': "صورة غير صالحة",
        'mode_replace_image': "إدراج صورة",
        'mode_conflict_voice_image': "الوضع {0} نشط. هل تريد الخروج وإدراج صورة؟",
        'image_active_title': "الصورة نشطة",
        'image_replace_question': "يوجد بالفعل صورة نشطة.\n\nهل تريد استبدال الصورة الحالية؟",
        'image_replace': "استبدال الصورة",
        'image_replace_voice': "استبدال الصورة الحالية أم إلغاء؟",
        'image_filter_all': "الصور (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;جميع الملفات (*.*)",
        'no_copied_image': "لا توجد صورة منسوخة",
        'image_discarded': "تم تجاهل الصورة",
        'image_save_question': "حفظ جميع الصور، تعديل أم تجاهل هذه؟",
        'no_images_to_save': "لا توجد صور للحفظ",
        'no_valid_images': "لا توجد صور صالحة للحفظ",
        'images_saved_title': "تم حفظ الصور",
        'images_saved': "تم إدراج {0} صور في PDF.\n\nتم إعادة تحميل PDF...",
        'images_saved_voice': "تم حفظ {0} صور.",
        'all_images_discarded': "تم تجاهل جميع الصور",
        'image_settings_updated': "تم تحديث إعدادات الصور",
        'image_replace_title': "اختر صورة جديدة",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "إعدادات الأشكال",
        'form_basic': "الإعدادات الأساسية",
        'form_default_type': "نوع الشكل الافتراضي:",
        'form_rectangle': "مستطيل",
        'form_ellipse': "قطع ناقص",
        'form_line': "خط",
        'form_arrow': "سهم",
        'form_line_width': "سماكة الخط:",
        'form_colors': "الألوان",
        'form_line_color': "لون الخط:",
        'form_fill_color': "لون التعبئة:",
        'form_choose_color': "اختيار",
        'form_transparent': "خلفية شفافة (خط فقط)",
        'form_filled': "مملوء",
        'form_dark_mode': "الوضع الداكن",
        'form_dark_invert': "عكس الألوان في الوضع الداكن",
        'form_fine_tuning': "ضبط دقيق (بكسل)",
        'form_offset_x': "إزاحة X:",
        'form_offset_y': "إزاحة Y:",
        'form_offset_x_tooltip': "القيم السالبة تحرك الشكل لليسار عند الحفظ، الموجبة لليمين",
        'form_offset_y_tooltip': "القيم السالبة تحرك الشكل لأعلى عند الحفظ، الموجبة لأسفل",
        'form_preview': "معاينة",
        'form_insert': "إدراج شكل",
        'form_rectangle_insert': "مستطيل",
        'form_ellipse_insert': "قطع ناقص/دائرة",
        'form_line_insert': "خط (نقرتان)",
        'form_arrow_insert': "سهم (نقرتان)",
        'form_customize': " تعديل الشكل",
        'form_transparent_toggle': " خلفية شفافة",
        'form_discard': " تجاهل هذا الشكل",
        'form_save_all': " حفظ جميع الأشكال",
        'form_discard_all': " تجاهل جميع الأشكال",
        'form_guide_title': "إدراج الأشكال – دليل",
        'form_guide': """
📐 إدراج الأشكال في PDF – دليل سريع:

1. اختر نوع الشكل (مستطيل، قطع ناقص، خط، سهم)
2. انقر في الموضع
   - مستطيل/قطع ناقص: نقرة واحدة تضع الشكل
   - خط/سهم: نقرتان لنقطة البداية والنهاية
3. ضع الشكل: اسحب بالماوس
4. اضبط الحجم: اسحب من الزوايا/الحواف
5. حفظ الشكل: Enter
6. تجاهل الشكل: ESC
7. تعديلات إضافية: انقر بزر الماوس الأيمن على الشكل

نصيحة: في القائمة السياقية، يمكنك ضبط الإعدادات.
        """,
        'form_inserted': "تم إدراج {0} في الصفحة {1}",
        'form_deleted': "تم حذف الشكل",
        'form_copied': "تم نسخ الشكل",
        'form_pasted': "تم لصق الشكل",
        'form_saved': "تم إدراج {0} أشكال في PDF.\n\nتم إعادة تحميل PDF...",
        'form_saved_voice': "تم حفظ {0} أشكال",
        'form_reset': "تم إعادة الشكل إلى الحجم الافتراضي",
        'form_transparent_on': "مفعل",
        'form_transparent_off': "معطل",
        'form_transparent_toggled': "الخلفية الشفافة {0}",
        'form_line_cancel': "تم إلغاء رسم الخط",
        'form_second_click': "الآن انقر على نقطة النهاية لـ {0}",
        'mode_replace_form': "إدراج شكل",
        'mode_conflict_voice_form': "الوضع {0} نشط. هل تريد الخروج وإدراج شكل؟",
        'form_settings_updated': "تم تحديث إعدادات الأشكال",
        'form_unknown': "شكل",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. انقر على نقطة البداية",
        'form_line_guide_2': "2. انقر على نقطة النهاية",
        'form_line_guide_3': "سيتم رسم الخط بين النقطتين.",
        'form_line_status_1': "في انتظار النقرة الأولى...",
        'form_line_status_2': "تم تعيين النقطة الأولى: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "الآن انقر على نقطة النهاية...",
        'form_line_status_4': "تم تعيين كلتا النقطتين.\nانقر على 'إنهاء' للحفظ.",
        'form_line_reset': "إعادة تعيين",
        'form_line_finish': "إنهاء",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "نسخ (Cmd+C)",
        'paste': "لصق (Cmd+V)",
        'copied': "تم النسخ: {0}",
        'no_element_to_copy': "لم يتم تحديد عنصر للنسخ",
        'no_copied_data': "لا توجد بيانات منسوخة",
        'no_valid_position': "لا يوجد موضع صالح للصق",
        'copy_text': "تم نسخ النص",
        'copy_image': "تم نسخ الصورة",
        'copy_form': "تم نسخ الشكل",
        'copy_signature': "تم نسخ التوقيع",
        'element_text': "نص",
        'element_image': "صورة",
        'element_form': "شكل",
        'element_signature': "توقيع",
        'element_unknown': "عنصر",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "تضارب الأوضاع",
        'mode_conflict_message': "الوضع '{0}' نشط بالفعل.\n\nهل تريد الخروج منه و {1}؟",
        'mode_replace': "الخروج من الوضع و {0}",
        'mode_cancel': "إلغاء",
        'mode_replace_text': "إدراج نص",
        'mode_replace_cross': "إدراج علامة",
        'mode_replace_signature': "إدراج توقيع",
        'mode_replace_image': "إدراج صورة",
        'mode_replace_form': "إدراج شكل",
        'mode_conflict_voice': "الوضع {0} نشط. هل تريد الخروج وإدراج نص؟",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "إدخال نص",
        'active_mode_signature': "توقيع",
        'active_mode_image': "صورة",
        'active_mode_form': "شكل",
        'active_mode_and': " و ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "إدراج",
        'insert_another_text': "إدراج نص",
        'insert_another_cross': "إدراج علامة",
        'insert_another_signature_1': "التوقيع 1",
        'insert_another_signature_2': "التوقيع 2",
        'insert_another_image': "إدراج صورة",
        'insert_another_form_rect': "مستطيل",
        'insert_another_form_ellipse': "قطع ناقص",
        'insert_another_form_line': "خط (نقرتان)",
        'insert_another_form_arrow': "سهم (نقرتان)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "حفظ {0}",
        'save_dialog_message': "سيتم حفظ {0} في الصفحة {1}.\n\nكيف تريد المتابعة؟",
        'save_all': "حفظ جميع {0}",
        'save_single': "حفظ {0}",
        'save_customize': "تعديل {0}",
        'save_discard': "تجاهل هذا {0}",
        'save_continue': "متابعة التحرير",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " الذهاب إلى الصفحة {0}",
        'context_rotate': " تدوير الصفحة {0}",
        'context_delete': " حذف الصفحة {0}",
        'context_export': " تصدير الصفحة {0}",
        'context_mark_as': " وضع علامة على الصفحة كـ...",
        'context_mark_empty': " صفحة فارغة",
        'context_unmark_empty': " لم تعد فارغة",
        'context_mark_export': " وضع علامة للتصدير",
        'context_unmark_export': " لا تصدر بعد الآن",
        'context_batch_actions': " إجراءات جماعية",
        'context_batch_delete_empty': " حذف جميع الصفحات الفارغة ({0})",
        'context_batch_export_single': " تصدير جميع الصفحات ({0}) (ملف واحد)",
        'context_batch_export_split': " تصدير جميع الصفحات ({0}) (منفصلة)",
        'context_drag_start': " بدء السحب والإفلات",
        'context_drag_stop': " إيقاف السحب والإفلات",
        'context_insert': " إدراج",
        'context_insert_pages': " إدراج صفحات",
        'context_zoom': "تكبير",
        'discard_mixed': "تجاهل جميع {0} {1} و {2} {3}",
        'save_mixed': "حفظ {0} {1} و {2} {3}",
        'discard_texts': "تجاهل جميع النصوص ({0})",
        'discard_text_single': "تجاهل نص واحد",
        'save_texts': "حفظ {0} نصوص",
        'save_text_single': "حفظ نص واحد",
        'discard_crosses': "تجاهل جميع العلامات ({0})",
        'discard_cross_single': "تجاهل علامة واحدة",
        'save_crosses': "حفظ {0} علامات",
        'save_cross_single': "حفظ علامة واحدة",
        'discard_signatures': "تجاهل جميع التوقيعات ({0})",
        'save_signature_single': "حفظ توقيع واحد",
        'save_signatures': "حفظ {0} توقيعات",
        'discard_images': "تجاهل جميع الصور ({0})",
        'save_image_single': "حفظ صورة واحدة",
        'save_images': "حفظ {0} صور",
        'discard_forms': "تجاهل جميع الأشكال ({0})",
        'save_form_single': "حفظ شكل واحد",
        'save_forms': "حفظ {0} أشكال",
        'cross_discard': "تجاهل هذه العلامة",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 معلومات التصدير / الاستيراد",
        'export_what': "📋 ما الذي يتم تصديره؟",
        'export_general': "الإعدادات العامة",
        'export_general_items': "• الإخراج الصوتي (تشغيل/إيقاف، السرعة)\n• الوضع الداكن/الفاتح\n• إعدادات النسخ الاحتياطي\n• إعدادات OCR",
        'export_image_form': "إعدادات الصور والأشكال",
        'export_image_form_items': "• إعدادات الصور (نسبة العرض إلى الارتفاع، الحجم الافتراضي)\n• إعدادات الأشكال (سماكة الخط، الألوان)\n• إعدادات التوقيع (المسارات، الأحجام، الطابع الزمني)",
        'export_passwords': "قاعدة بيانات كلمات المرور",
        'export_passwords_items': "• جميع كلمات مرور PDF المحفوظة\n• قابلة للاختيار مشفرة أو مفكوكة التشفير",
        'export_master': "إعدادات كلمة المرور الرئيسية",
        'export_master_items': "• هاش كلمة المرور الرئيسية\n• إعدادات التوقيعات/كتل النص",
        'export_signatures': "التوقيعات وكتل النص",
        'export_signatures_items': "• جميع ملفات الصور (التوقيعات)\n• جميع كتل النص مع التنسيق\n• علامات خاصة/عامة",
        'export_import_warning': "⚠️ ملاحظات هامة",
        'export_import_note': "• عند الاستيراد، سيتم استبدال جميع الإعدادات الحالية\n• يلزم إعادة تشغيل التطبيق\n• سيتم استبدال التوقيعات/كتل النص الموجودة",
        'export_master_note': "• إذا تم تعيين كلمة مرور رئيسية، يمكنك اختيار:\n  - مفكوك التشفير (كلمات المرور بنص واضح)\n  - مشفر (قابل للقراءة فقط بكلمة المرور الرئيسية)",
        'export_security': "• ملف ZIP المُصدَّر يحتوي على بيانات سرية\n• احتفظ به بأمان (مثل محرك أقراص USB مشفر)\n• في حالة فقدان الملف، تفقد كلمات المرور بشكل نهائي",
        'export_format': "📁 تنسيق التصدير",
        'export_format_desc': "يتم حفظ الإعدادات في ملف ZIP واحد:",
        'export_filename': "إعدادات_PDFDarkView_YYYYMMDD_HHMMSS.zip",
        'export_success': "تم تصدير الإعدادات بنجاح",
        'export_failed': "فشل التصدير",
        'export_import_question': "هل تريد إعادة تشغيل التطبيق الآن؟",
        'export_password_question': "تم تعيين كلمة مرور رئيسية.\n\nهل تريد تصدير كلمات المرور مفكوكة التشفير؟\n(وإلا سيتم تصديرها مشفرة)",
        'export_decrypt': "تصدير مفكوك التشفير",
        'export_encrypt': "تصدير مشفر",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " معلومات",
        'info_title': "حول PDF دارك فيو",
        'info_version': "الإصدار",
        'info_author': "تم التطوير بواسطة Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "حول",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> هو عارض PDF يمكن الوصول إليه، تم تطويره خصيصًا للأشخاص ذوي الإعاقة البصرية.</p>

            <p><strong>الميزات الأساسية:</strong></p>
            <ul>
                <li>واجهة عالية التباين وقابلة للتخصيص</li>
                <li>تحكم كامل عبر لوحة المفاتيح</li>
                <li>ميزة النطق المدمجة</li>
                <li>OCR للمستندات الممسوحة ضوئيًا</li>
                <li>أدوات تحرير شاملة</li>
            </ul>

            <p>يتم دعم أكثر من 50 لغة – مما يجعل ملفات PDF في متناول الجميع.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "الميزات",
        'info_features_intro': "يتيح لك PDF Dark View الإمكانيات التالية:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>العرض والتنقل</strong> – الوضع الداكن/الفاتح، تصفح الصفحات، التكبير، الانتقال إلى صفحة</li>
            <li><strong>OCR (التعرف على النص)</strong> – جعل المستندات الممسوحة ضوئيًا قابلة للبحث والنسخ</li>
            <li><strong>التحرير</strong> – إدراج نصوص، علامات X، توقيعات، صور وأشكال</li>
            <li><strong>إدارة الصفحات</strong> – حذف، استخراج، إدراج، نقل عبر السحب والإفلات</li>
            <li><strong>التصدير</strong> – إلى Word، Pages أو كنص</li>
            <li><strong>الأمان</strong> – حماية وإدارة كلمات المرور</li>
            <li><strong>سهولة الوصول</strong> – النطق، التحكم عبر لوحة المفاتيح، تباين عالٍ</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "الاستخدام",
        'info_accessibility': "♿ سهولة الوصول – تحكم كامل عبر لوحة المفاتيح",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 عام</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> فتح PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> بحث</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> تبديل الوضع الداكن/الفاتح</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> طباعة</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> إنهاء</div>

        <div class="shortcut-cat">📖 التنقل</div>
        <div class="shortcut-row"><kbd>أسهم</kbd> تصفح صفحة تلو الأخرى</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> الانتقال إلى صفحة</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> الصفحة الأولى</div>
        <div class="shortcut-row"><kbd>Ende</kbd> الصفحة الأخيرة</div>

        <div class="shortcut-cat">✏️ التحرير</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> إدراج نص</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> حذف الصفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> استخراج الصفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> إدراج صفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> نقل الصفحات</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> تدوير الصفحة</div>

        <div class="shortcut-cat">🖼️ نقل العناصر</div>
        <div class="shortcut-row"><kbd>أسهم</kbd> نقل نص/صورة/توقيع</div>
        <div class="shortcut-row"><kbd>Ctrl+أسهم</kbd> خطوات أكبر</div>
        <div class="shortcut-row"><kbd>Enter</kbd> حفظ</div>
        <div class="shortcut-row"><kbd>ESC</kbd> تجاهل</div>

        <div class="shortcut-cat">🗣️ النطق</div>
        <div class="shortcut-row"><kbd>F2</kbd> تشغيل/إيقاف النطق</div>
        """,
        'info_contextmenu': "📌 هام: جميع الوظائف متاحة أيضًا عبر القائمة المنسدلة (زر الفأرة الأيمن)!",
        'info_accessibility_hint': "💡 تلميح: ميزة النطق (F2) تسهل التوجيه وتوفر ردود فعل للقوائم والحوارات.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "الترخيص & بصمة",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 بصمة</strong><br>
        المعلومات وفقًا للمادة § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, ألمانيا<br>
        البريد الإلكتروني: binhdiez64@gmail.com<br>
        المسؤول عن المحتوى: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ إخلاء مسؤولية</strong><br>
        تم تطوير البرنامج بأقصى درجات العناية. لا يتم تقديم أي ضمان للدقة والاكتمال والوظائف. الاستخدام على مسؤوليتك الخاصة.<br><br>

        <strong>📄 ترخيص MIT (الاستخدام الخاص)</strong><br>
        حقوق النشر (c) 2026 Toralf Schulz (BinhDiez)<br>
        المسموح به: الاستخدام المجاني، التعديلات الخاصة، النسخ الشخصية.<br>
        غير المسموح به: البيع، الاستخدام التجاري، إزالة إشعارات حقوق النشر.<br><br>

        <strong>🔧 مكونات الطرف الثالث</strong><br>
        يحتوي هذا البرنامج على مكونات بموجب تراخيص GPL، AGPL، Apache 2.0، BSD و MIT.<br>
        عند إعادة التوزيع، يجب الامتثال لشروط الترخيص الخاصة بكل منها.<br><br>

        <strong>🌐 مفتوح المصدر</strong><br>
        الكود المصدري متاح ويمكن الاطلاع عليه وتعديله وإعادة توزيعه وفقًا لشروط الترخيص الخاصة بكل منها.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "شكر وتقدير",
        'info_credits': "شكرًا لمجتمع المصادر المفتوحة",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – معالجة PDF</li>
            <li><strong>PyQt5</strong> – الواجهة الرسومية</li>
            <li><strong>Tesseract OCR</strong> – التعرف على النص</li>
            <li><strong>OCRmyPDF</strong> – دمج OCR</li>
            <li><strong>python-docx</strong> – تصدير إلى Word</li>
            <li><strong>qtawesome</strong> – أيقونات</li>
            <li><strong>DeepSeek</strong> – الدعم في الترجمات (50+ لغة)</li>
            <li><strong>جميع المستخدمين</strong> – للتغذية الراجعة القيمة</li>
            <li><strong>مجتمع المصادر المفتوحة</strong> – للمكتبات الرائعة</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "اللغات",
        'info_languages_header': "🌍 دعم اللغات",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>يدعم PDF Dark View حاليًا <strong>62 لغة</strong> – لضمان إمكانية استخدام البرنامج عالميًا دون عوائق.</p>

            <p><strong>📖 قائمة اللغات الكاملة (حالة: مارس 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 الأفريقانية</li>
                    <li>🇦🇱 الألبانية (Shqip)</li>
                    <li>🇩🇿 العربية (العربية)</li>
                    <li>🇮🇩 البالية (Basa Bali)</li>
                    <li>🇧🇩 البنغالية (বাংলা)</li>
                    <li>🇲🇲 البورمية (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 البوسنية (Bosanski)</li>
                    <li>🇧🇬 البلغارية (Български)</li>
                    <li>🇨🇳 الصينية (中文)</li>
                    <li>🇩🇰 الدنماركية (Dansk)</li>
                    <li>🇩🇪 الألمانية</li>
                    <li>🇬🇧 الإنجليزية (English)</li>
                    <li>🇪🇪 الإستونية (Eesti)</li>
                    <li>🇫🇮 الفنلندية (Suomi)</li>
                    <li>🇫🇷 الفرنسية (Français)</li>
                    <li>🇬🇷 اليونانية (Ελληνικά)</li>
                    <li>🇮🇱 العبرية (עברית)</li>
                    <li>🇮🇳 الهندية (हिन्दी)</li>
                    <li>🇭🇷 الكرواتية (Hrvatski)</li>
                    <li>🇭🇺 المجرية (Magyar)</li>
                    <li>🇮🇩 الإندونيسية (Bahasa Indonesia)</li>
                    <li>🇮🇪 الأيرلندية (Gaeilge)</li>
                    <li>🇮🇸 الأيسلندية (Íslenska)</li>
                    <li>🇮🇹 الإيطالية (Italiano)</li>
                    <li>🇯🇵 اليابانية (日本語)</li>
                    <li>🇰🇭 الخميرية (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 الكورية (한국어)</li>
                    <li>🇱🇦 اللاوسية (ພາສາລາວ)</li>
                    <li>🇱🇻 اللاتفية (Latviešu)</li>
                    <li>🇱🇹 الليتوانية (Lietuvių)</li>
                    <li>🇱🇺 اللوكسمبورغية (Lëtzebuergesch)</li>
                    <li>🇲🇾 الماليزية (Bahasa Melayu)</li>
                    <li>🇮🇳 الماراثية (मराठी)</li>
                    <li>🇲🇳 المنغولية (Монгол)</li>
                    <li>🇳🇵 النيبالية (नेपाली)</li>
                    <li>🇳🇱 الهولندية (Nederlands)</li>
                    <li>🇳🇴 النرويجية (Norsk)</li>
                    <li>🇦🇫 البشتوية (پښتو)</li>
                    <li>🇮🇷 الفارسية (فارسی)</li>
                    <li>🇵🇱 البولندية (Polski)</li>
                    <li>🇵🇹 البرتغالية (Português)</li>
                    <li>🇮🇳 البنجابية (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 الرومانية (Română)</li>
                    <li>🇷🇺 الروسية (Русский)</li>
                    <li>🇸🇪 السويدية (Svenska)</li>
                    <li>🇷🇸 الصربية (Српски)</li>
                    <li>🇸🇰 السلوفاكية (Slovenčina)</li>
                    <li>🇸🇮 السلوفينية (Slovenščina)</li>
                    <li>🇪🇸 الإسبانية (Español)</li>
                    <li>🇹🇿 السواحيلية (Kiswahili)</li>
                    <li>🇵🇭 التاغالوغية (Filipino)</li>
                    <li>🇮🇳 التاميلية (தமிழ்)</li>
                    <li>🇮🇳 التيلوغوية (తెలుగు)</li>
                    <li>🇹🇭 التايلاندية (ไทย)</li>
                    <li>🇨🇿 التشيكية (Čeština)</li>
                    <li>🇹🇷 التركية (Türkçe)</li>
                    <li>🇺🇦 الأوكرانية (Українська)</li>
                    <li>🇵🇰 الأردية (اردو)</li>
                    <li>🇻🇳 الفيتنامية (Tiếng Việt)</li>
                    <li>🇸🇳 الولوفية (Wolof)</li>
                    <li>🇺🇸 اليديشية (ייִדיש)</li>
                    <li>🇿🇦 الزولو (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 إضافة لغات خاصة:</strong><br>
                هل ترغب في لغة غير متوفرة بعد؟ ما عليك سوى وضع ملف القاموس الخاص بك (<code>sprache_xx.py</code>) بجانب التطبيق – وسيتعرف عليه البرنامج تلقائيًا. إذا كنت مهتمًا بترجمة خاصة، فلا تتردد في الاتصال بي.
            </div>

            <p><strong>🙏 شكر خاص:</strong> DeepSeek لدعمه في ترجمة جميع القواميس إلى 62 لغة.</p>

            <p>📧 للتواصل بخصوص الترجمات: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "خطأ",
        'error_occurred': "حدث خطأ",
        'error_pdf_load': "خطأ في تحميل PDF",
        'error_pdf_save': "خطأ في حفظ PDF",
        'error_ocr': "خطأ في التعرف على النص",
        'error_no_pdf': "لا يوجد PDF محمل",
        'error_page_not_found': "الصفحة غير موجودة",
        'error_invalid_range': "نطاق صفحات غير صالح",
        'error_file_not_found': "الملف غير موجود",
        'error_permission': "لا توجد صلاحية",
        'error_unknown': "خطأ غير معروف",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "نجاح",
        'success_operation': "تمت العملية بنجاح",
        'success_saved': "تم الحفظ بنجاح",
        'success_exported': "تم التصدير بنجاح",
        'success_imported': "تم الاستيراد بنجاح",
        'success_deleted': "تم الحذف بنجاح",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "تأكيد",
        'confirm_yes': "نعم",
        'confirm_no': "لا",
        'confirm_ok': "موافق",
        'confirm_cancel': "إلغاء",
        'confirm_delete': "حذف",
        'confirm_overwrite': "استبدال",
        'confirm_continue': "متابعة",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "جاري تحميل PDF...",
        'progress_saving': "جاري حفظ PDF...",
        'progress_exporting': "جاري تصدير PDF...",
        'progress_processing': "جاري المعالجة...",
        'progress_wait': "الرجاء الانتظار...",
        'progress_preparing': "جاري التحضير...",
        'progress_finalizing': "جاري الإنهاء...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "أبيض",
        'color_black': "أسود",
        'color_red': "أحمر",
        'color_green': "أخضر",
        'color_blue': "أزرق",
        'color_yellow': "أصفر",
        'color_magenta': "أرجواني",
        'color_cyan': "سماوي",
        'color_orange': "برتقالي",
        'color_gray': "رمادي",
        'color_custom': "اختيار لون",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&ملف",
        'menu_edit': "&تحرير",
        'menu_view': "&عرض",
        'menu_tools': "&أدوات",
        'menu_settings': "&إعدادات",
        'menu_help': "&مساعدة",
        'menu_language': "🌐 اللغة",
        'menu_guides': "&أدلة",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&فتح",
        'file_save_as': "&حفظ باسم...",
        'file_protect': "&حماية المستند...",
        'file_export': "&تصدير",
        'file_export_pages': "تصدير إلى Pages",
        'file_export_word': "تصدير إلى DOCX",
        'file_export_text': "تصدير إلى TXT",
        'file_print_now': "&طباعة فورية",
        'file_print': "&طباعة",
        'file_close': "&إغلاق",
        'file_quit': "&خروج",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&بحث",
        'edit_ocr': " إجراء OCR",
        'edit_rotate': "&تدوير الصفحة",
        'edit_rotate_all': "تدوير &جميع الصفحات",
        'edit_delete_pages': "&حذف الصفحات",
        'edit_extract_pages': "&استخراج الصفحات",
        'edit_insert_pages': "&إدراج صفحات",
        'edit_move_pages': "&نقل الصفحات",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " إدراج نصوص وعلامات",
        'text_insert': " إدراج نص",
        'cross_insert': " إدراج علامة",
        'text_customize': " تعديل النص",
        'cross_customize': " تعديل هذه العلامة",
        'cross_customize_all': " تعديل جميع العلامات",
        'text_discard': " تجاهل هذا النص/العلامة",
        'text_discard_all': " تجاهل جميع النصوص والعلامات",
        'text_save_all': " حفظ جميع النصوص والعلامات",
        'text_guide': " إدخال النص / كتل النص – دليل",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " إدراج توقيع",
        'signature_settings_menu': " إعدادات...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " إدراج صورة",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " إدراج أشكال",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&إظهار نافذة النص",
        'view_zoom': "&تكبير",
        'view_zoom_page': "&عرض الصفحة (افتراضي)",
        'view_zoom_two': "&صفحتان",
        'view_zoom_overview': "&نظرة عامة (عدة صفحات)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&إمكانية الوصول",
        'settings_voice': "الإخراج الصوتي",
        'settings_voice_tooltip': "يكمل الإخراج الصوتي لقارئات الشاشة بمعلومات إضافية",
        'settings_signature': "&إعدادات التوقيع",
        'settings_password': "&إدارة كلمات المرور",
        'settings_backup': "إنشاء نسخة احتياطية قبل التغييرات",
        'settings_export_import': "&تصدير الإعدادات / استيراد الإعدادات",
        'settings_export': "&تصدير جميع الإعدادات...",
        'settings_import': "&استيراد جميع الإعدادات...",
        'settings_export_info': "&ما الذي يتم تصديره؟",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "تشغيل",
        'voice_off': "إيقاف",
        'voice_toggle': "الإخراج الصوتي {0}",
        'voice_speed': "السرعة {0} بالمئة",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "الأداة غير موجودة:\n{0}\n\nBASE_DIR: {1}\nتأكد من تثبيت أدوات PDF في الدليل {1}.",
        'tool_started': "تم بدء {0}",
        'tool_start_failed': "تعذر البدء",
        'process_error_failed_to_start': "تعذر بدء العملية. هل الملف موجود؟",
        'process_error_crashed': "تعطلت العملية أثناء البدء.",
        'process_error_timeout': "انتهت مهلة العملية.",
        'process_error_write': "خطأ في الكتابة إلى العملية.",
        'process_error_read': "خطأ في القراءة من العملية.",
        'process_error_unknown': "خطأ غير معروف في العملية",
        'process_command': "الأمر",
        'process_normal_exit': "انتهى بشكل طبيعي",
        'process_crashed': "تعطل",
        'process_nonzero_exit': "انتهى {0} برمز خطأ {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "جاري الإلغاء...",
        'move_cancelling': "جاري إلغاء النقل",
        'opening_pdf': "جاري فتح PDF...",
        'loading_document': "جاري تحميل المستند...",
        'pdf_opened': "تم فتح PDF",
        'pages_found_moving': "تم العثور على {0} صفحات، {1} للنقل",
        'creating_backup': "جاري إنشاء نسخة احتياطية...",
        'backup_description': "جاري إنشاء نسخة احتياطية من الملف الأصلي...",
        'backup_saved_as': "تم حفظ النسخة الاحتياطية كـ: {0}",
        'error_format': "خطأ: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDF دارك فيو بواسطة BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "تم إعادة تعيين البحث",
        'page_header_simple': "=== الصفحة {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "إدارة كلمات المرور – دليل",
        'password_guide_voice': "دليل إدارة كلمات المرور. الرجاء قراءة الملاحظات.",
        'password_guide_html': """
        <html dir="rtl">
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 إدارة كلمات المرور – دليل مفصل</strong></p>

        <p><strong>1. حماية PDF بكلمة مرور</strong></p>
        <ul>
        <li>عند فتح PDF محمي بكلمة مرور، يظهر حوار حيث يمكنك إدخال كلمة المرور.</li>
        <li>يمكنك حفظ كلمة المرور بشكل مشفر حتى لا تضطر إلى إدخالها في كل مرة (مربع الاختيار "حفظ كلمة المرور").</li>
        <li>باستخدام زر "إزالة كلمة المرور"، يمكنك إنشاء نسخة مفكوكة التشفير من PDF وحذف كلمة المرور من قاعدة البيانات.</li>
        </ul>

        <p><strong>2. كلمة المرور الرئيسية</strong></p>
        <ul>
        <li>تحمي كلمة المرور الرئيسية الوصول إلى جميع كلمات مرور PDF المحفوظة.</li>
        <li><strong>الإعداد:</strong> انتقل إلى "الإعدادات ← إدارة كلمات المرور ← إعدادات كلمة المرور الرئيسية" وانقر على "إعداد كلمة المرور الرئيسية". اختر كلمة مرور قوية (8 أحرف على الأقل).</li>
        <li><strong>التغيير:</strong> بعد التوثيق الناجح، يمكنك تغيير كلمة المرور الرئيسية.</li>
        <li><strong>الإزالة:</strong> إذا قمت بحذف كلمة المرور الرئيسية، سيتم حذف جميع كلمات المرور المحفوظة بشكل نهائي. يمكنك تصدير نسخة احتياطية قبل ذلك.</li>
        <li>مرة واحدة في الجلسة، يجب عليك التوثيق بكلمة المرور الرئيسية للوصول إلى الوظائف المحمية (مثل عرض كلمات المرور).</li>
        </ul>

        <p><strong>3. إدارة كلمات المرور (قائمة)</strong></p>
        <ul>
        <li>في "الإعدادات ← إدارة كلمات المرور" تفتح جدولاً بجميع ملفات PDF المحفوظة وكلمات المرور المشفرة.</li>
        <li><strong>بدون كلمة مرور رئيسية:</strong> يمكنك فقط حذف الإدخالات – تظل كلمات المرور مخفية.</li>
        <li><strong>مع كلمة مرور رئيسية (موثقة):</strong> يمكنك عرض ونسخ وتصدير وحذف كلمات المرور.</li>
        <li><strong>التصدير:</strong> اختر تنسيقاً (JSON، CSV، TXT) واحفظ القائمة. إذا تم تعيين كلمة مرور رئيسية، يمكنك اختيار ما إذا كانت كلمات المرور تُصدَّر مفكوكة التشفير أو مشفرة.</li>
        <li><strong>الاستيراد:</strong> يمكن إعادة استيراد ملف ZIP مُصدَّر مسبقاً (جميع الإعدادات) عبر "الإعدادات ← تصدير الإعدادات / استيراد الإعدادات". تحذير: سيتم استبدال البيانات الموجودة!</li>
        </ul>

        <p><strong>4. مولد كلمات المرور</strong></p>
        <ul>
        <li>في حوار كلمة المرور (مثل حماية PDF)، على يمين حقل الإدخال يوجد زر نرد 🎲.</li>
        <li>انقر عليه لفتح مولد كلمات المرور. يمكنك ضبط الطول ومجموعات الأحرف (أحرف كبيرة، أحرف صغيرة، أرقام، رموز) وفاصل لتحسين القراءة.</li>
        <li>يمكن استخدام كلمة المرور المُنشأة مباشرة ونسخها إذا لزم الأمر.</li>
        </ul>

        <p><strong>5. ملاحظات أمان هامة</strong></p>
        <ul>
        <li>يتم تخزين كلمات المرور المحفوظة مشفرة باستخدام AES-256. يُشتق المفتاح من كلمة المرور الرئيسية (إذا تم تعيينها) أو من قيمة ثابتة (بدون كلمة مرور رئيسية).</li>
        <li>بدون كلمة مرور رئيسية، تكون كلمات المرور مشفرة ولكن المفتاح مدمج في البرنامج – يمكن للمهاجم الذي لديه إمكانية الوصول إلى ملفاتك فك تشفيرها. لذلك نوصي بشدة باستخدام كلمة مرور رئيسية.</li>
        <li>توجد قاعدة بيانات كلمات المرور في ملف `Data/passwords.json`. قم بعمل نسخ احتياطية بانتظام، خاصة قبل إزالة كلمة المرور الرئيسية.</li>
        <li>في حالة فقدان كلمة المرور الرئيسية، تُفقد جميع كلمات المرور المحفوظة بشكل نهائي.</li>
        </ul>
        </body>
        </html>
        """,


        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "وضع الانعكاس",
        'invert_mode_classic': "كلاسيكي (عكس كل الألوان)",
        'invert_mode_smart': "ذكي (عكس السطوع فقط)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "عتبة التدرج الرمادي",
        'gray_threshold_10': "10% (صارم)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (قياسي)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (ناعم)",
        'threshold_changed': "تم تعيين العتبة إلى {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "عتبة التدرج الرمادي – شرح",
        'threshold_guide_text': "تحدد عتبة التدرج الرمادي وحدات البكسل التي تعتبر 'رمادية' في الوضع المظلم الذكي ويتم عكسها.\n\n"
                                "• قيمة منخفضة (10%) تعكس فقط درجات الرماد شبه المثالية – تبقى العناصر الملونة محفوظة بالكامل.\n"
                                "• قيمة عالية (50%) تعكس أيضًا وحدات البكسل الملونة قليلاً – مما يزيد التباين، ولكنه قد يشوه الألوان.\n\n"
                                "تعتمد القيمة المثلى على المستند. بالنسبة لمستندات النص الخالص، غالبًا ما تكون 30-40% مثالية، وبالنسبة للرسومات الملونة، يفضل 10-20%.\n\n"
                                "يمكنك ضبط القيمة في أي وقت عبر قائمة 'الإعدادات' – سيتم إعادة تحميل ملف PDF على الفور.\n\n"
                                "ملاحظة:\n* لا يمكن عرض الصور والصور الفوتوغرافية بشكل صحيح إلا في الوضع الفاتح!\n* تظهر إعدادات الانعكاس فقط عند تنشيط الوضع المظلم.",
        'threshold_guide_voice': "تحدد عتبة التدرج الرمادي مدى تدخل الوضع المظلم الذكي. القيمة المنخفضة تحافظ على الألوان، والقيمة العالية تزيد التباين.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "جاري فتح PDF...",
        'progress_loading_document': "جاري تحميل المستند...",
        'progress_pdf_opened': "تم فتح PDF",
        'progress_creating_backup': "جاري إنشاء نسخة احتياطية...",
        'progress_backup_description': "جاري تأمين الملف الأصلي...",
        'progress_backup_created': "تم إنشاء النسخة الاحتياطية",
        'progress_backup_saved_as': "تم الحفظ باسم: {0}",
        'progress_analyzing_start': "بدء التحليل...",
        'progress_searching_empty': "البحث عن صفحات فارغة...",
        'progress_page_empty': "الصفحة {0} فارغة",
        'progress_page_keep': "الاحتفاظ بالصفحة {0}",
        'progress_analysis_complete': "اكتمل التحليل",
        'progress_empty_found': "تم العثور على {0} صفحة فارغة",
        'progress_current_page': "الصفحة الحالية",
        'progress_mark_delete': "تم وضع علامة للحذف",
        'progress_range_selected': "نطاق الصفحات {0}-{1}",
        'progress_deleting_pages': "جاري حذف {0} صفحات",
        'progress_creating_new_pdf': "جاري إنشاء PDF جديد...",
        'progress_transferring_pages': "جاري نقل الصفحات",
        'progress_keeping_page': "سيتم الاحتفاظ بالصفحة {0} ({1}/{2})",
        'progress_saving_pdf': "جاري حفظ PDF...",
        'progress_optimizing': "جاري تحسين حجم الملف...",
        'progress_finalizing': "جاري الإنهاء...",
        'progress_new_size': "الحجم الجديد: {0:.2f} ميجابايت",
        'progress_cancelling': "جاري الإلغاء...",
        'progress_cancel_message': "جاري إلغاء {0}",
        'progress_pages_found_moving': "تم العثور على {0} صفحة، {1} لنقلها",

        # OCR-Fortschritt
        'ocr_status_analyzing': "جاري تحليل PDF...",
        'ocr_status_optimizing': "جاري تحسين الصورة...",
        'ocr_status_recognizing': "جاري التعرف على النص...",
        'ocr_status_embedding': "جاري تضمين النص...",
        'ocr_status_finalizing': "جاري إنهاء PDF...",

        # PDF-Laden
        'progress_preparing': "جاري التحضير...",
        'progress_loading': "جاري تحميل PDF...",

        # Seitenoperationen
        'progress_deleting_title': "جاري حذف الصفحات...",
        'progress_moving_title': "جاري نقل الصفحات...",
        'pages_found': "تم العثور على صفحات",
        'progress_creating_new_order': "جاري إنشاء ترتيب جديد...",
        'progress_sorting_pages': "جاري ترتيب الصفحات...",
        'progress_moving_to_begin': "نقل {0} صفحات إلى البداية",
        'progress_transferring_count': "نقل {0} صفحات",
        'progress_transferring_before_target': "نقل الصفحات قبل الهدف",
        'progress_moving_pages': "نقل {0} صفحات",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_نسخة_احتياطية_",
        'filename_protected_suffix': "_محمي_",
        'filename_copy_suffix': "_نسخة",
        'filename_page_single': "_صفحة_",
        'filename_page_range': "_صفحات_",
        'filename_export_page': "_صفحة_{0:03}",
        'filename_export_range': "_صفحات_{0}-{1}",
        'filename_export_multiple': "_صفحات_{0}",
        'filename_with_text': "_مع_نص",
        'filename_with_signature': "_مع_توقيع",
        'filename_with_image': "_مع_صورة",
        'filename_with_forms': "_مع_أشكال",
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
        'view_toggle_navbar': "إظهار شريط الأزرار",
		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "لا يمكن حذف جميع الصفحات",
		'pages_cannot_delete_last_page': 'لا يمكن حذف الصفحة الأخيرة!',
		'pages_cannot_delete_all_pages': 'يجب أن تبقى صفحة واحدة على الأقل في المستند!',
		'delete_pages_confirm': 'هل أنت متأكد من حذف {0} صفحة؟',
		'delete_pages_confirm_voice': 'هل أنت متأكد من حذف {0} صفحة؟',
		'pages_deleted': 'تم حذف {0} صفحة بنجاح.',
		'warning': 'تحذير',
		'error': 'خطأ',



        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "لم يتم اختيار نموذج",
        'form_customized': "تم تخصيص النموذج",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "اختر",
        'btn_use': "استخدم",
        'master_password_for_spasswords': "لتخزين واستخدام كلمات المرور، يجب أولاً إعداد كلمة مرور رئيسية.\n\nهل تريد إعداد كلمة المرور الرئيسية الآن؟",
        'open_saved_dialog_title': "فتح ملف محفوظ",
        'open_saved_question': "هل تريد فتح الملف المحفوظ الآن؟",
        'password': "كلمة المرور",
        'password_manager_master_required': "مدير كلمات المرور متوفر فقط عند إعداد كلمة مرور رئيسية.\n\nهل تريد إعداد كلمة المرور الرئيسية الآن؟",
        'password_master_required_for_select': "لعرض واختيار كلمات المرور المحفوظة، يجب عليك أولاً المصادقة باستخدام كلمة المرور الرئيسية الخاصة بك.\n\nهل تريد المصادقة الآن؟",
        'password_not_available': "كلمة المرور المحددة غير متوفرة أو لم يتم فك تشفيرها.",
        'password_options_title': "خيارات كلمة المرور",
        'password_save_choice_change': "تعيين كلمة مرور جديدة",
        'password_save_choice_keep': "استخدام كلمة المرور الحالية",
        'password_save_choice_none': "حفظ بدون تشفير",
        'password_save_hint': "قم أولاً بإعداد كلمة مرور رئيسية لحفظ كلمات المرور بشكل آمن.",
        'password_save_master_required': "حفظ كلمة المرور (متوفر فقط مع كلمة مرور رئيسية)",
        'password_save_question': "ملف PDF الحالي محمي بكلمة مرور. هل تريد استخدام كلمة المرور الحالية، تعيين كلمة مرور جديدة أم حفظ بدون تشفير؟",
        'password_select': "اختر كلمة المرور",
        'password_select_none': "لم يتم اختيار أي كلمة مرور.\n\nالرجاء اختيار كلمة مرور من القائمة.",
        'password_select_one': "الرجاء اختيار كلمة مرور واحدة بالضبط.\n\nلقد حددت عدة كلمات مرور.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_نسخة_احتياطية",
        'filename_insert_suffix': "_مع_إدراج",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_تم_حذف_الصفحات",
        'filename_pages_moved': "_تم_نقل_الصفحات",
        'filename_rotated_all_suffix': "_تم_تدوير_كل_الصفحات",
        'filename_rotated_suffix': "_تم_تدوير_الصفحة",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "تكوين أسماء الملفات عند تغيير PDF",
        'filename_keep_suffixes': "الاحتفاظ باللواحق السابقة (مثل _مع_نص)",
        'filename_keep_suffixes_false': "استبدال",
        'filename_keep_suffixes_true': "الاحتفاظ",
        'filename_preview_label': "معاينة اسم الملف:",
        'filename_preview_overwrite_hint': "المعاينة غير متوفرة – سيتم استبدال الأصل.",
        'filename_separator': "فاصل بين الكلمات",
        'filename_separator_none': "بدون فاصل",
        'filename_separator_space': "مسافة ( )",
        'filename_separator_underscore': "شرطة سفلية (_)",
        'filename_settings_saved': "تم حفظ إعدادات اسم الملف",
        'filename_settings_title': "تنسيق اسم الملف والنسخ الاحتياطي",
        'filename_timestamp_position': "موقع الطابع الزمني",
        'filename_timestamp_position_after': "بعد الاسم الأساسي",
        'filename_timestamp_position_before': "في البداية",
        'filename_timestamp_position_end': "في النهاية",
        'filename_use_timestamp': "استخدام طابع زمني",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>السلوك عند التغييرات:</b><ul><li>حذف وإدراج الصفحات</li><li>إدراج نص وتوقيع وصورة وأشكال</li><li>OCR</li></ul></html>",
        'backup_section': "نسخ احتياطي لعمليات الصفحات (حذف، نقل)",
        'behavior_info': "ملاحظة: عند 'استبدال الأصل'، يتم تجاهل الطوابع الزمنية واللواحق – يحتفظ الملف باسمه.",
        'behavior_new_file': "إنشاء ملف جديد دائمًا (مع طابع زمني ولاحقة)",
        'behavior_overwrite': "استبدال الأصل (لا ملف جديد)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "تم تدوير جميع الصفحات.\n\nبقي الأصل دون تغيير.\nالملف الجديد: {0}",
        'all_pages_rotated_voice': "تم تدوير جميع الصفحات، تم إنشاء ملف جديد.",
        'empty_pages_deleted_new_file': "تم حذف {0} صفحة فارغة.\n\nبقي الأصل دون تغيير.\nالملف الجديد: {1}",
        'empty_pages_deleted_voice': "تم حذف {0} صفحة فارغة، تم إنشاء ملف جديد.",
        'ocr_keep_original': "الاحتفاظ بالأصل (فتح يدويًا لاحقًا)",
        'ocr_new_file_question': "تم حفظ ملف PDF الجديد القابل للبحث في:\n{0}\n\nهل تريد فتحه الآن؟",
        'ocr_open_new': "فتح ملف OCR الجديد",
        'ocr_original_kept': "يبقى الملف الأصلي مفتوحًا. تم حفظ ملف OCR.",
        'page_deleted_new_file': "تم حذف الصفحة {0}.\n\nبقي الأصل دون تغيير.\nالملف الجديد: {1}",
        'page_deleted_voice': "تم حذف الصفحة {0}، تم إنشاء ملف جديد.",
        'page_rotated_new_file': "تم تدوير الصفحة {0}.\n\nبقي الأصل دون تغيير.\nالملف الجديد: {1}",
        'page_rotated_voice': "تم تدوير الصفحة {0}، تم إنشاء ملف جديد.",
        'pages_deleted_new_file': "تم حذف {0} صفحة.\n\nبقي الملف الأصلي دون تغيير.\nالملف الجديد: {1}",
        'pages_deleted_new_file_voice': "تم حذف {0} صفحة، تم إنشاء ملف جديد.",
        'pages_inserted_new_file': "تم إدراج {0} صفحة.\n\nبقي الملف الأصلي دون تغيير.\nالملف الجديد: {1}",
        'pages_inserted_new_file_ask': "تم إدراج {0} صفحة.\n\nبقي الأصل دون تغيير.\nالملف الجديد: {1}\n\nهل تريد فتحه الآن؟",
        'pages_inserted_voice_new': "تم إدراج {0} صفحة، تم إنشاء ملف جديد.",
        'pages_moved_new_file': "تم نقل {0} صفحة.\n\nبقي الملف الأصلي دون تغيير.\nالملف الجديد: {1}",
        'pages_moved_new_file_voice': "تم نقل {0} صفحة، تم إنشاء ملف جديد.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "عدم الإظهار مرة أخرى",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 إعداد النسخ الاحتياطي</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ النسخ الاحتياطي تشغيل</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">عند جميع التغييرات التي تستبدل الأصل</strong> (نص، توقيع، صورة، شكل، OCR، تدوير، إدراج، حذف/نقل الصفحات) يتم <strong>إنشاء نسخة احتياطية تلقائية بطابع زمني</strong> قبل تطبيق التغيير.</p>
                <p style="margin: 5px 0 5px 20px;">• توجد النسخة الاحتياطية بجوار الملف الأصلي (مثال: <code>Dokument_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• إذا قمت أيضًا بتنشيط الخيار <strong>„استبدال الأصل“</strong>، يتم أيضًا إنشاء نسخة احتياطية.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 النسخ الاحتياطي إيقاف</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>لا يتم إنشاء نسخة احتياطية</strong> – لا عند الاستبدال ولا عند عمليات الصفحات.</p>
                <p style="margin: 5px 0 5px 20px;">• يمكن فقدان الملف الأصلي بشكل لا رجعة فيه عند الاستبدال.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">موصى به فقط للمستخدمين ذوي الخبرة!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>تلميح:</strong> إعداد النسخ الاحتياطي مستقل عن خيار "استبدال الأصل". يمكنك الجمع بينهما.<br>
                يمكنك إخفاء هذه الرسالة بشكل دائم.
            </div>
        </div>
        """,
        'backup_info_title': "سلوك النسخ الاحتياطي",
        'backup_info_voice': "إشعار حول سلوك النسخ الاحتياطي في عمليات الصفحات. النسخ الاحتياطي تشغيل يستبدل الأصل، النسخ الاحتياطي إيقاف ينشئ ملفًا جديدًا.",
        'show_backup_info': "معلومات حول إعداد النسخ الاحتياطي",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "عدم الإظهار مرة أخرى",
        'overwrite_enable_backup': "تفعيل النسخ الاحتياطي (موصى به)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ استبدال الأصل</p>
            <p>عند تفعيل هذا الخيار، يتم حفظ التغييرات (نص، توقيع، صورة، شكل، OCR، تدوير، إدراج) <strong>مباشرة في الأصل</strong> – <strong>لا يتم إنشاء ملف جديد</strong>.</p>
            <p>• يبقى اسم الملف دون تغيير.<br>
            • يتم تجاهل الطوابع الزمنية واللواحق.<br>
            • <strong>بدون نسخ احتياطي، يمكن فقدان الأصل بشكل لا رجعة فيه.</strong></p>
            <p style="color: #FFD700;">توصية: قم بتفعيل خيار النسخ الاحتياطي بالإضافة إلى ذلك للحصول على نسخ أمان تلقائية.</p>
        </div>
        """,
        'overwrite_info_title': "استبدال الأصل",
        'overwrite_info_voice': "تحذير: استبدال الأصل – لا ملف جديد. يوصى بالنسخ الاحتياطي.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "تم إدراج {0} صفحة.\n\nتم استبدال الملف الأصلي.\nتم إنشاء نسخة احتياطية.",
        'pages_inserted_overwrite_no_backup': "تم إدراج {0} صفحة.\n\nتم استبدال الملف الأصلي.\nلم يتم إنشاء نسخة احتياطية.",
        'texts_saved_overwrite_with_backup': "تم حفظ التغييرات في الأصل.\n\nتم إنشاء نسخة احتياطية.",
        'texts_saved_overwrite_no_backup': "تم حفظ التغييرات في الأصل.\n\nلم يتم إنشاء نسخة احتياطية.",
        'texts_crosses_saved_new_file': "تم إدراج {0} {1} و {2} {3}.\n\nبقي الملف الأصلي دون تغيير.\nتم إنشاء ملف جديد.\n\nيتم تحميل ملف PDF الجديد...",
        'texts_saved_new_file': "تم إدراج {0} {1}.\n\nبقي الملف الأصلي دون تغيير.\nتم إنشاء ملف جديد.\n\nيتم تحميل ملف PDF الجديد...",
        'crosses_saved_new_file': "تم إدراج {0} {1}.\n\nبقي الملف الأصلي دون تغيير.\nتم إنشاء ملف جديد.\n\nيتم تحميل ملف PDF الجديد...",
        'elements_saved_new_file': "تم إدراج {0} عنصر.\n\nبقي الملف الأصلي دون تغيير.\nتم إنشاء ملف جديد.\n\nيتم تحميل ملف PDF الجديد...",
        'signatures_saved_overwrite_with_backup': "تم حفظ التوقيع (التوقيعات) في الأصل.\n\nتم إنشاء نسخة احتياطية.",
        'signatures_saved_overwrite_no_backup': "تم حفظ التوقيع (التوقيعات) في الأصل.\n\nلم يتم إنشاء نسخة احتياطية.",
        'images_saved_overwrite_with_backup': "تم حفظ الصورة (الصور) في الأصل.\n\nتم إنشاء نسخة احتياطية.",
        'images_saved_overwrite_no_backup': "تم حفظ الصورة (الصور) في الأصل.\n\nلم يتم إنشاء نسخة احتياطية.",
        'forms_saved_overwrite_with_backup': "تم حفظ الشكل (الأشكال) في الأصل.\n\nتم إنشاء نسخة احتياطية.",
        'forms_saved_overwrite_no_backup': "تم حفظ الشكل (الأشكال) في الأصل.\n\nلم يتم إنشاء نسخة احتياطية.",
        'signatures_saved_new_file': "تم إدراج {0} توقيع.\n\nبقي الملف الأصلي دون تغيير.\nتم إنشاء ملف جديد.\n\nيتم تحميل ملف PDF الجديد...",
        'images_saved_new_file': "تم إدراج {0} صورة.\n\nبقي الملف الأصلي دون تغيير.\nتم إنشاء ملف جديد.\n\nيتم تحميل ملف PDF الجديد...",
        'forms_saved_new_file': "تم إدراج {0} شكل.\n\nبقي الملف الأصلي دون تغيير.\nتم إنشاء ملف جديد.\n\nيتم تحميل ملف PDF الجديد...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "تحذير: يحتوي ملف PDF هذا على صفحات مدورة. قد يختلف تحديد المواقع.",
        'page_rotated_warning_title': "تم اكتشاف صفحة مدورة",
        'page_rotated_warning_message': "الصفحة الحالية {0} مدورة بمقدار {1}°.\n\nلا يدعم إدراج العناصر على الصفحات المدورة.\n\nهل تريد تدوير الصفحة الآن إلى الوضع المستقيم؟",
        'page_rotated_warning_voice': "تحذير: الصفحة مدورة. الرجاء تدويرها أولاً.",
        'paste_on_rotated_page_simple_warning': "لا يمكن الإدراج في الصفحة {0}!\n\nهذه الصفحة مدورة بمقدار {1}°.\n\nالرجاء تدوير الصفحة أولاً إلى 0° (القائمة: تحرير → محاذاة الصفحة).\n\nتحذير:\nسيتم فقدان العنصر المنسوخ مسبقًا إذا لم تقم بالحفظ قبل تدوير الصفحة.",
        'paste_on_rotated_page_voice': "تم إلغاء الإدراج. الصفحة مدورة. الرجاء محاذاة الصفحة أولاً.",
        'page_rotated_cancel': "إلغاء",
        'page_rotated_rotate_until_upright': "تدوير الصفحة بشكل متكرر (حتى تستقيم)",
        'page_rotated_now_upright': "الصفحة الآن مستقيمة. يمكنك الآن الإدراج.",
        'page_rotated_still_not_upright': "لم يتمكن من تدوير الصفحة إلى الوضع المستقيم. الرجاء التصحيح يدويًا.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "مساعدة: تصحيح الصفحات المدورة",
        'help_rotated_pages_voice': "سيتم فتح مساعدة تصحيح الصفحات المدورة.",
        'btn_help': "مساعدة",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 مشكلة: صفحة مدورة – الإدراج لا يعمل بشكل صحيح</p>

            <p>إذا كان إدراج النصوص أو التوقيعات أو الأشكال على صفحة مدورة لا يعمل بشكل صحيح، يمكنك تصحيح الصفحة باستخدام محرر PDF خارجي.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ الحل باستخدام أداة خارجية (مثال: معاينة macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>تصدير الصفحة</strong><br>
                &nbsp;&nbsp;انقر في القائمة على <strong>ملف → تصدير كصفحات</strong> أو استخدم طريقة أخرى لحفظ الصفحة المطلوبة كملف PDF منفرد.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>فتح الصفحة في برنامج خارجي</strong><br>
                &nbsp;&nbsp;افتح ملف PDF المُصدَّر في محرر PDF (مثال: <strong>معاينة macOS</strong>، Adobe Acrobat، PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>تدوير الصفحة</strong><br>
                &nbsp;&nbsp;قم بتدوير الصفحة بحيث تكون مستقيمة (في المعاينة: <strong>أدوات → تدوير</strong> أو <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>حفظ</strong><br>
                &nbsp;&nbsp;احفظ الصفحة المصححة (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>إعادة إدراج الصفحة في المستند الأصلي</strong><br>
                &nbsp;&nbsp;عد إلى PDFDarkView وأدرج الصفحة المصححة في الموضع المطلوب:<br>
                &nbsp;&nbsp;<strong>تحرير → إدراج صفحات</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 بديل: تدوير الصفحة في الأصل</p>
                <p style="margin: 5px 0 5px 20px;">• استخدم وظيفة التدوير المدمجة (<strong>تحرير → تدوير الصفحة</strong>) لتصحيح الصفحة تدريجيًا.<br>
                • بعد كل تدوير، يمكنك التحقق مما إذا كان الإدراج يعمل الآن.<br>
                • هذا غالبًا ما يكون الحل الأسرع – جربه أولاً!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>تلميح:</strong> إذا واجهت صفحات مدورة بشكل متكرر، يمكنك إخفاء التحذير في حوار الإدراج بشكل دائم.<br>
                قد يختلف تحديد المواقع بعد ذلك – استخدم هذا الخيار فقط إذا كنت تعرف العواقب.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "محاذاة الصفحات",
        'menu_rotate_normalize_tooltip': "تدوير الصفحة أو إعادة تعيينها إلى 0°",
        'normalize_current_page': "جلب الصفحة الحالية إلى الوضع المستقيم (ضبط على 0°)",
        'normalize_all_pages': "جلب جميع الصفحات إلى الوضع المستقيم (ضبط على 0°)",
        'page_normalized': "تم ضبط الصفحة {0} على الوضع المستقيم.",
        'all_pages_normalized': "تم ضبط جميع الصفحات على الوضع المستقيم.",
        'page_already_upright': "الصفحة {0} مستقيمة بالفعل.",
        'all_pages_already_upright': "جميع الصفحات مستقيمة بالفعل.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>لا يحتوي ملف PDF على نص قابل للبحث.</p><p>هل تريد إجراء OCR للتصدير إلى {0}؟</p>",
        'export_ocr_voice': "لا يحتوي ملف PDF على نص. OCR مطلوب للتصدير إلى {0}.",
        'export_no_ocr_possible': "التصدير بدون OCR غير ممكن. الرجاء إجراء OCR عبر القائمة.",
        'ocr_failed_export_not_possible': "فشل OCR. لا يمكن إجراء التصدير.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "سيتم فتح PDF في المعاينة. الرجاء بدء عملية الطباعة هناك.",
        'print_preview_manual': "تم فتح PDF. الرجاء تنفيذ أمر الطباعة يدويًا (مثال: Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "دمج PDF",
        'merge_pdfs': "دمج PDF",
        'merge_progress_title': "جاري دمج PDF...",
        'merge_pdfs_list': "PDF بالترتيب (اسحب وأفلت للترتيب)",
        'merge_add_pdf': "إضافة PDF",
        'merge_remove': "إزالة",
        'merge_move_up': "أعلى",
        'merge_move_down': "أسفل",
        'merge_pdfs_info': "💡 تلميح: يمكنك تغيير الترتيب عن طريق السحب والإفلات",
        'merge_no_pdfs': "لم يتم تحديد أي PDF. انقر على 'إضافة PDF'.",
        'merge_info': "تم تحديد {0} PDF (تقريبًا {1} صفحة)",
        'merge_open_file': "فتح ملف",
        'merge_merge': "دمج",
        'merge_error': "خطأ أثناء الدمج",
        'merge_min_two_pdfs_error': "الرجاء تحديد ملفي PDF على الأقل للدمج.",
        'merge_select_pdfs': "تحديد PDF للدمج",
        'merge_error_file': "خطأ في المعالجة",
        'merge_cancelled': "تم إلغاء الدمج",
        'merge_preparing': "جاري التحضير...",
        'merge_processing': "معالجة PDF {0} من {1}",
        'merge_saving': "جاري حفظ PDF المدمج...",
        'merge_complete': "اكتمل!",
        'merge_success_title': "تم الدمج بنجاح",
        'merge_success_voice': "تم دمج {0} PDF بنجاح.",
        'merge_success_message': "تم دمج {0} PDF بنجاح.\n\nيحتوي المستند الجديد الآن على {1} صفحة.\n\nالملف الجديد:\n{2}\n\nموقع الحفظ:\n{3}\n{2}\n\nهل تريد فتح ملف PDF هذا؟",
        'replace_file_title': "استبدال الملف؟",
        'replace_file_message': "يوجد PDF مفتوح بالفعل. هل تريد استبداله بالملف الجديد؟",
        'btn_yes': "نعم",
        'btn_no': "لا",
        'filename_merge_suffix': "مدمج",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "جاري فتح {0}...",
        'progress_merge_reading': "جاري قراءة {0}...",
        'progress_merge_adding': "جاري إضافة {0} صفحة...",
        'progress_merge_optimizing': "جاري تحسين PDF...",
        'progress_merge_writing': "جاري كتابة PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "إغلاق PDF",
        'action_close_window': "إغلاق النافذة",
        'action_open_new_pdf': "فتح PDF جديد",
        'action_quit_app': "إنهاء التطبيق",
        'changes_saved': "تم حفظ التغييرات.",
        'file_close_title': "إغلاق ملف PDF",
        'save_before_action': "هل تريد حفظ التغييرات قبل {0}؟ نعم أو لا؟",
        'save_before_action_voice': "هل تريد حفظ التغييرات قبل {0}؟ نعم أو لا؟",
        'save_before_close_question': "هل تريد حفظ التغييرات قبل الإغلاق؟ نعم أو لا؟",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>تم إنشاء PDF قابل للبحث:\n\n{0}\n\n<b>حاول مرة أخرى إذا لزم الأمر",
        "ocr_rotate_title": "محاذاة الصفحات قبل OCR",
        "ocr_rotate_question": "يحتوي PDF على صفحات ملتفة.\nهل تريد محاذاة جميع الصفحات إلى 0° قبل OCR؟\nهذا يحسن التعرف على النص بشكل كبير.",
        "ocr_rotate_yes": "نعم، محاذاة",
        "ocr_rotate_no": "لا، بدء OCR مباشرة",
        "ocr_rotate_voice": "يحتوي PDF على صفحات ملتفة. هل يجب محاذاة جميع الصفحات قبل OCR؟",
        "ocr_not_performed_message": "لا يوجد نص. الرجاء إجراء OCR (القائمة \"تحرير\" → \"إجراء OCR\" أو مفتاح Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "إعدادات OCR",
        "ocr_language_btn": "اختر لغة OCR",
        "ocr_language": "لغة(ات) OCR",
        "ocr_language_current": "اللغة الحالية:",
        "ocr_param_info": "معلومات حول المعامل",

        "ocr_force_ocr_label": "فرض OCR",
        "ocr_deskew_label": "تصحيح الانحراف",
        "ocr_clean_label": "تنظيف الصورة",
        "ocr_oversample_label": "الدقة (DPI)",
        "ocr_pagesegmode_label": "تقسيم الصفحة",
        "ocr_oem_label": "وضع محرك OCR",
        "ocr_optimize_label": "ضغط PDF",
        "ocr_jobs_label": "العمليات المتوازية",
        "ocr_verbose_label": "تفصيل السجل",

        "ocr_force_ocr_tooltip": "فرض OCR على كل صفحة، حتى إذا كان النص موجودًا بالفعل",
        "ocr_deskew_tooltip": "محاذاة الممسوحات الضوئية المائلة تلقائيًا",
        "ocr_clean_tooltip": "إزالة الضوضاء والقطع الأثرية من الصورة",
        "ocr_oversample_tooltip": "تكبير الصورة قبل OCR إلىDPI هذه",
        "ocr_pagesegmode_tooltip": "يحدد كيفية تقسيم الصفحة إلى مناطق نصية",
        "ocr_oem_tooltip": "يختار محرك OCR من Tesseract",
        "ocr_optimize_tooltip": "مستوى ضغط PDF الناتج",
        "ocr_jobs_tooltip": "عدد عمليات OCR المتوازية",
        "ocr_verbose_tooltip": "مستوى تفصيل مخرجات السجل",
        "ocr_settings_explain_btn": "شرح",

        "ocr_force_ocr_explain": "يفرض التعرف على النص في <b>كل</b> صفحة، حتى إذا كانت تحتوي بالفعل على نص.\n\nتوصية: <b>تشغيل</b> لملفات PDF الممسوحة ضوئيًا، <b>إيقاف</b> لملفات PDF الأصلية التي تحتوي بالفعل على نص.",

        "ocr_deskew_explain": "يصحيح المسوحات الضوئية المائلة قليلاً (حتى 5 درجات تقريبًا).\n\nتوصية: <b>تشغيل</b> للمستندات الممسوحة ضوئيًا، <b>إيقاف</b> إذا كانت الصفحات مستقيمة تمامًا بالفعل.",

        "ocr_clean_explain": "يزيل الضوضاء والنقاط والقطع الأثرية الصغيرة من الصورة.\n<b>هام:</b> للنصوص العربية أو التايلاندية أو الفيتنامية التي تحتوي على علامات تشكيل (نقاط أعلى/أسفل الحروف) يجب <b>تعطيل</b> هذا الخيار، وإلا فقد يتم فقدان أحرف مهمة.",

        "ocr_oversample_explain": "يكبر الصورة <b>قبل</b> التعرف على النص إلىDPI المحددة.<br><br>• <b>72-150 نقطة في البوصة:</b> سريع جدًا، ولكن معدل تعرف منخفض<br>• <b>200-300 نقطة في البوصة:</b> النطاق الأمثل (القياسي: 300)<br>• <b>400+ نقطة في البوصة:</b> تحسن طفيف في التعرف، ولكن ملفات أكبر بكثير<br><br>توصية: 300 نقطة في البوصة للخطوط المعقدة (العربية، الصينية، اليابانية)، 200 نقطة في البوصة للغات الغربية.",

        "ocr_pagesegmode_explain": "يحدد كيفية تقسيم Tesseract للصفحة إلى مناطق نصية.\n\n• <b>3 - تلقائي (قياسي):</b> جيد للتخطيطات المختلطة\n• <b>4 - عمود واحد:</b> للنصوص ذات العمود الواحد\n• <b>5 - كتلة عمودية:</b> للكتابات العمودية (اليابانية، الصينية)\n• <b>6 - كتلة نصية موحدة:</b> مثالي للنص المتدفق بدون أعمدة\n• <b>11 - صورة خام:</b> للمسوحات الضوئية الرديئة / الكتابة اليدوية\n\nتوصية: <b>6</b> للمستندات النصية البسيطة، <b>3</b> للتخطيطات المعقدة.",

        "ocr_oem_explain": "يختار محرك OCR من Tesseract.\n\n• <b>0 - Legacy:</b> محرك قديم (سريع، لكن أقل دقة)\n• <b>1 - LSTM:</b> محرك عصبي (أبطأ، لكن أكثر دقة)\n• <b>2 - Legacy + LSTM:</b> يجمع بين النتائج\n• <b>3 - قياسي (LSTM مفضل):</b> أفضل خيار لمعظم الحالات\n\nتوصية: <b>3</b> لأقصى دقة تعرف.",

        "ocr_optimize_explain": "يضغط PDF الناتج.\n\n• <b>0:</b> بدون تحسين (أسرع معالجة)\n• <b>1:</b> تحسين خفيف (حل وسط جيد)\n• <b>2:</b> تحسين معتدل\n• <b>3:</b> تحسين قوي (أصغر ملف، لكن أبطأ)\n\nتوصية: <b>1</b> للاستخدام اليومي.",

        "ocr_jobs_explain": "عدد العمليات المتوازية لـ OCR.\n\n• <b>1:</b> بطيء، لكن أقل استهلاك للذاكرة\n• <b>4-8:</b> مثالي للمعماريات متعددة النوى الحديثة\n• <b>12+:</b> معالجة أسرع قليلاً مع استهلاك عالي للذاكرة\n\nتوصية: عدد نوى المعالج (مثل <b>4</b> على أنظمة 4 نوى).",

        "ocr_verbose_explain": "مستوى تفصيل مخرجات السجل في وحدة التحكم.\n\n• <b>0:</b> بدون مخرجات\n• <b>1:</b> تقدم ورسائل الحالة\n• <b>2:</b> مخرجات مفصلة\n• <b>3:</b> مخرجات تصحيح أخطاء كاملة (شاملة جدًا)\n\nتوصية: <b>1</b> للتشغيل العادي.",

        "ocr_reset_title": "تمت إعادة تعيين الإعدادات",
        "ocr_reset_message": "تمت إعادة تعيين جميع إعدادات OCR إلى القيم الافتراضية.",
        "info_tooltip": "مزيد من المعلومات حول هذا المعامل",
        "ocr_reset_defaults": "إعادة تعيين إلى الافتراضي",

        "ocr_psm_0": "تلقائي (محرك Legacy)",
        "ocr_psm_1": "كشف الأعمدة تلقائيًا",
        "ocr_psm_3": "تلقائي (قياسي)",
        "ocr_psm_4": "عمود واحد",
        "ocr_psm_5": "كتلة عمودية",
        "ocr_psm_6": "كتلة نصية موحدة",
        "ocr_psm_7": "سطر نص واحد",
        "ocr_psm_8": "كلمة واحدة",
        "ocr_psm_11": "صورة خام (بدون تحليل تخطيط)",

        "ocr_oem_0": "محرك Legacy (سريع)",
        "ocr_oem_1": "محرك LSTM (عصبي، دقيق)",
        "ocr_oem_2": "Legacy + LSTM مدمجان",
        "ocr_oem_3": "قياسي (LSTM مفضل)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "لغة(ات) OCR...",
        "ocr_language_title": "اختر لغة(ات) OCR",
        "ocr_language_instruction": "اختر اللغة(ات) للتعرف على النص (OCR).\nتنبيه: اللغات المتعددة تؤثر سلبًا على الأداء والدقة!\nتحصل على أفضل النتائج عند اختيار لغة واحدة فقط.",
        "ocr_language_predefined": "مجموعات محددة مسبقًا",
        "ocr_language_custom": "مخصص...",
        "ocr_language_selected": "لغات OCR المختارة",
        "ocr_language_changed": "تم تغيير لغة OCR إلى {0}",
        "ocr_language_auto_detect": "يتم اكتشاف اللغات المتاحة تلقائيًا.",
        "ocr_language_none_found": "لم يتم العثور على بيانات لغات Tesseract! الرجاء تثبيت حزم اللغة (مثل 'tesseract-ocr-deu'، 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "اختيار لغة مخصص",
        "ocr_language_available": "اللغات المتاحة (المثبتة):",
        "ocr_language_select_hint": "اختر لغة أو أكثر:",
        "ocr_language_confirm": "تطبيق",
        "ocr_language_reset": "إعادة تعيين إلى الافتراضي (deu+eng+vie)",
        "ocr_language_priorities": "اللغات الموصى بها (مثبتة مسبقًا):",

        "select_all_languages": "تحديد الكل",
        "clear_all_languages": "إلغاء التحديد",
        "install_language_packs": "تثبيت حزم اللغة المفقودة...",
        "install_hint": "💡 تلميح: ليست كل اللغات مثبتة على نظامك. من هذا الزر يمكنك الحصول على مساعدة للتثبيت.",
        "ocr_language_install_title": "تثبيت حزم لغات Tesseract",

        "ocr_missing_languages": "حزم لغات OCR مفقودة",
        "ocr_missing_languages_message": "اللغات التالية المحددة غير مثبتة على نظامك:\n\n{0}\n\nالرجاء تثبيت حزم اللغة المفقودة (انظر المساعدة في 'مساعدة التثبيت').\n\nهل تريد فتح مساعدة التثبيت الآن؟",
        "ocr_missing_languages_voice": "حزم لغات مفقودة. الرجاء تثبيت اللغات المفقودة.",
        "ocr_install_help_now": "فتح المساعدة",
        "ocr_continue_anyway": "المحاولة على أي حال",
        "ocr_language_error_title": "خطأ في لغة OCR",
        "ocr_language_error_message": "خطأ في التعرف على النص: {0}\n\nالرجاء التحقق من إعدادات لغة OCR (الإعدادات → لغة OCR).",
        "ocr_install_help_button": "مساعدة التثبيت",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 تثبيت حزم لغات Tesseract</p>

        <p>لكي يعمل OCR بلغة معينة، يجب أن تكون بيانات اللغة المقابلة مثبتة على نظامك. اتبع التعليمات لنظام التشغيل الخاص بك:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>افتح <strong>Terminal</strong> (Finder → البرامج → الأدوات المساعدة → Terminal).</li>
        <li>قم بتثبيت جميع اللغات المتاحة باستخدام:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (قد يستغرق ذلك بضع دقائق.)</li>
        <li>أو فقط لغات فردية (مثل الفيتنامية):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        في إصدارات Homebrew الحالية، قد يلزم تنزيل <code>*.traineddata</code> يدويًا (انظر أدناه).</li>
        <li>بعد التثبيت: أغلق هذا الحوار وافتح اختيار لغة OCR مرة أخرى – ستظهر اللغات الجديدة تلقائيًا.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>افتح الطرفية (Ctrl+Alt+T).</li>
        <li>قم بتثبيت اللغة المطلوبة، مثلاً للفيتنامية:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        رموز اللغة الهامة: <code>deu</code> (ألمانية)، <code>eng</code> (إنجليزية)، <code>vie</code> (فيتنامية)، <code>spa</code> (إسبانية)، <code>fra</code> (فرنسية)، <code>ita</code> (إيطالية)، <code>nld</code> (هولندية)، <code>fin</code> (فنلندية)، <code>swe</code> (سويدية)، <code>nor</code> (نرويجية).</li>
        <li>عرض جميع الحزم المتاحة:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (يدوي)</p>
        <ol>
        <li>قم بتنزيل ملفات <code>*.traineddata</code> المطلوبة من:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (مثل <code>vie.traineddata</code> للفيتنامية).</li>
        <li>انسخ الملفات إلى مجلد لغات Tesseract، عادة:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (قم بالتعديل حسب التثبيت الفردي.)</li>
        <li>أعد تشغيل التطبيق (أو أعد فتح اختيار لغة OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 بديل لجميع الأنظمة</p>
        <ul>
        <li>قم بتثبيت <strong>OCRmyPDF</strong> و <strong>Tesseract</strong> باستخدام مدير الحزم الذي تختاره. معظم التثبيتات تحتوي بالفعل على بعض اللغات القياسية (الإنجليزية، الألمانية، الفرنسية).</li>
        <li>يمكن تثبيت اللغات المفقودة في أي وقت – قائمة اختيار لغة OCR تعرض فقط اللغات الموجودة بالفعل.</li>
        </ul>

        <hr>
        <p><b>✅ بعد التثبيت:</b> لا حاجة لإعادة تشغيل التطبيق – اللغات المضافة حديثًا ستظهر فورًا في القائمة.</p>
        <p><b>📖 مساعدة حول رموز اللغة:</b> قائمة كاملة متاحة في <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">وثائق Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "خطوط Noto Sans",
        "info_noto_font_voice": "دليل تثبيت خطوط Noto Sans",
        "btn_info_noto_font_install": "معلومات الخط",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ كيفية تثبيت خطوط Noto المجانية من Google</h2>

        <p><strong>خطوط Noto</strong> هي عائلة خطوط مفتوحة المصدر من Google. هدفها هو عدم رؤية <em>"لا توفو"</em> (أي لا مربعات فارغة □) وعرض كل حرف من معيار Unicode بشكل صحيح. إنها الإضافة المثالية للتطبيقات التي تحتاج إلى عرض نصوص بلغات مختلفة كثيرة.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 التثبيت على macOS</h3>

        <p><strong>الطريقة 1: باستخدام Homebrew (للمتقدمين)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>الطريقة 2: عبر "خطوط الكتاب" (موصى به)</strong></p>

        <ol>
        <li>قم بتنزيل حزمة الخطوط الرسمية:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>فك ضغط ملف ZIP</li>
        <li>انسخ الملفات إلى <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 التثبيت على Windows (10 & 11)</h3>

        <p><strong>الطريقة 1: متجر Microsoft (موصى به)</strong><br>
        ابحث عن "Google Noto Fonts" أو "Noto Sans" وانقر على <strong>تثبيت</strong>.</p>

        <p><strong>الطريقة 2: التثبيت اليدوي</strong></p>

        <ol>
        <li>تحميل:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>فك ضغط ZIP</li>
        <li>حدد ملفات .ttf / .otf</li>
        <li>زر الفأرة الأيمن → <strong>تثبيت</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        أو<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\الاسم\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 التثبيت على Linux</h3>

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

        <p>التحقق:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "إدارة الإشارات المرجعية",
        "bookmark_add": "إضافة إشارة مرجعية",
        "bookmark_add_tooltip": "حفظ الصفحة الحالية كإشارة مرجعية",
        "bookmark_remove": "إزالة إشارة مرجعية",
        "bookmark_remove_tooltip": "حذف الإشارة المرجعية المحددة",
        "bookmark_remove_all": "إزالة الكل",
        "bookmark_remove_all_tooltip": "حذف جميع الإشارات المرجعية لهذا PDF",
        "bookmark_jump": "الانتقال إلى الإشارة المرجعية",
        "bookmark_jump_tooltip": "الانتقال إلى الصفحة المحددة",
        "bookmark_name": "الاسم",
        "bookmark_page": "الصفحة",
        "bookmark_no_bookmarks": "لا توجد إشارات مرجعية.\nانقر على 'إضافة' لحفظ الصفحة الحالية كإشارة مرجعية.",
        "bookmark_added": "تمت إضافة إشارة مرجعية للصفحة {0}: {1}",
        "bookmark_removed": "تمت إزالة الإشارة المرجعية: {0}",
        "bookmark_all_removed": "تمت إزالة جميع الإشارات المرجعية.",
        "bookmark_name_default": "صفحة {0}",
        "bookmark_name_prompt": "اسم الإشارة المرجعية:\n(سيتم تقصير النص الطويل إلى 50 حرفًا)",
        "bookmark_name_prompt_title": "اسم الإشارة المرجعية",
        "bookmark_confirm_remove_all": "هل أنت متأكد أنك تريد إزالة جميع الإشارات المرجعية {0}؟",
        "menu_bookmarks": "الإشارات المرجعية",
        "bookmark_manage": "إدارة الإشارات المرجعية",
        "bookmark_next": "الإشارة التالية",
        "bookmark_prev": "الإشارة السابقة",
        "bookmark_page_display": "صفحة {0}",
        "bookmark_exists": "إشارة مرجعية لهذه الصفحة بهذا الاسم موجودة بالفعل.",
        "bookmark_select_first": "الرجاء تحديد إشارة مرجعية أولاً.",
        "bookmark_confirm_remove": "هل أنت متأكد أنك تريد إزالة الإشارة المرجعية 'صفحة {0}: {1}'؟",
        "bookmark_jumped_to": "تم الانتقال إلى الإشارة المرجعية '{0}' في الصفحة {1}.",
        "bookmark_jumped_to_voice": "إشارة مرجعية {0}، صفحة {1}",
        "btn_close": "إغلاق",

        "bookmark_list": "إشاراتك المرجعية",
        "bookmark_rename": "إعادة تسمية الإشارة المرجعية",
        "bookmark_rename_tooltip": "تغيير اسم الإشارة المرجعية المحددة",
        "bookmark_rename_title": "إعادة تسمية الإشارة المرجعية",
        "bookmark_rename_prompt": "اسم جديد للإشارة المرجعية في الصفحة {0}:\n(حد أقصى 50 حرفًا)",
        "bookmark_renamed": "تمت إعادة تسمية الإشارة المرجعية '{0}' إلى '{1}'.",
        "bookmark_item_tooltip": "صفحة {0}: {1}\nنقر مزدوج للانتقال",
        "bookmark_name_exists_question": "إشارة مرجعية بالاسم '{0}' موجودة بالفعل في هذه الصفحة.\nإعادة التسمية على أي حال؟",

        "context_bookmarks": "الإشارات المرجعية",
        "context_bookmark_add_here": "إضافة إشارة مرجعية لهذه الصفحة",
        "context_bookmarks_existing": "الإشارات المرجعية الموجودة:",
        "context_bookmarks_jump": "الانتقال إلى إشارة مرجعية:",
        "context_bookmarks_none": "لا توجد إشارات مرجعية",
        "context_bookmarks_clear_all": "إزالة جميع الإشارات المرجعية {0}",

        "bookmark_search_placeholder": "بحث في الإشارات المرجعية... (الاسم أو الصفحة)",
        "bookmark_search_results": "تم العثور على %d إشارة مرجعية لـ \"%s\"",
        "bookmark_no_search_results": "لم يتم العثور على إشارات مرجعية لـ \"%s\"",
        "bookmark_no_search_results_label": "لا توجد نتائج لـ \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "تحرير بيانات PDF الوصفية",
        "metadata_title": "العنوان",
        "metadata_title_placeholder": "عنوان المستند",
        "metadata_title_tooltip": "عنوان المستند (يظهر في شريط العنوان)",
        "metadata_author": "المؤلف",
        "metadata_author_placeholder": "اسم المؤلف",
        "metadata_author_tooltip": "منشئ المستند",
        "metadata_subject": "الموضوع",
        "metadata_subject_placeholder": "موضوع المستند",
        "metadata_subject_tooltip": "وصف قصير للمحتوى",
        "metadata_keywords": "الكلمات المفتاحية",
        "metadata_keywords_placeholder": "كلمات مفتاحية، مفصولة بفواصل",
        "metadata_keywords_tooltip": "كلمات مفتاحية لتصنيف المستند",
        "metadata_creator": "المنشئ",
        "metadata_creator_placeholder": "التطبيق الذي أنشأ PDF",
        "metadata_creator_tooltip": "البرنامج الذي تم إنشاء المستند به",
        "metadata_producer": "المنتج",
        "metadata_producer_placeholder": "التطبيق الذي حول PDF",
        "metadata_producer_tooltip": "البرنامج الذي قام بتحويل PDF",
        "metadata_creation_date": "تاريخ الإنشاء",
        "metadata_creation_date_tooltip": "تاريخ إنشاء المستند",
        "metadata_mod_date": "تاريخ التعديل",
        "metadata_mod_date_tooltip": "تاريخ آخر تعديل",
        "metadata_pdf_info": "📄 معلومات PDF",
        "metadata_pages": "عدد الصفحات",
        "metadata_file_size": "حجم الملف",
        "metadata_pdf_version": "إصدار PDF",
        "metadata_encrypted": "مشفر",
        "metadata_encrypted_yes": "نعم (محمي بكلمة مرور)",
        "metadata_encrypted_no": "لا",
        "metadata_reload": "📂 إعادة تحميل من PDF",
        "metadata_reset": "تجاهل التغييرات",
        "metadata_reloaded": "تم إعادة تحميل البيانات الوصفية من PDF.",
        "metadata_reset_done": "تمت إعادة تعيين جميع حقول البيانات الوصفية.",
        "metadata_no_file": "لم يتم تحميل ملف PDF.",
        "metadata_save_error": "خطأ في حفظ البيانات الوصفية",
        "metadata_saved": "تم حفظ البيانات الوصفية بنجاح.",
        "metadata_pdf_version_unknown": "PDF (غير معروف)",
        "metadata_saved_message": "تم حفظ البيانات الوصفية بنجاح.",
        "metadata_saved_voice": "تم حفظ البيانات الوصفية.",

        "metadata_custom": "🔧 بيانات وصفية مخصصة",
        "metadata_custom_placeholder": "{\n  \"حقي_المخصص\": \"قيمتي\",\n  \"حقل_آخر\": 123\n}",
        "metadata_custom_tooltip": "تنسيق JSON للبيانات الوصفية المخصصة (اختياري)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "تم اختيار القالب \"{0}\" - انقر نقرًا مزدوجًا للإدراج",
        "text_use_template": "استخدام قالب نصي",
        "text_type": "النوع",
        "text_search_templates": "البحث في القوالب النصية...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 معلومات التصدير / الاستيراد",
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

        <h3>📦 ما الذي يتم تصديره؟ (نظرة عامة)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">إعدادات التطبيق العامة</span></li>
            <li class="detail">• الوضع الداكن/الفاتح</li>
            <li class="detail">• عكس الصور في الوضع الداكن</li>
            <li class="detail">• قيمة عتبة الرمادي</li>
            <li class="detail">• اللغة</li>
            <li class="detail">• هندسة النافذة</li>
            <li class="detail">• وضع التكبير/التصغير</li>
            <li class="detail">• التنقل (شريط التنقل مرئي)</li>
            <li class="detail">• الإخراج الصوتي (تشغيل/إيقاف)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">إعدادات النسخ الاحتياطي</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">تسمية الملفات (الطابع الزمني، الفاصل، اللواحق)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">إعدادات إدراج</span></li>
            <li class="detail">• التوقيعات</li>
            <li class="detail">• النص وقوالب النص</li>
            <li class="detail">• علامات الاختيار والصور والأشكال</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">إعدادات OCR</span></li>
            <li class="detail">• اللغة</li>
            <li class="detail">• فرض OCR · وضع الصفحة</li>
            <li class="detail">• معالجة الصورة المسبقة: تصحيح الانحراف، التنظيف، أخذ العينات الزائد</li>
            <li class="detail">• عدد المهام المتوازية</li>
            <li class="detail">• وضع العكس</li>
            <li class="detail">• قيمة عتبة الرمادي</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">الإشارات المرجعية</span></li>
            <li class="detail">• جميع الإشارات المرجعية لكل ملف PDF (الصفحة، الاسم، وقت الإنشاء)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">قاعدة بيانات كلمات المرور</span></li>
            <li class="detail">• كلمات مرور PDF المحفوظة (مشفرة أو نص عادي حسب الاختيار)</li>
            <li class="detail">• تجزئة كلمة المرور الرئيسية (إذا تم تعيينها)</li>
            <li class="detail">• بيانات التحقق</li>
        </ul>

        <h4>⚠️ تنبيهات هامة</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 عند الاستيراد:</strong>
            <ul>
                <li><span class="warning">➜ سيتم استبدال ALL الإعدادات الحالية بالكامل</span></li>
                <li>• إعادة تشغيل التطبيق إلزامية</li>
                <li>• سيتم استبدال التوقيعات والقوالب النصية والإشارات المرجعية الموجودة</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 كلمة المرور الرئيسية ووضع التصدير:</strong>
            <ul>
                <li>• عند تفعيل كلمة المرور الرئيسية، يمكنك الاختيار:</li>
                <li>  - <span style="color: #98FB98;"><strong>غير مشفر</strong></span> (كلمات المرور بنص عادي في ملف ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>مشفر</strong></span> (قابلة للقراءة فقط بكلمة المرور الرئيسية على النظام الهدف)</li>
                <li>• تجزئة كلمة المرور الرئيسية نفسها يتم تخزينها <strong>دائمًا</strong> بشكل مشفر</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ تنبيه أمني:</strong>
            <ul>
                <li>• ملف ZIP المُصدَّر يحتوي على بيانات حساسة (<strong>كلمات المرور، الإشارات المرجعية، التوقيعات</strong>)</li>
                <li>• يرجى حفظه بأمان (مثال: محرك USB مشفر، مدير كلمات المرور)</li>
                <li>• في حالة فقدان الملف، تكون كلمات مرور PDF المحفوظة مفقودة بشكل لا يمكن استرداده</li>
            </ul>
        </div>

        <h4>📁 تنسيق التصدير</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            يتم حفظ الإعدادات في ملف ZIP واحد:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            يحتوي ملف ZIP هذا على ملف <code>settings.json</code> الكامل (من تكوينك) بالإضافة إلى ملفات صور التوقيع المضمنة وكلمات المرور المشفرة.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "التوقيعات - دليل",
        'signature_guide_html': """
        📝 <strong>التوقيعات - دليل سريع</strong><br>
        <ul>
        <li>تعيين كلمة مرور رئيسية</li>
        <li>تكوين التوقيعات في قائمة <em>الإعدادات</em> (الحجم، الطابع الزمني، …)</li>
        <li>الإدراج باستخدام <strong>الزر الأيمن</strong> في الموضع المطلوب (كلمة مرور رئيسية مطلوبة مرة واحدة لكل جلسة)</li>
        <li>تحريك التوقيع باستخدام الماوس أو مفاتيح الأسهم</li>
        <li>إدراج توقيعات متعددة تباعًا</li>
        <li>تخصيص كل توقيع على حدة</li>
        <li>رفض توقيع فردي</li>
        <li>حفظ / رفض جميع التوقيعات مرة واحدة</li>
        <li>بدلاً من ذلك، يمكن استخدام شريط القوائم أيضًا.</li>
        </ul>
        """,
        'signature_guide_voice': "دليل سريع للتوقيعات. تعيين كلمة مرور رئيسية. تكوين التوقيعات في الإعدادات. إدراج بالزر الأيمن.",

        'image_guide_title': "إدراج الصور - دليل",
        'image_guide_html': """
        📷 <strong>إدراج الصور في PDF - دليل سريع</strong><br>
        <ol>
        <li>الزر الأيمن على الموضع المطلوب</li>
        <li><em>„إدراج صورة“</em> → اختر صورة</li>
        <li>تحديد موضع الصورة: سحب بالماوس</li>
        <li>تغيير الحجم: سحب من الزوايا/الحواف</li>
        <li>الحفاظ على نسبة العرض إلى الارتفاع: مفتاح <strong>[A]</strong></li>
        <li>تعديلات إضافية: الزر الأيمن على الصورة</li>
        </ol>
        <p><strong>نصيحة:</strong> في قائمة السياق، يمكنك تعديل الإعدادات.</p>
        """,
        'image_guide_voice': "دليل سريع للصور. زر أيمن، إدراج صورة، اختر. تحديد الموضع بالماوس، تغيير الحجم من الزوايا. نسبة العرض إلى الارتفاع باستخدام مفتاح A.",

        'form_guide_title': "إدراج الأشكال - دليل",
        'form_guide_html': """
        📐 <strong>إدراج الأشكال في PDF - دليل سريع</strong><br>
        <ol>
        <li>اختر نوع الشكل (مستطيل، قطع ناقص، خط، سهم)</li>
        <li>انقر على الموضع:
            <ul>
            <li>للمستطيل/القطع الناقص: نقرة واحدة تضع الشكل</li>
            <li>للخط/السهم: نقرتان لنقطة البداية والنهاية</li>
            </ul>
        </li>
        <li>تحديد موضع الشكل: سحب بالماوس</li>
        <li>تغيير الحجم: سحب من الزوايا/الحواف</li>
        <li>حفظ الشكل: <strong>Enter</strong></li>
        <li>رفض الشكل: <strong>ESC</strong></li>
        <li>تعديلات إضافية: الزر الأيمن على الشكل</li>
        </ol>
        <p><strong>نصيحة:</strong> في قائمة السياق، يمكنك تعديل الإعدادات.</p>
        """,
        'form_guide_voice': "دليل سريع للأشكال. اختر نوع الشكل. للمستطيل أو القطع الناقص انقر مرة واحدة، للخط أو السهم انقر مرتين. تحديد الموضع بالماوس، تغيير الحجم من الزوايا. حفظ بالضغط على Enter، رفض بالضغط على Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "السابق",
        "btn_next_result": "التالي",
        "ocr_text_window": "نافذة نص OCR",
        "bookmark_existing": "إشارات مرجعية موجودة",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "مقارنة OCR بين Mac و Windows",
        'ocr_method_mac_win_title': "اختلافات OCR بين Mac و Windows",
        'ocr_method_mac_win_voice': "Mac أفضل",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – الاختلافات بين macOS و Windows</strong></p>

        <p><strong>macOS (موصى به)</strong></p>
        <p>الأداة:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>النتيجة:</p>
        <ul>
        <li>ملف PDF قابل للبحث بنص مدمج يحتفظ إلى حد كبير بالتخطيط الأصلي.</li>
        </ul>
        <p>المزايا:</p>
        <ul>
        <li>جودة ممتازة للتعرف على النص (حتى في الصفحات المائلة).</li>
        <li>الاحتفاظ بالرسومات المتجهة والخطوط.</li>
        <li>شريط تقدم واجهة المستخدم عبر تقييم العملية الفرعية.</li>
        <li>تحكم كامل في جميع معلمات OCR (إزالة الانحراف، التنظيف، الإفراط في أخذ العينات، التحسين).</li>
        <li>البحث عن النص متاح مباشرة في النافذة الرئيسية (عرض PDF).</li>
        </ul>
        <p>العيوب:</p>
        <ul>
        <li>يتطلب أدوات نظام إضافية (ocrmypdf، Ghostscript، unpaper، pngquant – مضمنة في حزمة التطبيق).</li>
        <li>معالجة أخطاء أكثر تعقيدًا (حالات توقف تام، مهلات).</li>
        </ul>

        <p><strong>Windows (بديل مستقر)</strong></p>
        <p>الأداة:</p>
        <ul>
        <li>pytesseract (اتصال مباشر بـ Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>النتيجة:</p>
        <ul>
        <li>ملف PDF قابل للبحث يتطابق بصريًا مع PDF صورة، ولكنه قابل للبحث من خلال النص الشفاف.</li>
        </ul>
        <p>المزايا:</p>
        <ul>
        <li>لا أستطيع التفكير في أي ميزة الآن.</li>
        </ul>
        <p>العيوب:</p>
        <ul>
        <li>ملف PDF هو في الأساس صورة بنص غير مرئي؛ قد ينحرف التخطيط قليلاً في المستندات المعقدة (الأعمدة، الجداول).</li>
        <li>لا يوجد تصحيح تلقائي للانحراف (--deskew) أو تنظيف الصورة (--clean).</li>
        <li>يتم تحديث شريط تقدم واجهة المستخدم بشكل تقريبي فقط بناءً على عدد الصفحات المعالجة.</li>
        <li>سرعة OCR أبطأ قليلاً (حيث تتم معالجة كل صفحة على حدة).</li>
        <li>يتم توجيه البحث عن النص إلى نافذة نص OCR.</li>
        </ul>

        <p><strong>القواسم المشتركة</strong></p>
        <ul>
        <li>تنتج كلتا العمليتين ملف PDF قابل للبحث في نفس الدليل الموجود به الملف المصدر.</li>
        <li>يمكن تكوين إعدادات OCR (اللغة، DPI، وضع تجزئة الصفحة، وضع محرك OCR) عبر OCRSettingsDialog وتكون سارية المفعول في كلا التطبيقين.</li>
        </ul>

        <p><strong>توصية:</strong></p>
        <ul>
        <li>macOS: الملف الثنائي ocrmypdf يقدم أفضل النتائج – اشترِ جهاز Mac واستخدم الإصدار (PDFDarkView لأجهزة Mac المزودة بشريحة Apple Silicon أو Intel). نتائج OCR أفضل مما هي عليه تحت Windows!</li>
        <li>Windows: استخدم حل pytesseract. إنه مستقر ويقدم جودة كافية تمامًا لمعظم المستندات.</li>
        </ul>

        <p><strong>ملاحظة هامة:</strong></p>
        <ul>
        <li>كلا الإصدارين متكاملان بالكامل في واجهة المستخدم – لا يلاحظ المستخدم أي فرق.</li>
        <li>يقرر البرنامج تلقائيًا محرك OCR الذي سيتم استخدامه بناءً على نظام التشغيل.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "إنشاء توقيع (من مسح ضوئي)",
        "signature_create_title": "اختر توقيعًا ممسوحًا ضوئيًا (PDF/صورة)",
        "image_pdf_filter": "الصور و PDF",
        "signature_pdf_empty": "ملف PDF لا يحتوي على صفحات.",
        "signature_created_success": "تم إنشاء التوقيع بنجاح: {0}",
        "signature_create_error": "خطأ أثناء إنشاء التوقيع:\n{0}",
        "rembg_missing": "rembg غير مثبت.\nالرجاء التثبيت: pip install rembg\nخطأ: {0}",
        "signature_name_title": "اسم الملف للتوقيع",
        "signature_name_message": "الرجاء إدخال اسم ملف للتوقيع الجديد (سيتم حفظه بصيغة PNG بخلفية شفافة):",
        "signature_name_label": "اسم الملف:",
        "signature_name_voice": "أدخل اسم ملف للتوقيع",
        "signature_processing": "المعالجة جارية...",
        "signature_creation_title": "جاري إنشاء التوقيع",
        "signature_overwrite_warning": "الملف '{0}' موجود بالفعل. هل تريد الاستبدال؟",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"تحضير PDF للتوقيع",
        "signature_prepare_instruction":"الرجاء اختيار ملف PDF يحتوي على توقيع ممسوح ضوئيًا على صفحة واحدة.\n\nلتحقيق التعرف الأمثل، يجب أن:\n• يكون التوقيع مكتوبًا بحبر أسود (قلم حبر جاف أو قلم تحديد) على ورق أبيض.\n• يكون التوقيع في الثلث العلوي من صفحة A4 الفارغة بخلاف ذلك.\n• تم مسح PDF ضوئيًا بدقة 300 نقطة في البوصة على الأقل.\n• يكون التوقيع واضحًا وليس رفيعًا جدًا.\n• لا توجد أنماط خلفية مزعجة أو خطوط.",
        "signature_prepare_voice":"الرجاء اختيار PDF يحتوي على توقيع ممسوح ضوئيًا. انتبه إلى الجودة الجيدة والتباين.",
        "sig_thickness_label":"سمك الخط:",
        "sig_thickness_normal":"عادي (رفيع)",
        "sig_thickness_bold":"غامق (موصى به)",
        "sig_thickness_very_bold":"غامق جدًا",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "إضافة لغات واجهة المستخدم و OCR - دليل",
        'language_guide_title': "إضافة لغات واجهة المستخدم و OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>واجهة المستخدم</h2>
        <p>قم بتنزيل ملف الترجمة المطلوب <code>translations_xy.py</code> من<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        وضعه في الدليل التالي:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>افتح متصفح الويب الخاص بك.</li>
        <li>انتقل إلى: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>ابحث على الحافة اليمنى للشاشة عن "Releases" واختر المسمى <strong>"latest"</strong>.</li>
        <li>في صفحة الإصدار التالية، قم بتنزيل الملف <code>Source Code.zip</code> من الأسفل.</li>
        <li>فك ضغط ملف ZIP.</li>
        <li>ابحث في المجلد غير المضغوط عن جميع ملفات اللغة التي تحتاجها، وانسخها إلى الدليل:<br/>
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
        "menu_watermark":"إدراج علامة مائية",
        "fullpage_text_watermark_title":"نص كعلامة مائية",
        "fullpage_image_watermark_title":"صورة كعلامة مائية",
        "filename_with_watermark":"_مع_علامة_مائية",
        "watermark_text":"النص:",
        "watermark_text_placeholder":"نص العلامة المائية الخاصة بك...",
        "watermark_font_family":"الخط:",
        "watermark_font_size":"حجم الخط:",
        "watermark_format":"التنسيق:",
        "watermark_bold":"غامق",
        "watermark_italic":"مائل",
        "watermark_color":"اللون:",
        "watermark_choose_color":"اختر لوناً...",
        "watermark_opacity":"العتامة / الشفافية:",
        "watermark_direction":"اتجاه القراءة:",
        "watermark_direction_l_r":"يسار ← يمين",
        "watermark_direction_bl_tr":"أسفل يسار ← أعلى يمين",
        "watermark_direction_tl_br":"أعلى يسار ← أسفل",
        "watermark_direction_b_t":"أسفل ← أعلى",
        "watermark_direction_t_b":"أعلى ← أسفل",
        "watermark_preview":"معاينة:",
        "watermark_preview_sample":"نص تجريبي",
        "watermark_empty_text":"يرجى إدخال نص.",
        "watermark_applied":"تم تطبيق العلامة المائية على جميع الصفحات.",
        "watermark_saved":"تم حفظ العلامة المائية.",
        "image_scale":"الحجم:",
        "image_preview":"معاينة الصورة:",
        "no_image_selected":"لم يتم اختيار صورة",
        "browse":"تصفح...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "عمليات التحرير",
        "redact_add_black": "تحرير (أسود)",
        "redact_add_white": "تحرير (أبيض / مسح)",
        "redact_added_black": "تمت إضافة تحرير أسود",
        "redact_added_white": "تمت إضافة تحرير أبيض",
        "redact_apply_all": "تطبيق جميع عمليات التحرير وحفظ",
        "redact_discard_all": "تجاهل جميع عمليات التحرير",
        "redact_discard": "تجاهل هذا التحرير",
        "no_redactions": "لا توجد عمليات تحرير",
        "redact_confirm_title": "تطبيق عمليات التحرير بشكل دائم",
        "redact_confirm_message": "تحذير: سيتم حذف المناطق المحددة نهائياً (أسود أو أبيض).\nسيتم إنشاء نسخة احتياطية (إذا تم تفعيلها).\n\nالمتابعة؟",
        "redact_apply": "نعم، احذف الآن",
        "redact_saved": "تم تطبيق وحفظ {0} عملية تحرير بنجاح.",
        "redact_saved_voice": "تم تطبيق {0} عملية تحرير",
        "redact_error": "خطأ أثناء التحرير",
        "filename_redacted":"_مع_تحرير",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'إدراج أرقام الصفحات',
        'page_numbers_format': 'تنسيق الأرقام:',
        'page_numbers_format_arabic': '1، 2، 3 ... (عربي)',
        'page_numbers_format_roman_lower': 'i، ii، iii ... (روماني صغير)',
        'page_numbers_format_roman_upper': 'I، II، III ... (روماني كبير)',
        'page_numbers_format_letter': 'A، B، C ... (حروف)',
        'page_numbers_format_custom': 'مخصص',
        'page_numbers_custom_pattern': 'النمط:',
        'page_numbers_custom_placeholder': 'مثال "صفحة {nummer}" أو "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'استخدم {nummer} لرقم الصفحة الحالي و {total} للإجمالي',
        'page_numbers_position': 'الموضع:',
        'page_numbers_pos_tl': 'أعلى يسار',
        'page_numbers_pos_tc': 'أعلى وسط',
        'page_numbers_pos_tr': 'أعلى يمين',
        'page_numbers_pos_ml': 'وسط يسار',
        'page_numbers_pos_mc': 'في المنتصف',
        'page_numbers_pos_mr': 'وسط يمين',
        'page_numbers_pos_bl': 'أسفل يسار',
        'page_numbers_pos_bc': 'أسفل وسط',
        'page_numbers_pos_br': 'أسفل يمين',
        'page_numbers_margins': 'الهوامش:',
        'page_numbers_margin_x': 'المسافة الأفقية:',
        'page_numbers_margin_y': 'المسافة العمودية:',
        'page_numbers_range': 'نطاق الصفحات:',
        'page_numbers_all_pages': 'جميع الصفحات',
        'page_numbers_custom_range': 'نطاق مخصص',
        'page_numbers_from': 'من:',
        'page_numbers_to': 'إلى:',
        'page_numbers_progress': 'جاري إدراج أرقام الصفحات...',
        'page_numbers_start': 'بدء إدراج أرقام الصفحات...',
        'page_numbers_cancel': 'تم إلغاء إدراج أرقام الصفحات',
        'page_numbers_success': 'تمت إضافة أرقام الصفحات بنجاح.\n\nهل تريد فتح PDF الجديد؟\n\n{0}',
        'page_numbers_complete': 'تمت إضافة أرقام الصفحات',
        'page_numbers_error_format': 'خطأ أثناء إدراج أرقام الصفحات: {0}',
        'page_numbers_content_type': 'نوع المحتوى:',
        'page_numbers_tab_simple': 'رقم بسيط',
        'page_numbers_tab_range': 'صفحة X من Y',
        'page_numbers_tab_date': 'التاريخ',
        'page_numbers_tab_custom': 'نص حر',
        'page_numbers_range_format': 'التنسيق:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'صفحة {aktuell} من {gesamt}',
        'page_numbers_range_custom': 'مخصص',
        'page_numbers_range_placeholder': 'مثال "صفحة {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'تنسيق التاريخ:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 يناير 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'مخصص',
        'page_numbers_date_placeholder': 'مثال %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'الموضع:',
        'page_numbers_date_before': 'التاريخ قبل رقم الصفحة',
        'page_numbers_date_after': 'التاريخ بعد رقم الصفحة',
        'page_numbers_date_only': 'التاريخ فقط (بدون رقم صفحة)',
        'page_numbers_custom_text': 'نص مخصص:',
        'page_numbers_custom_placeholder_text': 'استخدم {seite} لرقم الصفحة و {gesamt} للإجمالي\nمثال "سري - صفحة {seite}" أو "{seite} من {gesamt}"',
        "filename_with_page_number":"_مع_رقم_الصفحة",
        "filename_with_page_declaration":"_مع_بيان_الصفحة",
        "filename_with_pagenumber":"_مع_رقم_الصفحة",
        "filename_with_date":"_مع_التاريخ",
        "filename_with_my_page_declaration":"_مع_بيان_صفحة_مخصص",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "تغييرات غير محفوظة",
        "unsaved_changes_message_darkmode": "توجد إدراجات غير محفوظة.\nهل تريد حفظها قبل التبديل؟",
        "save_and_switch": "حفظ وتبديل",
        "discard_and_switch": "تبديل الآن",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'تصدير الصفحات كصور',
        'export_images_menu': 'تصدير كصور (PNG/JPEG)',
        'export_images_format': 'تنسيق الصورة:',
        'export_images_dpi': 'الدقة (DPI):',
        'export_images_quality': 'جودة JPEG:',
        'export_images_range': 'نطاق الصفحات:',
        'export_images_all_pages': 'جميع الصفحات',
        'export_images_custom_range': 'نطاق مخصص',
        'export_images_from': 'من:',
        'export_images_to': 'إلى:',
        'export_images_options': 'خيارات:',
        'export_images_single_files': 'كل صفحة كملف منفصل',
        'export_images_subfolder': 'تصدير إلى مجلد فرعي',
        'export_images_subfolder_info': 'إلى مجلد فرعي "اسم_PDF_صور"',
        'export_images_same_folder': 'في نفس مجلد PDF',
        'export_images_apply_darkmode': 'تطبيق إعدادات PDFDarkView (الوضع الداكن)',
        'export_images_target_folder': 'المجلد الهدف:',
        'export_images_browse': 'تصفح...',
        'export_images_preview': 'معاينة:',
        'export_images_preview_info': 'اختر الإعدادات للتصدير',
        'export_images_preview_info_detail': '{0} صفحة كـ {1}\nالدقة: {2} DPI\nاسم الملف: {3}\n{4}',
        'export_images_select_folder': 'اختر المجلد الهدف',
        'export_images_start': 'بدء تصدير الصور...',
        'export_images_progress': 'جاري تصدير الصور...',
        'export_images_saving': 'حفظ صفحة {0} من {1}...',
        'export_images_success': 'تم التصدير بنجاح!\n\nتم حفظ {0} صورة في:\n{1}',
        'export_images_complete': 'اكتمل تصدير الصور',
        'export_images_open_folder': '📁 فتح المجلد',
        'export_images_cancel': 'تم إلغاء تصدير الصور',
        'export_images_error_format': 'خطأ أثناء تصدير الصور: {0}',
        'export_images_pdf2image_missing': 'المكتبة "pdf2image" غير مثبتة.\n\nيرجى تثبيتها باستخدام:\npip install pdf2image\n\nبالنسبة لنظام Windows، تحتاج أيضاً إلى Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'تحويل PDF/A للأرشفة طويلة المدى',
        'pdfa_menu': 'تحويل PDF/A (مناسب للأرشفة)',
        'pdfa_info': 'يحول PDF إلى تنسيق PDF/A.\n\nتم تطوير PDF/A خصيصاً للأرشفة طويلة المدى ويضمن عرض المستند بشكل صحيح في المستقبل.',
        'pdfa_standard': 'معيار PDF/A:',
        'pdfa_standard_select': 'الإصدار:',
        'pdfa_1': 'PDF/A-1 (بسيط، متوافق على نطاق واسع)',
        'pdfa_2': 'PDF/A-2 (حديث، ضغط أفضل)',
        'pdfa_3': 'PDF/A-3 (أحدث إصدار، يسمح بالمرفقات)',
        'pdfa_standards_explanation': '📖 شرح المعايير:\n\n'
            '• PDF/A-1: أساسي، متوافق مع الأنظمة القديمة (حوالي 2005)\n'
            '• PDF/A-2: أكثر حداثة، ضغط أفضل، دعم الشفافية (حوالي 2011)\n'
            '• PDF/A-3: أحدث إصدار، يسمح بإرفاق ملفات (حوالي 2013)\n\n'
            'توصية: PDF/A-2 هو حل وسط جيد بين التوافق والوظائف الحديثة.',
        'pdfa_options': 'خيارات:',
        'pdfa_compress_enable': 'ضغط PDF (ملف أصغر)',
        'pdfa_metadata_preserve': 'الحفاظ على البيانات الوصفية (العنوان، المؤلف، إلخ)',
        'pdfa_target_folder': 'المجلد الهدف:',
        'pdfa_browse': 'تصفح...',
        'pdfa_select_folder': 'اختر المجلد الهدف',
        'pdfa_ocr_info_unknown': '🔍 تعذر التحقق من محتوى النص.',
        'pdfa_ocr_info_not_needed': '✅ النص موجود - OCR غير مطلوب.\nيمكن إنشاء PDF/A مباشرة.',
        'pdfa_ocr_info_recommended': '⚠️ لم يتم العثور على نص كافٍ.\n\nللملفات PDF القابلة للبحث، نوصي بإجراء OCR أولاً.\nملاحظة: يعمل PDF/A أيضاً بدون OCR - لكن النص لن يكون قابلاً للبحث.',
        'pdfa_ocr_info_error': '❌ خطأ أثناء التحقق: {0}',
        'pdfa_start': 'بدء تحويل PDF/A...',
        'pdfa_progress': 'جاري تحويل PDF/A...',
        'pdfa_success': 'تم تحويل PDF/A بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nهل تريد فتح PDF الجديد؟',
        'pdfa_complete': 'اكتمل تحويل PDF/A',
        'pdfa_cancel': 'تم إلغاء تحويل PDF/A',
        'pdfa_error_format': 'خطأ أثناء تحويل PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'المكتبة "ocrmypdf" غير مثبتة.\n\nيرجى تثبيتها باستخدام:\npip install ocrmypdf',
        'btn_convert': 'تحويل',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'تحسين PDF (تقليل حجم الملف)',
        'optimize_menu': 'تحسين PDF (حجم الملف)',
        'optimize_info': 'يقلل حجم ملف PDF من خلال طرق تحسين متعددة.\n\nكلما ارتفع مستوى الضغط، أصبح الملف أصغر - مع احتمال فقدان الجودة في الصور.',
        'optimize_level': 'مستوى الضغط:',
        'optimize_level_low': 'منخفض (سريع، توفير بسيط)',
        'optimize_level_medium': 'متوسط (حل وسط جيد)',
        'optimize_level_high': 'مرتفع (توفير قوي)',
        'optimize_level_maximum': 'أقصى (أقصى توفير، بطيء)',
        'optimize_level_explanation': 'توصية: "متوسط" هو حل وسط جيد بين السرعة وحجم الملف.',
        'optimize_options': 'خيارات:',
        'optimize_compress_images': 'ضغط الصور (تقليل جودة JPEG)',
        'optimize_clean_objects': 'إزالة الكائنات غير المستخدمة',
        'optimize_preserve_metadata': 'الحفاظ على البيانات الوصفية (العنوان، المؤلف، إلخ)',
        'optimize_image_quality': 'جودة الصورة:',
        'optimize_range': 'نطاق الصفحات:',
        'optimize_all_pages': 'جميع الصفحات',
        'optimize_custom_range': 'نطاق مخصص',
        'optimize_from': 'من:',
        'optimize_to': 'إلى:',
        'optimize_target_folder': 'المجلد الهدف:',
        'optimize_browse': 'تصفح...',
        'optimize_select_folder': 'اختر المجلد الهدف',
        'optimize_info_box': 'معلومات',
        'optimize_info_text': 'قد يستغرق التحسين عدة دقائق في الملفات PDF الكبيرة.\n\nسيتم حفظ الصور بجودة مخفضة، مما يمكن أن يقلل حجم الملف بشكل كبير.',
        'optimize_start': 'بدء تحسين PDF...',
        'optimize_progress': 'جاري تحسين PDF...',
        'optimize_cancel': 'تم إلغاء تحسين PDF',
        'optimize_complete': 'اكتمل تحسين PDF',
        'optimize_error_format': 'خطأ أثناء تحسين PDF:\n\n{0}',
        'optimize_success_message': 'تم تحسين PDF بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nقبل: {1}\nبعد: {2}\nالتوفير: {3:.1f}%\n\n{4}\n\nهل تريد فتح PDF المحسن؟',
        'optimize_success_message_no_size': 'تم تحسين PDF بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nمعلومات الحجم غير متوفرة.\n\nهل تريد فتح PDF المحسن؟',
        'optimize_result_positive': 'تم تقليل الملف بنسبة {0:.1f}%.',
        'optimize_result_zero': 'لا يوجد تغيير في حجم الملف.',
        'optimize_result_negative': 'زاد حجم الملف بنسبة {0:.1f}%.\nتم تخطي التحسين، وتم الاحتفاظ بالملف الأصلي.',
        'btn_optimize': 'بدء التحسين',
        'filename_optimize_low_suffix': '_محسن_منخفض',
        'filename_optimize_medium_suffix': '_محسن',
        'filename_optimize_high_suffix': '_محسن_مرتفع',
        'filename_optimize_maximum_suffix': '_محسن_أقصى',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'قص PDF',
        'crop_menu': 'قص PDF (Crop)',
        'crop_range': 'تطبيق على:',
        'crop_all_pages': 'جميع الصفحات',
        'crop_current_page': 'الصفحة الحالية فقط',
        'crop_values': 'قيم القص (بالنقاط):',
        'crop_left': 'يسار:',
        'crop_right': 'يمين:',
        'crop_top': 'أعلى:',
        'crop_bottom': 'أسفل:',
        'crop_presets': 'إعدادات مسبقة:',
        'crop_preset_white': 'كشف الهوامش البيضاء',
        'crop_reset': 'إعادة تعيين',
        'crop_mouse_hint': '🖱️ اسحب مستطيلاً لتحديد المنطقة تقريباً.\nبعد ذلك يمكنك ضبط القيم بدقة في SpinBoxes.\nلا يمكن الضبط اليدوي بالماوس.',
        'crop_apply': 'قص',
        'crop_scope_all': 'جميع الصفحات',
        'crop_scope_current': 'الصفحة الحالية',
        'crop_new_size': 'الحجم الجديد: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'لم يتم تحميل PDF',
        'crop_preview_error': 'خطأ أثناء تحميل المعاينة',
        'crop_start': 'بدء القص...',
        'crop_progress': 'جاري قص PDF...',
        'crop_success': 'تم قص PDF بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nهل تريد فتح PDF المقصوص؟',
        'crop_complete': 'اكتمل القص',
        'crop_cancel': 'تم إلغاء القص',
        'crop_error_format': 'خطأ أثناء القص:\n\n{0}',
        'filename_crop_suffix': '_مقصوص',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'تسطيح PDF (Flatten)',
        'flatten_menu': 'تسطيح PDF (Flatten)',
        'flatten_info': 'تسطيح PDF "يحرق" جميع العناصر القابلة للتحرير في محتوى الصفحة.\n\nبعد ذلك، لا يمكن تحرير حقول النماذج والتعليقات والنصوص والعلامات والتوقيعات والصور والأشكال بشكل فردي.',
        'flatten_explanation_title': '📖 لماذا هذا مفيد؟',
        'flatten_explanation_text': 'التسطيح مطلوب في الحالات التالية:\n\n'
            '• 📄 تريد تحضير المستند للطباعة\n'
            '• 🔒 تريد منع أي شخص من تغيير حقول النماذج\n'
            '• 📎 تريد تضمين التعليقات والملاحظات "بشكل دائم" في المستند\n'
            '• 🖼️ تريد تثبيت النصوص والعلامات والتوقيعات والصور والأشكال المدرجة بشكل دائم في المستند\n'
            '• 📦 تريد تحضير الملف للأرشفة\n\n'
            'يجعل التسطيح PDF أصغر ويمنع نقل العناصر أو حذفها عن طريق الخطأ.',
        'flatten_what_title': 'ما الذي يتم تسطيحه؟',
        'flatten_what_list': '• ✅ حقول النماذج (حقول النص، مربعات الاختيار، الأزرار)\n'
            '• ✅ التعليقات (التعليقات، التمييز، الملاحظات)\n'
            '• ✅ الطبقات العلوية (النصوص، العلامات، التوقيعات، الصور، الأشكال)',
        'flatten_options': 'خيارات:',
        'flatten_forms': 'تسطيح حقول النماذج',
        'flatten_annotations': 'تسطيح التعليقات',
        'flatten_overlays': 'تسطيح الطبقات العلوية (النصوص، العلامات، التوقيعات، الصور، الأشكال)',
        'flatten_target_folder': 'المجلد الهدف:',
        'flatten_browse': 'تصفح...',
        'flatten_select_folder': 'اختر المجلد الهدف',
        'flatten_warning': '⚠️ مهم: التسطيح عملية لا رجعة فيها!\n\nبعد التسطيح، لا يمكن تغيير أو حذف العناصر القابلة للتحرير بشكل فردي.\nأنشئ نسخة احتياطية مسبقاً إذا لزم الأمر.',
        'flatten_apply': 'تسطيح',
        'flatten_start': 'بدء التسطيح...',
        'flatten_progress': 'جاري تسطيح PDF...',
        'flatten_success': 'تم تسطيح PDF بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nهل تريد فتح PDF المسطح؟',
        'flatten_complete': 'اكتمل التسطيح',
        'flatten_cancel': 'تم إلغاء التسطيح',
        'flatten_error_format': 'خطأ أثناء التسطيح:\n\n{0}',
        'filename_flatten_suffix': '_مسطح',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'تراكب PDF (Overlay)',
        'overlay_menu': 'تراكب PDF (Overlay)',
        'overlay_info': 'يضع PDF (تراكب) فوق PDF آخر.\n\nيتم وضع PDF التراكب على PDF الأساسي. هذا مفيد للعلامات المائية والشعارات والرؤوس أو الأختام.',
        'overlay_explanation_title': '📖 لماذا هذا مفيد؟',
        'overlay_explanation_text': 'التراكب مطلوب في الحالات التالية:\n\n'
            '• 🏢 وضع شعار الشركة كعلامة مائية على كل صفحة\n'
            '• 📄 وضع رأسية على PDF فارغ\n'
            '• 🖊️ وضع تراكب ختم على مستند\n'
            '• 🔖 وضع علامة مائية على جميع الصفحات\n'
            '• 📑 وضع تراكب نموذج على قالب',
        'overlay_type': 'نوع التراكب:',
        'overlay_type_fullpage': 'صفحة كاملة (تغطية)',
        'overlay_type_transparent': 'صفحة كاملة (شفاف - موصى به)',
        'overlay_type_stamp': 'ختم (قابل للتحديد)',
        'overlay_type_info_fullpage': '📄 يتم وضع PDF التراكب تماماً فوق الصفحة بأكملها.\nيمكن إزالة الخلفية البيضاء بحيث يبقى المحتوى فقط مرئياً.',
        'overlay_type_info_transparent': '🔍 يتم وضع PDF التراكب بخلفية شفافة فوق الصفحة بأكملها.\nتتم إزالة الخلفية البيضاء تلقائياً - مثالي للعلامات المائية والشعارات!',
        'overlay_type_info_stamp': '🖊️ يتم وضع PDF التراكب كختم وتحديد حجمه.\nمثالي للشعارات أو الأختام أو التوقيعات في مواضع محددة.',
        'overlay_remove_background': 'إزالة الخلفية البيضاء:',
        'overlay_remove_background_enable': 'إزالة الخلفية البيضاء من PDF التراكب (يجعل التراكب شفافاً)',
        'overlay_remove_background_tooltip': 'يزيل المناطق البيضاء من PDF التراكب بحيث يصبح النص السفلي مرئياً.',
        'overlay_threshold': 'قيمة العتبة:',
        'overlay_threshold_hint': '(1-254، أعلى = إزالة المزيد من الأبيض)',
        'overlay_select_file': 'اختر PDF التراكب:',
        'overlay_file_placeholder': 'يرجى اختيار ملف PDF للتراكب',
        'overlay_browse': 'تصفح...',
        'overlay_select_overlay': 'اختر PDF التراكب',
        'overlay_range': 'نطاق الصفحات:',
        'overlay_all_pages': 'جميع الصفحات',
        'overlay_custom_range': 'نطاق مخصص',
        'overlay_from': 'من:',
        'overlay_to': 'إلى:',
        'overlay_position': 'الموضع:',
        'overlay_position_center': 'المنتصف',
        'overlay_position_top_left': 'أعلى يسار',
        'overlay_position_top_right': 'أعلى يمين',
        'overlay_position_bottom_left': 'أسفل يسار',
        'overlay_position_bottom_right': 'أسفل يمين',
        'overlay_size': 'الحجم:',
        'overlay_size_original': 'الحجم الأصلي',
        'overlay_size_fit_page': 'ملاءمة للصفحة',
        'overlay_size_custom': 'مخصص (%)',
        'overlay_opacity': 'الشفافية:',
        'overlay_target_folder': 'المجلد الهدف:',
        'overlay_browse_folder': 'تصفح...',
        'overlay_select_folder': 'اختر المجلد الهدف',
        'overlay_warning': '⚠️ ملاحظة: يتم وضع PDF التراكب على PDF الأساسي و"حرقه" فيه.\n\nلا يمكن تحرير عناصر PDF التراكب بشكل فردي بعد الحفظ.',
        'overlay_apply': 'تراكب',
        'overlay_start': 'بدء التراكب...',
        'overlay_progress': 'جاري تراكب PDF...',
        'overlay_success': 'تم تراكب PDF بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nهل تريد فتح PDF المتراكب؟',
        'overlay_complete': 'اكتمل التراكب',
        'overlay_cancel': 'تم إلغاء التراكب',
        'overlay_error_format': 'خطأ أثناء التراكب:\n\n{0}',
        'overlay_no_file': 'لم يتم اختيار PDF تراكب.\n\nيرجى اختيار ملف PDF للتراكب.',
        'filename_overlay_suffix': '_متراكب',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'استخراج الصور من PDF',
        'extract_images_menu': 'استخراج جميع الصور',
        'extract_images_info': 'يستخرج جميع الصور من PDF ويحفظها كملفات منفصلة.\n\nيتم حفظ الصور بتنسيقها الأصلي أو تحويلها إلى تنسيق محدد.',
        'extract_images_format': 'تنسيق الصورة:',
        'extract_images_quality': 'جودة JPEG:',
        'extract_images_options': 'خيارات:',
        'extract_images_subfolder': 'استخراج إلى مجلد فرعي ("اسم_PDF_صور")',
        'extract_images_unique': 'الصور الفريدة فقط (تجنب التكرار)',
        'extract_images_range': 'نطاق الصفحات:',
        'extract_images_all_pages': 'جميع الصفحات',
        'extract_images_custom_range': 'نطاق مخصص',
        'extract_images_from': 'من:',
        'extract_images_to': 'إلى:',
        'extract_images_target_folder': 'المجلد الهدف:',
        'extract_images_browse': 'تصفح...',
        'extract_images_select_folder': 'اختر المجلد الهدف',
        'extract_images_info_box': 'معلومات',
        'extract_images_info_text': 'قد يستغرق الاستخراج عدة دقائق في الملفات PDF الكبيرة.\n\nيتم حفظ الصور باسمها الأصلي (صفحة_صورة).',
        'extract_images_extract': 'استخراج',
        'extract_images_start': 'بدء الاستخراج...',
        'extract_images_progress': 'جاري استخراج الصور...',
        'extract_images_success': '✅ تم استخراج الصور بنجاح!\n\nتم حفظ {0} صورة في:\n{1}',
        'extract_images_complete': 'اكتمل استخراج الصور',
        'extract_images_cancel': 'تم إلغاء الاستخراج',
        'extract_images_error_format': 'خطأ أثناء استخراج الصور:\n\n{0}',
        'extract_images_open_folder': '📁 فتح المجلد',
        'extract_images_no_images': 'لم يتم العثور على صور في PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'صفحات متعددة على صفحة واحدة (N-Up)',
        'nup_menu': 'صفحات متعددة على صفحة واحدة (N-Up)',
        'nup_info': 'يرتب عدة صفحات PDF على صفحة واحدة.\n\nمثالي للمطبوعات المدمجة والنظرات العامة أو النشرات.',
        'nup_layout': 'التخطيط:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'معاينة:',
        'nup_preview_info': '{0} صفحات → {1} صفحة لكل ورقة → {2} ورقة\nالتخطيط: {3}',
        'nup_order': 'الترتيب:',
        'nup_order_horizontal': 'أفقي (صفاً تلو الآخر)',
        'nup_order_vertical': 'عمودي (عموداً تلو الآخر)',
        'nup_order_horizontal_reverse': 'أفقي عكسي',
        'nup_order_vertical_reverse': 'عمودي عكسي',
        'nup_range': 'نطاق الصفحات:',
        'nup_all_pages': 'جميع الصفحات',
        'nup_custom_range': 'نطاق مخصص',
        'nup_from': 'من:',
        'nup_to': 'إلى:',
        'nup_options': 'خيارات:',
        'nup_margins': 'الهوامش:',
        'nup_margin_between': 'المسافة بين الصفحات:',
        'nup_page_numbers': 'إدراج أرقام الصفحات',
        'nup_target_folder': 'المجلد الهدف:',
        'nup_browse': 'تصفح...',
        'nup_select_folder': 'اختر المجلد الهدف',
        'nup_create': 'إنشاء',
        'nup_start': 'بدء N-Up...',
        'nup_progress': 'جاري إنشاء N-Up...',
        'nup_success': 'تم إنشاء N-Up بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nهل تريد فتح PDF الجديد؟',
        'nup_complete': 'اكتمل N-Up',
        'nup_cancel': 'تم إلغاء N-Up',
        'nup_error_format': 'خطأ أثناء N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'تغيير حجم الصفحة',
        'pagesize_menu': 'تغيير حجم الصفحة',
        'pagesize_info': 'يغير حجم صفحة PDF.\n\nيتم تكييف المحتوى تلقائياً مع الحجم الجديد.',
        'pagesize_format': 'التنسيق:',
        'pagesize_select': 'اختر تنسيقاً قياسياً:',
        'pagesize_custom': 'حجم مخصص:',
        'pagesize_width': 'العرض:',
        'pagesize_height': 'الارتفاع:',
        'pagesize_orientation': 'الاتجاه:',
        'pagesize_portrait': 'عمودي',
        'pagesize_landscape': 'أفقي',
        'pagesize_scale_options': 'خيارات التحجيم:',
        'pagesize_fit': 'تكييف (الحفاظ على نسبة العرض إلى الارتفاع)',
        'pagesize_stretch': 'تمديد (تشويه)',
        'pagesize_center': 'توسيط (الحجم الأصلي)',
        'pagesize_range': 'نطاق الصفحات:',
        'pagesize_all_pages': 'جميع الصفحات',
        'pagesize_custom_range': 'نطاق مخصص',
        'pagesize_from': 'من:',
        'pagesize_to': 'إلى:',
        'pagesize_target_folder': 'المجلد الهدف:',
        'pagesize_browse': 'تصفح...',
        'pagesize_select_folder': 'اختر المجلد الهدف',
        'pagesize_apply': 'تطبيق',
        'pagesize_start': 'بدء تغيير حجم الصفحة...',
        'pagesize_progress': 'جاري تغيير حجم الصفحة...',
        'pagesize_success': 'تم تغيير حجم الصفحة بنجاح!\n\nتم الحفظ كـ:\n{0}\n\nهل تريد فتح PDF الجديد؟',
        'pagesize_complete': 'اكتمل تغيير حجم الصفحة',
        'pagesize_cancel': 'تم إلغاء تغيير حجم الصفحة',
        'pagesize_error_format': 'خطأ أثناء تغيير حجم الصفحة:\n\n{0}',
        'pagesize_preview_info': 'الحجم الجديد: {0} x {1} pt',
        'filename_pagesize_suffix': '_حجم_جديد',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'معلومات PDF',
        'pdf_info_menu': 'عرض معلومات PDF',
        'pdf_info_voice': 'جاري عرض معلومات PDF',
        'pdf_info_error': 'خطأ أثناء عرض معلومات PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "عرض اختصارات لوحة المفاتيح",
        "shortcuts_dialog_title": "اختصارات لوحة المفاتيح",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 ملف</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>فتح PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>إغلاق PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>حفظ باسم...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>حماية المستند</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>طباعة</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>طباعة فورية (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>إنهاء التطبيق</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 تصدير</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>تصدير كـ Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>تصدير كـ DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>تصدير كـ TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>تصدير كصور (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>استخراج الصور</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ معالجة المستندات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (صفحات متعددة)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>تحويل PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>تسطيح PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>تراكب PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>تحسين PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ تحرير</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>بحث</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>إضافة إشارة مرجعية</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>إدارة الإشارات المرجعية</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>الإشارة المرجعية التالية</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>الإشارة المرجعية السابقة</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>تنفيذ OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 إدارة الصفحات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>تدوير الصفحة الحالية</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>تدوير جميع الصفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>تطبيع الصفحة الحالية</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>تطبيع جميع الصفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>حذف الصفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>استخراج الصفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>إدراج صفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>نقل الصفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>دمج PDFs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>تغيير حجم الصفحة</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 إدراج</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>إدراج نص</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>إدراج علامة</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>إدراج توقيع 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>إدراج توقيع 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>إدراج صورة</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>إدراج مستطيل</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>إدراج قطع ناقص</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>إدراج خط</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>إدراج سهم</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>إدراج أرقام الصفحات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>علامة مائية نصية</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>علامة مائية صورية</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ عمليات التحرير</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>تحرير (أسود)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>تحرير (أبيض)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>تطبيق جميع عمليات التحرير</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ متقدم</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>قص PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>تحرير البيانات الوصفية</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ عرض</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>تبديل الوضع الداكن/الفاتح</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>عرض نافذة النص</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>عرض الصفحة (تكبير)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>صفحتان (تكبير)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>نظرة عامة (تكبير)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ الإعدادات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>إدارة كلمات المرور</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>إعدادات OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>إعدادات التوقيع</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>تنسيق اسم الملف</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>تصدير الإعدادات</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>استيراد الإعدادات</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ معلومات</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>عرض معلومات PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>تشغيل/إيقاف الإخراج الصوتي</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>تركيز شريط القوائم</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "إصدار جديد متاح",
        "update_available_message": "يوجد إصدار جديد <b>{0}</b>.\n\nقم بزيارة صفحة الإصدار لتحميل التحديث:\n{1}",
        "update_available_voice": "الإصدار الجديد {0} متاح. يرجى تحميل التحديث من صفحة GitHub.",
        "update_open_release": "فتح صفحة الإصدار",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "تحميل جميع الترجمات",
        "ask_download_all_translations": """بالإضافة إلى الألمانية والإنجليزية والفيتنامية، هناك {total_languages} لغة واجهة أخرى متاحة.\n\nهل يجب توفيرها / تحديثها؟\n\nملاحظة:\nيمكنك حذف اللغات غير الضرورية لاحقاً يدوياً في الدليل:\n{translations_path}
        \nإذا قمت بالإلغاء، يمكنك تحميل لغات الواجهة لاحقاً عبر القائمة 'أدوات → تحديث الترجمات'.""",
        "menu_update_translations": "تحديث الترجمات",
        "translations_updated": "تم تحديث الترجمات",
        "translations_update_success": "تم تحديث {} ترجمة بنجاح ({} جديدة، {} محدثة).",
        "translations_update_error": "خطأ في تحديث الترجمات",
        "translations_update_no_changes": "جميع الترجمات محدثة بالفعل.",
        "translations_update_offline": "لا يوجد اتصال بالإنترنت. لم يمكن تحديث الترجمات.",
        "translations_update_in_progress": "جاري تحديث الترجمات في الخلفية...",
        "translations_downloading": "جاري تحميل الترجمات...",
        "translations_path_hint": "دليل المستخدم للترجمات",
        "translations_update_not_available_title": "التحديث غير متاح",
        "translations_update_not_available_message": """تحديث الترجمات متاح فقط في النسخة المثبتة.\n\nفي وضع التطوير، الترجمات محدثة بالفعل.""",
        "translations_update_no_internet_title": "لا يوجد اتصال بالإنترنت",
        "translations_update_no_internet_message": """لا يمكن إنشاء اتصال بالإنترنت.\n\nلا يمكن تحميل الترجمات من GitHub.\n\nالحلول الممكنة:
        • تحقق من اتصالك بالإنترنت
        • قم بتعطيل جدار الحماية مؤقتاً
        • حاول مرة أخرى لاحقاً
        \nيمكنك أيضاً تحميل الترجمات يدوياً من GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "التحديث قيد التنفيذ بالفعل",
        "btn_retry": "إعادة المحاولة",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "مرحباً بك في PDF Dark View",
        "welcome_title_not_supported": "مرحباً بك في PDF Dark View",
        "welcome_message": "مرحباً بك في PDF Dark View!\n\nتم التعرف على لغة نظامك كـ '{language}'.\nهل تريد استخدام هذه اللغة لواجهة المستخدم؟\n\nيمكنك تغيير اللغة في أي وقت عبر 'الإعدادات → اللغة'.",
        "welcome_message_language_not_available": "مرحباً بك في PDF Dark View!\n\nتم التعرف على لغة نظامك كـ '{language}'.\nهذه اللغة غير مثبتة حالياً.\n\nهل تريد تحميل ترجمات {language} الآن من GitHub؟\n\n(سيتم استخدام اللغة تلقائياً لواجهة المستخدم.)",
        "welcome_message_language_not_supported": "مرحباً بك في PDF Dark View!\n\nتم التعرف على لغة نظامك كـ '{language}'.\nللأسف، لا توجد ترجمات لهذه اللغة حالياً.\n\nسيتم عرض واجهة المستخدم بـ {fallback_language}.\n\nيمكنك تغيير اللغة في أي وقت عبر 'الإعدادات → اللغة'.\nإذا أردت، يمكنك أيضاً المساهمة بترجمة للغتك:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "نعم، استخدام لغة النظام",
        "welcome_keep_english": "لا، الاحتفاظ بالإنجليزية",
        "welcome_download_language": "نعم، تحميل {language}",

        # ============================================
        # 107. المسارات المستخدمة مؤخرًا
        # ============================================

        'menu_recent': 'المستخدمة مؤخرًا',
        'menu_recent_dirs': 'المجلدات...',
        'menu_recent_files': 'الملفات...',
        'recent_manage': 'إدارة...',
        'recent_enable_tracking': 'حفظ المسارات المستخدمة مؤخرًا (الخصوصية)',
        'recent_enable_info': 'عطّل هذا الخيار لعدم حفظ أي مسارات',
        'recent_tracking_disabled': 'تعقب المسار معطل',
        'recent_enabled': 'مفعل',
        'recent_disabled': 'معطل',
        'recent_tracking_status': 'تعقب المسار {0}',
        'recent_dialog_title': 'المسارات المستخدمة مؤخرًا',
        'recent_tab_directories': 'المجلدات',
        'recent_tab_files': 'الملفات',
        'recent_dirs_instruction': 'انقر مرتين لفتح حوار الملف في المجلد',
        'recent_files_instruction': 'انقر مرتين لفتح PDF مباشرةً',
        'recent_no_directories': '(لا توجد مجلدات محفوظة)',
        'recent_no_files': '(لا توجد ملفات محفوظة)',
        'recent_default_current': '⭐ الافتراضي: {0}',
        'recent_set_as_default': '⭐ تعيين كافتراضي',
        'recent_default_set_title': 'تم تعيين المجلد الافتراضي',
        'recent_default_set_message': 'تم تعيين المجلد "{0}" كافتراضي لفتح ملفات PDF.',
        'recent_default_set_voice': 'تم تعيين المجلد الافتراضي',
        'recent_directory_not_found': 'المجلد غير موجود',
        'recent_file_not_found': 'الملف غير موجود',
        'recent_remove_selected': 'إزالة',
        'recent_remove_title': 'إزالة المسار',
        'recent_remove_confirm': 'هل تريد حقًا إزالة المسار "{0}" من القائمة؟',
        'recent_path_removed': 'تم إزالة المسار',
        'recent_clear_all': 'إزالة الكل',
        'recent_clear_title': 'إزالة جميع المسارات',
        'recent_clear_confirm_type': 'هل تريد حقًا حذف جميع {0}؟',
        'recent_cleared': 'تم مسح القائمة',
        'recent_path_not_found_title': 'المسار غير موجود',
        'recent_path_not_found_message': 'لم يعد المسار "{0}" موجودًا.',
        'recent_open_file': 'فتح الملف',
        'btn_open_recent': 'فتح',
        'recent_open_file_question': 'هل تريد فتح "{0}" كـ PDF؟',
        'recent_not_pdf': 'الملف المحدد ليس PDF.',
        'recent_more_entries': 'المزيد من الإدخالات...',
        'btn_remove': 'إزالة',
        'btn_clear': 'مسح الكل',
        'recent_context_open': 'فتح',
        'recent_context_reveal': 'عرض في Finder',
        'recent_context_set_default': '⭐ تعيين كافتراضي',
        'recent_context_open_terminal': '💻 فتح الطرفية',
        'recent_context_file_info': 'معلومات الملف',
        'recent_context_open_with_default': '📄 فتح بالتطبيق الافتراضي',
        'recent_context_remove': 'إزالة من القائمة',
        'recent_context_clear_all': 'إزالة الكل',
        'recent_file_info_title': 'معلومات الملف',
        'recent_file_info_name': 'الاسم',
        'recent_file_info_path': 'المسار',
        'recent_file_info_size': 'الحجم',
        'recent_file_info_modified': 'آخر تعديل',
        'recent_file_info_pages': 'الصفحات',
        'recent_error_reveal': 'خطأ في الفتح في Finder',
        'recent_error_terminal': 'خطأ في فتح الطرفية',
        'recent_error_info': 'خطأ في جلب معلومات الملف',
        'open_user_data_folder': 'عرض مجلد بيانات المستخدم',

        # ============================================
        # 108. حذف الصفحات الزوجية/الفردية
        # ============================================
        "pages_delete_even": "حذف جميع الصفحات الزوجية",
        "pages_delete_odd":  "حذف جميع الصفحات الفردية",
        "progress_even_pages": "جارٍ حذف الصفحات الزوجية",
        "progress_odd_pages": "جارٍ حذف الصفحات الفردية",
        "progress_mark_delete_even": "تم تحديد {} صفحة زوجية للحذف",
        "progress_mark_delete_odd":  "تم تحديد {} صفحة فردية للحذف",

        # ============================================
        # 109. إنهاء البرنامج
        # ============================================
        "app_quitting": "جاري إنهاء البرنامج",

    }


