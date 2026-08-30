
# ============================================
# translations_ko.py - 한국어 사전
# Vollständig sortiert nach Kategorien
# ============================================

def load_korean_strings():
    """Lädt alle koreanischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF 열기",
        'btn_text_window': "OCR 텍스트",
        'btn_first': "첫 페이지",
        'btn_prev': "이전 페이지",
        'btn_next': "다음 페이지",
        'btn_last': "마지막 페이지",
        'btn_print': "인쇄",
        'btn_darkmode_light': "라이트 모드",
        'btn_darkmode_dark': "다크 모드",
        'btn_delete_pages': "페이지 삭제",
        'btn_extract_pages': "페이지 추출",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "확인",
        'btn_cancel': "취소",
        'btn_save': "저장",
        'btn_close': "닫기",
        'btn_delete': "삭제",
        'btn_delete_all': "모두 삭제",
        'btn_copy': "복사",
        'btn_export': "내보내기",
        'btn_show': "비밀번호 표시",
        'btn_hide': "비밀번호 숨기기",
        'btn_authenticate': "인증",
        'btn_settings': "설정",
        'btn_protect': "보호",
        'btn_remove_password': "비밀번호 제거",
        'btn_manage': "비밀번호 관리",
        'btn_retry': "다시 시도",
        'btn_select_all': "모두 선택",
        'btn_clear_selection': "선택 해제",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "{0} / {1} 페이지",
        'page_count': "/ {0}",
        'goto_page': "페이지 이동",
        'page_simple': "{0} 페이지",
        'full_view_page': "페이지 {0} 전체 화면",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "검색어 입력 + Enter",
        'search_results': "결과: {0} / {1}",
        'search_nav_hint': "Enter: 다음 (Shift+Enter: 이전) 결과",
        'search_no_results': "결과 없음",
        'search_error': "검색 오류",
        'search_active': "검색 필드 활성화됨",
        'search_closed': "검색 종료됨",
        'search_position': "페이지 {0} {1}",
        'search_pos_top': "맨 위",
        'search_pos_upper': "위",
        'search_pos_middle': "중간",
        'search_pos_lower': "아래",
        'search_pos_bottom': "맨 아래",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "텍스트 인식이 성공적으로 완료되었습니다!",
        'ocr_success_title': "OCR 성공",
        'ocr_success_message': "이제 문서를 검색할 수 있습니다.",
        'ocr_failed': "OCR 실패",
        'ocr_in_progress': "OCR 진행 중",
        'ocr_preparing': "PDF 준비 중...",
        'ocr_analyzing': "PDF 분석 중...",
        'ocr_optimizing': "이미지 최적화 중...",
        'ocr_recognizing': "텍스트 인식 중...",
        'ocr_embedding': "텍스트 삽입 중...",
        'ocr_finalizing': "PDF 마무리 중...",
        'ocr_not_available': "OCR을 사용할 수 없습니다",
        'ocr_install_message': "OCR 도구를 찾을 수 없습니다.\n\n설치하십시오:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR이 필요합니다",
        'ocr_question': "PDF에 검색 가능한 텍스트가 없습니다.\n{0}을(를) 활성화하기 위해 OCR을 실행하시겠습니까?",
        'ocr_perform': "OCR 실행",
        'ocr_later': "나중에",
        'ocr_starting': "보장된 OCR을 시작하는 중...",
        'ocr_success_voice': "OCR 성공. PDF를 이제 검색할 수 있습니다.",
        'ocr_partial_success': "OCR이 실행되었지만 교체 중에 문제가 발생했습니다.\n\n검색 가능한 버전이 다음 위치에 저장되었습니다:\n{0}\n\n오류: {1}",
        'ocr_partial_title': "OCR 부분 성공",
        'ocr_partial_voice': "OCR이 실행되었지만 교체에 실패했습니다.",
        'original_file': "원본 파일:",
        'old_size': "이전 크기:    {0} 바이트",
        'new_size': "새 크기: {0} 바이트",
        'size_change': "변경: {0}{1} 바이트",
        'backup_created_file': "백업이 생성되었습니다:\n{0}",
        'backup_not_created': "백업이 생성되지 않았습니다 (설정이 비활성화됨)",
        'page_header': "=== 페이지 {0} ===\n{1}\n",
        'scanned_page_header': "=== 페이지 {0} (스캔됨) ===\n[이 페이지에는 스캔된 텍스트만 포함되어 있습니다]\n[수동으로 OCR을 실행하십시오]\n",
        'scanned_warning': "⚠️ 스캔된 텍스트 - OCR 필요",
        'guaranteed_title': "검색 가능한 PDF가 생성되었습니다",
        'guaranteed_message': "<b>보장된 검색 가능 버전이 생성되었습니다!</b>\n\n자동 OCR이 실패했으므로 대체 검색 가능 PDF가 생성되었습니다:\n\n{0}\n\n<b>이 파일에는 다음이 포함됩니다:</b>\n• 추출된 텍스트 (있는 경우)\n• 스캔된 페이지에 대한 지침\n• 완전히 검색 가능",
        'guaranteed_voice': "보장된 검색 가능 PDF가 생성되었습니다.",
        'instruction_title': "OCR 지침",
        'instruction_file': "원본 파일: {0}",
        'instruction_text': "자동 텍스트 인식(OCR)이 실패했습니다.\n수동으로 OCR을 실행하십시오:\n\n1. OCRmyPDF 사용 (명령줄):\n   ocrmypdf --force-ocr \"[파일]\" \"출력.pdf\"\n\n2. Adobe Acrobat 사용 (macOS/Windows):\n   • Acrobat에서 PDF 열기\n   • 도구 > PDF 편집\n   • '텍스트 인식' 선택\n\n3. 미리보기 사용 (macOS):\n   • 미리보기에서 PDF 열기\n   • 파일 > 내보내기...\n   • Quartz 필터: '파일 크기 줄이기'\n   • 'OCR 실행' 활성화\n\n4. 온라인 OCR 서비스:\n   • smallpdf.com/kr/ocr-pdf\n   • ilovepdf.com/kr/ocr-pdf\n   • adobe.com/kr/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR 지침이 생성되었습니다",
        'instruction_created_message': "자세한 지침이 생성되었습니다:\n\n{0}\n\n수동 OCR 단계를 따르십시오.",
        'instruction_created_voice': "OCR 지침이 생성되었습니다.",
        'ocr_impossible': "OCR이 불가능합니다",
        'ocr_impossible_message': "OCR을 실행할 수 없습니다.\n\nOCR 소프트웨어로 '{0}'을(를) 수동으로 처리하십시오.",
        'ocr_impossible_voice': "OCR이 불가능합니다. 수동으로 처리하십시오.",
        'emergency_title': "긴급 OCR",
        'emergency_message': "긴급 PDF가 생성되었습니다:\n\n{0}\n\n이 파일을 OCR로 수동 처리하십시오.",
        'emergency_voice': "긴급 PDF가 생성되었습니다. 수동으로 OCR을 실행하십시오.",
        'critical_error': "심각한 오류",
        'critical_error_message': "OCR을 시작할 수 없습니다.\n\n프로그램을 다시 시작하고 OCR 설치를 확인하십시오.",
        'critical_error_voice': "심각한 OCR 오류",
        'ocr_question_html': "<p>PDF에 검색 가능한 텍스트가 없습니다.<p>{0}을(를) 활성화하기 위해 OCR을 실행하시겠습니까?</p>",
        'ocr_question_voice': "OCR이 필요합니다. PDF에 검색 가능한 텍스트가 없습니다. {0}을(를) 활성화하기 위해 OCR을 실행하시겠습니까?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "로드된 PDF 없음",
        'no_pdf_message': "로드된 PDF가 없습니다",
        'pdf_not_found': "PDF 파일을 찾을 수 없습니다",
        'file_size': "파일 크기",
        'bytes': "바이트",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "백업이 생성되었습니다",
        'backup_disabled': "백업이 비활성화되었습니다",
        'backup_activated': "백업 생성이 활성화되었습니다",
        'backup_deactivated': "백업 생성이 비활성화되었습니다",
        'backup_status': "백업: {0}",
        'backup_on': "✔ 활성화",
        'backup_off': "✘ 비활성화",
        'close_pdf': "PDF 닫는 중: {0}",
        'pdf_not_found_format': "PDF 파일을 찾을 수 없습니다: {0}",
        'error_pdf_load_format': "PDF 로드 중 오류 발생: {0}",
        'load_failed_format': "로드 실패:\n{0}",
        'decrypted_suffix': "(복호화됨)",
        'decryption_failed': "복호화에 실패했습니다.",
        'decryption_error': "복호화 중 오류 발생",
        'decryption_success': "성공적으로 복호화되었습니다",
        'decryption_success_message': "PDF가 복호화되어 다음 위치에 저장되었습니다:\n\n{0}",
        'decryption_success_voice': "PDF가 복호화되어 저장되었습니다.",
        'password_remove_error': "비밀번호 제거 중 오류 발생",
        'save_unencrypted': "암호화되지 않은 PDF를 다른 이름으로 저장",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "다른 이름으로 저장...",
        'save_copy': "복사본 저장",
        'save_success': "PDF가 저장되었습니다: {0}",
        'save_encrypted': "보호된 PDF가 저장되었습니다: {0}",
        'save_error': "PDF를 저장할 수 없습니다",
        'encryption_question': "PDF를 비밀번호로 보호하시겠습니까?",
        'encryption_yes': "예",
        'encryption_no': "아니요",
        'encryption_cancel': "취소",
        'save_cancel': "저장이 취소되었습니다",
        'save_encrypted_voice': "파일이 암호화되어 저장되었습니다.",
        'save_success_voice': "PDF 파일이 암호화되지 않고 저장되었습니다.",
        'save_error_format': "PDF를 저장할 수 없습니다:\n{0}",
        'export_pages_success': "Pages로 내보내기 성공",
        'export_pages_error': "Pages로 내보내기 실패",
        'export_pages_error_format': "Pages로 내보내기 실패: {0}",
        'export_word_success': "Word로 내보내기 성공",
        'export_word_error': "Word로 내보내기 실패",
        'export_word_error_format': "Word로 내보내기 실패: {0}",
        'export_text_success': "텍스트 내보내기 성공",
        'export_text_error': "텍스트 내보내기 실패",
        'export_text_error_format': "텍스트 내보내기 실패: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "비밀번호가 필요합니다",
        'password_enter': "비밀번호를 입력하십시오",
        'password_confirm': "비밀번호 확인",
        'password_new': "새 비밀번호",
        'password_current': "현재 비밀번호",
        'password_save': "비밀번호 저장 (암호화됨)",
        'password_saved': "✓ 이 파일의 비밀번호가 저장되었습니다",
        'password_wrong': "잘못된 비밀번호",
        'password_mismatch': "비밀번호가 일치하지 않습니다",
        'password_too_short': "비밀번호가 너무 짧습니다",
        'password_min_length': "비밀번호는 최소 4자 이상이어야 합니다",
        'password_strength': "비밀번호 강도",
        'password_strength_very_weak': "매우 약함",
        'password_strength_weak': "약함",
        'password_strength_medium': "보통",
        'password_strength_strong': "강함",
        'password_strength_very_strong': "매우 강함",
        'password_char_count': "({0}자)",
        'password_match': "✓ 일치",
        'password_no_match': "✗ 비밀번호가 일치하지 않습니다",
        'password_show': "표시",
        'password_hide': "숨기기",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "비밀번호 관리",
        'password_table_filename': "파일 이름",
        'password_table_password': "비밀번호",
        'password_count': "{0}개의 저장된 비밀번호",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "저장된 비밀번호가 없습니다",
        'password_copied': "{0}개의 비밀번호가 복사되었습니다",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "정말로 '{0}'의 비밀번호를 삭제하시겠습니까?",
        'password_delete_multiple': "정말로 선택한 {0}개의 비밀번호를 삭제하시겠습니까?",
        'password_delete_all_confirm': "정말로 저장된 모든 비밀번호({0}개)를 삭제하시겠습니까?",
        'password_deleted': "{0}개의 비밀번호가 삭제되었습니다",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "모든 비밀번호가 삭제되었습니다",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "비밀번호 생성기",
        'generator_generated': "생성된 비밀번호:",
        'generator_regenerate': "다시 생성",
        'generator_copy': "복사",
        'generator_use': "사용",
        'generator_settings': "설정",
        'generator_length': "길이:",
        'generator_group_every': "구분 기호",
        'generator_group_chars': "자마다.    구분 기호:",
        'generator_uppercase': "대문자 (A-Z)",
        'generator_lowercase': "소문자 (a-z)",
        'generator_digits': "숫자 (0-9)",
        'generator_symbols': "특수 문자 (!@#$%^&*)",
        'generator_exclude': "제외:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "마스터 비밀번호가 필요합니다",
        'master_password_setup': "마스터 비밀번호 설정",
        'master_password_change': "마스터 비밀번호 변경",
        'master_password_enter': "마스터 비밀번호를 입력하십시오",
        'master_password_choose': "강력한 마스터 비밀번호를 선택하십시오 (최소 8자)",
        'master_password_new': "새 마스터 비밀번호를 입력하십시오",
        'master_password_confirm': "비밀번호 확인",
        'master_password_authenticate': "인증",
        'master_password_success': "마스터 비밀번호가 성공적으로 설정되었습니다.",
        'master_password_changed': "마스터 비밀번호가 성공적으로 변경되었습니다.",
        'master_password_removed': "마스터 비밀번호와 모든 비밀번호가 삭제되었습니다.",
        'master_password_remove': "마스터 비밀번호 제거",
        'master_password_remove_confirm': "정말로 모든 비밀번호를 삭제하시겠습니까?\n\n이 작업은 되돌릴 수 없습니다!",
        'master_password_export_before': "미리 백업을 내보내시겠습니까?",
        'master_password_export_delete': "내보내고 삭제",
        'master_password_delete_now': "지금 삭제",
        'master_password_for_signatures': "서명을 사용하려면 마스터 비밀번호를 설정해야 합니다.\n\n지금 마스터 비밀번호를 설정하시겠습니까?",
        'master_password_for_private': "개인 텍스트 블록을 사용하려면 마스터 비밀번호를 설정해야 합니다.\n\n지금 마스터 비밀번호를 설정하시겠습니까?",
        'master_password_info': """
            <b>🔐 마스터 비밀번호 없음:</b><br>
            • 비밀번호 표시, 복사, 내보내기 불가능<br>
            • 비밀번호 삭제는 항상 가능 (마스터 비밀번호 없어도 가능)<br><br>

            <b>🔐 마스터 비밀번호 있음:</b><br>
            • 인증 후 모든 기능 사용 가능<br>
            • 비밀번호는 마스터 비밀번호로 암호화됨<br>
            • 최소 길이: 8자<br>
            • 안전한 SHA-256 해시 저장<br><br>

            <b>중요:</b><br>
            • 마스터 비밀번호를 분실하면 비밀번호를 복구할 수 없습니다<br>
            • 마스터 비밀번호를 제거하면 모든 비밀번호가 삭제됩니다<br>
            • 삭제 전 내보내기 옵션이 있습니다<br>
            • 마스터 비밀번호는 언제든지 변경할 수 있습니다
        """,
        'signature_auth_disabled': "서명에 대한 비밀번호 요청 비활성화",
        'template_auth_disabled': "개인 텍스트 블록에 대한 비밀번호 요청 비활성화",
        'master_password_for_signatures_settings': "서명을 사용하려면 마스터 비밀번호를 설정해야 합니다.\n\n설정 → 비밀번호 관리로 이동하십시오",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF 보호",
        'protect_info': "파일 '{0}'이(가) 비밀번호로 보호됩니다.",
        'protect_instruction': "원하는 비밀번호를 두 번 입력하여 문서를 보호하거나, 입력 필드 오른쪽의 비밀번호 생성기를 사용하십시오.",
        'protect_success': "PDF가 성공적으로 보호되어 다음 위치에 저장되었습니다:\n{0}\n\n비밀번호: {1}\n\n보호된 PDF를 지금 여시겠습니까?",
        'protect_open': "예",
        'protect_skip': "아니요",
        'protect_error': "PDF 보호 중 오류 발생",
        'protect_open_title': "보호된 PDF 열기",
        'protect_question': "완료되었습니다. 보호된 PDF를 지금 여시겠습니까? 예 또는 아니요?",
        'password_cancel': "비밀번호 대화상자가 취소되었습니다",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "페이지 삭제",
        'pages_extract': "페이지 추출",
        'pages_insert': "페이지 삽입",
        'pages_move': "페이지 이동",
        'pages_delete_options': "삭제 옵션",
        'pages_delete_empty': "모든 빈 페이지 삭제",
        'pages_delete_current': "현재 페이지 삭제",
        'pages_delete_range': "페이지 범위 삭제",
        'pages_extract_options': "추출 옵션",
        'pages_extract_current': "현재 페이지 추출",
        'pages_extract_range': "페이지 범위 추출",
        'pages_insert_position': "삽입 위치",
        'pages_insert_before': "페이지 앞에 삽입:",
        'pages_insert_select': "PDF 선택",
        'pages_insert_none': "선택된 PDF 없음",
        'pages_move_source': "이동할 페이지",
        'pages_move_from': "시작 페이지:",
        'pages_move_to': "끝 페이지:",
        'pages_move_target': "대상 위치",
        'pages_move_before': "페이지 앞으로 이동:",
        'pages_move_hint': "참고: 1페이지 = 시작, {0} = 끝",
        'pages_range_invalid': "시작 페이지는 끝 페이지보다 작거나 같아야 합니다.",
        'pages_position_invalid': "대상 위치는 이동 범위 내에 있을 수 없습니다.",
        'pages_no_pdf_selected': "선택된 PDF가 없습니다.",
        'pages_deleted': "{0}페이지가 삭제되었습니다.",
        'pages_extracted': "추출됨: {0}\n저장 위치: {1}\n파일 크기: {2:.1f} KB",
        'pages_inserted': "{0}페이지가 삽입되었습니다",
        'pages_moved': "{0}페이지가 이동되었습니다.",
        'pages_deleted_none': "삭제된 페이지가 없습니다.",
        'pages_delete_progress': "페이지 삭제 중...",
        'pages_deleted_with_backup': "{0}페이지가 삭제되었습니다.\n\n백업: {1}",
        'pages_deleted_voice': "백업이 생성되고 {0}페이지가 삭제되었습니다.",
        'info': "정보",
        'error_dialog_creation': "대화상자를 생성할 수 없습니다",
        'extract_page_single': "{0}페이지 추출",
        'extract_page_range': "{0}-{1}페이지 추출",
        'extract_success_voice': "페이지가 성공적으로 추출되었습니다",
        'extract_error_format': "추출 중 오류 발생: {0}",
        'pages_inserted_voice': "{0}페이지가 삽입되었습니다.",
        'insert_error_format': "삽입 중 오류 발생: {0}",
        'pages_move_progress': "페이지 이동 중...",
        'pages_moved_with_backup': "{0}페이지가 이동되었습니다.\n\n백업: {1}",
        'move_success_title': "이동 성공",
        'pages_moved_voice': "{0}페이지가 성공적으로 이동되었습니다",
        'mark_removed': "페이지 {0}의 표시가 제거되었습니다",
        'mark_empty': "페이지 {0}이(가) 빈 페이지로 표시되었습니다",
        'mark_export_removed': "페이지 {0}의 내보내기 표시가 제거되었습니다",
        'mark_export': "페이지 {0}이(가) 내보내기용으로 표시되었습니다",
        'no_empty_pages': "삭제할 빈 페이지가 표시되지 않았습니다",
        'delete_empty_confirm': "표시된 {0}개의 빈 페이지를 모두 삭제하시겠습니까?",
        'delete_empty_confirm_voice': "지금 표시된 {0}개의 빈 페이지를 삭제하시겠습니까? 예 또는 아니요.",
        'empty_pages_deleted': "{0}개의 빈 페이지가 삭제되었습니다",
        'no_export_pages': "내보내기용으로 표시된 페이지가 없습니다",
        'overwrite_title': "기존 파일 덮어쓰기",
        'overwrite_question': "파일\n\n{0}\n\n이(가) 이미 존재합니다.\n덮어쓰시겠습니까?",
        'overwrite_voice': "기존 파일을 덮어쓰시겠습니까? 예 또는 아니요.",
        'page_skipped': "페이지 {0}이(가) 건너뛰어졌습니다",
        'export_complete': "내보내기가 완료되었습니다.",
        'export_complete_voice': "내보내기가 완료되었습니다.",
        'no_pages_exported': "내보낸 페이지가 없습니다",
        'export_cancelled': "내보내기가 취소되었습니다",
        'pages_exported': "{0}페이지가 {1}(으)로 내보내졌습니다",
        'export_page_title': "페이지 내보내기",
        'page_exported': "페이지 {0}이(가) {1}(으)로 내보내졌습니다",
        'export_error': "내보내기 중 오류 발생",
        'export_marked_title': "표시된 페이지 내보내기",
        'rotate_all_title': "모든 페이지 회전",
        'rotate_all_question': "모든 페이지를 오른쪽으로 90도 회전하시겠습니까?",
        'rotate_all_voice': "모든 페이지를 오른쪽으로 90도 회전하시겠습니까? 예 또는 아니요?",
        'all_pages_rotated': "모든 페이지가 회전되었습니다",
        'page_rotated': "페이지 {0}이(가) 회전되었습니다",
        'rotate_error': "페이지를 회전할 수 없습니다",
        'delete_page_confirm': "페이지 {0}을(를) 삭제하시겠습니까?",
        'delete_page_confirm_voice': "정말로 페이지 {0}을(를) 삭제하시겠습니까? 예 또는 아니요.",
        'page_deleted': "페이지 {0}이(가) 삭제되었습니다",
        'delete_error': "페이지를 삭제할 수 없습니다",
        'pages_deleted_voice': "{0}페이지가 삭제되었습니다",
        'pages_exported_split': "{0}페이지가 성공적으로 내보내졌습니다.",
        'pages_skipped': "{0}페이지가 건너뛰어졌습니다.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "페이지 추출 (고급)",
        'pdf_splitter_title': "PDF 분할 및 추출기",
        'pdf_splitter_load': " PDF 파일 선택",
        'pdf_splitter_info': "PDF 문서에 대한 옵션을 선택하십시오",
        'pdf_splitter_basic': "기본 작업",
        'pdf_splitter_single': "개별 페이지로 분할",
        'pdf_splitter_range': "페이지 추출:",
        'pdf_splitter_range_placeholder': "예: 1-3,5,7-9",
        'pdf_splitter_clean': "정리 작업",
        'pdf_splitter_remove_empty': "모든 빈 페이지 제거",
        'pdf_splitter_remove': "페이지 범위 삭제:",
        'pdf_splitter_remove_placeholder': "예: 2,4-6",
        'pdf_splitter_process': "PDF 처리",
        'pdf_splitter_loaded': "PDF가 로드되었습니다. 옵션을 선택하십시오",
        'pdf_read_error': "PDF를 읽을 수 없습니다",
        'pages': "페이지",
        'pages_created': "페이지가 생성되었습니다",
        'range_empty': "페이지 범위를 입력하십시오",
        'range_invalid': "잘못된 페이지 범위입니다",
        'range_created': "선택한 페이지로 새 PDF가 생성되었습니다:\n{0}",
        'empty_removed': "{0}개의 빈 페이지가 제거되었습니다.\n출력: {1}",
        'remove_empty': "제거할 페이지를 입력하십시오",
        'remove_invalid': "제거할 페이지가 잘못되었습니다",
        'remove_done': "정리된 PDF가 생성되었습니다:\n{0}",
        'open_folder': "폴더 열기",
        'show_in_finder': "Finder에 표시",
        'pdf_splitter_no_pdf': "먼저 PDF 파일을 로드하십시오.",
        'process_error': "PDF 처리 중 오류 발생",
        'pages_created_voice': "{0}페이지가 생성되었습니다",
        'range_created_voice': "선택한 페이지로 PDF가 생성되었습니다",
        'empty_removed_voice': "{0}개의 빈 페이지가 제거되었습니다",
        'remove_done_voice': "정리된 PDF가 생성되었습니다",
        'pdf_splitter_split_groups': "연속된 각 그룹을 별도 파일로",
        'range_created_single': "새 PDF가 생성되었습니다:\n{0}",
        'range_created_multiple': "{0}개의 PDF 파일이 생성되었습니다.",
        'range_created_voice_single': "선택한 페이지로 하나의 PDF가 생성되었습니다",
        'range_created_voice_multiple': "{0}개의 PDF 파일이 생성되었습니다",
        'empty_removed_none_left': "남은 페이지가 없습니다",
        'empty_removed_all_empty': "모든 페이지가 빈 페이지로 인식되어 제거됩니다. 파일이 생성되지 않았습니다.",
        'preview_single': "미리보기: {0}",
        'preview_enter_range': "페이지 범위를 입력하십시오.",
        'preview_invalid_range': "잘못된 페이지 범위입니다.",
        'preview_file': "미리보기: {0}",
        'preview_files': "미리보기: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "인쇄 시작",
        'print_sent': "인쇄 작업이 전송되었습니다",
        'print_now': "지금 인쇄",
        'print_error': "즉시 인쇄 중 오류 발생",
        'print_limited': "이 시스템에서는 인쇄 기능이 제한됩니다",
        'print_error_format': "즉시 인쇄 중 오류 발생: {0}",
        'warning': "경고",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "라이트 모드로 전환",
        'mode_switch_to_dark': "다크 모드로 전환",
        'mode_dark_activated': "다크 모드가 활성화되었습니다",
        'mode_light_activated': "라이트 모드가 활성화되었습니다",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "전체 화면",
        'zoom_two_pages': "두 페이지 나란히",
        'zoom_overview': "개요 모드",
        'zoom_cannot_during_search': "검색 중에는 확대/축소할 수 없습니다",
        'zoom_exit_first': "먼저 확대/축소를 종료하십시오",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "드래그 앤 드롭이 활성화되었습니다",
        'drag_disabled': "드래그 앤 드롭이 비활성화되었습니다",
        'drag_page_grab': "페이지 {0}을(를) 잡았습니다",
        'drag_page_dropped': "페이지 {0}이(가) 위치 {1}에 삽입되었습니다",
        'drag_position_invalid': "잘못된 위치입니다",
        'drag_same_position': "페이지 {0}은(는) 위치 {0}에 유지됩니다",
        'drag_error': "이동 중 오류 발생",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "고급 서식 및 텍스트 블록 관리가 포함된 텍스트 입력",
        'text_templates': "사용 가능한 텍스트 블록:",
        'text_name': "이름",
        'text_preview': "텍스트 미리보기",
        'text_enter': "텍스트:",
        'text_font_size': "글꼴 크기:",
        'text_formatting': "서식:",
        'text_bold': "굵게",
        'text_italic': "기울임꼴",
        'text_underline': "밑줄",
        'text_alignment': "정렬:",
        'text_left': "왼쪽",
        'text_center': "가운데",
        'text_right': "오른쪽",
        'text_color': "텍스트 색상:",
        'text_opacity': "불투명도:",
        'text_word_wrap': "줄 바꿈:",
        'text_auto': "자동",
        'text_page_width_95': "페이지 너비 (95%)",
        'text_page_width_85': "매우 넓음 (85%)",
        'text_page_width_75': "더 넓음 (75%)",
        'text_page_width_60': "넓음 (60%)",
        'text_page_width_50': "중간 (50%)",
        'text_page_width_30': "좁음 (30%)",
        'text_page_width_20': "더 좁음 (20%)",
        'text_page_width_10': "매우 좁음 (10%)",
        'text_no_wrap': "줄 바꿈 안 함",
        'text_private': "개인 텍스트 블록 (인증 필요)",
        'text_preview_label': "미리보기:",
        'text_preview_placeholder': "여기에 텍스트 미리보기가 표시됩니다...",
        'text_no_text': "(텍스트 없음)",
        'text_save_template': "💾 블록으로 저장",
        'text_delete_template': "🗑 선택한 텍스트 블록 삭제",
        'text_show_private': "개인 표시",
        'text_hide_private': "개인 숨기기",
        'text_use': "✅ 텍스트 사용",
        'text_saved': "텍스트 블록이 다음 이름으로 저장되었습니다:\n{0}",
        'text_saved_voice': "텍스트 블록이 저장되었습니다",
        'text_deleted': "텍스트 블록이 삭제되었습니다",
        'text_no_text_to_save': "저장할 텍스트가 없습니다.",
        'text_no_templates': "텍스트 블록을 찾을 수 없습니다",
        'text_private_master_required': "개인 블록은 마스터 비밀번호가 설정된 경우에만 사용할 수 있습니다.\n\n지금 마스터 비밀번호를 설정하시겠습니까?",
        'text_filename': "텍스트 블록의 파일 이름 ('Text_' 및 '.txt' 제외):",
        'text_filename_hint': "예: '전화 홈오피스'는 'Text_전화 홈오피스.txt'로 저장됩니다",
        'text_save_hint': "텍스트 블록은 서식과 함께 자동으로 저장됩니다.",
        'text_guide_title': "텍스트 입력 – 가이드",
        'text_delete_confirm': "정말로 이 텍스트 블록을 삭제하시겠습니까?\n\n파일: {0}\n텍스트: {1}...",
        'text_make_public': "공개로 표시",
        'text_make_private': "개인으로 표시",
        'text_privacy_changed': "개인 정보 상태가 변경되었습니다",
        'text_private_always': "개인 항상 표시 (설정)",
        'text_mode_required': "먼저 텍스트 모드를 활성화하십시오",
        'text_continue_editing': "편집 계속 – 커서가 텍스트 끝에 있습니다",
        'text_no_input': "입력된 텍스트가 없습니다 – 텍스트가 삭제되었습니다",
        'save_dialog_question': "어떻게 진행하시겠습니까?",
        'text_save_question': "모든 텍스트와 십자를 저장, 조정, 편집 계속 또는 삭제하시겠습니까?",
        'copy_cross': "십자가 복사되었습니다",
        'paste_cross': "십자가 붙여넣기되었습니다",
        'paste_text': "텍스트가 붙여넣기되었습니다",
        'cross_discarded': "십자가 삭제되었습니다",
        'all_discarded': "모두 삭제되었습니다",
        'text_discarded': "텍스트가 삭제되었습니다",
        'no_texts_to_save': "저장할 텍스트가 없습니다",
        'no_valid_texts': "저장할 유효한 텍스트가 없습니다",
        'text_word_singular': "텍스트",
        'text_word_plural': "텍스트",
        'cross_word_singular': "십자",
        'cross_word_plural': "십자",
        'texts_saved_title': "텍스트가 저장되었습니다",
        'texts_crosses_saved': "{0}개의 {1}와(과) {2}개의 {3}이(가) PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'texts_crosses_saved_voice': "{0}개의 {1}와(과) {2}개의 {3}이(가) 저장되었습니다.",
        'texts_saved': "{0}개의 {1}이(가) PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'texts_saved_voice': "{0}개의 {1}이(가) 저장되었습니다.",
        'crosses_saved': "{0}개의 {1}이(가) PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'crosses_saved_voice': "{0}개의 {1}이(가) 저장되었습니다.",
        'elements_saved': "{0}개의 요소가 PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'elements_saved_voice': "{0}개의 요소가 저장되었습니다.",
        'text_window_load_error': "텍스트 창을 로드할 수 없습니다",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **텍스트 입력 및 텍스트 블록 – 상세 가이드**

        **1. 텍스트 삽입 및 편집**
        - 문서에서 원하는 위치를 마우스 오른쪽 버튼으로 클릭하고 "텍스트 삽입"을 선택합니다.
        - 대화상자가 열리며 텍스트를 입력하고 서식을 지정할 수 있습니다:
        • 글꼴 크기, 굵게, 기울임꼴, 밑줄
        • 텍스트 색상 (자유 선택)
        • 투명도 (불투명도) 슬라이더
        • 줄 바꿈 (다양한 너비, 예: 페이지 너비, 좁게, 줄 바꿈 안 함)
        - 확인 후 텍스트가 클릭한 위치에 나타납니다. 마우스나 화살표 키로 이동할 수 있습니다.
        - 텍스트를 두 번 클릭하면 편집 모드가 열립니다. ESC를 누르면 종료됩니다.

        **2. 텍스트 블록(템플릿) 관리**
        - 텍스트 대화상자 왼쪽에 저장된 모든 텍스트 블록 목록이 표시됩니다.
        - **블록 저장:** 텍스트를 입력하고 서식을 지정한 후 "💾 블록으로 저장"을 클릭합니다. 파일 이름을 입력합니다 (확장자 없음).
        - **블록 로드:** 목록에서 원하는 이름을 클릭합니다. 텍스트와 서식이 로드되고 필요에 따라 조정할 수 있습니다.
        - **삭제:** 블록을 마우스 오른쪽 버튼으로 클릭하여 삭제하거나 개인 정보 상태를 변경합니다.

        **3. 개인 텍스트 블록 (마스터 비밀번호)**
        - 마스터 비밀번호를 설정한 경우 (설정 → 비밀번호 관리), 블록을 "개인"으로 표시할 수 있습니다.
        - 저장하기 전에 대화상자에서 "개인 텍스트 블록" 확인란을 선택합니다.
        - 개인 블록은 세션당 한 번 마스터 비밀번호를 입력한 경우에만 목록에 표시됩니다 (자물쇠 아이콘 또는 첫 액세스 시 인증).
        - 이렇게 하면 기밀 텍스트 블록을 무단 액세스로부터 보호할 수 있습니다.

        **4. 십자 삽입**
        - 컨텍스트 메뉴에서 그래픽 십자(예: 체크박스용)를 삽입할 수도 있습니다.
        - 십자의 크기, 선 두께, 색상은 설정에서 전역적으로 조정할 수 있습니다 (메뉴 "설정" → "십자 설정").
        - 기존 십자를 마우스 오른쪽 버튼으로 클릭하여 개별적으로 변경할 수 있습니다.

        **5. 일괄 작업**
        - 한 페이지에 여러 텍스트 또는 십자를 배치한 경우, 컨텍스트 메뉴(텍스트 모드에서 마우스 오른쪽 버튼 클릭)에서 모두 한 번에 저장하거나 삭제할 수 있습니다.
        - 저장하면 모든 요소가 PDF에 포함되고 벡터 그래픽으로 유지됩니다.

        **6. 텍스트 모드의 키보드 단축키**
        - 화살표 키: 요소 이동
        - Ctrl+화살표 키: 더 큰 단계
        - Enter: 저장 대화상자 열기 (모두 저장 / 조정 / 삭제)
        - ESC: 현재 요소 삭제
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 텍스트 입력 및 텍스트 블록 – 상세 가이드</strong></p>

        <p><strong>1. 텍스트 삽입 및 편집</strong></p>
        <ul>
        <li>문서에서 원하는 위치를 마우스 오른쪽 버튼으로 클릭하고 "텍스트 삽입"을 선택합니다.</li>
        <li>대화상자가 열리며 텍스트를 입력하고 서식을 지정할 수 있습니다:<br/>
        • 글꼴 크기, 굵게, 기울임꼴, 밑줄<br/>
        • 텍스트 색상 (자유 선택)<br/>
        • 투명도 (불투명도) 슬라이더<br/>
        • 줄 바꿈 (다양한 너비, 예: 페이지 너비, 좁게, 줄 바꿈 안 함)</li>
        <li>확인 후 텍스트가 클릭한 위치에 나타납니다. 마우스나 화살표 키로 이동할 수 있습니다.</li>
        <li>텍스트를 두 번 클릭하면 편집 모드가 열립니다. ESC를 누르면 종료됩니다.</li>
        </ul>

        <p><strong>2. 텍스트 블록(템플릿) 관리</strong></p>
        <ul>
        <li>텍스트 대화상자 왼쪽에 저장된 모든 텍스트 블록 목록이 표시됩니다.</li>
        <li><strong>블록 저장:</strong> 텍스트를 입력하고 서식을 지정한 후 "💾 블록으로 저장"을 클릭합니다. 파일 이름을 입력합니다 (확장자 없음).</li>
        <li><strong>블록 로드:</strong> 목록에서 원하는 이름을 클릭합니다. 텍스트와 서식이 로드되고 필요에 따라 조정할 수 있습니다.</li>
        <li><strong>삭제:</strong> 블록을 마우스 오른쪽 버튼으로 클릭하여 삭제하거나 개인 정보 상태를 변경합니다.</li>
        </ul>

        <p><strong>3. 개인 텍스트 블록 (마스터 비밀번호)</strong></p>
        <ul>
        <li>마스터 비밀번호를 설정한 경우 (설정 → 비밀번호 관리), 블록을 "개인"으로 표시할 수 있습니다.</li>
        <li>저장하기 전에 대화상자에서 "개인 텍스트 블록" 확인란을 선택합니다.</li>
        <li>개인 블록은 세션당 한 번 마스터 비밀번호를 입력한 경우에만 목록에 표시됩니다 (자물쇠 아이콘 또는 첫 액세스 시 인증).</li>
        <li>이렇게 하면 기밀 텍스트 블록을 무단 액세스로부터 보호할 수 있습니다.</li>
        </ul>

        <p><strong>4. 십자 삽입</strong></p>
        <ul>
        <li>컨텍스트 메뉴에서 그래픽 십자(예: 체크박스용)를 삽입할 수도 있습니다.</li>
        <li>십자의 크기, 선 두께, 색상은 설정에서 전역적으로 조정할 수 있습니다 (메뉴 "설정" → "십자 설정").</li>
        <li>기존 십자를 마우스 오른쪽 버튼으로 클릭하여 개별적으로 변경할 수 있습니다.</li>
        </ul>

        <p><strong>5. 일괄 작업</strong></p>
        <ul>
        <li>한 페이지에 여러 텍스트 또는 십자를 배치한 경우, 컨텍스트 메뉴(텍스트 모드에서 마우스 오른쪽 버튼 클릭)에서 모두 한 번에 저장하거나 삭제할 수 있습니다.</li>
        <li>저장하면 모든 요소가 PDF에 포함되고 벡터 그래픽으로 유지됩니다.</li>
        </ul>

        <p><strong>6. 텍스트 모드의 키보드 단축키</strong></p>
        <ul>
        <li>화살표 키: 요소 이동</li>
        <li>Ctrl+화살표 키: 더 큰 단계</li>
        <li>Enter: 저장 대화상자 열기 (모두 저장 / 조정 / 삭제)</li>
        <li>ESC: 현재 요소 삭제</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "십자 설정",
        'cross_properties': "십자 속성",
        'cross_size': "크기 (px):",
        'cross_line_width': "선 두께:",
        'cross_color': "색상:",
        'cross_choose_color': "선택",
        'cross_fine_tuning': "저장 시 미세 조정 (픽셀)",
        'cross_offset_x': "X 오프셋:",
        'cross_offset_y': "Y 오프셋:",
        'cross_offset_x_tooltip': "음수 값은 저장 시 십자를 왼쪽으로, 양수는 오른쪽으로 이동",
        'cross_offset_y_tooltip': "음수 값은 저장 시 십자를 위로, 양수는 아래로 이동",
        'cross_preview': "미리보기",
        'cross_save': "설정 적용",
        'cross_customized': "십자가 조정되었습니다",
        'cross_settings_applied': "십자 설정이 저장되었습니다.\n크기: {0}px, 선 두께: {1}px\n{2}",
        'cross_updated_count': "{0}개의 기존 십자가 업데이트되었습니다.",
        'cross_no_crosses': "기존 십자를 찾을 수 없습니다.",
        'cross_settings_applied_all': "십자 설정이 모든 {0}개의 십자에 적용되었습니다",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "서명 설정",
        'signature_1': "서명 1",
        'signature_2': "서명 2",
        'signature_select': "서명 선택",
        'signature_add': "➕ 새 서명 추가...",
        'signature_size': "서명 {0} 크기 (%):",
        'signature_common': "일반 설정",
        'signature_timestamp': "타임스탬프 자동 추가",
        'signature_location': "기본 위치:",
        'signature_timestamp_size': "타임스탬프 글꼴 크기:",
        'signature_no_files': "-- 서명을 찾을 수 없습니다 --",
        'signature_insert': "서명 삽입",
        'signature_insert_1': "서명 1 삽입",
        'signature_insert_2': "서명 2 삽입",
        'signature_customize': " 서명 조정",
        'signature_discard': " 이 서명 삭제",
        'signature_save_all': " 모든 서명 저장",
        'signature_discard_all': " 모든 서명 삭제",
        'signature_guide_title': "서명 – 가이드",
        'signature_guide': """
