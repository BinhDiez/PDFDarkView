
# ============================================
# translations_de.py - Deutsches Wörterbuch für PDFDarkView
# Vollständig sortiert nach Kategorien
# ============================================

def load_german_strings():
    """Lädt alle deutschen Strings"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "PDF laden",
        'btn_text_window': "OCR Text",
        'btn_first': "Erste Seite",
        'btn_prev': "Seite zurück",
        'btn_next': "Seite vor",
        'btn_last': "Letzte Seite",
        'btn_print': "Drucken",
        'btn_darkmode_light': "Light Mode",
        'btn_darkmode_dark': "Dark Mode",
        'btn_delete_pages': "Seiten löschen",
        'btn_extract_pages': "Seiten entnehmen",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Abbrechen",
        'btn_save': "Speichern",
        'btn_close': "Schließen",
        'btn_delete': "Löschen",
        'btn_delete_all': "Alle löschen",
        'btn_copy': "Kopieren",
        'btn_export': "Exportieren",
        'btn_show': "PW anzeigen",
        'btn_hide': "PW verbergen",
        'btn_authenticate': "Authentifizieren",
        'btn_settings': "Einstellungen",
        'btn_protect': "Schützen",
        'btn_remove_password': "Passwort entfernen",
        'btn_manage': "Passwortverwaltung",
        'btn_retry': "Erneut versuchen",
        'btn_select_all': "Alle auswählen",
        'btn_clear_selection': "Auswahl aufheben",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Seite {0} von {1}",
        'page_count': "von {0}",
        'goto_page': "Gehe zu Seite",
        'page_simple': "Seite {0}",
        'full_view_page': "Vollansicht Seite {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Suchbegriff eingeben + Enter",
        'search_results': "Treffer: {0} von {1}",
        'search_nav_hint': "Enter: nächster  (Shift+Enter: vorheriger) Treffer",
        'search_no_results': "Keine Treffer",
        'search_error': "Suchfehler",
        'search_active': "Suchfeld aktiviert",
        'search_closed': "Suche beendet",
        'search_position': "Seite {0} {1}",
        'search_pos_top': "ganz oben",
        'search_pos_upper': "oben",
        'search_pos_middle': "Mitte",
        'search_pos_lower': "unten",
        'search_pos_bottom': "ganz unten",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Texterkennung erfolgreich abgeschlossen!",
        'ocr_success_title': "OCR erfolgreich",
        'ocr_success_message': "Das Dokument ist jetzt durchsuchbar.",
        'ocr_failed': "OCR fehlgeschlagen",
        'ocr_in_progress': "OCR in Bearbeitung",
        'ocr_preparing': "PDF wird vorbereitet...",
        'ocr_analyzing': "PDF wird analysiert...",
        'ocr_optimizing': "Bildoptimierung läuft...",
        'ocr_recognizing': "Texterkennung in Arbeit...",
        'ocr_embedding': "Text wird eingebettet...",
        'ocr_finalizing': "Finalisierung der PDF...",
        'ocr_not_available': "OCR nicht verfügbar",
        'ocr_install_message': "OCR-Tools wurden nicht gefunden.\n\nBitte installieren Sie:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "OCR erforderlich",
        'ocr_question': "Das PDF enthält keinen durchsuchbaren Text.\nMöchten Sie OCR durchführen, um {0} zu ermöglichen?",
        'ocr_perform': "OCR durchführen",
        'ocr_later': "Später",
        'ocr_starting': "Starte garantierte OCR...",
        'ocr_success_voice': "OCR erfolgreich. PDF ist jetzt durchsuchbar.",
        'ocr_partial_success': "OCR wurde durchgeführt, aber beim Ersetzen gab es Probleme.\n\nDie durchsuchbare Version wurde gespeichert unter:\n{0}\n\nFehler: {1}",
        'ocr_partial_title': "OCR teilweise erfolgreich",
        'ocr_partial_voice': "OCR durchgeführt, aber Ersetzen fehlgeschlagen.",
        'original_file': "Originaldatei:",
        'old_size': "Alte Dateigröße:    {0} Bytes",
        'new_size': "Neue Dateigröße: {0} Bytes",
        'size_change': "Änderung: {0}{1} Bytes",
        'backup_created_file': "Backup erstellt:\n{0}",
        'backup_not_created': "Backup: Nicht erstellt (Einstellung deaktiviert)",
        'page_header': "=== Seite {0} ===\n{1}\n",
        'scanned_page_header': "=== Seite {0} (gescannt) ===\n[Diese Seite enthält nur gescannten Text]\n[Bitte manuell OCR durchführen]\n",
        'scanned_warning': "⚠️ GESCANNTER TEXT - OCR ERFORDERLICH",
        'guaranteed_title': "Durchsuchbare PDF erstellt",
        'guaranteed_message': "<b>Durchsuchbare Version erstellt!</b>\n\nDa die automatische OCR fehlgeschlagen ist, wurde eine\nalternative durchsuchbare PDF erstellt:\n\n{0}\n\n<b>Diese Datei enthält:</b>\n• Extrahierten Text (falls vorhanden)\n• Hinweise für gescannte Seiten\n• Ist vollständig durchsuchbar",
        'guaranteed_voice': "Durchsuchbare PDF erstellt.",
        'instruction_title': "ANLEITUNG FÜR OCR",
        'instruction_file': "Originaldatei: {0}",
        'instruction_text': "Die automatische Texterkennung (OCR) ist fehlgeschlagen.\nBitte führen Sie OCR manuell durch:\n\n1. MIT OCRmyPDF (Kommandozeile):\n   ocrmypdf --force-ocr \"[DATEI]\" \"ausgabe.pdf\"\n\n2. MIT ADOBE ACROBAT (macOS/Windows):\n   • PDF in Acrobat öffnen\n   • Werkzeuge > PDF bearbeiten\n   • 'Texterkennung' auswählen\n\n3. MIT PREVIEW (macOS):\n   • PDF in Preview öffnen\n   • Datei > Exportieren...\n   • Quartz-Filter: 'Reduce File Size'\n   • 'OCR durchführen' aktivieren\n\n4. ONLINE OCR DIENSTE:\n   • smallpdf.com/de/ocr-pdf\n   • ilovepdf.com/de/ocr-pdf\n   • adobe.com/de/acrobat/online/pdf-to-word.html",
        'instruction_created': "OCR-Anleitung erstellt",
        'instruction_created_message': "Eine detaillierte Anleitung wurde erstellt:\n\n{0}\n\nBitte folgen Sie den Schritten für manuelle OCR.",
        'instruction_created_voice': "OCR-Anleitung erstellt.",
        'ocr_impossible': "OCR nicht möglich",
        'ocr_impossible_message': "OCR konnte nicht durchgeführt werden.\n\nBitte verarbeiten Sie '{0}' manuell mit OCR-Software.",
        'ocr_impossible_voice': "OCR nicht möglich. Bitte manuell verarbeiten.",
        'emergency_title': "Notfall-OCR",
        'emergency_message': "Eine Notfall-PDF wurde erstellt:\n\n{0}\n\nBitte verarbeiten Sie diese Datei manuell mit OCR.",
        'emergency_voice': "Notfall-PDF erstellt. Bitte manuell OCR durchführen.",
        'critical_error': "Kritischer Fehler",
        'critical_error_message': "OCR konnte nicht gestartet werden.\n\nBitte starten Sie das Programm neu und\nüberprüfen Sie die OCR-Installation.",
        'critical_error_voice': "Kritischer OCR-Fehler",
        'ocr_question_html': "<p>Das PDF enthält keinen durchsuchbaren Text.<p>Möchten Sie OCR durchführen, um <b>{0}</b> zu ermöglichen?</p>",
        'ocr_question_voice': "OCR erforderlich. Das PDF enthält keinen durchsuchbaren Text. Möchten Sie OCR durchführen, um {0} zu ermöglichen?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "kein PDF geladen",
        'no_pdf_message': "Es ist kein PDF geladen",
        'pdf_not_found': "PDF-Datei nicht gefunden",
        'file_size': "Dateigröße",
        'bytes': "Bytes",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Backup erstellt",
        'backup_disabled': "Backup deaktiviert",
        'backup_activated': "Backup Erstellung aktiviert",
        'backup_deactivated': "Backup Erstellung deaktiviert",
        'backup_status': "Backup: {0}",
        'backup_on': "✔ aktiviert",
        'backup_off': "✘ deaktiviert",
        'close_pdf': "Schließe PDF: {0}",
        'pdf_not_found_format': "PDF-Datei nicht gefunden: {0}",
        'error_pdf_load_format': "Fehler beim Laden der PDF: {0}",
        'load_failed_format': "Laden fehlgeschlagen:\n{0}",
        'decrypted_suffix': "(entschlüsselt)",
        'decryption_failed': "Entschlüsselung fehlgeschlagen.",
        'decryption_error': "Fehler beim Entschlüsseln",
        'decryption_success': "Erfolgreich entschlüsselt",
        'decryption_success_message': "PDF wurde entschlüsselt und gespeichert unter:\n\n{0}",
        'decryption_success_voice': "PDF wurde entschlüsselt und gespeichert.",
        'password_remove_error': "Fehler beim Entfernen des Passworts",
        'save_unencrypted': "Unverschlüsselte PDF speichern unter",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Speichern unter...",
        'save_copy': "Kopie speichern",
        'save_success': "PDF gespeichert unter: {0}",
        'save_encrypted': "Geschütztes PDF gespeichert unter: {0}",
        'save_error': "PDF konnte nicht gespeichert werden",
        'encryption_question': "Möchten Sie die PDF mit einem Passwort schützen?",
        'encryption_yes': "Ja",
        'encryption_no': "Nein",
        'encryption_cancel': "Abbrechen",
        'save_cancel': "Speichern abgebrochen",
        'save_encrypted_voice': "Datei verschlüsselt und gespeichert.",
        'save_success_voice': "Die PDF Datei wurde unverschlüsselt gespeichert.",
        'save_error_format': "PDF konnte nicht gespeichert werden:\n{0}",
        'export_pages_success': "Pages-Export erfolgreich",
        'export_pages_error': "Pages-Export fehlgeschlagen",
        'export_pages_error_format': "Pages-Export fehlgeschlagen: {0}",
        'export_word_success': "Word-Export erfolgreich",
        'export_word_error': "Word-Export fehlgeschlagen",
        'export_word_error_format': "Word-Export fehlgeschlagen: {0}",
        'export_text_success': "Text-Export erfolgreich",
        'export_text_error': "Text-Export fehlgeschlagen",
        'export_text_error_format': "Text-Export fehlgeschlagen: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Passwort erforderlich",
        'password_enter': "Bitte geben Sie das Passwort ein",
        'password_confirm': "Passwort bestätigen",
        'password_new': "Neues Passwort",
        'password_current': "Aktuelles Passwort",
        'password_save': "Passwort speichern (verschlüsselt)",
        'password_saved': "✓ Passwort für diese Datei ist gespeichert",
        'password_wrong': "Falsches Passwort",
        'password_mismatch': "Passwörter stimmen nicht überein",
        'password_too_short': "Passwort zu kurz",
        'password_min_length': "Das Passwort muss mindestens 4 Zeichen lang sein",
        'password_strength': "Passwortstärke",
        'password_strength_very_weak': "Sehr schwach",
        'password_strength_weak': "Schwach",
        'password_strength_medium': "Mittel",
        'password_strength_strong': "Stark",
        'password_strength_very_strong': "Sehr stark",
        'password_char_count': "({0} Zeichen)",
        'password_match': "✓ Übereinstimmung",
        'password_no_match': "✗ Passwörter stimmen nicht überein",
        'password_show': "Anzeigen",
        'password_hide': "Verbergen",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Passwortverwaltung",
        'password_table_filename': "Dateiname",
        'password_table_password': "Passwort",
        'password_count': "{0} gespeicherte Passwort{1}",
        'password_count_singular': "er",
        'password_count_plural': "er",
        'password_none': "Keine gespeicherten Passwörter",
        'password_copied': "{0} Passwort{1} kopiert",
        'password_copied_singular': "",
        'password_copied_plural': "er",
        'password_delete_confirm': "Möchten Sie das Passwort für '{0}' wirklich löschen?",
        'password_delete_multiple': "Möchten Sie die {0} ausgewählten Passwörter wirklich löschen?",
        'password_delete_all_confirm': "Möchten Sie wirklich alle {0} gespeicherten Passwörter löschen?",
        'password_deleted': "{0} Passwort{1} wurde{2} gelöscht",
        'password_deleted_singular': "",
        'password_deleted_plural': "er",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "n",
        'password_all_deleted': "Alle Passwörter wurden gelöscht",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Passwortgenerator",
        'generator_generated': "Generiertes Passwort:",
        'generator_regenerate': "Neu generieren",
        'generator_copy': "Kopieren",
        'generator_use': "Verwenden",
        'generator_settings': "Einstellungen",
        'generator_length': "Länge:",
        'generator_group_every': "Trennzeichen alle",
        'generator_group_chars': "Zeichen.    Trenner:",
        'generator_uppercase': "Großbuchstaben (A-Z)",
        'generator_lowercase': "Kleinbuchstaben (a-z)",
        'generator_digits': "Zahlen (0-9)",
        'generator_symbols': "Sonderzeichen (!@#$%^&*)",
        'generator_exclude': "Ausgeschlossen:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Master-Passwort erforderlich",
        'master_password_setup': "Master-Passwort einrichten",
        'master_password_change': "Master-Passwort ändern",
        'master_password_enter': "Bitte geben Sie Ihr Master-Passwort ein",
        'master_password_choose': "Wählen Sie ein sicheres Master-Passwort (mindestens 8 Zeichen)",
        'master_password_new': "Bitte geben Sie Ihr neues Master-Passwort ein",
        'master_password_confirm': "Passwort bestätigen",
        'master_password_authenticate': "Authentifizieren",
        'master_password_success': "Master-Passwort wurde erfolgreich eingerichtet.",
        'master_password_changed': "Master-Passwort wurde erfolgreich geändert.",
        'master_password_removed': "Master-Passwort und alle Passwörter wurden gelöscht.",
        'master_password_remove': "Master-Passwort entfernen",
        'master_password_remove_confirm': "Sind Sie SICHER, dass Sie ALLE Passwörter löschen möchten?\n\nDiese Aktion ist UNWIEDERBRINGLICH!",
        'master_password_export_before': "Möchten Sie vorher eine Sicherungskopie exportieren?",
        'master_password_export_delete': "Exportieren & löschen",
        'master_password_delete_now': "Sofort löschen",
        'master_password_for_signatures': "Um Signaturen verwenden zu können, müssen Sie ein Master-Passwort einrichten.\n\nMöchten Sie jetzt ein Master-Passwort einrichten?",
        'master_password_for_private': "Um private Textbausteine verwenden zu können, müssen Sie ein Master-Passwort einrichten.\n\nMöchten Sie jetzt ein Master-Passwort einrichten?",
        'master_password_info': """
            <b>🔐 OHNE MASTER-PASSWORT:</b><br>
            • Keine Anzeige, Kopieren und Export von Passwörtern möglich<br>
            • Löschen von Passwörtern ist immer möglich (auch ohne Master-Passwort)<br><br>

            <b>🔐 MIT MASTER-PASSWORT:</b><br>
            • Alle Funktionen verfügbar nach Authentifizierung<br>
            • Passwörter werden mit dem Master-Passwort verschlüsselt<br>
            • Mindestlänge: 8 Zeichen<br>
            • Sichere SHA-256 Hash-Speicherung<br><br>

            <b>WICHTIG:</b><br>
            • Bei Verlust des Master-Passworts: Passwörter nicht wiederherstellbar<br>
            • Beim Entfernen des Master-Passworts: ALLE Passwörter werden gelöscht<br>
            • Export-Option vor Löschung verfügbar<br>
            • Master-Passwort jederzeit änderbar
        """,
        'signature_auth_disabled': "Passwortabfrage für Signaturen deaktivieren",
        'template_auth_disabled': "Passwortabfrage für private Textbausteine deaktivieren",
        'master_password_for_signatures_settings': "Um Signaturen verwenden zu können, müssen Sie ein Master-Passwort einrichten.\n\nGehen Sie dazu in Einstellungen - Passwortverwaltung",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "PDF schützen",
        'protect_info': "Die Datei '{0}' wird mit einem Passwort geschützt.",
        'protect_instruction': "Bitte geben Sie 2 mal das gewünschte Passwort ein, um das Dokument zu schützen, oder verwenden Sie den Passwortgenerator rechts neben dem Eingabefeld.",
        'protect_success': "PDF wurde erfolgreich geschützt und gespeichert unter:\n{0}\n\nPasswort: {1}\n\nMöchten Sie das geschützte PDF jetzt öffnen?",
        'protect_open': "Ja",
        'protect_skip': "Nein",
        'protect_error': "Fehler beim Schützen der PDF",
        'protect_open_title': "geschütztes PDF öffnen",
        'protect_question': "Erledigt. Möchten Sie das geschützte PDF jetzt öffnen? Ja oder Nein?",
        'password_cancel': "Passwort-Dialog abgebrochen",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Seiten löschen",
        'pages_extract': "Seiten entnehmen",
        'pages_insert': "Seiten einfügen",
        'pages_move': "Seiten verschieben",
        'pages_delete_options': "Löschoptionen",
        'pages_delete_empty': "Alle leeren Seiten löschen",
        'pages_delete_current': "Aktuelle Seite löschen",
        'pages_delete_range': "Seitenbereich löschen",
        'pages_cannot_delete_all': "Es können nicht alle Seiten gelöscht werden",
        'pages_extract_options': "Entnahmeoptionen",
        'pages_extract_current': "Aktuelle Seite entnehmen",
        'pages_extract_range': "Seitenbereich entnehmen",
        'pages_insert_position': "Einfügeposition",
        'pages_insert_before': "Einfügen vor Seite:",
        'pages_insert_select': "PDF auswählen",
        'pages_insert_none': "Keine PDF ausgewählt",
        'pages_move_source': "Zu verschiebende Seiten",
        'pages_move_from': "Von Seite:",
        'pages_move_to': "Bis Seite:",
        'pages_move_target': "Zielposition",
        'pages_move_before': "Verschieben vor Seite:",
        'pages_move_hint': "Hinweis: Seite 1 = Anfang, {0} = Ende",
        'pages_range_invalid': "Die Startseite muss kleiner oder gleich der Endseite sein.",
        'pages_position_invalid': "Die Zielposition darf nicht innerhalb des zu verschiebenden Bereichs liegen.",
        'pages_no_pdf_selected': "Es ist keine PDF ausgewählt.",
        'pages_deleted': "Es wurden {0} Seiten gelöscht.",
        'pages_extracted': "Extrahiert: {0}\nGespeichert unter: {1}\nDateigröße: {2:.1f} KB",
        'pages_inserted': "{0} Seiten eingefügt",
        'pages_moved': "Es wurden {0} Seiten verschoben.",
        'pages_deleted_none': "Es wurden keine Seiten gelöscht.",
        'pages_delete_progress': "Seiten löschen...",
        'pages_deleted_with_backup': "Es wurden {0} Seiten gelöscht.\n\nBackup: {1}",
        'pages_deleted_voice': "Es wurde ein Backup angelegt und {0} Seiten gelöscht.",
        'info': "Hinweis",
        'error_dialog_creation': "Dialog konnte nicht erstellt werden",
        'extract_page_single': "Seite {0} extrahieren",
        'extract_page_range': "Seiten {0}-{1} extrahieren",
        'extract_success_voice': "Seiten erfolgreich extrahiert",
        'extract_error_format': "Fehler beim Extrahieren: {0}",
        'pages_inserted_voice': "Es wurden {0} Seiten eingefügt.",
        'insert_error_format': "Fehler beim Einfügen: {0}",
        'pages_move_progress': "Seiten verschieben...",
        'pages_moved_with_backup': "Es wurden {0} Seiten verschoben.\n\nBackup: {1}",
        'move_success_title': "Erfolgreich verschoben",
        'pages_moved_voice': "{0} Seiten erfolgreich verschoben",
        'mark_removed': "Markierung von Seite {0} entfernt",
        'mark_empty': "Seite {0} als leer markiert",
        'mark_export_removed': "Export-Markierung von Seite {0} entfernt",
        'mark_export': "Seite {0} für Export markiert",
        'no_empty_pages': "Keine leeren Seiten zum Löschen markiert",
        'delete_empty_confirm': "Möchten Sie alle {0} markierten leeren Seiten löschen?",
        'delete_empty_confirm_voice': "Jetzt alle {0} markierten leeren Seiten löschen? Ja oder Nein.",
        'empty_pages_deleted': "{0} leere Seiten gelöscht",
        'no_export_pages': "Keine Seiten für Export markiert",
        'overwrite_title': "Bestehende Datei überschreiben",
        'overwrite_question': "Die Datei\n\n{0}\n\nexistiert bereits.\nMöchten Sie diese überschreiben?",
        'overwrite_voice': "Bereits existierende Datei überschreiben? Ja oder Nein.",
        'page_skipped': "Seite {0} wurde übersprungen",
        'export_complete': "Export abgeschlossen.",
        'export_complete_voice': "Der Export ist abgeschlossen.",
        'no_pages_exported': "Keine Seite exportiert",
        'export_cancelled': "Export abgebrochen",
        'pages_exported': "{0} Seiten exportiert nach {1}",
        'export_page_title': "Seite exportieren",
        'page_exported': "Seite {0} exportiert nach {1}",
        'export_error': "Fehler beim Export",
        'export_marked_title': "Markierte Seiten exportieren",
        'rotate_all_title': "alle Seiten drehen",
        'rotate_all_question': "Möchten Sie alle Seiten um 90 Grad nach rechts drehen?",
        'rotate_all_voice': "Möchten Sie alle Seiten um 90 Grad nach rechts drehen? Ja oder Nein?",
        'all_pages_rotated': "Alle Seiten gedreht",
        'page_rotated': "Seite {0} gedreht",
        'rotate_error': "Seite konnte nicht gedreht werden",
        'delete_page_confirm': "Möchten Sie Seite {0} löschen?",
        'delete_page_confirm_voice': "Möchten Sie die Seite {0} wirklich löschen? Ja oder Nein.",
        'page_deleted': "Seite {0} gelöscht",
        'delete_error': "Seite konnte nicht gelöscht werden",
        'pages_deleted_voice': "{0} Seiten gelöscht",
        'pages_exported_split': "{0} Seiten wurden erfolgreich exportiert.",
        'pages_skipped': "{0} Seiten wurden übersprungen.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Seiten entnehmen (erweitert)",
        'pdf_splitter_title': "PDF Splitter & Extractor",
        'pdf_splitter_load': " PDF-Datei auswählen",
        'pdf_splitter_info': "Bitte wählen Sie eine Option für Ihr PDF-Dokument",
        'pdf_splitter_basic': "Grundlegende Operationen",
        'pdf_splitter_single': "In einzelne Seiten aufteilen",
        'pdf_splitter_range': "Seiten extrahieren:",
        'pdf_splitter_range_placeholder': "z.B. 1-3,5,7-9",
        'pdf_splitter_clean': "Bereinigungsoperationen",
        'pdf_splitter_remove_empty': "Alle leeren Seiten entfernen",
        'pdf_splitter_remove': "Seitenbereich löschen:",
        'pdf_splitter_remove_placeholder': "z.B. 2,4-6",
        'pdf_splitter_process': "PDF verarbeiten",
        'pdf_splitter_loaded': "PDF geladen. Bitte wählen Sie eine Option",
        'pdf_read_error': "PDF konnte nicht gelesen werden",
        'pages': "Seiten",
        'pages_created': "Seiten wurden erstellt",
        'range_empty': "Bitte geben Sie einen Seitenbereich ein",
        'range_invalid': "Ungültiger Seitenbereich",
        'range_created': "Neues PDF mit den ausgewählten Seiten wurde erstellt:\n{0}",
        'empty_removed': "{0} leere Seiten entfernt.\nAusgabe: {1}",
        'remove_empty': "Bitte geben Sie Seiten zum Entfernen ein",
        'remove_invalid': "Ungültige Seiten zum Entfernen",
        'remove_done': "Bereinigtes PDF erstellt:\n{0}",
        'open_folder': "Ordner öffnen",
        'show_in_finder': "Im Finder anzeigen",
        'pdf_splitter_no_pdf': "Bitte laden Sie zuerst eine PDF-Datei.",
        'process_error': "Fehler beim Verarbeiten der PDF",
        'pages_created_voice': "{0} Seiten wurden erstellt",
        'range_created_voice': "PDF mit den ausgewählten Seiten wurde erstellt",
        'empty_removed_voice': "{0} leere Seiten wurden entfernt",
        'remove_done_voice': "Bereinigtes PDF wurde erstellt",
        'pdf_splitter_split_groups': "Jede zusammenhängende Gruppe in separate Datei",
        'range_created_single': "Neue PDF erstellt:\n{0}",
        'range_created_multiple': "{0} PDF-Dateien wurden erstellt.",
        'range_created_voice_single': "Eine PDF mit den ausgewählten Seiten wurde erstellt",
        'range_created_voice_multiple': "{0} PDF-Dateien wurden erstellt",
        'empty_removed_none_left': "Keine Seiten übrig",
        'empty_removed_all_empty': "Alle Seiten wurden als leer erkannt und würden entfernt. Es wurde keine Datei erstellt.",
        'preview_single': "Vorschau: {0}",
        'preview_enter_range': "Bitte geben Sie einen Seitenbereich ein.",
        'preview_invalid_range': "Ungültiger Seitenbereich.",
        'preview_file': "Vorschau: {0}",
        'preview_files': "Vorschau: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Starte Druckvorgang",
        'print_sent': "Druckauftrag gesendet",
        'print_now': "Sofort drucken",
        'print_error': "Fehler beim Sofort-Druck",
        'print_limited': "Druckfunktion auf diesem System eingeschränkt",
        'print_error_format': "Fehler beim Sofort-Druck: {0}",
        'warning': "Hinweis",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Zu Light Mode wechseln",
        'mode_switch_to_dark': "Zu Dark Mode wechseln",
        'mode_dark_activated': "Dark Mode aktiviert",
        'mode_light_activated': "Light Mode aktiviert",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Vollansicht",
        'zoom_two_pages': "Zwei Seiten nebeneinander",
        'zoom_overview': "Übersichtsmodus",
        'zoom_cannot_during_search': "Zoom während Suche nicht möglich",
        'zoom_exit_first': "Bitte zuerst Zoom beenden",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Drag & Drop aktiviert",
        'drag_disabled': "Drag & Drop deaktiviert",
        'drag_page_grab': "Seite {0} greifen",
        'drag_page_dropped': "Seite {0} an Position {1} eingefügt",
        'drag_position_invalid': "Ungültige Position",
        'drag_same_position': "Seite {0} bleibt auf Position {0}",
        'drag_error': "Fehler beim Verschieben",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Texteingabe mit erweiterten Formatierungen und TextBausteinverwaltung",
        'text_templates': "Verfügbare Textbausteine:",
        'text_name': "Name",
        'text_preview': "Textvorschau",
        'text_enter': "Text:",
        'text_font_size': "Schriftgröße:",
        'text_formatting': "Formatierung:",
        'text_bold': "Fett",
        'text_italic': "Kursiv",
        'text_underline': "Unterstrichen",
        'text_alignment': "Ausrichtung:",
        'text_left': "Links",
        'text_center': "Zentriert",
        'text_right': "Rechts",
        'text_color': "Textfarbe:",
        'text_opacity': "Deckkraft:",
        'text_word_wrap': "Zeilenumbruch:",
        'text_auto': "Automatisch",
        'text_page_width_95': "Seitenbreite (95%)",
        'text_page_width_85': "Sehr breit (85%)",
        'text_page_width_75': "Breiter (75%)",
        'text_page_width_60': "Breit (60%)",
        'text_page_width_50': "Mittel (50%)",
        'text_page_width_30': "Schmal (30%)",
        'text_page_width_20': "schmaler (20%)",
        'text_page_width_10': "Sehr schmal (10%)",
        'text_no_wrap': "Kein Umbruch",
        'text_private': "Privater Textbaustein (erfordert Authentifizierung)",
        'text_preview_label': "Vorschau:",
        'text_preview_placeholder': "Hier wird eine Vorschau des Textes angezeigt...",
        'text_no_text': "(Kein Text)",
        'text_save_template': "Als Baustein speichern",
        'text_delete_template': "Ausgewählten Textbaustein löschen",
        'text_show_private': "Private anzeigen",
        'text_hide_private': "Private ausblenden",
        'text_use': "Text verwenden",
        'text_saved': "Textbaustein gespeichert als:\n{0}",
        'text_saved_voice': "Textbaustein gespeichert",
        'text_deleted': "Textbaustein gelöscht",
        'text_no_text_to_save': "Kein Text zum Speichern.",
        'text_no_templates': "Keine Textbausteine gefunden",
        'text_private_master_required': "Private Bausteine können nur verwendet werden, wenn ein Master-Passwort eingerichtet ist.\n\nMöchten Sie jetzt ein Master-Passwort einrichten?",
        'text_filename': "Dateiname für Textbaustein (ohne 'Text_' und '.txt'):",
        'text_filename_hint': "Beispiel: 'Telefon HomeOffice' wird gespeichert als 'Text_Telefon HomeOffice.txt'",
        'text_save_hint': "Der Textbaustein wird automatisch mit Formatierung gespeichert.",
        'text_guide_title': "Texteingabe - Anleitung",
        'text_delete_confirm': "Möchten Sie den Textbaustein wirklich löschen?\n\nDatei: {0}\nText: {1}...",
        'text_make_public': "Als öffentlich markieren",
        'text_make_private': "Als privat markieren",
        'text_privacy_changed': "Privatstatus geändert",
        'text_private_always': "Private immer sichtbar (Einstellung)",
        'text_mode_required': "Bitte zuerst Text-Modus aktivieren",
        'text_continue_editing': "Weiter bearbeiten - Cursor am Textende",
        'text_no_input': "Kein Text eingegeben - Text verworfen",
        'save_dialog_question': "Wie möchten Sie fortfahren?",
        'text_save_question': "Alle Texte und Kreuze speichern, anpassen, weiter bearbeiten oder verwerfen?",
        'copy_cross': "Kreuz kopiert",
        'paste_cross': "Kreuz eingefügt",
        'paste_text': "Text eingefügt",
        'cross_discarded': "Kreuz verworfen",
        'all_discarded': "Alles verworfen",
        'text_discarded': "Text verworfen",
        'no_texts_to_save': "Keine Texte zum Speichern",
        'no_valid_texts': "Keine gültigen Texte zum Speichern",
        'text_word_singular': "Text",
        'text_word_plural': "Texte",
        'cross_word_singular': "Kreuz",
        'cross_word_plural': "Kreuze",
        'texts_saved_title': "Texte gespeichert",
        'texts_crosses_saved': "{0} {1} und {2} {3} wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'texts_crosses_saved_voice': "{0} {1} und {2} {3} gespeichert.",
        'texts_saved': "{0} {1} wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'texts_saved_voice': "{0} {1} gespeichert.",
        'crosses_saved': "{0} {1} wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'crosses_saved_voice': "{0} {1} gespeichert.",
        'elements_saved': "{0} Elemente wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'elements_saved_voice': "{0} Elemente gespeichert.",
        'text_window_load_error': "Textfenster konnte nicht geladen werden",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Texteingabe und Textbausteine – Ausführliche Anleitung**

        **1. Text einfügen und bearbeiten**
        - Klicken Sie mit der rechten Maustaste an die gewünschte Stelle im Dokument und wählen Sie "Text einfügen".
        - Es öffnet sich ein Dialog, in dem Sie Ihren Text eingeben und formatieren können:
        • Schriftgröße, Fett, Kursiv, Unterstreichen
        • Textfarbe (frei wählbar)
        • Transparenz (Deckkraft) über Schieberegler
        • Zeilenumbruch (verschiedene Breiten, z.B. Seitenbreite, schmal, kein Umbruch)
        - Nach Bestätigung erscheint der Text an der Klickposition. Sie können ihn mit der Maus oder den Pfeiltasten verschieben.
        - Doppelklick auf den Text öffnet den Bearbeitungsmodus; mit ESC verlassen Sie ihn wieder.

        **2. Textbausteine (Templates) verwalten**
        - Im Text-Dialog sehen Sie links eine Liste aller gespeicherten Textbausteine.
        - **Speichern eines Bausteins:** Geben Sie Ihren Text ein, formatieren Sie ihn und klicken Sie auf "💾 Als Baustein speichern". Geben Sie einen Dateinamen ein (ohne Endung).
        - **Laden eines Bausteins:** Klicken Sie in der Liste auf den gewünschten Namen. Der Text und die Formatierung werden übernommen und können bei Bedarf noch angepasst werden.
        - **Löschen:** Mit Rechtsklick auf einen Baustein können Sie ihn löschen oder seinen Privatstatus ändern.

        **3. Private Textbausteine (Master-Passwort)**
        - Wenn Sie ein Master-Passwort eingerichtet haben (unter Einstellungen → Passwortverwaltung), können Sie Bausteine als "privat" markieren.
        - Aktivieren Sie dazu die Checkbox "Privater Textbaustein" im Dialog bevor Sie speichern.
        - Private Bausteine werden in der Liste nur angezeigt, wenn Sie einmal pro Sitzung Ihr Master-Passwort eingegeben haben (Authentifizierung über das Schlosssymbol oder beim ersten Zugriff).
        - So können Sie vertrauliche Textbausteine vor fremdem Zugriff schützen.

        **4. Kreuze einfügen**
        - Über das Kontextmenü können Sie auch ein grafisches Kreuz (z.B. für Kontrollkästchen) einfügen.
        - Die Größe, Linienstärke und Farbe von Kreuzen können Sie global in den Einstellungen anpassen (Menü "Einstellungen" → "Ankreuzen-Einstellungen").
        - Mit Rechtsklick auf ein bestehendes Kreuz können Sie es individuell verändern.

        **5. Sammelaktionen**
        - Wenn Sie mehrere Texte oder Kreuze auf einer Seite platziert haben, können Sie über das Kontextmenü (Rechtsklick im Textmodus) alle Elemente gemeinsam speichern oder verwerfen.
        - Beim Speichern werden alle Elemente in das PDF eingebettet und bleiben als Vektorgrafiken erhalten.

        **6. Tastaturkürzel im Textmodus**
        - Pfeiltasten: Element verschieben
        - Strg+Pfeiltasten: größere Schritte
        - Enter: Speicherdialog öffnen (alle speichern / anpassen / verwerfen)
        - ESC: aktuelles Element verwerfen
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Texteingabe und Textbausteine – Ausführliche Anleitung</strong></p>

        <p><strong>1. Text einfügen und bearbeiten</strong></p>
        <ul>
        <li>Klicken Sie mit der rechten Maustaste an die gewünschte Stelle im Dokument und wählen Sie "Text einfügen".</li>
        <li>Es öffnet sich ein Dialog, in dem Sie Ihren Text eingeben und formatieren können:<br/>
        • Schriftgröße, Fett, Kursiv, Unterstreichen<br/>
        • Textfarbe (frei wählbar)<br/>
        • Transparenz (Deckkraft) über Schieberegler<br/>
        • Zeilenumbruch (verschiedene Breiten, z.B. Seitenbreite, schmal, kein Umbruch)</li>
        <li>Nach Bestätigung erscheint der Text an der Klickposition. Sie können ihn mit der Maus oder den Pfeiltasten verschieben.</li>
        <li>Doppelklick auf den Text öffnet den Bearbeitungsmodus; mit ESC verlassen Sie ihn wieder.</li>
        </ul>

        <p><strong>2. Textbausteine (Templates) verwalten</strong></p>
        <ul>
        <li>Im Text-Dialog sehen Sie links eine Liste aller gespeicherten Textbausteine.</li>
        <li><strong>Speichern eines Bausteins:</strong> Geben Sie Ihren Text ein, formatieren Sie ihn und klicken Sie auf "💾 Als Baustein speichern". Geben Sie einen Dateinamen ein (ohne Endung).</li>
        <li><strong>Laden eines Bausteins:</strong> Klicken Sie in der Liste auf den gewünschten Namen. Der Text und die Formatierung werden übernommen und können bei Bedarf noch angepasst werden.</li>
        <li><strong>Löschen:</strong> Mit Rechtsklick auf einen Baustein können Sie ihn löschen oder seinen Privatstatus ändern.</li>
        </ul>

        <p><strong>3. Private Textbausteine (Master-Passwort)</strong></p>
        <ul>
        <li>Wenn Sie ein Master-Passwort eingerichtet haben (unter Einstellungen → Passwortverwaltung), können Sie Bausteine als "privat" markieren.</li>
        <li>Aktivieren Sie dazu die Checkbox "Privater Textbaustein" im Dialog bevor Sie speichern.</li>
        <li>Private Bausteine werden in der Liste nur angezeigt, wenn Sie einmal pro Sitzung Ihr Master-Passwort eingegeben haben (Authentifizierung über das Schlosssymbol oder beim ersten Zugriff).</li>
        <li>So können Sie vertrauliche Textbausteine vor fremdem Zugriff schützen.</li>
        </ul>

        <p><strong>4. Kreuze einfügen</strong></p>
        <ul>
        <li>Über das Kontextmenü können Sie auch ein grafisches Kreuz (z.B. für Kontrollkästchen) einfügen.</li>
        <li>Die Größe, Linienstärke und Farbe von Kreuzen können Sie global in den Einstellungen anpassen (Menü "Einstellungen" → "Ankreuzen-Einstellungen").</li>
        <li>Mit Rechtsklick auf ein bestehendes Kreuz können Sie es individuell verändern.</li>
        </ul>

        <p><strong>5. Sammelaktionen</strong></p>
        <ul>
        <li>Wenn Sie mehrere Texte oder Kreuze auf einer Seite platziert haben, können Sie über das Kontextmenü (Rechtsklick im Textmodus) alle Elemente gemeinsam speichern oder verwerfen.</li>
        <li>Beim Speichern werden alle Elemente in das PDF eingebettet und bleiben als Vektorgrafiken erhalten.</li>
        </ul>

        <p><strong>6. Tastaturkürzel im Textmodus</strong></p>
        <ul>
        <li>Pfeiltasten: Element verschieben</li>
        <li>Strg+Pfeiltasten: größere Schritte</li>
        <li>Enter: Speicherdialog öffnen (alle speichern / anpassen / verwerfen)</li>
        <li>ESC: aktuelles Element verwerfen</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Ankreuzen-Einstellungen",
        'cross_properties': "Kreuz-Eigenschaften",
        'cross_size': "Größe (px):",
        'cross_line_width': "Linienstärke:",
        'cross_color': "Farbe:",
        'cross_choose_color': "Wählen",
        'cross_fine_tuning': "Feinjustierung beim Speichern (Pixel)",
        'cross_offset_x': "X-Offset:",
        'cross_offset_y': "Y-Offset:",
        'cross_offset_x_tooltip': "Negative Werte verschieben das Kreuz beim Speichern nach links, positive nach rechts",
        'cross_offset_y_tooltip': "Negative Werte verschieben das Kreuz beim Speichern nach oben, positive nach unten",
        'cross_preview': "Vorschau",
        'cross_save': "Einstellungen übernehmen",
        'cross_customized': "Kreuz angepasst",
        'cross_settings_applied': "Kreuze-Einstellungen gespeichert.\nGröße: {0}px, Linienstärke: {1}px\n{2}",
        'cross_updated_count': "{0} vorhandene Kreuze wurden aktualisiert.",
        'cross_no_crosses': "Keine vorhandenen Kreuze gefunden.",
        'cross_settings_applied_all': "Kreuzeinstellungen für alle {0} Kreuze übernommen",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Signatur-Einstellungen",
        'signature_1': "Signatur 1",
        'signature_2': "Signatur 2",
        'signature_select': "Signatur auswählen",
        'signature_add': "Neue Unterschrift hinzufügen...",
        'signature_size': "Größe für Signatur {0} (%):",
        'signature_common': "Allgemeine Einstellungen",
        'signature_timestamp': "Zeitstempel automatisch hinzufügen",
        'signature_location': "Standard-Ort:",
        'signature_timestamp_size': "Zeitstempel Schriftgröße:",
        'signature_no_files': "-- Keine Unterschriften gefunden --",
        'signature_insert': "Unterschrift einfügen",
        'signature_insert_1': "Signatur 1 einfügen",
        'signature_insert_2': "Signatur 2 einfügen",
        'signature_customize': " Signatur anpassen",
        'signature_discard': " Diese Signatur verwerfen",
        'signature_save_all': " Alle Signaturen speichern",
        'signature_discard_all': " Alle Signaturen verwerfen",
        'signature_guide_title': "Unterschriften - Anleitung",
        'signature_guide': """
