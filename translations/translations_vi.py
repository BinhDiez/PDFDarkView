
# ============================================
# translations_vi.py - Từ điển Tiếng Việt
# Sắp xếp đầy đủ theo danh mục
# Bình luận bằng tiếng Đức để nhất quán
# ============================================

def load_vietnamese_strings():
    """Tải tất cả các chuỗi tiếng Việt"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View của BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Mở PDF",
        'btn_text_window': "Văn bản OCR",
        'btn_first': "Trang đầu",
        'btn_prev': "Trang trước",
        'btn_next': "Trang sau",
        'btn_last': "Trang cuối",
        'btn_print': "In",
        'btn_darkmode_light': "Chế độ sáng",
        'btn_darkmode_dark': "Chế độ tối",
        'btn_delete_pages': "Xóa trang",
        'btn_extract_pages': "Trích xuất trang",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Hủy",
        'btn_save': "Lưu",
        'btn_close': "Đóng",
        'btn_delete': "Xóa",
        'btn_delete_all': "Xóa tất cả",
        'btn_copy': "Sao chép",
        'btn_export': "Xuất",
        'btn_show': "Hiện mật khẩu",
        'btn_hide': "Ẩn mật khẩu",
        'btn_authenticate': "Xác thực",
        'btn_settings': "Cài đặt",
        'btn_protect': "Bảo vệ",
        'btn_remove_password': "Xóa mật khẩu",
        'btn_manage': "Quản lý mật khẩu",
        'btn_retry': "Thử lại",
        'btn_select_all': "Chọn tất cả",
        'btn_clear_selection': "Bỏ chọn",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Trang {0} trên {1}",
        'page_count': "trên {0}",
        'goto_page': "Đi tới trang",
        'page_simple': "Trang {0}",
        'full_view_page': "Xem toàn trang {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Nhập từ khóa + Enter",
        'search_results': "Kết quả: {0} trên {1}",
        'search_nav_hint': "Enter: kết quả tiếp (Shift+Enter: trước đó)",
        'search_no_results': "Không có kết quả",
        'search_error': "Lỗi tìm kiếm",
        'search_active': "Trường tìm kiếm được kích hoạt",
        'search_closed': "Đã đóng tìm kiếm",
        'search_position': "Trang {0} {1}",
        'search_pos_top': "rất trên",
        'search_pos_upper': "trên",
        'search_pos_middle': "giữa",
        'search_pos_lower': "dưới",
        'search_pos_bottom': "rất dưới",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Nhận dạng văn bản hoàn tất thành công!",
        'ocr_success_title': "OCR thành công",
        'ocr_success_message': "Tài liệu hiện có thể tìm kiếm được.",
        'ocr_failed': "OCR thất bại",
        'ocr_in_progress': "OCR đang tiến hành",
        'ocr_preparing': "Đang chuẩn bị PDF...",
        'ocr_analyzing': "Đang phân tích PDF...",
        'ocr_optimizing': "Đang tối ưu hình ảnh...",
        'ocr_recognizing': "Đang nhận dạng văn bản...",
        'ocr_embedding': "Đang nhúng văn bản...",
        'ocr_finalizing': "Đang hoàn thiện PDF...",
        'ocr_not_available': "OCR không khả dụng",
        'ocr_install_message': "Không tìm thấy công cụ OCR.\n\nVui lòng cài đặt:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Yêu cầu OCR",
        'ocr_question': "PDF không chứa văn bản có thể tìm kiếm.\nBạn có muốn chạy OCR để cho phép {0}?",
        'ocr_perform': "Chạy OCR",
        'ocr_later': "Để sau",
        'ocr_starting': "Đang bắt đầu OCR đảm bảo...",
        'ocr_success_voice': "OCR thành công. PDF hiện có thể tìm kiếm.",
        'ocr_partial_success': "OCR đã được thực hiện, nhưng có vấn đề khi thay thế.\n\nPhiên bản có thể tìm kiếm đã được lưu tại:\n{0}\n\nLỗi: {1}",
        'ocr_partial_title': "OCR thành công một phần",
        'ocr_partial_voice': "Đã thực hiện OCR, nhưng thay thế thất bại.",
        'original_file': "Tệp gốc:",
        'old_size': "Kích thước cũ:    {0} byte",
        'new_size': "Kích thước mới: {0} byte",
        'size_change': "Thay đổi: {0}{1} byte",
        'backup_created_file': "Đã tạo bản sao lưu:\n{0}",
        'backup_not_created': "Sao lưu: Không tạo (tắt cài đặt)",
        'page_header': "=== Trang {0} ===\n{1}\n",
        'scanned_page_header': "=== Trang {0} (đã quét) ===\n[Trang này chỉ chứa văn bản quét]\n[Vui lòng chạy OCR thủ công]\n",
        'scanned_warning': "⚠️ VĂN BẢN QUÉT - YÊU CẦU OCR",
        'guaranteed_title': "Đã tạo PDF có thể tìm kiếm",
        'guaranteed_message': "<b>Đã tạo phiên bản có thể tìm kiếm đảm bảo!</b>\n\nVì OCR tự động thất bại, một PDF thay thế có thể tìm kiếm đã được tạo:\n\n{0}\n\n<b>Tệp này chứa:</b>\n• Văn bản được trích xuất (nếu có)\n• Gợi ý cho các trang quét\n• Có thể tìm kiếm đầy đủ",
        'guaranteed_voice': "Đã tạo PDF có thể tìm kiếm đảm bảo.",
        'instruction_title': "HƯỚNG DẪN OCR",
        'instruction_file': "Tệp gốc: {0}",
        'instruction_text': "Nhận dạng văn bản tự động (OCR) đã thất bại.\nVui lòng thực hiện OCR thủ công:\n\n1. VỚI OCRmyPDF (dòng lệnh):\n   ocrmypdf --force-ocr \"[TÊP]\" \"dau-ra.pdf\"\n\n2. VỚI ADOBE ACROBAT (macOS/Windows):\n   • Mở PDF trong Acrobat\n   • Công cụ > Chỉnh sửa PDF\n   • Chọn 'Nhận dạng văn bản'\n\n3. VỚI PREVIEW (macOS):\n   • Mở PDF trong Preview\n   • Tệp > Xuất...\n   • Bộ lọc Quartz: 'Reduce File Size'\n   • Bật 'Thực hiện OCR'\n\n4. DỊCH VỤ OCR TRỰC TUYẾN:\n   • smallpdf.com/ocr-pdf\n   • ilovepdf.com/ocr-pdf\n   • adobe.com/acrobat/online/pdf-to-word.html",
        'instruction_created': "Đã tạo hướng dẫn OCR",
        'instruction_created_message': "Một hướng dẫn chi tiết đã được tạo:\n\n{0}\n\nVui lòng làm theo các bước cho OCR thủ công.",
        'instruction_created_voice': "Đã tạo hướng dẫn OCR.",
        'ocr_impossible': "Không thể OCR",
        'ocr_impossible_message': "Không thể thực hiện OCR.\n\nVui lòng xử lý '{0}' thủ công bằng phần mềm OCR.",
        'ocr_impossible_voice': "Không thể OCR. Vui lòng xử lý thủ công.",
        'emergency_title': "OCR khẩn cấp",
        'emergency_message': "Một PDF khẩn cấp đã được tạo:\n\n{0}\n\nVui lòng xử lý tệp này thủ công bằng OCR.",
        'emergency_voice': "Đã tạo PDF khẩn cấp. Vui lòng chạy OCR thủ công.",
        'critical_error': "Lỗi nghiêm trọng",
        'critical_error_message': "Không thể bắt đầu OCR.\n\nVui lòng khởi động lại chương trình và\nkiểm tra cài đặt OCR.",
        'critical_error_voice': "Lỗi OCR nghiêm trọng",
        'ocr_question_html': "<p>PDF không chứa văn bản có thể tìm kiếm.<p>Bạn có muốn chạy OCR để cho phép <b>{0}</b>?</p>",
        'ocr_question_voice': "Yêu cầu OCR. PDF không chứa văn bản có thể tìm kiếm. Bạn có muốn chạy OCR để cho phép {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "chưa mở PDF",
        'no_pdf_message': "Chưa có PDF nào được mở",
        'pdf_not_found': "Không tìm thấy tệp PDF",
        'file_size': "Kích thước tệp",
        'bytes': "byte",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Đã tạo bản sao lưu",
        'backup_disabled': "Tắt sao lưu",
        'backup_activated': "Đã bật tạo bản sao lưu",
        'backup_deactivated': "Đã tắt tạo bản sao lưu",
        'backup_status': "Sao lưu: {0}",
        'backup_on': "✔ bật",
        'backup_off': "✘ tắt",
        'close_pdf': "Đang đóng PDF: {0}",
        'pdf_not_found_format': "Không tìm thấy tệp PDF: {0}",
        'error_pdf_load_format': "Lỗi khi tải PDF: {0}",
        'load_failed_format': "Tải thất bại:\n{0}",
        'decrypted_suffix': "(đã giải mã)",
        'decryption_failed': "Giải mã thất bại.",
        'decryption_error': "Lỗi khi giải mã",
        'decryption_success': "Giải mã thành công",
        'decryption_success_message': "PDF đã được giải mã và lưu tại:\n\n{0}",
        'decryption_success_voice': "PDF đã được giải mã và lưu.",
        'password_remove_error': "Lỗi khi xóa mật khẩu",
        'save_unencrypted': "Lưu PDF không mã hóa dưới dạng",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Lưu dưới dạng...",
        'save_copy': "Lưu bản sao",
        'save_success': "PDF đã lưu tại: {0}",
        'save_encrypted': "PDF được bảo vệ đã lưu tại: {0}",
        'save_error': "Không thể lưu PDF",
        'encryption_question': "Bạn có muốn bảo vệ PDF bằng mật khẩu?",
        'encryption_yes': "Có",
        'encryption_no': "Không",
        'encryption_cancel': "Hủy",
        'save_cancel': "Đã hủy lưu",
        'save_encrypted_voice': "Tệp đã được mã hóa và lưu.",
        'save_success_voice': "Tệp PDF đã được lưu không mã hóa.",
        'save_error_format': "Không thể lưu PDF:\n{0}",
        'export_pages_success': "Xuất Pages thành công",
        'export_pages_error': "Xuất Pages thất bại",
        'export_pages_error_format': "Xuất Pages thất bại: {0}",
        'export_word_success': "Xuất Word thành công",
        'export_word_error': "Xuất Word thất bại",
        'export_word_error_format': "Xuất Word thất bại: {0}",
        'export_text_success': "Xuất văn bản thành công",
        'export_text_error': "Xuất văn bản thất bại",
        'export_text_error_format': "Xuất văn bản thất bại: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Yêu cầu mật khẩu",
        'password_enter': "Vui lòng nhập mật khẩu",
        'password_confirm': "Xác nhận mật khẩu",
        'password_new': "Mật khẩu mới",
        'password_current': "Mật khẩu hiện tại",
        'password_save': "Lưu mật khẩu (đã mã hóa)",
        'password_saved': "✓ Mật khẩu cho tệp này đã được lưu",
        'password_wrong': "Sai mật khẩu",
        'password_mismatch': "Mật khẩu không khớp",
        'password_too_short': "Mật khẩu quá ngắn",
        'password_min_length': "Mật khẩu phải có ít nhất 4 ký tự",
        'password_strength': "Độ mạnh mật khẩu",
        'password_strength_very_weak': "Rất yếu",
        'password_strength_weak': "Yếu",
        'password_strength_medium': "Trung bình",
        'password_strength_strong': "Mạnh",
        'password_strength_very_strong': "Rất mạnh",
        'password_char_count': "({0} ký tự)",
        'password_match': "✓ Khớp",
        'password_no_match': "✗ Mật khẩu không khớp",
        'password_show': "Hiện",
        'password_hide': "Ẩn",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Quản lý mật khẩu",
        'password_table_filename': "Tên tệp",
        'password_table_password': "Mật khẩu",
        'password_count': "{0} mật khẩu đã lưu{1}",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "Không có mật khẩu nào được lưu",
        'password_copied': "Đã sao chép {0} mật khẩu{1}",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "Bạn có thực sự muốn xóa mật khẩu cho '{0}'?",
        'password_delete_multiple': "Bạn có thực sự muốn xóa {0} mật khẩu đã chọn?",
        'password_delete_all_confirm': "Bạn có thực sự muốn xóa tất cả {0} mật khẩu đã lưu?",
        'password_deleted': "Đã xóa {0} mật khẩu{1}",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "Đã xóa tất cả mật khẩu",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Trình tạo mật khẩu",
        'generator_generated': "Mật khẩu đã tạo:",
        'generator_regenerate': "Tạo lại",
        'generator_copy': "Sao chép",
        'generator_use': "Sử dụng",
        'generator_settings': "Cài đặt",
        'generator_length': "Độ dài:",
        'generator_group_every': "Dấu phân cách mỗi",
        'generator_group_chars': "ký tự.   Dấu phân cách:",
        'generator_uppercase': "Chữ hoa (A-Z)",
        'generator_lowercase': "Chữ thường (a-z)",
        'generator_digits': "Số (0-9)",
        'generator_symbols': "Ký tự đặc biệt (!@#$%^&*)",
        'generator_exclude': "Loại trừ:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Yêu cầu mật khẩu chính",
        'master_password_setup': "Thiết lập mật khẩu chính",
        'master_password_change': "Thay đổi mật khẩu chính",
        'master_password_enter': "Vui lòng nhập mật khẩu chính của bạn",
        'master_password_choose': "Chọn mật khẩu chính mạnh (ít nhất 8 ký tự)",
        'master_password_new': "Vui lòng nhập mật khẩu chính mới",
        'master_password_confirm': "Xác nhận mật khẩu",
        'master_password_authenticate': "Xác thực",
        'master_password_success': "Đã thiết lập mật khẩu chính thành công.",
        'master_password_changed': "Đã thay đổi mật khẩu chính thành công.",
        'master_password_removed': "Đã xóa mật khẩu chính và tất cả mật khẩu.",
        'master_password_remove': "Xóa mật khẩu chính",
        'master_password_remove_confirm': "Bạn có CHẮC CHẮN muốn xóa TẤT CẢ mật khẩu?\n\nHành động này KHÔNG THỂ ĐẢO NGƯỢC!",
        'master_password_export_before': "Bạn có muốn xuất bản sao lưu trước không?",
        'master_password_export_delete': "Xuất & xóa",
        'master_password_delete_now': "Xóa ngay",
        'master_password_for_signatures': "Để sử dụng chữ ký, bạn phải thiết lập mật khẩu chính.\n\nBạn có muốn thiết lập mật khẩu chính ngay bây giờ?",
        'master_password_for_private': "Để sử dụng mẫu văn bản riêng tư, bạn phải thiết lập mật khẩu chính.\n\nBạn có muốn thiết lập mật khẩu chính ngay bây giờ?",
        'master_password_info': """
            <b>🔐 KHÔNG CÓ MẬT KHẨU CHÍNH:</b><br>
            • Không thể xem, sao chép và xuất mật khẩu<br>
            • Xóa mật khẩu luôn có thể thực hiện (ngay cả khi không có mật khẩu chính)<br><br>

            <b>🔐 CÓ MẬT KHẨU CHÍNH:</b><br>
            • Tất cả chức năng khả dụng sau khi xác thực<br>
            • Mật khẩu được mã hóa bằng mật khẩu chính<br>
            • Độ dài tối thiểu: 8 ký tự<br>
            • Lưu trữ băm SHA-256 an toàn<br><br>

            <b>QUAN TRỌNG:</b><br>
            • Nếu mất mật khẩu chính: không thể khôi phục mật khẩu<br>
            • Khi xóa mật khẩu chính: TẤT CẢ mật khẩu sẽ bị xóa<br>
            • Có tùy chọn xuất trước khi xóa<br>
            • Có thể thay đổi mật khẩu chính bất kỳ lúc nào
        """,
        'signature_auth_disabled': "Tắt yêu cầu mật khẩu cho chữ ký",
        'template_auth_disabled': "Tắt yêu cầu mật khẩu cho mẫu văn bản riêng tư",
        'master_password_for_signatures_settings': "Để sử dụng chữ ký, bạn phải thiết lập mật khẩu chính.\n\nVào Cài đặt - Quản lý mật khẩu để thực hiện",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Bảo vệ PDF",
        'protect_info': "Tệp '{0}' sẽ được bảo vệ bằng mật khẩu.",
        'protect_instruction': "Vui lòng nhập mật khẩu mong muốn hai lần để bảo vệ tài liệu, hoặc sử dụng trình tạo mật khẩu ở bên phải trường nhập.",
        'protect_success': "PDF đã được bảo vệ thành công và lưu tại:\n{0}\n\nMật khẩu: {1}\n\nBạn có muốn mở PDF được bảo vệ ngay bây giờ?",
        'protect_open': "Có",
        'protect_skip': "Không",
        'protect_error': "Lỗi khi bảo vệ PDF",
        'protect_open_title': "mở PDF đã bảo vệ",
        'protect_question': "Hoàn tất. Bạn có muốn mở PDF đã bảo vệ ngay bây giờ? Có hay Không?",
        'password_cancel': "Đã hủy hộp thoại mật khẩu",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Xóa trang",
        'pages_extract': "Trích xuất trang",
        'pages_insert': "Chèn trang",
        'pages_move': "Di chuyển trang",
        'pages_delete_options': "Tùy chọn xóa",
        'pages_delete_empty': "Xóa tất cả trang trống",
        'pages_delete_current': "Xóa trang hiện tại",
        'pages_delete_range': "Xóa khoảng trang",
        'pages_extract_options': "Tùy chọn trích xuất",
        'pages_extract_current': "Trích xuất trang hiện tại",
        'pages_extract_range': "Trích xuất khoảng trang",
        'pages_insert_position': "Vị trí chèn",
        'pages_insert_before': "Chèn trước trang:",
        'pages_insert_select': "Chọn PDF",
        'pages_insert_none': "Chưa chọn PDF",
        'pages_move_source': "Các trang cần di chuyển",
        'pages_move_from': "Từ trang:",
        'pages_move_to': "Đến trang:",
        'pages_move_target': "Vị trí đích",
        'pages_move_before': "Di chuyển trước trang:",
        'pages_move_hint': "Lưu ý: trang 1 = đầu, {0} = cuối",
        'pages_range_invalid': "Trang bắt đầu phải nhỏ hơn hoặc bằng trang kết thúc.",
        'pages_position_invalid': "Vị trí đích không được nằm trong khoảng cần di chuyển.",
        'pages_no_pdf_selected': "Chưa chọn PDF nào.",
        'pages_deleted': "Đã xóa {0} trang.",
        'pages_extracted': "Đã trích xuất: {0}\nĐã lưu tại: {1}\nKích thước tệp: {2:.1f} KB",
        'pages_inserted': "Đã chèn {0} trang",
        'pages_moved': "Đã di chuyển {0} trang.",
        'pages_deleted_none': "Không có trang nào bị xóa.",
        'pages_delete_progress': "Đang xóa trang...",
        'pages_deleted_with_backup': "Đã xóa {0} trang.\n\nSao lưu: {1}",
        'pages_deleted_voice': "Đã tạo bản sao lưu và xóa {0} trang.",
        'info': "Thông tin",
        'error_dialog_creation': "Không thể tạo hộp thoại",
        'extract_page_single': "Trích xuất trang {0}",
        'extract_page_range': "Trích xuất các trang {0}-{1}",
        'extract_success_voice': "Đã trích xuất trang thành công",
        'extract_error_format': "Lỗi khi trích xuất: {0}",
        'pages_inserted_voice': "Đã chèn {0} trang.",
        'insert_error_format': "Lỗi khi chèn: {0}",
        'pages_move_progress': "Đang di chuyển trang...",
        'pages_moved_with_backup': "Đã di chuyển {0} trang.\n\nSao lưu: {1}",
        'move_success_title': "Di chuyển thành công",
        'pages_moved_voice': "Đã di chuyển thành công {0} trang",
        'mark_removed': "Đã xóa đánh dấu khỏi trang {0}",
        'mark_empty': "Trang {0} được đánh dấu là trống",
        'mark_export_removed': "Đã xóa đánh dấu xuất khỏi trang {0}",
        'mark_export': "Trang {0} được đánh dấu để xuất",
        'no_empty_pages': "Không có trang trống nào được đánh dấu để xóa",
        'delete_empty_confirm': "Bạn có muốn xóa tất cả {0} trang trống đã đánh dấu?",
        'delete_empty_confirm_voice': "Xóa tất cả {0} trang trống đã đánh dấu ngay bây giờ? Có hoặc Không.",
        'empty_pages_deleted': "Đã xóa {0} trang trống",
        'no_export_pages': "Không có trang nào được đánh dấu để xuất",
        'overwrite_title': "Ghi đè tệp hiện có",
        'overwrite_question': "Tệp\n\n{0}\n\nđã tồn tại.\nBạn có muốn ghi đè không?",
        'overwrite_voice': "Ghi đè tệp hiện có? Có hoặc Không.",
        'page_skipped': "Đã bỏ qua trang {0}",
        'export_complete': "Đã hoàn tất xuất.",
        'export_complete_voice': "Việc xuất đã hoàn tất.",
        'no_pages_exported': "Không có trang nào được xuất",
        'export_cancelled': "Đã hủy xuất",
        'pages_exported': "Đã xuất {0} trang đến {1}",
        'export_page_title': "Xuất trang",
        'page_exported': "Đã xuất trang {0} đến {1}",
        'export_error': "Lỗi khi xuất",
        'export_marked_title': "Xuất các trang đã đánh dấu",
        'rotate_all_title': "xoay tất cả trang",
        'rotate_all_question': "Bạn có muốn xoay tất cả trang 90 độ sang phải?",
        'rotate_all_voice': "Bạn có muốn xoay tất cả trang 90 độ sang phải? Có hay Không?",
        'all_pages_rotated': "Đã xoay tất cả trang",
        'page_rotated': "Đã xoay trang {0}",
        'rotate_error': "Không thể xoay trang",
        'delete_page_confirm': "Bạn có muốn xóa trang {0}?",
        'delete_page_confirm_voice': "Bạn có thực sự muốn xóa trang {0}? Có hoặc Không.",
        'page_deleted': "Đã xóa trang {0}",
        'delete_error': "Không thể xóa trang",
        'pages_deleted_voice': "Đã xóa {0} trang",
        'pages_exported_split': "Đã xuất thành công {0} trang.",
        'pages_skipped': "Đã bỏ qua {0} trang.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Trích xuất trang (nâng cao)",
        'pdf_splitter_title': "PDF Splitter & Extractor",
        'pdf_splitter_load': " Chọn tệp PDF",
        'pdf_splitter_info': "Vui lòng chọn một tùy chọn cho tài liệu PDF của bạn",
        'pdf_splitter_basic': "Thao tác cơ bản",
        'pdf_splitter_single': "Chia thành từng trang riêng lẻ",
        'pdf_splitter_range': "Trích xuất trang:",
        'pdf_splitter_range_placeholder': "ví dụ: 1-3,5,7-9",
        'pdf_splitter_clean': "Thao tác dọn dẹp",
        'pdf_splitter_remove_empty': "Xóa tất cả trang trống",
        'pdf_splitter_remove': "Xóa khoảng trang:",
        'pdf_splitter_remove_placeholder': "ví dụ: 2,4-6",
        'pdf_splitter_process': "Xử lý PDF",
        'pdf_splitter_loaded': "Đã tải PDF. Vui lòng chọn một tùy chọn",
        'pdf_read_error': "Không thể đọc PDF",
        'pages': "Trang",
        'pages_created': "Đã tạo trang",
        'range_empty': "Vui lòng nhập khoảng trang",
        'range_invalid': "Khoảng trang không hợp lệ",
        'range_created': "Đã tạo PDF mới với các trang đã chọn:\n{0}",
        'empty_removed': "Đã xóa {0} trang trống.\nĐầu ra: {1}",
        'remove_empty': "Vui lòng nhập các trang cần xóa",
        'remove_invalid': "Các trang cần xóa không hợp lệ",
        'remove_done': "Đã tạo PDF đã dọn dẹp:\n{0}",
        'open_folder': "Mở thư mục",
        'show_in_finder': "Hiển thị trong Finder",
        'pdf_splitter_no_pdf': "Vui lòng tải tệp PDF trước.",
        'process_error': "Lỗi khi xử lý PDF",
        'pages_created_voice': "Đã tạo {0} trang",
        'range_created_voice': "Đã tạo PDF với các trang đã chọn",
        'empty_removed_voice': "Đã xóa {0} trang trống",
        'remove_done_voice': "Đã tạo PDF đã dọn dẹp",
        'pdf_splitter_split_groups': "Mỗi nhóm liên tiếp vào tệp riêng",
        'range_created_single': "Đã tạo PDF mới:\n{0}",
        'range_created_multiple': "Đã tạo {0} tệp PDF.",
        'range_created_voice_single': "Đã tạo một PDF với các trang đã chọn",
        'range_created_voice_multiple': "Đã tạo {0} tệp PDF",
        'empty_removed_none_left': "Không còn trang nào",
        'empty_removed_all_empty': "Tất cả trang được nhận dạng là trống và sẽ bị xóa. Không có tệp nào được tạo.",
        'preview_single': "Xem trước: {0}",
        'preview_enter_range': "Vui lòng nhập khoảng trang.",
        'preview_invalid_range': "Khoảng trang không hợp lệ.",
        'preview_file': "Xem trước: {0}",
        'preview_files': "Xem trước: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Đang bắt đầu in",
        'print_sent': "Đã gửi lệnh in",
        'print_now': "In ngay",
        'print_error': "Lỗi khi in trực tiếp",
        'print_limited': "Chức năng in bị hạn chế trên hệ thống này",
        'print_error_format': "Lỗi khi in trực tiếp: {0}",
        'warning': "Lưu ý",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Chuyển sang Chế độ sáng",
        'mode_switch_to_dark': "Chuyển sang Chế độ tối",
        'mode_dark_activated': "Đã kích hoạt Chế độ tối",
        'mode_light_activated': "Đã kích hoạt Chế độ sáng",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Xem toàn trang",
        'zoom_two_pages': "Hai trang cạnh nhau",
        'zoom_overview': "Chế độ tổng quan",
        'zoom_cannot_during_search': "Không thể phóng to trong khi tìm kiếm",
        'zoom_exit_first': "Vui lòng thoát phóng to trước",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Đã bật Kéo & Thả",
        'drag_disabled': "Đã tắt Kéo & Thả",
        'drag_page_grab': "Đang kéo trang {0}",
        'drag_page_dropped': "Đã chèn trang {0} vào vị trí {1}",
        'drag_position_invalid': "Vị trí không hợp lệ",
        'drag_same_position': "Trang {0} vẫn ở vị trí {0}",
        'drag_error': "Lỗi khi di chuyển",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Nhập văn bản với định dạng nâng cao và quản lý mẫu",
        'text_templates': "Mẫu văn bản có sẵn:",
        'text_name': "Tên",
        'text_preview': "Xem trước văn bản",
        'text_enter': "Văn bản:",
        'text_font_size': "Cỡ chữ:",
        'text_formatting': "Định dạng:",
        'text_bold': "Đậm",
        'text_italic': "Nghiêng",
        'text_underline': "Gạch chân",
        'text_alignment': "Căn chỉnh:",
        'text_left': "Trái",
        'text_center': "Giữa",
        'text_right': "Phải",
        'text_color': "Màu chữ:",
        'text_opacity': "Độ mờ:",
        'text_word_wrap': "Ngắt dòng:",
        'text_auto': "Tự động",
        'text_page_width_95': "Chiều rộng trang (95%)",
        'text_page_width_85': "Rất rộng (85%)",
        'text_page_width_75': "Rộng hơn (75%)",
        'text_page_width_60': "Rộng (60%)",
        'text_page_width_50': "Trung bình (50%)",
        'text_page_width_30': "Hẹp (30%)",
        'text_page_width_20': "Hẹp hơn (20%)",
        'text_page_width_10': "Rất hẹp (10%)",
        'text_no_wrap': "Không ngắt dòng",
        'text_private': "Mẫu văn bản riêng tư (yêu cầu xác thực)",
        'text_preview_label': "Xem trước:",
        'text_preview_placeholder': "Bản xem trước của văn bản sẽ được hiển thị ở đây...",
        'text_no_text': "(Không có văn bản)",
        'text_save_template': "💾 Lưu làm mẫu",
        'text_delete_template': "🗑 Xóa mẫu văn bản đã chọn",
        'text_show_private': "Hiện riêng tư",
        'text_hide_private': "Ẩn riêng tư",
        'text_use': "✅ Sử dụng văn bản",
        'text_saved': "Đã lưu mẫu văn bản dưới dạng:\n{0}",
        'text_saved_voice': "Đã lưu mẫu văn bản",
        'text_deleted': "Đã xóa mẫu văn bản",
        'text_no_text_to_save': "Không có văn bản để lưu.",
        'text_no_templates': "Không tìm thấy mẫu văn bản nào",
        'text_private_master_required': "Mẫu riêng tư chỉ có thể được sử dụng nếu mật khẩu chính được thiết lập.\n\nBạn có muốn thiết lập mật khẩu chính ngay bây giờ?",
        'text_filename': "Tên tệp cho mẫu văn bản (không có 'Text_' và '.txt'):",
        'text_filename_hint': "Ví dụ: 'DienThoai VanPhong' sẽ được lưu dưới dạng 'Text_DienThoai VanPhong.txt'",
        'text_save_hint': "Mẫu văn bản sẽ tự động được lưu với định dạng.",
        'text_guide_title': "Nhập văn bản - Hướng dẫn",
        'text_delete_confirm': "Bạn có thực sự muốn xóa mẫu văn bản?\n\nTệp: {0}\nVăn bản: {1}...",
        'text_make_public': "Đánh dấu là công khai",
        'text_make_private': "Đánh dấu là riêng tư",
        'text_privacy_changed': "Đã thay đổi trạng thái riêng tư",
        'text_private_always': "Riêng tư luôn hiển thị (cài đặt)",
        'text_mode_required': "Vui lòng kích hoạt chế độ văn bản trước",
        'text_continue_editing': "Tiếp tục chỉnh sửa - con trỏ ở cuối văn bản",
        'text_no_input': "Không có văn bản được nhập - đã hủy văn bản",
        'save_dialog_question': "Bạn muốn tiếp tục như thế nào?",
        'text_save_question': "Lưu tất cả văn bản và dấu gạch chéo, điều chỉnh, tiếp tục chỉnh sửa, hay hủy bỏ?",
        'copy_cross': "Đã sao chép dấu gạch chéo",
        'paste_cross': "Đã dán dấu gạch chéo",
        'paste_text': "Đã dán văn bản",
        'cross_discarded': "Đã hủy dấu gạch chéo",
        'all_discarded': "Đã hủy tất cả",
        'text_discarded': "Đã hủy văn bản",
        'no_texts_to_save': "Không có văn bản để lưu",
        'no_valid_texts': "Không có văn bản hợp lệ để lưu",
        'text_word_singular': "văn bản",
        'text_word_plural': "văn bản",
        'cross_word_singular': "dấu gạch chéo",
        'cross_word_plural': "dấu gạch chéo",
        'texts_saved_title': "Đã lưu văn bản",
        'texts_crosses_saved': "Đã chèn {0} {1} và {2} {3} vào PDF.\n\nĐã tải lại PDF...",
        'texts_crosses_saved_voice': "Đã lưu {0} {1} và {2} {3}.",
        'texts_saved': "Đã chèn {0} {1} vào PDF.\n\nĐã tải lại PDF...",
        'texts_saved_voice': "Đã lưu {0} {1}.",
        'crosses_saved': "Đã chèn {0} {1} vào PDF.\n\nĐã tải lại PDF...",
        'crosses_saved_voice': "Đã lưu {0} {1}.",
        'elements_saved': "Đã chèn {0} phần tử vào PDF.\n\nĐã tải lại PDF...",
        'elements_saved_voice': "Đã lưu {0} phần tử.",
        'text_window_load_error': "Không thể tải cửa sổ văn bản",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Nhập văn bản và Mẫu văn bản – Hướng dẫn chi tiết**

        **1. Chèn và chỉnh sửa văn bản**
        - Nhấp chuột phải vào vị trí mong muốn trong tài liệu và chọn "Chèn văn bản".
        - Một hộp thoại mở ra, nơi bạn có thể nhập và định dạng văn bản:
        • Cỡ chữ, Đậm, Nghiêng, Gạch chân
        • Màu chữ (có thể chọn tự do)
        • Độ trong suốt (độ mờ) qua thanh trượt
        • Ngắt dòng (nhiều độ rộng khác nhau, ví dụ: chiều rộng trang, hẹp, không ngắt)
        - Sau khi xác nhận, văn bản xuất hiện tại vị trí nhấp chuột. Bạn có thể di chuyển nó bằng chuột hoặc phím mũi tên.
        - Nhấp đúp vào văn bản mở chế độ chỉnh sửa; ESC thoát khỏi nó.

        **2. Quản lý mẫu văn bản**
        - Trong hộp thoại văn bản, bạn thấy danh sách tất cả mẫu văn bản đã lưu ở bên trái.
        - **Lưu mẫu:** Nhập văn bản của bạn, định dạng nó, và nhấp vào "💾 Lưu làm mẫu". Nhập tên tệp (không có phần mở rộng).
        - **Tải mẫu:** Nhấp vào tên mong muốn trong danh sách. Văn bản và định dạng được áp dụng và có thể điều chỉnh nếu cần.
        - **Xóa:** Nhấp chuột phải vào mẫu để xóa hoặc thay đổi trạng thái riêng tư của nó.

        **3. Mẫu văn bản riêng tư (Mật khẩu chính)**
        - Nếu bạn đã thiết lập mật khẩu chính (trong Cài đặt → Quản lý mật khẩu), bạn có thể đánh dấu mẫu là "riêng tư".
        - Kích hoạt hộp kiểm "Mẫu văn bản riêng tư" trong hộp thoại trước khi lưu.
        - Mẫu riêng tư chỉ được hiển thị trong danh sách nếu bạn đã nhập mật khẩu chính một lần mỗi phiên (xác thực qua biểu tượng ổ khóa hoặc khi truy cập lần đầu).
        - Bằng cách này, bạn có thể bảo vệ các mẫu văn bản bí mật khỏi truy cập trái phép.

        **4. Chèn dấu gạch chéo**
        - Qua menu ngữ cảnh, bạn cũng có thể chèn một dấu gạch chéo đồ họa (ví dụ: cho hộp kiểm).
        - Kích thước, độ rộng đường và màu sắc của dấu gạch chéo có thể được điều chỉnh toàn cục trong cài đặt (menu "Cài đặt" → "Cài đặt dấu gạch chéo").
        - Nhấp chuột phải vào dấu gạch chéo hiện có để thay đổi nó riêng lẻ.

        **5. Hành động hàng loạt**
        - Nếu bạn đã đặt nhiều văn bản hoặc dấu gạch chéo trên một trang, bạn có thể lưu hoặc hủy tất cả phần tử cùng nhau qua menu ngữ cảnh (nhấp chuột phải trong chế độ văn bản).
        - Khi lưu, tất cả phần tử được nhúng vào PDF và vẫn giữ nguyên dưới dạng đồ họa vector.

        **6. Phím tắt trong chế độ văn bản**
        - Phím mũi tên: di chuyển phần tử
        - Ctrl+Phím mũi tên: bước lớn hơn
        - Enter: mở hộp thoại lưu (lưu tất cả / điều chỉnh / hủy)
        - ESC: hủy phần tử hiện tại
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Nhập văn bản và Mẫu văn bản – Hướng dẫn chi tiết</strong></p>

        <p><strong>1. Chèn và chỉnh sửa văn bản</strong></p>
        <ul>
        <li>Nhấp chuột phải vào vị trí mong muốn trong tài liệu và chọn "Chèn văn bản".</li>
        <li>Một hộp thoại mở ra, nơi bạn có thể nhập và định dạng văn bản:<br/>
        • Cỡ chữ, Đậm, Nghiêng, Gạch chân<br/>
        • Màu chữ (có thể chọn tự do)<br/>
        • Độ trong suốt (độ mờ) qua thanh trượt<br/>
        • Ngắt dòng (nhiều độ rộng khác nhau, ví dụ: chiều rộng trang, hẹp, không ngắt)</li>
        <li>Sau khi xác nhận, văn bản xuất hiện tại vị trí nhấp chuột. Bạn có thể di chuyển nó bằng chuột hoặc phím mũi tên.</li>
        <li>Nhấp đúp vào văn bản mở chế độ chỉnh sửa; ESC thoát khỏi nó.</li>
        </ul>

        <p><strong>2. Quản lý mẫu văn bản</strong></p>
        <ul>
        <li>Trong hộp thoại văn bản, bạn thấy danh sách tất cả mẫu văn bản đã lưu ở bên trái.</li>
        <li><strong>Lưu mẫu:</strong> Nhập văn bản của bạn, định dạng nó, và nhấp vào "💾 Lưu làm mẫu". Nhập tên tệp (không có phần mở rộng).</li>
        <li><strong>Tải mẫu:</strong> Nhấp vào tên mong muốn trong danh sách. Văn bản và định dạng được áp dụng và có thể điều chỉnh nếu cần.</li>
        <li><strong>Xóa:</strong> Nhấp chuột phải vào mẫu để xóa hoặc thay đổi trạng thái riêng tư của nó.</li>
        </ul>

        <p><strong>3. Mẫu văn bản riêng tư (Mật khẩu chính)</strong></p>
        <ul>
        <li>Nếu bạn đã thiết lập mật khẩu chính (trong Cài đặt → Quản lý mật khẩu), bạn có thể đánh dấu mẫu là "riêng tư".</li>
        <li>Kích hoạt hộp kiểm "Mẫu văn bản riêng tư" trong hộp thoại trước khi lưu.</li>
        <li>Mẫu riêng tư chỉ được hiển thị trong danh sách nếu bạn đã nhập mật khẩu chính một lần mỗi phiên (xác thực qua biểu tượng ổ khóa hoặc khi truy cập lần đầu).</li>
        <li>Bằng cách này, bạn có thể bảo vệ các mẫu văn bản bí mật khỏi truy cập trái phép.</li>
        </ul>

        <p><strong>4. Chèn dấu gạch chéo</strong></p>
        <ul>
        <li>Qua menu ngữ cảnh, bạn cũng có thể chèn một dấu gạch chéo đồ họa (ví dụ: cho hộp kiểm).</li>
        <li>Kích thước, độ rộng đường và màu sắc của dấu gạch chéo có thể được điều chỉnh toàn cục trong cài đặt (menu "Cài đặt" → "Cài đặt dấu gạch chéo").</li>
        <li>Nhấp chuột phải vào dấu gạch chéo hiện có để thay đổi nó riêng lẻ.</li>
        </ul>

        <p><strong>5. Hành động hàng loạt</strong></p>
        <ul>
        <li>Nếu bạn đã đặt nhiều văn bản hoặc dấu gạch chéo trên một trang, bạn có thể lưu hoặc hủy tất cả phần tử cùng nhau qua menu ngữ cảnh (nhấp chuột phải trong chế độ văn bản).</li>
        <li>Khi lưu, tất cả phần tử được nhúng vào PDF và vẫn giữ nguyên dưới dạng đồ họa vector.</li>
        </ul>

        <p><strong>6. Phím tắt trong chế độ văn bản</strong></p>
        <ul>
        <li>Phím mũi tên: di chuyển phần tử</li>
        <li>Ctrl+Phím mũi tên: bước lớn hơn</li>
        <li>Enter: mở hộp thoại lưu (lưu tất cả / điều chỉnh / hủy)</li>
        <li>ESC: hủy phần tử hiện tại</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Cài đặt dấu gạch chéo",
        'cross_properties': "Thuộc tính dấu gạch chéo",
        'cross_size': "Kích thước (px):",
        'cross_line_width': "Độ rộng đường:",
        'cross_color': "Màu sắc:",
        'cross_choose_color': "Chọn",
        'cross_fine_tuning': "Điều chỉnh tinh khi lưu (pixel)",
        'cross_offset_x': "Độ lệch X:",
        'cross_offset_y': "Độ lệch Y:",
        'cross_offset_x_tooltip': "Giá trị âm di chuyển dấu gạch chéo sang trái khi lưu, giá trị dương sang phải",
        'cross_offset_y_tooltip': "Giá trị âm di chuyển dấu gạch chéo lên trên khi lưu, giá trị dương xuống dưới",
        'cross_preview': "Xem trước",
        'cross_save': "Áp dụng cài đặt",
        'cross_customized': "Đã tùy chỉnh dấu gạch chéo",
        'cross_settings_applied': "Đã lưu cài đặt dấu gạch chéo.\nKích thước: {0}px, Độ rộng đường: {1}px\n{2}",
        'cross_updated_count': "Đã cập nhật {0} dấu gạch chéo hiện có.",
        'cross_no_crosses': "Không tìm thấy dấu gạch chéo nào.",
        'cross_settings_applied_all': "Đã áp dụng cài đặt dấu gạch chéo cho tất cả {0} dấu gạch chéo",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Cài đặt chữ ký",
        'signature_1': "Chữ ký 1",
        'signature_2': "Chữ ký 2",
        'signature_select': "Chọn chữ ký",
        'signature_add': "➕ Thêm chữ ký mới...",
        'signature_size': "Kích thước cho chữ ký {0} (%):",
        'signature_common': "Cài đặt chung",
        'signature_timestamp': "Tự động thêm dấu thời gian",
        'signature_location': "Địa điểm mặc định:",
        'signature_timestamp_size': "Cỡ chữ dấu thời gian:",
        'signature_no_files': "-- Không tìm thấy chữ ký --",
        'signature_insert': "Chèn chữ ký",
        'signature_insert_1': "Chèn chữ ký 1",
        'signature_insert_2': "Chèn chữ ký 2",
        'signature_customize': " Tùy chỉnh chữ ký",
        'signature_discard': " Hủy bỏ chữ ký này",
        'signature_save_all': " Lưu tất cả chữ ký",
        'signature_discard_all': " Hủy bỏ tất cả chữ ký",
        'signature_guide_title': "Chữ ký - Hướng dẫn",
        'signature_guide': """
