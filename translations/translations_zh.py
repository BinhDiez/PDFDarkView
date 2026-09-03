
# ============================================
# translations_zh.py - Chinesisches Wörterbuch (vereinfacht)
# Vollständig sortiert nach Kategorien
# ============================================

def load_chinese_strings():
    """Lädt alle chinesischen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View 作者 BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "加载 PDF",
        'btn_text_window': "OCR 文本",
        'btn_first': "第一页",
        'btn_prev': "上一页",
        'btn_next': "下一页",
        'btn_last': "最后一页",
        'btn_print': "打印",
        'btn_darkmode_light': "亮色模式",
        'btn_darkmode_dark': "深色模式",
        'btn_delete_pages': "删除页面",
        'btn_extract_pages': "提取页面",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialoge)
        # ============================================
        'btn_ok': "确定",
        'btn_cancel': "取消",
        'btn_save': "保存",
        'btn_close': "关闭",
        'btn_delete': "删除",
        'btn_delete_all': "全部删除",
        'btn_copy': "复制",
        'btn_export': "导出",
        'btn_show': "显示密码",
        'btn_hide': "隐藏密码",
        'btn_authenticate': "身份验证",
        'btn_settings': "设置",
        'btn_protect': "保护",
        'btn_remove_password': "移除密码",
        'btn_manage': "密码管理",
        'btn_retry': "重试",
        'btn_select_all': "全选",
        'btn_clear_selection': "取消选择",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "第 {0} 页，共 {1} 页",
        'page_count': "共 {0} 页",
        'goto_page': "转到页面",
        'page_simple': "第 {0} 页",
        'full_view_page': "第 {0} 页全屏视图",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "输入搜索词 + 回车",
        'search_results': "结果: {0} / {1}",
        'search_nav_hint': "回车: 下一个 (Shift+回车: 上一个)",
        'search_no_results': "未找到结果",
        'search_error': "搜索错误",
        'search_active': "搜索框已激活",
        'search_closed': "搜索结束",
        'search_position': "第 {0} 页 {1}",
        'search_pos_top': "顶部",
        'search_pos_upper': "上部",
        'search_pos_middle': "中部",
        'search_pos_lower': "下部",
        'search_pos_bottom': "底部",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "文本识别成功完成！",
        'ocr_success_title': "OCR 成功",
        'ocr_success_message': "文档现在可以搜索了。",
        'ocr_failed': "OCR 失败",
        'ocr_in_progress': "OCR 进行中",
        'ocr_preparing': "正在准备 PDF...",
        'ocr_analyzing': "正在分析 PDF...",
        'ocr_optimizing': "正在优化图像...",
        'ocr_recognizing': "正在识别文本...",
        'ocr_embedding': "正在嵌入文本...",
        'ocr_finalizing': "正在完成 PDF...",
        'ocr_not_available': "OCR 不可用",
        'ocr_install_message': "未找到 OCR 工具。\n\n请安装:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "需要 OCR",
        'ocr_question': "此 PDF 不包含可搜索文本。\n您想执行 OCR 以启用 {0} 吗？",
        'ocr_perform': "执行 OCR",
        'ocr_later': "稍后",
        'ocr_starting': "正在启动有保证的 OCR...",
        'ocr_success_voice': "OCR 成功。PDF 现在可以搜索了。",
        'ocr_partial_success': "已执行 OCR，但替换时出现问题。\n\n可搜索版本已保存至:\n{0}\n\n错误: {1}",
        'ocr_partial_title': "OCR 部分成功",
        'ocr_partial_voice': "已执行 OCR，但替换失败。",
        'original_file': "原始文件:",
        'old_size': "旧大小:    {0} 字节",
        'new_size': "新大小: {0} 字节",
        'size_change': "变化: {0}{1} 字节",
        'backup_created_file': "已创建备份:\n{0}",
        'backup_not_created': "备份: 未创建 (设置已禁用)",
        'page_header': "=== 第 {0} 页 ===\n{1}\n",
        'scanned_page_header': "=== 第 {0} 页 (扫描) ===\n[此页仅包含扫描文本]\n[请手动执行 OCR]\n",
        'scanned_warning': "⚠️ 扫描文本 - 需要 OCR",
        'guaranteed_title': "已创建可搜索 PDF",
        'guaranteed_message': "<b>已创建有保证的可搜索版本！</b>\n\n由于自动 OCR 失败，已创建替代的可搜索 PDF:\n\n{0}\n\n<b>此文件包含:</b>\n• 提取的文本 (如有)\n• 针对扫描页面的提示\n• 完全可搜索",
        'guaranteed_voice': "已创建有保证的可搜索 PDF。",
        'instruction_title': "OCR 指南",
        'instruction_file': "原始文件: {0}",
        'instruction_text': "自动文本识别 (OCR) 失败。\n请手动执行 OCR:\n\n1. 使用 OCRmyPDF (命令行):\n   ocrmypdf --force-ocr \"[文件路径]\" \"输出.pdf\"\n\n2. 使用 ADOBE ACROBAT (macOS/Windows):\n   • 在 Acrobat 中打开 PDF\n   • 工具 > 编辑 PDF\n   • 选择 '识别文本'\n\n3. 使用 PREVIEW (macOS):\n   • 在 Preview 中打开 PDF\n   • 文件 > 导出...\n   • Quartz 过滤器: '减小文件大小'\n   • 启用 '执行 OCR'\n\n4. 在线 OCR 服务:\n   • smallpdf.com/cn/ocr-pdf\n   • ilovepdf.com/zh-cn/ocr-pdf\n   • adobe.com/cn/acrobat/online/pdf-to-word.html",
        'instruction_created': "已创建 OCR 指南",
        'instruction_created_message': "已创建详细指南:\n\n{0}\n\n请按照步骤手动执行 OCR。",
        'instruction_created_voice': "已创建 OCR 指南。",
        'ocr_impossible': "无法执行 OCR",
        'ocr_impossible_message': "无法执行 OCR。\n\n请使用 OCR 软件手动处理 '{0}'。",
        'ocr_impossible_voice': "无法执行 OCR。请手动处理。",
        'emergency_title': "紧急 OCR",
        'emergency_message': "已创建紧急 PDF:\n\n{0}\n\n请使用 OCR 手动处理此文件。",
        'emergency_voice': "已创建紧急 PDF。请手动执行 OCR。",
        'critical_error': "严重错误",
        'critical_error_message': "无法启动 OCR。\n\n请重启程序并检查 OCR 安装。",
        'critical_error_voice': "严重 OCR 错误",
        'ocr_question_html': "<p>此 PDF 不包含可搜索文本。<p>您想执行 OCR 以启用 <b>{0}</b> 吗？</p>",
        'ocr_question_voice': "需要 OCR。PDF 不包含可搜索文本。您想执行 OCR 以启用 {0} 吗？",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "未加载 PDF",
        'no_pdf_message': "没有加载 PDF",
        'pdf_not_found': "未找到 PDF 文件",
        'file_size': "文件大小",
        'bytes': "字节",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "已创建备份",
        'backup_disabled': "备份已禁用",
        'backup_activated': "已启用备份创建",
        'backup_deactivated': "已禁用备份创建",
        'backup_status': "备份: {0}",
        'backup_on': "✔ 已启用",
        'backup_off': "✘ 已禁用",
        'close_pdf': "正在关闭 PDF: {0}",
        'pdf_not_found_format': "未找到 PDF 文件: {0}",
        'error_pdf_load_format': "加载 PDF 时出错: {0}",
        'load_failed_format': "加载失败:\n{0}",
        'decrypted_suffix': "(已解密)",
        'decryption_failed': "解密失败。",
        'decryption_error': "解密时出错",
        'decryption_success': "解密成功",
        'decryption_success_message': "PDF 已解密并保存至:\n\n{0}",
        'decryption_success_voice': "PDF 已解密并保存。",
        'password_remove_error': "移除密码时出错",
        'save_unencrypted': "将未加密的 PDF 另存为",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "另存为...",
        'save_copy': "保存副本",
        'save_success': "PDF 已保存至: {0}",
        'save_encrypted': "受保护的 PDF 已保存至: {0}",
        'save_error': "无法保存 PDF",
        'encryption_question': "您想用密码保护此 PDF 吗？",
        'encryption_yes': "是",
        'encryption_no': "否",
        'encryption_cancel': "取消",
        'save_cancel': "已取消保存",
        'save_encrypted_voice': "文件已加密并保存。",
        'save_success_voice': "PDF 文件已未加密保存。",
        'save_error_format': "无法保存 PDF:\n{0}",
        'export_pages_success': "Pages 导出成功",
        'export_pages_error': "Pages 导出失败",
        'export_pages_error_format': "Pages 导出失败: {0}",
        'export_word_success': "Word 导出成功",
        'export_word_error': "Word 导出失败",
        'export_word_error_format': "Word 导出失败: {0}",
        'export_text_success': "文本导出成功",
        'export_text_error': "文本导出失败",
        'export_text_error_format': "文本导出失败: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "需要密码",
        'password_enter': "请输入密码",
        'password_confirm': "确认密码",
        'password_new': "新密码",
        'password_current': "当前密码",
        'password_save': "保存密码 (加密)",
        'password_saved': "✓ 已保存此文件的密码",
        'password_wrong': "密码错误",
        'password_mismatch': "密码不匹配",
        'password_too_short': "密码太短",
        'password_min_length': "密码必须至少包含 4 个字符",
        'password_strength': "密码强度",
        'password_strength_very_weak': "非常弱",
        'password_strength_weak': "弱",
        'password_strength_medium': "中",
        'password_strength_strong': "强",
        'password_strength_very_strong': "非常强",
        'password_char_count': "({0} 个字符)",
        'password_match': "✓ 匹配",
        'password_no_match': "✗ 密码不匹配",
        'password_show': "显示",
        'password_hide': "隐藏",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "密码管理",
        'password_table_filename': "文件名",
        'password_table_password': "密码",
        'password_count': "已保存 {0} 个密码",
        'password_count_singular': "",
        'password_count_plural': "",
        'password_none': "没有保存的密码",
        'password_copied': "已复制 {0} 个密码",
        'password_copied_singular': "",
        'password_copied_plural': "",
        'password_delete_confirm': "您确定要删除 '{0}' 的密码吗？",
        'password_delete_multiple': "您确定要删除选定的 {0} 个密码吗？",
        'password_delete_all_confirm': "您确定要删除所有已保存的 {0} 个密码吗？",
        'password_deleted': "已删除 {0} 个密码",
        'password_deleted_singular': "",
        'password_deleted_plural': "",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "所有密码已删除",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "密码生成器",
        'generator_generated': "生成的密码:",
        'generator_regenerate': "重新生成",
        'generator_copy': "复制",
        'generator_use': "使用",
        'generator_settings': "设置",
        'generator_length': "长度:",
        'generator_group_every': "每",
        'generator_group_chars': "个字符添加分隔符。分隔符:",
        'generator_uppercase': "大写字母 (A-Z)",
        'generator_lowercase': "小写字母 (a-z)",
        'generator_digits': "数字 (0-9)",
        'generator_symbols': "特殊字符 (!@#$%^&*)",
        'generator_exclude': "排除:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "需要主密码",
        'master_password_setup': "设置主密码",
        'master_password_change': "更改主密码",
        'master_password_enter': "请输入您的主密码",
        'master_password_choose': "选择一个强主密码 (至少 8 个字符)",
        'master_password_new': "请输入您的新主密码",
        'master_password_confirm': "确认密码",
        'master_password_authenticate': "身份验证",
        'master_password_success': "主密码已成功设置。",
        'master_password_changed': "主密码已成功更改。",
        'master_password_removed': "主密码和所有密码已删除。",
        'master_password_remove': "移除主密码",
        'master_password_remove_confirm': "您确定要删除所有密码吗？\n\n此操作不可撤销！",
        'master_password_export_before': "您想先导出备份吗？",
        'master_password_export_delete': "导出并删除",
        'master_password_delete_now': "立即删除",
        'master_password_for_signatures': "要使用签名，您必须设置一个主密码。\n\n您想现在设置主密码吗？",
        'master_password_for_private': "要使用私人文本块，您必须设置一个主密码。\n\n您想现在设置主密码吗？",
        'master_password_info': """
            <b>🔐 无主密码:</b><br>
            • 无法显示、复制和导出密码<br>
            • 始终可以删除密码 (即使没有主密码)<br><br>

            <b>🔐 有主密码:</b><br>
            • 身份验证后所有功能可用<br>
            • 密码使用主密码加密<br>
            • 最小长度: 8 个字符<br>
            • 安全的 SHA-256 哈希存储<br><br>

            <b>重要:</b><br>
            • 如果丢失主密码: 密码无法恢复<br>
            • 移除主密码时: 所有密码将被删除<br>
            • 删除前可导出选项<br>
            • 主密码可随时更改
        """,
        'signature_auth_disabled': "禁用签名的密码询问",
        'template_auth_disabled': "禁用私人文本块的密码询问",
        'master_password_for_signatures_settings': "要使用签名，您必须设置一个主密码。\n\n请前往 设置 - 密码管理",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "保护 PDF",
        'protect_info': "文件 '{0}' 将使用密码保护。",
        'protect_instruction': "请输入所需密码两次以保护文档，或使用输入框右侧的密码生成器。",
        'protect_success': "PDF 已成功保护并保存至:\n{0}\n\n密码: {1}\n\n您想现在打开受保护的 PDF 吗？",
        'protect_open': "是",
        'protect_skip': "否",
        'protect_error': "保护 PDF 时出错",
        'protect_open_title': "打开受保护的 PDF",
        'protect_question': "已完成。您想现在打开受保护的 PDF 吗？是或否？",
        'password_cancel': "密码对话框已取消",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "删除页面",
        'pages_extract': "提取页面",
        'pages_insert': "插入页面",
        'pages_move': "移动页面",
        'pages_delete_options': "删除选项",
        'pages_delete_empty': "删除所有空白页",
        'pages_delete_current': "删除当前页面",
        'pages_delete_range': "删除页面范围",
        'pages_extract_options': "提取选项",
        'pages_extract_current': "提取当前页面",
        'pages_extract_range': "提取页面范围",
        'pages_insert_position': "插入位置",
        'pages_insert_before': "插入到页面之前:",
        'pages_insert_select': "选择 PDF",
        'pages_insert_none': "未选择 PDF",
        'pages_move_source': "要移动的页面",
        'pages_move_from': "从页面:",
        'pages_move_to': "到页面:",
        'pages_move_target': "目标位置",
        'pages_move_before': "移动到页面之前:",
        'pages_move_hint': "提示: 第 1 页 = 开头, {0} = 结尾",
        'pages_range_invalid': "起始页必须小于或等于结束页。",
        'pages_position_invalid': "目标位置不能位于要移动的范围内。",
        'pages_no_pdf_selected': "未选择 PDF。",
        'pages_deleted': "已删除 {0} 页。",
        'pages_extracted': "已提取: {0}\n已保存至: {1}\n文件大小: {2:.1f} KB",
        'pages_inserted': "已插入 {0} 页",
        'pages_moved': "已移动 {0} 页。",
        'pages_deleted_none': "没有页面被删除。",
        'pages_delete_progress': "正在删除页面...",
        'pages_deleted_with_backup': "已删除 {0} 页。\n\n备份: {1}",
        'pages_deleted_voice': "已创建备份并删除 {0} 页。",
        'info': "提示",
        'error_dialog_creation': "无法创建对话框",
        'extract_page_single': "提取第 {0} 页",
        'extract_page_range': "提取第 {0}-{1} 页",
        'extract_success_voice': "页面提取成功",
        'extract_error_format': "提取时出错: {0}",
        'pages_inserted_voice': "已插入 {0} 页。",
        'insert_error_format': "插入时出错: {0}",
        'pages_move_progress': "正在移动页面...",
        'pages_moved_with_backup': "已移动 {0} 页。\n\n备份: {1}",
        'move_success_title': "移动成功",
        'pages_moved_voice': "成功移动 {0} 页",
        'mark_removed': "已移除第 {0} 页的标记",
        'mark_empty': "已将第 {0} 页标记为空白",
        'mark_export_removed': "已移除第 {0} 页的导出标记",
        'mark_export': "已将第 {0} 页标记为导出",
        'no_empty_pages': "没有标记为删除的空白页",
        'delete_empty_confirm': "您想删除所有标记的 {0} 个空白页吗？",
        'delete_empty_confirm_voice': "现在删除所有标记的 {0} 个空白页？是或否。",
        'empty_pages_deleted': "已删除 {0} 个空白页",
        'no_export_pages': "没有标记为导出的页面",
        'overwrite_title': "覆盖现有文件",
        'overwrite_question': "文件\n\n{0}\n\n已存在。\n您想覆盖它吗？",
        'overwrite_voice': "覆盖现有文件？是或否。",
        'page_skipped': "已跳过第 {0} 页",
        'export_complete': "导出完成。",
        'export_complete_voice': "导出已完成。",
        'no_pages_exported': "没有页面被导出",
        'export_cancelled': "导出已取消",
        'pages_exported': "已将 {0} 页导出到 {1}",
        'export_page_title': "导出页面",
        'page_exported': "已将第 {0} 页导出到 {1}",
        'export_error': "导出时出错",
        'export_marked_title': "导出标记的页面",
        'rotate_all_title': "旋转所有页面",
        'rotate_all_question': "您想将所有页面向右旋转 90 度吗？",
        'rotate_all_voice': "您想将所有页面向右旋转 90 度吗？是或否？",
        'all_pages_rotated': "所有页面已旋转",
        'page_rotated': "第 {0} 页已旋转",
        'rotate_error': "无法旋转页面",
        'delete_page_confirm': "您想删除第 {0} 页吗？",
        'delete_page_confirm_voice': "您确定要删除第 {0} 页吗？是或否。",
        'page_deleted': "第 {0} 页已删除",
        'delete_error': "无法删除页面",
        'pages_deleted_voice': "已删除 {0} 页",
        'pages_exported_split': "成功导出 {0} 页。",
        'pages_skipped': "已跳过 {0} 页。",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "提取页面 (高级)",
        'pdf_splitter_title': "PDF 分割与提取器",
        'pdf_splitter_load': " 选择 PDF 文件",
        'pdf_splitter_info': "请为您的 PDF 文档选择一个选项",
        'pdf_splitter_basic': "基本操作",
        'pdf_splitter_single': "拆分为单个页面",
        'pdf_splitter_range': "提取页面:",
        'pdf_splitter_range_placeholder': "例如 1-3,5,7-9",
        'pdf_splitter_clean': "清理操作",
        'pdf_splitter_remove_empty': "删除所有空白页",
        'pdf_splitter_remove': "删除页面范围:",
        'pdf_splitter_remove_placeholder': "例如 2,4-6",
        'pdf_splitter_process': "处理 PDF",
        'pdf_splitter_loaded': "已加载 PDF。请选择一个选项",
        'pdf_read_error': "无法读取 PDF",
        'pages': "页",
        'pages_created': "页面已创建",
        'range_empty': "请输入页面范围",
        'range_invalid': "无效的页面范围",
        'range_created': "已使用所选页面创建新 PDF:\n{0}",
        'empty_removed': "已移除 {0} 个空白页。\n输出: {1}",
        'remove_empty': "请输入要删除的页面",
        'remove_invalid': "要删除的页面无效",
        'remove_done': "已创建清理后的 PDF:\n{0}",
        'open_folder': "打开文件夹",
        'show_in_finder': "在 Finder 中显示",
        'pdf_splitter_no_pdf': "请先加载一个 PDF 文件。",
        'process_error': "处理 PDF 时出错",
        'pages_created_voice': "已创建 {0} 页",
        'range_created_voice': "已使用所选页面创建 PDF",
        'empty_removed_voice': "已移除 {0} 个空白页",
        'remove_done_voice': "已创建清理后的 PDF",
        'pdf_splitter_split_groups': "每个连续组放入单独文件",
        'range_created_single': "已创建新 PDF:\n{0}",
        'range_created_multiple': "已创建 {0} 个 PDF 文件。",
        'range_created_voice_single': "已创建一个包含所选页面的 PDF",
        'range_created_voice_multiple': "已创建 {0} 个 PDF 文件",
        'empty_removed_none_left': "没有剩余页面",
        'empty_removed_all_empty': "所有页面均被识别为空白，将被删除。未创建文件。",
        'preview_single': "预览: {0}",
        'preview_enter_range': "请输入页面范围。",
        'preview_invalid_range': "无效的页面范围。",
        'preview_file': "预览: {0}",
        'preview_files': "预览: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "开始打印",
        'print_sent': "打印作业已发送",
        'print_now': "立即打印",
        'print_error': "立即打印时出错",
        'print_limited': "此系统上的打印功能受限",
        'print_error_format': "立即打印时出错: {0}",
        'warning': "警告",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "切换到亮色模式",
        'mode_switch_to_dark': "切换到深色模式",
        'mode_dark_activated': "深色模式已激活",
        'mode_light_activated': "亮色模式已激活",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "全页视图",
        'zoom_two_pages': "并排两页",
        'zoom_overview': "概览模式",
        'zoom_cannot_during_search': "搜索时无法缩放",
        'zoom_exit_first': "请先退出缩放模式",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "拖放已启用",
        'drag_disabled': "拖放已禁用",
        'drag_page_grab': "正在抓取第 {0} 页",
        'drag_page_dropped': "已将第 {0} 页插入到位置 {1}",
        'drag_position_invalid': "无效位置",
        'drag_same_position': "第 {0} 页保持在位置 {0}",
        'drag_error': "移动时出错",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "文本输入，支持高级格式和文本块管理",
        'text_templates': "可用文本块:",
        'text_name': "名称",
        'text_preview': "文本预览",
        'text_enter': "文本:",
        'text_font_size': "字体大小:",
        'text_formatting': "格式:",
        'text_bold': "粗体",
        'text_italic': "斜体",
        'text_underline': "下划线",
        'text_alignment': "对齐:",
        'text_left': "左对齐",
        'text_center': "居中",
        'text_right': "右对齐",
        'text_color': "文本颜色:",
        'text_opacity': "不透明度:",
        'text_word_wrap': "换行:",
        'text_auto': "自动",
        'text_page_width_95': "页面宽度 (95%)",
        'text_page_width_85': "非常宽 (85%)",
        'text_page_width_75': "较宽 (75%)",
        'text_page_width_60': "宽 (60%)",
        'text_page_width_50': "中等 (50%)",
        'text_page_width_30': "窄 (30%)",
        'text_page_width_20': "较窄 (20%)",
        'text_page_width_10': "非常窄 (10%)",
        'text_no_wrap': "不换行",
        'text_private': "私人文本块 (需要身份验证)",
        'text_preview_label': "预览:",
        'text_preview_placeholder': "此处显示文本预览...",
        'text_no_text': "(无文本)",
        'text_save_template': "💾 保存为模板",
        'text_delete_template': "🗑 删除所选文本块",
        'text_show_private': "显示私人",
        'text_hide_private': "隐藏私人",
        'text_use': "✅ 使用文本",
        'text_saved': "文本块已保存为:\n{0}",
        'text_saved_voice': "文本块已保存",
        'text_deleted': "文本块已删除",
        'text_no_text_to_save': "没有要保存的文本。",
        'text_no_templates': "未找到文本块",
        'text_private_master_required': "私人块只能在设置了主密码时使用。\n\n您想现在设置主密码吗？",
        'text_filename': "文本块的文件名 (不含 'Text_' 和 '.txt'):",
        'text_filename_hint': "例如: '家庭电话' 将保存为 'Text_家庭电话.txt'",
        'text_save_hint': "文本块将自动与格式一起保存。",
        'text_guide_title': "文本输入 - 指南",
        'text_delete_confirm': "您确定要删除此文本块吗？\n\n文件: {0}\n文本: {1}...",
        'text_make_public': "标记为公共",
        'text_make_private': "标记为私人",
        'text_privacy_changed': "隐私状态已更改",
        'text_private_always': "私人始终可见 (设置)",
        'text_mode_required': "请先激活文本模式",
        'text_continue_editing': "继续编辑 - 光标在文本末尾",
        'text_no_input': "未输入文本 - 文本已丢弃",
        'save_dialog_question': "您想如何继续？",
        'text_save_question': "保存所有文本和叉号、调整、继续编辑还是丢弃？",
        'copy_cross': "叉号已复制",
        'paste_cross': "叉号已粘贴",
        'paste_text': "文本已粘贴",
        'cross_discarded': "叉号已丢弃",
        'all_discarded': "全部已丢弃",
        'text_discarded': "文本已丢弃",
        'no_texts_to_save': "没有要保存的文本",
        'no_valid_texts': "没有要保存的有效文本",
        'text_word_singular': "文本",
        'text_word_plural': "文本",
        'cross_word_singular': "叉号",
        'cross_word_plural': "叉号",
        'texts_saved_title': "文本已保存",
        'texts_crosses_saved': "{0} 个{1}和 {2} 个{3}已插入 PDF。\n\nPDF 已重新加载...",
        'texts_crosses_saved_voice': "{0} 个{1}和 {2} 个{3}已保存。",
        'texts_saved': "{0} 个{1}已插入 PDF。\n\nPDF 已重新加载...",
        'texts_saved_voice': "{0} 个{1}已保存。",
        'crosses_saved': "{0} 个{1}已插入 PDF。\n\nPDF 已重新加载...",
        'crosses_saved_voice': "{0} 个{1}已保存。",
        'elements_saved': "{0} 个元素已插入 PDF。\n\nPDF 已重新加载...",
        'elements_saved_voice': "{0} 个元素已保存。",
        'text_window_load_error': "无法加载文本窗口",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **文本输入和文本块 – 详细指南**

        **1. 插入和编辑文本**
        - 在文档中所需位置右键单击，然后选择“插入文本”。
        - 将打开一个对话框，您可以在其中输入和格式化文本：
        • 字体大小、粗体、斜体、下划线
        • 文本颜色（可自由选择）
        • 透明度（不透明度）通过滑块
        • 换行（各种宽度，例如页面宽度、窄、不换行）
        - 确认后，文本将出现在单击位置。您可以使用鼠标或箭头键移动它。
        - 双击文本打开编辑模式；按 ESC 退出。

        **2. 管理文本块（模板）**
        - 在文本对话框中，您会在左侧看到所有已保存文本块的列表。
        - **保存块：** 输入您的文本，格式化，然后单击“💾 保存为模板”。输入文件名（不带扩展名）。
        - **加载块：** 单击列表中所需的名称。文本和格式将被采用，如果需要，可以进行调整。
        - **删除：** 右键单击块，您可以删除它或更改其隐私状态。

        **3. 私人文本块（主密码）**
        - 如果您已设置主密码（在“设置”→“密码管理”下），您可以将块标记为“私人”。
        - 在保存之前，在对话框中激活“私人文本块”复选框。
        - 私人块仅在您每个会话输入一次主密码后才会在列表中显示（通过锁图标或在首次访问时进行身份验证）。
        - 这样，您可以保护机密文本块免受他人访问。

        **4. 插入叉号**
        - 通过上下文菜单，您还可以插入一个图形叉号（例如用于复选框）。
        - 叉号的大小、线宽和颜色可以在设置中全局调整（菜单“设置”→“叉号设置”）。
        - 右键单击现有叉号可以单独更改它。

        **5. 批量操作**
        - 如果您在一页上放置了多个文本或叉号，您可以通过上下文菜单（在文本模式下右键单击）一起保存或丢弃所有元素。
        - 保存时，所有元素都将嵌入 PDF 中，并保留为矢量图形。

        **6. 文本模式下的键盘快捷键**
        - 箭头键：移动元素
        - Ctrl+箭头键：更大步长移动
        - Enter：打开保存对话框（全部保存/调整/丢弃）
        - ESC：丢弃当前元素
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 文本输入和文本块 – 详细指南</strong></p>

        <p><strong>1. 插入和编辑文本</strong></p>
        <ul>
        <li>在文档中所需位置右键单击，然后选择“插入文本”。</li>
        <li>将打开一个对话框，您可以在其中输入和格式化文本：<br/>
        • 字体大小、粗体、斜体、下划线<br/>
        • 文本颜色（可自由选择）<br/>
        • 透明度（不透明度）通过滑块<br/>
        • 换行（各种宽度，例如页面宽度、窄、不换行）</li>
        <li>确认后，文本将出现在单击位置。您可以使用鼠标或箭头键移动它。</li>
        <li>双击文本打开编辑模式；按 ESC 退出。</li>
        </ul>

        <p><strong>2. 管理文本块（模板）</strong></p>
        <ul>
        <li>在文本对话框中，您会在左侧看到所有已保存文本块的列表。</li>
        <li><strong>保存块：</strong> 输入您的文本，格式化，然后单击“💾 保存为模板”。输入文件名（不带扩展名）。</li>
        <li><strong>加载块：</strong> 单击列表中所需的名称。文本和格式将被采用，如果需要，可以进行调整。</li>
        <li><strong>删除：</strong> 右键单击块，您可以删除它或更改其隐私状态。</li>
        </ul>

        <p><strong>3. 私人文本块（主密码）</strong></p>
        <ul>
        <li>如果您已设置主密码（在“设置”→“密码管理”下），您可以将块标记为“私人”。</li>
        <li>在保存之前，在对话框中激活“私人文本块”复选框。</li>
        <li>私人块仅在您每个会话输入一次主密码后才会在列表中显示（通过锁图标或在首次访问时进行身份验证）。</li>
        <li>这样，您可以保护机密文本块免受他人访问。</li>
        </ul>

        <p><strong>4. 插入叉号</strong></p>
        <ul>
        <li>通过上下文菜单，您还可以插入一个图形叉号（例如用于复选框）。</li>
        <li>叉号的大小、线宽和颜色可以在设置中全局调整（菜单“设置”→“叉号设置”）。</li>
        <li>右键单击现有叉号可以单独更改它。</li>
        </ul>

        <p><strong>5. 批量操作</strong></p>
        <ul>
        <li>如果您在一页上放置了多个文本或叉号，您可以通过上下文菜单（在文本模式下右键单击）一起保存或丢弃所有元素。</li>
        <li>保存时，所有元素都将嵌入 PDF 中，并保留为矢量图形。</li>
        </ul>

        <p><strong>6. 文本模式下的键盘快捷键</strong></p>
        <ul>
        <li>箭头键：移动元素</li>
        <li>Ctrl+箭头键：更大步长移动</li>
        <li>Enter：打开保存对话框（全部保存/调整/丢弃）</li>
        <li>ESC：丢弃当前元素</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "叉号设置",
        'cross_properties': "叉号属性",
        'cross_size': "大小 (px):",
        'cross_line_width': "线宽:",
        'cross_color': "颜色:",
        'cross_choose_color': "选择",
        'cross_fine_tuning': "保存时的微调 (像素)",
        'cross_offset_x': "X 偏移:",
        'cross_offset_y': "Y 偏移:",
        'cross_offset_x_tooltip': "负值在保存时将叉号向左移动，正值向右",
        'cross_offset_y_tooltip': "负值在保存时将叉号向上移动，正值向下",
        'cross_preview': "预览",
        'cross_save': "应用设置",
        'cross_customized': "叉号已调整",
        'cross_settings_applied': "叉号设置已保存。\n大小: {0}px, 线宽: {1}px\n{2}",
        'cross_updated_count': "已更新 {0} 个现有叉号。",
        'cross_no_crosses': "未找到现有叉号。",
        'cross_settings_applied_all': "已对所有 {0} 个叉号应用叉号设置",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "签名设置",
        'signature_1': "签名 1",
        'signature_2': "签名 2",
        'signature_select': "选择签名",
        'signature_add': "➕ 添加新签名...",
        'signature_size': "签名 {0} 的大小 (%):",
        'signature_common': "通用设置",
        'signature_timestamp': "自动添加时间戳",
        'signature_location': "默认位置:",
        'signature_timestamp_size': "时间戳字体大小:",
        'signature_no_files': "-- 未找到签名 --",
        'signature_insert': "插入签名",
        'signature_insert_1': "插入签名 1",
        'signature_insert_2': "插入签名 2",
        'signature_customize': " 调整此签名",
        'signature_discard': " 丢弃此签名",
        'signature_save_all': " 保存所有签名",
        'signature_discard_all': " 丢弃所有签名",
        'signature_guide_title': "签名 - 指南",
        'signature_guide': """
