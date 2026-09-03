
# ============================================
# translations_en.py - English dictionary
# Fully sorted by categories
# Comments in German for consistency
# ============================================

def load_english_strings():
    """Loads all English strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Open PDF",
        'btn_text_window': "OCR Text",
        'btn_first': "First Page",
        'btn_prev': "Previous Page",
        'btn_next': "Next Page",
        'btn_last': "Last Page",
        'btn_print': "Print",
        'btn_darkmode_light': "Light Mode",
        'btn_darkmode_dark': "Dark Mode",
        'btn_delete_pages': "Delete Pages",
        'btn_extract_pages': "Extract Pages",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Cancel",
        'btn_save': "Save",
        'btn_close': "Close",
        'btn_delete': "Delete",
        'btn_delete_all': "Delete All",
        'btn_copy': "Copy",
        'btn_export': "Export",
        'btn_show': "Show PW",
        'btn_hide': "Hide PW",
        'btn_authenticate': "Authenticate",
        'btn_settings': "Settings",
        'btn_protect': "Protect",
        'btn_remove_password': "Remove Password",
        'btn_manage': "Password Manager",
        'btn_retry': "Retry",
        'btn_select_all': "Select All",
        'btn_clear_selection': "Clear Selection",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Page {0} of {1}",
        'page_count': "of {0}",
        'goto_page': "Go to Page",
        'page_simple': "Page {0}",
        'full_view_page': "Full view Page {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Enter search term + Enter",
        'search_results': "Results: {0} of {1}",
        'search_nav_hint': "Enter: next  (Shift+Enter: previous) result",
        'search_no_results': "No results",
        'search_error': "Search error",
        'search_active': "Search field activated",
        'search_closed': "Search closed",
        'search_position': "Page {0} {1}",
        'search_pos_top': "very top",
        'search_pos_upper': "top",
        'search_pos_middle': "middle",
        'search_pos_lower': "bottom",
        'search_pos_bottom': "very bottom",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Text recognition completed successfully!",
        'ocr_success_title': "OCR successful",
        'ocr_success_message': "The document is now searchable.",
        'ocr_failed': "OCR failed",
        'ocr_in_progress': "OCR in progress",
        'ocr_preparing': "Preparing PDF...",
        'ocr_analyzing': "Analyzing PDF...",
        'ocr_optimizing': "Image optimization in progress...",
        'ocr_recognizing': "Text recognition in progress...",
        'ocr_embedding': "Embedding text...",
        'ocr_finalizing': "Finalizing PDF...",
        'ocr_not_available': "OCR not available",
        'ocr_install_message': "OCR tools were not found.\n\nPlease install:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR required",
        'ocr_question': "The PDF contains no searchable text.\nDo you want to run OCR to enable {0}?",
        'ocr_perform': "Run OCR",
        'ocr_later': "Later",
        'ocr_starting': "Starting guaranteed OCR...",
        'ocr_success_voice': "OCR successful. PDF is now searchable.",
        'ocr_partial_success': "OCR was performed, but there were issues during replacement.\n\nThe searchable version was saved at:\n{0}\n\nError: {1}",
        'ocr_partial_title': "OCR partially successful",
        'ocr_partial_voice': "OCR performed, but replacement failed.",
        'original_file': "Original file:",
        'old_size': "Old file size:    {0} bytes",
        'new_size': "New file size: {0} bytes",
        'size_change': "Change: {0}{1} bytes",
        'backup_created_file': "Backup created:\n{0}",
        'backup_not_created': "Backup: Not created (setting disabled)",
        'page_header': "=== Page {0} ===\n{1}\n",
        'scanned_page_header': "=== Page {0} (scanned) ===\n[This page contains only scanned text]\n[Please run OCR manually]\n",
        'scanned_warning': "⚠️ SCANNED TEXT - OCR REQUIRED",
        'guaranteed_title': "Searchable PDF created",
        'guaranteed_message': "<b>Guaranteed searchable version created!</b>\n\nSince automatic OCR failed, an\nalternative searchable PDF was created:\n\n{0}\n\n<b>This file contains:</b>\n• Extracted text (if available)\n• Hints for scanned pages\n• Is fully searchable",
        'guaranteed_voice': "Guaranteed searchable PDF created.",
        'instruction_title': "OCR INSTRUCTION",
        'instruction_file': "Original file: {0}",
        'instruction_text': "Automatic text recognition (OCR) has failed.\nPlease perform OCR manually:\n\n1. WITH OCRmyPDF (command line):\n   ocrmypdf --force-ocr \"[FILE]\" \"output.pdf\"\n\n2. WITH ADOBE ACROBAT (macOS/Windows):\n   • Open PDF in Acrobat\n   • Tools > Edit PDF\n   • Select 'Recognize Text'\n\n3. WITH PREVIEW (macOS):\n   • Open PDF in Preview\n   • File > Export...\n   • Quartz Filter: 'Reduce File Size'\n   • Enable 'Perform OCR'\n\n4. ONLINE OCR SERVICES:\n   • smallpdf.com/ocr-pdf\n   • ilovepdf.com/ocr-pdf\n   • adobe.com/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR instruction created",
        'instruction_created_message': "A detailed instruction was created:\n\n{0}\n\nPlease follow the steps for manual OCR.",
        'instruction_created_voice': "OCR instruction created.",
        'ocr_impossible': "OCR not possible",
        'ocr_impossible_message': "OCR could not be performed.\n\nPlease process '{0}' manually with OCR software.",
        'ocr_impossible_voice': "OCR not possible. Please process manually.",
        'emergency_title': "Emergency OCR",
        'emergency_message': "An emergency PDF was created:\n\n{0}\n\nPlease process this file manually with OCR.",
        'emergency_voice': "Emergency PDF created. Please run OCR manually.",
        'critical_error': "Critical error",
        'critical_error_message': "OCR could not be started.\n\nPlease restart the program and\ncheck the OCR installation.",
        'critical_error_voice': "Critical OCR error",
        'ocr_question_html': "<p>The PDF contains no searchable text.<p>Do you want to run OCR to enable <b>{0}</b>?</p>",
        'ocr_question_voice': "OCR required. The PDF contains no searchable text. Do you want to run OCR to enable {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "no PDF loaded",
        'no_pdf_message': "No PDF is loaded",
        'pdf_not_found': "PDF file not found",
        'file_size': "File size",
        'bytes': "bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup created",
        'backup_disabled': "Backup disabled",
        'backup_activated': "Backup creation activated",
        'backup_deactivated': "Backup creation deactivated",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ enabled",
        'backup_off': "✘ disabled",
        'close_pdf': "Closing PDF: {0}",
        'pdf_not_found_format': "PDF file not found: {0}",
        'error_pdf_load_format': "Error loading PDF: {0}",
        'load_failed_format': "Loading failed:\n{0}",
        'decrypted_suffix': "(decrypted)",
        'decryption_failed': "Decryption failed.",
        'decryption_error': "Error during decryption",
        'decryption_success': "Successfully decrypted",
        'decryption_success_message': "PDF was decrypted and saved at:\n\n{0}",
        'decryption_success_voice': "PDF was decrypted and saved.",
        'password_remove_error': "Error removing password",
        'save_unencrypted': "Save unencrypted PDF as",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Save as...",
        'save_copy': "Save copy",
        'save_success': "PDF saved at: {0}",
        'save_encrypted': "Protected PDF saved at: {0}",
        'save_error': "Could not save PDF",
        'encryption_question': "Do you want to protect the PDF with a password?",
        'encryption_yes': "Yes",
        'encryption_no': "No",
        'encryption_cancel': "Cancel",
        'save_cancel': "Saving cancelled",
        'save_encrypted_voice': "File encrypted and saved.",
        'save_success_voice': "The PDF file was saved unencrypted.",
        'save_error_format': "Could not save PDF:\n{0}",
        'export_pages_success': "Pages export successful",
        'export_pages_error': "Pages export failed",
        'export_pages_error_format': "Pages export failed: {0}",
        'export_word_success': "Word export successful",
        'export_word_error': "Word export failed",
        'export_word_error_format': "Word export failed: {0}",
        'export_text_success': "Text export successful",
        'export_text_error': "Text export failed",
        'export_text_error_format': "Text export failed: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Password required",
        'password_enter': "Please enter the password",
        'password_confirm': "Confirm password",
        'password_new': "New password",
        'password_current': "Current password",
        'password_save': "Save password (encrypted)",
        'password_saved': "✓ Password for this file is saved",
        'password_wrong': "Wrong password",
        'password_mismatch': "Passwords do not match",
        'password_too_short': "Password too short",
        'password_min_length': "Password must be at least 4 characters long",
        'password_strength': "Password strength",
        'password_strength_very_weak': "Very weak",
        'password_strength_weak': "Weak",
        'password_strength_medium': "Medium",
        'password_strength_strong': "Strong",
        'password_strength_very_strong': "Very strong",
        'password_char_count': "({0} characters)",
        'password_match': "✓ Match",
        'password_no_match': "✗ Passwords do not match",
        'password_show': "Show",
        'password_hide': "Hide",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Password Manager",
        'password_table_filename': "Filename",
        'password_table_password': "Password",
        'password_count': "{0} saved password{1}",
        'password_count_singular': "",
        'password_count_plural': "s",
        'password_none': "No saved passwords",
        'password_copied': "{0} password{1} copied",
        'password_copied_singular': "",
        'password_copied_plural': "s",
        'password_delete_confirm': "Do you really want to delete the password for '{0}'?",
        'password_delete_multiple': "Do you really want to delete the {0} selected passwords?",
        'password_delete_all_confirm': "Do you really want to delete all {0} saved passwords?",
        'password_deleted': "{0} password{1} deleted",
        'password_deleted_singular': "",
        'password_deleted_plural': "s",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "",
        'password_all_deleted': "All passwords deleted",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Password Generator",
        'generator_generated': "Generated password:",
        'generator_regenerate': "Regenerate",
        'generator_copy': "Copy",
        'generator_use': "Use",
        'generator_settings': "Settings",
        'generator_length': "Length:",
        'generator_group_every': "Separator every",
        'generator_group_chars': "characters.   Separator:",
        'generator_uppercase': "Uppercase (A-Z)",
        'generator_lowercase': "Lowercase (a-z)",
        'generator_digits': "Digits (0-9)",
        'generator_symbols': "Symbols (!@#$%^&*)",
        'generator_exclude': "Excluded:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Master password required",
        'master_password_setup': "Set up master password",
        'master_password_change': "Change master password",
        'master_password_enter': "Please enter your master password",
        'master_password_choose': "Choose a strong master password (at least 8 characters)",
        'master_password_new': "Please enter your new master password",
        'master_password_confirm': "Confirm password",
        'master_password_authenticate': "Authenticate",
        'master_password_success': "Master password successfully set up.",
        'master_password_changed': "Master password successfully changed.",
        'master_password_removed': "Master password and all passwords deleted.",
        'master_password_remove': "Remove master password",
        'master_password_remove_confirm': "Are you SURE you want to delete ALL passwords?\n\nThis action is IRREVERSIBLE!",
        'master_password_export_before': "Do you want to export a backup before?",
        'master_password_export_delete': "Export & delete",
        'master_password_delete_now': "Delete now",
        'master_password_for_signatures': "To use signatures, you must set up a master password.\n\nDo you want to set up a master password now?",
        'master_password_for_private': "To use private text templates, you must set up a master password.\n\nDo you want to set up a master password now?",
        'master_password_info': """
            <b>🔐 WITHOUT MASTER PASSWORD:</b><br>
            • No viewing, copying, or exporting of passwords possible<br>
            • Deleting passwords is always possible (even without master password)<br><br>

            <b>🔐 WITH MASTER PASSWORD:</b><br>
            • All functions available after authentication<br>
            • Passwords are encrypted with the master password<br>
            • Minimum length: 8 characters<br>
            • Secure SHA-256 hash storage<br><br>

            <b>IMPORTANT:</b><br>
            • If master password is lost: passwords cannot be recovered<br>
            • When removing master password: ALL passwords are deleted<br>
            • Export option available before deletion<br>
            • Master password can be changed at any time
        """,
        'signature_auth_disabled': "Disable password prompt for signatures",
        'template_auth_disabled': "Disable password prompt for private text templates",
        'master_password_for_signatures_settings': "To use signatures, you must set up a master password.\n\nGo to Settings - Password Manager for that",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Protect PDF",
        'protect_info': "The file '{0}' will be protected with a password.",
        'protect_instruction': "Please enter the desired password twice to protect the document, or use the password generator to the right of the input field.",
        'protect_success': "PDF was successfully protected and saved at:\n{0}\n\nPassword: {1}\n\nDo you want to open the protected PDF now?",
        'protect_open': "Yes",
        'protect_skip': "No",
        'protect_error': "Error protecting PDF",
        'protect_open_title': "open protected PDF",
        'protect_question': "Done. Do you want to open the protected PDF now? Yes or No?",
        'password_cancel': "Password dialog cancelled",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Delete pages",
        'pages_extract': "Extract pages",
        'pages_insert': "Insert pages",
        'pages_move': "Move pages",
        'pages_delete_options': "Delete options",
        'pages_delete_empty': "Delete all empty pages",
        'pages_delete_current': "Delete current page",
        'pages_delete_range': "Delete page range",
        'pages_extract_options': "Extract options",
        'pages_extract_current': "Extract current page",
        'pages_extract_range': "Extract page range",
        'pages_insert_position': "Insert position",
        'pages_insert_before': "Insert before page:",
        'pages_insert_select': "Select PDF",
        'pages_insert_none': "No PDF selected",
        'pages_move_source': "Pages to move",
        'pages_move_from': "From page:",
        'pages_move_to': "To page:",
        'pages_move_target': "Target position",
        'pages_move_before': "Move before page:",
        'pages_move_hint': "Note: page 1 = beginning, {0} = end",
        'pages_range_invalid': "Start page must be less than or equal to end page.",
        'pages_position_invalid': "Target position must not be within the range to be moved.",
        'pages_no_pdf_selected': "No PDF selected.",
        'pages_deleted': "{0} pages were deleted.",
        'pages_extracted': "Extracted: {0}\nSaved at: {1}\nFile size: {2:.1f} KB",
        'pages_inserted': "{0} pages inserted",
        'pages_moved': "{0} pages were moved.",
        'pages_deleted_none': "No pages were deleted.",
        'pages_delete_progress': "Deleting pages...",
        'pages_deleted_with_backup': "{0} pages were deleted.\n\nBackup: {1}",
        'pages_deleted_voice': "A backup was created and {0} pages deleted.",
        'info': "Info",
        'error_dialog_creation': "Could not create dialog",
        'extract_page_single': "Extract page {0}",
        'extract_page_range': "Extract pages {0}-{1}",
        'extract_success_voice': "Pages successfully extracted",
        'extract_error_format': "Error extracting: {0}",
        'pages_inserted_voice': "{0} pages inserted.",
        'insert_error_format': "Error inserting: {0}",
        'pages_move_progress': "Moving pages...",
        'pages_moved_with_backup': "{0} pages were moved.\n\nBackup: {1}",
        'move_success_title': "Successfully moved",
        'pages_moved_voice': "{0} pages successfully moved",
        'mark_removed': "Marking removed from page {0}",
        'mark_empty': "Page {0} marked as empty",
        'mark_export_removed': "Export marking removed from page {0}",
        'mark_export': "Page {0} marked for export",
        'no_empty_pages': "No empty pages marked for deletion",
        'delete_empty_confirm': "Do you want to delete all {0} marked empty pages?",
        'delete_empty_confirm_voice': "Delete all {0} marked empty pages now? Yes or No.",
        'empty_pages_deleted': "{0} empty pages deleted",
        'no_export_pages': "No pages marked for export",
        'overwrite_title': "Overwrite existing file",
        'overwrite_question': "The file\n\n{0}\n\nalready exists.\nDo you want to overwrite it?",
        'overwrite_voice': "Overwrite existing file? Yes or No.",
        'page_skipped': "Page {0} was skipped",
        'export_complete': "Export completed.",
        'export_complete_voice': "The export is completed.",
        'no_pages_exported': "No page exported",
        'export_cancelled': "Export cancelled",
        'pages_exported': "{0} pages exported to {1}",
        'export_page_title': "Export page",
        'page_exported': "Page {0} exported to {1}",
        'export_error': "Error exporting",
        'export_marked_title': "Export marked pages",
        'rotate_all_title': "rotate all pages",
        'rotate_all_question': "Do you want to rotate all pages 90 degrees to the right?",
        'rotate_all_voice': "Do you want to rotate all pages 90 degrees to the right? Yes or No?",
        'all_pages_rotated': "All pages rotated",
        'page_rotated': "Page {0} rotated",
        'rotate_error': "Could not rotate page",
        'delete_page_confirm': "Do you want to delete page {0}?",
        'delete_page_confirm_voice': "Do you really want to delete page {0}? Yes or No.",
        'page_deleted': "Page {0} deleted",
        'delete_error': "Could not delete page",
        'pages_deleted_voice': "{0} pages deleted",
        'pages_exported_split': "{0} pages were successfully exported.",
        'pages_skipped': "{0} pages were skipped.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Extract pages (advanced)",
        'pdf_splitter_title': "PDF Splitter & Extractor",
        'pdf_splitter_load': " Select PDF file",
        'pdf_splitter_info': "Please choose an option for your PDF document",
        'pdf_splitter_basic': "Basic operations",
        'pdf_splitter_single': "Split into single pages",
        'pdf_splitter_range': "Extract pages:",
        'pdf_splitter_range_placeholder': "e.g. 1-3,5,7-9",
        'pdf_splitter_clean': "Cleaning operations",
        'pdf_splitter_remove_empty': "Remove all empty pages",
        'pdf_splitter_remove': "Delete page range:",
        'pdf_splitter_remove_placeholder': "e.g. 2,4-6",
        'pdf_splitter_process': "Process PDF",
        'pdf_splitter_loaded': "PDF loaded. Please choose an option",
        'pdf_read_error': "Could not read PDF",
        'pages': "Pages",
        'pages_created': "Pages were created",
        'range_empty': "Please enter a page range",
        'range_invalid': "Invalid page range",
        'range_created': "New PDF with the selected pages was created:\n{0}",
        'empty_removed': "{0} empty pages removed.\nOutput: {1}",
        'remove_empty': "Please enter pages to remove",
        'remove_invalid': "Invalid pages to remove",
        'remove_done': "Cleaned PDF created:\n{0}",
        'open_folder': "Open folder",
        'show_in_finder': "Show in Finder",
        'pdf_splitter_no_pdf': "Please load a PDF file first.",
        'process_error': "Error processing PDF",
        'pages_created_voice': "{0} pages were created",
        'range_created_voice': "PDF with the selected pages was created",
        'empty_removed_voice': "{0} empty pages were removed",
        'remove_done_voice': "Cleaned PDF was created",
        'pdf_splitter_split_groups': "Each contiguous group into separate file",
        'range_created_single': "New PDF created:\n{0}",
        'range_created_multiple': "{0} PDF files were created.",
        'range_created_voice_single': "One PDF with the selected pages was created",
        'range_created_voice_multiple': "{0} PDF files were created",
        'empty_removed_none_left': "No pages left",
        'empty_removed_all_empty': "All pages were recognized as empty and would be removed. No file was created.",
        'preview_single': "Preview: {0}",
        'preview_enter_range': "Please enter a page range.",
        'preview_invalid_range': "Invalid page range.",
        'preview_file': "Preview: {0}",
        'preview_files': "Preview: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Starting print process",
        'print_sent': "Print job sent",
        'print_now': "Print now",
        'print_error': "Error during direct print",
        'print_limited': "Print function limited on this system",
        'print_error_format': "Error during direct print: {0}",
        'warning': "Notice",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Switch to Light Mode",
        'mode_switch_to_dark': "Switch to Dark Mode",
        'mode_dark_activated': "Dark Mode activated",
        'mode_light_activated': "Light Mode activated",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Full view",
        'zoom_two_pages': "Two pages side by side",
        'zoom_overview': "Overview mode",
        'zoom_cannot_during_search': "Zoom not possible during search",
        'zoom_exit_first': "Please exit zoom first",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop enabled",
        'drag_disabled': "Drag & Drop disabled",
        'drag_page_grab': "Grabbing page {0}",
        'drag_page_dropped': "Page {0} inserted at position {1}",
        'drag_position_invalid': "Invalid position",
        'drag_same_position': "Page {0} remains at position {0}",
        'drag_error': "Error moving",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Text input and template management",
        'text_templates': "Available text templates:",
        'text_name': "Name",
        'text_preview': "Text preview",
        'text_enter': "Text:",
        'text_font_size': "Font size:",
        'text_formatting': "Formatting:",
        'text_bold': "Bold",
        'text_italic': "Italic",
        'text_underline': "Underline",
        'text_alignment': "Alignment:",
        'text_left': "Left",
        'text_center': "Center",
        'text_right': "Right",
        'text_color': "Text color:",
        'text_opacity': "Opacity:",
        'text_word_wrap': "Word wrap:",
        'text_auto': "Automatic",
        'text_page_width_95': "Page width (95%)",
        'text_page_width_85': "Very wide (85%)",
        'text_page_width_75': "Wider (75%)",
        'text_page_width_60': "Wide (60%)",
        'text_page_width_50': "Medium (50%)",
        'text_page_width_30': "Narrow (30%)",
        'text_page_width_20': "Narrower (20%)",
        'text_page_width_10': "Very narrow (10%)",
        'text_no_wrap': "No wrap",
        'text_private': "Private text template (requires authentication)",
        'text_preview_label': "Preview:",
        'text_preview_placeholder': "A preview of the text will be shown here...",
        'text_no_text': "(No text)",
        'text_save_template': "💾 Save as template",
        'text_delete_template': "🗑 Delete selected text template",
        'text_show_private': "Show private",
        'text_hide_private': "Hide private",
        'text_use': "✅ Use text",
        'text_saved': "Text template saved as:\n{0}",
        'text_saved_voice': "Text template saved",
        'text_deleted': "Text template deleted",
        'text_no_text_to_save': "No text to save.",
        'text_no_templates': "No text templates found",
        'text_private_master_required': "Private templates can only be used if a master password is set up.\n\nDo you want to set up a master password now?",
        'text_filename': "Filename for text template (without 'Text_' and '.txt'):",
        'text_filename_hint': "Example: 'Phone HomeOffice' will be saved as 'Text_Phone HomeOffice.txt'",
        'text_save_hint': "The text template will automatically be saved with formatting.",
        'text_guide_title': "Text input - Guide",
        'text_delete_confirm': "Do you really want to delete the text template?\n\nFile: {0}\nText: {1}...",
        'text_make_public': "Mark as public",
        'text_make_private': "Mark as private",
        'text_privacy_changed': "Privacy status changed",
        'text_private_always': "Private always visible (setting)",
        'text_mode_required': "Please activate text mode first",
        'text_continue_editing': "Continue editing - cursor at end of text",
        'text_no_input': "No text entered - text discarded",
        'save_dialog_question': "How do you want to proceed?",
        'text_save_question': "Save all texts and crosses, adjust, continue editing, or discard?",
        'copy_cross': "Cross copied",
        'paste_cross': "Cross pasted",
        'paste_text': "Text pasted",
        'cross_discarded': "Cross discarded",
        'all_discarded': "Everything discarded",
        'text_discarded': "Text discarded",
        'no_texts_to_save': "No texts to save",
        'no_valid_texts': "No valid texts to save",
        'text_word_singular': "text",
        'text_word_plural': "texts",
        'cross_word_singular': "cross",
        'cross_word_plural': "crosses",
        'texts_saved_title': "Texts saved",
        'texts_crosses_saved': "{0} {1} and {2} {3} were inserted into the PDF.\n\nPDF was reloaded...",
        'texts_crosses_saved_voice': "{0} {1} and {2} {3} saved.",
        'texts_saved': "{0} {1} were inserted into the PDF.\n\nPDF was reloaded...",
        'texts_saved_voice': "{0} {1} saved.",
        'crosses_saved': "{0} {1} were inserted into the PDF.\n\nPDF was reloaded...",
        'crosses_saved_voice': "{0} {1} saved.",
        'elements_saved': "{0} elements were inserted into the PDF.\n\nPDF was reloaded...",
        'elements_saved_voice': "{0} elements saved.",
        'text_window_load_error': "Could not load text window",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Text Input and Text Templates – Detailed Guide**

        **1. Inserting and editing text**
        - Right-click at the desired position in the document and select "Insert text".
        - A dialog opens where you can enter and format your text:
        • Font size, Bold, Italic, Underline
        • Text color (freely selectable)
        • Transparency (opacity) via slider
        • Word wrap (various widths, e.g. page width, narrow, no wrap)
        - After confirmation, the text appears at the click position. You can move it with the mouse or arrow keys.
        - Double-click on the text opens edit mode; ESC exits it.

        **2. Managing text templates**
        - In the text dialog, you see a list of all saved text templates on the left.
        - **Saving a template:** Enter your text, format it, and click "💾 Save as template". Enter a filename (without extension).
        - **Loading a template:** Click on the desired name in the list. The text and formatting are adopted and can be adjusted if needed.
        - **Deleting:** Right-click on a template to delete it or change its privacy status.

        **3. Private text templates (Master password)**
        - If you have set up a master password (under Settings → Password Manager), you can mark templates as "private".
        - Activate the checkbox "Private text template" in the dialog before saving.
        - Private templates are only shown in the list if you have entered your master password once per session (authentication via the lock symbol or on first access).
        - This way you can protect confidential text templates from unauthorized access.

        **4. Inserting crosses**
        - Via the context menu you can also insert a graphical cross (e.g. for checkboxes).
        - The size, line width and color of crosses can be adjusted globally in the settings (menu "Settings" → "Cross settings").
        - Right-click on an existing cross to change it individually.

        **5. Batch actions**
        - If you have placed several texts or crosses on a page, you can save or discard all elements together via the context menu (right-click in text mode).
        - When saving, all elements are embedded into the PDF and remain as vector graphics.

        **6. Keyboard shortcuts in text mode**
        - Arrow keys: move element
        - Ctrl+Arrow keys: larger steps
        - Enter: open save dialog (save all / adjust / discard)
        - ESC: discard current element
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Text Input and Text Templates – Detailed Guide</strong></p>

        <p><strong>1. Inserting and editing text</strong></p>
        <ul>
        <li>Right-click at the desired position in the document and select "Insert text".</li>
        <li>A dialog opens where you can enter and format your text:<br/>
        • Font size, Bold, Italic, Underline<br/>
        • Text color (freely selectable)<br/>
        • Transparency (opacity) via slider<br/>
        • Word wrap (various widths, e.g. page width, narrow, no wrap)</li>
        <li>After confirmation, the text appears at the click position. You can move it with the mouse or arrow keys.</li>
        <li>Double-click on the text opens edit mode; ESC exits it.</li>
        </ul>

        <p><strong>2. Managing text templates</strong></p>
        <ul>
        <li>In the text dialog, you see a list of all saved text templates on the left.</li>
        <li><strong>Saving a template:</strong> Enter your text, format it, and click "💾 Save as template". Enter a filename (without extension).</li>
        <li><strong>Loading a template:</strong> Click on the desired name in the list. The text and formatting are adopted and can be adjusted if needed.</li>
        <li><strong>Deleting:</strong> Right-click on a template to delete it or change its privacy status.</li>
        </ul>

        <p><strong>3. Private text templates (Master password)</strong></p>
        <ul>
        <li>If you have set up a master password (under Settings → Password Manager), you can mark templates as "private".</li>
        <li>Activate the checkbox "Private text template" in the dialog before saving.</li>
        <li>Private templates are only shown in the list if you have entered your master password once per session (authentication via the lock symbol or on first access).</li>
        <li>This way you can protect confidential text templates from unauthorized access.</li>
        </ul>

        <p><strong>4. Inserting crosses</strong></p>
        <ul>
        <li>Via the context menu you can also insert a graphical cross (e.g. for checkboxes).</li>
        <li>The size, line width and color of crosses can be adjusted globally in the settings (menu "Settings" → "Cross settings").</li>
        <li>Right-click on an existing cross to change it individually.</li>
        </ul>

        <p><strong>5. Batch actions</strong></p>
        <ul>
        <li>If you have placed several texts or crosses on a page, you can save or discard all elements together via the context menu (right-click in text mode).</li>
        <li>When saving, all elements are embedded into the PDF and remain as vector graphics.</li>
        </ul>

        <p><strong>6. Keyboard shortcuts in text mode</strong></p>
        <ul>
        <li>Arrow keys: move element</li>
        <li>Ctrl+Arrow keys: larger steps</li>
        <li>Enter: open save dialog (save all / adjust / discard)</li>
        <li>ESC: discard current element</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Cross Settings",
        'cross_properties': "Cross Properties",
        'cross_size': "Size (px):",
        'cross_line_width': "Line width:",
        'cross_color': "Color:",
        'cross_choose_color': "Choose",
        'cross_fine_tuning': "Fine adjustment when saving (pixels)",
        'cross_offset_x': "X offset:",
        'cross_offset_y': "Y offset:",
        'cross_offset_x_tooltip': "Negative values move the cross left when saving, positive values move it right",
        'cross_offset_y_tooltip': "Negative values move the cross up when saving, positive values move it down",
        'cross_preview': "Preview",
        'cross_save': "Apply settings",
        'cross_customized': "Cross customized",
        'cross_settings_applied': "Cross settings saved.\nSize: {0}px, Line width: {1}px\n{2}",
        'cross_updated_count': "{0} existing crosses were updated.",
        'cross_no_crosses': "No existing crosses found.",
        'cross_settings_applied_all': "Cross settings applied to all {0} crosses",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Signature Settings",
        'signature_1': "Signature 1",
        'signature_2': "Signature 2",
        'signature_select': "Select signature",
        'signature_add': "➕ Add new signature...",
        'signature_size': "Size for signature {0} (%):",
        'signature_common': "General settings",
        'signature_timestamp': "Add timestamp automatically",
        'signature_location': "Default location:",
        'signature_timestamp_size': "Timestamp font size:",
        'signature_no_files': "-- No signatures found --",
        'signature_insert': "Insert signature",
        'signature_insert_1': "Insert signature 1",
        'signature_insert_2': "Insert signature 2",
        'signature_customize': " Customize signature",
        'signature_discard': " Discard this signature",
        'signature_save_all': " Save all signatures",
        'signature_discard_all': " Discard all signatures",
        'signature_guide_title': "Signatures - Guide",
        'signature_guide': """
