
# ============================================
# translations_th.py - Thailändisches Wörterbuch
# Vollständig sortiert nach Kategorien
# ============================================

def load_thai_strings():
    """Lädt alle thailändischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View โดย BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "โหลด PDF",
        'btn_text_window': "ข้อความ OCR",
        'btn_first': "หน้าแรก",
        'btn_prev': "หน้าก่อนหน้า",
        'btn_next': "หน้าถัดไป",
        'btn_last': "หน้าสุดท้าย",
        'btn_print': "พิมพ์",
        'btn_darkmode_light': "โหมดสว่าง",
        'btn_darkmode_dark': "โหมดมืด",
        'btn_delete_pages': "ลบหน้า",
        'btn_extract_pages': "แยกหน้า",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "ตกลง",
        'btn_cancel': "ยกเลิก",
        'btn_save': "บันทึก",
        'btn_close': "ปิด",
        'btn_delete': "ลบ",
        'btn_delete_all': "ลบทั้งหมด",
        'btn_copy': "คัดลอก",
        'btn_export': "ส่งออก",
        'btn_show': "แสดงรหัสผ่าน",
        'btn_hide': "ซ่อนรหัสผ่าน",
        'btn_authenticate': "ยืนยันตัวตน",
        'btn_settings': "ตั้งค่า",
        'btn_protect': "ป้องกัน",
        'btn_remove_password': "ลบรหัสผ่าน",
        'btn_manage': "จัดการรหัสผ่าน",
        'btn_retry': "ลองอีกครั้ง",
        'btn_select_all': "เลือกทั้งหมด",
        'btn_clear_selection': "ยกเลิกการเลือก",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "หน้า {0} จาก {1}",
        'page_count': "จาก {0}",
        'goto_page': "ไปที่หน้า",
        'page_simple': "หน้า {0}",
        'full_view_page': "ดูเต็มหน้าหน้า {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "ป้อนคำค้นหา + Enter",
        'search_results': "ผลลัพธ์: {0} จาก {1}",
        'search_nav_hint': "Enter: ถัดไป (Shift+Enter: ก่อนหน้า)",
        'search_no_results': "ไม่พบผลลัพธ์",
        'search_error': "ข้อผิดพลาดในการค้นหา",
        'search_active': "เปิดช่องค้นหา",
        'search_closed': "สิ้นสุดการค้นหา",
        'search_position': "หน้า {0} {1}",
        'search_pos_top': "บนสุด",
        'search_pos_upper': "ตอนบน",
        'search_pos_middle': "กลาง",
        'search_pos_lower': "ตอนล่าง",
        'search_pos_bottom': "ล่างสุด",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "การรู้จำข้อความเสร็จสมบูรณ์!",
        'ocr_success_title': "OCR สำเร็จ",
        'ocr_success_message': "เอกสารนี้สามารถค้นหาได้แล้ว",
        'ocr_failed': "OCR ล้มเหลว",
        'ocr_in_progress': "กำลังดำเนินการ OCR",
        'ocr_preparing': "กำลังเตรียม PDF...",
        'ocr_analyzing': "กำลังวิเคราะห์ PDF...",
        'ocr_optimizing': "กำลังปรับภาพให้เหมาะสม...",
        'ocr_recognizing': "กำลังรู้จำข้อความ...",
        'ocr_embedding': "กำลังฝังข้อความ...",
        'ocr_finalizing': "กำลังทำ PDF ให้เสร็จ...",
        'ocr_not_available': "OCR ไม่พร้อมใช้งาน",
        'ocr_install_message': "ไม่พบเครื่องมือ OCR\n\nโปรดติดตั้ง:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "จำเป็นต้องใช้ OCR",
        'ocr_question': "PDF นี้ไม่มีข้อความที่สามารถค้นหาได้\nคุณต้องการทำ OCR เพื่อให้ {0} ได้หรือไม่?",
        'ocr_perform': "ทำ OCR",
        'ocr_later': "ภายหลัง",
        'ocr_starting': "เริ่มต้น OCR แบบรับประกัน...",
        'ocr_success_voice': "OCR สำเร็จ PDF สามารถค้นหาได้แล้ว",
        'ocr_partial_success': "ดำเนินการ OCR แล้ว แต่มีปัญหาในการแทนที่\n\nบันทึกเวอร์ชันที่ค้นหาได้ที่:\n{0}\n\nข้อผิดพลาด: {1}",
        'ocr_partial_title': "OCR สำเร็จบางส่วน",
        'ocr_partial_voice': "ดำเนินการ OCR แล้ว แต่การแทนที่ล้มเหลว",
        'original_file': "ไฟล์ต้นฉบับ:",
        'old_size': "ขนาดเก่า:    {0} ไบต์",
        'new_size': "ขนาดใหม่: {0} ไบต์",
        'size_change': "เปลี่ยนแปลง: {0}{1} ไบต์",
        'backup_created_file': "สร้างสำเนาสำรองแล้ว:\n{0}",
        'backup_not_created': "สำเนาสำรอง: ไม่ได้สร้าง (ปิดการตั้งค่า)",
        'page_header': "=== หน้า {0} ===\n{1}\n",
        'scanned_page_header': "=== หน้า {0} (สแกน) ===\n[หน้านี้มีเฉพาะข้อความที่สแกน]\n[โปรดทำ OCR ด้วยตนเอง]\n",
        'scanned_warning': "⚠️ ข้อความที่สแกน - จำเป็นต้องใช้ OCR",
        'guaranteed_title': "สร้าง PDF ที่ค้นหาได้แล้ว",
        'guaranteed_message': "<b>สร้างเวอร์ชันที่ค้นหาได้แบบรับประกันแล้ว!</b>\n\nเนื่องจาก OCR อัตโนมัติล้มเหลว จึงได้สร้าง PDF ที่ค้นหาได้ทางเลือก:\n\n{0}\n\n<b>ไฟล์นี้ประกอบด้วย:</b>\n• ข้อความที่แยกได้ (ถ้ามี)\n• คำแนะนำสำหรับหน้าที่สแกน\n• สามารถค้นหาได้อย่างสมบูรณ์",
        'guaranteed_voice': "สร้าง PDF ที่ค้นหาได้แบบรับประกันแล้ว",
        'instruction_title': "คำแนะนำสำหรับ OCR",
        'instruction_file': "ไฟล์ต้นฉบับ: {0}",
        'instruction_text': "การรู้จำข้อความอัตโนมัติ (OCR) ล้มเหลว\nโปรดทำ OCR ด้วยตนเอง:\n\n1. ด้วย OCRmyPDF (บรรทัดคำสั่ง):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. ด้วย ADOBE ACROBAT (macOS/Windows):\n   • เปิด PDF ใน Acrobat\n   • เครื่องมือ > แก้ไข PDF\n   • เลือก 'รู้จำข้อความ'\n\n3. ด้วย PREVIEW (macOS):\n   • เปิด PDF ใน Preview\n   • ไฟล์ > ส่งออก...\n   • ตัวกรอง Quartz: 'ลดขนาดไฟล์'\n   • เปิดใช้งาน 'ทำ OCR'\n\n4. บริการ OCR ออนไลน์:\n   • smallpdf.com/th/ocr-pdf\n   • ilovepdf.com/th/ocr-pdf\n   • adobe.com/th/acrobat/online/pdf-to-word.html",
        'instruction_created': "สร้างคำแนะนำ OCR แล้ว",
        'instruction_created_message': "สร้างคำแนะนำโดยละเอียดแล้ว:\n\n{0}\n\nโปรดทำตามขั้นตอนสำหรับ OCR ด้วยตนเอง",
        'instruction_created_voice': "สร้างคำแนะนำ OCR แล้ว",
        'ocr_impossible': "OCR ไม่สามารถทำได้",
        'ocr_impossible_message': "ไม่สามารถทำ OCR ได้\n\nโปรดประมวลผล '{0}' ด้วยตนเองด้วยซอฟต์แวร์ OCR",
        'ocr_impossible_voice': "OCR ไม่สามารถทำได้ โปรดประมวลผลด้วยตนเอง",
        'emergency_title': "OCR ฉุกเฉิน",
        'emergency_message': "สร้าง PDF ฉุกเฉินแล้ว:\n\n{0}\n\nโปรดประมวลผลไฟล์นี้ด้วยตนเองด้วย OCR",
        'emergency_voice': "สร้าง PDF ฉุกเฉินแล้ว โปรดทำ OCR ด้วยตนเอง",
        'critical_error': "ข้อผิดพลาดร้ายแรง",
        'critical_error_message': "ไม่สามารถเริ่ม OCR ได้\n\nโปรดเริ่มโปรแกรมใหม่และตรวจสอบการติดตั้ง OCR",
        'critical_error_voice': "ข้อผิดพลาดร้ายแรง OCR",
        'ocr_question_html': "<p>PDF นี้ไม่มีข้อความที่ค้นหาได้<p>คุณต้องการทำ OCR เพื่อให้ <b>{0}</b> ได้หรือไม่?</p>",
        'ocr_question_voice': "จำเป็นต้องใช้ OCR PDF ไม่มีข้อความที่ค้นหาได้ คุณต้องการทำ OCR เพื่อให้ {0} ได้หรือไม่?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "ไม่มี PDF โหลด",
        'no_pdf_message': "ไม่มี PDF โหลด",
        'pdf_not_found': "ไม่พบไฟล์ PDF",
        'file_size': "ขนาดไฟล์",
        'bytes': "ไบต์",
        'kb': "กิโลไบต์",
        'mb': "เมกะไบต์",
        'backup_created': "สร้างสำเนาสำรองแล้ว",
        'backup_disabled': "ปิดการสำรองข้อมูล",
        'backup_activated': "เปิดการสร้างสำเนาสำรอง",
        'backup_deactivated': "ปิดการสร้างสำเนาสำรอง",
        'backup_status': "สำรองข้อมูล: {0}",
        'backup_on': "✔ เปิด",
        'backup_off': "✘ ปิด",
        'close_pdf': "ปิด PDF: {0}",
        'pdf_not_found_format': "ไม่พบไฟล์ PDF: {0}",
        'error_pdf_load_format': "ข้อผิดพลาดในการโหลด PDF: {0}",
        'load_failed_format': "โหลดไม่สำเร็จ:\n{0}",
        'decrypted_suffix': "(ถอดรหัสแล้ว)",
        'decryption_failed': "การถอดรหัสล้มเหลว",
        'decryption_error': "ข้อผิดพลาดในการถอดรหัส",
        'decryption_success': "ถอดรหัสสำเร็จ",
        'decryption_success_message': "ถอดรหัส PDF และบันทึกที่:\n\n{0}",
        'decryption_success_voice': "ถอดรหัส PDF และบันทึกแล้ว",
        'password_remove_error': "ข้อผิดพลาดในการลบรหัสผ่าน",
        'save_unencrypted': "บันทึก PDF ที่ไม่เข้ารหัสเป็น",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "บันทึกเป็น...",
        'save_copy': "บันทึกสำเนา",
        'save_success': "บันทึก PDF ที่: {0}",
        'save_encrypted': "บันทึก PDF ที่ป้องกันที่: {0}",
        'save_error': "ไม่สามารถบันทึก PDF ได้",
        'encryption_question': "คุณต้องการป้องกัน PDF ด้วยรหัสผ่านหรือไม่?",
        'encryption_yes': "ใช่",
        'encryption_no': "ไม่",
        'encryption_cancel': "ยกเลิก",
        'save_cancel': "ยกเลิกการบันทึก",
        'save_encrypted_voice': "เข้ารหัสและบันทึกไฟล์แล้ว",
        'save_success_voice': "บันทึกไฟล์ PDF โดยไม่เข้ารหัสแล้ว",
        'save_error_format': "ไม่สามารถบันทึก PDF ได้:\n{0}",
        'export_pages_success': "ส่งออก Pages สำเร็จ",
        'export_pages_error': "ส่งออก Pages ล้มเหลว",
        'export_pages_error_format': "ส่งออก Pages ล้มเหลว: {0}",
        'export_word_success': "ส่งออก Word สำเร็จ",
        'export_word_error': "ส่งออก Word ล้มเหลว",
        'export_word_error_format': "ส่งออก Word ล้มเหลว: {0}",
        'export_text_success': "ส่งออกข้อความสำเร็จ",
        'export_text_error': "ส่งออกข้อความล้มเหลว",
        'export_text_error_format': "ส่งออกข้อความล้มเหลว: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "จำเป็นต้องใช้รหัสผ่าน",
        'password_enter': "โปรดป้อนรหัสผ่าน",
        'password_confirm': "ยืนยันรหัสผ่าน",
        'password_new': "รหัสผ่านใหม่",
        'password_current': "รหัสผ่านปัจจุบัน",
        'password_save': "บันทึกรหัสผ่าน (เข้ารหัส)",
        'password_saved': "✓ บันทึกรหัสผ่านสำหรับไฟล์นี้แล้ว",
        'password_wrong': "รหัสผ่านผิด",
        'password_mismatch': "รหัสผ่านไม่ตรงกัน",
        'password_too_short': "รหัสผ่านสั้นเกินไป",
        'password_min_length': "รหัสผ่านต้องมีความยาวอย่างน้อย 4 ตัวอักษร",
        'password_strength': "ความแข็งแรงของรหัสผ่าน",
        'password_strength_very_weak': "อ่อนมาก",
        'password_strength_weak': "อ่อน",
        'password_strength_medium': "ปานกลาง",
        'password_strength_strong': "แข็งแรง",
        'password_strength_very_strong': "แข็งแรงมาก",
        'password_char_count': "({0} ตัวอักษร)",
        'password_match': "✓ ตรงกัน",
        'password_no_match': "✗ รหัสผ่านไม่ตรงกัน",
        'password_show': "แสดง",
        'password_hide': "ซ่อน",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "การจัดการรหัสผ่าน",
        'password_table_filename': "ชื่อไฟล์",
        'password_table_password': "รหัสผ่าน",
        'password_count': "บันทึกรหัสผ่าน {0} รายการ",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "ไม่มีรหัสผ่านที่บันทึก",
        'password_copied': "คัดลอกรหัสผ่าน {0} รายการแล้ว",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "คุณแน่ใจหรือไม่ว่าต้องการลบรหัสผ่านสำหรับ '{0}'?",
        'password_delete_multiple': "คุณแน่ใจหรือไม่ว่าต้องการลบรหัสผ่านที่เลือก {0} รายการ?",
        'password_delete_all_confirm': "คุณแน่ใจหรือไม่ว่าต้องการลบรหัสผ่านที่บันทึกทั้งหมด {0} รายการ?",
        'password_deleted': "ลบรหัสผ่าน {0} รายการแล้ว",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "ลบรหัสผ่านทั้งหมดแล้ว",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "เครื่องสร้างรหัสผ่าน",
        'generator_generated': "รหัสผ่านที่สร้าง:",
        'generator_regenerate': "สร้างใหม่",
        'generator_copy': "คัดลอก",
        'generator_use': "ใช้",
        'generator_settings': "ตั้งค่า",
        'generator_length': "ความยาว:",
        'generator_group_every': "ตัวคั่นทุก",
        'generator_group_chars': "ตัวอักษร ตัวคั่น:",
        'generator_uppercase': "ตัวพิมพ์ใหญ่ (A-Z)",
        'generator_lowercase': "ตัวพิมพ์เล็ก (a-z)",
        'generator_digits': "ตัวเลข (0-9)",
        'generator_symbols': "สัญลักษณ์พิเศษ (!@#$%^&*)",
        'generator_exclude': "ไม่รวม:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "จำเป็นต้องใช้รหัสผ่านหลัก",
        'master_password_setup': "ตั้งค่ารหัสผ่านหลัก",
        'master_password_change': "เปลี่ยนรหัสผ่านหลัก",
        'master_password_enter': "โปรดป้อนรหัสผ่านหลักของคุณ",
        'master_password_choose': "เลือกรหัสผ่านหลักที่แข็งแรง (อย่างน้อย 8 ตัวอักษร)",
        'master_password_new': "โปรดป้อนรหัสผ่านหลักใหม่ของคุณ",
        'master_password_confirm': "ยืนยันรหัสผ่าน",
        'master_password_authenticate': "ยืนยันตัวตน",
        'master_password_success': "ตั้งค่ารหัสผ่านหลักสำเร็จ",
        'master_password_changed': "เปลี่ยนรหัสผ่านหลักสำเร็จ",
        'master_password_removed': "ลบรหัสผ่านหลักและรหัสผ่านทั้งหมดแล้ว",
        'master_password_remove': "ลบรหัสผ่านหลัก",
        'master_password_remove_confirm': "คุณแน่ใจหรือไม่ว่าต้องการลบรหัสผ่านทั้งหมด?\n\nการดำเนินการนี้ไม่สามารถย้อนกลับได้!",
        'master_password_export_before': "คุณต้องการส่งออกสำเนาสำรองก่อนหรือไม่?",
        'master_password_export_delete': "ส่งออกและลบ",
        'master_password_delete_now': "ลบทันที",
        'master_password_for_signatures': "หากต้องการใช้ลายเซ็น คุณต้องตั้งค่ารหัสผ่านหลัก\n\nคุณต้องการตั้งค่ารหัสผ่านหลักตอนนี้หรือไม่?",
        'master_password_for_private': "หากต้องการใช้บล็อกข้อความส่วนตัว คุณต้องตั้งค่ารหัสผ่านหลัก\n\nคุณต้องการตั้งค่ารหัสผ่านหลักตอนนี้หรือไม่?",
        'master_password_info': """
            <b>🔐 ไม่มีรหัสผ่านหลัก:</b><br>
            • ไม่สามารถแสดง คัดลอก และส่งออกรหัสผ่านได้<br>
            • สามารถลบรหัสผ่านได้เสมอ (แม้ไม่มีรหัสผ่านหลัก)<br><br>

            <b>🔐 มีรหัสผ่านหลัก:</b><br>
            • ฟังก์ชันทั้งหมดพร้อมใช้งานหลังยืนยันตัวตน<br>
            • รหัสผ่านถูกเข้ารหัสด้วยรหัสผ่านหลัก<br>
            • ความยาวขั้นต่ำ: 8 ตัวอักษร<br>
            • จัดเก็บแฮช SHA-256 อย่างปลอดภัย<br><br>

            <b>สำคัญ:</b><br>
            • หากลืมรหัสผ่านหลัก: ไม่สามารถกู้คืนรหัสผ่านได้<br>
            • เมื่อลบรหัสผ่านหลัก: รหัสผ่านทั้งหมดถูกลบ<br>
            • มีตัวเลือกส่งออกก่อนลบ<br>
            • สามารถเปลี่ยนรหัสผ่านหลักได้ทุกเมื่อ
        """,
        'signature_auth_disabled': "ปิดการถามรหัสผ่านสำหรับลายเซ็น",
        'template_auth_disabled': "ปิดการถามรหัสผ่านสำหรับบล็อกข้อความส่วนตัว",
        'master_password_for_signatures_settings': "หากต้องการใช้ลายเซ็น คุณต้องตั้งค่ารหัสผ่านหลัก\n\nไปที่ การตั้งค่า - การจัดการรหัสผ่าน",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "ป้องกัน PDF",
        'protect_info': "ไฟล์ '{0}' จะถูกป้องกันด้วยรหัสผ่าน",
        'protect_instruction': "โปรดป้อนรหัสผ่านที่ต้องการสองครั้งเพื่อป้องกันเอกสาร หรือใช้เครื่องสร้างรหัสผ่านทางด้านขวาของช่องป้อนข้อมูล",
        'protect_success': "ป้องกัน PDF สำเร็จและบันทึกที่:\n{0}\n\nรหัสผ่าน: {1}\n\nคุณต้องการเปิด PDF ที่ป้องกันตอนนี้หรือไม่?",
        'protect_open': "ใช่",
        'protect_skip': "ไม่",
        'protect_error': "ข้อผิดพลาดในการป้องกัน PDF",
        'protect_open_title': "เปิด PDF ที่ป้องกัน",
        'protect_question': "เสร็จสิ้น คุณต้องการเปิด PDF ที่ป้องกันตอนนี้หรือไม่? ใช่หรือไม่?",
        'password_cancel': "ยกเลิกไดอะล็อกรหัสผ่าน",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "ลบหน้า",
        'pages_extract': "แยกหน้า",
        'pages_insert': "แทรกหน้า",
        'pages_move': "ย้ายหน้า",
        'pages_delete_options': "ตัวเลือกการลบ",
        'pages_delete_empty': "ลบหน้าว่างทั้งหมด",
        'pages_delete_current': "ลบหน้าปัจจุบัน",
        'pages_delete_range': "ลบช่วงหน้า",
        'pages_extract_options': "ตัวเลือกการแยก",
        'pages_extract_current': "แยกหน้าปัจจุบัน",
        'pages_extract_range': "แยกช่วงหน้า",
        'pages_insert_position': "ตำแหน่งแทรก",
        'pages_insert_before': "แทรกก่อนหน้า:",
        'pages_insert_select': "เลือก PDF",
        'pages_insert_none': "ไม่ได้เลือก PDF",
        'pages_move_source': "หน้าที่จะย้าย",
        'pages_move_from': "จากหน้า:",
        'pages_move_to': "ถึงหน้า:",
        'pages_move_target': "ตำแหน่งเป้าหมาย",
        'pages_move_before': "ย้ายก่อนหน้า:",
        'pages_move_hint': "หมายเหตุ: หน้า 1 = ต้น, {0} = ปลาย",
        'pages_range_invalid': "หน้าเริ่มต้นต้องน้อยกว่าหรือเท่ากับหน้าสิ้นสุด",
        'pages_position_invalid': "ตำแหน่งเป้าหมายต้องไม่อยู่ในช่วงที่กำลังย้าย",
        'pages_no_pdf_selected': "ไม่ได้เลือก PDF",
        'pages_deleted': "ลบ {0} หน้าแล้ว",
        'pages_extracted': "แยก: {0}\nบันทึกที่: {1}\nขนาดไฟล์: {2:.1f} KB",
        'pages_inserted': "แทรก {0} หน้า",
        'pages_moved': "ย้าย {0} หน้าแล้ว",
        'pages_deleted_none': "ไม่มีการลบหน้า",
        'pages_delete_progress': "กำลังลบหน้า...",
        'pages_deleted_with_backup': "ลบ {0} หน้าแล้ว\n\nสำรอง: {1}",
        'pages_deleted_voice': "สร้างสำรองและลบ {0} หน้าแล้ว",
        'info': "หมายเหตุ",
        'error_dialog_creation': "ไม่สามารถสร้างไดอะล็อกได้",
        'extract_page_single': "แยกหน้า {0}",
        'extract_page_range': "แยกหน้า {0}-{1}",
        'extract_success_voice': "แยกหน้าสำเร็จ",
        'extract_error_format': "ข้อผิดพลาดในการแยก: {0}",
        'pages_inserted_voice': "แทรก {0} หน้าแล้ว",
        'insert_error_format': "ข้อผิดพลาดในการแทรก: {0}",
        'pages_move_progress': "กำลังย้ายหน้า...",
        'pages_moved_with_backup': "ย้าย {0} หน้าแล้ว\n\nสำรอง: {1}",
        'move_success_title': "ย้ายสำเร็จ",
        'pages_moved_voice': "ย้าย {0} หน้าสำเร็จ",
        'mark_removed': "ลบเครื่องหมายจากหน้า {0}",
        'mark_empty': "ทำเครื่องหมายหน้าว่างที่หน้า {0}",
        'mark_export_removed': "ลบเครื่องหมายส่งออกจากหน้า {0}",
        'mark_export': "ทำเครื่องหมายหน้า {0} สำหรับส่งออก",
        'no_empty_pages': "ไม่มีหน้าว่างที่ทำเครื่องหมายเพื่อลบ",
        'delete_empty_confirm': "คุณต้องการลบหน้าว่างที่ทำเครื่องหมายทั้งหมด {0} หน้าหรือไม่?",
        'delete_empty_confirm_voice': "ลบหน้าว่างที่ทำเครื่องหมายทั้งหมด {0} หน้าตอนนี้? ใช่หรือไม่",
        'empty_pages_deleted': "ลบหน้าว่าง {0} หน้า",
        'no_export_pages': "ไม่มีหน้าที่ทำเครื่องหมายสำหรับส่งออก",
        'overwrite_title': "แทนที่ไฟล์ที่มีอยู่",
        'overwrite_question': "ไฟล์\n\n{0}\n\nมีอยู่แล้ว\nคุณต้องการแทนที่หรือไม่?",
        'overwrite_voice': "แทนที่ไฟล์ที่มีอยู่? ใช่หรือไม่",
        'page_skipped': "ข้ามหน้า {0}",
        'export_complete': "ส่งออกเสร็จสิ้น",
        'export_complete_voice': "การส่งออกเสร็จสิ้น",
        'no_pages_exported': "ไม่มีหน้าถูกส่งออก",
        'export_cancelled': "ยกเลิกการส่งออก",
        'pages_exported': "ส่งออก {0} หน้าไปยัง {1}",
        'export_page_title': "ส่งออกหน้า",
        'page_exported': "ส่งออกหน้า {0} ไปยัง {1}",
        'export_error': "ข้อผิดพลาดในการส่งออก",
        'export_marked_title': "ส่งออกหน้าที่ทำเครื่องหมาย",
        'rotate_all_title': "หมุนทุกหน้า",
        'rotate_all_question': "คุณต้องการหมุนทุกหน้า 90 องศาไปทางขวาหรือไม่?",
        'rotate_all_voice': "คุณต้องการหมุนทุกหน้า 90 องศาไปทางขวาหรือไม่? ใช่หรือไม่?",
        'all_pages_rotated': "หมุนทุกหน้าแล้ว",
        'page_rotated': "หมุนหน้า {0} แล้ว",
        'rotate_error': "ไม่สามารถหมุนหน้าได้",
        'delete_page_confirm': "คุณต้องการลบหน้า {0} หรือไม่?",
        'delete_page_confirm_voice': "คุณแน่ใจหรือไม่ว่าต้องการลบหน้า {0}? ใช่หรือไม่",
        'page_deleted': "ลบหน้า {0} แล้ว",
        'delete_error': "ไม่สามารถลบหน้าได้",
        'pages_deleted_voice': "ลบ {0} หน้าแล้ว",
        'pages_exported_split': "ส่งออก {0} หน้าสำเร็จ",
        'pages_skipped': "ข้าม {0} หน้า",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "แยกหน้า (ขั้นสูง)",
        'pdf_splitter_title': "ตัวแบ่งและแยก PDF",
        'pdf_splitter_load': " เลือกไฟล์ PDF",
        'pdf_splitter_info': "โปรดเลือกตัวเลือกสำหรับเอกสาร PDF ของคุณ",
        'pdf_splitter_basic': "การดำเนินการพื้นฐาน",
        'pdf_splitter_single': "แบ่งเป็นหน้าเดี่ยว",
        'pdf_splitter_range': "แยกหน้า:",
        'pdf_splitter_range_placeholder': "เช่น 1-3,5,7-9",
        'pdf_splitter_clean': "การดำเนินการทำความสะอาด",
        'pdf_splitter_remove_empty': "ลบหน้าว่างทั้งหมด",
        'pdf_splitter_remove': "ลบช่วงหน้า:",
        'pdf_splitter_remove_placeholder': "เช่น 2,4-6",
        'pdf_splitter_process': "ประมวลผล PDF",
        'pdf_splitter_loaded': "โหลด PDF แล้ว โปรดเลือกตัวเลือก",
        'pdf_read_error': "ไม่สามารถอ่าน PDF ได้",
        'pages': "หน้า",
        'pages_created': "สร้างหน้าแล้ว",
        'range_empty': "โปรดป้อนช่วงหน้า",
        'range_invalid': "ช่วงหน้าไม่ถูกต้อง",
        'range_created': "สร้าง PDF ใหม่ด้วยหน้าที่เลือก:\n{0}",
        'empty_removed': "ลบหน้าว่าง {0} หน้า\nผลลัพธ์: {1}",
        'remove_empty': "โปรดป้อนหน้าที่จะลบ",
        'remove_invalid': "หน้าที่จะลบไม่ถูกต้อง",
        'remove_done': "สร้าง PDF ที่ทำความสะอาดแล้ว:\n{0}",
        'open_folder': "เปิดโฟลเดอร์",
        'show_in_finder': "แสดงใน Finder",
        'pdf_splitter_no_pdf': "โปรดโหลดไฟล์ PDF ก่อน",
        'process_error': "ข้อผิดพลาดในการประมวลผล PDF",
        'pages_created_voice': "สร้าง {0} หน้าแล้ว",
        'range_created_voice': "สร้าง PDF ด้วยหน้าที่เลือกแล้ว",
        'empty_removed_voice': "ลบหน้าว่าง {0} หน้าแล้ว",
        'remove_done_voice': "สร้าง PDF ที่ทำความสะอาดแล้ว",
        'pdf_splitter_split_groups': "แต่ละกลุ่มต่อเนื่องเป็นไฟล์แยก",
        'range_created_single': "สร้าง PDF ใหม่:\n{0}",
        'range_created_multiple': "สร้างไฟล์ PDF {0} ไฟล์",
        'range_created_voice_single': "สร้าง PDF หนึ่งไฟล์ด้วยหน้าที่เลือก",
        'range_created_voice_multiple': "สร้างไฟล์ PDF {0} ไฟล์",
        'empty_removed_none_left': "ไม่มีหน้าเหลือ",
        'empty_removed_all_empty': "ทุกหน้าถูกตรวจพบว่าว่างและจะถูกลบ ไม่ได้สร้างไฟล์",
        'preview_single': "แสดงตัวอย่าง: {0}",
        'preview_enter_range': "โปรดป้อนช่วงหน้า",
        'preview_invalid_range': "ช่วงหน้าไม่ถูกต้อง",
        'preview_file': "แสดงตัวอย่าง: {0}",
        'preview_files': "แสดงตัวอย่าง: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "เริ่มพิมพ์",
        'print_sent': "ส่งงานพิมพ์แล้ว",
        'print_now': "พิมพ์ทันที",
        'print_error': "ข้อผิดพลาดในการพิมพ์ทันที",
        'print_limited': "ฟังก์ชันการพิมพ์จำกัดบนระบบนี้",
        'print_error_format': "ข้อผิดพลาดในการพิมพ์ทันที: {0}",
        'warning': "คำเตือน",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "สลับไปโหมดสว่าง",
        'mode_switch_to_dark': "สลับไปโหมดมืด",
        'mode_dark_activated': "เปิดโหมดมืด",
        'mode_light_activated': "เปิดโหมดสว่าง",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "ดูเต็มหน้า",
        'zoom_two_pages': "สองหน้าคู่กัน",
        'zoom_overview': "โหมดภาพรวม",
        'zoom_cannot_during_search': "ไม่สามารถซูมระหว่างค้นหาได้",
        'zoom_exit_first': "โปรดออกจากโหมดซูมก่อน",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "เปิดใช้การลากแล้ววาง",
        'drag_disabled': "ปิดใช้การลากแล้ววาง",
        'drag_page_grab': "จับหน้า {0}",
        'drag_page_dropped': "วางหน้า {0} ที่ตำแหน่ง {1}",
        'drag_position_invalid': "ตำแหน่งไม่ถูกต้อง",
        'drag_same_position': "หน้า {0} ยังคงอยู่ที่ตำแหน่ง {0}",
        'drag_error': "ข้อผิดพลาดในการย้าย",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "ป้อนข้อความพร้อมการจัดรูปแบบขั้นสูงและการจัดการบล็อกข้อความ",
        'text_templates': "บล็อกข้อความที่มี:",
        'text_name': "ชื่อ",
        'text_preview': "ตัวอย่างข้อความ",
        'text_enter': "ข้อความ:",
        'text_font_size': "ขนาดตัวอักษร:",
        'text_formatting': "การจัดรูปแบบ:",
        'text_bold': "ตัวหนา",
        'text_italic': "ตัวเอียง",
        'text_underline': "ขีดเส้นใต้",
        'text_alignment': "การจัดตำแหน่ง:",
        'text_left': "ซ้าย",
        'text_center': "กลาง",
        'text_right': "ขวา",
        'text_color': "สีข้อความ:",
        'text_opacity': "ความทึบ:",
        'text_word_wrap': "ตัดข้อความ:",
        'text_auto': "อัตโนมัติ",
        'text_page_width_95': "ความกว้างหน้า (95%)",
        'text_page_width_85': "กว้างมาก (85%)",
        'text_page_width_75': "กว้าง (75%)",
        'text_page_width_60': "ค่อนข้างกว้าง (60%)",
        'text_page_width_50': "ปานกลาง (50%)",
        'text_page_width_30': "แคบ (30%)",
        'text_page_width_20': "แคบกว่า (20%)",
        'text_page_width_10': "แคบมาก (10%)",
        'text_no_wrap': "ไม่ตัด",
        'text_private': "บล็อกข้อความส่วนตัว (ต้องยืนยันตัวตน)",
        'text_preview_label': "ตัวอย่าง:",
        'text_preview_placeholder': "ตัวอย่างข้อความจะแสดงที่นี่...",
        'text_no_text': "(ไม่มีข้อความ)",
        'text_save_template': "💾 บันทึกเป็นบล็อก",
        'text_delete_template': "🗑 ลบบล็อกข้อความที่เลือก",
        'text_show_private': "แสดงส่วนตัว",
        'text_hide_private': "ซ่อนส่วนตัว",
        'text_use': "✅ ใช้ข้อความ",
        'text_saved': "บันทึกบล็อกข้อความเป็น:\n{0}",
        'text_saved_voice': "บันทึกบล็อกข้อความแล้ว",
        'text_deleted': "ลบบล็อกข้อความแล้ว",
        'text_no_text_to_save': "ไม่มีข้อความที่จะบันทึก",
        'text_no_templates': "ไม่พบบล็อกข้อความ",
        'text_private_master_required': "บล็อกส่วนตัวสามารถใช้ได้เฉพาะเมื่อตั้งค่ารหัสผ่านหลักแล้ว\n\nคุณต้องการตั้งค่ารหัสผ่านหลักตอนนี้หรือไม่?",
        'text_filename': "ชื่อไฟล์สำหรับบล็อกข้อความ (ไม่มี 'Text_' และ '.txt'):",
        'text_filename_hint': "ตัวอย่าง: 'โทรศัพท์บ้าน' จะถูกบันทึกเป็น 'Text_โทรศัพท์บ้าน.txt'",
        'text_save_hint': "บล็อกข้อความจะถูกบันทึกพร้อมการจัดรูปแบบโดยอัตโนมัติ",
        'text_guide_title': "การป้อนข้อความ - คำแนะนำ",
        'text_delete_confirm': "คุณแน่ใจหรือไม่ว่าต้องการลบบล็อกข้อความนี้?\n\nไฟล์: {0}\nข้อความ: {1}...",
        'text_make_public': "ทำเครื่องหมายเป็นสาธารณะ",
        'text_make_private': "ทำเครื่องหมายเป็นส่วนตัว",
        'text_privacy_changed': "เปลี่ยนสถานะส่วนตัวแล้ว",
        'text_private_always': "ส่วนตัวแสดงเสมอ (การตั้งค่า)",
        'text_mode_required': "โปรดเปิดโหมดข้อความก่อน",
        'text_continue_editing': "แก้ไขต่อ - เคอร์เซอร์ที่ท้ายข้อความ",
        'text_no_input': "ไม่ได้ป้อนข้อความ - ทิ้งข้อความ",
        'save_dialog_question': "คุณต้องการดำเนินการต่ออย่างไร?",
        'text_save_question': "บันทึกข้อความและกากบาททั้งหมด ปรับแต่ง แก้ไขต่อ หรือทิ้ง?",
        'copy_cross': "คัดลอกกากบาท",
        'paste_cross': "วางกากบาท",
        'paste_text': "วางข้อความ",
        'cross_discarded': "ทิ้งกากบาท",
        'all_discarded': "ทิ้งทั้งหมด",
        'text_discarded': "ทิ้งข้อความ",
        'no_texts_to_save': "ไม่มีข้อความที่จะบันทึก",
        'no_valid_texts': "ไม่มีข้อความที่ถูกต้องสำหรับบันทึก",
        'text_word_singular': "ข้อความ",
        'text_word_plural': "ข้อความ",
        'cross_word_singular': "กากบาท",
        'cross_word_plural': "กากบาท",
        'texts_saved_title': "บันทึกข้อความแล้ว",
        'texts_crosses_saved': "แทรก {0} {1} และ {2} {3} ลงใน PDF\n\nโหลด PDF ใหม่...",
        'texts_crosses_saved_voice': "บันทึก {0} {1} และ {2} {3} แล้ว",
        'texts_saved': "แทรก {0} {1} ลงใน PDF\n\nโหลด PDF ใหม่...",
        'texts_saved_voice': "บันทึก {0} {1} แล้ว",
        'crosses_saved': "แทรก {0} {1} ลงใน PDF\n\nโหลด PDF ใหม่...",
        'crosses_saved_voice': "บันทึก {0} {1} แล้ว",
        'elements_saved': "แทรก {0} รายการลงใน PDF\n\nโหลด PDF ใหม่...",
        'elements_saved_voice': "บันทึก {0} รายการแล้ว",
        'text_window_load_error': "ไม่สามารถโหลดหน้าต่างข้อความได้",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **การป้อนข้อความและบล็อกข้อความ – คำแนะนำโดยละเอียด**

        **1. การแทรกและแก้ไขข้อความ**
        - คลิกขวาที่ตำแหน่งที่ต้องการในเอกสารและเลือก "แทรกข้อความ"
        - จะเปิดไดอะล็อกที่คุณสามารถป้อนและจัดรูปแบบข้อความ:
        • ขนาดตัวอักษร ตัวหนา ตัวเอียง ขีดเส้นใต้
        • สีข้อความ (เลือกได้อิสระ)
        • ความโปร่งใส (ความทึบ) ด้วยแถบเลื่อน
        • การตัดข้อความ (ความกว้างต่าง ๆ เช่น ความกว้างหน้า แคบ ไม่ตัด)
        - หลังจากยืนยัน ข้อความจะปรากฏที่ตำแหน่งคลิก คุณสามารถย้ายด้วยเมาส์หรือปุ่มลูกศร
        - ดับเบิลคลิกที่ข้อความเพื่อเปิดโหมดแก้ไข; ESC เพื่อออก

        **2. การจัดการบล็อกข้อความ (เทมเพลต)**
        - ในไดอะล็อกข้อความ คุณจะเห็นรายการบล็อกข้อความทั้งหมดที่บันทึกไว้ทางซ้าย
        - **บันทึกบล็อก:** ป้อนข้อความ จัดรูปแบบ และคลิก "💾 บันทึกเป็นบล็อก" ป้อนชื่อไฟล์ (ไม่มีนามสกุล)
        - **โหลดบล็อก:** คลิกชื่อที่ต้องการในรายการ ข้อความและการจัดรูปแบบจะถูกนำมาใช้และสามารถปรับแต่งได้
        - **ลบ:** คลิกขวาที่บล็อกเพื่อลบหรือเปลี่ยนสถานะส่วนตัว

        **3. บล็อกข้อความส่วนตัว (รหัสผ่านหลัก)**
        - หากคุณตั้งค่ารหัสผ่านหลัก (ในการตั้งค่า → การจัดการรหัสผ่าน) คุณสามารถทำเครื่องหมายบล็อกเป็น "ส่วนตัว"
        - เปิดใช้งานช่องทำเครื่องหมาย "บล็อกข้อความส่วนตัว" ในไดอะล็อกก่อนบันทึก
        - บล็อกส่วนตัวจะแสดงในรายการเฉพาะเมื่อคุณป้อนรหัสผ่านหลักครั้งเดียวในแต่ละเซสชัน (ยืนยันตัวตนผ่านไอคอนกุญแจหรือเมื่อเข้าถึงครั้งแรก)
        - วิธีนี้ช่วยปกป้องบล็อกข้อความที่เป็นความลับจากการเข้าถึงของผู้อื่น

        **4. การแทรกกากบาท**
        - ผ่านเมนูบริบท คุณสามารถแทรกกากบาทกราฟิก (เช่น สำหรับช่องทำเครื่องหมาย)
        - ขนาด ความหนาของเส้น และสีของกากบาทสามารถปรับได้ทั่วโลกในการตั้งค่า (เมนู "การตั้งค่า" → "การตั้งค่ากากบาท")
        - คลิกขวาที่กากบาทที่มีอยู่เพื่อเปลี่ยนแปลงแยกต่างหาก

        **5. การดำเนินการกลุ่ม**
        - หากคุณวางข้อความหรือกากบาทหลายรายการในหน้าเดียว คุณสามารถบันทึกหรือทิ้งองค์ประกอบทั้งหมดพร้อมกันผ่านเมนูบริบท (คลิกขวาในโหมดข้อความ)
        - เมื่อบันทึก องค์ประกอบทั้งหมดจะถูกฝังลงใน PDF และคงอยู่ในรูปแบบกราฟิกเวกเตอร์

        **6. ปุ่มลัดในโหมดข้อความ**
        - ปุ่มลูกศร: ย้ายองค์ประกอบ
        - Ctrl+ปุ่มลูกศร: ขยับทีละมาก
        - Enter: เปิดไดอะล็อกบันทึก (บันทึกทั้งหมด / ปรับแต่ง / ทิ้ง)
        - ESC: ทิ้งองค์ประกอบปัจจุบัน
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 การป้อนข้อความและบล็อกข้อความ – คำแนะนำโดยละเอียด</strong></p>

        <p><strong>1. การแทรกและแก้ไขข้อความ</strong></p>
        <ul>
        <li>คลิกขวาที่ตำแหน่งที่ต้องการในเอกสารและเลือก "แทรกข้อความ"</li>
        <li>จะเปิดไดอะล็อกที่คุณสามารถป้อนและจัดรูปแบบข้อความ:<br/>
        • ขนาดตัวอักษร ตัวหนา ตัวเอียง ขีดเส้นใต้<br/>
        • สีข้อความ (เลือกได้อิสระ)<br/>
        • ความโปร่งใส (ความทึบ) ด้วยแถบเลื่อน<br/>
        • การตัดข้อความ (ความกว้างต่าง ๆ เช่น ความกว้างหน้า แคบ ไม่ตัด)</li>
        <li>หลังจากยืนยัน ข้อความจะปรากฏที่ตำแหน่งคลิก คุณสามารถย้ายด้วยเมาส์หรือปุ่มลูกศร</li>
        <li>ดับเบิลคลิกที่ข้อความเพื่อเปิดโหมดแก้ไข; ESC เพื่อออก</li>
        </ul>

        <p><strong>2. การจัดการบล็อกข้อความ (เทมเพลต)</strong></p>
        <ul>
        <li>ในไดอะล็อกข้อความ คุณจะเห็นรายการบล็อกข้อความทั้งหมดที่บันทึกไว้ทางซ้าย</li>
        <li><strong>บันทึกบล็อก:</strong> ป้อนข้อความ จัดรูปแบบ และคลิก "💾 บันทึกเป็นบล็อก" ป้อนชื่อไฟล์ (ไม่มีนามสกุล)</li>
        <li><strong>โหลดบล็อก:</strong> คลิกชื่อที่ต้องการในรายการ ข้อความและการจัดรูปแบบจะถูกนำมาใช้และสามารถปรับแต่งได้</li>
        <li><strong>ลบ:</strong> คลิกขวาที่บล็อกเพื่อลบหรือเปลี่ยนสถานะส่วนตัว</li>
        </ul>

        <p><strong>3. บล็อกข้อความส่วนตัว (รหัสผ่านหลัก)</strong></p>
        <ul>
        <li>หากคุณตั้งค่ารหัสผ่านหลัก (ในการตั้งค่า → การจัดการรหัสผ่าน) คุณสามารถทำเครื่องหมายบล็อกเป็น "ส่วนตัว"</li>
        <li>เปิดใช้งานช่องทำเครื่องหมาย "บล็อกข้อความส่วนตัว" ในไดอะล็อกก่อนบันทึก</li>
        <li>บล็อกส่วนตัวจะแสดงในรายการเฉพาะเมื่อคุณป้อนรหัสผ่านหลักครั้งเดียวในแต่ละเซสชัน (ยืนยันตัวตนผ่านไอคอนกุญแจหรือเมื่อเข้าถึงครั้งแรก)</li>
        <li>วิธีนี้ช่วยปกป้องบล็อกข้อความที่เป็นความลับจากการเข้าถึงของผู้อื่น</li>
        </ul>

        <p><strong>4. การแทรกกากบาท</strong></p>
        <ul>
        <li>ผ่านเมนูบริบท คุณสามารถแทรกกากบาทกราฟิก (เช่น สำหรับช่องทำเครื่องหมาย)</li>
        <li>ขนาด ความหนาของเส้น และสีของกากบาทสามารถปรับได้ทั่วโลกในการตั้งค่า (เมนู "การตั้งค่า" → "การตั้งค่ากากบาท")</li>
        <li>คลิกขวาที่กากบาทที่มีอยู่เพื่อเปลี่ยนแปลงแยกต่างหาก</li>
        </ul>

        <p><strong>5. การดำเนินการกลุ่ม</strong></p>
        <ul>
        <li>หากคุณวางข้อความหรือกากบาทหลายรายการในหน้าเดียว คุณสามารถบันทึกหรือทิ้งองค์ประกอบทั้งหมดพร้อมกันผ่านเมนูบริบท (คลิกขวาในโหมดข้อความ)</li>
        <li>เมื่อบันทึก องค์ประกอบทั้งหมดจะถูกฝังลงใน PDF และคงอยู่ในรูปแบบกราฟิกเวกเตอร์</li>
        </ul>

        <p><strong>6. ปุ่มลัดในโหมดข้อความ</strong></p>
        <ul>
        <li>ปุ่มลูกศร: ย้ายองค์ประกอบ</li>
        <li>Ctrl+ปุ่มลูกศร: ขยับทีละมาก</li>
        <li>Enter: เปิดไดอะล็อกบันทึก (บันทึกทั้งหมด / ปรับแต่ง / ทิ้ง)</li>
        <li>ESC: ทิ้งองค์ประกอบปัจจุบัน</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "การตั้งค่ากากบาท",
        'cross_properties': "คุณสมบัติกากบาท",
        'cross_size': "ขนาด (px):",
        'cross_line_width': "ความหนาของเส้น:",
        'cross_color': "สี:",
        'cross_choose_color': "เลือก",
        'cross_fine_tuning': "ปรับละเอียดเมื่อบันทึก (พิกเซล)",
        'cross_offset_x': "ออฟเซ็ต X:",
        'cross_offset_y': "ออฟเซ็ต Y:",
        'cross_offset_x_tooltip': "ค่าลบเลื่อนกากบาทไปทางซ้ายเมื่อบันทึก ค่าบวกไปทางขวา",
        'cross_offset_y_tooltip': "ค่าลบเลื่อนกากบาทขึ้นเมื่อบันทึก ค่าบวกลง",
        'cross_preview': "ตัวอย่าง",
        'cross_save': "ใช้การตั้งค่า",
        'cross_customized': "ปรับกากบาทแล้ว",
        'cross_settings_applied': "บันทึกการตั้งค่ากากบาท\nขนาด: {0}px, ความหนาเส้น: {1}px\n{2}",
        'cross_updated_count': "อัปเดตกากบาทที่มีอยู่ {0} รายการแล้ว",
        'cross_no_crosses': "ไม่พบกากบาทที่มีอยู่",
        'cross_settings_applied_all': "ใช้การตั้งค่ากากบาทกับกากบาททั้งหมด {0} รายการ",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "การตั้งค่าลายเซ็น",
        'signature_1': "ลายเซ็น 1",
        'signature_2': "ลายเซ็น 2",
        'signature_select': "เลือกลายเซ็น",
        'signature_add': "➕ เพิ่มลายเซ็นใหม่...",
        'signature_size': "ขนาดสำหรับลายเซ็น {0} (%):",
        'signature_common': "การตั้งค่าทั่วไป",
        'signature_timestamp': "เพิ่มประทับเวลาอัตโนมัติ",
        'signature_location': "สถานที่เริ่มต้น:",
        'signature_timestamp_size': "ขนาดตัวอักษรประทับเวลา:",
        'signature_no_files': "-- ไม่พบลายเซ็น --",
        'signature_insert': "แทรกลายเซ็น",
        'signature_insert_1': "แทรกลายเซ็น 1",
        'signature_insert_2': "แทรกลายเซ็น 2",
        'signature_customize': " ปรับแต่งลายเซ็นนี้",
        'signature_discard': " ทิ้งลายเซ็นนี้",
        'signature_save_all': " บันทึกลายเซ็นทั้งหมด",
        'signature_discard_all': " ทิ้งลายเซ็นทั้งหมด",
        'signature_guide_title': "ลายเซ็น - คำแนะนำ",
        'signature_guide': """
