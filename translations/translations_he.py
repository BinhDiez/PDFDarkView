
# ============================================
# translations_he.py - מילון עברי (Hebräisch - Ivrit)
# Vollständig sortiert nach Kategorien
# ============================================

def load_hebrew_strings():
    """Lädt alle hebräischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View מאת BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "פתח קובץ PDF",
        'btn_text_window': "טקסט OCR",
        'btn_first': "עמוד ראשון",
        'btn_prev': "עמוד קודם",
        'btn_next': "עמוד הבא",
        'btn_last': "עמוד אחרון",
        'btn_print': "הדפס",
        'btn_darkmode_light': "מצב בהיר",
        'btn_darkmode_dark': "מצב כהה",
        'btn_delete_pages': "מחק עמודים",
        'btn_extract_pages': "חלץ עמודים",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "אישור",
        'btn_cancel': "ביטול",
        'btn_save': "שמור",
        'btn_close': "סגור",
        'btn_delete': "מחק",
        'btn_delete_all': "מחק הכל",
        'btn_copy': "העתק",
        'btn_export': "ייצא",
        'btn_show': "הצג סיסמה",
        'btn_hide': "הסתר סיסמה",
        'btn_authenticate': "אמת",
        'btn_settings': "הגדרות",
        'btn_protect': "הגן",
        'btn_remove_password': "הסר סיסמה",
        'btn_manage': "ניהול סיסמאות",
        'btn_retry': "נסה שוב",
        'btn_select_all': "בחר הכל",
        'btn_clear_selection': "נקה בחירה",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "עמוד {0} מתוך {1}",
        'page_count': "מתוך {0}",
        'goto_page': "עבור לעמוד",
        'page_simple': "עמוד {0}",
        'full_view_page': "תצוגה מלאה עמוד {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "הכנס מונח חיפוש + Enter",
        'search_results': "תוצאות: {0} מתוך {1}",
        'search_nav_hint': "Enter: תוצאה הבאה (Shift+Enter: תוצאה קודמת)",
        'search_no_results': "אין תוצאות",
        'search_error': "שגיאת חיפוש",
        'search_active': "שדה החיפוש הופעל",
        'search_closed': "החיפוש הסתיים",
        'search_position': "עמוד {0} {1}",
        'search_pos_top': "ממש למעלה",
        'search_pos_upper': "למעלה",
        'search_pos_middle': "באמצע",
        'search_pos_lower': "למטה",
        'search_pos_bottom': "ממש למטה",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "זיהוי הטקסט הושלם בהצלחה!",
        'ocr_success_title': "OCR הצליח",
        'ocr_success_message': "המסמך ניתן כעת לחיפוש.",
        'ocr_failed': "OCR נכשל",
        'ocr_in_progress': "OCR בעיצומו",
        'ocr_preparing': "מכין PDF...",
        'ocr_analyzing': "מנתח PDF...",
        'ocr_optimizing': "מיטוב תמונה...",
        'ocr_recognizing': "מזהה טקסט...",
        'ocr_embedding': "מטמיע טקסט...",
        'ocr_finalizing': "מסיים PDF...",
        'ocr_not_available': "OCR אינו זמין",
        'ocr_install_message': "כלי OCR לא נמצאו.\n\nאנא התקן:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "נדרש OCR",
        'ocr_question': "ה-PDF אינו מכיל טקסט הניתן לחיפוש.\nהאם ברצונך לבצע OCR כדי לאפשר {0}?",
        'ocr_perform': "בצע OCR",
        'ocr_later': "אחר כך",
        'ocr_starting': "מתחיל OCR מובטח...",
        'ocr_success_voice': "OCR הצליח. ה-PDF ניתן כעת לחיפוש.",
        'ocr_partial_success': "OCR בוצע, אך היו בעיות בהחלפה.\n\nהגרסה הניתנת לחיפוש נשמרה בכתובת:\n{0}\n\nשגיאה: {1}",
        'ocr_partial_title': "OCR הצליח חלקית",
        'ocr_partial_voice': "OCR בוצע, אך ההחלפה נכשלה.",
        'original_file': "קובץ מקורי:",
        'old_size': "גודל ישן:    {0} בתים",
        'new_size': "גודל חדש: {0} בתים",
        'size_change': "שינוי: {0}{1} בתים",
        'backup_created_file': "גיבוי נוצר:\n{0}",
        'backup_not_created': "גיבוי לא נוצר (ההגדרה כבויה)",
        'page_header': "=== עמוד {0} ===\n{1}\n",
        'scanned_page_header': "=== עמוד {0} (סרוק) ===\n[עמוד זה מכיל רק טקסט סרוק]\n[אנא בצע OCR ידנית]\n",
        'scanned_warning': "⚠️ טקסט סרוק - נדרש OCR",
        'guaranteed_title': "נוצר PDF הניתן לחיפוש",
        'guaranteed_message': "<b>נוצרה גרסה מובטחת הניתנת לחיפוש!</b>\n\nמאחר ש-OCR האוטומטי נכשל, נוצר PDF חלופי הניתן לחיפוש:\n\n{0}\n\n<b>קובץ זה מכיל:</b>\n• טקסט שחולץ (אם היה קיים)\n• הוראות לעמודים סרוקים\n• ניתן לחיפוש מלא",
        'guaranteed_voice': "נוצר PDF מובטח הניתן לחיפוש.",
        'instruction_title': "הוראות OCR",
        'instruction_file': "קובץ מקורי: {0}",
        'instruction_text': "זיהוי הטקסט האוטומטי (OCR) נכשל.\nבצע OCR ידנית:\n\n1. עם OCRmyPDF (שורת פקודה):\n   ocrmypdf --force-ocr \"[קובץ]\" \"פלט.pdf\"\n\n2. עם ADOBE ACROBAT (macOS/Windows):\n   • פתח את ה-PDF ב-Acrobat\n   • כלים > ערוך PDF\n   • בחר 'זיהוי טקסט'\n\n3. עם PREVIEW (macOS):\n   • פתח את ה-PDF בתצוגה מקדימה\n   • קובץ > ייצא...\n   • מסנן Quartz: 'הקטן גודל קובץ'\n   • הפעל 'בצע OCR'\n\n4. שירותי OCR מקוונים:\n   • smallpdf.com/he/ocr-pdf\n   • ilovepdf.com/he/ocr-pdf\n   • adobe.com/he/acrobat/online/pdf-to-word.html",
        'instruction_created': "נוצרו הוראות OCR",
        'instruction_created_message': "נוצרו הוראות מפורטות:\n\n{0}\n\nבצע את השלבים ל-OCR ידני.",
        'instruction_created_voice': "נוצרו הוראות OCR.",
        'ocr_impossible': "OCR אינו אפשרי",
        'ocr_impossible_message': "לא ניתן היה לבצע OCR.\n\nעבד את '{0}' ידנית באמצעות תוכנת OCR.",
        'ocr_impossible_voice': "OCR אינו אפשרי. אנא עבד ידנית.",
        'emergency_title': "OCR חירום",
        'emergency_message': "נוצר PDF חירום:\n\n{0}\n\nאנא עבד קובץ זה ידנית באמצעות OCR.",
        'emergency_voice': "נוצר PDF חירום. אנא בצע OCR ידנית.",
        'critical_error': "שגיאה קריטית",
        'critical_error_message': "לא ניתן היה להפעיל OCR.\n\nהפעל מחדש את התוכנית ובדוק את התקנת OCR.",
        'critical_error_voice': "שגיאת OCR קריטית",
        'ocr_question_html': "<p dir=\"rtl\">ה-PDF אינו מכיל טקסט הניתן לחיפוש.<p dir=\"rtl\">האם ברצונך לבצע OCR כדי לאפשר <b>{0}</b>?</p>",
        'ocr_question_voice': "נדרש OCR. ה-PDF אינו מכיל טקסט הניתן לחיפוש. האם ברצונך לבצע OCR כדי לאפשר {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "לא נטען PDF",
        'no_pdf_message': "לא נטען קובץ PDF",
        'pdf_not_found': "קובץ PDF לא נמצא",
        'file_size': "גודל קובץ",
        'bytes': "בתים",
        'kb': "ק\"ב",
        'mb': "מ\"ב",
        'backup_created': "גיבוי נוצר",
        'backup_disabled': "גיבוי כבוי",
        'backup_activated': "יצירת גיבויים הופעלה",
        'backup_deactivated': "יצירת גיבויים כובתה",
        'backup_status': "גיבוי: {0}",
        'backup_on': "✔ פועל",
        'backup_off': "✘ כבוי",
        'close_pdf': "סוגר PDF: {0}",
        'pdf_not_found_format': "קובץ PDF לא נמצא: {0}",
        'error_pdf_load_format': "שגיאה בטעינת PDF: {0}",
        'load_failed_format': "טעינה נכשלה:\n{0}",
        'decrypted_suffix': "(מפוענח)",
        'decryption_failed': "פענוח נכשל.",
        'decryption_error': "שגיאה בפענוח",
        'decryption_success': "פענוח הצליח",
        'decryption_success_message': "ה-PDF פוענח ונשמר בכתובת:\n\n{0}",
        'decryption_success_voice': "ה-PDF פוענח ונשמר.",
        'password_remove_error': "שגיאה בהסרת הסיסמה",
        'save_unencrypted': "שמור PDF לא מוצפן כ",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "שמור בשם...",
        'save_copy': "שמור עותק",
        'save_success': "PDF נשמר בכתובת: {0}",
        'save_encrypted': "PDF מוגן נשמר בכתובת: {0}",
        'save_error': "לא ניתן היה לשמור את ה-PDF",
        'encryption_question': "האם ברצונך להגן על ה-PDF באמצעות סיסמה?",
        'encryption_yes': "כן",
        'encryption_no': "לא",
        'encryption_cancel': "ביטול",
        'save_cancel': "השמירה בוטלה",
        'save_encrypted_voice': "הקובץ הוצפן ונשמר.",
        'save_success_voice': "קובץ ה-PDF נשמר לא מוצפן.",
        'save_error_format': "לא ניתן היה לשמור את ה-PDF:\n{0}",
        'export_pages_success': "ייצוא ל-Pages הצליח",
        'export_pages_error': "ייצוא ל-Pages נכשל",
        'export_pages_error_format': "ייצוא ל-Pages נכשל: {0}",
        'export_word_success': "ייצוא ל-Word הצליח",
        'export_word_error': "ייצוא ל-Word נכשל",
        'export_word_error_format': "ייצוא ל-Word נכשל: {0}",
        'export_text_success': "ייצוא טקסט הצליח",
        'export_text_error': "ייצוא טקסט נכשל",
        'export_text_error_format': "ייצוא טקסט נכשל: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "נדרשת סיסמה",
        'password_enter': "אנא הכנס סיסמה",
        'password_confirm': "אשר סיסמה",
        'password_new': "סיסמה חדשה",
        'password_current': "סיסמה נוכחית",
        'password_save': "שמור סיסמה (מוצפנת)",
        'password_saved': "✓ הסיסמה לקובץ זה נשמרה",
        'password_wrong': "סיסמה שגויה",
        'password_mismatch': "הסיסמאות אינן תואמות",
        'password_too_short': "הסיסמה קצרה מדי",
        'password_min_length': "הסיסמה חייבת להכיל לפחות 4 תווים",
        'password_strength': "חוזק סיסמה",
        'password_strength_very_weak': "חלש מאוד",
        'password_strength_weak': "חלש",
        'password_strength_medium': "בינוני",
        'password_strength_strong': "חזק",
        'password_strength_very_strong': "חזק מאוד",
        'password_char_count': "({0} תווים)",
        'password_match': "✓ תואם",
        'password_no_match': "✗ הסיסמאות אינן תואמות",
        'password_show': "הצג",
        'password_hide': "הסתר",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "ניהול סיסמאות",
        'password_table_filename': "שם קובץ",
        'password_table_password': "סיסמה",
        'password_count': "{0} סיסמאות שמורות",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "אין סיסמאות שמורות",
        'password_copied': "{0} סיסמאות הועתקו",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "האם אתה בטוח שברצונך למחוק את הסיסמה עבור '{0}'?",
        'password_delete_multiple': "האם אתה בטוח שברצונך למחוק {0} סיסמאות נבחרות?",
        'password_delete_all_confirm': "האם אתה בטוח שברצונך למחוק את כל {0} הסיסמאות השמורות?",
        'password_deleted': "נמחקו {0} סיסמאות",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "כל הסיסמאות נמחקו",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "מחולל סיסמאות",
        'generator_generated': "סיסמה שנוצרה:",
        'generator_regenerate': "צור שוב",
        'generator_copy': "העתק",
        'generator_use': "השתמש",
        'generator_settings': "הגדרות",
        'generator_length': "אורך:",
        'generator_group_every': "מפריד כל",
        'generator_group_chars': "תוים.    מפריד:",
        'generator_uppercase': "אותיות גדולות (A-Z)",
        'generator_lowercase': "אותיות קטנות (a-z)",
        'generator_digits': "ספרות (0-9)",
        'generator_symbols': "סמלים (!@#$%^&*)",
        'generator_exclude': "לא נכלל:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "נדרשת סיסמת אב",
        'master_password_setup': "הגדר סיסמת אב",
        'master_password_change': "שנה סיסמת אב",
        'master_password_enter': "אנא הכנס את סיסמת האב שלך",
        'master_password_choose': "בחר סיסמת אב חזקה (לפחות 8 תווים)",
        'master_password_new': "אנא הכנס את סיסמת האב החדשה שלך",
        'master_password_confirm': "אשר סיסמה",
        'master_password_authenticate': "אמת",
        'master_password_success': "סיסמת האב הוגדרה בהצלחה.",
        'master_password_changed': "סיסמת האב שונתה בהצלחה.",
        'master_password_removed': "סיסמת האב וכל הסיסמאות נמחקו.",
        'master_password_remove': "הסר סיסמת אב",
        'master_password_remove_confirm': "האם אתה בטוח לחלוטין שברצונך למחוק את כל הסיסמאות?\n\nפעולה זו היא בלתי הפיכה!",
        'master_password_export_before': "האם ברצונך לייצא גיבוי לפני כן?",
        'master_password_export_delete': "ייצא ומחק",
        'master_password_delete_now': "מחק עכשיו",
        'master_password_for_signatures': "כדי להשתמש בחתימות, עליך להגדיר סיסמת אב.\n\nהאם ברצונך להגדיר סיסמת אב כעת?",
        'master_password_for_private': "כדי להשתמש בבלוקי טקסט פרטיים, עליך להגדיר סיסמת אב.\n\nהאם ברצונך להגדיר סיסמת אב כעת?",
        'master_password_info': """
            <b>🔐 ללא סיסמת אב:</b><br>
            • לא ניתן להציג, להעתיק ולייצא סיסמאות<br>
            • מחיקת סיסמאות תמיד אפשרית (גם ללא סיסמת אב)<br><br>

            <b>🔐 עם סיסמת אב:</b><br>
            • כל הפונקציות זמינות לאחר אימות<br>
            • סיסמאות מוצפנות באמצעות סיסמת האב<br>
            • אורך מינימלי: 8 תווים<br>
            • אחסון מאובטח של גיבוב SHA-256<br><br>

            <b>חשוב:</b><br>
            • אם תאבד את סיסמת האב, לא ניתן לשחזר סיסמאות<br>
            • בעת הסרת סיסמת האב, כל הסיסמאות יימחקו<br>
            • אפשרות ייצוא זמינה לפני מחיקה<br>
            • ניתן לשנות את סיסמת האב בכל עת
        """,
        'signature_auth_disabled': "השבת בקשת סיסמה לחתימות",
        'template_auth_disabled': "השבת בקשת סיסמה לבלוקי טקסט פרטיים",
        'master_password_for_signatures_settings': "כדי להשתמש בחתימות, עליך להגדיר סיסמת אב.\n\nעבור אל הגדרות - ניהול סיסמאות",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "הגן על PDF",
        'protect_info': "הקובץ '{0}' יוגן באמצעות סיסמה.",
        'protect_instruction': "אנא הכנס את הסיסמה הרצויה פעמיים כדי להגן על המסמך, או השתמש במחולל הסיסמאות מימין לשדה הקלט.",
        'protect_success': "ה-PDF הוגן בהצלחה ונשמר בכתובת:\n{0}\n\nסיסמה: {1}\n\nהאם ברצונך לפתוח את ה-PDF המוגן כעת?",
        'protect_open': "כן",
        'protect_skip': "לא",
        'protect_error': "שגיאה בהגנת ה-PDF",
        'protect_open_title': "פתח PDF מוגן",
        'protect_question': "הסתיים. האם ברצונך לפתוח את ה-PDF המוגן כעת? כן או לא?",
        'password_cancel': "דיאלוג הסיסמה בוטל",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "מחק עמודים",
        'pages_extract': "חלץ עמודים",
        'pages_insert': "הכנס עמודים",
        'pages_move': "הזז עמודים",
        'pages_delete_options': "אפשרויות מחיקה",
        'pages_delete_empty': "מחק את כל העמודים הריקים",
        'pages_delete_current': "מחק עמוד נוכחי",
        'pages_delete_range': "מחק טווח עמודים",
        'pages_extract_options': "אפשרויות חילוץ",
        'pages_extract_current': "חלץ עמוד נוכחי",
        'pages_extract_range': "חלץ טווח עמודים",
        'pages_insert_position': "מיקום הכנסה",
        'pages_insert_before': "הכנס לפני עמוד:",
        'pages_insert_select': "בחר PDF",
        'pages_insert_none': "לא נבחר PDF",
        'pages_move_source': "עמודים להזזה",
        'pages_move_from': "מעמוד:",
        'pages_move_to': "עד עמוד:",
        'pages_move_target': "מיקום יעד",
        'pages_move_before': "הזז לפני עמוד:",
        'pages_move_hint': "הערה: עמוד 1 = התחלה, {0} = סוף",
        'pages_range_invalid': "עמוד ההתחלה חייב להיות קטן או שווה לעמוד הסיום.",
        'pages_position_invalid': "מיקום היעד לא יכול להיות בתוך הטווח המוזז.",
        'pages_no_pdf_selected': "לא נבחר PDF.",
        'pages_deleted': "נמחקו {0} עמודים.",
        'pages_extracted': "חולצו: {0}\nנשמר בכתובת: {1}\nגודל קובץ: {2:.1f} ק\"ב",
        'pages_inserted': "הוכנסו {0} עמודים",
        'pages_moved': "הוזזו {0} עמודים.",
        'pages_deleted_none': "לא נמחקו עמודים.",
        'pages_delete_progress': "מוחק עמודים...",
        'pages_deleted_with_backup': "נמחקו {0} עמודים.\n\nגיבוי: {1}",
        'pages_deleted_voice': "נוצר גיבוי ונמחקו {0} עמודים.",
        'info': "מידע",
        'error_dialog_creation': "לא ניתן היה ליצור דיאלוג",
        'extract_page_single': "חלץ עמוד {0}",
        'extract_page_range': "חלץ עמודים {0}-{1}",
        'extract_success_voice': "עמודים חולצו בהצלחה",
        'extract_error_format': "שגיאה בחילוץ: {0}",
        'pages_inserted_voice': "הוכנסו {0} עמודים.",
        'insert_error_format': "שגיאה בהכנסה: {0}",
        'pages_move_progress': "מזיז עמודים...",
        'pages_moved_with_backup': "הוזזו {0} עמודים.\n\nגיבוי: {1}",
        'move_success_title': "הוזז בהצלחה",
        'pages_moved_voice': "{0} עמודים הוזזו בהצלחה",
        'mark_removed': "הסימון של עמוד {0} הוסר",
        'mark_empty': "עמוד {0} סומן כריק",
        'mark_export_removed': "סימון הייצוא של עמוד {0} הוסר",
        'mark_export': "עמוד {0} סומן לייצוא",
        'no_empty_pages': "אין עמודים ריקים המסומנים למחיקה",
        'delete_empty_confirm': "האם ברצונך למחוק את כל {0} העמודים הריקים המסומנים?",
        'delete_empty_confirm_voice': "למחוק כעת את כל {0} העמודים הריקים המסומנים? כן או לא.",
        'empty_pages_deleted': "נמחקו {0} עמודים ריקים",
        'no_export_pages': "אין עמודים המסומנים לייצוא",
        'overwrite_title': "החלף קובץ קיים",
        'overwrite_question': "הקובץ\n\n{0}\n\nכבר קיים.\nהאם ברצונך להחליפו?",
        'overwrite_voice': "החלף קובץ קיים? כן או לא.",
        'page_skipped': "עמוד {0} דולג",
        'export_complete': "הייצוא הושלם.",
        'export_complete_voice': "הייצוא הושלם.",
        'no_pages_exported': "לא יוצאו עמודים",
        'export_cancelled': "הייצוא בוטל",
        'pages_exported': "{0} עמודים יוצאו אל {1}",
        'export_page_title': "ייצא עמוד",
        'page_exported': "עמוד {0} יוצא אל {1}",
        'export_error': "שגיאה בייצוא",
        'export_marked_title': "ייצא עמודים מסומנים",
        'rotate_all_title': "סובב את כל העמודים",
        'rotate_all_question': "האם ברצונך לסובב את כל העמודים ב-90 מעלות ימינה?",
        'rotate_all_voice': "האם ברצונך לסובב את כל העמודים ב-90 מעלות ימינה? כן או לא?",
        'all_pages_rotated': "כל העמודים סובבו",
        'page_rotated': "עמוד {0} סובב",
        'rotate_error': "לא ניתן היה לסובב את העמוד",
        'delete_page_confirm': "האם ברצונך למחוק את עמוד {0}?",
        'delete_page_confirm_voice': "האם אתה בטוח שברצונך למחוק את עמוד {0}? כן או לא.",
        'page_deleted': "עמוד {0} נמחק",
        'delete_error': "לא ניתן היה למחוק את העמוד",
        'pages_deleted_voice': "{0} עמודים נמחקו",
        'pages_exported_split': "{0} עמודים יוצאו בהצלחה.",
        'pages_skipped': "{0} עמודים דולגו.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "חלץ עמודים (מתקדם)",
        'pdf_splitter_title': "מפצל וחולץ PDF",
        'pdf_splitter_load': " בחר קובץ PDF",
        'pdf_splitter_info': "אנא בחר אפשרות עבור מסמך ה-PDF שלך",
        'pdf_splitter_basic': "פעולות בסיסיות",
        'pdf_splitter_single': "חלק לעמודים בודדים",
        'pdf_splitter_range': "חלץ עמודים:",
        'pdf_splitter_range_placeholder': "לדוגמה 1-3,5,7-9",
        'pdf_splitter_clean': "פעולות ניקוי",
        'pdf_splitter_remove_empty': "הסר את כל העמודים הריקים",
        'pdf_splitter_remove': "מחק טווח עמודים:",
        'pdf_splitter_remove_placeholder': "לדוגמה 2,4-6",
        'pdf_splitter_process': "עבד PDF",
        'pdf_splitter_loaded': "PDF נטען. אנא בחר אפשרות",
        'pdf_read_error': "לא ניתן היה לקרוא את ה-PDF",
        'pages': "עמודים",
        'pages_created': "עמודים נוצרו",
        'range_empty': "אנא הכנס טווח עמודים",
        'range_invalid': "טווח עמודים לא חוקי",
        'range_created': "נוצר PDF חדש עם העמודים הנבחרים:\n{0}",
        'empty_removed': "הוסרו {0} עמודים ריקים.\nפלט: {1}",
        'remove_empty': "אנא הכנס עמודים להסרה",
        'remove_invalid': "עמודים לא חוקיים להסרה",
        'remove_done': "נוצר PDF מנוקה:\n{0}",
        'open_folder': "פתח תיקייה",
        'show_in_finder': "הצג ב-Finder",
        'pdf_splitter_no_pdf': "אנא טען תחילה קובץ PDF.",
        'process_error': "שגיאה בעיבוד ה-PDF",
        'pages_created_voice': "נוצרו {0} עמודים",
        'range_created_voice': "נוצר PDF עם העמודים הנבחרים",
        'empty_removed_voice': "הוסרו {0} עמודים ריקים",
        'remove_done_voice': "נוצר PDF מנוקה",
        'pdf_splitter_split_groups': "כל קבוצה רציפה לקובץ נפרד",
        'range_created_single': "נוצר PDF חדש:\n{0}",
        'range_created_multiple': "נוצרו {0} קבצי PDF.",
        'range_created_voice_single': "נוצר PDF אחד עם העמודים הנבחרים",
        'range_created_voice_multiple': "נוצרו {0} קבצי PDF",
        'empty_removed_none_left': "לא נותרו עמודים",
        'empty_removed_all_empty': "כל העמודים זוהו כריקים והיו מוסרים. לא נוצר קובץ.",
        'preview_single': "תצוגה מקדימה: {0}",
        'preview_enter_range': "אנא הכנס טווח עמודים.",
        'preview_invalid_range': "טווח עמודים לא חוקי.",
        'preview_file': "תצוגה מקדימה: {0}",
        'preview_files': "תצוגה מקדימה: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "מתחיל הדפסה",
        'print_sent': "משימת ההדפסה נשלחה",
        'print_now': "הדפס עכשיו",
        'print_error': "שגיאה בהדפסה מיידית",
        'print_limited': "פונקציית ההדפסה מוגבלת במערכת זו",
        'print_error_format': "שגיאה בהדפסה מיידית: {0}",
        'warning': "אזהרה",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "עבור למצב בהיר",
        'mode_switch_to_dark': "עבור למצב כהה",
        'mode_dark_activated': "מצב כהה הופעל",
        'mode_light_activated': "מצב בהיר הופעל",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "תצוגה מלאה",
        'zoom_two_pages': "שני עמודים זה לצד זה",
        'zoom_overview': "מצב סקירה",
        'zoom_cannot_during_search': "לא ניתן להתקרב במהלך חיפוש",
        'zoom_exit_first': "אנא צא תחילה מהתקריב",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "גרור ושחרר הופעל",
        'drag_disabled': "גרור ושחרר כובה",
        'drag_page_grab': "עמוד {0} נתפס",
        'drag_page_dropped': "עמוד {0} הוכנס במיקום {1}",
        'drag_position_invalid': "מיקום לא חוקי",
        'drag_same_position': "עמוד {0} נשאר במיקום {0}",
        'drag_error': "שגיאה בהזזה",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "הכנס טקסט עם עיצוב מתקדם וניהול בלוקי טקסט",
        'text_templates': "בלוקי טקסט זמינים:",
        'text_name': "שם",
        'text_preview': "תצוגה מקדימה של הטקסט",
        'text_enter': "טקסט:",
        'text_font_size': "גודל גופן:",
        'text_formatting': "עיצוב:",
        'text_bold': "מודגש",
        'text_italic': "נטוי",
        'text_underline': "קו תחתון",
        'text_alignment': "יישור:",
        'text_left': "שמאל",
        'text_center': "מרכז",
        'text_right': "ימין",
        'text_color': "צבע טקסט:",
        'text_opacity': "אטימות:",
        'text_word_wrap': "גלישת שורות:",
        'text_auto': "אוטומטי",
        'text_page_width_95': "רוחב עמוד (95%)",
        'text_page_width_85': "רחב מאוד (85%)",
        'text_page_width_75': "רחב יותר (75%)",
        'text_page_width_60': "רחב (60%)",
        'text_page_width_50': "בינוני (50%)",
        'text_page_width_30': "צר (30%)",
        'text_page_width_20': "צר יותר (20%)",
        'text_page_width_10': "צר מאוד (10%)",
        'text_no_wrap': "ללא גלישה",
        'text_private': "בלוק טקסט פרטי (דורש אימות)",
        'text_preview_label': "תצוגה מקדימה:",
        'text_preview_placeholder': "כאן תוצג תצוגה מקדימה של הטקסט...",
        'text_no_text': "(אין טקסט)",
        'text_save_template': "💾 שמור כבלוק",
        'text_delete_template': "🗑 מחק בלוק טקסט נבחר",
        'text_show_private': "הצג פרטיים",
        'text_hide_private': "הסתר פרטיים",
        'text_use': "✅ השתמש בטקסט",
        'text_saved': "בלוק הטקסט נשמר כ:\n{0}",
        'text_saved_voice': "בלוק הטקסט נשמר",
        'text_deleted': "בלוק הטקסט נמחק",
        'text_no_text_to_save': "אין טקסט לשמירה.",
        'text_no_templates': "לא נמצאו בלוקי טקסט",
        'text_private_master_required': "ניתן להשתמש בבלוקים פרטיים רק אם הוגדרה סיסמת אב.\n\nהאם ברצונך להגדיר סיסמת אב כעת?",
        'text_filename': "שם קובץ לבלוק הטקסט (ללא 'Text_' ו-'.txt'):",
        'text_filename_hint': "דוגמה: 'טלפון משרד ביתי' יישמר כ-'Text_טלפון משרד ביתי.txt'",
        'text_save_hint': "בלוק הטקסט יישמר אוטומטית עם העיצוב.",
        'text_guide_title': "הכנסת טקסט – מדריך",
        'text_delete_confirm': "האם אתה בטוח שברצונך למחוק את בלוק הטקסט?\n\nקובץ: {0}\nטקסט: {1}...",
        'text_make_public': "סמן כציבורי",
        'text_make_private': "סמן כפרטי",
        'text_privacy_changed': "סטטוס הפרטיות שונה",
        'text_private_always': "פרטיים תמיד גלויים (הגדרה)",
        'text_mode_required': "אנא הפעל תחילה מצב טקסט",
        'text_continue_editing': "המשך עריכה – הסמן בסוף הטקסט",
        'text_no_input': "לא הוזן טקסט – הטקסט נמחק",
        'save_dialog_question': "כיצד ברצונך להמשיך?",
        'text_save_question': "לשמור את כל הטקסטים והצלבנות, להתאים, להמשיך בעריכה או למחוק?",
        'copy_cross': "הצלבן הועתק",
        'paste_cross': "הצלבן הודבק",
        'paste_text': "הטקסט הודבק",
        'cross_discarded': "הצלבן נמחק",
        'all_discarded': "הכל נמחק",
        'text_discarded': "הטקסט נמחק",
        'no_texts_to_save': "אין טקסטים לשמירה",
        'no_valid_texts': "אין טקסטים תקפים לשמירה",
        'text_word_singular': "טקסט",
        'text_word_plural': "טקסטים",
        'cross_word_singular': "צלבן",
        'cross_word_plural': "צלבנות",
        'texts_saved_title': "הטקסטים נשמרו",
        'texts_crosses_saved': "{0} {1} ו-{2} {3} הוכנסו ל-PDF.\n\nה-PDF נטען מחדש...",
        'texts_crosses_saved_voice': "{0} {1} ו-{2} {3} נשמרו.",
        'texts_saved': "{0} {1} הוכנסו ל-PDF.\n\nה-PDF נטען מחדש...",
        'texts_saved_voice': "{0} {1} נשמרו.",
        'crosses_saved': "{0} {1} הוכנסו ל-PDF.\n\nה-PDF נטען מחדש...",
        'crosses_saved_voice': "{0} {1} נשמרו.",
        'elements_saved': "{0} אלמנטים הוכנסו ל-PDF.\n\nה-PDF נטען מחדש...",
        'elements_saved_voice': "{0} אלמנטים נשמרו.",
        'text_window_load_error': "לא ניתן היה לטעון את חלון הטקסט",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **הכנסת טקסט ובלוקי טקסט – מדריך מפורט**

        **1. הכנסת טקסט ועריכתו**
        - לחץ לחיצה ימנית במקום הרצוי במסמך ובחר "הכנס טקסט".
        - ייפתח דיאלוג שבו תוכל להזין ולעצב את הטקסט:
        • גודל גופן, מודגש, נטוי, קו תחתון
        • צבע טקסט (בחירה חופשית)
        • שקיפות (אטימות) באמצעות מחוון
        • גלישת שורות (רוחבים שונים, למשל רוחב עמוד, צר, ללא גלישה)
        - לאחר האישור, הטקסט יופיע במקום הלחיצה. תוכל להזיז אותו בעזרת העכבר או מקשי החצים.
        - לחץ פעמיים על הטקסט כדי לפתוח מצב עריכה; ESC יוצא ממנו.

        **2. ניהול בלוקי טקסט (תבניות)**
        - בצד שמאל של דיאלוג הטקסט תראה רשימה של כל בלוקי הטקסט השמורים.
        - **שמירת בלוק:** הזן את הטקסט, עצב אותו ולחץ על "💾 שמור כבלוק". הזן שם קובץ (ללא סיומת).
        - **טעינת בלוק:** לחץ על השם הרצוי ברשימה. הטקסט והעיצוב ייטענו וניתן להתאים אותם במידת הצורך.
        - **מחיקה:** לחץ לחיצה ימנית על בלוק כדי למחוק אותו או לשנות את סטטוס הפרטיות שלו.

        **3. בלוקי טקסט פרטיים (סיסמת אב)**
        - אם הגדרת סיסמת אב (בהגדרות → ניהול סיסמאות), תוכל לסמן בלוקים כ"פרטיים".
        - סמן את התיבה "בלוק טקסט פרטי" בדיאלוג לפני השמירה.
        - בלוקים פרטיים מופיעים ברשימה רק אם הזנת את סיסמת האב שלך פעם אחת בכל סשן (אימות באמצעות סמל המנעול או בגישה הראשונה).
        - כך תוכל להגן על בלוקי טקסט רגישים מפני גישה לא מורשית.

        **4. הכנסת צלבנות**
        - מתפריט ההקשר תוכל גם להכניס צלבן גרפי (למשל לתיבות סימון).
        - ניתן להתאים את הגודל, עובי הקו והצבע של הצלבנות באופן גלובלי בהגדרות (תפריט "הגדרות" → "הגדרות צלבנות").
        - לחץ לחיצה ימנית על צלבן קיים כדי לשנות אותו באופן אישי.

        **5. פעולות קבוצתיות**
        - אם הצבת כמה טקסטים או צלבנות בעמוד אחד, תוכל לשמור או למחוק את כולם יחד מתפריט ההקשר (לחיצה ימנית במצב טקסט).
        - בעת שמירה, כל האלמנטים מוטמעים ב-PDF ונשארים כגרפיקה וקטורית.

        **6. קיצורי מקלדת במצב טקסט**
        - מקשי חצים: הזזת האלמנט
        - Ctrl+מקשי חצים: צעדים גדולים יותר
        - Enter: פתיחת דיאלוג השמירה (שמור הכל / התאם / מחק)
        - ESC: מחיקת האלמנט הנוכחי
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html dir="rtl">
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 הכנסת טקסט ובלוקי טקסט – מדריך מפורט</strong></p>

        <p><strong>1. הכנסת טקסט ועריכתו</strong></p>
        <ul>
        <li>לחץ לחיצה ימנית במקום הרצוי במסמך ובחר "הכנס טקסט".</li>
        <li>ייפתח דיאלוג שבו תוכל להזין ולעצב את הטקסט:<br/>
        • גודל גופן, מודגש, נטוי, קו תחתון<br/>
        • צבע טקסט (בחירה חופשית)<br/>
        • שקיפות (אטימות) באמצעות מחוון<br/>
        • גלישת שורות (רוחבים שונים, למשל רוחב עמוד, צר, ללא גלישה)</li>
        <li>לאחר האישור, הטקסט יופיע במקום הלחיצה. תוכל להזיז אותו בעזרת העכבר או מקשי החצים.</li>
        <li>לחץ פעמיים על הטקסט כדי לפתוח מצב עריכה; ESC יוצא ממנו.</li>
        </ul>

        <p><strong>2. ניהול בלוקי טקסט (תבניות)</strong></p>
        <ul>
        <li>בצד שמאל של דיאלוג הטקסט תראה רשימה של כל בלוקי הטקסט השמורים.</li>
        <li><strong>שמירת בלוק:</strong> הזן את הטקסט, עצב אותו ולחץ על "💾 שמור כבלוק". הזן שם קובץ (ללא סיומת).</li>
        <li><strong>טעינת בלוק:</strong> לחץ על השם הרצוי ברשימה. הטקסט והעיצוב ייטענו וניתן להתאים אותם במידת הצורך.</li>
        <li><strong>מחיקה:</strong> לחץ לחיצה ימנית על בלוק כדי למחוק אותו או לשנות את סטטוס הפרטיות שלו.</li>
        </ul>

        <p><strong>3. בלוקי טקסט פרטיים (סיסמת אב)</strong></p>
        <ul>
        <li>אם הגדרת סיסמת אב (בהגדרות → ניהול סיסמאות), תוכל לסמן בלוקים כ"פרטיים".</li>
        <li>סמן את התיבה "בלוק טקסט פרטי" בדיאלוג לפני השמירה.</li>
        <li>בלוקים פרטיים מופיעים ברשימה רק אם הזנת את סיסמת האב שלך פעם אחת בכל סשן (אימות באמצעות סמל המנעול או בגישה הראשונה).</li>
        <li>כך תוכל להגן על בלוקי טקסט רגישים מפני גישה לא מורשית.</li>
        </ul>

        <p><strong>4. הכנסת צלבנות</strong></p>
        <ul>
        <li>מתפריט ההקשר תוכל גם להכניס צלבן גרפי (למשל לתיבות סימון).</li>
        <li>ניתן להתאים את הגודל, עובי הקו והצבע של הצלבנות באופן גלובלי בהגדרות (תפריט "הגדרות" → "הגדרות צלבנות").</li>
        <li>לחץ לחיצה ימנית על צלבן קיים כדי לשנות אותו באופן אישי.</li>
        </ul>

        <p><strong>5. פעולות קבוצתיות</strong></p>
        <ul>
        <li>אם הצבת כמה טקסטים או צלבנות בעמוד אחד, תוכל לשמור או למחוק את כולם יחד מתפריט ההקשר (לחיצה ימנית במצב טקסט).</li>
        <li>בעת שמירה, כל האלמנטים מוטמעים ב-PDF ונשארים כגרפיקה וקטורית.</li>
        </ul>

        <p><strong>6. קיצורי מקלדת במצב טקסט</strong></p>
        <ul>
        <li>מקשי חצים: הזזת האלמנט</li>
        <li>Ctrl+מקשי חצים: צעדים גדולים יותר</li>
        <li>Enter: פתיחת דיאלוג השמירה (שמור הכל / התאם / מחק)</li>
        <li>ESC: מחיקת האלמנט הנוכחי</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "הגדרות צלבנות",
        'cross_properties': "מאפייני צלבן",
        'cross_size': "גודל (px):",
        'cross_line_width': "עובי קו:",
        'cross_color': "צבע:",
        'cross_choose_color': "בחר",
        'cross_fine_tuning': "כוונון עדין בעת שמירה (פיקסלים)",
        'cross_offset_x': "הסטה X:",
        'cross_offset_y': "הסטה Y:",
        'cross_offset_x_tooltip': "ערכים שליליים מזיזים את הצלבן שמאלה בעת שמירה, חיוביים ימינה",
        'cross_offset_y_tooltip': "ערכים שליליים מזיזים את הצלבן למעלה בעת שמירה, חיוביים למטה",
        'cross_preview': "תצוגה מקדימה",
        'cross_save': "החל הגדרות",
        'cross_customized': "הצלבן הותאם",
        'cross_settings_applied': "הגדרות הצלבנות נשמרו.\nגודל: {0}px, עובי קו: {1}px\n{2}",
        'cross_updated_count': "עודכנו {0} צלבנות קיימות.",
        'cross_no_crosses': "לא נמצאו צלבנות קיימות.",
        'cross_settings_applied_all': "הגדרות הצלבנות הוחלו על כל {0} הצלבנות",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "הגדרות חתימות",
        'signature_1': "חתימה 1",
        'signature_2': "חתימה 2",
        'signature_select': "בחר חתימה",
        'signature_add': "➕ הוסף חתימה חדשה...",
        'signature_size': "גודל לחתימה {0} (%):",
        'signature_common': "הגדרות כלליות",
        'signature_timestamp': "הוסף חותמת זמן אוטומטית",
        'signature_location': "מיקום ברירת מחדל:",
        'signature_timestamp_size': "גודל גופן חותמת זמן:",
        'signature_no_files': "-- לא נמצאו חתימות --",
        'signature_insert': "הכנס חתימה",
        'signature_insert_1': "הכנס חתימה 1",
        'signature_insert_2': "הכנס חתימה 2",
        'signature_customize': " התאם חתימה",
        'signature_discard': " מחק חתימה זו",
        'signature_save_all': " שמור את כל החתימות",
        'signature_discard_all': " מחק את כל החתימות",
        'signature_guide_title': "חתימות – מדריך",
        'signature_guide': """
