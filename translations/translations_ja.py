
# ============================================
# translations_ja.py - 日本語辞書 (Nihongo -Japanisch)
# Vollständig sortiert nach Kategorien
# ============================================

def load_japanese_strings():
    """Lädt alle japanischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDFを開く",
        'btn_text_window': "OCRテキスト",
        'btn_first': "最初のページ",
        'btn_prev': "前のページ",
        'btn_next': "次のページ",
        'btn_last': "最後のページ",
        'btn_print': "印刷",
        'btn_darkmode_light': "ライトモード",
        'btn_darkmode_dark': "ダークモード",
        'btn_delete_pages': "ページを削除",
        'btn_extract_pages': "ページを抽出",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "キャンセル",
        'btn_save': "保存",
        'btn_close': "閉じる",
        'btn_delete': "削除",
        'btn_delete_all': "すべて削除",
        'btn_copy': "コピー",
        'btn_export': "エクスポート",
        'btn_show': "パスワードを表示",
        'btn_hide': "パスワードを隠す",
        'btn_authenticate': "認証",
        'btn_settings': "設定",
        'btn_protect': "保護",
        'btn_remove_password': "パスワードを削除",
        'btn_manage': "パスワード管理",
        'btn_retry': "再試行",
        'btn_select_all': "すべて選択",
        'btn_clear_selection': "選択をクリア",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "{0} / {1} ページ",
        'page_count': "/ {0}",
        'goto_page': "ページへ移動",
        'page_simple': "{0} ページ",
        'full_view_page': "ページ {0} 全画面表示",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "検索語を入力 + Enter",
        'search_results': "結果: {0} / {1}",
        'search_nav_hint': "Enter: 次の結果 (Shift+Enter: 前の結果)",
        'search_no_results': "結果なし",
        'search_error': "検索エラー",
        'search_active': "検索フィールドがアクティブになりました",
        'search_closed': "検索が終了しました",
        'search_position': "ページ {0} {1}",
        'search_pos_top': "最上部",
        'search_pos_upper': "上部",
        'search_pos_middle': "中央",
        'search_pos_lower': "下部",
        'search_pos_bottom': "最下部",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "テキスト認識が正常に完了しました！",
        'ocr_success_title': "OCR成功",
        'ocr_success_message': "文書が検索可能になりました。",
        'ocr_failed': "OCR失敗",
        'ocr_in_progress': "OCR実行中",
        'ocr_preparing': "PDFを準備中...",
        'ocr_analyzing': "PDFを分析中...",
        'ocr_optimizing': "画像最適化中...",
        'ocr_recognizing': "テキスト認識中...",
        'ocr_embedding': "テキスト埋め込み中...",
        'ocr_finalizing': "PDFを最終処理中...",
        'ocr_not_available': "OCRが利用できません",
        'ocr_install_message': "OCRツールが見つかりませんでした。\n\nインストールしてください:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCRが必要です",
        'ocr_question': "PDFに検索可能なテキストが含まれていません。\n{0} を有効にするためにOCRを実行しますか？",
        'ocr_perform': "OCRを実行",
        'ocr_later': "後で",
        'ocr_starting': "保証付きOCRを開始しています...",
        'ocr_success_voice': "OCR成功。PDFは検索可能になりました。",
        'ocr_partial_success': "OCRは実行されましたが、置換中に問題が発生しました。\n\n検索可能なバージョンは次の場所に保存されました:\n{0}\n\nエラー: {1}",
        'ocr_partial_title': "OCRが部分的に成功",
        'ocr_partial_voice': "OCR実行されましたが、置換に失敗しました。",
        'original_file': "元のファイル:",
        'old_size': "旧サイズ:    {0} バイト",
        'new_size': "新サイズ: {0} バイト",
        'size_change': "変更: {0}{1} バイト",
        'backup_created_file': "バックアップが作成されました:\n{0}",
        'backup_not_created': "バックアップは作成されませんでした (設定が無効)",
        'page_header': "=== ページ {0} ===\n{1}\n",
        'scanned_page_header': "=== ページ {0} (スキャン) ===\n[このページにはスキャンテキストのみ含まれています]\n[手動でOCRを実行してください]\n",
        'scanned_warning': "⚠️ スキャンテキスト - OCRが必要",
        'guaranteed_title': "検索可能なPDFが作成されました",
        'guaranteed_message': "<b>保証付き検索可能バージョンが作成されました！</b>\n\n自動OCRが失敗したため、代替の検索可能PDFが作成されました:\n\n{0}\n\n<b>このファイルには以下が含まれます:</b>\n• 抽出されたテキスト (存在する場合)\n• スキャンされたページの指示\n• 完全に検索可能",
        'guaranteed_voice': "保証付き検索可能PDFが作成されました。",
        'instruction_title': "OCR手順",
        'instruction_file': "元のファイル: {0}",
        'instruction_text': "自動テキスト認識 (OCR) が失敗しました。\n手動でOCRを実行してください:\n\n1. OCRmyPDF を使用 (コマンドライン):\n   ocrmypdf --force-ocr \"[ファイル]\" \"出力.pdf\"\n\n2. Adobe Acrobat を使用 (macOS/Windows):\n   • AcrobatでPDFを開く\n   • ツール > PDFを編集\n   • 'テキスト認識' を選択\n\n3. プレビューを使用 (macOS):\n   • プレビューでPDFを開く\n   • ファイル > 書き出す...\n   • Quartzフィルター: 'ファイルサイズを縮小'\n   • 'OCRを実行' を有効にする\n\n4. オンラインOCRサービス:\n   • smallpdf.com/jp/ocr-pdf\n   • ilovepdf.com/jp/ocr-pdf\n   • adobe.com/jp/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR手順が作成されました",
        'instruction_created_message': "詳細な手順が作成されました:\n\n{0}\n\n手動OCRの手順に従ってください。",
        'instruction_created_voice': "OCR手順が作成されました。",
        'ocr_impossible': "OCRが不可能です",
        'ocr_impossible_message': "OCRを実行できませんでした。\n\nOCRソフトウェアを使用して '{0}' を手動で処理してください。",
        'ocr_impossible_voice': "OCRが不可能です。手動で処理してください。",
        'emergency_title': "緊急OCR",
        'emergency_message': "緊急PDFが作成されました:\n\n{0}\n\nこのファイルをOCRで手動処理してください。",
        'emergency_voice': "緊急PDFが作成されました。手動でOCRを実行してください。",
        'critical_error': "重大なエラー",
        'critical_error_message': "OCRを開始できませんでした。\n\nプログラムを再起動し、OCRのインストールを確認してください。",
        'critical_error_voice': "重大なOCRエラー",
        'ocr_question_html': "<p>PDFに検索可能なテキストが含まれていません。<p>{0} を有効にするためにOCRを実行しますか？</p>",
        'ocr_question_voice': "OCRが必要です。PDFに検索可能なテキストが含まれていません。{0} を有効にするためにOCRを実行しますか？",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "PDFが読み込まれていません",
        'no_pdf_message': "PDFが読み込まれていません",
        'pdf_not_found': "PDFファイルが見つかりません",
        'file_size': "ファイルサイズ",
        'bytes': "バイト",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "バックアップが作成されました",
        'backup_disabled': "バックアップは無効です",
        'backup_activated': "バックアップ作成が有効になりました",
        'backup_deactivated': "バックアップ作成が無効になりました",
        'backup_status': "バックアップ: {0}",
        'backup_on': "✔ 有効",
        'backup_off': "✘ 無効",
        'close_pdf': "PDFを閉じています: {0}",
        'pdf_not_found_format': "PDFファイルが見つかりません: {0}",
        'error_pdf_load_format': "PDFの読み込み中にエラーが発生しました: {0}",
        'load_failed_format': "読み込みに失敗しました:\n{0}",
        'decrypted_suffix': "(復号済み)",
        'decryption_failed': "復号に失敗しました。",
        'decryption_error': "復号中にエラーが発生しました",
        'decryption_success': "復号に成功しました",
        'decryption_success_message': "PDFは復号され、次の場所に保存されました:\n\n{0}",
        'decryption_success_voice': "PDFは復号され保存されました。",
        'password_remove_error': "パスワードの削除中にエラーが発生しました",
        'save_unencrypted': "暗号化されていないPDFを名前を付けて保存",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "名前を付けて保存...",
        'save_copy': "コピーを保存",
        'save_success': "PDFが保存されました: {0}",
        'save_encrypted': "保護されたPDFが保存されました: {0}",
        'save_error': "PDFを保存できませんでした",
        'encryption_question': "PDFをパスワードで保護しますか？",
        'encryption_yes': "はい",
        'encryption_no': "いいえ",
        'encryption_cancel': "キャンセル",
        'save_cancel': "保存がキャンセルされました",
        'save_encrypted_voice': "ファイルは暗号化されて保存されました。",
        'save_success_voice': "PDFファイルは暗号化されずに保存されました。",
        'save_error_format': "PDFを保存できませんでした:\n{0}",
        'export_pages_success': "Pagesへのエクスポートに成功しました",
        'export_pages_error': "Pagesへのエクスポートに失敗しました",
        'export_pages_error_format': "Pagesへのエクスポートに失敗しました: {0}",
        'export_word_success': "Wordへのエクスポートに成功しました",
        'export_word_error': "Wordへのエクスポートに失敗しました",
        'export_word_error_format': "Wordへのエクスポートに失敗しました: {0}",
        'export_text_success': "テキストのエクスポートに成功しました",
        'export_text_error': "テキストのエクスポートに失敗しました",
        'export_text_error_format': "テキストのエクスポートに失敗しました: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "パスワードが必要です",
        'password_enter': "パスワードを入力してください",
        'password_confirm': "パスワードを確認",
        'password_new': "新しいパスワード",
        'password_current': "現在のパスワード",
        'password_save': "パスワードを保存 (暗号化)",
        'password_saved': "✓ このファイルのパスワードは保存されました",
        'password_wrong': "パスワードが間違っています",
        'password_mismatch': "パスワードが一致しません",
        'password_too_short': "パスワードが短すぎます",
        'password_min_length': "パスワードは少なくとも4文字必要です",
        'password_strength': "パスワードの強度",
        'password_strength_very_weak': "非常に弱い",
        'password_strength_weak': "弱い",
        'password_strength_medium': "中程度",
        'password_strength_strong': "強い",
        'password_strength_very_strong': "非常に強い",
        'password_char_count': "({0} 文字)",
        'password_match': "✓ 一致",
        'password_no_match': "✗ パスワードが一致しません",
        'password_show': "表示",
        'password_hide': "隠す",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "パスワード管理",
        'password_table_filename': "ファイル名",
        'password_table_password': "パスワード",
        'password_count': "{0} 件の保存済みパスワード",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "保存されたパスワードはありません",
        'password_copied': "{0} 個のパスワードをコピーしました",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "本当に '{0}' のパスワードを削除しますか？",
        'password_delete_multiple': "本当に選択した {0} 個のパスワードを削除しますか？",
        'password_delete_all_confirm': "本当にすべての保存済みパスワード ({0} 個) を削除しますか？",
        'password_deleted': "{0} 個のパスワードを削除しました",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "すべてのパスワードが削除されました",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "パスワード生成器",
        'generator_generated': "生成されたパスワード:",
        'generator_regenerate': "再生成",
        'generator_copy': "コピー",
        'generator_use': "使用",
        'generator_settings': "設定",
        'generator_length': "長さ:",
        'generator_group_every': "区切り文字",
        'generator_group_chars': "文字ごと。    区切り文字:",
        'generator_uppercase': "大文字 (A-Z)",
        'generator_lowercase': "小文字 (a-z)",
        'generator_digits': "数字 (0-9)",
        'generator_symbols': "記号 (!@#$%^&*)",
        'generator_exclude': "除外:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "マスターパスワードが必要です",
        'master_password_setup': "マスターパスワードを設定",
        'master_password_change': "マスターパスワードを変更",
        'master_password_enter': "マスターパスワードを入力してください",
        'master_password_choose': "強力なマスターパスワードを選択してください (少なくとも8文字)",
        'master_password_new': "新しいマスターパスワードを入力してください",
        'master_password_confirm': "パスワードを確認",
        'master_password_authenticate': "認証",
        'master_password_success': "マスターパスワードが正常に設定されました。",
        'master_password_changed': "マスターパスワードが正常に変更されました。",
        'master_password_removed': "マスターパスワードとすべてのパスワードが削除されました。",
        'master_password_remove': "マスターパスワードを削除",
        'master_password_remove_confirm': "本当にすべてのパスワードを削除しますか？\n\nこの操作は元に戻せません！",
        'master_password_export_before': "事前にバックアップをエクスポートしますか？",
        'master_password_export_delete': "エクスポートして削除",
        'master_password_delete_now': "今すぐ削除",
        'master_password_for_signatures': "署名を使用するには、マスターパスワードを設定する必要があります。\n\n今すぐマスターパスワードを設定しますか？",
        'master_password_for_private': "プライベートテキストブロックを使用するには、マスターパスワードを設定する必要があります。\n\n今すぐマスターパスワードを設定しますか？",
        'master_password_info': """
            <b>🔐 マスターパスワードなし:</b><br>
            • パスワードの表示、コピー、エクスポートはできません<br>
            • パスワードの削除は常に可能です (マスターパスワードがなくても)<br><br>

            <b>🔐 マスターパスワードあり:</b><br>
            • 認証後、すべての機能が利用可能になります<br>
            • パスワードはマスターパスワードで暗号化されます<br>
            • 最小長: 8文字<br>
            • SHA-256ハッシュによる安全な保存<br><br>

            <b>重要:</b><br>
            • マスターパスワードを紛失すると、パスワードは復元できません<br>
            • マスターパスワードを削除すると、すべてのパスワードが削除されます<br>
            • 削除前にエクスポートオプションがあります<br>
            • マスターパスワードはいつでも変更できます
        """,
        'signature_auth_disabled': "署名のパスワード要求を無効にする",
        'template_auth_disabled': "プライベートテキストブロックのパスワード要求を無効にする",
        'master_password_for_signatures_settings': "署名を使用するには、マスターパスワードを設定する必要があります。\n\n設定 → パスワード管理 に移動してください",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDFを保護",
        'protect_info': "ファイル '{0}' はパスワードで保護されます。",
        'protect_instruction': "希望するパスワードを2回入力して文書を保護するか、入力フィールドの右側にあるパスワード生成器を使用してください。",
        'protect_success': "PDFは正常に保護され、次の場所に保存されました:\n{0}\n\nパスワード: {1}\n\n保護されたPDFを今すぐ開きますか？",
        'protect_open': "はい",
        'protect_skip': "いいえ",
        'protect_error': "PDFの保護中にエラーが発生しました",
        'protect_open_title': "保護されたPDFを開く",
        'protect_question': "完了しました。保護されたPDFを今すぐ開きますか？はい または いいえ？",
        'password_cancel': "パスワードダイアログがキャンセルされました",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "ページを削除",
        'pages_extract': "ページを抽出",
        'pages_insert': "ページを挿入",
        'pages_move': "ページを移動",
        'pages_delete_options': "削除オプション",
        'pages_delete_empty': "すべての空白ページを削除",
        'pages_delete_current': "現在のページを削除",
        'pages_delete_range': "ページ範囲を削除",
        'pages_extract_options': "抽出オプション",
        'pages_extract_current': "現在のページを抽出",
        'pages_extract_range': "ページ範囲を抽出",
        'pages_insert_position': "挿入位置",
        'pages_insert_before': "ページの前に挿入:",
        'pages_insert_select': "PDFを選択",
        'pages_insert_none': "PDFが選択されていません",
        'pages_move_source': "移動するページ",
        'pages_move_from': "開始ページ:",
        'pages_move_to': "終了ページ:",
        'pages_move_target': "移動先",
        'pages_move_before': "ページの前に移動:",
        'pages_move_hint': "注意: 1ページ = 開始, {0} = 終了",
        'pages_range_invalid': "開始ページは終了ページ以下である必要があります。",
        'pages_position_invalid': "移動先が移動範囲内にあってはいけません。",
        'pages_no_pdf_selected': "PDFが選択されていません。",
        'pages_deleted': "{0} ページが削除されました。",
        'pages_extracted': "抽出しました: {0}\n保存先: {1}\nファイルサイズ: {2:.1f} KB",
        'pages_inserted': "{0} ページを挿入しました",
        'pages_moved': "{0} ページを移動しました。",
        'pages_deleted_none': "ページは削除されませんでした。",
        'pages_delete_progress': "ページを削除中...",
        'pages_deleted_with_backup': "{0} ページが削除されました。\n\nバックアップ: {1}",
        'pages_deleted_voice': "バックアップが作成され、{0} ページが削除されました。",
        'info': "情報",
        'error_dialog_creation': "ダイアログを作成できませんでした",
        'extract_page_single': "ページ {0} を抽出",
        'extract_page_range': "ページ {0}-{1} を抽出",
        'extract_success_voice': "ページが正常に抽出されました",
        'extract_error_format': "抽出中にエラーが発生しました: {0}",
        'pages_inserted_voice': "{0} ページが挿入されました。",
        'insert_error_format': "挿入中にエラーが発生しました: {0}",
        'pages_move_progress': "ページを移動中...",
        'pages_moved_with_backup': "{0} ページが移動されました。\n\nバックアップ: {1}",
        'move_success_title': "移動成功",
        'pages_moved_voice': "{0} ページが正常に移動されました",
        'mark_removed': "ページ {0} のマークが解除されました",
        'mark_empty': "ページ {0} が空白としてマークされました",
        'mark_export_removed': "ページ {0} のエクスポートマークが解除されました",
        'mark_export': "ページ {0} がエクスポート用にマークされました",
        'no_empty_pages': "削除する空白ページはマークされていません",
        'delete_empty_confirm': "マークされた {0} 個の空白ページをすべて削除しますか？",
        'delete_empty_confirm_voice': "マークされた {0} 個の空白ページを今すぐ削除しますか？はい または いいえ。",
        'empty_pages_deleted': "{0} 個の空白ページを削除しました",
        'no_export_pages': "エクスポート用にマークされたページはありません",
        'overwrite_title': "既存のファイルを上書き",
        'overwrite_question': "ファイル\n\n{0}\n\nは既に存在します。\n上書きしますか？",
        'overwrite_voice': "既存のファイルを上書きしますか？はい または いいえ。",
        'page_skipped': "ページ {0} はスキップされました",
        'export_complete': "エクスポートが完了しました。",
        'export_complete_voice': "エクスポートが完了しました。",
        'no_pages_exported': "ページはエクスポートされませんでした",
        'export_cancelled': "エクスポートがキャンセルされました",
        'pages_exported': "{0} ページが {1} にエクスポートされました",
        'export_page_title': "ページをエクスポート",
        'page_exported': "ページ {0} が {1} にエクスポートされました",
        'export_error': "エクスポート中にエラーが発生しました",
        'export_marked_title': "マークされたページをエクスポート",
        'rotate_all_title': "すべてのページを回転",
        'rotate_all_question': "すべてのページを右に90度回転しますか？",
        'rotate_all_voice': "すべてのページを右に90度回転しますか？はい または いいえ？",
        'all_pages_rotated': "すべてのページが回転されました",
        'page_rotated': "ページ {0} が回転されました",
        'rotate_error': "ページを回転できませんでした",
        'delete_page_confirm': "ページ {0} を削除しますか？",
        'delete_page_confirm_voice': "本当にページ {0} を削除しますか？はい または いいえ。",
        'page_deleted': "ページ {0} が削除されました",
        'delete_error': "ページを削除できませんでした",
        'pages_deleted_voice': "{0} ページが削除されました",
        'pages_exported_split': "{0} ページが正常にエクスポートされました。",
        'pages_skipped': "{0} ページがスキップされました。",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "ページを抽出 (詳細)",
        'pdf_splitter_title': "PDF分割・抽出ツール",
        'pdf_splitter_load': " PDFファイルを選択",
        'pdf_splitter_info': "PDF文書のオプションを選択してください",
        'pdf_splitter_basic': "基本操作",
        'pdf_splitter_single': "個々のページに分割",
        'pdf_splitter_range': "ページを抽出:",
        'pdf_splitter_range_placeholder': "例: 1-3,5,7-9",
        'pdf_splitter_clean': "クリーンアップ操作",
        'pdf_splitter_remove_empty': "すべての空白ページを削除",
        'pdf_splitter_remove': "ページ範囲を削除:",
        'pdf_splitter_remove_placeholder': "例: 2,4-6",
        'pdf_splitter_process': "PDFを処理",
        'pdf_splitter_loaded': "PDFが読み込まれました。オプションを選択してください",
        'pdf_read_error': "PDFを読み込めませんでした",
        'pages': "ページ",
        'pages_created': "ページが作成されました",
        'range_empty': "ページ範囲を入力してください",
        'range_invalid': "無効なページ範囲です",
        'range_created': "選択したページで新しいPDFが作成されました:\n{0}",
        'empty_removed': "{0} 個の空白ページが削除されました。\n出力: {1}",
        'remove_empty': "削除するページを入力してください",
        'remove_invalid': "削除するページが無効です",
        'remove_done': "クリーンアップされたPDFが作成されました:\n{0}",
        'open_folder': "フォルダを開く",
        'show_in_finder': "Finderに表示",
        'pdf_splitter_no_pdf': "最初にPDFファイルを読み込んでください。",
        'process_error': "PDFの処理中にエラーが発生しました",
        'pages_created_voice': "{0} ページが作成されました",
        'range_created_voice': "選択したページでPDFが作成されました",
        'empty_removed_voice': "{0} 個の空白ページが削除されました",
        'remove_done_voice': "クリーンアップされたPDFが作成されました",
        'pdf_splitter_split_groups': "連続する各グループを別ファイルに",
        'range_created_single': "新しいPDFが作成されました:\n{0}",
        'range_created_multiple': "{0} 個のPDFファイルが作成されました。",
        'range_created_voice_single': "選択したページで1つのPDFが作成されました",
        'range_created_voice_multiple': "{0} 個のPDFファイルが作成されました",
        'empty_removed_none_left': "残りのページはありません",
        'empty_removed_all_empty': "すべてのページが空白として認識され、削除されます。ファイルは作成されませんでした。",
        'preview_single': "プレビュー: {0}",
        'preview_enter_range': "ページ範囲を入力してください。",
        'preview_invalid_range': "無効なページ範囲です。",
        'preview_file': "プレビュー: {0}",
        'preview_files': "プレビュー: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "印刷を開始します",
        'print_sent': "印刷ジョブが送信されました",
        'print_now': "すぐに印刷",
        'print_error': "すぐに印刷中にエラーが発生しました",
        'print_limited': "このシステムでは印刷機能が制限されています",
        'print_error_format': "すぐに印刷中にエラーが発生しました: {0}",
        'warning': "警告",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "ライトモードに切り替え",
        'mode_switch_to_dark': "ダークモードに切り替え",
        'mode_dark_activated': "ダークモードがアクティブになりました",
        'mode_light_activated': "ライトモードがアクティブになりました",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "全画面表示",
        'zoom_two_pages': "2ページ見開き",
        'zoom_overview': "概要モード",
        'zoom_cannot_during_search': "検索中はズームできません",
        'zoom_exit_first': "先にズームを終了してください",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "ドラッグ＆ドロップが有効です",
        'drag_disabled': "ドラッグ＆ドロップが無効です",
        'drag_page_grab': "ページ {0} をつかみました",
        'drag_page_dropped': "ページ {0} を位置 {1} に挿入しました",
        'drag_position_invalid': "無効な位置です",
        'drag_same_position': "ページ {0} は位置 {0} に留まります",
        'drag_error': "移動中にエラーが発生しました",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "高度な書式設定とテキストブロック管理によるテキスト入力",
        'text_templates': "利用可能なテキストブロック:",
        'text_name': "名前",
        'text_preview': "テキストプレビュー",
        'text_enter': "テキスト:",
        'text_font_size': "フォントサイズ:",
        'text_formatting': "書式設定:",
        'text_bold': "太字",
        'text_italic': "斜体",
        'text_underline': "下線",
        'text_alignment': "配置:",
        'text_left': "左揃え",
        'text_center': "中央揃え",
        'text_right': "右揃え",
        'text_color': "テキストの色:",
        'text_opacity': "不透明度:",
        'text_word_wrap': "ワードラップ:",
        'text_auto': "自動",
        'text_page_width_95': "ページ幅 (95%)",
        'text_page_width_85': "非常に広い (85%)",
        'text_page_width_75': "より広い (75%)",
        'text_page_width_60': "広い (60%)",
        'text_page_width_50': "中程度 (50%)",
        'text_page_width_30': "狭い (30%)",
        'text_page_width_20': "より狭い (20%)",
        'text_page_width_10': "非常に狭い (10%)",
        'text_no_wrap': "折り返さない",
        'text_private': "プライベートテキストブロック (認証が必要)",
        'text_preview_label': "プレビュー:",
        'text_preview_placeholder': "ここにテキストのプレビューが表示されます...",
        'text_no_text': "(テキストなし)",
        'text_save_template': "💾 ブロックとして保存",
        'text_delete_template': "🗑 選択したテキストブロックを削除",
        'text_show_private': "プライベートを表示",
        'text_hide_private': "プライベートを隠す",
        'text_use': "✅ テキストを使用",
        'text_saved': "テキストブロックが次の名前で保存されました:\n{0}",
        'text_saved_voice': "テキストブロックが保存されました",
        'text_deleted': "テキストブロックが削除されました",
        'text_no_text_to_save': "保存するテキストがありません。",
        'text_no_templates': "テキストブロックが見つかりません",
        'text_private_master_required': "プライベートブロックは、マスターパスワードが設定されている場合のみ使用できます。\n\n今すぐマスターパスワードを設定しますか？",
        'text_filename': "テキストブロックのファイル名 ('Text_' と '.txt' を除く):",
        'text_filename_hint': "例: '電話 ホームオフィス' は 'Text_電話 ホームオフィス.txt' として保存されます",
        'text_save_hint': "テキストブロックは書式設定と共に自動的に保存されます。",
        'text_guide_title': "テキスト入力 – ガイド",
        'text_delete_confirm': "本当にこのテキストブロックを削除しますか？\n\nファイル: {0}\nテキスト: {1}...",
        'text_make_public': "公開としてマーク",
        'text_make_private': "プライベートとしてマーク",
        'text_privacy_changed': "プライバシーステータスが変更されました",
        'text_private_always': "プライベートは常に表示 (設定)",
        'text_mode_required': "まずテキストモードを有効にしてください",
        'text_continue_editing': "編集を続行 – カーソルはテキストの最後にあります",
        'text_no_input': "テキストが入力されていません – テキストは破棄されました",
        'save_dialog_question': "どのように続行しますか？",
        'text_save_question': "すべてのテキストと十字を保存、調整、編集を続ける、または破棄しますか？",
        'copy_cross': "十字をコピーしました",
        'paste_cross': "十字を貼り付けました",
        'paste_text': "テキストを貼り付けました",
        'cross_discarded': "十字を破棄しました",
        'all_discarded': "すべて破棄しました",
        'text_discarded': "テキストを破棄しました",
        'no_texts_to_save': "保存するテキストがありません",
        'no_valid_texts': "有効なテキストがありません",
        'text_word_singular': "テキスト",
        'text_word_plural': "テキスト",
        'cross_word_singular': "十字",
        'cross_word_plural': "十字",
        'texts_saved_title': "テキストが保存されました",
        'texts_crosses_saved': "{0} 件の {1} と {2} 件の {3} がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'texts_crosses_saved_voice': "{0} 件の {1} と {2} 件の {3} が保存されました。",
        'texts_saved': "{0} 件の {1} がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'texts_saved_voice': "{0} 件の {1} が保存されました。",
        'crosses_saved': "{0} 件の {1} がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'crosses_saved_voice': "{0} 件の {1} が保存されました。",
        'elements_saved': "{0} 個の要素がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'elements_saved_voice': "{0} 個の要素が保存されました。",
        'text_window_load_error': "テキストウィンドウを読み込めませんでした",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **テキスト入力とテキストブロック – 詳細ガイド**

        **1. テキストの挿入と編集**
        - ドキュメント内の目的の場所を右クリックし、「テキストを挿入」を選択します。
        - ダイアログが開き、テキストを入力して書式設定できます:
        • フォントサイズ、太字、斜体、下線
        • テキストの色 (自由選択)
        • 透明度 (不透明度) スライダー
        • ワードラップ (さまざまな幅、例: ページ幅、狭い、折り返さない)
        - 確認後、テキストがクリックした場所に表示されます。マウスまたは矢印キーで移動できます。
        - テキストをダブルクリックすると編集モードが開きます。ESCで終了します。

        **2. テキストブロック (テンプレート) の管理**
        - テキストダイアログの左側に、保存されたすべてのテキストブロックのリストが表示されます。
        - **ブロックの保存:** テキストを入力し、書式設定して、「💾 ブロックとして保存」をクリックします。ファイル名を入力します (拡張子なし)。
        - **ブロックの読み込み:** リスト内の目的の名前をクリックします。テキストと書式設定が読み込まれ、必要に応じて調整できます。
        - **削除:** ブロックを右クリックして削除するか、プライバシーステータスを変更します。

        **3. プライベートテキストブロック (マスターパスワード)**
        - マスターパスワードを設定している場合 (設定 → パスワード管理)、ブロックを「プライベート」としてマークできます。
        - 保存前にダイアログで「プライベートテキストブロック」チェックボックスをオンにします。
        - プライベートブロックは、セッションごとに1回マスターパスワードを入力した場合のみリストに表示されます (鍵アイコンまたは最初のアクセス時の認証)。
        - これにより、機密性の高いテキストブロックを不正アクセスから保護できます。

        **4. 十字の挿入**
        - コンテキストメニューから、グラフィック十字 (例: チェックボックス用) を挿入することもできます。
        - 十字のサイズ、線幅、色は、設定でグローバルに調整できます (メニュー「設定」→「十字の設定」)。
        - 既存の十字を右クリックして個別に変更できます。

        **5. 一括操作**
        - 1ページに複数のテキストまたは十字を配置した場合、コンテキストメニュー (テキストモードで右クリック) からすべてを一度に保存または破棄できます。
        - 保存すると、すべての要素がPDFに埋め込まれ、ベクターグラフィックとして残ります。

        **6. テキストモードでのキーボードショートカット**
        - 矢印キー: 要素の移動
        - Ctrl+矢印キー: より大きなステップ
        - Enter: 保存ダイアログを開く (すべて保存 / 調整 / 破棄)
        - ESC: 現在の要素を破棄
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 テキスト入力とテキストブロック – 詳細ガイド</strong></p>

        <p><strong>1. テキストの挿入と編集</strong></p>
        <ul>
        <li>ドキュメント内の目的の場所を右クリックし、「テキストを挿入」を選択します。</li>
        <li>ダイアログが開き、テキストを入力して書式設定できます:<br/>
        • フォントサイズ、太字、斜体、下線<br/>
        • テキストの色 (自由選択)<br/>
        • 透明度 (不透明度) スライダー<br/>
        • ワードラップ (さまざまな幅、例: ページ幅、狭い、折り返さない)</li>
        <li>確認後、テキストがクリックした場所に表示されます。マウスまたは矢印キーで移動できます。</li>
        <li>テキストをダブルクリックすると編集モードが開きます。ESCで終了します。</li>
        </ul>

        <p><strong>2. テキストブロック (テンプレート) の管理</strong></p>
        <ul>
        <li>テキストダイアログの左側に、保存されたすべてのテキストブロックのリストが表示されます。</li>
        <li><strong>ブロックの保存:</strong> テキストを入力し、書式設定して、「💾 ブロックとして保存」をクリックします。ファイル名を入力します (拡張子なし)。</li>
        <li><strong>ブロックの読み込み:</strong> リスト内の目的の名前をクリックします。テキストと書式設定が読み込まれ、必要に応じて調整できます。</li>
        <li><strong>削除:</strong> ブロックを右クリックして削除するか、プライバシーステータスを変更します。</li>
        </ul>

        <p><strong>3. プライベートテキストブロック (マスターパスワード)</strong></p>
        <ul>
        <li>マスターパスワードを設定している場合 (設定 → パスワード管理)、ブロックを「プライベート」としてマークできます。</li>
        <li>保存前にダイアログで「プライベートテキストブロック」チェックボックスをオンにします。</li>
        <li>プライベートブロックは、セッションごとに1回マスターパスワードを入力した場合のみリストに表示されます (鍵アイコンまたは最初のアクセス時の認証)。</li>
        <li>これにより、機密性の高いテキストブロックを不正アクセスから保護できます。</li>
        </ul>

        <p><strong>4. 十字の挿入</strong></p>
        <ul>
        <li>コンテキストメニューから、グラフィック十字 (例: チェックボックス用) を挿入することもできます。</li>
        <li>十字のサイズ、線幅、色は、設定でグローバルに調整できます (メニュー「設定」→「十字の設定」)。</li>
        <li>既存の十字を右クリックして個別に変更できます。</li>
        </ul>

        <p><strong>5. 一括操作</strong></p>
        <ul>
        <li>1ページに複数のテキストまたは十字を配置した場合、コンテキストメニュー (テキストモードで右クリック) からすべてを一度に保存または破棄できます。</li>
        <li>保存すると、すべての要素がPDFに埋め込まれ、ベクターグラフィックとして残ります。</li>
        </ul>

        <p><strong>6. テキストモードでのキーボードショートカット</strong></p>
        <ul>
        <li>矢印キー: 要素の移動</li>
        <li>Ctrl+矢印キー: より大きなステップ</li>
        <li>Enter: 保存ダイアログを開く (すべて保存 / 調整 / 破棄)</li>
        <li>ESC: 現在の要素を破棄</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "十字の設定",
        'cross_properties': "十字のプロパティ",
        'cross_size': "サイズ (px):",
        'cross_line_width': "線の太さ:",
        'cross_color': "色:",
        'cross_choose_color': "選択",
        'cross_fine_tuning': "保存時の微調整 (ピクセル)",
        'cross_offset_x': "Xオフセット:",
        'cross_offset_y': "Yオフセット:",
        'cross_offset_x_tooltip': "負の値は保存時に十字を左に移動、正の値は右に移動",
        'cross_offset_y_tooltip': "負の値は保存時に十字を上に移動、正の値は下に移動",
        'cross_preview': "プレビュー",
        'cross_save': "設定を適用",
        'cross_customized': "十字が調整されました",
        'cross_settings_applied': "十字の設定が保存されました。\nサイズ: {0}px、線の太さ: {1}px\n{2}",
        'cross_updated_count': "{0} 個の既存の十字が更新されました。",
        'cross_no_crosses': "既存の十字は見つかりませんでした。",
        'cross_settings_applied_all': "十字の設定がすべての {0} 個の十字に適用されました",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "署名の設定",
        'signature_1': "署名1",
        'signature_2': "署名2",
        'signature_select': "署名を選択",
        'signature_add': "➕ 新しい署名を追加...",
        'signature_size': "署名 {0} のサイズ (%):",
        'signature_common': "共通設定",
        'signature_timestamp': "タイムスタンプを自動追加",
        'signature_location': "デフォルトの場所:",
        'signature_timestamp_size': "タイムスタンプのフォントサイズ:",
        'signature_no_files': "-- 署名が見つかりません --",
        'signature_insert': "署名を挿入",
        'signature_insert_1': "署名1を挿入",
        'signature_insert_2': "署名2を挿入",
        'signature_customize': " 署名を調整",
        'signature_discard': " この署名を破棄",
        'signature_save_all': " すべての署名を保存",
        'signature_discard_all': " すべての署名を破棄",
        'signature_guide_title': "署名 – ガイド",
        'signature_guide': """