📝 ลายเซ็น - คำแนะนำด่วน

- ตั้งค่ารหัสผ่านหลัก
- กำหนดค่าลายเซ็นในเมนูการตั้งค่า
  (ขนาด, ประทับเวลา ...)
- แทรกด้วยคลิกขวาที่ตำแหน่งที่ต้องการ
  (ต้องใช้รหัสผ่านหลักครั้งเดียวต่อเซสชัน)
- ย้ายลายเซ็นด้วยเมาส์หรือปุ่มลูกศร
- สามารถแทรกลายเซ็นหลายรายการต่อเนื่องกัน
- แต่ละลายเซ็นสามารถปรับแต่งแยกกัน
- ทิ้งลายเซ็นแต่ละรายการ
- บันทึก / ทิ้งลายเซ็นทั้งหมดพร้อมกัน
- หรือใช้แถบเมนูก็ได้
        """,
        'signature_placeholder': "ไม่มีตัวอย่าง",
        'signature_info': "ลายเซ็น {0}: {1}×{2} px ({3}% ของ {4}×{5})",
        'signature_info_placeholder': "การตั้งค่าสำหรับลายเซ็น {0}",
        'signature_inserted': "แทรกลายเซ็น {0} ที่หน้า {1}",
        'signature_deleted': "ลบลายเซ็น",
        'signature_copied': "คัดลอกลายเซ็น",
        'signature_pasted': "วางลายเซ็น {0}",
        'signature_saved': "แทรกลายเซ็น {0} รายการลงใน PDF\n\nโหลด PDF ใหม่...",
        'signature_saved_voice': "บันทึกลายเซ็น {0} รายการ",
        'mode_replace_signature_format': "สิ้นสุดโหมดและแทรกลายเซ็น {0}",
        'mode_conflict_voice_signature': "โหมด {0} เปิดอยู่ สิ้นสุดและแทรกลายเซ็น?",
        'signature_not_configured': "ไม่ได้กำหนดค่าลายเซ็น {0}",
        'signature_file_not_found': "ไม่พบไฟล์ลายเซ็น",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "ไม่มีลายเซ็นที่คัดลอก",
        'no_signatures_to_save': "ไม่มีลายเซ็นที่จะบันทึก",
        'signature_save_question': "บันทึกลายเซ็นทั้งหมด ปรับแต่ง หรือทิ้งอันนี้?",
        'signatures_saved_title': "บันทึกลายเซ็นแล้ว",
        'signatures_saved': "แทรกลายเซ็น {0} รายการลงใน PDF\n\nโหลด PDF ใหม่...",
        'signatures_saved_voice': "บันทึกลายเซ็น {0} รายการ",
        'all_signatures_discarded': "ทิ้งลายเซ็นทั้งหมด",
        'signature_settings_saved': "บันทึกการตั้งค่าลายเซ็น",
        'signature_cancelled': "ทิ้งลายเซ็น",
        'signature_active_title': "ลายเซ็นกำลังทำงาน",
        'signature_replace_question': "มีลายเซ็นที่กำลังทำงานอยู่แล้ว\n\nคุณต้องการแทนที่ลายเซ็นปัจจุบันหรือไม่?",
        'signature_replace': "แทนที่ลายเซ็น",
        'signature_replace_voice': "แทนที่ลายเซ็นปัจจุบันหรือยกเลิก?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "การตั้งค่ารูปภาพ",
        'image_common': "การตั้งค่ารูปภาพทั่วไป",
        'image_keep_aspect': "รักษาสัดส่วนเมื่อลาก",
        'image_default_size': "ขนาดเริ่มต้น (%):",
        'image_dark_invert': "กลับสีรูปภาพในโหมดมืด",
        'image_dark_invert_tooltip': "เปิด: รูปภาพจะถูกกลับสีเพื่อให้มองเห็นได้ดีขึ้น",
        'image_fine_tuning': "ปรับละเอียด (พิกเซล)",
        'image_offset_x': "ออฟเซ็ต X:",
        'image_offset_y': "ออฟเซ็ต Y:",
        'image_offset_x_tooltip': "ค่าลบเลื่อนรูปภาพไปทางซ้ายเมื่อบันทึก ค่าบวกไปทางขวา",
        'image_offset_y_tooltip': "ค่าลบเลื่อนรูปภาพขึ้นเมื่อบันทึก ค่าบวกลง",
        'image_select': "เลือกรูปภาพ",
        'image_insert': "แทรกรูปภาพ",
        'image_customize': " ปรับแต่งรูปภาพนี้",
        'image_aspect': " รักษาสัดส่วน",
        'image_discard': " ทิ้งรูปภาพนี้",
        'image_save_all': " บันทึกรูปภาพทั้งหมด",
        'image_discard_all': " ทิ้งรูปภาพทั้งหมด",
        'image_filter': "รูปภาพ",
        'image_guide_title': "แทรกรูปภาพ - คำแนะนำ",
        'image_guide': """
📷 แทรกรูปภาพใน PDF - คำแนะนำด่วน:

1. คลิกขวาที่ตำแหน่งที่ต้องการ
2. "แทรกรูปภาพ" → เลือกรูปภาพ
3. วางรูปภาพ: ลากด้วยเมาส์
4. ปรับขนาด: ลากที่มุม/ขอบ
5. รักษาสัดส่วน: กดปุ่ม [A]
6. ปรับแต่งเพิ่มเติม: คลิกขวาที่รูปภาพ