📝 חתימות – מדריך קצר

- הגדר סיסמת אב
- הגדר את החתימות בתפריט הגדרות
  (גודל, חותמת זמן ...)
- הכנס בלחיצה ימנית במקום הרצוי
  (סיסמת אב נדרשת פעם אחת בכל סשן)
- הזז את החתימה בעזרת העכבר או מקשי החצים
- ניתן להכניס מספר חתימות בזו אחר זו
- כל חתימה ניתנת להתאמה אישית
- מחק חתימה בודדת
- שמור / מחק את כל החתימות בבת אחת
- לחלופין, ניתן להשתמש גם בשורת התפריטים.
        """,
        'signature_placeholder': "תצוגה מקדימה לא זמינה",
        'signature_info': "חתימה {0}: {1}×{2} px ({3}% מ-{4}×{5})",
        'signature_info_placeholder': "הגדרות לחתימה {0}",
        'signature_inserted': "חתימה {0} הוכנסה לעמוד {1}",
        'signature_deleted': "החתימה נמחקה",
        'signature_copied': "החתימה הועתקה",
        'signature_pasted': "חתימה {0} הודבקה",
        'signature_saved': "הוכנסו {0} חתימות ל-PDF.\n\nה-PDF נטען מחדש...",
        'signature_saved_voice': "נשמרו {0} חתימות",
        'mode_replace_signature_format': "צא ממצב והכנס חתימה {0}",
        'mode_conflict_voice_signature': "מצב {0} פעיל. לצאת ולהכניס חתימה?",
        'signature_not_configured': "חתימה {0} לא הוגדרה",
        'signature_file_not_found': "קובץ החתימה לא נמצא",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "אין חתימה מועתקת",
        'no_signatures_to_save': "אין חתימות לשמירה",
        'signature_save_question': "לשמור את כל החתימות, להתאים או למחוק את זו?",
        'signatures_saved_title': "החתימות נשמרו",
        'signatures_saved': "הוכנסו {0} חתימות ל-PDF.\n\nה-PDF נטען מחדש...",
        'signatures_saved_voice': "נשמרו {0} חתימות.",
        'all_signatures_discarded': "כל החתימות נמחקו",
        'signature_settings_saved': "הגדרות החתימות נשמרו",
        'signature_cancelled': "החתימה נמחקה",
        'signature_active_title': "חתימה פעילה",
        'signature_replace_question': "כבר קיימת חתימה פעילה.\n\nהאם ברצונך להחליף את החתימה הנוכחית?",
        'signature_replace': "החלף חתימה",
        'signature_replace_voice': "להחליף את החתימה הנוכחית או לבטל?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "הגדרות תמונות",
        'image_common': "הגדרות כלליות לתמונות",
        'image_keep_aspect': "שמור יחס גובה-רוחב בעת גרירה",
        'image_default_size': "גודל ברירת מחדל (%):",
        'image_dark_invert': "הפוך תמונות במצב כהה",
        'image_dark_invert_tooltip': "פעיל: תמונות מתהפכות לראות טובה יותר",
        'image_fine_tuning': "כוונון עדין (פיקסלים)",
        'image_offset_x': "הסטה X:",
        'image_offset_y': "הסטה Y:",
        'image_offset_x_tooltip': "ערכים שליליים מזיזים את התמונה שמאלה בעת שמירה, חיוביים ימינה",
        'image_offset_y_tooltip': "ערכים שליליים מזיזים את התמונה למעלה בעת שמירה, חיוביים למטה",
        'image_select': "בחר תמונה",
        'image_insert': "הכנס תמונה",
        'image_customize': " התאם תמונה",
        'image_aspect': " שמור יחס גובה-רוחב",
        'image_discard': " מחק תמונה זו",
        'image_save_all': " שמור את כל התמונות",
        'image_discard_all': " מחק את כל התמונות",
        'image_filter': "תמונות",
        'image_guide_title': "הכנסת תמונות – מדריך",
        'image_guide': """