📝 Signatures - Quick guide

- Set up master password
- Configure signatures in the Settings menu
  (size, timestamp ...)
- Insert with RIGHT-CLICK at desired position
  (master password required once per session)
- Move signature with mouse or arrow keys
- Multiple signatures can be inserted one after another
- Each signature can be customized individually
- Discard single signature
- Save / discard all signatures at once
- Alternatively, the menu bar can be used.
        """,
        'signature_placeholder': "No preview available",
        'signature_info': "Signature {0}: {1}×{2} px ({3}% of {4}×{5})",
        'signature_info_placeholder': "Settings for signature {0}",
        'signature_inserted': "Signature {0} inserted on page {1}",
        'signature_deleted': "Signature deleted",
        'signature_copied': "Signature copied",
        'signature_pasted': "Signature {0} pasted",
        'signature_saved': "{0} signatures were inserted into the PDF.\n\nPDF was reloaded...",
        'signature_saved_voice': "{0} signatures saved",
        'mode_replace_signature_format': "Exit mode and insert signature {0}",
        'mode_conflict_voice_signature': "{0} mode is active. Exit and insert signature?",
        'signature_not_configured': "Signature {0} not configured",
        'signature_file_not_found': "Signature file not found",
        'timestamp_format': "{0}, {1}",
        'no_copied_signature': "No copied signature available",
        'no_signatures_to_save': "No signatures to save",
        'signature_save_question': "Save all signatures, adjust, or discard this one?",
        'signatures_saved_title': "Signatures saved",
        'signatures_saved': "{0} signatures were inserted into the PDF.\n\nPDF was reloaded...",
        'signatures_saved_voice': "{0} signatures saved.",
        'all_signatures_discarded': "All signatures discarded",
        'signature_settings_saved': "Signature settings saved",
        'signature_cancelled': "Signature discarded",
        'signature_active_title': "Signature active",
        'signature_replace_question': "A signature is already active.\n\nDo you want to replace the current signature?",
        'signature_replace': "Replace signature",
        'signature_replace_voice': "Replace current signature or cancel?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Image settings",
        'image_common': "General image settings",
        'image_keep_aspect': "Keep aspect ratio when dragging",
        'image_default_size': "Default size (%):",
        'image_dark_invert': "Invert images in Dark Mode",
        'image_dark_invert_tooltip': "Enabled: images are inverted for better visibility",
        'image_fine_tuning': "Fine adjustment (pixels)",
        'image_offset_x': "X offset:",
        'image_offset_y': "Y offset:",
        'image_offset_x_tooltip': "Negative values move the image left when saving, positive values move it right",
        'image_offset_y_tooltip': "Negative values move the image up when saving, positive values move it down",
        'image_select': "Select image",
        'image_insert': "Insert image",
        'image_customize': " Customize image",
        'image_aspect': " Keep aspect ratio",
        'image_discard': " Discard this image",
        'image_save_all': " Save all images",
        'image_discard_all': " Discard all images",
        'image_filter': "Images",
        'image_guide_title': "Insert images - Guide",
        'image_guide': """
📷 Insert images into PDF - Quick guide:

1. Right-click at the desired position
2. "Insert image" → select image
3. Position image: drag with mouse
4. Adjust size: drag at corners/edges
5. Keep aspect ratio: [A] key
6. Further adjustments: right-click on image