📝 签名 - 快速指南

- 设置主密码
- 在菜单“设置”中配置签名
  (大小、时间戳...)
- 在所需位置右键单击插入
  (每个会话需要一次主密码)
- 用鼠标或箭头键移动签名
- 可以连续插入多个签名
- 每个签名可以单独调整
- 丢弃单个签名
- 一次性保存/丢弃所有签名
- 也可以使用菜单栏。
        """,
        'signature_placeholder': "无预览可用",
        'signature_info': "签名 {0}: {1}×{2} px ({3}% 的 {4}×{5})",
        'signature_info_placeholder': "签名 {0} 的设置",
        'signature_inserted': "已在第 {1} 页插入签名 {0}",
        'signature_deleted': "签名已删除",
        'signature_copied': "签名已复制",
        'signature_pasted': "已粘贴签名 {0}",
        'signature_saved': "{0} 个签名已插入 PDF。\n\nPDF 已重新加载...",
        'signature_saved_voice': "{0} 个签名已保存",
        'mode_replace_signature_format': "结束模式并插入签名 {0}",
        'mode_conflict_voice_signature': "模式 {0} 已激活。结束并插入签名？",
        'signature_not_configured': "签名 {0} 未配置",
        'signature_file_not_found': "未找到签名文件",
        'timestamp_format': "{0}，{1}",
        'no_copied_signature': "没有复制的签名",
        'no_signatures_to_save': "没有要保存的签名",
        'signature_save_question': "保存所有签名、调整还是丢弃此签名？",
        'signatures_saved_title': "签名已保存",
        'signatures_saved': "{0} 个签名已插入 PDF。\n\nPDF 已重新加载...",
        'signatures_saved_voice': "{0} 个签名已保存。",
        'all_signatures_discarded': "所有签名已丢弃",
        'signature_settings_saved': "签名设置已保存",
        'signature_cancelled': "签名已丢弃",
        'signature_active_title': "签名已激活",
        'signature_replace_question': "已有一个签名处于激活状态。\n\n您想替换当前签名吗？",
        'signature_replace': "替换签名",
        'signature_replace_voice': "替换当前签名还是取消？",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "图像设置",
        'image_common': "通用图像设置",
        'image_keep_aspect': "拖动时保持纵横比",
        'image_default_size': "默认大小 (%):",
        'image_dark_invert': "在深色模式下反转图像",
        'image_dark_invert_tooltip': "启用：图像将反转以获得更好的可见性",
        'image_fine_tuning': "微调 (像素)",
        'image_offset_x': "X 偏移:",
        'image_offset_y': "Y 偏移:",
        'image_offset_x_tooltip': "负值在保存时将图像向左移动，正值向右",
        'image_offset_y_tooltip': "负值在保存时将图像向上移动，正值向下",
        'image_select': "选择图像",
        'image_insert': "插入图像",
        'image_customize': " 调整此图像",
        'image_aspect': " 保持纵横比",
        'image_discard': " 丢弃此图像",
        'image_save_all': " 保存所有图像",
        'image_discard_all': " 丢弃所有图像",
        'image_filter': "图像",
        'image_guide_title': "插入图像 - 指南",
        'image_guide': """
📷 在 PDF 中插入图像 - 快速指南：

1. 在所需位置右键单击
2. “插入图像” → 选择图像
3. 放置图像：用鼠标拖动
4. 调整大小：在角/边缘拖动
5. 保持纵横比：按 [A] 键
6. 进一步调整：右键单击图像