เคล็ดลับ: ในเมนูบริบทคุณสามารถปรับการตั้งค่าได้
        """,
        'image_inserted': "แทรกรูปภาพ {0} ที่หน้า {1}",
        'image_deleted': "ทิ้งรูปภาพ",
        'image_copied': "คัดลอกรูปภาพ",
        'image_pasted': "วางรูปภาพ",
        'image_saved': "แทรกรูปภาพ {0} รายการลงใน PDF\n\nโหลด PDF ใหม่...",
        'image_saved_voice': "บันทึกรูปภาพ {0} รายการ",
        'image_aspect_on': "เปิด",
        'image_aspect_off': "ปิด",
        'image_aspect_toggle': "รักษาสัดส่วน {0}",
        'image_reset': "รีเซ็ตรูปภาพเป็นขนาดเดิม",
        'image_replaced': "แทนที่รูปภาพ",
        'image_invalid': "รูปภาพไม่ถูกต้อง",
        'mode_replace_image': "แทรกรูปภาพ",
        'mode_conflict_voice_image': "โหมด {0} เปิดอยู่ สิ้นสุดและแทรกรูปภาพ?",
        'image_active_title': "รูปภาพกำลังทำงาน",
        'image_replace_question': "มีรูปภาพที่กำลังทำงานอยู่แล้ว\n\nคุณต้องการแทนที่รูปภาพปัจจุบันหรือไม่?",
        'image_replace': "แทนที่รูปภาพ",
        'image_replace_voice': "แทนที่รูปภาพปัจจุบันหรือยกเลิก?",
        'image_filter_all': "รูปภาพ (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;ไฟล์ทั้งหมด (*.*)",
        'no_copied_image': "ไม่มีรูปภาพที่คัดลอก",
        'image_discarded': "ทิ้งรูปภาพ",
        'image_save_question': "บันทึกรูปภาพทั้งหมด ปรับแต่ง หรือทิ้งอันนี้?",
        'no_images_to_save': "ไม่มีรูปภาพที่จะบันทึก",
        'no_valid_images': "ไม่มีรูปภาพที่ถูกต้องสำหรับบันทึก",
        'images_saved_title': "บันทึกรูปภาพแล้ว",
        'images_saved': "แทรกรูปภาพ {0} รายการลงใน PDF\n\nโหลด PDF ใหม่...",
        'images_saved_voice': "บันทึกรูปภาพ {0} รายการ",
        'all_images_discarded': "ทิ้งรูปภาพทั้งหมด",
        'image_settings_updated': "อัปเดตการตั้งค่ารูปภาพ",
        'image_replace_title': "เลือกรูปภาพใหม่",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "การตั้งค่ารูปร่าง",
        'form_basic': "การตั้งค่าพื้นฐาน",
        'form_default_type': "ประเภทเริ่มต้น:",
        'form_rectangle': "สี่เหลี่ยมผืนผ้า",
        'form_ellipse': "วงรี",
        'form_line': "เส้น",
        'form_arrow': "ลูกศร",
        'form_line_width': "ความหนาของเส้น:",
        'form_colors': "สี",
        'form_line_color': "สีเส้น:",
        'form_fill_color': "สีพื้น:",
        'form_choose_color': "เลือก",
        'form_transparent': "พื้นหลังโปร่งใส (เฉพาะเส้น)",
        'form_filled': "เติมสี",
        'form_dark_mode': "โหมดมืด",
        'form_dark_invert': "กลับสีในโหมดมืด",
        'form_fine_tuning': "ปรับละเอียด (พิกเซล)",
        'form_offset_x': "ออฟเซ็ต X:",
        'form_offset_y': "ออฟเซ็ต Y:",
        'form_offset_x_tooltip': "ค่าลบเลื่อนรูปร่างไปทางซ้ายเมื่อบันทึก ค่าบวกไปทางขวา",
        'form_offset_y_tooltip': "ค่าลบเลื่อนรูปร่างขึ้นเมื่อบันทึก ค่าบวกลง",
        'form_preview': "ตัวอย่าง",
        'form_insert': "แทรกรูปร่าง",
        'form_rectangle_insert': "สี่เหลี่ยมผืนผ้า",
        'form_ellipse_insert': "วงรี/วงกลม",
        'form_line_insert': "เส้น (2 คลิก)",
        'form_arrow_insert': "ลูกศร (2 คลิก)",
        'form_customize': " ปรับแต่งรูปร่างนี้",
        'form_transparent_toggle': " พื้นหลังโปร่งใส",
        'form_discard': " ทิ้งรูปร่างนี้",
        'form_save_all': " บันทึกรูปร่างทั้งหมด",
        'form_discard_all': " ทิ้งรูปร่างทั้งหมด",
        'form_guide_title': "แทรกรูปร่าง - คำแนะนำ",
        'form_guide': """
📐 แทรกรูปร่างใน PDF - คำแนะนำด่วน:

1. เลือกประเภท (สี่เหลี่ยมผืนผ้า วงรี เส้น ลูกศร)
2. คลิกที่ตำแหน่ง
   - สำหรับสี่เหลี่ยม/วงรี: คลิกครั้งเดียววางรูปร่าง
   - สำหรับเส้น/ลูกศร: คลิกสองครั้งสำหรับจุดเริ่มและจุดสิ้นสุด
3. วางรูปร่าง: ลากด้วยเมาส์
4. ปรับขนาด: ลากที่มุม/ขอบ
5. บันทึกรูปร่าง: Enter
6. ทิ้งรูปร่าง: ESC
7. ปรับแต่งเพิ่มเติม: คลิกขวาที่รูปร่าง