📝 Chữ ký - Hướng dẫn nhanh

- Thiết lập mật khẩu chính
- Cấu hình chữ ký trong menu Cài đặt
  (kích thước, dấu thời gian ...)
- Chèn bằng NHẤP CHUỘT PHẢI tại vị trí mong muốn
  (yêu cầu mật khẩu chính một lần mỗi phiên)
- Di chuyển chữ ký bằng chuột hoặc phím mũi tên
- Có thể chèn nhiều chữ ký lần lượt
- Mỗi chữ ký có thể được tùy chỉnh riêng
- Hủy bỏ từng chữ ký
- Lưu / hủy bỏ tất cả chữ ký cùng lúc
- Ngoài ra, có thể sử dụng thanh menu.
        """,
        'signature_placeholder': "Không có bản xem trước",
        'signature_info': "Chữ ký {0}: {1}×{2} px ({3}% của {4}×{5})",
        'signature_info_placeholder': "Cài đặt cho chữ ký {0}",
        'signature_inserted': "Đã chèn chữ ký {0} vào trang {1}",
        'signature_deleted': "Đã xóa chữ ký",
        'signature_copied': "Đã sao chép chữ ký",
        'signature_pasted': "Đã dán chữ ký {0}",
        'signature_saved': "Đã chèn {0} chữ ký vào PDF.\n\nĐã tải lại PDF...",
        'signature_saved_voice': "Đã lưu {0} chữ ký",
        'mode_replace_signature_format': "Thoát chế độ và chèn chữ ký {0}",
        'mode_conflict_voice_signature': "Chế độ {0} đang hoạt động. Thoát và chèn chữ ký?",
        'signature_not_configured': "Chữ ký {0} chưa được cấu hình",
        'signature_file_not_found': "Không tìm thấy tệp chữ ký",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "Không có chữ ký đã sao chép",
        'no_signatures_to_save': "Không có chữ ký để lưu",
        'signature_save_question': "Lưu tất cả chữ ký, điều chỉnh, hay hủy bỏ cái này?",
        'signatures_saved_title': "Đã lưu chữ ký",
        'signatures_saved': "Đã chèn {0} chữ ký vào PDF.\n\nĐã tải lại PDF...",
        'signatures_saved_voice': "Đã lưu {0} chữ ký.",
        'all_signatures_discarded': "Đã hủy bỏ tất cả chữ ký",
        'signature_settings_saved': "Đã lưu cài đặt chữ ký",
        'signature_cancelled': "Đã hủy chữ ký",
        'signature_active_title': "Chữ ký đang hoạt động",
        'signature_replace_question': "Một chữ ký đã đang hoạt động.\n\nBạn có muốn thay thế chữ ký hiện tại?",
        'signature_replace': "Thay thế chữ ký",
        'signature_replace_voice': "Thay thế chữ ký hiện tại hay hủy?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Cài đặt hình ảnh",
        'image_common': "Cài đặt hình ảnh chung",
        'image_keep_aspect': "Giữ tỷ lệ khung hình khi kéo",
        'image_default_size': "Kích thước mặc định (%):",
        'image_dark_invert': "Đảo ngược hình ảnh trong Chế độ tối",
        'image_dark_invert_tooltip': "Đã bật: hình ảnh được đảo ngược để dễ nhìn hơn",
        'image_fine_tuning': "Điều chỉnh tinh (pixel)",
        'image_offset_x': "Độ lệch X:",
        'image_offset_y': "Độ lệch Y:",
        'image_offset_x_tooltip': "Giá trị âm di chuyển hình ảnh sang trái khi lưu, giá trị dương sang phải",
        'image_offset_y_tooltip': "Giá trị âm di chuyển hình ảnh lên trên khi lưu, giá trị dương xuống dưới",
        'image_select': "Chọn hình ảnh",
        'image_insert': "Chèn hình ảnh",
        'image_customize': " Tùy chỉnh hình ảnh",
        'image_aspect': " Giữ tỷ lệ khung hình",
        'image_discard': " Hủy bỏ hình ảnh này",
        'image_save_all': " Lưu tất cả hình ảnh",
        'image_discard_all': " Hủy bỏ tất cả hình ảnh",
        'image_filter': "Hình ảnh",
        'image_guide_title': "Chèn hình ảnh - Hướng dẫn",
        'image_guide': """
📷 Chèn hình ảnh vào PDF - Hướng dẫn nhanh:

1. Nhấp chuột phải vào vị trí mong muốn
2. "Chèn hình ảnh" → chọn hình ảnh
3. Định vị hình ảnh: kéo bằng chuột
4. Điều chỉnh kích thước: kéo ở các góc/cạnh
5. Giữ tỷ lệ khung hình: phím [A]
6. Điều chỉnh thêm: nhấp chuột phải vào hình ảnh