📷 הכנסת תמונות ל-PDF – מדריך קצר:

1. לחץ לחיצה ימנית במקום הרצוי
2. "הכנס תמונה" → בחר תמונה
3. מקם את התמונה: גרור בעזרת העכבר
4. התאם גודל: גרור בפינות/קצוות
5. שמור יחס גובה-רוחב: מקש [A]
6. התאמות נוספות: לחץ לחיצה ימנית על התמונה

טיפ: בתפריט ההקשר תוכל להתאים את ההגדרות.
        """,
        'image_inserted': "תמונה הוכנסה לעמוד {1}",
        'image_deleted': "התמונה נמחקה",
        'image_copied': "התמונה הועתקה",
        'image_pasted': "התמונה הודבקה",
        'image_saved': "הוכנסו {0} תמונות ל-PDF.\n\nה-PDF נטען מחדש...",
        'image_saved_voice': "נשמרו {0} תמונות",
        'image_aspect_on': "פעיל",
        'image_aspect_off': "כבוי",
        'image_aspect_toggle': "שמור יחס גובה-רוחב {0}",
        'image_reset': "התמונה הוחזרה לגודל המקורי",
        'image_replaced': "התמונה הוחלפה",
        'image_invalid': "תמונה לא חוקית",
        'mode_replace_image': "הכנס תמונה",
        'mode_conflict_voice_image': "מצב {0} פעיל. לצאת ולהכניס תמונה?",
        'image_active_title': "תמונה פעילה",
        'image_replace_question': "כבר קיימת תמונה פעילה.\n\nהאם ברצונך להחליף את התמונה הנוכחית?",
        'image_replace': "החלף תמונה",
        'image_replace_voice': "להחליף את התמונה הנוכחית או לבטל?",
        'image_filter_all': "תמונות (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;כל הקבצים (*.*)",
        'no_copied_image': "אין תמונה מועתקת",
        'image_discarded': "התמונה נמחקה",
        'image_save_question': "לשמור את כל התמונות, להתאים או למחוק את זו?",
        'no_images_to_save': "אין תמונות לשמירה",
        'no_valid_images': "אין תמונות תקפות לשמירה",
        'images_saved_title': "התמונות נשמרו",
        'images_saved': "הוכנסו {0} תמונות ל-PDF.\n\nה-PDF נטען מחדש...",
        'images_saved_voice': "נשמרו {0} תמונות.",
        'all_images_discarded': "כל התמונות נמחקו",
        'image_settings_updated': "הגדרות התמונות עודכנו",
        'image_replace_title': "בחר תמונה חדשה",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "הגדרות צורות",
        'form_basic': "הגדרות בסיסיות",
        'form_default_type': "סוג צורת ברירת מחדל:",
        'form_rectangle': "מלבן",
        'form_ellipse': "אליפסה",
        'form_line': "קו",
        'form_arrow': "חץ",
        'form_line_width': "עובי קו:",
        'form_colors': "צבעים",
        'form_line_color': "צבע קו:",
        'form_fill_color': "צבע מילוי:",
        'form_choose_color': "בחר",
        'form_transparent': "רקע שקוף (קו בלבד)",
        'form_filled': "ממולא",
        'form_dark_mode': "מצב כהה",
        'form_dark_invert': "הפוך צבעים במצב כהה",
        'form_fine_tuning': "כוונון עדין (פיקסלים)",
        'form_offset_x': "הסטה X:",
        'form_offset_y': "הסטה Y:",
        'form_offset_x_tooltip': "ערכים שליליים מזיזים את הצורה שמאלה בעת שמירה, חיוביים ימינה",
        'form_offset_y_tooltip': "ערכים שליליים מזיזים את הצורה למעלה בעת שמירה, חיוביים למטה",
        'form_preview': "תצוגה מקדימה",
        'form_insert': "הכנס צורה",
        'form_rectangle_insert': "מלבן",
        'form_ellipse_insert': "אליפסה/עיגול",
        'form_line_insert': "קו (2 לחיצות)",
        'form_arrow_insert': "חץ (2 לחיצות)",
        'form_customize': " התאם צורה",
        'form_transparent_toggle': " רקע שקוף",
        'form_discard': " מחק צורה זו",
        'form_save_all': " שמור את כל הצורות",
        'form_discard_all': " מחק את כל הצורות",
        'form_guide_title': "הכנסת צורות – מדריך",
        'form_guide': """
📐 הכנסת צורות ל-PDF – מדריך קצר:

1. בחר סוג צורה (מלבן, אליפסה, קו, חץ)
2. לחץ במקום
   - מלבן/אליפסה: לחיצה אחת ממקמת את הצורה
   - קו/חץ: שתי לחיצות לנקודת התחלה וסיום
3. מקם את הצורה: גרור בעזרת העכבר
4. התאם גודל: גרור בפינות/קצוות
5. שמור צורה: Enter
6. מחק צורה: ESC
7. התאמות נוספות: לחץ לחיצה ימנית על הצורה