提示：在上下文菜单中，您可以调整设置。
        """,
        'image_inserted': "已在第 {1} 页插入图像 {0}",
        'image_deleted': "图像已丢弃",
        'image_copied': "图像已复制",
        'image_pasted': "图像已粘贴",
        'image_saved': "{0} 个图像已插入 PDF。\n\nPDF 已重新加载...",
        'image_saved_voice': "{0} 个图像已保存",
        'image_aspect_on': "已启用",
        'image_aspect_off': "已禁用",
        'image_aspect_toggle': "保持纵横比 {0}",
        'image_reset': "图像已重置为原始大小",
        'image_replaced': "图像已替换",
        'image_invalid': "无效的图像",
        'mode_replace_image': "插入图像",
        'mode_conflict_voice_image': "模式 {0} 已激活。结束并插入图像？",
        'image_active_title': "图像已激活",
        'image_replace_question': "已有一个图像处于激活状态。\n\n您想替换当前图像吗？",
        'image_replace': "替换图像",
        'image_replace_voice': "替换当前图像还是取消？",
        'image_filter_all': "图像 (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;所有文件 (*.*)",
        'no_copied_image': "没有复制的图像",
        'image_discarded': "图像已丢弃",
        'image_save_question': "保存所有图像、调整还是丢弃此图像？",
        'no_images_to_save': "没有要保存的图像",
        'no_valid_images': "没有要保存的有效图像",
        'images_saved_title': "图像已保存",
        'images_saved': "{0} 个图像已插入 PDF。\n\nPDF 已重新加载...",
        'images_saved_voice': "{0} 个图像已保存。",
        'all_images_discarded': "所有图像已丢弃",
        'image_settings_updated': "图像设置已更新",
        'image_replace_title': "选择新图像",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "形状设置",
        'form_basic': "基本设置",
        'form_default_type': "默认形状类型:",
        'form_rectangle': "矩形",
        'form_ellipse': "椭圆",
        'form_line': "线条",
        'form_arrow': "箭头",
        'form_line_width': "线宽:",
        'form_colors': "颜色",
        'form_line_color': "线条颜色:",
        'form_fill_color': "填充颜色:",
        'form_choose_color': "选择",
        'form_transparent': "透明背景 (仅线条)",
        'form_filled': "填充",
        'form_dark_mode': "深色模式",
        'form_dark_invert': "在深色模式下反转颜色",
        'form_fine_tuning': "微调 (像素)",
        'form_offset_x': "X 偏移:",
        'form_offset_y': "Y 偏移:",
        'form_offset_x_tooltip': "负值在保存时将形状向左移动，正值向右",
        'form_offset_y_tooltip': "负值在保存时将形状向上移动，正值向下",
        'form_preview': "预览",
        'form_insert': "插入形状",
        'form_rectangle_insert': "矩形",
        'form_ellipse_insert': "椭圆/圆形",
        'form_line_insert': "线条 (2 次单击)",
        'form_arrow_insert': "箭头 (2 次单击)",
        'form_customize': " 调整此形状",
        'form_transparent_toggle': " 透明背景",
        'form_discard': " 丢弃此形状",
        'form_save_all': " 保存所有形状",
        'form_discard_all': " 丢弃所有形状",
        'form_guide_title': "插入形状 - 指南",
        'form_guide': """
📐 在 PDF 中插入形状 - 快速指南：

1. 选择形状类型（矩形、椭圆、线条、箭头）
2. 单击位置
   - 对于矩形/椭圆：单击一次放置形状
   - 对于线条/箭头：单击两次确定起点和终点
3. 放置形状：用鼠标拖动
4. 调整大小：在角/边缘拖动
5. 保存形状：Enter
6. 丢弃形状：ESC
7. 进一步调整：右键单击形状