Mẹo: Bạn có thể điều chỉnh cài đặt trong menu ngữ cảnh.
        """,
        'image_inserted': "Đã chèn hình ảnh {0} vào trang {1}",
        'image_deleted': "Đã hủy hình ảnh",
        'image_copied': "Đã sao chép hình ảnh",
        'image_pasted': "Đã dán hình ảnh",
        'image_saved': "Đã chèn {0} hình ảnh vào PDF.\n\nĐã tải lại PDF...",
        'image_saved_voice': "Đã lưu {0} hình ảnh",
        'image_aspect_on': "đã bật",
        'image_aspect_off': "đã tắt",
        'image_aspect_toggle': "Giữ tỷ lệ khung hình {0}",
        'image_reset': "Đã đặt lại hình ảnh về kích thước gốc",
        'image_replaced': "Đã thay thế hình ảnh",
        'image_invalid': "Không phải hình ảnh hợp lệ",
        'mode_replace_image': "Chèn hình ảnh",
        'mode_conflict_voice_image': "Chế độ {0} đang hoạt động. Thoát và chèn hình ảnh?",
        'image_active_title': "Hình ảnh đang hoạt động",
        'image_replace_question': "Một hình ảnh đã đang hoạt động.\n\nBạn có muốn thay thế hình ảnh hiện tại?",
        'image_replace': "Thay thế hình ảnh",
        'image_replace_voice': "Thay thế hình ảnh hiện tại hay hủy?",
        'image_filter_all': "Hình ảnh (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Tất cả tệp (*.*)",
        'no_copied_image': "Không có hình ảnh đã sao chép",
        'image_discarded': "Đã hủy hình ảnh",
        'image_save_question': "Lưu tất cả hình ảnh, điều chỉnh, hay hủy bỏ cái này?",
        'no_images_to_save': "Không có hình ảnh để lưu",
        'no_valid_images': "Không có hình ảnh hợp lệ để lưu",
        'images_saved_title': "Đã lưu hình ảnh",
        'images_saved': "Đã chèn {0} hình ảnh vào PDF.\n\nĐã tải lại PDF...",
        'images_saved_voice': "Đã lưu {0} hình ảnh.",
        'all_images_discarded': "Đã hủy bỏ tất cả hình ảnh",
        'image_settings_updated': "Đã cập nhật cài đặt hình ảnh",
        'image_replace_title': "Chọn hình ảnh mới",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Cài đặt hình dạng",
        'form_basic': "Cài đặt cơ bản",
        'form_default_type': "Loại hình dạng mặc định:",
        'form_rectangle': "Hình chữ nhật",
        'form_ellipse': "Hình elip",
        'form_line': "Đường thẳng",
        'form_arrow': "Mũi tên",
        'form_line_width': "Độ rộng đường:",
        'form_colors': "Màu sắc",
        'form_line_color': "Màu đường:",
        'form_fill_color': "Màu tô:",
        'form_choose_color': "Chọn",
        'form_transparent': "Nền trong suốt (chỉ đường)",
        'form_filled': "đã tô",
        'form_dark_mode': "Chế độ tối",
        'form_dark_invert': "Đảo ngược màu trong Chế độ tối",
        'form_fine_tuning': "Điều chỉnh tinh (pixel)",
        'form_offset_x': "Độ lệch X:",
        'form_offset_y': "Độ lệch Y:",
        'form_offset_x_tooltip': "Giá trị âm di chuyển hình dạng sang trái khi lưu, giá trị dương sang phải",
        'form_offset_y_tooltip': "Giá trị âm di chuyển hình dạng lên trên khi lưu, giá trị dương xuống dưới",
        'form_preview': "Xem trước",
        'form_insert': "Chèn hình dạng",
        'form_rectangle_insert': "Hình chữ nhật",
        'form_ellipse_insert': "Hình elip/Hình tròn",
        'form_line_insert': "Đường thẳng (2 lần nhấp)",
        'form_arrow_insert': "Mũi tên (2 lần nhấp)",
        'form_customize': " Tùy chỉnh hình dạng",
        'form_transparent_toggle': " Nền trong suốt",
        'form_discard': " Hủy bỏ hình dạng này",
        'form_save_all': " Lưu tất cả hình dạng",
        'form_discard_all': " Hủy bỏ tất cả hình dạng",
        'form_guide_title': "Chèn hình dạng - Hướng dẫn",
        'form_guide': """
📐 Chèn hình dạng vào PDF - Hướng dẫn nhanh:

1. Chọn loại hình dạng (hình chữ nhật, elip, đường thẳng, mũi tên)
2. Nhấp vào vị trí
   - Với hình chữ nhật/elip: Một lần nhấp đặt hình dạng
   - Với đường thẳng/mũi tên: Hai lần nhấp cho điểm bắt đầu và kết thúc
3. Định vị hình dạng: kéo bằng chuột
4. Điều chỉnh kích thước: kéo ở các góc/cạnh
5. Lưu hình dạng: Enter
6. Hủy bỏ hình dạng: ESC
7. Điều chỉnh thêm: nhấp chuột phải vào hình dạng