טיפ: בתפריט ההקשר תוכל להתאים את ההגדרות.
        """,
        'form_inserted': "{0} הוכנס לעמוד {1}",
        'form_deleted': "הצורה נמחקה",
        'form_copied': "הצורה הועתקה",
        'form_pasted': "הצורה הודבקה",
        'form_saved': "הוכנסו {0} צורות ל-PDF.\n\nה-PDF נטען מחדש...",
        'form_saved_voice': "נשמרו {0} צורות",
        'form_reset': "הצורה הוחזרה לגודל ברירת המחדל",
        'form_transparent_on': "פעיל",
        'form_transparent_off': "כבוי",
        'form_transparent_toggled': "רקע שקוף {0}",
        'form_line_cancel': "ציור הקו בוטל",
        'form_second_click': "כעת לחץ על נקודת הסיום עבור {0}",
        'mode_replace_form': "הכנס צורה",
        'mode_conflict_voice_form': "מצב {0} פעיל. לצאת ולהכניס צורה?",
        'form_settings_updated': "הגדרות הצורות עודכנו",
        'form_unknown': "צורה",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. לחץ על נקודת ההתחלה",
        'form_line_guide_2': "2. לחץ על נקודת הסיום",
        'form_line_guide_3': "הקו יצויר בין שתי הנקודות.",
        'form_line_status_1': "ממתין ללחיצה ראשונה...",
        'form_line_status_2': "הנקודה הראשונה הוגדרה: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "כעת לחץ על נקודת הסיום...",
        'form_line_status_4': "שתי הנקודות הוגדרו.\nלחץ 'סיום' כדי לשמור.",
        'form_line_reset': "אפס",
        'form_line_finish': "סיום",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "העתק (Cmd+C)",
        'paste': "הדבק (Cmd+V)",
        'copied': "הועתק: {0}",
        'no_element_to_copy': "לא נבחר אלמנט להעתקה",
        'no_copied_data': "אין נתונים מועתקים",
        'no_valid_position': "אין מיקום תקף להדבקה",
        'copy_text': "הטקסט הועתק",
        'copy_image': "התמונה הועתקה",
        'copy_form': "הצורה הועתקה",
        'copy_signature': "החתימה הועתקה",
        'element_text': "טקסט",
        'element_image': "תמונה",
        'element_form': "צורה",
        'element_signature': "חתימה",
        'element_unknown': "אלמנט",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "התנגשות מצבים",
        'mode_conflict_message': "המצב '{0}' כבר פעיל.\n\nהאם ברצונך לצאת ממנו ו{1}?",
        'mode_replace': "צא ממצב ו{0}",
        'mode_cancel': "ביטול",
        'mode_replace_text': "להכניס טקסט",
        'mode_replace_cross': "להכניס צלבן",
        'mode_replace_signature': "להכניס חתימה",
        'mode_replace_image': "להכניס תמונה",
        'mode_replace_form': "להכניס צורה",
        'mode_conflict_voice': "מצב {0} פעיל. לצאת ולהכניס טקסט?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "הכנסת טקסט",
        'active_mode_signature': "חתימה",
        'active_mode_image': "תמונה",
        'active_mode_form': "צורה",
        'active_mode_and': " ו",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "הכנס",
        'insert_another_text': "הכנס טקסט",
        'insert_another_cross': "הכנס צלבן",
        'insert_another_signature_1': "חתימה 1",
        'insert_another_signature_2': "חתימה 2",
        'insert_another_image': "הכנס תמונה",
        'insert_another_form_rect': "מלבן",
        'insert_another_form_ellipse': "אליפסה",
        'insert_another_form_line': "קו (2 לחיצות)",
        'insert_another_form_arrow': "חץ (2 לחיצות)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "שמור {0}",
        'save_dialog_message': "{0} יישמר בעמוד {1}.\n\nכיצד ברצונך להמשיך?",
        'save_all': "שמור את כל {0}",
        'save_single': "שמור {0}",
        'save_customize': "התאם {0}",
        'save_discard': "מחק {0} זה",
        'save_continue': "המשך עריכה",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " עבור לעמוד {0}",
        'context_rotate': " סובב עמוד {0}",
        'context_delete': " מחק עמוד {0}",
        'context_export': " ייצא עמוד {0}",
        'context_mark_as': " סמן עמוד כ...",
        'context_mark_empty': " עמוד ריק",
        'context_unmark_empty': " לא ריק יותר",
        'context_mark_export': " סמן לייצוא",
        'context_unmark_export': " אל תייצא יותר",
        'context_batch_actions': " פעולות קבוצתיות",
        'context_batch_delete_empty': " מחק את כל {0} העמודים הריקים",
        'context_batch_export_single': " ייצא את כל {0} העמודים (קובץ אחד)",
        'context_batch_export_split': " ייצא את כל {0} העמודים (בנפרד)",
        'context_drag_start': " התחל גרור ושחרר",
        'context_drag_stop': " סיים גרור ושחרר",
        'context_insert': " הכנס",
        'context_insert_pages': " הכנס עמודים",
        'context_zoom': "תקריב",
        'discard_mixed': "מחק את כל {0} {1} ו-{2} {3}",
        'save_mixed': "שמור {0} {1} ו-{2} {3}",
        'discard_texts': "מחק את כל {0} הטקסטים",
        'discard_text_single': "מחק טקסט 1",
        'save_texts': "שמור {0} טקסטים",
        'save_text_single': "שמור טקסט 1",
        'discard_crosses': "מחק את כל {0} הצלבנות",
        'discard_cross_single': "מחק צלבן 1",
        'save_crosses': "שמור {0} צלבנות",
        'save_cross_single': "שמור צלבן 1",
        'discard_signatures': "מחק את כל {0} החתימות",
        'save_signature_single': "שמור חתימה 1",
        'save_signatures': "שמור {0} חתימות",
        'discard_images': "מחק את כל {0} התמונות",
        'save_image_single': "שמור תמונה 1",
        'save_images': "שמור {0} תמונות",
        'discard_forms': "מחק את כל {0} הצורות",
        'save_form_single': "שמור צורה 1",
        'save_forms': "שמור {0} צורות",
        'cross_discard': "מחק צלבן זה",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 מידע על ייצוא/ייבוא",
        'export_what': "📋 מה מיוצא?",
        'export_general': "הגדרות כלליות",
        'export_general_items': "• פלט קולי (פעיל/כבוי, מהירות)\n• מצב כהה/בהיר\n• הגדרות גיבוי\n• הגדרות OCR",
        'export_image_form': "הגדרות תמונות וצורות",
        'export_image_form_items': "• הגדרות תמונות (יחס גובה-רוחב, גודל ברירת מחדל)\n• הגדרות צורות (עובי קו, צבעים)\n• הגדרות חתימות (נתיבים, גדלים, חותמת זמן)",
        'export_passwords': "מסד נתונים של סיסמאות",
        'export_passwords_items': "• כל סיסמאות ה-PDF השמורות\n• לפי בחירה מוצפנות או מפוענחות",
        'export_master': "הגדרות סיסמת אב",
        'export_master_items': "• גיבוב סיסמת אב\n• הגדרות לחתימות/בלוקי טקסט",
        'export_signatures': "חתימות ובלוקי טקסט",
        'export_signatures_items': "• כל קבצי התמונות (חתימות)\n• כל בלוקי הטקסט עם עיצוב\n• סימונים פרטיים/ציבוריים",
        'export_import_warning': "⚠️ הערות חשובות",
        'export_import_note': "• בעת ייבוא, כל ההגדרות הנוכחיות יוחלפו\n• נדרשת הפעלה מחדש של האפליקציה\n• חתימות/בלוקי טקסט קיימים יוחלפו",
        'export_master_note': "• אם הוגדרה סיסמת אב, תוכל לבחור:\n  - מפוענח (סיסמאות בטקסט ברור)\n  - מוצפן (קריא רק עם סיסמת אב)",
        'export_security': "• קובץ ה-ZIP המיוצא מכיל נתונים רגישים\n• שמור אותו במקום בטוח (למשל ב-USB מוצפן)\n• אם תאבד את הקובץ, הסיסמאות יאבדו לנצח",
        'export_format': "📁 פורמט ייצוא",
        'export_format_desc': "ההגדרות נשמרות בקובץ ZIP אחד:",
        'export_filename': "הגדרות_PDFDarkView_YYYYMMDD_HHMMSS.zip",
        'export_success': "ההגדרות יוצאו בהצלחה",
        'export_failed': "הייצוא נכשל",
        'export_import_question': "האם ברצונך להפעיל מחדש את האפליקציה כעת?",
        'export_password_question': "הוגדרה סיסמת אב.\n\nהאם ברצונך לייצא את הסיסמאות מפוענחות?\n(אחרת הן ייוצאו מוצפנות)",
        'export_decrypt': "ייצא מפוענח",
        'export_encrypt': "ייצא מוצפן",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " מידע",
        'info_title': "אודות PDF Dark View",
        'info_version': "גרסה",
        'info_author': "פותח על ידי טורלף שולץ (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "אודות",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> הוא מציג PDF נגיש, שפותח במיוחד עבור אנשים עם לקות ראייה.</p>

            <p><strong>תכונות עיקריות:</strong></p>
            <ul>
                <li>ממשק עתיר ניגודיות, ניתן להתאמה אישית</li>
                <li>שליטה מלאה באמצעות מקלדת</li>
                <li>הקראה קולית מובנית</li>
                <li>OCR למסמכים סרוקים</li>
                <li>כלי עריכה מקיפים</li>
            </ul>

            <p>נתמכות יותר מ-50 שפות – כך שקובצי PDF נגישים לכולם.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "תכונות",
        'info_features_intro': "PDF Dark View מציע לך את האפשרויות הבאות:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>תצוגה וניווט</strong> – מצב כהה/בהיר, דפדוף בעמודים, זום, קפיצה לעמוד</li>
            <li><strong>OCR (זיהוי טקסט)</strong> – הפוך מסמכים סרוקים לניתנים לחיפוש והעתקה</li>
            <li><strong>עריכה</strong> – הוספת טקסט, סימני X, חתימות, תמונות וצורות</li>
            <li><strong>ניהול עמודים</strong> – מחיקה, חילוץ, הוספה, הזזה באמצעות גרירה ושחרור</li>
            <li><strong>ייצוא</strong> – ל-Word, Pages או כטקסט</li>
            <li><strong>אבטחה</strong> – הגנה וניהול באמצעות סיסמה</li>
            <li><strong>נגישות</strong> – הקראה קולית, שליטה באמצעות מקלדת, ניגודיות גבוהה</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "תפעול",
        'info_accessibility': "♿ נגישות – שליטה מלאה באמצעות מקלדת",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 כללי</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> פתיחת PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> חיפוש</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> החלפה בין מצב כהה/בהיר</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> הדפסה</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> יציאה</div>

        <div class="shortcut-cat">📖 ניווט</div>
        <div class="shortcut-row"><kbd>מקשי חצים</kbd> דפדוף עמוד אחר עמוד</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> מעבר לעמוד</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> עמוד ראשון</div>
        <div class="shortcut-row"><kbd>Ende</kbd> עמוד אחרון</div>

        <div class="shortcut-cat">✏️ עריכה</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> הוספת טקסט</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> מחיקת עמודים</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> חילוץ עמודים</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> הוספת עמודים</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> הזזת עמודים</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> סיבוב עמוד</div>

        <div class="shortcut-cat">🖼️ הזזת אלמנטים</div>
        <div class="shortcut-row"><kbd>מקשי חצים</kbd> הזזת טקסט/תמונה/חתימה</div>
        <div class="shortcut-row"><kbd>Ctrl+מקשי חצים</kbd> צעדים גדולים יותר</div>
        <div class="shortcut-row"><kbd>Enter</kbd> שמירה</div>
        <div class="shortcut-row"><kbd>ESC</kbd> ביטול</div>

        <div class="shortcut-cat">🗣️ הקראה קולית</div>
        <div class="shortcut-row"><kbd>F2</kbd> הפעלה/כיבוי של ההקראה הקולית</div>
        """,
        'info_contextmenu': "📌 חשוב: כל הפונקציות זמינות גם דרך תפריט ההקשר (לחצן עכבר ימני)!",
        'info_accessibility_hint': "💡 טיפ: ההקראה הקולית (F2) מקלה על ההתמצאות ומספקת משוב על תפריטים ודיאלוגים.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "רישיון & אימפרסום",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 אימפרסום</strong><br>
        מידע לפי § 5 TMG:<br>
        טורלף שולץ<br>
        Schusterstraße 3, 65582 Diez, גרמניה<br>
        דוא"ל: binhdiez64@gmail.com<br>
        אחראי על התוכן: טורלף שולץ (BinhDiez)<br><br>

        <strong>⚠️ כתב ויתור</strong><br>
        התוכנה פותחה בקפדנות רבה. לא ניתנת כל אחריות על נכונות, שלמות ותפקוד. השימוש הוא על אחריות המשתמש בלבד.<br><br>

        <strong>📄 רישיון MIT (שימוש פרטי)</strong><br>
        זכויות יוצרים (c) 2026 טורלף שולץ (BinhDiez)<br>
        מותר: שימוש חופשי, שינויים פרטיים, עותקים אישיים.<br>
        אסור: מכירה, שימוש מסחרי, הסרת הודעות זכויות יוצרים.<br><br>

        <strong>🔧 רכיבי צד שלישי</strong><br>
        תוכנה זו מכילה רכיבים תחת רישיונות GPL, AGPL, Apache 2.0, BSD ו-MIT.<br>
        בעת הפצה חוזרת, יש לעמוד בתנאי הרישיון המתאימים.<br><br>

        <strong>🌐 קוד פתוח</strong><br>
        קוד המקור זמין וניתן לצפייה, שינוי והפצה חוזרת בהתאם לתנאי הרישיון המתאימים.<br><br>

        © 2026 טורלף שולץ (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "תודות",
        'info_credits': "תודה לקהילת הקוד הפתוח",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – עיבוד PDF</li>
            <li><strong>PyQt5</strong> – ממשק גרפי</li>
            <li><strong>Tesseract OCR</strong> – זיהוי טקסט</li>
            <li><strong>OCRmyPDF</strong> – שילוב OCR</li>
            <li><strong>python-docx</strong> – ייצוא ל-Word</li>
            <li><strong>qtawesome</strong> – אייקונים</li>
            <li><strong>DeepSeek</strong> – תמיכה בתרגומים (50+ שפות)</li>
            <li><strong>כל המשתמשים</strong> – על משוב יקר ערך</li>
            <li><strong>קהילת הקוד הפתוח</strong> – על ספריות נהדרות</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "שפות",
        'info_languages_header': "🌍 תמיכה בשפות",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View תומך כרגע ב-<strong>62 שפות</strong> – כך שניתן להשתמש בתוכנה ללא מחסומים ברחבי העולם.</p>

            <p><strong>📖 רשימת שפות מלאה (נכון למרץ 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 אפריקאנס</li>
                    <li>🇦🇱 אלבנית (Shqip)</li>
                    <li>🇩🇿 ערבית (العربية)</li>
                    <li>🇮🇩 באלינזית (Basa Bali)</li>
                    <li>🇧🇩 בנגלית (বাংলা)</li>
                    <li>🇲🇲 בורמזית (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 בוסנית (Bosanski)</li>
                    <li>🇧🇬 בולגרית (Български)</li>
                    <li>🇨🇳 סינית (中文)</li>
                    <li>🇩🇰 דנית (Dansk)</li>
                    <li>🇩🇪 גרמנית (Deutsch)</li>
                    <li>🇬🇧 אנגלית (English)</li>
                    <li>🇪🇪 אסטונית (Eesti)</li>
                    <li>🇫🇮 פינית (Suomi)</li>
                    <li>🇫🇷 צרפתית (Français)</li>
                    <li>🇬🇷 יוונית (Ελληνικά)</li>
                    <li>🇮🇱 עברית (עברית)</li>
                    <li>🇮🇳 הינדית (हिन्दी)</li>
                    <li>🇭🇷 קרואטית (Hrvatski)</li>
                    <li>🇭🇺 הונגרית (Magyar)</li>
                    <li>🇮🇩 אינדונזית (Bahasa Indonesia)</li>
                    <li>🇮🇪 אירית (Gaeilge)</li>
                    <li>🇮🇸 איסלנדית (Íslenska)</li>
                    <li>🇮🇹 איטלקית (Italiano)</li>
                    <li>🇯🇵 יפנית (日本語)</li>
                    <li>🇰🇭 חמרית (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 קוריאנית (한국어)</li>
                    <li>🇱🇦 לאית (ພາສາລາວ)</li>
                    <li>🇱🇻 לטבית (Latviešu)</li>
                    <li>🇱🇹 ליטאית (Lietuvių)</li>
                    <li>🇱🇺 לוקסמבורגית (Lëtzebuergesch)</li>
                    <li>🇲🇾 מלאית (Bahasa Melayu)</li>
                    <li>🇮🇳 מראטהית (मराठी)</li>
                    <li>🇲🇳 מונגולית (Монгол)</li>
                    <li>🇳🇵 נפאלית (नेपाली)</li>
                    <li>🇳🇱 הולנדית (Nederlands)</li>
                    <li>🇳🇴 נורווגית (Norsk)</li>
                    <li>🇦🇤פתו (پښتو)</li>
                    <li>🇮🇷 פרסית (فارسی)</li>
                    <li>🇵🇱 פולנית (Polski)</li>
                    <li>🇵🇹 פורטוגזית (Português)</li>
                    <li>🇮🇳 פנג'אבית (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 רומנית (Română)</li>
                    <li>🇷🇺 רוסית (Русский)</li>
                    <li>🇸🇪 שוודית (Svenska)</li>
                    <li>🇷🇸 סרבית (Српски)</li>
                    <li>🇸🇰 סלובקית (Slovenčina)</li>
                    <li>🇸🇮 סלובנית (Slovenščina)</li>
                    <li>🇪🇸 ספרדית (Español)</li>
                    <li>🇹🇿 סוואהילית (Kiswahili)</li>
                    <li>🇵🇭 טגלוג (Filipino)</li>
                    <li>🇮🇳 טמילית (தமிழ்)</li>
                    <li>🇮🇳 טלוגו (తెలుగు)</li>
                    <li>🇹🇭 תאילנדית (ไทย)</li>
                    <li>🇨🇿 צ'כית (Čeština)</li>
                    <li>🇹🇷 טורקית (Türkçe)</li>
                    <li>🇺🇦 אוקראינית (Українська)</li>
                    <li>🇵🇰 אורדו (اردو)</li>
                    <li>🇻🇳 וייטנאמית (Tiếng Việt)</li>
                    <li>🇸🇳 וולוף (Wolof)</li>
                    <li>🇺🇸 יידיש (ייִדיש)</li>
                    <li>🇿🇦 זולו (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 הוספת שפות משלך:</strong><br>
                רוצה שפה שעדיין לא כלולה? פשוט הנח את קובץ המילון שלך (<code>sprache_xx.py</code>) לצד היישום – התוכנה תזהה אותו אוטומטית. אם אתה מעוניין בתרגום ספציפי, אל תהסס ליצור איתי קשר.
            </div>

            <p><strong>🙏 תודה מיוחדת:</strong> ל-DeepSeek על התמיכה בתרגום כל המילונים ל-62 שפות.</p>

            <p>📧 יצירת קשר לתרגומים: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "שגיאה",
        'error_occurred': "אירעה שגיאה",
        'error_pdf_load': "שגיאה בטעינת PDF",
        'error_pdf_save': "שגיאה בשמירת PDF",
        'error_ocr': "שגיאה בזיהוי טקסט",
        'error_no_pdf': "לא נטען PDF",
        'error_page_not_found': "העמוד לא נמצא",
        'error_invalid_range': "טווח עמודים לא חוקי",
        'error_file_not_found': "הקובץ לא נמצא",
        'error_permission': "אין הרשאה",
        'error_unknown': "שגיאה לא ידועה",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "הצלחה",
        'success_operation': "הפעולה הושלמה בהצלחה",
        'success_saved': "נשמר בהצלחה",
        'success_exported': "יוצא בהצלחה",
        'success_imported': "יובא בהצלחה",
        'success_deleted': "נמחק בהצלחה",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "אישור",
        'confirm_yes': "כן",
        'confirm_no': "לא",
        'confirm_ok': "אישור",
        'confirm_cancel': "ביטול",
        'confirm_delete': "מחק",
        'confirm_overwrite': "החלף",
        'confirm_continue': "המשך",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "טוען PDF...",
        'progress_saving': "שומר PDF...",
        'progress_exporting': "מייצא PDF...",
        'progress_processing': "מעבד...",
        'progress_wait': "אנא המתן...",
        'progress_preparing': "מכין...",
        'progress_finalizing': "מסיים...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "לבן",
        'color_black': "שחור",
        'color_red': "אדום",
        'color_green': "ירוק",
        'color_blue': "כחול",
        'color_yellow': "צהוב",
        'color_magenta': "מג'נטה",
        'color_cyan': "ציאן",
        'color_orange': "כתום",
        'color_gray': "אפור",
        'color_custom': "בחירת צבע",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&קובץ",
        'menu_edit': "&עריכה",
        'menu_view': "&תצוגה",
        'menu_tools': "&כלים",
        'menu_settings': "&הגדרות",
        'menu_help': "&עזרה",
        'menu_language': "🌐 שפה",
        'menu_guides': "&מדריכים",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&פתח",
        'file_save_as': "&שמור בשם...",
        'file_protect': "&הגן על מסמך...",
        'file_export': "&ייצא",
        'file_export_pages': "ייצא ל-Pages",
        'file_export_word': "ייצא ל-DOCX",
        'file_export_text': "ייצא ל-TXT",
        'file_print_now': "&הדפס עכשיו",
        'file_print': "&הדפס",
        'file_close': "&סגור",
        'file_quit': "&צא",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&חפש",
        'edit_ocr': " בצע OCR",
        'edit_rotate': "&סובב עמוד",
        'edit_rotate_all': "סובב את &כל העמודים",
        'edit_delete_pages': "&מחק עמודים",
        'edit_extract_pages': "&חלץ עמודים",
        'edit_insert_pages': "&הכנס עמודים",
        'edit_move_pages': "&הזז עמודים",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " הכנס טקסט וצלבנות",
        'text_insert': " הכנס טקסט",
        'cross_insert': " הכנס צלבן",
        'text_customize': " התאם טקסט",
        'cross_customize': " התאם צלבן זה",
        'cross_customize_all': " התאם את כל הצלבנות",
        'text_discard': " מחק טקסט/צלבן זה",
        'text_discard_all': " מחק את כל הטקסטים והצלבנות",
        'text_save_all': " שמור את כל הטקסטים והצלבנות",
        'text_guide': " הכנסת טקסט / בלוקי טקסט – מדריך",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " הכנס חתימה",
        'signature_settings_menu': " הגדרות...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " הכנס תמונה",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " הכנס צורות",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&הצג חלון טקסט",
        'view_zoom': "&תקריב",
        'view_zoom_page': "&רוחב עמוד (ברירת מחדל)",
        'view_zoom_two': "&שני עמודים",
        'view_zoom_overview': "&סקירה (עמודים מרובים)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&נגישות",
        'settings_voice': "פלט קולי",
        'settings_voice_tooltip': "משלים את הפלט הקולי של קוראי מסך במידע נוסף",
        'settings_signature': "&הגדרות חתימות",
        'settings_password': "&ניהול סיסמאות",
        'settings_backup': "צור גיבוי לפני שינויים",
        'settings_export_import': "&ייצא הגדרות / ייבא הגדרות",
        'settings_export': "&ייצא את כל ההגדרות...",
        'settings_import': "&ייבא את כל ההגדרות...",
        'settings_export_info': "&מה מיוצא?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "פעיל",
        'voice_off': "כבוי",
        'voice_toggle': "פלט קולי {0}",
        'voice_speed': "מהירות {0} אחוז",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "הכלי לא נמצא:\n{0}\n\nBASE_DIR: {1}\nודא שכלי PDF מותקנים בספרייה {1}.",
        'tool_started': "{0} הופעל",
        'tool_start_failed': "לא ניתן היה להפעיל",
        'process_error_failed_to_start': "לא ניתן היה להפעיל את התהליך. האם הקובץ קיים?",
        'process_error_crashed': "התהליך קרס בעת ההפעלה.",
        'process_error_timeout': "הגיע למגבלת הזמן של התהליך.",
        'process_error_write': "שגיאת כתיבה בתהליך.",
        'process_error_read': "שגיאת קריאה מהתהליך.",
        'process_error_unknown': "שגיאת תהליך לא ידועה",
        'process_command': "פקודה",
        'process_normal_exit': "הסתיים כרגיל",
        'process_crashed': "קרס",
        'process_nonzero_exit': "{0} הסתיים עם קוד שגיאה {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "מבטל...",
        'move_cancelling': "מבטל הזזה",
        'opening_pdf': "פותח PDF...",
        'loading_document': "טוען מסמך...",
        'pdf_opened': "PDF נפתח",
        'pages_found_moving': "נמצאו {0} עמודים, {1} להזזה",
        'creating_backup': "יוצר גיבוי...",
        'backup_description': "מגבה קובץ מקורי...",
        'backup_saved_as': "הגיבוי נשמר כ: {0}",
        'error_format': "שגיאה: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView מאת BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "החיפוש אופס",
        'page_header_simple': "=== עמוד {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "ניהול סיסמאות – מדריך",
        'password_guide_voice': "מדריך לניהול סיסמאות. אנא קרא את ההערות.",
        'password_guide_html': """
        <html dir="rtl">
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 ניהול סיסמאות – מדריך מפורט</strong></p>

        <p><strong>1. הגנה על PDF באמצעות סיסמה</strong></p>
        <ul>
        <li>בעת פתיחת PDF המוגן בסיסמה, יופיע דיאלוג שבו תוכל להזין את הסיסמה.</li>
        <li>תוכל לשמור את הסיסמה מוצפנת כדי שלא תצטרך להזין אותה בכל פעם (תיבת סימון "שמור סיסמה").</li>
        <li>באמצעות הלחצן "הסר סיסמה" תוכל ליצור עותק מפוענח של ה-PDF ולמחוק את הסיסמה ממסד הנתונים.</li>
        </ul>

        <p><strong>2. סיסמת אב</strong></p>
        <ul>
        <li>סיסמת האב מגנה על הגישה לכל סיסמאות ה-PDF השמורות.</li>
        <li><strong>הגדרה:</strong> עבור אל "הגדרות → ניהול סיסמאות → הגדרות סיסמת אב" ולחץ על "הגדר סיסמת אב". בחר סיסמה חזקה (לפחות 8 תווים).</li>
        <li><strong>שינוי:</strong> לאחר אימות מוצלח, תוכל לשנות את סיסמת האב.</li>
        <li><strong>הסרה:</strong> אם תסיר את סיסמת האב, כל הסיסמאות השמורות יימחקו באופן בלתי הפיך. תוכל לייצא גיבוי לפני כן.</li>
        <li>פעם אחת בכל סשן, עליך לאמת את עצמך באמצעות סיסמת האב כדי לגשת לפונקציות המוגנות (למשל הצגת סיסמאות).</li>
        </ul>

        <p><strong>3. ניהול סיסמאות (רשימה)</strong></p>
        <ul>
        <li>ב"הגדרות → ניהול סיסמאות" נפתחת טבלה של כל קבצי ה-PDF השמורים עם הסיסמאות המוצפנות שלהם.</li>
        <li><strong>ללא סיסמת אב:</strong> תוכל רק למחוק רשומות – הסיסמאות נותרות מוסתרות.</li>
        <li><strong>עם סיסמת אב (מאומת):</strong> תוכל להציג, להעתיק, לייצא ולמחוק סיסמאות.</li>
        <li><strong>ייצוא:</strong> בחר פורמט (JSON, CSV, TXT) ושמור את הרשימה. אם הוגדרה סיסמת אב, תוכל לבחור אם הסיסמאות ייוצאו מפוענחות או מוצפנות.</li>
        <li><strong>ייבוא:</strong> ניתן לייבא קובץ ZIP שיוצא בעבר (כל ההגדרות) דרך "הגדרות → ייצוא הגדרות / ייבוא הגדרות". אזהרה: נתונים קיימים יוחלפו!</li>
        </ul>

        <p><strong>4. מחולל סיסמאות</strong></p>
        <ul>
        <li>בדיאלוג הסיסמה (למשל בעת הגנה על PDF), מימין לשדה הקלט נמצא לחצן קובייה 🎲.</li>
        <li>לחץ עליו כדי לפתוח את מחולל הסיסמאות. תוכל להגדיר אורך, קבוצות תווים (אותיות גדולות, אותיות קטנות, ספרות, סמלים) ומפריד לקריאות טובה יותר.</li>
        <li>ניתן להשתמש בסיסמה שנוצרה ישירות ולהעתיק אותה במידת הצורך.</li>
        </ul>

        <p><strong>5. הערות אבטחה חשובות</strong></p>
        <ul>
        <li>סיסמאות שמורות נשמרות מוצפנות באמצעות AES-256. המפתח נגזר מסיסמת האב שלך (אם הוגדרה) או מערך קבוע (ללא סיסמת אב).</li>
        <li>ללא סיסמת אב, הסיסמאות אמנם מוצפנות, אך המפתח מוטבע בתוכנה – תוקף עם גישה לקבצים שלך עלול לפענח אותן. לכן אנו ממליצים בחום להשתמש בסיסמת אב.</li>
        <li>מסד הנתונים של הסיסמאות נמצא בקובץ `Data/passwords.json`. צור גיבויים באופן קבוע, במיוחד לפני הסרת סיסמת האב.</li>
        <li>אם תאבד את סיסמת האב, כל הסיסמאות השמורות יאבדו לנצח.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "מצב היפוך",
        'invert_mode_classic': "קלאסי (היפוך כל הצבעים)",
        'invert_mode_smart': "חכם (היפוך בהירות בלבד)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "סף גווני אפור",
        'gray_threshold_10': "10% (קפדני)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (ברירת מחדל)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (רך)",
        'threshold_changed': "הסף נקבע ל-{0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "סף גווני אפור – הסבר",
        'threshold_guide_text': "סף גווני האפור קובע אילו פיקסלים במצב הכהה החכם נחשבים 'אפורים' ומתהפכים.\n\n"
                                "• ערך נמוך (10%) הופך רק גווני אפור כמעט מושלמים – אלמנטים צבעוניים נשמרים לחלוטין.\n"
                                "• ערך גבוה (50%) הופך גם פיקסלים צבעוניים מעט – זה מגדיל את הניגודיות, אך עלול לעוות צבעים.\n\n"
                                "הערך האופטימלי תלוי במסמך. עבור מסמכי טקסט טהורים, 30-40% הוא לרוב אידיאלי, עבור גרפיקה צבעונית עדיף 10-20%.\n\n"
                                "אתה יכול להתאים את הערך בכל עת דרך תפריט 'הגדרות' – קובץ ה-PDF ייטען מחדש מיד.\n\n"
                                "שימו לב:\n* ניתן להציג תמונות וצילומים כראוי רק במצב בהיר!\n* הגדרות ההיפוך מוצגות רק כאשר מצב כהה מופעל.",
        'threshold_guide_voice': "סף גווני האפור קובע עד כמה המצב הכהה החכם מתערב. ערך נמוך שומר על צבעים, ערך גבוה מגביר ניגודיות.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "פתיחת PDF...",
        'progress_loading_document': "טעינת מסמך...",
        'progress_pdf_opened': "PDF נפתח",
        'progress_creating_backup': "יצירת גיבוי...",
        'progress_backup_description': "אבטחת הקובץ המקורי...",
        'progress_backup_created': "גיבוי נוצר",
        'progress_backup_saved_as': "נשמר כ: {0}",
        'progress_analyzing_start': "התחלת ניתוח...",
        'progress_searching_empty': "חיפוש עמודים ריקים...",
        'progress_page_empty': "עמוד {0} ריק",
        'progress_page_keep': "שמירת עמוד {0}",
        'progress_analysis_complete': "הניתוח הושלם",
        'progress_empty_found': "נמצאו {0} עמודים ריקים",
        'progress_current_page': "עמוד נוכחי",
        'progress_mark_delete': "מסומן למחיקה",
        'progress_range_selected': "טווח עמודים {0}-{1}",
        'progress_deleting_pages': "מחיקת {0} עמודים",
        'progress_creating_new_pdf': "יצירת PDF חדש...",
        'progress_transferring_pages': "העברת עמודים",
        'progress_keeping_page': "עמוד {0} יישמר ({1}/{2})",
        'progress_saving_pdf': "שמירת PDF...",
        'progress_optimizing': "אופטימיזציה של גודל הקובץ...",
        'progress_finalizing': "השלמה...",
        'progress_new_size': "גודל חדש: {0:.2f} MB",
        'progress_cancelling': "מתבטל...",
        'progress_cancel_message': "{0} מתבטל",
        'progress_pages_found_moving': "נמצאו {0} עמודים, {1} להזזה",

        # OCR-Fortschritt
        'ocr_status_analyzing': "ניתוח PDF...",
        'ocr_status_optimizing': "אופטימיזציית תמונה מתבצעת...",
        'ocr_status_recognizing': "זיהוי טקסט מתבצע...",
        'ocr_status_embedding': "הטבעת טקסט...",
        'ocr_status_finalizing': "השלמת PDF...",

        # PDF-Laden
        'progress_preparing': "הכנה...",
        'progress_loading': "טעינת PDF...",

        # Seitenoperationen
        'progress_deleting_title': "מחיקת עמודים...",
        'progress_moving_title': "הזזת עמודים...",
        'pages_found': "עמודים נמצאו",
        'progress_creating_new_order': "יצירת סדר חדש...",
        'progress_sorting_pages': "מיון עמודים...",
        'progress_moving_to_begin': "הזזת {0} עמודים להתחלה",
        'progress_transferring_count': "העברת {0} עמודים",
        'progress_transferring_before_target': "העברת עמודים לפני היעד",
        'progress_moving_pages': "הזזת {0} עמודים",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_גיבוי_",
        'filename_protected_suffix': "_מוגן_",
        'filename_copy_suffix': "_עותק",
        'filename_page_single': "_עמוד_",
        'filename_page_range': "_עמודים_",
        'filename_export_page': "_עמוד_{0:03}",
        'filename_export_range': "_עמודים_{0}-{1}",
        'filename_export_multiple': "_עמודים_{0}",
        'filename_with_text': "_עם_טקסט",
        'filename_with_signature': "_עם_חתימה",
        'filename_with_image': "_עם_תמונה",
        'filename_with_forms': "_עם_צורות",
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
        'view_toggle_navbar': "הצג סרגל כפתורים",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "לא ניתן למחוק את כל הדפים",
		'pages_cannot_delete_last_page': 'לא ניתן למחוק את העמוד האחרון!',
		'pages_cannot_delete_all_pages': 'חייב להישאר לפחות עמוד אחד במסמך!',
		'delete_pages_confirm': 'האם אתה בטוח שברצונך למחוק {0} עמודים?',
		'delete_pages_confirm_voice': 'האם אתה בטוח שברצונך למחוק {0} עמודים?',
		'pages_deleted': '{0} עמודים נמחקו בהצלחה.',
		'warning': 'אזהרה',
		'error': 'שגיאה',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "לא נבחר טופס",
        'form_customized': "הטופס הותאם אישית",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "בחר",
        'btn_use': "השתמש",
        'master_password_for_spasswords': "כדי לאחסן ולהשתמש בסיסמאות, תחילה יש להגדיר סיסמת אב.\n\nהאם ברצונך להגדיר סיסמת אב כעת?",
        'open_saved_dialog_title': "פתיחת קובץ שמור",
        'open_saved_question': "האם ברצונך לפתוח את הקובץ השמור כעת?",
        'password': "סיסמה",
        'password_manager_master_required': "מנהל הסיסמאות זמין רק אם הוגדרה סיסמת אב.\n\nהאם ברצונך להגדיר סיסמת אב כעת?",
        'password_master_required_for_select': "כדי להציג ולבחור סיסמאות שמורות, עליך קודם כל לאמת את עצמך עם סיסמת האב שלך.\n\nהאם ברצונך לאמת כעת?",
        'password_not_available': "הסיסמה שנבחרה אינה זמינה או לא ניתן לפענח אותה.",
        'password_options_title': "אפשרויות סיסמה",
        'password_save_choice_change': "הגדר סיסמה חדשה",
        'password_save_choice_keep': "השתמש בסיסמה קיימת",
        'password_save_choice_none': "שמור ללא הצפנה",
        'password_save_hint': "הגדר תחילה סיסמת אב כדי לאחסן סיסמאות בצורה מאובטחת.",
        'password_save_master_required': "שמור סיסמה (אפשרי רק עם סיסמת אב)",
        'password_save_question': "ה-PDF הנוכחי מוגן בסיסמה. האם ברצונך להשתמש בסיסמה הקיימת, להגדיר חדשה או לשמור ללא הצפנה?",
        'password_select': "בחר סיסמה",
        'password_select_none': "לא נבחרה סיסמה.\n\nאנא בחר סיסמה מהרשימה.",
        'password_select_one': "אנא בחר סיסמה אחת בדיוק.\n\nסימנת מספר סיסמאות.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_גיבוי",
        'filename_insert_suffix': "_עם_הוספה",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_דפים_נמחקו",
        'filename_pages_moved': "_דפים_הועברו",
        'filename_rotated_all_suffix': "_כל_הדפים_הוסבו",
        'filename_rotated_suffix': "_דף_הוסב",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "הגדרת שמות קבצים בעת שינוי PDF",
        'filename_keep_suffixes': "שמור סיומות קודמות (למשל _עם_טקסט)",
        'filename_keep_suffixes_false': "החלף",
        'filename_keep_suffixes_true': "שמור",
        'filename_preview_label': "תצוגה מקדימה של שם הקובץ:",
        'filename_preview_overwrite_hint': "תצוגה מקדימה לא זמינה – המקור יידרס.",
        'filename_separator': "מפריד בין מילים",
        'filename_separator_none': "ללא מפריד",
        'filename_separator_space': "רווח ( )",
        'filename_separator_underscore': "קו תחתון (_)",
        'filename_settings_saved': "הגדרות שם הקובץ נשמרו",
        'filename_settings_title': "עיצוב שם קובץ וגיבוי",
        'filename_timestamp_position': "מיקום חותמת הזמן",
        'filename_timestamp_position_after': "אחרי השם הבסיסי",
        'filename_timestamp_position_before': "מלפנים",
        'filename_timestamp_position_end': "בסוף",
        'filename_use_timestamp': "השתמש בחותמת זמן",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>התנהגות בעת שינויים:</b><ul><li>מחיקה והוספה של דפים</li><li>הוספת טקסט, חתימה, תמונה וצורות</li><li>OCR</li></ul></html>",
        'backup_section': "גיבוי לפעולות דף (מחיקה, העברה)",
        'behavior_info': "הערה: ב'דריסת מקור' מתעלמים מחותמות זמן וסיומות – הקובץ שומר על שמו.",
        'behavior_new_file': "צור תמיד קובץ חדש (עם חותמת זמן וסיומת)",
        'behavior_overwrite': "דרוס מקור (ללא קובץ חדש)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "כל הדפים הוסבו.\n\nהמקור נותר ללא שינוי.\nקובץ חדש: {0}",
        'all_pages_rotated_voice': "כל הדפים הוסבו, נוצר קובץ חדש.",
        'empty_pages_deleted_new_file': "{0} דפים ריקים נמחקו.\n\nהמקור נותר ללא שינוי.\nקובץ חדש: {1}",
        'empty_pages_deleted_voice': "{0} דפים ריקים נמחקו, נוצר קובץ חדש.",
        'ocr_keep_original': "שמור מקור (פתח ידנית מאוחר יותר)",
        'ocr_new_file_question': "ה-PDF החדש הניתן לחיפוש נשמר תחת:\n{0}\n\nהאם ברצונך לפתוח אותו כעת?",
        'ocr_open_new': "פתח קובץ OCR חדש",
        'ocr_original_kept': "הקובץ המקורי נשאר פתוח. קובץ ה-OCR נשמר.",
        'page_deleted_new_file': "דף {0} נמחק.\n\nהמקור נותר ללא שינוי.\nקובץ חדש: {1}",
        'page_deleted_voice': "דף {0} נמחק, נוצר קובץ חדש.",
        'page_rotated_new_file': "דף {0} הוסב.\n\nהמקור נותר ללא שינוי.\nקובץ חדש: {1}",
        'page_rotated_voice': "דף {0} הוסב, נוצר קובץ חדש.",
        'pages_deleted_new_file': "נמחקו {0} דפים.\n\nהקובץ המקורי נותר ללא שינוי.\nקובץ חדש: {1}",
        'pages_deleted_new_file_voice': "{0} דפים נמחקו, נוצר קובץ חדש.",
        'pages_inserted_new_file': "הוספו {0} דפים.\n\nהקובץ המקורי נותר ללא שינוי.\nקובץ חדש: {1}",
        'pages_inserted_new_file_ask': "הוספו {0} דפים.\n\nהמקור נותר ללא שינוי.\nקובץ חדש: {1}\n\nהאם ברצונך לפתוח אותו כעת?",
        'pages_inserted_voice_new': "{0} דפים הוספו, נוצר קובץ חדש.",
        'pages_moved_new_file': "הועברו {0} דפים.\n\nהקובץ המקורי נותר ללא שינוי.\nקובץ חדש: {1}",
        'pages_moved_new_file_voice': "{0} דפים הועברו, נוצר קובץ חדש.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "אל תציג שוב",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 הגדרת גיבוי</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ גיבוי פעיל</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">בכל השינויים שדורסים את המקור</strong> (טקסט, חתימה, תמונה, צורה, OCR, היפוך, הוספה, מחיקה/העברת דפים) נוצר <strong>אוטומטית גיבוי עם חותמת זמן</strong> לפני החלת השינוי.</p>
                <p style="margin: 5px 0 5px 20px;">• הגיבוי נמצא לצד הקובץ המקורי (למשל <code>מסמך_גיבוי_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• אם בנוסף לכך הפעלת את האפשרות <strong>„דרוס מקור“</strong>, נוצר גם גיבוי.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 גיבוי כבוי</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>לא נוצר גיבוי</strong> – לא בעת דריסה ולא בעת פעולות דף.</p>
                <p style="margin: 5px 0 5px 20px;">• הקובץ המקורי עלול ללכת לאיבוד באופן בלתי הפיך בעת דריסה.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">מומלץ רק למשתמשים מנוסים!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>טיפ:</strong> הגדרת הגיבוי אינה תלויה באפשרות „דרוס מקור“. ניתן לשלב בין שניהם.<br>
                ניתן להסתיר הודעה זו לצמיתות.
            </div>
        </div>
        """,
        'backup_info_title': "התנהגות גיבוי",
        'backup_info_voice': "הודעה על התנהגות הגיבוי בפעולות דף. גיבוי פעיל דורס את המקור, גיבוי כבוי יוצר קובץ חדש.",
        'show_backup_info': "מידע על הגדרת גיבוי",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "אל תציג שוב",
        'overwrite_enable_backup': "הפעל גיבוי (מומלץ)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ דרוס מקור</p>
            <p>אם תפעיל אפשרות זו, שינויים (טקסט, חתימה, תמונה, צורה, OCR, היפוך, הוספה) נשמרים <strong>ישירות במקור</strong> – <strong>לא נוצר קובץ חדש</strong>.</p>
            <p>• שם הקובץ נשאר ללא שינוי.<br>
            • מתעלמים מחותמות זמן וסיומות.<br>
            • <strong>ללא גיבוי, המקור עלול ללכת לאיבוד באופן בלתי הפיך.</strong></p>
            <p style="color: #FFD700;">המלצה: הפעל בנוסף את אפשרות הגיבוי כדי לקבל עותקי גיבוי אוטומטיים.</p>
        </div>
        """,
        'overwrite_info_title': "דרוס מקור",
        'overwrite_info_voice': "אזהרה: דרוס מקור – ללא קובץ חדש. גיבוי מומלץ.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "הוספו {0} דפים.\n\nהקובץ המקורי נדרס.\nנוצר גיבוי.",
        'pages_inserted_overwrite_no_backup': "הוספו {0} דפים.\n\nהקובץ המקורי נדרס.\nלא נוצר גיבוי.",
        'texts_saved_overwrite_with_backup': "השינויים נשמרו במקור.\n\nנוצר גיבוי.",
        'texts_saved_overwrite_no_backup': "השינויים נשמרו במקור.\n\nלא נוצר גיבוי.",
        'texts_crosses_saved_new_file': "{0} {1} ו-{2} {3} הוספו.\n\nהקובץ המקורי נותר ללא שינוי.\nנוצר קובץ חדש.\n\nה-PDF החדש נטען...",
        'texts_saved_new_file': "{0} {1} הוספו.\n\nהקובץ המקורי נותר ללא שינוי.\nנוצר קובץ חדש.\n\nה-PDF החדש נטען...",
        'crosses_saved_new_file': "{0} {1} הוספו.\n\nהקובץ המקורי נותר ללא שינוי.\nנוצר קובץ חדש.\n\nה-PDF החדש נטען...",
        'elements_saved_new_file': "{0} רכיבים הוספו.\n\nהקובץ המקורי נותר ללא שינוי.\nנוצר קובץ חדש.\n\nה-PDF החדש נטען...",
        'signatures_saved_overwrite_with_backup': "החתימה/ות נשמרה/ו במקור.\n\nנוצר גיבוי.",
        'signatures_saved_overwrite_no_backup': "החתימה/ות נשמרה/ו במקור.\n\nלא נוצר גיבוי.",
        'images_saved_overwrite_with_backup': "התמונה/ות נשמרה/ו במקור.\n\nנוצר גיבוי.",
        'images_saved_overwrite_no_backup': "התמונה/ות נשמרה/ו במקור.\n\nלא נוצר גיבוי.",
        'forms_saved_overwrite_with_backup': "הצורה/ות נשמרה/ו במקור.\n\nנוצר גיבוי.",
        'forms_saved_overwrite_no_backup': "הצורה/ות נשמרה/ו במקור.\n\nלא נוצר גיבוי.",
        'signatures_saved_new_file': "{0} חתימות הוספו.\n\nהקובץ המקורי נותר ללא שינוי.\nנוצר קובץ חדש.\n\nה-PDF החדש נטען...",
        'images_saved_new_file': "{0} תמונות הוספו.\n\nהקובץ המקורי נותר ללא שינוי.\nנוצר קובץ חדש.\n\nה-PDF החדש נטען...",
        'forms_saved_new_file': "{0} צורות הוספו.\n\nהקובץ המקורי נותר ללא שינוי.\nנוצר קובץ חדש.\n\nה-PDF החדש נטען...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "אזהרה: קובץ PDF זה מכיל דפים מוסבים. המיקום עלול להיות שונה.",
        'page_rotated_warning_title': "זוהה דף מוסב",
        'page_rotated_warning_message': "הדף הנוכחי {0} הוסב ב-{1}°.\n\nהוספת רכיבים על דפים מוסבים אינה נתמכת.\n\nהאם ברצונך להסב את הדף כעת למצב זקוף?",
        'page_rotated_warning_voice': "אזהרה: הדף מוסב. אנא הסב אותו תחילה.",
        'paste_on_rotated_page_simple_warning': "לא ניתן להוסיף על דף {0}!\n\nדף זה הוסב ב-{1}°.\n\nאנא הסב תחילה את הדף ל-0° (תפריט: עריכה → יישר דף).\n\nאזהרה:\nהרכיב שהועתק קודם יאבד אם לא תשמור לפני היפוך הדף.",
        'paste_on_rotated_page_voice': "ההוספה בוטלה. הדף מוסב. אנא יישר את הדף תחילה.",
        'page_rotated_cancel': "ביטול",
        'page_rotated_rotate_until_upright': "הסב דף שוב ושוב (עד שיהיה זקוף)",
        'page_rotated_now_upright': "הדף כעת זקוף. כעת ניתן להוסיף.",
        'page_rotated_still_not_upright': "לא ניתן היה להסב את הדף למצב זקוף. אנא תקן ידנית.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "עזרה: תיקון דפים מוסבים",
        'help_rotated_pages_voice': "נפתחת עזרה לתיקון דפים מוסבים.",
        'btn_help': "עזרה",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 בעיה: דף מוסב – ההוספה אינה פועלת כראוי</p>

            <p>אם הוספת טקסטים, חתימות או צורות על דף מוסב אינה פועלת כראוי, ניתן לתקן את הדף באמצעות עורך PDF חיצוני.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ פתרון עם כלי חיצוני (למשל macOS Preview)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>ייצא דף</strong><br>
                &nbsp;&nbsp;לחץ בתפריט על <strong>קובץ → ייצא כדפים</strong> או השתמש בשיטה אחרת כדי לשמור את הדף הרצוי כ-PDF בודד.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>פתח דף בתוכנה חיצונית</strong><br>
                &nbsp;&nbsp;פתח את ה-PDF המיוצא בעורך PDF (למשל <strong>macOS Preview</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>הסב דף</strong><br>
                &nbsp;&nbsp;הסב את הדף כך שיהיה זקוף (ב-Preview: <strong>כלים → הסב</strong> או <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>שמור</strong><br>
                &nbsp;&nbsp;שמור את הדף המתוקן (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>הוסף שוב את הדף למסמך המקורי</strong><br>
                &nbsp;&nbsp;חזור ל-PDFDarkView והוסף את הדף המתוקן במיקום הרצוי:<br>
                &nbsp;&nbsp;<strong>עריכה → הוסף דפים</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 אלטרנטיבה: הסב דף במקור</p>
                <p style="margin: 5px 0 5px 20px;">• השתמש בפונקציית ההיפוך המובנית (<strong>עריכה → הסב דף</strong>) כדי לתקן את הדף שלב אחר שלב.<br>
                • לאחר כל היפוך תוכל לבדוק האם ההוספה פועלת כעת.<br>
                • זהו לעתים קרובות הפתרון המהיר יותר – נסה אותו תחילה!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>טיפ:</strong> אם אתה נתקל לעתים קרובות בדפים מוסבים, תוכל להסתיר לצמיתות את האזהרה בדיאלוג ההוספה.<br>
                המיקום עלול אז להיות שונה – השתמש באפשרות זו רק אם אתה מכיר את ההשלכות.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "יישר דפים",
        'menu_rotate_normalize_tooltip': "הסב דף או אפס ל-0°",
        'normalize_current_page': "הבא את הדף הנוכחי למצב זקוף (הגדר ל-0°)",
        'normalize_all_pages': "הבא את כל הדפים למצב זקוף (הגדר ל-0°)",
        'page_normalized': "דף {0} הוגדר למצב זקוף.",
        'all_pages_normalized': "כל הדפים הוגדרו למצב זקוף.",
        'page_already_upright': "דף {0} כבר זקוף.",
        'all_pages_already_upright': "כל הדפים כבר זקופים.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>ה-PDF אינו מכיל טקסט שניתן לחיפוש.</p><p>האם ברצונך לבצע OCR כדי לייצא ל-{0}?</p>",
        'export_ocr_voice': "ה-PDF אינו מכיל טקסט. יש צורך ב-OCR לייצוא ל-{0}.",
        'export_no_ocr_possible': "ייצוא ללא OCR אינו אפשרי. אנא בצע OCR דרך התפריט.",
        'ocr_failed_export_not_possible': "OCR נכשל. לא ניתן לבצע ייצוא.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "ה-PDF ייפתח ב-Preview. אנא התחל את תהליך ההדפסה שם.",
        'print_preview_manual': "ה-PDF נפתח. אנא בצע את פקודת ההדפסה ידנית (למשל Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "מיזוג PDFs",
        'merge_pdfs': "מיזוג PDFs",
        'merge_progress_title': "ממזג PDFs...",
        'merge_pdfs_list': "PDFs בסדר (גרור ושחרר למיון)",
        'merge_add_pdf': "הוסף PDF",
        'merge_remove': "הסר",
        'merge_move_up': "למעלה",
        'merge_move_down': "למטה",
        'merge_pdfs_info': "💡 טיפ: ניתן לשנות את הסדר באמצעות גרירה ושחרור",
        'merge_no_pdfs': "לא נבחרו PDFs. לחץ על 'הוסף PDF'.",
        'merge_info': "{0} PDFs נבחרו (כ-{1} דפים)",
        'merge_open_file': "פתח קובץ",
        'merge_merge': "מזג",
        'merge_error': "שגיאה בעת מיזוג",
        'merge_min_two_pdfs_error': "אנא בחר לפחות שני קבצי PDF למיזוג.",
        'merge_select_pdfs': "בחר PDFs למיזוג",
        'merge_error_file': "שגיאה בעת עיבוד",
        'merge_cancelled': "המיזוג בוטל",
        'merge_preparing': "מתכונן...",
        'merge_processing': "מעבד PDF {0} מתוך {1}",
        'merge_saving': "שומר PDF ממוזג...",
        'merge_complete': "הושלם!",
        'merge_success_title': "המיזוג הצליח",
        'merge_success_voice': "{0} PDFs מוזגו בהצלחה.",
        'merge_success_message': "{0} PDFs מוזגו בהצלחה.\n\nהמסמך החדש מכיל כעת {1} דפים.\n\nקובץ חדש:\n{2}\n\nמיקום שמירה:\n{3}\n{2}\n\nהאם ברצונך לפתוח PDF זה?",
        'replace_file_title': "להחליף קובץ?",
        'replace_file_message': "כבר פתוח PDF. האם ברצונך להחליף אותו בקובץ החדש?",
        'btn_yes': "כן",
        'btn_no': "לא",
        'filename_merge_suffix': "ממוזג",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "פותח {0}...",
        'progress_merge_reading': "קורא {0}...",
        'progress_merge_adding': "מוסיף {0} דפים...",
        'progress_merge_optimizing': "מייעל PDF...",
        'progress_merge_writing': "כותב PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "סגירת ה-PDF",
        'action_close_window': "סגירת החלון",
        'action_open_new_pdf': "פתיחת PDF חדש",
        'action_quit_app': "יציאה מהיישום",
        'changes_saved': "השינויים נשמרו.",
        'file_close_title': "סגור קובץ PDF",
        'save_before_action': "האם יש לשמור את השינויים לפני {0}? כן או לא?",
        'save_before_action_voice': "האם יש לשמור את השינויים לפני {0}? כן או לא?",
        'save_before_close_question': "האם יש לשמור את השינויים לפני הסגירה? כן או לא?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>נוצר PDF הניתן לחיפוש:\n\n{0}\n\n<b>נסה שוב במידת הצורך",
        "ocr_rotate_title": "יישור דפים לפני OCR",
        "ocr_rotate_question": "ה-PDF מכיל דפים מסובבים.\nהאם ברצונך לישר את כל הדפים ל-0° לפני OCR?\nפעולה זו משפרת משמעותית את זיהוי הטקסט.",
        "ocr_rotate_yes": "כן, יישר",
        "ocr_rotate_no": "לא, התחל OCR ישירות",
        "ocr_rotate_voice": "ה-PDF מכיל דפים מסובבים. האם יש לישר את כל הדפים לפני OCR?",
        "ocr_not_performed_message": "אין טקסט קיים. אנא בצע OCR (תפריט \"עריכה\" → \"בצע OCR\" או מקש Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "הגדרות OCR",
        "ocr_language_btn": "בחר שפת OCR",
        "ocr_language": "שפת(ות) OCR",
        "ocr_language_current": "שפה נוכחית:",
        "ocr_param_info": "מידע על הפרמטר",

        "ocr_force_ocr_label": "כפיית OCR",
        "ocr_deskew_label": "תיקון הטיה",
        "ocr_clean_label": "ניקוי תמונה",
        "ocr_oversample_label": "רזולוציה (DPI)",
        "ocr_pagesegmode_label": "פילוח דף",
        "ocr_oem_label": "מצב מנוע OCR",
        "ocr_optimize_label": "דחיסת PDF",
        "ocr_jobs_label": "תהליכים מקביליים",
        "ocr_verbose_label": "פירוט יומן",

        "ocr_force_ocr_tooltip": "כפיית OCR על כל דף, גם אם טקסט כבר קיים",
        "ocr_deskew_tooltip": "יישור אוטומטי של סריקות מוטות",
        "ocr_clean_tooltip": "הסרת רעש וארט�קטים מהתמונה",
        "ocr_oversample_tooltip": "הגדלת תמונה לפני OCR ל-DPI זה",
        "ocr_pagesegmode_tooltip": "קובע כיצד הדף מחולק לאזורי טקסט",
        "ocr_oem_tooltip": "בוחר את מנוע ה-OCR של Tesseract",
        "ocr_optimize_tooltip": "רמת דחיסה של PDF הפלט",
        "ocr_jobs_tooltip": "מספר תהליכי OCR מקביליים",
        "ocr_verbose_tooltip": "רמת פירוט של פלט היומן",
        "ocr_settings_explain_btn": "הסבר",

        "ocr_force_ocr_explain": "כופה זיהוי טקסט על <b>כל</b> דף, גם אם הוא כבר מכיל טקסט.\n\nהמלצה: <b>מופעל</b> עבור PDF סרוקים, <b>מושבת</b> עבור PDF מקוריים עם טקסט קיים.",

        "ocr_deskew_explain": "מתקן סריקות המוטות מעט (עד כ-5°).\n\nהמלצה: <b>מופעל</b> עבור מסמכים סרוקים, <b>מושבת</b> אם הדפים כבר ישרים לחלוטין.",

        "ocr_clean_explain": "מסיר רעש, נקודות וארט�קטים קטנים מהתמונה.\n<b>חשוב:</b> עבור טקסטים ערביים, תאילנדיים או וייטנאמיים עם סימנים דיאקריטיים (נקודות מעל/מתחת לאותיות) יש <b>להשבית</b> אפשרות זו, אחרת תווים חשובים עלולים ללכת לאיבוד.",

        "ocr_oversample_explain": "מגדיל את התמונה <b>לפני</b> זיהוי הטקסט ל-DPI שצוין.<br><br>• <b>72-150 DPI:</b> מהיר מאוד, אך שיעור זיהוי נמוך<br>• <b>200-300 DPI:</b> טווח אופטימלי (ברירת מחדל: 300)<br>• <b>400+ DPI:</b> בקושי זיהוי טוב יותר, אך קבצים גדולים משמעותית<br><br>המלצה: 300 DPI עבור כתבים מורכבים (ערבית, סינית, יפנית), 200 DPI עבור שפות מערביות.",

        "ocr_pagesegmode_explain": "קובע כיצד Tesseract מחלק את הדף לאזורי טקסט.\n\n• <b>3 - אוטומטי (ברירת מחדל):</b> טוב לפריסות מעורבות\n• <b>4 - עמודה בודדת:</b> עבור טקסטים בעמודה אחת\n• <b>5 - בלוק אנכי:</b> עבור כתבים אנכיים (יפנית, סינית)\n• <b>6 - בלוק טקסט אחיד:</b> אופטימלי עבור טקסט זורם ללא עמודות\n• <b>11 - תמונה גולמית:</b> עבור סריקות גרועות / כתב יד\n\nהמלצה: <b>6</b> עבור מסמכי טקסט פשוטים, <b>3</b> עבור פריסות מורכבות.",

        "ocr_oem_explain": "בוחר את מנוע ה-OCR של Tesseract.\n\n• <b>0 - Legacy:</b> מנוע ישן (מהיר, אך פחות מדויק)\n• <b>1 - LSTM:</b> מנוע עצבי (איטי יותר, אך מדויק יותר)\n• <b>2 - Legacy + LSTM:</b> משלב את שתי התוצאות\n• <b>3 - ברירת מחדל (LSTM מועדף):</b> הבחירה הטובה ביותר עבור רוב המקרים\n\nהמלצה: <b>3</b> עבור דיוק זיהוי מרבי.",

        "ocr_optimize_explain": "דוחס את PDF הפלט.\n\n• <b>0:</b> ללא אופטימיזציה (עיבוד מהיר ביותר)\n• <b>1:</b> אופטימיזציה קלה (פשרה טובה)\n• <b>2:</b> אופטימיזציה מתונה\n• <b>3:</b> אופטימיזציה חזקה (קובץ קטן ביותר, אך איטי יותר)\n\nהמלצה: <b>1</b> לשימוש יומיומי.",

        "ocr_jobs_explain": "מספר תהליכים מקביליים עבור OCR.\n\n• <b>1:</b> איטי, אך צריכת הזיכרון הנמוכה ביותר\n• <b>4-8:</b> אופטימלי עבור מעבדים מרובי ליבות מודרניים\n• <b>12+:</b> בקושי עיבוד מהיר יותר עם צריכת זיכרון גבוהה\n\nהמלצה: מספר ליבות CPU (למשל <b>4</b> במערכות 4 ליבות).",

        "ocr_verbose_explain": "רמת פירוט של פלט היומן במסוף.\n\n• <b>0:</b> ללא פלט\n• <b>1:</b> התקדמות והודעות מצב\n• <b>2:</b> פלט מפורט\n• <b>3:</b> פלט ניפוי שגיאות מלא (נרחב מאוד)\n\nהמלצה: <b>1</b> לפעולה רגילה.",

        "ocr_reset_title": "ההגדרות אופסו",
        "ocr_reset_message": "כל הגדרות ה-OCR אופסו לערכי ברירת המחדל.",
        "info_tooltip": "מידע נוסף על פרמטר זה",
        "ocr_reset_defaults": "איפוס לברירות המחדל",

        "ocr_psm_0": "אוטומטי (מנוע Legacy)",
        "ocr_psm_1": "זיהוי עמודות אוטומטי",
        "ocr_psm_3": "אוטומטי (ברירת מחדל)",
        "ocr_psm_4": "עמודה בודדת",
        "ocr_psm_5": "בלוק אנכי",
        "ocr_psm_6": "בלוק טקסט אחיד",
        "ocr_psm_7": "שורת טקסט בודדת",
        "ocr_psm_8": "מילה בודדת",
        "ocr_psm_11": "תמונה גולמית (ללא ניתוח פריסה)",

        "ocr_oem_0": "מנוע Legacy (מהיר)",
        "ocr_oem_1": "מנוע LSTM (עצבי, מדויק)",
        "ocr_oem_2": "Legacy + LSTM משולב",
        "ocr_oem_3": "ברירת מחדל (LSTM מועדף)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "שפת(ות) OCR...",
        "ocr_language_title": "בחר שפת(ות) OCR",
        "ocr_language_instruction": "בחר את השפה(ות) עבור זיהוי טקסט (OCR).\nאזהרה: שפות מרובות באות על חשבון ביצועים ודיוק!\nאתה משיג את התוצאות הטובות ביותר אם תבחר שפה אחת בלבד.",
        "ocr_language_predefined": "שילובים מוגדרים מראש",
        "ocr_language_custom": "מותאם אישית...",
        "ocr_language_selected": "שפות OCR נבחרות",
        "ocr_language_changed": "שפת OCR שונתה ל-{0}",
        "ocr_language_auto_detect": "שפות זמינות מתגלות באופן אוטומטי.",
        "ocr_language_none_found": "לא נמצאו נתוני שפה של Tesseract! אנא התקן חבילות שפה (למשל 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "בחירת שפה מותאמת אישית",
        "ocr_language_available": "שפות זמינות (מותקנות):",
        "ocr_language_select_hint": "בחר שפה אחת או יותר:",
        "ocr_language_confirm": "החל",
        "ocr_language_reset": "איפוס לברירת המחדל (deu+eng+vie)",
        "ocr_language_priorities": "שפות מומלצות (מותקנות מראש):",

        "select_all_languages": "בחר הכל",
        "clear_all_languages": "נקה בחירה",
        "install_language_packs": "התקן חבילות שפה חסרות...",
        "install_hint": "💡 טיפ: לא כל השפות מותקנות במערכת שלך. באמצעות כפתור זה תקבל עזרה בהתקנה.",
        "ocr_language_install_title": "התקנת חבילות שפה של Tesseract",

        "ocr_missing_languages": "חבילות שפת OCR חסרות",
        "ocr_missing_languages_message": "השפות הנבחרות הבאות אינן מותקנות במערכת שלך:\n\n{0}\n\nאנא התקן את חבילות השפה החסרות (ראה עזרה תחת 'עזרת התקנה').\n\nהאם ברצונך לפתוח את עזרת ההתקנה כעת?",
        "ocr_missing_languages_voice": "חבילות שפה חסרות. אנא התקן את השפות החסרות.",
        "ocr_install_help_now": "פתח עזרה",
        "ocr_continue_anyway": "נסה בכל זאת",
        "ocr_language_error_title": "שגיאת שפת OCR",
        "ocr_language_error_message": "שגיאה במהלך זיהוי טקסט: {0}\n\nאנא בדוק את הגדרות שפת ה-OCR שלך (הגדרות → שפת OCR).",
        "ocr_install_help_button": "עזרת התקנה",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 התקנת חבילות שפה של Tesseract</p>

        <p>כדי ש-OCR יעבוד בשפה ספציפית, יש להתקין את נתוני השפה המתאימים במערכת שלך. עקוב אחר ההוראות עבור מערכת ההפעלה שלך:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>פתח את <strong>הטרמינל</strong> (Finder → תוכניות → כלי עזר → טרמינל).</li>
        <li>התקן את כל השפות הזמינות עם:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (פעולה זו עשויה להימשך מספר דקות.)</li>
        <li>או רק שפות בודדות (למשל וייטנאמית):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        בגרסאות Homebrew עדכניות, ייתכן שיהיה צורך להוריד את <code>*.traineddata</code> באופן ידני (ראה להלן).</li>
        <li>לאחר ההתקנה: סגור דיאלוג זה ופתח שוב את בחירת שפת OCR – השפות החדשות יופיעו אוטומטית.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>פתח טרמינל (Ctrl+Alt+T).</li>
        <li>התקן את השפה הרצויה, למשל עבור וייטנאמית:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        קודי שפה חשובים: <code>deu</code> (גרמנית), <code>eng</code> (אנגלית), <code>vie</code> (וייטנאמית), <code>spa</code> (ספרדית), <code>fra</code> (צרפתית), <code>ita</code> (איטלקית), <code>nld</code> (הולנדית), <code>fin</code> (פינית), <code>swe</code> (שוודית), <code>nor</code> (נורווגית).</li>
        <li>הצג את כל החבילות הזמינות:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ידני)</p>
        <ol>
        <li>הורד את קבצי <code>*.traineddata</code> הרצויים מ:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (למשל <code>vie.traineddata</code> עבור וייטנאמית).</li>
        <li>העתק את הקבצים לתיקיית השפה של Tesseract, בדרך כלל:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (התאם לפי התקנה אינדיבידואלית.)</li>
        <li>הפעל מחדש את היישום (או פתח שוב את בחירת שפת OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 חלופה לכל המערכות</p>
        <ul>
        <li>התקן את <strong>OCRmyPDF</strong> ואת <strong>Tesseract</strong> עם מנהל חבילות לפי בחירתך. רוב ההתקנות כבר מכילות כמה שפות סטנדרטיות (אנגלית, גרמנית, צרפתית).</li>
        <li>ניתן להתקין שפות חסרות בכל עת – בחירת שפת OCR מפרטת רק את השפות הקיימות בפועל.</li>
        </ul>

        <hr>
        <p><b>✅ לאחר ההתקנה:</b> אין צורך להפעיל מחדש את היישום – השפות החדשות שנוספו יופיעו מיד ברשימה.</p>
        <p><b>📖 עזרה עם קודי שפה:</b> רשימה מלאה זמינה ב-<a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">תיעוד של Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "גופני Noto Sans",
        "info_noto_font_voice": "מדריך התקנה לגופני Noto Sans",
        "btn_info_noto_font_install": "מידע על גופן",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word; direction: ltr; text-align: left;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ כיצד להתקין את גופני Noto החינמיים של Google</h2>

        <p><strong>גופני Noto</strong> הם משפחת גופנים בקוד פתוח של Google. המטרה שלהם היא לראות <em>"ללא טופו"</em> (כלומר ללא תיבות ריקות □) ולהציג נכון כל תו מתקן Unicode. הם התוספת האידיאלית עבור יישומים שצריכים להציג טקסטים בשפות שונות רבות.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 התקנה ב-macOS</h3>

        <p><strong>שיטה 1: עם Homebrew (למתקדמים)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>שיטה 2: דרך "Font Book" (מומלץ)</strong></p>

        <ol>
        <li>הורד את חבילת הגופנים הרשמית:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>חלץ את קובץ ה-ZIP</li>
        <li>העתק קבצים אל <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 התקנה ב-Windows (10 & 11)</h3>

        <p><strong>שיטה 1: Microsoft Store (מומלץ)</strong><br>
        חפש "Google Noto Fonts" או "Noto Sans" ולחץ על <strong>התקן</strong>.</p>

        <p><strong>שיטה 2: התקנה ידנית</strong></p>

        <ol>
        <li>הורדה:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>חלץ ZIP</li>
        <li>בחר קבצי .ttf / .otf</li>
        <li>לחץ לחיצה ימנית → <strong>התקן</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        או<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\שם\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 התקנה ב-Linux</h3>

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

        <p>אימות:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "ניהול סימניות",
        "bookmark_add": "הוסף סימניה",
        "bookmark_add_tooltip": "שמור דף נוכחי כסימניה",
        "bookmark_remove": "הסר סימניה",
        "bookmark_remove_tooltip": "מחק את הסימניה המסומנת",
        "bookmark_remove_all": "הסר הכל",
        "bookmark_remove_all_tooltip": "מחק את כל הסימניות של PDF זה",
        "bookmark_jump": "קפוץ לסימניה",
        "bookmark_jump_tooltip": "קפוץ לדף הנבחר",
        "bookmark_name": "שם",
        "bookmark_page": "דף",
        "bookmark_no_bookmarks": "אין סימניות.\nלחץ על 'הוסף' כדי לשמור את הדף הנוכחי כסימניה.",
        "bookmark_added": "סימניה עבור דף {0} נוספה: {1}",
        "bookmark_removed": "סימניה הוסרה: {0}",
        "bookmark_all_removed": "כל הסימניות הוסרו.",
        "bookmark_name_default": "דף {0}",
        "bookmark_name_prompt": "שם עבור הסימניה:\n(טקסט ארוך יקוצר ל-50 תווים)",
        "bookmark_name_prompt_title": "שם סימניה",
        "bookmark_confirm_remove_all": "האם אתה בטוח שברצונך להסיר את כל {0} הסימניות?",
        "menu_bookmarks": "סימניות",
        "bookmark_manage": "ניהול סימניות",
        "bookmark_next": "סימניה הבאה",
        "bookmark_prev": "סימניה קודמת",
        "bookmark_page_display": "דף {0}",
        "bookmark_exists": "סימניה עבור דף זה עם שם זה כבר קיימת.",
        "bookmark_select_first": "אנא בחר תחילה סימניה.",
        "bookmark_confirm_remove": "האם אתה בטוח שברצונך להסיר את הסימניה 'דף {0}: {1}'?",
        "bookmark_jumped_to": "קפץ לסימניה '{0}' בעמוד {1}.",
        "bookmark_jumped_to_voice": "סימניה {0}, דף {1}",
        "btn_close": "סגור",

        "bookmark_list": "הסימניות שלך",
        "bookmark_rename": "שנה שם סימניה",
        "bookmark_rename_tooltip": "שנה את שם הסימניה הנבחרת",
        "bookmark_rename_title": "שנה שם סימניה",
        "bookmark_rename_prompt": "שם חדש עבור סימניה בדף {0}:\n(מקסימום 50 תווים)",
        "bookmark_renamed": "הסימניה '{0}' שינתה את שמה ל-'{1}'.",
        "bookmark_item_tooltip": "דף {0}: {1}\nלחץ פעמיים כדי לקפוץ",
        "bookmark_name_exists_question": "סימניה בשם '{0}' כבר קיימת בדף זה.\nלשנות שם בכל זאת?",

        "context_bookmarks": "סימניות",
        "context_bookmark_add_here": "הוסף סימניה עבור דף זה",
        "context_bookmarks_existing": "סימניות קיימות:",
        "context_bookmarks_jump": "קפוץ לסימניה:",
        "context_bookmarks_none": "אין סימניות",
        "context_bookmarks_clear_all": "הסר את כל {0} הסימניות",

        "bookmark_search_placeholder": "חפש סימניות... (שם או דף)",
        "bookmark_search_results": "נמצאו %d סימניות עבור \"%s\"",
        "bookmark_no_search_results": "לא נמצאו סימניות עבור \"%s\"",
        "bookmark_no_search_results_label": "אין תוצאות עבור \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "ערוך מטא-נתונים של PDF",
        "metadata_title": "כותרת",
        "metadata_title_placeholder": "כותרת המסמך",
        "metadata_title_tooltip": "כותרת המסמך (מוצגת בשורת הכותרת)",
        "metadata_author": "מחבר",
        "metadata_author_placeholder": "שם המחבר",
        "metadata_author_tooltip": "יוצר המסמך",
        "metadata_subject": "נושא",
        "metadata_subject_placeholder": "נושא המסמך",
        "metadata_subject_tooltip": "תיאור קצר של התוכן",
        "metadata_keywords": "מילות מפתח",
        "metadata_keywords_placeholder": "מילות מפתח, מופרדות בפסיקים",
        "metadata_keywords_tooltip": "מילות מפתח לקטלוג המסמך",
        "metadata_creator": "יוצר",
        "metadata_creator_placeholder": "יישום שיצר את ה-PDF",
        "metadata_creator_tooltip": "התוכנה שבה נוצר המסמך",
        "metadata_producer": "מפיק",
        "metadata_producer_placeholder": "יישום שהמיר את ה-PDF",
        "metadata_producer_tooltip": "התוכנה שהמירה את ה-PDF",
        "metadata_creation_date": "תאריך יצירה",
        "metadata_creation_date_tooltip": "תאריך יצירת המסמך",
        "metadata_mod_date": "תאריך שינוי",
        "metadata_mod_date_tooltip": "תאריך השינוי האחרון",
        "metadata_pdf_info": "📄 מידע על PDF",
        "metadata_pages": "מספר דפים",
        "metadata_file_size": "גודל קובץ",
        "metadata_pdf_version": "גרסת PDF",
        "metadata_encrypted": "מוצפן",
        "metadata_encrypted_yes": "כן (מוגן בסיסמה)",
        "metadata_encrypted_no": "לא",
        "metadata_reload": "📂 טען מחדש מ-PDF",
        "metadata_reset": "בטל שינויים",
        "metadata_reloaded": "המטא-נתונים נטענו מחדש מה-PDF.",
        "metadata_reset_done": "כל שדות המטא-נתונים אופסו.",
        "metadata_no_file": "לא נטען קובץ PDF.",
        "metadata_save_error": "שגיאה בשמירת מטא-נתונים",
        "metadata_saved": "המטא-נתונים נשמרו בהצלחה.",
        "metadata_pdf_version_unknown": "PDF (לא ידוע)",
        "metadata_saved_message": "המטא-נתונים נשמרו בהצלחה.",
        "metadata_saved_voice": "מטא-נתונים נשמרו.",

        "metadata_custom": "🔧 מטא-נתונים מותאמים אישית",
        "metadata_custom_placeholder": "{\n  \"השדה_שלי\": \"הערך_שלי\",\n  \"שדה_אחר\": 123\n}",
        "metadata_custom_tooltip": "תצורת JSON עבור מטא-נתונים מותאמים אישית (אופציונלי)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "תבנית \"{0}\" נבחרה - לחץ פעמיים כדי להכניס",
        "text_use_template": "השתמש בחסימת טקסט",
        "text_type": "סוג",
        "text_search_templates": "חפש חסימות טקסט...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 מידע על ייצוא / ייבוא",
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

        <h3>📦 מה מיוצא? (סקירה כללית)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">הגדרות יישום כלליות</span></li>
            <li class="detail">• מצב כהה/בהיר</li>
            <li class="detail">• היפוך מצב כהה עבור תמונות</li>
            <li class="detail">• ערך סף אפור</li>
            <li class="detail">• שפה</li>
            <li class="detail">• גאומטריית חלון</li>
            <li class="detail">• מצב זום</li>
            <li class="detail">• ניווט (סרגל ניווט גלוי)</li>
            <li class="detail">• פלט קולי (מופעל/מושבת)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">הגדרות גיבוי</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">מתן שמות לקבצים (חותמת זמן, מפריד, סיומות)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">הגדרות עבור הוספות של</span></li>
            <li class="detail">• חתימות</li>
            <li class="detail">• טקסט וחסימות טקסט</li>
            <li class="detail">• סימני V, תמונות וצורות</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">הגדרות OCR</span></li>
            <li class="detail">• שפה</li>
            <li class="detail">• כפיית OCR · מצב דף</li>
            <li class="detail">• עיבוד מקדים של תמונה: תיקון הטיה, ניקוי, דגימת יתר</li>
            <li class="detail">• מספר משימות מקביליות</li>
            <li class="detail">• מצב היפוך</li>
            <li class="detail">• ערך סף אפור</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">סימניות</span></li>
            <li class="detail">• כל הסימניות לפי קובץ PDF (דף, שם, זמן יצירה)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">מסד נתונים של סיסמאות</span></li>
            <li class="detail">• סיסמאות PDF שמורות (מוצפנות או טקסט רגיל לפי בחירה)</li>
            <li class="detail">• Hash של סיסמת האב (אם הוגדרה)</li>
            <li class="detail">• נתוני אימות</li>
        </ul>

        <h4>⚠️ הערות חשובות</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 בעת ייבוא:</strong>
            <ul>
                <li><span class="warning">➜ כל ההגדרות הנוכחיות יידרסו לחלוטין</span></li>
                <li>• נדרשת הפעלה מחדש של היישום</li>
                <li>• חתימות, חסימות טקסט וסימניות קיימות יוחלפו</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 סיסמת אב ומצב ייצוא:</strong>
            <ul>
                <li>• כאשר סיסמת האב פעילה, תוכל לבחור:</li>
                <li>  - <span style="color: #98FB98;"><strong>לא מוצפן</strong></span> (סיסמאות הן בטקסט רגיל ב-ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>מוצפן</strong></span> (ניתן לקריאה רק עם סיסמת האב במערכת היעד)</li>
                <li>• Hash של סיסמת האב <strong>תמיד</strong> מאוחסן מוצפן</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ הודעת אבטחה:</strong>
            <ul>
                <li>• קובץ ה-ZIP המיוצא מכיל נתונים רגישים (<strong>סיסמאות, סימניות, חתימות</strong>)</li>
                <li>• אנא שמור אותו במקום בטוח (למשל דיסק און קי מוצפן, מנהל סיסמאות)</li>
                <li>• אם הקובץ יאבד, סיסמאות PDF שמורות יאבדו ללא תקנה</li>
            </ul>
        </div>

        <h4>📁 תבנית ייצוא</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            ההגדרות נשמרות בקובץ ZIP אחד:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP זה מכיל את קובץ <code>settings.json</code> המלא (מתוך התצורה שלך) וכן קבצי תמונת חתימה מוטמעים וסיסמאות מוצפנות.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "חתימות - מדריך",
        'signature_guide_html': """
        📝 <strong>חתימות - מדריך מהיר</strong><br>
        <ul>
        <li>הגדרת סיסמת מאסטר</li>
        <li>הגדרת חתימות בתפריט <em>הגדרות</em> (גודל, חותמת זמן, …)</li>
        <li>הוספה עם <strong>לחיצה ימנית</strong> במיקום הרצוי (סיסמת מאסטר נדרשת פעם אחת לכל הפעלה)</li>
        <li>הזזת החתימה עם העכבר או מקשי החצים</li>
        <li>הוספת חתימות מרובות ברצף</li>
        <li>התאמה אישית של כל חתימה בנפרד</li>
        <li>ביטול חתימה בודדת</li>
        <li>שמירה / ביטול של כל החתימות בבת אחת</li>
        <li>לחלופין, ניתן להשתמש גם בשורת התפריטים.</li>
        </ul>
        """,
        'signature_guide_voice': "מדריך מהיר לחתימות. הגדרת סיסמת מאסטר. הגדרת חתימות בהגדרות. הוספה בלחיצה ימנית.",

        'image_guide_title': "הוספת תמונות - מדריך",
        'image_guide_html': """
        📷 <strong>הוספת תמונות ל-PDF - מדריך מהיר</strong><br>
        <ol>
        <li>לחיצה ימנית במיקום הרצוי</li>
        <li><em>„הוסף תמונה“</em> → בחר תמונה</li>
        <li>מיקום התמונה: גרור בעכבר</li>
        <li>התאמת גודל: גרור בפינות/בקצוות</li>
        <li>שמירה על יחס ממדים: מקש <strong>[A]</strong></li>
        <li>התאמות נוספות: לחיצה ימנית על התמונה</li>
        </ol>
        <p><strong>טיפ:</strong> בתפריט ההקשר תוכל להתאים את ההגדרות.</p>
        """,
        'image_guide_voice': "מדריך מהיר לתמונות. לחיצה ימנית, הוסף תמונה, בחר. מיקום בעכבר, התאמת גודל בפינות. יחס ממדים עם מקש A.",

        'form_guide_title': "הוספת צורות - מדריך",
        'form_guide_html': """
        📐 <strong>הוספת צורות ל-PDF - מדריך מהיר</strong><br>
        <ol>
        <li>בחר סוג צורה (מלבן, אליפסה, קו, חץ)</li>
        <li>לחץ על המיקום:
            <ul>
            <li>למלבן/אליפסה: לחיצה אחת ממקמת את הצורה</li>
            <li>לקו/חץ: שתי לחיצות לנקודת התחלה וסיום</li>
            </ul>
        </li>
        <li>מיקום הצורה: גרור בעכבר</li>
        <li>התאמת גודל: גרור בפינות/בקצוות</li>
        <li>שמירת הצורה: <strong>Enter</strong></li>
        <li>ביטול הצורה: <strong>ESC</strong></li>
        <li>התאמות נוספות: לחיצה ימנית על הצורה</li>
        </ol>
        <p><strong>טיפ:</strong> בתפריט ההקשר תוכל להתאים את ההגדרות.</p>
        """,
        'form_guide_voice': "מדריך מהיר לצורות. בחר סוג צורה. עבור מלבן או אליפסה לחץ פעם אחת, עבור קו או חץ לחץ פעמיים. מיקום בעכבר, התאמת גודל בפינות. שמירה עם Enter, ביטול עם Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "קודם",
        "btn_next_result": "הבא",
        "ocr_text_window": "חלון טקסט OCR",
        "bookmark_existing": "סימניות קיימות",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "השוואת OCR Mac - Windows",
        'ocr_method_mac_win_title': "הבדלי OCR בין Mac ל-Windows",
        'ocr_method_mac_win_voice': "Mac טוב יותר",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – הבדלים בין macOS ל-Windows</strong></p>

        <p><strong>macOS (מומלץ)</strong></p>
        <p>כלי:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>תוצאה:</p>
        <ul>
        <li>PDF הניתן לחיפוש עם טקסט מוטבע השומר במידה רבה על הפריסה המקורית.</li>
        </ul>
        <p>יתרונות:</p>
        <ul>
        <li>איכות מעולה של זיהוי טקסט (אפילו בעמודים עקומים).</li>
        <li>שמירה על גרפיקה וקטורית וגופנים.</li>
        <li>סרגל התקדמות GUI דרך הערכת תת-תהליך.</li>
        <li>שליטה מלאה בכל פרמטרי ה-OCR (Deskew, Clean, Oversample, אופטימיזציה).</li>
        <li>חיפוש טקסט זמין ישירות בחלון הראשי (תצוגת PDF).</li>
        </ul>
        <p>חסרונות:</p>
        <ul>
        <li>דורש כלי מערכת נוספים (ocrmypdf, Ghostscript, unpaper, pngquant – כלולים בחבילת האפליקציה).</li>
        <li>טיפול בשגיאות מורכב יותר (קיפאונות, פסקי זמן).</li>
        </ul>

        <p><strong>Windows (חלופה יציבה)</strong></p>
        <p>כלי:</p>
        <ul>
        <li>pytesseract (חיבור ישיר ל-Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>תוצאה:</p>
        <ul>
        <li>PDF הניתן לחיפוש התואם מבחינה ויזואלית ל-PDF של תמונה, אך ניתן לחיפוש דרך הטקסט השקוף.</li>
        </ul>
        <p>יתרונות:</p>
        <ul>
        <li>אף אחד לא עולה לי בראש כרגע.</li>
        </ul>
        <p>חסרונות:</p>
        <ul>
        <li>ה-PDF הוא בעצם תמונה עם טקסט בלתי נראה; הפריסה עלולה לסטות מעט במסמכים מורכבים (עמודות, טבלאות).</li>
        <li>אין תיקון הטיה אוטומטי (--deskew) או ניקוי תמונה (--clean).</li>
        <li>סרגל ההתקדמות GUI מתעדכן רק באופן גס על סמך מספר העמודים המעובדים.</li>
        <li>מהירות ה-OCR איטית במקצת (מכיוון שכל עמוד מעובד בנפרד).</li>
        <li>חיפוש הטקסט מופנה לחלון טקסט OCR.</li>
        </ul>

        <p><strong>קווי דמיון</strong></p>
        <ul>
        <li>שתי השיטות יוצרות PDF הניתן לחיפוש באותה ספרייה כמו קובץ המקור.</li>
        <li>ניתן להגדיר את הגדרות ה-OCR (שפה, DPI, מצב פילוח עמוד, מצב מנוע OCR) דרך OCRSettingsDialog והן חלות בשני המימושים.</li>
        </ul>

        <p><strong>המלצה:</strong></p>
        <ul>
        <li>macOS: הקובץ הבינארי ocrmypdf מספק את התוצאות הטובות ביותר – קנו Mac והשתמשו בגרסה (PDFDarkView עבור Mac עם שבב Apple Silicon או Intel). תוצאות ה-OCR טובות יותר מאשר ב-Windows!</li>
        <li>Windows: השתמשו בפתרון pytesseract. הוא יציב ומספק איכות מספקת לחלוטין עבור רוב המסמכים.</li>
        </ul>

        <p><strong>הערה חשובה:</strong></p>
        <ul>
        <li>שתי הגרסאות משולבות לחלוטין בממשק המשתמש – המשתמש אינו מבחין בהבדל.</li>
        <li>התוכנית מחליטה אוטומטית באיזה מנוע OCR להשתמש על סמך מערכת ההפעלה.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "יצירת חתימה (מסריקה)",
        "signature_create_title": "בחירת חתימה סרוקה (PDF/תמונה)",
        "image_pdf_filter": "תמונות ו-PDF",
        "signature_pdf_empty": "ה-PDF אינו מכיל עמודים.",
        "signature_created_success": "החתימה נוצרה בהצלחה: {0}",
        "signature_create_error": "שגיאה ביצירת החתימה:\n{0}",
        "rembg_missing": "rembg אינו מותקן.\nאנא התקן: pip install rembg\nשגיאה: {0}",
        "signature_name_title": "שם קובץ לחתימה",
        "signature_name_message": "אנא הזן שם קובץ לחתימה החדשה (יישמר כ-PNG עם רקע שקוף):",
        "signature_name_label": "שם קובץ:",
        "signature_name_voice": "הזן שם קובץ לחתימה",
        "signature_processing": "העיבוד מתבצע...",
        "signature_creation_title": "החתימה נוצרת",
        "signature_overwrite_warning": "הקובץ '{0}' כבר קיים. להחליף?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"הכן PDF לחתימה",
        "signature_prepare_instruction":"אנא בחר PDF המכיל בעמוד בודד חתימה סרוקה.\n\nלזיהוי מיטבי, ודא כי:\n• החתימה כתובה בדיו שחורה (עט כדורי או עט דק) על נייר לבן.\n• החתימה נמצאת בשליש העליון של דף A4 הריק מלבד זאת.\n• ה-PDF נסרק ברזולוציה של 300 dpi לפחות.\n• החתימה ברורה ואינה דקה מדי.\n• אין דפוסי רקע או קווים מפריעים.",
        "signature_prepare_voice":"אנא בחר PDF עם חתימה סרוקה. שים לב לאיכות טובה וניגודיות.",
        "sig_thickness_label":"עובי קו:",
        "sig_thickness_normal":"רגיל (דק)",
        "sig_thickness_bold":"מודגש (מומלץ)",
        "sig_thickness_very_bold":"מודגש מאוד",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "הוספת שפות GUI ו-OCR - מדריך",
        'language_guide_title': "הוספת שפות GUI ו-OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>הורד את קובץ התרגום הרצוי <code>translations_xy.py</code> מ-<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        והנח אותו בספרייה הבאה:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>פתח את דפדפן האינטרנט שלך.</li>
        <li>עבור אל: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>בקצה הימני של המסך, חפש "Releases" ובחר את זה המסומן <strong>"latest"</strong>.</li>
        <li>בדף השחרור הבא, הורד את הקובץ <code>Source Code.zip</code> בתחתית.</li>
        <li>חלץ את קובץ ה-ZIP.</li>
        <li>בתיקייה המחולצת, חפש את כל קובצי השפה הדרושים לך והעתק אותם לספרייה:<br/>
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
        "menu_watermark":"הוספת סימן מים",
        "fullpage_text_watermark_title":"טקסט כסימן מים",
        "fullpage_image_watermark_title":"תמונה כסימן מים",
        "filename_with_watermark":"_עם_סימן_מים",
        "watermark_text":"טקסט:",
        "watermark_text_placeholder":"טקסט סימן המים שלך...",
        "watermark_font_family":"גופן:",
        "watermark_font_size":"גודל גופן:",
        "watermark_format":"עיצוב:",
        "watermark_bold":"מודגש",
        "watermark_italic":"נטוי",
        "watermark_color":"צבע:",
        "watermark_choose_color":"בחירת צבע...",
        "watermark_opacity":"אטימות / שקיפות:",
        "watermark_direction":"כיוון קריאה:",
        "watermark_direction_l_r":"שמאל → ימין",
        "watermark_direction_bl_tr":"למטה שמאל → למעלה ימין",
        "watermark_direction_tl_br":"למעלה שמאל → למטה",
        "watermark_direction_b_t":"למטה → למעלה",
        "watermark_direction_t_b":"למעלה → למטה",
        "watermark_preview":"תצוגה מקדימה:",
        "watermark_preview_sample":"טקסט לדוגמה",
        "watermark_empty_text":"אנא הזן טקסט.",
        "watermark_applied":"סימן המים הוחל על כל הדפים.",
        "watermark_saved":"סימן המים נשמר.",
        "image_scale":"גודל:",
        "image_preview":"תצוגה מקדימה של תמונה:",
        "no_image_selected":"לא נבחרה תמונה",
        "browse":"עיון...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "השחרות",
        "redact_add_black": "השחרה (שחור)",
        "redact_add_white": "השחרה (לבן / מחיקה)",
        "redact_added_black": "השחרה שחורה נוספה",
        "redact_added_white": "השחרה לבנה נוספה",
        "redact_apply_all": "החל את כל ההשחרות ושמור",
        "redact_discard_all": "בטל את כל ההשחרות",
        "redact_discard": "בטל השחרה זו",
        "no_redactions": "אין השחרות",
        "redact_confirm_title": "החל השחרות באופן קבוע",
        "redact_confirm_message": "אזהרה: האזורים המסומנים יימחקו לצמיתות (שחור או לבן).\nתיווצר גיבוי (אם מופעל).\n\nלהמשיך?",
        "redact_apply": "כן, השחר עכשיו",
        "redact_saved": "{0} השחרות הוחלו ונשמרו בהצלחה.",
        "redact_saved_voice": "{0} השחרות הוחלו",
        "redact_error": "שגיאה בהשחרה",
        "filename_redacted":"_מושחר",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'הוספת מספרי עמודים',
        'page_numbers_format': 'פורמט מספר:',
        'page_numbers_format_arabic': '1, 2, 3 ... (ערבי)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (רומי קטן)',
        'page_numbers_format_roman_upper': 'I, II, III ... (רומי גדול)',
        'page_numbers_format_letter': 'A, B, C ... (אותיות)',
        'page_numbers_format_custom': 'מותאם אישית',
        'page_numbers_custom_pattern': 'תבנית:',
        'page_numbers_custom_placeholder': 'למשל "עמוד {nummer}" או "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'השתמש ב-{nummer} עבור מספר העמוד הנוכחי ו-{total} עבור המספר הכולל',
        'page_numbers_position': 'מיקום:',
        'page_numbers_pos_tl': 'למעלה שמאל',
        'page_numbers_pos_tc': 'למעלה מרכז',
        'page_numbers_pos_tr': 'למעלה ימין',
        'page_numbers_pos_ml': 'אמצע שמאל',
        'page_numbers_pos_mc': 'במרכז',
        'page_numbers_pos_mr': 'אמצע ימין',
        'page_numbers_pos_bl': 'למטה שמאל',
        'page_numbers_pos_bc': 'למטה מרכז',
        'page_numbers_pos_br': 'למטה ימין',
        'page_numbers_margins': 'שוליים:',
        'page_numbers_margin_x': 'מרחק אופקי:',
        'page_numbers_margin_y': 'מרחק אנכי:',
        'page_numbers_range': 'טווח עמודים:',
        'page_numbers_all_pages': 'כל העמודים',
        'page_numbers_custom_range': 'טווח מותאם אישית',
        'page_numbers_from': 'מ:',
        'page_numbers_to': 'עד:',
        'page_numbers_progress': 'מוסיף מספרי עמודים...',
        'page_numbers_start': 'מתחיל הוספת מספרי עמודים...',
        'page_numbers_cancel': 'הוספת מספרי עמודים בוטלה',
        'page_numbers_success': 'מספרי העמודים נוספו בהצלחה.\n\nהאם ברצונך לפתוח את ה-PDF החדש?\n\n{0}',
        'page_numbers_complete': 'מספרי עמודים נוספו',
        'page_numbers_error_format': 'שגיאה בהוספת מספרי עמודים: {0}',
        'page_numbers_content_type': 'סוג תוכן:',
        'page_numbers_tab_simple': 'מספר פשוט',
        'page_numbers_tab_range': 'עמוד X מתוך Y',
        'page_numbers_tab_date': 'תאריך',
        'page_numbers_tab_custom': 'טקסט חופשי',
        'page_numbers_range_format': 'פורמט:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'עמוד {aktuell} מתוך {gesamt}',
        'page_numbers_range_custom': 'מותאם אישית',
        'page_numbers_range_placeholder': 'למשל "עמוד {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'פורמט תאריך:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 בינואר 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'מותאם אישית',
        'page_numbers_date_placeholder': 'למשל %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'מיקום:',
        'page_numbers_date_before': 'תאריך לפני מספר העמוד',
        'page_numbers_date_after': 'תאריך אחרי מספר העמוד',
        'page_numbers_date_only': 'רק תאריך (ללא מספר עמוד)',
        'page_numbers_custom_text': 'טקסט מותאם אישית:',
        'page_numbers_custom_placeholder_text': 'השתמש ב-{seite} עבור מספר העמוד ו-{gesamt} עבור המספר הכולל\nלמשל "סודי - עמוד {seite}" או "{seite} מתוך {gesamt}"',
        "filename_with_page_number":"_עם_מספר_עמוד",
        "filename_with_page_declaration":"_עם_הצהרת_עמוד",
        "filename_with_pagenumber":"_עם_מספר_עמוד",
        "filename_with_date":"_עם_תאריך",
        "filename_with_my_page_declaration":"_עם_הצהרת_עמוד_מותאמת",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "שינויים שלא נשמרו",
        "unsaved_changes_message_darkmode": "קיימות הוספות שלא נשמרו.\nהאם ברצונך לשמור אותן לפני ההחלפה?",
        "save_and_switch": "שמור והחלף",
        "discard_and_switch": "החלף עכשיו",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'ייצוא עמודים כתמונות',
        'export_images_menu': 'ייצוא כתמונות (PNG/JPEG)',
        'export_images_format': 'פורמט תמונה:',
        'export_images_dpi': 'רזולוציה (DPI):',
        'export_images_quality': 'איכות JPEG:',
        'export_images_range': 'טווח עמודים:',
        'export_images_all_pages': 'כל העמודים',
        'export_images_custom_range': 'טווח מותאם אישית',
        'export_images_from': 'מ:',
        'export_images_to': 'עד:',
        'export_images_options': 'אפשרויות:',
        'export_images_single_files': 'כל עמוד כקובץ נפרד',
        'export_images_subfolder': 'ייצוא לתיקיית משנה',
        'export_images_subfolder_info': 'לתיקיית משנה "שםPDF_תמונות"',
        'export_images_same_folder': 'באותה תיקייה כמו ה-PDF',
        'export_images_apply_darkmode': 'החל הגדרות PDFDarkView (מצב כהה)',
        'export_images_target_folder': 'תיקיית יעד:',
        'export_images_browse': 'עיון...',
        'export_images_preview': 'תצוגה מקדימה:',
        'export_images_preview_info': 'בחר הגדרות לייצוא',
        'export_images_preview_info_detail': '{0} עמודים כ-{1}\nרזולוציה: {2} DPI\nשם קובץ: {3}\n{4}',
        'export_images_select_folder': 'בחר תיקיית יעד',
        'export_images_start': 'מתחיל ייצוא תמונות...',
        'export_images_progress': 'מייצא תמונות...',
        'export_images_saving': 'שומר עמוד {0} מתוך {1}...',
        'export_images_success': 'הייצוא הצליח!\n\n{0} תמונות נשמרו ב:\n{1}',
        'export_images_complete': 'ייצוא התמונות הושלם',
        'export_images_open_folder': '📁 פתח תיקייה',
        'export_images_cancel': 'ייצוא התמונות בוטל',
        'export_images_error_format': 'שגיאה בייצוא תמונות: {0}',
        'export_images_pdf2image_missing': 'הספרייה "pdf2image" אינה מותקנת.\n\nאנא התקן אותה באמצעות:\npip install pdf2image\n\nעבור Windows אתה צריך גם את Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'המרת PDF/A לארכוב ארוך טווח',
        'pdfa_menu': 'המרת PDF/A (מתאים לארכוב)',
        'pdfa_info': 'ממיר את ה-PDF לפורמט PDF/A.\n\nPDF/A תוכנן במיוחד לארכוב ארוך טווח ומבטיח שהמסמך יוצג כהלכה בעתיד.',
        'pdfa_standard': 'תקן PDF/A:',
        'pdfa_standard_select': 'גרסה:',
        'pdfa_1': 'PDF/A-1 (פשוט, תואם באופן נרחב)',
        'pdfa_2': 'PDF/A-2 (מודרני, דחיסה טובה יותר)',
        'pdfa_3': 'PDF/A-3 (הגרסה העדכנית ביותר, מאפשר קבצים מצורפים)',
        'pdfa_standards_explanation': '📖 הסבר על התקנים:\n\n'
            '• PDF/A-1: בסיסי, תואם למערכות ישנות (בערך 2005)\n'
            '• PDF/A-2: מודרני יותר, דחיסה טובה יותר, תמיכה בשקיפות (בערך 2011)\n'
            '• PDF/A-3: הגרסה העדכנית ביותר, מאפשר הטמעת קבצים מצורפים (בערך 2013)\n\n'
            'המלצה: PDF/A-2 הוא פשרה טובה בין תאימות לפונקציונליות מודרנית.',
        'pdfa_options': 'אפשרויות:',
        'pdfa_compress_enable': 'דחוס PDF (קובץ קטן יותר)',
        'pdfa_metadata_preserve': 'שמור מטא-נתונים (כותרת, מחבר וכו\')',
        'pdfa_target_folder': 'תיקיית יעד:',
        'pdfa_browse': 'עיון...',
        'pdfa_select_folder': 'בחר תיקיית יעד',
        'pdfa_ocr_info_unknown': '🔍 לא ניתן היה לבדוק את תוכן הטקסט.',
        'pdfa_ocr_info_not_needed': '✅ טקסט זמין - OCR אינו נדרש.\nניתן ליצור PDF/A ישירות.',
        'pdfa_ocr_info_recommended': '⚠️ לא נמצא טקסט מספק.\n\nעבור PDFs הניתנים לחיפוש, אנו ממליצים להפעיל OCR תחילה.\nהערה: PDF/A עובד גם ללא OCR - אך הטקסט לא יהיה ניתן לחיפוש.',
        'pdfa_ocr_info_error': '❌ שגיאה בבדיקה: {0}',
        'pdfa_start': 'מתחיל המרת PDF/A...',
        'pdfa_progress': 'המרת PDF/A בעיצומה...',
        'pdfa_success': 'המרת PDF/A הצליחה!\n\nנשמר כ:\n{0}\n\nהאם ברצונך לפתוח את ה-PDF החדש?',
        'pdfa_complete': 'המרת PDF/A הושלמה',
        'pdfa_cancel': 'המרת PDF/A בוטלה',
        'pdfa_error_format': 'שגיאה בהמרת PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'הספרייה "ocrmypdf" אינה מותקנת.\n\nאנא התקן אותה באמצעות:\npip install ocrmypdf',
        'btn_convert': 'המר',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'ייעול PDF (הקטנת גודל קובץ)',
        'optimize_menu': 'ייעול PDF (גודל קובץ)',
        'optimize_info': 'מקטין את גודל קובץ ה-PDF באמצעות שיטות ייעול שונות.\n\nככל שרמת הדחיסה גבוהה יותר, הקובץ קטן יותר - עם אובדן איכות אפשרי בתמונות.',
        'optimize_level': 'רמת דחיסה:',
        'optimize_level_low': 'נמוכה (מהיר, חיסכון קטן)',
        'optimize_level_medium': 'בינונית (פשרה טובה)',
        'optimize_level_high': 'גבוהה (חיסכון גדול)',
        'optimize_level_maximum': 'מקסימלית (חיסכון מקסימלי, איטי)',
        'optimize_level_explanation': 'המלצה: "בינונית" היא פשרה טובה בין מהירות לגודל קובץ.',
        'optimize_options': 'אפשרויות:',
        'optimize_compress_images': 'דחוס תמונות (הקטן איכות JPEG)',
        'optimize_clean_objects': 'הסר אובייקטים שאינם בשימוש',
        'optimize_preserve_metadata': 'שמור מטא-נתונים (כותרת, מחבר וכו\')',
        'optimize_image_quality': 'איכות תמונה:',
        'optimize_range': 'טווח עמודים:',
        'optimize_all_pages': 'כל העמודים',
        'optimize_custom_range': 'טווח מותאם אישית',
        'optimize_from': 'מ:',
        'optimize_to': 'עד:',
        'optimize_target_folder': 'תיקיית יעד:',
        'optimize_browse': 'עיון...',
        'optimize_select_folder': 'בחר תיקיית יעד',
        'optimize_info_box': 'מידע',
        'optimize_info_text': 'ייעול עלול לקחת מספר דקות עבור PDFs גדולים.\n\nתמונות נשמרות באיכות מופחתת, מה שיכול להקטין משמעותית את גודל הקובץ.',
        'optimize_start': 'מתחיל ייעול PDF...',
        'optimize_progress': 'מייעל PDF...',
        'optimize_cancel': 'ייעול PDF בוטל',
        'optimize_complete': 'ייעול PDF הושלם',
        'optimize_error_format': 'שגיאה בייעול PDF:\n\n{0}',
        'optimize_success_message': 'ייעול PDF הצליח!\n\nנשמר כ:\n{0}\n\nלפני: {1}\nאחרי: {2}\nחיסכון: {3:.1f}%\n\n{4}\n\nהאם ברצונך לפתוח את ה-PDF המיועל?',
        'optimize_success_message_no_size': 'ייעול PDF הצליח!\n\nנשמר כ:\n{0}\n\nמידע על גודל אינו זמין.\n\nהאם ברצונך לפתוח את ה-PDF המיועל?',
        'optimize_result_positive': 'הקובץ הוקטן ב-{0:.1f}%.',
        'optimize_result_zero': 'אין שינוי בגודל הקובץ.',
        'optimize_result_negative': 'הקובץ גדל ב-{0:.1f}%.\nהייעול דולג, הקובץ המקורי נשמר.',
        'btn_optimize': 'התחל ייעול',
        'filename_optimize_low_suffix': '_מיועל_נמוך',
        'filename_optimize_medium_suffix': '_מיועל',
        'filename_optimize_high_suffix': '_מיועל_גבוה',
        'filename_optimize_maximum_suffix': '_מיועל_מקס',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'חיתוך PDF',
        'crop_menu': 'חיתוך PDF (Crop)',
        'crop_range': 'החל על:',
        'crop_all_pages': 'כל העמודים',
        'crop_current_page': 'רק העמוד הנוכחי',
        'crop_values': 'ערכי חיתוך (בנקודות):',
        'crop_left': 'שמאל:',
        'crop_right': 'ימין:',
        'crop_top': 'למעלה:',
        'crop_bottom': 'למטה:',
        'crop_presets': 'הגדרות מוגדרות מראש:',
        'crop_preset_white': 'זיהוי שוליים לבנים',
        'crop_reset': 'איפוס',
        'crop_mouse_hint': '🖱️ גרור מלבן לבחירה גסה של האזור.\nלאחר מכן תוכל לכוונן את הערכים במדויק ב-SpinBoxes.\nלא ניתן לכוונן ידנית עם העכבר.',
        'crop_apply': 'חיתוך',
        'crop_scope_all': 'כל העמודים',
        'crop_scope_current': 'עמוד נוכחי',
        'crop_new_size': 'גודל חדש: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'לא נטען PDF',
        'crop_preview_error': 'שגיאה בטעינת התצוגה המקדימה',
        'crop_start': 'מתחיל חיתוך...',
        'crop_progress': 'חותך PDF...',
        'crop_success': 'PDF נחתך בהצלחה!\n\nנשמר כ:\n{0}\n\nהאם ברצונך לפתוח את ה-PDF החתוך?',
        'crop_complete': 'חיתוך הושלם',
        'crop_cancel': 'חיתוך בוטל',
        'crop_error_format': 'שגיאה בחיתוך:\n\n{0}',
        'filename_crop_suffix': '_חתוך',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'שיטוח PDF (Flatten)',
        'flatten_menu': 'שיטוח PDF (Flatten)',
        'flatten_info': 'שיטוח PDF "שורף" את כל האלמנטים הניתנים לעריכה לתוך תוכן העמוד.\n\nלאחר מכן, שדות טופס, הערות, טקסטים, צלבים, חתימות, תמונות וצורות אינם ניתנים לעריכה בנפרד.',
        'flatten_explanation_title': '📖 למה זה טוב?',
        'flatten_explanation_text': 'שיטוח נדרש במצבים הבאים:\n\n'
            '• 📄 אתה רוצה להכין את המסמך להדפסה\n'
            '• 🔒 אתה רוצה למנוע ממישהו לשנות שדות טופס\n'
            '• 📎 אתה רוצה "להטביע" הערות ותגובות באופן קבוע במסמך\n'
            '• 🖼️ אתה רוצה לעגן טקסטים, צלבים, חתימות, תמונות וצורות באופן קבוע במסמך\n'
            '• 📦 אתה רוצה להכין את הקובץ לארכוב\n\n'
            'שיטוח הופך את ה-PDF לקטן יותר ומונע הזזה או מחיקה מקרית של אלמנטים.',
        'flatten_what_title': 'מה משוטח?',
        'flatten_what_list': '• ✅ שדות טופס (שדות טקסט, תיבות סימון, כפתורים)\n'
            '• ✅ הערות (תגובות, הדגשות, הערות)\n'
            '• ✅ שכבות על (טקסטים, צלבים, חתימות, תמונות, צורות)',
        'flatten_options': 'אפשרויות:',
        'flatten_forms': 'שטח שדות טופס',
        'flatten_annotations': 'שטח הערות',
        'flatten_overlays': 'שטח שכבות על (טקסטים, צלבים, חתימות, תמונות, צורות)',
        'flatten_target_folder': 'תיקיית יעד:',
        'flatten_browse': 'עיון...',
        'flatten_select_folder': 'בחר תיקיית יעד',
        'flatten_warning': '⚠️ חשוב: שיטוח הוא תהליך בלתי הפיך!\n\nלאחר השיטוח, לא ניתן לשנות או למחוק אלמנטים ניתנים לעריכה בנפרד.\nצור גיבוי מראש במידת הצורך.',
        'flatten_apply': 'שטח',
        'flatten_start': 'מתחיל שיטוח...',
        'flatten_progress': 'משטח PDF...',
        'flatten_success': 'PDF שוטח בהצלחה!\n\nנשמר כ:\n{0}\n\nהאם ברצונך לפתוח את ה-PDF המשוטח?',
        'flatten_complete': 'שיטוח הושלם',
        'flatten_cancel': 'שיטוח בוטל',
        'flatten_error_format': 'שגיאה בשיטוח:\n\n{0}',
        'filename_flatten_suffix': '_משוטח',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'הרכבת PDF (Overlay)',
        'overlay_menu': 'הרכבת PDF (Overlay)',
        'overlay_info': 'מניח PDF אחד (שכבת על) על גבי PDF אחר.\n\nPDF שכבת העל מונח על PDF הבסיס. זה שימושי עבור סימני מים, לוגואים, ניירות מכתבים או חותמות.',
        'overlay_explanation_title': '📖 למה זה טוב?',
        'overlay_explanation_text': 'הרכבה נדרשת במצבים הבאים:\n\n'
            '• 🏢 הנחת לוגו של חברה כסימן מים על כל עמוד\n'
            '• 📄 הנחת נייר מכתבים על PDF ריק\n'
            '• 🖊️ הנחת שכבת על של חותמת על מסמך\n'
            '• 🔖 הנחת סימן מים על כל העמודים\n'
            '• 📑 הנחת שכבת על של טופס על תבנית',
        'overlay_type': 'סוג הרכבה:',
        'overlay_type_fullpage': 'עמוד מלא (מכסה)',
        'overlay_type_transparent': 'עמוד מלא (שקוף - מומלץ)',
        'overlay_type_stamp': 'חותמת (ניתן למיקום)',
        'overlay_type_info_fullpage': '📄 PDF שכבת העל מונח בדיוק על כל העמוד.\nניתן להסיר את הרקע הלבן כך שרק התוכן יישאר גלוי.',
        'overlay_type_info_transparent': '🔍 PDF שכבת העל מונח על כל העמוד עם רקע שקוף.\nהרקע הלבן מוסר אוטומטית - אידיאלי עבור סימני מים ולוגואים!',
        'overlay_type_info_stamp': '🖊️ PDF שכבת העל ממוקם ומוקטן כחותמת.\nמושלם עבור לוגואים, חותמות או חתימות במיקומים ספציפיים.',
        'overlay_remove_background': 'הסר רקע לבן:',
        'overlay_remove_background_enable': 'הסר רקע לבן מ-PDF שכבת העל (הופך את שכבת העל לשקופה)',
        'overlay_remove_background_tooltip': 'מסיר אזורים לבנים מ-PDF שכבת העל כך שהטקסט שמתחת הופך לגלוי.',
        'overlay_threshold': 'ערך סף:',
        'overlay_threshold_hint': '(1-254, גבוה יותר = יותר לבן מוסר)',
        'overlay_select_file': 'בחר PDF לשכבות על:',
        'overlay_file_placeholder': 'אנא בחר קובץ PDF לשכבות על',
        'overlay_browse': 'עיון...',
        'overlay_select_overlay': 'בחר PDF לשכבות על',
        'overlay_range': 'טווח עמודים:',
        'overlay_all_pages': 'כל העמודים',
        'overlay_custom_range': 'טווח מותאם אישית',
        'overlay_from': 'מ:',
        'overlay_to': 'עד:',
        'overlay_position': 'מיקום:',
        'overlay_position_center': 'מרכז',
        'overlay_position_top_left': 'למעלה שמאל',
        'overlay_position_top_right': 'למעלה ימין',
        'overlay_position_bottom_left': 'למטה שמאל',
        'overlay_position_bottom_right': 'למטה ימין',
        'overlay_size': 'גודל:',
        'overlay_size_original': 'גודל מקורי',
        'overlay_size_fit_page': 'התאם לעמוד',
        'overlay_size_custom': 'מותאם אישית (%)',
        'overlay_opacity': 'שקיפות:',
        'overlay_target_folder': 'תיקיית יעד:',
        'overlay_browse_folder': 'עיון...',
        'overlay_select_folder': 'בחר תיקיית יעד',
        'overlay_warning': '⚠️ הערה: PDF שכבת העל מונח על PDF הבסיס ו"נשרף" לתוכו.\n\nלא ניתן לערוך את האלמנטים של PDF שכבת העל בנפרד לאחר השמירה.',
        'overlay_apply': 'הרכבה',
        'overlay_start': 'מתחיל הרכבה...',
        'overlay_progress': 'מרכיב PDF...',
        'overlay_success': 'PDF הורכב בהצלחה!\n\nנשמר כ:\n{0}\n\nהאם ברצונך לפתוח את ה-PDF המורכב?',
        'overlay_complete': 'הרכבה הושלמה',
        'overlay_cancel': 'הרכבה בוטלה',
        'overlay_error_format': 'שגיאה בהרכבה:\n\n{0}',
        'overlay_no_file': 'לא נבחר PDF לשכבות על.\n\nאנא בחר קובץ PDF להרכבה.',
        'filename_overlay_suffix': '_מורכב',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'חילוץ תמונות מ-PDF',
        'extract_images_menu': 'חלץ את כל התמונות',
        'extract_images_info': 'חולץ את כל התמונות מה-PDF ושומר אותן כקבצים נפרדים.\n\nהתמונות נשמרות בפורמט המקורי שלהן או מומרות לפורמט נבחר.',
        'extract_images_format': 'פורמט תמונה:',
        'extract_images_quality': 'איכות JPEG:',
        'extract_images_options': 'אפשרויות:',
        'extract_images_subfolder': 'חלץ לתיקיית משנה ("שםPDF_תמונות")',
        'extract_images_unique': 'רק תמונות ייחודיות (הימנעות מכפילויות)',
        'extract_images_range': 'טווח עמודים:',
        'extract_images_all_pages': 'כל העמודים',
        'extract_images_custom_range': 'טווח מותאם אישית',
        'extract_images_from': 'מ:',
        'extract_images_to': 'עד:',
        'extract_images_target_folder': 'תיקיית יעד:',
        'extract_images_browse': 'עיון...',
        'extract_images_select_folder': 'בחר תיקיית יעד',
        'extract_images_info_box': 'מידע',
        'extract_images_info_text': 'חילוץ עלול לקחת מספר דקות עבור PDFs גדולים.\n\nתמונות נשמרות עם שמם המקורי (עמוד_תמונה).',
        'extract_images_extract': 'חלץ',
        'extract_images_start': 'מתחיל חילוץ...',
        'extract_images_progress': 'חולץ תמונות...',
        'extract_images_success': '✅ תמונות חולצו בהצלחה!\n\n{0} תמונות נשמרו ב:\n{1}',
        'extract_images_complete': 'חילוץ תמונות הושלם',
        'extract_images_cancel': 'חילוץ בוטל',
        'extract_images_error_format': 'שגיאה בחילוץ תמונות:\n\n{0}',
        'extract_images_open_folder': '📁 פתח תיקייה',
        'extract_images_no_images': 'לא נמצאו תמונות ב-PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'עמודים מרובים על עמוד אחד (N-Up)',
        'nup_menu': 'עמודים מרובים על עמוד אחד (N-Up)',
        'nup_info': 'מסדר מספר עמודי PDF על עמוד אחד.\n\nאידיאלי להדפסות קומפקטיות, סקירות או דפי מידע.',
        'nup_layout': 'פריסה:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'תצוגה מקדימה:',
        'nup_preview_info': '{0} עמודים → {1} עמודים לכל גיליון → {2} גיליונות\nפריסה: {3}',
        'nup_order': 'סדר:',
        'nup_order_horizontal': 'אופקי (שורה אחר שורה)',
        'nup_order_vertical': 'אנכי (עמודה אחר עמודה)',
        'nup_order_horizontal_reverse': 'אופקי הפוך',
        'nup_order_vertical_reverse': 'אנכי הפוך',
        'nup_range': 'טווח עמודים:',
        'nup_all_pages': 'כל העמודים',
        'nup_custom_range': 'טווח מותאם אישית',
        'nup_from': 'מ:',
        'nup_to': 'עד:',
        'nup_options': 'אפשרויות:',
        'nup_margins': 'שוליים:',
        'nup_margin_between': 'מרווח בין עמודים:',
        'nup_page_numbers': 'הוסף מספרי עמודים',
        'nup_target_folder': 'תיקיית יעד:',
        'nup_browse': 'עיון...',
        'nup_select_folder': 'בחר תיקיית יעד',
        'nup_create': 'צור',
        'nup_start': 'מתחיל N-Up...',
        'nup_progress': 'יוצר N-Up...',
        'nup_success': 'N-Up נוצר בהצלחה!\n\nנשמר כ:\n{0}\n\nהאם ברצונך לפתוח את ה-PDF החדש?',
        'nup_complete': 'N-Up הושלם',
        'nup_cancel': 'N-Up בוטל',
        'nup_error_format': 'שגיאה ב-N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'שנה גודל עמוד',
        'pagesize_menu': 'שנה גודל עמוד',
        'pagesize_info': 'משנה את גודל העמוד של ה-PDF.\n\nהתוכן מותאם אוטומטית לגודל החדש.',
        'pagesize_format': 'פורמט:',
        'pagesize_select': 'בחר פורמט סטנדרטי:',
        'pagesize_custom': 'גודל מותאם אישית:',
        'pagesize_width': 'רוחב:',
        'pagesize_height': 'גובה:',
        'pagesize_orientation': 'כיוון:',
        'pagesize_portrait': 'דיוקן',
        'pagesize_landscape': 'נוף',
        'pagesize_scale_options': 'אפשרויות קנה מידה:',
        'pagesize_fit': 'התאם (שמור יחס)',
        'pagesize_stretch': 'מתח (עוות)',
        'pagesize_center': 'מרכז (גודל מקורי)',
        'pagesize_range': 'טווח עמודים:',
        'pagesize_all_pages': 'כל העמודים',
        'pagesize_custom_range': 'טווח מותאם אישית',
        'pagesize_from': 'מ:',
        'pagesize_to': 'עד:',
        'pagesize_target_folder': 'תיקיית יעד:',
        'pagesize_browse': 'עיון...',
        'pagesize_select_folder': 'בחר תיקיית יעד',
        'pagesize_apply': 'החל',
        'pagesize_start': 'מתחיל שינוי גודל עמוד...',
        'pagesize_progress': 'משנה גודל עמוד...',
        'pagesize_success': 'גודל העמוד שונה בהצלחה!\n\nנשמר כ:\n{0}\n\nהאם ברצונך לפתוח את ה-PDF החדש?',
        'pagesize_complete': 'שינוי גודל עמוד הושלם',
        'pagesize_cancel': 'שינוי גודל עמוד בוטל',
        'pagesize_error_format': 'שגיאה בשינוי גודל עמוד:\n\n{0}',
        'pagesize_preview_info': 'גודל חדש: {0} x {1} pt',
        'filename_pagesize_suffix': '_גודל_חדש',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'מידע על PDF',
        'pdf_info_menu': 'הצג מידע על PDF',
        'pdf_info_voice': 'מציג מידע על PDF',
        'pdf_info_error': 'שגיאה בהצגת מידע על PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "הצג קיצורי מקלדת",
        "shortcuts_dialog_title": "קיצורי מקלדת",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 קובץ</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>פתח PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>סגור PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>שמור בשם...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>הגן על מסמך</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>הדפס</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>הדפס מיידי (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>צא מהיישום</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 ייצוא</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>ייצא כ-Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>ייצא כ-DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>ייצא כ-TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ייצא כתמונות (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>חלץ תמונות</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ עיבוד מסמכים</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (עמודים מרובים)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>המרת PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>שטח PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>הרכבת PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>ייעל PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ עריכה</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>חיפוש</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>הוסף סימניה</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ניהול סימניות</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>סימניה הבאה</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>סימניה קודמת</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>הפעל OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 ניהול עמודים</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>סובב עמוד נוכחי</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>סובב את כל העמודים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>נרמל עמוד נוכחי</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>נרמל את כל העמודים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>מחק עמודים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>חלץ עמודים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>הוסף עמודים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>הזז עמודים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>מזג PDFs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>שנה גודל עמוד</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 הוספה</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>הוסף טקסט</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>הוסף צלב</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>הוסף חתימה 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>הוסף חתימה 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>הוסף תמונה</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>הוסף מלבן</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>הוסף אליפסה</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>הוסף קו</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>הוסף חץ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>הוסף מספרי עמודים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>סימן מים טקסט</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>סימן מים תמונה</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ השחרות</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>השחרה (שחור)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>השחרה (לבן)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>החל את כל ההשחרות</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ מתקדם</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>חתוך PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ערוך מטא-נתונים</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ תצוגה</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>החלף בין מצב כהה/בהיר</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>הצג חלון טקסט</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>רוחב עמוד (זום)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>שני עמודים (זום)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>סקירה (זום)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ הגדרות</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>ניהול סיסמאות</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>הגדרות OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>הגדרות חתימה</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>עיצוב שמות קבצים</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>ייצא הגדרות</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>ייבא הגדרות</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ מידע</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>הצג מידע על PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>הפעל/כבה פלט קולי</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>מיקוד בשורת התפריטים</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "גרסה חדשה זמינה",
        "update_available_message": "קיימת גרסה חדשה <b>{0}</b>.\n\nבקר בדף השחרור כדי להוריד את העדכון:\n{1}",
        "update_available_voice": "גרסה חדשה {0} זמינה. אנא הורד את העדכון מדף ה-GitHub.",
        "update_open_release": "פתח דף שחרור",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "הורד את כל התרגומים",
        "ask_download_all_translations": """בנוסף לגרמנית, אנגלית וויאטנמית, קיימות {total_languages} שפות ממשק נוספות.\n\nהאם יש לספק / לעדכן אותן?\n\nהערה:\nשפות שאינן נחוצות תוכל למחוק מאוחר יותר באופן ידני בספרייה:\n{translations_path}
        \nאם תבטל, תוכל להוריד את שפות הממשק מאוחר יותר דרך התפריט 'כלים → עדכן תרגומים'.""",
        "menu_update_translations": "עדכן תרגומים",
        "translations_updated": "התרגומים עודכנו",
        "translations_update_success": "{} תרגומים עודכנו בהצלחה ({} חדשים, {} מעודכנים).",
        "translations_update_error": "שגיאה בעדכון התרגומים",
        "translations_update_no_changes": "כל התרגומים כבר מעודכנים.",
        "translations_update_offline": "אין חיבור לאינטרנט. לא ניתן היה לעדכן את התרגומים.",
        "translations_update_in_progress": "התרגומים מתעדכנים ברקע...",
        "translations_downloading": "מוריד תרגומים...",
        "translations_path_hint": "ספריית משתמש לתרגומים",
        "translations_update_not_available_title": "העדכון אינו זמין",
        "translations_update_not_available_message": """עדכון התרגומים זמין רק בגרסה המותקנת.\n\nבמצב פיתוח, התרגומים כבר מעודכנים.""",
        "translations_update_no_internet_title": "אין חיבור לאינטרנט",
        "translations_update_no_internet_message": """לא ניתן ליצור חיבור לאינטרנט.\n\nלא ניתן להוריד את התרגומים מ-GitHub.\n\nפתרונות אפשריים:
        • בדוק את חיבור האינטרנט שלך
        • השבת זמנית כל חומת אש
        • נסה שוב מאוחר יותר
        \nתוכל גם להוריד את התרגומים באופן ידני מ-GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "עדכון כבר מתבצע",
        "btn_retry": "נסה שוב",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "ברוכים הבאים ל-PDF Dark View",
        "welcome_title_not_supported": "ברוכים הבאים ל-PDF Dark View",
        "welcome_message": "ברוכים הבאים ל-PDF Dark View!\n\nשפת המערכת שלך זוהתה כ-'{language}'.\nהאם ברצונך להשתמש בשפה זו עבור ממשק המשתמש?\n\nתוכל לשנות את השפה בכל עת דרך 'הגדרות → שפה'.",
        "welcome_message_language_not_available": "ברוכים הבאים ל-PDF Dark View!\n\nשפת המערכת שלך זוהתה כ-'{language}'.\nשפה זו עדיין לא מותקנת.\n\nהאם ברצונך להוריד כעת את התרגומים עבור {language} מ-GitHub?\n\n(השפה תשמש אז אוטומטית עבור ממשק המשתמש.)",
        "welcome_message_language_not_supported": "ברוכים הבאים ל-PDF Dark View!\n\nשפת המערכת שלך זוהתה כ-'{language}'.\nלמרבה הצער, אין עדיין תרגומים לשפה זו.\n\nממשק המשתמש יוצג ב-{fallback_language}.\n\nתוכל לשנות את השפה בכל עת דרך 'הגדרות → שפה'.\nאם תרצה, תוכל גם לתרום תרגום לשפה שלך:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "כן, השתמש בשפת המערכת",
        "welcome_keep_english": "לא, שמור אנגלית",
        "welcome_download_language": "כן, הורד {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "התוכנית נסגרת",

    }