提示：在上下文菜单中，您可以调整设置。
        """,
        'form_inserted': "已在第 {1} 页插入 {0}",
        'form_deleted': "形状已删除",
        'form_copied': "形状已复制",
        'form_pasted': "形状已粘贴",
        'form_saved': "{0} 个形状已插入 PDF。\n\nPDF 已重新加载...",
        'form_saved_voice': "{0} 个形状已保存",
        'form_reset': "形状已重置为默认大小",
        'form_transparent_on': "已启用",
        'form_transparent_off': "已禁用",
        'form_transparent_toggled': "透明背景 {0}",
        'form_line_cancel': "绘制线条已取消",
        'form_second_click': "现在单击 {0} 的终点",
        'mode_replace_form': "插入形状",
        'mode_conflict_voice_form': "模式 {0} 已激活。结束并插入形状？",
        'form_settings_updated': "形状设置已更新",
        'form_unknown': "形状",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. 单击起始位置",
        'form_line_guide_2': "2. 单击结束位置",
        'form_line_guide_3': "线条将在两点之间绘制。",
        'form_line_status_1': "等待第一次单击...",
        'form_line_status_2': "已设置第一个点: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "现在单击终点...",
        'form_line_status_4': "已设置两个点。\n单击“完成”以保存。",
        'form_line_reset': "重置",
        'form_line_finish': "完成",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "复制 (Cmd+C)",
        'paste': "粘贴 (Cmd+V)",
        'copied': "已复制: {0}",
        'no_element_to_copy': "没有选择要复制的元素",
        'no_copied_data': "没有复制的数据",
        'no_valid_position': "没有有效的粘贴位置",
        'copy_text': "文本已复制",
        'copy_image': "图像已复制",
        'copy_form': "形状已复制",
        'copy_signature': "签名已复制",
        'element_text': "文本",
        'element_image': "图像",
        'element_form': "形状",
        'element_signature': "签名",
        'element_unknown': "元素",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "模式冲突",
        'mode_conflict_message': "模式 '{0}' 已激活。\n\n您想结束它并{1}吗？",
        'mode_replace': "结束模式并{0}",
        'mode_cancel': "取消",
        'mode_replace_text': "插入文本",
        'mode_replace_cross': "插入叉号",
        'mode_replace_signature': "插入签名",
        'mode_replace_image': "插入图像",
        'mode_replace_form': "插入形状",
        'mode_conflict_voice': "模式 {0} 已激活。结束并插入文本？",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "文本输入",
        'active_mode_signature': "签名",
        'active_mode_image': "图像",
        'active_mode_form': "形状",
        'active_mode_and': " 和 ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "插入",
        'insert_another_text': "插入文本",
        'insert_another_cross': "插入叉号",
        'insert_another_signature_1': "签名 1",
        'insert_another_signature_2': "签名 2",
        'insert_another_image': "插入图像",
        'insert_another_form_rect': "矩形",
        'insert_another_form_ellipse': "椭圆",
        'insert_another_form_line': "线条 (2 次单击)",
        'insert_another_form_arrow': "箭头 (2 次单击)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "保存 {0}",
        'save_dialog_message': "{0} 将保存到第 {1} 页。\n\n您想如何继续？",
        'save_all': "保存所有 {0}",
        'save_single': "保存 {0}",
        'save_customize': "调整 {0}",
        'save_discard': "丢弃此 {0}",
        'save_continue': "继续编辑",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " 转到第 {0} 页",
        'context_rotate': " 旋转第 {0} 页",
        'context_delete': " 删除第 {0} 页",
        'context_export': " 导出第 {0} 页",
        'context_mark_as': " 将页面标记为...",
        'context_mark_empty': " 空白页",
        'context_unmark_empty': " 不再空白",
        'context_mark_export': " 标记为导出",
        'context_unmark_export': " 取消导出标记",
        'context_batch_actions': " 批量操作",
        'context_batch_delete_empty': " 删除所有 {0} 个空白页",
        'context_batch_export_single': " 导出所有 {0} 页 (单个文件)",
        'context_batch_export_split': " 导出所有 {0} 页 (分开)",
        'context_drag_start': " 开始拖放",
        'context_drag_stop': " 结束拖放",
        'context_insert': " 插入",
        'context_insert_pages': " 插入页面",
        'context_zoom': "缩放",
        'discard_mixed': "丢弃所有 {0} 个{1}和 {2} 个{3}",
        'save_mixed': "保存 {0} 个{1}和 {2} 个{3}",
        'discard_texts': "丢弃所有 {0} 个文本",
        'discard_text_single': "丢弃 1 个文本",
        'save_texts': "保存 {0} 个文本",
        'save_text_single': "保存 1 个文本",
        'discard_crosses': "丢弃所有 {0} 个叉号",
        'discard_cross_single': "丢弃 1 个叉号",
        'save_crosses': "保存 {0} 个叉号",
        'save_cross_single': "保存 1 个叉号",
        'discard_signatures': "丢弃所有 {0} 个签名",
        'save_signature_single': "保存 1 个签名",
        'save_signatures': "保存 {0} 个签名",
        'discard_images': "丢弃所有 {0} 个图像",
        'save_image_single': "保存 1 个图像",
        'save_images': "保存 {0} 个图像",
        'discard_forms': "丢弃所有 {0} 个形状",
        'save_form_single': "保存 1 个形状",
        'save_forms': "保存 {0} 个形状",
        'cross_discard': "丢弃此叉号",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 导出/导入信息",
        'export_what': "📋 导出什么？",
        'export_general': "通用设置",
        'export_general_items': "• 语音输出 (开/关, 速度)\n• 深色/亮色模式\n• 备份设置\n• OCR 设置",
        'export_image_form': "图像和形状设置",
        'export_image_form_items': "• 图像设置 (纵横比, 默认大小)\n• 形状设置 (线宽, 颜色)\n• 签名设置 (路径, 大小, 时间戳)",
        'export_passwords': "密码数据库",
        'export_passwords_items': "• 所有已保存的 PDF 密码\n• 可选择加密或解密导出",
        'export_master': "主密码设置",
        'export_master_items': "• 主密码哈希\n• 签名/文本块的设置",
        'export_signatures': "签名和文本块",
        'export_signatures_items': "• 所有图像文件 (签名)\n• 所有带格式的文本块\n• 私人/公共标记",
        'export_import_warning': "⚠️ 重要提示",
        'export_import_note': "• 导入时，所有当前设置将被覆盖\n• 需要重启应用程序\n• 现有签名/文本块将被替换",
        'export_master_note': "• 如果设置了主密码，您可以选择：\n  - 解密导出 (密码明文)\n  - 加密导出 (仅能使用主密码读取)",
        'export_security': "• 导出的 ZIP 文件包含敏感数据\n• 请妥善保管 (例如加密的 U 盘)\n• 如果文件丢失：密码将无法恢复",
        'export_format': "📁 导出格式",
        'export_format_desc': "设置将保存在一个 ZIP 文件中：",
        'export_filename': "PDFDarkView_设置_YYYYMMDD_HHMMSS.zip",
        'export_success': "设置已成功导出",
        'export_failed': "导出失败",
        'export_import_question': "您想现在重启应用程序吗？",
        'export_password_question': "已设置主密码。\n\n您想以解密形式导出密码吗？\n(否则将以加密形式导出)",
        'export_decrypt': "解密导出",
        'export_encrypt': "加密导出",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " 信息",
        'info_title': "关于 PDF Dark View",
        'info_version': "版本",
        'info_author': "由 Toralf Schulz (BinhDiez) 开发",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "关于",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> 是一款无障碍 PDF 查看器，专为视力障碍人士开发。</p>

            <p><strong>主要特点：</strong></p>
            <ul>
                <li>高对比度、可定制的界面</li>
                <li>完整的键盘控制</li>
                <li>集成的语音输出</li>
                <li>针对扫描文档的 OCR</li>
                <li>全面的编辑工具</li>
            </ul>

            <p>支持超过 50 种语言 – 让 PDF 对所有人都无障碍。</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "功能",
        'info_features_intro': "PDF Dark View 为您提供以下功能：",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>显示与导航</strong> – 深色/浅色模式、翻页、缩放、跳转到页面</li>
            <li><strong>OCR（文字识别）</strong> – 使扫描的文档可搜索和可复制</li>
            <li><strong>编辑</strong> – 插入文本、十字、签名、图像和形状</li>
            <li><strong>页面管理</strong> – 删除、提取、插入、通过拖放移动</li>
            <li><strong>导出</strong> – 导出为 Word、Pages 或文本</li>
            <li><strong>安全</strong> – 密码保护和管理</li>
            <li><strong>无障碍性</strong> – 语音输出、键盘控制、高对比度</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "操作",
        'info_accessibility': "♿ 无障碍性 – 完整的键盘控制",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 通用</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> 打开 PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> 搜索</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> 切换深色/浅色模式</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> 打印</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> 退出</div>

        <div class="shortcut-cat">📖 导航</div>
        <div class="shortcut-row"><kbd>方向键</kbd> 逐页翻页</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> 转到页面</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> 第一页</div>
        <div class="shortcut-row"><kbd>Ende</kbd> 最后一页</div>

        <div class="shortcut-cat">✏️ 编辑</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> 插入文本</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> 删除页面</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> 提取页面</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> 插入页面</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> 移动页面</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> 旋转页面</div>

        <div class="shortcut-cat">🖼️ 移动元素</div>
        <div class="shortcut-row"><kbd>方向键</kbd> 移动文本/图像/签名</div>
        <div class="shortcut-row"><kbd>Ctrl+方向键</kbd> 更大步长</div>
        <div class="shortcut-row"><kbd>Enter</kbd> 保存</div>
        <div class="shortcut-row"><kbd>ESC</kbd> 放弃</div>

        <div class="shortcut-cat">🗣️ 语音输出</div>
        <div class="shortcut-row"><kbd>F2</kbd> 开启/关闭语音输出</div>
        """,
        'info_contextmenu': "📌 重要：所有功能也可通过上下文菜单（鼠标右键）访问！",
        'info_accessibility_hint': "💡 提示：语音输出 (F2) 便于定位，并提供菜单和对话框的反馈。",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "许可证 & 出版信息",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 出版信息</strong><br>
        根据 § 5 TMG 的信息：<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, 德国<br>
        电子邮件：binhdiez64@gmail.com<br>
        内容负责人：Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ 免责声明</strong><br>
        本软件经过最精心的开发。对正确性、完整性和功能性不提供任何保证。使用风险自负。<br><br>

        <strong>📄 MIT 许可证（私人使用）</strong><br>
        版权 (c) 2026 Toralf Schulz (BinhDiez)<br>
        允许：免费使用、私人修改、个人副本。<br>
        不允许：销售、商业用途、删除版权声明。<br><br>

        <strong>🔧 第三方组件</strong><br>
        本软件包含 GPL、AGPL、Apache 2.0、BSD 和 MIT 许可证下的组件。<br>
        重新分发时，必须遵守相应的许可条款。<br><br>

        <strong>🌐 开源</strong><br>
        源代码可用，并可根据相应的许可条款进行查看、修改和重新分发。<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "致谢",
        'info_credits': "感谢开源社区",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF 处理</li>
            <li><strong>PyQt5</strong> – 图形界面</li>
            <li><strong>Tesseract OCR</strong> – 文字识别</li>
            <li><strong>OCRmyPDF</strong> – OCR 集成</li>
            <li><strong>python-docx</strong> – Word 导出</li>
            <li><strong>qtawesome</strong> – 图标</li>
            <li><strong>DeepSeek</strong> – 翻译支持（50+ 种语言）</li>
            <li><strong>所有用户</strong> – 感谢宝贵的反馈</li>
            <li><strong>开源社区</strong> – 感谢优秀的库</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "语言",
        'info_languages_header': "🌍 语言支持",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View 目前支持 <strong>62 种语言</strong> – 以确保该软件可在全球无障碍使用。</p>

            <p><strong>📖 完整语言列表（截至2026年3月）：</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 南非荷兰语</li>
                    <li>🇦🇱 阿尔巴尼亚语 (Shqip)</li>
                    <li>🇩🇿 阿拉伯语 (العربية)</li>
                    <li>🇮🇩 巴厘语 (Basa Bali)</li>
                    <li>🇧🇩 孟加拉语 (বাংলা)</li>
                    <li>🇲🇲 缅甸语 (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 波斯尼亚语 (Bosanski)</li>
                    <li>🇧🇬 保加利亚语 (Български)</li>
                    <li>🇨🇳 中文 (中文)</li>
                    <li>🇩🇰 丹麦语 (Dansk)</li>
                    <li>🇩🇪 德语</li>
                    <li>🇬🇧 英语 (English)</li>
                    <li>🇪🇪 爱沙尼亚语 (Eesti)</li>
                    <li>🇫🇮 芬兰语 (Suomi)</li>
                    <li>🇫🇷 法语 (Français)</li>
                    <li>🇬🇷 希腊语 (Ελληνικά)</li>
                    <li>🇮🇱 希伯来语 (עברית)</li>
                    <li>🇮🇳 印地语 (हिन्दी)</li>
                    <li>🇭🇷 克罗地亚语 (Hrvatski)</li>
                    <li>🇭🇺 匈牙利语 (Magyar)</li>
                    <li>🇮🇩 印度尼西亚语 (Bahasa Indonesia)</li>
                    <li>🇮🇪 爱尔兰语 (Gaeilge)</li>
                    <li>🇮🇸 冰岛语 (Íslenska)</li>
                    <li>🇮🇹 意大利语 (Italiano)</li>
                    <li>🇯🇵 日语 (日本語)</li>
                    <li>🇰🇭 高棉语 (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 韩语 (한국어)</li>
                    <li>🇱🇦 老挝语 (ພາສາລາວ)</li>
                    <li>🇱🇻 拉脱维亚语 (Latviešu)</li>
                    <li>🇱🇹 立陶宛语 (Lietuvių)</li>
                    <li>🇱🇺 卢森堡语 (Lëtzebuergesch)</li>
                    <li>🇲🇾 马来语 (Bahasa Melayu)</li>
                    <li>🇮🇳 马拉地语 (मराठी)</li>
                    <li>🇲🇳 蒙古语 (Монгол)</li>
                    <li>🇳🇵 尼泊尔语 (नेपाली)</li>
                    <li>🇳🇱 荷兰语 (Nederlands)</li>
                    <li>🇳🇴 挪威语 (Norsk)</li>
                    <li>🇦🇫 普什图语 (پښتو)</li>
                    <li>🇮🇷 波斯语 (فارسی)</li>
                    <li>🇵🇱 波兰语 (Polski)</li>
                    <li>🇵🇹 葡萄牙语 (Português)</li>
                    <li>🇮🇳 旁遮普语 (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 罗马尼亚语 (Română)</li>
                    <li>🇷🇺 俄语 (Русский)</li>
                    <li>🇸🇪 瑞典语 (Svenska)</li>
                    <li>🇷🇸 塞尔维亚语 (Српски)</li>
                    <li>🇸🇰 斯洛伐克语 (Slovenčina)</li>
                    <li>🇸🇮 斯洛文尼亚语 (Slovenščina)</li>
                    <li>🇪🇸 西班牙语 (Español)</li>
                    <li>🇹🇿 斯瓦希里语 (Kiswahili)</li>
                    <li>🇵🇭 他加禄语 (Filipino)</li>
                    <li>🇮🇳 泰米尔语 (தமிழ்)</li>
                    <li>🇮🇳 泰卢固语 (తెలుగు)</li>
                    <li>🇹🇭 泰语 (ไทย)</li>
                    <li>🇨🇿 捷克语 (Čeština)</li>
                    <li>🇹🇷 土耳其语 (Türkçe)</li>
                    <li>🇺🇦 乌克兰语 (Українська)</li>
                    <li>🇵🇰 乌尔都语 (اردو)</li>
                    <li>🇻🇳 越南语 (Tiếng Việt)</li>
                    <li>🇸🇳 沃洛夫语 (Wolof)</li>
                    <li>🇺🇸 意第绪语 (ייִדיש)</li>
                    <li>🇿🇦 祖鲁语 (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 添加自己的语言：</strong><br>
                想要尚未包含的语言？只需将您自己的词典文件 (<code>sprache_xx.py</code>) 放在应用程序旁边 – 软件会自动识别。如果您对特定翻译感兴趣，请随时与我联系。
            </div>

            <p><strong>🙏 特别感谢：</strong> DeepSeek 协助将所有词典翻译成 62 种语言。</p>

            <p>📧 翻译联系方式： <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "错误",
        'error_occurred': "发生错误",
        'error_pdf_load': "加载 PDF 时出错",
        'error_pdf_save': "保存 PDF 时出错",
        'error_ocr': "文本识别时出错",
        'error_no_pdf': "未加载 PDF",
        'error_page_not_found': "未找到页面",
        'error_invalid_range': "无效的页面范围",
        'error_file_not_found': "未找到文件",
        'error_permission': "没有权限",
        'error_unknown': "未知错误",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "成功",
        'success_operation': "操作成功完成",
        'success_saved': "保存成功",
        'success_exported': "导出成功",
        'success_imported': "导入成功",
        'success_deleted': "删除成功",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "确认",
        'confirm_yes': "是",
        'confirm_no': "否",
        'confirm_ok': "确定",
        'confirm_cancel': "取消",
        'confirm_delete': "删除",
        'confirm_overwrite': "覆盖",
        'confirm_continue': "继续",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "正在加载 PDF...",
        'progress_saving': "正在保存 PDF...",
        'progress_exporting': "正在导出 PDF...",
        'progress_processing': "正在处理...",
        'progress_wait': "请稍候...",
        'progress_preparing': "正在准备...",
        'progress_finalizing': "正在完成...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "白色",
        'color_black': "黑色",
        'color_red': "红色",
        'color_green': "绿色",
        'color_blue': "蓝色",
        'color_yellow': "黄色",
        'color_magenta': "品红",
        'color_cyan': "青色",
        'color_orange': "橙色",
        'color_gray': "灰色",
        'color_custom': "颜色选择",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&文件",
        'menu_edit': "&编辑",
        'menu_view': "&视图",
        'menu_tools': "&工具",
        'menu_settings': "&设置",
        'menu_help': "&帮助",
        'menu_language': "🌐 语言",
        'menu_guides': "&指南",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&打开",
        'file_save_as': "&另存为...",
        'file_protect': "&保护文档...",
        'file_export': "&导出",
        'file_export_pages': "导出为 Pages",
        'file_export_word': "导出为 DOCX",
        'file_export_text': "导出为 TXT",
        'file_print_now': "&立即打印",
        'file_print': "&打印",
        'file_close': "&关闭",
        'file_quit': "&退出",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&搜索",
        'edit_ocr': " 执行 OCR",
        'edit_rotate': "&旋转页面",
        'edit_rotate_all': "&旋转所有页面",
        'edit_delete_pages': "&删除页面",
        'edit_extract_pages': "&提取页面",
        'edit_insert_pages': "&插入页面",
        'edit_move_pages': "&移动页面",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " 插入文本和叉号",
        'text_insert': " 插入文本",
        'cross_insert': " 插入叉号",
        'text_customize': " 调整此文本",
        'cross_customize': " 调整此叉号",
        'cross_customize_all': " 调整所有叉号",
        'text_discard': " 丢弃此文本/叉号",
        'text_discard_all': " 丢弃所有文本和叉号",
        'text_save_all': " 保存所有文本和叉号",
        'text_guide': " 文本输入 / 文本块 - 指南",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " 插入签名",
        'signature_settings_menu': " 设置...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " 插入图像",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " 插入形状",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&显示文本窗口",
        'view_zoom': "&缩放",
        'view_zoom_page': "&页面宽度 (默认)",
        'view_zoom_two': "&两页",
        'view_zoom_overview': "&概览 (多页)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&辅助功能",
        'settings_voice': "语音输出",
        'settings_voice_tooltip': "用额外信息补充屏幕阅读器的语音输出",
        'settings_signature': "&签名设置",
        'settings_password': "&密码管理",
        'settings_backup': "更改前创建备份",
        'settings_export_import': "&导出 / 导入设置",
        'settings_export': "&导出所有设置...",
        'settings_import': "&导入所有设置...",
        'settings_export_info': "&导出什么？",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "开",
        'voice_off': "关",
        'voice_toggle': "语音输出 {0}",
        'voice_speed': "速度 {0}%",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "未找到工具：\n{0}\n\nBASE_DIR: {1}\n请确保在目录 {1} 中安装了 PDF 工具。",
        'tool_started': "{0} 已启动",
        'tool_start_failed': "无法启动",
        'process_error_failed_to_start': "无法启动进程。文件是否存在？",
        'process_error_crashed': "进程在启动时崩溃。",
        'process_error_timeout': "进程超时。",
        'process_error_write': "写入进程时出错。",
        'process_error_read': "从进程读取时出错。",
        'process_error_unknown': "未知的进程错误",
        'process_command': "命令",
        'process_normal_exit': "正常结束",
        'process_crashed': "崩溃",
        'process_nonzero_exit': "{0} 以错误代码 {1} 结束",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "正在取消...",
        'move_cancelling': "正在取消移动",
        'opening_pdf': "正在打开 PDF...",
        'loading_document': "正在加载文档...",
        'pdf_opened': "PDF 已打开",
        'pages_found_moving': "找到 {0} 页，{1} 页要移动",
        'creating_backup': "正在创建备份...",
        'backup_description': "正在备份原始文件...",
        'backup_saved_as': "已备份为: {0}",
        'error_format': "错误: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView 作者 BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "搜索已重置",
        'page_header_simple': "=== 第 {0} 页 ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "密码管理 – 指南",
        'password_guide_voice': "密码管理指南。请阅读注意事项。",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 密码管理 – 详细指南</strong></p>

        <p><strong>1. PDF 的密码保护</strong></p>
        <ul>
        <li>打开受密码保护的 PDF 时，会出现一个对话框，您可以在其中输入密码。</li>
        <li>您可以加密保存密码，这样就不必每次都重新输入（复选框“保存密码”）。</li>
        <li>使用“移除密码”按钮，您可以创建解密的 PDF 副本，并从数据库中删除密码。</li>
        </ul>

        <p><strong>2. 主密码</strong></p>
        <ul>
        <li>主密码保护对所有已保存 PDF 密码的访问。</li>
        <li><strong>设置：</strong> 转到“设置”→“密码管理”→“主密码设置”，然后单击“设置主密码”。选择一个强密码（至少 8 个字符）。</li>
        <li><strong>更改：</strong> 成功验证后，您可以更改主密码。</li>
        <li><strong>移除：</strong> 如果您删除主密码，所有已保存的密码将被永久删除。您可以在之前导出备份。</li>
        <li>每个会话一次，您必须使用主密码进行身份验证，才能访问受保护的功能（例如显示密码）。</li>
        </ul>

        <p><strong>3. 密码管理（列表）</strong></p>
        <ul>
        <li>在“设置”→“密码管理”下，您将打开一个表格，其中包含所有已保存的 PDF 及其加密密码。</li>
        <li><strong>无主密码：</strong> 您只能删除条目 – 密码保持隐藏。</li>
        <li><strong>有主密码（已验证）：</strong> 您可以查看、复制、导出和删除密码。</li>
        <li><strong>导出：</strong> 选择一种格式（JSON、CSV、TXT）并保存列表。如果设置了主密码，您可以决定密码是以明文形式导出还是继续加密导出。</li>
        <li><strong>导入：</strong> 以前导出的 ZIP 文件包含所有设置（包括密码）可以通过“设置”→“导出/导入设置”重新导入。注意：现有数据将被覆盖！</li>
        </ul>

        <p><strong>4. 密码生成器</strong></p>
        <ul>
        <li>在密码对话框中（例如保护 PDF 时），您会在输入框右侧找到一个骰子按钮 🎲。</li>
        <li>单击它以打开密码生成器。您可以设置长度、字符集（大写字母、小写字母、数字、特殊符号）和分隔符以提高可读性。</li>
        <li>生成的密码可以直接使用，如果需要也可以复制。</li>
        </ul>

        <p><strong>5. 重要安全提示</strong></p>
        <ul>
        <li>保存的密码使用 AES-256 加密存储。密钥来自您的主密码（如果已设置）或来自固定值（无主密码）。</li>
        <li>没有主密码，密码虽然被加密，但密钥存储在程序中 – 能够访问您文件的攻击者可以解密它们。因此，我们强烈建议使用主密码。</li>
        <li>密码数据库位于目录 `Daten/passwords.json` 中。定期备份，尤其是在删除主密码之前。</li>
        <li>如果主密码丢失，所有保存的密码将永久丢失。</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "反色模式",
        'invert_mode_classic': "经典（反转所有颜色）",
        'invert_mode_smart': "智能（仅反转亮度）",
        # ======== COMBOBOX =============
        'gray_threshold_label': "灰度阈值",
        'gray_threshold_10': "10%（严格）",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30%（默认）",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50%（柔和）",
        'threshold_changed': "阈值设置为 {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "灰度阈值 – 说明",
        'threshold_guide_text': "灰度阈值决定智能深色模式中哪些像素被视为'灰色'并被反转。\n\n"
                                "• 低值（10%）仅反转近乎完美的灰色调 – 彩色元素完全保留。\n"
                                "• 高值（50%）也会反转轻微着色的像素 – 这会增加对比度，但可能会扭曲颜色。\n\n"
                                "最佳值取决于文档。对于纯文本文档，30–40% 通常是理想的，对于彩色图形则更倾向于 10–20%。\n\n"
                                "您可以随时通过'设置'菜单调整该值 – PDF 将立即重新加载。\n\n"
                                "注意：\n* 照片和图像只能在浅色模式下正确显示！\n* 反色设置仅在深色模式激活时显示。",
        'threshold_guide_voice': "灰度阈值决定智能深色模式的干预强度。低值保护颜色，高值增加对比度。",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "正在打开 PDF...",
        'progress_loading_document': "正在加载文档...",
        'progress_pdf_opened': "PDF 已打开",
        'progress_creating_backup': "正在创建备份...",
        'progress_backup_description': "正在保护原始文件...",
        'progress_backup_created': "备份已创建",
        'progress_backup_saved_as': "已保存为：{0}",
        'progress_analyzing_start': "开始分析...",
        'progress_searching_empty': "正在搜索空白页...",
        'progress_page_empty': "第 {0} 页为空",
        'progress_page_keep': "保留第 {0} 页",
        'progress_analysis_complete': "分析完成",
        'progress_empty_found': "找到 {0} 个空白页",
        'progress_current_page': "当前页面",
        'progress_mark_delete': "正在标记为删除",
        'progress_range_selected': "页面范围 {0}-{1}",
        'progress_deleting_pages': "正在删除 {0} 页",
        'progress_creating_new_pdf': "正在创建新 PDF...",
        'progress_transferring_pages': "正在传输页面",
        'progress_keeping_page': "第 {0} 页将被保留 ({1}/{2})",
        'progress_saving_pdf': "正在保存 PDF...",
        'progress_optimizing': "正在优化文件大小...",
        'progress_finalizing': "正在完成...",
        'progress_new_size': "新大小：{0:.2f} MB",
        'progress_cancelling': "正在取消...",
        'progress_cancel_message': "正在取消 {0}",
        'progress_pages_found_moving': "找到 {0} 页，{1} 页待移动",

        # OCR-Fortschritt
        'ocr_status_analyzing': "正在分析 PDF...",
        'ocr_status_optimizing': "图像优化进行中...",
        'ocr_status_recognizing': "文字识别进行中...",
        'ocr_status_embedding': "正在嵌入文本...",
        'ocr_status_finalizing': "正在完成 PDF...",

        # PDF-Laden
        'progress_preparing': "准备中...",
        'progress_loading': "正在加载 PDF...",

        # Seitenoperationen
        'progress_deleting_title': "正在删除页面...",
        'progress_moving_title': "正在移动页面...",
        'pages_found': "找到的页面",
        'progress_creating_new_order': "正在创建新顺序...",
        'progress_sorting_pages': "正在排序页面...",
        'progress_moving_to_begin': "将 {0} 页移到开头",
        'progress_transferring_count': "传输 {0} 页",
        'progress_transferring_before_target': "在目标前传输页面",
        'progress_moving_pages': "移动 {0} 页",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_备份_",
        'filename_protected_suffix': "_受保护_",
        'filename_copy_suffix': "_副本",
        'filename_page_single': "_页_",
        'filename_page_range': "_页_",
        'filename_export_page': "_第{0:03}页",
        'filename_export_range': "_第{0}-{1}页",
        'filename_export_multiple': "_第{0}页",
        'filename_with_text': "_带文本",
        'filename_with_signature': "_带签名",
        'filename_with_image': "_带图像",
        'filename_with_forms': "_带形状",
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
        'view_toggle_navbar': "显示按钮栏",

		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "无法删除所有页面",
		'pages_cannot_delete_last_page': '无法删除最后一页！',
		'pages_cannot_delete_all_pages': '文档中必须至少保留一页！',
		'delete_pages_confirm': '确定要删除 {0} 页吗？',
		'delete_pages_confirm_voice': '确定要删除 {0} 页吗？',
		'pages_deleted': '成功删除了 {0} 页。',
		'warning': '警告',
		'error': '错误',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "未选择表单",
        'form_customized': "表单已自定义",

        # ============================================
        # 59. 扩展密码管理
        # ============================================
        'btn_select': "选择",
        'btn_use': "使用",
        'master_password_for_spasswords': "要存储和使用密码，必须先设置主密码。\n\n您想要立即设置主密码吗？",
        'open_saved_dialog_title': "打开已保存的文件",
        'open_saved_question': "您想要立即打开已保存的文件吗？",
        'password': "密码",
        'password_manager_master_required': "密码管理器仅在设置了主密码时才可用。\n\n您想要立即设置主密码吗？",
        'password_master_required_for_select': "要查看和选择已保存的密码，您必须首先使用主密码进行身份验证。\n\n您想要立即进行身份验证吗？",
        'password_not_available': "所选密码不可用或无法解密。",
        'password_options_title': "密码选项",
        'password_save_choice_change': "设置新密码",
        'password_save_choice_keep': "使用现有密码",
        'password_save_choice_none': "不加密保存",
        'password_save_hint': "首先设置主密码以安全存储密码。",
        'password_save_master_required': "保存密码（仅可使用主密码）",
        'password_save_question': "当前 PDF 受密码保护。您想要使用现有密码、设置新密码还是不加密保存？",
        'password_select': "选择密码",
        'password_select_none': "未选择密码。\n\n请从列表中选择一个密码。",
        'password_select_one': "请只选择一个密码。\n\n您标记了多个密码。",

        # ============================================
        # 60. 中央文件名生成（附加后缀）
        # ============================================
        'filename_backup_suffix': "_备份",
        'filename_insert_suffix': "_已插入",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_页面已删除",
        'filename_pages_moved': "_页面已移动",
        'filename_rotated_all_suffix': "_所有页面已旋转",
        'filename_rotated_suffix': "_页面已旋转",

        # ============================================
        # 61. 文件名设置（对话框）
        # ============================================
        'filename_settings_dialog_title': "更改 PDF 时的文件名配置",
        'filename_keep_suffixes': "保留先前的扩展名（例如 _带文本）",
        'filename_keep_suffixes_false': "替换",
        'filename_keep_suffixes_true': "保留",
        'filename_preview_label': "文件名预览：",
        'filename_preview_overwrite_hint': "预览不可用 – 原始文件将被覆盖。",
        'filename_separator': "单词之间的分隔符",
        'filename_separator_none': "无分隔符",
        'filename_separator_space': "空格 ( )",
        'filename_separator_underscore': "下划线 (_)",
        'filename_settings_saved': "文件名设置已保存",
        'filename_settings_title': "文件名格式化和备份",
        'filename_timestamp_position': "时间戳的位置",
        'filename_timestamp_position_after': "基础名称之后",
        'filename_timestamp_position_before': "最前面",
        'filename_timestamp_position_end': "在末尾",
        'filename_use_timestamp': "使用时间戳",

        # ============================================
        # 62. 更改时的行为（对话框）
        # ============================================
        'behavior_section': "<html><b>更改时的行为：</b><ul><li>删除和插入页面</li><li>插入文本、签名、图像和形状</li><li>OCR</li></ul></html>",
        'backup_section': "页面操作的备份（删除、移动）",
        'behavior_info': "注意：在“覆盖原始文件”时，时间戳和后缀将被忽略 – 文件保留其名称。",
        'behavior_new_file': "始终创建新文件（带有时间戳和后缀）",
        'behavior_overwrite': "覆盖原始文件（无新文件）",

        # ============================================
        # 63. 成功消息（新文件/覆盖）
        # ============================================
        'all_pages_rotated_new_file': "所有页面已旋转。\n\n原始文件保持不变。\n新文件：{0}",
        'all_pages_rotated_voice': "所有页面已旋转，已创建新文件。",
        'empty_pages_deleted_new_file': "已删除 {0} 个空白页。\n\n原始文件保持不变。\n新文件：{1}",
        'empty_pages_deleted_voice': "已删除 {0} 个空白页，已创建新文件。",
        'ocr_keep_original': "保留原始文件（稍后手动打开）",
        'ocr_new_file_question': "新的可搜索 PDF 已保存在：\n{0}\n\n您想要立即打开它吗？",
        'ocr_open_new': "打开新的 OCR 文件",
        'ocr_original_kept': "原始文件保持打开状态。OCR 文件已保存。",
        'page_deleted_new_file': "页面 {0} 已删除。\n\n原始文件保持不变。\n新文件：{1}",
        'page_deleted_voice': "页面 {0} 已删除，已创建新文件。",
        'page_rotated_new_file': "页面 {0} 已旋转。\n\n原始文件保持不变。\n新文件：{1}",
        'page_rotated_voice': "页面 {0} 已旋转，已创建新文件。",
        'pages_deleted_new_file': "已删除 {0} 页。\n\n原始文件保持不变。\n新文件：{1}",
        'pages_deleted_new_file_voice': "已删除 {0} 页，已创建新文件。",
        'pages_inserted_new_file': "已插入 {0} 页。\n\n原始文件保持不变。\n新文件：{1}",
        'pages_inserted_new_file_ask': "已插入 {0} 页。\n\n原始文件保持不变。\n新文件：{1}\n\n您想要立即打开它吗？",
        'pages_inserted_voice_new': "已插入 {0} 页，已创建新文件。",
        'pages_moved_new_file': "已移动 {0} 页。\n\n原始文件保持不变。\n新文件：{1}",
        'pages_moved_new_file_voice': "已移动 {0} 页，已创建新文件。",

        # ============================================
        # 64. 备份信息对话框
        # ============================================
        'backup_do_not_show': "不再显示",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 备份设置</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ 备份开启</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">对于所有覆盖原始文件的更改</strong>（文本、签名、图像、形状、OCR、旋转、插入、删除/移动页面），<strong>在应用更改之前会自动创建带有时间戳的备份</strong>。</p>
                <p style="margin: 5px 0 5px 20px;">• 备份位于原始文件旁边（例如 <code>文档_备份_20260412_120000.pdf</code>）。</p>
                <p style="margin: 5px 0 5px 20px;">• 如果您还启用了 <strong>„覆盖原始文件“</strong> 选项，也会创建备份。</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 备份关闭</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>不会创建任何备份</strong> – 无论是在覆盖时还是在页面操作时。</p>
                <p style="margin: 5px 0 5px 20px;">• 覆盖时原始文件可能会不可挽回地丢失。</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">仅推荐给有经验的用户！</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>提示：</strong> 备份设置与“覆盖原始文件”选项无关。您可以同时使用两者。<br>
                您可以永久隐藏此消息。
            </div>
        </div>
        """,
        'backup_info_title': "备份行为",
        'backup_info_voice': "关于页面操作时备份行为的通知。备份开启会覆盖原始文件，备份关闭会创建新文件。",
        'show_backup_info': "关于备份设置的信息",

        # ============================================
        # 65. 覆盖信息对话框
        # ============================================
        'overwrite_do_not_show': "不再显示",
        'overwrite_enable_backup': "启用备份（推荐）",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ 覆盖原始文件</p>
            <p>如果您启用此选项，更改（文本、签名、图像、形状、OCR、旋转、插入）将<strong>直接保存在原始文件中</strong> – <strong>不会创建新文件</strong>。</p>
            <p>• 文件名保持不变。<br>
            • 时间戳和后缀将被忽略。<br>
            • <strong>如果没有备份，原始文件可能会不可挽回地丢失。</strong></p>
            <p style="color: #FFD700;">建议：另外启用备份选项以获得自动备份。</p>
        </div>
        """,
        'overwrite_info_title': "覆盖原始文件",
        'overwrite_info_voice': "警告：覆盖原始文件 – 没有新文件。建议备份。",

        # ======================================================
        # 66. 成功消息（不同设置下）
        # ======================================================
        'pages_inserted_overwrite_with_backup': "已插入 {0} 页。\n\n原始文件已被覆盖。\n已创建备份。",
        'pages_inserted_overwrite_no_backup': "已插入 {0} 页。\n\n原始文件已被覆盖。\n未创建备份。",
        'texts_saved_overwrite_with_backup': "更改已保存在原始文件中。\n\n已创建备份。",
        'texts_saved_overwrite_no_backup': "更改已保存在原始文件中。\n\n未创建备份。",
        'texts_crosses_saved_new_file': "已插入 {0} {1} 和 {2} {3}。\n\n原始文件保持不变。\n已创建新文件。\n\n正在加载新的 PDF...",
        'texts_saved_new_file': "已插入 {0} {1}。\n\n原始文件保持不变。\n已创建新文件。\n\n正在加载新的 PDF...",
        'crosses_saved_new_file': "已插入 {0} {1}。\n\n原始文件保持不变。\n已创建新文件。\n\n正在加载新的 PDF...",
        'elements_saved_new_file': "已插入 {0} 个元素。\n\n原始文件保持不变。\n已创建新文件。\n\n正在加载新的 PDF...",
        'signatures_saved_overwrite_with_backup': "签名已保存在原始文件中。\n\n已创建备份。",
        'signatures_saved_overwrite_no_backup': "签名已保存在原始文件中。\n\n未创建备份。",
        'images_saved_overwrite_with_backup': "图像已保存在原始文件中。\n\n已创建备份。",
        'images_saved_overwrite_no_backup': "图像已保存在原始文件中。\n\n未创建备份。",
        'forms_saved_overwrite_with_backup': "形状已保存在原始文件中。\n\n已创建备份。",
        'forms_saved_overwrite_no_backup': "形状已保存在原始文件中。\n\n未创建备份。",
        'signatures_saved_new_file': "已插入 {0} 个签名。\n\n原始文件保持不变。\n已创建新文件。\n\n正在加载新的 PDF...",
        'images_saved_new_file': "已插入 {0} 张图像。\n\n原始文件保持不变。\n已创建新文件。\n\n正在加载新的 PDF...",
        'forms_saved_new_file': "已插入 {0} 个形状。\n\n原始文件保持不变。\n已创建新文件。\n\n正在加载新的 PDF...",

        # ======================================================
        # 67. 旋转页面的旋转
        # ======================================================
        'rotation_warning': "警告：此 PDF 包含旋转的页面。定位可能偏差。",
        'page_rotated_warning_title': "检测到旋转的页面",
        'page_rotated_warning_message': "当前页面 {0} 旋转了 {1}°。\n\n不支持在旋转的页面上插入元素。\n\n您想要立即将页面旋转到直立位置吗？",
        'page_rotated_warning_voice': "警告：页面已旋转。请先将其旋转。",
        'paste_on_rotated_page_simple_warning': "无法在页面 {0} 上插入！\n\n此页面旋转了 {1}°。\n\n请先将页面旋转到 0°（菜单：编辑 → 对齐页面）。\n\n警告：\n如果在旋转页面之前不保存，之前复制的元素将会丢失。",
        'paste_on_rotated_page_voice': "插入已取消。页面已旋转。请先对齐页面。",
        'page_rotated_cancel': "取消",
        'page_rotated_rotate_until_upright': "重复旋转页面（直到直立）",
        'page_rotated_now_upright': "页面现在已直立。您现在可以插入了。",
        'page_rotated_still_not_upright': "无法将页面旋转到直立位置。请手动修正。",

        # ============================================
        # 68. 问题页面帮助对话框
        # ============================================
        'help_rotated_pages_title': "帮助：修正旋转的页面",
        'help_rotated_pages_voice': "正在打开修正旋转页面的帮助。",
        'btn_help': "帮助",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 问题：旋转的页面 – 插入无法正常工作</p>

            <p>如果在旋转的页面上插入文本、签名或形状无法正常工作，您可以使用外部 PDF 编辑器修正该页面。</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ 使用外部工具解决（例如 macOS 预览）</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>导出页面</strong><br>
                &nbsp;&nbsp;在菜单中点击 <strong>文件 → 导出为页面</strong> 或使用其他方法将所需页面保存为单个 PDF。</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>在外部程序中打开页面</strong><br>
                &nbsp;&nbsp;在 PDF 编辑器中打开导出的 PDF（例如 <strong>macOS 预览</strong>、Adobe Acrobat、PDF Expert）。</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>旋转页面</strong><br>
                &nbsp;&nbsp;旋转页面使其直立（在预览中：<strong>工具 → 旋转</strong> 或 <strong>⌘ + R</strong>）。</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>保存</strong><br>
                &nbsp;&nbsp;保存修正后的页面（<strong>⌘ + S</strong>）。</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>将页面重新插入原始文档</strong><br>
                &nbsp;&nbsp;返回 PDFDarkView 并将修正后的页面插入到所需位置：<br>
                &nbsp;&nbsp;<strong>编辑 → 插入页面</strong>。</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 替代方案：在原始文件中旋转页面</p>
                <p style="margin: 5px 0 5px 20px;">• 使用内置的旋转功能（<strong>编辑 → 旋转页面</strong>）逐步修正页面。<br>
                • 每次旋转后，您可以检查插入是否现在可以正常工作。<br>
                • 这通常是更快的解决方案 – 请先尝试！</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>提示：</strong> 如果您经常遇到旋转的页面，您可以永久隐藏插入对话框中的警告。<br>
                定位可能因此偏差 – 仅当您了解后果时才使用此选项。
            </div>
        </div>
        """,

        # ============================================
        # 69. 旋转页面并重置为零度
        # ============================================
        'menu_rotate_normalize': "对齐页面",
        'menu_rotate_normalize_tooltip': "旋转页面或重置为 0°",
        'normalize_current_page': "将当前页面置于直立位置（设置为 0°）",
        'normalize_all_pages': "将所有页面置于直立位置（设置为 0°）",
        'page_normalized': "页面 {0} 已设置为直立位置。",
        'all_pages_normalized': "所有页面已设置为直立位置。",
        'page_already_upright': "页面 {0} 已直立。",
        'all_pages_already_upright': "所有页面均已直立。",

        # ============================================
        # 70. 导出消息
        # ============================================
        'export_ocr_question_html': "<p>PDF 不包含可搜索的文本。</p><p>您想要执行 OCR 以导出到 {0} 吗？</p>",
        'export_ocr_voice': "PDF 不包含文本。导出到 {0} 需要 OCR。",
        'export_no_ocr_possible': "无法在没有 OCR 的情况下导出。请通过菜单执行 OCR。",
        'ocr_failed_export_not_possible': "OCR 失败。无法执行导出。",

        # ============================================
        # 71. 打印（附加消息）
        # ============================================
        'print_preview_start': "PDF 将在预览中打开。请在那里开始打印过程。",
        'print_preview_manual': "PDF 已打开。请手动执行打印命令（例如 Ctrl+P）。",

        # ============================================
        # 72. 合并 PDF
        # ============================================
        'merge_pdfs_title': "合并 PDF",
        'merge_pdfs': "合并 PDF",
        'merge_progress_title': "正在合并 PDF...",
        'merge_pdfs_list': "按顺序排列的 PDF（拖放以排序）",
        'merge_add_pdf': "添加 PDF",
        'merge_remove': "移除",
        'merge_move_up': "上移",
        'merge_move_down': "下移",
        'merge_pdfs_info': "💡 提示：您可以通过拖放更改顺序",
        'merge_no_pdfs': "未选择 PDF。点击“添加 PDF”。",
        'merge_info': "已选择 {0} 个 PDF（约 {1} 页）",
        'merge_open_file': "打开文件",
        'merge_merge': "合并",
        'merge_error': "合并时出错",
        'merge_min_two_pdfs_error': "请至少选择两个 PDF 文件进行合并。",
        'merge_select_pdfs': "选择要合并的 PDF",
        'merge_error_file': "处理时出错",
        'merge_cancelled': "合并已取消",
        'merge_preparing': "正在准备...",
        'merge_processing': "正在处理第 {0} 个 PDF，共 {1} 个",
        'merge_saving': "正在保存合并后的 PDF...",
        'merge_complete': "完成！",
        'merge_success_title': "合并成功",
        'merge_success_voice': "{0} 个 PDF 已成功合并。",
        'merge_success_message': "{0} 个 PDF 已成功合并。\n\n新文档现在有 {1} 页。\n\n新文件：\n{2}\n\n保存位置：\n{3}\n{2}\n\n您想要打开此 PDF 吗？",
        'replace_file_title': "替换文件？",
        'replace_file_message': "已有一个 PDF 打开。您想要用新文件替换它吗？",
        'btn_yes': "是",
        'btn_no': "否",
        'filename_merge_suffix': "已合并",

        # ============================================
        # 73. 合并的进度消息
        # ============================================
        'progress_merge_opening': "正在打开 {0}...",
        'progress_merge_reading': "正在读取 {0}...",
        'progress_merge_adding': "正在添加 {0} 页...",
        'progress_merge_optimizing': "正在优化 PDF...",
        'progress_merge_writing': "正在写入 PDF...",

        # ============================================
        # 74. 关闭前保存
        # ============================================
        'action_close_pdf': "关闭 PDF",
        'action_close_window': "关闭窗口",
        'action_open_new_pdf': "打开新的 PDF",
        'action_quit_app': "退出应用程序",
        'changes_saved': "更改已保存。",
        'file_close_title': "关闭 PDF 文件",
        'save_before_action': "是否应在 {0} 之前保存更改？是或否？",
        'save_before_action_voice': "是否应在 {0} 之前保存更改？是或否？",
        'save_before_close_question': "是否应在关闭前保存更改？是或否？",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>已创建可搜索的 PDF：\n\n{0}\n\n<b>如需，请重试",
        "ocr_rotate_title": "OCR 前对齐页面",
        "ocr_rotate_question": "PDF 包含旋转的页面。\n是否要在 OCR 前将所有页面对齐到 0°？\n这将显著提高文本识别率。",
        "ocr_rotate_yes": "是，对齐",
        "ocr_rotate_no": "否，直接开始 OCR",
        "ocr_rotate_voice": "PDF 包含旋转的页面。是否应在 OCR 前将所有页面对齐？",
        "ocr_not_performed_message": "没有文本。请执行 OCR（菜单“编辑”→“执行 OCR”或按 Ctrl+R）。",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR 设置",
        "ocr_language_btn": "选择 OCR 语言",
        "ocr_language": "OCR 语言",
        "ocr_language_current": "当前语言：",
        "ocr_param_info": "参数信息",

        "ocr_force_ocr_label": "强制 OCR",
        "ocr_deskew_label": "校正倾斜",
        "ocr_clean_label": "清理图像",
        "ocr_oversample_label": "分辨率 (DPI)",
        "ocr_pagesegmode_label": "页面分割",
        "ocr_oem_label": "OCR 引擎模式",
        "ocr_optimize_label": "PDF 压缩",
        "ocr_jobs_label": "并行进程",
        "ocr_verbose_label": "日志详细程度",

        "ocr_force_ocr_tooltip": "强制对每一页进行 OCR，即使已存在文本",
        "ocr_deskew_tooltip": "自动对齐倾斜的扫描",
        "ocr_clean_tooltip": "从图像中去除噪声和伪影",
        "ocr_oversample_tooltip": "在 OCR 前将图像放大到此 DPI",
        "ocr_pagesegmode_tooltip": "确定页面如何划分为文本区域",
        "ocr_oem_tooltip": "选择 Tesseract 的 OCR 引擎",
        "ocr_optimize_tooltip": "输出 PDF 的压缩级别",
        "ocr_jobs_tooltip": "并行 OCR 进程的数量",
        "ocr_verbose_tooltip": "日志输出的详细程度",
        "ocr_settings_explain_btn": "说明",

        "ocr_force_ocr_explain": "强制在<b>每个</b>页面上进行文本识别（即使已包含文本）。\n\n建议：对于扫描的 PDF 启用，对于已有文本的原生 PDF 禁用。",

        "ocr_deskew_explain": "校正轻微倾斜的扫描（最多约 5°）。\n\n建议：对于扫描文档启用，如果页面已完全平直则禁用。",

        "ocr_clean_explain": "从图像中去除噪点、点和小伪影。\n<b>重要：</b>对于带有变音符号（字母上方/下方的点）的阿拉伯语、泰语或越南语文本，应<b>禁用</b>此选项，否则重要字符可能会丢失。",

        "ocr_oversample_explain": "在文本识别<b>之前</b>将图像放大到指定的 DPI。<br><br>• <b>72-150 DPI：</b>非常快，但识别率低<br>• <b>200-300 DPI：</b>最佳范围（默认：300）<br>• <b>400+ DPI：</b>几乎没有更好的识别，但文件显著增大<br><br>建议：复杂文字（阿拉伯语、中文、日文）使用 300 DPI，西方语言使用 200 DPI。",

        "ocr_pagesegmode_explain": "确定 Tesseract 如何将页面划分为文本区域。\n\n• <b>3 - 自动（默认）：</b>适用于混合布局\n• <b>4 - 单列：</b>适用于单列文本\n• <b>5 - 垂直块：</b>适用于垂直文字（日文、中文）\n• <b>6 - 统一文本块：</b>适用于无列流式文本\n• <b>11 - 原始图像：</b>适用于低质量扫描/手写体\n\n建议：简单文本文档用 <b>6</b>，复杂布局用 <b>3</b>。",

        "ocr_oem_explain": "选择 Tesseract 的 OCR 引擎。\n\n• <b>0 - Legacy：</b>旧引擎（快速，但精度较低）\n• <b>1 - LSTM：</b>神经引擎（较慢，但更精确）\n• <b>2 - Legacy + LSTM：</b>结合两种结果\n• <b>3 - 默认（首选 LSTM）：</b>大多数情况下的最佳选择\n\n建议：为获得最大识别精度，选择 <b>3</b>。",

        "ocr_optimize_explain": "压缩输出 PDF。\n\n• <b>0：</b>无优化（最快处理）\n• <b>1：</b>轻度优化（良好的折衷）\n• <b>2：</b>中度优化\n• <b>3：</b>强力优化（文件最小，但较慢）\n\n建议：日常使用选 <b>1</b>。",

        "ocr_jobs_explain": "OCR 的并行进程数。\n\n• <b>1：</b>慢，但内存消耗最低\n• <b>4-8：</b>适合现代多核处理器\n• <b>12+：</b>高内存使用下几乎不更快\n\n建议：CPU 核心数（例如 4 核系统上选 <b>4</b>）。",

        "ocr_verbose_explain": "控制台日志输出的详细程度。\n\n• <b>0：</b>无输出\n• <b>1：</b>进度和状态消息\n• <b>2：</b>详细输出\n• <b>3：</b>完整调试输出（非常广泛）\n\n建议：正常操作用 <b>1</b>。",

        "ocr_reset_title": "设置已重置",
        "ocr_reset_message": "所有 OCR 设置已重置为默认值。",
        "info_tooltip": "关于此参数的更多信息",
        "ocr_reset_defaults": "重置为默认值",

        "ocr_psm_0": "自动（Legacy 引擎）",
        "ocr_psm_1": "自动列检测",
        "ocr_psm_3": "自动（默认）",
        "ocr_psm_4": "单列",
        "ocr_psm_5": "垂直块",
        "ocr_psm_6": "统一文本块",
        "ocr_psm_7": "单行文本",
        "ocr_psm_8": "单个单词",
        "ocr_psm_11": "原始图像（无布局分析）",

        "ocr_oem_0": "Legacy 引擎（快速）",
        "ocr_oem_1": "LSTM 引擎（神经，精确）",
        "ocr_oem_2": "Legacy + LSTM 组合",
        "ocr_oem_3": "默认（首选 LSTM）",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR 语言...",
        "ocr_language_title": "选择 OCR 语言",
        "ocr_language_instruction": "选择文本识别（OCR）的语言。\n注意：多种语言会牺牲性能和准确性！\n只选择一种语言可获得最佳效果。",
        "ocr_language_predefined": "预定义组合",
        "ocr_language_custom": "自定义...",
        "ocr_language_selected": "已选择的 OCR 语言",
        "ocr_language_changed": "OCR 语言已更改为 {0}",
        "ocr_language_auto_detect": "可用语言将被自动检测。",
        "ocr_language_none_found": "未找到 Tesseract 语言数据！请安装语言包（例如 'tesseract-ocr-deu', 'tesseract-ocr-eng'）。",
        "ocr_language_select_custom": "自定义语言选择",
        "ocr_language_available": "可用语言（已安装）：",
        "ocr_language_select_hint": "选择一种或多种语言：",
        "ocr_language_confirm": "应用",
        "ocr_language_reset": "重置为默认值 (deu+eng+vie)",
        "ocr_language_priorities": "推荐语言（预装）：",

        "select_all_languages": "全选",
        "clear_all_languages": "清除选择",
        "install_language_packs": "安装缺失的语言包...",
        "install_hint": "💡 提示：并非所有语言都已安装在您的系统上。通过此按钮您将获得安装帮助。",
        "ocr_language_install_title": "Tesseract 语言包安装",

        "ocr_missing_languages": "缺失的 OCR 语言包",
        "ocr_missing_languages_message": "以下所选语言未安装在您的系统上：\n\n{0}\n\n请安装缺失的语言包（请参阅“安装帮助”中的帮助）。\n\n是否立即打开安装帮助？",
        "ocr_missing_languages_voice": "缺失语言包。请安装缺失的语言。",
        "ocr_install_help_now": "打开帮助",
        "ocr_continue_anyway": "仍然尝试",
        "ocr_language_error_title": "OCR 语言错误",
        "ocr_language_error_message": "文本识别期间出错：{0}\n\n请检查您的 OCR 语言设置（设置 → OCR 语言）。",
        "ocr_install_help_button": "安装帮助",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 安装 Tesseract 语言包</p>

        <p>要使 OCR 以特定语言工作，相应的语言数据必须安装在您的系统上。请按照您的操作系统的说明操作：</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS（Homebrew）</p>
        <ol>
        <li>打开<strong>终端</strong>（Finder → 程序 → 实用工具 → 终端）。</li>
        <li>使用以下命令安装所有可用语言：<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        （这可能需要几分钟。）</li>
        <li>或仅安装单个语言（例如越南语）：<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        对于当前版本的 Homebrew，可能需要手动下载 <code>*.traineddata</code>（见下文）。</li>
        <li>安装后：关闭此对话框并重新打开 OCR 语言选择 – 新语言将自动出现。</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux（Debian/Ubuntu）</p>
        <ol>
        <li>打开终端（Ctrl+Alt+T）。</li>
        <li>安装所需语言，例如越南语：<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        重要语言代码：<code>deu</code>（德语），<code>eng</code>（英语），<code>vie</code>（越南语），<code>spa</code>（西班牙语），<code>fra</code>（法语），<code>ita</code>（意大利语），<code>nld</code>（荷兰语），<code>fin</code>（芬兰语），<code>swe</code>（瑞典语），<code>nor</code>（挪威语）。</li>
        <li>显示所有可用软件包：<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows（手动）</p>
        <ol>
        <li>从以下地址下载所需的 <code>*.traineddata</code> 文件：<br>
        <a href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        （例如越南语的 <code>vie.traineddata</code>）。</li>
        <li>将文件复制到 Tesseract 语言文件夹，通常为：<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        （根据个人安装情况进行调整。）</li>
        <li>重新启动应用程序（或重新打开 OCR 语言选择）。</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 所有系统的替代方法</p>
        <ul>
        <li>使用您选择的包管理器安装 <strong>OCRmyPDF</strong> 和 <strong>Tesseract</strong>。大多数安装已包含一些标准语言（英语、德语、法语）。</li>
        <li>缺失的语言可以随时安装 – OCR 语言选择仅列出实际存在的语言。</li>
        </ul>

        <hr>
        <p><b>✅ 安装后：</b>无需重新启动应用程序 – 新添加的语言将立即出现在列表中。</p>
        <p><b>📖 语言代码帮助：</b>完整列表可在 <a href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract 文档</a>中找到。</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans 字体",
        "info_noto_font_voice": "Noto Sans 字体安装指南",
        "btn_info_noto_font_install": "字体信息",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ 如何安装 Google 的免费 Noto 字体</h2>

        <p><strong>Noto 字体</strong>是 Google 的一个开源字体家族。其目标是看不到<em>“豆腐”</em>（即没有空框 □）并正确显示 Unicode 标准中的每个字符。它们是需要在多种不同语言中显示文本的应用程序的理想补充。</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 在 macOS 上安装</h3>

        <p><strong>方法1：使用 Homebrew（适用于高级用户）</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>方法2：通过“字体册”（推荐）</strong></p>

        <ol>
        <li>下载官方字体包：<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>解压 ZIP 文件</li>
        <li>将文件复制到 <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 在 Windows 上安装（10 和 11）</h3>

        <p><strong>方法1：Microsoft Store（推荐）</strong><br>
        搜索“Google Noto Fonts”或“Noto Sans”，然后单击<strong>安装</strong>。</p>

        <p><strong>方法2：手动安装</strong></p>

        <ol>
        <li>下载：<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>解压 ZIP</li>
        <li>选择 .ttf / .otf 文件</li>
        <li>右键单击 → <strong>安装</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        或<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\用户名\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 在 Linux 上安装</h3>

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

        <p>验证：<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "管理书签",
        "bookmark_add": "添加书签",
        "bookmark_add_tooltip": "将当前页面保存为书签",
        "bookmark_remove": "删除书签",
        "bookmark_remove_tooltip": "删除标记的书签",
        "bookmark_remove_all": "删除全部",
        "bookmark_remove_all_tooltip": "删除此 PDF 的所有书签",
        "bookmark_jump": "跳转到书签",
        "bookmark_jump_tooltip": "跳转到所选页面",
        "bookmark_name": "名称",
        "bookmark_page": "页面",
        "bookmark_no_bookmarks": "没有书签。\n单击“添加”将当前页面保存为书签。",
        "bookmark_added": "已添加页面 {0} 的书签：{1}",
        "bookmark_removed": "已删除书签：{0}",
        "bookmark_all_removed": "已删除所有书签。",
        "bookmark_name_default": "第 {0} 页",
        "bookmark_name_prompt": "书签名称：\n（长文本将缩短为 50 个字符）",
        "bookmark_name_prompt_title": "书签名称",
        "bookmark_confirm_remove_all": "您确定要删除所有 {0} 个书签吗？",
        "menu_bookmarks": "书签",
        "bookmark_manage": "管理书签",
        "bookmark_next": "下一个书签",
        "bookmark_prev": "上一个书签",
        "bookmark_page_display": "第 {0} 页",
        "bookmark_exists": "此页面已存在此名称的书签。",
        "bookmark_select_first": "请先选择一个书签。",
        "bookmark_confirm_remove": "您确定要删除书签“第 {0} 页：{1}”吗？",
        "bookmark_jumped_to": "已跳转到第 {1} 页的书签“{0}”。",
        "bookmark_jumped_to_voice": "书签 {0}，第 {1} 页",
        "btn_close": "关闭",

        "bookmark_list": "您的书签",
        "bookmark_rename": "重命名书签",
        "bookmark_rename_tooltip": "更改所选书签的名称",
        "bookmark_rename_title": "重命名书签",
        "bookmark_rename_prompt": "第 {0} 页上书签的新名称：\n（最多 50 个字符）",
        "bookmark_renamed": "书签“{0}”已重命名为“{1}”。",
        "bookmark_item_tooltip": "第 {0} 页：{1}\n双击跳转",
        "bookmark_name_exists_question": "此页面上已存在名称为“{0}”的书签。\n仍然重命名吗？",

        "context_bookmarks": "书签",
        "context_bookmark_add_here": "为此页面添加书签",
        "context_bookmarks_existing": "现有书签：",
        "context_bookmarks_jump": "跳转到书签：",
        "context_bookmarks_none": "没有书签",
        "context_bookmarks_clear_all": "删除全部 {0} 个书签",

        "bookmark_search_placeholder": "搜索书签...（名称或页面）",
        "bookmark_search_results": "找到 %d 个书签匹配“%s”",
        "bookmark_no_search_results": "未找到匹配“%s”的书签",
        "bookmark_no_search_results_label": "“%s”没有结果",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "编辑 PDF 元数据",
        "metadata_title": "标题",
        "metadata_title_placeholder": "文档标题",
        "metadata_title_tooltip": "文档的标题（显示在标题栏中）",
        "metadata_author": "作者",
        "metadata_author_placeholder": "作者姓名",
        "metadata_author_tooltip": "文档的创建者",
        "metadata_subject": "主题",
        "metadata_subject_placeholder": "文档的主题",
        "metadata_subject_tooltip": "内容的简短描述",
        "metadata_keywords": "关键词",
        "metadata_keywords_placeholder": "用逗号分隔的关键词",
        "metadata_keywords_tooltip": "用于分类文档的关键词",
        "metadata_creator": "创建者",
        "metadata_creator_placeholder": "创建 PDF 的应用程序",
        "metadata_creator_tooltip": "创建文档所使用的软件",
        "metadata_producer": "生产者",
        "metadata_producer_placeholder": "转换 PDF 的应用程序",
        "metadata_producer_tooltip": "转换 PDF 的软件",
        "metadata_creation_date": "创建日期",
        "metadata_creation_date_tooltip": "文档创建日期",
        "metadata_mod_date": "修改日期",
        "metadata_mod_date_tooltip": "最后修改日期",
        "metadata_pdf_info": "📄 PDF 信息",
        "metadata_pages": "页数",
        "metadata_file_size": "文件大小",
        "metadata_pdf_version": "PDF 版本",
        "metadata_encrypted": "已加密",
        "metadata_encrypted_yes": "是（受密码保护）",
        "metadata_encrypted_no": "否",
        "metadata_reload": "📂 从 PDF 重新加载",
        "metadata_reset": "放弃更改",
        "metadata_reloaded": "已从 PDF 重新加载元数据。",
        "metadata_reset_done": "已重置所有元数据字段。",
        "metadata_no_file": "未加载 PDF 文件。",
        "metadata_save_error": "保存元数据时出错",
        "metadata_saved": "元数据已成功保存。",
        "metadata_pdf_version_unknown": "PDF（未知）",
        "metadata_saved_message": "元数据已成功保存。",
        "metadata_saved_voice": "元数据已保存。",

        "metadata_custom": "🔧 自定义元数据",
        "metadata_custom_placeholder": "{\n  \"我的字段\": \"我的值\",\n  \"其他字段\": 123\n}",
        "metadata_custom_tooltip": "自定义元数据的 JSON 格式（可选）",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "已选择模板“{0}” - 双击插入",
        "text_use_template": "使用文本块",
        "text_type": "类型",
        "text_search_templates": "搜索文本块...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 导出 / 导入信息",
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

        <h3>📦 导出什么？（概述）</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">常规应用程序设置</span></li>
            <li class="detail">• 深色/浅色模式</li>
            <li class="detail">• 图像的深色模式反转</li>
            <li class="detail">• 灰度阈值</li>
            <li class="detail">• 语言</li>
            <li class="detail">• 窗口几何形状</li>
            <li class="detail">• 缩放模式</li>
            <li class="detail">• 导航（导航栏可见）</li>
            <li class="detail">• 语音输出（开/关）</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">备份设置</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">文件命名（时间戳、分隔符、后缀）</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">插入设置</span></li>
            <li class="detail">• 签名</li>
            <li class="detail">• 文本和文本块</li>
            <li class="detail">• 勾选标记、图像和形状</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR 设置</span></li>
            <li class="detail">• 语言</li>
            <li class="detail">• 强制 OCR · 页面模式</li>
            <li class="detail">• 图像预处理：校正倾斜、清理、过采样</li>
            <li class="detail">• 并行作业数</li>
            <li class="detail">• 反转模式</li>
            <li class="detail">• 灰度阈值</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">书签</span></li>
            <li class="detail">• 每个 PDF 文件的所有书签（页面、名称、创建时间）</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">密码数据库</span></li>
            <li class="detail">• 保存的 PDF 密码（可选加密或纯文本）</li>
            <li class="detail">• 主密码哈希（如果已设置）</li>
            <li class="detail">• 验证数据</li>
        </ul>

        <h4>⚠️ 重要说明</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 导入时：</strong>
            <ul>
                <li><span class="warning">➜ 所有当前设置将被完全覆盖</span></li>
                <li>• 必须重启应用程序</li>
                <li>• 现有的签名、文本块和书签将被替换</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 主密码和导出模式：</strong>
            <ul>
                <li>• 当主密码激活时，您可以选择：</li>
                <li>  - <span style="color: #98FB98;"><strong>已解密</strong></span>（密码在 ZIP 中以纯文本形式存在）</li>
                <li>  - <span style="color: #FFA07A;"><strong>已加密</strong></span>（只能在目标系统上用主密码读取）</li>
                <li>• 主密码哈希<strong>始终</strong>以加密形式存储</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ 安全提示：</strong>
            <ul>
                <li>• 导出的 ZIP 文件包含敏感数据（<strong>密码、书签、签名</strong>）</li>
                <li>• 请将其安全存放（例如加密的 U 盘、密码管理器）</li>
                <li>• 如果文件丢失，保存的 PDF 密码将无法恢复地丢失</li>
            </ul>
        </div>

        <h4>📁 导出格式</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            设置将保存到一个 ZIP 文件中：<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            此 ZIP 包含完整的 <code>settings.json</code>（来自您的配置）以及可能嵌入的签名图像文件和加密的密码。
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "签名 - 指南",
        'signature_guide_html': """
        📝 <strong>签名 - 快速指南</strong><br>
        <ul>
        <li>设置主密码</li>
        <li>在<em>设置</em>菜单中配置签名（大小、时间戳等）</li>
        <li>在所需位置<strong>右键单击</strong>插入（每次会话需要一次主密码）</li>
        <li>用鼠标或箭头键移动签名</li>
        <li>连续插入多个签名</li>
        <li>单独自定义每个签名</li>
        <li>丢弃单个签名</li>
        <li>一次性保存/丢弃所有签名</li>
        <li>或者，也可以使用菜单栏。</li>
        </ul>
        """,
        'signature_guide_voice': "签名快速指南。设置主密码。在设置中配置签名。右键单击插入。",

        'image_guide_title': "插入图片 - 指南",
        'image_guide_html': """
        📷 <strong>在PDF中插入图片 - 快速指南</strong><br>
        <ol>
        <li>在所需位置右键单击</li>
        <li><em>„插入图片“</em> → 选择图片</li>
        <li>定位图片：用鼠标拖动</li>
        <li>调整大小：在角/边缘拖动</li>
        <li>保持宽高比：按<strong>[A]</strong>键</li>
        <li>更多调整：在图片上右键单击</li>
        </ol>
        <p><strong>提示：</strong>在上下文菜单中您可以调整设置。</p>
        """,
        'image_guide_voice': "图片快速指南。右键单击，插入图片，选择。用鼠标定位，在角上调整大小。用A键保持宽高比。",

        'form_guide_title': "插入形状 - 指南",
        'form_guide_html': """
        📐 <strong>在PDF中插入形状 - 快速指南</strong><br>
        <ol>
        <li>选择形状类型（矩形、椭圆、线条、箭头）</li>
        <li>点击位置：
            <ul>
            <li>对于矩形/椭圆：单击一次放置形状</li>
            <li>对于线条/箭头：单击两次设置起点和终点</li>
            </ul>
        </li>
        <li>定位形状：用鼠标拖动</li>
        <li>调整大小：在角/边缘拖动</li>
        <li>保存形状：按<strong>Enter</strong></li>
        <li>丢弃形状：按<strong>ESC</strong></li>
        <li>更多调整：在形状上右键单击</li>
        </ol>
        <p><strong>提示：</strong>在上下文菜单中您可以调整设置。</p>
        """,
        'form_guide_voice': "形状快速指南。选择形状类型。对于矩形或椭圆单击一次，对于线条或箭头单击两次。用鼠标定位，在角上调整大小。按Enter保存，按Escape丢弃。",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "上一个",
        "btn_next_result": "下一个",
        "ocr_text_window": "OCR文本窗口",
        "bookmark_existing": "现有书签",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR比较 Mac - Windows",
        'ocr_method_mac_win_title': "Mac和Windows之间的OCR差异",
        'ocr_method_mac_win_voice': "Mac更好",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – macOS和Windows之间的差异</strong></p>

        <p><strong>macOS（推荐）</strong></p>
        <p>工具：</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>结果：</p>
        <ul>
        <li>带有嵌入文本的可搜索PDF，很大程度上保留原始布局。</li>
        </ul>
        <p>优点：</p>
        <ul>
        <li>出色的文本识别质量（即使在歪斜的页面上）。</li>
        <li>保留矢量图形和字体。</li>
        <li>通过子进程评估的GUI进度条。</li>
        <li>完全控制所有OCR参数（Deskew、Clean、Oversample、优化）。</li>
        <li>文本搜索直接在主窗口（PDF视图）中可用。</li>
        </ul>
        <p>缺点：</p>
        <ul>
        <li>需要额外的系统工具（ocrmypdf、Ghostscript、unpaper、pngquant – 包含在应用程序包中）。</li>
        <li>更复杂的错误处理（死锁、超时）。</li>
        </ul>

        <p><strong>Windows（稳定的替代方案）</strong></p>
        <p>工具：</p>
        <ul>
        <li>pytesseract（直接连接到Tesseract）+ reportlab + PyPDF2</li>
        </ul>
        <p>结果：</p>
        <ul>
        <li>一个可搜索的PDF，在视觉上相当于图像PDF，但可通过透明文本进行搜索。</li>
        </ul>
        <p>优点：</p>
        <ul>
        <li>目前想不出任何优点。</li>
        </ul>
        <p>缺点：</p>
        <ul>
        <li>PDF本质上是一张带有不可见文本的图像；对于复杂文档（列、表格），布局可能会略有偏差。</li>
        <li>没有自动倾斜校正（--deskew）或图像清理（--clean）。</li>
        <li>GUI进度条仅根据处理的页数粗略更新。</li>
        <li>OCR速度稍慢（因为每页单独处理）。</li>
        <li>文本搜索被重定向到OCR文本窗口。</li>
        </ul>

        <p><strong>共同点</strong></p>
        <ul>
        <li>两种方法在与源文件相同的目录中创建可搜索的PDF。</li>
        <li>OCR设置（语言、DPI、页面分段模式、OCR引擎模式）可通过OCRSettingsDialog配置，并在两种实现中生效。</li>
        </ul>

        <p><strong>建议：</strong></p>
        <ul>
        <li>macOS：ocrmypdf二进制文件提供最佳结果 – 购买Mac并使用该版本（适用于Apple Silicon或Intel芯片的Mac的PDFDarkView）。OCR结果比Windows下更好！</li>
        <li>Windows：使用pytesseract解决方案。它稳定且为大多数文档提供完全足够的质量。</li>
        </ul>

        <p><strong>重要提示：</strong></p>
        <ul>
        <li>两个版本完全集成在用户界面中 – 用户不会注意到任何差异。</li>
        <li>程序根据操作系统自动决定使用哪个OCR引擎。</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "创建签名（从扫描）",
        "signature_create_title": "选择扫描的签名（PDF/图片）",
        "image_pdf_filter": "图片和PDF",
        "signature_pdf_empty": "PDF不包含任何页面。",
        "signature_created_success": "签名创建成功：{0}",
        "signature_create_error": "创建签名时出错：\n{0}",
        "rembg_missing": "未安装rembg。\n请安装：pip install rembg\n错误：{0}",
        "signature_name_title": "签名的文件名",
        "signature_name_message": "请为新签名输入文件名（将保存为带透明背景的PNG）：",
        "signature_name_label": "文件名：",
        "signature_name_voice": "输入签名的文件名",
        "signature_processing": "处理中...",
        "signature_creation_title": "正在创建签名",
        "signature_overwrite_warning": "文件'{0}'已存在。是否覆盖？",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"准备PDF以签名",
        "signature_prepare_instruction":"请选择一个PDF，它在单页上包含扫描的签名。\n\n要获得最佳识别效果，请确保：\n• 签名是用黑色墨水（圆珠笔或细线笔）在白纸上书写的。\n• 签名位于原本空白的A4页面的上三分之一处。\n• PDF以至少300 dpi扫描。\n• 签名清晰且不太细。\n• 没有干扰性的背景图案或线条。",
        "signature_prepare_voice":"请选择带有扫描签名的PDF。注意良好的质量和对比度。",
        "sig_thickness_label":"线条粗细：",
        "sig_thickness_normal":"普通（细）",
        "sig_thickness_bold":"粗（推荐）",
        "sig_thickness_very_bold":"非常粗",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "添加GUI和OCR语言 - 指南",
        'language_guide_title': "添加GUI和OCR语言",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>从以下位置下载所需的翻译文件<code>translations_xy.py</code><br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        并将其放入以下目录：</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>打开您的网页浏览器。</li>
        <li>转到：<a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>在屏幕右边缘找到“Releases”，然后选择标记为<strong>“latest”</strong>的那个。</li>
        <li>在下一个发布页面上，下载最底部的<code>Source Code.zip</code>文件。</li>
        <li>解压ZIP文件。</li>
        <li>在解压的文件夹中找到您需要的所有语言文件，并将它们复制到目录：<br/>
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
        "menu_watermark":"插入水印",
        "fullpage_text_watermark_title":"文字水印",
        "fullpage_image_watermark_title":"图片水印",
        "filename_with_watermark":"_带水印",
        "watermark_text":"文字：",
        "watermark_text_placeholder":"您的水印文字...",
        "watermark_font_family":"字体：",
        "watermark_font_size":"字号：",
        "watermark_format":"格式：",
        "watermark_bold":"粗体",
        "watermark_italic":"斜体",
        "watermark_color":"颜色：",
        "watermark_choose_color":"选择颜色...",
        "watermark_opacity":"不透明度 / 透明度：",
        "watermark_direction":"阅读方向：",
        "watermark_direction_l_r":"左 → 右",
        "watermark_direction_bl_tr":"左下 → 右上",
        "watermark_direction_tl_br":"左上 → 下",
        "watermark_direction_b_t":"下 → 上",
        "watermark_direction_t_b":"上 → 下",
        "watermark_preview":"预览：",
        "watermark_preview_sample":"示例文字",
        "watermark_empty_text":"请输入文字。",
        "watermark_applied":"水印已应用于所有页面。",
        "watermark_saved":"水印已保存。",
        "image_scale":"大小：",
        "image_preview":"图片预览：",
        "no_image_selected":"未选择图片",
        "browse":"浏览...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "编辑限制",
        "redact_add_black": "编辑限制（黑色）",
        "redact_add_white": "编辑限制（白色 / 擦除）",
        "redact_added_black": "已添加黑色编辑限制",
        "redact_added_white": "已添加白色编辑限制",
        "redact_apply_all": "应用所有编辑限制并保存",
        "redact_discard_all": "放弃所有编辑限制",
        "redact_discard": "放弃此编辑限制",
        "no_redactions": "无编辑限制",
        "redact_confirm_title": "永久应用编辑限制",
        "redact_confirm_message": "警告：标记区域将被永久删除（黑色或白色）。\n将创建备份（如已启用）。\n\n继续？",
        "redact_apply": "是，立即应用编辑限制",
        "redact_saved": "已成功应用并保存 {0} 个编辑限制。",
        "redact_saved_voice": "已应用 {0} 个编辑限制",
        "redact_error": "应用编辑限制时出错",
        "filename_redacted":"_已编辑限制",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': '插入页码',
        'page_numbers_format': '编号格式：',
        'page_numbers_format_arabic': '1, 2, 3 ...（阿拉伯数字）',
        'page_numbers_format_roman_lower': 'i, ii, iii ...（罗马小写）',
        'page_numbers_format_roman_upper': 'I, II, III ...（罗马大写）',
        'page_numbers_format_letter': 'A, B, C ...（字母）',
        'page_numbers_format_custom': '自定义',
        'page_numbers_custom_pattern': '模式：',
        'page_numbers_custom_placeholder': '例如 "第{nummer}页" 或 "{nummer} / {total}"',
        'page_numbers_custom_tooltip': '使用 {nummer} 表示当前页码，{total} 表示总页数',
        'page_numbers_position': '位置：',
        'page_numbers_pos_tl': '左上',
        'page_numbers_pos_tc': '上中',
        'page_numbers_pos_tr': '右上',
        'page_numbers_pos_ml': '左中',
        'page_numbers_pos_mc': '居中',
        'page_numbers_pos_mr': '右中',
        'page_numbers_pos_bl': '左下',
        'page_numbers_pos_bc': '下中',
        'page_numbers_pos_br': '右下',
        'page_numbers_margins': '边距：',
        'page_numbers_margin_x': '水平距离：',
        'page_numbers_margin_y': '垂直距离：',
        'page_numbers_range': '页面范围：',
        'page_numbers_all_pages': '所有页面',
        'page_numbers_custom_range': '自定义范围',
        'page_numbers_from': '从：',
        'page_numbers_to': '到：',
        'page_numbers_progress': '正在插入页码...',
        'page_numbers_start': '正在开始插入页码...',
        'page_numbers_cancel': '页码插入已取消',
        'page_numbers_success': '页码已成功添加。\n\n是否打开新PDF？\n\n{0}',
        'page_numbers_complete': '页码已添加',
        'page_numbers_error_format': '插入页码时出错：{0}',
        'page_numbers_content_type': '内容类型：',
        'page_numbers_tab_simple': '简单数字',
        'page_numbers_tab_range': '第X页/共Y页',
        'page_numbers_tab_date': '日期',
        'page_numbers_tab_custom': '自由文本',
        'page_numbers_range_format': '格式：',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': '第{aktuell}页/共{gesamt}页',
        'page_numbers_range_custom': '自定义',
        'page_numbers_range_placeholder': '例如 "第{aktuell}页 / 共{gesamt}页"',
        'page_numbers_date_format': '日期格式：',
        'page_numbers_date_short': '2024.01.01',
        'page_numbers_date_long': '2024年1月1日',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': '自定义',
        'page_numbers_date_placeholder': '例如 %Y年%m月%d日 %H:%M',
        'page_numbers_date_position': '位置：',
        'page_numbers_date_before': '日期在页码前',
        'page_numbers_date_after': '日期在页码后',
        'page_numbers_date_only': '仅日期（无页码）',
        'page_numbers_custom_text': '自定义文本：',
        'page_numbers_custom_placeholder_text': '使用 {seite} 表示页码，{gesamt} 表示总页数\n例如 "机密 - 第{seite}页" 或 "{seite} / {gesamt}"',
        "filename_with_page_number":"_带页码",
        "filename_with_page_declaration":"_带页面声明",
        "filename_with_pagenumber":"_带页码",
        "filename_with_date":"_带日期",
        "filename_with_my_page_declaration":"_带自定义页面声明",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "未保存的更改",
        "unsaved_changes_message_darkmode": "存在未保存的插入内容。\n是否在切换前保存？",
        "save_and_switch": "保存并切换",
        "discard_and_switch": "立即切换",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': '将页面导出为图片',
        'export_images_menu': '导出为图片（PNG/JPEG）',
        'export_images_format': '图片格式：',
        'export_images_dpi': '分辨率（DPI）：',
        'export_images_quality': 'JPEG质量：',
        'export_images_range': '页面范围：',
        'export_images_all_pages': '所有页面',
        'export_images_custom_range': '自定义范围',
        'export_images_from': '从：',
        'export_images_to': '到：',
        'export_images_options': '选项：',
        'export_images_single_files': '每页作为单独文件',
        'export_images_subfolder': '导出到子文件夹',
        'export_images_subfolder_info': '到子文件夹 "PDF名称_图片"',
        'export_images_same_folder': '与PDF在同一文件夹',
        'export_images_apply_darkmode': '应用PDFDarkView设置（深色模式）',
        'export_images_target_folder': '目标文件夹：',
        'export_images_browse': '浏览...',
        'export_images_preview': '预览：',
        'export_images_preview_info': '选择导出设置',
        'export_images_preview_info_detail': '{0} 页导出为 {1}\n分辨率：{2} DPI\n文件名：{3}\n{4}',
        'export_images_select_folder': '选择目标文件夹',
        'export_images_start': '正在开始导出图片...',
        'export_images_progress': '正在导出图片...',
        'export_images_saving': '正在保存第 {0}/{1} 页...',
        'export_images_success': '导出成功！\n\n已保存 {0} 张图片到：\n{1}',
        'export_images_complete': '图片导出完成',
        'export_images_open_folder': '📁 打开文件夹',
        'export_images_cancel': '图片导出已取消',
        'export_images_error_format': '导出图片时出错：{0}',
        'export_images_pdf2image_missing': '未安装 "pdf2image" 库。\n\n请使用以下命令安装：\npip install pdf2image\n\nWindows 系统还需要 Poppler：\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A转换用于长期存档',
        'pdfa_menu': 'PDF/A转换（适合存档）',
        'pdfa_info': '将PDF转换为PDF/A格式。\n\nPDF/A专为长期存档设计，确保文档在未来能够正确显示。',
        'pdfa_standard': 'PDF/A标准：',
        'pdfa_standard_select': '版本：',
        'pdfa_1': 'PDF/A-1（简单，广泛兼容）',
        'pdfa_2': 'PDF/A-2（现代，更好的压缩）',
        'pdfa_3': 'PDF/A-3（最新版本，允许附件）',
        'pdfa_standards_explanation': '📖 标准说明：\n\n'
            '• PDF/A-1：基础，兼容旧系统（约2005年）\n'
            '• PDF/A-2：更现代，更好的压缩，支持透明度（约2011年）\n'
            '• PDF/A-3：最新版本，允许嵌入文件附件（约2013年）\n\n'
            '建议：PDF/A-2是兼容性和现代功能之间的良好折中。',
        'pdfa_options': '选项：',
        'pdfa_compress_enable': '压缩PDF（更小的文件）',
        'pdfa_metadata_preserve': '保留元数据（标题、作者等）',
        'pdfa_target_folder': '目标文件夹：',
        'pdfa_browse': '浏览...',
        'pdfa_select_folder': '选择目标文件夹',
        'pdfa_ocr_info_unknown': '🔍 无法检查文本内容。',
        'pdfa_ocr_info_not_needed': '✅ 文本可用 - 无需OCR。\n可直接创建PDF/A。',
        'pdfa_ocr_info_recommended': '⚠️ 未找到足够的文本。\n\n对于可搜索的PDF，建议先运行OCR。\n注意：PDF/A无需OCR也可工作 - 但文本将不可搜索。',
        'pdfa_ocr_info_error': '❌ 检查时出错：{0}',
        'pdfa_start': '正在开始PDF/A转换...',
        'pdfa_progress': '正在执行PDF/A转换...',
        'pdfa_success': 'PDF/A转换成功！\n\n已保存为：\n{0}\n\n是否打开新的PDF？',
        'pdfa_complete': 'PDF/A转换完成',
        'pdfa_cancel': 'PDF/A转换已取消',
        'pdfa_error_format': 'PDF/A转换时出错：\n\n{0}',
        'pdfa_ocrmypdf_missing': '未安装 "ocrmypdf" 库。\n\n请使用以下命令安装：\npip install ocrmypdf',
        'btn_convert': '转换',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': '优化PDF（减小文件大小）',
        'optimize_menu': '优化PDF（文件大小）',
        'optimize_info': '通过多种优化方法减小PDF文件大小。\n\n压缩级别越高，文件越小 - 但图片质量可能下降。',
        'optimize_level': '压缩级别：',
        'optimize_level_low': '低（快速，少量节省）',
        'optimize_level_medium': '中（良好折中）',
        'optimize_level_high': '高（大量节省）',
        'optimize_level_maximum': '最大（最大节省，较慢）',
        'optimize_level_explanation': '建议："中"是速度和文件大小之间的良好折中。',
        'optimize_options': '选项：',
        'optimize_compress_images': '压缩图片（降低JPEG质量）',
        'optimize_clean_objects': '删除未使用的对象',
        'optimize_preserve_metadata': '保留元数据（标题、作者等）',
        'optimize_image_quality': '图片质量：',
        'optimize_range': '页面范围：',
        'optimize_all_pages': '所有页面',
        'optimize_custom_range': '自定义范围',
        'optimize_from': '从：',
        'optimize_to': '到：',
        'optimize_target_folder': '目标文件夹：',
        'optimize_browse': '浏览...',
        'optimize_select_folder': '选择目标文件夹',
        'optimize_info_box': '信息',
        'optimize_info_text': '大型PDF的优化可能需要几分钟。\n\n图片将以降低的质量保存，这可以显著减小文件大小。',
        'optimize_start': '正在开始PDF优化...',
        'optimize_progress': '正在优化PDF...',
        'optimize_cancel': 'PDF优化已取消',
        'optimize_complete': 'PDF优化完成',
        'optimize_error_format': 'PDF优化时出错：\n\n{0}',
        'optimize_success_message': 'PDF优化成功！\n\n已保存为：\n{0}\n\n优化前：{1}\n优化后：{2}\n节省：{3:.1f}%\n\n{4}\n\n是否打开优化后的PDF？',
        'optimize_success_message_no_size': 'PDF优化成功！\n\n已保存为：\n{0}\n\n大小信息不可用。\n\n是否打开优化后的PDF？',
        'optimize_result_positive': '文件已减小 {0:.1f}%。',
        'optimize_result_zero': '文件大小无变化。',
        'optimize_result_negative': '文件增大了 {0:.1f}%。\n已跳过优化，保留原始文件。',
        'btn_optimize': '开始优化',
        'filename_optimize_low_suffix': '_优化_低',
        'filename_optimize_medium_suffix': '_优化',
        'filename_optimize_high_suffix': '_优化_高',
        'filename_optimize_maximum_suffix': '_优化_最大',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': '裁剪PDF',
        'crop_menu': '裁剪PDF（Crop）',
        'crop_range': '应用于：',
        'crop_all_pages': '所有页面',
        'crop_current_page': '仅当前页面',
        'crop_values': '裁剪值（以点为单位）：',
        'crop_left': '左：',
        'crop_right': '右：',
        'crop_top': '上：',
        'crop_bottom': '下：',
        'crop_presets': '预设：',
        'crop_preset_white': '检测白色边距',
        'crop_reset': '重置',
        'crop_mouse_hint': '🖱️ 拖动矩形大致选择区域。\n然后可以在SpinBox中精确调整数值。\n无法使用鼠标手动调整。',
        'crop_apply': '裁剪',
        'crop_scope_all': '所有页面',
        'crop_scope_current': '当前页面',
        'crop_new_size': '新尺寸：{0:.0f} x {1:.0f} pt',
        'crop_no_pdf': '未加载PDF',
        'crop_preview_error': '加载预览时出错',
        'crop_start': '正在开始裁剪...',
        'crop_progress': '正在裁剪PDF...',
        'crop_success': 'PDF裁剪成功！\n\n已保存为：\n{0}\n\n是否打开裁剪后的PDF？',
        'crop_complete': '裁剪完成',
        'crop_cancel': '裁剪已取消',
        'crop_error_format': '裁剪时出错：\n\n{0}',
        'filename_crop_suffix': '_已裁剪',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': '压平PDF（Flatten）',
        'flatten_menu': '压平PDF（Flatten）',
        'flatten_info': '压平PDF会将所有可编辑元素"烧入"页面内容中。\n\n之后，表单字段、注释、文本、叉号、签名、图片和形状将无法单独编辑。',
        'flatten_explanation_title': '📖 这有什么用？',
        'flatten_explanation_text': '压平在以下情况下需要：\n\n'
            '• 📄 准备打印文档\n'
            '• 🔒 防止他人更改表单字段\n'
            '• 📎 将注释和评论"永久"嵌入文档\n'
            '• 🖼️ 将插入的文本、叉号、签名、图片和形状永久固定在文档中\n'
            '• 📦 准备文件用于存档\n\n'
            '压平使PDF更小，并防止元素被意外移动或删除。',
        'flatten_what_title': '什么被压平？',
        'flatten_what_list': '• ✅ 表单字段（文本字段、复选框、按钮）\n'
            '• ✅ 注释（评论、高亮、笔记）\n'
            '• ✅ 叠加层（文本、叉号、签名、图片、形状）',
        'flatten_options': '选项：',
        'flatten_forms': '压平表单字段',
        'flatten_annotations': '压平注释',
        'flatten_overlays': '压平叠加层（文本、叉号、签名、图片、形状）',
        'flatten_target_folder': '目标文件夹：',
        'flatten_browse': '浏览...',
        'flatten_select_folder': '选择目标文件夹',
        'flatten_warning': '⚠️ 重要：压平是不可逆的过程！\n\n压平后，可编辑元素将无法单独修改或删除。\n如有需要，请事先创建备份。',
        'flatten_apply': '压平',
        'flatten_start': '正在开始压平...',
        'flatten_progress': '正在压平PDF...',
        'flatten_success': 'PDF压平成功！\n\n已保存为：\n{0}\n\n是否打开压平后的PDF？',
        'flatten_complete': '压平完成',
        'flatten_cancel': '压平已取消',
        'flatten_error_format': '压平时出错：\n\n{0}',
        'filename_flatten_suffix': '_已压平',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'PDF叠加（Overlay）',
        'overlay_menu': 'PDF叠加（Overlay）',
        'overlay_info': '将一个PDF（叠加层）放在另一个PDF之上。\n\n叠加PDF被放置在基础PDF之上。这适用于水印、徽标、信头或印章。',
        'overlay_explanation_title': '📖 这有什么用？',
        'overlay_explanation_text': '叠加在以下情况下需要：\n\n'
            '• 🏢 将公司徽标作为水印放在每页上\n'
            '• 📄 将信头放在空白PDF上\n'
            '• 🖊️ 在文档上放置印章叠加层\n'
            '• 🔖 在所有页面上放置水印\n'
            '• 📑 在模板上放置表单叠加层',
        'overlay_type': '叠加类型：',
        'overlay_type_fullpage': '整页（覆盖）',
        'overlay_type_transparent': '整页（透明 - 推荐）',
        'overlay_type_stamp': '印章（可定位）',
        'overlay_type_info_fullpage': '📄 叠加PDF被精确地放置在整个页面上。\n可以移除白色背景，以便只显示内容。',
        'overlay_type_info_transparent': '🔍 叠加PDF以透明背景放置在整个页面上。\n白色背景自动移除 - 非常适合水印和徽标！',
        'overlay_type_info_stamp': '🖊️ 叠加PDF作为印章被定位和缩放。\n非常适合在特定位置的徽标、印章或签名。',
        'overlay_remove_background': '移除白色背景：',
        'overlay_remove_background_enable': '从叠加PDF中移除白色背景（使叠加层透明）',
        'overlay_remove_background_tooltip': '从叠加PDF中移除白色区域，使下方的文本可见。',
        'overlay_threshold': '阈值：',
        'overlay_threshold_hint': '（1-254，越高 = 移除更多白色）',
        'overlay_select_file': '选择叠加PDF：',
        'overlay_file_placeholder': '请选择用于叠加的PDF文件',
        'overlay_browse': '浏览...',
        'overlay_select_overlay': '选择叠加PDF',
        'overlay_range': '页面范围：',
        'overlay_all_pages': '所有页面',
        'overlay_custom_range': '自定义范围',
        'overlay_from': '从：',
        'overlay_to': '到：',
        'overlay_position': '位置：',
        'overlay_position_center': '居中',
        'overlay_position_top_left': '左上',
        'overlay_position_top_right': '右上',
        'overlay_position_bottom_left': '左下',
        'overlay_position_bottom_right': '右下',
        'overlay_size': '大小：',
        'overlay_size_original': '原始大小',
        'overlay_size_fit_page': '适应页面',
        'overlay_size_custom': '自定义（%）',
        'overlay_opacity': '透明度：',
        'overlay_target_folder': '目标文件夹：',
        'overlay_browse_folder': '浏览...',
        'overlay_select_folder': '选择目标文件夹',
        'overlay_warning': '⚠️ 注意：叠加PDF被放置在基础PDF上并"烧入"其中。\n\n保存后，叠加PDF的元素将无法单独编辑。',
        'overlay_apply': '叠加',
        'overlay_start': '正在开始叠加...',
        'overlay_progress': '正在叠加PDF...',
        'overlay_success': 'PDF叠加成功！\n\n已保存为：\n{0}\n\n是否打开叠加后的PDF？',
        'overlay_complete': '叠加完成',
        'overlay_cancel': '叠加已取消',
        'overlay_error_format': '叠加时出错：\n\n{0}',
        'overlay_no_file': '未选择叠加PDF。\n\n请选择要叠加的PDF文件。',
        'filename_overlay_suffix': '_已叠加',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': '从PDF中提取图片',
        'extract_images_menu': '提取所有图片',
        'extract_images_info': '从PDF中提取所有图片并保存为单独的文件。\n\n图片以原始格式保存或转换为所选格式。',
        'extract_images_format': '图片格式：',
        'extract_images_quality': 'JPEG质量：',
        'extract_images_options': '选项：',
        'extract_images_subfolder': '提取到子文件夹（"PDF名称_图片"）',
        'extract_images_unique': '仅唯一图片（避免重复）',
        'extract_images_range': '页面范围：',
        'extract_images_all_pages': '所有页面',
        'extract_images_custom_range': '自定义范围',
        'extract_images_from': '从：',
        'extract_images_to': '到：',
        'extract_images_target_folder': '目标文件夹：',
        'extract_images_browse': '浏览...',
        'extract_images_select_folder': '选择目标文件夹',
        'extract_images_info_box': '信息',
        'extract_images_info_text': '大型PDF的提取可能需要几分钟。\n\n图片以原始名称保存（页面_图片）。',
        'extract_images_extract': '提取',
        'extract_images_start': '正在开始提取...',
        'extract_images_progress': '正在提取图片...',
        'extract_images_success': '✅ 图片提取成功！\n\n已保存 {0} 张图片到：\n{1}',
        'extract_images_complete': '图片提取完成',
        'extract_images_cancel': '提取已取消',
        'extract_images_error_format': '提取图片时出错：\n\n{0}',
        'extract_images_open_folder': '📁 打开文件夹',
        'extract_images_no_images': '在PDF中未找到图片。',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': '一页多版（N-Up）',
        'nup_menu': '一页多版（N-Up）',
        'nup_info': '将多个PDF页面排列在一页上。\n\n适用于紧凑打印、概览或讲义。',
        'nup_layout': '布局：',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': '预览：',
        'nup_preview_info': '{0} 页 → 每张 {1} 页 → {2} 张\n布局：{3}',
        'nup_order': '顺序：',
        'nup_order_horizontal': '水平（逐行）',
        'nup_order_vertical': '垂直（逐列）',
        'nup_order_horizontal_reverse': '水平反向',
        'nup_order_vertical_reverse': '垂直反向',
        'nup_range': '页面范围：',
        'nup_all_pages': '所有页面',
        'nup_custom_range': '自定义范围',
        'nup_from': '从：',
        'nup_to': '到：',
        'nup_options': '选项：',
        'nup_margins': '边距：',
        'nup_margin_between': '页面间距：',
        'nup_page_numbers': '插入页码',
        'nup_target_folder': '目标文件夹：',
        'nup_browse': '浏览...',
        'nup_select_folder': '选择目标文件夹',
        'nup_create': '创建',
        'nup_start': '正在开始N-Up...',
        'nup_progress': '正在创建N-Up...',
        'nup_success': 'N-Up创建成功！\n\n已保存为：\n{0}\n\n是否打开新的PDF？',
        'nup_complete': 'N-Up完成',
        'nup_cancel': 'N-Up已取消',
        'nup_error_format': 'N-Up时出错：\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': '更改页面大小',
        'pagesize_menu': '更改页面大小',
        'pagesize_info': '更改PDF的页面大小。\n\n内容自动适应新大小。',
        'pagesize_format': '格式：',
        'pagesize_select': '选择标准格式：',
        'pagesize_custom': '自定义大小：',
        'pagesize_width': '宽度：',
        'pagesize_height': '高度：',
        'pagesize_orientation': '方向：',
        'pagesize_portrait': '纵向',
        'pagesize_landscape': '横向',
        'pagesize_scale_options': '缩放选项：',
        'pagesize_fit': '适应（保持宽高比）',
        'pagesize_stretch': '拉伸（变形）',
        'pagesize_center': '居中（原始大小）',
        'pagesize_range': '页面范围：',
        'pagesize_all_pages': '所有页面',
        'pagesize_custom_range': '自定义范围',
        'pagesize_from': '从：',
        'pagesize_to': '到：',
        'pagesize_target_folder': '目标文件夹：',
        'pagesize_browse': '浏览...',
        'pagesize_select_folder': '选择目标文件夹',
        'pagesize_apply': '应用',
        'pagesize_start': '正在开始更改页面大小...',
        'pagesize_progress': '正在更改页面大小...',
        'pagesize_success': '页面大小更改成功！\n\n已保存为：\n{0}\n\n是否打开新的PDF？',
        'pagesize_complete': '页面大小更改完成',
        'pagesize_cancel': '页面大小更改已取消',
        'pagesize_error_format': '更改页面大小时出错：\n\n{0}',
        'pagesize_preview_info': '新大小：{0} x {1} pt',
        'filename_pagesize_suffix': '_新大小',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF信息',
        'pdf_info_menu': '显示PDF信息',
        'pdf_info_voice': '正在显示PDF信息',
        'pdf_info_error': '显示PDF信息时出错：\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "显示键盘快捷键",
        "shortcuts_dialog_title": "键盘快捷键",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 文件</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>打开PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>关闭PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>另存为...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>保护文档</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>打印</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>立即打印（macOS）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>退出应用程序</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 导出</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>导出为Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>导出为DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>导出为TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>导出为图片（macOS）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>提取图片</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ 文档处理</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up（多页）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A转换（macOS）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>压平PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF叠加</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>优化PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ 编辑</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>搜索</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>添加书签</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>管理书签</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>下一个书签</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>上一个书签</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>运行OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 页面管理</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>旋转当前页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>旋转所有页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>规范化当前页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>规范化所有页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>删除页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>提取页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>插入页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>移动页面</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>合并PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>更改页面大小</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 插入</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>插入文本</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>插入叉号</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>插入签名1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>插入签名2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>插入图片</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>插入矩形</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>插入椭圆</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>插入线条</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>插入箭头</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>插入页码</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>文字水印</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>图片水印</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ 编辑限制</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>编辑限制（黑色）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>编辑限制（白色）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>应用所有编辑限制</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ 高级</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>裁剪PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>编辑元数据</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ 视图</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>切换深色/浅色模式</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>显示文本窗口</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>页面宽度（缩放）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>两页（缩放）</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>概览（缩放）</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ 设置</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>密码管理</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR设置</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>签名设置</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>文件名格式</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>导出设置</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>导入设置</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ 信息</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>显示PDF信息</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>切换语音输出</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>聚焦菜单栏</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "有新版本可用",
        "update_available_message": "有新版本 <b>{0}</b>。\n\n请访问发布页面下载更新：\n{1}",
        "update_available_voice": "新版本 {0} 可用。请从 GitHub 页面下载更新。",
        "update_open_release": "打开发布页面",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "下载所有翻译",
        "ask_download_all_translations": """除德语、英语和越南语外，还有 {total_languages} 种 GUI 语言可用。\n\n是否要提供 / 更新它们？\n\n注意：\n不需要的语言您可以稍后在目录中手动删除：\n{translations_path}
        \n如果您取消，您可以稍后通过“工具 → 更新翻译”菜单下载 GUI 语言。""",
        "menu_update_translations": "更新翻译",
        "translations_updated": "翻译已更新",
        "translations_update_success": "{} 个翻译已成功更新（{} 个新，{} 个已更新）。",
        "translations_update_error": "更新翻译时出错",
        "translations_update_no_changes": "所有翻译已是最新。",
        "translations_update_offline": "没有网络连接。无法更新翻译。",
        "translations_update_in_progress": "正在后台更新翻译...",
        "translations_downloading": "正在下载翻译...",
        "translations_path_hint": "翻译的用户目录",
        "translations_update_not_available_title": "更新不可用",
        "translations_update_not_available_message": """更新翻译仅在已安装版本中可用。\n\n在开发模式下，翻译已是最新。""",
        "translations_update_no_internet_title": "没有网络连接",
        "translations_update_no_internet_message": """无法建立网络连接。\n\n无法从 GitHub 下载翻译。\n\n可能的解决方案：
        • 检查您的网络连接
        • 暂时禁用任何防火墙
        • 稍后重试
        \n您也可以手动从 GitHub 下载翻译：
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "更新已在进行中",
        "btn_retry": "重试",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "欢迎使用 PDF Dark View",
        "welcome_title_not_supported": "欢迎使用 PDF Dark View",
        "welcome_message": "欢迎使用 PDF Dark View！\n\n您的系统语言被检测为“{language}”。\n您是否要使用此语言作为用户界面语言？\n\n您可以随时通过“设置 → 语言”更改语言。",
        "welcome_message_language_not_available": "欢迎使用 PDF Dark View！\n\n您的系统语言被检测为“{language}”。\n此语言尚未安装。\n\n您是否要立即从 GitHub 下载 {language} 的翻译？\n\n（然后该语言将自动用于用户界面。）",
        "welcome_message_language_not_supported": "欢迎使用 PDF Dark View！\n\n您的系统语言被检测为“{language}”。\n很遗憾，此语言尚没有翻译。\n\n用户界面将显示为 {fallback_language}。\n\n您可以随时通过“设置 → 语言”更改语言。\n如果您愿意，您也可以为您的语言贡献翻译：\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "是，使用系统语言",
        "welcome_keep_english": "否，保留英语",
        "welcome_download_language": "是，下载 {language}",

        # ============================================
        # 107. 最近使用的路径
        # ============================================

        'menu_recent': '最近使用',
        'menu_recent_dirs': '目录...',
        'menu_recent_files': '文件...',
        'recent_manage': '管理...',
        'recent_enable_tracking': '保存最近使用的路径（隐私）',
        'recent_enable_info': '禁用此选项以不保存路径',
        'recent_tracking_disabled': '路径跟踪已禁用',
        'recent_enabled': '已启用',
        'recent_disabled': '已禁用',
        'recent_tracking_status': '路径跟踪 {0}',
        'recent_dialog_title': '最近使用的路径',
        'recent_tab_directories': '目录',
        'recent_tab_files': '文件',
        'recent_dirs_instruction': '双击以在目录中打开文件对话框',
        'recent_files_instruction': '双击以直接打开 PDF',
        'recent_no_directories': '(没有保存的目录)',
        'recent_no_files': '(没有保存的文件)',
        'recent_default_current': '⭐ 默认: {0}',
        'recent_set_as_default': '⭐ 设为默认',
        'recent_default_set_title': '默认目录已设置',
        'recent_default_set_message': '目录 "{0}" 已设置为打开 PDF 的默认目录。',
        'recent_default_set_voice': '默认目录已设置',
        'recent_directory_not_found': '未找到目录',
        'recent_file_not_found': '未找到文件',
        'recent_remove_selected': '移除',
        'recent_remove_title': '移除路径',
        'recent_remove_confirm': '您确定要从列表中移除路径 "{0}" 吗？',
        'recent_path_removed': '路径已移除',
        'recent_clear_all': '全部移除',
        'recent_clear_title': '移除所有路径',
        'recent_clear_confirm_type': '您确定要删除所有 {0} 吗？',
        'recent_cleared': '列表已清空',
        'recent_path_not_found_title': '未找到路径',
        'recent_path_not_found_message': '路径 "{0}" 已不存在。',
        'recent_open_file': '打开文件',
        'btn_open_recent': '打开',
        'recent_open_file_question': '您想将 "{0}" 作为 PDF 打开吗？',
        'recent_not_pdf': '选中的文件不是 PDF。',
        'recent_more_entries': '更多条目...',
        'btn_remove': '移除',
        'btn_clear': '全部清除',
        'recent_context_open': '打开',
        'recent_context_reveal': '在 Finder 中显示',
        'recent_context_set_default': '⭐ 设为默认',
        'recent_context_open_terminal': '💻 打开终端',
        'recent_context_file_info': '文件信息',
        'recent_context_open_with_default': '📄 用默认应用打开',
        'recent_context_remove': '从列表中移除',
        'recent_context_clear_all': '全部移除',
        'recent_file_info_title': '文件信息',
        'recent_file_info_name': '名称',
        'recent_file_info_path': '路径',
        'recent_file_info_size': '大小',
        'recent_file_info_modified': '修改日期',
        'recent_file_info_pages': '页数',
        'recent_error_reveal': '在 Finder 中打开时出错',
        'recent_error_terminal': '打开终端时出错',
        'recent_error_info': '获取文件信息时出错',
        'open_user_data_folder': '显示用户数据目录',

        # ============================================
        # 108. 删除偶数/奇数页
        # ============================================
        "pages_delete_even": "删除所有偶数页",
        "pages_delete_odd":  "删除所有奇数页",
        "progress_even_pages": "正在删除偶数页",
        "progress_odd_pages": "正在删除奇数页",
        "progress_mark_delete_even": "{} 个偶数页已标记为删除",
        "progress_mark_delete_odd":  "{} 个奇数页已标记为删除",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "程序正在退出",

    }