Mẹo: Bạn có thể điều chỉnh cài đặt trong menu ngữ cảnh.
        """,
        'form_inserted': "Đã chèn {0} vào trang {1}",
        'form_deleted': "Đã xóa hình dạng",
        'form_copied': "Đã sao chép hình dạng",
        'form_pasted': "Đã dán hình dạng",
        'form_saved': "Đã chèn {0} hình dạng vào PDF.\n\nĐã tải lại PDF...",
        'form_saved_voice': "Đã lưu {0} hình dạng",
        'form_reset': "Đã đặt lại hình dạng về kích thước mặc định",
        'form_transparent_on': "đã bật",
        'form_transparent_off': "đã tắt",
        'form_transparent_toggled': "Nền trong suốt {0}",
        'form_line_cancel': "Đã hủy vẽ đường thẳng",
        'form_second_click': "Bây giờ nhấp điểm kết thúc cho {0}",
        'mode_replace_form': "Chèn hình dạng",
        'mode_conflict_voice_form': "Chế độ {0} đang hoạt động. Thoát và chèn một hình dạng?",
        'form_settings_updated': "Đã cập nhật cài đặt hình dạng",
        'form_unknown': "Hình dạng",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Nhấp vào vị trí bắt đầu",
        'form_line_guide_2': "2. Nhấp vào vị trí kết thúc",
        'form_line_guide_3': "Đường thẳng sẽ được vẽ giữa hai điểm.",
        'form_line_status_1': "Đang chờ lần nhấp đầu tiên...",
        'form_line_status_2': "Đã đặt điểm đầu tiên: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Bây giờ nhấp điểm kết thúc...",
        'form_line_status_4': "Đã đặt cả hai điểm.\nNhấp 'Hoàn tất' để lưu.",
        'form_line_reset': "Đặt lại",
        'form_line_finish': "Hoàn tất",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Sao chép (Cmd+C)",
        'paste': "Dán (Cmd+V)",
        'copied': "Đã sao chép: {0}",
        'no_element_to_copy': "Chưa chọn phần tử để sao chép",
        'no_copied_data': "Không có dữ liệu đã sao chép",
        'no_valid_position': "Không có vị trí hợp lệ để dán",
        'copy_text': "Đã sao chép văn bản",
        'copy_image': "Đã sao chép hình ảnh",
        'copy_form': "Đã sao chép hình dạng",
        'copy_signature': "Đã sao chép chữ ký",
        'element_text': "văn bản",
        'element_image': "hình ảnh",
        'element_form': "hình dạng",
        'element_signature': "chữ ký",
        'element_unknown': "phần tử",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Xung đột chế độ",
        'mode_conflict_message': "Chế độ '{0}' đã đang hoạt động.\n\nBạn có muốn thoát nó và {1}?",
        'mode_replace': "Thoát chế độ và {0}",
        'mode_cancel': "Hủy",
        'mode_replace_text': "chèn văn bản",
        'mode_replace_cross': "chèn dấu gạch chéo",
        'mode_replace_signature': "chèn chữ ký",
        'mode_replace_image': "chèn hình ảnh",
        'mode_replace_form': "chèn hình dạng",
        'mode_conflict_voice': "Chế độ {0} đang hoạt động. Thoát và chèn văn bản?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Nhập văn bản",
        'active_mode_signature': "Chữ ký",
        'active_mode_image': "Hình ảnh",
        'active_mode_form': "Hình dạng",
        'active_mode_and': " và ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Chèn",                    # Hauptmenü
        'insert_another_text': "Chèn văn bản",          # Vereinfacht
        'insert_another_cross': "Chèn dấu gạch chéo",        # Vereinfacht
        'insert_another_signature_1': "Chữ ký 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Chữ ký 2",      # Untermenü-Eintrag
        'insert_another_image': "Chèn hình ảnh",         # Vereinfacht
        'insert_another_form_rect': "Hình chữ nhật",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Hình elip",        # Untermenü-Eintrag
        'insert_another_form_line': "Đường thẳng (2 lần nhấp)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Mũi tên (2 lần nhấp)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Lưu {0}",
        'save_dialog_message': "{0} sẽ được lưu trên trang {1}.\n\nBạn muốn tiếp tục như thế nào?",
        'save_all': "Lưu tất cả {0}",
        'save_single': "Lưu {0}",
        'save_customize': "Tùy chỉnh {0}",
        'save_discard': "Hủy bỏ {0} này",
        'save_continue': "Tiếp tục chỉnh sửa",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Đi tới trang {0}",
        'context_rotate': " Xoay trang {0}",
        'context_delete': " Xóa trang {0}",
        'context_export': " Xuất trang {0}",
        'context_mark_as': " Đánh dấu trang là...",
        'context_mark_empty': " Trang trống",
        'context_unmark_empty': " Không còn trống",
        'context_mark_export': " Đánh dấu để xuất",
        'context_unmark_export': " Không còn xuất",
        'context_batch_actions': " Hành động hàng loạt",
        'context_batch_delete_empty': " Xóa tất cả {0} trang trống",
        'context_batch_export_single': " Tất cả {0} trang (một tệp)",
        'context_batch_export_split': " Tất cả {0} trang (riêng lẻ)",
        'context_drag_start': " Bắt đầu Kéo & Thả",
        'context_drag_stop': " Kết thúc Kéo & Thả",
        'context_insert': " Chèn",
        'context_insert_pages': " Chèn trang",
        'context_zoom': "Phóng to",
        'discard_mixed': "Hủy bỏ tất cả {0} {1} và {2} {3}",
        'save_mixed': "Lưu {0} {1} và {2} {3}",
        'discard_texts': "Hủy bỏ tất cả {0} văn bản",
        'discard_text_single': "Hủy bỏ 1 văn bản",
        'save_texts': "Lưu {0} văn bản",
        'save_text_single': "Lưu 1 văn bản",
        'discard_crosses': "Hủy bỏ tất cả {0} dấu gạch chéo",
        'discard_cross_single': "Hủy bỏ 1 dấu gạch chéo",
        'save_crosses': "Lưu {0} dấu gạch chéo",
        'save_cross_single': "Lưu 1 dấu gạch chéo",
        'discard_signatures': "Hủy bỏ tất cả {0} chữ ký",
        'save_signature_single': "Lưu 1 chữ ký",
        'save_signatures': "Lưu {0} chữ ký",
        'discard_images': "Hủy bỏ tất cả {0} hình ảnh",
        'save_image_single': "Lưu 1 hình ảnh",
        'save_images': "Lưu {0} hình ảnh",
        'discard_forms': "Hủy bỏ tất cả {0} hình dạng",
        'save_form_single': "Lưu 1 hình dạng",
        'save_forms': "Lưu {0} hình dạng",
        'cross_discard': "Hủy bỏ dấu gạch chéo này",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Thông tin Xuất / Nhập",
        'export_what': "📋 Cái gì được xuất?",
        'export_general': "Cài đặt chung",
        'export_general_items': "• Đầu ra giọng nói (bật/tắt, tốc độ)\n• Chế độ Tối/Sáng\n• Cài đặt sao lưu\n• Cài đặt OCR",
        'export_image_form': "Cài đặt hình ảnh và hình dạng",
        'export_image_form_items': "• Cài đặt hình ảnh (tỷ lệ khung hình, kích thước mặc định)\n• Cài đặt hình dạng (độ rộng đường, màu sắc)\n• Cài đặt chữ ký (đường dẫn, kích thước, dấu thời gian)",
        'export_passwords': "Cơ sở dữ liệu mật khẩu",
        'export_passwords_items': "• Tất cả mật khẩu PDF đã lưu\n• Có thể chọn mã hóa hoặc giải mã",
        'export_master': "Cài đặt mật khẩu chính",
        'export_master_items': "• Băm mật khẩu chính\n• Cài đặt cho chữ ký/mẫu văn bản",
        'export_signatures': "Chữ ký và mẫu văn bản",
        'export_signatures_items': "• Tất cả tệp hình ảnh (chữ ký)\n• Tất cả mẫu văn bản với định dạng\n• Đánh dấu riêng tư/công khai",
        'export_import_warning': "⚠️ Lưu ý quan trọng",
        'export_import_note': "• Khi nhập, TẤT CẢ cài đặt hiện tại sẽ bị ghi đè\n• Cần khởi động lại ứng dụng\n• Các chữ ký/mẫu văn bản hiện có sẽ bị thay thế",
        'export_master_note': "• Nếu có mật khẩu chính, bạn có thể chọn:\n  - Giải mã (mật khẩu dạng văn bản rõ)\n  - Mã hóa (chỉ đọc được bằng mật khẩu chính)",
        'export_security': "• Tệp ZIP được xuất chứa dữ liệu bí mật\n• Vui lòng lưu trữ an toàn (ví dụ: USB được mã hóa)\n• Nếu mất tệp, mật khẩu sẽ mất vĩnh viễn",
        'export_format': "📁 Định dạng xuất",
        'export_format_desc': "Các cài đặt được lưu trong một tệp ZIP duy nhất:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Đã xuất cài đặt thành công",
        'export_failed': "Xuất thất bại",
        'export_import_question': "Bạn có muốn khởi động lại ứng dụng ngay bây giờ?",
        'export_password_question': "Một mật khẩu chính đã được thiết lập.\n\nBạn có muốn xuất mật khẩu dưới dạng giải mã?\n(nếu không, chúng sẽ được xuất dưới dạng mã hóa)",
        'export_decrypt': "Xuất đã giải mã",
        'export_encrypt': "Xuất đã mã hóa",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Thông tin",
        'info_title': "Giới thiệu về PDF Dark View",
        'info_version': "Phiên bản",
        'info_author': "Được phát triển bởi Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Giới thiệu",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> là trình xem PDF dễ tiếp cận, được phát triển đặc biệt cho người khiếm thị.</p>

            <p><strong>Tính năng chính:</strong></p>
            <ul>
                <li>Giao diện tương phản cao, có thể tùy chỉnh</li>
                <li>Điều khiển hoàn toàn bằng bàn phím</li>
                <li>Đọc văn bản tích hợp</li>
                <li>OCR cho tài liệu quét</li>
                <li>Công cụ chỉnh sửa toàn diện</li>
            </ul>

            <p>Hỗ trợ hơn 50 ngôn ngữ – để PDF có thể tiếp cận với mọi người.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Tính năng",
        'info_features_intro': "PDF Dark View cung cấp cho bạn các khả năng sau:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Hiển thị và điều hướng</strong> – Chế độ Tối/Sáng, lật trang, phóng to, nhảy đến trang</li>
            <li><strong>OCR (Nhận dạng văn bản)</strong> – Biến tài liệu quét thành có thể tìm kiếm và sao chép</li>
            <li><strong>Chỉnh sửa</strong> – Chèn văn bản, dấu thập, chữ ký, hình ảnh và hình dạng</li>
            <li><strong>Quản lý trang</strong> – Xóa, trích xuất, chèn, di chuyển bằng kéo và thả</li>
            <li><strong>Xuất</strong> – Sang Word, Pages hoặc dưới dạng văn bản</li>
            <li><strong>Bảo mật</strong> – Bảo vệ và quản lý bằng mật khẩu</li>
            <li><strong>Khả năng tiếp cận</strong> – Đọc văn bản, điều khiển bàn phím, tương phản cao</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Thao tác",
        'info_accessibility': "♿ Khả năng tiếp cận – điều khiển hoàn toàn bằng bàn phím",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Chung</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Mở PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Tìm kiếm</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Chuyển đổi chế độ Tối/Sáng</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> In</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Thoát</div>

        <div class="shortcut-cat">📖 Điều hướng</div>
        <div class="shortcut-row"><kbd>Phím mũi tên</kbd> Lật từng trang</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Đến trang</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Trang đầu tiên</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Trang cuối cùng</div>

        <div class="shortcut-cat">✏️ Chỉnh sửa</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Chèn văn bản</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Xóa trang</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Trích xuất trang</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Chèn trang</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Di chuyển trang</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Xoay trang</div>

        <div class="shortcut-cat">🖼️ Di chuyển thành phần</div>
        <div class="shortcut-row"><kbd>Phím mũi tên</kbd> Di chuyển văn bản/hình ảnh/chữ ký</div>
        <div class="shortcut-row"><kbd>Ctrl+Phím mũi tên</kbd> Bước lớn hơn</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Lưu</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Hủy bỏ</div>

        <div class="shortcut-cat">🗣️ Đọc văn bản</div>
        <div class="shortcut-row"><kbd>F2</kbd> Bật/tắt đọc văn bản</div>
        """,
        'info_contextmenu': "📌 Quan trọng: Tất cả các chức năng cũng có thể truy cập qua menu ngữ cảnh (nút chuột phải)!",
        'info_accessibility_hint': "💡 Mẹo: Đọc văn bản (F2) giúp định hướng dễ dàng hơn và cung cấp phản hồi về menu và hộp thoại.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Giấy phép & Thông tin xuất bản",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 THÔNG TIN XUẤT BẢN</strong><br>
        Thông tin theo § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Đức<br>
        Email: binhdiez64@gmail.com<br>
        Chịu trách nhiệm về nội dung: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Tuyên bố miễn trừ trách nhiệm</strong><br>
        Phần mềm được phát triển với sự cẩn trọng tối đa. Không có bảo đảm về tính chính xác, đầy đủ và chức năng. Việc sử dụng là tự chịu rủi ro.<br><br>

        <strong>📄 Giấy phép MIT (sử dụng cá nhân)</strong><br>
        Bản quyền (c) 2026 Toralf Schulz (BinhDiez)<br>
        Được phép: sử dụng miễn phí, thay đổi cá nhân, bản sao cá nhân.<br>
        Không được phép: bán, sử dụng thương mại, xóa thông báo bản quyền.<br><br>

        <strong>🔧 Thành phần của bên thứ ba</strong><br>
        Phần mềm này chứa các thành phần theo giấy phép GPL, AGPL, Apache 2.0, BSD và MIT.<br>
        Khi phân phối lại, phải tuân thủ các điều khoản giấy phép tương ứng.<br><br>

        <strong>🌐 Mã nguồn mở</strong><br>
        Mã nguồn có sẵn và có thể được xem, sửa đổi và phân phối lại theo các điều khoản giấy phép tương ứng.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Lời cảm ơn",
        'info_credits': "Cảm ơn cộng đồng mã nguồn mở",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – Xử lý PDF</li>
            <li><strong>PyQt5</strong> – Giao diện đồ họa</li>
            <li><strong>Tesseract OCR</strong> – Nhận dạng văn bản</li>
            <li><strong>OCRmyPDF</strong> – Tích hợp OCR</li>
            <li><strong>python-docx</strong> – Xuất Word</li>
            <li><strong>qtawesome</strong> – Biểu tượng</li>
            <li><strong>DeepSeek</strong> – Hỗ trợ dịch thuật (50+ ngôn ngữ)</li>
            <li><strong>Tất cả người dùng</strong> – Vì những phản hồi quý giá</li>
            <li><strong>Cộng đồng mã nguồn mở</strong> – Vì những thư viện tuyệt vời</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Ngôn ngữ",
        'info_languages_header': "🌍 Hỗ trợ ngôn ngữ",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View hiện hỗ trợ <strong>62 ngôn ngữ</strong> – để phần mềm có thể được sử dụng dễ dàng trên toàn thế giới.</p>

            <p><strong>📖 Danh sách đầy đủ các ngôn ngữ (Tính đến tháng 3 năm 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Tiếng Afrikaans</li>
                    <li>🇦🇱 Tiếng Albania (Shqip)</li>
                    <li>🇩🇿 Tiếng Ả Rập (العربية)</li>
                    <li>🇮🇩 Tiếng Bali (Basa Bali)</li>
                    <li>🇧🇩 Tiếng Bengal (বাংলা)</li>
                    <li>🇲🇲 Tiếng Miến Điện (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Tiếng Bosnia (Bosanski)</li>
                    <li>🇧🇬 Tiếng Bulgaria (Български)</li>
                    <li>🇨🇳 Tiếng Trung (中文)</li>
                    <li>🇩🇰 Tiếng Đan Mạch (Dansk)</li>
                    <li>🇩🇪 Tiếng Đức (Deutsch)</li>
                    <li>🇬🇧 Tiếng Anh (English)</li>
                    <li>🇪🇪 Tiếng Estonia (Eesti)</li>
                    <li>🇫🇮 Tiếng Phần Lan (Suomi)</li>
                    <li>🇫🇷 Tiếng Pháp (Français)</li>
                    <li>🇬🇷 Tiếng Hy Lạp (Ελληνικά)</li>
                    <li>🇮🇱 Tiếng Do Thái (עברית)</li>
                    <li>🇮🇳 Tiếng Hindi (हिन्दी)</li>
                    <li>🇭🇷 Tiếng Croatia (Hrvatski)</li>
                    <li>🇭🇺 Tiếng Hungary (Magyar)</li>
                    <li>🇮🇩 Tiếng Indonesia (Bahasa Indonesia)</li>
                    <li>🇮🇪 Tiếng Ireland (Gaeilge)</li>
                    <li>🇮🇸 Tiếng Iceland (Íslenska)</li>
                    <li>🇮🇹 Tiếng Ý (Italiano)</li>
                    <li>🇯🇵 Tiếng Nhật (日本語)</li>
                    <li>🇰🇭 Tiếng Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Tiếng Hàn (한국어)</li>
                    <li>🇱🇦 Tiếng Lào (ພາສາລາວ)</li>
                    <li>🇱🇻 Tiếng Latvia (Latviešu)</li>
                    <li>🇱🇹 Tiếng Litva (Lietuvių)</li>
                    <li>🇱🇺 Tiếng Luxembourg (Lëtzebuergesch)</li>
                    <li>🇲🇾 Tiếng Mã Lai (Bahasa Melayu)</li>
                    <li>🇮🇳 Tiếng Marathi (मराठी)</li>
                    <li>🇲🇳 Tiếng Mông Cổ (Монгол)</li>
                    <li>🇳🇵 Tiếng Nepal (नेपाली)</li>
                    <li>🇳🇱 Tiếng Hà Lan (Nederlands)</li>
                    <li>🇳🇴 Tiếng Na Uy (Norsk)</li>
                    <li>🇦🇫 Tiếng Pashto (پښتو)</li>
                    <li>🇮🇷 Tiếng Ba Tư (فارسی)</li>
                    <li>🇵🇱 Tiếng Ba Lan (Polski)</li>
                    <li>🇵🇹 Tiếng Bồ Đào Nha (Português)</li>
                    <li>🇮🇳 Tiếng Punjab (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Tiếng Romania (Română)</li>
                    <li>🇷🇺 Tiếng Nga (Русский)</li>
                    <li>🇸🇪 Tiếng Thụy Điển (Svenska)</li>
                    <li>🇷🇸 Tiếng Serbia (Српски)</li>
                    <li>🇸🇰 Tiếng Slovakia (Slovenčina)</li>
                    <li>🇸🇮 Tiếng Slovenia (Slovenščina)</li>
                    <li>🇪🇸 Tiếng Tây Ban Nha (Español)</li>
                    <li>🇹🇿 Tiếng Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tiếng Tagalog (Filipino)</li>
                    <li>🇮🇳 Tiếng Tamil (தமிழ்)</li>
                    <li>🇮🇳 Tiếng Telugu (తెలుగు)</li>
                    <li>🇹🇭 Tiếng Thái (ไทย)</li>
                    <li>🇨🇿 Tiếng Séc (Čeština)</li>
                    <li>🇹🇷 Tiếng Thổ Nhĩ Kỳ (Türkçe)</li>
                    <li>🇺🇦 Tiếng Ukraina (Українська)</li>
                    <li>🇵🇰 Tiếng Urdu (اردو)</li>
                    <li>🇻🇳 Tiếng Việt (Tiếng Việt)</li>
                    <li>🇸🇳 Tiếng Wolof (Wolof)</li>
                    <li>🇺🇸 Tiếng Yiddish (ייִדיש)</li>
                    <li>🇿🇦 Tiếng Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Thêm ngôn ngữ của riêng bạn:</strong><br>
                Bạn muốn một ngôn ngữ chưa được bao gồm? Chỉ cần đặt tệp từ điển của riêng bạn (<code>sprache_xx.py</code>) bên cạnh ứng dụng – phần mềm sẽ tự động nhận dạng nó. Nếu bạn quan tâm đến một bản dịch đặc biệt, vui lòng liên hệ với tôi.
            </div>

            <p><strong>🙏 Lời cảm ơn đặc biệt:</strong> DeepSeek đã hỗ trợ dịch tất cả các từ điển sang 62 ngôn ngữ.</p>

            <p>📧 Liên hệ để biết thông tin dịch thuật: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Lỗi",
        'error_occurred': "Đã xảy ra lỗi",
        'error_pdf_load': "Lỗi khi tải PDF",
        'error_pdf_save': "Lỗi khi lưu PDF",
        'error_ocr': "Lỗi khi nhận dạng văn bản",
        'error_no_pdf': "Chưa mở PDF",
        'error_page_not_found': "Không tìm thấy trang",
        'error_invalid_range': "Khoảng trang không hợp lệ",
        'error_file_not_found': "Không tìm thấy tệp",
        'error_permission': "Không có quyền",
        'error_unknown': "Lỗi không xác định",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Thành công",
        'success_operation': "Thao tác hoàn tất thành công",
        'success_saved': "Đã lưu thành công",
        'success_exported': "Đã xuất thành công",
        'success_imported': "Đã nhập thành công",
        'success_deleted': "Đã xóa thành công",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Xác nhận",
        'confirm_yes': "Có",
        'confirm_no': "Không",
        'confirm_ok': "OK",
        'confirm_cancel': "Hủy",
        'confirm_delete': "Xóa",
        'confirm_overwrite': "Ghi đè",
        'confirm_continue': "Tiếp tục",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Đang tải PDF...",
        'progress_saving': "Đang lưu PDF...",
        'progress_exporting': "Đang xuất PDF...",
        'progress_processing': "Đang xử lý...",
        'progress_wait': "Vui lòng chờ...",
        'progress_preparing': "Đang chuẩn bị...",
        'progress_finalizing': "Đang hoàn thiện...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Trắng",
        'color_black': "Đen",
        'color_red': "Đỏ",
        'color_green': "Xanh lá",
        'color_blue': "Xanh dương",
        'color_yellow': "Vàng",
        'color_magenta': "Đỏ tươi",
        'color_cyan': "Xanh lơ",
        'color_orange': "Cam",
        'color_gray': "Xám",
        'color_custom': "Bộ chọn màu",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Tệp",
        'menu_edit': "&Sửa",
        'menu_view': "&Xem",
        'menu_tools': "&Công cụ",
        'menu_settings': "&Cài đặt",
        'menu_help': "&Trợ giúp",
        'menu_language': "🌐 Ngôn ngữ",
        'menu_guides': "&Hướng dẫn",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Mở",
        'file_save_as': "&Lưu dưới dạng...",
        'file_protect': "&Bảo vệ tài liệu...",
        'file_export': "&Xuất",
        'file_export_pages': "Xuất dưới dạng Pages",
        'file_export_word': "Xuất dưới dạng DOCX",
        'file_export_text': "Xuất dưới dạng TXT",
        'file_print_now': "&In ngay",
        'file_print': "&In",
        'file_close': "&Đóng",
        'file_quit': "&Thoát",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Tìm kiếm",
        'edit_ocr': " Chạy OCR",
        'edit_rotate': "&Xoay trang",
        'edit_rotate_all': "&Xoay tất cả trang",
        'edit_delete_pages': "&Xóa trang",
        'edit_extract_pages': "&Trích xuất trang",
        'edit_insert_pages': "&Chèn trang",
        'edit_move_pages': "&Di chuyển trang",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Chèn văn bản và dấu gạch chéo",
        'text_insert': " Chèn văn bản",
        'cross_insert': " Chèn dấu gạch chéo",
        'text_customize': " Tùy chỉnh văn bản",
        'cross_customize': " Tùy chỉnh dấu gạch chéo này",
        'cross_customize_all': " Tùy chỉnh tất cả dấu gạch chéo",
        'text_discard': " Hủy bỏ văn bản / dấu gạch chéo này",
        'text_discard_all': " Hủy bỏ tất cả văn bản và dấu gạch chéo",
        'text_save_all': " Lưu tất cả văn bản và dấu gạch chéo",
        'text_guide': " Nhập văn bản / mẫu văn bản - Hướng dẫn",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Chèn chữ ký",
        'signature_settings_menu': " Cài đặt...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Chèn hình ảnh",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Chèn hình dạng",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Hiển thị cửa sổ văn bản",
        'view_zoom': "&Phóng to",
        'view_zoom_page': "&Chiều rộng trang (mặc định)",
        'view_zoom_two': "&Hai trang",
        'view_zoom_overview': "&Tổng quan (nhiều trang)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Trợ năng",
        'settings_voice': "Đầu ra giọng nói",
        'settings_voice_tooltip': "bổ sung thông tin cho đầu ra giọng nói của trình đọc màn hình",
        'settings_signature': "&Cài đặt chữ ký",
        'settings_password': "&Quản lý mật khẩu",
        'settings_backup': "Tạo bản sao lưu trước khi thay đổi",
        'settings_export_import': "&Xuất / nhập cài đặt",
        'settings_export': "&Xuất tất cả cài đặt...",
        'settings_import': "&Nhập tất cả cài đặt...",
        'settings_export_info': "&Cái gì được xuất?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "bật",
        'voice_off': "tắt",
        'voice_toggle': "Đầu ra giọng nói {0}",
        'voice_speed': "Tốc độ {0} phần trăm",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Không tìm thấy công cụ:\n{0}\n\nBASE_DIR: {1}\nĐảm bảo các công cụ PDF được cài đặt trong thư mục {1}.",
        'tool_started': "Đã khởi động {0}",
        'tool_start_failed': "Không thể khởi động",
        'process_error_failed_to_start': "Không thể khởi động tiến trình. Tệp có tồn tại không?",
        'process_error_crashed': "Tiến trình bị treo trong khi khởi động.",
        'process_error_timeout': "Đã đạt thời gian chờ tiến trình.",
        'process_error_write': "Lỗi ghi vào tiến trình.",
        'process_error_read': "Lỗi đọc từ tiến trình.",
        'process_error_unknown': "Lỗi tiến trình không xác định",
        'process_command': "Lệnh",
        'process_normal_exit': "kết thúc bình thường",
        'process_crashed': "bị treo",
        'process_nonzero_exit': "{0} kết thúc với mã lỗi {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Đang hủy...",
        'move_cancelling': "Đang hủy di chuyển",
        'opening_pdf': "Đang mở PDF...",
        'loading_document': "Đang tải tài liệu...",
        'pdf_opened': "Đã mở PDF",
        'pages_found_moving': "Đã tìm thấy {0} trang, {1} để di chuyển",
        'creating_backup': "Đang tạo bản sao lưu...",
        'backup_description': "Đang sao lưu tệp gốc...",
        'backup_saved_as': "Đã sao lưu dưới dạng: {0}",
        'error_format': "Lỗi: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Đã đặt lại tìm kiếm",
        'page_header_simple': "=== Trang {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Quản lý mật khẩu – Hướng dẫn",
        'password_guide_voice': "Hướng dẫn quản lý mật khẩu. Vui lòng đọc các lưu ý.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Quản lý mật khẩu – Hướng dẫn chi tiết</strong></p>

        <p><strong>1. Bảo vệ mật khẩu cho PDF</strong></p>
        <ul>
        <li>Khi mở PDF được bảo vệ bằng mật khẩu, một hộp thoại xuất hiện nơi bạn có thể nhập mật khẩu.</li>
        <li>Bạn có thể lưu mật khẩu đã mã hóa để không phải nhập lại mỗi lần (hộp kiểm "Lưu mật khẩu").</li>
        <li>Với nút "Xóa mật khẩu", bạn có thể tạo một bản sao đã giải mã của PDF và xóa mật khẩu khỏi cơ sở dữ liệu.</li>
        </ul>

        <p><strong>2. Mật khẩu chính</strong></p>
        <ul>
        <li>Mật khẩu chính bảo vệ quyền truy cập vào tất cả mật khẩu PDF đã lưu.</li>
        <li><strong>Thiết lập:</strong> Vào "Cài đặt → Quản lý mật khẩu → Cài đặt mật khẩu chính" và nhấp "Thiết lập mật khẩu chính". Chọn mật khẩu mạnh (ít nhất 8 ký tự).</li>
        <li><strong>Thay đổi:</strong> Sau khi xác thực thành công, bạn có thể thay đổi mật khẩu chính.</li>
        <li><strong>Xóa:</strong> Nếu bạn xóa mật khẩu chính, TẤT CẢ mật khẩu đã lưu sẽ bị xóa vĩnh viễn. Bạn có thể xuất bản sao lưu trước.</li>
        <li>Một lần mỗi phiên, bạn phải xác thực bằng mật khẩu chính để truy cập các chức năng được bảo vệ (ví dụ: xem mật khẩu).</li>
        </ul>

        <p><strong>3. Quản lý mật khẩu (danh sách)</strong></p>
        <ul>
        <li>Dưới "Cài đặt → Quản lý mật khẩu", bạn mở một bảng tất cả các PDF đã lưu với mật khẩu đã mã hóa của chúng.</li>
        <li><strong>Không có mật khẩu chính:</strong> Bạn chỉ có thể xóa các mục – mật khẩu vẫn bị ẩn.</li>
        <li><strong>Có mật khẩu chính (đã xác thực):</strong> Bạn có thể xem, sao chép, xuất và xóa mật khẩu.</li>
        <li><strong>Xuất:</strong> Chọn định dạng (JSON, CSV, TXT) và lưu danh sách. Nếu có mật khẩu chính, bạn có thể quyết định xem mật khẩu được xuất dưới dạng văn bản rõ hay vẫn được mã hóa.</li>
        <li><strong>Nhập:</strong> Một tệp ZIP đã xuất trước đó với tất cả cài đặt (bao gồm mật khẩu) có thể được nhập lại qua "Cài đặt → Xuất/nhập cài đặt". Chú ý: Dữ liệu hiện có sẽ bị ghi đè!</li>
        </ul>

        <p><strong>4. Trình tạo mật khẩu</strong></p>
        <ul>
        <li>Trong hộp thoại mật khẩu (ví dụ khi bảo vệ PDF), bạn sẽ thấy một nút xúc xắc 🎲 ở bên phải trường nhập.</li>
        <li>Nhấp vào nó để mở trình tạo mật khẩu. Bạn có thể đặt độ dài, bộ ký tự (chữ hoa, chữ thường, số, ký tự đặc biệt) và dấu phân cách để dễ đọc hơn.</li>
        <li>Mật khẩu được tạo có thể được áp dụng trực tiếp và sao chép nếu cần.</li>
        </ul>

        <p><strong>5. Lưu ý bảo mật quan trọng</strong></p>
        <ul>
        <li>Mật khẩu đã lưu được lưu trữ mã hóa với AES-256. Khóa được dẫn xuất từ mật khẩu chính của bạn (nếu có) hoặc từ một giá trị cố định (không có mật khẩu chính).</li>
        <li>Không có mật khẩu chính, mật khẩu vẫn được mã hóa, nhưng khóa được nhúng trong chương trình – kẻ tấn công có quyền truy cập vào tệp của bạn có thể giải mã chúng. Do đó chúng tôi khuyến nghị sử dụng mật khẩu chính.</li>
        <li>Cơ sở dữ liệu mật khẩu nằm trong thư mục `Data/passwords.json`. Hãy sao lưu thường xuyên, đặc biệt trước khi xóa mật khẩu chính.</li>
        <li>Nếu mất mật khẩu chính, tất cả mật khẩu đã lưu sẽ mất vĩnh viễn.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Chế độ đảo ngược",
        'invert_mode_classic': "Cổ điển (đảo ngược tất cả màu sắc)",
        'invert_mode_smart': "Thông minh (chỉ đảo ngược độ sáng)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Ngưỡng thang độ xám",
        'gray_threshold_10': "10% (nghiêm ngặt)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Mặc định)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (mềm)",
        'threshold_changed': "Đã đặt ngưỡng thành {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Ngưỡng thang độ xám – Giải thích",
        'threshold_guide_text': "Ngưỡng thang độ xám xác định pixel nào trong chế độ tối thông minh được coi là 'xám' và bị đảo ngược.\n\n"
                                "• Giá trị thấp (10%) chỉ đảo ngược các tông màu xám gần như hoàn hảo – các phần tử màu sắc được giữ nguyên hoàn toàn.\n"
                                "• Giá trị cao (50%) cũng đảo ngược các pixel hơi có màu – điều này làm tăng độ tương phản, nhưng có thể làm sai lệch màu sắc.\n\n"
                                "Giá trị tối ưu phụ thuộc vào tài liệu. Đối với tài liệu văn bản thuần túy, 30–40% thường là lý tưởng, đối với đồ họa màu thì nên dùng 10–20%.\n\n"
                                "Bạn có thể điều chỉnh giá trị bất cứ lúc nào qua menu 'Cài đặt' – PDF sẽ được tải lại ngay lập tức.\n\n"
                                "Lưu ý:\n* Ảnh và hình ảnh chỉ có thể hiển thị chính xác ở chế độ sáng!\n* Cài đặt đảo ngược chỉ hiển thị khi chế độ tối được kích hoạt.",
        'threshold_guide_voice': "Ngưỡng thang độ xám xác định mức độ can thiệp của chế độ tối thông minh. Giá trị thấp bảo toàn màu sắc, giá trị cao tăng độ tương phản.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Đang mở PDF...",
        'progress_loading_document': "Đang tải tài liệu...",
        'progress_pdf_opened': "Đã mở PDF",
        'progress_creating_backup': "Đang tạo bản sao lưu...",
        'progress_backup_description': "Đang bảo vệ tệp gốc...",
        'progress_backup_created': "Đã tạo bản sao lưu",
        'progress_backup_saved_as': "Đã lưu dưới tên: {0}",
        'progress_analyzing_start': "Bắt đầu phân tích...",
        'progress_searching_empty': "Đang tìm trang trống...",
        'progress_page_empty': "Trang {0} trống",
        'progress_page_keep': "Giữ trang {0}",
        'progress_analysis_complete': "Phân tích hoàn tất",
        'progress_empty_found': "Đã tìm thấy {0} trang trống",
        'progress_current_page': "Trang hiện tại",
        'progress_mark_delete': "Đang đánh dấu để xóa",
        'progress_range_selected': "Phạm vi trang {0}-{1}",
        'progress_deleting_pages': "Đang xóa {0} trang",
        'progress_creating_new_pdf': "Đang tạo PDF mới...",
        'progress_transferring_pages': "Đang truyền trang",
        'progress_keeping_page': "Trang {0} sẽ được giữ lại ({1}/{2})",
        'progress_saving_pdf': "Đang lưu PDF...",
        'progress_optimizing': "Đang tối ưu hóa kích thước tệp...",
        'progress_finalizing': "Đang hoàn thiện...",
        'progress_new_size': "Kích thước mới: {0:.2f} MB",
        'progress_cancelling': "Đang hủy...",
        'progress_cancel_message': "Đang hủy {0}",
        'progress_pages_found_moving': "Đã tìm thấy {0} trang, {1} để di chuyển",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Đang phân tích PDF...",
        'ocr_status_optimizing': "Đang tối ưu hóa hình ảnh...",
        'ocr_status_recognizing': "Đang nhận dạng văn bản...",
        'ocr_status_embedding': "Đang nhúng văn bản...",
        'ocr_status_finalizing': "Đang hoàn thiện PDF...",

        # PDF-Laden
        'progress_preparing': "Đang chuẩn bị...",
        'progress_loading': "Đang tải PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Đang xóa trang...",
        'progress_moving_title': "Đang di chuyển trang...",
        'pages_found': "Đã tìm thấy trang",
        'progress_creating_new_order': "Đang tạo thứ tự mới...",
        'progress_sorting_pages': "Đang sắp xếp trang...",
        'progress_moving_to_begin': "Di chuyển {0} trang lên đầu",
        'progress_transferring_count': "Truyền {0} trang",
        'progress_transferring_before_target': "Truyền trang trước mục tiêu",
        'progress_moving_pages': "Di chuyển {0} trang",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_sao_luu_",
        'filename_protected_suffix': "_bao_ve_",
        'filename_copy_suffix': "_BanSao",
        'filename_page_single': "_Trang_",
        'filename_page_range': "_CacTrang_",
        'filename_export_page': "_Trang_{0:03}",
        'filename_export_range': "_CacTrang_{0}-{1}",
        'filename_export_multiple': "_CacTrang_{0}",
        'filename_with_text': "_co_VanBan",
        'filename_with_signature': "_co_ChuKy",
        'filename_with_image': "_co_HinhAnh",
        'filename_with_forms': "_co_HinhDang",
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
        'view_toggle_navbar': "Hiển thị thanh nút",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Không thể xóa tất cả các trang",
		'pages_cannot_delete_last_page': 'Không thể xóa trang cuối cùng!',
		'pages_cannot_delete_all_pages': 'Phải còn lại ít nhất một trang trong tài liệu!',
		'delete_pages_confirm': 'Bạn có chắc chắn muốn xóa {0} trang?',
		'delete_pages_confirm_voice': 'Bạn có chắc chắn muốn xóa {0} trang?',
		'pages_deleted': 'Đã xóa thành công {0} trang.',
		'warning': 'Cảnh báo',
		'error': 'Lỗi',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Chưa chọn biểu mẫu",
        'form_customized': "Biểu mẫu đã được tùy chỉnh",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Chọn",
        'btn_use': "Sử dụng",
        'master_password_for_spasswords': "Để lưu trữ và sử dụng mật khẩu, trước tiên bạn cần thiết lập mật khẩu chính.\n\nBạn có muốn thiết lập mật khẩu chính ngay bây giờ không?",
        'open_saved_dialog_title': "Mở tệp đã lưu",
        'open_saved_question': "Bạn có muốn mở tệp đã lưu ngay bây giờ không?",
        'password': "Mật khẩu",
        'password_manager_master_required': "Trình quản lý mật khẩu chỉ khả dụng nếu mật khẩu chính đã được thiết lập.\n\nBạn có muốn thiết lập mật khẩu chính ngay bây giờ không?",
        'password_master_required_for_select': "Để xem và chọn mật khẩu đã lưu, trước tiên bạn phải xác thực bằng mật khẩu chính của mình.\n\nBạn có muốn xác thực ngay bây giờ không?",
        'password_not_available': "Mật khẩu đã chọn không khả dụng hoặc không thể giải mã.",
        'password_options_title': "Tùy chọn mật khẩu",
        'password_save_choice_change': "Đặt mật khẩu mới",
        'password_save_choice_keep': "Sử dụng mật khẩu hiện có",
        'password_save_choice_none': "Lưu không mã hóa",
        'password_save_hint': "Trước tiên hãy thiết lập mật khẩu chính để lưu trữ mật khẩu một cách an toàn.",
        'password_save_master_required': "Lưu mật khẩu (chỉ có thể với mật khẩu chính)",
        'password_save_question': "PDF hiện tại được bảo vệ bằng mật khẩu. Bạn có muốn sử dụng mật khẩu hiện có, đặt mật khẩu mới hay lưu không mã hóa?",
        'password_select': "Chọn mật khẩu",
        'password_select_none': "Không có mật khẩu nào được chọn.\n\nVui lòng chọn mật khẩu từ danh sách.",
        'password_select_one': "Vui lòng chọn chính xác một mật khẩu.\n\nBạn đã đánh dấu nhiều mật khẩu.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_sao_luu",
        'filename_insert_suffix': "_co_chen",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_trang_da_xoa",
        'filename_pages_moved': "_trang_da_di_chuyen",
        'filename_rotated_all_suffix': "_tat_ca_trang_da_xoay",
        'filename_rotated_suffix': "_trang_da_xoay",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Cấu hình tên tệp khi thay đổi PDF",
        'filename_keep_suffixes': "Giữ lại các phần mở rộng trước đó (ví dụ: _co_van_ban)",
        'filename_keep_suffixes_false': "Thay thế",
        'filename_keep_suffixes_true': "Giữ lại",
        'filename_preview_label': "Xem trước tên tệp:",
        'filename_preview_overwrite_hint': "Không có bản xem trước – tệp gốc sẽ bị ghi đè.",
        'filename_separator': "Dấu phân cách giữa các từ",
        'filename_separator_none': "Không có dấu phân cách",
        'filename_separator_space': "Khoảng trắng ( )",
        'filename_separator_underscore': "Gạch dưới (_)",
        'filename_settings_saved': "Đã lưu cài đặt tên tệp",
        'filename_settings_title': "Định dạng tên tệp và sao lưu",
        'filename_timestamp_position': "Vị trí của dấu thời gian",
        'filename_timestamp_position_after': "Sau tên cơ sở",
        'filename_timestamp_position_before': "Ở phía trước",
        'filename_timestamp_position_end': "Ở cuối",
        'filename_use_timestamp': "Sử dụng dấu thời gian",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Hành vi khi thay đổi:</b><ul><li>Xóa và chèn trang</li><li>Chèn văn bản, chữ ký, hình ảnh và hình dạng</li><li>OCR</li></ul></html>",
        'backup_section': "Sao lưu cho các thao tác trang (Xóa, Di chuyển)",
        'behavior_info': "Lưu ý: Với 'Ghi đè bản gốc', dấu thời gian và hậu tố bị bỏ qua – tệp giữ nguyên tên của nó.",
        'behavior_new_file': "Luôn tạo tệp mới (có dấu thời gian và hậu tố)",
        'behavior_overwrite': "Ghi đè bản gốc (không có tệp mới)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Tất cả các trang đã được xoay.\n\nBản gốc không thay đổi.\nTệp mới: {0}",
        'all_pages_rotated_voice': "Tất cả các trang đã được xoay, tệp mới được tạo.",
        'empty_pages_deleted_new_file': "{0} trang trống đã bị xóa.\n\nBản gốc không thay đổi.\nTệp mới: {1}",
        'empty_pages_deleted_voice': "{0} trang trống đã bị xóa, tệp mới được tạo.",
        'ocr_keep_original': "Giữ bản gốc (mở thủ công sau)",
        'ocr_new_file_question': "PDF mới có thể tìm kiếm đã được lưu tại:\n{0}\n\nBạn có muốn mở nó ngay bây giờ không?",
        'ocr_open_new': "Mở tệp OCR mới",
        'ocr_original_kept': "Tệp gốc vẫn mở. Tệp OCR đã được lưu.",
        'page_deleted_new_file': "Trang {0} đã bị xóa.\n\nBản gốc không thay đổi.\nTệp mới: {1}",
        'page_deleted_voice': "Trang {0} đã bị xóa, tệp mới được tạo.",
        'page_rotated_new_file': "Trang {0} đã được xoay.\n\nBản gốc không thay đổi.\nTệp mới: {1}",
        'page_rotated_voice': "Trang {0} đã được xoay, tệp mới được tạo.",
        'pages_deleted_new_file': "Đã xóa {0} trang.\n\nTệp gốc không thay đổi.\nTệp mới: {1}",
        'pages_deleted_new_file_voice': "{0} trang đã bị xóa, tệp mới được tạo.",
        'pages_inserted_new_file': "Đã chèn {0} trang.\n\nTệp gốc không thay đổi.\nTệp mới: {1}",
        'pages_inserted_new_file_ask': "Đã chèn {0} trang.\n\nBản gốc không thay đổi.\nTệp mới: {1}\n\nBạn có muốn mở nó ngay bây giờ không?",
        'pages_inserted_voice_new': "{0} trang đã được chèn, tệp mới được tạo.",
        'pages_moved_new_file': "Đã di chuyển {0} trang.\n\nTệp gốc không thay đổi.\nTệp mới: {1}",
        'pages_moved_new_file_voice': "{0} trang đã được di chuyển, tệp mới được tạo.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Không hiển thị lại",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Cài đặt sao lưu</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Sao lưu BẬT</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Đối với tất cả các thay đổi ghi đè bản gốc</strong> (văn bản, chữ ký, hình ảnh, hình dạng, OCR, xoay, chèn, xóa/di chuyển trang) <strong>tự động tạo bản sao lưu có dấu thời gian</strong> trước khi áp dụng thay đổi.</p>
                <p style="margin: 5px 0 5px 20px;">• Bản sao lưu nằm bên cạnh tệp gốc (ví dụ: <code>TaiLieu_sao_luu_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Nếu bạn đã bật thêm tùy chọn <strong>„Ghi đè bản gốc“</strong>, cũng được tạo bản sao lưu.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Sao lưu TẮT</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Không có bản sao lưu nào được tạo</strong> – cả khi ghi đè cũng như khi thao tác trang.</p>
                <p style="margin: 5px 0 5px 20px;">• Tệp gốc có thể bị mất vĩnh viễn khi bị ghi đè.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Chỉ được khuyến nghị cho người dùng có kinh nghiệm!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Mẹo:</strong> Cài đặt sao lưu độc lập với tùy chọn „Ghi đè bản gốc“. Bạn có thể kết hợp cả hai.<br>
                Bạn có thể ẩn vĩnh viễn thông báo này.
            </div>
        </div>
        """,
        'backup_info_title': "Hành vi sao lưu",
        'backup_info_voice': "Thông báo về hành vi sao lưu khi thao tác trang. Sao lưu BẬT ghi đè bản gốc, TẮT tạo tệp mới.",
        'show_backup_info': "Thông tin về cài đặt sao lưu",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Không hiển thị lại",
        'overwrite_enable_backup': "Bật sao lưu (khuyến nghị)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Ghi đè bản gốc</p>
            <p>Nếu bạn bật tùy chọn này, các thay đổi (văn bản, chữ ký, hình ảnh, hình dạng, OCR, xoay, chèn) được <strong>lưu trực tiếp vào bản gốc</strong> – <strong>không có tệp mới nào được tạo</strong>.</p>
            <p>• Tên tệp không thay đổi.<br>
            • Dấu thời gian và hậu tố bị bỏ qua.<br>
            • <strong>Nếu không có sao lưu, bản gốc có thể bị mất vĩnh viễn.</strong></p>
            <p style="color: #FFD700;">Khuyến nghị: Bật thêm tùy chọn sao lưu để có bản sao an toàn tự động.</p>
        </div>
        """,
        'overwrite_info_title': "Ghi đè bản gốc",
        'overwrite_info_voice': "Cảnh báo: Ghi đè bản gốc – không có tệp mới. Nên sao lưu.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Đã chèn {0} trang.\n\nTệp gốc đã bị ghi đè.\nMột bản sao lưu đã được tạo.",
        'pages_inserted_overwrite_no_backup': "Đã chèn {0} trang.\n\nTệp gốc đã bị ghi đè.\nKHÔNG có bản sao lưu nào được tạo.",
        'texts_saved_overwrite_with_backup': "Các thay đổi đã được lưu trong bản gốc.\n\nMột bản sao lưu đã được tạo.",
        'texts_saved_overwrite_no_backup': "Các thay đổi đã được lưu trong bản gốc.\n\nKHÔNG có bản sao lưu nào được tạo.",
        'texts_crosses_saved_new_file': "{0} {1} và {2} {3} đã được chèn.\n\nTệp gốc không thay đổi.\nMột tệp mới đã được tạo.\n\nĐang tải PDF mới...",
        'texts_saved_new_file': "{0} {1} đã được chèn.\n\nTệp gốc không thay đổi.\nMột tệp mới đã được tạo.\n\nĐang tải PDF mới...",
        'crosses_saved_new_file': "{0} {1} đã được chèn.\n\nTệp gốc không thay đổi.\nMột tệp mới đã được tạo.\n\nĐang tải PDF mới...",
        'elements_saved_new_file': "{0} phần tử đã được chèn.\n\nTệp gốc không thay đổi.\nMột tệp mới đã được tạo.\n\nĐang tải PDF mới...",
        'signatures_saved_overwrite_with_backup': "(Các) chữ ký đã được lưu trong bản gốc.\n\nMột bản sao lưu đã được tạo.",
        'signatures_saved_overwrite_no_backup': "(Các) chữ ký đã được lưu trong bản gốc.\n\nKHÔNG có bản sao lưu nào được tạo.",
        'images_saved_overwrite_with_backup': "(Các) hình ảnh đã được lưu trong bản gốc.\n\nMột bản sao lưu đã được tạo.",
        'images_saved_overwrite_no_backup': "(Các) hình ảnh đã được lưu trong bản gốc.\n\nKHÔNG có bản sao lưu nào được tạo.",
        'forms_saved_overwrite_with_backup': "(Các) hình dạng đã được lưu trong bản gốc.\n\nMột bản sao lưu đã được tạo.",
        'forms_saved_overwrite_no_backup': "(Các) hình dạng đã được lưu trong bản gốc.\n\nKHÔNG có bản sao lưu nào được tạo.",
        'signatures_saved_new_file': "{0} chữ ký đã được chèn.\n\nTệp gốc không thay đổi.\nMột tệp mới đã được tạo.\n\nĐang tải PDF mới...",
        'images_saved_new_file': "{0} hình ảnh đã được chèn.\n\nTệp gốc không thay đổi.\nMột tệp mới đã được tạo.\n\nĐang tải PDF mới...",
        'forms_saved_new_file': "{0} hình dạng đã được chèn.\n\nTệp gốc không thay đổi.\nMột tệp mới đã được tạo.\n\nĐang tải PDF mới...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Cảnh báo: PDF này chứa các trang đã bị xoay. Vị trí có thể sai lệch.",
        'page_rotated_warning_title': "Đã phát hiện trang bị xoay",
        'page_rotated_warning_message': "Trang hiện tại {0} đã bị xoay {1}°.\n\nChèn phần tử trên các trang bị xoay không được hỗ trợ.\n\nBạn có muốn xoay trang về vị trí thẳng đứng ngay bây giờ không?",
        'page_rotated_warning_voice': "Cảnh báo: Trang đã bị xoay. Vui lòng xoay nó trước.",
        'paste_on_rotated_page_simple_warning': "Không thể chèn trên trang {0}!\n\nTrang này đã bị xoay {1}°.\n\nVui lòng xoay trang về 0° trước (Menu: Chỉnh sửa → Căn chỉnh trang).\n\nCảnh báo:\nPhần tử đã sao chép trước đó sẽ bị mất nếu bạn không lưu trước khi xoay trang.",
        'paste_on_rotated_page_voice': "Đã hủy chèn. Trang đã bị xoay. Vui lòng căn chỉnh trang trước.",
        'page_rotated_cancel': "Hủy",
        'page_rotated_rotate_until_upright': "Xoay trang nhiều lần (cho đến khi thẳng đứng)",
        'page_rotated_now_upright': "Trang bây giờ đã thẳng đứng. Bạn có thể chèn ngay bây giờ.",
        'page_rotated_still_not_upright': "Không thể xoay trang về vị trí thẳng đứng. Vui lòng sửa thủ công.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Trợ giúp: Sửa các trang bị xoay",
        'help_rotated_pages_voice': "Đang mở trợ giúp để sửa các trang bị xoay.",
        'btn_help': "Trợ giúp",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Vấn đề: Trang bị xoay – Chèn không hoạt động chính xác</p>

            <p>Nếu chèn văn bản, chữ ký hoặc hình dạng trên trang bị xoay không hoạt động chính xác, bạn có thể sửa trang bằng trình chỉnh sửa PDF bên ngoài.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Giải pháp với công cụ bên ngoài (ví dụ: macOS Xem trước)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Xuất trang</strong><br>
                &nbsp;&nbsp;Nhấp vào menu <strong>Tệp → Xuất dưới dạng trang</strong> hoặc sử dụng phương pháp khác để lưu trang mong muốn dưới dạng PDF duy nhất.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Mở trang trong chương trình bên ngoài</strong><br>
                &nbsp;&nbsp;Mở PDF đã xuất trong trình chỉnh sửa PDF (ví dụ: <strong>macOS Xem trước</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Xoay trang</strong><br>
                &nbsp;&nbsp;Xoay trang sao cho thẳng đứng (trong Xem trước: <strong>Công cụ → Xoay</strong> hoặc <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Lưu</strong><br>
                &nbsp;&nbsp;Lưu trang đã sửa (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Chèn lại trang vào tài liệu gốc</strong><br>
                &nbsp;&nbsp;Quay lại PDFDarkView và chèn trang đã sửa tại vị trí mong muốn:<br>
                &nbsp;&nbsp;<strong>Chỉnh sửa → Chèn trang</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Phương án thay thế: Xoay trang trong bản gốc</p>
                <p style="margin: 5px 0 5px 20px;">• Sử dụng chức năng xoay tích hợp sẵn (<strong>Chỉnh sửa → Xoay trang</strong>) để sửa trang từng bước.<br>
                • Sau mỗi lần xoay, bạn có thể kiểm tra xem chèn đã hoạt động chưa.<br>
                • Đây thường là giải pháp nhanh hơn – hãy thử trước!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Mẹo:</strong> Nếu bạn thường xuyên gặp các trang bị xoay, bạn có thể ẩn vĩnh viễn cảnh báo trong hộp thoại chèn.<br>
                Vị trí sau đó có thể sai lệch – chỉ sử dụng tùy chọn này nếu bạn biết hậu quả.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Căn chỉnh trang",
        'menu_rotate_normalize_tooltip': "Xoay trang hoặc đặt lại về 0°",
        'normalize_current_page': "Đưa trang hiện tại về vị trí thẳng đứng (đặt thành 0°)",
        'normalize_all_pages': "Đưa tất cả các trang về vị trí thẳng đứng (đặt thành 0°)",
        'page_normalized': "Trang {0} đã được đặt ở vị trí thẳng đứng.",
        'all_pages_normalized': "Tất cả các trang đã được đặt ở vị trí thẳng đứng.",
        'page_already_upright': "Trang {0} đã thẳng đứng.",
        'all_pages_already_upright': "Tất cả các trang đã thẳng đứng.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF không chứa văn bản có thể tìm kiếm.</p><p>Bạn có muốn thực hiện OCR để xuất sang {0} không?</p>",
        'export_ocr_voice': "PDF không chứa văn bản. Cần OCR để xuất sang {0}.",
        'export_no_ocr_possible': "Không thể xuất mà không có OCR. Vui lòng thực hiện OCR qua menu.",
        'ocr_failed_export_not_possible': "OCR thất bại. Không thể thực hiện xuất.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF sẽ mở trong Xem trước. Vui lòng bắt đầu quá trình in ở đó.",
        'print_preview_manual': "PDF đã được mở. Vui lòng thực hiện lệnh in thủ công (ví dụ: Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Hợp nhất PDF",
        'merge_pdfs': "Hợp nhất PDF",
        'merge_progress_title': "Đang hợp nhất PDF...",
        'merge_pdfs_list': "PDF theo thứ tự (Kéo và thả để sắp xếp)",
        'merge_add_pdf': "Thêm PDF",
        'merge_remove': "Xóa",
        'merge_move_up': "Lên",
        'merge_move_down': "Xuống",
        'merge_pdfs_info': "💡 Mẹo: Bạn có thể thay đổi thứ tự bằng cách kéo và thả",
        'merge_no_pdfs': "Không có PDF nào được chọn. Nhấp vào 'Thêm PDF'.",
        'merge_info': "Đã chọn {0} PDF (khoảng {1} trang)",
        'merge_open_file': "Mở tệp",
        'merge_merge': "Hợp nhất",
        'merge_error': "Lỗi khi hợp nhất",
        'merge_min_two_pdfs_error': "Vui lòng chọn ít nhất hai tệp PDF để hợp nhất.",
        'merge_select_pdfs': "Chọn PDF để hợp nhất",
        'merge_error_file': "Lỗi khi xử lý",
        'merge_cancelled': "Việc hợp nhất đã bị hủy",
        'merge_preparing': "Đang chuẩn bị...",
        'merge_processing': "Đang xử lý PDF {0} trên {1}",
        'merge_saving': "Đang lưu PDF đã hợp nhất...",
        'merge_complete': "Hoàn tất!",
        'merge_success_title': "Hợp nhất thành công",
        'merge_success_voice': "{0} PDF đã được hợp nhất thành công.",
        'merge_success_message': "{0} PDF đã được hợp nhất thành công.\n\nTài liệu mới hiện có {1} trang.\n\nTệp mới:\n{2}\n\nVị trí lưu:\n{3}\n{2}\n\nBạn có muốn mở PDF này không?",
        'replace_file_title': "Thay thế tệp?",
        'replace_file_message': "Đã có một PDF đang mở. Bạn có muốn thay thế nó bằng tệp mới không?",
        'btn_yes': "Có",
        'btn_no': "Không",
        'filename_merge_suffix': "đã_hợp_nhất",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Đang mở {0}...",
        'progress_merge_reading': "Đang đọc {0}...",
        'progress_merge_adding': "Đang thêm {0} trang...",
        'progress_merge_optimizing': "Đang tối ưu hóa PDF...",
        'progress_merge_writing': "Đang ghi PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "đóng PDF",
        'action_close_window': "đóng cửa sổ",
        'action_open_new_pdf': "mở một PDF mới",
        'action_quit_app': "thoát ứng dụng",
        'changes_saved': "Các thay đổi đã được lưu.",
        'file_close_title': "Đóng tệp PDF",
        'save_before_action': "Có nên lưu các thay đổi trước khi {0} không? Có hoặc Không?",
        'save_before_action_voice': "Có nên lưu các thay đổi trước khi {0} không? Có hoặc Không?",
        'save_before_close_question': "Có nên lưu các thay đổi trước khi đóng không? Có hoặc Không?",


        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Đã tạo PDF có thể tìm kiếm:\n\n{0}\n\n<b>thử lại nếu cần",
        "ocr_rotate_title": "Căn chỉnh trang trước khi OCR",
        "ocr_rotate_question": "PDF chứa các trang bị xoay.\nBạn có muốn căn chỉnh tất cả các trang về 0° trước khi OCR không?\nĐiều này cải thiện đáng kể khả năng nhận dạng văn bản.",
        "ocr_rotate_yes": "Có, căn chỉnh",
        "ocr_rotate_no": "Không, bắt đầu OCR ngay",
        "ocr_rotate_voice": "PDF chứa các trang bị xoay. Có nên căn chỉnh tất cả các trang trước khi OCR không?",
        "ocr_not_performed_message": "Không có văn bản. Vui lòng thực hiện OCR (menu \"Chỉnh sửa\" → \"Thực hiện OCR\" hoặc phím Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Cài đặt OCR",
        "ocr_language_btn": "Chọn ngôn ngữ OCR",
        "ocr_language": "Ngôn ngữ OCR",
        "ocr_language_current": "Ngôn ngữ hiện tại:",
        "ocr_param_info": "Thông tin về tham số",

        "ocr_force_ocr_label": "Buộc OCR",
        "ocr_deskew_label": "Sửa độ nghiêng",
        "ocr_clean_label": "Làm sạch hình ảnh",
        "ocr_oversample_label": "Độ phân giải (DPI)",
        "ocr_pagesegmode_label": "Phân chia trang",
        "ocr_oem_label": "Chế độ động cơ OCR",
        "ocr_optimize_label": "Nén PDF",
        "ocr_jobs_label": "Quy trình song song",
        "ocr_verbose_label": "Chi tiết nhật ký",

        "ocr_force_ocr_tooltip": "Buộc OCR trên mọi trang, ngay cả khi văn bản đã tồn tại",
        "ocr_deskew_tooltip": "Tự động căn chỉnh các bản quét bị nghiêng",
        "ocr_clean_tooltip": "Loại bỏ nhiễu và các tạo tác khỏi hình ảnh",
        "ocr_oversample_tooltip": "Phóng to hình ảnh trước khi OCR lên DPI này",
        "ocr_pagesegmode_tooltip": "Xác định cách trang được chia thành các vùng văn bản",
        "ocr_oem_tooltip": "Chọn động cơ OCR của Tesseract",
        "ocr_optimize_tooltip": "Mức độ nén của PDF đầu ra",
        "ocr_jobs_tooltip": "Số lượng quy trình OCR song song",
        "ocr_verbose_tooltip": "Mức độ chi tiết của đầu ra nhật ký",
        "ocr_settings_explain_btn": "Giải thích",

        "ocr_force_ocr_explain": "Buộc nhận dạng văn bản trên <b>mọi</b> trang, ngay cả khi trang đó đã chứa văn bản.\n\nKhuyến nghị: <b>Bật</b> cho PDF được quét, <b>Tắt</b> cho PDF gốc có văn bản đã tồn tại.",

        "ocr_deskew_explain": "Sửa các bản quét hơi bị nghiêng (lên đến khoảng 5°).\n\nKhuyến nghị: <b>Bật</b> cho tài liệu được quét, <b>Tắt</b> nếu các trang đã thẳng hoàn hảo.",

        "ocr_clean_explain": "Loại bỏ nhiễu, dấu chấm và các tạo tác nhỏ khỏi hình ảnh.\n<b>QUAN TRỌNG:</b> Đối với văn bản tiếng Ả Rập, Thái Lan hoặc Việt Nam có dấu phụ (chấm trên/dưới chữ cái), tùy chọn này nên được <b>tắt</b>, nếu không các ký tự quan trọng có thể bị mất.",

        "ocr_oversample_explain": "Phóng to hình ảnh <b>trước khi</b> nhận dạng văn bản lên DPI được chỉ định.<br><br>• <b>72-150 DPI:</b> Rất nhanh, nhưng tỷ lệ nhận dạng thấp<br>• <b>200-300 DPI:</b> Phạm vi tối ưu (Mặc định: 300)<br>• <b>400+ DPI:</b> Hầu như không nhận dạng tốt hơn, nhưng tệp lớn hơn đáng kể<br><br>Khuyến nghị: 300 DPI cho chữ viết phức tạp (Ả Rập, Trung Quốc, Nhật Bản), 200 DPI cho ngôn ngữ phương Tây.",

        "ocr_pagesegmode_explain": "Xác định cách Tesseract chia trang thành các vùng văn bản.\n\n• <b>3 - Tự động (Mặc định):</b> Tốt cho bố cục hỗn hợp\n• <b>4 - Một cột:</b> Cho văn bản một cột\n• <b>5 - Khối dọc:</b> Cho chữ viết dọc (Nhật Bản, Trung Quốc)\n• <b>6 - Khối văn bản đồng nhất:</b> Tối ưu cho văn bản chảy không có cột\n• <b>11 - Hình ảnh thô:</b> Cho bản quét kém / chữ viết tay\n\nKhuyến nghị: <b>6</b> cho tài liệu văn bản đơn giản, <b>3</b> cho bố cục phức tạp.",

        "ocr_oem_explain": "Chọn động cơ OCR của Tesseract.\n\n• <b>0 - Legacy:</b> Động cơ cũ (nhanh, nhưng kém chính xác)\n• <b>1 - LSTM:</b> Động cơ thần kinh (chậm hơn, nhưng chính xác hơn)\n• <b>2 - Legacy + LSTM:</b> Kết hợp cả hai kết quả\n• <b>3 - Mặc định (LSTM ưu tiên):</b> Lựa chọn tốt nhất cho hầu hết các trường hợp\n\nKhuyến nghị: <b>3</b> để có độ chính xác nhận dạng tối đa.",

        "ocr_optimize_explain": "Nén PDF đầu ra.\n\n• <b>0:</b> Không tối ưu hóa (xử lý nhanh nhất)\n• <b>1:</b> Tối ưu hóa nhẹ (thỏa hiệp tốt)\n• <b>2:</b> Tối ưu hóa vừa phải\n• <b>3:</b> Tối ưu hóa mạnh (tệp nhỏ nhất, nhưng chậm hơn)\n\nKhuyến nghị: <b>1</b> cho sử dụng hàng ngày.",

        "ocr_jobs_explain": "Số lượng quy trình song song cho OCR.\n\n• <b>1:</b> Chậm, nhưng tiêu thụ bộ nhớ thấp nhất\n• <b>4-8:</b> Tối ưu cho bộ vi xử lý đa lõi hiện đại\n• <b>12+:</b> Hầu như không xử lý nhanh hơn với mức sử dụng bộ nhớ cao\n\nKhuyến nghị: Số lõi CPU (ví dụ <b>4</b> trên hệ thống 4 lõi).",

        "ocr_verbose_explain": "Mức độ chi tiết của đầu ra nhật ký trong bảng điều khiển.\n\n• <b>0:</b> Không có đầu ra\n• <b>1:</b> Tiến trình và thông báo trạng thái\n• <b>2:</b> Đầu ra chi tiết\n• <b>3:</b> Đầu ra gỡ lỗi đầy đủ (rất rộng)\n\nKhuyến nghị: <b>1</b> cho hoạt động bình thường.",

        "ocr_reset_title": "Đã đặt lại cài đặt",
        "ocr_reset_message": "Tất cả cài đặt OCR đã được đặt lại về giá trị mặc định.",
        "info_tooltip": "Thêm thông tin về tham số này",
        "ocr_reset_defaults": "Đặt lại về mặc định",

        "ocr_psm_0": "Tự động (động cơ Legacy)",
        "ocr_psm_1": "Phát hiện cột tự động",
        "ocr_psm_3": "Tự động (Mặc định)",
        "ocr_psm_4": "Một cột",
        "ocr_psm_5": "Khối dọc",
        "ocr_psm_6": "Khối văn bản đồng nhất",
        "ocr_psm_7": "Một dòng văn bản",
        "ocr_psm_8": "Một từ",
        "ocr_psm_11": "Hình ảnh thô (không phân tích bố cục)",

        "ocr_oem_0": "Động cơ Legacy (nhanh)",
        "ocr_oem_1": "Động cơ LSTM (thần kinh, chính xác)",
        "ocr_oem_2": "Legacy + LSTM kết hợp",
        "ocr_oem_3": "Mặc định (LSTM ưu tiên)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Ngôn ngữ OCR...",
        "ocr_language_title": "Chọn ngôn ngữ OCR",
        "ocr_language_instruction": "Chọn ngôn ngữ để nhận dạng văn bản (OCR).\nLưu ý: Nhiều ngôn ngữ sẽ ảnh hưởng đến hiệu suất và độ chính xác!\nBạn đạt được kết quả tốt nhất nếu chỉ chọn một ngôn ngữ.",
        "ocr_language_predefined": "Kết hợp được xác định trước",
        "ocr_language_custom": "Tùy chỉnh...",
        "ocr_language_selected": "Ngôn ngữ OCR đã chọn",
        "ocr_language_changed": "Đã thay đổi ngôn ngữ OCR thành {0}",
        "ocr_language_auto_detect": "Các ngôn ngữ có sẵn được phát hiện tự động.",
        "ocr_language_none_found": "Không tìm thấy dữ liệu ngôn ngữ Tesseract! Vui lòng cài đặt gói ngôn ngữ (ví dụ 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Lựa chọn ngôn ngữ tùy chỉnh",
        "ocr_language_available": "Các ngôn ngữ có sẵn (đã cài đặt):",
        "ocr_language_select_hint": "Chọn một hoặc nhiều ngôn ngữ:",
        "ocr_language_confirm": "Áp dụng",
        "ocr_language_reset": "Đặt lại về mặc định (deu+eng+vie)",
        "ocr_language_priorities": "Ngôn ngữ được khuyến nghị (đã cài đặt sẵn):",

        "select_all_languages": "Chọn tất cả",
        "clear_all_languages": "Xóa lựa chọn",
        "install_language_packs": "Cài đặt gói ngôn ngữ bị thiếu...",
        "install_hint": "💡 Mẹo: Không phải tất cả các ngôn ngữ đều được cài đặt trên hệ thống của bạn. Thông qua nút này, bạn sẽ nhận được trợ giúp cài đặt.",
        "ocr_language_install_title": "Cài đặt gói ngôn ngữ Tesseract",

        "ocr_missing_languages": "Thiếu gói ngôn ngữ OCR",
        "ocr_missing_languages_message": "Các ngôn ngữ đã chọn sau đây không được cài đặt trên hệ thống của bạn:\n\n{0}\n\nVui lòng cài đặt các gói ngôn ngữ bị thiếu (xem trợ giúp trong 'Trợ giúp cài đặt').\n\nBạn có muốn mở trợ giúp cài đặt ngay bây giờ không?",
        "ocr_missing_languages_voice": "Thiếu gói ngôn ngữ. Vui lòng cài đặt các ngôn ngữ bị thiếu.",
        "ocr_install_help_now": "Mở trợ giúp",
        "ocr_continue_anyway": "Vẫn thử",
        "ocr_language_error_title": "Lỗi ngôn ngữ OCR",
        "ocr_language_error_message": "Lỗi trong quá trình nhận dạng văn bản: {0}\n\nVui lòng kiểm tra cài đặt ngôn ngữ OCR của bạn (Cài đặt → Ngôn ngữ OCR).",
        "ocr_install_help_button": "Trợ giúp cài đặt",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Cài đặt gói ngôn ngữ Tesseract</p>

        <p>Để OCR hoạt động bằng một ngôn ngữ cụ thể, dữ liệu ngôn ngữ tương ứng phải được cài đặt trên hệ thống của bạn. Làm theo hướng dẫn cho hệ điều hành của bạn:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Mở <strong>Terminal</strong> (Finder → Chương trình → Tiện ích → Terminal).</li>
        <li>Cài đặt tất cả các ngôn ngữ có sẵn với:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Việc này có thể mất vài phút.)</li>
        <li>Hoặc chỉ các ngôn ngữ riêng lẻ (ví dụ tiếng Việt):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Với các phiên bản Homebrew hiện tại, có thể cần tải xuống <code>*.traineddata</code> theo cách thủ công (xem bên dưới).</li>
        <li>Sau khi cài đặt: Đóng hộp thoại này và mở lại lựa chọn ngôn ngữ OCR – các ngôn ngữ mới sẽ xuất hiện tự động.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Mở terminal (Ctrl+Alt+T).</li>
        <li>Cài đặt ngôn ngữ mong muốn, ví dụ cho tiếng Việt:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Mã ngôn ngữ quan trọng: <code>deu</code> (Đức), <code>eng</code> (Anh), <code>vie</code> (Việt), <code>spa</code> (Tây Ban Nha), <code>fra</code> (Pháp), <code>ita</code> (Ý), <code>nld</code> (Hà Lan), <code>fin</code> (Phần Lan), <code>swe</code> (Thụy Điển), <code>nor</code> (Na Uy).</li>
        <li>Hiển thị tất cả các gói có sẵn:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (thủ công)</p>
        <ol>
        <li>Tải xuống các tệp <code>*.traineddata</code> mong muốn từ:<br>
        <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (ví dụ <code>vie.traineddata</code> cho tiếng Việt).</li>
        <li>Sao chép các tệp vào thư mục ngôn ngữ của Tesseract, thường là:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Điều chỉnh theo cài đặt cá nhân.)</li>
        <li>Khởi động lại ứng dụng (hoặc mở lại lựa chọn ngôn ngữ OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Giải pháp thay thế cho tất cả các hệ thống</p>
        <ul>
        <li>Cài đặt <strong>OCRmyPDF</strong> và <strong>Tesseract</strong> với trình quản lý gói theo lựa chọn của bạn. Hầu hết các bản cài đặt đều có sẵn một số ngôn ngữ tiêu chuẩn (Anh, Đức, Pháp).</li>
        <li>Các ngôn ngữ bị thiếu có thể được cài đặt bất cứ lúc nào – lựa chọn ngôn ngữ OCR chỉ liệt kê các ngôn ngữ thực sự tồn tại.</li>
        </ul>

        <hr>
        <p><b>✅ Sau khi cài đặt:</b> Không cần khởi động lại ứng dụng – các ngôn ngữ mới được thêm vào sẽ xuất hiện ngay trong danh sách.</p>
        <p><b>📖 Trợ giúp về mã ngôn ngữ:</b> Có thể tìm thấy danh sách đầy đủ trong <a style="color:#E0E0E0;" href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">tài liệu Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Phông chữ Noto Sans",
        "info_noto_font_voice": "Hướng dẫn cài đặt phông chữ Noto Sans",
        "btn_info_noto_font_install": "Thông tin phông chữ",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Cách cài đặt phông chữ Noto miễn phí của Google</h2>

        <p><strong>Phông chữ Noto</strong> là một họ phông chữ mã nguồn mở của Google. Mục tiêu của chúng là không nhìn thấy <em>"tofu"</em> (tức là không có ô trống □) và hiển thị chính xác mọi ký tự từ tiêu chuẩn Unicode. Chúng là sự bổ sung lý tưởng cho các ứng dụng cần hiển thị văn bản bằng nhiều ngôn ngữ khác nhau.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Cài đặt trên macOS</h3>

        <p><strong>Phương pháp 1: Dùng Homebrew (dành cho người dùng nâng cao)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Phương pháp 2: Thông qua "Font Book" (Được khuyến nghị)</strong></p>

        <ol>
        <li>Tải xuống gói phông chữ chính thức:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Giải nén tệp ZIP</li>
        <li>Sao chép các tệp vào <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Cài đặt trên Windows (10 & 11)</h3>

        <p><strong>Phương pháp 1: Microsoft Store (Được khuyến nghị)</strong><br>
        Tìm kiếm "Google Noto Fonts" hoặc "Noto Sans" và nhấp vào <strong>Cài đặt</strong>.</p>

        <p><strong>Phương pháp 2: Cài đặt thủ công</strong></p>

        <ol>
        <li>Tải xuống:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Giải nén ZIP</li>
        <li>Chọn các tệp .ttf / .otf</li>
        <li>Nhấp chuột phải → <strong>Cài đặt</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        hoặc<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Tên\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Cài đặt trên Linux</h3>

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

        <p>Xác minh:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Quản lý dấu trang",
        "bookmark_add": "Thêm dấu trang",
        "bookmark_add_tooltip": "Lưu trang hiện tại làm dấu trang",
        "bookmark_remove": "Xóa dấu trang",
        "bookmark_remove_tooltip": "Xóa dấu trang đã đánh dấu",
        "bookmark_remove_all": "Xóa tất cả",
        "bookmark_remove_all_tooltip": "Xóa tất cả dấu trang của PDF này",
        "bookmark_jump": "Đi đến dấu trang",
        "bookmark_jump_tooltip": "Đi đến trang đã chọn",
        "bookmark_name": "Tên",
        "bookmark_page": "Trang",
        "bookmark_no_bookmarks": "Không có dấu trang.\nNhấp vào 'Thêm' để lưu trang hiện tại làm dấu trang.",
        "bookmark_added": "Đã thêm dấu trang cho trang {0}: {1}",
        "bookmark_removed": "Đã xóa dấu trang: {0}",
        "bookmark_all_removed": "Tất cả các dấu trang đã được xóa.",
        "bookmark_name_default": "Trang {0}",
        "bookmark_name_prompt": "Tên cho dấu trang:\n(văn bản dài sẽ được rút ngắn xuống 50 ký tự)",
        "bookmark_name_prompt_title": "Tên dấu trang",
        "bookmark_confirm_remove_all": "Bạn có chắc chắn muốn xóa tất cả {0} dấu trang không?",
        "menu_bookmarks": "Dấu trang",
        "bookmark_manage": "Quản lý dấu trang",
        "bookmark_next": "Dấu trang tiếp theo",
        "bookmark_prev": "Dấu trang trước",
        "bookmark_page_display": "Trang {0}",
        "bookmark_exists": "Đã tồn tại dấu trang cho trang này với tên này.",
        "bookmark_select_first": "Vui lòng chọn dấu trang trước.",
        "bookmark_confirm_remove": "Bạn có chắc chắn muốn xóa dấu trang 'Trang {0}: {1}' không?",
        "bookmark_jumped_to": "Đã đi đến dấu trang '{0}' tại trang {1}.",
        "bookmark_jumped_to_voice": "Dấu trang {0}, trang {1}",
        "btn_close": "Đóng",

        "bookmark_list": "Dấu trang của bạn",
        "bookmark_rename": "Đổi tên dấu trang",
        "bookmark_rename_tooltip": "Thay đổi tên của dấu trang đã chọn",
        "bookmark_rename_title": "Đổi tên dấu trang",
        "bookmark_rename_prompt": "Tên mới cho dấu trang tại trang {0}:\n(tối đa 50 ký tự)",
        "bookmark_renamed": "Dấu trang '{0}' đã được đổi tên thành '{1}'.",
        "bookmark_item_tooltip": "Trang {0}: {1}\nNhấp đúp để đi đến",
        "bookmark_name_exists_question": "Đã tồn tại dấu trang có tên '{0}' trên trang này.\nVẫn đổi tên?",

        "context_bookmarks": "Dấu trang",
        "context_bookmark_add_here": "Thêm dấu trang cho trang này",
        "context_bookmarks_existing": "Dấu trang hiện có:",
        "context_bookmarks_jump": "Đi đến dấu trang:",
        "context_bookmarks_none": "Không có dấu trang",
        "context_bookmarks_clear_all": "Xóa tất cả {0} dấu trang",

        "bookmark_search_placeholder": "Tìm kiếm dấu trang... (tên hoặc trang)",
        "bookmark_search_results": "Đã tìm thấy %d dấu trang cho \"%s\"",
        "bookmark_no_search_results": "Không tìm thấy dấu trang nào cho \"%s\"",
        "bookmark_no_search_results_label": "Không có kết quả cho \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Chỉnh sửa siêu dữ liệu PDF",
        "metadata_title": "Tiêu đề",
        "metadata_title_placeholder": "Tiêu đề tài liệu",
        "metadata_title_tooltip": "Tiêu đề của tài liệu (được hiển thị trên thanh tiêu đề)",
        "metadata_author": "Tác giả",
        "metadata_author_placeholder": "Tên tác giả",
        "metadata_author_tooltip": "Người tạo tài liệu",
        "metadata_subject": "Chủ đề",
        "metadata_subject_placeholder": "Chủ đề của tài liệu",
        "metadata_subject_tooltip": "Mô tả ngắn gọn về nội dung",
        "metadata_keywords": "Từ khóa",
        "metadata_keywords_placeholder": "Từ khóa, phân cách bằng dấu phẩy",
        "metadata_keywords_tooltip": "Từ khóa để phân loại tài liệu",
        "metadata_creator": "Người tạo",
        "metadata_creator_placeholder": "Ứng dụng đã tạo PDF",
        "metadata_creator_tooltip": "Phần mềm đã được sử dụng để tạo tài liệu",
        "metadata_producer": "Nhà sản xuất",
        "metadata_producer_placeholder": "Ứng dụng đã chuyển đổi PDF",
        "metadata_producer_tooltip": "Phần mềm đã chuyển đổi PDF",
        "metadata_creation_date": "Ngày tạo",
        "metadata_creation_date_tooltip": "Ngày tạo tài liệu",
        "metadata_mod_date": "Ngày sửa đổi",
        "metadata_mod_date_tooltip": "Ngày sửa đổi lần cuối",
        "metadata_pdf_info": "📄 Thông tin PDF",
        "metadata_pages": "Số trang",
        "metadata_file_size": "Kích thước tệp",
        "metadata_pdf_version": "Phiên bản PDF",
        "metadata_encrypted": "Đã mã hóa",
        "metadata_encrypted_yes": "Có (được bảo vệ bằng mật khẩu)",
        "metadata_encrypted_no": "Không",
        "metadata_reload": "📂 Tải lại từ PDF",
        "metadata_reset": "Hủy bỏ thay đổi",
        "metadata_reloaded": "Siêu dữ liệu đã được tải lại từ PDF.",
        "metadata_reset_done": "Tất cả các trường siêu dữ liệu đã được đặt lại.",
        "metadata_no_file": "Không có tệp PDF nào được tải.",
        "metadata_save_error": "Lỗi khi lưu siêu dữ liệu",
        "metadata_saved": "Siêu dữ liệu đã được lưu thành công.",
        "metadata_pdf_version_unknown": "PDF (không rõ)",
        "metadata_saved_message": "Siêu dữ liệu đã được lưu thành công.",
        "metadata_saved_voice": "Đã lưu siêu dữ liệu.",

        "metadata_custom": "🔧 Siêu dữ liệu tùy chỉnh",
        "metadata_custom_placeholder": "{\n  \"trường_của_tôi\": \"giá_trị_của_tôi\",\n  \"trường_khác\": 123\n}",
        "metadata_custom_tooltip": "Định dạng JSON cho siêu dữ liệu tùy chỉnh (tùy chọn)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Đã chọn mẫu \"{0}\" - Nhấp đúp để chèn",
        "text_use_template": "Sử dụng khối văn bản",
        "text_type": "Loại",
        "text_search_templates": "Tìm kiếm khối văn bản...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Thông tin xuất / nhập",
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

        <h3>📦 Những gì được xuất? (Tổng quan)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Cài đặt ứng dụng chung</span></li>
            <li class="detail">• Chế độ Tối/Sáng</li>
            <li class="detail">• Đảo ngược chế độ tối cho hình ảnh</li>
            <li class="detail">• Giá trị ngưỡng xám</li>
            <li class="detail">• Ngôn ngữ</li>
            <li class="detail">• Hình học cửa sổ</li>
            <li class="detail">• Chế độ thu phóng</li>
            <li class="detail">• Điều hướng (Thanh điều hướng hiển thị)</li>
            <li class="detail">• Đầu ra giọng nói (bật/tắt)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Cài đặt sao lưu</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Đặt tên tệp (Dấu thời gian, Dấu phân cách, Hậu tố)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Cài đặt cho việc chèn</span></li>
            <li class="detail">• Chữ ký</li>
            <li class="detail">• Văn bản và khối văn bản</li>
            <li class="detail">• Dấu kiểm, hình ảnh và hình dạng</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Cài đặt OCR</span></li>
            <li class="detail">• Ngôn ngữ</li>
            <li class="detail">• Buộc OCR · Chế độ trang</li>
            <li class="detail">• Tiền xử lý hình ảnh: Sửa độ nghiêng, Làm sạch, Lấy mẫu quá mức</li>
            <li class="detail">• Số lượng tác vụ song song</li>
            <li class="detail">• Chế độ đảo ngược</li>
            <li class="detail">• Giá trị ngưỡng xám</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Dấu trang</span></li>
            <li class="detail">• Tất cả dấu trang trên mỗi tệp PDF (Trang, Tên, Thời gian tạo)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Cơ sở dữ liệu mật khẩu</span></li>
            <li class="detail">• Mật khẩu PDF đã lưu (tùy chọn được mã hóa hoặc văn bản thuần túy)</li>
            <li class="detail">• Băm mật khẩu chính (nếu được đặt)</li>
            <li class="detail">• Dữ liệu xác minh</li>
        </ul>

        <h4>⚠️ Lưu ý quan trọng</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Khi nhập:</strong>
            <ul>
                <li><span class="warning">➜ TẤT CẢ cài đặt hiện tại sẽ bị ghi đè hoàn toàn</span></li>
                <li>• Bắt buộc phải khởi động lại ứng dụng</li>
                <li>• Chữ ký, khối văn bản và dấu trang hiện có sẽ được thay thế</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Mật khẩu chính và chế độ xuất:</strong>
            <ul>
                <li>• Khi mật khẩu chính đang hoạt động, bạn có thể chọn:</li>
                <li>  - <span style="color: #98FB98;"><strong>Đã giải mã</strong></span> (mật khẩu ở dạng văn bản thuần túy trong ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Đã mã hóa</strong></span> (chỉ có thể đọc bằng mật khẩu chính trên hệ thống đích)</li>
                <li>• Băm mật khẩu chính <strong>luôn</strong> được lưu trữ dưới dạng mã hóa</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Thông báo bảo mật:</strong>
            <ul>
                <li>• Tệp ZIP được xuất chứa dữ liệu nhạy cảm (<strong>mật khẩu, dấu trang, chữ ký</strong>)</li>
                <li>• Vui lòng lưu trữ ở nơi an toàn (ví dụ: USB được mã hóa, trình quản lý mật khẩu)</li>
                <li>• Nếu tệp bị mất, mật khẩu PDF đã lưu sẽ bị mất vĩnh viễn</li>
            </ul>
        </div>

        <h4>📁 Định dạng xuất</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Cài đặt được lưu trong một tệp ZIP duy nhất:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            ZIP này chứa <code>settings.json</code> đầy đủ (từ cấu hình của bạn) cũng như các tệp hình ảnh chữ ký được nhúng và mật khẩu được mã hóa.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Chữ ký - Hướng dẫn",
        'signature_guide_html': """
        📝 <strong>Chữ ký - Hướng dẫn nhanh</strong><br>
        <ul>
        <li>Thiết lập mật khẩu chính</li>
        <li>Cấu hình chữ ký trong menu <em>Cài đặt</em> (kích thước, dấu thời gian, …)</li>
        <li>Chèn bằng <strong>CHUỘT PHẢI</strong> tại vị trí mong muốn (cần mật khẩu chính một lần mỗi phiên)</li>
        <li>Di chuyển chữ ký bằng chuột hoặc phím mũi tên</li>
        <li>Chèn nhiều chữ ký liên tiếp</li>
        <li>Tùy chỉnh từng chữ ký riêng lẻ</li>
        <li>Hủy bỏ một chữ ký</li>
        <li>Lưu / hủy bỏ tất cả chữ ký cùng lúc</li>
        <li>Ngoài ra, bạn cũng có thể sử dụng thanh menu.</li>
        </ul>
        """,
        'signature_guide_voice': "Hướng dẫn nhanh cho chữ ký. Thiết lập mật khẩu chính. Cấu hình chữ ký trong cài đặt. Chèn bằng chuột phải.",

        'image_guide_title': "Chèn ảnh - Hướng dẫn",
        'image_guide_html': """
        📷 <strong>Chèn ảnh vào PDF - Hướng dẫn nhanh</strong><br>
        <ol>
        <li>Chuột phải tại vị trí mong muốn</li>
        <li><em>"Chèn ảnh"</em> → chọn ảnh</li>
        <li>Định vị ảnh: Kéo bằng chuột</li>
        <li>Điều chỉnh kích thước: Kéo ở các góc/cạnh</li>
        <li>Giữ tỷ lệ khung hình: Nhấn phím <strong>[A]</strong></li>
        <li>Điều chỉnh thêm: Chuột phải vào ảnh</li>
        </ol>
        <p><strong>Mẹo:</strong> Bạn có thể điều chỉnh cài đặt trong menu ngữ cảnh.</p>
        """,
        'image_guide_voice': "Hướng dẫn nhanh cho ảnh. Chuột phải, chèn ảnh, chọn. Định vị bằng chuột, điều chỉnh kích thước ở các góc. Giữ tỷ lệ khung hình bằng phím A.",

        'form_guide_title': "Chèn hình khối - Hướng dẫn",
        'form_guide_html': """
        📐 <strong>Chèn hình khối vào PDF - Hướng dẫn nhanh</strong><br>
        <ol>
        <li>Chọn loại hình khối (hình chữ nhật, hình elip, đường thẳng, mũi tên)</li>
        <li>Nhấp vào vị trí:
            <ul>
            <li>Với hình chữ nhật/elip: Một cú nhấp chuột đặt hình khối</li>
            <li>Với đường thẳng/mũi tên: Hai cú nhấp chuột cho điểm đầu và điểm cuối</li>
            </ul>
        </li>
        <li>Định vị hình khối: Kéo bằng chuột</li>
        <li>Điều chỉnh kích thước: Kéo ở các góc/cạnh</li>
        <li>Lưu hình khối: <strong>Enter</strong></li>
        <li>Hủy bỏ hình khối: <strong>ESC</strong></li>
        <li>Điều chỉnh thêm: Chuột phải vào hình khối</li>
        </ol>
        <p><strong>Mẹo:</strong> Bạn có thể điều chỉnh cài đặt trong menu ngữ cảnh.</p>
        """,
        'form_guide_voice': "Hướng dẫn nhanh cho hình khối. Chọn loại hình khối. Với hình chữ nhật hoặc elip nhấp một lần, với đường thẳng hoặc mũi tên nhấp hai lần. Định vị bằng chuột, điều chỉnh kích thước ở các góc. Lưu bằng Enter, hủy bỏ bằng Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "trước",
        "btn_next_result": "tiếp",
        "ocr_text_window": "Cửa sổ văn bản OCR",
        "bookmark_existing": "Đánh dấu hiện có",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "So sánh OCR Mac - Windows",
        'ocr_method_mac_win_title': "Khác biệt OCR giữa Mac và Windows",
        'ocr_method_mac_win_voice': "Mac tốt hơn",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Khác biệt giữa macOS và Windows</strong></p>

        <p><strong>macOS (khuyến nghị)</strong></p>
        <p>Công cụ:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Kết quả:</p>
        <ul>
        <li>PDF có thể tìm kiếm với văn bản nhúng, phần lớn giữ nguyên bố cục gốc.</li>
        </ul>
        <p>Ưu điểm:</p>
        <ul>
        <li>Chất lượng nhận dạng văn bản xuất sắc (ngay cả với trang bị lệch).</li>
        <li>Giữ nguyên đồ họa vector và phông chữ.</li>
        <li>Thanh tiến trình GUI thông qua đánh giá subprocess.</li>
        <li>Kiểm soát hoàn toàn mọi tham số OCR (deskew, clean, oversample, tối ưu hóa).</li>
        <li>Tìm kiếm văn bản có sẵn trực tiếp trong cửa sổ chính (chế độ xem PDF).</li>
        </ul>
        <p>Nhược điểm:</p>
        <ul>
        <li>Cần thêm công cụ hệ thống (ocrmypdf, Ghostscript, unpaper, pngquant – đã được gói trong ứng dụng).</li>
        <li>Xử lý lỗi phức tạp hơn (deadlock, timeout).</li>
        </ul>

        <p><strong>Windows (lựa chọn thay thế ổn định)</strong></p>
        <p>Công cụ:</p>
        <ul>
        <li>pytesseract (kết nối trực tiếp với Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Kết quả:</p>
        <ul>
        <li>PDF có thể tìm kiếm, về mặt hình ảnh giống PDF ảnh nhưng có thể tìm kiếm nhờ văn bản trong suốt.</li>
        </ul>
        <p>Ưu điểm:</p>
        <ul>
        <li>Tôi chưa nghĩ ra ưu điểm nào ngay lúc này.</li>
        </ul>
        <p>Nhược điểm:</p>
        <ul>
        <li>PDF về cơ bản là một hình ảnh với văn bản vô hình; bố cục có thể hơi lệch đối với tài liệu phức tạp (cột, bảng).</li>
        <li>Không có tính năng tự động chỉnh nghiêng (--deskew) hoặc làm sạch ảnh (--clean).</li>
        <li>Thanh tiến trình GUI chỉ được cập nhật đại khái dựa trên số trang đã xử lý.</li>
        <li>Tốc độ OCR chậm hơn một chút (vì mỗi trang được xử lý riêng lẻ).</li>
        <li>Tìm kiếm văn bản được chuyển hướng đến cửa sổ văn bản OCR.</li>
        </ul>

        <p><strong>Điểm chung</strong></p>
        <ul>
        <li>Cả hai phương pháp đều tạo ra PDF có thể tìm kiếm trong cùng thư mục với tệp nguồn.</li>
        <li>Các cài đặt OCR (ngôn ngữ, DPI, chế độ phân đoạn trang, chế độ động cơ OCR) có thể được cấu hình qua OCRSettingsDialog và có hiệu lực trong cả hai triển khai.</li>
        </ul>

        <p><strong>Khuyến nghị:</strong></p>
        <ul>
        <li>macOS: Tệp nhị phân ocrmypdf cho kết quả tốt nhất – hãy mua máy Mac và sử dụng phiên bản (PDFDarkView cho Mac dùng chip Apple Silicon hoặc Intel). Kết quả OCR tốt hơn so với trên Windows!</li>
        <li>Windows: Sử dụng giải pháp pytesseract. Nó ổn định và cung cấp chất lượng đủ dùng cho hầu hết tài liệu.</li>
        </ul>

        <p><strong>Lưu ý quan trọng:</strong></p>
        <ul>
        <li>Cả hai phiên bản đều được tích hợp đầy đủ vào giao diện người dùng – người dùng không nhận thấy sự khác biệt.</li>
        <li>Chương trình tự động quyết định động cơ OCR nào được sử dụng dựa trên hệ điều hành.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN
        # ============================================
        "signature_create_from_scan": "Tạo chữ ký (từ bản quét)",
        "signature_create_title": "Chọn chữ ký quét (PDF/Hình ảnh)",
        "image_pdf_filter": "Hình ảnh và PDF",
        "signature_pdf_empty": "PDF không có trang nào.",
        "signature_created_success": "Đã tạo chữ ký thành công: {0}",
        "signature_create_error": "Lỗi khi tạo chữ ký:\n{0}",
        "rembg_missing": "rembg chưa được cài đặt.\nVui lòng chạy: pip install rembg\nLỗi: {0}",
        "signature_name_title": "Tên tệp cho chữ ký",
        "signature_name_message": "Nhập tên tệp cho chữ ký mới (lưu dưới dạng PNG):",
        "signature_name_label": "Tên tệp:",
        "signature_name_voice": "Nhập tên tệp cho chữ ký",
        "signature_processing": "Đang xử lý...",
        "signature_creation_title": "Đang tạo chữ ký",
        "signature_overwrite_warning": "Tệp '{0}' đã tồn tại. Ghi đè?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Chuẩn bị PDF cho chữ ký",
        "signature_prepare_instruction":"Vui lòng chọn một tệp PDF có chứa chữ ký được quét trên một trang duy nhất.\n\nNhận dạng tối ưu đạt được nếu:\n• Chữ ký được viết bằng mực đen (bút bi hoặc bút lông) trên giấy trắng.\n• Chữ ký nằm ở một phần ba phía trên của trang A4 trống.\n• PDF được quét ở độ phân giải ít nhất 300 dpi.\n• Chữ ký rõ ràng và không quá mảnh.\n• Không có họa tiết hoặc đường kẻ nền gây nhiễu.",
        "signature_prepare_voice":"Vui lòng chọn PDF có chữ ký được quét. Chú ý chất lượng và độ tương phản tốt.",
        "sig_thickness_label":"Độ dày nét:",
        "sig_thickness_normal":"Bình thường (mảnh)",
        "sig_thickness_bold":"Đậm (khuyến nghị)",
        "sig_thickness_very_bold":"Rất đậm",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Thêm Ngôn ngữ GUI và OCR - Hướng dẫn",
        'language_guide_title': "Thêm Ngôn ngữ GUI và OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Tải xuống tệp dịch thuật mong muốn <code>translations_xy.py</code> từ<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        và đặt nó vào thư mục sau:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Mở trình duyệt web của bạn.</li>
        <li>Đi đến: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Tìm ở bên phải màn hình "Releases" và chọn bản có nhãn <strong>"latest"</strong> (mới nhất).</li>
        <li>Trên trang phát hành tiếp theo, cuộn xuống dưới cùng và tải xuống tệp <code>Source Code.zip</code>.</li>
        <li>Giải nén tệp ZIP.</li>
        <li>Trong thư mục đã giải nén, tìm tất cả các tệp ngôn ngữ bạn cần và sao chép chúng vào thư mục:<br/>
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
        "menu_watermark":"Chèn hình mờ",
        "fullpage_text_watermark_title":"Văn bản làm hình mờ",
        "fullpage_image_watermark_title":"Hình ảnh làm hình mờ",
        "filename_with_watermark":"_co_hinh_mo",
        "watermark_text":"Văn bản:",
        "watermark_text_placeholder":"Văn bản hình mờ của bạn...",
        "watermark_font_family":"Phông chữ:",
        "watermark_font_size":"Cỡ chữ:",
        "watermark_format":"Định dạng:",
        "watermark_bold":"Đậm",
        "watermark_italic":"Nghiêng",
        "watermark_color":"Màu sắc:",
        "watermark_choose_color":"Chọn màu...",
        "watermark_opacity":"Độ mờ / Độ trong suốt:",
        "watermark_direction":"Hướng đọc:",
        "watermark_direction_l_r":"Trái → Phải",
        "watermark_direction_bl_tr":"Dưới trái → Trên phải",
        "watermark_direction_tl_br":"Trên trái → Dưới",
        "watermark_direction_b_t":"Dưới → Trên",
        "watermark_direction_t_b":"Trên → Dưới",
        "watermark_preview":"Xem trước:",
        "watermark_preview_sample":"Văn bản mẫu",
        "watermark_empty_text":"Vui lòng nhập văn bản.",
        "watermark_applied":"Hình mờ đã được áp dụng cho tất cả các trang.",
        "watermark_saved":"Đã lưu hình mờ.",
        "image_scale":"Kích thước:",
        "image_preview":"Xem trước hình ảnh:",
        "no_image_selected":"Chưa chọn hình ảnh",
        "browse":"Duyệt...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Che xóa",
        "redact_add_black": "Che xóa (màu đen)",
        "redact_add_white": "Che xóa (màu trắng / xóa)",
        "redact_added_black": "Đã thêm che xóa màu đen",
        "redact_added_white": "Đã thêm che xóa màu trắng",
        "redact_apply_all": "Áp dụng tất cả che xóa và lưu",
        "redact_discard_all": "Hủy bỏ tất cả che xóa",
        "redact_discard": "Hủy bỏ che xóa này",
        "no_redactions": "Không có che xóa nào",
        "redact_confirm_title": "Áp dụng che xóa vĩnh viễn",
        "redact_confirm_message": "Cảnh báo: Các khu vực được đánh dấu sẽ bị xóa vĩnh viễn (màu đen hoặc trắng).\nBản sao lưu sẽ được tạo (nếu được bật).\n\nTiếp tục?",
        "redact_apply": "Có, che xóa ngay",
        "redact_saved": "Đã áp dụng và lưu thành công {0} che xóa.",
        "redact_saved_voice": "Đã áp dụng {0} che xóa",
        "redact_error": "Lỗi khi che xóa",
        "filename_redacted":"_da_che_xoa",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Chèn số trang',
        'page_numbers_format': 'Định dạng số:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Ả Rập)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (La Mã thường)',
        'page_numbers_format_roman_upper': 'I, II, III ... (La Mã hoa)',
        'page_numbers_format_letter': 'A, B, C ... (Chữ cái)',
        'page_numbers_format_custom': 'Tùy chỉnh',
        'page_numbers_custom_pattern': 'Mẫu:',
        'page_numbers_custom_placeholder': 'Ví dụ "Trang {nummer}" hoặc "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Sử dụng {nummer} cho số trang hiện tại và {total} cho tổng số',
        'page_numbers_position': 'Vị trí:',
        'page_numbers_pos_tl': 'Trên cùng bên trái',
        'page_numbers_pos_tc': 'Trên cùng ở giữa',
        'page_numbers_pos_tr': 'Trên cùng bên phải',
        'page_numbers_pos_ml': 'Giữa bên trái',
        'page_numbers_pos_mc': 'Ở giữa',
        'page_numbers_pos_mr': 'Giữa bên phải',
        'page_numbers_pos_bl': 'Dưới cùng bên trái',
        'page_numbers_pos_bc': 'Dưới cùng ở giữa',
        'page_numbers_pos_br': 'Dưới cùng bên phải',
        'page_numbers_margins': 'Lề:',
        'page_numbers_margin_x': 'Khoảng cách ngang:',
        'page_numbers_margin_y': 'Khoảng cách dọc:',
        'page_numbers_range': 'Phạm vi trang:',
        'page_numbers_all_pages': 'Tất cả các trang',
        'page_numbers_custom_range': 'Phạm vi tùy chỉnh',
        'page_numbers_from': 'Từ:',
        'page_numbers_to': 'Đến:',
        'page_numbers_progress': 'Đang chèn số trang...',
        'page_numbers_start': 'Bắt đầu chèn số trang...',
        'page_numbers_cancel': 'Đã hủy chèn số trang',
        'page_numbers_success': 'Đã thêm số trang thành công.\n\nBạn có muốn mở PDF mới không?\n\n{0}',
        'page_numbers_complete': 'Đã thêm số trang',
        'page_numbers_error_format': 'Lỗi khi chèn số trang: {0}',
        'page_numbers_content_type': 'Loại nội dung:',
        'page_numbers_tab_simple': 'Số đơn giản',
        'page_numbers_tab_range': 'Trang X của Y',
        'page_numbers_tab_date': 'Ngày tháng',
        'page_numbers_tab_custom': 'Văn bản tự do',
        'page_numbers_range_format': 'Định dạng:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Trang {aktuell} trên {gesamt}',
        'page_numbers_range_custom': 'Tùy chỉnh',
        'page_numbers_range_placeholder': 'Ví dụ "Trang {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Định dạng ngày:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 tháng 1 năm 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Tùy chỉnh',
        'page_numbers_date_placeholder': 'Ví dụ %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Vị trí:',
        'page_numbers_date_before': 'Ngày trước số trang',
        'page_numbers_date_after': 'Ngày sau số trang',
        'page_numbers_date_only': 'Chỉ ngày (không có số trang)',
        'page_numbers_custom_text': 'Văn bản tùy chỉnh:',
        'page_numbers_custom_placeholder_text': 'Sử dụng {seite} cho số trang và {gesamt} cho tổng số\nVí dụ "Bảo mật - Trang {seite}" hoặc "{seite} trên {gesamt}"',
        "filename_with_page_number":"_co_so_trang",
        "filename_with_page_declaration":"_co_ghi_chu_trang",
        "filename_with_pagenumber":"_co_so_trang",
        "filename_with_date":"_co_ngay_thang",
        "filename_with_my_page_declaration":"_co_ghi_chu_trang_tuy_chinh",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Thay đổi chưa lưu",
        "unsaved_changes_message_darkmode": "Có các nội dung chèn chưa được lưu.\nBạn có muốn lưu chúng trước khi chuyển đổi không?",
        "save_and_switch": "Lưu và chuyển đổi",
        "discard_and_switch": "Chuyển đổi ngay",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Xuất trang dưới dạng hình ảnh',
        'export_images_menu': 'Xuất dưới dạng hình ảnh (PNG/JPEG)',
        'export_images_format': 'Định dạng hình ảnh:',
        'export_images_dpi': 'Độ phân giải (DPI):',
        'export_images_quality': 'Chất lượng JPEG:',
        'export_images_range': 'Phạm vi trang:',
        'export_images_all_pages': 'Tất cả các trang',
        'export_images_custom_range': 'Phạm vi tùy chỉnh',
        'export_images_from': 'Từ:',
        'export_images_to': 'Đến:',
        'export_images_options': 'Tùy chọn:',
        'export_images_single_files': 'Mỗi trang là một tệp riêng',
        'export_images_subfolder': 'Xuất vào thư mục con',
        'export_images_subfolder_info': 'Vào thư mục con "TenPDF_hinh_anh"',
        'export_images_same_folder': 'Trong cùng thư mục với PDF',
        'export_images_apply_darkmode': 'Áp dụng cài đặt PDFDarkView (Chế độ tối)',
        'export_images_target_folder': 'Thư mục đích:',
        'export_images_browse': 'Duyệt...',
        'export_images_preview': 'Xem trước:',
        'export_images_preview_info': 'Chọn cài đặt để xuất',
        'export_images_preview_info_detail': '{0} trang dưới dạng {1}\nĐộ phân giải: {2} DPI\nTên tệp: {3}\n{4}',
        'export_images_select_folder': 'Chọn thư mục đích',
        'export_images_start': 'Bắt đầu xuất hình ảnh...',
        'export_images_progress': 'Đang xuất hình ảnh...',
        'export_images_saving': 'Đang lưu trang {0} trên {1}...',
        'export_images_success': 'Xuất thành công!\n\nĐã lưu {0} hình ảnh vào:\n{1}',
        'export_images_complete': 'Đã hoàn thành xuất hình ảnh',
        'export_images_open_folder': '📁 Mở thư mục',
        'export_images_cancel': 'Đã hủy xuất hình ảnh',
        'export_images_error_format': 'Lỗi khi xuất hình ảnh: {0}',
        'export_images_pdf2image_missing': 'Thư viện "pdf2image" chưa được cài đặt.\n\nVui lòng cài đặt với:\npip install pdf2image\n\nĐối với Windows, bạn cũng cần Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'Chuyển đổi PDF/A để lưu trữ dài hạn',
        'pdfa_menu': 'Chuyển đổi PDF/A (phù hợp lưu trữ)',
        'pdfa_info': 'Chuyển đổi PDF sang định dạng PDF/A.\n\nPDF/A được thiết kế đặc biệt cho lưu trữ dài hạn và đảm bảo tài liệu sẽ được hiển thị chính xác trong tương lai.',
        'pdfa_standard': 'Tiêu chuẩn PDF/A:',
        'pdfa_standard_select': 'Phiên bản:',
        'pdfa_1': 'PDF/A-1 (đơn giản, tương thích rộng rãi)',
        'pdfa_2': 'PDF/A-2 (hiện đại, nén tốt hơn)',
        'pdfa_3': 'PDF/A-3 (phiên bản mới nhất, cho phép tệp đính kèm)',
        'pdfa_standards_explanation': '📖 Giải thích các tiêu chuẩn:\n\n'
            '• PDF/A-1: Cơ bản, tương thích với hệ thống cũ (khoảng 2005)\n'
            '• PDF/A-2: Hiện đại hơn, nén tốt hơn, hỗ trợ độ trong suốt (khoảng 2011)\n'
            '• PDF/A-3: Phiên bản mới nhất, cho phép nhúng tệp đính kèm (khoảng 2013)\n\n'
            'Khuyến nghị: PDF/A-2 là sự cân bằng tốt giữa tương thích và tính năng hiện đại.',
        'pdfa_options': 'Tùy chọn:',
        'pdfa_compress_enable': 'Nén PDF (tệp nhỏ hơn)',
        'pdfa_metadata_preserve': 'Giữ siêu dữ liệu (tiêu đề, tác giả, v.v.)',
        'pdfa_target_folder': 'Thư mục đích:',
        'pdfa_browse': 'Duyệt...',
        'pdfa_select_folder': 'Chọn thư mục đích',
        'pdfa_ocr_info_unknown': '🔍 Không thể kiểm tra nội dung văn bản.',
        'pdfa_ocr_info_not_needed': '✅ Có văn bản - Không cần OCR.\nCó thể tạo PDF/A trực tiếp.',
        'pdfa_ocr_info_recommended': '⚠️ Không tìm thấy đủ văn bản.\n\nĐối với PDF có thể tìm kiếm, chúng tôi khuyên bạn nên chạy OCR trước.\nLưu ý: PDF/A vẫn hoạt động nếu không có OCR - nhưng văn bản sẽ không thể tìm kiếm được.',
        'pdfa_ocr_info_error': '❌ Lỗi khi kiểm tra: {0}',
        'pdfa_start': 'Bắt đầu chuyển đổi PDF/A...',
        'pdfa_progress': 'Đang chuyển đổi PDF/A...',
        'pdfa_success': 'Chuyển đổi PDF/A thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nBạn có muốn mở PDF mới không?',
        'pdfa_complete': 'Đã hoàn thành chuyển đổi PDF/A',
        'pdfa_cancel': 'Đã hủy chuyển đổi PDF/A',
        'pdfa_error_format': 'Lỗi khi chuyển đổi PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Thư viện "ocrmypdf" chưa được cài đặt.\n\nVui lòng cài đặt với:\npip install ocrmypdf',
        'btn_convert': 'Chuyển đổi',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Tối ưu hóa PDF (giảm kích thước tệp)',
        'optimize_menu': 'Tối ưu hóa PDF (kích thước tệp)',
        'optimize_info': 'Giảm kích thước tệp PDF thông qua các phương pháp tối ưu hóa khác nhau.\n\nMức nén càng cao, tệp càng nhỏ - nhưng có thể giảm chất lượng hình ảnh.',
        'optimize_level': 'Mức nén:',
        'optimize_level_low': 'Thấp (nhanh, tiết kiệm ít)',
        'optimize_level_medium': 'Trung bình (cân bằng tốt)',
        'optimize_level_high': 'Cao (tiết kiệm nhiều)',
        'optimize_level_maximum': 'Tối đa (tiết kiệm tối đa, chậm)',
        'optimize_level_explanation': 'Khuyến nghị: "Trung bình" là sự cân bằng tốt giữa tốc độ và kích thước tệp.',
        'optimize_options': 'Tùy chọn:',
        'optimize_compress_images': 'Nén hình ảnh (giảm chất lượng JPEG)',
        'optimize_clean_objects': 'Loại bỏ đối tượng không sử dụng',
        'optimize_preserve_metadata': 'Giữ siêu dữ liệu (tiêu đề, tác giả, v.v.)',
        'optimize_image_quality': 'Chất lượng hình ảnh:',
        'optimize_range': 'Phạm vi trang:',
        'optimize_all_pages': 'Tất cả các trang',
        'optimize_custom_range': 'Phạm vi tùy chỉnh',
        'optimize_from': 'Từ:',
        'optimize_to': 'Đến:',
        'optimize_target_folder': 'Thư mục đích:',
        'optimize_browse': 'Duyệt...',
        'optimize_select_folder': 'Chọn thư mục đích',
        'optimize_info_box': 'Thông tin',
        'optimize_info_text': 'Quá trình tối ưu hóa có thể mất vài phút đối với PDF lớn.\n\nHình ảnh sẽ được lưu với chất lượng giảm, có thể giảm đáng kể kích thước tệp.',
        'optimize_start': 'Bắt đầu tối ưu hóa PDF...',
        'optimize_progress': 'Đang tối ưu hóa PDF...',
        'optimize_cancel': 'Đã hủy tối ưu hóa PDF',
        'optimize_complete': 'Đã hoàn thành tối ưu hóa PDF',
        'optimize_error_format': 'Lỗi khi tối ưu hóa PDF:\n\n{0}',
        'optimize_success_message': 'Tối ưu hóa PDF thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nTrước: {1}\nSau: {2}\nTiết kiệm: {3:.1f}%\n\n{4}\n\nBạn có muốn mở PDF đã tối ưu không?',
        'optimize_success_message_no_size': 'Tối ưu hóa PDF thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nKhông có thông tin kích thước.\n\nBạn có muốn mở PDF đã tối ưu không?',
        'optimize_result_positive': 'Tệp đã được giảm {0:.1f}%.',
        'optimize_result_zero': 'Không có thay đổi về kích thước tệp.',
        'optimize_result_negative': 'Tệp đã tăng {0:.1f}%.\nĐã bỏ qua tối ưu hóa, giữ nguyên tệp gốc.',
        'btn_optimize': 'Bắt đầu tối ưu hóa',
        'filename_optimize_low_suffix': '_toi_uu_thap',
        'filename_optimize_medium_suffix': '_toi_uu',
        'filename_optimize_high_suffix': '_toi_uu_cao',
        'filename_optimize_maximum_suffix': '_toi_uu_toi_da',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Cắt PDF',
        'crop_menu': 'Cắt PDF (Crop)',
        'crop_range': 'Áp dụng cho:',
        'crop_all_pages': 'Tất cả các trang',
        'crop_current_page': 'Chỉ trang hiện tại',
        'crop_values': 'Giá trị cắt (theo điểm):',
        'crop_left': 'Trái:',
        'crop_right': 'Phải:',
        'crop_top': 'Trên:',
        'crop_bottom': 'Dưới:',
        'crop_presets': 'Cài đặt sẵn:',
        'crop_preset_white': 'Phát hiện lề trắng',
        'crop_reset': 'Đặt lại',
        'crop_mouse_hint': '🖱️ Kéo một hình chữ nhật để chọn khu vực một cách sơ bộ.\nSau đó bạn có thể điều chỉnh chính xác các giá trị trong SpinBox.\nKhông thể điều chỉnh thủ công bằng chuột.',
        'crop_apply': 'Cắt',
        'crop_scope_all': 'Tất cả các trang',
        'crop_scope_current': 'Trang hiện tại',
        'crop_new_size': 'Kích thước mới: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Chưa tải PDF',
        'crop_preview_error': 'Lỗi khi tải bản xem trước',
        'crop_start': 'Bắt đầu cắt...',
        'crop_progress': 'Đang cắt PDF...',
        'crop_success': 'Cắt PDF thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nBạn có muốn mở PDF đã cắt không?',
        'crop_complete': 'Đã hoàn thành cắt',
        'crop_cancel': 'Đã hủy cắt',
        'crop_error_format': 'Lỗi khi cắt:\n\n{0}',
        'filename_crop_suffix': '_da_cat',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Làm phẳng PDF (Flatten)',
        'flatten_menu': 'Làm phẳng PDF (Flatten)',
        'flatten_info': 'Làm phẳng PDF "đốt cháy" tất cả các thành phần có thể chỉnh sửa vào nội dung trang.\n\nSau đó, các trường biểu mẫu, chú thích, văn bản, dấu gạch chéo, chữ ký, hình ảnh và hình dạng không thể chỉnh sửa riêng lẻ được nữa.',
        'flatten_explanation_title': '📖 Điều này dùng để làm gì?',
        'flatten_explanation_text': 'Làm phẳng được sử dụng trong các trường hợp sau:\n\n'
            '• 📄 Bạn muốn chuẩn bị tài liệu để in\n'
            '• 🔒 Bạn muốn ngăn người khác thay đổi trường biểu mẫu\n'
            '• 📎 Bạn muốn "gắn" chú thích và bình luận vĩnh viễn vào tài liệu\n'
            '• 🖼️ Bạn muốn neo vĩnh viễn văn bản, dấu gạch chéo, chữ ký, hình ảnh và hình dạng trong tài liệu\n'
            '• 📦 Bạn muốn chuẩn bị tệp để lưu trữ\n\n'
            'Làm phẳng làm cho PDF nhỏ hơn và ngăn các thành phần bị di chuyển hoặc xóa nhầm.',
        'flatten_what_title': 'Những gì được làm phẳng?',
        'flatten_what_list': '• ✅ Trường biểu mẫu (trường văn bản, hộp kiểm, nút)\n'
            '• ✅ Chú thích (bình luận, đánh dấu, ghi chú)\n'
            '• ✅ Lớp phủ (văn bản, dấu gạch chéo, chữ ký, hình ảnh, hình dạng)',
        'flatten_options': 'Tùy chọn:',
        'flatten_forms': 'Làm phẳng trường biểu mẫu',
        'flatten_annotations': 'Làm phẳng chú thích',
        'flatten_overlays': 'Làm phẳng lớp phủ (văn bản, dấu gạch chéo, chữ ký, hình ảnh, hình dạng)',
        'flatten_target_folder': 'Thư mục đích:',
        'flatten_browse': 'Duyệt...',
        'flatten_select_folder': 'Chọn thư mục đích',
        'flatten_warning': '⚠️ Quan trọng: Làm phẳng là quá trình không thể đảo ngược!\n\nSau khi làm phẳng, các thành phần có thể chỉnh sửa không thể thay đổi hoặc xóa riêng lẻ được nữa.\nTạo bản sao lưu trước nếu cần.',
        'flatten_apply': 'Làm phẳng',
        'flatten_start': 'Bắt đầu làm phẳng...',
        'flatten_progress': 'Đang làm phẳng PDF...',
        'flatten_success': 'Làm phẳng PDF thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nBạn có muốn mở PDF đã làm phẳng không?',
        'flatten_complete': 'Đã hoàn thành làm phẳng',
        'flatten_cancel': 'Đã hủy làm phẳng',
        'flatten_error_format': 'Lỗi khi làm phẳng:\n\n{0}',
        'filename_flatten_suffix': '_da_lam_phang',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Chồng PDF (Overlay)',
        'overlay_menu': 'Chồng PDF (Overlay)',
        'overlay_info': 'Đặt một PDF (lớp phủ) lên trên một PDF khác.\n\nPDF lớp phủ được đặt lên PDF cơ sở. Điều này hữu ích cho hình mờ, logo, tiêu đề thư hoặc con dấu.',
        'overlay_explanation_title': '📖 Điều này dùng để làm gì?',
        'overlay_explanation_text': 'Chồng được sử dụng trong các trường hợp sau:\n\n'
            '• 🏢 Đặt logo công ty làm hình mờ trên mỗi trang\n'
            '• 📄 Đặt tiêu đề thư lên PDF trống\n'
            '• 🖊️ Đặt lớp phủ con dấu lên tài liệu\n'
            '• 🔖 Đặt hình mờ trên tất cả các trang\n'
            '• 📑 Đặt lớp phủ biểu mẫu lên một mẫu',
        'overlay_type': 'Loại chồng:',
        'overlay_type_fullpage': 'Toàn trang (che phủ)',
        'overlay_type_transparent': 'Toàn trang (trong suốt - khuyến nghị)',
        'overlay_type_stamp': 'Con dấu (có thể định vị)',
        'overlay_type_info_fullpage': '📄 PDF lớp phủ được đặt chính xác trên toàn bộ trang.\nCó thể loại bỏ nền trắng để chỉ hiển thị nội dung.',
        'overlay_type_info_transparent': '🔍 PDF lớp phủ được đặt trên toàn bộ trang với nền trong suốt.\nNền trắng được tự động loại bỏ - lý tưởng cho hình mờ và logo!',
        'overlay_type_info_stamp': '🖊️ PDF lớp phủ được định vị và chia tỷ lệ như một con dấu.\nHoàn hảo cho logo, con dấu hoặc chữ ký tại các vị trí cụ thể.',
        'overlay_remove_background': 'Loại bỏ nền trắng:',
        'overlay_remove_background_enable': 'Loại bỏ nền trắng của PDF lớp phủ (làm cho lớp phủ trong suốt)',
        'overlay_remove_background_tooltip': 'Loại bỏ vùng trắng khỏi PDF lớp phủ để văn bản bên dưới hiển thị.',
        'overlay_threshold': 'Giá trị ngưỡng:',
        'overlay_threshold_hint': '(1-254, cao hơn = loại bỏ nhiều màu trắng hơn)',
        'overlay_select_file': 'Chọn PDF lớp phủ:',
        'overlay_file_placeholder': 'Vui lòng chọn tệp PDF cho lớp phủ',
        'overlay_browse': 'Duyệt...',
        'overlay_select_overlay': 'Chọn PDF lớp phủ',
        'overlay_range': 'Phạm vi trang:',
        'overlay_all_pages': 'Tất cả các trang',
        'overlay_custom_range': 'Phạm vi tùy chỉnh',
        'overlay_from': 'Từ:',
        'overlay_to': 'Đến:',
        'overlay_position': 'Vị trí:',
        'overlay_position_center': 'Trung tâm',
        'overlay_position_top_left': 'Trên cùng bên trái',
        'overlay_position_top_right': 'Trên cùng bên phải',
        'overlay_position_bottom_left': 'Dưới cùng bên trái',
        'overlay_position_bottom_right': 'Dưới cùng bên phải',
        'overlay_size': 'Kích thước:',
        'overlay_size_original': 'Kích thước gốc',
        'overlay_size_fit_page': 'Vừa với trang',
        'overlay_size_custom': 'Tùy chỉnh (%)',
        'overlay_opacity': 'Độ trong suốt:',
        'overlay_target_folder': 'Thư mục đích:',
        'overlay_browse_folder': 'Duyệt...',
        'overlay_select_folder': 'Chọn thư mục đích',
        'overlay_warning': '⚠️ Lưu ý: PDF lớp phủ được đặt lên PDF cơ sở và "đốt cháy" vào đó.\n\nCác thành phần của PDF lớp phủ không thể chỉnh sửa riêng lẻ sau khi lưu.',
        'overlay_apply': 'Chồng',
        'overlay_start': 'Bắt đầu chồng...',
        'overlay_progress': 'Đang chồng PDF...',
        'overlay_success': 'Chồng PDF thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nBạn có muốn mở PDF đã chồng không?',
        'overlay_complete': 'Đã hoàn thành chồng',
        'overlay_cancel': 'Đã hủy chồng',
        'overlay_error_format': 'Lỗi khi chồng:\n\n{0}',
        'overlay_no_file': 'Chưa chọn PDF lớp phủ.\n\nVui lòng chọn tệp PDF để chồng.',
        'filename_overlay_suffix': '_da_chong',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Trích xuất hình ảnh từ PDF',
        'extract_images_menu': 'Trích xuất tất cả hình ảnh',
        'extract_images_info': 'Trích xuất tất cả hình ảnh từ PDF và lưu dưới dạng tệp riêng.\n\nHình ảnh được lưu ở định dạng gốc hoặc chuyển đổi sang định dạng đã chọn.',
        'extract_images_format': 'Định dạng hình ảnh:',
        'extract_images_quality': 'Chất lượng JPEG:',
        'extract_images_options': 'Tùy chọn:',
        'extract_images_subfolder': 'Trích xuất vào thư mục con ("TenPDF_hinh_anh")',
        'extract_images_unique': 'Chỉ hình ảnh duy nhất (tránh trùng lặp)',
        'extract_images_range': 'Phạm vi trang:',
        'extract_images_all_pages': 'Tất cả các trang',
        'extract_images_custom_range': 'Phạm vi tùy chỉnh',
        'extract_images_from': 'Từ:',
        'extract_images_to': 'Đến:',
        'extract_images_target_folder': 'Thư mục đích:',
        'extract_images_browse': 'Duyệt...',
        'extract_images_select_folder': 'Chọn thư mục đích',
        'extract_images_info_box': 'Thông tin',
        'extract_images_info_text': 'Quá trình trích xuất có thể mất vài phút đối với PDF lớn.\n\nHình ảnh được lưu với tên gốc (trang_hinh_anh).',
        'extract_images_extract': 'Trích xuất',
        'extract_images_start': 'Bắt đầu trích xuất...',
        'extract_images_progress': 'Đang trích xuất hình ảnh...',
        'extract_images_success': '✅ Trích xuất hình ảnh thành công!\n\nĐã lưu {0} hình ảnh vào:\n{1}',
        'extract_images_complete': 'Đã hoàn thành trích xuất hình ảnh',
        'extract_images_cancel': 'Đã hủy trích xuất',
        'extract_images_error_format': 'Lỗi khi trích xuất hình ảnh:\n\n{0}',
        'extract_images_open_folder': '📁 Mở thư mục',
        'extract_images_no_images': 'Không tìm thấy hình ảnh nào trong PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Nhiều trang trên một trang (N-Up)',
        'nup_menu': 'Nhiều trang trên một trang (N-Up)',
        'nup_info': 'Sắp xếp nhiều trang PDF trên một trang.\n\nLý tưởng cho bản in nhỏ gọn, tổng quan hoặc tài liệu phát tay.',
        'nup_layout': 'Bố cục:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Xem trước:',
        'nup_preview_info': '{0} trang → {1} trang mỗi tờ → {2} tờ\nBố cục: {3}',
        'nup_order': 'Thứ tự:',
        'nup_order_horizontal': 'Ngang (theo hàng)',
        'nup_order_vertical': 'Dọc (theo cột)',
        'nup_order_horizontal_reverse': 'Ngang ngược',
        'nup_order_vertical_reverse': 'Dọc ngược',
        'nup_range': 'Phạm vi trang:',
        'nup_all_pages': 'Tất cả các trang',
        'nup_custom_range': 'Phạm vi tùy chỉnh',
        'nup_from': 'Từ:',
        'nup_to': 'Đến:',
        'nup_options': 'Tùy chọn:',
        'nup_margins': 'Lề:',
        'nup_margin_between': 'Khoảng cách giữa các trang:',
        'nup_page_numbers': 'Chèn số trang',
        'nup_target_folder': 'Thư mục đích:',
        'nup_browse': 'Duyệt...',
        'nup_select_folder': 'Chọn thư mục đích',
        'nup_create': 'Tạo',
        'nup_start': 'Bắt đầu N-Up...',
        'nup_progress': 'Đang tạo N-Up...',
        'nup_success': 'Tạo N-Up thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nBạn có muốn mở PDF mới không?',
        'nup_complete': 'Đã hoàn thành N-Up',
        'nup_cancel': 'Đã hủy N-Up',
        'nup_error_format': 'Lỗi khi tạo N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Thay đổi kích thước trang',
        'pagesize_menu': 'Thay đổi kích thước trang',
        'pagesize_info': 'Thay đổi kích thước trang của PDF.\n\nNội dung được tự động điều chỉnh theo kích thước mới.',
        'pagesize_format': 'Định dạng:',
        'pagesize_select': 'Chọn định dạng tiêu chuẩn:',
        'pagesize_custom': 'Kích thước tùy chỉnh:',
        'pagesize_width': 'Chiều rộng:',
        'pagesize_height': 'Chiều cao:',
        'pagesize_orientation': 'Hướng:',
        'pagesize_portrait': 'Dọc',
        'pagesize_landscape': 'Ngang',
        'pagesize_scale_options': 'Tùy chọn tỷ lệ:',
        'pagesize_fit': 'Điều chỉnh (giữ tỷ lệ khung hình)',
        'pagesize_stretch': 'Kéo giãn (làm méo)',
        'pagesize_center': 'Căn giữa (kích thước gốc)',
        'pagesize_range': 'Phạm vi trang:',
        'pagesize_all_pages': 'Tất cả các trang',
        'pagesize_custom_range': 'Phạm vi tùy chỉnh',
        'pagesize_from': 'Từ:',
        'pagesize_to': 'Đến:',
        'pagesize_target_folder': 'Thư mục đích:',
        'pagesize_browse': 'Duyệt...',
        'pagesize_select_folder': 'Chọn thư mục đích',
        'pagesize_apply': 'Áp dụng',
        'pagesize_start': 'Bắt đầu thay đổi kích thước trang...',
        'pagesize_progress': 'Đang thay đổi kích thước trang...',
        'pagesize_success': 'Thay đổi kích thước trang thành công!\n\nĐã lưu dưới dạng:\n{0}\n\nBạn có muốn mở PDF mới không?',
        'pagesize_complete': 'Đã hoàn thành thay đổi kích thước trang',
        'pagesize_cancel': 'Đã hủy thay đổi kích thước trang',
        'pagesize_error_format': 'Lỗi khi thay đổi kích thước trang:\n\n{0}',
        'pagesize_preview_info': 'Kích thước mới: {0} x {1} pt',
        'filename_pagesize_suffix': '_kich_thuoc_moi',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Thông tin PDF',
        'pdf_info_menu': 'Hiển thị thông tin PDF',
        'pdf_info_voice': 'Đang hiển thị thông tin PDF',
        'pdf_info_error': 'Lỗi khi hiển thị thông tin PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Hiển thị phím tắt",
        "shortcuts_dialog_title": "Phím tắt bàn phím",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 TỆP</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Mở PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Đóng PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Lưu thành...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Bảo vệ tài liệu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>In</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>In ngay (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Thoát ứng dụng</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 XUẤT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Xuất dưới dạng Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Xuất dưới dạng DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Xuất dưới dạng TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Xuất dưới dạng hình ảnh (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Trích xuất hình ảnh</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ XỬ LÝ TÀI LIỆU</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Nhiều trang)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Chuyển đổi PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Làm phẳng PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Chồng PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Tối ưu hóa PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ CHỈNH SỬA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Tìm kiếm</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Thêm đánh dấu trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Quản lý đánh dấu trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Đánh dấu trang tiếp theo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Đánh dấu trang trước</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Chạy OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 QUẢN LÝ TRANG</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Xoay trang hiện tại</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Xoay tất cả các trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Chuẩn hóa trang hiện tại</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Chuẩn hóa tất cả các trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Xóa trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Trích xuất trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Chèn trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Di chuyển trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Hợp nhất PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Thay đổi kích thước trang</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 CHÈN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Chèn văn bản</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Chèn dấu gạch chéo</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Chèn chữ ký 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Chèn chữ ký 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Chèn hình ảnh</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Chèn hình chữ nhật</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Chèn hình elip</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Chèn đường thẳng</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Chèn mũi tên</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Chèn số trang</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Hình mờ văn bản</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Hình mờ hình ảnh</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ CHE XÓA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Che xóa (đen)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Che xóa (trắng)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Áp dụng tất cả che xóa</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ NÂNG CAO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Cắt PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Chỉnh sửa siêu dữ liệu</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ XEM</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Chuyển đổi Chế độ Tối/Sáng</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Hiển thị cửa sổ văn bản</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Chiều rộng trang (Phóng to)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Hai trang (Phóng to)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Tổng quan (Phóng to)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ CÀI ĐẶT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Quản lý mật khẩu</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Cài đặt OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Cài đặt chữ ký</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Định dạng tên tệp</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Xuất cài đặt</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Nhập cài đặt</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ THÔNG TIN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Hiển thị thông tin PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Bật/tắt đầu ra giọng nói</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Tập trung vào thanh menu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Đã có phiên bản mới",
        "update_available_message": "Có phiên bản mới <b>{0}</b>.\n\nTruy cập trang phát hành để tải bản cập nhật:\n{1}",
        "update_available_voice": "Đã có phiên bản mới {0}. Vui lòng tải bản cập nhật từ trang GitHub.",
        "update_open_release": "Mở trang phát hành",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Tải tất cả bản dịch",
        "ask_download_all_translations": """Ngoài tiếng Đức, Anh và Việt, còn có {total_languages} ngôn ngữ giao diện khác.\n\nCó nên cung cấp / cập nhật chúng không?\n\nLưu ý:\nBạn có thể xóa thủ công các ngôn ngữ không cần thiết sau trong thư mục:\n{translations_path}
        \nNếu bạn hủy, bạn có thể tải ngôn ngữ giao diện sau qua menu 'Công cụ → Cập nhật bản dịch'.""",
        "menu_update_translations": "Cập nhật bản dịch",
        "translations_updated": "Đã cập nhật bản dịch",
        "translations_update_success": "Đã cập nhật thành công {} bản dịch ({} mới, {} đã cập nhật).",
        "translations_update_error": "Lỗi khi cập nhật bản dịch",
        "translations_update_no_changes": "Tất cả bản dịch đã được cập nhật.",
        "translations_update_offline": "Không có kết nối Internet. Không thể cập nhật bản dịch.",
        "translations_update_in_progress": "Đang cập nhật bản dịch trong nền...",
        "translations_downloading": "Đang tải bản dịch...",
        "translations_path_hint": "Thư mục người dùng cho bản dịch",
        "translations_update_not_available_title": "Không có bản cập nhật",
        "translations_update_not_available_message": """Cập nhật bản dịch chỉ có sẵn trong phiên bản đã cài đặt.\n\nTrong chế độ phát triển, bản dịch đã được cập nhật.""",
        "translations_update_no_internet_title": "Không có kết nối Internet",
        "translations_update_no_internet_message": """Không thể thiết lập kết nối Internet.\n\nKhông thể tải bản dịch từ GitHub.\n\nGiải pháp khả thi:
        • Kiểm tra kết nối Internet của bạn
        • Tạm thời tắt tường lửa
        • Thử lại sau
        \nBạn cũng có thể tải bản dịch thủ công từ GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Đang cập nhật",
        "btn_retry": "Thử lại",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Chào mừng đến với PDF Dark View",
        "welcome_title_not_supported": "Chào mừng đến với PDF Dark View",
        "welcome_message": "Chào mừng đến với PDF Dark View!\n\nNgôn ngữ hệ thống của bạn được phát hiện là '{language}'.\nBạn có muốn sử dụng ngôn ngữ này cho giao diện người dùng không?\n\nBạn có thể thay đổi ngôn ngữ bất kỳ lúc nào qua 'Cài đặt → Ngôn ngữ'.",
        "welcome_message_language_not_available": "Chào mừng đến với PDF Dark View!\n\nNgôn ngữ hệ thống của bạn được phát hiện là '{language}'.\nNgôn ngữ này chưa được cài đặt.\n\nBạn có muốn tải bản dịch cho {language} ngay bây giờ từ GitHub không?\n\n(Ngôn ngữ sẽ được tự động sử dụng cho giao diện người dùng.)",
        "welcome_message_language_not_supported": "Chào mừng đến với PDF Dark View!\n\nNgôn ngữ hệ thống của bạn được phát hiện là '{language}'.\nRất tiếc, chưa có bản dịch cho ngôn ngữ này.\n\nGiao diện người dùng sẽ được hiển thị bằng {fallback_language}.\n\nBạn có thể thay đổi ngôn ngữ bất kỳ lúc nào qua 'Cài đặt → Ngôn ngữ'.\nNếu muốn, bạn cũng có thể đóng góp bản dịch cho ngôn ngữ của mình:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Có, sử dụng ngôn ngữ hệ thống",
        "welcome_keep_english": "Không, giữ tiếng Anh",
        "welcome_download_language": "Có, tải {language}",

        # ============================================
        # 107. ĐƯỜNG DẪN GẦN ĐÂY
        # ============================================
        'menu_recent': 'Gần đây',
        'menu_recent_dirs': 'Thư mục...',
        'menu_recent_files': 'Tệp...',
        'recent_manage': 'Quản lý...',
        # Recent Paths - Cài đặt
        'recent_enable_tracking': 'Lưu đường dẫn gần đây (Quyền riêng tư)',
        'recent_enable_info': 'Tắt tùy chọn này để không lưu bất kỳ đường dẫn nào',
        'recent_tracking_disabled': 'Theo dõi đường dẫn đã tắt',
        'recent_enabled': 'đã bật',
        'recent_disabled': 'đã tắt',
        'recent_tracking_status': 'Theo dõi đường dẫn {0}',
        # Recent Paths - Hộp thoại
        'recent_dialog_title': 'Đường dẫn gần đây',
        'recent_tab_directories': 'Thư mục',
        'recent_tab_files': 'Tệp',
        'recent_dirs_instruction': 'Nhấp đúp để mở hộp thoại tệp trong thư mục',
        'recent_files_instruction': 'Nhấp đúp để mở trực tiếp PDF',
        'recent_no_directories': '(không có thư mục nào được lưu)',
        'recent_no_files': '(không có tệp nào được lưu)',
        'recent_default_current': '⭐ Mặc định: {0}',
        'recent_set_as_default': '⭐ Đặt làm mặc định',
        'recent_default_set_title': 'Đã đặt thư mục mặc định',
        'recent_default_set_message': 'Thư mục "{0}" đã được đặt làm mặc định để mở PDF.',
        'recent_default_set_voice': 'Đã đặt thư mục mặc định',
        'recent_directory_not_found': 'Không tìm thấy thư mục',
        'recent_file_not_found': 'Không tìm thấy tệp',
        'recent_remove_selected': 'Xóa',
        'recent_remove_title': 'Xóa đường dẫn',
        'recent_remove_confirm': 'Bạn có chắc chắn muốn xóa đường dẫn "{0}" khỏi danh sách?',
        'recent_path_removed': 'Đã xóa đường dẫn',
        'recent_clear_all': 'Xóa tất cả',
        'recent_clear_title': 'Xóa tất cả đường dẫn',
        'recent_clear_confirm_type': 'Bạn có chắc chắn muốn xóa tất cả {0}?',
        'recent_cleared': 'Đã xóa danh sách',
        'recent_path_not_found_title': 'Không tìm thấy đường dẫn',
        'recent_path_not_found_message': 'Đường dẫn "{0}" không còn tồn tại.',
        'recent_open_file': 'Mở tệp',
        'btn_open_recent': 'Mở',
        'recent_open_file_question': 'Bạn có muốn mở "{0}" dưới dạng PDF?',
        'recent_not_pdf': 'Tệp được chọn không phải là PDF.',
        'recent_more_entries': 'Thêm mục...',
        'btn_remove': 'Xóa',
        'btn_clear': 'Xóa tất cả',
        # Recent Paths - Menu ngữ cảnh
        'recent_context_open': 'Mở',
        'recent_context_reveal': 'Hiển thị trong Finder',
        'recent_context_set_default': '⭐ Đặt làm mặc định',
        'recent_context_open_terminal': '💻 Mở Terminal',
        'recent_context_file_info': 'Thông tin tệp',
        'recent_context_open_with_default': '📄 Mở với ứng dụng mặc định',
        'recent_context_remove': 'Xóa khỏi danh sách',
        'recent_context_clear_all': 'Xóa tất cả',
        # Recent Paths - Thông tin tệp
        'recent_file_info_title': 'Thông tin tệp',
        'recent_file_info_name': 'Tên',
        'recent_file_info_path': 'Đường dẫn',
        'recent_file_info_size': 'Kích thước',
        'recent_file_info_modified': 'Đã sửa đổi',
        'recent_file_info_pages': 'Trang',
        # Recent Paths - Lỗi
        'recent_error_reveal': 'Lỗi khi mở trong Finder',
        'recent_error_terminal': 'Lỗi khi mở Terminal',
        'recent_error_info': 'Lỗi khi lấy thông tin tệp',
        # USER DATA FOLDER
        'open_user_folder': 'Hiển thị thư mục dữ liệu người dùng',

        # ============================================
        # 108. THOÁT CHƯƠNG TRÌNH
        # ============================================
        "app_quitting": "Chương trình đang thoát",

    }