📝 Unterschriften - Kurzanleitung

- Master Passwort einrichten
- Unterschriften im Menü Einstellungen konfigurieren
  (Größe, Zeitstempel ...)
- Einfügen mit RECHTSKLICK an der gewünschten Position
  (Master Passwort einmalig pro Sitzung erforderlich)
- Signatur mit der Maus oder Pfeiltasten verschieben
- Mehrere Signaturen können nacheinander eingefügt werden
- Jede Signatur kann individuell angepasst werden
- Einzelne Signatur verwerfen
- Alle Signaturen auf einmal speichern / verwerfen
- Alternativ kann auch die Menüleiste genutzt werden.
        """,
        'signature_placeholder': "Keine Vorschau verfügbar",
        'signature_info': "Signatur {0}: {1}×{2} px ({3}% von {4}×{5})",
        'signature_info_placeholder': "Einstellungen für Signatur {0}",
        'signature_inserted': "Signatur {0} auf Seite {1} eingefügt",
        'signature_deleted': "Signatur gelöscht",
        'signature_copied': "Signatur kopiert",
        'signature_pasted': "Signatur {0} eingefügt",
        'signature_saved': "{0} Signaturen wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'signature_saved_voice': "{0} Signaturen gespeichert",
        'mode_replace_signature_format': "Modus beenden und Signatur {0} einfügen",
        'mode_conflict_voice_signature': "{0} Modus ist aktiv. Beenden und Signatur einfügen?",
        'signature_not_configured': "Signatur {0} nicht konfiguriert",
        'signature_file_not_found': "Signatur Datei nicht gefunden",
        'timestamp_format': "{0}, den {1}",
        'no_copied_signature': "Keine kopierte Signatur vorhanden",
        'no_signatures_to_save': "Keine Signaturen zum Speichern",
        'signature_save_question': "Alle Signaturen speichern, anpassen oder diese verwerfen?",
        'signatures_saved_title': "Signaturen gespeichert",
        'signatures_saved': "{0} Signaturen wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'signatures_saved_voice': "{0} Signaturen gespeichert.",
        'all_signatures_discarded': "Alle Signaturen verworfen",
        'signature_settings_saved': "Signatur-Einstellungen gespeichert",
        'signature_cancelled': "Signatur verworfen",
        'signature_active_title': "Signatur aktiv",
        'signature_replace_question': "Es ist bereits eine Signatur aktiv.\n\nMöchten Sie die aktuelle Signatur ersetzen?",
        'signature_replace': "Unterschrift ersetzen",
        'signature_replace_voice': "Aktuelle Signatur ersetzen oder abbrechen?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Bildeinstellungen",
        'image_common': "Allgemeine Bildeinstellungen",
        'image_keep_aspect': "Seitenverhältnis beim Ziehen beibehalten",
        'image_default_size': "Standardgröße (%):",
        'image_dark_invert': "Bilder im Dark Mode invertieren",
        'image_dark_invert_tooltip': "Aktiviert: Bilder werden für bessere Sichtbarkeit invertiert",
        'image_fine_tuning': "Feinjustierung (Pixel)",
        'image_offset_x': "X-Offset:",
        'image_offset_y': "Y-Offset:",
        'image_offset_x_tooltip': "Negative Werte verschieben das Bild beim Speichern nach links, positive nach rechts",
        'image_offset_y_tooltip': "Negative Werte verschieben das Bild beim Speichern nach oben, positive nach unten",
        'image_select': "Bild auswählen",
        'image_insert': "Bild einfügen",
        'image_customize': " Bild anpassen",
        'image_aspect': " Seitenverhältnis beibehalten",
        'image_discard': " Dieses Bild verwerfen",
        'image_save_all': " Alle Bilder speichern",
        'image_discard_all': " Alle Bilder verwerfen",
        'image_filter': "Bilder",
        'image_guide_title': "Bilder einfügen - Anleitung",
        'image_guide': """
📷 Bilder in PDF einfügen - Kurzanleitung:

1. Rechtsklick auf die gewünschte Position
2. "Bild einfügen" → Bild auswählen
3. Bild positionieren: Ziehen mit der Maus
4. Größe anpassen: Ziehen an den Ecken/Kanten
5. Seitenverhältnis beibehalten: [A] Taste
6. Weitere Anpassungen: Rechtsklick auf Bild