Tip: You can adjust settings in the context menu.
        """,
        'image_inserted': "Image {0} inserted on page {1}",
        'image_deleted': "Image discarded",
        'image_copied': "Image copied",
        'image_pasted': "Image pasted",
        'image_saved': "{0} images were inserted into the PDF.\n\nPDF was reloaded...",
        'image_saved_voice': "{0} images saved",
        'image_aspect_on': "enabled",
        'image_aspect_off': "disabled",
        'image_aspect_toggle': "Keep aspect ratio {0}",
        'image_reset': "Image reset to original size",
        'image_replaced': "Image replaced",
        'image_invalid': "Not a valid image",
        'mode_replace_image': "Insert image",
        'mode_conflict_voice_image': "{0} mode is active. Exit and insert image?",
        'image_active_title': "Image active",
        'image_replace_question': "An image is already active.\n\nDo you want to replace the current image?",
        'image_replace': "Replace image",
        'image_replace_voice': "Replace current image or cancel?",
        'image_filter_all': "Images (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;All files (*.*)",
        'no_copied_image': "No copied image available",
        'image_discarded': "Image discarded",
        'image_save_question': "Save all images, adjust, or discard this one?",
        'no_images_to_save': "No images to save",
        'no_valid_images': "No valid images to save",
        'images_saved_title': "Images saved",
        'images_saved': "{0} images were inserted into the PDF.\n\nPDF was reloaded...",
        'images_saved_voice': "{0} images saved.",
        'all_images_discarded': "All images discarded",
        'image_settings_updated': "Image settings updated",
        'image_replace_title': "Select new image",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Shape settings",
        'form_basic': "Basic settings",
        'form_default_type': "Default shape type:",
        'form_rectangle': "Rectangle",
        'form_ellipse': "Ellipse",
        'form_line': "Line",
        'form_arrow': "Arrow",
        'form_line_width': "Line width:",
        'form_colors': "Colors",
        'form_line_color': "Line color:",
        'form_fill_color': "Fill color:",
        'form_choose_color': "Choose",
        'form_transparent': "Transparent background (line only)",
        'form_filled': "filled",
        'form_dark_mode': "Dark Mode",
        'form_dark_invert': "Invert colors in Dark Mode",
        'form_fine_tuning': "Fine adjustment (pixels)",
        'form_offset_x': "X offset:",
        'form_offset_y': "Y offset:",
        'form_offset_x_tooltip': "Negative values move the shape left when saving, positive values move it right",
        'form_offset_y_tooltip': "Negative values move the shape up when saving, positive values move it down",
        'form_preview': "Preview",
        'form_insert': "Insert shape",
        'form_rectangle_insert': "Rectangle",
        'form_ellipse_insert': "Ellipse/Circle",
        'form_line_insert': "Line (2 clicks)",
        'form_arrow_insert': "Arrow (2 clicks)",
        'form_customize': " Customize shape",
        'form_transparent_toggle': " Transparent background",
        'form_discard': " Discard this shape",
        'form_save_all': " Save all shapes",
        'form_discard_all': " Discard all shapes",
        'form_guide_title': "Insert shapes - Guide",
        'form_guide': """
📐 Insert shapes into PDF - Quick guide:

1. Select shape type (rectangle, ellipse, line, arrow)
2. Click on position
   - For rectangle/ellipse: One click places the shape
   - For line/arrow: Two clicks for start and end point
3. Position shape: drag with mouse
4. Adjust size: drag at corners/edges
5. Save shape: Enter
6. Discard shape: ESC
7. Further adjustments: right-click on shape