📝 署名 – クイックガイド

- マスターパスワードを設定します
- 設定メニューで署名を構成します
  (サイズ、タイムスタンプ ...)
- 目的の場所で右クリックして挿入します
  (マスターパスワードはセッションごとに1回必要)
- マウスまたは矢印キーで署名を移動します
- 複数の署名を次々に挿入できます
- 各署名は個別に調整できます
- 単一の署名を破棄
- すべての署名を一度に保存/破棄
- メニューバーも使用できます。
        """,
        'signature_placeholder': "プレビューは利用できません",
        'signature_info': "署名 {0}: {1}×{2} ピクセル ({3}% of {4}×{5})",
        'signature_info_placeholder': "署名 {0} の設定",
        'signature_inserted': "署名 {0} がページ {1} に挿入されました",
        'signature_deleted': "署名が削除されました",
        'signature_copied': "署名がコピーされました",
        'signature_pasted': "署名 {0} が貼り付けられました",
        'signature_saved': "{0} 個の署名がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'signature_saved_voice': "{0} 個の署名が保存されました",
        'mode_replace_signature_format': "モードを終了して署名 {0} を挿入",
        'mode_conflict_voice_signature': "モード {0} がアクティブです。終了して署名を挿入しますか？",
        'signature_not_configured': "署名 {0} は構成されていません",
        'signature_file_not_found': "署名ファイルが見つかりません",
        'timestamp_format': "{0}、{1}",
        'no_copied_signature': "コピーされた署名はありません",
        'no_signatures_to_save': "保存する署名はありません",
        'signature_save_question': "すべての署名を保存、調整、またはこれを破棄しますか？",
        'signatures_saved_title': "署名が保存されました",
        'signatures_saved': "{0} 個の署名がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'signatures_saved_voice': "{0} 個の署名が保存されました。",
        'all_signatures_discarded': "すべての署名が破棄されました",
        'signature_settings_saved': "署名の設定が保存されました",
        'signature_cancelled': "署名が破棄されました",
        'signature_active_title': "署名がアクティブです",
        'signature_replace_question': "既にアクティブな署名があります。\n\n現在の署名を置き換えますか？",
        'signature_replace': "署名を置き換え",
        'signature_replace_voice': "現在の署名を置き換えるか、キャンセルしますか？",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "画像の設定",
        'image_common': "画像の共通設定",
        'image_keep_aspect': "ドラッグ時にアスペクト比を維持",
        'image_default_size': "デフォルトサイズ (%):",
        'image_dark_invert': "ダークモードで画像を反転",
        'image_dark_invert_tooltip': "有効: 視認性を高めるため画像が反転されます",
        'image_fine_tuning': "微調整 (ピクセル)",
        'image_offset_x': "Xオフセット:",
        'image_offset_y': "Yオフセット:",
        'image_offset_x_tooltip': "負の値は保存時に画像を左に移動、正の値は右に移動",
        'image_offset_y_tooltip': "負の値は保存時に画像を上に移動、正の値は下に移動",
        'image_select': "画像を選択",
        'image_insert': "画像を挿入",
        'image_customize': " 画像を調整",
        'image_aspect': " アスペクト比を維持",
        'image_discard': " この画像を破棄",
        'image_save_all': " すべての画像を保存",
        'image_discard_all': " すべての画像を破棄",
        'image_filter': "画像",
        'image_guide_title': "画像の挿入 – ガイド",
        'image_guide': """
📷 PDFへの画像挿入 – クイックガイド:

1. 目的の場所を右クリック
2. 「画像を挿入」→ 画像を選択
3. 画像を配置: マウスでドラッグ
4. サイズを調整: 角/端をドラッグ
5. アスペクト比を維持: [A]キー
6. さらに調整: 画像を右クリック

ヒント: コンテキストメニューで設定を調整できます。
        """,
        'image_inserted': "画像がページ {1} に挿入されました",
        'image_deleted': "画像が破棄されました",
        'image_copied': "画像がコピーされました",
        'image_pasted': "画像が貼り付けられました",
        'image_saved': "{0} 個の画像がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'image_saved_voice': "{0} 個の画像が保存されました",
        'image_aspect_on': "有効",
        'image_aspect_off': "無効",
        'image_aspect_toggle': "アスペクト比を維持 {0}",
        'image_reset': "画像が元のサイズに戻りました",
        'image_replaced': "画像が置き換えられました",
        'image_invalid': "無効な画像です",
        'mode_replace_image': "画像を挿入",
        'mode_conflict_voice_image': "モード {0} がアクティブです。終了して画像を挿入しますか？",
        'image_active_title': "画像がアクティブです",
        'image_replace_question': "既にアクティブな画像があります。\n\n現在の画像を置き換えますか？",
        'image_replace': "画像を置き換え",
        'image_replace_voice': "現在の画像を置き換えるか、キャンセルしますか？",
        'image_filter_all': "画像 (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;すべてのファイル (*.*)",
        'no_copied_image': "コピーされた画像はありません",
        'image_discarded': "画像が破棄されました",
        'image_save_question': "すべての画像を保存、調整、またはこれを破棄しますか？",
        'no_images_to_save': "保存する画像はありません",
        'no_valid_images': "有効な画像はありません",
        'images_saved_title': "画像が保存されました",
        'images_saved': "{0} 個の画像がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'images_saved_voice': "{0} 個の画像が保存されました。",
        'all_images_discarded': "すべての画像が破棄されました",
        'image_settings_updated': "画像の設定が更新されました",
        'image_replace_title': "新しい画像を選択",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "図形の設定",
        'form_basic': "基本設定",
        'form_default_type': "デフォルトの図形タイプ:",
        'form_rectangle': "長方形",
        'form_ellipse': "楕円",
        'form_line': "直線",
        'form_arrow': "矢印",
        'form_line_width': "線の太さ:",
        'form_colors': "色",
        'form_line_color': "線の色:",
        'form_fill_color': "塗りつぶしの色:",
        'form_choose_color': "選択",
        'form_transparent': "透明な背景 (線のみ)",
        'form_filled': "塗りつぶし",
        'form_dark_mode': "ダークモード",
        'form_dark_invert': "ダークモードで色を反転",
        'form_fine_tuning': "微調整 (ピクセル)",
        'form_offset_x': "Xオフセット:",
        'form_offset_y': "Yオフセット:",
        'form_offset_x_tooltip': "負の値は保存時に図形を左に移動、正の値は右に移動",
        'form_offset_y_tooltip': "負の値は保存時に図形を上に移動、正の値は下に移動",
        'form_preview': "プレビュー",
        'form_insert': "図形を挿入",
        'form_rectangle_insert': "長方形",
        'form_ellipse_insert': "楕円/円",
        'form_line_insert': "直線 (2クリック)",
        'form_arrow_insert': "矢印 (2クリック)",
        'form_customize': " 図形を調整",
        'form_transparent_toggle': " 透明な背景",
        'form_discard': " この図形を破棄",
        'form_save_all': " すべての図形を保存",
        'form_discard_all': " すべての図形を破棄",
        'form_guide_title': "図形の挿入 – ガイド",
        'form_guide': """
📐 PDFへの図形挿入 – クイックガイド:

1. 図形タイプを選択 (長方形、楕円、直線、矢印)
2. 場所をクリック
   - 長方形/楕円: 1回のクリックで図形を配置
   - 直線/矢印: 2回クリックで開始点と終了点
3. 図形を配置: マウスでドラッグ
4. サイズを調整: 角/端をドラッグ
5. 図形を保存: Enter
6. 図形を破棄: ESC
7. さらに調整: 図形を右クリック