📝 서명 – 빠른 가이드

- 마스터 비밀번호 설정
- 설정 메뉴에서 서명 구성
  (크기, 타임스탬프 ...)
- 원하는 위치에서 마우스 오른쪽 버튼 클릭하여 삽입
  (마스터 비밀번호는 세션당 한 번 필요)
- 마우스 또는 화살표 키로 서명 이동
- 여러 서명을 연속으로 삽입 가능
- 각 서명을 개별적으로 조정 가능
- 단일 서명 삭제
- 모든 서명 한 번에 저장/삭제
- 메뉴 모음도 사용할 수 있습니다.
        """,
        'signature_placeholder': "미리보기를 사용할 수 없습니다",
        'signature_info': "서명 {0}: {1}×{2} 픽셀 ({3}% of {4}×{5})",
        'signature_info_placeholder': "서명 {0} 설정",
        'signature_inserted': "서명 {0}이(가) 페이지 {1}에 삽입되었습니다",
        'signature_deleted': "서명이 삭제되었습니다",
        'signature_copied': "서명이 복사되었습니다",
        'signature_pasted': "서명 {0}이(가) 붙여넣기되었습니다",
        'signature_saved': "{0}개의 서명이 PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'signature_saved_voice': "{0}개의 서명이 저장되었습니다",
        'mode_replace_signature_format': "모드 종료 및 서명 {0} 삽입",
        'mode_conflict_voice_signature': "모드 {0}이(가) 활성화되어 있습니다. 종료하고 서명을 삽입하시겠습니까?",
        'signature_not_configured': "서명 {0}이(가) 구성되지 않았습니다",
        'signature_file_not_found': "서명 파일을 찾을 수 없습니다",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "복사된 서명이 없습니다",
        'no_signatures_to_save': "저장할 서명이 없습니다",
        'signature_save_question': "모든 서명을 저장, 조정 또는 이 서명을 삭제하시겠습니까?",
        'signatures_saved_title': "서명이 저장되었습니다",
        'signatures_saved': "{0}개의 서명이 PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'signatures_saved_voice': "{0}개의 서명이 저장되었습니다.",
        'all_signatures_discarded': "모든 서명이 삭제되었습니다",
        'signature_settings_saved': "서명 설정이 저장되었습니다",
        'signature_cancelled': "서명이 삭제되었습니다",
        'signature_active_title': "서명 활성화됨",
        'signature_replace_question': "이미 활성화된 서명이 있습니다.\n\n현재 서명을 바꾸시겠습니까?",
        'signature_replace': "서명 바꾸기",
        'signature_replace_voice': "현재 서명을 바꾸시겠습니까 아니면 취소하시겠습니까?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "이미지 설정",
        'image_common': "일반 이미지 설정",
        'image_keep_aspect': "드래그 시 가로세로 비율 유지",
        'image_default_size': "기본 크기 (%):",
        'image_dark_invert': "다크 모드에서 이미지 반전",
        'image_dark_invert_tooltip': "활성화: 가시성을 높이기 위해 이미지가 반전됩니다",
        'image_fine_tuning': "미세 조정 (픽셀)",
        'image_offset_x': "X 오프셋:",
        'image_offset_y': "Y 오프셋:",
        'image_offset_x_tooltip': "음수 값은 저장 시 이미지를 왼쪽으로, 양수는 오른쪽으로 이동",
        'image_offset_y_tooltip': "음수 값은 저장 시 이미지를 위로, 양수는 아래로 이동",
        'image_select': "이미지 선택",
        'image_insert': "이미지 삽입",
        'image_customize': " 이미지 조정",
        'image_aspect': " 가로세로 비율 유지",
        'image_discard': " 이 이미지 삭제",
        'image_save_all': " 모든 이미지 저장",
        'image_discard_all': " 모든 이미지 삭제",
        'image_filter': "이미지",
        'image_guide_title': "이미지 삽입 – 가이드",
        'image_guide': """