Tip: You can adjust settings in the context menu.
        """,
        'form_inserted': "{0} inserted on page {1}",
        'form_deleted': "Shape deleted",
        'form_copied': "Shape copied",
        'form_pasted': "Shape pasted",
        'form_saved': "{0} shapes were inserted into the PDF.\n\nPDF was reloaded...",
        'form_saved_voice': "{0} shapes saved",
        'form_reset': "Shape reset to default size",
        'form_transparent_on': "enabled",
        'form_transparent_off': "disabled",
        'form_transparent_toggled': "Transparent background {0}",
        'form_line_cancel': "Line drawing cancelled",
        'form_second_click': "Now click end point for {0}",
        'mode_replace_form': "Insert shape",
        'mode_conflict_voice_form': "{0} mode is active. Exit and insert a shape?",
        'form_settings_updated': "Shape settings updated",
        'form_unknown': "Shape",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Click on the start position",
        'form_line_guide_2': "2. Click on the end position",
        'form_line_guide_3': "The line will be drawn between both points.",
        'form_line_status_1': "Waiting for first click...",
        'form_line_status_2': "First point set: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Now click end point...",
        'form_line_status_4': "Both points set.\nClick 'Finish' to save.",
        'form_line_reset': "Reset",
        'form_line_finish': "Finish",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Copy (Cmd+C)",
        'paste': "Paste (Cmd+V)",
        'copied': "Copied: {0}",
        'no_element_to_copy': "No element selected to copy",
        'no_copied_data': "No copied data available",
        'no_valid_position': "No valid position to paste",
        'copy_text': "Text copied",
        'copy_image': "Image copied",
        'copy_form': "Shape copied",
        'copy_signature': "Signature copied",
        'element_text': "text",
        'element_image': "image",
        'element_form': "shape",
        'element_signature': "signature",
        'element_unknown': "element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Mode conflict",
        'mode_conflict_message': "The mode '{0}' is already active.\n\nDo you want to exit it and {1}?",
        'mode_replace': "Exit mode and {0}",
        'mode_cancel': "Cancel",
        'mode_replace_text': "insert text",
        'mode_replace_cross': "insert cross",
        'mode_replace_signature': "insert signature",
        'mode_replace_image': "insert image",
        'mode_replace_form': "insert shape",
        'mode_conflict_voice': "{0} mode is active. Exit and insert text?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Text input",
        'active_mode_signature': "Signature",
        'active_mode_image': "Image",
        'active_mode_form': "Shape",
        'active_mode_and': " and ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Insert",                    # Hauptmenü
        'insert_another_text': "Insert text",          # Vereinfacht
        'insert_another_cross': "Insert cross",        # Vereinfacht
        'insert_another_signature_1': "Signature 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Signature 2",      # Untermenü-Eintrag
        'insert_another_image': "Insert image",         # Vereinfacht
        'insert_another_form_rect': "Rectangle",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Ellipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Line (2 clicks)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Arrow (2 clicks)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Save {0}",
        'save_dialog_message': "{0} will be saved on page {1}.\n\nHow do you want to proceed?",
        'save_all': "Save all {0}",
        'save_single': "Save {0}",
        'save_customize': "Customize {0}",
        'save_discard': "Discard this {0}",
        'save_continue': "Continue editing",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Go to page {0}",
        'context_rotate': " Rotate page {0}",
        'context_delete': " Delete page {0}",
        'context_export': " Export page {0}",
        'context_mark_as': " Mark page as...",
        'context_mark_empty': " Empty page",
        'context_unmark_empty': " Not empty anymore",
        'context_mark_export': " Mark for export",
        'context_unmark_export': " No longer export",
        'context_batch_actions': " Batch actions",
        'context_batch_delete_empty': " Delete all {0} empty pages",
        'context_batch_export_single': " All {0} pages (one file)",
        'context_batch_export_split': " All {0} pages (separate)",
        'context_drag_start': " Start Drag & Drop",
        'context_drag_stop': " End Drag & Drop",
        'context_insert': " Insert",
        'context_insert_pages': " Insert pages",
        'context_zoom': "Zoom",
        'discard_mixed': "Discard all {0} {1} and {2} {3}",
        'save_mixed': "Save {0} {1} and {2} {3}",
        'discard_texts': "Discard all {0} texts",
        'discard_text_single': "Discard 1 text",
        'save_texts': "Save {0} texts",
        'save_text_single': "Save 1 text",
        'discard_crosses': "Discard all {0} crosses",
        'discard_cross_single': "Discard 1 cross",
        'save_crosses': "Save {0} crosses",
        'save_cross_single': "Save 1 cross",
        'discard_signatures': "Discard all {0} signatures",
        'save_signature_single': "Save 1 signature",
        'save_signatures': "Save {0} signatures",
        'discard_images': "Discard all {0} images",
        'save_image_single': "Save 1 image",
        'save_images': "Save {0} images",
        'discard_forms': "Discard all {0} shapes",
        'save_form_single': "Save 1 shape",
        'save_forms': "Save {0} shapes",
        'cross_discard': "Discard this cross",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Export / Import Information",
        'export_what': "📋 What is exported?",
        'export_general': "General settings",
        'export_general_items': "• Voice output (on/off, speed)\n• Dark/Light Mode\n• Backup settings\n• OCR settings",
        'export_image_form': "Image and shape settings",
        'export_image_form_items': "• Image settings (aspect ratio, default size)\n• Shape settings (line width, colors)\n• Signature settings (paths, sizes, timestamp)",
        'export_passwords': "Password database",
        'export_passwords_items': "• All saved PDF passwords\n• Optionally encrypted or decrypted",
        'export_master': "Master password settings",
        'export_master_items': "• Master password hash\n• Settings for signatures/text templates",
        'export_signatures': "Signatures and text templates",
        'export_signatures_items': "• All image files (signatures)\n• All text templates with formatting\n• Private/public markings",
        'export_import_warning': "⚠️ Important notes",
        'export_import_note': "• During import, ALL current settings are overwritten\n• A restart of the application is required\n• Existing signatures/text templates will be replaced",
        'export_master_note': "• If a master password is set, you can choose:\n  - Decrypted (passwords in plain text)\n  - Encrypted (only readable with master password)",
        'export_security': "• The exported ZIP file contains confidential data\n• Please store it securely (e.g. encrypted USB stick)\n• If the file is lost, passwords are irretrievably lost",
        'export_format': "📁 Export format",
        'export_format_desc': "The settings are saved in a single ZIP file:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Settings successfully exported",
        'export_failed': "Export failed",
        'export_import_question': "Do you want to restart the application now?",
        'export_password_question': "A master password is set.\n\nDo you want to export the passwords decrypted?\n(otherwise they will be exported encrypted)",
        'export_decrypt': "Export decrypted",
        'export_encrypt': "Export encrypted",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "About PDF Dark View",
        'info_version': "Version",
        'info_author': "Developed by Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "About",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> is an accessible PDF viewer, specially developed for people with visual impairments.</p>

            <p><strong>Key Features:</strong></p>
            <ul>
                <li>High-contrast, customizable interface</li>
                <li>Full keyboard control</li>
                <li>Integrated text-to-speech</li>
                <li>OCR for scanned documents</li>
                <li>Comprehensive editing tools</li>
            </ul>

            <p>More than 50 languages are supported – making PDFs accessible to everyone.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Features",
        'info_features_intro': "PDF Dark View offers you the following possibilities:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>View & Navigation</strong> – Dark/Light mode, page browsing, zoom, jump to page</li>
            <li><strong>OCR (Text Recognition)</strong> – Make scanned documents searchable and copyable</li>
            <li><strong>Editing</strong> – Insert text, crosses, signatures, images, and shapes</li>
            <li><strong>Page Management</strong> – Delete, extract, insert, move via drag & drop</li>
            <li><strong>Export</strong> – To Word, Pages, or as text</li>
            <li><strong>Security</strong> – Password protection and management</li>
            <li><strong>Accessibility</strong> – Text-to-speech, keyboard control, high contrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Operation",
        'info_accessibility': "♿ Accessibility – full keyboard control",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 General</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Open PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Search</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Toggle Dark/Light Mode</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Print</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Quit</div>

        <div class="shortcut-cat">📖 Navigation</div>
        <div class="shortcut-row"><kbd>Arrow keys</kbd> Browse page by page</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Go to page</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> First page</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Last page</div>

        <div class="shortcut-cat">✏️ Editing</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Insert text</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Delete pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Extract pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Insert pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Move pages</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Rotate page</div>

        <div class="shortcut-cat">🖼️ Move elements</div>
        <div class="shortcut-row"><kbd>Arrow keys</kbd> Move text/image/signature</div>
        <div class="shortcut-row"><kbd>Ctrl+Arrow keys</kbd> Larger steps</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Save</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Discard</div>

        <div class="shortcut-cat">🗣️ Text-to-Speech</div>
        <div class="shortcut-row"><kbd>F2</kbd> Toggle text-to-speech on/off</div>
        """,
        'info_contextmenu': "📌 Important: All functions are also accessible via the context menu (right mouse button)!",
        'info_accessibility_hint': "💡 Tip: Text-to-speech (F2) facilitates orientation and provides feedback on menus and dialogs.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "License & Imprint",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRINT</strong><br>
        Information according to § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        E-Mail: binhdiez64@gmail.com<br>
        Responsible for the content: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Disclaimer</strong><br>
        The software was developed with the utmost care. No warranty is given for accuracy, completeness, and functionality. Use is at your own risk.<br><br>

        <strong>📄 MIT License (private use)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Permitted: free use, private modifications, personal copies.<br>
        Not permitted: sale, commercial use, removal of copyright notices.<br><br>

        <strong>🔧 Third-party components</strong><br>
        This software contains components under GPL, AGPL, Apache 2.0, BSD, and MIT licenses.<br>
        When redistributing, the respective license terms must be complied with.<br><br>

        <strong>🌐 Open Source</strong><br>
        The source code is available and can be viewed, modified, and redistributed according to the respective license terms.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Credits",
        'info_credits': "Thanks to the open-source community",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF processing</li>
            <li><strong>PyQt5</strong> – Graphical user interface</li>
            <li><strong>Tesseract OCR</strong> – Text recognition</li>
            <li><strong>OCRmyPDF</strong> – OCR integration</li>
            <li><strong>python-docx</strong> – Word export</li>
            <li><strong>qtawesome</strong> – Icons</li>
            <li><strong>DeepSeek</strong> – Support for translations (50+ languages)</li>
            <li><strong>All users</strong> – For valuable feedback</li>
            <li><strong>The open-source community</strong> – For great libraries</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Languages",
        'info_languages_header': "🌍 Language Support",
        'info_languages_html': r"""
        <div style="line-height:1.6;">
            <p>PDF Dark View currently supports <strong>62 languages</strong> – ensuring the software can be used accessibly worldwide.</p>

            <p><strong>📖 Complete language list (as of March 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanian (Shqip)</li>
                    <li>🇩🇿 Arabic (العربية)</li>
                    <li>🇮🇩 Balinese (Basa Bali)</li>
                    <li>🇧🇩 Bengali (বাংলা)</li>
                    <li>🇲🇲 Burmese (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnian (Bosanski)</li>
                    <li>🇧🇬 Bulgarian (Български)</li>
                    <li>🇨🇳 Chinese (中文)</li>
                    <li>🇩🇰 Danish (Dansk)</li>
                    <li>🇩🇪 German (Deutsch)</li>
                    <li>🇬🇧 English (English)</li>
                    <li>🇪🇪 Estonian (Eesti)</li>
                    <li>🇫🇮 Finnish (Suomi)</li>
                    <li>🇫🇷 French (Français)</li>
                    <li>🇬🇷 Greek (Ελληνικά)</li>
                    <li>🇮🇱 Hebrew (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Croatian (Hrvatski)</li>
                    <li>🇭🇺 Hungarian (Magyar)</li>
                    <li>🇮🇩 Indonesian (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irish (Gaeilge)</li>
                    <li>🇮🇸 Icelandic (Íslenska)</li>
                    <li>🇮🇹 Italian (Italiano)</li>
                    <li>🇯🇵 Japanese (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Korean (한국어)</li>
                    <li>🇱🇦 Lao (ພາສາລາວ)</li>
                    <li>🇱🇻 Latvian (Latviešu)</li>
                    <li>🇱🇹 Lithuanian (Lietuvių)</li>
                    <li>🇱🇺 Luxembourgish (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malay (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolian (Монгол)</li>
                    <li>🇳🇵 Nepali (नेपाली)</li>
                    <li>🇳🇱 Dutch (Nederlands)</li>
                    <li>🇳🇴 Norwegian (Norsk)</li>
                    <li>🇦🇫 Pashto (پښتو)</li>
                    <li>🇮🇷 Persian (فارسی)</li>
                    <li>🇵🇱 Polish (Polski)</li>
                    <li>🇵🇹 Portuguese (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Romanian (Română)</li>
                    <li>🇷🇺 Russian (Русский)</li>
                    <li>🇸🇪 Swedish (Svenska)</li>
                    <li>🇷🇸 Serbian (Српски)</li>
                    <li>🇸🇰 Slovak (Slovenčina)</li>
                    <li>🇸🇮 Slovenian (Slovenščina)</li>
                    <li>🇪🇸 Spanish (Español)</li>
                    <li>🇹🇿 Swahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thai (ไทย)</li>
                    <li>🇨🇿 Czech (Čeština)</li>
                    <li>🇹🇷 Turkish (Türkçe)</li>
                    <li>🇺🇦 Ukrainian (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamese (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Yiddish (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Add your own languages:</strong><br>
                Want a language that is not yet included? Simply place your own dictionary file (<code>sprache_xx.py</code>) next to the application – the software will recognize it automatically. If you are interested in a specific translation, feel free to contact me.
            </div>

            <p><strong>🙏 Special thanks:</strong> DeepSeek for supporting the translation of all dictionaries into 62 languages.</p>

            <p>📧 Contact for translations: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Error",
        'error_occurred': "An error occurred",
        'error_pdf_load': "Error loading PDF",
        'error_pdf_save': "Error saving PDF",
        'error_ocr': "Error during text recognition",
        'error_no_pdf': "No PDF loaded",
        'error_page_not_found': "Page not found",
        'error_invalid_range': "Invalid page range",
        'error_file_not_found': "File not found",
        'error_permission': "No permission",
        'error_unknown': "Unknown error",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Success",
        'success_operation': "Operation completed successfully",
        'success_saved': "Successfully saved",
        'success_exported': "Successfully exported",
        'success_imported': "Successfully imported",
        'success_deleted': "Successfully deleted",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Confirmation",
        'confirm_yes': "Yes",
        'confirm_no': "No",
        'confirm_ok': "OK",
        'confirm_cancel': "Cancel",
        'confirm_delete': "Delete",
        'confirm_overwrite': "Overwrite",
        'confirm_continue': "Continue",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Loading PDF...",
        'progress_saving': "Saving PDF...",
        'progress_exporting': "Exporting PDF...",
        'progress_processing': "Processing...",
        'progress_wait': "Please wait...",
        'progress_preparing': "Preparing...",
        'progress_finalizing': "Finalizing...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "White",
        'color_black': "Black",
        'color_red': "Red",
        'color_green': "Green",
        'color_blue': "Blue",
        'color_yellow': "Yellow",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Orange",
        'color_gray': "Gray",
        'color_custom': "Color chooser",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&File",
        'menu_edit': "&Edit",
        'menu_view': "&View",
        'menu_tools': "&Tools",
        'menu_settings': "&Settings",
        'menu_help': "&Help",
        'menu_language': "Language",
        'menu_guides': "&Guides",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Open",
        'file_save_as': "&Save as...",
        'file_protect': "&Protect document...",
        'file_export': "&Export",
        'file_export_pages': "Export as Pages",
        'file_export_word': "Export as DOCX",
        'file_export_text': "Export as TXT",
        'file_print_now': "&Print now",
        'file_print': "&Print",
        'file_close': "&Close",
        'file_quit': "&Quit",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Search",
        'edit_ocr': " Run OCR",
        'edit_rotate': "&Rotate page",
        'edit_rotate_all': "&Rotate all pages",
        'edit_delete_pages': "&Delete pages",
        'edit_extract_pages': "&Extract pages",
        'edit_insert_pages': "&Insert pages",
        'edit_move_pages': "&Move pages",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Insert text and crosses",
        'text_insert': " Insert text",
        'cross_insert': " Insert cross",
        'text_customize': " Customize text",
        'cross_customize': " Customize this cross",
        'cross_customize_all': " Customize all crosses",
        'text_discard': " Discard this text/cross",
        'text_discard_all': " Discard all texts and crosses",
        'text_save_all': " Save all texts and crosses",
        'text_guide': " Text input / text templates - Guide",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Insert signature",
        'signature_settings_menu': " Settings...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Insert image",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Insert shapes",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Show text window",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Page width (default)",
        'view_zoom_two': "&Two pages",
        'view_zoom_overview': "&Overview (multiple pages)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Accessibility",
        'settings_voice': "Voice output",
        'settings_voice_tooltip': "supplements screen reader voice output with additional information",
        'settings_signature': "&Signature settings",
        'settings_password': "&Password manager",
        'settings_backup': "Create backup before changes",
        'settings_export_import': "&Export / import settings",
        'settings_export': "&Export all settings...",
        'settings_import': "&Import all settings...",
        'settings_export_info': "&What is exported?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "on",
        'voice_off': "off",
        'voice_toggle': "Voice output {0}",
        'voice_speed': "Speed at {0} percent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Tool not found:\n{0}\n\nBASE_DIR: {1}\nMake sure the PDF tools are installed in directory {1}.",
        'tool_started': "{0} started",
        'tool_start_failed': "Could not start",
        'process_error_failed_to_start': "Process could not be started. Does the file exist?",
        'process_error_crashed': "Process crashed during startup.",
        'process_error_timeout': "Process timeout reached.",
        'process_error_write': "Write error to process.",
        'process_error_read': "Read error from process.",
        'process_error_unknown': "Unknown process error",
        'process_command': "Command",
        'process_normal_exit': "exited normally",
        'process_crashed': "crashed",
        'process_nonzero_exit': "{0} exited with error code {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Cancelling...",
        'move_cancelling': "Moving cancelled",
        'opening_pdf': "Opening PDF...",
        'loading_document': "Loading document...",
        'pdf_opened': "PDF opened",
        'pages_found_moving': "{0} pages found, {1} to move",
        'creating_backup': "Creating backup...",
        'backup_description': "Backing up original file...",
        'backup_saved_as': "Backed up as: {0}",
        'error_format': "Error: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Search reset",
        'page_header_simple': "=== Page {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Password Manager – Guide",
        'password_guide_voice': "Guide to password management. Please read the notes.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Password Manager – Detailed Guide</strong></p>

        <p><strong>1. Password protection for PDFs</strong></p>
        <ul>
        <li>When opening a password-protected PDF, a dialog appears where you can enter the password.</li>
        <li>You can save the password encrypted so you don't have to enter it every time (checkbox "Save password").</li>
        <li>With the button "Remove password" you can create a decrypted copy of the PDF and delete the password from the database.</li>
        </ul>

        <p><strong>2. Master password</strong></p>
        <ul>
        <li>The master password protects access to all saved PDF passwords.</li>
        <li><strong>Setup:</strong> Go to "Settings → Password Manager → Master PW Settings" and click "Set up master password". Choose a strong password (at least 8 characters).</li>
        <li><strong>Change:</strong> After successful authentication you can change the master password.</li>
        <li><strong>Remove:</strong> If you delete the master password, ALL saved passwords are irretrievably deleted. You can export a backup beforehand.</li>
        <li>Once per session you must authenticate with the master password to access protected functions (e.g. viewing passwords).</li>
        </ul>

        <p><strong>3. Password manager (list)</strong></p>
        <ul>
        <li>Under "Settings → Password Manager" you open a table of all saved PDFs with their encrypted passwords.</li>
        <li><strong>Without master password:</strong> You can only delete entries – the passwords remain hidden.</li>
        <li><strong>With master password (authenticated):</strong> You can view, copy, export and delete passwords.</li>
        <li><strong>Export:</strong> Choose a format (JSON, CSV, TXT) and save the list. If a master password is set, you can decide whether the passwords are exported in plain text or still encrypted.</li>
        <li><strong>Import:</strong> A previously exported ZIP file with all settings (including passwords) can be re-imported via "Settings → Export/import settings". Caution: Existing data will be overwritten!</li>
        </ul>

        <p><strong>4. Password generator</strong></p>
        <ul>
        <li>In the password dialog (e.g. when protecting a PDF) you will find a dice button 🎲 to the right of the input field.</li>
        <li>Click it to open the password generator. You can set length, character sets (uppercase, lowercase, digits, symbols) and separators for better readability.</li>
        <li>The generated password can be adopted directly and copied if needed.</li>
        </ul>

        <p><strong>5. Important security notes</strong></p>
        <ul>
        <li>Saved passwords are stored encrypted with AES-256. The key is derived from your master password (if set) or from a fixed value (without master password).</li>
        <li>Without master password, the passwords are encrypted, but the key is embedded in the program – an attacker with access to your files could decrypt them. Therefore we strongly recommend using a master password.</li>
        <li>The password database is located in the directory `Data/passwords.json`. Make regular backups, especially before removing the master password.</li>
        <li>If the master password is lost, all saved passwords are irretrievably lost.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Inversion mode",
        'invert_mode_classic': "Classic (invert all colors)",
        'invert_mode_smart': "Smart (invert only brightness)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Grayscale threshold",
        'gray_threshold_10': "10% (strict)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Default)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (soft)",
        'threshold_changed': "Threshold set to {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Grayscale threshold – Explanation",
        'threshold_guide_text': "The grayscale threshold determines which pixels in smart dark mode are considered 'gray' and are inverted.\n\n"
                                "• A low value (10%) inverts only nearly perfect shades of gray – colored elements remain fully preserved.\n"
                                "• A high value (50%) also inverts slightly colored pixels – this increases contrast, but can distort colors.\n\n"
                                "The optimal value depends on the document. For pure text documents, 30–40% is often ideal, for colored graphics rather 10–20%.\n\n"
                                "You can adjust the value at any time via the 'Settings' menu – the PDF will then be reloaded immediately.\n\n"
                                "Note:\n* Photos and images can only be displayed correctly in Light Mode!\n* The inversion settings are only displayed when Dark Mode is activated.",
        'threshold_guide_voice': "The grayscale threshold determines how strongly the smart dark mode intervenes. A low value preserves colors, a high value increases contrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Opening PDF...",
        'progress_loading_document': "Loading document...",
        'progress_pdf_opened': "PDF opened",
        'progress_creating_backup': "Creating backup...",
        'progress_backup_description': "Securing original file...",
        'progress_backup_created': "Backup created",
        'progress_backup_saved_as': "Saved as: {0}",
        'progress_analyzing_start': "Starting analysis...",
        'progress_searching_empty': "Searching for empty pages...",
        'progress_page_empty': "Page {0} is empty",
        'progress_page_keep': "Keep page {0}",
        'progress_analysis_complete': "Analysis completed",
        'progress_empty_found': "Found {0} empty pages",
        'progress_current_page': "Current page",
        'progress_mark_delete': "Marked for deletion",
        'progress_range_selected': "Page range {0}-{1}",
        'progress_deleting_pages': "Deleting {0} pages",
        'progress_creating_new_pdf': "Creating new PDF...",
        'progress_transferring_pages': "Transferring pages",
        'progress_keeping_page': "Page {0} will be kept ({1}/{2})",
        'progress_saving_pdf': "Saving PDF...",
        'progress_optimizing': "Optimizing file size...",
        'progress_finalizing': "Finalizing...",
        'progress_new_size': "New size: {0:.2f} MB",
        'progress_cancelling': "Canceling...",
        'progress_cancel_message': "{0} is being canceled",
        'progress_pages_found_moving': "Found {0} pages, {1} to move",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analyzing PDF...",
        'ocr_status_optimizing': "Image optimization in progress...",
        'ocr_status_recognizing': "Text recognition in progress...",
        'ocr_status_embedding': "Embedding text...",
        'ocr_status_finalizing': "Finalizing PDF...",

        # PDF-Laden
        'progress_preparing': "Preparing...",
        'progress_loading': "Loading PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Deleting pages...",
        'progress_moving_title': "Moving pages...",
        'pages_found': "Pages found",
        'progress_creating_new_order': "Creating new order...",
        'progress_sorting_pages': "Sorting pages...",
        'progress_moving_to_begin': "Moving {0} pages to the beginning",
        'progress_transferring_count': "Transferring {0} pages",
        'progress_transferring_before_target': "Transferring pages before target",
        'progress_moving_pages': "Moving {0} pages",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_protected_",
        'filename_copy_suffix': "_Copy",
        'filename_page_single': "_Page_",
        'filename_page_range': "_Pages_",
        'filename_export_page': "_Page_{0:03}",
        'filename_export_range': "_Pages_{0}-{1}",
        'filename_export_multiple': "_Pages_{0}",
        'filename_with_text': "_with_Text",
        'filename_with_signature': "_with_Signature",
        'filename_with_image': "_with_Image",
        'filename_with_forms': "_with_Shapes",
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
        'view_toggle_navbar': "Show button bar",


		# ============================================
		# 57. SEITEN LÖSCHEN
		# ============================================
		'pages_cannot_delete_all': "Cannot delete all pages",
		'pages_cannot_delete_last_page': 'The last page cannot be deleted!',
		'pages_cannot_delete_all_pages': 'At least one page must remain in the document!',
		'delete_pages_confirm': 'Are you sure you want to delete {0} pages?',
		'delete_pages_confirm_voice': 'Are you sure you want to delete {0} pages?',
		'pages_deleted': '{0} pages were successfully deleted.',
		'warning': 'Warning',
		'error': 'Error',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "No form selected",
        'form_customized': "Form customized",

        # ============================================
        # 59. EXTENDED PASSWORD MANAGEMENT
        # ============================================
        'btn_select': "Select",
        'btn_use': "Use",
        'master_password_for_spasswords': "To store and use passwords, you must first set up a master password.\n\nDo you want to set up the master password now?",
        'open_saved_dialog_title': "Open saved file",
        'open_saved_question': "Do you want to open the saved file now?",
        'password': "Password",
        'password_manager_master_required': "The password manager is only available if a master password has been set up.\n\nDo you want to set up the master password now?",
        'password_master_required_for_select': "To view and select saved passwords, you must first authenticate with your master password.\n\nDo you want to authenticate now?",
        'password_not_available': "The selected password is not available or could not be decrypted.",
        'password_options_title': "Password options",
        'password_save_choice_change': "Set new password",
        'password_save_choice_keep': "Use existing password",
        'password_save_choice_none': "Save unencrypted",
        'password_save_hint': "First set up a master password to store passwords securely.",
        'password_save_master_required': "Save password (only possible with master password)",
        'password_save_question': "The current PDF is password protected. Do you want to use the existing password, set a new one, or save unencrypted?",
        'password_select': "Select password",
        'password_select_none': "No password selected.\n\nPlease select a password from the list.",
        'password_select_one': "Please select exactly one password.\n\nYou have marked multiple passwords.",

        # ============================================
        # 60. CENTRAL FILENAME GENERATION (additional suffixes)
        # ============================================
        'filename_backup_suffix': "_backup",
        'filename_insert_suffix': "_with_insertion",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_pages_deleted",
        'filename_pages_moved': "_pages_moved",
        'filename_rotated_all_suffix': "_all_pages_rotated",
        'filename_rotated_suffix': "_page_rotated",

        # ============================================
        # 61. FILENAME SETTINGS (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Configuration of filenames when changing PDF",
        'filename_keep_suffixes': "Keep previous extensions (e.g., _with_text)",
        'filename_keep_suffixes_false': "Replace",
        'filename_keep_suffixes_true': "Keep",
        'filename_preview_label': "Filename preview:",
        'filename_preview_overwrite_hint': "Preview not available – the original will be overwritten.",
        'filename_separator': "Separator between words",
        'filename_separator_none': "No separator",
        'filename_separator_space': "Space ( )",
        'filename_separator_underscore': "Underscore (_)",
        'filename_settings_saved': "Filename settings saved",
        'filename_settings_title': "Filename formatting & backup",
        'filename_timestamp_position': "Position of timestamp",
        'filename_timestamp_position_after': "After the base name",
        'filename_timestamp_position_before': "At the very front",
        'filename_timestamp_position_end': "At the end",
        'filename_use_timestamp': "Use timestamp",

        # ============================================
        # 62. BEHAVIOR ON CHANGES (Dialog)
        # ============================================
        'behavior_section': "<html><b>Behavior on changes like:</b><ul><li>Delete and insert pages</li><li>Insert text, signature, image and shapes</li><li>OCR...</li></ul></html>",
        'backup_section': "Backup for page operations (Delete, Move)",
        'behavior_info': "Note: With 'Overwrite original', timestamps and suffixes are ignored – the file keeps its name.",
        'behavior_new_file': "Always create new file (with timestamp and suffix)",
        'behavior_overwrite': "Overwrite original (no new file)",

        # ============================================
        # 63. SUCCESS MESSAGES (new file / overwrite)
        # ============================================
        'all_pages_rotated_new_file': "All pages were rotated.\n\nOriginal remained unchanged.\nNew file: {0}",
        'all_pages_rotated_voice': "All pages rotated, new file created.",
        'empty_pages_deleted_new_file': "{0} empty pages were deleted.\n\nOriginal remained unchanged.\nNew file: {1}",
        'empty_pages_deleted_voice': "{0} empty pages deleted, new file created.",
        'ocr_keep_original': "Keep original (open manually later)",
        'ocr_new_file_question': "The new searchable PDF was saved at:\n{0}\n\nDo you want to open it now?",
        'ocr_open_new': "Open new OCR file",
        'ocr_original_kept': "The original file remains open. The OCR file has been saved.",
        'page_deleted_new_file': "Page {0} was deleted.\n\nOriginal remained unchanged.\nNew file: {1}",
        'page_deleted_voice': "Page {0} deleted, new file created.",
        'page_rotated_new_file': "Page {0} was rotated.\n\nOriginal remained unchanged.\nNew file: {1}",
        'page_rotated_voice': "Page {0} rotated, new file created.",
        'pages_deleted_new_file': "{0} pages were deleted.\n\nThe original file remained unchanged.\nNew file: {1}",
        'pages_deleted_new_file_voice': "{0} pages deleted, new file created.",
        'pages_inserted_new_file': "{0} pages were inserted.\n\nThe original file remained unchanged.\nNew file: {1}",
        'pages_inserted_new_file_ask': "{0} pages were inserted.\n\nOriginal remained unchanged.\nNew file: {1}\n\nDo you want to open it now?",
        'pages_inserted_voice_new': "{0} pages inserted, new file created.",
        'pages_moved_new_file': "{0} pages were moved.\n\nThe original file remained unchanged.\nNew file: {1}",
        'pages_moved_new_file_voice': "{0} pages moved, new file created.",

        # ============================================
        # 64. BACKUP INFO DIALOG
        # ============================================
        'backup_do_not_show': "Do not show again",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Backup setting</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Backup ON</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">For all changes that overwrite the original</strong> (text, signature, image, shape, OCR, rotate, insert, delete/move pages) <strong>a backup with timestamp is automatically created</strong> before the change is applied.</p>
                <p style="margin: 5px 0 5px 20px;">• The backup is located next to the original file (e.g., <code>Document_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• If you have additionally activated the <strong>„Overwrite original“</strong> option, a backup is also created.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Backup OFF</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>No backup is created</strong> – neither when overwriting nor during page operations.</p>
                <p style="margin: 5px 0 5px 20px;">• The original file can be irretrievably lost when overwriting.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Recommended only for experienced users!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> The backup setting is independent of the "Overwrite original" option. You can combine both.<br>
                You can permanently hide this message.
            </div>
        </div>
        """,
        'backup_info_title': "Backup behavior",
        'backup_info_voice': "Notice about backup behavior during page operations. Backup ON overwrites original, Backup OFF creates new file.",
        'show_backup_info': "Info about backup setting",

        # ============================================
        # 65. OVERWRITE INFO DIALOG
        # ============================================
        'overwrite_do_not_show': "Do not show again",
        'overwrite_enable_backup': "Enable backup (recommended)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Overwrite original</p>
            <p>If you enable this option, changes (text, signature, image, shape, OCR, rotate, insert) are <strong>saved directly in the original</strong> – <strong>no new file is created</strong>.</p>
            <p>• The filename remains unchanged.<br>
            • Timestamps and suffixes are ignored.<br>
            • <strong>Without backup, the original can be irretrievably lost.</strong></p>
            <p style="color: #FFD700;">Recommendation: Additionally enable the backup option to get automatic backups.</p>
        </div>
        """,
        'overwrite_info_title': "Overwrite original",
        'overwrite_info_voice': "Warning: Overwrite original – no new file. Backup recommended.",

        # ======================================================
        # 66. SUCCESS MESSAGES (with different settings)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "{0} pages were inserted.\n\nThe original file was overwritten.\nA backup was created.",
        'pages_inserted_overwrite_no_backup': "{0} pages were inserted.\n\nThe original file was overwritten.\nNo backup was created.",
        'texts_saved_overwrite_with_backup': "The changes were saved in the original.\n\nA backup was created.",
        'texts_saved_overwrite_no_backup': "The changes were saved in the original.\n\nNo backup was created.",
        'texts_crosses_saved_new_file': "{0} {1} and {2} {3} were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'texts_saved_new_file': "{0} {1} were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'crosses_saved_new_file': "{0} {1} were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'elements_saved_new_file': "{0} elements were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'signatures_saved_overwrite_with_backup': "The signature(s) were saved in the original.\n\nA backup was created.",
        'signatures_saved_overwrite_no_backup': "The signature(s) were saved in the original.\n\nNo backup was created.",
        'images_saved_overwrite_with_backup': "The image(s) were saved in the original.\n\nA backup was created.",
        'images_saved_overwrite_no_backup': "The image(s) were saved in the original.\n\nNo backup was created.",
        'forms_saved_overwrite_with_backup': "The shape(s) were saved in the original.\n\nA backup was created.",
        'forms_saved_overwrite_no_backup': "The shape(s) were saved in the original.\n\nNo backup was created.",
        'signatures_saved_new_file': "{0} signatures were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'images_saved_new_file': "{0} images were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",
        'forms_saved_new_file': "{0} shapes were inserted.\n\nThe original file remained unchanged.\nA new file was created.\n\nLoading the new PDF...",

        # ======================================================
        # 67. ROTATED PAGES ROTATION
        # ======================================================
        'rotation_warning': "Warning: This PDF contains rotated pages. Positioning may deviate.",
        'page_rotated_warning_title': "Rotated page detected",
        'page_rotated_warning_message': "The current page {0} is rotated by {1}°.\n\nInserting elements on rotated pages is not supported.\n\nDo you want to rotate the page to upright position now?",
        'page_rotated_warning_voice': "Warning: The page is rotated. Please rotate it first.",
        'paste_on_rotated_page_simple_warning': "Inserting on page {0} not possible!\n\nThis page is rotated by {1}°.\n\nPlease first rotate the page to 0° (Menu: Edit → Align page).\n\nWarning:\nThe previously copied element will be lost if you do not save before rotating the page.",
        'paste_on_rotated_page_voice': "Insertion cancelled. Page is rotated. Please align the page first.",
        'page_rotated_cancel': "Cancel",
        'page_rotated_rotate_until_upright': "Rotate page repeatedly (until upright)",
        'page_rotated_now_upright': "The page is now upright. You can now insert.",
        'page_rotated_still_not_upright': "The page could not be rotated to upright position. Please correct manually.",

        # ============================================
        # 68. HELP DIALOG FOR PROBLEMATIC PAGES
        # ============================================
        'help_rotated_pages_title': "Help: Correct rotated pages",
        'help_rotated_pages_voice': "Help for correcting rotated pages is opening.",
        'btn_help': "Help",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Rotated page – Insertion does not work correctly</p>

            <p>If inserting texts, signatures or shapes on a rotated page does not work properly, you can correct the page with an external PDF editor.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Solution with external tool (e.g., macOS Preview)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Export page</strong><br>
                &nbsp;&nbsp;Click in the menu on <strong>File → Export as Pages</strong> or use another method to save the desired page as a single PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Open page in external program</strong><br>
                &nbsp;&nbsp;Open the exported PDF in a PDF editor (e.g., <strong>macOS Preview</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Rotate page</strong><br>
                &nbsp;&nbsp;Rotate the page so that it is upright (in Preview: <strong>Tools → Rotate</strong> or <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Save</strong><br>
                &nbsp;&nbsp;Save the corrected page (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Reinsert the page into the original document</strong><br>
                &nbsp;&nbsp;Return to PDFDarkView and insert the corrected page at the desired position:<br>
                &nbsp;&nbsp;<strong>Edit → Insert pages</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternative: Rotate page in the original</p>
                <p style="margin: 5px 0 5px 20px;">• Use the built-in rotate function (<strong>Edit → Rotate page</strong>) to correct the page step by step.<br>
                • After each rotation, you can check if insertion now works.<br>
                • This is often the faster solution – try it first!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tip:</strong> If you frequently encounter rotated pages, you can permanently hide the warning in the insert dialog.<br>
                Positioning may then deviate – only use this option if you know the consequences.
            </div>
        </div>
        """,

        # ============================================
        # 69. ROTATE AND RESET PAGES TO ZERO
        # ============================================
        'menu_rotate_normalize': "Align pages",
        'menu_rotate_normalize_tooltip': "Rotate page or reset to 0°",
        'normalize_current_page': "Bring current page to upright position (set to 0°)",
        'normalize_all_pages': "Bring all pages to upright position (set to 0°)",
        'page_normalized': "Page {0} was set to upright position.",
        'all_pages_normalized': "All pages were set to upright position.",
        'page_already_upright': "Page {0} is already upright.",
        'all_pages_already_upright': "All pages are already upright.",

        # ============================================
        # 70. EXPORT MESSAGES
        # ============================================
        'export_ocr_question_html': "<p>The PDF does not contain any searchable text.</p><p>Do you want to perform OCR to export to {0}?</p>",
        'export_ocr_voice': "The PDF does not contain any text. OCR required for export to {0}.",
        'export_no_ocr_possible': "Export without OCR not possible. Please perform OCR via the menu.",
        'ocr_failed_export_not_possible': "OCR failed. Export cannot be performed.",

        # ============================================
        # 71. PRINTING (additional messages)
        # ============================================
        'print_preview_start': "PDF will open in Preview. Please start the printing process there.",
        'print_preview_manual': "PDF has been opened. Please execute the print command manually (e.g., Ctrl+P).",

        # ============================================
        # 72. MERGE PDFS
        # ============================================
        'merge_pdfs_title': "Merge PDFs",
        'merge_pdfs': "Merge PDFs",
        'merge_progress_title': "Merging PDFs...",
        'merge_pdfs_list': "PDFs in order (Drag & drop to sort)",
        'merge_add_pdf': "Add PDF",
        'merge_remove': "Remove",
        'merge_move_up': "Move up",
        'merge_move_down': "Move down",
        'merge_pdfs_info': "💡 Tip: You can change the order by drag & drop",
        'merge_no_pdfs': "No PDFs selected. Click on 'Add PDF'.",
        'merge_info': "{0} PDFs selected (approx. {1} pages)",
        'merge_open_file': "Open file",
        'merge_merge': "Merge",
        'merge_error': "Error while merging",
        'merge_min_two_pdfs_error': "Please select at least two PDF files to merge.",
        'merge_select_pdfs': "Select PDFs to merge",
        'merge_error_file': "Error while processing",
        'merge_cancelled': "Merging was cancelled",
        'merge_preparing': "Preparing...",
        'merge_processing': "Processing PDF {0} of {1}",
        'merge_saving': "Saving merged PDF...",
        'merge_complete': "Done!",
        'merge_success_title': "Merge successful",
        'merge_success_voice': "{0} PDFs were successfully merged.",
        'merge_success_message': "{0} PDFs were successfully merged.\n\nThe new document now has {1} pages.\n\nNew file:\n{2}\n\nSave location:\n{3}\n{2}\n\nDo you want to open this PDF?",
        'replace_file_title': "Replace file?",
        'replace_file_message': "A PDF is already open. Do you want to replace it with the new file?",
        'btn_yes': "Yes",
        'btn_no': "No",
        'filename_merge_suffix': "merged",

        # ============================================
        # 73. PROGRESS MESSAGES FOR MERGE
        # ============================================
        'progress_merge_opening': "Opening {0}...",
        'progress_merge_reading': "Reading {0}...",
        'progress_merge_adding': "Adding {0} pages...",
        'progress_merge_optimizing': "Optimizing PDF...",
        'progress_merge_writing': "Writing PDF...",

        # ============================================
        # 74. SAVE BEFORE CLOSING
        # ============================================
        'action_close_pdf': "closing the PDF",
        'action_close_window': "closing the window",
        'action_open_new_pdf': "opening a new PDF",
        'action_quit_app': "quitting the application",
        'changes_saved': "The changes have been saved.",
        'file_close_title': "Close PDF file",
        'save_before_action': "Should the changes be saved before {0}? Yes or No?",
        'save_before_action_voice': "Should the changes be saved before {0}? Yes or No?",
        'save_before_close_question': "Should the changes be saved before closing? Yes or No?",

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Searchable PDF created:\n\n{0}\n\n<b>try again if necessary",
        "ocr_rotate_title": "Align pages before OCR",
        "ocr_rotate_question": "The PDF contains rotated pages.\nDo you want to align all pages to 0° before OCR?\nThis significantly improves text recognition.",
        "ocr_rotate_yes": "Yes, align",
        "ocr_rotate_no": "No, start OCR directly",
        "ocr_rotate_voice": "The PDF contains rotated pages. Should all pages be aligned before OCR?",
        "ocr_not_performed_message": "No text present. Please perform OCR (menu \"Edit\" → \"Perform OCR\" or key Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR Settings",
        "ocr_language_btn": "Select OCR language",
        "ocr_language": "OCR language(s)",
        "ocr_language_current": "Current language:",
        "ocr_param_info": "Parameter information",

        "ocr_force_ocr_label": "Force OCR",
        "ocr_deskew_label": "Correct skew",
        "ocr_clean_label": "Clean image",
        "ocr_oversample_label": "Resolution (DPI)",
        "ocr_pagesegmode_label": "Page segmentation",
        "ocr_oem_label": "OCR engine mode",
        "ocr_optimize_label": "PDF compression",
        "ocr_jobs_label": "Parallel processes",
        "ocr_verbose_label": "Log detail",

        "ocr_force_ocr_tooltip": "Force OCR on every page, even if text already exists",
        "ocr_deskew_tooltip": "Automatically align skewed scans",
        "ocr_clean_tooltip": "Remove noise and artifacts from the image",
        "ocr_oversample_tooltip": "Upscale image before OCR to this DPI",
        "ocr_pagesegmode_tooltip": "Determines how the page is divided into text areas",
        "ocr_oem_tooltip": "Selects Tesseract's OCR engine",
        "ocr_optimize_tooltip": "Compression level of the output PDF",
        "ocr_jobs_tooltip": "Number of parallel OCR processes",
        "ocr_verbose_tooltip": "Level of detail of log output",
        "ocr_settings_explain_btn": "Explanation",

        "ocr_force_ocr_explain": "Forces text recognition on <b>every</b> page, even if it already contains text.\n\nRecommendation: <b>On</b> for scanned PDFs, <b>Off</b> for native PDFs with existing text.",

        "ocr_deskew_explain": "Corrects slightly skewed scans (up to approx. 5°).\n\nRecommendation: <b>On</b> for scanned documents, <b>Off</b> if pages are already perfectly straight.",

        "ocr_clean_explain": "Removes noise, dots and small artifacts from the image.\n<b>IMPORTANT:</b> For Arabic, Thai or Vietnamese texts with diacritics (dots above/below letters) this option should be <b>disabled</b>, otherwise important characters may be lost.",

        "ocr_oversample_explain": "Upscales the image <b>before</b> text recognition to the specified DPI.<br><br>• <b>72-150 DPI:</b> Very fast, but low recognition rate<br>• <b>200-300 DPI:</b> Optimal range (Default: 300)<br>• <b>400+ DPI:</b> Barely better recognition, but significantly larger files<br><br>Recommendation: 300 DPI for complex scripts (Arabic, Chinese, Japanese), 200 DPI for Western languages.",

        "ocr_pagesegmode_explain": "Determines how Tesseract divides the page into text areas.\n\n• <b>3 - Automatic (Default):</b> Good for mixed layouts\n• <b>4 - Single column:</b> For single-column texts\n• <b>5 - Vertical block:</b> For vertical scripts (Japanese, Chinese)\n• <b>6 - Uniform text block:</b> Optimal for flowing text without columns\n• <b>11 - Raw image:</b> For poor scans / handwriting\n\nRecommendation: <b>6</b> for simple text documents, <b>3</b> for complex layouts.",

        "ocr_oem_explain": "Selects Tesseract's OCR engine.\n\n• <b>0 - Legacy:</b> Old engine (fast, but less accurate)\n• <b>1 - LSTM:</b> Neural engine (slower, but more accurate)\n• <b>2 - Legacy + LSTM:</b> Combines both results\n• <b>3 - Default (LSTM preferred):</b> Best choice for most cases\n\nRecommendation: <b>3</b> for maximum recognition accuracy.",

        "ocr_optimize_explain": "Compresses the output PDF.\n\n• <b>0:</b> No optimization (fastest processing)\n• <b>1:</b> Light optimization (good compromise)\n• <b>2:</b> Moderate optimization\n• <b>3:</b> Strong optimization (smallest file, but slower)\n\nRecommendation: <b>1</b> for daily use.",

        "ocr_jobs_explain": "Number of parallel processes for OCR.\n\n• <b>1:</b> Slow, but lowest memory consumption\n• <b>4-8:</b> Optimal for modern multi-core processors\n• <b>12+:</b> Barely faster processing at high memory usage\n\nRecommendation: Number of CPU cores (e.g. <b>4</b> on 4-core systems).",

        "ocr_verbose_explain": "Level of detail of log output in the console.\n\n• <b>0:</b> No output\n• <b>1:</b> Progress and status messages\n• <b>2:</b> Detailed output\n• <b>3:</b> Full debug output (very extensive)\n\nRecommendation: <b>1</b> for normal operation.",

        "ocr_reset_title": "Settings reset",
        "ocr_reset_message": "All OCR settings have been reset to default values.",
        "info_tooltip": "More information about this parameter",
        "ocr_reset_defaults": "Reset to defaults",

        "ocr_psm_0": "Automatic (Legacy engine)",
        "ocr_psm_1": "Automatic column detection",
        "ocr_psm_3": "Automatic (Default)",
        "ocr_psm_4": "Single column",
        "ocr_psm_5": "Vertical block",
        "ocr_psm_6": "Uniform text block",
        "ocr_psm_7": "Single text line",
        "ocr_psm_8": "Single word",
        "ocr_psm_11": "Raw image (no layout analysis)",

        "ocr_oem_0": "Legacy engine (fast)",
        "ocr_oem_1": "LSTM engine (neural, accurate)",
        "ocr_oem_2": "Legacy + LSTM combined",
        "ocr_oem_3": "Default (LSTM preferred)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR language(s)...",
        "ocr_language_title": "Select OCR language(s)",
        "ocr_language_instruction": "Select the language(s) for text recognition (OCR).\nCaution: Multiple languages come at the expense of performance and accuracy!\nYou achieve the best results if you select only one language.",
        "ocr_language_predefined": "Predefined combinations",
        "ocr_language_custom": "Custom...",
        "ocr_language_selected": "Selected OCR languages",
        "ocr_language_changed": "OCR language changed to {0}",
        "ocr_language_auto_detect": "Available languages are automatically detected.",
        "ocr_language_none_found": "No Tesseract language data found! Please install language packages (e.g. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Custom language selection",
        "ocr_language_available": "Available languages (installed):",
        "ocr_language_select_hint": "Select one or more languages:",
        "ocr_language_confirm": "Apply",
        "ocr_language_reset": "Reset to default (deu+eng+vie)",
        "ocr_language_priorities": "Recommended languages (pre-installed):",

        "select_all_languages": "Select all",
        "clear_all_languages": "Clear selection",
        "install_language_packs": "Install missing language packages...",
        "install_hint": "💡 Tip: Not all languages are installed on your system. Use this button to get installation help.",
        "ocr_language_install_title": "Installation of Tesseract language packages",

        "ocr_missing_languages": "Missing OCR language packages",
        "ocr_missing_languages_message": "The following selected languages are not installed on your system:\n\n{0}\n\nPlease install the missing language packages (see help under 'Installation help').\n\nDo you want to open the installation help now?",
        "ocr_missing_languages_voice": "Missing language packages. Please install the missing languages.",
        "ocr_install_help_now": "Open help",
        "ocr_continue_anyway": "Try anyway",
        "ocr_language_error_title": "OCR language error",
        "ocr_language_error_message": "Error during text recognition: {0}\n\nPlease check your OCR language settings (Settings → OCR language).",
        "ocr_install_help_button": "Installation help",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Install Tesseract language packages</p>

        <p>For OCR to work in a specific language, the corresponding language data must be installed on your system. Follow the instructions for your operating system:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Open <strong>Terminal</strong> (Finder → Programs → Utilities → Terminal).</li>
        <li>Install all available languages with:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (This may take a few minutes.)</li>
        <li>Or only individual languages (e.g. Vietnamese):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        With current Homebrew versions, <code>*.traineddata</code> may need to be downloaded manually (see below).</li>
        <li>After installation: Close this dialog and open the OCR language selection again – the new languages will appear automatically.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Open a terminal (Ctrl+Alt+T).</li>
        <li>Install the desired language, e.g. for Vietnamese:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Important language codes: <code>deu</code> (German), <code>eng</code> (English), <code>vie</code> (Vietnamese), <code>spa</code> (Spanish), <code>fra</code> (French), <code>ita</code> (Italian), <code>nld</code> (Dutch), <code>fin</code> (Finnish), <code>swe</code> (Swedish), <code>nor</code> (Norwegian).</li>
        <li>Show all available packages:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manual)</p>
        <ol>
        <li>Download the desired <code>*.traineddata</code> files from:<br>
        <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (e.g. <code>vie.traineddata</code> for Vietnamese).</li>
        <li>Copy the files to the Tesseract language folder, usually:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Adjust according to individual installation.)</li>
        <li>Restart the application (or reopen the OCR language selection).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternative for all systems</p>
        <ul>
        <li>Install <strong>OCRmyPDF</strong> and <strong>Tesseract</strong> with a package manager of your choice. Most installations already contain some standard languages (English, German, French).</li>
        <li>Missing languages can be installed at any time – the OCR language selection only lists the actually existing languages.</li>
        </ul>

        <hr>
        <p><b>✅ After installation:</b> No restart of the application necessary – the newly added languages will appear immediately in the list.</p>
        <p><b>📖 Help with language codes:</b> A complete list is available in the <a style="color:#E0E0E0;" href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract documentation</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans fonts",
        "info_noto_font_voice": "Noto Sans font installation guide",
        "btn_info_noto_font_install": "Font info",

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ How to install the free Noto fonts from Google</h2>

        <p>The <strong>Noto fonts</strong> are an open-source font family from Google. Their goal is to see <em>"no tofu"</em> (i.e. no empty boxes □) and to correctly display every character from the Unicode standard. They are the ideal addition for applications that need to display texts in many different languages.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installation on macOS</h3>

        <p><strong>Method 1: With Homebrew (for advanced users)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Method 2: Via "Font Book" (Recommended)</strong></p>

        <ol>
        <li>Download the official font package:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extract the ZIP file</li>
        <li>Copy files to <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installation on Windows (10 & 11)</h3>

        <p><strong>Method 1: Microsoft Store (Recommended)</strong><br>
        Search for "Google Noto Fonts" or "Noto Sans" and click <strong>Install</strong>.</p>

        <p><strong>Method 2: Manual installation</strong></p>

        <ol>
        <li>Download:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Extract ZIP</li>
        <li>Select .ttf / .otf files</li>
        <li>Right-click → <strong>Install</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        or<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Name\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installation on Linux</h3>

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

        <p>Verification:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Manage bookmarks",
        "bookmark_add": "Add bookmark",
        "bookmark_add_tooltip": "Save current page as bookmark",
        "bookmark_remove": "Remove bookmark",
        "bookmark_remove_tooltip": "Delete the marked bookmark",
        "bookmark_remove_all": "Remove all",
        "bookmark_remove_all_tooltip": "Delete all bookmarks of this PDF",
        "bookmark_jump": "Go to bookmark",
        "bookmark_jump_tooltip": "Go to selected page",
        "bookmark_name": "Name",
        "bookmark_page": "Page",
        "bookmark_no_bookmarks": "No bookmarks present.\nClick 'Add' to save the current page as a bookmark.",
        "bookmark_added": "Bookmark for page {0} added: {1}",
        "bookmark_removed": "Bookmark removed: {0}",
        "bookmark_all_removed": "All bookmarks have been removed.",
        "bookmark_name_default": "Page {0}",
        "bookmark_name_prompt": "Name for the bookmark:\n(long text will be shortened to 50 characters)",
        "bookmark_name_prompt_title": "Bookmark name",
        "bookmark_confirm_remove_all": "Are you sure you want to remove all {0} bookmarks?",
        "menu_bookmarks": "Bookmarks",
        "bookmark_manage": "Manage bookmarks",
        "bookmark_next": "Next bookmark",
        "bookmark_prev": "Previous bookmark",
        "bookmark_page_display": "Page {0}",
        "bookmark_exists": "A bookmark for this page with this name already exists.",
        "bookmark_select_first": "Please select a bookmark first.",
        "bookmark_confirm_remove": "Are you sure you want to remove the bookmark 'Page {0}: {1}'?",
        "bookmark_jumped_to": "Jumped to bookmark '{0}' on page {1}.",
        "bookmark_jumped_to_voice": "Bookmark {0}, page {1}",
        "btn_close": "Close",

        "bookmark_list": "Your bookmarks",
        "bookmark_rename": "Rename bookmark",
        "bookmark_rename_tooltip": "Change the name of the selected bookmark",
        "bookmark_rename_title": "Rename bookmark",
        "bookmark_rename_prompt": "New name for bookmark on page {0}:\n(max. 50 characters)",
        "bookmark_renamed": "Bookmark '{0}' has been renamed to '{1}'.",
        "bookmark_item_tooltip": "Page {0}: {1}\nDouble-click to jump",
        "bookmark_name_exists_question": "A bookmark with the name '{0}' already exists on this page.\nRename anyway?",

        "context_bookmarks": "Bookmarks",
        "context_bookmark_add_here": "Add bookmark for this page",
        "context_bookmarks_existing": "Existing bookmarks:",
        "context_bookmarks_jump": "Go to bookmark:",
        "context_bookmarks_none": "No bookmarks present",
        "context_bookmarks_clear_all": "Remove all {0} bookmarks",

        "bookmark_search_placeholder": "Search bookmarks... (name or page)",
        "bookmark_search_results": "%d bookmarks found for \"%s\"",
        "bookmark_no_search_results": "No bookmarks found for \"%s\"",
        "bookmark_no_search_results_label": "No results for \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Edit PDF metadata",
        "metadata_title": "Title",
        "metadata_title_placeholder": "Document title",
        "metadata_title_tooltip": "The title of the document (displayed in the title bar)",
        "metadata_author": "Author",
        "metadata_author_placeholder": "Author's name",
        "metadata_author_tooltip": "The creator of the document",
        "metadata_subject": "Subject",
        "metadata_subject_placeholder": "Subject of the document",
        "metadata_subject_tooltip": "A short description of the content",
        "metadata_keywords": "Keywords",
        "metadata_keywords_placeholder": "Keywords, separated by commas",
        "metadata_keywords_tooltip": "Keywords for categorizing the document",
        "metadata_creator": "Creator",
        "metadata_creator_placeholder": "Application that created the PDF",
        "metadata_creator_tooltip": "The software with which the document was created",
        "metadata_producer": "Producer",
        "metadata_producer_placeholder": "Application that converted the PDF",
        "metadata_producer_tooltip": "The software that converted the PDF",
        "metadata_creation_date": "Creation date",
        "metadata_creation_date_tooltip": "The date of document creation",
        "metadata_mod_date": "Modification date",
        "metadata_mod_date_tooltip": "The date of the last modification",
        "metadata_pdf_info": "📄 PDF information",
        "metadata_pages": "Number of pages",
        "metadata_file_size": "File size",
        "metadata_pdf_version": "PDF version",
        "metadata_encrypted": "Encrypted",
        "metadata_encrypted_yes": "Yes (password protected)",
        "metadata_encrypted_no": "No",
        "metadata_reload": "📂 Reload from PDF",
        "metadata_reset": "Discard changes",
        "metadata_reloaded": "Metadata has been reloaded from the PDF.",
        "metadata_reset_done": "All metadata fields have been reset.",
        "metadata_no_file": "No PDF file loaded.",
        "metadata_save_error": "Error saving metadata",
        "metadata_saved": "Metadata has been saved successfully.",
        "metadata_pdf_version_unknown": "PDF (unknown)",
        "metadata_saved_message": "The metadata has been saved successfully.",
        "metadata_saved_voice": "Metadata saved.",

        "metadata_custom": "🔧 Custom metadata",
        "metadata_custom_placeholder": "{\n  \"my_field\": \"my value\",\n  \"other_field\": 123\n}",
        "metadata_custom_tooltip": "JSON format for custom metadata (optional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Template \"{0}\" selected - Double-click to insert",
        "text_use_template": "Use text block",
        "text_type": "Type",
        "text_search_templates": "Search text blocks...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Export / Import Information",
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

        <h3>📦 What is exported? (Overview)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">General application settings</span></li>
            <li class="detail">• Dark/Light mode</li>
            <li class="detail">• Dark mode inversion for images</li>
            <li class="detail">• Gray threshold value</li>
            <li class="detail">• Language</li>
            <li class="detail">• Window geometry</li>
            <li class="detail">• Zoom mode</li>
            <li class="detail">• Navigation (Navbar visible)</li>
            <li class="detail">• Speech output (on/off)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Backup settings</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">File naming (Timestamp, Separator, Suffixes)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Settings for insertions of</span></li>
            <li class="detail">• Signatures</li>
            <li class="detail">• Text &amp; text blocks</li>
            <li class="detail">• Checks, images and shapes</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR settings</span></li>
            <li class="detail">• Language</li>
            <li class="detail">• Force OCR · Page mode</li>
            <li class="detail">• Image preprocessing: Deskew, Clean, Oversampling</li>
            <li class="detail">• Number of parallel jobs</li>
            <li class="detail">• Inversion mode</li>
            <li class="detail">• Gray threshold value</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Bookmarks</span></li>
            <li class="detail">• All bookmarks per PDF file (Page, Name, Creation time)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Password database</span></li>
            <li class="detail">• Saved PDF passwords (optionally encrypted or plain text)</li>
            <li class="detail">• Master password hash (if set)</li>
            <li class="detail">• Verification data</li>
        </ul>

        <h4>⚠️ Important notes</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 When importing:</strong>
            <ul>
                <li><span class="warning">➜ ALL current settings will be completely overwritten</span></li>
                <li>• A restart of the application is mandatory</li>
                <li>• Existing signatures, text blocks and bookmarks will be replaced</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Master password &amp; export mode:</strong>
            <ul>
                <li>• When master password is active, you can choose:</li>
                <li>  - <span style="color: #98FB98;"><strong>Decrypted</strong></span> (passwords are in plain text in the ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Encrypted</strong></span> (only readable with master password on the target system)</li>
                <li>• The master password hash itself is <strong>always</strong> stored encrypted</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Security notice:</strong>
            <ul>
                <li>• The exported ZIP file contains sensitive data (<strong>passwords, bookmarks, signatures</strong>)</li>
                <li>• Please store it securely (e.g. encrypted USB stick, password manager)</li>
                <li>• If the file is lost, saved PDF passwords are irretrievably lost</li>
            </ul>
        </div>

        <h4>📁 Export format</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            The settings are saved in a single ZIP file:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            This ZIP contains the complete <code>settings.json</code> (from your configuration) as well as possibly embedded signature image files and encrypted passwords.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Signatures - Guide",
        'signature_guide_html': """
        📝 <strong>Signatures - Quick Guide</strong><br>
        <ul>
        <li>Set up master password</li>
        <li>Configure signatures in <em>Settings</em> menu (size, timestamp, …)</li>
        <li>Insert with <strong>RIGHT CLICK</strong> at desired position (master password required once per session)</li>
        <li>Move signature with mouse or arrow keys</li>
        <li>Insert multiple signatures one after another</li>
        <li>Customize each signature individually</li>
        <li>Discard single signature</li>
        <li>Save / discard all signatures at once</li>
        <li>Alternatively, you can also use the menu bar.</li>
        </ul>
        """,
        'signature_guide_voice': "Quick guide for signatures. Set up master password. Configure signatures in settings. Insert with right click.",

        'image_guide_title': "Insert images - Guide",
        'image_guide_html': """
        📷 <strong>Insert images into PDF - Quick Guide</strong><br>
        <ol>
        <li>Right click on desired position</li>
        <li><em>"Insert image"</em> → select image</li>
        <li>Position image: Drag with mouse</li>
        <li>Adjust size: Drag at corners/edges</li>
        <li>Keep aspect ratio: Press <strong>[A]</strong></li>
        <li>Further adjustments: Right click on image</li>
        </ol>
        <p><strong>Tip:</strong> You can adjust settings in the context menu.</p>
        """,
        'image_guide_voice': "Quick guide for images. Right click, insert image, select. Position with mouse, adjust size at corners. Keep aspect ratio with key A.",

        'form_guide_title': "Insert shapes - Guide",
        'form_guide_html': """
        📐 <strong>Insert shapes into PDF - Quick Guide</strong><br>
        <ol>
        <li>Select shape type (rectangle, ellipse, line, arrow)</li>
        <li>Click on position:
            <ul>
            <li>For rectangle/ellipse: One click places the shape</li>
            <li>For line/arrow: Two clicks for start and end point</li>
            </ul>
        </li>
        <li>Position shape: Drag with mouse</li>
        <li>Adjust size: Drag at corners/edges</li>
        <li>Save shape: <strong>Enter</strong></li>
        <li>Discard shape: <strong>ESC</strong></li>
        <li>Further adjustments: Right click on shape</li>
        </ol>
        <p><strong>Tip:</strong> You can adjust settings in the context menu.</p>
        """,
        'form_guide_voice': "Quick guide for shapes. Select shape type. For rectangle or ellipse click once, for line or arrow click twice. Position with mouse, adjust size at corners. Save with Enter, discard with Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "previous",
        "btn_next_result": "next",
        "ocr_text_window": "OCR Text Window",
        "bookmark_existing": "Existing bookmarks",


        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR Comparison Mac - Windows",
        'ocr_method_mac_win_title': "OCR Differences Mac and Windows",
        'ocr_method_mac_win_voice': "Mac is better",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Differences between macOS and Windows</strong></p>

        <p><strong>macOS (recommended)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Result:</p>
        <ul>
        <li>A searchable PDF with embedded text that largely preserves the original layout.</li>
        </ul>
        <p>Advantages:</p>
        <ul>
        <li>Excellent text recognition quality (even with skewed pages).</li>
        <li>Preservation of vector graphics and fonts.</li>
        <li>GUI progress bar via subprocess evaluation.</li>
        <li>Full control over all OCR parameters (deskew, clean, oversample, optimization).</li>
        <li>Text search is available directly in the main window (PDF view).</li>
        </ul>
        <p>Disadvantages:</p>
        <ul>
        <li>Requires additional system tools (ocrmypdf, Ghostscript, unpaper, pngquant – included in the app bundle).</li>
        <li>More complex error handling (deadlocks, timeouts).</li>
        </ul>

        <p><strong>Windows (stable alternative)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>pytesseract (direct binding to Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Result:</p>
        <ul>
        <li>A searchable PDF that visually resembles an image PDF but is searchable due to transparent text.</li>
        </ul>
        <p>Advantages:</p>
        <ul>
        <li>None come to mind right now.</li>
        </ul>
        <p>Disadvantages:</p>
        <ul>
        <li>The PDF is essentially an image with invisible text; layout may deviate slightly for complex documents (columns, tables).</li>
        <li>No automatic skew correction (--deskew) or image cleaning (--clean).</li>
        <li>The GUI progress bar is only updated roughly based on the number of processed pages.</li>
        <li>OCR speed is slightly slower (because each page is processed individually).</li>
        <li>Text search is redirected to the OCR text window.</li>
        </ul>

        <p><strong>Commonalities</strong></p>
        <ul>
        <li>Both methods produce a searchable PDF in the same directory as the source file.</li>
        <li>OCR settings (language, DPI, page segmentation mode, OCR engine mode) can be configured via the OCRSettingsDialog and take effect in both implementations.</li>
        </ul>

        <p><strong>Recommendation:</strong></p>
        <ul>
        <li>macOS: The ocrmypdf binary delivers the best results – buy a Mac and use the version (PDFDarkView for Macs with Apple Silicon or Intel chip). The OCR results are better than on Windows!</li>
        <li>Windows: Use the pytesseract solution. It is stable and provides completely sufficient quality for most documents.</li>
        </ul>

        <p><strong>Important note:</strong></p>
        <ul>
        <li>Both versions are fully integrated into the user interface – the user notices no difference.</li>
        <li>The program automatically decides which OCR engine to use based on the operating system.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN
        # ============================================
        "signature_create_from_scan": "Create signature (from scan)",
        "signature_create_title": "Select scanned signature (PDF/Image)",
        "image_pdf_filter": "Images and PDF",
        "signature_pdf_empty": "The PDF contains no pages.",
        "signature_created_success": "Signature successfully created: {0}",
        "signature_create_error": "Error creating signature:\n{0}",
        "rembg_missing": "rembg is not installed.\nPlease run: pip install rembg\nError: {0}",
        "signature_name_title": "Filename for signature",
        "signature_name_message": "Enter a filename for the new signature (saved as PNG with transparent background):",
        "signature_name_label": "Filename:",
        "signature_name_voice": "Enter filename for signature",
        "signature_processing": "Processing...",
        "signature_creation_title": "Creating signature",
        "signature_overwrite_warning": "File '{0}' already exists. Overwrite?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Prepare PDF for Signature",
        "signature_prepare_instruction":"Please select a PDF that contains a scanned signature on a single page.\n\nOptimal recognition is achieved if:\n• The signature is written with black ink (ballpoint pen or fineliner) on white paper.\n• The signature is located in the upper third of an otherwise blank A4 page.\n• The PDF was scanned at at least 300 dpi.\n• The signature is clear and not too thin.\n• There are no distracting background patterns or lines.",
        "signature_prepare_voice":"Please select a PDF with a scanned signature. Pay attention to good quality and contrast.",
        "sig_thickness_label":"Line thickness:",
        "sig_thickness_normal":"Normal (thin)",
        "sig_thickness_bold":"Bold (recommended)",
        "sig_thickness_very_bold":"Very bold",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
                # ============================================
        'language_guide_menu': "Add GUI and OCR Languages - Guide",
        'language_guide_title': "Add GUI and OCR Languages",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Download the desired translation file <code>translations_xy.py</code> from<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez/PDFDarkView/tree/main/translations">https://github.com/BinhDiez/PDFDarkView/tree/main/translations</a><br/>
        and place it in the following directory:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Open your web browser.</li>
        <li>Go to: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Look on the right side of the screen for "Releases" and select the one marked <strong>"latest"</strong>.</li>
        <li>On the following release page, scroll to the bottom and download the <code>Source Code.zip</code> file.</li>
        <li>Extract the ZIP file.</li>
        <li>In the extracted folder, find all the language files you need and copy them into the directory:<br/>
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
        "menu_watermark":"Insert watermark",
        "fullpage_text_watermark_title":"Text as watermark",
        "fullpage_image_watermark_title":"Image as watermark",
        "filename_with_watermark":"_with_watermark",
        "watermark_text":"Text:",
        "watermark_text_placeholder":"Your watermark text...",
        "watermark_font_family":"Font:",
        "watermark_font_size":"Font size:",
        "watermark_format":"Formatting:",
        "watermark_bold":"Bold",
        "watermark_italic":"Italic",
        "watermark_color":"Color:",
        "watermark_choose_color":"Choose color...",
        "watermark_opacity":"Opacity / Transparency:",
        "watermark_direction":"Reading direction:",
        "watermark_direction_l_r":"Left → Right",
        "watermark_direction_bl_tr":"Bottom left → Top right",
        "watermark_direction_tl_br":"Top left → Bottom",
        "watermark_direction_b_t":"Bottom → Top",
        "watermark_direction_t_b":"Top → Bottom",
        "watermark_preview":"Preview:",
        "watermark_preview_sample":"Sample text",
        "watermark_empty_text":"Please enter text.",
        "watermark_applied":"Watermark has been applied to all pages.",
        "watermark_saved":"Watermark saved.",
        "image_scale":"Size:",
        "image_preview":"Image preview:",
        "no_image_selected":"No image selected",
        "browse":"Browse...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI
        # ============================================
        "menu_redact": "Redactions",
        "redact_add_black": "Redaction (black)",
        "redact_add_white": "Redaction (white / erase)",
        "redact_added_black": "Black redaction added",
        "redact_added_white": "White redaction added",
        "redact_apply_all": "Apply all redactions and save",
        "redact_discard_all": "Discard all redactions",
        "redact_discard": "Discard this redaction",
        "no_redactions": "No redactions",
        "redact_confirm_title": "Apply redactions permanently",
        "redact_confirm_message": "Warning: Marked areas will be permanently deleted (black or white).\nA backup will be created (if enabled).\n\nContinue?",
        "redact_apply": "Yes, redact now",
        "redact_saved": "{0} redaction(s) successfully applied and saved.",
        "redact_saved_voice": "{0} redaction(s) applied",
        "redact_error": "Error during redaction",
        "filename_redacted":"_redacted",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        'page_numbers_title': 'Insert page numbers',
        'page_numbers_format': 'Number format:',
        'page_numbers_format_arabic': '1, 2, 3 ... (Arabic)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (Roman lowercase)',
        'page_numbers_format_roman_upper': 'I, II, III ... (Roman uppercase)',
        'page_numbers_format_letter': 'A, B, C ... (Letters)',
        'page_numbers_format_custom': 'Custom',
        'page_numbers_custom_pattern': 'Pattern:',
        'page_numbers_custom_placeholder': 'e.g. "Page {nummer}" or "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Use {nummer} for current page number and {total} for total count',
        'page_numbers_position': 'Position:',
        'page_numbers_pos_tl': 'Top left',
        'page_numbers_pos_tc': 'Top center',
        'page_numbers_pos_tr': 'Top right',
        'page_numbers_pos_ml': 'Middle left',
        'page_numbers_pos_mc': 'Centered',
        'page_numbers_pos_mr': 'Middle right',
        'page_numbers_pos_bl': 'Bottom left',
        'page_numbers_pos_bc': 'Bottom center',
        'page_numbers_pos_br': 'Bottom right',
        'page_numbers_margins': 'Margins:',
        'page_numbers_margin_x': 'Horizontal margin:',
        'page_numbers_margin_y': 'Vertical margin:',
        'page_numbers_range': 'Page range:',
        'page_numbers_all_pages': 'All pages',
        'page_numbers_custom_range': 'Custom range',
        'page_numbers_from': 'From:',
        'page_numbers_to': 'To:',
        'page_numbers_progress': 'Inserting page numbers...',
        'page_numbers_start': 'Starting page number insertion...',
        'page_numbers_cancel': 'Page number insertion cancelled',
        'page_numbers_success': 'Page numbers were successfully added.\n\nWould you like to open the new PDF?\n\n{0}',
        'page_numbers_complete': 'Page numbers were added',
        'page_numbers_error_format': 'Error inserting page numbers: {0}',
        'page_numbers_content_type': 'Content type:',
        'page_numbers_tab_simple': 'Simple number',
        'page_numbers_tab_range': 'Page X of Y',
        'page_numbers_tab_date': 'Date',
        'page_numbers_tab_custom': 'Free text',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Page {aktuell} of {gesamt}',
        'page_numbers_range_custom': 'Custom',
        'page_numbers_range_placeholder': 'e.g. "Page {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Date format:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': 'January 1, 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Custom',
        'page_numbers_date_placeholder': 'e.g. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Position:',
        'page_numbers_date_before': 'Date before page number',
        'page_numbers_date_after': 'Date after page number',
        'page_numbers_date_only': 'Date only (no page number)',
        'page_numbers_custom_text': 'Custom text:',
        'page_numbers_custom_placeholder_text': 'Use {seite} for page number and {gesamt} for total\ne.g. "Confidential - Page {seite}" or "{seite} of {gesamt}"',
        "filename_with_page_number":"_with_page_number",
        "filename_with_page_declaration":"_with_page_statement",
        "filename_with_pagenumber":"_with_page_number",
        "filename_with_date":"_with_date",
        "filename_with_my_page_declaration":"_with_custom_page_statement",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Unsaved changes",
        "unsaved_changes_message_darkmode": "There are unsaved insertions.\nWould you like to save them before switching?",
        "save_and_switch": "Save and switch",
        "discard_and_switch": "Switch now",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        'export_images_title': 'Export pages as images',
        'export_images_menu': 'Export as images (PNG/JPEG)',
        'export_images_format': 'Image format:',
        'export_images_dpi': 'Resolution (DPI):',
        'export_images_quality': 'JPEG quality:',
        'export_images_range': 'Page range:',
        'export_images_all_pages': 'All pages',
        'export_images_custom_range': 'Custom range',
        'export_images_from': 'From:',
        'export_images_to': 'To:',
        'export_images_options': 'Options:',
        'export_images_single_files': 'Each page as separate file',
        'export_images_subfolder': 'Export to subfolder',
        'export_images_subfolder_info': 'To subfolder "PDFname_images"',
        'export_images_same_folder': 'In same folder as PDF',
        'export_images_apply_darkmode': 'Apply PDFDarkView settings (Dark Mode)',
        'export_images_target_folder': 'Target folder:',
        'export_images_browse': 'Browse...',
        'export_images_preview': 'Preview:',
        'export_images_preview_info': 'Select settings for export',
        'export_images_preview_info_detail': '{0} pages as {1}\nResolution: {2} DPI\nFilename: {3}\n{4}',
        'export_images_select_folder': 'Select target folder',
        'export_images_start': 'Starting image export...',
        'export_images_progress': 'Exporting images...',
        'export_images_saving': 'Saving page {0} of {1}...',
        'export_images_success': 'Export successful!\n\n{0} images were saved in:\n{1}',
        'export_images_complete': 'Image export completed',
        'export_images_open_folder': '📁 Open folder',
        'export_images_cancel': 'Image export cancelled',
        'export_images_error_format': 'Error exporting images: {0}',
        'export_images_pdf2image_missing': 'The library "pdf2image" is not installed.\n\nPlease install it with:\npip install pdf2image\n\nFor Windows you also need Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        'pdfa_title': 'PDF/A conversion for long-term archiving',
        'pdfa_menu': 'PDF/A conversion (archive-ready)',
        'pdfa_info': 'Converts the PDF to PDF/A format.\n\nPDF/A is specifically designed for long-term archiving and ensures that the document will be displayed correctly in the future.',
        'pdfa_standard': 'PDF/A standard:',
        'pdfa_standard_select': 'Version:',
        'pdfa_1': 'PDF/A-1 (simple, widely compatible)',
        'pdfa_2': 'PDF/A-2 (modern, better compression)',
        'pdfa_3': 'PDF/A-3 (latest version, allows attachments)',
        'pdfa_standards_explanation': '📖 Explanation of standards:\n\n'
            '• PDF/A-1: Basic, compatible with older systems (approx. 2005)\n'
            '• PDF/A-2: More modern, better compression, transparency support (approx. 2011)\n'
            '• PDF/A-3: Latest version, allows embedding of file attachments (approx. 2013)\n\n'
            'Recommendation: PDF/A-2 is a good compromise between compatibility and modern features.',
        'pdfa_options': 'Options:',
        'pdfa_compress_enable': 'Compress PDF (smaller file)',
        'pdfa_metadata_preserve': 'Preserve metadata (title, author, etc.)',
        'pdfa_target_folder': 'Target folder:',
        'pdfa_browse': 'Browse...',
        'pdfa_select_folder': 'Select target folder',
        'pdfa_ocr_info_unknown': '🔍 Could not check text content.',
        'pdfa_ocr_info_not_needed': '✅ Text available - OCR is not required.\nPDF/A can be created directly.',
        'pdfa_ocr_info_recommended': '⚠️ No sufficient text found.\n\nFor searchable PDFs we recommend running OCR first.\nNote: PDF/A also works without OCR - but the text will not be searchable.',
        'pdfa_ocr_info_error': '❌ Error while checking: {0}',
        'pdfa_start': 'Starting PDF/A conversion...',
        'pdfa_progress': 'PDF/A conversion in progress...',
        'pdfa_success': 'PDF/A conversion successful!\n\nSaved as:\n{0}\n\nWould you like to open the new PDF?',
        'pdfa_complete': 'PDF/A conversion completed',
        'pdfa_cancel': 'PDF/A conversion cancelled',
        'pdfa_error_format': 'Error during PDF/A conversion:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'The library "ocrmypdf" is not installed.\n\nPlease install it with:\npip install ocrmypdf',
        'btn_convert': 'Convert',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        # ============================================
        # 95. OPTIMIEREN (KOMPRIMIEREN)
        # ============================================
        'optimize_title': 'Optimize PDF (reduce file size)',
        'optimize_menu': 'Optimize PDF (file size)',
        'optimize_info': 'Reduces the file size of the PDF through various optimization methods.\n\nThe higher the compression level, the smaller the file becomes - with possible quality loss in images.',
        'optimize_level': 'Compression level:',
        'optimize_level_low': 'Low (fast, slight savings)',
        'optimize_level_medium': 'Medium (good compromise)',
        'optimize_level_high': 'High (strong savings)',
        'optimize_level_maximum': 'Maximum (maximum savings, slow)',
        'optimize_level_explanation': 'Recommendation: "Medium" is a good compromise between speed and file size.',
        'optimize_options': 'Options:',
        'optimize_compress_images': 'Compress images (reduce JPEG quality)',
        'optimize_clean_objects': 'Remove unused objects',
        'optimize_preserve_metadata': 'Preserve metadata (title, author, etc.)',
        'optimize_image_quality': 'Image quality:',
        'optimize_range': 'Page range:',
        'optimize_all_pages': 'All pages',
        'optimize_custom_range': 'Custom range',
        'optimize_from': 'From:',
        'optimize_to': 'To:',
        'optimize_target_folder': 'Target folder:',
        'optimize_browse': 'Browse...',
        'optimize_select_folder': 'Select target folder',
        'optimize_info_box': 'Information',
        'optimize_info_text': 'Optimization can take several minutes for large PDFs.\n\nImages are saved with reduced quality, which can significantly reduce file size.',
        'optimize_start': 'Starting PDF optimization...',
        'optimize_progress': 'Optimizing PDF...',
        'optimize_cancel': 'PDF optimization cancelled',
        'optimize_complete': 'PDF optimization completed',
        'optimize_error_format': 'Error during PDF optimization:\n\n{0}',
        'optimize_success_message': 'PDF optimization successful!\n\nSaved as:\n{0}\n\nBefore: {1}\nAfter: {2}\nSavings: {3:.1f}%\n\n{4}\n\nWould you like to open the optimized PDF?',
        'optimize_success_message_no_size': 'PDF optimization successful!\n\nSaved as:\n{0}\n\nSize information not available.\n\nWould you like to open the optimized PDF?',
        'optimize_result_positive': 'The file was reduced by {0:.1f}%.',
        'optimize_result_zero': 'No change in file size.',
        'optimize_result_negative': 'The file has increased by {0:.1f}%.\nOptimization was skipped, the original file was preserved.',
        'btn_optimize': 'Start optimization',
        'filename_optimize_low_suffix': '_optimized_low',
        'filename_optimize_medium_suffix': '_optimized',
        'filename_optimize_high_suffix': '_optimized_high',
        'filename_optimize_maximum_suffix': '_optimized_max',

        # ============================================
        # 96. ZUSCHNEIDEN CROPPING
        # ============================================
        'crop_title': 'Crop PDF',
        'crop_menu': 'Crop PDF',
        'crop_range': 'Apply to:',
        'crop_all_pages': 'All pages',
        'crop_current_page': 'Current page only',
        'crop_values': 'Crop values (in points):',
        'crop_left': 'Left:',
        'crop_right': 'Right:',
        'crop_top': 'Top:',
        'crop_bottom': 'Bottom:',
        'crop_presets': 'Presets:',
        'crop_preset_white': 'Detect white margins',
        'crop_reset': 'Reset',
        'crop_mouse_hint': '🖱️ Drag a rectangle to roughly select the area.\nThen you can adjust the values precisely in the SpinBoxes.\nManual adjustment with the mouse is not possible.',
        'crop_apply': 'Crop',
        'crop_scope_all': 'All pages',
        'crop_scope_current': 'Current page',
        'crop_new_size': 'New size: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'No PDF loaded',
        'crop_preview_error': 'Error loading preview',
        'crop_start': 'Starting crop...',
        'crop_progress': 'Cropping PDF...',
        'crop_success': 'PDF cropped successfully!\n\nSaved as:\n{0}\n\nWould you like to open the cropped PDF?',
        'crop_complete': 'Cropping completed',
        'crop_cancel': 'Cropping cancelled',
        'crop_error_format': 'Error during cropping:\n\n{0}',
        'filename_crop_suffix': '_cropped',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        'flatten_title': 'Flatten PDF',
        'flatten_menu': 'Flatten PDF',
        'flatten_info': 'Flattening a PDF "burns" all editable elements into the page content.\n\nAfterwards, form fields, annotations, texts, crosses, signatures, images and shapes are no longer individually editable.',
        'flatten_explanation_title': '📖 What is this good for?',
        'flatten_explanation_text': 'Flattening is needed in the following situations:\n\n'
            '• 📄 You want to prepare the document for printing\n'
            '• 🔒 You want to prevent someone from changing form fields\n'
            '• 📎 You want to "embed" annotations and comments permanently into the document\n'
            '• 🖼️ You want to permanently anchor inserted texts, crosses, signatures, images and shapes in the document\n'
            '• 📦 You want to prepare the file for archiving\n\n'
            'Flattening makes the PDF smaller and prevents elements from being accidentally moved or deleted.',
        'flatten_what_title': 'What is flattened?',
        'flatten_what_list': '• ✅ Form fields (text fields, checkboxes, buttons)\n'
            '• ✅ Annotations (comments, highlights, notes)\n'
            '• ✅ Overlays (texts, crosses, signatures, images, shapes)',
        'flatten_options': 'Options:',
        'flatten_forms': 'Flatten form fields',
        'flatten_annotations': 'Flatten annotations',
        'flatten_overlays': 'Flatten overlays (texts, crosses, signatures, images, shapes)',
        'flatten_target_folder': 'Target folder:',
        'flatten_browse': 'Browse...',
        'flatten_select_folder': 'Select target folder',
        'flatten_warning': '⚠️ Important: Flattening is an irreversible process!\n\nAfter flattening, editable elements can no longer be individually changed or deleted.\nCreate a backup beforehand if necessary.',
        'flatten_apply': 'Flatten',
        'flatten_start': 'Starting flattening...',
        'flatten_progress': 'Flattening PDF...',
        'flatten_success': 'PDF flattened successfully!\n\nSaved as:\n{0}\n\nWould you like to open the flattened PDF?',
        'flatten_complete': 'Flattening completed',
        'flatten_cancel': 'Flattening cancelled',
        'flatten_error_format': 'Error during flattening:\n\n{0}',
        'filename_flatten_suffix': '_flattened',

        # ============================================
        # 98. PDF ÜBEREINANDERLEGEN OVERLAY
        # ============================================
        'overlay_title': 'Overlay PDF',
        'overlay_menu': 'Overlay PDF',
        'overlay_info': 'Places one PDF (overlay) on top of another PDF.\n\nThe overlay PDF is placed on the base PDF. This is useful for watermarks, logos, letterheads or stamps.',
        'overlay_explanation_title': '📖 What is this good for?',
        'overlay_explanation_text': 'Overlaying is needed in the following situations:\n\n'
            '• 🏢 Place a company logo as a watermark on every page\n'
            '• 📄 Place a letterhead on an empty PDF\n'
            '• 🖊️ Place a stamp overlay on a document\n'
            '• 🔖 Place a watermark on all pages\n'
            '• 📑 Place a form overlay on a template',
        'overlay_type': 'Overlay type:',
        'overlay_type_fullpage': 'Full page (covering)',
        'overlay_type_transparent': 'Full page (transparent - recommended)',
        'overlay_type_stamp': 'Stamp (positionable)',
        'overlay_type_info_fullpage': '📄 The overlay PDF is placed exactly over the entire page.\nThe white background can be removed so that only the content remains visible.',
        'overlay_type_info_transparent': '🔍 The overlay PDF is placed over the entire page with transparent background.\nThe white background is automatically removed - ideal for watermarks and logos!',
        'overlay_type_info_stamp': '🖊️ The overlay PDF is positioned and scaled as a stamp.\nPerfect for logos, stamps or signatures at specific positions.',
        'overlay_remove_background': 'Remove white background:',
        'overlay_remove_background_enable': 'Remove white background from overlay PDF (makes the overlay transparent)',
        'overlay_remove_background_tooltip': 'Removes white areas from the overlay PDF so that the underlying text becomes visible.',
        'overlay_threshold': 'Threshold value:',
        'overlay_threshold_hint': '(1-254, higher = more white is removed)',
        'overlay_select_file': 'Select overlay PDF:',
        'overlay_file_placeholder': 'Please select a PDF file for the overlay',
        'overlay_browse': 'Browse...',
        'overlay_select_overlay': 'Select overlay PDF',
        'overlay_range': 'Page range:',
        'overlay_all_pages': 'All pages',
        'overlay_custom_range': 'Custom range',
        'overlay_from': 'From:',
        'overlay_to': 'To:',
        'overlay_position': 'Position:',
        'overlay_position_center': 'Center',
        'overlay_position_top_left': 'Top left',
        'overlay_position_top_right': 'Top right',
        'overlay_position_bottom_left': 'Bottom left',
        'overlay_position_bottom_right': 'Bottom right',
        'overlay_size': 'Size:',
        'overlay_size_original': 'Original size',
        'overlay_size_fit_page': 'Fit to page',
        'overlay_size_custom': 'Custom (%)',
        'overlay_opacity': 'Transparency:',
        'overlay_target_folder': 'Target folder:',
        'overlay_browse_folder': 'Browse...',
        'overlay_select_folder': 'Select target folder',
        'overlay_warning': '⚠️ Note: The overlay PDF is placed on the base PDF and "burned" into it.\n\nThe elements of the overlay PDF can no longer be edited individually after saving.',
        'overlay_apply': 'Overlay',
        'overlay_start': 'Starting overlay...',
        'overlay_progress': 'Overlaying PDF...',
        'overlay_success': 'PDF overlaid successfully!\n\nSaved as:\n{0}\n\nWould you like to open the overlaid PDF?',
        'overlay_complete': 'Overlay completed',
        'overlay_cancel': 'Overlay cancelled',
        'overlay_error_format': 'Error during overlay:\n\n{0}',
        'overlay_no_file': 'No overlay PDF selected.\n\nPlease select a PDF file to overlay.',
        'filename_overlay_suffix': '_overlaid',

        # ============================================
        # 99. ALLE BILDER EXTRAHIEREN
        # ============================================
        'extract_images_title': 'Extract images from PDF',
        'extract_images_menu': 'Extract all images',
        'extract_images_info': 'Extracts all images from the PDF and saves them as separate files.\n\nThe images are saved in their original format or converted to a selected format.',
        'extract_images_format': 'Image format:',
        'extract_images_quality': 'JPEG quality:',
        'extract_images_options': 'Options:',
        'extract_images_subfolder': 'Extract to subfolder ("PDFname_images")',
        'extract_images_unique': 'Only unique images (avoid duplicates)',
        'extract_images_range': 'Page range:',
        'extract_images_all_pages': 'All pages',
        'extract_images_custom_range': 'Custom range',
        'extract_images_from': 'From:',
        'extract_images_to': 'To:',
        'extract_images_target_folder': 'Target folder:',
        'extract_images_browse': 'Browse...',
        'extract_images_select_folder': 'Select target folder',
        'extract_images_info_box': 'Information',
        'extract_images_info_text': 'Extraction can take several minutes for large PDFs.\n\nImages are saved with their original name (page_image).',
        'extract_images_extract': 'Extract',
        'extract_images_start': 'Starting extraction...',
        'extract_images_progress': 'Extracting images...',
        'extract_images_success': '✅ Images successfully extracted!\n\n{0} images were saved in:\n{1}',
        'extract_images_complete': 'Image extraction completed',
        'extract_images_cancel': 'Extraction cancelled',
        'extract_images_error_format': 'Error extracting images:\n\n{0}',
        'extract_images_open_folder': '📁 Open folder',
        'extract_images_no_images': 'No images found in PDF.',

        # ============================================
        # 100. MEHRERE SEITEN AUF EINE SEITE
        # ============================================
        'nup_title': 'Multiple pages on one page (N-Up)',
        'nup_menu': 'Multiple pages on one page (N-Up)',
        'nup_info': 'Arranges multiple PDF pages on one page.\n\nIdeal for compact prints, overviews or handouts.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Preview:',
        'nup_preview_info': '{0} pages → {1} pages per sheet → {2} sheets\nLayout: {3}',
        'nup_order': 'Order:',
        'nup_order_horizontal': 'Horizontal (row by row)',
        'nup_order_vertical': 'Vertical (column by column)',
        'nup_order_horizontal_reverse': 'Horizontal reverse',
        'nup_order_vertical_reverse': 'Vertical reverse',
        'nup_range': 'Page range:',
        'nup_all_pages': 'All pages',
        'nup_custom_range': 'Custom range',
        'nup_from': 'From:',
        'nup_to': 'To:',
        'nup_options': 'Options:',
        'nup_margins': 'Margins:',
        'nup_margin_between': 'Spacing between pages:',
        'nup_page_numbers': 'Insert page numbers',
        'nup_target_folder': 'Target folder:',
        'nup_browse': 'Browse...',
        'nup_select_folder': 'Select target folder',
        'nup_create': 'Create',
        'nup_start': 'Starting N-Up...',
        'nup_progress': 'Creating N-Up...',
        'nup_success': 'N-Up created successfully!\n\nSaved as:\n{0}\n\nWould you like to open the new PDF?',
        'nup_complete': 'N-Up completed',
        'nup_cancel': 'N-Up cancelled',
        'nup_error_format': 'Error during N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        # ============================================
        # 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        # ============================================
        'pagesize_title': 'Change page size',
        'pagesize_menu': 'Change page size',
        'pagesize_info': 'Changes the page size of the PDF.\n\nThe content is automatically adapted to the new size.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Select a standard format:',
        'pagesize_custom': 'Custom size:',
        'pagesize_width': 'Width:',
        'pagesize_height': 'Height:',
        'pagesize_orientation': 'Orientation:',
        'pagesize_portrait': 'Portrait',
        'pagesize_landscape': 'Landscape',
        'pagesize_scale_options': 'Scaling options:',
        'pagesize_fit': 'Fit (maintain aspect ratio)',
        'pagesize_stretch': 'Stretch (distort)',
        'pagesize_center': 'Center (original size)',
        'pagesize_range': 'Page range:',
        'pagesize_all_pages': 'All pages',
        'pagesize_custom_range': 'Custom range',
        'pagesize_from': 'From:',
        'pagesize_to': 'To:',
        'pagesize_target_folder': 'Target folder:',
        'pagesize_browse': 'Browse...',
        'pagesize_select_folder': 'Select target folder',
        'pagesize_apply': 'Apply',
        'pagesize_start': 'Starting page size change...',
        'pagesize_progress': 'Changing page size...',
        'pagesize_success': 'Page size changed successfully!\n\nSaved as:\n{0}\n\nWould you like to open the new PDF?',
        'pagesize_complete': 'Page size change completed',
        'pagesize_cancel': 'Page size change cancelled',
        'pagesize_error_format': 'Error changing page size:\n\n{0}',
        'pagesize_preview_info': 'New size: {0} x {1} pt',
        'filename_pagesize_suffix': '_newsize',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF Information',
        'pdf_info_menu': 'Show PDF info',
        'pdf_info_voice': 'Displaying PDF information',
        'pdf_info_error': 'Error displaying PDF info:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Show keyboard shortcuts",
        "shortcuts_dialog_title": "Keyboard Shortcuts",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 FILE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Open PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Close PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Save as...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Protect document</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Print</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Print immediately (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Quit application</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Export as Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Export as DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Export as TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Export as images (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Extract images</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOCUMENT PROCESSING</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Multiple pages)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A conversion (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Flatten PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Overlay PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optimize PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDIT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Search</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Add bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Manage bookmarks</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Next bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Previous bookmark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Run OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 PAGE MANAGEMENT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rotate current page</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Rotate all pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Normalize current page</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Normalize all pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Delete pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Extract pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Insert pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Move pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Merge PDFs</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Change page size</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 INSERT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Insert text</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Insert cross</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Insert signature 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Insert signature 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Insert image</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Insert rectangle</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Insert ellipse</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Insert line</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Insert arrow</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Insert page numbers</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Text watermark</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Image watermark</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ REDACTIONS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Redaction (black)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Redaction (white)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Apply all redactions</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ADVANCED</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Crop PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Edit metadata</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ VIEW</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Toggle Dark/Light Mode</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Show text window</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Page width (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Two pages (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Overview (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ SETTINGS</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Password management</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR settings</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Signature settings</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Filename formatting</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Export settings</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Import settings</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Show PDF info</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Toggle speech output</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Focus menu bar</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "New version available",
        "update_available_message": "There is a new version <b>{0}</b>.\n\nVisit the release page to download the update:\n{1}",
        "update_available_voice": "New version {0} available. Please download the update from the GitHub page.",
        "update_open_release": "Open release page",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Download all translations",
        "ask_download_all_translations": """In addition to German, English and Vietnamese, there are {total_languages} other GUI languages available.\n\nShould they be provided / updated?\n\nNote:\nUnneeded languages can be deleted later manually in the directory:\n{translations_path}
        \nIf you cancel, you can download the GUI languages later via the menu 'Tools → Update translations'.""",
        "menu_update_translations": "Update translations",
        "translations_updated": "Translations updated",
        "translations_update_success": "{} translations were successfully updated ({} new, {} updated).",
        "translations_update_error": "Error updating translations",
        "translations_update_no_changes": "All translations are already up to date.",
        "translations_update_offline": "No internet connection. Translations could not be updated.",
        "translations_update_in_progress": "Translations are being updated in the background...",
        "translations_downloading": "Downloading translations...",
        "translations_path_hint": "User directory for translations",
        "translations_update_not_available_title": "Update not available",
        "translations_update_not_available_message": """Updating translations is only available in the installed version.\n\nIn development mode, translations are already up to date.""",
        "translations_update_no_internet_title": "No internet connection",
        "translations_update_no_internet_message": """Could not establish an internet connection.\n\nTranslations cannot be downloaded from GitHub.\n\nPossible solutions:
        • Check your internet connection
        • Temporarily disable any firewall
        • Try again later
        \nYou can also download the translations manually from GitHub:
        https://github.com/BinhDiez/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Update already in progress",
        "btn_retry": "Retry",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Welcome to PDF Dark View",
        "welcome_title_not_supported": "Welcome to PDF Dark View",
        "welcome_message": "Welcome to PDF Dark View!\n\nYour system language was detected as '{language}'.\nWould you like to use this language for the user interface?\n\nYou can change the language at any time via 'Settings → Language'.",
        "welcome_message_language_not_available": "Welcome to PDF Dark View!\n\nYour system language was detected as '{language}'.\nThis language is not yet installed.\n\nWould you like to download the translations for {language} now from GitHub?\n\n(The language will then be automatically used for the user interface.)",
        "welcome_message_language_not_supported": "Welcome to PDF Dark View!\n\nYour system language was detected as '{language}'.\nUnfortunately, there are no translations for this language yet.\n\nThe user interface will be displayed in {fallback_language}.\n\nYou can change the language at any time via 'Settings → Language'.\nIf you like, you can also contribute a translation for your language:\nhttps://github.com/BinhDiez/PDFDarkView",
        "welcome_use_system_language": "Yes, use system language",
        "welcome_keep_english": "No, keep English",
        "welcome_download_language": "Yes, download {language}",

        # ============================================
        # 107. RECENTLY USED PATHS
        # ============================================

        'menu_recent': 'Recently used',
        'menu_recent_dirs': 'Directories...',
        'menu_recent_files': 'Files...',
        'recent_manage': 'Manage...',
        # Recent Paths - Settings
        'recent_enable_tracking': 'Save recently used paths (privacy)',
        'recent_enable_info': 'Disable this option to not save any paths',
        'recent_tracking_disabled': 'Path tracking disabled',
        'recent_enabled': 'enabled',
        'recent_disabled': 'disabled',
        'recent_tracking_status': 'Path tracking {0}',
        # Recent Paths - Dialog
        'recent_dialog_title': 'Recently used paths',
        'recent_tab_directories': 'Directories',
        'recent_tab_files': 'Files',
        'recent_dirs_instruction': 'Double-click to open file dialog in directory',
        'recent_files_instruction': 'Double-click to open PDF directly',
        'recent_no_directories': '(no directories saved)',
        'recent_no_files': '(no files saved)',
        'recent_default_current': '⭐ Default: {0}',
        'recent_set_as_default': '⭐ Set as default',
        'recent_default_set_title': 'Default directory set',
        'recent_default_set_message': 'The directory "{0}" has been set as the default for opening PDFs.',
        'recent_default_set_voice': 'Default directory has been set',
        'recent_directory_not_found': 'Directory not found',
        'recent_file_not_found': 'File not found',
        'recent_remove_selected': 'Remove',
        'recent_remove_title': 'Remove path',
        'recent_remove_confirm': 'Do you really want to remove the path "{0}" from the list?',
        'recent_path_removed': 'Path has been removed',
        'recent_clear_all': 'Remove all',
        'recent_clear_title': 'Remove all paths',
        'recent_clear_confirm_type': 'Do you really want to delete all {0}?',
        'recent_cleared': 'List has been cleared',
        'recent_path_not_found_title': 'Path not found',
        'recent_path_not_found_message': 'The path "{0}" no longer exists.',
        'recent_open_file': 'Open file',
        'btn_open_recent': 'Open',
        'recent_open_file_question': 'Do you want to open "{0}" as PDF?',
        'recent_not_pdf': 'The selected file is not a PDF.',
        'recent_more_entries': 'More entries...',
        'btn_remove': 'Remove',
        'btn_clear': 'Clear all',
        # Recent Paths - Context Menu
        'recent_context_open': 'Open',
        'recent_context_reveal': 'Show in Finder',
        'recent_context_set_default': '⭐ Set as default',
        'recent_context_open_terminal': '💻 Open Terminal',
        'recent_context_file_info': 'File info',
        'recent_context_open_with_default': '📄 Open with default app',
        'recent_context_remove': 'Remove from list',
        'recent_context_clear_all': 'Remove all',

        # Recent Paths - File Info
        'recent_file_info_title': 'File information',
        'recent_file_info_name': 'Name',
        'recent_file_info_path': 'Path',
        'recent_file_info_size': 'Size',
        'recent_file_info_modified': 'Modified',
        'recent_file_info_pages': 'Pages',

        # Recent Paths - Errors
        'recent_error_reveal': 'Error opening in Finder',
        'recent_error_terminal': 'Error opening Terminal',
        'recent_error_info': 'Error retrieving file info',
        'open_user_data_folder': 'Show user data directory',

        # ============================================
        # 108. DELETE EVEN/ODD PAGES
        # ============================================
        "pages_delete_even": "Delete all even pages",
        "pages_delete_odd":  "Delete all odd pages",
        "progress_even_pages": "Deleting even pages",
        "progress_odd_pages": "Deleting odd pages",
        "progress_mark_delete_even": "{} even page(s) marked for deletion",
        "progress_mark_delete_odd":  "{} odd page(s) marked for deletion",

        # ============================================
        # 109. BENUTZERNAME IN SUFFIXEN
        # ============================================
        # FilenameSettingsDialog - Username in suffixes
        "username_in_suffix": "Username in suffixes",
        "username_in_suffix_enable": "Append username to suffixes",
        "username_label": "Username:",
        "username_placeholder": "e.g. J.Doe",
        "username_hint": "The username will be appended to all suffixes (e.g. _with_Text).\nExample: Document_with_Text_J.Doe.pdf",
        "username_reset": "Reset",
        "username_reset_success": "Username reset to system username",

        # ============================================
        # 110. QUIT PROGRAM
        # ============================================
        "app_quitting": "Quitting program",

    }