Tipp: Im Kontextmenü können Sie die Einstellungen anpassen.
        """,
        'image_inserted': "Bild {0} auf Seite {1} eingefügt",
        'image_deleted': "Bild verworfen",
        'image_copied': "Bild kopiert",
        'image_pasted': "Bild eingefügt",
        'image_saved': "{0} Bilder wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'image_saved_voice': "{0} Bilder gespeichert",
        'image_aspect_on': "aktiviert",
        'image_aspect_off': "deaktiviert",
        'image_aspect_toggle': "Seitenverhältnis beibehalten {0}",
        'image_reset': "Bild auf Originalgröße zurückgesetzt",
        'image_replaced': "Bild ersetzt",
        'image_invalid': "Kein gültiges Bild",
        'mode_replace_image': "Bild einfügen",
        'mode_conflict_voice_image': "{0} Modus ist aktiv. Beenden und Bild einfügen?",
        'image_active_title': "Bild aktiv",
        'image_replace_question': "Es ist bereits ein Bild aktiv.\n\nMöchten Sie das aktuelle Bild ersetzen?",
        'image_replace': "Bild ersetzen",
        'image_replace_voice': "Aktuelles Bild ersetzen oder abbrechen?",
        'image_filter_all': "Bilder (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Alle Dateien (*.*)",
        'no_copied_image': "Kein kopiertes Bild vorhanden",
        'image_discarded': "Bild verworfen",
        'image_save_question': "Alle Bilder speichern, anpassen oder dieses verwerfen?",
        'no_images_to_save': "Keine Bilder zum Speichern",
        'no_valid_images': "Keine gültigen Bilder zum Speichern",
        'images_saved_title': "Bilder gespeichert",
        'images_saved': "{0} Bilder wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'images_saved_voice': "{0} Bilder gespeichert.",
        'all_images_discarded': "Alle Bilder verworfen",
        'image_settings_updated': "Bildeinstellungen aktualisiert",
        'image_replace_title': "Neues Bild auswählen",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Formen Einstellungen",
        'form_basic': "Grundlegende Einstellungen",
        'form_default_type': "Standard-Formtyp:",
        'form_rectangle': "Rechteck",
        'form_ellipse': "Ellipse",
        'form_line': "Linie",
        'form_arrow': "Pfeil",
        'form_line_width': "Linienstärke:",
        'form_colors': "Farben",
        'form_line_color': "Linienfarbe:",
        'form_fill_color': "Füllfarbe:",
        'form_choose_color': "Wählen",
        'form_transparent': "Transparenter Hintergrund (nur Linie)",
        'form_filled': "gefüllt",
        'form_dark_mode': "Dark Mode",
        'form_dark_invert': "Farben im Dark Mode invertieren",
        'form_fine_tuning': "Feinjustierung (Pixel)",
        'form_offset_x': "X-Offset:",
        'form_offset_y': "Y-Offset:",
        'form_offset_x_tooltip': "Negative Werte verschieben die Form beim Speichern nach links, positive nach rechts",
        'form_offset_y_tooltip': "Negative Werte verschieben die Form beim Speichern nach oben, positive nach unten",
        'form_preview': "Vorschau",
        'form_insert': "Form einfügen",
        'form_rectangle_insert': "Rechteck",
        'form_ellipse_insert': "Kreis / Ellipse",
        'form_line_insert': "Linie (2 Klicks)",
        'form_arrow_insert': "Pfeil (2 Klicks)",
        'form_customize': " Form anpassen",
        'form_transparent_toggle': " Transparenter Hintergrund",
        'form_discard': " Diese Form verwerfen",
        'form_save_all': " Alle Formen speichern",
        'form_discard_all': " Alle Formen verwerfen",
        'form_guide_title': "Formen einfügen - Anleitung",
        'form_guide': """
📐 Formen in PDF einfügen - Kurzanleitung:

1. Form-Typ auswählen (Rechteck, Kreis/Ellipse, Linie, Pfeil)
2. Auf Position klicken
   - Bei Rechteck/Ellipse: Ein Klick platziert die Form
   - Bei Linie/Pfeil: Zwei Klicks für Start- und Endpunkt
3. Form positionieren: Ziehen mit der Maus
4. Größe anpassen: Ziehen an den Ecken/Kanten
5. Form speichern: Enter
6. Form verwerfen: ESC
7. Weitere Anpassungen: Rechtsklick auf Form