ヒント: コンテキストメニューで設定を調整できます。
        """,
        'form_inserted': "{0} がページ {1} に挿入されました",
        'form_deleted': "図形が削除されました",
        'form_copied': "図形がコピーされました",
        'form_pasted': "図形が貼り付けられました",
        'form_saved': "{0} 個の図形がPDFに挿入されました。\n\nPDFが再読み込みされました...",
        'form_saved_voice': "{0} 個の図形が保存されました",
        'form_reset': "図形がデフォルトサイズに戻りました",
        'form_transparent_on': "有効",
        'form_transparent_off': "無効",
        'form_transparent_toggled': "透明な背景 {0}",
        'form_line_cancel': "直線の描画がキャンセルされました",
        'form_second_click': "今すぐ {0} の終点をクリックしてください",
        'mode_replace_form': "図形を挿入",
        'mode_conflict_voice_form': "モード {0} がアクティブです。終了して図形を挿入しますか？",
        'form_settings_updated': "図形の設定が更新されました",
        'form_unknown': "図形",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. 開始点をクリック",
        'form_line_guide_2': "2. 終了点をクリック",
        'form_line_guide_3': "線は2点間に描画されます。",
        'form_line_status_1': "最初のクリックを待っています...",
        'form_line_status_2': "最初の点が設定されました: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "今すぐ終了点をクリックしてください...",
        'form_line_status_4': "両方の点が設定されました。\n保存するには「完了」をクリックしてください。",
        'form_line_reset': "リセット",
        'form_line_finish': "完了",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "コピー (Cmd+C)",
        'paste': "貼り付け (Cmd+V)",
        'copied': "コピーしました: {0}",
        'no_element_to_copy': "コピーする要素が選択されていません",
        'no_copied_data': "コピーされたデータはありません",
        'no_valid_position': "貼り付けに有効な位置がありません",
        'copy_text': "テキストをコピーしました",
        'copy_image': "画像をコピーしました",
        'copy_form': "図形をコピーしました",
        'copy_signature': "署名をコピーしました",
        'element_text': "テキスト",
        'element_image': "画像",
        'element_form': "図形",
        'element_signature': "署名",
        'element_unknown': "要素",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "モードの競合",
        'mode_conflict_message': "モード '{0}' は既にアクティブです。\n\n終了して {1} しますか？",
        'mode_replace': "モードを終了して {0}",
        'mode_cancel': "キャンセル",
        'mode_replace_text': "テキストを挿入",
        'mode_replace_cross': "十字を挿入",
        'mode_replace_signature': "署名を挿入",
        'mode_replace_image': "画像を挿入",
        'mode_replace_form': "図形を挿入",
        'mode_conflict_voice': "モード {0} がアクティブです。終了してテキストを挿入しますか？",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "テキスト入力",
        'active_mode_signature': "署名",
        'active_mode_image': "画像",
        'active_mode_form': "図形",
        'active_mode_and': " と ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "挿入",
        'insert_another_text': "テキストを挿入",
        'insert_another_cross': "十字を挿入",
        'insert_another_signature_1': "署名1",
        'insert_another_signature_2': "署名2",
        'insert_another_image': "画像を挿入",
        'insert_another_form_rect': "長方形",
        'insert_another_form_ellipse': "楕円",
        'insert_another_form_line': "直線 (2クリック)",
        'insert_another_form_arrow': "矢印 (2クリック)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} を保存",
        'save_dialog_message': "{0} はページ {1} に保存されます。\n\nどのように続行しますか？",
        'save_all': "すべての {0} を保存",
        'save_single': "{0} を保存",
        'save_customize': "{0} を調整",
        'save_discard': "この {0} を破棄",
        'save_continue': "編集を続行",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " ページ {0} へ移動",
        'context_rotate': " ページ {0} を回転",
        'context_delete': " ページ {0} を削除",
        'context_export': " ページ {0} をエクスポート",
        'context_mark_as': " ページをマーク...",
        'context_mark_empty': " 空白ページ",
        'context_unmark_empty': " 空白解除",
        'context_mark_export': " エクスポート用にマーク",
        'context_unmark_export': " エクスポートマーク解除",
        'context_batch_actions': " 一括操作",
        'context_batch_delete_empty': " すべての空白ページ ({0} ページ) を削除",
        'context_batch_export_single': " すべてのページ ({0} ページ) をエクスポート (1ファイル)",
        'context_batch_export_split': " すべてのページ ({0} ページ) をエクスポート (個別ファイル)",
        'context_drag_start': " ドラッグ＆ドロップを開始",
        'context_drag_stop': " ドラッグ＆ドロップを終了",
        'context_insert': " 挿入",
        'context_insert_pages': " ページを挿入",
        'context_zoom': "ズーム",
        'discard_mixed': "{0} 件の {1} と {2} 件の {3} を破棄",
        'save_mixed': "{0} 件の {1} と {2} 件の {3} を保存",
        'discard_texts': "{0} 件のテキストを破棄",
        'discard_text_single': "1件のテキストを破棄",
        'save_texts': "{0} 件のテキストを保存",
        'save_text_single': "1件のテキストを保存",
        'discard_crosses': "{0} 個の十字を破棄",
        'discard_cross_single': "1個の十字を破棄",
        'save_crosses': "{0} 個の十字を保存",
        'save_cross_single': "1個の十字を保存",
        'discard_signatures': "{0} 個の署名を破棄",
        'save_signature_single': "1個の署名を保存",
        'save_signatures': "{0} 個の署名を保存",
        'discard_images': "{0} 個の画像を破棄",
        'save_image_single': "1個の画像を保存",
        'save_images': "{0} 個の画像を保存",
        'discard_forms': "{0} 個の図形を破棄",
        'save_form_single': "1個の図形を保存",
        'save_forms': "{0} 個の図形を保存",
        'cross_discard': "この十字を破棄",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 エクスポート/インポート情報",
        'export_what': "📋 エクスポートされるもの:",
        'export_general': "一般設定",
        'export_general_items': "• 音声出力 (オン/オフ、速度)\n• ダーク/ライトモード\n• バックアップ設定\n• OCR設定",
        'export_image_form': "画像・図形設定",
        'export_image_form_items': "• 画像設定 (アスペクト比、デフォルトサイズ)\n• 図形設定 (線の太さ、色)\n• 署名設定 (パス、サイズ、タイムスタンプ)",
        'export_passwords': "パスワードデータベース",
        'export_passwords_items': "• 保存されたすべてのPDFパスワード\n• 暗号化または復号化を選択可能",
        'export_master': "マスターパスワード設定",
        'export_master_items': "• マスターパスワードのハッシュ\n• 署名/テキストブロックの設定",
        'export_signatures': "署名とテキストブロック",
        'export_signatures_items': "• すべての画像ファイル (署名)\n• すべてのテキストブロック (書式設定付き)\n• プライベート/パブリックのマーク",
        'export_import_warning': "⚠️ 重要な注意事項",
        'export_import_note': "• インポート時、現在のすべての設定が上書きされます\n• アプリケーションの再起動が必要です\n• 既存の署名/テキストブロックは置き換えられます",
        'export_master_note': "• マスターパスワードが設定されている場合、選択できます:\n  - 復号化 (パスワードが平文で)\n  - 暗号化 (マスターパスワードでのみ読み取り可能)",
        'export_security': "• エクスポートされたZIPファイルには機密データが含まれています\n• 安全な場所に保管してください (例: 暗号化USBメモリ)\n• ファイルを紛失すると、パスワードは永久に失われます",
        'export_format': "📁 エクスポート形式",
        'export_format_desc': "設定は1つのZIPファイルに保存されます:",
        'export_filename': "PDFDarkView_設定_YYYYMMDD_HHMMSS.zip",
        'export_success': "設定が正常にエクスポートされました",
        'export_failed': "エクスポートに失敗しました",
        'export_import_question': "今すぐアプリケーションを再起動しますか？",
        'export_password_question': "マスターパスワードが設定されています。\n\nパスワードを復号化してエクスポートしますか？\n(そうしないと暗号化されたままエクスポートされます)",
        'export_decrypt': "復号化してエクスポート",
        'export_encrypt': "暗号化してエクスポート",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " 情報",
        'info_title': "PDF Dark View について",
        'info_version': "バージョン",
        'info_author': "開発者: Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "概要",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> は、視覚障害者のために特別に開発された、アクセシブルなPDFビューアです。</p>

            <p><strong>主な機能:</strong></p>
            <ul>
                <li>コントラストが高く、カスタマイズ可能なインターフェース</li>
                <li>完全なキーボード操作</li>
                <li>統合された音声出力</li>
                <li>スキャン文書用のOCR</li>
                <li>充実した編集ツール</li>
            </ul>

            <p>50以上の言語に対応 – 誰もがPDFにアクセスできるように。</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "機能",
        'info_features_intro': "PDF Dark View は以下の機能を提供します:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>表示とナビゲーション</strong> – ダーク/ライトモード、ページ送り、ズーム、ページへジャンプ</li>
            <li><strong>OCR (テキスト認識)</strong> – スキャン文書を検索可能・コピー可能にする</li>
            <li><strong>編集</strong> – テキスト、クロス、署名、画像、図形の挿入</li>
            <li><strong>ページ管理</strong> – 削除、抽出、挿入、ドラッグ＆ドロップで移動</li>
            <li><strong>エクスポート</strong> – Word、Pages、またはテキストとして</li>
            <li><strong>セキュリティ</strong> – パスワード保護と管理</li>
            <li><strong>アクセシビリティ</strong> – 音声出力、キーボード操作、高コントラスト</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "操作方法",
        'info_accessibility': "♿ アクセシビリティ – 完全なキーボード操作",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 一般</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDFを開く</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> 検索</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> ダーク/ライトモード切替</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> 印刷</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> 終了</div>

        <div class="shortcut-cat">📖 ナビゲーション</div>
        <div class="shortcut-row"><kbd>矢印キー</kbd> ページをめくる</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> ページへ移動</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> 最初のページ</div>
        <div class="shortcut-row"><kbd>Ende</kbd> 最後のページ</div>

        <div class="shortcut-cat">✏️ 編集</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> テキスト挿入</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> ページ削除</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> ページ抽出</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> ページ挿入</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> ページ移動</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> ページ回転</div>

        <div class="shortcut-cat">🖼️ 要素の移動</div>
        <div class="shortcut-row"><kbd>矢印キー</kbd> テキスト/画像/署名を移動</div>
        <div class="shortcut-row"><kbd>Ctrl+矢印キー</kbd> 大きなステップ</div>
        <div class="shortcut-row"><kbd>Enter</kbd> 保存</div>
        <div class="shortcut-row"><kbd>ESC</kbd> 破棄</div>

        <div class="shortcut-cat">🗣️ 音声出力</div>
        <div class="shortcut-row"><kbd>F2</kbd> 音声出力のオン/オフ</div>
        """,
        'info_contextmenu': "📌 重要: すべての機能はコンテキストメニュー (右クリック) からも利用できます！",
        'info_accessibility_hint': "💡 ヒント: 音声出力 (F2) は操作の方向性を容易にし、メニューやダイアログのフィードバックを提供します。",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "ライセンス & インプリント",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 インプリント</strong><br>
        § 5 TMGに基づく情報:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, ドイツ<br>
        Eメール: binhdiez64@gmail.com<br>
        内容責任者: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ 免責事項</strong><br>
        本ソフトウェアは細心の注意を払って開発されました。正確性、完全性、機能性についての保証は一切いたしません。使用は自己責任で行ってください。<br><br>

        <strong>📄 MITライセンス (個人利用)</strong><br>
        著作権 (c) 2026 Toralf Schulz (BinhDiez)<br>
        許可: 無料使用、私的変更、個人的なコピー。<br>
        不許可: 販売、商用利用、著作権表示の削除。<br><br>

        <strong>🔧 サードパーティコンポーネント</strong><br>
        このソフトウェアには、GPL、AGPL、Apache 2.0、BSD、MITライセンスのコンポーネントが含まれています。<br>
        再配布する際は、それぞれのライセンス条件に従う必要があります。<br><br>

        <strong>🌐 オープンソース</strong><br>
        ソースコードは公開されており、それぞれのライセンス条件に従って閲覧、変更、再配布することができます。<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "謝辞",
        'info_credits': "オープンソースコミュニティへの感謝",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF処理</li>
            <li><strong>PyQt5</strong> – グラフィカルインターフェース</li>
            <li><strong>Tesseract OCR</strong> – テキスト認識</li>
            <li><strong>OCRmyPDF</strong> – OCR統合</li>
            <li><strong>python-docx</strong> – Wordエクスポート</li>
            <li><strong>qtawesome</strong> – アイコン</li>
            <li><strong>DeepSeek</strong> – 翻訳サポート (50以上の言語)</li>
            <li><strong>すべてのユーザー</strong> – 貴重なフィードバックに感謝</li>
            <li><strong>オープンソースコミュニティ</strong> – 素晴らしいライブラリに感謝</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "言語",
        'info_languages_header': "🌍 言語サポート",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View は現在 <strong>62 言語</strong>をサポートしています – これにより、ソフトウェアを世界中でアクセシブルに利用できます。</p>

            <p><strong>📖 完全な言語リスト（2026年3月現在）:</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 アフリカーンス語</li>
                    <li>🇦🇱 アルバニア語 (Shqip)</li>
                    <li>🇩🇿 アラビア語 (العربية)</li>
                    <li>🇮🇩 バリ語 (Basa Bali)</li>
                    <li>🇧🇩 ベンガル語 (বাংলা)</li>
                    <li>🇲🇲 ビルマ語 (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 ボスニア語 (Bosanski)</li>
                    <li>🇧🇬 ブルガリア語 (Български)</li>
                    <li>🇨🇳 中国語 (中文)</li>
                    <li>🇩🇰 デンマーク語 (Dansk)</li>
                    <li>🇩🇪 ドイツ語 (Deutsch)</li>
                    <li>🇬🇧 英語 (English)</li>
                    <li>🇪🇪 エストニア語 (Eesti)</li>
                    <li>🇫🇮 フィンランド語 (Suomi)</li>
                    <li>🇫🇷 フランス語 (Français)</li>
                    <li>🇬🇷 ギリシャ語 (Ελληνικά)</li>
                    <li>🇮🇱 ヘブライ語 (עברית)</li>
                    <li>🇮🇳 ヒンディー語 (हिन्दी)</li>
                    <li>🇭🇷 クロアチア語 (Hrvatski)</li>
                    <li>🇭🇺 ハンガリー語 (Magyar)</li>
                    <li>🇮🇩 インドネシア語 (Bahasa Indonesia)</li>
                    <li>🇮🇪 アイルランド語 (Gaeilge)</li>
                    <li>🇮🇸 アイスランド語 (Íslenska)</li>
                    <li>🇮🇹 イタリア語 (Italiano)</li>
                    <li>🇯🇵 日本語 (日本語)</li>
                    <li>🇰🇭 クメール語 (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 韓国語 (한국어)</li>
                    <li>🇱🇦 ラオ語 (ພາສາລາວ)</li>
                    <li>🇱🇻 ラトビア語 (Latviešu)</li>
                    <li>🇱🇹 リトアニア語 (Lietuvių)</li>
                    <li>🇱🇺 ルクセンブルク語 (Lëtzebuergesch)</li>
                    <li>🇲🇾 マレー語 (Bahasa Melayu)</li>
                    <li>🇮🇳 マラーティー語 (मराठी)</li>
                    <li>🇲🇳 モンゴル語 (Монгол)</li>
                    <li>🇳🇵 ネパール語 (नेपाली)</li>
                    <li>🇳🇱 オランダ語 (Nederlands)</li>
                    <li>🇳🇴 ノルウェー語 (Norsk)</li>
                    <li>🇦🇫 パシュトゥー語 (پښتو)</li>
                    <li>🇮🇷 ペルシア語 (فارسی)</li>
                    <li>🇵🇱 ポーランド語 (Polski)</li>
                    <li>🇵🇹 ポルトガル語 (Português)</li>
                    <li>🇮🇳 パンジャーブ語 (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 ルーマニア語 (Română)</li>
                    <li>🇷🇺 ロシア語 (Русский)</li>
                    <li>🇸🇪 スウェーデン語 (Svenska)</li>
                    <li>🇷🇸 セルビア語 (Српски)</li>
                    <li>🇸🇰 スロバキア語 (Slovenčina)</li>
                    <li>🇸🇮 スロベニア語 (Slovenščina)</li>
                    <li>🇪🇸 スペイン語 (Español)</li>
                    <li>🇹🇿 スワヒリ語 (Kiswahili)</li>
                    <li>🇵🇭 タガログ語 (Filipino)</li>
                    <li>🇮🇳 タミル語 (தமிழ்)</li>
                    <li>🇮🇳 テルグ語 (తెలుగు)</li>
                    <li>🇹🇭 タイ語 (ไทย)</li>
                    <li>🇨🇿 チェコ語 (Čeština)</li>
                    <li>🇹🇷 トルコ語 (Türkçe)</li>
                    <li>🇺🇦 ウクライナ語 (Українська)</li>
                    <li>🇵🇰 ウルドゥー語 (اردو)</li>
                    <li>🇻🇳 ベトナム語 (Tiếng Việt)</li>
                    <li>🇸🇳 ウォロフ語 (Wolof)</li>
                    <li>🇺🇸 イディッシュ語 (ייִדיש)</li>
                    <li>🇿🇦 ズールー語 (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 独自の言語を追加:</strong><br>
                まだ含まれていない言語をご希望ですか？ 独自の辞書ファイル（<code>sprache_xx.py</code>）をアプリケーションの隣に置くだけで、ソフトウェアが自動的に認識します。特定の翻訳にご興味があれば、お気軽にお問い合わせください。
            </div>

            <p><strong>🙏 特別な感謝:</strong> すべての辞書を62言語に翻訳する際にサポートしてくれたDeepSeekに感謝します。</p>

            <p>📧 翻訳に関するお問い合わせ: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "エラー",
        'error_occurred': "エラーが発生しました",
        'error_pdf_load': "PDFの読み込み中にエラーが発生しました",
        'error_pdf_save': "PDFの保存中にエラーが発生しました",
        'error_ocr': "テキスト認識中にエラーが発生しました",
        'error_no_pdf': "PDFが読み込まれていません",
        'error_page_not_found': "ページが見つかりません",
        'error_invalid_range': "無効なページ範囲です",
        'error_file_not_found': "ファイルが見つかりません",
        'error_permission': "権限がありません",
        'error_unknown': "不明なエラー",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "成功",
        'success_operation': "操作が正常に完了しました",
        'success_saved': "正常に保存されました",
        'success_exported': "正常にエクスポートされました",
        'success_imported': "正常にインポートされました",
        'success_deleted': "正常に削除されました",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "確認",
        'confirm_yes': "はい",
        'confirm_no': "いいえ",
        'confirm_ok': "OK",
        'confirm_cancel': "キャンセル",
        'confirm_delete': "削除",
        'confirm_overwrite': "上書き",
        'confirm_continue': "続行",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDFを読み込み中...",
        'progress_saving': "PDFを保存中...",
        'progress_exporting': "PDFをエクスポート中...",
        'progress_processing': "処理中...",
        'progress_wait': "しばらくお待ちください...",
        'progress_preparing': "準備中...",
        'progress_finalizing': "最終処理中...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "白",
        'color_black': "黒",
        'color_red': "赤",
        'color_green': "緑",
        'color_blue': "青",
        'color_yellow': "黄",
        'color_magenta': "マゼンタ",
        'color_cyan': "シアン",
        'color_orange': "オレンジ",
        'color_gray': "灰色",
        'color_custom': "色を選択",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&ファイル",
        'menu_edit': "&編集",
        'menu_view': "&表示",
        'menu_tools': "&ツール",
        'menu_settings': "&設定",
        'menu_help': "&ヘルプ",
        'menu_language': "🌐 言語",
        'menu_guides': "&ガイド",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&開く",
        'file_save_as': "&名前を付けて保存...",
        'file_protect': "&文書を保護...",
        'file_export': "&エクスポート",
        'file_export_pages': "Pagesにエクスポート",
        'file_export_word': "DOCXにエクスポート",
        'file_export_text': "TXTにエクスポート",
        'file_print_now': "&すぐに印刷",
        'file_print': "&印刷",
        'file_close': "&閉じる",
        'file_quit': "&終了",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&検索",
        'edit_ocr': " OCRを実行",
        'edit_rotate': "&ページを回転",
        'edit_rotate_all': "すべてのページを回転",
        'edit_delete_pages': "&ページを削除",
        'edit_extract_pages': "&ページを抽出",
        'edit_insert_pages': "&ページを挿入",
        'edit_move_pages': "&ページを移動",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " テキストと十字を挿入",
        'text_insert': " テキストを挿入",
        'cross_insert': " 十字を挿入",
        'text_customize': " テキストを調整",
        'cross_customize': " この十字を調整",
        'cross_customize_all': " すべての十字を調整",
        'text_discard': " このテキスト/十字を破棄",
        'text_discard_all': " すべてのテキストと十字を破棄",
        'text_save_all': " すべてのテキストと十字を保存",
        'text_guide': " テキスト入力 / テキストブロック – ガイド",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " 署名を挿入",
        'signature_settings_menu': " 設定...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " 画像を挿入",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " 図形を挿入",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&テキストウィンドウを表示",
        'view_zoom': "&ズーム",
        'view_zoom_page': "&ページ幅 (デフォルト)",
        'view_zoom_two': "&2ページ表示",
        'view_zoom_overview': "&概要 (複数ページ)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&アクセシビリティ",
        'settings_voice': "音声出力",
        'settings_voice_tooltip': "スクリーンリーダーの音声出力を追加情報で補完します",
        'settings_signature': "&署名の設定",
        'settings_password': "&パスワード管理",
        'settings_backup': "変更前にバックアップを作成",
        'settings_export_import': "&設定をエクスポート / インポート",
        'settings_export': "&すべての設定をエクスポート...",
        'settings_import': "&すべての設定をインポート...",
        'settings_export_info': "&エクスポートされるもの",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "オン",
        'voice_off': "オフ",
        'voice_toggle': "音声出力 {0}",
        'voice_speed': "速度 {0}%",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "ツールが見つかりません:\n{0}\n\nBASE_DIR: {1}\nPDFツールがディレクトリ {1} にインストールされていることを確認してください。",
        'tool_started': "{0} を開始しました",
        'tool_start_failed': "開始できませんでした",
        'process_error_failed_to_start': "プロセスを開始できませんでした。ファイルは存在しますか？",
        'process_error_crashed': "プロセスが起動時にクラッシュしました。",
        'process_error_timeout': "プロセスのタイムアウトが発生しました。",
        'process_error_write': "プロセスへの書き込みエラー。",
        'process_error_read': "プロセスからの読み取りエラー。",
        'process_error_unknown': "不明なプロセスエラー",
        'process_command': "コマンド",
        'process_normal_exit': "正常終了",
        'process_crashed': "クラッシュ",
        'process_nonzero_exit': "{0} がエラーコード {1} で終了しました",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "キャンセル中...",
        'move_cancelling': "移動をキャンセル中",
        'opening_pdf': "PDFを開いています...",
        'loading_document': "文書を読み込んでいます...",
        'pdf_opened': "PDFが開かれました",
        'pages_found_moving': "{0} ページ見つかりました、{1} ページ移動",
        'creating_backup': "バックアップを作成中...",
        'backup_description': "元のファイルをバックアップ中...",
        'backup_saved_as': "バックアップが保存されました: {0}",
        'error_format': "エラー: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "検索がクリアされました",
        'page_header_simple': "=== ページ {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "パスワード管理 – ガイド",
        'password_guide_voice': "パスワード管理のガイドです。注意事項をお読みください。",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 パスワード管理 – 詳細ガイド</strong></p>

        <p><strong>1. PDFのパスワード保護</strong></p>
        <ul>
        <li>パスワードで保護されたPDFを開くと、パスワードを入力するダイアログが表示されます。</li>
        <li>パスワードを暗号化して保存すると、毎回入力する必要がなくなります (「パスワードを保存」チェックボックス)。</li>
        <li>「パスワードを削除」ボタンで、復号化されたPDFのコピーを作成し、データベースからパスワードを削除できます。</li>
        </ul>

        <p><strong>2. マスターパスワード</strong></p>
        <ul>
        <li>マスターパスワードは、保存されたすべてのPDFパスワードへのアクセスを保護します。</li>
        <li><strong>設定:</strong> 「設定 → パスワード管理 → マスターパスワード設定」に移動し、「マスターパスワードを設定」をクリックします。強力なパスワードを選択してください (少なくとも8文字)。</li>
        <li><strong>変更:</strong> 認証に成功した後、マスターパスワードを変更できます。</li>
        <li><strong>削除:</strong> マスターパスワードを削除すると、保存されたすべてのパスワードが完全に削除されます。事前にバックアップをエクスポートできます。</li>
        <li>セッションごとに一度、保護された機能 (例: パスワードの表示) にアクセスするには、マスターパスワードで認証する必要があります。</li>
        </ul>

        <p><strong>3. パスワード管理 (一覧)</strong></p>
        <ul>
        <li>「設定 → パスワード管理」では、保存されたすべてのPDFファイルとその暗号化されたパスワードのテーブルが表示されます。</li>
        <li><strong>マスターパスワードなし:</strong> エントリの削除のみ可能 – パスワードは非表示のままです。</li>
        <li><strong>マスターパスワードあり (認証済み):</strong> パスワードの表示、コピー、エクスポート、削除が可能です。</li>
        <li><strong>エクスポート:</strong> 形式 (JSON、CSV、TXT) を選択し、リストを保存します。マスターパスワードが設定されている場合、パスワードを復号化してエクスポートするか、暗号化したままにするかを選択できます。</li>
        <li><strong>インポート:</strong> 以前にエクスポートしたZIPファイル (すべての設定) は、「設定 → 設定をエクスポート / インポート」から再インポートできます。注意: 既存のデータは上書きされます！</li>
        </ul>

        <p><strong>4. パスワード生成器</strong></p>
        <ul>
        <li>パスワードダイアログ (例: PDF保護時) で、入力フィールドの右側にあるサイコロボタン 🎲 をクリックします。</li>
        <li>パスワード生成器が開きます。長さ、文字セット (大文字、小文字、数字、記号)、読みやすさのための区切り文字を設定できます。</li>
        <li>生成されたパスワードは直接使用でき、必要に応じてコピーできます。</li>
        </ul>

        <p><strong>5. 重要なセキュリティ注意事項</strong></p>
        <ul>
        <li>保存されたパスワードはAES-256で暗号化されて保存されます。鍵はマスターパスワード (設定されている場合) または固定値 (マスターパスワードなし) から導出されます。</li>
        <li>マスターパスワードがない場合、パスワードは暗号化されていますが、鍵はプログラムに組み込まれています – ファイルにアクセスできる攻撃者はそれらを復号化できる可能性があります。そのため、マスターパスワードの使用を強くお勧めします。</li>
        <li>パスワードデータベースは `Data/passwords.json` ファイルにあります。定期的にバックアップを作成し、特にマスターパスワードを削除する前に行ってください。</li>
        <li>マスターパスワードを紛失すると、保存されたすべてのパスワードが永久に失われます。</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "反転モード",
        'invert_mode_classic': "クラシック (すべての色を反転)",
        'invert_mode_smart': "スマート (明るさのみ反転)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "グレースケールしきい値",
        'gray_threshold_10': "10% (厳格)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (標準)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (ソフト)",
        'threshold_changed': "しきい値を {0}% に設定しました",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "グレースケールしきい値 – 説明",
        'threshold_guide_text': "グレースケールしきい値は、スマートダークモードで「グレー」と見なされ反転されるピクセルを決定します。\n\n"
                                "• 低い値 (10%) はほぼ完全なグレートーンのみを反転します – 色付きの要素は完全に保持されます。\n"
                                "• 高い値 (50%) はわずかに色付きのピクセルも反転します – これによりコントラストが向上しますが、色が歪む可能性があります。\n\n"
                                "最適な値はドキュメントによって異なります。純粋なテキストドキュメントでは 30–40% が理想的で、色付きのグラフィックでは 10–20% が適しています。\n\n"
                                "値は「設定」メニューからいつでも調整できます – PDFはすぐに再読み込みされます。\n\n"
                                "注意:\n* 写真や画像はライトモードでのみ正しく表示できます！\n* 反転設定はダークモードが有効な場合にのみ表示されます。",
        'threshold_guide_voice': "グレースケールしきい値は、スマートダークモードの介入の強さを決定します。低い値は色を保護し、高い値はコントラストを高めます。",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDFを開いています...",
        'progress_loading_document': "ドキュメントを読み込んでいます...",
        'progress_pdf_opened': "PDFを開きました",
        'progress_creating_backup': "バックアップを作成しています...",
        'progress_backup_description': "元のファイルを保護しています...",
        'progress_backup_created': "バックアップを作成しました",
        'progress_backup_saved_as': "{0} として保存しました",
        'progress_analyzing_start': "分析を開始しています...",
        'progress_searching_empty': "空のページを検索しています...",
        'progress_page_empty': "ページ {0} は空です",
        'progress_page_keep': "ページ {0} を保持します",
        'progress_analysis_complete': "分析が完了しました",
        'progress_empty_found': "{0} 件の空のページが見つかりました",
        'progress_current_page': "現在のページ",
        'progress_mark_delete': "削除対象としてマークされています",
        'progress_range_selected': "ページ範囲 {0}-{1}",
        'progress_deleting_pages': "{0} ページを削除しています",
        'progress_creating_new_pdf': "新しいPDFを作成しています...",
        'progress_transferring_pages': "ページを転送しています",
        'progress_keeping_page': "ページ {0} は保持されます ({1}/{2})",
        'progress_saving_pdf': "PDFを保存しています...",
        'progress_optimizing': "ファイルサイズを最適化しています...",
        'progress_finalizing': "仕上げています...",
        'progress_new_size': "新しいサイズ: {0:.2f} MB",
        'progress_cancelling': "キャンセルしています...",
        'progress_cancel_message': "{0} をキャンセルしています",
        'progress_pages_found_moving': "{0} ページが見つかりました、{1} ページを移動します",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDFを分析しています...",
        'ocr_status_optimizing': "画像を最適化しています...",
        'ocr_status_recognizing': "テキストを認識しています...",
        'ocr_status_embedding': "テキストを埋め込んでいます...",
        'ocr_status_finalizing': "PDFを仕上げています...",

        # PDF-Laden
        'progress_preparing': "準備しています...",
        'progress_loading': "PDFを読み込んでいます...",

        # Seitenoperationen
        'progress_deleting_title': "ページを削除しています...",
        'progress_moving_title': "ページを移動しています...",
        'pages_found': "見つかったページ",
        'progress_creating_new_order': "新しい順序を作成しています...",
        'progress_sorting_pages': "ページをソートしています...",
        'progress_moving_to_begin': "{0} ページを先頭に移動します",
        'progress_transferring_count': "{0} ページを転送します",
        'progress_transferring_before_target': "ターゲットの前にページを転送します",
        'progress_moving_pages': "{0} ページを移動します",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_バックアップ_",
        'filename_protected_suffix': "_保護_",
        'filename_copy_suffix': "_コピー",
        'filename_page_single': "_ページ_",
        'filename_page_range': "_ページ_",
        'filename_export_page': "_ページ_{0:03}",
        'filename_export_range': "_ページ_{0}-{1}",
        'filename_export_multiple': "_ページ_{0}",
        'filename_with_text': "_テキスト付き",
        'filename_with_signature': "_署名付き",
        'filename_with_image': "_画像付き",
        'filename_with_forms': "_図形付き",
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
        'view_toggle_navbar': "ボタンバーを表示",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "すべてのページを削除することはできません",
		'pages_cannot_delete_last_page': '最後のページは削除できません！',
		'pages_cannot_delete_all_pages': 'ドキュメントには少なくとも1ページ残す必要があります！',
		'delete_pages_confirm': '{0}ページを削除してもよろしいですか？',
		'delete_pages_confirm_voice': '{0}ページを削除してもよろしいですか？',
		'pages_deleted': '{0}ページが正常に削除されました。',
		'warning': '警告',
		'error': 'エラー',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "フォームが選択されていません",
        'form_customized': "フォームをカスタマイズしました",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "選択",
        'btn_use': "使用",
        'master_password_for_spasswords': "パスワードを保存して使用するには、最初にマスターパスワードを設定する必要があります。\n\n今すぐマスターパスワードを設定しますか？",
        'open_saved_dialog_title': "保存されたファイルを開く",
        'open_saved_question': "保存されたファイルを今すぐ開きますか？",
        'password': "パスワード",
        'password_manager_master_required': "パスワードマネージャーは、マスターパスワードが設定されている場合のみ利用できます。\n\n今すぐマスターパスワードを設定しますか？",
        'password_master_required_for_select': "保存されたパスワードを表示して選択するには、最初にマスターパスワードで認証する必要があります。\n\n今すぐ認証しますか？",
        'password_not_available': "選択されたパスワードは利用できないか、復号化できませんでした。",
        'password_options_title': "パスワードオプション",
        'password_save_choice_change': "新しいパスワードを設定",
        'password_save_choice_keep': "既存のパスワードを使用",
        'password_save_choice_none': "暗号化せずに保存",
        'password_save_hint': "パスワードを安全に保存するには、最初にマスターパスワードを設定してください。",
        'password_save_master_required': "パスワードを保存（マスターパスワードが必要）",
        'password_save_question': "現在のPDFはパスワードで保護されています。既存のパスワードを使用しますか、新しいパスワードを設定しますか、それとも暗号化せずに保存しますか？",
        'password_select': "パスワードを選択",
        'password_select_none': "パスワードが選択されていません。\n\nリストからパスワードを選択してください。",
        'password_select_one': "正確に1つのパスワードを選択してください。\n\n複数のパスワードがマークされています。",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_バックアップ",
        'filename_insert_suffix': "_挿入済み",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_ページ削除",
        'filename_pages_moved': "_ページ移動",
        'filename_rotated_all_suffix': "_全ページ回転",
        'filename_rotated_suffix': "_ページ回転",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "PDF変更時のファイル名設定",
        'filename_keep_suffixes': "以前の拡張子を保持（例：_テキスト付き）",
        'filename_keep_suffixes_false': "置き換え",
        'filename_keep_suffixes_true': "保持",
        'filename_preview_label': "ファイル名のプレビュー:",
        'filename_preview_overwrite_hint': "プレビュー不可 – 元のファイルは上書きされます。",
        'filename_separator': "単語間の区切り文字",
        'filename_separator_none': "区切り文字なし",
        'filename_separator_space': "スペース ( )",
        'filename_separator_underscore': "アンダースコア (_)",
        'filename_settings_saved': "ファイル名設定を保存しました",
        'filename_settings_title': "ファイル名の書式設定とバックアップ",
        'filename_timestamp_position': "タイムスタンプの位置",
        'filename_timestamp_position_after': "ベース名の後",
        'filename_timestamp_position_before': "先頭",
        'filename_timestamp_position_end': "末尾",
        'filename_use_timestamp': "タイムスタンプを使用",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>変更時の動作:</b><ul><li>ページの削除と挿入</li><li>テキスト、署名、画像、図形の挿入</li><li>OCR</li></ul></html>",
        'backup_section': "ページ操作のバックアップ（削除、移動）",
        'behavior_info': "注意：「元を上書き」の場合、タイムスタンプと接尾辞は無視されます – ファイル名はそのまま維持されます。",
        'behavior_new_file': "常に新しいファイルを作成（タイムスタンプと接尾辞付き）",
        'behavior_overwrite': "元を上書き（新しいファイルは作成しない）",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "すべてのページが回転されました。\n\n元のファイルは変更されていません。\n新しいファイル: {0}",
        'all_pages_rotated_voice': "すべてのページを回転、新しいファイルを作成しました。",
        'empty_pages_deleted_new_file': "{0} 枚の空白ページが削除されました。\n\n元のファイルは変更されていません。\n新しいファイル: {1}",
        'empty_pages_deleted_voice': "{0} 枚の空白ページを削除、新しいファイルを作成しました。",
        'ocr_keep_original': "元のファイルを保持（後で手動で開く）",
        'ocr_new_file_question': "新しい検索可能なPDFが保存されました:\n{0}\n\n今すぐ開きますか？",
        'ocr_open_new': "新しいOCRファイルを開く",
        'ocr_original_kept': "元のファイルは開いたままです。OCRファイルは保存されました。",
        'page_deleted_new_file': "ページ {0} が削除されました。\n\n元のファイルは変更されていません。\n新しいファイル: {1}",
        'page_deleted_voice': "ページ {0} を削除、新しいファイルを作成しました。",
        'page_rotated_new_file': "ページ {0} が回転されました。\n\n元のファイルは変更されていません。\n新しいファイル: {1}",
        'page_rotated_voice': "ページ {0} を回転、新しいファイルを作成しました。",
        'pages_deleted_new_file': "{0} 枚のページが削除されました。\n\n元のファイルは変更されていません。\n新しいファイル: {1}",
        'pages_deleted_new_file_voice': "{0} 枚のページを削除、新しいファイルを作成しました。",
        'pages_inserted_new_file': "{0} 枚のページが挿入されました。\n\n元のファイルは変更されていません。\n新しいファイル: {1}",
        'pages_inserted_new_file_ask': "{0} 枚のページが挿入されました。\n\n元のファイルは変更されていません。\n新しいファイル: {1}\n\n今すぐ開きますか？",
        'pages_inserted_voice_new': "{0} 枚のページを挿入、新しいファイルを作成しました。",
        'pages_moved_new_file': "{0} 枚のページが移動されました。\n\n元のファイルは変更されていません。\n新しいファイル: {1}",
        'pages_moved_new_file_voice': "{0} 枚のページを移動、新しいファイルを作成しました。",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "今後表示しない",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 バックアップ設定</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ バックアップ ON</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">元を上書きするすべての変更</strong>（テキスト、署名、画像、図形、OCR、回転、挿入、ページの削除/移動）に対して、変更を適用する前に<strong>タイムスタンプ付きのバックアップが自動的に作成されます</strong>。</p>
                <p style="margin: 5px 0 5px 20px;">• バックアップは元のファイルの隣に配置されます（例: <code>ドキュメント_バックアップ_20260412_120000.pdf</code>）。</p>
                <p style="margin: 5px 0 5px 20px;">• さらに<strong>「元を上書き」</strong>オプションを有効にしている場合も、バックアップが作成されます。</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 バックアップ OFF</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>バックアップは作成されません</strong> – 上書き時もページ操作時も。</p>
                <p style="margin: 5px 0 5px 20px;">• 上書きすると元のファイルは回復不能に失われる可能性があります。</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">経験豊富なユーザーのみ推奨！</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ヒント:</strong> バックアップ設定は「元を上書き」オプションとは独立しています。両方を組み合わせることができます。<br>
                このメッセージを永久に非表示にできます。
            </div>
        </div>
        """,
        'backup_info_title': "バックアップの動作",
        'backup_info_voice': "ページ操作時のバックアップ動作についてのお知らせ。バックアップONは元を上書き、バックアップOFFは新しいファイルを作成します。",
        'show_backup_info': "バックアップ設定についての情報",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "今後表示しない",
        'overwrite_enable_backup': "バックアップを有効にする（推奨）",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ 元を上書き</p>
            <p>このオプションを有効にすると、変更（テキスト、署名、画像、図形、OCR、回転、挿入）は<strong>直接元のファイルに保存されます</strong> – <strong>新しいファイルは作成されません</strong>。</p>
            <p>• ファイル名は変更されません。<br>
            • タイムスタンプと接尾辞は無視されます。<br>
            • <strong>バックアップがない場合、元のファイルは回復不能に失われる可能性があります。</strong></p>
            <p style="color: #FFD700;">推奨: 自動バックアップを取得するために、バックアップオプションも有効にしてください。</p>
        </div>
        """,
        'overwrite_info_title': "元を上書き",
        'overwrite_info_voice': "警告: 元を上書き – 新しいファイルは作成されません。バックアップ推奨。",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} 枚のページが挿入されました。\n\n元のファイルは上書きされました。\nバックアップが作成されました。",
        'pages_inserted_overwrite_no_backup': "{0} 枚のページが挿入されました。\n\n元のファイルは上書きされました。\nバックアップは作成されませんでした。",
        'texts_saved_overwrite_with_backup': "変更は元のファイルに保存されました。\n\nバックアップが作成されました。",
        'texts_saved_overwrite_no_backup': "変更は元のファイルに保存されました。\n\nバックアップは作成されませんでした。",
        'texts_crosses_saved_new_file': "{0} {1} と {2} {3} が挿入されました。\n\n元のファイルは変更されていません。\n新しいファイルが作成されました。\n\n新しいPDFを読み込み中...",
        'texts_saved_new_file': "{0} {1} が挿入されました。\n\n元のファイルは変更されていません。\n新しいファイルが作成されました。\n\n新しいPDFを読み込み中...",
        'crosses_saved_new_file': "{0} {1} が挿入されました。\n\n元のファイルは変更されていません。\n新しいファイルが作成されました。\n\n新しいPDFを読み込み中...",
        'elements_saved_new_file': "{0} 個の要素が挿入されました。\n\n元のファイルは変更されていません。\n新しいファイルが作成されました。\n\n新しいPDFを読み込み中...",
        'signatures_saved_overwrite_with_backup': "署名は元のファイルに保存されました。\n\nバックアップが作成されました。",
        'signatures_saved_overwrite_no_backup': "署名は元のファイルに保存されました。\n\nバックアップは作成されませんでした。",
        'images_saved_overwrite_with_backup': "画像は元のファイルに保存されました。\n\nバックアップが作成されました。",
        'images_saved_overwrite_no_backup': "画像は元のファイルに保存されました。\n\nバックアップは作成されませんでした。",
        'forms_saved_overwrite_with_backup': "図形は元のファイルに保存されました。\n\nバックアップが作成されました。",
        'forms_saved_overwrite_no_backup': "図形は元のファイルに保存されました。\n\nバックアップは作成されませんでした。",
        'signatures_saved_new_file': "{0} 個の署名が挿入されました。\n\n元のファイルは変更されていません。\n新しいファイルが作成されました。\n\n新しいPDFを読み込み中...",
        'images_saved_new_file': "{0} 個の画像が挿入されました。\n\n元のファイルは変更されていません。\n新しいファイルが作成されました。\n\n新しいPDFを読み込み中...",
        'forms_saved_new_file': "{0} 個の図形が挿入されました。\n\n元のファイルは変更されていません。\n新しいファイルが作成されました。\n\n新しいPDFを読み込み中...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "警告: このPDFには回転されたページが含まれています。配置がずれる可能性があります。",
        'page_rotated_warning_title': "回転されたページが検出されました",
        'page_rotated_warning_message': "現在のページ {0} は {1}° 回転されています。\n\n回転されたページへの要素の挿入はサポートされていません。\n\nページを今すぐ直立位置に回転しますか？",
        'page_rotated_warning_voice': "警告: ページが回転されています。最初に回転してください。",
        'paste_on_rotated_page_simple_warning': "ページ {0} への挿入はできません！\n\nこのページは {1}° 回転されています。\n\n最初にページを 0° に回転してください（メニュー: 編集 → ページを整列）。\n\n警告:\nページを回転する前に保存しないと、以前コピーした要素は失われます。",
        'paste_on_rotated_page_voice': "挿入を中止しました。ページが回転されています。最初にページを整列してください。",
        'page_rotated_cancel': "キャンセル",
        'page_rotated_rotate_until_upright': "ページを繰り返し回転（直立するまで）",
        'page_rotated_now_upright': "ページは直立しました。挿入できます。",
        'page_rotated_still_not_upright': "ページを直立位置に回転できませんでした。手動で修正してください。",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "ヘルプ: 回転されたページを修正する",
        'help_rotated_pages_voice': "回転されたページを修正するためのヘルプを開きます。",
        'btn_help': "ヘルプ",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 問題: 回転されたページ – 挿入が正しく機能しない</p>

            <p>回転されたページへのテキスト、署名、図形の挿入が正しく機能しない場合、外部のPDFエディタでページを修正できます。</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ 外部ツールでの解決方法（例: macOSプレビュー）</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>ページを書き出す</strong><br>
                &nbsp;&nbsp;メニューの<strong>ファイル → ページとして書き出す</strong>をクリックするか、別の方法で目的のページを単一のPDFとして保存します。</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>外部プログラムでページを開く</strong><br>
                &nbsp;&nbsp;書き出したPDFをPDFエディタで開きます（例: <strong>macOSプレビュー</strong>, Adobe Acrobat, PDF Expert）。</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>ページを回転する</strong><br>
                &nbsp;&nbsp;ページが直立するように回転します（プレビューでは: <strong>ツール → 回転</strong> または <strong>⌘ + R</strong>）。</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>保存する</strong><br>
                &nbsp;&nbsp;修正したページを保存します（<strong>⌘ + S</strong>）。</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>ページを元のドキュメントに再挿入する</strong><br>
                &nbsp;&nbsp;PDFDarkViewに戻り、修正したページを目的の位置に挿入します:<br>
                &nbsp;&nbsp;<strong>編集 → ページを挿入</strong>。</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 代替方法: 元のファイルでページを回転する</p>
                <p style="margin: 5px 0 5px 20px;">• 組み込みの回転機能（<strong>編集 → ページを回転</strong>）を使用して、ページを段階的に修正します。<br>
                • 回転するたびに、挿入が機能するようになったか確認できます。<br>
                • これが多くの場合、より迅速な解決方法です – まずこれを試してください！</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>ヒント:</strong> 回転されたページに頻繁に遭遇する場合は、挿入ダイアログの警告を永久に非表示にできます。<br>
                その場合、配置がずれる可能性があります – 結果を理解している場合のみこのオプションを使用してください。
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "ページを整列",
        'menu_rotate_normalize_tooltip': "ページを回転するか、0°にリセット",
        'normalize_current_page': "現在のページを直立位置に戻す（0°に設定）",
        'normalize_all_pages': "すべてのページを直立位置に戻す（0°に設定）",
        'page_normalized': "ページ {0} を直立位置に設定しました。",
        'all_pages_normalized': "すべてのページを直立位置に設定しました。",
        'page_already_upright': "ページ {0} はすでに直立しています。",
        'all_pages_already_upright': "すべてのページはすでに直立しています。",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDFに検索可能なテキストが含まれていません。</p><p>{0} にエクスポートするためにOCRを実行しますか？</p>",
        'export_ocr_voice': "PDFにテキストが含まれていません。{0} へのエクスポートにはOCRが必要です。",
        'export_no_ocr_possible': "OCRなしのエクスポートはできません。メニューからOCRを実行してください。",
        'ocr_failed_export_not_possible': "OCRに失敗しました。エクスポートを実行できません。",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDFはプレビューで開きます。そこで印刷プロセスを開始してください。",
        'print_preview_manual': "PDFが開かれました。手動で印刷コマンドを実行してください（例: Ctrl+P）。",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDFを結合",
        'merge_pdfs': "PDFを結合",
        'merge_progress_title': "PDFを結合中...",
        'merge_pdfs_list': "順序通りのPDF（ドラッグ＆ドロップで並べ替え）",
        'merge_add_pdf': "PDFを追加",
        'merge_remove': "削除",
        'merge_move_up': "上へ",
        'merge_move_down': "下へ",
        'merge_pdfs_info': "💡 ヒント: ドラッグ＆ドロップで順序を変更できます",
        'merge_no_pdfs': "PDFが選択されていません。「PDFを追加」をクリックしてください。",
        'merge_info': "{0} 個のPDFを選択（約 {1} ページ）",
        'merge_open_file': "ファイルを開く",
        'merge_merge': "結合",
        'merge_error': "結合中にエラーが発生しました",
        'merge_min_two_pdfs_error': "結合するPDFファイルを少なくとも2つ選択してください。",
        'merge_select_pdfs': "結合するPDFを選択",
        'merge_error_file': "処理中にエラーが発生しました",
        'merge_cancelled': "結合がキャンセルされました",
        'merge_preparing': "準備中...",
        'merge_processing': "PDF {0} / {1} を処理中",
        'merge_saving': "結合したPDFを保存中...",
        'merge_complete': "完了！",
        'merge_success_title': "結合成功",
        'merge_success_voice': "{0} 個のPDFが正常に結合されました。",
        'merge_success_message': "{0} 個のPDFが正常に結合されました。\n\n新しいドキュメントには {1} ページがあります。\n\n新しいファイル:\n{2}\n\n保存場所:\n{3}\n{2}\n\nこのPDFを開きますか？",
        'replace_file_title': "ファイルを置き換えますか？",
        'replace_file_message': "すでにPDFが開いています。新しいファイルに置き換えますか？",
        'btn_yes': "はい",
        'btn_no': "いいえ",
        'filename_merge_suffix': "結合",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "{0} を開いています...",
        'progress_merge_reading': "{0} を読み込んでいます...",
        'progress_merge_adding': "{0} ページを追加しています...",
        'progress_merge_optimizing': "PDFを最適化しています...",
        'progress_merge_writing': "PDFを書き込んでいます...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "PDFを閉じる",
        'action_close_window': "ウィンドウを閉じる",
        'action_open_new_pdf': "新しいPDFを開く",
        'action_quit_app': "アプリケーションを終了する",
        'changes_saved': "変更が保存されました。",
        'file_close_title': "PDFファイルを閉じる",
        'save_before_action': "{0} の前に変更を保存しますか？ はい または いいえ？",
        'save_before_action_voice': "{0} の前に変更を保存しますか？ はい または いいえ？",
        'save_before_close_question': "閉じる前に変更を保存しますか？ はい または いいえ？",

         # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>検索可能なPDFを作成しました:\n\n{0}\n\n<b>必要に応じて再試行してください",
        "ocr_rotate_title": "OCR前にページを整列",
        "ocr_rotate_question": "PDFに回転したページが含まれています。\nOCR前にすべてのページを0°に整列しますか？\nこれによりテキスト認識が大幅に向上します。",
        "ocr_rotate_yes": "はい、整列する",
        "ocr_rotate_no": "いいえ、直接OCRを開始する",
        "ocr_rotate_voice": "PDFに回転したページが含まれています。OCR前にすべてのページを整列する必要がありますか？",
        "ocr_not_performed_message": "テキストがありません。「編集」メニュー→「OCRを実行」またはCtrl+RキーでOCRを実行してください。",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR設定",
        "ocr_language_btn": "OCR言語を選択",
        "ocr_language": "OCR言語",
        "ocr_language_current": "現在の言語:",
        "ocr_param_info": "パラメータ情報",

        "ocr_force_ocr_label": "OCRを強制",
        "ocr_deskew_label": "傾き補正",
        "ocr_clean_label": "画像をクリーンアップ",
        "ocr_oversample_label": "解像度 (DPI)",
        "ocr_pagesegmode_label": "ページ分割",
        "ocr_oem_label": "OCRエンジンモード",
        "ocr_optimize_label": "PDF圧縮",
        "ocr_jobs_label": "並列処理数",
        "ocr_verbose_label": "ログ詳細度",

        "ocr_force_ocr_tooltip": "テキストが既に存在する場合でも、すべてのページでOCRを強制する",
        "ocr_deskew_tooltip": "傾いたスキャンを自動的に整列する",
        "ocr_clean_tooltip": "画像からノイズやアーティファクトを除去する",
        "ocr_oversample_tooltip": "OCR前に画像をこのDPIに拡大する",
        "ocr_pagesegmode_tooltip": "ページをテキスト領域に分割する方法を決定する",
        "ocr_oem_tooltip": "TesseractのOCRエンジンを選択する",
        "ocr_optimize_tooltip": "出力PDFの圧縮レベル",
        "ocr_jobs_tooltip": "並列OCRプロセスの数",
        "ocr_verbose_tooltip": "ログ出力の詳細レベル",
        "ocr_settings_explain_btn": "説明",

        "ocr_force_ocr_explain": "<b>すべての</b>ページでテキスト認識を強制します（既にテキストが含まれている場合でも）。\n\n推奨: スキャンしたPDFは<b>オン</b>、既存のテキストがあるネイティブPDFは<b>オフ</b>。",

        "ocr_deskew_explain": "わずかに傾いたスキャンを補正します（最大約5°）。\n\n推奨: スキャンしたドキュメントは<b>オン</b>、ページが完全に真っ直ぐな場合は<b>オフ</b>。",

        "ocr_clean_explain": "画像からノイズ、ドット、小さなアーティファクトを除去します。\n<b>重要:</b> ダイアクリティカルマーク（文字の上/下のドット）を含むアラビア語、タイ語、ベトナム語のテキストの場合、このオプションは<b>無効</b>にしてください。そうしないと重要な文字が失われる可能性があります。",

        "ocr_oversample_explain": "指定されたDPIに<b>テキスト認識前に</b>画像を拡大します。<br><br>• <b>72-150 DPI:</b> 非常に高速だが認識率が低い<br>• <b>200-300 DPI:</b> 最適範囲（デフォルト: 300）<br>• <b>400+ DPI:</b> 認識はわずかに向上するがファイルが大幅に大きくなる<br><br>推奨: 複雑な文字（アラビア語、中国語、日本語）は300 DPI、西洋言語は200 DPI。",

        "ocr_pagesegmode_explain": "Tesseractがページをテキスト領域に分割する方法を決定します。\n\n• <b>3 - 自動（デフォルト）:</b> 混合レイアウトに適しています\n• <b>4 - 単一カラム:</b> 単一カラムのテキスト用\n• <b>5 - 垂直ブロック:</b> 垂直書きの文字用（日本語、中国語）\n• <b>6 - 統一テキストブロック:</b> カラムなしのフローテキストに最適\n• <b>11 - 生画像:</b> スキャン不良/手書き用\n\n推奨: シンプルなテキストドキュメントは<b>6</b>、複雑なレイアウトは<b>3</b>。",

        "ocr_oem_explain": "TesseractのOCRエンジンを選択します。\n\n• <b>0 - Legacy:</b> 旧エンジン（高速だが精度が低い）\n• <b>1 - LSTM:</b> ニューラルエンジン（低速だが高精度）\n• <b>2 - Legacy + LSTM:</b> 両方の結果を組み合わせる\n• <b>3 - デフォルト（LSTM優先）:</b> ほとんどの場合に最適な選択\n\n推奨: 最大の認識精度を得るには<b>3</b>。",

        "ocr_optimize_explain": "出力PDFを圧縮します。\n\n• <b>0:</b> 最適化なし（最速処理）\n• <b>1:</b> 軽い最適化（良い妥協点）\n• <b>2:</b> 中程度の最適化\n• <b>3:</b> 強力な最適化（最小ファイル、ただし低速）\n\n推奨: 日常使用には<b>1</b>。",

        "ocr_jobs_explain": "OCRの並列処理数。\n\n• <b>1:</b> 低速だがメモリ消費が最も少ない\n• <b>4-8:</b> 最新のマルチコアプロセッサに最適\n• <b>12+:</b> 高メモリ使用で処理速度はわずかに向上\n\n推奨: CPUコア数（例: 4コアシステムでは<b>4</b>）。",

        "ocr_verbose_explain": "コンソールでのログ出力の詳細レベル。\n\n• <b>0:</b> 出力なし\n• <b>1:</b> 進捗とステータスメッセージ\n• <b>2:</b> 詳細な出力\n• <b>3:</b> 完全なデバッグ出力（非常に広範囲）\n\n推奨: 通常動作では<b>1</b>。",

        "ocr_reset_title": "設定をリセットしました",
        "ocr_reset_message": "すべてのOCR設定がデフォルト値にリセットされました。",
        "info_tooltip": "このパラメータの詳細情報",
        "ocr_reset_defaults": "デフォルトにリセット",

        "ocr_psm_0": "自動（Legacyエンジン）",
        "ocr_psm_1": "自動カラム検出",
        "ocr_psm_3": "自動（デフォルト）",
        "ocr_psm_4": "単一カラム",
        "ocr_psm_5": "垂直ブロック",
        "ocr_psm_6": "統一テキストブロック",
        "ocr_psm_7": "単一テキスト行",
        "ocr_psm_8": "単一単語",
        "ocr_psm_11": "生画像（レイアウト分析なし）",

        "ocr_oem_0": "Legacyエンジン（高速）",
        "ocr_oem_1": "LSTMエンジン（ニューラル、高精度）",
        "ocr_oem_2": "Legacy + LSTM組み合わせ",
        "ocr_oem_3": "デフォルト（LSTM優先）",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR言語...",
        "ocr_language_title": "OCR言語を選択",
        "ocr_language_instruction": "テキスト認識（OCR）の言語を選択してください。\n注意: 複数言語はパフォーマンスと精度の犠牲になります！\n最良の結果を得るには、1つの言語のみを選択してください。",
        "ocr_language_predefined": "定義済みの組み合わせ",
        "ocr_language_custom": "カスタム...",
        "ocr_language_selected": "選択されたOCR言語",
        "ocr_language_changed": "OCR言語を{0}に変更しました",
        "ocr_language_auto_detect": "利用可能な言語は自動的に検出されます。",
        "ocr_language_none_found": "Tesseract言語データが見つかりません！言語パッケージをインストールしてください（例: 'tesseract-ocr-deu', 'tesseract-ocr-eng'）。",
        "ocr_language_select_custom": "カスタム言語選択",
        "ocr_language_available": "利用可能な言語（インストール済み）:",
        "ocr_language_select_hint": "1つ以上の言語を選択してください:",
        "ocr_language_confirm": "適用",
        "ocr_language_reset": "デフォルトにリセット（deu+eng+vie）",
        "ocr_language_priorities": "推奨言語（プリインストール済み）:",

        "select_all_languages": "すべて選択",
        "clear_all_languages": "選択をクリア",
        "install_language_packs": "不足している言語パッケージをインストール...",
        "install_hint": "💡 ヒント: すべての言語がシステムにインストールされているわけではありません。このボタンからインストールヘルプを表示できます。",
        "ocr_language_install_title": "Tesseract言語パッケージのインストール",

        "ocr_missing_languages": "不足しているOCR言語パッケージ",
        "ocr_missing_languages_message": "以下の選択された言語はシステムにインストールされていません:\n\n{0}\n\n不足している言語パッケージをインストールしてください（「インストールヘルプ」のヘルプを参照）。\n\n今すぐインストールヘルプを開きますか？",
        "ocr_missing_languages_voice": "言語パッケージが不足しています。不足している言語をインストールしてください。",
        "ocr_install_help_now": "ヘルプを開く",
        "ocr_continue_anyway": "それでも試す",
        "ocr_language_error_title": "OCR言語エラー",
        "ocr_language_error_message": "テキスト認識中のエラー: {0}\n\nOCR言語設定を確認してください（設定 → OCR言語）。",
        "ocr_install_help_button": "インストールヘルプ",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract言語パッケージをインストール</p>

        <p>特定の言語でOCRを機能させるには、対応する言語データがシステムにインストールされている必要があります。お使いのオペレーティングシステムの手順に従ってください:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li><strong>ターミナル</strong>を開きます（Finder → プログラム → ユーティリティ → ターミナル）。</li>
        <li>以下のコマンドですべての利用可能な言語をインストールします:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        （数分かかる場合があります。）</li>
        <li>または個別の言語のみ（例: ベトナム語）:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        現在のHomebrewバージョンでは、<code>*.traineddata</code>を手動でダウンロードする必要がある場合があります（以下参照）。</li>
        <li>インストール後: このダイアログを閉じて、OCR言語選択を再度開きます – 新しい言語が自動的に表示されます。</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>ターミナルを開きます（Ctrl+Alt+T）。</li>
        <li>必要な言語をインストールします（例: ベトナム語）:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        重要な言語コード: <code>deu</code>（ドイツ語）、<code>eng</code>（英語）、<code>vie</code>（ベトナム語）、<code>spa</code>（スペイン語）、<code>fra</code>（フランス語）、<code>ita</code>（イタリア語）、<code>nld</code>（オランダ語）、<code>fin</code>（フィンランド語）、<code>swe</code>（スウェーデン語）、<code>nor</code>（ノルウェー語）。</li>
        <li>利用可能なすべてのパッケージを表示:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (手動)</p>
        <ol>
        <li>必要な<code>*.traineddata</code>ファイルを以下からダウンロードします:<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        （例: ベトナム語用の<code>vie.traineddata</code>）。</li>
        <li>ファイルをTesseractの言語フォルダにコピーします（通常は以下のパス）:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        （個別のインストールに応じて調整してください。）</li>
        <li>アプリケーションを再起動するか、OCR言語選択を再度開きます。</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 すべてのシステムの代替方法</p>
        <ul>
        <li>お好みのパッケージマネージャで<strong>OCRmyPDF</strong>と<strong>Tesseract</strong>をインストールします。ほとんどのインストールには既にいくつかの標準言語（英語、ドイツ語、フランス語）が含まれています。</li>
        <li>不足している言語はいつでもインストールできます – OCR言語選択には実際に存在する言語のみが表示されます。</li>
        </ul>

        <hr>
        <p><b>✅ インストール後:</b> アプリケーションの再起動は不要です – 新しく追加された言語はすぐにリストに表示されます。</p>
        <p><b>📖 言語コードのヘルプ:</b> 完全なリストは<a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseractドキュメント</a>でご覧いただけます。</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans フォント",
        "info_noto_font_voice": "Noto Sans フォントインストールガイド",
        "btn_info_noto_font_install": "フォント情報",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Googleの無料Notoフォントをインストールする方法</h2>

        <p><strong>Notoフォント</strong>は、Googleのオープンソースフォントファミリーです。その目的は、<em>"豆腐なし"</em>（つまり空のボックス□なし）を実現し、Unicode標準のすべての文字を正しく表示することです。多くの異なる言語でテキストを表示する必要があるアプリケーションに最適な追加機能です。</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 macOSへのインストール</h3>

        <p><strong>方法1: Homebrewを使用（上級者向け）</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>方法2: 「Font Book」経由（推奨）</strong></p>

        <ol>
        <li>公式フォントパッケージをダウンロード:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIPファイルを解凍</li>
        <li>ファイルを<code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code>にコピー</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Windowsへのインストール（10 & 11）</h3>

        <p><strong>方法1: Microsoft Store（推奨）</strong><br>
        "Google Noto Fonts"または"Noto Sans"を検索し、<strong>インストール</strong>をクリックします。</p>

        <p><strong>方法2: 手動インストール</strong></p>

        <ol>
        <li>ダウンロード:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIPを解凍</li>
        <li>.ttf / .otfファイルを選択</li>
        <li>右クリック → <strong>インストール</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        または<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\ユーザー名\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Linuxへのインストール</h3>

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

        <p>確認:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "ブックマークを管理",
        "bookmark_add": "ブックマークを追加",
        "bookmark_add_tooltip": "現在のページをブックマークとして保存",
        "bookmark_remove": "ブックマークを削除",
        "bookmark_remove_tooltip": "マークされたブックマークを削除",
        "bookmark_remove_all": "すべて削除",
        "bookmark_remove_all_tooltip": "このPDFのすべてのブックマークを削除",
        "bookmark_jump": "ブックマークへ移動",
        "bookmark_jump_tooltip": "選択したページへ移動",
        "bookmark_name": "名前",
        "bookmark_page": "ページ",
        "bookmark_no_bookmarks": "ブックマークがありません。\n「追加」をクリックして現在のページをブックマークとして保存します。",
        "bookmark_added": "ページ{0}のブックマークを追加しました: {1}",
        "bookmark_removed": "ブックマークを削除しました: {0}",
        "bookmark_all_removed": "すべてのブックマークが削除されました。",
        "bookmark_name_default": "ページ{0}",
        "bookmark_name_prompt": "ブックマークの名前:\n（長いテキストは50文字に短縮されます）",
        "bookmark_name_prompt_title": "ブックマーク名",
        "bookmark_confirm_remove_all": "すべての{0}個のブックマークを削除してもよろしいですか？",
        "menu_bookmarks": "ブックマーク",
        "bookmark_manage": "ブックマークを管理",
        "bookmark_next": "次のブックマーク",
        "bookmark_prev": "前のブックマーク",
        "bookmark_page_display": "ページ{0}",
        "bookmark_exists": "この名前のブックマークはこのページに既に存在します。",
        "bookmark_select_first": "最初にブックマークを選択してください。",
        "bookmark_confirm_remove": "ブックマーク「ページ{0}: {1}」を削除してもよろしいですか？",
        "bookmark_jumped_to": "ページ{1}のブックマーク「{0}」に移動しました。",
        "bookmark_jumped_to_voice": "ブックマーク{0}、ページ{1}",
        "btn_close": "閉じる",

        "bookmark_list": "あなたのブックマーク",
        "bookmark_rename": "ブックマークの名前を変更",
        "bookmark_rename_tooltip": "選択したブックマークの名前を変更",
        "bookmark_rename_title": "ブックマークの名前を変更",
        "bookmark_rename_prompt": "ページ{0}のブックマークの新しい名前:\n（最大50文字）",
        "bookmark_renamed": "ブックマーク「{0}」の名前を「{1}」に変更しました。",
        "bookmark_item_tooltip": "ページ{0}: {1}\n移動するにはダブルクリック",
        "bookmark_name_exists_question": "このページには既に「{0}」という名前のブックマークが存在します。\nそれでも名前を変更しますか？",

        "context_bookmarks": "ブックマーク",
        "context_bookmark_add_here": "このページにブックマークを追加",
        "context_bookmarks_existing": "既存のブックマーク:",
        "context_bookmarks_jump": "ブックマークへ移動:",
        "context_bookmarks_none": "ブックマークがありません",
        "context_bookmarks_clear_all": "すべての{0}個のブックマークを削除",

        "bookmark_search_placeholder": "ブックマークを検索...（名前またはページ）",
        "bookmark_search_results": "\"%s\"のブックマークが%d件見つかりました",
        "bookmark_no_search_results": "\"%s\"のブックマークは見つかりませんでした",
        "bookmark_no_search_results_label": "\"%s\"の結果はありません",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDFメタデータを編集",
        "metadata_title": "タイトル",
        "metadata_title_placeholder": "ドキュメントのタイトル",
        "metadata_title_tooltip": "ドキュメントのタイトル（タイトルバーに表示されます）",
        "metadata_author": "作成者",
        "metadata_author_placeholder": "作成者の名前",
        "metadata_author_tooltip": "ドキュメントの作成者",
        "metadata_subject": "件名",
        "metadata_subject_placeholder": "ドキュメントの件名",
        "metadata_subject_tooltip": "内容の簡単な説明",
        "metadata_keywords": "キーワード",
        "metadata_keywords_placeholder": "カンマ区切りのキーワード",
        "metadata_keywords_tooltip": "ドキュメントを分類するためのキーワード",
        "metadata_creator": "クリエイター",
        "metadata_creator_placeholder": "PDFを作成したアプリケーション",
        "metadata_creator_tooltip": "ドキュメントの作成に使用されたソフトウェア",
        "metadata_producer": "プロデューサー",
        "metadata_producer_placeholder": "PDFを変換したアプリケーション",
        "metadata_producer_tooltip": "PDFを変換したソフトウェア",
        "metadata_creation_date": "作成日",
        "metadata_creation_date_tooltip": "ドキュメントの作成日",
        "metadata_mod_date": "更新日",
        "metadata_mod_date_tooltip": "最終更新日",
        "metadata_pdf_info": "📄 PDF情報",
        "metadata_pages": "ページ数",
        "metadata_file_size": "ファイルサイズ",
        "metadata_pdf_version": "PDFバージョン",
        "metadata_encrypted": "暗号化",
        "metadata_encrypted_yes": "はい（パスワードで保護されています）",
        "metadata_encrypted_no": "いいえ",
        "metadata_reload": "📂 PDFから再読み込み",
        "metadata_reset": "変更を破棄",
        "metadata_reloaded": "メタデータがPDFから再読み込みされました。",
        "metadata_reset_done": "すべてのメタデータフィールドがリセットされました。",
        "metadata_no_file": "PDFファイルが読み込まれていません。",
        "metadata_save_error": "メタデータの保存中にエラーが発生しました",
        "metadata_saved": "メタデータが正常に保存されました。",
        "metadata_pdf_version_unknown": "PDF（不明）",
        "metadata_saved_message": "メタデータが正常に保存されました。",
        "metadata_saved_voice": "メタデータを保存しました。",

        "metadata_custom": "🔧 カスタムメタデータ",
        "metadata_custom_placeholder": "{\n  \"私のフィールド\": \"私の値\",\n  \"他のフィールド\": 123\n}",
        "metadata_custom_tooltip": "カスタムメタデータのJSON形式（オプション）",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "テンプレート「{0}」を選択しました - 挿入するにはダブルクリック",
        "text_use_template": "テキストブロックを使用",
        "text_type": "タイプ",
        "text_search_templates": "テキストブロックを検索...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 エクスポート / インポート情報",
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

        <h3>📦 何がエクスポートされますか？（概要）</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">一般アプリケーション設定</span></li>
            <li class="detail">• ダーク/ライトモード</li>
            <li class="detail">• 画像のダークモード反転</li>
            <li class="detail">• グレーしきい値</li>
            <li class="detail">• 言語</li>
            <li class="detail">• ウィンドウ形状</li>
            <li class="detail">• ズームモード</li>
            <li class="detail">• ナビゲーション（ナビバー表示）</li>
            <li class="detail">• 音声出力（オン/オフ）</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">バックアップ設定</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ファイル命名（タイムスタンプ、区切り文字、接尾辞）</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">挿入の設定</span></li>
            <li class="detail">• 署名</li>
            <li class="detail">• テキストとテキストブロック</li>
            <li class="detail">• チェック、画像、図形</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR設定</span></li>
            <li class="detail">• 言語</li>
            <li class="detail">• OCRを強制 · ページモード</li>
            <li class="detail">• 画像前処理: 傾き補正、クリーンアップ、オーバーサンプリング</li>
            <li class="detail">• 並列ジョブ数</li>
            <li class="detail">• 反転モード</li>
            <li class="detail">• グレーしきい値</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">ブックマーク</span></li>
            <li class="detail">• PDFファイルごとのすべてのブックマーク（ページ、名前、作成時間）</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">パスワードデータベース</span></li>
            <li class="detail">• 保存されたPDFパスワード（オプションで暗号化またはプレーンテキスト）</li>
            <li class="detail">• マスターパスワードハッシュ（設定されている場合）</li>
            <li class="detail">• 検証データ</li>
        </ul>

        <h4>⚠️ 重要な注意事項</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 インポート時:</strong>
            <ul>
                <li><span class="warning">➜ 現在のすべての設定が完全に上書きされます</span></li>
                <li>• アプリケーションの再起動が必要です</li>
                <li>• 既存の署名、テキストブロック、ブックマークは置き換えられます</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 マスターパスワードとエクスポートモード:</strong>
            <ul>
                <li>• マスターパスワードがアクティブな場合、選択できます:</li>
                <li>  - <span style="color: #98FB98;"><strong>復号化</strong></span>（パスワードはZIP内でプレーンテキストになります）</li>
                <li>  - <span style="color: #FFA07A;"><strong>暗号化</strong></span>（ターゲットシステムでマスターパスワードを使用した場合のみ読み取り可能）</li>
                <li>• マスターパスワードハッシュ自体は<strong>常に</strong>暗号化されて保存されます</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ セキュリティ通知:</strong>
            <ul>
                <li>• エクスポートされたZIPファイルには機密データ（<strong>パスワード、ブックマーク、署名</strong>）が含まれています</li>
                <li>• 安全な場所に保管してください（例: 暗号化USBメモリ、パスワードマネージャー）</li>
                <li>• ファイルを失うと、保存されたPDFパスワードは回復不能に失われます</li>
            </ul>
        </div>

        <h4>📁 エクスポート形式</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            設定は1つのZIPファイルに保存されます:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            このZIPには、完全な<code>settings.json</code>（設定から）と、埋め込まれた署名画像ファイルや暗号化されたパスワードが含まれています。
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "署名 - ガイド",
        'signature_guide_html': """
        📝 <strong>署名 - クイックガイド</strong><br>
        <ul>
        <li>マスターパスワードを設定する</li>
        <li><em>設定</em>メニューで署名を設定する（サイズ、タイムスタンプなど）</li>
        <li>希望の位置で<strong>右クリック</strong>して挿入（セッションごとにマスターパスワードが1回必要）</li>
        <li>マウスまたは矢印キーで署名を移動する</li>
        <li>複数の署名を連続して挿入する</li>
        <li>各署名を個別にカスタマイズする</li>
        <li>単一の署名を破棄する</li>
        <li>すべての署名を一度に保存/破棄する</li>
        <li>代わりにメニューバーも使用できます。</li>
        </ul>
        """,
        'signature_guide_voice': "署名のクイックガイド。マスターパスワードを設定。設定で署名を設定。右クリックで挿入。",

        'image_guide_title': "画像挿入 - ガイド",
        'image_guide_html': """
        📷 <strong>PDFに画像を挿入 - クイックガイド</strong><br>
        <ol>
        <li>希望の位置で右クリック</li>
        <li><em>„画像を挿入“</em> → 画像を選択</li>
        <li>画像を配置：マウスでドラッグ</li>
        <li>サイズ調整：隅/端でドラッグ</li>
        <li>アスペクト比を維持：<strong>[A]</strong>キー</li>
        <li>その他の調整：画像上で右クリック</li>
        </ol>
        <p><strong>ヒント：</strong>コンテキストメニューで設定を調整できます。</p>
        """,
        'image_guide_voice': "画像のクイックガイド。右クリック、画像挿入、選択。マウスで配置、隅でサイズ調整。Aキーでアスペクト比。",

        'form_guide_title': "図形挿入 - ガイド",
        'form_guide_html': """
        📐 <strong>PDFに図形を挿入 - クイックガイド</strong><br>
        <ol>
        <li>図形タイプを選択（長方形、楕円、線、矢印）</li>
        <li>位置をクリック：
            <ul>
            <li>長方形/楕円の場合：ワンクリックで図形を配置</li>
            <li>線/矢印の場合：始点と終点に2回クリック</li>
            </ul>
        </li>
        <li>図形を配置：マウスでドラッグ</li>
        <li>サイズ調整：隅/端でドラッグ</li>
        <li>図形を保存：<strong>Enter</strong></li>
        <li>図形を破棄：<strong>ESC</strong></li>
        <li>その他の調整：図形上で右クリック</li>
        </ol>
        <p><strong>ヒント：</strong>コンテキストメニューで設定を調整できます。</p>
        """,
        'form_guide_voice': "図形のクイックガイド。図形タイプを選択。長方形または楕円は1回クリック、線または矢印は2回クリック。マウスで配置、隅でサイズ調整。Enterで保存、Escapeで破棄。",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "前へ",
        "btn_next_result": "次へ",
        "ocr_text_window": "OCRテキストウィンドウ",
        "bookmark_existing": "既存のブックマーク",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR比較 Mac - Windows",
        'ocr_method_mac_win_title': "MacとWindowsのOCRの違い",
        'ocr_method_mac_win_voice': "Macの方が優れている",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – macOSとWindowsの違い</strong></p>

        <p><strong>macOS（推奨）</strong></p>
        <p>ツール：</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>結果：</p>
        <ul>
        <li>元のレイアウトをほぼ維持した、埋め込みテキスト付きの検索可能なPDF。</li>
        </ul>
        <p>利点：</p>
        <ul>
        <li>優れたテキスト認識品質（歪んだページでも）。</li>
        <li>ベクターグラフィックスとフォントの保持。</li>
        <li>サブプロセス評価によるGUI進行バー。</li>
        <li>すべてのOCRパラメータを完全に制御（Deskew、Clean、Oversample、最適化）。</li>
        <li>テキスト検索はメインウィンドウ（PDF表示）で直接利用可能。</li>
        </ul>
        <p>欠点：</p>
        <ul>
        <li>追加のシステムツールが必要（ocrmypdf、Ghostscript、unpaper、pngquant – アプリバンドルに含まれています）。</li>
        <li>より複雑なエラー処理（デッドロック、タイムアウト）。</li>
        </ul>

        <p><strong>Windows（安定した代替案）</strong></p>
        <p>ツール：</p>
        <ul>
        <li>pytesseract（Tesseractへの直接接続）+ reportlab + PyPDF2</li>
        </ul>
        <p>結果：</p>
        <ul>
        <li>視覚的には画像PDFに相当するが、透明テキストを通じて検索可能なPDF。</li>
        </ul>
        <p>利点：</p>
        <ul>
        <li>今のところ思いつきません。</li>
        </ul>
        <p>欠点：</p>
        <ul>
        <li>PDFは本質的に不可視テキスト付きの画像です。複雑なドキュメント（列、表）ではレイアウトがわずかにずれることがあります。</li>
        <li>自動傾き補正（--deskew）や画像クリーンアップ（--clean）はありません。</li>
        <li>GUI進行バーは処理されたページ数に基づいて大まかにのみ更新されます。</li>
        <li>OCR速度はわずかに遅い（各ページが個別に処理されるため）。</li>
        <li>テキスト検索はOCRテキストウィンドウにリダイレクトされます。</li>
        </ul>

        <p><strong>共通点</strong></p>
        <ul>
        <li>どちらの方法も、ソースファイルと同じディレクトリに検索可能なPDFを作成します。</li>
        <li>OCR設定（言語、DPI、ページセグメンテーションモード、OCRエンジンモード）はOCRSettingsDialogを介して構成でき、両方の実装で有効です。</li>
        </ul>

        <p><strong>推奨：</strong></p>
        <ul>
        <li>macOS：ocrmypdfバイナリが最高の結果を提供します – Macを購入してバージョンを使用してください（Apple SiliconまたはIntelチップを搭載したMac用のPDFDarkView）。OCR結果はWindowsよりも優れています！</li>
        <li>Windows：pytesseractソリューションを使用してください。安定しており、ほとんどのドキュメントに十分な品質を提供します。</li>
        </ul>

        <p><strong>重要な注意：</strong></p>
        <ul>
        <li>どちらのバージョンもユーザーインターフェースに完全に統合されています – ユーザーは違いに気づきません。</li>
        <li>プログラムはオペレーティングシステムに基づいて自動的に使用するOCRエンジンを決定します。</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "署名を作成（スキャンから）",
        "signature_create_title": "スキャンした署名を選択（PDF/画像）",
        "image_pdf_filter": "画像とPDF",
        "signature_pdf_empty": "PDFにページがありません。",
        "signature_created_success": "署名が正常に作成されました: {0}",
        "signature_create_error": "署名作成中のエラー:\n{0}",
        "rembg_missing": "rembgがインストールされていません。\nインストールしてください: pip install rembg\nエラー: {0}",
        "signature_name_title": "署名のファイル名",
        "signature_name_message": "新しい署名のファイル名を入力してください（透明な背景のPNGとして保存されます）:",
        "signature_name_label": "ファイル名:",
        "signature_name_voice": "署名のファイル名を入力",
        "signature_processing": "処理中...",
        "signature_creation_title": "署名を作成中",
        "signature_overwrite_warning": "ファイル '{0}' は既に存在します。上書きしますか？",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"署名用にPDFを準備",
        "signature_prepare_instruction":"1ページにスキャンされた署名を含むPDFを選択してください。\n\n最適な認識を得るには、以下の条件を満たしている必要があります：\n• 署名が白い紙に黒インク（ボールペンまたは細いフェルトペン）で書かれている。\n• 署名がそれ以外は空白のA4ページの上部3分の1にある。\n• PDFが少なくとも300 dpiでスキャンされている。\n• 署名が明確で細すぎない。\n• 邪魔な背景パターンや線がない。",
        "signature_prepare_voice":"スキャンされた署名を含むPDFを選択してください。品質とコントラストに注意してください。",
        "sig_thickness_label":"線の太さ:",
        "sig_thickness_normal":"標準（細い）",
        "sig_thickness_bold":"太い（推奨）",
        "sig_thickness_very_bold":"非常に太い",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUIとOCR言語を追加 - ガイド",
        'language_guide_title': "GUIとOCR言語を追加",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>希望する翻訳ファイル <code>translations_xy.py</code> を以下からダウンロードし<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        次のディレクトリに配置してください：</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Webブラウザを開きます。</li>
        <li>次のURLに移動します： <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>画面右端の「Releases」を探し、<strong>"latest"</strong>とマークされたものを選択します。</li>
        <li>次のリリースページで、一番下にある <code>Source Code.zip</code> ファイルをダウンロードします。</li>
        <li>ZIPファイルを解凍します。</li>
        <li>解凍したフォルダ内で必要な言語ファイルをすべて見つけ、次のディレクトリにコピーします：<br/>
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
        "menu_watermark":"透かしの挿入",
        "fullpage_text_watermark_title":"テキストを透かしとして",
        "fullpage_image_watermark_title":"画像を透かしとして",
        "filename_with_watermark":"_透かし付き",
        "watermark_text":"テキスト:",
        "watermark_text_placeholder":"透かしテキスト...",
        "watermark_font_family":"フォント:",
        "watermark_font_size":"フォントサイズ:",
        "watermark_format":"書式:",
        "watermark_bold":"太字",
        "watermark_italic":"斜体",
        "watermark_color":"色:",
        "watermark_choose_color":"色を選択...",
        "watermark_opacity":"不透明度 / 透明度:",
        "watermark_direction":"読み方向:",
        "watermark_direction_l_r":"左 → 右",
        "watermark_direction_bl_tr":"左下 → 右上",
        "watermark_direction_tl_br":"左上 → 下",
        "watermark_direction_b_t":"下 → 上",
        "watermark_direction_t_b":"上 → 下",
        "watermark_preview":"プレビュー:",
        "watermark_preview_sample":"サンプルテキスト",
        "watermark_empty_text":"テキストを入力してください。",
        "watermark_applied":"すべてのページに透かしが適用されました。",
        "watermark_saved":"透かしを保存しました。",
        "image_scale":"サイズ:",
        "image_preview":"画像プレビュー:",
        "no_image_selected":"画像が選択されていません",
        "browse":"参照...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "墨消し",
        "redact_add_black": "墨消し（黒）",
        "redact_add_white": "墨消し（白 / 消去）",
        "redact_added_black": "黒の墨消しを追加しました",
        "redact_added_white": "白の墨消しを追加しました",
        "redact_apply_all": "すべての墨消しを適用して保存",
        "redact_discard_all": "すべての墨消しを破棄",
        "redact_discard": "この墨消しを破棄",
        "no_redactions": "墨消しはありません",
        "redact_confirm_title": "墨消しを永続的に適用",
        "redact_confirm_message": "警告: マークされた領域は永久に削除されます（黒または白）。\nバックアップが作成されます（有効な場合）。\n\n続行しますか？",
        "redact_apply": "はい、今すぐ墨消し",
        "redact_saved": "{0}件の墨消しを適用して保存しました。",
        "redact_saved_voice": "{0}件の墨消しを適用",
        "redact_error": "墨消し中にエラーが発生しました",
        "filename_redacted":"_墨消し済み",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'ページ番号の挿入',
        'page_numbers_format': '番号形式:',
        'page_numbers_format_arabic': '1, 2, 3 ...（アラビア数字）',
        'page_numbers_format_roman_lower': 'i, ii, iii ...（ローマ数字小文字）',
        'page_numbers_format_roman_upper': 'I, II, III ...（ローマ数字大文字）',
        'page_numbers_format_letter': 'A, B, C ...（アルファベット）',
        'page_numbers_format_custom': 'カスタム',
        'page_numbers_custom_pattern': 'パターン:',
        'page_numbers_custom_placeholder': '例: "ページ {nummer}" または "{nummer} / {total}"',
        'page_numbers_custom_tooltip': '現在のページ番号には {nummer}、合計には {total} を使用します',
        'page_numbers_position': '位置:',
        'page_numbers_pos_tl': '左上',
        'page_numbers_pos_tc': '上中央',
        'page_numbers_pos_tr': '右上',
        'page_numbers_pos_ml': '左中央',
        'page_numbers_pos_mc': '中央',
        'page_numbers_pos_mr': '右中央',
        'page_numbers_pos_bl': '左下',
        'page_numbers_pos_bc': '下中央',
        'page_numbers_pos_br': '右下',
        'page_numbers_margins': 'マージン:',
        'page_numbers_margin_x': '水平距離:',
        'page_numbers_margin_y': '垂直距離:',
        'page_numbers_range': 'ページ範囲:',
        'page_numbers_all_pages': 'すべてのページ',
        'page_numbers_custom_range': 'カスタム範囲',
        'page_numbers_from': '開始:',
        'page_numbers_to': '終了:',
        'page_numbers_progress': 'ページ番号を挿入中...',
        'page_numbers_start': 'ページ番号の挿入を開始...',
        'page_numbers_cancel': 'ページ番号の挿入をキャンセルしました',
        'page_numbers_success': 'ページ番号が正常に追加されました。\n\n新しいPDFを開きますか？\n\n{0}',
        'page_numbers_complete': 'ページ番号を追加しました',
        'page_numbers_error_format': 'ページ番号の挿入中にエラーが発生しました: {0}',
        'page_numbers_content_type': 'コンテンツタイプ:',
        'page_numbers_tab_simple': 'シンプルな番号',
        'page_numbers_tab_range': 'ページ X / Y',
        'page_numbers_tab_date': '日付',
        'page_numbers_tab_custom': 'フリーテキスト',
        'page_numbers_range_format': '形式:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'ページ {aktuell} / {gesamt}',
        'page_numbers_range_custom': 'カスタム',
        'page_numbers_range_placeholder': '例: "ページ {aktuell} / {gesamt}"',
        'page_numbers_date_format': '日付形式:',
        'page_numbers_date_short': '2024.01.01',
        'page_numbers_date_long': '2024年1月1日',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'カスタム',
        'page_numbers_date_placeholder': '例: %Y年%m月%d日 %H:%M',
        'page_numbers_date_position': '位置:',
        'page_numbers_date_before': 'ページ番号の前に日付',
        'page_numbers_date_after': 'ページ番号の後に日付',
        'page_numbers_date_only': '日付のみ（ページ番号なし）',
        'page_numbers_custom_text': 'カスタムテキスト:',
        'page_numbers_custom_placeholder_text': 'ページ番号には {seite}、合計には {gesamt} を使用します\n例: "機密 - ページ {seite}" または "{seite} / {gesamt}"',
        "filename_with_page_number":"_ページ番号付き",
        "filename_with_page_declaration":"_ページ宣言付き",
        "filename_with_pagenumber":"_ページ番号付き",
        "filename_with_date":"_日付付き",
        "filename_with_my_page_declaration":"_カスタムページ宣言付き",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "未保存の変更",
        "unsaved_changes_message_darkmode": "未保存の挿入があります。\n切り替える前に保存しますか？",
        "save_and_switch": "保存して切り替え",
        "discard_and_switch": "今すぐ切り替え",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'ページを画像としてエクスポート',
        'export_images_menu': '画像としてエクスポート（PNG/JPEG）',
        'export_images_format': '画像形式:',
        'export_images_dpi': '解像度（DPI）:',
        'export_images_quality': 'JPEG品質:',
        'export_images_range': 'ページ範囲:',
        'export_images_all_pages': 'すべてのページ',
        'export_images_custom_range': 'カスタム範囲',
        'export_images_from': '開始:',
        'export_images_to': '終了:',
        'export_images_options': 'オプション:',
        'export_images_single_files': '各ページを個別ファイルとして',
        'export_images_subfolder': 'サブフォルダにエクスポート',
        'export_images_subfolder_info': 'サブフォルダ "PDF名_画像" へ',
        'export_images_same_folder': 'PDFと同じフォルダ',
        'export_images_apply_darkmode': 'PDFDarkView設定を適用（ダークモード）',
        'export_images_target_folder': '出力先フォルダ:',
        'export_images_browse': '参照...',
        'export_images_preview': 'プレビュー:',
        'export_images_preview_info': 'エクスポート設定を選択',
        'export_images_preview_info_detail': '{0} ページを {1} として\n解像度: {2} DPI\nファイル名: {3}\n{4}',
        'export_images_select_folder': '出力先フォルダを選択',
        'export_images_start': '画像エクスポートを開始...',
        'export_images_progress': '画像をエクスポート中...',
        'export_images_saving': 'ページ {0}/{1} を保存中...',
        'export_images_success': 'エクスポート成功！\n\n{0}枚の画像を保存しました:\n{1}',
        'export_images_complete': '画像エクスポート完了',
        'export_images_open_folder': '📁 フォルダを開く',
        'export_images_cancel': '画像エクスポートをキャンセルしました',
        'export_images_error_format': '画像エクスポート中にエラーが発生しました: {0}',
        'export_images_pdf2image_missing': 'ライブラリ "pdf2image" がインストールされていません。\n\n以下のコマンドでインストールしてください:\npip install pdf2image\n\nWindowsの場合はPopplerも必要です:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': '長期保存用PDF/A変換',
        'pdfa_menu': 'PDF/A変換（アーカイブ対応）',
        'pdfa_info': 'PDFをPDF/A形式に変換します。\n\nPDF/Aは長期保存用に特別に設計されており、将来にわたってドキュメントが正しく表示されることを保証します。',
        'pdfa_standard': 'PDF/A規格:',
        'pdfa_standard_select': 'バージョン:',
        'pdfa_1': 'PDF/A-1（シンプル、広く互換性あり）',
        'pdfa_2': 'PDF/A-2（モダン、圧縮性能向上）',
        'pdfa_3': 'PDF/A-3（最新版、添付ファイル許可）',
        'pdfa_standards_explanation': '📖 規格の説明:\n\n'
            '• PDF/A-1: 基本、旧システムと互換性あり（2005年頃）\n'
            '• PDF/A-2: よりモダン、圧縮性能向上、透明度サポート（2011年頃）\n'
            '• PDF/A-3: 最新版、ファイル添付の埋め込みを許可（2013年頃）\n\n'
            '推奨: PDF/A-2は互換性とモダンな機能のバランスが良いです。',
        'pdfa_options': 'オプション:',
        'pdfa_compress_enable': 'PDFを圧縮（ファイルサイズを小さく）',
        'pdfa_metadata_preserve': 'メタデータを保持（タイトル、作者など）',
        'pdfa_target_folder': '出力先フォルダ:',
        'pdfa_browse': '参照...',
        'pdfa_select_folder': '出力先フォルダを選択',
        'pdfa_ocr_info_unknown': '🔍 テキスト内容を確認できませんでした。',
        'pdfa_ocr_info_not_needed': '✅ テキストあり - OCRは不要です。\nPDF/Aを直接作成できます。',
        'pdfa_ocr_info_recommended': '⚠️ 十分なテキストが見つかりませんでした。\n\n検索可能なPDFにするには、先にOCRを実行することをお勧めします。\n注: OCRなしでもPDF/Aは機能しますが、テキストは検索できません。',
        'pdfa_ocr_info_error': '❌ 確認中にエラーが発生しました: {0}',
        'pdfa_start': 'PDF/A変換を開始...',
        'pdfa_progress': 'PDF/A変換を実行中...',
        'pdfa_success': 'PDF/A変換成功！\n\n保存先:\n{0}\n\n新しいPDFを開きますか？',
        'pdfa_complete': 'PDF/A変換完了',
        'pdfa_cancel': 'PDF/A変換をキャンセルしました',
        'pdfa_error_format': 'PDF/A変換中にエラーが発生しました:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'ライブラリ "ocrmypdf" がインストールされていません。\n\n以下のコマンドでインストールしてください:\npip install ocrmypdf',
        'btn_convert': '変換',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'PDF最適化（ファイルサイズ削減）',
        'optimize_menu': 'PDF最適化（ファイルサイズ）',
        'optimize_info': '様々な最適化手法によりPDFファイルのサイズを削減します。\n\n圧縮レベルが高いほどファイルは小さくなりますが、画像品質が低下する可能性があります。',
        'optimize_level': '圧縮レベル:',
        'optimize_level_low': '低（高速、わずかな削減）',
        'optimize_level_medium': '中（バランス良好）',
        'optimize_level_high': '高（大幅な削減）',
        'optimize_level_maximum': '最大（最大限の削減、低速）',
        'optimize_level_explanation': '推奨: "中"は速度とファイルサイズのバランスが良いです。',
        'optimize_options': 'オプション:',
        'optimize_compress_images': '画像を圧縮（JPEG品質を低下）',
        'optimize_clean_objects': '未使用オブジェクトを削除',
        'optimize_preserve_metadata': 'メタデータを保持（タイトル、作者など）',
        'optimize_image_quality': '画像品質:',
        'optimize_range': 'ページ範囲:',
        'optimize_all_pages': 'すべてのページ',
        'optimize_custom_range': 'カスタム範囲',
        'optimize_from': '開始:',
        'optimize_to': '終了:',
        'optimize_target_folder': '出力先フォルダ:',
        'optimize_browse': '参照...',
        'optimize_select_folder': '出力先フォルダを選択',
        'optimize_info_box': '情報',
        'optimize_info_text': '大きなPDFでは最適化に数分かかる場合があります。\n\n画像は品質を落として保存され、ファイルサイズを大幅に削減できます。',
        'optimize_start': 'PDF最適化を開始...',
        'optimize_progress': 'PDFを最適化中...',
        'optimize_cancel': 'PDF最適化をキャンセルしました',
        'optimize_complete': 'PDF最適化完了',
        'optimize_error_format': 'PDF最適化中にエラーが発生しました:\n\n{0}',
        'optimize_success_message': 'PDF最適化成功！\n\n保存先:\n{0}\n\n最適化前: {1}\n最適化後: {2}\n削減率: {3:.1f}%\n\n{4}\n\n最適化したPDFを開きますか？',
        'optimize_success_message_no_size': 'PDF最適化成功！\n\n保存先:\n{0}\n\nサイズ情報が利用できません。\n\n最適化したPDFを開きますか？',
        'optimize_result_positive': 'ファイルサイズが {0:.1f}% 削減されました。',
        'optimize_result_zero': 'ファイルサイズに変化はありませんでした。',
        'optimize_result_negative': 'ファイルサイズが {0:.1f}% 増加しました。\n最適化をスキップし、元のファイルを保持しました。',
        'btn_optimize': '最適化を開始',
        'filename_optimize_low_suffix': '_最適化_低',
        'filename_optimize_medium_suffix': '_最適化',
        'filename_optimize_high_suffix': '_最適化_高',
        'filename_optimize_maximum_suffix': '_最適化_最大',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'PDFを切り抜き',
        'crop_menu': 'PDFを切り抜き（クロップ）',
        'crop_range': '適用先:',
        'crop_all_pages': 'すべてのページ',
        'crop_current_page': '現在のページのみ',
        'crop_values': '切り抜き値（ポイント単位）:',
        'crop_left': '左:',
        'crop_right': '右:',
        'crop_top': '上:',
        'crop_bottom': '下:',
        'crop_presets': 'プリセット:',
        'crop_preset_white': '白い余白を検出',
        'crop_reset': 'リセット',
        'crop_mouse_hint': '🖱️ 矩形をドラッグしておおよその範囲を選択します。\nその後、スピンボックスで値を正確に調整できます。\nマウスでの手動調整はできません。',
        'crop_apply': '切り抜き',
        'crop_scope_all': 'すべてのページ',
        'crop_scope_current': '現在のページ',
        'crop_new_size': '新しいサイズ: {0:.0f} × {1:.0f} pt',
        'crop_no_pdf': 'PDFが読み込まれていません',
        'crop_preview_error': 'プレビューの読み込み中にエラーが発生しました',
        'crop_start': '切り抜きを開始...',
        'crop_progress': 'PDFを切り抜き中...',
        'crop_success': 'PDFの切り抜き成功！\n\n保存先:\n{0}\n\n切り抜いたPDFを開きますか？',
        'crop_complete': '切り抜き完了',
        'crop_cancel': '切り抜きをキャンセルしました',
        'crop_error_format': '切り抜き中にエラーが発生しました:\n\n{0}',
        'filename_crop_suffix': '_切り抜き',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'PDFをフラット化（Flatten）',
        'flatten_menu': 'PDFをフラット化（Flatten）',
        'flatten_info': 'PDFをフラット化すると、すべての編集可能な要素がページコンテンツに「焼き付け」られます。\n\nその後、フォームフィールド、注釈、テキスト、十字、署名、画像、図形は個別に編集できなくなります。',
        'flatten_explanation_title': '📖 これは何に役立ちますか？',
        'flatten_explanation_text': 'フラット化は以下の状況で必要です:\n\n'
            '• 📄 ドキュメントを印刷用に準備したい\n'
            '• 🔒 誰かがフォームフィールドを変更するのを防ぎたい\n'
            '• 📎 注釈やコメントをドキュメントに「永続的に」埋め込みたい\n'
            '• 🖼️ 挿入したテキスト、十字、署名、画像、図形をドキュメントに永続的に固定したい\n'
            '• 📦 ファイルをアーカイブ用に準備したい\n\n'
            'フラット化によりPDFが小さくなり、要素が誤って移動または削除されるのを防ぎます。',
        'flatten_what_title': '何がフラット化されますか？',
        'flatten_what_list': '• ✅ フォームフィールド（テキストフィールド、チェックボックス、ボタン）\n'
            '• ✅ 注釈（コメント、ハイライト、ノート）\n'
            '• ✅ オーバーレイ（テキスト、十字、署名、画像、図形）',
        'flatten_options': 'オプション:',
        'flatten_forms': 'フォームフィールドをフラット化',
        'flatten_annotations': '注釈をフラット化',
        'flatten_overlays': 'オーバーレイをフラット化（テキスト、十字、署名、画像、図形）',
        'flatten_target_folder': '出力先フォルダ:',
        'flatten_browse': '参照...',
        'flatten_select_folder': '出力先フォルダを選択',
        'flatten_warning': '⚠️ 重要: フラット化は元に戻せない処理です！\n\nフラット化後、編集可能な要素は個別に変更または削除できなくなります。\n必要に応じて事前にバックアップを作成してください。',
        'flatten_apply': 'フラット化',
        'flatten_start': 'フラット化を開始...',
        'flatten_progress': 'PDFをフラット化中...',
        'flatten_success': 'PDFのフラット化成功！\n\n保存先:\n{0}\n\nフラット化したPDFを開きますか？',
        'flatten_complete': 'フラット化完了',
        'flatten_cancel': 'フラット化をキャンセルしました',
        'flatten_error_format': 'フラット化中にエラーが発生しました:\n\n{0}',
        'filename_flatten_suffix': '_フラット化',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDFオーバーレイ（Overlay）',
        'overlay_menu': 'PDFオーバーレイ（Overlay）',
        'overlay_info': 'あるPDF（オーバーレイ）を別のPDFの上に配置します。\n\nオーバーレイPDFはベースPDFの上に配置されます。これは透かし、ロゴ、レターヘッド、スタンプに便利です。',
        'overlay_explanation_title': '📖 これは何に役立ちますか？',
        'overlay_explanation_text': 'オーバーレイは以下の状況で必要です:\n\n'
            '• 🏢 会社のロゴを透かしとして各ページに配置\n'
            '• 📄 空のPDFにレターヘッドを配置\n'
            '• 🖊️ ドキュメントにスタンプオーバーレイを配置\n'
            '• 🔖 すべてのページに透かしを配置\n'
            '• 📑 テンプレートにフォームオーバーレイを配置',
        'overlay_type': 'オーバーレイタイプ:',
        'overlay_type_fullpage': '全ページ（カバー）',
        'overlay_type_transparent': '全ページ（透明 - 推奨）',
        'overlay_type_stamp': 'スタンプ（位置指定可能）',
        'overlay_type_info_fullpage': '📄 オーバーレイPDFがページ全体に正確に配置されます。\n白い背景を除去して、コンテンツのみを表示できます。',
        'overlay_type_info_transparent': '🔍 オーバーレイPDFが透明な背景でページ全体に配置されます。\n白い背景が自動的に除去されます - 透かしやロゴに最適！',
        'overlay_type_info_stamp': '🖊️ オーバーレイPDFがスタンプとして位置決め・スケーリングされます。\n特定の位置でのロゴ、スタンプ、署名に最適です。',
        'overlay_remove_background': '白い背景を除去:',
        'overlay_remove_background_enable': 'オーバーレイPDFから白い背景を除去（オーバーレイを透明化）',
        'overlay_remove_background_tooltip': 'オーバーレイPDFから白い領域を除去し、下のテキストが見えるようにします。',
        'overlay_threshold': 'しきい値:',
        'overlay_threshold_hint': '(1-254、数値が高いほど多くの白が除去されます)',
        'overlay_select_file': 'オーバーレイPDFを選択:',
        'overlay_file_placeholder': 'オーバーレイ用のPDFファイルを選択してください',
        'overlay_browse': '参照...',
        'overlay_select_overlay': 'オーバーレイPDFを選択',
        'overlay_range': 'ページ範囲:',
        'overlay_all_pages': 'すべてのページ',
        'overlay_custom_range': 'カスタム範囲',
        'overlay_from': '開始:',
        'overlay_to': '終了:',
        'overlay_position': '位置:',
        'overlay_position_center': '中央',
        'overlay_position_top_left': '左上',
        'overlay_position_top_right': '右上',
        'overlay_position_bottom_left': '左下',
        'overlay_position_bottom_right': '右下',
        'overlay_size': 'サイズ:',
        'overlay_size_original': '元のサイズ',
        'overlay_size_fit_page': 'ページに合わせる',
        'overlay_size_custom': 'カスタム（%）',
        'overlay_opacity': '透明度:',
        'overlay_target_folder': '出力先フォルダ:',
        'overlay_browse_folder': '参照...',
        'overlay_select_folder': '出力先フォルダを選択',
        'overlay_warning': '⚠️ 注記: オーバーレイPDFがベースPDFの上に配置され、「焼き付け」られます。\n\n保存後、オーバーレイPDFの要素は個別に編集できなくなります。',
        'overlay_apply': 'オーバーレイ',
        'overlay_start': 'オーバーレイを開始...',
        'overlay_progress': 'PDFをオーバーレイ中...',
        'overlay_success': 'PDFオーバーレイ成功！\n\n保存先:\n{0}\n\nオーバーレイしたPDFを開きますか？',
        'overlay_complete': 'オーバーレイ完了',
        'overlay_cancel': 'オーバーレイをキャンセルしました',
        'overlay_error_format': 'オーバーレイ中にエラーが発生しました:\n\n{0}',
        'overlay_no_file': 'オーバーレイPDFが選択されていません。\n\nオーバーレイするPDFファイルを選択してください。',
        'filename_overlay_suffix': '_オーバーレイ',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'PDFから画像を抽出',
        'extract_images_menu': 'すべての画像を抽出',
        'extract_images_info': 'PDFからすべての画像を抽出し、個別のファイルとして保存します。\n\n画像は元の形式で保存されるか、選択した形式に変換されます。',
        'extract_images_format': '画像形式:',
        'extract_images_quality': 'JPEG品質:',
        'extract_images_options': 'オプション:',
        'extract_images_subfolder': 'サブフォルダに抽出（"PDF名_画像"）',
        'extract_images_unique': 'ユニークな画像のみ（重複を回避）',
        'extract_images_range': 'ページ範囲:',
        'extract_images_all_pages': 'すべてのページ',
        'extract_images_custom_range': 'カスタム範囲',
        'extract_images_from': '開始:',
        'extract_images_to': '終了:',
        'extract_images_target_folder': '出力先フォルダ:',
        'extract_images_browse': '参照...',
        'extract_images_select_folder': '出力先フォルダを選択',
        'extract_images_info_box': '情報',
        'extract_images_info_text': '大きなPDFでは抽出に数分かかる場合があります。\n\n画像は元の名前（ページ_画像）で保存されます。',
        'extract_images_extract': '抽出',
        'extract_images_start': '抽出を開始...',
        'extract_images_progress': '画像を抽出中...',
        'extract_images_success': '✅ 画像抽出成功！\n\n{0}枚の画像を保存しました:\n{1}',
        'extract_images_complete': '画像抽出完了',
        'extract_images_cancel': '抽出をキャンセルしました',
        'extract_images_error_format': '画像抽出中にエラーが発生しました:\n\n{0}',
        'extract_images_open_folder': '📁 フォルダを開く',
        'extract_images_no_images': 'PDFに画像が見つかりませんでした。',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': '1ページに複数ページ（N-Up）',
        'nup_menu': '1ページに複数ページ（N-Up）',
        'nup_info': '複数のPDFページを1ページに配置します。\n\nコンパクトな印刷、概要、配布資料に最適です。',
        'nup_layout': 'レイアウト:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'プレビュー:',
        'nup_preview_info': '{0} ページ → 1枚あたり {1} ページ → {2} 枚\nレイアウト: {3}',
        'nup_order': '順序:',
        'nup_order_horizontal': '水平（行順）',
        'nup_order_vertical': '垂直（列順）',
        'nup_order_horizontal_reverse': '水平逆順',
        'nup_order_vertical_reverse': '垂直逆順',
        'nup_range': 'ページ範囲:',
        'nup_all_pages': 'すべてのページ',
        'nup_custom_range': 'カスタム範囲',
        'nup_from': '開始:',
        'nup_to': '終了:',
        'nup_options': 'オプション:',
        'nup_margins': 'マージン:',
        'nup_margin_between': 'ページ間の間隔:',
        'nup_page_numbers': 'ページ番号を挿入',
        'nup_target_folder': '出力先フォルダ:',
        'nup_browse': '参照...',
        'nup_select_folder': '出力先フォルダを選択',
        'nup_create': '作成',
        'nup_start': 'N-Upを開始...',
        'nup_progress': 'N-Upを作成中...',
        'nup_success': 'N-Up作成成功！\n\n保存先:\n{0}\n\n新しいPDFを開きますか？',
        'nup_complete': 'N-Up完了',
        'nup_cancel': 'N-Upをキャンセルしました',
        'nup_error_format': 'N-Up中にエラーが発生しました:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'ページサイズ変更',
        'pagesize_menu': 'ページサイズ変更',
        'pagesize_info': 'PDFのページサイズを変更します。\n\nコンテンツは自動的に新しいサイズに適応されます。',
        'pagesize_format': '形式:',
        'pagesize_select': '標準形式を選択:',
        'pagesize_custom': 'カスタムサイズ:',
        'pagesize_width': '幅:',
        'pagesize_height': '高さ:',
        'pagesize_orientation': '向き:',
        'pagesize_portrait': '縦向き',
        'pagesize_landscape': '横向き',
        'pagesize_scale_options': 'スケーリングオプション:',
        'pagesize_fit': '調整（アスペクト比を維持）',
        'pagesize_stretch': '伸縮（歪み）',
        'pagesize_center': '中央揃え（元のサイズ）',
        'pagesize_range': 'ページ範囲:',
        'pagesize_all_pages': 'すべてのページ',
        'pagesize_custom_range': 'カスタム範囲',
        'pagesize_from': '開始:',
        'pagesize_to': '終了:',
        'pagesize_target_folder': '出力先フォルダ:',
        'pagesize_browse': '参照...',
        'pagesize_select_folder': '出力先フォルダを選択',
        'pagesize_apply': '適用',
        'pagesize_start': 'ページサイズ変更を開始...',
        'pagesize_progress': 'ページサイズを変更中...',
        'pagesize_success': 'ページサイズ変更成功！\n\n保存先:\n{0}\n\n新しいPDFを開きますか？',
        'pagesize_complete': 'ページサイズ変更完了',
        'pagesize_cancel': 'ページサイズ変更をキャンセルしました',
        'pagesize_error_format': 'ページサイズ変更中にエラーが発生しました:\n\n{0}',
        'pagesize_preview_info': '新しいサイズ: {0} × {1} pt',
        'filename_pagesize_suffix': '_新しいサイズ',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF情報',
        'pdf_info_menu': 'PDF情報を表示',
        'pdf_info_voice': 'PDF情報を表示中',
        'pdf_info_error': 'PDF情報の表示中にエラーが発生しました:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "キーボードショートカットを表示",
        "shortcuts_dialog_title": "キーボードショートカット",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 ファイル</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDFを開く</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDFを閉じる</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>名前を付けて保存...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>ドキュメントを保護</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>印刷</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>すぐに印刷（macOS）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>アプリケーションを終了</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 エクスポート</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Pagesとしてエクスポート</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>DOCXとしてエクスポート</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>TXTとしてエクスポート</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>画像としてエクスポート（macOS）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>画像を抽出</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ ドキュメント処理</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up（複数ページ）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A変換（macOS）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDFをフラット化</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDFオーバーレイ</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF最適化</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ 編集</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>検索</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>ブックマークを追加</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>ブックマークを管理</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>次のブックマーク</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>前のブックマーク</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCRを実行</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 ページ管理</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>現在のページを回転</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>すべてのページを回転</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>現在のページを正規化</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>すべてのページを正規化</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ページを削除</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>ページを抽出</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>ページを挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>ページを移動</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDFを結合</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>ページサイズを変更</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 挿入</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>テキストを挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>十字を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>署名1を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>署名2を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>画像を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>長方形を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>楕円を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>線を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>矢印を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>ページ番号を挿入</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>テキスト透かし</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>画像透かし</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ 墨消し</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>墨消し（黒）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>墨消し（白）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>すべての墨消しを適用</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ 高度な機能</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDFを切り抜き</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>メタデータを編集</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ 表示</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>ダーク/ライトモード切替</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>テキストウィンドウを表示</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>ページ幅（ズーム）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>2ページ（ズーム）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>概要（ズーム）</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ 設定</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>パスワード管理</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR設定</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>署名設定</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>ファイル名書式</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>設定をエクスポート</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>設定をインポート</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ 情報</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF情報を表示</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>音声出力切替</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>メニューバーにフォーカス</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "新しいバージョンが利用可能です",
        "update_available_message": "新しいバージョン <b>{0}</b> が利用可能です。\n\nリリースページにアクセスして更新プログラムをダウンロードしてください:\n{1}",
        "update_available_voice": "新しいバージョン {0} が利用可能です。GitHubページから更新プログラムをダウンロードしてください。",
        "update_open_release": "リリースページを開く",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "すべての翻訳をダウンロード",
        "ask_download_all_translations": """ドイツ語、英語、ベトナム語に加えて、{total_languages} のGUI言語が利用可能です。\n\nこれらを提供 / 更新しますか？\n\n注意:\n不要な言語は後でディレクトリから手動で削除できます:\n{translations_path}
        \nキャンセルした場合、GUI言語は後で「ツール → 翻訳を更新」メニューからダウンロードできます。""",
        "menu_update_translations": "翻訳を更新",
        "translations_updated": "翻訳が更新されました",
        "translations_update_success": "{} 件の翻訳が正常に更新されました（{} 件新規、{} 件更新）。",
        "translations_update_error": "翻訳の更新中にエラーが発生しました",
        "translations_update_no_changes": "すべての翻訳は最新です。",
        "translations_update_offline": "インターネット接続がありません。翻訳を更新できませんでした。",
        "translations_update_in_progress": "翻訳をバックグラウンドで更新中...",
        "translations_downloading": "翻訳をダウンロード中...",
        "translations_path_hint": "翻訳用のユーザーディレクトリ",
        "translations_update_not_available_title": "更新は利用できません",
        "translations_update_not_available_message": """翻訳の更新はインストール版でのみ利用可能です。\n\n開発モードでは翻訳は既に最新です。""",
        "translations_update_no_internet_title": "インターネット接続がありません",
        "translations_update_no_internet_message": """インターネット接続を確立できませんでした。\n\nGitHubから翻訳をダウンロードできません。\n\n考えられる解決策:
        • インターネット接続を確認してください
        • ファイアウォールを一時的に無効にしてください
        • 後でもう一度試してください
        \nGitHubから手動で翻訳をダウンロードすることもできます:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "更新は既に実行中です",
        "btn_retry": "再試行",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "PDF Dark View へようこそ",
        "welcome_title_not_supported": "PDF Dark View へようこそ",
        "welcome_message": "PDF Dark View へようこそ！\n\nシステム言語が '{language}' として検出されました。\nこの言語をユーザーインターフェースに使用しますか？\n\n言語は「設定 → 言語」からいつでも変更できます。",
        "welcome_message_language_not_available": "PDF Dark View へようこそ！\n\nシステム言語が '{language}' として検出されました。\nこの言語はまだインストールされていません。\n\n{language} の翻訳を今すぐGitHubからダウンロードしますか？\n\n（言語はその後自動的にユーザーインターフェースに使用されます。）",
        "welcome_message_language_not_supported": "PDF Dark View へようこそ！\n\nシステム言語が '{language}' として検出されました。\n残念ながら、この言語の翻訳はまだありません。\n\nユーザーインターフェースは {fallback_language} で表示されます。\n\n言語は「設定 → 言語」からいつでも変更できます。\nご希望の場合は、ご自身の言語の翻訳に貢献することもできます:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "はい、システム言語を使用する",
        "welcome_keep_english": "いいえ、英語を維持する",
        "welcome_download_language": "はい、{language} をダウンロードする",

        # ============================================
        # 107. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "プログラムを終了しています",

    }