เคล็ดลับ: ในเมนูบริบทคุณสามารถปรับการตั้งค่าได้
        """,
        'form_inserted': "แทรก {0} ที่หน้า {1}",
        'form_deleted': "ลบรูปร่าง",
        'form_copied': "คัดลอกรูปร่าง",
        'form_pasted': "วางรูปร่าง",
        'form_saved': "แทรกรูปร่าง {0} รายการลงใน PDF\n\nโหลด PDF ใหม่...",
        'form_saved_voice': "บันทึกรูปร่าง {0} รายการ",
        'form_reset': "รีเซ็ตรูปร่างเป็นขนาดเริ่มต้น",
        'form_transparent_on': "เปิด",
        'form_transparent_off': "ปิด",
        'form_transparent_toggled': "พื้นหลังโปร่งใส {0}",
        'form_line_cancel': "ยกเลิกการวาดเส้น",
        'form_second_click': "ตอนนี้คลิกจุดสิ้นสุดสำหรับ {0}",
        'mode_replace_form': "แทรกรูปร่าง",
        'mode_conflict_voice_form': "โหมด {0} เปิดอยู่ สิ้นสุดและแทรกรูปร่าง?",
        'form_settings_updated': "อัปเดตการตั้งค่ารูปร่าง",
        'form_unknown': "รูปร่าง",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. คลิกที่ตำแหน่งเริ่มต้น",
        'form_line_guide_2': "2. คลิกที่ตำแหน่งสิ้นสุด",
        'form_line_guide_3': "เส้นจะถูกลากระหว่างจุดสองจุด",
        'form_line_status_1': "รอคลิกแรก...",
        'form_line_status_2': "ตั้งจุดแรกแล้ว: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "ตอนนี้คลิกจุดสิ้นสุด...",
        'form_line_status_4': "ตั้งจุดทั้งสองแล้ว\nคลิก 'เสร็จ' เพื่อบันทึก",
        'form_line_reset': "รีเซ็ต",
        'form_line_finish': "เสร็จ",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "คัดลอก (Cmd+C)",
        'paste': "วาง (Cmd+V)",
        'copied': "คัดลอก: {0}",
        'no_element_to_copy': "ไม่มีรายการที่เลือกสำหรับคัดลอก",
        'no_copied_data': "ไม่มีข้อมูลที่คัดลอก",
        'no_valid_position': "ไม่มีตำแหน่งที่ถูกต้องสำหรับวาง",
        'copy_text': "คัดลอกข้อความ",
        'copy_image': "คัดลอกรูปภาพ",
        'copy_form': "คัดลอกรูปร่าง",
        'copy_signature': "คัดลอกลายเซ็น",
        'element_text': "ข้อความ",
        'element_image': "รูปภาพ",
        'element_form': "รูปร่าง",
        'element_signature': "ลายเซ็น",
        'element_unknown': "รายการ",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "ข้อขัดแย้งโหมด",
        'mode_conflict_message': "โหมด '{0}' กำลังทำงานอยู่\n\nคุณต้องการสิ้นสุดและ {1} หรือไม่?",
        'mode_replace': "สิ้นสุดโหมดและ {0}",
        'mode_cancel': "ยกเลิก",
        'mode_replace_text': "แทรกข้อความ",
        'mode_replace_cross': "แทรกกากบาท",
        'mode_replace_signature': "แทรกลายเซ็น",
        'mode_replace_image': "แทรกรูปภาพ",
        'mode_replace_form': "แทรกรูปร่าง",
        'mode_conflict_voice': "โหมด {0} เปิดอยู่ สิ้นสุดและแทรกข้อความ?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "ป้อนข้อความ",
        'active_mode_signature': "ลายเซ็น",
        'active_mode_image': "รูปภาพ",
        'active_mode_form': "รูปร่าง",
        'active_mode_and': " และ ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "แทรก",
        'insert_another_text': "แทรกข้อความ",
        'insert_another_cross': "แทรกกากบาท",
        'insert_another_signature_1': "ลายเซ็น 1",
        'insert_another_signature_2': "ลายเซ็น 2",
        'insert_another_image': "แทรกรูปภาพ",
        'insert_another_form_rect': "สี่เหลี่ยมผืนผ้า",
        'insert_another_form_ellipse': "วงรี",
        'insert_another_form_line': "เส้น (2 คลิก)",
        'insert_another_form_arrow': "ลูกศร (2 คลิก)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "บันทึก {0}",
        'save_dialog_message': "จะบันทึก {0} ที่หน้า {1}\n\nคุณต้องการดำเนินการต่ออย่างไร?",
        'save_all': "บันทึก {0} ทั้งหมด",
        'save_single': "บันทึก {0}",
        'save_customize': "ปรับแต่ง {0}",
        'save_discard': "ทิ้ง {0} นี้",
        'save_continue': "แก้ไขต่อ",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " ไปที่หน้า {0}",
        'context_rotate': " หมุนหน้า {0}",
        'context_delete': " ลบหน้า {0}",
        'context_export': " ส่งออกหน้า {0}",
        'context_mark_as': " ทำเครื่องหมายหน้าเป็น...",
        'context_mark_empty': " หน้าว่าง",
        'context_unmark_empty': " ไม่ว่างอีกต่อไป",
        'context_mark_export': " ทำเครื่องหมายสำหรับส่งออก",
        'context_unmark_export': " ยกเลิกเครื่องหมายส่งออก",
        'context_batch_actions': " การดำเนินการกลุ่ม",
        'context_batch_delete_empty': " ลบหน้าว่างทั้งหมด {0} หน้า",
        'context_batch_export_single': " ส่งออก {0} หน้าทั้งหมด (ไฟล์เดียว)",
        'context_batch_export_split': " ส่งออก {0} หน้าทั้งหมด (แยกไฟล์)",
        'context_drag_start': " เริ่มลากแล้ววาง",
        'context_drag_stop': " หยุดลากแล้ววาง",
        'context_insert': " แทรก",
        'context_insert_pages': " แทรกหน้า",
        'context_zoom': "ซูม",
        'discard_mixed': "ทิ้ง {0} {1} และ {2} {3} ทั้งหมด",
        'save_mixed': "บันทึก {0} {1} และ {2} {3}",
        'discard_texts': "ทิ้งข้อความ {0} ทั้งหมด",
        'discard_text_single': "ทิ้ง 1 ข้อความ",
        'save_texts': "บันทึก {0} ข้อความ",
        'save_text_single': "บันทึก 1 ข้อความ",
        'discard_crosses': "ทิ้งกากบาท {0} ทั้งหมด",
        'discard_cross_single': "ทิ้ง 1 กากบาท",
        'save_crosses': "บันทึก {0} กากบาท",
        'save_cross_single': "บันทึก 1 กากบาท",
        'discard_signatures': "ทิ้งลายเซ็น {0} ทั้งหมด",
        'save_signature_single': "บันทึก 1 ลายเซ็น",
        'save_signatures': "บันทึก {0} ลายเซ็น",
        'discard_images': "ทิ้งรูปภาพ {0} ทั้งหมด",
        'save_image_single': "บันทึก 1 รูปภาพ",
        'save_images': "บันทึก {0} รูปภาพ",
        'discard_forms': "ทิ้งรูปร่าง {0} ทั้งหมด",
        'save_form_single': "บันทึก 1 รูปร่าง",
        'save_forms': "บันทึก {0} รูปร่าง",
        'cross_discard': "ทิ้งกากบาทนี้",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 ข้อมูลการส่งออก/นำเข้า",
        'export_what': "📋 ส่งออกอะไร?",
        'export_general': "การตั้งค่าทั่วไป",
        'export_general_items': "• เสียงพูด (เปิด/ปิด, ความเร็ว)\n• โหมดมืด/สว่าง\n• การตั้งค่าสำรอง\n• การตั้งค่า OCR",
        'export_image_form': "การตั้งค่ารูปภาพและรูปร่าง",
        'export_image_form_items': "• การตั้งค่ารูปภาพ (สัดส่วน, ขนาดเริ่มต้น)\n• การตั้งค่ารูปร่าง (ความหนาเส้น, สี)\n• การตั้งค่าลายเซ็น (พาธ, ขนาด, ประทับเวลา)",
        'export_passwords': "ฐานข้อมูลรหัสผ่าน",
        'export_passwords_items': "• รหัสผ่าน PDF ที่บันทึกทั้งหมด\n• เลือกเข้ารหัสหรือถอดรหัสได้",
        'export_master': "การตั้งค่ารหัสผ่านหลัก",
        'export_master_items': "• แฮชรหัสผ่านหลัก\n• การตั้งค่าสำหรับลายเซ็น/บล็อกข้อความ",
        'export_signatures': "ลายเซ็นและบล็อกข้อความ",
        'export_signatures_items': "• ไฟล์รูปภาพทั้งหมด (ลายเซ็น)\n• บล็อกข้อความทั้งหมดพร้อมการจัดรูปแบบ\n• เครื่องหมายส่วนตัว/สาธารณะ",
        'export_import_warning': "⚠️ หมายเหตุสำคัญ",
        'export_import_note': "• เมื่อนำเข้า การตั้งค่าปัจจุบันทั้งหมดจะถูกเขียนทับ\n• ต้องรีสตาร์ทแอปพลิเคชัน\n• ลายเซ็น/บล็อกข้อความที่มีอยู่จะถูกแทนที่",
        'export_master_note': "• หากตั้งค่ารหัสผ่านหลัก คุณสามารถเลือก:\n  - ถอดรหัส (รหัสผ่านเป็นข้อความธรรมดา)\n  - เข้ารหัส (อ่านได้ด้วยรหัสหลักเท่านั้น)",
        'export_security': "• ไฟล์ ZIP ที่ส่งออกมีข้อมูลที่เป็นความลับ\n• โปรดเก็บไว้อย่างปลอดภัย (เช่น แฟลชไดรฟ์ที่เข้ารหัส)\n• หากไฟล์หาย: รหัสผ่านไม่สามารถกู้คืนได้",
        'export_format': "📁 รูปแบบส่งออก",
        'export_format_desc': "การตั้งค่าจะถูกบันทึกในไฟล์ ZIP เดียว:",
        'export_filename': "PDFDarkView_การตั้งค่า_YYYYMMDD_HHMMSS.zip",
        'export_success': "ส่งออกการตั้งค่าสำเร็จ",
        'export_failed': "ส่งออกไม่สำเร็จ",
        'export_import_question': "คุณต้องการรีสตาร์ทแอปพลิเคชันตอนนี้หรือไม่?",
        'export_password_question': "ตั้งค่ารหัสผ่านหลักแล้ว\n\nคุณต้องการส่งออกรหัสผ่านแบบถอดรหัสหรือไม่?\n(มิฉะนั้นจะส่งออกแบบเข้ารหัส)",
        'export_decrypt': "ส่งออกแบบถอดรหัส",
        'export_encrypt': "ส่งออกแบบเข้ารหัส",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " ข้อมูล",
        'info_title': "เกี่ยวกับ PDF Dark View",
        'info_version': "เวอร์ชัน",
        'info_author': "พัฒนาโดย Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "เกี่ยวกับ",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> เป็นโปรแกรมดู PDF ที่เข้าถึงได้ พัฒนาขึ้นโดยเฉพาะสำหรับผู้ที่มีความบกพร่องทางการมองเห็น</p>

            <p><strong>คุณสมบัติหลัก:</strong></p>
            <ul>
                <li>อินเทอร์เฟซที่ตัดกันสูง ปรับแต่งได้</li>
                <li>ควบคุมด้วยแป้นพิมพ์อย่างสมบูรณ์</li>
                <li>การอ่านออกเสียงในตัว</li>
                <li>OCR สำหรับเอกสารที่สแกน</li>
                <li>เครื่องมือแก้ไขที่ครอบคลุม</li>
            </ul>

            <p>รองรับมากกว่า 50 ภาษา – เพื่อให้ PDF เข้าถึงได้สำหรับทุกคน</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "คุณสมบัติ",
        'info_features_intro': "PDF Dark View นำเสนอความเป็นไปได้ต่อไปนี้แก่คุณ:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>การแสดงผลและการนำทาง</strong> – โหมดมืด/สว่าง, การพลิกหน้า, ซูม, ไปยังหน้า</li>
            <li><strong>OCR (การรู้จำข้อความ)</strong> – ทำให้เอกสารที่สแกนสามารถค้นหาและคัดลอกได้</li>
            <li><strong>การแก้ไข</strong> – แทรกข้อความ, กากบาท, ลายเซ็น, รูปภาพ และรูปร่าง</li>
            <li><strong>การจัดการหน้า</strong> – ลบ, แยก, แทรก, ย้ายด้วยการลากและวาง</li>
            <li><strong>การส่งออก</strong> – ไปยัง Word, Pages หรือเป็นข้อความ</li>
            <li><strong>ความปลอดภัย</strong> – การป้องกันและการจัดการรหัสผ่าน</li>
            <li><strong>การเข้าถึง</strong> – การอ่านออกเสียง, การควบคุมด้วยแป้นพิมพ์, ความคมชัดสูง</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "การใช้งาน",
        'info_accessibility': "♿ การเข้าถึง – การควบคุมด้วยแป้นพิมพ์อย่างสมบูรณ์",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 ทั่วไป</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> เปิด PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> ค้นหา</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> สลับโหมดมืด/สว่าง</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> พิมพ์</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> ออกจากโปรแกรม</div>

        <div class="shortcut-cat">📖 การนำทาง</div>
        <div class="shortcut-row"><kbd>ปุ่มลูกศร</kbd> พลิกทีละหน้า</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> ไปยังหน้า</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> หน้าแรก</div>
        <div class="shortcut-row"><kbd>Ende</kbd> หน้าสุดท้าย</div>

        <div class="shortcut-cat">✏️ การแก้ไข</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> แทรกข้อความ</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> ลบหน้า</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> แยกหน้า</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> แทรกหน้า</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> ย้ายหน้า</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> หมุนหน้า</div>

        <div class="shortcut-cat">🖼️ การย้ายองค์ประกอบ</div>
        <div class="shortcut-row"><kbd>ปุ่มลูกศร</kbd> ย้ายข้อความ/รูปภาพ/ลายเซ็น</div>
        <div class="shortcut-row"><kbd>Ctrl+ปุ่มลูกศร</kbd> ก้าวที่ใหญ่ขึ้น</div>
        <div class="shortcut-row"><kbd>Enter</kbd> บันทึก</div>
        <div class="shortcut-row"><kbd>ESC</kbd> ยกเลิก</div>

        <div class="shortcut-cat">🗣️ การอ่านออกเสียง</div>
        <div class="shortcut-row"><kbd>F2</kbd> เปิด/ปิด การอ่านออกเสียง</div>
        """,
        'info_contextmenu': "📌 สำคัญ: ทุกฟังก์ชันสามารถเข้าถึงได้ผ่านเมนูบริบท (ปุ่มเมาส์ขวา)!",
        'info_accessibility_hint': "💡 เคล็ดลับ: การอ่านออกเสียง (F2) ช่วยให้การวางทิศทางง่ายขึ้นและให้ข้อเสนอแนะเกี่ยวกับเมนูและกล่องโต้ตอบ",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "ใบอนุญาต & ข้อมูลผู้เผยแพร่",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 ข้อมูลผู้เผยแพร่</strong><br>
        ข้อมูลตาม § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, เยอรมนี<br>
        อีเมล: binhdiez64@gmail.com<br>
        ผู้รับผิดชอบเนื้อหา: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ การปฏิเสธความรับผิดชอบ</strong><br>
        ซอฟต์แวร์นี้ได้รับการพัฒนาด้วยความระมัดระวังสูงสุด ไม่มีการรับประกันความถูกต้อง ความสมบูรณ์ และการทำงาน การใช้งานเป็นความเสี่ยงของคุณเอง<br><br>

        <strong>📄 ใบอนุญาต MIT (การใช้งานส่วนตัว)</strong><br>
        ลิขสิทธิ์ (c) 2026 Toralf Schulz (BinhDiez)<br>
        อนุญาต: การใช้งานฟรี, การปรับเปลี่ยนส่วนตัว, สำเนาส่วนบุคคล<br>
        ไม่อนุญาต: การขาย, การใช้เพื่อการค้า, การลบข้อความแจ้งลิขสิทธิ์<br><br>

        <strong>🔧 ส่วนประกอบของบุคคลที่สาม</strong><br>
        ซอฟต์แวร์นี้มีส่วนประกอบภายใต้ใบอนุญาต GPL, AGPL, Apache 2.0, BSD และ MIT<br>
        เมื่อแจกจ่ายต่อ ต้องปฏิบัติตามเงื่อนไขใบอนุญาตที่เกี่ยวข้อง<br><br>

        <strong>🌐 โอเพนซอร์ส</strong><br>
        ซอร์สโค้ดพร้อมให้บริการและสามารถดู แก้ไข และแจกจ่ายต่อได้ตามเงื่อนไขใบอนุญาตที่เกี่ยวข้อง<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "คำขอบคุณ",
        'info_credits': "ขอบคุณชุมชนโอเพนซอร์ส",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – การประมวลผล PDF</li>
            <li><strong>PyQt5</strong> – อินเทอร์เฟซกราฟิก</li>
            <li><strong>Tesseract OCR</strong> – การรู้จำข้อความ</li>
            <li><strong>OCRmyPDF</strong> – การรวม OCR</li>
            <li><strong>python-docx</strong> – การส่งออก Word</li>
            <li><strong>qtawesome</strong> – ไอคอน</li>
            <li><strong>DeepSeek</strong> – การสนับสนุนการแปล (50+ ภาษา)</li>
            <li><strong>ผู้ใช้ทุกท่าน</strong> – สำหรับข้อเสนอแนะอันมีค่า</li>
            <li><strong>ชุมชนโอเพนซอร์ส</strong> – สำหรับไลบรารีที่ยอดเยี่ยม</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "ภาษา",
        'info_languages_header': "🌍 การรองรับภาษา",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View รองรับ <strong>62 ภาษา</strong> ในปัจจุบัน – เพื่อให้ซอฟต์แวร์สามารถใช้งานได้อย่างทั่วถึงทั่วโลก</p>

            <p><strong>📖 รายชื่อภาษาทั้งหมด (ณ มีนาคม 2569):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 แอฟริกาans</li>
                    <li>🇦🇱 แอลเบเนีย (Shqip)</li>
                    <li>🇩🇿 อาหรับ (العربية)</li>
                    <li>🇮🇩 บาหลี (Basa Bali)</li>
                    <li>🇧🇩 เบงกาลี (বাংলা)</li>
                    <li>🇲🇲 พม่า (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 บอสเนีย (Bosanski)</li>
                    <li>🇧🇬 บัลแกเรีย (Български)</li>
                    <li>🇨🇳 จีน (中文)</li>
                    <li>🇩🇰 เดนมาร์ก (Dansk)</li>
                    <li>🇩🇪 เยอรมัน (Deutsch)</li>
                    <li>🇬🇧 อังกฤษ (English)</li>
                    <li>🇪🇪 เอสโตเนีย (Eesti)</li>
                    <li>🇫🇮 ฟินแลนด์ (Suomi)</li>
                    <li>🇫🇷 ฝรั่งเศส (Français)</li>
                    <li>🇬🇷 กรีก (Ελληνικά)</li>
                    <li>🇮🇱 ฮีบรู (עברית)</li>
                    <li>🇮🇳 ฮินดี (हिन्दी)</li>
                    <li>🇭🇷 โครเอเชีย (Hrvatski)</li>
                    <li>🇭🇺 ฮังการี (Magyar)</li>
                    <li>🇮🇩 อินโดนีเซีย (Bahasa Indonesia)</li>
                    <li>🇮🇪 ไอริช (Gaeilge)</li>
                    <li>🇮🇸 ไอซ์แลนด์ (Íslenska)</li>
                    <li>🇮🇹 อิตาลี (Italiano)</li>
                    <li>🇯🇵 ญี่ปุ่น (日本語)</li>
                    <li>🇰🇭 เขมร (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 เกาหลี (한국어)</li>
                    <li>🇱🇦 ลาว (ພາສາລາວ)</li>
                    <li>🇱🇻 ลัตเวีย (Latviešu)</li>
                    <li>🇱🇹 ลิทัวเนีย (Lietuvių)</li>
                    <li>🇱🇺 ลักเซมเบิร์ก (Lëtzebuergesch)</li>
                    <li>🇲🇾 มาเลย์ (Bahasa Melayu)</li>
                    <li>🇮🇳 มราฐี (मराठी)</li>
                    <li>🇲🇳 มองโกเลีย (Монгол)</li>
                    <li>🇳🇵 เนปาล (नेपाली)</li>
                    <li>🇳🇱 ดัตช์ (Nederlands)</li>
                    <li>🇳🇴 นอร์เวย์ (Norsk)</li>
                    <li>🇦🇫 พัชตู (پښتو)</li>
                    <li>🇮🇷 เปอร์เซีย (فارسی)</li>
                    <li>🇵🇱 โปแลนด์ (Polski)</li>
                    <li>🇵🇹 โปรตุเกส (Português)</li>
                    <li>🇮🇳 ปัญจาบ (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 โรมาเนีย (Română)</li>
                    <li>🇷🇺 รัสเซีย (Русский)</li>
                    <li>🇸🇪 สวีเดน (Svenska)</li>
                    <li>🇷🇸 เซอร์เบีย (Српски)</li>
                    <li>🇸🇰 สโลวัก (Slovenčina)</li>
                    <li>🇸🇮 สโลวีเนีย (Slovenščina)</li>
                    <li>🇪🇸 สเปน (Español)</li>
                    <li>🇹🇿 สวาฮีลี (Kiswahili)</li>
                    <li>🇵🇭 ตากาล็อก (Filipino)</li>
                    <li>🇮🇳 ทมิฬ (தமிழ்)</li>
                    <li>🇮🇳 เตลูกู (తెలుగు)</li>
                    <li>🇹🇭 ไทย (ไทย)</li>
                    <li>🇨🇿 เช็ก (Čeština)</li>
                    <li>🇹🇷 ตุรกี (Türkçe)</li>
                    <li>🇺🇦 ยูเครน (Українська)</li>
                    <li>🇵🇰 อูรดู (اردو)</li>
                    <li>🇻🇳 เวียดนาม (Tiếng Việt)</li>
                    <li>🇸🇳 โวลอฟ (Wolof)</li>
                    <li>🇺🇸 ยิดดิช (ייִדיש)</li>
                    <li>🇿🇦 ซูลู (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 เพิ่มภาษาของคุณเอง:</strong><br>
                ต้องการภาษาที่ยังไม่รวมอยู่ในรายการหรือไม่? เพียงวางไฟล์พจนานุกรมของคุณเอง (<code>sprache_xx.py</code>) ไว้ข้างแอปพลิเคชัน – ซอฟต์แวร์จะจดจำโดยอัตโนมัติ หากคุณสนใจการแปลภาษาเฉพาะ โปรดติดต่อฉัน
            </div>

            <p><strong>🙏 ขอขอบคุณเป็นพิเศษ:</strong> DeepSeek สำหรับการสนับสนุนในการแปลพจนานุกรมทั้งหมดเป็น 62 ภาษา</p>

            <p>📧 ติดต่อสำหรับการแปล: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "ข้อผิดพลาด",
        'error_occurred': "เกิดข้อผิดพลาด",
        'error_pdf_load': "ข้อผิดพลาดในการโหลด PDF",
        'error_pdf_save': "ข้อผิดพลาดในการบันทึก PDF",
        'error_ocr': "ข้อผิดพลาดในการรู้จำข้อความ",
        'error_no_pdf': "ไม่มี PDF โหลด",
        'error_page_not_found': "ไม่พบหน้า",
        'error_invalid_range': "ช่วงหน้าไม่ถูกต้อง",
        'error_file_not_found': "ไม่พบไฟล์",
        'error_permission': "ไม่มีสิทธิ์",
        'error_unknown': "ข้อผิดพลาดไม่ทราบสาเหตุ",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "สำเร็จ",
        'success_operation': "ดำเนินการสำเร็จ",
        'success_saved': "บันทึกสำเร็จ",
        'success_exported': "ส่งออกสำเร็จ",
        'success_imported': "นำเข้าสำเร็จ",
        'success_deleted': "ลบสำเร็จ",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "ยืนยัน",
        'confirm_yes': "ใช่",
        'confirm_no': "ไม่",
        'confirm_ok': "ตกลง",
        'confirm_cancel': "ยกเลิก",
        'confirm_delete': "ลบ",
        'confirm_overwrite': "เขียนทับ",
        'confirm_continue': "ดำเนินการต่อ",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "กำลังโหลด PDF...",
        'progress_saving': "กำลังบันทึก PDF...",
        'progress_exporting': "กำลังส่งออก PDF...",
        'progress_processing': "กำลังประมวลผล...",
        'progress_wait': "โปรดรอ...",
        'progress_preparing': "กำลังเตรียม...",
        'progress_finalizing': "กำลังสรุป...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "ขาว",
        'color_black': "ดำ",
        'color_red': "แดง",
        'color_green': "เขียว",
        'color_blue': "น้ำเงิน",
        'color_yellow': "เหลือง",
        'color_magenta': "ม่วงแดง",
        'color_cyan': "ฟ้า",
        'color_orange': "ส้ม",
        'color_gray': "เทา",
        'color_custom': "เลือกสี",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&ไฟล์",
        'menu_edit': "&แก้ไข",
        'menu_view': "&มุมมอง",
        'menu_tools': "&เครื่องมือ",
        'menu_settings': "&การตั้งค่า",
        'menu_help': "&ช่วยเหลือ",
        'menu_language': "🌐 ภาษา",
        'menu_guides': "&คำแนะนำ",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&เปิด",
        'file_save_as': "&บันทึกเป็น...",
        'file_protect': "&ป้องกันเอกสาร...",
        'file_export': "&ส่งออก",
        'file_export_pages': "ส่งออกเป็น Pages",
        'file_export_word': "ส่งออกเป็น DOCX",
        'file_export_text': "ส่งออกเป็น TXT",
        'file_print_now': "&พิมพ์ทันที",
        'file_print': "&พิมพ์",
        'file_close': "&ปิด",
        'file_quit': "&ออก",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&ค้นหา",
        'edit_ocr': " ทำ OCR",
        'edit_rotate': "&หมุนหน้า",
        'edit_rotate_all': "&หมุนทุกหน้า",
        'edit_delete_pages': "&ลบหน้า",
        'edit_extract_pages': "&แยกหน้า",
        'edit_insert_pages': "&แทรกหน้า",
        'edit_move_pages': "&ย้ายหน้า",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " แทรกข้อความและกากบาท",
        'text_insert': " แทรกข้อความ",
        'cross_insert': " แทรกกากบาท",
        'text_customize': " ปรับแต่งข้อความนี้",
        'cross_customize': " ปรับแต่งกากบาทนี้",
        'cross_customize_all': " ปรับแต่งกากบาททั้งหมด",
        'text_discard': " ทิ้งข้อความ/กากบาทนี้",
        'text_discard_all': " ทิ้งข้อความและกากบาททั้งหมด",
        'text_save_all': " บันทึกข้อความและกากบาททั้งหมด",
        'text_guide': " การป้อนข้อความ / บล็อกข้อความ - คำแนะนำ",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " แทรกลายเซ็น",
        'signature_settings_menu': " การตั้งค่า...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " แทรกรูปภาพ",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " แทรกรูปร่าง",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&แสดงหน้าต่างข้อความ",
        'view_zoom': "&ซูม",
        'view_zoom_page': "&ความกว้างหน้า (ค่าเริ่มต้น)",
        'view_zoom_two': "&สองหน้า",
        'view_zoom_overview': "&ภาพรวม (หลายหน้า)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&เครื่องมือช่วยเหลือ",
        'settings_voice': "เสียงพูด",
        'settings_voice_tooltip': "เพิ่มเสียงพูดของโปรแกรมอ่านหน้าจอด้วยข้อมูลเพิ่มเติม",
        'settings_signature': "&การตั้งค่าลายเซ็น",
        'settings_password': "&การจัดการรหัสผ่าน",
        'settings_backup': "สร้างสำรองก่อนการเปลี่ยนแปลง",
        'settings_export_import': "&ส่งออก / นำเข้าการตั้งค่า",
        'settings_export': "&ส่งออกการตั้งค่าทั้งหมด...",
        'settings_import': "&นำเข้าการตั้งค่าทั้งหมด...",
        'settings_export_info': "&ส่งออกอะไร?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "เปิด",
        'voice_off': "ปิด",
        'voice_toggle': "เสียงพูด {0}",
        'voice_speed': "ความเร็ว {0} เปอร์เซ็นต์",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "ไม่พบเครื่องมือ:\n{0}\n\nBASE_DIR: {1}\nโปรดตรวจสอบให้แน่ใจว่าติดตั้งเครื่องมือ PDF ในไดเรกทอรี {1}",
        'tool_started': "เริ่ม {0} แล้ว",
        'tool_start_failed': "ไม่สามารถเริ่มได้",
        'process_error_failed_to_start': "ไม่สามารถเริ่มกระบวนการได้ ไฟล์มีอยู่หรือไม่?",
        'process_error_crashed': "กระบวนการหยุดทำงานระหว่างเริ่มต้น",
        'process_error_timeout': "กระบวนการหมดเวลา",
        'process_error_write': "ข้อผิดพลาดในการเขียนไปยังกระบวนการ",
        'process_error_read': "ข้อผิดพลาดในการอ่านจากกระบวนการ",
        'process_error_unknown': "ข้อผิดพลาดกระบวนการไม่ทราบสาเหตุ",
        'process_command': "คำสั่ง",
        'process_normal_exit': "สิ้นสุดตามปกติ",
        'process_crashed': "หยุดทำงาน",
        'process_nonzero_exit': "{0} สิ้นสุดด้วยรหัสข้อผิดพลาด {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "กำลังยกเลิก...",
        'move_cancelling': "กำลังยกเลิกการย้าย",
        'opening_pdf': "กำลังเปิด PDF...",
        'loading_document': "กำลังโหลดเอกสาร...",
        'pdf_opened': "เปิด PDF แล้ว",
        'pages_found_moving': "พบ {0} หน้า, {1} สำหรับการย้าย",
        'creating_backup': "กำลังสร้างสำรอง...",
        'backup_description': "กำลังสำรองไฟล์ต้นฉบับ...",
        'backup_saved_as': "สำรองเป็น: {0}",
        'error_format': "ข้อผิดพลาด: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView โดย BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "รีเซ็ตการค้นหา",
        'page_header_simple': "=== หน้า {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "การจัดการรหัสผ่าน – คำแนะนำ",
        'password_guide_voice': "คำแนะนำสำหรับการจัดการรหัสผ่าน โปรดอ่านหมายเหตุ",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 การจัดการรหัสผ่าน – คำแนะนำโดยละเอียด</strong></p>

        <p><strong>1. การป้องกันด้วยรหัสผ่านสำหรับ PDF</strong></p>
        <ul>
        <li>เมื่อเปิด PDF ที่มีการป้องกันด้วยรหัสผ่าน จะมีไดอะล็อกให้ป้อนรหัสผ่าน</li>
        <li>คุณสามารถบันทึกรหัสผ่านแบบเข้ารหัสเพื่อไม่ต้องป้อนทุกครั้ง (ช่อง "บันทึกรหัสผ่าน")</li>
        <li>ด้วยปุ่ม "ลบรหัสผ่าน" คุณสามารถสร้างสำเนา PDF ที่ถอดรหัสแล้วและลบรหัสผ่านออกจากฐานข้อมูล</li>
        </ul>

        <p><strong>2. รหัสผ่านหลัก</strong></p>
        <ul>
        <li>รหัสผ่านหลักป้องกันการเข้าถึงรหัสผ่าน PDF ที่บันทึกไว้ทั้งหมด</li>
        <li><strong>การตั้งค่า:</strong> ไปที่ "การตั้งค่า → การจัดการรหัสผ่าน → การตั้งค่ารหัสผ่านหลัก" และคลิก "ตั้งค่ารหัสผ่านหลัก" เลือกรหัสผ่านที่แข็งแรง (อย่างน้อย 8 ตัวอักษร)</li>
        <li><strong>การเปลี่ยน:</strong> หลังจากยืนยันตัวตนสำเร็จ คุณสามารถเปลี่ยนรหัสผ่านหลักได้</li>
        <li><strong>การลบ:</strong> หากคุณลบรหัสผ่านหลัก รหัสผ่านที่บันทึกไว้ทั้งหมดจะถูกลบอย่างถาวร คุณสามารถส่งออกสำรองก่อนได้</li>
        <li>หนึ่งครั้งต่อเซสชัน คุณต้องยืนยันตัวตนด้วยรหัสผ่านหลักเพื่อเข้าถึงฟังก์ชันที่ป้องกัน (เช่น การแสดงรหัสผ่าน)</li>
        </ul>

        <p><strong>3. การจัดการรหัสผ่าน (รายการ)</strong></p>
        <ul>
        <li>ภายใต้ "การตั้งค่า → การจัดการรหัสผ่าน" คุณจะเปิดตารางของ PDF ที่บันทึกทั้งหมดพร้อมรหัสผ่านที่เข้ารหัส</li>
        <li><strong>ไม่มีรหัสผ่านหลัก:</strong> คุณสามารถลบรายการได้เท่านั้น – รหัสผ่านยังคงซ่อนอยู่</li>
        <li><strong>มีรหัสผ่านหลัก (ยืนยันตัวตนแล้ว):</strong> คุณสามารถดู คัดลอก ส่งออก และลบรหัสผ่านได้</li>
        <li><strong>ส่งออก:</strong> เลือกรูปแบบ (JSON, CSV, TXT) และบันทึกรายการ หากตั้งค่ารหัสผ่านหลัก คุณสามารถตัดสินใจได้ว่ารหัสผ่านจะถูกส่งออกเป็นข้อความธรรมดาหรือเข้ารหัสต่อไป</li>
        <li><strong>นำเข้า:</strong> ไฟล์ ZIP ที่ส่งออกก่อนหน้านี้พร้อมการตั้งค่าทั้งหมด (รวมรหัสผ่าน) สามารถอ่านกลับได้ผ่าน "การตั้งค่า → ส่งออก/นำเข้าการตั้งค่า" ข้อควรระวัง: ข้อมูลที่มีอยู่จะถูกเขียนทับ!</li>
        </ul>

        <p><strong>4. เครื่องสร้างรหัสผ่าน</strong></p>
        <ul>
        <li>ในไดอะล็อกรหัสผ่าน (เช่น เมื่อป้องกัน PDF) คุณจะพบปุ่มลูกเต๋า 🎲 ทางด้านขวาของช่องป้อนข้อมูล</li>
        <li>คลิกเพื่อเปิดเครื่องสร้างรหัสผ่าน คุณสามารถตั้งค่าความยาว ชุดอักขระ (ตัวพิมพ์ใหญ่ ตัวพิมพ์เล็ก ตัวเลข สัญลักษณ์พิเศษ) และตัวคั่นเพื่อให้อ่านง่ายขึ้น</li>
        <li>รหัสผ่านที่สร้างขึ้นสามารถนำมาใช้ได้ทันทีและคัดลอกได้หากจำเป็น</li>
        </ul>

        <p><strong>5. หมายเหตุด้านความปลอดภัยที่สำคัญ</strong></p>
        <ul>
        <li>รหัสผ่านที่บันทึกไว้จะถูกจัดเก็บด้วยการเข้ารหัส AES-256 คีย์ได้มาจากรหัสผ่านหลักของคุณ (หากตั้งค่า) หรือจากค่าคงที่ (ไม่มีรหัสผ่านหลัก)</li>
        <li>หากไม่มีรหัสผ่านหลัก รหัสผ่านจะถูกเข้ารหัสแต่คีย์ถูกเก็บไว้ในโปรแกรม – ผู้โจมตีที่เข้าถึงไฟล์ของคุณสามารถถอดรหัสได้ ดังนั้นเราขอแนะนำอย่างยิ่งให้ใช้รหัสผ่านหลัก</li>
        <li>ฐานข้อมูลรหัสผ่านอยู่ในไดเรกทอรี `Daten/passwords.json` ทำการสำรองข้อมูลเป็นประจำ โดยเฉพาะก่อนลบรหัสผ่านหลัก</li>
        <li>หากลืมรหัสผ่านหลัก รหัสผ่านที่บันทึกไว้ทั้งหมดจะสูญหายอย่างถาวร</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "โหมดการกลับสี",
        'invert_mode_classic': "คลาสสิก (กลับสีทั้งหมด)",
        'invert_mode_smart': "อัจฉริยะ (กลับเฉพาะความสว่าง)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "ค่าเกณฑ์ระดับสีเทา",
        'gray_threshold_10': "10% (เข้มงวด)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (ค่าเริ่มต้น)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (นุ่มนวล)",
        'threshold_changed': "ตั้งค่าเกณฑ์เป็น {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "ค่าเกณฑ์ระดับสีเทา – คำอธิบาย",
        'threshold_guide_text': "ค่าเกณฑ์ระดับสีเทากำหนดว่าพิกเซลใดในโหมดมืดอัจฉริยะถือเป็น 'สีเทา' และถูกกลับสี\n\n"
                                "• ค่าต่ำ (10%) กลับเฉพาะเฉดสีเทาที่เกือบสมบูรณ์ – องค์ประกอบสีจะคงอยู่ครบถ้วน\n"
                                "• ค่าสูง (50%) กลับพิกเซลที่มีสีเล็กน้อยด้วย – ซึ่งเพิ่มความคมชัด แต่สามารถบิดเบือนสีได้\n\n"
                                "ค่าที่เหมาะสมขึ้นอยู่กับเอกสาร สำหรับเอกสารข้อความล้วน 30–40% มักจะเหมาะสม สำหรับกราฟิกสีควรใช้ 10–20%\n\n"
                                "คุณสามารถปรับค่าได้ตลอดเวลาผ่านเมนู 'การตั้งค่า' – PDF จะโหลดซ้ำทันที\n\n"
                                "หมายเหตุ:\n* รูปถ่ายและรูปภาพสามารถแสดงได้อย่างถูกต้องเฉพาะในโหมดสว่างเท่านั้น!\n* การตั้งค่าการกลับสีจะแสดงเฉพาะเมื่อเปิดใช้งานโหมดมืดเท่านั้น",
        'threshold_guide_voice': "ค่าเกณฑ์ระดับสีเทากำหนดว่าโหมดมืดอัจฉริยะเข้าแทรกแซงมากเพียงใด ค่าต่ำช่วยรักษาสี ค่าสูงเพิ่มความคมชัด",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "กำลังเปิด PDF...",
        'progress_loading_document': "กำลังโหลดเอกสาร...",
        'progress_pdf_opened': "เปิด PDF แล้ว",
        'progress_creating_backup': "กำลังสร้างข้อมูลสำรอง...",
        'progress_backup_description': "กำลังสำรองไฟล์ต้นฉบับ...",
        'progress_backup_created': "สร้างข้อมูลสำรองแล้ว",
        'progress_backup_saved_as': "บันทึกเป็น: {0}",
        'progress_analyzing_start': "เริ่มการวิเคราะห์...",
        'progress_searching_empty': "กำลังค้นหาหน้าว่าง...",
        'progress_page_empty': "หน้า {0} ว่างเปล่า",
        'progress_page_keep': "เก็บหน้า {0} ไว้",
        'progress_analysis_complete': "การวิเคราะห์เสร็จสิ้น",
        'progress_empty_found': "พบ {0} หน้าว่าง",
        'progress_current_page': "หน้าปัจจุบัน",
        'progress_mark_delete': "กำลังทำเครื่องหมายเพื่อลบ",
        'progress_range_selected': "ช่วงหน้า {0}-{1}",
        'progress_deleting_pages': "กำลังลบ {0} หน้า",
        'progress_creating_new_pdf': "กำลังสร้าง PDF ใหม่...",
        'progress_transferring_pages': "กำลังถ่ายโอนหน้า",
        'progress_keeping_page': "หน้า {0} จะถูกเก็บไว้ ({1}/{2})",
        'progress_saving_pdf': "กำลังบันทึก PDF...",
        'progress_optimizing': "กำลังเพิ่มประสิทธิภาพขนาดไฟล์...",
        'progress_finalizing': "กำลังสรุป...",
        'progress_new_size': "ขนาดใหม่: {0:.2f} MB",
        'progress_cancelling': "กำลังยกเลิก...",
        'progress_cancel_message': "กำลังยกเลิก {0}",
        'progress_pages_found_moving': "พบ {0} หน้า, {1} หน้าที่จะย้าย",

        # OCR-Fortschritt
        'ocr_status_analyzing': "กำลังวิเคราะห์ PDF...",
        'ocr_status_optimizing': "กำลังเพิ่มประสิทธิภาพภาพ...",
        'ocr_status_recognizing': "กำลังรู้จำข้อความ...",
        'ocr_status_embedding': "กำลังฝังข้อความ...",
        'ocr_status_finalizing': "กำลังสรุป PDF...",

        # PDF-Laden
        'progress_preparing': "กำลังเตรียม...",
        'progress_loading': "กำลังโหลด PDF...",

        # Seitenoperationen
        'progress_deleting_title': "กำลังลบหน้า...",
        'progress_moving_title': "กำลังย้ายหน้า...",
        'pages_found': "พบหน้า",
        'progress_creating_new_order': "กำลังสร้างลำดับใหม่...",
        'progress_sorting_pages': "กำลังจัดเรียงหน้า...",
        'progress_moving_to_begin': "ย้าย {0} หน้าไปที่จุดเริ่มต้น",
        'progress_transferring_count': "ถ่ายโอน {0} หน้า",
        'progress_transferring_before_target': "ถ่ายโอนหน้าก่อนเป้าหมาย",
        'progress_moving_pages': "ย้าย {0} หน้า",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_สำรอง_",
        'filename_protected_suffix': "_ป้องกัน_",
        'filename_copy_suffix': "_สำเนา",
        'filename_page_single': "_หน้า_",
        'filename_page_range': "_หน้า_",
        'filename_export_page': "_หน้า_{0:03}",
        'filename_export_range': "_หน้า_{0}-{1}",
        'filename_export_multiple': "_หน้า_{0}",
        'filename_with_text': "_พร้อม_ข้อความ",
        'filename_with_signature': "_พร้อม_ลายเซ็น",
        'filename_with_image': "_พร้อม_รูปภาพ",
        'filename_with_forms': "_พร้อม_รูปร่าง",
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
        'view_toggle_navbar': "แสดงแถบปุ่ม",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "ไม่สามารถลบหน้าทั้งหมดได้",
		'pages_cannot_delete_last_page': 'ไม่สามารถลบหน้าสุดท้ายได้!',
		'pages_cannot_delete_all_pages': 'ต้องเหลืออย่างน้อยหนึ่งหน้าในเอกสาร!',
		'delete_pages_confirm': 'คุณแน่ใจหรือไม่ว่าต้องการลบ {0} หน้า?',
		'delete_pages_confirm_voice': 'คุณแน่ใจหรือไม่ว่าต้องการลบ {0} หน้า?',
		'pages_deleted': 'ลบ {0} หน้าเรียบร้อยแล้ว',
		'warning': 'คำเตือน',
		'error': 'ข้อผิดพลาด',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "ไม่ได้เลือกแบบฟอร์ม",
        'form_customized': "ปรับแต่งแบบฟอร์มเรียบร้อยแล้ว",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "เลือก",
        'btn_use': "ใช้",
        'master_password_for_spasswords': "ในการจัดเก็บและใช้รหัสผ่าน คุณต้องตั้งรหัสผ่านหลักก่อน\n\nคุณต้องการตั้งรหัสผ่านหลักตอนนี้หรือไม่?",
        'open_saved_dialog_title': "เปิดไฟล์ที่บันทึกไว้",
        'open_saved_question': "คุณต้องการเปิดไฟล์ที่บันทึกไว้ตอนนี้หรือไม่?",
        'password': "รหัสผ่าน",
        'password_manager_master_required': "ตัวจัดการรหัสผ่านจะพร้อมใช้งานก็ต่อเมื่อมีการตั้งรหัสผ่านหลักแล้ว\n\nคุณต้องการตั้งรหัสผ่านหลักตอนนี้หรือไม่?",
        'password_master_required_for_select': "ในการดูและเลือกรหัสผ่านที่บันทึกไว้ คุณต้องยืนยันตัวตนด้วยรหัสผ่านหลักของคุณก่อน\n\nคุณต้องการยืนยันตัวตนตอนนี้หรือไม่?",
        'password_not_available': "รหัสผ่านที่เลือกไม่พร้อมใช้งานหรือไม่สามารถถอดรหัสได้",
        'password_options_title': "ตัวเลือกรหัสผ่าน",
        'password_save_choice_change': "ตั้งรหัสผ่านใหม่",
        'password_save_choice_keep': "ใช้รหัสผ่านที่มีอยู่",
        'password_save_choice_none': "บันทึกโดยไม่เข้ารหัส",
        'password_save_hint': "ตั้งรหัสผ่านหลักก่อนเพื่อจัดเก็บรหัสผ่านอย่างปลอดภัย",
        'password_save_master_required': "บันทึกรหัสผ่าน (สามารถทำได้ด้วยรหัสผ่านหลักเท่านั้น)",
        'password_save_question': "PDF ปัจจุบันมีการป้องกันด้วยรหัสผ่าน คุณต้องการใช้รหัสผ่านที่มีอยู่ ตั้งใหม่ หรือบันทึกโดยไม่เข้ารหัส?",
        'password_select': "เลือกรหัสผ่าน",
        'password_select_none': "ไม่ได้เลือกรหัสผ่าน\n\nโปรดเลือกรหัสผ่านจากรายการ",
        'password_select_one': "โปรดเลือกรหัสผ่านเพียงหนึ่งเดียว\n\nคุณทำเครื่องหมายรหัสผ่านหลายรายการ",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_สำรอง",
        'filename_insert_suffix': "_พร้อมการแทรก",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_ลบหน้าแล้ว",
        'filename_pages_moved': "_ย้ายหน้าแล้ว",
        'filename_rotated_all_suffix': "_หมุนทุกหน้าแล้ว",
        'filename_rotated_suffix': "_หมุนหน้าแล้ว",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "การกำหนดค่าชื่อไฟล์เมื่อมีการเปลี่ยนแปลง PDF",
        'filename_keep_suffixes': "เก็บนามสกุลเดิมไว้ (เช่น _พร้อมข้อความ)",
        'filename_keep_suffixes_false': "แทนที่",
        'filename_keep_suffixes_true': "เก็บไว้",
        'filename_preview_label': "ตัวอย่างชื่อไฟล์:",
        'filename_preview_overwrite_hint': "ไม่มีตัวอย่าง – ไฟล์ต้นฉบับจะถูกเขียนทับ",
        'filename_separator': "ตัวคั่นระหว่างคำ",
        'filename_separator_none': "ไม่มีตัวคั่น",
        'filename_separator_space': "ช่องว่าง ( )",
        'filename_separator_underscore': "ขีดล่าง (_)",
        'filename_settings_saved': "บันทึกการตั้งค่าชื่อไฟล์แล้ว",
        'filename_settings_title': "การจัดรูปแบบชื่อไฟล์และการสำรองข้อมูล",
        'filename_timestamp_position': "ตำแหน่งของประทับเวลา",
        'filename_timestamp_position_after': "หลังชื่อฐาน",
        'filename_timestamp_position_before': "ข้างหน้าสุด",
        'filename_timestamp_position_end': "ที่ส่วนท้าย",
        'filename_use_timestamp': "ใช้ประทับเวลา",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>พฤติกรรมเมื่อมีการเปลี่ยนแปลง:</b><ul><li>การลบและแทรกหน้า</li><li>การแทรกข้อความ ลายเซ็น รูปภาพ และรูปร่าง</li><li>OCR</li></ul></html>",
        'backup_section': "การสำรองข้อมูลสำหรับการดำเนินการหน้า (ลบ ย้าย)",
        'behavior_info': "หมายเหตุ: เมื่อ 'เขียนทับต้นฉบับ' ประทับเวลาและคำต่อท้ายจะถูกละเว้น – ไฟล์จะคงชื่อไว้",
        'behavior_new_file': "สร้างไฟล์ใหม่เสมอ (พร้อมประทับเวลาและคำต่อท้าย)",
        'behavior_overwrite': "เขียนทับต้นฉบับ (ไม่มีไฟล์ใหม่)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "หมุนทุกหน้าแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {0}",
        'all_pages_rotated_voice': "หมุนทุกหน้าแล้ว สร้างไฟล์ใหม่",
        'empty_pages_deleted_new_file': "ลบหน้าเปล่า {0} หน้าแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {1}",
        'empty_pages_deleted_voice': "ลบหน้าเปล่า {0} หน้าแล้ว สร้างไฟล์ใหม่",
        'ocr_keep_original': "เก็บต้นฉบับไว้ (เปิดด้วยตนเองทีหลัง)",
        'ocr_new_file_question': "PDF ใหม่ที่ค้นหาได้ถูกบันทึกที่:\n{0}\n\nคุณต้องการเปิดตอนนี้หรือไม่?",
        'ocr_open_new': "เปิดไฟล์ OCR ใหม่",
        'ocr_original_kept': "ไฟล์ต้นฉบับยังคงเปิดอยู่ ไฟล์ OCR ถูกบันทึกแล้ว",
        'page_deleted_new_file': "ลบหน้า {0} แล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {1}",
        'page_deleted_voice': "ลบหน้า {0} แล้ว สร้างไฟล์ใหม่",
        'page_rotated_new_file': "หมุนหน้า {0} แล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {1}",
        'page_rotated_voice': "หมุนหน้า {0} แล้ว สร้างไฟล์ใหม่",
        'pages_deleted_new_file': "ลบ {0} หน้าแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {1}",
        'pages_deleted_new_file_voice': "ลบ {0} หน้าแล้ว สร้างไฟล์ใหม่",
        'pages_inserted_new_file': "แทรก {0} หน้าแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {1}",
        'pages_inserted_new_file_ask': "แทรก {0} หน้าแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {1}\n\nคุณต้องการเปิดตอนนี้หรือไม่?",
        'pages_inserted_voice_new': "แทรก {0} หน้าแล้ว สร้างไฟล์ใหม่",
        'pages_moved_new_file': "ย้าย {0} หน้าแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nไฟล์ใหม่: {1}",
        'pages_moved_new_file_voice': "ย้าย {0} หน้าแล้ว สร้างไฟล์ใหม่",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "ไม่แสดงอีก",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 การตั้งค่าการสำรองข้อมูล</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ เปิดการสำรองข้อมูล</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">สำหรับการเปลี่ยนแปลงทั้งหมดที่เขียนทับต้นฉบับ</strong> (ข้อความ ลายเซ็น รูปภาพ รูปร่าง OCR การหมุน การแทรก การลบ/ย้ายหน้า) <strong>จะสร้างการสำรองข้อมูลพร้อมประทับเวลาโดยอัตโนมัติ</strong> ก่อนที่จะใช้การเปลี่ยนแปลง</p>
                <p style="margin: 5px 0 5px 20px;">• การสำรองข้อมูลจะอยู่ถัดจากไฟล์ต้นฉบับ (เช่น <code>เอกสาร_สำรอง_20260412_120000.pdf</code>)</p>
                <p style="margin: 5px 0 5px 20px;">• หากคุณเปิดใช้งานตัวเลือก <strong>„เขียนทับต้นฉบับ“</strong> เพิ่มเติม ก็จะสร้างการสำรองข้อมูลด้วยเช่นกัน</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 ปิดการสำรองข้อมูล</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>ไม่มีการสร้างการสำรองข้อมูล</strong> – ทั้งเมื่อเขียนทับและเมื่อดำเนินการกับหน้า</p>
                <p style="margin: 5px 0 5px 20px;">• ไฟล์ต้นฉบับอาจสูญหายอย่างไม่มีทางกู้คืนเมื่อถูกเขียนทับ</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">แนะนำสำหรับผู้ใช้ที่มีประสบการณ์เท่านั้น!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>เคล็ดลับ:</strong> การตั้งค่าการสำรองข้อมูลเป็นอิสระจากตัวเลือก „เขียนทับต้นฉบับ“ คุณสามารถรวมทั้งสองอย่างได้<br>
                คุณสามารถซ่อนข้อความนี้ได้อย่างถาวร
            </div>
        </div>
        """,
        'backup_info_title': "พฤติกรรมการสำรองข้อมูล",
        'backup_info_voice': "แจ้งเกี่ยวกับพฤติกรรมการสำรองข้อมูลเมื่อดำเนินการกับหน้า เปิดการสำรองข้อมูลจะเขียนทับต้นฉบับ ปิดการสำรองข้อมูลจะสร้างไฟล์ใหม่",
        'show_backup_info': "ข้อมูลเกี่ยวกับการตั้งค่าการสำรองข้อมูล",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "ไม่แสดงอีก",
        'overwrite_enable_backup': "เปิดใช้งานการสำรองข้อมูล (แนะนำ)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ เขียนทับต้นฉบับ</p>
            <p>หากคุณเปิดใช้งานตัวเลือกนี้ การเปลี่ยนแปลง (ข้อความ ลายเซ็น รูปภาพ รูปร่าง OCR การหมุน การแทรก) จะ <strong>ถูกบันทึกโดยตรงในไฟล์ต้นฉบับ</strong> – <strong>ไม่มีไฟล์ใหม่ถูกสร้าง</strong></p>
            <p>• ชื่อไฟล์ยังคงเดิม<br>
            • ประทับเวลาและคำต่อท้ายจะถูกละเว้น<br>
            • <strong>หากไม่มีการสำรองข้อมูล ไฟล์ต้นฉบับอาจสูญหายอย่างไม่มีทางกู้คืน</strong></p>
            <p style="color: #FFD700;">คำแนะนำ: เปิดใช้งานตัวเลือกการสำรองข้อมูลเพิ่มเติมเพื่อรับสำเนาความปลอดภัยอัตโนมัติ</p>
        </div>
        """,
        'overwrite_info_title': "เขียนทับต้นฉบับ",
        'overwrite_info_voice': "คำเตือน: เขียนทับต้นฉบับ – ไม่มีไฟล์ใหม่ แนะนำให้สำรองข้อมูล",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "แทรก {0} หน้าแล้ว\n\nไฟล์ต้นฉบับถูกเขียนทับ\nสร้างการสำรองข้อมูลแล้ว",
        'pages_inserted_overwrite_no_backup': "แทรก {0} หน้าแล้ว\n\nไฟล์ต้นฉบับถูกเขียนทับ\nไม่ได้สร้างการสำรองข้อมูล",
        'texts_saved_overwrite_with_backup': "บันทึกการเปลี่ยนแปลงในไฟล์ต้นฉบับแล้ว\n\nสร้างการสำรองข้อมูลแล้ว",
        'texts_saved_overwrite_no_backup': "บันทึกการเปลี่ยนแปลงในไฟล์ต้นฉบับแล้ว\n\nไม่ได้สร้างการสำรองข้อมูล",
        'texts_crosses_saved_new_file': "แทรก {0} {1} และ {2} {3} แล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nสร้างไฟล์ใหม่แล้ว\n\nกำลังโหลด PDF ใหม่...",
        'texts_saved_new_file': "แทรก {0} {1} แล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nสร้างไฟล์ใหม่แล้ว\n\nกำลังโหลด PDF ใหม่...",
        'crosses_saved_new_file': "แทรก {0} {1} แล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nสร้างไฟล์ใหม่แล้ว\n\nกำลังโหลด PDF ใหม่...",
        'elements_saved_new_file': "แทรก {0} องค์ประกอบแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nสร้างไฟล์ใหม่แล้ว\n\nกำลังโหลด PDF ใหม่...",
        'signatures_saved_overwrite_with_backup': "บันทึกลายเซ็นในไฟล์ต้นฉบับแล้ว\n\nสร้างการสำรองข้อมูลแล้ว",
        'signatures_saved_overwrite_no_backup': "บันทึกลายเซ็นในไฟล์ต้นฉบับแล้ว\n\nไม่ได้สร้างการสำรองข้อมูล",
        'images_saved_overwrite_with_backup': "บันทึกรูปภาพในไฟล์ต้นฉบับแล้ว\n\nสร้างการสำรองข้อมูลแล้ว",
        'images_saved_overwrite_no_backup': "บันทึกรูปภาพในไฟล์ต้นฉบับแล้ว\n\nไม่ได้สร้างการสำรองข้อมูล",
        'forms_saved_overwrite_with_backup': "บันทึกรูปร่างในไฟล์ต้นฉบับแล้ว\n\nสร้างการสำรองข้อมูลแล้ว",
        'forms_saved_overwrite_no_backup': "บันทึกรูปร่างในไฟล์ต้นฉบับแล้ว\n\nไม่ได้สร้างการสำรองข้อมูล",
        'signatures_saved_new_file': "แทรก {0} ลายเซ็นแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nสร้างไฟล์ใหม่แล้ว\n\nกำลังโหลด PDF ใหม่...",
        'images_saved_new_file': "แทรก {0} รูปภาพแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nสร้างไฟล์ใหม่แล้ว\n\nกำลังโหลด PDF ใหม่...",
        'forms_saved_new_file': "แทรก {0} รูปร่างแล้ว\n\nไฟล์ต้นฉบับไม่เปลี่ยนแปลง\nสร้างไฟล์ใหม่แล้ว\n\nกำลังโหลด PDF ใหม่...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "คำเตือน: PDF นี้มีหน้าที่หมุนแล้ว การวางตำแหน่งอาจคลาดเคลื่อน",
        'page_rotated_warning_title': "ตรวจพบหน้าที่หมุน",
        'page_rotated_warning_message': "หน้าปัจจุบัน {0} ถูกหมุน {1}°\n\nการแทรกองค์ประกอบบนหน้าที่หมุนไม่รองรับ\n\nคุณต้องการหมุนหน้าไปยังตำแหน่งตั้งตรงตอนนี้หรือไม่?",
        'page_rotated_warning_voice': "คำเตือน: หน้าถูกหมุน กรุณาหมุนหน้าก่อน",
        'paste_on_rotated_page_simple_warning': "ไม่สามารถแทรกบนหน้า {0} ได้!\n\nหน้านี้ถูกหมุน {1}°\n\nกรุณาหมุนหน้าไปที่ 0° ก่อน (เมนู: แก้ไข → จัดแนวหน้า)\n\nคำเตือน:\nองค์ประกอบที่คัดลอกก่อนหน้านี้จะหายไปหากคุณไม่บันทึกก่อนหมุนหน้า",
        'paste_on_rotated_page_voice': "ยกเลิกการแทรก หน้าถูกหมุน กรุณาจัดแนวหน้าก่อน",
        'page_rotated_cancel': "ยกเลิก",
        'page_rotated_rotate_until_upright': "หมุนหน้าซ้ำๆ (จนกว่าจะตั้งตรง)",
        'page_rotated_now_upright': "หน้า現在ตั้งตรงแล้ว คุณสามารถแทรกได้แล้ว",
        'page_rotated_still_not_upright': "ไม่สามารถหมุนหน้าไปยังตำแหน่งตั้งตรงได้ กรุณาแก้ไขด้วยตนเอง",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "วิธีใช้: แก้ไขหน้าที่หมุน",
        'help_rotated_pages_voice': "กำลังเปิดวิธีใช้สำหรับแก้ไขหน้าที่หมุน",
        'btn_help': "วิธีใช้",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 ปัญหา: หน้าที่หมุน – การแทรกทำงานไม่ถูกต้อง</p>

            <p>หากการแทรกข้อความ ลายเซ็น หรือรูปร่างบนหน้าที่หมุนทำงานไม่ถูกต้อง คุณสามารถแก้ไขหน้าด้วยโปรแกรมแก้ไข PDF ภายนอก</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ วิธีแก้ด้วยเครื่องมือภายนอก (เช่น ตัวอย่าง macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>ส่งออกหน้า</strong><br>
                &nbsp;&nbsp;คลิกในเมนู <strong>ไฟล์ → ส่งออกเป็นหน้า</strong> หรือใช้วิธีอื่นเพื่อบันทึกหน้าที่ต้องการเป็น PDF เดี่ยว</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>เปิดหน้าในโปรแกรมภายนอก</strong><br>
                &nbsp;&nbsp;เปิด PDF ที่ส่งออกในโปรแกรมแก้ไข PDF (เช่น <strong>ตัวอย่าง macOS</strong>, Adobe Acrobat, PDF Expert)</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>หมุนหน้า</strong><br>
                &nbsp;&nbsp;หมุนหน้าให้ตั้งตรง (ในตัวอย่าง: <strong>เครื่องมือ → หมุน</strong> หรือ <strong>⌘ + R</strong>)</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>บันทึก</strong><br>
                &nbsp;&nbsp;บันทึกหน้าที่แก้ไขแล้ว (<strong>⌘ + S</strong>)</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>แทรกหน้ากลับเข้าไปในเอกสารต้นฉบับ</strong><br>
                &nbsp;&nbsp;กลับไปที่ PDFDarkView และแทรกหน้าที่แก้ไขแล้วในตำแหน่งที่ต้องการ:<br>
                &nbsp;&nbsp;<strong>แก้ไข → แทรกหน้า</strong></p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 ทางเลือกอื่น: หมุนหน้าในไฟล์ต้นฉบับ</p>
                <p style="margin: 5px 0 5px 20px;">• ใช้ฟังก์ชันหมุนในตัว (<strong>แก้ไข → หมุนหน้า</strong>) เพื่อแก้ไขหน้าทีละขั้น<br>
                • หลังจากหมุนแต่ละครั้ง คุณสามารถตรวจสอบว่าการแทรกทำงานตอนนี้หรือไม่<br>
                • นี่มักเป็นวิธีแก้ปัญหาที่เร็วกว่า – ลองดูก่อน!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>เคล็ดลับ:</strong> หากคุณพบหน้าที่หมุนบ่อยครั้ง คุณสามารถซ่อนคำเตือนในกล่องโต้ตอบการแทรกได้อย่างถาวร<br>
                การวางตำแหน่งอาจคลาดเคลื่อน – ใช้ตัวเลือกนี้เฉพาะเมื่อคุณทราบผลที่ตามมา
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "จัดแนวหน้า",
        'menu_rotate_normalize_tooltip': "หมุนหน้าหรือรีเซ็ตเป็น 0°",
        'normalize_current_page': "นำหน้าปัจจุบันไปยังตำแหน่งตั้งตรง (ตั้งเป็น 0°)",
        'normalize_all_pages': "นำทุกหน้าไปยังตำแหน่งตั้งตรง (ตั้งเป็น 0°)",
        'page_normalized': "ตั้งหน้าตั้ง {0} ไปยังตำแหน่งตั้งตรงแล้ว",
        'all_pages_normalized': "ตั้งทุกหน้าไปยังตำแหน่งตั้งตรงแล้ว",
        'page_already_upright': "หน้า {0} ตั้งตรงอยู่แล้ว",
        'all_pages_already_upright': "ทุกหน้าตั้งตรงอยู่แล้ว",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF ไม่มีข้อความที่ค้นหาได้</p><p>คุณต้องการทำ OCR เพื่อส่งออกไปยัง {0} หรือไม่?</p>",
        'export_ocr_voice': "PDF ไม่มีข้อความ จำเป็นต้องใช้ OCR สำหรับการส่งออกไปยัง {0}",
        'export_no_ocr_possible': "ไม่สามารถส่งออกโดยไม่มี OCR ได้ กรุณาทำ OCR ผ่านเมนู",
        'ocr_failed_export_not_possible': "OCR ล้มเหลว ไม่สามารถดำเนินการส่งออกได้",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF จะเปิดในตัวอย่าง กรุณาเริ่มกระบวนการพิมพ์ที่นั่น",
        'print_preview_manual': "เปิด PDF แล้ว กรุณาดำเนินการคำสั่งพิมพ์ด้วยตนเอง (เช่น Ctrl+P)",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "รวม PDF",
        'merge_pdfs': "รวม PDF",
        'merge_progress_title': "กำลังรวม PDF...",
        'merge_pdfs_list': "PDF ตามลำดับ (ลากและวางเพื่อจัดเรียง)",
        'merge_add_pdf': "เพิ่ม PDF",
        'merge_remove': "ลบออก",
        'merge_move_up': "ขึ้น",
        'merge_move_down': "ลง",
        'merge_pdfs_info': "💡 เคล็ดลับ: คุณสามารถเปลี่ยนลำดับได้โดยการลากและวาง",
        'merge_no_pdfs': "ไม่ได้เลือก PDF คลิก 'เพิ่ม PDF'",
        'merge_info': "เลือก {0} PDF (ประมาณ {1} หน้า)",
        'merge_open_file': "เปิดไฟล์",
        'merge_merge': "รวม",
        'merge_error': "ข้อผิดพลาดขณะรวม",
        'merge_min_two_pdfs_error': "กรุณาเลือกไฟล์ PDF อย่างน้อยสองไฟล์เพื่อรวม",
        'merge_select_pdfs': "เลือก PDF เพื่อรวม",
        'merge_error_file': "ข้อผิดพลาดขณะประมวลผล",
        'merge_cancelled': "ยกเลิกการรวมแล้ว",
        'merge_preparing': "กำลังเตรียม...",
        'merge_processing': "กำลังประมวลผล PDF {0} จาก {1}",
        'merge_saving': "กำลังบันทึก PDF ที่รวมแล้ว...",
        'merge_complete': "เสร็จสิ้น!",
        'merge_success_title': "การรวมสำเร็จ",
        'merge_success_voice': "รวม PDF {0} ไฟล์สำเร็จแล้ว",
        'merge_success_message': "รวม PDF {0} ไฟล์สำเร็จแล้ว\n\nเอกสารใหม่ตอนนี้มี {1} หน้า\n\nไฟล์ใหม่:\n{2}\n\nตำแหน่งที่บันทึก:\n{3}\n{2}\n\nคุณต้องการเปิด PDF นี้หรือไม่?",
        'replace_file_title': "แทนที่ไฟล์?",
        'replace_file_message': "มี PDF เปิดอยู่แล้ว คุณต้องการแทนที่ด้วยไฟล์ใหม่หรือไม่?",
        'btn_yes': "ใช่",
        'btn_no': "ไม่",
        'filename_merge_suffix': "รวมแล้ว",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "กำลังเปิด {0}...",
        'progress_merge_reading': "กำลังอ่าน {0}...",
        'progress_merge_adding': "กำลังเพิ่ม {0} หน้า...",
        'progress_merge_optimizing': "กำลังปรับแต่ง PDF...",
        'progress_merge_writing': "กำลังเขียน PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "การปิด PDF",
        'action_close_window': "การปิดหน้าต่าง",
        'action_open_new_pdf': "การเปิด PDF ใหม่",
        'action_quit_app': "การออกจากแอปพลิเคชัน",
        'changes_saved': "บันทึกการเปลี่ยนแปลงแล้ว",
        'file_close_title': "ปิดไฟล์ PDF",
        'save_before_action': "ควรบันทึกการเปลี่ยนแปลงก่อน {0} หรือไม่? ใช่ หรือ ไม่?",
        'save_before_action_voice': "ควรบันทึกการเปลี่ยนแปลงก่อน {0} หรือไม่? ใช่ หรือ ไม่?",
        'save_before_close_question': "ควรบันทึกการเปลี่ยนแปลงก่อนปิดหรือไม่? ใช่ หรือ ไม่?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>สร้าง PDF ที่ค้นหาได้:\n\n{0}\n\n<b>ลองอีกครั้งหากจำเป็น",
        "ocr_rotate_title": "จัดแนวหน้าก่อน OCR",
        "ocr_rotate_question": "PDF มีหน้าที่ถูกหมุน\nคุณต้องการจัดแนวทุกหน้าเป็น 0° ก่อน OCR หรือไม่?\nซึ่งจะช่วยปรับปรุงการรู้จำข้อความอย่างมาก",
        "ocr_rotate_yes": "ใช่, จัดแนว",
        "ocr_rotate_no": "ไม่, เริ่ม OCR โดยตรง",
        "ocr_rotate_voice": "PDF มีหน้าที่ถูกหมุน ควรจัดแนวทุกหน้าก่อน OCR หรือไม่?",
        "ocr_not_performed_message": "ไม่มีข้อความ กรุณาทำ OCR (เมนู \"แก้ไข\" → \"ทำ OCR\" หรือปุ่ม Ctrl+R)",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "การตั้งค่า OCR",
        "ocr_language_btn": "เลือกภาษา OCR",
        "ocr_language": "ภาษา OCR",
        "ocr_language_current": "ภาษาปัจจุบัน:",
        "ocr_param_info": "ข้อมูลเกี่ยวกับพารามิเตอร์",

        "ocr_force_ocr_label": "บังคับ OCR",
        "ocr_deskew_label": "แก้ไขความเอียง",
        "ocr_clean_label": "ทำความสะอาดภาพ",
        "ocr_oversample_label": "ความละเอียด (DPI)",
        "ocr_pagesegmode_label": "การแบ่งหน้า",
        "ocr_oem_label": "โหมดเครื่องมือ OCR",
        "ocr_optimize_label": "การบีบอัด PDF",
        "ocr_jobs_label": "กระบวนการขนาน",
        "ocr_verbose_label": "รายละเอียดบันทึก",

        "ocr_force_ocr_tooltip": "บังคับ OCR บนทุกหน้า แม้ว่าจะมีข้อความอยู่แล้ว",
        "ocr_deskew_tooltip": "จัดแนวการสแกนที่เอียงโดยอัตโนมัติ",
        "ocr_clean_tooltip": "ลบสัญญาณรบกวนและสิ่งปลอมปนออกจากภาพ",
        "ocr_oversample_tooltip": "ขยายภาพก่อน OCR ไปยัง DPI นี้",
        "ocr_pagesegmode_tooltip": "กำหนดวิธีการแบ่งหน้าออกเป็นพื้นที่ข้อความ",
        "ocr_oem_tooltip": "เลือกเครื่องมือ OCR ของ Tesseract",
        "ocr_optimize_tooltip": "ระดับการบีบอัดของ PDF เอาต์พุต",
        "ocr_jobs_tooltip": "จำนวนกระบวนการ OCR แบบขนาน",
        "ocr_verbose_tooltip": "ระดับรายละเอียดของเอาต์พุตบันทึก",
        "ocr_settings_explain_btn": "คำอธิบาย",

        "ocr_force_ocr_explain": "บังคับการรู้จำข้อความบน <b>ทุก</b>หน้า แม้ว่าจะมีข้อความอยู่แล้ว\n\nคำแนะนำ: <b>เปิด</b> สำหรับ PDF ที่สแกน, <b>ปิด</b> สำหรับ PDF ต้นฉบับที่มีข้อความอยู่แล้ว",

        "ocr_deskew_explain": "แก้ไขการสแกนที่เอียงเล็กน้อย (สูงสุดประมาณ 5°)\n\nคำแนะนำ: <b>เปิด</b> สำหรับเอกสารที่สแกน, <b>ปิด</b> หากหน้าตรงสมบูรณ์แบบอยู่แล้ว",

        "ocr_clean_explain": "ลบสัญญาณรบกวน จุด และสิ่งปลอมปนเล็กน้อยออกจากภาพ\n<b>สำคัญ:</b> สำหรับข้อความภาษาอาหรับ ไทย หรือเวียดนามที่มีเครื่องหมายกำกับเสียง (จุดเหนือ/ใต้ตัวอักษร) ควร<b>ปิดใช้งาน</b>ตัวเลือกนี้ มิฉะนั้นอักขระสำคัญอาจสูญหายได้",

        "ocr_oversample_explain": "ขยายภาพ <b>ก่อน</b>การรู้จำข้อความไปยัง DPI ที่กำหนด<br><br>• <b>72-150 DPI:</b> รวดเร็วมาก แต่อัตราการรู้จำต่ำ<br>• <b>200-300 DPI:</b> ช่วงที่เหมาะสมที่สุด (ค่าเริ่มต้น: 300)<br>• <b>400+ DPI:</b> แทบไม่มีการรู้จำที่ดีขึ้น แต่ไฟล์ใหญ่ขึ้นอย่างมาก<br><br>คำแนะนำ: 300 DPI สำหรับอักษรที่ซับซ้อน (อาหรับ จีน ญี่ปุ่น), 200 DPI สำหรับภาษาตะวันตก",

        "ocr_pagesegmode_explain": "กำหนดวิธีที่ Tesseract แบ่งหน้าออกเป็นพื้นที่ข้อความ\n\n• <b>3 - อัตโนมัติ (ค่าเริ่มต้น):</b> เหมาะสำหรับเลย์เอาต์แบบผสม\n• <b>4 - คอลัมน์เดียว:</b> สำหรับข้อความคอลัมน์เดียว\n• <b>5 - บล็อกแนวตั้ง:</b> สำหรับอักษรแนวตั้ง (ญี่ปุ่น จีน)\n• <b>6 - บล็อกข้อความสม่ำเสมอ:</b> เหมาะที่สุดสำหรับข้อความที่ไหลโดยไม่มีคอลัมน์\n• <b>11 - ภาพดิบ:</b> สำหรับการสแกนไม่ดี / ลายมือ\n\nคำแนะนำ: <b>6</b> สำหรับเอกสารข้อความธรรมดา, <b>3</b> สำหรับเลย์เอาต์ที่ซับซ้อน",

        "ocr_oem_explain": "เลือกเครื่องมือ OCR ของ Tesseract\n\n• <b>0 - Legacy:</b> เครื่องมือเก่า (รวดเร็ว แต่แม่นยำน้อยกว่า)\n• <b>1 - LSTM:</b> เครื่องมือโครงข่ายประสาท (ช้ากว่า แต่แม่นยำกว่า)\n• <b>2 - Legacy + LSTM:</b> รวมผลลัพธ์ทั้งสอง\n• <b>3 - ค่าเริ่มต้น (LSTM 優先):</b> ตัวเลือกที่ดีที่สุดสำหรับกรณีส่วนใหญ่\n\nคำแนะนำ: <b>3</b> เพื่อความแม่นยำในการรู้จำสูงสุด",

        "ocr_optimize_explain": "บีบอัด PDF เอาต์พุต\n\n• <b>0:</b> ไม่มีการเพิ่มประสิทธิภาพ (การประมวลผลเร็วที่สุด)\n• <b>1:</b> การเพิ่มประสิทธิภาพเล็กน้อย (การประนีประนอมที่ดี)\n• <b>2:</b> การเพิ่มประสิทธิภาพปานกลาง\n• <b>3:</b> การเพิ่มประสิทธิภาพสูง (ไฟล์เล็กที่สุด แต่ช้ากว่า)\n\nคำแนะนำ: <b>1</b> สำหรับการใช้งานประจำวัน",

        "ocr_jobs_explain": "จำนวนกระบวนการขนานสำหรับ OCR\n\n• <b>1:</b> ช้า แต่การใช้หน่วยความจำต่ำที่สุด\n• <b>4-8:</b> เหมาะสำหรับโปรเซสเซอร์แบบหลายคอร์สมัยใหม่\n• <b>12+:</b> แทบจะไม่เร็วขึ้นด้วยการใช้หน่วยความจำสูง\n\nคำแนะนำ: จำนวนคอร์ CPU (เช่น <b>4</b> บนระบบ 4 คอร์)",

        "ocr_verbose_explain": "ระดับรายละเอียดของเอาต์พุตบันทึกในคอนโซล\n\n• <b>0:</b> ไม่มีเอาต์พุต\n• <b>1:</b> ความคืบหน้าและข้อความสถานะ\n• <b>2:</b> เอาต์พุตโดยละเอียด\n• <b>3:</b> เอาต์พุตการดีบักแบบเต็ม (กว้างขวางมาก)\n\nคำแนะนำ: <b>1</b> สำหรับการทำงานปกติ",

        "ocr_reset_title": "รีเซ็ตการตั้งค่าแล้ว",
        "ocr_reset_message": "การตั้งค่า OCR ทั้งหมดถูกรีเซ็ตเป็นค่าดEFAULT",
        "info_tooltip": "ข้อมูลเพิ่มเติมเกี่ยวกับพารามิเตอร์นี้",
        "ocr_reset_defaults": "รีเซ็ตเป็นค่าเริ่มต้น",

        "ocr_psm_0": "อัตโนมัติ (เครื่องมือ Legacy)",
        "ocr_psm_1": "การตรวจจับคอลัมน์อัตโนมัติ",
        "ocr_psm_3": "อัตโนมัติ (ค่าเริ่มต้น)",
        "ocr_psm_4": "คอลัมน์เดียว",
        "ocr_psm_5": "บล็อกแนวตั้ง",
        "ocr_psm_6": "บล็อกข้อความสม่ำเสมอ",
        "ocr_psm_7": "บรรทัดข้อความเดียว",
        "ocr_psm_8": "คำเดียว",
        "ocr_psm_11": "ภาพดิบ (ไม่มีการวิเคราะห์เลย์เอาต์)",

        "ocr_oem_0": "เครื่องมือ Legacy (รวดเร็ว)",
        "ocr_oem_1": "เครื่องมือ LSTM (โครงข่ายประสาท, แม่นยำ)",
        "ocr_oem_2": "Legacy + LSTM แบบรวม",
        "ocr_oem_3": "ค่าเริ่มต้น (LSTM 優先)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "ภาษา OCR...",
        "ocr_language_title": "เลือกภาษา OCR",
        "ocr_language_instruction": "เลือกภาษาสำหรับการรู้จำข้อความ (OCR)\nข้อควรระวัง: หลายภาษาส่งผลเสียต่อประสิทธิภาพและความแม่นยำ!\nคุณจะได้ผลลัพธ์ที่ดีที่สุดหากเลือกภาษาเดียว",
        "ocr_language_predefined": "ชุดค่าผสมที่กำหนดไว้ล่วงหน้า",
        "ocr_language_custom": "กำหนดเอง...",
        "ocr_language_selected": "ภาษา OCR ที่เลือก",
        "ocr_language_changed": "เปลี่ยนภาษา OCR เป็น {0}",
        "ocr_language_auto_detect": "ตรวจพบภาษาที่มีอยู่โดยอัตโนมัติ",
        "ocr_language_none_found": "ไม่พบข้อมูลภาษา Tesseract! กรุณาติดตั้งแพ็คเกจภาษา (เช่น 'tesseract-ocr-deu', 'tesseract-ocr-eng')",
        "ocr_language_select_custom": "การเลือกภาษาแบบกำหนดเอง",
        "ocr_language_available": "ภาษาที่มีอยู่ (ติดตั้งแล้ว):",
        "ocr_language_select_hint": "เลือกหนึ่งภาษาหรือมากกว่า:",
        "ocr_language_confirm": "ใช้",
        "ocr_language_reset": "รีเซ็ตเป็นค่าเริ่มต้น (deu+eng+vie)",
        "ocr_language_priorities": "ภาษาที่แนะนำ (ติดตั้งไว้ล่วงหน้า):",

        "select_all_languages": "เลือกทั้งหมด",
        "clear_all_languages": "ล้างการเลือก",
        "install_language_packs": "ติดตั้งแพ็คเกจภาษาที่ขาดหายไป...",
        "install_hint": "💡 เคล็ดลับ: ไม่ใช่ทุกภาษาที่ติดตั้งในระบบของคุณ ปุ่มนี้จะช่วยคุณในการติดตั้ง",
        "ocr_language_install_title": "การติดตั้งแพ็คเกจภาษา Tesseract",

        "ocr_missing_languages": "แพ็คเกจภาษา OCR ที่ขาดหายไป",
        "ocr_missing_languages_message": "ภาษาที่เลือกต่อไปนี้ไม่ได้ติดตั้งในระบบของคุณ:\n\n{0}\n\nกรุณาติดตั้งแพ็คเกจภาษาที่ขาดหายไป (ดูความช่วยเหลือภายใต้ 'ความช่วยเหลือการติดตั้ง')\n\nคุณต้องการเปิดความช่วยเหลือการติดตั้งตอนนี้หรือไม่?",
        "ocr_missing_languages_voice": "แพ็คเกจภาษาขาดหายไป กรุณาติดตั้งภาษาที่ขาดหายไป",
        "ocr_install_help_now": "เปิดความช่วยเหลือ",
        "ocr_continue_anyway": "ลองต่อไป",
        "ocr_language_error_title": "ข้อผิดพลาดภาษา OCR",
        "ocr_language_error_message": "ข้อผิดพลาดระหว่างการรู้จำข้อความ: {0}\n\nกรุณาตรวจสอบการตั้งค่าภาษา OCR ของคุณ (การตั้งค่า → ภาษา OCR)",
        "ocr_install_help_button": "ความช่วยเหลือการติดตั้ง",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 ติดตั้งแพ็คเกจภาษา Tesseract</p>

        <p>เพื่อให้ OCR ทำงานในภาษาเฉพาะ ข้อมูลภาษาที่เกี่ยวข้องต้องติดตั้งในระบบของคุณ ทำตามคำแนะนำสำหรับระบบปฏิบัติการของคุณ:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>เปิด <strong>เทอร์มินัล</strong> (Finder → โปรแกรม → ยูทิลิตี้ → เทอร์มินัล)</li>
        <li>ติดตั้งภาษาที่มีอยู่ทั้งหมดด้วย:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (อาจใช้เวลาสักครู่)</li>
        <li>หรือเฉพาะภาษาเดียว (เช่น เวียดนาม):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        สำหรับ Homebrew เวอร์ชันปัจจุบัน อาจต้องดาวน์โหลด <code>*.traineddata</code> ด้วยตนเอง (ดูด้านล่าง)</li>
        <li>หลังติดตั้ง: ปิดกล่องโต้ตอบนี้แล้วเปิดการเลือกภาษา OCR อีกครั้ง – ภาษาใหม่จะปรากฏโดยอัตโนมัติ</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>เปิดเทอร์มินัล (Ctrl+Alt+T)</li>
        <li>ติดตั้งภาษาที่ต้องการ เช่น สำหรับเวียดนาม:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        รหัสภาษาที่สำคัญ: <code>deu</code> (เยอรมัน), <code>eng</code> (อังกฤษ), <code>vie</code> (เวียดนาม), <code>spa</code> (สเปน), <code>fra</code> (ฝรั่งเศส), <code>ita</code> (อิตาลี), <code>nld</code> (ดัตช์), <code>fin</code> (ฟินแลนด์), <code>swe</code> (สวีเดน), <code>nor</code> (นอร์เวย์)</li>
        <li>แสดงแพ็คเกจที่มีอยู่ทั้งหมด:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ด้วยตนเอง)</p>
        <ol>
        <li>ดาวน์โหลดไฟล์ <code>*.traineddata</code> ที่ต้องการจาก:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (เช่น <code>vie.traineddata</code> สำหรับเวียดนาม)</li>
        <li>คัดลอกไฟล์ไปยังโฟลเดอร์ภาษาของ Tesseract โดยปกติ:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (ปรับตามการติดตั้งเฉพาะบุคคล)</li>
        <li>รีสตาร์ทแอปพลิเคชัน (หรือเปิดการเลือกภาษา OCR อีกครั้ง)</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 ทางเลือกสำหรับทุกระบบ</p>
        <ul>
        <li>ติดตั้ง <strong>OCRmyPDF</strong> และ <strong>Tesseract</strong> ด้วยตัวจัดการแพ็คเกจที่คุณเลือก การติดตั้งส่วนใหญ่มีภาษามาตรฐานบางภาษาอยู่แล้ว (อังกฤษ, เยอรมัน, ฝรั่งเศส)</li>
        <li>ภาษาที่ขาดหายไปสามารถติดตั้งได้ตลอดเวลา – การเลือกภาษา OCR จะแสดงเฉพาะภาษาที่มีอยู่จริง</li>
        </ul>

        <hr>
        <p><b>✅ หลังติดตั้ง:</b> ไม่จำเป็นต้องรีสตาร์ทแอปพลิเคชัน – ภาษาใหม่ที่เพิ่มจะปรากฏในรายการทันที</p>
        <p><b>📖 ความช่วยเหลือเกี่ยวกับรหัสภาษา:</b> สามารถดูรายการทั้งหมดได้ใน <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">เอกสาร Tesseract</a></p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "แบบอักษร Noto Sans",
        "info_noto_font_voice": "คู่มือการติดตั้งแบบอักษร Noto Sans",
        "btn_info_noto_font_install": "ข้อมูลแบบอักษร",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ วิธีติดตั้งแบบอักษร Noto ฟรีจาก Google</h2>

        <p><strong>แบบอักษร Noto</strong> คือตระกูลแบบอักษรโอเพนซอร์สจาก Google เป้าหมายของพวกเขาคือการไม่เห็น <em>"โทฟุ"</em> (นั่นคือไม่มีกล่องว่าง □) และแสดงอักขระทุกตัวจากมาตรฐาน Unicode ได้อย่างถูกต้อง เป็นส่วนเสริมที่เหมาะสำหรับแอปพลิเคชันที่ต้องแสดงข้อความในหลายภาษาที่แตกต่างกัน</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 การติดตั้งบน macOS</h3>

        <p><strong>วิธีที่ 1: ใช้ Homebrew (สำหรับผู้ใช้ขั้นสูง)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>วิธีที่ 2: ผ่าน "Font Book" (แนะนำ)</strong></p>

        <ol>
        <li>ดาวน์โหลดแพ็คเกจแบบอักษรอย่างเป็นทางการ:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>แตกไฟล์ ZIP</li>
        <li>คัดลอกไฟล์ไปยัง <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 การติดตั้งบน Windows (10 และ 11)</h3>

        <p><strong>วิธีที่ 1: Microsoft Store (แนะนำ)</strong><br>
        ค้นหา "Google Noto Fonts" หรือ "Noto Sans" แล้วคลิก <strong>ติดตั้ง</strong></p>

        <p><strong>วิธีที่ 2: การติดตั้งด้วยตนเอง</strong></p>

        <ol>
        <li>ดาวน์โหลด:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>แตก ZIP</li>
        <li>เลือกไฟล์ .ttf / .otf</li>
        <li>คลิกขวา → <strong>ติดตั้ง</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        หรือ<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\ชื่อ\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 การติดตั้งบน Linux</h3>

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

        <p>การตรวจสอบ:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "จัดการที่คั่นหน้า",
        "bookmark_add": "เพิ่มที่คั่นหน้า",
        "bookmark_add_tooltip": "บันทึกหน้าปัจจุบันเป็นที่คั่นหน้า",
        "bookmark_remove": "ลบที่คั่นหน้า",
        "bookmark_remove_tooltip": "ลบที่คั่นหน้าที่ทำเครื่องหมาย",
        "bookmark_remove_all": "ลบทั้งหมด",
        "bookmark_remove_all_tooltip": "ลบที่คั่นหน้าทั้งหมดของ PDF นี้",
        "bookmark_jump": "ไปที่ที่คั่นหน้า",
        "bookmark_jump_tooltip": "ไปยังหน้าที่เลือก",
        "bookmark_name": "ชื่อ",
        "bookmark_page": "หน้า",
        "bookmark_no_bookmarks": "ไม่มีที่คั่นหน้า\nคลิก 'เพิ่ม' เพื่อบันทึกหน้าปัจจุบันเป็นที่คั่นหน้า",
        "bookmark_added": "เพิ่มที่คั่นหน้าสำหรับหน้า {0}: {1}",
        "bookmark_removed": "ลบที่คั่นหน้า: {0}",
        "bookmark_all_removed": "ลบที่คั่นหน้าทั้งหมดแล้ว",
        "bookmark_name_default": "หน้า {0}",
        "bookmark_name_prompt": "ชื่อสำหรับที่คั่นหน้า:\n(ข้อความยาวจะถูกย่อเหลือ 50 ตัวอักษร)",
        "bookmark_name_prompt_title": "ชื่อที่คั่นหน้า",
        "bookmark_confirm_remove_all": "คุณแน่ใจหรือต้องการลบที่คั่นหน้าทั้ง {0} รายการ?",
        "menu_bookmarks": "ที่คั่นหน้า",
        "bookmark_manage": "จัดการที่คั่นหน้า",
        "bookmark_next": "ที่คั่นหน้าถัดไป",
        "bookmark_prev": "ที่คั่นหน้าก่อนหน้า",
        "bookmark_page_display": "หน้า {0}",
        "bookmark_exists": "มีที่คั่นหน้าสำหรับหน้านี้ด้วยชื่อนี้อยู่แล้ว",
        "bookmark_select_first": "กรุณาเลือกที่คั่นหน้าก่อน",
        "bookmark_confirm_remove": "คุณแน่ใจหรือต้องการลบที่คั่นหน้า 'หน้า {0}: {1}'?",
        "bookmark_jumped_to": "ไปที่ที่คั่นหน้า '{0}' บนหน้า {1}",
        "bookmark_jumped_to_voice": "ที่คั่นหน้า {0}, หน้า {1}",
        "btn_close": "ปิด",

        "bookmark_list": "ที่คั่นหน้าของคุณ",
        "bookmark_rename": "เปลี่ยนชื่อที่คั่นหน้า",
        "bookmark_rename_tooltip": "เปลี่ยนชื่อที่คั่นหน้าที่เลือก",
        "bookmark_rename_title": "เปลี่ยนชื่อที่คั่นหน้า",
        "bookmark_rename_prompt": "ชื่อใหม่สำหรับที่คั่นหน้าบนหน้า {0}:\n(สูงสุด 50 ตัวอักษร)",
        "bookmark_renamed": "เปลี่ยนชื่อที่คั่นหน้า '{0}' เป็น '{1}' แล้ว",
        "bookmark_item_tooltip": "หน้า {0}: {1}\nดับเบิลคลิกเพื่อไป",
        "bookmark_name_exists_question": "มีที่คั่นหน้าชื่อ '{0}' บนหน้านี้อยู่แล้ว\nจะเปลี่ยนชื่อหรือไม่?",

        "context_bookmarks": "ที่คั่นหน้า",
        "context_bookmark_add_here": "เพิ่มที่คั่นหน้าสำหรับหน้านี้",
        "context_bookmarks_existing": "ที่คั่นหน้าที่มีอยู่:",
        "context_bookmarks_jump": "ไปที่ที่คั่นหน้า:",
        "context_bookmarks_none": "ไม่มีที่คั่นหน้า",
        "context_bookmarks_clear_all": "ลบที่คั่นหน้าทั้ง {0} รายการ",

        "bookmark_search_placeholder": "ค้นหาที่คั่นหน้า... (ชื่อหรือหน้า)",
        "bookmark_search_results": "พบ %d ที่คั่นหน้าสำหรับ \"%s\"",
        "bookmark_no_search_results": "ไม่พบที่คั่นหน้าสำหรับ \"%s\"",
        "bookmark_no_search_results_label": "ไม่มีผลลัพธ์สำหรับ \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "แก้ไขเมทาดาทา PDF",
        "metadata_title": "ชื่อเรื่อง",
        "metadata_title_placeholder": "ชื่อเรื่องเอกสาร",
        "metadata_title_tooltip": "ชื่อเรื่องของเอกสาร (แสดงในแถบชื่อเรื่อง)",
        "metadata_author": "ผู้แต่ง",
        "metadata_author_placeholder": "ชื่อผู้แต่ง",
        "metadata_author_tooltip": "ผู้สร้างเอกสาร",
        "metadata_subject": "หัวเรื่อง",
        "metadata_subject_placeholder": "หัวเรื่องของเอกสาร",
        "metadata_subject_tooltip": "คำอธิบายสั้น ๆ ของเนื้อหา",
        "metadata_keywords": "คำสำคัญ",
        "metadata_keywords_placeholder": "คำสำคัญ คั่นด้วยจุลภาค",
        "metadata_keywords_tooltip": "คำสำคัญสำหรับการจัดหมวดหมู่เอกสาร",
        "metadata_creator": "ผู้สร้าง",
        "metadata_creator_placeholder": "แอปพลิเคชันที่สร้าง PDF",
        "metadata_creator_tooltip": "ซอฟต์แวร์ที่ใช้สร้างเอกสาร",
        "metadata_producer": "ผู้ผลิต",
        "metadata_producer_placeholder": "แอปพลิเคชันที่แปลง PDF",
        "metadata_producer_tooltip": "ซอฟต์แวร์ที่แปลง PDF",
        "metadata_creation_date": "วันที่สร้าง",
        "metadata_creation_date_tooltip": "วันที่สร้างเอกสาร",
        "metadata_mod_date": "วันที่แก้ไข",
        "metadata_mod_date_tooltip": "วันที่แก้ไขครั้งล่าสุด",
        "metadata_pdf_info": "📄 ข้อมูล PDF",
        "metadata_pages": "จำนวนหน้า",
        "metadata_file_size": "ขนาดไฟล์",
        "metadata_pdf_version": "เวอร์ชัน PDF",
        "metadata_encrypted": "เข้ารหัส",
        "metadata_encrypted_yes": "ใช่ (ป้องกันด้วยรหัสผ่าน)",
        "metadata_encrypted_no": "ไม่",
        "metadata_reload": "📂 โหลดซ้ำจาก PDF",
        "metadata_reset": "ยกเลิกการเปลี่ยนแปลง",
        "metadata_reloaded": "โหลดเมทาดาทาซ้ำจาก PDF แล้ว",
        "metadata_reset_done": "รีเซ็ตฟิลด์เมทาดาทาทั้งหมดแล้ว",
        "metadata_no_file": "ไม่มีไฟล์ PDF ที่โหลด",
        "metadata_save_error": "ข้อผิดพลาดในการบันทึกเมทาดาทา",
        "metadata_saved": "บันทึกเมทาดาทาสำเร็จแล้ว",
        "metadata_pdf_version_unknown": "PDF (ไม่ทราบ)",
        "metadata_saved_message": "บันทึกเมทาดาทาสำเร็จแล้ว",
        "metadata_saved_voice": "บันทึกเมทาดาทาแล้ว",

        "metadata_custom": "🔧 เมทาดาทาแบบกำหนดเอง",
        "metadata_custom_placeholder": "{\n  \"ฟิลด์ของฉัน\": \"ค่าของฉัน\",\n  \"ฟิลด์อื่น\": 123\n}",
        "metadata_custom_tooltip": "รูปแบบ JSON สำหรับเมทาดาทาแบบกำหนดเอง (ไม่บังคับ)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "เลือกเทมเพลต \"{0}\" แล้ว - ดับเบิลคลิกเพื่อแทรก",
        "text_use_template": "ใช้บล็อกข้อความ",
        "text_type": "ประเภท",
        "text_search_templates": "ค้นหาบล็อกข้อความ...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 ข้อมูลการส่งออก / นำเข้า",
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

        <h3>📦 สิ่งที่ถูกส่งออก? (ภาพรวม)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">การตั้งค่าแอปพลิเคชันทั่วไป</span></li>
            <li class="detail">• โหมดมืด/สว่าง</li>
            <li class="detail">• การกลับสีโหมดมืดสำหรับรูปภาพ</li>
            <li class="detail">• ค่าเกณฑ์สีเทา</li>
            <li class="detail">• ภาษา</li>
            <li class="detail">• เรขาคณิตหน้าต่าง</li>
            <li class="detail">• โหมดซูม</li>
            <li class="detail">• การนำทาง (แถบนำทางแสดง)</li>
            <li class="detail">• เอาต์พุตเสียง (เปิด/ปิด)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">การตั้งค่าสำรองข้อมูล</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">การตั้งชื่อไฟล์ (ประทับเวลา, ตัวคั่น, คำต่อท้าย)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">การตั้งค่าสำหรับการแทรก</span></li>
            <li class="detail">• ลายเซ็น</li>
            <li class="detail">• ข้อความและบล็อกข้อความ</li>
            <li class="detail">• เครื่องหมาย, รูปภาพ และรูปร่าง</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">การตั้งค่า OCR</span></li>
            <li class="detail">• ภาษา</li>
            <li class="detail">• บังคับ OCR · โหมดหน้า</li>
            <li class="detail">• การประมวลผลภาพล่วงหน้า: แก้ไขความเอียง, ทำความสะอาด, การสุ่มตัวอย่างเกิน</li>
            <li class="detail">• จำนวนงานขนาน</li>
            <li class="detail">• โหมดการกลับสี</li>
            <li class="detail">• ค่าเกณฑ์สีเทา</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ที่คั่นหน้า</span></li>
            <li class="detail">• ที่คั่นหน้าทั้งหมดต่อไฟล์ PDF (หน้า, ชื่อ, เวลาสร้าง)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ฐานข้อมูลรหัสผ่าน</span></li>
            <li class="detail">• รหัสผ่าน PDF ที่บันทึกไว้ (เข้ารหัสหรือข้อความธรรมดาตามตัวเลือก)</li>
            <li class="detail">• แฮชรหัสผ่านหลัก (หากตั้งค่า)</li>
            <li class="detail">• ข้อมูลการยืนยัน</li>
        </ul>

        <h4>⚠️ หมายเหตุสำคัญ</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 เมื่อนำเข้า:</strong>
            <ul>
                <li><span class="warning">➜ การตั้งค่าปัจจุบันทั้งหมดจะถูกเขียนทับทั้งหมด</span></li>
                <li>• จำเป็นต้องรีสตาร์ทแอปพลิเคชัน</li>
                <li>• ลายเซ็น, บล็อกข้อความ และที่คั่นหน้าที่มีอยู่จะถูกแทนที่</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 รหัสผ่านหลักและโหมดการส่งออก:</strong>
            <ul>
                <li>• เมื่อรหัสผ่านหลักทำงาน คุณสามารถเลือก:</li>
                <li>  - <span style="color: #98FB98;"><strong>ถอดรหัสแล้ว</strong></span> (รหัสผ่านอยู่ในข้อความธรรมดาใน ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>เข้ารหัสแล้ว</strong></span> (อ่านได้เฉพาะกับรหัสผ่านหลักบนระบบเป้าหมาย)</li>
                <li>• แฮชรหัสผ่านหลักจะถูกเก็บ <strong>เป็น</strong> เข้ารหัสเสมอ</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ ประกาศด้านความปลอดภัย:</strong>
            <ul>
                <li>• ไฟล์ ZIP ที่ส่งออกมีข้อมูลที่ละเอียดอ่อน (<strong>รหัสผ่าน, ที่คั่นหน้า, ลายเซ็น</strong>)</li>
                <li>• กรุณาเก็บไว้ในที่ปลอดภัย (เช่น USB ที่เข้ารหัส, ตัวจัดการรหัสผ่าน)</li>
                <li>• หากไฟล์สูญหาย รหัสผ่าน PDF ที่บันทึกไว้จะสูญหายอย่างไม่มีทางกู้คืน</li>
            </ul>
        </div>

        <h4>📁 รูปแบบการส่งออก</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            การตั้งค่าจะถูกบันทึกในไฟล์ ZIP เดียว:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP นี้มี <code>settings.json</code> ที่สมบูรณ์ (จากการกำหนดค่าของคุณ) รวมถึงไฟล์ภาพลายเซ็นที่ฝังไว้และรหัสผ่านที่เข้ารหัส
        </p>

        </body>
        </html>""",

    # ======================================================
    # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
    # ======================================================
    'signature_guide_title': "ลายเซ็น - คู่มือ",
    'signature_guide_html': """
    📝 <strong>ลายเซ็น - คู่มือด่วน</strong><br>
    <ul>
    <li>ตั้งรหัสผ่านหลัก</li>
    <li>กำหนดค่าลายเซ็นในเมนู <em>การตั้งค่า</em> (ขนาด, ประทับเวลา, …)</li>
    <li>แทรกด้วย <strong>คลิกขวา</strong> ที่ตำแหน่งที่ต้องการ (ต้องใช้รหัสผ่านหลักหนึ่งครั้งต่อเซสชัน)</li>
    <li>ย้ายลายเซ็นด้วยเมาส์หรือปุ่มลูกศร</li>
    <li>แทรกลายเซ็นหลายรายการติดต่อกัน</li>
    <li>ปรับแต่งลายเซ็นแต่ละรายการแยกกัน</li>
    <li>ยกเลิกลายเซ็นเดียว</li>
    <li>บันทึก / ยกเลิกลายเซ็นทั้งหมดในครั้งเดียว</li>
    <li>อีกทางหนึ่ง สามารถใช้แถบเมนูได้เช่นกัน</li>
    </ul>
    """,
    'signature_guide_voice': "คู่มือด่วนสำหรับลายเซ็น ตั้งรหัสผ่านหลัก กำหนดค่าลายเซ็นในการตั้งค่า แทรกด้วยคลิกขวา",

    'image_guide_title': "แทรกรูปภาพ - คู่มือ",
    'image_guide_html': """
    📷 <strong>การแทรกรูปภาพใน PDF - คู่มือด่วน</strong><br>
    <ol>
    <li>คลิกขวาที่ตำแหน่งที่ต้องการ</li>
    <li><em>„แทรกรูปภาพ“</em> → เลือกรูปภาพ</li>
    <li>กำหนดตำแหน่งรูปภาพ: ลากด้วยเมาส์</li>
    <li>ปรับขนาด: ลากที่มุม/ขอบ</li>
    <li>รักษาอัตราส่วนภาพ: ปุ่ม <strong>[A]</strong></li>
    <li>การปรับแต่งเพิ่มเติม: คลิกขวาที่รูปภาพ</li>
    </ol>
    <p><strong>เคล็ดลับ:</strong> ในเมนูบริบท คุณสามารถปรับแต่งการตั้งค่าได้</p>
    """,
    'image_guide_voice': "คู่มือด่วนสำหรับรูปภาพ คลิกขวา แทรกรูปภาพ เลือก กำหนดตำแหน่งด้วยเมาส์ ปรับขนาดที่มุม อัตราส่วนภาพด้วยปุ่ม A",

    'form_guide_title': "แทรกรูปทรง - คู่มือ",
    'form_guide_html': """
    📐 <strong>การแทรกรูปทรงใน PDF - คู่มือด่วน</strong><br>
    <ol>
    <li>เลือกประเภทของรูปทรง (สี่เหลี่ยมผืนผ้า, วงรี, เส้น, ลูกศร)</li>
    <li>คลิกที่ตำแหน่ง:
        <ul>
        <li>สำหรับสี่เหลี่ยมผืนผ้า/วงรี: คลิกเดียววางรูปทรง</li>
        <li>สำหรับเส้น/ลูกศร: สองคลิกสำหรับจุดเริ่มต้นและจุดสิ้นสุด</li>
        </ul>
    </li>
    <li>กำหนดตำแหน่งรูปทรง: ลากด้วยเมาส์</li>
    <li>ปรับขนาด: ลากที่มุม/ขอบ</li>
    <li>บันทึกรูปทรง: <strong>Enter</strong></li>
    <li>ยกเลิกรูปทรง: <strong>ESC</strong></li>
    <li>การปรับแต่งเพิ่มเติม: คลิกขวาที่รูปทรง</li>
    </ol>
    <p><strong>เคล็ดลับ:</strong> ในเมนูบริบท คุณสามารถปรับแต่งการตั้งค่าได้</p>
    """,
    'form_guide_voice': "คู่มือด่วนสำหรับรูปทรง เลือกประเภทของรูปทรง สำหรับสี่เหลี่ยมผืนผ้าหรือวงรีคลิกครั้งเดียว สำหรับเส้นหรือลูกศรคลิกสองครั้ง กำหนดตำแหน่งด้วยเมาส์ ปรับขนาดที่มุม บันทึกด้วย Enter ยกเลิกด้วย Escape",

    # ============================================
    # 85. OCR TEXTFENSTER
    # ============================================
    "btn_prev_result": "ก่อนหน้า",
    "btn_next_result": "ถัดไป",
    "ocr_text_window": "หน้าต่างข้อความ OCR",
    "bookmark_existing": "บุ๊กมาร์กที่มีอยู่",

    # ============================================
    # 86. OCR Vergleich Mac Win
    # ============================================
    'ocr_method_mac_win_menu': "เปรียบเทียบ OCR Mac - Windows",
    'ocr_method_mac_win_title': "ความแตกต่างของ OCR ระหว่าง Mac และ Windows",
    'ocr_method_mac_win_voice': "Mac ดีกว่า",
    'ocr_method_mac_win_html': """
    <html>
    <head/>
    <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
    <p><strong>📄 OCR – ความแตกต่างระหว่าง macOS และ Windows</strong></p>

    <p><strong>macOS (แนะนำ)</strong></p>
    <p>เครื่องมือ:</p>
    <ul>
    <li>Tesseract + ocrmypdf</li>
    </ul>
    <p>ผลลัพธ์:</p>
    <ul>
    <li>PDF ที่ค้นหาได้พร้อมข้อความแบบฝัง ซึ่งยังคงเค้าโครงเดิมเป็นส่วนใหญ่</li>
    </ul>
    <p>ข้อดี:</p>
    <ul>
    <li>คุณภาพการรู้จำข้อความที่ยอดเยี่ยม (แม้ในหน้าที่เบี้ยว)</li>
    <li>การรักษากราฟิกเวกเตอร์และฟอนต์</li>
    <li>แถบความคืบหน้า GUI ผ่านการประเมินกระบวนการย่อย</li>
    <li>ควบคุมพารามิเตอร์ OCR ทั้งหมดได้อย่างเต็มที่ (Deskew, Clean, Oversample, การปรับให้เหมาะสม)</li>
    <li>การค้นหาข้อความสามารถใช้ได้โดยตรงในหน้าต่างหลัก (มุมมอง PDF)</li>
    </ul>
    <p>ข้อเสีย:</p>
    <ul>
    <li>ต้องการเครื่องมือระบบเพิ่มเติม (ocrmypdf, Ghostscript, unpaper, pngquant – รวมอยู่ในชุดแอป)</li>
    <li>การจัดการข้อผิดพลาดที่ซับซ้อนกว่า (deadlocks, timeouts)</li>
    </ul>

    <p><strong>Windows (ตัวเลือกที่เสถียร)</strong></p>
    <p>เครื่องมือ:</p>
    <ul>
    <li>pytesseract (การเชื่อมต่อโดยตรงกับ Tesseract) + reportlab + PyPDF2</li>
    </ul>
    <p>ผลลัพธ์:</p>
    <ul>
    <li>PDF ที่ค้นหาได้ซึ่งสายตาตรงกับ PDF รูปภาพ แต่สามารถค้นหาได้ผ่านข้อความโปร่งใส</li>
    </ul>
    <p>ข้อดี:</p>
    <ul>
    <li>ไม่มีอะไรที่นึกออกในขณะนี้</li>
    </ul>
    <p>ข้อเสีย:</p>
    <ul>
    <li>PDF คือภาพที่มีข้อความมองไม่เห็น เค้าโครงอาจเบี่ยงเบนเล็กน้อยสำหรับเอกสารที่ซับซ้อน (คอลัมน์, ตาราง)</li>
    <li>ไม่มีการแก้ไขความเอียงอัตโนมัติ (--deskew) หรือการทำความสะอาดภาพ (--clean)</li>
    <li>แถบความคืบหน้า GUI อัปเดตเพียงคร่าวๆ ตามจำนวนหน้าที่ประมวลผล</li>
    <li>ความเร็ว OCR ช้ากว่าเล็กน้อย (เนื่องจากแต่ละหน้าถูกประมวลผลแยกกัน)</li>
    <li>การค้นหาข้อความถูกเปลี่ยนเส้นทางไปยังหน้าต่างข้อความ OCR</li>
    </ul>

    <p><strong>ลักษณะร่วม</strong></p>
    <ul>
    <li>ทั้งสองวิธีสร้าง PDF ที่ค้นหาได้ในไดเรกทอรีเดียวกับไฟล์ต้นฉบับ</li>
    <li>การตั้งค่า OCR (ภาษา, DPI, โหมดการแบ่งส่วนหน้า, โหมดเครื่องมือ OCR) สามารถกำหนดค่าได้ผ่าน OCRSettingsDialog และมีผลในการใช้งานทั้งสองแบบ</li>
    </ul>

    <p><strong>คำแนะนำ:</strong></p>
    <ul>
    <li>macOS: ไบนารี ocrmypdf ให้ผลลัพธ์ที่ดีที่สุด – ซื้อ Mac และใช้เวอร์ชัน (PDFDarkView สำหรับ Mac ที่มีชิป Apple Silicon หรือ Intel) ผลลัพธ์ OCR ดีกว่าบน Windows!</li>
    <li>Windows: ใช้โซลูชัน pytesseract มีเสถียรภาพและให้คุณภาพที่เพียงพอสำหรับเอกสารส่วนใหญ่</li>
    </ul>

    <p><strong>หมายเหตุสำคัญ:</strong></p>
    <ul>
    <li>ทั้งสองเวอร์ชันรวมเข้ากับอินเทอร์เฟซผู้ใช้อย่างสมบูรณ์ – ผู้ใช้ไม่สังเกตเห็นความแตกต่าง</li>
    <li>โปรแกรมตัดสินใจโดยอัตโนมัติว่าจะใช้เครื่องมือ OCR ใดตามระบบปฏิบัติการ</li>
    </ul>
    </body>
    </html>
    """,

    # ============================================
    # 87. SIGNATUR ERSTELLEN (REMBG)
    # ============================================
    "signature_create_from_scan": "สร้างลายเซ็น (จากการสแกน)",
    "signature_create_title": "เลือกลายเซ็นที่สแกน (PDF/รูปภาพ)",
    "image_pdf_filter": "รูปภาพและ PDF",
    "signature_pdf_empty": "PDF ไม่มีหน้า",
    "signature_created_success": "สร้างลายเซ็นสำเร็จ: {0}",
    "signature_create_error": "ข้อผิดพลาดขณะสร้างลายเซ็น:\n{0}",
    "rembg_missing": "ไม่ได้ติดตั้ง rembg\nกรุณาติดตั้ง: pip install rembg\nข้อผิดพลาด: {0}",
    "signature_name_title": "ชื่อไฟล์สำหรับลายเซ็น",
    "signature_name_message": "กรุณาป้อนชื่อไฟล์สำหรับลายเซ็นใหม่ (จะถูกบันทึกเป็น PNG ที่มีพื้นหลังโปร่งใส):",
    "signature_name_label": "ชื่อไฟล์:",
    "signature_name_voice": "ป้อนชื่อไฟล์สำหรับลายเซ็น",
    "signature_processing": "กำลังประมวลผล...",
    "signature_creation_title": "กำลังสร้างลายเซ็น",
    "signature_overwrite_warning": "ไฟล์ '{0}' มีอยู่แล้ว จะเขียนทับหรือไม่?",
    # NEUE SIGNATUR ERSTELLEN
    "signature_prepare_title":"เตรียม PDF สำหรับลายเซ็น",
    "signature_prepare_instruction":"กรุณาเลือก PDF ที่มีลายเซ็นที่สแกนในหน้าเดียว\n\nเพื่อการรู้จำที่ดีที่สุด ตรวจสอบให้แน่ใจว่า:\n• ลายเซ็นเขียนด้วยหมึกดำ (ปากกาลูกลื่นหรือปากกาปลายแหลม) บนกระดาษขาว\n• ลายเซ็นอยู่ในส่วนบนหนึ่งในสามของหน้ากระดาษ A4 ที่เว้นว่างไว้\n• PDF ถูกสแกนด้วยความละเอียดอย่างน้อย 300 dpi\n• ลายเซ็นชัดเจนและไม่บางเกินไป\n• ไม่มีลวดลายพื้นหลังหรือเส้นที่รบกวน",
    "signature_prepare_voice":"กรุณาเลือก PDF ที่มีลายเซ็นที่สแกน ใส่ใจกับคุณภาพที่ดีและความคมชัด",
    "sig_thickness_label":"ความหนาของเส้น:",
    "sig_thickness_normal":"ปกติ (บาง)",
    "sig_thickness_bold":"หนา (แนะนำ)",
    "sig_thickness_very_bold":"หนามาก",

    # ============================================
    # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
    # ============================================
    'language_guide_menu': "เพิ่มภาษา GUI และ OCR - คู่มือ",
    'language_guide_title': "เพิ่มภาษา GUI และ OCR",
    'language_guide_detailed_html': """
    <html>
    <head/>
    <body>
    <h2>GUI</h2>
    <p>ดาวน์โหลดไฟล์คำแปลที่ต้องการ <code>translations_xy.py</code> จาก<br/>
    <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
    และวางไว้ในไดเรกทอรีต่อไปนี้:</p>
    <ul>
    <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
    <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
    <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
    </ul>

    <h2>OCR</h2>
    <ol>
    <li>เปิดเว็บเบราว์เซอร์ของคุณ</li>
    <li>ไปที่: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
    <li>ที่ขอบด้านขวาของหน้าจอ ค้นหา "Releases" และเลือกอันที่ทำเครื่องหมาย <strong>"latest"</strong></li>
    <li>ในหน้าเผยแพร่ถัดไป ดาวน์โหลดไฟล์ <code>Source Code.zip</code> ที่ด้านล่างสุด</li>
    <li>แตกไฟล์ ZIP</li>
    <li>ในโฟลเดอร์ที่แตกออกมา ให้ค้นหาไฟล์ภาษาทั้งหมดที่คุณต้องการ และคัดลอกไปยังไดเรกทอรี:<br/>
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
        "menu_watermark":"แทรกลายน้ำ",
        "fullpage_text_watermark_title":"ข้อความเป็นลายน้ำ",
        "fullpage_image_watermark_title":"รูปภาพเป็นลายน้ำ",
        "filename_with_watermark":"_พร้อมลายน้ำ",
        "watermark_text":"ข้อความ:",
        "watermark_text_placeholder":"ข้อความลายน้ำของคุณ...",
        "watermark_font_family":"แบบอักษร:",
        "watermark_font_size":"ขนาดแบบอักษร:",
        "watermark_format":"การจัดรูปแบบ:",
        "watermark_bold":"ตัวหนา",
        "watermark_italic":"ตัวเอียง",
        "watermark_color":"สี:",
        "watermark_choose_color":"เลือกสี...",
        "watermark_opacity":"ความทึบ / ความโปร่งใส:",
        "watermark_direction":"ทิศทางการอ่าน:",
        "watermark_direction_l_r":"ซ้าย → ขวา",
        "watermark_direction_bl_tr":"ล่างซ้าย → บนขวา",
        "watermark_direction_tl_br":"บนซ้าย → ล่าง",
        "watermark_direction_b_t":"ล่าง → บน",
        "watermark_direction_t_b":"บน → ล่าง",
        "watermark_preview":"ตัวอย่าง:",
        "watermark_preview_sample":"ข้อความตัวอย่าง",
        "watermark_empty_text":"กรุณาใส่ข้อความ",
        "watermark_applied":"ลายน้ำถูกนำไปใช้กับทุกหน้า",
        "watermark_saved":"บันทึกลายน้ำแล้ว",
        "image_scale":"ขนาด:",
        "image_preview":"ตัวอย่างรูปภาพ:",
        "no_image_selected":"ไม่ได้เลือกรูปภาพ",
        "browse":"เรียกดู...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "การปกปิดข้อมูล",
        "redact_add_black": "ปกปิดข้อมูล (สีดำ)",
        "redact_add_white": "ปกปิดข้อมูล (สีขาว / ลบ)",
        "redact_added_black": "เพิ่มการปกปิดข้อมูลสีดำแล้ว",
        "redact_added_white": "เพิ่มการปกปิดข้อมูลสีขาวแล้ว",
        "redact_apply_all": "ใช้การปกปิดข้อมูลทั้งหมดและบันทึก",
        "redact_discard_all": "ยกเลิกการปกปิดข้อมูลทั้งหมด",
        "redact_discard": "ยกเลิกการปกปิดข้อมูลนี้",
        "no_redactions": "ไม่มีการปกปิดข้อมูล",
        "redact_confirm_title": "ใช้การปกปิดข้อมูลอย่างถาวร",
        "redact_confirm_message": "คำเตือน: พื้นที่ที่ทำเครื่องหมายจะถูกลบอย่างถาวร (สีดำหรือสีขาว)\nจะสร้างข้อมูลสำรอง (หากเปิดใช้งาน)\n\nดำเนินการต่อ?",
        "redact_apply": "ใช่, ปกปิดข้อมูลตอนนี้",
        "redact_saved": "ใช้และบันทึกการปกปิดข้อมูล {0} รายการเรียบร้อยแล้ว",
        "redact_saved_voice": "ใช้การปกปิดข้อมูล {0} รายการ",
        "redact_error": "ข้อผิดพลาดระหว่างการปกปิดข้อมูล",
        "filename_redacted":"_ถูกปกปิด",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'แทรกหมายเลขหน้า',
        'page_numbers_format': 'รูปแบบหมายเลข:',
        'page_numbers_format_arabic': '1, 2, 3 ... (อาหรับ)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (โรมันตัวเล็ก)',
        'page_numbers_format_roman_upper': 'I, II, III ... (โรมันตัวใหญ่)',
        'page_numbers_format_letter': 'A, B, C ... (ตัวอักษร)',
        'page_numbers_format_custom': 'กำหนดเอง',
        'page_numbers_custom_pattern': 'รูปแบบ:',
        'page_numbers_custom_placeholder': 'เช่น "หน้า {nummer}" หรือ "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'ใช้ {nummer} สำหรับหมายเลขหน้าปัจจุบันและ {total} สำหรับจำนวนทั้งหมด',
        'page_numbers_position': 'ตำแหน่ง:',
        'page_numbers_pos_tl': 'บนซ้าย',
        'page_numbers_pos_tc': 'บนกลาง',
        'page_numbers_pos_tr': 'บนขวา',
        'page_numbers_pos_ml': 'กลางซ้าย',
        'page_numbers_pos_mc': 'กึ่งกลาง',
        'page_numbers_pos_mr': 'กลางขวา',
        'page_numbers_pos_bl': 'ล่างซ้าย',
        'page_numbers_pos_bc': 'ล่างกลาง',
        'page_numbers_pos_br': 'ล่างขวา',
        'page_numbers_margins': 'ขอบ:',
        'page_numbers_margin_x': 'ระยะแนวนอน:',
        'page_numbers_margin_y': 'ระยะแนวตั้ง:',
        'page_numbers_range': 'ช่วงหน้า:',
        'page_numbers_all_pages': 'ทุกหน้า',
        'page_numbers_custom_range': 'ช่วงที่กำหนดเอง',
        'page_numbers_from': 'จาก:',
        'page_numbers_to': 'ถึง:',
        'page_numbers_progress': 'กำลังแทรกหมายเลขหน้า...',
        'page_numbers_start': 'เริ่มแทรกหมายเลขหน้า...',
        'page_numbers_cancel': 'ยกเลิกการแทรกหมายเลขหน้า',
        'page_numbers_success': 'เพิ่มหมายเลขหน้าเรียบร้อยแล้ว\n\nคุณต้องการเปิด PDF ใหม่หรือไม่?\n\n{0}',
        'page_numbers_complete': 'เพิ่มหมายเลขหน้าแล้ว',
        'page_numbers_error_format': 'ข้อผิดพลาดขณะแทรกหมายเลขหน้า: {0}',
        'page_numbers_content_type': 'ประเภทเนื้อหา:',
        'page_numbers_tab_simple': 'หมายเลขธรรมดา',
        'page_numbers_tab_range': 'หน้า X จาก Y',
        'page_numbers_tab_date': 'วันที่',
        'page_numbers_tab_custom': 'ข้อความอิสระ',
        'page_numbers_range_format': 'รูปแบบ:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'หน้า {aktuell} จาก {gesamt}',
        'page_numbers_range_custom': 'กำหนดเอง',
        'page_numbers_range_placeholder': 'เช่น "หน้า {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'รูปแบบวันที่:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 มกราคม 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'กำหนดเอง',
        'page_numbers_date_placeholder': 'เช่น %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'ตำแหน่ง:',
        'page_numbers_date_before': 'วันที่ก่อนหมายเลขหน้า',
        'page_numbers_date_after': 'วันที่หลังหมายเลขหน้า',
        'page_numbers_date_only': 'เฉพาะวันที่ (ไม่มีหมายเลขหน้า)',
        'page_numbers_custom_text': 'ข้อความที่กำหนดเอง:',
        'page_numbers_custom_placeholder_text': 'ใช้ {seite} สำหรับหมายเลขหน้าและ {gesamt} สำหรับจำนวนทั้งหมด\nเช่น "ความลับ - หน้า {seite}" หรือ "{seite} จาก {gesamt}"',
        "filename_with_page_number":"_พร้อมหมายเลขหน้า",
        "filename_with_page_declaration":"_พร้อมคำประกาศหน้า",
        "filename_with_pagenumber":"_พร้อมหมายเลขหน้า",
        "filename_with_date":"_พร้อมวันที่",
        "filename_with_my_page_declaration":"_พร้อมคำประกาศหน้าที่กำหนดเอง",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "การเปลี่ยนแปลงที่ยังไม่ได้บันทึก",
        "unsaved_changes_message_darkmode": "มีการแทรกที่ยังไม่ได้บันทึก\nคุณต้องการบันทึกก่อนเปลี่ยนหรือไม่?",
        "save_and_switch": "บันทึกและเปลี่ยน",
        "discard_and_switch": "เปลี่ยนตอนนี้",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'ส่งออกหน้าเป็นรูปภาพ',
        'export_images_menu': 'ส่งออกเป็นรูปภาพ (PNG/JPEG)',
        'export_images_format': 'รูปแบบรูปภาพ:',
        'export_images_dpi': 'ความละเอียด (DPI):',
        'export_images_quality': 'คุณภาพ JPEG:',
        'export_images_range': 'ช่วงหน้า:',
        'export_images_all_pages': 'ทุกหน้า',
        'export_images_custom_range': 'ช่วงที่กำหนดเอง',
        'export_images_from': 'จาก:',
        'export_images_to': 'ถึง:',
        'export_images_options': 'ตัวเลือก:',
        'export_images_single_files': 'แต่ละหน้าเป็นไฟล์แยก',
        'export_images_subfolder': 'ส่งออกไปยังโฟลเดอร์ย่อย',
        'export_images_subfolder_info': 'ไปยังโฟลเดอร์ย่อย "ชื่อPDF_รูปภาพ"',
        'export_images_same_folder': 'ในโฟลเดอร์เดียวกับ PDF',
        'export_images_apply_darkmode': 'ใช้การตั้งค่า PDFDarkView (โหมดมืด)',
        'export_images_target_folder': 'โฟลเดอร์ปลายทาง:',
        'export_images_browse': 'เรียกดู...',
        'export_images_preview': 'ตัวอย่าง:',
        'export_images_preview_info': 'เลือกการตั้งค่าสำหรับการส่งออก',
        'export_images_preview_info_detail': '{0} หน้าเป็น {1}\nความละเอียด: {2} DPI\nชื่อไฟล์: {3}\n{4}',
        'export_images_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'export_images_start': 'เริ่มส่งออกรูปภาพ...',
        'export_images_progress': 'กำลังส่งออกรูปภาพ...',
        'export_images_saving': 'กำลังบันทึกหน้า {0} จาก {1}...',
        'export_images_success': 'การส่งออกสำเร็จ!\n\nบันทึกรูปภาพ {0} รายการใน:\n{1}',
        'export_images_complete': 'การส่งออกรูปภาพเสร็จสิ้น',
        'export_images_open_folder': '📁 เปิดโฟลเดอร์',
        'export_images_cancel': 'ยกเลิกการส่งออกรูปภาพ',
        'export_images_error_format': 'ข้อผิดพลาดขณะส่งออกรูปภาพ: {0}',
        'export_images_pdf2image_missing': 'ไลบรารี "pdf2image" ไม่ได้ติดตั้ง\n\nกรุณาติดตั้งด้วย:\npip install pdf2image\n\nสำหรับ Windows คุณต้องมี Poppler ด้วย:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'การแปลง PDF/A สำหรับการเก็บถาวรระยะยาว',
        'pdfa_menu': 'การแปลง PDF/A (เหมาะสำหรับการเก็บถาวร)',
        'pdfa_info': 'แปลง PDF เป็นรูปแบบ PDF/A\n\nPDF/A ได้รับการออกแบบมาโดยเฉพาะสำหรับการเก็บถาวรระยะยาวและรับประกันว่าเอกสารจะแสดงอย่างถูกต้องในอนาคต',
        'pdfa_standard': 'มาตรฐาน PDF/A:',
        'pdfa_standard_select': 'เวอร์ชัน:',
        'pdfa_1': 'PDF/A-1 (ง่าย, เข้ากันได้กว้าง)',
        'pdfa_2': 'PDF/A-2 (ทันสมัย, การบีบอัดดีกว่า)',
        'pdfa_3': 'PDF/A-3 (เวอร์ชันล่าสุด, อนุญาตไฟล์แนบ)',
        'pdfa_standards_explanation': '📖 คำอธิบายมาตรฐาน:\n\n'
            '• PDF/A-1: พื้นฐาน, เข้ากันได้กับระบบเก่า (ประมาณ 2005)\n'
            '• PDF/A-2: ทันสมัยกว่า, การบีบอัดดีกว่า, รองรับความโปร่งใส (ประมาณ 2011)\n'
            '• PDF/A-3: เวอร์ชันล่าสุด, อนุญาตให้ฝังไฟล์แนบ (ประมาณ 2013)\n\n'
            'คำแนะนำ: PDF/A-2 เป็นการประนีประนอมที่ดีระหว่างความเข้ากันได้และฟังก์ชันที่ทันสมัย',
        'pdfa_options': 'ตัวเลือก:',
        'pdfa_compress_enable': 'บีบอัด PDF (ไฟล์เล็กลง)',
        'pdfa_metadata_preserve': 'รักษาเมทาดาทา (ชื่อเรื่อง, ผู้แต่ง, ฯลฯ)',
        'pdfa_target_folder': 'โฟลเดอร์ปลายทาง:',
        'pdfa_browse': 'เรียกดู...',
        'pdfa_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'pdfa_ocr_info_unknown': '🔍 ไม่สามารถตรวจสอบเนื้อหาข้อความได้',
        'pdfa_ocr_info_not_needed': '✅ มีข้อความ - ไม่จำเป็นต้องใช้ OCR\nสามารถสร้าง PDF/A ได้โดยตรง',
        'pdfa_ocr_info_recommended': '⚠️ ไม่พบข้อความเพียงพอ\n\nสำหรับ PDF ที่ค้นหาได้ เราขอแนะนำให้เรียกใช้ OCR ก่อน\nหมายเหตุ: PDF/A ทำงานได้โดยไม่มี OCR - แต่ข้อความจะไม่สามารถค้นหาได้',
        'pdfa_ocr_info_error': '❌ ข้อผิดพลาดขณะตรวจสอบ: {0}',
        'pdfa_start': 'เริ่มการแปลง PDF/A...',
        'pdfa_progress': 'กำลังแปลง PDF/A...',
        'pdfa_success': 'การแปลง PDF/A สำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nคุณต้องการเปิด PDF ใหม่หรือไม่?',
        'pdfa_complete': 'การแปลง PDF/A เสร็จสิ้น',
        'pdfa_cancel': 'ยกเลิกการแปลง PDF/A',
        'pdfa_error_format': 'ข้อผิดพลาดขณะแปลง PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'ไลบรารี "ocrmypdf" ไม่ได้ติดตั้ง\n\nกรุณาติดตั้งด้วย:\npip install ocrmypdf',
        'btn_convert': 'แปลง',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'ปรับแต่ง PDF (ลดขนาดไฟล์)',
        'optimize_menu': 'ปรับแต่ง PDF (ขนาดไฟล์)',
        'optimize_info': 'ลดขนาดไฟล์ PDF ด้วยวิธีการปรับแต่งต่างๆ\n\nยิ่งระดับการบีบอัดสูงขึ้น ไฟล์ก็จะเล็กลง - โดยอาจสูญเสียคุณภาพของรูปภาพ',
        'optimize_level': 'ระดับการบีบอัด:',
        'optimize_level_low': 'ต่ำ (เร็ว, ประหยัดน้อย)',
        'optimize_level_medium': 'ปานกลาง (การประนีประนอมที่ดี)',
        'optimize_level_high': 'สูง (ประหยัดมาก)',
        'optimize_level_maximum': 'สูงสุด (ประหยัดสูงสุด, ช้า)',
        'optimize_level_explanation': 'คำแนะนำ: "ปานกลาง" เป็นการประนีประนอมที่ดีระหว่างความเร็วและขนาดไฟล์',
        'optimize_options': 'ตัวเลือก:',
        'optimize_compress_images': 'บีบอัดรูปภาพ (ลดคุณภาพ JPEG)',
        'optimize_clean_objects': 'ลบวัตถุที่ไม่ได้ใช้',
        'optimize_preserve_metadata': 'รักษาเมทาดาทา (ชื่อเรื่อง, ผู้แต่ง, ฯลฯ)',
        'optimize_image_quality': 'คุณภาพรูปภาพ:',
        'optimize_range': 'ช่วงหน้า:',
        'optimize_all_pages': 'ทุกหน้า',
        'optimize_custom_range': 'ช่วงที่กำหนดเอง',
        'optimize_from': 'จาก:',
        'optimize_to': 'ถึง:',
        'optimize_target_folder': 'โฟลเดอร์ปลายทาง:',
        'optimize_browse': 'เรียกดู...',
        'optimize_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'optimize_info_box': 'ข้อมูล',
        'optimize_info_text': 'การปรับแต่งอาจใช้เวลาหลายนาทีสำหรับ PDF ขนาดใหญ่\n\nรูปภาพจะถูกบันทึกด้วยคุณภาพที่ลดลง ซึ่งสามารถลดขนาดไฟล์ได้อย่างมาก',
        'optimize_start': 'เริ่มปรับแต่ง PDF...',
        'optimize_progress': 'กำลังปรับแต่ง PDF...',
        'optimize_cancel': 'ยกเลิกการปรับแต่ง PDF',
        'optimize_complete': 'การปรับแต่ง PDF เสร็จสิ้น',
        'optimize_error_format': 'ข้อผิดพลาดขณะปรับแต่ง PDF:\n\n{0}',
        'optimize_success_message': 'การปรับแต่ง PDF สำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nก่อน: {1}\nหลัง: {2}\nประหยัด: {3:.1f}%\n\n{4}\n\nคุณต้องการเปิด PDF ที่ปรับแต่งแล้วหรือไม่?',
        'optimize_success_message_no_size': 'การปรับแต่ง PDF สำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nไม่มีข้อมูลขนาด\n\nคุณต้องการเปิด PDF ที่ปรับแต่งแล้วหรือไม่?',
        'optimize_result_positive': 'ไฟล์ลดลง {0:.1f}%',
        'optimize_result_zero': 'ไม่มีการเปลี่ยนแปลงขนาดไฟล์',
        'optimize_result_negative': 'ไฟล์เพิ่มขึ้น {0:.1f}%\nข้ามการปรับแต่ง, เก็บไฟล์ต้นฉบับไว้',
        'btn_optimize': 'เริ่มปรับแต่ง',
        'filename_optimize_low_suffix': '_ปรับแต่ง_ต่ำ',
        'filename_optimize_medium_suffix': '_ปรับแต่ง',
        'filename_optimize_high_suffix': '_ปรับแต่ง_สูง',
        'filename_optimize_maximum_suffix': '_ปรับแต่ง_สูงสุด',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'ครอบตัด PDF',
        'crop_menu': 'ครอบตัด PDF (Crop)',
        'crop_range': 'ใช้กับ:',
        'crop_all_pages': 'ทุกหน้า',
        'crop_current_page': 'เฉพาะหน้าปัจจุบัน',
        'crop_values': 'ค่าครอบตัด (เป็นจุด):',
        'crop_left': 'ซ้าย:',
        'crop_right': 'ขวา:',
        'crop_top': 'บน:',
        'crop_bottom': 'ล่าง:',
        'crop_presets': 'ค่าที่ตั้งไว้ล่วงหน้า:',
        'crop_preset_white': 'ตรวจจับขอบสีขาว',
        'crop_reset': 'รีเซ็ต',
        'crop_mouse_hint': '🖱️ ลากสี่เหลี่ยมเพื่อเลือกพื้นที่คร่าวๆ\nจากนั้นคุณสามารถปรับค่าใน SpinBox ได้อย่างแม่นยำ\nไม่สามารถปรับด้วยเมาส์ด้วยตนเองได้',
        'crop_apply': 'ครอบตัด',
        'crop_scope_all': 'ทุกหน้า',
        'crop_scope_current': 'หน้าปัจจุบัน',
        'crop_new_size': 'ขนาดใหม่: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'ไม่มี PDF ที่โหลด',
        'crop_preview_error': 'ข้อผิดพลาดขณะโหลดตัวอย่าง',
        'crop_start': 'เริ่มครอบตัด...',
        'crop_progress': 'กำลังครอบตัด PDF...',
        'crop_success': 'ครอบตัด PDF สำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nคุณต้องการเปิด PDF ที่ครอบตัดแล้วหรือไม่?',
        'crop_complete': 'การครอบตัดเสร็จสิ้น',
        'crop_cancel': 'ยกเลิกการครอบตัด',
        'crop_error_format': 'ข้อผิดพลาดขณะครอบตัด:\n\n{0}',
        'filename_crop_suffix': '_ถูกครอบตัด',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'ปรับ PDF ให้เรียบ (Flatten)',
        'flatten_menu': 'ปรับ PDF ให้เรียบ (Flatten)',
        'flatten_info': 'การปรับ PDF ให้เรียบจะ "เผา" องค์ประกอบที่แก้ไขได้ทั้งหมดลงในเนื้อหาของหน้า\n\nหลังจากนั้น ช่องฟอร์ม, คำอธิบายประกอบ, ข้อความ, กากบาท, ลายเซ็น, รูปภาพ และรูปร่างจะไม่สามารถแก้ไขแยกกันได้อีกต่อไป',
        'flatten_explanation_title': '📖 ใช้ทำอะไร?',
        'flatten_explanation_text': 'การปรับให้เรียบจำเป็นในสถานการณ์ต่อไปนี้:\n\n'
            '• 📄 คุณต้องการเตรียมเอกสารสำหรับการพิมพ์\n'
            '• 🔒 คุณต้องการป้องกันไม่ให้ใครเปลี่ยนแปลงช่องฟอร์ม\n'
            '• 📎 คุณต้องการ "ฝัง" คำอธิบายประกอบและความคิดเห็นอย่างถาวรในเอกสาร\n'
            '• 🖼️ คุณต้องการยึดข้อความ, กากบาท, ลายเซ็น, รูปภาพ และรูปร่างที่แทรกไว้ในเอกสารอย่างถาวร\n'
            '• 📦 คุณต้องการเตรียมไฟล์สำหรับการเก็บถาวร\n\n'
            'การปรับให้เรียบทำให้ PDF เล็กลงและป้องกันการเคลื่อนย้ายหรือลบองค์ประกอบโดยไม่ได้ตั้งใจ',
        'flatten_what_title': 'อะไรถูกปรับให้เรียบ?',
        'flatten_what_list': '• ✅ ช่องฟอร์ม (ช่องข้อความ, ช่องทำเครื่องหมาย, ปุ่ม)\n'
            '• ✅ คำอธิบายประกอบ (ความคิดเห็น, การไฮไลต์, โน้ต)\n'
            '• ✅ การซ้อนทับ (ข้อความ, กากบาท, ลายเซ็น, รูปภาพ, รูปร่าง)',
        'flatten_options': 'ตัวเลือก:',
        'flatten_forms': 'ปรับช่องฟอร์มให้เรียบ',
        'flatten_annotations': 'ปรับคำอธิบายประกอบให้เรียบ',
        'flatten_overlays': 'ปรับการซ้อนทับให้เรียบ (ข้อความ, กากบาท, ลายเซ็น, รูปภาพ, รูปร่าง)',
        'flatten_target_folder': 'โฟลเดอร์ปลายทาง:',
        'flatten_browse': 'เรียกดู...',
        'flatten_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'flatten_warning': '⚠️ สำคัญ: การปรับให้เรียบเป็นกระบวนการที่ไม่สามารถย้อนกลับได้!\n\nหลังจากปรับให้เรียบแล้ว องค์ประกอบที่แก้ไขได้จะไม่สามารถเปลี่ยนแปลงหรือลบแยกกันได้อีกต่อไป\nสร้างข้อมูลสำรองล่วงหน้าหากจำเป็น',
        'flatten_apply': 'ปรับให้เรียบ',
        'flatten_start': 'เริ่มปรับให้เรียบ...',
        'flatten_progress': 'กำลังปรับ PDF ให้เรียบ...',
        'flatten_success': 'ปรับ PDF ให้เรียบสำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nคุณต้องการเปิด PDF ที่ปรับให้เรียบแล้วหรือไม่?',
        'flatten_complete': 'การปรับให้เรียบเสร็จสิ้น',
        'flatten_cancel': 'ยกเลิกการปรับให้เรียบ',
        'flatten_error_format': 'ข้อผิดพลาดขณะปรับให้เรียบ:\n\n{0}',
        'filename_flatten_suffix': '_ถูกปรับให้เรียบ',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'การซ้อนทับ PDF (Overlay)',
        'overlay_menu': 'การซ้อนทับ PDF (Overlay)',
        'overlay_info': 'วาง PDF หนึ่ง (การซ้อนทับ) ทับ PDF อีกหนึ่ง\n\nPDF ที่ซ้อนทับจะถูกวางบน PDF พื้นฐาน มีประโยชน์สำหรับลายน้ำ, โลโก้, หัวจดหมาย หรือตราประทับ',
        'overlay_explanation_title': '📖 ใช้ทำอะไร?',
        'overlay_explanation_text': 'การซ้อนทับจำเป็นในสถานการณ์ต่อไปนี้:\n\n'
            '• 🏢 วางโลโก้บริษัทเป็นลายน้ำบนทุกหน้า\n'
            '• 📄 วางหัวจดหมายบน PDF ว่าง\n'
            '• 🖊️ วางการซ้อนทับตราประทับบนเอกสาร\n'
            '• 🔖 วางลายน้ำบนทุกหน้า\n'
            '• 📑 วางการซ้อนทับฟอร์มบนเทมเพลต',
        'overlay_type': 'ประเภทการซ้อนทับ:',
        'overlay_type_fullpage': 'เต็มหน้า (ครอบคลุม)',
        'overlay_type_transparent': 'เต็มหน้า (โปร่งใส - แนะนำ)',
        'overlay_type_stamp': 'ตราประทับ (สามารถปรับตำแหน่งได้)',
        'overlay_type_info_fullpage': '📄 PDF ที่ซ้อนทับจะถูกวางอย่างแม่นยำเหนือทั้งหน้า\nสามารถลบพื้นหลังสีขาวออกเพื่อให้เห็นเฉพาะเนื้อหา',
        'overlay_type_info_transparent': '🔍 PDF ที่ซ้อนทับจะถูกวางเหนือทั้งหน้าด้วยพื้นหลังโปร่งใส\nพื้นหลังสีขาวจะถูกลบโดยอัตโนมัติ - เหมาะสำหรับลายน้ำและโลโก้!',
        'overlay_type_info_stamp': '🖊️ PDF ที่ซ้อนทับจะถูกวางตำแหน่งและปรับขนาดเป็นตราประทับ\nเหมาะสำหรับโลโก้, ตราประทับ หรือลายเซ็นในตำแหน่งที่กำหนด',
        'overlay_remove_background': 'ลบพื้นหลังสีขาว:',
        'overlay_remove_background_enable': 'ลบพื้นหลังสีขาวจาก PDF ที่ซ้อนทับ (ทำให้การซ้อนทับโปร่งใส)',
        'overlay_remove_background_tooltip': 'ลบพื้นที่สีขาวจาก PDF ที่ซ้อนทับเพื่อให้ข้อความด้านล่างปรากฏ',
        'overlay_threshold': 'ค่าเกณฑ์:',
        'overlay_threshold_hint': '(1-254, สูงกว่า = ลบสีขาวมากขึ้น)',
        'overlay_select_file': 'เลือก PDF ที่ซ้อนทับ:',
        'overlay_file_placeholder': 'กรุณาเลือกไฟล์ PDF สำหรับการซ้อนทับ',
        'overlay_browse': 'เรียกดู...',
        'overlay_select_overlay': 'เลือก PDF ที่ซ้อนทับ',
        'overlay_range': 'ช่วงหน้า:',
        'overlay_all_pages': 'ทุกหน้า',
        'overlay_custom_range': 'ช่วงที่กำหนดเอง',
        'overlay_from': 'จาก:',
        'overlay_to': 'ถึง:',
        'overlay_position': 'ตำแหน่ง:',
        'overlay_position_center': 'กึ่งกลาง',
        'overlay_position_top_left': 'บนซ้าย',
        'overlay_position_top_right': 'บนขวา',
        'overlay_position_bottom_left': 'ล่างซ้าย',
        'overlay_position_bottom_right': 'ล่างขวา',
        'overlay_size': 'ขนาด:',
        'overlay_size_original': 'ขนาดต้นฉบับ',
        'overlay_size_fit_page': 'ปรับให้พอดีกับหน้า',
        'overlay_size_custom': 'กำหนดเอง (%)',
        'overlay_opacity': 'ความโปร่งใส:',
        'overlay_target_folder': 'โฟลเดอร์ปลายทาง:',
        'overlay_browse_folder': 'เรียกดู...',
        'overlay_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'overlay_warning': '⚠️ หมายเหตุ: PDF ที่ซ้อนทับจะถูกวางบน PDF พื้นฐานและ "เผา" ลงในนั้น\n\nองค์ประกอบของ PDF ที่ซ้อนทับจะไม่สามารถแก้ไขแยกกันได้หลังจากบันทึก',
        'overlay_apply': 'ซ้อนทับ',
        'overlay_start': 'เริ่มการซ้อนทับ...',
        'overlay_progress': 'กำลังซ้อนทับ PDF...',
        'overlay_success': 'ซ้อนทับ PDF สำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nคุณต้องการเปิด PDF ที่ซ้อนทับแล้วหรือไม่?',
        'overlay_complete': 'การซ้อนทับเสร็จสิ้น',
        'overlay_cancel': 'ยกเลิกการซ้อนทับ',
        'overlay_error_format': 'ข้อผิดพลาดขณะซ้อนทับ:\n\n{0}',
        'overlay_no_file': 'ไม่ได้เลือก PDF ที่ซ้อนทับ\n\nกรุณาเลือกไฟล์ PDF สำหรับการซ้อนทับ',
        'filename_overlay_suffix': '_ถูกซ้อนทับ',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'แยกรูปภาพจาก PDF',
        'extract_images_menu': 'แยกรูปภาพทั้งหมด',
        'extract_images_info': 'แยกรูปภาพทั้งหมดจาก PDF และบันทึกเป็นไฟล์แยกกัน\n\nรูปภาพจะถูกบันทึกในรูปแบบต้นฉบับหรือแปลงเป็นรูปแบบที่เลือก',
        'extract_images_format': 'รูปแบบรูปภาพ:',
        'extract_images_quality': 'คุณภาพ JPEG:',
        'extract_images_options': 'ตัวเลือก:',
        'extract_images_subfolder': 'แยกไปยังโฟลเดอร์ย่อย ("ชื่อPDF_รูปภาพ")',
        'extract_images_unique': 'เฉพาะรูปภาพที่ไม่ซ้ำกัน (หลีกเลี่ยงการซ้ำ)',
        'extract_images_range': 'ช่วงหน้า:',
        'extract_images_all_pages': 'ทุกหน้า',
        'extract_images_custom_range': 'ช่วงที่กำหนดเอง',
        'extract_images_from': 'จาก:',
        'extract_images_to': 'ถึง:',
        'extract_images_target_folder': 'โฟลเดอร์ปลายทาง:',
        'extract_images_browse': 'เรียกดู...',
        'extract_images_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'extract_images_info_box': 'ข้อมูล',
        'extract_images_info_text': 'การแยกอาจใช้เวลาหลายนาทีสำหรับ PDF ขนาดใหญ่\n\nรูปภาพจะถูกบันทึกด้วยชื่อต้นฉบับ (หน้า_รูปภาพ)',
        'extract_images_extract': 'แยก',
        'extract_images_start': 'เริ่มการแยก...',
        'extract_images_progress': 'กำลังแยกรูปภาพ...',
        'extract_images_success': '✅ แยกรูปภาพสำเร็จ!\n\nบันทึกรูปภาพ {0} รายการใน:\n{1}',
        'extract_images_complete': 'การแยกรูปภาพเสร็จสิ้น',
        'extract_images_cancel': 'ยกเลิกการแยก',
        'extract_images_error_format': 'ข้อผิดพลาดขณะแยกรูปภาพ:\n\n{0}',
        'extract_images_open_folder': '📁 เปิดโฟลเดอร์',
        'extract_images_no_images': 'ไม่พบรูปภาพใน PDF',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'หลายหน้าบนหน้าเดียว (N-Up)',
        'nup_menu': 'หลายหน้าบนหน้าเดียว (N-Up)',
        'nup_info': 'จัดเรียงหลายหน้า PDF บนหน้าเดียว\n\nเหมาะสำหรับการพิมพ์แบบกะทัดรัด, ภาพรวม หรือเอกสารแจก',
        'nup_layout': 'เลย์เอาต์:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'ตัวอย่าง:',
        'nup_preview_info': '{0} หน้า → {1} หน้าต่อแผ่น → {2} แผ่น\nเลย์เอาต์: {3}',
        'nup_order': 'ลำดับ:',
        'nup_order_horizontal': 'แนวนอน (ทีละแถว)',
        'nup_order_vertical': 'แนวตั้ง (ทีละคอลัมน์)',
        'nup_order_horizontal_reverse': 'แนวนอนย้อนกลับ',
        'nup_order_vertical_reverse': 'แนวตั้งย้อนกลับ',
        'nup_range': 'ช่วงหน้า:',
        'nup_all_pages': 'ทุกหน้า',
        'nup_custom_range': 'ช่วงที่กำหนดเอง',
        'nup_from': 'จาก:',
        'nup_to': 'ถึง:',
        'nup_options': 'ตัวเลือก:',
        'nup_margins': 'ขอบ:',
        'nup_margin_between': 'ระยะห่างระหว่างหน้า:',
        'nup_page_numbers': 'แทรกหมายเลขหน้า',
        'nup_target_folder': 'โฟลเดอร์ปลายทาง:',
        'nup_browse': 'เรียกดู...',
        'nup_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'nup_create': 'สร้าง',
        'nup_start': 'เริ่ม N-Up...',
        'nup_progress': 'กำลังสร้าง N-Up...',
        'nup_success': 'สร้าง N-Up สำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nคุณต้องการเปิด PDF ใหม่หรือไม่?',
        'nup_complete': 'N-Up เสร็จสิ้น',
        'nup_cancel': 'ยกเลิก N-Up',
        'nup_error_format': 'ข้อผิดพลาดขณะ N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'เปลี่ยนขนาดหน้า',
        'pagesize_menu': 'เปลี่ยนขนาดหน้า',
        'pagesize_info': 'เปลี่ยนขนาดหน้าของ PDF\n\nเนื้อหาจะถูกปรับให้เข้ากับขนาดใหม่โดยอัตโนมัติ',
        'pagesize_format': 'รูปแบบ:',
        'pagesize_select': 'เลือกรูปแบบมาตรฐาน:',
        'pagesize_custom': 'ขนาดที่กำหนดเอง:',
        'pagesize_width': 'ความกว้าง:',
        'pagesize_height': 'ความสูง:',
        'pagesize_orientation': 'การวางแนว:',
        'pagesize_portrait': 'แนวตั้ง',
        'pagesize_landscape': 'แนวนอน',
        'pagesize_scale_options': 'ตัวเลือกการปรับขนาด:',
        'pagesize_fit': 'ปรับพอดี (รักษาอัตราส่วน)',
        'pagesize_stretch': 'ยืด (บิดเบือน)',
        'pagesize_center': 'กึ่งกลาง (ขนาดต้นฉบับ)',
        'pagesize_range': 'ช่วงหน้า:',
        'pagesize_all_pages': 'ทุกหน้า',
        'pagesize_custom_range': 'ช่วงที่กำหนดเอง',
        'pagesize_from': 'จาก:',
        'pagesize_to': 'ถึง:',
        'pagesize_target_folder': 'โฟลเดอร์ปลายทาง:',
        'pagesize_browse': 'เรียกดู...',
        'pagesize_select_folder': 'เลือกโฟลเดอร์ปลายทาง',
        'pagesize_apply': 'ใช้',
        'pagesize_start': 'เริ่มเปลี่ยนขนาดหน้า...',
        'pagesize_progress': 'กำลังเปลี่ยนขนาดหน้า...',
        'pagesize_success': 'เปลี่ยนขนาดหน้าสำเร็จ!\n\nบันทึกเป็น:\n{0}\n\nคุณต้องการเปิด PDF ใหม่หรือไม่?',
        'pagesize_complete': 'การเปลี่ยนขนาดหน้าเสร็จสิ้น',
        'pagesize_cancel': 'ยกเลิกการเปลี่ยนขนาดหน้า',
        'pagesize_error_format': 'ข้อผิดพลาดขณะเปลี่ยนขนาดหน้า:\n\n{0}',
        'pagesize_preview_info': 'ขนาดใหม่: {0} x {1} pt',
        'filename_pagesize_suffix': '_ขนาดใหม่',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'ข้อมูล PDF',
        'pdf_info_menu': 'แสดงข้อมูล PDF',
        'pdf_info_voice': 'กำลังแสดงข้อมูล PDF',
        'pdf_info_error': 'ข้อผิดพลาดขณะแสดงข้อมูล PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "แสดงทางลัดแป้นพิมพ์",
        "shortcuts_dialog_title": "ทางลัดแป้นพิมพ์",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 ไฟล์</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>เปิด PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>ปิด PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>บันทึกเป็น...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>ป้องกันเอกสาร</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>พิมพ์</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>พิมพ์ทันที (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>ออกจากแอปพลิเคชัน</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 ส่งออก</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>ส่งออกเป็น Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>ส่งออกเป็น DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>ส่งออกเป็น TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>ส่งออกเป็นรูปภาพ (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>แยกรูปภาพ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ การประมวลผลเอกสาร</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (หลายหน้า)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>การแปลง PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>ปรับ PDF ให้เรียบ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>ซ้อนทับ PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>ปรับแต่ง PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ แก้ไข</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>ค้นหา</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>เพิ่มบุ๊กมาร์ก</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>จัดการบุ๊กมาร์ก</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>บุ๊กมาร์กถัดไป</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>บุ๊กมาร์กก่อนหน้า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>เรียกใช้ OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 การจัดการหน้า</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>หมุนหน้าปัจจุบัน</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>หมุนทุกหน้า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>ปรับหน้าปัจจุบันให้เป็นปกติ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>ปรับทุกหน้าให้เป็นปกติ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ลบหน้า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>แยกหน้า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>แทรกหน้า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>ย้ายหน้า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>รวม PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>เปลี่ยนขนาดหน้า</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 แทรก</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>แทรกข้อความ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>แทรกกากบาท</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>แทรกลายเซ็น 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>แทรกลายเซ็น 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>แทรกรูปภาพ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>แทรกรูปสี่เหลี่ยม</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>แทรกรูปวงรี</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>แทรกเส้น</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>แทรกลูกศร</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>แทรกหมายเลขหน้า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ลายน้ำข้อความ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>ลายน้ำรูปภาพ</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ การปกปิดข้อมูล</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ปกปิดข้อมูล (สีดำ)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>ปกปิดข้อมูล (สีขาว)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>ใช้การปกปิดข้อมูลทั้งหมด</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ขั้นสูง</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>ครอบตัด PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>แก้ไขเมทาดาทา</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ มุมมอง</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>สลับโหมดมืด/สว่าง</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>แสดงหน้าต่างข้อความ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>ความกว้างหน้า (ซูม)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>สองหน้า (ซูม)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>ภาพรวม (ซูม)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ การตั้งค่า</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>การจัดการรหัสผ่าน</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>การตั้งค่า OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>การตั้งค่าลายเซ็น</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>การจัดรูปแบบชื่อไฟล์</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>ส่งออกการตั้งค่า</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>นำเข้าการตั้งค่า</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ ข้อมูล</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>แสดงข้อมูล PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>เปิด/ปิดเสียงอ่าน</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>โฟกัสที่แถบเมนู</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "มีเวอร์ชันใหม่",
        "update_available_message": "มีเวอร์ชันใหม่ <b>{0}</b>\n\nไปที่หน้าเผยแพร่เพื่อดาวน์โหลดอัปเดต:\n{1}",
        "update_available_voice": "มีเวอร์ชันใหม่ {0} โปรดดาวน์โหลดอัปเดตจากหน้า GitHub",
        "update_open_release": "เปิดหน้าเผยแพร่",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "ดาวน์โหลดคำแปลทั้งหมด",
        "ask_download_all_translations": """นอกเหนือจากภาษาเยอรมัน อังกฤษ และเวียดนามแล้ว ยังมีภาษา GUI อื่นๆ อีก {total_languages} ภาษา\n\nควรจัดเตรียม / อัปเดตหรือไม่?\n\nหมายเหตุ:\nภาษาที่ไม่จำเป็นคุณสามารถลบด้วยตนเองในภายหลังในไดเรกทอรี:\n{translations_path}
        \nหากคุณยกเลิก คุณสามารถดาวน์โหลดภาษา GUI ในภายหลังผ่านเมนู 'เครื่องมือ → อัปเดตคำแปล'""",
        "menu_update_translations": "อัปเดตคำแปล",
        "translations_updated": "อัปเดตคำแปลแล้ว",
        "translations_update_success": "อัปเดตคำแปล {} รายการสำเร็จ ({} ใหม่, {} อัปเดต)",
        "translations_update_error": "ข้อผิดพลาดในการอัปเดตคำแปล",
        "translations_update_no_changes": "คำแปลทั้งหมดเป็นปัจจุบันอยู่แล้ว",
        "translations_update_offline": "ไม่มีการเชื่อมต่ออินเทอร์เน็ต ไม่สามารถอัปเดตคำแปลได้",
        "translations_update_in_progress": "กำลังอัปเดตคำแปลในพื้นหลัง...",
        "translations_downloading": "กำลังดาวน์โหลดคำแปล...",
        "translations_path_hint": "ไดเรกทอรีผู้ใช้สำหรับคำแปล",
        "translations_update_not_available_title": "ไม่มีการอัปเดต",
        "translations_update_not_available_message": """การอัปเดตคำแปลมีเฉพาะในเวอร์ชันที่ติดตั้งเท่านั้น\n\nในโหมดพัฒนา คำแปลเป็นปัจจุบันอยู่แล้ว""",
        "translations_update_no_internet_title": "ไม่มีการเชื่อมต่ออินเทอร์เน็ต",
        "translations_update_no_internet_message": """ไม่สามารถสร้างการเชื่อมต่ออินเทอร์เน็ตได้\n\nไม่สามารถดาวน์โหลดคำแปลจาก GitHub ได้\n\nวิธีแก้ไขที่เป็นไปได้:
        • ตรวจสอบการเชื่อมต่ออินเทอร์เน็ตของคุณ
        • ปิดไฟร์วอลล์ชั่วคราว
        • ลองอีกครั้งในภายหลัง
        \nคุณยังสามารถดาวน์โหลดคำแปลด้วยตนเองจาก GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "กำลังอัปเดตอยู่แล้ว",
        "btn_retry": "ลองอีกครั้ง",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "ยินดีต้อนรับสู่ PDF Dark View",
        "welcome_title_not_supported": "ยินดีต้อนรับสู่ PDF Dark View",
        "welcome_message": "ยินดีต้อนรับสู่ PDF Dark View!\n\nภาษาระบบของคุณถูกตรวจพบว่าเป็น '{language}'\nคุณต้องการใช้ภาษานี้สำหรับส่วนติดต่อผู้ใช้หรือไม่?\n\nคุณสามารถเปลี่ยนภาษาได้ตลอดเวลาผ่าน 'การตั้งค่า → ภาษา'",
        "welcome_message_language_not_available": "ยินดีต้อนรับสู่ PDF Dark View!\n\nภาษาระบบของคุณถูกตรวจพบว่าเป็น '{language}'\nภาษานี้ยังไม่ได้ติดตั้ง\n\nคุณต้องการดาวน์โหลดคำแปลสำหรับ {language} ตอนนี้จาก GitHub หรือไม่?\n\n(ภาษาจะถูกใช้โดยอัตโนมัติสำหรับส่วนติดต่อผู้ใช้)",
        "welcome_message_language_not_supported": "ยินดีต้อนรับสู่ PDF Dark View!\n\nภาษาระบบของคุณถูกตรวจพบว่าเป็น '{language}'\nขออภัย ยังไม่มีคำแปลสำหรับภาษานี้\n\nส่วนติดต่อผู้ใช้จะแสดงเป็น {fallback_language}\n\nคุณสามารถเปลี่ยนภาษาได้ตลอดเวลาผ่าน 'การตั้งค่า → ภาษา'\nหากต้องการ คุณสามารถร่วมให้คำแปลสำหรับภาษาของคุณได้:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "ใช่ ใช้ภาษาระบบ",
        "welcome_keep_english": "ไม่ เก็บภาษาอังกฤษไว้",
        "welcome_download_language": "ใช่ ดาวน์โหลด {language}",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "กำลังปิดโปรแกรม",

    }