Tipp: Im Kontextmenü können Sie die Einstellungen anpassen.
        """,
        'form_inserted': "{0} auf Seite {1} eingefügt",
        'form_deleted': "Form gelöscht",
        'form_copied': "Form kopiert",
        'form_pasted': "Form eingefügt",
        'form_saved': "{0} Formen wurden in das PDF eingefügt.\n\nPDF wurde neu geladen...",
        'form_saved_voice': "{0} Formen gespeichert",
        'form_reset': "Form auf Standardgröße zurückgesetzt",
        'form_transparent_on': "aktiviert",
        'form_transparent_off': "deaktiviert",
        'form_transparent_toggled': "Transparenter Hintergrund {0}",
        'form_line_cancel': "Linien-Zeichnen abgebrochen",
        'form_second_click': "Jetzt Endpunkt für {0} klicken",
        'mode_replace_form': "Form einfügen",
        'mode_conflict_voice_form': "{0} Modus ist aktiv. Beenden und eine Form einfügen?",
        'form_settings_updated': "Formen-Einstellungen aktualisiert",
        'form_unknown': "Form",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Klicken Sie auf die Startposition",
        'form_line_guide_2': "2. Klicken Sie auf die Endposition",
        'form_line_guide_3': "Die Linie wird zwischen beiden Punkten gezeichnet.",
        'form_line_status_1': "Warte auf ersten Klick...",
        'form_line_status_2': "Erster Punkt gesetzt: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Jetzt Endpunkt klicken...",
        'form_line_status_4': "Beide Punkte gesetzt.\nKlicken Sie auf 'Fertig' um zu speichern.",
        'form_line_reset': "Zurücksetzen",
        'form_line_finish': "Fertig",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopieren (Cmd+C)",
        'paste': "Einfügen (Cmd+V)",
        'copied': "Kopiert: {0}",
        'no_element_to_copy': "Kein Element zum Kopieren ausgewählt",
        'no_copied_data': "Keine kopierten Daten vorhanden",
        'no_valid_position': "Keine gültige Position zum Einfügen",
        'copy_text': "Text kopiert",
        'copy_image': "Bild kopiert",
        'copy_form': "Form kopiert",
        'copy_signature': "Signatur kopiert",
        'element_text': "Text",
        'element_image': "Bild",
        'element_form': "Form",
        'element_signature': "Signatur",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Modus-Konflikt",
        'mode_conflict_message': "Es ist bereits der Modus '{0}' aktiv.\n\nMöchten Sie diesen beenden und {1}?",
        'mode_replace': "Modus beenden und {0}",
        'mode_cancel': "Abbrechen",
        'mode_replace_text': "Text einfügen",
        'mode_replace_cross': "Kreuz einfügen",
        'mode_replace_signature': "Signatur einfügen",
        'mode_replace_image': "Bild einfügen",
        'mode_replace_form': "Form einfügen",
        'mode_conflict_voice': "{0} Modus ist aktiv. Beenden und Text einfügen?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Texteingabe",
        'active_mode_signature': "Signatur",
        'active_mode_image': "Bild",
        'active_mode_form': "Form",
        'active_mode_and': " und ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Einfügen",                    # Hauptmenü
        'insert_another_text': "Text einfügen",          # Vereinfacht
        'insert_another_cross': "Kreuz einfügen",        # Vereinfacht
        'insert_another_signature_1': "Signatur 1",      # Untermenü-Eintrag
        'insert_another_signature_2': "Signatur 2",      # Untermenü-Eintrag
        'insert_another_image': "Bild einfügen",         # Vereinfacht
        'insert_another_form_rect': "Rechteck",          # Untermenü-Eintrag
        'insert_another_form_ellipse': "Kreis / Ellipse",        # Untermenü-Eintrag
        'insert_another_form_line': "Linie (2 Klicks)",  # Untermenü-Eintrag
        'insert_another_form_arrow': "Pfeil (2 Klicks)", # Untermenü-Eintrag

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "{0} speichern",
        'save_dialog_message': "{0} wird auf Seite {1} gespeichert.\n\nWie möchten Sie fortfahren?",
        'save_all': "Alle {0} speichern",
        'save_single': "{0} speichern",
        'save_customize': "{0} anpassen",
        'save_discard': "Diese {0} verwerfen",
        'save_continue': "Weiter bearbeiten",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Zu Seite {0} springen",
        'context_rotate': " Seite {0} drehen",
        'context_delete': " Seite {0} löschen",
        'context_export': " Seite {0} exportieren",
        'context_mark_as': " Seite markieren als...",
        'context_mark_empty': " Leere Seite",
        'context_unmark_empty': " Nicht mehr leer",
        'context_mark_export': " Für Export markieren",
        'context_unmark_export': " Nicht mehr exportieren",
        'context_batch_actions': " Sammelaktionen",
        'context_batch_delete_empty': " Alle {0} leeren Seiten löschen",
        'context_batch_export_single': " Alle {0} Seiten (eine Datei)",
        'context_batch_export_split': " Alle {0} Seiten (getrennt)",
        'context_drag_start': " Drag & Drop starten",
        'context_drag_stop': " Drag & Drop beenden",
        'context_insert': " Einfügen",
        'context_insert_pages': " Seiten einfügen",
        'context_zoom': "Zoom",
        'discard_mixed': "Alle {0} {1} und {2} {3} verwerfen",
        'save_mixed': "{0} {1} und {2} {3} speichern",
        'discard_texts': "Alle {0} Texte verwerfen",
        'discard_text_single': "1 Text verwerfen",
        'save_texts': "{0} Texte speichern",
        'save_text_single': "1 Text speichern",
        'discard_crosses': "Alle {0} Kreuze verwerfen",
        'discard_cross_single': "1 Kreuz verwerfen",
        'save_crosses': "{0} Kreuze speichern",
        'save_cross_single': "1 Kreuz speichern",
        'discard_signatures': "Alle {0} Signaturen verwerfen",
        'save_signature_single': "1 Signatur speichern",
        'save_signatures': "{0} Signaturen speichern",
        'discard_images': "Alle {0} Bilder verwerfen",
        'save_image_single': "1 Bild speichern",
        'save_images': "{0} Bilder speichern",
        'discard_forms': "Alle {0} Formen verwerfen",
        'save_form_single': "1 Form speichern",
        'save_forms': "{0} Formen speichern",
        'cross_discard': "Dieses Kreuz verwerfen",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Export / Import Information",
        'export_what': "📋 Was wird exportiert?",
        'export_general': "Allgemeine Einstellungen",
        'export_general_items': "• Sprachausgabe (ein/aus, Geschwindigkeit)\n• Dark/Light Mode\n• Backup-Einstellungen\n• OCR-Einstellungen",
        'export_image_form': "Bild- und Formen-Einstellungen",
        'export_image_form_items': "• Bildeinstellungen (Seitenverhältnis, Standardgröße)\n• Formen-Einstellungen (Linienstärke, Farben)\n• Signatur-Einstellungen (Pfade, Größen, Zeitstempel)",
        'export_passwords': "Passwort-Datenbank",
        'export_passwords_items': "• Alle gespeicherten PDF-Passwörter\n• Wahlweise verschlüsselt oder entschlüsselt",
        'export_master': "Master-Passwort-Einstellungen",
        'export_master_items': "• Master-Passwort-Hash\n• Einstellungen für Signaturen/Textbausteine",
        'export_signatures': "Signaturen und Textbausteine",
        'export_signatures_items': "• Alle Bild-Dateien (Unterschriften)\n• Alle Textbausteine mit Formatierungen\n• Private/öffentliche Markierungen",
        'export_import_warning': "⚠️ Wichtige Hinweise",
        'export_import_note': "• Beim Import werden ALLE aktuellen Einstellungen überschrieben\n• Ein Neustart der Anwendung ist erforderlich\n• Vorhandene Signaturen/Textbausteine werden ersetzt",
        'export_master_note': "• Bei gesetztem Master-Passwort können Sie wählen:\n  - Entschlüsselt (Passwörter im Klartext)\n  - Verschlüsselt (nur mit Master-PW lesbar)",
        'export_security': "• Die exportierte ZIP-Datei enthält vertrauliche Daten\n• Bitte sicher aufbewahren (z.B. verschlüsselter USB-Stick)\n• Bei Verlust der Datei: Passwörter unwiederbringlich verloren",
        'export_format': "📁 Exportformat",
        'export_format_desc': "Die Einstellungen werden in einer einzigen ZIP-Datei gespeichert:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Einstellungen wurden erfolgreich exportiert",
        'export_failed': "Export fehlgeschlagen",
        'export_import_question': "Möchten Sie die Anwendung jetzt neu starten?",
        'export_password_question': "Es ist ein Master-Passwort gesetzt.\n\nMöchten Sie die Passwörter entschlüsselt exportieren?\n(ansonsten werden sie verschlüsselt exportiert)",
        'export_decrypt': "Entschlüsselt exportieren",
        'export_encrypt': "Verschlüsselt exportieren",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Info",
        'info_title': "Über PDF Dark View",
        'info_version': "Version",
        'info_author': "Entwickelt von Toralf Schulz (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "Über",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> ist ein barrierefreier PDF-Viewer, der speziell für Menschen mit Sehbehinderung entwickelt wurde.</p>

            <p><strong>Kernmerkmale:</strong></p>
            <ul>
                <li>Kontrastreiche, anpassbare Oberfläche</li>
                <li>Vollständige Tastatursteuerung</li>
                <li>Integrierte Sprachausgabe</li>
                <li>OCR für gescannte Dokumente</li>
                <li>Umfangreiche Bearbeitungswerkzeuge</li>
            </ul>

            <p>Mehr als 60 Sprachen werden bisher unterstützt – damit PDFs für alle zugänglich sind.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funktionen",
        'info_features_intro': "PDF Dark View bietet Ihnen folgende Möglichkeiten:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Anzeige & Navigation</strong> – Dark/Light Mode, Seiten blättern, Zoom, Sprung zu Seite, Lesezeichen</li>
            <li><strong>OCR (Texterkennung)</strong> – Gescannte Dokumente durchsuch- und kopierbar machen</li>
            <li><strong>Bearbeitung</strong> – Texte, Kreuze, Signaturen, Bilder und Formen einfügen</li>
            <li><strong>Seitenverwaltung</strong> – Löschen, drehen, extrahieren, einfügen, verschieben per Drag & Drop</li>
            <li><strong>PDF`s zusammenführen</li>
            <li><strong>Export</strong> – Nach Word, Pages oder als Text</li>
            <li><strong>Sicherheit</strong> – Passwortschutz und -verwaltung</li>
            <li><strong>Metadaten</strong> – Bearbeiten</li>
            <li><strong>Dateinamen</strong> – Zentrale Einstellung für Backup und Dateinamen bei Änderungen</li>
            <li><strong>Barrierefreiheit</strong> – Sprachausgabe, Tastatursteuerung, hoher Kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Bedienung",
        'info_accessibility': "♿ Barrierefreiheit – vollständige Tastatursteuerung",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Allgemein</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> PDF öffnen</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Suchen</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Dark/Light Mode umschalten</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Drucken</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Beenden</div>

        <div class="shortcut-cat">📖 Navigation</div>
        <div class="shortcut-row"><kbd>Pfeiltasten</kbd> Seite für Seite blättern</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Gehe zu Seite</div>
        <div class="shortcut-row"><kbd>Home / Pos1</kbd> Erste Seite</div>
        <div class="shortcut-row"><kbd>Ende</kbd> Letzte Seite</div>

        <div class="shortcut-cat">✏️ Bearbeitung</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Text einfügen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Seiten löschen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Seiten entnehmen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Seiten einfügen</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Seiten verschieben</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Seite drehen</div>

        <div class="shortcut-cat">🖼️ Elemente verschieben</div>
        <div class="shortcut-row"><kbd>Pfeiltasten</kbd> Text/Bild/Signatur verschieben</div>
        <div class="shortcut-row"><kbd>Ctrl+Pfeiltasten</kbd> Größere Schritte</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Speichern</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Verwerfen</div>

        <div class="shortcut-cat">🗣️ Sprachausgabe</div>
        <div class="shortcut-row"><kbd>F2</kbd> Sprachausgabe ein/aus</div>
        """,
        'info_contextmenu': "📌 Wichtig: Alle Funktionen sind auch über das Kontextmenü (rechte Maustaste) erreichbar!",
        'info_accessibility_hint': "💡 Tipp: Die Sprachausgabe (F2) erleichtert die Orientierung und gibt Feedback zu Menüs und Dialogen.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Lizenz & Impressum",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRESSUM</strong><br>
        Angaben gemäß § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Deutschland<br>
        E-Mail: binhdiez64@gmail.com<br>
        Internet: https://github.com/BinhDiez64/PDFDarkView<br>
        Verantwortlich für den Inhalt: Toralf Schulz (BinhDiez)<br><br>

        <strong>Haftungsausschluss</strong><br>
        Die Software wurde mit größter Sorgfalt entwickelt. Eine Gewähr für die Richtigkeit, Vollständigkeit und Funktionalität<br>
        wird nicht übernommen. Die Nutzung erfolgt auf eigene Verantwortung.<br><br>

        <strong>📄 MIT-Lizenz (private Nutzung)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Erlaubt: kostenlose Nutzung, private Veränderungen, persönliche Kopien.<br>
        Nicht erlaubt: Verkauf, kommerzielle Nutzung, Entfernung von Urheberrechtshinweisen.<br><br>

        <strong>🔧 Drittanbieter-Komponenten</strong><br>
        Diese Software enthält Komponenten unter GPL, AGPL, Apache 2.0, BSD und MIT-Lizenzen.<br>
        Bei Weitergabe müssen die jeweiligen Lizenzbedingungen eingehalten werden.<br><br>

        <strong>🌐 Open Source</strong><br>
        Der Quellcode ist verfügbar und kann gemäß den jeweiligen Lizenzbedingungen eingesehen, verändert und weiterverbreitet werden.<br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # Englische Version (bleibt in allen Sprachversionen gleich, wird unter dem landessprachlichen Text angezeigt)
        'info_license_html_en': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 IMPRINT</strong><br>
        Information according to § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Germany<br>
        Email: binhdiez64@gmail.com<br>
        Responsible for content: Toralf Schulz (BinhDiez)<br><br>

        <strong>⚠️ Disclaimer</strong><br>
        This software was developed with the greatest care. No warranty is given for correctness, completeness or functionality. Use is at your own risk.<br><br>

        <strong>📄 MIT License (private use)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Permitted: free use, private modifications, personal copies.<br>
        Not permitted: sale, commercial use, removal of copyright notices.<br><br>

        <strong>🔧 Third-Party Components</strong><br>
        This software contains components under GPL, AGPL, Apache 2.0, BSD and MIT licenses.<br>
        When redistributing, the respective license terms must be complied with.<br><br>

        <strong>🌐 Open Source</strong><br>
        The source code is available and can be viewed, modified and redistributed according to the respective license terms.<br><br>

        <em>📖 This license information is also available in your local language – simply change the application language.</em><br><br>

        © 2026 Toralf Schulz (BinhDiez)
        </div>
        """,

        # -------------------- Tab 5: CREDITS --------------------
        'info_tab_credits': "Danksagungen",
        'info_credits': "Dank an die Open-Source-Community",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – PDF-Verarbeitung</li>
            <li><strong>PyQt5</strong> – Grafische Oberfläche</li>
            <li><strong>Tesseract OCR</strong> – Texterkennung</li>
            <li><strong>OCRmyPDF</strong> – OCR-Integration</li>
            <li><strong>python-docx</strong> – Word-Export</li>
            <li><strong>qtawesome</strong> – Icons</li>
            <li><strong>DeepSeek</strong> – Unterstützung bei Übersetzungen (60+ Sprachen)</li>
            <li><strong>Allen Nutzern</strong> – Für wertvolles Feedback</li>
            <li><strong>Der Open-Source-Community</strong> – Für großartige Bibliotheken</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Sprachen",
        'info_languages_header': "🌍 Sprachunterstützung",
        'info_languages_html': """
        <div style="line-height:1.6;">
            <p>PDF Dark View unterstützt derzeit <strong>62 Sprachen</strong> – damit die Software weltweit barrierefrei genutzt werden kann.</p>

            <p><strong>📖 Vollständige Sprachliste (Stand: März 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albanisch (Shqip)</li>
                    <li>🇩🇿 Arabisch (العربية)</li>
                    <li>🇮🇩 Balinesisch (Basa Bali)</li>
                    <li>🇧🇩 Bengalisch (বাংলা)</li>
                    <li>🇲🇲 Birmanisch (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bosnisch (Bosanski)</li>
                    <li>🇧🇬 Bulgarisch (Български)</li>
                    <li>🇨🇳 Chinesisch (中文)</li>
                    <li>🇩🇰 Dänisch (Dansk)</li>
                    <li>🇩🇪 Deutsch</li>
                    <li>🇬🇧 Englisch (English)</li>
                    <li>🇪🇪 Estnisch (Eesti)</li>
                    <li>🇫🇮 Finnisch (Suomi)</li>
                    <li>🇫🇷 Französisch (Français)</li>
                    <li>🇬🇷 Griechisch (Ελληνικά)</li>
                    <li>🇮🇱 Hebräisch (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Kroatisch (Hrvatski)</li>
                    <li>🇭🇺 Ungarisch (Magyar)</li>
                    <li>🇮🇩 Indonesisch (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irisch (Gaeilge)</li>
                    <li>🇮🇸 Isländisch (Íslenska)</li>
                    <li>🇮🇹 Italienisch (Italiano)</li>
                    <li>🇯🇵 Japanisch (日本語)</li>
                    <li>🇰🇭 Khmer (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreanisch (한국어)</li>
                    <li>🇱🇦 Laotisch (ພາສາລາວ)</li>
                    <li>🇱🇻 Lettisch (Latviešu)</li>
                    <li>🇱🇹 Litauisch (Lietuvių)</li>
                    <li>🇱🇺 Luxemburgisch (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malaiisch (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolisch (Монгол)</li>
                    <li>🇳🇵 Nepalesisch (नेपाली)</li>
                    <li>🇳🇱 Niederländisch (Nederlands)</li>
                    <li>🇳🇴 Norwegisch (Norsk)</li>
                    <li>🇦🇫 Paschtunisch (پښتو)</li>
                    <li>🇮🇷 Persisch (فارسی)</li>
                    <li>🇵🇱 Polnisch (Polski)</li>
                    <li>🇵🇹 Portugiesisch (Português)</li>
                    <li>🇮🇳 Punjabi (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumänisch (Română)</li>
                    <li>🇷🇺 Russisch (Русский)</li>
                    <li>🇸🇪 Schwedisch (Svenska)</li>
                    <li>🇷🇸 Serbisch (Српски)</li>
                    <li>🇸🇰 Slowakisch (Slovenčina)</li>
                    <li>🇸🇮 Slowenisch (Slovenščina)</li>
                    <li>🇪🇸 Spanisch (Español)</li>
                    <li>🇹🇿 Suaheli (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamil (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Thailändisch (ไทย)</li>
                    <li>🇨🇿 Tschechisch (Čeština)</li>
                    <li>🇹🇷 Türkisch (Türkçe)</li>
                    <li>🇺🇦 Ukrainisch (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Vietnamesisch (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jiddisch (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Eigene Sprachen hinzufügen:</strong><br>
                Möchten Sie eine Sprache, die noch nicht enthalten ist? Legen Sie einfach eine eigene Wörterbuch-Datei (<code>sprache_xx.py</code>) neben die Anwendung – die Software erkennt sie automatisch. Bei Interesse an einer speziellen Übersetzung kontaktieren Sie mich gerne.
            </div>

            <p><strong>🙏 Besonderer Dank:</strong> DeepSeek für die Unterstützung bei der Übersetzung aller Wörterbücher in 62 Sprachen.</p>

            <p>📧 Kontakt für Übersetzungen: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Fehler",
        'error_occurred': "Es ist ein Fehler aufgetreten",
        'error_pdf_load': "Fehler beim Laden der PDF",
        'error_pdf_save': "Fehler beim Speichern der PDF",
        'error_ocr': "Fehler bei der Texterkennung",
        'error_no_pdf': "Kein PDF geladen",
        'error_page_not_found': "Seite nicht gefunden",
        'error_invalid_range': "Ungültiger Seitenbereich",
        'error_file_not_found': "Datei nicht gefunden",
        'error_permission': "Keine Berechtigung",
        'error_unknown': "Unbekannter Fehler",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Erfolg",
        'success_operation': "Vorgang erfolgreich abgeschlossen",
        'success_saved': "Erfolgreich gespeichert",
        'success_exported': "Erfolgreich exportiert",
        'success_imported': "Erfolgreich importiert",
        'success_deleted': "Erfolgreich gelöscht",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Bestätigung",
        'confirm_yes': "Ja",
        'confirm_no': "Nein",
        'confirm_ok': "OK",
        'confirm_cancel': "Abbrechen",
        'confirm_delete': "Löschen",
        'confirm_overwrite': "Überschreiben",
        'confirm_continue': "Fortfahren",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "PDF wird geladen...",
        'progress_saving': "PDF wird gespeichert...",
        'progress_exporting': "PDF wird exportiert...",
        'progress_processing': "Verarbeitung läuft...",
        'progress_wait': "Bitte warten...",
        'progress_preparing': "Vorbereitung...",
        'progress_finalizing': "Finalisierung...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Weiß",
        'color_black': "Schwarz",
        'color_red': "Rot",
        'color_green': "Grün",
        'color_blue': "Blau",
        'color_yellow': "Gelb",
        'color_magenta': "Magenta",
        'color_cyan': "Cyan",
        'color_orange': "Orange",
        'color_gray': "Grau",
        'color_custom': "Farbauswahl",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Datei",
        'menu_edit': "&Bearbeiten",
        'menu_view': "&Ansicht",
        'menu_tools': "&Extras",
        'menu_settings': "&Einstellungen",
        'menu_help': "&Hilfe",
        'menu_language': "🌐 Sprache",
        'menu_guides': "&Anleitungen",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Öffnen",
        'file_save_as': "&Speichern unter...",
        'file_protect': "Dokument &schützen...",
        'file_export': "&Exportieren",
        'file_export_pages': "Als Pages exportieren",
        'file_export_word': "Als DOCX exportieren",
        'file_export_text': "Als TXT exportieren",
        'file_print_now': "&Sofort drucken",
        'file_print': "&Drucken",
        'file_close': "&Schließen",
        'file_quit': "&Beenden",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Suchen",
        'edit_ocr': " OCR durchführen",
        'edit_rotate': "Seite &drehen",
        'edit_rotate_all': "&Alle Seiten drehen",
        'edit_delete_pages': "Seiten &löschen",
        'edit_extract_pages': "Seiten &entnehmen",
        'edit_insert_pages': "Seiten &einfügen",
        'edit_move_pages': "Seiten &verschieben",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Text und Kreuze einfügen",
        'text_insert': " Text einfügen",
        'cross_insert': " Kreuz einfügen",
        'text_customize': " Text anpassen",
        'cross_customize': " Dieses Kreuz anpassen",
        'cross_customize_all': " Alle Kreuze anpassen",
        'text_discard': " Diesen Text / Kreuz verwerfen",
        'text_discard_all': " Alle Texte und Kreuze verwerfen",
        'text_save_all': " Alle Texte und Kreuze speichern",
        'text_guide': " Texteingabe / Textbausteine - Anleitung",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Unterschrift einfügen",
        'signature_settings_menu': " Einstellungen...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Bild einfügen",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Formen einfügen",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "&Textfenster anzeigen",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Seitenbreite (Standard)",
        'view_zoom_two': "&Zwei Seiten",
        'view_zoom_overview': "&Übersicht (mehrere Seiten)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Bedienungshilfen",
        'settings_voice': "Sprachausgabe",
        'settings_voice_tooltip': "ergänzt die Sprachausgabe von Screenreadern mit zusätzlichen Informationen",
        'settings_signature': "&Signatur-Einstellungen",
        'settings_password': "&Passwortverwaltung",
        'settings_backup': "Backup vor Änderungen erstellen",
        'settings_export_import': "&Einstellungen exportieren / importieren",
        'settings_export': "&Alle Einstellungen exportieren...",
        'settings_import': "&Alle Einstellungen importieren...",
        'settings_export_info': "&Was wird exportiert?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "ein",
        'voice_off': "aus",
        'voice_toggle': "Sprachausgabe {0}",
        'voice_speed': "Geschwindigkeit auf {0} Prozent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Tool nicht gefunden:\n{0}\n\nBASE_DIR: {1}\nStellen Sie sicher, dass die PDF-Tools im Verzeichnis {1} installiert sind.",
        'tool_started': "{0} gestartet",
        'tool_start_failed': "Konnte nicht gestartet werden",
        'process_error_failed_to_start': "Prozess konnte nicht gestartet werden. Existiert die Datei?",
        'process_error_crashed': "Prozess abgestürzt während des Starts.",
        'process_error_timeout': "Prozess-Timeout erreicht.",
        'process_error_write': "Schreibfehler beim Prozess.",
        'process_error_read': "Lesefehler beim Prozess.",
        'process_error_unknown': "Unbekannter Prozess-Fehler",
        'process_command': "Befehl",
        'process_normal_exit': "normal beendet",
        'process_crashed': "abgestürzt",
        'process_nonzero_exit': "{0} wurde mit Fehlercode {1} beendet",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Wird abgebrochen...",
        'move_cancelling': "Verschieben wird abgebrochen",
        'opening_pdf': "PDF wird geöffnet...",
        'loading_document': "Lade Dokument...",
        'pdf_opened': "PDF geöffnet",
        'pages_found_moving': "{0} Seiten gefunden, {1} zum Verschieben",
        'creating_backup': "Erstelle Backup...",
        'backup_description': "Sichere Originaldatei...",
        'backup_saved_as': "Gesichert als: {0}",
        'error_format': "Fehler: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Suche zurückgesetzt",
        'page_header_simple': "=== Seite {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Passwortverwaltung – Anleitung",
        'password_guide_voice': "Anleitung zur Passwortverwaltung. Bitte lesen Sie die Hinweise.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Passwortverwaltung – Ausführliche Anleitung</strong></p>

        <p><strong>1. Passwortschutz für PDFs</strong></p>
        <ul>
        <li>Beim Öffnen einer passwortgeschützten PDF erscheint ein Dialog, in dem Sie das Passwort eingeben können.</li>
        <li>Sie können das Passwort verschlüsselt speichern, damit Sie es nicht jedes Mal neu eingeben müssen (Checkbox „Passwort speichern“).</li>
        <li>Mit dem Button „Passwort entfernen“ können Sie eine entschlüsselte Kopie der PDF erstellen und das Passwort aus der Datenbank löschen.</li>
        </ul>

        <p><strong>2. Master-Passwort</strong></p>
        <ul>
        <li>Das Master-Passwort schützt den Zugriff auf alle gespeicherten PDF-Passwörter.</li>
        <li><strong>Einrichten:</strong> Gehen Sie zu „Einstellungen → Passwortverwaltung → Master-PW Einstellungen“ und klicken Sie auf „Master-Passwort einrichten“. Wählen Sie ein sicheres Passwort (mindestens 8 Zeichen).</li>
        <li><strong>Ändern:</strong> Nach erfolgreicher Authentifizierung können Sie das Master-Passwort ändern.</li>
        <li><strong>Entfernen:</strong> Wenn Sie das Master-Passwort löschen, werden ALLE gespeicherten Passwörter unwiderruflich gelöscht. Sie können vorher eine Sicherung exportieren.</li>
        <li>Einmal pro Sitzung müssen Sie sich mit dem Master-Passwort authentifizieren, um auf geschützte Funktionen (z.B. Anzeigen von Passwörtern) zugreifen zu können.</li>
        </ul>

        <p><strong>3. Passwortverwaltung (Liste)</strong></p>
        <ul>
        <li>Unter „Einstellungen → Passwortverwaltung“ öffnen Sie eine Tabelle aller gespeicherten PDFs mit ihren verschlüsselten Passwörtern.</li>
        <li><strong>Ohne Master-Passwort:</strong> Sie können nur Einträge löschen – die Passwörter bleiben verborgen.</li>
        <li><strong>Mit Master-Passwort (authentifiziert):</strong> Sie können Passwörter anzeigen, kopieren, exportieren und löschen.</li>
        <li><strong>Export:</strong> Wählen Sie ein Format (JSON, CSV, TXT) und speichern Sie die Liste. Bei gesetztem Master-Passwort können Sie entscheiden, ob die Passwörter im Klartext oder weiterhin verschlüsselt exportiert werden.</li>
        <li><strong>Import:</strong> Eine zuvor exportierte ZIP-Datei mit allen Einstellungen (inklusive Passwörtern) kann über „Einstellungen → Einstellungen exportieren/importieren“ wieder eingelesen werden. Achtung: Vorhandene Daten werden überschrieben!</li>
        </ul>

        <p><strong>4. Passwortgenerator</strong></p>
        <ul>
        <li>Im Passwort-Dialog (z.B. beim Schützen einer PDF) finden Sie rechts neben dem Eingabefeld einen Würfel-Button 🎲.</li>
        <li>Klicken Sie darauf, um den Passwortgenerator zu öffnen. Sie können Länge, Zeichensätze (Großbuchstaben, Kleinbuchstaben, Zahlen, Sonderzeichen) und Trennzeichen für bessere Lesbarkeit einstellen.</li>
        <li>Das generierte Passwort kann direkt übernommen und bei Bedarf auch kopiert werden.</li>
        </ul>

        <p><strong>5. Wichtige Sicherheitshinweise</strong></p>
        <ul>
        <li>Gespeicherte Passwörter werden mit AES-256 verschlüsselt abgelegt. Der Schlüssel wird aus Ihrem Master-Passwort abgeleitet (falls gesetzt) oder aus einem festen Wert (ohne Master-Passwort).</li>
        <li>Ohne Master-Passwort sind die Passwörter zwar verschlüsselt, aber der Schlüssel ist im Programm hinterlegt – ein Angreifer mit Zugriff auf Ihre Dateien könnte sie entschlüsseln. Daher empfehlen wir dringend die Verwendung eines Master-Passworts.</li>
        <li>Die Passwort-Datenbank liegt im Verzeichnis `Daten/passwords.json`. Machen Sie regelmäßig Backups, besonders vor dem Entfernen des Master-Passworts.</li>
        <li>Bei Verlust des Master-Passworts sind alle gespeicherten Passwörter unwiederbringlich verloren.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # Neu ab 2026-03-19
        # (32 Info und alles ab 53 in den anderen Wörterbüchern ersetzen)
        # ============================================

        # ============================================
        # 53. EINSTELLUNGEN FÜR DARKMODE - hinzugefügt am 2026-03-16
        # ============================================
        'invert_mode_label': "Invertierungsmodus",
        'invert_mode_classic': "Klassisch (alle Farben invertieren)",
        'invert_mode_smart': "Intelligent (nur Helligkeit invertieren)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Graustufen-Schwellwert",
        'gray_threshold_10': "10% (streng)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (Standard)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (weich)",
        'threshold_changed': "Schwellwert auf {0}% gesetzt",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Graustufen-Schwellwert – Erklärung",
        'threshold_guide_text': "Der Graustufen-Schwellwert bestimmt, welche Pixel im intelligenten Dark Mode als 'grau' gelten und invertiert werden.\n\n"
                                "• Ein niedriger Wert (10%) invertiert nur nahezu perfekte Grautöne – farbige Elemente bleiben vollständig erhalten.\n"
                                "• Ein hoher Wert (50%) invertiert auch leicht farbige Pixel – das erhöht den Kontrast, kann aber Farben verfälschen.\n\n"
                                "Der optimale Wert hängt vom Dokument ab. Für reine Textdokumente ist 30–40% oft ideal, für farbige Grafiken eher 10–20%.\n\n"
                                "Sie können den Wert jederzeit über das Menü 'Einstellungen' anpassen – das PDF wird dann sofort neu geladen.\n\n"
                                "Beachte:\n* Fotos und Bilder können nur im Light Mode korrekt angezeigt werden!\n* Die Invertierungseinstellungen werden nur bei aktiviertem Dark Mode angezeigt.",
        'threshold_guide_voice': "Der Graustufen-Schwellwert bestimmt, wie stark der intelligente Dark Mode eingreift. Ein niedriger Wert schont Farben, ein hoher erhöht den Kontrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "PDF wird geöffnet...",
        'progress_loading_document': "Lade Dokument...",
        'progress_pdf_opened': "PDF geöffnet",
        'progress_creating_backup': "Erstelle Backup...",
        'progress_backup_description': "Sichere Originaldatei...",
        'progress_backup_created': "Backup erstellt",
        'progress_backup_saved_as': "Gesichert als: {0}",
        'progress_analyzing_start': "Starte Analyse...",
        'progress_searching_empty': "Suche leere Seiten...",
        'progress_page_empty': "Seite {0} ist leer",
        'progress_page_keep': "Seite {0} behalten",
        'progress_analysis_complete': "Analyse abgeschlossen",
        'progress_empty_found': "{0} leere Seiten gefunden",
        'progress_current_page': "Aktuelle Seite",
        'progress_mark_delete': "Wird zum Löschen markiert",
        'progress_range_selected': "Seitenbereich {0}-{1}",
        'progress_deleting_pages': "Lösche {0} Seiten",
        'progress_creating_new_pdf': "Erstelle neue PDF...",
        'progress_transferring_pages': "Übertrage Seiten",
        'progress_keeping_page': "Seite {0} wird behalten ({1}/{2})",
        'progress_saving_pdf': "Speichere PDF...",
        'progress_optimizing': "Optimiere Dateigröße...",
        'progress_finalizing': "Finalisiere...",
        'progress_new_size': "Neue Größe: {0:.2f} MB",
        'progress_cancelling': "Wird abgebrochen...",
        'progress_cancel_message': "{0} wird abgebrochen",
        'progress_pages_found_moving': "{0} Seiten gefunden, {1} zum Verschieben",

        # OCR-Fortschritt
        'ocr_status_analyzing': "PDF wird analysiert...",
        'ocr_status_optimizing': "Bildoptimierung läuft...",
        'ocr_status_recognizing': "Texterkennung in Arbeit...",
        'ocr_status_embedding': "Text wird eingebettet...",
        'ocr_status_finalizing': "Finalisierung der PDF...",

        # PDF-Laden
        'progress_preparing': "Vorbereitung...",
        'progress_loading': "PDF wird geladen...",

        # Seitenoperationen
        'progress_deleting_title': "Seiten löschen...",
        'progress_moving_title': "Seiten verschieben...",
        'pages_found': "Seiten gefunden",
        'progress_creating_new_order': "Erstelle neue Reihenfolge...",
        'progress_sorting_pages': "Sortiere Seiten...",
        'progress_moving_to_begin': "Verschiebe {0} Seiten an den Anfang",
        'progress_transferring_count': "Übertrage {0} Seiten",
        'progress_transferring_before_target': "Übertrage Seiten vor dem Ziel",
        'progress_moving_pages': "Verschiebe {0} Seiten",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_geschützt_",
        'filename_copy_suffix': "_Kopie",
        'filename_page_single': "_Seite_",
        'filename_page_range': "_Seiten_",
        'filename_export_page': "_Seite_{0:03}",
        'filename_export_range': "_Seiten_{0}-{1}",
        'filename_export_multiple': "_Seiten_{0}",
        'filename_with_text': "_mit_Text",
        'filename_with_signature': "_mit_Unterschrift",
        'filename_with_image': "_mit_Bild",
        'filename_with_forms': "_mit_Formen",
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
        'view_toggle_navbar': "Buttonleiste anzeigen",

        # ============================================
        # 57. SEITEN LÖSCHEN
        # ============================================
		'pages_cannot_delete_all': "Es können nicht alle Seiten gelöscht werden",
        'pages_cannot_delete_last_page': 'Die letzte Seite kann nicht gelöscht werden!',
        'pages_cannot_delete_all_pages': 'Es muss mindestens eine Seite im Dokument verbleiben!',
        'delete_pages_confirm': 'Sind Sie sicher, dass Sie {0} Seiten löschen möchten?',
        'delete_pages_confirm_voice': 'Sind Sie sicher, dass Sie {0} Seiten löschen möchten?',
        'pages_deleted': '{0} Seiten wurden erfolgreich gelöscht.',
        'warning': 'Warnung',
        'error': 'Fehler',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Keine Form ausgewählt",
        'form_customized': "Form angepasst",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Auswählen",
        'btn_use': "Verwenden",
        'master_password_for_spasswords': "Um Passwörter zu speichern und zu verwenden, muss zuerst ein Master-Passwort eingerichtet werden.\n\nMöchten jetzt das Master-Passwort einrichten?",
        'open_saved_dialog_title': "Gespeicherte Datei öffnen",
        'open_saved_question': "Möchten Sie die gespeicherte Datei jetzt öffnen?",
        'password': "Passwort",
        'password_manager_master_required': "Der Passwort-Manager ist nur verfügbar, wenn ein Master-Passwort eingerichtet wurde.\n\nMöchten Sie jetzt das Master Passwort einrichten?",
        'password_master_required_for_select': "Um gespeicherte Passwörter anzeigen und auswählen zu können, müssen Sie sich zuerst mit Ihrem Master-Passwort authentifizieren.\n\nMöchten Sie sich jetzt authentifizieren?",
        'password_not_available': "Das ausgewählte Passwort ist nicht verfügbar oder konnte nicht entschlüsselt werden.",
        'password_options_title': "Passwort-Optionen",
        'password_save_choice_change': "Neues Passwort festlegen",
        'password_save_choice_keep': "Bestehendes Passwort verwenden",
        'password_save_choice_none': "Unverschlüsselt speichern",
        'password_save_hint': "Richten Sie zuerst ein Master-Passwort ein, um Passwörter sicher zu speichern.",
        'password_save_master_required': "Passwort speichern (nur mit Master-Passwort möglich)",
        'password_save_question': "Die aktuelle PDF ist passwortgeschützt. Möchten Sie das bestehende Passwort verwenden, ein neues festlegen oder unverschlüsselt speichern?",
        'password_select': "Passwort auswählen",
        'password_select_none': "Kein Passwort ausgewählt.\n\nBitte wählen Sie ein Passwort aus der Liste aus.",
        'password_select_one': "Bitte wählen Sie genau ein Passwort aus.\n\nSie haben mehrere Passwörter markiert.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_backup",  # Hinweis: Dieser Eintrag existiert bereits in 55, wird hier aber für andere Kontexte genutzt. Ist kein Duplikat im Sinne des Dictionary-Keys, da der Schlüssel gleich ist. Aber Achtung: Der Wert wird überschrieben. Ich belasse es zur Sicherheit so, wie es war. In der Praxis sollte man den Schlüssel nicht doppelt verwenden.
        'filename_insert_suffix': "_mit_Einfuegung",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_Seiten_gelöscht",
        'filename_pages_moved': "_Seiten_verschoben",
        'filename_rotated_all_suffix': "_alle_Seiten_gedreht",
        'filename_rotated_suffix': "_Seite_gedreht",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfiguration der Dateinamen bei Änderungen am PDF",
        'filename_keep_suffixes': "Vorherige Erweiterungen (z.B. _mit_Text) behalten",
        'filename_keep_suffixes_false': "Ersetzen",
        'filename_keep_suffixes_true': "Behalten",
        'filename_preview_label': "Vorschau des Dateinamens:",
        'filename_preview_overwrite_hint': "Vorschau nicht verfügbar – das Original wird überschrieben.",
        'filename_separator': "Trennzeichen zwischen den Wörtern",
        'filename_separator_none': "Kein Trennzeichen",
        'filename_separator_space': "Leerzeichen ( )",
        'filename_separator_underscore': "Unterstrich (_)",
        'filename_settings_saved': "Dateinamen-Einstellungen gespeichert",
        'filename_settings_title': "Dateinamen-Formatierung & Backup",
        'filename_timestamp_position': "Position des Zeitstempels",
        'filename_timestamp_position_after': "Nach dem Basisnamen",
        'filename_timestamp_position_before': "Ganz vorne",
        'filename_timestamp_position_end': "Am Ende",
        'filename_use_timestamp': "Zeitstempel verwenden",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Verhalten bei Änderungen:</b><ul><li>Löschen und Einfügen von Seiten</li><li>Einfügen von Text, Signatur, Bild und Formen</li><li>OCR</li></ul></html>",
        'backup_section': "Backup für Seiten-Operationen (Löschen, Verschieben)",
        'behavior_info': "Hinweis: Bei 'Original überschreiben' werden Zeitstempel und Suffixe ignoriert – die Datei behält ihren Namen.",
        'behavior_new_file': "Immer neue Datei erstellen (mit Zeitstempel und Suffix)",
        'behavior_overwrite': "Original überschreiben (keine neue Datei)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Alle Seiten wurden gedreht.\n\nOriginal blieb unverändert.\nNeue Datei: {0}",
        'all_pages_rotated_voice': "Alle Seiten gedreht, neue Datei erstellt.",
        'empty_pages_deleted_new_file': "{0} leere Seiten wurden gelöscht.\n\nOriginal blieb unverändert.\nNeue Datei: {1}",
        'empty_pages_deleted_voice': "{0} leere Seiten gelöscht, neue Datei erstellt.",
        'ocr_keep_original': "Original behalten (später manuell öffnen)",
        'ocr_new_file_question': "Die neue durchsuchbare PDF wurde gespeichert unter:\n{0}\n\nMöchten Sie diese jetzt öffnen?",
        'ocr_open_new': "Neue OCR-Datei öffnen",
        'ocr_original_kept': "Die Originaldatei bleibt geöffnet. Die OCR-Datei wurde gespeichert.",
        'page_deleted_new_file': "Seite {0} wurde gelöscht.\n\nOriginal blieb unverändert.\nNeue Datei: {1}",
        'page_deleted_voice': "Seite {0} gelöscht, neue Datei erstellt.",
        'page_rotated_new_file': "Seite {0} wurde gedreht.\n\nOriginal blieb unverändert.\nNeue Datei: {1}",
        'page_rotated_voice': "Seite {0} gedreht, neue Datei erstellt.",
        'pages_deleted_new_file': "Es wurden {0} Seiten gelöscht.\n\nDie Originaldatei blieb unverändert.\nNeue Datei: {1}",
        'pages_deleted_new_file_voice': "{0} Seiten gelöscht, neue Datei erstellt.",
        'pages_inserted_new_file': "Es wurden {0} Seiten eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei: {1}",
        'pages_inserted_new_file_ask': "Es wurden {0} Seiten eingefügt.\n\nOriginal blieb unverändert.\nNeue Datei: {1}\n\nMöchten Sie diese jetzt öffnen?",
        'pages_inserted_voice_new': "{0} Seiten eingefügt, neue Datei erstellt.",
        'pages_moved_new_file': "Es wurden {0} Seiten verschoben.\n\nDie Originaldatei blieb unverändert.\nNeue Datei: {1}",
        'pages_moved_new_file_voice': "{0} Seiten verschoben, neue Datei erstellt.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Nicht mehr anzeigen",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Backup-Einstellung</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Backup EIN</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Bei allen Änderungen, die das Original überschreiben</strong> (Text, Signatur, Bild, Form, OCR, Drehen, Einfügen, Seiten löschen/verschieben) wird <strong>automatisch ein Backup mit Zeitstempel</strong> erstellt, bevor die Änderung angewendet wird.</p>
                <p style="margin: 5px 0 5px 20px;">• Das Backup liegt neben der Originaldatei (z. B. <code>Dokument_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Wenn Sie zusätzlich die Option <strong>„Original überschreiben“</strong> aktiviert haben, wird ebenfalls ein Backup erstellt.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Backup AUS</p>
                <p style="margin: 5px 0 5px 20px;">• Es wird <strong>kein Backup</strong> erstellt – weder beim Überschreiben noch bei Seiten-Operationen.</p>
                <p style="margin: 5px 0 5px 20px;">• Die Originaldatei kann bei Überschreiben unwiderruflich verloren gehen.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Nur für erfahrene Benutzer empfohlen!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tipp:</strong> Die Backup-Einstellung ist unabhängig von der Option „Original überschreiben“. Sie können beides kombinieren.<br>
                Sie können diese Meldung dauerhaft ausblenden.
            </div>
        </div>
        """,
        'backup_info_title': "Backup-Verhalten",
        'backup_info_voice': "Hinweis zum Backup-Verhalten bei Seitenoperationen. Backup an überschreibt Original, Backup aus erstellt neue Datei.",
        'show_backup_info': "Info zur Backup Einstellung",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Nicht mehr anzeigen",
        'overwrite_enable_backup': "Backup aktivieren (empfohlen)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Original überschreiben</p>
            <p>Wenn Sie diese Option aktivieren, werden Änderungen (Text, Signatur, Bild, Form, OCR, Drehen, Einfügen) <strong>direkt im Original gespeichert</strong> – es entsteht <strong>keine neue Datei</strong>.</p>
            <p>• Der Dateiname bleibt unverändert.<br>
            • Zeitstempel und Suffixe werden ignoriert.<br>
            • <strong>Ohne Backup kann das Original unwiderruflich verloren gehen.</strong></p>
            <p style="color: #FFD700;">Empfehlung: Aktivieren Sie zusätzlich die Backup-Option, um automatische Sicherungen zu erhalten.</p>
        </div>
        """,
        'overwrite_info_title': "Original überschreiben",
        'overwrite_info_voice': "Achtung: Original überschreiben – keine neue Datei. Backup empfohlen.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Es wurden {0} Seiten eingefügt.\n\nDie Originaldatei wurde überschrieben.\nEin Backup wurde erstellt.",
        'pages_inserted_overwrite_no_backup': "Es wurden {0} Seiten eingefügt.\n\nDie Originaldatei wurde überschrieben.\nEs wurde KEIN Backup erstellt.",
        'texts_saved_overwrite_with_backup': "Die Änderungen wurden im Original gespeichert.\n\nEin Backup wurde erstellt.",
        'texts_saved_overwrite_no_backup': "Die Änderungen wurden im Original gespeichert.\n\nEs wurde KEIN Backup erstellt.",
        'texts_crosses_saved_new_file': "{0} {1} und {2} {3} wurden eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei wurde erstellt.\n\nDie neue PDF wird geladen...",
        'texts_saved_new_file': "{0} {1} wurden eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei wurde erstellt.\n\nDie neue PDF wird geladen...",
        'crosses_saved_new_file': "{0} {1} wurden eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei wurde erstellt.\n\nDie neue PDF wird geladen...",
        'elements_saved_new_file': "{0} Elemente wurden eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei wurde erstellt.\n\nDie neue PDF wird geladen...",
        'signatures_saved_overwrite_with_backup': "Die Signatur(en) wurden im Original gespeichert.\n\nEin Backup wurde erstellt.",
        'signatures_saved_overwrite_no_backup': "Die Signatur(en) wurden im Original gespeichert.\n\nEs wurde KEIN Backup erstellt.",
        'images_saved_overwrite_with_backup': "Die Bild(er) wurden im Original gespeichert.\n\nEin Backup wurde erstellt.",
        'images_saved_overwrite_no_backup': "Die Bild(er) wurden im Original gespeichert.\n\nEs wurde KEIN Backup erstellt.",
        'forms_saved_overwrite_with_backup': "Die Form(en) wurden im Original gespeichert.\n\nEin Backup wurde erstellt.",
        'forms_saved_overwrite_no_backup': "Die Form(en) wurden im Original gespeichert.\n\nEs wurde KEIN Backup erstellt.",
        'signatures_saved_new_file': "{0} Signaturen wurden eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei wurde erstellt.\n\nDie neue PDF wird geladen...",
        'images_saved_new_file': "{0} Bilder wurden eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei wurde erstellt.\n\nDie neue PDF wird geladen...",
        'forms_saved_new_file': "{0} Formen wurden eingefügt.\n\nDie Originaldatei blieb unverändert.\nNeue Datei wurde erstellt.\n\nDie neue PDF wird geladen...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Achtung: Diese PDF enthält gedrehte Seiten. Die Positionierung könnte abweichen.",
        'page_rotated_warning_title': "Gedrehte Seite erkannt",
        'page_rotated_warning_message': "Die aktuelle Seite {0} ist um {1}° gedreht.\n\nDas Einfügen von Elementen auf gedrehten Seiten wird nicht unterstützt.\n\nMöchten Sie die Seite jetzt in aufrechte Position drehen?",
        'page_rotated_warning_voice': "Achtung: Die Seite ist gedreht. Bitte drehen Sie sie zuerst.",
        'paste_on_rotated_page_simple_warning': "Einfügen auf Seite {0} nicht möglich!\n\nDiese Seite ist um {1}° gedreht.\n\nBitte drehen Sie die Seite zuerst auf 0° (Menü: Bearbeiten → Seite ausrichten).\n\nAchtung:\nDas vorher kopierte Element geht verloren, wenn Sie vor dem Drehen der Seite nicht speichern.",
        'paste_on_rotated_page_voice': "Einfügen abgebrochen. Seite ist gedreht. Bitte zuerst Seite ausrichten.",
        'page_rotated_cancel': "Abbrechen",
        'page_rotated_rotate_until_upright': "Seite wiederholt drehen (bis aufrecht)",
        'page_rotated_now_upright': "Die Seite ist jetzt aufrecht. Sie können nun einfügen.",
        'page_rotated_still_not_upright': "Die Seite konnte nicht aufrecht gedreht werden. Bitte manuell korrigieren.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Hilfe: Gedrehte Seiten korrigieren",
        'help_rotated_pages_voice': "Hilfe zum Korrigieren gedrehter Seiten wird geöffnet.",
        'btn_help': "Hilfe",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Gedrehte Seite – Einfügen funktioniert nicht korrekt</p>

            <p>Wenn das Einfügen von Texten, Signaturen oder Formen auf einer gedrehten Seite nicht richtig funktioniert, können Sie die Seite mit einem externen PDF-Editor korrigieren.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Lösung mit externem Tool (z. B. macOS Vorschau)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Seite exportieren</strong><br>
                &nbsp;&nbsp;Klicken Sie im Menü auf <strong>Datei → Als Pages exportieren</strong> oder verwenden Sie eine andere Methode, um die gewünschte Seite als einzelne PDF zu speichern.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Seite in externem Programm öffnen</strong><br>
                &nbsp;&nbsp;Öffnen Sie die exportierte PDF in einem PDF-Editor (z. B. <strong>macOS Vorschau</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Seite drehen</strong><br>
                &nbsp;&nbsp;Drehen Sie die Seite so, dass sie aufrecht steht (in Vorschau: <strong>Werkzeuge → Drehen</strong> oder <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Speichern</strong><br>
                &nbsp;&nbsp;Speichern Sie die korrigierte Seite (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Seite wieder in das Originaldokument einfügen</strong><br>
                &nbsp;&nbsp;Kehren Sie zu PDFDarkView zurück und fügen Sie die korrigierte Seite an der gewünschten Position ein:<br>
                &nbsp;&nbsp;<strong>Bearbeiten → Seiten einfügen</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternative: Seite im Original drehen</p>
                <p style="margin: 5px 0 5px 20px;">• Verwenden Sie die integrierte Drehfunktion (<strong>Bearbeiten → Seite drehen</strong>), um die Seite schrittweise zu korrigieren.<br>
                • Nach jeder Drehung können Sie prüfen, ob das Einfügen nun funktioniert.<br>
                • Dies ist oft die schnellere Lösung – probieren Sie es zuerst!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Tipp:</strong> Wenn Sie häufig auf gedrehte Seiten stoßen, können Sie die Warnung im Einfüge-Dialog dauerhaft ausblenden.<br>
                Die Positionierung kann dann jedoch abweichen – nutzen Sie diese Option nur, wenn Sie die Auswirkungen kennen.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Seiten ausrichten",
        'menu_rotate_normalize_tooltip': "Seite drehen oder auf 0° zurücksetzen",
        'normalize_current_page': "Aktuelle Seite in aufrechte Position bringen (auf 0° setzen)",
        'normalize_all_pages': "Alle Seiten in aufrechte Position bringen (auf 0° setzen)",
        'page_normalized': "Seite {0} wurde auf aufrechte Position gesetzt.",
        'all_pages_normalized': "Alle Seiten wurden auf aufrechte Position gesetzt.",
        'page_already_upright': "Seite {0} ist bereits aufrecht.",
        'all_pages_already_upright': "Alle Seiten sind bereits aufrecht.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>Das PDF enthält keinen durchsuchbaren Text.</p><p>Möchten Sie OCR durchführen, um nach {0} zu exportieren?</p>",
        'export_ocr_voice': "Das PDF enthält keinen Text. OCR erforderlich für Export nach {0}.",
        'export_no_ocr_possible': "Export ohne OCR nicht möglich. Bitte führen Sie OCR über das Menü aus.",
        'ocr_failed_export_not_possible': "OCR fehlgeschlagen. Export kann nicht durchgeführt werden.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF wird in der Vorschau geöffnet. Bitte starten Sie dort den Druckvorgang.",
        'print_preview_manual': "PDF wurde geöffnet. Bitte führen Sie den Druckbefehl manuell aus (z. B. Strg+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "PDFs zusammenführen",
        'merge_pdfs': "PDFs zusammenführen",
        'merge_progress_title': "PDFs werden zusammengeführt...",
        'merge_pdfs_list': "PDFs in der Reihenfolge (Drag & Drop zum Sortieren)",
        'merge_add_pdf': "PDF hinzufügen",
        'merge_remove': "Entfernen",
        'merge_move_up': "Nach oben",
        'merge_move_down': "Nach unten",
        'merge_pdfs_info': "💡 Tipp: Sie können die Reihenfolge per Drag & Drop ändern",
        'merge_no_pdfs': "Keine PDFs ausgewählt. Klicken Sie auf 'PDF hinzufügen'.",
        'merge_info': "{0} PDFs ausgewählt (ca. {1} Seiten)",
        'merge_open_file': "Datei öffnen",
        'merge_merge': "Zusammenführen",
        'merge_error': "Fehler beim Zusammenführen",
        'merge_min_two_pdfs_error': "Bitte wählen Sie mindestens zwei PDF-Dateien zum Zusammenführen aus.",
        'merge_select_pdfs': "PDFs zum Zusammenführen auswählen",
        'merge_error_file': "Fehler beim Verarbeiten",
        'merge_cancelled': "Zusammenführen wurde abgebrochen",
        'merge_preparing': "Vorbereitung...",
        'merge_processing': "Verarbeite PDF {0} von {1}",
        'merge_saving': "Speichere zusammengeführte PDF...",
        'merge_complete': "Fertig!",
        'merge_success_title': "Zusammenführen erfolgreich",
        'merge_success_voice': "Es wurden {0} PDFs erfolgreich zusammengeführt.",
        'merge_success_message': "Es wurden {0} PDFs erfolgreich zusammengeführt.\n\nDas neue Dokument hat jetzt {1} Seiten.\n\nNeue Datei:\n{2}\n\nSpeicherort:\n{3}\n{2}\n\nMöchten Sie diese PDF öffnen?",
        'replace_file_title': "Datei ersetzen?",
        'replace_file_message': "Es ist bereits eine PDF geöffnet. Möchten Sie diese durch die neue Datei ersetzen?",
        'btn_yes': "Ja",
        'btn_no': "Nein",
        'filename_merge_suffix': "zusammengefuegt",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Öffne {0}...",
        'progress_merge_reading': "Lese {0}...",
        'progress_merge_adding': "Füge {0} Seiten hinzu...",
        'progress_merge_optimizing': "Optimiere PDF...",
        'progress_merge_writing': "Schreibe PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "dem Schließen der PDF",
        'action_close_window': "dem Schließen des Fensters",
        'action_open_new_pdf': "dem Öffnen einer neuen PDF",
        'action_quit_app': "dem Beenden der Anwendung",
        'changes_saved': "Die Änderungen wurden gespeichert.",
        'file_close_title': "PDF Datei Schließen",
        'save_before_action': "Sollen die Änderungen vor {0} gespeichert werden? Ja oder Nein?",
        'save_before_action_voice': "Sollen die Änderungen vor {0} gespeichert werden? Ja oder Nein?",
        'save_before_close_question': "Sollen die Änderungen vor dem Schließen gespeichert werden? Ja oder Nein?",

        # ============================================
        # Neue Einträge (noch nicht übersetzt)
        # ============================================

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Durchsuchbare PDF erstellt:\n\n{0}\n\n<b>ggf. erneut versuchen",
        "ocr_rotate_title": "Seiten ausrichten vor OCR",
        "ocr_rotate_question": "Das PDF enthält gedrehte Seiten.\nMöchten Sie alle Seiten vor der OCR auf 0° ausrichten?\nDies verbessert die Texterkennung erheblich.",
        "ocr_rotate_yes": "Ja, ausrichten",
        "ocr_rotate_no": "Nein, direkt OCR starten",
        "ocr_rotate_voice": "Das PDF enthält gedrehte Seiten. Sollen alle Seiten vor der OCR ausgerichtet werden?",
        "ocr_not_performed_message": "Kein Text vorhanden. Bitte führen Sie OCR durch (Menü \"Bearbeiten\" → \"OCR durchführen\" oder Taste Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "OCR-Einstellungen",
        "ocr_language_btn": "OCR-Sprache auswählen",
        "ocr_language": "OCR-Sprache(n)",
        "ocr_language_current": "Aktuelle Sprache:",
        "ocr_param_info": "Information zum Parameter",

        # Parameter-Labels
        "ocr_force_ocr_label": "OCR erzwingen",
        "ocr_deskew_label": "Schiefe korrigieren",
        "ocr_clean_label": "Bild reinigen",
        "ocr_oversample_label": "Auflösung (DPI)",
        "ocr_pagesegmode_label": "Seitenaufteilung",
        "ocr_oem_label": "OCR-Engine-Modus",
        "ocr_optimize_label": "PDF-Komprimierung",
        "ocr_jobs_label": "Parallele Prozesse",
        "ocr_verbose_label": "Log-Detailgrad",
        # Tooltips für die Controls
        "ocr_force_ocr_tooltip": "OCR auf jeder Seite erzwingen, auch wenn Text vorhanden ist",
        "ocr_deskew_tooltip": "Schiefe Scans automatisch ausrichten",
        "ocr_clean_tooltip": "Rauschen und Artefakte aus dem Bild entfernen",
        "ocr_oversample_tooltip": "Bild vor der OCR auf diese DPI hochskalieren",
        "ocr_pagesegmode_tooltip": "Legt fest, wie die Seite in Textbereiche aufgeteilt wird",
        "ocr_oem_tooltip": "Wählt die OCR-Engine von Tesseract",
        "ocr_optimize_tooltip": "Komprimierungsstufe der Ausgabe-PDF",
        "ocr_jobs_tooltip": "Anzahl der parallelen OCR-Prozesse",
        "ocr_verbose_tooltip": "Detailgrad der Log-Ausgaben",
        "ocr_settings_explain_btn": "Erklärung",

        # Parameter-Erklärungen (Tooltips + Info-Dialoge)
        "ocr_force_ocr_explain": "Erzwingt die Texterkennung auf <b>jeder</b> Seite, auch wenn diese bereits Text enthält.\n\nEmpfehlung: <b>Ein</b> für gescannte PDFs, <b>Aus</b> für native PDFs mit bereits vorhandenem Text.",

        "ocr_deskew_explain": "Korrigiert leicht schiefe Scans (bis ca. 5°).\n\nEmpfehlung: <b>Ein</b> für gescannte Dokumente, <b>Aus</b> wenn die Seiten bereits perfekt gerade sind.",

        "ocr_clean_explain": "Entfernt Rauschen, Punkte und kleine Artefakte aus dem Bild.\n<b>WICHTIG:</b> Bei arabischen, thailändischen oder vietnamesischen Texten mit Diakritika (Punkten über/unter Buchstaben) sollte diese Option <b>deaktiviert</b> werden, da sonst wichtige Zeichen verloren gehen können.",

        "ocr_oversample_explain": "Skaliert das Bild <b>vor</b> der Texterkennung auf die angegebene DPI hoch.<br><br>• <b>72-150 DPI:</b> Sehr schnell, aber geringe Erkennungsquote<br>• <b>200-300 DPI:</b> Optimaler Bereich (Standard: 300)<br>• <b>400+ DPI:</b> Kaum bessere Erkennung, aber deutlich größere Dateien<br><br>Empfehlung: 300 DPI für komplexe Schriften (Arabisch, Chinesisch, Japanisch), 200 DPI für westliche Sprachen.",
        "ocr_pagesegmode_explain": "Legt fest, wie Tesseract die Seite in Textbereiche aufteilt.\n\n• <b>3 - Automatisch (Standard):</b> Gut für gemischte Layouts\n• <b>4 - Einzelne Spalte:</b> Für einspaltige Texte\n• <b>5 - Vertikaler Block:</b> Für vertikale Schriften (Japanisch, Chinesisch)\n• <b>6 - Einheitlicher Textblock:</b> Optimal für Fließtext ohne Spalten\n• <b>11 - Rohes Bild:</b> Für schlechte Scans / Handschriften\n\nEmpfehlung: <b>6</b> für einfache Textdokumente, <b>3</b> für komplexe Layouts.",

        "ocr_oem_explain": "Wählt die OCR-Engine von Tesseract.\n\n• <b>0 - Legacy:</b> Alte Engine (schnell, aber weniger genau)\n• <b>1 - LSTM:</b> Neuronale Engine (langsamer, aber genauer)\n• <b>2 - Legacy + LSTM:</b> Kombiniert beide Ergebnisse\n• <b>3 - Standard (LSTM bevorzugt):</b> Beste Wahl für die meisten Fälle\n\nEmpfehlung: <b>3</b> für maximale Erkennungsgenauigkeit.",

        "ocr_optimize_explain": "Komprimiert die Ausgabe-PDF.\n\n• <b>0:</b> Keine Optimierung (schnellste Verarbeitung)\n• <b>1:</b> Leichte Optimierung (guter Kompromiss)\n• <b>2:</b> Moderate Optimierung\n• <b>3:</b> Starke Optimierung (kleinste Datei, aber langsamer)\n\nEmpfehlung: <b>1</b> für den täglichen Gebrauch.",

        "ocr_jobs_explain": "Anzahl der parallelen Prozesse für die OCR.\n\n• <b>1:</b> Langsam, aber niedrigster Speicherverbrauch\n• <b>4-8:</b> Optimal für moderne Mehrkern-Prozessoren\n• <b>12+:</b> Kaum schnellere Verarbeitung bei hohem Speicherverbrauch\n\nEmpfehlung: Anzahl der CPU-Kerne (z.B. <b>4</b> bei 4-Kern-Systemen).",

        "ocr_verbose_explain": "Detailgrad der Log-Ausgaben in der Konsole.\n\n• <b>0:</b> Keine Ausgaben\n• <b>1:</b> Fortschritt und Statusmeldungen\n• <b>2:</b> Detaillierte Ausgaben\n• <b>3:</b> Vollständige Debug-Ausgaben (sehr umfangreich)\n\nEmpfehlung: <b>1</b> für den normalen Betrieb.",

        "ocr_reset_title": "Einstellungen zurückgesetzt",
        "ocr_reset_message": "Alle OCR-Einstellungen wurden auf die Standardwerte zurückgesetzt.",
        "info_tooltip": "Weitere Informationen zu diesem Parameter",
        "ocr_reset_defaults": "Auf Standard zurücksetzen",
        # ==================== OCR PSM-Modi (Seitenaufteilung) ====================
        "ocr_psm_0": "Automatisch (Legacy-Engine)",
        "ocr_psm_1": "Automatische Spaltenerkennung",
        "ocr_psm_3": "Automatisch (Standard)",
        "ocr_psm_4": "Einzelne Spalte",
        "ocr_psm_5": "Vertikaler Block",
        "ocr_psm_6": "Einheitlicher Textblock",
        "ocr_psm_7": "Einzelne Textzeile",
        "ocr_psm_8": "Einzelnes Wort",
        "ocr_psm_11": "Rohes Bild (keine Layoutanalyse)",
        # ==================== OCR OEM-Modi (Engine-Modus) ====================
        "ocr_oem_0": "Legacy-Engine (schnell)",
        "ocr_oem_1": "LSTM-Engine (neuronal, genau)",
        "ocr_oem_2": "Legacy + LSTM kombiniert",
        "ocr_oem_3": "Standard (LSTM bevorzugt)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "OCR-Sprache(n)...",
        "ocr_language_title": "OCR-Sprache(n) auswählen",
        "ocr_language_instruction": "Wählen Sie die Sprache(n) für die Texterkennung (OCR).\nAchtung: Mehrere Sprachen gehen zu Lasten der Performance und Genauigkeit!\nDie besten Ergebnisse erzielen Sie, wenn Sie nur eine Sprache auswählen.",
        "ocr_language_predefined": "Vordefinierte Kombinationen",
        "ocr_language_custom": "Benutzerdefiniert...",
        "ocr_language_selected": "Ausgewählte OCR-Sprachen",
        "ocr_language_changed": "OCR-Sprache geändert auf {0}",
        "ocr_language_auto_detect": "Verfügbare Sprachen werden automatisch erkannt.",
        "ocr_language_none_found": "Keine Tesseract-Sprachdaten gefunden! Bitte installieren Sie Sprachpakete (z.B. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Benutzerdefinierte Sprachauswahl",
        "ocr_language_available": "Verfügbare Sprachen (installiert):",
        "ocr_language_select_hint": "Wählen Sie eine oder mehrere Sprachen aus:",
        "ocr_language_confirm": "Übernehmen",
        "ocr_language_reset": "Auf Standard zurücksetzen (deu+eng+vie)",
        "ocr_language_priorities": "Empfohlene Sprachen (vorinstalliert):",
        # Für den MultiLanguageDialog
        "select_all_languages": "Alle auswählen",
        "clear_all_languages": "Auswahl aufheben",
        "install_language_packs": "Fehlende Sprachpakete installieren...",
        "install_hint": "💡 Tipp: Nicht alle Sprachen sind auf Ihrem System installiert. Über diesen Button erhalten Sie Hilfe zur Installation.",
        "ocr_language_install_title": "Installation von Tesseract-Sprachpaketen",
        # OCR-Sprachfehler und Hilfetexte
        "ocr_missing_languages": "Fehlende OCR-Sprachpakete",
        "ocr_missing_languages_message": "Die folgenden ausgewählten Sprachen sind nicht auf Ihrem System installiert:\n\n{0}\n\nBitte installieren Sie die fehlenden Sprachpakete (siehe Hilfe unter 'Installationshilfe').\n\nMöchten Sie die Installationshilfe jetzt öffnen?",
        "ocr_missing_languages_voice": "Fehlende Sprachpakete. Bitte installieren Sie die fehlenden Sprachen.",
        "ocr_install_help_now": "Hilfe öffnen",
        "ocr_continue_anyway": "Trotzdem versuchen",
        "ocr_language_error_title": "OCR-Sprachfehler",
        "ocr_language_error_message": "Fehler bei der Texterkennung: {0}\n\nBitte überprüfen Sie Ihre OCR-Spracheinstellungen (Einstellungen → OCR-Sprache).",
        "ocr_install_help_button": "Installationshilfe",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Tesseract-Sprachpakete installieren</p>

        <p>Damit OCR in einer bestimmten Sprache funktioniert, müssen die entsprechenden Sprachdaten auf Ihrem System installiert sein. Folgen Sie der Anleitung für Ihr Betriebssystem:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Öffnen Sie das <strong>Terminal</strong> (Finder → Programme → Dienstprogramme → Terminal).</li>
        <li>Installieren Sie alle verfügbaren Sprachen mit:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (Das kann einige Minuten dauern.)</li>
        <li>Oder nur einzelne Sprachen (z. B. Vietnamesisch):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        Bei aktuellen Homebrew-Versionen muss ggf. die <code>*.traineddata</code> manuell heruntergeladen werden (siehe unten).</li>
        <li>Nach der Installation: Schließen Sie diesen Dialog und öffnen Sie die OCR-Sprachauswahl erneut – die neuen Sprachen erscheinen automatisch.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Öffnen Sie ein Terminal (Strg+Alt+T).</li>
        <li>Installieren Sie die gewünschte Sprache, z. B. für Vietnamesisch:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Wichtige Sprachcodes: <code>deu</code> (Deutsch), <code>eng</code> (Englisch), <code>vie</code> (Vietnamesisch), <code>spa</code> (Spanisch), <code>fra</code> (Französisch), <code>ita</code> (Italienisch), <code>nld</code> (Niederländisch), <code>fin</code> (Finnisch), <code>swe</code> (Schwedisch), <code>nor</code> (Norwegisch).</li>
        <li>Alle verfügbaren Pakete anzeigen:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (manuell)</p>
        <ol>
        <li>Laden Sie die gewünschten <code>*.traineddata</code>-Dateien herunter von:<br>
        <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (z. B. <code>vie.traineddata</code> für Vietnamesisch).</li>
        <li>Kopieren Sie die Dateien in den Tesseract-Sprachordner, üblicherweise:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (Bei individueller Installation entsprechend anpassen.)</li>
        <li>Starten Sie die Anwendung neu (oder öffnen Sie die OCR-Sprachauswahl erneut).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternative für alle Systeme</p>
        <ul>
        <li>Installieren Sie <strong>OCRmyPDF</strong> und <strong>Tesseract</strong> mit einem Paketmanager Ihrer Wahl. Die meisten Installationen enthalten bereits einige Standardsprachen (Englisch, Deutsch, Französisch).</li>
        <li>Fehlende Sprachen lassen sich jederzeit nachinstallieren – die OCR-Sprachauswahl listet nur die tatsächlich vorhandenen.</li>
        </ul>

        <hr>
        <p><b>✅ Nach der Installation:</b> Kein Neustart der Anwendung nötig – die neu hinzugekommenen Sprachen erscheinen sofort in der Liste.</p>
        <p><b>📖 Hilfe zu Sprachcodes:</b> Eine vollständige Liste finden Sie in der <a style="color:#E0E0E0;" href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">Tesseract-Dokumentation</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Noto Sans Schriftarten",
        "info_noto_font_voice": "Noto Sans Schriftarten Installationsanleitung",
        "btn_info_noto_font_install": "Font Info",
        # Anleitung

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ So installieren Sie die kostenlosen Noto-Schriften von Google</h2>

        <p>Die <strong>Noto-Schriften</strong> sind eine Open-Source-Schriftfamilie von Google. Ihr Ziel ist es, <em>"keine Tofu"</em> (also keine leeren Kästchen □) mehr zu sehen und wirklich jedes Zeichen aus dem Unicode-Standard korrekt darzustellen. Sie sind die ideale Ergänzung für Anwendungen, die Texte in vielen verschiedenen Sprachen anzeigen müssen.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Installation unter macOS</h3>

        <p><strong>Methode 1: Mit Homebrew (für Fortgeschrittene)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Methode 2: Über die "Schriftzugabe" (Empfohlen)</strong></p>

        <ol>
        <li>Laden Sie das offizielle Schriftpaket herunter:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP-Datei entpacken</li>
        <li>Dateien nach <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > User > Library > Fonts</code> kopieren</li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Installation unter Windows (10 & 11)</h3>

        <p><strong>Methode 1: Microsoft Store (Empfohlen)</strong><br>
        Suche nach "Google Noto Fonts" oder "Noto Sans" und klicke auf <strong>Installieren</strong>.</p>

        <p><strong>Methode 2: Manuelle Installation</strong></p>

        <ol>
        <li>Download:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>ZIP entpacken</li>
        <li>.ttf / .otf Dateien auswählen</li>
        <li>Rechtsklick → <strong>Installieren</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        oder<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\Name\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Installation unter Linux</h3>

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

        <p>Überprüfung:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Lesezeichen verwalten",
        "bookmark_add": "Lesezeichen hinzufügen",
        "bookmark_add_tooltip": "Aktuelle Seite als Lesezeichen speichern",
        "bookmark_remove": "Lesezeichen entfernen",
        "bookmark_remove_tooltip": "Das markierte Lesezeichen löschen",
        "bookmark_remove_all": "Alle entfernen",
        "bookmark_remove_all_tooltip": "Sämtliche Lesezeichen dieser PDF löschen",
        "bookmark_jump": "Zum Lesezeichen springen",
        "bookmark_jump_tooltip": "Zur ausgewählten Seite springen",
        "bookmark_name": "Name",
        "bookmark_page": "Seite",
        "bookmark_no_bookmarks": "Keine Lesezeichen vorhanden.\nKlicken Sie auf 'Hinzufügen', um die aktuelle Seite als Lesezeichen zu speichern.",
        "bookmark_added": "Lesezeichen für Seite {0} hinzugefügt: {1}",
        "bookmark_removed": "Lesezeichen entfernt: {0}",
        "bookmark_all_removed": "Alle Lesezeichen wurden entfernt.",
        "bookmark_name_default": "Seite {0}",
        "bookmark_name_prompt": "Name für das Lesezeichen:\n(längerer Text wird auf 50 Zeichen gekürzt)",
        "bookmark_name_prompt_title": "Lesezeichen-Name",
        "bookmark_confirm_remove_all": "Möchten Sie wirklich alle {0} Lesezeichen entfernen?",
        "menu_bookmarks": "Lesezeichen",
        "bookmark_manage": "Lesezeichen verwalten",
        "bookmark_next": "Nächstes Lesezeichen",
        "bookmark_prev": "Vorheriges Lesezeichen",
        "bookmark_page_display": "Seite {0}",
        "bookmark_exists": "Lesezeichen für diese Seite mit diesem Namen existiert bereits.",
        "bookmark_select_first": "Bitte wählen Sie zuerst ein Lesezeichen aus.",
        "bookmark_confirm_remove": "Möchten Sie das Lesezeichen 'Seite {0}: {1}' wirklich entfernen?",
        "bookmark_jumped_to": "Zu Lesezeichen '{0}' auf Seite {1} gesprungen.",
        "bookmark_jumped_to_voice": "Lesezeichen {0}, Seite {1}",
        "btn_close": "Schließen",
        # LESEZEICHEN KONTEXTMENÜ im Dialog
        "bookmark_list": "Ihre Lesezeichen",
        "bookmark_rename": "Lesezeichen umbenennen",
        "bookmark_rename_tooltip": "Den Namen des ausgewählten Lesezeichens ändern",
        "bookmark_rename_title": "Lesezeichen umbenennen",
        "bookmark_rename_prompt": "Neuer Name für Lesezeichen auf Seite {0}:\n(max. 50 Zeichen)",
        "bookmark_renamed": "Lesezeichen '{0}' wurde in '{1}' umbenannt.",
        "bookmark_item_tooltip": "Seite {0}: {1}\nDoppelklick zum Springen",
        "bookmark_name_exists_question": "Ein Lesezeichen mit dem Namen '{0}' existiert bereits auf dieser Seite.\nTrotzdem umbenennen?",
        # LESEZEICHEN KONTEXTMENÜ im Hauptfenster
        "context_bookmarks": "Lesezeichen",
        "context_bookmark_add_here": "Lesezeichen für diese Seite hinzufügen",
        "context_bookmarks_existing": "Vorhandene Lesezeichen:",
        "context_bookmarks_jump": "Springe zu Lesezeichen:",
        "context_bookmarks_none": "Keine Lesezeichen vorhanden",
        "context_bookmarks_clear_all": "Alle {0} Lesezeichen entfernen",
        # LESEZEICHEN SUCHLEISTE
        "bookmark_search_placeholder": "Lesezeichen suchen... (Name oder Seite)",
        "bookmark_search_results": "%d Lesezeichen gefunden für \"%s\"",
        "bookmark_no_search_results": "Keine Lesezeichen gefunden für \"%s\"",
        "bookmark_no_search_results_label": "Keine Ergebnisse für \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "PDF-Metadaten bearbeiten",
        "metadata_title": "Titel",
        "metadata_title_placeholder": "Dokumententitel",
        "metadata_title_tooltip": "Der Titel des Dokuments (wird in der Titelleiste angezeigt)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Name des Autors",
        "metadata_author_tooltip": "Der Ersteller des Dokuments",
        "metadata_subject": "Betreff",
        "metadata_subject_placeholder": "Betreff des Dokuments",
        "metadata_subject_tooltip": "Eine kurze Beschreibung des Inhalts",
        "metadata_keywords": "Stichwörter",
        "metadata_keywords_placeholder": "Stichwörter, durch Kommas getrennt",
        "metadata_keywords_tooltip": "Schlagwörter zur Kategorisierung des Dokuments",
        "metadata_creator": "Erzeuger",
        "metadata_creator_placeholder": "Anwendung, die das PDF erstellt hat",
        "metadata_creator_tooltip": "Die Software, mit der das Dokument erstellt wurde",
        "metadata_producer": "Produzent",
        "metadata_producer_placeholder": "Anwendung, die das PDF konvertiert hat",
        "metadata_producer_tooltip": "Die Software, die das PDF konvertiert hat",
        "metadata_creation_date": "Erstellungsdatum",
        "metadata_creation_date_tooltip": "Das Datum der Dokumenterstellung",
        "metadata_mod_date": "Änderungsdatum",
        "metadata_mod_date_tooltip": "Das Datum der letzten Änderung",
        "metadata_pdf_info": "📄 PDF-Informationen",
        "metadata_pages": "Seitenanzahl",
        "metadata_file_size": "Dateigröße",
        "metadata_pdf_version": "PDF-Version",
        "metadata_encrypted": "Verschlüsselt",
        "metadata_encrypted_yes": "Ja (passwortgeschützt)",
        "metadata_encrypted_no": "Nein",
        "metadata_reload": "📂 Aus PDF neu laden",
        "metadata_reset": "Änderungen verwerfen",
        "metadata_reloaded": "Metadaten wurden neu aus der PDF geladen.",
        "metadata_reset_done": "Alle Metadaten-Felder wurden zurückgesetzt.",
        "metadata_no_file": "Keine PDF-Datei geladen.",
        "metadata_save_error": "Fehler beim Speichern der Metadaten",
        "metadata_saved": "Metadaten wurden erfolgreich gespeichert.",
        "metadata_pdf_version_unknown": "PDF (unbekannt)",
        "metadata_saved_message": "Die Metadaten wurden erfolgreich gespeichert.",
        "metadata_saved_voice": "Metadaten gespeichert.",

        "metadata_custom": "🔧 Benutzerdefinierte Metadaten",
        "metadata_custom_placeholder": "{\n  \"mein_feld\": \"mein Wert\",\n  \"anderes_feld\": 123\n}",
        "metadata_custom_tooltip": "JSON-Format für benutzerdefinierte Metadaten (optional)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Vorlage \"{0}\" ausgewählt - Doppelklick zum Einfügen",
        "text_use_template": "Textbaustein verwenden",
        "text_type": "Typ",
        "text_search_templates": "Textbausteine durchsuchen...",

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

        <h3>📦 Was wird exportiert? (Übersicht)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Allgemeine Anwendungseinstellungen</span></li>
            <li class="detail">• Dark/Light Mode</li>
            <li class="detail">• Dark-Mode Invertierung für Bilder</li>
            <li class="detail">• Grau-Schwellwert</li>
            <li class="detail">• Sprache</li>
            <li class="detail">• Fenstergeometrie</li>
            <li class="detail">• Zoom-Modus</li>
            <li class="detail">• Navigation (Navbar sichtbar)</li>
            <li class="detail">• Sprachausgabe (ein/aus)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Backup-Einstellungen</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Dateibenennung (Timestamp, Separator, Suffixe)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Einstellungen für Einfügungen von</span></li>
            <li class="detail">• Signaturen</li>
            <li class="detail">• Text &amp; Textbausteinen</li>
            <li class="detail">• Kreuzen, Bilder und Formen</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">OCR-Einstellungen</span></li>
            <li class="detail">• Sprache</li>
            <li class="detail">• OCR erzwingen · Seitenmodus</li>
            <li class="detail">• Bildvorverarbeitung: Deskew, Clean, Oversampling</li>
            <li class="detail">• Anzahl paralleler Jobs</li>
            <li class="detail">• Invertierungsmodus</li>
            <li class="detail">• Grau-Schwellwert</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Lesezeichen</span></li>
            <li class="detail">• Alle Lesezeichen pro PDF-Datei (Seite, Name, Erstellzeit)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Passwort-Datenbank</span></li>
            <li class="detail">• Gespeicherte PDF-Passwörter (wahlweise verschlüsselt oder Klartext)</li>
            <li class="detail">• Master-Passwort-Hash (falls gesetzt)</li>
            <li class="detail">• Verifikationsdaten</li>
        </ul>

        <h4>⚠️ Wichtige Hinweise</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Beim Import:</strong>
            <ul>
                <li><span class="warning">➜ ALLE aktuellen Einstellungen werden vollständig überschrieben</span></li>
                <li>• Ein Neustart der Anwendung ist zwingend erforderlich</li>
                <li>• Vorhandene Signaturen, Textbausteine und Lesezeichen werden ersetzt</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Master-Passwort &amp; Exportmodus:</strong>
            <ul>
                <li>• Bei aktivem Master-Passwort können Sie wählen:</li>
                <li>  - <span style="color: #98FB98;"><strong>Entschlüsselt</strong></span> (Passwörter liegen im Klartext in der ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Verschlüsselt</strong></span> (nur mit Master-Passwort im Zielsystem lesbar)</li>
                <li>• Der Master-Passwort-Hash selbst wird <strong>immer</strong> verschlüsselt abgelegt</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Sicherheitshinweis:</strong>
            <ul>
                <li>• Die exportierte ZIP-Datei enthält vertrauliche Daten (<strong>Passwörter, Lesezeichen, Signaturen</strong>)</li>
                <li>• Bitte sicher aufbewahren (z.B. verschlüsselter USB-Stick, Passwort-Manager)</li>
                <li>• Bei Verlust der Datei sind gespeicherte PDF-Passwörter unwiederbringlich verloren</li>
            </ul>
        </div>

        <h4>📁 Exportformat</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Die Einstellungen werden in einer einzigen ZIP-Datei gespeichert:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Diese ZIP enthält die vollständige <code>settings.json</code> (aus Ihrer Konfiguration) sowie ggf. eingebettete Signatur-Bilddateien und verschlüsselte Passwörter.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Unterschriften - Anleitung",
        'signature_guide_html': """
        📝 <strong>Unterschriften - Kurzanleitung</strong><br>
        <ul>
        <li>Master Passwort einrichten</li>
        <li>Unterschriften im Menü <em>Einstellungen</em> konfigurieren (Größe, Zeitstempel, …)</li>
        <li>Einfügen mit <strong>RECHTSKLICK</strong> an der gewünschten Position (Master Passwort einmalig pro Sitzung erforderlich)</li>
        <li>Signatur mit der Maus oder Pfeiltasten verschieben</li>
        <li>Mehrere Signaturen nacheinander einfügen</li>
        <li>Jede Signatur individuell anpassen</li>
        <li>Einzelne Signatur verwerfen</li>
        <li>Alle Signaturen auf einmal speichern / verwerfen</li>
        <li>Alternativ kann auch die Menüleiste genutzt werden.</li>
        </ul>
        """,
        'signature_guide_voice': "Kurzanleitung für Unterschriften. Master Passwort einrichten. Unterschriften in den Einstellungen konfigurieren. Einfügen mit Rechtsklick.",

        'image_guide_title': "Bilder einfügen - Anleitung",
        'image_guide_html': """
        📷 <strong>Bilder in PDF einfügen - Kurzanleitung</strong><br>
        <ol>
        <li>Rechtsklick auf die gewünschte Position</li>
        <li><em>„Bild einfügen“</em> → Bild auswählen</li>
        <li>Bild positionieren: Ziehen mit der Maus</li>
        <li>Größe anpassen: Ziehen an den Ecken/Kanten</li>
        <li>Seitenverhältnis beibehalten: Taste <strong>[A]</strong></li>
        <li>Weitere Anpassungen: Rechtsklick auf das Bild</li>
        </ol>
        <p><strong>Tipp:</strong> Im Kontextmenü können Sie die Einstellungen anpassen.</p>
        """,
        'image_guide_voice': "Kurzanleitung für Bilder. Rechtsklick, Bild einfügen, auswählen. Positionieren mit Maus, Größe anpassen an Ecken. Seitenverhältnis mit Taste A.",

        'form_guide_title': "Formen einfügen - Anleitung",
        'form_guide_html': """
        📐 <strong>Formen in PDF einfügen - Kurzanleitung</strong><br>
        <ol>
        <li>Form-Typ auswählen (Rechteck, Ellipse, Linie, Pfeil)</li>
        <li>Auf Position klicken:
            <ul>
            <li>Bei Rechteck/Ellipse: Ein Klick platziert die Form</li>
            <li>Bei Linie/Pfeil: Zwei Klicks für Start- und Endpunkt</li>
            </ul>
        </li>
        <li>Form positionieren: Ziehen mit der Maus</li>
        <li>Größe anpassen: Ziehen an den Ecken/Kanten</li>
        <li>Form speichern: <strong>Enter</strong></li>
        <li>Form verwerfen: <strong>ESC</strong></li>
        <li>Weitere Anpassungen: Rechtsklick auf die Form</li>
        </ol>
        <p><strong>Tipp:</strong> Im Kontextmenü können Sie die Einstellungen anpassen.</p>
        """,
        'form_guide_voice': "Kurzanleitung für Formen. Form-Typ auswählen. Bei Rechteck oder Ellipse einmal klicken, bei Linie oder Pfeil zweimal klicken. Positionieren mit Maus, Größe anpassen an Ecken. Speichern mit Enter, verwerfen mit Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "vorheriger",
        "btn_next_result": "nächster",
        "ocr_text_window": "OCR Textfenster",
        "bookmark_existing": "Ovorhandene Lesezeichen",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "OCR Vergleich Mac - Windows",
        'ocr_method_mac_win_title': "OCR Unterschiede Mac und Windows",
        'ocr_method_mac_win_voice': "Mac ist besser",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – Unterschiede zwischen macOS und Windows</strong></p>

        <p><strong>macOS (empfohlen)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Ergebnis:</p>
        <ul>
        <li>Eine durchsuchbare PDF mit eingebettetem Text, die weitgehend das originale Layout bewahrt.</li>
        </ul>
        <p>Vorteile:</p>
        <ul>
        <li>Ausgezeichnete Qualität der Texterkennung (auch bei krummen Seiten).</li>
        <li>Beibehaltung von Vektorgrafiken und Schriftarten.</li>
        <li>GUI-Fortschrittsbalken über subprocess-Auswertung.</li>
        <li>Volle Kontrolle über alle OCR-Parameter (Deskew, Clean, Oversample, Optimierung).</li>
        <li>Die Textsuche ist direkt im Hauptfenster (PDF Ansicht) verfügbar.</li>
        </ul>
        <p>Nachteile:</p>
        <ul>
        <li>Benötigt zusätzliche System‑Tools (ocrmypdf, Ghostscript, unpaper, pngquant – im App Bundle enthalten).</li>
        <li>Komplexere Fehlerbehandlung (Deadlocks, Timeouts).</li>
        </ul>

        <p><strong>Windows (stabile Alternative)</strong></p>
        <p>Tool:</p>
        <ul>
        <li>pytesseract (direkte Anbindung an Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Ergebnis:</p>
        <ul>
        <li>Eine durchsuchbare PDF, die optisch einer Bild‑PDF entspricht, aber durch den transparenten Text durchsuchbar ist.</li>
        </ul>
        <p>Vorteile:</p>
        <ul>
        <li>Da fallen mir gerade keine ein.</li>
        </ul>
        <p>Nachteile:</p>
        <ul>
        <li>Die PDF ist im Wesentlichen ein Bild mit unsichtbarem Text; das Layout kann bei komplexen Dokumenten (Spalten, Tabellen) leicht abweichen.</li>
        <li>Keine automatische Schräglagenkorrektur (--deskew) oder Bildbereinigung (--clean).</li>
        <li>Der GUI-Fortschrittsbalken wird nur grob über die Anzahl der verarbeiteten Seiten aktualisiert.</li>
        <li>Die OCR-Geschwindigkeit ist geringfügig langsamer (da jede Seite einzeln verarbeitet wird).</li>
        <li>Die Textsuche wird auf das OCR Textfenster umgeleitet.</li>
        </ul>

        <p><strong>Gemeinsamkeiten</strong></p>
        <ul>
        <li>Beide Verfahren erzeugen eine durchsuchbare PDF im selben Verzeichnis wie die Quelldatei.</li>
        <li>Die OCR‑Einstellungen (Sprache, DPI, Seiten‑Segmentierungsmodus, OCR‑Engine‑Modus) können über den OCRSettingsDialog konfiguriert werden und wirken in beiden Implementierungen.</li>
        </ul>

        <p><strong>Empfehlung:</strong></p>
        <ul>
        <li>macOS: Die ocrmypdf-Binary liefert die besten Ergebnisse – Kaufen Sie sich einen Mac und nutzen Sie die Version (PDFDarkView für Mac`s mit Apple Silicon oder Intel Chip). Die OCR Ergebnisse sind besser als unter Windows!</li>
        <li>Windows: Verwenden Sie die pytesseract-Lösung. Sie ist stabil und liefert für die meisten Dokumente eine völlig ausreichende Qualität.</li>
        </ul>

        <p><strong>Wichtiger Hinweis:</strong></p>
        <ul>
        <li>Beide Versionen sind vollständig in die Benutzeroberfläche integriert – der Benutzer merkt keinen Unterschied.</li>
        <li>Die Entscheidung, welche OCR-Engine verwendet wird, trifft das Programm automatisch basierend auf dem Betriebssystem.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Signatur erstellen (aus Scan)",
        "signature_create_title": "Gescannte Unterschrift auswählen (PDF/Bild)",
        "image_pdf_filter": "Bilder und PDF",
        "signature_pdf_empty": "Die PDF enthält keine Seiten.",
        "signature_created_success": "Signatur erfolgreich erstellt: {0}",
        "signature_create_error": "Fehler beim Erstellen der Signatur:\n{0}",
        "rembg_missing": "rembg ist nicht installiert.\nBitte installiere: pip install rembg\nFehler: {0}",
        "signature_name_title": "Dateiname für die Signatur",
        "signature_name_message": "Bitte gib einen Dateinamen für die neue Signatur ein (wird als PNG mit transparentem Hintergrund gespeichert):",
        "signature_name_label": "Dateiname:",
        "signature_name_voice": "Dateiname für die Signatur eingeben",
        "signature_processing": "Verarbeitung läuft...",
        "signature_creation_title": "Signatur wird erstellt",
        "signature_overwrite_warning": "Die Datei '{0}' existiert bereits. Überschreiben?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"PDF für Signatur vorbereiten",
        "signature_prepare_instruction":"Bitte wählen Sie ein PDF aus, das auf einer einzelnen Seite eine eingescannte Unterschrift enthält.\n\nOptimale Erkennung erreichen Sie, wenn:\n• Die Unterschrift mit schwarzer Tinte (Kugelschreiber oder Fineliner) auf weißem Papier geschrieben ist.\n• Die Unterschrift sich im oberen Drittel der ansonsten leeren A4 Seite befindet.\n• Das PDF mit mindestens 300 dpi gescannt wurde.\n• Die Unterschrift klar und nicht zu dünn ist.\n• Keine störenden Hintergrundmuster oder Linien vorhanden sind.",
        "signature_prepare_voice":"Bitte wählen Sie ein PDF mit einer eingescannten Unterschrift aus. Achten Sie auf gute Qualität und Kontrast.",
        "sig_thickness_label":"Linienstärke:",
        "sig_thickness_normal":"Normal (dünn)",
        "sig_thickness_bold":"Kräftig (empfohlen)",
        "sig_thickness_very_bold":"Sehr kräftig",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "GUI und OCR Sprachen hinzufügen - Anleitung",
        'language_guide_title': "GUI und OCR Sprachen hinzufügen",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Laden Sie die gewünschte Übersetzungsdatei <code>translations_xy.py</code> von<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        herunter und legen Sie sie in folgendes Verzeichnis:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Öffnen Sie Ihren Webbrowser.</li>
        <li>Gehen Sie zu: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Suchen Sie am rechten Bildschirmrand nach "Releases" und wählen Sie das mit <strong>"latest"</strong> gekennzeichnete.</li>
        <li>Laden Sie auf der folgenden Release-Seite ganz unten die Datei <code>Source Code.zip</code> herunter.</li>
        <li>Entpacken Sie die ZIP-Datei.</li>
        <li>Suchen Sie im entpackten Ordner alle Sprachdateien, die Sie benötigen, und kopieren Sie sie in das Verzeichnis:<br/>
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
        "menu_watermark":"Wasserzeichen einfügen",
        "fullpage_text_watermark_title":"Text als Wasserzeichen",
        "fullpage_image_watermark_title":"Bild als Wasserzeichen",
        "filename_with_watermark":"_mit_Wasserzeichen",

        # ===== DIALOG TEXTE =====
        "watermark_text":"Text:",
        "watermark_text_placeholder":"Ihr Wasserzeichen-Text...",
        "watermark_font_family":"Schriftart:",
        "watermark_font_size":"Schriftgröße:",
        "watermark_format":"Formatierung:",
        "watermark_bold":"Fett",
        "watermark_italic":"Kursiv",
        "watermark_color":"Farbe:",
        "watermark_choose_color":"Farbe wählen...",
        "watermark_opacity":"Deckkraft / Transparenz:",
        "watermark_direction":"Leserichtung:",
        "watermark_direction_l_r":"Links → Rechts",
        "watermark_direction_bl_tr":"Unten links → Oben rechts",
        "watermark_direction_tl_br":"Oben links → Unten",
        "watermark_direction_b_t":"Unten → Oben",
        "watermark_direction_t_b":"Oben → Unten",
        "watermark_preview":"Vorschau:",
        "watermark_preview_sample":"Beispieltext",
        "watermark_empty_text":"Bitte geben Sie einen Text ein.",
        "watermark_applied":"Wasserzeichen wurde auf alle Seiten angewendet.",
        "watermark_saved":"Wasserzeichen gespeichert.",

        # ===== DIALOG BILD =====
        "image_scale":"Größe:",
        "image_preview":"Bildvorschau:",
        "no_image_selected":"Kein Bild ausgewählt",
        "browse":"Durchsuchen...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI (REDAKTION)
        # ============================================
        "menu_redact": "Auslöschungen",
        "redact_add_black": "Auslöschung (schwarz)",
        "redact_add_white": "Auslöschung (weiß / radieren)",
        "redact_added_black": "Schwarze Auslöschung hinzugefügt",
        "redact_added_white": "Weiße Auslöschung hinzugefügt",
        "redact_apply_all": "Alle Auslöschungen anwenden und speichern",
        "redact_discard_all": "Alle Auslöschungen verwerfen",
        "redact_discard": "Diese Auslöschung verwerfen",
        "no_redactions": "Keine Auslöschungen vorhanden",
        "redact_confirm_title": "Auslöschungen dauerhaft anwenden",
        "redact_confirm_message": "Achtung: Die markierten Bereiche werden unwiderruflich gelöscht (schwarz oder weiß).\nEin Backup wird erstellt (falls aktiviert).\n\nFortfahren?",
        "redact_apply": "Ja, jetzt auslöschen",
        "redact_saved": "{0} Auslöschung(en) erfolgreich angewendet und gespeichert.",
        "redact_saved_voice": "{0} Auslöschung(en) angewendet",
        "redact_error": "Fehler beim Auslöschen",
        "filename_redacted":"_mit_Auslöschung",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        # Dialog-Titel und Beschriftungen
        'page_numbers_title': 'Seitenzahlen einfügen',
        'page_numbers_format': 'Zahlenformat:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabisch)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (römisch klein)',
        'page_numbers_format_roman_upper': 'I, II, III ... (römisch groß)',
        'page_numbers_format_letter': 'A, B, C ... (Buchstaben)',
        'page_numbers_format_custom': 'Benutzerdefiniert',
        'page_numbers_custom_pattern': 'Muster:',
        'page_numbers_custom_placeholder': 'z.B. "Seite {nummer}" oder "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Verwende {nummer} für die aktuelle Seitenzahl und {total} für die Gesamtzahl',
        'page_numbers_position': 'Position:',
        'page_numbers_pos_tl': 'Oben links',
        'page_numbers_pos_tc': 'Oben mitte',
        'page_numbers_pos_tr': 'Oben rechts',
        'page_numbers_pos_ml': 'Mitte links',
        'page_numbers_pos_mc': 'Zentriert',
        'page_numbers_pos_mr': 'Mitte rechts',
        'page_numbers_pos_bl': 'Unten links',
        'page_numbers_pos_bc': 'Unten mitte',
        'page_numbers_pos_br': 'Unten rechts',
        'page_numbers_margins': 'Abstände:',
        'page_numbers_margin_x': 'Horizontaler Abstand:',
        'page_numbers_margin_y': 'Vertikaler Abstand:',
        'page_numbers_range': 'Seitenbereich:',
        'page_numbers_all_pages': 'Alle Seiten',
        'page_numbers_custom_range': 'Benutzerdefinierter Bereich',
        'page_numbers_from': 'Von:',
        'page_numbers_to': 'Bis:',
        'page_numbers_progress': 'Füge Seitenzahlen ein...',
        'page_numbers_start': 'Starte Seitenzahlen-Einfügung...',
        'page_numbers_cancel': 'Seitenzahlen-Einfügung abgebrochen',
        'page_numbers_success': 'Seitenzahlen wurden erfolgreich hinzugefügt.\n\nMöchten Sie die neue PDF öffnen?\n\n{0}',
        'page_numbers_complete': 'Seitenzahlen wurden hinzugefügt',
        'page_numbers_error_format': 'Fehler beim Einfügen der Seitenzahlen: {0}',
        # Zusätzliche Übersetzungen für den erweiterten Dialog
        'page_numbers_content_type': 'Inhaltstyp:',
        'page_numbers_tab_simple': 'Einfache Zahl',
        'page_numbers_tab_range': 'Seite X von Y',
        'page_numbers_tab_date': 'Datum',
        'page_numbers_tab_custom': 'Freitext',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktuell}/{gesamt}',
        'page_numbers_range_long': 'Seite {aktuell} von {gesamt}',
        'page_numbers_range_custom': 'Benutzerdefiniert',
        'page_numbers_range_placeholder': 'z.B. "Seite {aktuell} / {gesamt}"',
        'page_numbers_date_format': 'Datumsformat:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1. Januar 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Benutzerdefiniert',
        'page_numbers_date_placeholder': 'z.B. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Position:',
        'page_numbers_date_before': 'Datum vor Seitenzahl',
        'page_numbers_date_after': 'Datum nach Seitenzahl',
        'page_numbers_date_only': 'Nur Datum (keine Seitenzahl)',
        'page_numbers_custom_text': 'Benutzerdefinierter Text:',
        'page_numbers_custom_placeholder_text': 'Verwende {seite} für die Seitenzahl und {gesamt} für die Gesamtzahl\nz.B. "Vertraulich - Seite {seite}" oder "{seite} von {gesamt}"',
        "filename_with_page_number":"_mit_Seitenzahl",
        "filename_with_page_declaration":"_mit_Seitenangabe",
        "filename_with_pagenumber":"_mit_Seitenzahl",
        "filename_with_date":"_mit_Datum",
        "filename_with_my_page_declaration":"_mit_eigener_Seitenangabe",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Ungespeicherte Änderungen",
        "unsaved_changes_message_darkmode": "Es sind noch nicht gespeicherte Einfügungen vorhanden.\nMöchten Sie diese vor dem Umschalten speichern?",
        "save_and_switch": "Speichern und umschalten",
        "discard_and_switch": "Jetzt umschalten",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        # Export Images Dialog
        'export_images_title': 'Seiten als Bilder exportieren',
        'export_images_menu': 'Als Bilder exportieren (PNG/JPEG)',
        'export_images_format': 'Bildformat:',
        'export_images_dpi': 'Auflösung (DPI):',
        'export_images_quality': 'JPEG-Qualität:',
        'export_images_range': 'Seitenbereich:',
        'export_images_all_pages': 'Alle Seiten',
        'export_images_custom_range': 'Benutzerdefinierter Bereich',
        'export_images_from': 'Von:',
        'export_images_to': 'Bis:',
        'export_images_options': 'Optionen:',
        'export_images_single_files': 'Jede Seite als einzelne Datei',
        'export_images_subfolder': 'In Unterordner exportieren',
        'export_images_subfolder_info': 'In Unterordner "PDFname_bilder"',
        'export_images_same_folder': 'Im selben Ordner wie die PDF',
        'export_images_apply_darkmode': 'PDFDarkView-Einstellungen anwenden (Dark Mode)',
        'export_images_target_folder': 'Zielordner:',
        'export_images_browse': 'Durchsuchen...',
        'export_images_preview': 'Vorschau:',
        'export_images_preview_info': 'Wählen Sie die Einstellungen für den Export',
        'export_images_preview_info_detail': '{0} Seiten als {1}\nAuflösung: {2} DPI\nDateiname: {3}\n{4}',
        'export_images_select_folder': 'Zielordner auswählen',
        'export_images_start': 'Starte Bild-Export...',
        'export_images_progress': 'Exportiere Bilder...',
        'export_images_saving': 'Speichere Seite {0} von {1}...',
        'export_images_success': 'Erfolgreich exportiert!\n\n{0} Bilder wurden gespeichert in:\n{1}',
        'export_images_complete': 'Bild-Export abgeschlossen',
        'export_images_open_folder': '📁 Ordner öffnen',
        'export_images_cancel': 'Bild-Export abgebrochen',
        'export_images_error_format': 'Fehler beim Export der Bilder: {0}',
        'export_images_pdf2image_missing': 'Die Bibliothek "pdf2image" ist nicht installiert.\n\nBitte installieren Sie sie mit:\npip install pdf2image\n\nFür Windows benötigen Sie auch Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        # PDF/A Dialog
        'pdfa_title': 'PDF/A-Konvertierung für Langzeitarchivierung',
        'pdfa_menu': 'PDF/A-Konvertierung (archivtauglich)',
        'pdfa_info': 'Konvertiert die PDF in ein PDF/A-Format.\n\nPDF/A ist speziell für die Langzeitarchivierung entwickelt und stellt sicher, dass das Dokument auch in Zukunft korrekt dargestellt wird.',
        'pdfa_standard': 'PDF/A-Standard:',
        'pdfa_standard_select': 'Version:',
        'pdfa_1': 'PDF/A-1 (einfach, breit kompatibel)',
        'pdfa_2': 'PDF/A-2 (modern, bessere Komprimierung)',
        'pdfa_3': 'PDF/A-3 (neueste Version, erlaubt Anhänge)',
        'pdfa_standards_explanation': '📖 Erklärung der Standards:\n\n'
            '• PDF/A-1: Grundlegend, kompatibel mit älteren Systemen (ca. 2005)\n'
            '• PDF/A-2: Moderner, bessere Komprimierung, Transparenz-Unterstützung (ca. 2011)\n'
            '• PDF/A-3: Neueste Version, erlaubt das Einbetten von Dateianhängen (ca. 2013)\n\n'
            'Empfehlung: PDF/A-2 ist ein guter Kompromiss zwischen Kompatibilität und modernen Funktionen.',
        'pdfa_options': 'Optionen:',
        'pdfa_compress_enable': 'PDF komprimieren (kleinere Datei)',
        'pdfa_metadata_preserve': 'Metadaten erhalten (Titel, Autor, etc.)',
        'pdfa_target_folder': 'Zielordner:',
        'pdfa_browse': 'Durchsuchen...',
        'pdfa_select_folder': 'Zielordner auswählen',
        'pdfa_ocr_info_unknown': '🔍 Konnte Textinhalt nicht prüfen.',
        'pdfa_ocr_info_not_needed': '✅ Text vorhanden - OCR ist nicht erforderlich.\nPDF/A kann direkt erstellt werden.',
        'pdfa_ocr_info_recommended': '⚠️ Kein ausreichender Text gefunden.\n\nFür durchsuchbare PDFs empfehlen wir vorher OCR durchzuführen.\nHinweis: PDF/A funktioniert auch ohne OCR - der Text ist dann aber nicht durchsuchbar.',
        'pdfa_ocr_info_error': '❌ Fehler beim Prüfen: {0}',
        'pdfa_start': 'Starte PDF/A-Konvertierung...',
        'pdfa_progress': 'PDF/A-Konvertierung läuft...',
        'pdfa_success': 'PDF/A-Konvertierung erfolgreich!\n\nGespeichert als:\n{0}\n\nMöchten Sie die neue PDF öffnen?',
        'pdfa_complete': 'PDF/A-Konvertierung abgeschlossen',
        'pdfa_cancel': 'PDF/A-Konvertierung abgebrochen',
        'pdfa_error_format': 'Fehler bei PDF/A-Konvertierung:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Die Bibliothek "ocrmypdf" ist nicht installiert.\n\nBitte installieren Sie sie mit:\npip install ocrmypdf',
        'btn_convert': 'Konvertierung',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        ### ------------------------------------
        ### 95. OPTIMIEREN (KOMPIMIEREN)
        ### ------------------------------------
        # ===== PDF OPTIMIEREN =====
        'optimize_title': 'PDF optimieren (Dateigröße reduzieren)',
        'optimize_menu': 'PDF optimieren (Dateigröße)',
        'optimize_info': 'Reduziert die Dateigröße der PDF durch verschiedene Optimierungsmethoden.\n\nJe höher die Komprimierungsstufe, desto kleiner wird die Datei - bei möglichem Qualitätsverlust bei Bildern.',
        'optimize_level': 'Komprimierungsstufe:',
        'optimize_level_low': 'Niedrig (schnell, geringe Einsparung)',
        'optimize_level_medium': 'Mittel (guter Kompromiss)',
        'optimize_level_high': 'Hoch (starke Einsparung)',
        'optimize_level_maximum': 'Maximum (maximale Einsparung, langsam)',
        'optimize_level_explanation': 'Empfehlung: "Mittel" ist ein guter Kompromiss zwischen Geschwindigkeit und Dateigröße.',
        'optimize_options': 'Optionen:',
        'optimize_compress_images': 'Bilder komprimieren (JPEG-Qualität reduzieren)',
        'optimize_clean_objects': 'Unbenutzte Objekte entfernen',
        'optimize_preserve_metadata': 'Metadaten erhalten (Titel, Autor, etc.)',
        'optimize_image_quality': 'Bildqualität:',
        'optimize_range': 'Seitenbereich:',
        'optimize_all_pages': 'Alle Seiten',
        'optimize_custom_range': 'Benutzerdefinierter Bereich',
        'optimize_from': 'Von:',
        'optimize_to': 'Bis:',
        'optimize_target_folder': 'Zielordner:',
        'optimize_browse': 'Durchsuchen...',
        'optimize_select_folder': 'Zielordner auswählen',
        'optimize_info_box': 'Informationen',
        'optimize_info_text': 'Die Optimierung kann bei großen PDFs mehrere Minuten dauern.\n\nBilder werden mit reduzierter Qualität gespeichert, was die Dateigröße erheblich reduzieren kann.',
        'optimize_start': 'Starte PDF-Optimierung...',
        'optimize_progress': 'PDF wird optimiert...',
        'optimize_cancel': 'PDF-Optimierung abgebrochen',
        'optimize_complete': 'PDF-Optimierung abgeschlossen',
        'optimize_error_format': 'Fehler bei PDF-Optimierung:\n\n{0}',
        # Erfolgsmeldungen (mit Platzhaltern)
        'optimize_success_message': 'PDF-Optimierung erfolgreich!\n\nGespeichert als:\n{0}\n\nVorher:  {1}\nNachher: {2}\nErsparnis: {3:.1f}%\n\n{4}\n\nMöchten Sie die optimierte PDF öffnen?',
        'optimize_success_message_no_size': 'PDF-Optimierung erfolgreich!\n\nGespeichert als:\n{0}\n\nGrößeninformation nicht verfügbar.\n\nMöchten Sie die optimierte PDF öffnen?',
        # Ergebnis-Texte
        'optimize_result_positive': 'Die Datei wurde um {0:.1f}% verkleinert.',
        'optimize_result_zero': 'Keine Veränderung der Dateigröße.',
        'optimize_result_negative': 'Die Datei ist um {0:.1f}% größer geworden.\nDie Optimierung wurde übersprungen, die Originaldatei wurde beibehalten.',
        'btn_optimize': 'Optimierung starten',
        # Dateinamen-Suffixe
        'filename_optimize_low_suffix': '_optimiert_niedrig',
        'filename_optimize_medium_suffix': '_optimiert',
        'filename_optimize_high_suffix': '_optimiert_hoch',
        'filename_optimize_maximum_suffix': '_optimiert_max',

        ### ------------------------------------
        ### 96. ZUSCHNEIDEN CROPPING
        ### ------------------------------------
        # ===== PDF ZUSCHNEIDEN =====
        # Crop Dialog
        'crop_title': 'PDF zuschneiden',
        'crop_menu': 'PDF zuschneiden (Crop)',
        'crop_range': 'Anwenden auf:',
        'crop_all_pages': 'Alle Seiten',
        'crop_current_page': 'Nur aktuelle Seite',
        'crop_values': 'Crop-Werte (in Punkten):',
        'crop_left': 'Links:',
        'crop_right': 'Rechts:',
        'crop_top': 'Oben:',
        'crop_bottom': 'Unten:',
        'crop_presets': 'Voreinstellungen:',
        'crop_preset_white': 'Weiße Ränder erkennen',
        'crop_reset': 'Zurücksetzen',
        'crop_mouse_hint': '🖱️ Ziehen Sie ein Rechteck auf, um den Bereich grob auszuwählen.\nAnschließend können Sie die Werte in den SpinBoxen exakt nachjustieren.\nEin manuelles Nachjustieren mit der Maus ist nicht möglich.',
        'crop_apply': 'Zuschneiden',
        'crop_scope_all': 'Alle Seiten',
        'crop_scope_current': 'Aktuelle Seite',
        'crop_new_size': 'Neue Größe: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Kein PDF geladen',
        'crop_preview_error': 'Fehler beim Laden der Vorschau',
        'crop_start': 'Starte Zuschneiden...',
        'crop_progress': 'PDF wird zugeschnitten...',
        'crop_success': 'PDF erfolgreich zugeschnitten!\n\nGespeichert als:\n{0}\n\nMöchten Sie die zugeschnittene PDF öffnen?',
        'crop_complete': 'Zuschneiden abgeschlossen',
        'crop_cancel': 'Zuschneiden abgebrochen',
        'crop_error_format': 'Fehler beim Zuschneiden:\n\n{0}',
        'filename_crop_suffix': '_zugeschnitten',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        # ===== PDF GLÄTTEN =====
        'flatten_title': 'PDF glätten (Flatten)',
        'flatten_menu': 'PDF glätten (Flatten)',
        'flatten_info': 'Das Glätten (Flatten) einer PDF "brennt" alle bearbeitbaren Elemente in den Seiteninhalt ein.\n\nDanach sind Formularfelder, Anmerkungen, Texte, Kreuze, Signaturen, Bilder und Formen nicht mehr einzeln editierbar.',
        'flatten_explanation_title': '📖 Wofür ist das gut?',
        'flatten_explanation_text': 'Das Glätten wird in folgenden Situationen benötigt:\n\n'
            '• 📄 Sie möchten das Dokument für den Druck vorbereiten\n'
            '• 🔒 Sie möchten verhindern, dass jemand Formularfelder ändert\n'
            '• 📎 Sie möchten Anmerkungen und Kommentare "fest" in das Dokument einbetten\n'
            '• 🖼️ Sie möchten eingefügte Texte, Kreuze, Signaturen, Bilder und Formen dauerhaft im Dokument verankern\n'
            '• 📦 Sie möchten die Datei für die Archivierung vorbereiten\n\n'
            'Das Glätten macht die PDF kleiner und verhindert, dass Elemente versehentlich verschoben oder gelöscht werden.',
        'flatten_what_title': 'Was wird geglättet?',
        'flatten_what_list': '• ✅ Formularfelder (Textfelder, Checkboxen, Buttons)\n'
            '• ✅ Anmerkungen (Kommentare, Hervorhebungen, Notizen)\n'
            '• ✅ Overlays (Texte, Kreuze, Signaturen, Bilder, Formen)',
        'flatten_options': 'Optionen:',
        'flatten_forms': 'Formularfelder glätten',
        'flatten_annotations': 'Anmerkungen glätten',
        'flatten_overlays': 'Overlays glätten (Texte, Kreuze, Signaturen, Bilder, Formen)',
        'flatten_target_folder': 'Zielordner:',
        'flatten_browse': 'Durchsuchen...',
        'flatten_select_folder': 'Zielordner auswählen',
        'flatten_warning': '⚠️ Wichtig: Das Glätten ist ein irreversibler Vorgang!\n\n'
            'Nach dem Glätten können bearbeitbare Elemente nicht mehr einzeln verändert oder gelöscht werden.\n'
            'Erstellen Sie bei Bedarf vorher ein Backup.',
        'flatten_apply': 'Glätten',
        'flatten_start': 'Starte Glätten...',
        'flatten_progress': 'PDF wird geglättet...',
        'flatten_success': 'PDF erfolgreich geglättet!\n\nGespeichert als:\n{0}\n\nMöchten Sie die geglättete PDF öffnen?',
        'flatten_complete': 'Glätten abgeschlossen',
        'flatten_cancel': 'Glätten abgebrochen',
        'flatten_error_format': 'Fehler beim Glätten:\n\n{0}',
        'filename_flatten_suffix': '_geglättet',

        ### ------------------------------------
        ### 98. PDF ÜBEREINANDERLEGEN OVERLAY
        ### ------------------------------------
        'overlay_title': 'PDF übereinanderlegen (Overlay)',
        'overlay_menu': 'PDF übereinanderlegen (Overlay)',
        'overlay_info': 'Legt eine PDF (Overlay) über eine andere PDF.\n\nDie Overlay-PDF wird auf die Basis-PDF gelegt. Das ist nützlich für Wasserzeichen, Logos, Briefköpfe oder Stempel.',
        'overlay_explanation_title': '📖 Wofür ist das gut?',
        'overlay_explanation_text': 'Das Überlagern wird in folgenden Situationen benötigt:\n\n'
            '• 🏢 Ein Firmenlogo als Wasserzeichen auf jede Seite legen\n'
            '• 📄 Einen Briefkopf auf eine leere PDF legen\n'
            '• 🖊️ Ein Stempel-Overlay auf ein Dokument legen\n'
            '• 🔖 Ein Wasserzeichen auf alle Seiten legen\n'
            '• 📑 Ein Formular-Overlay auf eine Vorlage legen',
        'overlay_type': 'Overlay-Typ:',
        'overlay_type_fullpage': 'Ganze Seite (deckend)',
        'overlay_type_transparent': 'Ganze Seite (transparent - empfohlen)',
        'overlay_type_stamp': 'Stempel (positionierbar)',
        'overlay_type_info_fullpage': '📄 Die Overlay-PDF wird exakt über die gesamte Seite gelegt.\nDer weiße Hintergrund kann entfernt werden, sodass nur der Inhalt sichtbar bleibt.',
        'overlay_type_info_transparent': '🔍 Die Overlay-PDF wird mit transparentem Hintergrund über die gesamte Seite gelegt.\nDer weiße Hintergrund wird automatisch entfernt - ideal für Wasserzeichen und Logos!',
        'overlay_type_info_stamp': '🖊️ Die Overlay-PDF wird als Stempel positioniert und skaliert.\nPerfekt für Logos, Stempel oder Unterschriften an bestimmten Positionen.',
        'overlay_remove_background': 'Weißen Hintergrund entfernen:',
        'overlay_remove_background_enable': 'Weißen Hintergrund der Overlay-PDF entfernen (macht das Overlay transparent)',
        'overlay_remove_background_tooltip': 'Entfernt weiße Bereiche aus der Overlay-PDF, sodass der darunterliegende Text sichtbar wird.',
        'overlay_threshold': 'Schwellwert:',
        'overlay_threshold_hint': '(1-254, höher = mehr Weiß wird entfernt)',
        'overlay_select_file': 'Overlay-PDF auswählen:',
        'overlay_file_placeholder': 'Bitte wählen Sie eine PDF-Datei für das Overlay',
        'overlay_browse': 'Durchsuchen...',
        'overlay_select_overlay': 'Overlay-PDF auswählen',
        'overlay_range': 'Seitenbereich:',
        'overlay_all_pages': 'Alle Seiten',
        'overlay_custom_range': 'Benutzerdefinierter Bereich',
        'overlay_from': 'Von:',
        'overlay_to': 'Bis:',
        'overlay_position': 'Position:',
        'overlay_position_center': 'Mitte',
        'overlay_position_top_left': 'Oben links',
        'overlay_position_top_right': 'Oben rechts',
        'overlay_position_bottom_left': 'Unten links',
        'overlay_position_bottom_right': 'Unten rechts',
        'overlay_size': 'Größe:',
        'overlay_size_original': 'Originalgröße',
        'overlay_size_fit_page': 'An Seite anpassen',
        'overlay_size_custom': 'Benutzerdefiniert (%)',
        'overlay_opacity': 'Transparenz:',
        'overlay_target_folder': 'Zielordner:',
        'overlay_browse_folder': 'Durchsuchen...',
        'overlay_select_folder': 'Zielordner auswählen',
        'overlay_warning': '⚠️ Hinweis: Die Overlay-PDF wird auf die Basis-PDF gelegt und dabei "eingebrannt".\n\n'
            'Die Elemente der Overlay-PDF können nach dem Speichern nicht mehr einzeln bearbeitet werden.',
        'overlay_apply': 'Überlagern',
        'overlay_start': 'Starte Überlagerung...',
        'overlay_progress': 'PDF wird überlagert...',
        'overlay_success': 'PDF erfolgreich überlagert!\n\nGespeichert als:\n{0}\n\nMöchten Sie die überlagerte PDF öffnen?',
        'overlay_complete': 'Überlagerung abgeschlossen',
        'overlay_cancel': 'Überlagerung abgebrochen',
        'overlay_error_format': 'Fehler beim Überlagern:\n\n{0}',
        'overlay_no_file': 'Es wurde keine Overlay-PDF ausgewählt.\n\nBitte wählen Sie eine PDF-Datei zum Überlagern aus.',
        'filename_overlay_suffix': '_überlagert',

        ###==============================================
        ### 99. ALLE BILDER EXPTRAHIEREN
        ###==============================================
        'extract_images_title': 'Bilder aus PDF extrahieren',
        'extract_images_menu': 'Alle Bilder extrahieren',
        'extract_images_info': 'Extrahiert alle Bilder aus der PDF und speichert sie als einzelne Dateien.\n\nDie Bilder werden mit ihrem Originalformat oder in ein ausgewähltes Format konvertiert.',
        'extract_images_format': 'Bildformat:',
        'extract_images_quality': 'JPEG-Qualität:',
        'extract_images_options': 'Optionen:',
        'extract_images_subfolder': 'In Unterordner extrahieren ("PDFname_bilder")',
        'extract_images_unique': 'Nur eindeutige Bilder (Duplikate vermeiden)',
        'extract_images_range': 'Seitenbereich:',
        'extract_images_all_pages': 'Alle Seiten',
        'extract_images_custom_range': 'Benutzerdefinierter Bereich',
        'extract_images_from': 'Von:',
        'extract_images_to': 'Bis:',
        'extract_images_target_folder': 'Zielordner:',
        'extract_images_browse': 'Durchsuchen...',
        'extract_images_select_folder': 'Zielordner auswählen',
        'extract_images_info_box': 'Informationen',
        'extract_images_info_text': 'Die Extraktion kann bei großen PDFs mehrere Minuten dauern.\n\nBilder werden mit ihrem ursprünglichen Namen (Seite_Bild) gespeichert.',
        'extract_images_extract': 'Extrahieren',
        'extract_images_start': 'Starte Extraktion...',
        'extract_images_progress': 'Bilder werden extrahiert...',
        'extract_images_success': '✅ Bilder erfolgreich extrahiert!\n\n{0} Bilder wurden gespeichert in:\n{1}',
        'extract_images_complete': 'Bild-Extraktion abgeschlossen',
        'extract_images_cancel': 'Extraktion abgebrochen',
        'extract_images_error_format': 'Fehler beim Extrahieren der Bilder:\n\n{0}',
        'extract_images_open_folder': '📁 Ordner öffnen',
        'extract_images_no_images': 'Keine Bilder in der PDF gefunden.',

        ### ------------------------
        ### 100.MEHRERE SEITEN AUF EINE SEITE
        ### ------------------------
        'nup_title': 'Mehrere Seiten auf eine Seite (N-Up)',
        'nup_menu': 'Mehrere Seiten auf eine Seite (N-Up)',
        'nup_info': 'Ordnet mehrere PDF-Seiten auf einer Seite an.\n\nIdeal für kompakte Ausdrucke, Übersichten oder Handouts.',
        'nup_layout': 'Layout:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Vorschau:',
        'nup_preview_info': '{0} Seiten → {1} Seiten pro Blatt → {2} Blätter\nLayout: {3}',
        'nup_order': 'Reihenfolge:',
        'nup_order_horizontal': 'Horizontal (Zeilenweise)',
        'nup_order_vertical': 'Vertikal (Spaltenweise)',
        'nup_order_horizontal_reverse': 'Horizontal rückwärts',
        'nup_order_vertical_reverse': 'Vertikal rückwärts',
        'nup_range': 'Seitenbereich:',
        'nup_all_pages': 'Alle Seiten',
        'nup_custom_range': 'Benutzerdefinierter Bereich',
        'nup_from': 'Von:',
        'nup_to': 'Bis:',
        'nup_options': 'Optionen:',
        'nup_margins': 'Ränder:',
        'nup_margin_between': 'Abstand zwischen den Seiten:',
        'nup_page_numbers': 'Seitenzahlen einfügen',
        'nup_target_folder': 'Zielordner:',
        'nup_browse': 'Durchsuchen...',
        'nup_select_folder': 'Zielordner auswählen',
        'nup_create': 'Erstellen',
        'nup_start': 'Starte N-Up...',
        'nup_progress': 'N-Up wird erstellt...',
        'nup_success': 'N-Up erfolgreich erstellt!\n\nGespeichert als:\n{0}\n\nMöchten Sie die neue PDF öffnen?',
        'nup_complete': 'N-Up abgeschlossen',
        'nup_cancel': 'N-Up abgebrochen',
        'nup_error_format': 'Fehler bei N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        ###==============================================
        ### 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        ###==============================================
        'pagesize_title': 'Seitengröße ändern',
        'pagesize_menu': 'Seitengröße ändern',
        'pagesize_info': 'Ändert die Seitengröße der PDF.\n\nDer Inhalt wird automatisch an die neue Größe angepasst.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Wählen Sie ein Standardformat:',
        'pagesize_custom': 'Benutzerdefinierte Größe:',
        'pagesize_width': 'Breite:',
        'pagesize_height': 'Höhe:',
        'pagesize_orientation': 'Ausrichtung:',
        'pagesize_portrait': 'Hochformat',
        'pagesize_landscape': 'Querformat',
        'pagesize_scale_options': 'Skalierungsoptionen:',
        'pagesize_fit': 'Anpassen (Seitenverhältnis beibehalten)',
        'pagesize_stretch': 'Strecken (Verzerren)',
        'pagesize_center': 'Zentrieren (Originalgröße)',
        'pagesize_range': 'Seitenbereich:',
        'pagesize_all_pages': 'Alle Seiten',
        'pagesize_custom_range': 'Benutzerdefinierter Bereich',
        'pagesize_from': 'Von:',
        'pagesize_to': 'Bis:',
        'pagesize_target_folder': 'Zielordner:',
        'pagesize_browse': 'Durchsuchen...',
        'pagesize_select_folder': 'Zielordner auswählen',
        'pagesize_apply': 'Anwenden',
        'pagesize_start': 'Starte Seitengrößen-Änderung...',
        'pagesize_progress': 'Seitengröße wird geändert...',
        'pagesize_success': 'Seitengröße erfolgreich geändert!\n\nGespeichert als:\n{0}\n\nMöchten Sie die neue PDF öffnen?',
        'pagesize_complete': 'Seitengrößen-Änderung abgeschlossen',
        'pagesize_cancel': 'Seitengrößen-Änderung abgebrochen',
        'pagesize_error_format': 'Fehler beim Ändern der Seitengröße:\n\n{0}',
        'pagesize_preview_info': 'Neue Größe: {0} x {1} pt',
        'filename_pagesize_suffix': '_neuegroesse',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'PDF-Informationen',
        'pdf_info_menu': 'PDF-Info anzeigen',
        'pdf_info_voice': 'PDF-Informationen werden angezeigt',
        'pdf_info_error': 'Fehler beim Anzeigen der PDF-Info:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Tastaturkürzel anzeigen",
        "shortcuts_dialog_title": "Tastaturkürzel",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 DATEI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>PDF öffnen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>PDF schließen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Speichern unter...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Dokument schützen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Drucken</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Sofort drucken (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Anwendung beenden</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EXPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Als Pages exportieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Als DOCX exportieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Als TXT exportieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Als Bilder exportieren (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Bilder extrahieren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ DOKUMENTENVERARBEITUNG</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (Mehrere Seiten)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>PDF/A-Konvertierung (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>PDF glätten</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>PDF übereinanderlegen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>PDF optimieren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ BEARBEITEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Suchen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Lesezeichen hinzufügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Lesezeichen verwalten</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Nächstes Lesezeichen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Vorheriges Lesezeichen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>OCR durchführen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 SEITENVERWALTUNG</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Aktuelle Seite drehen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Alle Seiten drehen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Aktuelle Seite normalisieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Alle Seiten normalisieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Seiten löschen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Seiten entnehmen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Seiten einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Seiten verschieben</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>PDFs zusammenführen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Seitengröße ändern</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 EINFÜGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Text einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Kreuz einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Signatur 1 einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Signatur 2 einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Bild einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Rechteck einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Ellipse einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Linie einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Pfeil einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Seitenzahlen einfügen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Text-Wasserzeichen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Bild-Wasserzeichen</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ AUSLÖSCHUNGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Auslöschung (schwarz)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Auslöschung (weiß)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Alle Auslöschungen anwenden</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ FORTGESCHRITTEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>PDF zuschneiden</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Metadaten bearbeiten</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ ANSICHT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Dark/Light Mode umschalten</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Textfenster anzeigen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Seitenbreite (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Zwei Seiten (Zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Übersicht (Zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ EINSTELLUNGEN</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Passwortverwaltung</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>OCR-Einstellungen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Signatur-Einstellungen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Dateinamen-Formatierung</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Einstellungen exportieren</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Einstellungen importieren</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFO</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>PDF-Info anzeigen</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Sprachausgabe ein/aus</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Menüleiste fokussieren</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Neue Version verfügbar",
        "update_available_message": "Es gibt eine neue Version <b>{0}</b>.\n\nBesuchen Sie die Release‑Seite, um das Update herunterzuladen:\n{1}",
        "update_available_voice": "Neue Version {0} verfügbar. Bitte laden Sie das Update von der GitHub‑Seite herunter.",
        "update_open_release": "Release Seite öffnen",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Alle Übersetzungen herunterladen",
        "ask_download_all_translations": """Es sind außer Deutsch, Englisch und Vietnamesisch noch  {total_languages} weitere GUI-Sprachen verfügbar.\n\nSollen diese bereitgestellt / aktualisiert werden?\n\nHinweis:\nNicht benötigte Sprachen können Sie später im Verzeichnis:\n{translations_path}
        manuell löschen.\n\nWenn Sie abbrechen, können Sie die GUI-Sprachen später über das Menü 'Extras → Übersetzungen aktualisieren' herunterladen.""",
        "menu_update_translations": "Übersetzungen aktualisieren",
        "translations_updated": "Übersetzungen aktualisiert",
        "translations_update_success": "{} Übersetzungen wurden erfolgreich aktualisiert ({} neu, {} aktualisiert).",
        "translations_update_error": "Fehler beim Aktualisieren der Übersetzungen",
        "translations_update_no_changes": "Alle Übersetzungen sind bereits aktuell.",
        "translations_update_offline": "Keine Internetverbindung. Übersetzungen konnten nicht aktualisiert werden.",
        "translations_update_in_progress": "Übersetzungen werden im Hintergrund aktualisiert...",
        "translations_downloading": "Lade Übersetzungen herunter...",
        "translations_path_hint": "Benutzerverzeichnis für Übersetzungen",
        "translations_update_not_available_title": "Update nicht verfügbar",
        "translations_update_not_available_message": """Das Aktualisieren der Übersetzungen ist nur in der installierten Version verfügbar.\n\nIm Entwicklungsmodus sind die Übersetzungen bereits aktuell.""",
        "translations_update_no_internet_title": "Keine Internetverbindung",
        "translations_update_no_internet_message": """Es konnte keine Internetverbindung hergestellt werden.\n\nDie Übersetzungen können nicht von GitHub heruntergeladen werden.\n\nMögliche Lösungen:
        • Überprüfen Sie Ihre Internetverbindung
        • Deaktivieren Sie eine eventuelle Firewall kurzzeitig
        • Versuchen Sie es später erneut
        \nSie können die Übersetzungen auch manuell von GitHub herunterladen:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Update läuft bereits",
        "btn_retry": "Erneut versuchen",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Willkommen bei PDF Dark View",
        "welcome_title_not_supported": "Willkommen bei PDF Dark View",
        "welcome_message": "Willkommen bei PDF Dark View!\n\nIhre Systemsprache wurde als '{language}' erkannt.\nMöchten Sie diese Sprache für die Benutzeroberfläche verwenden?\n\nSie können die Sprache jederzeit über 'Einstellungen → Sprache' ändern.",
        "welcome_message_language_not_available": "Willkommen bei PDF Dark View!\n\nIhre Systemsprache wurde als '{language}' erkannt.\nDiese Sprache ist derzeit noch nicht installiert.\n\nMöchten Sie die Übersetzungen für {language} jetzt von GitHub herunterladen?\n\n(Die Sprache wird dann automatisch für die Benutzeroberfläche verwendet.)",
        "welcome_message_language_not_supported": "Willkommen bei PDF Dark View!\n\nIhre Systemsprache wurde als '{language}' erkannt.\nLeider gibt es für diese Sprache derzeit noch keine Übersetzungen.\n\nDie Benutzeroberfläche wird daher auf {fallback_language} angezeigt.\n\nSie können die Sprache jederzeit über 'Einstellungen → Sprache' ändern.\nWenn Sie möchten, können Sie auch selbst eine Übersetzung für Ihre Sprache beitragen:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Ja, Systemsprache verwenden",
        "welcome_keep_english": "Nein, Englisch behalten",
        "welcome_download_language": "Ja, {language} herunterladen",


        # --> ab hier neu (noch nicht übersetzt)

        # ============================================
        # 107. ZULETZT VERWENDETE PFADE
        # ============================================

        'menu_recent': 'Zuletzt verwendet',
        'menu_recent_dirs': 'Verzeichnisse...',
        'menu_recent_files': 'Dateien...',
        'recent_manage': 'Verwalten...',
        # Recent Paths - Einstellungen
        'recent_enable_tracking': 'Zuletzt verwendete Pfade speichern (Datenschutz)',
        'recent_enable_info': 'Deaktivieren Sie diese Option, um keine Pfade zu speichern',
        'recent_tracking_disabled': 'Pfadverfolgung deaktiviert',
        'recent_enabled': 'aktiviert',
        'recent_disabled': 'deaktiviert',
        'recent_tracking_status': 'Pfadverfolgung {0}',
        # Recent Paths - Dialog
        'recent_dialog_title': 'Zuletzt verwendete Pfade',
        'recent_tab_directories': 'Verzeichnisse',
        'recent_tab_files': 'Dateien',
        'recent_dirs_instruction': 'Doppelklick zum Öffnen des Dateidialogs im Verzeichnis',
        'recent_files_instruction': 'Doppelklick zum direkten Öffnen der PDF',
        'recent_no_directories': '(keine Verzeichnisse gespeichert)',
        'recent_no_files': '(keine Dateien gespeichert)',
        'recent_default_current': '⭐ Standard: {0}',
        'recent_set_as_default': '⭐ Als Standard setzen',
        'recent_default_set_title': 'Standard-Verzeichnis gesetzt',
        'recent_default_set_message': 'Das Verzeichnis "{0}" wurde als Standard für das Öffnen von PDFs gesetzt.',
        'recent_default_set_voice': 'Standard-Verzeichnis wurde gesetzt',
        'recent_directory_not_found': 'Verzeichnis nicht gefunden',
        'recent_file_not_found': 'Datei nicht gefunden',
        'recent_remove_selected': 'Entfernen',
        'recent_remove_title': 'Pfad entfernen',
        'recent_remove_confirm': 'Möchten Sie den Pfad "{0}" wirklich aus der Liste entfernen?',
        'recent_path_removed': 'Pfad wurde entfernt',
        'recent_clear_all': 'Alle entfernen',
        'recent_clear_title': 'Alle Pfade entfernen',
        'recent_clear_confirm_type': 'Möchten Sie wirklich alle {0} löschen?',
        'recent_cleared': 'Liste wurde gelöscht',
        'recent_path_not_found_title': 'Pfad nicht gefunden',
        'recent_path_not_found_message': 'Der Pfad "{0}" existiert nicht mehr.',
        'recent_open_file': 'Datei öffnen',
        'btn_open_recent': 'Öffnen',
        'recent_open_file_question': 'Möchten Sie "{0}" als PDF öffnen?',
        'recent_not_pdf': 'Die ausgewählte Datei ist keine PDF.',
        'recent_more_entries': 'Weitere Einträge...',
        'btn_remove': 'Entfernen',
        'btn_clear': 'Alle löschen',
        # Recent Paths - Context Menu
        'recent_context_open': 'Öffnen',
        'recent_context_reveal': 'Im Finder anzeigen',
        'recent_context_set_default': '⭐ Als Standard setzen',
        'recent_context_open_terminal': '💻 Terminal öffnen',
        'recent_context_file_info': 'Datei-Info',
        'recent_context_open_with_default': '📄 Mit Standard-App öffnen',
        'recent_context_remove': 'Aus Liste entfernen',
        'recent_context_clear_all': 'Alle entfernen',

        # Recent Paths - File Info
        'recent_file_info_title': 'Datei-Informationen',
        'recent_file_info_name': 'Name',
        'recent_file_info_path': 'Pfad',
        'recent_file_info_size': 'Größe',
        'recent_file_info_modified': 'Geändert',
        'recent_file_info_pages': 'Seiten',

        # Recent Paths - Errors
        'recent_error_reveal': 'Fehler beim Öffnen im Finder',
        'recent_error_terminal': 'Fehler beim Öffnen des Terminals',
        'recent_error_info': 'Fehler beim Abrufen der Datei-Info',
        'open_user_data_folder': 'Benutzerdaten-Verzeichnis anzeigen',

        # ============================================
        # 108. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Programm wird beendet",

    }