📷 PDF에 이미지 삽입 – 빠른 가이드:

1. 원하는 위치에서 마우스 오른쪽 버튼 클릭
2. "이미지 삽입" → 이미지 선택
3. 이미지 배치: 마우스로 드래그
4. 크기 조정: 모서리/가장자리 드래그
5. 가로세로 비율 유지: [A] 키
6. 추가 조정: 이미지를 마우스 오른쪽 버튼으로 클릭

팁: 컨텍스트 메뉴에서 설정을 조정할 수 있습니다.
        """,
        'image_inserted': "이미지가 페이지 {1}에 삽입되었습니다",
        'image_deleted': "이미지가 삭제되었습니다",
        'image_copied': "이미지가 복사되었습니다",
        'image_pasted': "이미지가 붙여넣기되었습니다",
        'image_saved': "{0}개의 이미지가 PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'image_saved_voice': "{0}개의 이미지가 저장되었습니다",
        'image_aspect_on': "활성화",
        'image_aspect_off': "비활성화",
        'image_aspect_toggle': "가로세로 비율 유지 {0}",
        'image_reset': "이미지가 원래 크기로 재설정되었습니다",
        'image_replaced': "이미지가 교체되었습니다",
        'image_invalid': "잘못된 이미지입니다",
        'mode_replace_image': "이미지 삽입",
        'mode_conflict_voice_image': "모드 {0}이(가) 활성화되어 있습니다. 종료하고 이미지를 삽입하시겠습니까?",
        'image_active_title': "이미지 활성화됨",
        'image_replace_question': "이미 활성화된 이미지가 있습니다.\n\n현재 이미지를 바꾸시겠습니까?",
        'image_replace': "이미지 바꾸기",
        'image_replace_voice': "현재 이미지를 바꾸시겠습니까 아니면 취소하시겠습니까?",
        'image_filter_all': "이미지 (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;모든 파일 (*.*)",
        'no_copied_image': "복사된 이미지가 없습니다",
        'image_discarded': "이미지가 삭제되었습니다",
        'image_save_question': "모든 이미지를 저장, 조정 또는 이 이미지를 삭제하시겠습니까?",
        'no_images_to_save': "저장할 이미지가 없습니다",
        'no_valid_images': "저장할 유효한 이미지가 없습니다",
        'images_saved_title': "이미지가 저장되었습니다",
        'images_saved': "{0}개의 이미지가 PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'images_saved_voice': "{0}개의 이미지가 저장되었습니다.",
        'all_images_discarded': "모든 이미지가 삭제되었습니다",
        'image_settings_updated': "이미지 설정이 업데이트되었습니다",
        'image_replace_title': "새 이미지 선택",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "도형 설정",
        'form_basic': "기본 설정",
        'form_default_type': "기본 도형 유형:",
        'form_rectangle': "직사각형",
        'form_ellipse': "타원",
        'form_line': "선",
        'form_arrow': "화살표",
        'form_line_width': "선 두께:",
        'form_colors': "색상",
        'form_line_color': "선 색상:",
        'form_fill_color': "채우기 색상:",
        'form_choose_color': "선택",
        'form_transparent': "투명 배경 (선만)",
        'form_filled': "채우기",
        'form_dark_mode': "다크 모드",
        'form_dark_invert': "다크 모드에서 색상 반전",
        'form_fine_tuning': "미세 조정 (픽셀)",
        'form_offset_x': "X 오프셋:",
        'form_offset_y': "Y 오프셋:",
        'form_offset_x_tooltip': "음수 값은 저장 시 도형을 왼쪽으로, 양수는 오른쪽으로 이동",
        'form_offset_y_tooltip': "음수 값은 저장 시 도형을 위로, 양수는 아래로 이동",
        'form_preview': "미리보기",
        'form_insert': "도형 삽입",
        'form_rectangle_insert': "직사각형",
        'form_ellipse_insert': "타원/원",
        'form_line_insert': "선 (2회 클릭)",
        'form_arrow_insert': "화살표 (2회 클릭)",
        'form_customize': " 도형 조정",
        'form_transparent_toggle': " 투명 배경",
        'form_discard': " 이 도형 삭제",
        'form_save_all': " 모든 도형 저장",
        'form_discard_all': " 모든 도형 삭제",
        'form_guide_title': "도형 삽입 – 가이드",
        'form_guide': """
📐 PDF에 도형 삽입 – 빠른 가이드:

1. 도형 유형 선택 (직사각형, 타원, 선, 화살표)
2. 위치 클릭
   - 직사각형/타원: 한 번 클릭으로 도형 배치
   - 선/화살표: 두 번 클릭으로 시작점과 끝점 지정
3. 도형 배치: 마우스로 드래그
4. 크기 조정: 모서리/가장자리 드래그
5. 도형 저장: Enter
6. 도형 삭제: ESC
7. 추가 조정: 도형을 마우스 오른쪽 버튼으로 클릭

