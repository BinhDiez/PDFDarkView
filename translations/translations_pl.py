
# ============================================
# translations_pl.py - Polskie słownictwo dla PDFDarkView
# Pełne posortowane według kategorii
# ============================================

def load_polish_strings():
    """Ładuje wszystkie polskie napisy"""

    return {
        # ============================================
        # 1. APP-NAME UND TITEL
        # ============================================
        'app_title': "PDF Dark View by BinhDiez",
        'app_name': "PDF Dark View",

        # ============================================
        # 2. HAUPTFENSTER BUTTONS
        # ============================================
        'btn_open': "Wczytaj PDF",
        'btn_text_window': "Tekst OCR",
        'btn_first': "Pierwsza strona",
        'btn_prev': "Poprzednia strona",
        'btn_next': "Następna strona",
        'btn_last': "Ostatnia strona",
        'btn_print': "Drukuj",
        'btn_darkmode_light': "Tryb jasny",
        'btn_darkmode_dark': "Tryb ciemny",
        'btn_delete_pages': "Usuń strony",
        'btn_extract_pages': "Wyodrębnij strony",

        # ============================================
        # 3. ALLGEMEINE BUTTONS (Dialioge)
        # ============================================
        'btn_ok': "OK",
        'btn_cancel': "Anuluj",
        'btn_save': "Zapisz",
        'btn_close': "Zamknij",
        'btn_delete': "Usuń",
        'btn_delete_all': "Usuń wszystko",
        'btn_copy': "Kopiuj",
        'btn_export': "Eksportuj",
        'btn_show': "Pokaż hasło",
        'btn_hide': "Ukryj hasło",
        'btn_authenticate': "Uwierzytelnij",
        'btn_settings': "Ustawienia",
        'btn_protect': "Zabezpiecz",
        'btn_remove_password': "Usuń hasło",
        'btn_manage': "Zarządzanie hasłami",
        'btn_retry': "Spróbuj ponownie",
        'btn_select_all': "Zaznacz wszystkie",
        'btn_clear_selection': "Odznacz zaznaczenie",

        # ============================================
        # 4. SEITEN-NAVIGATION
        # ============================================
        'page_of': "Strona {0} z {1}",
        'page_count': "z {0}",
        'goto_page': "Przejdź do strony",
        'page_simple': "Strona {0}",
        'full_view_page': "Pełny widok strony {0}",

        # ============================================
        # 5. SUCHE
        # ============================================
        'search_placeholder': "Wpisz szukane hasło + Enter",
        'search_results': "Znaleziono: {0} z {1}",
        'search_nav_hint': "Enter: następny (Shift+Enter: poprzedni) wynik",
        'search_no_results': "Brak wyników",
        'search_error': "Błąd wyszukiwania",
        'search_active': "Pole wyszukiwania aktywne",
        'search_closed': "Wyszukiwanie zakończone",
        'search_position': "Strona {0} {1}",
        'search_pos_top': "na samym początku",
        'search_pos_upper': "na górze",
        'search_pos_middle': "w środku",
        'search_pos_lower': "na dole",
        'search_pos_bottom': "na samym dole",

        # ============================================
        # 6. OCR
        # ============================================
        'ocr_success': "Rozpoznawanie tekstu zakończone pomyślnie!",
        'ocr_success_title': "OCR powiódł się",
        'ocr_success_message': "Dokument jest teraz przeszukiwalny.",
        'ocr_failed': "OCR nie powiódł się",
        'ocr_in_progress': "OCR w toku",
        'ocr_preparing': "Przygotowywanie PDF...",
        'ocr_analyzing': "Analizowanie PDF...",
        'ocr_optimizing': "Optymalizacja obrazu...",
        'ocr_recognizing': "Rozpoznawanie tekstu...",
        'ocr_embedding': "Osadzanie tekstu...",
        'ocr_finalizing': "Finalizacja PDF...",
        'ocr_not_available': "OCR niedostępny",
        'ocr_install_message': "Narzędzia OCR nie zostały znalezione.\n\nZainstaluj:\n• Tesseract: brew install tesseract\n• OCRmyPDF: pip install ocrmypdf",
        'ocr_required': "Wymagane OCR",
        'ocr_question': "PDF nie zawiera przeszukiwalnego tekstu.\nCzy chcesz przeprowadzić OCR, aby umożliwić {0}?",
        'ocr_perform': "Wykonaj OCR",
        'ocr_later': "Później",
        'ocr_starting': "Uruchamianie gwarantowanego OCR...",
        'ocr_success_voice': "OCR powiódł się. PDF jest teraz przeszukiwalny.",
        'ocr_partial_success': "OCR został wykonany, ale wystąpiły problemy podczas zastępowania.\n\nPrzeszukiwalna wersja została zapisana jako:\n{0}\n\nBłąd: {1}",
        'ocr_partial_title': "OCR częściowo udany",
        'ocr_partial_voice': "OCR wykonany, ale zastępowanie nie powiodło się.",
        'original_file': "Oryginalny plik:",
        'old_size': "Stary rozmiar:    {0} bajtów",
        'new_size': "Nowy rozmiar: {0} bajtów",
        'size_change': "Zmiana: {0}{1} bajtów",
        'backup_created_file': "Utworzono kopię zapasową:\n{0}",
        'backup_not_created': "Kopia zapasowa: nie utworzono (ustawienie wyłączone)",
        'page_header': "=== Strona {0} ===\n{1}\n",
        'scanned_page_header': "=== Strona {0} (zeskanowana) ===\n[Ta strona zawiera tylko zeskanowany tekst]\n[Wykonaj ręcznie OCR]\n",
        'scanned_warning': "⚠️ TEKST ZESKANOWANY - WYMAGANE OCR",
        'guaranteed_title': "Utworzono przeszukiwalny PDF",
        'guaranteed_message': "<b>Utworzono przeszukiwalną wersję!</b>\n\nPonieważ automatyczne OCR nie powiodło się, utworzono\nalternatywny przeszukiwalny PDF:\n\n{0}\n\n<b>Ten plik zawiera:</b>\n• Wyodrębniony tekst (jeśli istnieje)\n• Wskazówki dla zeskanowanych stron\n• Jest w pełni przeszukiwalny",
        'guaranteed_voice': "Utworzono przeszukiwalny PDF.",
        'instruction_title': "INSTRUKCJA DLA OCR",
        'instruction_file': "Oryginalny plik: {0}",
        'instruction_text': "Automatyczne rozpoznawanie tekstu (OCR) nie powiodło się.\nWykonaj OCR ręcznie:\n\n1. Z OCRmyPDF (wiersz poleceń):\n   ocrmypdf --force-ocr \"[PLIK]\" \"wyjście.pdf\"\n\n2. Z ADOBE ACROBAT (macOS/Windows):\n   • Otwórz PDF w Acrobat\n   • Narzędzia > Edytuj PDF\n   • Wybierz 'Rozpoznawanie tekstu'\n\n3. Z PREVIEW (macOS):\n   • Otwórz PDF w Podglądzie\n   • Plik > Eksportuj...\n   • Filtr Quartz: 'Reduce File Size'\n   • Włącz 'Wykonaj OCR'\n\n4. ONLINE USŁUGI OCR:\n   • smallpdf.com/pl/ocr-pdf\n   • ilovepdf.com/pl/ocr-pdf\n   • adobe.com/pl/acrobat/online/pdf-to-word.html",
        'instruction_created': "Utworzono instrukcję OCR",
        'instruction_created_message': "Utworzono szczegółową instrukcję:\n\n{0}\n\nPostępuj zgodnie z krokami, aby wykonać ręczne OCR.",
        'instruction_created_voice': "Utworzono instrukcję OCR.",
        'ocr_impossible': "OCR niemożliwy",
        'ocr_impossible_message': "Nie można było przeprowadzić OCR.\n\nPrzetwórz '{0}' ręcznie za pomocą oprogramowania OCR.",
        'ocr_impossible_voice': "OCR niemożliwy. Przetwórz ręcznie.",
        'emergency_title': "Awaryjne OCR",
        'emergency_message': "Utworzono awaryjny PDF:\n\n{0}\n\nPrzetwórz ten plik ręcznie za pomocą OCR.",
        'emergency_voice': "Utworzono awaryjny PDF. Wykonaj ręczne OCR.",
        'critical_error': "Krytyczny błąd",
        'critical_error_message': "Nie można było uruchomić OCR.\n\nUruchom ponownie program i\nsprawdź instalację OCR.",
        'critical_error_voice': "Krytyczny błąd OCR",
        'ocr_question_html': "<p>PDF nie zawiera przeszukiwalnego tekstu.<p>Czy chcesz przeprowadzić OCR, aby umożliwić <b>{0}</b>?</p>",
        'ocr_question_voice': "Wymagane OCR. PDF nie zawiera przeszukiwalnego tekstu. Czy chcesz przeprowadzić OCR, aby umożliwić {0}?",

        # ============================================
        # 7. DATEIOPERATIONEN
        # ============================================
        'no_pdf_loaded': "brak załadowanego PDF",
        'no_pdf_message': "Nie załadowano żadnego PDF",
        'pdf_not_found': "Nie znaleziono pliku PDF",
        'file_size': "Rozmiar pliku",
        'bytes': "bajtów",
        'kb': "KB",
        'mb': "MB",
        'backup_created': "Utworzono kopię zapasową",
        'backup_disabled': "Kopia zapasowa wyłączona",
        'backup_activated': "Tworzenie kopii zapasowej włączone",
        'backup_deactivated': "Tworzenie kopii zapasowej wyłączone",
        'backup_status': "Kopia zapasowa: {0}",
        'backup_on': "✔ włączona",
        'backup_off': "✘ wyłączona",
        'close_pdf': "Zamykanie PDF: {0}",
        'pdf_not_found_format': "Nie znaleziono pliku PDF: {0}",
        'error_pdf_load_format': "Błąd podczas ładowania PDF: {0}",
        'load_failed_format': "Ładowanie nie powiodło się:\n{0}",
        'decrypted_suffix': "(odszyfrowany)",
        'decryption_failed': "Odszyfrowanie nie powiodło się.",
        'decryption_error': "Błąd odszyfrowania",
        'decryption_success': "Pomyślnie odszyfrowano",
        'decryption_success_message': "PDF został odszyfrowany i zapisany jako:\n\n{0}",
        'decryption_success_voice': "PDF odszyfrowany i zapisany.",
        'password_remove_error': "Błąd podczas usuwania hasła",
        'save_unencrypted': "Zapisz niezabezpieczony PDF jako",

        # ============================================
        # 8. SPEICHERN
        # ============================================
        'save_as': "Zapisz jako...",
        'save_copy': "Zapisz kopię",
        'save_success': "PDF zapisany jako: {0}",
        'save_encrypted': "Zabezpieczony PDF zapisany jako: {0}",
        'save_error': "Nie można zapisać PDF",
        'encryption_question': "Czy chcesz zabezpieczyć PDF hasłem?",
        'encryption_yes': "Tak",
        'encryption_no': "Nie",
        'encryption_cancel': "Anuluj",
        'save_cancel': "Zapisywanie anulowane",
        'save_encrypted_voice': "Plik zaszyfrowany i zapisany.",
        'save_success_voice': "Plik PDF został zapisany bez szyfrowania.",
        'save_error_format': "Nie można zapisać PDF:\n{0}",
        'export_pages_success': "Eksport do Pages powiódł się",
        'export_pages_error': "Eksport do Pages nie powiódł się",
        'export_pages_error_format': "Eksport do Pages nie powiódł się: {0}",
        'export_word_success': "Eksport do Word powiódł się",
        'export_word_error': "Eksport do Word nie powiódł się",
        'export_word_error_format': "Eksport do Word nie powiódł się: {0}",
        'export_text_success': "Eksport do tekstu powiódł się",
        'export_text_error': "Eksport do tekstu nie powiódł się",
        'export_text_error_format': "Eksport do tekstu nie powiódł się: {0}",

        # ============================================
        # 9. PASSWORT-DIALOGE
        # ============================================
        'password_required': "Wymagane hasło",
        'password_enter': "Wprowadź hasło",
        'password_confirm': "Potwierdź hasło",
        'password_new': "Nowe hasło",
        'password_current': "Aktualne hasło",
        'password_save': "Zapisz hasło (zaszyfrowane)",
        'password_saved': "✓ Hasło dla tego pliku jest zapisane",
        'password_wrong': "Nieprawidłowe hasło",
        'password_mismatch': "Hasła nie są zgodne",
        'password_too_short': "Hasło za krótkie",
        'password_min_length': "Hasło musi mieć co najmniej 4 znaki",
        'password_strength': "Siła hasła",
        'password_strength_very_weak': "Bardzo słabe",
        'password_strength_weak': "Słabe",
        'password_strength_medium': "Średnie",
        'password_strength_strong': "Silne",
        'password_strength_very_strong': "Bardzo silne",
        'password_char_count': "({0} znaków)",
        'password_match': "✓ Zgodność",
        'password_no_match': "✗ Hasła nie są zgodne",
        'password_show': "Pokaż",
        'password_hide': "Ukryj",

        # ============================================
        # 10. PASSWORTVERWALTUNG
        # ============================================
        'password_manager': "Zarządzanie hasłami",
        'password_table_filename': "Nazwa pliku",
        'password_table_password': "Hasło",
        'password_count': "{0} zapisane hasło{1}",
        'password_count_singular': "",
        'password_count_plural': "a",
        'password_none': "Brak zapisanych haseł",
        'password_copied': "Skopiowano {0} hasło{1}",
        'password_copied_singular': "",
        'password_copied_plural': "a",
        'password_delete_confirm': "Czy na pewno chcesz usunąć hasło dla '{0}'?",
        'password_delete_multiple': "Czy na pewno chcesz usunąć {0} zaznaczone hasła?",
        'password_delete_all_confirm': "Czy na pewno chcesz usunąć wszystkie {0} zapisane hasła?",
        'password_deleted': "Usunięto {0} hasło{1}",
        'password_deleted_singular': "",
        'password_deleted_plural': "a",
        'password_deleted_verb_singular': "",
        'password_deleted_verb_plural': "o",
        'password_all_deleted': "Wszystkie hasła zostały usunięte",

        # ============================================
        # 11. PASSWORT-GENERATOR
        # ============================================
        'generator_title': "Generator haseł",
        'generator_generated': "Wygenerowane hasło:",
        'generator_regenerate': "Generuj ponownie",
        'generator_copy': "Kopiuj",
        'generator_use': "Użyj",
        'generator_settings': "Ustawienia",
        'generator_length': "Długość:",
        'generator_group_every': "Separator co",
        'generator_group_chars': "znaków.    Separator:",
        'generator_uppercase': "Wielkie litery (A-Z)",
        'generator_lowercase': "Małe litery (a-z)",
        'generator_digits': "Cyfry (0-9)",
        'generator_symbols': "Znaki specjalne (!@#$%^&*)",
        'generator_exclude': "Wykluczone:",

        # ============================================
        # 12. MASTER-PASSWORT
        # ============================================
        'master_password_required': "Wymagane hasło główne",
        'master_password_setup': "Ustaw hasło główne",
        'master_password_change': "Zmień hasło główne",
        'master_password_enter': "Wprowadź swoje hasło główne",
        'master_password_choose': "Wybierz silne hasło główne (minimum 8 znaków)",
        'master_password_new': "Wprowadź nowe hasło główne",
        'master_password_confirm': "Potwierdź hasło",
        'master_password_authenticate': "Uwierzytelnij",
        'master_password_success': "Hasło główne zostało pomyślnie ustawione.",
        'master_password_changed': "Hasło główne zostało pomyślnie zmienione.",
        'master_password_removed': "Hasło główne i wszystkie hasła zostały usunięte.",
        'master_password_remove': "Usuń hasło główne",
        'master_password_remove_confirm': "Czy na PEWNO chcesz usunąć WSZYSTKIE hasła?\n\nTa operacja jest NIEODWRACALNA!",
        'master_password_export_before': "Czy chcesz najpierw wyeksportować kopię zapasową?",
        'master_password_export_delete': "Eksportuj i usuń",
        'master_password_delete_now': "Usuń teraz",
        'master_password_for_signatures': "Aby używać podpisów, musisz ustawić hasło główne.\n\nCzy chcesz teraz ustawić hasło główne?",
        'master_password_for_private': "Aby używać prywatnych fragmentów tekstu, musisz ustawić hasło główne.\n\nCzy chcesz teraz ustawić hasło główne?",
        'master_password_info': """
            <b>🔐 BEZ HASŁA GŁÓWNEGO:</b><br>
            • Brak możliwości wyświetlania, kopiowania i eksportu haseł<br>
            • Usuwanie haseł jest zawsze możliwe (nawet bez hasła głównego)<br><br>

            <b>🔐 Z HASŁEM GŁÓWNYM:</b><br>
            • Wszystkie funkcje dostępne po uwierzytelnieniu<br>
            • Hasła są szyfrowane hasłem głównym<br>
            • Minimalna długość: 8 znaków<br>
            • Bezpieczne przechowywanie z użyciem SHA-256<br><br>

            <b>WAŻNE:</b><br>
            • W przypadku utraty hasła głównego: hasła nie są odtwarzalne<br>
            • Przy usuwaniu hasła głównego: WSZYSTKIE hasła zostaną usunięte<br>
            • Opcja eksportu przed usunięciem dostępna<br>
            • Hasło główne można zmienić w dowolnym momencie
        """,
        'signature_auth_disabled': "Wyłącz zapytanie o hasło dla podpisów",
        'template_auth_disabled': "Wyłącz zapytanie o hasło dla prywatnych fragmentów tekstu",
        'master_password_for_signatures_settings': "Aby używać podpisów, musisz ustawić hasło główne.\n\nPrzejdź do Ustawienia - Zarządzanie hasłami",

        # ============================================
        # 13. PDF SCHÜTZEN
        # ============================================
        'protect_title': "Zabezpiecz PDF",
        'protect_info': "Plik '{0}' zostanie zabezpieczony hasłem.",
        'protect_instruction': "Wprowadź dwukrotnie żądane hasło, aby zabezpieczyć dokument, lub użyj generatora haseł po prawej stronie pola wprowadzania.",
        'protect_success': "PDF został pomyślnie zabezpieczony i zapisany jako:\n{0}\n\nHasło: {1}\n\nCzy chcesz teraz otworzyć zabezpieczony PDF?",
        'protect_open': "Tak",
        'protect_skip': "Nie",
        'protect_error': "Błąd podczas zabezpieczania PDF",
        'protect_open_title': "otwórz zabezpieczony PDF",
        'protect_question': "Gotowe. Czy chcesz teraz otworzyć zabezpieczony PDF? Tak lub Nie?",
        'password_cancel': "Anulowano okno dialogowe hasła",

        # ============================================
        # 14.1 SEITENOPERATIONEN
        # ============================================
        'pages_delete': "Usuń strony",
        'pages_extract': "Wyodrębnij strony",
        'pages_insert': "Wstaw strony",
        'pages_move': "Przesuń strony",
        'pages_delete_options': "Opcje usuwania",
        'pages_delete_empty': "Usuń wszystkie puste strony",
        'pages_delete_current': "Usuń bieżącą stronę",
        'pages_delete_range': "Usuń zakres stron",
        'pages_cannot_delete_all': "Nie można usunąć wszystkich stron",
        'pages_extract_options': "Opcje wyodrębniania",
        'pages_extract_current': "Wyodrębnij bieżącą stronę",
        'pages_extract_range': "Wyodrębnij zakres stron",
        'pages_insert_position': "Pozycja wstawiania",
        'pages_insert_before': "Wstaw przed stroną:",
        'pages_insert_select': "Wybierz PDF",
        'pages_insert_none': "Nie wybrano PDF",
        'pages_move_source': "Strony do przesunięcia",
        'pages_move_from': "Od strony:",
        'pages_move_to': "Do strony:",
        'pages_move_target': "Pozycja docelowa",
        'pages_move_before': "Przesuń przed stronę:",
        'pages_move_hint': "Uwaga: strona 1 = początek, {0} = koniec",
        'pages_range_invalid': "Strona początkowa musi być mniejsza lub równa stronie końcowej.",
        'pages_position_invalid': "Docelowa pozycja nie może znajdować się wewnątrz przesuwanego zakresu.",
        'pages_no_pdf_selected': "Nie wybrano żadnego PDF.",
        'pages_deleted': "Usunięto {0} stron.",
        'pages_extracted': "Wyodrębniono: {0}\nZapisano jako: {1}\nRozmiar: {2:.1f} KB",
        'pages_inserted': "Wstawiono {0} stron",
        'pages_moved': "Przesunięto {0} stron.",
        'pages_deleted_none': "Nie usunięto żadnych stron.",
        'pages_delete_progress': "Usuwanie stron...",
        'pages_deleted_with_backup': "Usunięto {0} stron.\n\nKopia zapasowa: {1}",
        'pages_deleted_voice': "Utworzono kopię zapasową i usunięto {0} stron.",
        'info': "Uwaga",
        'error_dialog_creation': "Nie można utworzyć okna dialogowego",
        'extract_page_single': "Wyodrębnij stronę {0}",
        'extract_page_range': "Wyodrębnij strony {0}-{1}",
        'extract_success_voice': "Strony zostały pomyślnie wyodrębnione",
        'extract_error_format': "Błąd podczas wyodrębniania: {0}",
        'pages_inserted_voice': "Wstawiono {0} stron.",
        'insert_error_format': "Błąd podczas wstawiania: {0}",
        'pages_move_progress': "Przesuwanie stron...",
        'pages_moved_with_backup': "Przesunięto {0} stron.\n\nKopia zapasowa: {1}",
        'move_success_title': "Pomyślnie przesunięto",
        'pages_moved_voice': "Pomyślnie przesunięto {0} stron",
        'mark_removed': "Usunięto oznaczenie strony {0}",
        'mark_empty': "Oznaczono stronę {0} jako pustą",
        'mark_export_removed': "Usunięto oznaczenie eksportu dla strony {0}",
        'mark_export': "Oznaczono stronę {0} do eksportu",
        'no_empty_pages': "Brak pustych stron oznaczonych do usunięcia",
        'delete_empty_confirm': "Czy chcesz usunąć wszystkie {0} oznaczone puste strony?",
        'delete_empty_confirm_voice': "Czy teraz usunąć wszystkie {0} oznaczone puste strony? Tak lub Nie.",
        'empty_pages_deleted': "Usunięto {0} pustych stron",
        'no_export_pages': "Brak stron oznaczonych do eksportu",
        'overwrite_title': "Nadpisać istniejący plik?",
        'overwrite_question': "Plik\n\n{0}\n\njuż istnieje.\nCzy chcesz go nadpisać?",
        'overwrite_voice': "Nadpisać istniejący plik? Tak lub Nie.",
        'page_skipped': "Pominięto stronę {0}",
        'export_complete': "Eksport zakończony.",
        'export_complete_voice': "Eksport został zakończony.",
        'no_pages_exported': "Nie wyeksportowano żadnej strony",
        'export_cancelled': "Eksport anulowany",
        'pages_exported': "Eksportowano {0} stron do {1}",
        'export_page_title': "Eksportuj stronę",
        'page_exported': "Eksportowano stronę {0} do {1}",
        'export_error': "Błąd eksportu",
        'export_marked_title': "Eksportuj oznaczone strony",
        'rotate_all_title': "obróć wszystkie strony",
        'rotate_all_question': "Czy chcesz obrócić wszystkie strony o 90 stopni w prawo?",
        'rotate_all_voice': "Czy chcesz obrócić wszystkie strony o 90 stopni w prawo? Tak lub Nie?",
        'all_pages_rotated': "Obrócono wszystkie strony",
        'page_rotated': "Obrócono stronę {0}",
        'rotate_error': "Nie można obrócić strony",
        'delete_page_confirm': "Czy chcesz usunąć stronę {0}?",
        'delete_page_confirm_voice': "Czy na pewno chcesz usunąć stronę {0}? Tak lub Nie.",
        'page_deleted': "Usunięto stronę {0}",
        'delete_error': "Nie można usunąć strony",
        'pages_deleted_voice': "Usunięto {0} stron",
        'pages_exported_split': "Pomyślnie wyeksportowano {0} stron.",
        'pages_skipped': "Pominięto {0} stron.",

        # ============================================
        # 14.2 SEITENOPERATIONEN - Seiten entnehmen (SPLITTER)
        # ============================================
        'edit_extract_pages_advanced': "Wyodrębnij strony (zaawansowane)",
        'pdf_splitter_title': "Splitter i ekstraktor PDF",
        'pdf_splitter_load': " Wybierz plik PDF",
        'pdf_splitter_info': "Wybierz opcję dla swojego dokumentu PDF",
        'pdf_splitter_basic': "Podstawowe operacje",
        'pdf_splitter_single': "Podziel na pojedyncze strony",
        'pdf_splitter_range': "Wyodrębnij strony:",
        'pdf_splitter_range_placeholder': "np. 1-3,5,7-9",
        'pdf_splitter_clean': "Operacje czyszczenia",
        'pdf_splitter_remove_empty': "Usuń wszystkie puste strony",
        'pdf_splitter_remove': "Usuń zakres stron:",
        'pdf_splitter_remove_placeholder': "np. 2,4-6",
        'pdf_splitter_process': "Przetwórz PDF",
        'pdf_splitter_loaded': "PDF załadowany. Wybierz opcję",
        'pdf_read_error': "Nie można odczytać PDF",
        'pages': "stron",
        'pages_created': "Utworzono strony",
        'range_empty': "Wprowadź zakres stron",
        'range_invalid': "Nieprawidłowy zakres stron",
        'range_created': "Utworzono nowy PDF z wybranymi stronami:\n{0}",
        'empty_removed': "Usunięto {0} pustych stron.\nWynik: {1}",
        'remove_empty': "Wprowadź strony do usunięcia",
        'remove_invalid': "Nieprawidłowe strony do usunięcia",
        'remove_done': "Utworzono oczyszczony PDF:\n{0}",
        'open_folder': "Otwórz folder",
        'show_in_finder': "Pokaż w Finderze",
        'pdf_splitter_no_pdf': "Najpierw załaduj plik PDF.",
        'process_error': "Błąd podczas przetwarzania PDF",
        'pages_created_voice': "Utworzono {0} stron",
        'range_created_voice': "Utworzono PDF z wybranymi stronami",
        'empty_removed_voice': "Usunięto {0} pustych stron",
        'remove_done_voice': "Utworzono oczyszczony PDF",
        'pdf_splitter_split_groups': "Każdą spójną grupę do osobnego pliku",
        'range_created_single': "Utworzono nowy PDF:\n{0}",
        'range_created_multiple': "Utworzono {0} plików PDF.",
        'range_created_voice_single': "Utworzono PDF z wybranymi stronami",
        'range_created_voice_multiple': "Utworzono {0} plików PDF",
        'empty_removed_none_left': "Brak pozostałych stron",
        'empty_removed_all_empty': "Wszystkie strony zostały uznane za puste i zostałyby usunięte. Nie utworzono pliku.",
        'preview_single': "Podgląd: {0}",
        'preview_enter_range': "Wprowadź zakres stron.",
        'preview_invalid_range': "Nieprawidłowy zakres stron.",
        'preview_file': "Podgląd: {0}",
        'preview_files': "Podgląd: {0}",

        # ============================================
        # 15. DRUCKEN
        # ============================================
        'print_start': "Rozpoczynanie drukowania",
        'print_sent': "Zlecenie druku wysłane",
        'print_now': "Drukuj natychmiast",
        'print_error': "Błąd druku natychmiastowego",
        'print_limited': "Funkcja drukowania ograniczona w tym systemie",
        'print_error_format': "Błąd druku natychmiastowego: {0}",
        'warning': "Uwaga",

        # ============================================
        # 16. DARK/LIGHT MODE
        # ============================================
        'mode_switch_to_light': "Przełącz na tryb jasny",
        'mode_switch_to_dark': "Przełącz na tryb ciemny",
        'mode_dark_activated': "Tryb ciemny włączony",
        'mode_light_activated': "Tryb jasny włączony",

        # ============================================
        # 17. ZOOM-MODI
        # ============================================
        'zoom_page': "Pełny widok",
        'zoom_two_pages': "Dwie strony obok siebie",
        'zoom_overview': "Tryb przeglądu",
        'zoom_cannot_during_search': "Zoom podczas wyszukiwania niedostępny",
        'zoom_exit_first': "Najpierw wyjdź z zoomu",

        # ============================================
        # 18. DRAG & DROP
        # ============================================
        'drag_enabled': "Przeciąganie i upuszczanie włączone",
        'drag_disabled': "Przeciąganie i upuszczanie wyłączone",
        'drag_page_grab': "Chwycono stronę {0}",
        'drag_page_dropped': "Wstawiono stronę {0} na pozycję {1}",
        'drag_position_invalid': "Nieprawidłowa pozycja",
        'drag_same_position': "Strona {0} pozostaje na pozycji {0}",
        'drag_error': "Błąd podczas przesuwania",

        # ============================================
        # 19.1 TEXTEINGABE
        # ============================================
        'text_input': "Wprowadzanie tekstu z zaawansowanym formatowaniem i zarządzaniem fragmentami",
        'text_templates': "Dostępne fragmenty tekstu:",
        'text_name': "Nazwa",
        'text_preview': "Podgląd tekstu",
        'text_enter': "Tekst:",
        'text_font_size': "Rozmiar czcionki:",
        'text_formatting': "Formatowanie:",
        'text_bold': "Pogrubienie",
        'text_italic': "Kursywa",
        'text_underline': "Podkreślenie",
        'text_alignment': "Wyrównanie:",
        'text_left': "Do lewej",
        'text_center': "Wyśrodkowany",
        'text_right': "Do prawej",
        'text_color': "Kolor tekstu:",
        'text_opacity': "Przezroczystość:",
        'text_word_wrap': "Zawijanie wierszy:",
        'text_auto': "Automatyczne",
        'text_page_width_95': "Szerokość strony (95%)",
        'text_page_width_85': "Bardzo szeroki (85%)",
        'text_page_width_75': "Szeroki (75%)",
        'text_page_width_60': "Szeroki (60%)",
        'text_page_width_50': "Średni (50%)",
        'text_page_width_30': "Wąski (30%)",
        'text_page_width_20': "Węższy (20%)",
        'text_page_width_10': "Bardzo wąski (10%)",
        'text_no_wrap': "Bez zawijania",
        'text_private': "Prywatny fragment tekstu (wymaga uwierzytelnienia)",
        'text_preview_label': "Podgląd:",
        'text_preview_placeholder': "Tutaj pojawi się podgląd tekstu...",
        'text_no_text': "(Brak tekstu)",
        'text_save_template': "Zapisz jako fragment",
        'text_delete_template': "Usuń wybrany fragment",
        'text_show_private': "Pokaż prywatne",
        'text_hide_private': "Ukryj prywatne",
        'text_use': "Użyj tekstu",
        'text_saved': "Fragment tekstu zapisany jako:\n{0}",
        'text_saved_voice': "Zapisano fragment tekstu",
        'text_deleted': "Usunięto fragment tekstu",
        'text_no_text_to_save': "Brak tekstu do zapisania.",
        'text_no_templates': "Nie znaleziono fragmentów tekstu",
        'text_private_master_required': "Prywatne fragmenty mogą być używane tylko po ustawieniu hasła głównego.\n\nCzy chcesz teraz ustawić hasło główne?",
        'text_filename': "Nazwa pliku dla fragmentu (bez 'Text_' i '.txt'):",
        'text_filename_hint': "Przykład: 'Telefon HomeOffice' zostanie zapisany jako 'Text_Telefon HomeOffice.txt'",
        'text_save_hint': "Fragment tekstu zostanie automatycznie zapisany z formatowaniem.",
        'text_guide_title': "Wprowadzanie tekstu - instrukcja",
        'text_delete_confirm': "Czy na pewno chcesz usunąć fragment tekstu?\n\nPlik: {0}\nTekst: {1}...",
        'text_make_public': "Oznacz jako publiczny",
        'text_make_private': "Oznacz jako prywatny",
        'text_privacy_changed': "Zmieniono status prywatności",
        'text_private_always': "Prywatne zawsze widoczne (ustawienie)",
        'text_mode_required': "Najpierw włącz tryb tekstowy",
        'text_continue_editing': "Kontynuuj edycję - kursor na końcu tekstu",
        'text_no_input': "Nie wprowadzono tekstu - odrzucono",
        'save_dialog_question': "Jak chcesz kontynuować?",
        'text_save_question': "Zapisać wszystkie teksty i krzyżyki, dostosować, kontynuować edycję czy odrzucić?",
        'copy_cross': "Skopiowano krzyżyk",
        'paste_cross': "Wklejono krzyżyk",
        'paste_text': "Wklejono tekst",
        'cross_discarded': "Odrzucono krzyżyk",
        'all_discarded': "Odrzucono wszystko",
        'text_discarded': "Odrzucono tekst",
        'no_texts_to_save': "Brak tekstów do zapisania",
        'no_valid_texts': "Brak poprawnych tekstów do zapisania",
        'text_word_singular': "tekst",
        'text_word_plural': "teksty",
        'cross_word_singular': "krzyżyk",
        'cross_word_plural': "krzyżyki",
        'texts_saved_title': "Zapisano teksty",
        'texts_crosses_saved': "Zapisano {0} {1} i {2} {3} w PDF.\n\nPrzeładowano PDF...",
        'texts_crosses_saved_voice': "Zapisano {0} {1} i {2} {3}.",
        'texts_saved': "Zapisano {0} {1} w PDF.\n\nPrzeładowano PDF...",
        'texts_saved_voice': "Zapisano {0} {1}.",
        'crosses_saved': "Zapisano {0} {1} w PDF.\n\nPrzeładowano PDF...",
        'crosses_saved_voice': "Zapisano {0} {1}.",
        'elements_saved': "Zapisano {0} elementów w PDF.\n\nPrzeładowano PDF...",
        'elements_saved_voice': "Zapisano {0} elementów.",
        'text_window_load_error': "Nie można załadować okna tekstu",

        # ============================================
        # 19.2 TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed': """
        📝 **Wprowadzanie tekstu i fragmenty tekstu – szczegółowa instrukcja**

        **1. Wstawianie i edycja tekstu**
        - Kliknij prawym przyciskiem myszy w żądanym miejscu dokumentu i wybierz "Wstaw tekst".
        - Otworzy się okno dialogowe, w którym możesz wprowadzić i sformatować tekst:
        • Rozmiar czcionki, pogrubienie, kursywa, podkreślenie
        • Kolor tekstu (do wyboru)
        • Przezroczystość (przez suwak)
        • Zawijanie wierszy (różne szerokości, np. szerokość strony, wąski, bez zawijania)
        - Po zatwierdzeniu tekst pojawi się w miejscu kliknięcia. Możesz go przesuwać myszą lub klawiszami strzałek.
        - Dwuklik na tekście otwiera tryb edycji; naciśnij ESC, aby go opuścić.

        **2. Zarządzanie fragmentami tekstu (szablonami)**
        - W oknie dialogowym tekstu po lewej stronie znajduje się lista wszystkich zapisanych fragmentów.
        - **Zapisanie fragmentu:** Wprowadź tekst, sformatuj go i kliknij "💾 Zapisz jako fragment". Podaj nazwę pliku (bez rozszerzenia).
        - **Wczytanie fragmentu:** Kliknij na żądaną nazwę na liście. Tekst i formatowanie zostaną załadowane i w razie potrzeby można je dostosować.
        - **Usuwanie:** Kliknij prawym przyciskiem na fragment, aby go usunąć lub zmienić jego status prywatności.

        **3. Prywatne fragmenty tekstu (hasło główne)**
        - Jeśli ustawiłeś hasło główne (w Ustawienia → Zarządzanie hasłami), możesz oznaczyć fragmenty jako "prywatne".
        - Zaznacz pole wyboru "Prywatny fragment tekstu" w oknie dialogowym przed zapisaniem.
        - Prywatne fragmenty są wyświetlane na liście tylko po wprowadzeniu hasła głównego raz na sesję (uwierzytelnienie przez ikonę kłódki lub przy pierwszym dostępie).
        - Pozwala to chronić poufne fragmenty przed niepowołanym dostępem.

        **4. Wstawianie krzyżyków**
        - Z menu kontekstowego możesz również wstawić graficzny krzyżyk (np. do pól wyboru).
        - Rozmiar, grubość linii i kolor krzyżyków można dostosować globalnie w ustawieniach (menu "Ustawienia" → "Ustawienia krzyżyków").
        - Kliknij prawym przyciskiem na istniejący krzyżyk, aby go zmodyfikować indywidualnie.

        **5. Operacje zbiorcze**
        - Jeśli umieściłeś na stronie wiele tekstów lub krzyżyków, możesz za pomocą menu kontekstowego (prawy przycisk w trybie tekstowym) zapisać lub odrzucić wszystkie elementy jednocześnie.
        - Podczas zapisywania wszystkie elementy są osadzane w PDF i pozostają jako grafiki wektorowe.

        **6. Skróty klawiaturowe w trybie tekstowym**
        - Klawisze strzałek: przesuwanie elementu
        - Ctrl+strzałki: większe kroki
        - Enter: otwiera okno zapisu (zapisz wszystko / dostosuj / odrzuć)
        - ESC: odrzuca bieżący element
        """,

        # ============================================
        # 19.3 HTML TEXT-ANLEITUNG (ausführlich)
        # ============================================
        'text_guide_detailed_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📝 Wprowadzanie tekstu i fragmenty tekstu – szczegółowa instrukcja</strong></p>

        <p><strong>1. Wstawianie i edycja tekstu</strong></p>
        <ul>
        <li>Kliknij prawym przyciskiem myszy w żądanym miejscu dokumentu i wybierz "Wstaw tekst".</li>
        <li>Otworzy się okno dialogowe, w którym możesz wprowadzić i sformatować tekst:<br/>
        • Rozmiar czcionki, pogrubienie, kursywa, podkreślenie<br/>
        • Kolor tekstu (do wyboru)<br/>
        • Przezroczystość (przez suwak)<br/>
        • Zawijanie wierszy (różne szerokości, np. szerokość strony, wąski, bez zawijania)</li>
        <li>Po zatwierdzeniu tekst pojawi się w miejscu kliknięcia. Możesz go przesuwać myszą lub klawiszami strzałek.</li>
        <li>Dwuklik na tekście otwiera tryb edycji; naciśnij ESC, aby go opuścić.</li>
        </ul>

        <p><strong>2. Zarządzanie fragmentami tekstu (szablonami)</strong></p>
        <ul>
        <li>W oknie dialogowym tekstu po lewej stronie znajduje się lista wszystkich zapisanych fragmentów.</li>
        <li><strong>Zapisanie fragmentu:</strong> Wprowadź tekst, sformatuj go i kliknij "💾 Zapisz jako fragment". Podaj nazwę pliku (bez rozszerzenia).</li>
        <li><strong>Wczytanie fragmentu:</strong> Kliknij na żądaną nazwę na liście. Tekst i formatowanie zostaną załadowane i w razie potrzeby można je dostosować.</li>
        <li><strong>Usuwanie:</strong> Kliknij prawym przyciskiem na fragment, aby go usunąć lub zmienić jego status prywatności.</li>
        </ul>

        <p><strong>3. Prywatne fragmenty tekstu (hasło główne)</strong></p>
        <ul>
        <li>Jeśli ustawiłeś hasło główne (w Ustawienia → Zarządzanie hasłami), możesz oznaczyć fragmenty jako "prywatne".</li>
        <li>Zaznacz pole wyboru "Prywatny fragment tekstu" w oknie dialogowym przed zapisaniem.</li>
        <li>Prywatne fragmenty są wyświetlane na liście tylko po wprowadzeniu hasła głównego raz na sesję (uwierzytelnienie przez ikonę kłódki lub przy pierwszym dostępie).</li>
        <li>Pozwala to chronić poufne fragmenty przed niepowołanym dostępem.</li>
        </ul>

        <p><strong>4. Wstawianie krzyżyków</strong></p>
        <ul>
        <li>Z menu kontekstowego możesz również wstawić graficzny krzyżyk (np. do pól wyboru).</li>
        <li>Rozmiar, grubość linii i kolor krzyżyków można dostosować globalnie w ustawieniach (menu "Ustawienia" → "Ustawienia krzyżyków").</li>
        <li>Kliknij prawym przyciskiem na istniejący krzyżyk, aby go zmodyfikować indywidualnie.</li>
        </ul>

        <p><strong>5. Operacje zbiorcze</strong></p>
        <ul>
        <li>Jeśli umieściłeś na stronie wiele tekstów lub krzyżyków, możesz za pomocą menu kontekstowego (prawy przycisk w trybie tekstowym) zapisać lub odrzucić wszystkie elementy jednocześnie.</li>
        <li>Podczas zapisywania wszystkie elementy są osadzane w PDF i pozostają jako grafiki wektorowe.</li>
        </ul>

        <p><strong>6. Skróty klawiaturowe w trybie tekstowym</strong></p>
        <ul>
        <li>Klawisze strzałek: przesuwanie elementu</li>
        <li>Ctrl+strzałki: większe kroki</li>
        <li>Enter: otwiera okno zapisu (zapisz wszystko / dostosuj / odrzuć)</li>
        <li>ESC: odrzuca bieżący element</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 20. KREUZE
        # ============================================
        'cross_title': "Ustawienia krzyżyków",
        'cross_properties': "Właściwości krzyżyka",
        'cross_size': "Rozmiar (px):",
        'cross_line_width': "Grubość linii:",
        'cross_color': "Kolor:",
        'cross_choose_color': "Wybierz",
        'cross_fine_tuning': "Dostrajanie przy zapisie (piksele)",
        'cross_offset_x': "Przesunięcie X:",
        'cross_offset_y': "Przesunięcie Y:",
        'cross_offset_x_tooltip': "Ujemne wartości przesuwają krzyżyk w lewo, dodatnie w prawo",
        'cross_offset_y_tooltip': "Ujemne wartości przesuwają krzyżyk w górę, dodatnie w dół",
        'cross_preview': "Podgląd",
        'cross_save': "Zastosuj ustawienia",
        'cross_customized': "Dostosowano krzyżyk",
        'cross_settings_applied': "Zapisano ustawienia krzyżyków.\nRozmiar: {0}px, grubość linii: {1}px\n{2}",
        'cross_updated_count': "Zaktualizowano {0} istniejących krzyżyków.",
        'cross_no_crosses': "Nie znaleziono istniejących krzyżyków.",
        'cross_settings_applied_all': "Zastosowano ustawienia krzyżyków dla wszystkich {0} krzyżyków",

        # ============================================
        # 21. SIGNATUREN
        # ============================================
        'signature_settings': "Ustawienia podpisu",
        'signature_1': "Podpis 1",
        'signature_2': "Podpis 2",
        'signature_select': "Wybierz podpis",
        'signature_add': "Dodaj nowy podpis...",
        'signature_size': "Rozmiar dla podpisu {0} (%):",
        'signature_common': "Ustawienia ogólne",
        'signature_timestamp': "Automatycznie dodawaj znacznik czasu",
        'signature_location': "Domyślna lokalizacja:",
        'signature_timestamp_size': "Rozmiar czcionki znacznika czasu:",
        'signature_no_files': "-- Nie znaleziono podpisów --",
        'signature_insert': "Wstaw podpis",
        'signature_insert_1': "Wstaw podpis 1",
        'signature_insert_2': "Wstaw podpis 2",
        'signature_customize': " Dostosuj podpis",
        'signature_discard': " Odrzuć ten podpis",
        'signature_save_all': " Zapisz wszystkie podpisy",
        'signature_discard_all': " Odrzuć wszystkie podpisy",
        'signature_guide_title': "Podpisy – instrukcja",
        'signature_guide': """
📝 Podpisy – krótka instrukcja

- Ustaw hasło główne
- Skonfiguruj podpisy w menu Ustawienia
  (rozmiar, znacznik czasu ...)
- Wstaw za pomocą PRAWEgo PRZYCIsku w żądanym miejscu
  (hasło główne wymagane raz na sesję)
- Przesuwaj podpis myszą lub klawiszami strzałek
- Można wstawić wiele podpisów jeden po drugim
- Każdy podpis można dostosować indywidualnie
- Odrzuć pojedynczy podpis
- Zapisz / odrzuć wszystkie podpisy jednocześnie
- Alternatywnie można użyć paska menu.
        """,
        'signature_placeholder': "Brak podglądu",
        'signature_info': "Podpis {0}: {1}×{2} px ({3}% z {4}×{5})",
        'signature_info_placeholder': "Ustawienia dla podpisu {0}",
        'signature_inserted': "Wstawiono podpis {0} na stronie {1}",
        'signature_deleted': "Usunięto podpis",
        'signature_copied': "Skopiowano podpis",
        'signature_pasted': "Wklejono podpis {0}",
        'signature_saved': "Zapisano {0} podpisów w PDF.\n\nPrzeładowano PDF...",
        'signature_saved_voice': "Zapisano {0} podpisów",
        'mode_replace_signature_format': "Zakończ tryb i wstaw podpis {0}",
        'mode_conflict_voice_signature': "Tryb {0} jest aktywny. Zakończyć i wstawić podpis?",
        'signature_not_configured': "Podpis {0} nie skonfigurowany",
        'signature_file_not_found': "Nie znaleziono pliku podpisu",
        'timestamp_format': "{0}, dnia {1}",
        'no_copied_signature': "Brak skopiowanego podpisu",
        'no_signatures_to_save': "Brak podpisów do zapisania",
        'signature_save_question': "Zapisać wszystkie podpisy, dostosować czy odrzucić ten?",
        'signatures_saved_title': "Zapisano podpisy",
        'signatures_saved': "Zapisano {0} podpisów w PDF.\n\nPrzeładowano PDF...",
        'signatures_saved_voice': "Zapisano {0} podpisów.",
        'all_signatures_discarded': "Odrzucono wszystkie podpisy",
        'signature_settings_saved': "Zapisano ustawienia podpisów",
        'signature_cancelled': "Odrzucono podpis",
        'signature_active_title': "Podpis aktywny",
        'signature_replace_question': "Podpis jest już aktywny.\n\nCzy chcesz zastąpić bieżący podpis?",
        'signature_replace': "Zastąp podpis",
        'signature_replace_voice': "Zastąpić bieżący podpis czy anulować?",

        # ============================================
        # 22. BILDER
        # ============================================
        'image_settings': "Ustawienia obrazów",
        'image_common': "Ogólne ustawienia obrazów",
        'image_keep_aspect': "Zachowaj proporcje podczas przeciągania",
        'image_default_size': "Domyślny rozmiar (%):",
        'image_dark_invert': "Odwracaj obrazy w trybie ciemnym",
        'image_dark_invert_tooltip': "Włączone: obrazy są odwracane dla lepszej widoczności",
        'image_fine_tuning': "Dostrajanie (piksele)",
        'image_offset_x': "Przesunięcie X:",
        'image_offset_y': "Przesunięcie Y:",
        'image_offset_x_tooltip': "Ujemne wartości przesuwają obraz w lewo, dodatnie w prawo",
        'image_offset_y_tooltip': "Ujemne wartości przesuwają obraz w górę, dodatnie w dół",
        'image_select': "Wybierz obraz",
        'image_insert': "Wstaw obraz",
        'image_customize': " Dostosuj obraz",
        'image_aspect': " Zachowaj proporcje",
        'image_discard': " Odrzuć ten obraz",
        'image_save_all': " Zapisz wszystkie obrazy",
        'image_discard_all': " Odrzuć wszystkie obrazy",
        'image_filter': "Obrazy",
        'image_guide_title': "Wstawianie obrazów – instrukcja",
        'image_guide': """
📷 Wstawianie obrazów do PDF – krótka instrukcja:

1. Kliknij prawym przyciskiem w żądanym miejscu
2. "Wstaw obraz" → wybierz obraz
3. Pozycjonowanie: przeciągaj myszą
4. Zmiana rozmiaru: przeciągaj za rogi/krawędzie
5. Zachowaj proporcje: klawisz [A]
6. Dalsze dostosowania: prawy przycisk na obrazie

Wskazówka: W menu kontekstowym można dostosować ustawienia.
        """,
        'image_inserted': "Wstawiono obraz {0} na stronie {1}",
        'image_deleted': "Odrzucono obraz",
        'image_copied': "Skopiowano obraz",
        'image_pasted': "Wklejono obraz",
        'image_saved': "Zapisano {0} obrazów w PDF.\n\nPrzeładowano PDF...",
        'image_saved_voice': "Zapisano {0} obrazów",
        'image_aspect_on': "włączone",
        'image_aspect_off': "wyłączone",
        'image_aspect_toggle': "Zachowaj proporcje {0}",
        'image_reset': "Przywrócono oryginalny rozmiar obrazu",
        'image_replaced': "Zastąpiono obraz",
        'image_invalid': "Nieprawidłowy obraz",
        'mode_replace_image': "Wstaw obraz",
        'mode_conflict_voice_image': "Tryb {0} jest aktywny. Zakończyć i wstawić obraz?",
        'image_active_title': "Obraz aktywny",
        'image_replace_question': "Obraz jest już aktywny.\n\nCzy chcesz zastąpić bieżący obraz?",
        'image_replace': "Zastąp obraz",
        'image_replace_voice': "Zastąpić bieżący obraz czy anulować?",
        'image_filter_all': "Obrazy (*.png *.jpg *.jpeg *.bmp *.tiff *.gif *.webp);;Wszystkie pliki (*.*)",
        'no_copied_image': "Brak skopiowanego obrazu",
        'image_discarded': "Odrzucono obraz",
        'image_save_question': "Zapisać wszystkie obrazy, dostosować czy odrzucić ten?",
        'no_images_to_save': "Brak obrazów do zapisania",
        'no_valid_images': "Brak poprawnych obrazów do zapisania",
        'images_saved_title': "Zapisano obrazy",
        'images_saved': "Zapisano {0} obrazów w PDF.\n\nPrzeładowano PDF...",
        'images_saved_voice': "Zapisano {0} obrazów.",
        'all_images_discarded': "Odrzucono wszystkie obrazy",
        'image_settings_updated': "Zaktualizowano ustawienia obrazów",
        'image_replace_title': "Wybierz nowy obraz",

        # ============================================
        # 23. FORMEN
        # ============================================
        'form_settings': "Ustawienia kształtów",
        'form_basic': "Ustawienia podstawowe",
        'form_default_type': "Domyślny typ kształtu:",
        'form_rectangle': "Prostokąt",
        'form_ellipse': "Elipsa",
        'form_line': "Linia",
        'form_arrow': "Strzałka",
        'form_line_width': "Grubość linii:",
        'form_colors': "Kolory",
        'form_line_color': "Kolor linii:",
        'form_fill_color': "Kolor wypełnienia:",
        'form_choose_color': "Wybierz",
        'form_transparent': "Przezroczyste tło (tylko linia)",
        'form_filled': "wypełnione",
        'form_dark_mode': "Tryb ciemny",
        'form_dark_invert': "Odwracaj kolory w trybie ciemnym",
        'form_fine_tuning': "Dostrajanie (piksele)",
        'form_offset_x': "Przesunięcie X:",
        'form_offset_y': "Przesunięcie Y:",
        'form_offset_x_tooltip': "Ujemne wartości przesuwają kształt w lewo, dodatnie w prawo",
        'form_offset_y_tooltip': "Ujemne wartości przesuwają kształt w górę, dodatnie w dół",
        'form_preview': "Podgląd",
        'form_insert': "Wstaw kształt",
        'form_rectangle_insert': "Prostokąt",
        'form_ellipse_insert': "Koło / Elipsa",
        'form_line_insert': "Linia (2 kliknięcia)",
        'form_arrow_insert': "Strzałka (2 kliknięcia)",
        'form_customize': " Dostosuj kształt",
        'form_transparent_toggle': " Przezroczyste tło",
        'form_discard': " Odrzuć ten kształt",
        'form_save_all': " Zapisz wszystkie kształty",
        'form_discard_all': " Odrzuć wszystkie kształty",
        'form_guide_title': "Wstawianie kształtów – instrukcja",
        'form_guide': """
📐 Wstawianie kształtów do PDF – krótka instrukcja:

1. Wybierz typ kształtu (prostokąt, koło/elipsa, linia, strzałka)
2. Kliknij w miejscu docelowym
   - Dla prostokąta/elipsy: jedno kliknięcie umieszcza kształt
   - Dla linii/strzałki: dwa kliknięcia dla punktu początkowego i końcowego
3. Pozycjonuj kształt: przeciągaj myszą
4. Zmień rozmiar: przeciągaj za rogi/krawędzie
5. Zapisz kształt: Enter
6. Odrzuć kształt: ESC
7. Dalsze dostosowania: prawy przycisk na kształcie

Wskazówka: W menu kontekstowym można dostosować ustawienia.
        """,
        'form_inserted': "Wstawiono {0} na stronie {1}",
        'form_deleted': "Usunięto kształt",
        'form_copied': "Skopiowano kształt",
        'form_pasted': "Wklejono kształt",
        'form_saved': "Zapisano {0} kształtów w PDF.\n\nPrzeładowano PDF...",
        'form_saved_voice': "Zapisano {0} kształtów",
        'form_reset': "Przywrócono domyślny rozmiar kształtu",
        'form_transparent_on': "włączone",
        'form_transparent_off': "wyłączone",
        'form_transparent_toggled': "Przezroczyste tło {0}",
        'form_line_cancel': "Anulowano rysowanie linii",
        'form_second_click': "Teraz kliknij punkt końcowy dla {0}",
        'mode_replace_form': "Wstaw kształt",
        'mode_conflict_voice_form': "Tryb {0} jest aktywny. Zakończyć i wstawić kształt?",
        'form_settings_updated': "Zaktualizowano ustawienia kształtów",
        'form_unknown': "Kształt",

        # ============================================
        # 24. FORM-LINE DIALOG
        # ============================================
        'form_line_guide_1': "1. Kliknij punkt początkowy",
        'form_line_guide_2': "2. Kliknij punkt końcowy",
        'form_line_guide_3': "Linia zostanie narysowana między dwoma punktami.",
        'form_line_status_1': "Oczekiwanie na pierwsze kliknięcie...",
        'form_line_status_2': "Ustawiono pierwszy punkt: ({0:.0f}, {1:.0f})",
        'form_line_status_3': "Teraz kliknij punkt końcowy...",
        'form_line_status_4': "Oba punkty ustawione.\nKliknij 'Gotowe', aby zapisać.",
        'form_line_reset': "Resetuj",
        'form_line_finish': "Gotowe",

        # ============================================
        # 25. COPY & PASTE
        # ============================================
        'copy': "Kopiuj (Cmd+C)",
        'paste': "Wklej (Cmd+V)",
        'copied': "Skopiowano: {0}",
        'no_element_to_copy': "Nie wybrano elementu do skopiowania",
        'no_copied_data': "Brak skopiowanych danych",
        'no_valid_position': "Brak prawidłowej pozycji do wklejenia",
        'copy_text': "Skopiowano tekst",
        'copy_image': "Skopiowano obraz",
        'copy_form': "Skopiowano kształt",
        'copy_signature': "Skopiowano podpis",
        'element_text': "Tekst",
        'element_image': "Obraz",
        'element_form': "Kształt",
        'element_signature': "Podpis",
        'element_unknown': "Element",

        # ============================================
        # 26. KONFLIKT-DIALOGE
        # ============================================
        'mode_conflict': "Konflikt trybów",
        'mode_conflict_message': "Tryb '{0}' jest już aktywny.\n\nCzy chcesz go zakończyć i {1}?",
        'mode_replace': "Zakończ tryb i {0}",
        'mode_cancel': "Anuluj",
        'mode_replace_text': "wstaw tekst",
        'mode_replace_cross': "wstaw krzyżyk",
        'mode_replace_signature': "wstaw podpis",
        'mode_replace_image': "wstaw obraz",
        'mode_replace_form': "wstaw kształt",
        'mode_conflict_voice': "Tryb {0} jest aktywny. Zakończyć i wstawić tekst?",

        # ============================================
        # 27. AKTIVE MODI
        # ============================================
        'active_mode_text': "Wprowadzanie tekstu",
        'active_mode_signature': "Podpis",
        'active_mode_image': "Obraz",
        'active_mode_form': "Kształt",
        'active_mode_and': " i ",

        # ============================================
        # 28. EINFÜGE-DIALOGE
        # ============================================
        'insert_another': "Wstaw",
        'insert_another_text': "Wstaw tekst",
        'insert_another_cross': "Wstaw krzyżyk",
        'insert_another_signature_1': "Podpis 1",
        'insert_another_signature_2': "Podpis 2",
        'insert_another_image': "Wstaw obraz",
        'insert_another_form_rect': "Prostokąt",
        'insert_another_form_ellipse': "Koło / Elipsa",
        'insert_another_form_line': "Linia (2 kliknięcia)",
        'insert_another_form_arrow': "Strzałka (2 kliknięcia)",

        # ============================================
        # 29. SPEICHERDIALOGE
        # ============================================
        'save_dialog_title': "Zapisz {0}",
        'save_dialog_message': "{0} zostanie zapisany na stronie {1}.\n\nJak chcesz kontynuować?",
        'save_all': "Zapisz wszystkie {0}",
        'save_single': "Zapisz {0}",
        'save_customize': "Dostosuj {0}",
        'save_discard': "Odrzuć ten {0}",
        'save_continue': "Kontynuuj edycję",

        # ============================================
        # 30. KONTEXTMENÜ
        # ============================================
        'context_goto_page': " Przejdź do strony {0}",
        'context_rotate': " Obróć stronę {0}",
        'context_delete': " Usuń stronę {0}",
        'context_export': " Eksportuj stronę {0}",
        'context_mark_as': " Oznacz stronę jako...",
        'context_mark_empty': " Pusta strona",
        'context_unmark_empty': " Nie pusta",
        'context_mark_export': " Oznacz do eksportu",
        'context_unmark_export': " Nie eksportuj",
        'context_batch_actions': " Akcje zbiorcze",
        'context_batch_delete_empty': " Usuń wszystkie {0} puste strony",
        'context_batch_export_single': " Eksportuj wszystkie {0} stron (jeden plik)",
        'context_batch_export_split': " Eksportuj wszystkie {0} stron (osobno)",
        'context_drag_start': " Rozpocznij przeciąganie",
        'context_drag_stop': " Zakończ przeciąganie",
        'context_insert': " Wstaw",
        'context_insert_pages': " Wstaw strony",
        'context_zoom': "Zoom",
        'discard_mixed': "Odrzuć wszystkie {0} {1} i {2} {3}",
        'save_mixed': "Zapisz {0} {1} i {2} {3}",
        'discard_texts': "Odrzuć wszystkie {0} teksty",
        'discard_text_single': "Odrzuć 1 tekst",
        'save_texts': "Zapisz {0} teksty",
        'save_text_single': "Zapisz 1 tekst",
        'discard_crosses': "Odrzuć wszystkie {0} krzyżyki",
        'discard_cross_single': "Odrzuć 1 krzyżyk",
        'save_crosses': "Zapisz {0} krzyżyki",
        'save_cross_single': "Zapisz 1 krzyżyk",
        'discard_signatures': "Odrzuć wszystkie {0} podpisy",
        'save_signature_single': "Zapisz 1 podpis",
        'save_signatures': "Zapisz {0} podpisy",
        'discard_images': "Odrzuć wszystkie {0} obrazy",
        'save_image_single': "Zapisz 1 obraz",
        'save_images': "Zapisz {0} obrazy",
        'discard_forms': "Odrzuć wszystkie {0} kształty",
        'save_form_single': "Zapisz 1 kształt",
        'save_forms': "Zapisz {0} kształty",
        'cross_discard': "Odrzuć ten krzyżyk",

        # ============================================
        # 31. EXPORT
        # ============================================
        'export_info_title': "📦 Informacje o eksporcie / imporcie",
        'export_what': "📋 Co jest eksportowane?",
        'export_general': "Ustawienia ogólne",
        'export_general_items': "• Mowa (włącz/wyłącz, prędkość)\n• Tryb jasny/ciemny\n• Ustawienia kopii zapasowej\n• Ustawienia OCR",
        'export_image_form': "Ustawienia obrazów i kształtów",
        'export_image_form_items': "• Ustawienia obrazów (proporcje, domyślny rozmiar)\n• Ustawienia kształtów (grubość linii, kolory)\n• Ustawienia podpisów (ścieżki, rozmiary, znaczniki czasu)",
        'export_passwords': "Baza danych haseł",
        'export_passwords_items': "• Wszystkie zapisane hasła PDF\n• Opcjonalnie zaszyfrowane lub odszyfrowane",
        'export_master': "Ustawienia hasła głównego",
        'export_master_items': "• Hash hasła głównego\n• Ustawienia dla podpisów/fragmentów tekstu",
        'export_signatures': "Podpisy i fragmenty tekstu",
        'export_signatures_items': "• Wszystkie pliki obrazów (podpisy)\n• Wszystkie fragmenty tekstu z formatowaniem\n• Oznaczenia prywatne/publiczne",
        'export_import_warning': "⚠️ Ważne uwagi",
        'export_import_note': "• Podczas importu WSZYSTKIE bieżące ustawienia zostaną nadpisane\n• Wymagane jest ponowne uruchomienie aplikacji\n• Istniejące podpisy/fragmenty tekstu zostaną zastąpione",
        'export_master_note': "• Gdy hasło główne jest ustawione, możesz wybrać:\n  - Odszyfrowane (hasła w postaci jawnej)\n  - Zaszyfrowane (czytelne tylko z hasłem głównym)",
        'export_security': "• Wyeksportowany plik ZIP zawiera poufne dane\n• Przechowuj go bezpiecznie (np. zaszyfrowany pendrive)\n• W przypadku utraty pliku: hasła są bezpowrotnie utracone",
        'export_format': "📁 Format eksportu",
        'export_format_desc': "Ustawienia są zapisywane w jednym pliku ZIP:",
        'export_filename': "PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip",
        'export_success': "Ustawienia zostały pomyślnie wyeksportowane",
        'export_failed': "Eksport nie powiódł się",
        'export_import_question': "Czy chcesz teraz ponownie uruchomić aplikację?",
        'export_password_question': "Hasło główne jest ustawione.\n\nCzy chcesz wyeksportować hasła w postaci jawnej?\n(w przeciwnym razie zostaną wyeksportowane zaszyfrowane)",
        'export_decrypt': "Eksportuj odszyfrowane",
        'export_encrypt': "Eksportuj zaszyfrowane",

        # ============================================
        # 32.INFO-FENSTER - Über PDF DarkView
        # ============================================

        # -------------------- Allgemein --------------------
        'info_menu': " Informacje",
        'info_title': "O PDF Dark View",
        'info_version': "Wersja",
        'info_author': "Opracowane przez Toralfa Schulza (BinhDiez)",
        'info_copyright': "© 2026 BinhDiez",

        # -------------------- Tab 1: ÜBER --------------------
        'info_tab_about': "O programie",
        'info_about_html': """
        <div style="line-height:1.6;">
            <p><strong>PDF Dark View</strong> to dostępny przeglądarka PDF, opracowana specjalnie dla osób z wadami wzroku.</p>

            <p><strong>Kluczowe cechy:</strong></p>
            <ul>
                <li>Kontrastowy, konfigurowalny interfejs</li>
                <li>Pełna obsługa klawiatury</li>
                <li>Wbudowany syntezator mowy</li>
                <li>OCR dla zeskanowanych dokumentów</li>
                <li>Rozbudowane narzędzia edycyjne</li>
            </ul>

            <p>Obsługiwanych jest obecnie ponad 60 języków – aby PDF-y były dostępne dla wszystkich.</p>
        </div>
        """,

        # -------------------- Tab 2: FUNKTIONEN --------------------
        'info_tab_features': "Funkcje",
        'info_features_intro': "PDF Dark View oferuje następujące możliwości:",
        'info_features_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>Wyświetlanie i nawigacja</strong> – tryb jasny/ciemny, przewijanie stron, zoom, skok do strony, zakładki</li>
            <li><strong>OCR (rozpoznawanie tekstu)</strong> – uczynienie zeskanowanych dokumentów przeszukiwalnymi i kopiowalnymi</li>
            <li><strong>Edycja</strong> – wstawianie tekstu, krzyżyków, podpisów, obrazów i kształtów</li>
            <li><strong>Zarządzanie stronami</strong> – usuwanie, obracanie, wyodrębnianie, wstawianie, przesuwanie przez przeciąganie</li>
            <li><strong>Łączenie PDF</strong></li>
            <li><strong>Eksport</strong> – do Word, Pages lub jako tekst</li>
            <li><strong>Bezpieczeństwo</strong> – ochrona hasłem i zarządzanie hasłami</li>
            <li><strong>Metadane</strong> – edycja</li>
            <li><strong>Nazwy plików</strong> – centralne ustawienie dla kopii zapasowej i nazw plików przy zmianach</li>
            <li><strong>Dostępność</strong> – syntezator mowy, obsługa klawiatury, wysoki kontrast</li>
        </ul>
        """,

        # -------------------- Tab 3: BEDIENUNG --------------------
        'info_tab_shortcuts': "Obsługa",
        'info_accessibility': "♿ Dostępność – pełna obsługa klawiatury",
        'info_shortcuts_html': """
        <style>
            .shortcut-cat { font-weight: bold; margin-top: 1em; color: #ffaa66; }
            .shortcut-row { margin: 0.5em 0; }
            kbd { background: #2d2d3a; border-radius: 4px; padding: 0.2em 0.5em; font-family: monospace; border: 1px solid #5a5a6a; margin-right: 1em; display: inline-block; min-width: 160px; }
        </style>

        <div class="shortcut-cat">📌 Ogólne</div>
        <div class="shortcut-row"><kbd>Ctrl+O</kbd> Otwórz PDF</div>
        <div class="shortcut-row"><kbd>Ctrl+S</kbd> Szukaj</div>
        <div class="shortcut-row"><kbd>Ctrl+D</kbd> Przełącz tryb jasny/ciemny</div>
        <div class="shortcut-row"><kbd>Ctrl+P</kbd> Drukuj</div>
        <div class="shortcut-row"><kbd>Ctrl+Q</kbd> Zakończ</div>

        <div class="shortcut-cat">📖 Nawigacja</div>
        <div class="shortcut-row"><kbd>Strzałki</kbd> Przewijanie strony po stronie</div>
        <div class="shortcut-row"><kbd>Ctrl+G</kbd> Przejdź do strony</div>
        <div class="shortcut-row"><kbd>Home</kbd> Pierwsza strona</div>
        <div class="shortcut-row"><kbd>End</kbd> Ostatnia strona</div>

        <div class="shortcut-cat">✏️ Edycja</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+T</kbd> Wstaw tekst</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+D</kbd> Usuń strony</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+E</kbd> Wyodrębnij strony</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+I</kbd> Wstaw strony</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+M</kbd> Przesuń strony</div>
        <div class="shortcut-row"><kbd>Ctrl+Shift+R</kbd> Obróć stronę</div>

        <div class="shortcut-cat">🖼️ Przesuwanie elementów</div>
        <div class="shortcut-row"><kbd>Strzałki</kbd> Przesuwanie tekstu/obrazu/podpisu</div>
        <div class="shortcut-row"><kbd>Ctrl+Strzałki</kbd> Większe kroki</div>
        <div class="shortcut-row"><kbd>Enter</kbd> Zapisz</div>
        <div class="shortcut-row"><kbd>ESC</kbd> Odrzuć</div>

        <div class="shortcut-cat">🗣️ Syntezator mowy</div>
        <div class="shortcut-row"><kbd>F2</kbd> Włącz/wyłącz mowę</div>
        """,
        'info_contextmenu': "📌 Ważne: Wszystkie funkcje są również dostępne przez menu kontekstowe (prawy przycisk myszy)!",
        'info_accessibility_hint': "💡 Wskazówka: Syntezator mowy (F2) ułatwia orientację i dostarcza informacji zwrotnych o menu i oknach dialogowych.",

        # -------------------- Tab 4: LIZENZ (landessprachlich + englisch) --------------------
        'info_tab_license': "Licencja i stopka",

        # Landessprachlicher Lizenztext (wird in jedes Wörterbuch übersetzt)
        'info_license_html': """
        <div style="font-family: monospace; white-space: pre-wrap; font-size: 12px; line-height: 1.4;">
        <strong>📌 STOPKA</strong><br>
        Informacja zgodnie z § 5 TMG:<br>
        Toralf Schulz<br>
        Schusterstraße 3, 65582 Diez, Niemcy<br>
        E-mail: binhdiez64@gmail.com<br>
        Internet: https://github.com/BinhDiez64/PDFDarkView<br>
        Odpowiedzialny za treść: Toralf Schulz (BinhDiez)<br><br>

        <strong>Zastrzeżenie odpowiedzialności</strong><br>
        Oprogramowanie zostało opracowane z największą starannością. Nie udziela się gwarancji co do poprawności, kompletności i funkcjonalności.<br>
        Korzystanie odbywa się na własne ryzyko.<br><br>

        <strong>📄 Licencja MIT (użytek prywatny)</strong><br>
        Copyright (c) 2026 Toralf Schulz (BinhDiez)<br>
        Dozwolone: bezpłatne użytkowanie, prywatne modyfikacje, kopie osobiste.<br>
        Niedozwolone: sprzedaż, komercyjne wykorzystanie, usuwanie informacji o prawach autorskich.<br><br>

        <strong>🔧 Komponenty innych dostawców</strong><br>
        Oprogramowanie zawiera komponenty na licencjach GPL, AGPL, Apache 2.0, BSD i MIT.<br>
        Przy dalszej dystrybucji należy przestrzegać odpowiednich warunków licencyjnych.<br><br>

        <strong>🌐 Open Source</strong><br>
        Kod źródłowy jest dostępny i może być przeglądany, modyfikowany i rozpowszechniany zgodnie z odpowiednimi warunkami licencji.<br><br>

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
        'info_tab_credits': "Podziękowania",
        'info_credits': "Podziękowania dla społeczności Open Source",
        'info_credits_html': """
        <ul style="margin:0; padding-left:20px;">
            <li><strong>PyMuPDF (fitz)</strong> – przetwarzanie PDF</li>
            <li><strong>PyQt5</strong> – interfejs graficzny</li>
            <li><strong>Tesseract OCR</strong> – rozpoznawanie tekstu</li>
            <li><strong>OCRmyPDF</strong> – integracja OCR</li>
            <li><strong>python-docx</strong> – eksport do Word</li>
            <li><strong>qtawesome</strong> – ikony</li>
            <li><strong>DeepSeek</strong> – wsparcie przy tłumaczeniach (ponad 60 języków)</li>
            <li><strong>Wszystkim użytkownikom</strong> – za cenne uwagi</li>
            <li><strong>Społeczności Open Source</strong> – za świetne biblioteki</li>
        </ul>
        """,

        # -------------------- Tab 6: SPRACHEN (VOLLSTÄNDIGE LISTE) --------------------
        'info_tab_languages': "Języki",
        'info_languages_header': "🌍 Wsparcie językowe",
        'info_languages_html': """
        <div style="line-height:1.6;">
            <p>PDF Dark View obsługuje obecnie <strong>62 języki</strong> – aby oprogramowanie mogło być używane na całym świecie w sposób dostępny.</p>

            <p><strong>📖 Pełna lista języków (stan na marzec 2026):</strong></p>
            <div style="column-count: 3; column-gap: 20px; margin: 10px 0 20px 0;">
                <ul style="margin:0;">
                    <li>🇿🇦 Afrikaans</li>
                    <li>🇦🇱 Albański (Shqip)</li>
                    <li>🇩🇿 Arabski (العربية)</li>
                    <li>🇮🇩 Balijski (Basa Bali)</li>
                    <li>🇧🇩 Bengalski (বাংলা)</li>
                    <li>🇲🇲 Birmański (မြန်မာဘာသာ)</li>
                    <li>🇧🇦 Bośniacki (Bosanski)</li>
                    <li>🇧🇬 Bułgarski (Български)</li>
                    <li>🇨🇳 Chiński (中文)</li>
                    <li>🇩🇰 Duński (Dansk)</li>
                    <li>🇩🇪 Niemiecki (Deutsch)</li>
                    <li>🇬🇧 Angielski (English)</li>
                    <li>🇪🇪 Estoński (Eesti)</li>
                    <li>🇫🇮 Fiński (Suomi)</li>
                    <li>🇫🇷 Francuski (Français)</li>
                    <li>🇬🇷 Grecki (Ελληνικά)</li>
                    <li>🇮🇱 Hebrajski (עברית)</li>
                    <li>🇮🇳 Hindi (हिन्दी)</li>
                    <li>🇭🇷 Chorwacki (Hrvatski)</li>
                    <li>🇭🇺 Węgierski (Magyar)</li>
                    <li>🇮🇩 Indonezyjski (Bahasa Indonesia)</li>
                    <li>🇮🇪 Irlandzki (Gaeilge)</li>
                    <li>🇮🇸 Islandzki (Íslenska)</li>
                    <li>🇮🇹 Włoski (Italiano)</li>
                    <li>🇯🇵 Japoński (日本語)</li>
                    <li>🇰🇭 Khmerski (ភាសាខ្មែរ)</li>
                    <li>🇰🇷 Koreański (한국어)</li>
                    <li>🇱🇦 Laotański (ພາສາລາວ)</li>
                    <li>🇱🇻 Łotewski (Latviešu)</li>
                    <li>🇱🇹 Litewski (Lietuvių)</li>
                    <li>🇱🇺 Luksemburski (Lëtzebuergesch)</li>
                    <li>🇲🇾 Malajski (Bahasa Melayu)</li>
                    <li>🇮🇳 Marathi (मराठी)</li>
                    <li>🇲🇳 Mongolski (Монгол)</li>
                    <li>🇳🇵 Nepalski (नेपाली)</li>
                    <li>🇳🇱 Niderlandzki (Nederlands)</li>
                    <li>🇳🇴 Norweski (Norsk)</li>
                    <li>🇦🇫 Paszto (پښتو)</li>
                    <li>🇮🇷 Perski (فارسی)</li>
                    <li>🇵🇱 Polski</li>
                    <li>🇵🇹 Portugalski (Português)</li>
                    <li>🇮🇳 Pendżabski (ਪੰਜਾਬੀ)</li>
                    <li>🇷🇴 Rumuński (Română)</li>
                    <li>🇷🇺 Rosyjski (Русский)</li>
                    <li>🇸🇪 Szwedzki (Svenska)</li>
                    <li>🇷🇸 Serbski (Српски)</li>
                    <li>🇸🇰 Słowacki (Slovenčina)</li>
                    <li>🇸🇮 Słoweński (Slovenščina)</li>
                    <li>🇪🇸 Hiszpański (Español)</li>
                    <li>🇹🇿 Suahili (Kiswahili)</li>
                    <li>🇵🇭 Tagalog (Filipino)</li>
                    <li>🇮🇳 Tamilski (தமிழ்)</li>
                    <li>🇮🇳 Telugu (తెలుగు)</li>
                    <li>🇹🇭 Tajski (ไทย)</li>
                    <li>🇨🇿 Czeski (Čeština)</li>
                    <li>🇹🇷 Turecki (Türkçe)</li>
                    <li>🇺🇦 Ukraiński (Українська)</li>
                    <li>🇵🇰 Urdu (اردو)</li>
                    <li>🇻🇳 Wietnamski (Tiếng Việt)</li>
                    <li>🇸🇳 Wolof (Wolof)</li>
                    <li>🇺🇸 Jidysz (ייִדיש)</li>
                    <li>🇿🇦 Zulu (isiZulu)</li>
                </ul>
            </div>

            <div style="background: #3a3a4a; padding: 12px; border-radius: 8px; margin: 15px 0;">
                <strong>📁 Dodawanie własnych języków:</strong><br>
                Chcesz dodać język, którego jeszcze nie ma? Wystarczy umieścić własny plik słownika (<code>jezyk_xy.py</code>) obok aplikacji – oprogramowanie wykryje go automatycznie. W razie zainteresowania konkretnym tłumaczeniem, skontaktuj się ze mną.
            </div>

            <p><strong>🙏 Szczególne podziękowania:</strong> DeepSeek za pomoc w tłumaczeniu wszystkich słowników na 62 języki.</p>

            <p>📧 Kontakt w sprawie tłumaczeń: <strong>binhdiez64@gmail.com</strong></p>
        </div>
        """,

        # ============================================
        # 33. FEHLERMELDUNGEN
        # ============================================
        'error': "Błąd",
        'error_occurred': "Wystąpił błąd",
        'error_pdf_load': "Błąd podczas ładowania PDF",
        'error_pdf_save': "Błąd podczas zapisywania PDF",
        'error_ocr': "Błąd rozpoznawania tekstu",
        'error_no_pdf': "Nie załadowano PDF",
        'error_page_not_found': "Nie znaleziono strony",
        'error_invalid_range': "Nieprawidłowy zakres stron",
        'error_file_not_found': "Nie znaleziono pliku",
        'error_permission': "Brak uprawnień",
        'error_unknown': "Nieznany błąd",

        # ============================================
        # 34. ERFOLGSMELDUNGEN
        # ============================================
        'success': "Sukces",
        'success_operation': "Operacja zakończona pomyślnie",
        'success_saved': "Zapisano pomyślnie",
        'success_exported': "Wyeksportowano pomyślnie",
        'success_imported': "Zaimportowano pomyślnie",
        'success_deleted': "Usunięto pomyślnie",

        # ============================================
        # 35. BESTÄTIGUNGEN
        # ============================================
        'confirm': "Potwierdzenie",
        'confirm_yes': "Tak",
        'confirm_no': "Nie",
        'confirm_ok': "OK",
        'confirm_cancel': "Anuluj",
        'confirm_delete': "Usuń",
        'confirm_overwrite': "Nadpisz",
        'confirm_continue': "Kontynuuj",

        # ============================================
        # 36. FORTSCHRITT
        # ============================================
        'progress_loading': "Ładowanie PDF...",
        'progress_saving': "Zapisywanie PDF...",
        'progress_exporting': "Eksportowanie PDF...",
        'progress_processing': "Przetwarzanie...",
        'progress_wait': "Proszę czekać...",
        'progress_preparing': "Przygotowywanie...",
        'progress_finalizing': "Finalizacja...",

        # ============================================
        # 37. FARBEN
        # ============================================
        'color_white': "Biały",
        'color_black': "Czarny",
        'color_red': "Czerwony",
        'color_green': "Zielony",
        'color_blue': "Niebieski",
        'color_yellow': "Żółty",
        'color_magenta': "Magenta",
        'color_cyan': "Cyjan",
        'color_orange': "Pomarańczowy",
        'color_gray': "Szary",
        'color_custom': "Wybór koloru",

        # ============================================
        # 38. MENÜS
        # ============================================
        'menu_file': "&Plik",
        'menu_edit': "&Edycja",
        'menu_view': "&Widok",
        'menu_tools': "&Narzędzia",
        'menu_settings': "&Ustawienia",
        'menu_help': "&Pomoc",
        'menu_language': "🌐 Język",
        'menu_guides': "&Instrukcje",

        # ============================================
        # 39. DATEI-MENÜ
        # ============================================
        'file_open': "&Otwórz",
        'file_save_as': "&Zapisz jako...",
        'file_protect': "Zabezpiecz &dokument...",
        'file_export': "&Eksportuj",
        'file_export_pages': "Eksportuj jako Pages",
        'file_export_word': "Eksportuj jako DOCX",
        'file_export_text': "Eksportuj jako TXT",
        'file_print_now': "&Drukuj natychmiast",
        'file_print': "&Drukuj",
        'file_close': "&Zamknij",
        'file_quit': "&Zakończ",

        # ============================================
        # 40. BEARBEITEN-MENÜ
        # ============================================
        'edit_search': "&Szukaj",
        'edit_ocr': " Wykonaj OCR",
        'edit_rotate': "&Obróć stronę",
        'edit_rotate_all': "Obróć &wszystkie strony",
        'edit_delete_pages': "&Usuń strony",
        'edit_extract_pages': "&Wyodrębnij strony",
        'edit_insert_pages': "&Wstaw strony",
        'edit_move_pages': "&Przesuń strony",

        # ============================================
        # 41. TEXT-MENÜ
        # ============================================
        'text_menu': " Wstaw tekst i krzyżyki",
        'text_insert': " Wstaw tekst",
        'cross_insert': " Wstaw krzyżyk",
        'text_customize': " Dostosuj tekst",
        'cross_customize': " Dostosuj ten krzyżyk",
        'cross_customize_all': " Dostosuj wszystkie krzyżyki",
        'text_discard': " Odrzuć ten tekst/krzyżyk",
        'text_discard_all': " Odrzuć wszystkie teksty i krzyżyki",
        'text_save_all': " Zapisz wszystkie teksty i krzyżyki",
        'text_guide': " Wprowadzanie tekstu / fragmenty - instrukcja",

        # ============================================
        # 42. SIGNATUR-MENÜ
        # ============================================
        'signature_menu': " Wstaw podpis",
        'signature_settings_menu': " Ustawienia...",

        # ============================================
        # 43. BILD-MENÜ
        # ============================================
        'image_menu': " Wstaw obraz",

        # ============================================
        # 44. FORM-MENÜ
        # ============================================
        'form_menu': " Wstaw kształty",

        # ============================================
        # 45. ANSICHT-MENÜ
        # ============================================
        'view_text_window': "Pokaż &okno tekstowe",
        'view_zoom': "&Zoom",
        'view_zoom_page': "&Szerokość strony (domyślnie)",
        'view_zoom_two': "&Dwie strony",
        'view_zoom_overview': "&Przegląd (wiele stron)",

        # ============================================
        # 46. EINSTELLUNGEN-MENÜ
        # ============================================
        'settings_accessibility': "&Ułatwienia dostępu",
        'settings_voice': "Syntezator mowy",
        'settings_voice_tooltip': "uzupełnia mowę czytników ekranu o dodatkowe informacje",
        'settings_signature': "&Ustawienia podpisu",
        'settings_password': "&Zarządzanie hasłami",
        'settings_backup': "Twórz kopię zapasową przed zmianami",
        'settings_export_import': "&Eksportuj / importuj ustawienia",
        'settings_export': "&Eksportuj wszystkie ustawienia...",
        'settings_import': "&Importuj wszystkie ustawienia...",
        'settings_export_info': "&Co jest eksportowane?",

        # ============================================
        # 47. SPRACHAUSGABE
        # ============================================
        'voice_on': "włącz",
        'voice_off': "wyłącz",
        'voice_toggle': "Syntezator mowy {0}",
        'voice_speed': "Prędkość na {0} procent",

        # ============================================
        # 48. EXTERNE TOOLS
        # ============================================
        'tool_not_found': "Nie znaleziono narzędzia:\n{0}\n\nBASE_DIR: {1}\nUpewnij się, że narzędzia PDF są zainstalowane w katalogu {1}.",
        'tool_started': "Uruchomiono {0}",
        'tool_start_failed': "Nie można uruchomić",
        'process_error_failed_to_start': "Nie można uruchomić procesu. Czy plik istnieje?",
        'process_error_crashed': "Proces uległ awarii podczas uruchamiania.",
        'process_error_timeout': "Przekroczono limit czasu procesu.",
        'process_error_write': "Błąd zapisu w procesie.",
        'process_error_read': "Błąd odczytu w procesie.",
        'process_error_unknown': "Nieznany błąd procesu",
        'process_command': "Polecenie",
        'process_normal_exit': "zakończono normalnie",
        'process_crashed': "awaria",
        'process_nonzero_exit': "{0} zakończył się kodem błędu {1}",

        # ============================================
        # 49. WORKER-THREADS
        # ============================================
        'cancelling': "Anulowanie...",
        'move_cancelling': "Anulowanie przesuwania",
        'opening_pdf': "Otwieranie PDF...",
        'loading_document': "Ładowanie dokumentu...",
        'pdf_opened': "PDF otwarty",
        'pages_found_moving': "Znaleziono {0} stron, {1} do przesunięcia",
        'creating_backup': "Tworzenie kopii zapasowej...",
        'backup_description': "Zabezpieczanie oryginalnego pliku...",
        'backup_saved_as': "Zapisano jako: {0}",
        'error_format': "Błąd: {0}",

        # ============================================
        # 50. UNIVERSALDIALOG
        # ============================================
        'app_title_format': "PDFDarkView by BinhDiez - {0}",

        # ============================================
        # 51. TEXTVIEWER
        # ============================================
        'search_cleared': "Wyszukiwanie zresetowane",
        'page_header_simple': "=== Strona {0} ===",

        # ============================================
        # 52. PASSWORT-ANLEITUNG (HTML)
        # ============================================
        'password_guide_title': "Zarządzanie hasłami – instrukcja",
        'password_guide_voice': "Instrukcja zarządzania hasłami. Przeczytaj uwagi.",
        'password_guide_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px;">
        <p><strong>🔐 Zarządzanie hasłami – szczegółowa instrukcja</strong></p>

        <p><strong>1. Ochrona hasłem PDF</strong></p>
        <ul>
        <li>Podczas otwierania PDF zabezpieczonego hasłem pojawi się okno dialogowe, w którym możesz wprowadzić hasło.</li>
        <li>Możesz zapisać hasło w zaszyfrowanej formie, aby nie musieć go ponownie wprowadzać (pole wyboru „Zapisz hasło”).</li>
        <li>Za pomocą przycisku „Usuń hasło” możesz utworzyć odszyfrowaną kopię PDF i usunąć hasło z bazy danych.</li>
        </ul>

        <p><strong>2. Hasło główne</strong></p>
        <ul>
        <li>Hasło główne chroni dostęp do wszystkich zapisanych haseł PDF.</li>
        <li><strong>Ustawianie:</strong> Przejdź do „Ustawienia → Zarządzanie hasłami → Ustawienia hasła głównego” i kliknij „Ustaw hasło główne”. Wybierz silne hasło (minimum 8 znaków).</li>
        <li><strong>Zmiana:</strong> Po pomyślnym uwierzytelnieniu możesz zmienić hasło główne.</li>
        <li><strong>Usuwanie:</strong> Jeśli usuniesz hasło główne, WSZYSTKIE zapisane hasła zostaną bezpowrotnie usunięte. Możesz wcześniej wyeksportować kopię zapasową.</li>
        <li>Raz na sesję musisz uwierzytelnić się hasłem głównym, aby uzyskać dostęp do chronionych funkcji (np. wyświetlanie haseł).</li>
        </ul>

        <p><strong>3. Zarządzanie hasłami (lista)</strong></p>
        <ul>
        <li>W „Ustawienia → Zarządzanie hasłami” otwiera się tabela wszystkich zapisanych PDF-ów z ich zaszyfrowanymi hasłami.</li>
        <li><strong>Bez hasła głównego:</strong> Możesz tylko usuwać wpisy – hasła pozostają ukryte.</li>
        <li><strong>Z hasłem głównym (uwierzytelniony):</strong> Możesz wyświetlać, kopiować, eksportować i usuwać hasła.</li>
        <li><strong>Eksport:</strong> Wybierz format (JSON, CSV, TXT) i zapisz listę. Jeśli hasło główne jest ustawione, możesz zdecydować, czy hasła mają być eksportowane w postaci jawnej czy nadal zaszyfrowane.</li>
        <li><strong>Import:</strong> Wcześniej wyeksportowany plik ZIP ze wszystkimi ustawieniami (w tym hasłami) można zaimportować przez „Ustawienia → Eksportuj/importuj ustawienia”. Uwaga: Istniejące dane zostaną nadpisane!</li>
        </ul>

        <p><strong>4. Generator haseł</strong></p>
        <ul>
        <li>W oknie dialogowym hasła (np. podczas zabezpieczania PDF) po prawej stronie pola wprowadzania znajduje się przycisk z kostką 🎲.</li>
        <li>Kliknij go, aby otworzyć generator haseł. Możesz ustawić długość, zestawy znaków (wielkie litery, małe litery, cyfry, znaki specjalne) oraz separatory dla lepszej czytelności.</li>
        <li>Wygenerowane hasło można bezpośrednio przejąć i w razie potrzeby skopiować.</li>
        </ul>

        <p><strong>5. Ważne wskazówki dotyczące bezpieczeństwa</strong></p>
        <ul>
        <li>Zapisane hasła są przechowywane w zaszyfrowanej formie przy użyciu AES-256. Klucz jest wyprowadzany z hasła głównego (jeśli ustawione) lub ze stałej wartości (bez hasła głównego).</li>
        <li>Bez hasła głównego hasła są wprawdzie zaszyfrowane, ale klucz jest zapisany w programie – osoba atakująca z dostępem do Twoich plików mogłaby je odszyfrować. Dlatego zdecydowanie zalecamy używanie hasła głównego.</li>
        <li>Baza danych haseł znajduje się w katalogu `Daten/passwords.json`. Regularnie twórz kopie zapasowe, zwłaszcza przed usunięciem hasła głównego.</li>
        <li>W przypadku utraty hasła głównego wszystkie zapisane hasła są bezpowrotnie utracone.</li>
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
        'invert_mode_label': "Tryb inwersji",
        'invert_mode_classic': "Klasyczny (odwracaj wszystkie kolory)",
        'invert_mode_smart': "Inteligentny (odwracaj tylko jasność)",
        # ======== COMBOBOX =============
        'gray_threshold_label': "Próg skali szarości",
        'gray_threshold_10': "10% (ostry)",
        'gray_threshold_20': "20%",
        'gray_threshold_30': "30% (domyślny)",
        'gray_threshold_40': "40%",
        'gray_threshold_50': "50% (łagodny)",
        'threshold_changed': "Ustawiono próg na {0}%",
        # ======== ANLEITUNG =============
        'threshold_guide_title': "Próg skali szarości – wyjaśnienie",
        'threshold_guide_text': "Próg skali szarości określa, które piksele w inteligentnym trybie ciemnym są uznawane za 'szare' i odwracane.\n\n"
                                "• Niska wartość (10%) odwraca tylko niemal idealne odcienie szarości – kolorowe elementy pozostają w pełni zachowane.\n"
                                "• Wysoka wartość (50%) odwraca również lekko kolorowe piksele – zwiększa to kontrast, ale może zniekształcać kolory.\n\n"
                                "Optymalna wartość zależy od dokumentu. W przypadku czystych dokumentów tekstowych 30–40% jest często idealne, dla kolorowych grafik raczej 10–20%.\n\n"
                                "Możesz zmienić wartość w dowolnym momencie przez menu 'Ustawienia' – PDF zostanie wtedy natychmiast przeładowany.\n\n"
                                "Uwaga:\n* Zdjęcia i obrazy mogą być poprawnie wyświetlane tylko w trybie jasnym!\n* Ustawienia inwersji są wyświetlane tylko przy włączonym trybie ciemnym.",
        'threshold_guide_voice': "Próg skali szarości określa, jak silnie interweniuje inteligentny tryb ciemny. Niska wartość chroni kolory, wysoka zwiększa kontrast.",

        # ============================================
        # 54. Fortschrittsmeldungen (Worker, OCR, etc.)
        # ============================================
        'progress_opening_pdf': "Otwieranie PDF...",
        'progress_loading_document': "Ładowanie dokumentu...",
        'progress_pdf_opened': "PDF otwarty",
        'progress_creating_backup': "Tworzenie kopii zapasowej...",
        'progress_backup_description': "Zabezpieczanie oryginalnego pliku...",
        'progress_backup_created': "Utworzono kopię zapasową",
        'progress_backup_saved_as': "Zapisano jako: {0}",
        'progress_analyzing_start': "Rozpoczęcie analizy...",
        'progress_searching_empty': "Szukanie pustych stron...",
        'progress_page_empty': "Strona {0} jest pusta",
        'progress_page_keep': "Zachowanie strony {0}",
        'progress_analysis_complete': "Analiza zakończona",
        'progress_empty_found': "Znaleziono {0} pustych stron",
        'progress_current_page': "Bieżąca strona",
        'progress_mark_delete': "Oznaczanie do usunięcia",
        'progress_range_selected': "Zaznaczono zakres {0}-{1}",
        'progress_deleting_pages': "Usuwanie {0} stron",
        'progress_creating_new_pdf': "Tworzenie nowego PDF...",
        'progress_transferring_pages': "Przenoszenie stron",
        'progress_keeping_page': "Strona {0} zostaje zachowana ({1}/{2})",
        'progress_saving_pdf': "Zapisywanie PDF...",
        'progress_optimizing': "Optymalizacja rozmiaru...",
        'progress_finalizing': "Finalizacja...",
        'progress_new_size': "Nowy rozmiar: {0:.2f} MB",
        'progress_cancelling': "Anulowanie...",
        'progress_cancel_message': "Anulowanie {0}",
        'progress_pages_found_moving': "Znaleziono {0} stron, {1} do przesunięcia",

        # OCR-Fortschritt
        'ocr_status_analyzing': "Analizowanie PDF...",
        'ocr_status_optimizing': "Optymalizacja obrazu...",
        'ocr_status_recognizing': "Rozpoznawanie tekstu...",
        'ocr_status_embedding': "Osadzanie tekstu...",
        'ocr_status_finalizing': "Finalizacja PDF...",

        # PDF-Laden
        'progress_preparing': "Przygotowywanie...",
        'progress_loading': "Ładowanie PDF...",

        # Seitenoperationen
        'progress_deleting_title': "Usuwanie stron...",
        'progress_moving_title': "Przesuwanie stron...",
        'pages_found': "Znaleziono stron",
        'progress_creating_new_order': "Tworzenie nowej kolejności...",
        'progress_sorting_pages': "Sortowanie stron...",
        'progress_moving_to_begin': "Przesuwanie {0} stron na początek",
        'progress_transferring_count': "Przenoszenie {0} stron",
        'progress_transferring_before_target': "Przenoszenie stron przed celem",
        'progress_moving_pages': "Przesuwanie {0} stron",

        # ============================================
        # 55. Dateinamen
        # ============================================
        'filename_backup_suffix': "_backup_",
        'filename_protected_suffix': "_zabezpieczony_",
        'filename_copy_suffix': "_kopia",
        'filename_page_single': "_strona_",
        'filename_page_range': "_strony_",
        'filename_export_page': "_strona_{0:03}",
        'filename_export_range': "_strony_{0}-{1}",
        'filename_export_multiple': "_strony_{0}",
        'filename_with_text': "_z_tekstem",
        'filename_with_signature': "_z_podpisem",
        'filename_with_image': "_z_obrazem",
        'filename_with_forms': "_z_kształtami",
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
        'view_toggle_navbar': "Pokaż pasek przycisków",

        # ============================================
        # 57. SEITEN LÖSCHEN
        # ============================================
        'pages_cannot_delete_all': "Nie można usunąć wszystkich stron",
        'pages_cannot_delete_last_page': 'Nie można usunąć ostatniej strony!',
        'pages_cannot_delete_all_pages': 'W dokumencie musi pozostać co najmniej jedna strona!',
        'delete_pages_confirm': 'Czy na pewno chcesz usunąć {0} stron?',
        'delete_pages_confirm_voice': 'Czy na pewno chcesz usunąć {0} stron?',
        'pages_deleted': 'Pomyślnie usunięto {0} stron.',
        'warning': 'Ostrzeżenie',
        'error': 'Błąd',

        # ============================================
        # 58. FORM ANPASSEN
        # ============================================
        'no_form_selected': "Nie wybrano kształtu",
        'form_customized': "Dostosowano kształt",

        # ============================================
        # 59. ERWEITERTE PASSWORTVERWALTUNG
        # ============================================
        'btn_select': "Wybierz",
        'btn_use': "Użyj",
        'master_password_for_spasswords': "Aby przechowywać i używać haseł, należy najpierw ustawić hasło główne.\n\nCzy chcesz teraz ustawić hasło główne?",
        'open_saved_dialog_title': "Otwórz zapisany plik",
        'open_saved_question': "Czy chcesz teraz otworzyć zapisany plik?",
        'password': "Hasło",
        'password_manager_master_required': "Menedżer haseł jest dostępny tylko po ustawieniu hasła głównego.\n\nCzy chcesz teraz ustawić hasło główne?",
        'password_master_required_for_select': "Aby wyświetlić i wybrać zapisane hasła, musisz najpierw uwierzytelnić się hasłem głównym.\n\nCzy chcesz się teraz uwierzytelnić?",
        'password_not_available': "Wybrane hasło jest niedostępne lub nie można go odszyfrować.",
        'password_options_title': "Opcje hasła",
        'password_save_choice_change': "Ustaw nowe hasło",
        'password_save_choice_keep': "Użyj istniejącego hasła",
        'password_save_choice_none': "Zapisz bez szyfrowania",
        'password_save_hint': "Najpierw ustaw hasło główne, aby bezpiecznie przechowywać hasła.",
        'password_save_master_required': "Zapisz hasło (tylko z hasłem głównym)",
        'password_save_question': "Bieżący PDF jest chroniony hasłem. Czy chcesz użyć istniejącego hasła, ustawić nowe, czy zapisać bez szyfrowania?",
        'password_select': "Wybierz hasło",
        'password_select_none': "Nie wybrano hasła.\n\nWybierz hasło z listy.",
        'password_select_one': "Wybierz dokładnie jedno hasło.\n\nZaznaczyłeś wiele haseł.",

        # ============================================
        # 60. ZENTRALE DATEINAMEN-GENERIERUNG (zusätzliche Suffixe)
        # ============================================
        'filename_backup_suffix': "_backup",  # Hinweis: Dieser Eintrag existiert bereits in 55, wird hier aber für andere Kontexte genutzt. Ist kein Duplikat im Sinne des Dictionary-Keys, da der Schlüssel gleich ist. Aber Achtung: Der Wert wird überschrieben. Ich belasse es zur Sicherheit so, wie es war. In der Praxis sollte man den Schlüssel nicht doppelt verwenden.
        'filename_insert_suffix': "_z_wstawieniem",
        'filename_ocr_suffix': "_ocr",
        'filename_pages_deleted': "_usuniete_strony",
        'filename_pages_moved': "_przesuniete_strony",
        'filename_rotated_all_suffix': "_wszystkie_strony_obrocone",
        'filename_rotated_suffix': "_strona_obrocona",

        # ============================================
        # 61. DATEINAMEN-EINSTELLUNGEN (Dialog)
        # ============================================
        'filename_settings_dialog_title': "Konfiguracja nazw plików przy zmianach w PDF",
        'filename_keep_suffixes': "Zachowaj poprzednie rozszerzenia (np. _z_tekstem)",
        'filename_keep_suffixes_false': "Zastąp",
        'filename_keep_suffixes_true': "Zachowaj",
        'filename_preview_label': "Podgląd nazwy pliku:",
        'filename_preview_overwrite_hint': "Podgląd niedostępny – oryginał zostanie nadpisany.",
        'filename_separator': "Separator między słowami",
        'filename_separator_none': "Brak separatora",
        'filename_separator_space': "Spacja ( )",
        'filename_separator_underscore': "Podkreślnik (_)",
        'filename_settings_saved': "Zapisano ustawienia nazw plików",
        'filename_settings_title': "Formatowanie nazw plików i kopia zapasowa",
        'filename_timestamp_position': "Pozycja znacznika czasu",
        'filename_timestamp_position_after': "Po nazwie podstawowej",
        'filename_timestamp_position_before': "Na początku",
        'filename_timestamp_position_end': "Na końcu",
        'filename_use_timestamp': "Używaj znacznika czasu",

        # ============================================
        # 62. VERHALTEN BEI ÄNDERUNGEN (Dialog)
        # ============================================
        'behavior_section': "<html><b>Zachowanie przy zmianach:</b><ul><li>Usuwanie i wstawianie stron</li><li>Wstawianie tekstu, podpisu, obrazu i kształtów</li><li>OCR</li></ul></html>",
        'backup_section': "Kopia zapasowa dla operacji na stronach (usuwanie, przesuwanie)",
        'behavior_info': "Uwaga: Przy 'Nadpisz oryginał' znaczniki czasu i sufiksy są ignorowane – plik zachowuje swoją nazwę.",
        'behavior_new_file': "Zawsze twórz nowy plik (z znacznikiem czasu i sufiksem)",
        'behavior_overwrite': "Nadpisz oryginał (bez nowego pliku)",

        # ============================================
        # 63. ERFOLGSMELDUNGEN (neue Datei / Überschreiben)
        # ============================================
        'all_pages_rotated_new_file': "Obrócono wszystkie strony.\n\nOryginał pozostał bez zmian.\nNowy plik: {0}",
        'all_pages_rotated_voice': "Obrócono wszystkie strony, utworzono nowy plik.",
        'empty_pages_deleted_new_file': "Usunięto {0} pustych stron.\n\nOryginał pozostał bez zmian.\nNowy plik: {1}",
        'empty_pages_deleted_voice': "Usunięto {0} pustych stron, utworzono nowy plik.",
        'ocr_keep_original': "Zachowaj oryginał (otwórz później ręcznie)",
        'ocr_new_file_question': "Nowy przeszukiwalny PDF został zapisany jako:\n{0}\n\nCzy chcesz go teraz otworzyć?",
        'ocr_open_new': "Otwórz nowy plik OCR",
        'ocr_original_kept': "Oryginalny plik pozostaje otwarty. Plik OCR został zapisany.",
        'page_deleted_new_file': "Usunięto stronę {0}.\n\nOryginał pozostał bez zmian.\nNowy plik: {1}",
        'page_deleted_voice': "Usunięto stronę {0}, utworzono nowy plik.",
        'page_rotated_new_file': "Obrócono stronę {0}.\n\nOryginał pozostał bez zmian.\nNowy plik: {1}",
        'page_rotated_voice': "Obrócono stronę {0}, utworzono nowy plik.",
        'pages_deleted_new_file': "Usunięto {0} stron.\n\nOryginalny plik pozostał bez zmian.\nNowy plik: {1}",
        'pages_deleted_new_file_voice': "Usunięto {0} stron, utworzono nowy plik.",
        'pages_inserted_new_file': "Wstawiono {0} stron.\n\nOryginalny plik pozostał bez zmian.\nNowy plik: {1}",
        'pages_inserted_new_file_ask': "Wstawiono {0} stron.\n\nOryginał pozostał bez zmian.\nNowy plik: {1}\n\nCzy chcesz go teraz otworzyć?",
        'pages_inserted_voice_new': "Wstawiono {0} stron, utworzono nowy plik.",
        'pages_moved_new_file': "Przesunięto {0} stron.\n\nOryginalny plik pozostał bez zmian.\nNowy plik: {1}",
        'pages_moved_new_file_voice': "Przesunięto {0} stron, utworzono nowy plik.",

        # ============================================
        # 64. BACKUP-INFO-DIALOG
        # ============================================
        'backup_do_not_show': "Nie pokazuj więcej",
        'backup_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700; margin-bottom: 15px;">📌 Ustawienie kopii zapasowej</p>
            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">✅ Kopia zapasowa WŁĄCZONA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Przy wszystkich zmianach nadpisujących oryginał</strong> (tekst, podpis, obraz, kształt, OCR, obracanie, wstawianie, usuwanie/przesuwanie stron) tworzona jest <strong>automatycznie kopia zapasowa z znacznikiem czasu</strong>, zanim zmiana zostanie zastosowana.</p>
                <p style="margin: 5px 0 5px 20px;">• Kopia znajduje się obok oryginalnego pliku (np. <code>Dokument_backup_20260412_120000.pdf</code>).</p>
                <p style="margin: 5px 0 5px 20px;">• Jeśli dodatkowo włączysz opcję <strong>„Nadpisz oryginał”</strong>, również zostanie utworzona kopia zapasowa.</p>
            </div>
            <div style="background-color: #C62828; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🔄 Kopia zapasowa WYŁĄCZONA</p>
                <p style="margin: 5px 0 5px 20px;">• <strong>Nie tworzy się kopii</strong> – ani przy nadpisywaniu, ani przy operacjach na stronach.</p>
                <p style="margin: 5px 0 5px 20px;">• Oryginalny plik może zostać bezpowrotnie utracony podczas nadpisywania.</p>
                <p style="margin: 5px 0 5px 20px;">• <strong style="color: #FFD700;">Zalecane tylko dla zaawansowanych użytkowników!</strong></p>
            </div>
            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Wskazówka:</strong> Ustawienie kopii zapasowej jest niezależne od opcji „Nadpisz oryginał”. Możesz łączyć obie opcje.<br>
                Możesz trwale ukryć ten komunikat.
            </div>
        </div>
        """,
        'backup_info_title': "Zachowanie kopii zapasowej",
        'backup_info_voice': "Uwaga dotycząca zachowania kopii zapasowej przy operacjach na stronach. Kopia włączona nadpisuje oryginał, kopia wyłączona tworzy nowy plik.",
        'show_backup_info': "Informacje o ustawieniu kopii zapasowej",

        # ============================================
        # 65. ÜBERSCHREIBEN-INFO-DIALOG
        # ============================================
        'overwrite_do_not_show': "Nie pokazuj więcej",
        'overwrite_enable_backup': "Włącz kopię zapasową (zalecane)",
        'overwrite_info_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">⚠️ Nadpisz oryginał</p>
            <p>Włączenie tej opcji powoduje, że zmiany (tekst, podpis, obraz, kształt, OCR, obracanie, wstawianie) są <strong>zapisywane bezpośrednio w oryginale</strong> – <strong>nie powstaje nowy plik</strong>.</p>
            <p>• Nazwa pliku pozostaje bez zmian.<br>
            • Znaczniki czasu i sufiksy są ignorowane.<br>
            • <strong>Bez kopii zapasowej oryginał może zostać bezpowrotnie utracony.</strong></p>
            <p style="color: #FFD700;">Zalecenie: Włącz dodatkowo opcję kopii zapasowej, aby uzyskać automatyczne zabezpieczenia.</p>
        </div>
        """,
        'overwrite_info_title': "Nadpisz oryginał",
        'overwrite_info_voice': "Uwaga: Nadpisz oryginał – bez nowego pliku. Zalecana kopia zapasowa.",

        # ======================================================
        # 66. ERFOLGSMELDUNGEN (bei verschiedenen Einstellungen)
        # ======================================================
        'pages_inserted_overwrite_with_backup': "Wstawiono {0} stron.\n\nOryginalny plik został nadpisany.\nUtworzono kopię zapasową.",
        'pages_inserted_overwrite_no_backup': "Wstawiono {0} stron.\n\nOryginalny plik został nadpisany.\nNIE utworzono kopii zapasowej.",
        'texts_saved_overwrite_with_backup': "Zmiany zostały zapisane w oryginale.\n\nUtworzono kopię zapasową.",
        'texts_saved_overwrite_no_backup': "Zmiany zostały zapisane w oryginale.\n\nNIE utworzono kopii zapasowej.",
        'texts_crosses_saved_new_file': "Zapisano {0} {1} i {2} {3}.\n\nOryginalny plik pozostał bez zmian.\nUtworzono nowy plik.\n\nNowy PDF jest ładowany...",
        'texts_saved_new_file': "Zapisano {0} {1}.\n\nOryginalny plik pozostał bez zmian.\nUtworzono nowy plik.\n\nNowy PDF jest ładowany...",
        'crosses_saved_new_file': "Zapisano {0} {1}.\n\nOryginalny plik pozostał bez zmian.\nUtworzono nowy plik.\n\nNowy PDF jest ładowany...",
        'elements_saved_new_file': "Zapisano {0} elementów.\n\nOryginalny plik pozostał bez zmian.\nUtworzono nowy plik.\n\nNowy PDF jest ładowany...",
        'signatures_saved_overwrite_with_backup': "Podpis(y) został(y) zapisany(e) w oryginale.\n\nUtworzono kopię zapasową.",
        'signatures_saved_overwrite_no_backup': "Podpis(y) został(y) zapisany(e) w oryginale.\n\nNIE utworzono kopii zapasowej.",
        'images_saved_overwrite_with_backup': "Obraz(y) został(y) zapisany(e) w oryginale.\n\nUtworzono kopię zapasową.",
        'images_saved_overwrite_no_backup': "Obraz(y) został(y) zapisany(e) w oryginale.\n\nNIE utworzono kopii zapasowej.",
        'forms_saved_overwrite_with_backup': "Kształt(y) został(y) zapisany(e) w oryginale.\n\nUtworzono kopię zapasową.",
        'forms_saved_overwrite_no_backup': "Kształt(y) został(y) zapisany(e) w oryginale.\n\nNIE utworzono kopii zapasowej.",
        'signatures_saved_new_file': "Zapisano {0} podpisów.\n\nOryginalny plik pozostał bez zmian.\nUtworzono nowy plik.\n\nNowy PDF jest ładowany...",
        'images_saved_new_file': "Zapisano {0} obrazów.\n\nOryginalny plik pozostał bez zmian.\nUtworzono nowy plik.\n\nNowy PDF jest ładowany...",
        'forms_saved_new_file': "Zapisano {0} kształtów.\n\nOryginalny plik pozostał bez zmian.\nUtworzono nowy plik.\n\nNowy PDF jest ładowany...",

        # ======================================================
        # 67. GEDREHTE SEITEN ROTATION
        # ======================================================
        'rotation_warning': "Uwaga: Ten PDF zawiera obrócone strony. Pozycjonowanie może być nieprawidłowe.",
        'page_rotated_warning_title': "Wykryto obróconą stronę",
        'page_rotated_warning_message': "Bieżąca strona {0} jest obrócona o {1}°.\n\nWstawianie elementów na obróconych stronach nie jest obsługiwane.\n\nCzy chcesz teraz obrócić stronę do pozycji pionowej?",
        'page_rotated_warning_voice': "Uwaga: Strona jest obrócona. Najpierw ją obróć.",
        'paste_on_rotated_page_simple_warning': "Wklejanie na stronie {0} nie jest możliwe!\n\nTa strona jest obrócona o {1}°.\n\nNajpierw obróć stronę do 0° (menu: Edycja → Wyrównaj stronę).\n\nUwaga:\nSkopiowany wcześniej element zostanie utracony, jeśli nie zapiszesz go przed obróceniem strony.",
        'paste_on_rotated_page_voice': "Wklejanie anulowane. Strona jest obrócona. Najpierw wyrównaj stronę.",
        'page_rotated_cancel': "Anuluj",
        'page_rotated_rotate_until_upright': "Obróć stronę wielokrotnie (aż będzie pionowa)",
        'page_rotated_now_upright': "Strona jest teraz pionowa. Możesz teraz wkleić.",
        'page_rotated_still_not_upright': "Nie można obrócić strony do pozycji pionowej. Skoryguj ręcznie.",

        # ============================================
        # 68. HILFEDIALOG FÜR PROBLEMATISCHE SEITEN
        # ============================================
        'help_rotated_pages_title': "Pomoc: Korekcja obróconych stron",
        'help_rotated_pages_voice': "Otwieranie pomocy dotyczącej korekcji obróconych stron.",
        'btn_help': "Pomoc",
        'help_rotated_pages_html': """
        <div style="font-size: 14px; line-height: 1.5;">
            <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📌 Problem: Obrócona strona – wklejanie nie działa poprawnie</p>

            <p>Jeśli wklejanie tekstów, podpisów lub kształtów na obróconej stronie nie działa prawidłowo, możesz skorygować stronę za pomocą zewnętrznego edytora PDF.</p>

            <div style="background-color: #2E7D32; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">🛠️ Rozwiązanie z zewnętrznym narzędziem (np. Podgląd macOS)</p>
                <p style="margin: 5px 0 5px 20px;">1. <strong>Wyeksportuj stronę</strong><br>
                &nbsp;&nbsp;W menu wybierz <strong>Plik → Eksportuj jako Pages</strong> lub użyj innej metody, aby zapisać żądaną stronę jako osobny PDF.</p>

                <p style="margin: 5px 0 5px 20px;">2. <strong>Otwórz stronę w zewnętrznym programie</strong><br>
                &nbsp;&nbsp;Otwórz wyeksportowany PDF w edytorze PDF (np. <strong>Podgląd macOS</strong>, Adobe Acrobat, PDF Expert).</p>

                <p style="margin: 5px 0 5px 20px;">3. <strong>Obróć stronę</strong><br>
                &nbsp;&nbsp;Obróć stronę tak, aby była pionowa (w Podglądzie: <strong>Narzędzia → Obróć</strong> lub <strong>⌘ + R</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">4. <strong>Zapisz</strong><br>
                &nbsp;&nbsp;Zapisz poprawioną stronę (<strong>⌘ + S</strong>).</p>

                <p style="margin: 5px 0 5px 20px;">5. <strong>Wstaw stronę z powrotem do oryginalnego dokumentu</strong><br>
                &nbsp;&nbsp;Wróć do PDFDarkView i wstaw poprawioną stronę w żądane miejsce:<br>
                &nbsp;&nbsp;<strong>Edycja → Wstaw strony</strong>.</p>
            </div>

            <div style="background-color: #1565C0; padding: 10px; border-radius: 8px; margin: 10px 0;">
                <p style="font-size: 16px; font-weight: bold; color: #87CEEB; margin: 0 0 8px 0;">💡 Alternatywa: Obróć stronę w oryginale</p>
                <p style="margin: 5px 0 5px 20px;">• Użyj wbudowanej funkcji obracania (<strong>Edycja → Obróć stronę</strong>), aby stopniowo korygować stronę.<br>
                • Po każdym obróceniu możesz sprawdzić, czy wklejanie działa.<br>
                • To często szybsze rozwiązanie – wypróbuj je najpierw!</p>
            </div>

            <div style="margin-top: 15px; font-style: italic; color: #AAAAAA; border-top: 1px solid #555; padding-top: 10px;">
                💡 <strong>Wskazówka:</strong> Jeśli często napotykasz obrócone strony, możesz trwale wyłączyć ostrzeżenie w oknie wklejania.<br>
                Pozycjonowanie może wtedy jednak być nieprawidłowe – używaj tej opcji tylko wtedy, gdy znasz jej skutki.
            </div>
        </div>
        """,

        # ============================================
        # 69. SEITEN DREHEN UND ZURÜCKDREHEN auf Null
        # ============================================
        'menu_rotate_normalize': "Wyrównaj strony",
        'menu_rotate_normalize_tooltip': "Obróć stronę lub zresetuj do 0°",
        'normalize_current_page': "Ustaw bieżącą stronę w pozycji pionowej (ustaw na 0°)",
        'normalize_all_pages': "Ustaw wszystkie strony w pozycji pionowej (ustaw na 0°)",
        'page_normalized': "Strona {0} została ustawiona w pozycji pionowej.",
        'all_pages_normalized': "Wszystkie strony zostały ustawione w pozycji pionowej.",
        'page_already_upright': "Strona {0} jest już pionowa.",
        'all_pages_already_upright': "Wszystkie strony są już pionowe.",

        # ============================================
        # 70. EXPORT MELDUNGEN
        # ============================================
        'export_ocr_question_html': "<p>PDF nie zawiera przeszukiwalnego tekstu.</p><p>Czy chcesz przeprowadzić OCR, aby wyeksportować do {0}?</p>",
        'export_ocr_voice': "PDF nie zawiera tekstu. OCR wymagane do eksportu do {0}.",
        'export_no_ocr_possible': "Eksport bez OCR niemożliwy. Wykonaj OCR przez menu.",
        'ocr_failed_export_not_possible': "OCR nie powiódł się. Eksport niemożliwy.",

        # ============================================
        # 71. DRUCKEN (zusätzliche Meldungen)
        # ============================================
        'print_preview_start': "PDF otwiera się w podglądzie. Rozpocznij drukowanie ręcznie.",
        'print_preview_manual': "PDF otwarty. Wykonaj polecenie druku ręcznie (np. Ctrl+P).",

        # ============================================
        # 72. PDFs ZUSAMMENFÜHREN (MERGE)
        # ============================================
        'merge_pdfs_title': "Scal PDF-y",
        'merge_pdfs': "Scal PDF-y",
        'merge_progress_title': "Scalanie PDF-ów...",
        'merge_pdfs_list': "PDF-y w kolejności (przeciągnij, aby posortować)",
        'merge_add_pdf': "Dodaj PDF",
        'merge_remove': "Usuń",
        'merge_move_up': "W górę",
        'merge_move_down': "W dół",
        'merge_pdfs_info': "💡 Wskazówka: Możesz zmienić kolejność przez przeciąganie",
        'merge_no_pdfs': "Nie wybrano PDF-ów. Kliknij 'Dodaj PDF'.",
        'merge_info': "Wybrano {0} PDF-ów (ok. {1} stron)",
        'merge_open_file': "Otwórz plik",
        'merge_merge': "Scal",
        'merge_error': "Błąd scalania",
        'merge_min_two_pdfs_error': "Wybierz co najmniej dwa pliki PDF do scalenia.",
        'merge_select_pdfs': "Wybierz PDF-y do scalenia",
        'merge_error_file': "Błąd przetwarzania",
        'merge_cancelled': "Scalanie anulowane",
        'merge_preparing': "Przygotowywanie...",
        'merge_processing': "Przetwarzanie PDF {0} z {1}",
        'merge_saving': "Zapisywanie scalonego PDF...",
        'merge_complete': "Gotowe!",
        'merge_success_title': "Scalanie powiodło się",
        'merge_success_voice': "Pomyślnie scalono {0} PDF-ów.",
        'merge_success_message': "Pomyślnie scalono {0} PDF-ów.\n\nNowy dokument ma teraz {1} stron.\n\nNowy plik:\n{2}\n\nLokalizacja:\n{3}\n{2}\n\nCzy chcesz otworzyć ten PDF?",
        'replace_file_title': "Zastąpić plik?",
        'replace_file_message': "PDF jest już otwarty. Czy chcesz zastąpić go nowym plikiem?",
        'btn_yes': "Tak",
        'btn_no': "Nie",
        'filename_merge_suffix': "scalony",

        # ============================================
        # 73. FORTSCHRITTSMELDUNGEN FÜR MERGE
        # ============================================
        'progress_merge_opening': "Otwieranie {0}...",
        'progress_merge_reading': "Odczytywanie {0}...",
        'progress_merge_adding': "Dodawanie {0} stron...",
        'progress_merge_optimizing': "Optymalizacja PDF...",
        'progress_merge_writing': "Zapisywanie PDF...",

        # ============================================
        # 74. SPEICHERN VOR DEM SCHLIESSEN
        # ============================================
        'action_close_pdf': "zamknięciem PDF",
        'action_close_window': "zamknięciem okna",
        'action_open_new_pdf': "otwarciem nowego PDF",
        'action_quit_app': "zakończeniem aplikacji",
        'changes_saved': "Zmiany zostały zapisane.",
        'file_close_title': "Zamknij plik PDF",
        'save_before_action': "Czy zapisać zmiany przed {0}? Tak lub Nie?",
        'save_before_action_voice': "Czy zapisać zmiany przed {0}? Tak lub Nie?",
        'save_before_close_question': "Czy zapisać zmiany przed zamknięciem? Tak lub Nie?",

        # ============================================
        # Neue Einträge (noch nicht übersetzt)
        # ============================================

        # ============================================
        # 75. OCR PDF AUSRICHTEN
        # ============================================
        "guaranteed_message_short": "<b>Utworzono przeszukiwalny PDF:\n\n{0}\n\n<b>spróbuj ponownie, jeśli to konieczne",
        "ocr_rotate_title": "Wyrównaj strony przed OCR",
        "ocr_rotate_question": "PDF zawiera obrócone strony.\nCzy chcesz wyrównać wszystkie strony do 0° przed OCR?\nZnacznie poprawi to rozpoznawanie tekstu.",
        "ocr_rotate_yes": "Tak, wyrównaj",
        "ocr_rotate_no": "Nie, rozpocznij OCR bez wyrównania",
        "ocr_rotate_voice": "PDF zawiera obrócone strony. Czy wyrównać wszystkie strony przed OCR?",
        "ocr_not_performed_message": "Brak tekstu. Wykonaj OCR (menu \"Edycja\" → \"Wykonaj OCR\" lub klawisz Ctrl+R).",

        # ============================================
        # 76. OCR SETTINGS DIALOG
        # ============================================
        "ocr_settings_title": "Ustawienia OCR",
        "ocr_language_btn": "Wybierz język OCR",
        "ocr_language": "Język(i) OCR",
        "ocr_language_current": "Bieżący język:",
        "ocr_param_info": "Informacje o parametrze",

        # Parameter-Labels
        "ocr_force_ocr_label": "Wymuś OCR",
        "ocr_deskew_label": "Korekta przekoszenia",
        "ocr_clean_label": "Czyszczenie obrazu",
        "ocr_oversample_label": "Rozdzielczość (DPI)",
        "ocr_pagesegmode_label": "Podział strony",
        "ocr_oem_label": "Tryb silnika OCR",
        "ocr_optimize_label": "Kompresja PDF",
        "ocr_jobs_label": "Procesy równoległe",
        "ocr_verbose_label": "Poziom szczegółowości logów",
        # Tooltips für die Controls
        "ocr_force_ocr_tooltip": "Wymuś OCR na każdej stronie, nawet jeśli zawiera tekst",
        "ocr_deskew_tooltip": "Automatycznie koryguj przekoszenie skanów",
        "ocr_clean_tooltip": "Usuń szumy i artefakty z obrazu",
        "ocr_oversample_tooltip": "Przeskaluj obraz przed OCR do podanych DPI",
        "ocr_pagesegmode_tooltip": "Określa, jak strona jest dzielona na obszary tekstu",
        "ocr_oem_tooltip": "Wybiera silnik OCR Tesseract",
        "ocr_optimize_tooltip": "Poziom kompresji wyjściowego PDF",
        "ocr_jobs_tooltip": "Liczba równoległych procesów OCR",
        "ocr_verbose_tooltip": "Poziom szczegółowości logów",
        "ocr_settings_explain_btn": "Wyjaśnienie",

        # Parameter-Erklärungen (Tooltips + Info-Dialoge)
        "ocr_force_ocr_explain": "Wymusza rozpoznawanie tekstu na <b>każdej</b> stronie, nawet jeśli już zawiera tekst.\n\nZalecenie: <b>Włącz</b> dla zeskanowanych PDF-ów, <b>Wyłącz</b> dla rodzimych PDF-ów z już istniejącym tekstem.",

        "ocr_deskew_explain": "Koryguje lekko przekoszone skany (do ok. 5°).\n\nZalecenie: <b>Włącz</b> dla dokumentów skanowanych, <b>Wyłącz</b> jeśli strony są już idealnie proste.",

        "ocr_clean_explain": "Usuwa szumy, kropki i małe artefakty z obrazu.\n<b>WAŻNE:</b> W przypadku tekstów arabskich, tajskich lub wietnamskich z diakrytykami (kropkami nad/pod literami) ta opcja powinna być <b>wyłączona</b>, aby nie utracić ważnych znaków.",

        "ocr_oversample_explain": "Skaluje obraz <b>przed</b> rozpoznawaniem do podanych DPI.<br><br>• <b>72-150 DPI:</b> Bardzo szybko, ale niska skuteczność<br>• <b>200-300 DPI:</b> Optymalny zakres (domyślnie: 300)<br>• <b>400+ DPI:</b> Niewiele lepsze rozpoznawanie, ale znacznie większe pliki<br><br>Zalecenie: 300 DPI dla złożonych pism (arabski, chiński, japoński), 200 DPI dla języków zachodnich.",
        "ocr_pagesegmode_explain": "Określa, jak Tesseract dzieli stronę na obszary tekstu.\n\n• <b>3 - Automatycznie (domyślnie):</b> Dobre dla mieszanych układów\n• <b>4 - Pojedyncza kolumna:</b> Dla tekstów jednokolumnowych\n• <b>5 - Blok pionowy:</b> Dla pism pionowych (japoński, chiński)\n• <b>6 - Jednolity blok tekstowy:</b> Optymalne dla tekstu ciągłego bez kolumn\n• <b>11 - Surowy obraz:</b> Dla słabych skanów / odręcznych\n\nZalecenie: <b>6</b> dla prostych dokumentów tekstowych, <b>3</b> dla złożonych układów.",

        "ocr_oem_explain": "Wybiera silnik OCR Tesseract.\n\n• <b>0 - Legacy:</b> Stary silnik (szybki, ale mniej dokładny)\n• <b>1 - LSTM:</b> Silnik neuronowy (wolniejszy, ale dokładniejszy)\n• <b>2 - Legacy + LSTM:</b> Łączy wyniki obu\n• <b>3 - Standard (preferowany LSTM):</b> Najlepszy wybór w większości przypadków\n\nZalecenie: <b>3</b> dla maksymalnej dokładności.",

        "ocr_optimize_explain": "Kompresuje wyjściowy PDF.\n\n• <b>0:</b> Brak optymalizacji (najszybsze przetwarzanie)\n• <b>1:</b> Lekka optymalizacja (dobry kompromis)\n• <b>2:</b> Umiarkowana optymalizacja\n• <b>3:</b> Silna optymalizacja (najmniejszy plik, ale wolniejsze)\n\nZalecenie: <b>1</b> do codziennego użytku.",

        "ocr_jobs_explain": "Liczba równoległych procesów dla OCR.\n\n• <b>1:</b> Wolne, ale najmniejsze zużycie pamięci\n• <b>4-8:</b> Optymalne dla nowoczesnych procesorów wielordzeniowych\n• <b>12+:</b> Prawie żadne przyspieszenie przy wysokim zużyciu pamięci\n\nZalecenie: Liczba rdzeni CPU (np. <b>4</b> dla 4-rdzeniowego systemu).",

        "ocr_verbose_explain": "Poziom szczegółowości logów w konsoli.\n\n• <b>0:</b> Brak wyjścia\n• <b>1:</b> Postęp i komunikaty statusu\n• <b>2:</b> Szczegółowe wyjście\n• <b>3:</b> Pełne debugowanie (bardzo obszerne)\n\nZalecenie: <b>1</b> dla normalnej pracy.",

        "ocr_reset_title": "Ustawienia zresetowane",
        "ocr_reset_message": "Wszystkie ustawienia OCR zostały przywrócone do wartości domyślnych.",
        "info_tooltip": "Więcej informacji o tym parametrze",
        "ocr_reset_defaults": "Przywróć domyślne",
        # ==================== OCR PSM-Modi (Seitenaufteilung) ====================
        "ocr_psm_0": "Automatycznie (silnik Legacy)",
        "ocr_psm_1": "Automatyczne wykrywanie kolumn",
        "ocr_psm_3": "Automatycznie (domyślnie)",
        "ocr_psm_4": "Pojedyncza kolumna",
        "ocr_psm_5": "Blok pionowy",
        "ocr_psm_6": "Jednolity blok tekstowy",
        "ocr_psm_7": "Pojedynczy wiersz",
        "ocr_psm_8": "Pojedyncze słowo",
        "ocr_psm_11": "Surowy obraz (bez analizy układu)",
        # ==================== OCR OEM-Modi (Engine-Modus) ====================
        "ocr_oem_0": "Silnik Legacy (szybki)",
        "ocr_oem_1": "Silnik LSTM (neuronowy, dokładny)",
        "ocr_oem_2": "Legacy + LSTM łączone",
        "ocr_oem_3": "Standard (preferowany LSTM)",

        # ============================================
        # 77. OCR-Sprachauswahl (neu)
        # ============================================
        "ocr_language_menu": "Język(i) OCR...",
        "ocr_language_title": "Wybierz język(i) OCR",
        "ocr_language_instruction": "Wybierz język(i) do rozpoznawania tekstu (OCR).\nUwaga: Wiele języków wpływa na wydajność i dokładność!\nNajlepsze wyniki uzyskasz, wybierając tylko jeden język.",
        "ocr_language_predefined": "Predefiniowane kombinacje",
        "ocr_language_custom": "Niestandardowe...",
        "ocr_language_selected": "Wybrane języki OCR",
        "ocr_language_changed": "Zmieniono język OCR na {0}",
        "ocr_language_auto_detect": "Dostępne języki są wykrywane automatycznie.",
        "ocr_language_none_found": "Nie znaleziono danych językowych Tesseract! Zainstaluj pakiety językowe (np. 'tesseract-ocr-deu', 'tesseract-ocr-eng').",
        "ocr_language_select_custom": "Niestandardowy wybór języka",
        "ocr_language_available": "Dostępne języki (zainstalowane):",
        "ocr_language_select_hint": "Wybierz jeden lub więcej języków:",
        "ocr_language_confirm": "Zastosuj",
        "ocr_language_reset": "Przywróć domyślne (deu+eng+vie)",
        "ocr_language_priorities": "Zalecane języki (domyślnie zainstalowane):",
        # Für den MultiLanguageDialog
        "select_all_languages": "Zaznacz wszystkie",
        "clear_all_languages": "Odznacz wszystkie",
        "install_language_packs": "Zainstaluj brakujące pakiety językowe...",
        "install_hint": "💡 Wskazówka: Nie wszystkie języki są zainstalowane w Twoim systemie. Ten przycisk pomoże Ci w instalacji.",
        "ocr_language_install_title": "Instalacja pakietów językowych Tesseract",
        # OCR-Sprachfehler und Hilfetexte
        "ocr_missing_languages": "Brakujące pakiety językowe OCR",
        "ocr_missing_languages_message": "Następujące wybrane języki nie są zainstalowane w Twoim systemie:\n\n{0}\n\nZainstaluj brakujące pakiety językowe (patrz pomoc w 'Pomocy instalacji').\n\nCzy chcesz teraz otworzyć pomoc instalacji?",
        "ocr_missing_languages_voice": "Brakujące pakiety językowe. Zainstaluj brakujące języki.",
        "ocr_install_help_now": "Otwórz pomoc",
        "ocr_continue_anyway": "Spróbuj mimo to",
        "ocr_language_error_title": "Błąd języka OCR",
        "ocr_language_error_message": "Błąd podczas rozpoznawania tekstu: {0}\n\nSprawdź ustawienia języka OCR (Ustawienia → Język OCR).",
        "ocr_install_help_button": "Pomoc instalacji",

        # ==========================================
        # 78. OCR-Sprachen Installationshilfe (HTML)
        # ==========================================
        "ocr_install_help_html": """
        <html>
        <head/>
        <body style="font-family: system-ui, -apple-system, sans-serif; font-size: 14px; line-height: 1.5;">
        <p style="font-size: 18px; font-weight: bold; color: #FFD700;">📦 Instalacja pakietów językowych Tesseract</p>

        <p>Aby OCR działał w określonym języku, odpowiednie dane językowe muszą być zainstalowane w systemie. Postępuj zgodnie z instrukcją dla swojego systemu operacyjnego:</p>

        <hr>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🍎 macOS (Homebrew)</p>
        <ol>
        <li>Otwórz <strong>Terminal</strong> (Finder → Programy → Narzędzia → Terminal).</li>
        <li>Zainstaluj wszystkie dostępne języki za pomocą:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract-lang</code><br>
        (To może potrwać kilka minut.)</li>
        <li>Lub tylko pojedyncze języki (np. wietnamski):<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">brew install tesseract --with-vie</code><br>
        W przypadku nowszych wersji Homebrew może być konieczne ręczne pobranie pliku <code>*.traineddata</code> (patrz poniżej).</li>
        <li>Po instalacji: Zamknij ten okno i otwórz ponownie wybór języka OCR – nowe języki pojawią się automatycznie.</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🐧 Linux (Debian/Ubuntu)</p>
        <ol>
        <li>Otwórz terminal (Ctrl+Alt+T).</li>
        <li>Zainstaluj żądany język, np. dla wietnamskiego:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">sudo apt install tesseract-ocr-vie</code><br>
        Ważne kody języków: <code>deu</code> (niemiecki), <code>eng</code> (angielski), <code>vie</code> (wietnamski), <code>spa</code> (hiszpański), <code>fra</code> (francuski), <code>ita</code> (włoski), <code>nld</code> (holenderski), <code>fin</code> (fiński), <code>swe</code> (szwedzki), <code>nor</code> (norweski).</li>
        <li>Wyświetl wszystkie dostępne pakiety:<br>
        <code style="background: #2d2d3a; padding: 4px 8px; border-radius: 6px;">apt search tesseract-ocr-</code></li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">🪟 Windows (ręcznie)</p>
        <ol>
        <li>Pobierz żądane pliki <code>*.traineddata</code> z:<br>
        <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a><br>
        (np. <code>vie.traineddata</code> dla wietnamskiego).</li>
        <li>Skopiuj pliki do folderu językowego Tesseract, zazwyczaj:<br>
        <code>C:\\Program Files\\Tesseract-OCR\\tessdata</code><br>
        (W przypadku instalacji niestandardowej odpowiednio dostosuj.)</li>
        <li>Uruchom ponownie aplikację (lub otwórz ponownie wybór języka OCR).</li>
        </ol>

        <p style="font-size: 16px; font-weight: bold; color: #87CEEB;">💡 Alternatywa dla wszystkich systemów</p>
        <ul>
        <li>Zainstaluj <strong>OCRmyPDF</strong> i <strong>Tesseract</strong> za pomocą menedżera pakietów. Większość instalacji zawiera już kilka standardowych języków (angielski, niemiecki, francuski).</li>
        <li>Brakujące języki można zawsze doinstalować – lista języka OCR wyświetla tylko faktycznie dostępne.</li>
        </ul>

        <hr>
        <p><b>✅ Po instalacji:</b> Nie trzeba ponownie uruchamiać aplikacji – nowo dodane języki pojawią się od razu na liście.</p>
        <p><b>📖 Pomoc dotycząca kodów języków:</b> Pełną listę znajdziesz w <a style="color:#E0E0E0;" href="https://tesseract-ocr.github.io/tessdoc/Data-Files#data-files-for-version-400-november-29-2016">dokumentacji Tesseract</a>.</p>
        </body>
        </html>
        """,

        # ============================================
        # 79. NOTO SANS SCHRIFTARTEN INSTALLIEREN
        # ============================================
        "show_info_noto_font_title": "Czcionki Noto Sans",
        "info_noto_font_voice": "Instrukcja instalacji czcionek Noto Sans",
        "btn_info_noto_font_install": "Informacje o czcionkach",
        # Anleitung

        "info_noto_font_install": """
        <div style='background-color: #000000; color: #ffffff; font-family: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 100%; margin: 0 auto; padding: 1.5rem; border-radius: 1.5rem; line-height: 1.6; overflow-wrap: anywhere; word-break: break-word;'>

        <h2 style='font-size: 1.8rem; font-weight: 600; margin-top: 0; border-left: 5px solid #60a5fa; padding-left: 1rem;'>🖌️ Jak zainstalować darmowe czcionki Noto od Google</h2>

        <p><strong>Noto</strong> to rodzina czcionek open source od Google. Ich celem jest wyeliminowanie <em>"tofu"</em> (pustych prostokątów □) i poprawne wyświetlanie każdego znaku ze standardu Unicode. Są idealnym uzupełnieniem dla aplikacji wyświetlających teksty w wielu językach.</p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🍏 Instalacja na macOS</h3>

        <p><strong>Metoda 1: Za pomocą Homebrew (dla zaawansowanych)</strong></p>

        <pre style='background: #1e293b; color: #e2e8f0; padding: 0.8rem; border-radius: 0.75rem; font-family: monospace; white-space: pre-wrap; overflow-wrap: anywhere;'>brew install font-noto-sans</pre>

        <p><strong>Metoda 2: Przez „Dodaj czcionkę” (zalecana)</strong></p>

        <ol>
        <li>Pobierz oficjalny pakiet czcionek:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Rozpakuj plik ZIP</li>
        <li>Skopiuj pliki do <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>Macintosh HD > Użytkownicy > Nazwa użytkownika > Biblioteka > Czcionki</code></li>
        </ol>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🪟 Instalacja na Windows (10 i 11)</h3>

        <p><strong>Metoda 1: Microsoft Store (zalecana)</strong><br>
        Wyszukaj "Google Noto Fonts" lub "Noto Sans" i kliknij <strong>Zainstaluj</strong>.</p>

        <p><strong>Metoda 2: Instalacja ręczna</strong></p>

        <ol>
        <li>Pobierz:<br>
        <a href='https://fonts.google.com/noto/specimen/Noto+Sans' target='_blank' style='color: #4ade80;'>https://fonts.google.com/noto/specimen/Noto+Sans</a></li>
        <li>Rozpakuj ZIP</li>
        <li>Wybierz pliki .ttf / .otf</li>
        <li>Kliknij prawym przyciskiem → <strong>Zainstaluj</strong></li>
        </ol>

        <p>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Windows\\Fonts</code><br>
        lub<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>C:\\Users\\NazwaUżytkownika\\AppData\\Local\\Microsoft\\Windows\\Fonts</code>
        </p>

        <h3 style='font-size: 1.4rem; margin-top: 1.8rem;'>🐧 Instalacja na Linux</h3>

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

        <p>Weryfikacja:<br>
        <code style='background: #1e293b; padding: 0.2rem 0.4rem; border-radius: 0.375rem;'>fc-list | grep "Noto"</code>
        </p>

        </div>
        """,

        # ==================================================
        # 80. LESEZEICHEN (BOOKMARKS)
        # ==================================================
        "bookmark_dialog_title": "Zarządzanie zakładkami",
        "bookmark_add": "Dodaj zakładkę",
        "bookmark_add_tooltip": "Zapisz bieżącą stronę jako zakładkę",
        "bookmark_remove": "Usuń zakładkę",
        "bookmark_remove_tooltip": "Usuń zaznaczoną zakładkę",
        "bookmark_remove_all": "Usuń wszystkie",
        "bookmark_remove_all_tooltip": "Usuń wszystkie zakładki tego PDF",
        "bookmark_jump": "Przejdź do zakładki",
        "bookmark_jump_tooltip": "Przejdź do wybranej strony",
        "bookmark_name": "Nazwa",
        "bookmark_page": "Strona",
        "bookmark_no_bookmarks": "Brak zakładek.\nKliknij 'Dodaj', aby zapisać bieżącą stronę jako zakładkę.",
        "bookmark_added": "Dodano zakładkę dla strony {0}: {1}",
        "bookmark_removed": "Usunięto zakładkę: {0}",
        "bookmark_all_removed": "Usunięto wszystkie zakładki.",
        "bookmark_name_default": "Strona {0}",
        "bookmark_name_prompt": "Nazwa zakładki:\n(dłuższy tekst zostanie skrócony do 50 znaków)",
        "bookmark_name_prompt_title": "Nazwa zakładki",
        "bookmark_confirm_remove_all": "Czy na pewno chcesz usunąć wszystkie {0} zakładek?",
        "menu_bookmarks": "Zakładki",
        "bookmark_manage": "Zarządzaj zakładkami",
        "bookmark_next": "Następna zakładka",
        "bookmark_prev": "Poprzednia zakładka",
        "bookmark_page_display": "Strona {0}",
        "bookmark_exists": "Zakładka dla tej strony o tej nazwie już istnieje.",
        "bookmark_select_first": "Najpierw wybierz zakładkę.",
        "bookmark_confirm_remove": "Czy na pewno chcesz usunąć zakładkę 'Strona {0}: {1}'?",
        "bookmark_jumped_to": "Przejście do zakładki '{0}' na stronie {1}.",
        "bookmark_jumped_to_voice": "Zakładka {0}, strona {1}",
        "btn_close": "Zamknij",
        # LESEZEICHEN KONTEXTMENÜ im Dialog
        "bookmark_list": "Twoje zakładki",
        "bookmark_rename": "Zmień nazwę zakładki",
        "bookmark_rename_tooltip": "Zmień nazwę wybranej zakładki",
        "bookmark_rename_title": "Zmień nazwę zakładki",
        "bookmark_rename_prompt": "Nowa nazwa zakładki na stronie {0}:\n(max. 50 znaków)",
        "bookmark_renamed": "Zakładka '{0}' została zmieniona na '{1}'.",
        "bookmark_item_tooltip": "Strona {0}: {1}\nDwuklik, aby przejść",
        "bookmark_name_exists_question": "Zakładka o nazwie '{0}' już istnieje na tej stronie.\nMimo to zmienić nazwę?",
        # LESEZEICHEN KONTEXTMENÜ im Hauptfenster
        "context_bookmarks": "Zakładki",
        "context_bookmark_add_here": "Dodaj zakładkę dla tej strony",
        "context_bookmarks_existing": "Istniejące zakładki:",
        "context_bookmarks_jump": "Przejdź do zakładki:",
        "context_bookmarks_none": "Brak zakładek",
        "context_bookmarks_clear_all": "Usuń wszystkie {0} zakładek",
        # LESEZEICHEN SUCHLEISTE
        "bookmark_search_placeholder": "Szukaj zakładek... (nazwa lub strona)",
        "bookmark_search_results": "Znaleziono %d zakładek dla \"%s\"",
        "bookmark_no_search_results": "Nie znaleziono zakładek dla \"%s\"",
        "bookmark_no_search_results_label": "Brak wyników dla \"%s\"",

        # ==================================================
        # 81. PDF METADATEN BEARBEITEN (DIALOG)
        # ==================================================
        "metadata_dialog_title": "Edycja metadanych PDF",
        "metadata_title": "Tytuł",
        "metadata_title_placeholder": "Tytuł dokumentu",
        "metadata_title_tooltip": "Tytuł dokumentu (wyświetlany w pasku tytułu)",
        "metadata_author": "Autor",
        "metadata_author_placeholder": "Nazwisko autora",
        "metadata_author_tooltip": "Twórca dokumentu",
        "metadata_subject": "Temat",
        "metadata_subject_placeholder": "Temat dokumentu",
        "metadata_subject_tooltip": "Krótki opis zawartości",
        "metadata_keywords": "Słowa kluczowe",
        "metadata_keywords_placeholder": "Słowa kluczowe oddzielone przecinkami",
        "metadata_keywords_tooltip": "Hasła do kategoryzacji dokumentu",
        "metadata_creator": "Twórca",
        "metadata_creator_placeholder": "Aplikacja, która utworzyła PDF",
        "metadata_creator_tooltip": "Oprogramowanie, za pomocą którego utworzono dokument",
        "metadata_producer": "Producent",
        "metadata_producer_placeholder": "Aplikacja, która przekonwertowała PDF",
        "metadata_producer_tooltip": "Oprogramowanie, które przekonwertowało PDF",
        "metadata_creation_date": "Data utworzenia",
        "metadata_creation_date_tooltip": "Data utworzenia dokumentu",
        "metadata_mod_date": "Data modyfikacji",
        "metadata_mod_date_tooltip": "Data ostatniej modyfikacji",
        "metadata_pdf_info": "📄 Informacje o PDF",
        "metadata_pages": "Liczba stron",
        "metadata_file_size": "Rozmiar pliku",
        "metadata_pdf_version": "Wersja PDF",
        "metadata_encrypted": "Zaszyfrowany",
        "metadata_encrypted_yes": "Tak (chroniony hasłem)",
        "metadata_encrypted_no": "Nie",
        "metadata_reload": "📂 Załaduj z PDF",
        "metadata_reset": "Odrzuć zmiany",
        "metadata_reloaded": "Metadane zostały załadowane z PDF.",
        "metadata_reset_done": "Wszystkie pola metadanych zostały zresetowane.",
        "metadata_no_file": "Nie załadowano pliku PDF.",
        "metadata_save_error": "Błąd podczas zapisywania metadanych",
        "metadata_saved": "Metadane zostały pomyślnie zapisane.",
        "metadata_pdf_version_unknown": "PDF (nieznany)",
        "metadata_saved_message": "Metadane zostały pomyślnie zapisane.",
        "metadata_saved_voice": "Zapisano metadane.",

        "metadata_custom": "🔧 Niestandardowe metadane",
        "metadata_custom_placeholder": "{\n  \"moje_pole\": \"moja wartość\",\n  \"inne_pole\": 123\n}",
        "metadata_custom_tooltip": "Format JSON dla niestandardowych metadanych (opcjonalne)",

        # ============================================
        # 82. TEXT TEMPLATE KONTEXTMENÜ
        # ============================================
        "template_selected_hint": "Wybrano szablon \"{0}\" - dwuklik, aby wstawić",
        "text_use_template": "Użyj fragmentu tekstu",
        "text_type": "Typ",
        "text_search_templates": "Szukaj fragmentów tekstu...",

        # ============================================
        # 83. SETTINGS EXPORT INFO
        # ============================================
        "qsettings_export_import_title": "📦 Informacje o eksporcie / imporcie",
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

        <h3>📦 Co jest eksportowane? (Przegląd)</h3>

        <ul>
            <li><span class="checkmark">✓</span> <span class="category">Ogólne ustawienia aplikacji</span></li>
            <li class="detail">• Tryb jasny/ciemny</li>
            <li class="detail">• Inwersja obrazów w trybie ciemnym</li>
            <li class="detail">• Próg szarości</li>
            <li class="detail">• Język</li>
            <li class="detail">• Geometria okna</li>
            <li class="detail">• Tryb zoomu</li>
            <li class="detail">• Nawigacja (pasek przycisków widoczny)</li>
            <li class="detail">• Syntezator mowy (włącz/wyłącz)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Ustawienia kopii zapasowej</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Nazewnictwo plików (znacznik czasu, separator, sufiksy)</span></li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Ustawienia dla wstawek</span></li>
            <li class="detail">• Podpisy</li>
            <li class="detail">• Tekst i fragmenty tekstu</li>
            <li class="detail">• Krzyżyki, obrazy i kształty</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Ustawienia OCR</span></li>
            <li class="detail">• Język</li>
            <li class="detail">• Wymuś OCR · tryb strony</li>
            <li class="detail">• Przetwarzanie wstępne obrazu: Deskew, Clean, Oversampling</li>
            <li class="detail">• Liczba równoległych zadań</li>
            <li class="detail">• Tryb inwersji</li>
            <li class="detail">• Próg szarości</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Zakładki</span></li>
            <li class="detail">• Wszystkie zakładki dla każdego pliku PDF (strona, nazwa, czas utworzenia)</li>

            <li style="margin-top: 16px;"><span class="checkmark">✓</span> <span class="category">Baza danych haseł</span></li>
            <li class="detail">• Zapisane hasła PDF (do wyboru zaszyfrowane lub jawne)</li>
            <li class="detail">• Hash hasła głównego (jeśli ustawiony)</li>
            <li class="detail">• Dane weryfikacyjne</li>
        </ul>

        <h4>⚠️ Ważne uwagi</h4>

        <div class="box">
            <strong style="color: #FFD700;">📥 Przy imporcie:</strong>
            <ul>
                <li><span class="warning">➜ WSZYSTKIE bieżące ustawienia zostaną całkowicie nadpisane</span></li>
                <li>• Ponowne uruchomienie aplikacji jest wymagane</li>
                <li>• Istniejące podpisy, fragmenty tekstu i zakładki zostaną zastąpione</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #87CEEB;">🔐 Hasło główne i tryb eksportu:</strong>
            <ul>
                <li>• Przy aktywnym haśle głównym możesz wybrać:</li>
                <li>  - <span style="color: #98FB98;"><strong>Odszyfrowane</strong></span> (hasła w postaci jawnej w ZIP)</li>
                <li>  - <span style="color: #FFA07A;"><strong>Zaszyfrowane</strong></span> (czytelne tylko z hasłem głównym w docelowym systemie)</li>
                <li>• Hash hasła głównego jest <strong>zawsze</strong> przechowywany w zaszyfrowanej formie</li>
            </ul>
        </div>

        <div class="box">
            <strong style="color: #FFA07A;">🛡️ Wskazówki bezpieczeństwa:</strong>
            <ul>
                <li>• Eksportowany plik ZIP zawiera poufne dane (<strong>hasła, zakładki, podpisy</strong>)</li>
                <li>• Przechowuj go bezpiecznie (np. zaszyfrowany pendrive, menedżer haseł)</li>
                <li>• W przypadku utraty pliku zapisane hasła PDF są bezpowrotnie utracone</li>
            </ul>
        </div>

        <h4>📁 Format eksportu</h4>
        <p style="margin-left: 20px; color: #DDDDDD;">
            Ustawienia są zapisywane w jednym pliku ZIP:<br>
            <code>PDFDarkView_Settings_YYYYMMDD_HHMMSS.zip</code>
        </p>
        <p style="margin-left: 20px; color: #BBBBBB; font-size: 14px;">
            Ten ZIP zawiera kompletny plik <code>settings.json</code> (z Twojej konfiguracji) oraz ewentualnie osadzone pliki obrazów podpisów i zaszyfrowane hasła.
        </p>

        </body>
        </html>""",

        # ======================================================
        # 84. HILFEDIALOGE FÜR UNTERSCHRIFTEN, BILDER UND FORMEN
        # ======================================================
        'signature_guide_title': "Podpisy – instrukcja",
        'signature_guide_html': """
        📝 <strong>Podpisy – krótka instrukcja</strong><br>
        <ul>
        <li>Ustaw hasło główne</li>
        <li>Skonfiguruj podpisy w menu <em>Ustawienia</em> (rozmiar, znacznik czasu, …)</li>
        <li>Wstaw za pomocą <strong>PRAWEgo PRZYCIŚKU</strong> w żądanym miejscu (hasło główne wymagane raz na sesję)</li>
        <li>Przesuwaj podpis myszą lub klawiszami strzałek</li>
        <li>Można wstawić wiele podpisów jeden po drugim</li>
        <li>Każdy podpis można dostosować indywidualnie</li>
        <li>Odrzuć pojedynczy podpis</li>
        <li>Zapisz / odrzuć wszystkie podpisy jednocześnie</li>
        <li>Alternatywnie można użyć paska menu.</li>
        </ul>
        """,
        'signature_guide_voice': "Krótka instrukcja podpisów. Ustaw hasło główne. Skonfiguruj podpisy w ustawieniach. Wstaw za pomocą prawego przycisku.",

        'image_guide_title': "Wstawianie obrazów – instrukcja",
        'image_guide_html': """
        📷 <strong>Wstawianie obrazów do PDF – krótka instrukcja</strong><br>
        <ol>
        <li>Kliknij prawym przyciskiem w żądanym miejscu</li>
        <li>„Wstaw obraz” → wybierz obraz</li>
        <li>Pozycjonuj obraz: przeciągaj myszą</li>
        <li>Zmień rozmiar: przeciągaj za rogi/krawędzie</li>
        <li>Zachowaj proporcje: klawisz <strong>[A]</strong></li>
        <li>Dalsze dostosowania: prawy przycisk na obrazie</li>
        </ol>
        <p><strong>Wskazówka:</strong> W menu kontekstowym można dostosować ustawienia.</p>
        """,
        'image_guide_voice': "Krótka instrukcja obrazów. Kliknij prawym przyciskiem, wstaw obraz, wybierz. Pozycjonuj myszą, zmieniaj rozmiar za rogi. Zachowaj proporcje klawiszem A.",

        'form_guide_title': "Wstawianie kształtów – instrukcja",
        'form_guide_html': """
        📐 <strong>Wstawianie kształtów do PDF – krótka instrukcja</strong><br>
        <ol>
        <li>Wybierz typ kształtu (prostokąt, elipsa, linia, strzałka)</li>
        <li>Kliknij w miejscu docelowym:
            <ul>
            <li>Dla prostokąta/elipsy: jedno kliknięcie umieszcza kształt</li>
            <li>Dla linii/strzałki: dwa kliknięcia dla punktu początkowego i końcowego</li>
            </ul>
        </li>
        <li>Pozycjonuj kształt: przeciągaj myszą</li>
        <li>Zmień rozmiar: przeciągaj za rogi/krawędzie</li>
        <li>Zapisz kształt: <strong>Enter</strong></li>
        <li>Odrzuć kształt: <strong>ESC</strong></li>
        <li>Dalsze dostosowania: prawy przycisk na kształcie</li>
        </ol>
        <p><strong>Wskazówka:</strong> W menu kontekstowym można dostosować ustawienia.</p>
        """,
        'form_guide_voice': "Krótka instrukcja kształtów. Wybierz typ kształtu. Dla prostokąta lub elipsy kliknij raz, dla linii lub strzałki dwa razy. Pozycjonuj myszą, zmieniaj rozmiar za rogi. Zapisz Enter, odrzuć Escape.",

        # ============================================
        # 85. OCR TEXTFENSTER
        # ============================================
        "btn_prev_result": "poprzedni",
        "btn_next_result": "następny",
        "ocr_text_window": "Okno tekstu OCR",
        "bookmark_existing": "Istniejące zakładki",

        # ============================================
        # 86. OCR Vergleich Mac Win
        # ============================================
        'ocr_method_mac_win_menu': "Porównanie OCR Mac - Windows",
        'ocr_method_mac_win_title': "Różnice OCR między Mac i Windows",
        'ocr_method_mac_win_voice': "Mac jest lepszy",
        'ocr_method_mac_win_html': """
        <html>
        <head/>
        <body style="font-family:'Arial'; font-size:14px; color:#E0E0E0;">
        <p><strong>📄 OCR – różnice między macOS a Windows</strong></p>

        <p><strong>macOS (zalecany)</strong></p>
        <p>Narzędzie:</p>
        <ul>
        <li>Tesseract + ocrmypdf</li>
        </ul>
        <p>Wynik:</p>
        <ul>
        <li>Przeszukiwalny PDF z osadzonym tekstem, który w dużej mierze zachowuje oryginalny układ.</li>
        </ul>
        <p>Zalety:</p>
        <ul>
        <li>Doskonała jakość rozpoznawania tekstu (również przy przekoszonych stronach).</li>
        <li>Zachowanie grafiki wektorowej i czcionek.</li>
        <li>Pasek postępu GUI oparty na analizie subprocess.</li>
        <li>Pełna kontrola nad wszystkimi parametrami OCR (Deskew, Clean, Oversample, optymalizacja).</li>
        <li>Wyszukiwanie tekstu dostępne bezpośrednio w oknie głównym (widok PDF).</li>
        </ul>
        <p>Wady:</p>
        <ul>
        <li>Wymaga dodatkowych narzędzi systemowych (ocrmypdf, Ghostscript, unpaper, pngquant – zawarte w pakiecie aplikacji).</li>
        <li>Bardziej złożona obsługa błędów (zakleszczenia, limity czasu).</li>
        </ul>

        <p><strong>Windows (stabilna alternatywa)</strong></p>
        <p>Narzędzie:</p>
        <ul>
        <li>pytesseract (bezpośrednie połączenie z Tesseract) + reportlab + PyPDF2</li>
        </ul>
        <p>Wynik:</p>
        <ul>
        <li>Przeszukiwalny PDF, który wizualnie przypomina obraz PDF, ale dzięki przezroczystemu tekstowi jest przeszukiwalny.</li>
        </ul>
        <p>Zalety:</p>
        <ul>
        <li>Nie przychodzą mi do głowy żadne.</li>
        </ul>
        <p>Wady:</p>
        <ul>
        <li>PDF jest w zasadzie obrazem z niewidocznym tekstem; układ może nieznacznie odbiegać w przypadku złożonych dokumentów (kolumny, tabele).</li>
        <li>Brak automatycznej korekty przekoszenia (--deskew) lub czyszczenia obrazu (--clean).</li>
        <li>Pasek postępu GUI jest aktualizowany tylko ogólnie na podstawie liczby przetworzonych stron.</li>
        <li>Prędkość OCR jest nieco wolniejsza (ponieważ każda strona jest przetwarzana osobno).</li>
        <li>Wyszukiwanie tekstu jest przekierowywane do okna tekstu OCR.</li>
        </ul>

        <p><strong>Wspólne cechy</strong></p>
        <ul>
        <li>Obie metody tworzą przeszukiwalny PDF w tym samym katalogu co plik źródłowy.</li>
        <li>Ustawienia OCR (język, DPI, tryb segmentacji strony, tryb silnika OCR) można skonfigurować za pomocą OCRSettingsDialog i działają one w obu implementacjach.</li>
        </ul>

        <p><strong>Zalecenie:</strong></p>
        <ul>
        <li>macOS: binarna ocrmypdf daje najlepsze wyniki – kup Maca i korzystaj z wersji (PDFDarkView dla Maców z Apple Silicon lub Intel). Wyniki OCR są lepsze niż pod Windows!</li>
        <li>Windows: użyj rozwiązania pytesseract. Jest stabilne i zapewnia wystarczającą jakość dla większości dokumentów.</li>
        </ul>

        <p><strong>Ważne:</strong></p>
        <ul>
        <li>Obie wersje są w pełni zintegrowane z interfejsem użytkownika – użytkownik nie zauważa różnicy.</li>
        <li>Decyzję, który silnik OCR zostanie użyty, program podejmuje automatycznie na podstawie systemu operacyjnego.</li>
        </ul>
        </body>
        </html>
        """,

        # ============================================
        # 87. SIGNATUR ERSTELLEN (REMBG)
        # ============================================
        "signature_create_from_scan": "Utwórz podpis (ze skanu)",
        "signature_create_title": "Wybierz zeskanowany podpis (PDF/obraz)",
        "image_pdf_filter": "Obrazy i PDF",
        "signature_pdf_empty": "PDF nie zawiera żadnych stron.",
        "signature_created_success": "Podpis został pomyślnie utworzony: {0}",
        "signature_create_error": "Błąd podczas tworzenia podpisu:\n{0}",
        "rembg_missing": "rembg nie jest zainstalowane.\nZainstaluj: pip install rembg\nBłąd: {0}",
        "signature_name_title": "Nazwa pliku dla podpisu",
        "signature_name_message": "Podaj nazwę pliku dla nowego podpisu (zostanie zapisany jako PNG z przezroczystym tłem):",
        "signature_name_label": "Nazwa pliku:",
        "signature_name_voice": "Wprowadź nazwę pliku dla podpisu",
        "signature_processing": "Przetwarzanie...",
        "signature_creation_title": "Tworzenie podpisu",
        "signature_overwrite_warning": "Plik '{0}' już istnieje. Nadpisać?",
        # NEUE SIGNATUR ERSTELLEN
        "signature_prepare_title":"Przygotowanie PDF dla podpisu",
        "signature_prepare_instruction":"Wybierz PDF, który na jednej stronie zawiera zeskanowany podpis.\n\nOptymalne rozpoznanie uzyskasz, gdy:\n• Podpis jest napisany czarnym tuszem (długopis lub cienkopis) na białym papierze.\n• Podpis znajduje się w górnej jednej trzeciej pustej strony A4.\n• PDF został zeskanowany z rozdzielczością co najmniej 300 dpi.\n• Podpis jest wyraźny i nie zbyt cienki.\n• Brak przeszkadzających wzorów tła lub linii.",
        "signature_prepare_voice":"Wybierz PDF z zeskanowanym podpisem. Zwróć uwagę na dobrą jakość i kontrast.",
        "sig_thickness_label":"Grubość linii:",
        "sig_thickness_normal":"Normalna (cienka)",
        "sig_thickness_bold":"Gruba (zalecana)",
        "sig_thickness_very_bold":"Bardzo gruba",

        # ============================================
        # 88. SPRACHEN HINZUFÜGEN (OCR und GUI) Anleitung
        # ============================================
        'language_guide_menu': "Dodawanie języków GUI i OCR – instrukcja",
        'language_guide_title': "Dodawanie języków GUI i OCR",
        'language_guide_detailed_html': """
        <html>
        <head/>
        <body>
        <h2>GUI</h2>
        <p>Pobierz żądany plik tłumaczenia <code>translations_xy.py</code> z<br/>
        <a style="color:#E0E0E0;" href="https://github.com/BinhDiez64/PDFDarkView/tree/main/translations">https://github.com/BinhDiez64/PDFDarkView/tree/main/translations</a><br/>
        i umieść go w następującym katalogu:</p>
        <ul>
        <li><strong>macOS</strong>:<br/><code>~/Library/Application Support/PDFDarkView/translations/</code></li>
        <li><strong>Windows</strong>:<br/><code>%USERPROFILE%\\AppData\\Local\\PDFDarkView\\translations</code></li>
        <li><strong>Linux</strong>:<br/><code>~/.local/share/PDFDarkView/translations</code></li>
        </ul>

        <h2>OCR</h2>
        <ol>
        <li>Otwórz przeglądarkę internetową.</li>
        <li>Przejdź do: <a style="color:#E0E0E0;" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></li>
        <li>Szukaj po prawej stronie ekranu "Releases" i wybierz to oznaczone <strong>"latest"</strong>.</li>
        <li>Na następnej stronie wydania pobierz na dole plik <code>Source Code.zip</code>.</li>
        <li>Rozpakuj plik ZIP.</li>
        <li>W rozpakowanym folderze znajdź wszystkie potrzebne pliki językowe i skopiuj je do katalogu:<br/>
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
        "menu_watermark":"Wstaw znak wodny",
        "fullpage_text_watermark_title":"Znak wodny (tekst)",
        "fullpage_image_watermark_title":"Znak wodny (obraz)",
        "filename_with_watermark":"_ze_znakiem_wodnym",

        # ===== DIALOG TEXTE =====
        "watermark_text":"Tekst:",
        "watermark_text_placeholder":"Twój tekst znaku wodnego...",
        "watermark_font_family":"Czcionka:",
        "watermark_font_size":"Rozmiar czcionki:",
        "watermark_format":"Formatowanie:",
        "watermark_bold":"Pogrubienie",
        "watermark_italic":"Kursywa",
        "watermark_color":"Kolor:",
        "watermark_choose_color":"Wybierz kolor...",
        "watermark_opacity":"Przezroczystość / krycie:",
        "watermark_direction":"Kierunek odczytu:",
        "watermark_direction_l_r":"Lewo → Prawo",
        "watermark_direction_bl_tr":"Lewy dół → Prawa góra",
        "watermark_direction_tl_br":"Lewy góra → Prawy dół",
        "watermark_direction_b_t":"Dół → Góra",
        "watermark_direction_t_b":"Góra → Dół",
        "watermark_preview":"Podgląd:",
        "watermark_preview_sample":"Przykładowy tekst",
        "watermark_empty_text":"Wprowadź tekst.",
        "watermark_applied":"Znak wodny został zastosowany na wszystkich stronach.",
        "watermark_saved":"Znak wodny zapisany.",

        # ===== DIALOG BILD =====
        "image_scale":"Rozmiar:",
        "image_preview":"Podgląd obrazu:",
        "no_image_selected":"Nie wybrano obrazu",
        "browse":"Przeglądaj...",

        # ============================================
        # 90. AUSLÖSCHUNGEN SCHWÄRZEN / RADIERGUMMI (REDAKTION)
        # ============================================
        "menu_redact": "Wycinki",
        "redact_add_black": "Wycinek (czarny)",
        "redact_add_white": "Wycinek (biały / gumka)",
        "redact_added_black": "Dodano czarny wycinek",
        "redact_added_white": "Dodano biały wycinek",
        "redact_apply_all": "Zastosuj i zapisz wszystkie wycinki",
        "redact_discard_all": "Odrzuć wszystkie wycinki",
        "redact_discard": "Odrzuć ten wycinek",
        "no_redactions": "Brak wycinków",
        "redact_confirm_title": "Trwale zastosować wycinki",
        "redact_confirm_message": "Uwaga: Zaznaczone obszary zostaną trwale usunięte (czarne lub białe).\nKopia zapasowa zostanie utworzona (jeśli włączona).\n\nKontynuować?",
        "redact_apply": "Tak, usuń teraz",
        "redact_saved": "Pomyślnie zastosowano i zapisano {0} wycinek(ów).",
        "redact_saved_voice": "Zastosowano {0} wycinek(ów)",
        "redact_error": "Błąd podczas wycinania",
        "filename_redacted":"_z_wycinkami",

        # ============================================
        # 91. SEITENZAHLEN EINFÜGEN
        # ============================================
        # Dialog-Titel und Beschriftungen
        'page_numbers_title': 'Wstaw numery stron',
        'page_numbers_format': 'Format numerów:',
        'page_numbers_format_arabic': '1, 2, 3 ... (arabskie)',
        'page_numbers_format_roman_lower': 'i, ii, iii ... (rzymskie małe)',
        'page_numbers_format_roman_upper': 'I, II, III ... (rzymskie duże)',
        'page_numbers_format_letter': 'A, B, C ... (litery)',
        'page_numbers_format_custom': 'Niestandardowy',
        'page_numbers_custom_pattern': 'Wzór:',
        'page_numbers_custom_placeholder': 'np. "Strona {nummer}" lub "{nummer} / {total}"',
        'page_numbers_custom_tooltip': 'Użyj {nummer} dla bieżącego numeru i {total} dla całkowitej liczby stron',
        'page_numbers_position': 'Pozycja:',
        'page_numbers_pos_tl': 'Lewy górny',
        'page_numbers_pos_tc': 'Górny środek',
        'page_numbers_pos_tr': 'Prawy górny',
        'page_numbers_pos_ml': 'Lewy środkowy',
        'page_numbers_pos_mc': 'Środek',
        'page_numbers_pos_mr': 'Prawy środkowy',
        'page_numbers_pos_bl': 'Lewy dolny',
        'page_numbers_pos_bc': 'Dolny środek',
        'page_numbers_pos_br': 'Prawy dolny',
        'page_numbers_margins': 'Marginesy:',
        'page_numbers_margin_x': 'Margines poziomy:',
        'page_numbers_margin_y': 'Margines pionowy:',
        'page_numbers_range': 'Zakres stron:',
        'page_numbers_all_pages': 'Wszystkie strony',
        'page_numbers_custom_range': 'Zakres niestandardowy',
        'page_numbers_from': 'Od:',
        'page_numbers_to': 'Do:',
        'page_numbers_progress': 'Wstawianie numerów stron...',
        'page_numbers_start': 'Rozpoczęcie wstawiania numerów stron...',
        'page_numbers_cancel': 'Anulowano wstawianie numerów stron',
        'page_numbers_success': 'Numery stron zostały pomyślnie dodane.\n\nCzy chcesz otworzyć nowy PDF?\n\n{0}',
        'page_numbers_complete': 'Dodano numery stron',
        'page_numbers_error_format': 'Błąd podczas wstawiania numerów stron: {0}',
        # Zusätzliche Übersetzungen für den erweiterten Dialog
        'page_numbers_content_type': 'Typ zawartości:',
        'page_numbers_tab_simple': 'Prosty numer',
        'page_numbers_tab_range': 'Strona X z Y',
        'page_numbers_tab_date': 'Data',
        'page_numbers_tab_custom': 'Dowolny tekst',
        'page_numbers_range_format': 'Format:',
        'page_numbers_range_short': '{aktualny}/{całkowity}',
        'page_numbers_range_long': 'Strona {aktualny} z {całkowity}',
        'page_numbers_range_custom': 'Niestandardowy',
        'page_numbers_range_placeholder': 'np. "Strona {aktualny} / {całkowity}"',
        'page_numbers_date_format': 'Format daty:',
        'page_numbers_date_short': '01.01.2024',
        'page_numbers_date_long': '1 stycznia 2024',
        'page_numbers_date_iso': '2024-01-01',
        'page_numbers_date_us': '01/01/2024',
        'page_numbers_date_custom': 'Niestandardowy',
        'page_numbers_date_placeholder': 'np. %d.%m.%Y %H:%M',
        'page_numbers_date_position': 'Pozycja:',
        'page_numbers_date_before': 'Data przed numerem strony',
        'page_numbers_date_after': 'Data po numerze strony',
        'page_numbers_date_only': 'Tylko data (bez numeru)',
        'page_numbers_custom_text': 'Tekst niestandardowy:',
        'page_numbers_custom_placeholder_text': 'Użyj {strona} dla numeru strony i {całkowity} dla całkowitej liczby\nnp. "Poufne - strona {strona}" lub "{strona} z {całkowity}"',
        "filename_with_page_number":"_z_numerem_strony",
        "filename_with_page_declaration":"_z_oznaczeniem_strony",
        "filename_with_pagenumber":"_z_numerem_strony",
        "filename_with_date":"_z_data",
        "filename_with_my_page_declaration":"_z_wlasnym_oznaczeniem_strony",

        # ============================================
        # 92. ASK TOGGLE DARK MODE
        # ============================================
        "unsaved_changes_title": "Niezapisane zmiany",
        "unsaved_changes_message_darkmode": "Istnieją niezapisane wstawki.\nCzy chcesz je zapisać przed przełączeniem?",
        "save_and_switch": "Zapisz i przełącz",
        "discard_and_switch": "Przełącz teraz",

        # ============================================
        # 94. SEITEN ALS BILDER EXPORTIEREN
        # ============================================
        # Export Images Dialog
        'export_images_title': 'Eksportuj strony jako obrazy',
        'export_images_menu': 'Eksportuj jako obrazy (PNG/JPEG)',
        'export_images_format': 'Format obrazu:',
        'export_images_dpi': 'Rozdzielczość (DPI):',
        'export_images_quality': 'Jakość JPEG:',
        'export_images_range': 'Zakres stron:',
        'export_images_all_pages': 'Wszystkie strony',
        'export_images_custom_range': 'Zakres niestandardowy',
        'export_images_from': 'Od:',
        'export_images_to': 'Do:',
        'export_images_options': 'Opcje:',
        'export_images_single_files': 'Każda strona jako osobny plik',
        'export_images_subfolder': 'Eksportuj do podfolderu',
        'export_images_subfolder_info': 'Do podfolderu "NazwaPDF_obrazy"',
        'export_images_same_folder': 'W tym samym folderze co PDF',
        'export_images_apply_darkmode': 'Zastosuj ustawienia PDFDarkView (tryb ciemny)',
        'export_images_target_folder': 'Folder docelowy:',
        'export_images_browse': 'Przeglądaj...',
        'export_images_preview': 'Podgląd:',
        'export_images_preview_info': 'Wybierz ustawienia dla eksportu',
        'export_images_preview_info_detail': '{0} stron jako {1}\nRozdzielczość: {2} DPI\nNazwa pliku: {3}\n{4}',
        'export_images_select_folder': 'Wybierz folder docelowy',
        'export_images_start': 'Rozpoczęcie eksportu obrazów...',
        'export_images_progress': 'Eksportowanie obrazów...',
        'export_images_saving': 'Zapisywanie strony {0} z {1}...',
        'export_images_success': 'Eksport powiódł się!\n\nZapisano {0} obrazów w:\n{1}',
        'export_images_complete': 'Eksport obrazów zakończony',
        'export_images_open_folder': '📁 Otwórz folder',
        'export_images_cancel': 'Anulowano eksport obrazów',
        'export_images_error_format': 'Błąd podczas eksportu obrazów: {0}',
        'export_images_pdf2image_missing': 'Biblioteka "pdf2image" nie jest zainstalowana.\n\nZainstaluj ją za pomocą:\npip install pdf2image\n\nDla Windows potrzebny jest również Poppler:\nhttps://github.com/oschwartz10612/poppler-windows/releases/',

        # ============================================
        # 94. PDF/A KONVERTIERUNG
        # ============================================
        # PDF/A Dialog
        'pdfa_title': 'Konwersja do PDF/A dla długotrwałego archiwizowania',
        'pdfa_menu': 'Konwersja do PDF/A (archiwalna)',
        'pdfa_info': 'Konwertuje PDF do formatu PDF/A.\n\nPDF/A jest przeznaczony do długotrwałego archiwizowania i zapewnia, że dokument będzie poprawnie wyświetlany również w przyszłości.',
        'pdfa_standard': 'Standard PDF/A:',
        'pdfa_standard_select': 'Wersja:',
        'pdfa_1': 'PDF/A-1 (prosty, szeroko kompatybilny)',
        'pdfa_2': 'PDF/A-2 (nowoczesny, lepsza kompresja)',
        'pdfa_3': 'PDF/A-3 (najnowsza wersja, pozwala na załączniki)',
        'pdfa_standards_explanation': '📖 Wyjaśnienie standardów:\n\n'
            '• PDF/A-1: Podstawowy, kompatybilny ze starszymi systemami (ok. 2005)\n'
            '• PDF/A-2: Nowocześniejszy, lepsza kompresja, obsługa przezroczystości (ok. 2011)\n'
            '• PDF/A-3: Najnowsza wersja, umożliwia dołączanie plików (ok. 2013)\n\n'
            'Zalecenie: PDF/A-2 to dobry kompromis między kompatybilnością a nowoczesnymi funkcjami.',
        'pdfa_options': 'Opcje:',
        'pdfa_compress_enable': 'Kompresuj PDF (mniejszy plik)',
        'pdfa_metadata_preserve': 'Zachowaj metadane (tytuł, autor, itp.)',
        'pdfa_target_folder': 'Folder docelowy:',
        'pdfa_browse': 'Przeglądaj...',
        'pdfa_select_folder': 'Wybierz folder docelowy',
        'pdfa_ocr_info_unknown': '🔍 Nie można sprawdzić zawartości tekstowej.',
        'pdfa_ocr_info_not_needed': '✅ Tekst istnieje - OCR nie jest wymagane.\nPDF/A można utworzyć bezpośrednio.',
        'pdfa_ocr_info_recommended': '⚠️ Nie znaleziono wystarczającego tekstu.\n\nDla przeszukiwalnych PDF zalecamy wcześniejsze wykonanie OCR.\nUwaga: PDF/A działa również bez OCR - tekst nie będzie wtedy przeszukiwalny.',
        'pdfa_ocr_info_error': '❌ Błąd podczas sprawdzania: {0}',
        'pdfa_start': 'Rozpoczęcie konwersji do PDF/A...',
        'pdfa_progress': 'Konwersja do PDF/A w toku...',
        'pdfa_success': 'Konwersja do PDF/A powiodła się!\n\nZapisano jako:\n{0}\n\nCzy chcesz otworzyć nowy PDF?',
        'pdfa_complete': 'Konwersja do PDF/A zakończona',
        'pdfa_cancel': 'Anulowano konwersję do PDF/A',
        'pdfa_error_format': 'Błąd podczas konwersji do PDF/A:\n\n{0}',
        'pdfa_ocrmypdf_missing': 'Biblioteka "ocrmypdf" nie jest zainstalowana.\n\nZainstaluj ją za pomocą:\npip install ocrmypdf',
        'btn_convert': 'Konwertuj',
        'filename_pdfa1_suffix':"_PDFA-1",
        'filename_pdfa2_suffix':"_PDFA-2",
        'filename_pdfa3_suffix':"_PDFA-3",

        ### ------------------------------------
        ### 95. OPTIMIEREN (KOMPIMIEREN)
        ### ------------------------------------
        # ===== PDF OPTIMIEREN =====
        'optimize_title': 'Optymalizacja PDF (zmniejszenie rozmiaru)',
        'optimize_menu': 'Optymalizuj PDF (rozmiar)',
        'optimize_info': 'Zmniejsza rozmiar pliku PDF za pomocą różnych metod optymalizacji.\n\nIm wyższy poziom kompresji, tym mniejszy plik - przy możliwej utracie jakości obrazów.',
        'optimize_level': 'Poziom kompresji:',
        'optimize_level_low': 'Niski (szybki, niewielka oszczędność)',
        'optimize_level_medium': 'Średni (dobry kompromis)',
        'optimize_level_high': 'Wysoki (duża oszczędność)',
        'optimize_level_maximum': 'Maksymalny (maksymalna oszczędność, wolny)',
        'optimize_level_explanation': 'Zalecenie: "Średni" to dobry kompromis między szybkością a rozmiarem pliku.',
        'optimize_options': 'Opcje:',
        'optimize_compress_images': 'Kompresuj obrazy (zmniejsz jakość JPEG)',
        'optimize_clean_objects': 'Usuń nieużywane obiekty',
        'optimize_preserve_metadata': 'Zachowaj metadane (tytuł, autor, itp.)',
        'optimize_image_quality': 'Jakość obrazów:',
        'optimize_range': 'Zakres stron:',
        'optimize_all_pages': 'Wszystkie strony',
        'optimize_custom_range': 'Zakres niestandardowy',
        'optimize_from': 'Od:',
        'optimize_to': 'Do:',
        'optimize_target_folder': 'Folder docelowy:',
        'optimize_browse': 'Przeglądaj...',
        'optimize_select_folder': 'Wybierz folder docelowy',
        'optimize_info_box': 'Informacje',
        'optimize_info_text': 'Optymalizacja dużych PDF-ów może zająć kilka minut.\n\nObrazy są zapisywane z obniżoną jakością, co może znacznie zmniejszyć rozmiar pliku.',
        'optimize_start': 'Rozpoczęcie optymalizacji PDF...',
        'optimize_progress': 'Optymalizacja PDF w toku...',
        'optimize_cancel': 'Anulowano optymalizację PDF',
        'optimize_complete': 'Optymalizacja PDF zakończona',
        'optimize_error_format': 'Błąd podczas optymalizacji PDF:\n\n{0}',
        # Erfolgsmeldungen (mit Platzhaltern)
        'optimize_success_message': 'Optymalizacja PDF powiodła się!\n\nZapisano jako:\n{0}\n\nPrzed:  {1}\nPo:     {2}\nOszczędność: {3:.1f}%\n\n{4}\n\nCzy chcesz otworzyć zoptymalizowany PDF?',
        'optimize_success_message_no_size': 'Optymalizacja PDF powiodła się!\n\nZapisano jako:\n{0}\n\nInformacje o rozmiarze niedostępne.\n\nCzy chcesz otworzyć zoptymalizowany PDF?',
        # Ergebnis-Texte
        'optimize_result_positive': 'Plik został zmniejszony o {0:.1f}%.',
        'optimize_result_zero': 'Brak zmiany rozmiaru pliku.',
        'optimize_result_negative': 'Plik jest większy o {0:.1f}%.\nOptymalizacja została pominięta, zachowano oryginalny plik.',
        'btn_optimize': 'Rozpocznij optymalizację',
        # Dateinamen-Suffixe
        'filename_optimize_low_suffix': '_optymalizowany_niski',
        'filename_optimize_medium_suffix': '_optymalizowany',
        'filename_optimize_high_suffix': '_optymalizowany_wysoki',
        'filename_optimize_maximum_suffix': '_optymalizowany_max',

        ### ------------------------------------
        ### 96. ZUSCHNEIDEN CROPPING
        ### ------------------------------------
        # ===== PDF ZUSCHNEIDEN =====
        # Crop Dialog
        'crop_title': 'Przytnij PDF',
        'crop_menu': 'Przytnij PDF',
        'crop_range': 'Zastosuj do:',
        'crop_all_pages': 'Wszystkie strony',
        'crop_current_page': 'Tylko bieżąca strona',
        'crop_values': 'Wartości przycinania (w punktach):',
        'crop_left': 'Lewo:',
        'crop_right': 'Prawo:',
        'crop_top': 'Góra:',
        'crop_bottom': 'Dół:',
        'crop_presets': 'Ustawienia wstępne:',
        'crop_preset_white': 'Wykryj białe marginesy',
        'crop_reset': 'Resetuj',
        'crop_mouse_hint': '🖱️ Przeciągnij prostokąt, aby wstępnie wybrać obszar.\nNastępnie możesz dostosować wartości w polach liczbowych.\nRęczna korekta myszą nie jest możliwa.',
        'crop_apply': 'Przytnij',
        'crop_scope_all': 'Wszystkie strony',
        'crop_scope_current': 'Bieżąca strona',
        'crop_new_size': 'Nowy rozmiar: {0:.0f} x {1:.0f} pt',
        'crop_no_pdf': 'Nie załadowano PDF',
        'crop_preview_error': 'Błąd podczas ładowania podglądu',
        'crop_start': 'Rozpoczęcie przycinania...',
        'crop_progress': 'Przycinanie PDF w toku...',
        'crop_success': 'PDF został pomyślnie przycięty!\n\nZapisano jako:\n{0}\n\nCzy chcesz otworzyć przycięty PDF?',
        'crop_complete': 'Przycinanie zakończone',
        'crop_cancel': 'Anulowano przycinanie',
        'crop_error_format': 'Błąd podczas przycinania:\n\n{0}',
        'filename_crop_suffix': '_przyciety',

        # ============================================
        # 97. PDF GLÄTTEN FLATTEN
        # ============================================
        # ===== PDF GLÄTTEN =====
        'flatten_title': 'Spłaszcz PDF (Flatten)',
        'flatten_menu': 'Spłaszcz PDF (Flatten)',
        'flatten_info': 'Spłaszczenie PDF "wypala" wszystkie edytowalne elementy w treści strony.\n\nPo tym formularze, adnotacje, teksty, krzyżyki, podpisy, obrazy i kształty nie są już osobno edytowalne.',
        'flatten_explanation_title': '📖 Do czego to służy?',
        'flatten_explanation_text': 'Spłaszczenie jest potrzebne w następujących sytuacjach:\n\n'
            '• 📄 Przygotowanie dokumentu do druku\n'
            '• 🔒 Zapobieganie zmianom w polach formularzy\n'
            '• 📎 Trwałe osadzenie adnotacji i komentarzy w dokumencie\n'
            '• 🖼️ Trwałe zakotwiczenie wstawionych tekstów, krzyżyków, podpisów, obrazów i kształtów\n'
            '• 📦 Przygotowanie pliku do archiwizacji\n\n'
            'Spłaszczenie zmniejsza rozmiar PDF i zapobiega przypadkowemu przesuwaniu lub usuwaniu elementów.',
        'flatten_what_title': 'Co jest spłaszczane?',
        'flatten_what_list': '• ✅ Pola formularzy (pola tekstowe, checkboxy, przyciski)\n'
            '• ✅ Adnotacje (komentarze, podkreślenia, notatki)\n'
            '• ✅ Nakładki (teksty, krzyżyki, podpisy, obrazy, kształty)',
        'flatten_options': 'Opcje:',
        'flatten_forms': 'Spłaszcz pola formularzy',
        'flatten_annotations': 'Spłaszcz adnotacje',
        'flatten_overlays': 'Spłaszcz nakładki (teksty, krzyżyki, podpisy, obrazy, kształty)',
        'flatten_target_folder': 'Folder docelowy:',
        'flatten_browse': 'Przeglądaj...',
        'flatten_select_folder': 'Wybierz folder docelowy',
        'flatten_warning': '⚠️ Ważne: Spłaszczenie jest operacją nieodwracalną!\n\nPo spłaszczeniu edytowalne elementy nie mogą być już indywidualnie zmieniane ani usuwane.\n\nW razie potrzeby utwórz kopię zapasową przed spłaszczeniem.',
        'flatten_apply': 'Spłaszcz',
        'flatten_start': 'Rozpoczęcie spłaszczania...',
        'flatten_progress': 'Spłaszczanie PDF w toku...',
        'flatten_success': 'PDF został pomyślnie spłaszczony!\n\nZapisano jako:\n{0}\n\nCzy chcesz otworzyć spłaszczony PDF?',
        'flatten_complete': 'Spłaszczanie zakończone',
        'flatten_cancel': 'Anulowano spłaszczanie',
        'flatten_error_format': 'Błąd podczas spłaszczania:\n\n{0}',
        'filename_flatten_suffix': '_spłaszczony',

        ### ------------------------------------
        ### 98. PDF ÜBEREINANDERLEGEN OVERLAY
        ### ------------------------------------
        'overlay_title': 'Nakładanie PDF (Overlay)',
        'overlay_menu': 'Nakładanie PDF (Overlay)',
        'overlay_info': 'Nakłada jeden PDF (nakładkę) na inny PDF.\n\nNakładka PDF jest umieszczana na bazowym PDF. Przydatne do znaków wodnych, logo, nagłówków lub pieczęci.',
        'overlay_explanation_title': '📖 Do czego to służy?',
        'overlay_explanation_text': 'Nakładanie jest potrzebne w następujących sytuacjach:\n\n'
            '• 🏢 Umieszczenie logo firmy jako znak wodny na każdej stronie\n'
            '• 📄 Nałożenie nagłówka na pusty PDF\n'
            '• 🖊️ Nałożenie pieczęci na dokument\n'
            '• 🔖 Nałożenie znaku wodnego na wszystkie strony\n'
            '• 📑 Nałożenie nakładki formularza na szablon',
        'overlay_type': 'Typ nakładki:',
        'overlay_type_fullpage': 'Cała strona (pokrywająca)',
        'overlay_type_transparent': 'Cała strona (przezroczysta - zalecana)',
        'overlay_type_stamp': 'Pieczęć (można pozycjonować)',
        'overlay_type_info_fullpage': '📄 Nakładka PDF jest umieszczana dokładnie na całej stronie.\nBiałe tło można usunąć, aby widoczna była tylko zawartość.',
        'overlay_type_info_transparent': '🔍 Nakładka PDF jest umieszczana na całej stronie z przezroczystym tłem.\nBiałe tło jest automatycznie usuwane - idealne dla znaków wodnych i logo!',
        'overlay_type_info_stamp': '🖊️ Nakładka PDF jest pozycjonowana i skalowana jako pieczęć.\nIdealne dla logo, pieczęci lub podpisów w określonych miejscach.',
        'overlay_remove_background': 'Usuń białe tło:',
        'overlay_remove_background_enable': 'Usuń białe tło z nakładki PDF (uczyni ją przezroczystą)',
        'overlay_remove_background_tooltip': 'Usuwa białe obszary z nakładki PDF, aby tekst pod spodem był widoczny.',
        'overlay_threshold': 'Próg:',
        'overlay_threshold_hint': '(1-254, wyższy = więcej bieli jest usuwane)',
        'overlay_select_file': 'Wybierz nakładkę PDF:',
        'overlay_file_placeholder': 'Wybierz plik PDF dla nakładki',
        'overlay_browse': 'Przeglądaj...',
        'overlay_select_overlay': 'Wybierz nakładkę PDF',
        'overlay_range': 'Zakres stron:',
        'overlay_all_pages': 'Wszystkie strony',
        'overlay_custom_range': 'Zakres niestandardowy',
        'overlay_from': 'Od:',
        'overlay_to': 'Do:',
        'overlay_position': 'Pozycja:',
        'overlay_position_center': 'Środek',
        'overlay_position_top_left': 'Lewy górny',
        'overlay_position_top_right': 'Prawy górny',
        'overlay_position_bottom_left': 'Lewy dolny',
        'overlay_position_bottom_right': 'Prawy dolny',
        'overlay_size': 'Rozmiar:',
        'overlay_size_original': 'Oryginalny rozmiar',
        'overlay_size_fit_page': 'Dopasuj do strony',
        'overlay_size_custom': 'Niestandardowy (%)',
        'overlay_opacity': 'Przezroczystość:',
        'overlay_target_folder': 'Folder docelowy:',
        'overlay_browse_folder': 'Przeglądaj...',
        'overlay_select_folder': 'Wybierz folder docelowy',
        'overlay_warning': '⚠️ Uwaga: Nakładka PDF jest „wypalana” w bazowym PDF.\n\nElementy nakładki nie mogą być później edytowane indywidualnie.',
        'overlay_apply': 'Nałóż',
        'overlay_start': 'Rozpoczęcie nakładania...',
        'overlay_progress': 'Nakładanie PDF w toku...',
        'overlay_success': 'Nakładanie PDF powiodło się!\n\nZapisano jako:\n{0}\n\nCzy chcesz otworzyć nałożony PDF?',
        'overlay_complete': 'Nakładanie zakończone',
        'overlay_cancel': 'Anulowano nakładanie',
        'overlay_error_format': 'Błąd podczas nakładania:\n\n{0}',
        'overlay_no_file': 'Nie wybrano nakładki PDF.\n\nWybierz plik PDF do nałożenia.',
        'filename_overlay_suffix': '_nałożony',

        ###==============================================
        ### 99. ALLE BILDER EXPTRAHIEREN
        ###==============================================
        'extract_images_title': 'Wyodrębnij obrazy z PDF',
        'extract_images_menu': 'Wyodrębnij wszystkie obrazy',
        'extract_images_info': 'Wyodrębnia wszystkie obrazy z PDF i zapisuje je jako osobne pliki.\n\nObrazy są zapisywane w oryginalnym formacie lub konwertowane do wybranego formatu.',
        'extract_images_format': 'Format obrazu:',
        'extract_images_quality': 'Jakość JPEG:',
        'extract_images_options': 'Opcje:',
        'extract_images_subfolder': 'Wyodrębnij do podfolderu ("NazwaPDF_obrazy")',
        'extract_images_unique': 'Tylko unikalne obrazy (unikaj duplikatów)',
        'extract_images_range': 'Zakres stron:',
        'extract_images_all_pages': 'Wszystkie strony',
        'extract_images_custom_range': 'Zakres niestandardowy',
        'extract_images_from': 'Od:',
        'extract_images_to': 'Do:',
        'extract_images_target_folder': 'Folder docelowy:',
        'extract_images_browse': 'Przeglądaj...',
        'extract_images_select_folder': 'Wybierz folder docelowy',
        'extract_images_info_box': 'Informacje',
        'extract_images_info_text': 'Ekstrakcja może zająć kilka minut w przypadku dużych PDF-ów.\n\nObrazy są zapisywane z nazwami (strona_obraz).',
        'extract_images_extract': 'Wyodrębnij',
        'extract_images_start': 'Rozpoczęcie ekstrakcji...',
        'extract_images_progress': 'Ekstrakcja obrazów w toku...',
        'extract_images_success': '✅ Obrazy zostały pomyślnie wyodrębnione!\n\nZapisano {0} obrazów w:\n{1}',
        'extract_images_complete': 'Ekstrakcja obrazów zakończona',
        'extract_images_cancel': 'Anulowano ekstrakcję',
        'extract_images_error_format': 'Błąd podczas wyodrębniania obrazów:\n\n{0}',
        'extract_images_open_folder': '📁 Otwórz folder',
        'extract_images_no_images': 'Nie znaleziono obrazów w PDF.',

        ### ------------------------
        ### 100.MEHRERE SEITEN AUF EINE SEITE
        ### ------------------------
        'nup_title': 'Wiele stron na jednej stronie (N-Up)',
        'nup_menu': 'Wiele stron na jednej stronie (N-Up)',
        'nup_info': 'Układa wiele stron PDF na jednej stronie.\n\nIdealne do kompaktowych wydruków, przeglądów lub materiałów informacyjnych.',
        'nup_layout': 'Układ:',
        'nup_layout_2x1': '2x1',
        'nup_layout_2x2': '2x2',
        'nup_layout_2x3': '2x3',
        'nup_layout_3x2': '3x2',
        'nup_layout_3x3': '3x3',
        'nup_layout_3x4': '3x4',
        'nup_layout_4x3': '4x3',
        'nup_layout_4x4': '4x4',
        'nup_preview': 'Podgląd:',
        'nup_preview_info': '{0} stron → {1} stron na arkusz → {2} arkuszy\nUkład: {3}',
        'nup_order': 'Kolejność:',
        'nup_order_horizontal': 'Poziomo (wierszami)',
        'nup_order_vertical': 'Pionowo (kolumnami)',
        'nup_order_horizontal_reverse': 'Poziomo odwrotnie',
        'nup_order_vertical_reverse': 'Pionowo odwrotnie',
        'nup_range': 'Zakres stron:',
        'nup_all_pages': 'Wszystkie strony',
        'nup_custom_range': 'Zakres niestandardowy',
        'nup_from': 'Od:',
        'nup_to': 'Do:',
        'nup_options': 'Opcje:',
        'nup_margins': 'Marginesy:',
        'nup_margin_between': 'Odstęp między stronami:',
        'nup_page_numbers': 'Wstaw numery stron',
        'nup_target_folder': 'Folder docelowy:',
        'nup_browse': 'Przeglądaj...',
        'nup_select_folder': 'Wybierz folder docelowy',
        'nup_create': 'Utwórz',
        'nup_start': 'Rozpoczęcie N-Up...',
        'nup_progress': 'Tworzenie N-Up...',
        'nup_success': 'N-Up został pomyślnie utworzony!\n\nZapisano jako:\n{0}\n\nCzy chcesz otworzyć nowy PDF?',
        'nup_complete': 'N-Up zakończony',
        'nup_cancel': 'Anulowano N-Up',
        'nup_error_format': 'Błąd podczas N-Up:\n\n{0}',
        'filename_nup_suffix': '_nup',

        ###==============================================
        ### 101. SEITENGRÖSSE ÄNDERN A3 A4 A5 ...
        ###==============================================
        'pagesize_title': 'Zmień rozmiar strony',
        'pagesize_menu': 'Zmień rozmiar strony',
        'pagesize_info': 'Zmienia rozmiar strony PDF.\n\nZawartość jest automatycznie dostosowywana do nowego rozmiaru.',
        'pagesize_format': 'Format:',
        'pagesize_select': 'Wybierz standardowy format:',
        'pagesize_custom': 'Rozmiar niestandardowy:',
        'pagesize_width': 'Szerokość:',
        'pagesize_height': 'Wysokość:',
        'pagesize_orientation': 'Orientacja:',
        'pagesize_portrait': 'Pionowa',
        'pagesize_landscape': 'Pozioma',
        'pagesize_scale_options': 'Opcje skalowania:',
        'pagesize_fit': 'Dopasuj (zachowaj proporcje)',
        'pagesize_stretch': 'Rozciągnij (zniekształć)',
        'pagesize_center': 'Wyśrodkuj (oryginalny rozmiar)',
        'pagesize_range': 'Zakres stron:',
        'pagesize_all_pages': 'Wszystkie strony',
        'pagesize_custom_range': 'Zakres niestandardowy',
        'pagesize_from': 'Od:',
        'pagesize_to': 'Do:',
        'pagesize_target_folder': 'Folder docelowy:',
        'pagesize_browse': 'Przeglądaj...',
        'pagesize_select_folder': 'Wybierz folder docelowy',
        'pagesize_apply': 'Zastosuj',
        'pagesize_start': 'Rozpoczęcie zmiany rozmiaru stron...',
        'pagesize_progress': 'Zmiana rozmiaru stron w toku...',
        'pagesize_success': 'Rozmiar stron został pomyślnie zmieniony!\n\nZapisano jako:\n{0}\n\nCzy chcesz otworzyć nowy PDF?',
        'pagesize_complete': 'Zmiana rozmiaru stron zakończona',
        'pagesize_cancel': 'Anulowano zmianę rozmiaru stron',
        'pagesize_error_format': 'Błąd podczas zmiany rozmiaru stron:\n\n{0}',
        'pagesize_preview_info': 'Nowy rozmiar: {0} x {1} pt',
        'filename_pagesize_suffix': '_nowy_rozmiar',

        # ============================================
        # 102. PDF INFO Menü
        # ============================================
        'pdf_info_title': 'Informacje o PDF',
        'pdf_info_menu': 'Pokaż informacje o PDF',
        'pdf_info_voice': 'Wyświetlanie informacji o PDF',
        'pdf_info_error': 'Błąd podczas wyświetlania informacji o PDF:\n\n{0}',

        # ============================================
        # 103. SHORTCUT INFO
        # ============================================
        "show_shortcuts": "Pokaż skróty klawiaturowe",
        "shortcuts_dialog_title": "Skróty klawiaturowe",
        "show_shortcuts_text": "<style>td { padding: 3px 20px 3px 5px; } th { padding: 12px 0 6px 0; font-size: 15px; } table { border-collapse: collapse; }</style><table>"
        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📁 PLIK</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+O</td><td style='padding:3px 5px;'>Otwórz PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+W</td><td style='padding:3px 5px;'>Zamknij PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+S</td><td style='padding:3px 5px;'>Zapisz jako...</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+P</td><td style='padding:3px 5px;'>Zabezpiecz dokument</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+P</td><td style='padding:3px 5px;'>Drukuj</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+P</td><td style='padding:3px 5px;'>Drukuj natychmiast (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Q</td><td style='padding:3px 5px;'>Zakończ aplikację</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📤 EKSPORT</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+E</td><td style='padding:3px 5px;'>Eksportuj jako Pages</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+W</td><td style='padding:3px 5px;'>Eksportuj jako DOCX</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+T</td><td style='padding:3px 5px;'>Eksportuj jako TXT</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Eksportuj jako obrazy (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+X</td><td style='padding:3px 5px;'>Wyodrębnij obrazy</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ PRZETWARZANIE DOKUMENTÓW</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+N</td><td style='padding:3px 5px;'>N-Up (wiele stron)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+A</td><td style='padding:3px 5px;'>Konwersja do PDF/A (macOS)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+F</td><td style='padding:3px 5px;'>Spłaszcz PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+L</td><td style='padding:3px 5px;'>Nakładanie PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+O</td><td style='padding:3px 5px;'>Optymalizuj PDF</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✏️ EDYCJA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+F</td><td style='padding:3px 5px;'>Szukaj</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+B</td><td style='padding:3px 5px;'>Dodaj zakładkę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Zarządzaj zakładkami</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Down</td><td style='padding:3px 5px;'>Następna zakładka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Up</td><td style='padding:3px 5px;'>Poprzednia zakładka</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+R</td><td style='padding:3px 5px;'>Wykonaj OCR</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📄 ZARZĄDZANIE STRONAMI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Obróć bieżącą stronę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Obróć wszystkie strony</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+0</td><td style='padding:3px 5px;'>Wyrównaj bieżącą stronę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+0</td><td style='padding:3px 5px;'>Wyrównaj wszystkie strony</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Usuń strony</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Wyodrębnij strony</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+I</td><td style='padding:3px 5px;'>Wstaw strony</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+M</td><td style='padding:3px 5px;'>Przesuń strony</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+J</td><td style='padding:3px 5px;'>Scal PDF-y</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+S</td><td style='padding:3px 5px;'>Zmień rozmiar strony</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>📎 WSTAW</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+T</td><td style='padding:3px 5px;'>Wstaw tekst</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+X</td><td style='padding:3px 5px;'>Wstaw krzyżyk</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+1</td><td style='padding:3px 5px;'>Wstaw podpis 1</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+2</td><td style='padding:3px 5px;'>Wstaw podpis 2</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Wstaw obraz</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+R</td><td style='padding:3px 5px;'>Wstaw prostokąt</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+E</td><td style='padding:3px 5px;'>Wstaw elipsę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+L</td><td style='padding:3px 5px;'>Wstaw linię</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+A</td><td style='padding:3px 5px;'>Wstaw strzałkę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Num</td><td style='padding:3px 5px;'>Wstaw numery stron</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Znak wodny (tekst)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+Alt+W</td><td style='padding:3px 5px;'>Znak wodny (obraz)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⬛ WYCINKI</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+B</td><td style='padding:3px 5px;'>Wycinek (czarny)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+W</td><td style='padding:3px 5px;'>Wycinek (biały)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+R</td><td style='padding:3px 5px;'>Zastosuj wszystkie wycinki</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>✂️ ZAAWANSOWANE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+C</td><td style='padding:3px 5px;'>Przytnij PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Edytuj metadane</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>👁️ WIDOK</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Shift+D</td><td style='padding:3px 5px;'>Przełącz tryb jasny/ciemny</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+T</td><td style='padding:3px 5px;'>Pokaż okno tekstowe</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+1</td><td style='padding:3px 5px;'>Szerokość strony (zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+2</td><td style='padding:3px 5px;'>Dwie strony (zoom)</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+3</td><td style='padding:3px 5px;'>Przegląd (zoom)</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>⚙️ USTAWIENIA</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+K</td><td style='padding:3px 5px;'>Zarządzanie hasłami</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+O</td><td style='padding:3px 5px;'>Ustawienia OCR</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+S</td><td style='padding:3px 5px;'>Ustawienia podpisów</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+F</td><td style='padding:3px 5px;'>Formatowanie nazw plików</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+E</td><td style='padding:3px 5px;'>Eksportuj ustawienia</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+Shift+I</td><td style='padding:3px 5px;'>Importuj ustawienia</td></tr>"

        "<tr><th colspan='2' style='text-align:left;font-size:16px;padding-top:18px;padding-bottom:6px;'>ℹ️ INFORMACJE</th></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>Ctrl+Alt+I</td><td style='padding:3px 5px;'>Pokaż informacje o PDF</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F2</td><td style='padding:3px 5px;'>Włącz/wyłącz mowę</td></tr>"
        "<tr><td style='padding:3px 25px 3px 5px;'>F1</td><td style='padding:3px 5px;'>Ustaw fokus na pasku menu</td></tr>"
        "</table>",

        # ============================================
        # 104. UPDATE
        # ============================================
        "update_available_title": "Dostępna jest nowa wersja",
        "update_available_message": "Dostępna jest nowa wersja <b>{0}</b>.\n\nOdwiedź stronę wydań, aby pobrać aktualizację:\n{1}",
        "update_available_voice": "Dostępna jest nowa wersja {0}. Pobierz aktualizację ze strony GitHub.",
        "update_open_release": "Otwórz stronę wydań",

        # ============================================
        # 105. DOWNLOAD TRANSLATIONS
        # ============================================
        "download_all_translations": "Pobierz wszystkie tłumaczenia",
        "ask_download_all_translations": """Oprócz niemieckiego, angielskiego i wietnamskiego dostępnych jest jeszcze {total_languages} innych języków GUI.\n\nCzy pobrać / zaktualizować je?\n\nUwaga:\nNiepotrzebne języki możesz później usunąć ręcznie z katalogu:\n{translations_path}\n\nJeśli anulujesz, możesz później pobrać języki GUI przez menu 'Narzędzia → Aktualizuj tłumaczenia'.""",
        "menu_update_translations": "Aktualizuj tłumaczenia",
        "translations_updated": "Zaktualizowano tłumaczenia",
        "translations_update_success": "Pomyślnie zaktualizowano {} tłumaczeń ({} nowych, {} zaktualizowanych).",
        "translations_update_error": "Błąd podczas aktualizacji tłumaczeń",
        "translations_update_no_changes": "Wszystkie tłumaczenia są już aktualne.",
        "translations_update_offline": "Brak połączenia z internetem. Nie można zaktualizować tłumaczeń.",
        "translations_update_in_progress": "Aktualizacja tłumaczeń w tle...",
        "translations_downloading": "Pobieranie tłumaczeń...",
        "translations_path_hint": "Katalog użytkownika dla tłumaczeń",
        "translations_update_not_available_title": "Aktualizacja niedostępna",
        "translations_update_not_available_message": """Aktualizacja tłumaczeń jest dostępna tylko w wersji zainstalowanej.\n\nW trybie deweloperskim tłumaczenia są już aktualne.""",
        "translations_update_no_internet_title": "Brak połączenia z internetem",
        "translations_update_no_internet_message": """Nie można nawiązać połączenia z internetem.\n\nTłumaczenia nie mogą być pobrane z GitHub.\n\nMożliwe rozwiązania:
        • Sprawdź połączenie internetowe
        • Tymczasowo wyłącz zaporę sieciową
        • Spróbuj ponownie później
        \nMożesz również pobrać tłumaczenia ręcznie z GitHub:
        https://github.com/BinhDiez64/PDFDarkView/tree/main/translations""",
        "translations_update_in_progress_title": "Aktualizacja już trwa",
        "btn_retry": "Spróbuj ponownie",

        # ============================================
        # 106. WILLKOMMEN
        # ============================================
        "welcome_title": "Witamy w PDF Dark View",
        "welcome_title_not_supported": "Witamy w PDF Dark View",
        "welcome_message": "Witamy w PDF Dark View!\n\nJęzyk systemowy został rozpoznany jako '{language}'.\nCzy chcesz używać tego języka w interfejsie?\n\nJęzyk możesz zmienić w dowolnym momencie w 'Ustawienia → Język'.",
        "welcome_message_language_not_available": "Witamy w PDF Dark View!\n\nJęzyk systemowy został rozpoznany jako '{language}'.\nTen język nie jest jeszcze zainstalowany.\n\nCzy chcesz teraz pobrać tłumaczenia dla {language} z GitHub?\n\n(Język zostanie automatycznie ustawiony jako interfejs.)",
        "welcome_message_language_not_supported": "Witamy w PDF Dark View!\n\nJęzyk systemowy został rozpoznany jako '{language}'.\nNiestety, obecnie nie ma tłumaczenia dla tego języka.\n\nInterfejs zostanie wyświetlony w języku {fallback_language}.\n\nJęzyk możesz zmienić w dowolnym momencie w 'Ustawienia → Język'.\nJeśli chcesz, możesz samodzielnie dodać tłumaczenie dla swojego języka:\nhttps://github.com/BinhDiez64/PDFDarkView",
        "welcome_use_system_language": "Tak, użyj języka systemowego",
        "welcome_keep_english": "Nie, zachowaj angielski",
        "welcome_download_language": "Tak, pobierz {language}",

        # ============================================
        # 107. ZULETZT VERWENDETE PFADE
        # ============================================

        'menu_recent': 'Ostatnio używane',
        'menu_recent_dirs': 'Katalogi...',
        'menu_recent_files': 'Pliki...',
        'recent_manage': 'Zarządzaj...',
        # Recent Paths - Einstellungen
        'recent_enable_tracking': 'Zapisuj ostatnio używane ścieżki (ochrona danych)',
        'recent_enable_info': 'Wyłącz tę opcję, aby nie zapisywać ścieżek',
        'recent_tracking_disabled': 'Śledzenie ścieżek wyłączone',
        'recent_enabled': 'włączone',
        'recent_disabled': 'wyłączone',
        'recent_tracking_status': 'Śledzenie ścieżek {0}',
        # Recent Paths - Dialog
        'recent_dialog_title': 'Ostatnio używane ścieżki',
        'recent_tab_directories': 'Katalogi',
        'recent_tab_files': 'Pliki',
        'recent_dirs_instruction': 'Dwuklik, aby otworzyć okno wyboru pliku w katalogu',
        'recent_files_instruction': 'Dwuklik, aby bezpośrednio otworzyć PDF',
        'recent_no_directories': '(brak zapisanych katalogów)',
        'recent_no_files': '(brak zapisanych plików)',
        'recent_default_current': '⭐ Domyślny: {0}',
        'recent_set_as_default': '⭐ Ustaw jako domyślny',
        'recent_default_set_title': 'Ustawiono domyślny katalog',
        'recent_default_set_message': 'Katalog "{0}" został ustawiony jako domyślny do otwierania PDF-ów.',
        'recent_default_set_voice': 'Ustawiono domyślny katalog',
        'recent_directory_not_found': 'Nie znaleziono katalogu',
        'recent_file_not_found': 'Nie znaleziono pliku',
        'recent_remove_selected': 'Usuń',
        'recent_remove_title': 'Usuń ścieżkę',
        'recent_remove_confirm': 'Czy na pewno chcesz usunąć ścieżkę "{0}" z listy?',
        'recent_path_removed': 'Ścieżka została usunięta',
        'recent_clear_all': 'Usuń wszystkie',
        'recent_clear_title': 'Usuń wszystkie ścieżki',
        'recent_clear_confirm_type': 'Czy na pewno chcesz usunąć wszystkie {0}?',
        'recent_cleared': 'Lista została wyczyszczona',
        'recent_path_not_found_title': 'Nie znaleziono ścieżki',
        'recent_path_not_found_message': 'Ścieżka "{0}" już nie istnieje.',
        'recent_open_file': 'Otwórz plik',
        'btn_open_recent': 'Otwórz',
        'recent_open_file_question': 'Czy chcesz otworzyć "{0}" jako PDF?',
        'recent_not_pdf': 'Wybrany plik nie jest PDF.',
        'recent_more_entries': 'Więcej wpisów...',
        'btn_remove': 'Usuń',
        'btn_clear': 'Usuń wszystkie',
        # Recent Paths - Context Menu
        'recent_context_open': 'Otwórz',
        'recent_context_reveal': 'Pokaż w Finderze',
        'recent_context_set_default': '⭐ Ustaw jako domyślny',
        'recent_context_open_terminal': '💻 Otwórz terminal',
        'recent_context_file_info': 'Informacje o pliku',
        'recent_context_open_with_default': '📄 Otwórz domyślną aplikacją',
        'recent_context_remove': 'Usuń z listy',
        'recent_context_clear_all': 'Usuń wszystkie',

        # Recent Paths - File Info
        'recent_file_info_title': 'Informacje o pliku',
        'recent_file_info_name': 'Nazwa',
        'recent_file_info_path': 'Ścieżka',
        'recent_file_info_size': 'Rozmiar',
        'recent_file_info_modified': 'Zmodyfikowany',
        'recent_file_info_pages': 'Strony',

        # Recent Paths - Errors
        'recent_error_reveal': 'Błąd podczas otwierania w Finderze',
        'recent_error_terminal': 'Błąd podczas otwierania terminala',
        'recent_error_info': 'Błąd podczas pobierania informacji o pliku',
        'open_user_data_folder': 'Pokaż katalog danych użytkownika',

        # ============================================
        # 108. GERADE UNGERADE SEITEN LÖSCHEN
        # ============================================
        "pages_delete_even": "Usuń wszystkie parzyste strony",
        "pages_delete_odd":  "Usuń wszystkie nieparzyste strony",
        "progress_even_pages": "Usuwanie parzystych stron",
        "progress_odd_pages": "Usuwanie nieparzystych stron",
        "progress_mark_delete_even": "Oznaczono {} parzyste strony do usunięcia",
        "progress_mark_delete_odd":  "Oznaczono {} nieparzyste strony do usunięcia",

        # ============================================
        # 109. PROGRAMM BEENDEN
        # ============================================
        "app_quitting": "Zamykanie programu",

    }