팁: 컨텍스트 메뉴에서 설정을 조정할 수 있습니다.
        """,
        'form_inserted': "{0}이(가) 페이지 {1}에 삽입되었습니다",
        'form_deleted': "도형이 삭제되었습니다",
        'form_copied': "도형이 복사되었습니다",
        'form_pasted': "도형이 붙여넣기되었습니다",
        'form_saved': "{0}개의 도형이 PDF에 삽입되었습니다.\n\nPDF가 다시 로드되었습니다...",
        'form_saved_voice': "{0}개의 도형이 저장되었습니다",
        'form_reset': "도형이 기본 크기로 재설정되었습니다",
        'form_transparent_on': "활성화",
        'form_transparent_off': "비활성화",
        'form_transparent_toggled': "투명 배경 {0}",
        'form_line_cancel': "선 그리기가 취소되었습니다",
        'form_second_click': "지금 {0}의 끝점을 클릭하십시오",
        'mode_replace_form': "도형 삽입",
        'mode_conflict_voice_form': "모드 {0}이(가) 활성화되어 있습니다. 종료하고 도형을 삽입하시겠습니까?",
        'form_settings_updated': "도형 설정이 업데이트되었습니다",
        'form_unknown': "도형",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. 시작점 클릭",
        'form_line_guide_2': "2. 끝점 클릭",
        'form_line_guide_3': "선이 두 점 사이에 그려집니다.",
        'form_line_status_1': "첫 번째 클릭을 기다리는 중...",
        'form_line_status_2': "첫 번째 점 설정됨: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "지금 끝점을 클릭하십시오...",
        'form_line_status_4': "두 점이 모두 설정되었습니다.\n저장하려면 '완료'를 클릭하십시오.",
        'form_line_reset': "초기화",
        'form_line_finish': "완료",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "복사 (Cmd+C)",
        'paste': "붙여넣기 (Cmd+V)",
        'copied': "복사됨: {0}",
        'no_element_to_copy': "복사할 요소가 선택되지 않았습니다",
        'no_copied_data': "복사된 데이터가 없습니다",
        'no_valid_position': "붙여넣기에 유효한 위치가 없습니다",
        'copy_text': "텍스트가 복사되었습니다",
        'copy_image': "이미지가 복사되었습니다",
        'copy_form': "도형이 복사되었습니다",
        'copy_signature': "서명이 복사되었습니다",
        'element_text': "텍스트",
        'element_image': "이미지",
        'element_form': "도형",
        'element_signature': "서명",
        'element_unknown': "요소",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "모드 충돌",
        'mode_conflict_message': "모드 '{0}'이(가) 이미 활성화되어 있습니다.\n\n종료하고 {1}하시겠습니까?",
        'mode_replace': "모드 종료 및 {0}",
        'mode_cancel': "취소",
        'mode_replace_text': "텍스트 삽입",
        'mode_replace_cross': "십자 삽입",
        'mode_replace_signature': "서명 삽입",
        'mode_replace_image': "이미지 삽입",
        'mode_replace_form': "도형 삽입",
        'mode_conflict_voice': "모드 {0}이(가) 활성화되어 있습니다. 종료하고 텍스트를 삽입하시겠습니까?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "텍스트 입력",
        'active_mode_signature': "서명",
        'active_mode_image': "이미지",
        'active_mode_form': "도형",
        'active_mode_and': " 및 ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "삽입",
        'insert_another_text': "텍스트 삽입",
        'insert_another_cross': "십자 삽입",
        'insert_another_signature_1': "서명 1",
        'insert_another_signature_2': "서명 2",
        'insert_another_image': "이미지 삽입",
        'insert_another_form_rect': "직사각형",
        'insert_another_form_ellipse': "타원",
        'insert_another_form_line': "선 (2회 클릭)",
        'insert_another_form_arrow': "화살표 (2회 클릭)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} 저장",
        'save_dialog_message': "{0}이(가) 페이지 {1}에 저장됩니다.\n\n어떻게 진행하시겠습니까?",
        'save_all': "모든 {0} 저장",
        'save_single': "{0} 저장",
        'save_customize': "{0} 조정",
        'save_discard': "이 {0} 삭제",
        'save_continue': "편집 계속",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " 페이지 {0}(으)로 이동",
        'context_rotate': " 페이지 {0} 회전",
        'context_delete': " 페이지 {0} 삭제",
        'context_export': " 페이지 {0} 내보내기",
        'context_mark_as': " 페이지 표시...",
        'context_mark_empty': " 빈 페이지",
        'context_unmark_empty': " 빈 페이지 해제",
        'context_mark_export': " 내보내기용으로 표시",
        'context_unmark_export': " 내보내기 표시 해제",
        'context_batch_actions': " 일괄 작업",
        'context_batch_delete_empty': " 모든 빈 페이지({0}개) 삭제",
        'context_batch_export_single': " 모든 페이지({0}개) 내보내기 (하나의 파일)",
        'context_batch_export_split': " 모든 페이지({0}개) 내보내기 (개별 파일)",
        'context_drag_start': " 드래그 앤 드롭 시작",
        'context_drag_stop': " 드래그 앤 드롭 중지",
        'context_insert': " 삽입",
        'context_insert_pages': " 페이지 삽입",
        'context_zoom': "확대/축소",
        'discard_mixed': "{0}개의 {1}와(과) {2}개의 {3} 삭제",
        'save_mixed': "{0}개의 {1}와(과) {2}개의 {3} 저장",
        'discard_texts': "{0}개의 텍스트 삭제",
        'discard_text_single': "1개 텍스트 삭제",
        'save_texts': "{0}개의 텍스트 저장",
        'save_text_single': "1개 텍스트 저장",
        'discard_crosses': "{0}개의 십자 삭제",
        'discard_cross_single': "1개 십자 삭제",
        'save_crosses': "{0}개의 십자 저장",
        'save_cross_single': "1개 십자 저장",
        'discard_signatures': "{0}개의 서명 삭제",
        'save_signature_single': "1개 서명 저장",
        'save_signatures': "{0}개의 서명 저장",
        'discard_images': "{0}개의 이미지 삭제",
        'save_image_single': "1개 이미지 저장",
        'save_images': "{0}개의 이미지 저장",
        'discard_forms': "{0}개의 도형 삭제",
        'save_form_single': "1개 도형 저장",
        'save_forms': "{0}개의 도형 저장",
        'cross_discard': "이 십자 삭제",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 내보내기/가져오기 정보",
        'export_what': "📋 내보내는 항목:",
        'export_general': "일반 설정",
        'export_general_items': "• 음성 출력 (켜기/끄기, 속도)\n• 다크/라이트 모드\n• 백업 설정\n• OCR 설정",
        'export_image_form': "이미지 및 도형 설정",
        'export_image_form_items': "• 이미지 설정 (가로세로 비율, 기본 크기)\n• 도형 설정 (선 두께, 색상)\n• 서명 설정 (경로, 크기, 타임스탬프)",
        'export_passwords': "비밀번호 데이터베이스",
        'export_passwords_items': "• 저장된 모든 PDF 비밀번호\n• 선택적으로 암호화 또는 복호화",
        'export_master': "마스터 비밀번호 설정",
        'export_master_items': "• 마스터 비밀번호 해시\n• 서명/텍스트 블록 설정",
        'export_signatures': "서명 및 텍스트 블록",
        'export_signatures_items': "• 모든 이미지 파일 (서명)\n• 서식이 포함된 모든 텍스트 블록\n• 개인/공개 표시",
        'export_import_warning': "⚠️ 중요 참고 사항",
        'export_import_note': "• 가져올 때 현재 모든 설정이 덮어쓰여집니다\n• 애플리케이션을 다시 시작해야 합니다\n• 기존 서명/텍스트 블록이 교체됩니다",
        'export_master_note': "• 마스터 비밀번호가 설정된 경우 선택할 수 있습니다:\n  - 복호화 (비밀번호가 일반 텍스트로)\n  - 암호화 (마스터 비밀번호로만 읽을 수 있음)",
        'export_security': "• 내보낸 ZIP 파일에는 기밀 데이터가 포함되어 있습니다\n• 안전한 장소에 보관하십시오 (예: 암호화된 USB 메모리)\n• 파일을 분실하면 비밀번호를 영원히 잃게 됩니다",
        'export_format': "📁 내보내기 형식",
        'export_format_desc': "설정은 하나의 ZIP 파일에 저장됩니다:",
        'export_filename': "PDFDarkView_설정_YYYYMMDD_HHMMSS.zip",
        'export_success': "설정이 성공적으로 내보내졌습니다",
        'export_failed': "내보내기에 실패했습니다",
        'export_import_question': "지금 애플리케이션을 다시 시작하시겠습니까?",
        'export_password_question': "마스터 비밀번호가 설정되어 있습니다.\n\n비밀번호를 복호화하여 내보내시겠습니까?\n(그렇지 않으면 암호화된 상태로 내보내집니다)",
        'export_decrypt': "복호화하여 내보내기",
        'export_encrypt': "암호화하여 내보내기",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " 정보",
        'info_title': "PDF Dark View 정보",
        'info_version': "버전",
        'info_author': "개발자: Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "정보",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong>는 시각 장애인을 위해 특별히 개발된 접근성 PDF 뷰어입니다.</p>

            <p><strong>주요 기능:</strong></p>
            <ul>
                <li>고대비, 사용자 정의 가능한 인터페이스</li>
                <li>완전한 키보드 제어</li>
                <li>통합 음성 출력</li>
                <li>스캔 문서용 OCR</li>
                <li>포괄적인 편집 도구</li>
            </ul>

            <p>50개 이상의 언어를 지원 – 누구나 PDF에 접근할 수 있습니다.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "기능",
        'info_features_intro': "PDF Dark View는 다음과 같은 기능을 제공합니다:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>표시 및 탐색</strong> – 다크/라이트 모드, 페이지 넘기기, 줌, 페이지 이동</li>
            <li><strong>OCR (텍스트 인식)</strong> – 스캔 문서를 검색 및 복사 가능하게 만들기</li>
            <li><strong>편집</strong> – 텍스트, 십자 표시, 서명, 이미지 및 도형 삽입</li>
            <li><strong>페이지 관리</strong> – 삭제, 추출, 삽입, 드래그 앤 드롭으로 이동</li>
            <li><strong>내보내기</strong> – Word, Pages 또는 텍스트로</li>
            <li><strong>보안</strong> – 비밀번호 보호 및 관리</li>
            <li><strong>접근성</strong> – 음성 출력, 키보드 제어, 고대비</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "사용법",
        'info_accessibility': "♿ 접근성 – 완전한 키보드 제어",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 일반</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF 열기</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> 검색</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> 다크/라이트 모드 전환</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> 인쇄</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> 종료</div>

        <div class="shortcut-cat">📖 탐색</div>
        <div class="shortcut-row"><kbd>화살표 키</kbd> 페이지 단위로 넘기기</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> 페이지로 이동</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> 첫 페이지</div>
        <div class="shortcut-row"><kbd>Ende</kbd> 마지막 페이지</div>

        <div class="shortcut-cat">✏️ 편집</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> 텍스트 삽입</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> 페이지 삭제</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> 페이지 추출</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> 페이지 삽입</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> 페이지 이동</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> 페이지 회전</div>

        <div class="shortcut-cat">🖼️ 요소 이동</div>
        <div class="shortcut-row"><kbd>화살표 키</kbd> 텍스트/이미지/서명 이동</div>
        <div class="shortcut-row"><kbd>Ctrl+화살표 키</kbd> 더 큰 간격으로 이동</div>
        <div class="shortcut-row"><kbd>Enter</kbd> 저장</div>
        <div class="shortcut-row"><kbd>ESC</kbd> 취소</div>

        <div class="shortcut-cat">🗣️ 음성 출력</div>
        <div class="shortcut-row"><kbd>F2</kbd> 음성 출력 켜기/끄기</div>
        """,
        'info_contextmenu': "📌 중요: 모든 기능은 상황에 맞는 메뉴(마우스 오른쪽 버튼)를 통해서도 사용할 수 있습니다!",
        'info_accessibility_hint': "💡 팁: 음성 출력(F2)은 방향을 쉽게 잡을 수 있도록 도와주며 메뉴 및 대화 상자에 대한 피드백을 제공합니다.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "라이선스 & 임프린트",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 임프린트</strong><br>
        § 5 TMG에 따른 정보:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, 독일<br>
        이메일: binhdiez64@gmail.com<br>
        콘텐츠 책임자: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ 면책 조항</strong><br>
        본 소프트웨어는 최대한 주의를 기울여 개발되었습니다. 정확성, 완전성 및 기능성에 대한 보증은 제공되지 않습니다. 사용은 사용자 본인의 책임입니다.<br><br>

        <strong>📄 MIT 라이선스 (개인 사용)</strong><br>
        저작권 (c) 2026 Toralf Schulz (BinhDiez)<br>
        허용: 무료 사용, 개인적 변경, 개인적 복사.<br>
        불허: 판매, 상업적 사용, 저작권 표시 제거.<br><br>

        <strong>🔧 타사 구성 요소</strong><br>
        본 소프트웨어에는 GPL, AGPL, Apache 2.0, BSD 및 MIT 라이선스에 따른 구성 요소가 포함되어 있습니다.<br>
        재배포 시 해당 라이선스 조건을 준수해야 합니다.<br><br>

        <strong>🌐 오픈 소스</strong><br>
        소스 코드는 제공되며, 해당 라이선스 조건에 따라 열람, 수정, 재배포할 수 있습니다.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "감사의 말",
        'info_credits': "오픈 소스 커뮤니티에 감사드립니다",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF 처리</li>
            <li><strong>PyQt5</strong> – 그래픽 인터페이스</li>
            <li><strong>Tesseract OCR</strong> – 텍스트 인식</li>
            <li><strong>OCRmyPDF</strong> – OCR 통합</li>
            <li><strong>python-docx</strong> – Word 내보내기</li>
            <li><strong>qtawesome</strong> – 아이콘</li>
            <li><strong>DeepSeek</strong> – 번역 지원 (50개 이상의 언어)</li>
            <li><strong>모든 사용자</strong> – 소중한 피드백에 감사드립니다</li>
            <li><strong>오픈 소스 커뮤니티</strong> – 훌륭한 라이브러리에 감사드립니다</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "언어",
        'info_languages_header': "🌍 언어 지원",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View는 현재 <strong>62개 언어</strong>를 지원합니다 – 소프트웨어를 전 세계에서 접근 가능하게 사용할 수 있도록 합니다.</p>

            <p><strong>📖 전체 언어 목록 (2026년 3월 기준):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 아프리칸스어</li>
                    <li>🇦🇱 알바니아어 (Shqip)</li>
                    <li>🇩🇿 아랍어 (العربية)</li>
                    <li>🇮🇩 발리어 (Basa Bali)</li>
                    <li>🇧🇩 벵골어 (বাংলা)</li>
                    <li>🇲🇲 버마어 (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 보스니아어 (Bosanski)</li>
                    <li>🇧🇬 불가리아어 (Български)</li>
                    <li>🇨🇳 중국어 (中文)</li>
                    <li>🇩🇰 덴마크어 (Dansk)</li>
                    <li>🇩🇪 독일어 (Deutsch)</li>
                    <li>🇬🇧 영어 (English)</li>
                    <li>🇪🇪 에스토니아어 (Eesti)</li>
                    <li>🇫🇮 핀란드어 (Suomi)</li>
                    <li>🇫🇷 프랑스어 (Français)</li>
                    <li>🇬🇷 그리스어 (Ελληνικά)</li>
                    <li>🇮🇱 히브리어 (עברית)</li>
                    <li>🇮🇳 힌디어 (हिन्दी)</li>
                    <li>🇭🇷 크로아티아어 (Hrvatski)</li>
                    <li>🇭🇺 헝가리어 (Magyar)</li>
                    <li>🇮🇩 인도네시아어 (Bahasa Indonesia)</li>
                    <li>🇮🇪 아일랜드어 (Gaeilge)</li>
                    <li>🇮🇸 아이슬란드어 (Íslenska)</li>
                    <li>🇮🇹 이탈리아어 (Italiano)</li>
                    <li>🇯🇵 일본어 (日本語)</li>
                    <li>🇰🇭 크메르어 (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 한국어 (한국어)</li>
                    <li>🇱🇦 라오어 (ພາສາລາວ)</li>
                    <li>🇱🇻 라트비아어 (Latviešu)</li>
                    <li>🇱🇹 리투아니아어 (Lietuvių)</li>
                    <li>🇱🇺 룩셈부르크어 (Lëtzebuergesch)</li>
                    <li>🇲🇾 말레이어 (Bahasa Melayu)</li>
                    <li>🇮🇳 마라티어 (मराठी)</li>
                    <li>🇲🇳 몽골어 (Монгол)</li>
                    <li>🇳🇵 네팔어 (नेपाली)</li>
                    <li>🇳🇱 네덜란드어 (Nederlands)</li>
                    <li>🇳🇴 노르웨이어 (Norsk)</li>
                    <li>🇦🇫 파슈토어 (پښتو)</li>
                    <li>🇮🇷 페르시아어 (فارسی)</li>
                    <li>🇵🇱 폴란드어 (Polski)</li>
                    <li>🇵🇹 포르투갈어 (Português)</li>
                    <li>🇮🇳 펀자브어 (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 루마니아어 (Română)</li>
                    <li>🇷🇺 러시아어 (Русский)</li>
                    <li>🇸🇪 스웨덴어 (Svenska)</li>
                    <li>🇷🇸 세르비아어 (Српски)</li>
                    <li>🇸🇰 슬로바키아어 (Slovenčina)</li>
                    <li>🇸🇮 슬로베니아어 (Slovenščina)</li>
                    <li>🇪🇸 스페인어 (Español)</li>
                    <li>🇹🇿 스와힐리어 (Kiswahili)</li>
                    <li>🇵🇭 타갈로그어 (Filipino)</li>
                    <li>🇮🇳 타밀어 (தமிழ்)</li>
                    <li>🇮🇳 텔루구어 (తెలుగు)</li>
                    <li>🇹🇭 태국어 (ไทย)</li>
                    <li>🇨🇿 체코어 (Čeština)</li>
                    <li>🇹🇷 터키어 (Türkçe)</li>
                    <li>🇺🇦 우크라이나어 (Українська)</li>
                    <li>🇵🇰 우르두어 (اردو)</li>
                    <li>🇻🇳 베트남어 (Tiếng Việt)</li>
                    <li>🇸🇳 월로프어 (Wolof)</li>
                    <li>🇺🇸 이디시어 (ייִדיש)</li>
                    <li>🇿🇦 줄루어 (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 자체 언어 추가:</strong><br>
                아직 포함되지 않은 언어를 원하십니까? 자체 사전 파일(<code>sprache_xx.py</code>)을 애플리케이션 옆에 놓기만 하면 됩니다 – 소프트웨어가 자동으로 인식합니다. 특정 번역에 관심이 있으시면 언제든지 연락해 주십시오.
            </div>

            <p><strong>🙏 특별한 감사:</strong> 모든 사전을 62개 언어로 번역하는 데 지원해 주신 DeepSeek께 감사드립니다.</p>

            <p>📧 번역 관련 문의: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "오류",
        'error_occurred': "오류가 발생했습니다",
        'error_pdf_load': "PDF 로드 중 오류 발생",
        'error_pdf_save': "PDF 저장 중 오류 발생",
        'error_ocr': "텍스트 인식 중 오류 발생",
        'error_no_pdf': "로드된 PDF가 없습니다",
        'error_page_not_found': "페이지를 찾을 수 없습니다",
        'error_invalid_range': "잘못된 페이지 범위입니다",
        'error_file_not_found': "파일을 찾을 수 없습니다",
        'error_permission': "권한이 없습니다",
        'error_unknown': "알 수 없는 오류",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "성공",
        'success_operation': "작업이 성공적으로 완료되었습니다",
        'success_saved': "성공적으로 저장되었습니다",
        'success_exported': "성공적으로 내보내졌습니다",
        'success_imported': "성공적으로 가져왔습니다",
        'success_deleted': "성공적으로 삭제되었습니다",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "확인",
        'confirm_yes': "예",
        'confirm_no': "아니요",
        'confirm_ok': "확인",
        'confirm_cancel': "취소",
        'confirm_delete': "삭제",
        'confirm_overwrite': "덮어쓰기",
        'confirm_continue': "계속",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF 로드 중...",
        'progress_saving': "PDF 저장 중...",
        'progress_exporting': "PDF 내보내기 중...",
        'progress_processing': "처리 중...",
        'progress_wait': "잠시 기다려 주십시오...",
        'progress_preparing': "준비 중...",
        'progress_finalizing': "마무리 중...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "흰색",
        'color_black': "검정",
        'color_red': "빨강",
        'color_green': "초록",
        'color_blue': "파랑",
        'color_yellow': "노랑",
        'color_magenta': "자홍",
        'color_cyan': "청록",
        'color_orange': "주황",
        'color_gray': "회색",
        'color_custom': "색상 선택",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&파일",
        'menu_edit': "&편집",
        'menu_view': "&보기",
        'menu_tools': "&도구",
        'menu_settings': "&설정",
        'menu_help': "&도움말",
        'menu_language': "🌐 언어",
        'menu_guides': "&가이드",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&열기",
        'file_save_as': "&다른 이름으로 저장...",
        'file_protect': "&문서 보호...",
        'file_export': "&내보내기",
        'file_export_pages': "Pages로 내보내기",
        'file_export_word': "DOCX로 내보내기",
        'file_export_text': "TXT로 내보내기",
        'file_print_now': "&지금 인쇄",
        'file_print': "&인쇄",
        'file_close': "&닫기",
        'file_quit': "&종료",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&검색",
        'edit_ocr': " OCR 실행",
        'edit_rotate': "&페이지 회전",
        'edit_rotate_all': "모든 페이지 회전",
        'edit_delete_pages': "&페이지 삭제",
        'edit_extract_pages': "&페이지 추출",
        'edit_insert_pages': "&페이지 삽입",
        'edit_move_pages': "&페이지 이동",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " 텍스트 및 십자 삽입",
        'text_insert': " 텍스트 삽입",
        'cross_insert': " 십자 삽입",
        'text_customize': " 텍스트 조정",
        'cross_customize': " 이 십자 조정",
        'cross_customize_all': " 모든 십자 조정",
        'text_discard': " 이 텍스트/십자 삭제",
        'text_discard_all': " 모든 텍스트 및 십자 삭제",
        'text_save_all': " 모든 텍스트 및 십자 저장",
        'text_guide': " 텍스트 입력 / 텍스트 블록 – 가이드",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " 서명 삽입",
        'signature_settings_menu': " 설정...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " 이미지 삽입",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " 도형 삽입",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&텍스트 창 표시",
        'view_zoom': "&확대/축소",
        'view_zoom_page': "&페이지 너비 (기본)",
        'view_zoom_two': "&두 페이지",
        'view_zoom_overview': "&개요 (여러 페이지)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&접근성",
        'settings_voice': "음성 출력",
        'settings_voice_tooltip': "화면 판독기의 음성 출력을 추가 정보로 보완합니다",
        'settings_signature': "&서명 설정",
        'settings_password': "&비밀번호 관리",
        'settings_backup': "변경 전에 백업 생성",
        'settings_export_import': "&설정 내보내기 / 가져오기",
        'settings_export': "&모든 설정 내보내기...",
        'settings_import': "&모든 설정 가져오기...",
        'settings_export_info': "&내보내는 항목",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "켜짐",
        'voice_off': "꺼짐",
        'voice_toggle': "음성 출력 {0}",
        'voice_speed': "속도 {0}%",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "도구를 찾을 수 없습니다:\n{0}\n\nBASE_DIR: {1}\nPDF 도구가 디렉토리 {1}에 설치되어 있는지 확인하십시오.",
        'tool_started': "{0} 시작됨",
        'tool_start_failed': "시작할 수 없습니다",
        'process_error_failed_to_start': "프로세스를 시작할 수 없습니다. 파일이 존재합니까?",
        'process_error_crashed': "프로세스가 시작 중에 충돌했습니다.",
        'process_error_timeout': "프로세스 시간이 초과되었습니다.",
        'process_error_write': "프로세스에 쓰는 중 오류 발생",
        'process_error_read': "프로세스에서 읽는 중 오류 발생",
        'process_error_unknown': "알 수 없는 프로세스 오류",
        'process_command': "명령",
        'process_normal_exit': "정상 종료됨",
        'process_crashed': "충돌함",
        'process_nonzero_exit': "{0}이(가) 오류 코드 {1}(으)로 종료되었습니다",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "취소 중...",
        'move_cancelling': "이동 취소 중",
        'opening_pdf': "PDF 여는 중...",
        'loading_document': "문서 로드 중...",
        'pdf_opened': "PDF가 열렸습니다",
        'pages_found_moving': "{0}페이지를 찾았습니다, {1}페이지 이동",
        'creating_backup': "백업 생성 중...",
        'backup_description': "원본 파일 백업 중...",
        'backup_saved_as': "백업이 저장되었습니다: {0}",
        'error_format': "오류: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "검색이 초기화되었습니다",
        'page_header_simple': "=== 페이지 {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "비밀번호 관리 – 가이드",
        'password_guide_voice': "비밀번호 관리 가이드입니다. 참고 사항을 읽어 주십시오.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 비밀번호 관리 – 상세 가이드</strong></p>

        <p><strong>1. PDF 비밀번호 보호</strong></p>
        <ul>
        <li>비밀번호로 보호된 PDF를 열면 비밀번호를 입력하는 대화상자가 표시됩니다.</li>
        <li>비밀번호를 암호화하여 저장하면 매번 입력할 필요가 없습니다 ("비밀번호 저장" 확인란).</li>
        <li>"비밀번호 제거" 버튼으로 복호화된 PDF 복사본을 만들고 데이터베이스에서 비밀번호를 삭제할 수 있습니다.</li>
        </ul>

        <p><strong>2. 마스터 비밀번호</strong></p>
        <ul>
        <li>마스터 비밀번호는 저장된 모든 PDF 비밀번호에 대한 액세스를 보호합니다.</li>
        <li><strong>설정:</strong> "설정 → 비밀번호 관리 → 마스터 비밀번호 설정"으로 이동하여 "마스터 비밀번호 설정"을 클릭합니다. 강력한 비밀번호를 선택하십시오 (최소 8자).</li>
        <li><strong>변경:</strong> 인증에 성공하면 마스터 비밀번호를 변경할 수 있습니다.</li>
        <li><strong>제거:</strong> 마스터 비밀번호를 제거하면 저장된 모든 비밀번호가 영구적으로 삭제됩니다. 미리 백업을 내보낼 수 있습니다.</li>
        <li>세션당 한 번, 보호된 기능(예: 비밀번호 표시)에 액세스하려면 마스터 비밀번호로 인증해야 합니다.</li>
        </ul>

        <p><strong>3. 비밀번호 관리 (목록)</strong></p>
        <ul>
        <li>"설정 → 비밀번호 관리"에서는 저장된 모든 PDF 파일과 암호화된 비밀번호의 테이블이 표시됩니다.</li>
        <li><strong>마스터 비밀번호 없음:</strong> 항목만 삭제할 수 있습니다 – 비밀번호는 숨겨진 상태로 유지됩니다.</li>
        <li><strong>마스터 비밀번호 있음 (인증됨):</strong> 비밀번호를 표시, 복사, 내보내기, 삭제할 수 있습니다.</li>
        <li><strong>내보내기:</strong> 형식(JSON, CSV, TXT)을 선택하고 목록을 저장합니다. 마스터 비밀번호가 설정된 경우 비밀번호를 복호화하여 내보낼지 암호화된 상태로 내보낼지 선택할 수 있습니다.</li>
        <li><strong>가져오기:</strong> 이전에 내보낸 ZIP 파일(모든 설정)은 "설정 → 설정 내보내기 / 가져오기"를 통해 다시 가져올 수 있습니다. 주의: 기존 데이터는 덮어쓰여집니다!</li>
        </ul>

        <p><strong>4. 비밀번호 생성기</strong></p>
        <ul>
        <li>비밀번호 대화상자(예: PDF 보호 시)에서 입력 필드 오른쪽에 있는 주사위 버튼 🎲을 클릭합니다.</li>
        <li>비밀번호 생성기가 열립니다. 길이, 문자 세트(대문자, 소문자, 숫자, 기호), 가독성을 위한 구분 기호를 설정할 수 있습니다.</li>
        <li>생성된 비밀번호는 직접 사용할 수 있고 필요에 따라 복사할 수 있습니다.</li>
        </ul>

        <p><strong>5. 중요한 보안 참고 사항</strong></p>
        <ul>
        <li>저장된 비밀번호는 AES-256으로 암호화되어 저장됩니다. 키는 마스터 비밀번호(설정된 경우) 또는 고정 값(마스터 비밀번호 없음)에서 파생됩니다.</li>
        <li>마스터 비밀번호가 없으면 비밀번호는 암호화되어 있지만 키가 프로그램에 내장되어 있습니다 – 파일에 액세스할 수 있는 공격자가 이를 복호화할 수 있습니다. 따라서 마스터 비밀번호 사용을 강력히 권장합니다.</li>
        <li>비밀번호 데이터베이스는 `Data/passwords.json` 파일에 있습니다. 정기적으로 백업을 만들고, 특히 마스터 비밀번호를 제거하기 전에 만드십시오.</li>
        <li>마스터 비밀번호를 분실하면 저장된 모든 비밀번호가 영구적으로 손실됩니다.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "반전 모드",
        'invert_mode_classic': "클래식 (모든 색상 반전)",
        'invert_mode_smart': "스마트 (밝기만 반전)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "그레이스케일 임계값",
        'gray_threshold_10': "10% (엄격)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (기본값)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (부드러움)",
        'threshold_changed': "임계값이 {0}%로 설정되었습니다",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "그레이스케일 임계값 – 설명",
        'threshold_guide_text': "그레이스케일 임계값은 스마트 다크 모드에서 '회색'으로 간주되어 반전되는 픽셀을 결정합니다.\n\n"
                                "• 낮은 값(10%)은 거의 완벽한 회색조만 반전합니다 – 유색 요소는 완전히 보존됩니다.\n"
                                "• 높은 값(50%)은 약간 유색인 픽셀도 반전합니다 – 이는 대비를 높이지만 색상을 왜곡할 수 있습니다.\n\n"
                                "최적의 값은 문서에 따라 다릅니다. 순수 텍스트 문서의 경우 30–40%가 이상적이며, 유색 그래픽의 경우 10–20%가 적합합니다.\n\n"
                                "'설정' 메뉴를 통해 언제든지 값을 조정할 수 있습니다 – PDF가 즉시 다시 로드됩니다.\n\n"
                                "참고:\n* 사진과 이미지는 라이트 모드에서만 올바르게 표시될 수 있습니다!\n* 반전 설정은 다크 모드가 활성화된 경우에만 표시됩니다.",
        'threshold_guide_voice': "그레이스케일 임계값은 스마트 다크 모드의 개입 강도를 결정합니다. 낮은 값은 색상을 보존하고, 높은 값은 대비를 높입니다.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF를 여는 중...",
        'progress_loading_document': "문서를 불러오는 중...",
        'progress_pdf_opened': "PDF가 열렸습니다",
        'progress_creating_backup': "백업을 생성하는 중...",
        'progress_backup_description': "원본 파일을 보호하는 중...",
        'progress_backup_created': "백업이 생성되었습니다",
        'progress_backup_saved_as': "{0}(으)로 저장되었습니다",
        'progress_analyzing_start': "분석을 시작하는 중...",
        'progress_searching_empty': "빈 페이지를 검색하는 중...",
        'progress_page_empty': "페이지 {0}은(는) 비어 있습니다",
        'progress_page_keep': "페이지 {0}을(를) 유지합니다",
        'progress_analysis_complete': "분석이 완료되었습니다",
        'progress_empty_found': "{0}개의 빈 페이지를 찾았습니다",
        'progress_current_page': "현재 페이지",
        'progress_mark_delete': "삭제 표시 중",
        'progress_range_selected': "페이지 범위 {0}-{1}",
        'progress_deleting_pages': "{0}개 페이지를 삭제하는 중",
        'progress_creating_new_pdf': "새 PDF를 생성하는 중...",
        'progress_transferring_pages': "페이지를 전송하는 중",
        'progress_keeping_page': "페이지 {0}이(가) 유지됩니다 ({1}/{2})",
        'progress_saving_pdf': "PDF를 저장하는 중...",
        'progress_optimizing': "파일 크기를 최적화하는 중...",
        'progress_finalizing': "마무리하는 중...",
        'progress_new_size': "새 크기: {0:.2f} MB",
        'progress_cancelling': "취소하는 중...",
        'progress_cancel_message': "{0}을(를) 취소하는 중",
        'progress_pages_found_moving': "{0}개 페이지를 찾았으며, {1}개를 이동합니다",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF를 분석하는 중...",
        'ocr_status_optimizing': "이미지 최적화 중...",
        'ocr_status_recognizing': "텍스트 인식 중...",
        'ocr_status_embedding': "텍스트를 삽입하는 중...",
        'ocr_status_finalizing': "PDF를 마무리하는 중...",

        # PDF-Laden
        'progress_preparing': "준비 중...",
        'progress_loading': "PDF를 불러오는 중...",

        # Seitenoperationen
        'progress_deleting_title': "페이지를 삭제하는 중...",
        'progress_moving_title': "페이지를 이동하는 중...",
        'pages_found': "찾은 페이지",
        'progress_creating_new_order': "새 순서를 생성하는 중...",
        'progress_sorting_pages': "페이지를 정렬하는 중...",
        'progress_moving_to_begin': "{0}개 페이지를 처음으로 이동",
        'progress_transferring_count': "{0}개 페이지 전송",
        'progress_transferring_before_target': "대상 앞에 페이지 전송",
        'progress_moving_pages': "{0}개 페이지 이동",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_백업_",
        'filename_protected_suffix': "_보호됨_",
        'filename_copy_suffix': "_복사본",
        'filename_page_single': "_페이지_",
        'filename_page_range': "_페이지_",
        'filename_export_page': "_페이지_{0:03}",
        'filename_export_range': "_페이지_{0}-{1}",
        'filename_export_multiple': "_페이지_{0}",
        'filename_with_text': "_텍스트_포함",
        'filename_with_signature': "_서명_포함",
        'filename_with_image': "_이미지_포함",
        'filename_with_forms': "_도형_포함",
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
        'view_toggle_navbar': "버튼 막대 표시",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "모든 페이지를 삭제할 수 없습니다",
		'pages_cannot_delete_last_page': '마지막 페이지는 삭제할 수 없습니다!',
		'pages_cannot_delete_all_pages': '문서에 최소한 한 페이지는 남아 있어야 합니다!',
		'delete_pages_confirm': '{0} 페이지를 삭제하시겠습니까?',
		'delete_pages_confirm_voice': '{0} 페이지를 삭제하시겠습니까?',
		'pages_deleted': '{0} 페이지가 성공적으로 삭제되었습니다.',
		'warning': '경고',
		'error': '오류',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "선택된 양식 없음",
        'form_customized': "양식이 사용자 정의되었습니다",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "선택",
        'btn_use': "사용",
        'master_password_for_spasswords': "비밀번호를 저장하고 사용하려면 먼저 마스터 비밀번호를 설정해야 합니다.\n\n지금 마스터 비밀번호를 설정하시겠습니까?",
        'open_saved_dialog_title': "저장된 파일 열기",
        'open_saved_question': "저장된 파일을 지금 열겠습니까?",
        'password': "비밀번호",
        'password_manager_master_required': "비밀번호 관리자는 마스터 비밀번호가 설정된 경우에만 사용할 수 있습니다.\n\n지금 마스터 비밀번호를 설정하시겠습니까?",
        'password_master_required_for_select': "저장된 비밀번호를 보고 선택하려면 먼저 마스터 비밀번호로 인증해야 합니다.\n\n지금 인증하시겠습니까?",
        'password_not_available': "선택한 비밀번호를 사용할 수 없거나 복호화할 수 없습니다.",
        'password_options_title': "비밀번호 옵션",
        'password_save_choice_change': "새 비밀번호 설정",
        'password_save_choice_keep': "기존 비밀번호 사용",
        'password_save_choice_none': "암호화 없이 저장",
        'password_save_hint': "비밀번호를 안전하게 저장하려면 먼저 마스터 비밀번호를 설정하세요.",
        'password_save_master_required': "비밀번호 저장 (마스터 비밀번호로만 가능)",
        'password_save_question': "현재 PDF는 비밀번호로 보호되어 있습니다. 기존 비밀번호를 사용하시겠습니까, 새로 설정하시겠습니까, 아니면 암호화 없이 저장하시겠습니까?",
        'password_select': "비밀번호 선택",
        'password_select_none': "선택된 비밀번호가 없습니다.\n\n목록에서 비밀번호를 선택하세요.",
        'password_select_one': "정확히 하나의 비밀번호를 선택하세요.\n\n여러 비밀번호를 표시했습니다.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_백업",
        'filename_insert_suffix': "_삽입됨",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_페이지_삭제됨",
        'filename_pages_moved': "_페이지_이동됨",
        'filename_rotated_all_suffix': "_모든_페이지_회전됨",
        'filename_rotated_suffix': "_페이지_회전됨",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "PDF 변경 시 파일 이름 구성",
        'filename_keep_suffixes': "이전 확장자 유지 (예: _텍스트_포함)",
        'filename_keep_suffixes_false': "바꾸기",
        'filename_keep_suffixes_true': "유지",
        'filename_preview_label': "파일 이름 미리보기:",
        'filename_preview_overwrite_hint': "미리보기를 사용할 수 없음 – 원본이 덮어쓰여집니다.",
        'filename_separator': "단어 구분 기호",
        'filename_separator_none': "구분 기호 없음",
        'filename_separator_space': "공백 ( )",
        'filename_separator_underscore': "밑줄 (_)",
        'filename_settings_saved': "파일 이름 설정 저장됨",
        'filename_settings_title': "파일 이름 형식 및 백업",
        'filename_timestamp_position': "타임스탬프 위치",
        'filename_timestamp_position_after': "기본 이름 뒤",
        'filename_timestamp_position_before': "맨 앞",
        'filename_timestamp_position_end': "끝에",
        'filename_use_timestamp': "타임스탬프 사용",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>변경 시 동작:</b><ul><li>페이지 삭제 및 삽입</li><li>텍스트, 서명, 이미지 및 도형 삽입</li><li>OCR</li></ul></html>",
        'backup_section': "페이지 작업(삭제, 이동)에 대한 백업",
        'behavior_info': "참고: '원본 덮어쓰기' 시 타임스탬프와 접미사는 무시됩니다 – 파일은 이름을 유지합니다.",
        'behavior_new_file': "항상 새 파일 만들기 (타임스탬프 및 접미사 포함)",
        'behavior_overwrite': "원본 덮어쓰기 (새 파일 없음)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "모든 페이지가 회전되었습니다.\n\n원본은 변경되지 않았습니다.\n새 파일: {0}",
        'all_pages_rotated_voice': "모든 페이지 회전됨, 새 파일 생성됨.",
        'empty_pages_deleted_new_file': "{0}개의 빈 페이지가 삭제되었습니다.\n\n원본은 변경되지 않았습니다.\n새 파일: {1}",
        'empty_pages_deleted_voice': "{0}개의 빈 페이지 삭제됨, 새 파일 생성됨.",
        'ocr_keep_original': "원본 유지 (나중에 수동으로 열기)",
        'ocr_new_file_question': "새로운 검색 가능한 PDF가 저장되었습니다:\n{0}\n\n지금 열겠습니까?",
        'ocr_open_new': "새 OCR 파일 열기",
        'ocr_original_kept': "원본 파일이 열려 있습니다. OCR 파일이 저장되었습니다.",
        'page_deleted_new_file': "페이지 {0}이(가) 삭제되었습니다.\n\n원본은 변경되지 않았습니다.\n새 파일: {1}",
        'page_deleted_voice': "페이지 {0} 삭제됨, 새 파일 생성됨.",
        'page_rotated_new_file': "페이지 {0}이(가) 회전되었습니다.\n\n원본은 변경되지 않았습니다.\n새 파일: {1}",
        'page_rotated_voice': "페이지 {0} 회전됨, 새 파일 생성됨.",
        'pages_deleted_new_file': "{0}개의 페이지가 삭제되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일: {1}",
        'pages_deleted_new_file_voice': "{0}개의 페이지 삭제됨, 새 파일 생성됨.",
        'pages_inserted_new_file': "{0}개의 페이지가 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일: {1}",
        'pages_inserted_new_file_ask': "{0}개의 페이지가 삽입되었습니다.\n\n원본은 변경되지 않았습니다.\n새 파일: {1}\n\n지금 열겠습니까?",
        'pages_inserted_voice_new': "{0}개의 페이지 삽입됨, 새 파일 생성됨.",
        'pages_moved_new_file': "{0}개의 페이지가 이동되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일: {1}",
        'pages_moved_new_file_voice': "{0}개의 페이지 이동됨, 새 파일 생성됨.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "다시 표시하지 않음",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 백업 설정</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ 백업 켜짐</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">원본을 덮어쓰는 모든 변경</strong>(텍스트, 서명, 이미지, 도형, OCR, 회전, 삽입, 페이지 삭제/이동)에 대해 변경을 적용하기 전에 <strong>타임스탬프가 있는 백업이 자동으로 생성</strong>됩니다.</p>
                <p style="margin: 5px 0 5px 20px;">• 백업은 원본 파일 옆에 위치합니다 (예: <code>문서_백업_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>„원본 덮어쓰기“</strong> 옵션을 추가로 활성화한 경우에도 백업이 생성됩니다.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 백업 꺼짐</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>백업이 생성되지 않습니다</strong> – 덮어쓰기 시에도 페이지 작업 시에도.</p>
                <p style="margin: 5px 0 5px 20px;">• 덮어쓰기 시 원본 파일을 복구할 수 없게 손실될 수 있습니다.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">숙련된 사용자에게만 권장됩니다!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>팁:</strong> 백업 설정은 „원본 덮어쓰기“ 옵션과 독립적입니다. 둘 다 결합할 수 있습니다.<br>
                이 메시지를 영구적으로 숨길 수 있습니다.
            </div>
        </div>
        """,
        'backup_info_title': "백업 동작",
        'backup_info_voice': "페이지 작업 시 백업 동작에 대한 알림입니다. 백업 켜짐은 원본을 덮어쓰고, 백업 꺼짐은 새 파일을 만듭니다.",
        'show_backup_info': "백업 설정 정보",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "다시 표시하지 않음",
        'overwrite_enable_backup': "백업 활성화 (권장)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ 원본 덮어쓰기</p>
            <p>이 옵션을 활성화하면 변경 사항(텍스트, 서명, 이미지, 도형, OCR, 회전, 삽입)이 <strong>원본에 직접 저장</strong>됩니다 – <strong>새 파일이 생성되지 않습니다</strong>.</p>
            <p>• 파일 이름은 변경되지 않습니다.<br>
            • 타임스탬프와 접미사는 무시됩니다.<br>
            • <strong>백업 없이는 원본을 복구할 수 없게 손실될 수 있습니다.</strong></p>
            <p style="color: #FFD700;">권장 사항: 자동 백업을 받으려면 백업 옵션도 활성화하세요.</p>
        </div>
        """,
        'overwrite_info_title': "원본 덮어쓰기",
        'overwrite_info_voice': "경고: 원본 덮어쓰기 – 새 파일 없음. 백업 권장.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0}개의 페이지가 삽입되었습니다.\n\n원본 파일이 덮어쓰여졌습니다.\n백업이 생성되었습니다.",
        'pages_inserted_overwrite_no_backup': "{0}개의 페이지가 삽입되었습니다.\n\n원본 파일이 덮어쓰여졌습니다.\n백업이 생성되지 않았습니다.",
        'texts_saved_overwrite_with_backup': "변경 사항이 원본에 저장되었습니다.\n\n백업이 생성되었습니다.",
        'texts_saved_overwrite_no_backup': "변경 사항이 원본에 저장되었습니다.\n\n백업이 생성되지 않았습니다.",
        'texts_crosses_saved_new_file': "{0} {1} 및 {2} {3}이(가) 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일이 생성되었습니다.\n\n새 PDF를 로드하는 중...",
        'texts_saved_new_file': "{0} {1}이(가) 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일이 생성되었습니다.\n\n새 PDF를 로드하는 중...",
        'crosses_saved_new_file': "{0} {1}이(가) 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일이 생성되었습니다.\n\n새 PDF를 로드하는 중...",
        'elements_saved_new_file': "{0}개 요소가 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일이 생성되었습니다.\n\n새 PDF를 로드하는 중...",
        'signatures_saved_overwrite_with_backup': "서명이 원본에 저장되었습니다.\n\n백업이 생성되었습니다.",
        'signatures_saved_overwrite_no_backup': "서명이 원본에 저장되었습니다.\n\n백업이 생성되지 않았습니다.",
        'images_saved_overwrite_with_backup': "이미지가 원본에 저장되었습니다.\n\n백업이 생성되었습니다.",
        'images_saved_overwrite_no_backup': "이미지가 원본에 저장되었습니다.\n\n백업이 생성되지 않았습니다.",
        'forms_saved_overwrite_with_backup': "도형이 원본에 저장되었습니다.\n\n백업이 생성되었습니다.",
        'forms_saved_overwrite_no_backup': "도형이 원본에 저장되었습니다.\n\n백업이 생성되지 않았습니다.",
        'signatures_saved_new_file': "{0}개의 서명이 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일이 생성되었습니다.\n\n새 PDF를 로드하는 중...",
        'images_saved_new_file': "{0}개의 이미지가 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일이 생성되었습니다.\n\n새 PDF를 로드하는 중...",
        'forms_saved_new_file': "{0}개의 도형이 삽입되었습니다.\n\n원본 파일은 변경되지 않았습니다.\n새 파일이 생성되었습니다.\n\n새 PDF를 로드하는 중...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "경고: 이 PDF에는 회전된 페이지가 포함되어 있습니다. 위치가 다를 수 있습니다.",
        'page_rotated_warning_title': "회전된 페이지 감지됨",
        'page_rotated_warning_message': "현재 페이지 {0}이(가) {1}° 회전되었습니다.\n\n회전된 페이지에 요소 삽입은 지원되지 않습니다.\n\n지금 페이지를 똑바로 회전하시겠습니까?",
        'page_rotated_warning_voice': "경고: 페이지가 회전되었습니다. 먼저 회전하세요.",
        'paste_on_rotated_page_simple_warning': "페이지 {0}에 삽입할 수 없습니다!\n\n이 페이지는 {1}° 회전되었습니다.\n\n먼저 페이지를 0°로 회전하세요 (메뉴: 편집 → 페이지 정렬).\n\n경고:\n페이지를 회전하기 전에 저장하지 않으면 이전에 복사한 요소가 손실됩니다.",
        'paste_on_rotated_page_voice': "삽입이 취소되었습니다. 페이지가 회전되었습니다. 먼저 페이지를 정렬하세요.",
        'page_rotated_cancel': "취소",
        'page_rotated_rotate_until_upright': "페이지를 반복해서 회전 (똑바를 때까지)",
        'page_rotated_now_upright': "페이지가 이제 똑바릅니다. 이제 삽입할 수 있습니다.",
        'page_rotated_still_not_upright': "페이지를 똑바로 회전할 수 없습니다. 수동으로 수정하세요.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "도움말: 회전된 페이지 수정",
        'help_rotated_pages_voice': "회전된 페이지 수정에 대한 도움말을 엽니다.",
        'btn_help': "도움말",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 문제: 회전된 페이지 – 삽입이 제대로 작동하지 않음</p>

            <p>회전된 페이지에 텍스트, 서명 또는 도형 삽입이 제대로 작동하지 않는 경우 외부 PDF 편집기로 페이지를 수정할 수 있습니다.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ 외부 도구로 해결 (예: macOS 미리보기)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>페이지 내보내기</strong><br>
                &nbsp;&nbsp;메뉴에서 <strong>파일 → 페이지로 내보내기</strong>를 클릭하거나 다른 방법을 사용하여 원하는 페이지를 단일 PDF로 저장합니다.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>외부 프로그램에서 페이지 열기</strong><br>
                &nbsp;&nbsp;내보낸 PDF를 PDF 편집기에서 엽니다 (예: <strong>macOS 미리보기</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>페이지 회전</strong><br>
                &nbsp;&nbsp;페이지가 똑바로 서도록 회전합니다 (미리보기에서: <strong>도구 → 회전</strong> 또는 <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>저장</strong><br>
                &nbsp;&nbsp;수정된 페이지를 저장합니다 (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>페이지를 원본 문서에 다시 삽입</strong><br>
                &nbsp;&nbsp;PDFDarkView로 돌아가서 수정된 페이지를 원하는 위치에 삽입합니다:<br>
                &nbsp;&nbsp;<strong>편집 → 페이지 삽입</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 대안: 원본에서 페이지 회전</p>
                <p style="margin: 5px 0 5px 20px;">• 내장된 회전 기능(<strong>편집 → 페이지 회전</strong>)을 사용하여 페이지를 단계별로 수정합니다.<br>
                • 각 회전 후 삽입이 작동하는지 확인할 수 있습니다.<br>
                • 이것이 종종 더 빠른 해결책입니다 – 먼저 시도해 보세요!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>팁:</strong> 회전된 페이지를 자주 만나는 경우 삽입 대화상자의 경고를 영구적으로 숨길 수 있습니다.<br>
                그러면 위치가 다를 수 있습니다 – 결과를 알고 있는 경우에만 이 옵션을 사용하세요.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "페이지 정렬",
        'menu_rotate_normalize_tooltip': "페이지 회전 또는 0°로 재설정",
        'normalize_current_page': "현재 페이지를 똑바로 세우기 (0°로 설정)",
        'normalize_all_pages': "모든 페이지를 똑바로 세우기 (0°로 설정)",
        'page_normalized': "페이지 {0}을(를) 똑바로 설정했습니다.",
        'all_pages_normalized': "모든 페이지를 똑바로 설정했습니다.",
        'page_already_upright': "페이지 {0}은(는) 이미 똑바릅니다.",
        'all_pages_already_upright': "모든 페이지가 이미 똑바릅니다.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF에 검색 가능한 텍스트가 없습니다.</p><p>{0}(으)로 내보내기 위해 OCR을 수행하시겠습니까?</p>",
        'export_ocr_voice': "PDF에 텍스트가 없습니다. {0}(으)로 내보내려면 OCR이 필요합니다.",
        'export_no_ocr_possible': "OCR 없이 내보낼 수 없습니다. 메뉴를 통해 OCR을 수행하세요.",
        'ocr_failed_export_not_possible': "OCR이 실패했습니다. 내보내기를 수행할 수 없습니다.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF가 미리보기에서 열립니다. 거기서 인쇄 프로세스를 시작하세요.",
        'print_preview_manual': "PDF가 열렸습니다. 수동으로 인쇄 명령을 실행하세요 (예: Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDF 병합",
        'merge_pdfs': "PDF 병합",
        'merge_progress_title': "PDF 병합 중...",
        'merge_pdfs_list': "순서대로 PDF (드래그 앤 드롭으로 정렬)",
        'merge_add_pdf': "PDF 추가",
        'merge_remove': "제거",
        'merge_move_up': "위로",
        'merge_move_down': "아래로",
        'merge_pdfs_info': "💡 팁: 드래그 앤 드롭으로 순서를 변경할 수 있습니다",
        'merge_no_pdfs': "선택한 PDF가 없습니다. 'PDF 추가'를 클릭하세요.",
        'merge_info': "{0}개 PDF 선택 (약 {1}페이지)",
        'merge_open_file': "파일 열기",
        'merge_merge': "병합",
        'merge_error': "병합 중 오류 발생",
        'merge_min_two_pdfs_error': "병합할 PDF 파일을 최소 2개 이상 선택하세요.",
        'merge_select_pdfs': "병합할 PDF 선택",
        'merge_error_file': "처리 중 오류 발생",
        'merge_cancelled': "병합이 취소되었습니다",
        'merge_preparing': "준비 중...",
        'merge_processing': "PDF {0}/{1} 처리 중",
        'merge_saving': "병합된 PDF 저장 중...",
        'merge_complete': "완료!",
        'merge_success_title': "병합 성공",
        'merge_success_voice': "{0}개 PDF가 성공적으로 병합되었습니다.",
        'merge_success_message': "{0}개 PDF가 성공적으로 병합되었습니다.\n\n새 문서는 이제 {1}페이지입니다.\n\n새 파일:\n{2}\n\n저장 위치:\n{3}\n{2}\n\n이 PDF를 열겠습니까?",
        'replace_file_title': "파일을 바꾸시겠습니까?",
        'replace_file_message': "이미 PDF가 열려 있습니다. 새 파일로 바꾸시겠습니까?",
        'btn_yes': "예",
        'btn_no': "아니오",
        'filename_merge_suffix': "병합됨",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "{0} 여는 중...",
        'progress_merge_reading': "{0} 읽는 중...",
        'progress_merge_adding': "{0}페이지 추가 중...",
        'progress_merge_optimizing': "PDF 최적화 중...",
        'progress_merge_writing': "PDF 쓰는 중...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDF 닫기",
        'action_close_window': "창 닫기",
        'action_open_new_pdf': "새 PDF 열기",
        'action_quit_app': "응용 프로그램 종료",
        'changes_saved': "변경 사항이 저장되었습니다.",
        'file_close_title': "PDF 파일 닫기",
        'save_before_action': "{0} 전에 변경 사항을 저장하시겠습니까? 예 또는 아니오?",
        'save_before_action_voice': "{0} 전에 변경 사항을 저장하시겠습니까? 예 또는 아니오?",
        'save_before_close_question': "닫기 전에 변경 사항을 저장하시겠습니까? 예 또는 아니오?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>검색 가능한 PDF 생성됨:\n\n{0}\n\n<b>필요시 다시 시도하세요",
        "ocr_rotate_title": "OCR 전 페이지 정렬",
        "ocr_rotate_question": "PDF에 회전된 페이지가 포함되어 있습니다.\nOCR 전에 모든 페이지를 0°로 정렬하시겠습니까?\n이렇게 하면 텍스트 인식이 크게 향상됩니다.",
        "ocr_rotate_yes": "예, 정렬",
        "ocr_rotate_no": "아니요, OCR 직접 시작",
        "ocr_rotate_voice": "PDF에 회전된 페이지가 포함되어 있습니다. OCR 전에 모든 페이지를 정렬해야 합니까?",
        "ocr_not_performed_message": "텍스트가 없습니다. OCR을 수행하세요 (메뉴 \"편집\" → \"OCR 수행\" 또는 Ctrl+R 키).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR 설정",
        "ocr_language_btn": "OCR 언어 선택",
        "ocr_language": "OCR 언어",
        "ocr_language_current": "현재 언어:",
        "ocr_param_info": "매개변수 정보",

        "ocr_force_ocr_label": "OCR 강제 실행",
        "ocr_deskew_label": "기울기 보정",
        "ocr_clean_label": "이미지 정리",
        "ocr_oversample_label": "해상도 (DPI)",
        "ocr_pagesegmode_label": "페이지 분할",
        "ocr_oem_label": "OCR 엔진 모드",
        "ocr_optimize_label": "PDF 압축",
        "ocr_jobs_label": "병렬 프로세스",
        "ocr_verbose_label": "로그 상세도",

        "ocr_force_ocr_tooltip": "텍스트가 이미 있는 경우에도 모든 페이지에서 OCR 강제 실행",
        "ocr_deskew_tooltip": "기울어진 스캔 자동 정렬",
        "ocr_clean_tooltip": "이미지에서 노이즈 및 아티팩트 제거",
        "ocr_oversample_tooltip": "OCR 전에 이미지를 이 DPI로 확대",
        "ocr_pagesegmode_tooltip": "페이지가 텍스트 영역으로 분할되는 방식을 결정",
        "ocr_oem_tooltip": "Tesseract의 OCR 엔진 선택",
        "ocr_optimize_tooltip": "출력 PDF의 압축 수준",
        "ocr_jobs_tooltip": "병렬 OCR 프로세스 수",
        "ocr_verbose_tooltip": "로그 출력의 상세 수준",
        "ocr_settings_explain_btn": "설명",

        "ocr_force_ocr_explain": "<b>모든</b> 페이지에서 텍스트 인식을 강제합니다(이미 텍스트가 포함된 경우에도).\n\n권장: 스캔한 PDF는 <b>켜기</b>, 이미 텍스트가 있는 기본 PDF는 <b>끄기</b>.",

        "ocr_deskew_explain": "약간 기울어진 스캔을 보정합니다(최대 약 5°).\n\n권장: 스캔한 문서는 <b>켜기</b>, 페이지가 이미 완벽하게 직선이면 <b>끄기</b>.",

        "ocr_clean_explain": "이미지에서 노이즈, 점 및 작은 아티팩트를 제거합니다.\n<b>중요:</b> 분음 부호(글자 위/아래 점)가 있는 아랍어, 태국어 또는 베트남어 텍스트의 경우 이 옵션을 <b>비활성화</b>해야 합니다. 그렇지 않으면 중요한 문자가 손실될 수 있습니다.",

        "ocr_oversample_explain": "지정된 DPI로 <b>텍스트 인식 전에</b> 이미지를 확대합니다.<br><br>• <b>72-150 DPI:</b> 매우 빠르지만 인식률 낮음<br>• <b>200-300 DPI:</b> 최적 범위(기본값: 300)<br>• <b>400+ DPI:</b> 인식은 약간만 향상되지만 파일 크기는 훨씬 커짐<br><br>권장: 복잡한 문자(아랍어, 중국어, 일본어)는 300 DPI, 서양 언어는 200 DPI.",

        "ocr_pagesegmode_explain": "Tesseract가 페이지를 텍스트 영역으로 분할하는 방식을 결정합니다.\n\n• <b>3 - 자동(기본값):</b> 혼합 레이아웃에 좋음\n• <b>4 - 단일 열:</b> 단일 열 텍스트용\n• <b>5 - 세로 블록:</b> 세로 문자용(일본어, 중국어)\n• <b>6 - 균일 텍스트 블록:</b> 열 없이 흐르는 텍스트에 최적\n• <b>11 - 원시 이미지:</b> 불량 스캔/손글씨용\n\n권장: 단순 텍스트 문서는 <b>6</b>, 복잡한 레이아웃은 <b>3</b>.",

        "ocr_oem_explain": "Tesseract의 OCR 엔진을 선택합니다.\n\n• <b>0 - Legacy:</b> 구형 엔진(빠르지만 정확도 낮음)\n• <b>1 - LSTM:</b> 신경망 엔진(느리지만 더 정확함)\n• <b>2 - Legacy + LSTM:</b> 두 결과를 결합\n• <b>3 - 기본값(LSTM 선호):</b> 대부분의 경우 최선의 선택\n\n권장: 최대 인식 정확도를 위해 <b>3</b>.",

        "ocr_optimize_explain": "출력 PDF를 압축합니다.\n\n• <b>0:</b> 최적화 없음(가장 빠른 처리)\n• <b>1:</b> 가벼운 최적화(좋은 절충안)\n• <b>2:</b> 중간 최적화\n• <b>3:</b> 강력한 최적화(가장 작은 파일, 그러나 느림)\n\n권장: 일상 사용에는 <b>1</b>.",

        "ocr_jobs_explain": "OCR을 위한 병렬 프로세스 수.\n\n• <b>1:</b> 느리지만 메모리 소비 가장 낮음\n• <b>4-8:</b> 최신 멀티코어 프로세서에 최적\n• <b>12+:</b> 높은 메모리 사용으로 처리 속도가 거의 향상되지 않음\n\n권장: CPU 코어 수(예: 4코어 시스템에서 <b>4</b>).",

        "ocr_verbose_explain": "콘솔의 로그 출력 상세 수준.\n\n• <b>0:</b> 출력 없음\n• <b>1:</b> 진행 상황 및 상태 메시지\n• <b>2:</b> 상세 출력\n• <b>3:</b> 전체 디버그 출력(매우 방대함)\n\n권장: 정상 작동 시 <b>1</b>.",

        "ocr_reset_title": "설정이 재설정되었습니다",
        "ocr_reset_message": "모든 OCR 설정이 기본값으로 재설정되었습니다.",
        "info_tooltip": "이 매개변수에 대한 추가 정보",
        "ocr_reset_defaults": "기본값으로 재설정",

        "ocr_psm_0": "자동(Legacy 엔진)",
        "ocr_psm_1": "자동 열 감지",
        "ocr_psm_3": "자동(기본값)",
        "ocr_psm_4": "단일 열",
        "ocr_psm_5": "세로 블록",
        "ocr_psm_6": "균일 텍스트 블록",
        "ocr_psm_7": "단일 텍스트 줄",
        "ocr_psm_8": "단일 단어",
        "ocr_psm_11": "원시 이미지(레이아웃 분석 없음)",

        "ocr_oem_0": "Legacy 엔진(빠름)",
        "ocr_oem_1": "LSTM 엔진(신경망, 정확함)",
        "ocr_oem_2": "Legacy + LSTM 결합",
        "ocr_oem_3": "기본값(LSTM 선호)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR 언어...",
        "ocr_language_title": "OCR 언어 선택",
        "ocr_language_instruction": "텍스트 인식(OCR)을 위한 언어를 선택하세요.\n주의: 여러 언어는 성능과 정확도를 저하시킵니다!\n하나의 언어만 선택하면 최상의 결과를 얻을 수 있습니다.",
        "ocr_language_predefined": "미리 정의된 조합",
        "ocr_language_custom": "사용자 정의...",
        "ocr_language_selected": "선택된 OCR 언어",
        "ocr_language_changed": "OCR 언어가 {0}(으)로 변경되었습니다",
        "ocr_language_auto_detect": "사용 가능한 언어가 자동으로 감지됩니다.",
        "ocr_language_none_found": "Tesseract 언어 데이터를 찾을 수 없습니다! 언어 패키지를 설치하세요(예: 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "사용자 정의 언어 선택",
        "ocr_language_available": "사용 가능한 언어(설치됨):",
        "ocr_language_select_hint": "하나 이상의 언어를 선택하세요:",
        "ocr_language_confirm": "적용",
        "ocr_language_reset": "기본값으로 재설정 (deu+eng+vie)",
        "ocr_language_priorities": "권장 언어(사전 설치됨):",

        "select_all_languages": "모두 선택",
        "clear_all_languages": "선택 해제",
        "install_language_packs": "누락된 언어 패키지 설치...",
        "install_hint": "💡 팁: 모든 언어가 시스템에 설치된 것은 아닙니다. 이 버튼을 통해 설치 도움말을 받을 수 있습니다.",
        "ocr_language_install_title": "Tesseract 언어 패키지 설치",

        "ocr_missing_languages": "누락된 OCR 언어 패키지",
        "ocr_missing_languages_message": "다음 선택된 언어가 시스템에 설치되어 있지 않습니다:\n\n{0}\n\n누락된 언어 패키지를 설치하세요('설치 도움말'의 도움말 참조).\n\n지금 설치 도움말을 열겠습니까?",
        "ocr_missing_languages_voice": "언어 패키지가 누락되었습니다. 누락된 언어를 설치하세요.",
        "ocr_install_help_now": "도움말 열기",
        "ocr_continue_anyway": "그래도 시도",
        "ocr_language_error_title": "OCR 언어 오류",
        "ocr_language_error_message": "텍스트 인식 중 오류 발생: {0}\n\nOCR 언어 설정을 확인하세요(설정 → OCR 언어).",
        "ocr_install_help_button": "설치 도움말",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract 언어 패키지 설치</p>

        <p>OCR이 특정 언어에서 작동하려면 해당 언어 데이터가 시스템에 설치되어 있어야 합니다. 운영 체제에 대한 지침을 따르세요:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li><strong>터미널</strong>을 엽니다(Finder → 프로그램 → 유틸리티 → 터미널).</li>
        <li>다음 명령으로 사용 가능한 모든 언어를 설치합니다:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (몇 분 정도 걸릴 수 있습니다.)</li>
        <li>또는 개별 언어만 설치(예: 베트남어):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        현재 Homebrew 버전에서는 <code>*.traineddata</code>를 수동으로 다운로드해야 할 수 있습니다(아래 참조).</li>
        <li>설치 후: 이 대화 상자를 닫고 OCR 언어 선택을 다시 엽니다 – 새 언어가 자동으로 나타납니다.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>터미널을 엽니다(Ctrl+Alt+T).</li>
        <li>원하는 언어를 설치합니다(예: 베트남어):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        중요한 언어 코드: <code>deu</code>(독일어), <code>eng</code>(영어), <code>vie</code>(베트남어), <code>spa</code>(스페인어), <code>fra</code>(프랑스어), <code>ita</code>(이탈리아어), <code>nld</code>(네덜란드어), <code>fin</code>(핀란드어), <code>swe</code>(스웨덴어), <code>nor</code>(노르웨이어).</li>
        <li>사용 가능한 모든 패키지 표시:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (수동)</p>
        <ol>
        <li>원하는 <code>*.traineddata</code> 파일을 다음에서 다운로드합니다:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (예: 베트남어용 <code>vie.traineddata</code>).</li>
        <li>파일을 Tesseract 언어 폴더에 복사합니다(일반적으로):<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (개별 설치에 따라 조정하세요.)</li>
        <li>애플리케이션을 다시 시작합니다(또는 OCR 언어 선택을 다시 엽니다).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 모든 시스템을 위한 대안</p>
        <ul>
        <li>원하는 패키지 관리자로 <strong>OCRmyPDF</strong>와 <strong>Tesseract</strong>를 설치합니다. 대부분의 설치는 이미 일부 표준 언어(영어, 독일어, 프랑스어)를 포함하고 있습니다.</li>
        <li>누락된 언어는 언제든지 설치할 수 있습니다 – OCR 언어 선택은 실제로 존재하는 언어만 나열합니다.</li>
        </ul>

        <hr>
        <p><b>✅ 설치 후:</b> 애플리케이션을 다시 시작할 필요가 없습니다 – 새로 추가된 언어가 즉시 목록에 나타납니다.</p>
        <p><b>📖 언어 코드 도움말:</b> 전체 목록은 <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract 문서</a>에서 확인할 수 있습니다.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans 글꼴",
        "info_noto_font_voice": "Noto Sans 글꼴 설치 가이드",
        "btn_info_noto_font_install": "글꼴 정보",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Google의 무료 Noto 글꼴 설치 방법</h2>

        <p><strong>Noto 글꼴</strong>은 Google의 오픈 소스 글꼴 모음입니다. 그 목표는 <em>"두부 없음"</em>(즉, 빈 상자 □ 없음)을 보고 Unicode 표준의 모든 문자를 올바르게 표시하는 것입니다. 다양한 언어로 텍스트를 표시해야 하는 애플리케이션에 이상적인 추가 기능입니다.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 macOS에 설치</h3>

        <p><strong>방법 1: Homebrew 사용(고급 사용자용)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>방법 2: "Font Book"을 통해(권장)</strong></p>

        <ol>
        <li>공식 글꼴 패키지 다운로드:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP 파일 압축 풀기</li>
        <li>파일을 <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code>에 복사</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Windows에 설치 (10 & 11)</h3>

        <p><strong>방법 1: Microsoft Store(권장)</strong><br>
        "Google Noto Fonts" 또는 "Noto Sans"를 검색하고 <strong>설치</strong>를 클릭합니다.</p>

        <p><strong>방법 2: 수동 설치</strong></p>

        <ol>
        <li>다운로드:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP 압축 풀기</li>
        <li>.ttf / .otf 파일 선택</li>
        <li>마우스 오른쪽 버튼 클릭 → <strong>설치</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        또는<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\사용자명\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Linux에 설치</h3>

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

        <p>확인:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "북마크 관리",
        "bookmark_add": "북마크 추가",
        "bookmark_add_tooltip": "현재 페이지를 북마크로 저장",
        "bookmark_remove": "북마크 제거",
        "bookmark_remove_tooltip": "표시된 북마크 삭제",
        "bookmark_remove_all": "모두 제거",
        "bookmark_remove_all_tooltip": "이 PDF의 모든 북마크 삭제",
        "bookmark_jump": "북마크로 이동",
        "bookmark_jump_tooltip": "선택한 페이지로 이동",
        "bookmark_name": "이름",
        "bookmark_page": "페이지",
        "bookmark_no_bookmarks": "북마크가 없습니다.\n'추가'를 클릭하여 현재 페이지를 북마크로 저장하세요.",
        "bookmark_added": "{0}페이지에 북마크 추가됨: {1}",
        "bookmark_removed": "북마크 제거됨: {0}",
        "bookmark_all_removed": "모든 북마크가 제거되었습니다.",
        "bookmark_name_default": "{0}페이지",
        "bookmark_name_prompt": "북마크 이름:\n(긴 텍스트는 50자로 단축됩니다)",
        "bookmark_name_prompt_title": "북마크 이름",
        "bookmark_confirm_remove_all": "모든 {0}개 북마크를 제거하시겠습니까?",
        "menu_bookmarks": "북마크",
        "bookmark_manage": "북마크 관리",
        "bookmark_next": "다음 북마크",
        "bookmark_prev": "이전 북마크",
        "bookmark_page_display": "{0}페이지",
        "bookmark_exists": "이 페이지에는 이미 이 이름의 북마크가 존재합니다.",
        "bookmark_select_first": "먼저 북마크를 선택하세요.",
        "bookmark_confirm_remove": "'{1}페이지: {0}' 북마크를 제거하시겠습니까?",
        "bookmark_jumped_to": "{1}페이지의 북마크 '{0}'(으)로 이동했습니다.",
        "bookmark_jumped_to_voice": "북마크 {0}, {1}페이지",
        "btn_close": "닫기",

        "bookmark_list": "내 북마크",
        "bookmark_rename": "북마크 이름 바꾸기",
        "bookmark_rename_tooltip": "선택한 북마크의 이름 변경",
        "bookmark_rename_title": "북마크 이름 바꾸기",
        "bookmark_rename_prompt": "{0}페이지 북마크의 새 이름:\n(최대 50자)",
        "bookmark_renamed": "북마크 '{0}'의 이름이 '{1}'(으)로 변경되었습니다.",
        "bookmark_item_tooltip": "{0}페이지: {1}\n더블 클릭하여 이동",
        "bookmark_name_exists_question": "이 페이지에 이미 '{0}' 이름의 북마크가 존재합니다.\n그래도 이름을 바꾸시겠습니까?",

        "context_bookmarks": "북마크",
        "context_bookmark_add_here": "이 페이지에 북마크 추가",
        "context_bookmarks_existing": "기존 북마크:",
        "context_bookmarks_jump": "북마크로 이동:",
        "context_bookmarks_none": "북마크 없음",
        "context_bookmarks_clear_all": "모든 {0}개 북마크 제거",

        "bookmark_search_placeholder": "북마크 검색... (이름 또는 페이지)",
        "bookmark_search_results": "\"%s\"에 대한 북마크 %d개 찾음",
        "bookmark_no_search_results": "\"%s\"에 대한 북마크를 찾을 수 없음",
        "bookmark_no_search_results_label": "\"%s\"에 대한 결과 없음",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF 메타데이터 편집",
        "metadata_title": "제목",
        "metadata_title_placeholder": "문서 제목",
        "metadata_title_tooltip": "문서의 제목(제목 표시줄에 표시됨)",
        "metadata_author": "작성자",
        "metadata_author_placeholder": "작성자 이름",
        "metadata_author_tooltip": "문서 작성자",
        "metadata_subject": "주제",
        "metadata_subject_placeholder": "문서 주제",
        "metadata_subject_tooltip": "내용에 대한 간단한 설명",
        "metadata_keywords": "키워드",
        "metadata_keywords_placeholder": "쉼표로 구분된 키워드",
        "metadata_keywords_tooltip": "문서 분류를 위한 키워드",
        "metadata_creator": "만든이",
        "metadata_creator_placeholder": "PDF를 만든 애플리케이션",
        "metadata_creator_tooltip": "문서를 만드는 데 사용된 소프트웨어",
        "metadata_producer": "제작자",
        "metadata_producer_placeholder": "PDF를 변환한 애플리케이션",
        "metadata_producer_tooltip": "PDF를 변환한 소프트웨어",
        "metadata_creation_date": "생성 날짜",
        "metadata_creation_date_tooltip": "문서 생성 날짜",
        "metadata_mod_date": "수정 날짜",
        "metadata_mod_date_tooltip": "마지막 수정 날짜",
        "metadata_pdf_info": "📄 PDF 정보",
        "metadata_pages": "페이지 수",
        "metadata_file_size": "파일 크기",
        "metadata_pdf_version": "PDF 버전",
        "metadata_encrypted": "암호화됨",
        "metadata_encrypted_yes": "예(비밀번호로 보호됨)",
        "metadata_encrypted_no": "아니요",
        "metadata_reload": "📂 PDF에서 다시 로드",
        "metadata_reset": "변경 사항 취소",
        "metadata_reloaded": "메타데이터가 PDF에서 다시 로드되었습니다.",
        "metadata_reset_done": "모든 메타데이터 필드가 재설정되었습니다.",
        "metadata_no_file": "로드된 PDF 파일이 없습니다.",
        "metadata_save_error": "메타데이터 저장 중 오류",
        "metadata_saved": "메타데이터가 성공적으로 저장되었습니다.",
        "metadata_pdf_version_unknown": "PDF(알 수 없음)",
        "metadata_saved_message": "메타데이터가 성공적으로 저장되었습니다.",
        "metadata_saved_voice": "메타데이터 저장됨.",

        "metadata_custom": "🔧 사용자 정의 메타데이터",
        "metadata_custom_placeholder": "{\n  \"내_필드\": \"내_값\",\n  \"기타_필드\": 123\n}",
        "metadata_custom_tooltip": "사용자 정의 메타데이터를 위한 JSON 형식(선택 사항)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "템플릿 \"{0}\" 선택됨 - 삽입하려면 더블 클릭",
        "text_use_template": "텍스트 블록 사용",
        "text_type": "유형",
        "text_search_templates": "텍스트 블록 검색...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 내보내기 / 가져오기 정보",
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

        <h3>📦 무엇이 내보내지나요? (개요)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">일반 애플리케이션 설정</span></li>
            <li class="detail">• 다크/라이트 모드</li>
            <li class="detail">• 이미지에 대한 다크 모드 반전</li>
            <li class="detail">• 회색 임계값</li>
            <li class="detail">• 언어</li>
            <li class="detail">• 창 형상</li>
            <li class="detail">• 확대/축소 모드</li>
            <li class="detail">• 탐색(탐색 모음 표시)</li>
            <li class="detail">• 음성 출력(켜기/끄기)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">백업 설정</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">파일 이름 지정(타임스탬프, 구분 기호, 접미사)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">삽입 설정</span></li>
            <li class="detail">• 서명</li>
            <li class="detail">• 텍스트 및 텍스트 블록</li>
            <li class="detail">• 체크 표시, 이미지 및 도형</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR 설정</span></li>
            <li class="detail">• 언어</li>
            <li class="detail">• OCR 강제 실행 · 페이지 모드</li>
            <li class="detail">• 이미지 전처리: 기울기 보정, 정리, 오버샘플링</li>
            <li class="detail">• 병렬 작업 수</li>
            <li class="detail">• 반전 모드</li>
            <li class="detail">• 회색 임계값</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">북마크</span></li>
            <li class="detail">• PDF 파일별 모든 북마크(페이지, 이름, 생성 시간)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">비밀번호 데이터베이스</span></li>
            <li class="detail">• 저장된 PDF 비밀번호(선택적으로 암호화 또는 일반 텍스트)</li>
            <li class="detail">• 마스터 비밀번호 해시(설정된 경우)</li>
            <li class="detail">• 확인 데이터</li>
        </ul>

        <h4>⚠️ 중요 참고 사항</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 가져올 때:</strong>
            <ul>
                <li><span class="warning">➜ 현재 모든 설정이 완전히 덮어쓰여집니다</span></li>
                <li>• 애플리케이션을 다시 시작해야 합니다</li>
                <li>• 기존 서명, 텍스트 블록 및 북마크가 대체됩니다</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 마스터 비밀번호 및 내보내기 모드:</strong>
            <ul>
                <li>• 마스터 비밀번호가 활성화되면 선택할 수 있습니다:</li>
                <li>  - <span style="color: #98FB98;"><strong>암호 해독됨</strong></span> (비밀번호는 ZIP에서 일반 텍스트로 표시됨)</li>
                <li>  - <span style="color: #FFA07A;"><strong>암호화됨</strong></span> (대상 시스템에서 마스터 비밀번호로만 읽을 수 있음)</li>
                <li>• 마스터 비밀번호 해시는 <strong>항상</strong> 암호화되어 저장됩니다</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ 보안 공지:</strong>
            <ul>
                <li>• 내보낸 ZIP 파일에는 민감한 데이터(<strong>비밀번호, 북마크, 서명</strong>)가 포함되어 있습니다</li>
                <li>• 안전한 곳에 보관하세요(예: 암호화된 USB 드라이브, 비밀번호 관리자)</li>
                <li>• 파일이 손실되면 저장된 PDF 비밀번호는 복구할 수 없게 손실됩니다</li>
            </ul>
        </div>

        <h4>📁 내보내기 형식</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            설정은 단일 ZIP 파일에 저장됩니다:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            이 ZIP에는 완전한 <code>settings.json</code>(구성 정보)과 포함된 서명 이미지 파일 및 암호화된 비밀번호가 포함되어 있습니다.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "서명 - 가이드",
        'signature_guide_html': """
        📝 <strong>서명 - 빠른 가이드</strong><br>
        <ul>
        <li>마스터 암호 설정</li>
        <li><em>설정</em> 메뉴에서 서명 구성 (크기, 타임스탬프, …)</li>
        <li>원하는 위치에서 <strong>마우스 오른쪽 버튼 클릭</strong>으로 삽입 (세션당 한 번 마스터 암호 필요)</li>
        <li>마우스 또는 화살표 키로 서명 이동</li>
        <li>여러 서명을 차례로 삽입</li>
        <li>각 서명 개별 맞춤 설정</li>
        <li>단일 서명 취소</li>
        <li>모든 서명 한 번에 저장 / 취소</li>
        <li>대신 메뉴 막대를 사용할 수도 있습니다.</li>
        </ul>
        """,
        'signature_guide_voice': "서명에 대한 빠른 가이드. 마스터 암호 설정. 설정에서 서명 구성. 마우스 오른쪽 버튼 클릭으로 삽입.",

        'image_guide_title': "이미지 삽입 - 가이드",
        'image_guide_html': """
        📷 <strong>PDF에 이미지 삽입 - 빠른 가이드</strong><br>
        <ol>
        <li>원하는 위치에서 마우스 오른쪽 버튼 클릭</li>
        <li><em>„이미지 삽입“</em> → 이미지 선택</li>
        <li>이미지 위치 지정: 마우스로 끌기</li>
        <li>크기 조정: 모서리/가장자리에서 끌기</li>
        <li>종횡비 유지: <strong>[A]</strong> 키</li>
        <li>추가 조정: 이미지에서 마우스 오른쪽 버튼 클릭</li>
        </ol>
        <p><strong>팁:</strong> 상황에 맞는 메뉴에서 설정을 조정할 수 있습니다.</p>
        """,
        'image_guide_voice': "이미지에 대한 빠른 가이드. 마우스 오른쪽 버튼 클릭, 이미지 삽입, 선택. 마우스로 위치 지정, 모서리에서 크기 조정. A 키로 종횡비 유지.",

        'form_guide_title': "도형 삽입 - 가이드",
        'form_guide_html': """
        📐 <strong>PDF에 도형 삽입 - 빠른 가이드</strong><br>
        <ol>
        <li>도형 유형 선택 (직사각형, 타원, 선, 화살표)</li>
        <li>위치 클릭:
            <ul>
            <li>직사각형/타원: 한 번 클릭으로 도형 배치</li>
            <li>선/화살표: 시작점과 끝점에 두 번 클릭</li>
            </ul>
        </li>
        <li>도형 위치 지정: 마우스로 끌기</li>
        <li>크기 조정: 모서리/가장자리에서 끌기</li>
        <li>도형 저장: <strong>Enter</strong></li>
        <li>도형 취소: <strong>ESC</strong></li>
        <li>추가 조정: 도형에서 마우스 오른쪽 버튼 클릭</li>
        </ol>
        <p><strong>팁:</strong> 상황에 맞는 메뉴에서 설정을 조정할 수 있습니다.</p>
        """,
        'form_guide_voice': "도형에 대한 빠른 가이드. 도형 유형 선택. 직사각형 또는 타원은 한 번 클릭, 선 또는 화살표는 두 번 클릭. 마우스로 위치 지정, 모서리에서 크기 조정. Enter로 저장, Escape로 취소.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "이전",
        "btn_next_result": "다음",
        "ocr_text_window": "OCR 텍스트 창",
        "bookmark_existing": "기존 책갈피",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR 비교 Mac - Windows",
        'ocr_method_mac_win_title': "Mac과 Windows의 OCR 차이점",
        'ocr_method_mac_win_voice': "Mac이 더 좋음",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – macOS와 Windows의 차이점</strong></p>

        <p><strong>macOS (권장)</strong></p>
        <p>도구:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>결과:</p>
        <ul>
        <li>원본 레이아웃을 대부분 유지하는 임베디드 텍스트가 포함된 검색 가능한 PDF.</li>
        </ul>
        <p>장점:</p>
        <ul>
        <li>뛰어난 텍스트 인식 품질 (휘어진 페이지에서도).</li>
        <li>벡터 그래픽 및 글꼴 유지.</li>
        <li>하위 프로세스 평가를 통한 GUI 진행 표시줄.</li>
        <li>모든 OCR 매개변수에 대한 완전한 제어 (Deskew, Clean, Oversample, 최적화).</li>
        <li>텍스트 검색은 기본 창(PDF 보기)에서 직접 사용 가능합니다.</li>
        </ul>
        <p>단점:</p>
        <ul>
        <li>추가 시스템 도구 필요 (ocrmypdf, Ghostscript, unpaper, pngquant – 앱 번들에 포함됨).</li>
        <li>더 복잡한 오류 처리 (교착 상태, 시간 초과).</li>
        </ul>

        <p><strong>Windows (안정적인 대안)</strong></p>
        <p>도구:</p>
        <ul>
        <li>pytesseract (Tesseract에 직접 연결) + reportlab + PyPDF2</li>
        </ul>
        <p>결과:</p>
        <ul>
        <li>시각적으로 이미지 PDF에 해당하지만 투명 텍스트를 통해 검색 가능한 PDF.</li>
        </ul>
        <p>장점:</p>
        <ul>
        <li>지금은 떠오르는 것이 없습니다.</li>
        </ul>
        <p>단점:</p>
        <ul>
        <li>PDF는 본질적으로 보이지 않는 텍스트가 있는 이미지입니다. 복잡한 문서(열, 표)에서는 레이아웃이 약간 다를 수 있습니다.</li>
        <li>자동 기울임 보정 (--deskew) 또는 이미지 정리 (--clean)가 없습니다.</li>
        <li>GUI 진행 표시줄은 처리된 페이지 수에 따라 대략적으로만 업데이트됩니다.</li>
        <li>OCR 속도가 약간 느립니다 (각 페이지가 개별적으로 처리되기 때문).</li>
        <li>텍스트 검색이 OCR 텍스트 창으로 리디렉션됩니다.</li>
        </ul>

        <p><strong>공통점</strong></p>
        <ul>
        <li>두 방법 모두 소스 파일과 동일한 디렉터리에 검색 가능한 PDF를 생성합니다.</li>
        <li>OCR 설정 (언어, DPI, 페이지 분할 모드, OCR 엔진 모드)은 OCRSettingsDialog를 통해 구성할 수 있으며 두 구현 모두에서 적용됩니다.</li>
        </ul>

        <p><strong>권장 사항:</strong></p>
        <ul>
        <li>macOS: ocrmypdf 바이너리가 최상의 결과를 제공합니다 – Mac을 구입하여 버전을 사용하십시오 (Apple Silicon 또는 Intel 칩이 장착된 Mac용 PDFDarkView). OCR 결과가 Windows보다 좋습니다!</li>
        <li>Windows: pytesseract 솔루션을 사용하십시오. 안정적이며 대부분의 문서에 대해 완전히 충분한 품질을 제공합니다.</li>
        </ul>

        <p><strong>중요 참고 사항:</strong></p>
        <ul>
        <li>두 버전 모두 사용자 인터페이스에 완전히 통합되어 있습니다 – 사용자는 차이를 느끼지 못합니다.</li>
        <li>프로그램은 운영 체제에 따라 사용할 OCR 엔진을 자동으로 결정합니다.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "서명 생성 (스캔에서)",
        "signature_create_title": "스캔한 서명 선택 (PDF/이미지)",
        "image_pdf_filter": "이미지 및 PDF",
        "signature_pdf_empty": "PDF에 페이지가 없습니다.",
        "signature_created_success": "서명이 성공적으로 생성되었습니다: {0}",
        "signature_create_error": "서명 생성 중 오류:\n{0}",
        "rembg_missing": "rembg가 설치되지 않았습니다.\n설치하세요: pip install rembg\n오류: {0}",
        "signature_name_title": "서명용 파일 이름",
        "signature_name_message": "새 서명의 파일 이름을 입력하세요 (투명 배경의 PNG로 저장됩니다):",
        "signature_name_label": "파일 이름:",
        "signature_name_voice": "서명용 파일 이름 입력",
        "signature_processing": "처리 중...",
        "signature_creation_title": "서명 생성 중",
        "signature_overwrite_warning": "파일 '{0}'이(가) 이미 존재합니다. 덮어쓰시겠습니까?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"서명용 PDF 준비",
        "signature_prepare_instruction":"단일 페이지에 스캔한 서명이 포함된 PDF를 선택하세요.\n\n최적의 인식을 위해 다음 조건을 충족해야 합니다:\n• 서명이 흰 종이에 검은 잉크(볼펜 또는 가는 펜)로 쓰여 있어야 합니다.\n• 서명이 비어 있는 A4 페이지의 상단 3분의 1에 위치해야 합니다.\n• PDF가 최소 300 dpi로 스캔되어야 합니다.\n• 서명이 선명하고 너무 가늘지 않아야 합니다.\n• 방해되는 배경 패턴이나 선이 없어야 합니다.",
        "signature_prepare_voice":"스캔한 서명이 있는 PDF를 선택하세요. 좋은 품질과 대비에 주의하세요.",
        "sig_thickness_label":"선 굵기:",
        "sig_thickness_normal":"보통 (얇음)",
        "sig_thickness_bold":"굵게 (권장)",
        "sig_thickness_very_bold":"매우 굵게",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI 및 OCR 언어 추가 - 가이드",
        'language_guide_title': "GUI 및 OCR 언어 추가",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>원하는 번역 파일 <code>translations_xy.py</code>을(를) 다음에서 다운로드하세요<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        다음 디렉토리에 넣으세요:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>웹 브라우저를 엽니다.</li>
        <li>다음으로 이동: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>화면 오른쪽 가장자리에서 "Releases"를 찾아 <strong>"latest"</strong>라고 표시된 것을 선택합니다.</li>
        <li>다음 릴리스 페이지에서 맨 아래에 있는 <code>Source Code.zip</code> 파일을 다운로드합니다.</li>
        <li>ZIP 파일의 압축을 풉니다.</li>
        <li>압축을 푼 폴더에서 필요한 모든 언어 파일을 찾아 다음 디렉토리에 복사합니다:<br/>
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
        "menu_watermark":"워터마크 삽입",
        "fullpage_text_watermark_title":"텍스트 워터마크",
        "fullpage_image_watermark_title":"이미지 워터마크",
        "filename_with_watermark":"_워터마크_포함",
        "watermark_text":"텍스트:",
        "watermark_text_placeholder":"워터마크 텍스트...",
        "watermark_font_family":"글꼴:",
        "watermark_font_size":"글꼴 크기:",
        "watermark_format":"서식:",
        "watermark_bold":"굵게",
        "watermark_italic":"기울임",
        "watermark_color":"색상:",
        "watermark_choose_color":"색상 선택...",
        "watermark_opacity":"불투명도 / 투명도:",
        "watermark_direction":"읽기 방향:",
        "watermark_direction_l_r":"왼쪽 → 오른쪽",
        "watermark_direction_bl_tr":"왼쪽 아래 → 오른쪽 위",
        "watermark_direction_tl_br":"왼쪽 위 → 아래",
        "watermark_direction_b_t":"아래 → 위",
        "watermark_direction_t_b":"위 → 아래",
        "watermark_preview":"미리보기:",
        "watermark_preview_sample":"샘플 텍스트",
        "watermark_empty_text":"텍스트를 입력하세요.",
        "watermark_applied":"모든 페이지에 워터마크가 적용되었습니다.",
        "watermark_saved":"워터마크가 저장되었습니다.",
        "image_scale":"크기:",
        "image_preview":"이미지 미리보기:",
        "no_image_selected":"선택된 이미지 없음",
        "browse":"찾아보기...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "편집 제한",
        "redact_add_black": "편집 제한 (검정)",
        "redact_add_white": "편집 제한 (흰색 / 지우기)",
        "redact_added_black": "검정 편집 제한 추가됨",
        "redact_added_white": "흰색 편집 제한 추가됨",
        "redact_apply_all": "모든 편집 제한 적용 및 저장",
        "redact_discard_all": "모든 편집 제한 취소",
        "redact_discard": "이 편집 제한 취소",
        "no_redactions": "편집 제한 없음",
        "redact_confirm_title": "편집 제한 영구 적용",
        "redact_confirm_message": "경고: 표시된 영역이 영구적으로 삭제됩니다 (검정 또는 흰색).\n백업이 생성됩니다 (활성화된 경우).\n\n계속하시겠습니까?",
        "redact_apply": "예, 지금 편집 제한 적용",
        "redact_saved": "{0}개 편집 제한이 성공적으로 적용 및 저장되었습니다.",
        "redact_saved_voice": "{0}개 편집 제한 적용됨",
        "redact_error": "편집 제한 중 오류 발생",
        "filename_redacted":"_편집제한됨",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': '페이지 번호 삽입',
        'page_numbers_format': '번호 형식:',
        'page_numbers_format_arabic': '1, 2, 3 ... (아라비아 숫자)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (로마자 소문자)',
        'page_numbers_format_roman_upper': 'I, II, III ... (로마자 대문자)',
        'page_numbers_format_letter': 'A, B, C ... (알파벳)',
        'page_numbers_format_custom': '사용자 정의',
        'page_numbers_custom_pattern': '패턴:',
        'page_numbers_custom_placeholder': '예: "페이지 {nummer}" 또는 "{nummer} / {total}"',
        'page_numbers_custom_tooltip': '현재 페이지 번호에는 {nummer}, 총계에는 {total}을 사용하세요',
        'page_numbers_position': '위치:',
        'page_numbers_pos_tl': '왼쪽 위',
        'page_numbers_pos_tc': '위 중앙',
        'page_numbers_pos_tr': '오른쪽 위',
        'page_numbers_pos_ml': '왼쪽 중앙',
        'page_numbers_pos_mc': '중앙',
        'page_numbers_pos_mr': '오른쪽 중앙',
        'page_numbers_pos_bl': '왼쪽 아래',
        'page_numbers_pos_bc': '아래 중앙',
        'page_numbers_pos_br': '오른쪽 아래',
        'page_numbers_margins': '여백:',
        'page_numbers_margin_x': '가로 거리:',
        'page_numbers_margin_y': '세로 거리:',
        'page_numbers_range': '페이지 범위:',
        'page_numbers_all_pages': '모든 페이지',
        'page_numbers_custom_range': '사용자 정의 범위',
        'page_numbers_from': '시작:',
        'page_numbers_to': '종료:',
        'page_numbers_progress': '페이지 번호 삽입 중...',
        'page_numbers_start': '페이지 번호 삽입 시작...',
        'page_numbers_cancel': '페이지 번호 삽입 취소됨',
        'page_numbers_success': '페이지 번호가 성공적으로 추가되었습니다.\n\n새 PDF를 열겠습니까?\n\n{0}',
        'page_numbers_complete': '페이지 번호 추가됨',
        'page_numbers_error_format': '페이지 번호 삽입 중 오류 발생: {0}',
        'page_numbers_content_type': '콘텐츠 유형:',
        'page_numbers_tab_simple': '간단한 번호',
        'page_numbers_tab_range': '페이지 X / Y',
        'page_numbers_tab_date': '날짜',
        'page_numbers_tab_custom': '자유 텍스트',
        'page_numbers_range_format': '형식:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': '페이지 {aktuell} / {gesamt}',
        'page_numbers_range_custom': '사용자 정의',
        'page_numbers_range_placeholder': '예: "페이지 {aktuell} / {gesamt}"',
        'page_numbers_date_format': '날짜 형식:',
        'page_numbers_date_short': '2024.01.01',
        'page_numbers_date_long': '2024년 1월 1일',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': '사용자 정의',
        'page_numbers_date_placeholder': '예: %Y년 %m월 %d일 %H:%M',
        'page_numbers_date_position': '위치:',
        'page_numbers_date_before': '페이지 번호 앞에 날짜',
        'page_numbers_date_after': '페이지 번호 뒤에 날짜',
        'page_numbers_date_only': '날짜만 (페이지 번호 없음)',
        'page_numbers_custom_text': '사용자 정의 텍스트:',
        'page_numbers_custom_placeholder_text': '페이지 번호에는 {seite}, 총계에는 {gesamt}을 사용하세요\n예: "기밀 - 페이지 {seite}" 또는 "{seite} / {gesamt}"',
        "filename_with_page_number":"_페이지번호_포함",
        "filename_with_page_declaration":"_페이지_선언_포함",
        "filename_with_pagenumber":"_페이지번호_포함",
        "filename_with_date":"_날짜_포함",
        "filename_with_my_page_declaration":"_사용자정의_페이지_선언_포함",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "저장되지 않은 변경사항",
        "unsaved_changes_message_darkmode": "저장되지 않은 삽입물이 있습니다.\n전환하기 전에 저장하시겠습니까?",
        "save_and_switch": "저장 및 전환",
        "discard_and_switch": "지금 전환",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': '페이지를 이미지로 내보내기',
        'export_images_menu': '이미지로 내보내기 (PNG/JPEG)',
        'export_images_format': '이미지 형식:',
        'export_images_dpi': '해상도 (DPI):',
        'export_images_quality': 'JPEG 품질:',
        'export_images_range': '페이지 범위:',
        'export_images_all_pages': '모든 페이지',
        'export_images_custom_range': '사용자 정의 범위',
        'export_images_from': '시작:',
        'export_images_to': '종료:',
        'export_images_options': '옵션:',
        'export_images_single_files': '각 페이지를 별도 파일로',
        'export_images_subfolder': '하위 폴더로 내보내기',
        'export_images_subfolder_info': '하위 폴더 "PDF이름_이미지"로',
        'export_images_same_folder': 'PDF와 동일한 폴더에',
        'export_images_apply_darkmode': 'PDFDarkView 설정 적용 (다크 모드)',
        'export_images_target_folder': '대상 폴더:',
        'export_images_browse': '찾아보기...',
        'export_images_preview': '미리보기:',
        'export_images_preview_info': '내보내기 설정 선택',
        'export_images_preview_info_detail': '{0} 페이지를 {1}(으)로\n해상도: {2} DPI\n파일명: {3}\n{4}',
        'export_images_select_folder': '대상 폴더 선택',
        'export_images_start': '이미지 내보내기 시작...',
        'export_images_progress': '이미지 내보내는 중...',
        'export_images_saving': '페이지 {0}/{1} 저장 중...',
        'export_images_success': '내보내기 성공!\n\n{0}개 이미지를 저장했습니다:\n{1}',
        'export_images_complete': '이미지 내보내기 완료',
        'export_images_open_folder': '📁 폴더 열기',
        'export_images_cancel': '이미지 내보내기 취소됨',
        'export_images_error_format': '이미지 내보내기 중 오류 발생: {0}',
        'export_images_pdf2image_missing': '"pdf2image" 라이브러리가 설치되지 않았습니다.\n\n다음 명령으로 설치하세요:\npip install pdf2image\n\nWindows의 경우 Poppler도 필요합니다:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': '장기 보관용 PDF/A 변환',
        'pdfa_menu': 'PDF/A 변환 (아카이브용)',
        'pdfa_info': 'PDF를 PDF/A 형식으로 변환합니다.\n\nPDF/A는 장기 보관용으로 특별히 설계되었으며, 문서가 미래에도 올바르게 표시되도록 보장합니다.',
        'pdfa_standard': 'PDF/A 표준:',
        'pdfa_standard_select': '버전:',
        'pdfa_1': 'PDF/A-1 (간단, 광범위 호환)',
        'pdfa_2': 'PDF/A-2 (현대적, 더 나은 압축)',
        'pdfa_3': 'PDF/A-3 (최신 버전, 첨부 파일 허용)',
        'pdfa_standards_explanation': '📖 표준 설명:\n\n'
            '• PDF/A-1: 기본, 구형 시스템과 호환 (약 2005년)\n'
            '• PDF/A-2: 더 현대적, 더 나은 압축, 투명도 지원 (약 2011년)\n'
            '• PDF/A-3: 최신 버전, 파일 첨부 삽입 허용 (약 2013년)\n\n'
            '권장: PDF/A-2는 호환성과 현대적 기능 간의 좋은 균형입니다.',
        'pdfa_options': '옵션:',
        'pdfa_compress_enable': 'PDF 압축 (더 작은 파일)',
        'pdfa_metadata_preserve': '메타데이터 보존 (제목, 저자 등)',
        'pdfa_target_folder': '대상 폴더:',
        'pdfa_browse': '찾아보기...',
        'pdfa_select_folder': '대상 폴더 선택',
        'pdfa_ocr_info_unknown': '🔍 텍스트 내용을 확인할 수 없습니다.',
        'pdfa_ocr_info_not_needed': '✅ 텍스트 있음 - OCR 불필요.\nPDF/A를 직접 생성할 수 있습니다.',
        'pdfa_ocr_info_recommended': '⚠️ 충분한 텍스트를 찾을 수 없습니다.\n\n검색 가능한 PDF의 경우 먼저 OCR을 실행하는 것이 좋습니다.\n참고: OCR 없이도 PDF/A는 작동하지만, 텍스트를 검색할 수 없습니다.',
        'pdfa_ocr_info_error': '❌ 확인 중 오류 발생: {0}',
        'pdfa_start': 'PDF/A 변환 시작...',
        'pdfa_progress': 'PDF/A 변환 중...',
        'pdfa_success': 'PDF/A 변환 성공!\n\n다음으로 저장됨:\n{0}\n\n새 PDF를 열겠습니까?',
        'pdfa_complete': 'PDF/A 변환 완료',
        'pdfa_cancel': 'PDF/A 변환 취소됨',
        'pdfa_error_format': 'PDF/A 변환 중 오류 발생:\n\n{0}',
        'pdfa_ocrmypdf_missing': '"ocrmypdf" 라이브러리가 설치되지 않았습니다.\n\n다음 명령으로 설치하세요:\npip install ocrmypdf',
        'btn_convert': '변환',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF 최적화 (파일 크기 줄이기)',
        'optimize_menu': 'PDF 최적화 (파일 크기)',
        'optimize_info': '다양한 최적화 방법을 통해 PDF 파일 크기를 줄입니다.\n\n압축 수준이 높을수록 파일이 작아지지만, 이미지 품질이 저하될 수 있습니다.',
        'optimize_level': '압축 수준:',
        'optimize_level_low': '낮음 (빠름, 작은 절감)',
        'optimize_level_medium': '중간 (좋은 균형)',
        'optimize_level_high': '높음 (큰 절감)',
        'optimize_level_maximum': '최대 (최대 절감, 느림)',
        'optimize_level_explanation': '권장: "중간"은 속도와 파일 크기 간의 좋은 균형입니다.',
        'optimize_options': '옵션:',
        'optimize_compress_images': '이미지 압축 (JPEG 품질 낮춤)',
        'optimize_clean_objects': '사용하지 않는 개체 제거',
        'optimize_preserve_metadata': '메타데이터 보존 (제목, 저자 등)',
        'optimize_image_quality': '이미지 품질:',
        'optimize_range': '페이지 범위:',
        'optimize_all_pages': '모든 페이지',
        'optimize_custom_range': '사용자 정의 범위',
        'optimize_from': '시작:',
        'optimize_to': '종료:',
        'optimize_target_folder': '대상 폴더:',
        'optimize_browse': '찾아보기...',
        'optimize_select_folder': '대상 폴더 선택',
        'optimize_info_box': '정보',
        'optimize_info_text': '큰 PDF의 경우 최적화에 몇 분이 걸릴 수 있습니다.\n\n이미지는 품질을 낮춰 저장되므로 파일 크기를 크게 줄일 수 있습니다.',
        'optimize_start': 'PDF 최적화 시작...',
        'optimize_progress': 'PDF 최적화 중...',
        'optimize_cancel': 'PDF 최적화 취소됨',
        'optimize_complete': 'PDF 최적화 완료',
        'optimize_error_format': 'PDF 최적화 중 오류 발생:\n\n{0}',
        'optimize_success_message': 'PDF 최적화 성공!\n\n다음으로 저장됨:\n{0}\n\n최적화 전: {1}\n최적화 후: {2}\n절감: {3:.1f}%\n\n{4}\n\n최적화된 PDF를 열겠습니까?',
        'optimize_success_message_no_size': 'PDF 최적화 성공!\n\n다음으로 저장됨:\n{0}\n\n크기 정보를 사용할 수 없습니다.\n\n최적화된 PDF를 열겠습니까?',
        'optimize_result_positive': '파일이 {0:.1f}% 줄었습니다.',
        'optimize_result_zero': '파일 크기에 변화가 없습니다.',
        'optimize_result_negative': '파일이 {0:.1f}% 증가했습니다.\n최적화를 건너뛰고 원본 파일을 유지했습니다.',
        'btn_optimize': '최적화 시작',
        'filename_optimize_low_suffix': '_최적화_낮음',
        'filename_optimize_medium_suffix': '_최적화',
        'filename_optimize_high_suffix': '_최적화_높음',
        'filename_optimize_maximum_suffix': '_최적화_최대',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDF 자르기',
        'crop_menu': 'PDF 자르기 (Crop)',
        'crop_range': '적용 대상:',
        'crop_all_pages': '모든 페이지',
        'crop_current_page': '현재 페이지만',
        'crop_values': '자르기 값 (포인트 단위):',
        'crop_left': '왼쪽:',
        'crop_right': '오른쪽:',
        'crop_top': '위:',
        'crop_bottom': '아래:',
        'crop_presets': '사전 설정:',
        'crop_preset_white': '흰색 여백 감지',
        'crop_reset': '재설정',
        'crop_mouse_hint': '🖱️ 사각형을 드래그하여 영역을 대략 선택합니다.\n그런 다음 SpinBox에서 값을 정확하게 조정할 수 있습니다.\n마우스로 수동 조정은 불가능합니다.',
        'crop_apply': '자르기',
        'crop_scope_all': '모든 페이지',
        'crop_scope_current': '현재 페이지',
        'crop_new_size': '새 크기: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': '로드된 PDF 없음',
        'crop_preview_error': '미리보기 로드 중 오류 발생',
        'crop_start': '자르기 시작...',
        'crop_progress': 'PDF 자르는 중...',
        'crop_success': 'PDF 자르기 성공!\n\n다음으로 저장됨:\n{0}\n\n자른 PDF를 열겠습니까?',
        'crop_complete': '자르기 완료',
        'crop_cancel': '자르기 취소됨',
        'crop_error_format': '자르기 중 오류 발생:\n\n{0}',
        'filename_crop_suffix': '_자름',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDF 평탄화 (Flatten)',
        'flatten_menu': 'PDF 평탄화 (Flatten)',
        'flatten_info': 'PDF를 평탄화하면 모든 편집 가능한 요소가 페이지 콘텐츠에 "굳혀집니다".\n\n이후에는 양식 필드, 주석, 텍스트, 십자, 서명, 이미지 및 도형을 개별적으로 편집할 수 없습니다.',
        'flatten_explanation_title': '📖 이것은 어떤 용도로 사용되나요?',
        'flatten_explanation_text': '평탄화는 다음 상황에서 필요합니다:\n\n'
            '• 📄 문서를 인쇄용으로 준비하려는 경우\n'
            '• 🔒 누군가 양식 필드를 변경하는 것을 방지하려는 경우\n'
            '• 📎 주석과 댓글을 문서에 "영구적으로" 포함하려는 경우\n'
            '• 🖼️ 삽입된 텍스트, 십자, 서명, 이미지 및 도형을 문서에 영구적으로 고정하려는 경우\n'
            '• 📦 파일을 아카이브용으로 준비하려는 경우\n\n'
            '평탄화는 PDF를 더 작게 만들고 요소가 실수로 이동되거나 삭제되는 것을 방지합니다.',
        'flatten_what_title': '무엇이 평탄화되나요?',
        'flatten_what_list': '• ✅ 양식 필드 (텍스트 필드, 체크박스, 버튼)\n'
            '• ✅ 주석 (댓글, 강조, 메모)\n'
            '• ✅ 오버레이 (텍스트, 십자, 서명, 이미지, 도형)',
        'flatten_options': '옵션:',
        'flatten_forms': '양식 필드 평탄화',
        'flatten_annotations': '주석 평탄화',
        'flatten_overlays': '오버레이 평탄화 (텍스트, 십자, 서명, 이미지, 도형)',
        'flatten_target_folder': '대상 폴더:',
        'flatten_browse': '찾아보기...',
        'flatten_select_folder': '대상 폴더 선택',
        'flatten_warning': '⚠️ 중요: 평탄화는 되돌릴 수 없는 과정입니다!\n\n평탄화 후에는 편집 가능한 요소를 개별적으로 변경하거나 삭제할 수 없습니다.\n필요한 경우 미리 백업을 만드세요.',
        'flatten_apply': '평탄화',
        'flatten_start': '평탄화 시작...',
        'flatten_progress': 'PDF 평탄화 중...',
        'flatten_success': 'PDF 평탄화 성공!\n\n다음으로 저장됨:\n{0}\n\n평탄화된 PDF를 열겠습니까?',
        'flatten_complete': '평탄화 완료',
        'flatten_cancel': '평탄화 취소됨',
        'flatten_error_format': '평탄화 중 오류 발생:\n\n{0}',
        'filename_flatten_suffix': '_평탄화됨',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF 오버레이 (Overlay)',
        'overlay_menu': 'PDF 오버레이 (Overlay)',
        'overlay_info': '하나의 PDF (오버레이)를 다른 PDF 위에 배치합니다.\n\n오버레이 PDF가 기본 PDF 위에 배치됩니다. 이는 워터마크, 로고, 레터헤드 또는 스탬프에 유용합니다.',
        'overlay_explanation_title': '📖 이것은 어떤 용도로 사용되나요?',
        'overlay_explanation_text': '오버레이는 다음 상황에서 필요합니다:\n\n'
            '• 🏢 회사 로고를 워터마크로 각 페이지에 배치\n'
            '• 📄 빈 PDF에 레터헤드 배치\n'
            '• 🖊️ 문서에 스탬프 오버레이 배치\n'
            '• 🔖 모든 페이지에 워터마크 배치\n'
            '• 📑 템플릿에 양식 오버레이 배치',
        'overlay_type': '오버레이 유형:',
        'overlay_type_fullpage': '전체 페이지 (덮기)',
        'overlay_type_transparent': '전체 페이지 (투명 - 권장)',
        'overlay_type_stamp': '스탬프 (위치 지정 가능)',
        'overlay_type_info_fullpage': '📄 오버레이 PDF가 전체 페이지에 정확히 배치됩니다.\n흰색 배경을 제거하여 콘텐츠만 표시할 수 있습니다.',
        'overlay_type_info_transparent': '🔍 오버레이 PDF가 투명 배경으로 전체 페이지에 배치됩니다.\n흰색 배경이 자동으로 제거됩니다 - 워터마크와 로고에 이상적!',
        'overlay_type_info_stamp': '🖊️ 오버레이 PDF가 스탬프로 위치 지정 및 크기 조정됩니다.\n특정 위치의 로고, 스탬프 또는 서명에 완벽합니다.',
        'overlay_remove_background': '흰색 배경 제거:',
        'overlay_remove_background_enable': '오버레이 PDF에서 흰색 배경 제거 (오버레이를 투명하게 만듦)',
        'overlay_remove_background_tooltip': '오버레이 PDF에서 흰색 영역을 제거하여 아래의 텍스트가 보이게 합니다.',
        'overlay_threshold': '임계값:',
        'overlay_threshold_hint': '(1-254, 높을수록 더 많은 흰색이 제거됨)',
        'overlay_select_file': '오버레이 PDF 선택:',
        'overlay_file_placeholder': '오버레이용 PDF 파일을 선택하세요',
        'overlay_browse': '찾아보기...',
        'overlay_select_overlay': '오버레이 PDF 선택',
        'overlay_range': '페이지 범위:',
        'overlay_all_pages': '모든 페이지',
        'overlay_custom_range': '사용자 정의 범위',
        'overlay_from': '시작:',
        'overlay_to': '종료:',
        'overlay_position': '위치:',
        'overlay_position_center': '중앙',
        'overlay_position_top_left': '왼쪽 위',
        'overlay_position_top_right': '오른쪽 위',
        'overlay_position_bottom_left': '왼쪽 아래',
        'overlay_position_bottom_right': '오른쪽 아래',
        'overlay_size': '크기:',
        'overlay_size_original': '원본 크기',
        'overlay_size_fit_page': '페이지에 맞춤',
        'overlay_size_custom': '사용자 정의 (%)',
        'overlay_opacity': '투명도:',
        'overlay_target_folder': '대상 폴더:',
        'overlay_browse_folder': '찾아보기...',
        'overlay_select_folder': '대상 폴더 선택',
        'overlay_warning': '⚠️ 참고: 오버레이 PDF가 기본 PDF 위에 배치되고 "굳혀집니다".\n\n저장 후 오버레이 PDF의 요소를 개별적으로 편집할 수 없습니다.',
        'overlay_apply': '오버레이',
        'overlay_start': '오버레이 시작...',
        'overlay_progress': 'PDF 오버레이 중...',
        'overlay_success': 'PDF 오버레이 성공!\n\n다음으로 저장됨:\n{0}\n\n오버레이된 PDF를 열겠습니까?',
        'overlay_complete': '오버레이 완료',
        'overlay_cancel': '오버레이 취소됨',
        'overlay_error_format': '오버레이 중 오류 발생:\n\n{0}',
        'overlay_no_file': '선택된 오버레이 PDF가 없습니다.\n\n오버레이할 PDF 파일을 선택하세요.',
        'filename_overlay_suffix': '_오버레이됨',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'PDF에서 이미지 추출',
        'extract_images_menu': '모든 이미지 추출',
        'extract_images_info': 'PDF에서 모든 이미지를 추출하여 별도 파일로 저장합니다.\n\n이미지는 원본 형식으로 저장되거나 선택한 형식으로 변환됩니다.',
        'extract_images_format': '이미지 형식:',
        'extract_images_quality': 'JPEG 품질:',
        'extract_images_options': '옵션:',
        'extract_images_subfolder': '하위 폴더로 추출 ("PDF이름_이미지")',
        'extract_images_unique': '고유 이미지만 (중복 방지)',
        'extract_images_range': '페이지 범위:',
        'extract_images_all_pages': '모든 페이지',
        'extract_images_custom_range': '사용자 정의 범위',
        'extract_images_from': '시작:',
        'extract_images_to': '종료:',
        'extract_images_target_folder': '대상 폴더:',
        'extract_images_browse': '찾아보기...',
        'extract_images_select_folder': '대상 폴더 선택',
        'extract_images_info_box': '정보',
        'extract_images_info_text': '큰 PDF의 경우 추출에 몇 분이 걸릴 수 있습니다.\n\n이미지는 원본 이름 (페이지_이미지)으로 저장됩니다.',
        'extract_images_extract': '추출',
        'extract_images_start': '추출 시작...',
        'extract_images_progress': '이미지 추출 중...',
        'extract_images_success': '✅ 이미지 추출 성공!\n\n{0}개 이미지를 저장했습니다:\n{1}',
        'extract_images_complete': '이미지 추출 완료',
        'extract_images_cancel': '추출 취소됨',
        'extract_images_error_format': '이미지 추출 중 오류 발생:\n\n{0}',
        'extract_images_open_folder': '📁 폴더 열기',
        'extract_images_no_images': 'PDF에서 이미지를 찾을 수 없습니다.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': '한 페이지에 여러 페이지 (N-Up)',
        'nup_menu': '한 페이지에 여러 페이지 (N-Up)',
        'nup_info': '여러 PDF 페이지를 한 페이지에 배치합니다.\n\n컴팩트한 인쇄, 개요 또는 유인물에 이상적입니다.',
        'nup_layout': '레이아웃:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': '미리보기:',
        'nup_preview_info': '{0} 페이지 → 시트당 {1} 페이지 → {2} 시트\n레이아웃: {3}',
        'nup_order': '순서:',
        'nup_order_horizontal': '가로 (행 순서)',
        'nup_order_vertical': '세로 (열 순서)',
        'nup_order_horizontal_reverse': '가로 역순',
        'nup_order_vertical_reverse': '세로 역순',
        'nup_range': '페이지 범위:',
        'nup_all_pages': '모든 페이지',
        'nup_custom_range': '사용자 정의 범위',
        'nup_from': '시작:',
        'nup_to': '종료:',
        'nup_options': '옵션:',
        'nup_margins': '여백:',
        'nup_margin_between': '페이지 간 간격:',
        'nup_page_numbers': '페이지 번호 삽입',
        'nup_target_folder': '대상 폴더:',
        'nup_browse': '찾아보기...',
        'nup_select_folder': '대상 폴더 선택',
        'nup_create': '만들기',
        'nup_start': 'N-Up 시작...',
        'nup_progress': 'N-Up 생성 중...',
        'nup_success': 'N-Up 생성 성공!\n\n다음으로 저장됨:\n{0}\n\n새 PDF를 열겠습니까?',
        'nup_complete': 'N-Up 완료',
        'nup_cancel': 'N-Up 취소됨',
        'nup_error_format': 'N-Up 중 오류 발생:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': '페이지 크기 변경',
        'pagesize_menu': '페이지 크기 변경',
        'pagesize_info': 'PDF의 페이지 크기를 변경합니다.\n\n콘텐츠가 자동으로 새 크기에 맞게 조정됩니다.',
        'pagesize_format': '형식:',
        'pagesize_select': '표준 형식 선택:',
        'pagesize_custom': '사용자 정의 크기:',
        'pagesize_width': '너비:',
        'pagesize_height': '높이:',
        'pagesize_orientation': '방향:',
        'pagesize_portrait': '세로',
        'pagesize_landscape': '가로',
        'pagesize_scale_options': '크기 조정 옵션:',
        'pagesize_fit': '맞춤 (종횡비 유지)',
        'pagesize_stretch': '늘리기 (왜곡)',
        'pagesize_center': '중앙 (원본 크기)',
        'pagesize_range': '페이지 범위:',
        'pagesize_all_pages': '모든 페이지',
        'pagesize_custom_range': '사용자 정의 범위',
        'pagesize_from': '시작:',
        'pagesize_to': '종료:',
        'pagesize_target_folder': '대상 폴더:',
        'pagesize_browse': '찾아보기...',
        'pagesize_select_folder': '대상 폴더 선택',
        'pagesize_apply': '적용',
        'pagesize_start': '페이지 크기 변경 시작...',
        'pagesize_progress': '페이지 크기 변경 중...',
        'pagesize_success': '페이지 크기 변경 성공!\n\n다음으로 저장됨:\n{0}\n\n새 PDF를 열겠습니까?',
        'pagesize_complete': '페이지 크기 변경 완료',
        'pagesize_cancel': '페이지 크기 변경 취소됨',
        'pagesize_error_format': '페이지 크기 변경 중 오류 발생:\n\n{0}',
        'pagesize_preview_info': '새 크기: {0} x {1} pt',
        'filename_pagesize_suffix': '_새크기',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF 정보',
        'pdf_info_menu': 'PDF 정보 표시',
        'pdf_info_voice': 'PDF 정보 표시 중',
        'pdf_info_error': 'PDF 정보 표시 중 오류 발생:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "키보드 단축키 표시",
        "shortcuts_dialog_title": "키보드 단축키",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 파일</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF 열기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF 닫기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>다른 이름으로 저장...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>문서 보호</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>인쇄</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>즉시 인쇄 (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>응용 프로그램 종료</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 내보내기</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Pages로 내보내기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>DOCX로 내보내기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>TXT로 내보내기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>이미지로 내보내기 (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>이미지 추출</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ 문서 처리</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (여러 페이지)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A 변환 (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF 평탄화</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF 오버레이</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF 최적화</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ 편집</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>검색</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>북마크 추가</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>북마크 관리</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>다음 북마크</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>이전 북마크</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR 실행</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 페이지 관리</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>현재 페이지 회전</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>모든 페이지 회전</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>현재 페이지 정규화</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>모든 페이지 정규화</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>페이지 삭제</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>페이지 추출</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>페이지 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>페이지 이동</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDF 병합</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>페이지 크기 변경</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 삽입</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>텍스트 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>십자 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>서명 1 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>서명 2 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>이미지 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>사각형 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>타원 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>선 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>화살표 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>페이지 번호 삽입</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>텍스트 워터마크</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>이미지 워터마크</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ 편집 제한</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>편집 제한 (검정)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>편집 제한 (흰색)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>모든 편집 제한 적용</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ 고급</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF 자르기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>메타데이터 편집</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ 보기</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>다크/라이트 모드 전환</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>텍스트 창 표시</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>페이지 너비 (확대)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>두 페이지 (확대)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>개요 (확대)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ 설정</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>비밀번호 관리</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR 설정</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>서명 설정</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>파일명 형식</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>설정 내보내기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>설정 가져오기</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ 정보</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF 정보 표시</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>음성 출력 켜기/끄기</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>메뉴 바 포커스</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "새 버전 사용 가능",
        "update_available_message": "새 버전 <b>{0}</b>이(가) 있습니다.\n\n릴리스 페이지를 방문하여 업데이트를 다운로드하세요:\n{1}",
        "update_available_voice": "새 버전 {0}을(를) 사용할 수 있습니다. GitHub 페이지에서 업데이트를 다운로드하세요.",
        "update_open_release": "릴리스 페이지 열기",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "모든 번역 다운로드",
        "ask_download_all_translations": """독일어, 영어, 베트남어 외에도 {total_languages}개의 GUI 언어를 사용할 수 있습니다.\n\n제공 / 업데이트하시겠습니까?\n\n참고:\n필요하지 않은 언어는 나중에 디렉토리에서 수동으로 삭제할 수 있습니다:\n{translations_path}
        \n취소하시면 나중에 '도구 → 번역 업데이트' 메뉴를 통해 GUI 언어를 다운로드할 수 있습니다.""",
        "menu_update_translations": "번역 업데이트",
        "translations_updated": "번역이 업데이트되었습니다",
        "translations_update_success": "{}개의 번역이 성공적으로 업데이트되었습니다 ({}개 신규, {}개 업데이트).",
        "translations_update_error": "번역 업데이트 중 오류 발생",
        "translations_update_no_changes": "모든 번역이 이미 최신 상태입니다.",
        "translations_update_offline": "인터넷 연결이 없습니다. 번역을 업데이트할 수 없습니다.",
        "translations_update_in_progress": "번역이 백그라운드에서 업데이트 중입니다...",
        "translations_downloading": "번역 다운로드 중...",
        "translations_path_hint": "번역을 위한 사용자 디렉토리",
        "translations_update_not_available_title": "업데이트를 사용할 수 없음",
        "translations_update_not_available_message": """번역 업데이트는 설치된 버전에서만 사용할 수 있습니다.\n\n개발 모드에서는 번역이 이미 최신 상태입니다.""",
        "translations_update_no_internet_title": "인터넷 연결 없음",
        "translations_update_no_internet_message": """인터넷 연결을 설정할 수 없습니다.\n\nGitHub에서 번역을 다운로드할 수 없습니다.\n\n가능한 해결 방법:
        • 인터넷 연결을 확인하세요
        • 방화벽을 일시적으로 비활성화하세요
        • 나중에 다시 시도하세요
        \nGitHub에서 수동으로 번역을 다운로드할 수도 있습니다:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "업데이트가 이미 진행 중입니다",
        "btn_retry": "다시 시도",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "PDF Dark View에 오신 것을 환영합니다",
        "welcome_title_not_supported": "PDF Dark View에 오신 것을 환영합니다",
        "welcome_message": "PDF Dark View에 오신 것을 환영합니다!\n\n시스템 언어가 '{language}'(으)로 감지되었습니다.\n이 언어를 사용자 인터페이스에 사용하시겠습니까?\n\n'설정 → 언어'에서 언제든지 언어를 변경할 수 있습니다.",
        "welcome_message_language_not_available": "PDF Dark View에 오신 것을 환영합니다!\n\n시스템 언어가 '{language}'(으)로 감지되었습니다.\n이 언어는 아직 설치되지 않았습니다.\n\n지금 GitHub에서 {language} 번역을 다운로드하시겠습니까?\n\n(그러면 언어가 자동으로 사용자 인터페이스에 사용됩니다.)",
        "welcome_message_language_not_supported": "PDF Dark View에 오신 것을 환영합니다!\n\n시스템 언어가 '{language}'(으)로 감지되었습니다.\n안타깝게도 이 언어에 대한 번역이 아직 없습니다.\n\n사용자 인터페이스는 {fallback_language}(으)로 표시됩니다.\n\n'설정 → 언어'에서 언제든지 언어를 변경할 수 있습니다.\n원하시면 직접 귀하의 언어에 대한 번역을 기여하실 수 있습니다:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "예, 시스템 언어 사용",
        "welcome_keep_english": "아니요, 영어 유지",
        "welcome_download_language": "예, {language} 다운로드",

        # ============================================
        # 107. 최근 사용한 경로
        # ============================================

        'menu_recent': '최근 사용 항목',
        'menu_recent_dirs': '디렉터리...',
        'menu_recent_files': '파일...',
        'recent_manage': '관리...',
        'recent_enable_tracking': '최근 경로 저장 (개인정보 보호)',
        'recent_enable_info': '경로를 저장하지 않으려면 이 옵션을 비활성화하세요',
        'recent_tracking_disabled': '경로 추적이 비활성화됨',
        'recent_enabled': '활성화됨',
        'recent_disabled': '비활성화됨',
        'recent_tracking_status': '경로 추적 {0}',
        'recent_dialog_title': '최근 사용한 경로',
        'recent_tab_directories': '디렉터리',
        'recent_tab_files': '파일',
        'recent_dirs_instruction': '더블 클릭하여 디렉터리에서 파일 대화상자 열기',
        'recent_files_instruction': '더블 클릭하여 PDF 직접 열기',
        'recent_no_directories': '(저장된 디렉터리 없음)',
        'recent_no_files': '(저장된 파일 없음)',
        'recent_default_current': '⭐ 기본값: {0}',
        'recent_set_as_default': '⭐ 기본값으로 설정',
        'recent_default_set_title': '기본 디렉터리 설정됨',
        'recent_default_set_message': '디렉터리 "{0}"이(가) PDF 열기 기본값으로 설정되었습니다.',
        'recent_default_set_voice': '기본 디렉터리가 설정되었습니다',
        'recent_directory_not_found': '디렉터리를 찾을 수 없음',
        'recent_file_not_found': '파일을 찾을 수 없음',
        'recent_remove_selected': '제거',
        'recent_remove_title': '경로 제거',
        'recent_remove_confirm': '경로 "{0}"을(를) 목록에서 제거하시겠습니까?',
        'recent_path_removed': '경로가 제거되었습니다',
        'recent_clear_all': '모두 제거',
        'recent_clear_title': '모든 경로 제거',
        'recent_clear_confirm_type': '모든 {0}을(를) 삭제하시겠습니까?',
        'recent_cleared': '목록이 지워졌습니다',
        'recent_path_not_found_title': '경로를 찾을 수 없음',
        'recent_path_not_found_message': '경로 "{0}"이(가) 더 이상 존재하지 않습니다.',
        'recent_open_file': '파일 열기',
        'btn_open_recent': '열기',
        'recent_open_file_question': '"{0}"을(를) PDF로 여시겠습니까?',
        'recent_not_pdf': '선택한 파일은 PDF가 아닙니다.',
        'recent_more_entries': '더 보기...',
        'btn_remove': '제거',
        'btn_clear': '모두 지우기',
        'recent_context_open': '열기',
        'recent_context_reveal': 'Finder에서 보기',
        'recent_context_set_default': '⭐ 기본값으로 설정',
        'recent_context_open_terminal': '💻 터미널 열기',
        'recent_context_file_info': '파일 정보',
        'recent_context_open_with_default': '📄 기본 앱으로 열기',
        'recent_context_remove': '목록에서 제거',
        'recent_context_clear_all': '모두 제거',
        'recent_file_info_title': '파일 정보',
        'recent_file_info_name': '이름',
        'recent_file_info_path': '경로',
        'recent_file_info_size': '크기',
        'recent_file_info_modified': '수정일',
        'recent_file_info_pages': '페이지',
        'recent_error_reveal': 'Finder에서 여는 중 오류 발생',
        'recent_error_terminal': '터미널 여는 중 오류 발생',
        'recent_error_info': '파일 정보를 가져오는 중 오류 발생',
        'open_user_data_folder': '사용자 데이터 디렉터리 보기',

        # ============================================
        # 108. 짝수/홀수 페이지 삭제
        # ============================================
        "pages_delete_even": "모든 짝수 페이지 삭제",
        "pages_delete_odd":  "모든 홀수 페이지 삭제",
        "progress_even_pages": "짝수 페이지 삭제 중",
        "progress_odd_pages": "홀수 페이지 삭제 중",
        "progress_mark_delete_even": "{}개의 짝수 페이지가 삭제 대상으로 표시됨",
        "progress_mark_delete_odd":  "{}개의 홀수 페이지가 삭제 대상으로 표시됨",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "프로그램을 종료하는 중입니다",

    }
